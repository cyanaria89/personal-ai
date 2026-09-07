# Spring Boot Part03 - DTO & ApiResponse

---

# 1. DTO Overview

## 1.1 DTO Purpose

### [개념]

DTO는 Data Transfer Object의 약자다.

Spring Boot Application에서 DTO는 Client와 Server 사이의 Request / Response 데이터를 전달하는 객체다.

DTO는 Entity를 외부 API에 직접 노출하지 않기 위한 API Boundary 객체다.

DTO의 목적:

- API 입력 구조 정의
- API 응답 구조 정의
- Entity 직접 노출 방지
- 민감정보 노출 방지
- Request Validation 적용
- Frontend 연동 안정화
- API Spec 변경 영향 최소화
- Backend Agent 코드 생성 기준 제공
- Review Agent 구조 검수 기준 제공

---

### [핵심]

DTO 핵심 키워드:

- DTO
- Request DTO
- Response DTO
- API Boundary
- Entity Separation
- Validation
- Binding
- Serialization
- Deserialization
- ApiResponse
- Response Convention
- Frontend Contract

DTO 기본 분류:

| DTO 종류     | 목적                    | 예                  |
| ------------ | ----------------------- | ------------------- |
| Request DTO  | Client 요청 데이터 수신 | `PostCreateRequest` |
| Response DTO | Server 응답 데이터 반환 | `PostResponse`      |
| Search DTO   | 검색 조건 수신          | `PostSearchRequest` |
| Update DTO   | 수정 요청 수신          | `PostUpdateRequest` |
| Error DTO    | 실패 응답 구조          | `ErrorResponse`     |

핵심 규칙:

- Entity를 RequestBody로 직접 받지 않는다.
- Entity를 Response로 직접 반환하지 않는다.
- Request DTO와 Response DTO를 분리한다.
- API Use Case별 DTO를 만든다.
- DTO에는 필요한 필드만 포함한다.
- 민감정보는 Response DTO에 포함하지 않는다.
- Request DTO에는 Validation Annotation을 적용한다.
- Response DTO는 Entity를 안전하게 변환한다.

---

### [실무]

기본 요청 흐름:

```text
Client JSON Request
→ Request DTO
→ Controller
→ Service
→ Entity
→ Repository
```

기본 응답 흐름:

```text
Repository
→ Entity
→ Service
→ Response DTO
→ Controller
→ ApiResponse
→ Client JSON Response
```

Request DTO 예:

```java
public record PostCreateRequest(
        @NotBlank String title,
        @NotBlank String content
) {
}
```

Response DTO 예:

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

Controller 예:

```java
@PostMapping
public ApiResponse<PostResponse> createPost(
        @Valid @RequestBody PostCreateRequest request
) {
    PostResponse response = postService.createPost(request);
    return ApiResponse.success(response);
}
```

권장:

- Java 17+ 기준 DTO는 record 사용을 검토한다.
- Request DTO는 API 입력 전용으로 둔다.
- Response DTO는 Frontend가 필요한 필드만 포함한다.
- Entity → DTO 변환은 `from` 또는 `of` 정적 팩토리 메서드로 통일할 수 있다.
- 생성 / 수정 / 검색 DTO를 무리하게 하나로 합치지 않는다.
- 비밀번호, 토큰, 내부 상태 값은 Response DTO에 포함하지 않는다.

---

### [FAQ]

Q. DTO는 왜 필요해?
A. Entity를 외부에 직접 노출하지 않고 API 요청 / 응답 구조를 안정적으로 관리하기 위해 필요하다.

Q. Entity를 DTO 대신 써도 돼?
A. 권장하지 않는다. API 구조와 DB 구조가 강하게 결합되고 민감정보 노출 위험이 생긴다.

Q. Request DTO와 Response DTO는 분리해야 해?
A. 요청과 응답의 필드, 검증 기준, 노출 기준이 다르면 분리하는 것이 좋다.

Q. DTO는 record로 만들어도 돼?
A. Java 17+와 Spring Boot 3.x 기준에서는 불변 DTO를 만들기 위해 record를 사용할 수 있다.

---

# 2. Request DTO

## 2.1 Request DTO Rules

### [개념]

Request DTO는 Client가 Server로 보내는 요청 데이터를 표현하는 객체다.

Request DTO는 Controller에서 `@RequestBody`, `@ModelAttribute`, `@RequestParam` 조합을 통해 수신된다.

Request DTO는 API 입력 구조와 Validation 기준을 정의한다.

---

### [핵심]

Request DTO 목적:

- API 입력 필드 정의
- Request Body Binding
- Query Parameter Binding
- Validation 적용
- Entity 직접 수신 방지
- Client 입력 값 제한
- Use Case별 요청 구조 분리

Request DTO 핵심 규칙:

- Entity를 Request DTO로 사용하지 않는다.
- Request DTO에 Entity의 모든 필드를 넣지 않는다.
- 필요한 입력 필드만 포함한다.
- 생성 DTO와 수정 DTO를 분리한다.
- 검색 조건은 SearchRequest DTO로 분리할 수 있다.
- DTO 필드명은 JSON 필드명과 일치시킨다.
- Request DTO에는 기본 형식 검증 Annotation을 적용한다.
- 비즈니스 검증은 Service에서 처리한다.

---

### [실무]

생성 Request DTO:

```java
public record UserCreateRequest(
        @Email String email,
        @NotBlank String password,
        @NotBlank String nickname
) {
}
```

수정 Request DTO:

```java
public record UserUpdateRequest(
        @NotBlank String nickname
) {
}
```

검색 Request DTO:

```java
public record PostSearchRequest(
        String keyword,
        String category,
        LocalDate startDate,
        LocalDate endDate
) {
}
```

Controller 사용:

```java
@PostMapping("/users")
public ApiResponse<UserResponse> createUser(
        @Valid @RequestBody UserCreateRequest request
) {
    return ApiResponse.success(userService.createUser(request));
}
```

검색 Controller 사용:

```java
@GetMapping("/posts/search")
public ApiResponse<Slice<PostResponse>> searchPosts(
        @ModelAttribute PostSearchRequest request,
        Pageable pageable
) {
    return ApiResponse.success(postService.searchPosts(request, pageable));
}
```

비권장:

```java
@PostMapping("/users")
public ApiResponse<UserResponse> createUser(
        @RequestBody User user
) {
    return ApiResponse.success(userService.createUser(user));
}
```

문제:

- Entity와 API 입력 구조 강결합
- password, role, status 등 민감 필드 조작 위험
- Validation 기준 불명확
- API 변경 시 Entity 영향
- Entity 변경 시 API 영향

---

### [FAQ]

Q. Request DTO는 뭐야?
A. Client가 Server로 보내는 요청 데이터를 표현하는 API 입력 객체다.

Q. Entity를 RequestBody로 받아도 돼?
A. 권장하지 않는다. Request DTO를 따로 만들어 API 입력 구조를 분리하는 것이 좋다.

Q. 생성 DTO와 수정 DTO는 분리해야 해?
A. 필드와 검증 조건이 다르면 분리하는 것이 좋다.

Q. 검색 조건도 DTO로 만들 수 있어?
A. 가능하다. 조건이 많으면 `@ModelAttribute`와 SearchRequest DTO를 사용하는 것이 좋다.

---

## 2.2 Request DTO Validation Rules

### [개념]

Request DTO Validation은 Client 요청 값이 기본 형식과 제약 조건을 만족하는지 확인하는 규칙이다.

Spring Boot에서는 Bean Validation Annotation과 Controller의 `@Valid`를 함께 사용한다.

Request DTO는 형식 검증을 담당하고, 비즈니스 검증은 Service에서 담당한다.

---

### [핵심]

주요 Validation Annotation:

- `@NotNull`
- `@NotBlank`
- `@NotEmpty`
- `@Size`
- `@Email`
- `@Pattern`
- `@Min`
- `@Max`
- `@Positive`
- `@PositiveOrZero`
- `@Past`
- `@Future`
- `@FutureOrPresent`

Request DTO 예:

```java
public record SignUpRequest(
        @Email String email,
        @NotBlank String password,
        @Size(min = 2, max = 20) String nickname
) {
}
```

Controller Trigger:

```java
@PostMapping("/signup")
public ApiResponse<UserResponse> signUp(
        @Valid @RequestBody SignUpRequest request
) {
    return ApiResponse.success(userService.signUp(request));
}
```

핵심 규칙:

- DTO 필드에 Validation Annotation을 붙인다.
- Controller Parameter에 `@Valid`를 붙인다.
- 형식 검증과 비즈니스 검증을 분리한다.
- Validation 실패는 GlobalExceptionHandler에서 처리한다.
- Validation 메시지는 사용자 노출 가능성을 고려한다.

---

### [실무]

Validation 대상 구분:

| 검증 종류     | 위치               | 예                           |
| ------------- | ------------------ | ---------------------------- |
| 형식 검증     | Request DTO        | 이메일 형식, 빈 값, 길이     |
| 타입 검증     | Binding 단계       | Long 변환, LocalDate 변환    |
| 비즈니스 검증 | Service            | 이메일 중복, 권한, 상태 전환 |
| 보안 검증     | Security / Service | 인증 사용자 권한, Role       |

DTO:

```java
public record ProductCreateRequest(
        @NotBlank String name,
        @Positive Integer price,
        @PositiveOrZero Integer stock
) {
}
```

Service 비즈니스 검증:

```java
@Transactional
public ProductResponse createProduct(ProductCreateRequest request) {
    if (productRepository.existsByName(request.name())) {
        throw new BusinessException(ErrorCode.PRODUCT_NAME_DUPLICATED);
    }

    Product product = Product.create(
            request.name(),
            request.price(),
            request.stock()
    );

    return ProductResponse.from(productRepository.save(product));
}
```

주의:

```java
public record UserCreateRequest(
        @NotBlank String email
) {
}
```

문제:

```text
email 필드가 빈 값은 막지만 이메일 형식은 검증하지 않음
```

개선:

```java
public record UserCreateRequest(
        @Email String email
) {
}
```

더 안전한 개선:

```java
public record UserCreateRequest(
        @NotBlank
        @Email
        String email
) {
}
```

---

### [FAQ]

Q. Request DTO에 Validation Annotation을 붙이면 바로 동작해?
A. Controller Parameter에 `@Valid`를 붙여야 검증이 실행된다.

Q. `@NotNull`, `@NotBlank`, `@NotEmpty` 차이는?
A. `@NotNull`은 null만 금지하고, `@NotBlank`는 공백 문자열을 금지하며, `@NotEmpty`는 null과 빈 값을 금지한다.

Q. 이메일 검증은 뭘 써?
A. `@Email`을 사용하고 빈 값도 막아야 하면 `@NotBlank`를 함께 사용한다.

Q. 중복 이메일 검증도 DTO에서 해?
A. 아니다. 중복 이메일 같은 비즈니스 검증은 Service에서 Repository를 통해 확인한다.

---

## 2.3 Request DTO Naming Rules

### [개념]

Request DTO Naming은 API 입력 객체의 목적과 Use Case를 이름으로 명확히 표현하는 규칙이다.

DTO 이름이 명확하면 Backend Agent와 Review Agent가 DTO 용도를 쉽게 판단할 수 있다.

---

### [핵심]

권장 Naming Pattern:

```text
{Resource}{Action}Request
```

예:

- `UserCreateRequest`
- `UserUpdateRequest`
- `UserLoginRequest`
- `PostCreateRequest`
- `PostUpdateRequest`
- `PostSearchRequest`
- `CommentCreateRequest`
- `PasswordResetRequest`

비권장:

- `UserDto`
- `PostDto`
- `RequestDto`
- `DataDto`
- `UserRequestResponse`
- `UserSaveDto`
- `ParamDto`

핵심 규칙:

- DTO 이름에 목적을 포함한다.
- Request와 Response를 이름으로 구분한다.
- Create / Update / Search / Login 등 Use Case를 포함한다.
- 단일 `UserDto`로 모든 요청 / 응답을 처리하지 않는다.
- 약어를 남용하지 않는다.
- 프로젝트 전체 Naming 규칙을 통일한다.

---

### [실무]

좋은 예:

```java
public record PostCreateRequest(
        String title,
        String content
) {
}
```

```java
public record PostUpdateRequest(
        String title,
        String content
) {
}
```

```java
public record PostSearchRequest(
        String keyword,
        String category
) {
}
```

나쁜 예:

```java
public record PostDto(
        Long id,
        String title,
        String content,
        String password,
        String createdAt
) {
}
```

문제:

- Request인지 Response인지 불명확
- 생성 / 수정 / 조회 용도 불명확
- 민감 필드 포함 가능
- Validation 기준 불명확
- API 응답 구조 불안정

권장 패키지 구조:

```text
dto
├ request
│ ├ UserCreateRequest.java
│ ├ UserUpdateRequest.java
│ └ UserLoginRequest.java
└ response
  ├ UserResponse.java
  └ LoginResponse.java
```

도메인별 DTO 구조:

```text
domain
└ user
  └ dto
    ├ request
    │ ├ UserCreateRequest.java
    │ └ UserUpdateRequest.java
    └ response
      └ UserResponse.java
```

---

### [FAQ]

Q. DTO 이름은 어떻게 짓는 게 좋아?
A. `UserCreateRequest`, `UserResponse`처럼 Resource, Action, Request / Response가 드러나게 짓는 것이 좋다.

Q. `UserDto` 하나로 다 처리하면 안 돼?
A. 권장하지 않는다. 요청과 응답의 필드, 검증 기준, 노출 기준이 달라질 수 있다.

Q. Search 조건 DTO 이름은 어떻게 지어?
A. `PostSearchRequest`, `FestivalSearchRequest`처럼 검색 대상 Resource와 SearchRequest를 붙이는 것이 좋다.

Q. DTO 패키지는 request / response로 나눠?
A. Request DTO와 Response DTO를 분리하면 구조와 역할이 명확해진다.

---

# 3. Response DTO

## 3.1 Response DTO Rules

### [개념]

Response DTO는 Server가 Client에게 반환하는 응답 데이터를 표현하는 객체다.

Response DTO는 Entity를 직접 노출하지 않고 필요한 데이터만 안전하게 전달한다.

Response DTO는 Frontend와의 API Contract 역할을 한다.

---

### [핵심]

Response DTO 목적:

- 응답 필드 통제
- Entity 직접 노출 방지
- 민감정보 제거
- API 응답 구조 안정화
- Frontend 연동 안정성 확보
- Lazy Loading 문제 완화
- 순환 참조 방지
- 날짜 / 상태 값 표현 통일

Response DTO 핵심 규칙:

- Entity를 그대로 반환하지 않는다.
- 필요한 필드만 포함한다.
- 민감정보를 제외한다.
- Response DTO 이름은 명확히 작성한다.
- Entity → DTO 변환 규칙을 통일한다.
- 날짜 포맷 기준을 통일한다.
- enum 노출 방식은 프로젝트 규칙으로 정한다.
- 연관 객체는 필요한 깊이만 포함한다.

---

### [실무]

Entity:

```java
@Entity
public class User {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String email;
    private String password;
    private String nickname;
    private String role;
}
```

Response DTO:

```java
public record UserResponse(
        Long userId,
        String email,
        String nickname
) {
    public static UserResponse from(User user) {
        return new UserResponse(
                user.getId(),
                user.getEmail(),
                user.getNickname()
        );
    }
}
```

Controller:

```java
@GetMapping("/{userId}")
public ApiResponse<UserResponse> getUser(
        @PathVariable Long userId
) {
    return ApiResponse.success(userService.getUser(userId));
}
```

비권장:

```java
@GetMapping("/{userId}")
public User getUser(@PathVariable Long userId) {
    return userRepository.findById(userId).orElseThrow();
}
```

문제:

- password 노출 위험
- role 같은 내부 권한 정보 노출 가능
- Lazy Loading 오류 가능
- 순환 참조 가능
- API 응답 구조가 Entity 변경에 따라 흔들림

---

### [FAQ]

Q. Response DTO는 뭐야?
A. Server가 Client에게 반환할 응답 데이터를 표현하는 API 출력 객체다.

Q. Entity를 그대로 Response로 반환해도 돼?
A. 권장하지 않는다. 민감정보 노출, Lazy Loading 문제, 순환 참조, API 변경 위험이 생길 수 있다.

Q. Response DTO에는 어떤 필드를 넣어?
A. Frontend가 필요한 필드만 넣고 비밀번호, 내부 상태, 민감정보는 제외한다.

Q. Response DTO는 어디서 만들어?
A. DTO의 static `from` 메서드나 Service에서 만들 수 있으며 팀 규칙으로 일관화하는 것이 중요하다.

---

## 3.2 Response DTO Conversion Rules

### [개념]

Response DTO Conversion은 Entity 또는 Domain Result를 API Response DTO로 변환하는 규칙이다.

변환 기준을 통일하면 코드 생성, 리뷰, 유지보수가 쉬워진다.

---

### [핵심]

변환 방식:

- DTO static `from`
- DTO static `of`
- Service 내부 변환
- Mapper Component
- Projection
- Query DTO

기본 권장:

```text
Entity
→ Response DTO
→ ApiResponse
```

`from` 사용 기준:

```java
public static UserResponse from(User user) {
    return new UserResponse(
            user.getId(),
            user.getEmail(),
            user.getNickname()
    );
}
```

`of` 사용 기준:

```java
public static UserSummaryResponse of(Long userId, String nickname) {
    return new UserSummaryResponse(userId, nickname);
}
```

핵심 규칙:

- 단일 Entity 변환은 `from`을 사용할 수 있다.
- 여러 값 조합은 `of`를 사용할 수 있다.
- 복잡한 변환은 Mapper Component를 검토한다.
- Entity 내부에 DTO 변환 로직을 넣지 않는다.
- Controller에서 복잡한 변환을 수행하지 않는다.

---

### [실무]

단건 변환:

```java
public record PostResponse(
        Long postId,
        String title,
        String content,
        String writerName
) {
    public static PostResponse from(Post post) {
        return new PostResponse(
                post.getId(),
                post.getTitle(),
                post.getContent(),
                post.getWriter().getNickname()
        );
    }
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

Slice 변환:

```java
@Transactional(readOnly = true)
public Slice<PostResponse> getPosts(Pageable pageable) {
    return postRepository.findAll(pageable)
            .map(PostResponse::from);
}
```

Mapper Component 검토 상황:

```text
변환 로직이 복잡함
→ 여러 Entity 조합 필요
→ 외부 API 응답 조합 필요
→ 조건별 필드 변환 필요
→ Mapper Component 검토
```

Mapper 예:

```java
@Component
public class PostMapper {

    public PostResponse toResponse(Post post) {
        return new PostResponse(
                post.getId(),
                post.getTitle(),
                post.getContent()
        );
    }
}
```

주의:

```java
@Entity
public class Post {

    public PostResponse toResponse() {
        return new PostResponse(id, title, content);
    }
}
```

비권장 이유:

- Entity가 API 응답 구조를 알게 됨
- Domain / Persistence Model이 API Layer에 의존함
- API 변경이 Entity에 영향을 줌

---

### [FAQ]

Q. DTO 변환은 어디서 해?
A. 간단한 변환은 DTO의 static `from` 메서드나 Service에서 처리할 수 있다.

Q. `from`과 `of` 차이는?
A. `from`은 Entity나 객체 하나에서 변환할 때, `of`는 여러 값을 조합해 생성할 때 자주 사용한다.

Q. Entity 안에 `toResponse()`를 만들어도 돼?
A. 권장하지 않는다. Entity가 API 응답 구조를 알게 되어 Layer 의존 방향이 흐려진다.

Q. 변환 로직이 복잡하면 어떻게 해?
A. Mapper Component를 만들어 변환 책임을 분리할 수 있다.

---

## 3.3 Response DTO Naming Rules

### [개념]

Response DTO Naming은 API 응답 객체의 목적과 범위를 이름으로 명확히 표현하는 규칙이다.

Response DTO 이름은 Frontend Contract와 Retrieval Matching에 중요하다.

---

### [핵심]

권장 Naming Pattern:

```text
{Resource}Response
{Resource}DetailResponse
{Resource}SummaryResponse
{Resource}ListResponse
{Action}Response
```

예:

- `UserResponse`
- `UserDetailResponse`
- `UserSummaryResponse`
- `PostResponse`
- `PostDetailResponse`
- `PostListResponse`
- `LoginResponse`
- `TokenResponse`
- `FestivalResponse`
- `NotificationResponse`

비권장:

- `UserDto`
- `UserResDto`
- `DataResponse`
- `ResultDto`
- `CommonDto`
- `PostRequestResponse`
- `ResponseData`

핵심 규칙:

- Response 목적을 이름에 포함한다.
- 상세 응답과 요약 응답을 구분한다.
- 로그인 / 토큰 응답처럼 Action 기반 이름도 가능하다.
- Request DTO와 이름이 겹치지 않게 한다.
- 축약어를 과도하게 사용하지 않는다.
- 프로젝트 전체 Naming 규칙을 통일한다.

---

### [실무]

요약 응답:

```java
public record PostSummaryResponse(
        Long postId,
        String title,
        String writerName
) {
    public static PostSummaryResponse from(Post post) {
        return new PostSummaryResponse(
                post.getId(),
                post.getTitle(),
                post.getWriter().getNickname()
        );
    }
}
```

상세 응답:

```java
public record PostDetailResponse(
        Long postId,
        String title,
        String content,
        String writerName,
        LocalDateTime createdAt
) {
    public static PostDetailResponse from(Post post) {
        return new PostDetailResponse(
                post.getId(),
                post.getTitle(),
                post.getContent(),
                post.getWriter().getNickname(),
                post.getCreatedAt()
        );
    }
}
```

로그인 응답:

```java
public record LoginResponse(
        String accessToken,
        String refreshToken,
        String tokenType
) {
}
```

목록 조회:

```java
@GetMapping
public ApiResponse<Slice<PostSummaryResponse>> getPosts(Pageable pageable) {
    return ApiResponse.success(postService.getPosts(pageable));
}
```

상세 조회:

```java
@GetMapping("/{postId}")
public ApiResponse<PostDetailResponse> getPost(
        @PathVariable Long postId
) {
    return ApiResponse.success(postService.getPost(postId));
}
```

---

### [FAQ]

Q. Response DTO 이름은 어떻게 짓는 게 좋아?
A. `UserResponse`, `PostDetailResponse`, `PostSummaryResponse`처럼 Resource와 응답 범위를 드러내는 이름이 좋다.

Q. 목록 응답과 상세 응답은 DTO를 분리해야 해?
A. 필드가 다르면 분리하는 것이 좋다. 목록에는 요약 필드만, 상세에는 상세 필드를 포함한다.

Q. 로그인 응답은 `UserResponse`로 해도 돼?
A. 로그인 결과가 토큰 중심이면 `LoginResponse`나 `TokenResponse`처럼 Action 또는 결과 중심 이름이 더 명확하다.

Q. `ResDto` 같은 축약어를 써도 돼?
A. 가능하지만 프로젝트 전체에서 통일해야 한다. RAG 문서에서는 `Response`처럼 명확한 이름을 권장한다.

---

# 4. DTO and Entity Boundary

## 4.1 DTO vs Entity

### [개념]

DTO와 Entity는 역할이 다르다.

Entity는 Database Table과 Domain State를 표현한다.

DTO는 API Request / Response 데이터를 표현한다.

DTO와 Entity를 분리하면 Persistence Layer와 API Layer의 결합을 줄일 수 있다.

---

### [핵심]

비교:

| 구분       | DTO                                 | Entity                  |
| ---------- | ----------------------------------- | ----------------------- |
| 목적       | API 입출력                          | DB / Domain Model       |
| 위치       | Controller Boundary                 | Persistence / Domain    |
| 변경 기준  | API Spec                            | DB Schema / Domain Rule |
| 외부 노출  | 가능                                | 직접 노출 지양          |
| Validation | Request 형식 검증                   | Domain 무결성           |
| Annotation | Validation, JSON                    | JPA                     |
| 예         | `UserCreateRequest`, `UserResponse` | `User`                  |

핵심 규칙:

- Entity는 내부 모델로 유지한다.
- DTO는 외부 API 계약으로 사용한다.
- Entity 변경이 API 응답에 직접 반영되지 않게 한다.
- API 변경이 Entity 구조를 흔들지 않게 한다.
- Entity에 API 응답 책임을 넣지 않는다.
- DTO에 Domain Logic을 과도하게 넣지 않는다.

---

### [실무]

나쁜 구조:

```java
@PostMapping("/users")
public User createUser(@RequestBody User user) {
    return userRepository.save(user);
}
```

위험:

```text
RequestBody Entity 수신
→ Client가 role, status 같은 필드 조작 가능
→ Entity 내부 구조 노출
→ Validation 기준 불명확
→ API와 DB 강결합
```

좋은 구조:

```java
@PostMapping("/users")
public ApiResponse<UserResponse> createUser(
        @Valid @RequestBody UserCreateRequest request
) {
    return ApiResponse.success(userService.createUser(request));
}
```

Service:

```java
@Transactional
public UserResponse createUser(UserCreateRequest request) {
    User user = User.create(
            request.email(),
            passwordEncoder.encode(request.password()),
            request.nickname()
    );

    User savedUser = userRepository.save(user);

    return UserResponse.from(savedUser);
}
```

Response DTO:

```java
public record UserResponse(
        Long userId,
        String email,
        String nickname
) {
    public static UserResponse from(User user) {
        return new UserResponse(
                user.getId(),
                user.getEmail(),
                user.getNickname()
        );
    }
}
```

---

### [FAQ]

Q. DTO와 Entity 차이는?
A. DTO는 API 입출력 데이터이고 Entity는 DB와 도메인 구조를 표현하는 내부 모델이다.

Q. Entity를 RequestBody로 받으면 왜 위험해?
A. Client가 내부 필드를 조작할 수 있고 API 입력 구조와 DB 구조가 강하게 결합된다.

Q. Entity를 Response로 반환하면 왜 위험해?
A. 민감정보 노출, Lazy Loading 문제, 순환 참조, API 구조 불안정 문제가 생길 수 있다.

Q. DTO와 Entity를 분리하면 코드가 많아지지 않아?
A. 코드량은 늘지만 API 안정성, 보안, 유지보수성, 테스트 가능성이 좋아진다.

---

## 4.2 Sensitive Data Exposure Rules

### [개념]

Sensitive Data Exposure는 API Response에서 비밀번호, 토큰, 권한 정보, 개인정보 같은 민감정보가 노출되는 문제다.

Response DTO는 민감정보 노출을 막는 주요 방어선이다.

---

### [핵심]

노출 금지 대상:

- password
- encodedPassword
- refreshToken
- accessToken 저장값
- secret key
- API key
- role 내부 값
- internal status
- 주민번호 / 고유식별번호
- 전화번호 전체
- 주소 상세정보
- 결제 정보
- 내부 운영 메모
- 삭제 여부
- 관리자 플래그

주의 대상:

- email
- nickname
- profileImageUrl
- providerId
- createdAt
- lastLoginAt
- userRole
- accountStatus

핵심 규칙:

- Entity를 직접 반환하지 않는다.
- Response DTO에 필요한 필드만 명시한다.
- 인증 사용자 본인 응답과 공개 응답을 구분한다.
- 관리자 응답과 일반 사용자 응답을 구분한다.
- Token은 필요한 API에서만 제한적으로 반환한다.
- 로그에도 민감정보를 남기지 않는다.

---

### [실무]

비권장:

```java
public record UserResponse(
        Long userId,
        String email,
        String password,
        String role,
        String refreshToken
) {
}
```

권장:

```java
public record UserResponse(
        Long userId,
        String email,
        String nickname
) {
}
```

공개 프로필 응답:

```java
public record PublicUserProfileResponse(
        Long userId,
        String nickname,
        String profileImageUrl
) {
}
```

내 정보 응답:

```java
public record MyProfileResponse(
        Long userId,
        String email,
        String nickname,
        String profileImageUrl
) {
}
```

관리자 응답:

```java
public record AdminUserResponse(
        Long userId,
        String email,
        String nickname,
        String status,
        LocalDateTime createdAt
) {
}
```

분리 기준:

```text
Public Response
→ 최소 공개 정보

My Response
→ 본인에게 필요한 정보

Admin Response
→ 운영에 필요한 정보

Token Response
→ 인증 흐름에 필요한 토큰 정보
```

---

### [FAQ]

Q. Response DTO에서 비밀번호를 빼야 해?
A. 반드시 제외해야 한다. 암호화된 비밀번호도 외부 응답에 포함하지 않는다.

Q. Role 정보는 응답해도 돼?
A. 필요한 경우에만 제한적으로 반환한다. 일반 공개 응답에는 포함하지 않는 것이 좋다.

Q. 내 정보 조회와 공개 프로필 조회는 같은 DTO를 써도 돼?
A. 노출 필드가 다르면 분리하는 것이 좋다.

Q. Token은 Response DTO에 넣어도 돼?
A. 로그인이나 재발급 응답처럼 필요한 경우에만 TokenResponse로 제한적으로 반환한다.

---

# 5. ApiResponse Convention

## 5.1 ApiResponse Purpose

### [개념]

ApiResponse는 API 성공 / 실패 응답 형식을 일관되게 만들기 위한 공통 응답 객체다.

ApiResponse는 Frontend가 응답을 예측 가능한 구조로 처리하도록 돕는다.

ApiResponse는 Controller 응답 규칙과 GlobalExceptionHandler 응답 규칙을 연결한다.

---

### [핵심]

ApiResponse 목적:

- 성공 응답 형식 통일
- 실패 응답 형식 통일
- Frontend 처리 단순화
- Error Handling 일관화
- API Contract 안정화
- Response Metadata 제공
- Backend Agent 응답 생성 기준 제공
- Review Agent 응답 구조 검수 기준 제공

공통 필드 후보:

- success
- message
- data
- errorCode
- status
- timestamp
- path

기본 성공 구조:

```json
{
  "success": true,
  "message": "success",
  "data": {
    "postId": 1,
    "title": "Spring Boot"
  }
}
```

기본 실패 구조:

```json
{
  "success": false,
  "message": "게시글을 찾을 수 없습니다.",
  "errorCode": "POST_NOT_FOUND"
}
```

---

### [실무]

간단한 ApiResponse:

```java
public record ApiResponse<T>(
        boolean success,
        String message,
        T data
) {
    public static <T> ApiResponse<T> success(T data) {
        return new ApiResponse<>(true, "success", data);
    }

    public static <T> ApiResponse<T> fail(String message) {
        return new ApiResponse<>(false, message, null);
    }
}
```

ErrorCode 포함 ApiResponse:

```java
public record ApiResponse<T>(
        boolean success,
        String message,
        T data,
        String errorCode
) {
    public static <T> ApiResponse<T> success(T data) {
        return new ApiResponse<>(true, "success", data, null);
    }

    public static <T> ApiResponse<T> fail(String errorCode, String message) {
        return new ApiResponse<>(false, message, null, errorCode);
    }
}
```

Controller 성공 응답:

```java
@GetMapping("/{postId}")
public ApiResponse<PostResponse> getPost(@PathVariable Long postId) {
    return ApiResponse.success(postService.getPost(postId));
}
```

GlobalExceptionHandler 실패 응답:

```java
@ExceptionHandler(BusinessException.class)
public ApiResponse<Void> handleBusinessException(BusinessException exception) {
    return ApiResponse.fail(
            exception.getErrorCode().name(),
            exception.getMessage()
    );
}
```

권장:

- 성공 응답은 Controller에서 `ApiResponse.success(data)`로 통일한다.
- 실패 응답은 GlobalExceptionHandler에서 `ApiResponse.fail(...)`로 통일한다.
- Controller마다 실패 응답을 직접 만들지 않는다.
- ErrorCode 체계를 별도로 둔다.
- ResponseEntity 사용 여부는 프로젝트 규칙으로 통일한다.

---

### [FAQ]

Q. ApiResponse는 왜 써?
A. 성공 / 실패 응답 형식을 통일해 Frontend가 일관되게 처리하도록 하기 위해 사용한다.

Q. 모든 응답을 ApiResponse로 감싸야 해?
A. 프로젝트 규칙에 따라 정한다. 일반 API는 통일하고 파일 다운로드나 스트리밍은 예외가 될 수 있다.

Q. 실패 응답도 ApiResponse로 처리해?
A. 가능하다. 보통 GlobalExceptionHandler에서 실패 응답을 공통 구조로 변환한다.

Q. ApiResponse에 errorCode가 필요해?
A. Frontend가 에러를 구분해 처리해야 한다면 errorCode를 포함하는 것이 좋다.

---

## 5.2 ApiResponse Design Rules

### [개념]

ApiResponse Design Rules는 공통 응답 객체의 필드, 생성 메서드, 성공 / 실패 구조를 설계하는 기준이다.

ApiResponse는 단순 Wrapper가 아니라 API 응답 규약이다.

---

### [핵심]

기본 설계 후보:

```java
public record ApiResponse<T>(
        boolean success,
        String message,
        T data,
        String errorCode,
        LocalDateTime timestamp
) {
}
```

필드 선택 기준:

| 필드      | 목적                 | 권장 여부          |
| --------- | -------------------- | ------------------ |
| success   | 성공 여부            | 권장               |
| message   | 사용자 / 공통 메시지 | 권장               |
| data      | 성공 응답 데이터     | 권장               |
| errorCode | 에러 구분 코드       | 권장               |
| timestamp | 응답 시각            | 선택               |
| status    | HTTP Status 코드     | 선택               |
| path      | 요청 경로            | 실패 응답에서 선택 |

핵심 규칙:

- 성공 응답과 실패 응답 구조를 예측 가능하게 만든다.
- data는 성공 시 사용하고 실패 시 null로 둘 수 있다.
- errorCode는 실패 시 사용하고 성공 시 null로 둘 수 있다.
- message 의미를 프로젝트에서 통일한다.
- HTTP Status와 Body status 중복 사용 여부를 결정한다.
- timestamp는 필요하면 자동 생성한다.
- Generic Type을 사용해 다양한 data 타입을 지원한다.

---

### [실무]

권장 기본형:

```java
public record ApiResponse<T>(
        boolean success,
        String message,
        T data,
        String errorCode
) {
    public static <T> ApiResponse<T> success(T data) {
        return new ApiResponse<>(true, "success", data, null);
    }

    public static <T> ApiResponse<T> success(String message, T data) {
        return new ApiResponse<>(true, message, data, null);
    }

    public static ApiResponse<Void> fail(String errorCode, String message) {
        return new ApiResponse<>(false, message, null, errorCode);
    }
}
```

timestamp 포함형:

```java
public record ApiResponse<T>(
        boolean success,
        String message,
        T data,
        String errorCode,
        LocalDateTime timestamp
) {
    public static <T> ApiResponse<T> success(T data) {
        return new ApiResponse<>(
                true,
                "success",
                data,
                null,
                LocalDateTime.now()
        );
    }

    public static ApiResponse<Void> fail(String errorCode, String message) {
        return new ApiResponse<>(
                false,
                message,
                null,
                errorCode,
                LocalDateTime.now()
        );
    }
}
```

주의:

```java
public record ApiResponse<T>(
        String result,
        String msg,
        Object payload,
        String code
) {
}
```

문제:

- 필드 의미 불명확
- Frontend 처리 기준 불명확
- 타입 안정성 약함
- 프로젝트 내 응답 일관성 저하

---

### [FAQ]

Q. ApiResponse 필드는 뭐가 필요해?
A. 기본적으로 success, message, data, errorCode 정도가 실무에서 사용하기 쉽다.

Q. data는 실패 시 어떻게 해?
A. 보통 null로 두고 errorCode와 message를 통해 실패 원인을 전달한다.

Q. timestamp는 꼭 필요해?
A. 필수는 아니지만 로그 추적이나 에러 분석에 도움이 된다.

Q. ApiResponse data 타입은 Object로 해도 돼?
A. 가능하지만 Generic `ApiResponse<T>`가 타입 안정성과 코드 가독성 측면에서 좋다.

---

## 5.3 ApiResponse Success Rules

### [개념]

ApiResponse Success Rules는 Controller가 성공 응답을 일관된 구조로 반환하는 규칙이다.

성공 응답은 Frontend가 data를 안정적으로 사용할 수 있게 만들어야 한다.

---

### [핵심]

성공 응답 기준:

- `success = true`
- `message = "success"` 또는 성공 메시지
- `data = Response DTO`
- `errorCode = null`
- HTTP Status는 기본 200 또는 필요 시 201

예:

```json
{
  "success": true,
  "message": "success",
  "data": {
    "userId": 1,
    "nickname": "jun"
  },
  "errorCode": null
}
```

Controller 기본:

```java
return ApiResponse.success(response);
```

핵심 규칙:

- 성공 응답은 `ApiResponse.success()`로 통일한다.
- Entity를 data에 직접 넣지 않는다.
- Response DTO를 data에 넣는다.
- 목록 응답은 `List`, `Page`, `Slice` 중 프로젝트 기준에 맞춘다.
- 삭제 응답은 `Void`, message, status 기준을 정한다.
- 생성 응답은 201 Created가 필요한지 검토한다.

---

### [실무]

단건 조회:

```java
@GetMapping("/{postId}")
public ApiResponse<PostResponse> getPost(@PathVariable Long postId) {
    return ApiResponse.success(postService.getPost(postId));
}
```

목록 조회:

```java
@GetMapping
public ApiResponse<Slice<PostSummaryResponse>> getPosts(Pageable pageable) {
    return ApiResponse.success(postService.getPosts(pageable));
}
```

생성:

```java
@PostMapping
public ApiResponse<PostResponse> createPost(
        @Valid @RequestBody PostCreateRequest request
) {
    return ApiResponse.success(postService.createPost(request));
}
```

생성 시 HTTP Status 제어:

```java
@PostMapping
public ResponseEntity<ApiResponse<PostResponse>> createPost(
        @Valid @RequestBody PostCreateRequest request
) {
    PostResponse response = postService.createPost(request);

    return ResponseEntity
            .status(HttpStatus.CREATED)
            .body(ApiResponse.success(response));
}
```

삭제:

```java
@DeleteMapping("/{postId}")
public ApiResponse<Void> deletePost(@PathVariable Long postId) {
    postService.deletePost(postId);
    return ApiResponse.success(null);
}
```

삭제 메시지 포함:

```java
@DeleteMapping("/{postId}")
public ApiResponse<Void> deletePost(@PathVariable Long postId) {
    postService.deletePost(postId);
    return ApiResponse.success("deleted", null);
}
```

---

### [FAQ]

Q. 성공 응답은 어떻게 반환해?
A. Controller에서 Response DTO를 받은 뒤 `ApiResponse.success(response)`로 감싸 반환한다.

Q. 삭제 API는 data를 뭘로 줘?
A. 프로젝트 규칙에 따라 `ApiResponse<Void>`에 null을 넣거나 성공 메시지만 반환할 수 있다.

Q. 생성 API는 무조건 201을 반환해야 해?
A. REST 기준으로는 201 Created가 적합할 수 있다. 필요하면 ResponseEntity로 HTTP Status를 제어한다.

Q. 목록 응답도 ApiResponse로 감싸?
A. 공통 응답 규칙을 사용한다면 `ApiResponse<List<T>>`, `ApiResponse<Page<T>>`, `ApiResponse<Slice<T>>` 형태로 감싼다.

---

## 5.4 ApiResponse Failure Rules

### [개념]

ApiResponse Failure Rules는 실패 응답을 일관된 구조로 반환하는 규칙이다.

실패 응답은 Controller에서 직접 조립하지 않고 GlobalExceptionHandler에서 처리하는 것이 좋다.

---

### [핵심]

실패 응답 기준:

- `success = false`
- `message = 사용자 또는 공통 에러 메시지`
- `data = null`
- `errorCode = ErrorCode`
- HTTP Status는 예외 유형에 맞게 설정 가능

예:

```json
{
  "success": false,
  "message": "사용자를 찾을 수 없습니다.",
  "data": null,
  "errorCode": "USER_NOT_FOUND"
}
```

핵심 규칙:

- 비즈니스 실패는 CustomException으로 표현한다.
- ErrorCode를 사용한다.
- 실패 응답은 GlobalExceptionHandler에서 생성한다.
- Controller에서 실패 ApiResponse를 직접 반복 생성하지 않는다.
- 내부 예외 메시지를 그대로 노출하지 않는다.
- Validation Error 응답 구조를 통일한다.

---

### [실무]

ErrorCode:

```java
public enum ErrorCode {
    USER_NOT_FOUND,
    POST_NOT_FOUND,
    INVALID_REQUEST,
    ACCESS_DENIED
}
```

BusinessException:

```java
public class BusinessException extends RuntimeException {

    private final ErrorCode errorCode;

    public BusinessException(ErrorCode errorCode, String message) {
        super(message);
        this.errorCode = errorCode;
    }

    public ErrorCode getErrorCode() {
        return errorCode;
    }
}
```

GlobalExceptionHandler:

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(BusinessException.class)
    public ApiResponse<Void> handleBusinessException(
            BusinessException exception
    ) {
        return ApiResponse.fail(
                exception.getErrorCode().name(),
                exception.getMessage()
        );
    }
}
```

Service:

```java
@Transactional(readOnly = true)
public UserResponse getUser(Long userId) {
    User user = userRepository.findById(userId)
            .orElseThrow(() -> new BusinessException(
                    ErrorCode.USER_NOT_FOUND,
                    "사용자를 찾을 수 없습니다."
            ));

    return UserResponse.from(user);
}
```

비권장 Controller:

```java
@GetMapping("/{userId}")
public ApiResponse<UserResponse> getUser(@PathVariable Long userId) {
    try {
        return ApiResponse.success(userService.getUser(userId));
    } catch (RuntimeException e) {
        return ApiResponse.fail("ERROR", e.getMessage());
    }
}
```

문제:

- Controller마다 try-catch 반복
- ErrorCode 불일치
- HTTP Status 제어 어려움
- 내부 예외 메시지 노출 가능
- 공통 에러 응답 관리 어려움

---

### [FAQ]

Q. 실패 응답은 어디서 만들어?
A. 일반적으로 GlobalExceptionHandler에서 공통 ApiResponse 실패 구조로 만든다.

Q. Controller에서 try-catch로 실패 응답을 만들어도 돼?
A. 반복되고 일관성이 깨지므로 권장하지 않는다.

Q. errorCode는 왜 필요해?
A. Frontend가 에러 상황을 구분하고 메시지, 화면 전환, 재시도 처리를 안정적으로 하기 위해 필요하다.

Q. 예외 메시지를 그대로 응답해도 돼?
A. 내부 정보가 노출될 수 있으므로 사용자에게 보여줄 메시지와 서버 로그 메시지를 구분하는 것이 좋다.

---

# 6. ResponseEntity and ApiResponse

## 6.1 ResponseEntity Usage Rules

### [개념]

ResponseEntity는 HTTP Response의 Status Code, Header, Body를 세밀하게 제어할 수 있는 Spring 객체다.

ApiResponse는 Body 구조를 통일하는 객체다.

둘은 함께 사용할 수 있다.

---

### [핵심]

비교:

| 구분      | ApiResponse                       | ResponseEntity                              |
| --------- | --------------------------------- | ------------------------------------------- |
| 목적      | Body 응답 구조 통일               | HTTP 응답 제어                              |
| 제어 대상 | success, message, data, errorCode | status, header, body                        |
| 사용 위치 | Controller / ExceptionHandler     | Controller / ExceptionHandler               |
| 장점      | Frontend 처리 일관화              | HTTP 의미 명확화                            |
| 예        | `ApiResponse<UserResponse>`       | `ResponseEntity<ApiResponse<UserResponse>>` |

선택 기준:

- 단순 성공 응답은 `ApiResponse<T>` 가능
- HTTP Status 제어가 필요하면 `ResponseEntity<ApiResponse<T>>`
- Header 제어가 필요하면 `ResponseEntity`
- Created Location이 필요하면 `ResponseEntity`
- 파일 다운로드는 별도 응답 구조 검토
- 프로젝트 규칙으로 통일한다.

---

### [실무]

ApiResponse 직접 반환:

```java
@GetMapping("/{postId}")
public ApiResponse<PostResponse> getPost(@PathVariable Long postId) {
    return ApiResponse.success(postService.getPost(postId));
}
```

ResponseEntity와 함께 사용:

```java
@PostMapping
public ResponseEntity<ApiResponse<PostResponse>> createPost(
        @Valid @RequestBody PostCreateRequest request
) {
    PostResponse response = postService.createPost(request);

    return ResponseEntity
            .status(HttpStatus.CREATED)
            .body(ApiResponse.success(response));
}
```

Header 제어:

```java
@PostMapping
public ResponseEntity<ApiResponse<PostResponse>> createPost(
        @Valid @RequestBody PostCreateRequest request
) {
    PostResponse response = postService.createPost(request);

    URI location = URI.create("/api/posts/" + response.postId());

    return ResponseEntity
            .created(location)
            .body(ApiResponse.success(response));
}
```

ExceptionHandler에서 사용:

```java
@ExceptionHandler(BusinessException.class)
public ResponseEntity<ApiResponse<Void>> handleBusinessException(
        BusinessException exception
) {
    return ResponseEntity
            .status(HttpStatus.BAD_REQUEST)
            .body(ApiResponse.fail(
                    exception.getErrorCode().name(),
                    exception.getMessage()
            ));
}
```

---

### [FAQ]

Q. ApiResponse만 반환해도 돼?
A. 프로젝트 규칙이 성공 응답은 ApiResponse 직접 반환하고 실패는 GlobalExceptionHandler가 처리하는 구조라면 가능하다.

Q. ResponseEntity는 언제 써?
A. HTTP 상태 코드, Header, Created Location 등 HTTP 응답을 세밀하게 제어해야 할 때 유용하다.

Q. ResponseEntity와 ApiResponse를 같이 써도 돼?
A. 가능하다. ResponseEntity는 HTTP 응답을 제어하고 ApiResponse는 Body 구조를 통일한다.

Q. 둘 중 하나만 써야 해?
A. 아니다. 프로젝트 응답 규칙에 따라 직접 반환 또는 조합 방식을 선택할 수 있다.

---

# 7. DTO with List, Page, Slice

## 7.1 List Response DTO Rules

### [개념]

List Response DTO는 여러 개의 Response DTO를 반환하는 응답 구조다.

Spring Boot에서는 `List<T>`, `Page<T>`, `Slice<T>`를 ApiResponse data로 감싸 반환할 수 있다.

목록 응답은 Pagination 전략과 함께 설계해야 한다.

---

### [핵심]

목록 응답 유형:

| 유형                 | 특징                  | 사용 상황               |
| -------------------- | --------------------- | ----------------------- |
| `List<T>`            | 전체 목록             | 데이터가 적을 때        |
| `Page<T>`            | 전체 개수 포함        | 페이지 번호 UI          |
| `Slice<T>`           | 다음 페이지 여부 중심 | 무한 스크롤 / 더보기    |
| Custom List Response | 메타데이터 직접 제어  | API 응답 포맷 고정 필요 |

예:

```java
ApiResponse<List<PostResponse>>
ApiResponse<Page<PostResponse>>
ApiResponse<Slice<PostResponse>>
```

핵심 규칙:

- 소량 데이터는 List 가능
- 목록 UI는 Page 또는 Slice 검토
- 무한 스크롤은 Slice가 적합할 수 있다.
- 대용량 데이터에서 Page count query 비용을 주의한다.
- Entity 목록을 직접 반환하지 않는다.
- 목록 전용 Summary Response DTO를 검토한다.

---

### [실무]

List 응답:

```java
@GetMapping("/popular")
public ApiResponse<List<PostSummaryResponse>> getPopularPosts() {
    return ApiResponse.success(postService.getPopularPosts());
}
```

Service:

```java
@Transactional(readOnly = true)
public List<PostSummaryResponse> getPopularPosts() {
    return postRepository.findTop10ByOrderByLikeCountDesc().stream()
            .map(PostSummaryResponse::from)
            .toList();
}
```

Slice 응답:

```java
@GetMapping
public ApiResponse<Slice<PostSummaryResponse>> getPosts(Pageable pageable) {
    return ApiResponse.success(postService.getPosts(pageable));
}
```

Service:

```java
@Transactional(readOnly = true)
public Slice<PostSummaryResponse> getPosts(Pageable pageable) {
    return postRepository.findAll(pageable)
            .map(PostSummaryResponse::from);
}
```

Page 응답:

```java
@GetMapping("/admin")
public ApiResponse<Page<PostSummaryResponse>> getPostsForAdmin(Pageable pageable) {
    return ApiResponse.success(postService.getPostsForAdmin(pageable));
}
```

Custom List Response:

```java
public record PostListResponse(
        List<PostSummaryResponse> posts,
        boolean hasNext
) {
}
```

사용:

```java
@GetMapping
public ApiResponse<PostListResponse> getPosts(Pageable pageable) {
    return ApiResponse.success(postService.getPosts(pageable));
}
```

---

### [FAQ]

Q. 목록 응답은 List로 반환하면 돼?
A. 데이터가 적으면 List도 가능하지만, 일반 목록 UI는 Page나 Slice를 검토하는 것이 좋다.

Q. Page와 Slice 차이는?
A. Page는 전체 개수를 포함하고 Slice는 다음 페이지 존재 여부 중심이다. 무한 스크롤은 Slice가 적합할 수 있다.

Q. 목록 조회에도 SummaryResponse가 필요해?
A. 상세 필드가 많다면 목록에는 필요한 요약 필드만 담은 SummaryResponse를 사용하는 것이 좋다.

Q. Page를 쓰면 항상 좋은가?
A. 아니다. total count query 비용이 발생할 수 있어 대용량 데이터에서는 Slice나 커서 기반 방식을 검토한다.

---

# 8. JSON Naming and Serialization

## 8.1 JSON Field Naming Rules

### [개념]

JSON Field Naming은 Client와 Server가 주고받는 JSON 필드 이름을 정하는 규칙이다.

Spring Boot DTO 필드명은 기본적으로 JSON 필드명과 매칭된다.

JSON Naming이 불일치하면 Request Binding 문제와 Frontend 연동 문제가 발생한다.

---

### [핵심]

기본 규칙:

- Java 필드는 camelCase 사용
- JSON 필드도 camelCase 사용 권장
- DTO 필드명과 JSON 필드명을 일치시킨다.
- 다른 이름이 필요하면 `@JsonProperty` 사용을 검토한다.
- 외부 API 응답과 내부 DTO를 분리한다.
- 날짜 포맷 기준을 통일한다.

예:

```java
public record UserResponse(
        Long userId,
        String profileImageUrl
) {
}
```

JSON:

```json
{
  "userId": 1,
  "profileImageUrl": "https://example.com/profile.png"
}
```

핵심 주의:

- `user_id`와 `userId` 혼용 금지
- `postId`, `id`, `post_id` 혼용 금지
- Frontend와 DTO 필드명을 맞춘다.
- 외부 API의 snake_case는 External Response DTO에서 처리한다.

---

### [실무]

기본 Request DTO:

```java
public record UserUpdateRequest(
        String profileImageUrl
) {
}
```

요청 JSON:

```json
{
  "profileImageUrl": "https://example.com/image.png"
}
```

필드명 불일치:

```json
{
  "profile_image_url": "https://example.com/image.png"
}
```

결과:

```text
profileImageUrl에 값이 매핑되지 않을 수 있음
```

`@JsonProperty` 사용:

```java
public record ExternalUserResponse(
        @JsonProperty("profile_image_url")
        String profileImageUrl
) {
}
```

권장:

```text
내부 API DTO
→ camelCase 통일

외부 API DTO
→ 외부 필드명에 맞게 @JsonProperty 사용

Entity
→ API JSON 필드명과 직접 결합하지 않음
```

---

### [FAQ]

Q. JSON 필드명은 camelCase로 해?
A. Spring Boot 내부 API에서는 Java 필드명과 맞춰 camelCase를 사용하는 경우가 많다.

Q. snake_case JSON을 받으려면?
A. `@JsonProperty`를 사용하거나 ObjectMapper naming strategy를 설정할 수 있다.

Q. DTO 필드명과 JSON 필드명이 다르면?
A. Binding이 실패하거나 값이 null로 들어올 수 있다.

Q. 외부 API 응답 DTO도 내부 Response DTO와 같이 써도 돼?
A. 권장하지 않는다. 외부 API 응답 DTO와 내부 API Response DTO를 분리하는 것이 좋다.

---

## 8.2 Date and Enum Response Rules

### [개념]

Date and Enum Response Rules는 DTO에서 날짜, 시간, enum 상태 값을 어떻게 표현할지 정하는 규칙이다.

날짜와 enum 표현이 불일치하면 Frontend 연동과 검색 조건 처리에서 문제가 생긴다.

---

### [핵심]

날짜 / 시간 타입:

- `LocalDate`
- `LocalDateTime`
- `ZonedDateTime`
- `Instant`

enum 표현 방식:

- enum name 그대로 반환
- 별도 code 반환
- code + label 반환
- Frontend 표시용 text 반환

날짜 기준:

- API 날짜 포맷 통일
- Timezone 기준 명확화
- LocalDate와 LocalDateTime 구분
- 문자열로 직접 조립 지양
- 필요 시 `@JsonFormat` 검토

enum 기준:

- 내부 enum 이름과 외부 표시명을 구분한다.
- Frontend 표시 text가 필요하면 label을 별도 제공한다.
- enum name 변경이 API 변경으로 이어질 수 있음을 주의한다.

---

### [실무]

날짜 응답:

```java
public record PostResponse(
        Long postId,
        String title,
        LocalDateTime createdAt
) {
}
```

JSON 예:

```json
{
  "postId": 1,
  "title": "Spring Boot",
  "createdAt": "2026-07-03T13:00:00"
}
```

날짜 포맷 지정:

```java
public record FestivalResponse(
        Long festivalId,
        String title,
        @JsonFormat(pattern = "yyyy-MM-dd")
        LocalDate startDate,
        @JsonFormat(pattern = "yyyy-MM-dd")
        LocalDate endDate
) {
}
```

enum:

```java
public enum PostStatus {
    DRAFT,
    PUBLISHED,
    DELETED
}
```

기본 응답:

```java
public record PostResponse(
        Long postId,
        String title,
        PostStatus status
) {
}
```

code + label 응답:

```java
public record PostStatusResponse(
        String code,
        String label
) {
    public static PostStatusResponse from(PostStatus status) {
        return new PostStatusResponse(
                status.name(),
                switch (status) {
                    case DRAFT -> "임시저장";
                    case PUBLISHED -> "게시됨";
                    case DELETED -> "삭제됨";
                }
        );
    }
}
```

권장:

- 내부 상태 enum을 그대로 노출할지 결정한다.
- 화면 표시명이 필요하면 label을 따로 제공한다.
- 날짜 기준은 API 문서에 명시한다.
- 시간대가 중요한 서비스는 Timezone 기준을 정한다.

---

### [FAQ]

Q. DTO에서 날짜는 String으로 반환해야 해?
A. 필수는 아니다. `LocalDate`, `LocalDateTime`을 사용하고 JSON 포맷 기준을 통일하는 것이 좋다.

Q. enum을 그대로 응답해도 돼?
A. 가능하지만 enum name 변경이 API 변경으로 이어질 수 있어 code / label 분리를 검토한다.

Q. 날짜 포맷은 어디서 정해?
A. 프로젝트 공통 ObjectMapper 설정이나 DTO의 `@JsonFormat`으로 정할 수 있다.

Q. 화면 표시용 enum 이름은 어디서 처리해?
A. Frontend에서 처리하거나 Backend Response DTO에서 label을 함께 제공할 수 있다.

---

# 9. DTO Anti Pattern

## 9.1 DTO Common Mistakes

### [개념]

DTO Anti Pattern은 DTO를 사용하지만 Request / Response / Entity 책임이 섞여 API 안정성과 보안성이 떨어지는 구조다.

DTO는 단순히 객체를 하나 더 만드는 것이 아니라 API Boundary를 설계하는 작업이다.

---

### [핵심]

자주 발생하는 실수:

- Entity를 RequestBody로 사용
- Entity를 Response로 반환
- Request DTO와 Response DTO를 하나로 합침
- `UserDto` 하나로 모든 API 처리
- DTO에 Entity 전체 필드 복사
- Response DTO에 password 포함
- DTO에 Business Logic 과다 작성
- DTO 변환 로직이 Controller에 흩어짐
- Entity 안에 `toResponse()` 작성
- Request DTO Validation 누락
- Controller Parameter에 `@Valid` 누락
- Map으로 Request 수신
- Object 타입으로 data 처리
- JSON 필드명 불일치
- 날짜 / enum 응답 기준 없음
- 목록 응답에서 Entity List 직접 반환

---

### [실무]

문제 예:

```java
public record UserDto(
        Long id,
        String email,
        String password,
        String role,
        String nickname
) {
}
```

사용:

```java
@PostMapping("/users")
public ApiResponse<UserDto> createUser(
        @RequestBody UserDto userDto
) {
    ...
}
```

문제:

```text
Request / Response 용도 혼합
→ password 응답 노출 위험
→ role 입력 조작 위험
→ Validation 기준 불명확
→ API Spec 불안정
```

개선:

```java
public record UserCreateRequest(
        @Email String email,
        @NotBlank String password,
        @NotBlank String nickname
) {
}
```

```java
public record UserResponse(
        Long userId,
        String email,
        String nickname
) {
}
```

문제 예:

```java
@GetMapping
public ApiResponse<List<Post>> getPosts() {
    return ApiResponse.success(postRepository.findAll());
}
```

개선:

```java
@GetMapping
public ApiResponse<List<PostSummaryResponse>> getPosts() {
    return ApiResponse.success(postService.getPosts());
}
```

---

### [FAQ]

Q. DTO를 쓰는데도 문제가 생기는 이유는?
A. Request / Response / Entity 책임을 분리하지 않고 하나의 DTO에 모두 넣으면 DTO의 목적이 사라진다.

Q. `UserDto` 하나로 요청과 응답을 처리하면 왜 안 좋아?
A. 요청 필드와 응답 필드가 달라 민감정보 노출, 입력 조작, Validation 혼란이 생길 수 있다.

Q. DTO에 비즈니스 로직을 넣어도 돼?
A. 단순 변환은 가능하지만 비즈니스 규칙은 Service나 Domain에서 처리하는 것이 좋다.

Q. Map으로 Request를 받으면 안 돼?
A. 테스트용은 가능하지만 실무 API에서는 타입 안정성과 Validation을 위해 Request DTO를 사용하는 것이 좋다.

---

# 10. Review Checklist

## 10.1 DTO and ApiResponse Checklist

### [개념]

DTO and ApiResponse Checklist는 DTO 구조, Entity 경계, 응답 형식 일관성을 검수하기 위한 기준이다.

Backend Agent와 Review Agent는 이 Checklist를 기준으로 API Boundary 문제를 탐지한다.

---

### [핵심]

Checklist:

```md
- [ ] Request DTO와 Response DTO가 분리되어 있는가?
- [ ] Entity를 RequestBody로 직접 받지 않는가?
- [ ] Entity를 Response로 직접 반환하지 않는가?
- [ ] DTO 이름이 Use Case를 명확히 표현하는가?
- [ ] Request DTO에 필요한 입력 필드만 포함했는가?
- [ ] Response DTO에 필요한 출력 필드만 포함했는가?
- [ ] Response DTO에 password, refreshToken, secret 등 민감정보가 없는가?
- [ ] 생성 / 수정 / 검색 DTO가 필요한 경우 분리되어 있는가?
- [ ] Request DTO에 Validation Annotation이 적용되어 있는가?
- [ ] Controller Parameter에 @Valid가 적용되어 있는가?
- [ ] DTO 필드명과 JSON 필드명이 일치하는가?
- [ ] 날짜 / 시간 응답 기준이 일관적인가?
- [ ] enum 응답 방식이 일관적인가?
- [ ] Entity → Response DTO 변환 위치가 일관적인가?
- [ ] Entity 내부에 API Response 변환 책임이 들어가지 않았는가?
- [ ] Controller에서 복잡한 DTO 변환을 수행하지 않는가?
- [ ] 목록 응답에서 Entity List를 직접 반환하지 않는가?
- [ ] 목록 / 상세 Response DTO가 필요한 경우 분리되어 있는가?
- [ ] ApiResponse 성공 응답 구조가 통일되어 있는가?
- [ ] ApiResponse 실패 응답 구조가 통일되어 있는가?
- [ ] ErrorCode가 필요한 실패 응답에 포함되어 있는가?
- [ ] ResponseEntity 사용 기준이 프로젝트 규칙과 일치하는가?
```

---

### [실무]

검수 흐름:

```text
API Use Case 확인
→ Request DTO 확인
→ Response DTO 확인
→ Entity 직접 노출 여부 확인
→ Validation 확인
→ Sensitive Data 확인
→ DTO Naming 확인
→ DTO Conversion 확인
→ ApiResponse 구조 확인
→ Error Response 구조 확인
→ List / Page / Slice 응답 확인
→ Final Review
```

검수 결과 예:

```text
문제:
UserResponse에 password 필드 포함

위험:
암호화된 비밀번호라도 외부 API로 노출됨

수정:
UserResponse에서 password 제거
```

검수 결과 예:

```text
문제:
PostController가 List<Post>를 반환

위험:
Entity 직접 노출
Lazy Loading 문제
API 구조 불안정

수정:
List<PostSummaryResponse>로 변환 후 반환
```

검수 결과 예:

```text
문제:
UserDto 하나를 생성 요청과 조회 응답에 모두 사용

위험:
요청 / 응답 필드 혼합
Validation 기준 불명확
민감정보 노출 가능

수정:
UserCreateRequest와 UserResponse로 분리
```

---

### [FAQ]

Q. DTO 검수에서 가장 중요한 것은?
A. Request / Response 분리, Entity 직접 노출 금지, 민감정보 제거, Validation 적용, 응답 구조 일관성이다.

Q. ApiResponse 검수에서 가장 중요한 것은?
A. 성공 / 실패 응답 구조가 통일되어 있고 errorCode, message, data 기준이 명확한지 확인하는 것이다.

Q. DTO Naming도 검수해야 해?
A. 맞다. 이름이 불명확하면 Agent Retrieval과 코드 생성 품질이 떨어진다.

Q. 목록 응답 검수는 어떻게 해?
A. Entity List 직접 반환 여부, Summary DTO 사용 여부, Page / Slice 선택 기준을 확인한다.

---

# 11. Part03 Final Goal

## 11.1 DTO and ApiResponse Final Goal

### [개념]

Spring Boot Part03의 최종 목표는 Backend Agent가 Request DTO, Response DTO, ApiResponse를 일관되게 설계하고 Review Agent가 Entity 노출, 민감정보 노출, 응답 구조 불일치를 탐지하도록 만드는 것이다.

Part03은 API Boundary와 Response Convention을 다룬다.

---

### [핵심]

Part03이 지원해야 하는 작업:

- DTO 목적 판단
- Request DTO 설계
- Response DTO 설계
- Search DTO 설계
- DTO Naming 적용
- Request DTO Validation 적용
- DTO와 Entity 분리
- Sensitive Data Exposure 탐지
- Entity → Response DTO 변환
- 목록 Response DTO 설계
- Detail / Summary Response DTO 분리
- JSON Field Naming 검토
- Date / Enum 응답 기준 적용
- ApiResponse 설계
- ApiResponse Success 응답 설계
- ApiResponse Failure 응답 설계
- ResponseEntity 사용 기준 판단
- DTO Anti Pattern 탐지

---

### [실무]

Backend Agent 수행 흐름:

```text
User API Requirement
→ Identify Request Fields
→ Create Request DTO
→ Apply Validation Annotation
→ Identify Response Fields
→ Remove Sensitive Data
→ Create Response DTO
→ Define Entity to DTO Conversion
→ Wrap with ApiResponse
→ Check ResponseEntity Need
→ Review DTO Boundary
```

Review Agent 수행 흐름:

```text
Input Controller / DTO Code
→ Check Request DTO
→ Check Response DTO
→ Detect Entity RequestBody
→ Detect Entity Response
→ Detect Sensitive Data
→ Check Validation
→ Check DTO Naming
→ Check DTO Conversion
→ Check ApiResponse Convention
→ Detect Response Inconsistency
→ Suggest Fix
```

---

### [FAQ]

Q. Spring Boot Part03의 최종 목적은 뭐야?
A. Request DTO, Response DTO, ApiResponse를 일관되게 설계하고 Entity 노출과 응답 구조 문제를 탐지하게 만드는 것이다.

Q. Part03 다음에는 어떤 문서가 이어져야 해?
A. Validation & Binding 문서가 이어지는 것이 좋다.

Q. Part03만으로 API 응답 구조를 만들 수 있어?
A. 가능하다. 다만 Validation Error Handling과 Exception Handling은 후속 Part와 함께 사용해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. DTO는 뭐야?
A. DTO는 Client와 Server 사이의 Request / Response 데이터를 전달하는 API Boundary 객체다.

Q. DTO는 왜 필요해?
A. Entity를 외부에 직접 노출하지 않고 API 요청 / 응답 구조를 안정적으로 관리하기 위해 필요하다.

Q. Request DTO는 뭐야?
A. Client가 Server로 보내는 요청 데이터를 표현하는 API 입력 객체다.

Q. Response DTO는 뭐야?
A. Server가 Client에게 반환할 응답 데이터를 표현하는 API 출력 객체다.

Q. Entity를 DTO 대신 써도 돼?
A. 권장하지 않는다. API 구조와 DB 구조가 강하게 결합되고 민감정보 노출 위험이 생긴다.

Q. Entity를 RequestBody로 받아도 돼?
A. 권장하지 않는다. Request DTO를 따로 만들어 API 입력 구조를 분리하는 것이 좋다.

Q. Entity를 그대로 Response로 반환해도 돼?
A. 권장하지 않는다. 민감정보 노출, Lazy Loading 문제, 순환 참조, API 변경 위험이 생길 수 있다.

Q. Request DTO와 Response DTO는 분리해야 해?
A. 요청과 응답의 필드, 검증 기준, 노출 기준이 다르면 분리하는 것이 좋다.

Q. DTO는 record로 만들어도 돼?
A. Java 17+와 Spring Boot 3.x 기준에서는 불변 DTO를 만들기 위해 record를 사용할 수 있다.

Q. 생성 DTO와 수정 DTO는 분리해야 해?
A. 필드와 검증 조건이 다르면 분리하는 것이 좋다.

Q. 검색 조건도 DTO로 만들 수 있어?
A. 가능하다. 조건이 많으면 `@ModelAttribute`와 SearchRequest DTO를 사용하는 것이 좋다.

Q. Request DTO에 Validation Annotation을 붙이면 바로 동작해?
A. Controller Parameter에 `@Valid`를 붙여야 검증이 실행된다.

Q. `@NotNull`, `@NotBlank`, `@NotEmpty` 차이는?
A. `@NotNull`은 null만 금지하고, `@NotBlank`는 공백 문자열을 금지하며, `@NotEmpty`는 null과 빈 값을 금지한다.

Q. 이메일 검증은 뭘 써?
A. `@Email`을 사용하고 빈 값도 막아야 하면 `@NotBlank`를 함께 사용한다.

Q. 중복 이메일 검증도 DTO에서 해?
A. 아니다. 중복 이메일 같은 비즈니스 검증은 Service에서 Repository를 통해 확인한다.

Q. DTO 이름은 어떻게 짓는 게 좋아?
A. `UserCreateRequest`, `UserResponse`처럼 Resource, Action, Request / Response가 드러나게 짓는 것이 좋다.

Q. `UserDto` 하나로 다 처리하면 안 돼?
A. 권장하지 않는다. 요청과 응답의 필드, 검증 기준, 노출 기준이 달라질 수 있다.

Q. Response DTO에는 어떤 필드를 넣어?
A. Frontend가 필요한 필드만 넣고 비밀번호, 내부 상태, 민감정보는 제외한다.

Q. DTO 변환은 어디서 해?
A. 간단한 변환은 DTO의 static `from` 메서드나 Service에서 처리할 수 있다.

Q. `from`과 `of` 차이는?
A. `from`은 Entity나 객체 하나에서 변환할 때, `of`는 여러 값을 조합해 생성할 때 자주 사용한다.

Q. Entity 안에 `toResponse()`를 만들어도 돼?
A. 권장하지 않는다. Entity가 API 응답 구조를 알게 되어 Layer 의존 방향이 흐려진다.

Q. 변환 로직이 복잡하면 어떻게 해?
A. Mapper Component를 만들어 변환 책임을 분리할 수 있다.

Q. Response DTO 이름은 어떻게 짓는 게 좋아?
A. `UserResponse`, `PostDetailResponse`, `PostSummaryResponse`처럼 Resource와 응답 범위를 드러내는 이름이 좋다.

Q. 목록 응답과 상세 응답은 DTO를 분리해야 해?
A. 필드가 다르면 분리하는 것이 좋다. 목록에는 요약 필드만, 상세에는 상세 필드를 포함한다.

Q. Response DTO에서 비밀번호를 빼야 해?
A. 반드시 제외해야 한다. 암호화된 비밀번호도 외부 응답에 포함하지 않는다.

Q. Role 정보는 응답해도 돼?
A. 필요한 경우에만 제한적으로 반환한다. 일반 공개 응답에는 포함하지 않는 것이 좋다.

Q. 내 정보 조회와 공개 프로필 조회는 같은 DTO를 써도 돼?
A. 노출 필드가 다르면 분리하는 것이 좋다.

Q. Token은 Response DTO에 넣어도 돼?
A. 로그인이나 재발급 응답처럼 필요한 경우에만 TokenResponse로 제한적으로 반환한다.

Q. ApiResponse는 뭐야?
A. API 성공 / 실패 응답 형식을 일관되게 만들기 위한 공통 응답 객체다.

Q. ApiResponse는 왜 써?
A. 성공 / 실패 응답 형식을 통일해 Frontend가 일관되게 처리하도록 하기 위해 사용한다.

Q. 모든 응답을 ApiResponse로 감싸야 해?
A. 프로젝트 규칙에 따라 정한다. 일반 API는 통일하고 파일 다운로드나 스트리밍은 예외가 될 수 있다.

Q. ApiResponse 필드는 뭐가 필요해?
A. 기본적으로 success, message, data, errorCode 정도가 실무에서 사용하기 쉽다.

Q. ApiResponse data는 실패 시 어떻게 해?
A. 보통 null로 두고 errorCode와 message를 통해 실패 원인을 전달한다.

Q. ApiResponse data 타입은 Object로 해도 돼?
A. 가능하지만 Generic `ApiResponse<T>`가 타입 안정성과 코드 가독성 측면에서 좋다.

Q. 성공 응답은 어떻게 반환해?
A. Controller에서 Response DTO를 받은 뒤 `ApiResponse.success(response)`로 감싸 반환한다.

Q. 실패 응답은 어디서 만들어?
A. 일반적으로 GlobalExceptionHandler에서 공통 ApiResponse 실패 구조로 만든다.

Q. errorCode는 왜 필요해?
A. Frontend가 에러 상황을 구분하고 메시지, 화면 전환, 재시도 처리를 안정적으로 하기 위해 필요하다.

Q. ResponseEntity는 언제 써?
A. HTTP 상태 코드, Header, Created Location 등 HTTP 응답을 세밀하게 제어해야 할 때 유용하다.

Q. ResponseEntity와 ApiResponse를 같이 써도 돼?
A. 가능하다. ResponseEntity는 HTTP 응답을 제어하고 ApiResponse는 Body 구조를 통일한다.

Q. 목록 응답은 List로 반환하면 돼?
A. 데이터가 적으면 List도 가능하지만, 일반 목록 UI는 Page나 Slice를 검토하는 것이 좋다.

Q. Page와 Slice 차이는?
A. Page는 전체 개수를 포함하고 Slice는 다음 페이지 존재 여부 중심이다. 무한 스크롤은 Slice가 적합할 수 있다.

Q. 목록 조회에도 SummaryResponse가 필요해?
A. 상세 필드가 많다면 목록에는 필요한 요약 필드만 담은 SummaryResponse를 사용하는 것이 좋다.

Q. JSON 필드명은 camelCase로 해?
A. Spring Boot 내부 API에서는 Java 필드명과 맞춰 camelCase를 사용하는 경우가 많다.

Q. snake_case JSON을 받으려면?
A. `@JsonProperty`를 사용하거나 ObjectMapper naming strategy를 설정할 수 있다.

Q. DTO 필드명과 JSON 필드명이 다르면?
A. Binding이 실패하거나 값이 null로 들어올 수 있다.

Q. DTO에서 날짜는 String으로 반환해야 해?
A. 필수는 아니다. `LocalDate`, `LocalDateTime`을 사용하고 JSON 포맷 기준을 통일하는 것이 좋다.

Q. enum을 그대로 응답해도 돼?
A. 가능하지만 enum name 변경이 API 변경으로 이어질 수 있어 code / label 분리를 검토한다.

Q. DTO를 쓰는데도 문제가 생기는 이유는?
A. Request / Response / Entity 책임을 분리하지 않고 하나의 DTO에 모두 넣으면 DTO의 목적이 사라진다.

Q. Map으로 Request를 받으면 안 돼?
A. 테스트용은 가능하지만 실무 API에서는 타입 안정성과 Validation을 위해 Request DTO를 사용하는 것이 좋다.

Q. DTO 검수에서 가장 중요한 것은?
A. Request / Response 분리, Entity 직접 노출 금지, 민감정보 제거, Validation 적용, 응답 구조 일관성이다.

Q. ApiResponse 검수에서 가장 중요한 것은?
A. 성공 / 실패 응답 구조가 통일되어 있고 errorCode, message, data 기준이 명확한지 확인하는 것이다.

Q. Spring Boot Part03 다음에는 뭐가 좋아?
A. Validation & Binding 문서가 이어지는 것이 좋다.
