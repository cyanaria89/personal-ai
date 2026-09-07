# JPA Advanced Part08 — Backend Integration, Troubleshooting, Anti Pattern

---

# 1. Backend Integration Purpose

## 1.1 JPA Backend Integration Concept

### [개념]

JPA Backend Integration은 Controller, DTO, Service, Repository, Entity, Transaction, Response 흐름을 JPA 기준으로 연결하는 설계다.

JPA는 Entity Mapping만으로 끝나지 않고 Service Transaction, Repository Query, DTO 변환, SQL Review, Troubleshooting까지 함께 검토해야 한다.

---

### [핵심]

핵심 키워드:

- Backend Integration
- Controller
- Request DTO
- Service
- Transaction
- Repository
- Entity
- Response DTO
- Persistence Context
- Dirty Checking
- Lazy Loading
- Fetch Join
- N+1
- Data Integrity
- SQL Review

기본 흐름:

```text
HTTP Request
→ Controller
→ Request DTO
→ Service @Transactional
→ Repository
→ Entity
→ Persistence Context
→ Dirty Checking / Query
→ Response DTO
→ HTTP Response
```

---

### [실무]

SQL Foundation 연결:

```text
SQL Part01 Query Purpose / Table Relationship
→ Entity Mapping / Association Mapping

SQL Part02 Filtering / JOIN / Aggregation
→ Repository Query / JPQL / Fetch Join

SQL Part03 INSERT / UPDATE / DELETE
→ save / Dirty Checking / delete

SQL Part04 Transaction / Constraint / Pagination
→ @Transactional / Data Integrity / Page / Slice

SQL Part05 Backend Integration / Troubleshooting / Anti Pattern
→ JPA Backend Integration / JPA Troubleshooting / JPA Anti Pattern
```

JPA Backend Integration 기준:

```text
Controller
→ HTTP와 DTO만 처리

Service
→ Transaction과 비즈니스 흐름 처리

Repository
→ Entity 조회 / 저장 처리

Entity
→ Persistence Model과 상태 변경 Method 보유

DTO
→ API 입출력 구조 담당
```

권장:

- Controller에서 Entity를 직접 다루지 않음
- RequestBody로 Entity를 직접 받지 않음
- Response로 Entity를 직접 반환하지 않음
- Service에서 Transaction Boundary 관리
- Repository는 Query와 Data Access에 집중
- Entity 변경은 Service Transaction 안에서 수행
- DTO 변환 위치는 Lazy Loading과 N+1을 고려해 결정
- SQL 로그로 실제 Query를 확인

주의:

- JPA 문제는 코드 구조와 SQL 실행 결과를 함께 봐야 한다.
- Entity 설계 오류는 Repository, Service, API 응답까지 전파된다.
- Repository Query 오류는 Pagination, DTO 변환, N+1 문제로 이어질 수 있다.
- Transaction 범위가 불명확하면 Dirty Checking과 Lazy Loading 문제가 발생한다.
- API 응답 구조를 Entity 구조와 동일하게 만들지 않는다.

---

### [FAQ]

Q. JPA Backend Integration은 뭐야?
A. Controller, DTO, Service, Repository, Entity, Transaction, Response 흐름을 JPA 기준으로 연결하는 설계다.

Q. JPA는 Entity만 잘 만들면 끝이야?
A. 아니다. Repository Query, Service Transaction, DTO 변환, SQL Review, Troubleshooting까지 함께 검토해야 한다.

Q. Controller에서 Entity를 직접 반환해도 돼?
A. 권장하지 않는다. Entity 직접 반환은 Lazy Loading, 순환 참조, 민감정보 노출, API 결합 문제를 만든다.

Q. JPA Backend Integration에서 가장 중요한 Layer는 어디야?
A. Service Layer다. Transaction Boundary와 Entity 상태 변경 흐름을 관리하기 때문이다.

---

## 1.2 Layer Responsibility Rule

### [개념]

Layer Responsibility Rule은 JPA 기반 Spring Boot Backend에서 각 Layer의 책임을 명확히 나누는 규칙이다.

Layer 책임이 섞이면 Transaction, Entity 노출, Repository 비즈니스 로직, DTO 변환 위치 문제가 발생한다.

---

### [핵심]

Layer 책임:

| Layer             | 책임                             |
| ----------------- | -------------------------------- |
| Controller        | HTTP Request / Response          |
| Request DTO       | 입력 값 수신 / Validation        |
| Service           | Transaction / Business Flow      |
| Repository        | Entity Data Access               |
| Entity            | Persistence Model / State Change |
| Response DTO      | API Response 구조                |
| Exception Handler | Error Response 변환              |

기본 구조:

```text
Controller
→ Request DTO
→ Service
→ Repository
→ Entity
→ Response DTO
```

---

### [실무]

Controller 예시:

```java
@PostMapping
public PostResponse createPost(@Valid @RequestBody PostCreateRequest request) {
    return postService.createPost(request);
}
```

Service 예시:

```java
@Transactional
public PostResponse createPost(PostCreateRequest request) {
    Post post = Post.create(request.title(), request.content());
    Post savedPost = postRepository.save(post);

    return PostResponse.from(savedPost);
}
```

Repository 예시:

```java
public interface PostRepository extends JpaRepository<Post, Long> {
}
```

Entity 예시:

```java
@Entity
public class Post {

    public void update(String title, String content) {
        this.title = title;
        this.content = content;
    }
}
```

권장:

- Controller는 Service 호출과 응답 반환에 집중
- Service는 Transaction과 비즈니스 흐름 관리
- Repository는 Query Method, JPQL, Native Query에 집중
- Entity는 상태와 Mapping 책임 보유
- DTO는 API 입출력 구조 담당
- Exception은 GlobalExceptionHandler에서 API 응답으로 변환

주의:

- Controller에서 Entity를 수정하지 않는다.
- Repository에서 권한 검증이나 비즈니스 결정을 하지 않는다.
- Entity에 화면 전용 Field를 넣지 않는다.
- DTO에 Persistence Context 의존 로직을 넣지 않는다.
- Service가 너무 비대해지면 Domain Method / Domain Service 분리를 검토한다.

---

### [FAQ]

Q. Controller는 JPA Entity를 직접 다뤄도 돼?
A. 권장하지 않는다. Controller는 DTO와 HTTP 흐름만 다루는 것이 안전하다.

Q. Repository에 비즈니스 로직을 넣어도 돼?
A. 권장하지 않는다. Repository는 Data Access Layer이고 비즈니스 흐름은 Service에서 처리한다.

Q. Entity에는 어떤 로직을 넣어도 돼?
A. Entity 상태 변경과 불변 조건에 가까운 Domain Method를 넣을 수 있다.

Q. DTO 변환은 어디서 해?
A. 프로젝트 규칙에 따라 Service 또는 DTO static factory에서 처리할 수 있지만 Lazy Loading과 Transaction 범위를 고려해야 한다.

---

# 2. Request Flow and Response Flow

## 2.1 Create Flow

### [개념]

Create Flow는 API 입력 값을 Request DTO로 받고 Service Transaction 안에서 Entity를 생성한 뒤 Repository를 통해 저장하는 흐름이다.

Create Flow에서는 Request DTO와 Entity 생성 규칙, Validation, Constraint, Response DTO 변환을 함께 검토한다.

---

### [핵심]

Create Flow:

```text
Client Request
→ Controller
→ Request DTO Validation
→ Service @Transactional
→ Entity.create()
→ Repository.save()
→ Flush / Commit
→ Response DTO
```

핵심 키워드:

- Request DTO
- Validation
- Entity Factory Method
- Repository save
- Primary Key
- Constraint
- Data Integrity
- Response DTO

---

### [실무]

Request DTO:

```java
public record PostCreateRequest(
        @NotBlank
        @Size(max = 100)
        String title,

        @NotBlank
        String content
) {
}
```

Entity 생성:

```java
public static Post create(String title, String content) {
    Post post = new Post();
    post.title = title;
    post.content = content;
    post.status = PostStatus.DRAFT;
    return post;
}
```

Service:

```java
@Transactional
public PostResponse createPost(PostCreateRequest request) {
    Post post = Post.create(request.title(), request.content());
    Post savedPost = postRepository.save(post);

    return PostResponse.from(savedPost);
}
```

권장:

- Request DTO에 Validation 적용
- Entity 생성은 Constructor 또는 Factory Method로 통제
- 필수 Field와 기본값 설정 확인
- Repository save는 신규 Entity 저장에 사용
- Unique Constraint는 Service 검증과 DB Constraint를 함께 사용
- Response DTO로 응답

주의:

- RequestBody로 Entity 직접 수신 금지
- Controller에서 Repository 직접 호출 지양
- Entity 생성 시 필수 Field 누락 주의
- 기본값 설정 위치를 일관화
- DB Constraint 위반 예외 처리 필요

---

### [FAQ]

Q. Create API에서 Entity를 RequestBody로 받아도 돼?
A. 권장하지 않는다. Request DTO로 입력을 받고 Service에서 Entity를 생성하는 것이 안전하다.

Q. 신규 Entity 저장은 save를 써도 돼?
A. 그렇다. 신규 Entity 저장에는 Repository save를 사용한다.

Q. 생성 시 기본값은 어디서 설정해?
A. Entity Field 초기값, Factory Method, Service 중 하나로 정하고 프로젝트 기준을 통일한다.

Q. Create Flow에서 Constraint는 어떻게 검토해?
A. DTO Validation, Service 중복 검증, DB Constraint를 함께 검토한다.

---

## 2.2 Read Flow

### [개념]

Read Flow는 Repository Query로 Entity 또는 DTO Projection을 조회하고 Response DTO로 변환해 반환하는 흐름이다.

Read Flow에서는 readOnly Transaction, Fetch Strategy, DTO Projection, N+1, Pagination을 함께 검토해야 한다.

---

### [핵심]

Read Flow:

```text
Client Request
→ Controller
→ Service @Transactional(readOnly = true)
→ Repository Query
→ Entity / DTO Projection 조회
→ DTO 변환
→ Response
```

핵심 키워드:

- readOnly Transaction
- Repository Query
- Query Method
- JPQL
- DTO Projection
- Fetch Join
- Lazy Loading
- N+1
- Page
- Slice

---

### [실무]

단건 조회:

```java
@Transactional(readOnly = true)
public PostResponse getPost(Long postId) {
    Post post = postRepository.findByIdWithUser(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

    return PostResponse.from(post);
}
```

Repository:

```java
@Query("""
    select p
    from Post p
    join fetch p.user
    where p.postId = :postId
""")
Optional<Post> findByIdWithUser(Long postId);
```

목록 Projection:

```java
@Query("""
    select new com.example.post.PostSummaryResponse(
        p.postId,
        p.title,
        u.nickname,
        p.createdAt
    )
    from Post p
    join p.user u
    where p.deleted = false
    order by p.createdAt desc
""")
Slice<PostSummaryResponse> findPostSummaries(Pageable pageable);
```

권장:

- 조회 Service에는 readOnly Transaction 적용
- 단건 상세는 필요한 연관 Entity Fetch Join 검토
- 목록 Read-only는 DTO Projection 검토
- Pagination은 Page / Slice 기준 명확화
- DTO 변환 중 Lazy 접근 확인
- SQL 로그로 Query 수 확인

주의:

- Entity를 그대로 Response로 반환하지 않음
- 목록 조회에서 findAll 남용 금지
- Page.map 내부 N+1 주의
- Collection Fetch Join + Pagination 조합 주의
- Projection 결과는 Managed Entity가 아님

---

### [FAQ]

Q. Read Flow에서 readOnly Transaction은 왜 써?
A. 조회 전용 의도를 명확히 하고 Lazy Loading / DTO 변환 범위를 통제하기 위해 사용한다.

Q. 목록 조회에는 Entity 조회와 Projection 중 뭐가 좋아?
A. 읽기 전용 목록이고 필요한 Field가 명확하면 DTO Projection이 적합한 경우가 많다.

Q. 단건 조회에서는 Fetch Join을 써도 돼?
A. 필요한 연관 Entity가 명확하면 Fetch Join을 사용할 수 있다.

Q. Read Flow에서 가장 많이 생기는 문제는 뭐야?
A. DTO 변환 중 Lazy Loading으로 인한 N+1과 Entity 직접 반환 문제다.

---

## 2.3 Update Flow

### [개념]

Update Flow는 Service Transaction 안에서 Entity를 조회한 뒤 상태 변경 Method를 호출하고 Dirty Checking으로 변경을 반영하는 흐름이다.

Update Flow에서는 Detached Entity save / merge 남용을 피해야 한다.

---

### [핵심]

Update Flow:

```text
Client Request
→ Controller
→ Request DTO
→ Service @Transactional
→ Repository findById
→ Managed Entity 조회
→ 권한 / 상태 검증
→ Entity.update()
→ Dirty Checking
→ Flush / Commit
→ Response
```

핵심 키워드:

- Managed Entity
- Dirty Checking
- Transaction
- Update Method
- Request DTO
- Detached Entity
- merge Caution
- save Caution

---

### [실무]

Request DTO:

```java
public record PostUpdateRequest(
        @NotBlank
        @Size(max = 100)
        String title,

        @NotBlank
        String content
) {
}
```

Service:

```java
@Transactional
public PostResponse updatePost(Long postId, PostUpdateRequest request) {
    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

    post.update(request.title(), request.content());

    return PostResponse.from(post);
}
```

Entity:

```java
public void update(String title, String content) {
    this.title = title;
    this.content = content;
}
```

권장:

- 수정 대상 Entity를 Transaction 안에서 조회
- Entity 상태 변경 Method 사용
- update 후 불필요한 save 반복 지양
- 권한 검증과 상태 검증 후 변경
- DTO 값만 필요한 Field에 반영
- SQL UPDATE 로그 확인

주의:

- Detached Entity를 save / merge로 덮어쓰기 금지
- RequestBody Entity 직접 수신 금지
- readOnly Transaction에서 수정 금지
- Setter 전체 공개로 무분별 변경 금지
- 변경 Method 없이 Field 직접 변경 남용 금지

---

### [FAQ]

Q. Update Flow에서 save를 다시 호출해야 해?
A. Managed Entity를 Transaction 안에서 변경했다면 Dirty Checking으로 반영될 수 있어 save가 필수는 아니다.

Q. 수정 API에서 Entity를 새로 만들어 save하면 안 돼?
A. 기존 값 덮어쓰기와 연관관계 손실 위험이 있으므로 Transaction 안에서 조회 후 변경하는 방식이 안전하다.

Q. Update Flow에서 가장 중요한 것은 뭐야?
A. Service Transaction 안에서 Managed Entity를 조회하고 Entity 상태 변경 Method를 호출하는 것이다.

Q. update 후 SQL이 안 나가면 뭘 확인해?
A. Transaction, readOnly 여부, Managed 상태, 변경 Method 호출 여부, Flush / Commit 시점을 확인한다.

---

## 2.4 Delete Flow

### [개념]

Delete Flow는 Entity 삭제 또는 Soft Delete 상태 변경을 처리하는 흐름이다.

Delete Flow에서는 Cascade, orphanRemoval, Foreign Key Constraint, Soft Delete 정책을 반드시 함께 검토해야 한다.

---

### [핵심]

Delete 방식:

- Hard Delete
- Soft Delete
- Cascade Remove
- orphanRemoval
- Bulk Delete
- Status Change

Delete Flow:

```text
Client Request
→ Service @Transactional
→ Entity 조회
→ 삭제 가능 여부 검증
→ delete() 또는 status 변경
→ Cascade / orphanRemoval 영향 확인
→ Flush / Commit
```

---

### [실무]

Soft Delete 예시:

```java
public void delete() {
    this.deleted = true;
    this.deletedAt = LocalDateTime.now();
}
```

Service:

```java
@Transactional
public void deletePost(Long postId) {
    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

    post.delete();
}
```

Hard Delete 예시:

```java
@Transactional
public void hardDeletePost(Long postId) {
    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

    postRepository.delete(post);
}
```

권장:

- 삭제 정책을 Hard Delete / Soft Delete로 명확히 결정
- 연관 Child 삭제 정책 검토
- Cascade REMOVE 범위 확인
- orphanRemoval 적용 여부 확인
- Foreign Key Constraint 위반 가능성 확인
- Soft Delete 조회 조건 누락 방지
- 삭제 전후 SQL 확인

주의:

- CascadeType.ALL은 삭제 전파를 포함한다.
- ManyToOne Cascade REMOVE는 매우 위험하다.
- Soft Delete와 Unique Constraint 충돌 가능성 검토
- Bulk Delete는 Persistence Context와 Auditing을 우회할 수 있다.
- 삭제 API는 복구 정책과 감사 요구사항을 함께 검토한다.

---

### [FAQ]

Q. Delete Flow에서 가장 먼저 정할 것은 뭐야?
A. Hard Delete인지 Soft Delete인지 삭제 정책을 먼저 정해야 한다.

Q. Soft Delete는 JPA delete를 호출해?
A. 보통 delete Method로 상태 Field를 변경하고 Dirty Checking으로 UPDATE 처리한다.

Q. Hard Delete에서 무엇을 주의해야 해?
A. Foreign Key Constraint, Cascade REMOVE, orphanRemoval, 데이터 복구 불가 문제를 주의해야 한다.

Q. 삭제에서 가장 위험한 JPA 설정은 뭐야?
A. 공유 Entity에 Cascade REMOVE 또는 CascadeType.ALL을 적용하는 것이다.

---

# 3. Performance Review

## 3.1 JPA Performance Review Concept

### [개념]

JPA Performance Review는 API 하나가 실행하는 SQL, Query 수, Join, Fetch Strategy, Pagination, Constraint, Index 필요성을 검토하는 과정이다.

JPA 성능 문제는 대부분 Entity Mapping, Repository Query, DTO 변환, Transaction 범위, Fetch Strategy에서 발생한다.

---

### [핵심]

핵심 키워드:

- Performance Review
- SQL Log
- Query Count
- N+1
- Fetch Join
- DTO Projection
- Pagination
- Count Query
- Index
- Constraint
- Transaction Time
- Bulk Query

검토 대상:

- 실행 SQL 수
- 반복 SELECT
- Join 대상
- Row 수 증가
- Count Query 비용
- Pagination 방식
- DTO 변환 Lazy 접근
- Transaction 길이
- Bulk Query 영향
- Index 필요성

---

### [실무]

Performance Review Flow:

```text
API 호출
→ SQL 로그 확인
→ Main Query 확인
→ 반복 Query 확인
→ Join / Fetch Join 확인
→ DTO 변환 위치 확인
→ Pagination Query 확인
→ Count Query 확인
→ Index 필요성 확인
→ Transaction 길이 확인
→ 개선 전략 선택
```

SQL Foundation 연결:

```text
SQL WHERE
→ Index 후보

SQL JOIN
→ Fetch Join / Join Cost 검토

SQL ORDER BY
→ Sort Index 검토

SQL LIMIT / OFFSET
→ Pagination Cost 검토

SQL SELECT 반복
→ N+1 Problem
```

권장:

- API 단위로 SQL 로그 확인
- Query 수와 Query 형태를 함께 확인
- 목록 API는 N+1 우선 검토
- Pagination은 Count Query와 Sort 확인
- Read-only 목록은 Projection 검토
- Transaction 안 외부 호출과 긴 처리 제거
- 개선 전후 SQL 비교

주의:

- Query 수가 적어도 Row 수가 많으면 느릴 수 있다.
- Fetch Join으로 Query 수를 줄여도 데이터 양이 늘 수 있다.
- Index는 DB 설계와 SQL 실행 계획 기준으로 검토해야 한다.
- JPA 설정 변경보다 Query 구조 개선이 우선일 수 있다.
- 성능은 테스트 데이터가 충분해야 드러난다.

---

### [FAQ]

Q. JPA Performance Review는 뭐야?
A. API가 실행하는 SQL, Query 수, Fetch Strategy, Pagination, Index 필요성을 검토하는 과정이다.

Q. JPA 성능 문제는 어디서 많이 생겨?
A. DTO 변환 중 Lazy Loading, N+1, Fetch Join 남용, Pagination Count Query, findAll 남용에서 자주 생긴다.

Q. 성능 검토에서 가장 먼저 볼 것은 뭐야?
A. SQL 로그와 Query 수를 먼저 확인한다.

Q. Query 수가 적으면 성능 문제가 없는 거야?
A. 아니다. Join으로 가져오는 Row 수가 많거나 Count Query가 비싸면 느릴 수 있다.

---

## 3.2 SQL Log Review

### [개념]

SQL Log Review는 JPA가 실제로 생성하고 실행한 SQL을 확인하는 검수 과정이다.

JPA 코드는 추상화되어 있으므로 최종 판단은 생성 SQL 기준으로 해야 한다.

---

### [핵심]

확인 항목:

- SELECT Query 수
- INSERT / UPDATE / DELETE 발생 여부
- 반복 SELECT
- JOIN SQL
- WHERE 조건
- ORDER BY
- LIMIT / OFFSET
- COUNT Query
- Parameter Binding
- Constraint Error

SQL Log Review 기준:

```text
JPA Code
→ Generated SQL
→ Query Count
→ Query Shape
→ Performance Risk
→ Correction
```

---

### [실무]

설정 후보:

```properties
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.format_sql=true
logging.level.org.hibernate.SQL=debug
logging.level.org.hibernate.orm.jdbc.bind=trace
```

검토 예시:

```text
select p.*
from posts p
where p.deleted = false
order by p.created_at desc
limit ?

select u.*
from users u
where u.user_id = ?
```

해석:

```text
Post 목록 조회 후 User 반복 조회
→ Post.user Lazy 접근 가능성
→ N+1 검토
```

권장:

- 기능 개발 후 SQL 로그 확인
- 목록 API는 반복 SELECT 확인
- 수정 API는 UPDATE 발생 여부 확인
- 삭제 API는 DELETE 또는 UPDATE Soft Delete 확인
- Pagination API는 Count Query 확인
- Native Query는 직접 SQL 실행 결과 확인

주의:

- show-sql만으로 Parameter 값 확인이 부족할 수 있다.
- 운영 환경에서 과도한 SQL 로그는 성능과 보안 문제가 될 수 있다.
- SQL 로그에 민감정보가 남을 수 있다.
- 로그 확인은 개발 / 테스트 환경 중심으로 수행
- Query Plan 분석은 DB 성능 문서와 연결한다.

---

### [FAQ]

Q. SQL Log Review는 왜 필요해?
A. JPA가 실제 어떤 SQL을 실행하는지 확인해야 성능과 Mapping 문제를 판단할 수 있기 때문이다.

Q. SQL 로그에서 가장 먼저 볼 것은 뭐야?
A. Query 수, 반복 SELECT, Join, Count Query, UPDATE / DELETE 발생 여부를 확인한다.

Q. JPA 코드만 보고 성능을 판단해도 돼?
A. 권장하지 않는다. 반드시 생성 SQL과 Query 수를 확인해야 한다.

Q. 운영 환경에서도 SQL 로그를 자세히 켜도 돼?
A. 권장하지 않는다. 성능 저하와 민감정보 노출 위험이 있어 개발 / 테스트 중심으로 사용한다.

---

# 4. Troubleshooting

## 4.1 Entity Mapping Error Troubleshooting

### [개념]

Entity Mapping Error Troubleshooting은 JPA Entity와 DB Table / Column / Association Mapping이 맞지 않아 발생하는 오류를 분석하는 과정이다.

Mapping 오류는 Application Startup, Query 실행, Flush, Schema 생성 시점에 발생할 수 있다.

---

### [핵심]

주요 원인:

- `@Entity` 누락
- `@Id` 누락
- 기본 생성자 없음
- Table 이름 불일치
- Column 이름 불일치
- nullable / length 불일치
- Enum Mapping 오류
- `mappedBy` 값 오류
- `@JoinColumn` 이름 오류
- FK Constraint 불일치
- JPQL Entity / Field 이름 오류
- Native Query Table / Column 이름 오류

Debug Flow:

```text
Error Message 확인
→ Entity Class 확인
→ @Entity / @Id 확인
→ Table / Column 이름 확인
→ Association Mapping 확인
→ mappedBy / JoinColumn 확인
→ JPQL / Native Query 이름 기준 확인
→ DB Schema 확인
```

---

### [실무]

mappedBy 오류 예시:

```java
@OneToMany(mappedBy = "post_id")
private List<Comment> comments = new ArrayList<>();
```

문제:

```text
mappedBy에 DB Column 이름 사용
→ 상대 Entity Field 이름이 아님
→ Mapping Error
```

개선:

```java
@OneToMany(mappedBy = "post")
private List<Comment> comments = new ArrayList<>();
```

JPQL 오류 예시:

```java
@Query("""
    select *
    from posts
    where post_id = :postId
""")
Optional<Post> findPost(Long postId);
```

개선:

```java
@Query("""
    select p
    from Post p
    where p.postId = :postId
""")
Optional<Post> findPost(Long postId);
```

권장:

- Error Message에서 Entity / Field 이름 확인
- JPQL과 Native Query 이름 기준 구분
- `mappedBy`는 상대 Entity Field 이름 사용
- `@JoinColumn`은 DB FK Column 이름 사용
- DB Schema와 Entity Mapping 비교
- Application Startup Error를 무시하지 않음

주의:

- JPQL은 Table / Column 이름을 쓰지 않는다.
- Native Query는 Entity / Field 이름을 쓰지 않는다.
- Column Naming Strategy에 의존하면 예상과 다른 이름이 될 수 있다.
- Schema 자동 생성 설정과 실제 운영 DB가 다를 수 있다.
- Mapping 오류는 테스트 데이터가 없으면 늦게 발견될 수 있다.

---

### [FAQ]

Q. Entity Mapping Error가 나면 무엇부터 확인해?
A. `@Entity`, `@Id`, 기본 생성자, Table / Column 이름, Association Mapping을 먼저 확인한다.

Q. mappedBy 오류는 왜 자주 생겨?
A. `mappedBy`에 DB Column 이름을 쓰는 실수가 많기 때문이다. 상대 Entity Field 이름을 써야 한다.

Q. JPQL 오류에서 가장 흔한 원인은 뭐야?
A. Entity / Field 이름 대신 Table / Column 이름을 사용하는 것이다.

Q. Native Query 오류에서 가장 흔한 원인은 뭐야?
A. 실제 DB Table / Column 이름과 Query 이름이 일치하지 않는 것이다.

---

## 4.2 Dirty Checking Troubleshooting

### [개념]

Dirty Checking Troubleshooting은 Entity 변경이 DB UPDATE로 반영되지 않는 문제를 분석하는 과정이다.

핵심은 Transaction 범위, Managed Entity 상태, readOnly 설정, Flush / Commit 시점을 확인하는 것이다.

---

### [핵심]

주요 원인:

- `@Transactional` 없음
- readOnly Transaction에서 수정
- Detached Entity 수정
- Entity를 조회하지 않고 새 객체 수정
- 변경 Method 호출 누락
- 변경 값이 기존 값과 동일
- Flush 전 SQL 확인
- 예외로 Rollback 발생
- Bulk Query 후 Persistence Context 불일치

Debug Flow:

```text
Update API 호출
→ Service @Transactional 확인
→ readOnly 여부 확인
→ Entity 조회 위치 확인
→ Managed 상태 확인
→ 변경 Method 호출 확인
→ Flush / Commit 확인
→ UPDATE SQL 확인
→ Rollback 여부 확인
```

---

### [실무]

문제 예시:

```java
public void updatePost(Long postId, PostUpdateRequest request) {
    Post post = postRepository.findById(postId).orElseThrow();
    post.update(request.title(), request.content());
}
```

개선:

```java
@Transactional
public void updatePost(Long postId, PostUpdateRequest request) {
    Post post = postRepository.findById(postId).orElseThrow();
    post.update(request.title(), request.content());
}
```

문제 예시:

```java
@Transactional(readOnly = true)
public void updatePost(Long postId, PostUpdateRequest request) {
    Post post = postRepository.findById(postId).orElseThrow();
    post.update(request.title(), request.content());
}
```

개선:

```java
@Transactional
public void updatePost(Long postId, PostUpdateRequest request) {
    Post post = postRepository.findById(postId).orElseThrow();
    post.update(request.title(), request.content());
}
```

권장:

- 수정 Method는 일반 `@Transactional`
- Entity를 Transaction 안에서 조회
- Entity 상태 변경 Method 호출
- SQL UPDATE 로그 확인
- 테스트에서 flush로 반영 시점 확인 가능
- 예외 발생으로 Rollback되는지 확인

주의:

- update 후 save가 없어서 문제가 아니라 Transaction / Managed 상태가 문제인 경우가 많다.
- readOnly Transaction에서는 변경 반영을 기대하지 않음
- Detached Entity는 Dirty Checking 대상이 아니다.
- UPDATE SQL이 안 나가도 변경 값이 동일한 경우일 수 있다.
- Bulk Query는 Dirty Checking과 별개다.

---

### [FAQ]

Q. Dirty Checking이 안 되면 무엇부터 확인해?
A. Service Method의 `@Transactional`, readOnly 여부, Entity Managed 상태, UPDATE SQL 로그를 확인한다.

Q. update 후 save를 안 해서 반영이 안 된 거야?
A. Managed Entity라면 save가 필수는 아니다. Transaction과 Entity 상태를 먼저 확인해야 한다.

Q. readOnly Transaction에서 수정하면 어떻게 돼?
A. 변경 반영을 기대하지 않아야 하며 수정 Method는 일반 Transaction을 사용해야 한다.

Q. Detached Entity를 수정하면 Dirty Checking이 돼?
A. 아니다. Detached Entity는 Persistence Context가 관리하지 않으므로 Dirty Checking 대상이 아니다.

---

## 4.3 LazyInitializationException Troubleshooting

### [개념]

LazyInitializationException Troubleshooting은 Transaction 종료 후 Lazy Association 접근으로 발생하는 예외를 해결하는 절차다.

핵심은 Entity 직접 반환을 제거하고 필요한 데이터를 Service Transaction 안에서 조회 / 변환하는 것이다.

---

### [핵심]

주요 원인:

- Entity 직접 반환
- DTO 변환이 Transaction 밖에서 수행
- Controller에서 Lazy Field 접근
- JSON 직렬화 중 Lazy Field 접근
- OSIV 의존
- Fetch Join 누락
- Projection 누락

Debug Flow:

```text
Exception 발생 위치 확인
→ Lazy Field 확인
→ Transaction 종료 여부 확인
→ Entity 직접 반환 여부 확인
→ DTO 변환 위치 확인
→ Fetch Join / Projection 필요성 확인
→ SQL Query 수 확인
```

---

### [실무]

문제 예시:

```java
@GetMapping("/{id}")
public Post getPost(@PathVariable Long id) {
    return postService.getPostEntity(id);
}
```

개선:

```java
@GetMapping("/{id}")
public PostResponse getPost(@PathVariable Long id) {
    return postService.getPost(id);
}
```

Service:

```java
@Transactional(readOnly = true)
public PostResponse getPost(Long postId) {
    Post post = postRepository.findByIdWithUser(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

    return PostResponse.from(post);
}
```

Repository:

```java
@Query("""
    select p
    from Post p
    join fetch p.user
    where p.postId = :postId
""")
Optional<Post> findByIdWithUser(Long postId);
```

권장:

- Entity 직접 반환 금지
- DTO 변환을 Service Transaction 안에서 수행
- 필요한 연관 Entity는 Fetch Join
- Read-only 목록은 DTO Projection
- OSIV 의존 지양
- 해결 후 N+1 여부 확인

주의:

- EAGER로 바꾸는 것은 권장 해결책이 아니다.
- Fetch Join을 추가해도 다른 Lazy Field 접근이 남아 있으면 예외가 날 수 있다.
- OSIV가 켜져 있으면 예외 대신 성능 문제가 숨을 수 있다.
- JSON 직렬화에 Entity를 넘기지 않는다.
- DTO from Method 내부 Lazy 접근도 점검한다.

---

### [FAQ]

Q. LazyInitializationException이 나면 뭘 먼저 확인해?
A. Lazy Field 접근 위치와 Transaction이 종료되었는지 먼저 확인한다.

Q. LazyInitializationException은 EAGER로 바꾸면 해결돼?
A. 권장하지 않는다. Fetch Join, DTO Projection, Service Transaction 안 DTO 변환을 우선 적용한다.

Q. Entity 직접 반환을 없애면 도움이 돼?
A. 그렇다. JSON 직렬화 중 Lazy Field 접근을 막고 API 구조를 안정화할 수 있다.

Q. Fetch Join을 했는데도 예외가 나면?
A. DTO 변환에서 접근하는 모든 Lazy Association이 조회되었는지 확인해야 한다.

---

## 4.4 N+1 Troubleshooting

### [개념]

N+1 Troubleshooting은 API 실행 중 반복 SELECT가 발생하는 원인을 찾고 Fetch Join, Projection, Batch Size, API 구조 변경으로 해결하는 절차다.

N+1은 목록 조회와 DTO 변환에서 가장 자주 발생한다.

---

### [핵심]

주요 원인:

- 목록 Entity 조회 후 연관 Entity 반복 접근
- DTO from Method 내부 Lazy Field 접근
- Page.map / Slice.map 내부 Lazy Field 접근
- EAGER Association 반복 조회
- Entity 직접 JSON 직렬화
- Collection Association 접근
- Fetch Join 누락
- Projection 미사용

Debug Flow:

```text
API 호출
→ SQL 로그 확인
→ 반복 SELECT Table 확인
→ DTO 변환 Method 확인
→ Lazy Field 접근 위치 확인
→ ManyToOne / OneToMany 구분
→ 해결 전략 선택
→ SQL 재확인
```

---

### [실무]

문제 예시:

```java
@Transactional(readOnly = true)
public List<PostResponse> getPosts() {
    return postRepository.findAll().stream()
            .map(PostResponse::from)
            .toList();
}
```

DTO:

```java
public static PostResponse from(Post post) {
    return new PostResponse(
            post.getPostId(),
            post.getTitle(),
            post.getUser().getNickname()
    );
}
```

해결 1 — Fetch Join:

```java
@Query("""
    select p
    from Post p
    join fetch p.user
    where p.deleted = false
    order by p.createdAt desc
""")
List<Post> findPostsWithUser();
```

해결 2 — DTO Projection:

```java
@Query("""
    select new com.example.post.PostResponse(
        p.postId,
        p.title,
        u.nickname
    )
    from Post p
    join p.user u
    where p.deleted = false
    order by p.createdAt desc
""")
List<PostResponse> findPostResponses();
```

해결 선택 기준:

```text
ManyToOne 정보 전체 필요
→ Fetch Join

필요 Field 일부만 필요
→ DTO Projection

OneToMany Collection + Pagination
→ Child Repository 별도 조회 / Batch Size

여러 Collection 필요
→ API 구조 변경 검토
```

권장:

- SQL 로그에서 반복 SELECT 확인
- 반복 대상 Table과 Entity Association 연결
- DTO 변환 내부 getter 확인
- 해결 후 Query 수와 Row 수 재확인
- Projection과 Fetch Join을 API 목적에 맞게 선택

주의:

- Fetch Join 남용은 데이터 양 폭증 가능
- Collection Fetch Join + Pagination은 위험
- DTO Projection은 수정 로직에 사용하지 않음
- Batch Size는 완화 전략
- EAGER 변경은 권장 해결책이 아님

---

### [FAQ]

Q. N+1 문제는 어떻게 찾는 게 좋아?
A. SQL 로그에서 API 하나가 실행하는 Query 수와 반복 SELECT 대상 Table을 확인한다.

Q. DTO from Method가 N+1 원인이 될 수 있어?
A. 그렇다. Lazy Association getter를 호출하면 목록 변환 중 반복 Query가 발생할 수 있다.

Q. N+1은 Fetch Join으로만 해결해?
A. 아니다. Fetch Join, DTO Projection, Batch Size, 별도 Query, API 구조 변경 중 선택한다.

Q. OneToMany N+1은 어떻게 해결해?
A. Collection Fetch Join보다 Child Repository 별도 Pagination, Batch Size, API 구조 변경을 우선 검토한다.

---

# 5. Data Integrity Troubleshooting

## 5.1 Constraint Violation Troubleshooting

### [개념]

Constraint Violation Troubleshooting은 DB Constraint 위반으로 INSERT / UPDATE / DELETE가 실패하는 문제를 분석하는 절차다.

JPA Mapping Annotation, DTO Validation, DB Schema, Migration 결과를 함께 확인해야 한다.

---

### [핵심]

주요 원인:

- NOT NULL 위반
- UNIQUE 위반
- Foreign Key 위반
- Length 초과
- Enum 값 불일치
- Check Constraint 위반
- Soft Delete와 Unique 충돌
- DTO Validation 누락
- DB Schema와 Entity Mapping 불일치

Debug Flow:

```text
Exception Message 확인
→ 위반 Constraint 이름 확인
→ Entity @Column / @JoinColumn 확인
→ Request DTO Validation 확인
→ Service 검증 확인
→ DB Schema 확인
→ Migration 확인
→ Exception Handling 확인
```

---

### [실무]

Unique 위반 예시:

```java
if (userRepository.existsByEmail(request.email())) {
    throw new BusinessException("EMAIL_DUPLICATED", "이미 사용 중인 이메일입니다.");
}
```

DB Constraint:

```java
@Column(nullable = false, unique = true, length = 100)
private String email;
```

Foreign Key 위반 예시:

```text
Post.user_id
→ 존재하지 않는 users.user_id 참조
→ FK Constraint Violation
```

권장:

- DTO Validation으로 입력 오류 조기 차단
- Service에서 비즈니스 중복 검증
- DB Constraint로 최종 Data Integrity 보장
- Constraint 이름을 명확히 지정
- GlobalExceptionHandler에서 사용자 친화적 응답 변환
- 동시성 중복은 DB Unique로 최종 방어

주의:

- Service existsBy만으로 Race Condition을 완전히 막을 수 없다.
- DB Unique Constraint가 최종 방어선이다.
- Soft Delete와 Unique Constraint 조합은 별도 정책 필요
- FK Constraint 위반은 Association 설정과 삭제 순서를 함께 봐야 한다.
- 운영 DB Schema가 Entity Annotation과 다를 수 있다.

---

### [FAQ]

Q. Constraint Violation이 나면 뭘 먼저 확인해?
A. 예외 메시지의 Constraint 이름, Entity Mapping, DTO Validation, DB Schema를 확인한다.

Q. Unique 중복은 existsBy로 충분해?
A. 아니다. 동시성 상황에서는 DB Unique Constraint가 최종 방어선이다.

Q. Foreign Key 위반은 왜 발생해?
A. 존재하지 않는 Parent를 참조하거나 삭제 순서 / Cascade 설정이 잘못되었을 때 발생할 수 있다.

Q. Constraint 예외는 어디서 응답으로 바꿔?
A. GlobalExceptionHandler에서 Custom Error Response로 변환한다.

---

## 5.2 Data Integrity Review

### [개념]

Data Integrity Review는 Entity Mapping, Constraint, Validation, Transaction, Repository Query가 데이터 일관성을 보장하는지 검수하는 과정이다.

Data Integrity는 Application Validation만으로 완성되지 않고 DB Constraint와 Transaction 정책을 함께 사용해야 한다.

---

### [핵심]

검토 대상:

- Primary Key 안정성
- Foreign Key Constraint
- NOT NULL
- UNIQUE
- CHECK
- DTO Validation
- Service Business Validation
- Transaction Boundary
- Cascade / orphanRemoval
- Soft Delete
- Bulk Query
- Concurrent Request

Review Flow:

```text
Entity Mapping 확인
→ DTO Validation 확인
→ Service Validation 확인
→ DB Constraint 확인
→ Transaction Boundary 확인
→ Cascade 삭제 영향 확인
→ Bulk Query 영향 확인
→ Exception Handling 확인
```

---

### [실무]

중복 방지 구조:

```text
Request DTO Validation
→ Service existsBy 검증
→ Repository save
→ DB Unique Constraint
→ Constraint Violation Exception Handling
```

관계 무결성 구조:

```text
Request userId 수신
→ Service에서 User 조회
→ Entity Association 설정
→ FK Constraint 검증
→ Commit
```

권장:

- ID만 받은 뒤 Service에서 Entity 조회
- 존재하지 않는 Parent 참조 방지
- 필수 관계는 `nullable = false`
- DB FK Constraint 확인
- Unique는 Service 검증 + DB Constraint
- 삭제는 FK / Cascade / orphanRemoval 영향 검토

주의:

- DTO Validation은 DB 무결성의 대체재가 아니다.
- DB Constraint 없이 Application 검증만 있으면 우회 가능성이 있다.
- Bulk Query는 Entity Rule과 Auditing을 우회할 수 있다.
- Soft Delete는 Query 조건 누락과 Unique 충돌을 만든다.
- 동시성 문제는 DB Constraint와 Lock 전략까지 검토할 수 있다.

---

### [FAQ]

Q. Data Integrity Review는 뭐야?
A. Entity Mapping, Validation, DB Constraint, Transaction이 데이터 일관성을 보장하는지 검토하는 과정이다.

Q. Application Validation만으로 충분해?
A. 아니다. DB Constraint가 최종 방어선으로 필요하다.

Q. Foreign Key Data Integrity는 어떻게 보장해?
A. Service에서 Parent Entity를 조회하고 Association을 설정하며 DB FK Constraint를 함께 확인한다.

Q. Soft Delete는 Data Integrity에 어떤 영향을 줘?
A. 조회 조건 누락, Unique Constraint 충돌, 복구 정책 문제를 만들 수 있다.

---

# 6. JPA Anti Pattern

## 6.1 Entity Anti Pattern

### [개념]

Entity Anti Pattern은 Entity를 Persistence Model이 아닌 API 객체, 화면 객체, 무분별한 데이터 컨테이너로 사용하는 잘못된 설계다.

Entity Anti Pattern은 API 결합, Lazy Loading, 보안, Dirty Checking, 유지보수 문제를 만든다.

---

### [핵심]

Anti Pattern:

- Entity를 API Response로 직접 반환
- RequestBody로 Entity 직접 수신
- Entity에 `@Data` 사용
- Entity에 전체 Setter 공개
- Entity에 화면 전용 Field 추가
- Entity에 DTO 역할 부여
- Entity에 복잡한 Presentation Logic 추가
- equals / hashCode에 Association 포함
- toString에 Association 포함
- 모든 연관관계를 양방향으로 설계

---

### [실무]

나쁜 예:

```java
@PostMapping
public User createUser(@RequestBody User user) {
    return userRepository.save(user);
}
```

문제:

```text
RequestBody Entity 직접 수신
Entity 직접 반환
Service Transaction 흐름 없음
Validation 책임 불명확
민감정보 노출 가능
API와 Entity 강결합
```

개선:

```java
@PostMapping
public UserResponse createUser(@Valid @RequestBody UserCreateRequest request) {
    return userService.createUser(request);
}
```

권장:

- Entity는 Persistence Model로 유지
- DTO와 Entity 분리
- 상태 변경 Method 사용
- `@Data` 사용 지양
- Association Field를 equals / hashCode / toString에서 제외
- API Response는 Response DTO 사용

주의:

- Entity 직접 반환은 작은 프로젝트에서도 습관화되면 위험하다.
- Lombok 편의 기능은 JPA Entity에서 신중히 사용
- 화면 요구사항을 Entity에 직접 추가하지 않음
- Entity 구조 변경이 API 변경으로 이어지지 않게 분리
- Entity 노출은 Lazy Loading과 보안 문제를 동시에 만든다.

---

### [FAQ]

Q. Entity Anti Pattern에서 가장 위험한 것은 뭐야?
A. Entity를 RequestBody로 받고 Response로 직접 반환하는 것이다.

Q. Entity에 `@Data`를 쓰면 왜 위험해?
A. Setter, equals, hashCode, toString이 무분별하게 생성되어 JPA 상태 관리와 Lazy Loading 문제를 만들 수 있다.

Q. Entity에 화면 전용 Field를 넣어도 돼?
A. 권장하지 않는다. 화면 전용 값은 Response DTO나 Projection DTO에서 처리한다.

Q. Entity 직접 반환은 왜 보안 문제야?
A. password, role, internal status 같은 민감 Field가 노출될 수 있기 때문이다.

---

## 6.2 Repository Anti Pattern

### [개념]

Repository Anti Pattern은 Repository가 Data Access 책임을 넘어 비즈니스 로직, 대량 메모리 필터링, 불명확한 Query를 수행하는 잘못된 설계다.

Repository는 Entity 조회와 저장을 담당하고, 비즈니스 흐름은 Service에서 관리해야 한다.

---

### [핵심]

Anti Pattern:

- Repository에 비즈니스 로직 작성
- `findAll` 후 Java Stream 필터링
- 대량 데이터를 List로 전부 조회
- Query Method 이름 과도하게 길어짐
- JPQL에서 Table / Column 이름 사용
- Native Query 남용
- Projection 없이 Entity 전체 조회
- Pagination 없이 목록 조회
- QueryDSL이 필요한 동적 Query를 Query Method로 억지 작성
- SQL 로그 확인 없이 Query 작성

---

### [실무]

나쁜 예:

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
전체 Entity 조회
DB Filtering 미사용
메모리 필터링
N+1 가능
Pagination 없음
```

개선:

```java
Slice<Post> findByTitleContainingAndDeletedFalseOrderByCreatedAtDesc(String keyword, Pageable pageable);
```

동적 조건 개선 후보:

```text
keyword optional
region optional
category optional
date optional
→ QueryDSL 전환
```

권장:

- Filtering은 DB Query로 처리
- 대량 목록은 Pagination 적용
- 단순 조건은 Query Method
- 고정 Query는 JPQL
- 동적 조건은 QueryDSL
- DB 특화 Query는 Native Query 제한 사용
- Query 작성 후 SQL 확인

주의:

- Repository Method가 길어지면 유지보수성이 떨어진다.
- findAll 남용은 테스트 데이터에서는 문제를 숨긴다.
- Native Query는 DB 종속성을 만든다.
- Projection 없이 Entity 전체 조회하면 Fetch 문제가 커질 수 있다.
- Repository에 권한 정책을 넣지 않는다.

---

### [FAQ]

Q. Repository Anti Pattern에서 가장 흔한 것은 뭐야?
A. findAll 후 Java Stream으로 필터링하는 것이다.

Q. Filtering은 Java Stream으로 하면 안 돼?
A. 대량 데이터에서는 DB WHERE 조건으로 처리해야 성능과 Pagination이 안정적이다.

Q. Repository에 비즈니스 로직을 넣으면 왜 안 좋아?
A. Data Access와 Business Flow가 섞여 Transaction과 테스트 책임이 불명확해진다.

Q. Query Method가 길어지면 어떻게 해?
A. JPQL 또는 QueryDSL로 분리한다. 동적 조건이 많으면 QueryDSL이 적합하다.

---

## 6.3 Service Transaction Anti Pattern

### [개념]

Service Transaction Anti Pattern은 Transaction 범위가 없거나, readOnly와 write를 혼동하거나, 예외 처리로 Rollback을 방해하는 잘못된 설계다.

Service는 JPA Entity 상태 변경과 Persistence Context 생명주기를 관리하는 핵심 Layer다.

---

### [핵심]

Anti Pattern:

- 수정 Method에 `@Transactional` 없음
- readOnly Transaction에서 Entity 수정
- Controller에 Transaction 적용
- Repository에 Transaction 흐름 분산
- Entity를 Transaction 밖에서 변경
- Detached Entity를 save / merge로 수정
- 예외 catch 후 삼킴
- CheckedException Rollback 누락
- Transaction 안에서 긴 외부 API 호출
- Self Invocation으로 Transaction 누락
- DTO 변환을 Transaction 밖에서 수행

---

### [실무]

나쁜 예:

```java
@Transactional(readOnly = true)
public void updateUser(Long userId, UserUpdateRequest request) {
    User user = userRepository.findById(userId).orElseThrow();
    user.updateNickname(request.nickname());
}
```

개선:

```java
@Transactional
public void updateUser(Long userId, UserUpdateRequest request) {
    User user = userRepository.findById(userId).orElseThrow();
    user.updateNickname(request.nickname());
}
```

나쁜 예:

```java
@Transactional
public void createOrder(OrderRequest request) {
    try {
        Order order = Order.create(request.userId());
        orderRepository.save(order);
    } catch (Exception e) {
        log.error("order failed", e);
    }
}
```

문제:

```text
예외 삼킴
→ Transaction 정상 종료 가능
→ Commit 가능성
→ 실패 응답 불명확
```

권장:

- 수정 Method는 일반 `@Transactional`
- 조회 Method는 `readOnly = true`
- Entity 변경은 Transaction 안에서 수행
- 예외는 필요한 경우 CustomException으로 던짐
- DTO 변환은 필요한 경우 Transaction 안에서 수행
- 외부 API 호출과 DB Transaction 순서 분리 검토

주의:

- `@Transactional`은 Proxy 기반이므로 Self Invocation 주의
- private method에 붙인 Transaction은 기대대로 동작하지 않을 수 있다.
- readOnly는 변경 방지 보안 장치가 아니다.
- 예외 처리 방식이 Rollback을 방해할 수 있다.
- Transaction 길이는 성능과 Lock에 영향을 준다.

---

### [FAQ]

Q. Service Transaction Anti Pattern에서 가장 흔한 것은 뭐야?
A. 수정 Method에 Transaction이 없거나 readOnly Transaction에서 수정하는 것이다.

Q. 예외를 catch하면 왜 Transaction 문제가 생겨?
A. 예외를 삼키면 Transaction이 정상 종료되어 Commit될 수 있기 때문이다.

Q. Detached Entity save는 왜 위험해?
A. null 덮어쓰기, 연관관계 손실, 변경 의도 불명확 문제가 생길 수 있다.

Q. Self Invocation은 왜 문제야?
A. 같은 Class 내부 호출은 Spring Proxy를 거치지 않아 `@Transactional`이 적용되지 않을 수 있다.

---

## 6.4 Fetch and Pagination Anti Pattern

### [개념]

Fetch and Pagination Anti Pattern은 Lazy Loading, EAGER 남용, Fetch Join 남용, N+1, Page.map N+1, Collection Fetch Join Pagination 문제를 만드는 설계다.

조회 성능 문제는 대부분 API 응답 DTO 변환과 SQL Query 수를 함께 확인해야 발견된다.

---

### [핵심]

Anti Pattern:

- `ManyToOne` 기본 EAGER 방치
- LazyInitializationException을 EAGER로 해결
- N+1을 EAGER로 해결
- DTO from Method에서 Lazy Field 반복 접근
- Page.map에서 Lazy Field 접근
- Entity 직접 JSON 직렬화
- Fetch Join 남용
- Collection Fetch Join + Pageable
- 여러 Collection Fetch Join
- Projection 없이 Entity 전체 조회
- Pagination 없이 대량 목록 조회
- SQL 로그 확인 없이 성능 판단

---

### [실무]

나쁜 예:

```java
@Transactional(readOnly = true)
public Page<PostResponse> getPosts(Pageable pageable) {
    return postRepository.findByDeletedFalse(pageable)
            .map(PostResponse::from);
}
```

DTO 문제:

```java
public static PostResponse from(Post post) {
    return new PostResponse(
            post.getPostId(),
            post.getTitle(),
            post.getUser().getNickname()
    );
}
```

개선 후보 1 — Fetch Join:

```java
@Query("""
    select p
    from Post p
    join fetch p.user
    where p.deleted = false
""")
Page<Post> findPageWithUser(Pageable pageable);
```

개선 후보 2 — Projection:

```java
@Query("""
    select new com.example.post.PostResponse(
        p.postId,
        p.title,
        u.nickname
    )
    from Post p
    join p.user u
    where p.deleted = false
""")
Page<PostResponse> findPostResponses(Pageable pageable);
```

권장:

- 목록 Read-only는 Projection 우선 검토
- DTO 변환 내부 Lazy 접근 확인
- ManyToOne N+1은 Fetch Join / Projection 검토
- OneToMany Pagination은 별도 Child Query 검토
- Page / Slice 선택 기준 명확화
- SQL 로그로 Query 수와 Count Query 확인

주의:

- Collection Fetch Join + Pageable은 위험하다.
- Fetch Join으로 Query 수는 줄어도 Row 수가 늘 수 있다.
- EAGER 변경은 문제를 숨길 수 있다.
- Page.map은 DTO 변환 로직에 따라 N+1이 발생한다.
- Projection DTO는 수정에 사용하지 않는다.

---

### [FAQ]

Q. Fetch and Pagination Anti Pattern에서 가장 흔한 것은 뭐야?
A. Page.map이나 DTO from Method에서 Lazy Association을 접근해 N+1을 만드는 것이다.

Q. Collection Fetch Join과 Pageable은 왜 위험해?
A. Child Row 때문에 Parent Row가 중복되어 Pagination이 불안정해질 수 있다.

Q. 목록 조회는 Fetch Join과 Projection 중 뭐가 좋아?
A. 읽기 전용 목록이고 필요한 Field가 명확하면 Projection이 적합한 경우가 많다.

Q. EAGER로 바꾸면 Fetch 문제가 해결돼?
A. 권장하지 않는다. 불필요한 조회와 N+1 문제가 숨겨지거나 확대될 수 있다.

---

# 7. Review Agent Checklist

## 7.1 JPA Backend Review Checklist

### [개념]

JPA Backend Review Checklist는 Backend Agent가 생성한 JPA 코드가 Entity, Repository, Service, Transaction, Query, DTO, Performance 기준을 만족하는지 검수하는 기준이다.

Review Agent는 API 흐름과 SQL 실행 결과를 함께 검토해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] Controller가 Entity를 직접 RequestBody로 받지 않는가?
- [ ] Controller가 Entity를 직접 Response로 반환하지 않는가?
- [ ] Request DTO와 Response DTO가 분리되어 있는가?
- [ ] Entity에 @Entity, @Id, 기본 생성자가 있는가?
- [ ] Entity에 무분별한 Setter / @Data가 없는가?
- [ ] Entity 상태 변경 Method가 있는가?
- [ ] Entity와 Table / Column Mapping이 명확한가?
- [ ] Primary Key가 안정적인 Surrogate Key인가?
- [ ] Column nullable / length / unique가 명확한가?
- [ ] EnumType.STRING을 사용하는가?
- [ ] Association의 FK 위치와 Owning Side가 맞는가?
- [ ] mappedBy 값이 상대 Entity Field 이름인가?
- [ ] ManyToOne에 FetchType.LAZY를 명시했는가?
- [ ] ManyToMany 직접 사용을 피했는가?
- [ ] Repository가 JpaRepository<Entity, IdType>을 올바르게 상속하는가?
- [ ] Repository에 비즈니스 로직이 없는가?
- [ ] findAll 후 Java Stream 필터링을 하지 않는가?
- [ ] Query Method가 Entity Field 이름 기준인가?
- [ ] JPQL이 Entity / Field 이름 기준인가?
- [ ] Native Query 사용 이유가 명확한가?
- [ ] Service public method에 Transaction Boundary가 있는가?
- [ ] 조회 Method는 readOnly Transaction인가?
- [ ] 수정 Method는 일반 Transaction인가?
- [ ] update는 Managed Entity + Dirty Checking Pattern인가?
- [ ] Detached Entity save / merge를 남용하지 않는가?
- [ ] DTO 변환 위치가 Transaction과 Lazy Loading 기준에 맞는가?
- [ ] 목록 API에서 N+1 가능성을 검토했는가?
- [ ] Page / Slice 선택 기준이 명확한가?
- [ ] Collection Fetch Join + Pagination을 피했는가?
- [ ] Cascade REMOVE / orphanRemoval 위험을 검토했는가?
- [ ] Auditing 설정이 필요한 Entity에 적용되었는가?
- [ ] SQL 로그로 Query 수와 Query 형태를 확인했는가?
- [ ] Constraint 위반 예외 처리가 있는가?
```

---

### [실무]

Review Flow:

```text
API Code 확인
→ Controller DTO 확인
→ Service Transaction 확인
→ Entity Mapping 확인
→ Repository Query 확인
→ DTO 변환 확인
→ Fetch Strategy 확인
→ Pagination 확인
→ Cascade / Delete 영향 확인
→ SQL 로그 확인
→ Anti Pattern 판단
```

Review Output Format 후보:

```text
[PASS]
- 기준 충족 항목

[WARN]
- 개선 권장 항목

[FAIL]
- 치명적 문제 항목

[FIX]
- 수정 방향

[SQL REVIEW]
- Query 수 / N+1 / Pagination / Count Query 검토
```

권장:

- Review는 코드 구조와 SQL 실행을 함께 검토
- FAIL은 데이터 손실, 보안 노출, Transaction 실패, N+1 대량 문제 중심
- WARN은 개선 여지가 있지만 즉시 장애는 아닌 항목
- FIX는 구체적 코드 방향 제시
- SQL REVIEW는 실제 Query 기준으로 작성

주의:

- Entity Mapping만 보고 JPA Review를 끝내지 않는다.
- DTO 변환 로직을 반드시 확인한다.
- Pagination과 Fetch Join 조합을 반드시 확인한다.
- Cascade 삭제 전파는 작은 코드 한 줄이어도 치명적일 수 있다.
- SQL 로그 없는 성능 판단은 신뢰도가 낮다.

---

### [FAQ]

Q. JPA Review에서 가장 먼저 볼 것은 뭐야?
A. Controller Entity 노출 여부, Service Transaction, Entity Mapping, Repository Query를 먼저 본다.

Q. Review Agent가 FAIL로 봐야 하는 항목은 뭐야?
A. Entity 직접 노출, Transaction 없는 수정, Cascade REMOVE 남용, N+1 대량 문제, Constraint 누락 같은 치명적 문제다.

Q. JPA Review에 SQL 로그가 필요한 이유는 뭐야?
A. 실제 Query 수, N+1, Join, Pagination Count Query는 SQL 로그로 확인해야 하기 때문이다.

Q. DTO 변환 로직도 Review 대상이야?
A. 그렇다. DTO 변환 중 Lazy Association 접근으로 N+1이나 LazyInitializationException이 생길 수 있다.

---

## 7.2 PM Agent Decision Checklist

### [개념]

PM Agent Decision Checklist는 기능 요구사항을 JPA 구현 작업으로 분해할 때 확인해야 하는 기준이다.

PM Agent는 Entity, Relationship, Query, Transaction, Pagination, Constraint, Performance 요구사항을 Backend Agent에게 명확히 전달해야 한다.

---

### [핵심]

PM 확인 항목:

- 어떤 Entity가 필요한가?
- 어떤 Table Relationship이 필요한가?
- Primary Key / Foreign Key는 무엇인가?
- Create / Read / Update / Delete 중 어떤 기능인가?
- 목록 조회인가 단건 조회인가?
- Pagination이 필요한가?
- 검색 조건이 동적인가?
- 연관 Entity 정보가 응답에 필요한가?
- 중복 방지가 필요한가?
- Transaction으로 묶어야 하는 작업인가?
- 삭제 정책은 Hard Delete인가 Soft Delete인가?
- Cascade가 필요한 완전 종속 Child인가?
- Auditing이 필요한가?

---

### [실무]

PM → Backend 전달 형식 후보:

```text
[Feature]
게시글 목록 조회

[Entity]
Post, User

[Relationship]
Post ManyToOne User

[Query]
deleted=false 게시글 목록
작성자 nickname 필요

[Pagination]
Slice 기반 무한 스크롤

[Fetch Strategy]
Post.user N+1 방지 필요
Projection 또는 Fetch Join 검토

[Response]
PostSummaryResponse

[Constraint]
deleted false 조건 누락 금지
```

PM 판단 Flow:

```text
Feature 분석
→ Entity 도출
→ Relationship 확인
→ CRUD 유형 구분
→ Query / Pagination 판단
→ Transaction 필요성 판단
→ Constraint / Data Integrity 판단
→ Performance Risk 전달
```

권장:

- 요구사항 단계에서 Pagination 여부를 명확히 함
- 목록 응답에 필요한 Field를 명시
- 동적 검색 조건이 있으면 QueryDSL 후보로 전달
- 중복 방지가 필요한 경우 Unique Constraint 요구
- 삭제 정책을 명확히 전달
- N+1 위험을 Backend Agent에게 전달

주의:

- "목록 조회"만 전달하면 성능 기준이 빠질 수 있다.
- "삭제"만 전달하면 Hard Delete / Soft Delete가 불명확하다.
- "작성자 정보 포함"은 Fetch Strategy 검토가 필요하다.
- "중복 불가"는 Service 검증과 DB Constraint가 모두 필요하다.
- "댓글 포함 게시글 목록"은 Collection Fetch Join Pagination 위험이 있다.

---

### [FAQ]

Q. PM Agent는 JPA 구현 전에 무엇을 정해야 해?
A. Entity, Relationship, Query 조건, Pagination, Transaction, Constraint, 삭제 정책을 정해야 한다.

Q. 목록 조회 요구사항에서 꼭 확인할 것은 뭐야?
A. Pagination 방식, 정렬 기준, 필요한 응답 Field, N+1 위험을 확인해야 한다.

Q. 삭제 기능 요구사항에서 꼭 확인할 것은 뭐야?
A. Hard Delete인지 Soft Delete인지, Cascade / orphanRemoval 영향이 있는지 확인해야 한다.

Q. 중복 방지 요구사항은 어떻게 전달해야 해?
A. Service existsBy 검증과 DB Unique Constraint가 모두 필요하다고 전달해야 한다.

---

# 8. Final Integration Flow

## 8.1 JPA Agent Work Loop

### [개념]

JPA Agent Work Loop는 PM Agent, Backend Agent, Review Agent가 JPA 기능을 설계하고 검수하는 반복 작업 흐름이다.

JPA 기능은 Entity Mapping → Repository Query → Service Transaction → DTO Response → SQL Review → Fix 순서로 진행한다.

---

### [핵심]

Work Loop:

```text
PM Requirement
→ Entity / Relationship 분석
→ Backend Agent Entity 설계
→ Repository Query 설계
→ Service Transaction 설계
→ DTO 설계
→ Review Agent 검수
→ SQL Review
→ Anti Pattern 탐지
→ Fix
→ Final Output
```

Agent 역할:

| Agent         | 역할                               |
| ------------- | ---------------------------------- |
| PM Agent      | 요구사항 분해 / 기준 전달          |
| Backend Agent | Entity / Repository / Service 구현 |
| Review Agent  | JPA Rule 검수 / Anti Pattern 탐지  |
| SQL Agent     | SQL / Index / Constraint 검토      |
| DevOps Agent  | DB Migration / 환경 설정 검토      |

---

### [실무]

JPA 기능 처리 Flow:

```text
Feature Request
→ CRUD 유형 결정
→ Entity Mapping 확인
→ Relationship 확인
→ Constraint 확인
→ Query Strategy 결정
→ Transaction Boundary 결정
→ DTO Mapping 결정
→ Fetch Strategy 결정
→ Pagination 결정
→ SQL Log Review
→ Final Code Output
```

Fix Loop:

```text
Review FAIL
→ 원인 분류
→ Entity / Repository / Service / DTO 중 위치 확인
→ Rule 재적용
→ SQL 재확인
→ PASS
```

권장:

- JPA 작업은 Part01~Part08 순서 기준으로 검토
- Entity부터 Query, Transaction, Performance 순서로 이동
- SQL Foundation 용어와 연결 유지
- QueryDSL 문법 상세는 QueryDSL Practical Rules로 연결
- Security 인증 사용자 연계는 Security Advanced Rules와 연결
- Testing은 Testing Domain Rules와 연결

주의:

- JPA 문서 하나로 모든 QueryDSL / Security / Testing 세부사항을 해결하지 않는다.
- JPA Review는 SQL Review와 분리하지 않는다.
- Entity 설계가 끝났다고 기능이 완료된 것이 아니다.
- 실제 API 성능은 Query 수와 Transaction 범위까지 확인해야 한다.
- 최종 결과는 DTO와 SQL 기준으로 검증한다.

---

### [FAQ]

Q. JPA Agent Work Loop는 뭐야?
A. 요구사항을 Entity, Repository, Service, DTO, SQL Review까지 순서대로 설계하고 검수하는 Agent 작업 흐름이다.

Q. JPA 기능은 어떤 순서로 검토해?
A. Entity Mapping, Relationship, Repository Query, Service Transaction, DTO 변환, Fetch Strategy, SQL Review 순서로 검토한다.

Q. Review FAIL이 나오면 어떻게 해?
A. 원인을 Entity, Repository, Service, DTO, Query, Transaction 중 하나로 분류하고 해당 Rule을 재적용한다.

Q. JPA Review는 SQL Review와 분리해도 돼?
A. 권장하지 않는다. JPA Query의 최종 결과는 SQL이므로 SQL 로그와 함께 검토해야 한다.

---

## 8.2 Part08 Final Goal

### [개념]

JPA Advanced Part08의 최종 목적은 Agent가 JPA 기반 Backend 기능을 전체 흐름으로 통합하고, Troubleshooting과 Anti Pattern 검수를 통해 안정적인 Persistence Layer를 완성하도록 만드는 것이다.

Part08은 SQL Foundation Part05 Backend Integration / Troubleshooting / Anti Pattern과 직접 연결되는 JPA 최종 검수 문서다.

---

### [핵심]

Agent가 수행해야 할 작업:

- Backend Layer 책임 분리
- Create / Read / Update / Delete Flow 설계
- Request DTO / Response DTO 분리
- Service Transaction 적용
- Repository Query 전략 선택
- Entity Mapping 검수
- Association Mapping 검수
- Dirty Checking Pattern 검수
- Fetch Strategy 검수
- Pagination 검수
- Cascade / orphanRemoval 삭제 영향 검수
- Auditing 적용 검수
- SQL Log Review 수행
- Constraint Violation Troubleshooting
- LazyInitializationException Troubleshooting
- N+1 Troubleshooting
- JPA Anti Pattern 탐지
- PM / Backend / Review Agent Work Loop 연결

---

### [실무]

Part08 통합 검수 Flow:

```text
Backend Feature 확인
→ CRUD Flow 확인
→ Layer Responsibility 확인
→ Entity / DTO 분리 확인
→ Transaction Boundary 확인
→ Repository Query 확인
→ Fetch Strategy 확인
→ Pagination 확인
→ Constraint / Data Integrity 확인
→ SQL Log Review
→ Troubleshooting 적용
→ Anti Pattern 제거
→ Final Output
```

Part08 이후 연결:

```text
JPA Advanced Completed
→ Security Advanced Rework
→ QueryDSL Practical 연계
→ Testing Domain Rules 연계
→ API Design Domain Rules 연계
→ Backend Agent Rule 활성화
```

---

### [FAQ]

Q. JPA Advanced Part08의 목적은 뭐야?
A. JPA 기반 Backend 기능을 전체 흐름으로 통합하고 Troubleshooting과 Anti Pattern 기준으로 최종 검수하는 것이다.

Q. Part08에서 가장 중요한 기준은 뭐야?
A. Layer 책임 분리, Service Transaction, DTO 분리, SQL Review, N+1 / Lazy / Constraint Troubleshooting, Anti Pattern 제거다.

Q. Part08은 SQL Foundation 어느 부분과 연결돼?
A. SQL Part05 Backend Integration / Troubleshooting / Anti Pattern과 직접 연결된다.

Q. Part08 이후에는 무엇을 하면 돼?
A. JPA Advanced를 완료 처리하고 Security Advanced Rework 또는 QueryDSL / Testing / API Design 연계 검토로 넘어간다.

---

# Retrieval Queries

### [FAQ]

Q. JPA Backend Integration은 뭐야?
A. Controller, DTO, Service, Repository, Entity, Transaction, Response 흐름을 JPA 기준으로 연결하는 설계다.

Q. JPA는 Entity만 잘 만들면 끝이야?
A. 아니다. Repository Query, Service Transaction, DTO 변환, SQL Review, Troubleshooting까지 함께 검토해야 한다.

Q. Controller에서 Entity를 직접 반환해도 돼?
A. 권장하지 않는다. Entity 직접 반환은 Lazy Loading, 순환 참조, 민감정보 노출, API 결합 문제를 만든다.

Q. JPA Backend Integration에서 가장 중요한 Layer는 어디야?
A. Service Layer다. Transaction Boundary와 Entity 상태 변경 흐름을 관리하기 때문이다.

Q. Controller는 JPA Entity를 직접 다뤄도 돼?
A. 권장하지 않는다. Controller는 DTO와 HTTP 흐름만 다루는 것이 안전하다.

Q. Repository에 비즈니스 로직을 넣어도 돼?
A. 권장하지 않는다. Repository는 Data Access Layer이고 비즈니스 흐름은 Service에서 처리한다.

Q. Entity에는 어떤 로직을 넣어도 돼?
A. Entity 상태 변경과 불변 조건에 가까운 Domain Method를 넣을 수 있다.

Q. DTO 변환은 어디서 해?
A. 프로젝트 규칙에 따라 Service 또는 DTO static factory에서 처리할 수 있지만 Lazy Loading과 Transaction 범위를 고려해야 한다.

Q. Create API에서 Entity를 RequestBody로 받아도 돼?
A. 권장하지 않는다. Request DTO로 입력을 받고 Service에서 Entity를 생성하는 것이 안전하다.

Q. 신규 Entity 저장은 save를 써도 돼?
A. 그렇다. 신규 Entity 저장에는 Repository save를 사용한다.

Q. 생성 시 기본값은 어디서 설정해?
A. Entity Field 초기값, Factory Method, Service 중 하나로 정하고 프로젝트 기준을 통일한다.

Q. Create Flow에서 Constraint는 어떻게 검토해?
A. DTO Validation, Service 중복 검증, DB Constraint를 함께 검토한다.

Q. Read Flow에서 readOnly Transaction은 왜 써?
A. 조회 전용 의도를 명확히 하고 Lazy Loading / DTO 변환 범위를 통제하기 위해 사용한다.

Q. 목록 조회에는 Entity 조회와 Projection 중 뭐가 좋아?
A. 읽기 전용 목록이고 필요한 Field가 명확하면 DTO Projection이 적합한 경우가 많다.

Q. 단건 조회에서는 Fetch Join을 써도 돼?
A. 필요한 연관 Entity가 명확하면 Fetch Join을 사용할 수 있다.

Q. Read Flow에서 가장 많이 생기는 문제는 뭐야?
A. DTO 변환 중 Lazy Loading으로 인한 N+1과 Entity 직접 반환 문제다.

Q. Update Flow에서 save를 다시 호출해야 해?
A. Managed Entity를 Transaction 안에서 변경했다면 Dirty Checking으로 반영될 수 있어 save가 필수는 아니다.

Q. 수정 API에서 Entity를 새로 만들어 save하면 안 돼?
A. 기존 값 덮어쓰기와 연관관계 손실 위험이 있으므로 Transaction 안에서 조회 후 변경하는 방식이 안전하다.

Q. Update Flow에서 가장 중요한 것은 뭐야?
A. Service Transaction 안에서 Managed Entity를 조회하고 Entity 상태 변경 Method를 호출하는 것이다.

Q. update 후 SQL이 안 나가면 뭘 확인해?
A. Transaction, readOnly 여부, Managed 상태, 변경 Method 호출 여부, Flush / Commit 시점을 확인한다.

Q. Delete Flow에서 가장 먼저 정할 것은 뭐야?
A. Hard Delete인지 Soft Delete인지 삭제 정책을 먼저 정해야 한다.

Q. Soft Delete는 JPA delete를 호출해?
A. 보통 delete Method로 상태 Field를 변경하고 Dirty Checking으로 UPDATE 처리한다.

Q. Hard Delete에서 무엇을 주의해야 해?
A. Foreign Key Constraint, Cascade REMOVE, orphanRemoval, 데이터 복구 불가 문제를 주의해야 한다.

Q. 삭제에서 가장 위험한 JPA 설정은 뭐야?
A. 공유 Entity에 Cascade REMOVE 또는 CascadeType.ALL을 적용하는 것이다.

Q. JPA Performance Review는 뭐야?
A. API가 실행하는 SQL, Query 수, Fetch Strategy, Pagination, Index 필요성을 검토하는 과정이다.

Q. JPA 성능 문제는 어디서 많이 생겨?
A. DTO 변환 중 Lazy Loading, N+1, Fetch Join 남용, Pagination Count Query, findAll 남용에서 자주 생긴다.

Q. 성능 검토에서 가장 먼저 볼 것은 뭐야?
A. SQL 로그와 Query 수를 먼저 확인한다.

Q. Query 수가 적으면 성능 문제가 없는 거야?
A. 아니다. Join으로 가져오는 Row 수가 많거나 Count Query가 비싸면 느릴 수 있다.

Q. SQL Log Review는 왜 필요해?
A. JPA가 실제 어떤 SQL을 실행하는지 확인해야 성능과 Mapping 문제를 판단할 수 있기 때문이다.

Q. SQL 로그에서 가장 먼저 볼 것은 뭐야?
A. Query 수, 반복 SELECT, Join, Count Query, UPDATE / DELETE 발생 여부를 확인한다.

Q. JPA 코드만 보고 성능을 판단해도 돼?
A. 권장하지 않는다. 반드시 생성 SQL과 Query 수를 확인해야 한다.

Q. Entity Mapping Error가 나면 무엇부터 확인해?
A. `@Entity`, `@Id`, 기본 생성자, Table / Column 이름, Association Mapping을 먼저 확인한다.

Q. mappedBy 오류는 왜 자주 생겨?
A. `mappedBy`에 DB Column 이름을 쓰는 실수가 많기 때문이다. 상대 Entity Field 이름을 써야 한다.

Q. JPQL 오류에서 가장 흔한 원인은 뭐야?
A. Entity / Field 이름 대신 Table / Column 이름을 사용하는 것이다.

Q. Native Query 오류에서 가장 흔한 원인은 뭐야?
A. 실제 DB Table / Column 이름과 Query 이름이 일치하지 않는 것이다.

Q. Dirty Checking이 안 되면 무엇부터 확인해?
A. Service Method의 `@Transactional`, readOnly 여부, Entity Managed 상태, UPDATE SQL 로그를 확인한다.

Q. update 후 save를 안 해서 반영이 안 된 거야?
A. Managed Entity라면 save가 필수는 아니다. Transaction과 Entity 상태를 먼저 확인해야 한다.

Q. readOnly Transaction에서 수정하면 어떻게 돼?
A. 변경 반영을 기대하지 않아야 하며 수정 Method는 일반 Transaction을 사용해야 한다.

Q. Detached Entity를 수정하면 Dirty Checking이 돼?
A. 아니다. Detached Entity는 Persistence Context가 관리하지 않으므로 Dirty Checking 대상이 아니다.

Q. LazyInitializationException이 나면 뭘 먼저 확인해?
A. Lazy Field 접근 위치와 Transaction이 종료되었는지 먼저 확인한다.

Q. LazyInitializationException은 EAGER로 바꾸면 해결돼?
A. 권장하지 않는다. Fetch Join, DTO Projection, Service Transaction 안 DTO 변환을 우선 적용한다.

Q. Entity 직접 반환을 없애면 도움이 돼?
A. 그렇다. JSON 직렬화 중 Lazy Field 접근을 막고 API 구조를 안정화할 수 있다.

Q. Fetch Join을 했는데도 예외가 나면?
A. DTO 변환에서 접근하는 모든 Lazy Association이 조회되었는지 확인해야 한다.

Q. N+1 문제는 어떻게 찾는 게 좋아?
A. SQL 로그에서 API 하나가 실행하는 Query 수와 반복 SELECT 대상 Table을 확인한다.

Q. DTO from Method가 N+1 원인이 될 수 있어?
A. 그렇다. Lazy Association getter를 호출하면 목록 변환 중 반복 Query가 발생할 수 있다.

Q. N+1은 Fetch Join으로만 해결해?
A. 아니다. Fetch Join, DTO Projection, Batch Size, 별도 Query, API 구조 변경 중 선택한다.

Q. OneToMany N+1은 어떻게 해결해?
A. Collection Fetch Join보다 Child Repository 별도 Pagination, Batch Size, API 구조 변경을 우선 검토한다.

Q. Constraint Violation이 나면 뭘 먼저 확인해?
A. 예외 메시지의 Constraint 이름, Entity Mapping, DTO Validation, DB Schema를 확인한다.

Q. Unique 중복은 existsBy로 충분해?
A. 아니다. 동시성 상황에서는 DB Unique Constraint가 최종 방어선이다.

Q. Foreign Key 위반은 왜 발생해?
A. 존재하지 않는 Parent를 참조하거나 삭제 순서 / Cascade 설정이 잘못되었을 때 발생할 수 있다.

Q. Constraint 예외는 어디서 응답으로 바꿔?
A. GlobalExceptionHandler에서 Custom Error Response로 변환한다.

Q. Data Integrity Review는 뭐야?
A. Entity Mapping, Validation, DB Constraint, Transaction이 데이터 일관성을 보장하는지 검토하는 과정이다.

Q. Application Validation만으로 충분해?
A. 아니다. DB Constraint가 최종 방어선으로 필요하다.

Q. Foreign Key Data Integrity는 어떻게 보장해?
A. Service에서 Parent Entity를 조회하고 Association을 설정하며 DB FK Constraint를 함께 확인한다.

Q. Soft Delete는 Data Integrity에 어떤 영향을 줘?
A. 조회 조건 누락, Unique Constraint 충돌, 복구 정책 문제를 만들 수 있다.

Q. Entity Anti Pattern에서 가장 위험한 것은 뭐야?
A. Entity를 RequestBody로 받고 Response로 직접 반환하는 것이다.

Q. Entity에 `@Data`를 쓰면 왜 위험해?
A. Setter, equals, hashCode, toString이 무분별하게 생성되어 JPA 상태 관리와 Lazy Loading 문제를 만들 수 있다.

Q. Entity에 화면 전용 Field를 넣어도 돼?
A. 권장하지 않는다. 화면 전용 값은 Response DTO나 Projection DTO에서 처리한다.

Q. Entity 직접 반환은 왜 보안 문제야?
A. password, role, internal status 같은 민감 Field가 노출될 수 있기 때문이다.

Q. Repository Anti Pattern에서 가장 흔한 것은 뭐야?
A. findAll 후 Java Stream으로 필터링하는 것이다.

Q. Filtering은 Java Stream으로 하면 안 돼?
A. 대량 데이터에서는 DB WHERE 조건으로 처리해야 성능과 Pagination이 안정적이다.

Q. Repository에 비즈니스 로직을 넣으면 왜 안 좋아?
A. Data Access와 Business Flow가 섞여 Transaction과 테스트 책임이 불명확해진다.

Q. Query Method가 길어지면 어떻게 해?
A. JPQL 또는 QueryDSL로 분리한다. 동적 조건이 많으면 QueryDSL이 적합하다.

Q. Service Transaction Anti Pattern에서 가장 흔한 것은 뭐야?
A. 수정 Method에 Transaction이 없거나 readOnly Transaction에서 수정하는 것이다.

Q. 예외를 catch하면 왜 Transaction 문제가 생겨?
A. 예외를 삼키면 Transaction이 정상 종료되어 Commit될 수 있기 때문이다.

Q. Detached Entity save는 왜 위험해?
A. null 덮어쓰기, 연관관계 손실, 변경 의도 불명확 문제가 생길 수 있다.

Q. Self Invocation은 왜 문제야?
A. 같은 Class 내부 호출은 Spring Proxy를 거치지 않아 `@Transactional`이 적용되지 않을 수 있다.

Q. Fetch and Pagination Anti Pattern에서 가장 흔한 것은 뭐야?
A. Page.map이나 DTO from Method에서 Lazy Association을 접근해 N+1을 만드는 것이다.

Q. Collection Fetch Join과 Pageable은 왜 위험해?
A. Child Row 때문에 Parent Row가 중복되어 Pagination이 불안정해질 수 있다.

Q. 목록 조회는 Fetch Join과 Projection 중 뭐가 좋아?
A. 읽기 전용 목록이고 필요한 Field가 명확하면 Projection이 적합한 경우가 많다.

Q. EAGER로 바꾸면 Fetch 문제가 해결돼?
A. 권장하지 않는다. 불필요한 조회와 N+1 문제가 숨겨지거나 확대될 수 있다.

Q. JPA Review에서 가장 먼저 볼 것은 뭐야?
A. Controller Entity 노출 여부, Service Transaction, Entity Mapping, Repository Query를 먼저 본다.

Q. Review Agent가 FAIL로 봐야 하는 항목은 뭐야?
A. Entity 직접 노출, Transaction 없는 수정, Cascade REMOVE 남용, N+1 대량 문제, Constraint 누락 같은 치명적 문제다.

Q. JPA Review에 SQL 로그가 필요한 이유는 뭐야?
A. 실제 Query 수, N+1, Join, Pagination Count Query는 SQL 로그로 확인해야 하기 때문이다.

Q. DTO 변환 로직도 Review 대상이야?
A. 그렇다. DTO 변환 중 Lazy Association 접근으로 N+1이나 LazyInitializationException이 생길 수 있다.

Q. PM Agent는 JPA 구현 전에 무엇을 정해야 해?
A. Entity, Relationship, Query 조건, Pagination, Transaction, Constraint, 삭제 정책을 정해야 한다.

Q. 목록 조회 요구사항에서 꼭 확인할 것은 뭐야?
A. Pagination 방식, 정렬 기준, 필요한 응답 Field, N+1 위험을 확인해야 한다.

Q. 삭제 기능 요구사항에서 꼭 확인할 것은 뭐야?
A. Hard Delete인지 Soft Delete인지, Cascade / orphanRemoval 영향이 있는지 확인해야 한다.

Q. 중복 방지 요구사항은 어떻게 전달해야 해?
A. Service existsBy 검증과 DB Unique Constraint가 모두 필요하다고 전달해야 한다.

Q. JPA Agent Work Loop는 뭐야?
A. 요구사항을 Entity, Repository, Service, DTO, SQL Review까지 순서대로 설계하고 검수하는 Agent 작업 흐름이다.

Q. JPA 기능은 어떤 순서로 검토해?
A. Entity Mapping, Relationship, Repository Query, Service Transaction, DTO 변환, Fetch Strategy, SQL Review 순서로 검토한다.

Q. Review FAIL이 나오면 어떻게 해?
A. 원인을 Entity, Repository, Service, DTO, Query, Transaction 중 하나로 분류하고 해당 Rule을 재적용한다.

Q. JPA Review는 SQL Review와 분리해도 돼?
A. 권장하지 않는다. JPA Query의 최종 결과는 SQL이므로 SQL 로그와 함께 검토해야 한다.

Q. JPA Advanced Part08의 목적은 뭐야?
A. JPA 기반 Backend 기능을 전체 흐름으로 통합하고 Troubleshooting과 Anti Pattern 기준으로 최종 검수하는 것이다.

Q. Part08에서 가장 중요한 기준은 뭐야?
A. Layer 책임 분리, Service Transaction, DTO 분리, SQL Review, N+1 / Lazy / Constraint Troubleshooting, Anti Pattern 제거다.

Q. Part08은 SQL Foundation 어느 부분과 연결돼?
A. SQL Part05 Backend Integration / Troubleshooting / Anti Pattern과 직접 연결된다.

Q. Part08 이후에는 무엇을 하면 돼?
A. JPA Advanced를 완료 처리하고 Security Advanced Rework 또는 QueryDSL / Testing / API Design 연계 검토로 넘어간다.
