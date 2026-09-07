# Redis Part 04 - Pub/Sub

---

# 1. Redis Pub/Sub Core

## 1.1 Pub/Sub Overview

### [개념]

Redis Pub/Sub은 Publisher가 메시지를 발행(Publish)하면 Subscriber가 실시간으로 수신(Subscribe)하는 Message Communication Pattern이다.

주요 목적:

- Real-time Messaging
- Event Notification
- Async Communication

---

### [핵심]

핵심 구성:

- Publisher
- Channel
- Subscriber

---

### [실무]

2026 실무 기준 Redis Pub/Sub은 Lightweight Real-time Messaging 용도로 자주 사용된다.

주요 사용처:

- Chat
- Notification
- Event Broadcast
- WebSocket Broadcast

---

### [FAQ]

Q. Redis Pub/Sub이란?
A. Publisher가 메시지를 발행하고 Subscriber가 수신하는 메시징 구조다.

Q. Redis Pub/Sub은 어디에 사용하는가?
A. Chat, Notification, Event Broadcast에 많이 사용한다.

---

# 2. Pub/Sub Flow

## 2.1 Message Flow

### [Flow]

```text
Publisher
→ Channel
→ Subscriber
```

---

### [핵심]

Flow:

- Publisher → Message Publish
- Channel → Message Broadcast
- Subscriber → Message Receive

---

### [FAQ]

Q. Channel이란?
A. Publisher와 Subscriber를 연결하는 메시지 통로다.

---

# 3. Publish

## 3.1 Message Publish

### [개념]

Publisher는 특정 Channel에 메시지를 발행한다.

---

### [예제]

```text
PUBLISH chat-room-1 "hello"
```

---

### [FAQ]

Q. Publish란?
A. 특정 Channel에 메시지를 전송하는 것이다.

---

# 4. Subscribe

## 4.1 Message Subscribe

### [개념]

Subscriber는 Channel 구독 후 메시지를 수신한다.

---

### [예제]

```text
SUBSCRIBE chat-room-1
```

---

### [FAQ]

Q. Subscribe란?
A. 특정 Channel 메시지를 수신하도록 등록하는 것이다.

---

# 5. Pub/Sub Characteristics

## 5.1 Core Features

### [개념]

Redis Pub/Sub은 Broadcast 기반이다.

---

### [핵심]

특징:

- Real-time
- Lightweight
- Broadcast
- Fire-and-Forget

---

### [주의]

중요:

- Message Persistence 없음
- Offline Subscriber 수신 불가
- Replay 불가

---

### [FAQ]

Q. Pub/Sub의 가장 큰 특징은?
A. 실시간 Broadcast 구조라는 점이다.

---

# 6. Pub/Sub vs Stream

## 6.1 Comparison

### [개념]

Pub/Sub과 Stream은 목적이 다르다.

---

### [Comparison]

| Category            | Pub/Sub   | Stream         |
| ------------------- | --------- | -------------- |
| Message Persistence | No        | Yes            |
| Replay              | No        | Yes            |
| Consumer Group      | No        | Yes            |
| Use Case            | Broadcast | Reliable Queue |

---

### [핵심]

선택 기준:

```text
Real-time Broadcast
→ Pub/Sub

Reliable Queue
→ Stream
```

---

### [FAQ]

Q. Pub/Sub과 Stream 차이는?
A. Pub/Sub은 Broadcast, Stream은 Reliable Queue다.

---

# 7. Spring Redis Pub/Sub

## 7.1 Integration

### [개념]

Spring Redis로 Pub/Sub 구현 가능.

---

### [핵심]

핵심 구성:

- RedisTemplate
- MessageListener
- RedisMessageListenerContainer

---

### [FAQ]

Q. Spring Redis에서도 Pub/Sub 가능한가?
A. 가능하다.

---

## 7.2 Publisher Example

### [예제]

```java
redisTemplate.convertAndSend(
        "chat-room-1",
        message
);
```

---

### [FAQ]

Q. 메시지 발행은 어떻게 하는가?
A. convertAndSend()를 사용한다.

---

## 7.3 Subscriber Example

### [예제]

```java
public class RedisSubscriber
        implements MessageListener {
}
```

---

### [FAQ]

Q. Subscriber 구현은 어떻게 하는가?
A. MessageListener 구현 방식이 일반적이다.

---

# 8. Pub/Sub Use Cases

## 8.1 Practical Usage

### [핵심]

대표 사용 사례:

- Chat Room Broadcast
- Notification Broadcast
- WebSocket Event Broadcast
- Cache Invalidation Event

---

### [실무]

특히 Multi Server 환경에서 유용하다.

예:

```text
Server A Publish
→ Redis Channel
→ Server B/C Receive
```

---

### [FAQ]

Q. Pub/Sub이 실무에서 유용한 이유는?
A. 서버 간 Event Broadcast가 쉽기 때문이다.

---

# 9. Session Store

## 9.1 Redis Session

### [개념]

Redis는 Pub/Sub 외에도 Session Store로 자주 사용된다.

---

### [핵심]

주요 용도:

- Login Session
- Shared Session
- Multi Server Session

---

### [FAQ]

Q. Redis는 Session Store로도 사용하는가?
A. 그렇다. Multi Server 환경에서 매우 많이 사용한다.

---

# 10. Rate Limiting

## 10.1 API Protection

### [개념]

Redis는 API Rate Limiting 구현에도 자주 사용된다.

---

### [핵심]

주요 용도:

- Request Count
- Token Bucket
- API Abuse Prevention

---

### [예제]

```text
INCR api:user:1
EXPIRE api:user:1 60
```

---

### [FAQ]

Q. Redis는 Rate Limiting에도 사용하는가?
A. 그렇다. Counter 기반 구현이 쉽다.

---

# 11. Limitations

## 11.1 Pub/Sub Problems

### [개념]

Pub/Sub은 강력하지만 제한이 있다.

---

### [핵심]

한계:

- Message Loss 가능
- Durability 없음
- Replay 불가

---

### [FAQ]

Q. Pub/Sub 단점은?
A. 메시지 유실 가능성과 Persistence 부재다.

---

# 12. Pub/Sub Rules

## 12.1 Best Practice

### [Best Practice]

권장:

- Real-time Broadcast에 사용
- Channel Naming 규칙 유지
- Durable Queue는 Stream 고려

---

### [주의]

금지:

- Message Durability 기대
- Critical Queue 용도 사용
- Persistence 필요 시스템 사용

---

### [Checklist]

- Broadcast 용도인가
- Persistence 필요한가
- Stream이 더 적합한가

---

# 13. Common Mistakes

## 13.1 Frequent Issues

### [Troubleshooting]

문제:

Message Loss

원인:

Offline Subscriber

해결:

Stream 검토

---

문제:

Message Not Received

원인:

Channel 불일치

해결:

Channel Name 확인

---

문제:

Subscriber 지연

원인:

High Traffic

해결:

Scaling 고려

---

# 14. Agent Decision Rules

## 14.1 Routing

### [Flow]

```text
Real-time Broadcast
→ Pub/Sub

Reliable Queue
→ Stream

Durable Messaging
→ Kafka / MQ
```

---

### [핵심]

Backend Agent Routing 기준.

---

### [FAQ]

Q. 언제 Pub/Sub을 사용해야 하는가?
A. Real-time Broadcast가 필요할 때다.

---

# Retrieval Queries

### [FAQ]

Q. Redis Pub/Sub이란?
A. Publisher가 메시지를 발행하고 Subscriber가 수신하는 구조다.

Q. Pub/Sub 핵심 특징은?
A. Real-time Broadcast.

Q. Pub/Sub과 Stream 차이는?
A. Pub/Sub은 Broadcast, Stream은 Reliable Queue.

Q. Pub/Sub 단점은?
A. Message Loss 가능성과 Persistence 부재.

Q. 언제 Pub/Sub을 사용하는가?
A. 실시간 이벤트 브로드캐스트가 필요할 때.
