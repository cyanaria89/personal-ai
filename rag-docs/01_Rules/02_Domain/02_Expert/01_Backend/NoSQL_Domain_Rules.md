# NoSQL Domain Rules

---

# 1. Domain Purpose

NoSQL Domain 문서는 Backend Agent / DevOps Agent / Review Agent용 RAG 문서이다.

목적:

- Non-Relational Database Support
- Flexible Data Modeling Support
- Horizontal Scaling Support
- High Availability Support
- NoSQL Troubleshooting

우선순위:

1. NoSQL Core
2. Data Model
3. Consistency / Scalability
4. Troubleshooting

---

# 2. Scope

포함 범위:

- NoSQL Core
- Key-Value
- Document DB
- Column Family
- Graph DB
- MongoDB
- Redis
- Cassandra
- Neo4j
- Schema-less
- Denormalization
- CAP Theorem
- Consistency
- Availability
- Partition Tolerance
- Replication
- Sharding
- Query Pattern
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

# 4. NoSQL Core Rules

NoSQL 문서는 Non-Relational Database 중심으로 작성.

핵심 구조:

- Data Model
- Storage
- Query Pattern
- Scalability

---

반드시 설명 포함:

- NoSQL 역할
- 왜 사용하는가
- RDB와 차이
- 어떤 문제를 해결하는가

---

예:

```text
Application
→ NoSQL Database
→ Flexible Data Storage
```

---

# 5. NoSQL Types Rules

매우 중요.

필수 포함:

- Key-Value
- Document
- Column Family
- Graph

---

예:

```text
Key-Value    → Redis
Document     → MongoDB
ColumnFamily → Cassandra
Graph        → Neo4j
```

---

반드시 설명:

- 유형별 특징
- 사용 사례

---

중요:

NoSQL 문서 품질은 Type 비교 품질이 결정.

---

# 6. Key-Value Rules

필수 포함:

- Key
- Value

---

반드시 설명:

- 단순 구조
- 빠른 조회

---

예:

- Redis

---

# 7. Document Rules

매우 중요.

필수 포함:

- JSON Document
- Flexible Schema

---

반드시 설명:

- Schema-less 구조
- Nested Data 저장

---

예:

- MongoDB

---

# 8. Column Family Rules

필수 포함:

- Wide Column
- Column Family

---

반드시 설명:

- 대용량 데이터
- 분산 저장

---

예:

- Cassandra

---

# 9. Graph DB Rules

필수 포함:

- Node
- Edge
- Relationship

---

반드시 설명:

- 관계 중심 데이터

---

예:

- Neo4j

---

# 10. Schema-less Rules

매우 중요.

필수 포함:

- Schema-less
- Flexible Structure

---

반드시 설명:

- 장점
- 단점

---

# 11. Denormalization Rules

매우 중요.

필수 포함:

- Denormalization
- Duplicate Data

---

반드시 설명:

- Join 최소화
- Read Optimization

---

# 12. MongoDB Rules

매우 중요.

필수 포함:

- Collection
- Document
- BSON

---

반드시 설명:

- MongoDB 핵심 구조
- Document Database 대표

---

# 13. CAP Rules

핵심.

필수 포함:

- Consistency
- Availability
- Partition Tolerance

---

반드시 설명:

- CAP Trade-off
- Distributed DB 핵심

---

중요:

NoSQL 핵심 Retrieval 포인트.

---

# 14. Consistency Rules

매우 중요.

필수 포함:

- Strong Consistency
- Eventual Consistency

---

반드시 설명:

- 데이터 일관성 수준

---

# 15. Availability Rules

필수 포함:

- Availability
- Fault Tolerance

---

반드시 설명:

- 장애 상황 대응

---

# 16. Replication Rules

필수 포함:

- Replication
- Replica

---

반드시 설명:

- 고가용성
- 읽기 확장

---

# 17. Sharding Rules

매우 중요.

필수 포함:

- Sharding
- Horizontal Scaling

---

반드시 설명:

- 데이터 분산 저장
- Scale Out

---

# 18. Query Pattern Rules

필수 포함:

- Query Optimization
- Access Pattern

---

반드시 설명:

- Query 기반 설계
- RDB와 다른 설계 방식

---

# 19. Monitoring Rules

필수 포함:

- Latency
- Throughput
- Replication Lag
- Storage Usage

---

반드시 설명:

- 운영 핵심 지표

---

# 20. Troubleshooting Rules

반드시 포함 추천.

예:

- Slow Query
- Replication Lag
- Shard Imbalance
- Data Inconsistency
- Hot Partition

---

형식:

문제:

원인:

해결:

---

# 21. Retrieval Optimization Rules

강조 대상:

- NoSQL
- MongoDB
- CAP
- Sharding
- Replication
- Schema-less
- Denormalization
- Eventual Consistency

키워드 반복 허용.

---

# 22. Version Rules

기준:

- MongoDB
- Redis
- Cassandra
- Neo4j
- Modern Distributed DB

---

Legacy 제외.

---

# 23. Common Mistakes

자주 발생:

- RDB 방식 그대로 적용
- CAP 오해
- Query Pattern 미설계
- Denormalization 부족
- Hot Partition 방치
- Consistency Trade-off 무시

---

# 24. Final Goal

NoSQL RAG 문서는 Agent가 아래 수행 가능해야 한다.

- Retrieve NoSQL Concepts
- Select Proper NoSQL Type
- Design Data Model
- Solve Scaling Problems
- Troubleshoot Distributed DB Issues

문서 품질이 Scalability 품질을 결정한다.
