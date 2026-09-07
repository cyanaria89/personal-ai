# SQL Part05 - Backend Integration, Troubleshooting, Anti Pattern

---

# 1. Backend Integration Foundation

## 1.1 SQL and Backend Repository

### [개념]

SQL은 Backend Repository 계층에서 실제 데이터 조회와 변경으로 연결된다.

Spring Boot Backend에서는 SQL 사고를 기반으로 Spring Data JPA Repository, JPQL, QueryDSL, Native Query를 선택한다.

Backend Agent는 요구사항을 SQL Query Purpose로 해석한 뒤 Repository 구현 방식까지 연결해야 한다.

---

### [핵심]

Backend Query 구현 방식:

- Spring Data JPA Repository Method
- Derived Query Method
- JPQL
- QueryDSL
- Native Query
- DTO Projection
- Entity Graph
- Fetch Join
- Pagination
- Transaction

선택 기준:

- Query Purpose
- Entity Relationship
- Dynamic Condition 여부
- Join 복잡도
- Pagination 필요 여부
- DTO Projection 필요 여부
- DB 특화 기능 필요 여부
- 성능 검토 필요 여부

---

### [실무]

2026 Backend 실무 기준 Repository 선택 Flow:

```text
Service Requirement
→ Query Purpose 확인
→ Entity Relationship 확인
→ 단순 CRUD 여부 확인
→ Derived Query 가능 여부 확인
→ JPQL 필요 여부 확인
→ QueryDSL 필요 여부 확인
→ Native Query 필요 여부 확인
→ Pagination / Index 검토
→ Test / Review
```

예시:

```text
회원 ID로 단건 조회
→ 단순 PK 조회
→ JpaRepository.findById 가능

사용자 이메일 중복 확인
→ 존재 여부 확인
→ existsByEmail 가능

복합 검색 조건 축제 목록
→ Dynamic Condition
→ QueryDSL 적합

DB 특화 Full Text Search
→ Native Query 검토
```

---

### [FAQ]

Q. SQL과 Repository는 왜 연결해서 봐야 해?
A. Repository Method, JPQL, QueryDSL, Native Query가 결국 DB에서 SQL로 실행되기 때문이다.

Q. 단순 조회는 무엇으로 구현해?
A. findById, findByEmail, existsByEmail 같은 Spring Data JPA Repository Method로 충분한 경우가 많다.

Q. 복잡한 검색 조건은 무엇이 적합해?
A. 동적 조건 조합이 많은 경우 QueryDSL이 적합하다.

Q. Native Query는 언제 사용해?
A. JPQL이나 QueryDSL로 표현하기 어렵거나 DB 특화 기능이 필요한 경우 검토한다.

---

## 1.2 Derived Query Method Rules

### [개념]

Derived Query Method는 Spring Data JPA가 Method 이름을 해석하여 Query를 생성하는 방식이다.

단순 조건 조회, 존재 여부 확인, 개수 조회에는 적합하지만 복잡한 JOIN, 동적 검색, 성능 최적화에는 한계가 있다.

---

### [핵심]

적합한 상황:

- 단건 조회
- 존재 여부 확인
- 단순 조건 목록
- 단순 Count
- 단순 Delete
- Unique Column 조회
- FK 기반 조회

예시 Method:

- findByEmail
- existsByEmail
- findByUserId
- findByUserIdAndFestivalId
- countByFestivalId
- deleteByUserIdAndFestivalId
- findByUserIdOrderByCreatedAtDesc

주의 상황:

- Method 이름 과도하게 길어짐
- 복잡한 OR 조건
- 동적 검색 조건
- 복잡한 JOIN
- DTO Projection 복잡
- 성능 Hint 필요
- Fetch 전략 제어 필요

---

### [실무]

단순 존재 확인:

```java
boolean existsByEmail(String email);
```

사용자별 찜 여부 확인:

```java
boolean existsByUser_UserIdAndFestival_FestivalId(Long userId, Long festivalId);
```

사용자별 알림 목록:

```java
Slice<Notification> findByUser_UserIdOrderByCreatedAtDesc(Long userId, Pageable pageable);
```

권장:

- 단순 조건은 Derived Query Method 사용
- Method 이름이 길어지면 JPQL / QueryDSL 검토
- 동적 조건은 QueryDSL 검토
- Pageable과 Sort 사용 시 정렬 안정성 확인
- exists Method는 중복 검증과 권한 확인에 활용 가능

주의:

- Derived Query가 생성하는 SQL을 로그로 확인
- Entity 연관 경로가 길어지면 가독성 저하
- 1:N 관계 조회에서 중복 Row 주의
- Pagination과 Fetch Join은 별도 검토

---

### [FAQ]

Q. Derived Query Method는 언제 써?
A. 단순 조건 조회, 존재 여부 확인, Count, FK 기반 조회처럼 Query가 단순할 때 사용한다.

Q. Method 이름이 길어지면 어떻게 해?
A. JPQL이나 QueryDSL로 분리하는 것이 좋다.

Q. existsBy는 언제 유용해?
A. 이메일 중복 확인, 찜 여부 확인, 권한 Row 존재 확인처럼 존재 여부만 필요할 때 유용하다.

Q. Derived Query도 SQL 확인이 필요해?
A. 필요하다. 실제 생성 SQL과 Join 방식, Pagination 동작을 로그로 확인하는 것이 좋다.

---

## 1.3 JPQL Rules

### [개념]

JPQL은 Entity 객체와 Entity Relationship을 기준으로 작성하는 JPA Query Language다.

JPQL은 Table이 아니라 Entity와 Field 이름을 사용하며 DB 독립적인 Query 작성에 적합하다.

---

### [핵심]

JPQL 특징:

- Entity 중심
- Field 이름 사용
- 객체 Relationship 사용
- DB 독립성
- DTO Projection 가능
- Fetch Join 가능
- Static Query에 적합

사용 상황:

- 단순 Repository Method로 부족한 Query
- 명확한 고정 조건 Query
- Entity 관계 기반 JOIN
- DTO Projection
- Fetch Join 필요
- Count Query 분리 가능

---

### [실무]

Entity 조회 JPQL:

```java
@Query("""
    select f
    from Festival f
    where f.active = true
    order by f.eventStartDate asc
""")
List<Festival> findActiveFestivals();
```

DTO Projection JPQL:

```java
@Query("""
    select new com.example.FestivalSummaryDto(
        f.festivalId,
        f.title,
        f.eventStartDate
    )
    from Festival f
    where f.active = true
""")
List<FestivalSummaryDto> findFestivalSummaries();
```

권장:

- Entity 이름과 Field 이름 기준으로 작성
- 복잡한 정적 Query에 사용
- DTO Projection은 필요한 Column만 조회
- Fetch Join은 N+1 해결 목적에 제한적으로 사용
- Pagination Query는 Count Query와 Fetch Join 영향 검토

주의:

- Table / Column 이름이 아니라 Entity / Field 이름 사용
- 동적 조건이 많으면 QueryDSL 검토
- Fetch Join + Pagination 주의
- 1:N Fetch Join은 중복 Row와 메모리 Pagination 위험
- DB 특화 함수는 Native Query 또는 Function 등록 검토

---

### [FAQ]

Q. JPQL은 SQL이랑 뭐가 달라?
A. SQL은 Table과 Column 기준이고 JPQL은 Entity와 Field 기준으로 작성한다.

Q. JPQL은 언제 사용해?
A. Derived Query Method로 표현하기 어렵지만 조건이 고정적인 Query에 사용한다.

Q. JPQL에서도 DTO Projection이 가능해?
A. 가능하다. 필요한 Field만 DTO 생성자로 조회할 수 있다.

Q. JPQL Fetch Join은 언제 써?
A. 연관 Entity를 함께 조회해 N+1 문제를 줄이고 싶을 때 사용한다.

---

## 1.4 QueryDSL Rules

### [개념]

QueryDSL은 Type-safe 방식으로 동적 Query를 작성하기 위한 Query Builder다.

복합 검색 조건, 선택적 필터, 동적 정렬, DTO Projection, 복잡한 조건 조합에 적합하다.

---

### [핵심]

QueryDSL 특징:

- Type-safe Query
- Dynamic Condition
- BooleanExpression
- BooleanBuilder
- DTO Projection
- Join Control
- Pagination
- Compile-time Safety

사용 상황:

- 검색 조건이 optional
- AND / OR 조건 조합
- 기간 검색
- 상태 필터
- 키워드 검색
- 복합 정렬
- 관리자 검색
- 목록 API
- DTO Projection

---

### [실무]

동적 조건 Flow:

```text
Search Request
→ null / empty 조건 제외
→ BooleanExpression 생성
→ where 조건 조합
→ orderBy 적용
→ offset / limit 또는 cursor 적용
→ fetch
```

QueryDSL 조건 예시:

```java
private BooleanExpression regionEq(String regionCode) {
    return hasText(regionCode) ? festival.regionCode.eq(regionCode) : null;
}

private BooleanExpression titleContains(String keyword) {
    return hasText(keyword) ? festival.title.contains(keyword) : null;
}
```

QueryDSL 목록 조회 예시:

```java
return queryFactory
    .select(Projections.constructor(
        FestivalSummaryDto.class,
        festival.festivalId,
        festival.title,
        festival.eventStartDate
    ))
    .from(festival)
    .where(
        regionEq(condition.getRegionCode()),
        titleContains(condition.getKeyword()),
        activeEq(true)
    )
    .orderBy(festival.eventStartDate.asc(), festival.festivalId.asc())
    .offset(pageable.getOffset())
    .limit(pageable.getPageSize())
    .fetch();
```

권장:

- Optional 조건은 null 반환 BooleanExpression 활용
- 검색 조건 Method 분리
- DTO Projection으로 필요한 Column만 조회
- Pagination에는 Stable Sort 적용
- Query 결과와 Count Query 분리 검토
- QueryDSL 생성 SQL 로그 확인

주의:

- 동적 Query가 복잡해지면 조건 Method Naming 통일
- contains는 LIKE '%keyword%'로 변환될 수 있어 성능 검토
- 1:N Join 후 Pagination 주의
- Fetch Join 남용 금지
- Count Query 비용 검토

---

### [FAQ]

Q. QueryDSL은 언제 사용해?
A. 검색 조건이 동적으로 조합되는 목록 조회나 복합 검색 API에 적합하다.

Q. BooleanExpression은 왜 분리해?
A. 조건 재사용, 테스트, 가독성, null 조건 제외를 위해 분리한다.

Q. QueryDSL을 쓰면 SQL을 몰라도 돼?
A. 아니다. QueryDSL도 SQL로 변환되므로 JOIN, Index, Pagination, Aggregation 이해가 필요하다.

Q. QueryDSL contains는 성능 문제가 없나?
A. contains는 LIKE '%keyword%' 형태가 될 수 있어 대량 데이터에서는 Full Text Search나 검색 엔진을 검토해야 한다.

---

## 1.5 Native Query Rules

### [개념]

Native Query는 DBMS SQL 문법을 직접 사용하는 Query다.

JPA 추상화로 표현하기 어렵거나 DB 특화 기능, 성능 최적화, 복잡한 집계가 필요한 경우 사용한다.

---

### [핵심]

Native Query 사용 상황:

- DB 특화 함수
- Full Text Search
- Window Function
- Recursive Query
- Vendor-specific SQL
- Complex Aggregation
- Performance Critical Query
- Bulk Operation
- Legacy Query

주의 대상:

- DB 종속성 증가
- Entity Mapping 오류
- DTO Mapping 복잡
- SQL Injection 위험
- 유지보수 비용 증가
- 테스트 필요성 증가

---

### [실무]

Native Query 예시:

```java
@Query(value = """
    SELECT f.festival_id, f.title
    FROM festivals f
    WHERE MATCH(f.title) AGAINST (:keyword IN NATURAL LANGUAGE MODE)
    ORDER BY f.event_start_date ASC
    LIMIT :limit
""", nativeQuery = true)
List<Object[]> searchByFullText(@Param("keyword") String keyword, @Param("limit") int limit);
```

권장:

- Native Query 사용 이유를 명확히 기록
- Parameter Binding 필수
- SELECT Column 명시
- DTO Mapping 기준 명확화
- DBMS 의존성 문서화
- Execution Plan 확인
- Integration Test 작성

주의:

- 문자열 결합으로 사용자 입력 삽입 금지
- Entity Field 이름이 아니라 실제 Table / Column 이름 사용
- DB 변경 시 Query 깨질 가능성
- Pagination과 Count Query 직접 관리 필요
- Portable Query가 아니므로 이식성 낮음

---

### [FAQ]

Q. Native Query는 언제 써?
A. JPQL이나 QueryDSL로 표현하기 어렵거나 DB 특화 기능이 필요한 경우 사용한다.

Q. Native Query의 가장 큰 단점은?
A. DBMS 종속성과 유지보수 비용이 증가한다는 점이다.

Q. Native Query에서도 Parameter Binding이 필요해?
A. 반드시 필요하다. 사용자 입력을 문자열 결합으로 넣으면 SQL Injection 위험이 있다.

Q. Native Query는 테스트가 더 필요해?
A. 필요하다. Entity Mapping, DTO Mapping, DBMS 문법, 실행 계획을 직접 검증해야 한다.

---

# 2. SQL Troubleshooting Foundation

## 2.1 Wrong Result Troubleshooting

### [개념]

Wrong Result Troubleshooting은 SQL 결과가 기대와 다를 때 조건, JOIN, 집계, NULL, Pagination을 단계적으로 점검하는 과정이다.

SQL 문제는 Query 전체를 한 번에 보지 않고 Base Table부터 조건을 하나씩 추가하며 확인해야 한다.

---

### [핵심]

확인 대상:

- Expected Result
- Base Table
- WHERE Condition
- JOIN Condition
- Row Count
- NULL Handling
- 1:N Duplication
- GROUP BY
- HAVING
- ORDER BY
- Pagination
- Data Type
- Soft Delete Condition

---

### [실무]

Debug Flow:

```text
Expected Result 정의
→ Base Table 단독 조회
→ WHERE 조건 하나씩 추가
→ JOIN 하나씩 추가
→ Row Count 확인
→ GROUP BY 결과 확인
→ HAVING 조건 확인
→ ORDER BY / LIMIT 확인
→ 실제 데이터 샘플 확인
```

예시 문제:

```text
문제: 축제 목록에 삭제된 축제가 보임
확인:
1. festivals.deleted_at 값 확인
2. WHERE deleted_at IS NULL 조건 여부 확인
3. Repository 기본 조건 확인
4. 관리자 조회와 일반 조회 구분 확인
```

예시 문제:

```text
문제: 리뷰 수가 실제보다 많음
확인:
1. reviews 단독 COUNT 확인
2. festivals + reviews JOIN 확인
3. images JOIN 추가 후 Row 수 확인
4. GROUP BY 기준 확인
5. COUNT(DISTINCT) 또는 집계 Subquery 검토
```

---

### [FAQ]

Q. SQL 결과가 이상하면 어디서부터 확인해?
A. Base Table 단독 조회부터 시작해 WHERE, JOIN, GROUP BY를 단계적으로 추가하며 Row 수를 확인한다.

Q. 결과가 너무 많이 나오는 이유는?
A. WHERE 조건 누락, JOIN 조건 오류, 1:N JOIN 중복, Soft Delete 조건 누락 가능성이 있다.

Q. 결과가 누락되는 이유는?
A. INNER JOIN으로 선택 관계 Row가 제외되었거나 WHERE 조건이 과도하게 적용되었을 수 있다.

Q. 삭제된 데이터가 조회되면 무엇을 확인해?
A. Soft Delete 기준인 deleted_at IS NULL 또는 active = true 조건이 포함되었는지 확인한다.

---

## 2.2 Slow Query Troubleshooting

### [개념]

Slow Query Troubleshooting은 SQL 실행 시간이 느릴 때 원인을 분석하고 개선 방향을 찾는 과정이다.

Slow Query는 SQL Query 자체, Index, JOIN, Pagination, Lock, ORM N+1에서 발생할 수 있다.

---

### [핵심]

확인 대상:

- Query Frequency
- Data Size
- Execution Plan
- Full Table Scan
- Missing Index
- Non-Sargable Condition
- Leading Wildcard LIKE
- Inefficient JOIN
- 1:N Join Explosion
- Large OFFSET
- Large Sort
- Large GROUP BY
- N+1 Query
- Lock Wait

---

### [실무]

Debug Flow:

```text
Slow Query 식별
→ 실행 빈도 확인
→ Query Purpose 확인
→ WHERE / JOIN Column 확인
→ Index 존재 확인
→ EXPLAIN 확인
→ SELECT Column 축소
→ JOIN 구조 검토
→ Pagination 방식 검토
→ ORM N+1 확인
→ 개선 후 재측정
```

예시:

```text
문제: 알림 목록 조회가 느림
원인 후보:
- user_id Index 없음
- created_at 정렬 Index 없음
- OFFSET 증가
- 읽음 상태 조건과 정렬 Index 불일치

개선:
- notifications(user_id, created_at DESC)
- notifications(user_id, read_status, created_at DESC)
- Cursor Pagination 검토
```

예시:

```text
문제: 검색 Query가 느림
원인 후보:
- title LIKE '%keyword%'
- 대량 데이터
- Full Table Scan

개선:
- Full Text Search
- 검색 엔진
- 검색 조건 제한
- 검색 전용 Column / Index 검토
```

---

### [FAQ]

Q. 쿼리가 느리면 가장 먼저 뭘 확인해?
A. 실제 병목 Query와 실행 빈도를 확인한 뒤 Execution Plan으로 Scan 방식과 Index 사용 여부를 본다.

Q. Slow Query는 무조건 SQL 문제야?
A. 아니다. ORM N+1, Lock 대기, 네트워크, 데이터 양, Pagination 방식도 원인이 될 수 있다.

Q. Index를 추가하면 항상 해결돼?
A. 아니다. Query 조건, 데이터 분포, 정렬, JOIN 구조를 확인한 뒤 필요한 Index만 추가해야 한다.

Q. 개선 후 무엇을 해야 해?
A. 실행 시간, Execution Plan, 결과 정확성을 다시 확인해야 한다.

---

## 2.3 N+1 Query Troubleshooting

### [개념]

N+1 Query는 한 번의 목록 조회 후 각 Row의 연관 데이터를 조회하기 위해 추가 Query가 반복 실행되는 문제다.

ORM 환경에서 자주 발생하며 SQL 실행 횟수 증가로 성능 저하를 만든다.

---

### [핵심]

N+1 발생 상황:

- Lazy Loading 반복 접근
- 목록 조회 후 연관 Entity 접근
- 반복문 내부 Repository 호출
- DTO 변환 중 연관 객체 접근
- View Rendering 중 Lazy Loading

증상:

- Query 수 급증
- 목록 개수만큼 추가 SELECT
- 응답 시간 증가
- DB 부하 증가
- 로그에 반복 Query 출력

해결 후보:

- Fetch Join
- EntityGraph
- Batch Size
- DTO Projection
- QueryDSL Projection
- 별도 Query 분리

---

### [실무]

문제 예시:

```java
List<Review> reviews = reviewRepository.findByFestivalId(festivalId);

for (Review review : reviews) {
    String nickname = review.getUser().getNickname();
}
```

문제:

```text
reviews 20개 조회
→ review.getUser() 접근 시 user 조회 20번 추가 가능
→ 1 + 20 Query
```

해결 예시 JPQL Fetch Join:

```java
@Query("""
    select r
    from Review r
    join fetch r.user
    where r.festival.festivalId = :festivalId
""")
List<Review> findReviewsWithUser(@Param("festivalId") Long festivalId);
```

DTO Projection 예시:

```java
@Query("""
    select new com.example.ReviewSummaryDto(
        r.reviewId,
        r.content,
        u.nickname
    )
    from Review r
    join r.user u
    where r.festival.festivalId = :festivalId
""")
List<ReviewSummaryDto> findReviewSummaries(@Param("festivalId") Long festivalId);
```

주의:

- 1:N Fetch Join + Pagination 주의
- Fetch Join 남용 시 데이터 폭증 가능
- 목록 API는 DTO Projection이 더 적합한 경우 많음
- Query 로그로 실제 SQL 횟수 확인
- Batch Size는 상황별 보완책

---

### [FAQ]

Q. N+1 Query는 뭐야?
A. 목록 1번 조회 후 각 Row의 연관 데이터를 조회하기 위해 N번의 추가 Query가 발생하는 문제다.

Q. N+1은 어떻게 찾을 수 있어?
A. SQL 로그에서 동일한 SELECT가 목록 Row 수만큼 반복되는지 확인한다.

Q. N+1은 어떻게 해결해?
A. Fetch Join, EntityGraph, DTO Projection, Batch Size, QueryDSL Projection 등을 검토한다.

Q. Fetch Join을 항상 쓰면 돼?
A. 아니다. 1:N Fetch Join과 Pagination 조합은 중복 Row와 메모리 Pagination 문제가 발생할 수 있다.

---

## 2.4 Pagination Troubleshooting

### [개념]

Pagination Troubleshooting은 목록 조회에서 중복, 누락, 순서 흔들림, 성능 저하를 점검하는 과정이다.

Pagination 문제는 ORDER BY, Stable Sort, 1:N JOIN, OFFSET 크기, Cursor 조건 오류에서 발생한다.

---

### [핵심]

문제 유형:

- ORDER BY 없음
- Stable Sort 미보장
- PK Tie-breaker 없음
- 큰 OFFSET
- 1:N JOIN 후 Pagination
- Fetch Join + Pagination
- Cursor 조건 오류
- totalCount 비용 과다
- 데이터 변경 중 페이지 이동

---

### [실무]

문제 예시:

```sql
SELECT post_id, title, created_at
FROM posts
ORDER BY created_at DESC
LIMIT 20 OFFSET 20;
```

문제 가능성:

```text
created_at 값 중복 가능
→ 같은 created_at Row 간 순서 불안정
→ 페이지 중복 / 누락 가능
```

개선:

```sql
SELECT post_id, title, created_at
FROM posts
ORDER BY created_at DESC, post_id DESC
LIMIT 20 OFFSET 20;
```

Cursor 조건 오류 예시:

```sql
-- created_at만 cursor로 사용하면 같은 시간 데이터 누락 가능
WHERE created_at < :lastCreatedAt
ORDER BY created_at DESC, post_id DESC
```

개선:

```sql
WHERE created_at < :lastCreatedAt
   OR (created_at = :lastCreatedAt AND post_id < :lastPostId)
ORDER BY created_at DESC, post_id DESC
```

---

### [FAQ]

Q. 페이지 이동 시 데이터가 중복되는 이유는?
A. ORDER BY가 없거나 정렬 기준이 중복되어 Stable Sort가 보장되지 않았을 가능성이 있다.

Q. Pagination에 PK를 추가 정렬하는 이유는?
A. created_at 같은 값이 중복될 때 결과 순서를 안정적으로 만들기 위해서다.

Q. Cursor Pagination에서 데이터가 누락되는 이유는?
A. Cursor 조건이 정렬 조건과 정확히 일치하지 않거나 Tie-breaker가 없기 때문이다.

Q. Pagination 성능이 느리면 무엇을 확인해?
A. OFFSET 크기, ORDER BY Index, WHERE 조건 Index, Count Query 비용을 확인한다.

---

# 3. SQL Anti Pattern

## 3.1 SELECT Anti Pattern

### [개념]

SELECT Anti Pattern은 조회 Query에서 성능 저하, 보안 위험, 결과 오류를 만드는 잘못된 작성 방식이다.

조회 Query는 필요한 Column, 조건, 정렬, Pagination, JOIN 범위를 명확히 해야 한다.

---

### [핵심]

SELECT Anti Pattern:

- SELECT \* 남용
- 불필요한 Column 조회
- 민감 정보 조회
- WHERE 조건 누락
- ORDER BY 없는 목록
- ORDER BY 없는 Pagination
- 큰 OFFSET 방치
- 불필요한 JOIN
- 1:N JOIN 후 중복 미검토
- LIKE '%keyword%' 성능 무시
- Non-Sargable Condition
- NULL 비교 오류

---

### [실무]

Anti Pattern:

```sql
SELECT *
FROM users;
```

문제:

```text
불필요한 Column 조회
민감 정보 노출 가능
응답 데이터 증가
DTO 목적 불명확
```

개선:

```sql
SELECT user_id, email, nickname
FROM users
WHERE active = true
ORDER BY created_at DESC;
```

Anti Pattern:

```sql
SELECT festival_id, title
FROM festivals
LIMIT 20 OFFSET 20;
```

개선:

```sql
SELECT festival_id, title, created_at
FROM festivals
ORDER BY created_at DESC, festival_id DESC
LIMIT 20 OFFSET 20;
```

---

### [FAQ]

Q. SELECT \*는 왜 Anti Pattern이야?
A. 불필요한 Column 조회, 민감 정보 노출, 네트워크 비용 증가, DTO 의도 불명확 문제가 생길 수 있다.

Q. ORDER BY 없는 목록 조회는 왜 문제야?
A. 결과 순서가 보장되지 않아 Pagination에서 중복이나 누락이 발생할 수 있다.

Q. 민감 정보 조회는 왜 Query 단계에서 막아야 해?
A. Service나 Response 단계에서 제거하기보다 처음부터 조회하지 않는 것이 안전하다.

Q. Non-Sargable 조건은 왜 Anti Pattern이야?
A. Index를 효율적으로 사용하지 못해 대량 데이터에서 성능 문제가 발생할 수 있기 때문이다.

---

## 3.2 JOIN Anti Pattern

### [개념]

JOIN Anti Pattern은 Table Relationship을 잘못 연결하거나 불필요한 JOIN을 사용해 결과 오류와 성능 저하를 만드는 패턴이다.

JOIN은 반드시 Query Purpose, PK / FK Relationship, Row 증가 가능성을 기준으로 검토해야 한다.

---

### [핵심]

JOIN Anti Pattern:

- JOIN 조건 누락
- 잘못된 Column JOIN
- 불필요한 JOIN
- 1:N JOIN 중복 미검토
- LEFT JOIN 후 WHERE 조건 실수
- 여러 1:N Table 동시 JOIN
- DISTINCT로 원인 숨기기
- Pagination 대상에 1:N JOIN 적용
- Fetch Join 남용
- Implicit Join 남용

---

### [실무]

JOIN 조건 누락:

```sql
SELECT u.user_id, p.post_id
FROM users u
JOIN posts p;
```

문제:

```text
Cartesian Product 발생
Row 수 폭증
잘못된 결과
성능 저하
```

LEFT JOIN Anti Pattern:

```sql
SELECT f.festival_id, f.title
FROM festivals f
LEFT JOIN reviews r ON f.festival_id = r.festival_id
WHERE r.rating >= 4;
```

문제:

```text
오른쪽 Table 조건이 WHERE에 있음
NULL Row 제거
LEFT JOIN이 INNER JOIN처럼 동작
```

개선:

```sql
SELECT f.festival_id, f.title
FROM festivals f
LEFT JOIN reviews r
  ON f.festival_id = r.festival_id
 AND r.rating >= 4;
```

---

### [FAQ]

Q. JOIN에서 가장 치명적인 Anti Pattern은?
A. JOIN 조건 누락이다. Cartesian Product가 발생해 Row 수가 폭증한다.

Q. LEFT JOIN이 INNER JOIN처럼 동작하는 이유는?
A. WHERE 절에서 오른쪽 Table 조건을 걸면 NULL Row가 제거되기 때문이다.

Q. DISTINCT로 JOIN 중복을 제거하면 괜찮아?
A. 원인을 숨길 수 있으므로 JOIN 구조와 Query Purpose를 먼저 검토해야 한다.

Q. 1:N JOIN 후 Pagination은 왜 위험해?
A. 부모 Row가 자식 Row 수만큼 중복되어 페이지 결과가 왜곡될 수 있기 때문이다.

---

## 3.3 Aggregation Anti Pattern

### [개념]

Aggregation Anti Pattern은 GROUP BY, COUNT, SUM, AVG 사용 시 집계 결과를 왜곡하거나 성능 문제를 만드는 패턴이다.

집계 Query는 GROUP BY 기준, JOIN Row 수, NULL 처리, HAVING 조건을 명확히 해야 한다.

---

### [핵심]

Aggregation Anti Pattern:

- GROUP BY 기준 불명확
- SELECT 일반 Column과 GROUP BY 불일치
- COUNT(\*)와 COUNT(column) 혼동
- 여러 1:N JOIN 후 COUNT 왜곡
- SUM 중복 계산
- AVG 왜곡
- HAVING을 WHERE처럼 사용
- DISTINCT 남용
- 집계 결과 NULL 미처리
- 대량 GROUP BY 성능 미검토

---

### [실무]

잘못된 GROUP BY:

```sql
SELECT festival_id, content, COUNT(*) AS review_count
FROM reviews
GROUP BY festival_id;
```

문제:

```text
content는 GROUP BY 기준도 아니고 집계 함수도 아님
DBMS 설정에 따라 오류 또는 예측 어려운 값 반환
```

JOIN 집계 왜곡:

```sql
SELECT f.festival_id,
       COUNT(r.review_id) AS review_count,
       COUNT(i.image_id) AS image_count
FROM festivals f
LEFT JOIN reviews r ON f.festival_id = r.festival_id
LEFT JOIN festival_images i ON f.festival_id = i.festival_id
GROUP BY f.festival_id;
```

개선:

```sql
SELECT f.festival_id,
       COALESCE(rc.review_count, 0) AS review_count,
       COALESCE(ic.image_count, 0) AS image_count
FROM festivals f
LEFT JOIN (
  SELECT festival_id, COUNT(*) AS review_count
  FROM reviews
  GROUP BY festival_id
) rc ON f.festival_id = rc.festival_id
LEFT JOIN (
  SELECT festival_id, COUNT(*) AS image_count
  FROM festival_images
  GROUP BY festival_id
) ic ON f.festival_id = ic.festival_id;
```

---

### [FAQ]

Q. Aggregation에서 가장 흔한 Anti Pattern은?
A. GROUP BY 기준 오류와 여러 1:N JOIN으로 인한 COUNT 왜곡이다.

Q. COUNT(\*)와 COUNT(column)을 혼동하면 어떤 문제가 생겨?
A. NULL 처리 차이 때문에 예상과 다른 개수가 나올 수 있다.

Q. HAVING을 WHERE처럼 쓰면 왜 문제야?
A. 집계 전에 줄일 수 있는 Row를 늦게 필터링해 불필요한 GROUP BY 비용이 발생할 수 있다.

Q. 집계 결과가 NULL이면 어떻게 해?
A. COALESCE를 사용해 0 같은 기본값 처리 기준을 명확히 할 수 있다.

---

## 3.4 Modification Anti Pattern

### [개념]

Modification Anti Pattern은 INSERT, UPDATE, DELETE에서 데이터 손상, 중복, 정합성 붕괴를 만드는 잘못된 패턴이다.

변경 Query는 조회 Query보다 더 엄격하게 WHERE, Constraint, Transaction, Rollback을 검토해야 한다.

---

### [핵심]

Modification Anti Pattern:

- INSERT Column 목록 생략
- Required Column 누락
- Unique Constraint 없이 중복 방지
- Application 중복 체크만 의존
- FK 대상 미확인
- UPDATE WHERE 누락
- DELETE WHERE 누락
- User Scope 조건 누락
- Status 조건 누락
- Soft Delete 기준 혼용
- Cascade Delete 영향 미확인
- Transaction 누락
- Affected Row 미확인
- 외부 API 호출과 Transaction 경계 오류

---

### [실무]

위험한 UPDATE:

```sql
UPDATE users
SET role = 'ROLE_ADMIN';
```

개선:

```sql
UPDATE users
SET role = 'ROLE_ADMIN',
    updated_at = NOW()
WHERE user_id = 1;
```

위험한 DELETE:

```sql
DELETE FROM reviews;
```

개선:

```sql
UPDATE reviews
SET deleted_at = NOW(),
    updated_at = NOW()
WHERE review_id = 100
  AND user_id = 1;
```

중복 방지 Anti Pattern:

```text
Application에서 existsByUserIdAndFestivalId 확인
→ 동시에 두 요청이 통과
→ favorites 중복 INSERT 발생 가능
```

개선:

```sql
ALTER TABLE favorites
ADD CONSTRAINT uk_favorites_user_festival UNIQUE (user_id, festival_id);
```

---

### [FAQ]

Q. Modification에서 가장 치명적인 Anti Pattern은?
A. UPDATE / DELETE WHERE 조건 누락이다.

Q. Application 중복 체크만으로 충분하지 않은 이유는?
A. 동시 요청이 동시에 중복 체크를 통과할 수 있기 때문이다.

Q. User Scope 조건은 왜 필요해?
A. 사용자가 자신의 데이터만 수정하거나 삭제하도록 제한하기 위해 필요하다.

Q. Soft Delete 기준을 혼용하면 어떤 문제가 생겨?
A. Query마다 삭제 데이터 포함 여부가 달라져 결과 일관성이 깨질 수 있다.

---

# 4. SQL Review Workflow

## 4.1 SQL Generation Review

### [개념]

SQL Generation Review는 AI Agent가 SQL을 생성한 뒤 Query Purpose, 결과 정확성, 성능, 정합성을 검토하는 과정이다.

RAG 문서의 목표는 SQL 생성뿐 아니라 생성된 SQL의 위험 요소를 탐지하는 것이다.

---

### [핵심]

Review 단계:

1. Query Purpose Review
2. Table Relationship Review
3. SELECT Column Review
4. Filtering Review
5. JOIN Review
6. Aggregation Review
7. Pagination Review
8. Index Review
9. Transaction Review
10. Constraint Review
11. Backend Mapping Review
12. Anti Pattern Review

---

### [실무]

SQL Review Flow:

```text
Generated SQL
→ Query Purpose 확인
→ Base Table 확인
→ SELECT Column 확인
→ WHERE 조건 확인
→ JOIN 조건 확인
→ GROUP BY / HAVING 확인
→ ORDER BY / Pagination 확인
→ Index 후보 확인
→ Transaction 필요 여부 확인
→ Constraint 영향 확인
→ Repository 구현 방식 확인
→ Anti Pattern 확인
→ Final SQL
```

예시 Review:

```text
Query: 사용자 찜한 축제 목록

확인:
- Query Purpose: 목록 조회
- Base Table: favorites 또는 festivals
- Relationship: favorites.festival_id = festivals.festival_id
- Filter: favorites.user_id
- Sort: festival.event_start_date
- Pagination: ORDER BY + LIMIT
- Index: favorites(user_id), favorites(festival_id)
- Anti Pattern: 불필요한 JOIN 없음
```

---

### [FAQ]

Q. SQL Review는 왜 필요해?
A. 생성된 SQL이 문법적으로 맞아도 결과 오류, 성능 문제, 데이터 정합성 문제가 있을 수 있기 때문이다.

Q. SQL Review는 어디서 시작해?
A. Query Purpose와 Base Table 확인에서 시작한다.

Q. Review에서 가장 먼저 제거해야 하는 것은?
A. Query Purpose와 무관한 불필요한 JOIN, SELECT \*, 잘못된 WHERE 조건이다.

Q. SQL 생성 후 반드시 봐야 하는 것은?
A. 결과 정확성, JOIN 안전성, Pagination 안정성, Index 가능성, 변경 Query 안전성이다.

---

## 4.2 Backend Mapping Review

### [개념]

Backend Mapping Review는 SQL Query 결과가 DTO, Entity, Repository Method, API Response와 올바르게 연결되는지 검토하는 과정이다.

SQL 결과 Column과 Backend 반환 타입이 맞지 않으면 Mapping 오류, N+1, 불필요한 데이터 조회가 발생할 수 있다.

---

### [핵심]

검토 대상:

- Entity Mapping
- DTO Projection
- Column Alias
- Field Name
- Nullable Field
- Enum Mapping
- Date / Time Mapping
- Pagination Response
- Slice / Page
- Count Query
- Repository Return Type

---

### [실무]

DTO Projection 검수:

```text
SQL Column:
festival_id, title, event_start_date

DTO Field:
festivalId, title, eventStartDate

검토:
- Alias 일치 여부
- 타입 일치 여부
- Nullable 여부
- 날짜 타입 변환 여부
```

Projection Query 예시:

```java
@Query("""
    select new com.example.FestivalSummaryDto(
        f.festivalId,
        f.title,
        f.eventStartDate
    )
    from Festival f
    where f.active = true
""")
List<FestivalSummaryDto> findFestivalSummaries();
```

권장:

- 목록 API는 DTO Projection 우선 검토
- Entity 전체 조회 후 Response 변환 남용 금지
- Column Alias와 DTO Field 이름 일치
- Nullable Field 처리 기준 명확화
- Page / Slice 응답 정책 구분
- Count Query 비용 검토

---

### [FAQ]

Q. Backend Mapping Review는 왜 필요해?
A. SQL 결과와 DTO / Entity 반환 타입이 맞아야 Mapping 오류와 불필요한 조회를 막을 수 있기 때문이다.

Q. 목록 API는 Entity를 그대로 반환해도 돼?
A. 권장하지 않는다. 필요한 데이터만 DTO Projection으로 조회하는 것이 좋다.

Q. Column Alias는 왜 중요해?
A. DTO Mapping과 API Response Field 이름을 명확히 맞추기 위해 중요하다.

Q. Page와 Slice는 어떻게 골라?
A. totalCount가 필요하면 Page, 더보기나 무한 스크롤처럼 hasNext만 필요하면 Slice가 적합하다.

---

## 4.3 File-to-File Link Review

### [개념]

File-to-File Link Review는 SQL 문서가 다른 Domain Rules 문서와 역할을 명확히 나누고 필요한 연결 지점을 유지하는 검토 과정이다.

SQL Part05는 SQL Foundation을 마무리하며 JPA Advanced, QueryDSL Practical, API Design, Performance Tuning 문서와 연결된다.

---

### [핵심]

연결 대상:

- MASTER_RAG_RULES
- PROJECT_PROGRESS
- SQL Domain Rules
- JPA Advanced Domain Rules
- QueryDSL Practical Domain Rules
- API Design Domain Rules
- Testing Domain Rules
- Performance Tuning Domain Rules
- Security Advanced Domain Rules

연결 기준:

- SQL → Query Purpose / Table Relationship / Index / Transaction
- JPA → Entity Mapping / Fetch Strategy / Transaction
- QueryDSL → Dynamic Query / DTO Projection / Pagination
- API Design → Request / Response / Pagination Contract
- Testing → Repository Test / Query Test / Integration Test
- Performance → Execution Plan / Slow Query / Index Tuning
- Security → Permission Filter / User Scope / Data Access Control

---

### [실무]

연계 Flow:

```text
Backend Requirement
→ API Design에서 Request / Response 정의
→ SQL에서 Query Purpose와 Data Access 기준 정의
→ JPA에서 Entity Relationship 구현
→ QueryDSL에서 Dynamic Query 구현
→ Testing에서 Repository / Integration Test 검증
→ Performance에서 Slow Query와 Index 튜닝
→ Security에서 User Scope와 Permission 조건 검증
```

문서 역할 분리:

```text
SQL 문서:
Query Purpose, SQL 작성 기준, 성능 기초, Anti Pattern

JPA 문서:
Entity Mapping, Persistence Context, Fetch Strategy, Transaction 적용

QueryDSL 문서:
동적 조건, BooleanExpression, Projection, Pagination 구현

API Design 문서:
Request DTO, Response DTO, Error Response, Pagination 응답 계약
```

---

### [FAQ]

Q. SQL 문서는 어떤 문서와 가장 많이 연결돼?
A. JPA Advanced, QueryDSL Practical, API Design, Performance Tuning 문서와 많이 연결된다.

Q. SQL과 QueryDSL 문서는 어떻게 역할을 나눠?
A. SQL은 Query 사고와 성능 기준을 다루고 QueryDSL은 동적 Query 구현 패턴을 다룬다.

Q. SQL과 JPA 문서는 어떻게 연결돼?
A. SQL은 실제 Query 결과와 성능을 다루고 JPA는 Entity Mapping, Fetch Strategy, Transaction을 다룬다.

Q. SQL 문서가 Security와도 연결돼?
A. 연결된다. User Scope, 권한 기반 조회, 데이터 접근 제한 조건은 Security와 SQL이 함께 검토해야 한다.

---

# 5. Final SQL Checklist

## 5.1 Final Review Checklist

### [개념]

Final Review Checklist는 SQL Foundation 전체 문서를 기준으로 Query 생성과 검수를 마무리하는 최종 점검 기준이다.

Agent는 SQL Query를 생성한 뒤 Checklist 기준으로 치명적 문제를 확인해야 한다.

---

### [핵심]

Final Checklist:

```md
- [ ] Query Purpose가 명확한가?
- [ ] Base Table이 요구사항과 일치하는가?
- [ ] 필요한 Column만 SELECT하는가?
- [ ] 민감 정보 Column을 제외했는가?
- [ ] WHERE 조건이 정확한가?
- [ ] NULL 비교를 IS NULL / IS NOT NULL로 처리했는가?
- [ ] AND / OR 조건 우선순위를 괄호로 명확히 했는가?
- [ ] 날짜 조건이 Sargable Range 조건인가?
- [ ] JOIN이 실제로 필요한가?
- [ ] JOIN 조건이 PK / FK와 일치하는가?
- [ ] INNER JOIN / LEFT JOIN 선택이 Query Purpose와 일치하는가?
- [ ] LEFT JOIN 후 WHERE 조건으로 기준 Row가 제거되지 않는가?
- [ ] 1:N JOIN으로 Row 중복이 발생하지 않는가?
- [ ] GROUP BY 기준이 명확한가?
- [ ] SELECT 일반 Column과 GROUP BY가 충돌하지 않는가?
- [ ] COUNT(\*)와 COUNT(column)을 구분했는가?
- [ ] JOIN 후 Aggregation 결과가 왜곡되지 않는가?
- [ ] Subquery 결과가 단건 / 목록 / 존재 여부 중 무엇인지 명확한가?
- [ ] EXISTS / IN 선택이 Query Purpose와 일치하는가?
- [ ] NOT IN 사용 시 NULL 가능성을 검토했는가?
- [ ] UPDATE / DELETE에 WHERE 조건이 있는가?
- [ ] User Scope 조건이 필요한 Query에 포함되었는가?
- [ ] Status 조건이 필요한 변경 Query에 포함되었는가?
- [ ] Soft Delete 기준이 통일되었는가?
- [ ] Unique Constraint로 중복 방지를 보장하는가?
- [ ] Foreign Key 영향이 검토되었는가?
- [ ] Transaction이 필요한 작업인가?
- [ ] Lock / Isolation 검토가 필요한 동시성 작업인가?
- [ ] Pagination에 ORDER BY가 있는가?
- [ ] Pagination 정렬이 Stable Sort인가?
- [ ] OFFSET이 커질 가능성을 검토했는가?
- [ ] Cursor Pagination이 더 적합한지 검토했는가?
- [ ] WHERE / JOIN / ORDER BY Column이 Index 후보인지 검토했는가?
- [ ] 조건이 Sargable한가?
- [ ] Slow Query는 Execution Plan으로 확인했는가?
- [ ] Repository 구현 방식이 Query 복잡도와 일치하는가?
- [ ] DTO Projection과 Column Alias가 일치하는가?
- [ ] N+1 Query 가능성을 검토했는가?
- [ ] SQL Anti Pattern이 없는가?
```

---

### [실무]

Final Review Flow:

```text
Generated SQL
→ Correctness Review
→ Safety Review
→ Performance Review
→ Backend Mapping Review
→ Anti Pattern Review
→ File-to-File Link Review
→ Final Output
```

치명적 문제 기준:

```text
Critical:
- UPDATE / DELETE WHERE 누락
- JOIN 조건 누락
- 잘못된 권한 Scope
- 중복 방지 Constraint 누락
- Transaction 누락
- 민감 정보 조회
- SQL Injection 위험
- Pagination 순서 불안정

Major:
- SELECT * 사용
- 불필요한 JOIN
- Non-Sargable 조건
- 큰 OFFSET 방치
- N+1 가능성
- Count Query 비용 미검토

Minor:
- Alias Naming 불명확
- DTO Field Naming 불일치
- FAQ / Retrieval Query 누락
```

---

### [FAQ]

Q. SQL 최종 검수에서 Critical 문제는 뭐야?
A. WHERE 없는 변경 Query, JOIN 조건 누락, 권한 Scope 누락, 중복 방지 누락, Transaction 누락, 민감 정보 조회가 Critical이다.

Q. SQL Query가 문법적으로 맞으면 충분해?
A. 아니다. 결과 정확성, 성능, 정합성, 보안 Scope, Backend Mapping까지 검토해야 한다.

Q. Final Checklist는 언제 사용해?
A. SQL Query 생성 후 최종 답변 또는 코드 반영 전에 사용한다.

Q. SQL 문서 전체의 최종 목표는 뭐야?
A. Backend Agent가 SQL Query를 작성하고 결과 정확성, 성능, 정합성, Anti Pattern까지 검토하도록 지원하는 것이다.

---

## 5.2 SQL Domain Completion Summary

### [개념]

SQL Domain Completion Summary는 SQL Foundation 문서 세트가 Agent에게 제공해야 하는 최종 능력을 정리한다.

SQL Part01부터 Part05까지는 Backend Agent, Review Agent, PM Agent가 SQL 기반 데이터 접근을 해석하고 검증하기 위한 Foundation 지식 세트다.

---

### [핵심]

SQL Foundation 구성:

- Part01: SQL Basics / Query Purpose / SELECT
- Part02: Filtering / JOIN / Aggregation
- Part03: Subquery / EXISTS / Data Modification
- Part04: Index / Pagination / Transaction / Constraint
- Part05: Backend Integration / Troubleshooting / Anti Pattern

Agent 수행 가능 작업:

- Query Purpose 파악
- Table Relationship 분석
- SELECT Query 작성
- Filtering 조건 설계
- JOIN 조건 설계
- Aggregation Query 작성
- Subquery / EXISTS 선택
- INSERT / UPDATE / DELETE 안전성 검토
- Index 후보 판단
- Pagination 방식 선택
- Transaction 필요 여부 판단
- Constraint 기반 무결성 판단
- Repository 구현 방식 선택
- Slow Query 원인 분석
- SQL Anti Pattern 탐지

---

### [실무]

SQL Domain 최종 Workflow:

```text
User Backend Data Request
→ Query Purpose 식별
→ Target Table 식별
→ Table Relationship 확인
→ SQL Query 설계
→ Filtering / Join / Aggregation 검토
→ Pagination / Sorting 검토
→ Index / Transaction / Constraint 검토
→ Repository / QueryDSL / Native Query Mapping
→ Troubleshooting / Anti Pattern Review
→ Final SQL or Backend Implementation Guide
```

문서 연계 완료 기준:

```text
MASTER_RAG_RULES 적용
→ Required Section 포함
→ FAQ 강화
→ Retrieval Queries 포함
→ SQL Domain Rules 범위 반영
→ PROJECT_PROGRESS의 SQL Rework 대상 완료 가능 상태
→ JPA / QueryDSL / API Design / Testing / Performance 문서와 연결 가능
```

---

### [FAQ]

Q. SQL Foundation은 총 몇 Part야?
A. SQL Foundation은 Part01부터 Part05까지 5개 Part 구성이 적합하다.

Q. SQL Part05의 역할은 뭐야?
A. SQL을 Backend Repository 구현, Troubleshooting, Anti Pattern 검수와 연결해 SQL Foundation을 마무리하는 역할이다.

Q. SQL 문서 세트 완료 후 다음 연결 대상은?
A. JPA Advanced, QueryDSL Practical, API Design, Testing, Performance Tuning 문서와 연결된다.

Q. SQL Domain 문서가 Agent에게 제공해야 하는 최종 능력은?
A. SQL 작성뿐 아니라 결과 정확성, 성능, Transaction, Constraint, Backend Mapping, Anti Pattern 검토 능력이다.

---

# Retrieval Queries

### [FAQ]

Q. SQL Part05는 무엇을 다뤄?
A. Backend Integration, Repository 구현 방식, JPQL, QueryDSL, Native Query, Troubleshooting, N+1, Anti Pattern, Final Checklist를 다룬다.

Q. SQL과 Repository는 왜 연결해서 봐야 해?
A. Repository Method, JPQL, QueryDSL, Native Query가 결국 DB에서 SQL로 실행되기 때문이다.

Q. Backend Query 구현 방식은 뭐가 있어?
A. Spring Data JPA Repository Method, Derived Query Method, JPQL, QueryDSL, Native Query, DTO Projection이 있다.

Q. 단순 조회는 무엇으로 구현해?
A. findById, findByEmail, existsByEmail 같은 Spring Data JPA Repository Method로 충분한 경우가 많다.

Q. 복잡한 검색 조건은 무엇이 적합해?
A. 동적 조건 조합이 많은 경우 QueryDSL이 적합하다.

Q. Native Query는 언제 사용해?
A. JPQL이나 QueryDSL로 표현하기 어렵거나 DB 특화 기능이 필요한 경우 사용한다.

Q. Derived Query Method는 언제 써?
A. 단순 조건 조회, 존재 여부 확인, Count, FK 기반 조회처럼 Query가 단순할 때 사용한다.

Q. Method 이름이 길어지면 어떻게 해?
A. JPQL이나 QueryDSL로 분리하는 것이 좋다.

Q. existsBy는 언제 유용해?
A. 이메일 중복 확인, 찜 여부 확인, 권한 Row 존재 확인처럼 존재 여부만 필요할 때 유용하다.

Q. JPQL은 SQL이랑 뭐가 달라?
A. SQL은 Table과 Column 기준이고 JPQL은 Entity와 Field 기준으로 작성한다.

Q. JPQL은 언제 사용해?
A. Derived Query Method로 표현하기 어렵지만 조건이 고정적인 Query에 사용한다.

Q. JPQL에서도 DTO Projection이 가능해?
A. 가능하다. 필요한 Field만 DTO 생성자로 조회할 수 있다.

Q. JPQL Fetch Join은 언제 써?
A. 연관 Entity를 함께 조회해 N+1 문제를 줄이고 싶을 때 사용한다.

Q. QueryDSL은 언제 사용해?
A. 검색 조건이 동적으로 조합되는 목록 조회나 복합 검색 API에 적합하다.

Q. BooleanExpression은 왜 분리해?
A. 조건 재사용, 테스트, 가독성, null 조건 제외를 위해 분리한다.

Q. QueryDSL을 쓰면 SQL을 몰라도 돼?
A. 아니다. QueryDSL도 SQL로 변환되므로 JOIN, Index, Pagination, Aggregation 이해가 필요하다.

Q. QueryDSL contains는 성능 문제가 없나?
A. contains는 LIKE '%keyword%' 형태가 될 수 있어 대량 데이터에서는 Full Text Search나 검색 엔진을 검토해야 한다.

Q. Native Query의 가장 큰 단점은?
A. DBMS 종속성과 유지보수 비용이 증가한다는 점이다.

Q. Native Query에서도 Parameter Binding이 필요해?
A. 반드시 필요하다. 사용자 입력을 문자열 결합으로 넣으면 SQL Injection 위험이 있다.

Q. SQL 결과가 이상하면 어디서부터 확인해?
A. Base Table 단독 조회부터 시작해 WHERE, JOIN, GROUP BY를 단계적으로 추가하며 Row 수를 확인한다.

Q. 결과가 너무 많이 나오는 이유는?
A. WHERE 조건 누락, JOIN 조건 오류, 1:N JOIN 중복, Soft Delete 조건 누락 가능성이 있다.

Q. 결과가 누락되는 이유는?
A. INNER JOIN으로 선택 관계 Row가 제외되었거나 WHERE 조건이 과도하게 적용되었을 수 있다.

Q. 삭제된 데이터가 조회되면 무엇을 확인해?
A. Soft Delete 기준인 deleted_at IS NULL 또는 active = true 조건이 포함되었는지 확인한다.

Q. 쿼리가 느리면 가장 먼저 뭘 확인해?
A. 실제 병목 Query와 실행 빈도를 확인한 뒤 Execution Plan으로 Scan 방식과 Index 사용 여부를 본다.

Q. Slow Query는 무조건 SQL 문제야?
A. 아니다. ORM N+1, Lock 대기, 네트워크, 데이터 양, Pagination 방식도 원인이 될 수 있다.

Q. N+1 Query는 뭐야?
A. 목록 1번 조회 후 각 Row의 연관 데이터를 조회하기 위해 N번의 추가 Query가 발생하는 문제다.

Q. N+1은 어떻게 찾을 수 있어?
A. SQL 로그에서 동일한 SELECT가 목록 Row 수만큼 반복되는지 확인한다.

Q. N+1은 어떻게 해결해?
A. Fetch Join, EntityGraph, DTO Projection, Batch Size, QueryDSL Projection 등을 검토한다.

Q. Fetch Join을 항상 쓰면 돼?
A. 아니다. 1:N Fetch Join과 Pagination 조합은 중복 Row와 메모리 Pagination 문제가 발생할 수 있다.

Q. 페이지 이동 시 데이터가 중복되는 이유는?
A. ORDER BY가 없거나 정렬 기준이 중복되어 Stable Sort가 보장되지 않았을 가능성이 있다.

Q. Cursor Pagination에서 데이터가 누락되는 이유는?
A. Cursor 조건이 정렬 조건과 정확히 일치하지 않거나 Tie-breaker가 없기 때문이다.

Q. SELECT \*는 왜 Anti Pattern이야?
A. 불필요한 Column 조회, 민감 정보 노출, 네트워크 비용 증가, DTO 의도 불명확 문제가 생길 수 있다.

Q. JOIN에서 가장 치명적인 Anti Pattern은?
A. JOIN 조건 누락이다. Cartesian Product가 발생해 Row 수가 폭증한다.

Q. LEFT JOIN이 INNER JOIN처럼 동작하는 이유는?
A. WHERE 절에서 오른쪽 Table 조건을 걸면 NULL Row가 제거되기 때문이다.

Q. Aggregation에서 가장 흔한 Anti Pattern은?
A. GROUP BY 기준 오류와 여러 1:N JOIN으로 인한 COUNT 왜곡이다.

Q. Modification에서 가장 치명적인 Anti Pattern은?
A. UPDATE / DELETE WHERE 조건 누락이다.

Q. Application 중복 체크만으로 충분하지 않은 이유는?
A. 동시 요청이 동시에 중복 체크를 통과할 수 있기 때문이다.

Q. SQL Review는 왜 필요해?
A. 생성된 SQL이 문법적으로 맞아도 결과 오류, 성능 문제, 데이터 정합성 문제가 있을 수 있기 때문이다.

Q. SQL Review는 어디서 시작해?
A. Query Purpose와 Base Table 확인에서 시작한다.

Q. Backend Mapping Review는 왜 필요해?
A. SQL 결과와 DTO / Entity 반환 타입이 맞아야 Mapping 오류와 불필요한 조회를 막을 수 있기 때문이다.

Q. 목록 API는 Entity를 그대로 반환해도 돼?
A. 권장하지 않는다. 필요한 데이터만 DTO Projection으로 조회하는 것이 좋다.

Q. Page와 Slice는 어떻게 골라?
A. totalCount가 필요하면 Page, 더보기나 무한 스크롤처럼 hasNext만 필요하면 Slice가 적합하다.

Q. SQL 문서는 어떤 문서와 가장 많이 연결돼?
A. JPA Advanced, QueryDSL Practical, API Design, Performance Tuning 문서와 많이 연결된다.

Q. SQL과 QueryDSL 문서는 어떻게 역할을 나눠?
A. SQL은 Query 사고와 성능 기준을 다루고 QueryDSL은 동적 Query 구현 패턴을 다룬다.

Q. SQL과 JPA 문서는 어떻게 연결돼?
A. SQL은 실제 Query 결과와 성능을 다루고 JPA는 Entity Mapping, Fetch Strategy, Transaction을 다룬다.

Q. SQL 문서가 Security와도 연결돼?
A. 연결된다. User Scope, 권한 기반 조회, 데이터 접근 제한 조건은 Security와 SQL이 함께 검토해야 한다.

Q. SQL 최종 검수에서 Critical 문제는 뭐야?
A. WHERE 없는 변경 Query, JOIN 조건 누락, 권한 Scope 누락, 중복 방지 누락, Transaction 누락, 민감 정보 조회가 Critical이다.

Q. SQL Query가 문법적으로 맞으면 충분해?
A. 아니다. 결과 정확성, 성능, 정합성, 보안 Scope, Backend Mapping까지 검토해야 한다.

Q. SQL Foundation은 총 몇 Part야?
A. SQL Foundation은 Part01부터 Part05까지 5개 Part 구성이 적합하다.

Q. SQL Part05의 역할은 뭐야?
A. SQL을 Backend Repository 구현, Troubleshooting, Anti Pattern 검수와 연결해 SQL Foundation을 마무리하는 역할이다.

Q. SQL 문서 세트 완료 후 다음 연결 대상은?
A. JPA Advanced, QueryDSL Practical, API Design, Testing, Performance Tuning 문서와 연결된다.

Q. SQL Domain 문서가 Agent에게 제공해야 하는 최종 능력은?
A. SQL 작성뿐 아니라 결과 정확성, 성능, Transaction, Constraint, Backend Mapping, Anti Pattern 검토 능력이다.
