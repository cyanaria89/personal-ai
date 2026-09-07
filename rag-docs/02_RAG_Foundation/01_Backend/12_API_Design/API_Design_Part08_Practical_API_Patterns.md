# API Design Part 08 - Practical API Patterns & Endpoint Design Templates

---

# 1. Practical API Pattern

## 1.1 API Pattern Purpose

### [개념]

Practical API Pattern은 반복적으로 사용되는 API 설계 구조를 표준 Template으로 정리한 것이다.

API Pattern은 PM Agent, Backend Agent, Review Agent가 기능 요구사항을 빠르게 Endpoint, Request, Response, Error Contract로 변환하도록 돕는다.

```text
Feature Requirement
→ API Pattern
→ Endpoint
→ Request Contract
→ Response Contract
→ Error Contract
```

---

### [핵심]

- API Pattern은 반복 설계를 줄인다.
- API Pattern은 Endpoint 품질을 일정하게 만든다.
- API Pattern은 CRUD, Search, Action, Ownership, Pagination 구조를 표준화한다.
- API Pattern은 Agent Code Generation 정확도를 높인다.
- API Pattern은 API Review 기준으로 재사용된다.
- API Pattern은 프로젝트 Convention과 함께 관리해야 한다.
- API Pattern은 Security, Error Response, Test Case와 함께 사용해야 한다.

---

### [실무]

2026 실무 기준 Backend API는 기능별로 완전히 새로 설계하기보다 검증된 API Pattern을 조합해 만든다.

대표 Pattern:

- Collection 조회 Pattern
- Detail 조회 Pattern
- Create Pattern
- Update Pattern
- Delete Pattern
- Search Pattern
- Toggle Pattern
- Ownership Pattern
- Admin Pattern
- Command Pattern
- File Upload Pattern
- Batch Pattern
- External API Proxy Pattern

API Pattern은 다음 항목을 포함해야 한다.

| 항목         | 설명                                       |
| ------------ | ------------------------------------------ |
| URI          | Resource 경로                              |
| Method       | HTTP Method                                |
| Access Level | Public / Protected / Admin                 |
| Request      | Header, Path, Query, Body                  |
| Response     | Success Response DTO                       |
| Error        | Error Code, Status Code                    |
| Validation   | Request Validation                         |
| Security     | Authentication / Authorization / Ownership |
| Review Point | Agent 검수 포인트                          |

---

### [FAQ]

Q. Practical API Pattern이란 무엇인가?

A. 반복적으로 사용되는 API 설계 구조를 표준 Template으로 정리한 것이다.

Q. API Pattern이 필요한 이유는 무엇인가?

A. API 설계 품질을 일정하게 유지하고 Agent가 Endpoint를 빠르게 생성·검수하기 위해 필요하다.

Q. API Pattern은 어디에 사용하는가?

A. CRUD, Search, Toggle, Ownership, Admin, File Upload, Batch, Command API 설계에 사용한다.

---

# 2. Collection Query Pattern

## 2.1 List API Pattern

### [개념]

Collection Query Pattern은 Resource 목록을 조회하는 API Pattern이다.

목록 조회 API는 Pagination, Filtering, Sorting을 기본 검토해야 한다.

```text
GET /api/v1/resources?page=0&size=20&sort=createdAt,desc
```

---

### [핵심]

- 목록 조회는 GET을 사용한다.
- Collection Resource는 복수형 URI를 사용한다.
- Pagination을 기본 검토한다.
- Filtering 조건은 Query Parameter로 전달한다.
- Sorting 조건은 Query Parameter로 전달한다.
- Response에는 content와 metadata를 포함할 수 있다.
- 목록 API는 대량 데이터 증가를 전제로 설계한다.

---

### [실무]

Endpoint Template:

```text
GET /api/v1/{resources}
```

Request Query Template:

```text
?page=0&size=20&sort=createdAt,desc
```

Spring Boot Controller Template:

```java
@GetMapping("/resources")
public ApiResponse<Page<ResourceSummaryResponse>> getResources(
        @ModelAttribute ResourceSearchRequest request,
        @PageableDefault(size = 20, sort = "createdAt", direction = Sort.Direction.DESC)
        Pageable pageable
) {
    return ApiResponse.success(resourceService.getResources(request, pageable));
}
```

Response Template:

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

### [Review Point]

- 목록 API에 Pagination이 있는가?
- 기본 Sort 기준이 있는가?
- size 최대값 제한이 있는가?
- Filter Parameter 이름이 일관적인가?
- Response DTO가 Summary Response인가?
- Entity를 직접 반환하지 않는가?
- Count Query 비용이 큰 경우 Slice 또는 Cursor를 고려했는가?

---

### [FAQ]

Q. Collection Query Pattern은 언제 사용하는가?

A. Resource 목록을 조회할 때 사용한다.

Q. 목록 API에는 Pagination이 필요한가?

A. 데이터가 증가할 수 있다면 기본적으로 필요하다.

Q. 목록 Response는 Detail Response를 써도 되는가?

A. 권장하지 않는다. 목록에는 필요한 Field만 포함한 Summary Response를 사용하는 것이 좋다.

---

# 3. Detail Query Pattern

## 3.1 Detail API Pattern

### [개념]

Detail Query Pattern은 특정 Resource의 상세 정보를 조회하는 API Pattern이다.

Detail API는 Path Variable로 Resource Identifier를 받고 Detail Response DTO를 반환한다.

```text
GET /api/v1/resources/{resourceId}
```

---

### [핵심]

- 단건 조회는 GET을 사용한다.
- Resource Identifier는 Path Variable로 전달한다.
- Path Variable 이름은 구체적으로 작성한다.
- 존재하지 않는 Resource는 404 Not Found를 반환한다.
- Detail Response DTO는 상세 화면에 필요한 Field를 포함한다.
- 인증 또는 권한이 필요한 Detail API는 Access Level을 명시한다.

---

### [실무]

Endpoint Template:

```text
GET /api/v1/{resources}/{resourceId}
```

Spring Boot Controller Template:

```java
@GetMapping("/resources/{resourceId}")
public ApiResponse<ResourceDetailResponse> getResource(
        @PathVariable Long resourceId
) {
    return ApiResponse.success(resourceService.getResource(resourceId));
}
```

Response Template:

```json
{
  "success": true,
  "data": {
    "resourceId": 1,
    "title": "Resource Title",
    "description": "Resource Detail",
    "createdAt": "2026-06-27T10:00:00"
  },
  "message": null
}
```

Error Template:

```json
{
  "code": "RESOURCE_NOT_FOUND",
  "message": "Resource not found"
}
```

---

### [Review Point]

- URI가 Resource 중심인가?
- Path Variable 이름이 구체적인가?
- Resource 없음이 404로 처리되는가?
- Detail Response DTO를 사용하는가?
- 민감 정보가 노출되지 않는가?
- Ownership 검증이 필요한 Resource인가?
- OpenAPI에 404 Error Response가 문서화되어 있는가?

---

### [FAQ]

Q. Detail Query Pattern은 언제 사용하는가?

A. 특정 Resource의 상세 정보를 조회할 때 사용한다.

Q. Detail API에서 Resource가 없으면 어떤 Status Code를 사용하는가?

A. 404 Not Found를 사용한다.

Q. Detail Response와 Summary Response는 분리해야 하는가?

A. 분리하는 것이 좋다. 상세 조회와 목록 조회는 필요한 Field 범위가 다르다.

---

# 4. Create Pattern

## 4.1 Create API Pattern

### [개념]

Create Pattern은 새로운 Resource를 생성하는 API Pattern이다.

Create API는 POST Method와 Request Body를 사용한다.

```text
POST /api/v1/resources
```

---

### [핵심]

- 생성 API는 POST를 사용한다.
- Request Body는 Create Request DTO로 받는다.
- Entity를 Request Body로 직접 받지 않는다.
- Request Validation을 적용한다.
- 생성 성공은 201 Created 또는 200 OK를 사용할 수 있다.
- 중복 생성 위험이 있으면 Idempotency 또는 Unique Constraint를 고려한다.

---

### [실무]

Endpoint Template:

```text
POST /api/v1/{resources}
```

Request Template:

```json
{
  "title": "Resource Title",
  "content": "Resource Content"
}
```

Spring Boot Controller Template:

```java
@PostMapping("/resources")
public ApiResponse<ResourceResponse> createResource(
        @Valid @RequestBody ResourceCreateRequest request
) {
    return ApiResponse.success(resourceService.createResource(request));
}
```

Create Request DTO Template:

```java
public record ResourceCreateRequest(
        @NotBlank
        @Size(max = 100)
        String title,

        @NotBlank
        @Size(max = 2000)
        String content
) {
}
```

---

### [Review Point]

- POST Method를 사용하는가?
- Create Request DTO를 사용하는가?
- Entity 직접 바인딩이 없는가?
- `@Valid`가 적용되어 있는가?
- Required Field Validation이 있는가?
- 생성 성공 Status Code 정책이 명확한가?
- 중복 생성 방지 정책이 필요한가?
- 인증 필요 여부가 명확한가?

---

### [FAQ]

Q. Create Pattern은 언제 사용하는가?

A. 새로운 Resource를 생성할 때 사용한다.

Q. 생성 API는 어떤 HTTP Method를 사용하는가?

A. POST를 사용한다.

Q. 생성 API에서 Entity를 Request Body로 받아도 되는가?

A. 권장하지 않는다. Create Request DTO를 사용해야 한다.

---

# 5. Update Pattern

## 5.1 Update API Pattern

### [개념]

Update Pattern은 기존 Resource를 수정하는 API Pattern이다.

전체 수정은 PUT, 부분 수정은 PATCH를 사용한다.

```text
PUT /api/v1/resources/{resourceId}
PATCH /api/v1/resources/{resourceId}
```

---

### [핵심]

- 전체 수정은 PUT을 사용한다.
- 부분 수정은 PATCH를 사용한다.
- Resource Identifier는 Path Variable로 전달한다.
- 수정 데이터는 Update Request DTO로 전달한다.
- 수정 대상이 없으면 404 Not Found를 반환한다.
- 권한 또는 Ownership 검증이 필요할 수 있다.
- PATCH는 null 처리 정책을 명확히 해야 한다.

---

### [실무]

PUT Endpoint Template:

```text
PUT /api/v1/{resources}/{resourceId}
```

PATCH Endpoint Template:

```text
PATCH /api/v1/{resources}/{resourceId}
```

Spring Boot Controller Template:

```java
@PatchMapping("/resources/{resourceId}")
public ApiResponse<ResourceResponse> updateResource(
        @PathVariable Long resourceId,
        @Valid @RequestBody ResourceUpdateRequest request
) {
    return ApiResponse.success(resourceService.updateResource(resourceId, request));
}
```

Update Request DTO Template:

```java
public record ResourceUpdateRequest(
        @Size(max = 100)
        String title,

        @Size(max = 2000)
        String content
) {
}
```

---

### [Review Point]

- PUT과 PATCH 의미가 구분되어 있는가?
- Path Variable로 수정 대상을 식별하는가?
- Update Request DTO를 사용하는가?
- Entity 직접 수정 요청을 받지 않는가?
- Resource 없음이 404로 처리되는가?
- 작성자 또는 소유자 검증이 필요한가?
- PATCH null 처리 정책이 문서화되어 있는가?

---

### [FAQ]

Q. Update Pattern은 언제 사용하는가?

A. 기존 Resource를 수정할 때 사용한다.

Q. PUT과 PATCH의 차이는 무엇인가?

A. PUT은 전체 수정이고 PATCH는 부분 수정이다.

Q. 수정 API에서 Ownership 검증이 필요한 이유는 무엇인가?

A. 다른 사용자가 소유하지 않은 Resource를 수정하지 못하게 하기 위해서이다.

---

# 6. Delete Pattern

## 6.1 Delete API Pattern

### [개념]

Delete Pattern은 기존 Resource를 삭제하는 API Pattern이다.

Delete API는 DELETE Method와 Path Variable을 사용한다.

```text
DELETE /api/v1/resources/{resourceId}
```

---

### [핵심]

- 삭제 API는 DELETE를 사용한다.
- 삭제 대상은 Path Variable로 식별한다.
- 단건 삭제에서 Request Body는 사용하지 않는 것이 원칙이다.
- 삭제 성공은 204 No Content 또는 200 OK를 사용할 수 있다.
- 삭제 대상이 없으면 404 Not Found를 반환한다.
- 삭제 권한 또는 Ownership 검증이 필요하다.
- Soft Delete와 Hard Delete 정책을 구분한다.

---

### [실무]

Endpoint Template:

```text
DELETE /api/v1/{resources}/{resourceId}
```

Spring Boot Controller Template:

```java
@DeleteMapping("/resources/{resourceId}")
public ApiResponse<Void> deleteResource(
        @PathVariable Long resourceId
) {
    resourceService.deleteResource(resourceId);
    return ApiResponse.success();
}
```

Error Mapping:

```text
RESOURCE_NOT_FOUND → 404 Not Found
ACCESS_DENIED → 403 Forbidden
DELETE_CONFLICT → 409 Conflict
```

---

### [Review Point]

- DELETE Method를 사용하는가?
- 삭제 대상을 Path Variable로 식별하는가?
- Request Body에 의존하지 않는가?
- 삭제 성공 Status Code 정책이 명확한가?
- Resource 없음이 404로 처리되는가?
- Ownership 또는 Admin 권한 검증이 있는가?
- Soft Delete 정책이 필요한가?
- Batch Delete와 단건 Delete를 구분했는가?

---

### [FAQ]

Q. Delete Pattern은 언제 사용하는가?

A. 기존 Resource를 삭제할 때 사용한다.

Q. 삭제 성공 시 어떤 Status Code를 사용하는가?

A. Response Body가 없으면 204 No Content, 공통 Response Wrapper가 필요하면 200 OK를 사용할 수 있다.

Q. Soft Delete도 DELETE Method를 사용하는가?

A. 외부 API 의미가 삭제라면 내부 구현이 Soft Delete여도 DELETE Method를 사용할 수 있다.

---

# 7. Search Pattern

## 7.1 Search API Pattern

### [개념]

Search Pattern은 Keyword와 Filter 조건을 기반으로 Resource를 검색하는 API Pattern이다.

Search API는 Pagination, Filtering, Sorting과 함께 설계한다.

```text
GET /api/v1/resources/search?keyword=test&page=0&size=20
```

---

### [핵심]

- Search API는 GET을 기본으로 사용한다.
- 검색어는 `keyword` 또는 `q`로 통일한다.
- 복합 검색 조건은 Search Request DTO로 묶는다.
- Search Result는 Pagination을 적용한다.
- 검색어 길이 제한을 고려한다.
- 검색 대상 Field를 문서화한다.
- 복잡한 검색은 Search 전용 Endpoint를 둘 수 있다.
- 검색 API는 Rate Limiting 또는 Debounce를 고려할 수 있다.

---

### [실무]

Endpoint Template:

```text
GET /api/v1/{resources}/search
```

Query Template:

```text
?keyword=music&region=seoul&page=0&size=20&sort=createdAt,desc
```

Search Request DTO Template:

```java
public record ResourceSearchRequest(
        String keyword,
        String category,
        LocalDate startDate,
        LocalDate endDate
) {
}
```

Controller Template:

```java
@GetMapping("/resources/search")
public ApiResponse<Page<ResourceSummaryResponse>> searchResources(
        @ModelAttribute ResourceSearchRequest request,
        Pageable pageable
) {
    return ApiResponse.success(resourceService.searchResources(request, pageable));
}
```

---

### [Review Point]

- Search와 Filter 조건이 명확히 구분되는가?
- 검색어 Parameter 이름이 통일되어 있는가?
- Search Result에 Pagination이 적용되어 있는가?
- 검색어 Validation 또는 길이 제한이 있는가?
- 기본 Sort 기준이 있는가?
- Search DTO가 필요한 수준인가?
- Query 성능과 Index를 고려했는가?
- 과도한 요청 방지를 위한 Rate Limiting 또는 Frontend Debounce가 필요한가?

---

### [FAQ]

Q. Search Pattern은 언제 사용하는가?

A. Keyword와 조건을 기반으로 Resource를 검색할 때 사용한다.

Q. Search API에도 Pagination이 필요한가?

A. 필요하다. 검색 결과가 많아질 수 있기 때문이다.

Q. 검색어 Parameter 이름은 무엇을 사용하는가?

A. `keyword` 또는 `q` 중 하나로 프로젝트 전체에서 통일한다.

---

# 8. Toggle Pattern

## 8.1 Like Favorite Toggle Pattern

### [개념]

Toggle Pattern은 좋아요, 즐겨찾기, 팔로우처럼 등록과 취소가 반복되는 사용자 액션 API Pattern이다.

Toggle API는 명확한 등록 / 취소 Endpoint로 분리하거나 하나의 Toggle Endpoint로 처리할 수 있다.

```text
POST /api/v1/festivals/{festivalId}/likes
DELETE /api/v1/festivals/{festivalId}/likes
```

---

### [핵심]

- Toggle 대상은 Resource와 User 관계이다.
- 등록은 POST를 사용할 수 있다.
- 취소는 DELETE를 사용할 수 있다.
- 중복 등록은 409 Conflict 또는 Idempotent Success로 처리할 수 있다.
- 취소 대상이 없을 때 404 또는 Idempotent Success 정책을 정한다.
- 인증이 필요하다.
- 현재 사용자 ID는 SecurityContext에서 가져온다.
- Unique Constraint로 동시성 중복 등록을 방지한다.

---

### [실무]

명시적 등록 / 취소 Pattern:

```text
POST /api/v1/festivals/{festivalId}/likes
DELETE /api/v1/festivals/{festivalId}/likes

POST /api/v1/festivals/{festivalId}/favorites
DELETE /api/v1/festivals/{festivalId}/favorites
```

Controller Template:

```java
@PostMapping("/festivals/{festivalId}/likes")
public ApiResponse<Void> likeFestival(
        @PathVariable Long festivalId,
        @AuthenticationPrincipal CustomUserPrincipal principal
) {
    festivalLikeService.like(principal.userId(), festivalId);
    return ApiResponse.success();
}
```

중복 방지 DB Constraint:

```text
UNIQUE(user_id, festival_id)
```

---

### [주의]

- Request Body로 userId를 받지 않는다.
- 중복 등록 처리 정책을 명확히 한다.
- 등록 / 취소 API를 하나의 POST `/toggle`로 만들 경우 상태 예측성이 낮아질 수 있다.
- 좋아요 수 증가 / 감소는 Transaction 안에서 처리한다.
- 동시성 상황에서 Unique Constraint가 필요하다.
- Toggle API는 Idempotency 정책을 문서화해야 한다.

---

### [FAQ]

Q. Toggle Pattern은 언제 사용하는가?

A. 좋아요, 즐겨찾기, 팔로우처럼 사용자와 Resource의 관계를 등록·취소할 때 사용한다.

Q. 좋아요 등록과 취소는 어떻게 설계하는가?

A. `POST /resources/{id}/likes`, `DELETE /resources/{id}/likes`처럼 분리할 수 있다.

Q. Toggle API에서 userId를 Body로 받아도 되는가?

A. 안 된다. 현재 사용자 ID는 SecurityContext에서 가져와야 한다.

---

# 9. Ownership Pattern

## 9.1 User Owned Resource Pattern

### [개념]

Ownership Pattern은 사용자가 소유한 Resource를 조회, 수정, 삭제할 때 현재 사용자와 Resource Owner를 검증하는 API Pattern이다.

Ownership 검증은 Authorization의 핵심이다.

```text
Authenticated User
→ Load Resource
→ Compare ownerId
→ Allow or Deny
```

---

### [핵심]

- Ownership은 Resource 소유자 검증이다.
- 수정 / 삭제 API에서 자주 필요하다.
- 현재 사용자 ID는 SecurityContext에서 가져온다.
- Resource Owner ID와 현재 사용자 ID를 비교한다.
- Ownership 실패는 403 Forbidden을 사용한다.
- Resource 없음과 권한 없음 응답 정책을 정한다.

---

### [실무]

Ownership 대상 API:

```text
PATCH /api/v1/reviews/{reviewId}
DELETE /api/v1/reviews/{reviewId}
PATCH /api/v1/users/me
GET /api/v1/orders/{orderId}
```

Service Template:

```java
@Transactional
public ReviewResponse updateReview(
        Long currentUserId,
        Long reviewId,
        ReviewUpdateRequest request
) {
    Review review = reviewRepository.findById(reviewId)
            .orElseThrow(() -> new BusinessException(ErrorCode.REVIEW_NOT_FOUND));

    if (!review.isWrittenBy(currentUserId)) {
        throw new BusinessException(ErrorCode.ACCESS_DENIED);
    }

    review.update(request.content(), request.rating());
    return reviewMapper.toResponse(review);
}
```

Error Mapping:

```text
REVIEW_NOT_FOUND → 404 Not Found
ACCESS_DENIED → 403 Forbidden
```

---

### [Review Point]

- Ownership이 필요한 API인가?
- 현재 사용자 ID를 SecurityContext에서 가져오는가?
- Request Body의 userId를 신뢰하지 않는가?
- Resource Owner와 currentUserId를 비교하는가?
- 권한 실패가 403으로 처리되는가?
- Admin 예외 권한이 필요한가?
- Resource 없음과 권한 없음 노출 정책이 필요한가?

---

### [FAQ]

Q. Ownership Pattern은 언제 사용하는가?

A. 사용자가 소유한 Resource를 조회, 수정, 삭제할 때 사용한다.

Q. Ownership 실패는 어떤 Status Code를 사용하는가?

A. 403 Forbidden을 사용한다.

Q. 현재 사용자 ID는 어디에서 가져오는가?

A. Request Body가 아니라 SecurityContext 또는 Authentication Principal에서 가져온다.

---

# 10. Admin API Pattern

## 10.1 Admin Resource Pattern

### [개념]

Admin API Pattern은 관리자 권한이 필요한 Resource 관리 API를 설계하는 Pattern이다.

Admin API는 일반 사용자 API와 URI, Security, Response 범위를 명확히 구분해야 한다.

```text
GET /api/v1/admin/users
DELETE /api/v1/admin/users/{userId}
POST /api/v1/admin/festivals
```

---

### [핵심]

- Admin API는 ROLE_ADMIN 권한이 필요하다.
- URI에 `/admin` Prefix를 사용할 수 있다.
- 관리자 API는 일반 API보다 더 많은 Field를 반환할 수 있다.
- 관리자 API는 Audit Log를 고려한다.
- 삭제, 차단, 승인 같은 위험 Action은 권한 검증을 강화한다.
- OpenAPI 문서에서 Admin Tag로 구분한다.
- 관리자 Batch API는 Rate Limiting 또는 Audit Log를 고려한다.

---

### [실무]

Endpoint Template:

```text
GET /api/v1/admin/{resources}
POST /api/v1/admin/{resources}
PATCH /api/v1/admin/{resources}/{resourceId}
DELETE /api/v1/admin/{resources}/{resourceId}
```

Controller Template:

```java
@PreAuthorize("hasRole('ADMIN')")
@GetMapping("/admin/users")
public ApiResponse<Page<AdminUserResponse>> getUsers(
        Pageable pageable
) {
    return ApiResponse.success(adminUserService.getUsers(pageable));
}
```

Security Config Template:

```java
.requestMatchers("/api/v1/admin/**").hasRole("ADMIN")
```

---

### [Review Point]

- `/admin` Prefix가 명확한가?
- ROLE_ADMIN 검증이 있는가?
- Security Config와 Method Security가 일치하는가?
- 관리자 Response에 민감 정보가 과도하게 노출되지 않는가?
- 삭제 / 차단 / 승인 API에 Audit Log가 필요한가?
- 일반 사용자 API와 DTO를 분리했는가?
- OpenAPI에서 Admin API가 구분되는가?

---

### [FAQ]

Q. Admin API Pattern은 언제 사용하는가?

A. 관리자 권한으로 Resource를 관리하는 API를 설계할 때 사용한다.

Q. Admin API는 URI를 어떻게 구분하는가?

A. 보통 `/api/v1/admin/**` Prefix를 사용한다.

Q. Admin API에서 가장 중요한 검수 항목은 무엇인가?

A. ROLE_ADMIN 권한 검증과 민감 정보 노출 방지이다.

---

# 11. Command API Pattern

## 11.1 Domain Command Pattern

### [개념]

Command API Pattern은 단순 CRUD가 아니라 Domain Action을 실행하는 API Pattern이다.

결제 승인, 주문 취소, 비밀번호 재설정, 이메일 인증, Batch Delete 같은 API가 Command API에 해당할 수 있다.

```text
POST /api/v1/payments/{paymentId}/confirm
POST /api/v1/orders/{orderId}/cancel
POST /api/v1/users/password-reset
POST /api/v1/resources/batch-delete
```

---

### [핵심]

- Command API는 POST를 주로 사용한다.
- URI에 Action이 포함될 수 있다.
- Action 이름은 Domain 의미가 명확해야 한다.
- Command API는 중복 요청 처리와 Idempotency가 중요하다.
- Command API는 상태 전이 Validation이 필요하다.
- Command API는 Error Code를 명확히 정의해야 한다.
- REST Resource 표현이 애매한 대량 처리나 복합 작업에 사용할 수 있다.

---

### [실무]

Command API 예시:

```text
POST /api/v1/payments/{paymentId}/confirm
POST /api/v1/orders/{orderId}/cancel
POST /api/v1/email-verifications/confirm
POST /api/v1/password-reset-tokens/verify
POST /api/v1/resources/batch-delete
```

Controller Template:

```java
@PostMapping("/payments/{paymentId}/confirm")
public ApiResponse<PaymentConfirmResponse> confirmPayment(
        @PathVariable Long paymentId,
        @RequestHeader(value = "Idempotency-Key", required = false) String idempotencyKey,
        @Valid @RequestBody PaymentConfirmRequest request
) {
    return ApiResponse.success(paymentService.confirm(paymentId, idempotencyKey, request));
}
```

Error Mapping:

```text
PAYMENT_NOT_FOUND → 404 Not Found
PAYMENT_ALREADY_CONFIRMED → 409 Conflict
INVALID_PAYMENT_STATUS → 409 Conflict
PAYMENT_PROVIDER_ERROR → 502 Bad Gateway or 500 Internal Server Error
RATE_LIMIT_EXCEEDED → 429 Too Many Requests
```

---

### [Review Point]

- Command가 단순 CRUD로 표현하기 어려운가?
- POST Method 사용이 적절한가?
- Action URI가 명확한 Domain 용어인가?
- 상태 전이 Validation이 있는가?
- 중복 요청 처리 정책이 있는가?
- Idempotency Key가 필요한가?
- Error Code가 상태별로 정의되어 있는가?
- Rate Limiting이 필요한 Command인가?

---

### [FAQ]

Q. Command API Pattern은 언제 사용하는가?

A. 결제 승인, 주문 취소, 이메일 인증처럼 단순 CRUD가 아닌 Domain Action을 실행할 때 사용한다.

Q. Command API에 POST를 사용하는 이유는 무엇인가?

A. 서버 상태를 변경하거나 Domain Action을 실행하기 때문이다.

Q. Command API에서 중요한 것은 무엇인가?

A. 상태 전이 Validation, Idempotency, Error Code 정의이다.

---

# 12. File Upload API Pattern

## 12.1 Multipart Upload Pattern

### [개념]

File Upload API Pattern은 이미지, 문서, 첨부파일을 업로드하는 API 설계 Pattern이다.

File Upload API는 Multipart Request, File Size Limit, MIME Type Validation, Storage Policy를 명확히 정의해야 한다.

```text
POST /api/v1/files
Content-Type: multipart/form-data
```

---

### [핵심]

- 파일 업로드는 multipart/form-data를 사용한다.
- 파일 크기 제한을 정의한다.
- 허용 MIME Type을 정의한다.
- 허용 확장자를 정의한다.
- 저장 위치와 접근 URL 정책을 정의한다.
- 인증 필요 여부를 명시한다.
- 악성 파일 업로드 방지를 고려한다.
- 파일 업로드 API는 Rate Limiting을 고려할 수 있다.

---

### [실무]

Endpoint Template:

```text
POST /api/v1/files
POST /api/v1/users/me/profile-image
POST /api/v1/reviews/{reviewId}/images
```

Controller Template:

```java
@PostMapping(value = "/files", consumes = MediaType.MULTIPART_FORM_DATA_VALUE)
public ApiResponse<FileUploadResponse> uploadFile(
        @RequestPart MultipartFile file
) {
    return ApiResponse.success(fileService.upload(file));
}
```

Response Template:

```json
{
  "success": true,
  "data": {
    "fileId": 1,
    "fileUrl": "https://cdn.example.com/files/image.jpg",
    "originalName": "image.jpg",
    "contentType": "image/jpeg",
    "size": 102400
  },
  "message": null
}
```

---

### [주의]

- 파일명을 그대로 저장 경로로 사용하지 않는다.
- 확장자만 믿지 말고 MIME Type을 검증한다.
- 업로드 용량 제한을 둔다.
- 실행 가능한 파일 업로드를 제한한다.
- Public URL과 Private File Access 정책을 구분한다.
- 이미지 파일은 필요 시 리사이징 또는 메타데이터 제거를 고려한다.
- 업로드 남용 방지를 위해 Rate Limit과 사용자별 저장 용량 제한을 고려한다.

---

### [FAQ]

Q. File Upload API는 어떤 Content-Type을 사용하는가?

A. `multipart/form-data`를 사용한다.

Q. File Upload API에서 검증해야 할 것은 무엇인가?

A. 파일 크기, MIME Type, 확장자, 저장 경로, 접근 권한을 검증해야 한다.

Q. 파일명을 그대로 저장하면 안 되는 이유는 무엇인가?

A. 이름 충돌, 경로 조작, 보안 문제가 발생할 수 있기 때문이다.

---

# 13. Batch API Pattern

## 13.1 Batch Request Pattern

### [개념]

Batch API Pattern은 여러 Resource를 한 번의 요청으로 처리하는 API Pattern이다.

Batch API는 대량 등록, 대량 수정, 대량 삭제, 상태 일괄 변경에 사용된다.

```text
POST /api/v1/resources/batch
PATCH /api/v1/resources/batch
POST /api/v1/resources/batch-delete
```

---

### [핵심]

- Batch API는 여러 항목을 한 번에 처리한다.
- Request Body에 ID List 또는 Item List를 포함한다.
- 최대 처리 개수를 제한한다.
- 전체 성공 / 부분 성공 정책을 정해야 한다.
- 실패 항목 Error 정보를 제공할 수 있다.
- Transaction 범위를 신중히 결정해야 한다.
- 권한 검증을 항목별로 수행할 수 있다.
- Batch Delete는 DELETE Body 호환성 문제를 고려해야 한다.

---

### [실무]

Batch Delete Request 예시:

```json
{
  "resourceIds": [1, 2, 3]
}
```

호환성 주의가 필요한 설계:

```text
DELETE /api/v1/resources/batch
Body:
{
  "resourceIds": [1, 2, 3]
}
```

실무 호환성 중심 대안:

```text
POST /api/v1/resources/batch-delete
Body:
{
  "resourceIds": [1, 2, 3]
}
```

Controller Template:

```java
@PostMapping("/resources/batch-delete")
public ApiResponse<BatchResultResponse> deleteResources(
        @Valid @RequestBody BatchDeleteRequest request
) {
    return ApiResponse.success(resourceService.deleteBatch(request));
}
```

Batch Response Template:

```json
{
  "success": true,
  "data": {
    "requestedCount": 3,
    "successCount": 2,
    "failedCount": 1,
    "failures": [
      {
        "resourceId": 3,
        "code": "ACCESS_DENIED",
        "message": "Access denied"
      }
    ]
  },
  "message": null
}
```

---

### [주의]

- Batch Size 최대값을 제한한다.
- 부분 성공 허용 여부를 문서화한다.
- 실패 항목별 Error Code를 제공한다.
- Transaction을 전체 단위로 묶을지 항목 단위로 처리할지 정한다.
- 모든 항목에 대한 Authorization을 검증한다.
- Batch API는 일반 API보다 테스트 케이스가 많아야 한다.
- `DELETE + Request Body`는 일부 Client, Proxy, Gateway에서 호환성 문제가 생길 수 있다.
- Body가 필요한 Batch Delete는 POST Command API로 설계하는 방식이 더 안전할 수 있다.

---

### [FAQ]

Q. Batch API Pattern은 언제 사용하는가?

A. 여러 Resource를 한 번의 요청으로 등록, 수정, 삭제, 상태 변경할 때 사용한다.

Q. Batch API에서 중요한 정책은 무엇인가?

A. 최대 처리 개수, 부분 성공 여부, Transaction 범위, 항목별 Error Response이다.

Q. Batch API도 권한 검증이 필요한가?

A. 필요하다. 각 Resource에 대한 접근 권한을 검증해야 한다.

---

# 14. Batch Delete Compatibility

## 14.1 DELETE Body Compatibility

### [개념]

Batch Delete에서 `DELETE` 요청에 Request Body를 사용하는 방식은 일부 Client, Proxy, Gateway, 문서화 도구에서 호환성 문제가 발생할 수 있다.

HTTP 규격상 DELETE Body가 완전히 금지된 것은 아니지만, 실무에서는 처리 일관성이 낮을 수 있다.

---

### [핵심]

- `DELETE + Request Body`는 호환성 문제가 생길 수 있다.
- 일부 Client나 Proxy가 DELETE Body를 무시할 수 있다.
- OpenAPI, Gateway, CORS, Security Filter에서 예상과 다르게 동작할 수 있다.
- Batch Delete는 `POST /resources/batch-delete` 또는 `POST /resources/delete`로 설계할 수 있다.
- REST 순수성보다 안정적인 API Contract가 더 중요할 수 있다.
- 팀 Convention으로 Batch Delete 방식을 명확히 정해야 한다.

---

### [실무]

비권장 또는 주의 설계:

```text
DELETE /api/v1/resources/batch
Content-Type: application/json

{
  "resourceIds": [1, 2, 3]
}
```

권장 대안:

```text
POST /api/v1/resources/batch-delete
Content-Type: application/json

{
  "resourceIds": [1, 2, 3]
}
```

또는 Command API Pattern으로 처리한다.

```text
POST /api/v1/resources/delete
POST /api/v1/resources/bulk-delete
```

Batch 삭제는 단순 Resource 삭제라기보다 여러 Resource에 대한 Command 성격이 강하므로 POST 사용이 실무적으로 더 안전할 수 있다.

---

### [Best Practice]

- 단건 삭제는 `DELETE /resources/{resourceId}`를 사용한다.
- 여러 ID를 Body로 받아 삭제해야 하면 POST Command API를 고려한다.
- Batch API는 최대 처리 개수를 제한한다.
- 부분 성공 / 전체 실패 정책을 명확히 한다.
- 항목별 Error Response를 제공한다.
- Authorization을 항목별로 검증한다.
- Batch Delete 설계는 OpenAPI 문서와 Postman / Frontend 테스트로 검증한다.

---

### [FAQ]

Q. DELETE 요청에 Body를 넣어도 되는가?

A. 가능은 하지만 실무 호환성 문제가 생길 수 있어 주의가 필요하다.

Q. Batch Delete는 어떻게 설계하는 것이 안전한가?

A. `POST /resources/batch-delete` 같은 Command API로 설계하는 방식이 더 안전할 수 있다.

Q. 단건 삭제도 POST를 써야 하는가?

A. 아니다. 단건 Resource 삭제는 `DELETE /resources/{id}`가 적절하다.

---

# 15. External API Proxy Pattern

## 15.1 External Provider API Pattern

### [개념]

External API Proxy Pattern은 Backend가 외부 API Provider를 호출하고 그 결과를 Client에 맞는 내부 Response Contract로 변환하는 API Pattern이다.

Tour API, Kakao Map API, Payment Provider, Email API, AI API 연동에 사용된다.

```text
Frontend
→ Backend API
→ External Provider API
→ Backend Mapping
→ Internal Response DTO
```

---

### [핵심]

- Client가 Provider API Key를 직접 사용하지 않도록 한다.
- Backend가 Provider Response를 내부 DTO로 변환한다.
- Provider Error를 내부 Error Code로 Mapping한다.
- Timeout과 Retry 정책을 정의한다.
- External API 비용 보호를 위해 Rate Limiting을 고려한다.
- Provider 장애 시 Fallback 또는 사용자 안내가 필요할 수 있다.
- Provider의 민감한 Error Message를 Client에 그대로 노출하지 않는다.

---

### [실무]

Endpoint Template:

```text
GET /api/v1/external/festivals/sync
GET /api/v1/locations/coordinates?keyword=서울시 강남구
POST /api/v1/ai/recommendations
POST /api/v1/payments/confirm
```

Service Flow:

```text
Request
→ Validate Input
→ Check Rate Limit
→ Call External Provider
→ Parse Provider Response
→ Map Internal DTO
→ Handle Provider Error
→ Return ApiResponse
```

External Error Mapping:

```text
Provider Bad Response → 502 Bad Gateway
Provider Unavailable → 503 Service Unavailable
Provider Timeout → 504 Gateway Timeout
Internal Mapping Error → 500 Internal Server Error
Business Conflict → 409 Conflict
Rate Limit Exceeded → 429 Too Many Requests
```

---

### [주의]

- Provider API Key를 Frontend에 노출하지 않는다.
- Provider Response Schema 변경에 대비한다.
- Provider Timeout 설정을 반드시 둔다.
- 외부 API 호출 실패를 무조건 500으로만 처리할지 502 / 503 / 504로 구분할지 정책을 정한다.
- Payment Provider API는 Idempotency와 상태 검증을 함께 적용한다.
- AI API와 Search API는 비용 보호를 위해 Rate Limiting을 고려한다.

---

### [FAQ]

Q. External API Proxy Pattern은 언제 사용하는가?

A. Backend가 외부 API Provider를 호출하고 내부 Response DTO로 변환해야 할 때 사용한다.

Q. 외부 API Key를 Frontend에 노출해도 되는가?

A. 안 된다. Provider API Key는 Backend 또는 안전한 서버 환경에서 관리해야 한다.

Q. External API 오류는 어떻게 처리하는가?

A. Provider 오류를 내부 Error Code로 변환하고 필요 시 502, 503, 504로 구분한다.

---

# 16. API Pattern Selection Guide

## 16.1 Pattern Selection

### [개념]

API Pattern Selection Guide는 기능 요구사항에 따라 어떤 API Pattern을 적용할지 결정하는 기준이다.

Agent는 요구사항을 분석한 뒤 적절한 Pattern을 선택해야 한다.

---

### [핵심]

| 요구사항           | 추천 Pattern                            |
| ------------------ | --------------------------------------- |
| 목록 조회          | Collection Query Pattern                |
| 단건 조회          | Detail Query Pattern                    |
| 생성               | Create Pattern                          |
| 전체 수정          | PUT Update Pattern                      |
| 부분 수정          | PATCH Update Pattern                    |
| 삭제               | Delete Pattern                          |
| 검색               | Search Pattern                          |
| 좋아요 / 찜        | Toggle Pattern                          |
| 본인 Resource 수정 | Ownership Pattern                       |
| 관리자 관리        | Admin API Pattern                       |
| 결제 승인 / 취소   | Command API Pattern                     |
| 파일 업로드        | File Upload Pattern                     |
| 대량 처리          | Batch API Pattern                       |
| Batch Delete       | Command API Pattern + Batch API Pattern |
| 외부 API 호출      | External API Proxy Pattern              |

---

### [실무]

Pattern 선택 Flow:

```text
User Requirement
→ Resource 식별
→ Action 유형 판단
→ CRUD 여부 판단
→ 인증 / 권한 판단
→ 목록 여부 판단
→ 중복 요청 위험 판단
→ API Pattern 선택
→ Contract 작성
```

예시:

```text
요구사항: 사용자가 축제를 찜한다.
→ Resource: Festival, Favorite
→ Action: User Resource Relation Create
→ Auth: Required
→ Pattern: Toggle Pattern
→ API: POST /api/v1/festivals/{festivalId}/favorites
```

예시:

```text
요구사항: 관리자가 축제를 등록한다.
→ Resource: Festival
→ Action: Create
→ Auth: Admin
→ Pattern: Admin API Pattern + Create Pattern
→ API: POST /api/v1/admin/festivals
```

예시:

```text
요구사항: 여러 리뷰를 한 번에 삭제한다.
→ Resource: Review
→ Action: Batch Delete Command
→ Auth: Admin or Owner
→ Pattern: Batch API Pattern + Command API Pattern
→ API: POST /api/v1/reviews/batch-delete
```

---

### [FAQ]

Q. API Pattern은 어떻게 선택하는가?

A. Resource, Action 유형, 인증/권한, 목록 여부, 중복 요청 위험을 기준으로 선택한다.

Q. 하나의 API에 여러 Pattern을 적용할 수 있는가?

A. 가능하다. 예를 들어 관리자 생성 API는 Admin API Pattern과 Create Pattern을 함께 사용한다.

Q. 좋아요 API는 어떤 Pattern인가?

A. Toggle Pattern 또는 User Resource Relation Pattern이다.

---

# 17. Common Mistakes

## 17.1 Practical Pattern Mistakes

### [Troubleshooting]

문제: 목록 API가 Detail Response를 반환한다.

원인: Collection Query Pattern과 Detail Query Pattern을 분리하지 않았다.

해결: 목록 API는 Summary Response, 상세 API는 Detail Response를 사용한다.

---

문제: 좋아요 API가 `/likeFestival` URI를 사용한다.

원인: Toggle Action을 Resource 중심 URI로 설계하지 않았다.

해결: `POST /festivals/{festivalId}/likes`, `DELETE /festivals/{festivalId}/likes`로 설계한다.

---

문제: 수정 API에서 Request Body로 userId를 받는다.

원인: Ownership Pattern을 적용하지 않았다.

해결: currentUserId는 SecurityContext에서 가져오고 Resource Owner와 비교한다.

---

문제: 관리자 API와 일반 API가 같은 URI를 사용한다.

원인: Admin API Pattern이 적용되지 않았다.

해결: `/api/v1/admin/**` Prefix와 ROLE_ADMIN 권한을 적용한다.

---

문제: 결제 승인 API에 중복 요청 처리가 없다.

원인: Command API Pattern과 Idempotency Pattern을 함께 적용하지 않았다.

해결: Idempotency Key, Payment Status, Unique Constraint를 적용한다.

---

문제: 파일 업로드 API에 검증이 없다.

원인: File Upload Pattern의 Size, MIME Type, Extension Validation이 누락되었다.

해결: 파일 크기, MIME Type, 확장자, 저장 경로, 접근 권한을 검증한다.

---

문제: Batch API가 모든 항목 성공만 가정한다.

원인: 부분 성공 / 실패 정책을 정의하지 않았다.

해결: 전체 성공, 전체 실패, 부분 성공 정책과 항목별 Error Response를 문서화한다.

---

문제: Batch Delete API를 `DELETE + Body`로 만들었는데 일부 환경에서 Body가 전달되지 않는다.

원인: Client, Proxy, Gateway, 문서화 도구가 DELETE Request Body를 일관되게 처리하지 않았다.

해결: `POST /resources/batch-delete` 같은 Command API로 변경하거나 팀 Convention과 Gateway 설정을 명확히 검증한다.

---

문제: External API Provider 오류 메시지가 그대로 Client에 노출된다.

원인: External API Proxy Pattern에서 Error Mapping을 하지 않았다.

해결: Provider Error를 내부 Error Code로 변환하고 민감한 Provider Message를 제거한다.

---

### [FAQ]

Q. Practical API Pattern에서 가장 흔한 실수는 무엇인가?

A. 목록/상세 DTO 미분리, 동사형 URI, Ownership 누락, Admin Prefix 누락, Idempotency 누락이다.

Q. Pattern을 적용하면 무엇이 좋아지는가?

A. API 설계 일관성, 코드 생성 정확도, Review 품질, Frontend 연동 안정성이 좋아진다.

Q. Pattern 적용 후에도 Review가 필요한가?

A. 필요하다. Pattern은 설계 출발점이고 실제 API Contract와 구현 일치 여부는 별도 검수가 필요하다.

---

# Retrieval Queries

### [FAQ]

Q. Practical API Pattern이란 무엇인가?
A. 반복적으로 사용되는 API 설계 구조를 표준 Template으로 정리한 것이다.

Q. API Pattern은 왜 필요한가?
A. API 설계 품질을 일정하게 유지하고 Agent가 Endpoint를 빠르게 생성·검수하기 위해 필요하다.

Q. Collection Query Pattern은 언제 사용하는가?
A. Resource 목록을 조회할 때 사용한다.

Q. 목록 API에는 Pagination이 필요한가?
A. 데이터가 증가할 수 있다면 기본적으로 필요하다.

Q. Detail Query Pattern은 언제 사용하는가?
A. 특정 Resource의 상세 정보를 조회할 때 사용한다.

Q. Detail API에서 Resource가 없으면 어떤 Status Code를 사용하는가?
A. 404 Not Found를 사용한다.

Q. Create Pattern은 언제 사용하는가?
A. 새로운 Resource를 생성할 때 사용한다.

Q. 생성 API는 어떤 HTTP Method를 사용하는가?
A. POST를 사용한다.

Q. Update Pattern은 언제 사용하는가?
A. 기존 Resource를 수정할 때 사용한다.

Q. PUT과 PATCH의 차이는 무엇인가?
A. PUT은 전체 수정이고 PATCH는 부분 수정이다.

Q. Delete Pattern은 언제 사용하는가?
A. 기존 Resource를 삭제할 때 사용한다.

Q. 삭제 성공 시 어떤 Status Code를 사용하는가?
A. Response Body가 없으면 204 No Content, 공통 Response Wrapper가 필요하면 200 OK를 사용할 수 있다.

Q. Search Pattern은 언제 사용하는가?
A. Keyword와 조건을 기반으로 Resource를 검색할 때 사용한다.

Q. Search API에도 Pagination이 필요한가?
A. 필요하다. 검색 결과가 많아질 수 있기 때문이다.

Q. Toggle Pattern은 언제 사용하는가?
A. 좋아요, 즐겨찾기, 팔로우처럼 사용자와 Resource의 관계를 등록·취소할 때 사용한다.

Q. 좋아요 API는 어떻게 설계하는가?
A. `POST /resources/{id}/likes`, `DELETE /resources/{id}/likes`처럼 설계할 수 있다.

Q. Toggle API에서 userId를 Body로 받아도 되는가?
A. 안 된다. 현재 사용자 ID는 SecurityContext에서 가져와야 한다.

Q. Ownership Pattern은 언제 사용하는가?
A. 사용자가 소유한 Resource를 조회, 수정, 삭제할 때 사용한다.

Q. Ownership 실패는 어떤 Status Code를 사용하는가?
A. 403 Forbidden을 사용한다.

Q. Admin API Pattern은 언제 사용하는가?
A. 관리자 권한으로 Resource를 관리하는 API를 설계할 때 사용한다.

Q. Admin API는 URI를 어떻게 구분하는가?
A. 보통 `/api/v1/admin/**` Prefix를 사용한다.

Q. Command API Pattern은 언제 사용하는가?
A. 결제 승인, 주문 취소, 이메일 인증처럼 단순 CRUD가 아닌 Domain Action을 실행할 때 사용한다.

Q. Command API에서 중요한 것은 무엇인가?
A. 상태 전이 Validation, Idempotency, Error Code 정의이다.

Q. File Upload API는 어떤 Content-Type을 사용하는가?
A. `multipart/form-data`를 사용한다.

Q. File Upload API에서 검증해야 할 것은 무엇인가?
A. 파일 크기, MIME Type, 확장자, 저장 경로, 접근 권한을 검증해야 한다.

Q. Batch API Pattern은 언제 사용하는가?
A. 여러 Resource를 한 번의 요청으로 등록, 수정, 삭제, 상태 변경할 때 사용한다.

Q. Batch API에서 중요한 정책은 무엇인가?
A. 최대 처리 개수, 부분 성공 여부, Transaction 범위, 항목별 Error Response이다.

Q. DELETE 요청에 Body를 넣어도 되는가?
A. 가능은 하지만 실무 호환성 문제가 생길 수 있어 주의가 필요하다.

Q. Batch Delete는 어떻게 설계하는 것이 안전한가?
A. `POST /resources/batch-delete` 같은 Command API로 설계하는 방식이 더 안전할 수 있다.

Q. External API Proxy Pattern은 언제 사용하는가?
A. Backend가 외부 API Provider를 호출하고 내부 Response DTO로 변환해야 할 때 사용한다.

Q. 외부 API Key를 Frontend에 노출해도 되는가?
A. 안 된다. Provider API Key는 Backend 또는 안전한 서버 환경에서 관리해야 한다.

Q. External API 오류는 어떻게 처리하는가?
A. Provider 오류를 내부 Error Code로 변환하고 필요 시 502, 503, 504로 구분한다.

Q. API Pattern은 어떻게 선택하는가?
A. Resource, Action 유형, 인증/권한, 목록 여부, 중복 요청 위험을 기준으로 선택한다.

Q. 하나의 API에 여러 Pattern을 적용할 수 있는가?
A. 가능하다. 예를 들어 관리자 생성 API는 Admin API Pattern과 Create Pattern을 함께 사용한다.

Q. Practical API Pattern에서 가장 흔한 실수는 무엇인가?
A. 목록/상세 DTO 미분리, 동사형 URI, Ownership 누락, Admin Prefix 누락, Idempotency 누락이다.
