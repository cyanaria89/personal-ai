# JPA Advanced Part01 — ORM and Entity Mapping

---

# 1. ORM Concept

## 1.1 ORM Purpose

### [개념]

ORM(Object Relational Mapping)은 Java Object와 Relational Database Table을 Mapping하는 기술이다.

JPA는 Java ORM 표준이고, Hibernate는 대표적인 JPA 구현체다.

ORM의 목적은 SQL을 완전히 제거하는 것이 아니라, Application의 Entity 상태와 DB Row 저장을 연결하는 것이다.

---

### [핵심]

핵심 키워드:

- ORM
- Object Relational Mapping
- JPA
- Hibernate
- Entity
- Table
- Row
- Column
- Persistence Context
- SQL Generation
- Entity Mapping
- Table Mapping

ORM 기준:

- Java Object ↔ DB Table Mapping
- Entity Field ↔ Table Column Mapping
- Entity Reference ↔ Foreign Key Mapping
- Entity State ↔ SQL INSERT / UPDATE / DELETE 연결
- Repository ↔ Data Access 추상화
- Persistence Context ↔ Entity 상태 관리

---

### [실무]

2026 실무 기준에서 JPA는 SQL을 모르는 상태로 사용하는 기술이 아니다.

JPA 개발 흐름:

```text
Requirement
→ DB Table Relationship 이해
→ Entity Mapping 설계
→ Primary Key / Foreign Key 확인
→ Repository Query 설계
→ Service Transaction 적용
→ SQL 로그 확인
→ N+1 / Pagination / Constraint 검토
```

SQL Foundation 연결:

```text
SQL Part01 SELECT / Table Relationship
→ JPA Entity Mapping / Table Mapping

SQL Part02 JOIN / Filtering
→ JPA Association / JPQL / Fetch Join

SQL Part03 INSERT / UPDATE / DELETE
→ JPA persist / Dirty Checking / remove

SQL Part04 Transaction / Constraint
→ JPA Transaction Boundary / Column Constraint

SQL Part05 Backend Integration
→ JPA Repository / Service / DTO Mapping
```

주의:

- JPA는 SQL을 생성한다.
- SQL 로그 확인 없는 JPA 사용은 위험하다.
- Entity 설계는 DB Table 구조와 무관하지 않다.
- 객체 그래프 탐색은 실제 SQL 조회로 이어질 수 있다.
- JPA 편의성보다 명확한 Mapping과 Query 전략이 중요하다.

---

### [FAQ]

Q. ORM은 뭐야?
A. Java Object와 Relational Database Table을 Mapping해서 객체 상태와 DB 저장을 연결하는 기술이다.

Q. JPA는 SQL을 안 써도 되는 기술이야?
A. 아니다. SQL을 직접 덜 작성하게 해주지만 내부적으로 SQL이 생성되므로 SQL 동작을 이해해야 한다.

Q. Hibernate는 JPA랑 같은 거야?
A. 아니다. JPA는 표준 인터페이스이고 Hibernate는 JPA 구현체다.

Q. JPA를 쓰면 SQL Foundation 문서가 필요 없어?
A. 아니다. JPA가 생성하는 SQL, JOIN, Constraint, Transaction, Pagination을 이해하려면 SQL Foundation이 필요하다.

---

## 1.2 JPA and Hibernate

### [개념]

JPA(Java Persistence API)는 Java ORM 표준 명세다.

Hibernate는 JPA 표준을 구현한 ORM Framework다.

Spring Data JPA는 JPA 사용을 편하게 해주는 Repository 추상화다.

---

### [핵심]

구분:

| 용어                | 역할              |
| ------------------- | ----------------- |
| JPA                 | Java ORM 표준     |
| Hibernate           | JPA 구현체        |
| Spring Data JPA     | Repository 추상화 |
| EntityManager       | JPA 핵심 API      |
| Persistence Context | Entity 관리 공간  |
| Repository          | Data Access Layer |

관계:

```text
Spring Data JPA
→ JPA
→ Hibernate
→ JDBC
→ Database
```

---

### [실무]

Spring Boot 3.x 기준:

- `jakarta.persistence.*` 사용
- Hibernate 6.x 계열 사용 가능
- Repository는 `JpaRepository` 기반 사용
- EntityManager 직접 사용은 제한적으로 사용
- 일반 CRUD와 단순 Query는 Repository 사용
- 복잡한 동적 Query는 QueryDSL 검토
- DB 특화 Query는 Native Query 제한적 사용

권장 흐름:

```text
Controller
→ Service
→ Repository
→ JPA
→ Hibernate
→ SQL
→ Database
```

주의:

- Spring Data JPA는 JPA 자체가 아니다.
- Hibernate 전용 기능은 JPA 표준과 구분해야 한다.
- JPA 표준 기능 우선 사용 후 필요 시 Hibernate 기능을 검토한다.
- Repository가 비즈니스 로직을 담당하지 않는다.

---

### [FAQ]

Q. Spring Data JPA는 JPA야?
A. 아니다. Spring Data JPA는 JPA Repository 사용을 편하게 해주는 Spring 추상화다.

Q. Hibernate 기능을 마음대로 써도 돼?
A. 가능하지만 JPA 표준과 Hibernate 전용 기능을 구분해야 유지보수가 쉽다.

Q. EntityManager를 직접 써야 해?
A. 대부분은 Repository로 충분하다. 복잡한 영속성 제어나 특수한 상황에서 EntityManager를 제한적으로 사용한다.

Q. Spring Boot 3에서는 javax.persistence를 써?
A. Spring Boot 3 기준에서는 Jakarta 전환으로 `jakarta.persistence` 패키지를 사용한다.

---

# 2. Entity Concept

## 2.1 Entity Definition

### [개념]

Entity는 DB Table과 Mapping되는 Persistence Model이다.

Entity는 API Request / Response 객체가 아니다.

Entity는 DB Row를 Java Object로 표현하고, JPA Persistence Context가 상태를 관리하는 객체다.

---

### [핵심]

Entity 핵심 요소:

- `@Entity`
- `@Table`
- `@Id`
- `@GeneratedValue`
- `@Column`
- Field
- Constructor
- Business Method
- Association
- Persistence Context
- Managed Entity
- Dirty Checking

Entity 역할:

- Table Mapping
- Column Mapping
- Primary Key Mapping
- Foreign Key Association Mapping
- Entity State Management
- Dirty Checking 대상
- Repository 조회 대상

---

### [실무]

Entity 설계 기준:

```text
DB Table 확인
→ Primary Key 확인
→ Column 확인
→ Constraint 확인
→ Foreign Key 확인
→ Entity Field 설계
→ Association 필요 여부 결정
→ DTO 분리
```

Entity는 아래 목적에 사용한다.

- DB 저장 구조 표현
- Persistence Context 관리 대상
- Transaction 안에서 상태 변경
- Repository Query 대상
- Association Mapping 기준

Entity는 아래 목적으로 사용하지 않는다.

- API RequestBody 직접 수신
- API Response 직접 반환
- 화면 전용 필드 저장
- 임시 계산 결과 보관
- Controller Layer 데이터 전달 객체

주의:

- Entity 변경은 DB Schema와 연결된다.
- Entity 노출은 API 스펙 노출로 이어질 수 있다.
- Entity에 화면 전용 요구사항을 섞으면 Persistence Model이 오염된다.
- Entity 필드 추가는 Column 추가 가능성과 함께 검토한다.

---

### [FAQ]

Q. Entity는 뭐야?
A. DB Table과 Mapping되는 Persistence Model이며 JPA가 상태를 관리하는 객체다.

Q. Entity는 DTO랑 같아?
A. 아니다. Entity는 DB 저장 모델이고 DTO는 API 입출력 또는 계층 간 데이터 전달 모델이다.

Q. Entity를 API Response로 바로 반환해도 돼?
A. 권장하지 않는다. 민감정보 노출, Lazy Loading, 순환 참조, API 스펙 결합 문제가 생길 수 있다.

Q. Entity는 Controller에서 만들어도 돼?
A. 단순 생성 자체는 가능하지만 일반적으로 Request DTO를 Service에서 Entity 생성 로직으로 변환하는 구조가 더 명확하다.

---

## 2.2 Entity Basic Structure

### [개념]

Entity Basic Structure는 JPA가 Entity를 인식하고 DB Table과 Mapping하기 위한 최소 구조다.

기본적으로 `@Entity`, `@Id`, 기본 생성자, Column Field가 필요하다.

---

### [핵심]

필수 구조:

- Class Level `@Entity`
- Primary Key Field `@Id`
- 기본 생성자
- Field 기반 Mapping
- Access Level 통제
- 상태 변경 Method

권장 구조:

- `@Table(name = "...")`
- `@Column(nullable = false, length = ...)`
- `@GeneratedValue(strategy = GenerationType.IDENTITY)`
- `protected` no-args constructor
- 무분별한 Setter 지양
- static factory method 사용 가능
- update method 사용 가능

---

### [실무]

예시:

```java
@Entity
@Table(name = "posts")
@Getter
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class Post {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long postId;

    @Column(nullable = false, length = 100)
    private String title;

    @Column(nullable = false, columnDefinition = "TEXT")
    private String content;

    public static Post create(String title, String content) {
        Post post = new Post();
        post.title = title;
        post.content = content;
        return post;
    }

    public void update(String title, String content) {
        this.title = title;
        this.content = content;
    }
}
```

실무 기준:

- 기본 생성자는 JPA를 위해 필요하다.
- 외부 무분별 생성을 막기 위해 `protected` 기본 생성자를 사용한다.
- Setter 전체 공개는 지양한다.
- 상태 변경은 의미 있는 method로 표현한다.
- `@Column`으로 nullable, length, columnDefinition을 명확히 한다.
- Primary Key 이름은 Entity 기준으로 명확히 한다.

---

### [FAQ]

Q. Entity에 기본 생성자가 왜 필요해?
A. JPA가 Reflection으로 Entity를 생성하기 위해 기본 생성자가 필요하다.

Q. 기본 생성자는 public이어야 해?
A. 아니다. 외부 생성을 막기 위해 `protected`로 두는 경우가 많다.

Q. Setter를 전부 열어도 돼?
A. 권장하지 않는다. 변경 의도가 드러나는 method로 상태 변경을 통제하는 것이 좋다.

Q. Entity에 create method를 두는 이유는 뭐야?
A. 생성 의도를 명확히 하고 필수 값 설정을 한 곳에서 관리하기 위해 사용한다.

---

# 3. Table Mapping

## 3.1 Entity and Table Mapping

### [개념]

Table Mapping은 Entity Class를 DB Table과 연결하는 Mapping이다.

`@Entity`는 JPA 관리 대상임을 표시하고, `@Table`은 DB Table 이름과 설정을 지정한다.

---

### [핵심]

주요 Annotation:

- `@Entity`
- `@Table`
- `name`
- `schema`
- `indexes`
- `uniqueConstraints`

Mapping 관계:

```text
Entity Class
→ DB Table

Entity Field
→ DB Column

Entity ID
→ Primary Key

Entity Association
→ Foreign Key Relationship
```

---

### [실무]

예시:

```java
@Entity
@Table(name = "users")
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long userId;
}
```

명명 기준:

| Java Entity | DB Table      |
| ----------- | ------------- |
| User        | users         |
| Post        | posts         |
| OrderItem   | order_items   |
| Festival    | festivals     |
| ChatMessage | chat_messages |

권장:

- Entity 이름은 단수형 사용
- Table 이름은 프로젝트 DB Convention에 맞춤
- Snake Case Table 이름 사용 가능
- 예약어 Table 이름 주의
- Table 이름을 명시해 생성 SQL 예측 가능하게 유지
- 기존 DB Schema와 이름 일치 확인

주의:

- Entity 이름과 Table 이름이 항상 같지는 않다.
- DB Table 이름이 바뀌면 Repository Query와 Native Query에도 영향이 있다.
- Native Query는 Table / Column 이름을 직접 사용한다.
- JPQL은 Table 이름이 아니라 Entity 이름을 사용한다.

---

### [FAQ]

Q. `@Entity`만 쓰고 `@Table`은 생략해도 돼?
A. 가능하지만 Table 이름을 명확히 하기 위해 `@Table(name = "...")`을 사용하는 것이 좋다.

Q. Entity 이름은 단수, Table 이름은 복수로 해도 돼?
A. 가능하다. 중요한 것은 프로젝트 Convention을 일관되게 유지하는 것이다.

Q. JPQL에서는 Table 이름을 써?
A. 아니다. JPQL은 Table 이름이 아니라 Entity 이름과 Field 이름을 사용한다.

Q. Native Query에서는 Entity 이름을 써?
A. 아니다. Native Query는 실제 DB Table 이름과 Column 이름을 사용한다.

---

## 3.2 Field and Column Mapping

### [개념]

Column Mapping은 Entity Field를 DB Column과 연결하는 Mapping이다.

`@Column`은 nullable, length, unique, columnDefinition 같은 DB Column 제약과 속성을 표현한다.

---

### [핵심]

주요 속성:

- `name`
- `nullable`
- `length`
- `unique`
- `columnDefinition`
- `precision`
- `scale`
- `insertable`
- `updatable`

Field Mapping 기준:

```text
String Field
→ VARCHAR / TEXT

Long Field
→ BIGINT

Integer Field
→ INT

BigDecimal Field
→ DECIMAL

LocalDate
→ DATE

LocalDateTime
→ DATETIME / TIMESTAMP

Enum
→ VARCHAR with EnumType.STRING
```

---

### [실무]

예시:

```java
@Column(nullable = false, length = 100)
private String title;

@Column(nullable = false, columnDefinition = "TEXT")
private String content;

@Column(nullable = false, unique = true, length = 100)
private String email;
```

권장:

- 필수 값은 `nullable = false`
- 문자열 길이는 명확히 지정
- 긴 본문은 `TEXT` 전략 검토
- 금액은 `BigDecimal`과 precision / scale 검토
- 날짜는 `LocalDate`, 일시는 `LocalDateTime` 사용
- DB Constraint와 Application Validation을 함께 검토

SQL Foundation 연결:

```text
SQL Column
→ JPA Field

SQL NOT NULL
→ @Column(nullable = false)

SQL UNIQUE
→ @Column(unique = true) + DB Unique Constraint

SQL VARCHAR Length
→ @Column(length = n)

SQL TEXT
→ columnDefinition = "TEXT"
```

주의:

- `nullable = false`는 DB NOT NULL과 연결된다.
- Bean Validation `@NotNull`과 DB `NOT NULL`은 역할이 다르다.
- `unique = true`만 믿지 말고 DB Constraint 생성 여부를 확인한다.
- `columnDefinition`은 DB 종속성을 높일 수 있다.

---

### [FAQ]

Q. `@Column(nullable = false)`는 꼭 써야 해?
A. 필수는 아니지만 DB 무결성과 코드 의도를 명확히 하기 위해 중요한 필드는 명시하는 것이 좋다.

Q. `@NotNull`과 `nullable = false`는 같아?
A. 아니다. `@NotNull`은 Application Validation이고 `nullable = false`는 DB Column 제약과 연결된다.

Q. `columnDefinition`은 언제 써?
A. TEXT, DECIMAL, DB 특화 타입처럼 기본 Mapping만으로 의도가 부족할 때 제한적으로 사용한다.

Q. Column 이름은 꼭 `@Column(name = "...")`으로 써야 해?
A. Convention이 명확하면 생략 가능하지만 기존 DB와 이름이 다르면 명시해야 한다.

---

# 4. Primary Key Mapping

## 4.1 Primary Key Strategy

### [개념]

Primary Key Mapping은 Entity 식별자와 DB Primary Key를 연결하는 Mapping이다.

JPA Entity는 반드시 식별자 Field를 가져야 한다.

---

### [핵심]

핵심 Annotation:

- `@Id`
- `@GeneratedValue`
- `GenerationType.IDENTITY`
- `GenerationType.SEQUENCE`
- `GenerationType.AUTO`
- `GenerationType.TABLE`

주요 개념:

- Primary Key
- Surrogate Key
- Natural Key
- Entity Identity
- DB Identity
- ID Generation Strategy

---

### [실무]

예시:

```java
@Id
@GeneratedValue(strategy = GenerationType.IDENTITY)
private Long userId;
```

권장:

- 대부분 `Long` Surrogate Key 사용
- 비즈니스 값은 Primary Key로 사용 지양
- 이메일, 전화번호, 닉네임은 Unique Column 후보
- Primary Key 값은 변경하지 않음
- DB 종류에 맞는 ID 생성 전략 사용
- MySQL 계열은 `IDENTITY` 사용 가능
- Oracle / PostgreSQL 계열은 `SEQUENCE` 검토 가능

SQL Foundation 연결:

```text
SQL Primary Key
→ JPA @Id

SQL Auto Increment
→ GenerationType.IDENTITY

SQL Sequence
→ GenerationType.SEQUENCE

Business Unique Value
→ Unique Column, not Primary Key
```

주의:

- Natural Key는 변경 가능성이 있으면 PK로 부적합하다.
- Entity equals / hashCode에서 ID 사용 시 생성 전 Entity 상태를 주의한다.
- ID 생성 시점은 전략에 따라 다르다.
- `IDENTITY`는 INSERT 시점에 ID가 생성된다.

---

### [FAQ]

Q. JPA Entity에는 반드시 `@Id`가 필요해?
A. 필요하다. JPA Entity는 식별자를 기준으로 Persistence Context에서 관리된다.

Q. Entity ID는 어떤 타입이 좋아?
A. 대부분 `Long` 타입의 Surrogate Key를 사용한다.

Q. 이메일을 Primary Key로 써도 돼?
A. 권장하지 않는다. 이메일은 변경될 수 있으므로 Unique Column으로 두는 것이 좋다.

Q. `IDENTITY`와 `SEQUENCE`는 뭐가 달라?
A. `IDENTITY`는 DB Auto Increment 기반이고, `SEQUENCE`는 DB Sequence 기반 ID 생성 전략이다.

---

## 4.2 Entity Identity and Object Identity

### [개념]

Entity Identity는 DB Primary Key 기준의 식별성이다.

Object Identity는 Java Object Reference 기준의 동일성이다.

JPA Persistence Context는 같은 Transaction 안에서 같은 Primary Key Entity에 대해 동일 객체를 보장할 수 있다.

---

### [핵심]

구분:

| 개념                 | 기준                                    |
| -------------------- | --------------------------------------- |
| Entity Identity      | Primary Key                             |
| Object Identity      | Java Reference                          |
| Persistence Identity | Persistence Context 안의 Managed Entity |
| Business Equality    | 비즈니스 값 기준 비교                   |

핵심 키워드:

- Entity Identity
- Primary Key
- Object Reference
- First Level Cache
- Persistence Context
- Managed Entity
- equals
- hashCode

---

### [실무]

흐름:

```text
Transaction Begin
→ findById(1L)
→ Persistence Context 저장
→ findById(1L)
→ 같은 Managed Entity 반환 가능
```

주의:

- 영속 상태에서는 같은 ID Entity가 같은 객체로 관리될 수 있다.
- Transaction 밖 Detached Entity는 동일성 보장이 약해진다.
- equals / hashCode 구현은 신중해야 한다.
- ID가 아직 없는 신규 Entity는 비교 기준이 불안정하다.
- Entity를 HashSet에 넣은 뒤 ID가 생성되면 hashCode 문제가 생길 수 있다.

권장:

- Entity equals / hashCode는 프로젝트 규칙으로 통일
- 무분별한 Lombok `@EqualsAndHashCode` 사용 지양
- Association Field를 equals / hashCode에 포함하지 않음
- 순환 참조와 Lazy Loading을 유발하는 equals / hashCode 금지

---

### [FAQ]

Q. Entity Identity는 뭐야?
A. DB Primary Key를 기준으로 Entity를 식별하는 개념이다.

Q. 같은 ID면 항상 같은 Java 객체야?
A. 아니다. 같은 Persistence Context 안에서는 같을 수 있지만 Transaction 범위 밖에서는 다를 수 있다.

Q. Entity에 Lombok `@Data`를 써도 돼?
A. 권장하지 않는다. Setter, equals, hashCode, toString이 무분별하게 생성되어 JPA 문제를 만들 수 있다.

Q. equals / hashCode에 연관관계를 넣어도 돼?
A. 권장하지 않는다. Lazy Loading, 순환 참조, StackOverflow 문제가 발생할 수 있다.

---

# 5. DTO and Entity Separation

## 5.1 DTO Separation Purpose

### [개념]

DTO와 Entity 분리는 API 입출력 모델과 Persistence Model을 분리하는 설계 원칙이다.

Entity는 DB 저장 모델이고 DTO는 Request / Response / Projection / Layer 전달 모델이다.

---

### [핵심]

분리 이유:

- Entity 직접 노출 방지
- API 스펙과 DB Schema 결합 방지
- 민감정보 노출 방지
- Lazy Loading 문제 방지
- 순환 참조 방지
- Validation 분리
- Request / Response 구조 분리
- 화면 요구사항과 Persistence Model 분리
- 변경 영향 범위 축소

DTO 종류:

- Request DTO
- Response DTO
- Projection DTO
- Command DTO
- Search Condition DTO

---

### [실무]

나쁜 예:

```java
@GetMapping("/{id}")
public User getUser(@PathVariable Long id) {
    return userRepository.findById(id).orElseThrow();
}
```

좋은 예:

```java
@GetMapping("/{id}")
public UserResponse getUser(@PathVariable Long id) {
    return userService.getUser(id);
}
```

Response DTO 예시:

```java
public record UserResponse(
        Long userId,
        String email,
        String nickname
) {

    public static UserResponse from(User user) {
        return new UserResponse(
                user.getUserId(),
                user.getEmail(),
                user.getNickname()
        );
    }
}
```

권장 흐름:

```text
Request DTO
→ Service
→ Entity 조회 / 생성 / 변경
→ Response DTO 변환
→ Controller Response
```

주의:

- RequestBody로 Entity 직접 수신 금지
- Entity를 Controller Response로 직접 반환 금지
- DTO 변환 시 Lazy Loading 발생 가능성 확인
- DTO 변환 위치는 Transaction 범위와 함께 결정
- 목록 조회는 DTO Projection 검토

---

### [FAQ]

Q. Entity와 DTO는 왜 분리해?
A. API 변경과 DB 변경을 분리하고 민감정보 노출, Lazy Loading, 순환 참조 문제를 막기 위해 분리한다.

Q. Entity를 Controller에서 바로 반환하면 왜 안 돼?
A. 민감정보 노출, Lazy Loading, 순환 참조, API 스펙 변경 위험이 생길 수 있다.

Q. RequestBody로 Entity를 받아도 돼?
A. 권장하지 않는다. API 입력 구조와 Entity 내부 구조가 강하게 결합되고 보안 문제가 생길 수 있다.

Q. DTO 변환은 어디서 해?
A. 간단한 변환은 DTO의 `from` method 또는 Service에서 처리할 수 있다. 프로젝트 규칙으로 일관화하는 것이 중요하다.

---

## 5.2 Request DTO and Response DTO

### [개념]

Request DTO는 Client 입력을 받는 객체다.

Response DTO는 Client 응답을 만드는 객체다.

Request DTO와 Response DTO는 역할이 다르므로 분리하는 것이 좋다.

---

### [핵심]

Request DTO 역할:

- 입력 값 수신
- Validation 적용
- API 입력 스펙 표현
- Entity 생성 / 변경 값 전달

Response DTO 역할:

- 출력 필드 제어
- 민감정보 제외
- API 응답 스펙 표현
- Entity 내부 구조 은닉
- 화면 요구사항 반영

분리 기준:

```text
Client Input
→ Request DTO

Database Entity
→ Entity

Client Output
→ Response DTO
```

---

### [실무]

Request DTO 예시:

```java
public record PostCreateRequest(
        @NotBlank String title,
        @NotBlank String content
) {
}
```

Response DTO 예시:

```java
public record PostResponse(
        Long postId,
        String title,
        String content
) {

    public static PostResponse from(Post post) {
        return new PostResponse(
                post.getPostId(),
                post.getTitle(),
                post.getContent()
        );
    }
}
```

Service 예시:

```java
@Transactional
public Long createPost(PostCreateRequest request) {
    Post post = Post.create(request.title(), request.content());
    Post savedPost = postRepository.save(post);
    return savedPost.getPostId();
}

@Transactional(readOnly = true)
public PostResponse getPost(Long postId) {
    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

    return PostResponse.from(post);
}
```

주의:

- Request DTO에 Entity Association을 직접 받지 않는다.
- Request DTO에는 필요한 ID 값만 받는 것이 일반적이다.
- Response DTO에 Entity 전체를 중첩하지 않는다.
- Response DTO는 API별로 달라질 수 있다.
- 민감정보는 Response DTO에서 제외한다.

---

### [FAQ]

Q. Request DTO와 Response DTO를 하나로 써도 돼?
A. 작은 예제에서는 가능하지만 실무에서는 입력과 출력 요구사항이 달라지는 경우가 많아 분리하는 것이 좋다.

Q. Request DTO에서 User Entity를 직접 받아도 돼?
A. 권장하지 않는다. 일반적으로 `userId` 같은 식별자를 받고 Service에서 Entity를 조회한다.

Q. Response DTO에 Entity를 필드로 넣어도 돼?
A. 권장하지 않는다. 필요한 값만 DTO Field로 풀어서 응답하는 것이 안전하다.

Q. DTO에 Validation을 붙여도 돼?
A. Request DTO에는 입력 검증을 위해 Bean Validation을 적용하는 것이 일반적이다.

---

# 6. Entity Design Rules

## 6.1 Setter Control

### [개념]

Setter Control은 Entity Field를 아무 곳에서나 변경하지 못하게 하고, 의미 있는 상태 변경 method로 변경 경로를 통제하는 규칙이다.

---

### [핵심]

권장:

- 전체 Setter 공개 지양
- 필요한 상태 변경 method 제공
- method 이름에 의도 표현
- Validation / Business Rule 포함 가능
- Entity 상태 변경 경로 제한

비권장:

- `@Setter` 전체 적용
- Lombok `@Data` 사용
- Controller에서 Entity Field 직접 변경
- DTO 값을 Entity에 무분별 복사
- Reflection 기반 무작위 변경

---

### [실무]

나쁜 예:

```java
@Setter
@Entity
public class Post {

    private String title;
    private String content;
}
```

좋은 예:

```java
@Entity
@Getter
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class Post {

    @Column(nullable = false, length = 100)
    private String title;

    @Column(nullable = false, columnDefinition = "TEXT")
    private String content;

    public void update(String title, String content) {
        this.title = title;
        this.content = content;
    }
}
```

상태 변경 method 예시:

```java
public void publish() {
    this.status = PostStatus.PUBLISHED;
}

public void delete() {
    this.deleted = true;
}
```

장점:

- 변경 의도 명확
- Dirty Checking 추적 쉬움
- 비즈니스 규칙 위치 명확
- Review Agent가 변경 경로 검토 가능
- 무분별한 Field 변경 방지

---

### [FAQ]

Q. Entity Setter를 전부 열면 왜 안 좋아?
A. 어디서 어떤 의도로 상태가 바뀌는지 추적하기 어렵고 비즈니스 규칙이 흩어진다.

Q. Entity 상태 변경 method는 왜 필요해?
A. 변경 의도를 method 이름으로 표현하고 변경 규칙을 Entity 내부에 모을 수 있기 때문이다.

Q. DTO 값을 Entity에 복사할 때 BeanUtils를 써도 돼?
A. 권장하지 않는다. 의도하지 않은 Field 변경과 보안 문제가 생길 수 있다.

Q. Dirty Checking을 쓰려면 Setter가 필요해?
A. 아니다. Transaction 안에서 Entity 상태가 변경되면 method를 통한 변경도 Dirty Checking 대상이 된다.

---

## 6.2 Constructor and Factory Method

### [개념]

Entity Constructor와 Factory Method는 Entity 생성 규칙을 명확히 하는 방법이다.

JPA 기본 생성자와 비즈니스 생성 경로를 분리하는 것이 중요하다.

---

### [핵심]

기준:

- JPA 기본 생성자 필요
- 기본 생성자는 `protected` 권장
- 외부 생성은 static factory method 가능
- 필수 값 누락 방지
- 생성 의도 표현
- Association 설정은 별도 method 검토

---

### [실무]

예시:

```java
@Entity
@Getter
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class Comment {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long commentId;

    @Column(nullable = false, columnDefinition = "TEXT")
    private String content;

    public static Comment create(String content) {
        Comment comment = new Comment();
        comment.content = content;
        return comment;
    }
}
```

Association 포함 생성 예시:

```java
public static Comment create(Post post, User user, String content) {
    Comment comment = new Comment();
    comment.post = post;
    comment.user = user;
    comment.content = content;
    return comment;
}
```

권장:

- 필수 값은 create method에서 받음
- 생성 후 변경하면 안 되는 값은 생성 시점에 설정
- Association은 연관관계 편의 method와 함께 검토
- 생성 method 이름은 의도를 담음
- 복잡한 생성은 Domain Service 또는 Factory 검토

주의:

- JPA 기본 생성자는 비즈니스 생성용이 아니다.
- public no-args constructor는 외부 오용 가능성이 있다.
- 생성자에서 지나치게 많은 로직을 수행하지 않는다.

---

### [FAQ]

Q. Entity 기본 생성자와 생성 method를 둘 다 둬야 해?
A. JPA 기본 생성자는 JPA용이고 생성 method는 비즈니스 생성용이므로 역할이 다르다.

Q. static factory method를 꼭 써야 해?
A. 필수는 아니지만 생성 의도와 필수 값을 명확히 하기 좋다.

Q. Entity 생성자에 비즈니스 로직을 많이 넣어도 돼?
A. 과도한 로직은 피하고 생성 규칙 중심으로 유지하는 것이 좋다.

Q. Association도 create method에서 세팅해도 돼?
A. 가능하지만 양방향 관계라면 편의 method로 양쪽 객체 상태를 함께 맞추는 것을 검토해야 한다.

---

# 7. Entity Naming and Package Rules

## 7.1 Entity Naming

### [개념]

Entity Naming은 Entity Class, Field, Table, Column 이름을 일관되게 유지하는 규칙이다.

Naming Consistency는 Repository Query Method, JPQL, DTO Mapping, Retrieval 정확도에 영향을 준다.

---

### [핵심]

권장 Naming:

- Entity Class: PascalCase
- Entity Field: camelCase
- DB Table: snake_case or plural convention
- DB Column: snake_case
- Primary Key Field: `{entityName}Id`
- Foreign Key Column: `{entityName}_id`
- Repository: `{Entity}Repository`
- DTO: `{Entity}{Action}Request`, `{Entity}Response`

예시:

| 요소         | 예               |
| ------------ | ---------------- |
| Entity       | `Post`           |
| Table        | `posts`          |
| ID Field     | `postId`         |
| ID Column    | `post_id`        |
| Repository   | `PostRepository` |
| Response DTO | `PostResponse`   |

---

### [실무]

명명 흐름:

```text
DB Table: posts
→ Entity: Post
→ Primary Key Column: post_id
→ Entity ID Field: postId
→ Repository: PostRepository
→ Response DTO: PostResponse
```

JPQL 영향:

```java
@Query("""
    select p
    from Post p
    where p.title = :title
""")
List<Post> findByTitle(String title);
```

주의:

- JPQL은 Entity / Field 이름을 사용한다.
- Native Query는 Table / Column 이름을 사용한다.
- Query Method는 Entity Field 이름을 사용한다.
- Field 이름 변경은 Query Method와 JPQL에 영향을 준다.
- Naming 불일치는 Retrieval과 Code Generation 품질을 떨어뜨린다.

---

### [FAQ]

Q. Entity Field 이름과 DB Column 이름은 같아야 해?
A. 꼭 같을 필요는 없지만 Mapping이 명확해야 한다. Java는 camelCase, DB는 snake_case를 많이 사용한다.

Q. Repository Query Method는 Column 이름 기준이야?
A. 아니다. Entity Field 이름 기준이다.

Q. JPQL은 Column 이름 기준이야?
A. 아니다. JPQL은 Entity 이름과 Field 이름 기준이다.

Q. Native Query는 Field 이름 기준이야?
A. 아니다. Native Query는 실제 DB Table 이름과 Column 이름 기준이다.

---

## 7.2 Package Responsibility

### [개념]

Package Responsibility는 Entity, DTO, Repository, Service, Controller의 책임을 Package 단위로 분리하는 규칙이다.

JPA Entity는 Persistence Layer와 Domain Model 경계에 위치한다.

---

### [핵심]

기본 구조:

```text
controller
→ API Endpoint

service
→ Transaction / Business Logic

repository
→ Data Access

entity
→ Persistence Model

dto.request
→ Request DTO

dto.response
→ Response DTO
```

Entity 관련 Package:

- `entity`
- `entity.enums`
- `repository`
- `dto.request`
- `dto.response`
- `service`

---

### [실무]

권장 흐름:

```text
Controller
→ Request DTO
→ Service
→ Repository
→ Entity
→ Response DTO
→ Controller
```

예시 구조:

```text
src/main/java/com/example/project
├ controller
├ service
├ repository
├ entity
│ └ enums
└ dto
  ├ request
  └ response
```

책임 기준:

| Layer      | 책임                        |
| ---------- | --------------------------- |
| Controller | HTTP 요청 / 응답            |
| Service    | Transaction / 비즈니스 흐름 |
| Repository | Entity 조회 / 저장          |
| Entity     | 상태와 Mapping              |
| DTO        | API 입출력                  |
| Exception  | 실패 표현                   |

주의:

- Repository에 비즈니스 로직을 넣지 않는다.
- Controller에서 Entity를 수정하지 않는다.
- DTO가 Entity 내부 구조에 과도하게 의존하지 않는다.
- Entity Package와 DTO Package를 섞지 않는다.
- Entity는 API Layer에 직접 노출하지 않는다.

---

### [FAQ]

Q. Entity는 어느 Package에 두는 게 좋아?
A. 일반적으로 `entity` Package에 두고 Enum은 `entity.enums`로 분리할 수 있다.

Q. Repository는 Entity Package 안에 둬도 돼?
A. 가능은 하지만 책임 분리를 위해 `repository` Package로 분리하는 경우가 많다.

Q. DTO를 Entity 옆에 둬도 돼?
A. 권장하지 않는다. API 입출력 모델과 Persistence Model을 구분하기 위해 DTO Package를 분리하는 것이 좋다.

Q. Repository에서 비즈니스 로직을 처리해도 돼?
A. 권장하지 않는다. Repository는 Data Access 중심이고 비즈니스 흐름은 Service에서 처리한다.

---

# 8. Entity Mapping Review

## 8.1 Entity Mapping Checklist

### [개념]

Entity Mapping Checklist는 Entity 설계가 JPA, SQL, Backend Layer 기준에 맞는지 검수하는 목록이다.

Review Agent는 Entity 생성 후 Mapping, Constraint, DTO 분리, Naming, Layer 책임을 확인해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] Entity에 @Entity가 있는가?
- [ ] Table 이름이 명확한가?
- [ ] Primary Key에 @Id가 있는가?
- [ ] ID 생성 전략이 DB와 맞는가?
- [ ] 기본 생성자가 있는가?
- [ ] 기본 생성자 접근 제한이 적절한가?
- [ ] Column nullable / length가 명확한가?
- [ ] 필수 값과 선택 값이 구분되는가?
- [ ] Entity와 DTO가 분리되었는가?
- [ ] Entity를 API Response로 직접 반환하지 않는가?
- [ ] RequestBody로 Entity를 직접 받지 않는가?
- [ ] Setter 전체 공개를 피했는가?
- [ ] 상태 변경 method가 있는가?
- [ ] Table / Column Naming이 일관적인가?
- [ ] Repository Query Method가 Field 이름과 맞는가?
- [ ] JPQL이 Entity / Field 이름 기준으로 작성되는가?
- [ ] Native Query가 Table / Column 이름 기준으로 작성되는가?
- [ ] Lombok @Data 사용을 피했는가?
- [ ] equals / hashCode에 Association Field를 넣지 않았는가?
- [ ] Entity에 화면 전용 Field를 넣지 않았는가?
```

---

### [실무]

Review Flow:

```text
Entity Class 확인
→ @Entity / @Table 확인
→ @Id / @GeneratedValue 확인
→ @Column 확인
→ Constructor 확인
→ Setter 확인
→ DTO 분리 확인
→ Naming 확인
→ Repository / JPQL 영향 확인
→ API 직접 노출 여부 확인
```

Common Review Findings:

```text
문제: Entity를 Controller에서 직접 반환
위험: 민감정보 노출, Lazy Loading, 순환 참조
해결: Response DTO 반환

문제: @Setter 전체 적용
위험: 상태 변경 경로 추적 어려움
해결: 의미 있는 update method 제공

문제: Entity Field와 Query Method 이름 불일치
위험: Application Startup Error
해결: Field 이름 기준으로 Query Method 수정

문제: JPQL에서 Table 이름 사용
위험: Query Parsing Error
해결: Entity 이름과 Field 이름 사용
```

---

### [FAQ]

Q. Entity Mapping 검수에서 가장 먼저 볼 것은 뭐야?
A. `@Entity`, `@Id`, 기본 생성자, Table / Column Mapping, DTO 분리 여부를 먼저 확인한다.

Q. Entity 직접 반환은 왜 Review에서 잡아야 해?
A. API 스펙과 DB 구조가 결합되고 Lazy Loading, 순환 참조, 민감정보 노출 위험이 있기 때문이다.

Q. Entity에 `@Data`가 있으면 왜 위험해?
A. Setter, equals, hashCode, toString이 자동 생성되어 JPA 연관관계와 Lazy Loading 문제를 만들 수 있다.

Q. JPQL 오류가 나면 뭘 확인해?
A. Table / Column 이름이 아니라 Entity / Field 이름을 사용했는지 확인한다.

---

# 9. Common Mistakes

## 9.1 Entity Mapping Common Mistakes

### [개념]

Entity Mapping Common Mistakes는 JPA 초기에 자주 발생하는 Mapping, DTO 분리, Naming, Layer 책임 오류다.

---

### [핵심]

자주 발생하는 실수:

- `@Entity` 누락
- `@Id` 누락
- 기본 생성자 없음
- 기본 생성자 public 남용
- `@Setter` 전체 공개
- Lombok `@Data` 사용
- Entity를 API Response로 직접 반환
- RequestBody로 Entity 직접 수신
- Entity에 화면 전용 Field 추가
- Column nullable / length 미지정
- Primary Key에 비즈니스 값 사용
- Entity Field와 Query Method 이름 불일치
- JPQL에서 Table / Column 이름 사용
- Native Query에서 Entity / Field 이름 사용
- DTO 변환 중 Lazy Loading 발생 가능성 무시
- Repository에 비즈니스 로직 작성
- Controller에서 Entity 상태 변경

---

### [실무]

Anti Pattern 예시:

```java
@PostMapping
public Post createPost(@RequestBody Post post) {
    return postRepository.save(post);
}
```

문제:

- RequestBody로 Entity 직접 수신
- Entity 직접 반환
- Service Transaction 흐름 없음
- DTO 분리 없음
- Validation 책임 불명확
- API 스펙과 Entity 구조 결합

개선 예시:

```java
@PostMapping
public PostResponse createPost(@Valid @RequestBody PostCreateRequest request) {
    return postService.createPost(request);
}
```

Service 개선 예시:

```java
@Transactional
public PostResponse createPost(PostCreateRequest request) {
    Post post = Post.create(request.title(), request.content());
    Post savedPost = postRepository.save(post);
    return PostResponse.from(savedPost);
}
```

Review 기준:

```text
API Request
→ Request DTO 사용 여부 확인

Entity Creation
→ Entity 생성 method 확인

Persistence
→ Repository save 위치 확인

Response
→ Response DTO 변환 확인
```

---

### [FAQ]

Q. Entity를 RequestBody로 받으면 왜 안 좋아?
A. Client 입력과 Entity 내부 구조가 결합되고 의도하지 않은 Field 변경이나 보안 문제가 생길 수 있다.

Q. Entity를 Response로 반환하면 왜 안 좋아?
A. 민감정보, Lazy Field, 연관관계 순환 참조, API 스펙 결합 문제가 생길 수 있다.

Q. Entity에 화면 표시용 Field를 넣어도 돼?
A. 권장하지 않는다. 화면 표시용 값은 Response DTO나 Projection DTO에서 처리하는 것이 좋다.

Q. JPA 초보가 Entity에서 가장 많이 실수하는 부분은 뭐야?
A. Entity와 DTO를 분리하지 않고 Setter를 전부 열어 API와 DB 구조를 강하게 결합하는 실수가 많다.

---

# 10. Part01 Final Goal

## 10.1 Agent Output Goal

### [개념]

JPA Advanced Part01의 최종 목적은 Agent가 Entity를 단순 Java Class가 아니라 DB Table과 연결된 Persistence Model로 설계하도록 만드는 것이다.

Part01은 ORM, JPA, Hibernate, Entity, Table Mapping, DTO 분리, Entity 기본 구조를 담당한다.

---

### [핵심]

Agent가 수행해야 할 작업:

- ORM 개념 이해
- JPA와 Hibernate 구분
- Entity와 Table Mapping 설계
- Field와 Column Mapping 설계
- Primary Key 기본 Mapping 판단
- Entity와 DTO 분리
- Request DTO / Response DTO 분리
- Entity 직접 노출 Anti Pattern 탐지
- Setter 남용 탐지
- Naming Consistency 검토
- JPQL / Native Query 이름 기준 구분
- Entity Mapping Checklist 적용

---

### [실무]

Agent 작업 흐름:

```text
User Backend Request
→ Identify Persistence Model
→ Design Entity
→ Map Table
→ Map Primary Key
→ Map Column
→ Separate DTO
→ Define State Change Method
→ Check Naming
→ Check API Exposure
→ Review Entity Mapping
```

Part01 이후 연결:

```text
Part01 ORM / Entity Mapping
→ Part02 Primary Key / Column / Constraint
→ Part03 Association Mapping / Table Relationship
→ Part04 Persistence Context / Dirty Checking
→ Part05 Repository / JPQL / Native Query
→ Part06 Fetch Join / N+1
→ Part07 Transaction / Cascade / Pagination
→ Part08 Troubleshooting / Anti Pattern
```

---

### [FAQ]

Q. JPA Advanced Part01의 목적은 뭐야?
A. Agent가 ORM, JPA, Hibernate, Entity Mapping, Table Mapping, DTO 분리 기준을 이해하고 안정적인 Entity 기본 구조를 만들게 하는 것이다.

Q. Part01에서 연관관계까지 깊게 다뤄?
A. 아니다. Part01은 Entity와 Table Mapping 기본을 다루고 연관관계는 Part03에서 깊게 다룬다.

Q. Part01에서 Repository까지 다뤄?
A. 아니다. Repository, Query Method, JPQL, Native Query는 Part05에서 다룬다.

Q. Part01에서 가장 중요한 Review 기준은 뭐야?
A. Entity와 DTO 분리, `@Entity` / `@Id` / 기본 생성자 / Column Mapping, Setter 통제, Entity 직접 반환 금지다.

---

# Retrieval Queries

### [FAQ]

Q. ORM은 뭐야?
A. ORM은 Java Object와 Relational Database Table을 Mapping해서 객체 상태와 DB 저장을 연결하는 기술이다.

Q. JPA는 뭐야?
A. JPA는 Java ORM 표준이며 Entity와 DB Table Mapping, Persistence Context, Entity 상태 관리를 제공한다.

Q. Hibernate는 뭐야?
A. Hibernate는 JPA 표준을 구현한 대표적인 ORM Framework다.

Q. JPA와 Hibernate는 같은 거야?
A. 아니다. JPA는 표준 인터페이스이고 Hibernate는 구현체다.

Q. Spring Data JPA는 JPA야?
A. 아니다. Spring Data JPA는 JPA Repository 사용을 편하게 해주는 Spring 추상화다.

Q. JPA는 SQL을 몰라도 쓸 수 있어?
A. 아니다. JPA는 SQL을 생성하므로 SELECT, JOIN, Transaction, Constraint, Pagination 같은 SQL 이해가 필요하다.

Q. Entity는 뭐야?
A. Entity는 DB Table과 Mapping되는 Persistence Model이며 JPA Persistence Context가 상태를 관리하는 객체다.

Q. Entity와 Table은 같은 개념이야?
A. 아니다. Entity는 Java Persistence Model이고 Table은 DB 저장 구조다. JPA가 둘을 Mapping한다.

Q. Entity Mapping은 뭐야?
A. Entity Class와 DB Table, Entity Field와 DB Column, Entity Association과 Foreign Key를 연결하는 Mapping이다.

Q. Table Mapping은 뭐야?
A. Entity Class를 DB Table과 연결하는 Mapping이며 `@Entity`, `@Table`을 사용한다.

Q. Column Mapping은 뭐야?
A. Entity Field를 DB Column과 연결하고 nullable, length, unique 같은 속성을 지정하는 Mapping이다.

Q. `@Entity`는 뭐야?
A. 해당 Class가 JPA 관리 Entity임을 표시하는 Annotation이다.

Q. `@Table`은 왜 써?
A. Entity와 Mapping될 DB Table 이름과 Table 설정을 명확히 하기 위해 사용한다.

Q. `@Column(nullable = false)`는 왜 써?
A. 필수 Column 의도를 명확히 하고 DB NOT NULL Constraint와 연결하기 위해 사용한다.

Q. `@NotNull`과 `nullable = false`는 같아?
A. 아니다. `@NotNull`은 Application Validation이고 `nullable = false`는 DB Column 제약과 연결된다.

Q. Primary Key Mapping은 뭐야?
A. Entity 식별자 Field와 DB Primary Key를 연결하는 Mapping이다.

Q. Entity에는 `@Id`가 꼭 필요해?
A. 필요하다. JPA는 식별자를 기준으로 Entity를 관리한다.

Q. JPA Entity ID는 어떤 타입이 좋아?
A. 대부분 `Long` 타입의 Surrogate Key를 사용한다.

Q. 이메일을 Primary Key로 써도 돼?
A. 권장하지 않는다. 이메일은 변경 가능한 비즈니스 값이므로 Unique Column으로 두는 것이 좋다.

Q. `GenerationType.IDENTITY`는 뭐야?
A. DB Auto Increment 기반으로 INSERT 시점에 ID를 생성하는 전략이다.

Q. Entity 기본 생성자는 왜 필요해?
A. JPA가 Reflection으로 Entity를 생성하기 위해 기본 생성자가 필요하다.

Q. Entity 기본 생성자는 public이어야 해?
A. 아니다. 외부 생성을 막기 위해 `protected`로 두는 경우가 많다.

Q. Entity에 Setter를 전부 열어도 돼?
A. 권장하지 않는다. 상태 변경 의도가 드러나는 method로 변경 경로를 통제하는 것이 좋다.

Q. Entity에 Lombok `@Data`를 써도 돼?
A. 권장하지 않는다. Setter, equals, hashCode, toString이 무분별하게 생성되어 JPA 문제를 만들 수 있다.

Q. Entity에 `@Setter` 전체 적용해도 돼?
A. 권장하지 않는다. Entity 상태 변경 경로가 불명확해진다.

Q. Entity 상태 변경 method는 왜 필요해?
A. 변경 의도를 method 이름으로 표현하고 Dirty Checking 대상 변경을 명확히 하기 위해 필요하다.

Q. Entity create method는 왜 써?
A. Entity 생성 의도와 필수 값을 명확히 하고 생성 규칙을 한 곳에서 관리하기 위해 사용한다.

Q. Entity와 DTO는 왜 분리해?
A. API 변경과 DB 변경을 분리하고 민감정보 노출, Lazy Loading, 순환 참조 문제를 막기 위해 분리한다.

Q. Entity를 Controller에서 바로 반환하면 왜 안 돼?
A. 민감정보 노출, Lazy Loading, 순환 참조, API 스펙 변경 위험이 생길 수 있다.

Q. RequestBody로 Entity를 받아도 돼?
A. 권장하지 않는다. Client 입력 구조와 Entity 내부 구조가 강하게 결합되고 보안 문제가 생길 수 있다.

Q. Request DTO는 뭐야?
A. Client 입력을 받는 DTO이며 Validation과 API 입력 스펙을 표현한다.

Q. Response DTO는 뭐야?
A. Client 응답을 구성하는 DTO이며 출력 필드 제어와 Entity 내부 구조 은닉을 담당한다.

Q. Request DTO와 Response DTO를 하나로 써도 돼?
A. 작은 예제에서는 가능하지만 실무에서는 입력과 출력 요구사항이 달라지는 경우가 많아 분리하는 것이 좋다.

Q. DTO 변환은 어디서 해?
A. 간단한 변환은 DTO의 `from` method 또는 Service에서 처리할 수 있다. Transaction 범위와 프로젝트 규칙을 함께 고려한다.

Q. JPQL은 Table 이름을 사용해?
A. 아니다. JPQL은 Entity 이름과 Field 이름을 사용한다.

Q. Native Query는 Entity 이름을 사용해?
A. 아니다. Native Query는 실제 DB Table 이름과 Column 이름을 사용한다.

Q. Repository Query Method는 Column 이름 기준이야?
A. 아니다. Repository Query Method는 Entity Field 이름 기준이다.

Q. Entity Naming은 왜 중요해?
A. Repository Query Method, JPQL, DTO Mapping, Code Generation, Retrieval 정확도에 영향을 주기 때문이다.

Q. Entity Field와 DB Column 이름은 같아야 해?
A. 꼭 같을 필요는 없지만 Mapping이 명확해야 한다. Java는 camelCase, DB는 snake_case를 많이 사용한다.

Q. Entity는 어느 Package에 두는 게 좋아?
A. 일반적으로 `entity` Package에 두고 Enum은 `entity.enums`로 분리할 수 있다.

Q. Repository는 무슨 역할이야?
A. Entity 조회와 저장을 담당하는 Data Access Layer다. 비즈니스 로직은 Service에서 처리한다.

Q. Repository에 비즈니스 로직을 넣어도 돼?
A. 권장하지 않는다. Repository는 Data Access 중심이고 비즈니스 흐름은 Service에서 처리한다.

Q. Entity Mapping 검수에서 가장 먼저 확인할 것은 뭐야?
A. `@Entity`, `@Id`, 기본 생성자, Table / Column Mapping, DTO 분리 여부를 먼저 확인한다.

Q. Entity 직접 반환은 왜 Anti Pattern이야?
A. API 스펙과 DB 구조가 결합되고 Lazy Loading, 순환 참조, 민감정보 노출 위험이 생기기 때문이다.

Q. Entity에 화면 표시용 Field를 넣어도 돼?
A. 권장하지 않는다. 화면 표시용 값은 Response DTO나 Projection DTO에서 처리하는 것이 좋다.

Q. JPA Part01에서 가장 중요한 기준은 뭐야?
A. ORM 이해, Entity Mapping, Table Mapping, DTO 분리, Setter 통제, Entity 직접 노출 금지다.

Q. JPA Part01 다음에는 무엇을 다뤄?
A. Part02에서 Primary Key, Column Mapping, Constraint, Data Integrity, Enum Mapping을 다룬다.
