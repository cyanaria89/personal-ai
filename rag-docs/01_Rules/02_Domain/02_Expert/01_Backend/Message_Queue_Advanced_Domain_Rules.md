# Message Queue Advanced Domain Rules

---

# 1. Domain Purpose

Message Queue Advanced Domain 문서는 Backend Agent / DevOps Agent / Review Agent용 RAG 문서이다.

목적:

- Messaging Architecture Support
- Async Processing Support
- Queue Pattern Support
- Reliability Improvement
- Message Queue Troubleshooting

우선순위:

1. MQ Core
2. Queue Pattern
3. Reliability / Delivery
4. Troubleshooting

---

# 2. Scope

포함 범위:

- Message Queue Core
- Queue
- Producer
- Consumer
- Broker
- RabbitMQ
- SQS
- Pub/Sub
- Exchange
- Routing Key
- Queue Pattern
- Retry
- DLQ
- Ordering
- Delivery Guarantee
- Back Pressure
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

# 4. MQ Core Rules

Message Queue 문서는 Async Messaging 중심으로 작성.

핵심 구조:

- Producer
- Broker
- Queue
- Consumer

---

반드시 설명 포함:

- MQ 역할
- 왜 사용하는가
- Kafka와 차이
- 어떤 문제를 해결하는가

---

예:

```text
Producer
→ Broker
→ Queue
→ Consumer
```

---

# 5. Queue Rules

매우 중요.

필수 포함:

- Queue
- FIFO
- Async Processing

---

반드시 설명:

- 작업 대기열
- Producer / Consumer 분리

---

중요:

MQ 문서 품질은 Queue 설명 품질이 결정.

---

# 6. Producer Rules

필수 포함:

- Producer
- Publish

---

반드시 설명:

- Message 생성
- Broker 전송

---

# 7. Consumer Rules

필수 포함:

- Consumer
- Consume
- Ack

---

반드시 설명:

- Message 처리
- Ack 의미

---

# 8. Broker Rules

필수 포함:

- Broker
- Routing

---

반드시 설명:

- Message 전달
- Queue 관리

---

# 9. RabbitMQ Rules

매우 중요.

필수 포함:

- RabbitMQ
- AMQP

---

반드시 설명:

- Queue 기반 MQ
- Reliable Delivery

---

# 10. SQS Rules

필수 포함:

- SQS
- Managed Queue

---

반드시 설명:

- Cloud MQ
- AWS 기반 Queue

---

# 11. Pub/Sub Rules

매우 중요.

필수 포함:

- Publisher
- Subscriber

---

반드시 설명:

- Event Broadcast
- One-to-Many 구조

---

# 12. Exchange Rules

필수 포함:

- Exchange
- Routing

---

반드시 설명:

- RabbitMQ 핵심

---

# 13. Routing Key Rules

필수 포함:

- Routing Key
- Message Routing

---

반드시 설명:

- Queue 전달 규칙

---

# 14. Queue Pattern Rules

매우 중요.

필수 포함:

- Work Queue
- Fanout
- Routing
- Topic

---

반드시 설명:

- 패턴별 사용 케이스

---

# 15. Retry Rules

매우 중요.

필수 포함:

- Retry
- Backoff

---

반드시 설명:

- 일시 장애 대응

---

# 16. DLQ Rules

매우 중요.

필수 포함:

- Dead Letter Queue
- Failed Message

---

반드시 설명:

- 실패 메시지 격리
- 재처리

---

# 17. Ordering Rules

필수 포함:

- Ordering
- FIFO

---

반드시 설명:

- 순서 보장
- 병렬 처리 Trade-off

---

# 18. Delivery Guarantee Rules

매우 중요.

필수 포함:

- At Most Once
- At Least Once
- Exactly Once

---

반드시 설명:

- 유실
- 중복
- 보장 수준

---

# 19. Back Pressure Rules

필수 포함:

- Back Pressure
- Flow Control

---

반드시 설명:

- Consumer 처리 속도 문제

---

# 20. Monitoring Rules

필수 포함:

- Queue Depth
- Consumer Lag
- Throughput
- Error Rate

---

반드시 설명:

- 운영 핵심 지표

---

# 21. Troubleshooting Rules

반드시 포함 추천.

예:

- Queue Backlog
- Consumer Slow
- Retry Storm
- Message Loss
- Duplicate Message
- DLQ Overflow

---

형식:

문제:

원인:

해결:

---

# 22. Retrieval Optimization Rules

강조 대상:

- Message Queue
- Producer
- Consumer
- Queue
- Retry
- DLQ
- Pub/Sub
- RabbitMQ

키워드 반복 허용.

---

# 23. Version Rules

기준:

- RabbitMQ
- SQS
- Modern Queue Architecture

---

Legacy 제외.

---

# 24. Common Mistakes

자주 발생:

- Retry 무한 반복
- DLQ 미구성
- Ack 처리 실수
- Queue Backlog 방치
- Ordering 오해
- Consumer Scaling 미숙

---

# 25. Final Goal

MessageQueue Advanced RAG 문서는 Agent가 아래 수행 가능해야 한다.

- Retrieve MQ Pattern
- Design Queue Architecture
- Improve Reliability
- Solve Async Processing Issues
- Troubleshoot Messaging Problems

문서 품질이 Async Messaging 품질을 결정한다.
