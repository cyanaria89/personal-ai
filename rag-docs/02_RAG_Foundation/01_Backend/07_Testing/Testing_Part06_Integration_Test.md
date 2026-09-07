# Testing Part 06 - Integration Test

---

# 1. Integration Test Core

## 1.1 Integration Test Overview

### [개념]

Integration Test는 여러 Layer가 함께 동작하는 전체 Flow를 검증하는 테스트다.

주요 목적:

- Layer Integration Validation
- Core Flow Validation
- Transaction Validation
- Security Validation

---

### [핵심]

검증 대상:

- Controller
- Service
- Repository
- Database
- Security

---

### [실무]

2026 Spring Boot 실무 기준 Integration Test는 핵심 Business Flow 검증에 사용된다.

대표 대상:

- 회원가입
- 로그인
- 주문
- 결제
- 알림 발송

---

### [FAQ]

Q. Integration Test란?
A. 여러 Layer가 연결된 전체 Flow를 검증하는 테스트다.

Q. Integration Test 핵심은?
A. Core Flow, Transaction, Security 검증이다.

---

# 2. Integration Test Scope

## 2.1 Test Target

### [개념]

애플리케이션의 핵심 Flow를 검증한다.

---

### [핵심]

포함:

- Controller
- Service
- Repository
- Security
- Database

제외:

- Frontend
- Real External API

---

### [FAQ]

Q. External API도 실제 호출하는가?
A. 아니다. 외부 API는 Mock 또는 Stub 처리한다.

---

# 3. Core Annotation

## 3.1 @SpringBootTest

### [개념]

@SpringBootTest는 전체 Application Context를 로드한다.

---

### [핵심]

포함:

- All Beans
- Security
- Repository
- Service
- Controller

---

### [예제]

```java
@SpringBootTest
class UserIntegrationTest {
}
```

---

### [Flow]

```text
Load Full Context
→ Execute Flow
→ Validate Result
```

---

### [FAQ]

Q. Integration Test에서 SpringBootTest가 필요한가?
A. 대부분 필요하다.

---

# 4. Core Flow Test

## 4.1 Flow Validation

### [개념]

핵심 비즈니스 흐름 검증.

---

### [Flow]

```text
Request
→ Controller
→ Service
→ Repository
→ Database
→ Response
```

---

### [핵심]

반드시 검증:

- End-to-End Flow
- State Change
- Data Consistency

---

### [FAQ]

Q. Integration Test 핵심은?
A. 전체 Flow가 정상 동작하는지 검증하는 것이다.

---

# 5. Database Integration

## 5.1 Database Validation

### [개념]

DB 연동 검증.

---

### [핵심]

검증 대상:

- Insert
- Update
- Delete
- Query

---

### [FAQ]

Q. 실제 DB를 사용하는가?
A. 테스트 DB 또는 Container 기반 DB를 사용한다.

---

# 6. Security Integration

## 6.1 Authentication & Authorization

### [개념]

Security Filter 포함 전체 인증 흐름 검증.

---

### [핵심]

검증 대상:

- Authentication
- Authorization
- JWT Flow
- Access Control

---

### [FAQ]

Q. Security도 Integration Test 대상인가?
A. 그렇다. 핵심 검증 대상이다.

Q. 인증 실패는 어떻게 검증하는가?
A. 401 Unauthorized 응답 검증.

Q. 권한 부족은 어떻게 검증하는가?
A. 403 Forbidden 응답 검증.

---

# 7. Transaction Test

## 7.1 Transaction Validation

### [개념]

Transaction Commit / Rollback 검증.

---

### [핵심]

검증 대상:

- Commit Success
- Rollback Trigger
- Data Consistency

---

### [FAQ]

Q. Transaction 검증이 중요한 이유는?
A. 데이터 정합성과 안정성에 직접 영향이 있다.

---

# 8. External Dependency

## 8.1 External Client Handling

### [개념]

외부 시스템은 실제 호출하지 않는다.

---

### [핵심]

대상:

- Payment API
- Mail
- SMS
- External API

---

### [주의]

Real Call 금지.

복잡한 Infra 검증은 Part07(Testcontainers) 참조.

---

### [FAQ]

Q. 외부 API는 어떻게 처리하는가?
A. Mock 또는 Stub 처리한다.

---

# 9. Test Profile

## 9.1 Test Environment

### [개념]

테스트 전용 환경 구성.

---

### [핵심]

- application-test.yml
- Test DB
- Test Secret

---

### [예제]

```java
@ActiveProfiles("test")
@SpringBootTest
class IntegrationTest {
}
```

---

### [FAQ]

Q. 운영 환경 설정을 사용해도 되는가?
A. 안 된다. 반드시 Test Profile 사용.

---

# 10. Integration Test Rules

## 10.1 Best Practice

### [Best Practice]

권장:

- 핵심 Flow만 테스트
- Test Profile 분리
- Security 포함
- Transaction 포함

---

### [주의]

금지:

- 모든 기능 Integration Test
- External API 실제 호출
- 불필요한 Full Flow

---

### [Checklist]

- Core Flow 검증
- DB 검증
- Security 검증
- Transaction 검증

---

# 11. Common Mistakes

## 11.1 Frequent Issues

### [Troubleshooting]

문제:

테스트 느림

원인:

Full Context Loading

해결:

핵심 Flow만 테스트

---

문제:

DB Connection Error

원인:

Test DB 설정 문제

해결:

Profile 확인

---

문제:

External API Failure

원인:

Real Call

해결:

Mock 처리

---

# 12. Agent Decision Rules

## 12.1 Test Routing

### [Flow]

```text
Multi-layer Flow Validation
→ Integration Test

Security Flow Validation
→ Integration Test

Transaction Validation
→ Integration Test

Pure Business Logic
→ Unit / Service Test
```

---

### [핵심]

Backend Agent Routing 기준.

---

### [FAQ]

Q. 언제 Integration Test를 생성해야 하는가?
A. 여러 Layer가 연결된 핵심 Flow 검증이 필요할 때다.

---

# Retrieval Queries

### [FAQ]

Q. Integration Test란?
A. 여러 Layer 연결 검증 테스트다.

Q. Integration Test 핵심 Annotation은?
A. @SpringBootTest.

Q. Integration Test 핵심 검증은?
A. Core Flow, Security, Transaction.

Q. External API도 실제 호출하는가?
A. 아니다. Mock 처리한다.

Q. 언제 Integration Test를 사용하는가?
A. Multi-layer Flow 검증이 필요할 때.
