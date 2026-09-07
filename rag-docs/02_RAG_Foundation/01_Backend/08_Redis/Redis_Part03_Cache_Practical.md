# Redis Part 03 - Cache Practical

---

# 1. Cache Core

## 1.1 Cache Overview

### [개념]

Cache는 자주 조회되는 데이터를 빠른 저장소에 저장하여 응답 속도를 높이는 전략이다.

주요 목적:

- Response Speed Improvement
- DB Load Reduction
- Throughput Improvement

---

### [핵심]

Cache 핵심 개념:

- Cache Hit
- Cache Miss
- Cache Invalidation
- TTL

---

### [실무]

2026 실무 기준 Redis의 가장 대표적인 사용 목적은 Cache다.

주요 대상:

- Product Detail
- User Profile
- Popular Data
- Ranking Data

---

### [FAQ]

Q. Cache란?
A. 자주 조회되는 데이터를 빠르게 반환하기 위한 저장 전략이다.

Q. Cache 목적은?
A. 응답 속도 향상과 DB 부하 감소다.

---

# 2. Cache Flow

## 2.1 Cache Hit / Miss

### [Flow]

```text
Request
→ Redis Check
→ Hit → Return
→ Miss → DB Query
```

---

### [핵심]

- Hit → Redis Return
- Miss → DB Fallback

---

### [FAQ]

Q. Cache Hit란?
A. 요청 데이터가 Cache에 존재하는 상태다.

Q. Cache Miss란?
A. Cache에 데이터가 없어 DB 조회가 필요한 상태다.

---

# 3. Cache Aside

## 3.1 Cache Aside Strategy

### [개념]

가장 많이 사용하는 Cache 전략.

---

### [Flow]

```text
Read Request
→ Cache Check
→ Miss
→ DB Query
→ Cache Save
```

---

### [핵심]

장점:

- 구현 쉬움
- 실무 활용도 높음

단점:

- Cache Miss 발생 가능

---

### [실무]

대부분 Backend 서비스 기본 전략.

---

### [FAQ]

Q. 가장 많이 쓰는 Cache 전략은?
A. Cache Aside다.

---

# 4. Write Through

## 4.1 Write Through Strategy

### [개념]

Write 시 Cache와 DB를 동시에 업데이트.

---

### [Flow]

```text
Write Request
→ Cache Write
→ DB Write
```

---

### [핵심]

장점:

- Data Consistency 높음

단점:

- Write Latency 증가

---

### [FAQ]

Q. Write Through 장점은?
A. 데이터 일관성이 높다.

---

# 5. Write Back

## 5.1 Write Back Strategy

### [개념]

Write는 Cache에 먼저 저장 후 나중에 DB 반영.

---

### [Flow]

```text
Write Request
→ Cache Write
→ Async DB Write
```

---

### [핵심]

장점:

- Write 성능 우수

단점:

- 데이터 유실 위험

---

### [FAQ]

Q. Write Back 단점은?
A. 장애 시 데이터 유실 가능성이 있다.

---

# 6. Write Around

## 6.1 Write Around Strategy

### [개념]

Write는 DB만 저장하고 Cache는 건드리지 않는다.

---

### [핵심]

장점:

- 불필요 Cache 방지

단점:

- Read 시 Miss 가능

---

### [FAQ]

Q. Write Around는 언제 좋은가?
A. Write 빈도가 높고 Read 빈도가 낮을 때다.

---

# 7. Cache Invalidation

## 7.1 Cache Invalidation

### [개념]

오래된 Cache 제거 전략.

---

### [핵심]

방법:

- TTL Expiration
- Manual Delete
- Event-based Update

---

### [FAQ]

Q. Cache Invalidation이 중요한 이유는?
A. Stale Data 방지 때문이다.

---

# 8. Eviction Policy

## 8.1 Memory Full Strategy

### [개념]

Memory Full 시 어떤 Key를 제거할지 결정한다.

---

### [핵심]

대표 정책:

- noeviction
- allkeys-lru
- volatile-lru
- allkeys-lfu

---

### [FAQ]

Q. Eviction Policy란?
A. 메모리 부족 시 Key 제거 정책이다.

---

# 9. Cache Problems

## 9.1 Cache Stampede

### [개념]

동시에 많은 Cache Miss 발생.

---

### [핵심]

원인:

- Popular Key Expired

해결:

- TTL Randomization
- Lock
- Prewarming

---

### [FAQ]

Q. Cache Stampede란?
A. 동시 Cache Miss로 DB 부하가 급증하는 현상이다.

---

## 9.2 Cache Penetration

### [개념]

존재하지 않는 데이터 반복 조회.

---

### [핵심]

원인:

- Invalid Request

해결:

- Null Cache
- Bloom Filter

---

### [FAQ]

Q. Cache Penetration이란?
A. 존재하지 않는 데이터 조회가 반복되는 현상이다.

---

## 9.3 Cache Avalanche

### [개념]

많은 Key TTL이 동시에 만료.

---

### [핵심]

원인:

- Same TTL

해결:

- Random TTL

---

### [FAQ]

Q. Cache Avalanche란?
A. 대량 Key가 동시에 만료되는 현상이다.

---

## 9.4 Hot Key

### [개념]

특정 Key에 트래픽 집중.

---

### [핵심]

문제:

- CPU Spike
- Latency Increase

해결:

- Sharding
- Local Cache

---

### [FAQ]

Q. Hot Key란?
A. 특정 Key에 요청이 과도하게 몰리는 현상이다.

---

# 10. Cache Practical Rules

## 10.1 Best Practice

### [Best Practice]

권장:

- Cache Aside 기본 전략
- TTL 반드시 설정
- Invalidation 전략 설계
- Hot Key 모니터링

---

### [주의]

금지:

- TTL 없는 Cache
- Invalidation 누락
- Cache Problem 방치

---

### [Checklist]

- Cache Strategy 선택
- TTL 설정
- Invalidation 설계
- Cache Problem 대응

---

# 11. Common Mistakes

## 11.1 Frequent Issues

### [Troubleshooting]

문제:

Cache Hit Rate 낮음

원인:

TTL 설정 문제

해결:

TTL 재조정

---

문제:

DB 부하 급증

원인:

Stampede

해결:

Lock / Random TTL

---

문제:

Stale Data 발생

원인:

Invalidation 실패

해결:

Cache 삭제 전략 강화

---

# 12. Agent Decision Rules

## 12.1 Cache Routing

### [Flow]

```text
Read Heavy
→ Cache Aside

Strong Consistency
→ Write Through

Write Heavy
→ Write Back
```

---

### [핵심]

Backend Agent Routing 기준.

---

### [FAQ]

Q. 언제 Cache Aside를 사용하는가?
A. Read-heavy 서비스에서 가장 적합하다.

---

# Retrieval Queries

### [FAQ]

Q. Cache Aside란?
A. Read 시 Cache Miss면 DB 조회 후 Cache 저장 전략이다.

Q. 가장 많이 사용하는 Cache 전략은?
A. Cache Aside.

Q. Cache Stampede란?
A. 동시 Cache Miss로 DB 부하가 급증하는 현상이다.

Q. Cache Avalanche란?
A. 대량 Key가 동시에 만료되는 현상이다.

Q. Hot Key란?
A. 특정 Key에 요청이 집중되는 현상이다.
