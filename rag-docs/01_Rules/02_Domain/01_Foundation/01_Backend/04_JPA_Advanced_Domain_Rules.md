# JPA Advanced Domain Rules

---

# 1. Domain Purpose

## 1.1 Purpose

### [개념]

JPA Advanced Domain Rules 문서는 Backend Agent / Review Agent / PM Agent용 RAG 문서 제작 규칙이다.

목적:

- JPA 기반 Persistence Layer 설계 지원
- Entity / Table Mapping 기준 제공
- 연관관계 설계 판단 기준 제공
- 영속성 컨텍스트와 변경 감지 이해 지원
- Lazy Loading / Fetch Join / N+1 문제 분석 지원
- Transaction 경계와 Entity 상태 관리 지원
- Repository Query Method / JPQL / Projection 기준 제공
- DTO 변환과 Entity 노출 방지 기준 제공
- 데이터 무결성과 성능 문제 검출 지원
- JPA Anti Pattern 탐지 지원

---

### [핵심]

우선순위:

1. Entity Mapping
2. Primary Key Strategy
3. Column Mapping
4. Association Mapping
5. Owning Side
6. Lazy Loading
7. Persistence Context
8. Dirty Checking
9. Transaction Boundary
10. Repository
11. JPQL
12. Fetch Join
13. N+1 Problem
14. DTO Projection
15. Cascade
16. Orphan Removal
17. Auditing
18. Entity Lifecycle
19. Performance Review
20. JPA Anti Pattern

---

### [실무]

JPA Advanced 문서는 단순 Annotation 사용법 문서가 아니다.

Backend Agent가 아래 작업을 수행할 수 있도록 작성한다.

- Entity 설계 검토
- Table / Column Mapping 검토
- 연관관계 방향 결정
- 단방향 / 양방향 선택 기준 제공
- 연관관계 주인 판단
- Lazy Loading 문제 예측
- N+1 문제 탐지
- Fetch Join 적용 여부 판단
- Transaction 범위 검토
- Entity 변경 감지 동작 검토
- DTO 변환 위치 판단
- Repository Query Method 적절성 검토
- JPQL / QueryDSL 필요 여부 판단
- Cascade / orphanRemoval 사용 위험 검토
- Entity 직접 반환 Anti Pattern 탐지

---

### [FAQ]

Q. JPA Domain Rules는 Spring Boot Domain Rules와 뭐가 달라?

A.
Spring Boot Domain Rules는 Application Layer 구조 중심이고 JPA Domain Rules는 Entity, Mapping, Persistence Context, 연관관계, Query, 성능 문제를 다룬다.

Q. JPA에서 가장 중요한 기준은 뭐야?

A.
Entity Mapping, 연관관계 주인, Lazy Loading, Transaction 경계, N+1 문제, DTO 분리, Cascade 사용 기준이다.

Q. JPA는 SQL을 몰라도 쓸 수 있어?

A.
아니다. JPA는 SQL을 생성하는 ORM이므로 실제 SQL, Index, Join, Transaction 이해가 함께 필요하다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

JPA Advanced 문서는 Backend Foundation에서 JPA 실무 개발에 필요한 핵심 범위를 포함한다.

포함 범위:

- ORM Concept
- Entity Mapping
- Table Mapping
- Column Mapping
- Primary Key Strategy
- Entity Lifecycle
- Persistence Context
- First Level Cache
- Dirty Checking
- Flush
- Detach / Merge
- Association Mapping
- OneToMany
- ManyToOne
- OneToOne
- ManyToMany Caution
- Owning Side
- Lazy Loading
- Eager Loading Caution
- Fetch Join
- N+1 Problem
- Cascade
- Orphan Removal
- Embedded Value Type
- Enum Mapping
- Auditing
- Repository Query Method
- JPQL Basics
- Native Query Caution
- DTO Projection
- Pagination
- Transaction Boundary
- Entity to DTO Mapping
- Common JPA Anti Patterns

---

### [핵심]

반드시 포함:

- Entity는 DB Table과 매핑되는 Persistence Model
- Entity를 API Response로 직접 반환하지 않음
- 기본 Fetch 전략을 맹신하지 않음
- ManyToOne / OneToOne은 LAZY 명시 권장
- 양방향 연관관계는 필요한 경우에만 사용
- 연관관계 주인은 FK를 가진 쪽
- N+1 문제는 조회 시점에 반드시 검토
- Fetch Join은 필요한 조회에서만 사용
- Transaction 안에서 Entity 변경 감지가 동작
- Cascade는 생명주기가 완전히 종속될 때만 사용
- ManyToMany 직접 사용은 지양
- Repository에 비즈니스 로직을 넣지 않음

---

### [실무]

JPA 문서는 SQL / Java / Spring Boot / QueryDSL 문서와 함께 사용된다.

실무 연결:

```text
SQL
→ Java
→ Spring Boot
→ JPA Advanced
→ QueryDSL Practical
→ API Design
→ Testing
```

JPA 개발 흐름:

```text
Requirement
→ Entity Design
→ Association Design
→ Repository Design
→ Service Transaction
→ Query Strategy
→ DTO Mapping
→ Performance Review
```

---

### [FAQ]

Q. JPA 문서에서 QueryDSL도 깊게 다뤄?

A.
아니다. 동적 쿼리와 QueryDSL 문법은 QueryDSL Practical Domain Rules에서 다룬다.

Q. SQL 튜닝도 여기서 다뤄?

A.
JPA 관점의 N+1, Fetch Join, Pagination, Query 전략은 포함하지만 Index 설계와 SQL 튜닝 심화는 SQL Domain Rules에서 다룬다.

Q. Spring Transaction은 여기서 다뤄?

A.
JPA Entity 상태와 영속성 컨텍스트에 필요한 Transaction 기준은 포함하고 Spring Boot 일반 Transaction 규칙은 Spring Boot Domain Rules와 연결한다.

---

## 2.2 Excluded Scope

### [개념]

JPA Advanced 문서에서는 ORM 심화와 다른 전문 Domain 문서와 겹치는 범위를 제외한다.

제외 범위:

- QueryDSL 상세 문법
- 복잡한 SQL 튜닝 심화
- Database Index 설계 심화
- Multi Tenancy
- Hibernate Internal 심화
- Second Level Cache 심화
- Entity Graph 심화
- Batch Insert / Bulk Processing 심화
- Sharding
- CQRS
- Event Sourcing
- NoSQL Mapping
- Reactive Persistence
- R2DBC
- Distributed Transaction

---

### [핵심]

제외 이유:

- Foundation 범위 유지
- Agent Retrieval 혼선 방지
- SQL / QueryDSL / Performance / Expert Rules와 책임 분리
- Chunk 품질 유지
- Entity Mapping과 실무 JPA 문제 해결에 집중

---

### [실무]

고급 기술은 별도 Domain Rules로 분리한다.

예:

```text
JPA Advanced
→ QueryDSL Practical
→ SQL Performance
→ Advanced Spring Architecture
→ MSA
```

---

### [FAQ]

Q. Hibernate 내부 구조까지 다뤄?

A.
아니다. 실무 개발에 필요한 영속성 컨텍스트, Lazy Loading, Flush, Dirty Checking 수준을 우선한다.

Q. Second Level Cache는 여기서 다뤄?

A.
기초 언급은 가능하지만 캐시 전략 심화는 별도 고급 성능 문서가 적합하다.

Q. Bulk Update는 여기서 다뤄?

A.
주의사항은 포함할 수 있지만 대량 처리 심화는 고급 성능 또는 QueryDSL 문서에서 다루는 것이 좋다.

---

# 3. Section Priority

## 3.1 Required Sections

### [개념]

JPA RAG 문서는 모든 주요 Chunk에 아래 Section을 우선 포함한다.

Required:

- [개념]
- [핵심]
- [실무]
- [FAQ]

---

### [핵심]

필수 Section 목적:

- [개념]: 정의와 역할
- [핵심]: 검색 친화 키워드
- [실무]: 실제 Entity / Query 설계 기준
- [FAQ]: 사용자 질문 매칭 강화

---

### [실무]

각 문서는 아래 구조를 기본으로 한다.

```md
# Topic

## Sub Topic

### [개념]

### [핵심]

### [실무]

### [FAQ]
```

---

### [FAQ]

Q. JPA 문서에도 FAQ가 필요해?

A.
필요하다. Entity, Lazy Loading, N+1, Transaction, DTO, Cascade 같은 질문과 RAG 검색 매칭을 강화한다.

Q. [면접] 섹션을 써도 돼?

A.
안 된다. 반드시 [FAQ] 섹션을 사용한다.

---

## 3.2 Recommended Sections

### [개념]

JPA 문서에는 Mapping과 Query 문제를 분석하기 위해 추가 Section을 포함할 수 있다.

Strongly Recommended:

- [Flow]
- [예제]
- [주의]
- [Best Practice]
- [Troubleshooting]
- [Checklist]
- [Comparison]

---

### [핵심]

추천 Section 사용 기준:

- Persistence Context 설명 → [Flow]
- 연관관계 설명 → [Comparison], [주의]
- N+1 문제 설명 → [Troubleshooting], [예제]
- Transaction 설명 → [Flow], [주의]
- Cascade 설명 → [주의]
- Entity 설계 검수 → [Checklist]

---

### [실무]

예시:

```md
### [Flow]

Service Method Start
→ Transaction Begin
→ Entity 조회
→ Persistence Context 관리
→ Entity 변경
→ Flush
→ Commit
```

---

### [FAQ]

Q. JPA 문서에 Flow가 중요한 이유는?

A.
영속성 컨텍스트, 변경 감지, Flush, Transaction 동작은 흐름으로 이해해야 오류를 추적하기 쉽다.

Q. Comparison이 필요한 이유는?

A.
Entity와 DTO, Lazy와 Eager, Cascade와 orphanRemoval, Fetch Join과 일반 Join처럼 혼동되는 개념이 많기 때문이다.

---

# 4. ORM and Entity Rules

## 4.1 ORM Concept Rules

### [개념]

ORM(Object Relational Mapping)은 객체와 관계형 데이터베이스 테이블을 매핑하는 기술이다.

JPA는 Java ORM 표준이고 Hibernate는 대표 구현체다.

---

### [핵심]

핵심 키워드:

- ORM
- JPA
- Hibernate
- Entity
- Table Mapping
- Object Model
- Relational Model
- Persistence Context
- SQL Generation

---

### [실무]

JPA 사용 시 Agent는 아래를 함께 검토한다.

```text
객체 모델 설계
→ 테이블 구조와 매핑
→ 연관관계 설계
→ 생성 SQL 예측
→ 조회 SQL 예측
→ 성능 문제 검토
```

주의:

- JPA를 사용해도 SQL 이해 필요
- Entity 설계가 DB 구조와 완전히 독립적일 수 없음
- 객체 그래프 탐색이 실제 SQL을 발생시킬 수 있음
- 편의성보다 명확한 Query 전략이 중요

---

### [FAQ]

Q. JPA는 SQL을 안 써도 되는 기술이야?

A.
아니다. SQL을 직접 덜 작성하게 해주지만 내부적으로 SQL이 생성되므로 SQL 동작을 이해해야 한다.

Q. JPA와 Hibernate는 같은 거야?

A.
JPA는 표준 인터페이스이고 Hibernate는 JPA 구현체다.

---

## 4.2 Entity Design Rules

### [개념]

Entity는 DB Table과 매핑되는 Persistence Model이다.

Entity는 API 입출력 객체가 아니라 도메인 데이터와 DB 저장 구조를 표현한다.

---

### [핵심]

Entity 구성:

- @Entity
- @Table
- @Id
- @GeneratedValue
- @Column
- Field
- Constructor
- Business Method
- Association
- protected no-args constructor

---

### [실무]

예:

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

권장:

- 기본 생성자는 protected
- Setter 무분별 사용 지양
- 의미 있는 생성 메서드 사용
- Entity 내부에 상태 변경 메서드 제공
- API 응답을 위한 필드 추가 금지
- 비즈니스 규칙과 무관한 편의 필드 주의

---

### [FAQ]

Q. Entity에 Setter를 전부 열어도 돼?

A.
권장하지 않는다. 상태 변경 의도가 드러나는 메서드를 만들어 변경 경로를 통제하는 것이 좋다.

Q. Entity 기본 생성자는 왜 필요해?

A.
JPA가 Reflection으로 Entity를 생성하기 위해 기본 생성자가 필요하다. 외부 생성을 막기 위해 protected로 두는 경우가 많다.

---

## 4.3 DTO and Entity Separation Rules

### [개념]

DTO와 Entity 분리는 API 입출력 모델과 Persistence Model을 분리하는 규칙이다.

---

### [핵심]

분리 이유:

- Entity 직접 노출 방지
- API 변경과 DB 변경 분리
- 민감정보 노출 방지
- Lazy Loading 문제 방지
- 순환 참조 방지
- 응답 필드 제어
- Validation 분리

---

### [실무]

나쁜 예:

```java
@GetMapping("/{id}")
public Post getPost(@PathVariable Long id) {
    return postRepository.findById(id).orElseThrow();
}
```

좋은 예:

```java
@GetMapping("/{id}")
public PostResponse getPost(@PathVariable Long id) {
    return postService.getPost(id);
}
```

DTO 변환:

```java
public record PostResponse(Long postId, String title, String content) {

    public static PostResponse from(Post post) {
        return new PostResponse(
                post.getPostId(),
                post.getTitle(),
                post.getContent()
        );
    }
}
```

---

### [FAQ]

Q. Entity를 Controller에서 바로 반환하면 왜 안 돼?

A.
민감정보 노출, Lazy Loading, 순환 참조, API 스펙 변경 위험이 생길 수 있다.

Q. Entity와 DTO 변환은 어디서 해?

A.
간단한 변환은 DTO의 static from 메서드 또는 Service에서 처리할 수 있다. 프로젝트 규칙으로 일관화하는 것이 중요하다.

---

# 5. Primary Key and Column Mapping Rules

## 5.1 Primary Key Strategy Rules

### [개념]

Primary Key Strategy는 Entity 식별자를 DB에서 어떻게 생성하고 관리할지 결정하는 기준이다.

---

### [핵심]

주요 전략:

- GenerationType.IDENTITY
- GenerationType.SEQUENCE
- GenerationType.AUTO
- GenerationType.TABLE
- UUID
- Natural Key Caution
- Surrogate Key

---

### [실무]

예:

```java
@Id
@GeneratedValue(strategy = GenerationType.IDENTITY)
private Long userId;
```

권장:

- 대부분 Long surrogate key 사용
- 비즈니스 값은 Primary Key로 사용 지양
- DB 종류에 맞는 생성 전략 선택
- 식별자는 변경하지 않음
- equals / hashCode에서 식별자 사용 시 주의

주의:

- IDENTITY는 insert 시점에 ID 생성
- SEQUENCE는 DB sequence 기반
- AUTO는 DB와 구현체에 따라 달라질 수 있음
- 이메일, 전화번호 같은 값은 변경 가능하므로 PK 지양

---

### [FAQ]

Q. JPA Entity ID는 뭘 쓰는 게 좋아?

A.
대부분 Long 타입의 surrogate key를 사용하고 DB 전략에 맞게 IDENTITY나 SEQUENCE를 선택한다.

Q. 이메일을 Primary Key로 써도 돼?

A.
권장하지 않는다. 이메일은 변경될 수 있는 비즈니스 값이므로 별도 unique column으로 두는 것이 좋다.

---

## 5.2 Column Mapping Rules

### [개념]

Column Mapping은 Entity Field를 DB Column에 연결하고 제약 조건을 표현하는 규칙이다.

---

### [핵심]

주요 Annotation:

- @Column
- nullable
- length
- unique
- columnDefinition
- precision
- scale
- @Enumerated
- @Lob
- @Temporal Legacy Caution

---

### [실무]

예:

```java
@Column(nullable = false, length = 100)
private String title;

@Column(nullable = false, columnDefinition = "TEXT")
private String content;

@Column(nullable = false, unique = true)
private String email;
```

권장:

- nullable 명확화
- 문자열 길이 명확화
- unique는 DB 제약과 함께 검토
- 대용량 문자열은 TEXT 전략 검토
- 숫자 정밀도는 BigDecimal과 precision / scale 검토
- LocalDate / LocalDateTime 사용 권장

---

### [FAQ]

Q. @Column(nullable = false)는 꼭 써야 해?

A.
필수는 아니지만 DB 무결성과 코드 의도를 명확히 하기 위해 중요한 필드는 명시하는 것이 좋다.

Q. unique = true만 쓰면 충분해?

A.
간단한 경우는 가능하지만 운영 DB 제약, 중복 검증, 예외 처리까지 함께 고려해야 한다.

---

## 5.3 Enum Mapping Rules

### [개념]

Enum Mapping은 Java Enum 값을 DB Column에 저장하는 방식이다.

---

### [핵심]

사용 방식:

- @Enumerated(EnumType.STRING)
- EnumType.ORDINAL Caution
- Status Field
- Code Field
- Display Name Separation

---

### [실무]

예:

```java
@Enumerated(EnumType.STRING)
@Column(nullable = false)
private PostStatus status;
```

권장:

- EnumType.STRING 우선
- ORDINAL 사용 지양
- 화면 표시명과 DB 저장값 분리
- 상태 전환 메서드에서 검증
- Enum 이름 변경 시 DB 영향 주의

주의:

- ORDINAL은 enum 순서 변경 시 데이터 의미가 깨질 수 있음
- STRING은 저장 공간이 더 들지만 의미가 명확함
- 상태 값은 enum으로 표현하면 오타를 줄일 수 있음

---

### [FAQ]

Q. Enum은 ORDINAL로 저장해도 돼?

A.
권장하지 않는다. enum 순서가 바뀌면 기존 데이터 의미가 깨질 수 있으므로 STRING을 우선한다.

Q. 상태값은 String으로 둬도 돼?

A.
가능하지만 정해진 값 집합이면 Enum을 사용해 오타와 잘못된 상태를 줄이는 것이 좋다.

---

# 6. Association Mapping Rules

## 6.1 Association Design Rules

### [개념]

Association Mapping은 Entity 간 관계를 객체 참조와 DB Foreign Key로 연결하는 규칙이다.

---

### [핵심]

관계 종류:

- @ManyToOne
- @OneToMany
- @OneToOne
- @ManyToMany
- @JoinColumn
- mappedBy
- owning side
- inverse side
- foreign key

---

### [실무]

연관관계 설계 순서:

```text
DB FK 위치 확인
→ 객체 탐색 방향 결정
→ 단방향으로 충분한지 확인
→ 양방향 필요 여부 확인
→ 연관관계 주인 설정
→ Fetch 전략 설정
→ Cascade 필요 여부 확인
```

권장:

- 기본은 단방향부터 시작
- 양방향은 실제 탐색 필요가 있을 때만 사용
- ManyToOne 쪽이 FK를 가지는 경우가 많음
- 연관관계 주인은 FK를 가진 쪽
- ManyToMany 직접 사용 지양
- FetchType.LAZY 명시 고려

---

### [FAQ]

Q. JPA 연관관계는 무조건 양방향으로 해야 해?

A.
아니다. 단방향으로 충분하면 단방향이 단순하고 유지보수에 좋다.

Q. 연관관계 주인은 어떻게 정해?

A.
DB Foreign Key를 가진 Entity가 연관관계 주인이 된다.

---

## 6.2 ManyToOne Rules

### [개념]

ManyToOne은 여러 Entity가 하나의 Entity를 참조하는 관계다.

DB에서는 Many 쪽 Table이 Foreign Key를 가진다.

---

### [핵심]

사용 예:

- Post → User
- Comment → Post
- OrderItem → Order
- Review → User
- Favorite → Festival

---

### [실무]

예:

```java
@ManyToOne(fetch = FetchType.LAZY)
@JoinColumn(name = "user_id", nullable = false)
private User user;
```

권장:

- FetchType.LAZY 명시
- JoinColumn 이름 명확화
- nullable 기준 명확화
- FK를 가진 쪽이 연관관계 주인
- Response DTO 변환 시 Lazy Loading 주의
- 필요한 조회는 Fetch Join 검토

주의:

- ManyToOne 기본 Fetch는 EAGER이므로 LAZY 명시 권장
- user.getName() 접근 시 Lazy Loading 발생 가능
- Transaction 밖 Lazy Loading 접근 주의

---

### [FAQ]

Q. ManyToOne은 왜 LAZY를 명시해?

A.
ManyToOne 기본 Fetch는 EAGER라 불필요한 Join과 조회가 발생할 수 있으므로 LAZY를 명시하는 것이 좋다.

Q. ManyToOne에서 JoinColumn은 어디에 둬?

A.
Foreign Key를 가진 Many 쪽 Entity에 둔다.

---

## 6.3 OneToMany Rules

### [개념]

OneToMany는 하나의 Entity가 여러 자식 Entity Collection을 참조하는 관계다.

---

### [핵심]

사용 예:

- User → Posts
- Post → Comments
- Order → OrderItems
- Festival → Reviews

---

### [실무]

양방향 예:

```java
@OneToMany(mappedBy = "post")
private List<Comment> comments = new ArrayList<>();
```

권장:

- mappedBy로 연관관계 주인이 아님을 표시
- Collection은 빈 컬렉션으로 초기화
- 무분별한 OneToMany 조회 주의
- Collection 직접 노출 지양
- 페이징이 필요한 자식 목록은 Repository Query로 조회 고려
- Cascade / orphanRemoval은 신중히 적용

주의:

- OneToMany Collection을 Fetch Join하면 중복 row와 Pagination 문제가 발생할 수 있음
- 큰 Collection을 Entity에서 직접 탐색하는 방식은 성능 문제 가능
- 자식 목록 API는 별도 Repository Query가 더 적합할 수 있음

---

### [FAQ]

Q. OneToMany에는 mappedBy를 왜 써?

A.
상대 Entity가 Foreign Key를 가진 연관관계 주인임을 표시하기 위해 사용한다.

Q. OneToMany 컬렉션을 바로 반환해도 돼?

A.
권장하지 않는다. DTO로 변환하고 큰 목록은 별도 Query와 Pagination을 고려해야 한다.

---

## 6.4 OneToOne Rules

### [개념]

OneToOne은 하나의 Entity가 하나의 Entity와 연결되는 관계다.

---

### [핵심]

사용 예:

- User → UserProfile
- Order → Payment
- Member → Locker

---

### [실무]

예:

```java
@OneToOne(fetch = FetchType.LAZY)
@JoinColumn(name = "profile_id")
private UserProfile profile;
```

권장:

- FK 위치를 명확히 결정
- 연관관계 주인 확인
- FetchType.LAZY 명시 고려
- 실제로 OneToOne이 필요한지 검토
- 같은 생명주기면 Embedded도 검토 가능

주의:

- OneToOne 기본 Fetch는 EAGER
- Lazy가 기대대로 동작하지 않을 수 있는 상황 주의
- 테이블 분리 필요성이 약하면 같은 Entity에 포함 가능

---

### [FAQ]

Q. OneToOne은 언제 써?

A.
두 데이터가 독립 테이블로 분리되어야 하고 1:1 관계가 명확할 때 사용한다.

Q. OneToOne도 LAZY를 써야 해?

A.
불필요한 즉시 로딩을 막기 위해 LAZY를 고려하지만 구현체 제약으로 기대와 다르게 동작할 수 있어 조회 SQL을 확인해야 한다.

---

## 6.5 ManyToMany Caution Rules

### [개념]

ManyToMany는 양쪽 Entity가 서로 여러 개를 참조하는 관계다.

실무에서는 중간 Entity를 명시적으로 만들어 ManyToOne / OneToMany로 풀어내는 것이 일반적이다.

---

### [핵심]

문제:

- 중간 테이블에 추가 필드 넣기 어려움
- 관계 자체를 Entity로 다루기 어려움
- Cascade 위험
- Query 확장 어려움
- 실무 요구사항 변경에 취약

---

### [실무]

비권장:

```java
@ManyToMany
private List<Tag> tags = new ArrayList<>();
```

권장 구조:

```text
Post
→ PostTag
→ Tag
```

예:

```java
@Entity
public class PostTag {

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "post_id")
    private Post post;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "tag_id")
    private Tag tag;
}
```

---

### [FAQ]

Q. ManyToMany를 바로 쓰면 안 돼?

A.
가능은 하지만 실무에서는 중간 테이블에 생성일, 상태 같은 추가 필드가 필요한 경우가 많아 중간 Entity로 풀어내는 것이 좋다.

Q. 좋아요, 찜 같은 관계는 ManyToMany야?

A.
개념적으로는 다대다지만 Like, Favorite 같은 중간 Entity로 표현하는 것이 실무에 적합하다.

---

## 6.6 Owning Side Rules

### [개념]

Owning Side는 JPA 연관관계에서 Foreign Key 값을 실제로 관리하는 쪽이다.

---

### [핵심]

판단 기준:

- DB Foreign Key를 가진 쪽
- @JoinColumn이 있는 쪽
- mappedBy가 없는 쪽
- 관계 변경 SQL에 반영되는 쪽

---

### [실무]

예:

```java
// 연관관계 주인
@ManyToOne(fetch = FetchType.LAZY)
@JoinColumn(name = "post_id")
private Post post;

// 반대편
@OneToMany(mappedBy = "post")
private List<Comment> comments = new ArrayList<>();
```

주의:

- mappedBy 쪽만 변경하면 FK가 반영되지 않음
- 양방향 편의 메서드로 양쪽 값을 맞춤
- 주인은 DB FK 기준이지 객체 참조 방향 기준이 아님

편의 메서드 예:

```java
public void addComment(Comment comment) {
    comments.add(comment);
    comment.changePost(this);
}
```

---

### [FAQ]

Q. mappedBy가 있는 쪽이 주인이야?

A.
아니다. mappedBy가 있는 쪽은 연관관계 주인이 아니며 FK를 직접 관리하지 않는다.

Q. 양방향 관계에서 한쪽만 세팅해도 돼?

A.
DB 반영은 주인 쪽이 기준이지만 객체 상태 일관성을 위해 양쪽을 함께 맞추는 편의 메서드를 사용하는 것이 좋다.

---

# 7. Persistence Context Rules

## 7.1 Persistence Context Basics

### [개념]

Persistence Context는 Entity를 관리하는 JPA의 1차 캐시이자 Entity 상태 추적 공간이다.

같은 Transaction 안에서 조회한 Entity는 영속성 컨텍스트에 의해 관리된다.

---

### [핵심]

핵심 개념:

- EntityManager
- Persistence Context
- Managed Entity
- First Level Cache
- Identity Guarantee
- Dirty Checking
- Flush
- Detach
- Merge
- Transaction

---

### [실무]

흐름:

```text
Transaction Begin
→ Entity 조회
→ Persistence Context 저장
→ Entity 변경
→ Dirty Checking
→ Flush
→ Commit
```

특징:

- 같은 ID Entity는 같은 객체로 관리
- 변경 감지는 영속 상태 Entity에만 적용
- Transaction 종료 후 Entity는 준영속 상태가 될 수 있음
- Lazy Loading은 영속성 컨텍스트와 Transaction 범위에 영향받음

---

### [FAQ]

Q. 영속성 컨텍스트가 뭐야?

A.
JPA가 Entity를 관리하는 공간이며 1차 캐시, 동일성 보장, 변경 감지 같은 기능을 제공한다.

Q. Entity를 변경했는데 save를 다시 안 해도 돼?

A.
Transaction 안의 영속 상태 Entity라면 Dirty Checking으로 변경 사항이 반영될 수 있다.

---

## 7.2 Entity Lifecycle Rules

### [개념]

Entity Lifecycle은 Entity가 JPA에서 어떤 상태로 관리되는지 나타낸다.

---

### [핵심]

Entity 상태:

- Transient
- Managed
- Detached
- Removed

---

### [실무]

상태 흐름:

```text
new Entity()
→ Transient

entityManager.persist(entity)
→ Managed

transaction commit / clear / close
→ Detached

entityManager.remove(entity)
→ Removed
```

주의:

- new로 만든 객체는 아직 DB와 무관
- persist 후 영속 상태
- Transaction 밖 Entity는 Lazy Loading 실패 가능
- merge는 detached entity를 다시 managed로 복사
- remove는 영속 상태 Entity에 적용

---

### [FAQ]

Q. 준영속 상태가 뭐야?

A.
한때 영속성 컨텍스트가 관리했지만 현재는 분리되어 JPA가 변경을 추적하지 않는 상태다.

Q. Detached Entity를 수정하면 DB에 반영돼?

A.
그 자체로는 반영되지 않는다. 다시 영속 상태로 만들거나 Transaction 안에서 조회한 Entity를 수정해야 한다.

---

## 7.3 Dirty Checking Rules

### [개념]

Dirty Checking은 Transaction 안에서 영속 상태 Entity의 변경을 감지해 DB Update SQL을 생성하는 기능이다.

---

### [핵심]

동작 조건:

- Entity가 Managed 상태
- Transaction 범위 안
- 변경 전 Snapshot 존재
- Flush 시점에 변경 감지
- Commit 시 Flush 발생 가능

---

### [실무]

예:

```java
@Transactional
public void updatePost(Long postId, PostUpdateRequest request) {
    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

    post.update(request.title(), request.content());
}
```

권장:

- Entity 상태 변경 메서드 사용
- update 후 무조건 save 호출하지 않음
- Transaction 범위 확인
- 변경 대상 Entity가 영속 상태인지 확인
- Bulk Update와 Dirty Checking 차이 이해

---

### [FAQ]

Q. JPA update 할 때 save를 꼭 해야 해?

A.
Transaction 안에서 조회한 영속 Entity를 변경하면 Dirty Checking으로 반영될 수 있어 save가 필수는 아니다.

Q. Dirty Checking이 안 되면 뭘 확인해?

A.
@Transactional 범위, Entity 영속 상태, 조회 방식, Transaction 종료 시점, 변경 메서드 호출 여부를 확인한다.

---

## 7.4 Flush Rules

### [개념]

Flush는 영속성 컨텍스트의 변경 내용을 DB에 SQL로 반영하는 과정이다.

Flush는 Commit과 같지 않다.

---

### [핵심]

Flush 발생 시점:

- Transaction Commit
- JPQL Query 실행 전
- entityManager.flush()
- FlushMode 설정에 따른 시점

---

### [실무]

주의:

- Flush는 DB에 SQL을 보내지만 Transaction Commit은 아님
- Flush 후 Rollback 가능
- JPQL 실행 전 Flush로 인해 예상보다 빨리 SQL 발생 가능
- Bulk Query 전후 영속성 컨텍스트 상태 주의
- 테스트에서 flush로 제약조건 오류를 빨리 확인 가능

---

### [FAQ]

Q. Flush와 Commit은 같은 거야?

A.
아니다. Flush는 SQL을 DB에 반영하는 과정이고 Commit은 Transaction을 확정하는 과정이다.

Q. JPQL 전에 Flush가 일어나는 이유는?

A.
Query 결과가 영속성 컨텍스트 변경 내용과 일치하도록 하기 위해 Flush가 발생할 수 있다.

---

# 8. Fetch Strategy and N+1 Rules

## 8.1 Lazy Loading Rules

### [개념]

Lazy Loading은 연관 Entity를 실제 사용하는 시점에 조회하는 전략이다.

---

### [핵심]

관련 개념:

- FetchType.LAZY
- Proxy
- Persistence Context
- Transaction
- LazyInitializationException
- N+1 Problem
- DTO Mapping

---

### [실무]

권장:

```java
@ManyToOne(fetch = FetchType.LAZY)
@JoinColumn(name = "user_id")
private User user;
```

주의:

- Transaction 밖에서 Lazy Loading 접근 시 예외 가능
- DTO 변환 시 연관 Entity 접근으로 추가 SQL 발생 가능
- 단순히 LAZY로 바꾼다고 N+1이 사라지는 것은 아님
- 필요한 조회에서는 Fetch Join 또는 Projection 검토

---

### [FAQ]

Q. Lazy Loading은 무조건 좋아?

A.
아니다. 불필요한 즉시 조회를 줄일 수 있지만 잘못 사용하면 N+1 문제나 LazyInitializationException이 발생할 수 있다.

Q. LazyInitializationException은 왜 발생해?

A.
영속성 컨텍스트가 닫힌 뒤 Lazy 연관 객체에 접근했기 때문이다.

---

## 8.2 Eager Loading Caution Rules

### [개념]

Eager Loading은 Entity 조회 시 연관 Entity를 즉시 함께 조회하는 전략이다.

---

### [핵심]

문제:

- 예상치 못한 Join
- 불필요한 데이터 조회
- 복잡한 SQL 생성
- N+1 문제 발생 가능
- 성능 제어 어려움

---

### [실무]

권장:

- 기본 전략을 EAGER에 의존하지 않음
- ManyToOne / OneToOne은 LAZY 명시 고려
- 필요한 조회는 Fetch Join으로 명시
- API별 조회 전략을 Repository Query에서 결정
- Entity Mapping은 기본적으로 보수적으로 설계

---

### [FAQ]

Q. EAGER면 N+1 문제가 없어져?

A.
아니다. EAGER도 조회 방식에 따라 추가 쿼리가 발생할 수 있고 제어하기 어려운 성능 문제가 생길 수 있다.

Q. FetchType은 어떻게 정해?

A.
기본은 LAZY로 두고 필요한 API 조회에서 Fetch Join이나 Projection으로 명시적으로 가져오는 방식이 좋다.

---

## 8.3 N+1 Problem Rules

### [개념]

N+1 Problem은 목록 1번 조회 후 각 Row의 연관 Entity를 조회하기 위해 N번 추가 Query가 발생하는 문제다.

---

### [핵심]

발생 상황:

- List 조회
- 연관 Entity 접근
- Lazy Loading
- Eager Loading
- DTO 변환 중 연관 객체 접근
- 반복문 내부 getter 호출

---

### [실무]

문제 예:

```java
List<Post> posts = postRepository.findAll();

for (Post post : posts) {
    String nickname = post.getUser().getNickname();
}
```

흐름:

```text
Post 목록 조회 1번
→ 각 Post의 User 조회 N번
→ 총 1 + N Query 발생
```

해결 후보:

- Fetch Join
- EntityGraph
- DTO Projection
- Batch Size
- QueryDSL Projection
- API 응답 구조 재검토

---

### [FAQ]

Q. N+1 문제는 어떻게 찾는 게 좋아?

A.
SQL 로그를 켜고 목록 조회 후 반복문이나 DTO 변환 과정에서 연관 Entity 조회가 반복되는지 확인한다.

Q. N+1 문제는 무조건 Fetch Join으로 해결해?

A.
아니다. Fetch Join, DTO Projection, Batch Size, API 구조 변경 중 상황에 맞게 선택한다.

---

## 8.4 Fetch Join Rules

### [개념]

Fetch Join은 JPQL에서 연관 Entity를 함께 조회해 Lazy Loading에 따른 추가 Query를 줄이는 방법이다.

---

### [핵심]

사용 대상:

- 필요한 연관 Entity 함께 조회
- N+1 문제 해결
- 단건 상세 조회
- ManyToOne 연관 조회
- OneToOne 연관 조회
- 제한적 OneToMany 조회

---

### [실무]

예:

```java
@Query("""
    select p
    from Post p
    join fetch p.user
    where p.postId = :postId
""")
Optional<Post> findByIdWithUser(Long postId);
```

주의:

- Collection Fetch Join과 Pagination 함께 사용 주의
- 중복 Row 발생 가능
- distinct 필요 가능
- 여러 Collection Fetch Join 위험
- 필요한 API에서만 사용
- 무분별한 Fetch Join은 과도한 데이터 조회

---

### [FAQ]

Q. Fetch Join은 언제 써?

A.
특정 조회에서 연관 Entity가 반드시 필요하고 Lazy Loading으로 추가 Query가 많이 발생할 때 사용한다.

Q. Collection Fetch Join에 Pagination을 같이 써도 돼?

A.
주의해야 한다. DB Pagination이 기대대로 동작하지 않거나 메모리에서 처리될 수 있어 별도 전략을 검토해야 한다.

---

# 9. Repository and Query Rules

## 9.1 Spring Data JPA Repository Rules

### [개념]

Spring Data JPA Repository는 Entity의 CRUD와 Query Method를 쉽게 작성할 수 있게 해주는 추상화다.

---

### [핵심]

기본 Interface:

- JpaRepository
- CrudRepository
- PagingAndSortingRepository
- Query Method
- @Query
- Optional
- Page
- Slice

---

### [실무]

예:

```java
public interface PostRepository extends JpaRepository<Post, Long> {

    Optional<Post> findByPostIdAndDeletedFalse(Long postId);

    boolean existsByTitle(String title);

    Slice<Post> findByUser_UserIdOrderByCreatedAtDesc(Long userId, Pageable pageable);
}
```

권장:

- 단건 조회 실패 가능성은 Optional
- 존재 여부는 existsBy
- 목록은 List / Page / Slice 기준 명확화
- Query Method가 너무 길면 @Query 또는 QueryDSL 검토
- Repository는 Entity 조회 중심
- 비즈니스 로직은 Service에서 처리

---

### [FAQ]

Q. Repository Query Method는 언제 써?

A.
조건이 단순하고 메서드 이름이 과도하게 길어지지 않을 때 적합하다.

Q. Optional은 Repository에서만 쓰는 게 좋아?

A.
주로 Repository 단건 조회 결과에 사용하고 Service에서 처리해 Controller까지 그대로 노출하지 않는 것이 좋다.

---

## 9.2 JPQL Rules

### [개념]

JPQL은 Entity 객체와 필드를 기준으로 작성하는 객체 지향 Query Language다.

SQL처럼 Table과 Column이 아니라 Entity와 Field를 사용한다.

---

### [핵심]

특징:

- Entity 기준 Query
- Field 기준 접근
- Join 가능
- Fetch Join 가능
- DTO Projection 가능
- Native SQL과 다름

---

### [실무]

예:

```java
@Query("""
    select p
    from Post p
    where p.title like concat('%', :keyword, '%')
    order by p.createdAt desc
""")
List<Post> searchByKeyword(String keyword);
```

주의:

- Table 이름이 아니라 Entity 이름 사용
- Column 이름이 아니라 Field 이름 사용
- 동적 조건이 많으면 QueryDSL 검토
- Fetch Join 사용 시 Pagination 주의
- 복잡한 Query는 SQL 로그 확인

---

### [FAQ]

Q. JPQL은 SQL이랑 뭐가 달라?

A.
JPQL은 Table과 Column이 아니라 Entity와 Field를 기준으로 작성하고 JPA가 SQL로 변환한다.

Q. 동적 검색 조건이 많으면 JPQL로 해도 돼?

A.
가능하지만 조건 조합이 많아지면 QueryDSL이 더 적합할 수 있다.

---

## 9.3 Native Query Caution Rules

### [개념]

Native Query는 DB SQL을 직접 작성해 실행하는 방식이다.

JPA 추상화로 표현하기 어려운 DB 특화 Query에 사용할 수 있다.

---

### [핵심]

사용 후보:

- DB specific function
- 복잡한 SQL
- 성능 튜닝 SQL
- Window Function
- Recursive Query
- Vendor specific feature

---

### [실무]

주의:

- DB 종속성 증가
- Entity Mapping과 불일치 위험
- Pagination count query 별도 필요 가능
- 컬럼 alias와 DTO 매핑 주의
- 유지보수 비용 증가
- 가능하면 JPQL / QueryDSL 우선 검토

예:

```java
@Query(value = """
    select *
    from posts
    where title like concat('%', :keyword, '%')
""", nativeQuery = true)
List<Post> searchNative(String keyword);
```

---

### [FAQ]

Q. Native Query는 언제 써?

A.
JPQL이나 QueryDSL로 표현하기 어렵거나 DB 특화 기능이 필요한 경우에 사용한다.

Q. Native Query를 많이 쓰면 문제야?

A.
DB 종속성과 유지보수 비용이 커질 수 있어 필요한 경우에만 사용하는 것이 좋다.

---

## 9.4 DTO Projection Rules

### [개념]

DTO Projection은 Entity 전체가 아니라 필요한 필드만 조회해 DTO로 반환하는 방식이다.

---

### [핵심]

사용 상황:

- 목록 화면
- read-only 조회
- 필요한 필드가 적음
- 연관 Entity 전체 로딩 불필요
- 성능 최적화
- API Response 전용 조회

---

### [실무]

JPQL 생성자 Projection 예:

```java
@Query("""
    select new com.example.post.PostSummaryResponse(
        p.postId,
        p.title,
        u.nickname
    )
    from Post p
    join p.user u
    order by p.createdAt desc
""")
List<PostSummaryResponse> findPostSummaries();
```

권장:

- 목록 조회는 Projection 고려
- 변경 로직에는 Entity 조회 사용
- DTO 패키지 경로 변경에 주의
- 복잡한 Projection은 QueryDSL 검토
- 필요한 필드만 조회해 성능 개선 가능

---

### [FAQ]

Q. DTO Projection은 언제 써?

A.
읽기 전용 목록이나 화면 응답에서 Entity 전체가 필요하지 않을 때 사용한다.

Q. 수정 작업에도 DTO Projection을 써도 돼?

A.
수정 작업은 Entity 상태 변경이 필요하므로 Entity를 조회하는 것이 일반적이다.

---

# 10. Transaction and Entity State Rules

## 10.1 JPA Transaction Boundary Rules

### [개념]

JPA Transaction Boundary는 Entity 조회, 변경 감지, Lazy Loading, Flush가 동작하는 범위를 결정한다.

---

### [핵심]

기준:

- Service public method
- @Transactional
- readOnly
- Persistence Context
- Dirty Checking
- Lazy Loading
- Flush
- Commit
- Rollback

---

### [실무]

권장:

```java
@Transactional
public void updateUser(Long userId, UserUpdateRequest request) {
    User user = userRepository.findById(userId)
            .orElseThrow(() -> new BusinessException("USER_NOT_FOUND", "사용자를 찾을 수 없습니다."));

    user.updateNickname(request.nickname());
}
```

조회:

```java
@Transactional(readOnly = true)
public UserResponse getUser(Long userId) {
    User user = userRepository.findById(userId)
            .orElseThrow(() -> new BusinessException("USER_NOT_FOUND", "사용자를 찾을 수 없습니다."));

    return UserResponse.from(user);
}
```

주의:

- Entity 변경은 Transaction 안에서 수행
- DTO 변환 중 Lazy Loading이 필요하면 Transaction 범위 고려
- Controller에서 Lazy 객체 접근 지양
- Open Session In View 의존 지양
- readOnly는 변경 작업에 사용하지 않음

---

### [FAQ]

Q. JPA에서 @Transactional은 왜 중요해?

A.
영속성 컨텍스트, Dirty Checking, Lazy Loading, Flush가 Transaction 범위와 밀접하게 연결되기 때문이다.

Q. Controller에서 Entity를 DTO로 변환해도 돼?

A.
권장하지 않는다. Lazy Loading과 책임 분리 문제를 피하기 위해 Service Transaction 범위 안에서 변환하는 것이 좋다.

---

## 10.2 ReadOnly Transaction Rules

### [개념]

ReadOnly Transaction은 조회 작업에서 변경 감지 부담을 줄이고 읽기 의도를 명확히 하는 Transaction 설정이다.

---

### [핵심]

사용 대상:

- 단순 조회
- 상세 조회
- 목록 조회
- Projection 조회
- read-only Service Method

---

### [실무]

예:

```java
@Transactional(readOnly = true)
public List<PostResponse> getPosts() {
    return postRepository.findAll().stream()
            .map(PostResponse::from)
            .toList();
}
```

주의:

- readOnly에서 Entity 변경 기대 금지
- DB / Driver / JPA Provider에 따라 최적화 동작 차이 가능
- 조회 메서드 의도 표현에 유용
- Lazy Loading이 필요한 조회 범위 설정에 도움

---

### [FAQ]

Q. 조회 메서드에 readOnly = true를 왜 붙여?

A.
조회 의도를 명확히 하고 변경 감지 부담을 줄이는 데 도움이 될 수 있다.

Q. readOnly Transaction 안에서 Entity를 변경하면 반영돼?

A.
기대하지 않는 것이 좋다. 변경 작업은 일반 Transaction에서 수행해야 한다.

---

# 11. Cascade and Orphan Removal Rules

## 11.1 Cascade Rules

### [개념]

Cascade는 부모 Entity의 영속성 작업을 자식 Entity에도 전파하는 설정이다.

---

### [핵심]

Cascade 종류:

- PERSIST
- MERGE
- REMOVE
- REFRESH
- DETACH
- ALL

---

### [실무]

사용 후보:

- 부모와 자식 생명주기가 완전히 같음
- 자식이 부모 없이 의미 없음
- Aggregate 내부 구성 요소
- Order → OrderItem

예:

```java
@OneToMany(mappedBy = "order", cascade = CascadeType.ALL)
private List<OrderItem> orderItems = new ArrayList<>();
```

주의:

- ManyToOne에 Cascade REMOVE 사용 주의
- 공유 Entity에 Cascade REMOVE 금지
- User 같은 독립 Entity에 Cascade 삭제 위험
- Cascade ALL은 신중히 사용
- DB Cascade와 JPA Cascade 차이 이해

---

### [FAQ]

Q. Cascade는 언제 써?

A.
부모와 자식의 생명주기가 완전히 같고 자식이 부모 없이 의미 없을 때 사용한다.

Q. CascadeType.ALL을 무조건 써도 돼?

A.
아니다. 삭제 전파까지 포함하므로 독립 Entity나 공유 Entity에 사용하면 위험하다.

---

## 11.2 Orphan Removal Rules

### [개념]

orphanRemoval은 부모 Collection에서 제거된 자식 Entity를 고아 객체로 보고 삭제하는 설정이다.

---

### [핵심]

사용 상황:

- 부모가 자식 생명주기 소유
- 자식이 부모 없이 존재 불가
- Collection 제거가 DB 삭제 의미
- Aggregate 내부 자식 관리

---

### [실무]

예:

```java
@OneToMany(mappedBy = "order", orphanRemoval = true)
private List<OrderItem> orderItems = new ArrayList<>();
```

주의:

- Collection에서 제거하면 delete 발생 가능
- 단순 관계 해제와 삭제를 구분
- 공유 자식 Entity에 사용 금지
- Cascade REMOVE와 의미 비교 필요
- 비즈니스 삭제 정책과 일치해야 함

---

### [FAQ]

Q. orphanRemoval은 Cascade REMOVE와 같아?

A.
비슷하지만 다르다. orphanRemoval은 부모와의 관계가 끊어진 자식을 삭제하는 설정이다.

Q. orphanRemoval은 언제 위험해?

A.
자식 Entity가 다른 곳에서도 참조되거나 독립적으로 존재해야 할 때 위험하다.

---

# 12. Embedded and Value Type Rules

## 12.1 Embedded Value Type Rules

### [개념]

Embedded Value Type은 여러 필드를 하나의 값 객체로 묶어 Entity 안에 포함하는 방식이다.

---

### [핵심]

관련 Annotation:

- @Embeddable
- @Embedded
- @AttributeOverride
- Value Object
- Immutable Value
- Address
- Money
- Period

---

### [실무]

예:

```java
@Embeddable
@Getter
@NoArgsConstructor(access = AccessLevel.PROTECTED)
public class Address {

    private String city;
    private String street;
    private String zipcode;
}
```

사용:

```java
@Embedded
private Address address;
```

권장:

- 값 객체는 불변에 가깝게 설계
- 의미 있는 필드 묶음에 사용
- Entity 식별자가 필요하면 Entity로 분리
- 같은 Embedded 타입을 여러 번 쓰면 AttributeOverride 검토

---

### [FAQ]

Q. Embedded는 언제 써?

A.
주소, 기간, 금액처럼 여러 필드가 하나의 값으로 함께 움직일 때 사용한다.

Q. Embedded와 Entity 차이는?

A.
Embedded는 독립 식별자가 없는 값 객체이고 Entity는 식별자를 가진 독립 Persistence 객체다.

---

# 13. Auditing and Base Entity Rules

## 13.1 Auditing Rules

### [개념]

Auditing은 생성일, 수정일, 생성자, 수정자 같은 공통 메타데이터를 자동으로 관리하는 기능이다.

---

### [핵심]

관련 Annotation:

- @CreatedDate
- @LastModifiedDate
- @CreatedBy
- @LastModifiedBy
- @EntityListeners
- @EnableJpaAuditing
- BaseTimeEntity

---

### [실무]

예:

```java
@MappedSuperclass
@EntityListeners(AuditingEntityListener.class)
@Getter
public abstract class BaseTimeEntity {

    @CreatedDate
    private LocalDateTime createdAt;

    @LastModifiedDate
    private LocalDateTime updatedAt;
}
```

Entity:

```java
public class Post extends BaseTimeEntity {
}
```

권장:

- createdAt / updatedAt 공통화
- 시간 타입은 LocalDateTime 사용 가능
- Auditing 활성화 확인
- 테스트에서 시간 값 검증 기준 정리
- 생성자 / 수정자 추적은 Security 연동 고려

---

### [FAQ]

Q. createdAt, updatedAt은 Entity마다 직접 넣어야 해?

A.
공통 Base Entity로 분리하면 중복을 줄일 수 있다.

Q. Auditing이 동작하지 않으면 뭘 확인해?

A.
@EnableJpaAuditing, @EntityListeners, Base Entity 상속, Transaction 저장 여부를 확인한다.

---

# 14. Pagination and Collection Query Rules

## 14.1 JPA Pagination Rules

### [개념]

JPA Pagination은 목록 Query 결과를 Page, Slice, Pageable로 나누어 조회하는 방식이다.

---

### [핵심]

개념:

- Pageable
- Page
- Slice
- Sort
- Count Query
- Offset Pagination
- Keyset Pagination Basics
- Collection Fetch Join Caution

---

### [실무]

예:

```java
Slice<Post> findByDeletedFalseOrderByCreatedAtDesc(Pageable pageable);
```

선택 기준:

| Type  | 특징            | 사용 상황            |
| ----- | --------------- | -------------------- |
| Page  | 전체 count 포함 | 페이지 번호 UI       |
| Slice | hasNext 중심    | 무한 스크롤 / 더보기 |
| List  | 소량 데이터     | 고정 목록            |

주의:

- Page는 count query 비용 발생
- Slice는 count query 부담을 줄일 수 있음
- Collection Fetch Join과 Pagination 조합 주의
- 정렬 기준은 안정적으로 설정
- 대용량 offset pagination 성능 주의

---

### [FAQ]

Q. Page와 Slice 중 뭐가 좋아?

A.
전체 페이지 수가 필요하면 Page, 무한 스크롤이나 더보기면 Slice가 적합할 수 있다.

Q. Fetch Join과 Pagination을 같이 쓰면 안 돼?

A.
특히 Collection Fetch Join에서는 DB Pagination이 기대대로 동작하지 않을 수 있어 주의해야 한다.

---

# 15. Performance Review Rules

## 15.1 JPA Performance Review

### [개념]

JPA Performance Review는 Entity Mapping과 Query가 실제 SQL에서 성능 문제를 만들지 않는지 검토하는 과정이다.

---

### [핵심]

확인 대상:

- Generated SQL
- N+1 Problem
- Lazy Loading
- Eager Loading
- Fetch Join
- Pagination
- Count Query
- Index Usage
- DTO Projection
- Batch Size
- Bulk Query
- Transaction Length

---

### [실무]

Review Flow:

```text
API 조회 기능 확인
→ Repository Query 확인
→ 생성 SQL 확인
→ 연관 Entity 접근 확인
→ N+1 여부 확인
→ Pagination 방식 확인
→ DTO Projection 가능성 확인
→ Index 필요성 확인
```

권장:

- SQL 로그 확인
- 목록 API는 N+1 검토 필수
- 상세 API는 필요한 연관 Entity만 Fetch Join
- 단순 목록은 Projection 고려
- 대량 데이터는 Pagination 필수
- 무조건 Entity 전체 조회하지 않음

---

### [FAQ]

Q. JPA 성능 문제는 어떻게 찾는 게 좋아?

A.
SQL 로그를 확인하고 API 하나가 몇 개의 Query를 실행하는지, Join과 추가 조회가 적절한지 확인한다.

Q. Entity 전체 조회와 DTO Projection 중 뭐가 좋아?

A.
수정이 필요한 경우 Entity 조회가 적합하고, 읽기 전용 목록은 DTO Projection이 성능상 유리할 수 있다.

---

# 16. Backend Integration Rules

## 16.1 JPA with Spring Boot Rules

### [개념]

JPA는 Spring Boot Service, Repository, Transaction 구조와 함께 사용된다.

---

### [핵심]

연결 기준:

- Service Transaction
- Repository Data Access
- Entity Mapping
- DTO Response
- Exception Handling
- Validation
- Configuration

---

### [실무]

권장 흐름:

```text
Controller
→ Request DTO
→ Service @Transactional
→ Repository
→ Entity
→ Response DTO
→ Controller
```

주의:

- Controller에서 EntityManager 직접 사용 지양
- Repository는 Entity 접근 담당
- Service가 Transaction과 비즈니스 로직 담당
- DTO 변환은 Transaction 범위 고려
- 예외는 CustomException으로 표현

---

### [FAQ]

Q. JPA 코드는 어느 Layer에서 주로 다뤄?

A.
Repository는 데이터 접근, Service는 Transaction 안에서 Entity 조회와 변경을 담당한다.

---

## 16.2 JPA with SQL Rules

### [개념]

JPA는 SQL을 생성하므로 SQL Domain Rules와 함께 검토해야 한다.

---

### [핵심]

확인 대상:

- Join SQL
- Where Condition
- Index
- Order By
- Group By
- Pagination
- Count Query
- Constraint
- Foreign Key

---

### [실무]

권장:

- 복잡한 조회는 생성 SQL 확인
- Index가 필요한 조건인지 확인
- 불필요한 Join 제거
- 정렬 조건과 Pagination 비용 확인
- DB Constraint와 Entity Validation 역할 구분
- SQL 실행 계획은 필요 시 확인

---

### [FAQ]

Q. JPA를 쓰면 SQL 튜닝은 안 해도 돼?

A.
아니다. JPA가 SQL을 생성하므로 실제 생성 SQL과 DB 성능을 반드시 확인해야 한다.

---

## 16.3 JPA with QueryDSL Rules

### [개념]

QueryDSL은 타입 안전한 동적 Query를 작성하기 위한 도구다.

JPA Query Method나 JPQL이 복잡해질 때 QueryDSL을 검토한다.

---

### [핵심]

QueryDSL 검토 상황:

- 동적 검색 조건
- 복잡한 where 조합
- 복잡한 정렬
- Projection
- Join 조건 제어
- Query Method 이름 과다
- JPQL 문자열 유지보수 어려움

---

### [실무]

전환 기준:

```text
단순 조건
→ Query Method

고정 Query
→ JPQL

동적 조건 많음
→ QueryDSL
```

주의:

- QueryDSL은 JPA 대체가 아니라 Query 작성 보조
- Entity Mapping 문제를 해결하지 않음
- 성능 문제는 생성 SQL 기준으로 검토
- 상세 문법은 QueryDSL Domain Rules 참조

---

### [FAQ]

Q. Query Method가 길어지면 어떻게 해?

A.
JPQL이나 QueryDSL로 분리하는 것이 좋다. 동적 조건이 많으면 QueryDSL이 적합하다.

---

# 17. Troubleshooting Rules

## 17.1 LazyInitializationException

### [개념]

LazyInitializationException은 영속성 컨텍스트가 닫힌 후 Lazy 연관 객체에 접근할 때 발생하는 예외다.

---

### [핵심]

원인:

- Transaction 밖 Lazy 접근
- Controller에서 Entity 반환
- View / JSON 직렬화 중 Lazy 접근
- DTO 변환 위치 오류
- OSIV 의존

---

### [실무]

Debug Flow:

```text
Exception 발생 위치 확인
→ Lazy Field 확인
→ Transaction 범위 확인
→ DTO 변환 위치 확인
→ Fetch Join 필요 여부 확인
→ Entity 직접 반환 여부 확인
```

해결:

- Service Transaction 안에서 DTO 변환
- 필요한 연관 Entity Fetch Join
- DTO Projection 사용
- Entity 직접 반환 제거
- OSIV에 의존하지 않는 구조 설계

---

### [FAQ]

Q. LazyInitializationException은 왜 발생해?

A.
영속성 컨텍스트가 닫힌 뒤 Lazy 연관 객체에 접근했기 때문이다.

Q. 해결하려고 EAGER로 바꾸면 돼?

A.
권장하지 않는다. 필요한 조회에서 Fetch Join이나 DTO Projection으로 해결하는 것이 좋다.

---

## 17.2 N+1 Troubleshooting

### [개념]

N+1 Troubleshooting은 API 조회 시 불필요한 연관 Entity Query가 반복 발생하는 문제를 분석하는 과정이다.

---

### [핵심]

확인 대상:

- 목록 조회
- DTO 변환 반복문
- 연관 Entity getter
- Fetch 전략
- SQL 로그
- Query 수
- Pagination 조합

---

### [실무]

Debug Flow:

```text
API 하나 호출
→ SQL 로그 확인
→ 첫 Query 확인
→ 반복 Query 확인
→ 연관 Field 접근 위치 확인
→ 해결 전략 선택
```

해결 후보:

```text
ManyToOne N+1
→ Fetch Join / EntityGraph / DTO Projection

OneToMany N+1
→ Batch Size / 별도 Query / DTO Projection / API 구조 변경

목록 read-only
→ DTO Projection
```

---

### [FAQ]

Q. N+1 문제는 항상 Lazy 때문에 생겨?

A.
Lazy에서 자주 보이지만 EAGER에서도 조회 방식에 따라 발생할 수 있다.

Q. N+1 문제를 해결했는지 어떻게 확인해?

A.
SQL 로그에서 API 하나당 실행 Query 수가 줄었는지 확인한다.

---

## 17.3 Entity Mapping Error

### [개념]

Entity Mapping Error는 Entity Annotation, Column, 연관관계 설정이 DB 구조나 JPA 규칙과 맞지 않아 발생하는 문제다.

---

### [핵심]

원인:

- @Id 누락
- 기본 생성자 없음
- Column 이름 불일치
- JoinColumn 오류
- mappedBy 필드명 오류
- Enum Mapping 오류
- Table 이름 불일치
- nullable 제약 불일치

---

### [실무]

Debug Flow:

```text
Error Message 확인
→ Entity Annotation 확인
→ @Id 확인
→ 기본 생성자 확인
→ Table / Column 이름 확인
→ 연관관계 mappedBy 확인
→ DB Schema 확인
```

---

### [FAQ]

Q. Entity Mapping 오류가 나면 뭘 먼저 확인해?

A.
@Id, 기본 생성자, @Entity, Table / Column 이름, mappedBy 필드명, JoinColumn 설정을 확인한다.

---

## 17.4 Detached Entity Problem

### [개념]

Detached Entity Problem은 준영속 상태 Entity를 영속 상태처럼 수정하거나 저장하면서 발생하는 문제다.

---

### [핵심]

원인:

- Transaction 밖 Entity 수정
- Controller로 Entity 전달
- 요청 DTO 대신 Entity 재사용
- merge 오해
- 영속 Entity와 Detached Entity 혼동

---

### [실무]

권장:

- 수정 작업은 Transaction 안에서 Entity를 다시 조회
- 요청 값은 DTO로 받고 Entity에 반영
- Detached Entity를 그대로 save하는 방식 주의
- merge보다 변경 감지 방식 우선
- Entity 상태를 명확히 관리

예:

```java
@Transactional
public void updateUser(Long userId, UserUpdateRequest request) {
    User user = userRepository.findById(userId)
            .orElseThrow(...);

    user.update(request.nickname());
}
```

---

### [FAQ]

Q. Detached Entity를 그대로 수정하면 DB에 반영돼?

A.
아니다. 영속성 컨텍스트가 관리하지 않으므로 변경 감지가 동작하지 않는다.

Q. 수정 API에서 Entity를 새로 만들어 save하면 돼?

A.
가능은 하지만 기존 값 덮어쓰기, 연관관계 손실 위험이 있어 Transaction 안에서 조회 후 변경하는 방식이 안전하다.

---

# 18. Comparison Rules

## 18.1 Required Comparisons

### [개념]

JPA 문서는 헷갈리는 개념을 비교해서 작성한다.

---

### [핵심]

필수 비교 대상:

- Entity vs DTO
- JPA vs Hibernate
- Persist vs Merge
- Managed vs Detached
- Flush vs Commit
- Lazy vs Eager
- Join vs Fetch Join
- OneToMany vs ManyToOne
- Unidirectional vs Bidirectional
- Owning Side vs Inverse Side
- Cascade REMOVE vs orphanRemoval
- JPQL vs SQL
- Query Method vs JPQL vs QueryDSL
- Page vs Slice
- Entity 조회 vs DTO Projection
- Dirty Checking vs save
- Validation Constraint vs DB Constraint

---

### [실무]

예시:

| 비교      | Lazy Loading        | Eager Loading      |
| --------- | ------------------- | ------------------ |
| 조회 시점 | 사용 시점           | Entity 조회 시점   |
| 장점      | 불필요한 조회 감소  | 즉시 사용 가능     |
| 단점      | N+1, Lazy 예외 가능 | 불필요한 Join 가능 |
| 권장      | 기본 전략으로 고려  | 필요한 경우 제한적 |
| 제어      | Fetch Join으로 보완 | 제어 어려움        |

---

### [FAQ]

Q. JPA Comparison은 왜 필요해?

A.
JPA는 비슷해 보이는 개념이 많고 선택에 따라 성능과 버그가 크게 달라지기 때문이다.

Q. 가장 중요한 비교는 뭐야?

A.
Entity vs DTO, Lazy vs Eager, Join vs Fetch Join, Managed vs Detached, Flush vs Commit이다.

---

# 19. Checklist Rules

## 19.1 JPA Checklist

### [개념]

JPA 문서 검수 시 Entity 설계와 Query 성능 체크리스트를 사용한다.

---

### [핵심]

Checklist:

```md
- [ ] Entity Mapping 기준이 포함되었는가?
- [ ] DTO와 Entity 분리 기준이 포함되었는가?
- [ ] Primary Key 전략이 포함되었는가?
- [ ] Column nullable / length 기준이 포함되었는가?
- [ ] EnumType.STRING 기준이 포함되었는가?
- [ ] 연관관계 설계 기준이 포함되었는가?
- [ ] 단방향 / 양방향 선택 기준이 포함되었는가?
- [ ] 연관관계 주인 기준이 포함되었는가?
- [ ] ManyToOne LAZY 기준이 포함되었는가?
- [ ] OneToMany Collection 주의사항이 포함되었는가?
- [ ] ManyToMany 직접 사용 지양 기준이 포함되었는가?
- [ ] Persistence Context 기준이 포함되었는가?
- [ ] Dirty Checking 기준이 포함되었는가?
- [ ] Flush와 Commit 차이가 포함되었는가?
- [ ] Lazy Loading 주의사항이 포함되었는가?
- [ ] N+1 Problem 탐지 기준이 포함되었는가?
- [ ] Fetch Join 사용 기준이 포함되었는가?
- [ ] Repository Query Method 기준이 포함되었는가?
- [ ] JPQL 기준이 포함되었는가?
- [ ] DTO Projection 기준이 포함되었는가?
- [ ] Transaction Boundary 기준이 포함되었는가?
- [ ] Cascade / orphanRemoval 주의사항이 포함되었는가?
- [ ] Auditing 기준이 포함되었는가?
- [ ] Pagination 기준이 포함되었는가?
- [ ] Troubleshooting이 포함되었는가?
- [ ] Common Mistakes가 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 흐름:

```text
Draft
→ Entity Mapping Check
→ Association Check
→ Persistence Context Check
→ Transaction Check
→ Query Strategy Check
→ N+1 Check
→ DTO Separation Check
→ Cascade Check
→ Troubleshooting Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

---

### [FAQ]

Q. JPA 문서 검수에서 가장 중요한 것은?

A.
Entity와 DTO 분리, 연관관계 주인, Lazy Loading, N+1 문제, Transaction 경계, Cascade 위험 검토다.

---

# 20. Retrieval Optimization Rules

## 20.1 Keyword Rules

### [개념]

JPA 문서는 검색 매칭을 위해 핵심 키워드를 반복 허용한다.

---

### [핵심]

강조 키워드:

- JPA
- Hibernate
- ORM
- Entity
- DTO
- Persistence Context
- EntityManager
- Dirty Checking
- Flush
- Commit
- Managed
- Detached
- Lazy Loading
- Eager Loading
- LazyInitializationException
- N+1 Problem
- Fetch Join
- JPQL
- Native Query
- Repository
- Query Method
- DTO Projection
- OneToMany
- ManyToOne
- OneToOne
- ManyToMany
- Owning Side
- mappedBy
- JoinColumn
- Cascade
- orphanRemoval
- Embedded
- Auditing
- Transaction
- readOnly
- Page
- Slice
- Pageable
- GeneratedValue
- EnumType.STRING
- Entity Lifecycle
- Anti Pattern

---

### [실무]

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

예:

- JPA Entity는 어떻게 설계해?
- Entity와 DTO는 왜 분리해?
- Entity를 Response로 바로 반환하면 안 되는 이유는?
- ManyToOne은 왜 LAZY로 해?
- mappedBy는 뭐야?
- 연관관계 주인은 뭐야?
- N+1 문제는 어떻게 해결해?
- Fetch Join은 언제 써?
- LazyInitializationException은 왜 발생해?
- Dirty Checking은 뭐야?
- update 할 때 save 해야 해?
- Flush와 Commit 차이는?
- Cascade는 언제 써?
- orphanRemoval은 언제 위험해?
- JPQL과 SQL 차이는?
- Query Method가 너무 길면?
- DTO Projection은 언제 써?
- Page와 Slice 차이는?
- JPA 성능 문제는 어떻게 찾지?

---

### [FAQ]

Q. 키워드 반복은 중복이야?

A.
불필요한 장문 반복은 금지지만 Retrieval 최적화를 위한 핵심 키워드 반복은 허용된다.

Q. JPA FAQ 질문은 어떤 스타일이 좋아?

A.
실제 개발 중 자주 묻는 Entity, 연관관계, N+1, Lazy Loading, Transaction 질문 형태가 좋다.

---

# 21. Version Rules

## 21.1 Modern JPA 기준

### [개념]

JPA 문서는 Modern Spring Boot + JPA 기준으로 작성한다.

---

### [핵심]

기준:

- Spring Boot 3.x
- Java 17+
- Jakarta Persistence
- Hibernate 6.x 기준 호환
- Spring Data JPA
- Constructor / Protected NoArgs Constructor
- DTO Separation
- LAZY First Strategy
- Service Transaction Boundary
- Query Performance Review
- Entity to DTO Mapping
- Auditing
- QueryDSL 연계 가능성

Legacy 제외:

- javax.persistence 중심 신규 문서
- Entity 직접 API 반환 중심
- Open Session In View 의존 중심 설계
- EAGER 기본 전략 맹신
- ManyToMany 직접 남용
- 무분별한 CascadeType.ALL
- Controller에서 Entity 수정
- Repository에 비즈니스 로직 작성
- 모든 조회를 findAll 후 Java에서 필터링
- SQL 로그 확인 없는 JPA 사용

---

### [실무]

실무 기준:

```text
Modern JPA
→ Entity Mapping
→ Association LAZY
→ Service Transaction
→ Repository Query
→ DTO Mapping
→ SQL Review
→ N+1 Check
→ Performance Review
```

---

### [FAQ]

Q. Spring Boot 3에서는 javax.persistence를 써?

A.
Spring Boot 3 기준에서는 Jakarta 전환으로 jakarta.persistence 패키지를 사용하는 경우가 많다.

Q. OSIV에 의존해도 돼?

A.
권장하지 않는다. Service Transaction 범위 안에서 필요한 데이터를 DTO로 변환하는 구조가 더 명확하다.

---

# 22. Common Mistakes

## 22.1 JPA Common Mistakes

### [개념]

JPA 문서는 자주 발생하는 Entity 설계 / Query / Transaction 실수를 명확히 포함해야 한다.

---

### [핵심]

자주 발생:

- Entity를 API Response로 직접 반환
- RequestBody로 Entity 직접 수신
- 모든 연관관계를 양방향으로 설계
- ManyToOne LAZY 명시 누락
- EAGER로 N+1 해결 시도
- mappedBy와 JoinColumn 혼동
- 연관관계 주인 아닌 쪽만 수정
- ManyToMany 직접 사용
- CascadeType.ALL 남용
- orphanRemoval 의미 오해
- Dirty Checking을 모름
- update 후 무조건 save 호출
- Transaction 밖에서 Lazy 접근
- Controller에서 DTO 변환 중 Lazy 예외 발생
- Fetch Join과 Pagination 무분별 조합
- Query Method 이름 과도하게 길어짐
- findAll 후 Java Stream으로 필터링
- Entity에 화면 전용 필드 추가
- EnumType.ORDINAL 사용
- equals / hashCode 잘못 구현
- SQL 로그 확인 안 함
- Repository에 비즈니스 로직 작성

---

### [실무]

문서 작성 시 Common Mistakes는 Troubleshooting과 연결한다.

예:

```text
문제: 목록 조회 API에서 SQL이 수십 번 실행됨
원인: Post 목록 조회 후 DTO 변환에서 post.getUser().getNickname() 반복 접근
해결: Fetch Join 또는 DTO Projection으로 필요한 User 정보를 함께 조회
```

예:

```text
문제: 수정 API에서 값이 DB에 반영되지 않음
원인: Transaction 밖 Detached Entity 수정
해결: Service @Transactional 안에서 Entity 조회 후 변경 메서드 호출
```

---

### [FAQ]

Q. JPA 초보가 가장 많이 하는 실수는?

A.
Entity를 API에 직접 노출하거나 연관관계를 모두 EAGER / 양방향으로 만들고 N+1 문제를 확인하지 않는 실수가 많다.

Q. JPA 문제는 어떻게 찾는 게 좋아?

A.
Entity Mapping, Transaction 범위, Lazy 접근 위치, 생성 SQL, Query 수, DTO 변환 위치를 순서대로 확인한다.

---

# 23. Final Goal

## 23.1 Domain Final Goal

### [개념]

JPA RAG 문서는 Backend Agent가 Entity와 Repository를 단순히 생성하는 것이 아니라 Persistence Context, 연관관계, Query 성능, Transaction 경계를 함께 고려해 안정적인 Persistence Layer를 설계하도록 지원해야 한다.

---

### [핵심]

최종 목표:

- Entity Mapping 설계
- DTO / Entity 분리
- Primary Key 전략 선택
- Column 제약 명확화
- EnumType.STRING 적용 판단
- 연관관계 방향 결정
- 단방향 / 양방향 선택
- Owning Side 판단
- ManyToOne LAZY 적용
- OneToMany Collection 주의
- ManyToMany 중간 Entity 전환
- Persistence Context 이해
- Entity Lifecycle 판단
- Dirty Checking 적용
- Flush / Commit 차이 이해
- Lazy Loading 문제 분석
- N+1 Problem 탐지
- Fetch Join 적용 판단
- Repository Query Method 작성
- JPQL 작성 기준 판단
- DTO Projection 적용 판단
- Transaction Boundary 설정
- Cascade / orphanRemoval 위험 검토
- Auditing 적용
- Pagination 기준 선택
- JPA Performance Review 수행
- JPA Anti Pattern 탐지

---

### [실무]

Agent 수행 가능 작업:

```text
User Persistence Request
→ Identify Entity
→ Design Table Mapping
→ Design Association
→ Decide Owning Side
→ Apply Lazy Strategy
→ Design Repository Query
→ Apply Transaction Boundary
→ Map Entity to DTO
→ Check N+1 Problem
→ Review SQL
→ Check Cascade Risk
→ JPA Output
```

---

### [FAQ]

Q. JPA 문서의 최종 목적은 뭐야?

A.
Backend Agent가 Entity, 연관관계, Repository, Transaction, DTO 변환, Query 성능을 함께 검토하면서 안정적인 Persistence Layer를 만들게 하는 것이다.

Q. 이 문서 다음에는 어떤 Domain Rules가 이어져야 해?

A.
Security Advanced, QueryDSL Practical, Testing, API Design Domain Rules와 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. JPA Domain Rules는 왜 필요해?
A. Backend Agent가 Entity, 연관관계, Repository, Transaction, DTO 변환, Query 성능을 일관되게 설계해야 하기 때문이다.

Q. JPA는 SQL을 안 써도 되는 기술이야?
A. 아니다. SQL을 직접 덜 작성하게 해주지만 내부적으로 SQL이 생성되므로 SQL 동작을 이해해야 한다.

Q. JPA와 Hibernate는 같은 거야?
A. JPA는 표준 인터페이스이고 Hibernate는 JPA 구현체다.

Q. Entity는 뭐야?
A. Entity는 DB Table과 매핑되는 Persistence Model이다.

Q. JPA Entity는 어떻게 설계해?
A. @Entity, @Id, @Column, 연관관계, 기본 생성자, 상태 변경 메서드를 기준으로 설계한다.

Q. Entity에 Setter를 전부 열어도 돼?
A. 권장하지 않는다. 상태 변경 의도가 드러나는 메서드를 만들어 변경 경로를 통제하는 것이 좋다.

Q. Entity 기본 생성자는 왜 필요해?
A. JPA가 Reflection으로 Entity를 생성하기 위해 기본 생성자가 필요하다. 외부 생성을 막기 위해 protected로 두는 경우가 많다.

Q. Entity와 DTO는 왜 분리해?
A. API 변경과 DB 변경을 분리하고 민감정보 노출, Lazy Loading, 순환 참조 문제를 막기 위해 분리한다.

Q. Entity를 Controller에서 바로 반환하면 왜 안 돼?
A. 민감정보 노출, Lazy Loading, 순환 참조, API 스펙 변경 위험이 생길 수 있다.

Q. RequestBody로 Entity를 받아도 돼?
A. 권장하지 않는다. API 입력 구조와 Entity 내부 구조가 강하게 결합되고 보안 문제가 생길 수 있다.

Q. Entity와 DTO 변환은 어디서 해?
A. 간단한 변환은 DTO의 static from 메서드 또는 Service에서 처리할 수 있다. 프로젝트 규칙으로 일관화하는 것이 중요하다.

Q. JPA Entity ID는 뭘 쓰는 게 좋아?
A. 대부분 Long 타입의 surrogate key를 사용하고 DB 전략에 맞게 IDENTITY나 SEQUENCE를 선택한다.

Q. 이메일을 Primary Key로 써도 돼?
A. 권장하지 않는다. 이메일은 변경될 수 있는 비즈니스 값이므로 별도 unique column으로 두는 것이 좋다.

Q. @Column(nullable = false)는 꼭 써야 해?
A. 필수는 아니지만 DB 무결성과 코드 의도를 명확히 하기 위해 중요한 필드는 명시하는 것이 좋다.

Q. Enum은 ORDINAL로 저장해도 돼?
A. 권장하지 않는다. enum 순서가 바뀌면 기존 데이터 의미가 깨질 수 있으므로 STRING을 우선한다.

Q. JPA 연관관계는 무조건 양방향으로 해야 해?
A. 아니다. 단방향으로 충분하면 단방향이 단순하고 유지보수에 좋다.

Q. 연관관계 주인은 어떻게 정해?
A. DB Foreign Key를 가진 Entity가 연관관계 주인이 된다.

Q. ManyToOne은 왜 LAZY를 명시해?
A. ManyToOne 기본 Fetch는 EAGER라 불필요한 Join과 조회가 발생할 수 있으므로 LAZY를 명시하는 것이 좋다.

Q. ManyToOne에서 JoinColumn은 어디에 둬?
A. Foreign Key를 가진 Many 쪽 Entity에 둔다.

Q. OneToMany에는 mappedBy를 왜 써?
A. 상대 Entity가 Foreign Key를 가진 연관관계 주인임을 표시하기 위해 사용한다.

Q. mappedBy가 있는 쪽이 주인이야?
A. 아니다. mappedBy가 있는 쪽은 연관관계 주인이 아니며 FK를 직접 관리하지 않는다.

Q. 양방향 관계에서 한쪽만 세팅해도 돼?
A. DB 반영은 주인 쪽이 기준이지만 객체 상태 일관성을 위해 양쪽을 함께 맞추는 편의 메서드를 사용하는 것이 좋다.

Q. ManyToMany를 바로 쓰면 안 돼?
A. 가능은 하지만 실무에서는 중간 테이블에 생성일, 상태 같은 추가 필드가 필요한 경우가 많아 중간 Entity로 풀어내는 것이 좋다.

Q. 좋아요, 찜 같은 관계는 ManyToMany야?
A. 개념적으로는 다대다지만 Like, Favorite 같은 중간 Entity로 표현하는 것이 실무에 적합하다.

Q. 영속성 컨텍스트가 뭐야?
A. JPA가 Entity를 관리하는 공간이며 1차 캐시, 동일성 보장, 변경 감지 같은 기능을 제공한다.

Q. Entity Lifecycle은 뭐야?
A. Entity가 비영속, 영속, 준영속, 삭제 상태로 관리되는 흐름이다.

Q. 준영속 상태가 뭐야?
A. 한때 영속성 컨텍스트가 관리했지만 현재는 분리되어 JPA가 변경을 추적하지 않는 상태다.

Q. Dirty Checking은 뭐야?
A. Transaction 안에서 영속 상태 Entity의 변경을 감지해 DB Update SQL을 생성하는 기능이다.

Q. JPA update 할 때 save를 꼭 해야 해?
A. Transaction 안에서 조회한 영속 Entity를 변경하면 Dirty Checking으로 반영될 수 있어 save가 필수는 아니다.

Q. Dirty Checking이 안 되면 뭘 확인해?
A. @Transactional 범위, Entity 영속 상태, 조회 방식, Transaction 종료 시점, 변경 메서드 호출 여부를 확인한다.

Q. Flush와 Commit은 같은 거야?
A. 아니다. Flush는 SQL을 DB에 반영하는 과정이고 Commit은 Transaction을 확정하는 과정이다.

Q. JPQL 전에 Flush가 일어나는 이유는?
A. Query 결과가 영속성 컨텍스트 변경 내용과 일치하도록 하기 위해 Flush가 발생할 수 있다.

Q. Lazy Loading은 무조건 좋아?
A. 아니다. 불필요한 즉시 조회를 줄일 수 있지만 잘못 사용하면 N+1 문제나 LazyInitializationException이 발생할 수 있다.

Q. LazyInitializationException은 왜 발생해?
A. 영속성 컨텍스트가 닫힌 뒤 Lazy 연관 객체에 접근했기 때문이다.

Q. LazyInitializationException 해결하려고 EAGER로 바꾸면 돼?
A. 권장하지 않는다. 필요한 조회에서 Fetch Join이나 DTO Projection으로 해결하는 것이 좋다.

Q. EAGER면 N+1 문제가 없어져?
A. 아니다. EAGER도 조회 방식에 따라 추가 쿼리가 발생할 수 있고 제어하기 어려운 성능 문제가 생길 수 있다.

Q. N+1 문제는 뭐야?
A. 목록 1번 조회 후 각 Row의 연관 Entity를 조회하기 위해 N번 추가 Query가 발생하는 문제다.

Q. N+1 문제는 어떻게 찾는 게 좋아?
A. SQL 로그를 켜고 목록 조회 후 반복문이나 DTO 변환 과정에서 연관 Entity 조회가 반복되는지 확인한다.

Q. N+1 문제는 무조건 Fetch Join으로 해결해?
A. 아니다. Fetch Join, DTO Projection, Batch Size, API 구조 변경 중 상황에 맞게 선택한다.

Q. Fetch Join은 언제 써?
A. 특정 조회에서 연관 Entity가 반드시 필요하고 Lazy Loading으로 추가 Query가 많이 발생할 때 사용한다.

Q. Collection Fetch Join에 Pagination을 같이 써도 돼?
A. 주의해야 한다. DB Pagination이 기대대로 동작하지 않거나 메모리에서 처리될 수 있어 별도 전략을 검토해야 한다.

Q. Repository Query Method는 언제 써?
A. 조건이 단순하고 메서드 이름이 과도하게 길어지지 않을 때 적합하다.

Q. Query Method가 너무 길어지면 어떻게 해?
A. JPQL이나 QueryDSL로 분리하는 것이 좋다. 동적 조건이 많으면 QueryDSL이 적합하다.

Q. JPQL은 SQL이랑 뭐가 달라?
A. JPQL은 Table과 Column이 아니라 Entity와 Field를 기준으로 작성하고 JPA가 SQL로 변환한다.

Q. Native Query는 언제 써?
A. JPQL이나 QueryDSL로 표현하기 어렵거나 DB 특화 기능이 필요한 경우에 사용한다.

Q. DTO Projection은 언제 써?
A. 읽기 전용 목록이나 화면 응답에서 Entity 전체가 필요하지 않을 때 사용한다.

Q. 수정 작업에도 DTO Projection을 써도 돼?
A. 수정 작업은 Entity 상태 변경이 필요하므로 Entity를 조회하는 것이 일반적이다.

Q. JPA에서 @Transactional은 왜 중요해?
A. 영속성 컨텍스트, Dirty Checking, Lazy Loading, Flush가 Transaction 범위와 밀접하게 연결되기 때문이다.

Q. Controller에서 Entity를 DTO로 변환해도 돼?
A. 권장하지 않는다. Lazy Loading과 책임 분리 문제를 피하기 위해 Service Transaction 범위 안에서 변환하는 것이 좋다.

Q. 조회 메서드에 readOnly = true를 왜 붙여?
A. 조회 의도를 명확히 하고 변경 감지 부담을 줄이는 데 도움이 될 수 있다.

Q. Cascade는 언제 써?
A. 부모와 자식의 생명주기가 완전히 같고 자식이 부모 없이 의미 없을 때 사용한다.

Q. CascadeType.ALL을 무조건 써도 돼?
A. 아니다. 삭제 전파까지 포함하므로 독립 Entity나 공유 Entity에 사용하면 위험하다.

Q. orphanRemoval은 Cascade REMOVE와 같아?
A. 비슷하지만 다르다. orphanRemoval은 부모와의 관계가 끊어진 자식을 삭제하는 설정이다.

Q. orphanRemoval은 언제 위험해?
A. 자식 Entity가 다른 곳에서도 참조되거나 독립적으로 존재해야 할 때 위험하다.

Q. Embedded는 언제 써?
A. 주소, 기간, 금액처럼 여러 필드가 하나의 값으로 함께 움직일 때 사용한다.

Q. Embedded와 Entity 차이는?
A. Embedded는 독립 식별자가 없는 값 객체이고 Entity는 식별자를 가진 독립 Persistence 객체다.

Q. createdAt, updatedAt은 Entity마다 직접 넣어야 해?
A. 공통 Base Entity로 분리하면 중복을 줄일 수 있다.

Q. Auditing이 동작하지 않으면 뭘 확인해?
A. @EnableJpaAuditing, @EntityListeners, Base Entity 상속, Transaction 저장 여부를 확인한다.

Q. Page와 Slice 중 뭐가 좋아?
A. 전체 페이지 수가 필요하면 Page, 무한 스크롤이나 더보기면 Slice가 적합할 수 있다.

Q. JPA 성능 문제는 어떻게 찾는 게 좋아?
A. SQL 로그를 확인하고 API 하나가 몇 개의 Query를 실행하는지, Join과 추가 조회가 적절한지 확인한다.

Q. Entity 전체 조회와 DTO Projection 중 뭐가 좋아?
A. 수정이 필요한 경우 Entity 조회가 적합하고, 읽기 전용 목록은 DTO Projection이 성능상 유리할 수 있다.

Q. JPA를 쓰면 SQL 튜닝은 안 해도 돼?
A. 아니다. JPA가 SQL을 생성하므로 실제 생성 SQL과 DB 성능을 반드시 확인해야 한다.

Q. Entity Mapping 오류가 나면 뭘 먼저 확인해?
A. @Id, 기본 생성자, @Entity, Table / Column 이름, mappedBy 필드명, JoinColumn 설정을 확인한다.

Q. Detached Entity를 그대로 수정하면 DB에 반영돼?
A. 아니다. 영속성 컨텍스트가 관리하지 않으므로 변경 감지가 동작하지 않는다.

Q. 수정 API에서 Entity를 새로 만들어 save하면 돼?
A. 가능은 하지만 기존 값 덮어쓰기, 연관관계 손실 위험이 있어 Transaction 안에서 조회 후 변경하는 방식이 안전하다.

Q. JPA 초보가 가장 많이 하는 실수는?
A. Entity를 API에 직접 노출하거나 연관관계를 모두 EAGER / 양방향으로 만들고 N+1 문제를 확인하지 않는 실수가 많다.

Q. JPA 문제는 어떻게 찾는 게 좋아?
A. Entity Mapping, Transaction 범위, Lazy 접근 위치, 생성 SQL, Query 수, DTO 변환 위치를 순서대로 확인한다.

Q. JPA 다음 문서는 뭐가 좋아?
A. Security Advanced, QueryDSL Practical, Testing, API Design Domain Rules와 이어지는 것이 좋다.
