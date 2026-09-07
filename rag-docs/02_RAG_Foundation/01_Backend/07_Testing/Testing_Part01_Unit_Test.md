# Testing Part 01 - Unit Test

---

# 1. Unit Test Core

## 1.1 Unit Test Overview

### [개념]

Unit Test는 애플리케이션의 가장 작은 테스트 가능한 단위를 독립적으로 검증하는 테스트다.

Testing Domain에서 Unit은 주로 아래를 의미한다.

- Service Logic
- Domain Logic
- Validator
- Mapper
- Policy Class
- Utility Class

---

### [핵심]

목표:

- Business Logic Validation
- Failure Case Detection
- Regression Prevention

특징:

- Fast
- Independent
- Isolated

---

### [실무]

2026 Spring Boot 실무 기준 Unit Test는 테스트 피라미드에서 가장 높은 비중을 차지한다.

---

### [FAQ]

Q. Unit Test란?
A. 가장 작은 로직 단위를 독립적으로 검증하는 테스트다.

Q. Unit Test에서 중요한 것은?
A. 빠른 실행, 독립성, Failure Case 검증이다.

---

# 2. Unit Test Scope

## 2.1 Test Target

### [개념]

Unit Test는 외부 의존성이 없는 순수 로직 검증이 핵심이다.

---

### [핵심]

적합:

- Business Logic
- Calculation Logic
- Validation Logic
- Rule Engine

비적합:

- DB Query
- HTTP Request
- External API
- Infrastructure

---

### [FAQ]

Q. DB가 필요한 테스트도 Unit Test인가?
A. 아니다. DB가 필요하면 Repository Test 또는 Integration Test다.

---

# 3. Test Pyramid

## 3.1 Test Strategy

### [개념]

Testing 전략은 Test Pyramid 기반으로 설계한다.

---

### [Flow]

```text
Unit Test (Most)
→ Slice Test
→ Integration Test
→ E2E Test (Least)
```

---

### [핵심]

권장 비율:

- Unit Test 많이
- Slice Test 적절히
- Integration Test 핵심만
- E2E 최소화

---

### [FAQ]

Q. 왜 Unit Test를 가장 많이 작성해야 하나?
A. 가장 빠르고 비용이 낮으며 회귀 방지 효율이 높기 때문이다.

---

# 4. Unit Test Structure

## 4.1 Given When Then

### [개념]

Unit Test는 Given / When / Then 구조를 권장한다.

---

### [Flow]

```text
Given
→ Test Data Setup

When
→ Execute Method

Then
→ Assertion
```

---

### [핵심]

- Given → 데이터 준비
- When → 로직 실행
- Then → 결과 검증

---

### [예제]

```java
@Test
void calculate_discount_success() {
    // given

    // when

    // then
}
```

---

### [FAQ]

Q. Given When Then은 필수인가?
A. 필수는 아니지만 가독성과 유지보수성이 크게 향상된다.

---

# 5. Success Case

## 5.1 Happy Path

### [개념]

정상 흐름 검증.

---

### [핵심]

검증 대상:

- Correct Output
- Correct State
- Expected Flow

---

### [FAQ]

Q. Success Case만 테스트하면 충분한가?
A. 아니다. Failure Case도 반드시 작성해야 한다.

---

# 6. Failure Case

## 6.1 Exception Path

### [개념]

예외 흐름 검증.

---

### [핵심]

필수 검증:

- Null Input
- Invalid Input
- Boundary Value
- Exception

---

### [FAQ]

Q. Failure Case는 왜 중요한가?
A. 실무 버그 대부분은 예외 처리 누락에서 발생한다.

---

# 7. Boundary Test

## 7.1 Edge Case

### [개념]

경계값 테스트.

---

### [핵심]

예:

- 0
- 1
- MAX
- MIN
- Empty String
- Null

---

### [FAQ]

Q. Boundary Test는 언제 필요한가?
A. 입력 범위 제한이 있는 로직에서 매우 중요하다.

---

# 8. Unit Test Rules

## 8.1 Best Practice

### [Best Practice]

권장:

- 하나의 테스트 = 하나의 목적
- 독립 실행 가능
- 빠른 실행
- 명확한 Assertion

---

### [주의]

금지:

- SpringBootTest 사용
- 실제 DB 접근
- 외부 API 호출
- 테스트 순서 의존

---

### [Checklist]

- 목적이 명확한가
- Success Case 작성
- Failure Case 작성
- Boundary Test 필요한가

---

# 9. Common Mistakes

## 9.1 Frequent Issues

### [Troubleshooting]

문제:

테스트가 느리다

원인:

불필요한 Context Loading

해결:

Unit Test로 분리

---

문제:

테스트가 불안정하다

원인:

외부 의존성

해결:

Dependency 분리

---

문제:

회귀 버그 발생

원인:

Failure Case 누락

해결:

예외 테스트 강화

---

# 10. Agent Decision Rules

## 10.1 Test Routing

### [Flow]

```text
Pure Business Logic
→ Unit Test

Repository Query Validation
→ Repository Test

API Contract Validation
→ Controller Test

Multi-layer Flow
→ Integration Test
```

---

### [핵심]

Backend Agent Routing 기준.

---

### [FAQ]

Q. 언제 Unit Test를 생성해야 하는가?
A. 순수 Business Logic 검증이 필요할 때 생성한다.

---

# Retrieval Queries

### [FAQ]

Q. Unit Test란?
A. 작은 로직 단위를 독립적으로 검증하는 테스트다.

Q. Unit Test는 언제 사용하는가?
A. 순수 Business Logic 검증 시 사용한다.

Q. Unit Test에서 DB 사용 가능한가?
A. 아니다.

Q. Unit Test에서 중요한 것은?
A. Success, Failure, Boundary 검증.

Q. 언제 Repository Test를 써야 하나?
A. DB Query 검증이 필요할 때다.
