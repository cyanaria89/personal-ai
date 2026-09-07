# API Design Part 03 - Request, Response & Contract Design

---

# 1. Request Contract

## 1.1 Request

### [개념]

Request는 Client가 Server에 전달하는 요청 정보이다.

API Request Contract는 Client가 어떤 형식으로 데이터를 보내야 하는지 정의하는 규칙이다.

Request는 보통 Header, Path Variable, Query Parameter, Body로 구성된다.

```text
Client
→ Request Header
→ Path Variable
→ Query Parameter
→ Request Body
→ Server
```

---

### [핵심]

- Request는 API 입력 Contract이다.
- Request 구조는 API 문서에 명확히 정의해야 한다.
- Request Header는 인증, Content-Type, Client 정보를 전달한다.
- Path Variable은 Resource Identifier를 전달한다.
- Query Parameter는 검색, 필터링, 정렬, 페이지 조건을 전달한다.
- Request Body는 생성, 수정, Command 데이터를 전달한다.
- Request Contract가 불명확하면 Frontend / Backend 연동 오류가 발생한다.

---

### [실무]

2026 실무 기준 Request Contract는 OpenAPI 3.x 또는 Swagger UI로 문서화한다.

Spring Boot 3.x API에서는 Request DTO를 사용하여 입력 구조를 고정한다.

```java
public record ReviewCreateRequest(
        Long festivalId,
        Integer rating,
        String content
) {
}
```

Controller는 Request DTO를 통해 입력을 받고 Validation을 적용한다.

```java
@PostMapping("/reviews")
public ApiResponse<ReviewResponse> createReview(
        @Valid @RequestBody ReviewCreateRequest request
) {
    return ApiResponse.success(reviewService.createReview(request));
}
```

Request Contract에는 다음 항목을 포함한다.

| 항목            | 설명                        |
| --------------- | --------------------------- |
| Method          | HTTP Method                 |
| URI             | Resource 경로               |
| Header          | Authorization, Content-Type |
| Path Variable   | Resource Identifier         |
| Query Parameter | 조회 조건                   |
| Request Body    | 생성/수정 데이터            |
| Validation Rule | 입력 검증 규칙              |

---

### [FAQ]

Q. Request Contract란 무엇인가?

A. Client가 Server에 어떤 입력을 어떤 형식으로 보내야 하는지 정의한 API 입력 규칙이다.

Q. Request Contract에 포함되는 것은 무엇인가?

A. Header, Path Variable, Query Parameter, Request Body, Validation Rule이 포함된다.

Q. Request DTO를 사용하는 이유는 무엇인가?

A. API 입력 구조를 고정하고 Entity 직접 노출을 방지하며 Validation을 적용하기 위해서이다.

---

# 2. Request Header

## 2.1 Header

### [개념]

Request Header는 Client가 Server에 전달하는 부가 정보이다.

Header는 인증 정보, Content-Type, Accept, Client Metadata 등을 전달한다.

```http
GET /users/me HTTP/1.1
Authorization: Bearer access-token
Accept: application/json
```

---

### [핵심]

- Header는 Request Metadata를 전달한다.
- Authorization Header는 인증 Token을 전달한다.
- Content-Type은 Request Body 형식을 나타낸다.
- Accept는 Client가 원하는 Response 형식을 나타낸다.
- Header는 API Contract에 명확히 문서화해야 한다.
- 민감한 인증 정보는 Query Parameter가 아니라 Header에 담는다.

---

### [실무]

JWT Authentication을 사용하는 API는 Authorization Header를 사용한다.

```http
Authorization: Bearer eyJhbGciOiJIUzI1NiJ9...
```

JSON Request Body를 사용하는 API는 Content-Type을 명시한다.

```http
Content-Type: application/json
```

Spring Security + JWT 구조에서는 Filter에서 Authorization Header를 읽고 Token을 검증한다.

```text
Request
→ Authorization Header
→ JWT Filter
→ Token Validation
→ SecurityContext
→ Controller
```

---

### [주의]

- Access Token을 Query Parameter로 전달하지 않는다.
- Content-Type 누락 시 Request Body Binding 오류가 발생할 수 있다.
- Header 이름은 표준 이름을 우선 사용한다.
- Custom Header는 남용하지 않는다.
- Header 기반 Versioning을 사용할 경우 문서화가 필수이다.

---

### [FAQ]

Q. Authorization Header는 무엇인가?

A. Client 인증 정보를 Server에 전달하는 Header이다.

Q. JWT는 어디에 담아 보내는가?

A. 보통 `Authorization: Bearer access-token` 형식으로 Request Header에 담는다.

Q. Content-Type은 왜 필요한가?

A. Server가 Request Body 형식을 올바르게 해석하기 위해 필요하다.

---

# 3. Path Variable Contract

## 3.1 Path Variable

### [개념]

Path Variable은 URI 경로에 포함되는 Resource Identifier이다.

Path Variable은 특정 Resource를 조회, 수정, 삭제할 때 사용한다.

```text
/users/{userId}
/festivals/{festivalId}
/reviews/{reviewId}
```

---

### [핵심]

- Path Variable은 Resource 식별자이다.
- Path Variable은 필수 값이다.
- Path Variable 이름은 구체적으로 작성한다.
- `{id}`보다 `{userId}`, `{festivalId}`를 권장한다.
- Path Variable Type은 API 문서에 명확히 작성한다.
- Path Variable은 Query Parameter와 역할이 다르다.

---

### [실무]

Spring Boot 3.x에서는 `@PathVariable`로 Path Variable을 바인딩한다.

```java
@GetMapping("/festivals/{festivalId}")
public ApiResponse<FestivalDetailResponse> getFestival(
        @PathVariable Long festivalId
) {
    return ApiResponse.success(festivalService.getFestival(festivalId));
}
```

Path Variable Contract에는 다음 항목을 명시한다.

| 항목        | 예시                         |
| ----------- | ---------------------------- |
| Name        | festivalId                   |
| Type        | Long                         |
| Required    | true                         |
| Description | Festival Resource Identifier |

---

### [FAQ]

Q. Path Variable은 언제 사용하는가?

A. 특정 Resource를 식별해야 할 때 사용한다.

Q. Path Variable 이름은 어떻게 작성하는가?

A. `{id}`보다 `{userId}`, `{festivalId}`처럼 Resource 의미가 드러나게 작성한다.

Q. Path Variable을 선택 조건으로 사용해도 되는가?

A. 권장하지 않는다. 선택 조건은 Query Parameter로 분리한다.

---

# 4. Query Parameter Contract

## 4.1 Query Parameter

### [개념]

Query Parameter는 Resource 조회 조건을 전달하는 Request 요소이다.

검색, 필터링, 정렬, 페이지 조건은 Query Parameter로 표현한다.

```text
/festivals?keyword=music&region=seoul&page=0&size=20
```

---

### [핵심]

- Query Parameter는 조회 조건이다.
- Query Parameter는 Optional 조건에 적합하다.
- Search, Filter, Sort, Page 조건에 사용한다.
- Query Parameter 이름은 일관되게 작성한다.
- 조건이 많으면 Search Request DTO로 묶는다.
- Query Parameter는 Resource Identifier 대체용으로 남용하지 않는다.

---

### [실무]

단순 조건은 `@RequestParam`을 사용한다.

```java
@GetMapping("/festivals")
public ApiResponse<Page<FestivalResponse>> getFestivals(
        @RequestParam(required = false) String keyword,
        @RequestParam(required = false) String region,
        Pageable pageable
) {
    return ApiResponse.success(festivalService.getFestivals(keyword, region, pageable));
}
```

조건이 많으면 `@ModelAttribute` Request DTO를 사용한다.

```java
public record FestivalSearchRequest(
        String keyword,
        String region,
        String theme,
        LocalDate startDate,
        LocalDate endDate
) {
}
```

```java
@GetMapping("/festivals/search")
public ApiResponse<Page<FestivalResponse>> searchFestivals(
        @ModelAttribute FestivalSearchRequest request,
        Pageable pageable
) {
    return ApiResponse.success(festivalService.searchFestivals(request, pageable));
}
```

---

### [Best Practice]

- `page`, `size`, `sort` 이름을 표준화한다.
- 날짜 조건은 `startDate`, `endDate`처럼 의미 있게 작성한다.
- 검색어는 `keyword` 또는 `q` 중 하나로 통일한다.
- Boolean 조건은 `active=true`처럼 명확히 작성한다.
- 다중 조건 검색은 DTO로 묶어 관리한다.

---

### [FAQ]

Q. Query Parameter는 언제 사용하는가?

A. 검색, 필터링, 정렬, 페이지 조건을 전달할 때 사용한다.

Q. Query Parameter가 많아지면 어떻게 처리하는가?

A. Search Request DTO로 묶고 `@ModelAttribute`로 바인딩한다.

Q. Query Parameter와 Request Body의 차이는 무엇인가?

A. Query Parameter는 조회 조건에 사용하고 Request Body는 생성, 수정, Command 데이터에 사용한다.

---

# 5. Request Body Contract

## 5.1 Request Body

### [개념]

Request Body는 Client가 Server에 전달하는 본문 데이터이다.

생성, 수정, Command 요청에서 주로 사용한다.

```json
{
  "rating": 5,
  "content": "Great festival"
}
```

---

### [핵심]

- Request Body는 생성, 수정, Command 데이터에 사용한다.
- Request Body는 DTO로 받는다.
- Request Body는 Entity로 직접 받지 않는다.
- Request Body에는 Validation Rule을 적용한다.
- GET 요청에서는 Request Body를 사용하지 않는 것이 원칙이다.
- Request Body Schema는 API 문서에 명확히 정의해야 한다.

---

### [실무]

Spring Boot 3.x에서는 `@RequestBody`로 JSON Body를 DTO에 바인딩한다.

```java
@PostMapping("/festivals/{festivalId}/reviews")
public ApiResponse<ReviewResponse> createReview(
        @PathVariable Long festivalId,
        @Valid @RequestBody ReviewCreateRequest request
) {
    return ApiResponse.success(reviewService.createReview(festivalId, request));
}
```

Request DTO는 API 입력 전용으로 분리한다.

```java
public record ReviewCreateRequest(
        @NotNull Integer rating,
        @NotBlank String content
) {
}
```

Request Body Contract에는 Field Name, Type, Required, Validation, Description을 포함한다.

| Field   | Type    | Required | Validation |
| ------- | ------- | -------- | ---------- |
| rating  | Integer | true     | 1~5        |
| content | String  | true     | not blank  |

---

### [주의]

- Entity를 Request Body로 직접 받지 않는다.
- Request DTO와 Response DTO를 분리한다.
- GET API에서 Request Body에 의존하지 않는다.
- 민감 정보는 로그에 남지 않도록 주의한다.
- PATCH Request에서 null 처리 정책을 명확히 한다.

---

### [FAQ]

Q. Request Body는 언제 사용하는가?

A. Resource 생성, 수정, Command 요청처럼 데이터를 본문으로 전달해야 할 때 사용한다.

Q. Entity를 Request Body로 직접 받아도 되는가?

A. 권장하지 않는다. API Contract와 내부 Domain Model이 강하게 결합되기 때문이다.

Q. Request DTO와 Response DTO는 분리해야 하는가?

A. 분리하는 것이 좋다. 입력 구조와 출력 구조는 목적이 다르기 때문이다.

---

# 6. Response Contract

## 6.1 Response

### [개념]

Response는 Server가 Client 요청 처리 결과로 반환하는 응답 정보이다.

API Response Contract는 Client가 어떤 Status Code와 Body Schema를 받을 수 있는지 정의한다.

```text
Server
→ Status Code
→ Response Header
→ Response Body
→ Client
```

---

### [핵심]

- Response는 API 출력 Contract이다.
- Response는 Status Code와 Body Schema를 포함한다.
- Response Schema는 안정적으로 유지해야 한다.
- Success Response와 Error Response를 구분한다.
- Response Field 이름은 Frontend와 반드시 일치해야 한다.
- Response Contract 변경은 Breaking Change가 될 수 있다.

---

### [실무]

Spring Boot 3.x API에서는 Response DTO를 사용한다.

```java
public record FestivalResponse(
        Long festivalId,
        String title,
        String address,
        LocalDate eventStartDate,
        LocalDate eventEndDate
) {
}
```

Controller는 Entity가 아니라 Response DTO를 반환한다.

```java
@GetMapping("/festivals/{festivalId}")
public ApiResponse<FestivalResponse> getFestival(
        @PathVariable Long festivalId
) {
    return ApiResponse.success(festivalService.getFestival(festivalId));
}
```

Response Contract에는 다음 항목을 포함한다.

| 항목        | 설명                                        |
| ----------- | ------------------------------------------- |
| Status Code | 200, 201, 204, 400, 401, 403, 404, 409, 500 |
| Header      | Content-Type                                |
| Body        | Response DTO Schema                         |
| Error Body  | Error Code, Error Message                   |
| Pagination  | Page Metadata 또는 Cursor                   |

---

### [FAQ]

Q. Response Contract란 무엇인가?

A. Server가 Client에게 반환하는 Status Code, Header, Body Schema 규칙이다.

Q. Entity를 Response로 직접 반환해도 되는가?

A. 권장하지 않는다. 내부 구조 노출과 Contract 변경 위험이 크기 때문이다.

Q. Response Field 변경이 위험한 이유는 무엇인가?

A. Frontend가 기존 Field 이름과 구조에 의존하므로 화면 오류가 발생할 수 있기 때문이다.

---

# 7. Success Response Schema

## 7.1 Success Response

### [개념]

Success Response는 API 요청이 정상 처리되었을 때 반환하는 응답 구조이다.

Success Response Schema는 프로젝트 전체에서 일관되게 유지하는 것이 좋다.

```json
{
  "success": true,
  "data": {}
}
```

---

### [핵심]

- Success Response는 2xx Status Code와 함께 반환한다.
- Response Body는 DTO 기반으로 설계한다.
- 공통 Response Wrapper를 사용할 수 있다.
- 목록 응답에는 Pagination Metadata를 포함할 수 있다.
- Success Response와 Error Response 구조를 혼동하지 않는다.
- Field 이름은 camelCase를 권장한다.

---

### [실무]

공통 Response Wrapper 예시:

```java
public record ApiResponse<T>(
        boolean success,
        T data,
        String message
) {
    public static <T> ApiResponse<T> success(T data) {
        return new ApiResponse<>(true, data, null);
    }
}
```

단건 조회 응답 예시:

```json
{
  "success": true,
  "data": {
    "festivalId": 1,
    "title": "Seoul Music Festival"
  },
  "message": null
}
```

목록 조회 응답 예시:

```json
{
  "success": true,
  "data": {
    "content": [],
    "page": 0,
    "size": 20,
    "totalElements": 100,
    "totalPages": 5
  },
  "message": null
}
```

---

### [주의]

- API마다 Response Wrapper 구조를 다르게 만들지 않는다.
- Entity 전체를 그대로 반환하지 않는다.
- 필요 없는 내부 Field를 노출하지 않는다.
- 날짜 형식은 프로젝트 기준으로 통일한다.
- `data`, `result`, `body` 같은 Wrapper Field 이름을 혼용하지 않는다.

---

### [FAQ]

Q. Success Response Schema는 왜 통일해야 하는가?

A. Frontend 처리, API 테스트, Error Handling, 문서화가 쉬워지기 때문이다.

Q. 공통 Response Wrapper는 반드시 필요한가?

A. 필수는 아니지만 일관된 API Contract를 위해 많이 사용한다.

Q. 목록 응답에는 무엇을 포함해야 하는가?

A. content와 함께 page, size, totalElements, totalPages 같은 Pagination Metadata를 포함할 수 있다.

---

# 8. Error Response Schema

## 8.1 Error Response

### [개념]

Error Response는 API 요청이 실패했을 때 반환하는 응답 구조이다.

Error Response Contract는 Client가 실패 원인을 일관되게 처리할 수 있도록 도와준다.

```json
{
  "code": "FESTIVAL_NOT_FOUND",
  "message": "Festival not found"
}
```

---

### [핵심]

- Error Response는 실패 응답 Contract이다.
- Error Response는 Status Code와 의미가 일치해야 한다.
- Error Code는 서비스 내부 오류 식별자이다.
- Error Message는 Client 또는 사용자에게 전달 가능한 설명이다.
- Validation Error는 Field Error 정보를 포함할 수 있다.
- Error Response Schema는 전역으로 통일해야 한다.

---

### [실무]

Spring Boot 3.x에서는 GlobalExceptionHandler에서 Error Response를 통일한다.

```java
public record ErrorResponse(
        String code,
        String message
) {
}
```

```json
{
  "code": "INVALID_INPUT",
  "message": "Invalid request input"
}
```

Validation Error는 Field 단위 오류를 포함할 수 있다.

```json
{
  "code": "VALIDATION_FAILED",
  "message": "Validation failed",
  "errors": [
    {
      "field": "rating",
      "message": "rating must be between 1 and 5"
    }
  ]
}
```

---

### [Best Practice]

- Error Code는 대문자 Snake Case를 사용한다.
- Error Message는 짧고 명확하게 작성한다.
- Status Code와 Error Code 의미를 일치시킨다.
- 내부 Stack Trace를 Response에 포함하지 않는다.
- Validation Error는 Field Error 구조를 별도로 제공한다.
- GlobalExceptionHandler로 Error Response를 중앙화한다.

---

### [FAQ]

Q. Error Response Schema에는 무엇이 필요한가?

A. Error Code와 Error Message가 필요하고, Validation 실패에는 Field Error를 추가할 수 있다.

Q. Error Code와 Status Code는 같은가?

A. 아니다. Status Code는 HTTP 표준 코드이고 Error Code는 서비스 내부 오류 식별자이다.

Q. Error Response를 통일해야 하는 이유는 무엇인가?

A. Frontend Error Handling, 테스트, 문서화, 유지보수를 쉽게 하기 위해서이다.

---

# 9. Response DTO

## 9.1 Response DTO Design

### [개념]

Response DTO는 API가 Client에게 반환하는 출력 전용 객체이다.

Response DTO는 Entity를 외부 Contract에 맞게 변환한 API 표현 모델이다.

```text
Entity
→ Response DTO
→ API Response
→ Client
```

---

### [핵심]

- Response DTO는 출력 전용 객체이다.
- Entity를 직접 반환하지 않는다.
- Response DTO는 Client Use Case 기준으로 설계한다.
- Response DTO Field 이름은 API Contract와 일치해야 한다.
- Response DTO는 필요한 데이터만 포함한다.
- 민감 정보는 Response DTO에서 제외한다.

---

### [실무]

Entity와 Response DTO를 분리한다.

```java
public record UserResponse(
        Long userId,
        String email,
        String nickname
) {
}
```

Entity를 Response DTO로 변환한다.

```java
public UserResponse toUserResponse(User user) {
    return new UserResponse(
            user.getUserId(),
            user.getEmail(),
            user.getNickname()
    );
}
```

Frontend 화면 요구사항에 따라 Detail Response와 Summary Response를 분리한다.

```java
public record FestivalSummaryResponse(
        Long festivalId,
        String title,
        String thumbnailUrl
) {
}

public record FestivalDetailResponse(
        Long festivalId,
        String title,
        String address,
        String description,
        LocalDate eventStartDate,
        LocalDate eventEndDate
) {
}
```

---

### [주의]

- Password, Refresh Token, Internal Role 정보를 노출하지 않는다.
- Lazy Loading Entity를 그대로 JSON 직렬화하지 않는다.
- 순환 참조가 발생하는 Entity 관계를 직접 반환하지 않는다.
- 화면별로 필요한 응답 구조가 다르면 DTO를 분리한다.
- DTO 이름은 일관된 Naming Convention을 사용한다.

---

### [FAQ]

Q. Response DTO를 사용하는 이유는 무엇인가?

A. 내부 Entity 구조를 숨기고 API 출력 Contract를 안정적으로 유지하기 위해서이다.

Q. Summary Response와 Detail Response를 분리하는 이유는 무엇인가?

A. 목록 화면과 상세 화면이 필요한 데이터 범위가 다르기 때문이다.

Q. Entity를 직접 Response로 반환하면 어떤 문제가 생기는가?

A. 내부 구조 노출, 순환 참조, Lazy Loading 오류, 불필요한 Field 노출 문제가 발생할 수 있다.

---

# 10. Date Time Response Contract

## 10.1 Date Time Format

### [개념]

Date Time Response Contract는 날짜와 시간 데이터를 API에서 어떤 형식으로 주고받을지 정의하는 규칙이다.

날짜 형식이 통일되지 않으면 Frontend 표시, 정렬, 필터링, 검색에서 오류가 발생한다.

```json
{
  "eventStartDate": "2026-07-01",
  "createdAt": "2026-07-01T10:30:00"
}
```

---

### [핵심]

- 날짜 형식은 프로젝트 전체에서 통일한다.
- 날짜만 필요하면 `yyyy-MM-dd`를 사용한다.
- 날짜와 시간이 필요하면 ISO-8601 형식을 사용한다.
- Time Zone 정책을 명확히 한다.
- LocalDate와 LocalDateTime 사용 기준을 분리한다.
- Frontend와 Backend가 같은 Date Time Contract를 사용해야 한다.

---

### [실무]

Spring Boot 3.x에서는 LocalDate, LocalDateTime을 많이 사용한다.

```java
public record FestivalResponse(
        LocalDate eventStartDate,
        LocalDate eventEndDate,
        LocalDateTime createdAt
) {
}
```

API JSON 예시:

```json
{
  "eventStartDate": "2026-07-01",
  "eventEndDate": "2026-07-10",
  "createdAt": "2026-06-27T14:30:00"
}
```

Time Zone이 중요한 서비스는 UTC 저장 + Client Local Time 변환 정책을 권장한다.

한국 전용 서비스는 `Asia/Seoul` 기준을 명시할 수 있다.

---

### [주의]

- 날짜 문자열 형식을 API마다 다르게 쓰지 않는다.
- `2026/07/01`, `2026-07-01`, timestamp를 혼용하지 않는다.
- Time Zone이 필요한 API에서 LocalDateTime만 무조건 사용하지 않는다.
- Frontend 표시 형식과 Backend 저장 형식을 혼동하지 않는다.

---

### [FAQ]

Q. API 날짜 형식은 무엇을 권장하는가?

A. 날짜는 `yyyy-MM-dd`, 날짜와 시간은 ISO-8601 형식을 권장한다.

Q. LocalDate와 LocalDateTime은 어떻게 구분하는가?

A. 날짜만 필요하면 LocalDate, 시간까지 필요하면 LocalDateTime을 사용한다.

Q. Time Zone 정책은 왜 중요한가?

A. 사용자 지역, 예약 시간, 이벤트 시간 계산에서 오류를 방지하기 위해서이다.

---

# 11. Contract Stability

## 11.1 Stable Contract

### [개념]

Contract Stability는 API Request / Response 구조를 안정적으로 유지하는 원칙이다.

API Contract가 자주 깨지면 Frontend, Mobile, External Client가 함께 깨진다.

```text
API Field Changed
→ Frontend Mapping Error
→ UI Error
→ Deployment Issue
```

---

### [핵심]

- API Contract 변경은 신중하게 수행한다.
- Response Field 삭제는 Breaking Change가 될 수 있다.
- Field 이름 변경은 Frontend 오류를 만들 수 있다.
- Type 변경은 Client Parsing 오류를 만들 수 있다.
- Error Response 변경은 Error Handling 실패를 만들 수 있다.
- Contract 변경은 Versioning 또는 Backward Compatibility를 고려한다.

---

### [실무]

실무에서는 다음 변경을 Breaking Change로 본다.

| 변경                         | 위험도 |
| ---------------------------- | ------ |
| Response Field 삭제          | 높음   |
| Response Field 이름 변경     | 높음   |
| Response Field Type 변경     | 높음   |
| Error Code 변경              | 높음   |
| Required Request Field 추가  | 높음   |
| Optional Response Field 추가 | 낮음   |
| New Endpoint 추가            | 낮음   |

Contract 변경 시 대응 방법:

```text
Contract Change
→ Impact Check
→ Frontend Agreement
→ OpenAPI Update
→ Backward Compatibility
→ Versioning if needed
```

---

### [Best Practice]

- Response Field는 삭제보다 Deprecated 처리한다.
- 신규 Field는 Optional로 추가한다.
- Request Required Field 추가는 신중하게 한다.
- Error Code는 쉽게 변경하지 않는다.
- OpenAPI 문서를 먼저 수정한다.
- Frontend와 Contract 변경 시점을 합의한다.

---

### [FAQ]

Q. API Contract 변경이 위험한 이유는 무엇인가?

A. Frontend, Mobile, External Client가 기존 Contract에 의존하기 때문이다.

Q. Response Field 이름 변경은 Breaking Change인가?

A. 대부분 Breaking Change이다. Client Mapping 오류가 발생할 수 있다.

Q. 안전한 API 변경 방식은 무엇인가?

A. Optional Field 추가, Deprecated 처리, Versioning, Backward Compatibility 유지이다.

---

# 12. OpenAPI Contract Documentation

## 12.1 OpenAPI

### [개념]

OpenAPI는 REST API Contract를 표준 형식으로 문서화하는 Specification이다.

OpenAPI 문서는 URI, Method, Request, Response, Error Response, Security Scheme을 정의한다.

---

### [핵심]

- OpenAPI는 API Contract 문서화 표준이다.
- Swagger UI는 OpenAPI 기반 API 테스트 UI이다.
- OpenAPI 문서는 Frontend / Backend 협업 기준이 된다.
- API Contract 변경 시 OpenAPI 문서도 함께 변경해야 한다.
- OpenAPI 문서는 Request / Response Schema를 명확히 보여준다.

---

### [실무]

Spring Boot 3.x에서는 springdoc-openapi를 사용하여 Swagger UI를 구성할 수 있다.

OpenAPI 문서에 포함할 항목:

- API Summary
- API Description
- Path Variable
- Query Parameter
- Request Body Schema
- Response Body Schema
- Error Response Schema
- Authentication Requirement
- Status Code
- Example

API 문서와 실제 Controller 구현이 다르면 Contract Mismatch가 발생한다.

---

### [Best Practice]

- Swagger UI로 API Contract를 직접 테스트한다.
- Request / Response Example을 작성한다.
- Error Response Example을 작성한다.
- 인증 필요 API에는 Security Requirement를 표시한다.
- Pageable Parameter를 명확히 문서화한다.
- API 변경 시 문서를 먼저 업데이트한다.

---

### [FAQ]

Q. OpenAPI는 무엇인가?

A. REST API Contract를 표준 형식으로 문서화하는 Specification이다.

Q. Swagger UI는 무엇인가?

A. OpenAPI 문서를 기반으로 API를 확인하고 테스트할 수 있는 UI이다.

Q. OpenAPI 문서가 중요한 이유는 무엇인가?

A. Frontend / Backend 협업, API 테스트, Contract 검증의 기준이 되기 때문이다.

---

# 13. Common Mistakes

## 13.1 Request Response Contract Mistakes

### [Troubleshooting]

문제: Request Body를 Entity로 직접 받는다.

원인: API 입력 Contract와 내부 Domain Model을 분리하지 않았다.

해결: Request DTO를 만들고 `@RequestBody`로 DTO를 받는다.

---

문제: Response로 Entity를 직접 반환한다.

원인: API 출력 Contract와 내부 Entity 구조를 분리하지 않았다.

해결: Response DTO로 변환하여 필요한 Field만 반환한다.

---

문제: API마다 Success Response 구조가 다르다.

원인: 공통 Response Wrapper 또는 Response Convention이 없다.

해결: `ApiResponse<T>` 같은 공통 응답 구조를 정의한다.

---

문제: Error Response 구조가 API마다 다르다.

원인: GlobalExceptionHandler와 ErrorResponse Schema가 없다.

해결: Error Code, Error Message 기반 Error Response Contract를 통일한다.

---

문제: Validation Error Field 정보가 없다.

원인: Validation Exception 처리 구조가 부족하다.

해결: Field Error List를 포함한 Validation Error Response를 설계한다.

---

문제: Response Field 이름이 Frontend와 다르다.

원인: API Contract 합의 없이 Backend DTO가 변경되었다.

해결: OpenAPI 문서를 기준으로 Field 이름을 고정하고 변경 시 Frontend와 합의한다.

---

문제: 날짜 형식이 API마다 다르다.

원인: Date Time Contract가 정의되지 않았다.

해결: LocalDate는 `yyyy-MM-dd`, LocalDateTime은 ISO-8601 형식으로 통일한다.

---

문제: API 문서와 실제 응답이 다르다.

원인: OpenAPI 문서 업데이트가 누락되었다.

해결: Controller, DTO, OpenAPI 문서를 함께 검수한다.

---

### [FAQ]

Q. Request / Response Contract에서 가장 흔한 실수는 무엇인가?

A. Entity 직접 사용, DTO 분리 누락, Response Schema 불일치, Error Response 불일치, 날짜 형식 혼용이다.

Q. Contract Mismatch란 무엇인가?

A. API 문서, Backend 구현, Frontend 기대 구조가 서로 다른 상태이다.

Q. Contract Mismatch를 줄이는 방법은 무엇인가?

A. OpenAPI 문서화, DTO 분리, Response Schema 통일, Frontend / Backend Contract 합의가 필요하다.

---

# Retrieval Queries

### [FAQ]

Q. Request Contract란 무엇인가?
A. Client가 Server에 어떤 입력을 어떤 형식으로 보내야 하는지 정의한 API 입력 규칙이다.

Q. Request는 무엇으로 구성되는가?
A. Header, Path Variable, Query Parameter, Request Body로 구성된다.

Q. Request Header는 무엇인가?
A. 인증 정보, Content-Type, Accept 같은 Request Metadata를 전달하는 요소이다.

Q. Authorization Header는 무엇인가?
A. Client 인증 정보를 Server에 전달하는 Header이다.

Q. JWT는 어디에 담아 보내는가?
A. `Authorization: Bearer access-token` 형식으로 Request Header에 담는다.

Q. Content-Type은 왜 필요한가?
A. Server가 Request Body 형식을 올바르게 해석하기 위해 필요하다.

Q. Path Variable은 무엇인가?
A. URI 경로 안에서 특정 Resource를 식별하는 값이다.

Q. Query Parameter는 무엇인가?
A. 검색, 필터링, 정렬, 페이지 조건 같은 조회 조건을 전달하는 값이다.

Q. Request Body는 무엇인가?
A. Client가 Server에 전달하는 본문 데이터이며 생성, 수정, Command 요청에 사용한다.

Q. Request DTO를 사용하는 이유는 무엇인가?
A. 입력 구조를 고정하고 Entity 직접 노출을 방지하며 Validation을 적용하기 위해서이다.

Q. Response Contract란 무엇인가?
A. Server가 Client에게 반환하는 Status Code, Header, Body Schema 규칙이다.

Q. Response DTO를 사용하는 이유는 무엇인가?
A. 내부 Entity 구조를 숨기고 API 출력 Contract를 안정적으로 유지하기 위해서이다.

Q. Success Response Schema는 왜 통일해야 하는가?
A. Frontend 처리, 테스트, 문서화, 유지보수를 쉽게 하기 위해서이다.

Q. Error Response Schema에는 무엇이 필요한가?
A. Error Code, Error Message가 필요하고 Validation 실패에는 Field Error를 추가할 수 있다.

Q. Error Code와 Status Code는 같은가?
A. 아니다. Status Code는 HTTP 표준 코드이고 Error Code는 서비스 내부 오류 식별자이다.

Q. Entity를 Request Body로 직접 받아도 되는가?
A. 권장하지 않는다. API Contract와 내부 Domain Model이 강하게 결합되기 때문이다.

Q. Entity를 Response로 직접 반환해도 되는가?
A. 권장하지 않는다. 내부 구조 노출, 순환 참조, Lazy Loading 오류가 발생할 수 있다.

Q. API 날짜 형식은 무엇을 권장하는가?
A. 날짜는 `yyyy-MM-dd`, 날짜와 시간은 ISO-8601 형식을 권장한다.

Q. API Contract 변경이 위험한 이유는 무엇인가?
A. Frontend, Mobile, External Client가 기존 Contract에 의존하기 때문이다.

Q. Breaking Change란 무엇인가?
A. 기존 Client가 더 이상 정상 동작하지 않게 만드는 API Contract 변경이다.

Q. 안전한 API 변경 방식은 무엇인가?
A. Optional Field 추가, Deprecated 처리, Versioning, Backward Compatibility 유지이다.

Q. OpenAPI는 무엇인가?
A. REST API Contract를 표준 형식으로 문서화하는 Specification이다.

Q. Swagger UI는 무엇인가?
A. OpenAPI 문서를 기반으로 API를 확인하고 테스트할 수 있는 UI이다.

Q. Contract Mismatch란 무엇인가?
A. API 문서, Backend 구현, Frontend 기대 구조가 서로 다른 상태이다.

Q. Contract Mismatch를 줄이는 방법은 무엇인가?
A. OpenAPI 문서화, DTO 분리, Response Schema 통일, Frontend / Backend Contract 합의가 필요하다.
