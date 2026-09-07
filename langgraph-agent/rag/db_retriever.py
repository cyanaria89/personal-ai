from __future__ import annotations

import json
import math
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(__file__).resolve().parent.parent

DB_SOURCE_DIRS = [
    PROJECT_ROOT / "data" / "rag-source" / "backend-domain",
    PROJECT_ROOT / "data" / "rag-source" / "backend-foundation",
]

INDEX_PATH = (
    PROJECT_ROOT
    / "rag"
    / "indexes"
    / "db_index.json"
)

OLLAMA_EMBED_URL = "http://localhost:11434/api/embed"
EMBED_MODEL = "bge-m3"

MIN_CHUNK_LENGTH = 80
MAX_CHUNK_LENGTH = 1800


def read_markdown_files() -> list[dict[str, str]]:
    """DB RAG 원본 폴더에서 Markdown 문서를 읽는다."""

    documents: list[dict[str, str]] = []

    for source_dir in DB_SOURCE_DIRS:
        if not source_dir.exists():
            print(
                f"[DB RAG 경고] 원본 폴더를 찾을 수 없습니다: "
                f"{source_dir}"
            )
            continue

        for path in sorted(source_dir.rglob("*.md")):
            try:
                text = path.read_text(
                    encoding="utf-8",
                ).strip()
            except UnicodeDecodeError:
                print(
                    f"[DB RAG 경고] UTF-8로 읽을 수 없습니다: "
                    f"{path}"
                )
                continue

            if not text:
                continue

            documents.append(
                {
                    "source": str(
                        path.relative_to(PROJECT_ROOT)
                    ),
                    "text": text,
                }
            )

    return documents


def split_markdown(
    source: str,
    text: str,
) -> list[dict[str, str]]:
    """
    Markdown 문서를 제목과 빈 줄을 기준으로 분할한다.

    너무 긴 조각은 MAX_CHUNK_LENGTH 기준으로 다시 나눈다.
    """

    chunks: list[dict[str, str]] = []

    current_heading = ""
    current_parts: list[str] = []

    def flush() -> None:
        nonlocal current_parts

        content = "\n\n".join(
            part.strip()
            for part in current_parts
            if part.strip()
        ).strip()

        current_parts = []

        if len(content) < MIN_CHUNK_LENGTH:
            return

        full_content = content

        for start in range(
            0,
            len(full_content),
            MAX_CHUNK_LENGTH,
        ):
            piece = full_content[
                start:start + MAX_CHUNK_LENGTH
            ].strip()

            if len(piece) < MIN_CHUNK_LENGTH:
                continue

            chunks.append(
                {
                    "source": source,
                    "heading": current_heading,
                    "content": piece,
                }
            )

    for block in text.split("\n\n"):
        stripped = block.strip()

        if not stripped:
            continue

        first_line = stripped.splitlines()[0]

        if first_line.startswith("#"):
            flush()
            current_heading = first_line

            remaining_lines = stripped.splitlines()[1:]
            remaining_text = "\n".join(remaining_lines).strip()

            if remaining_text:
                current_parts.append(remaining_text)
        else:
            current_parts.append(stripped)

        current_length = sum(
            len(part)
            for part in current_parts
        )

        if current_length >= MAX_CHUNK_LENGTH:
            flush()

    flush()

    return chunks


def embed_texts(
    texts: list[str],
) -> list[list[float]]:
    """Ollama BGE-M3를 사용해 문자열 목록을 임베딩한다."""

    if not texts:
        return []

    payload = json.dumps(
        {
            "model": EMBED_MODEL,
            "input": texts,
        }
    ).encode("utf-8")

    request = urllib.request.Request(
        OLLAMA_EMBED_URL,
        data=payload,
        headers={
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(
            request,
            timeout=300,
        ) as response:
            data: dict[str, Any] = json.loads(
                response.read().decode("utf-8")
            )
    except urllib.error.URLError as exc:
        raise RuntimeError(
            "Ollama 임베딩 API 호출에 실패했습니다. "
            "Ollama 실행 상태와 bge-m3 설치 여부를 확인하세요."
        ) from exc

    embeddings = data.get("embeddings")

    if not isinstance(embeddings, list):
        raise RuntimeError(
            "Ollama 응답에 embeddings 배열이 없습니다."
        )

    return embeddings


def cosine_similarity(
    vector_a: list[float],
    vector_b: list[float],
) -> float:
    """두 벡터의 코사인 유사도를 계산한다."""

    if len(vector_a) != len(vector_b):
        raise ValueError(
            "임베딩 벡터 길이가 서로 다릅니다."
        )

    dot_product = sum(
        a * b
        for a, b in zip(vector_a, vector_b)
    )

    norm_a = math.sqrt(
        sum(value * value for value in vector_a)
    )
    norm_b = math.sqrt(
        sum(value * value for value in vector_b)
    )

    if norm_a == 0 or norm_b == 0:
        return 0.0

    return dot_product / (norm_a * norm_b)


def build_db_index() -> int:
    """DB RAG 문서를 임베딩하여 JSON 인덱스를 생성한다."""

    documents = read_markdown_files()

    all_chunks: list[dict[str, Any]] = []

    for document in documents:
        chunks = split_markdown(
            source=document["source"],
            text=document["text"],
        )
        all_chunks.extend(chunks)

    if not all_chunks:
        raise RuntimeError(
            "인덱싱할 DB RAG 문서 조각이 없습니다."
        )

    print(
        f"[DB RAG] 문서 {len(documents)}개, "
        f"조각 {len(all_chunks)}개"
    )

    batch_size = 8

    for start in range(
        0,
        len(all_chunks),
        batch_size,
    ):
        batch = all_chunks[
            start:start + batch_size
        ]

        embeddings = embed_texts(
            [
                chunk["content"]
                for chunk in batch
            ]
        )

        if len(embeddings) != len(batch):
            raise RuntimeError(
                "임베딩 개수와 문서 조각 개수가 일치하지 않습니다."
            )

        for chunk, embedding in zip(
            batch,
            embeddings,
        ):
            chunk["embedding"] = embedding

        print(
            f"[DB RAG] 임베딩 진행: "
            f"{min(start + batch_size, len(all_chunks))}"
            f"/{len(all_chunks)}"
        )

    INDEX_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    INDEX_PATH.write_text(
        json.dumps(
            {
                "model": EMBED_MODEL,
                "chunks": all_chunks,
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    print(
        f"[DB RAG] 인덱스 저장 완료: "
        f"{INDEX_PATH}"
    )

    return len(all_chunks)


def load_db_index() -> list[dict[str, Any]]:
    """저장된 DB RAG 인덱스를 불러온다."""

    if not INDEX_PATH.exists():
        raise FileNotFoundError(
            "DB RAG 인덱스가 없습니다. "
            "먼저 build_db_index()를 실행하세요."
        )

    data = json.loads(
        INDEX_PATH.read_text(
            encoding="utf-8",
        )
    )

    chunks = data.get("chunks")

    if not isinstance(chunks, list):
        raise RuntimeError(
            "DB RAG 인덱스 형식이 올바르지 않습니다."
        )

    return chunks


def search_db_context(
    query: str,
    top_k: int = 5,
) -> list[dict[str, Any]]:
    """질의와 유사한 DB RAG 문서 조각을 검색한다."""

    query = query.strip()

    if not query:
        return []

    chunks = load_db_index()
    query_embedding = embed_texts([query])[0]

    scored_chunks: list[dict[str, Any]] = []

    for chunk in chunks:
        embedding = chunk.get("embedding")

        if not isinstance(embedding, list):
            continue

        score = cosine_similarity(
            query_embedding,
            embedding,
        )

        scored_chunks.append(
            {
                "source": chunk.get("source", ""),
                "heading": chunk.get("heading", ""),
                "content": chunk.get("content", ""),
                "score": score,
            }
        )

    scored_chunks.sort(
        key=lambda item: item["score"],
        reverse=True,
    )

    return scored_chunks[:top_k]


def format_db_context(
    results: list[dict[str, Any]],
) -> str:
    """검색 결과를 DB Agent 프롬프트용 문자열로 만든다."""

    if not results:
        return "검색된 DB RAG 문서가 없습니다."

    sections: list[str] = []

    for index, result in enumerate(
        results,
        start=1,
    ):
        sections.append(
            "\n".join(
                [
                    f"[DB RAG {index}]",
                    f"Source: {result['source']}",
                    f"Heading: {result['heading'] or '없음'}",
                    f"Score: {result['score']:.4f}",
                    "",
                    result["content"],
                ]
            )
        )

    return "\n\n---\n\n".join(sections)


if __name__ == "__main__":
    build_db_index()
