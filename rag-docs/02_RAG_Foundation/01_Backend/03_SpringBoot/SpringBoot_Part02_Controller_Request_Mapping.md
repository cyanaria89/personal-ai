# Spring Boot Part02 - Controller & Request Mapping

---

# 1. Controller Layer

## 1.1 Controller Purpose

### [개념]

Controller는 Spring Boot Application에서 HTTP Request와 HTTP Response를 처리하는 Layer다.

Controller는 Client 요청을 Application 내부 Use Case로 연결하는 진입점이다.

Controller는 Business Logic을 직접 수행하지 않는다.

Controller의 목적:

- HTTP Method Mapping
- URL Path Mapping
- Request Parameter 수신
- Request Body 수신
- Request DTO Binding
- Validation Trigger
- Authentication Principal 수신
- Service 호출
- Response DTO 반환
- ApiResponse 반환

---

### [핵심]

Controller 핵심 키워드:

- `@RestController`
- `@Controller`
- `@RequestMapping`
- `@GetMapping`
- `@PostMapping`
- `@PutMapping`
- `@PatchMapping`
- `@DeleteMapping`
- `@PathVariable`
- `@RequestParam`
- `@RequestBody`
- `@ModelAttribute`
- `@RequestHeader`
- `@Valid`
- Service Call
- Response DTO
- ApiResponse

Controller 책임:

- HTTP 요청 수신
- 입력 값 Binding
- Validation 실행
- Service 호출
- 응답 반환

Controller 금지:

- Repository 직접 호출
- Business Logic 작성
- Entity 직접 저장
- Entity 직접 반환
- Transaction 처리
- 복잡한 조건문 처리
- 외부 API 직접 호출
- 반복 try-catch 예외 처리

---

### [실무]

기본 REST Controller 예:

```java
@RestController
@RequestMapping("/api/posts")
@RequiredArgsConstructor
public class PostController {

    private final PostService postService;

    @PostMapping
    public ApiResponse<PostResponse> createPost(
            @Valid @RequestBody PostCreateRequest request
    ) {
        PostResponse response = postService.createPost(request);
        return ApiResponse.success(response);
    }
}
```

Controller 설계 기준:

```text
HTTP Request
→ Controller Mapping
→ Request DTO Binding
→ Validation Trigger
→ Service Call
→ Response DTO
→ ApiResponse
→ HTTP Response
```

권장:

- Controller는 얇게 유지한다.
- Method 이름은 Use Case를 표현한다.
- Request DTO와 Response DTO를 사용한다.
- Validation은 Controller 경계에서 트리거한다.
- 성공 응답은 프로젝트 공통 응답 규칙을 따른다.
- 실패 응답은 GlobalExceptionHandler에 위임한다.

비권장:

```java
@RestController
@RequiredArgsConstructor
public class PostController {

    private final PostRepository postRepository;

    @PostMapping("/posts")
    public Post createPost(@RequestBody Post post) {
        return postRepository.save(post);
    }
}
```

문제:

- Controller에서 Repository 직접 호출
- Entity를 RequestBody로 직접 수신
- Entity를 Response로 직접 반환
- Validation 기준 불명확
- Transaction Boundary 불명확
- Business Logic 위치 불명확

---

### [FAQ]

Q. Controller는 어디까지 해야 해?
A. 요청을 받고 검증을 트리거한 뒤 Service를 호출하고 응답을 반환하는 정도가 적합하다.

Q. Controller에서 Repository를 바로 호출해도 돼?
A. 실무 구조에서는 Service를 거쳐 비즈니스 로직과 트랜잭션 경계를 관리하는 것이 좋다.

Q. Controller에 비즈니스 로직이 많으면 왜 문제야?
A. HTTP 책임과 비즈니스 책임이 섞이고 테스트와 유지보수가 어려워진다.

Q. Controller에서 Entity를 반환해도 돼?
A. 권장하지 않는다. Response DTO로 변환해 필요한 필드만 반환하는 것이 좋다.

---

## 1.2 `@Controller` vs `@RestController`

### [개념]

`@Controller`와 `@RestController`는 Spring MVC에서 요청을 처리하는 Controller Bean을 등록하는 Annotation이다.

`@Controller`는 View 반환 중심이다.

`@RestController`는 JSON / XML 같은 Body Response 반환 중심이다.

`@RestController`는 `@Controller`와 `@ResponseBody`를 합친 형태다.

---

### [핵심]

비교:

| 구분        | `@Controller`        | `@RestController` |
| ----------- | -------------------- | ----------------- |
| 목적        | View 반환            | REST API 응답     |
| 기본 반환   | View Name            | Response Body     |
| JSON 응답   | `@ResponseBody` 필요 | 기본 지원         |
| 사용 예     | Thymeleaf, JSP       | JSON API          |
| Backend API | 비권장               | 권장              |

핵심 규칙:

- REST API Controller는 `@RestController`를 사용한다.
- SSR View Controller는 `@Controller`를 사용할 수 있다.
- JSON API에서 `@Controller`만 사용하면 View Resolver가 동작할 수 있다.
- API와 View Controller를 섞을 때 책임을 분리한다.

---

### [실무]

REST API 권장:

```java
@RestController
@RequestMapping("/api/users")
@RequiredArgsConstructor
public class UserController {

    private final UserService userService;

    @GetMapping("/{userId}")
    public ApiResponse<UserResponse> getUser(@PathVariable Long userId) {
        return ApiResponse.success(userService.getUser(userId));
    }
}
```

View Controller 예:

```java
@Controller
public class PageController {

    @GetMapping("/posts")
    public String postsPage() {
        return "posts/list";
    }
}
```

`@Controller`에서 JSON 반환:

```java
@Controller
@RequestMapping("/api/posts")
public class LegacyPostController {

    @ResponseBody
    @GetMapping("/{postId}")
    public PostResponse getPost(@PathVariable Long postId) {
        return postService.getPost(postId);
    }
}
```

Foundation 기준:

```text
REST API
→ @RestController 우선

SSR / Thymeleaf
→ @Controller 사용 가능
```

---

### [FAQ]

Q. `@Controller`와 `@RestController` 차이는?
A. `@Controller`는 View 반환에 주로 사용하고 `@RestController`는 JSON 응답 API에 사용한다.

Q. REST API에서는 어떤 걸 써야 해?
A. JSON API라면 `@RestController`를 사용하는 것이 좋다.

Q. `@Controller`로 JSON을 반환할 수 있어?
A. 가능하지만 `@ResponseBody`가 필요하다. REST API에서는 `@RestController`가 더 명확하다.

Q. Thymeleaf를 쓰면 `@RestController`를 써?
A. View Page를 반환할 때는 `@Controller`를 사용한다.

---

# 2. Request Mapping

## 2.1 Request Mapping Overview

### [개념]

Request Mapping은 HTTP Method와 URL Path를 Controller Method에 연결하는 규칙이다.

Spring Boot는 Mapping Annotation을 통해 요청을 특정 Controller Method로 라우팅한다.

Request Mapping은 API Endpoint 설계의 핵심이다.

---

### [핵심]

Mapping Annotation:

- `@RequestMapping`
- `@GetMapping`
- `@PostMapping`
- `@PutMapping`
- `@PatchMapping`
- `@DeleteMapping`

Parameter Annotation:

- `@PathVariable`
- `@RequestParam`
- `@RequestBody`
- `@ModelAttribute`
- `@RequestHeader`
- `@CookieValue`

기본 구조:

```java
@RestController
@RequestMapping("/api/posts")
public class PostController {

    @GetMapping("/{postId}")
    public ApiResponse<PostResponse> getPost(@PathVariable Long postId) {
        ...
    }
}
```

최종 URL:

```text
GET /api/posts/{postId}
```

---

### [실무]

Mapping 설계 흐름:

```text
API Use Case 확인
→ Resource 이름 결정
→ Base Path 결정
→ HTTP Method 결정
→ Path Variable 결정
→ Query Parameter 결정
→ Request Body 필요 여부 결정
→ Response DTO 결정
```

예:

| Use Case         | HTTP Method | URL                   | Parameter              |
| ---------------- | ----------- | --------------------- | ---------------------- |
| 게시글 목록 조회 | GET         | `/api/posts`          | `page`, `size`         |
| 게시글 단건 조회 | GET         | `/api/posts/{postId}` | `postId`               |
| 게시글 생성      | POST        | `/api/posts`          | Request Body           |
| 게시글 수정      | PATCH       | `/api/posts/{postId}` | `postId`, Request Body |
| 게시글 삭제      | DELETE      | `/api/posts/{postId}` | `postId`               |

권장:

- URI는 명사 중심으로 작성한다.
- HTTP Method 의미를 준수한다.
- Base Path는 Controller class level에 둔다.
- 세부 Path는 Method level에 둔다.
- PathVariable 이름과 Method Parameter 이름을 일치시킨다.
- Frontend Axios URL과 Controller Mapping을 반드시 일치시킨다.

---

### [FAQ]

Q. Request Mapping은 뭐야?
A. HTTP Method와 URL Path를 Controller Method에 연결하는 규칙이다.

Q. `@RequestMapping`은 어디에 붙여?
A. 보통 Controller class level에는 base path를, method level에는 세부 path를 지정한다.

Q. `@GetMapping`과 `@RequestMapping(method = GET)`은 같아?
A. 기능적으로 유사하지만 `@GetMapping`이 더 짧고 의도가 명확하다.

Q. URL 404가 나면 Mapping을 봐야 해?
A. 맞다. Controller base path, method path, HTTP Method, Frontend 요청 URL을 함께 확인해야 한다.

---

## 2.2 HTTP Method Mapping Rules

### [개념]

HTTP Method Mapping은 요청 목적에 맞는 HTTP Method를 선택하는 규칙이다.

REST API에서는 Resource에 대해 Method 의미를 일관되게 적용한다.

---

### [핵심]

HTTP Method 기준:

| Method | 목적             | 예                      |
| ------ | ---------------- | ----------------------- |
| GET    | 조회             | 게시글 목록 / 단건 조회 |
| POST   | 생성 / 처리 요청 | 게시글 생성, 로그인     |
| PUT    | 전체 수정        | 전체 필드 교체          |
| PATCH  | 부분 수정        | 닉네임 변경             |
| DELETE | 삭제             | 게시글 삭제             |

Spring Annotation:

| HTTP Method | Annotation       |
| ----------- | ---------------- |
| GET         | `@GetMapping`    |
| POST        | `@PostMapping`   |
| PUT         | `@PutMapping`    |
| PATCH       | `@PatchMapping`  |
| DELETE      | `@DeleteMapping` |

핵심 규칙:

- 조회는 GET을 사용한다.
- 생성은 POST를 사용한다.
- 부분 수정은 PATCH를 우선 검토한다.
- 삭제는 DELETE를 사용한다.
- GET 요청에 Request Body를 사용하지 않는다.
- Method 의미와 실제 동작을 일치시킨다.

---

### [실무]

게시글 API 예:

```java
@RestController
@RequestMapping("/api/posts")
@RequiredArgsConstructor
public class PostController {

    private final PostService postService;

    @GetMapping
    public ApiResponse<Slice<PostResponse>> getPosts(Pageable pageable) {
        return ApiResponse.success(postService.getPosts(pageable));
    }

    @GetMapping("/{postId}")
    public ApiResponse<PostResponse> getPost(@PathVariable Long postId) {
        return ApiResponse.success(postService.getPost(postId));
    }

    @PostMapping
    public ApiResponse<PostResponse> createPost(
            @Valid @RequestBody PostCreateRequest request
    ) {
        return ApiResponse.success(postService.createPost(request));
    }

    @PatchMapping("/{postId}")
    public ApiResponse<PostResponse> updatePost(
            @PathVariable Long postId,
            @Valid @RequestBody PostUpdateRequest request
    ) {
        return ApiResponse.success(postService.updatePost(postId, request));
    }

    @DeleteMapping("/{postId}")
    public ApiResponse<Void> deletePost(@PathVariable Long postId) {
        postService.deletePost(postId);
        return ApiResponse.success(null);
    }
}
```

주의:

```text
POST /posts/search
```

검색 조건이 복잡하고 Body가 필요한 경우 사용할 수 있다.

단순 검색은 다음을 우선한다.

```text
GET /posts?keyword=spring&category=backend
```

---

### [FAQ]

Q. 조회 API는 어떤 Method를 써?
A. 조회는 GET을 사용한다.

Q. 생성 API는 어떤 Method를 써?
A. 생성은 POST를 사용한다.

Q. 수정은 PUT과 PATCH 중 뭐가 좋아?
A. 전체 교체는 PUT, 일부 필드 수정은 PATCH가 적합하다.

Q. GET 요청에 RequestBody를 써도 돼?
A. 권장하지 않는다. Query Parameter나 PathVariable을 사용한다.

---

# 3. Parameter Binding

## 3.1 `@PathVariable`

### [개념]

`@PathVariable`은 URL Path에 포함된 값을 Controller Method Parameter로 바인딩하는 Annotation이다.

Resource 식별자에 주로 사용한다.

예:

```text
GET /api/posts/10
```

여기서 `10`은 `postId`로 바인딩할 수 있다.

---

### [핵심]

사용 상황:

- Resource ID
- User ID
- Post ID
- Order ID
- Path 기반 식별자
- 계층형 Resource 식별

예:

```java
@GetMapping("/{postId}")
public ApiResponse<PostResponse> getPost(
        @PathVariable Long postId
) {
    return ApiResponse.success(postService.getPost(postId));
}
```

명시적 이름 지정:

```java
@GetMapping("/{postId}")
public ApiResponse<PostResponse> getPost(
        @PathVariable("postId") Long id
) {
    return ApiResponse.success(postService.getPost(id));
}
```

핵심 규칙:

- Path 변수명과 Parameter명을 일치시키는 것이 좋다.
- 식별자는 `@PathVariable`을 우선 사용한다.
- Optional 값에는 적합하지 않다.
- 타입 변환 실패 시 400 Error가 발생할 수 있다.

---

### [실무]

계층형 Resource 예:

```java
@GetMapping("/{postId}/comments/{commentId}")
public ApiResponse<CommentResponse> getComment(
        @PathVariable Long postId,
        @PathVariable Long commentId
) {
    return ApiResponse.success(commentService.getComment(postId, commentId));
}
```

URL:

```text
GET /api/posts/10/comments/5
```

주의:

```java
@GetMapping("/{postId}")
public ApiResponse<PostResponse> getPost(
        @PathVariable Long id
) {
    ...
}
```

Parameter 이름이 `id`이고 Path 이름이 `postId`면 환경에 따라 Binding 문제가 생길 수 있다.

안전한 방식:

```java
@PathVariable("postId") Long id
```

권장:

- 식별자는 명확한 이름을 사용한다.
- `id`보다 `postId`, `userId`, `commentId`처럼 구체적으로 작성한다.
- 여러 PathVariable이 있으면 이름 충돌을 피한다.

---

### [FAQ]

Q. `@PathVariable`은 언제 써?
A. URL 경로에 포함된 Resource 식별자를 받을 때 사용한다.

Q. `@PathVariable`과 `@RequestParam` 차이는?
A. `@PathVariable`은 URL 경로 일부를 받고 `@RequestParam`은 query string 값을 받는다.

Q. PathVariable 이름과 Parameter 이름은 같아야 해?
A. 같게 작성하는 것이 좋다. 다르면 `@PathVariable("postId")`처럼 명시한다.

Q. PathVariable 타입이 안 맞으면 어떻게 돼?
A. 타입 변환 실패로 400 Bad Request가 발생할 수 있다.

---

## 3.2 `@RequestParam`

### [개념]

`@RequestParam`은 Query String 값을 Controller Method Parameter로 바인딩하는 Annotation이다.

주로 검색, 필터, 정렬, 페이지 번호 같은 선택 조건에 사용한다.

예:

```text
GET /api/posts?keyword=spring&page=0&size=10
```

---

### [핵심]

사용 상황:

- 검색 키워드
- 필터 조건
- 정렬 조건
- 페이지 번호
- 크기
- 선택 옵션
- 단순 Query Parameter

예:

```java
@GetMapping
public ApiResponse<List<PostResponse>> searchPosts(
        @RequestParam String keyword
) {
    return ApiResponse.success(postService.searchPosts(keyword));
}
```

옵션 값:

```java
@GetMapping
public ApiResponse<List<PostResponse>> searchPosts(
        @RequestParam(required = false) String keyword
) {
    return ApiResponse.success(postService.searchPosts(keyword));
}
```

기본 값:

```java
@GetMapping
public ApiResponse<List<PostResponse>> getPosts(
        @RequestParam(defaultValue = "0") int page,
        @RequestParam(defaultValue = "10") int size
) {
    return ApiResponse.success(postService.getPosts(page, size));
}
```

---

### [실무]

검색 API 예:

```java
@GetMapping("/search")
public ApiResponse<Slice<PostResponse>> searchPosts(
        @RequestParam(required = false) String keyword,
        @RequestParam(required = false) String category,
        Pageable pageable
) {
    return ApiResponse.success(
            postService.searchPosts(keyword, category, pageable)
    );
}
```

URL:

```text
GET /api/posts/search?keyword=spring&category=backend&page=0&size=10
```

권장:

- 단순 검색 조건은 `@RequestParam`을 사용한다.
- Optional 조건은 `required = false`를 사용한다.
- 기본 값이 필요한 경우 `defaultValue`를 사용한다.
- 조건이 많아지면 `@ModelAttribute` DTO를 검토한다.
- 복잡한 검색 Body가 필요하면 POST 검색 API를 검토한다.

주의:

```java
@GetMapping("/search")
public ApiResponse<?> search(@RequestBody SearchRequest request) {
    ...
}
```

GET + RequestBody는 권장하지 않는다.

대안:

```java
@GetMapping("/search")
public ApiResponse<?> search(@ModelAttribute SearchRequest request) {
    ...
}
```

또는:

```java
@PostMapping("/search")
public ApiResponse<?> search(@RequestBody SearchRequest request) {
    ...
}
```

---

### [FAQ]

Q. `@RequestParam`은 언제 써?
A. Query String으로 전달되는 검색, 필터, 페이지, 정렬 조건을 받을 때 사용한다.

Q. Query Parameter가 없어도 되게 하려면?
A. `@RequestParam(required = false)`를 사용한다.

Q. 기본 값을 주려면?
A. `@RequestParam(defaultValue = "10")`처럼 사용한다.

Q. 검색 조건이 많으면 어떻게 해?
A. `@ModelAttribute`로 검색 조건 DTO를 받거나 복잡한 조건은 POST Body 검색을 검토한다.

---

## 3.3 `@RequestBody`

### [개념]

`@RequestBody`는 HTTP Request Body의 JSON 데이터를 Java 객체로 변환하는 Annotation이다.

주로 생성, 수정 API에서 Request DTO를 받을 때 사용한다.

Spring Boot는 Jackson MessageConverter를 통해 JSON을 DTO로 변환한다.

---

### [핵심]

사용 상황:

- JSON Body 요청
- 생성 API
- 수정 API
- 로그인 요청
- 복잡한 입력 데이터
- Request DTO Binding

예:

```java
@PostMapping
public ApiResponse<PostResponse> createPost(
        @Valid @RequestBody PostCreateRequest request
) {
    return ApiResponse.success(postService.createPost(request));
}
```

핵심 규칙:

- Entity를 `@RequestBody`로 직접 받지 않는다.
- Request DTO를 사용한다.
- `@Valid`와 함께 사용해 검증을 트리거한다.
- JSON 필드명과 DTO 필드명을 맞춘다.
- Content-Type은 `application/json`이어야 한다.
- GET 요청에서는 RequestBody 사용을 지양한다.

---

### [실무]

Request DTO 예:

```java
public record PostCreateRequest(
        @NotBlank String title,
        @NotBlank String content
) {
}
```

JSON 요청:

```json
{
  "title": "Spring Boot",
  "content": "Controller Mapping"
}
```

Controller:

```java
@PostMapping
public ApiResponse<PostResponse> createPost(
        @Valid @RequestBody PostCreateRequest request
) {
    return ApiResponse.success(postService.createPost(request));
}
```

RequestBody 값이 null인 경우 확인:

```text
Content-Type 확인
→ @RequestBody 누락 확인
→ JSON 필드명 확인
→ DTO 생성자 / record 구조 확인
→ Jackson 변환 오류 확인
→ Validation Error 확인
```

비권장:

```java
@PostMapping("/users")
public User createUser(@RequestBody User user) {
    return userService.createUser(user);
}
```

문제:

- Entity와 API 입력 구조 강결합
- 민감 필드 수신 가능
- Validation 기준 불명확
- 보안 문제 가능

---

### [FAQ]

Q. `@RequestBody`는 언제 써?
A. JSON Body 요청을 Request DTO로 받을 때 사용한다.

Q. `@RequestBody` 값이 null이면 뭘 확인해?
A. Content-Type, `@RequestBody` 누락, JSON 필드명, DTO 구조, Jackson 변환 오류를 확인한다.

Q. Entity를 RequestBody로 받아도 돼?
A. 권장하지 않는다. Request DTO를 따로 만들어 API 입력 구조를 분리하는 것이 좋다.

Q. `@RequestBody`와 `@Valid`를 같이 써야 해?
A. Request DTO 검증이 필요하면 `@Valid @RequestBody` 형태로 사용한다.

---

## 3.4 `@ModelAttribute`

### [개념]

`@ModelAttribute`는 Query Parameter 또는 Form Data를 객체로 바인딩하는 Annotation이다.

검색 조건 DTO, 필터 DTO, Form 요청 처리에 사용할 수 있다.

GET 검색 조건이 많을 때 유용하다.

---

### [핵심]

사용 상황:

- 검색 조건 DTO
- Query Parameter 객체 바인딩
- Form Data
- Multipart Form 일부
- GET 요청의 복합 조건

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

URL:

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

- GET Query Object는 `@ModelAttribute`를 검토한다.
- JSON Body 요청에는 `@RequestBody`를 사용한다.
- 검색 조건이 많으면 `@RequestParam` 여러 개보다 DTO가 낫다.
- Binding 가능한 구조를 유지한다.
- Validation이 필요하면 `@Valid`와 함께 사용할 수 있다.

---

### [실무]

검색 조건 DTO 예:

```java
public record FestivalSearchRequest(
        String keyword,
        String regionCode,
        String themeCode,
        LocalDate startDate,
        LocalDate endDate
) {
}
```

Controller:

```java
@GetMapping("/search")
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
GET /api/festivals/search?keyword=music&regionCode=11&themeCode=FESTIVAL
```

`@RequestParam` 다수 사용보다 좋은 경우:

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

대안:

```java
@GetMapping("/search")
public ApiResponse<?> search(@ModelAttribute FestivalSearchRequest request) {
    ...
}
```

---

### [FAQ]

Q. `@ModelAttribute`는 언제 써?
A. Query Parameter나 Form 데이터를 객체로 바인딩할 때 사용한다.

Q. 검색 조건이 많으면 `@RequestParam`을 계속 써?
A. 조건이 많아지면 `@ModelAttribute` DTO로 묶는 것이 좋다.

Q. JSON Body도 `@ModelAttribute`로 받아?
A. 아니다. JSON Body는 `@RequestBody`로 받는다.

Q. GET 검색 API에서 DTO를 받을 수 있어?
A. 가능하다. `@ModelAttribute`를 사용하면 Query Parameter를 DTO로 바인딩할 수 있다.

---

## 3.5 `@RequestHeader`

### [개념]

`@RequestHeader`는 HTTP Header 값을 Controller Method Parameter로 바인딩하는 Annotation이다.

인증 토큰, 클라이언트 정보, 요청 메타데이터를 받을 때 사용할 수 있다.

단, 인증 / 인가 판단은 Controller보다 Security Filter에서 처리하는 것이 일반적이다.

---

### [핵심]

사용 상황:

- Authorization Header 확인
- Custom Header 수신
- Client Version 확인
- Locale Header 확인
- Request Trace ID 확인

예:

```java
@GetMapping("/me")
public ApiResponse<UserResponse> getMe(
        @RequestHeader("Authorization") String authorizationHeader
) {
    ...
}
```

핵심 규칙:

- 인증 처리는 Security Filter에서 우선 처리한다.
- Controller에서 Token Parsing을 반복하지 않는다.
- 필요한 Header만 명시적으로 받는다.
- Header가 없을 수 있으면 `required = false`를 사용한다.
- 민감 Header를 로그에 남기지 않는다.

---

### [실무]

Custom Header 예:

```java
@GetMapping("/version-check")
public ApiResponse<Void> checkVersion(
        @RequestHeader(value = "X-Client-Version", required = false) String clientVersion
) {
    versionService.check(clientVersion);
    return ApiResponse.success(null);
}
```

인증 사용자 정보 권장 흐름:

```text
Authorization Header
→ Security Filter
→ Token Validation
→ Authentication 생성
→ SecurityContext 저장
→ Controller에서 Principal 사용
```

비권장:

```java
@GetMapping("/me")
public ApiResponse<UserResponse> getMe(
        @RequestHeader("Authorization") String token
) {
    Long userId = jwtProvider.parse(token);
    return ApiResponse.success(userService.getUser(userId));
}
```

문제:

- Controller마다 Token Parsing 반복
- Security 책임 분산
- 인증 / 인가 기준 불일치 가능
- 테스트 복잡도 증가

---

### [FAQ]

Q. `@RequestHeader`는 언제 써?
A. HTTP Header 값을 Controller에서 직접 받아야 할 때 사용한다.

Q. Authorization Header를 Controller에서 파싱해도 돼?
A. 반복 파싱은 권장하지 않는다. 인증 처리는 Security Filter에서 처리하는 것이 좋다.

Q. Header가 없을 수도 있으면?
A. `@RequestHeader(required = false)`를 사용한다.

Q. Header 값을 로그에 찍어도 돼?
A. Authorization Token 같은 민감정보는 로그에 남기면 안 된다.

---

# 4. Controller Method Design

## 4.1 Controller Method Signature Rules

### [개념]

Controller Method Signature는 Controller Method가 어떤 요청 값을 받고 어떤 응답을 반환하는지 정의하는 구조다.

Method Signature는 API 명세와 직접 연결된다.

---

### [핵심]

구성 요소:

- Mapping Annotation
- PathVariable
- RequestParam
- RequestBody
- ModelAttribute
- RequestHeader
- Pageable
- Principal
- Request DTO
- Response DTO
- ApiResponse

권장 Signature:

```java
@PostMapping
public ApiResponse<PostResponse> createPost(
        @Valid @RequestBody PostCreateRequest request
) {
    ...
}
```

비권장 Signature:

```java
@PostMapping
public Post createPost(
        @RequestBody Post post,
        HttpServletRequest request
) {
    ...
}
```

핵심 규칙:

- 불필요한 Servlet API 의존을 줄인다.
- Entity를 Parameter로 받지 않는다.
- Request DTO를 사용한다.
- Response DTO를 반환한다.
- 공통 응답 규칙을 따른다.
- Parameter 순서는 읽기 쉽게 유지한다.

---

### [실무]

권장 Parameter 순서:

```text
@PathVariable
→ @RequestParam / @ModelAttribute
→ @RequestBody
→ Pageable
→ Authentication Principal
```

예:

```java
@PatchMapping("/{postId}")
public ApiResponse<PostResponse> updatePost(
        @PathVariable Long postId,
        @Valid @RequestBody PostUpdateRequest request
) {
    return ApiResponse.success(postService.updatePost(postId, request));
}
```

목록 조회:

```java
@GetMapping
public ApiResponse<Slice<PostResponse>> getPosts(
        @ModelAttribute PostSearchRequest request,
        Pageable pageable
) {
    return ApiResponse.success(postService.getPosts(request, pageable));
}
```

인증 사용자 기준 요청:

```java
@GetMapping("/me")
public ApiResponse<UserResponse> getMe(
        @AuthenticationPrincipal CustomUserDetails userDetails
) {
    return ApiResponse.success(userService.getMe(userDetails.getUserId()));
}
```

Security 세부 구현은 Security Advanced Domain Rules에서 다룬다.

---

### [FAQ]

Q. Controller Method는 어떤 형태가 좋아?
A. Request DTO를 받고 Service를 호출한 뒤 Response DTO 또는 ApiResponse를 반환하는 형태가 좋다.

Q. Controller Method에 HttpServletRequest를 받아도 돼?
A. 가능하지만 불필요하게 Servlet API에 의존하지 않도록 필요한 값만 Annotation으로 받는 것이 좋다.

Q. Entity를 Controller Method Parameter로 받아도 돼?
A. 권장하지 않는다. Request DTO를 사용한다.

Q. 인증 사용자 정보는 userId를 RequestBody로 받아?
A. 인증된 사용자 기준 작업이라면 RequestBody의 userId보다 SecurityContext나 인증 Principal에서 가져오는 것이 안전하다.

---

## 4.2 ApiResponse Return Rules

### [개념]

ApiResponse Return Rule은 Controller가 일관된 성공 응답 형식을 반환하도록 하는 규칙이다.

ApiResponse는 Frontend가 응답을 안정적으로 처리할 수 있게 한다.

---

### [핵심]

공통 응답 요소:

- success
- message
- data
- errorCode
- timestamp
- status

예:

```java
public record ApiResponse<T>(
        boolean success,
        String message,
        T data
) {
    public static <T> ApiResponse<T> success(T data) {
        return new ApiResponse<>(true, "success", data);
    }
}
```

Controller 반환 예:

```java
@GetMapping("/{postId}")
public ApiResponse<PostResponse> getPost(@PathVariable Long postId) {
    return ApiResponse.success(postService.getPost(postId));
}
```

핵심 규칙:

- 성공 응답 형식을 통일한다.
- 실패 응답은 GlobalExceptionHandler에서 통일한다.
- Controller에서 에러 응답을 직접 조립하지 않는다.
- ResponseEntity 사용 여부는 프로젝트 규칙으로 통일한다.

---

### [실무]

성공 응답:

```java
@PostMapping
public ApiResponse<PostResponse> createPost(
        @Valid @RequestBody PostCreateRequest request
) {
    return ApiResponse.success(postService.createPost(request));
}
```

삭제 응답:

```java
@DeleteMapping("/{postId}")
public ApiResponse<Void> deletePost(@PathVariable Long postId) {
    postService.deletePost(postId);
    return ApiResponse.success(null);
}
```

ResponseEntity가 필요한 경우:

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

선택 기준:

| 반환 방식                        | 사용 상황                               |
| -------------------------------- | --------------------------------------- |
| `ApiResponse<T>`                 | 일반 성공 응답                          |
| `ResponseEntity<ApiResponse<T>>` | HTTP Status, Header, Location 제어 필요 |
| `Response DTO`                   | 공통 응답을 쓰지 않는 프로젝트          |
| Entity                           | 비권장                                  |

---

### [FAQ]

Q. Controller에서 ApiResponse만 반환해도 돼?
A. 프로젝트 규칙이 성공 응답은 ApiResponse 직접 반환하고 실패는 GlobalExceptionHandler가 처리하는 구조라면 가능하다.

Q. ResponseEntity는 언제 써?
A. HTTP 상태 코드, Header, Created Location 등 HTTP 응답을 세밀하게 제어해야 할 때 유용하다.

Q. 실패 응답은 Controller에서 직접 만들어?
A. 일반적으로 GlobalExceptionHandler에서 공통 처리하는 것이 좋다.

Q. 삭제 API는 무엇을 반환해?
A. 프로젝트 규칙에 따라 `ApiResponse<Void>` 또는 상태 코드 중심 응답을 반환할 수 있다.

---

# 5. URL Design Basics

## 5.1 REST URL Naming Rules

### [개념]

REST URL Naming은 API Resource를 URI로 표현하는 규칙이다.

Spring Boot Controller Mapping은 REST URL Naming과 직접 연결된다.

Foundation 단계에서는 복잡한 REST 성숙도보다 일관성과 명확성을 우선한다.

---

### [핵심]

URL Naming 규칙:

- Resource는 명사로 표현한다.
- 복수형 Resource를 사용한다.
- 동사는 HTTP Method로 표현한다.
- PathVariable은 식별자에 사용한다.
- Query Parameter는 검색 / 필터에 사용한다.
- URL 마지막에 불필요한 동사를 붙이지 않는다.
- 대소문자를 섞지 않는다.
- 언더스코어보다 하이픈 또는 소문자 단어를 선호한다.
- 프로젝트 내 URI 스타일을 통일한다.

권장:

```text
GET /api/posts
GET /api/posts/{postId}
POST /api/posts
PATCH /api/posts/{postId}
DELETE /api/posts/{postId}
```

비권장:

```text
GET /api/getPosts
POST /api/createPost
POST /api/posts/delete/{postId}
GET /api/PostList
```

---

### [실무]

Resource 중심 URL:

```text
/api/users
/api/posts
/api/comments
/api/festivals
/api/reviews
/api/notifications
```

계층형 Resource:

```text
GET /api/posts/{postId}/comments
POST /api/posts/{postId}/comments
DELETE /api/posts/{postId}/comments/{commentId}
```

검색 / 필터:

```text
GET /api/festivals?region=seoul&theme=music
GET /api/posts/search?keyword=spring
```

복잡한 검색:

```text
POST /api/festivals/search
```

사용 가능 조건:

- 검색 조건이 매우 많음
- Body 구조가 필요함
- GET Query String 길이가 과도함
- 복합 필터 / 정렬 조건이 복잡함

주의:

- `/festival`과 `/festivals` 혼용 금지
- Controller `@RequestMapping`과 Frontend Axios URL 일치
- API Prefix `/api` 사용 여부 통일
- 인증 API, 관리자 API Prefix 분리 가능

---

### [FAQ]

Q. REST URL은 어떻게 짓는 게 좋아?
A. Resource는 명사로 표현하고 동작은 HTTP Method로 표현하는 것이 좋다.

Q. `/getUsers` 같은 URL은 안 좋아?
A. REST 스타일에서는 동사보다 `GET /users`처럼 Method와 Resource 조합을 선호한다.

Q. 단수와 복수 중 뭐가 좋아?
A. 프로젝트 내에서 통일하는 것이 중요하며 일반적으로 복수형 Resource를 많이 사용한다.

Q. 검색 API는 GET이야 POST야?
A. 단순 검색은 GET Query Parameter가 좋고, 조건이 복잡하면 POST Body 검색을 검토할 수 있다.

---

## 5.2 Base Path and Prefix Rules

### [개념]

Base Path는 Controller 전체에 적용되는 공통 URL Prefix다.

Spring Boot에서는 class level `@RequestMapping`으로 Base Path를 지정한다.

---

### [핵심]

예:

```java
@RestController
@RequestMapping("/api/posts")
public class PostController {
}
```

Base Path:

```text
/api/posts
```

Method Path:

```java
@GetMapping("/{postId}")
```

최종 Path:

```text
GET /api/posts/{postId}
```

Prefix 종류:

- `/api`
- `/api/v1`
- `/admin`
- `/auth`
- `/public`
- `/internal`

핵심 규칙:

- API Prefix 사용 여부를 프로젝트 규칙으로 정한다.
- Controller Base Path와 Frontend URL을 일치시킨다.
- 버전 관리가 필요하면 `/api/v1`을 검토한다.
- 관리자 API는 `/admin` 또는 `/api/admin` 등으로 구분한다.
- 인증이 필요 없는 API와 필요한 API를 명확히 구분한다.

---

### [실무]

일반 API:

```java
@RestController
@RequestMapping("/api/posts")
@RequiredArgsConstructor
public class PostController {
}
```

인증 API:

```java
@RestController
@RequestMapping("/api/auth")
@RequiredArgsConstructor
public class AuthController {
}
```

관리자 API:

```java
@RestController
@RequestMapping("/api/admin/users")
@RequiredArgsConstructor
public class AdminUserController {
}
```

문제 예:

```text
Controller:
@RequestMapping("/festivals")

Frontend:
publicApi.get("/festival")
```

결과:

```text
404 Not Found
```

해결:

```text
Controller Prefix와 Frontend URL을 일치시킨다.
```

검수 흐름:

```text
Frontend Request URL 확인
→ Axios baseURL 확인
→ Controller @RequestMapping 확인
→ Method Mapping 확인
→ 최종 URL 조합 확인
```

---

### [FAQ]

Q. Base Path는 어디에 지정해?
A. 보통 Controller class level `@RequestMapping`에 지정한다.

Q. `/api` Prefix는 꼭 붙여야 해?
A. 필수는 아니지만 API와 View Route를 구분하기 위해 사용하는 경우가 많다.

Q. `/festival`과 `/festivals`가 섞이면 문제야?
A. 문제가 될 수 있다. Controller Mapping과 Frontend 요청 URL이 다르면 404가 발생한다.

Q. API 버전은 언제 붙여?
A. 외부 공개 API거나 장기 유지보수가 필요한 경우 `/api/v1` 같은 버전을 검토한다.

---

# 6. Pageable and List Request Mapping

## 6.1 Pageable Controller Rules

### [개념]

Pageable은 Spring Data에서 page, size, sort 같은 pagination 요청 값을 받는 객체다.

Controller에서 Pageable을 Parameter로 받을 수 있다.

목록 조회 API에서 Page 또는 Slice 응답과 함께 사용한다.

---

### [핵심]

관련 키워드:

- Pageable
- Page
- Slice
- page
- size
- sort
- total count
- hasNext
- infinite scroll
- pagination
- list query

기본 요청:

```text
GET /api/posts?page=0&size=10&sort=createdAt,desc
```

Controller:

```java
@GetMapping
public ApiResponse<Slice<PostResponse>> getPosts(Pageable pageable) {
    return ApiResponse.success(postService.getPosts(pageable));
}
```

선택 기준:

| Type  | 특징                  | 사용 상황            |
| ----- | --------------------- | -------------------- |
| Page  | total count 포함      | 페이지 번호 UI       |
| Slice | 다음 페이지 여부 중심 | 무한 스크롤 / 더보기 |
| List  | 전체 목록             | 소량 데이터          |

---

### [실무]

무한 스크롤 API:

```java
@GetMapping
public ApiResponse<Slice<PostResponse>> getPosts(Pageable pageable) {
    return ApiResponse.success(postService.getPosts(pageable));
}
```

검색 조건 + Pageable:

```java
@GetMapping("/search")
public ApiResponse<Slice<PostResponse>> searchPosts(
        @ModelAttribute PostSearchRequest request,
        Pageable pageable
) {
    return ApiResponse.success(postService.searchPosts(request, pageable));
}
```

권장:

- 기본 page size 정책을 정한다.
- 최대 size 제한을 검토한다.
- 정렬 기준을 명확히 한다.
- 무한 스크롤은 Slice를 우선 검토한다.
- Page는 total count query 비용을 고려한다.
- Pageable을 Service까지 전달할 수 있다.

주의:

```text
대용량 데이터 + Page
→ count query 비용 발생 가능
```

대안:

```text
무한 스크롤
→ Slice 사용

커서 기반 페이지네이션
→ Expert / Performance 문서에서 심화
```

---

### [FAQ]

Q. Pageable은 Controller에서 바로 받아도 돼?
A. 가능하다. 다만 기본 size, sort, 최대 size 정책을 정하는 것이 좋다.

Q. Page와 Slice 차이는?
A. Page는 전체 개수를 포함하고 Slice는 다음 페이지 존재 여부 중심이다. 무한 스크롤은 Slice가 적합할 수 있다.

Q. 목록 조회에는 항상 Page를 써?
A. 아니다. 무한 스크롤이나 더보기 UI는 Slice가 더 적합할 수 있다.

Q. Pageable과 검색 DTO를 같이 받을 수 있어?
A. 가능하다. `@ModelAttribute` 검색 DTO와 Pageable을 함께 사용할 수 있다.

---

# 7. Controller Validation Trigger

## 7.1 `@Valid` in Controller

### [개념]

`@Valid`는 Controller에서 Request DTO 검증을 트리거하는 Annotation이다.

Spring Boot는 Bean Validation을 통해 Request DTO의 Validation Annotation을 검사한다.

Validation 실패는 일반적으로 GlobalExceptionHandler에서 처리한다.

---

### [핵심]

사용 위치:

```java
@PostMapping
public ApiResponse<PostResponse> createPost(
        @Valid @RequestBody PostCreateRequest request
) {
    ...
}
```

검증 Annotation:

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

핵심 규칙:

- Request DTO 앞에 `@Valid`를 붙인다.
- 형식 검증은 DTO에서 처리한다.
- 비즈니스 검증은 Service에서 처리한다.
- Validation Error는 GlobalExceptionHandler에서 응답으로 변환한다.
- Controller에서 BindingResult를 남용하지 않는다.

---

### [실무]

DTO:

```java
public record SignUpRequest(
        @Email String email,
        @NotBlank String password,
        @NotBlank String nickname
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
→ Controller
→ @Valid
→ Bean Validation
→ MethodArgumentNotValidException
→ GlobalExceptionHandler
→ Error Response
```

주의:

```java
@PostMapping("/signup")
public ApiResponse<UserResponse> signUp(
        @RequestBody SignUpRequest request
) {
    ...
}
```

문제:

- DTO에 Validation Annotation이 있어도 `@Valid`가 없으면 검증이 실행되지 않을 수 있다.

---

### [FAQ]

Q. `@Valid`는 어디에 붙여?
A. Controller Method에서 Request DTO 앞에 붙여 요청 검증을 트리거한다.

Q. DTO에 `@NotBlank`가 있으면 `@Valid` 없어도 돼?
A. 아니다. Controller Parameter에 `@Valid`를 붙여야 검증이 실행된다.

Q. Validation 실패는 어디서 처리해?
A. GlobalExceptionHandler에서 MethodArgumentNotValidException 등을 처리해 공통 에러 응답으로 변환한다.

Q. Validation과 비즈니스 검증 차이는?
A. Validation은 형식과 기본 제약 검증이고 비즈니스 검증은 중복, 권한, 상태 전환 같은 도메인 규칙 검증이다.

---

# 8. Controller Troubleshooting

## 8.1 404 Mapping Not Found

### [개념]

404 Mapping Not Found는 요청 URL과 HTTP Method에 맞는 Controller Method를 찾지 못하는 문제다.

Controller Mapping 문제, Frontend URL 문제, Security 설정 문제, SPA Routing 문제가 원인일 수 있다.

---

### [핵심]

주요 원인:

- URL 오타
- HTTP Method 불일치
- Controller `@RequestMapping` prefix 불일치
- Method Mapping 누락
- Controller Bean 등록 실패
- Frontend Axios baseURL 불일치
- API Prefix 누락
- 단수 / 복수 URL 혼용
- PathVariable 경로 누락
- Security에서 차단
- SPA Routing 문제와 혼동

Debug Flow:

```text
Frontend Request URL 확인
→ HTTP Method 확인
→ Axios baseURL 확인
→ Controller @RequestMapping 확인
→ Method Mapping 확인
→ 최종 URL 조합 확인
→ Controller Bean 등록 확인
→ Security 차단 여부 확인
→ SPA Routing 문제와 구분
```

---

### [실무]

문제 예:

```java
@RestController
@RequestMapping("/api/festivals")
public class FestivalController {

    @GetMapping("/{festivalId}")
    public ApiResponse<FestivalResponse> getFestival(
            @PathVariable Long festivalId
    ) {
        ...
    }
}
```

Frontend 요청:

```javascript
publicApi.get("/api/festival/1");
```

실제 Mapping:

```text
GET /api/festivals/1
```

요청 URL:

```text
GET /api/festival/1
```

결과:

```text
404 Not Found
```

해결:

```javascript
publicApi.get("/api/festivals/1");
```

또는 Controller Prefix 통일:

```java
@RequestMapping("/api/festival")
```

주의:

- 프로젝트 전체에서 `/festival` 또는 `/festivals` 중 하나로 통일한다.
- API Prefix `/api`가 Axios baseURL에 이미 포함되어 있는지 확인한다.
- Controller가 Main Class 하위 패키지에 있는지 확인한다.

---

### [FAQ]

Q. 404가 나면 무조건 Controller가 없는 거야?
A. 아니다. URL, HTTP Method, prefix, Security, Frontend baseURL, SPA routing 문제를 함께 확인해야 한다.

Q. Frontend에서는 맞게 호출한 것 같은데 404가 나면?
A. Axios baseURL과 Controller `@RequestMapping`을 합친 최종 URL을 비교해야 한다.

Q. `/festival`과 `/festivals` 차이도 404 원인이야?
A. 맞다. 단수 / 복수 URL이 다르면 다른 경로로 인식된다.

Q. Controller가 있는데 Mapping이 안 잡히면?
A. Main Class 위치, Component Scan 범위, `@RestController` Annotation을 확인한다.

---

## 8.2 400 Binding Error

### [개념]

400 Binding Error는 Client 요청 값이 Controller Parameter 또는 Request DTO에 제대로 변환되지 않을 때 발생한다.

RequestBody, RequestParam, PathVariable, ModelAttribute Binding 문제에서 자주 발생한다.

---

### [핵심]

주요 원인:

- JSON 형식 오류
- Content-Type 누락
- `@RequestBody` 누락
- JSON 필드명 불일치
- DTO 필드 타입 불일치
- PathVariable 타입 불일치
- RequestParam 타입 불일치
- 날짜 포맷 불일치
- Validation 실패
- record / 생성자 Binding 문제
- Jackson 변환 오류

Debug Flow:

```text
Request Payload 확인
→ Content-Type 확인
→ Controller Parameter Annotation 확인
→ DTO Field Name 확인
→ DTO Field Type 확인
→ Date Format 확인
→ Validation Error 확인
→ Jackson Error 확인
```

---

### [실무]

문제 예:

```java
public record PostCreateRequest(
        String title,
        String content
) {
}
```

Controller:

```java
@PostMapping
public ApiResponse<PostResponse> createPost(
        @RequestBody PostCreateRequest request
) {
    ...
}
```

잘못된 JSON:

```json
{
  "postTitle": "Spring",
  "postContent": "Boot"
}
```

DTO 필드:

```text
title
content
```

결과:

```text
request.title() == null
request.content() == null
```

해결:

```json
{
  "title": "Spring",
  "content": "Boot"
}
```

PathVariable 타입 오류:

```text
GET /api/posts/abc
```

Controller:

```java
@GetMapping("/{postId}")
public ApiResponse<PostResponse> getPost(@PathVariable Long postId) {
    ...
}
```

결과:

```text
400 Bad Request
```

원인:

```text
abc를 Long으로 변환할 수 없음
```

---

### [FAQ]

Q. 400 Bad Request가 나면 뭘 확인해?
A. Request Body, Content-Type, DTO 필드명, JSON 형식, 타입 변환, Validation 실패 여부를 확인한다.

Q. RequestBody 값이 null로 들어오면?
A. `@RequestBody` 누락, JSON 필드명 불일치, Content-Type, DTO 구조, Jackson 변환 오류를 확인한다.

Q. PathVariable에 문자를 넣으면?
A. Controller Parameter가 Long 같은 숫자 타입이면 타입 변환 실패로 400이 발생할 수 있다.

Q. 날짜 값이 Binding 안 되면?
A. 요청 날짜 형식과 DTO 필드 타입, Date Format 설정을 확인해야 한다.

---

## 8.3 405 Method Not Allowed

### [개념]

405 Method Not Allowed는 URL Path는 존재하지만 HTTP Method가 맞지 않을 때 발생한다.

예를 들어 Controller는 POST만 지원하는데 Client가 GET으로 요청하면 405가 발생할 수 있다.

---

### [핵심]

주요 원인:

- HTTP Method 불일치
- Frontend Axios method 오류
- Form submit method 오류
- Controller Mapping Annotation 오류
- Preflight OPTIONS 처리 문제
- API 문서와 실제 Mapping 불일치

Debug Flow:

```text
Request URL 확인
→ Request HTTP Method 확인
→ Controller Mapping Method 확인
→ Axios 호출 함수 확인
→ Swagger / API 문서 비교
→ CORS Preflight 여부 확인
```

---

### [실무]

Controller:

```java
@PostMapping("/login")
public ApiResponse<LoginResponse> login(
        @RequestBody LoginRequest request
) {
    ...
}
```

잘못된 요청:

```text
GET /api/auth/login
```

결과:

```text
405 Method Not Allowed
```

해결:

```text
POST /api/auth/login
```

Axios:

```javascript
axios.post("/api/auth/login", request);
```

비슷한 문제:

```java
@GetMapping("/{postId}")
public ApiResponse<PostResponse> getPost(@PathVariable Long postId) {
    ...
}
```

삭제 요청을 보냄:

```text
DELETE /api/posts/1
```

결과:

```text
405 또는 404
```

해결:

```java
@DeleteMapping("/{postId}")
public ApiResponse<Void> deletePost(@PathVariable Long postId) {
    ...
}
```

---

### [FAQ]

Q. 405 Method Not Allowed는 뭐야?
A. URL은 맞지만 HTTP Method가 Controller Mapping과 맞지 않을 때 발생한다.

Q. 405가 나면 뭘 확인해?
A. Frontend 요청 Method와 Controller의 `@GetMapping`, `@PostMapping`, `@PatchMapping`, `@DeleteMapping`을 비교한다.

Q. 로그인은 GET이야 POST야?
A. 일반적으로 로그인처럼 Body와 인증 처리가 필요한 요청은 POST를 사용한다.

Q. CORS Preflight도 405 원인이 될 수 있어?
A. OPTIONS 요청 처리가 맞지 않으면 관련 문제가 생길 수 있다. CORS 설정을 확인해야 한다.

---

# 9. Controller Anti Pattern

## 9.1 Controller Anti Pattern Rules

### [개념]

Controller Anti Pattern은 Controller가 HTTP 요청 / 응답 책임을 넘어 Business Logic, Data Access, Exception Handling을 직접 처리하는 구조 문제다.

Controller가 두꺼워지면 Application 전체 구조가 무너진다.

---

### [핵심]

Anti Pattern:

- Fat Controller
- Controller에서 Repository 직접 호출
- Controller에서 Entity 생성 / 수정
- Controller에서 Entity 직접 반환
- Controller에서 try-catch 반복
- Controller에서 Token Parsing 반복
- Controller에서 외부 API 직접 호출
- Controller에서 Transaction 처리
- Controller에서 복잡한 if / else Business Rule 처리
- Controller Method가 지나치게 길어짐
- Request DTO 없이 Map으로 요청 수신
- Response 형식이 Method마다 다름

---

### [실무]

Anti Pattern 예:

```java
@PostMapping("/orders")
public ApiResponse<OrderResponse> createOrder(@RequestBody Map<String, Object> body) {
    Long userId = Long.valueOf(body.get("userId").toString());
    Long productId = Long.valueOf(body.get("productId").toString());

    User user = userRepository.findById(userId).orElseThrow();
    Product product = productRepository.findById(productId).orElseThrow();

    if (product.getStock() <= 0) {
        return ApiResponse.fail("OUT_OF_STOCK", "재고가 없습니다.");
    }

    product.decreaseStock();
    Order order = orderRepository.save(new Order(user, product));

    return ApiResponse.success(OrderResponse.from(order));
}
```

문제:

- Map으로 요청 수신
- Controller에서 Repository 직접 호출
- Business Rule 처리
- Entity 변경
- Error Response 직접 생성
- Transaction Boundary 불명확

개선:

```java
@PostMapping("/orders")
public ApiResponse<OrderResponse> createOrder(
        @Valid @RequestBody OrderCreateRequest request
) {
    return ApiResponse.success(orderService.createOrder(request));
}
```

Service에서 처리:

```java
@Transactional
public OrderResponse createOrder(OrderCreateRequest request) {
    User user = userRepository.findById(request.userId())
            .orElseThrow(() -> new BusinessException(ErrorCode.USER_NOT_FOUND));

    Product product = productRepository.findById(request.productId())
            .orElseThrow(() -> new BusinessException(ErrorCode.PRODUCT_NOT_FOUND));

    product.decreaseStock();

    Order order = orderRepository.save(Order.create(user, product));

    return OrderResponse.from(order);
}
```

---

### [FAQ]

Q. Fat Controller는 뭐야?
A. Controller에 Business Logic, Repository 호출, Entity 변경, 예외 처리가 과도하게 들어간 구조다.

Q. Controller에서 Map으로 Request를 받아도 돼?
A. 간단한 테스트는 가능하지만 실무 API에서는 Request DTO를 사용하는 것이 좋다.

Q. Controller에서 에러 응답을 직접 만들면 안 돼?
A. 반복되고 일관성이 깨질 수 있으므로 비즈니스 예외를 던지고 GlobalExceptionHandler에서 처리하는 것이 좋다.

Q. Controller가 길어지면 어떻게 해?
A. Business Logic은 Service로 이동하고 Request / Response 구조는 DTO로 분리한다.

---

# 10. Review Checklist

## 10.1 Controller and Mapping Checklist

### [개념]

Controller and Mapping Checklist는 Controller 구조, Request Mapping, Parameter Binding 문제를 검수하기 위한 기준이다.

Backend Agent와 Review Agent는 이 Checklist를 기준으로 Controller 문제를 탐지한다.

---

### [핵심]

Checklist:

```md
- [ ] REST API Controller에 @RestController를 사용했는가?
- [ ] Controller class level @RequestMapping base path가 명확한가?
- [ ] HTTP Method Mapping이 Use Case와 일치하는가?
- [ ] URI가 Resource 명사 중심으로 설계되었는가?
- [ ] 단수 / 복수 URL이 프로젝트 내에서 일관적인가?
- [ ] Frontend Axios URL과 Controller Mapping이 일치하는가?
- [ ] @PathVariable 이름과 Parameter 이름이 일치하는가?
- [ ] 검색 / 필터 조건에 @RequestParam 또는 @ModelAttribute를 적절히 사용했는가?
- [ ] JSON Body 요청에 @RequestBody를 사용했는가?
- [ ] Entity를 @RequestBody로 직접 받지 않는가?
- [ ] Request DTO 앞에 @Valid를 붙였는가?
- [ ] Response로 Entity를 직접 반환하지 않는가?
- [ ] Controller가 Service만 호출하는가?
- [ ] Controller에서 Repository를 직접 호출하지 않는가?
- [ ] Controller에 Business Logic이 없는가?
- [ ] Controller에서 Token Parsing을 반복하지 않는가?
- [ ] Controller에서 try-catch를 반복하지 않는가?
- [ ] 성공 응답 형식이 ApiResponse 등으로 통일되었는가?
- [ ] 실패 응답 처리를 GlobalExceptionHandler에 위임하는가?
- [ ] 목록 조회에서 Pageable, Page, Slice 선택 기준이 명확한가?
- [ ] 404 / 400 / 405 문제를 확인할 수 있는 Debug Flow가 있는가?
```

---

### [실무]

검수 흐름:

```text
Controller Annotation 확인
→ Base Path 확인
→ Method Mapping 확인
→ HTTP Method 확인
→ Parameter Binding 확인
→ Request DTO 확인
→ Validation Trigger 확인
→ Service Call 확인
→ Response DTO 확인
→ ApiResponse 확인
→ Anti Pattern 확인
→ Final Review
```

검수 결과 예:

```text
문제:
PostController가 PostRepository를 직접 호출함

위험:
Controller 책임 초과
Business Logic 위치 불명확
Transaction Boundary 불명확

수정:
PostService를 생성하고 Controller → Service → Repository 구조로 변경
```

검수 결과 예:

```text
문제:
Frontend는 /api/festival 호출, Controller는 /api/festivals 사용

위험:
404 Not Found 발생

수정:
Controller Prefix 또는 Frontend URL을 하나로 통일
```

---

### [FAQ]

Q. Controller 검수에서 가장 중요한 것은?
A. Mapping 일치, Request DTO 사용, Service 호출 구조, Entity 직접 노출 금지, Controller Thin Rule 준수다.

Q. Mapping 검수는 어떻게 해?
A. Frontend 요청 URL, Axios baseURL, Controller `@RequestMapping`, Method Mapping, HTTP Method를 합쳐 최종 URL을 비교한다.

Q. Binding 검수는 어떻게 해?
A. Parameter Annotation, JSON 필드명, DTO 필드 타입, Content-Type, Validation Annotation을 확인한다.

Q. Controller Anti Pattern은 어떻게 찾나?
A. Repository 직접 호출, Entity 반환, Map Request, try-catch 반복, Business Logic 포함 여부를 확인한다.

---

# 11. Part02 Final Goal

## 11.1 Controller and Request Mapping Final Goal

### [개념]

Spring Boot Part02의 최종 목표는 Backend Agent가 Controller와 Request Mapping을 일관되게 설계하고 Review Agent가 Mapping / Binding / Controller 책임 문제를 탐지하도록 만드는 것이다.

Part02는 HTTP Request가 Application Use Case로 연결되는 진입점을 다룬다.

---

### [핵심]

Part02가 지원해야 하는 작업:

- REST Controller 설계
- `@Controller` / `@RestController` 구분
- Base Path 설계
- HTTP Method Mapping 설계
- REST URL Naming 적용
- `@PathVariable` 적용
- `@RequestParam` 적용
- `@RequestBody` 적용
- `@ModelAttribute` 적용
- `@RequestHeader` 적용
- Controller Method Signature 설계
- ApiResponse 반환 기준 적용
- Pageable 목록 조회 설계
- Validation Trigger 적용
- 404 Mapping 문제 분석
- 400 Binding 문제 분석
- 405 Method 문제 분석
- Controller Anti Pattern 탐지

---

### [실무]

Backend Agent 수행 흐름:

```text
User API Request
→ Identify Resource
→ Choose HTTP Method
→ Design Base Path
→ Design Method Mapping
→ Choose Parameter Binding
→ Create Request DTO
→ Apply @Valid
→ Call Service
→ Return Response DTO
→ Wrap ApiResponse
→ Review Controller Thin Rule
```

Review Agent 수행 흐름:

```text
Input Controller Code
→ Check @RestController
→ Check @RequestMapping
→ Check HTTP Method
→ Check URL Naming
→ Check Parameter Binding
→ Check Request DTO
→ Check Validation
→ Check Service Call
→ Check Response DTO
→ Detect Repository Direct Call
→ Detect Entity Exposure
→ Detect Mapping Mismatch
→ Suggest Fix
```

---

### [FAQ]

Q. Spring Boot Part02의 최종 목적은 뭐야?
A. Controller와 Request Mapping을 일관되게 설계하고 Mapping, Binding, Controller 책임 문제를 탐지하게 만드는 것이다.

Q. Part02 다음에는 어떤 문서가 이어져야 해?
A. DTO & ApiResponse 문서가 이어지는 것이 좋다.

Q. Part02만으로 REST API를 만들 수 있어?
A. 기본 Controller Mapping은 가능하지만 DTO 설계, Validation, Exception Handling, Transaction은 후속 Part와 함께 사용해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Spring Boot Controller는 뭐야?
A. HTTP 요청을 받고 Request DTO를 Binding한 뒤 Service를 호출하고 Response DTO 또는 ApiResponse를 반환하는 Layer다.

Q. Controller는 어디까지 해야 해?
A. 요청을 받고 검증을 트리거한 뒤 Service를 호출하고 응답을 반환하는 정도가 적합하다.

Q. Controller에서 Repository를 바로 호출해도 돼?
A. 실무 구조에서는 Service를 거쳐 비즈니스 로직과 트랜잭션 경계를 관리하는 것이 좋다.

Q. Controller에 비즈니스 로직이 많으면 왜 문제야?
A. HTTP 책임과 비즈니스 책임이 섞이고 테스트와 유지보수가 어려워진다.

Q. `@Controller`와 `@RestController` 차이는?
A. `@Controller`는 View 반환에 주로 사용하고 `@RestController`는 JSON 응답 API에 사용한다.

Q. REST API에서는 `@Controller`와 `@RestController` 중 무엇을 써?
A. JSON API라면 `@RestController`를 사용하는 것이 좋다.

Q. `@RequestMapping`은 뭐야?
A. HTTP Method와 URL Path를 Controller Method에 연결하는 Mapping Annotation이다.

Q. `@RequestMapping`은 어디에 붙여?
A. 보통 Controller class level에는 base path를, method level에는 세부 path를 지정한다.

Q. `@GetMapping`은 언제 써?
A. Resource 조회 API에 사용한다.

Q. `@PostMapping`은 언제 써?
A. Resource 생성이나 로그인처럼 Body 기반 처리 요청에 사용한다.

Q. `@PutMapping`과 `@PatchMapping` 차이는?
A. 전체 교체는 PUT, 일부 필드 수정은 PATCH가 적합하다.

Q. `@DeleteMapping`은 언제 써?
A. Resource 삭제 요청에 사용한다.

Q. GET 요청에 RequestBody를 써도 돼?
A. 권장하지 않는다. Query Parameter나 PathVariable을 사용한다.

Q. `@PathVariable`은 언제 써?
A. URL 경로에 포함된 Resource 식별자를 받을 때 사용한다.

Q. `@PathVariable`과 `@RequestParam` 차이는?
A. `@PathVariable`은 URL 경로 일부를 받고 `@RequestParam`은 query string 값을 받는다.

Q. PathVariable 이름과 Parameter 이름은 같아야 해?
A. 같게 작성하는 것이 좋다. 다르면 `@PathVariable("postId")`처럼 명시한다.

Q. `@RequestParam`은 언제 써?
A. Query String으로 전달되는 검색, 필터, 페이지, 정렬 조건을 받을 때 사용한다.

Q. Query Parameter가 없어도 되게 하려면?
A. `@RequestParam(required = false)`를 사용한다.

Q. RequestParam 기본 값을 주려면?
A. `@RequestParam(defaultValue = "10")`처럼 사용한다.

Q. 검색 조건이 많으면 어떻게 해?
A. `@ModelAttribute`로 검색 조건 DTO를 받거나 복잡한 조건은 POST Body 검색을 검토한다.

Q. `@RequestBody`는 언제 써?
A. JSON Body 요청을 Request DTO로 받을 때 사용한다.

Q. RequestBody 값이 null이면 뭘 확인해?
A. Content-Type, `@RequestBody` 누락, JSON 필드명, DTO 구조, Jackson 변환 오류를 확인한다.

Q. Entity를 RequestBody로 받아도 돼?
A. 권장하지 않는다. Request DTO를 따로 만들어 API 입력 구조를 분리하는 것이 좋다.

Q. `@RequestBody`와 `@Valid`를 같이 써야 해?
A. Request DTO 검증이 필요하면 `@Valid @RequestBody` 형태로 사용한다.

Q. `@ModelAttribute`는 언제 써?
A. Query Parameter나 Form 데이터를 객체로 바인딩할 때 사용한다.

Q. GET 검색 API에서 DTO를 받을 수 있어?
A. 가능하다. `@ModelAttribute`를 사용하면 Query Parameter를 DTO로 바인딩할 수 있다.

Q. JSON Body도 `@ModelAttribute`로 받아?
A. 아니다. JSON Body는 `@RequestBody`로 받는다.

Q. `@RequestHeader`는 언제 써?
A. HTTP Header 값을 Controller에서 직접 받아야 할 때 사용한다.

Q. Authorization Header를 Controller에서 파싱해도 돼?
A. 반복 파싱은 권장하지 않는다. 인증 처리는 Security Filter에서 처리하는 것이 좋다.

Q. Controller Method는 어떤 형태가 좋아?
A. Request DTO를 받고 Service를 호출한 뒤 Response DTO 또는 ApiResponse를 반환하는 형태가 좋다.

Q. Controller Method에 HttpServletRequest를 받아도 돼?
A. 가능하지만 불필요하게 Servlet API에 의존하지 않도록 필요한 값만 Annotation으로 받는 것이 좋다.

Q. 인증 사용자 정보는 userId를 RequestBody로 받아?
A. 인증된 사용자 기준 작업이라면 RequestBody의 userId보다 SecurityContext나 인증 Principal에서 가져오는 것이 안전하다.

Q. Controller에서 ApiResponse만 반환해도 돼?
A. 프로젝트 규칙이 성공 응답은 ApiResponse 직접 반환하고 실패는 GlobalExceptionHandler가 처리하는 구조라면 가능하다.

Q. ResponseEntity는 언제 써?
A. HTTP 상태 코드, Header, Created Location 등 HTTP 응답을 세밀하게 제어해야 할 때 유용하다.

Q. REST URL은 어떻게 짓는 게 좋아?
A. Resource는 명사로 표현하고 동작은 HTTP Method로 표현하는 것이 좋다.

Q. `/getUsers` 같은 URL은 안 좋아?
A. REST 스타일에서는 동사보다 `GET /users`처럼 Method와 Resource 조합을 선호한다.

Q. 단수와 복수 URL 중 뭐가 좋아?
A. 프로젝트 내에서 통일하는 것이 중요하며 일반적으로 복수형 Resource를 많이 사용한다.

Q. Base Path는 어디에 지정해?
A. 보통 Controller class level `@RequestMapping`에 지정한다.

Q. `/api` Prefix는 꼭 붙여야 해?
A. 필수는 아니지만 API와 View Route를 구분하기 위해 사용하는 경우가 많다.

Q. `/festival`과 `/festivals`가 섞이면 문제야?
A. 문제가 될 수 있다. Controller Mapping과 Frontend 요청 URL이 다르면 404가 발생한다.

Q. Pageable은 Controller에서 바로 받아도 돼?
A. 가능하다. 다만 기본 size, sort, 최대 size 정책을 정하는 것이 좋다.

Q. Page와 Slice 차이는?
A. Page는 전체 개수를 포함하고 Slice는 다음 페이지 존재 여부 중심이다. 무한 스크롤은 Slice가 적합할 수 있다.

Q. `@Valid`는 어디에 붙여?
A. Controller Method에서 Request DTO 앞에 붙여 요청 검증을 트리거한다.

Q. DTO에 `@NotBlank`가 있으면 `@Valid` 없어도 돼?
A. 아니다. Controller Parameter에 `@Valid`를 붙여야 검증이 실행된다.

Q. 404가 나면 뭘 확인해?
A. URL, HTTP Method, Controller prefix, Method Mapping, Frontend baseURL, Security 차단 여부를 확인한다.

Q. 400 Bad Request가 나면 뭘 확인해?
A. Request Body, Content-Type, DTO 필드명, JSON 형식, 타입 변환, Validation 실패 여부를 확인한다.

Q. 405 Method Not Allowed는 뭐야?
A. URL은 맞지만 HTTP Method가 Controller Mapping과 맞지 않을 때 발생한다.

Q. Fat Controller는 뭐야?
A. Controller에 Business Logic, Repository 호출, Entity 변경, 예외 처리가 과도하게 들어간 구조다.

Q. Controller에서 Map으로 Request를 받아도 돼?
A. 간단한 테스트는 가능하지만 실무 API에서는 Request DTO를 사용하는 것이 좋다.

Q. Controller 검수에서 가장 중요한 것은?
A. Mapping 일치, Request DTO 사용, Service 호출 구조, Entity 직접 노출 금지, Controller Thin Rule 준수다.

Q. Spring Boot Part02 다음에는 뭐가 좋아?
A. DTO & ApiResponse 문서가 이어지는 것이 좋다.
