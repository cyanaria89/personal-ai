# API Design Part 04 - Pagination, Filtering, Sorting & Validation

---

# 1. Pagination

## 1.1 Pagination

### [개념]

Pagination은 대량 데이터 목록을 한 번에 모두 반환하지 않고 일정 단위로 나누어 조회하는 API 설계 방식이다.

Pagination은 목록 조회 API의 성능, 안정성, 사용성을 높이는 핵심 Contract이다.

```text
Client
→ GET /festivals?page=0&size=20
→ Server
→ Page Response
→ Client
```

---

### [핵심]

- Pagination은 대량 데이터 조회에 필수이다.
- Pagination은 응답 크기를 제한한다.
- Pagination은 DB 부하와 Network 비용을 줄인다.
- Pagination은 Frontend 목록 UI, 무한 스크롤, 더보기 UI와 연결된다.
- Pagination Contract에는 page, size, sort, hasNext, totalElements 같은 정보가 포함될 수 있다.
- 목록 조회 API는 기본적으로 Pagination 적용을 검토해야 한다.

---

### [실무]

2026 실무 기준 일반적인 목록 조회 API는 Page 기반 Pagination 또는 Cursor 기반 Pagination을 사용한다.

Spring Boot 3.x에서는 `Pageable`, `Page<T>`, `Slice<T>`를 자주 사용한다.

```java
@GetMapping("/festivals")
public ApiResponse<Page<FestivalResponse>> getFestivals(
        Pageable pageable
) {
    return ApiResponse.success(festivalService.getFestivals(pageable));
}
```

API 요청 예시:

```text
GET /festivals?page=0&size=20&sort=eventStartDate,asc
```

API 응답 예시:

```json
{
  "success": true,
  "data": {
    "content": [],
    "page": 0,
    "size": 20,
    "totalElements": 100,
    "totalPages": 5
  }
}
```

---

### [FAQ]

Q. Pagination은 왜 필요한가?

A. 대량 데이터를 한 번에 반환하지 않아 DB 부하, Network 비용, Client 렌더링 부담을 줄이기 위해 필요하다.

Q. 목록 조회 API에는 항상 Pagination을 적용해야 하는가?

A. 데이터가 증가할 수 있는 목록 조회 API라면 기본적으로 적용하는 것이 좋다.

Q. Pagination Contract에는 무엇이 포함되는가?

A. content, page, size, totalElements, totalPages, hasNext, sort 정보가 포함될 수 있다.

---

# 2. Page Based Pagination

## 2.1 Page Pagination

### [개념]

Page 기반 Pagination은 page 번호와 size를 사용하여 데이터를 페이지 단위로 조회하는 방식이다.

```text
/products?page=0&size=20
/festivals?page=1&size=10
```

Page 기반 Pagination은 일반적인 관리자 화면, 검색 결과, 목록 화면에 적합하다.

---

### [핵심]

- Page Pagination은 page와 size를 사용한다.
- page는 보통 0부터 시작한다.
- size는 한 페이지에 반환할 데이터 개수이다.
- totalElements와 totalPages를 제공할 수 있다.
- 특정 페이지 이동 UI에 적합하다.
- 데이터가 자주 변경되는 무한 스크롤에는 Cursor Pagination이 더 적합할 수 있다.

---

### [실무]

Spring Data JPA의 `Pageable`은 Page 기반 Pagination을 쉽게 지원한다.

```java
@GetMapping("/reviews")
public ApiResponse<Page<ReviewResponse>> getReviews(
        Pageable pageable
) {
    return ApiResponse.success(reviewService.getReviews(pageable));
}
```

Repository 예시:

```java
Page<Review> findByFestival_FestivalId(
        Long festivalId,
        Pageable pageable
);
```

요청 예시:

```text
GET /reviews?festivalId=1&page=0&size=20&sort=createdAt,desc
```

응답 예시:

```json
{
  "content": [],
  "page": 0,
  "size": 20,
  "totalElements": 53,
  "totalPages": 3,
  "first": true,
  "last": false
}
```

---

### [주의]

- page 시작 번호가 0인지 1인지 명확히 문서화한다.
- size 최대값을 제한한다.
- 기본 sort 기준을 정의한다.
- 데이터 변경이 잦은 경우 중복 또는 누락이 발생할 수 있다.
- `totalElements` 계산은 Count Query 비용이 발생할 수 있다.

---

### [FAQ]

Q. Page 기반 Pagination은 언제 사용하는가?

A. 검색 결과, 관리자 목록, 일반 목록처럼 특정 페이지 이동이 필요한 API에 사용한다.

Q. page는 0부터 시작하는가?

A. Spring Pageable 기본값은 0부터 시작한다. 프로젝트 Contract에 명확히 문서화해야 한다.

Q. Page Pagination의 단점은 무엇인가?

A. 데이터 변경이 잦으면 중복이나 누락이 생길 수 있고 Count Query 비용이 발생할 수 있다.

---

# 3. Cursor Based Pagination

## 3.1 Cursor Pagination

### [개념]

Cursor 기반 Pagination은 마지막으로 조회한 데이터의 기준값을 Cursor로 전달하여 다음 데이터를 조회하는 방식이다.

```text
/chat-messages?cursor=100&size=20
/notifications?cursor=2026-06-27T10:00:00&size=20
```

Cursor Pagination은 무한 스크롤, 실시간 목록, 대량 데이터 조회에 적합하다.

---

### [핵심]

- Cursor Pagination은 cursor와 size를 사용한다.
- cursor는 마지막 조회 데이터의 기준값이다.
- Cursor Pagination은 무한 스크롤에 적합하다.
- 데이터 변경이 잦은 목록에서 Page보다 안정적이다.
- totalElements를 제공하지 않는 경우가 많다.
- hasNext 또는 nextCursor를 함께 제공하는 것이 좋다.

---

### [실무]

채팅 메시지, 알림, 피드, 로그 같은 데이터는 Cursor 기반 조회 또는 Slice 기반 조회가 적합하다.

```text
GET /chat-rooms/{chatRoomId}/messages?cursor=300&size=30
GET /notifications?cursor=2026-06-27T15:00:00&size=20
```

응답 예시:

```json
{
  "success": true,
  "data": {
    "content": [],
    "nextCursor": 280,
    "hasNext": true
  }
}
```

Spring Data JPA에서는 `Slice<T>`를 사용하여 Count Query 없이 다음 페이지 존재 여부를 확인할 수 있다.

```java
Slice<ChatMessage> findByChatRoom_ChatRoomIdOrderByCreatedAtDesc(
        Long chatRoomId,
        Pageable pageable
);
```

---

### [Best Practice]

- Cursor는 정렬 기준과 일치해야 한다.
- Cursor Field는 고유하거나 Tie-breaker가 있어야 한다.
- `createdAt`만 사용하면 동일 시간 데이터에서 중복 문제가 생길 수 있다.
- `createdAt + id` 조합을 Cursor로 사용할 수 있다.
- 응답에는 `hasNext` 또는 `nextCursor`를 포함한다.
- Cursor 의미와 정렬 방향을 API 문서에 명시한다.

---

### [FAQ]

Q. Cursor Pagination은 언제 사용하는가?

A. 무한 스크롤, 채팅 메시지, 알림, 피드, 로그처럼 데이터가 자주 추가되는 목록에 적합하다.

Q. Cursor Pagination은 Page Pagination보다 항상 좋은가?

A. 아니다. 특정 페이지 이동이 필요한 화면에는 Page Pagination이 더 적합하다.

Q. Cursor 응답에는 무엇을 포함해야 하는가?

A. content, nextCursor, hasNext 정보를 포함하는 것이 좋다.

---

# 4. Page vs Slice vs Cursor

## 4.1 Pagination Type Comparison

### [개념]

Page, Slice, Cursor는 목록 API에서 데이터를 나누어 반환하는 방식이다.

각 방식은 Count Query, 무한 스크롤, 특정 페이지 이동 가능 여부가 다르다.

---

### [핵심]

| 방식   | 특징                         | 적합한 상황            |
| ------ | ---------------------------- | ---------------------- |
| Page   | 전체 개수와 전체 페이지 제공 | 관리자 목록, 검색 결과 |
| Slice  | 다음 페이지 존재 여부만 제공 | 더보기, 무한 스크롤    |
| Cursor | 기준값 이후 데이터 조회      | 채팅, 알림, 피드       |

---

### [실무]

Spring Boot 3.x + JPA 기준 선택 기준:

```text
관리자 목록 → Page
검색 결과 페이지 → Page
더보기 목록 → Slice
무한 스크롤 → Slice or Cursor
채팅 메시지 → Cursor or Slice
알림 목록 → Cursor or Slice
대량 로그 → Cursor
```

`Page<T>`는 totalElements 계산을 위해 Count Query가 필요하다.

`Slice<T>`는 size보다 1개 더 조회하여 hasNext를 판단할 수 있다.

Cursor는 정렬 기준과 Cursor Field 설계가 중요하다.

---

### [주의]

- 모든 목록 API에 무조건 Page를 사용하지 않는다.
- Count Query 비용이 큰 목록에는 Slice 또는 Cursor를 고려한다.
- Cursor 기준이 불안정하면 중복 또는 누락이 발생한다.
- Frontend UI 방식과 Pagination 방식을 맞춘다.

---

### [FAQ]

Q. Page와 Slice의 차이는 무엇인가?

A. Page는 전체 개수와 전체 페이지 정보를 제공하고 Slice는 다음 페이지 존재 여부만 제공한다.

Q. Slice는 언제 사용하는가?

A. 더보기, 무한 스크롤처럼 전체 개수가 필요 없는 목록에 사용한다.

Q. Cursor는 언제 사용하는가?

A. 채팅, 알림, 피드처럼 데이터가 계속 추가되는 목록에 사용한다.

---

# 5. Filtering

## 5.1 Filter

### [개념]

Filtering은 특정 조건에 맞는 Resource만 조회하는 API 기능이다.

Filtering 조건은 보통 Query Parameter로 전달한다.

```text
/festivals?region=seoul
/products?category=food
/reviews?rating=5
```

---

### [핵심]

- Filtering은 조건 기반 조회이다.
- Filtering 조건은 Query Parameter로 표현한다.
- Filtering 이름은 Domain 용어와 일치해야 한다.
- 여러 Filter 조건을 조합할 수 있다.
- Filter 조건은 API 문서에 Type, Required, Example을 명확히 작성한다.
- Filtering은 DB Index와 성능을 함께 고려해야 한다.

---

### [실무]

Spring Boot 3.x API에서는 단순 Filter는 `@RequestParam`, 복합 Filter는 `@ModelAttribute` DTO를 사용한다.

```java
public record FestivalSearchRequest(
        String region,
        String theme,
        LocalDate startDate,
        LocalDate endDate
) {
}
```

```java
@GetMapping("/festivals")
public ApiResponse<Page<FestivalResponse>> getFestivals(
        @ModelAttribute FestivalSearchRequest request,
        Pageable pageable
) {
    return ApiResponse.success(festivalService.getFestivals(request, pageable));
}
```

Filter API 요청 예시:

```text
GET /festivals?region=seoul&theme=music&startDate=2026-07-01&endDate=2026-07-31
```

---

### [Best Practice]

- Filter Parameter 이름을 일관되게 유지한다.
- 날짜 범위는 `startDate`, `endDate`처럼 명확히 작성한다.
- 지역 조건은 `region`, `city`, `district` 등 프로젝트 용어를 통일한다.
- Boolean 조건은 `active=true`처럼 명확히 작성한다.
- 다중 선택 조건은 배열, 반복 Parameter, comma-separated 중 하나로 통일한다.
- Filter 조건이 많아지면 Search DTO를 사용한다.

---

### [FAQ]

Q. Filtering은 무엇인가?

A. 특정 조건에 맞는 Resource만 조회하는 API 기능이다.

Q. Filtering 조건은 어디에 담는가?

A. 보통 Query Parameter에 담는다.

Q. Filter 조건이 많으면 어떻게 처리하는가?

A. Search Request DTO로 묶고 `@ModelAttribute`로 바인딩한다.

---

# 6. Search

## 6.1 Search Query

### [개념]

Search는 사용자가 입력한 검색어 또는 조건을 기반으로 Resource를 찾는 API 기능이다.

Search는 Filtering보다 자유로운 키워드 검색을 포함할 수 있다.

```text
/festivals/search?keyword=music
/products/search?q=notebook
```

---

### [핵심]

- Search는 Keyword 기반 조회이다.
- Search Parameter 이름은 `keyword` 또는 `q` 중 하나로 통일한다.
- Search는 Filtering, Sorting, Pagination과 함께 사용된다.
- Search 결과는 Pagination 적용이 필요하다.
- 검색 대상 Field를 문서화하는 것이 좋다.
- 검색어 Validation과 길이 제한이 필요하다.

---

### [실무]

간단한 검색은 Query Parameter로 처리한다.

```java
@GetMapping("/festivals/search")
public ApiResponse<Page<FestivalResponse>> searchFestivals(
        @RequestParam String keyword,
        Pageable pageable
) {
    return ApiResponse.success(festivalService.searchFestivals(keyword, pageable));
}
```

복합 검색은 Search DTO로 처리한다.

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

Search API 요청 예시:

```text
GET /festivals/search?keyword=music&region=seoul&page=0&size=20
```

---

### [주의]

- 검색어 길이 제한을 두지 않으면 성능 문제가 발생할 수 있다.
- 검색어를 SQL에 직접 연결하지 않는다.
- LIKE 검색은 성능 저하가 발생할 수 있다.
- 대규모 검색은 Elasticsearch 또는 Full Text Search를 고려한다.
- Search Parameter 이름을 API마다 다르게 쓰지 않는다.

---

### [FAQ]

Q. Search와 Filtering의 차이는 무엇인가?

A. Search는 키워드 기반 검색이고 Filtering은 명확한 조건 기반 조회이다.

Q. 검색어 Parameter 이름은 무엇을 쓰는가?

A. `keyword` 또는 `q` 중 하나로 프로젝트 전체에서 통일한다.

Q. Search API에도 Pagination이 필요한가?

A. 필요하다. 검색 결과가 많을 수 있기 때문이다.

---

# 7. Sorting

## 7.1 Sort

### [개념]

Sorting은 목록 조회 결과를 특정 기준으로 정렬하는 API 기능이다.

Sorting 조건은 보통 Query Parameter로 전달한다.

```text
/festivals?sort=eventStartDate,asc
/reviews?sort=createdAt,desc
```

---

### [핵심]

- Sorting은 조회 결과 순서를 결정한다.
- Sorting 조건은 Query Parameter로 전달한다.
- 기본 정렬 기준을 정의해야 한다.
- 정렬 가능한 Field를 제한해야 한다.
- 정렬 방향은 asc 또는 desc로 표현한다.
- Sorting은 Pagination과 함께 사용되는 경우가 많다.

---

### [실무]

Spring Data Pageable은 `sort=field,direction` 형식을 지원한다.

```text
GET /festivals?page=0&size=20&sort=eventStartDate,asc
GET /reviews?page=0&size=10&sort=createdAt,desc
```

Controller 예시:

```java
@GetMapping("/festivals")
public ApiResponse<Page<FestivalResponse>> getFestivals(
        Pageable pageable
) {
    return ApiResponse.success(festivalService.getFestivals(pageable));
}
```

기본 정렬은 Service 또는 Pageable Default로 정의할 수 있다.

```java
@GetMapping("/reviews")
public ApiResponse<Page<ReviewResponse>> getReviews(
        @PageableDefault(size = 20, sort = "createdAt", direction = Sort.Direction.DESC)
        Pageable pageable
) {
    return ApiResponse.success(reviewService.getReviews(pageable));
}
```

---

### [Best Practice]

- 기본 정렬 기준을 반드시 정의한다.
- 정렬 가능한 Field를 API 문서에 명시한다.
- Client가 임의의 내부 Field로 정렬하지 못하게 제한한다.
- Pagination과 Sorting 기준을 함께 고정한다.
- Cursor Pagination에서는 정렬 기준과 Cursor 기준을 일치시킨다.

---

### [FAQ]

Q. Sorting은 무엇인가?

A. 목록 조회 결과를 특정 기준으로 정렬하는 API 기능이다.

Q. Sorting Parameter는 어떻게 작성하는가?

A. 보통 `sort=field,direction` 형식을 사용한다.

Q. 기본 정렬 기준이 필요한 이유는 무엇인가?

A. 정렬 기준이 없으면 Pagination 결과가 불안정해질 수 있기 때문이다.

---

# 8. Pagination Filtering Sorting Combination

## 8.1 Query Combination

### [개념]

목록 조회 API는 Pagination, Filtering, Sorting을 함께 사용하는 경우가 많다.

이 세 요소는 목록 API Contract의 핵심이다.

```text
/festivals?region=seoul&theme=music&page=0&size=20&sort=eventStartDate,asc
```

---

### [핵심]

- Filtering은 어떤 데이터를 조회할지 결정한다.
- Sorting은 어떤 순서로 반환할지 결정한다.
- Pagination은 몇 개씩 반환할지 결정한다.
- 세 조건은 Query Parameter로 함께 표현할 수 있다.
- Contract가 명확하지 않으면 Frontend 목록 UI 오류가 발생한다.
- 목록 API 문서에는 Filter, Sort, Page 조건을 함께 명시해야 한다.

---

### [실무]

복합 목록 조회 API 예시:

```java
@GetMapping("/festivals")
public ApiResponse<Page<FestivalResponse>> getFestivals(
        @ModelAttribute FestivalSearchRequest request,
        @PageableDefault(size = 20, sort = "eventStartDate", direction = Sort.Direction.ASC)
        Pageable pageable
) {
    return ApiResponse.success(festivalService.getFestivals(request, pageable));
}
```

요청 예시:

```text
GET /festivals?keyword=music&region=seoul&theme=concert&page=0&size=20&sort=eventStartDate,asc
```

응답 예시:

```json
{
  "success": true,
  "data": {
    "content": [],
    "page": 0,
    "size": 20,
    "totalElements": 40,
    "totalPages": 2,
    "sort": "eventStartDate,asc"
  }
}
```

---

### [주의]

- Filter 조건과 Sort Field 이름을 문서마다 다르게 쓰지 않는다.
- Pageable 기본값을 숨기지 말고 문서화한다.
- size 최대값을 제한한다.
- 정렬 기준이 없는 Pagination은 결과가 불안정할 수 있다.
- 복합 조건 검색은 Index와 Query 성능을 검토한다.

---

### [FAQ]

Q. 목록 조회 API에서 가장 중요한 Query 조건은 무엇인가?

A. Filtering, Sorting, Pagination이다.

Q. Pagination과 Sorting을 함께 써야 하는 이유는 무엇인가?

A. 정렬 기준이 없으면 페이지마다 데이터 순서가 불안정해질 수 있기 때문이다.

Q. 목록 API 문서에는 무엇을 포함해야 하는가?

A. Filter Parameter, Sort Field, Page Parameter, Response Metadata를 포함해야 한다.

---

# 9. Validation

## 9.1 Request Validation

### [개념]

Validation은 Client Request가 API Contract와 Business Rule에 맞는지 검사하는 과정이다.

Validation은 잘못된 입력으로 인한 오류, 보안 문제, 데이터 무결성 문제를 방지한다.

```text
Request
→ Binding
→ Validation
→ Service
→ Response
```

---

### [핵심]

- Validation은 Invalid Input을 방지한다.
- Validation은 Request DTO에 적용한다.
- Validation 실패는 보통 400 Bad Request로 처리한다.
- Validation Error Response는 Field Error를 포함할 수 있다.
- Validation은 Controller 진입 전 또는 Service 진입 전에 수행한다.
- Business Validation은 Service Layer에서 처리할 수 있다.

---

### [실무]

Spring Boot 3.x에서는 Jakarta Bean Validation을 사용한다.

```java
public record ReviewCreateRequest(
        @NotNull
        @Min(1)
        @Max(5)
        Integer rating,

        @NotBlank
        @Size(max = 1000)
        String content
) {
}
```

Controller에서 `@Valid`를 적용한다.

```java
@PostMapping("/reviews")
public ApiResponse<ReviewResponse> createReview(
        @Valid @RequestBody ReviewCreateRequest request
) {
    return ApiResponse.success(reviewService.createReview(request));
}
```

Validation 실패 응답 예시:

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

### [FAQ]

Q. Validation은 왜 필요한가?

A. 잘못된 입력으로 인한 오류, 보안 문제, 데이터 무결성 문제를 방지하기 위해 필요하다.

Q. Validation 실패는 어떤 Status Code를 사용하는가?

A. 일반적으로 400 Bad Request를 사용한다.

Q. Validation은 어디에 적용하는가?

A. Request DTO에 Bean Validation Annotation을 적용하고 Controller에서 `@Valid`로 검증한다.

---

# 10. Input Validation Types

## 10.1 Validation Rule

### [개념]

Input Validation Type은 입력 데이터의 필수 여부, 길이, 범위, 형식, 패턴을 검사하는 규칙이다.

API Request Field마다 Validation Rule을 명확히 정의해야 한다.

---

### [핵심]

| Validation    | 목적             |
| ------------- | ---------------- |
| NotNull       | null 방지        |
| NotBlank      | 빈 문자열 방지   |
| Size          | 문자열 길이 제한 |
| Min / Max     | 숫자 범위 제한   |
| Email         | 이메일 형식 검증 |
| Pattern       | 정규식 검증      |
| Positive      | 양수 검증        |
| Past / Future | 날짜 조건 검증   |

---

### [실무]

Request DTO Validation 예시:

```java
public record UserSignupRequest(
        @NotBlank
        @Email
        String email,

        @NotBlank
        @Size(min = 8, max = 50)
        String password,

        @NotBlank
        @Size(max = 20)
        String nickname
) {
}
```

날짜 범위 검증은 단일 Annotation으로 부족할 수 있으므로 Custom Validation 또는 Service Validation을 사용한다.

```text
startDate <= endDate
eventStartDate <= eventEndDate
```

---

### [주의]

- String 필수값에는 `@NotNull`보다 `@NotBlank`를 고려한다.
- 숫자 범위는 `@Min`, `@Max`를 명확히 작성한다.
- 날짜 범위 검증은 별도 로직이 필요할 수 있다.
- Validation Message를 사용자 친화적으로 작성한다.
- Validation Rule과 DB Constraint가 서로 충돌하지 않게 한다.

---

### [FAQ]

Q. `@NotNull`과 `@NotBlank`의 차이는 무엇인가?

A. `@NotNull`은 null만 막고 `@NotBlank`는 null, 빈 문자열, 공백 문자열을 막는다.

Q. 숫자 범위 검증은 무엇을 사용하는가?

A. `@Min`, `@Max`, `@Positive` 등을 사용한다.

Q. 날짜 시작일과 종료일 관계는 어떻게 검증하는가?

A. Custom Validation 또는 Service Layer Business Validation으로 검증한다.

---

# 11. Business Validation

## 11.1 Business Rule Validation

### [개념]

Business Validation은 단순 입력 형식이 아니라 Domain Rule과 Business Rule을 검증하는 과정이다.

예를 들어 중복 이메일, 존재하지 않는 Resource, 이미 좋아요한 상태, 결제 상태 충돌 등이 Business Validation 대상이다.

---

### [핵심]

- Business Validation은 Service Layer에서 주로 처리한다.
- Business Validation 실패는 적절한 4xx Status Code로 처리한다.
- Resource 없음은 404 Not Found로 처리한다.
- 중복 또는 상태 충돌은 409 Conflict로 처리한다.
- 권한 부족은 403 Forbidden으로 처리한다.
- Business Error Code를 명확히 정의해야 한다.

---

### [실무]

Business Validation 예시:

```java
public void likeFestival(Long userId, Long festivalId) {
    Festival festival = festivalRepository.findById(festivalId)
            .orElseThrow(() -> new BusinessException(ErrorCode.FESTIVAL_NOT_FOUND));

    if (festivalLikeRepository.existsByUserIdAndFestivalId(userId, festivalId)) {
        throw new BusinessException(ErrorCode.ALREADY_LIKED_FESTIVAL);
    }

    festivalLikeRepository.save(FestivalLike.create(userId, festival));
}
```

Error Mapping 예시:

```text
FESTIVAL_NOT_FOUND → 404 Not Found
ALREADY_LIKED_FESTIVAL → 409 Conflict
ACCESS_DENIED → 403 Forbidden
```

---

### [주의]

- Business Exception을 500으로 처리하지 않는다.
- 모든 예외를 400으로 뭉개지 않는다.
- Validation Error와 Business Error를 구분한다.
- Error Code는 변경 비용이 크므로 신중히 설계한다.
- 중복 요청은 Idempotency 정책과 함께 검토한다.

---

### [FAQ]

Q. Business Validation은 무엇인가?

A. Domain Rule과 Business Rule에 맞는지 검증하는 과정이다.

Q. Business Validation은 어디에서 처리하는가?

A. 주로 Service Layer에서 처리한다.

Q. 중복 좋아요 같은 오류는 어떤 Status Code를 사용하는가?

A. 보통 409 Conflict를 사용한다.

---

# 12. Validation Error Response

## 12.1 Field Error Response

### [개념]

Validation Error Response는 Request Validation 실패 시 Client에게 어떤 Field가 왜 잘못되었는지 알려주는 Error Response이다.

Validation Error는 일반 Error Response보다 Field 단위 정보가 필요할 수 있다.

```json
{
  "code": "VALIDATION_FAILED",
  "message": "Validation failed",
  "errors": []
}
```

---

### [핵심]

- Validation 실패는 400 Bad Request를 사용한다.
- Error Code는 `VALIDATION_FAILED`처럼 명확히 작성한다.
- Field Error는 field, message를 포함한다.
- 필요하면 rejectedValue를 포함할 수 있다.
- 민감한 입력값은 rejectedValue로 노출하지 않는다.
- Frontend Form Error 표시와 연결된다.

---

### [실무]

Validation Error Response 예시:

```json
{
  "code": "VALIDATION_FAILED",
  "message": "Validation failed",
  "errors": [
    {
      "field": "email",
      "message": "email must be a valid email address"
    },
    {
      "field": "password",
      "message": "password size must be between 8 and 50"
    }
  ]
}
```

Spring Boot GlobalExceptionHandler 예시:

```java
@ExceptionHandler(MethodArgumentNotValidException.class)
public ResponseEntity<ValidationErrorResponse> handleValidation(
        MethodArgumentNotValidException ex
) {
    List<FieldErrorResponse> errors = ex.getBindingResult()
            .getFieldErrors()
            .stream()
            .map(error -> new FieldErrorResponse(
                    error.getField(),
                    error.getDefaultMessage()
            ))
            .toList();

    return ResponseEntity.badRequest()
            .body(new ValidationErrorResponse(
                    "VALIDATION_FAILED",
                    "Validation failed",
                    errors
            ));
}
```

---

### [FAQ]

Q. Validation Error Response에는 무엇이 들어가는가?

A. Error Code, Error Message, Field Error List가 들어간다.

Q. Field Error에는 무엇을 포함하는가?

A. field와 message를 포함하고 필요 시 rejectedValue를 포함할 수 있다.

Q. rejectedValue를 항상 포함해도 되는가?

A. 아니다. 비밀번호, 토큰 같은 민감 정보는 노출하면 안 된다.

---

# 13. Security Validation

## 13.1 Security Input Validation

### [개념]

Security Validation은 악의적인 입력으로부터 API를 보호하기 위한 입력 검증이다.

SQL Injection, XSS, Path Traversal, Mass Assignment 같은 공격을 방지하는 데 중요하다.

---

### [핵심]

- 사용자 입력은 신뢰하지 않는다.
- SQL 문자열 직접 연결을 피한다.
- Entity 직접 바인딩을 피한다.
- 허용된 Field만 Request DTO로 받는다.
- 길이 제한을 적용한다.
- HTML 입력은 저장/출력 정책을 명확히 한다.
- 파일 경로, URL, Redirect Parameter는 별도 검증한다.

---

### [실무]

JPA Query Parameter Binding 또는 QueryDSL을 사용하여 SQL Injection 위험을 줄인다.

```java
@Query("select f from Festival f where f.title like concat('%', :keyword, '%')")
List<Festival> searchByKeyword(@Param("keyword") String keyword);
```

Request DTO로 허용 Field만 받는다.

```java
public record UserProfileUpdateRequest(
        @Size(max = 20)
        String nickname,

        @Size(max = 500)
        String profileImageUrl
) {
}
```

Mass Assignment 방지를 위해 Entity를 직접 Request Body로 받지 않는다.

---

### [주의]

- Request Body를 Entity에 직접 매핑하지 않는다.
- 검색어를 SQL 문자열에 직접 연결하지 않는다.
- HTML 입력 허용 여부를 명확히 정한다.
- URL 입력은 허용 도메인 또는 형식 검증을 고려한다.
- 파일 업로드는 확장자, MIME Type, Size 검증이 필요하다.

---

### [FAQ]

Q. Security Validation은 무엇인가?

A. 악의적인 입력으로부터 API를 보호하기 위한 입력 검증이다.

Q. Mass Assignment는 어떻게 방지하는가?

A. Entity를 직접 받지 않고 Request DTO로 허용 Field만 입력받는다.

Q. SQL Injection은 어떻게 줄이는가?

A. Parameter Binding, JPA, QueryDSL, Prepared Statement를 사용하고 문자열 직접 연결을 피한다.

---

# 14. Common Mistakes

## 14.1 Pagination Filtering Sorting Validation Mistakes

### [Troubleshooting]

문제: 목록 조회 API가 전체 데이터를 반환한다.

원인: Pagination Contract가 정의되지 않았다.

해결: Page, Slice, Cursor 중 하나를 선택하고 page, size, sort 또는 cursor Contract를 문서화한다.

---

문제: 무한 스크롤 API에서 Page를 사용해 중복 데이터가 발생한다.

원인: 데이터 추가가 잦은 목록에 Page Pagination을 적용했다.

해결: Cursor Pagination 또는 Slice 기반 Pagination을 사용한다.

---

문제: Query Parameter 이름이 API마다 다르다.

원인: Filter / Search Naming Convention이 없다.

해결: `keyword`, `region`, `theme`, `startDate`, `endDate`, `page`, `size`, `sort`처럼 표준 이름을 정한다.

---

문제: Pagination 결과 순서가 불안정하다.

원인: 기본 Sort 기준이 없다.

해결: `createdAt desc`, `id desc` 같은 기본 정렬 기준을 정의한다.

---

문제: size 값이 너무 커서 서버 부하가 발생한다.

원인: Page Size 최대값 제한이 없다.

해결: 최대 size 제한과 기본 size를 API 정책으로 정의한다.

---

문제: Validation 실패가 500으로 반환된다.

원인: MethodArgumentNotValidException 처리가 없다.

해결: GlobalExceptionHandler에서 Validation Error를 400 Bad Request로 변환한다.

---

문제: 중복 데이터 오류를 Validation Error로 처리한다.

원인: Request Validation과 Business Validation을 구분하지 않았다.

해결: 형식 검증은 400, 중복과 상태 충돌은 409 Conflict로 처리한다.

---

문제: Entity를 Request Body로 직접 받아 보안 문제가 생긴다.

원인: Mass Assignment 방어가 없다.

해결: Request DTO로 허용 Field만 입력받는다.

---

### [FAQ]

Q. Pagination에서 가장 흔한 실수는 무엇인가?

A. 전체 데이터 반환, 기본 정렬 누락, size 제한 누락, Page와 Cursor 선택 오류이다.

Q. Filtering에서 가장 흔한 실수는 무엇인가?

A. Query Parameter 이름 불일치, 조건 의미 불명확, Search DTO 부재이다.

Q. Sorting에서 가장 흔한 실수는 무엇인가?

A. 기본 정렬 기준 누락과 정렬 가능한 Field 제한 부재이다.

Q. Validation에서 가장 흔한 실수는 무엇인가?

A. DTO Validation 누락, Business Validation과 혼동, Validation Error Response 불일치이다.

---

# Retrieval Queries

### [FAQ]

Q. Pagination이란 무엇인가?
A. 대량 데이터 목록을 일정 단위로 나누어 조회하는 API 설계 방식이다.

Q. Pagination은 왜 필요한가?
A. DB 부하, Network 비용, Client 렌더링 부담을 줄이기 위해 필요하다.

Q. Page Pagination은 무엇인가?
A. page 번호와 size를 사용하여 데이터를 페이지 단위로 조회하는 방식이다.

Q. Cursor Pagination은 무엇인가?
A. 마지막 조회 데이터의 기준값을 Cursor로 전달해 다음 데이터를 조회하는 방식이다.

Q. Slice는 무엇인가?
A. 전체 개수 없이 다음 페이지 존재 여부만 제공하는 Pagination 방식이다.

Q. Page와 Slice의 차이는 무엇인가?
A. Page는 전체 개수와 전체 페이지 정보를 제공하고 Slice는 다음 페이지 존재 여부만 제공한다.

Q. Cursor Pagination은 언제 사용하는가?
A. 채팅, 알림, 피드, 로그처럼 데이터가 자주 추가되는 목록에 사용한다.

Q. Page Pagination은 언제 사용하는가?
A. 관리자 목록, 검색 결과처럼 특정 페이지 이동이 필요한 API에 사용한다.

Q. Filtering이란 무엇인가?
A. 특정 조건에 맞는 Resource만 조회하는 API 기능이다.

Q. Filtering 조건은 어디에 담는가?
A. 보통 Query Parameter에 담는다.

Q. Search와 Filtering의 차이는 무엇인가?
A. Search는 키워드 기반 검색이고 Filtering은 명확한 조건 기반 조회이다.

Q. Search Parameter 이름은 무엇을 쓰는가?
A. `keyword` 또는 `q` 중 하나로 프로젝트 전체에서 통일한다.

Q. Sorting이란 무엇인가?
A. 목록 조회 결과를 특정 기준으로 정렬하는 API 기능이다.

Q. Sorting Parameter는 어떻게 작성하는가?
A. 보통 `sort=field,direction` 형식을 사용한다.

Q. 기본 정렬 기준이 필요한 이유는 무엇인가?
A. 정렬 기준이 없으면 Pagination 결과가 불안정해질 수 있기 때문이다.

Q. 목록 조회 API의 핵심 Query 조건은 무엇인가?
A. Filtering, Sorting, Pagination이다.

Q. Validation이란 무엇인가?
A. Client Request가 API Contract와 Business Rule에 맞는지 검사하는 과정이다.

Q. Request Validation 실패는 어떤 Status Code를 사용하는가?
A. 일반적으로 400 Bad Request를 사용한다.

Q. Bean Validation은 어디에 적용하는가?
A. Request DTO Field에 적용하고 Controller Parameter에 `@Valid`를 사용한다.

Q. `@NotNull`과 `@NotBlank`의 차이는 무엇인가?
A. `@NotNull`은 null만 막고 `@NotBlank`는 null, 빈 문자열, 공백 문자열을 막는다.

Q. Business Validation이란 무엇인가?
A. Domain Rule과 Business Rule에 맞는지 검증하는 과정이다.

Q. Business Validation은 어디에서 처리하는가?
A. 주로 Service Layer에서 처리한다.

Q. 중복 데이터 오류는 어떤 Status Code를 사용하는가?
A. 보통 409 Conflict를 사용한다.

Q. Validation Error Response에는 무엇이 들어가는가?
A. Error Code, Error Message, Field Error List가 들어간다.

Q. Security Validation이란 무엇인가?
A. 악의적인 입력으로부터 API를 보호하기 위한 입력 검증이다.

Q. Mass Assignment는 어떻게 방지하는가?
A. Entity를 직접 받지 않고 Request DTO로 허용 Field만 입력받는다.

Q. SQL Injection은 어떻게 줄이는가?
A. Parameter Binding, JPA, QueryDSL, Prepared Statement를 사용하고 문자열 직접 연결을 피한다.
