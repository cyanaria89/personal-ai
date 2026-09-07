# Kafka Domain Rules

---

# 1. Domain Purpose

Kafka Domain 문서는 Backend Agent / DevOps Agent / Review Agent용 RAG 문서이다.

목적:

- Event Streaming Support
- Message Architecture Support
- Async Processing Support
- Distributed Messaging Support
- Kafka Troubleshooting

우선순위:

1. Kafka Core
2. Producer / Consumer
3. Event Streaming
4. Performance / Troubleshooting

---

# 2. Scope

포함 범위:

- Kafka Core
- Broker
- Topic
- Partition
- Producer
- Consumer
- Consumer Group
- Offset
- Replication
- Leader / Follower
- Event Streaming
- Ordering
- Delivery Semantics
- Retention
- Retry
- DLQ
- Spring Kafka
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

# 4. Kafka Core Rules

Kafka 문서는 Distributed Event Streaming 중심으로 작성.

핵심 구조:

- Broker
- Topic
- Partition
- Producer
- Consumer

---

반드시 설명 포함:

- Kafka 역할
- 왜 사용하는가
- RabbitMQ와 차이
- 어떤 문제를 해결하는가

---

예:

```text
Producer
→ Topic
→ Partition
→ Consumer
```

---

# 5. Broker Rules

필수 포함:

- Broker
- Cluster
- Node

---

반드시 설명:

- Kafka Server 역할
- Cluster 구조

---

# 6. Topic Rules

매우 중요.

필수 포함:

- Topic
- Message Stream

---

예:

```text
order-events
payment-events
notification-events
```

---

반드시 설명:

- Topic 역할
- Event 저장 위치

---

중요:

Kafka 문서 품질은 Topic 설명 품질이 결정.

---

# 7. Partition Rules

매우 중요.

필수 포함:

- Partition
- Parallel Processing
- Ordering

---

반드시 설명:

- Partition 역할
- Ordering 보장 범위

---

예:

```text
Topic
├─ Partition 0
├─ Partition 1
└─ Partition 2
```

---

# 8. Producer Rules

필수 포함:

- Producer
- Send
- Batch
- Compression

---

반드시 설명:

- Event Publish
- Partition 선택

---

예:

```java
kafkaTemplate.send("order-events", event);
```

---

# 9. Consumer Rules

필수 포함:

- Consumer
- Poll
- Process

---

반드시 설명:

- Event Consume
- Message Processing

---

# 10. Consumer Group Rules

매우 중요.

필수 포함:

- Consumer Group
- Parallel Consume

---

반드시 설명:

- Scaling
- Load Distribution

---

예:

```text
Consumer Group A
Consumer 1 → Partition 0
Consumer 2 → Partition 1
```

---

# 11. Offset Rules

매우 중요.

필수 포함:

- Offset
- Commit
- Resume

---

반드시 설명:

- Message 위치 추적
- 재처리 가능 구조

---

# 12. Replication Rules

필수 포함:

- Replication
- Fault Tolerance

---

반드시 설명:

- 데이터 복제
- 장애 복구

---

# 13. Leader / Follower Rules

필수 포함:

- Leader
- Follower

---

반드시 설명:

- 읽기/쓰기 구조
- Failover

---

# 14. Delivery Semantics Rules

매우 중요.

필수 포함:

- At Most Once
- At Least Once
- Exactly Once

---

반드시 설명:

- 메시지 유실
- 중복 처리
- 실무 선택 기준

---

# 15. Ordering Rules

필수 포함:

- Ordering
- Partition Key

---

반드시 설명:

- Partition 내부 순서
- Global Ordering 불가

---

중요:

Ordering은 Kafka 핵심 Retrieval 포인트.

---

# 16. Retention Rules

필수 포함:

- Retention
- Log Storage

---

반드시 설명:

- 메시지 보관 기간
- 삭제 정책

---

# 17. Retry Rules

필수 포함:

- Retry
- Backoff

---

반드시 설명:

- 일시 실패 처리
- Retry 전략

---

# 18. DLQ Rules

매우 중요.

필수 포함:

- Dead Letter Queue
- Failed Message

---

반드시 설명:

- 실패 이벤트 격리
- 재처리 전략

---

# 19. Spring Kafka Rules

필수 포함:

- spring-kafka
- KafkaTemplate
- @KafkaListener

---

예:

```java
@KafkaListener(topics = "order-events")
```

---

반드시 설명:

- Spring Boot 연동 방식

---

# 20. Event Streaming Rules

매우 중요.

필수 포함:

- Event Stream
- Stream Processing

---

반드시 설명:

- Event-Driven Architecture
- Async Flow

---

Flow:

```text
Event Created
→ Kafka
→ Consumers
→ Async Processing
```

---

# 21. Performance Rules

필수 포함:

- Throughput
- Latency
- Batch Size
- Compression

---

반드시 설명:

- 성능 튜닝 포인트
- 병목 위치

---

# 22. Monitoring Rules

필수 포함:

- Consumer Lag
- Broker Health
- Throughput

---

반드시 설명:

- 운영 모니터링 핵심 지표

---

# 23. Troubleshooting Rules

반드시 포함 추천.

예:

- Consumer Lag High
- Rebalance Frequent
- Message Duplication
- Ordering Issue
- Broker Down
- Partition Hotspot

---

형식:

문제:

원인:

해결:

---

# 24. Retrieval Optimization Rules

강조 대상:

- Kafka
- Topic
- Partition
- Producer
- Consumer
- Consumer Group
- Offset
- DLQ

키워드 반복 허용.

---

# 25. Version Rules

기준:

- Kafka 3.x+
- Spring Boot 3.x
- Java 21
- Spring Kafka

---

Legacy 제외.

---

# 26. Common Mistakes

자주 발생:

- Partition 부족
- Ordering 오해
- Offset 관리 실패
- Consumer Lag 방치
- DLQ 미구성
- Retry 무한 반복
- Message Duplication 미대응
- Consumer Group 구조 오해

---

# 27. Final Goal

Kafka RAG 문서는 Agent가 아래 수행 가능해야 한다.

- Retrieve Kafka Pattern
- Design Event Architecture
- Configure Producer / Consumer
- Solve Async Processing Issues
- Troubleshoot Kafka Problems
- Optimize Streaming Performance

문서 품질이 Event Architecture 품질을 결정한다.
