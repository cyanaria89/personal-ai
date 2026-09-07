# JPA Advanced Part05 — Repository, JPQL, Query Method, Native Query

---

# 1. Repository Purpose

## 1.1 Repository Concept

### [개념]

Repository는 Entity 조회와 저장을 담당하는 Data Access Layer다.

Spring Data JPA Repository는 JPA Entity에 대한 CRUD, Query Method, Pagination, JPQL, Native Query 사용을 추상화한다.

Repository는 비즈니스 로직을 처리하는 계층이 아니라 Entity Persistence 접근을 담당하는 계층이다.

---

### [핵심]

핵심 키워드:

- Repository
- JpaRepository
- Data Access Layer
- Entity
- Query Method
- JPQL
- Native Query
- Optional
- List
- Page
- Slice
- Pageable
- DTO Projection
- QueryDSL
- Persistence Context

Repository 역할:

- Entity 저장
- Entity 단건 조회
- Entity 목록 조회
- Entity 삭제
- Query Method 제공
- JPQL 실행
- Native Query 실행
- Pagination Query 실행
- Projection Query 실행

---

### [실무]

기본 구조:

```java
public interface PostRepository extends JpaRepository<Post, Long> {
}
```

기본 사용 흐름:

```text
Controller
→ Service
→ Repository
→ Entity
→ Persistence Context
→ SQL
→ Database
```

SQL Foundation 연결:

```text
SQL SELECT
→ Repository findById / findAll / Query Method

SQL WHERE
→ Query Method 조건

SQL JOIN
→ JPQL Join / Fetch Join / QueryDSL

SQL INSERT
→ Repository save

SQL UPDATE
→ Dirty Checking / Bulk Query

SQL DELETE
→ Repository delete / Bulk Delete
```

권장:

- Repository는 Entity 접근 중심으로 유지
- 비즈니스 로직은 Service에서 처리
- 단건 조회 실패 가능성은 `Optional` 사용
- 목록 조회는 `List`, `Page`, `Slice` 기준 명확화
- 단순 조건은 Query Method 우선
- 복잡한 고정 Query는 JPQL 검토
- 동적 조건은 QueryDSL 검토
- DB 특화 Query는 Native Query 제한적 사용

주의:

- Repository에 비즈니스 흐름을 넣지 않는다.
- Repository Method 이름이 과도하게 길어지면 JPQL / QueryDSL로 분리한다.
- 모든 데이터를 `findAll`로 가져온 뒤 Java Stream으로 필터링하지 않는다.
- Repository는 Entity Field 이름 기준으로 Query Method를 작성한다.
- Transaction 경계는 일반적으로 Service Layer에서 관리한다.

---

### [FAQ]

Q. Repository는 뭐야?
A. Entity 조회, 저장, 삭제 같은 Data Access를 담당하는 계층이다.

Q. Repository에 비즈니스 로직을 넣어도 돼?
A. 권장하지 않는다. Repository는 Data Access 중심이고 비즈니스 흐름은 Service에서 처리한다.

Q. Repository는 SQL을 직접 실행해?
A. Spring Data JPA가 Repository Method, JPQL, Native Query를 기반으로 SQL을 생성하거나 실행한다.

Q. Transaction은 Repository에 붙이는 게 좋아?
A. 일반적으로 Service public method에 Transaction을 두고 Repository는 데이터 접근에 집중한다.

---

## 1.2 JpaRepository Rule

### [개념]

`JpaRepository`는 Spring Data JPA가 제공하는 Repository Interface다.

Entity Type과 ID Type을 Generic으로 지정하면 기본 CRUD와 Paging 기능을 사용할 수 있다.

---

### [핵심]

기본 형식:

```java
public interface EntityRepository extends JpaRepository<Entity, IdType> {
}
```

주요 기능:

- `save`
- `findById`
- `findAll`
- `delete`
- `existsById`
- `count`
- Paging
- Sorting
- Query Method

Generic 기준:

```text
JpaRepository<Post, Long>
→ Entity Type: Post
→ ID Type: Long
```

---

### [실무]

예시:

```java
public interface UserRepository extends JpaRepository<User, Long> {

    Optional<User> findByEmail(String email);

    boolean existsByEmail(String email);
}
```

Service 사용 예시:

```java
@Transactional(readOnly = true)
public UserResponse getUser(Long userId) {
    User user = userRepository.findById(userId)
            .orElseThrow(() -> new BusinessException("USER_NOT_FOUND", "사용자를 찾을 수 없습니다."));

    return UserResponse.from(user);
}
```

권장:

- Repository 이름은 `{Entity}Repository`
- ID Type은 Entity `@Id` Type과 일치
- 단건 조회는 `Optional<Entity>`
- 존재 여부는 `existsBy...`
- 중복 검사는 Service에서 Repository existsBy 호출
- 저장 후 반환 Entity 사용 여부는 프로젝트 기준 통일

주의:

- `save`는 신규 저장과 병합 상황을 구분해야 한다.
- 수정 작업에서 Managed Entity는 Dirty Checking을 우선 검토한다.
- `findById` 결과를 Controller까지 Optional 그대로 전달하지 않는다.
- Repository 반환 Entity를 API Response로 직접 노출하지 않는다.
- `deleteById`는 존재 여부와 예외 정책을 함께 검토한다.

---

### [FAQ]

Q. `JpaRepository<Post, Long>`에서 Long은 뭐야?
A. Post Entity의 Primary Key Type이다.

Q. `findById`는 왜 Optional을 반환해?
A. 해당 ID의 Entity가 없을 수 있기 때문이다.

Q. `save`는 insert야 update야?
A. 신규 Entity면 저장이고 Detached Entity면 merge처럼 동작할 수 있다. 수정은 Dirty Checking을 우선 검토한다.

Q. `existsByEmail`은 어디서 써?
A. 회원가입 같은 중복 검증에서 Service가 호출해 사전 검증에 사용한다.

---

# 2. Query Method

## 2.1 Query Method Concept

### [개념]

Query Method는 Repository Method 이름을 기반으로 Spring Data JPA가 Query를 생성하는 방식이다.

Entity Field 이름과 조건 키워드를 조합해 WHERE, ORDER BY, EXISTS 같은 Query를 표현한다.

---

### [핵심]

핵심 키워드:

- Query Method
- Method Name Query
- Entity Field
- WHERE
- ORDER BY
- AND
- OR
- Containing
- Between
- Exists
- Optional
- Slice
- Page

기본 예:

```java
Optional<Post> findByPostIdAndDeletedFalse(Long postId);

List<Post> findByTitleContainingOrderByCreatedAtDesc(String keyword);

boolean existsByEmail(String email);
```

---

### [실무]

SQL Foundation 연결:

```text
SQL WHERE
→ findByField

SQL AND
→ findByAAndB

SQL OR
→ findByAOrB

SQL LIKE
→ findByTitleContaining

SQL ORDER BY
→ OrderByCreatedAtDesc

SQL EXISTS
→ existsByEmail
```

예시:

```java
public interface PostRepository extends JpaRepository<Post, Long> {

    Optional<Post> findByPostIdAndDeletedFalse(Long postId);

    List<Post> findByTitleContainingOrderByCreatedAtDesc(String keyword);

    Slice<Post> findByUser_UserIdOrderByCreatedAtDesc(Long userId, Pageable pageable);

    boolean existsByTitle(String title);
}
```

권장:

- 조건이 단순할 때 사용
- Entity Field 이름을 정확히 사용
- Method 이름이 읽을 수 있는 수준일 때 사용
- 연관 Entity 조건은 `_` 경로 사용 가능
- 목록은 정렬 기준을 명확히 포함
- 무한 스크롤은 Slice 검토
- 전체 페이지 수가 필요하면 Page 검토

주의:

- Query Method는 DB Column 이름이 아니라 Entity Field 이름 기준이다.
- Method 이름이 너무 길어지면 유지보수성이 떨어진다.
- 조건 조합이 많으면 QueryDSL이 더 적합하다.
- 복잡한 Join Query는 JPQL / QueryDSL 검토
- Query Method는 생성 SQL을 반드시 확인해야 한다.

---

### [FAQ]

Q. Query Method는 뭐야?
A. Repository Method 이름을 기반으로 Spring Data JPA가 Query를 생성하는 방식이다.

Q. Query Method는 Column 이름 기준이야?
A. 아니다. Entity Field 이름 기준이다.

Q. Query Method는 언제 쓰는 게 좋아?
A. 조건이 단순하고 Method 이름이 과도하게 길어지지 않을 때 적합하다.

Q. Query Method가 너무 길어지면 어떻게 해?
A. JPQL이나 QueryDSL로 분리하는 것이 좋다.

---

## 2.2 Query Method Return Type

### [개념]

Query Method Return Type은 조회 결과의 개수, 실패 가능성, Pagination 요구사항에 따라 결정한다.

단건 조회는 `Optional`, 목록 조회는 `List`, Pagination 조회는 `Page` 또는 `Slice`를 사용한다.

---

### [핵심]

Return Type 기준:

| Return Type        | 사용 상황                      |
| ------------------ | ------------------------------ |
| `Optional<Entity>` | 단건 조회, 없을 수 있음        |
| `Entity`           | 반드시 존재해야 하는 내부 규칙 |
| `List<Entity>`     | 소량 목록                      |
| `Page<Entity>`     | 전체 count와 페이지 번호 필요  |
| `Slice<Entity>`    | 무한 스크롤 / 더보기           |
| `boolean`          | exists 조회                    |
| `long`             | count 조회                     |
| DTO                | Projection 조회                |

---

### [실무]

예시:

```java
Optional<User> findByEmail(String email);

List<Post> findByDeletedFalseOrderByCreatedAtDesc();

Page<Post> findByDeletedFalse(Pageable pageable);

Slice<Comment> findByPost_PostIdOrderByCreatedAtDesc(Long postId, Pageable pageable);

boolean existsByEmail(String email);

long countByUser_UserId(Long userId);
```

선택 기준:

```text
단건 + 없을 수 있음
→ Optional

소량 고정 목록
→ List

페이지 번호 UI
→ Page

무한 스크롤 / 더보기
→ Slice

존재 확인
→ boolean existsBy

개수 확인
→ long countBy
```

권장:

- 단건 조회 실패는 Service에서 예외로 변환
- Controller로 Optional을 그대로 반환하지 않음
- 대량 목록에 List 남용 금지
- Page는 count query 비용 검토
- Slice는 hasNext 중심 조회에 적합
- count가 필요 없으면 Slice 고려

주의:

- `List`로 대량 데이터를 전부 조회하지 않는다.
- `Page`는 Count Query가 추가로 실행될 수 있다.
- `Slice`는 전체 페이지 수를 제공하지 않는다.
- 단건 조회에서 결과가 여러 개면 오류가 발생할 수 있다.
- Return Type은 API 응답 구조와 성능에 영향을 준다.

---

### [FAQ]

Q. 단건 조회는 어떤 Return Type이 좋아?
A. 없을 수 있는 단건 조회는 `Optional<Entity>`가 적합하다.

Q. Page와 Slice는 뭐가 달라?
A. Page는 전체 count를 포함하고 Slice는 다음 페이지 존재 여부 중심이다.

Q. 무한 스크롤에는 Page와 Slice 중 뭐가 좋아?
A. 전체 페이지 수가 필요 없으면 Slice가 적합할 수 있다.

Q. List 조회는 언제 써?
A. 데이터 수가 작고 고정적이거나 Pagination이 필요 없는 경우에 사용한다.

---

## 2.3 Query Method Naming

### [개념]

Query Method Naming은 Entity Field 이름과 Spring Data JPA 키워드를 조합해 Repository Query를 표현하는 규칙이다.

Naming Consistency는 Query 생성, Code Generation, RAG Retrieval 정확도에 직접 영향을 준다.

---

### [핵심]

주요 키워드:

- `findBy`
- `existsBy`
- `countBy`
- `deleteBy`
- `And`
- `Or`
- `Between`
- `LessThan`
- `GreaterThan`
- `Containing`
- `StartingWith`
- `EndingWith`
- `OrderBy`
- `True`
- `False`
- `IsNull`
- `IsNotNull`

---

### [실무]

예시:

```java
Optional<Post> findByPostIdAndDeletedFalse(Long postId);

List<Post> findByTitleContainingAndDeletedFalseOrderByCreatedAtDesc(String title);

List<Festival> findByEventStartDateBetween(LocalDate startDate, LocalDate endDate);

boolean existsByUser_UserIdAndFestival_FestivalId(Long userId, Long festivalId);

long countByUser_UserIdAndReadStatusFalse(Long userId);
```

연관 Field 경로:

```text
Post.user.userId
→ findByUser_UserId

Favorite.user.userId + Favorite.festival.festivalId
→ existsByUser_UserIdAndFestival_FestivalId
```

권장:

- Method 이름은 읽기 가능한 수준으로 유지
- 3개 이상 조건 조합은 JPQL / QueryDSL 검토
- 연관 경로는 `_`로 명확히 표현
- Boolean 조건은 `True`, `False` 사용 가능
- 정렬 기준은 `OrderBy...Desc`로 명확화
- Soft Delete가 있으면 `DeletedFalse` 조건 누락 주의

주의:

- Field 이름 오타는 Application Startup Error를 만들 수 있다.
- Column 이름 기준으로 작성하면 실패한다.
- 너무 긴 Method 이름은 유지보수성이 낮다.
- OR 조건이 많으면 의도가 불명확해질 수 있다.
- 동적 검색 조건을 Query Method로 억지 작성하지 않는다.

---

### [FAQ]

Q. Query Method 이름은 어떤 기준으로 작성해?
A. Entity Field 이름과 Spring Data JPA 키워드를 조합해서 작성한다.

Q. 연관 Entity Field 조건은 어떻게 써?
A. `findByUser_UserId`처럼 `_`로 Field 경로를 표현할 수 있다.

Q. Boolean 조건은 어떻게 표현해?
A. `findByDeletedFalse`, `findByActiveTrue`처럼 `True`, `False`를 사용할 수 있다.

Q. Query Method 이름이 길면 왜 문제야?
A. 읽기 어렵고 변경에 취약하며 조건 조합이 늘어날수록 유지보수가 어렵다.

---

# 3. JPQL

## 3.1 JPQL Concept

### [개념]

JPQL(Java Persistence Query Language)은 Entity 객체와 Field를 기준으로 작성하는 JPA Query Language다.

SQL처럼 Table과 Column을 직접 대상으로 하지 않고 Entity와 Entity Field를 대상으로 Query를 작성한다.

---

### [핵심]

핵심 키워드:

- JPQL
- Entity Based Query
- Field Based Query
- `@Query`
- SELECT
- WHERE
- JOIN
- Fetch Join
- DTO Projection
- Named Parameter
- Entity Name
- Field Name

JPQL 기준:

```text
SQL
→ Table / Column 기준

JPQL
→ Entity / Field 기준
```

---

### [실무]

JPQL 예시:

```java
@Query("""
    select p
    from Post p
    where p.title like concat('%', :keyword, '%')
    order by p.createdAt desc
""")
List<Post> searchByKeyword(String keyword);
```

SQL과 비교:

```sql
select *
from posts p
where p.title like concat('%', ?, '%')
order by p.created_at desc;
```

SQL Foundation 연결:

```text
SQL SELECT
→ JPQL select Entity

SQL WHERE
→ JPQL where Field

SQL JOIN
→ JPQL join Association

SQL ORDER BY
→ JPQL order by Field
```

권장:

- 고정 Query가 Query Method보다 명확할 때 사용
- Table 이름이 아니라 Entity 이름 사용
- Column 이름이 아니라 Field 이름 사용
- Parameter는 Named Parameter 사용
- 복잡한 문자열 Query는 테스트로 검증
- 동적 조건이 많으면 QueryDSL 검토

주의:

- JPQL은 Native SQL이 아니다.
- Entity 이름과 Field 이름 오타에 주의한다.
- DB 함수 사용은 제약이 있을 수 있다.
- Fetch Join과 Pagination 조합은 주의한다.
- JPQL 실행 전 Auto Flush가 발생할 수 있다.

---

### [FAQ]

Q. JPQL은 뭐야?
A. Entity와 Field를 기준으로 작성하는 JPA Query Language다.

Q. JPQL은 SQL이랑 뭐가 달라?
A. SQL은 Table과 Column 기준이고 JPQL은 Entity와 Field 기준이다.

Q. JPQL에서는 Table 이름을 써?
A. 아니다. Entity 이름을 사용한다.

Q. JPQL에서는 Column 이름을 써?
A. 아니다. Entity Field 이름을 사용한다.

---

## 3.2 JPQL Join

### [개념]

JPQL Join은 Entity Association을 기준으로 연관 Entity를 Query에서 연결하는 방식이다.

JPQL Join은 SQL JOIN으로 변환되지만, 작성 기준은 Entity Association과 Field다.

---

### [핵심]

Join 종류:

- Inner Join
- Left Join
- Fetch Join
- Association Join
- Explicit Join
- Implicit Join Caution

기본 예:

```java
@Query("""
    select p
    from Post p
    join p.user u
    where u.nickname = :nickname
""")
List<Post> findByUserNickname(String nickname);
```

---

### [실무]

SQL Foundation 연결:

```text
SQL JOIN
→ JPQL Association Join

posts.user_id = users.user_id
→ join p.user u
```

Left Join 예시:

```java
@Query("""
    select p
    from Post p
    left join p.comments c
    where p.deleted = false
""")
List<Post> findPostsWithCommentJoin();
```

권장:

- Association Field 기준으로 Join 작성
- Join 목적을 명확히 함
- 조건 필터링용 Join과 Fetch Join을 구분
- 목록 Query에서 불필요한 Join 제거
- Join 결과 중복 가능성 확인
- 생성 SQL 확인

주의:

- JPQL Join은 연관 Entity를 조회 조건에 사용할 수 있지만 반드시 함께 로딩한다는 의미는 아니다.
- 연관 Entity를 함께 로딩하려면 Fetch Join을 사용한다.
- Collection Join은 Row 중복을 만들 수 있다.
- Implicit Join은 SQL 예측을 어렵게 할 수 있다.
- Fetch Join 상세는 Part06에서 다룬다.

---

### [FAQ]

Q. JPQL Join은 SQL Join과 같은 거야?
A. SQL Join으로 변환되지만 JPQL에서는 Entity Association Field 기준으로 작성한다.

Q. `join p.user u`에서 `user`는 Column 이름이야?
A. 아니다. Post Entity의 user Field 이름이다.

Q. JPQL Join을 쓰면 연관 Entity가 항상 로딩돼?
A. 아니다. 조건용 Join일 수 있다. 함께 로딩하려면 Fetch Join이 필요하다.

Q. Collection Join은 왜 주의해야 해?
A. Parent Row가 Child 수만큼 중복될 수 있어 Pagination과 결과 처리에 영향을 준다.

---

## 3.3 JPQL Parameter and Sorting

### [개념]

JPQL Parameter는 Query에 외부 값을 안전하게 전달하는 방식이다.

Sorting은 JPQL `order by` 또는 Pageable Sort로 처리할 수 있다.

---

### [핵심]

Parameter 종류:

- Named Parameter
- Positional Parameter
- `@Param`
- Dynamic Parameter
- Collection Parameter

권장:

- Named Parameter 우선
- `@Param` 명확화
- 문자열 연결로 Query 직접 조립 금지
- Sort 기준 명확화
- Pageable Sort와 JPQL order by 중복 주의

---

### [실무]

Named Parameter 예시:

```java
@Query("""
    select p
    from Post p
    where p.title like concat('%', :keyword, '%')
      and p.deleted = false
    order by p.createdAt desc
""")
List<Post> search(@Param("keyword") String keyword);
```

Collection Parameter 예시:

```java
@Query("""
    select p
    from Post p
    where p.category in :categories
""")
List<Post> findByCategories(@Param("categories") List<PostCategory> categories);
```

권장:

- Parameter 이름과 Method 인자 이름 일치
- `@Param` 사용으로 명확성 확보
- 정렬 기준은 안정적인 Column / Field 사용
- Pagination Query는 정렬 기준 필수 검토
- `createdAt desc`, `id desc` 같은 보조 정렬 검토

주의:

- 문자열 더하기로 JPQL을 만들지 않는다.
- 사용자 입력을 Query 문자열에 직접 삽입하지 않는다.
- 동적 정렬이 복잡하면 QueryDSL 검토
- `order by`가 없으면 결과 순서는 보장되지 않는다.
- Pageable Sort와 JPQL order by가 충돌하지 않도록 한다.

---

### [FAQ]

Q. JPQL Parameter는 왜 써?
A. 외부 값을 Query에 안전하고 명확하게 전달하기 위해 사용한다.

Q. Named Parameter와 Positional Parameter 중 뭐가 좋아?
A. Named Parameter가 의미가 명확해 유지보수에 유리하다.

Q. JPQL에서 문자열로 Query를 직접 이어 붙여도 돼?
A. 권장하지 않는다. Injection 위험과 유지보수 문제가 생길 수 있다.

Q. 정렬 기준은 꼭 필요해?
A. 목록과 Pagination Query에서는 안정적인 정렬 기준을 명확히 두는 것이 좋다.

---

# 4. Native Query

## 4.1 Native Query Concept

### [개념]

Native Query는 JPQL이 아니라 DB SQL을 직접 작성해 실행하는 방식이다.

Native Query는 DB Table과 Column 이름을 기준으로 작성한다.

---

### [핵심]

핵심 키워드:

- Native Query
- SQL
- Table Name
- Column Name
- DB Specific Function
- Window Function
- Recursive Query
- Performance Tuning
- Vendor Dependency
- Mapping Risk

Native Query 사용 후보:

- DB 특화 함수
- 복잡한 SQL
- 성능 튜닝 Query
- Window Function
- Recursive Query
- 특정 DB 문법
- JPQL / QueryDSL로 표현이 어려운 Query

---

### [실무]

예시:

```java
@Query(value = """
    select *
    from posts
    where title like concat('%', :keyword, '%')
    order by created_at desc
""", nativeQuery = true)
List<Post> searchNative(@Param("keyword") String keyword);
```

JPQL과 비교:

```text
JPQL
→ Entity / Field 이름 사용

Native Query
→ DB Table / Column 이름 사용
```

SQL Foundation 연결:

```text
SQL Foundation Query
→ Native Query 직접 작성

SQL Table
→ Native Query FROM

SQL Column
→ Native Query SELECT / WHERE / ORDER BY
```

권장:

- JPQL / QueryDSL로 어려운 경우에만 사용
- DB 종속성을 문서화
- Entity Mapping과 Column Alias 일치 확인
- Pagination 시 Count Query 별도 검토
- DTO Mapping이 필요하면 Projection 전략 명확화
- 테스트로 SQL 실행 검증

주의:

- DB 종속성이 증가한다.
- Table / Column 이름 변경에 취약하다.
- Entity Field 이름을 쓰면 안 된다.
- Pagination Count Query를 직접 작성해야 할 수 있다.
- Result Mapping 오류가 발생할 수 있다.
- 유지보수 비용이 JPQL보다 높을 수 있다.

---

### [FAQ]

Q. Native Query는 뭐야?
A. JPA에서 DB SQL을 직접 작성해 실행하는 Query 방식이다.

Q. Native Query는 언제 써?
A. JPQL이나 QueryDSL로 표현하기 어렵거나 DB 특화 기능이 필요한 경우에 사용한다.

Q. Native Query에서는 Entity 이름을 써?
A. 아니다. 실제 DB Table 이름과 Column 이름을 사용한다.

Q. Native Query를 많이 써도 돼?
A. 권장하지 않는다. DB 종속성과 유지보수 비용이 커질 수 있다.

---

## 4.2 Native Query Caution

### [개념]

Native Query Caution은 직접 SQL 사용으로 인해 발생하는 DB 종속성, Mapping 오류, Pagination 오류, 유지보수 비용을 검토하는 기준이다.

---

### [핵심]

주의 대상:

- DB Vendor Dependency
- Table / Column Name Coupling
- Entity Mapping Mismatch
- DTO Projection Mapping
- Count Query
- Pagination
- SQL Injection
- Column Alias
- Schema Change
- Test Coverage

---

### [실무]

Pagination Native Query 예시:

```java
@Query(
    value = """
        select *
        from posts
        where deleted = false
        order by created_at desc
    """,
    countQuery = """
        select count(*)
        from posts
        where deleted = false
    """,
    nativeQuery = true
)
Page<Post> findPostPageNative(Pageable pageable);
```

DTO Projection Native Query 주의:

```text
Native Query Result
→ Column Alias 확인
→ Projection Interface / DTO Mapping 확인
→ Type Conversion 확인
```

권장:

- Native Query에는 명확한 목적을 기록
- Pagination은 countQuery 작성
- Column Alias를 DTO Field와 맞춤
- SQL Injection 방지를 위해 Parameter Binding 사용
- DB Migration과 함께 Query 영향 검토
- 운영 DB와 동일한 Dialect 환경에서 테스트

주의:

- 문자열 직접 결합으로 SQL 작성 금지
- DB별 함수는 다른 DB로 이전 시 실패 가능
- Entity 전체 조회 Native Query는 Column 누락에 주의
- `select *`는 Schema 변경에 취약하다.
- Native Query가 많아지면 Repository 유지보수성이 낮아진다.

---

### [FAQ]

Q. Native Query Pagination에는 countQuery가 필요해?
A. Page 반환에서는 countQuery가 필요할 수 있다. 복잡한 Query는 직접 작성하는 것이 안전하다.

Q. Native Query에서 `select *`를 써도 돼?
A. 가능하지만 Schema 변경과 Mapping 문제에 취약하므로 필요한 Column을 명시하는 것이 좋다.

Q. Native Query도 Parameter Binding을 써야 해?
A. 그렇다. 사용자 입력을 문자열로 직접 연결하지 말고 Parameter Binding을 사용해야 한다.

Q. Native Query는 테스트가 필요해?
A. 필요하다. DB 종속 문법과 Mapping 오류를 확인해야 한다.

---

# 5. DTO Projection

## 5.1 DTO Projection Concept

### [개념]

DTO Projection은 Entity 전체가 아니라 필요한 Field만 조회해 DTO 또는 Interface로 반환하는 방식이다.

읽기 전용 목록, 화면 응답, 성능 최적화에 유용하다.

---

### [핵심]

핵심 키워드:

- DTO Projection
- Interface Projection
- Constructor Projection
- Read-only Query
- Select Fields
- Response DTO
- Query Performance
- Entity Loading Avoidance

사용 상황:

- 목록 화면
- Read-only 조회
- 필요한 Field가 적음
- Entity 전체 로딩 불필요
- 연관 Entity 전체가 필요 없음
- N+1 방지 후보
- API Response 전용 Query

---

### [실무]

JPQL Constructor Projection 예시:

```java
@Query("""
    select new com.example.post.PostSummaryResponse(
        p.postId,
        p.title,
        u.nickname
    )
    from Post p
    join p.user u
    where p.deleted = false
    order by p.createdAt desc
""")
List<PostSummaryResponse> findPostSummaries();
```

DTO 예시:

```java
public record PostSummaryResponse(
        Long postId,
        String title,
        String authorNickname
) {
}
```

SQL Foundation 연결:

```text
SQL SELECT specific columns
→ JPQL DTO Projection
→ 필요한 Field만 조회
→ Entity 전체 로딩 감소
```

권장:

- 목록 조회는 Projection 검토
- Read-only Query에 사용
- 수정 작업에는 Entity 조회 사용
- DTO 생성자 경로 변경에 주의
- 복잡한 Projection은 QueryDSL 검토
- Projection Query도 SQL 로그 확인

주의:

- DTO Projection 결과는 Managed Entity가 아니다.
- Dirty Checking 대상이 아니다.
- 생성자 패키지 경로가 바뀌면 JPQL 수정 필요
- 복잡한 DTO 생성은 JPQL 문자열이 길어질 수 있다.
- Projection 남용은 Query 중복을 늘릴 수 있다.

---

### [FAQ]

Q. DTO Projection은 뭐야?
A. Entity 전체가 아니라 필요한 Field만 조회해 DTO로 반환하는 방식이다.

Q. DTO Projection은 언제 써?
A. 읽기 전용 목록이나 화면 응답에서 Entity 전체가 필요하지 않을 때 사용한다.

Q. DTO Projection 결과는 Entity야?
A. 아니다. Projection 결과는 Managed Entity가 아니며 Dirty Checking 대상이 아니다.

Q. 수정 작업에도 DTO Projection을 써도 돼?
A. 수정 작업은 Entity 상태 변경이 필요하므로 Entity를 조회하는 것이 일반적이다.

---

## 5.2 Interface Projection and Class Projection

### [개념]

Interface Projection은 Getter 형태의 Interface로 필요한 Field를 조회하는 방식이다.

Class Projection은 DTO Constructor 또는 Record Constructor로 필요한 Field를 조회하는 방식이다.

---

### [핵심]

Projection 종류:

| 방식                 | 특징                   |
| -------------------- | ---------------------- |
| Interface Projection | 간단한 Field 조회      |
| Class Projection     | 명확한 DTO 생성        |
| Record Projection    | 불변 DTO 구성          |
| QueryDSL Projection  | 타입 안전한 Projection |
| Native Projection    | Alias Mapping 주의     |

---

### [실무]

Interface Projection 예시:

```java
public interface PostSummaryView {

    Long getPostId();

    String getTitle();

    String getAuthorNickname();
}
```

Repository 예시:

```java
@Query("""
    select p.postId as postId,
           p.title as title,
           u.nickname as authorNickname
    from Post p
    join p.user u
    where p.deleted = false
""")
List<PostSummaryView> findPostSummaryViews();
```

Class Projection 예시:

```java
@Query("""
    select new com.example.post.PostSummaryResponse(
        p.postId,
        p.title,
        u.nickname
    )
    from Post p
    join p.user u
""")
List<PostSummaryResponse> findPostSummaries();
```

권장:

- 간단한 조회는 Interface Projection 가능
- API Response DTO가 명확하면 Class / Record Projection 사용
- 복잡한 동적 Projection은 QueryDSL 검토
- Alias 이름과 Interface Getter 이름 일치 확인
- Projection 전용 DTO와 일반 Response DTO 역할 구분

주의:

- Interface Projection은 Alias 불일치에 주의
- Class Projection은 생성자 순서와 타입 일치 필요
- JPQL Constructor Projection은 패키지 경로를 직접 작성해야 한다.
- Native Projection은 DB Column Type 변환을 확인해야 한다.
- Projection은 변경 로직에 사용하지 않는다.

---

### [FAQ]

Q. Interface Projection은 언제 써?
A. 간단한 읽기 전용 Field 조회에 사용할 수 있다.

Q. Class Projection은 언제 써?
A. 명확한 DTO 생성이 필요하고 응답 구조가 고정되어 있을 때 적합하다.

Q. Projection Alias는 왜 중요해?
A. Interface Projection에서 Alias가 Getter 이름과 맞지 않으면 값 Mapping이 실패할 수 있다.

Q. Projection DTO를 API Response로 그대로 써도 돼?
A. 가능하지만 API 응답 역할과 Query 최적화 역할이 섞이지 않도록 프로젝트 기준을 정하는 것이 좋다.

---

# 6. Pagination Query

## 6.1 Repository Pagination

### [개념]

Repository Pagination은 `Pageable`, `Page`, `Slice`를 사용해 목록 Query 결과를 나누어 조회하는 방식이다.

Pagination은 대량 데이터 조회에서 필수적으로 검토해야 한다.

---

### [핵심]

핵심 키워드:

- Pageable
- Page
- Slice
- Sort
- Count Query
- Offset Pagination
- Keyset Pagination
- Limit
- Order By
- Stable Sort

비교:

| Type  | 특징            | 사용 상황            |
| ----- | --------------- | -------------------- |
| Page  | 전체 count 포함 | 페이지 번호 UI       |
| Slice | hasNext 중심    | 무한 스크롤 / 더보기 |
| List  | 전체 조회       | 소량 고정 데이터     |

---

### [실무]

Page 예시:

```java
Page<Post> findByDeletedFalse(Pageable pageable);
```

Slice 예시:

```java
Slice<Comment> findByPost_PostIdOrderByCreatedAtDesc(Long postId, Pageable pageable);
```

Service 예시:

```java
@Transactional(readOnly = true)
public Slice<CommentResponse> getComments(Long postId, Pageable pageable) {
    return commentRepository.findByPost_PostIdOrderByCreatedAtDesc(postId, pageable)
            .map(CommentResponse::from);
}
```

SQL Foundation 연결:

```text
SQL LIMIT / OFFSET
→ Pageable

SQL COUNT
→ Page

No Count, hasNext
→ Slice

SQL ORDER BY
→ Sort / OrderBy
```

권장:

- 대량 목록은 Pagination 적용
- 전체 페이지 수가 필요하면 Page
- 무한 스크롤 / 더보기는 Slice
- 정렬 기준은 안정적으로 설정
- `createdAt desc`, `id desc` 보조 정렬 검토
- Collection Fetch Join + Pagination 조합 주의

주의:

- Page는 Count Query 비용 발생
- Offset Pagination은 뒤 페이지로 갈수록 비용 증가 가능
- 정렬 기준이 불안정하면 중복 / 누락이 생길 수 있다.
- `Page<Entity>`를 그대로 API Response로 노출하지 않는다.
- Pagination Query도 N+1 가능성을 검토해야 한다.

---

### [FAQ]

Q. Pageable은 뭐야?
A. 페이지 크기, 페이지 번호, 정렬 정보를 Repository Query에 전달하는 객체다.

Q. Page와 Slice 중 뭐가 좋아?
A. 전체 페이지 수가 필요하면 Page, 무한 스크롤이나 더보기면 Slice가 적합하다.

Q. Page는 왜 비용이 더 들 수 있어?
A. 전체 개수를 구하기 위한 Count Query가 추가로 실행될 수 있기 때문이다.

Q. Pagination에서 정렬 기준이 왜 중요해?
A. 정렬 기준이 불안정하면 페이지 간 중복이나 누락이 발생할 수 있다.

---

## 6.2 Pagination Query Caution

### [개념]

Pagination Query Caution은 JPA Pagination에서 Count Query, Fetch Join, Collection Join, Offset 비용, 정렬 안정성을 검토하는 기준이다.

---

### [핵심]

주의 대상:

- Count Query 비용
- Collection Fetch Join
- OneToMany Join 중복
- Offset Pagination 비용
- Sort 기준 불안정
- N+1 Problem
- DTO Projection 필요성
- Page Entity 직접 반환

---

### [실무]

비권장 흐름:

```text
Post Page 조회
→ Post.comments Collection Fetch Join
→ Row 중복
→ Pagination 불안정
→ Memory Pagination 가능성
```

권장 후보:

```text
목록 API
→ DTO Projection

Parent 목록 + Child Count
→ Projection / Subquery / 별도 Count Query

Child 목록
→ Child Repository에서 Parent ID 조건으로 Slice 조회

무한 스크롤
→ Slice / Keyset Pagination 검토
```

Page DTO 변환 예시:

```java
@Transactional(readOnly = true)
public Page<PostResponse> getPosts(Pageable pageable) {
    return postRepository.findByDeletedFalse(pageable)
            .map(PostResponse::from);
}
```

권장:

- Entity Page를 DTO Page로 변환
- Collection Fetch Join과 Pageable 조합 피하기
- Count Query가 복잡하면 countQuery 분리
- Offset 비용이 크면 Keyset Pagination 검토
- 목록 Query는 Projection 검토
- SQL 로그로 Count Query와 Main Query 확인

주의:

- `Page.map()`은 DTO 변환 중 Lazy Loading을 발생시킬 수 있다.
- DTO 변환에서 연관 Entity 접근 시 N+1 가능
- `distinct`만으로 Collection Pagination 문제가 해결되지 않을 수 있다.
- Pageable Sort가 JPQL order by와 충돌하지 않도록 주의
- Native Query Page는 countQuery 확인 필요

---

### [FAQ]

Q. Collection Fetch Join과 Pagination을 같이 쓰면 왜 위험해?
A. Parent Row가 Child 수만큼 중복되어 DB Pagination이 기대대로 동작하지 않을 수 있다.

Q. Page Entity를 그대로 반환해도 돼?
A. 권장하지 않는다. DTO로 변환해 API 응답 구조를 분리하는 것이 좋다.

Q. Page.map으로 DTO 변환하면 안전해?
A. DTO 변환 중 Lazy Field 접근이 있으면 N+1이 발생할 수 있어 Query 전략을 함께 검토해야 한다.

Q. Offset Pagination이 느려지면 어떻게 해?
A. 조건에 따라 Keyset Pagination이나 Cursor 기반 조회를 검토할 수 있다.

---

# 7. QueryDSL Decision Rule

## 7.1 QueryDSL Transition Criteria

### [개념]

QueryDSL은 타입 안전한 동적 Query를 작성하기 위한 도구다.

JPA Query Method나 JPQL이 복잡해질 때 QueryDSL을 검토한다.

---

### [핵심]

Query 전략 선택:

```text
단순 조건
→ Query Method

고정 Query
→ JPQL

동적 조건 많음
→ QueryDSL

DB 특화 기능 필요
→ Native Query
```

QueryDSL 검토 상황:

- 동적 검색 조건
- optional filter 다수
- 복잡한 where 조합
- 복잡한 정렬
- Projection
- Join 조건 제어
- Query Method 이름 과다
- JPQL 문자열 유지보수 어려움

---

### [실무]

검색 조건 예시:

```text
keyword optional
region optional
category optional
startDate optional
endDate optional
sort optional
```

Query Method로 억지 작성하면:

```text
findByTitleContainingAndRegionCodeAndCategoryAndStartDateGreaterThanEqualAndEndDateLessThanEqual...
→ 유지보수 어려움
→ 조건 optional 처리 어려움
```

QueryDSL 전환 기준:

```text
조건이 1~2개 고정
→ Query Method

고정 Query + Join 필요
→ JPQL

조건이 Optional로 조합됨
→ QueryDSL

DB 함수 / 특수 SQL 필요
→ Native Query
```

권장:

- 동적 검색은 QueryDSL 우선 검토
- Query Method가 길어지면 중단
- JPQL 문자열 조합으로 동적 Query 만들지 않음
- Projection이 복잡하면 QueryDSL Projection 검토
- QueryDSL 상세 문법은 QueryDSL Practical Domain Rules 참조

주의:

- QueryDSL은 JPA 대체가 아니다.
- QueryDSL은 Entity Mapping 문제를 해결하지 않는다.
- 성능 문제는 생성 SQL 기준으로 검토한다.
- QueryDSL로 작성해도 N+1 가능성은 별도 검토한다.
- QueryDSL 적용은 프로젝트 설정과 QClass 생성이 필요하다.

---

### [FAQ]

Q. QueryDSL은 언제 써?
A. 동적 검색 조건이 많거나 JPQL / Query Method 유지보수가 어려울 때 사용한다.

Q. QueryDSL은 JPA를 대체해?
A. 아니다. JPA 기반 Query 작성을 타입 안전하게 도와주는 도구다.

Q. Query Method가 길어지면 QueryDSL로 가야 해?
A. 동적 조건이 많거나 Method 이름이 과도하게 길어지면 QueryDSL을 검토하는 것이 좋다.

Q. QueryDSL을 쓰면 성능 문제가 자동으로 해결돼?
A. 아니다. 생성 SQL, Join, Index, N+1 문제는 별도로 검토해야 한다.

---

## 7.2 Query Strategy Comparison

### [개념]

Query Strategy Comparison은 Query Method, JPQL, QueryDSL, Native Query 중 어떤 방식을 선택할지 비교하는 기준이다.

---

### [핵심]

비교:

| 방식         | 장점                  | 단점                 | 사용 상황     |
| ------------ | --------------------- | -------------------- | ------------- |
| Query Method | 빠르고 간단           | 복잡하면 이름 길어짐 | 단순 조건     |
| JPQL         | Entity 기준 명확      | 문자열 Query         | 고정 Query    |
| QueryDSL     | 타입 안전, 동적 Query | 설정 필요            | 동적 조건     |
| Native Query | SQL 자유도 높음       | DB 종속              | DB 특화 Query |

선택 Flow:

```text
Query Requirement 확인
→ 조건 개수 확인
→ 동적 여부 확인
→ Join 복잡도 확인
→ Projection 필요 여부 확인
→ DB 특화 기능 필요 여부 확인
→ Query Strategy 선택
```

---

### [실무]

예시 판단:

```text
이메일로 User 조회
→ Query Method

게시글 제목 검색 고정 Query
→ Query Method 또는 JPQL

게시글 + 작성자 닉네임 목록 Projection
→ JPQL DTO Projection 또는 QueryDSL

축제 검색 조건 keyword / region / theme / date optional
→ QueryDSL

Window Function Ranking
→ Native Query
```

권장:

- 단순한 것은 단순하게 유지
- Query Method 남용 금지
- JPQL 문자열 동적 조립 금지
- QueryDSL은 동적 Query에서 적극 검토
- Native Query는 목적이 명확할 때만 사용
- 어떤 전략이든 SQL 로그 확인

주의:

- Query 전략 선택은 코드 가독성과 성능 모두에 영향을 준다.
- QueryDSL을 모든 Query에 무조건 쓰지 않는다.
- Native Query는 DB 변경에 취약하다.
- Projection Query와 Entity Query를 역할별로 구분한다.
- 조회 Query와 수정 Command Query를 분리해서 생각한다.

---

### [FAQ]

Q. Query Method, JPQL, QueryDSL 중 뭐가 제일 좋아?
A. 상황에 따라 다르다. 단순 조건은 Query Method, 고정 Query는 JPQL, 동적 조건은 QueryDSL이 적합하다.

Q. Native Query는 언제 선택해?
A. DB 특화 함수나 JPQL / QueryDSL로 표현하기 어려운 SQL이 필요할 때 선택한다.

Q. 모든 Query를 QueryDSL로 통일해도 돼?
A. 가능하지만 단순 Query까지 복잡하게 만들 수 있으므로 필요에 따라 선택하는 것이 좋다.

Q. Query 전략 선택 후 무엇을 확인해야 해?
A. 생성 SQL, 실행 Query 수, Index 사용 가능성, N+1 여부, Pagination 비용을 확인해야 한다.

---

# 8. Repository Query Review

## 8.1 Repository Query Checklist

### [개념]

Repository Query Checklist는 Repository Method, Query Method, JPQL, Native Query, Projection, Pagination이 적절한지 검수하는 기준이다.

Review Agent는 Query가 Entity Field 기준인지, SQL이 예측 가능한지, 성능 문제가 없는지 확인해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] Repository가 JpaRepository<Entity, IdType>을 올바르게 상속하는가?
- [ ] Repository에 비즈니스 로직이 들어가지 않았는가?
- [ ] Query Method가 Entity Field 이름 기준으로 작성되었는가?
- [ ] Query Method 이름이 과도하게 길지 않은가?
- [ ] 단건 조회에 Optional을 사용하는가?
- [ ] 존재 여부 조회에 existsBy를 사용하는가?
- [ ] 대량 목록에 List를 남용하지 않는가?
- [ ] Pagination이 필요한 목록에 Page 또는 Slice를 사용하는가?
- [ ] Page와 Slice 선택 기준이 적절한가?
- [ ] JPQL에서 Entity 이름과 Field 이름을 사용하는가?
- [ ] JPQL에서 Table / Column 이름을 사용하지 않았는가?
- [ ] Native Query에서 Table / Column 이름을 정확히 사용하는가?
- [ ] Native Query 사용 이유가 명확한가?
- [ ] Native Query Pagination에 countQuery가 필요한가?
- [ ] DTO Projection이 필요한 목록 조회인가?
- [ ] Projection Alias / Constructor가 정확한가?
- [ ] QueryDSL 전환이 필요한 동적 조건인가?
- [ ] Collection Join과 Pagination 조합을 피했는가?
- [ ] DTO 변환 중 Lazy Loading / N+1 가능성을 검토했는가?
- [ ] SQL 로그로 생성 Query를 확인했는가?
```

---

### [실무]

Review Flow:

```text
Repository Method 확인
→ Query Method / JPQL / Native Query 구분
→ Return Type 확인
→ Entity Field / DB Column 기준 확인
→ Pagination 필요성 확인
→ Projection 필요성 확인
→ Join / Fetch 전략 확인
→ N+1 가능성 확인
→ QueryDSL 전환 필요성 확인
→ SQL 로그 확인
```

Common Review Findings:

```text
문제: findAll 후 Java Stream 필터링
위험: DB Filtering 미사용, 대량 데이터 성능 문제
해결: Repository Query Method / JPQL / QueryDSL 사용

문제: JPQL에서 posts 테이블 이름 사용
위험: Query Parsing Error
해결: Entity 이름 Post 사용

문제: Query Method 이름 과도
위험: 가독성 / 유지보수 저하
해결: JPQL 또는 QueryDSL 전환

문제: Page 사용하지만 countQuery 비용 큼
위험: 목록 API 성능 저하
해결: Slice 또는 countQuery 최적화 검토

문제: Native Query에서 countQuery 없음
위험: Pagination 오류
해결: countQuery 명시
```

---

### [FAQ]

Q. Repository Query 검수에서 가장 먼저 확인할 것은 뭐야?
A. Query Method, JPQL, Native Query가 각각 올바른 이름 기준을 사용하는지 확인한다.

Q. JPQL 오류에서 자주 보는 실수는 뭐야?
A. Entity / Field 이름 대신 DB Table / Column 이름을 사용하는 실수다.

Q. Repository Method 이름이 너무 길면 어떻게 해?
A. JPQL 또는 QueryDSL로 분리하는 것이 좋다.

Q. Query Review에서 SQL 로그는 왜 중요해?
A. 실제 실행 Query, Join, Count Query, N+1 여부를 확인할 수 있기 때문이다.

---

# 9. Common Mistakes

## 9.1 Repository and Query Common Mistakes

### [개념]

Repository and Query Common Mistakes는 Repository 책임, Query Method, JPQL, Native Query, Projection, Pagination에서 자주 발생하는 오류다.

---

### [핵심]

자주 발생하는 실수:

- Repository에 비즈니스 로직 작성
- 모든 데이터를 `findAll`로 조회 후 Java Stream 필터링
- Query Method를 DB Column 이름 기준으로 작성
- Query Method 이름 과도하게 길어짐
- Optional을 Controller까지 그대로 전달
- Page / Slice 기준 없이 List 사용
- JPQL에서 Table 이름 사용
- JPQL에서 Column 이름 사용
- Native Query에서 Entity Field 이름 사용
- Native Query 사용 이유 불명확
- Native Query Pagination countQuery 누락
- Projection Constructor 경로 오류
- Interface Projection Alias 불일치
- DTO Projection 결과를 Entity처럼 수정
- Page Entity를 API Response로 직접 반환
- DTO 변환 중 Lazy Loading으로 N+1 발생
- Collection Join과 Pagination 무분별 조합
- 동적 Query를 JPQL 문자열 조합으로 작성
- QueryDSL이 필요한 상황에서 Query Method 남용
- SQL 로그 확인 안 함

---

### [실무]

Anti Pattern 예시:

```java
@Transactional(readOnly = true)
public List<PostResponse> search(String keyword) {
    return postRepository.findAll().stream()
            .filter(post -> post.getTitle().contains(keyword))
            .map(PostResponse::from)
            .toList();
}
```

문제:

```text
DB Filtering 미사용
전체 Entity Loading
대량 데이터 성능 문제
DTO 변환 중 N+1 가능
```

개선:

```java
List<Post> findByTitleContainingAndDeletedFalseOrderByCreatedAtDesc(String keyword);
```

Anti Pattern 예시:

```java
@Query("""
    select *
    from posts
    where created_at > :date
""")
List<Post> findRecentPosts(LocalDateTime date);
```

문제:

```text
JPQL에서 SQL 문법 사용
Table / Column 이름 사용
Entity / Field 기준 아님
```

개선:

```java
@Query("""
    select p
    from Post p
    where p.createdAt > :date
""")
List<Post> findRecentPosts(LocalDateTime date);
```

Anti Pattern 예시:

```java
String jpql = "select p from Post p where 1=1 ";
if (keyword != null) {
    jpql += " and p.title like '%" + keyword + "%'";
}
```

문제:

```text
문자열 조합 Query
Injection 위험
유지보수 어려움
Parameter Binding 누락
```

개선 후보:

```text
동적 조건 많음
→ QueryDSL 사용
```

Review 기준:

```text
Query Requirement
→ Query Strategy 선택
→ Return Type 확인
→ Pagination 확인
→ Projection 확인
→ SQL 로그 확인
```

---

### [FAQ]

Q. Repository에서 가장 흔한 실수는 뭐야?
A. Repository에 비즈니스 로직을 넣거나 findAll 후 Java Stream으로 필터링하는 것이다.

Q. Query Method에서 가장 흔한 실수는 뭐야?
A. Entity Field 이름이 아니라 DB Column 이름 기준으로 작성하는 것이다.

Q. JPQL에서 가장 흔한 실수는 뭐야?
A. Entity / Field 이름 대신 Table / Column 이름을 사용하는 것이다.

Q. Native Query에서 가장 흔한 실수는 뭐야?
A. 사용 이유 없이 Native Query를 남용하거나 Pagination countQuery를 누락하는 것이다.

---

# 10. Part05 Final Goal

## 10.1 Agent Output Goal

### [개념]

JPA Advanced Part05의 최종 목적은 Agent가 Repository, Query Method, JPQL, Native Query, DTO Projection, Pagination, QueryDSL 전환 기준을 기반으로 안정적인 조회 계층을 설계하도록 만드는 것이다.

Part05는 SQL Foundation의 SELECT, WHERE, JOIN, Pagination, Backend Integration 기준과 JPA Repository Query 전략을 연결한다.

---

### [핵심]

Agent가 수행해야 할 작업:

- Repository 책임 구분
- JpaRepository 기본 구조 작성
- Query Method 작성
- Query Method Return Type 선택
- Optional / List / Page / Slice 구분
- JPQL 작성 기준 판단
- JPQL Entity / Field 이름 사용
- JPQL Join 사용 기준 판단
- Native Query 사용 여부 판단
- Native Query DB 종속성 검토
- DTO Projection 적용 판단
- Interface / Class Projection 구분
- Repository Pagination 설계
- Page / Slice 선택
- QueryDSL 전환 기준 판단
- Query Strategy 비교
- Repository Query Checklist 적용
- Query Anti Pattern 탐지

---

### [실무]

Agent 작업 흐름:

```text
User Query Requirement
→ Identify Entity
→ Decide Query Strategy
→ Query Method / JPQL / QueryDSL / Native Query 선택
→ Decide Return Type
→ Apply Pagination if Needed
→ Apply Projection if Needed
→ Check Join Requirement
→ Check N+1 Risk
→ Verify Generated SQL
→ Return Repository Output
```

Query Strategy Flow:

```text
단순 조건
→ Query Method

고정 Query + Join
→ JPQL

동적 검색 조건
→ QueryDSL

DB 특화 SQL
→ Native Query

읽기 전용 목록
→ DTO Projection 검토

대량 목록
→ Page / Slice 적용
```

Part05 이후 연결:

```text
Part05 Repository / JPQL / Native Query
→ Part06 Fetch Strategy / Fetch Join / N+1
→ Part07 Transaction / Cascade / Auditing / Pagination
→ Part08 Backend Integration / Troubleshooting / Anti Pattern
```

---

### [FAQ]

Q. JPA Advanced Part05의 목적은 뭐야?
A. Agent가 Repository와 Query 전략을 올바르게 선택하고 JPQL, Native Query, Projection, Pagination을 안정적으로 설계하도록 만드는 것이다.

Q. Part05에서 가장 중요한 기준은 뭐야?
A. Repository 책임 분리, Query Method Field 이름 기준, JPQL Entity 기준, Native Query 제한 사용, Projection과 Pagination 검토다.

Q. Part05는 SQL Foundation 어느 부분과 연결돼?
A. SQL Part01 SELECT, SQL Part02 WHERE / JOIN, SQL Part04 Pagination, SQL Part05 Backend Integration과 연결된다.

Q. Part05 다음에는 무엇을 다뤄?
A. Part06에서 Fetch Strategy, Lazy Loading, Fetch Join, N+1 Problem, LazyInitializationException을 다룬다.

---

# Retrieval Queries

### [FAQ]

Q. Repository는 뭐야?
A. Entity 조회, 저장, 삭제 같은 Data Access를 담당하는 계층이다.

Q. Repository에 비즈니스 로직을 넣어도 돼?
A. 권장하지 않는다. Repository는 Data Access 중심이고 비즈니스 흐름은 Service에서 처리한다.

Q. `JpaRepository<Post, Long>`에서 Long은 뭐야?
A. Post Entity의 Primary Key Type이다.

Q. `findById`는 왜 Optional을 반환해?
A. 해당 ID의 Entity가 없을 수 있기 때문이다.

Q. `save`는 insert야 update야?
A. 신규 Entity면 저장이고 Detached Entity면 merge처럼 동작할 수 있다. 수정은 Dirty Checking을 우선 검토한다.

Q. Query Method는 뭐야?
A. Repository Method 이름을 기반으로 Spring Data JPA가 Query를 생성하는 방식이다.

Q. Query Method는 Column 이름 기준이야?
A. 아니다. Entity Field 이름 기준이다.

Q. Query Method는 언제 쓰는 게 좋아?
A. 조건이 단순하고 Method 이름이 과도하게 길어지지 않을 때 적합하다.

Q. Query Method가 너무 길어지면 어떻게 해?
A. JPQL이나 QueryDSL로 분리하는 것이 좋다.

Q. 단건 조회는 어떤 Return Type이 좋아?
A. 없을 수 있는 단건 조회는 `Optional<Entity>`가 적합하다.

Q. Page와 Slice는 뭐가 달라?
A. Page는 전체 count를 포함하고 Slice는 다음 페이지 존재 여부 중심이다.

Q. 무한 스크롤에는 Page와 Slice 중 뭐가 좋아?
A. 전체 페이지 수가 필요 없으면 Slice가 적합할 수 있다.

Q. List 조회는 언제 써?
A. 데이터 수가 작고 고정적이거나 Pagination이 필요 없는 경우에 사용한다.

Q. Query Method 이름은 어떤 기준으로 작성해?
A. Entity Field 이름과 Spring Data JPA 키워드를 조합해서 작성한다.

Q. 연관 Entity Field 조건은 어떻게 써?
A. `findByUser_UserId`처럼 `_`로 Field 경로를 표현할 수 있다.

Q. Boolean 조건은 어떻게 표현해?
A. `findByDeletedFalse`, `findByActiveTrue`처럼 `True`, `False`를 사용할 수 있다.

Q. JPQL은 뭐야?
A. Entity와 Field를 기준으로 작성하는 JPA Query Language다.

Q. JPQL은 SQL이랑 뭐가 달라?
A. SQL은 Table과 Column 기준이고 JPQL은 Entity와 Field 기준이다.

Q. JPQL에서는 Table 이름을 써?
A. 아니다. Entity 이름을 사용한다.

Q. JPQL에서는 Column 이름을 써?
A. 아니다. Entity Field 이름을 사용한다.

Q. JPQL Join은 SQL Join과 같은 거야?
A. SQL Join으로 변환되지만 JPQL에서는 Entity Association Field 기준으로 작성한다.

Q. `join p.user u`에서 `user`는 Column 이름이야?
A. 아니다. Post Entity의 user Field 이름이다.

Q. JPQL Join을 쓰면 연관 Entity가 항상 로딩돼?
A. 아니다. 조건용 Join일 수 있다. 함께 로딩하려면 Fetch Join이 필요하다.

Q. Collection Join은 왜 주의해야 해?
A. Parent Row가 Child 수만큼 중복될 수 있어 Pagination과 결과 처리에 영향을 준다.

Q. JPQL Parameter는 왜 써?
A. 외부 값을 Query에 안전하고 명확하게 전달하기 위해 사용한다.

Q. Named Parameter와 Positional Parameter 중 뭐가 좋아?
A. Named Parameter가 의미가 명확해 유지보수에 유리하다.

Q. JPQL에서 문자열로 Query를 직접 이어 붙여도 돼?
A. 권장하지 않는다. Injection 위험과 유지보수 문제가 생길 수 있다.

Q. Native Query는 뭐야?
A. JPA에서 DB SQL을 직접 작성해 실행하는 Query 방식이다.

Q. Native Query는 언제 써?
A. JPQL이나 QueryDSL로 표현하기 어렵거나 DB 특화 기능이 필요한 경우에 사용한다.

Q. Native Query에서는 Entity 이름을 써?
A. 아니다. 실제 DB Table 이름과 Column 이름을 사용한다.

Q. Native Query를 많이 써도 돼?
A. 권장하지 않는다. DB 종속성과 유지보수 비용이 커질 수 있다.

Q. Native Query Pagination에는 countQuery가 필요해?
A. Page 반환에서는 countQuery가 필요할 수 있다. 복잡한 Query는 직접 작성하는 것이 안전하다.

Q. Native Query에서 `select *`를 써도 돼?
A. 가능하지만 Schema 변경과 Mapping 문제에 취약하므로 필요한 Column을 명시하는 것이 좋다.

Q. Native Query도 Parameter Binding을 써야 해?
A. 그렇다. 사용자 입력을 문자열로 직접 연결하지 말고 Parameter Binding을 사용해야 한다.

Q. DTO Projection은 뭐야?
A. Entity 전체가 아니라 필요한 Field만 조회해 DTO로 반환하는 방식이다.

Q. DTO Projection은 언제 써?
A. 읽기 전용 목록이나 화면 응답에서 Entity 전체가 필요하지 않을 때 사용한다.

Q. DTO Projection 결과는 Entity야?
A. 아니다. Projection 결과는 Managed Entity가 아니며 Dirty Checking 대상이 아니다.

Q. 수정 작업에도 DTO Projection을 써도 돼?
A. 수정 작업은 Entity 상태 변경이 필요하므로 Entity를 조회하는 것이 일반적이다.

Q. Interface Projection은 언제 써?
A. 간단한 읽기 전용 Field 조회에 사용할 수 있다.

Q. Class Projection은 언제 써?
A. 명확한 DTO 생성이 필요하고 응답 구조가 고정되어 있을 때 적합하다.

Q. Projection Alias는 왜 중요해?
A. Interface Projection에서 Alias가 Getter 이름과 맞지 않으면 값 Mapping이 실패할 수 있다.

Q. Pageable은 뭐야?
A. 페이지 크기, 페이지 번호, 정렬 정보를 Repository Query에 전달하는 객체다.

Q. Page는 왜 비용이 더 들 수 있어?
A. 전체 개수를 구하기 위한 Count Query가 추가로 실행될 수 있기 때문이다.

Q. Pagination에서 정렬 기준이 왜 중요해?
A. 정렬 기준이 불안정하면 페이지 간 중복이나 누락이 발생할 수 있다.

Q. Collection Fetch Join과 Pagination을 같이 쓰면 왜 위험해?
A. Parent Row가 Child 수만큼 중복되어 DB Pagination이 기대대로 동작하지 않을 수 있다.

Q. Page Entity를 그대로 반환해도 돼?
A. 권장하지 않는다. DTO로 변환해 API 응답 구조를 분리하는 것이 좋다.

Q. Page.map으로 DTO 변환하면 안전해?
A. DTO 변환 중 Lazy Field 접근이 있으면 N+1이 발생할 수 있어 Query 전략을 함께 검토해야 한다.

Q. QueryDSL은 언제 써?
A. 동적 검색 조건이 많거나 JPQL / Query Method 유지보수가 어려울 때 사용한다.

Q. QueryDSL은 JPA를 대체해?
A. 아니다. JPA 기반 Query 작성을 타입 안전하게 도와주는 도구다.

Q. QueryDSL을 쓰면 성능 문제가 자동으로 해결돼?
A. 아니다. 생성 SQL, Join, Index, N+1 문제는 별도로 검토해야 한다.

Q. Query Method, JPQL, QueryDSL 중 뭐가 제일 좋아?
A. 상황에 따라 다르다. 단순 조건은 Query Method, 고정 Query는 JPQL, 동적 조건은 QueryDSL이 적합하다.

Q. Native Query는 언제 선택해?
A. DB 특화 함수나 JPQL / QueryDSL로 표현하기 어려운 SQL이 필요할 때 선택한다.

Q. 모든 Query를 QueryDSL로 통일해도 돼?
A. 가능하지만 단순 Query까지 복잡하게 만들 수 있으므로 필요에 따라 선택하는 것이 좋다.

Q. Repository Query 검수에서 가장 먼저 확인할 것은 뭐야?
A. Query Method, JPQL, Native Query가 각각 올바른 이름 기준을 사용하는지 확인한다.

Q. JPQL 오류에서 자주 보는 실수는 뭐야?
A. Entity / Field 이름 대신 DB Table / Column 이름을 사용하는 실수다.

Q. Repository에서 가장 흔한 실수는 뭐야?
A. Repository에 비즈니스 로직을 넣거나 findAll 후 Java Stream으로 필터링하는 것이다.

Q. Query Method에서 가장 흔한 실수는 뭐야?
A. Entity Field 이름이 아니라 DB Column 이름 기준으로 작성하는 것이다.

Q. Native Query에서 가장 흔한 실수는 뭐야?
A. 사용 이유 없이 Native Query를 남용하거나 Pagination countQuery를 누락하는 것이다.

Q. JPA Part05에서 가장 중요한 기준은 뭐야?
A. Repository 책임 분리, Query Method Field 이름 기준, JPQL Entity 기준, Native Query 제한 사용, Projection과 Pagination 검토다.

Q. JPA Part05 다음에는 무엇을 다뤄?
A. Part06에서 Fetch Strategy, Lazy Loading, Fetch Join, N+1 Problem, LazyInitializationException을 다룬다.
