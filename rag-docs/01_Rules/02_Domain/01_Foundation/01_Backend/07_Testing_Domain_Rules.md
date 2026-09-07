# Testing Domain Rules

---

# 1. Domain Purpose

Testing Domain 문서는 Backend Agent / Review Agent용 RAG 문서이다.

목적:

- Test Code Generation Support
- Test Strategy Retrieval
- Code Review Support
- Failure Case Detection
- Regression Prevention Support

우선순위:

1. Unit Test Generation
2. Service / Repository / Controller Test
3. Integration Test
4. Testcontainers 기반 실전 검증

---

# 2. Scope

포함 범위:

- Unit Test
- JUnit 5
- AssertJ
- Mockito
- MockBean
- Repository Test
- Service Test
- Controller Test
- Integration Test
- SpringBootTest
- WebMvcTest
- DataJpaTest
- Testcontainers
- Test Fixture
- Test Profile
- Security Test
- Validation Test
- Exception Test

---

# 3. Section Priority

## Required

- [개념]
- [핵심]
- [실무]
- [FAQ]

---

## Strongly Recommended

- [Flow]
- [예제]
- [주의]
- [Best Practice]

---

## Optional

- [Checklist]
- [Troubleshooting]
- [Comparison]

---

# 4. Testing Core Rules

Testing 문서는 Test 목적과 Test 대상 중심으로 작성.

핵심 구조:

- Test Target
- Test Scope
- Test Tool
- Test Data
- Assertion
- Failure Case

---

반드시 설명 포함:

- 무엇을 테스트하는가
- 왜 테스트하는가
- 어떤 도구를 사용하는가
- 어떤 실패 케이스를 검증하는가

---

예:

```text
Requirement
→ Test Case
→ Test Data
→ Execute
→ Assertion
→ Regression Protection
```

---

# 5. Unit Test Rules

Unit Test 문서는 Spring Context 없이 빠르게 검증하는 구조 중심.

필수 포함:

- Service Logic
- Domain Logic
- Validator
- Mapper
- Policy Class

---

권장 도구:

- JUnit 5
- AssertJ
- Mockito

---

예:

```java
@ExtendWith(MockitoExtension.class)
class UserServiceTest {
}
```

---

중요:

Unit Test는 빠르고 독립적이어야 한다.

금지:

- 불필요한 SpringBootTest 사용
- 외부 API 실제 호출
- 실제 DB 의존

---

# 6. JUnit 5 Rules

필수 포함:

- @Test
- @DisplayName
- @BeforeEach
- @Nested
- @ParameterizedTest

---

예:

```java
@Test
@DisplayName("회원 조회 성공")
void findUser_success() {
}
```

---

반드시 설명:

- Test Method 이름 규칙
- given / when / then 구조
- 실패 케이스 작성 방식

---

# 7. AssertJ Rules

AssertJ 문서는 Assertion 가독성 중심.

필수 포함:

- assertThat
- assertThatThrownBy
- isEqualTo
- hasSize
- contains
- isInstanceOf

---

예:

```java
assertThat(response.email()).isEqualTo("user@test.com");
```

---

예외 검증:

```java
assertThatThrownBy(() -> userService.findUser(1L))
        .isInstanceOf(UserNotFoundException.class);
```

---

# 8. Mockito Rules

Mockito 문서는 Mock 기반 의존성 격리 중심.

필수 포함:

- @Mock
- @InjectMocks
- given / willReturn
- when / thenReturn
- verify
- never
- any
- ArgumentCaptor

---

예:

```java
given(userRepository.findById(1L))
        .willReturn(Optional.of(user));
```

---

반드시 설명:

- Mock 역할
- Stubbing 의미
- verify 사용 기준

---

금지:

- 과도한 Mock
- 구현 세부사항에 강하게 결합된 Test

---

# 9. Service Test Rules

Service Test는 Business Logic 검증 중심.

필수 포함:

- 성공 케이스
- 실패 케이스
- Repository 호출 검증
- Exception 검증
- Transaction 영향 설명

---

예:

```java
@ExtendWith(MockitoExtension.class)
class UserServiceTest {

    @Mock
    private UserRepository userRepository;

    @InjectMocks
    private UserService userService;
}
```

---

중요:

Service Test는 Backend Agent가 가장 자주 생성해야 하는 Test이다.

---

# 10. Repository Test Rules

Repository Test는 Query와 Mapping 검증 중심.

필수 포함:

- @DataJpaTest
- Query Method
- JPQL
- Entity Mapping
- Constraint
- Test Data

---

예:

```java
@DataJpaTest
class UserRepositoryTest {
}
```

---

반드시 설명:

- H2와 운영 DB 차이
- Testcontainers 필요 상황
- Transaction Rollback

---

# 11. Controller Test Rules

Controller Test는 API Entry 검증 중심.

필수 포함:

- @WebMvcTest
- MockMvc
- Request Binding
- Validation
- Status Code
- Response Body
- Exception Handler

---

예:

```java
@WebMvcTest(UserController.class)
class UserControllerTest {
}
```

---

반드시 설명:

- Service는 MockBean으로 대체
- Controller Layer만 검증
- API 계약 검증

---

# 12. MockMvc Rules

필수 포함:

- perform
- get / post / put / patch / delete
- status
- jsonPath
- contentType
- request body

---

예:

```java
mockMvc.perform(get("/users/1"))
        .andExpect(status().isOk())
        .andExpect(jsonPath("$.data.email").value("user@test.com"));
```

---

중요:

REST API Test는 Request / Response 계약 검증 중심.

---

# 13. Integration Test Rules

Integration Test는 여러 Layer 연결 검증 중심.

필수 포함:

- @SpringBootTest
- 실제 Bean
- DB 연동
- Security 연동
- External Client Mock

---

예:

```java
@SpringBootTest
class UserIntegrationTest {
}
```

---

주의:

@SpringBootTest 남용 금지.

핵심 Flow 검증에 사용.

---

# 14. Testcontainers Rules

Testcontainers 문서는 실제 Infrastructure 검증 중심.

필수 포함:

- MySQLContainer
- PostgreSQLContainer
- RedisContainer
- LocalStack
- DynamicPropertySource

---

예:

```java
@Testcontainers
@SpringBootTest
class RepositoryIntegrationTest {
}
```

---

반드시 설명:

- 운영 DB와 유사한 테스트
- H2 차이 문제 해결
- CI 실행 비용

---

# 15. Test Fixture Rules

Fixture 문서는 테스트 데이터 생성 중심.

필수 포함:

- Fixture Class
- Test Data Builder
- Object Mother
- 중복 제거

---

예:

```java
public class UserFixture {

    public static User user(String email) {
        return new User(email);
    }
}
```

---

주의:

Fixture가 너무 복잡하면 테스트 의도가 흐려진다.

---

# 16. Test Profile Rules

필수 포함:

- application-test.yml
- @ActiveProfiles("test")
- Test DB
- Test Redis
- Test Secret

---

예:

```java
@ActiveProfiles("test")
@SpringBootTest
class IntegrationTest {
}
```

---

중요:

운영 Secret을 테스트에서 사용하지 않는다.

---

# 17. Security Test Rules

필수 포함:

- spring-security-test
- @WithMockUser
- 인증 성공
- 미인증 요청
- 권한 부족
- 401 / 403

---

예:

```java
@WithMockUser(roles = "ADMIN")
@Test
void adminApi_success() {
}
```

---

반드시 설명:

- Authentication Test
- Authorization Test
- Security Filter 적용 여부

---

# 18. Validation Test Rules

필수 포함:

- @Valid
- Bean Validation
- MethodArgumentNotValidException
- ErrorResponse

---

예:

```java
mockMvc.perform(post("/users")
        .contentType(MediaType.APPLICATION_JSON)
        .content("{}"))
        .andExpect(status().isBadRequest());
```

---

중요:

Validation 실패 케이스는 Controller Test에 반드시 포함.

---

# 19. Exception Test Rules

필수 포함:

- CustomException
- GlobalExceptionHandler
- ErrorCode
- ErrorResponse

---

반드시 검증:

- HTTP Status
- Error Code
- Error Message
- Response Schema

---

예:

```java
.andExpect(jsonPath("$.code").value("USER_NOT_FOUND"));
```

---

# 20. Test Strategy Rules

문서에는 Test Pyramid 관점 포함.

기본 전략:

```text
Unit Test 많이
Slice Test 적절히
Integration Test 핵심 Flow만
E2E Test 최소화
```

---

반드시 설명:

- 어떤 테스트를 어디까지 작성할지
- Test Scope 경계
- 테스트 비용과 속도

---

# 21. Troubleshooting Rules

반드시 포함 추천.

예:

- Mock Not Working
- WebMvcTest Bean Error
- DataJpaTest Failure
- H2 Dialect Issue
- Testcontainers Start Failed
- Security Test 401 / 403
- Flaky Test

---

형식:

문제:

원인:

해결:

---

# 22. Retrieval Optimization Rules

강조 대상:

- JUnit 5
- AssertJ
- Mockito
- MockMvc
- WebMvcTest
- DataJpaTest
- SpringBootTest
- Testcontainers
- WithMockUser
- Test Fixture

키워드 반복 허용.

---

# 23. Version Rules

기준:

- Java 21
- Spring Boot 3.x
- JUnit 5
- Mockito 5.x
- AssertJ
- Spring Security 6
- Testcontainers

---

Legacy 제외:

- JUnit 4 중심 설명
- @RunWith 중심 설명
- 구식 Spring Test 방식

---

# 24. Common Mistakes

자주 발생:

- @SpringBootTest 남용
- Mock 과도 사용
- 실패 케이스 누락
- Validation Test 누락
- Security Test 누락
- H2와 운영 DB 차이 무시
- Test Fixture 과복잡화
- 테스트 순서 의존
- 외부 API 실제 호출
- Flaky Test 방치

---

# 25. Final Goal

Testing RAG 문서는 Agent가 아래 수행 가능해야 한다.

- Retrieve Test Pattern
- Generate Unit Test
- Generate Controller Test
- Generate Repository Test
- Generate Integration Test
- Review Test Quality
- Find Missing Failure Cases
- Suggest Test Improvements

문서 품질이 Review Agent 품질을 결정한다.
