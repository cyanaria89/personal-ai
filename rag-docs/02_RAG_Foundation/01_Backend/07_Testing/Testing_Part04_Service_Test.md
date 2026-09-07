# Testing Part 04 - Service Test

---

# 1. Service Test Core

## 1.1 Service Test Overview

### [개념]

Service Test는 Business Logic Layer를 검증하는 테스트다.

주요 목적:

- Business Logic Validation
- Rule Validation
- Failure Case Detection
- Regression Prevention

---

### [핵심]

검증 대상:

- Service Logic
- Domain Rule
- Validation Logic
- Exception Handling
- Transaction Boundary

---

### [실무]

2026 Spring Boot 실무 기준 Service Test는 Backend Agent가 가장 많이 생성하는 테스트다.

핵심 이유:

- Business Logic 집중
- 조건 분기 많음
- Failure Case 빈번

---

### [FAQ]

Q. Service Test란?
A. Business Logic Layer를 검증하는 테스트다.

Q. Service Test 핵심은?
A. Business Logic과 Failure Case 검증이다.

---

# 2. Service Test Scope

## 2.1 Test Target

### [개념]

Service Layer만 집중 검증한다.

---

### [핵심]

포함:

- Business Logic
- Domain Validation
- Rule Engine
- Transaction Logic

제외:

- Request Binding
- DB Query Validation
- HTTP Layer

---

### [FAQ]

Q. Repository Query도 Service Test 대상인가?
A. 아니다. Query는 Repository Test 대상이다.

---

# 3. Service Test Structure

## 3.1 Standard Flow

### [Flow]

```text
Test Data Setup
→ Dependency Mock
→ Execute Service
→ Assert Result
```

---

### [핵심]

기본 구조:

- Input Setup
- Dependency Isolation
- Service Execute
- Result Validation

---

### [FAQ]

Q. Service Test 기본 구조는?
A. Setup → Execute → Assert 구조다.

---

# 4. Success Case

## 4.1 Happy Path

### [개념]

정상 흐름 검증.

---

### [핵심]

검증 대상:

- Return Value
- State Change
- Expected Result

---

### [예제]

```java
User result = userService.findUser(1L);

assertThat(result).isNotNull();
assertThat(result.getEmail())
        .isEqualTo("user@test.com");
```

---

### [FAQ]

Q. Success Case는 무엇을 검증하는가?
A. 정상 입력에 대한 예상 결과를 검증한다.

---

# 5. Failure Case

## 5.1 Exception Path

### [개념]

예외 흐름 검증.

---

### [핵심]

필수 검증:

- Null Input
- Invalid Input
- Not Found
- Duplicate
- Unauthorized

---

### [예제]

```java
assertThatThrownBy(() ->
        userService.findUser(999L))
        .isInstanceOf(UserNotFoundException.class);
```

---

### [FAQ]

Q. Failure Case가 중요한 이유는?
A. 실무 버그 대부분이 예외 처리 누락에서 발생하기 때문이다.

---

# 6. Business Rule Test

## 6.1 Rule Validation

### [개념]

도메인 규칙 검증.

---

### [핵심]

예:

- 할인 정책
- 권한 정책
- 상태 전이 규칙
- 포인트 계산

---

### [FAQ]

Q. Service Test에서 Rule 검증도 중요한가?
A. 매우 중요하다. 핵심 비즈니스 로직이기 때문이다.

---

# 7. Transaction Logic

## 7.1 Transaction Boundary

### [개념]

Service Layer는 Transaction Boundary가 자주 위치한다.

---

### [핵심]

검증 대상:

- Save Flow
- Update Flow
- Delete Flow
- Rollback Trigger

---

### [FAQ]

Q. Transaction Logic도 Service Test 대상인가?
A. Business Rule 관점에서는 포함된다.

---

# 8. External Dependency

## 8.1 External Client Isolation

### [개념]

외부 시스템 의존성은 격리해야 한다.

---

### [핵심]

대상:

- Payment API
- Mail Client
- Redis
- Kafka
- External API

---

### [FAQ]

Q. 외부 API도 Service Test에서 호출하는가?
A. 아니다. 반드시 격리해야 한다.

---

# 9. Service Test Rules

## 9.1 Best Practice

### [Best Practice]

권장:

- Service 단위 테스트
- Success + Failure 모두 작성
- Business Rule 중심
- 독립 실행 가능

---

### [주의]

금지:

- Controller 로직 포함
- DB Query 검증 포함
- 과도한 Integration

---

### [Checklist]

- Success Case 작성
- Failure Case 작성
- Rule 검증
- Boundary 검증

---

# 10. Common Mistakes

## 10.1 Frequent Issues

### [Troubleshooting]

문제:

Success Case만 작성

원인:

Failure Case 누락

해결:

예외 케이스 추가

---

문제:

테스트 느림

원인:

불필요한 Context Loading

해결:

Service Layer 집중

---

문제:

회귀 버그

원인:

Rule Test 부족

해결:

Business Rule 강화

---

# 11. Agent Decision Rules

## 11.1 Test Routing

### [Flow]

```text
Business Logic Validation
→ Service Test

Rule Validation
→ Service Test

Query Validation
→ Repository Test

API Contract Validation
→ Controller Test
```

---

### [핵심]

Backend Agent Routing 기준.

---

### [FAQ]

Q. 언제 Service Test를 생성해야 하는가?
A. Business Logic과 Rule 검증이 필요할 때다.

---

# Retrieval Queries

### [FAQ]

Q. Service Test란?
A. Business Logic Layer 테스트다.

Q. Service Test 핵심 검증은?
A. Business Logic, Rule, Failure Case.

Q. Service Test에서 중요한 것은?
A. Success Case와 Failure Case.

Q. Query 검증도 포함되는가?
A. 아니다. Repository Test 대상이다.

Q. 언제 Service Test를 사용하는가?
A. Business Logic 검증이 필요할 때.
