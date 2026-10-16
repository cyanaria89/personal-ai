"""Backend 검색은 기존 Backend domain/foundation 인덱스를 공유한다.

db_index.json은 SQL뿐 아니라 Java, Spring Boot, JPA 문서도 포함한다.
문서 로딩, chunking, BGE-M3 임베딩, 유사도 검색 정책은 DB와 동일하다.
인덱스 재생성은 기존 python rag/db_retriever.py 명령을 사용한다.
"""

from typing import Any

from rag.db_retriever import format_db_context, search_domain_context


def search_backend_context(query: str, top_k: int = 3) -> list[dict[str, Any]]:
    return search_domain_context(query, agent="backend", top_k=top_k)


def format_backend_context(results: list[dict[str, Any]]) -> str:
    return format_db_context(results, domain="Backend Domain")
