# Testing Part 03 - Repository Test

---

# 1. Repository Test Core

## 1.1 Repository Test Overview

### [개념]

Repository Test는 Persistence Layer를 검증하는 테스트다.

주요 목적:

- Query Validation
- Entity Mapping Validation
- Constraint Validation
- Database Behavior Validation

---

### [핵심]

검증 대상:

- Query Method
- JPQL
- Native Query
- Entity Mapping
- Constraint
- Transaction Behavior

---

### [실무]

2026 Spring Boot 실무 기준 Repository Test는 DB Query 정확성과 Mapping 검증이 핵심이다.

특히 중요:

- Complex Join Query
- QueryDSL Query
- Native SQL
- Constraint Validation

---

### [FAQ]

Q. Repository Test란?
A. Persistence Layer 검증 테스트다.

Q. Repository Test 핵심은?
A. Query, Mapping, Constraint 검증이다.

---

# 2. Repository Test Scope

## 2.1 Test Target

### [개념]

Repository Layer만 집중 검증한다.

---

### [핵심]

포함:

- JpaRepository
- Custom Repository
- QueryDSL Repository

제외:

- Service Logic
- Controller
- External API

---

### [FAQ]

Q. Business Logic도 Repository Test 대상인가?
A. 아니다. Repository Layer만 검증한다.

---

# 3. Core Annotation

## 3.1 @DataJpaTest

### [개념]

@DataJpaTest는 JPA 관련 Bean만 로드한다.

---

### [핵심]

포함:

- Repository
- EntityManager
- JPA Components

제외:

- Controller
- Service
- Security

---

### [예제]

```java
@DataJpaTest
class UserRepositoryTest {
}
```

---

### [Flow]

```text
Load JPA Context
→ Execute Query
→ Validate Result
```

---

### [FAQ]

Q. Repository Test에서 SpringBootTest가 필요한가?
A. 대부분 필요 없다. DataJpaTest가 더 적합하다.

---

# 4. Query Method Test

## 4.1 Derived Query

### [개념]

Method Naming 기반 Query 검증.

---

### [핵심]

검증 대상:

- findBy
- existsBy
- countBy
- deleteBy

---

### [예제]

```java
Optional<User> findByEmail(String email);
```

---

### [FAQ]

Q. Derived Query도 테스트가 필요한가?
A. 핵심 Query라면 테스트 권장이다.

---

# 5. JPQL Test

## 5.1 Custom Query

### [개념]

@Query 기반 JPQL 검증.

---

### [핵심]

반드시 검증:

- Join
- Projection
- Sorting
- Filtering

---

### [예제]

```java
@Query("select u from User u where u.email = :email")
Optional<User> findByEmailJPQL(String email);
```

---

### [FAQ]

Q. JPQL 테스트가 중요한 이유는?
A. 런타임 Query 오류 가능성이 높기 때문이다.

---

# 6. Native Query Test

## 6.1 Native SQL

### [개념]

Native Query는 실제 DB SQL을 직접 사용한다.

---

### [핵심]

검증 대상:

- SQL Syntax
- Result Mapping
- DB Compatibility

---

### [FAQ]

Q. Native Query가 위험한 이유는?
A. DB 의존성과 SQL 오류 가능성이 높다.

---

# 7. Entity Mapping Test

## 7.1 Mapping Validation

### [개념]

Entity 관계와 Mapping 정확성을 검증한다.

---

### [핵심]

검증 대상:

- OneToOne
- OneToMany
- ManyToOne
- ManyToMany

---

### [FAQ]

Q. Mapping Test가 중요한 이유는?
A. Lazy Loading, Cascade 문제를 조기 발견할 수 있다.

---

# 8. Constraint Test

## 8.1 Constraint Validation

### [개념]

DB Constraint 검증.

---

### [핵심]

검증 대상:

- Unique
- Not Null
- Foreign Key
- Check Constraint

---

### [FAQ]

Q. Constraint Test는 필요한가?
A. 필수다. 운영 DB 오류 예방에 중요하다.

---

# 9. Transaction Test

## 9.1 Rollback

### [개념]

DataJpaTest는 기본 Rollback된다.

---

### [Flow]

```text
Transaction Start
→ Test Execute
→ Rollback
```

---

### [FAQ]

Q. 테스트 데이터가 남지 않는 이유는?
A. 테스트 종료 후 자동 Rollback 되기 때문이다.

---

# 10. H2 vs Production DB

## 10.1 Database Difference

### [개념]

H2는 운영 DB와 완전히 동일하지 않다.

---

### [Comparison]

| Category   | H2   | Production DB |
| ---------- | ---- | ------------- |
| Speed      | Fast | Normal        |
| Cost       | Low  | Higher        |
| Similarity | Low  | High          |

---

### [주의]

차이 발생 가능:

- SQL Dialect
- JSON Column
- Index Behavior
- Lock Behavior

---

### [FAQ]

Q. H2만 사용해도 되는가?
A. 단순 Query는 가능하지만 복잡한 Query는 위험하다.

---

# 11. Repository Test Rules

## 11.1 Best Practice

### [Best Practice]

권장:

- Query별 테스트 작성
- Mapping 검증
- Constraint 검증
- Rollback 활용

---

### [주의]

금지:

- Service Logic 포함
- Full Context 남용
- Query 미검증

---

### [Checklist]

- Query 검증 완료
- Mapping 검증 완료
- Constraint 검증 완료
- DB 차이 고려

---

# 12. Common Mistakes

## 12.1 Frequent Issues

### [Troubleshooting]

문제:

Query 실패

원인:

JPQL Syntax Error

해결:

Query 검토

---

문제:

LazyInitializationException

원인:

Lazy Loading

해결:

Transaction 범위 확인

---

문제:

H2 성공, 운영 DB 실패

원인:

Dialect 차이

해결:

Testcontainers 검토

---

# 13. Agent Decision Rules

## 13.1 Test Routing

### [Flow]

```text
DB Query Validation
→ Repository Test

Complex DB Behavior
→ Repository Test + Testcontainers

Business Logic Validation
→ Service Test
```

---

### [핵심]

Backend Agent Routing 기준.

---

### [FAQ]

Q. 언제 Repository Test를 생성해야 하는가?
A. DB Query와 Entity Mapping 검증이 필요할 때다.

---

# Retrieval Queries

### [FAQ]

Q. Repository Test란?
A. Persistence Layer 검증 테스트다.

Q. Repository Test 핵심 Annotation은?
A. @DataJpaTest.

Q. Repository Test 핵심 검증은?
A. Query, Mapping, Constraint.

Q. H2만 믿어도 되는가?
A. 복잡한 Query는 위험하다.

Q. 언제 Testcontainers가 필요한가?
A. 운영 DB와 차이 검증이 필요할 때.
