# Spring Boot Part04 - Validation & Binding

---

# 1. Validation Overview

## 1.1 Validation Purpose

### [개념]

Validation은 Client 요청 값이 Application에서 처리 가능한 형식과 제약 조건을 만족하는지 확인하는 과정이다.

Spring Boot에서는 Bean Validation과 `@Valid`를 사용해 Request DTO 검증을 수행한다.

Validation은 API Boundary에서 잘못된 입력을 조기에 차단하는 역할을 한다.

Validation의 목적:

- 잘못된 Request 차단
- Request DTO 입력 제약 명확화
- Controller 진입 시 기본 형식 검증
- Service Business Logic 보호
- Error Response 일관화
- Frontend 입력 오류 처리 지원
- Backend Agent Request 검증 기준 제공
- Review Agent Validation 누락 탐지 기준 제공

---

### [핵심]

Validation 핵심 키워드:

- Bean Validation
- `@Valid`
- `@Validated`
- Request DTO
- Binding
- Constraint
- Validation Annotation
- MethodArgumentNotValidException
- ConstraintViolationException
- BindException
- GlobalExceptionHandler
- Field Error
- ErrorCode
- Error Response

Validation 위치:

| 검증 종류     | 위치               | 예                             |
| ------------- | ------------------ | ------------------------------ |
| 형식 검증     | Request DTO        | 빈 값, 길이, 이메일 형식       |
| 타입 검증     | Binding 단계       | Long, Integer, LocalDate 변환  |
| 비즈니스 검증 | Service            | 중복 이메일, 권한, 상태 전환   |
| 보안 검증     | Security / Service | 인증 사용자, Role, 소유자 검증 |

핵심 규칙:

- Request DTO에 Validation Annotation을 적용한다.
- Controller Parameter에 `@Valid`를 붙인다.
- 형식 검증은 Request DTO에서 처리한다.
- 비즈니스 검증은 Service에서 처리한다.
- Validation 실패는 GlobalExceptionHandler에서 공통 응답으로 변환한다.
- Entity가 아닌 Request DTO를 검증한다.
- Controller에서 Validation Error를 직접 조립하지 않는다.

---

### [실무]

Request DTO:

```java
public record SignUpRequest(
        @NotBlank
        @Email
        String email,

        @NotBlank
        @Size(min = 8, max = 30)
        String password,

        @NotBlank
        @Size(min = 2, max = 20)
        String nickname
) {
}
```

Controller:

```java
@PostMapping("/signup")
public ApiResponse<UserResponse> signUp(
        @Valid @RequestBody SignUpRequest request
) {
    return ApiResponse.success(userService.signUp(request));
}
```

Validation 실패 흐름:

```text
Client Request
→ JSON Binding
→ Request DTO
→ @Valid
→ Bean Validation
→ MethodArgumentNotValidException
→ GlobalExceptionHandler
→ ApiResponse Error
```

Service 비즈니스 검증:

```java
@Transactional
public UserResponse signUp(SignUpRequest request) {
    if (userRepository.existsByEmail(request.email())) {
        throw new BusinessException(ErrorCode.EMAIL_DUPLICATED);
    }

    User user = User.create(
            request.email(),
            passwordEncoder.encode(request.password()),
            request.nickname()
    );

    return UserResponse.from(userRepository.save(user));
}
```

권장:

- Request DTO에 기본 입력 검증을 둔다.
- Service에는 DB 조회가 필요한 비즈니스 검증을 둔다.
- Validation Error는 ErrorCode와 함께 응답한다.
- Field Error 포함 여부는 프로젝트 규칙으로 정한다.
- 사용자 메시지와 서버 로그 메시지를 구분한다.

---

### [FAQ]

Q. Validation은 왜 필요해?
A. 잘못된 입력을 API 경계에서 차단하고 Service Business Logic을 안전하게 유지하기 위해 필요하다.

Q. Validation은 Controller에서 해?
A. Controller에서 `@Valid`로 검증을 트리거하고 실제 제약 조건은 Request DTO에 작성한다.

Q. 비즈니스 검증도 DTO Validation으로 해?
A. 아니다. 중복 이메일, 권한, 상태 전환 같은 비즈니스 검증은 Service에서 처리한다.

Q. Validation 실패는 어디서 처리해?
A. GlobalExceptionHandler에서 Validation Exception을 잡아 공통 Error Response로 변환한다.

---

# 2. Bean Validation Annotation

## 2.1 Common Validation Annotation Rules

### [개념]

Bean Validation Annotation은 Request DTO 필드에 입력 제약 조건을 선언하는 Annotation이다.

Spring Boot 3.x 기준에서는 Jakarta Bean Validation을 사용한다.

Validation Annotation은 API 입력 조건을 코드에 명시하는 역할을 한다.

---

### [핵심]

주요 Annotation:

| Annotation         | 의미                       | 사용 예              |
| ------------------ | -------------------------- | -------------------- |
| `@NotNull`         | null 금지                  | 필수 객체, 숫자      |
| `@NotBlank`        | null, 빈 문자열, 공백 금지 | 이름, 제목, 비밀번호 |
| `@NotEmpty`        | null, empty 금지           | 문자열, 컬렉션       |
| `@Size`            | 길이 / 크기 제한           | 닉네임, 제목         |
| `@Email`           | 이메일 형식                | 이메일               |
| `@Pattern`         | 정규식 검증                | 전화번호, 코드       |
| `@Min`             | 최소값                     | 수량                 |
| `@Max`             | 최대값                     | 점수                 |
| `@Positive`        | 양수                       | 가격                 |
| `@PositiveOrZero`  | 0 이상                     | 재고                 |
| `@Past`            | 과거 날짜                  | 생년월일             |
| `@Future`          | 미래 날짜                  | 예약일               |
| `@FutureOrPresent` | 현재 또는 미래             | 시작일               |

핵심 규칙:

- 문자열 필수 입력은 `@NotBlank`를 우선 검토한다.
- 숫자 필수 입력은 `@NotNull`과 범위 Annotation을 조합한다.
- 이메일은 `@Email`과 `@NotBlank`를 함께 검토한다.
- 가격, 수량은 `@Positive`, `@PositiveOrZero`를 사용한다.
- 정규식은 너무 복잡하게 만들지 않는다.
- Validation 메시지는 일관된 정책으로 관리한다.

---

### [실무]

문자열 검증:

```java
public record PostCreateRequest(
        @NotBlank
        @Size(max = 100)
        String title,

        @NotBlank
        @Size(max = 5000)
        String content
) {
}
```

숫자 검증:

```java
public record ProductCreateRequest(
        @NotBlank
        String name,

        @NotNull
        @Positive
        Integer price,

        @NotNull
        @PositiveOrZero
        Integer stock
) {
}
```

이메일 검증:

```java
public record LoginRequest(
        @NotBlank
        @Email
        String email,

        @NotBlank
        String password
) {
}
```

날짜 검증:

```java
public record ReservationRequest(
        @NotNull
        @FutureOrPresent
        LocalDate reservationDate
) {
}
```

정규식 검증:

```java
public record PhoneUpdateRequest(
        @Pattern(regexp = "^010-\\d{4}-\\d{4}$")
        String phoneNumber
) {
}
```

주의:

```java
public record UserCreateRequest(
        @Email String email
) {
}
```

문제:

```text
@Email은 빈 문자열을 허용할 수 있음
필수 이메일이면 @NotBlank를 함께 사용
```

개선:

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

Q. `@NotNull`, `@NotBlank`, `@NotEmpty` 차이는?
A. `@NotNull`은 null만 금지하고, `@NotBlank`는 공백 문자열까지 금지하며, `@NotEmpty`는 null과 empty를 금지한다.

Q. 문자열 필수 값은 뭘 써?
A. 공백까지 막아야 하므로 보통 `@NotBlank`를 사용한다.

Q. 숫자 필수 값은 뭘 써?
A. `@NotNull`과 `@Positive`, `@Min`, `@Max` 같은 범위 검증을 조합한다.

Q. 이메일은 `@Email`만 쓰면 돼?
A. 필수 입력이면 `@NotBlank`와 `@Email`을 함께 사용하는 것이 좋다.

---

## 2.2 Validation Message Rules

### [개념]

Validation Message는 Request DTO 검증 실패 시 사용자 또는 Frontend에게 전달할 오류 메시지다.

Validation Message는 사용자 경험과 Error Response 일관성에 영향을 준다.

---

### [핵심]

Message 작성 기준:

- 짧고 명확하게 작성
- 사용자에게 노출 가능한 표현 사용
- 내부 구현 정보 노출 금지
- 필드명과 제약 조건을 이해 가능하게 작성
- 프로젝트 전체 톤 통일
- 다국어 필요 시 message source 검토
- Frontend 표시 메시지와 errorCode 역할 분리

예:

```java
@NotBlank(message = "제목은 필수입니다.")
@Size(max = 100, message = "제목은 100자 이하로 입력해야 합니다.")
String title
```

핵심 규칙:

- ErrorCode는 처리 기준이다.
- message는 사용자 표시 또는 안내 기준이다.
- 개발자용 상세 로그와 사용자 메시지를 분리한다.
- Validation Message를 과도하게 길게 작성하지 않는다.
- Field Error를 포함할지 프로젝트 규칙을 정한다.

---

### [실무]

DTO 메시지 예:

```java
public record PostCreateRequest(
        @NotBlank(message = "제목은 필수입니다.")
        @Size(max = 100, message = "제목은 100자 이하로 입력해야 합니다.")
        String title,

        @NotBlank(message = "내용은 필수입니다.")
        String content
) {
}
```

Error Response 예:

```json
{
  "success": false,
  "message": "요청 값이 올바르지 않습니다.",
  "data": null,
  "errorCode": "INVALID_REQUEST"
}
```

Field Error 포함 예:

```json
{
  "success": false,
  "message": "요청 값이 올바르지 않습니다.",
  "errorCode": "INVALID_REQUEST",
  "fieldErrors": [
    {
      "field": "title",
      "message": "제목은 필수입니다."
    }
  ]
}
```

권장:

```text
일반 사용자 메시지
→ 요청 값이 올바르지 않습니다.

Field Error
→ title: 제목은 필수입니다.

Server Log
→ MethodArgumentNotValidException details
```

주의:

```java
@NotBlank(message = "title field failed NotBlank validation at PostCreateRequest")
String title
```

문제:

- 사용자에게 부적합
- 내부 구현 정보 노출
- 메시지 톤 불일치

---

### [FAQ]

Q. Validation message는 꼭 작성해야 해?
A. 필수는 아니지만 사용자에게 명확한 오류 안내가 필요하면 작성하는 것이 좋다.

Q. Validation message와 errorCode는 같은 역할이야?
A. 아니다. errorCode는 Frontend 처리 기준이고 message는 사용자 안내 문구에 가깝다.

Q. Field Error를 응답에 포함해야 해?
A. 프로젝트 요구사항에 따라 정한다. Form 입력 화면에서는 포함하면 유용하다.

Q. 내부 예외 메시지를 그대로 보여줘도 돼?
A. 권장하지 않는다. 사용자 메시지와 서버 로그 메시지를 분리하는 것이 좋다.

---

# 3. `@Valid` and `@Validated`

## 3.1 `@Valid` Rules

### [개념]

`@Valid`는 Controller Method Parameter에 붙여 Request DTO의 Bean Validation을 실행하는 Annotation이다.

Request DTO에 Validation Annotation이 있어도 Controller Parameter에 `@Valid`가 없으면 검증이 실행되지 않을 수 있다.

---

### [핵심]

사용 위치:

```java
@PostMapping
public ApiResponse<PostResponse> createPost(
        @Valid @RequestBody PostCreateRequest request
) {
    return ApiResponse.success(postService.createPost(request));
}
```

적용 대상:

- `@RequestBody`
- `@ModelAttribute`
- Nested DTO
- Collection Element Validation
- Form Object

핵심 규칙:

- Request DTO 앞에 `@Valid`를 붙인다.
- DTO 내부 필드에 Validation Annotation을 붙인다.
- Nested DTO 검증이 필요하면 내부 필드에도 `@Valid`를 붙인다.
- Validation 실패는 Exception으로 처리한다.
- Controller에서 BindingResult로 우회하지 않는다.

---

### [실무]

기본 사용:

```java
@PostMapping("/posts")
public ApiResponse<PostResponse> createPost(
        @Valid @RequestBody PostCreateRequest request
) {
    return ApiResponse.success(postService.createPost(request));
}
```

`@ModelAttribute` 사용:

```java
@GetMapping("/posts/search")
public ApiResponse<Slice<PostResponse>> searchPosts(
        @Valid @ModelAttribute PostSearchRequest request,
        Pageable pageable
) {
    return ApiResponse.success(postService.searchPosts(request, pageable));
}
```

Nested DTO:

```java
public record OrderCreateRequest(
        @NotNull Long userId,
        @Valid
        List<OrderItemRequest> items
) {
}
```

```java
public record OrderItemRequest(
        @NotNull Long productId,
        @Positive Integer quantity
) {
}
```

Collection Validation:

```java
public record BulkDeleteRequest(
        @NotEmpty
        List<@NotNull Long> ids
) {
}
```

주의:

```java
@PostMapping("/posts")
public ApiResponse<PostResponse> createPost(
        @RequestBody PostCreateRequest request
) {
    return ApiResponse.success(postService.createPost(request));
}
```

문제:

```text
Request DTO에 @NotBlank가 있어도 @Valid가 없으면 검증이 실행되지 않을 수 있음
```

---

### [FAQ]

Q. `@Valid`는 어디에 붙여?
A. Controller Method에서 Request DTO 앞에 붙여 요청 검증을 트리거한다.

Q. DTO에 `@NotBlank`가 있으면 `@Valid` 없어도 돼?
A. 아니다. Controller Parameter에 `@Valid`를 붙여야 검증이 실행된다.

Q. Nested DTO도 자동으로 검증돼?
A. 내부 DTO 필드에 `@Valid`를 붙여야 중첩 객체 검증이 수행된다.

Q. List 내부 값도 검증할 수 있어?
A. 가능하다. `List<@NotNull Long>`처럼 Element Validation을 사용할 수 있다.

---

## 3.2 `@Validated` Rules

### [개념]

`@Validated`는 Spring에서 제공하는 Validation Annotation이다.

`@Validated`는 Method Parameter Validation, Validation Group, Class Level Validation에 사용할 수 있다.

일반 Request DTO 검증은 `@Valid`를 우선 사용하고, Group 검증이나 Method Validation이 필요하면 `@Validated`를 검토한다.

---

### [핵심]

`@Valid`와 `@Validated` 비교:

| 구분              | `@Valid`           | `@Validated` |
| ----------------- | ------------------ | ------------ |
| 제공              | Jakarta Validation | Spring       |
| 기본 DTO 검증     | 적합               | 가능         |
| Validation Group  | 제한적             | 지원         |
| Method Validation | 제한적             | 적합         |
| 사용 난이도       | 낮음               | 중간         |
| Foundation 권장   | 우선 사용          | 필요 시 사용 |

사용 상황:

- Validation Group
- Service Method Parameter Validation
- Controller Class Level Validation
- PathVariable / RequestParam 직접 검증
- 복잡한 검증 그룹 분리

핵심 규칙:

- 단순 Request DTO 검증은 `@Valid`를 사용한다.
- Group 검증이 필요하면 `@Validated`를 사용한다.
- Method Parameter Validation에는 class level `@Validated`가 필요할 수 있다.
- 너무 복잡한 Group 검증은 DTO 분리로 대체 가능한지 검토한다.

---

### [실무]

RequestParam 검증:

```java
@RestController
@RequestMapping("/api/posts")
@Validated
public class PostController {

    @GetMapping
    public ApiResponse<List<PostResponse>> getPosts(
            @RequestParam @Positive Integer size
    ) {
        return ApiResponse.success(postService.getPosts(size));
    }
}
```

Validation Group 예:

```java
public interface CreateGroup {
}

public interface UpdateGroup {
}
```

```java
public record UserRequest(
        @NotBlank(groups = CreateGroup.class)
        String email,

        @NotBlank(groups = {CreateGroup.class, UpdateGroup.class})
        String nickname
) {
}
```

Controller:

```java
@PostMapping
public ApiResponse<UserResponse> createUser(
        @Validated(CreateGroup.class) @RequestBody UserRequest request
) {
    return ApiResponse.success(userService.createUser(request));
}
```

주의:

```text
Create / Update 검증 조건이 크게 다름
→ Validation Group보다 CreateRequest / UpdateRequest DTO 분리가 더 단순할 수 있음
```

권장 대안:

```java
public record UserCreateRequest(
        @NotBlank String email,
        @NotBlank String nickname
) {
}
```

```java
public record UserUpdateRequest(
        @NotBlank String nickname
) {
}
```

---

### [FAQ]

Q. `@Valid`와 `@Validated` 차이는?
A. `@Valid`는 기본 Bean Validation에 적합하고, `@Validated`는 Spring의 Validation Group과 Method Validation에 유용하다.

Q. 보통은 뭘 쓰면 돼?
A. 일반 Request DTO 검증은 `@Valid`를 우선 사용한다.

Q. Validation Group은 언제 써?
A. 같은 DTO를 생성 / 수정 등 다른 검증 조건으로 사용해야 할 때 쓴다.

Q. Validation Group보다 DTO 분리가 나을 때도 있어?
A. 맞다. 생성 / 수정 조건이 많이 다르면 DTO를 분리하는 것이 더 명확하다.

---

# 4. Request Binding Overview

## 4.1 Binding Purpose

### [개념]

Binding은 HTTP Request 데이터를 Controller Parameter나 Request DTO로 변환하는 과정이다.

Spring Boot는 Request Body, Query String, Path Variable, Header 값을 Java 타입으로 Binding한다.

Binding은 Validation보다 먼저 수행된다.

---

### [핵심]

Binding 대상:

- `@RequestBody`
- `@ModelAttribute`
- `@RequestParam`
- `@PathVariable`
- `@RequestHeader`
- Pageable
- Date / Time
- Enum
- Collection

Binding 흐름:

```text
HTTP Request
→ HandlerMapping
→ Controller Method 선택
→ Parameter Binding
→ Type Conversion
→ Validation
→ Controller Method 실행
```

핵심 규칙:

- JSON Body는 `@RequestBody`로 Binding한다.
- Query String은 `@RequestParam` 또는 `@ModelAttribute`로 Binding한다.
- URL Path 값은 `@PathVariable`로 Binding한다.
- Header 값은 `@RequestHeader`로 Binding한다.
- Binding 실패는 400 Bad Request로 이어질 수 있다.
- DTO 필드명과 JSON 필드명은 일치시킨다.
- 타입 변환 가능성을 고려한다.

---

### [실무]

JSON Binding:

```json
{
  "title": "Spring Boot",
  "content": "Validation"
}
```

```java
public record PostCreateRequest(
        String title,
        String content
) {
}
```

```java
@PostMapping
public ApiResponse<PostResponse> createPost(
        @RequestBody PostCreateRequest request
) {
    return ApiResponse.success(postService.createPost(request));
}
```

Query Binding:

```text
GET /api/posts/search?keyword=spring&category=backend
```

```java
public record PostSearchRequest(
        String keyword,
        String category
) {
}
```

```java
@GetMapping("/search")
public ApiResponse<Slice<PostResponse>> searchPosts(
        @ModelAttribute PostSearchRequest request,
        Pageable pageable
) {
    return ApiResponse.success(postService.searchPosts(request, pageable));
}
```

PathVariable Binding:

```text
GET /api/posts/10
```

```java
@GetMapping("/{postId}")
public ApiResponse<PostResponse> getPost(
        @PathVariable Long postId
) {
    return ApiResponse.success(postService.getPost(postId));
}
```

Binding 실패 원인:

```text
JSON 필드명 불일치
→ DTO 값 null

PathVariable 타입 불일치
→ 400 Bad Request

RequestParam 날짜 포맷 불일치
→ 400 Bad Request

Content-Type 누락
→ RequestBody Binding 실패
```

---

### [FAQ]

Q. Binding은 뭐야?
A. HTTP Request 데이터를 Controller Parameter나 Request DTO로 변환하는 과정이다.

Q. Binding과 Validation은 뭐가 달라?
A. Binding은 요청 값을 Java 객체로 변환하는 과정이고, Validation은 변환된 값이 제약 조건을 만족하는지 검사하는 과정이다.

Q. Binding 실패도 400이 나?
A. 맞다. 타입 변환 실패, JSON 구조 오류, 날짜 포맷 오류 등은 400 Bad Request로 이어질 수 있다.

Q. JSON 필드명과 DTO 필드명이 다르면?
A. 값이 null로 들어오거나 Binding이 실패할 수 있다.

---

## 4.2 `@RequestBody` Binding Rules

### [개념]

`@RequestBody` Binding은 HTTP Request Body의 JSON 데이터를 Request DTO로 변환하는 과정이다.

Spring Boot는 Jackson MessageConverter를 사용해 JSON을 Java 객체로 변환한다.

---

### [핵심]

필수 조건:

- HTTP Body에 JSON 존재
- `Content-Type: application/json`
- Controller Parameter에 `@RequestBody`
- DTO 필드명과 JSON 필드명 일치
- DTO 타입 변환 가능
- Jackson이 생성 가능한 DTO 구조

기본 예:

```java
@PostMapping
public ApiResponse<PostResponse> createPost(
        @Valid @RequestBody PostCreateRequest request
) {
    return ApiResponse.success(postService.createPost(request));
}
```

핵심 규칙:

- Entity 대신 Request DTO를 사용한다.
- JSON Body 요청에는 `@RequestBody`를 붙인다.
- Request DTO에는 `@Valid`를 함께 적용한다.
- Content-Type을 확인한다.
- 필드명 불일치를 주의한다.
- 타입 불일치를 주의한다.
- GET 요청에는 RequestBody를 지양한다.

---

### [실무]

정상 요청:

```json
{
  "title": "Spring Boot",
  "content": "RequestBody Binding"
}
```

DTO:

```java
public record PostCreateRequest(
        @NotBlank String title,
        @NotBlank String content
) {
}
```

Controller:

```java
@PostMapping("/posts")
public ApiResponse<PostResponse> createPost(
        @Valid @RequestBody PostCreateRequest request
) {
    return ApiResponse.success(postService.createPost(request));
}
```

필드명 불일치:

```json
{
  "postTitle": "Spring Boot",
  "postContent": "RequestBody Binding"
}
```

결과:

```text
request.title() == null
request.content() == null
```

해결:

```json
{
  "title": "Spring Boot",
  "content": "RequestBody Binding"
}
```

또는 외부 필드명 매핑:

```java
public record PostCreateRequest(
        @JsonProperty("postTitle")
        String title,

        @JsonProperty("postContent")
        String content
) {
}
```

주의:

```java
@PostMapping("/posts")
public ApiResponse<PostResponse> createPost(
        PostCreateRequest request
) {
    ...
}
```

문제:

```text
@RequestBody 누락
→ JSON Body가 DTO에 Binding되지 않을 수 있음
```

---

### [FAQ]

Q. `@RequestBody` Binding은 언제 써?
A. JSON Body 요청을 Request DTO로 변환할 때 사용한다.

Q. RequestBody 값이 null로 들어오면 뭘 확인해?
A. Content-Type, `@RequestBody` 누락, JSON 필드명, DTO 구조, Jackson 변환 오류를 확인한다.

Q. JSON 필드명이 DTO와 다르면 어떻게 해?
A. 필드명을 맞추거나 `@JsonProperty`를 사용한다.

Q. GET 요청에도 `@RequestBody`를 써?
A. 권장하지 않는다. Query Parameter나 `@ModelAttribute`를 사용한다.

---

## 4.3 `@ModelAttribute` Binding Rules

### [개념]

`@ModelAttribute` Binding은 Query Parameter 또는 Form Data를 DTO 객체로 변환하는 과정이다.

GET 검색 조건, 필터 조건, Form 요청 처리에 적합하다.

---

### [핵심]

사용 상황:

- GET 검색 조건 DTO
- Query Parameter 복합 Binding
- Form Data Binding
- 필터 조건 DTO
- Pagination 조건과 조합

예:

```java
@GetMapping("/search")
public ApiResponse<Slice<PostResponse>> searchPosts(
        @ModelAttribute PostSearchRequest request,
        Pageable pageable
) {
    return ApiResponse.success(postService.searchPosts(request, pageable));
}
```

요청:

```text
GET /api/posts/search?keyword=spring&category=backend
```

DTO:

```java
public record PostSearchRequest(
        String keyword,
        String category
) {
}
```

핵심 규칙:

- Query Parameter가 많으면 `@ModelAttribute`를 사용한다.
- GET 검색 API에 적합하다.
- JSON Body에는 `@RequestBody`를 사용한다.
- DTO 필드명과 Query Parameter 이름을 일치시킨다.
- Date / Enum Binding을 주의한다.
- Validation이 필요하면 `@Valid @ModelAttribute`를 사용한다.

---

### [실무]

검색 DTO:

```java
public record FestivalSearchRequest(
        String keyword,
        String regionCode,
        String themeCode,
        @DateTimeFormat(pattern = "yyyy-MM-dd")
        LocalDate startDate,
        @DateTimeFormat(pattern = "yyyy-MM-dd")
        LocalDate endDate
) {
}
```

Controller:

```java
@GetMapping("/festivals/search")
public ApiResponse<Slice<FestivalResponse>> searchFestivals(
        @ModelAttribute FestivalSearchRequest request,
        Pageable pageable
) {
    return ApiResponse.success(
            festivalService.searchFestivals(request, pageable)
    );
}
```

요청:

```text
GET /api/festivals/search?keyword=music&regionCode=11&startDate=2026-07-01
```

`@RequestParam` 다수 사용:

```java
@GetMapping("/search")
public ApiResponse<?> search(
        @RequestParam String keyword,
        @RequestParam String regionCode,
        @RequestParam String themeCode,
        @RequestParam LocalDate startDate,
        @RequestParam LocalDate endDate
) {
    ...
}
```

개선:

```java
@GetMapping("/search")
public ApiResponse<?> search(
        @ModelAttribute FestivalSearchRequest request
) {
    ...
}
```

주의:

```text
Query Parameter 이름
→ DTO 필드명과 일치 필요

날짜 문자열
→ @DateTimeFormat 검토

Enum 문자열
→ enum name 또는 converter 기준 필요
```

---

### [FAQ]

Q. `@ModelAttribute`는 언제 써?
A. Query Parameter나 Form 데이터를 객체로 Binding할 때 사용한다.

Q. 검색 조건이 많으면 어떻게 해?
A. `@RequestParam`을 여러 개 쓰기보다 SearchRequest DTO와 `@ModelAttribute`를 사용하는 것이 좋다.

Q. `@ModelAttribute`에 `@Valid`를 붙일 수 있어?
A. 가능하다. Query Parameter 기반 검색 조건도 검증할 수 있다.

Q. JSON Body도 `@ModelAttribute`로 받아?
A. 아니다. JSON Body는 `@RequestBody`로 받는다.

---

## 4.4 `@PathVariable` and `@RequestParam` Binding Rules

### [개념]

`@PathVariable`은 URL Path 일부를 Controller Parameter로 Binding한다.

`@RequestParam`은 Query String 값을 Controller Parameter로 Binding한다.

둘은 목적이 다르며 혼용하면 Mapping과 Binding 오류가 발생할 수 있다.

---

### [핵심]

비교:

| 구분    | `@PathVariable` | `@RequestParam`         |
| ------- | --------------- | ----------------------- |
| 위치    | URL Path        | Query String            |
| 목적    | Resource 식별   | 검색 / 필터 / 옵션      |
| 예      | `/posts/10`     | `/posts?keyword=spring` |
| 필수성  | 보통 필수       | 선택 가능               |
| 사용 값 | postId, userId  | keyword, page, size     |

`@PathVariable` 예:

```java
@GetMapping("/{postId}")
public ApiResponse<PostResponse> getPost(
        @PathVariable Long postId
) {
    return ApiResponse.success(postService.getPost(postId));
}
```

`@RequestParam` 예:

```java
@GetMapping
public ApiResponse<List<PostResponse>> getPosts(
        @RequestParam(required = false) String keyword
) {
    return ApiResponse.success(postService.getPosts(keyword));
}
```

핵심 규칙:

- Resource ID는 `@PathVariable`을 사용한다.
- 검색 / 필터 값은 `@RequestParam`을 사용한다.
- PathVariable 이름과 Parameter 이름을 일치시킨다.
- Optional 검색 조건은 `required = false`를 사용한다.
- 기본 값은 `defaultValue`를 사용한다.
- 타입 변환 실패를 주의한다.

---

### [실무]

PathVariable 정상:

```text
GET /api/posts/10
```

```java
@GetMapping("/{postId}")
public ApiResponse<PostResponse> getPost(
        @PathVariable Long postId
) {
    return ApiResponse.success(postService.getPost(postId));
}
```

PathVariable 이름 불일치:

```java
@GetMapping("/{postId}")
public ApiResponse<PostResponse> getPost(
        @PathVariable Long id
) {
    return ApiResponse.success(postService.getPost(id));
}
```

안전한 방식:

```java
@GetMapping("/{postId}")
public ApiResponse<PostResponse> getPost(
        @PathVariable("postId") Long id
) {
    return ApiResponse.success(postService.getPost(id));
}
```

RequestParam 선택 값:

```java
@GetMapping("/search")
public ApiResponse<List<PostResponse>> searchPosts(
        @RequestParam(required = false) String keyword,
        @RequestParam(defaultValue = "10") int size
) {
    return ApiResponse.success(postService.searchPosts(keyword, size));
}
```

타입 오류:

```text
GET /api/posts/abc
```

```java
@PathVariable Long postId
```

결과:

```text
400 Bad Request
```

---

### [FAQ]

Q. `@PathVariable`과 `@RequestParam` 차이는?
A. `@PathVariable`은 URL 경로 일부를 받고 `@RequestParam`은 query string 값을 받는다.

Q. Resource ID는 뭘로 받아?
A. 일반적으로 `@PathVariable`을 사용한다.

Q. 검색 키워드는 뭘로 받아?
A. 일반적으로 `@RequestParam` 또는 조건이 많으면 `@ModelAttribute`를 사용한다.

Q. PathVariable 타입이 안 맞으면 어떻게 돼?
A. 타입 변환 실패로 400 Bad Request가 발생할 수 있다.

---

# 5. Type Conversion

## 5.1 Primitive and Wrapper Binding Rules

### [개념]

Type Conversion은 HTTP Request의 문자열 값을 Java 타입으로 변환하는 과정이다.

PathVariable, RequestParam, ModelAttribute Binding에서는 문자열 입력이 Java 타입으로 변환된다.

---

### [핵심]

주요 변환 대상:

- String
- Integer
- Long
- Boolean
- BigDecimal
- LocalDate
- LocalDateTime
- Enum
- List
- Pageable

예:

```text
GET /api/products?minPrice=1000&active=true
```

```java
@GetMapping
public ApiResponse<List<ProductResponse>> getProducts(
        @RequestParam Integer minPrice,
        @RequestParam Boolean active
) {
    ...
}
```

핵심 규칙:

- Query String은 기본적으로 문자열이다.
- Java 타입 변환이 실패하면 400 Bad Request가 발생할 수 있다.
- Optional 값은 Wrapper Type을 사용한다.
- 필수 값은 Validation과 함께 사용한다.
- 숫자 값에는 범위 검증을 적용한다.
- Boolean 값은 true / false 표현을 명확히 한다.

---

### [실무]

Wrapper Type 권장:

```java
@GetMapping("/products")
public ApiResponse<List<ProductResponse>> getProducts(
        @RequestParam(required = false) Integer minPrice,
        @RequestParam(required = false) Integer maxPrice
) {
    return ApiResponse.success(productService.getProducts(minPrice, maxPrice));
}
```

Primitive Type 주의:

```java
@GetMapping("/products")
public ApiResponse<List<ProductResponse>> getProducts(
        @RequestParam(required = false) int minPrice
) {
    ...
}
```

문제:

```text
required=false인데 primitive int는 null 표현 불가
기본값 0과 미입력 구분 어려움
```

개선:

```java
@RequestParam(required = false) Integer minPrice
```

기본 값 사용:

```java
@GetMapping("/products")
public ApiResponse<List<ProductResponse>> getProducts(
        @RequestParam(defaultValue = "0") int page,
        @RequestParam(defaultValue = "10") int size
) {
    ...
}
```

잘못된 요청:

```text
GET /api/products?minPrice=abc
```

결과:

```text
Integer 변환 실패
→ 400 Bad Request
```

---

### [FAQ]

Q. RequestParam 숫자 값은 자동 변환돼?
A. 가능하다. 문자열 query parameter가 Integer, Long 같은 타입으로 변환된다.

Q. 숫자 변환이 실패하면 어떻게 돼?
A. 400 Bad Request가 발생할 수 있다.

Q. Optional 숫자 파라미터는 int로 받아도 돼?
A. 권장하지 않는다. null 표현이 가능한 Integer 같은 Wrapper Type이 좋다.

Q. defaultValue를 쓰면 required=false가 필요해?
A. defaultValue가 있으면 값이 없을 때 기본값이 사용되므로 보통 required 설정이 필요 없다.

---

## 5.2 Date Time Binding Rules

### [개념]

Date Time Binding은 Request의 날짜 / 시간 문자열을 `LocalDate`, `LocalDateTime` 같은 Java 시간 타입으로 변환하는 과정이다.

날짜 포맷이 맞지 않으면 Binding 실패가 발생한다.

---

### [핵심]

주요 타입:

- `LocalDate`
- `LocalDateTime`
- `ZonedDateTime`
- `Instant`

Binding Annotation:

- `@DateTimeFormat`
- `@JsonFormat`

사용 위치:

| Annotation        | 사용 위치                                     | 목적                |
| ----------------- | --------------------------------------------- | ------------------- |
| `@DateTimeFormat` | Query Parameter, PathVariable, ModelAttribute | 요청 문자열 Binding |
| `@JsonFormat`     | JSON Body, Response Serialization             | JSON 날짜 포맷      |

핵심 규칙:

- Query Parameter 날짜는 `@DateTimeFormat`을 검토한다.
- JSON Body 날짜는 기본 ISO 형식을 우선 사용한다.
- Response 날짜 포맷은 프로젝트 기준으로 통일한다.
- LocalDate와 LocalDateTime을 목적에 맞게 구분한다.
- Timezone이 중요한 서비스는 기준을 명확히 한다.

---

### [실무]

Query Parameter 날짜:

```text
GET /api/festivals?startDate=2026-07-01&endDate=2026-07-31
```

DTO:

```java
public record FestivalSearchRequest(
        @DateTimeFormat(pattern = "yyyy-MM-dd")
        LocalDate startDate,

        @DateTimeFormat(pattern = "yyyy-MM-dd")
        LocalDate endDate
) {
}
```

Controller:

```java
@GetMapping("/festivals")
public ApiResponse<Slice<FestivalResponse>> getFestivals(
        @ModelAttribute FestivalSearchRequest request,
        Pageable pageable
) {
    return ApiResponse.success(festivalService.getFestivals(request, pageable));
}
```

JSON Body 날짜:

```json
{
  "reservationDate": "2026-07-03"
}
```

DTO:

```java
public record ReservationRequest(
        @NotNull
        LocalDate reservationDate
) {
}
```

Response 포맷:

```java
public record FestivalResponse(
        Long festivalId,
        String title,
        @JsonFormat(pattern = "yyyy-MM-dd")
        LocalDate startDate
) {
}
```

잘못된 날짜 요청:

```text
GET /api/festivals?startDate=2026/07/01
```

결과:

```text
LocalDate Binding 실패
→ 400 Bad Request
```

---

### [FAQ]

Q. Query Parameter 날짜는 어떻게 받아?
A. `LocalDate`와 `@DateTimeFormat(pattern = "yyyy-MM-dd")`를 사용할 수 있다.

Q. `@DateTimeFormat`과 `@JsonFormat` 차이는?
A. `@DateTimeFormat`은 요청 파라미터 Binding에 주로 쓰고, `@JsonFormat`은 JSON 직렬화 / 역직렬화 포맷에 사용한다.

Q. 날짜 포맷이 틀리면 어떻게 돼?
A. Binding 실패로 400 Bad Request가 발생할 수 있다.

Q. 날짜를 String으로 받는 게 더 편하지 않아?
A. 단기적으로 편하지만 검증과 타입 안정성이 떨어진다. 날짜 타입을 사용하는 것이 좋다.

---

## 5.3 Enum Binding Rules

### [개념]

Enum Binding은 Request 문자열 값을 Java enum 타입으로 변환하는 과정이다.

Spring Boot는 기본적으로 문자열과 enum name이 일치하면 Binding할 수 있다.

---

### [핵심]

Enum 예:

```java
public enum PostCategory {
    BACKEND,
    FRONTEND,
    AI
}
```

RequestParam:

```java
@GetMapping("/posts")
public ApiResponse<List<PostResponse>> getPosts(
        @RequestParam PostCategory category
) {
    return ApiResponse.success(postService.getPosts(category));
}
```

요청:

```text
GET /api/posts?category=BACKEND
```

핵심 규칙:

- 기본 Binding은 enum name 기준이다.
- 대소문자 불일치에 주의한다.
- 사용자 입력 값과 enum name을 직접 결합할지 검토한다.
- code 값이 따로 있으면 Converter를 검토한다.
- 잘못된 enum 값은 400 Bad Request가 발생할 수 있다.
- API 문서에 허용 enum 값을 명시한다.

---

### [실무]

기본 enum Binding:

```java
public enum FestivalTheme {
    MUSIC,
    FOOD,
    CULTURE
}
```

```java
public record FestivalSearchRequest(
        FestivalTheme theme
) {
}
```

요청:

```text
GET /api/festivals?theme=MUSIC
```

잘못된 요청:

```text
GET /api/festivals?theme=music
```

결과:

```text
기본 설정에서는 enum name 불일치로 400 Bad Request 가능
```

code 기반 enum:

```java
public enum FestivalTheme {
    MUSIC("music"),
    FOOD("food"),
    CULTURE("culture");

    private final String code;

    FestivalTheme(String code) {
        this.code = code;
    }

    public String getCode() {
        return code;
    }
}
```

code 기반 Binding은 별도 Converter를 검토한다.

Foundation 기준:

```text
단순 프로젝트
→ enum name 기반 Binding

외부 노출 API / 코드 값 필요
→ code 기반 Converter 검토
```

---

### [FAQ]

Q. enum은 RequestParam으로 바로 받을 수 있어?
A. 가능하다. 기본적으로 요청 문자열이 enum name과 일치해야 한다.

Q. enum 대소문자가 다르면 어떻게 돼?
A. 기본 Binding에서는 변환 실패로 400 Bad Request가 발생할 수 있다.

Q. enum code 값으로 받고 싶으면?
A. 별도 Converter를 구현하거나 문자열로 받은 뒤 Service에서 변환하는 방식을 검토한다.

Q. enum 허용 값은 어디에 써?
A. API 문서와 Retrieval Queries에 명확히 포함하는 것이 좋다.

---

# 6. Validation Error Handling

## 6.1 Validation Exception Types

### [개념]

Validation Exception은 Binding 또는 Validation 실패 시 Spring Boot에서 발생하는 예외다.

Validation Exception을 GlobalExceptionHandler에서 처리하면 Error Response를 일관화할 수 있다.

---

### [핵심]

주요 예외:

| 예외                                      | 발생 상황                                   |
| ----------------------------------------- | ------------------------------------------- |
| `MethodArgumentNotValidException`         | `@RequestBody` + `@Valid` 검증 실패         |
| `BindException`                           | `@ModelAttribute` Binding / Validation 실패 |
| `ConstraintViolationException`            | Method Parameter Validation 실패            |
| `MethodArgumentTypeMismatchException`     | PathVariable / RequestParam 타입 변환 실패  |
| `HttpMessageNotReadableException`         | JSON Body 파싱 실패                         |
| `MissingServletRequestParameterException` | 필수 RequestParam 누락                      |

핵심 규칙:

- Validation Exception을 개별 Controller에서 처리하지 않는다.
- GlobalExceptionHandler에서 공통 처리한다.
- ErrorCode는 `INVALID_REQUEST` 또는 세분화된 코드를 사용한다.
- 사용자 메시지는 안전하게 작성한다.
- Field Error 포함 여부를 정한다.
- 서버 로그에는 상세 예외 정보를 남긴다.

---

### [실무]

GlobalExceptionHandler 예:

```java
@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(MethodArgumentNotValidException.class)
    public ApiResponse<Void> handleMethodArgumentNotValid(
            MethodArgumentNotValidException exception
    ) {
        return ApiResponse.fail(
                "INVALID_REQUEST",
                "요청 값이 올바르지 않습니다."
        );
    }

    @ExceptionHandler(MethodArgumentTypeMismatchException.class)
    public ApiResponse<Void> handleTypeMismatch(
            MethodArgumentTypeMismatchException exception
    ) {
        return ApiResponse.fail(
                "INVALID_TYPE",
                "요청 값의 타입이 올바르지 않습니다."
        );
    }

    @ExceptionHandler(HttpMessageNotReadableException.class)
    public ApiResponse<Void> handleMessageNotReadable(
            HttpMessageNotReadableException exception
    ) {
        return ApiResponse.fail(
                "INVALID_JSON",
                "요청 본문 형식이 올바르지 않습니다."
        );
    }
}
```

Field Error 추출 예:

```java
@ExceptionHandler(MethodArgumentNotValidException.class)
public ApiResponse<List<FieldErrorResponse>> handleValidationException(
        MethodArgumentNotValidException exception
) {
    List<FieldErrorResponse> fieldErrors = exception.getBindingResult()
            .getFieldErrors()
            .stream()
            .map(error -> new FieldErrorResponse(
                    error.getField(),
                    error.getDefaultMessage()
            ))
            .toList();

    return ApiResponse.fail(
            "INVALID_REQUEST",
            "요청 값이 올바르지 않습니다.",
            fieldErrors
    );
}
```

FieldErrorResponse:

```java
public record FieldErrorResponse(
        String field,
        String message
) {
}
```

---

### [FAQ]

Q. Validation 실패 시 어떤 예외가 발생해?
A. `@RequestBody @Valid` 실패는 주로 MethodArgumentNotValidException이 발생한다.

Q. Query Parameter 타입 변환 실패는 어떤 예외야?
A. MethodArgumentTypeMismatchException이 발생할 수 있다.

Q. JSON 형식이 깨지면 어떤 예외야?
A. HttpMessageNotReadableException이 발생할 수 있다.

Q. Validation 예외는 어디서 처리해?
A. GlobalExceptionHandler에서 공통 처리하는 것이 좋다.

---

## 6.2 Field Error Response Rules

### [개념]

Field Error Response는 어떤 필드가 어떤 이유로 검증에 실패했는지 Client에게 전달하는 응답 구조다.

Form 입력 화면에서는 Field Error가 Frontend UX에 유용하다.

---

### [핵심]

Field Error 구성 요소:

- field
- message
- rejectedValue
- code

기본 구조:

```json
{
  "field": "email",
  "message": "이메일 형식이 올바르지 않습니다."
}
```

ApiResponse 포함 예:

```json
{
  "success": false,
  "message": "요청 값이 올바르지 않습니다.",
  "errorCode": "INVALID_REQUEST",
  "data": [
    {
      "field": "email",
      "message": "이메일 형식이 올바르지 않습니다."
    }
  ]
}
```

핵심 규칙:

- field는 DTO 필드명을 사용한다.
- message는 사용자에게 노출 가능한 문구로 작성한다.
- rejectedValue는 민감정보일 수 있으므로 노출 주의한다.
- password 같은 필드의 입력값은 절대 반환하지 않는다.
- Field Error 포함 여부는 프로젝트 규칙으로 통일한다.

---

### [실무]

FieldErrorResponse:

```java
public record FieldErrorResponse(
        String field,
        String message
) {
}
```

ApiResponse 확장 예:

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

    public static <T> ApiResponse<T> fail(
            String errorCode,
            String message,
            T data
    ) {
        return new ApiResponse<>(false, message, data, errorCode);
    }
}
```

Handler:

```java
@ExceptionHandler(MethodArgumentNotValidException.class)
public ApiResponse<List<FieldErrorResponse>> handleValidationException(
        MethodArgumentNotValidException exception
) {
    List<FieldErrorResponse> errors = exception.getBindingResult()
            .getFieldErrors()
            .stream()
            .map(error -> new FieldErrorResponse(
                    error.getField(),
                    error.getDefaultMessage()
            ))
            .toList();

    return ApiResponse.fail(
            "INVALID_REQUEST",
            "요청 값이 올바르지 않습니다.",
            errors
    );
}
```

주의:

```java
public record FieldErrorResponse(
        String field,
        Object rejectedValue,
        String message
) {
}
```

위험:

```text
password, token, personal data가 rejectedValue로 노출될 수 있음
```

권장:

```text
rejectedValue 제외
또는 민감 필드 마스킹
```

---

### [FAQ]

Q. Field Error는 꼭 응답해야 해?
A. 필수는 아니지만 Form 입력 화면에서는 어떤 필드가 잘못됐는지 알려주기 위해 유용하다.

Q. rejectedValue를 응답에 포함해도 돼?
A. 민감정보 노출 위험이 있어 권장하지 않는다.

Q. password 검증 실패 시 입력한 password를 돌려줘도 돼?
A. 절대 안 된다. password, token 같은 민감정보는 응답에 포함하지 않는다.

Q. Field Error의 field 이름은 무엇을 써?
A. 일반적으로 Request DTO 필드명을 사용한다.

---

# 7. Binding Troubleshooting

## 7.1 RequestBody Binding Problem

### [개념]

RequestBody Binding Problem은 JSON Body가 Request DTO로 제대로 변환되지 않는 문제다.

값이 null로 들어오거나, JSON 파싱 오류가 발생하거나, 타입 변환 실패가 발생할 수 있다.

---

### [핵심]

주요 원인:

- `@RequestBody` 누락
- Content-Type 누락
- JSON 문법 오류
- JSON 필드명 불일치
- DTO 필드 타입 불일치
- record 생성자 Binding 문제
- Jackson 변환 오류
- 날짜 형식 불일치
- enum 값 불일치
- 중첩 객체 구조 불일치

Debug Flow:

```text
Request Payload 확인
→ Content-Type 확인
→ @RequestBody 확인
→ JSON 문법 확인
→ DTO Field Name 확인
→ DTO Field Type 확인
→ Date / Enum Format 확인
→ Jackson Error 확인
→ Validation Error 확인
```

---

### [실무]

문제 1:

```java
@PostMapping("/posts")
public ApiResponse<PostResponse> createPost(
        PostCreateRequest request
) {
    ...
}
```

원인:

```text
@RequestBody 누락
```

수정:

```java
@PostMapping("/posts")
public ApiResponse<PostResponse> createPost(
        @Valid @RequestBody PostCreateRequest request
) {
    ...
}
```

문제 2:

```json
{
  "post_title": "Spring Boot"
}
```

DTO:

```java
public record PostCreateRequest(
        String postTitle
) {
}
```

가능한 문제:

```text
JSON field: post_title
DTO field: postTitle
기본 naming strategy 불일치
```

수정:

```json
{
  "postTitle": "Spring Boot"
}
```

또는:

```java
public record PostCreateRequest(
        @JsonProperty("post_title")
        String postTitle
) {
}
```

문제 3:

```json
{
  "price": "abc"
}
```

DTO:

```java
public record ProductCreateRequest(
        Integer price
) {
}
```

결과:

```text
Integer 변환 실패
→ 400 Bad Request
```

---

### [FAQ]

Q. RequestBody 값이 null로 들어오면?
A. `@RequestBody` 누락, JSON 필드명 불일치, Content-Type, DTO 구조, Jackson 변환 오류를 확인한다.

Q. JSON 문법이 틀리면?
A. HttpMessageNotReadableException이 발생할 수 있다.

Q. 숫자 필드에 문자열을 보내면?
A. 타입 변환 실패로 400 Bad Request가 발생할 수 있다.

Q. snake_case JSON을 camelCase DTO로 받으려면?
A. `@JsonProperty` 또는 ObjectMapper naming strategy를 검토한다.

---

## 7.2 ModelAttribute Binding Problem

### [개념]

ModelAttribute Binding Problem은 Query Parameter 또는 Form Data가 DTO로 제대로 Binding되지 않는 문제다.

검색 조건 DTO, 날짜 필터, enum 필터에서 자주 발생한다.

---

### [핵심]

주요 원인:

- Query Parameter 이름 불일치
- DTO 필드명 불일치
- 날짜 포맷 불일치
- enum 값 불일치
- 타입 변환 실패
- 빈 문자열 처리 문제
- Pageable parameter 충돌
- `@ModelAttribute` 누락 또는 오해

Debug Flow:

```text
Request Query String 확인
→ DTO Field Name 확인
→ Controller @ModelAttribute 확인
→ Type Conversion 확인
→ DateTimeFormat 확인
→ Enum Value 확인
→ Pageable Parameter 확인
```

---

### [실무]

문제:

```text
GET /api/festivals?region_code=11
```

DTO:

```java
public record FestivalSearchRequest(
        String regionCode
) {
}
```

결과:

```text
regionCode == null
```

수정:

```text
GET /api/festivals?regionCode=11
```

날짜 문제:

```text
GET /api/festivals?startDate=2026/07/01
```

DTO:

```java
public record FestivalSearchRequest(
        @DateTimeFormat(pattern = "yyyy-MM-dd")
        LocalDate startDate
) {
}
```

결과:

```text
날짜 포맷 불일치
→ 400 Bad Request
```

수정:

```text
GET /api/festivals?startDate=2026-07-01
```

enum 문제:

```text
GET /api/posts?category=backend
```

Enum:

```java
public enum PostCategory {
    BACKEND,
    FRONTEND
}
```

결과:

```text
backend → BACKEND 변환 실패 가능
```

수정:

```text
GET /api/posts?category=BACKEND
```

또는 Converter 구현 검토.

---

### [FAQ]

Q. `@ModelAttribute` 값이 null이면 뭘 확인해?
A. Query Parameter 이름과 DTO 필드명이 일치하는지 확인한다.

Q. Query 날짜가 Binding 안 되면?
A. 날짜 문자열 형식과 `@DateTimeFormat` 설정을 확인한다.

Q. enum 검색 조건이 Binding 안 되면?
A. 요청 값이 enum name과 일치하는지 확인한다.

Q. snake_case query parameter를 camelCase DTO로 자동 Binding해?
A. 기본적으로 일치하지 않을 수 있으므로 이름을 맞추거나 별도 설정을 검토한다.

---

## 7.3 Validation Not Working Problem

### [개념]

Validation Not Working Problem은 DTO에 Validation Annotation을 작성했지만 검증이 실행되지 않는 문제다.

대부분 `@Valid` 누락, 의존성 누락, 적용 위치 오류가 원인이다.

---

### [핵심]

주요 원인:

- Controller Parameter에 `@Valid` 누락
- Validation Dependency 누락
- Entity에만 Validation 작성
- Request DTO가 아닌 다른 객체 검증
- Nested DTO에 `@Valid` 누락
- `@Validated` class level 누락
- Validation Group 적용 오류
- Controller에서 BindingResult로 흐름 우회
- 테스트에서 Validation 환경 미구성

Debug Flow:

```text
Validation Dependency 확인
→ DTO Annotation 확인
→ Controller @Valid 확인
→ Nested DTO @Valid 확인
→ @Validated 필요 여부 확인
→ GlobalExceptionHandler 확인
→ Test 환경 확인
```

---

### [실무]

문제:

```java
public record PostCreateRequest(
        @NotBlank String title
) {
}
```

```java
@PostMapping("/posts")
public ApiResponse<PostResponse> createPost(
        @RequestBody PostCreateRequest request
) {
    return ApiResponse.success(postService.createPost(request));
}
```

원인:

```text
@Valid 누락
```

수정:

```java
@PostMapping("/posts")
public ApiResponse<PostResponse> createPost(
        @Valid @RequestBody PostCreateRequest request
) {
    return ApiResponse.success(postService.createPost(request));
}
```

Nested DTO 문제:

```java
public record OrderCreateRequest(
        List<OrderItemRequest> items
) {
}
```

```java
public record OrderItemRequest(
        @NotNull Long productId,
        @Positive Integer quantity
) {
}
```

문제:

```text
OrderItemRequest 내부 Validation이 실행되지 않을 수 있음
```

수정:

```java
public record OrderCreateRequest(
        @Valid
        @NotEmpty
        List<OrderItemRequest> items
) {
}
```

Dependency 확인:

```gradle
implementation 'org.springframework.boot:spring-boot-starter-validation'
```

---

### [FAQ]

Q. DTO에 `@NotBlank`를 붙였는데 검증이 안 돼?
A. Controller Parameter에 `@Valid`가 있는지 확인해야 한다.

Q. Validation 의존성이 따로 필요해?
A. Spring Boot 프로젝트에서는 `spring-boot-starter-validation` 의존성이 필요하다.

Q. Nested DTO 검증이 안 돼?
A. 중첩 필드에 `@Valid`를 붙였는지 확인한다.

Q. Entity에 Validation을 붙이면 Request 검증이 돼?
A. Entity를 Request DTO로 쓰지 않는 구조라면 Request DTO에 Validation을 작성해야 한다.

---

# 8. Validation Anti Pattern

## 8.1 Validation Common Mistakes

### [개념]

Validation Anti Pattern은 입력 검증 책임이 DTO, Controller, Service, Entity 사이에서 섞여 유지보수성과 응답 일관성을 떨어뜨리는 구조다.

Validation은 형식 검증과 비즈니스 검증을 분리해야 한다.

---

### [핵심]

자주 발생하는 실수:

- Request DTO 없이 Entity를 검증
- DTO에 Validation Annotation만 붙이고 `@Valid` 누락
- Controller에서 수동 if 검증 반복
- Service에서 빈 값 / 길이 같은 형식 검증 반복
- DTO에서 DB 조회가 필요한 비즈니스 검증 시도
- Validation 실패를 Controller try-catch로 처리
- Field Error 응답 구조가 API마다 다름
- `@Email`만 쓰고 `@NotBlank` 누락
- Optional 숫자 파라미터를 primitive type으로 받음
- 날짜 포맷 기준 없음
- enum 입력 기준 없음
- rejectedValue에 민감정보 노출
- Validation Group을 과도하게 사용
- Create / Update DTO를 무리하게 하나로 합침

---

### [실무]

Anti Pattern 1:

```java
@PostMapping("/users")
public ApiResponse<UserResponse> createUser(
        @RequestBody User user
) {
    if (user.getEmail() == null || user.getEmail().isBlank()) {
        return ApiResponse.fail("INVALID_EMAIL", "이메일은 필수입니다.");
    }

    return ApiResponse.success(userService.createUser(user));
}
```

문제:

```text
Entity RequestBody 사용
Controller 수동 검증
실패 응답 직접 생성
Validation 책임 혼합
```

개선:

```java
@PostMapping("/users")
public ApiResponse<UserResponse> createUser(
        @Valid @RequestBody UserCreateRequest request
) {
    return ApiResponse.success(userService.createUser(request));
}
```

Anti Pattern 2:

```java
public record UserRequest(
        String email,
        String password,
        String nickname,
        String role,
        String status
) {
}
```

문제:

```text
생성 / 수정 / 관리자 수정 요청이 하나의 DTO에 섞임
검증 조건 불명확
Client가 role, status 조작 가능
```

개선:

```java
public record UserCreateRequest(
        @NotBlank @Email String email,
        @NotBlank String password,
        @NotBlank String nickname
) {
}
```

```java
public record UserUpdateRequest(
        @NotBlank String nickname
) {
}
```

Anti Pattern 3:

```java
public record FieldErrorResponse(
        String field,
        Object rejectedValue,
        String message
) {
}
```

문제:

```text
password, token 등 민감 입력값 노출 가능
```

개선:

```java
public record FieldErrorResponse(
        String field,
        String message
) {
}
```

---

### [FAQ]

Q. Controller에서 if로 검증하면 안 돼?
A. 단순 형식 검증은 Request DTO Validation으로 처리하고 Controller 수동 검증은 줄이는 것이 좋다.

Q. Service에서 `title.isBlank()` 같은 검증을 해도 돼?
A. 형식 검증은 DTO Validation에서 처리하고 Service는 비즈니스 검증에 집중하는 것이 좋다.

Q. Validation Group을 많이 쓰면 좋아?
A. 과도한 Group은 복잡도를 높인다. Create / Update DTO 분리가 더 명확한 경우가 많다.

Q. rejectedValue를 Field Error에 넣으면 왜 위험해?
A. password, token, 개인정보 같은 민감 입력값이 응답으로 노출될 수 있다.

---

# 9. Review Checklist

## 9.1 Validation and Binding Checklist

### [개념]

Validation and Binding Checklist는 Request DTO 검증, Controller Binding, Error Handling을 검수하기 위한 기준이다.

Backend Agent와 Review Agent는 이 Checklist를 기준으로 입력 검증 문제와 Binding 문제를 탐지한다.

---

### [핵심]

Checklist:

```md
- [ ] Request DTO에 필요한 Validation Annotation이 있는가?
- [ ] Controller Parameter에 @Valid가 적용되어 있는가?
- [ ] Entity를 RequestBody로 직접 받지 않는가?
- [ ] 형식 검증과 비즈니스 검증이 분리되어 있는가?
- [ ] 비즈니스 검증은 Service에서 처리하는가?
- [ ] Validation 실패를 GlobalExceptionHandler에서 처리하는가?
- [ ] MethodArgumentNotValidException 처리가 있는가?
- [ ] BindException 또는 ModelAttribute 검증 실패 처리를 고려했는가?
- [ ] MethodArgumentTypeMismatchException 처리가 있는가?
- [ ] HttpMessageNotReadableException 처리가 있는가?
- [ ] Field Error 응답 구조가 일관적인가?
- [ ] rejectedValue로 민감정보를 노출하지 않는가?
- [ ] @NotBlank, @NotNull, @NotEmpty를 목적에 맞게 사용하는가?
- [ ] 이메일 필수 값에 @NotBlank와 @Email을 함께 사용하는가?
- [ ] Optional 숫자 파라미터에 Wrapper Type을 사용하는가?
- [ ] JSON 필드명과 DTO 필드명이 일치하는가?
- [ ] @RequestBody가 필요한 곳에 누락되지 않았는가?
- [ ] Query Parameter DTO에 @ModelAttribute를 적절히 사용하는가?
- [ ] 날짜 Query Parameter에 @DateTimeFormat이 필요한지 검토했는가?
- [ ] enum Binding 기준이 명확한가?
- [ ] Nested DTO에 @Valid가 필요한지 검토했는가?
- [ ] Validation Group이 과도하게 사용되지 않았는가?
- [ ] Create / Update DTO 분리가 필요한지 검토했는가?
```

---

### [실무]

검수 흐름:

```text
Controller Method 확인
→ Request DTO 확인
→ @Valid 확인
→ Validation Annotation 확인
→ Binding Annotation 확인
→ JSON / Query Field Name 확인
→ Type Conversion 확인
→ Date / Enum Binding 확인
→ GlobalExceptionHandler 확인
→ Field Error Response 확인
→ Anti Pattern 확인
→ Final Review
```

검수 결과 예:

```text
문제:
PostCreateRequest에 @NotBlank가 있지만 Controller에 @Valid가 없음

위험:
빈 제목 요청이 Service까지 전달될 수 있음

수정:
@Valid @RequestBody PostCreateRequest request 적용
```

검수 결과 예:

```text
문제:
UserCreateRequest email 필드에 @Email만 있음

위험:
빈 문자열이 통과할 수 있음

수정:
@NotBlank와 @Email 함께 적용
```

검수 결과 예:

```text
문제:
FieldErrorResponse에 rejectedValue 포함

위험:
password 등 민감정보 노출 가능

수정:
rejectedValue 제거 또는 민감 필드 마스킹
```

---

### [FAQ]

Q. Validation 검수에서 가장 중요한 것은?
A. Request DTO Annotation, Controller `@Valid`, GlobalExceptionHandler 처리, 형식 검증과 비즈니스 검증 분리다.

Q. Binding 검수에서 가장 중요한 것은?
A. `@RequestBody`, `@ModelAttribute`, DTO 필드명, 타입 변환, 날짜 / enum 포맷 일치 여부다.

Q. Validation Error 응답 검수는 어떻게 해?
A. ErrorCode, message, Field Error 구조, 민감정보 노출 여부를 확인한다.

Q. Validation이 동작하지 않으면 가장 먼저 뭘 봐?
A. Controller Parameter에 `@Valid`가 있는지 먼저 확인한다.

---

# 10. Part04 Final Goal

## 10.1 Validation and Binding Final Goal

### [개념]

Spring Boot Part04의 최종 목표는 Backend Agent가 Request Validation과 Binding을 일관되게 적용하고 Review Agent가 입력 검증 누락, Binding 오류, Error Response 불일치를 탐지하도록 만드는 것이다.

Part04는 Client Request가 안전하게 DTO로 변환되고 검증되는 과정을 다룬다.

---

### [핵심]

Part04가 지원해야 하는 작업:

- Request DTO Validation 설계
- Bean Validation Annotation 선택
- `@Valid` 적용
- `@Validated` 필요 여부 판단
- Validation Group 사용 여부 판단
- RequestBody Binding 설계
- ModelAttribute Binding 설계
- PathVariable Binding 설계
- RequestParam Binding 설계
- Date / Time Binding 설계
- Enum Binding 설계
- Type Conversion 오류 탐지
- Validation Exception 처리
- Field Error Response 설계
- Binding Troubleshooting
- Validation Anti Pattern 탐지

---

### [실무]

Backend Agent 수행 흐름:

```text
User API Requirement
→ Identify Request Fields
→ Create Request DTO
→ Apply Validation Annotation
→ Apply @Valid in Controller
→ Choose Binding Annotation
→ Check Type Conversion
→ Check Date / Enum Format
→ Define Validation Error Response
→ Connect GlobalExceptionHandler
→ Review Validation Boundary
```

Review Agent 수행 흐름:

```text
Input Controller / DTO Code
→ Check Request DTO
→ Check Validation Annotation
→ Check @Valid
→ Check Binding Annotation
→ Check Type Conversion Risk
→ Check Date / Enum Binding
→ Check GlobalExceptionHandler
→ Check Field Error Exposure
→ Detect Validation Anti Pattern
→ Suggest Fix
```

---

### [FAQ]

Q. Spring Boot Part04의 최종 목적은 뭐야?
A. Request Validation과 Binding을 일관되게 적용하고 검증 누락, Binding 오류, Error Response 문제를 탐지하게 만드는 것이다.

Q. Part04 다음에는 어떤 문서가 이어져야 해?
A. Service Layer & Business Logic 문서가 이어지는 것이 좋다.

Q. Part04만으로 입력 검증을 완성할 수 있어?
A. 기본 입력 검증은 가능하지만 비즈니스 검증과 Transaction 처리는 Service Layer 문서와 함께 사용해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Spring Boot Validation은 뭐야?
A. Client 요청 값이 Application에서 처리 가능한 형식과 제약 조건을 만족하는지 확인하는 과정이다.

Q. Validation은 왜 필요해?
A. 잘못된 입력을 API 경계에서 차단하고 Service Business Logic을 안전하게 유지하기 위해 필요하다.

Q. Validation은 어디서 해?
A. Request DTO에 제약 조건을 작성하고 Controller에서 `@Valid`로 검증을 트리거한다.

Q. 비즈니스 검증도 DTO Validation으로 해?
A. 아니다. 중복 이메일, 권한, 상태 전환 같은 비즈니스 검증은 Service에서 처리한다.

Q. Validation 실패는 어디서 처리해?
A. GlobalExceptionHandler에서 Validation Exception을 잡아 공통 Error Response로 변환한다.

Q. Bean Validation Annotation은 뭐가 있어?
A. `@NotNull`, `@NotBlank`, `@NotEmpty`, `@Size`, `@Email`, `@Pattern`, `@Min`, `@Max`, `@Positive`, `@PositiveOrZero` 등이 있다.

Q. `@NotNull`, `@NotBlank`, `@NotEmpty` 차이는?
A. `@NotNull`은 null만 금지하고, `@NotBlank`는 공백 문자열까지 금지하며, `@NotEmpty`는 null과 empty를 금지한다.

Q. 문자열 필수 값은 뭘 써?
A. 공백까지 막아야 하므로 보통 `@NotBlank`를 사용한다.

Q. 숫자 필수 값은 뭘 써?
A. `@NotNull`과 `@Positive`, `@Min`, `@Max` 같은 범위 검증을 조합한다.

Q. 이메일 검증은 뭘 써?
A. `@Email`을 사용하고 빈 값도 막아야 하면 `@NotBlank`를 함께 사용한다.

Q. `@Email`만 쓰면 빈 이메일도 막아?
A. 필수 이메일이면 `@NotBlank`와 `@Email`을 함께 사용하는 것이 좋다.

Q. Validation message는 꼭 작성해야 해?
A. 필수는 아니지만 사용자에게 명확한 오류 안내가 필요하면 작성하는 것이 좋다.

Q. Validation message와 errorCode는 같은 역할이야?
A. 아니다. errorCode는 Frontend 처리 기준이고 message는 사용자 안내 문구에 가깝다.

Q. Field Error를 응답에 포함해야 해?
A. 프로젝트 요구사항에 따라 정한다. Form 입력 화면에서는 포함하면 유용하다.

Q. `@Valid`는 어디에 붙여?
A. Controller Method에서 Request DTO 앞에 붙여 요청 검증을 트리거한다.

Q. DTO에 `@NotBlank`가 있으면 `@Valid` 없어도 돼?
A. 아니다. Controller Parameter에 `@Valid`를 붙여야 검증이 실행된다.

Q. Nested DTO도 자동으로 검증돼?
A. 내부 DTO 필드에 `@Valid`를 붙여야 중첩 객체 검증이 수행된다.

Q. List 내부 값도 검증할 수 있어?
A. 가능하다. `List<@NotNull Long>`처럼 Element Validation을 사용할 수 있다.

Q. `@Valid`와 `@Validated` 차이는?
A. `@Valid`는 기본 Bean Validation에 적합하고, `@Validated`는 Spring의 Validation Group과 Method Validation에 유용하다.

Q. 보통은 `@Valid`와 `@Validated` 중 뭘 써?
A. 일반 Request DTO 검증은 `@Valid`를 우선 사용한다.

Q. Validation Group은 언제 써?
A. 같은 DTO를 생성 / 수정 등 다른 검증 조건으로 사용해야 할 때 쓴다.

Q. Validation Group보다 DTO 분리가 나을 때도 있어?
A. 맞다. 생성 / 수정 조건이 많이 다르면 DTO를 분리하는 것이 더 명확하다.

Q. Binding은 뭐야?
A. HTTP Request 데이터를 Controller Parameter나 Request DTO로 변환하는 과정이다.

Q. Binding과 Validation은 뭐가 달라?
A. Binding은 요청 값을 Java 객체로 변환하는 과정이고, Validation은 변환된 값이 제약 조건을 만족하는지 검사하는 과정이다.

Q. Binding 실패도 400이 나?
A. 맞다. 타입 변환 실패, JSON 구조 오류, 날짜 포맷 오류 등은 400 Bad Request로 이어질 수 있다.

Q. JSON Body는 뭘로 Binding해?
A. `@RequestBody`를 사용해 Request DTO로 Binding한다.

Q. Query Parameter는 뭘로 Binding해?
A. `@RequestParam` 또는 조건이 많으면 `@ModelAttribute`를 사용한다.

Q. Path 값은 뭘로 Binding해?
A. `@PathVariable`을 사용한다.

Q. Header 값은 뭘로 Binding해?
A. `@RequestHeader`를 사용한다.

Q. RequestBody 값이 null로 들어오면 뭘 확인해?
A. Content-Type, `@RequestBody` 누락, JSON 필드명, DTO 구조, Jackson 변환 오류를 확인한다.

Q. JSON 필드명이 DTO와 다르면 어떻게 해?
A. 필드명을 맞추거나 `@JsonProperty`를 사용한다.

Q. GET 요청에도 `@RequestBody`를 써?
A. 권장하지 않는다. Query Parameter나 `@ModelAttribute`를 사용한다.

Q. `@ModelAttribute`는 언제 써?
A. Query Parameter나 Form 데이터를 객체로 Binding할 때 사용한다.

Q. 검색 조건이 많으면 어떻게 해?
A. `@RequestParam`을 여러 개 쓰기보다 SearchRequest DTO와 `@ModelAttribute`를 사용하는 것이 좋다.

Q. `@ModelAttribute`에 `@Valid`를 붙일 수 있어?
A. 가능하다. Query Parameter 기반 검색 조건도 검증할 수 있다.

Q. `@PathVariable`과 `@RequestParam` 차이는?
A. `@PathVariable`은 URL 경로 일부를 받고 `@RequestParam`은 query string 값을 받는다.

Q. Resource ID는 뭘로 받아?
A. 일반적으로 `@PathVariable`을 사용한다.

Q. 검색 키워드는 뭘로 받아?
A. 일반적으로 `@RequestParam` 또는 조건이 많으면 `@ModelAttribute`를 사용한다.

Q. PathVariable 타입이 안 맞으면 어떻게 돼?
A. 타입 변환 실패로 400 Bad Request가 발생할 수 있다.

Q. RequestParam 숫자 값은 자동 변환돼?
A. 가능하다. 문자열 query parameter가 Integer, Long 같은 타입으로 변환된다.

Q. Optional 숫자 파라미터는 int로 받아도 돼?
A. 권장하지 않는다. null 표현이 가능한 Integer 같은 Wrapper Type이 좋다.

Q. Query Parameter 날짜는 어떻게 받아?
A. `LocalDate`와 `@DateTimeFormat(pattern = "yyyy-MM-dd")`를 사용할 수 있다.

Q. `@DateTimeFormat`과 `@JsonFormat` 차이는?
A. `@DateTimeFormat`은 요청 파라미터 Binding에 주로 쓰고, `@JsonFormat`은 JSON 직렬화 / 역직렬화 포맷에 사용한다.

Q. 날짜 포맷이 틀리면 어떻게 돼?
A. Binding 실패로 400 Bad Request가 발생할 수 있다.

Q. enum은 RequestParam으로 바로 받을 수 있어?
A. 가능하다. 기본적으로 요청 문자열이 enum name과 일치해야 한다.

Q. enum 대소문자가 다르면 어떻게 돼?
A. 기본 Binding에서는 변환 실패로 400 Bad Request가 발생할 수 있다.

Q. enum code 값으로 받고 싶으면?
A. 별도 Converter를 구현하거나 문자열로 받은 뒤 Service에서 변환하는 방식을 검토한다.

Q. Validation 실패 시 어떤 예외가 발생해?
A. `@RequestBody @Valid` 실패는 주로 MethodArgumentNotValidException이 발생한다.

Q. Query Parameter 타입 변환 실패는 어떤 예외야?
A. MethodArgumentTypeMismatchException이 발생할 수 있다.

Q. JSON 형식이 깨지면 어떤 예외야?
A. HttpMessageNotReadableException이 발생할 수 있다.

Q. Field Error는 꼭 응답해야 해?
A. 필수는 아니지만 Form 입력 화면에서는 어떤 필드가 잘못됐는지 알려주기 위해 유용하다.

Q. rejectedValue를 응답에 포함해도 돼?
A. 민감정보 노출 위험이 있어 권장하지 않는다.

Q. password 검증 실패 시 입력한 password를 돌려줘도 돼?
A. 절대 안 된다. password, token 같은 민감정보는 응답에 포함하지 않는다.

Q. `@ModelAttribute` 값이 null이면 뭘 확인해?
A. Query Parameter 이름과 DTO 필드명이 일치하는지 확인한다.

Q. DTO에 `@NotBlank`를 붙였는데 검증이 안 돼?
A. Controller Parameter에 `@Valid`가 있는지 확인해야 한다.

Q. Validation 의존성이 따로 필요해?
A. Spring Boot 프로젝트에서는 `spring-boot-starter-validation` 의존성이 필요하다.

Q. Controller에서 if로 검증하면 안 돼?
A. 단순 형식 검증은 Request DTO Validation으로 처리하고 Controller 수동 검증은 줄이는 것이 좋다.

Q. Service에서 빈 값 검증을 해도 돼?
A. 형식 검증은 DTO Validation에서 처리하고 Service는 비즈니스 검증에 집중하는 것이 좋다.

Q. Validation 검수에서 가장 중요한 것은?
A. Request DTO Annotation, Controller `@Valid`, GlobalExceptionHandler 처리, 형식 검증과 비즈니스 검증 분리다.

Q. Binding 검수에서 가장 중요한 것은?
A. `@RequestBody`, `@ModelAttribute`, DTO 필드명, 타입 변환, 날짜 / enum 포맷 일치 여부다.

Q. Spring Boot Part04 다음에는 뭐가 좋아?
A. Service Layer & Business Logic 문서가 이어지는 것이 좋다.
