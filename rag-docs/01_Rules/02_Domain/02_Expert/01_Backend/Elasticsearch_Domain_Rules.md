# Elasticsearch Domain Rules

---

# 1. Domain Purpose

Elasticsearch Domain 문서는 Backend Agent / DevOps Agent / Review Agent용 RAG 문서이다.

목적:

- Search Engine Support
- Full Text Search Support
- Log Analytics Support
- Search Optimization Support
- Elasticsearch Troubleshooting

우선순위:

1. Elasticsearch Core
2. Index / Document / Mapping
3. Search Query
4. Performance / Troubleshooting

---

# 2. Scope

포함 범위:

- Elasticsearch Core
- Cluster
- Node
- Index
- Document
- Field
- Mapping
- Analyzer
- Tokenizer
- Inverted Index
- Search Query
- Full Text Search
- Keyword Search
- Aggregation
- Relevance Score
- Shard
- Replica
- Bulk API
- Monitoring
- Troubleshooting

---

# 3. Section Priority

## Required

- [개념]
- [핵심]
- [실무]
- [FAQ]

---

## Strongly Recommended

- [Flow]
- [예제]
- [주의]
- [Best Practice]

---

## Optional

- [Checklist]
- [Troubleshooting]
- [Comparison]

---

# 4. Elasticsearch Core Rules

Elasticsearch 문서는 Distributed Search Engine 중심으로 작성.

핵심 구조:

- Cluster
- Node
- Index
- Document
- Query

---

반드시 설명 포함:

- Elasticsearch 역할
- 왜 사용하는가
- DB 검색과 차이
- 어떤 문제를 해결하는가

---

예:

```text
Data
→ Indexing
→ Inverted Index
→ Search Query
→ Result
```

---

# 5. Cluster Rules

필수 포함:

- Cluster
- Node

---

반드시 설명:

- Cluster 구조
- Node 역할

---

# 6. Node Rules

필수 포함:

- Master Node
- Data Node
- Coordinating Node

---

반드시 설명:

- Node 유형
- 역할 차이

---

# 7. Index Rules

매우 중요.

필수 포함:

- Index
- Logical Collection

---

예:

```text
users
products
orders
logs
```

---

반드시 설명:

- RDB Table과 비교
- 데이터 저장 단위

---

중요:

Elasticsearch 문서 품질은 Index 설명 품질이 결정.

---

# 8. Document Rules

필수 포함:

- Document
- JSON

---

예:

```json
{
  "name": "jun",
  "age": 30
}
```

---

반드시 설명:

- Record 개념
- 저장 구조

---

# 9. Field Rules

필수 포함:

- Field
- Data Type

---

반드시 설명:

- Text
- Keyword
- Numeric
- Date

---

# 10. Mapping Rules

매우 중요.

필수 포함:

- Mapping
- Schema Definition

---

반드시 설명:

- Field Type
- Index Strategy

---

예:

```json
{
  "properties": {
    "name": { "type": "text" }
  }
}
```

---

# 11. Analyzer Rules

매우 중요.

필수 포함:

- Analyzer
- Tokenization
- Text Processing

---

반드시 설명:

- Search 정확도
- 언어 처리

---

# 12. Tokenizer Rules

필수 포함:

- Tokenizer
- Token

---

반드시 설명:

- 문장 분해
- Search 준비

---

# 13. Inverted Index Rules

핵심.

필수 포함:

- Inverted Index
- Search Optimization

---

반드시 설명:

- 빠른 검색 원리
- DB Index와 차이

---

중요:

Elasticsearch 핵심 Retrieval 포인트.

---

# 14. Search Query Rules

매우 중요.

필수 포함:

- Match Query
- Term Query
- Bool Query

---

반드시 설명:

- Full Text Search
- Exact Match Search

---

# 15. Full Text Search Rules

필수 포함:

- Match
- Relevance

---

반드시 설명:

- 자연어 검색
- 검색 점수

---

# 16. Keyword Search Rules

필수 포함:

- Exact Match
- Keyword Field

---

반드시 설명:

- Filter
- Exact Search

---

# 17. Aggregation Rules

매우 중요.

필수 포함:

- Terms Aggregation
- Avg
- Sum
- Count

---

반드시 설명:

- Analytics
- Dashboard

---

# 18. Relevance Score Rules

필수 포함:

- Score
- Ranking

---

반드시 설명:

- 검색 결과 정렬
- Relevance

---

# 19. Shard Rules

매우 중요.

필수 포함:

- Primary Shard
- Distributed Storage

---

반드시 설명:

- Horizontal Scaling
- Query Distribution

---

# 20. Replica Rules

필수 포함:

- Replica
- Fault Tolerance

---

반드시 설명:

- Availability
- Read Scaling

---

# 21. Bulk API Rules

필수 포함:

- Bulk Insert
- Bulk Update

---

반드시 설명:

- 대량 데이터 처리
- 성능 최적화

---

# 22. Spring Elasticsearch Rules

필수 포함:

- Spring Data Elasticsearch
- Repository
- ElasticsearchClient

---

반드시 설명:

- Spring Boot 연동 방식

---

# 23. Performance Rules

필수 포함:

- Query Latency
- Index Speed
- Memory Usage
- Heap Usage

---

반드시 설명:

- 성능 병목
- 튜닝 포인트

---

# 24. Monitoring Rules

필수 포함:

- Cluster Health
- Query Latency
- Heap Usage
- Disk Usage

---

반드시 설명:

- 운영 핵심 지표

---

# 25. Troubleshooting Rules

반드시 포함 추천.

예:

- Slow Search
- High Heap Usage
- Red Cluster
- Yellow Cluster
- Mapping Conflict
- Shard Imbalance

---

형식:

문제:

원인:

해결:

---

# 26. Retrieval Optimization Rules

강조 대상:

- Elasticsearch
- Index
- Document
- Mapping
- Analyzer
- Inverted Index
- Shard
- Aggregation

키워드 반복 허용.

---

# 27. Version Rules

기준:

- Elasticsearch 8.x
- Spring Boot 3.x
- Java 21
- Spring Data Elasticsearch

---

Legacy 제외.

---

# 28. Common Mistakes

자주 발생:

- Mapping 설계 부족
- Text / Keyword 혼동
- Analyzer 미설계
- Shard 과다 생성
- Replica 미설정
- Heap 부족
- Slow Query 방치
- Cluster Health 미확인

---

# 29. Final Goal

Elasticsearch RAG 문서는 Agent가 아래 수행 가능해야 한다.

- Retrieve Search Pattern
- Design Search Architecture
- Optimize Search Query
- Solve Search Problems
- Troubleshoot Elasticsearch Issues
- Improve Search Performance

문서 품질이 Search / Analytics 품질을 결정한다.
