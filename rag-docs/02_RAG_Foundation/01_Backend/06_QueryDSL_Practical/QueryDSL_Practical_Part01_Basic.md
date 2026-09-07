# QueryDSL Practical Part01 Basic

---

# 1. QueryDSL Overview

## 1.1 QueryDSL 개념

### [개념]

QueryDSL은 Java 코드 기반 Type-safe Query Builder이다.

문자열 기반 JPQL 대신 QClass를 사용하여 컴파일 시점에 Query 오류를 검출할 수 있다.

Spring Boot 3.x + JPA + Hibernate 6 환경에서 Dynamic Query, Projection, Pagination, Join Query 작성에 최적화되어 있다.

---

### [핵심]

- QueryDSL = Type-safe Query Builder
- 문자열 JPQL 대체
- Compile-time Validation
- Dynamic Query 강점
- DTO Projection 지원
- Pagination 지원
- Join / Fetch Join 지원

---

### [실무]

2026 실무 기준 QueryDSL은 모든 Query를 대체하지 않는다.

역할 분리:

```text
Simple CRUD
→ Spring Data JPA

Complex Query
→ QueryDSL
```

주 사용 사례:

- 검색 API
- 관리자 필터링
- 통계 API
- 복잡한 Join Query
- Dynamic Query

---

### [Flow]

```text
Entity
→ QClass
→ JPAQueryFactory
→ Query Build
→ JPQL
→ SQL
→ Result Mapping
```

---

### [FAQ]

Q. QueryDSL이란?
A. Java 코드로 Type-safe Query를 작성하는 Query Builder이다.

Q. QueryDSL은 언제 사용하는가?
A. Dynamic Query, Join, Projection, Pagination이 필요한 복잡한 조회에서 사용한다.

Q. QueryDSL이 JPA를 대체하는가?
A. 아니다. JPA 기반에서 Query 작성만 QueryDSL로 수행한다.

---

# 2. Build Configuration

## 2.1 QueryDSL 설정

### [개념]

QueryDSL 사용 전 Gradle 의존성과 Annotation Processor 설정이 필요하다.

QClass는 Build 시 자동 생성된다.

---

### [핵심]

- QueryDSL Dependency 필요
- Annotation Processor 필요
- generated source 필요
- Build 시 QClass 생성

---

### [예제]

Gradle:

```gradle
dependencies {
    implementation "com.querydsl:querydsl-jpa:5.1.0:jakarta"
    annotationProcessor "com.querydsl:querydsl-apt:5.1.0:jakarta"
    annotationProcessor "jakarta.annotation:jakarta.annotation-api"
    annotationProcessor "jakarta.persistence:jakarta.persistence-api"
}
```

Build:

```bash
./gradlew clean build
```

---

### [실무]

Spring Boot 3.x 이상은 반드시 Jakarta 버전 사용.

권장 버전:

- Spring Boot 3.x
- Java 21
- QueryDSL 5.x
- Hibernate 6

---

### [주의]

- `javax` 버전 사용 금지
- `jakarta` 버전 사용
- Boot 3.x와 버전 맞춤 필수

---

### [FAQ]

Q. QueryDSL 설정 핵심은?
A. querydsl-jpa, querydsl-apt, annotationProcessor 설정이다.

Q. Spring Boot 3.x에서 주의점은?
A. 반드시 Jakarta 버전을 사용해야 한다.

Q. QClass는 언제 생성되는가?
A. Build 시 자동 생성된다.

---

# 3. QClass

## 3.1 QClass 개념

### [개념]

QClass는 Entity 기반으로 자동 생성되는 QueryDSL 메타모델 클래스이다.

Type-safe Query 핵심이다.

---

### [핵심]

- Generated Class
- Entity 기반
- Type-safe Query 핵심
- Compile-time Validation

---

### [예제]

Entity:

```java
@Entity
public class User {
    @Id
    private Long id;
    private String username;
    private Integer age;
}
```

QClass:

```java
QUser user = QUser.user;
```

---

### [실무]

QClass가 생성되지 않으면 QueryDSL 사용이 불가능하다.

대부분 원인:

- Gradle 설정 문제
- Annotation Processor 누락
- Build 실패

---

### [Troubleshooting]

문제: QClass 생성 실패

원인:

- Dependency 누락
- Processor 누락
- Build 실패

해결:

- Gradle 확인
- clean build 실행

---

### [FAQ]

Q. QClass란?
A. Entity 기반으로 생성되는 QueryDSL 메타모델 클래스이다.

Q. QClass는 직접 작성하는가?
A. 아니다. Build 시 자동 생성된다.

Q. QClass 생성 실패 원인은?
A. Gradle 설정 또는 Annotation Processor 문제다.

---

# 4. JPAQueryFactory

## 4.1 JPAQueryFactory 개념

### [개념]

JPAQueryFactory는 QueryDSL Query 생성 시작점이다.

모든 QueryDSL Query는 JPAQueryFactory 중심으로 작성된다.

---

### [핵심]

- Query Start Point
- EntityManager 기반
- select / update / delete 지원
- QueryDSL 핵심 객체

---

### [예제]

Config:

```java
@Configuration
public class QuerydslConfig {

    @PersistenceContext
    private EntityManager em;

    @Bean
    public JPAQueryFactory queryFactory() {
        return new JPAQueryFactory(em);
    }
}
```

Repository:

```java
@RequiredArgsConstructor
public class UserRepositoryImpl {

    private final JPAQueryFactory queryFactory;
}
```

---

### [Flow]

```text
EntityManager
→ JPAQueryFactory
→ Query Build
→ Execute
```

---

### [FAQ]

Q. JPAQueryFactory란?
A. QueryDSL Query 생성 및 실행 객체이다.

Q. 왜 필요한가?
A. QueryDSL Query의 시작점이기 때문이다.

Q. 무엇 기반인가?
A. EntityManager 기반이다.

---

# 5. Basic Query

## 5.1 selectFrom

### [개념]

selectFrom은 Entity 전체 조회 기본 Query이다.

---

### [핵심]

- 기본 조회
- Entity 전체 조회
- where 조합 가능

---

### [예제]

```java
List<User> result = queryFactory
    .selectFrom(user)
    .fetch();
```

조건 조회:

```java
List<User> result = queryFactory
    .selectFrom(user)
    .where(user.username.eq("kim"))
    .fetch();
```

---

### [실무]

Entity 직접 반환은 내부 로직에서만 제한적으로 사용한다.

API 응답은 DTO Projection 권장.

---

### [FAQ]

Q. selectFrom이란?
A. Entity 전체 조회용 QueryDSL 기본 메서드이다.

Q. 언제 사용하는가?
A. Entity 조회 시 사용한다.

---

## 5.2 fetch 계열

### [개념]

fetch 계열 메서드는 Query 실행 시점이다.

---

### [핵심]

- fetch()
- fetchOne()
- fetchFirst()

---

### [예제]

```java
.fetch()
```

```java
.fetchOne()
```

```java
.fetchFirst()
```

---

### [실무]

- fetch = List
- fetchOne = 단건
- fetchFirst = 첫 row

주의:

- fetchOne은 2건 이상 시 예외 가능

---

### [FAQ]

Q. fetch란?
A. Query를 실행하고 결과를 반환한다.

Q. fetchOne 주의점은?
A. 결과가 여러 개면 예외가 발생할 수 있다.

---

# 6. Where Condition

## 6.1 Condition

### [개념]

where는 조건식을 구성한다.

---

### [핵심]

- eq
- ne
- gt
- goe
- lt
- loe
- in
- contains

---

### [예제]

```java
queryFactory
    .selectFrom(user)
    .where(
        user.username.eq("kim"),
        user.age.goe(20)
    )
    .fetch();
```

---

### [실무]

where multiple condition = AND

Dynamic Query는 Part02에서 다룬다.

---

### [FAQ]

Q. where 여러 조건은?
A. AND 조건으로 결합된다.

Q. contains 주의점은?
A. Index 효율이 떨어질 수 있다.

---

# 7. Order By

## 7.1 Sorting

### [개념]

orderBy는 정렬 조건이다.

---

### [핵심]

- asc
- desc
- multi sort

---

### [예제]

```java
queryFactory
    .selectFrom(user)
    .orderBy(
        user.createdAt.desc(),
        user.id.desc()
    )
    .fetch();
```

---

### [실무]

Pagination 시 안정적인 정렬 기준 중요.

권장:

```text
createdAt + id
```

---

### [FAQ]

Q. 정렬 기준 여러 개 가능?
A. 가능하다.

Q. Pagination에서 중요한 이유는?
A. 데이터 누락/중복 방지를 위해서다.

---

# 8. Repository Pattern

## 8.1 구조

### [개념]

QueryDSL은 Custom Repository 구조가 일반적이다.

---

### [핵심]

- Repository
- Custom Repository
- RepositoryImpl

---

### [예제]

```text
UserRepository
UserRepositoryCustom
UserRepositoryImpl
```

---

### [실무]

권장 구조:

```text
Repository
→ Custom Repository
→ QueryDSL Implementation
```

---

### [FAQ]

Q. QueryDSL 코드는 어디에 작성하는가?
A. RepositoryImpl에 작성한다.

Q. Service에 작성해도 되는가?
A. 권장하지 않는다.

---

# 9. DTO Mapping

## 9.1 DTO Mapping

### [개념]

Entity 직접 반환보다 DTO Mapping이 권장된다.

---

### [핵심]

- Entity 직접 반환 지양
- DTO 권장
- Projection 사용

---

### [실무]

Entity 직접 반환 문제:

- Lazy Loading
- 순환 참조
- 불필요 데이터 노출

---

### [FAQ]

Q. DTO Mapping이 필요한 이유는?
A. API 응답 구조와 Entity를 분리하기 위해서다.

Q. Projection은 어디서 다루는가?
A. Part03에서 다룬다.

---

# 10. Related Documents

- QueryDSL_Practical_Part02_Dynamic_Query.md
- QueryDSL_Practical_Part03_Paging_Projection.md
- QueryDSL_Practical_Part04_Practical.md

---

# Retrieval Queries

### [FAQ]

Q. QueryDSL이란?
A. Java 기반 Type-safe Query Builder이다.

Q. QueryDSL 핵심 객체는?
A. QClass와 JPAQueryFactory이다.

Q. QClass란?
A. Entity 기반 Generated Class이다.

Q. JPAQueryFactory란?
A. QueryDSL Query 시작점이다.

Q. selectFrom이란?
A. Entity 전체 조회 기본 메서드이다.

Q. fetchOne 주의점은?
A. 결과가 여러 개면 예외 가능하다.

Q. QueryDSL Repository 구조는?
A. Repository, Custom Repository, RepositoryImpl 구조다.

Q. DTO Mapping이 필요한 이유는?
A. Entity 직접 반환 문제를 방지하기 위해서다.
