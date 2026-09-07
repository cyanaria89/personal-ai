# API Design Part 02 - URI Design, HTTP Method & Status Code

---

# 1. URI Design

## 1.1 URI

### [개념]

URI(Uniform Resource Identifier)는 API에서 Resource를 식별하는 주소이다.

REST API에서 URI는 행위가 아니라 Resource를 표현한다.

```text
Good: /users/{userId}
Bad:  /getUserById
```

URI Design은 API Contract의 핵심 요소이다.

---

### [핵심]

- URI는 Resource를 식별한다.
- URI는 명사 중심으로 작성한다.
- URI는 복수형 Resource를 권장한다.
- URI는 일관된 Naming Convention을 사용한다.
- URI는 Frontend / Backend / OpenAPI 문서에서 동일해야 한다.
- URI가 불명확하면 API 검색성, 테스트성, 유지보수성이 낮아진다.

---

### [실무]

2026 실무 기준 URI Design은 단순하고 예측 가능해야 한다.

좋은 URI는 Client가 문서를 적게 봐도 Resource 구조를 이해할 수 있게 만든다.

```text
/users
/users/{userId}
/users/{userId}/orders
/products
/products/{productId}
/festivals
/festivals/{festivalId}
/festivals/{festivalId}/reviews
```

URI는 화면 이름이 아니라 Resource 이름으로 설계한다.

```text
Good: /festivals/{festivalId}/reviews
Bad:  /festivalReviewPage
```

---

### [Best Practice]

- Resource는 명사로 작성한다.
- Collection Resource는 복수형을 사용한다.
- Resource 식별자는 Path Variable로 표현한다.
- 검색 조건은 Query Parameter로 표현한다.
- URI Depth는 너무 깊게 만들지 않는다.
- URI Naming은 프로젝트 전체에서 통일한다.
- `/api/v1` 같은 Version Prefix는 정책적으로 통일한다.

---

### [FAQ]

Q. URI는 무엇을 표현해야 하는가?

A. URI는 행위가 아니라 Resource를 표현해야 한다.

Q. URI에 동사를 넣으면 안 되는 이유는?

A. REST에서는 행위를 HTTP Method가 표현하므로 URI에 동사를 넣으면 역할이 중복되고 일관성이 낮아진다.

Q. URI Design에서 가장 중요한 것은 무엇인가?

A. Resource 중심 설계, 명사 사용, 복수형 일관성, Path Variable과 Query Parameter 구분이다.

---

# 2. Resource Naming

## 2.1 Resource Name

### [개념]

Resource Name은 API가 제공하는 대상의 이름이다.

Resource Name은 URI의 핵심 구성 요소이며 Client가 API를 이해하는 기준이다.

```text
User Resource      → /users
Product Resource   → /products
Festival Resource  → /festivals
Review Resource    → /reviews
```

---

### [핵심]

- Resource Name은 명사로 작성한다.
- Resource Name은 복수형을 권장한다.
- Resource Name은 Domain 용어와 일치해야 한다.
- Resource Name은 API 문서, DTO, Frontend Type과 연결된다.
- Resource Name은 너무 추상적이거나 화면 중심이면 안 된다.

---

### [실무]

실무에서는 Entity 이름과 Resource 이름이 항상 1:1로 일치하지 않는다.

Resource는 Client Use Case 기준으로 설계할 수 있다.

```text
Entity: Festival
Resource:
/festivals
/festivals/{festivalId}/location
/festivals/{festivalId}/reviews
/festivals/{festivalId}/likes
/festivals/{festivalId}/chat-room
```

Resource Name은 API Contract에서 고정되므로 변경 비용이 크다.

초기 설계 시 Domain 용어를 명확히 정리해야 한다.

---

### [주의]

- `/data`, `/info`, `/list`처럼 의미가 약한 이름을 피한다.
- `/festivalList`처럼 화면 이름을 Resource로 쓰지 않는다.
- `/users`와 `/member`를 혼용하지 않는다.
- `/reviews`와 `/comments`를 같은 의미로 섞지 않는다.
- 단수형과 복수형을 섞지 않는다.

---

### [FAQ]

Q. Resource Name은 Entity 이름과 같아야 하는가?

A. 반드시 같을 필요는 없다. Resource는 외부 API 표현이고 Entity는 내부 Domain 또는 DB 모델이다.

Q. Resource Name을 복수형으로 쓰는 이유는?

A. Collection Resource를 자연스럽게 표현하고 URI 일관성을 유지하기 위해서이다.

Q. Resource Name을 화면 이름으로 지으면 안 되는 이유는?

A. API가 화면에 종속되어 재사용성과 유지보수성이 낮아지기 때문이다.

---

# 3. Path Variable

## 3.1 Path Variable

### [개념]

Path Variable은 URI 경로 안에서 특정 Resource를 식별하는 값이다.

```text
/users/{userId}
/products/{productId}
/festivals/{festivalId}
```

Path Variable은 Resource Identifier를 표현한다.

---

### [핵심]

- Path Variable은 특정 Resource 식별에 사용한다.
- Path Variable 이름은 의미 있게 작성한다.
- `{id}`보다 `{userId}`, `{festivalId}`처럼 구체적인 이름을 권장한다.
- Path Variable은 필수 값이다.
- Path Variable은 Resource 계층 관계를 표현할 수 있다.

---

### [실무]

Spring Boot 3.x Controller에서는 `@PathVariable`로 Path Variable을 바인딩한다.

```java
@GetMapping("/festivals/{festivalId}")
public ApiResponse<FestivalDetailResponse> getFestival(
        @PathVariable Long festivalId
) {
    return ApiResponse.success(festivalService.getFestival(festivalId));
}
```

Path Variable 이름은 URI Template, Controller Parameter, OpenAPI 문서에서 일치해야 한다.

---

### [예제]

```text
GET /users/10
GET /orders/100
GET /festivals/25
GET /festivals/25/reviews
```

---

### [FAQ]

Q. Path Variable은 언제 사용하는가?

A. 특정 Resource를 식별해야 할 때 사용한다.

Q. `{id}`보다 `{userId}`가 좋은 이유는?

A. 어떤 Resource의 식별자인지 명확해져 API 문서와 코드 가독성이 좋아지기 때문이다.

Q. Path Variable은 선택 값으로 사용해도 되는가?

A. 권장하지 않는다. 선택 조건은 Query Parameter로 분리하는 것이 좋다.

---

# 4. Query Parameter

## 4.1 Query Parameter

### [개념]

Query Parameter는 조회 조건, 검색어, 필터, 정렬, 페이지 정보를 URI 뒤에 전달하는 값이다.

```text
/products?category=food
/festivals?keyword=music
/festivals?page=0&size=20
```

Query Parameter는 Resource 자체가 아니라 Resource 조회 조건을 표현한다.

---

### [핵심]

- Query Parameter는 검색 조건에 사용한다.
- Query Parameter는 Filtering에 사용한다.
- Query Parameter는 Sorting에 사용한다.
- Query Parameter는 Pagination에 사용한다.
- Query Parameter는 Optional 조건에 적합하다.
- Query Parameter는 Resource Identifier 대체용으로 남용하지 않는다.

---

### [실무]

Spring Boot 3.x에서는 `@RequestParam` 또는 `@ModelAttribute`를 사용한다.

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

조건이 많으면 Search Request DTO로 묶는다.

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

### [예제]

```text
GET /festivals?keyword=music
GET /festivals?region=seoul
GET /festivals?theme=food
GET /festivals?startDate=2026-07-01&endDate=2026-07-31
GET /festivals?page=0&size=20&sort=startDate,asc
```

---

### [FAQ]

Q. Query Parameter는 언제 사용하는가?

A. 검색, 필터링, 정렬, 페이지 조건처럼 Resource 조회 조건을 전달할 때 사용한다.

Q. Path Variable과 Query Parameter의 차이는 무엇인가?

A. Path Variable은 특정 Resource 식별에 사용하고 Query Parameter는 조회 조건에 사용한다.

Q. 조건이 많은 검색 API는 어떻게 설계하는가?

A. Query Parameter를 Search Request DTO로 묶어 `@ModelAttribute`로 처리하는 것이 좋다.

---

# 5. HTTP Method

## 5.1 HTTP Method Role

### [개념]

HTTP Method는 Resource에 수행할 행위를 표현한다.

REST API에서는 URI가 Resource를 표현하고 HTTP Method가 행위를 표현한다.

```text
GET    → 조회
POST   → 생성
PUT    → 전체 수정
PATCH  → 부분 수정
DELETE → 삭제
```

---

### [핵심]

- GET은 Resource 조회에 사용한다.
- POST는 Resource 생성 또는 Command 처리에 사용한다.
- PUT은 Resource 전체 수정에 사용한다.
- PATCH는 Resource 부분 수정에 사용한다.
- DELETE는 Resource 삭제에 사용한다.
- Method 역할이 일관되지 않으면 API Contract 품질이 낮아진다.

---

### [실무]

2026 실무 기준 HTTP Method는 REST 원칙과 팀 API Convention을 함께 고려한다.

기본 CRUD API는 다음 Mapping을 권장한다.

```text
GET    /users          → 목록 조회
GET    /users/{userId} → 단건 조회
POST   /users          → 생성
PUT    /users/{userId} → 전체 수정
PATCH  /users/{userId} → 부분 수정
DELETE /users/{userId} → 삭제
```

Command 성격이 강한 API는 POST를 사용할 수 있다.

```text
POST /orders/{orderId}/cancel
POST /payments/{paymentId}/confirm
POST /users/{userId}/password-reset
```

단, Command URI는 남용하지 않고 Domain Action이 명확할 때만 사용한다.

---

### [FAQ]

Q. HTTP Method는 무엇을 표현하는가?

A. Resource에 수행할 행위를 표현한다.

Q. 조회 API에 POST를 사용해도 되는가?

A. 일반 조회는 GET이 원칙이다. 복잡한 검색 조건이나 보안상 Body가 필요한 특수 검색은 POST를 사용할 수 있지만 정책이 필요하다.

Q. Command API에서 POST를 사용하는 이유는?

A. 생성이 아니더라도 서버 상태를 변경하거나 Domain Command를 실행하는 요청은 POST가 적합할 수 있기 때문이다.

---

# 6. GET

## 6.1 GET Method

### [개념]

GET은 Resource를 조회하는 HTTP Method이다.

GET은 서버 상태를 변경하지 않는 Safe Method이다.

```text
GET /users
GET /users/{userId}
GET /festivals?region=seoul
```

---

### [핵심]

- GET은 조회에 사용한다.
- GET은 Request Body를 사용하지 않는 것이 원칙이다.
- GET은 Query Parameter와 함께 자주 사용한다.
- GET은 Safe Method이다.
- GET은 Idempotent Method이다.
- GET 응답은 Cache 정책과 연결될 수 있다.

---

### [실무]

GET API는 목록 조회, 단건 조회, 검색, 필터링, 정렬, 페이지 조회에 사용한다.

```java
@GetMapping("/festivals/{festivalId}")
public ApiResponse<FestivalDetailResponse> getFestival(
        @PathVariable Long festivalId
) {
    return ApiResponse.success(festivalService.getFestival(festivalId));
}
```

목록 조회 API는 Pagination을 기본 고려한다.

```text
GET /festivals?page=0&size=20&sort=eventStartDate,asc
```

---

### [주의]

- GET으로 생성, 수정, 삭제를 수행하지 않는다.
- GET Request Body에 의존하지 않는다.
- 민감 정보는 Query Parameter에 노출하지 않는다.
- 대량 목록 조회에는 Pagination을 적용한다.

---

### [FAQ]

Q. GET은 언제 사용하는가?

A. Resource를 조회할 때 사용한다.

Q. GET은 서버 데이터를 변경해도 되는가?

A. 안 된다. GET은 Safe Method이며 서버 상태 변경에 사용하지 않는다.

Q. GET 검색 조건은 어디에 담는가?

A. 보통 Query Parameter에 담는다.

---

# 7. POST

## 7.1 POST Method

### [개념]

POST는 Resource 생성 또는 서버 상태를 변경하는 Command 요청에 사용하는 HTTP Method이다.

```text
POST /users
POST /orders
POST /payments/{paymentId}/confirm
```

---

### [핵심]

- POST는 생성에 사용한다.
- POST는 서버 상태 변경에 사용한다.
- POST는 Request Body를 사용한다.
- POST는 기본적으로 Idempotent하지 않다.
- POST 성공 시 보통 201 Created 또는 200 OK를 반환한다.
- Command API에도 POST를 사용할 수 있다.

---

### [실무]

생성 API는 POST + Request Body 조합을 사용한다.

```java
@PostMapping("/reviews")
public ApiResponse<ReviewResponse> createReview(
        @Valid @RequestBody ReviewCreateRequest request
) {
    return ApiResponse.success(reviewService.createReview(request));
}
```

생성 결과가 명확한 경우 `201 Created`를 권장한다.

```text
POST /reviews
→ 201 Created
```

서버에서 처리 명령을 실행하는 API도 POST를 사용할 수 있다.

```text
POST /payments/{paymentId}/confirm
POST /orders/{orderId}/cancel
```

---

### [주의]

- 단순 조회를 POST로 만들지 않는다.
- 생성 API의 Request Body Schema를 명확히 정의한다.
- 중복 생성 위험이 있으면 Idempotency Key를 고려한다.
- Command API는 URI에 Action이 들어갈 수 있으나 남용하지 않는다.

---

### [FAQ]

Q. POST는 언제 사용하는가?

A. Resource 생성 또는 서버 상태를 변경하는 Command 요청에 사용한다.

Q. POST는 Idempotent한가?

A. 기본적으로 Idempotent하지 않다. 같은 요청을 반복하면 여러 Resource가 생성될 수 있다.

Q. POST 생성 성공 시 어떤 Status Code를 사용하는가?

A. 일반적으로 201 Created를 사용하고, 처리 결과 반환 중심이면 200 OK를 사용할 수 있다.

---

# 8. PUT

## 8.1 PUT Method

### [개념]

PUT은 Resource 전체 수정 또는 전체 교체에 사용하는 HTTP Method이다.

```text
PUT /users/{userId}
PUT /products/{productId}
```

PUT은 같은 요청을 여러 번 보내도 결과가 같아야 하는 Idempotent Method이다.

---

### [핵심]

- PUT은 전체 수정에 사용한다.
- PUT은 Resource 전체 상태를 교체하는 의미가 강하다.
- PUT은 Idempotent Method이다.
- PUT Request Body는 전체 Resource 수정 데이터를 포함한다.
- 부분 수정은 PATCH를 권장한다.

---

### [실무]

전체 수정 API는 PUT을 사용한다.

```java
@PutMapping("/users/{userId}")
public ApiResponse<UserResponse> updateUser(
        @PathVariable Long userId,
        @Valid @RequestBody UserUpdateRequest request
) {
    return ApiResponse.success(userService.updateUser(userId, request));
}
```

실무에서는 PUT과 PATCH의 경계를 팀 Convention으로 명확히 정해야 한다.

많은 프로젝트에서 대부분의 수정은 PATCH로 처리하고, 전체 교체 의미가 명확한 경우에만 PUT을 사용한다.

---

### [주의]

- 일부 Field만 수정하는 API를 PUT으로 만들지 않는다.
- PUT Request Body의 누락 Field 처리 정책을 명확히 한다.
- 전체 교체인지 전체 업데이트인지 팀 규칙을 문서화한다.

---

### [FAQ]

Q. PUT은 언제 사용하는가?

A. Resource 전체 수정 또는 전체 교체에 사용한다.

Q. PUT은 Idempotent한가?

A. 그렇다. 같은 요청을 여러 번 보내도 최종 결과가 같아야 한다.

Q. PUT과 PATCH의 차이는 무엇인가?

A. PUT은 전체 수정, PATCH는 부분 수정에 사용한다.

---

# 9. PATCH

## 9.1 PATCH Method

### [개념]

PATCH는 Resource의 일부 Field를 부분 수정하는 HTTP Method이다.

```text
PATCH /users/{userId}
PATCH /reviews/{reviewId}
```

PATCH는 변경할 Field만 Request Body에 포함하는 방식으로 자주 사용된다.

---

### [핵심]

- PATCH는 부분 수정에 사용한다.
- PATCH는 Request Body에 변경할 Field만 포함할 수 있다.
- PATCH는 Partial Update에 적합하다.
- PATCH는 PUT보다 수정 범위가 작다.
- PATCH의 Idempotency는 구현 방식에 따라 달라질 수 있다.

---

### [실무]

실무에서는 사용자 프로필 수정, 리뷰 내용 수정, 알림 읽음 처리 같은 API에 PATCH를 자주 사용한다.

```java
@PatchMapping("/reviews/{reviewId}")
public ApiResponse<ReviewResponse> updateReview(
        @PathVariable Long reviewId,
        @Valid @RequestBody ReviewUpdateRequest request
) {
    return ApiResponse.success(reviewService.updateReview(reviewId, request));
}
```

단일 상태 변경 API에도 PATCH를 사용할 수 있다.

```text
PATCH /notifications/{notificationId}/read
PATCH /users/{userId}/profile-image
```

---

### [주의]

- Request Body에서 null 값을 어떻게 처리할지 정해야 한다.
- Field 누락과 명시적 null의 의미를 구분해야 한다.
- PATCH API는 Validation Rule을 별도로 설계해야 한다.
- 단순 Command인지 Resource 부분 수정인지 구분해야 한다.

---

### [FAQ]

Q. PATCH는 언제 사용하는가?

A. Resource의 일부 Field를 부분 수정할 때 사용한다.

Q. PATCH와 PUT의 차이는 무엇인가?

A. PATCH는 부분 수정이고 PUT은 전체 수정 또는 전체 교체이다.

Q. PATCH에서 null 처리는 왜 중요한가?

A. null이 Field 삭제인지 변경 없음인지 의미가 모호할 수 있기 때문이다.

---

# 10. DELETE

## 10.1 DELETE Method

### [개념]

DELETE는 Resource를 삭제하는 HTTP Method이다.

```text
DELETE /users/{userId}
DELETE /reviews/{reviewId}
DELETE /favorites/{favoriteId}
```

DELETE는 특정 Resource Identifier와 함께 사용한다.

---

### [핵심]

- DELETE는 Resource 삭제에 사용한다.
- DELETE는 Path Variable로 삭제 대상을 식별한다.
- DELETE는 보통 Request Body를 사용하지 않는다.
- DELETE 성공 시 204 No Content 또는 200 OK를 반환한다.
- DELETE는 Idempotent하게 설계하는 것이 좋다.
- Soft Delete와 Hard Delete 정책을 구분해야 한다.

---

### [실무]

삭제 API는 명확한 Resource Identifier를 사용한다.

```java
@DeleteMapping("/reviews/{reviewId}")
public ApiResponse<Void> deleteReview(
        @PathVariable Long reviewId
) {
    reviewService.deleteReview(reviewId);
    return ApiResponse.success();
}
```

삭제 후 반환할 데이터가 없으면 204 No Content를 사용할 수 있다.

공통 Response Wrapper를 사용하는 프로젝트에서는 200 OK + Empty Body 또는 `data: null`을 사용할 수 있다.

---

### [주의]

- DELETE Body에 의존하지 않는다.
- 실제 DB 삭제인지 Soft Delete인지 정책을 명확히 한다.
- 권한 검증 없이 삭제 API를 열지 않는다.
- 이미 삭제된 Resource 요청 시 204, 404, 409 중 팀 정책을 정한다.

---

### [FAQ]

Q. DELETE는 언제 사용하는가?

A. Resource를 삭제할 때 사용한다.

Q. DELETE 성공 시 어떤 Status Code를 사용하는가?

A. 반환 데이터가 없으면 204 No Content, 공통 응답이 필요하면 200 OK를 사용할 수 있다.

Q. Soft Delete도 DELETE Method를 사용하는가?

A. 외부 API 의미가 삭제라면 내부 구현이 Soft Delete여도 DELETE Method를 사용할 수 있다.

---

# 11. Status Code

## 11.1 Status Code Role

### [개념]

HTTP Status Code는 API 처리 결과를 숫자로 표현하는 표준 응답 코드이다.

Status Code는 Client가 성공, 실패, 인증 오류, 권한 오류, 서버 오류를 구분하는 기준이다.

```text
2xx → Success
4xx → Client Error
5xx → Server Error
```

---

### [핵심]

- Status Code는 API 결과를 명확히 전달한다.
- 2xx는 성공 응답이다.
- 4xx는 Client 요청 오류이다.
- 5xx는 Server 처리 오류이다.
- Status Code와 Error Response Body는 의미가 일치해야 한다.
- Status Code 오사용은 Frontend Error Handling을 어렵게 한다.

---

### [실무]

2026 실무 기준 API는 Status Code와 Error Response를 함께 설계한다.

```json
{
  "code": "USER_NOT_FOUND",
  "message": "User not found"
}
```

Client는 Status Code로 오류 계층을 판단하고, Error Code로 세부 처리를 수행한다.

```text
404 + USER_NOT_FOUND → 사용자 없음
401 + INVALID_TOKEN  → 인증 실패
403 + ACCESS_DENIED  → 권한 없음
409 + DUPLICATE_EMAIL → 이메일 중복
```

---

### [FAQ]

Q. Status Code는 왜 중요한가?

A. Client가 API 처리 결과와 Error Handling 방식을 판단하는 기준이기 때문이다.

Q. Status Code와 Error Code는 같은가?

A. 다르다. Status Code는 HTTP 표준 코드이고 Error Code는 서비스 내부 오류 식별 코드이다.

Q. API 실패 응답에는 무엇이 필요한가?

A. 적절한 Status Code, Error Code, Error Message가 필요하다.

---

# 12. 2xx Success Status

## 12.1 Success Status Code

### [개념]

2xx Status Code는 API 요청이 성공적으로 처리되었음을 의미한다.

```text
200 OK
201 Created
204 No Content
```

---

### [핵심]

- 200 OK는 일반 성공 응답이다.
- 201 Created는 Resource 생성 성공 응답이다.
- 204 No Content는 성공했지만 Response Body가 없는 응답이다.
- 성공 응답도 Response Schema를 일관되게 유지해야 한다.
- 생성 API는 201 Created를 우선 고려한다.

---

### [실무]

일반 조회 성공은 200 OK를 사용한다.

```text
GET /users/{userId}
→ 200 OK
```

생성 성공은 201 Created를 권장한다.

```text
POST /users
→ 201 Created
```

삭제 성공 또는 Body 없는 성공은 204 No Content를 사용할 수 있다.

```text
DELETE /reviews/{reviewId}
→ 204 No Content
```

공통 Response Wrapper를 강하게 사용하는 프로젝트는 200 OK + `data: null`을 선택할 수 있다.

---

### [FAQ]

Q. 200 OK는 언제 사용하는가?

A. 일반적인 성공 응답에 사용한다.

Q. 201 Created는 언제 사용하는가?

A. Resource 생성이 성공했을 때 사용한다.

Q. 204 No Content는 언제 사용하는가?

A. 요청은 성공했지만 Response Body가 필요 없을 때 사용한다.

---

# 13. 4xx Client Error Status

## 13.1 Client Error Status Code

### [개념]

4xx Status Code는 Client Request에 문제가 있음을 의미한다.

```text
400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
409 Conflict
```

---

### [핵심]

- 400은 잘못된 요청이다.
- 401은 인증 실패이다.
- 403은 권한 없음이다.
- 404는 Resource 없음이다.
- 409는 현재 상태와 충돌이다.
- 4xx는 Client가 Request를 수정하면 해결될 수 있는 오류이다.

---

### [실무]

Validation 실패는 400 Bad Request를 사용한다.

```text
POST /users
→ 400 Bad Request
→ INVALID_INPUT
```

Token이 없거나 유효하지 않으면 401 Unauthorized를 사용한다.

```text
GET /users/me
→ 401 Unauthorized
→ INVALID_TOKEN
```

인증은 되었지만 권한이 없으면 403 Forbidden을 사용한다.

```text
DELETE /admin/users/{userId}
→ 403 Forbidden
→ ACCESS_DENIED
```

Resource가 없으면 404 Not Found를 사용한다.

```text
GET /festivals/999
→ 404 Not Found
→ FESTIVAL_NOT_FOUND
```

중복, 상태 충돌, 비즈니스 충돌은 409 Conflict를 사용한다.

```text
POST /users
→ 409 Conflict
→ DUPLICATE_EMAIL
```

---

### [FAQ]

Q. 400 Bad Request는 언제 사용하는가?

A. Request 형식이 잘못되었거나 Validation에 실패했을 때 사용한다.

Q. 401과 403의 차이는 무엇인가?

A. 401은 인증 실패이고 403은 인증은 되었지만 권한이 없는 상태이다.

Q. 409 Conflict는 언제 사용하는가?

A. 중복 생성, 상태 충돌, 비즈니스 규칙 충돌이 발생했을 때 사용한다.

---

# 14. 5xx Server Error Status

## 14.1 Server Error Status Code

### [개념]

5xx Status Code는 Server 내부 처리 중 오류가 발생했음을 의미한다.

```text
500 Internal Server Error
```

5xx는 Client 요청 자체보다 Server 처리 실패에 가깝다.

---

### [핵심]

- 500은 예상하지 못한 서버 오류이다.
- 5xx는 남발하지 않는다.
- 비즈니스 오류를 500으로 처리하지 않는다.
- 5xx 응답에도 Error Response Schema를 유지한다.
- Server Error는 Logging, Monitoring, Alert 대상이다.

---

### [실무]

Spring Boot 3.x에서는 GlobalExceptionHandler에서 예상 가능한 예외와 예상하지 못한 예외를 분리한다.

예상 가능한 비즈니스 예외는 4xx로 변환한다.

예상하지 못한 RuntimeException은 500으로 처리한다.

```text
BusinessException(USER_NOT_FOUND) → 404
BusinessException(DUPLICATE_EMAIL) → 409
MethodArgumentNotValidException → 400
RuntimeException → 500
```

500 응답에는 내부 Stack Trace를 노출하지 않는다.

---

### [주의]

- 사용자 입력 오류를 500으로 처리하지 않는다.
- 인증 실패를 500으로 처리하지 않는다.
- 권한 실패를 500으로 처리하지 않는다.
- DB 제약 조건 오류를 그대로 노출하지 않는다.
- Stack Trace를 Client에 반환하지 않는다.

---

### [FAQ]

Q. 500 Internal Server Error는 언제 사용하는가?

A. Server 내부에서 예상하지 못한 오류가 발생했을 때 사용한다.

Q. 비즈니스 예외를 500으로 처리해도 되는가?

A. 권장하지 않는다. Resource 없음, 중복, 권한 오류 등은 적절한 4xx로 처리해야 한다.

Q. 5xx Error Response에 Stack Trace를 포함해도 되는가?

A. 안 된다. 보안상 내부 구현 정보는 Client에 노출하지 않는다.

---

# 15. Status Code Mapping

## 15.1 Method Status Mapping

### [개념]

Status Code Mapping은 HTTP Method와 처리 결과에 맞는 Status Code를 연결하는 기준이다.

```text
GET success    → 200
POST created   → 201
DELETE success → 204
Validation fail → 400
Auth fail      → 401
Access denied  → 403
Not found      → 404
Conflict       → 409
Server error   → 500
```

---

### [핵심]

- Method와 Status Code는 의미가 맞아야 한다.
- 성공 응답은 2xx를 사용한다.
- Client 오류는 4xx를 사용한다.
- Server 오류는 5xx를 사용한다.
- Error Code와 Status Code는 의미가 일치해야 한다.
- 프로젝트 공통 Status Code 정책을 문서화한다.

---

### [실무]

API Review Agent는 다음 Mapping 오류를 우선 탐지해야 한다.

| 상황            | 권장 Status Code           |
| --------------- | -------------------------- |
| 조회 성공       | 200 OK                     |
| 생성 성공       | 201 Created                |
| 수정 성공       | 200 OK 또는 204 No Content |
| 삭제 성공       | 204 No Content 또는 200 OK |
| Validation 실패 | 400 Bad Request            |
| Token 없음      | 401 Unauthorized           |
| Token 만료      | 401 Unauthorized           |
| 권한 없음       | 403 Forbidden              |
| Resource 없음   | 404 Not Found              |
| 중복 데이터     | 409 Conflict               |
| 서버 내부 오류  | 500 Internal Server Error  |

---

### [FAQ]

Q. 생성 성공은 항상 201을 써야 하는가?

A. Resource 생성 의미가 명확하면 201 Created를 권장한다. 단순 처리 결과 반환이면 200 OK를 사용할 수 있다.

Q. 삭제 성공은 200과 204 중 무엇이 좋은가?

A. 반환 Body가 없으면 204 No Content, 공통 응답 Body가 필요하면 200 OK를 사용할 수 있다.

Q. Validation 실패와 비즈니스 충돌은 같은 Status Code인가?

A. 아니다. Validation 실패는 400, 중복이나 상태 충돌은 409를 권장한다.

---

# 16. Common Mistakes

## 16.1 URI Method Status Mistakes

### [Troubleshooting]

문제: URI에 `/getUser`, `/createUser` 같은 동사를 사용한다.

원인: URI가 Resource가 아니라 Action 중심으로 설계되었다.

해결: `/users`, `/users/{userId}`로 변경하고 행위는 HTTP Method로 표현한다.

---

문제: 조회 API에 POST를 사용한다.

원인: GET과 POST 역할 구분이 명확하지 않다.

해결: 일반 조회는 GET을 사용하고 조건은 Query Parameter로 전달한다.

---

문제: 부분 수정 API에 PUT을 사용한다.

원인: PUT과 PATCH 차이를 구분하지 않았다.

해결: 전체 수정은 PUT, 부분 수정은 PATCH로 분리한다.

---

문제: 인증 실패와 권한 실패를 모두 403으로 처리한다.

원인: Authentication과 Authorization 구분이 없다.

해결: 인증 실패는 401, 권한 실패는 403으로 처리한다.

---

문제: Resource 없음 오류를 500으로 반환한다.

원인: Business Exception을 Server Error로 처리했다.

해결: Resource 없음은 404 Not Found로 반환한다.

---

문제: 중복 데이터 오류를 400으로 반환한다.

원인: Validation Error와 Conflict Error를 구분하지 않았다.

해결: 중복 이메일, 중복 좋아요, 중복 예약 등은 409 Conflict로 처리한다.

---

문제: 삭제 성공 후 Response Body가 없는데 200을 사용한다.

원인: 204 No Content를 고려하지 않았다.

해결: Body가 없으면 204, 공통 Response Wrapper가 필요하면 200을 사용한다.

---

### [FAQ]

Q. URI, Method, Status Code에서 가장 흔한 실수는 무엇인가?

A. 동사형 URI, Method 오사용, 401/403 혼동, 400/409 혼동, 404를 500으로 처리하는 실수이다.

Q. API Review에서 Status Code는 어떻게 검수하는가?

A. 상황별 권장 Status Code와 Error Response Code가 의미상 일치하는지 확인한다.

Q. Method 오사용은 왜 위험한가?

A. Client, Cache, Proxy, API 문서, 테스트 코드가 HTTP 표준 의미를 기준으로 동작하기 때문이다.

---

# Retrieval Queries

### [FAQ]

Q. URI란 무엇인가?
A. API에서 Resource를 식별하는 주소이다.

Q. REST API에서 URI는 무엇을 표현하는가?
A. URI는 행위가 아니라 Resource를 표현한다.

Q. 좋은 URI Naming 기준은 무엇인가?
A. 명사 Resource, 복수형, 일관된 Naming, Path Variable과 Query Parameter 분리이다.

Q. Resource Name은 어떻게 작성하는가?
A. Domain 용어 기반 명사로 작성하고 복수형을 권장한다.

Q. Path Variable은 언제 사용하는가?
A. 특정 Resource Identifier를 URI 경로에서 표현할 때 사용한다.

Q. Query Parameter는 언제 사용하는가?
A. 검색, 필터링, 정렬, 페이지 조건처럼 조회 조건을 전달할 때 사용한다.

Q. GET은 언제 사용하는가?
A. Resource 조회에 사용한다.

Q. POST는 언제 사용하는가?
A. Resource 생성 또는 서버 상태를 변경하는 Command 요청에 사용한다.

Q. PUT은 언제 사용하는가?
A. Resource 전체 수정 또는 전체 교체에 사용한다.

Q. PATCH는 언제 사용하는가?
A. Resource 일부 Field를 부분 수정할 때 사용한다.

Q. DELETE는 언제 사용하는가?
A. Resource 삭제에 사용한다.

Q. 200 OK는 언제 사용하는가?
A. 일반적인 성공 응답에 사용한다.

Q. 201 Created는 언제 사용하는가?
A. Resource 생성 성공에 사용한다.

Q. 204 No Content는 언제 사용하는가?
A. 요청은 성공했지만 Response Body가 없을 때 사용한다.

Q. 400 Bad Request는 언제 사용하는가?
A. Request 형식 오류 또는 Validation 실패에 사용한다.

Q. 401 Unauthorized는 언제 사용하는가?
A. 인증 정보가 없거나 유효하지 않을 때 사용한다.

Q. 403 Forbidden은 언제 사용하는가?
A. 인증은 되었지만 Resource 접근 권한이 없을 때 사용한다.

Q. 404 Not Found는 언제 사용하는가?
A. 요청한 Resource가 존재하지 않을 때 사용한다.

Q. 409 Conflict는 언제 사용하는가?
A. 중복 데이터, 상태 충돌, 비즈니스 규칙 충돌이 발생했을 때 사용한다.

Q. 500 Internal Server Error는 언제 사용하는가?
A. Server 내부에서 예상하지 못한 오류가 발생했을 때 사용한다.

Q. PUT과 PATCH의 차이는 무엇인가?
A. PUT은 전체 수정이고 PATCH는 부분 수정이다.

Q. 401과 403의 차이는 무엇인가?
A. 401은 Authentication 실패이고 403은 Authorization 실패이다.

Q. API Status Code Review 기준은 무엇인가?
A. 처리 상황, HTTP Method, Error Code, Response Body 의미가 서로 일치하는지 확인한다.
