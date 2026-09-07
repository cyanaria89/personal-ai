# API Design Part 07 - Agent Review, Contract Checklist & Final Quality Gate

---

# 1. API Agent Review

## 1.1 Agent Review Purpose

### [개념]

API Agent Review는 PM Agent, Backend Agent, Review Agent가 API 설계와 구현 품질을 검수하기 위한 최종 점검 과정이다.

API Agent Review의 목적은 API Contract 불일치, Security 문제, Status Code 오류, Request / Response 오류, Pagination 누락, Validation 누락을 조기에 탐지하는 것이다.

```text
API Requirement
→ API Contract
→ Backend Implementation
→ OpenAPI Documentation
→ Agent Review
→ Fix
→ Stable API
```

---

### [핵심]

- API Review는 Contract 안정성을 검수한다.
- API Review는 URI, Method, Status Code를 검수한다.
- API Review는 Request / Response DTO를 검수한다.
- API Review는 Error Response 일관성을 검수한다.
- API Review는 Authentication / Authorization 조건을 검수한다.
- API Review는 Pagination / Filtering / Sorting 조건을 검수한다.
- API Review는 OpenAPI 문서와 실제 구현의 일치 여부를 검수한다.

---

### [실무]

2026 실무 기준 API Review는 코드만 보는 것이 아니라 API Contract 전체를 검수해야 한다.

Review 대상:

- Controller Mapping
- Request DTO
- Response DTO
- Validation Annotation
- Service Business Validation
- ErrorCode
- GlobalExceptionHandler
- Security Config
- OpenAPI / Swagger 문서
- Frontend Axios URL
- Frontend Type / Interface

API Review는 다음 순서로 수행한다.

```text
1. Requirement 확인
2. Resource 확인
3. URI 확인
4. Method 확인
5. Request Contract 확인
6. Response Contract 확인
7. Error Contract 확인
8. Security Contract 확인
9. Pagination / Filtering / Sorting 확인
10. OpenAPI 문서 확인
11. Frontend 연동 영향 확인
```

---

### [FAQ]

Q. API Agent Review란 무엇인가?

A. API 설계와 구현이 Contract 기준에 맞는지 Agent가 검수하는 과정이다.

Q. API Review에서 가장 중요한 것은 무엇인가?

A. API Contract 일치성, Security Contract, Status Code, Error Response, Validation, Pagination이다.

Q. API Review는 코드만 확인하면 되는가?

A. 아니다. Controller, DTO, Error Response, Security Config, OpenAPI 문서, Frontend 연동까지 함께 확인해야 한다.

---

# 2. PM Agent API Review

## 2.1 PM Agent Role

### [개념]

PM Agent는 사용자 요구사항을 API Resource, Use Case, Endpoint 후보로 변환하는 역할을 수행한다.

PM Agent는 API가 실제 기능 요구사항을 만족하는지 검수한다.

```text
User Requirement
→ Use Case
→ Resource
→ API Candidate
→ Contract Requirement
```

---

### [핵심]

- PM Agent는 기능 요구사항을 API 요구사항으로 변환한다.
- PM Agent는 Resource 단위를 식별한다.
- PM Agent는 API가 사용자 Use Case를 만족하는지 확인한다.
- PM Agent는 Public / Protected / Admin API를 구분한다.
- PM Agent는 Frontend 화면 흐름과 API 흐름을 연결한다.
- PM Agent는 API 누락 여부를 검수한다.

---

### [실무]

PM Agent 검수 질문:

- 이 기능에 필요한 Resource는 무엇인가?
- 목록 조회가 필요한가?
- 상세 조회가 필요한가?
- 생성, 수정, 삭제가 필요한가?
- 인증이 필요한가?
- 권한 검증이 필요한가?
- Pagination이 필요한가?
- Search / Filter / Sort가 필요한가?
- Frontend 화면에서 필요한 Response Field가 포함되어 있는가?
- API 누락 또는 중복이 있는가?

---

### [Checklist]

PM Agent API Checklist:

- 요구사항이 API Use Case로 변환되었는가?
- Resource가 명확한가?
- 사용자 화면 흐름과 API 흐름이 연결되는가?
- 필요한 CRUD API가 식별되었는가?
- 필요한 Search / Filter API가 식별되었는가?
- 인증 필요 API와 공개 API가 구분되었는가?
- 관리자 API가 일반 API와 구분되었는가?
- 응답 데이터가 Frontend 화면 요구사항을 만족하는가?
- 기능 누락 API가 없는가?
- 중복 API가 없는가?

---

### [FAQ]

Q. PM Agent는 API Review에서 무엇을 확인하는가?

A. 요구사항이 API Use Case와 Resource로 올바르게 변환되었는지 확인한다.

Q. PM Agent가 API 누락을 찾는 기준은 무엇인가?

A. 사용자 화면 흐름, 기능 요구사항, CRUD 필요 여부, Search / Filter / Sort 필요 여부를 기준으로 찾는다.

Q. PM Agent가 Security를 확인해야 하는가?

A. 확인해야 한다. Public / Protected / Admin API 구분은 요구사항 단계에서 먼저 정리해야 한다.

---

# 3. Backend Agent API Review

## 3.1 Backend Agent Role

### [개념]

Backend Agent는 API Contract를 Spring Boot 3.x Controller, DTO, Service, Repository 구현으로 변환하고 구현 품질을 검수하는 역할을 수행한다.

Backend Agent는 API Contract와 Backend Layer가 일치하는지 확인한다.

```text
API Contract
→ Controller
→ Request DTO
→ Service
→ Repository
→ Response DTO
```

---

### [핵심]

- Backend Agent는 Controller Mapping을 검수한다.
- Backend Agent는 Request DTO와 Response DTO 분리를 검수한다.
- Backend Agent는 Validation 적용 여부를 검수한다.
- Backend Agent는 Business Validation 위치를 검수한다.
- Backend Agent는 ErrorCode와 Exception Mapping을 검수한다.
- Backend Agent는 Transaction과 Repository Query를 검수한다.
- Backend Agent는 Entity 직접 노출 여부를 검수한다.

---

### [실무]

Backend Agent 검수 기준:

```text
Controller
→ URI / Method / Parameter Binding 확인

Request DTO
→ Field / Type / Validation 확인

Service
→ Business Rule / Transaction / Authorization 확인

Repository
→ Query Method / Pagination / Sorting 확인

Response DTO
→ Entity 변환 / Field 노출 범위 확인

Exception
→ ErrorCode / StatusCode / ErrorResponse 확인
```

Spring Boot API 구현 검수 예시:

```java
@GetMapping("/festivals/{festivalId}")
public ApiResponse<FestivalDetailResponse> getFestival(
        @PathVariable Long festivalId
) {
    return ApiResponse.success(festivalService.getFestival(festivalId));
}
```

Backend Agent는 위 코드에서 다음을 확인한다.

- URI가 Resource 중심인가?
- Method가 GET인가?
- Path Variable 이름이 명확한가?
- Response DTO를 반환하는가?
- Resource 없음 예외가 404로 Mapping되는가?
- OpenAPI 문서가 있는가?

---

### [Checklist]

Backend Agent API Checklist:

- Controller Mapping이 API Contract와 일치하는가?
- URI Prefix가 프로젝트 규칙과 일치하는가?
- HTTP Method가 역할에 맞는가?
- Path Variable 이름이 명확한가?
- Query Parameter 이름이 문서와 일치하는가?
- Request DTO를 사용하는가?
- Response DTO를 사용하는가?
- Entity를 직접 Request / Response로 사용하지 않는가?
- `@Valid`가 필요한 곳에 적용되어 있는가?
- Service Layer에서 Business Validation을 수행하는가?
- Transaction 범위가 적절한가?
- Repository Query가 Pagination / Sorting을 지원하는가?
- ErrorCode가 Status Code와 일치하는가?
- GlobalExceptionHandler에서 예외가 처리되는가?

---

### [FAQ]

Q. Backend Agent는 API Review에서 무엇을 확인하는가?

A. API Contract가 Controller, DTO, Service, Repository, Error Handling으로 올바르게 구현되었는지 확인한다.

Q. Backend Agent가 가장 먼저 확인할 코드는 무엇인가?

A. Controller Mapping, Request DTO, Response DTO, ErrorCode, Service Business Validation이다.

Q. Backend API 구현에서 가장 흔한 문제는 무엇인가?

A. Entity 직접 노출, Validation 누락, Status Code 오사용, Error Response 불일치, Security 검증 누락이다.

---

# 4. Review Agent API Review

## 4.1 Review Agent Role

### [개념]

Review Agent는 API 설계와 구현의 결함을 탐지하고 수정 방향을 제시하는 검수 전용 Agent이다.

Review Agent는 API 품질을 Contract, Security, Maintainability, Troubleshooting 관점에서 평가한다.

```text
API Design
→ Backend Code
→ OpenAPI Document
→ Review Agent
→ Issue List
→ Fix Recommendation
```

---

### [핵심]

- Review Agent는 Contract Mismatch를 탐지한다.
- Review Agent는 URI Naming Issue를 탐지한다.
- Review Agent는 Method Misuse를 탐지한다.
- Review Agent는 Wrong Status Code를 탐지한다.
- Review Agent는 Missing Validation을 탐지한다.
- Review Agent는 Missing Authorization을 탐지한다.
- Review Agent는 Error Response Inconsistency를 탐지한다.
- Review Agent는 Pagination Issue를 탐지한다.
- Review Agent는 Breaking Change Risk를 탐지한다.

---

### [실무]

Review Agent 출력 형식은 문제, 영향, 원인, 수정 방향을 포함해야 한다.

```text
Issue:
GET /reviews API has no Pagination.

Impact:
Large response size and slow list rendering.

Cause:
Pageable is not applied to list API.

Fix:
Add Pageable parameter and return Page or Slice response.
```

Review Agent 우선순위:

1. Security Issue
2. Contract Mismatch
3. Data Loss / Duplicate Request Issue
4. Wrong Status Code
5. Missing Validation
6. Error Response Inconsistency
7. Pagination Missing
8. URI Naming Issue
9. OpenAPI Documentation Missing
10. Naming Convention Issue

---

### [Checklist]

Review Agent API Checklist:

- API Contract와 구현이 일치하는가?
- Swagger 문서와 실제 Response가 일치하는가?
- Frontend Axios URL과 Backend Mapping이 일치하는가?
- URI에 동사가 포함되어 있지 않은가?
- HTTP Method가 REST 역할에 맞는가?
- Status Code와 Error Code 의미가 일치하는가?
- Error Response Schema가 통일되어 있는가?
- Validation Error Response가 Field Error를 포함하는가?
- 인증 필요 API에 Security Requirement가 있는가?
- 권한 필요 API에 Authorization 검증이 있는가?
- 목록 API에 Pagination이 있는가?
- Search / Filter / Sort Parameter가 문서화되어 있는가?
- Breaking Change가 발생하지 않는가?

---

### [FAQ]

Q. Review Agent는 무엇을 우선 검수하는가?

A. Security Issue, Contract Mismatch, Wrong Status Code, Missing Validation, Error Response Inconsistency를 우선 검수한다.

Q. Review Agent 출력에는 무엇이 포함되어야 하는가?

A. 문제, 영향, 원인, 수정 방향이 포함되어야 한다.

Q. Review Agent가 Breaking Change를 확인해야 하는가?

A. 확인해야 한다. Response Field 변경, Error Code 변경, Required Field 추가는 배포 장애를 만들 수 있다.

---

# 5. Contract Quality Gate

## 5.1 API Contract Gate

### [개념]

Contract Quality Gate는 API가 개발 또는 배포되기 전에 반드시 통과해야 하는 최소 품질 기준이다.

Contract Quality Gate를 통과하지 못한 API는 Frontend 연동, 테스트, 배포 단계에서 오류를 만들 가능성이 높다.

```text
API Draft
→ Contract Gate
→ Implementation Gate
→ Documentation Gate
→ Integration Gate
→ Release
```

---

### [핵심]

- Contract Gate는 API 설계 단계의 품질 기준이다.
- Implementation Gate는 Backend 구현 단계의 품질 기준이다.
- Documentation Gate는 OpenAPI 문서 단계의 품질 기준이다.
- Integration Gate는 Frontend 연동 단계의 품질 기준이다.
- Gate 실패 시 수정 후 재검수한다.
- Quality Gate는 Review Agent의 판단 기준으로 사용한다.

---

### [실무]

API Quality Gate 단계:

```text
1. Contract Gate
   - Resource, URI, Method, Request, Response, Status Code 확정

2. Implementation Gate
   - Controller, DTO, Service, Repository, Exception 구현 확인

3. Security Gate
   - Authentication, Authorization, Ownership, Rate Limiting 확인

4. Documentation Gate
   - OpenAPI, Swagger UI, Example, Error Response 확인

5. Integration Gate
   - Frontend Axios, Network Response, UI Field Mapping 확인
```

---

### [Checklist]

Contract Gate Checklist:

- Resource가 명확한가?
- URI가 Resource 중심인가?
- HTTP Method가 적절한가?
- Request Contract가 정의되었는가?
- Response Contract가 정의되었는가?
- Error Contract가 정의되었는가?
- Status Code 기준이 명확한가?
- Authentication 필요 여부가 명확한가?
- Authorization 조건이 명확한가?
- Pagination 필요 여부가 검토되었는가?
- Versioning 필요 여부가 검토되었는가?
- Idempotency 필요 여부가 검토되었는가?

---

### [FAQ]

Q. Contract Quality Gate란 무엇인가?

A. API가 개발 또는 배포되기 전에 반드시 통과해야 하는 최소 품질 기준이다.

Q. Quality Gate가 필요한 이유는 무엇인가?

A. API 연동 오류, 테스트 실패, 배포 장애를 줄이기 위해 필요하다.

Q. Contract Gate에서 가장 중요한 기준은 무엇인가?

A. Resource, URI, Method, Request, Response, Error Contract, Status Code, Security 조건이다.

---

# 6. Security Quality Gate

## 6.1 Security Gate

### [개념]

Security Quality Gate는 API가 인증, 권한, 소유권, Rate Limiting, 민감 정보 보호 기준을 만족하는지 검수하는 단계이다.

Security Gate는 배포 전 반드시 확인해야 하는 고위험 API 검수 기준이다.

---

### [핵심]

- Public API와 Protected API를 구분한다.
- Admin API와 User API를 구분한다.
- 인증 실패는 401로 처리한다.
- 권한 실패는 403으로 처리한다.
- Ownership 검증이 필요한 API를 식별한다.
- Request Body의 userId를 신뢰하지 않는다.
- 민감 정보가 Response에 노출되지 않는지 확인한다.
- Rate Limiting 필요 API를 식별한다.

---

### [실무]

Security Gate 검수 대상:

| 대상                  | 검수 기준                       |
| --------------------- | ------------------------------- |
| Login API             | Rate Limiting, Error Response   |
| Signup API            | Validation, Duplicate Check     |
| User API              | Self Access, Token Required     |
| Review Update API     | Ownership Check                 |
| Admin API             | ROLE_ADMIN Required             |
| Payment API           | Authentication, Idempotency     |
| Password Reset API    | Rate Limiting, Token Expiration |
| AI Recommendation API | Abuse Prevention, Rate Limiting |

Security Flow:

```text
Request
→ Authentication
→ Authorization
→ Ownership Check
→ Business Logic
→ Response
```

---

### [Checklist]

Security Gate Checklist:

- 인증 필요 API가 Security Config에서 보호되는가?
- Public API가 의도대로 공개되어 있는가?
- Admin API가 ROLE_ADMIN으로 제한되는가?
- 사용자 본인 API가 Self 검증을 수행하는가?
- 수정 / 삭제 API가 Ownership 검증을 수행하는가?
- Request Body의 userId를 신뢰하지 않는가?
- Access Token을 Header로 받는가?
- 민감 정보가 Response DTO에서 제외되는가?
- Login / Signup / Password Reset API에 Rate Limiting이 고려되었는가?
- 인증 실패와 권한 실패가 401 / 403으로 분리되는가?

---

### [FAQ]

Q. Security Quality Gate란 무엇인가?

A. API가 인증, 권한, 소유권, Rate Limiting, 민감 정보 보호 기준을 만족하는지 검수하는 단계이다.

Q. Security Gate에서 가장 위험한 누락은 무엇인가?

A. 인증만 확인하고 Ownership 검증을 누락하는 것이다.

Q. Request Body의 userId를 신뢰하면 안 되는 이유는 무엇인가?

A. Client가 임의로 userId를 조작해 다른 사용자의 Resource에 접근할 수 있기 때문이다.

---

# 7. Error Quality Gate

## 7.1 Error Contract Gate

### [개념]

Error Quality Gate는 API 실패 응답이 Status Code, Error Code, Error Message, Field Error 기준에 맞는지 검수하는 단계이다.

Error Contract가 불안정하면 Frontend Error Handling과 사용자 메시지 처리가 불안정해진다.

---

### [핵심]

- Error Response Schema는 전역으로 통일한다.
- Status Code와 Error Code 의미는 일치해야 한다.
- Validation Error는 Field Error를 포함한다.
- Business Error는 명확한 Error Code를 가진다.
- Internal Error는 Stack Trace를 노출하지 않는다.
- 인증 실패와 권한 실패를 구분한다.
- 중복 또는 상태 충돌은 409로 처리한다.

---

### [실무]

Error Contract 기준:

```text
Validation Error → 400 + VALIDATION_FAILED
Authentication Error → 401 + INVALID_TOKEN
Authorization Error → 403 + ACCESS_DENIED
Resource Not Found → 404 + *_NOT_FOUND
Conflict Error → 409 + DUPLICATE_* or ALREADY_*
Server Error → 500 + INTERNAL_SERVER_ERROR
```

공통 Error Response:

```json
{
  "code": "FESTIVAL_NOT_FOUND",
  "message": "Festival not found"
}
```

Validation Error Response:

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

### [Checklist]

Error Gate Checklist:

- Error Response Schema가 통일되어 있는가?
- Error Code Naming이 일관적인가?
- Error Message가 짧고 명확한가?
- 400 Validation Error가 Field Error를 포함하는가?
- 401 Authentication Error가 분리되어 있는가?
- 403 Authorization Error가 분리되어 있는가?
- 404 Resource Not Found가 명확한가?
- 409 Conflict Error가 중복 / 상태 충돌에 사용되는가?
- 500 Error에서 Stack Trace가 노출되지 않는가?
- GlobalExceptionHandler에서 예상 가능한 예외를 처리하는가?

---

### [FAQ]

Q. Error Quality Gate란 무엇인가?

A. API 실패 응답이 Status Code, Error Code, Error Message, Field Error 기준에 맞는지 검수하는 단계이다.

Q. Error Contract에서 가장 중요한 것은 무엇인가?

A. Status Code와 Error Code 의미 일치, Error Response Schema 통일, Validation Field Error 제공이다.

Q. Stack Trace를 Error Response에 포함해도 되는가?

A. 안 된다. 내부 구현 정보가 노출되어 보안 문제가 될 수 있다.

---

# 8. Pagination Quality Gate

## 8.1 List API Gate

### [개념]

Pagination Quality Gate는 목록 조회 API가 대량 데이터 증가에 대비하여 Pagination, Filtering, Sorting 기준을 갖추었는지 검수하는 단계이다.

목록 API는 데이터 증가 가능성을 기본 전제로 설계해야 한다.

---

### [핵심]

- 목록 조회 API에는 Pagination 적용을 검토한다.
- Page, Slice, Cursor 중 적절한 방식을 선택한다.
- 기본 정렬 기준을 정의한다.
- size 기본값과 최대값을 정의한다.
- Filtering Parameter를 문서화한다.
- Sorting 가능한 Field를 제한한다.
- 무한 스크롤은 Slice 또는 Cursor를 고려한다.

---

### [실무]

List API 선택 기준:

```text
관리자 목록 → Page
검색 결과 → Page
더보기 목록 → Slice
무한 스크롤 → Slice or Cursor
채팅 메시지 → Cursor or Slice
알림 목록 → Cursor or Slice
로그 데이터 → Cursor
```

Pagination Contract 예시:

```text
GET /api/v1/festivals?page=0&size=20&sort=eventStartDate,asc
```

Cursor Contract 예시:

```text
GET /api/v1/chat-rooms/{chatRoomId}/messages?cursor=300&size=30
```

---

### [Checklist]

Pagination Gate Checklist:

- 목록 API에 Pagination이 적용되어 있는가?
- Page / Slice / Cursor 선택 이유가 명확한가?
- 기본 page 값이 정의되어 있는가?
- 기본 size 값이 정의되어 있는가?
- 최대 size 제한이 있는가?
- 기본 sort 기준이 있는가?
- 정렬 Field가 고유하지 않을 때 Tie-breaker가 있는가?
- Cursor 기준이 정렬 기준과 일치하는가?
- Response에 page metadata 또는 hasNext가 포함되는가?
- Count Query 비용이 큰 API에 Slice / Cursor를 고려했는가?

---

### [FAQ]

Q. Pagination Quality Gate란 무엇인가?

A. 목록 조회 API가 Pagination, Filtering, Sorting 기준을 갖추었는지 검수하는 단계이다.

Q. 목록 API에 기본 정렬이 필요한 이유는 무엇인가?

A. 정렬 기준이 없으면 페이지 이동 시 데이터 중복 또는 누락이 발생할 수 있기 때문이다.

Q. 무한 스크롤에는 어떤 방식이 적합한가?

A. Slice 또는 Cursor Pagination이 적합하다.

---

# 9. OpenAPI Quality Gate

## 9.1 Documentation Gate

### [개념]

OpenAPI Quality Gate는 API 문서가 실제 구현과 일치하고, Frontend / Backend 협업에 필요한 정보를 충분히 포함하는지 검수하는 단계이다.

OpenAPI 문서는 API Contract의 Source of Truth로 사용될 수 있다.

---

### [핵심]

- URI와 Method가 실제 Controller와 일치해야 한다.
- Request Schema가 Request DTO와 일치해야 한다.
- Response Schema가 Response DTO와 일치해야 한다.
- Error Response Schema가 문서화되어야 한다.
- Security Requirement가 인증 필요 API에 표시되어야 한다.
- Example이 실제 응답과 일치해야 한다.
- Pagination Parameter가 명확히 표시되어야 한다.

---

### [실무]

OpenAPI 문서 필수 포함 항목:

- Summary
- Description
- Tag
- Path Variable
- Query Parameter
- Request Body
- Success Response
- Error Response
- Status Code
- Security Requirement
- Example
- Pagination Metadata
- Validation Rule

Swagger UI 테스트 기준:

```text
Swagger UI
→ Request Example 입력
→ Execute
→ Status Code 확인
→ Response Schema 확인
→ Error Response 확인
→ Contract Mismatch 기록
```

---

### [Checklist]

OpenAPI Gate Checklist:

- Swagger UI에 API가 표시되는가?
- API Summary가 명확한가?
- API Description이 실제 동작과 일치하는가?
- Path Variable 설명과 Example이 있는가?
- Query Parameter 설명과 Example이 있는가?
- Request Body Schema가 DTO와 일치하는가?
- Response Body Schema가 DTO와 일치하는가?
- Error Response가 Status Code별로 문서화되어 있는가?
- 인증 필요 API에 Bearer Security Requirement가 있는가?
- Pageable Parameter가 문서화되어 있는가?
- Example이 실제 응답과 일치하는가?
- Deprecated API가 표시되어 있는가?

---

### [FAQ]

Q. OpenAPI Quality Gate란 무엇인가?

A. API 문서가 실제 구현과 일치하고 협업에 필요한 정보를 포함하는지 검수하는 단계이다.

Q. OpenAPI 문서에서 반드시 필요한 것은 무엇인가?

A. URI, Method, Request, Response, Error Response, Status Code, Security Requirement, Example이다.

Q. Swagger 문서와 실제 응답이 다르면 무엇인가?

A. Contract Mismatch이다.

---

# 10. Frontend Integration Gate

## 10.1 Frontend Backend Contract

### [개념]

Frontend Integration Gate는 Frontend Axios 요청, Backend API Mapping, Response Field, Error Handling이 서로 일치하는지 검수하는 단계이다.

Frontend 연동 오류 대부분은 API Contract 불일치에서 발생한다.

```text
Frontend Axios
→ Request URL
→ Backend Controller
→ Response DTO
→ Frontend State
→ UI Rendering
```

---

### [핵심]

- Axios Base URL과 Backend API Prefix가 일치해야 한다.
- Frontend Request Method와 Backend Method가 일치해야 한다.
- Query Parameter 이름이 일치해야 한다.
- Request Body Field 이름이 DTO와 일치해야 한다.
- Response Field 이름이 Frontend Type과 일치해야 한다.
- Error Code가 Frontend Error Handling과 일치해야 한다.
- 인증 API는 Axios Interceptor가 Token을 전달해야 한다.

---

### [실무]

Frontend / Backend 연동 검수 항목:

```text
Axios URL
→ /api/v1/festivals

Controller Mapping
→ @RequestMapping("/api/v1/festivals")

Network Request
→ GET /api/v1/festivals?page=0&size=20

Response Field
→ data.content[].festivalId

Frontend Usage
→ festival.festivalId
```

Axios 인증 흐름:

```text
Login
→ Access Token 저장
→ Axios Interceptor
→ Authorization Header 추가
→ Protected API Request
→ 401 발생 시 Refresh Flow
```

---

### [Checklist]

Frontend Integration Checklist:

- Axios Base URL이 맞는가?
- API Prefix가 맞는가?
- HTTP Method가 맞는가?
- Path Variable 값이 올바르게 들어가는가?
- Query Parameter 이름이 Backend와 일치하는가?
- Request Body Field 이름이 DTO와 일치하는가?
- Response Field 이름이 Frontend 사용 코드와 일치하는가?
- Pagination Response 구조가 Frontend 목록 처리와 일치하는가?
- Error Code가 Frontend Error Handling과 일치하는가?
- Authorization Header가 Protected API에 포함되는가?
- 401 Refresh Flow가 필요한 경우 구현되어 있는가?
- CORS 설정이 API 요청을 허용하는가?

---

### [FAQ]

Q. Frontend Integration Gate란 무엇인가?

A. Frontend Axios 요청, Backend API Mapping, Response Field, Error Handling이 일치하는지 검수하는 단계이다.

Q. Frontend 연동 오류에서 가장 먼저 확인할 것은 무엇인가?

A. Browser Network Tab의 Request URL, Method, Header, Body, Status Code, Response Body이다.

Q. Axios 요청은 맞는데 Backend에서 404가 발생하면 무엇을 확인하는가?

A. Axios Base URL, API Prefix, Controller Mapping, Proxy 설정을 확인한다.

---

# 11. Breaking Change Gate

## 11.1 Change Review

### [개념]

Breaking Change Gate는 API 변경이 기존 Client를 깨뜨릴 위험이 있는지 검수하는 단계이다.

Breaking Change Gate는 API 수정, 리팩터링, 배포 전 반드시 확인해야 한다.

---

### [핵심]

- Response Field 삭제는 위험하다.
- Response Field 이름 변경은 위험하다.
- Response Field Type 변경은 위험하다.
- Required Request Field 추가는 위험하다.
- Error Code 변경은 위험하다.
- Authentication 방식 변경은 위험하다.
- Pagination Response 구조 변경은 위험하다.
- Breaking Change는 Versioning 또는 Migration이 필요하다.

---

### [실무]

Breaking Change Review Table:

| 변경                          | 위험도 | 대응                   |
| ----------------------------- | -----: | ---------------------- |
| Optional Response Field 추가  |   낮음 | 문서 업데이트          |
| Optional Query Parameter 추가 |   낮음 | 문서 업데이트          |
| New Endpoint 추가             |   낮음 | 문서 업데이트          |
| Response Field 삭제           |   높음 | Deprecated 후 제거     |
| Response Field 이름 변경      |   높음 | Versioning             |
| Response Field Type 변경      |   높음 | Versioning             |
| Required Request Field 추가   |   높음 | Versioning 또는 기본값 |
| Error Code 변경               |   높음 | Frontend 합의          |
| Auth 방식 변경                |   높음 | Migration Plan         |

Breaking Change Flow:

```text
API Change
→ Contract Diff
→ Client Impact Check
→ Breaking Change 판단
→ Versioning / Deprecated / Migration
→ OpenAPI Update
→ Release
```

---

### [Checklist]

Breaking Change Checklist:

- Response Field가 삭제되었는가?
- Response Field 이름이 변경되었는가?
- Response Field Type이 변경되었는가?
- Request Required Field가 추가되었는가?
- Error Code가 변경되었는가?
- Error Response Schema가 변경되었는가?
- Pagination Response 구조가 변경되었는가?
- Authentication 방식이 변경되었는가?
- Authorization 조건이 강화되었는가?
- Frontend 영향도를 확인했는가?
- OpenAPI 문서를 업데이트했는가?
- Versioning 필요 여부를 판단했는가?

---

### [FAQ]

Q. Breaking Change Gate란 무엇인가?

A. API 변경이 기존 Client를 깨뜨릴 위험이 있는지 검수하는 단계이다.

Q. 가장 위험한 API 변경은 무엇인가?

A. Response Field 삭제, Field 이름 변경, Field Type 변경, Required Request Field 추가이다.

Q. Breaking Change가 있으면 어떻게 해야 하는가?

A. Versioning, Deprecated 처리, Migration Plan, Frontend 합의가 필요하다.

---

# 12. Final API Checklist

## 12.1 Final Review Checklist

### [Checklist]

API Final Checklist:

- API 목적이 명확한가?
- Resource가 명확한가?
- URI가 명사 기반인가?
- URI가 복수형 Resource를 사용하는가?
- URI에 불필요한 동사가 없는가?
- HTTP Method가 역할에 맞는가?
- Path Variable 이름이 구체적인가?
- Query Parameter가 검색 조건으로 분리되어 있는가?
- Request Header가 문서화되어 있는가?
- Request Body Schema가 정의되어 있는가?
- Request DTO와 Entity가 분리되어 있는가?
- Response DTO와 Entity가 분리되어 있는가?
- Success Response Schema가 통일되어 있는가?
- Error Response Schema가 통일되어 있는가?
- Status Code가 상황에 맞는가?
- Error Code가 Status Code와 의미상 일치하는가?
- Validation Rule이 Request DTO에 적용되어 있는가?
- Validation Error가 Field Error를 포함하는가?
- Business Validation이 Service Layer에 있는가?
- Authentication 필요 여부가 명확한가?
- Authorization 조건이 명확한가?
- Ownership 검증이 필요한 API에 적용되어 있는가?
- Public / Protected / Admin API가 구분되어 있는가?
- 목록 API에 Pagination이 적용되어 있는가?
- Filtering Parameter가 문서화되어 있는가?
- Sorting 기준이 문서화되어 있는가?
- 기본 Sort 기준이 있는가?
- size 최대값 제한이 있는가?
- Idempotency가 필요한 API에 중복 요청 처리가 있는가?
- Rate Limiting이 필요한 API가 식별되어 있는가?
- OpenAPI 문서가 실제 구현과 일치하는가?
- Swagger UI에서 테스트 가능한가?
- Frontend Axios URL과 Backend Mapping이 일치하는가?
- Response Field가 Frontend 사용 Field와 일치하는가?
- Date Time Format이 통일되어 있는가?
- Breaking Change 여부를 검토했는가?

---

### [실무]

Final API Review Score 기준:

|     점수 | 기준                          |
| -------: | ----------------------------- |
| 95 ~ 100 | Contract 안정, 실무 적용 가능 |
|  90 ~ 94 | 경미한 문서 보완 필요         |
|  80 ~ 89 | 구현 전 보완 필요             |
|  70 ~ 79 | Contract 오류 다수            |
|  70 미만 | API 재설계 필요               |

Critical Issue가 있으면 점수와 관계없이 배포 불가로 판단한다.

Critical Issue:

- 인증 필요 API가 공개됨
- 권한 검증 누락
- Entity 직접 노출로 민감 정보 반환
- Error Response 불일치
- Status Code 대량 오사용
- 목록 API Pagination 누락
- Swagger 문서와 실제 응답 불일치
- Breaking Change 미검토

---

### [FAQ]

Q. API Final Checklist는 언제 사용하는가?

A. API 설계 완료 후, 구현 완료 후, Frontend 연동 전, 배포 전 검수에 사용한다.

Q. Critical Issue가 있으면 어떻게 해야 하는가?

A. 배포하지 않고 수정 후 재검수해야 한다.

Q. API Review 목표 품질은 몇 점인가?

A. 최소 95점 이상, 목표는 97점 이상이다.

---

# 13. Agent Review Output Template

## 13.1 Review Output

### [개념]

Agent Review Output Template은 Review Agent가 API 검수 결과를 일관된 형식으로 출력하기 위한 템플릿이다.

일관된 출력 형식은 문제 추적, 수정 요청, 재검수에 유리하다.

---

### [핵심]

- Review 결과는 문제 단위로 작성한다.
- 각 문제는 Severity를 포함한다.
- 각 문제는 영향도를 포함한다.
- 각 문제는 원인을 포함한다.
- 각 문제는 수정 방향을 포함한다.
- Critical Issue는 별도로 표시한다.
- 최종 점수와 배포 가능 여부를 표시한다.

---

### [실무]

Review Agent 출력 템플릿:

```text
# API Review Result

## Summary

Score: 92/100
Release: Blocked
Critical Issues: 1
Major Issues: 2
Minor Issues: 3

---

## Critical Issue

### Issue 1

Severity: Critical

Problem:
Protected API is publicly accessible.

Impact:
Unauthorized users can access private user data.

Cause:
Security Config permits `/api/v1/users/**`.

Fix:
Change Security Config to require authentication for `/api/v1/users/**`.

---

## Major Issue

### Issue 2

Severity: Major

Problem:
List API has no Pagination.

Impact:
Large data response can cause performance degradation.

Cause:
Controller returns List instead of Page or Slice.

Fix:
Apply Pageable and return Page or Slice response.

---

## Final Decision

Release: Blocked until Critical Issue is fixed.
```

---

### [FAQ]

Q. Agent Review Output Template이 필요한 이유는 무엇인가?

A. Review 결과를 일관되게 작성하고 문제 수정과 재검수를 쉽게 하기 위해서이다.

Q. Review 결과에는 무엇이 포함되어야 하는가?

A. Severity, Problem, Impact, Cause, Fix, Score, Release Decision이 포함되어야 한다.

Q. Critical Issue가 있으면 Release는 어떻게 판단하는가?

A. Critical Issue가 해결될 때까지 Release Blocked로 판단한다.

---

# 14. Common Mistakes

## 14.1 Agent Review Mistakes

### [Troubleshooting]

문제: API Review가 단순 코드 스타일 검수로 끝난다.

원인: API Contract, Security, Error Response, Frontend 연동을 함께 보지 않았다.

해결: Contract Gate, Security Gate, Error Gate, Frontend Integration Gate를 함께 적용한다.

---

문제: Review Agent가 URI Naming만 지적하고 Security 누락을 놓친다.

원인: Review 우선순위가 잘못되었다.

해결: Security Issue와 Contract Mismatch를 최우선으로 검수한다.

---

문제: API가 Swagger 문서에는 정상인데 Frontend 연동이 실패한다.

원인: Swagger 문서와 실제 응답 또는 Frontend Type이 다르다.

해결: Swagger UI Response, Browser Network Response, Frontend 사용 Field를 비교한다.

---

문제: Review 결과가 수정하기 어렵다.

원인: 문제만 있고 원인과 수정 방향이 없다.

해결: Problem, Impact, Cause, Fix 형식으로 작성한다.

---

문제: API 점수는 높지만 배포 후 장애가 발생한다.

원인: Critical Issue를 점수와 분리해 차단하지 않았다.

해결: 인증 누락, 권한 누락, 민감 정보 노출, Breaking Change는 Release Blocked로 판단한다.

---

문제: API 변경 후 기존 화면이 깨진다.

원인: Breaking Change Gate를 수행하지 않았다.

해결: Contract Diff, Frontend 영향도, Versioning 필요 여부를 검토한다.

---

문제: 목록 API가 개발 중에는 빠르지만 데이터 증가 후 느려진다.

원인: Pagination Gate와 size 제한 검토가 없었다.

해결: Page / Slice / Cursor 선택, 기본 Sort, 최대 size 제한을 적용한다.

---

### [FAQ]

Q. Agent Review에서 가장 흔한 실수는 무엇인가?

A. 코드 스타일만 보고 Contract, Security, Error Response, Frontend 연동을 놓치는 것이다.

Q. Review 우선순위는 어떻게 잡아야 하는가?

A. Security Issue, Contract Mismatch, Data Loss, Wrong Status Code, Missing Validation을 우선한다.

Q. Review 결과가 실무적으로 유용하려면 무엇이 필요한가?

A. 문제, 영향, 원인, 수정 방향이 명확해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. API Agent Review란 무엇인가?
A. API 설계와 구현이 Contract 기준에 맞는지 Agent가 검수하는 과정이다.

Q. API Review에서 가장 중요한 것은 무엇인가?
A. API Contract 일치성, Security Contract, Status Code, Error Response, Validation, Pagination이다.

Q. PM Agent는 API Review에서 무엇을 확인하는가?
A. 요구사항이 API Use Case와 Resource로 올바르게 변환되었는지 확인한다.

Q. Backend Agent는 API Review에서 무엇을 확인하는가?
A. API Contract가 Controller, DTO, Service, Repository, Error Handling으로 올바르게 구현되었는지 확인한다.

Q. Review Agent는 무엇을 우선 검수하는가?
A. Security Issue, Contract Mismatch, Wrong Status Code, Missing Validation, Error Response Inconsistency를 우선 검수한다.

Q. Contract Quality Gate란 무엇인가?
A. API가 개발 또는 배포되기 전에 반드시 통과해야 하는 최소 품질 기준이다.

Q. Security Quality Gate란 무엇인가?
A. API가 인증, 권한, 소유권, Rate Limiting, 민감 정보 보호 기준을 만족하는지 검수하는 단계이다.

Q. Error Quality Gate란 무엇인가?
A. API 실패 응답이 Status Code, Error Code, Error Message, Field Error 기준에 맞는지 검수하는 단계이다.

Q. Pagination Quality Gate란 무엇인가?
A. 목록 조회 API가 Pagination, Filtering, Sorting 기준을 갖추었는지 검수하는 단계이다.

Q. OpenAPI Quality Gate란 무엇인가?
A. API 문서가 실제 구현과 일치하고 협업에 필요한 정보를 포함하는지 검수하는 단계이다.

Q. Frontend Integration Gate란 무엇인가?
A. Frontend Axios 요청, Backend API Mapping, Response Field, Error Handling이 일치하는지 검수하는 단계이다.

Q. Breaking Change Gate란 무엇인가?
A. API 변경이 기존 Client를 깨뜨릴 위험이 있는지 검수하는 단계이다.

Q. Critical Issue란 무엇인가?
A. 배포를 차단해야 하는 심각한 API 문제이다.

Q. Critical Issue 예시는 무엇인가?
A. 인증 누락, 권한 누락, 민감 정보 노출, Error Response 불일치, Breaking Change 미검토이다.

Q. API Final Checklist는 언제 사용하는가?
A. API 설계 완료 후, 구현 완료 후, Frontend 연동 전, 배포 전 검수에 사용한다.

Q. API Review 목표 품질은 몇 점인가?
A. 최소 95점 이상, 목표는 97점 이상이다.

Q. Agent Review Output Template이 필요한 이유는 무엇인가?
A. Review 결과를 일관되게 작성하고 문제 수정과 재검수를 쉽게 하기 위해서이다.

Q. Review 결과에는 무엇이 포함되어야 하는가?
A. Severity, Problem, Impact, Cause, Fix, Score, Release Decision이 포함되어야 한다.

Q. Critical Issue가 있으면 Release는 어떻게 판단하는가?
A. Critical Issue가 해결될 때까지 Release Blocked로 판단한다.

Q. API Review에서 가장 흔한 실수는 무엇인가?
A. 코드 스타일만 보고 Contract, Security, Error Response, Frontend 연동을 놓치는 것이다.

Q. Review 우선순위는 어떻게 잡아야 하는가?
A. Security Issue, Contract Mismatch, Data Loss, Wrong Status Code, Missing Validation을 우선한다.

Q. Review 결과가 실무적으로 유용하려면 무엇이 필요한가?
A. 문제, 영향, 원인, 수정 방향이 명확해야 한다.
