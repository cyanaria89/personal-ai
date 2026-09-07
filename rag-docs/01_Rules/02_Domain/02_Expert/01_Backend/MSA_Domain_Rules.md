# MSA Domain Rules

---

# 1. Domain Purpose

MSA Domain 문서는 Backend Agent / DevOps Agent / PM Agent / Review Agent용 RAG 문서이다.

목적:

- Microservice Architecture Design Support
- Distributed System Support
- Service Decomposition Support
- Distributed Transaction Support
- MSA Troubleshooting

우선순위:

1. MSA Core
2. Service Communication
3. Distributed Transaction
4. Observability / Troubleshooting

---

# 2. Scope

포함 범위:

- MSA Core
- Monolith vs MSA
- Modular Monolith
- Service Decomposition
- API Gateway
- Service Discovery
- Inter-Service Communication
- Database per Service
- Event-Driven Architecture
- Eventual Consistency
- Distributed Transaction
- Saga Pattern
- Choreography
- Orchestration
- Outbox Pattern
- CQRS
- Circuit Breaker
- Distributed Tracing
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

# 4. MSA Core Rules

MSA 문서는 Distributed System Architecture 중심으로 작성.

핵심 구조:

- Service
- Network
- Database
- Messaging
- Observability

---

반드시 설명 포함:

- MSA 역할
- 왜 사용하는가
- Monolith와 차이
- 어떤 문제를 해결하는가

---

예:

```text
Client
→ API Gateway
→ Service A
→ Service B
→ Service C
```

---

# 5. Monolith vs MSA Rules

매우 중요.

필수 포함:

- Monolith
- MSA
- Trade-off

---

반드시 설명:

- 장점
- 단점
- 도입 기준

---

중요:

MSA 문서 품질은 Monolith vs MSA 설명 품질이 결정.

---

# 6. Modular Monolith Rules

필수 포함:

- Modular Monolith
- Domain Boundary

---

반드시 설명:

- MSA 이전 단계
- 현실적 Migration 전략

---

# 7. Service Decomposition Rules

매우 중요.

필수 포함:

- Domain Boundary
- Business Capability
- Service Ownership

---

반드시 설명:

- Service 분리 기준
- 잘못된 분리 사례

---

예:

```text
User Service
Order Service
Payment Service
Notification Service
```

---

# 8. API Gateway Rules

필수 포함:

- Gateway
- Routing
- Edge Layer

---

반드시 설명:

- Entry Point
- Common Concern 처리

---

# 9. Service Discovery Rules

필수 포함:

- Discovery
- Dynamic Routing

---

반드시 설명:

- Scaling
- Dynamic Endpoint

---

# 10. Communication Rules

매우 중요.

필수 포함:

- REST
- gRPC
- Messaging
- Event Streaming

---

반드시 설명:

- Sync vs Async
- 장단점

---

Flow:

```text
Service A
→ REST / Event
→ Service B
```

---

# 11. Database per Service Rules

매우 중요.

필수 포함:

- Data Ownership
- Database Isolation

---

반드시 설명:

- DB 공유 금지 이유
- Service Independence

---

중요:

DB 직접 공유는 Anti Pattern.

---

# 12. Event-Driven Architecture Rules

매우 중요.

필수 포함:

- Event
- Producer
- Consumer

---

반드시 설명:

- Async Architecture
- Loose Coupling

---

# 13. Eventual Consistency Rules

매우 중요.

필수 포함:

- Eventually Consistent
- Temporary Inconsistency

---

반드시 설명:

- Strong Consistency와 차이
- 실무적 의미

---

# 14. Distributed Transaction Rules

핵심.

필수 포함:

- Distributed Transaction
- Partial Failure

---

반드시 설명:

- 왜 어려운가
- 왜 2PC가 어려운가

---

# 15. Saga Pattern Rules

매우 중요.

필수 포함:

- Saga
- Compensation Transaction

---

반드시 설명:

- 분산 Transaction 해결 전략
- Rollback 대체 방식

---

Flow:

```text
Step1 Success
→ Step2 Success
→ Step3 Fail
→ Compensation
```

---

# 16. Choreography Rules

필수 포함:

- Event Chain
- Distributed Control

---

반드시 설명:

- 장점
- 단점

---

# 17. Orchestration Rules

필수 포함:

- Central Orchestrator

---

반드시 설명:

- Workflow Control
- Central Coordination

---

# 18. Outbox Pattern Rules

매우 중요.

필수 포함:

- Outbox Table
- Reliable Event Publish

---

반드시 설명:

- DB Commit + Event Publish 문제 해결

---

# 19. CQRS Rules

필수 포함:

- Command Model
- Query Model

---

반드시 설명:

- Read / Write 분리
- 적용 상황

---

# 20. Circuit Breaker Rules

필수 포함:

- Circuit Breaker
- Fault Isolation

---

반드시 설명:

- 장애 전파 차단
- Resilience

---

# 21. Observability Rules

매우 중요.

필수 포함:

- Metrics
- Logs
- Traces

---

반드시 설명:

- MSA 운영 핵심

---

# 22. Distributed Tracing Rules

필수 포함:

- Trace ID
- Span

---

반드시 설명:

- 요청 흐름 추적
- 장애 분석

---

# 23. Monitoring Rules

필수 포함:

- Health
- Latency
- Error Rate
- Traffic

---

반드시 설명:

- 운영 관측 포인트

---

# 24. Performance Rules

필수 포함:

- Latency
- Network Overhead
- Retry Storm

---

반드시 설명:

- MSA 성능 병목

---

# 25. Troubleshooting Rules

반드시 포함 추천.

예:

- Service Timeout
- Network Partition
- Retry Storm
- Data Inconsistency
- Event Loss
- Circuit Open
- Trace Missing

---

형식:

문제:

원인:

해결:

---

# 26. Retrieval Optimization Rules

강조 대상:

- MSA
- Service Decomposition
- API Gateway
- Eventual Consistency
- Saga
- Outbox
- CQRS
- Circuit Breaker

키워드 반복 허용.

---

# 27. Version Rules

기준:

- Spring Boot 3.x
- Java 21
- Docker
- Kubernetes
- Kafka
- Redis

---

Legacy 제외.

---

# 28. Common Mistakes

자주 발생:

- 너무 이른 MSA 도입
- DB 공유
- Sync Call Chain 과다
- Timeout 누락
- Retry Storm
- Saga 미설계
- Event Loss 방치
- Monitoring 부족
- Trace 없음
- 운영 복잡도 과소평가

---

# 29. Final Goal

MSA RAG 문서는 Agent가 아래 수행 가능해야 한다.

- Retrieve MSA Pattern
- Design Service Architecture
- Design Distributed Transaction
- Solve MSA Problems
- Troubleshoot Production Issues
- Improve Distributed System Reliability

문서 품질이 Distributed Architecture 품질을 결정한다.
