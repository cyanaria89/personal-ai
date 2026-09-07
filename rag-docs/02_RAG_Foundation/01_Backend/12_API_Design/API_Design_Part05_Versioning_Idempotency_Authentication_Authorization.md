# API Design Part 05 - Versioning, Idempotency, Authentication, Authorization & Rate Limiting

---

# 1. API Versioning

## 1.1 Versioning

### [개념]

API Versioning은 API Contract 변경을 안전하게 관리하기 위해 API 버전을 구분하는 설계 방식이다.

API Versioning은 기존 Client를 깨뜨리지 않고 새로운 Request / Response Contract를 제공하기 위한 변경 관리 전략이다.

```text
/api/v1/users
/api/v2/users
```

---

### [핵심]

- Versioning은 API 변경 관리 전략이다.
- Versioning은 Breaking Change를 분리한다.
- 기존 Client의 Backward Compatibility를 보호한다.
- URI Versioning 또는 Header Versioning을 사용할 수 있다.
- API Version은 문서, Controller, DTO, OpenAPI Contract와 함께 관리한다.
- Versioning은 남용하지 않고 필요할 때 적용한다.

---

### [실무]

2026 실무 기준 REST API에서는 URI Versioning을 가장 쉽게 적용할 수 있다.

```text
/api/v1/festivals
/api/v1/festivals/{festivalId}
/api/v1/reviews
```

Versioning이 필요한 상황:

- Response Field 삭제
- Response Field 이름 변경
- Response Field Type 변경
- Required Request Field 추가
- Error Code 구조 변경
- 인증 방식 변경
- Pagination Response 구조 변경
- Rate Limiting 정책 변경으로 Client 동작이 바뀌는 경우

Versioning 없이 가능한 변경:

- Optional Response Field 추가
- New Endpoint 추가
- Optional Query Parameter 추가
- Error Message 문구 보완
- 내부 구현 변경

---

### [FAQ]

Q. API Versioning이란 무엇인가?

A. API Contract 변경을 안전하게 관리하기 위해 API 버전을 구분하는 설계 방식이다.

Q. API Versioning은 언제 필요한가?

A. 기존 Client를 깨뜨릴 수 있는 Breaking Change가 발생할 때 필요하다.

Q. Versioning 없이 가능한 변경은 무엇인가?

A. Optional Field 추가, New Endpoint 추가, Optional Query Parameter 추가처럼 기존 Client를 깨뜨리지 않는 변경이다.

---

# 2. URI Versioning

## 2.1 URI Versioning

### [개념]

URI Versioning은 API 버전을 URI Path에 포함하는 방식이다.

```text
/api/v1/users
/api/v2/users
```

URI Versioning은 가장 명확하고 테스트하기 쉬운 Versioning 방식이다.

---

### [핵심]

- 버전이 URI에 직접 표시된다.
- Frontend와 Backend가 버전을 쉽게 구분할 수 있다.
- Swagger UI와 OpenAPI 문서화가 쉽다.
- Routing과 Controller 분리가 쉽다.
- URL이 길어질 수 있다.
- Version 증가 기준을 명확히 정해야 한다.

---

### [실무]

Spring Boot 3.x에서는 Controller RequestMapping에 Version Prefix를 둔다.

```java
@RestController
@RequestMapping("/api/v1/festivals")
public class FestivalController {

    @GetMapping("/{festivalId}")
    public ApiResponse<FestivalResponse> getFestival(
            @PathVariable Long festivalId
    ) {
        return ApiResponse.success(festivalService.getFestival(festivalId));
    }
}
```

v2 API가 필요하면 Controller Package 또는 Class를 분리할 수 있다.

```text
com.example.api.v1.FestivalController
com.example.api.v2.FestivalController
```

---

### [Best Practice]

- `/api/v1` Prefix를 프로젝트 전체에서 통일한다.
- Version Prefix 위치를 일관되게 유지한다.
- Version별 OpenAPI Group을 분리할 수 있다.
- v1과 v2 Response DTO를 섞지 않는다.
- Version 증가 사유를 문서화한다.
- Deprecated API 제거 일정을 관리한다.

---

### [FAQ]

Q. URI Versioning이란 무엇인가?

A. API 버전을 URI Path에 포함하는 방식이다.

Q. URI Versioning의 장점은 무엇인가?

A. 버전이 명확히 보이고 Routing, 테스트, 문서화가 쉽다.

Q. URI Versioning의 단점은 무엇인가?

A. URL에 버전이 노출되고 Version Prefix가 모든 Endpoint에 포함된다.

---

# 3. Header Versioning

## 3.1 Header Versioning

### [개념]

Header Versioning은 API 버전을 URI가 아니라 Request Header에 담아 전달하는 방식이다.

```http
GET /api/users HTTP/1.1
API-Version: 1
```

또는 Accept Header를 사용할 수 있다.

```http
Accept: application/vnd.example.v1+json
```

---

### [핵심]

- URI가 버전 정보로 오염되지 않는다.
- Client는 Header로 원하는 API Version을 명시한다.
- 같은 URI에서 Version별 Response를 다르게 제공할 수 있다.
- 테스트와 디버깅이 URI Versioning보다 어렵다.
- Swagger UI 문서화가 더 복잡할 수 있다.
- Header Versioning은 팀 Convention이 중요하다.

---

### [실무]

Header Versioning은 Public API, 외부 파트너 API, API Gateway 환경에서 사용할 수 있다.

Spring Boot에서는 Header 조건으로 Mapping을 분리할 수 있다.

```java
@GetMapping(value = "/users/{userId}", headers = "API-Version=1")
public ApiResponse<UserV1Response> getUserV1(
        @PathVariable Long userId
) {
    return ApiResponse.success(userService.getUserV1(userId));
}
```

```java
@GetMapping(value = "/users/{userId}", headers = "API-Version=2")
public ApiResponse<UserV2Response> getUserV2(
        @PathVariable Long userId
) {
    return ApiResponse.success(userService.getUserV2(userId));
}
```

---

### [주의]

- Header 누락 시 기본 Version 정책을 정해야 한다.
- Cache, Proxy, Gateway에서 Header를 고려해야 한다.
- Swagger UI에서 Version 선택 방법을 제공해야 한다.
- Frontend Axios Instance에 Version Header를 설정해야 한다.
- 내부 팀 프로젝트에서는 URI Versioning이 더 단순할 수 있다.

---

### [FAQ]

Q. Header Versioning이란 무엇인가?

A. API 버전을 Request Header에 담아 전달하는 방식이다.

Q. Header Versioning의 장점은 무엇인가?

A. URI를 깔끔하게 유지하고 같은 URI에서 Version별 Contract를 제공할 수 있다.

Q. Header Versioning의 단점은 무엇인가?

A. 테스트, 디버깅, 문서화가 URI Versioning보다 복잡할 수 있다.

---

# 4. Breaking Change

## 4.1 Breaking Change

### [개념]

Breaking Change는 기존 Client가 더 이상 정상 동작하지 않게 만드는 API Contract 변경이다.

Breaking Change는 Versioning, Deprecation, Migration Plan이 필요한 변경이다.

```text
Response Field Changed
→ Frontend Mapping Fail
→ Runtime Error
```

---

### [핵심]

- Response Field 삭제는 Breaking Change이다.
- Response Field 이름 변경은 Breaking Change이다.
- Response Field Type 변경은 Breaking Change이다.
- Required Request Field 추가는 Breaking Change이다.
- Error Code 변경은 Breaking Change일 수 있다.
- Authentication 방식 변경은 Breaking Change일 수 있다.
- Pagination Response 구조 변경은 Breaking Change일 수 있다.
- Rate Limiting 정책 변경은 Client Retry Flow에 영향을 줄 수 있다.

---

### [실무]

Breaking Change 판단 기준:

| 변경                               | Breaking Change 여부 |
| ---------------------------------- | -------------------- |
| Response Field 삭제                | Yes                  |
| Response Field 이름 변경           | Yes                  |
| Response Field Type 변경           | Yes                  |
| Required Request Field 추가        | Yes                  |
| Optional Response Field 추가       | No                   |
| Optional Query Parameter 추가      | No                   |
| New Endpoint 추가                  | No                   |
| Error Message 문구 수정            | 보통 No              |
| Error Code 변경                    | Yes 가능성 높음      |
| Authentication 방식 변경           | Yes 가능성 높음      |
| Rate Limit 적용으로 기존 요청 차단 | Yes 가능성 있음      |

Breaking Change 처리 흐름:

```text
Change Request
→ Contract Impact Review
→ Breaking Change 판단
→ Versioning 여부 결정
→ OpenAPI Update
→ Frontend Migration
→ Deprecated API 제거
```

---

### [Best Practice]

- Field 삭제보다 Deprecated 처리를 우선한다.
- Optional Field 추가를 선호한다.
- 기존 Error Code를 쉽게 변경하지 않는다.
- Breaking Change는 Review Agent가 반드시 표시해야 한다.
- OpenAPI Diff 검수를 수행한다.
- Migration Guide를 작성한다.
- Rate Limit 신규 적용 시 Frontend Retry / 안내 UI 영향도 확인한다.

---

### [FAQ]

Q. Breaking Change란 무엇인가?

A. 기존 Client가 더 이상 정상 동작하지 않게 만드는 API Contract 변경이다.

Q. Response Field 이름 변경은 Breaking Change인가?

A. 대부분 Breaking Change이다. Client Mapping 오류가 발생할 수 있다.

Q. Breaking Change를 줄이는 방법은 무엇인가?

A. Optional Field 추가, Deprecated 처리, Versioning, Backward Compatibility 유지가 필요하다.

---

# 5. Backward Compatibility

## 5.1 Compatibility

### [개념]

Backward Compatibility는 기존 Client가 API 변경 후에도 정상 동작하도록 기존 Contract를 유지하는 원칙이다.

Backward Compatibility는 API 안정성과 배포 안정성을 높인다.

---

### [핵심]

- 기존 Response Field를 유지한다.
- 기존 Error Code를 유지한다.
- 기존 Required Field 규칙을 갑자기 강화하지 않는다.
- 새로운 Field는 Optional로 추가한다.
- 기존 Endpoint 동작을 갑자기 바꾸지 않는다.
- Deprecated Field는 일정 기간 유지한다.
- 기존 Client가 예상하지 못한 Rate Limit 차단을 만들지 않는다.

---

### [실무]

안전한 변경 예시:

```json
{
  "festivalId": 1,
  "title": "Seoul Festival",
  "address": "Seoul",
  "thumbnailUrl": "https://example.com/image.jpg"
}
```

기존 응답에 Optional Field를 추가하는 것은 보통 안전하다.

```json
{
  "festivalId": 1,
  "title": "Seoul Festival",
  "address": "Seoul",
  "thumbnailUrl": "https://example.com/image.jpg",
  "averageRating": 4.7
}
```

위 변경은 기존 Client가 모르는 Field를 무시할 수 있으면 Backward Compatible하다.

---

### [주의]

- Optional Field 추가도 일부 엄격한 Client에서는 문제가 될 수 있다.
- Field Type 변경은 Backward Compatible하지 않다.
- Enum 값 추가는 Client 처리 방식에 따라 위험할 수 있다.
- Error Code 변경은 Frontend Error Handling을 깨뜨릴 수 있다.
- API Gateway, Cache, Mobile App 배포 주기를 함께 고려한다.
- Rate Limit 정책 변경은 기존 Client 호출 빈도를 분석한 뒤 적용한다.

---

### [FAQ]

Q. Backward Compatibility란 무엇인가?

A. API 변경 후에도 기존 Client가 정상 동작하도록 기존 Contract를 유지하는 원칙이다.

Q. Optional Response Field 추가는 안전한가?

A. 대부분 안전하지만 엄격한 Client에서는 문제가 될 수 있으므로 문서화가 필요하다.

Q. Error Code 변경이 위험한 이유는 무엇인가?

A. Frontend가 Error Code를 기준으로 사용자 메시지나 분기 처리를 할 수 있기 때문이다.

---

# 6. Idempotency

## 6.1 Idempotent API

### [개념]

Idempotency는 같은 요청을 여러 번 보내도 최종 결과가 동일한 성질이다.

Idempotent API는 네트워크 오류, Retry, 중복 클릭, 결제 재시도 같은 상황에서 안정성을 높인다.

```text
Same Request
→ Execute Once
→ Retry
→ Same Final Result
```

---

### [핵심]

- GET은 Safe하고 Idempotent하다.
- PUT은 Idempotent해야 한다.
- DELETE는 Idempotent하게 설계하는 것이 좋다.
- POST는 기본적으로 Idempotent하지 않다.
- 결제, 주문, 예약, 좋아요 같은 API는 중복 요청 처리가 중요하다.
- Idempotency Key를 사용할 수 있다.

---

### [실무]

Idempotency가 중요한 API:

- 결제 승인
- 주문 생성
- 예약 생성
- 후원 결제
- 이메일 발송
- 알림 발송
- 좋아요 등록
- 즐겨찾기 등록

POST 생성 API는 중복 요청으로 Resource가 여러 번 생성될 수 있다.

이를 방지하기 위해 Idempotency Key 또는 Unique Constraint를 사용할 수 있다.

```http
POST /payments/confirm HTTP/1.1
Idempotency-Key: 8c7b2d3f-2026-06-27
Content-Type: application/json
```

---

### [FAQ]

Q. Idempotency란 무엇인가?

A. 같은 요청을 여러 번 보내도 최종 결과가 동일한 성질이다.

Q. POST는 Idempotent한가?

A. 기본적으로 Idempotent하지 않다. 같은 요청을 반복하면 여러 Resource가 생성될 수 있다.

Q. Idempotency가 중요한 API는 무엇인가?

A. 결제, 주문, 예약, 후원, 이메일 발송, 좋아요 등록처럼 중복 처리 위험이 있는 API이다.

---

# 7. Idempotency Key

## 7.1 Idempotency Key

### [개념]

Idempotency Key는 Client가 중복 요청을 식별하기 위해 보내는 고유한 Key이다.

Server는 같은 Idempotency Key 요청을 한 번만 처리하거나 이전 처리 결과를 재사용한다.

```text
Client Request + Idempotency-Key
→ Server checks key
→ First request processed
→ Duplicate request returns same result
```

---

### [핵심]

- Idempotency Key는 중복 요청 방지에 사용한다.
- Client가 고유한 Key를 생성한다.
- Server는 Key와 처리 결과를 저장한다.
- 같은 Key 요청은 중복 처리하지 않는다.
- Key 저장 기간을 정해야 한다.
- Key Scope를 사용자, API, Resource 단위로 정해야 한다.

---

### [실무]

결제 API Idempotency Key 처리 흐름:

```text
POST /payments/confirm
→ Read Idempotency-Key
→ Check existing key
→ If not exists: process payment
→ Save key and result
→ Return response
→ If exists: return saved result
```

DB 저장 예시:

| Field          | Description                   |
| -------------- | ----------------------------- |
| idempotencyKey | Client Unique Key             |
| userId         | 요청 사용자                   |
| requestHash    | 요청 Body Hash                |
| responseBody   | 최초 응답                     |
| status         | PROCESSING / SUCCESS / FAILED |
| expiresAt      | Key 만료 시각                 |

---

### [주의]

- 같은 Key로 다른 Request Body를 보내는 경우 Conflict 처리한다.
- Key 저장소 장애를 고려한다.
- Processing 상태 중복 요청 정책을 정한다.
- Key를 영구 저장하지 않고 TTL을 둔다.
- 결제 Provider의 Idempotency 정책과 서비스 정책을 함께 맞춘다.

---

### [FAQ]

Q. Idempotency Key란 무엇인가?

A. 중복 요청을 식별하기 위해 Client가 보내는 고유한 Key이다.

Q. 같은 Idempotency Key로 다른 Body가 오면 어떻게 처리하는가?

A. 보통 409 Conflict로 처리한다.

Q. Idempotency Key는 어디에 담는가?

A. 보통 `Idempotency-Key` Request Header에 담는다.

---

# 8. Duplicate Request Handling

## 8.1 Duplicate Request

### [개념]

Duplicate Request Handling은 동일한 요청이 여러 번 들어왔을 때 중복 처리, 중복 저장, 중복 결제를 방지하는 API 설계이다.

중복 요청은 네트워크 Retry, 사용자 더블 클릭, Client Timeout, 서버 응답 지연으로 발생할 수 있다.

---

### [핵심]

- 중복 요청은 실무에서 자주 발생한다.
- POST API는 중복 생성 위험이 있다.
- Unique Constraint로 중복 데이터를 방지할 수 있다.
- Idempotency Key로 중복 처리를 제어할 수 있다.
- Business Rule로 이미 처리된 요청을 감지할 수 있다.
- Duplicate Request 실패는 409 Conflict를 사용할 수 있다.
- 중복 요청 방지는 Rate Limiting과 역할이 다르다.

---

### [실무]

좋아요 등록 API 중복 처리 예시:

```java
@Transactional
public void likeFestival(Long userId, Long festivalId) {
    if (festivalLikeRepository.existsByUserIdAndFestivalId(userId, festivalId)) {
        throw new BusinessException(ErrorCode.ALREADY_LIKED_FESTIVAL);
    }

    festivalLikeRepository.save(FestivalLike.create(userId, festivalId));
}
```

DB Unique Constraint 예시:

```text
UNIQUE(user_id, festival_id)
```

결제 API는 Idempotency Key와 결제 상태를 함께 확인한다.

```text
Payment Status:
READY → CONFIRMED
CONFIRMED → Duplicate Confirm Request
FAILED → Retry Policy Check
```

Duplicate Request와 Rate Limiting 차이:

| 구분                       | 목적                              |
| -------------------------- | --------------------------------- |
| Duplicate Request Handling | 같은 요청의 중복 처리 방지        |
| Rate Limiting              | 과도한 요청량 제한                |
| Idempotency Key            | 중복 요청 식별                    |
| 429 Too Many Requests      | 요청량 초과 응답                  |
| 409 Conflict               | 중복 상태 또는 비즈니스 충돌 응답 |

---

### [FAQ]

Q. 중복 요청은 왜 발생하는가?

A. 네트워크 Retry, 더블 클릭, Timeout, 응답 지연 때문에 발생한다.

Q. 중복 요청은 어떻게 방지하는가?

A. Idempotency Key, Unique Constraint, Business Validation으로 방지한다.

Q. 중복 생성 요청은 어떤 Status Code를 사용할 수 있는가?

A. 보통 409 Conflict를 사용할 수 있다.

---

# 9. Authentication

## 9.1 Authentication

### [개념]

Authentication은 사용자가 누구인지 확인하는 과정이다.

API Authentication은 Request를 보낸 Client 또는 User의 신원을 검증한다.

```text
Request
→ Credential
→ Authentication
→ Authenticated User
```

---

### [핵심]

- Authentication은 신원 확인이다.
- Authorization과 구분해야 한다.
- Token 기반 인증을 많이 사용한다.
- JWT Authentication은 Stateless API와 잘 맞는다.
- 인증 실패는 401 Unauthorized를 사용한다.
- 인증 정보는 보통 Authorization Header에 담는다.

---

### [실무]

JWT 기반 API 인증 흐름:

```text
Login Request
→ Credential Validation
→ Access Token issued
→ Client stores token
→ API Request with Authorization Header
→ JWT Filter validates token
→ SecurityContext stores Authentication
→ Controller
```

API 요청 예시:

```http
GET /api/v1/users/me HTTP/1.1
Authorization: Bearer access-token
```

인증 실패 Error Mapping:

```text
Missing Token → 401 Unauthorized
Invalid Token → 401 Unauthorized
Expired Token → 401 Unauthorized
Malformed Token → 401 Unauthorized
```

---

### [FAQ]

Q. Authentication이란 무엇인가?

A. 사용자가 누구인지 확인하는 과정이다.

Q. 인증 실패는 어떤 Status Code를 사용하는가?

A. 401 Unauthorized를 사용한다.

Q. JWT는 API 요청에서 어디에 담는가?

A. `Authorization: Bearer access-token` Header에 담는다.

---

# 10. Token Authentication

## 10.1 Access Token

### [개념]

Access Token은 인증된 사용자가 API에 접근할 때 사용하는 짧은 수명의 인증 Token이다.

Access Token은 Request마다 Authorization Header에 포함된다.

```http
Authorization: Bearer access-token
```

---

### [핵심]

- Access Token은 API 인증에 사용한다.
- Access Token은 짧은 만료 시간을 권장한다.
- Access Token은 Request마다 전달된다.
- Server는 Token Signature, Expiration, Claims를 검증한다.
- Token이 유효하면 Authentication을 구성한다.
- Access Token 만료 시 Refresh Token으로 재발급할 수 있다.

---

### [실무]

JWT Access Token 검증 항목:

- Signature 유효성
- Expiration 만료 여부
- Issuer
- Subject
- Role / Authority
- Token Type
- Blacklist 여부

JWT Filter 처리 흐름:

```text
Authorization Header
→ Extract Bearer Token
→ Validate Access Token
→ Load User Details
→ Create Authentication
→ Save SecurityContext
→ Continue Filter Chain
```

---

### [주의]

- Access Token을 LocalStorage에 저장할 경우 XSS 위험을 고려한다.
- Access Token을 Query Parameter로 전달하지 않는다.
- Token 만료 시간을 무한정 길게 잡지 않는다.
- Token Payload에 민감 정보를 넣지 않는다.
- HTTPS 사용을 기본 전제로 한다.
- Rate Limiting 대상 식별 시 IP뿐 아니라 인증 사용자 기준도 고려한다.

---

### [FAQ]

Q. Access Token은 무엇인가?

A. 인증된 사용자가 API에 접근할 때 사용하는 짧은 수명의 인증 Token이다.

Q. Access Token 검증 항목은 무엇인가?

A. Signature, Expiration, Issuer, Subject, Role, Token Type 등을 검증한다.

Q. Access Token에 민감 정보를 넣어도 되는가?

A. 안 된다. JWT Payload는 복호화가 아니라 Base64URL Encoding된 값이므로 노출될 수 있다.

---

# 11. Authorization

## 11.1 Authorization

### [개념]

Authorization은 인증된 사용자가 특정 Resource 또는 Action에 접근할 권한이 있는지 확인하는 과정이다.

Authentication이 “누구인가”를 확인한다면 Authorization은 “무엇을 할 수 있는가”를 확인한다.

```text
Authenticated User
→ Check Role / Permission / Ownership
→ Allow or Deny
```

---

### [핵심]

- Authorization은 권한 검증이다.
- Authentication 이후에 수행된다.
- 권한 실패는 403 Forbidden을 사용한다.
- Role 기반 권한 검증을 사용할 수 있다.
- Permission 기반 권한 검증을 사용할 수 있다.
- Resource Ownership 검증이 필요할 수 있다.
- Authorization은 Controller, Method Security, Service Layer에서 처리할 수 있다.

---

### [실무]

Role 기반 API 예시:

```java
@PreAuthorize("hasRole('ADMIN')")
@DeleteMapping("/admin/users/{userId}")
public ApiResponse<Void> deleteUser(
        @PathVariable Long userId
) {
    userService.deleteUser(userId);
    return ApiResponse.success();
}
```

Ownership 기반 검증 예시:

```java
public void updateReview(Long userId, Long reviewId, ReviewUpdateRequest request) {
    Review review = reviewRepository.findById(reviewId)
            .orElseThrow(() -> new BusinessException(ErrorCode.REVIEW_NOT_FOUND));

    if (!review.isWrittenBy(userId)) {
        throw new BusinessException(ErrorCode.ACCESS_DENIED);
    }

    review.update(request.content());
}
```

---

### [FAQ]

Q. Authorization이란 무엇인가?

A. 인증된 사용자가 특정 Resource 또는 Action에 접근할 권한이 있는지 확인하는 과정이다.

Q. 권한 실패는 어떤 Status Code를 사용하는가?

A. 403 Forbidden을 사용한다.

Q. Authentication과 Authorization의 차이는 무엇인가?

A. Authentication은 신원 확인이고 Authorization은 권한 확인이다.

---

# 12. Permission Model

## 12.1 Role Permission Ownership

### [개념]

Permission Model은 API 접근 권한을 Role, Permission, Ownership 기준으로 정의하는 구조이다.

```text
Role: ADMIN, USER
Permission: REVIEW_DELETE, USER_BLOCK
Ownership: ownerId == currentUserId
```

---

### [핵심]

- Role은 사용자 그룹 권한이다.
- Permission은 세부 기능 권한이다.
- Ownership은 Resource 소유자 검증이다.
- 일반 서비스는 Role + Ownership 조합을 많이 사용한다.
- 관리자 기능은 Role 또는 Permission을 사용한다.
- API Contract에는 인증 필요 여부와 권한 조건을 명시한다.

---

### [실무]

API 권한 명세 예시:

| API                          | Authentication | Authorization |
| ---------------------------- | -------------- | ------------- |
| GET /festivals               | Public         | None          |
| POST /reviews                | Required       | ROLE_USER     |
| PATCH /reviews/{reviewId}    | Required       | Review Owner  |
| DELETE /admin/users/{userId} | Required       | ROLE_ADMIN    |
| GET /users/me                | Required       | Self          |

Service Layer Ownership 검증은 Method Security만으로 부족한 Resource 단위 권한을 처리한다.

```text
Request User ID
→ Load Resource
→ Compare Owner ID
→ Allow or Deny
```

---

### [주의]

- 인증만 하고 소유권 검증을 누락하지 않는다.
- User ID를 Request Body에서 받아 신뢰하지 않는다.
- 현재 사용자 ID는 SecurityContext에서 가져온다.
- 관리자 API와 일반 사용자 API를 구분한다.
- 권한 실패와 Resource 없음 응답 정책을 정한다.

---

### [FAQ]

Q. Role과 Permission의 차이는 무엇인가?

A. Role은 사용자 그룹 권한이고 Permission은 기능 단위 세부 권한이다.

Q. Ownership 검증은 무엇인가?

A. 현재 사용자가 해당 Resource의 소유자인지 확인하는 권한 검증이다.

Q. 현재 사용자 ID는 어디에서 가져와야 하는가?

A. Request Body가 아니라 인증된 SecurityContext에서 가져와야 한다.

---

# 13. Public API and Protected API

## 13.1 Access Level

### [개념]

Public API는 인증 없이 접근 가능한 API이고 Protected API는 인증 또는 권한 검증이 필요한 API이다.

API Contract에는 각 Endpoint의 Access Level을 명확히 표시해야 한다.

---

### [핵심]

- Public API는 인증 없이 접근 가능하다.
- Protected API는 Authentication이 필요하다.
- Admin API는 강한 Authorization이 필요하다.
- User-specific API는 Self 또는 Ownership 검증이 필요하다.
- Access Level은 OpenAPI 문서에 표시해야 한다.
- Security Config와 API Contract가 일치해야 한다.

---

### [실무]

Public API 예시:

```text
GET /api/v1/festivals
GET /api/v1/festivals/{festivalId}
GET /api/v1/calendar/monthly
```

Protected API 예시:

```text
GET /api/v1/users/me
POST /api/v1/reviews
POST /api/v1/favorites
GET /api/v1/notifications
```

Admin API 예시:

```text
POST /api/v1/admin/festivals
DELETE /api/v1/admin/users/{userId}
```

Spring Security 설정은 API Contract와 일치해야 한다.

```java
.requestMatchers(HttpMethod.GET, "/api/v1/festivals/**").permitAll()
.requestMatchers("/api/v1/admin/**").hasRole("ADMIN")
.anyRequest().authenticated()
```

---

### [FAQ]

Q. Public API란 무엇인가?

A. 인증 없이 접근 가능한 API이다.

Q. Protected API란 무엇인가?

A. 인증 또는 권한 검증이 필요한 API이다.

Q. API Contract에 Access Level을 적어야 하는 이유는 무엇인가?

A. Security Config, Frontend 인증 처리, API 테스트 기준을 일치시키기 위해서이다.

---

# 14. Rate Limiting

## 14.1 Rate Limiting

### [개념]

Rate Limiting은 일정 시간 동안 허용되는 API 요청 수를 제한하는 API 보호 기법이다.

Rate Limiting은 Abuse Prevention, Brute Force 방어, 과금 보호, 서버 안정성 확보에 사용한다.

```text
Client
→ Request
→ Rate Limit Check
→ Allow or 429 Too Many Requests
```

---

### [핵심]

- Rate Limiting은 과도한 요청을 방지한다.
- 인증 API, 검색 API, 결제 API, 외부 API Proxy에 중요하다.
- IP 기준, User 기준, Token 기준 제한을 사용할 수 있다.
- 초과 시 429 Too Many Requests를 반환한다.
- Rate Limit 응답에는 재시도 가능 시간을 포함할 수 있다.
- Redis를 사용해 분산 Rate Limiting을 구현할 수 있다.
- Rate Limiting은 Duplicate Request Handling과 다르다.

---

### [실무]

Rate Limit 적용 대상:

- Login API
- Signup API
- Password Reset API
- Email Verification API
- Search API
- Payment Confirm API
- AI Recommendation API
- External API Proxy
- File Upload API
- Admin Batch API

429 응답 예시:

```json
{
  "code": "RATE_LIMIT_EXCEEDED",
  "message": "Too many requests"
}
```

Header 예시:

```http
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 0
Retry-After: 60
```

Rate Limiting 기준 예시:

| 기준           | 설명                       |
| -------------- | -------------------------- |
| IP Based       | 비로그인 요청 제한         |
| User Based     | 로그인 사용자별 요청 제한  |
| Token Based    | API Token 기준 제한        |
| Endpoint Based | 특정 고위험 API별 제한     |
| Global Limit   | 전체 서비스 보호 목적 제한 |

---

### [주의]

- Rate Limit 초과를 400이나 403으로 처리하지 않는다.
- 429 Too Many Requests를 사용한다.
- Login API는 Brute Force 방어 목적의 Rate Limiting이 중요하다.
- AI API, 외부 API Proxy는 비용 보호 목적의 Rate Limiting이 중요하다.
- `Retry-After` Header를 제공하면 Client 재시도 제어가 쉬워진다.
- Rate Limit 신규 적용은 기존 Client 호출 패턴에 Breaking Change가 될 수 있다.

---

### [FAQ]

Q. Rate Limiting이란 무엇인가?

A. 일정 시간 동안 허용되는 API 요청 수를 제한하는 API 보호 기법이다.

Q. Rate Limit 초과 시 어떤 Status Code를 사용하는가?

A. 429 Too Many Requests를 사용한다.

Q. Rate Limiting은 어떤 API에 중요한가?

A. 로그인, 회원가입, 비밀번호 재설정, 검색, 결제, AI 추천, 외부 API Proxy에 중요하다.

---

# 15. Rate Limit Error Contract

## 15.1 429 Too Many Requests

### [개념]

429 Too Many Requests는 Client가 정해진 요청 한도를 초과했을 때 반환하는 HTTP Status Code이다.

429는 Rate Limiting, Abuse Prevention, Brute Force 방어, 외부 API 비용 보호와 연결된다.

```text
Too many requests
→ 429 Too Many Requests
→ RATE_LIMIT_EXCEEDED
```

---

### [핵심]

- 429는 Rate Limit 초과 응답이다.
- Error Code는 `RATE_LIMIT_EXCEEDED`를 사용할 수 있다.
- `Retry-After` Header를 포함할 수 있다.
- Client는 429 응답을 받으면 즉시 반복 요청하지 않아야 한다.
- Frontend는 사용자에게 잠시 후 재시도 안내를 표시할 수 있다.
- 429는 Status Code / Error Response / Security Contract에 함께 문서화해야 한다.

---

### [실무]

429 Error Response:

```json
{
  "code": "RATE_LIMIT_EXCEEDED",
  "message": "Too many requests"
}
```

429 Response Header:

```http
HTTP/1.1 429 Too Many Requests
Retry-After: 60
X-RateLimit-Limit: 10
X-RateLimit-Remaining: 0
```

Frontend 처리 기준:

```text
429 RATE_LIMIT_EXCEEDED
→ Disable retry button temporarily
→ Show retry-after message
→ Avoid automatic immediate retry loop
```

API 문서화 기준:

| 항목          | 값                                             |
| ------------- | ---------------------------------------------- |
| Status Code   | 429 Too Many Requests                          |
| Error Code    | RATE_LIMIT_EXCEEDED                            |
| Header        | Retry-After                                    |
| Client Action | Delay retry                                    |
| Target API    | Login, Search, AI, Payment, External API Proxy |

---

### [FAQ]

Q. 429 Too Many Requests는 언제 사용하는가?

A. Client가 정해진 요청 한도를 초과했을 때 사용한다.

Q. 429 응답에 어떤 Header를 포함할 수 있는가?

A. `Retry-After`, `X-RateLimit-Limit`, `X-RateLimit-Remaining` 등을 포함할 수 있다.

Q. 429와 409의 차이는 무엇인가?

A. 429는 요청량 초과이고 409는 Resource 상태 또는 Business Rule 충돌이다.

---

# 16. Security Contract Documentation

## 16.1 Security API Contract

### [개념]

Security Contract는 API별 인증 필요 여부, 권한 조건, Token 전달 방식, Rate Limiting, 실패 응답을 정의하는 문서 규칙이다.

Security Contract는 Backend Security Config, Frontend Axios Interceptor, OpenAPI 문서와 일치해야 한다.

---

### [핵심]

- 인증 필요 여부를 API마다 명시한다.
- 권한 Role 또는 Ownership 조건을 명시한다.
- Token 전달 방식을 명시한다.
- 인증 실패 401 응답을 명시한다.
- 권한 실패 403 응답을 명시한다.
- Rate Limit 초과 429 응답을 명시한다.
- OpenAPI Security Scheme을 정의한다.
- Public / Protected / Admin API를 구분한다.

---

### [실무]

API Security Contract 예시:

| API                                 | Access Level | Auth Header  | Rate Limit   | Error         |
| ----------------------------------- | ------------ | ------------ | ------------ | ------------- |
| GET /api/v1/festivals               | Public       | None         | Optional     | None          |
| GET /api/v1/users/me                | Protected    | Bearer Token | User Based   | 401           |
| POST /api/v1/reviews                | Protected    | Bearer Token | User Based   | 401, 403      |
| POST /api/v1/auth/login             | Public       | None         | IP Based     | 400, 401, 429 |
| DELETE /api/v1/admin/users/{userId} | Admin        | Bearer Token | Admin Policy | 401, 403      |

OpenAPI Security Scheme 예시:

```text
type: http
scheme: bearer
bearerFormat: JWT
```

---

### [Best Practice]

- Public API와 Protected API를 문서에서 분리한다.
- Security Config와 API 문서를 함께 검수한다.
- Axios Interceptor의 Token 전달 방식과 API 문서를 일치시킨다.
- Error Response Schema를 인증/권한/Rate Limit 실패에도 동일하게 적용한다.
- 관리자 API는 URI 또는 Tag로 명확히 구분한다.
- Rate Limiting 대상 API는 429 Error Contract를 문서화한다.

---

### [FAQ]

Q. Security Contract란 무엇인가?

A. API별 인증 필요 여부, 권한 조건, Token 전달 방식, Rate Limiting, 실패 응답을 정의하는 문서 규칙이다.

Q. Security Contract가 중요한 이유는 무엇인가?

A. Security Config, Frontend 인증 처리, OpenAPI 문서, API 테스트를 일치시키기 위해서이다.

Q. 인증 실패, 권한 실패, 요청량 초과 응답은 어떻게 구분하는가?

A. 인증 실패는 401, 권한 실패는 403, 요청량 초과는 429를 사용한다.

---

# 17. Common Mistakes

## 17.1 Versioning Idempotency Security Mistakes

### [Troubleshooting]

문제: Response Field 이름을 변경했는데 Frontend 화면이 깨진다.

원인: Breaking Change를 Versioning 없이 배포했다.

해결: Field 이름 변경은 Breaking Change로 판단하고 Versioning, Deprecated, Migration을 적용한다.

---

문제: v1과 v2 DTO가 섞여 응답 구조가 불안정하다.

원인: Version별 DTO와 Controller 분리가 부족하다.

해결: Version Package, Controller, DTO를 명확히 분리한다.

---

문제: 같은 결제 요청이 두 번 승인된다.

원인: POST 결제 API에 Idempotency 처리가 없다.

해결: Idempotency Key, 결제 상태 검증, Unique Constraint를 적용한다.

---

문제: 좋아요가 중복 등록된다.

원인: Business Validation과 DB Unique Constraint가 없다.

해결: `existsByUserIdAndFestivalId` 검증과 `UNIQUE(user_id, festival_id)` 제약을 적용한다.

---

문제: 인증 실패와 권한 실패를 모두 403으로 처리한다.

원인: Authentication과 Authorization 구분이 없다.

해결: 인증 실패는 401, 권한 실패는 403으로 분리한다.

---

문제: User ID를 Request Body로 받아 본인 여부를 판단한다.

원인: 인증된 사용자 Context를 신뢰하지 않고 Client 입력을 신뢰했다.

해결: 현재 사용자 ID는 SecurityContext에서 가져오고 Request Body의 userId는 신뢰하지 않는다.

---

문제: Public API가 Security Config에서 차단된다.

원인: API Contract와 Security Config가 일치하지 않는다.

해결: Public / Protected / Admin API 목록을 문서화하고 Security Config와 비교 검수한다.

---

문제: Login API가 무차별 대입 공격에 노출된다.

원인: Rate Limiting이 적용되지 않았다.

해결: IP 또는 User 기준 Rate Limiting을 적용하고 초과 시 429 Too Many Requests를 반환한다.

---

문제: Rate Limit 초과를 403 Forbidden으로 처리한다.

원인: Authorization 실패와 요청량 초과를 혼동했다.

해결: 권한 실패는 403, 요청량 초과는 429 Too Many Requests로 분리한다.

---

문제: AI 추천 API 또는 외부 API Proxy 비용이 급증한다.

원인: Rate Limiting과 Quota 정책이 없다.

해결: User Based Rate Limit, Daily Quota, 429 Error Contract, Monitoring을 적용한다.

---

문제: Access Token을 Query Parameter로 전달한다.

원인: Token 전달 방식 Contract가 잘못 설계되었다.

해결: `Authorization: Bearer access-token` Header를 사용한다.

---

문제: API 문서에 인증 필요 여부가 없다.

원인: Security Contract가 OpenAPI 문서에 반영되지 않았다.

해결: OpenAPI Security Scheme과 Endpoint별 Security Requirement를 작성한다.

---

### [FAQ]

Q. Versioning에서 가장 흔한 실수는 무엇인가?

A. Breaking Change를 Versioning 없이 배포하거나 v1/v2 DTO를 섞는 것이다.

Q. Idempotency에서 가장 흔한 실수는 무엇인가?

A. 결제, 주문, 예약, 좋아요 같은 중복 위험 API에 중복 요청 처리를 하지 않는 것이다.

Q. Authentication에서 가장 흔한 실수는 무엇인가?

A. Token을 Query Parameter로 전달하거나 인증 실패를 403으로 처리하는 것이다.

Q. Authorization에서 가장 흔한 실수는 무엇인가?

A. 인증만 확인하고 Resource Ownership 검증을 누락하는 것이다.

Q. Rate Limiting에서 가장 흔한 실수는 무엇인가?

A. Login, Password Reset, Email Verification, AI API, External API Proxy 같은 공격·비용 대상 API에 요청 제한을 두지 않는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. API Versioning이란 무엇인가?
A. API Contract 변경을 안전하게 관리하기 위해 API 버전을 구분하는 설계 방식이다.

Q. API Versioning은 언제 필요한가?
A. 기존 Client를 깨뜨릴 수 있는 Breaking Change가 발생할 때 필요하다.

Q. URI Versioning이란 무엇인가?
A. API 버전을 URI Path에 포함하는 방식이다.

Q. URI Versioning 예시는 무엇인가?
A. `/api/v1/users`, `/api/v2/users` 같은 형태이다.

Q. Header Versioning이란 무엇인가?
A. API 버전을 Request Header에 담아 전달하는 방식이다.

Q. Breaking Change란 무엇인가?
A. 기존 Client가 더 이상 정상 동작하지 않게 만드는 API Contract 변경이다.

Q. Breaking Change 예시는 무엇인가?
A. Response Field 삭제, Field 이름 변경, Field Type 변경, Required Request Field 추가, Error Code 변경이다.

Q. Backward Compatibility란 무엇인가?
A. API 변경 후에도 기존 Client가 정상 동작하도록 기존 Contract를 유지하는 원칙이다.

Q. Idempotency란 무엇인가?
A. 같은 요청을 여러 번 보내도 최종 결과가 동일한 성질이다.

Q. POST는 Idempotent한가?
A. 기본적으로 Idempotent하지 않다.

Q. Idempotency Key란 무엇인가?
A. 중복 요청을 식별하기 위해 Client가 보내는 고유한 Key이다.

Q. Idempotency Key는 어디에 담는가?
A. 보통 `Idempotency-Key` Request Header에 담는다.

Q. 같은 Idempotency Key로 다른 Body가 오면 어떻게 처리하는가?
A. 보통 409 Conflict로 처리한다.

Q. 중복 요청은 어떻게 방지하는가?
A. Idempotency Key, Unique Constraint, Business Validation으로 방지한다.

Q. Duplicate Request Handling과 Rate Limiting의 차이는 무엇인가?
A. Duplicate Request Handling은 같은 요청의 중복 처리를 막고 Rate Limiting은 과도한 요청량을 제한한다.

Q. Authentication이란 무엇인가?
A. 사용자가 누구인지 확인하는 과정이다.

Q. Authorization이란 무엇인가?
A. 인증된 사용자가 특정 Resource 또는 Action에 접근할 권한이 있는지 확인하는 과정이다.

Q. Authentication과 Authorization의 차이는 무엇인가?
A. Authentication은 신원 확인이고 Authorization은 권한 확인이다.

Q. 인증 실패는 어떤 Status Code를 사용하는가?
A. 401 Unauthorized를 사용한다.

Q. 권한 실패는 어떤 Status Code를 사용하는가?
A. 403 Forbidden을 사용한다.

Q. 요청량 초과는 어떤 Status Code를 사용하는가?
A. 429 Too Many Requests를 사용한다.

Q. JWT는 API 요청에서 어디에 담는가?
A. `Authorization: Bearer access-token` Header에 담는다.

Q. Access Token은 무엇인가?
A. 인증된 사용자가 API에 접근할 때 사용하는 짧은 수명의 인증 Token이다.

Q. Access Token 검증 항목은 무엇인가?
A. Signature, Expiration, Issuer, Subject, Role, Token Type 등을 검증한다.

Q. Access Token에 민감 정보를 넣어도 되는가?
A. 안 된다. JWT Payload는 노출될 수 있다.

Q. Role과 Permission의 차이는 무엇인가?
A. Role은 사용자 그룹 권한이고 Permission은 기능 단위 세부 권한이다.

Q. Ownership 검증은 무엇인가?
A. 현재 사용자가 해당 Resource의 소유자인지 확인하는 권한 검증이다.

Q. 현재 사용자 ID는 어디에서 가져와야 하는가?
A. Request Body가 아니라 인증된 SecurityContext에서 가져와야 한다.

Q. Public API란 무엇인가?
A. 인증 없이 접근 가능한 API이다.

Q. Protected API란 무엇인가?
A. 인증 또는 권한 검증이 필요한 API이다.

Q. Rate Limiting이란 무엇인가?
A. 일정 시간 동안 허용되는 API 요청 수를 제한하는 API 보호 기법이다.

Q. Rate Limit 초과 시 어떤 Status Code를 사용하는가?
A. 429 Too Many Requests를 사용한다.

Q. Rate Limiting Error Code는 무엇을 사용할 수 있는가?
A. `RATE_LIMIT_EXCEEDED`를 사용할 수 있다.

Q. 429 응답에는 어떤 Header를 포함할 수 있는가?
A. `Retry-After`, `X-RateLimit-Limit`, `X-RateLimit-Remaining` 등을 포함할 수 있다.

Q. 429와 409의 차이는 무엇인가?
A. 429는 요청량 초과이고 409는 Resource 상태 또는 Business Rule 충돌이다.

Q. Rate Limiting은 어떤 API에 중요한가?
A. 로그인, 회원가입, 비밀번호 재설정, 검색, 결제, AI 추천, 외부 API Proxy에 중요하다.

Q. Security Contract란 무엇인가?
A. API별 인증 필요 여부, 권한 조건, Token 전달 방식, Rate Limiting, 실패 응답을 정의하는 문서 규칙이다.

Q. Security Contract가 중요한 이유는 무엇인가?
A. Security Config, Frontend 인증 처리, OpenAPI 문서, API 테스트를 일치시키기 위해서이다.

Q. 인증 실패, 권한 실패, 요청량 초과 응답은 어떻게 구분하는가?
A. 인증 실패는 401, 권한 실패는 403, 요청량 초과는 429를 사용한다.
