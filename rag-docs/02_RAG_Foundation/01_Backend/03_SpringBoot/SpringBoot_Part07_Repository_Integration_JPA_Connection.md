# Spring Boot Part07 - Repository Integration & JPA 연결 기준

---

# 1. Repository Integration

## 1.1 Repository Integration 개념

### [개념]

Repository Integration은 Spring Boot Service Layer가 Repository Layer를 통해 Database와 연결되는 구조다.

Spring Boot에서 Repository는 데이터 접근 계층이며, JPA를 사용하는 경우 보통 Spring Data JPA Repository Interface를 통해 Entity CRUD와 Query Method를 처리한다.

기본 흐름:

```text
Controller
→ Service
→ Repository
→ JPA
→ Database
```

Repository Integration의 목적:

- Service에서 DB 접근 로직 분리
- Entity 중심 데이터 조회 / 저장
- Query Method 기반 조회
- Optional 기반 단건 조회 실패 표현
- Pagination / Slice 조회 연결
- Transaction Boundary와 JPA 영속성 연결
- Controller가 DB 접근을 직접 하지 않도록 구조화

---

### [핵심]

Repository 책임:

- Entity 저장
- Entity 조회
- Entity 삭제
- Query Method 제공
- 존재 여부 확인
- Pagination 조회
- JPQL / Native Query 연결
- Custom Repository 연결

Repository가 담당하지 않는 것:

- Business Logic 판단
- HTTP Request / Response 처리
- DTO 응답 생성 책임
- Transaction 전체 Use Case 흐름
- 권한 검사
- 상태 전환 규칙
- 외부 API 호출

---

### [실무]

Repository 기본 예:

```java
public interface PostRepository extends JpaRepository<Post, Long> {

    Optional<Post> findByIdAndDeletedFalse(Long postId);

    boolean existsByTitle(String title);

    Slice<Post> findByDeletedFalseOrderByCreatedAtDesc(Pageable pageable);
}
```

Service 사용 예:

```java
@Service
@RequiredArgsConstructor
public class PostService {

    private final PostRepository postRepository;

    @Transactional(readOnly = true)
    public PostResponse getPost(Long postId) {
        Post post = postRepository.findByIdAndDeletedFalse(postId)
                .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

        return PostResponse.from(post);
    }
}
```

권장:

- Repository는 Entity 중심으로 작성
- Service에서 Repository를 호출
- Controller에서 Repository 직접 호출 지양
- Optional은 Service에서 처리
- Entity 조회 실패는 CustomException으로 변환
- 조회 결과는 Response DTO로 변환
- 복잡한 조회는 JPA Advanced / QueryDSL 기준으로 분리

---

### [FAQ]

Q. Repository Integration은 뭐야?

A.
Service Layer가 Repository를 통해 Entity를 조회, 저장, 삭제하고 Database와 연결되는 구조다.

Q. Repository는 왜 필요한가?

A.
DB 접근 책임을 Service와 분리하고 Entity 중심으로 데이터 접근을 추상화하기 위해 필요하다.

Q. Controller에서 Repository를 바로 호출해도 돼?

A.
실무 구조에서는 권장하지 않는다. Service를 통해 Business Logic과 Transaction Boundary를 관리하는 것이 좋다.

---

# 2. Spring Data JPA Repository

## 2.1 JpaRepository 기본 구조

### [개념]

`JpaRepository`는 Spring Data JPA가 제공하는 Repository Interface다.

Entity 타입과 Entity ID 타입을 지정하면 기본 CRUD method를 사용할 수 있다.

기본 형식:

```java
public interface EntityRepository extends JpaRepository<Entity, IdType> {
}
```

---

### [핵심]

JpaRepository 제공 기능:

- save
- findById
- findAll
- delete
- deleteById
- existsById
- count
- flush
- pagination
- sorting

기본 선언:

```java
public interface UserRepository extends JpaRepository<User, Long> {
}
```

의미:

```text
User Entity를 Long ID 기준으로 관리하는 Repository
```

---

### [실무]

Entity 예:

```java
@Entity
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long userId;

    private String email;
    private String nickname;
}
```

Repository 예:

```java
public interface UserRepository extends JpaRepository<User, Long> {

    Optional<User> findByEmail(String email);

    boolean existsByEmail(String email);
}
```

Service 예:

```java
@Transactional(readOnly = true)
public UserResponse getUser(Long userId) {
    User user = userRepository.findById(userId)
            .orElseThrow(() -> new BusinessException("USER_NOT_FOUND", "사용자를 찾을 수 없습니다."));

    return UserResponse.from(user);
}
```

권장:

- Entity별 Repository Interface 작성
- ID 타입은 Entity의 `@Id` 타입과 일치
- 단건 조회는 Optional 사용
- 존재 여부만 필요하면 existsBy 사용
- Entity를 직접 Controller로 반환하지 않음

---

### [주의]

Repository 작성 시 주의:

- Entity 이름과 Repository 이름 일관성 유지
- ID 타입 불일치 주의
- Repository에 `@Repository` 생략 가능
- Repository Interface는 Spring Component Scan 범위 안에 위치
- Repository에서 Business Logic 작성 금지
- `findById().get()` 사용 지양

---

### [FAQ]

Q. JpaRepository는 뭐야?

A.
Spring Data JPA가 제공하는 기본 Repository Interface이며 CRUD, pagination, sorting 기능을 제공한다.

Q. Repository에 @Repository를 붙여야 해?

A.
Spring Data JPA Repository Interface는 보통 `JpaRepository`를 상속하면 자동으로 Bean 등록되므로 별도 `@Repository`를 붙이지 않아도 된다.

Q. ID 타입은 어떻게 정해?

A.
Entity의 `@Id` 필드 타입과 Repository의 두 번째 Generic 타입을 일치시킨다.

---

## 2.2 Repository Bean 등록 기준

### [개념]

Spring Data JPA Repository는 Interface만 작성해도 Spring이 구현체를 생성하고 Bean으로 등록한다.

Repository는 Component Scan과 JPA Repository Scan 범위 안에 있어야 정상 등록된다.

---

### [핵심]

Repository Bean 등록 조건:

- `JpaRepository` 상속
- Entity 타입 지정
- ID 타입 지정
- Main Application Class 하위 패키지에 위치
- Spring Data JPA 의존성 존재
- Entity가 JPA Entity로 인식됨
- Repository Scan 범위 안에 있음

---

### [실무]

권장 패키지 구조:

```text
src/main/java/com/example/project
├ ProjectApplication.java
├ entity
│ └ User.java
├ repository
│ └ UserRepository.java
├ service
│ └ UserService.java
└ controller
  └ UserController.java
```

Main Class 위치:

```java
@SpringBootApplication
public class ProjectApplication {

    public static void main(String[] args) {
        SpringApplication.run(ProjectApplication.class, args);
    }
}
```

`ProjectApplication`이 상위 패키지에 있으면 하위 패키지의 Repository, Service, Controller, Entity를 탐색하기 쉽다.

---

### [Troubleshooting]

문제: Repository Bean을 찾을 수 없음

```text
원인 후보:
- Repository가 Main Class 하위 패키지 밖에 있음
- JpaRepository를 상속하지 않음
- Spring Data JPA 의존성 없음
- Entity 인식 실패
- Component Scan / Repository Scan 범위 문제
```

확인 순서:

```text
Repository 위치 확인
→ Main Class 위치 확인
→ JpaRepository 상속 확인
→ Entity @Entity 확인
→ ID 타입 확인
→ build.gradle 의존성 확인
```

---

### [FAQ]

Q. Repository Bean 등록이 안 되면 뭘 확인해?

A.
Repository 위치, Main Class 위치, JpaRepository 상속 여부, Entity @Entity 여부, Spring Data JPA 의존성을 확인한다.

Q. Repository 구현체는 직접 만들어야 해?

A.
기본 CRUD와 Query Method는 Spring Data JPA가 구현체를 자동 생성한다. 복잡한 동적 쿼리는 Custom Repository나 QueryDSL을 검토한다.

---

# 3. Query Method

## 3.1 Query Method 개념

### [개념]

Query Method는 Repository method 이름을 기반으로 Spring Data JPA가 Query를 생성하는 기능이다.

예:

```java
Optional<User> findByEmail(String email);
```

의미:

```text
email 값으로 User Entity를 조회
```

---

### [핵심]

자주 쓰는 Query Method Prefix:

- findBy
- findAllBy
- existsBy
- countBy
- deleteBy
- findTopBy
- findFirstBy

자주 쓰는 조건:

- And
- Or
- IsNull
- IsNotNull
- Containing
- Like
- Between
- GreaterThan
- LessThan
- OrderBy
- True
- False

---

### [실무]

단건 조회:

```java
Optional<User> findByEmail(String email);
```

목록 조회:

```java
List<Post> findAllByDeletedFalseOrderByCreatedAtDesc();
```

존재 여부 확인:

```java
boolean existsByEmail(String email);
```

삭제되지 않은 데이터 조회:

```java
Optional<Post> findByPostIdAndDeletedFalse(Long postId);
```

최신 데이터 조회:

```java
Optional<Comment> findTopByPostOrderByCreatedAtDesc(Post post);
```

권장:

- 단건 조회는 Optional 사용
- 존재 여부는 existsBy 사용
- boolean 필드는 True / False 조건 사용 가능
- 정렬은 OrderBy 사용 가능
- Query Method 이름이 길어지면 JPQL, QueryDSL, Custom Repository 검토

---

### [FAQ]

Q. Query Method는 뭐야?

A.
Repository method 이름으로 조회 조건을 표현하면 Spring Data JPA가 Query를 생성하는 기능이다.

Q. existsBy는 언제 써?

A.
중복 이메일, 이미 좋아요 여부, 이미 찜 여부처럼 존재 여부만 필요한 경우 사용한다.

Q. Query Method 이름이 너무 길면 어떻게 해?

A.
JPQL, QueryDSL, Custom Repository 분리를 검토하는 것이 좋다.

---

## 3.2 Query Method Naming 기준

### [개념]

Query Method Naming은 Repository method 이름으로 조회 조건을 명확히 표현하는 규칙이다.

이름이 지나치게 길어지면 Repository의 가독성과 유지보수성이 떨어진다.

---

### [핵심]

좋은 Query Method 조건:

- 조회 목적이 명확함
- 조건 개수가 적절함
- Entity 필드명과 일치함
- 반환 타입이 명확함
- Service에서 의미 있게 사용 가능함

나쁜 Query Method 신호:

- 이름이 지나치게 김
- 조건이 4개 이상 계속 연결됨
- 동적 조건이 많음
- 정렬 조건이 복잡함
- 여러 Entity 관계를 깊게 탐색함
- Method 이름만 보고 의도 파악이 어려움

---

### [실무]

괜찮은 예:

```java
Optional<Post> findByPostIdAndDeletedFalse(Long postId);

List<Post> findAllByCategoryAndDeletedFalse(PostCategory category);

Slice<Post> findAllByDeletedFalseOrderByCreatedAtDesc(Pageable pageable);
```

부담스러운 예:

```java
List<Post> findAllByCategoryAndDeletedFalseAndTitleContainingAndCreatedAtBetweenAndWriterNicknameOrderByCreatedAtDesc(
        PostCategory category,
        String title,
        LocalDateTime startDate,
        LocalDateTime endDate,
        String nickname
);
```

개선 방향:

```text
복잡한 검색 조건
→ SearchCondition DTO
→ QueryDSL 또는 Custom Repository
```

---

### [주의]

Query Method 주의:

- Entity 필드명이 바뀌면 Query Method도 깨질 수 있음
- 연관 필드 탐색은 과도하게 깊어지지 않게 주의
- 동적 검색 조건은 Query Method보다 QueryDSL이 적합할 수 있음
- 이름이 길어질수록 테스트와 검수가 중요
- Business Logic을 Query Method 이름에 억지로 담지 않음

---

### [FAQ]

Q. Query Method 조건은 몇 개까지가 적당해?

A.
정답은 없지만 이름이 길어져 읽기 어렵다면 JPQL, QueryDSL, Custom Repository를 검토하는 것이 좋다.

Q. 검색 필터가 여러 개면 Query Method로 다 만들면 돼?

A.
필터 조합이 많으면 Query Method가 폭발하므로 SearchCondition과 QueryDSL 같은 동적 쿼리 방식을 검토한다.

---

# 4. Optional 처리 기준

## 4.1 Optional Repository Result

### [개념]

Optional은 단건 조회 결과가 없을 수 있음을 표현하는 Java 타입이다.

Repository 단건 조회는 `Optional<Entity>`를 반환하고, Service에서 없을 때 CustomException으로 변환하는 구조가 좋다.

---

### [핵심]

권장 흐름:

```text
Repository
→ Optional<Entity>
→ Service
→ orElseThrow
→ CustomException
→ GlobalExceptionHandler
→ Error Response
```

Optional 사용 대상:

- findById
- findByEmail
- findByIdAndDeletedFalse
- findTopBy...
- 단건 조회 Query Method

---

### [실무]

Repository:

```java
public interface UserRepository extends JpaRepository<User, Long> {

    Optional<User> findByEmail(String email);
}
```

Service:

```java
@Transactional(readOnly = true)
public UserResponse getUserByEmail(String email) {
    User user = userRepository.findByEmail(email)
            .orElseThrow(() -> new BusinessException("USER_NOT_FOUND", "사용자를 찾을 수 없습니다."));

    return UserResponse.from(user);
}
```

권장:

- Optional은 Service에서 해소
- Controller로 Optional 반환 지양
- Optional.get 직접 사용 지양
- 없을 때 ErrorCode 명확화
- null 반환 지양

---

### [주의]

나쁜 예:

```java
public UserResponse getUser(Long userId) {
    User user = userRepository.findById(userId).get();

    return UserResponse.from(user);
}
```

문제:

- 값이 없을 때 NoSuchElementException 발생
- ErrorCode 불명확
- 사용자 응답 통제 어려움
- GlobalExceptionHandler에서 비즈니스 예외로 처리하기 어려움

좋은 예:

```java
public UserResponse getUser(Long userId) {
    User user = userRepository.findById(userId)
            .orElseThrow(() -> new BusinessException("USER_NOT_FOUND", "사용자를 찾을 수 없습니다."));

    return UserResponse.from(user);
}
```

---

### [FAQ]

Q. Repository Optional은 어디서 처리해?

A.
Service에서 처리하는 것이 좋다. 없을 경우 CustomException으로 변환해 GlobalExceptionHandler에서 공통 응답으로 처리한다.

Q. Optional.get은 왜 피해야 해?

A.
값이 없을 때 예외가 불명확하고 ErrorCode를 통제하기 어렵기 때문이다.

Q. Optional을 Controller까지 넘겨도 돼?

A.
권장하지 않는다. Controller는 성공 응답과 Service 호출에 집중하고 조회 실패 처리는 Service와 Exception Handler에서 처리하는 것이 좋다.

---

# 5. existsBy와 countBy

## 5.1 existsBy 사용 기준

### [개념]

`existsBy`는 특정 조건을 만족하는 데이터가 존재하는지만 확인하는 Repository Query Method다.

조회한 Entity 내용이 필요 없고 존재 여부만 필요할 때 사용한다.

---

### [핵심]

existsBy 사용 상황:

- 이메일 중복 검사
- 닉네임 중복 검사
- 이미 좋아요 여부 확인
- 이미 찜한 여부 확인
- 권한 관계 존재 여부 확인
- 특정 데이터 등록 여부 확인

반환 타입:

```java
boolean
```

---

### [실무]

Repository:

```java
public interface UserRepository extends JpaRepository<User, Long> {

    boolean existsByEmail(String email);

    boolean existsByNickname(String nickname);
}
```

Service:

```java
@Transactional
public UserResponse signUp(SignUpRequest request) {
    if (userRepository.existsByEmail(request.email())) {
        throw new BusinessException("DUPLICATED_EMAIL", "이미 사용 중인 이메일입니다.");
    }

    if (userRepository.existsByNickname(request.nickname())) {
        throw new BusinessException("DUPLICATED_NICKNAME", "이미 사용 중인 닉네임입니다.");
    }

    User user = User.create(request.email(), request.password(), request.nickname());

    return UserResponse.from(userRepository.save(user));
}
```

좋은 점:

- Entity 전체 조회 불필요
- 의도가 명확함
- Business Validation에 적합
- 중복 검사 코드가 간결함

---

### [주의]

existsBy 주의:

- 존재 확인 후 저장 사이에 동시성 문제가 생길 수 있음
- 중요한 중복 방지는 DB Unique Constraint도 함께 적용
- existsBy만으로 동시 요청 완전 방어 불가
- 권한 체크가 복잡하면 단순 existsBy보다 명확한 조회가 필요할 수 있음

---

### [FAQ]

Q. 중복 이메일 검사는 existsBy로 하면 돼?

A.
Service에서 existsByEmail로 검사할 수 있다. 다만 동시성까지 고려하면 DB Unique Constraint도 함께 적용하는 것이 좋다.

Q. existsBy와 findBy 중 뭐가 좋아?

A.
Entity 내용이 필요 없고 존재 여부만 필요하면 existsBy가 적합하다. Entity 값이 필요하면 findBy를 사용한다.

---

## 5.2 countBy 사용 기준

### [개념]

`countBy`는 특정 조건을 만족하는 데이터 개수를 조회하는 Repository Query Method다.

목록 전체를 가져오지 않고 개수만 필요할 때 사용한다.

---

### [핵심]

countBy 사용 상황:

- 게시글 수 조회
- 댓글 수 조회
- 좋아요 수 조회
- 사용자별 알림 개수 조회
- 읽지 않은 알림 개수 조회
- 특정 상태 데이터 개수 조회

반환 타입:

```java
long
```

또는

```java
int
```

---

### [실무]

Repository:

```java
public interface NotificationRepository extends JpaRepository<Notification, Long> {

    long countByUserIdAndReadStatusFalse(Long userId);
}
```

Service:

```java
@Transactional(readOnly = true)
public UnreadNotificationCountResponse getUnreadCount(Long userId) {
    long count = notificationRepository.countByUserIdAndReadStatusFalse(userId);

    return new UnreadNotificationCountResponse(count);
}
```

권장:

- 개수만 필요하면 countBy 사용
- 목록 조회 후 size 계산 지양
- 대용량 count query 비용 주의
- 자주 조회되는 count는 캐시나 별도 컬럼 전략 검토 가능

---

### [주의]

나쁜 예:

```java
public int getUnreadCount(Long userId) {
    List<Notification> notifications = notificationRepository.findAllByUserIdAndReadStatusFalse(userId);
    return notifications.size();
}
```

문제:

- 개수만 필요한데 전체 목록 조회
- 메모리 낭비
- DB / Application 부하 증가
- 대용량 데이터에서 비효율

좋은 예:

```java
public long getUnreadCount(Long userId) {
    return notificationRepository.countByUserIdAndReadStatusFalse(userId);
}
```

---

### [FAQ]

Q. 개수만 필요할 때 findAll 후 size를 써도 돼?

A.
데이터가 적으면 가능하지만 권장하지 않는다. 개수만 필요하면 countBy를 사용하는 것이 좋다.

Q. countBy는 항상 빠른가?

A.
항상 빠른 것은 아니다. 조건과 데이터 양에 따라 count query 비용이 클 수 있으므로 인덱스와 조회 패턴을 함께 고려해야 한다.

---

# 6. Pagination Repository

## 6.1 Page와 Slice Repository

### [개념]

Pagination Repository는 목록 데이터를 일정 단위로 나누어 조회하는 Repository 구조다.

Spring Data JPA에서는 `Pageable`, `Page`, `Slice`를 사용할 수 있다.

---

### [핵심]

주요 타입:

- Pageable
- Page
- Slice
- Sort

비교:

| 타입  | 특징                  | 사용 상황            |
| ----- | --------------------- | -------------------- |
| Page  | 전체 개수 포함        | 페이지 번호 UI       |
| Slice | 다음 페이지 여부 중심 | 무한 스크롤 / 더보기 |
| List  | 전체 목록             | 소량 데이터          |

---

### [실무]

Repository:

```java
public interface PostRepository extends JpaRepository<Post, Long> {

    Page<Post> findAllByDeletedFalse(Pageable pageable);

    Slice<Post> findAllByCategoryAndDeletedFalse(PostCategory category, Pageable pageable);
}
```

Service:

```java
@Transactional(readOnly = true)
public Slice<PostResponse> getPosts(PostCategory category, Pageable pageable) {
    return postRepository.findAllByCategoryAndDeletedFalse(category, pageable)
            .map(PostResponse::from);
}
```

Controller:

```java
@GetMapping
public ApiResponse<Slice<PostResponse>> getPosts(
        @RequestParam PostCategory category,
        Pageable pageable
) {
    return ApiResponse.success(postService.getPosts(category, pageable));
}
```

권장:

- 페이지 번호 UI는 Page
- 무한 스크롤은 Slice
- 대용량에서 Page count query 비용 주의
- Pageable 기본 size 제한 고려
- 정렬 기준 명확화
- Response DTO로 변환 후 반환

---

### [FAQ]

Q. Page와 Slice 차이는?

A.
Page는 전체 개수를 포함하고 Slice는 다음 페이지 존재 여부 중심이다. 무한 스크롤이나 더보기는 Slice가 적합할 수 있다.

Q. Pageable은 Repository에서만 써?

A.
Controller에서 Pageable을 받고 Service를 거쳐 Repository에 전달하는 구조가 일반적이다.

Q. Page나 Slice 안의 Entity를 DTO로 바꾸려면?

A.
`map(PostResponse::from)`처럼 map을 사용해 Entity를 Response DTO로 변환할 수 있다.

---

## 6.2 Pagination 주의사항

### [개념]

Pagination 주의사항은 목록 조회에서 성능, 정렬, 응답 형식, Frontend 연동 문제를 방지하기 위한 기준이다.

---

### [핵심]

주의할 점:

- 대용량 Page count query 비용
- 정렬 기준 누락
- 기본 size 과다
- 최대 size 제한 없음
- Entity 직접 반환
- N+1 문제
- 불안정한 정렬
- Frontend page index 기준 혼동
- Page와 Slice 선택 기준 없음

---

### [실무]

기본 정렬 적용 예:

```java
@GetMapping
public ApiResponse<Slice<PostResponse>> getPosts(
        @PageableDefault(size = 20, sort = "createdAt", direction = Sort.Direction.DESC)
        Pageable pageable
) {
    return ApiResponse.success(postService.getPosts(pageable));
}
```

Service:

```java
@Transactional(readOnly = true)
public Slice<PostResponse> getPosts(Pageable pageable) {
    return postRepository.findAllByDeletedFalse(pageable)
            .map(PostResponse::from);
}
```

권장:

- `@PageableDefault`로 기본 size / sort 설정
- 최대 size 제한 정책 검토
- 정렬 기준은 createdAt, id 등 안정적 기준 사용
- 무한 스크롤은 Slice 우선 검토
- 목록 응답도 Response DTO로 변환
- 복잡한 목록 조회는 QueryDSL / Projection 검토

---

### [Troubleshooting]

문제: 목록 순서가 요청마다 바뀜

```text
원인:
정렬 기준 없음
동일 createdAt 값에 대한 보조 정렬 없음

해결:
createdAt DESC, id DESC처럼 안정적인 정렬 기준 적용
```

문제: 무한 스크롤인데 count query가 부담됨

```text
원인:
Page 사용으로 total count 조회 발생

해결:
Slice 사용 검토
```

문제: page 번호가 이상함

```text
원인:
Spring Pageable은 기본 page index가 0부터 시작
Frontend는 1부터 시작한다고 가정

해결:
Frontend / Backend page index 기준 통일
```

---

### [FAQ]

Q. Pageable page는 0부터 시작해?

A.
Spring Pageable은 기본적으로 page index가 0부터 시작한다. Frontend와 기준을 맞춰야 한다.

Q. 무한 스크롤은 Page와 Slice 중 뭐가 좋아?

A.
전체 개수보다 다음 페이지 존재 여부가 중요하므로 Slice가 적합할 수 있다.

Q. 목록 조회에 정렬 기준이 꼭 필요해?

A.
권장된다. 정렬 기준이 없으면 응답 순서가 불안정해질 수 있다.

---

# 7. Repository와 Entity 연결

## 7.1 Entity 중심 Repository

### [개념]

Repository는 Entity 중심으로 작성한다.

Repository의 주된 반환 타입은 Entity, Optional Entity, Entity List, Page Entity, Slice Entity다.

---

### [핵심]

Repository 반환 타입:

- Entity
- Optional<Entity>
- List<Entity>
- Page<Entity>
- Slice<Entity>
- boolean
- long

주의할 반환 타입:

- Response DTO
- ApiResponse
- Controller 전용 객체
- Request DTO

---

### [실무]

권장 Repository:

```java
public interface PostRepository extends JpaRepository<Post, Long> {

    Optional<Post> findByPostIdAndDeletedFalse(Long postId);

    List<Post> findAllByWriter(User writer);

    Slice<Post> findAllByDeletedFalse(Pageable pageable);
}
```

Service에서 DTO 변환:

```java
@Transactional(readOnly = true)
public Slice<PostResponse> getPosts(Pageable pageable) {
    return postRepository.findAllByDeletedFalse(pageable)
            .map(PostResponse::from);
}
```

권장:

- Repository는 Entity 조회에 집중
- DTO 변환은 Service 또는 Mapper에서 처리
- API 응답 구조를 Repository에 넣지 않음
- Entity 관계 기준으로 Query Method 작성
- 복잡한 Projection은 JPA / QueryDSL 문서 기준으로 분리

---

### [주의]

비권장 Repository:

```java
public interface PostRepository extends JpaRepository<Post, Long> {

    ApiResponse<PostResponse> findPostResponseByPostId(Long postId);
}
```

문제:

- Repository가 API 응답 형식을 알게 됨
- Persistence Layer와 Web/API Layer 결합
- 테스트와 재사용성 저하
- Layer 책임 위반

---

### [FAQ]

Q. Repository에서 Response DTO를 바로 반환해도 돼?

A.
단순 Projection은 가능하지만 API 응답 형식인 ApiResponse나 Controller 전용 DTO를 Repository에 결합하는 것은 지양한다.

Q. Repository는 Entity 중심이어야 해?

A.
기초 구조에서는 Entity 중심이 좋다. 복잡한 조회 최적화가 필요할 때 Projection이나 QueryDSL을 검토한다.

---

## 7.2 Entity ID와 Repository Method

### [개념]

Repository Method는 Entity의 식별자와 필드명을 기준으로 작성한다.

Entity ID 필드명과 Repository Query Method 이름이 일관되어야 한다.

---

### [핵심]

ID 기준 예:

```java
@Entity
public class Post {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long postId;
}
```

Repository:

```java
Optional<Post> findByPostId(Long postId);
```

`JpaRepository<Post, Long>` 기본 method:

```java
Optional<Post> findById(Long id);
```

주의:

- `findById`는 Entity의 `@Id`를 기준으로 조회
- `findByPostId`는 필드명 `postId`를 기준으로 Query Method 생성
- 둘 다 가능하지만 팀 naming 기준 통일 필요

---

### [실무]

기본 조회:

```java
Optional<Post> post = postRepository.findById(postId);
```

삭제 조건 포함 조회:

```java
Optional<Post> post = postRepository.findByPostIdAndDeletedFalse(postId);
```

권장:

- 단순 ID 조회는 findById 사용 가능
- 추가 조건이 있으면 필드명 기반 Query Method 사용
- Entity ID 필드명은 프로젝트 전체에서 통일
- `id`, `userId`, `postId` naming 혼용 주의
- Request PathVariable 이름과 Service parameter 이름도 일관성 유지

---

### [FAQ]

Q. findById와 findByPostId는 뭐가 달라?

A.
findById는 JpaRepository 기본 method로 Entity의 @Id를 기준으로 조회하고, findByPostId는 postId라는 필드명을 기준으로 Query Method를 생성한다.

Q. Entity ID 이름은 id가 좋아, postId가 좋아?

A.
둘 다 가능하다. 중요한 것은 프로젝트 전체에서 일관되게 사용하는 것이다.

---

# 8. Repository와 Transaction 연결

## 8.1 Service Transaction 안의 Repository

### [개념]

Repository는 Service Transaction 안에서 호출되는 것이 일반적이다.

Service의 `@Transactional` 범위 안에서 Repository가 Entity를 조회하면 해당 Entity는 Transaction 동안 영속 상태로 관리된다.

---

### [핵심]

흐름:

```text
Service @Transactional
→ Repository findById
→ Entity 영속 상태
→ Entity method로 상태 변경
→ Transaction commit
→ Dirty Checking
→ DB 반영
```

Repository와 Transaction 연결 기준:

- Transaction Boundary는 Service 중심
- Repository는 DB 접근 수행
- Entity 변경은 Transaction 안에서 수행
- Dirty Checking은 영속 상태 Entity 기준
- 조회 전용은 readOnly Transaction 고려
- Lazy Loading은 Transaction 범위 안에서 처리

---

### [실무]

Update 예:

```java
@Transactional
public UserResponse updateNickname(Long userId, UserUpdateRequest request) {
    User user = userRepository.findById(userId)
            .orElseThrow(() -> new BusinessException("USER_NOT_FOUND", "사용자를 찾을 수 없습니다."));

    user.changeNickname(request.nickname());

    return UserResponse.from(user);
}
```

설명:

```text
userRepository.findById
→ User Entity 영속 상태
→ user.changeNickname
→ commit 시 Dirty Checking
→ update query 실행 가능
```

---

### [주의]

주의할 상황:

- Transaction 밖에서 Entity 변경
- readOnly Transaction에서 Entity 변경
- Entity를 detached 상태로 변경
- Controller에서 Entity 변경
- Service method에 `@Transactional` 누락
- self-invocation으로 Transaction 미적용
- Entity 조회 후 DTO 변환을 Transaction 밖에서 수행

---

### [FAQ]

Q. Repository에서 조회한 Entity는 언제 Dirty Checking 돼?

A.
Service Transaction 안에서 조회된 영속 상태 Entity를 변경하고 commit되면 Dirty Checking으로 반영될 수 있다.

Q. Repository method에 Transaction을 붙여야 해?

A.
전체 비즈니스 흐름의 Transaction Boundary는 Service에 두는 것이 좋다.

---

## 8.2 Repository 호출 순서와 rollback

### [개념]

Service에서 여러 Repository를 호출하는 경우 하나의 Transaction으로 묶어야 데이터 일관성을 유지할 수 있다.

중간에 예외가 발생하면 이전 DB 변경도 rollback되어야 한다.

---

### [핵심]

여러 Repository 조합 예:

- 주문 생성 + 재고 감소
- 댓글 등록 + 게시글 댓글 수 증가
- 좋아요 등록 + 게시글 좋아요 수 증가
- 결제 저장 + 주문 상태 변경
- 알림 생성 + 사용자 알림 카운트 변경

---

### [실무]

예:

```java
@Transactional
public LikeResponse likePost(Long postId, Long userId) {
    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

    User user = userRepository.findById(userId)
            .orElseThrow(() -> new BusinessException("USER_NOT_FOUND", "사용자를 찾을 수 없습니다."));

    if (likeRepository.existsByPostAndUser(post, user)) {
        throw new BusinessException("ALREADY_LIKED", "이미 좋아요한 게시글입니다.");
    }

    Like like = Like.create(post, user);
    likeRepository.save(like);

    post.increaseLikeCount();

    return LikeResponse.from(like);
}
```

rollback 대상:

```text
Like 저장
Post 좋아요 수 증가
```

중간 예외 발생 시 둘 다 취소되어야 한다.

---

### [주의]

여러 Repository 호출 시 주의:

- 하나의 Use Case는 하나의 Service Transaction으로 묶음
- 중간 예외 발생 시 rollback 가능해야 함
- CustomException은 RuntimeException 기반 권장
- 외부 API 호출이 섞이면 Transaction 경계 재검토
- 동시성 이슈가 있으면 Lock / Unique Constraint 검토

---

### [FAQ]

Q. 여러 Repository를 호출하면 Transaction이 꼭 필요해?

A.
데이터 일관성이 필요한 하나의 Use Case라면 Service method에 @Transactional을 적용하는 것이 좋다.

Q. 좋아요 저장 후 카운트 증가 중 실패하면 어떻게 해?

A.
같은 Transaction 안에서 처리하면 중간 실패 시 좋아요 저장과 카운트 증가가 함께 rollback될 수 있다.

---

# 9. DTO Projection 기초

## 9.1 Projection 개념

### [개념]

Projection은 Entity 전체가 아니라 필요한 필드만 조회하는 방식이다.

Spring Boot Foundation 문서에서는 Projection을 깊게 다루지 않고, Repository와 DTO 연결 시 주의 기준만 다룬다.

---

### [핵심]

Projection 사용 가능 상황:

- 목록 조회에서 일부 필드만 필요
- 대용량 조회 최적화 필요
- Entity 전체 로딩이 부담
- 통계성 조회
- 조인 결과 일부만 필요

Projection 방식:

- Interface Projection
- DTO Projection
- JPQL select new
- QueryDSL Projection

---

### [실무]

기초 구조에서는 우선 Entity 조회 후 Response DTO 변환:

```java
@Transactional(readOnly = true)
public List<PostSummaryResponse> getPostSummaries() {
    return postRepository.findAllByDeletedFalseOrderByCreatedAtDesc().stream()
            .map(PostSummaryResponse::from)
            .toList();
}
```

조회 최적화가 필요하면 Projection 검토:

```java
public record PostSummaryResponse(
        Long postId,
        String title,
        String writerName
) {
}
```

JPQL DTO Projection 예:

```java
@Query("""
       select new com.example.project.dto.response.PostSummaryResponse(
           p.postId,
           p.title,
           u.nickname
       )
       from Post p
       join p.writer u
       where p.deleted = false
       """)
List<PostSummaryResponse> findPostSummaries();
```

---

### [주의]

Projection 주의:

- Repository가 API 응답 정책에 과도하게 결합되지 않게 주의
- DTO Projection은 조회 전용으로 사용
- Command 작업에는 Entity 조회 후 상태 변경
- 복잡한 Projection은 JPA Advanced / QueryDSL 문서 기준
- Projection으로 Entity 변경 불가
- Projection 남용 시 구조 복잡도 증가

---

### [FAQ]

Q. Repository에서 DTO를 바로 조회해도 돼?

A.
조회 최적화가 필요하면 가능하다. 다만 API 응답 정책과 Repository가 과도하게 결합되지 않도록 주의해야 한다.

Q. Projection은 언제 써?

A.
Entity 전체가 필요 없고 목록이나 통계 조회에서 필요한 필드만 가져오고 싶을 때 검토한다.

Q. Projection으로 Entity 수정도 가능해?

A.
아니다. Projection은 조회 전용으로 보고, 수정 작업은 Entity를 조회해 Transaction 안에서 변경하는 것이 좋다.

---

# 10. JPQL / Native Query 연결 기준

## 10.1 @Query 사용 기준

### [개념]

`@Query`는 Repository Method에 JPQL 또는 Native SQL을 직접 작성하는 방식이다.

Query Method로 표현하기 어렵거나 명확한 조회 쿼리가 필요한 경우 사용할 수 있다.

---

### [핵심]

@Query 사용 상황:

- Query Method 이름이 너무 길어짐
- 명확한 JPQL이 더 읽기 쉬움
- join 조회 필요
- DTO Projection 필요
- 집계 조회 필요
- 조건이 고정된 복잡한 조회

---

### [실무]

JPQL 예:

```java
@Query("""
       select p
       from Post p
       where p.deleted = false
       order by p.createdAt desc
       """)
List<Post> findActivePosts();
```

Parameter Binding:

```java
@Query("""
       select p
       from Post p
       where p.category = :category
       and p.deleted = false
       """)
List<Post> findActivePostsByCategory(@Param("category") PostCategory category);
```

DTO Projection:

```java
@Query("""
       select new com.example.project.dto.response.PostSummaryResponse(
           p.postId,
           p.title
       )
       from Post p
       where p.deleted = false
       """)
List<PostSummaryResponse> findPostSummaries();
```

권장:

- Query Method보다 JPQL이 명확하면 @Query 사용
- parameter binding은 `@Param`으로 명확화
- Native Query는 필요한 경우에만 사용
- 복잡한 동적 쿼리는 QueryDSL 검토
- Query는 테스트로 검증

---

### [FAQ]

Q. @Query는 언제 써?

A.
Query Method 이름이 너무 길거나 join, 집계, DTO Projection처럼 직접 JPQL이 더 명확할 때 사용한다.

Q. JPQL과 SQL은 같아?

A.
아니다. JPQL은 Entity와 필드 기준으로 작성하고 SQL은 Table과 Column 기준으로 작성한다.

---

## 10.2 Native Query 주의

### [개념]

Native Query는 실제 Database SQL을 Repository에 직접 작성하는 방식이다.

DB 특화 기능이 필요할 때 사용할 수 있지만 이식성과 유지보수성을 주의해야 한다.

---

### [핵심]

Native Query 사용 상황:

- DB 전용 함수 사용
- 복잡한 SQL 최적화
- 성능 튜닝 Query
- View / Legacy Table 조회
- JPQL로 표현이 어려운 Query

주의:

- DB 종속성 증가
- Entity 필드명이 아닌 Table / Column 이름 사용
- DB 변경에 취약
- 테스트 중요
- Projection mapping 주의
- 복잡한 Native Query 남용 금지

---

### [실무]

예:

```java
@Query(
        value = """
                select *
                from posts
                where deleted = false
                order by created_at desc
                """,
        nativeQuery = true
)
List<Post> findActivePostsNative();
```

권장:

- Native Query 사용 이유를 명확히 함
- JPQL로 가능한지 먼저 검토
- DB column naming 확인
- 반환 타입 mapping 확인
- 운영 DB와 테스트 DB 차이 주의
- 복잡한 Native Query는 별도 문서화

---

### [FAQ]

Q. Native Query는 쓰면 안 돼?

A.
필요하면 사용할 수 있다. 다만 DB 종속성과 유지보수 비용이 커질 수 있으므로 JPQL이나 QueryDSL로 가능한지 먼저 검토한다.

Q. Native Query에서 Entity 필드명을 써?

A.
아니다. Native Query는 실제 Table과 Column 이름을 사용한다.

---

# 11. Repository Integration Anti Pattern

## 11.1 Common Anti Pattern

### [개념]

Repository Integration Anti Pattern은 Repository 책임이 Service, Controller, API 응답 책임과 섞이는 구조다.

이런 구조는 Layered Architecture를 무너뜨리고 테스트와 유지보수를 어렵게 만든다.

---

### [핵심]

자주 발생하는 Anti Pattern:

- Controller에서 Repository 직접 호출
- Repository에서 ApiResponse 반환
- Repository에서 Business Logic 처리
- Optional.get 직접 사용
- Entity 직접 Response 반환
- Query Method 이름 과도하게 길어짐
- findAll 후 Application에서 필터링
- 개수만 필요한데 전체 목록 조회
- Transaction 없이 Entity 변경
- Repository에 외부 API 호출 코드 작성
- Native Query 남용
- DTO / Entity 책임 혼합
- 삭제 조건 누락
- 정렬 없는 목록 조회

---

### [실무]

Anti Pattern 예:

```java
@RestController
@RequiredArgsConstructor
public class UserController {

    private final UserRepository userRepository;

    @GetMapping("/users/{userId}")
    public User getUser(@PathVariable Long userId) {
        return userRepository.findById(userId).get();
    }
}
```

문제:

- Controller가 Repository 직접 호출
- Optional.get 사용
- Entity 직접 반환
- CustomException 없음
- GlobalExceptionHandler와 연결 어려움
- DTO 경계 없음

개선:

```java
@RestController
@RequiredArgsConstructor
public class UserController {

    private final UserService userService;

    @GetMapping("/users/{userId}")
    public ApiResponse<UserResponse> getUser(@PathVariable Long userId) {
        return ApiResponse.success(userService.getUser(userId));
    }
}
```

```java
@Service
@RequiredArgsConstructor
public class UserService {

    private final UserRepository userRepository;

    @Transactional(readOnly = true)
    public UserResponse getUser(Long userId) {
        User user = userRepository.findById(userId)
                .orElseThrow(() -> new BusinessException("USER_NOT_FOUND", "사용자를 찾을 수 없습니다."));

        return UserResponse.from(user);
    }
}
```

---

### [Troubleshooting]

문제: API 응답에 원하지 않는 Entity 필드가 노출됨

```text
원인:
Entity를 Controller Response로 직접 반환

해결:
Response DTO를 만들고 Service에서 DTO로 변환 후 반환
```

문제: Repository method 이름이 너무 길어짐

```text
원인:
복잡한 검색 조건을 Query Method로 모두 표현

해결:
JPQL, QueryDSL, SearchCondition DTO, Custom Repository 검토
```

문제: 목록 조회가 느림

```text
원인 후보:
findAll 후 Application 필터링
정렬 / pagination 없음
N+1 문제
불필요한 Entity 전체 조회
count query 부담

해결:
Repository query 조건 추가
Page / Slice 적용
Projection 검토
JPA Advanced / QueryDSL 기준 확인
```

문제: 중복 데이터가 생김

```text
원인 후보:
existsBy 검사만 사용
DB Unique Constraint 없음
동시 요청 처리 미흡

해결:
Service Business Validation + DB Unique Constraint 함께 적용
동시성 요구가 크면 Lock 전략 검토
```

---

### [FAQ]

Q. Repository Integration에서 가장 흔한 실수는?

A.
Controller에서 Repository를 직접 호출하고 Entity를 그대로 반환하는 구조가 가장 흔하다.

Q. findAll로 다 가져온 뒤 Service에서 필터링해도 돼?

A.
데이터가 적으면 가능하지만 권장하지 않는다. 가능한 조건은 DB Query에서 처리하는 것이 좋다.

Q. Repository에 외부 API 호출을 넣어도 돼?

A.
안 된다. Repository는 데이터 접근 계층이고 외부 API 호출은 ExternalApiClient나 Service에서 조율하는 것이 좋다.

---

# 12. Repository Review Checklist

## 12.1 Repository Integration Checklist

### [개념]

Repository Integration Checklist는 Backend Agent가 Spring Boot Repository와 JPA 연결 구조를 검수할 때 사용하는 기준이다.

---

### [핵심]

검수 항목:

```md
- [ ] Repository가 JpaRepository를 상속하는가?
- [ ] Entity 타입과 ID 타입이 정확한가?
- [ ] Repository가 Main Class 하위 scan 범위에 있는가?
- [ ] Entity에 @Entity와 @Id가 있는가?
- [ ] Controller가 Repository를 직접 호출하지 않는가?
- [ ] Service에서 Repository를 호출하는가?
- [ ] Repository가 Business Logic을 포함하지 않는가?
- [ ] 단건 조회는 Optional로 표현하는가?
- [ ] Optional.get을 직접 사용하지 않는가?
- [ ] Service에서 orElseThrow로 CustomException을 발생시키는가?
- [ ] existsBy를 존재 여부 확인에 적절히 사용하는가?
- [ ] countBy를 개수 조회에 적절히 사용하는가?
- [ ] 목록 조회에 Pagination을 고려했는가?
- [ ] Page와 Slice 선택 기준이 명확한가?
- [ ] Repository가 ApiResponse를 반환하지 않는가?
- [ ] Entity 직접 Response 반환을 피하는가?
- [ ] Query Method 이름이 과도하게 길지 않은가?
- [ ] 복잡한 동적 검색은 QueryDSL / Custom Repository를 검토했는가?
- [ ] Native Query를 남용하지 않는가?
- [ ] Transaction Boundary는 Service에 있는가?
- [ ] Entity 변경은 Transaction 안에서 수행되는가?
- [ ] 삭제 조건이나 상태 조건이 필요한 조회에 반영되어 있는가?
- [ ] 정렬 기준이 필요한 목록 조회에 적용되어 있는가?
- [ ] 대용량 조회에서 findAll 남용을 피하는가?
```

---

### [실무]

Repository 검수 흐름:

```text
Entity 확인
→ Repository Generic 타입 확인
→ Query Method 이름 확인
→ 반환 타입 확인
→ Service 호출 구조 확인
→ Optional 처리 확인
→ Transaction 위치 확인
→ DTO 변환 위치 확인
→ Pagination 확인
→ Query 성능 위험 확인
→ Anti Pattern 확인
```

---

### [FAQ]

Q. Repository 검수에서 가장 먼저 볼 것은?

A.
Repository가 Entity와 ID 타입을 정확히 지정하고 Service에서 호출되는지 먼저 확인한다.

Q. Repository 품질의 핵심 기준은?

A.
Entity 중심, 데이터 접근 책임 집중, Optional 처리, Service Transaction 연결, DTO 경계 유지, Query Method 복잡도 관리다.

---

# Retrieval Queries

### [FAQ]

Q. Spring Boot Repository Integration은 뭐야?
A. Service Layer가 Repository를 통해 Entity를 조회, 저장, 삭제하고 JPA와 Database에 연결되는 구조다.

Q. Repository는 왜 필요해?
A. DB 접근 책임을 Service와 분리하고 Entity 중심으로 데이터 접근을 추상화하기 위해 필요하다.

Q. Repository의 책임은 뭐야?
A. Entity 저장, 조회, 삭제, Query Method, 존재 여부 확인, pagination 조회 같은 데이터 접근이다.

Q. Repository가 담당하지 말아야 할 것은?
A. Business Logic, HTTP 요청 처리, API 응답 생성, 권한 검사, 외부 API 호출은 Repository 책임이 아니다.

Q. Controller에서 Repository를 바로 호출해도 돼?
A. 실무 구조에서는 권장하지 않는다. Service를 통해 Business Logic과 Transaction Boundary를 관리하는 것이 좋다.

Q. JpaRepository는 뭐야?
A. Spring Data JPA가 제공하는 기본 Repository Interface이며 CRUD, pagination, sorting 기능을 제공한다.

Q. JpaRepository Generic 타입은 어떻게 정해?
A. 첫 번째는 Entity 타입, 두 번째는 Entity의 @Id 필드 타입을 지정한다.

Q. Repository에 @Repository를 붙여야 해?
A. Spring Data JPA Repository Interface는 보통 JpaRepository를 상속하면 자동으로 Bean 등록되므로 별도 @Repository를 붙이지 않아도 된다.

Q. Repository Bean 등록이 안 되면 뭘 확인해?
A. Repository 위치, Main Class 위치, JpaRepository 상속 여부, Entity @Entity 여부, Spring Data JPA 의존성을 확인한다.

Q. Query Method는 뭐야?
A. Repository method 이름으로 조회 조건을 표현하면 Spring Data JPA가 Query를 생성하는 기능이다.

Q. findBy는 언제 써?
A. 특정 필드 조건으로 Entity를 조회할 때 사용한다.

Q. existsBy는 언제 써?
A. 중복 이메일, 이미 좋아요 여부, 이미 찜 여부처럼 존재 여부만 필요한 경우 사용한다.

Q. countBy는 언제 써?
A. 읽지 않은 알림 수, 댓글 수, 게시글 수처럼 조건에 맞는 개수만 필요할 때 사용한다.

Q. Query Method 이름이 너무 길면 어떻게 해?
A. JPQL, QueryDSL, SearchCondition DTO, Custom Repository를 검토하는 것이 좋다.

Q. 검색 필터가 여러 개면 Query Method를 다 만들면 돼?
A. 필터 조합이 많으면 Query Method가 폭발하므로 QueryDSL 같은 동적 쿼리 방식을 검토한다.

Q. Optional은 어디서 처리해?
A. Repository는 Optional을 반환하고 Service에서 orElseThrow로 CustomException을 발생시키는 것이 좋다.

Q. Optional.get은 왜 피해야 해?
A. 값이 없을 때 예외가 불명확하고 ErrorCode를 통제하기 어렵기 때문이다.

Q. Optional을 Controller까지 넘겨도 돼?
A. 권장하지 않는다. 조회 실패 처리는 Service와 GlobalExceptionHandler에서 처리하는 것이 좋다.

Q. existsBy만 쓰면 중복 데이터가 완전히 막혀?
A. 아니다. 동시 요청까지 고려하면 DB Unique Constraint도 함께 적용하는 것이 좋다.

Q. 개수만 필요할 때 findAll 후 size를 써도 돼?
A. 권장하지 않는다. 개수만 필요하면 countBy를 사용하는 것이 좋다.

Q. Page와 Slice 차이는?
A. Page는 전체 개수를 포함하고 Slice는 다음 페이지 존재 여부 중심이다. 무한 스크롤은 Slice가 적합할 수 있다.

Q. Pageable은 어디서 받아?
A. Controller에서 Pageable을 받고 Service를 거쳐 Repository에 전달하는 구조가 일반적이다.

Q. Page나 Slice 안의 Entity를 DTO로 바꾸려면?
A. map(PostResponse::from)처럼 map을 사용해 Entity를 Response DTO로 변환할 수 있다.

Q. Pageable page는 0부터 시작해?
A. Spring Pageable은 기본적으로 page index가 0부터 시작한다. Frontend와 기준을 맞춰야 한다.

Q. 목록 조회에 정렬 기준이 꼭 필요해?
A. 권장된다. 정렬 기준이 없으면 응답 순서가 불안정해질 수 있다.

Q. Repository는 Entity 중심이어야 해?
A. 기초 구조에서는 Entity 중심이 좋다. 복잡한 조회 최적화가 필요할 때 Projection이나 QueryDSL을 검토한다.

Q. Repository에서 Response DTO를 바로 반환해도 돼?
A. 조회 최적화 목적의 Projection은 가능하지만 ApiResponse 같은 API 응답 형식을 Repository에 결합하는 것은 지양한다.

Q. findById와 findByPostId는 뭐가 달라?
A. findById는 JpaRepository 기본 method로 @Id를 기준으로 조회하고, findByPostId는 postId 필드명을 기준으로 Query Method를 생성한다.

Q. Entity ID 이름은 id가 좋아, postId가 좋아?
A. 둘 다 가능하다. 중요한 것은 프로젝트 전체에서 일관되게 사용하는 것이다.

Q. Repository에서 조회한 Entity는 언제 Dirty Checking 돼?
A. Service Transaction 안에서 조회된 영속 상태 Entity를 변경하고 commit되면 Dirty Checking으로 반영될 수 있다.

Q. Repository method에 Transaction을 붙여야 해?
A. 전체 비즈니스 흐름의 Transaction Boundary는 Service에 두는 것이 좋다.

Q. 여러 Repository를 호출하면 Transaction이 필요해?
A. 데이터 일관성이 필요한 하나의 Use Case라면 Service method에 @Transactional을 적용하는 것이 좋다.

Q. Projection은 언제 써?
A. Entity 전체가 필요 없고 목록이나 통계 조회에서 필요한 필드만 가져오고 싶을 때 검토한다.

Q. Projection으로 Entity 수정도 가능해?
A. 아니다. Projection은 조회 전용으로 보고, 수정 작업은 Entity를 조회해 Transaction 안에서 변경하는 것이 좋다.

Q. @Query는 언제 써?
A. Query Method 이름이 너무 길거나 join, 집계, DTO Projection처럼 직접 JPQL이 더 명확할 때 사용한다.

Q. JPQL과 SQL은 같아?
A. 아니다. JPQL은 Entity와 필드 기준으로 작성하고 SQL은 Table과 Column 기준으로 작성한다.

Q. Native Query는 쓰면 안 돼?
A. 필요하면 사용할 수 있다. 다만 DB 종속성과 유지보수 비용이 커질 수 있으므로 JPQL이나 QueryDSL로 가능한지 먼저 검토한다.

Q. Native Query에서는 Entity 필드명을 써?
A. 아니다. Native Query는 실제 Table과 Column 이름을 사용한다.

Q. findAll로 다 가져온 뒤 Service에서 필터링해도 돼?
A. 데이터가 적으면 가능하지만 권장하지 않는다. 가능한 조건은 DB Query에서 처리하는 것이 좋다.

Q. Repository에 외부 API 호출을 넣어도 돼?
A. 안 된다. Repository는 데이터 접근 계층이고 외부 API 호출은 ExternalApiClient나 Service에서 조율하는 것이 좋다.

Q. Repository Integration Anti Pattern은 뭐가 있어?
A. Controller에서 Repository 직접 호출, Entity 직접 반환, Optional.get 사용, findAll 후 필터링, Native Query 남용, Repository에서 ApiResponse 반환 등이 있다.

Q. Repository 검수에서 가장 먼저 볼 것은?
A. Repository가 Entity와 ID 타입을 정확히 지정하고 Service에서 호출되는지 먼저 확인한다.

Q. Repository 품질의 핵심 기준은?
A. Entity 중심, 데이터 접근 책임 집중, Optional 처리, Service Transaction 연결, DTO 경계 유지, Query Method 복잡도 관리다.
