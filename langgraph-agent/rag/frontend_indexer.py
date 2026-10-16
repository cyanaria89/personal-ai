"""Bounded, resumable Frontend indexing; no Agent or retrieval-policy connection.

Run from langgraph-agent: python -m rag.frontend_indexer --sample-only
Then: python -m rag.frontend_indexer
The SQLite checkpoint retains completed batches after interruption. Source or
splitter changes invalidate the checkpoint rather than mixing different inputs.
"""

from __future__ import annotations

import argparse
from collections import Counter
from contextlib import closing, contextmanager
import fcntl
import hashlib
import inspect
import json
import math
from pathlib import Path
import resource
import shutil
import sqlite3
import tempfile
import time

from rag.db_retriever import (
    EMBED_MODEL, INDEX_PATH as DB_INDEX_PATH, MAX_CHUNK_LENGTH,
    MIN_CHUNK_LENGTH, PROJECT_ROOT, cosine_similarity, embed_texts, split_markdown,
)


SOURCE_DIRS = (PROJECT_ROOT / "data/rag-source/frontend-domain",
               PROJECT_ROOT / "data/rag-source/frontend-foundation")
INDEX_PATH = PROJECT_ROOT / "rag/indexes/frontend_index.json"
WORK_DIR = PROJECT_ROOT / "rag/indexes/frontend_index.work"
DIMENSIONS = 1024
BATCH_SIZE = 8


def sha256(path: Path) -> str:
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def discover_documents(source_dirs=SOURCE_DIRS, root=PROJECT_ROOT) -> list[dict]:
    documents = []
    seen = set()
    for directory in source_dirs:
        if not directory.is_dir():
            raise FileNotFoundError(f"Frontend source directory missing: {directory}")
        for path in sorted(directory.rglob("*.md")):
            resolved = path.resolve()
            if resolved in seen:
                continue
            seen.add(resolved)
            # Preserve the symlink-relative source path, not the resolved path.
            text = path.read_text(encoding="utf-8").strip()
            if not text:
                raise ValueError(f"Empty Frontend document: {path}")
            documents.append({"source": path.relative_to(root).as_posix(),
                              "path": str(path), "sha256": sha256(path)})
    if not documents:
        raise ValueError("No Frontend documents")
    return sorted(documents, key=lambda document: document["source"])


def document_chunks(document):
    path = Path(document["path"])
    if sha256(path) != document["sha256"]:
        raise ValueError(f"Source changed during indexing: {path}")
    chunks = split_markdown(document["source"], path.read_text(encoding="utf-8").strip())
    if not chunks:
        raise ValueError(f"No chunks for document: {path}")
    return chunks


def validate_embedding(vector):
    if not isinstance(vector, list) or len(vector) != DIMENSIONS:
        raise ValueError("Embedding must have 1024 dimensions")
    if any(isinstance(value, bool) or not isinstance(value, (int, float))
           or not math.isfinite(value) for value in vector):
        raise ValueError("Embedding contains non-finite or non-numeric values")
    if not any(vector):
        raise ValueError("Zero embedding")


def iter_index_chunks(path=INDEX_PATH):
    """Read our line-delimited JSON array without materializing all vectors.

    The file remains a standard {model, chunks} JSON object, compatible with
    json.load. Each chunk occupies one physical line; embedded newlines escape.
    """
    with Path(path).open(encoding="utf-8") as stream:
        if stream.readline().strip() != "{":
            raise ValueError("Invalid index header")
        model_line = stream.readline().strip()
        if not model_line.endswith(",") or json.loads("{" + model_line[:-1] + "}") != {"model": EMBED_MODEL}:
            raise ValueError("Unexpected embedding model")
        if stream.readline().strip() != '"chunks": [':
            raise ValueError("Invalid chunks header")
        previous_comma = True
        count = 0
        for line in stream:
            line = line.strip()
            if line == "]":
                if count and previous_comma:
                    raise ValueError("Trailing comma in index")
                if stream.readline().strip() != "}" or stream.read().strip():
                    raise ValueError("Invalid index footer")
                return
            if not previous_comma:
                raise ValueError("Missing chunk separator")
            previous_comma = line.endswith(",")
            chunk = json.loads(line[:-1] if previous_comma else line)
            if not isinstance(chunk, dict) or set(chunk) != {"source", "heading", "content", "embedding"}:
                raise ValueError("Invalid chunk fields")
            if any(not isinstance(chunk[key], str) for key in ("source", "heading", "content")):
                raise ValueError("Invalid chunk metadata")
            if not chunk["source"] or not chunk["content"]:
                raise ValueError("Empty chunk metadata")
            validate_embedding(chunk["embedding"])
            count += 1
            yield chunk
        raise ValueError("Truncated index")


def validate_index(path, documents):
    """Check every chunk against the original document and splitter order."""
    actual = iter(iter_index_chunks(path))
    counts = Counter()
    for document in documents:
        for expected in document_chunks(document):
            chunk = next(actual, None)
            if chunk is None or any(chunk[key] != expected[key] for key in expected):
                raise ValueError(f"Missing, duplicate or altered chunk: {document['source']}")
            counts[chunk["source"]] += 1
    if next(actual, None) is not None:
        raise ValueError("Unexpected extra chunks")
    return {"documents": len(counts), "chunks": sum(counts.values()),
            "bytes": Path(path).stat().st_size, "sha256": sha256(Path(path))}


def resources():
    info = {}
    for line in Path("/proc/meminfo").read_text().splitlines():
        key, value = line.split(":", 1)
        if key in ("MemAvailable", "SwapFree"):
            info[key + "_bytes"] = int(value.split()[0]) * 1024
    info["python_peak_rss_bytes"] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024
    rss = 0
    for entry in Path("/proc").iterdir():
        if not entry.name.isdigit():
            continue
        try:
            if "ollama" not in (entry / "comm").read_text().lower():
                continue
            for line in (entry / "status").read_text().splitlines():
                if line.startswith("VmRSS:"):
                    rss += int(line.split()[1]) * 1024
        except (OSError, ProcessLookupError):
            continue
    info["ollama_observed_rss_bytes"] = rss
    return info


def guard_resources(directory, required_bytes=512 * 1024**2):
    if resources()["MemAvailable_bytes"] < 2 * 1024**3:
        raise RuntimeError("Available memory below 2 GiB; checkpoint retained")
    if shutil.disk_usage(directory).free < required_bytes:
        raise RuntimeError("Insufficient disk space; checkpoint retained")


@contextmanager
def checkpoint(documents, work_dir):
    work_dir.mkdir(parents=True, exist_ok=True)
    with (work_dir / "build.lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        with closing(sqlite3.connect(work_dir / "checkpoint.sqlite3")) as db:
            db.execute("PRAGMA cache_size=-8192")
            db.execute("CREATE TABLE IF NOT EXISTS metadata (key TEXT PRIMARY KEY, value TEXT)")
            signature = json.dumps({"documents": documents, "model": EMBED_MODEL,
                                    "dimensions": DIMENSIONS,
                                    "chunk_limits": [MIN_CHUNK_LENGTH, MAX_CHUNK_LENGTH],
                                    "splitter": inspect.getsource(split_markdown)}, sort_keys=True)
            prior = db.execute("SELECT value FROM metadata WHERE key='manifest'").fetchone()
            if prior and prior[0] != signature:
                raise ValueError("Checkpoint inputs changed; use a fresh work directory")
            db.execute("INSERT OR IGNORE INTO metadata VALUES ('manifest', ?)", (signature,))
            db.execute("CREATE TABLE IF NOT EXISTS documents (source TEXT PRIMARY KEY)")
            db.execute("CREATE TABLE IF NOT EXISTS chunks (source TEXT, ordinal INTEGER, heading TEXT, "
                       "content TEXT, embedding TEXT, PRIMARY KEY(source, ordinal))")
            db.execute("CREATE INDEX IF NOT EXISTS pending ON chunks(source, ordinal) WHERE embedding IS NULL")
            db.commit()
            for document in documents:
                if db.execute("SELECT 1 FROM documents WHERE source=?", (document["source"],)).fetchone():
                    continue
                # One document at a time; one transaction makes staging resumable.
                with db:
                    for ordinal, chunk in enumerate(document_chunks(document)):
                        db.execute("INSERT INTO chunks VALUES (?, ?, ?, ?, NULL)",
                                   (chunk["source"], ordinal, chunk["heading"], chunk["content"]))
                    db.execute("INSERT INTO documents VALUES (?)", (document["source"],))
            yield db


def embed_batch(db, rows):
    if not rows:
        return
    embeddings = embed_texts([row[2] for row in rows])
    if len(embeddings) != len(rows):
        raise ValueError("Embedding count mismatch")
    for vector in embeddings:
        validate_embedding(vector)
    with db:
        for row, vector in zip(rows, embeddings):
            db.execute("UPDATE chunks SET embedding=? WHERE source=? AND ordinal=?",
                       (json.dumps(vector, separators=(",", ":"), allow_nan=False), row[0], row[1]))


def build_frontend_index(*, sample_only=False, target=INDEX_PATH, work_dir=WORK_DIR,
                         source_dirs=SOURCE_DIRS, root=PROJECT_ROOT, pause=0.1):
    target, work_dir = Path(target), Path(work_dir)
    if target.resolve() == DB_INDEX_PATH.resolve():
        raise ValueError("Refusing to write the DB index")
    target.parent.mkdir(parents=True, exist_ok=True)
    documents = discover_documents(source_dirs, root)
    started = time.perf_counter()
    db_hash = sha256(DB_INDEX_PATH) if DB_INDEX_PATH.exists() else None
    with checkpoint(documents, work_dir) as db:
        total = db.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]
        print(f"[Frontend Index] documents={len(documents)}, chunks={total}", flush=True)
        guard_resources(target.parent)
        # Keep sample embeddings in the checkpoint; full build never repeats them.
        if not db.execute("SELECT 1 FROM chunks WHERE embedding IS NOT NULL").fetchone():
            for query in (
                "SELECT source,ordinal,content FROM chunks ORDER BY source,ordinal LIMIT 8",
                "SELECT source,ordinal,content FROM chunks WHERE embedding IS NULL "
                "ORDER BY length(content) DESC,source,ordinal LIMIT 8",
            ):
                embed_batch(db, db.execute(query).fetchall())
                time.sleep(pause)
        sample = db.execute("SELECT avg(length(embedding)+length(content)*3+length(source)+length(heading)*3+100) "
                            "FROM chunks WHERE embedding IS NOT NULL").fetchone()[0]
        estimated_bytes = int(sample * total)
        report = {"documents": len(documents), "chunks": total,
                  "estimated_json_bytes": estimated_bytes,
                  "estimated_checkpoint_plus_json_bytes": estimated_bytes * 3,
                  "elapsed_seconds": round(time.perf_counter() - started, 2), **resources()}
        print("[Frontend Index sample] " + json.dumps(report), flush=True)
        (work_dir / "sample_report.json").write_text(json.dumps(report, indent=2))
        if sample_only:
            return report
        guard_resources(target.parent, estimated_bytes * 3 + 512 * 1024**2)
        if target.exists():
            previous = db.execute("SELECT value FROM metadata WHERE key='index_sha256'").fetchone()
            if previous and previous[0] == sha256(target):
                return validate_index(target, documents)
        while True:
            guard_resources(target.parent)
            rows = db.execute("SELECT source,ordinal,content FROM chunks WHERE embedding IS NULL "
                              "ORDER BY source,ordinal LIMIT ?", (BATCH_SIZE,)).fetchall()
            if not rows:
                break
            embed_batch(db, rows)
            done = db.execute("SELECT COUNT(*) FROM chunks WHERE embedding IS NOT NULL").fetchone()[0]
            if done % 128 < BATCH_SIZE or done == total:
                print(f"[Frontend Index] {done}/{total} " + json.dumps(resources()), flush=True)
            time.sleep(pause)
        # Temp file is on the target filesystem. Existing index survives all errors
        # until streaming validation and the final DB hash check have succeeded.
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=target.parent,
                                         prefix=".frontend_index.", suffix=".json", delete=False) as stream:
            pending = Path(stream.name)
            stream.write('{\n"model": ' + json.dumps(EMBED_MODEL) + ',\n"chunks": [\n')
            for number, row in enumerate(db.execute(
                "SELECT source,heading,content,embedding FROM chunks ORDER BY source,ordinal"), 1):
                chunk = dict(zip(("source", "heading", "content", "embedding"), row))
                chunk["embedding"] = json.loads(chunk["embedding"])
                stream.write(json.dumps(chunk, ensure_ascii=False, allow_nan=False, separators=(",", ":")))
                stream.write(",\n" if number < total else "\n")
            stream.write("]\n}\n")
            stream.flush()
            import os
            os.fsync(stream.fileno())
        try:
            result = validate_index(pending, documents)
            if db_hash is not None and sha256(DB_INDEX_PATH) != db_hash:
                raise RuntimeError("DB index changed during build; not publishing")
            pending.replace(target)
            with db:
                db.execute("INSERT OR REPLACE INTO metadata VALUES ('index_sha256', ?)", (result["sha256"],))
        finally:
            pending.unlink(missing_ok=True)
        result.update(elapsed_seconds=round(time.perf_counter() - started, 2), **resources())
        (work_dir / "build_report.json").write_text(json.dumps(result, indent=2))
        print("[Frontend Index complete] " + json.dumps(result), flush=True)
        return result


def search_index(query, top_k=3, path=INDEX_PATH):
    """Index-only smoke search; not connected to any Agent."""
    if not query.strip():
        return []
    vector = embed_texts([query])[0]
    validate_embedding(vector)
    best = []
    for chunk in iter_index_chunks(path):
        score = cosine_similarity(vector, chunk.pop("embedding"))
        best.append(dict(chunk, score=score))
        best.sort(key=lambda item: item["score"], reverse=True)
        del best[top_k:]
    return best


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sample-only", action="store_true")
    parser.add_argument("--query", help="Search the generated index without invoking an Agent")
    args = parser.parse_args()
    if args.query:
        for result in search_index(args.query):
            print(json.dumps(result, ensure_ascii=False))
    else:
        build_frontend_index(sample_only=args.sample_only)
