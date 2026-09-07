# Performance Tuning Domain Rules

---

# 1. Domain Purpose

Performance Tuning Domain 문서는 Backend Expert Agent / Review Agent / DevOps Agent용 RAG 문서 제작 규칙이다.

목적:

- Backend Performance Bottleneck 분석
- API Latency 개선
- Database Query Performance 개선
- JVM / Thread / Connection Pool 튜닝
- Cache Strategy 판단
- Async Processing 적용 판단
- Load Test / Stress Test 기준 제공
- Performance Review / Troubleshooting 지원

우선순위:

1. Bottleneck Identification
2. Measurement Before Optimization
3. Database Performance
4. Application Performance
5. Cache Strategy
6. Resource Tuning
7. Scalability

---

# 2. Scope

포함 범위:

- Performance Tuning Core
- Bottleneck Analysis
- API Latency
- Database Query Performance
- N+1 Problem
- Index Optimization
- Pagination Optimization
- Batch Processing
- Cache Strategy
- Redis Cache
- JVM Tuning
- GC Basics
- Thread Pool
- Connection Pool
- Async Processing
- Web Server / WAS Tuning
- Load Test
- Stress Test
- Monitoring Metrics
- Performance Troubleshooting

제외 범위:

- Kubernetes 운영 상세
- CI/CD 상세
- Elasticsearch 검색 성능 심화
- Kafka Broker 운영 튜닝 심화
- OS Kernel 튜닝 심화
- Frontend 렌더링 성능 최적화

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
- [Troubleshooting]
- [Checklist]
- [Comparison]

---

# 4. Performance Tuning Core Rules

Performance Tuning 문서는 추측이 아니라 측정 기반으로 작성한다.

핵심 원칙:

```text
Measure
→ Identify Bottleneck
→ Apply Tuning
→ Verify
→ Monitor
```

반드시 설명:

- 성능 최적화는 병목 지점 확인 후 진행
- 빠른 코드보다 병목 제거가 우선
- Query / Network / Thread / Memory / External API 구분
- 최적화 전후 수치를 비교
- 단일 요청 성능과 동시 요청 성능은 다름

금지:

- 측정 없는 튜닝 권장
- 무조건 Cache 적용
- 무조건 비동기 처리 권장
- 무조건 Index 추가
- 무조건 JVM 옵션 변경
- 성능 문제를 코드 스타일 문제로만 설명

---

# 5. Bottleneck Analysis Rules

Bottleneck Analysis는 성능 문서의 핵심이다.

필수 포함:

- API Response Time
- Database Query Time
- External API Latency
- CPU Usage
- Memory Usage
- GC Time
- Thread Pool 상태
- Connection Pool 상태
- Network Latency
- Lock / Contention

기본 Flow:

```text
Slow Request
→ Check API Latency
→ Check DB Query
→ Check External API
→ Check Thread / Connection Pool
→ Check CPU / Memory / GC
→ Identify Bottleneck
```

반드시 설명:

- 병목은 가장 느린 구간이 전체 성능을 제한하는 현상
- Application, DB, Network, External System을 구분
- 평균 응답 시간보다 p95 / p99 지표가 중요할 수 있음
- 단일 테스트와 부하 테스트 결과는 다를 수 있음

주의:

- 로그만 보고 원인을 단정하지 말 것
- CPU가 낮아도 DB / 외부 API 병목일 수 있음
- DB가 빨라도 Thread Pool 고갈로 느려질 수 있음
- Cache Hit Rate가 낮으면 Cache가 성능 개선에 도움 안 될 수 있음

---

# 6. API Latency Rules

API Latency 문서는 요청 처리 시간을 단계별로 분해한다.

필수 포함:

- Controller Processing Time
- Service Processing Time
- Repository Query Time
- External API Call Time
- Serialization / Deserialization
- Network Round Trip
- Authentication / Authorization Overhead

기본 Flow:

```text
Request
→ Filter / Security
→ Controller
→ Service
→ Repository / External API
→ Response Serialization
→ Response
```

반드시 설명:

- API Latency는 전체 요청 처리 시간
- DB Query가 가장 흔한 원인이지만 유일한 원인은 아님
- 인증 필터, 외부 API, JSON 변환도 병목 가능
- p95 / p99 Latency는 사용자 체감과 장애 분석에 중요

Best Practice:

- Slow API 로그 수집
- 요청별 Trace ID / Correlation ID 사용
- 주요 구간별 실행 시간 로깅
- Timeout 설정
- 불필요한 동기 외부 호출 제거

---

# 7. Database Performance Rules

Database Performance는 Backend Tuning에서 가장 중요한 영역이다.

필수 포함:

- Slow Query
- Index
- Execution Plan
- Join Optimization
- N+1 Problem
- Fetch Join
- Pagination
- Batch Insert / Update
- Transaction Lock
- Connection Pool

기본 Flow:

```text
Slow API
→ Slow Query Check
→ Execution Plan
→ Index Check
→ Join / Fetch Strategy Check
→ Pagination / Batch Check
→ Verify
```

반드시 설명:

- DB 성능 문제는 API 지연의 주요 원인
- Index는 조회 성능을 높이지만 쓰기 성능과 저장 공간 비용이 있음
- Execution Plan으로 실제 쿼리 수행 방식을 확인
- JPA 사용 시 N+1 문제를 반드시 확인
- 대용량 데이터는 Pagination / Batch 기준으로 설계

주의:

- 모든 컬럼에 Index 추가 금지
- LIKE `%keyword%` 검색은 일반 B-Tree Index 효과 제한
- Fetch Join 남용 시 중복 데이터와 페이징 문제가 생길 수 있음
- 긴 Transaction은 Lock과 Connection 점유를 증가시킴

---

# 8. N+1 Problem Rules

N+1 Problem은 JPA 성능 문서에서 반드시 독립적으로 다룬다.

필수 포함:

- Lazy Loading
- Eager Loading
- Fetch Join
- EntityGraph
- Batch Size
- DTO Projection
- QueryDSL Projection

기본 Flow:

```text
Find Parent List
→ Access Child Relation
→ Additional Query Per Parent
→ N+1 Problem
```

해결 전략:

```text
N+1 발생
→ Fetch Join 검토
→ EntityGraph 검토
→ Batch Size 검토
→ DTO Projection 검토
```

반드시 설명:

- N+1은 연관관계 접근 시 추가 쿼리가 반복 발생하는 문제
- Fetch Join은 즉시 해결책이 될 수 있지만 항상 정답은 아님
- 목록 조회는 DTO Projection이 더 적합할 수 있음
- 연관관계 조회 목적에 따라 전략을 선택해야 함

주의:

- EAGER Fetch를 기본 해결책으로 사용 금지
- Collection Fetch Join과 Pagination 조합 주의
- Fetch Join으로 너무 많은 데이터를 한 번에 가져오지 말 것

---

# 9. Index Optimization Rules

Index Optimization 문서는 조회 조건과 정렬 조건 중심으로 작성한다.

필수 포함:

- B-Tree Index
- Composite Index
- Covering Index
- Selectivity
- Cardinality
- WHERE 조건
- ORDER BY 조건
- Execution Plan

기본 판단:

```text
Query Pattern
→ WHERE Column
→ JOIN Column
→ ORDER BY Column
→ Selectivity
→ Index Design
```

반드시 설명:

- Index는 조회 패턴 기준으로 설계
- 자주 조회되는 조건 컬럼을 우선 검토
- 복합 Index는 컬럼 순서가 중요
- ORDER BY / LIMIT과 함께 사용될 수 있음
- Index는 쓰기 성능 저하와 저장 공간 증가를 유발할 수 있음

주의:

- 사용되지 않는 Index는 제거 후보
- 낮은 Cardinality 컬럼 단독 Index는 효과가 낮을 수 있음
- 함수 적용 컬럼은 Index 사용이 제한될 수 있음
- Index 추가 후 Execution Plan 확인 필수

---

# 10. Pagination Optimization Rules

Pagination 문서는 대용량 목록 조회 성능 중심으로 작성한다.

필수 포함:

- Offset Pagination
- Cursor Pagination
- Keyset Pagination
- Slice
- Page
- Count Query
- Infinite Scroll

비교:

| 방식              | 특징                       | 적합                 |
| ----------------- | -------------------------- | -------------------- |
| Offset Pagination | page, size 기반            | 일반 목록            |
| Cursor Pagination | 마지막 ID / 기준값 기반    | 무한 스크롤          |
| Slice             | 다음 페이지 존재 여부 중심 | 더보기 / 무한 스크롤 |
| Page              | 전체 개수 포함             | 관리자 목록          |

반드시 설명:

- Offset이 커질수록 성능 저하 가능
- Count Query는 대용량 테이블에서 비용이 클 수 있음
- 무한 스크롤은 Slice / Cursor 방식이 적합
- 정렬 기준은 안정적이어야 함

주의:

- 정렬 기준 없이 Cursor Pagination 구현 금지
- Offset Pagination을 대용량 무한 스크롤에 남용 금지
- Count Query가 필요 없는 화면에는 Page보다 Slice 고려

---

# 11. Batch Processing Rules

Batch Processing 문서는 대량 데이터 처리 기준을 포함한다.

필수 포함:

- Batch Insert
- Batch Update
- Chunk Processing
- Bulk Query
- Persistence Context Clear
- Transaction Size
- Memory Usage

기본 Flow:

```text
Large Data
→ Split into Chunks
→ Process Batch
→ Flush
→ Clear Persistence Context
→ Commit
```

반드시 설명:

- 대량 데이터는 한 번에 처리하지 않고 Chunk 단위로 처리
- JPA Batch 작업은 Persistence Context 메모리 증가를 고려
- Bulk Query는 Entity 상태와 Persistence Context 불일치 가능
- Transaction 크기를 적절히 제한해야 함

주의:

- 대량 Insert / Update를 단일 Transaction으로 처리 금지
- Bulk Update 후 영속성 컨텍스트 상태 불일치 주의
- Batch 작업 중 장애 발생 시 재처리 전략 필요

---

# 12. Cache Strategy Rules

Cache Strategy는 매우 중요하다.

필수 포함:

- Cache Aside
- Read Through
- Write Through
- Write Behind
- TTL
- Cache Hit Rate
- Cache Invalidation
- Redis Cache
- Local Cache
- Distributed Cache

기본 Flow:

```text
Request
→ Cache Check
→ Cache Hit: Return
→ Cache Miss: DB Query
→ Store Cache
→ Return
```

반드시 설명:

- Cache는 반복 조회가 많고 변경이 적은 데이터에 적합
- Cache Hit Rate가 낮으면 효과가 낮음
- Cache Invalidation이 가장 어려운 문제
- Local Cache와 Distributed Cache의 차이를 설명
- Redis는 분산 환경에서 공유 Cache로 자주 사용

주의:

- 모든 데이터를 Cache하지 말 것
- 자주 변경되는 데이터는 Cache 무효화 전략 필요
- 개인정보 / 민감정보 Cache 주의
- Cache와 DB 데이터 불일치 가능성 설명
- TTL 없이 영구 Cache 사용 금지

---

# 13. JVM Tuning Rules

JVM Tuning 문서는 기본 개념 중심으로 작성한다.

필수 포함:

- Heap Memory
- Stack Memory
- Young Generation
- Old Generation
- Garbage Collection
- GC Pause
- OOM
- JVM Options
- Heap Dump
- Thread Dump

기본 Flow:

```text
Memory Issue
→ Check Heap Usage
→ Check GC Frequency
→ Check GC Pause
→ Check Object Allocation
→ Heap Dump Analysis
```

반드시 설명:

- JVM 튜닝은 최후의 수단에 가깝다
- 대부분의 성능 문제는 Query, I/O, Connection Pool에서 먼저 발생
- GC 로그와 Heap 사용량을 보고 판단
- OOM은 메모리 부족뿐 아니라 Memory Leak 가능성도 있음

주의:

- 무작정 Heap만 늘리지 말 것
- GC 옵션 변경 전 원인 분석 필수
- Memory Leak은 코드 / 객체 참조 문제일 수 있음
- Heap Dump에는 민감정보가 포함될 수 있음

---

# 14. Thread Pool Rules

Thread Pool 문서는 동시 요청 처리와 병목 분석 중심으로 작성한다.

필수 포함:

- Tomcat Thread Pool
- Executor Thread Pool
- Core Pool Size
- Max Pool Size
- Queue Capacity
- Blocking I/O
- Async Processing
- Thread Starvation

기본 Flow:

```text
Request Increase
→ Thread Pool Usage Increase
→ Queue Wait
→ Response Delay
→ Thread Exhaustion
```

반드시 설명:

- Thread는 무한하지 않음
- Blocking I/O가 많으면 Thread 점유 시간이 길어짐
- Thread Pool 크기는 CPU, I/O, 요청 특성에 따라 달라짐
- Queue가 너무 크면 장애가 늦게 드러날 수 있음

주의:

- Thread Pool을 무조건 크게 설정하지 말 것
- DB Connection Pool보다 훨씬 큰 Thread Pool은 대기 증가 가능
- 비동기 처리도 Thread Pool을 사용함
- Thread Dump로 Blocked / Waiting 상태 확인

---

# 15. Connection Pool Rules

Connection Pool은 Backend 성능에서 매우 중요하다.

필수 포함:

- HikariCP
- Maximum Pool Size
- Minimum Idle
- Connection Timeout
- Idle Timeout
- Max Lifetime
- Pool Exhaustion
- DB Connection Limit

기본 Flow:

```text
Request
→ Need DB Connection
→ Borrow Connection
→ Execute Query
→ Return Connection
```

반드시 설명:

- Connection Pool은 DB 연결을 재사용하기 위한 구조
- Pool 크기가 작으면 대기 시간이 증가
- Pool 크기가 너무 크면 DB 부하가 증가
- 긴 Transaction은 Connection을 오래 점유
- Slow Query는 Connection Pool 고갈 원인이 될 수 있음

주의:

- Maximum Pool Size를 무조건 크게 설정 금지
- DB 허용 Connection 수 고려
- Transaction 안에서 외부 API 호출 금지
- Connection Leak 여부 확인

---

# 16. Async Processing Rules

Async Processing은 응답 시간 단축과 작업 분리에 사용한다.

필수 포함:

- `@Async`
- Executor
- CompletableFuture
- Event Listener
- Message Queue
- Retry
- Failure Handling

적합한 경우:

- 이메일 발송
- 알림 발송
- 로그 적재
- 통계 계산
- 외부 API 후처리
- 시간이 오래 걸리는 비핵심 작업

기본 Flow:

```text
Request
→ Core Transaction
→ Publish Async Task
→ Return Response
→ Process Background Task
```

반드시 설명:

- 비동기는 성능 개선 도구이지만 복잡도를 증가시킴
- 실패 처리 / 재시도 / 보상 로직 필요
- 트랜잭션 Commit 이후 실행 여부를 고려
- 중요한 작업은 Message Queue 사용 고려

주의:

- 핵심 성공 여부가 필요한 로직을 무조건 비동기로 분리하지 말 것
- `@Async` 내부 예외 처리 누락 주의
- 비동기 작업도 Thread Pool을 사용함
- 순서 보장이 필요한 작업은 별도 설계 필요

---

# 17. External API Performance Rules

외부 API 호출은 자주 발생하는 성능 병목이다.

필수 포함:

- Timeout
- Retry
- Circuit Breaker
- Bulkhead
- Rate Limit
- Fallback
- Connection Pool
- Idempotency

기본 Flow:

```text
Service
→ External API Client
→ Timeout / Retry
→ Fallback
→ Response
```

반드시 설명:

- 외부 API는 내부 DB보다 예측이 어렵다
- Timeout 없는 외부 호출은 장애 확산 원인이 됨
- Retry는 부하를 증가시킬 수 있음
- Circuit Breaker는 장애 전파를 줄이는 데 사용
- 외부 API 호출은 DB Transaction과 분리 고려

주의:

- 무제한 Retry 금지
- Transaction 내부에서 느린 외부 API 호출 금지
- Fallback 데이터의 정확성 한계 설명
- Idempotency 없는 재시도는 중복 처리 위험

---

# 18. Load Test Rules

Load Test 문서는 성능 검증 기준을 포함한다.

필수 포함:

- Load Test
- Stress Test
- Spike Test
- Soak Test
- Throughput
- Latency
- TPS / RPS
- Concurrent Users
- Error Rate
- p95 / p99

기본 Flow:

```text
Define Scenario
→ Set Load
→ Run Test
→ Collect Metrics
→ Identify Bottleneck
→ Tune
→ Re-test
```

반드시 설명:

- 부하 테스트는 실제 사용자 시나리오 기반으로 설계
- 평균 응답 시간만 보지 말고 p95 / p99 확인
- Error Rate와 Resource Usage를 함께 확인
- 테스트 환경과 운영 환경 차이를 명시

주의:

- 로컬 PC 테스트 결과를 운영 성능으로 일반화 금지
- DB 초기 데이터가 적으면 성능 문제가 드러나지 않을 수 있음
- Warm-up 없이 첫 결과만 보고 판단 금지
- 테스트 중 외부 API 호출 비용 / 제한 확인

---

# 19. Monitoring Metrics Rules

Performance 문서는 관측 가능한 지표를 포함해야 한다.

필수 포함:

- Request Count
- Error Rate
- Latency
- Throughput
- CPU Usage
- Memory Usage
- GC Time
- DB Query Time
- Connection Pool Usage
- Thread Pool Usage
- Cache Hit Rate

기본 지표 그룹:

```text
Application Metrics
→ JVM Metrics
→ DB Metrics
→ Cache Metrics
→ External API Metrics
→ Infrastructure Metrics
```

반드시 설명:

- 성능 개선은 지표로 검증해야 함
- Latency, Traffic, Error, Saturation 중심으로 확인
- Application 로그와 Metrics를 함께 봐야 함
- Observability 문서와 연결 가능

주의:

- 지표 수집 자체도 비용이 있음
- 너무 많은 로그는 성능과 저장소에 부담
- 지표 이름과 단위를 통일
- 알림 기준은 실제 장애 기준과 연결

---

# 20. Performance Review Rules

Performance Review 문서는 코드 리뷰 기준을 포함한다.

필수 체크:

- N+1 발생 가능성
- 불필요한 반복 Query
- 대용량 조회에 Pagination 적용 여부
- Count Query 필요 여부
- Transaction 범위 적절성
- 외부 API Timeout 설정 여부
- Cache 적용 타당성
- Batch 처리 필요 여부
- Thread / Connection Pool 고갈 가능성
- DTO Projection 필요 여부

Review Flow:

```text
Code Review
→ Query Review
→ Transaction Review
→ External API Review
→ Cache Review
→ Load Risk Review
```

주의:

- 모든 Review가 성능 튜닝으로 이어질 필요는 없음
- 실제 병목 가능성이 높은 부분부터 지적
- 코드 가독성과 성능의 균형 고려

---

# 21. Troubleshooting Rules

반드시 포함 추천.

형식:

```md
문제:

원인:

해결:
```

---

## Slow API

문제:

- API 응답 시간이 느림

원인:

- Slow Query
- N+1 Problem
- 외부 API 지연
- Connection Pool 대기
- 대량 데이터 직렬화

해결:

- API 구간별 시간 측정
- Slow Query / Execution Plan 확인
- N+1 로그 확인
- 외부 API Timeout 확인
- Pagination / Projection 적용

---

## Connection Pool Exhaustion

문제:

- DB Connection을 얻지 못해 요청이 대기하거나 실패함

원인:

- Slow Query
- 긴 Transaction
- Connection Leak
- Pool Size 부족
- DB Connection Limit 초과

해결:

- HikariCP Metrics 확인
- Slow Query 개선
- Transaction 범위 축소
- Leak Detection 검토
- Pool Size와 DB Limit 조정

---

## High CPU Usage

문제:

- CPU 사용률이 높음

원인:

- 과도한 연산
- 무한 루프
- Serialization 비용
- GC 과다
- 너무 많은 동시 요청

해결:

- Profiling
- Thread Dump 확인
- Hot Method 분석
- 불필요한 반복 로직 제거
- 부하 제한 / Queue 조정

---

## High Memory Usage

문제:

- Memory 사용량이 지속적으로 증가함

원인:

- 대량 데이터 메모리 적재
- Cache 과다 사용
- Memory Leak
- Persistence Context 증가
- 큰 Response 객체 생성

해결:

- Heap Dump 분석
- Pagination / Streaming 적용
- Cache TTL / Size 제한
- Batch 처리 시 flush / clear 적용
- 불필요한 객체 참조 제거

---

## N+1 Problem

문제:

- 목록 조회 시 Query가 과도하게 많이 발생함

원인:

- Lazy Loading 연관관계 반복 접근
- Fetch 전략 미설계

해결:

- Fetch Join
- EntityGraph
- Batch Size
- DTO Projection
- QueryDSL Projection 검토

---

## Cache Ineffective

문제:

- Cache를 적용했지만 성능 개선이 없음

원인:

- Cache Hit Rate 낮음
- TTL이 너무 짧음
- Key 설계 부적절
- 자주 변경되는 데이터 Cache
- Cache Serialization 비용 큼

해결:

- Cache Hit Rate 측정
- Key 전략 수정
- TTL 조정
- Cache 대상 재선정
- Local Cache / Redis Cache 비교

---

# 22. Best Practice Rules

Best Practice:

- 최적화 전 반드시 측정
- Slow API부터 개선
- DB Query와 N+1 먼저 확인
- 대용량 조회에는 Pagination 적용
- 무한 스크롤은 Slice / Cursor 고려
- 반복 조회 + 낮은 변경 빈도에 Cache 적용
- Transaction 범위는 짧게 유지
- 외부 API 호출에는 Timeout 설정
- 비핵심 후처리는 Async / Event / Message Queue 고려
- Load Test 후 병목을 다시 확인
- p95 / p99 Latency를 확인
- 튜닝 전후 수치 기록

---

# 23. Comparison Rules

성능 문서는 비교 기준을 포함한다.

필수 비교 대상:

- Offset Pagination vs Cursor Pagination
- Page vs Slice
- Fetch Join vs EntityGraph vs Batch Size
- Entity 조회 vs DTO Projection
- Local Cache vs Redis Cache
- Sync Processing vs Async Processing
- Scale Up vs Scale Out
- Thread Pool 증가 vs Query 최적화
- Index 추가 vs Query 구조 변경

예시:

| 비교 | Offset Pagination     | Cursor Pagination  |
| ---- | --------------------- | ------------------ |
| 방식 | page / size 기반      | 마지막 기준값 기반 |
| 장점 | 구현 쉬움             | 대용량에서 안정적  |
| 단점 | Offset 증가 시 느려짐 | 정렬 기준 필요     |
| 적합 | 일반 게시판           | 무한 스크롤        |

---

# 24. Checklist Rules

Performance 문서에는 Checklist를 포함할 수 있다.

예시:

```md
### [Checklist]

- [ ] Slow API를 측정했는가?
- [ ] Slow Query를 확인했는가?
- [ ] Execution Plan을 확인했는가?
- [ ] N+1 Problem을 확인했는가?
- [ ] Pagination이 적용되어 있는가?
- [ ] Transaction 범위가 적절한가?
- [ ] 외부 API Timeout이 설정되어 있는가?
- [ ] Cache 적용 기준이 명확한가?
- [ ] Connection Pool 사용률을 확인했는가?
- [ ] p95 / p99 Latency를 확인했는가?
```

---

# 25. Retrieval Optimization Rules

강조 대상 키워드:

- Performance Tuning
- Bottleneck Analysis
- API Latency
- Slow Query
- Execution Plan
- Index Optimization
- N+1 Problem
- Fetch Join
- EntityGraph
- Batch Size
- DTO Projection
- Pagination
- Cursor Pagination
- Slice
- Page
- Cache Strategy
- Cache Hit Rate
- Cache Invalidation
- Redis Cache
- JVM Tuning
- GC Pause
- Heap Dump
- Thread Dump
- Thread Pool
- Connection Pool
- HikariCP
- Async Processing
- External API Timeout
- Circuit Breaker
- Load Test
- Stress Test
- p95
- p99
- Throughput
- Error Rate

키워드 반복 허용.

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

예:

- API가 느릴 때 어디부터 봐야 해?
- JPA N+1 문제는 어떻게 해결해?
- Index는 언제 추가해야 해?
- Page와 Slice 차이는?
- Cursor Pagination은 언제 써?
- Cache는 언제 적용해야 해?
- Redis Cache는 언제 써?
- Connection Pool 고갈은 왜 발생해?
- Thread Pool은 어떻게 튜닝해?
- 외부 API 호출이 느릴 때 어떻게 해야 해?

---

# 26. Version Rules

기준:

- Java 21
- Spring Boot 3.x
- Spring Framework 6.x
- Spring Data JPA
- QueryDSL
- HikariCP
- Redis
- MySQL / PostgreSQL 기준
- Modern Backend Architecture

Legacy 제외:

- Spring Boot 1.x / 2.x 전용 방식
- XML 기반 Spring 설정 중심
- 구형 WAS 튜닝 중심 설명
- 근거 없는 JVM 옵션 나열

---

# 27. Common Mistakes

자주 발생:

- 측정 없이 최적화 시작
- Slow Query 확인 없이 코드만 수정
- N+1 문제를 EAGER Fetch로 해결하려 함
- 모든 컬럼에 Index 추가
- 대용량 목록에 Offset Pagination만 사용
- Count Query 비용을 고려하지 않음
- 모든 데이터를 Cache하려 함
- Cache Invalidation 전략 없음
- Transaction 안에서 외부 API 호출
- Thread Pool을 무조건 크게 설정
- Connection Pool을 무조건 크게 설정
- Heap Memory만 늘리고 원인 분석하지 않음
- Load Test 없이 운영 성능을 추측
- 평균 응답 시간만 보고 p95 / p99를 무시

---

# 28. Final Goal

Performance Tuning RAG 문서는 Agent가 아래를 수행 가능해야 한다.

- Slow API 원인 분석
- Bottleneck 식별
- Database Query 성능 개선 방향 제안
- N+1 Problem 탐지 및 해결 제안
- Index 적용 여부 판단
- Pagination 전략 선택
- Cache 적용 여부 판단
- Transaction 범위 성능 검토
- Thread Pool / Connection Pool 문제 판단
- JVM / GC 문제 기초 분석
- Async Processing 적용 여부 판단
- Load Test 결과 해석
- Performance Review
- Troubleshooting Direction 제안

문서 품질이 Backend Performance 품질을 결정한다.

---

# Retrieval Queries

### [FAQ]

Q. API가 느릴 때 어디부터 확인해야 해?

A.
API 구간별 시간을 측정하고, Slow Query, N+1, 외부 API 지연, Connection Pool 대기 여부를 순서대로 확인한다.

Q. 성능 튜닝은 어디서부터 시작해야 해?

A.
추측하지 말고 측정부터 시작한다. Latency, Query Time, CPU, Memory, Thread, Connection Pool 지표를 확인한다.

Q. JPA N+1 문제는 어떻게 해결해?

A.
Fetch Join, EntityGraph, Batch Size, DTO Projection을 조회 목적에 맞게 선택한다. EAGER Fetch는 기본 해결책으로 사용하지 않는다.

Q. Index는 언제 추가해야 해?

A.
자주 사용되는 WHERE, JOIN, ORDER BY 조건을 기준으로 Execution Plan을 확인한 뒤 추가한다.

Q. 모든 컬럼에 Index를 추가하면 빨라져?

A.
아니다. Index는 쓰기 성능과 저장 공간 비용이 있고, 조회 패턴에 맞지 않으면 효과가 낮다.

Q. Page와 Slice 차이는?

A.
Page는 전체 개수 Count Query를 포함하고, Slice는 다음 페이지 존재 여부 중심이다. 무한 스크롤은 Slice가 더 적합한 경우가 많다.

Q. Cursor Pagination은 언제 써?

A.
대용량 데이터에서 Offset이 커져 성능 저하가 발생하거나 무한 스크롤을 구현할 때 사용한다.

Q. Cache는 언제 적용해야 해?

A.
반복 조회가 많고 변경 빈도가 낮으며 Cache Hit Rate가 높을 수 있는 데이터에 적용한다.

Q. Redis Cache는 언제 써?

A.
여러 서버가 같은 Cache를 공유해야 하거나 분산 환경에서 Cache 일관성이 필요할 때 사용한다.

Q. Cache 적용 후에도 느린 이유는?

A.
Cache Hit Rate가 낮거나 Key 설계가 잘못되었거나 Cache Serialization 비용이 클 수 있다.

Q. Connection Pool 고갈은 왜 발생해?

A.
Slow Query, 긴 Transaction, Connection Leak, Pool Size 부족, DB Connection Limit 초과 때문에 발생할 수 있다.

Q. Thread Pool은 크게 잡으면 무조건 좋아?

A.
아니다. Thread가 많아도 DB Connection, CPU, Blocking I/O가 병목이면 대기와 부하만 증가할 수 있다.

Q. 외부 API 호출이 느릴 때 어떻게 해야 해?

A.
Timeout, Retry 제한, Circuit Breaker, Fallback을 검토하고 DB Transaction 안에서 오래 호출하지 않도록 분리한다.

Q. 비동기 처리는 언제 써야 해?

A.
이메일, 알림, 로그, 통계처럼 핵심 응답 이후 처리해도 되는 작업에 적합하다.

Q. JVM 튜닝은 먼저 해야 해?

A.
아니다. 대부분은 Query, I/O, Connection Pool 문제가 먼저다. JVM 튜닝은 GC 로그와 Heap 사용량을 보고 판단한다.

Q. Load Test에서 어떤 지표를 봐야 해?

A.
Throughput, Average Latency, p95, p99, Error Rate, CPU, Memory, DB Connection, Thread Pool 사용률을 함께 확인한다.
