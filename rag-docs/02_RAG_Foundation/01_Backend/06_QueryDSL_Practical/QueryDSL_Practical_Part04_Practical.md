# QueryDSL Practical Part04 Practical

---

# 1. Practical Repository Pattern

## 1.1 실무 Repository 구조

### [개념]

실무 QueryDSL 구조는 역할 기반 Repository 분리가 핵심이다.

기본 CRUD는 `JpaRepository`가 담당하고, 복잡한 조회 Query는 `Custom Repository` 또는 `Query Repository`에서 담당한다.

Service는 비즈니스 로직을 담당하고, QueryDSL Query 작성 책임은 Repository 계층에 둔다.

---

### [핵심]

- JpaRepository = 기본 CRUD
- Custom Repository = QueryDSL 메서드 선언
- RepositoryImpl = QueryDSL 구현
- Query Repository = 복잡한 조회 전용 Repository
- Service 계층 QueryDSL 직접 작성 지양
- Query 책임과 비즈니스 책임 분리

---

### [실무]

기본 구조:

```text
repository/
├ UserRepository
├ UserRepositoryCustom
└ UserRepositoryImpl
```

대규모 프로젝트 권장 구조:

```text
repository/
├ user/
│ ├ UserRepository
│ ├ UserQueryRepository
│ └ UserQueryRepositoryImpl
```

---

### [Flow]

```text
Controller
→ Service
→ Repository Interface
→ Query Repository
→ QueryDSL Implementation
→ DB
→ DTO Response
```

---

### [주의]

- Service에 QueryDSL Query 직접 작성 금지
- RepositoryImpl이 너무 커지면 QueryRepository로 분리
- 조회 목적별 메서드명 명확화
- Entity 반환보다 DTO Projection 우선 고려

---

### [FAQ]

Q. QueryDSL 코드는 어디에 작성하는가?
A. Custom Repository 또는 Query Repository 구현체에 작성한다.

Q. Service에 QueryDSL을 작성해도 되는가?
A. 권장하지 않는다. Query 책임은 Repository 계층에 둔다.

Q. Repository를 분리하는 이유는?
A. Query 책임과 비즈니스 로직을 분리해 유지보수성을 높이기 위해서다.

---

# 2. Join Query

## 2.1 Join 기본

### [개념]

Join은 여러 Entity를 연결하여 하나의 Query에서 함께 조회하는 방식이다.

QueryDSL은 Entity 연관관계 기반 Join과 SQL 스타일 Join을 지원한다.

---

### [핵심]

- Inner Join
- Left Join
- Cross Join
- Relation Mapping 기반 Join
- SQL Join 변환
- 검색 API / 상세 조회 / 집계 Query에서 사용

---

### [예제]

Inner Join:

```java
List<Order> result = queryFactory
    .selectFrom(order)
    .join(order.user, user)
    .fetch();
```

Left Join:

```java
List<Order> result = queryFactory
    .selectFrom(order)
    .leftJoin(order.user, user)
    .fetch();
```

---

### [실무]

Join Query 주요 사용처:

- 상세 조회 API
- 검색 API
- 관리자 목록 API
- 통계 API
- 대시보드 Query

---

### [주의]

- 불필요한 Join은 성능 저하 원인
- Count Query에서는 Join 제거 가능 여부 검토
- Join과 Fetch Join의 역할 구분 필요
- Join은 연관 Entity를 반드시 로딩하지 않는다

---

### [FAQ]

Q. QueryDSL Join은 언제 사용하는가?
A. 여러 Entity 조건을 함께 사용하거나 연관 데이터를 기준으로 조회해야 할 때 사용한다.

Q. QueryDSL Join은 SQL Join으로 변환되는가?
A. 그렇다. QueryDSL Query는 JPQL을 거쳐 SQL Join Query로 실행된다.

Q. 일반 Join과 Fetch Join은 같은가?
A. 아니다. 일반 Join은 Query 조건 연결이고, Fetch Join은 연관 Entity 즉시 로딩까지 수행한다.

---

# 3. Fetch Join

## 3.1 Fetch Join 개념

### [개념]

Fetch Join은 Join과 동시에 연관 Entity를 즉시 로딩하는 JPA 조회 방식이다.

QueryDSL에서는 `.fetchJoin()`을 사용한다.

Fetch Join은 Lazy Loading으로 인해 발생하는 N+1 Problem 해결의 핵심 기법이다.

---

### [핵심]

- N+1 Problem 해결
- Lazy Loading 최적화
- Query Count 감소
- 연관 Entity 즉시 로딩
- JPA 성능 최적화 핵심
- `.fetchJoin()` 사용

---

### [예제]

```java
List<Order> result = queryFactory
    .selectFrom(order)
    .join(order.user, user).fetchJoin()
    .fetch();
```

---

### [Flow]

```text
Without Fetch Join
Order List Query
→ order.getUser()
→ User Query N times
→ N+1 Problem

With Fetch Join
Order + User Join Query
→ User Already Loaded
→ 1 Query
```

---

### [실무]

Fetch Join은 상세 조회 API와 연관 Entity 접근이 확실한 조회에서 사용한다.

예:

- 주문 상세 + 회원 정보
- 게시글 상세 + 작성자 정보
- 리뷰 목록 + 사용자 정보
- 축제 상세 + 이미지 일부

---

### [주의]

매우 중요:

- Collection Fetch Join + Pagination 비권장
- Fetch Join 남발 금지
- 필요한 연관관계에만 Fetch Join 적용
- 목록 API는 DTO Projection 대안 검토

나쁜 예:

```java
queryFactory
    .selectFrom(order)
    .join(order.items, item).fetchJoin()
    .offset(pageable.getOffset())
    .limit(pageable.getPageSize())
    .fetch();
```

문제:

- DB Pagination이 아닌 Memory Pagination 발생 가능
- Row 증가로 중복 Entity 발생
- 성능 저하 가능

---

### [FAQ]

Q. Fetch Join이 중요한 이유는?
A. Lazy Loading으로 인한 N+1 Problem을 해결하기 위해서다.

Q. 일반 Join과 Fetch Join 차이는?
A. 일반 Join은 조건 연결이고, Fetch Join은 연관 Entity를 즉시 로딩한다.

Q. Collection Fetch Join과 Pagination을 함께 써도 되는가?
A. 권장하지 않는다. 메모리 Pagination과 성능 저하 문제가 발생할 수 있다.

---

# 4. N+1 Problem

## 4.1 N+1 Problem 개념

### [개념]

N+1 Problem은 목록 조회 1번 이후 각 Row의 연관 Entity를 조회하기 위해 추가 Query가 N번 발생하는 문제다.

JPA Lazy Loading 환경에서 매우 자주 발생한다.

---

### [핵심]

- 1 Query + N Query
- Lazy Loading 원인
- Query Count 폭증
- 성능 저하
- Fetch Join / EntityGraph / Batch Size로 해결 가능

---

### [예제]

N+1 발생 예:

```java
List<Order> orders = queryFactory
    .selectFrom(order)
    .fetch();

for (Order order : orders) {
    order.getUser().getUsername();
}
```

Fetch Join 해결:

```java
List<Order> orders = queryFactory
    .selectFrom(order)
    .join(order.user, user).fetchJoin()
    .fetch();
```

---

### [실무]

N+1은 SQL 로그와 Query Count로 확인한다.

목록 API에서 연관 Entity 접근이 필요하면 다음 중 하나를 검토한다.

```text
Fetch Join
→ DTO Projection
→ Batch Size
→ EntityGraph
```

---

### [주의]

- Fetch Join이 항상 정답은 아님
- 목록 API에서는 DTO Projection이 더 적합할 수 있음
- Collection Fetch Join은 Row 수 증가 주의
- Pagination과 함께 사용 시 주의

---

### [FAQ]

Q. N+1 Problem이란?
A. 최초 목록 Query 1번 이후 연관 Entity 조회 Query가 N번 추가 발생하는 문제다.

Q. N+1은 어떻게 해결하는가?
A. Fetch Join, DTO Projection, Batch Size, EntityGraph를 상황에 맞게 사용한다.

Q. N+1 확인 방법은?
A. SQL 로그와 Query Count를 확인한다.

---

# 5. Distinct

## 5.1 distinct 사용

### [개념]

`distinct`는 중복 결과를 제거하기 위한 QueryDSL 메서드이다.

JPA Fetch Join에서 Collection Join으로 인해 같은 Root Entity가 중복 조회될 때 사용할 수 있다.

---

### [핵심]

- 중복 Root Entity 제거
- Collection Join 중복 대응
- Fetch Join 결과 정리
- SQL distinct + JPA Entity 중복 제거

---

### [예제]

```java
List<Order> result = queryFactory
    .selectFrom(order)
    .distinct()
    .join(order.items, item).fetchJoin()
    .fetch();
```

---

### [실무]

Collection Fetch Join 시 Root Entity 중복이 발생할 수 있다.

`distinct()`는 중복 결과를 줄이는 데 사용할 수 있지만, Pagination 문제를 해결하지는 않는다.

---

### [주의]

- distinct는 Pagination 문제 해결책이 아님
- Collection Fetch Join + Pagination은 여전히 비권장
- SQL distinct와 JPA Entity 중복 제거 차이 이해 필요
- 성능 영향 확인 필요

---

### [FAQ]

Q. Fetch Join에서 distinct는 왜 사용하는가?
A. Collection Join으로 Root Entity가 중복 조회될 수 있기 때문이다.

Q. distinct를 쓰면 Collection Fetch Join Pagination 문제가 해결되는가?
A. 아니다. 중복 제거와 Pagination 문제는 별개다.

---

# 6. Group By

## 6.1 Aggregation Query

### [개념]

Group By는 데이터를 특정 기준으로 그룹화하여 집계하는 Query 방식이다.

통계 API, 대시보드, 관리자 리포트에서 자주 사용한다.

---

### [핵심]

- GroupBy
- Count
- Sum
- Avg
- Max
- Min
- Having
- Reporting Query

---

### [예제]

```java
List<Tuple> result = queryFactory
    .select(user.status, user.count())
    .from(user)
    .groupBy(user.status)
    .fetch();
```

Having:

```java
List<Tuple> result = queryFactory
    .select(user.status, user.count())
    .from(user)
    .groupBy(user.status)
    .having(user.count().goe(10))
    .fetch();
```

---

### [실무]

Group By 주요 사용처:

- 상태별 회원 수
- 지역별 축제 수
- 월별 주문 수
- 카테고리별 리뷰 수
- 일별 매출 집계

---

### [주의]

- Group By 결과는 DTO Projection 권장
- Tuple은 임시 조회에만 사용 권장
- 집계 컬럼 Index 고려
- 대용량 집계는 별도 통계 테이블 검토

---

### [FAQ]

Q. Group By는 언제 사용하는가?
A. 특정 기준으로 데이터를 묶어 count, sum, avg 같은 집계 결과가 필요할 때 사용한다.

Q. Having은 언제 사용하는가?
A. Group By 이후 집계 결과에 조건을 걸 때 사용한다.

Q. Group By 결과는 어떻게 반환하는 것이 좋은가?
A. DTO Projection으로 반환하는 것이 좋다.

---

# 7. SubQuery

## 7.1 SubQuery 개념

### [개념]

SubQuery는 Query 내부에서 또 다른 Query를 사용하는 방식이다.

QueryDSL에서는 `JPAExpressions`를 사용한다.

---

### [핵심]

- JPAExpressions
- Exists
- In
- Avg
- Max
- Nested Query
- Complex Condition

---

### [예제]

Max SubQuery:

```java
List<User> result = queryFactory
    .selectFrom(user)
    .where(
        user.age.eq(
            JPAExpressions
                .select(user.age.max())
                .from(user)
        )
    )
    .fetch();
```

Exists SubQuery:

```java
List<User> result = queryFactory
    .selectFrom(user)
    .where(
        JPAExpressions
            .selectOne()
            .from(order)
            .where(order.user.eq(user))
            .exists()
    )
    .fetch();
```

---

### [실무]

SubQuery는 복잡한 조건 Query에서 유용하다.

다만 Join으로 대체 가능한 경우 Join이 더 나은지 먼저 검토한다.

---

### [주의]

- 성능 비용 큼
- Nested Query 과도 사용 금지
- Execution Plan 확인 필요
- Join 대체 가능 여부 검토
- JPA는 FROM 절 SubQuery 제약이 있음

---

### [FAQ]

Q. QueryDSL SubQuery 객체는?
A. `JPAExpressions`이다.

Q. SubQuery는 언제 사용하는가?
A. Exists, In, Max, Avg 같은 복잡한 조건 Query에서 사용한다.

Q. SubQuery 사용 시 주의점은?
A. 성능 비용이 클 수 있으므로 Execution Plan을 확인해야 한다.

---

# 8. Bulk Operation

## 8.1 Bulk Update / Delete

### [개념]

Bulk Operation은 여러 Row를 한 번에 수정하거나 삭제하는 Query이다.

QueryDSL은 `update()`, `delete()`를 통해 Bulk Query를 지원한다.

---

### [핵심]

- Bulk Update
- Bulk Delete
- 대량 데이터 처리
- DB 직접 수정
- Persistence Context 우회
- Flush / Clear 필요

---

### [예제]

Bulk Update:

```java
long count = queryFactory
    .update(user)
    .set(user.status, UserStatus.ACTIVE)
    .where(user.age.goe(20))
    .execute();
```

Bulk Delete:

```java
long count = queryFactory
    .delete(user)
    .where(user.status.eq(UserStatus.DELETED))
    .execute();
```

Flush / Clear:

```java
entityManager.flush();
entityManager.clear();
```

---

### [Flow]

```text
Bulk Execute
→ DB Direct Update
→ Persistence Context Not Updated
→ Data Mismatch Risk
→ entityManager.flush()
→ entityManager.clear()
```

---

### [실무]

Bulk Operation 주요 사용처:

- Batch Job
- Admin Bulk Update
- Migration
- 만료 데이터 정리
- 상태 일괄 변경

---

### [주의]

매우 중요:

Bulk Operation은 Persistence Context를 우회하고 DB를 직접 수정한다.

따라서 이미 영속성 컨텍스트에 올라온 Entity와 DB 데이터가 불일치할 수 있다.

Bulk Operation 이후에는 `flush()`와 `clear()`를 고려한다.

---

### [FAQ]

Q. Bulk Operation 장점은?
A. 여러 Row를 한 번에 처리할 수 있어 대량 수정 성능이 좋다.

Q. Bulk Operation 후 clear가 필요한 이유는?
A. Persistence Context와 DB 상태 불일치를 방지하기 위해서다.

Q. Bulk Operation은 Entity 변경 감지를 사용하는가?
A. 아니다. DB에 직접 Update 또는 Delete Query를 실행한다.

---

# 9. Count Query Optimization

## 9.1 Count Query 분리

### [개념]

Pagination Query는 Content Query와 Count Query를 분리하는 것이 실무 기본이다.

Content Query에는 Join과 Projection이 필요할 수 있지만, Count Query는 최대한 단순해야 한다.

---

### [핵심]

- Content Query 분리
- Count Query 분리
- 불필요 Join 제거
- PageableExecutionUtils 활용
- Count Query Slow 대응
- Pagination 성능 최적화

---

### [예제]

Content Query:

```java
List<UserListDto> content = queryFactory
    .select(Projections.constructor(
        UserListDto.class,
        user.id,
        user.username,
        user.createdAt
    ))
    .from(user)
    .leftJoin(user.orders, order)
    .where(statusEq(status))
    .offset(pageable.getOffset())
    .limit(pageable.getPageSize())
    .fetch();
```

Count Query:

```java
JPAQuery<Long> countQuery = queryFactory
    .select(user.count())
    .from(user)
    .where(statusEq(status));
```

Page 생성:

```java
return PageableExecutionUtils.getPage(
    content,
    pageable,
    countQuery::fetchOne
);
```

---

### [실무]

Count Query 최적화 핵심:

- Count Query에서 불필요한 Join 제거
- Count Query 조건 최소화
- Count Query와 Content Query 분리
- Slice로 Count Query 제거 가능 여부 검토
- Cursor Paging 전환 검토

---

### [주의]

- Content Query를 그대로 Count Query로 복사하지 않는다.
- Fetch Join은 Count Query에 사용하지 않는다.
- 복잡한 Count Query는 성능 병목이 된다.
- 전체 개수가 필요 없으면 Slice를 사용한다.

---

### [FAQ]

Q. Count Query를 분리하는 이유는?
A. Pagination 성능을 최적화하기 위해서다.

Q. Count Query 최적화 핵심은?
A. Count Query에서 불필요한 Join을 제거하는 것이다.

Q. 전체 개수가 필요 없으면 무엇을 사용하는가?
A. Slice를 사용해 Count Query를 제거한다.

---

# 10. Query Optimization

## 10.1 Performance Optimization

### [개념]

Query Optimization은 Query 성능 병목을 분석하고 개선하는 과정이다.

QueryDSL 최적화는 결국 실행 SQL, Query Count, Index, Execution Plan 확인이 핵심이다.

---

### [핵심]

- Fetch Join
- DTO Projection
- Index
- Query Count
- Execution Plan
- Count Query Optimization
- Pagination Strategy

---

### [Checklist]

- N+1 발생 여부 확인
- Fetch Join 필요 여부 확인
- DTO Projection 가능 여부 확인
- Count Query 비용 확인
- Full Table Scan 여부 확인
- Index 존재 여부 확인
- Deep Paging 여부 확인
- SQL 로그 확인
- Execution Plan 확인

---

### [실무]

주요 병목:

- N+1 Problem
- Count Query Slow
- Full Table Scan
- Deep Paging
- 불필요한 Join
- Projection 미사용
- contains 검색 남발

---

### [FAQ]

Q. QueryDSL 최적화 핵심은?
A. Fetch Join, DTO Projection, Index, Count Query 최적화이다.

Q. 가장 흔한 병목은?
A. N+1, Count Query Slow, Full Table Scan, Deep Paging이다.

Q. 최적화 전 무엇을 확인해야 하는가?
A. SQL 로그, Query Count, Execution Plan을 확인해야 한다.

---

# 11. Common Practical Problems

## 11.1 Troubleshooting

### [Troubleshooting]

문제: N+1 발생

원인:

- Lazy Loading
- Fetch Join 누락
- 연관 Entity 반복 접근

해결:

- Fetch Join 적용
- DTO Projection 사용
- Batch Size 검토
- EntityGraph 검토

---

문제: Count Query 느림

원인:

- Join 많음
- Content Query를 그대로 Count Query에 사용
- 불필요한 조건 포함

해결:

- Count Query 분리
- 불필요 Join 제거
- PageableExecutionUtils 사용
- Slice 전환 검토

---

문제: Full Table Scan 발생

원인:

- Index 부재
- contains 검색
- 조건 컬럼 Index 미설계

해결:

- Index 추가
- 검색 조건 개선
- Prefix Search 또는 Search Engine 검토

---

문제: Bulk Update 후 데이터 이상

원인:

- Persistence Context 미정리
- DB는 변경됐지만 영속 Entity는 이전 상태 유지

해결:

- entityManager.flush()
- entityManager.clear()

---

문제: Collection Fetch Join Pagination 경고 발생

원인:

- OneToMany Fetch Join과 Pageable 조합

해결:

- DTO Projection 사용
- Batch Size 사용
- Query 분리
- Collection Fetch Join 제거

---

### [FAQ]

Q. QueryDSL 실무 주요 문제는?
A. N+1, Count Query Slow, Full Scan, Bulk Update Issue, Collection Fetch Join Pagination 문제이다.

Q. 성능 문제는 어떻게 확인하는가?
A. SQL 로그, Query Count, Execution Plan으로 확인한다.

---

# 12. Best Practice

## 12.1 QueryDSL Best Practice

### [핵심]

- QueryDSL Query는 Repository 계층에 작성
- Dynamic Query는 BooleanExpression 우선
- 복잡한 OR 조건은 BooleanBuilder 검토
- Entity 직접 반환 지양
- 목록 API는 DTO Projection 우선
- N+1은 Fetch Join 또는 DTO Projection으로 해결
- Collection Fetch Join + Pagination 지양
- Page 남발 금지
- 무한 스크롤은 Slice 우선
- 대규모 피드는 Cursor Paging 검토
- Count Query는 Content Query와 분리
- Bulk Operation 이후 flush / clear 고려
- SQL 로그와 Execution Plan 확인

---

### [실무]

QueryDSL 실무 판단 흐름:

```text
Simple CRUD
→ Spring Data JPA

Complex Search
→ QueryDSL Dynamic Query

List API
→ DTO Projection + Pagination

Infinite Scroll
→ Slice

N+1 Problem
→ Fetch Join or DTO Projection

Large Feed
→ Cursor Paging

Bulk Update
→ Execute + Flush/Clear
```

---

### [FAQ]

Q. QueryDSL Best Practice 핵심은?
A. Repository 분리, BooleanExpression, DTO Projection, Fetch Join, Count Query 분리이다.

Q. 목록 API Best Practice는?
A. DTO Projection과 Pagination을 함께 사용하고 Count Query를 분리한다.

Q. 무한 스크롤 Best Practice는?
A. Page보다 Slice를 우선 고려한다.

---

# 13. Related Documents

- QueryDSL_Practical_Part01_Basic.md
- QueryDSL_Practical_Part02_Dynamic_Query.md
- QueryDSL_Practical_Part03_Paging_Projection.md

---

# Retrieval Queries

### [FAQ]

Q. QueryDSL Repository 구조는?
A. JpaRepository, Custom Repository, RepositoryImpl 또는 QueryRepository 구조를 사용한다.

Q. QueryDSL 코드는 어디에 작성하는가?
A. Repository 계층의 Custom Repository 또는 Query Repository 구현체에 작성한다.

Q. Fetch Join이란?
A. Join과 동시에 연관 Entity를 즉시 로딩하는 JPA 조회 방식이다.

Q. Fetch Join 장점은?
A. Lazy Loading으로 인한 N+1 Problem을 해결할 수 있다.

Q. 일반 Join과 Fetch Join 차이는?
A. 일반 Join은 조건 연결이고, Fetch Join은 연관 Entity 즉시 로딩까지 수행한다.

Q. N+1 Problem이란?
A. 최초 목록 Query 1번 이후 연관 Entity 조회 Query가 N번 추가 발생하는 문제다.

Q. N+1은 어떻게 해결하는가?
A. Fetch Join, DTO Projection, Batch Size, EntityGraph를 상황에 맞게 사용한다.

Q. Collection Fetch Join + Pagination 문제는?
A. 메모리 Pagination, 중복 Entity, 성능 저하가 발생할 수 있다.

Q. Fetch Join에서 distinct는 왜 사용하는가?
A. Collection Join으로 Root Entity가 중복 조회될 수 있기 때문이다.

Q. distinct가 Collection Fetch Join Pagination 문제를 해결하는가?
A. 아니다. distinct는 중복 완화용이며 Pagination 문제 해결책은 아니다.

Q. Group By는 언제 사용하는가?
A. count, sum, avg 같은 집계 Query 작성 시 사용한다.

Q. Having은 언제 사용하는가?
A. Group By 이후 집계 결과에 조건을 걸 때 사용한다.

Q. QueryDSL SubQuery 객체는?
A. JPAExpressions이다.

Q. SubQuery 사용 시 주의점은?
A. 성능 비용이 클 수 있으므로 Execution Plan을 확인해야 한다.

Q. Bulk Operation이란?
A. 여러 Row를 한 번에 수정하거나 삭제하는 Query이다.

Q. Bulk Operation 후 clear가 필요한 이유는?
A. Persistence Context와 DB 상태 불일치를 방지하기 위해서다.

Q. Count Query를 분리하는 이유는?
A. Pagination 성능을 최적화하기 위해서다.

Q. Count Query 최적화 핵심은?
A. 불필요한 Join 제거와 PageableExecutionUtils 활용이다.

Q. QueryDSL 최적화 핵심은?
A. Fetch Join, DTO Projection, Index, Count Query 최적화이다.

Q. QueryDSL 실무 주요 문제는?
A. N+1, Count Query Slow, Full Table Scan, Bulk Update Issue, Collection Fetch Join Pagination 문제이다.
