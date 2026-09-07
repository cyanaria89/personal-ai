# QueryDSL Practical Domain Rules

---

# 1. Domain Purpose

QueryDSL Practical Domain 문서는 Backend Agent / Review Agent용 RAG 문서이다.

목적:

- Dynamic Query Retrieval
- Complex Query Generation
- Query Refactoring Support
- Query Optimization Support
- Query Troubleshooting Support

우선순위:

1. Dynamic Query Generation
2. Query Optimization
3. Projection / Pagination
4. Practical Repository Pattern

---

# 2. Scope

포함 범위:

- QueryDSL Core
- QClass
- JPAQueryFactory
- Predicate
- BooleanExpression
- Dynamic Query
- Pageable
- Pagination
- Projection
- DTO Mapping
- Join
- Fetch Join
- GroupBy
- SubQuery
- Bulk Operation
- Query Optimization
- Repository Pattern

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

# 4. QueryDSL Core Rules

QueryDSL 문서는 Query Builder 중심으로 작성.

핵심 구조:

- Entity
- QClass
- QueryFactory
- Query Builder
- Result Mapping

---

반드시 설명 포함:

- 역할
- 책임
- Query Flow
- SQL 변환 흐름

---

예:

```text
Entity
→ QClass
→ QueryFactory
→ Query Build
→ SQL
→ Result Mapping
```

---

# 5. Query Factory Rules

핵심:

- JPAQueryFactory
- Query Start Point

---

예:

```java
@RequiredArgsConstructor
@Repository
public class UserRepositoryCustomImpl implements UserRepositoryCustom {

    private final JPAQueryFactory queryFactory;
}
```

---

반드시 설명:

- 왜 JPAQueryFactory를 사용하는가
- QueryDSL에서 핵심 역할은 무엇인가

---

중요:

모든 QueryDSL Query는 QueryFactory 중심.

---

# 6. QClass Rules

반드시 설명:

- QClass란 무엇인가
- Generated Class 역할
- Build 시 생성 방식

---

예:

```java
QUser user = QUser.user;
```

---

핵심:

QClass는 Type-safe Query 핵심.

---

금지:

QClass 설명 생략.

---

# 7. Dynamic Query Rules

Dynamic Query는 QueryDSL 핵심.

반드시 포함:

- BooleanBuilder
- BooleanExpression
- Null-safe Condition

---

예:

```java
private BooleanExpression usernameEq(String username) {
    return username != null ? user.username.eq(username) : null;
}
```

---

반드시 설명:

- Optional Filter
- Dynamic Condition 조합

---

중요:

QueryDSL 문서 품질은 Dynamic Query 설명 품질이 결정.

---

# 8. BooleanBuilder Rules

포함 대상:

- Complex Condition
- Multi Condition

---

예:

```java
BooleanBuilder builder = new BooleanBuilder();
builder.and(user.age.goe(20));
```

---

장점:

- 직관적
- 조건 누적 쉬움

---

단점:

- 코드 길어질 수 있음

---

# 9. BooleanExpression Rules

실무 권장 방식.

예:

```java
.where(
    usernameEq(username),
    ageGoe(age)
)
```

---

장점:

- 재사용성
- 가독성
- 유지보수

---

반드시 비교:

- BooleanBuilder
- BooleanExpression

---

# 10. Projection Rules

반드시 포함:

- Tuple
- DTO Projection
- Constructor Projection
- Field Projection
- Bean Projection

---

예:

```java
.select(new QUserDto(user.id, user.name))
```

또는:

```java
Projections.constructor(UserDto.class, user.id, user.name)
```

---

중요:

Entity 전체 조회보다 DTO Projection 권장.

---

# 11. DTO Mapping Rules

반드시 설명:

- Entity 직접 반환 위험
- DTO 변환 이유

---

권장:

- Response DTO
- Query DTO

---

예:

```java
UserSummaryDto
UserDetailDto
```

---

# 12. Join Rules

포함:

- Inner Join
- Left Join
- Cross Join

---

예:

```java
.from(order)
.join(order.user, user)
```

---

반드시 설명:

- Join 종류
- Query 영향
- SQL 변환

---

# 13. Fetch Join Rules

매우 중요.

반드시 포함:

- N+1 Problem
- Fetch Join
- Performance Impact

---

예:

```java
.join(order.user, user).fetchJoin()
```

---

핵심:

QueryDSL + JPA 실무 핵심.

---

# 14. Pagination Rules

반드시 포함:

- offset
- limit
- Pageable
- Slice
- Page

---

예:

```java
.offset(pageable.getOffset())
.limit(pageable.getPageSize())
```

---

반드시 설명:

- Pagination Query
- Count Query 문제

---

# 15. GroupBy Rules

포함:

- GroupBy
- Aggregation
- Count
- Sum
- Avg

---

예:

```java
.groupBy(user.age)
```

---

반드시 설명:

- Aggregation Query
- Reporting Query

---

# 16. SubQuery Rules

포함:

- Exists
- In
- Max
- Avg

---

예:

```java
JPAExpressions
```

---

주의:

SubQuery는 성능 영향 설명 포함.

---

# 17. Bulk Operation Rules

포함:

- Bulk Update
- Bulk Delete

---

예:

```java
queryFactory
    .update(user)
    .set(user.status, Status.ACTIVE)
    .execute();
```

---

중요:

반드시 설명:

- Persistence Context 영향
- Flush / Clear 필요성

---

# 18. Query Optimization Rules

필수 포함:

- Fetch Join
- Projection
- Index
- Query Count
- Execution Plan

---

반드시 설명:

- SQL 확인
- 성능 병목

---

예:

- N+1
- Count Query Slow
- Full Scan

---

# 19. Repository Pattern Rules

권장 구조:

```text
Repository
→ Custom Repository
→ QueryDSL Implementation
```

---

예:

```java
UserRepository
UserRepositoryCustom
UserRepositoryImpl
```

---

반드시 설명:

- 역할 분리
- 유지보수성

---

# 20. Troubleshooting Rules

반드시 포함 추천.

예:

- QClass Not Generated
- NoSuchFieldError
- Query Slow
- N+1
- Count Query Slow
- Bulk Update Issue

---

형식:

문제:

원인:

해결:

---

# 21. Retrieval Optimization Rules

강조 대상:

- QueryDSL
- JPAQueryFactory
- BooleanBuilder
- BooleanExpression
- Projection
- Fetch Join
- Pagination
- Dynamic Query

키워드 반복 허용.

---

# 22. Version Rules

기준:

- Spring Boot 3.x
- Java 21
- QueryDSL 5.x
- JPA / Hibernate 6

---

Legacy 제외.

---

# 23. Common Mistakes

자주 발생:

- Dynamic Query 과복잡화
- Entity 직접 반환
- Fetch Join 누락
- Count Query 비효율
- Bulk Operation 후 Clear 누락
- Projection 미사용
- N+1 방치

---

# 24. Final Goal

QueryDSL Practical RAG 문서는 Agent가 아래 수행 가능해야 한다.

- Retrieve Query Pattern
- Generate Dynamic Query
- Review Query
- Optimize Query
- Find Performance Issues
- Suggest Fixes

문서 품질이 Query Generation 품질을 결정한다.
