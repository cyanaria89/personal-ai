# Testing Part 05 - Controller Test

---

# 1. Controller Test Core

## 1.1 Controller Test Overview

### [개념]

Controller Test는 API Entry Layer를 검증하는 테스트다.

주요 목적:

- Request Validation
- Response Validation
- API Contract Validation
- Exception Response Validation

---

### [핵심]

검증 대상:

- Request Binding
- Validation
- HTTP Status
- Response Body
- Exception Handler
- Security Response

---

### [실무]

2026 Spring Boot 실무 기준 Controller Test는 FE-BE API 계약 검증의 핵심이다.

특히 중요:

- REST API Contract
- Validation Failure
- Error Response Schema
- Security Response

---

### [FAQ]

Q. Controller Test란?
A. API Entry Layer를 검증하는 테스트다.

Q. Controller Test 핵심은?
A. Request / Response 계약 검증이다.

---

# 2. Controller Test Scope

## 2.1 Test Target

### [개념]

Controller Layer만 집중 검증한다.

---

### [핵심]

포함:

- Controller
- Request Binding
- Validation
- Response Schema

제외:

- Service Logic
- Repository Query
- Database

---

### [FAQ]

Q. Service Logic도 검증하는가?
A. 아니다. Controller Layer만 검증한다.

---

# 3. Core Annotation

## 3.1 @WebMvcTest

### [개념]

@WebMvcTest는 Web Layer만 로드한다.

---

### [핵심]

포함:

- Controller
- MockMvc
- MVC Config
- Validation

제외:

- Service
- Repository
- Database

---

### [예제]

```java
@WebMvcTest(UserController.class)
class UserControllerTest {
}
```

---

### [Flow]

```text
Load Web Layer
→ Perform Request
→ Validate Response
```

---

### [FAQ]

Q. Controller Test에서 SpringBootTest가 필요한가?
A. 대부분 필요 없다. WebMvcTest가 더 적합하다.

---

# 4. MockMvc

## 4.1 API Simulation

### [개념]

MockMvc는 HTTP 요청을 시뮬레이션하는 테스트 도구다.

---

### [핵심]

지원:

- GET
- POST
- PUT
- PATCH
- DELETE

---

### [FAQ]

Q. MockMvc란?
A. 실제 서버 실행 없이 HTTP 요청 테스트가 가능한 도구다.

---

# 5. Request Test

## 5.1 Request Validation

### [개념]

Request Binding과 Payload 검증.

---

### [핵심]

검증 대상:

- Path Variable
- Query Parameter
- Request Body
- Content Type

---

### [예제]

```java
mockMvc.perform(post("/users")
        .contentType(MediaType.APPLICATION_JSON)
        .content("""
        {
            "email":"user@test.com"
        }
        """))
        .andExpect(status().isOk());
```

---

### [FAQ]

Q. Controller Test에서 Request는 무엇을 검증하는가?
A. Binding, Payload, ContentType을 검증한다.

---

# 6. Response Test

## 6.1 Response Validation

### [개념]

Response JSON 구조 검증.

---

### [핵심]

검증 대상:

- Status
- Response Body
- JSON Schema
- Field Value

---

### [예제]

```java
.andExpect(status().isOk())
.andExpect(jsonPath("$.data.email")
        .value("user@test.com"));
```

---

### [FAQ]

Q. Response Body는 어떻게 검증하는가?
A. jsonPath로 검증한다.

---

# 7. Validation Test

## 7.1 Invalid Request

### [개념]

Validation 실패 케이스 검증.

---

### [핵심]

검증 대상:

- @NotNull
- @NotBlank
- @Size
- @Email

---

### [예제]

```java
mockMvc.perform(post("/users")
        .contentType(MediaType.APPLICATION_JSON)
        .content("{}"))
        .andExpect(status().isBadRequest());
```

---

### [FAQ]

Q. Validation 실패 케이스도 필요한가?
A. 반드시 필요하다.

---

# 8. Exception Test

## 8.1 Exception Response

### [개념]

GlobalExceptionHandler 응답 검증.

---

### [핵심]

검증 대상:

- HTTP Status
- Error Code
- Error Message
- Response Schema

---

### [예제]

```java
.andExpect(status().isNotFound())
.andExpect(jsonPath("$.code")
        .value("USER_NOT_FOUND"));
```

---

### [FAQ]

Q. Exception Response도 검증해야 하는가?
A. 반드시 검증해야 한다.

---

# 9. Security Test

## 9.1 Authentication & Authorization

### [개념]

Security 적용 API 검증.

---

### [핵심]

검증 대상:

- Authenticated Request
- Unauthenticated Request
- Forbidden Request
- Role Access

---

### [예제]

```java
@WithMockUser(roles = "USER")
@Test
void userApi_success() {
}
```

---

### [FAQ]

Q. 인증 실패는 어떻게 테스트하는가?
A. 401 Unauthorized 응답 검증.

Q. 권한 부족은 어떻게 테스트하는가?
A. 403 Forbidden 응답 검증.

---

# 10. Controller Test Rules

## 10.1 Best Practice

### [Best Practice]

권장:

- API별 테스트 작성
- Validation 포함
- Exception 포함
- Security 포함

---

### [주의]

금지:

- Service Logic 검증
- DB 접근
- Full Context 남용

---

### [Checklist]

- Request 검증
- Response 검증
- Validation 검증
- Exception 검증
- Security 검증

---

# 11. Common Mistakes

## 11.1 Frequent Issues

### [Troubleshooting]

문제:

Bean Load Error

원인:

Mock Bean 누락

해결:

Dependency 확인

---

문제:

401 발생

원인:

Security 설정

해결:

Authentication 조건 확인

---

문제:

Validation 테스트 실패

원인:

잘못된 Payload

해결:

Request 확인

---

# 12. Agent Decision Rules

## 12.1 Test Routing

### [Flow]

```text
API Contract Validation
→ Controller Test

Validation Failure Test
→ Controller Test

Security Response Test
→ Controller Test

Business Logic Validation
→ Service Test
```

---

### [핵심]

Backend Agent Routing 기준.

---

### [FAQ]

Q. 언제 Controller Test를 생성해야 하는가?
A. API 계약 검증이 필요할 때다.

---

# Retrieval Queries

### [FAQ]

Q. Controller Test란?
A. API Entry Layer 테스트다.

Q. Controller Test 핵심 Annotation은?
A. @WebMvcTest.

Q. Controller Test 핵심 도구는?
A. MockMvc.

Q. Controller Test에서 중요한 것은?
A. Request / Response 계약 검증.

Q. Security Test도 포함해야 하나?
A. 보안 API는 반드시 포함해야 한다.

Q. @MockBean과 @MockitoBean 차이는?
A. Spring Boot 3.4+부터 MockitoBean이 추가되었지만
실무에서는 MockBean도 많이 사용한다.
