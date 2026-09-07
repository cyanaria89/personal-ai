# Redis Domain Rules

---

# 1. Domain Purpose

Redis Domain 문서는 Backend Agent / Review Agent용 RAG 문서이다.

목적:

- Cache Design Support
- Performance Optimization Support
- Distributed Coordination Support
- Session Management Support
- Redis Troubleshooting Support

우선순위:

1. Cache Strategy
2. Spring Redis Integration
3. Distributed Lock
4. Performance / Troubleshooting

---

# 2. Scope

포함 범위:

- Redis Core
- Data Structure
- String
- Hash
- List
- Set
- Sorted Set
- Stream
- TTL
- Expiration
- Eviction Policy
- Persistence
- RDB
- AOF
- Spring Data Redis
- RedisTemplate
- Spring Cache
- Cache
- Cache Aside
- Write Through
- Write Back
- Pub/Sub
- Distributed Lock
- Session Store
- Rate Limiting
- Performance Tuning
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

# 4. Redis Core Rules

Redis 문서는 Memory 기반 Key-Value 구조 중심으로 작성.

핵심 구조:

- Key
- Value
- TTL
- Memory
- Network

---

반드시 설명 포함:

- Redis 역할
- 왜 빠른가
- 언제 사용하는가
- 어떤 문제를 해결하는가

---

예:

```text
Application
→ Redis Read
→ Cache Hit / Miss
→ DB Fallback
```

---

# 5. Data Structure Rules

반드시 포함:

- String
- Hash
- List
- Set
- Sorted Set

---

반드시 설명:

- 특징
- 사용 케이스
- 시간복잡도
- 실무 활용

---

예:

```text
String     → Cache
Hash       → Object
List       → Queue
Set        → Unique Collection
Sorted Set → Ranking
```

---

금지:

자료구조 설명 생략.

---

# 6. String Rules

주요 용도:

- Cache
- Counter
- Token
- Session

---

예:

```text
user:1
view_count:post:100
```

---

반드시 설명:

- 가장 기본 자료구조
- 단순 Cache 용도

---

# 7. Hash Rules

주요 용도:

- User Profile
- Session Data
- Object Cache

---

예:

```text
user:1
name=jun
age=30
```

---

장점:

- Object-like 구조
- Partial Update 가능

---

# 8. List Rules

주요 용도:

- Queue
- Recent History
- Feed

---

예:

- LPUSH
- RPUSH
- LPOP
- RPOP

---

반드시 설명:

- FIFO / Stack
- Queue 활용

---

# 9. Set Rules

주요 용도:

- Unique Value
- Tag
- Membership Check

---

예:

- SADD
- SMEMBERS

---

장점:

- 중복 제거
- 빠른 Membership 확인

---

# 10. Sorted Set Rules

매우 중요.

주요 용도:

- Ranking
- Leaderboard
- Score-based Ordering

---

예:

- ZADD
- ZRANGE

---

반드시 설명:

- Score 기반 정렬
- Ranking 구현

---

# 11. Stream Rules

Redis 7.x 기준 중요도 상승.

반드시 포함:

- Stream
- XADD
- XREAD
- Consumer Group

---

주요 용도:

- Event Streaming
- Reliable Queue
- Message Processing

---

예:

Producer
→ Stream
→ Consumer Group
→ Consumer

---

반드시 설명:

- Pub/Sub와 차이
- Message Durability
- Consumer Group 구조

---

중요:

- Pub/Sub는 메시지 유실 가능.
- Stream은 메시지 저장 가능.

---

# 12. TTL Rules

TTL은 Redis 핵심.

반드시 포함:

- TTL
- EXPIRE
- Expiration

---

예:

```text
SET key value EX 300
```

---

반드시 설명:

- Cache 수명
- Expiration 전략

---

중요:

Redis 문서 품질은 TTL 설명 품질이 결정.

---

# 13. Eviction Policy Rules

필수 포함:

- noeviction
- allkeys-lru
- volatile-lru
- allkeys-lfu

---

반드시 설명:

- Memory Full 시 동작
- Cache 정책 영향

---

# 14. Persistence Rules

반드시 포함:

- Persistence
- RDB
- AOF

---

반드시 설명:

- Redis 데이터 영속성
- 재시작 시 데이터 복구
- Snapshot vs Append Log

---

RDB 특징:

- Snapshot 방식
- 복구 빠름
- 데이터 일부 손실 가능

---

AOF 특징:

- Command Log
- 데이터 안정성 높음
- 파일 크기 증가 가능

---

예:

Write Command
→ AOF Append

---

중요:

- Redis는 메모리 DB지만 영속성 지원 가능.

---

# 15. Spring Redis Rules

필수 포함:

- Spring Data Redis
- RedisTemplate
- Lettuce

---

예:

```java
private final RedisTemplate<String, Object> redisTemplate;
```

---

반드시 설명:

- Spring Boot 연동 방식
- Redis Client 역할

---

# 16 Spring Cache Rules

필수 포함:

- @Cacheable
- @CacheEvict
- @CachePut

---

예:

```java
@Cacheable(value = "users", key = "#id")
public User findUser(Long id)
```

---

반드시 설명:

- Spring Cache abstraction
- Redis backend 연동
- Cache Annotation 기반 자동 캐싱

---

비교:

- RedisTemplate → 직접 제어
- Spring Cache → 선언적 캐싱

---

# 17. RedisTemplate Rules

필수 포함:

- ValueOperations
- HashOperations
- SetOperations
- ListOperations

---

예:

```java
redisTemplate.opsForValue().set("key", "value");
```

---

반드시 설명:

- 자료구조별 접근 방식

---

# 18. Cache Rules

매우 중요.

반드시 포함:

- Cache
- Cache Hit
- Cache Miss
- Cache Invalidation

---

Flow:

```text
Request
→ Redis Check
→ Hit → Return
→ Miss → DB → Cache Save
```

---

반드시 설명:

- DB 부하 감소
- 응답 속도 개선

---

# 19. Cache Strategy Rules

필수 포함:

- Cache Aside
- Write Through
- Write Back
- Write Around

---

반드시 비교.

---

실무 권장:

대부분 Cache Aside.

---

# 20. Cache Aside Rules

핵심 전략.

Flow:

```text
Read
→ Cache Check
→ Miss
→ DB Query
→ Cache Save
```

---

반드시 설명:

- 가장 많이 사용하는 전략
- 장단점

---

# 21. Cache Problems Rules

반드시 포함:

- Cache Stampede
- Cache Penetration
- Cache Avalanche
- Hot Key

---

예:

문제:

원인:

해결:

---

중요:

Redis 실무 핵심 Troubleshooting.

---

# 22. Pub/Sub Rules

포함:

- Publisher
- Subscriber
- Channel

---

주요 용도:

- Notification
- Chat
- Broadcast

---

주의:

메시지 유실 가능성 설명 포함.

---

# 23. Distributed Lock Rules

매우 중요.

필수 포함:

- Lock
- Race Condition
- Distributed Lock

---

예:

- SETNX
- Redisson

---

반드시 설명:

- 동시성 제어
- 중복 실행 방지

---

# 24. Session Rules

포함:

- Session Store
- Login Session
- Shared Session

---

주요 용도:

- Multi Server Session
- Authentication Session

---

# 25. Rate Limiting Rules

포함:

- API Limit
- Token Bucket
- Sliding Window

---

예:

- 로그인 시도 제한
- API 호출 제한

---

반드시 설명:

- Abuse 방지
- DDoS 완화

---

# 26. Performance Rules

필수 포함:

- Memory Usage
- Latency
- Serialization
- Network
- Connection Pool

---

반드시 설명:

- 성능 병목
- Monitoring

---

# 27. High Availability Rules

Optional but Recommended.

포함:

- Replication
- Sentinel
- Cluster

---

반드시 설명:

- High Availability
- Failover
- Scaling

---

예:

Master
→ Replica

---

Sentinel:

- Failover 자동화

---

Cluster:

- Sharding 기반 수평 확장

---

# 28. Troubleshooting Rules

반드시 포함 추천.

예:

- Cache Miss High
- Redis Memory Full
- Hot Key
- Slow Command
- Connection Failed
- Eviction Issue

---

형식:

문제:

원인:

해결:

---

# 29. Retrieval Optimization Rules

강조 대상:

- Redis
- RedisTemplate
- Cache
- TTL
- Cache Aside
- Distributed Lock
- Rate Limiting
- Pub/Sub

키워드 반복 허용.

---

# 30. Version Rules

기준:

- Redis 7.x
- Spring Boot 3.x
- Java 21
- Spring Data Redis
- Lettuce
- Redisson

---

Legacy 제외.

---

# 31. Common Mistakes

자주 발생:

- TTL 미설정
- Cache Invalidation 누락
- Cache Stampede 방치
- Hot Key 미관리
- Eviction Policy 미설정
- Redis 무제한 저장소 오해
- Serialization 비용 무시
- Distributed Lock 오사용
- Pub/Sub 영속 Queue 오해

---

# 32. Final Goal

Redis RAG 문서는 Agent가 아래 수행 가능해야 한다.

- Retrieve Cache Pattern
- Design Cache Strategy
- Integrate Redis with Spring
- Solve Performance Issues
- Solve Redis Troubleshooting
- Suggest Best Practice

문서 품질이 Cache / Performance 품질을 결정한다.
