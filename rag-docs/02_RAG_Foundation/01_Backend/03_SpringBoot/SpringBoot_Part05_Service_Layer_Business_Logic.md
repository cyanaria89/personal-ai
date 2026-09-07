# Spring Boot Part05 - Service Layer & Business Logic

---

# 1. Service Layer

## 1.1 Service Layer 개념

### [개념]

Service Layer는 Spring Boot Application에서 비즈니스 로직을 처리하는 계층이다.

Service는 Controller와 Repository 사이에 위치하며, HTTP 요청 처리와 DB 접근 로직 사이의 비즈니스 흐름을 담당한다.

기본 구조:

```text
Controller
→ Service
→ Repository
→ Database
```

Service Layer의 핵심 목적:

- Business Logic 처리
- Use Case 단위 기능 구현
- Transaction Boundary 설정
- Repository 조합
- Entity 조회 / 생성 / 변경
- Custom Exception 발생
- DTO 변환 조율
- 외부 API 호출 조율
- Controller Thin Rule 유지

---

### [핵심]

Service Layer 책임:

- 비즈니스 규칙 적용
- 여러 Repository 호출 조합
- Entity 상태 변경
- Transaction 관리
- 예외 처리 기준 제공
- Request DTO를 Entity 작업으로 변환
- Entity를 Response DTO로 변환
- Controller가 비대해지는 것 방지

Service Layer 금지:

- HTTP Request / Response 직접 처리
- URL Mapping 처리
- View 반환
- SQL 세부 구현 직접 작성
- 과도한 외부 형식 의존
- Controller 역할 침범
- Repository 역할 침범

---

### [실무]

Service는 하나의 사용자 기능 또는 Use Case를 표현하는 public method 중심으로 작성한다.

예:

```java
@Service
@RequiredArgsConstructor
public class PostService {

    private final PostRepository postRepository;

    @Transactional
    public PostResponse createPost(PostCreateRequest request) {
        Post post = Post.create(
                request.title(),
                request.content()
        );

        Post savedPost = postRepository.save(post);

        return PostResponse.from(savedPost);
    }
}
```

실무 기준:

- Service class에는 `@Service` 사용
- 의존성은 생성자 주입 사용
- 필드는 `final`로 선언
- 쓰기 작업에는 `@Transactional` 적용
- 조회 작업에는 `@Transactional(readOnly = true)` 고려
- public method는 Use Case 단위로 작성
- Controller는 Service 호출만 담당
- Repository는 Service 내부에서 호출
- Entity 직접 반환은 지양
- Response DTO로 변환 후 반환

---

### [FAQ]

Q. Service Layer는 왜 필요해?

A.
Controller에서 비즈니스 로직을 분리하고 Transaction, Repository 조합, Entity 변경, 예외 처리를 한 곳에서 관리하기 위해 필요하다.

Q. Controller에서 Repository를 바로 호출하면 안 돼?

A.
간단한 예제에서는 가능하지만 실무에서는 Service를 거쳐 비즈니스 로직과 Transaction Boundary를 관리하는 것이 좋다.

Q. Service는 무조건 만들어야 해?

A.
실무 Backend 구조에서는 대부분 필요하다. 기능이 작아도 책임 분리와 테스트 가능성을 위해 Service Layer를 두는 것이 좋다.

---

# 2. Service Responsibility

## 2.1 Service 책임 분리

### [개념]

Service Responsibility는 Service가 담당해야 할 작업과 담당하지 말아야 할 작업을 구분하는 기준이다.

Service는 Application Use Case를 구현하는 계층이다.

Use Case 예:

```text
회원가입
게시글 작성
게시글 수정
댓글 등록
주문 생성
결제 승인
축제 찜 등록
알림 조회
```

---

### [핵심]

Service가 담당해야 하는 것:

- 사용자 기능 흐름
- 비즈니스 조건 검사
- Entity 조회
- Entity 생성
- Entity 상태 변경
- Repository 호출 순서 결정
- 예외 발생
- Transaction 범위 지정
- Response DTO 반환
- 외부 API Client 호출 조율

Service가 담당하지 않는 것:

- HTTP Method 판단
- Request URL Mapping
- JSON Binding
- Validation Trigger
- DB Query 세부 구현
- Entity Mapping 설정
- 화면 표시
- Frontend 상태 관리

---

### [실무]

좋은 Service 흐름:

```text
Request DTO 수신
→ Entity 조회
→ 비즈니스 조건 검사
→ Entity 상태 변경
→ Repository 저장
→ Response DTO 반환
```

예:

```java
@Transactional
public PostResponse updatePost(Long postId, PostUpdateRequest request) {
    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

    post.update(
            request.title(),
            request.content()
    );

    return PostResponse.from(post);
}
```

포인트:

- 게시글 조회는 Repository
- 게시글 없음 판단은 Service
- 게시글 상태 변경은 Entity method
- 응답 변환은 Response DTO
- 전체 작업은 Service method의 Transaction 안에서 처리

---

### [Comparison]

| 구분        | Controller                              | Service                 | Repository                    |
| ----------- | --------------------------------------- | ----------------------- | ----------------------------- |
| 주요 책임   | HTTP 요청 / 응답                        | 비즈니스 로직           | 데이터 접근                   |
| 입력        | Request DTO, PathVariable, RequestParam | DTO, id, command        | Entity, query parameter       |
| 출력        | ApiResponse                             | Response DTO, 결과 객체 | Entity, Optional, List, Slice |
| 예외 처리   | 직접 처리 지양                          | 비즈니스 예외 발생      | 조회 실패 표현                |
| Transaction | 지양                                    | 권장 위치               | 직접 경계 관리 지양           |
| 테스트      | Web Layer Test                          | Unit / Integration Test | Data JPA Test                 |

---

### [FAQ]

Q. Service에서 DTO를 받아도 돼?

A.
가능하다. Controller에서 Request DTO를 받고 Service가 해당 DTO를 이용해 Use Case를 처리하는 구조는 일반적이다.

Q. Service에서 Response DTO를 반환해도 돼?

A.
가능하다. 다만 팀 규칙에 따라 Service가 DTO를 반환할지 Entity를 반환하고 Controller에서 변환할지 일관되게 정해야 한다.

Q. Service에서 Entity 변경 메서드를 호출하는 게 좋아?

A.
좋다. Service는 흐름을 제어하고 실제 상태 변경 규칙은 Entity method로 캡슐화하면 책임이 더 명확해진다.

---

## 2.2 Service Method Naming

### [개념]

Service Method Naming은 Service의 public method 이름을 Use Case 중심으로 작성하는 규칙이다.

Service method 이름은 구현 방식보다 사용자의 기능 의도를 드러내야 한다.

---

### [핵심]

권장 이름:

- createPost
- updatePost
- deletePost
- getPost
- getPosts
- signUp
- login
- addFavorite
- cancelFavorite
- approvePayment
- sendNotification

비권장 이름:

- save
- process
- handle
- doPost
- execute
- logic
- serviceMethod
- insertData
- updateData

---

### [실무]

좋은 예:

```java
@Transactional
public CommentResponse createComment(Long postId, CommentCreateRequest request) {
    ...
}
```

나쁜 예:

```java
@Transactional
public CommentResponse process(Long id, CommentCreateRequest request) {
    ...
}
```

권장 기준:

- Method 이름만 보고 기능을 추측할 수 있어야 함
- CRUD라도 도메인 의미를 반영
- `process`, `handle`, `execute` 남용 금지
- 너무 긴 이름은 책임 과다 신호
- 하나의 method가 여러 Use Case를 처리하면 분리 검토

---

### [FAQ]

Q. Service method 이름은 어떻게 짓는 게 좋아?

A.
createPost, updateUser, addFavorite처럼 사용자의 기능 또는 Use Case가 드러나는 이름이 좋다.

Q. process 같은 이름은 왜 안 좋아?

A.
무엇을 처리하는지 알기 어렵고, 여러 책임이 섞여도 이름에서 드러나지 않기 때문이다.

---

# 3. Business Logic

## 3.1 Business Logic 개념

### [개념]

Business Logic은 Application이 해결해야 하는 업무 규칙이다.

Spring Boot에서 Business Logic은 주로 Service Layer에 위치한다.

Business Logic 예:

- 이미 가입된 이메일은 회원가입 불가
- 게시글 작성자만 수정 가능
- 삭제된 게시글은 조회 불가
- 재고가 부족하면 주문 불가
- 결제 완료 후 주문 상태 변경
- 본인은 자기 게시글에 좋아요 불가
- 이미 찜한 축제는 중복 찜 불가

---

### [핵심]

Business Logic 판단 기준:

- 데이터의 상태를 변경하는가?
- 여러 조건을 검사하는가?
- 도메인 규칙을 적용하는가?
- 실패 시 비즈니스 예외가 필요한가?
- 여러 Repository를 조합하는가?
- Transaction이 필요한가?
- 단순 조회가 아니라 의미 있는 Use Case인가?

위 항목에 해당하면 Service Layer에 배치한다.

---

### [실무]

예:

```java
@Transactional
public FavoriteResponse addFavorite(Long userId, Long festivalId) {
    User user = userRepository.findById(userId)
            .orElseThrow(() -> new BusinessException("USER_NOT_FOUND", "사용자를 찾을 수 없습니다."));

    Festival festival = festivalRepository.findById(festivalId)
            .orElseThrow(() -> new BusinessException("FESTIVAL_NOT_FOUND", "축제를 찾을 수 없습니다."));

    if (favoriteRepository.existsByUserAndFestival(user, festival)) {
        throw new BusinessException("ALREADY_FAVORITED", "이미 찜한 축제입니다.");
    }

    Favorite favorite = Favorite.create(user, festival);
    favoriteRepository.save(favorite);

    return FavoriteResponse.from(favorite);
}
```

이 코드의 Business Logic:

- 사용자 존재 여부 확인
- 축제 존재 여부 확인
- 중복 찜 여부 확인
- 찜 Entity 생성
- 저장 후 응답 반환

---

### [주의]

Business Logic을 Controller에 넣으면 안 좋은 이유:

- Controller가 비대해짐
- HTTP 책임과 업무 책임이 섞임
- 테스트가 어려워짐
- 중복 코드가 늘어남
- Transaction 관리가 애매해짐
- API 변경과 비즈니스 변경이 강하게 결합됨

Business Logic을 Repository에 넣으면 안 좋은 이유:

- DB 접근 책임과 업무 판단 책임이 섞임
- Query 재사용성이 떨어짐
- 테스트 범위가 불명확해짐
- Repository Method 이름이 과도하게 길어짐

---

### [FAQ]

Q. Business Logic은 어디에 넣어?

A.
대부분 Service Layer에 넣는다. Entity 자체의 상태 변경 규칙은 Entity method로 분리할 수 있다.

Q. 중복 이메일 검사는 Business Logic이야?

A.
그렇다. 단순 형식 검증이 아니라 도메인 규칙이므로 Service에서 Repository를 통해 검사하고 예외를 발생시키는 것이 좋다.

Q. 비즈니스 조건이 많아지면 어떻게 해?

A.
Service 내부 private method로 정리하거나 별도 Domain Service, Policy Component, Validator Component 분리를 검토한다.

---

## 3.2 Validation과 Business Validation 구분

### [개념]

Validation은 요청 값의 기본 형식 검증이고 Business Validation은 도메인 규칙 검증이다.

두 검증은 위치와 목적이 다르다.

---

### [핵심]

Validation 예:

- 이메일 형식 확인
- 빈 문자열 확인
- 글자 수 제한
- 숫자 최소 / 최대값 확인
- null 여부 확인

Business Validation 예:

- 이메일 중복 여부 확인
- 작성자 권한 확인
- 게시글 삭제 상태 확인
- 주문 가능 상태 확인
- 이미 좋아요 했는지 확인
- 재고 부족 여부 확인

---

### [Comparison]

| 구분      | Validation                      | Business Validation               |
| --------- | ------------------------------- | --------------------------------- |
| 목적      | 입력 형식 검증                  | 업무 규칙 검증                    |
| 위치      | Request DTO / Controller        | Service                           |
| 도구      | @Valid, Bean Validation         | Repository 조회, Entity 상태 확인 |
| 실패 예외 | MethodArgumentNotValidException | CustomException                   |
| 예        | @NotBlank, @Email               | 중복 이메일, 권한 없음            |

---

### [실무]

Request DTO Validation:

```java
public record SignUpRequest(
        @Email String email,
        @NotBlank String password,
        @NotBlank String nickname
) {
}
```

Service Business Validation:

```java
@Transactional
public UserResponse signUp(SignUpRequest request) {
    if (userRepository.existsByEmail(request.email())) {
        throw new BusinessException("DUPLICATED_EMAIL", "이미 사용 중인 이메일입니다.");
    }

    User user = User.create(
            request.email(),
            request.password(),
            request.nickname()
    );

    return UserResponse.from(userRepository.save(user));
}
```

권장:

- 형식 검증은 Request DTO
- 업무 규칙 검증은 Service
- 실패 응답은 GlobalExceptionHandler에서 통일
- Business Validation 실패는 명확한 ErrorCode 사용
- Controller에서 중복 검사하지 않음

---

### [FAQ]

Q. @Valid로 이메일 중복 검사까지 할 수 있어?

A.
기술적으로 Custom Validator로 가능하지만 기초 구조에서는 중복 이메일처럼 Repository 조회가 필요한 비즈니스 검증은 Service에서 처리하는 것이 명확하다.

Q. Validation과 Business Validation을 왜 구분해야 해?

A.
입력 형식 오류와 업무 규칙 위반은 원인과 처리 방식이 다르기 때문에 분리해야 유지보수가 쉽다.

---

# 4. Service와 Entity 변경

## 4.1 Entity 상태 변경 기준

### [개념]

Entity 상태 변경은 도메인 데이터의 값을 수정하는 작업이다.

Service는 Entity를 조회하고, 필요한 Business Logic을 검사한 뒤 Entity method를 호출해 상태를 변경한다.

---

### [핵심]

권장 흐름:

```text
Service
→ Entity 조회
→ 권한 / 상태 검사
→ Entity method 호출
→ Transaction commit
→ Dirty Checking 반영
```

Entity 변경 예:

- 게시글 제목 수정
- 회원 닉네임 변경
- 주문 상태 변경
- 좋아요 수 증가
- 알림 읽음 처리
- 삭제 상태 변경

---

### [실무]

Entity method 예:

```java
@Entity
public class Post {

    private String title;
    private String content;

    public void update(String title, String content) {
        this.title = title;
        this.content = content;
    }
}
```

Service 예:

```java
@Transactional
public PostResponse updatePost(Long postId, Long userId, PostUpdateRequest request) {
    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

    if (!post.isWriter(userId)) {
        throw new BusinessException("NO_PERMISSION", "게시글 수정 권한이 없습니다.");
    }

    post.update(request.title(), request.content());

    return PostResponse.from(post);
}
```

포인트:

- Service는 권한과 흐름을 판단
- Entity는 자신의 상태 변경을 수행
- Transaction 안에서 변경해야 Dirty Checking 가능
- setter 남용보다 의미 있는 method 권장

---

### [Best Practice]

Entity 변경 Best Practice:

- 무분별한 public setter 지양
- 의미 있는 Entity method 사용
- 상태 변경 전 Service에서 권한 / 존재 여부 확인
- Entity 내부에서 자기 상태에 대한 기본 규칙 보장
- 복잡한 Use Case 흐름은 Service에서 조율
- 변경 작업은 `@Transactional` 안에서 수행

예:

```java
post.updateTitle(newTitle);
post.markDeleted();
notification.markAsRead();
order.completePayment();
favorite.cancel();
```

---

### [FAQ]

Q. Entity에 setter를 열어두면 안 돼?

A.
가능은 하지만 무분별한 setter는 어디서 어떤 이유로 상태가 바뀌는지 추적하기 어렵다. 의미 있는 method를 권장한다.

Q. Entity 변경 후 save를 꼭 호출해야 해?

A.
JPA 영속 상태 Entity라면 Transaction commit 시 Dirty Checking으로 반영될 수 있다. 다만 신규 Entity 저장은 save가 필요하다.

Q. Entity method와 Service method 차이는 뭐야?

A.
Service method는 Use Case 흐름을 조율하고 Entity method는 Entity 자신의 상태 변경을 표현한다.

---

## 4.2 DTO 변환 위치 기준

### [개념]

DTO 변환은 Request DTO, Entity, Response DTO 사이의 데이터를 변환하는 작업이다.

Spring Boot Foundation 구조에서는 DTO 변환 위치를 팀 규칙으로 일관되게 정하는 것이 중요하다.

---

### [핵심]

DTO 변환 대상:

- Request DTO → Entity 생성 값
- Entity → Response DTO
- 외부 API Response → 내부 DTO
- Page / Slice Entity → Page / Slice Response DTO
- 여러 Entity 조합 → 통합 Response DTO

---

### [실무]

Response DTO static factory 예:

```java
public record PostResponse(
        Long postId,
        String title,
        String content
) {
    public static PostResponse from(Post post) {
        return new PostResponse(
                post.getId(),
                post.getTitle(),
                post.getContent()
        );
    }
}
```

Service에서 변환:

```java
@Transactional(readOnly = true)
public PostResponse getPost(Long postId) {
    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

    return PostResponse.from(post);
}
```

목록 변환:

```java
@Transactional(readOnly = true)
public List<PostResponse> getPosts() {
    return postRepository.findAll().stream()
            .map(PostResponse::from)
            .toList();
}
```

권장:

- Entity를 Controller Response로 직접 반환하지 않음
- Response DTO 변환 방식 통일
- 단순 변환은 DTO의 `from` 사용 가능
- 복잡한 조합은 Service 또는 Mapper Component 검토
- 외부 API DTO와 내부 Response DTO 분리

---

### [주의]

DTO 변환 Anti Pattern:

```java
@GetMapping("/{postId}")
public Post getPost(@PathVariable Long postId) {
    return postRepository.findById(postId).get();
}
```

문제:

- Entity 직접 노출
- Lazy Loading 문제 가능
- 민감정보 노출 가능
- API 응답 구조 불안정
- Controller가 Repository 직접 호출
- Optional get 사용 위험

---

### [FAQ]

Q. DTO 변환은 Controller에서 해도 돼?

A.
가능하지만 Controller Thin Rule을 유지하려면 Service에서 Response DTO까지 반환하거나 DTO의 static factory를 사용하는 방식이 일반적이다.

Q. Mapper 클래스를 따로 만들어야 해?

A.
단순 변환은 DTO의 from 메서드로 충분하다. 변환 로직이 복잡하거나 여러 Entity를 조합하면 Mapper Component를 검토할 수 있다.

---

# 5. Service와 Repository 조합

## 5.1 Repository 호출 기준

### [개념]

Service는 Repository를 사용해 Entity를 조회, 저장, 삭제한다.

Repository는 데이터 접근만 담당하고, Repository 호출 순서와 비즈니스 판단은 Service가 담당한다.

---

### [핵심]

Service에서 Repository를 사용하는 경우:

- Entity 단건 조회
- Entity 목록 조회
- Entity 존재 여부 확인
- 신규 Entity 저장
- Entity 삭제
- 여러 Entity 조합 조회
- 중복 데이터 검사
- 권한 판단을 위한 데이터 조회

---

### [실무]

단건 조회:

```java
@Transactional(readOnly = true)
public UserResponse getUser(Long userId) {
    User user = userRepository.findById(userId)
            .orElseThrow(() -> new BusinessException("USER_NOT_FOUND", "사용자를 찾을 수 없습니다."));

    return UserResponse.from(user);
}
```

존재 여부 확인:

```java
@Transactional
public UserResponse signUp(SignUpRequest request) {
    if (userRepository.existsByEmail(request.email())) {
        throw new BusinessException("DUPLICATED_EMAIL", "이미 사용 중인 이메일입니다.");
    }

    User user = User.create(request.email(), request.password(), request.nickname());

    return UserResponse.from(userRepository.save(user));
}
```

여러 Repository 조합:

```java
@Transactional
public CommentResponse createComment(Long postId, Long userId, CommentCreateRequest request) {
    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

    User user = userRepository.findById(userId)
            .orElseThrow(() -> new BusinessException("USER_NOT_FOUND", "사용자를 찾을 수 없습니다."));

    Comment comment = Comment.create(post, user, request.content());

    return CommentResponse.from(commentRepository.save(comment));
}
```

---

### [Best Practice]

Repository 호출 Best Practice:

- Optional은 Service에서 처리
- 없으면 CustomException 발생
- existsBy는 중복 / 존재 여부 검사에 사용
- 조회 실패 메시지와 ErrorCode 통일
- 복잡한 query method 이름은 QueryDSL 또는 Custom Repository 검토
- Repository 결과를 Controller까지 그대로 노출하지 않음
- N+1, Lazy Loading 심화 문제는 JPA 문서 기준 참고

---

### [FAQ]

Q. Optional은 어디서 처리해?

A.
Service에서 처리하는 것이 좋다. Repository는 Optional을 반환하고 Service가 없을 때 CustomException을 발생시킨다.

Q. existsBy는 언제 써?

A.
중복 이메일, 이미 좋아요 여부, 이미 찜한 여부처럼 존재 여부만 필요한 경우 사용한다.

Q. Repository 호출이 많아지면 문제야?

A.
Use Case상 필요한 조합은 괜찮지만 Service가 과도하게 복잡해지면 책임 분리나 조회 전용 Query Service 분리를 검토한다.

---

## 5.2 Repository 조합 Anti Pattern

### [개념]

Repository 조합 Anti Pattern은 Service가 Repository를 잘못 사용해 책임이 섞이거나 성능 / 유지보수 문제가 발생하는 구조다.

---

### [핵심]

Anti Pattern:

- Controller에서 Repository 직접 호출
- Repository에 비즈니스 조건문 작성
- Service에서 모든 테이블을 무분별하게 조회
- Optional.get 직접 사용
- 조회 실패 시 null 반환
- Query Method 이름 과도하게 길어짐
- Entity를 그대로 Response로 반환
- 중복 조회 반복
- Transaction 없이 Entity 변경

---

### [실무]

나쁜 예:

```java
public PostResponse getPost(Long postId) {
    Post post = postRepository.findById(postId).get();

    return PostResponse.from(post);
}
```

문제:

- 데이터가 없으면 NoSuchElementException 발생
- 비즈니스 ErrorCode 없음
- 사용자 응답 통제 어려움

좋은 예:

```java
public PostResponse getPost(Long postId) {
    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

    return PostResponse.from(post);
}
```

나쁜 예:

```java
if (postRepository.findById(postId).isEmpty()) {
    return null;
}
```

좋은 예:

```java
Post post = postRepository.findById(postId)
        .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));
```

---

### [Troubleshooting]

문제: 조회 결과가 없을 때 500 Error 발생

```text
원인:
Optional.get 직접 호출

해결:
orElseThrow로 CustomException 발생
GlobalExceptionHandler에서 공통 Error Response 반환
```

문제: Entity 변경이 DB에 반영되지 않음

```text
원인:
Transaction 밖에서 Entity 변경
또는 Entity가 영속 상태가 아님

해결:
Service public method에 @Transactional 적용
Entity 조회 후 Transaction 안에서 상태 변경
```

문제: Service method가 너무 길어짐

```text
원인:
여러 Use Case를 하나의 method에서 처리
조건문 과다
외부 API / DB / 변환 로직 혼합

해결:
Use Case 분리
private method 추출
별도 Component 또는 Domain Service 분리
```

---

### [FAQ]

Q. Optional.get은 왜 피해야 해?

A.
값이 없을 때 예외가 불명확하게 발생하고 API Error Response를 통제하기 어렵기 때문이다.

Q. Service에서 null을 반환해도 돼?

A.
권장하지 않는다. 조회 실패는 CustomException으로 명확히 표현하고 GlobalExceptionHandler에서 처리하는 것이 좋다.

---

# 6. Service 분리 기준

## 6.1 Service가 커지는 문제

### [개념]

Service가 커지는 문제는 하나의 Service가 너무 많은 Use Case와 책임을 담당해 유지보수가 어려워지는 상황이다.

Service는 비즈니스 로직을 담당하지만 모든 로직을 한 클래스에 모아야 한다는 의미는 아니다.

---

### [핵심]

Service가 커지는 신호:

- method 수가 과도하게 많음
- 하나의 method가 너무 김
- 조건문이 반복됨
- 여러 도메인을 동시에 다룸
- 외부 API 호출과 DB 변경이 섞임
- DTO 변환 로직이 과도함
- Transaction 경계가 불명확함
- 테스트 작성이 어려움
- 순환 참조가 발생함

---

### [실무]

분리 전:

```text
UserService
├ signUp
├ login
├ updateProfile
├ changePassword
├ sendEmailVerification
├ resetPassword
├ addFavoriteFestival
├ createNotification
└ callExternalApi
```

분리 후:

```text
UserService
├ signUp
├ updateProfile
└ changePassword

AuthService
├ login
└ refreshToken

EmailVerificationService
├ sendVerification
└ verifyEmail

FavoriteService
├ addFavorite
└ cancelFavorite

NotificationService
├ createNotification
└ getNotifications
```

분리 기준:

- 도메인 기준 분리
- Use Case 기준 분리
- Transaction 경계 기준 분리
- 외부 API 연동 기준 분리
- 조회 전용 Query Service 분리
- Command / Query 분리 가능

---

### [Best Practice]

Service 분리 Best Practice:

- 처음부터 과도하게 쪼개지 않음
- 책임이 커질 때 분리
- Controller 이름과 1:1로 억지 매칭하지 않음
- Repository 이름과 1:1로 억지 매칭하지 않음
- Use Case 흐름이 자연스럽게 보이게 구성
- 순환 참조가 생기면 분리 방향 재검토
- 공통 로직은 별도 Component 검토

---

### [FAQ]

Q. Service는 Entity마다 하나씩 만들어야 해?

A.
반드시 그렇지 않다. Entity 기준보다 Use Case와 도메인 책임 기준으로 나누는 것이 좋다.

Q. Controller 하나에 Service 하나가 정답이야?

A.
아니다. 단순 구조에서는 맞을 수 있지만 실무에서는 기능 책임에 따라 여러 Service를 조합할 수 있다.

Q. Service가 너무 커지면 어떻게 해?

A.
기능별 Service, Query Service, ExternalApiClient, Policy Component, Domain Service 등으로 책임을 나눌 수 있다.

---

## 6.2 Domain Service와 Component 분리

### [개념]

Domain Service 또는 Component는 Service 내부의 반복되거나 독립적인 비즈니스 판단을 분리하기 위한 객체다.

Spring Boot Foundation 단계에서는 Service가 너무 커질 때 선택적으로 사용한다.

---

### [핵심]

분리 대상:

- 반복되는 권한 검사
- 상태 전환 규칙
- 점수 계산
- 알림 생성 규칙
- 외부 API 호출
- 파일 저장 처리
- 결제 승인 처리
- 추천 계산
- 복잡한 DTO 조립

---

### [실무]

Policy Component 예:

```java
@Component
public class PostPermissionChecker {

    public void checkWritable(Post post, Long userId) {
        if (!post.isWriter(userId)) {
            throw new BusinessException("NO_PERMISSION", "게시글 수정 권한이 없습니다.");
        }
    }
}
```

Service에서 사용:

```java
@Transactional
public PostResponse updatePost(Long postId, Long userId, PostUpdateRequest request) {
    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

    postPermissionChecker.checkWritable(post, userId);

    post.update(request.title(), request.content());

    return PostResponse.from(post);
}
```

External API Client 예:

```java
@Component
@RequiredArgsConstructor
public class TourApiClient {

    public TourApiResponse getFestivalInfo(String keyword) {
        ...
    }
}
```

---

### [주의]

분리 시 주의:

- 의미 없는 Component 남용 금지
- 단순 한 줄 로직을 과도하게 분리하지 않음
- Service 흐름이 오히려 이해하기 어려워지면 실패
- Component가 여러 Service를 순환 참조하면 구조 문제
- Transaction 경계는 여전히 Service 중심으로 판단

---

### [FAQ]

Q. Domain Service는 언제 만들어?

A.
Service 내부에 반복되는 도메인 판단이나 여러 Use Case에서 공유되는 규칙이 생길 때 만들 수 있다.

Q. 모든 비즈니스 로직을 Component로 빼야 해?

A.
아니다. 핵심 Use Case 흐름은 Service에 두고 반복되거나 독립적인 규칙만 분리하는 것이 좋다.

---

# 7. Service Transaction 기본 기준

## 7.1 Service와 Transaction

### [개념]

Service Layer는 Transaction Boundary의 대표적인 위치다.

Transaction은 하나의 비즈니스 작업이 모두 성공하거나 모두 실패하도록 보장하는 범위다.

---

### [핵심]

Service에 Transaction을 적용하는 이유:

- 여러 DB 작업을 하나의 작업으로 묶음
- 실패 시 rollback 가능
- Entity 변경 감지 적용
- Lazy Loading 조회 범위 관리
- Use Case 단위 일관성 보장

---

### [실무]

쓰기 작업:

```java
@Transactional
public PostResponse createPost(PostCreateRequest request) {
    Post post = Post.create(request.title(), request.content());
    Post savedPost = postRepository.save(post);

    return PostResponse.from(savedPost);
}
```

읽기 작업:

```java
@Transactional(readOnly = true)
public PostResponse getPost(Long postId) {
    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

    return PostResponse.from(post);
}
```

권장:

- Service public method에 적용
- 쓰기 작업은 `@Transactional`
- 조회 작업은 `@Transactional(readOnly = true)` 고려
- Controller에 Transaction 적용 지양
- Repository에 Use Case Transaction 경계 두지 않음
- 외부 API 호출을 긴 Transaction 안에 두지 않도록 주의

---

### [주의]

Transaction 주의 사항:

- private method의 `@Transactional`은 기대대로 동작하지 않을 수 있음
- 같은 클래스 내부 self-invocation은 Proxy를 거치지 않을 수 있음
- 기본 rollback은 RuntimeException 중심
- Checked Exception rollback은 별도 설정 필요 가능
- readOnly는 쓰기 방지 목적이 아니라 조회 최적화 힌트 성격
- Transaction 안에서 오래 걸리는 외부 API 호출 지양

---

### [FAQ]

Q. @Transactional은 Service에 붙이는 게 좋아?

A.
대부분 Service public method에 붙인다. 비즈니스 Use Case 단위로 Transaction Boundary를 잡기 좋기 때문이다.

Q. 조회만 하는 Service에도 @Transactional이 필요해?

A.
JPA Lazy Loading이나 일관된 읽기 컨텍스트가 필요하면 `readOnly = true`로 적용할 수 있다.

Q. Controller에 @Transactional을 붙이면 안 돼?

A.
권장하지 않는다. HTTP 처리와 비즈니스 Transaction 경계가 섞이기 때문이다.

---

# 8. Service 예외 처리

## 8.1 Service에서 Custom Exception 발생

### [개념]

Service는 비즈니스 규칙 위반이나 조회 실패가 발생했을 때 Custom Exception을 발생시킨다.

GlobalExceptionHandler는 Service에서 발생한 예외를 공통 Error Response로 변환한다.

---

### [핵심]

Service에서 예외를 발생시키는 경우:

- Entity가 존재하지 않음
- 중복 데이터 존재
- 권한 없음
- 잘못된 상태 전환
- 이미 처리된 요청
- 삭제된 데이터 접근
- 재고 부족
- 외부 API 실패
- 비즈니스 조건 위반

---

### [실무]

Custom Exception 사용:

```java
public class BusinessException extends RuntimeException {

    private final String errorCode;

    public BusinessException(String errorCode, String message) {
        super(message);
        this.errorCode = errorCode;
    }

    public String getErrorCode() {
        return errorCode;
    }
}
```

Service 예:

```java
@Transactional(readOnly = true)
public PostResponse getPost(Long postId) {
    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

    if (post.isDeleted()) {
        throw new BusinessException("POST_DELETED", "삭제된 게시글입니다.");
    }

    return PostResponse.from(post);
}
```

권장:

- 비즈니스 의미가 있는 예외는 Custom Exception 사용
- ErrorCode를 명확히 작성
- 사용자 메시지와 로그 메시지 구분
- Controller에서 try-catch 반복 금지
- GlobalExceptionHandler에서 응답 형식 통일

---

### [주의]

나쁜 예:

```java
try {
    return postService.getPost(postId);
} catch (Exception e) {
    return ApiResponse.fail("ERROR", e.getMessage());
}
```

문제:

- Controller마다 예외 처리 중복
- ErrorCode 일관성 없음
- 내부 예외 메시지 노출 위험
- HTTP Status 정책 불명확
- GlobalExceptionHandler 역할 약화

좋은 흐름:

```text
Service에서 BusinessException 발생
→ GlobalExceptionHandler가 예외 처리
→ ApiResponse fail 응답 반환
```

---

### [FAQ]

Q. Service에서 RuntimeException을 그냥 던져도 돼?

A.
가능은 하지만 비즈니스 의미가 있는 오류는 CustomException과 ErrorCode로 명확하게 표현하는 것이 좋다.

Q. Controller에서 try-catch로 감싸면 안 돼?

A.
반복되는 try-catch는 지양한다. 공통 예외 처리는 GlobalExceptionHandler에서 처리하는 것이 좋다.

---

# 9. Service Layer Testing Readiness

## 9.1 테스트 가능한 Service 구조

### [개념]

테스트 가능한 Service 구조는 Service가 외부 의존성을 명확히 주입받고, Controller나 Framework 세부사항에 과도하게 의존하지 않는 구조다.

---

### [핵심]

테스트하기 좋은 Service 조건:

- Constructor Injection 사용
- final field 사용
- Repository 의존성 명확
- HTTP 객체 의존 최소화
- 비즈니스 로직이 Service에 위치
- 예외 조건이 명확
- method 입력 / 출력이 명확
- 외부 API는 Client Component로 분리
- Transaction 경계가 public method에 있음

---

### [실무]

테스트하기 쉬운 Service:

```java
@Service
@RequiredArgsConstructor
public class UserService {

    private final UserRepository userRepository;

    public UserResponse getUser(Long userId) {
        User user = userRepository.findById(userId)
                .orElseThrow(() -> new BusinessException("USER_NOT_FOUND", "사용자를 찾을 수 없습니다."));

        return UserResponse.from(user);
    }
}
```

테스트하기 어려운 Service:

```java
@Service
public class UserService {

    @Autowired
    private UserRepository userRepository;

    public UserResponse getUser(HttpServletRequest request) {
        Long userId = Long.valueOf(request.getParameter("userId"));
        ...
    }
}
```

문제:

- Field Injection으로 의존성 숨겨짐
- HTTP 객체에 직접 의존
- Controller 책임과 Service 책임 혼합
- Unit Test 작성 어려움

---

### [Checklist]

Service 테스트 준비 체크리스트:

```md
- [ ] 생성자 주입을 사용하는가?
- [ ] 의존성이 final field로 명확한가?
- [ ] Controller 객체에 직접 의존하지 않는가?
- [ ] Request / Response DTO 경계가 명확한가?
- [ ] Repository 조회 실패 시 CustomException을 던지는가?
- [ ] Business Validation이 Service에 있는가?
- [ ] Entity 상태 변경이 Transaction 안에서 수행되는가?
- [ ] 외부 API 호출이 별도 Component로 분리 가능한가?
- [ ] method 이름이 Use Case를 표현하는가?
- [ ] 하나의 method가 너무 많은 책임을 갖지 않는가?
```

---

### [FAQ]

Q. Service 테스트가 어려우면 구조가 잘못된 거야?

A.
항상 그런 것은 아니지만 Service가 HTTP 객체, 외부 API, DB, 변환 로직에 과도하게 결합되어 있으면 구조 개선 신호일 수 있다.

Q. 생성자 주입이 테스트에 좋은 이유는?

A.
테스트에서 필요한 의존성을 명확히 주입할 수 있고 필수 의존성 누락을 빠르게 확인할 수 있기 때문이다.

---

# 10. Service Layer Anti Pattern

## 10.1 Common Anti Pattern

### [개념]

Service Layer Anti Pattern은 Service가 책임을 잘못 가지거나 다른 Layer와 역할이 섞이는 구조다.

이런 구조는 유지보수, 테스트, 예외 처리, Transaction 관리에 문제를 만든다.

---

### [핵심]

자주 발생하는 Anti Pattern:

- Controller에서 Repository 직접 호출
- Controller에 비즈니스 로직 작성
- Service가 HTTP Request 객체에 직접 의존
- Service가 Entity를 그대로 외부에 반환
- Service에서 null 반환
- Optional.get 직접 호출
- Field Injection 사용
- Transaction 없이 Entity 변경
- 하나의 Service에 모든 기능 집중
- Service 간 순환 참조
- 외부 API 호출과 DB 변경을 긴 Transaction으로 묶음
- ErrorCode 없이 RuntimeException만 던짐
- DTO와 Entity 변환 기준 없음
- method 이름이 process / handle뿐임

---

### [실무]

Anti Pattern 예:

```java
@RestController
@RequiredArgsConstructor
public class PostController {

    private final PostRepository postRepository;

    @PostMapping("/posts")
    public Post createPost(@RequestBody PostCreateRequest request) {
        Post post = new Post(request.title(), request.content());
        return postRepository.save(post);
    }
}
```

문제:

- Controller가 Repository 직접 호출
- Controller에 Entity 생성 로직 존재
- Entity 직접 반환
- Transaction Boundary 불명확
- Validation 없음
- Exception Handling 기준 없음

개선:

```java
@RestController
@RequiredArgsConstructor
public class PostController {

    private final PostService postService;

    @PostMapping("/posts")
    public ApiResponse<PostResponse> createPost(
            @Valid @RequestBody PostCreateRequest request
    ) {
        return ApiResponse.success(postService.createPost(request));
    }
}
```

```java
@Service
@RequiredArgsConstructor
public class PostService {

    private final PostRepository postRepository;

    @Transactional
    public PostResponse createPost(PostCreateRequest request) {
        Post post = Post.create(request.title(), request.content());
        Post savedPost = postRepository.save(post);

        return PostResponse.from(savedPost);
    }
}
```

---

### [Troubleshooting]

문제: Controller 코드가 너무 길다

```text
원인:
Business Logic이 Controller에 있음

해결:
Use Case를 Service method로 이동
Controller는 Request 수신, Validation Trigger, Service 호출, Response 반환만 담당
```

문제: Service 간 순환 참조 발생

```text
원인:
AService가 BService를 호출하고 BService가 다시 AService를 호출

해결:
책임 재분리
공통 로직 Component 분리
도메인 이벤트 또는 별도 조율 Service 검토
```

문제: Service가 너무 많은 일을 한다

```text
원인:
회원, 인증, 알림, 외부 API, 파일 처리 등 여러 책임이 하나의 Service에 집중

해결:
Use Case 기준 Service 분리
ExternalApiClient 분리
NotificationService 분리
Query Service 분리
```

---

### [FAQ]

Q. Service Anti Pattern 중 가장 위험한 건 뭐야?

A.
Controller가 Repository를 직접 호출하고 Entity를 그대로 반환하는 구조가 흔하면서도 위험하다. Layer 책임, DTO 경계, Transaction 기준이 모두 흐려진다.

Q. Service가 HTTP Request를 직접 받으면 왜 안 좋아?

A.
Service가 Web Layer에 강하게 결합되어 테스트가 어려워지고 재사용성이 떨어진다.

Q. Service 간 순환 참조는 어떻게 해결해?

A.
공통 로직을 별도 Component로 분리하거나 Service 책임을 다시 나누는 것이 좋다.

---

# 11. Service Layer Checklist

## 11.1 Service Layer Review Checklist

### [개념]

Service Layer Checklist는 Backend Agent가 Spring Boot Service 코드를 생성하거나 검수할 때 사용하는 기준이다.

---

### [핵심]

검수 항목:

```md
- [ ] Service class에 @Service가 있는가?
- [ ] 생성자 주입을 사용하는가?
- [ ] 의존성이 final field로 선언되어 있는가?
- [ ] Controller가 Repository를 직접 호출하지 않는가?
- [ ] Controller에 Business Logic이 없는가?
- [ ] Service method 이름이 Use Case를 표현하는가?
- [ ] Repository 조회 실패를 CustomException으로 처리하는가?
- [ ] Optional.get을 직접 사용하지 않는가?
- [ ] null 반환을 피하는가?
- [ ] 쓰기 작업에 @Transactional이 적용되어 있는가?
- [ ] 조회 작업에 readOnly = true를 고려했는가?
- [ ] Entity 직접 반환을 피하고 Response DTO를 사용하는가?
- [ ] Entity 변경은 의미 있는 method로 수행하는가?
- [ ] Validation과 Business Validation을 구분했는가?
- [ ] ErrorCode가 명확한가?
- [ ] Service가 HTTP 객체에 직접 의존하지 않는가?
- [ ] 외부 API 호출이 필요하면 별도 Client 분리를 고려했는가?
- [ ] Service method가 너무 길지 않은가?
- [ ] Service 간 순환 참조가 없는가?
- [ ] 테스트 가능한 구조인가?
```

---

### [실무]

검수 흐름:

```text
Controller 확인
→ Service 호출 구조 확인
→ Service method 책임 확인
→ Repository 호출 위치 확인
→ Transaction 확인
→ Business Validation 확인
→ Custom Exception 확인
→ DTO 변환 확인
→ Anti Pattern 확인
→ 테스트 가능성 확인
```

---

### [FAQ]

Q. Service Layer 검수에서 가장 먼저 볼 것은?

A.
Controller가 Repository를 직접 호출하지 않고 Service를 통해 Use Case를 처리하는지 먼저 확인한다.

Q. Service 코드 품질의 핵심 기준은?

A.
책임 분리, Transaction Boundary, Business Logic 위치, Custom Exception, DTO 변환, 테스트 가능성이다.

---

# Retrieval Queries

### [FAQ]

Q. Spring Boot Service Layer는 뭐야?
A. Controller와 Repository 사이에서 Business Logic, Transaction Boundary, Repository 조합, Entity 변경, 예외 처리를 담당하는 계층이다.

Q. Service Layer는 왜 필요해?
A. Controller에서 비즈니스 로직을 분리하고 Use Case 단위로 Transaction과 Repository 호출을 관리하기 위해 필요하다.

Q. Controller에서 Repository를 바로 호출해도 돼?
A. 실무 구조에서는 권장하지 않는다. Service를 거쳐 비즈니스 로직과 Transaction Boundary를 관리하는 것이 좋다.

Q. Service에는 어떤 로직을 넣어?
A. 비즈니스 규칙, Repository 조합, Entity 조회 / 생성 / 변경, CustomException 발생, DTO 변환 조율을 넣는다.

Q. Service가 담당하지 말아야 하는 것은?
A. HTTP URL Mapping, Request Binding, JSON 변환, DB Query 세부 구현, 화면 표시 같은 책임은 담당하지 않는 것이 좋다.

Q. Service method 이름은 어떻게 짓는 게 좋아?
A. createPost, updateUser, addFavorite처럼 Use Case와 기능 의도가 드러나는 이름이 좋다.

Q. process나 handle 같은 Service method 이름은 왜 안 좋아?
A. 무엇을 처리하는지 알기 어렵고 여러 책임이 섞여도 이름에서 드러나지 않기 때문이다.

Q. Business Logic은 어디에 넣어?
A. 대부분 Service Layer에 넣고 Entity 자신의 상태 변경 규칙은 Entity method로 분리할 수 있다.

Q. Validation과 Business Validation 차이는?
A. Validation은 입력 형식 검증이고 Business Validation은 중복, 권한, 상태 전환 같은 업무 규칙 검증이다.

Q. 중복 이메일 검사는 어디서 해?
A. Repository 조회가 필요한 Business Validation이므로 Service에서 처리하는 것이 좋다.

Q. Service에서 Entity를 변경해도 돼?
A. 가능하다. Service가 Entity를 조회하고 권한 / 상태를 확인한 뒤 Entity method를 호출해 변경하는 구조가 좋다.

Q. Entity setter를 열어도 돼?
A. 가능은 하지만 무분별한 setter보다 update, markDeleted, completePayment 같은 의미 있는 method를 권장한다.

Q. DTO 변환은 어디서 해?
A. 팀 규칙에 따라 Service 또는 DTO static factory에서 처리할 수 있다. Entity 직접 반환은 지양한다.

Q. Service에서 Response DTO를 반환해도 돼?
A. 가능하다. Controller Thin Rule을 유지하기 위해 Service가 Response DTO를 반환하는 구조도 많이 사용된다.

Q. Optional은 어디서 처리해?
A. Repository는 Optional을 반환하고 Service에서 orElseThrow로 CustomException을 발생시키는 것이 좋다.

Q. Optional.get을 직접 쓰면 왜 안 좋아?
A. 값이 없을 때 예외가 불명확하게 발생하고 API Error Response를 통제하기 어렵기 때문이다.

Q. Service에서 null을 반환해도 돼?
A. 권장하지 않는다. 조회 실패나 비즈니스 오류는 CustomException으로 명확히 표현하는 것이 좋다.

Q. existsBy는 언제 써?
A. 중복 이메일, 이미 좋아요 여부, 이미 찜한 여부처럼 존재 여부만 필요한 경우 사용한다.

Q. Service가 너무 커지면 어떻게 해?
A. 기능별 Service, Query Service, ExternalApiClient, Policy Component, Domain Service 등으로 책임을 나눌 수 있다.

Q. Service는 Entity마다 하나씩 만들어야 해?
A. 반드시 그렇지 않다. Entity 기준보다 Use Case와 도메인 책임 기준으로 나누는 것이 좋다.

Q. Controller 하나에 Service 하나가 정답이야?
A. 아니다. 단순 구조에서는 가능하지만 실무에서는 기능 책임에 따라 여러 Service를 조합할 수 있다.

Q. Domain Service는 언제 만들어?
A. 반복되는 도메인 판단이나 여러 Use Case에서 공유되는 규칙이 생길 때 만들 수 있다.

Q. 모든 비즈니스 로직을 Component로 빼야 해?
A. 아니다. 핵심 Use Case 흐름은 Service에 두고 반복되거나 독립적인 규칙만 분리하는 것이 좋다.

Q. @Transactional은 어디에 붙여?
A. 대부분 Service public method에 붙인다. 비즈니스 Use Case 단위로 Transaction Boundary를 잡기 좋기 때문이다.

Q. 쓰기 Service에는 @Transactional이 필요해?
A. Entity 저장, 수정, 삭제처럼 DB 상태를 변경하는 작업에는 @Transactional을 적용하는 것이 좋다.

Q. 조회 Service에도 @Transactional이 필요해?
A. JPA Lazy Loading이나 일관된 읽기 컨텍스트가 필요하면 @Transactional(readOnly = true)를 적용할 수 있다.

Q. Controller에 @Transactional을 붙이면 안 돼?
A. 권장하지 않는다. HTTP 처리와 비즈니스 Transaction Boundary가 섞이기 때문이다.

Q. Service에서 CustomException은 언제 던져?
A. Entity 없음, 중복 데이터, 권한 없음, 잘못된 상태, 이미 처리된 요청 같은 비즈니스 오류에 사용한다.

Q. Controller에서 try-catch로 Service 예외를 잡아야 해?
A. 반복 try-catch는 지양하고 GlobalExceptionHandler에서 공통 처리하는 것이 좋다.

Q. Service 테스트가 어려우면 무엇을 확인해?
A. 생성자 주입 여부, HTTP 객체 의존 여부, 외부 API 분리 여부, Business Logic 위치, method 책임 크기를 확인한다.

Q. Service Anti Pattern은 뭐가 있어?
A. Controller에서 Repository 직접 호출, Entity 직접 반환, Optional.get 사용, null 반환, Field Injection, Transaction 없는 Entity 변경 등이 있다.

Q. Service가 HTTP Request를 직접 받으면 왜 안 좋아?
A. Service가 Web Layer에 강하게 결합되어 테스트가 어려워지고 재사용성이 떨어진다.

Q. Service 간 순환 참조는 어떻게 해결해?
A. 공통 로직을 별도 Component로 분리하거나 Service 책임을 다시 나누는 것이 좋다.

Q. Service Layer 검수 핵심은?
A. 책임 분리, Business Logic 위치, Transaction Boundary, Repository 조합, CustomException, DTO 변환, 테스트 가능성이다.
