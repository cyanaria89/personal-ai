# Redis Part 01 - Core

---

# 1. Redis Core

## 1.1 Redis Overview

### [개념]

Redis는 Memory 기반 In-Memory Key-Value Data Store다.

주요 목적:

- Fast Data Access
- Cache Storage
- Session Storage
- Real-time Data Processing

---

### [핵심]

Redis 핵심 특징:

- In-Memory
- Key-Value
- Single Thread Event Loop
- High Performance
- Low Latency

---

### [실무]

2026 실무 기준 Redis는 단순 Cache를 넘어 Backend Infrastructure Component로 사용된다.

주요 사용처:

- Cache
- Session
- Rate Limiting
- Distributed Lock
- Pub/Sub
- Queue

---

### [FAQ]

Q. Redis란?
A. Memory 기반 Key-Value Data Store다.

---

Q. Redis는 어디에 사용하는가?
A. Cache, Session, Lock, Queue 등에서 사용한다.

---

# 2. Why Redis

## 2.1 Why Fast

### [개념]

Redis가 빠른 이유는 모든 데이터를 Memory에 저장하기 때문이다.

---

### [핵심]

빠른 이유:

- Memory Access
- Minimal Disk I/O
- Efficient Data Structure
- Single Thread

---

### [Comparison]

| Category   | Redis     | RDBMS    |
| ---------- | --------- | -------- |
| Storage    | Memory    | Disk     |
| Latency    | Very Low  | Higher   |
| Throughput | Very High | Moderate |

---

### [FAQ]

Q. Redis가 빠른 이유는?
A. Disk 대신 Memory를 사용하기 때문이다.

---

# 3. Redis Flow

## 3.1 Basic Flow

### [Flow]

```text
Application
→ Redis Read
→ Cache Hit / Miss
→ DB Fallback
```

---

### [핵심]

Flow:

- Cache Hit → Redis Return
- Cache Miss → DB Query

---

### [FAQ]

Q. Cache Hit이란?
A. 요청 데이터가 Redis에 존재하는 상태다.

Q. Cache Miss란?
A. Redis에 데이터가 없어 DB 조회가 필요한 상태다.

---

# 4. Redis Key

## 4.1 Key Design

### [개념]

Redis는 Key 설계가 매우 중요하다.

---

### [핵심]

권장 규칙:

- Prefix 사용
- Domain 분리
- 명확한 Naming

---

### [예제]

```text
user:1
session:user:1
view_count:post:100
cache:product:200
```

---

### [Best Practice]

권장:

```text
domain:type:id
```

---

### [FAQ]

Q. Key Naming이 중요한 이유는?
A. 가독성, 관리성, 운영 효율에 직접 영향이 있다.

---

# 5. Data Structure Overview

## 5.1 Core Structures

### [개념]

Redis는 다양한 자료구조를 제공한다.

---

### [핵심]

핵심 자료구조:

```text
String     → Cache
Hash       → Object
List       → Queue
Set        → Unique Collection
Sorted Set → Ranking
Stream     → Event Queue
```

---

### [FAQ]

Q. Redis는 단순 Key-Value만 지원하는가?
A. 아니다. 다양한 자료구조를 지원한다.

---

# 6. String

## 6.1 String Overview

### [개념]

가장 기본적인 Redis 자료구조.

---

### [핵심]

주요 용도:

- Cache
- Counter
- Token
- Session

---

### [예제]

```text
SET user:1 "jun"
GET user:1
```

---

### [FAQ]

Q. String은 어디에 많이 사용하는가?
A. 단순 Cache와 Counter에 가장 많이 사용한다.

---

# 7. Hash

## 7.1 Hash Overview

### [개념]

Field-Value 기반 Object 구조.

---

### [핵심]

주요 용도:

- User Profile
- Session Data
- Object Cache

---

### [예제]

```text
HSET user:1 name jun
HSET user:1 age 30
```

---

### [FAQ]

Q. Hash 장점은?
A. Object-like 구조와 Partial Update 지원이다.

---

# 8. List

## 8.1 List Overview

### [개념]

순서가 있는 자료구조.

---

### [핵심]

주요 용도:

- Queue
- Recent History
- Feed

---

### [예제]

```text
LPUSH queue task1
RPOP queue
```

---

### [FAQ]

Q. List는 어디에 사용하는가?
A. Queue와 Feed 구현에 많이 사용한다.

---

# 9. Set

## 9.1 Set Overview

### [개념]

중복 없는 Collection.

---

### [핵심]

주요 용도:

- Unique Value
- Tag
- Membership Check

---

### [예제]

```text
SADD tags redis
SMEMBERS tags
```

---

### [FAQ]

Q. Set 장점은?
A. 중복 제거와 빠른 Membership 확인이다.

---

# 10. Sorted Set

## 10.1 Sorted Set Overview

### [개념]

Score 기반 정렬 자료구조.

---

### [핵심]

주요 용도:

- Ranking
- Leaderboard
- Score Ordering

---

### [예제]

```text
ZADD rank 100 user1
ZRANGE rank 0 -1
```

---

### [FAQ]

Q. Sorted Set은 어디에 사용하는가?
A. Ranking 구현에 가장 적합하다.

---

# 11. Stream

## 11.1 Stream Overview

### [개념]

Redis Stream은 Event Streaming 자료구조다.

---

### [핵심]

주요 용도:

- Event Queue
- Reliable Queue
- Message Processing

---

### [Flow]

```text
Producer
→ Stream
→ Consumer Group
→ Consumer
```

---

### [FAQ]

Q. Stream은 Pub/Sub와 무엇이 다른가?
A. Stream은 메시지를 저장하고 Consumer Group을 지원한다.

---

# 12. TTL

## 12.1 Expiration

### [개념]

TTL(Time To Live)은 Redis Key 생존 시간이다.

---

### [핵심]

핵심 명령어:

- TTL
- EXPIRE
- EX

---

### [예제]

```text
SET key value EX 300
```

---

### [실무]

TTL은 Cache 품질의 핵심이다.

---

### [FAQ]

Q. TTL이 중요한 이유는?
A. Cache 수명과 Memory 효율을 결정한다.

---

# 13. Persistence

## 13.1 Data Durability

### [개념]

Redis는 Memory DB지만 Persistence를 지원한다.

---

### [핵심]

지원 방식:

- RDB
- AOF

---

### [FAQ]

Q. Redis 재시작 시 데이터가 사라지는가?
A. Persistence 설정에 따라 복구 가능하다.

---

## 13.2 RDB

### [개념]

Snapshot 기반 저장.

---

### [핵심]

특징:

- 복구 빠름
- 파일 작음
- 일부 데이터 손실 가능

---

### [FAQ]

Q. RDB 장점은?
A. 복구가 빠르고 파일 크기가 작다.

---

## 13.3 AOF

### [개념]

Command Log 기반 저장.

---

### [Flow]

```text
Write Command
→ AOF Append
```

---

### [핵심]

특징:

- 데이터 안정성 높음
- 파일 크기 증가 가능

---

### [FAQ]

Q. AOF 장점은?
A. 데이터 안정성이 높다.

---

# 14. Redis Core Rules

## 14.1 Best Practice

### [Best Practice]

권장:

- Key Naming 규칙 통일
- TTL 적극 사용
- 자료구조 목적 맞게 선택

---

### [주의]

금지:

- TTL 없는 Cache 남용
- Key Naming 혼란
- Redis를 무제한 저장소처럼 사용

---

### [Checklist]

- Key Naming 적절한가
- TTL 설정했는가
- 자료구조 선택 적절한가

---

# 15. Common Mistakes

## 15.1 Frequent Issues

### [Troubleshooting]

문제:

Memory Full

원인:

TTL 미설정

해결:

Expiration 적용

---

문제:

Cache Miss 증가

원인:

TTL 너무 짧음

해결:

TTL 재조정

---

문제:

데이터 유실

원인:

Persistence 미설정

해결:

RDB/AOF 설정

---

# 16. Agent Decision Rules

## 16.1 Redis Routing

### [Flow]

```text
Simple Cache
→ String

Object Cache
→ Hash

Ranking
→ Sorted Set

Event Queue
→ Stream
```

---

### [핵심]

Backend Agent Routing 기준.

---

### [FAQ]

Q. 언제 Redis를 사용해야 하는가?
A. Low Latency와 High Throughput이 필요할 때다.

---

# Retrieval Queries

### [FAQ]

Q. Redis란?
A. Memory 기반 Key-Value Data Store다.

Q. Redis가 빠른 이유는?
A. Memory 기반이기 때문이다.

Q. Redis 핵심 자료구조는?
A. String, Hash, List, Set, Sorted Set, Stream.

Q. TTL이 중요한 이유는?
A. Cache 수명과 Memory 효율 때문이다.

Q. Redis Persistence 방식은?
A. RDB와 AOF.
