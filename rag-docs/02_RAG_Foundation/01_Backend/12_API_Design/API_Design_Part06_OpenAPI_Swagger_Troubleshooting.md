# API Design Part 06 - OpenAPI, Swagger & API Troubleshooting

---

# 1. OpenAPI

## 1.1 OpenAPI Specification

### [개념]

OpenAPI는 REST API Contract를 표준 형식으로 정의하는 API Documentation Specification이다.

OpenAPI는 URI, HTTP Method, Request, Response, Status Code, Error Response, Authentication, Authorization 정보를 구조화한다.

```text
API Contract
→ OpenAPI Specification
→ Swagger UI
→ API Test / Review / Client Integration
```

---

### [핵심]

- OpenAPI는 API Contract 문서화 표준이다.
- OpenAPI는 REST API 설계와 검수 기준이 된다.
- OpenAPI는 Frontend / Backend 협업 기준이다.
- OpenAPI는 Swagger UI, Client Generator, API Test Tool과 연결된다.
- OpenAPI 문서와 실제 Controller 구현은 일치해야 한다.
- OpenAPI 문서 품질은 API Contract 품질에 직접 영향을 준다.
- OpenAPI 문서는 Success Response와 Error Response를 모두 포함해야 한다.

---

### [실무]

2026 실무 기준 Spring Boot 3.x 프로젝트에서는 OpenAPI 3.x 기반 문서화를 사용한다.

Spring Boot에서는 `springdoc-openapi`를 많이 사용한다.

OpenAPI 문서에 포함해야 할 핵심 정보:

- API Summary
- API Description
- HTTP Method
- URI
- Path Variable
- Query Parameter
- Request Header
- Request Body Schema
- Response Body Schema
- Error Response Schema
- Status Code
- Authentication Requirement
- Authorization Requirement
- Rate Limit Error
- Example

---

### [FAQ]

Q. OpenAPI란 무엇인가?

A. REST API Contract를 표준 형식으로 정의하는 API Documentation Specification이다.

Q. OpenAPI가 중요한 이유는 무엇인가?

A. API Contract, 협업, 테스트, 검수, Client 연동의 기준이 되기 때문이다.

Q. OpenAPI 문서에는 무엇이 포함되어야 하는가?

A. URI, Method, Request, Response, Status Code, Error Response, 인증, 권한, Example이 포함되어야 한다.

---

# 2. Swagger UI

## 2.1 Swagger UI

### [개념]

Swagger UI는 OpenAPI 문서를 시각적으로 확인하고 API를 직접 테스트할 수 있는 Web UI이다.

Swagger UI는 개발자가 API Contract를 빠르게 검증하는 도구이다.

```text
OpenAPI Spec
→ Swagger UI
→ API Documentation
→ API Test
```

---

### [핵심]

- Swagger UI는 OpenAPI 기반 API 테스트 UI이다.
- Swagger UI는 API 목록, Request Schema, Response Schema를 보여준다.
- Swagger UI는 Path Variable, Query Parameter, Request Body 테스트를 지원한다.
- Swagger UI는 JWT Bearer Token 인증 테스트를 지원할 수 있다.
- Swagger UI는 Frontend / Backend 협업 도구로 사용할 수 있다.
- Swagger UI 결과와 실제 API 동작이 다르면 Contract Mismatch이다.
- Swagger UI 테스트만으로 전체 API 시나리오 테스트를 대체할 수는 없다.

---

### [실무]

Spring Boot 3.x + springdoc-openapi 기준 Swagger UI는 API 개발 중 빠른 수동 테스트에 유용하다.

Swagger UI 사용 목적:

- API Contract 확인
- Request Body Schema 확인
- Query Parameter 확인
- Status Code 확인
- Error Response 확인
- JWT 인증 API 테스트
- Frontend 연동 전 Backend 단독 테스트

Swagger UI는 Postman을 완전히 대체하지는 않는다.

Swagger UI는 문서 기반 테스트에 강하고, Postman은 시나리오 기반 테스트와 환경 변수 관리에 강하다.

---

### [FAQ]

Q. Swagger UI란 무엇인가?

A. OpenAPI 문서를 기반으로 API를 확인하고 직접 테스트할 수 있는 Web UI이다.

Q. Swagger UI는 왜 사용하는가?

A. API Contract 확인, Request / Response 테스트, Frontend 협업을 쉽게 하기 위해 사용한다.

Q. Swagger UI와 Postman은 같은 도구인가?

A. 아니다. Swagger UI는 문서 기반 테스트에 강하고 Postman은 시나리오 테스트와 환경 관리에 강하다.

---

# 3. OpenAPI Schema Design

## 3.1 Schema

### [개념]

OpenAPI Schema는 Request Body, Response Body, Error Response의 데이터 구조를 정의하는 규칙이다.

Schema는 API Contract에서 Field 이름, Type, Required, Format, Example을 명확히 표현한다.

```text
Request DTO
→ OpenAPI Request Schema

Response DTO
→ OpenAPI Response Schema

ErrorResponse
→ OpenAPI Error Schema
```

---

### [핵심]

- Schema는 API 데이터 구조를 정의한다.
- Request Schema와 Response Schema는 분리한다.
- Error Response Schema를 공통으로 정의한다.
- Field Type과 Required 여부를 명확히 작성한다.
- 날짜 Format을 명확히 작성한다.
- Example을 포함하면 Frontend 연동 품질이 좋아진다.
- Rate Limit, Authentication, Authorization Error Schema도 문서화한다.

---

### [실무]

Request Schema 예시:

```json
{
  "email": "user@example.com",
  "password": "password1234",
  "nickname": "festivalUser"
}
```

Response Schema 예시:

```json
{
  "success": true,
  "data": {
    "userId": 1,
    "email": "user@example.com",
    "nickname": "festivalUser"
  },
  "message": null
}
```

Error Response Schema 예시:

```json
{
  "code": "USER_NOT_FOUND",
  "message": "User not found"
}
```

Validation Error Schema 예시:

```json
{
  "code": "VALIDATION_FAILED",
  "message": "Validation failed",
  "errors": [
    {
      "field": "email",
      "message": "email must be a valid email address"
    }
  ]
}
```

Rate Limit Error Schema 예시:

```json
{
  "code": "RATE_LIMIT_EXCEEDED",
  "message": "Too many requests"
}
```

---

### [Best Practice]

- Request DTO와 Response DTO를 같은 Schema로 쓰지 않는다.
- Entity Schema를 API Schema로 직접 노출하지 않는다.
- 공통 `ApiResponse<T>` Wrapper 구조를 문서화한다.
- 공통 `ErrorResponse` 구조를 문서화한다.
- Validation Error Schema를 별도로 문서화한다.
- 날짜, 시간, Enum, Nullable Field를 명확히 표시한다.
- 400, 401, 403, 404, 409, 429, 500 Error Schema를 상황별로 문서화한다.

---

### [FAQ]

Q. OpenAPI Schema란 무엇인가?

A. API Request Body, Response Body, Error Response의 데이터 구조를 정의하는 규칙이다.

Q. Request Schema와 Response Schema를 분리해야 하는가?

A. 분리하는 것이 좋다. 입력과 출력은 목적과 Field 구성이 다르기 때문이다.

Q. Error Response Schema도 OpenAPI에 작성해야 하는가?

A. 작성해야 한다. Client가 실패 응답을 일관되게 처리할 수 있기 때문이다.

---

# 4. OpenAPI Annotation

## 4.1 Springdoc Annotation

### [개념]

OpenAPI Annotation은 Controller, DTO, Parameter, Response에 API 문서 정보를 추가하는 Annotation이다.

Spring Boot 3.x에서는 springdoc-openapi와 Swagger Annotation을 사용해 API Contract를 문서화할 수 있다.

---

### [핵심]

- `@Operation`은 API 요약과 설명을 작성한다.
- `@Parameter`는 Path Variable, Query Parameter 설명을 작성한다.
- `@Schema`는 DTO Field 설명과 Example을 작성한다.
- `@ApiResponse`는 Status Code별 응답을 작성한다.
- `@SecurityRequirement`는 인증 필요 API를 표시한다.
- Annotation은 실제 코드와 문서의 간격을 줄인다.
- 프로젝트 공통 `ApiResponse<T>`와 Swagger `@ApiResponse` 이름 충돌을 주의한다.

---

### [실무]

Controller 문서화 예시:

```java
@Operation(
        summary = "축제 상세 조회",
        description = "festivalId로 축제 상세 정보를 조회한다."
)
@io.swagger.v3.oas.annotations.responses.ApiResponse(
        responseCode = "200",
        description = "축제 상세 조회 성공"
)
@io.swagger.v3.oas.annotations.responses.ApiResponse(
        responseCode = "404",
        description = "축제를 찾을 수 없음"
)
@GetMapping("/festivals/{festivalId}")
public ApiResponse<FestivalDetailResponse> getFestival(
        @Parameter(description = "축제 ID", example = "1")
        @PathVariable Long festivalId
) {
    return ApiResponse.success(festivalService.getFestival(festivalId));
}
```

DTO 문서화 예시:

```java
public record FestivalDetailResponse(
        @Schema(description = "축제 ID", example = "1")
        Long festivalId,

        @Schema(description = "축제명", example = "Seoul Music Festival")
        String title,

        @Schema(description = "축제 시작일", example = "2026-07-01")
        LocalDate eventStartDate
) {
}
```

---

### [주의]

- Annotation 설명과 실제 코드 동작이 다르면 안 된다.
- `200 OK`만 작성하고 Error Response를 누락하지 않는다.
- 인증 필요 API에 Security Requirement를 누락하지 않는다.
- DTO Field Example을 오래된 값으로 방치하지 않는다.
- Controller Method 이름보다 API Contract 설명을 우선한다.
- `io.swagger.v3.oas.annotations.responses.ApiResponse`와 프로젝트 공통 `ApiResponse<T>` 이름 충돌을 주의한다.

---

### [FAQ]

Q. `@Operation`은 무엇인가?

A. API의 Summary와 Description을 문서화하는 Annotation이다.

Q. `@Schema`는 무엇인가?

A. DTO Field의 설명, 타입, Example 등을 문서화하는 Annotation이다.

Q. OpenAPI Annotation을 사용하는 이유는 무엇인가?

A. 코드와 API 문서의 간격을 줄이고 Swagger UI 문서 품질을 높이기 위해서이다.

---

# 5. Swagger ApiResponse Name Conflict

## 5.1 ApiResponse Import Conflict

### [개념]

Spring Boot 프로젝트에서 공통 응답 Wrapper 이름을 `ApiResponse<T>`로 사용하는 경우 Swagger Annotation의 `@ApiResponse`와 이름이 충돌할 수 있다.

Java는 import alias를 지원하지 않기 때문에 같은 Java 파일에서 두 타입 이름이 충돌하면 코드 생성 또는 컴파일 단계에서 문제가 발생할 수 있다.

---

### [핵심]

- 프로젝트 공통 응답 Wrapper: `ApiResponse<T>`
- Swagger Annotation: `io.swagger.v3.oas.annotations.responses.ApiResponse`
- 두 이름이 같으면 import 충돌 가능성이 있다.
- Controller 코드 생성 시 Agent가 잘못된 import를 선택할 수 있다.
- OpenAPI Annotation 사용 시 Fully Qualified Name 또는 Annotation Import 관리가 필요하다.
- 공통 응답 Wrapper 이름 변경은 기존 Controller 전체에 영향을 줄 수 있다.

---

### [실무]

문제 예시:

```java
import com.example.global.response.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
```

위 코드는 이름 충돌이 발생한다.

해결 방법 1: Swagger Annotation을 Fully Qualified Name으로 사용한다.

```java
@io.swagger.v3.oas.annotations.responses.ApiResponse(
        responseCode = "200",
        description = "조회 성공"
)
@GetMapping("/festivals/{festivalId}")
public ApiResponse<FestivalDetailResponse> getFestival(
        @PathVariable Long festivalId
) {
    return ApiResponse.success(festivalService.getFestival(festivalId));
}
```

해결 방법 2: 프로젝트 공통 응답 Wrapper 이름을 더 구체적으로 변경한다.

```text
ApiResult<T>
CommonResponse<T>
BaseResponse<T>
```

단, 이미 프로젝트에서 `ApiResponse<T>`를 사용 중이면 이름 변경은 Breaking Change가 될 수 있다.

---

### [Best Practice]

- Controller에서 공통 응답 Wrapper `ApiResponse<T>`를 유지한다면 Swagger Annotation은 Fully Qualified Name 사용을 고려한다.
- OpenAPI Annotation이 많은 프로젝트는 공통 응답 Wrapper 이름을 `ApiResult<T>`로 정할 수 있다.
- Agent 코드 생성 시 Swagger `@ApiResponse` import와 프로젝트 `ApiResponse<T>` import를 동시에 넣지 않도록 검수한다.
- 기존 코드가 많은 프로젝트에서는 Wrapper 이름 변경보다 Annotation Fully Qualified Name 사용이 안전하다.

---

### [FAQ]

Q. Swagger `@ApiResponse`와 프로젝트 `ApiResponse<T>`는 충돌할 수 있는가?

A. 그렇다. 이름이 같기 때문에 같은 Java 파일에서 import 충돌이 발생할 수 있다.

Q. 가장 안전한 해결 방법은 무엇인가?

A. Swagger Annotation을 Fully Qualified Name으로 사용하거나 공통 응답 Wrapper 이름을 변경하는 것이다.

Q. 이미 `ApiResponse<T>`를 많이 사용 중이면 이름을 바꾸는 것이 좋은가?

A. 반드시 그렇지는 않다. 기존 코드가 많다면 Swagger Annotation 쪽을 Fully Qualified Name으로 쓰는 것이 더 안전할 수 있다.

---

# 6. Authentication Documentation

## 6.1 Bearer Token Documentation

### [개념]

Authentication Documentation은 API 인증 방식, Token 전달 방법, 인증 실패 응답을 OpenAPI 문서에 명확히 표시하는 것이다.

JWT 기반 API는 Bearer Authentication Scheme을 문서화해야 한다.

```http
Authorization: Bearer access-token
```

---

### [핵심]

- 인증 필요 API를 문서에 표시한다.
- JWT Bearer Token 전달 방식을 명시한다.
- 인증 실패 401 응답을 명시한다.
- 권한 실패 403 응답을 명시한다.
- Rate Limit 초과 429 응답을 명시한다.
- Swagger UI Authorize 기능을 사용할 수 있게 설정한다.
- Public API와 Protected API를 구분한다.

---

### [실무]

OpenAPI Security Scheme 예시:

```text
Security Scheme:
type: http
scheme: bearer
bearerFormat: JWT
```

인증 필요 API 문서화 예시:

```java
@SecurityRequirement(name = "bearerAuth")
@Operation(summary = "내 정보 조회")
@GetMapping("/users/me")
public ApiResponse<UserMeResponse> getMe() {
    return ApiResponse.success(userService.getMe());
}
```

Security Contract 예시:

| API                                 | Access Level | Auth Header  | Error         |
| ----------------------------------- | ------------ | ------------ | ------------- |
| GET /api/v1/festivals               | Public       | None         | None          |
| GET /api/v1/users/me                | Protected    | Bearer Token | 401           |
| POST /api/v1/reviews                | Protected    | Bearer Token | 401, 403      |
| POST /api/v1/auth/login             | Public       | None         | 400, 401, 429 |
| DELETE /api/v1/admin/users/{userId} | Admin        | Bearer Token | 401, 403      |

---

### [FAQ]

Q. JWT 인증 API는 OpenAPI에 어떻게 표시하는가?

A. Bearer Authentication Scheme과 API별 Security Requirement를 설정한다.

Q. 인증 실패와 권한 실패는 각각 어떤 Status Code인가?

A. 인증 실패는 401 Unauthorized, 권한 실패는 403 Forbidden이다.

Q. Swagger UI에서 JWT 테스트를 하려면 무엇이 필요한가?

A. Bearer Token Security Scheme과 Authorize 설정이 필요하다.

---

# 7. API Example

## 7.1 Request Response Example

### [개념]

API Example은 Request와 Response의 실제 예시를 문서에 포함하여 Client가 Contract를 쉽게 이해하게 만드는 문서 요소이다.

Example은 API 연동 오류를 줄이고 Frontend 개발 속도를 높인다.

---

### [핵심]

- Request Example은 Client 입력 구조를 보여준다.
- Response Example은 성공 응답 구조를 보여준다.
- Error Example은 실패 응답 구조를 보여준다.
- Validation Error Example은 Form Error 처리에 도움을 준다.
- Rate Limit Error Example은 Retry UI 처리에 도움을 준다.
- Example은 실제 DTO Field와 일치해야 한다.
- Example은 오래되면 Contract Mismatch 원인이 된다.

---

### [실무]

API 문서에는 성공 / 실패 Example을 함께 작성한다.

Request Example:

```json
{
  "rating": 5,
  "content": "Great festival"
}
```

Success Response Example:

```json
{
  "success": true,
  "data": {
    "reviewId": 10,
    "rating": 5,
    "content": "Great festival"
  },
  "message": null
}
```

Error Response Example:

```json
{
  "code": "FESTIVAL_NOT_FOUND",
  "message": "Festival not found"
}
```

Validation Error Example:

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

Rate Limit Error Example:

```json
{
  "code": "RATE_LIMIT_EXCEEDED",
  "message": "Too many requests"
}
```

---

### [Best Practice]

- Example은 실제 API 응답과 같은 Field를 사용한다.
- Success Example과 Error Example을 모두 작성한다.
- 인증 필요 API는 Header Example을 포함한다.
- Pagination API는 Page Response Example을 포함한다.
- 날짜 Field Example은 프로젝트 Date Time Contract와 일치시킨다.
- Deprecated Field는 Example에서 제거하거나 명확히 표시한다.
- 429 Response는 `Retry-After` Header Example과 함께 작성한다.

---

### [FAQ]

Q. API Example은 왜 필요한가?

A. Client가 Request / Response 구조를 빠르게 이해하고 연동 오류를 줄일 수 있기 때문이다.

Q. Error Example도 작성해야 하는가?

A. 작성해야 한다. Frontend Error Handling 구현에 필요하다.

Q. Example이 실제 응답과 다르면 어떤 문제가 생기는가?

A. Contract Mismatch가 발생해 Frontend 연동 오류와 테스트 실패가 생긴다.

---

# 8. Contract Review

## 8.1 API Contract Review

### [개념]

API Contract Review는 API 문서, Controller 구현, DTO, Error Response, Security Config가 서로 일치하는지 검수하는 과정이다.

API Contract Review는 PM Agent, Backend Agent, Review Agent가 함께 사용하는 핵심 검수 단계이다.

```text
OpenAPI Document
→ Controller
→ DTO
→ ErrorResponse
→ Security Config
→ Frontend Contract
→ Review Result
```

---

### [핵심]

- API 문서와 구현이 일치해야 한다.
- URI와 Controller Mapping이 일치해야 한다.
- Request DTO와 OpenAPI Schema가 일치해야 한다.
- Response DTO와 OpenAPI Schema가 일치해야 한다.
- Status Code와 Error Code가 일치해야 한다.
- Security Contract와 Security Config가 일치해야 한다.
- Pagination / Filtering / Sorting Contract가 문서화되어야 한다.
- Rate Limiting 대상 API는 429 Error Contract가 문서화되어야 한다.

---

### [실무]

API Contract Review Checklist:

- URI Naming이 Resource 중심인가?
- HTTP Method가 역할에 맞는가?
- Path Variable 이름이 일치하는가?
- Query Parameter 이름이 일치하는가?
- Request Body Schema가 DTO와 일치하는가?
- Response Body Schema가 DTO와 일치하는가?
- Success Status Code가 적절한가?
- Error Status Code가 적절한가?
- Error Code가 문서화되어 있는가?
- Validation Rule이 문서화되어 있는가?
- Authentication 필요 여부가 명확한가?
- Authorization 조건이 명확한가?
- Rate Limiting 대상 API에 429가 문서화되어 있는가?
- Swagger UI에서 테스트 가능한가?
- Swagger `@ApiResponse`와 프로젝트 `ApiResponse<T>` import 충돌이 없는가?

---

### [FAQ]

Q. API Contract Review란 무엇인가?

A. API 문서, 구현, DTO, Error Response, Security Config가 서로 일치하는지 검수하는 과정이다.

Q. Contract Review에서 가장 중요한 것은 무엇인가?

A. URI, Method, Request, Response, Status Code, Error Response, Security Contract 일치 여부이다.

Q. Contract Review는 누가 사용하는가?

A. PM Agent, Backend Agent, Review Agent가 API 설계와 검수에 사용한다.

---

# 9. Contract Mismatch

## 9.1 Contract Mismatch

### [개념]

Contract Mismatch는 API 문서, Backend 구현, Frontend 기대 구조가 서로 다른 상태이다.

Contract Mismatch는 API 연동 오류, 테스트 실패, 배포 장애의 주요 원인이다.

```text
Swagger Response Field: title
Backend Response Field: festivalTitle
Frontend Expected Field: name

→ Contract Mismatch
```

---

### [핵심]

- 문서와 실제 응답이 다르면 Contract Mismatch이다.
- DTO Field와 Frontend Type이 다르면 Contract Mismatch이다.
- Status Code와 Error Response 의미가 다르면 Contract Mismatch이다.
- Security Config와 OpenAPI Security Requirement가 다르면 Contract Mismatch이다.
- Pagination Response 구조가 문서와 다르면 Contract Mismatch이다.
- Rate Limit Error가 실제로는 발생하지만 문서에 없으면 Contract Mismatch이다.
- Contract Mismatch는 API Review에서 우선 탐지해야 한다.

---

### [실무]

Contract Mismatch 탐지 대상:

| 영역       | 확인 항목                             |
| ---------- | ------------------------------------- |
| URI        | Swagger Path와 Controller Mapping     |
| Method     | GET / POST / PUT / PATCH / DELETE     |
| Request    | DTO Field, Required, Validation       |
| Response   | DTO Field, Type, Nullable             |
| Error      | Status Code, Error Code, Message      |
| Security   | Public / Protected / Admin            |
| Rate Limit | 429, Retry-After, RATE_LIMIT_EXCEEDED |
| Pagination | page, size, totalElements, hasNext    |
| Date       | yyyy-MM-dd, ISO-8601                  |

Contract Mismatch 해결 흐름:

```text
Mismatch Found
→ Source of Truth 확인
→ OpenAPI / DTO / Frontend Type 비교
→ Contract 결정
→ Code 수정
→ Swagger UI Test
→ Frontend Integration Test
```

---

### [FAQ]

Q. Contract Mismatch란 무엇인가?

A. API 문서, Backend 구현, Frontend 기대 구조가 서로 다른 상태이다.

Q. Contract Mismatch는 왜 위험한가?

A. Frontend 연동 오류, 테스트 실패, 배포 장애를 만들기 때문이다.

Q. Contract Mismatch를 줄이는 방법은 무엇인가?

A. OpenAPI 문서화, DTO 분리, Swagger 테스트, Frontend / Backend Contract 합의가 필요하다.

---

# 10. API Troubleshooting

## 10.1 Troubleshooting Process

### [개념]

API Troubleshooting은 API 요청 실패, 응답 오류, Contract 불일치, 인증 실패, 성능 문제의 원인을 찾고 해결하는 과정이다.

Troubleshooting은 문제, 원인, 해결 형식으로 문서화하면 Agent 검색 품질이 높아진다.

```text
Problem
→ Cause
→ Check
→ Fix
→ Retest
```

---

### [핵심]

- API 문제는 Request, Response, Server Log, DB, Security Config를 함께 확인한다.
- 문제를 Status Code 기준으로 분류한다.
- 400은 Request / Validation 문제를 의심한다.
- 401은 Authentication 문제를 의심한다.
- 403은 Authorization 또는 CSRF 문제를 의심한다.
- 404는 URI, Resource, Routing 문제를 의심한다.
- 409는 중복, 상태 충돌, Business Rule 문제를 의심한다.
- 429는 Rate Limit 초과를 의심한다.
- 500은 Server Exception, DB Error, NullPointerException 등을 의심한다.
- 502 / 503 / 504는 External API, Gateway, Provider, Timeout 문제를 의심한다.

---

### [실무]

Troubleshooting 기본 순서:

```text
1. Browser Network Tab 확인
2. Request URL / Method 확인
3. Request Header 확인
4. Request Body 확인
5. Status Code 확인
6. Response Body 확인
7. Server Log 확인
8. Controller Mapping 확인
9. Security Config 확인
10. Service / Repository / DB 확인
11. External API Provider Log 확인
12. Swagger UI 또는 Postman 재현
```

---

### [FAQ]

Q. API Troubleshooting은 무엇인가?

A. API 요청 실패, 응답 오류, Contract 불일치, 인증 실패, 성능 문제의 원인을 찾고 해결하는 과정이다.

Q. API 문제는 어디서부터 확인하는가?

A. Request URL, Method, Header, Body, Status Code, Response Body부터 확인한다.

Q. API 오류는 어떻게 분류하는가?

A. Status Code 기준으로 400, 401, 403, 404, 409, 429, 500, 502, 503, 504 등으로 분류한다.

---

# 11. Invalid Request Troubleshooting

## 11.1 400 Bad Request

### [개념]

400 Bad Request는 Client Request 형식이 잘못되었거나 Validation에 실패했을 때 발생하는 오류이다.

Request Body, Query Parameter, Path Variable, Content-Type, JSON 형식을 우선 확인한다.

---

### [핵심]

- 400은 Request 문제이다.
- JSON Body 형식 오류가 원인일 수 있다.
- Required Field 누락이 원인일 수 있다.
- Validation 실패가 원인일 수 있다.
- Type Mismatch가 원인일 수 있다.
- Content-Type 누락이 원인일 수 있다.

---

### [Troubleshooting]

문제: 400 Bad Request가 발생한다.

원인: Request Body JSON 형식이 잘못되었거나 Required Field가 누락되었다.

해결: Swagger UI의 Request Schema와 실제 Request Body를 비교한다.

---

문제: `HttpMessageNotReadableException`이 발생한다.

원인: JSON 문법 오류, 타입 불일치, 날짜 형식 오류가 발생했다.

해결: JSON 문법, Field Type, LocalDate / LocalDateTime Format을 확인한다.

---

문제: `MethodArgumentNotValidException`이 발생한다.

원인: Request DTO Bean Validation에 실패했다.

해결: Validation Error Response의 Field Error를 확인하고 입력값을 수정한다.

---

문제: Query Parameter가 바인딩되지 않는다.

원인: Parameter 이름이 Controller와 Frontend에서 다르다.

해결: OpenAPI 문서, Controller `@RequestParam`, Frontend Axios params 이름을 일치시킨다.

---

### [FAQ]

Q. 400 Bad Request는 언제 발생하는가?

A. Request 형식 오류, Validation 실패, Type Mismatch, JSON 파싱 오류가 있을 때 발생한다.

Q. 400 오류에서 가장 먼저 확인할 것은 무엇인가?

A. Request Body, Query Parameter, Content-Type, Validation Error Response이다.

Q. 날짜 Field 때문에 400이 발생하면 무엇을 확인하는가?

A. `yyyy-MM-dd`, ISO-8601 등 API Date Time Contract와 실제 입력 형식을 확인한다.

---

# 12. Authentication Troubleshooting

## 12.1 401 Unauthorized

### [개념]

401 Unauthorized는 인증 정보가 없거나 유효하지 않을 때 발생하는 오류이다.

JWT 기반 API에서는 Authorization Header와 Token 유효성을 우선 확인한다.

---

### [핵심]

- 401은 Authentication 실패이다.
- Authorization Header 누락이 원인일 수 있다.
- Bearer Prefix 누락이 원인일 수 있다.
- Access Token 만료가 원인일 수 있다.
- Token Signature 오류가 원인일 수 있다.
- Token 형식 오류가 원인일 수 있다.
- Swagger UI Authorize 설정 누락이 원인일 수 있다.

---

### [Troubleshooting]

문제: 인증 API에서 401 Unauthorized가 발생한다.

원인: Authorization Header가 없거나 Token이 유효하지 않다.

해결: `Authorization: Bearer access-token` 형식으로 Header를 전달한다.

---

문제: Swagger UI에서는 401이 발생한다.

원인: Swagger UI Authorize에 Token을 입력하지 않았거나 Bearer 설정이 잘못되었다.

해결: OpenAPI Security Scheme과 Swagger UI Authorize 설정을 확인한다.

---

문제: Frontend에서는 로그인 후에도 401이 발생한다.

원인: Axios Interceptor가 Access Token을 Header에 붙이지 못했다.

해결: Browser Network Tab에서 Authorization Header 존재 여부를 확인한다.

---

문제: Token 만료 후 계속 401이 발생한다.

원인: Refresh Token 재발급 Flow가 동작하지 않는다.

해결: 401 발생 시 Refresh API 호출, Token 재저장, 원 요청 재시도 Flow를 확인한다.

---

### [FAQ]

Q. 401 Unauthorized는 무엇인가?

A. 인증 정보가 없거나 유효하지 않을 때 발생하는 Authentication 실패 응답이다.

Q. JWT API에서 401이 발생하면 무엇을 확인하는가?

A. Authorization Header, Bearer Prefix, Token 만료, Token Signature, Swagger Authorize 설정을 확인한다.

Q. 401과 403의 차이는 무엇인가?

A. 401은 인증 실패이고 403은 인증은 되었지만 권한이 없는 상태이다.

---

# 13. Authorization Troubleshooting

## 13.1 403 Forbidden

### [개념]

403 Forbidden은 인증은 되었지만 해당 Resource 또는 Action에 접근할 권한이 없을 때 발생하는 오류이다.

Authorization 문제는 Role, Permission, Ownership, Security Config를 확인해야 한다.

Spring Security 환경에서는 CSRF 설정 때문에 POST / PUT / PATCH / DELETE 요청이 403을 반환할 수도 있으므로 권한 실패와 CSRF 실패를 구분해야 한다.

---

### [핵심]

- 403은 Authorization 실패이다.
- Role이 부족할 수 있다.
- Permission이 부족할 수 있다.
- Resource Ownership 검증에 실패할 수 있다.
- Security Config Rule이 잘못되었을 수 있다.
- Method Security Annotation이 잘못되었을 수 있다.
- CSRF 설정이 API 구조와 맞지 않을 수 있다.
- Stateless JWT API에서는 CSRF Disable 정책을 사용하는 경우가 많다.

---

### [Troubleshooting]

문제: 관리자 API에서 403 Forbidden이 발생한다.

원인: 현재 사용자가 ROLE_ADMIN 권한을 가지고 있지 않다.

해결: Token Claims, SecurityContext, `hasRole('ADMIN')` 설정을 확인한다.

---

문제: 본인이 작성한 리뷰 수정에서 403이 발생한다.

원인: Ownership 검증 로직이 현재 사용자 ID와 작성자 ID를 다르게 판단했다.

해결: SecurityContext의 userId와 Resource Owner ID를 비교한다.

---

문제: 모든 POST / PATCH / DELETE 요청에서 403이 발생한다.

원인: CSRF 설정이 Stateless JWT API와 맞지 않을 수 있다.

해결: Stateless REST API에서는 CSRF 정책과 Security Config를 검토한다.

---

문제: 인증은 성공했는데 권한이 반영되지 않는다.

원인: JWT Claims에서 Role을 읽어 Authority로 변환하지 않았다.

해결: JWT Filter에서 Role / Authority Mapping을 확인한다.

---

### [FAQ]

Q. 403 Forbidden은 무엇인가?

A. 인증은 되었지만 Resource 또는 Action에 접근할 권한이 없을 때 발생하는 Authorization 실패 응답이다.

Q. 403 오류에서 무엇을 확인하는가?

A. Role, Permission, Ownership, Security Config, Method Security, Token Claims, CSRF 설정을 확인한다.

Q. Ownership 검증은 어디에서 처리하는가?

A. 주로 Service Layer에서 현재 사용자 ID와 Resource Owner ID를 비교한다.

---

# 14. Not Found Troubleshooting

## 14.1 404 Not Found

### [개념]

404 Not Found는 요청한 URI 또는 Resource가 존재하지 않을 때 발생하는 오류이다.

404는 Routing 문제와 Resource 조회 실패를 구분해야 한다.

---

### [핵심]

- 404는 URI가 없을 때 발생할 수 있다.
- 404는 Resource가 없을 때 발생할 수 있다.
- Frontend 요청 경로와 Backend Mapping이 다를 수 있다.
- API Prefix가 누락되었을 수 있다.
- Path Variable 값에 해당하는 데이터가 없을 수 있다.
- SPA Routing 문제와 API 404를 구분해야 한다.

---

### [Troubleshooting]

문제: API 요청이 404 Not Found를 반환한다.

원인: Frontend Axios URL과 Backend Controller Mapping이 다르다.

해결: Browser Network Tab의 Request URL과 Controller `@RequestMapping`, `@GetMapping`을 비교한다.

---

문제: Swagger UI에는 API가 보이는데 Frontend에서 404가 발생한다.

원인: Frontend Base URL, Prefix, Proxy, Build 환경 설정이 다를 수 있다.

해결: Axios Base URL, Proxy, 배포 경로, `/api/v1` Prefix를 확인한다.

---

문제: 특정 ID 조회에서 404가 발생한다.

원인: URI는 맞지만 해당 Resource 데이터가 존재하지 않는다.

해결: DB에서 Resource 존재 여부를 확인하고 `*_NOT_FOUND` Error Code를 반환한다.

---

문제: React 새로고침 시 404가 발생한다.

원인: SPA Routing 요청을 Backend가 API로 처리하거나 index.html Forward 설정이 없다.

해결: API Path와 SPA Forward Path를 분리하고 Static Resource Routing을 설정한다.

---

### [FAQ]

Q. 404 Not Found는 언제 발생하는가?

A. 요청한 URI가 없거나 Resource가 존재하지 않을 때 발생한다.

Q. API 404와 Resource 404는 어떻게 구분하는가?

A. Controller Mapping이 없으면 API 404이고, Mapping은 있지만 데이터가 없으면 Resource 404이다.

Q. Frontend에서만 404가 발생하면 무엇을 확인하는가?

A. Axios Base URL, API Prefix, Proxy, 배포 경로, Controller Mapping을 확인한다.

---

# 15. Conflict Troubleshooting

## 15.1 409 Conflict

### [개념]

409 Conflict는 요청이 현재 Resource 상태 또는 Business Rule과 충돌할 때 발생하는 오류이다.

중복 데이터, 중복 요청, 상태 전이 오류, Idempotency Key 충돌은 409 대상이다.

---

### [핵심]

- 409는 Business Conflict이다.
- 중복 이메일은 409로 처리할 수 있다.
- 중복 좋아요는 409로 처리할 수 있다.
- 이미 처리된 결제 요청은 409 또는 Idempotent Response로 처리할 수 있다.
- 같은 Idempotency Key로 다른 Body가 오면 409로 처리할 수 있다.
- 상태 전이 불가능한 요청은 409로 처리할 수 있다.
- 409는 429 Rate Limit 초과와 구분해야 한다.

---

### [Troubleshooting]

문제: 회원가입에서 409 Conflict가 발생한다.

원인: 이미 사용 중인 Email 또는 Nickname이다.

해결: `DUPLICATE_EMAIL`, `DUPLICATE_NICKNAME` Error Code를 확인하고 사용자에게 안내한다.

---

문제: 좋아요 등록에서 409 Conflict가 발생한다.

원인: 이미 좋아요가 등록되어 있다.

해결: 중복 등록을 막고 현재 좋아요 상태를 기준으로 UI를 동기화한다.

---

문제: 결제 승인에서 409 Conflict가 발생한다.

원인: 이미 승인된 결제이거나 같은 Idempotency Key에 다른 Request Body가 전달되었다.

해결: Payment Status와 Idempotency Key 저장값을 확인한다.

---

문제: 상태 변경 API에서 409 Conflict가 발생한다.

원인: 현재 상태에서 요청한 상태로 전이할 수 없다.

해결: 상태 전이 규칙을 확인하고 Business Error Code를 명확히 반환한다.

---

### [FAQ]

Q. 409 Conflict는 언제 사용하는가?

A. 중복 데이터, 중복 요청, 상태 충돌, Business Rule 충돌이 발생했을 때 사용한다.

Q. 중복 이메일은 어떤 Status Code를 사용하는가?

A. 보통 409 Conflict를 사용한다.

Q. 같은 Idempotency Key로 다른 Body가 오면 어떻게 처리하는가?

A. 보통 409 Conflict로 처리한다.

---

# 16. Rate Limit Troubleshooting

## 16.1 429 Too Many Requests

### [개념]

429 Too Many Requests는 Client가 일정 시간 동안 허용된 요청 수를 초과했을 때 발생하는 오류이다.

429는 Authentication, Authorization, Conflict와 다른 Rate Limiting 전용 응답이다.

```text
Too Many Requests
→ Rate Limit Exceeded
→ 429
→ Retry Later
```

---

### [핵심]

- 429는 Rate Limit 초과 응답이다.
- Login API에서 Brute Force 방어에 사용한다.
- Search API에서 과도한 검색 요청 제한에 사용한다.
- AI API와 External API Proxy에서 비용 보호에 사용한다.
- Response Header에 `Retry-After`가 포함될 수 있다.
- Error Code는 `RATE_LIMIT_EXCEEDED`를 사용할 수 있다.
- Client는 즉시 자동 재시도를 반복하면 안 된다.

---

### [Troubleshooting]

문제: 로그인 API에서 429 Too Many Requests가 발생한다.

원인: 같은 IP 또는 사용자 기준으로 로그인 실패 또는 요청 횟수가 제한을 초과했다.

해결: Rate Limit 정책, Retry-After, 로그인 실패 카운트, IP 기준 제한을 확인한다.

---

문제: 검색 API에서 429가 발생한다.

원인: 짧은 시간에 너무 많은 검색 요청을 보냈다.

해결: Frontend Debounce, Cache, Rate Limit 정책을 조정한다.

---

문제: AI 추천 API에서 429가 발생한다.

원인: User 기준 또는 Token 기준 요청 한도를 초과했다.

해결: 사용자별 Quota, Daily Limit, Retry 안내 UI를 확인한다.

---

문제: Client가 429 후 계속 재시도한다.

원인: Frontend Retry Logic이 `Retry-After` Header를 고려하지 않는다.

해결: `Retry-After` 기반 지연 재시도 또는 재시도 차단 UI를 구현한다.

---

### [FAQ]

Q. 429 Too Many Requests는 언제 발생하는가?

A. Client가 정해진 요청 한도를 초과했을 때 발생한다.

Q. 429와 403의 차이는 무엇인가?

A. 429는 요청량 초과이고 403은 권한 부족이다.

Q. 429와 409의 차이는 무엇인가?

A. 429는 Rate Limit 초과이고 409는 Resource 상태 또는 Business Rule 충돌이다.

---

# 17. Server Error Troubleshooting

## 17.1 500 Internal Server Error

### [개념]

500 Internal Server Error는 Server 내부에서 예상하지 못한 오류가 발생했을 때 반환하는 응답이다.

500은 NullPointerException, DB 오류, RuntimeException, 설정 오류 등에서 발생할 수 있다.

---

### [핵심]

- 500은 Server Error이다.
- Business Error를 500으로 처리하지 않는다.
- Stack Trace를 Client에 노출하지 않는다.
- Server Log에서 실제 예외를 확인한다.
- GlobalExceptionHandler에서 예상 가능한 예외를 분리한다.
- Monitoring과 Alert 대상이다.
- External API 오류와 내부 RuntimeException을 구분하면 운영성이 좋아진다.

---

### [Troubleshooting]

문제: 500 Internal Server Error가 발생한다.

원인: Server 내부 RuntimeException 또는 처리되지 않은 예외가 발생했다.

해결: Server Log의 Stack Trace를 확인하고 예외 발생 지점을 수정한다.

---

문제: Resource가 없는데 500이 발생한다.

원인: `Optional.get()` 사용 또는 NullPointerException이 발생했다.

해결: `orElseThrow()`로 BusinessException을 발생시키고 404로 Mapping한다.

---

문제: DB 저장 중 500이 발생한다.

원인: Not Null Constraint, Unique Constraint, Foreign Key Constraint 위반일 수 있다.

해결: DB Constraint와 Request Validation, Business Validation을 일치시킨다.

---

문제: 외부 API 호출 중 500이 발생한다.

원인: Timeout, 인증 실패, Provider Error, Response Parsing 오류가 내부 예외로 처리되었다.

해결: 외부 API Error Mapping을 분리하고 502 / 503 / 504 사용 여부를 검토한다.

---

### [FAQ]

Q. 500 Internal Server Error는 언제 사용하는가?

A. Server 내부에서 예상하지 못한 오류가 발생했을 때 사용한다.

Q. Business Exception을 500으로 처리해도 되는가?

A. 권장하지 않는다. Resource 없음, 중복, 권한 오류는 적절한 4xx로 처리해야 한다.

Q. 500 오류에서 가장 먼저 확인할 것은 무엇인가?

A. Server Log의 Stack Trace와 예외 발생 위치이다.

---

# 18. External API Error Troubleshooting

## 18.1 502 503 504 External Error

### [개념]

External API Error는 Backend가 외부 API Provider와 통신하는 과정에서 발생하는 오류이다.

결제 Provider, 지도 API, Tour API, AI API, Email API 같은 외부 시스템 오류는 내부 서버 오류와 구분해 처리할 수 있다.

```text
Backend API
→ External Provider
→ Timeout / Failure / Bad Response
→ 502 / 503 / 504 or 500
```

---

### [핵심]

- 외부 API 오류를 무조건 500으로 처리하지 않는다.
- Provider 응답 형식 오류는 502 Bad Gateway로 처리할 수 있다.
- Provider 장애는 503 Service Unavailable로 처리할 수 있다.
- Provider Timeout은 504 Gateway Timeout으로 처리할 수 있다.
- 간단한 팀 프로젝트에서는 500으로 단순화할 수 있지만 정책 문서화가 필요하다.
- Provider 내부 메시지를 Client에 그대로 노출하지 않는다.
- 결제 API는 Provider Error와 결제 상태 충돌을 분리해야 한다.

---

### [실무]

External API Error Mapping 예시:

| 상황                    |               Status Code | Error Code                   |
| ----------------------- | ------------------------: | ---------------------------- |
| Provider 응답 형식 오류 |           502 Bad Gateway | EXTERNAL_BAD_RESPONSE        |
| Provider 서버 장애      |   503 Service Unavailable | EXTERNAL_SERVICE_UNAVAILABLE |
| Provider Timeout        |       504 Gateway Timeout | EXTERNAL_TIMEOUT             |
| 내부 처리 중 예외       | 500 Internal Server Error | INTERNAL_SERVER_ERROR        |
| Provider 인증 실패      |  502 또는 내부 정책 Error | EXTERNAL_AUTH_FAILED         |
| 결제 승인 상태 충돌     |              409 Conflict | PAYMENT_STATUS_CONFLICT      |

간단한 팀 프로젝트 단순화 정책:

```text
External API Failure → 500 INTERNAL_SERVER_ERROR
External API Timeout → 500 EXTERNAL_API_TIMEOUT
```

운영 환경 권장 정책:

```text
Bad provider response → 502
Provider unavailable → 503
Provider timeout → 504
```

---

### [Troubleshooting]

문제: 외부 API 호출 후 502 Bad Gateway가 발생한다.

원인: Provider 응답 형식이 예상 Schema와 다르거나 Gateway 응답이 비정상이다.

해결: Provider Response Body, Status Code, Parsing Logic을 확인한다.

---

문제: 외부 API 호출 후 503 Service Unavailable이 발생한다.

원인: Provider 서버가 장애 상태이거나 일시적으로 사용할 수 없다.

해결: Provider Status, Retry Policy, Fallback, Circuit Breaker를 확인한다.

---

문제: 외부 API 호출 후 504 Gateway Timeout이 발생한다.

원인: Provider 응답 시간이 Timeout 기준을 초과했다.

해결: Timeout 설정, Retry 횟수, 비동기 처리, 사용자 안내 메시지를 확인한다.

---

문제: 결제 Provider 오류 메시지가 Client에 그대로 노출된다.

원인: Provider Error Response를 서비스 Error Response로 변환하지 않았다.

해결: 내부 Error Code로 Mapping하고 민감 정보는 제거한다.

---

### [FAQ]

Q. 외부 API 오류는 항상 500으로 처리하는가?

A. 아니다. 운영 환경에서는 502, 503, 504로 구분할 수 있다.

Q. External API Timeout은 어떤 Status Code를 사용할 수 있는가?

A. 504 Gateway Timeout을 사용할 수 있다.

Q. Provider 서버 장애는 어떤 Status Code를 사용할 수 있는가?

A. 503 Service Unavailable을 사용할 수 있다.

Q. Provider 응답 오류는 어떤 Status Code를 사용할 수 있는가?

A. 502 Bad Gateway를 사용할 수 있다.

---

# 19. Pagination Troubleshooting

## 19.1 Pagination Issue

### [개념]

Pagination Issue는 목록 조회 API에서 중복, 누락, 정렬 불안정, 과도한 응답 크기, Count Query 성능 문제가 발생하는 상황이다.

Pagination 문제는 Frontend UI와 Backend Query 설계를 함께 확인해야 한다.

---

### [핵심]

- 기본 정렬이 없으면 페이지 결과가 불안정하다.
- 데이터 변경이 잦으면 Page Pagination에서 중복 또는 누락이 발생할 수 있다.
- size 제한이 없으면 서버 부하가 증가한다.
- Count Query가 느리면 Page 응답이 느려진다.
- Cursor 기준이 불안정하면 중복 또는 누락이 발생한다.
- Frontend page index와 Backend page index가 다를 수 있다.

---

### [Troubleshooting]

문제: 페이지를 넘길 때 같은 데이터가 반복된다.

원인: Sort 기준이 없거나 정렬 기준이 불안정하다.

해결: `createdAt desc`, `id desc` 같은 고정 정렬 기준을 추가한다.

---

문제: 무한 스크롤에서 데이터가 누락된다.

원인: Page 기반 Pagination 사용 중 새 데이터가 삽입되어 offset이 밀렸다.

해결: Cursor Pagination 또는 Slice 기반 Pagination을 사용한다.

---

문제: 목록 API가 느리다.

원인: Count Query 비용이 크거나 size가 너무 크다.

해결: Slice 사용, Count Query 최적화, size 최대값 제한을 적용한다.

---

문제: Frontend 첫 페이지 요청 결과가 이상하다.

원인: Frontend는 page=1 기준이고 Spring Pageable은 page=0 기준이다.

해결: page 시작 번호를 API Contract에 명확히 정의한다.

---

### [FAQ]

Q. Pagination 결과가 불안정한 이유는 무엇인가?

A. 기본 정렬 기준이 없거나 정렬 Field가 고유하지 않기 때문이다.

Q. 무한 스크롤에는 어떤 Pagination이 적합한가?

A. Cursor Pagination 또는 Slice 기반 Pagination이 적합하다.

Q. Spring Pageable의 page 시작 번호는 무엇인가?

A. 기본적으로 0부터 시작한다.

---

# 20. OpenAPI Troubleshooting

## 20.1 Swagger Documentation Issue

### [개념]

OpenAPI Troubleshooting은 Swagger UI 문서가 실제 API 구현과 다르거나 API가 문서에 표시되지 않는 문제를 해결하는 과정이다.

OpenAPI 문서 문제는 API Contract 신뢰도를 낮춘다.

---

### [핵심]

- Swagger UI에 API가 표시되지 않을 수 있다.
- Request Schema가 DTO와 다를 수 있다.
- Error Response가 문서에 누락될 수 있다.
- 인증 필요 API에 Security Requirement가 누락될 수 있다.
- Pageable Parameter가 문서에 불명확할 수 있다.
- Generic Response Wrapper가 제대로 표시되지 않을 수 있다.
- Swagger `@ApiResponse`와 프로젝트 `ApiResponse<T>` import 충돌이 발생할 수 있다.

---

### [Troubleshooting]

문제: Swagger UI에 API가 표시되지 않는다.

원인: Controller가 Component Scan 대상이 아니거나 Mapping Annotation이 누락되었다.

해결: Package 구조, `@RestController`, `@RequestMapping`, Spring Boot Scan 범위를 확인한다.

---

문제: Swagger UI에서 Request Body Schema가 이상하게 표시된다.

원인: DTO Field, Getter, Record 구조, Generic Wrapper 문서화가 불명확하다.

해결: Request DTO를 명확히 분리하고 `@Schema` 설명을 추가한다.

---

문제: 인증 API인데 Swagger UI에서 Authorize가 적용되지 않는다.

원인: Security Scheme 또는 `@SecurityRequirement` 설정이 누락되었다.

해결: Bearer Token Security Scheme과 API별 Security Requirement를 설정한다.

---

문제: 실제 Error Response와 Swagger 문서가 다르다.

원인: Error Response Schema와 GlobalExceptionHandler가 문서에 반영되지 않았다.

해결: 공통 ErrorResponse Schema를 정의하고 Status Code별 Error Response를 문서화한다.

---

문제: Controller에서 `ApiResponse` import 충돌이 발생한다.

원인: 프로젝트 공통 `ApiResponse<T>`와 Swagger `@ApiResponse` Annotation 이름이 같다.

해결: Swagger Annotation을 Fully Qualified Name으로 작성하거나 공통 Wrapper 이름을 변경한다.

---

### [FAQ]

Q. Swagger UI에 API가 안 보이면 무엇을 확인하는가?

A. Controller Package, `@RestController`, Mapping Annotation, Component Scan 범위를 확인한다.

Q. Swagger UI에서 JWT 인증 테스트가 안 되면 무엇을 확인하는가?

A. Bearer Token Security Scheme과 `@SecurityRequirement` 설정을 확인한다.

Q. Swagger 문서와 실제 응답이 다르면 무엇인가?

A. Contract Mismatch이다.

---

# 21. API Quality Checklist

## 21.1 Final API Review Checklist

### [Checklist]

API Design Checklist:

- Resource 중심 URI인가?
- URI에 불필요한 동사가 없는가?
- HTTP Method가 역할에 맞는가?
- Path Variable 이름이 명확한가?
- Query Parameter가 검색 조건으로 분리되어 있는가?
- Request DTO와 Response DTO가 분리되어 있는가?
- Entity를 직접 Request / Response로 사용하지 않는가?
- Request Validation이 적용되어 있는가?
- Business Validation이 Service Layer에 있는가?
- Status Code가 상황에 맞는가?
- Error Response Schema가 통일되어 있는가?
- Validation Error Response가 Field Error를 포함하는가?
- Pagination이 필요한 목록 API에 적용되어 있는가?
- Filtering / Sorting 조건이 문서화되어 있는가?
- Authentication 필요 여부가 명확한가?
- Authorization 조건이 명확한가?
- Public / Protected / Admin API가 구분되어 있는가?
- Rate Limiting 대상 API에 429 Error Contract가 있는가?
- Idempotency가 필요한 API에 중복 요청 처리가 있는가?
- OpenAPI 문서가 실제 구현과 일치하는가?
- Swagger UI에서 Request / Response 테스트가 가능한가?
- Swagger `@ApiResponse`와 프로젝트 `ApiResponse<T>` import 충돌이 없는가?
- Frontend Axios URL과 Backend Mapping이 일치하는가?
- Date Time Format이 통일되어 있는가?
- External API Error Mapping 정책이 정의되어 있는가?
- Breaking Change 여부를 검토했는가?

---

### [실무]

Review Agent는 API 설계를 검수할 때 다음 우선순위로 문제를 탐지한다.

1. Contract Mismatch
2. Security Misconfiguration
3. Wrong Status Code
4. Error Response Inconsistency
5. Missing Validation
6. Missing Pagination
7. Missing Rate Limit on High Risk API
8. URI Naming Issue
9. Method Misuse
10. Missing OpenAPI Documentation
11. External API Error Mapping Missing
12. Breaking Change Risk

---

### [FAQ]

Q. API 품질 검수에서 가장 중요한 것은 무엇인가?

A. API Contract 일치성, Security Contract, Status Code, Error Response, Validation, Pagination이다.

Q. Review Agent는 무엇을 우선 탐지해야 하는가?

A. Contract Mismatch, Security 문제, Status Code 오사용, Error Response 불일치, Validation 누락이다.

Q. API Checklist는 왜 필요한가?

A. API 설계와 구현을 일관되게 검수하고 품질 편차를 줄이기 위해 필요하다.

---

# 22. Common Mistakes

## 22.1 OpenAPI Swagger Troubleshooting Mistakes

### [Troubleshooting]

문제: Swagger 문서만 보고 개발했는데 Frontend 연동이 실패한다.

원인: Swagger 문서와 실제 API Response가 다르다.

해결: Swagger UI 테스트, 실제 Network Response, DTO Field를 비교한다.

---

문제: Error Response가 API마다 다르다.

원인: GlobalExceptionHandler와 공통 ErrorResponse Schema가 없다.

해결: ErrorResponse Schema를 통일하고 OpenAPI에 공통 Error Response를 문서화한다.

---

문제: Swagger UI에서 인증 API 테스트가 불가능하다.

원인: Bearer Token Security Scheme이 설정되지 않았다.

해결: OpenAPI Security Scheme과 Swagger Authorize 설정을 추가한다.

---

문제: API 문서에 200 응답만 있고 실패 응답이 없다.

원인: Error Contract 문서화가 누락되었다.

해결: 400, 401, 403, 404, 409, 429, 500 응답을 상황별로 문서화한다.

---

문제: Swagger Annotation `@ApiResponse`와 프로젝트 `ApiResponse<T>` import가 충돌한다.

원인: 같은 Java 파일에서 동일한 단순 이름을 가진 타입을 동시에 import했다.

해결: Swagger Annotation을 Fully Qualified Name으로 작성하거나 공통 응답 Wrapper 이름을 변경한다.

---

문제: Rate Limit 정책은 있는데 OpenAPI에 429 응답이 없다.

원인: Rate Limiting Error Contract 문서화가 누락되었다.

해결: 429 Too Many Requests, `RATE_LIMIT_EXCEEDED`, `Retry-After` Header를 문서화한다.

---

문제: External API 장애가 모두 500으로만 반환된다.

원인: External API Error Mapping 정책이 없다.

해결: 502, 503, 504 또는 프로젝트 단순화 정책을 명확히 정하고 문서화한다.

---

문제: Validation Rule이 문서에 없다.

원인: Request DTO Annotation만 있고 OpenAPI Schema 설명이 부족하다.

해결: Required, Size, Min, Max, Pattern, Example을 문서화한다.

---

문제: Contract Review 없이 API Field를 변경했다.

원인: Breaking Change 검토가 없다.

해결: Field 변경 전 Frontend 영향도, OpenAPI Diff, Versioning 필요 여부를 검토한다.

---

문제: 404 원인을 찾지 못한다.

원인: API Routing 404와 Resource Not Found 404를 구분하지 않았다.

해결: Controller Mapping 존재 여부와 DB Resource 존재 여부를 나누어 확인한다.

---

문제: 401과 403을 혼동한다.

원인: Authentication과 Authorization을 구분하지 않았다.

해결: 인증 실패는 401, 권한 실패는 403으로 처리한다.

---

문제: 403 원인을 권한 문제로만 판단한다.

원인: CSRF 설정에 의한 403 가능성을 확인하지 않았다.

해결: POST / PATCH / DELETE 요청에서 CSRF 설정과 Stateless API Security Config를 확인한다.

---

문제: API 성능 문제가 발생한다.

원인: Pagination 누락, size 제한 누락, Count Query 과다, Filter Index 부재가 원인일 수 있다.

해결: Pagination, Slice, Cursor, Index, Query Plan을 점검한다.

---

### [FAQ]

Q. OpenAPI 문서에서 가장 흔한 실수는 무엇인가?

A. 실제 API와 문서 불일치, Error Response 누락, 인증 정보 누락, Example 불일치이다.

Q. Swagger UI 테스트에서 가장 흔한 실수는 무엇인가?

A. JWT Authorize 누락, Request Body Schema 불일치, Query Parameter 이름 오류이다.

Q. API Troubleshooting에서 가장 흔한 실수는 무엇인가?

A. Status Code 의미를 구분하지 않고 400, 401, 403, 404, 409, 429, 500 원인을 섞어서 보는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. OpenAPI란 무엇인가?
A. REST API Contract를 표준 형식으로 정의하는 API Documentation Specification이다.

Q. OpenAPI가 중요한 이유는 무엇인가?
A. API Contract, 협업, 테스트, 검수, Client 연동의 기준이 되기 때문이다.

Q. Swagger UI란 무엇인가?
A. OpenAPI 문서를 기반으로 API를 확인하고 직접 테스트할 수 있는 Web UI이다.

Q. Swagger UI는 왜 사용하는가?
A. API Contract 확인, Request / Response 테스트, Frontend 협업을 쉽게 하기 위해 사용한다.

Q. OpenAPI Schema란 무엇인가?
A. API Request Body, Response Body, Error Response의 데이터 구조를 정의하는 규칙이다.

Q. Request Schema와 Response Schema를 분리해야 하는가?
A. 분리하는 것이 좋다. 입력과 출력은 목적과 Field 구성이 다르기 때문이다.

Q. Error Response Schema도 OpenAPI에 작성해야 하는가?
A. 작성해야 한다. Client가 실패 응답을 일관되게 처리할 수 있기 때문이다.

Q. `@Operation`은 무엇인가?
A. API의 Summary와 Description을 문서화하는 Annotation이다.

Q. `@Schema`는 무엇인가?
A. DTO Field의 설명, 타입, Example 등을 문서화하는 Annotation이다.

Q. Swagger `@ApiResponse`와 프로젝트 `ApiResponse<T>`는 충돌할 수 있는가?
A. 그렇다. 이름이 같기 때문에 같은 Java 파일에서 import 충돌이 발생할 수 있다.

Q. Swagger ApiResponse 충돌은 어떻게 해결하는가?
A. Swagger Annotation을 Fully Qualified Name으로 쓰거나 프로젝트 공통 응답 Wrapper 이름을 변경한다.

Q. JWT 인증 API는 OpenAPI에 어떻게 표시하는가?
A. Bearer Authentication Scheme과 API별 Security Requirement를 설정한다.

Q. Swagger UI에서 JWT 테스트를 하려면 무엇이 필요한가?
A. Bearer Token Security Scheme과 Authorize 설정이 필요하다.

Q. API Example은 왜 필요한가?
A. Client가 Request / Response 구조를 빠르게 이해하고 연동 오류를 줄일 수 있기 때문이다.

Q. Error Example도 작성해야 하는가?
A. 작성해야 한다. Frontend Error Handling 구현에 필요하다.

Q. API Contract Review란 무엇인가?
A. API 문서, 구현, DTO, Error Response, Security Config가 서로 일치하는지 검수하는 과정이다.

Q. Contract Mismatch란 무엇인가?
A. API 문서, Backend 구현, Frontend 기대 구조가 서로 다른 상태이다.

Q. Contract Mismatch를 줄이는 방법은 무엇인가?
A. OpenAPI 문서화, DTO 분리, Swagger 테스트, Frontend / Backend Contract 합의가 필요하다.

Q. API Troubleshooting은 무엇인가?
A. API 요청 실패, 응답 오류, Contract 불일치, 인증 실패, 성능 문제의 원인을 찾고 해결하는 과정이다.

Q. API 문제는 어디서부터 확인하는가?
A. Request URL, Method, Header, Body, Status Code, Response Body부터 확인한다.

Q. 400 Bad Request는 언제 발생하는가?
A. Request 형식 오류, Validation 실패, Type Mismatch, JSON 파싱 오류가 있을 때 발생한다.

Q. 401 Unauthorized는 무엇인가?
A. 인증 정보가 없거나 유효하지 않을 때 발생하는 Authentication 실패 응답이다.

Q. 403 Forbidden은 무엇인가?
A. 인증은 되었지만 Resource 또는 Action에 접근할 권한이 없을 때 발생하는 Authorization 실패 응답이다.

Q. 403 오류에서 CSRF도 확인해야 하는가?
A. 그렇다. Spring Security 환경에서 POST / PATCH / DELETE 요청은 CSRF 설정 때문에 403이 발생할 수 있다.

Q. 404 Not Found는 언제 발생하는가?
A. 요청한 URI가 없거나 Resource가 존재하지 않을 때 발생한다.

Q. API 404와 Resource 404는 어떻게 구분하는가?
A. Controller Mapping이 없으면 API 404이고 Mapping은 있지만 데이터가 없으면 Resource 404이다.

Q. 409 Conflict는 언제 사용하는가?
A. 중복 데이터, 중복 요청, 상태 충돌, Business Rule 충돌이 발생했을 때 사용한다.

Q. 429 Too Many Requests는 언제 발생하는가?
A. Client가 정해진 요청 한도를 초과했을 때 발생한다.

Q. 429와 403의 차이는 무엇인가?
A. 429는 요청량 초과이고 403은 권한 부족이다.

Q. 429와 409의 차이는 무엇인가?
A. 429는 Rate Limit 초과이고 409는 Resource 상태 또는 Business Rule 충돌이다.

Q. 500 Internal Server Error는 언제 사용하는가?
A. Server 내부에서 예상하지 못한 오류가 발생했을 때 사용한다.

Q. 외부 API 오류는 항상 500으로 처리하는가?
A. 아니다. 운영 환경에서는 502, 503, 504로 구분할 수 있다.

Q. External API Timeout은 어떤 Status Code를 사용할 수 있는가?
A. 504 Gateway Timeout을 사용할 수 있다.

Q. Provider 서버 장애는 어떤 Status Code를 사용할 수 있는가?
A. 503 Service Unavailable을 사용할 수 있다.

Q. Provider 응답 오류는 어떤 Status Code를 사용할 수 있는가?
A. 502 Bad Gateway를 사용할 수 있다.

Q. Pagination 결과가 불안정한 이유는 무엇인가?
A. 기본 정렬 기준이 없거나 정렬 Field가 고유하지 않기 때문이다.

Q. Swagger UI에 API가 안 보이면 무엇을 확인하는가?
A. Controller Package, `@RestController`, Mapping Annotation, Component Scan 범위를 확인한다.

Q. Swagger UI에서 JWT 인증 테스트가 안 되면 무엇을 확인하는가?
A. Bearer Token Security Scheme과 `@SecurityRequirement` 설정을 확인한다.

Q. API 품질 검수에서 가장 중요한 것은 무엇인가?
A. API Contract 일치성, Security Contract, Status Code, Error Response, Validation, Pagination이다.

Q. Review Agent는 무엇을 우선 탐지해야 하는가?
A. Contract Mismatch, Security 문제, Status Code 오사용, Error Response 불일치, Validation 누락이다.
