from __future__ import annotations

import json
from array import array
import math
import urllib.error
import urllib.request
from pathlib import Path
from pathlib import PurePosixPath
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

# 02_DB_Agent_RAG_Map / 03_Backend_Agent_RAG_Map의 Domain Rules와
# 실제 foundation 디렉터리 간 명시적인 대응. Reference-only는 허용하지 않는다.
DOMAIN_FOUNDATION_DIRS = {
    "01_SQL_Domain_Rules.md": "01_SQL",
    "02_Java_Domain_Rules.md": "02_Java",
    "03_Spring_Boot_Domain_Rules.md": "03_SpringBoot",
    "04_JPA_Advanced_Domain_Rules.md": "04_JPA_Advanced",
    "05_Security_Advanced_Domain_Rules.md": "05_Security_Advanced",
    "06_QueryDSL_Practical_Domain_Rules.md": "06_QueryDSL_Practical",
    "07_Testing_Domain_Rules.md": "07_Testing",
    "08_Redis_Domain_Rules.md": "08_Redis",
    "09_SSR_Thymeleaf_Domain_Rules.md": "09_SSR_Thymeleaf",
    "10_Git_GitHub_Domain_Rules.md": "10_Git_GitHub",
    "11_Docker_Domain_Rules.md": "11_Docker",
    "12_API_Design_Domain_Rules.md": "12_API_Design",
    "13_Design_Pattern_Domain_Rules.md": "13_Design_Pattern",
}

FRONTEND_FOUNDATION_DIRS = {
    "01_HTML_CSS_Foundation_Domain_Rules.md": "01_HTTP_CSS_Foundation",
    "02_JavaScript_Foundation_Domain_Rules.md": "02_JavaScript_Foundation",
    "03_TypeScript_Foundation_Domain_Rules.md": "03_TypeScript_Foundation",
    "04_React_Core_Domain_Rules.md": "04_React_Core",
    "05_React_Component_Design_Domain_Rules.md": "05_React_Component_Design",
    "06_React_Router_Domain_Rules.md": "06_React_Router",
    "07_State_Management_Domain_Rules.md": "07_State_Management",
    "08_Data_Fetching_REST_API_Integration_Domain_Rules.md": "08_Data_Fetching_REST_API_Integration",
    "09_Form_Handling_Validation_Domain_Rules.md": "09_Form_Handling_Validation",
    "10_Authentication_Frontend_Flow_Domain_Rules.md": "10_Authentication_Frontend_Flow",
    "11_Error_Handling_Loading_UX_Domain_Rules.md": "11_Error_Handling_Loading_UX",
    "12_UI_Component_Pattern_Domain_Rules.md": "12_UI_Component_Pattern",
    "13_Frontend_Testing_Domain_Rules.md": "13_Frontend_Testing",
    "14_Frontend_Accessibility_Domain_Rules.md": "14_Frontend_Accessibility",
    "15_Frontend_Build_Deploy_Domain_Rules.md": "15_Frontend_Build_Deploy",
    "16_Frontend_Code_Review_Domain_Rules.md": "16_Frontend_Code_Review",
    "17_Styling_Architecture_Domain_Rules.md": "17_Styling_Architecture",
    "18_Design_System_Foundation_Domain_Rules.md": "18_Design_System_Foundation",
}

AGENT_DOMAIN_RULES = {
    "frontend": {
        "primary": tuple(FRONTEND_FOUNDATION_DIRS),
        "secondary": ("12_API_Design_Domain_Rules.md", "05_Security_Advanced_Domain_Rules.md",
                      "10_Git_GitHub_Domain_Rules.md", "11_Docker_Domain_Rules.md"),
    },
    "db": {
        "primary": ("01_SQL_Domain_Rules.md", "04_JPA_Advanced_Domain_Rules.md",
                    "06_QueryDSL_Practical_Domain_Rules.md"),
        "secondary": ("03_Spring_Boot_Domain_Rules.md", "12_API_Design_Domain_Rules.md",
                      "13_Design_Pattern_Domain_Rules.md", "07_Testing_Domain_Rules.md"),
    },
    "backend": {
        "primary": ("02_Java_Domain_Rules.md", "03_Spring_Boot_Domain_Rules.md",
                    "04_JPA_Advanced_Domain_Rules.md", "05_Security_Advanced_Domain_Rules.md",
                    "06_QueryDSL_Practical_Domain_Rules.md", "12_API_Design_Domain_Rules.md",
                    "13_Design_Pattern_Domain_Rules.md"),
        "secondary": ("01_SQL_Domain_Rules.md", "07_Testing_Domain_Rules.md",
                      "08_Redis_Domain_Rules.md", "09_SSR_Thymeleaf_Domain_Rules.md",
                      "10_Git_GitHub_Domain_Rules.md", "11_Docker_Domain_Rules.md"),
    },
}


def classify_source(source: str) -> str | None:
    """기존 source 경로를 Domain Rules 파일명으로 분류한다."""
    if not isinstance(source, str):
        return None
    parts = PurePosixPath(source).parts
    if parts[:2] != ("data", "rag-source") or ".." in parts:
        return None
    mappings = {"backend": DOMAIN_FOUNDATION_DIRS, "frontend": FRONTEND_FOUNDATION_DIRS}
    for area, mapping in mappings.items():
        if len(parts) == 4 and parts[2] == f"{area}-domain":
            return parts[3] if parts[3] in mapping else None
        if len(parts) != 5 or parts[2] != f"{area}-foundation" or not parts[4].endswith(".md"):
            continue
        for rule, directory in mapping.items():
            if parts[3] == directory:
                return rule
    return None


def allowed_domain_rules(agent: str) -> set[str]:
    if agent not in AGENT_DOMAIN_RULES:
        raise ValueError(f"지원하지 않는 Domain RAG Agent입니다: {agent}")
    policy = AGENT_DOMAIN_RULES[agent]
    return set(policy["primary"]) | set(policy["secondary"])


def filter_agent_chunks(chunks: list[dict[str, Any]], agent: str) -> list[dict[str, Any]]:
    allowed = allowed_domain_rules(agent)
    candidates = []
    unclassified = set()
    for chunk in chunks:
        source = chunk.get("source", "")
        domain = classify_source(source)
        if domain is None:
            unclassified.add(str(source))
        elif domain in allowed:
            candidates.append(chunk)
    for source in sorted(unclassified):
        print(f"[{agent.upper()} RAG 경고] 미분류 문서 제외: {source or '(source 없음)'}")
    print(f"[{agent.upper()} RAG] 허용 후보 {len(candidates)}/{len(chunks)}개 chunks")
    return candidates


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
    """DB Primary/Secondary 문서 범위에서 검색한다."""
    return search_domain_context(query, agent="db", top_k=top_k)


def search_domain_context(
    query: str,
    *,
    agent: str,
    top_k: int = 3,
    chunks=None,
) -> list[dict[str, Any]]:
    """Agent별 후보를 먼저 제한한 뒤 기존 임베딩과 점수로 검색한다."""
    allowed_domain_rules(agent)

    query = query.strip()

    if not query:
        return []

    if agent == "frontend" and chunks is None:
        raise ValueError("Frontend 검색은 wrapper에서 두 인덱스 후보를 전달해야 합니다.")
    chunks = filter_agent_chunks(load_db_index() if chunks is None else chunks, agent)
    if not chunks:
        return []
    query_embedding = embed_texts([query])[0]

    scored_chunks: list[dict[str, Any]] = []

    for chunk in chunks:
        embedding = chunk.get("embedding")

        if not isinstance(embedding, (list, array)):
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
    *,
    domain: str = "DB",
) -> str:
    """검색 결과를 DB Agent 프롬프트용 문자열로 만든다."""

    if not results:
        return f"검색된 {domain} RAG 문서가 없습니다."

    sections: list[str] = []

    for index, result in enumerate(
        results,
        start=1,
    ):
        sections.append(
            "\n".join(
                [
                    f"[{domain} RAG {index}]",
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
