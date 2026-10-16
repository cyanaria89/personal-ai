"""Frontend Primary/Secondary candidates; shared BGE-M3/cosine ranking.

Stream both existing JSON indexes once per file revision. Cache only allowed
chunks with contiguous float64 arrays, preserving original numeric values.
No re-embedding, generated search database, or Agent state is involved.
"""

from array import array
from functools import lru_cache
from pathlib import Path
import time

from rag.db_retriever import (
    EMBED_MODEL, INDEX_PATH as BACKEND_INDEX, PROJECT_ROOT, allowed_domain_rules,
    classify_source, format_db_context, search_domain_context,
)
from rag.frontend_indexer import validate_embedding

FRONTEND_INDEX = PROJECT_ROOT / "rag/indexes/frontend_index.json"


def iter_index(path):
    import ijson
    with Path(path).open("rb") as stream:
        model = next(ijson.items(stream, "model"), None)
        if model != EMBED_MODEL:
            raise ValueError(f"Unexpected embedding model in {path}: {model}")
        stream.seek(0)
        yield from ijson.items(stream, "chunks.item", use_float=True)


@lru_cache(maxsize=1)
def _load_candidates(front_stamp, backend_stamp):
    started = time.perf_counter()
    allowed = allowed_domain_rules("frontend")
    candidates = []
    unknown = set()
    for stamp in (front_stamp, backend_stamp):
        for chunk in iter_index(stamp[0]):
            domain = classify_source(chunk.get("source", ""))
            if domain is None:
                unknown.add(str(chunk.get("source", "")))
            elif domain in allowed:
                validate_embedding(chunk.get("embedding"))
                chunk["embedding"] = array("d", chunk["embedding"])
                candidates.append(chunk)
    for source in sorted(unknown):
        print(f"[Frontend RAG 경고] 미분류 문서 제외: {source}")
    print(f"[Frontend RAG] 인덱스 cache 생성: sources={len({c['source'] for c in candidates})}, "
          f"chunks={len(candidates)}, {time.perf_counter() - started:.2f}초")
    return tuple(candidates)


def frontend_candidates():
    def stamp(path):
        stat = path.stat()
        return str(path.resolve()), stat.st_mtime_ns, stat.st_size
    return _load_candidates(stamp(FRONTEND_INDEX), stamp(BACKEND_INDEX))


def search_frontend_context(query: str, top_k: int = 3):
    if not query.strip():
        return []
    return search_domain_context(query, agent="frontend", top_k=top_k,
                                 chunks=frontend_candidates())


def format_frontend_context(results):
    return format_db_context(results, domain="Frontend Domain")
