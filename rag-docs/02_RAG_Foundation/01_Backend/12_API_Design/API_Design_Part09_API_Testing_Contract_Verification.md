# API Design Part 09 - API Testing, Contract Verification & Integration Validation

---

# 1. API Testing

## 1.1 API Testing Purpose

### [개념]

API Testing은 API가 Request / Response Contract, Status Code, Error Response, Security Contract, Business Rule을 올바르게 만족하는지 검증하는 과정이다.

API Testing은 단순 호출 성공 확인이 아니라 API Contract 안정성 검증이다.

```text
API Contract
→ Test Request
→ API Execution
→ Response Verification
→ Contract Validation
```

---

### [핵심]

- API Testing은 Contract 검증이다.
- API Testing은 정상 케이스와 실패 케이스를 모두 포함한다.
- API Testing은 Status Code를 검증한다.
- API Testing은 Response Body Schema를 검증한다.
- API Testing은 Error Response Schema를 검증한다.
- API Testing은 Authentication / Authorization을 검증한다.
- API Testing은 Rate Limiting과 Idempotency를 검증할 수 있다.
- API Testing은 Frontend Integration 전에 수행해야 한다.

---

### [실무]

2026 실무 기준 API Testing은 여러 레벨에서 수행한다.

| 테스트                | 목적                                                |
| --------------------- | --------------------------------------------------- |
| Controller Test       | Request Mapping, Validation, Response 확인          |
| Service Test          | Business Rule, Transaction, Exception 확인          |
| Repository Test       | Query, Pagination, Sorting 확인                     |
| Swagger UI Test       | 문서 기반 수동 API 검증                             |
| Postman Test          | 시나리오 기반 API 검증                              |
| Frontend Network Test | 실제 연동 검증                                      |
| Security Test         | Authentication, Authorization, CSRF, Ownership 검증 |
| Contract Test         | API 문서와 실제 응답 일치 검증                      |
| Regression Test       | 변경 후 기존 API 영향 검증                          |

API Testing은 다음 순서로 진행한다.

```text
Unit Test
→ Controller Test
→ Swagger UI Test
→ Postman Scenario Test
→ Frontend Integration Test
→ Regression Test
```

---

### [FAQ]

Q. API Testing이란 무엇인가?

A. API가 Request / Response Contract, Status Code, Error Response, Security Contract를 만족하는지 검증하는 과정이다.

Q. API Testing에서 가장 중요한 것은 무엇인가?

A. 정상 응답뿐 아니라 실패 응답, Error Response, 인증/권한 조건까지 검증하는 것이다.

Q. API Testing은 언제 수행하는가?

A. 구현 중, Swagger 테스트 시, Frontend 연동 전, 배포 전, 변경 후 Regression Test에서 수행한다.

---

# 2. Controller Test

## 2.1 Controller Layer Test

### [개념]

Controller Test는 API Entry Point에서 Request Mapping, Parameter Binding, Validation, Status Code, Response Body를 검증하는 테스트이다.

Spring Boot에서는 MockMvc 또는 WebTestClient를 사용할 수 있다.

```text
HTTP Request
→ Controller
→ Validation
→ Mock Service
→ Response
```

---

### [핵심]

- Controller Test는 API Mapping을 검증한다.
- Controller Test는 Path Variable Binding을 검증한다.
- Controller Test는 Query Parameter Binding을 검증한다.
- Controller Test는 Request Body Binding을 검증한다.
- Controller Test는 Validation 실패를 검증한다.
- Controller Test는 Response Schema를 검증한다.
- Controller Test는 Service Logic 자체보다 API Contract를 검증한다.
- Spring Security 적용 여부에 따라 인증, 권한, CSRF 설정을 고려해야 한다.

---

### [실무]

MockMvc Controller Test 예시:

```java
@WebMvcTest(ReviewController.class)
class ReviewControllerTest {

    @Autowired
    MockMvc mockMvc;

    @MockBean
    ReviewService reviewService;

    @Test
    void createReview_success() throws Exception {
        String requestBody = """
            {
              "rating": 5,
              "content": "Great festival"
            }
            """;

        mockMvc.perform(post("/api/v1/festivals/1/reviews")
                        .contentType(MediaType.APPLICATION_JSON)
                        .content(requestBody))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.success").value(true));
    }
}
```

Validation 실패 테스트 예시:

```java
@Test
void createReview_validationFail() throws Exception {
    String requestBody = """
        {
          "rating": 10,
          "content": ""
        }
        """;

    mockMvc.perform(post("/api/v1/festivals/1/reviews")
                    .contentType(MediaType.APPLICATION_JSON)
                    .content(requestBody))
            .andExpect(status().isBadRequest())
            .andExpect(jsonPath("$.code").value("VALIDATION_FAILED"));
}
```

---

### [주의]

- Controller Test에서 DB까지 검증하려 하지 않는다.
- Service는 Mock으로 대체한다.
- Validation 실패 케이스를 반드시 포함한다.
- Error Response Schema를 검증한다.
- 인증 필요 API는 Security Test 설정을 포함한다.
- Response Field 이름을 jsonPath로 검증한다.
- POST / PUT / PATCH / DELETE 테스트에서 403이 발생하면 CSRF 설정도 확인한다.

---

### [FAQ]

Q. Controller Test는 무엇을 검증하는가?

A. Request Mapping, Parameter Binding, Validation, Status Code, Response Body를 검증한다.

Q. Controller Test에서 Service는 실제 객체를 사용하는가?

A. 보통 Mock 객체를 사용해 Controller Contract에 집중한다.

Q. Controller Test에서 Validation 실패도 확인해야 하는가?

A. 확인해야 한다. Validation Error Response는 API Contract의 핵심이다.

---

# 3. MockMvc Security Test

## 3.1 Spring Security MockMvc Test

### [개념]

MockMvc Security Test는 Spring Security가 적용된 API에서 인증, 권한, CSRF, Security Filter 동작을 검증하는 테스트이다.

Spring Security가 활성화된 상태에서 POST, PUT, PATCH, DELETE 요청은 CSRF 설정에 따라 403 Forbidden이 발생할 수 있다.

```text
MockMvc Request
→ Security Filter Chain
→ CSRF Check
→ Authentication
→ Authorization
→ Controller
```

---

### [핵심]

- Security Filter가 적용되면 인증과 권한 조건이 테스트에 반영된다.
- POST / PUT / PATCH / DELETE 요청은 CSRF 설정 영향을 받을 수 있다.
- JWT Stateless REST API에서는 보통 CSRF를 비활성화한다.
- 테스트 설정과 실제 Security Config가 다르면 테스트 결과가 왜곡된다.
- `addFilters = false`는 Security Filter를 제거하므로 Security 검증에는 부적합하다.
- Controller Contract Test와 Security Test 목적을 구분해야 한다.

---

### [실무]

CSRF가 활성화된 테스트 예시:

```java
mockMvc.perform(post("/api/v1/reviews")
        .with(csrf())
        .contentType(MediaType.APPLICATION_JSON)
        .content(requestBody))
    .andExpect(status().isOk());
```

JWT Stateless API에서 CSRF Disable 예시:

```java
http
    .csrf(csrf -> csrf.disable())
    .sessionManagement(session ->
            session.sessionCreationPolicy(SessionCreationPolicy.STATELESS)
    );
```

Controller Contract만 검증할 때 Security Filter 제외 예시:

```java
@AutoConfigureMockMvc(addFilters = false)
```

단, `addFilters = false`는 Authentication / Authorization 검증을 생략한다.

인증 사용자 Mock 예시:

```java
mockMvc.perform(get("/api/v1/users/me")
        .with(user("user1").roles("USER")))
    .andExpect(status().isOk());
```

---

### [주의]

- 403이 항상 권한 실패는 아니다.
- CSRF 때문에 403이 발생할 수 있다.
- Security Test에서는 CSRF, Authentication, Authorization 원인을 분리한다.
- `addFilters = false`를 남용하면 Security Issue를 놓칠 수 있다.
- Protected API 테스트는 실제 Security Config와 최대한 유사하게 구성한다.
- JWT Filter를 Mock 처리할지 실제 Filter를 사용할지 테스트 목적에 따라 결정한다.

---

### [FAQ]

Q. MockMvc POST 테스트에서 403이 발생하면 무엇을 확인해야 하는가?

A. CSRF 설정, Security Filter, 인증 정보, 권한 설정을 확인해야 한다.

Q. JWT Stateless API에서 CSRF는 보통 어떻게 처리하는가?

A. 보통 CSRF를 비활성화한다.

Q. `@AutoConfigureMockMvc(addFilters = false)`를 사용해도 되는가?

A. Controller Contract 테스트에는 사용할 수 있지만 Security 검증에는 부적합하다.

---

# 4. Service Test

## 4.1 Service Layer Test

### [개념]

Service Test는 Business Logic, Business Validation, Transaction Rule, Exception Flow를 검증하는 테스트이다.

Service Test는 API Contract보다 Domain Rule과 Business Rule 정확성에 집중한다.

```text
Service Method
→ Business Validation
→ Repository
→ Domain Update
→ Response DTO
```

---

### [핵심]

- Service Test는 Business Rule을 검증한다.
- Service Test는 중복 검증을 확인한다.
- Service Test는 Resource 없음 예외를 확인한다.
- Service Test는 Ownership 검증을 확인한다.
- Service Test는 Transaction 내 상태 변경을 확인한다.
- Service Test는 ErrorCode 발생을 확인한다.
- Service Test는 Repository Mock 또는 Test DB를 사용할 수 있다.
- Idempotency와 상태 전이 검증을 포함할 수 있다.

---

### [실무]

Mockito Service Test 예시:

```java
@ExtendWith(MockitoExtension.class)
class FestivalLikeServiceTest {

    @Mock
    FestivalRepository festivalRepository;

    @Mock
    FestivalLikeRepository festivalLikeRepository;

    @InjectMocks
    FestivalLikeService festivalLikeService;

    @Test
    void likeFestival_duplicateLike_throwsConflict() {
        Long userId = 1L;
        Long festivalId = 10L;

        when(festivalRepository.findById(festivalId))
                .thenReturn(Optional.of(new Festival()));

        when(festivalLikeRepository.existsByUserIdAndFestivalId(userId, festivalId))
                .thenReturn(true);

        BusinessException ex = assertThrows(
                BusinessException.class,
                () -> festivalLikeService.like(userId, festivalId)
        );

        assertThat(ex.getErrorCode()).isEqualTo(ErrorCode.ALREADY_LIKED_FESTIVAL);
    }
}
```

Ownership 검증 테스트 예시:

```java
@Test
void updateReview_notOwner_throwsAccessDenied() {
    Long currentUserId = 1L;
    Long reviewOwnerId = 2L;

    Review review = Review.create(reviewOwnerId, "content", 5);

    when(reviewRepository.findById(10L))
            .thenReturn(Optional.of(review));

    BusinessException ex = assertThrows(
            BusinessException.class,
            () -> reviewService.updateReview(currentUserId, 10L, request)
    );

    assertThat(ex.getErrorCode()).isEqualTo(ErrorCode.ACCESS_DENIED);
}
```

---

### [주의]

- Service Test에서 Controller Mapping을 검증하지 않는다.
- Business ErrorCode를 명확히 검증한다.
- 중복 요청, 상태 충돌, 권한 실패를 테스트한다.
- Repository Mock이 너무 복잡하면 Integration Test를 고려한다.
- Transaction Rollback이 중요한 로직은 통합 테스트로 보완한다.
- 외부 API 호출 Service는 Provider Client를 Mock 처리한다.

---

### [FAQ]

Q. Service Test는 무엇을 검증하는가?

A. Business Logic, Business Validation, Ownership, Exception Flow, Transaction Rule을 검증한다.

Q. Service Test에서 중요한 실패 케이스는 무엇인가?

A. Resource 없음, 중복 요청, 권한 없음, 상태 충돌, Validation 이후 Business Rule 실패이다.

Q. Service Test와 Controller Test의 차이는 무엇인가?

A. Controller Test는 API Contract를 검증하고 Service Test는 Business Rule을 검증한다.

---

# 5. Repository Test

## 5.1 Repository Layer Test

### [개념]

Repository Test는 DB Query, Entity Mapping, Pagination, Filtering, Sorting, Constraint를 검증하는 테스트이다.

Spring Boot에서는 `@DataJpaTest`를 사용해 Repository Layer를 독립적으로 검증할 수 있다.

```text
Repository Method
→ JPA Query
→ Database
→ Entity Result
```

---

### [핵심]

- Repository Test는 Query 정확성을 검증한다.
- Repository Test는 Pagination을 검증한다.
- Repository Test는 Sorting을 검증한다.
- Repository Test는 Filtering 조건을 검증한다.
- Repository Test는 Unique Constraint를 검증한다.
- Repository Test는 Entity Mapping을 검증한다.
- Repository Test는 Service Business Logic 검증이 아니다.

---

### [실무]

Repository Pagination Test 예시:

```java
@DataJpaTest
class ReviewRepositoryTest {

    @Autowired
    ReviewRepository reviewRepository;

    @Test
    void findByFestivalId_pagination_success() {
        Pageable pageable = PageRequest.of(
                0,
                20,
                Sort.by(Sort.Direction.DESC, "createdAt")
        );

        Page<Review> result = reviewRepository.findByFestival_FestivalId(1L, pageable);

        assertThat(result.getSize()).isEqualTo(20);
    }
}
```

Unique Constraint 검증 예시:

```java
@Test
void duplicateLike_uniqueConstraintViolation() {
    FestivalLike like1 = FestivalLike.create(1L, 10L);
    FestivalLike like2 = FestivalLike.create(1L, 10L);

    festivalLikeRepository.save(like1);

    assertThrows(DataIntegrityViolationException.class,
            () -> festivalLikeRepository.saveAndFlush(like2));
}
```

---

### [주의]

- Repository Test는 실제 DB Dialect 차이를 고려한다.
- H2와 MySQL의 동작 차이를 주의한다.
- QueryDSL, Native Query는 별도 검증이 필요하다.
- Pagination Test는 Sort 기준을 함께 검증한다.
- Constraint Test는 DB Schema와 Entity Annotation이 일치해야 한다.
- Cursor Pagination은 정렬 기준과 Cursor 조건을 함께 검증한다.

---

### [FAQ]

Q. Repository Test는 무엇을 검증하는가?

A. DB Query, Entity Mapping, Pagination, Filtering, Sorting, Constraint를 검증한다.

Q. Repository Test에서 Pagination도 검증해야 하는가?

A. 해야 한다. 목록 API 품질은 Repository Query와 Pagination 정확성에 의존한다.

Q. H2 테스트만으로 충분한가?

A. 항상 충분하지 않다. MySQL, PostgreSQL 등 실제 DB와 Dialect 차이가 있을 수 있다.

---

# 6. Swagger UI Test

## 6.1 Manual Contract Test

### [개념]

Swagger UI Test는 OpenAPI 문서를 기반으로 API를 직접 호출하여 Request / Response Contract를 확인하는 수동 테스트이다.

Swagger UI Test는 Backend 단독 API 확인과 Frontend 연동 전 검증에 유용하다.

```text
Swagger UI
→ Request Input
→ Execute
→ Status Code
→ Response Body
→ Contract Check
```

---

### [핵심]

- Swagger UI Test는 문서 기반 테스트이다.
- Request Schema를 직접 확인할 수 있다.
- Response Schema를 직접 확인할 수 있다.
- Status Code를 확인할 수 있다.
- JWT Bearer Token 인증 테스트를 할 수 있다.
- Error Response 테스트도 수행해야 한다.
- Rate Limit Error와 External API Error 문서화 여부도 확인한다.
- Swagger 문서와 실제 응답이 다르면 Contract Mismatch이다.

---

### [실무]

Swagger UI Test Checklist:

- API가 Swagger UI에 표시되는가?
- Summary와 Description이 실제 기능과 일치하는가?
- Path Variable Example이 있는가?
- Query Parameter Example이 있는가?
- Request Body Schema가 DTO와 일치하는가?
- Success Response가 실제 DTO와 일치하는가?
- Error Response가 문서화되어 있는가?
- JWT Authorize가 동작하는가?
- Protected API에서 Token 없이 401이 발생하는가?
- 권한 없는 사용자로 403이 발생하는가?
- Rate Limit 대상 API에 429가 문서화되어 있는가?
- External API 연동 API에 502 / 503 / 504 또는 프로젝트 정책 Error가 문서화되어 있는가?

Swagger UI Test Flow:

```text
1. Swagger UI 접속
2. API 선택
3. Request Parameter 입력
4. Bearer Token 필요 시 Authorize
5. Execute
6. Status Code 확인
7. Response Body 확인
8. OpenAPI Schema와 실제 응답 비교
```

---

### [FAQ]

Q. Swagger UI Test는 무엇인가?

A. OpenAPI 문서를 기반으로 API를 직접 호출해 Contract를 확인하는 수동 테스트이다.

Q. Swagger UI Test에서 실패 응답도 확인해야 하는가?

A. 해야 한다. Error Response Contract가 Frontend Error Handling에 필요하기 때문이다.

Q. Swagger UI 결과와 실제 API가 다르면 무엇인가?

A. Contract Mismatch이다.

---

# 7. Postman Test

## 7.1 Scenario API Test

### [개념]

Postman Test는 API를 시나리오 단위로 호출하고 Environment, Token, Collection, Test Script를 활용해 검증하는 API 테스트 방식이다.

Postman은 로그인 후 Token 저장, 인증 API 호출, CRUD 시나리오 검증에 유용하다.

```text
Login API
→ Save Token
→ Protected API
→ Assert Response
→ Scenario Result
```

---

### [핵심]

- Postman은 시나리오 기반 테스트에 적합하다.
- Environment Variable로 Base URL과 Token을 관리할 수 있다.
- Collection으로 API 그룹을 관리한다.
- Test Script로 Status Code와 Response Field를 검증할 수 있다.
- 로그인 후 Access Token을 자동 저장할 수 있다.
- 배포 환경별 API 테스트에 유용하다.
- 401, 403, 409, 429 같은 실패 시나리오 검증에 유용하다.

---

### [실무]

Postman Environment 예시:

```text
baseUrl = http://localhost:8080
accessToken = eyJhbGciOiJIUzI1NiJ9...
```

Authorization Header 예시:

```text
Authorization: Bearer {{accessToken}}
```

Postman Test Script 예시:

```javascript
pm.test("Status code is 200", function () {
  pm.response.to.have.status(200);
});

pm.test("Response success is true", function () {
  const json = pm.response.json();
  pm.expect(json.success).to.eql(true);
});
```

Login 후 Token 저장 예시:

```javascript
const json = pm.response.json();
pm.environment.set("accessToken", json.data.accessToken);
```

429 Test Script 예시:

```javascript
pm.test("Rate limit exceeded", function () {
  pm.response.to.have.status(429);
  const json = pm.response.json();
  pm.expect(json.code).to.eql("RATE_LIMIT_EXCEEDED");
});
```

---

### [주의]

- Local, Dev, Prod 환경을 분리한다.
- Token 만료 시 재로그인 Flow를 준비한다.
- 테스트 데이터 생성과 삭제 순서를 관리한다.
- 테스트 간 의존성이 너무 강하면 유지보수가 어렵다.
- 실패 응답 Test Script도 작성한다.
- 민감한 Token을 공유 Collection에 저장하지 않는다.
- Rate Limit 테스트는 운영 환경에 무리한 부하를 주지 않도록 제한한다.

---

### [FAQ]

Q. Postman Test는 무엇인가?

A. API를 시나리오 단위로 호출하고 Environment, Token, Test Script로 검증하는 테스트 방식이다.

Q. Swagger UI와 Postman의 차이는 무엇인가?

A. Swagger UI는 문서 기반 테스트에 강하고 Postman은 시나리오 기반 테스트와 환경 관리에 강하다.

Q. Postman에서 Token은 어떻게 재사용하는가?

A. Login API 응답에서 Access Token을 추출해 Environment Variable에 저장하고 Header에서 사용한다.

---

# 8. Contract Verification

## 8.1 Contract Verification Process

### [개념]

Contract Verification은 API 문서, Backend 구현, Frontend 기대 구조, 실제 Network Response가 서로 일치하는지 검증하는 과정이다.

Contract Verification은 Contract Mismatch를 줄이는 핵심 단계이다.

```text
OpenAPI Document
→ Controller
→ DTO
→ Actual Response
→ Frontend Type
→ Contract Verified
```

---

### [핵심]

- OpenAPI 문서와 Controller Mapping을 비교한다.
- Request DTO와 Request Schema를 비교한다.
- Response DTO와 Response Schema를 비교한다.
- 실제 Response와 OpenAPI Example을 비교한다.
- Frontend Type과 Response Field를 비교한다.
- Error Response와 Frontend Error Handling을 비교한다.
- Security Config와 OpenAPI Security Requirement를 비교한다.
- Rate Limit Error와 Retry 처리 정책을 비교한다.
- Contract 변경 시 Regression Verification을 수행한다.

---

### [실무]

Contract Verification Checklist:

- URI가 Controller Mapping과 일치하는가?
- HTTP Method가 일치하는가?
- Path Variable 이름이 일치하는가?
- Query Parameter 이름이 일치하는가?
- Request Body Field가 Request DTO와 일치하는가?
- Response Body Field가 Response DTO와 일치하는가?
- Success Status Code가 문서와 일치하는가?
- Error Status Code가 문서와 일치하는가?
- Error Code가 문서와 일치하는가?
- Date Time Format이 문서와 일치하는가?
- Pagination Metadata가 문서와 일치하는가?
- Security Requirement가 실제 Security Config와 일치하는가?
- 429 Rate Limit Error가 실제 정책과 일치하는가?
- 502 / 503 / 504 External Error 정책이 문서와 일치하는가?

---

### [FAQ]

Q. Contract Verification이란 무엇인가?

A. API 문서, Backend 구현, Frontend 기대 구조, 실제 Network Response가 일치하는지 검증하는 과정이다.

Q. Contract Verification에서 비교해야 할 대상은 무엇인가?

A. OpenAPI 문서, Controller, DTO, 실제 Response, Frontend Type, Error Handling이다.

Q. Contract Verification이 중요한 이유는 무엇인가?

A. Contract Mismatch로 인한 Frontend 연동 오류와 배포 장애를 줄이기 위해서이다.

---

# 9. Frontend Integration Test

## 9.1 Browser Network Verification

### [개념]

Frontend Integration Test는 실제 Frontend 화면에서 API가 올바르게 호출되고 Response가 UI 상태와 렌더링에 정상 반영되는지 검증하는 테스트이다.

Browser Network Tab은 Frontend / Backend API 연동 오류를 확인하는 핵심 도구이다.

```text
User Action
→ Axios Request
→ Network Tab
→ API Response
→ State Update
→ UI Render
```

---

### [핵심]

- Frontend Integration Test는 실제 UI 흐름을 검증한다.
- Browser Network Tab에서 Request URL을 확인한다.
- Request Method를 확인한다.
- Request Header를 확인한다.
- Request Body와 Query Parameter를 확인한다.
- Response Status Code를 확인한다.
- Response Body Field와 Frontend Mapping을 확인한다.
- Console Error를 함께 확인한다.
- 401, 403, 404, 409, 429 처리 UI를 확인한다.

---

### [실무]

Frontend Integration Checklist:

- 클릭 또는 페이지 진입 시 API가 호출되는가?
- Axios Base URL이 올바른가?
- API Prefix가 맞는가?
- HTTP Method가 Backend와 일치하는가?
- Query Parameter 이름이 일치하는가?
- Path Variable 값이 정상인가?
- Authorization Header가 필요한 API에 포함되는가?
- Request Body Field가 DTO와 일치하는가?
- Response Field가 Frontend 코드에서 사용하는 이름과 일치하는가?
- Pagination Response 구조가 UI와 일치하는가?
- Error Code에 따른 사용자 메시지가 표시되는가?
- 429 발생 시 즉시 재시도 루프가 없는가?
- External API 실패 시 사용자 안내가 있는가?

Network Debug Flow:

```text
F12
→ Network
→ API Request 선택
→ Headers 확인
→ Payload 확인
→ Response 확인
→ Console 확인
→ Source Code Mapping 확인
```

---

### [FAQ]

Q. Frontend Integration Test는 무엇인가?

A. 실제 Frontend 화면에서 API 호출과 Response UI 반영이 정상인지 검증하는 테스트이다.

Q. Frontend API 오류에서 가장 먼저 확인할 것은 무엇인가?

A. Browser Network Tab의 Request URL, Method, Header, Payload, Status Code, Response Body이다.

Q. Response는 정상인데 화면이 안 나오면 무엇을 확인하는가?

A. Frontend Field Mapping, State Update, Conditional Rendering, Console Error를 확인한다.

---

# 10. Authentication Test

## 10.1 Authentication API Test

### [개념]

Authentication Test는 인증이 필요한 API가 Token 유무와 Token 유효성에 따라 올바른 응답을 반환하는지 검증하는 테스트이다.

JWT API에서는 Authorization Header와 Access Token 상태를 테스트해야 한다.

```text
Protected API
→ No Token
→ 401

Protected API
→ Invalid Token
→ 401

Protected API
→ Valid Token
→ 200
```

---

### [핵심]

- Token 없는 요청은 401을 반환해야 한다.
- Invalid Token 요청은 401을 반환해야 한다.
- Expired Token 요청은 401을 반환해야 한다.
- Valid Token 요청은 정상 처리되어야 한다.
- Bearer Prefix 누락 요청을 테스트한다.
- Public API는 Token 없이 접근 가능해야 한다.
- Protected API는 Security Config와 OpenAPI 문서가 일치해야 한다.

---

### [실무]

Authentication Test Case:

| Case                                | Expected        |
| ----------------------------------- | --------------- |
| Public API without Token            | 200             |
| Protected API without Token         | 401             |
| Protected API with Invalid Token    | 401             |
| Protected API with Expired Token    | 401             |
| Protected API without Bearer Prefix | 401             |
| Protected API with Valid Token      | 200             |
| Logout 후 기존 Token 사용           | 정책에 따라 401 |

MockMvc Security Test 예시:

```java
@Test
void protectedApi_withoutToken_returns401() throws Exception {
    mockMvc.perform(get("/api/v1/users/me"))
            .andExpect(status().isUnauthorized());
}
```

---

### [주의]

- 401과 403을 혼동하지 않는다.
- Public API가 실수로 Protected 처리되지 않았는지 확인한다.
- Protected API가 실수로 Public 처리되지 않았는지 확인한다.
- Swagger UI Authorize 설정과 실제 Security Config를 비교한다.
- Refresh Token Flow는 별도 시나리오로 테스트한다.
- Security Filter를 끈 테스트는 Authentication Test로 인정하지 않는다.

---

### [FAQ]

Q. Authentication Test는 무엇인가?

A. 인증이 필요한 API가 Token 유무와 Token 유효성에 따라 올바른 응답을 반환하는지 검증하는 테스트이다.

Q. Token 없는 Protected API 요청은 어떤 Status Code여야 하는가?

A. 401 Unauthorized여야 한다.

Q. Public API도 인증 테스트가 필요한가?

A. 필요하다. Token 없이 접근 가능해야 하는 API가 실제로 공개되어 있는지 확인해야 한다.

---

# 11. Authorization Test

## 11.1 Authorization API Test

### [개념]

Authorization Test는 인증된 사용자가 특정 Resource 또는 Action에 접근할 권한이 있는지 검증하는 테스트이다.

Authorization Test는 Role, Permission, Ownership 검증을 포함한다.

```text
Authenticated User
→ Role Check
→ Ownership Check
→ Allow or 403
```

---

### [핵심]

- 권한 없는 사용자는 403을 반환해야 한다.
- ROLE_USER와 ROLE_ADMIN 접근 범위를 검증한다.
- Resource Owner만 수정 / 삭제 가능한지 검증한다.
- 다른 사용자의 Resource 접근을 차단해야 한다.
- Request Body의 userId 조작을 방어해야 한다.
- Method Security와 Service Ownership 검증을 함께 확인한다.
- CSRF 403과 Authorization 403을 구분해야 한다.

---

### [실무]

Authorization Test Case:

| Case                           | Expected        |
| ------------------------------ | --------------- |
| ROLE_USER가 Admin API 호출     | 403             |
| ROLE_ADMIN이 Admin API 호출    | 200             |
| 작성자가 자신의 리뷰 수정      | 200             |
| 다른 사용자가 리뷰 수정        | 403             |
| Request Body userId 조작       | 403 또는 무시   |
| 비공개 Resource 타인 조회      | 403 또는 404    |
| CSRF Token 없이 상태 변경 요청 | 정책에 따라 403 |

Ownership Test 예시:

```java
@Test
void updateReview_notOwner_returns403() throws Exception {
    mockMvc.perform(patch("/api/v1/reviews/10")
                    .with(user("user1").roles("USER"))
                    .contentType(MediaType.APPLICATION_JSON)
                    .content("""
                        {
                          "content": "updated",
                          "rating": 4
                        }
                        """))
            .andExpect(status().isForbidden());
}
```

---

### [주의]

- 인증 성공만으로 권한 성공으로 판단하지 않는다.
- Ownership 검증은 Service Layer에서 수행하는 경우가 많다.
- Admin API는 Security Config와 Method Security를 함께 검증한다.
- Resource 없음과 권한 없음 응답 정책을 문서화한다.
- 403을 500으로 처리하지 않는다.
- CSRF 때문에 발생한 403을 권한 실패로 오판하지 않는다.

---

### [FAQ]

Q. Authorization Test는 무엇인가?

A. 인증된 사용자가 특정 Resource 또는 Action에 접근할 권한이 있는지 검증하는 테스트이다.

Q. 권한 없는 요청은 어떤 Status Code여야 하는가?

A. 403 Forbidden이어야 한다.

Q. Authorization Test에서 가장 중요한 것은 무엇인가?

A. Role 검증, Ownership 검증, Request Body userId 조작 방어이다.

---

# 12. Error Response Test

## 12.1 Error Contract Test

### [개념]

Error Response Test는 API 실패 상황에서 Status Code, Error Code, Error Message, Field Error가 API Contract와 일치하는지 검증하는 테스트이다.

Error Response Test는 Frontend Error Handling 안정성에 직접 연결된다.

```text
Invalid Request
→ Error Response
→ Status Code
→ Error Code
→ Frontend Error Handling
```

---

### [핵심]

- Validation 실패는 400과 Field Error를 반환해야 한다.
- Authentication 실패는 401을 반환해야 한다.
- Authorization 실패는 403을 반환해야 한다.
- Resource 없음은 404를 반환해야 한다.
- Conflict는 409를 반환해야 한다.
- Rate Limit 초과는 429를 반환해야 한다.
- External API Error는 정책에 따라 502 / 503 / 504 또는 500을 반환할 수 있다.
- Server Error는 500과 공통 Error Response를 반환해야 한다.
- 모든 Error Response Schema는 일관되어야 한다.

---

### [실무]

Error Response Test Case:

| 상황               | Expected                           |
| ------------------ | ---------------------------------- |
| Validation 실패    | 400 + VALIDATION_FAILED            |
| Token 없음         | 401 + INVALID_TOKEN                |
| 권한 없음          | 403 + ACCESS_DENIED                |
| Resource 없음      | 404 + \*\_NOT_FOUND                |
| 중복 데이터        | 409 + DUPLICATE\_\*                |
| 이미 처리됨        | 409 + ALREADY\_\*                  |
| Rate Limit 초과    | 429 + RATE_LIMIT_EXCEEDED          |
| Provider 응답 오류 | 502 + EXTERNAL_BAD_RESPONSE        |
| Provider 장애      | 503 + EXTERNAL_SERVICE_UNAVAILABLE |
| Provider Timeout   | 504 + EXTERNAL_TIMEOUT             |
| 예상 못한 오류     | 500 + INTERNAL_SERVER_ERROR        |

MockMvc Error Test 예시:

```java
@Test
void getFestival_notFound_returns404() throws Exception {
    when(festivalService.getFestival(999L))
            .thenThrow(new BusinessException(ErrorCode.FESTIVAL_NOT_FOUND));

    mockMvc.perform(get("/api/v1/festivals/999"))
            .andExpect(status().isNotFound())
            .andExpect(jsonPath("$.code").value("FESTIVAL_NOT_FOUND"));
}
```

Validation Error Test 예시:

```java
@Test
void invalidRequest_returnsValidationFieldErrors() throws Exception {
    mockMvc.perform(post("/api/v1/reviews")
                    .contentType(MediaType.APPLICATION_JSON)
                    .content("""
                        {
                          "rating": 10,
                          "content": ""
                        }
                        """))
            .andExpect(status().isBadRequest())
            .andExpect(jsonPath("$.code").value("VALIDATION_FAILED"))
            .andExpect(jsonPath("$.errors").isArray());
}
```

---

### [주의]

- 실패 테스트를 생략하지 않는다.
- Error Code와 Status Code 의미를 일치시킨다.
- Error Message 문구보다 Error Code를 우선 검증한다.
- Stack Trace가 Response에 노출되지 않는지 확인한다.
- Validation Field Error 구조를 검증한다.
- GlobalExceptionHandler 적용 여부를 확인한다.
- 429, 502, 503, 504는 프로젝트 정책에 맞게 테스트한다.

---

### [FAQ]

Q. Error Response Test는 무엇인가?

A. API 실패 상황에서 Status Code, Error Code, Error Message, Field Error가 Contract와 일치하는지 검증하는 테스트이다.

Q. Error Response Test에서 가장 중요한 것은 무엇인가?

A. Status Code와 Error Code 의미 일치, Error Response Schema 통일, Validation Field Error 제공이다.

Q. Error Message를 테스트에서 강하게 검증해야 하는가?

A. 보통 Error Message보다 Error Code를 우선 검증하는 것이 안정적이다.

---

# 13. Pagination Test

## 13.1 List API Test

### [개념]

Pagination Test는 목록 API가 page, size, sort, cursor, hasNext, totalElements 같은 Pagination Contract를 올바르게 처리하는지 검증하는 테스트이다.

목록 API는 데이터 증가를 전제로 테스트해야 한다.

```text
GET /api/v1/festivals?page=0&size=20&sort=eventStartDate,asc
→ Page Response
```

---

### [핵심]

- page 기본값을 검증한다.
- size 기본값을 검증한다.
- size 최대값을 검증한다.
- sort 기준을 검증한다.
- Page Response Metadata를 검증한다.
- Slice Response hasNext를 검증한다.
- Cursor Response nextCursor를 검증한다.
- 정렬 기준이 없을 때 불안정한 결과를 방지한다.

---

### [실무]

Pagination Test Case:

| Case                | Expected             |
| ------------------- | -------------------- |
| page=0 size=20      | 20개 이하 반환       |
| sort=createdAt,desc | 최신순 정렬          |
| size 최대값 초과    | 제한 또는 400        |
| page 음수           | 400 또는 기본값 처리 |
| 기본 sort 미전달    | 기본 sort 적용       |
| Slice 조회          | hasNext 포함         |
| Cursor 조회         | nextCursor 포함      |

MockMvc Pagination Test 예시:

```java
@Test
void getFestivals_withPagination_returnsPageMetadata() throws Exception {
    mockMvc.perform(get("/api/v1/festivals")
                    .param("page", "0")
                    .param("size", "20")
                    .param("sort", "eventStartDate,asc"))
            .andExpect(status().isOk())
            .andExpect(jsonPath("$.data.content").isArray())
            .andExpect(jsonPath("$.data.page").value(0))
            .andExpect(jsonPath("$.data.size").value(20));
}
```

---

### [주의]

- 목록 API가 List만 반환하는지 확인한다.
- Pagination Metadata 누락을 확인한다.
- 기본 Sort 누락을 확인한다.
- Page와 Slice Response 구조를 혼동하지 않는다.
- Frontend page index와 Backend page index가 일치하는지 확인한다.
- 정렬 기준이 고유하지 않으면 Tie-breaker를 추가한다.

---

### [FAQ]

Q. Pagination Test는 무엇인가?

A. 목록 API가 page, size, sort, cursor, hasNext 같은 Pagination Contract를 올바르게 처리하는지 검증하는 테스트이다.

Q. Pagination Test에서 기본 Sort를 검증해야 하는 이유는 무엇인가?

A. Sort 기준이 없으면 페이지 이동 시 데이터 중복 또는 누락이 발생할 수 있기 때문이다.

Q. 목록 API가 List만 반환하면 어떤 문제가 있는가?

A. 대량 데이터 증가 시 응답 크기와 성능 문제가 발생하고 Frontend Pagination 처리가 어렵다.

---

# 14. Idempotency Test

## 14.1 Duplicate Request Test

### [개념]

Idempotency Test는 같은 요청이 여러 번 들어와도 중복 생성, 중복 결제, 중복 상태 변경이 발생하지 않는지 검증하는 테스트이다.

Idempotency Test는 결제, 주문, 예약, 좋아요, 즐겨찾기, 이메일 발송 API에 중요하다.

```text
Same Request
→ First Success
→ Duplicate Request
→ Same Result or 409 Conflict
```

---

### [핵심]

- POST API는 중복 요청 위험이 있다.
- Idempotency Key 기반 중복 요청을 검증한다.
- Unique Constraint 기반 중복 방지를 검증한다.
- 이미 처리된 상태 요청을 검증한다.
- 중복 요청 정책은 API Contract와 일치해야 한다.
- 중복 요청은 409 Conflict 또는 Idempotent Success로 처리할 수 있다.
- Rate Limit 초과 429와 중복 요청 409를 구분한다.

---

### [실무]

Idempotency Test Case:

| Case                        | Expected                |
| --------------------------- | ----------------------- |
| 같은 Idempotency Key 재요청 | 기존 결과 반환          |
| 같은 Key + 다른 Body        | 409 Conflict            |
| 좋아요 중복 등록            | 409 또는 현재 상태 반환 |
| 즐겨찾기 중복 등록          | 409 또는 현재 상태 반환 |
| 결제 승인 중복 요청         | 기존 승인 결과 반환     |
| 이미 취소된 주문 취소       | 409 또는 현재 상태 반환 |

중복 좋아요 테스트 예시:

```java
@Test
void likeFestival_duplicate_returnsConflict() throws Exception {
    mockMvc.perform(post("/api/v1/festivals/1/likes")
                    .with(user("user1").roles("USER")))
            .andExpect(status().isOk());

    mockMvc.perform(post("/api/v1/festivals/1/likes")
                    .with(user("user1").roles("USER")))
            .andExpect(status().isConflict());
}
```

Idempotency Key 테스트 예시:

```text
POST /api/v1/payments/confirm
Idempotency-Key: abc-123
→ 200 OK

POST /api/v1/payments/confirm
Idempotency-Key: abc-123
→ 200 OK with same response
```

---

### [주의]

- 중복 요청 정책을 먼저 문서화한다.
- DB Unique Constraint와 Service Validation을 함께 검증한다.
- 동시 요청 Race Condition은 별도 테스트가 필요하다.
- 결제 API는 외부 Provider Idempotency 정책도 확인한다.
- 중복 요청을 무조건 500으로 처리하면 안 된다.
- Rate Limiting은 중복 요청 방지가 아니라 요청량 제한이다.

---

### [FAQ]

Q. Idempotency Test는 무엇인가?

A. 같은 요청이 여러 번 들어와도 중복 생성, 중복 결제, 중복 상태 변경이 발생하지 않는지 검증하는 테스트이다.

Q. Idempotency Test가 중요한 API는 무엇인가?

A. 결제, 주문, 예약, 좋아요, 즐겨찾기, 이메일 발송 API이다.

Q. 같은 Idempotency Key로 다른 Body가 오면 무엇을 기대하는가?

A. 보통 409 Conflict를 기대한다.

---

# 15. Rate Limiting Test

## 15.1 429 Too Many Requests Test

### [개념]

Rate Limiting Test는 API가 일정 시간 동안 허용되는 요청 수를 초과했을 때 429 Too Many Requests를 반환하는지 검증하는 테스트이다.

Rate Limiting Test는 Brute Force 방어, 비용 보호, 서버 안정성 검증에 사용된다.

```text
Request Count > Limit
→ 429 Too Many Requests
→ RATE_LIMIT_EXCEEDED
→ Retry-After
```

---

### [핵심]

- Rate Limit 초과는 429를 반환해야 한다.
- Error Code는 `RATE_LIMIT_EXCEEDED`를 사용할 수 있다.
- `Retry-After` Header를 검증할 수 있다.
- Login, Signup, Password Reset API에 중요하다.
- Search, AI Recommendation, External API Proxy에 중요하다.
- 테스트에서 실제 운영 Rate Limit에 과도한 부하를 주지 않아야 한다.
- Rate Limiting Test는 Duplicate Request Test와 다르다.

---

### [실무]

Rate Limiting Test Case:

| Case                    | Expected                  |
| ----------------------- | ------------------------- |
| 제한 이내 요청          | 200 또는 정상 응답        |
| 제한 초과 요청          | 429 + RATE_LIMIT_EXCEEDED |
| Retry-After Header 존재 | Header 포함               |
| 다른 사용자 요청        | 별도 Limit 적용           |
| 다른 IP 요청            | 정책에 따라 별도 Limit    |
| 로그인 실패 반복        | 429 또는 계정 보호 정책   |

MockMvc 개념 예시:

```java
@Test
void login_tooManyRequests_returns429() throws Exception {
    for (int i = 0; i < 10; i++) {
        mockMvc.perform(post("/api/v1/auth/login")
                .contentType(MediaType.APPLICATION_JSON)
                .content(loginRequest));
    }

    mockMvc.perform(post("/api/v1/auth/login")
            .contentType(MediaType.APPLICATION_JSON)
            .content(loginRequest))
        .andExpect(status().isTooManyRequests())
        .andExpect(jsonPath("$.code").value("RATE_LIMIT_EXCEEDED"));
}
```

Postman 검증 예시:

```text
Request login API repeatedly
→ Expected Status: 429
→ Expected Error Code: RATE_LIMIT_EXCEEDED
→ Check Retry-After Header
```

---

### [주의]

- Rate Limit Test는 운영 환경에서 무분별하게 수행하지 않는다.
- 테스트 전용 Limit 값을 낮게 설정할 수 있다.
- IP 기반 Limit은 테스트 환경에서 동일 IP로 인해 의도치 않게 실패할 수 있다.
- User 기반 Limit은 사용자별 격리 여부를 검증한다.
- 429를 403이나 409로 잘못 처리하지 않는다.
- Frontend는 429 발생 시 즉시 재시도 루프를 만들면 안 된다.

---

### [FAQ]

Q. Rate Limiting Test는 무엇인가?

A. API가 요청 한도 초과 시 429 Too Many Requests를 반환하는지 검증하는 테스트이다.

Q. Rate Limit 초과 시 어떤 Status Code를 기대하는가?

A. 429 Too Many Requests를 기대한다.

Q. Rate Limiting Test가 중요한 API는 무엇인가?

A. 로그인, 회원가입, 비밀번호 재설정, 검색, AI 추천, 외부 API Proxy이다.

---

# 16. External API Integration Test

## 16.1 External Provider Test

### [개념]

External API Integration Test는 Backend가 외부 API Provider를 호출하고 오류 상황을 올바르게 처리하는지 검증하는 테스트이다.

Tour API, Kakao Map API, Payment Provider, Email API, AI API 같은 외부 연동은 Timeout, Provider 장애, 응답 형식 오류를 테스트해야 한다.

```text
Backend Service
→ External Provider Client
→ Provider Response
→ Internal DTO Mapping
→ Error Mapping
```

---

### [핵심]

- Provider 정상 응답을 내부 DTO로 Mapping하는지 검증한다.
- Provider 응답 형식 오류를 검증한다.
- Provider Timeout을 검증한다.
- Provider 장애 응답을 검증한다.
- Provider 인증 실패를 검증한다.
- External Error를 502 / 503 / 504 또는 프로젝트 정책 Error로 변환한다.
- Provider 내부 메시지나 Secret을 Client에 노출하지 않는다.

---

### [실무]

External API Error Test Case:

| Case                      | Expected                           |
| ------------------------- | ---------------------------------- |
| Provider 정상 응답        | 200 + Internal DTO                 |
| Provider Bad Response     | 502 + EXTERNAL_BAD_RESPONSE        |
| Provider Unavailable      | 503 + EXTERNAL_SERVICE_UNAVAILABLE |
| Provider Timeout          | 504 + EXTERNAL_TIMEOUT             |
| Provider Auth Fail        | 정책 Error + 민감 정보 제거        |
| Mapping Error             | 500 또는 502 정책                  |
| Payment Duplicate Confirm | 409 또는 Idempotent Success        |

Mock Server 사용 흐름:

```text
Mock External Provider
→ Return Success Response
→ Verify Internal DTO

Mock External Provider
→ Return Timeout
→ Verify 504 or Project Error

Mock External Provider
→ Return Invalid JSON
→ Verify 502 or Project Error
```

Service Test 예시:

```java
@Test
void externalProvider_timeout_returnsExternalTimeout() {
    when(providerClient.getFestivalData())
            .thenThrow(new ExternalTimeoutException());

    BusinessException ex = assertThrows(
            BusinessException.class,
            () -> externalFestivalService.syncFestivals()
    );

    assertThat(ex.getErrorCode()).isEqualTo(ErrorCode.EXTERNAL_TIMEOUT);
}
```

---

### [주의]

- 실제 Provider에 의존하는 테스트는 불안정할 수 있다.
- Mock Server 또는 Stub Client를 사용한다.
- Provider API Key를 테스트 코드에 하드코딩하지 않는다.
- Payment Provider 테스트는 Idempotency와 상태 검증을 함께 수행한다.
- External API Timeout 설정을 검증한다.
- 운영 장애를 유발할 수 있는 반복 호출 테스트를 피한다.

---

### [FAQ]

Q. External API Integration Test는 무엇인가?

A. Backend가 외부 API Provider를 호출하고 정상 응답과 오류 상황을 올바르게 처리하는지 검증하는 테스트이다.

Q. External API 테스트에서 중요한 실패 케이스는 무엇인가?

A. Provider Timeout, Provider 장애, Bad Response, Auth Fail, Mapping Error이다.

Q. 실제 외부 API를 테스트에서 직접 호출해도 되는가?

A. 가능하지만 불안정하고 비용이 발생할 수 있으므로 Mock Server 또는 Stub을 사용하는 것이 좋다.

---

# 17. Regression Test

## 17.1 API Regression Test

### [개념]

Regression Test는 API 수정 후 기존 API Contract와 기존 기능이 깨지지 않았는지 확인하는 테스트이다.

Regression Test는 Breaking Change, Contract Mismatch, Error Response 변경을 탐지하는 데 중요하다.

```text
API Change
→ Existing Test Suite
→ Contract Check
→ Regression Result
```

---

### [핵심]

- Regression Test는 변경 후 기존 기능 보호를 목표로 한다.
- Response Field 삭제를 탐지한다.
- Status Code 변경을 탐지한다.
- Error Code 변경을 탐지한다.
- Authentication / Authorization 변경을 탐지한다.
- Pagination Response 구조 변경을 탐지한다.
- Rate Limit 정책 변경으로 기존 Client가 깨지는지 확인한다.
- Frontend 영향이 큰 API는 우선 테스트한다.

---

### [실무]

Regression Test 대상:

- Login API
- User Me API
- Main Page API
- 목록 조회 API
- 상세 조회 API
- 생성 / 수정 / 삭제 API
- 결제 API
- 알림 API
- 관리자 API
- Rate Limit 대상 API
- External API Proxy
- Frontend 주요 화면 API

Regression Test Checklist:

- 기존 Success Response Field가 유지되는가?
- 기존 Error Code가 유지되는가?
- 기존 Status Code가 유지되는가?
- 기존 인증 조건이 유지되는가?
- 기존 권한 조건이 유지되는가?
- 기존 Pagination 구조가 유지되는가?
- Rate Limit 신규 적용이 기존 Client 호출 패턴을 깨뜨리지 않는가?
- OpenAPI 문서가 변경 사항을 반영하는가?

---

### [FAQ]

Q. Regression Test란 무엇인가?

A. API 수정 후 기존 API Contract와 기능이 깨지지 않았는지 확인하는 테스트이다.

Q. Regression Test가 중요한 이유는 무엇인가?

A. 변경으로 인한 Breaking Change와 기존 화면 오류를 방지하기 위해서이다.

Q. Regression Test에서 가장 먼저 확인할 것은 무엇인가?

A. 기존 Response Field, Status Code, Error Code, 인증/권한 조건 유지 여부이다.

---

# 18. Test Case Template

## 18.1 API Test Case Template

### [개념]

API Test Case Template은 API 테스트 항목을 일관된 형식으로 작성하기 위한 구조이다.

Test Case는 API Contract 검증과 결함 추적을 위해 명확하게 작성해야 한다.

---

### [핵심]

- Test Case는 API 단위로 작성한다.
- 정상 케이스와 실패 케이스를 모두 작성한다.
- Request 조건을 명확히 작성한다.
- Expected Status Code를 작성한다.
- Expected Response를 작성한다.
- Priority를 지정한다.
- 실제 결과와 Pass / Fail을 기록한다.
- Retest 결과를 기록한다.

---

### [실무]

API Test Case Template:

```text
Test ID:
API:
Method:
URI:
Scenario:
Priority:
Precondition:
Request Header:
Path Variable:
Query Parameter:
Request Body:
Expected Status:
Expected Response:
Actual Result:
Pass / Fail:
Defect:
Fix Result:
Retest Result:
```

테스트 케이스 예시:

```text
Test ID: API-REVIEW-001
API: 리뷰 등록
Method: POST
URI: /api/v1/festivals/{festivalId}/reviews
Scenario: 정상 리뷰 등록
Priority: High
Precondition: 로그인된 사용자, 존재하는 festivalId
Request Header: Authorization: Bearer valid-token
Path Variable: festivalId=1
Request Body:
{
  "rating": 5,
  "content": "Great festival"
}
Expected Status: 201 Created or 200 OK
Expected Response: success=true, data.reviewId exists
Actual Result:
Pass / Fail:
Defect:
Fix Result:
Retest Result:
```

실패 케이스 예시:

```text
Test ID: API-REVIEW-002
API: 리뷰 등록
Method: POST
URI: /api/v1/festivals/{festivalId}/reviews
Scenario: rating 범위 초과
Priority: High
Request Body:
{
  "rating": 10,
  "content": "Great festival"
}
Expected Status: 400 Bad Request
Expected Response: code=VALIDATION_FAILED, errors includes rating
```

---

### [FAQ]

Q. API Test Case Template은 왜 필요한가?

A. API 테스트 항목을 일관되게 작성하고 Contract 검증과 결함 추적을 쉽게 하기 위해 필요하다.

Q. Test Case에는 무엇이 포함되어야 하는가?

A. API, Method, URI, Scenario, Request, Expected Status, Expected Response, Actual Result, Pass / Fail이 포함되어야 한다.

Q. 실패 케이스도 작성해야 하는가?

A. 반드시 작성해야 한다. 실패 응답도 API Contract의 일부이다.

---

# 19. Test Priority

## 19.1 Test Priority Rule

### [개념]

Test Priority는 API 테스트 케이스의 중요도와 실행 우선순위를 정의하는 기준이다.

Security, Payment, User Data, Contract Breaking Risk가 높은 API는 우선순위가 높다.

---

### [핵심]

| Priority | 기준                                                          |
| -------- | ------------------------------------------------------------- |
| High     | 인증, 권한, 결제, 사용자 정보, 생성/수정/삭제, Error Contract |
| Medium   | 목록 조회, 검색, Pagination, Filtering, Sorting, External API |
| Low      | 단순 공개 조회, 문서 설명, 부가 정보 조회                     |

---

### [실무]

High Priority Test:

- Login
- Logout
- Token Refresh
- User Me
- Password Reset
- Payment Confirm
- Admin API
- Resource Create
- Resource Update
- Resource Delete
- Ownership Check
- Validation Error
- Authorization Error
- Rate Limit on Login
- Idempotency on Payment

Medium Priority Test:

- List API
- Search API
- Pagination
- Filtering
- Sorting
- Detail API
- File Upload
- External API Proxy
- Rate Limit on Search

Low Priority Test:

- Public Code List
- Public Filter List
- Static Resource API
- Health Check
- Simple Metadata API

---

### [FAQ]

Q. Test Priority는 무엇인가?

A. API 테스트 케이스의 중요도와 실행 우선순위를 정의하는 기준이다.

Q. High Priority API는 무엇인가?

A. 인증, 권한, 결제, 사용자 정보, 생성/수정/삭제, Error Contract 관련 API이다.

Q. 단순 공개 조회 API는 우선순위가 낮은가?

A. 보통 낮지만 메인 화면 핵심 API라면 Medium 또는 High로 올릴 수 있다.

---

# 20. Defect Report

## 20.1 API Defect Report

### [개념]

Defect Report는 API 테스트 또는 Review 중 발견한 결함을 문제, 원인, 영향, 조치 결과로 기록하는 문서이다.

Defect Report는 수정 추적과 재검수에 사용된다.

---

### [핵심]

- 결함은 재현 가능해야 한다.
- 결함은 Expected Result와 Actual Result 차이를 포함한다.
- 결함은 영향도를 포함한다.
- 결함은 원인을 포함한다.
- 결함은 수정 방향을 포함한다.
- 수정 후 Retest 결과를 기록한다.
- Critical Defect는 Release Blocker로 처리한다.

---

### [실무]

Defect Report Template:

```text
Defect ID:
Severity:
API:
Method:
URI:
Scenario:
Expected Result:
Actual Result:
Impact:
Cause:
Fix:
Retest Result:
Status:
```

Defect Report 예시:

```text
Defect ID: DEF-API-001
Severity: Critical
API: 내 정보 조회
Method: GET
URI: /api/v1/users/me
Scenario: Token 없이 요청
Expected Result: 401 Unauthorized
Actual Result: 200 OK with user data
Impact: 인증 없이 개인정보 접근 가능
Cause: Security Config에서 /api/v1/users/** permitAll 처리
Fix: 해당 경로 authenticated 설정으로 변경
Retest Result: Token 없이 401 반환 확인
Status: Closed
```

---

### [FAQ]

Q. Defect Report란 무엇인가?

A. API 테스트 또는 Review 중 발견한 결함을 문제, 원인, 영향, 조치 결과로 기록하는 문서이다.

Q. Defect Report에 반드시 들어가야 하는 것은 무엇인가?

A. Expected Result, Actual Result, Impact, Cause, Fix, Retest Result가 필요하다.

Q. Critical Defect는 어떻게 처리하는가?

A. Release Blocker로 처리하고 수정 후 재검수해야 한다.

---

# 21. Common Mistakes

## 21.1 API Testing Mistakes

### [Troubleshooting]

문제: 정상 케이스만 테스트한다.

원인: 실패 응답도 API Contract라는 인식이 부족하다.

해결: Validation, Authentication, Authorization, Not Found, Conflict, Rate Limit, Server Error 케이스를 포함한다.

---

문제: Swagger UI에서 200만 확인하고 테스트를 끝낸다.

원인: Response Schema, Error Schema, Header, Status Code 검증이 부족하다.

해결: 실제 Response Body와 OpenAPI Schema를 비교하고 실패 응답도 테스트한다.

---

문제: Controller Test에서 Service 로직까지 검증하려 한다.

원인: 테스트 레이어 역할을 구분하지 않았다.

해결: Controller Test는 Mapping / Validation / Response에 집중하고 Service Test는 Business Rule에 집중한다.

---

문제: MockMvc POST 테스트에서 403이 발생해도 권한 문제로만 판단한다.

원인: Spring Security CSRF 설정을 확인하지 않았다.

해결: CSRF 설정, `.with(csrf())`, JWT Stateless Security Config, `addFilters` 설정을 확인한다.

---

문제: `addFilters = false`를 사용하고 Security 테스트가 통과했다고 판단한다.

원인: Security Filter가 제거된 상태에서 인증 / 권한 검증을 수행했다.

해결: Security Test는 Filter를 적용한 상태에서 별도로 수행한다.

---

문제: Service Test에서 권한 검증을 누락한다.

원인: Ownership과 Authorization을 Security Config만으로 해결된다고 판단했다.

해결: Resource Owner 검증과 ACCESS_DENIED 예외 테스트를 추가한다.

---

문제: Pagination Test가 없다.

원인: 목록 API를 단순 List 조회로만 판단했다.

해결: page, size, sort, metadata, hasNext, max size 테스트를 추가한다.

---

문제: Rate Limiting Test가 없다.

원인: Rate Limit을 보안 설정으로만 보고 API Contract 테스트에 포함하지 않았다.

해결: 429 Too Many Requests, RATE_LIMIT_EXCEEDED, Retry-After Header를 테스트한다.

---

문제: External API 오류 테스트가 없다.

원인: Provider가 항상 정상 응답한다고 가정했다.

해결: Timeout, Bad Response, Provider Unavailable, Auth Fail 테스트를 추가한다.

---

문제: Error Code를 테스트하지 않는다.

원인: Status Code만 검증하고 Frontend Error Handling 기준을 놓쳤다.

해결: Error Code와 Error Response Schema를 테스트한다.

---

문제: Frontend 연동 오류를 Backend 문제로만 본다.

원인: Axios URL, Proxy, Base URL, Response Field Mapping을 함께 확인하지 않았다.

해결: Browser Network Tab에서 Request와 Response를 확인하고 Frontend 사용 Field를 비교한다.

---

문제: API 변경 후 Regression Test를 하지 않는다.

원인: 기존 Client 영향도를 검토하지 않았다.

해결: 기존 주요 API의 Response Field, Status Code, Error Code, Security 조건을 재검증한다.

---

### [FAQ]

Q. API Testing에서 가장 흔한 실수는 무엇인가?

A. 정상 케이스만 테스트하고 실패 응답, Security, Error Response, Pagination을 누락하는 것이다.

Q. API 테스트에서 Status Code만 확인하면 충분한가?

A. 충분하지 않다. Response Body Schema, Error Code, Field Error, Security 조건도 확인해야 한다.

Q. API 변경 후 반드시 해야 할 테스트는 무엇인가?

A. Regression Test와 Contract Verification을 수행해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. API Testing이란 무엇인가?
A. API가 Request / Response Contract, Status Code, Error Response, Security Contract를 만족하는지 검증하는 과정이다.

Q. API Testing에서 가장 중요한 것은 무엇인가?
A. 정상 응답뿐 아니라 실패 응답, Error Response, 인증/권한 조건까지 검증하는 것이다.

Q. Controller Test는 무엇을 검증하는가?
A. Request Mapping, Parameter Binding, Validation, Status Code, Response Body를 검증한다.

Q. Controller Test에서 Service는 실제 객체를 사용하는가?
A. 보통 Mock 객체를 사용해 Controller Contract에 집중한다.

Q. MockMvc POST 테스트에서 403이 발생하면 무엇을 확인해야 하는가?
A. CSRF 설정, Security Filter, 인증 정보, 권한 설정을 확인해야 한다.

Q. JWT Stateless API에서 CSRF는 보통 어떻게 처리하는가?
A. 보통 CSRF를 비활성화한다.

Q. `@AutoConfigureMockMvc(addFilters = false)`를 사용해도 되는가?
A. Controller Contract 테스트에는 사용할 수 있지만 Security 검증에는 부적합하다.

Q. Service Test는 무엇을 검증하는가?
A. Business Logic, Business Validation, Ownership, Exception Flow, Transaction Rule을 검증한다.

Q. Repository Test는 무엇을 검증하는가?
A. DB Query, Entity Mapping, Pagination, Filtering, Sorting, Constraint를 검증한다.

Q. Swagger UI Test는 무엇인가?
A. OpenAPI 문서를 기반으로 API를 직접 호출해 Contract를 확인하는 수동 테스트이다.

Q. Postman Test는 무엇인가?
A. API를 시나리오 단위로 호출하고 Environment, Token, Test Script로 검증하는 테스트 방식이다.

Q. Swagger UI와 Postman의 차이는 무엇인가?
A. Swagger UI는 문서 기반 테스트에 강하고 Postman은 시나리오 기반 테스트와 환경 관리에 강하다.

Q. Contract Verification이란 무엇인가?
A. API 문서, Backend 구현, Frontend 기대 구조, 실제 Network Response가 일치하는지 검증하는 과정이다.

Q. Contract Verification에서 비교해야 할 대상은 무엇인가?
A. OpenAPI 문서, Controller, DTO, 실제 Response, Frontend Type, Error Handling이다.

Q. Frontend Integration Test는 무엇인가?
A. 실제 Frontend 화면에서 API 호출과 Response UI 반영이 정상인지 검증하는 테스트이다.

Q. Frontend API 오류에서 가장 먼저 확인할 것은 무엇인가?
A. Browser Network Tab의 Request URL, Method, Header, Payload, Status Code, Response Body이다.

Q. Authentication Test는 무엇인가?
A. 인증이 필요한 API가 Token 유무와 Token 유효성에 따라 올바른 응답을 반환하는지 검증하는 테스트이다.

Q. Token 없는 Protected API 요청은 어떤 Status Code여야 하는가?
A. 401 Unauthorized여야 한다.

Q. Authorization Test는 무엇인가?
A. 인증된 사용자가 특정 Resource 또는 Action에 접근할 권한이 있는지 검증하는 테스트이다.

Q. 권한 없는 요청은 어떤 Status Code여야 하는가?
A. 403 Forbidden이어야 한다.

Q. Authorization Test에서 가장 중요한 것은 무엇인가?
A. Role 검증, Ownership 검증, Request Body userId 조작 방어이다.

Q. Error Response Test는 무엇인가?
A. API 실패 상황에서 Status Code, Error Code, Error Message, Field Error가 Contract와 일치하는지 검증하는 테스트이다.

Q. Error Response Test에서 중요한 것은 무엇인가?
A. Status Code와 Error Code 의미 일치, Error Response Schema 통일, Validation Field Error 제공이다.

Q. Pagination Test는 무엇인가?
A. 목록 API가 page, size, sort, cursor, hasNext 같은 Pagination Contract를 올바르게 처리하는지 검증하는 테스트이다.

Q. Idempotency Test는 무엇인가?
A. 같은 요청이 여러 번 들어와도 중복 생성, 중복 결제, 중복 상태 변경이 발생하지 않는지 검증하는 테스트이다.

Q. Rate Limiting Test는 무엇인가?
A. API가 요청 한도 초과 시 429 Too Many Requests를 반환하는지 검증하는 테스트이다.

Q. Rate Limit 초과 시 어떤 Status Code를 기대하는가?
A. 429 Too Many Requests를 기대한다.

Q. External API Integration Test는 무엇인가?
A. Backend가 외부 API Provider를 호출하고 정상 응답과 오류 상황을 올바르게 처리하는지 검증하는 테스트이다.

Q. External API 테스트에서 중요한 실패 케이스는 무엇인가?
A. Provider Timeout, Provider 장애, Bad Response, Auth Fail, Mapping Error이다.

Q. Regression Test란 무엇인가?
A. API 수정 후 기존 API Contract와 기능이 깨지지 않았는지 확인하는 테스트이다.

Q. API Test Case Template은 왜 필요한가?
A. API 테스트 항목을 일관되게 작성하고 Contract 검증과 결함 추적을 쉽게 하기 위해 필요하다.

Q. Test Case에는 무엇이 포함되어야 하는가?
A. API, Method, URI, Scenario, Request, Expected Status, Expected Response, Actual Result, Pass / Fail이 포함되어야 한다.

Q. Test Priority는 무엇인가?
A. API 테스트 케이스의 중요도와 실행 우선순위를 정의하는 기준이다.

Q. High Priority API는 무엇인가?
A. 인증, 권한, 결제, 사용자 정보, 생성/수정/삭제, Error Contract 관련 API이다.

Q. Defect Report란 무엇인가?
A. API 테스트 또는 Review 중 발견한 결함을 문제, 원인, 영향, 조치 결과로 기록하는 문서이다.

Q. Critical Defect는 어떻게 처리하는가?
A. Release Blocker로 처리하고 수정 후 재검수해야 한다.

Q. API Testing에서 가장 흔한 실수는 무엇인가?
A. 정상 케이스만 테스트하고 실패 응답, Security, Error Response, Pagination을 누락하는 것이다.

Q. API 변경 후 반드시 해야 할 테스트는 무엇인가?
A. Regression Test와 Contract Verification을 수행해야 한다.
