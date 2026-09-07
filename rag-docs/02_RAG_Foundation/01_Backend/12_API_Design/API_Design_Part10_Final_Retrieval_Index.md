# API Design Part 10 - Final Retrieval Index, Cross Reference & Agent Usage Guide

---

# 1. API Design Retrieval Index

## 1.1 Retrieval Index Purpose

### [개념]

API Design Retrieval Index는 API Design 문서 전체를 Agent가 빠르게 검색하고 연결하기 위한 최종 색인 문서이다.

이 문서는 사람용 요약이 아니라 PM Agent, Backend Agent, Review Agent가 API 설계, 구현, 검수, 문제 해결 시 어떤 Part를 검색해야 하는지 안내하는 Retrieval Router 역할을 한다.

```text
User Query
→ Retrieval Index
→ Related API Design Part
→ Contract Rule
→ Code Generation / Review / Troubleshooting
```

---

### [핵심]

- Retrieval Index는 API Design 문서 전체의 검색 진입점이다.
- Agent는 사용자 질문을 API Topic으로 분류한다.
- Topic에 따라 관련 Part를 우선 검색한다.
- API 설계 질문은 Part01 ~ Part08을 우선 사용한다.
- API 테스트 질문은 Part09를 우선 사용한다.
- API 검수 질문은 Part07과 Part10을 우선 사용한다.
- API 문제 해결 질문은 Part06과 관련 Domain Part를 함께 사용한다.
- Edge Case 질문은 Part05, Part06, Part08, Part09의 보완 항목을 함께 검색한다.

---

### [실무]

2026 실무 기준 API Design RAG 문서는 단일 문서 검색보다 Cross Reference 기반 검색이 더 안정적이다.

사용자 질문 예시:

```text
"좋아요 API 어떻게 설계해?"
→ Part08 Toggle Pattern
→ Part05 Idempotency
→ Part07 Security Gate
→ Part09 Idempotency Test
```

사용자 질문 예시:

```text
"401이랑 403 뭐가 달라?"
→ Part02 Status Code
→ Part05 Authentication / Authorization
→ Part06 Troubleshooting
→ Part09 Authentication / Authorization Test
```

사용자 질문 예시:

```text
"목록 조회가 느려"
→ Part04 Pagination
→ Part06 Pagination Troubleshooting
→ Part09 Pagination Test
→ Part07 Pagination Quality Gate
```

사용자 질문 예시:

```text
"MockMvc POST 테스트가 403이 나와"
→ Part09 MockMvc Security Test
→ Part06 Authorization Troubleshooting
→ Part05 Authentication / Authorization
```

사용자 질문 예시:

```text
"Batch Delete를 DELETE Body로 만들어도 돼?"
→ Part08 Batch Delete Compatibility
→ Part02 HTTP Method
→ Part09 API Testing
```

---

### [FAQ]

Q. Retrieval Index는 무엇인가?

A. API Design 문서 전체를 Agent가 빠르게 검색하고 연결하기 위한 최종 색인 문서이다.

Q. Retrieval Index는 사람용 요약인가?

A. 아니다. Agent Retrieval, Topic Routing, Cross Reference, Review 품질 향상을 위한 문서이다.

Q. API 질문이 들어오면 Agent는 어떻게 사용해야 하는가?

A. 질문 Topic을 분류하고 관련 API Design Part를 우선 검색한 뒤 설계, 구현, 검수, 테스트 문서를 연결한다.

---

# 2. Document Map

## 2.1 API Design Parts

### [개념]

Document Map은 API Design RAG 문서 세트의 Part별 역할을 정의한다.

각 Part는 독립 검색 가능해야 하며, 동시에 다른 Part와 연결되어 API 설계와 검수를 완성해야 한다.

---

### [핵심]

|   Part | File                                                                   | Main Topic                                                                                       |
| -----: | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Part01 | API Core & REST Foundation                                             | API Core, REST, Resource, Stateless, Contract                                                    |
| Part02 | URI, Method & Status Code                                              | URI, Path Variable, Query Parameter, HTTP Method, Status Code                                    |
| Part03 | Request, Response & Contract                                           | Request Header, Body, DTO, Success Response, Error Response                                      |
| Part04 | Pagination, Filtering, Sorting & Validation                            | Page, Slice, Cursor, Filter, Search, Sort, Validation                                            |
| Part05 | Versioning, Idempotency, Authentication, Authorization & Rate Limiting | Versioning, Breaking Change, Idempotency, JWT, Role, Ownership, 429                              |
| Part06 | OpenAPI, Swagger & Troubleshooting                                     | OpenAPI, Swagger UI, ApiResponse Conflict, 400/401/403/404/409/429/500/502/503/504               |
| Part07 | Agent Review & Quality Gate                                            | PM Agent, Backend Agent, Review Agent, Quality Gate, Checklist                                   |
| Part08 | Practical API Patterns                                                 | CRUD Pattern, Search Pattern, Toggle, Ownership, Admin, Command, File, Batch, External API Proxy |
| Part09 | API Testing & Contract Verification                                    | Controller Test, MockMvc Security, Service Test, Repository Test, Swagger, Postman, Regression   |
| Part10 | Final Retrieval Index                                                  | Cross Reference, Query Routing, Final Checklist, Agent Usage                                     |

---

### [실무]

Agent는 다음 기준으로 Part를 선택한다.

```text
설계 원칙 질문 → Part01, Part02, Part03
Endpoint 설계 질문 → Part02, Part08
Request / Response 질문 → Part03
목록 조회 질문 → Part04
인증 / 권한 질문 → Part05
Rate Limiting 질문 → Part05, Part06, Part09
Swagger / OpenAPI 질문 → Part06
검수 / 리뷰 질문 → Part07
패턴 적용 질문 → Part08
Batch Delete 질문 → Part08, Part02, Part09
MockMvc / 테스트 질문 → Part09
External API 오류 질문 → Part06, Part08, Part09
문서 전체 연결 질문 → Part10
```

---

### [FAQ]

Q. API Design 문서는 몇 개 Part로 구성되는가?

A. Part01부터 Part10까지 구성된다.

Q. Endpoint 설계 질문은 어떤 Part를 우선 검색하는가?

A. Part02 URI / Method / Status Code와 Part08 Practical API Patterns를 우선 검색한다.

Q. 테스트 질문은 어떤 Part를 우선 검색하는가?

A. Part09 API Testing & Contract Verification을 우선 검색한다.

---

# 3. Topic Routing Rule

## 3.1 Query Topic Routing

### [개념]

Topic Routing Rule은 사용자 질문을 API Design 세부 Topic으로 분류하고 관련 문서를 연결하는 규칙이다.

Agent는 질문 속 Keyword를 기반으로 Primary Part와 Secondary Part를 선택해야 한다.

```text
User Query
→ Keyword Detection
→ Primary Part
→ Secondary Part
→ Answer / Code / Review
```

---

### [핵심]

| User Query Keyword                     | Primary Part | Secondary Part |
| -------------------------------------- | ------------ | -------------- |
| API, REST, Resource                    | Part01       | Part02, Part03 |
| URI, URL, Path, Query                  | Part02       | Part08         |
| GET, POST, PUT, PATCH, DELETE          | Part02       | Part08         |
| Status Code, 200, 400, 401, 403        | Part02       | Part06         |
| Request, Header, Body, DTO             | Part03       | Part09         |
| Response, ErrorResponse, ApiResponse   | Part03       | Part06, Part07 |
| Pagination, Page, Slice, Cursor        | Part04       | Part06, Part09 |
| Filtering, Search, Sorting             | Part04       | Part08         |
| Validation, @Valid, Error Field        | Part04       | Part09         |
| Versioning, Breaking Change            | Part05       | Part07, Part09 |
| Idempotency, Duplicate Request         | Part05       | Part08, Part09 |
| JWT, Authentication, Authorization     | Part05       | Part06, Part09 |
| Rate Limit, 429, Too Many Requests     | Part05       | Part06, Part09 |
| OpenAPI, Swagger                       | Part06       | Part07, Part09 |
| Swagger ApiResponse 충돌               | Part06       | Part03, Part10 |
| ApiResponse import conflict            | Part06       | Part03, Part10 |
| Troubleshooting, 404, 500              | Part06       | Part02, Part03 |
| External API Error, Provider Error     | Part06       | Part08, Part09 |
| 502, 503, 504, Gateway Timeout         | Part06       | Part08, Part09 |
| Review, Checklist, Quality Gate        | Part07       | Part10         |
| CRUD Pattern, Toggle, Admin            | Part08       | Part05, Part07 |
| Batch Delete, DELETE Body              | Part08       | Part02, Part09 |
| External API Proxy                     | Part08       | Part06, Part09 |
| Test, MockMvc, Postman                 | Part09       | Part06         |
| MockMvc 403, CSRF, addFilters          | Part09       | Part05, Part06 |
| Regression Test, Contract Verification | Part09       | Part07, Part10 |
| Final Check, 전체 검수                 | Part10       | Part07         |

---

### [실무]

Query Routing 예시:

```text
질문: "리뷰 수정 API 설계해줘"

Routing:
- Primary: Part08 Update Pattern
- Secondary: Part05 Ownership
- Secondary: Part03 Request / Response DTO
- Secondary: Part09 Authorization Test

Answer Focus:
- PATCH /api/v1/reviews/{reviewId}
- Request DTO
- Ownership Check
- 403 ACCESS_DENIED
- Validation / Error Response
```

Query Routing 예시:

```text
질문: "축제 목록 조회 API 느린데?"

Routing:
- Primary: Part04 Pagination
- Secondary: Part06 Pagination Troubleshooting
- Secondary: Part09 Pagination Test
- Secondary: Part07 Pagination Quality Gate

Answer Focus:
- Pagination 적용
- Page vs Slice vs Cursor
- Default Sort
- Max size
- Index / Count Query
```

Query Routing 예시:

```text
질문: "Swagger에서 ApiResponse import 충돌나는데?"

Routing:
- Primary: Part06 Swagger ApiResponse Name Conflict
- Secondary: Part03 Response Wrapper
- Secondary: Part10 Topic Routing

Answer Focus:
- 프로젝트 ApiResponse<T>와 Swagger @ApiResponse 충돌
- Fully Qualified Name 사용
- Wrapper 이름 변경 영향도
```

Query Routing 예시:

```text
질문: "외부 API timeout은 500으로 처리하면 돼?"

Routing:
- Primary: Part06 External API Error Troubleshooting
- Secondary: Part08 External API Proxy Pattern
- Secondary: Part09 External API Integration Test

Answer Focus:
- 504 Gateway Timeout 가능
- 프로젝트 단순화 시 500 정책 가능
- Provider Error Mapping 문서화
```

---

### [FAQ]

Q. Topic Routing Rule은 무엇인가?

A. 사용자 질문을 API Design 세부 Topic으로 분류하고 관련 문서를 연결하는 규칙이다.

Q. Agent는 Primary Part만 검색하면 되는가?

A. 아니다. API 설계는 Contract, Security, Test가 연결되므로 Secondary Part도 함께 검색해야 한다.

Q. Topic Routing의 목표는 무엇인가?

A. Retrieval Hit를 높이고 API 답변, 코드 생성, 리뷰 품질을 안정화하는 것이다.

---

# 4. Cross Reference Matrix

## 4.1 API Design Cross Reference

### [개념]

Cross Reference Matrix는 API Design Topic 사이의 연관 관계를 정의한다.

API 설계는 단일 Topic으로 끝나지 않으며 URI, Method, Status Code, Request, Response, Security, Test가 함께 연결된다.

---

### [핵심]

| Topic               | 반드시 함께 볼 Topic                                           |
| ------------------- | -------------------------------------------------------------- |
| URI Design          | HTTP Method, Resource, Status Code                             |
| HTTP Method         | URI, Status Code, Idempotency                                  |
| Status Code         | Error Response, Troubleshooting, Test                          |
| Request Body        | Request DTO, Validation, Security                              |
| Response Body       | Response DTO, Contract Stability, OpenAPI                      |
| Error Response      | Status Code, GlobalExceptionHandler, Frontend Error Handling   |
| Pagination          | Sorting, Filtering, Performance, Test                          |
| Validation          | Request DTO, Error Response, Field Error                       |
| Authentication      | Authorization Header, JWT, 401 Test                            |
| Authorization       | Role, Permission, Ownership, 403 Test                          |
| Rate Limiting       | 429, Retry-After, Abuse Prevention, Rate Limiting Test         |
| Idempotency         | Duplicate Request, Unique Constraint, 409 Test                 |
| OpenAPI             | Swagger UI, Contract Review, Frontend Integration              |
| ApiResponse Wrapper | OpenAPI Annotation, Swagger Import Conflict, Response Contract |
| Batch Delete        | DELETE Body Compatibility, Command API, Batch Test             |
| External API Proxy  | 502/503/504, Timeout, Provider Error, External API Test        |
| MockMvc Security    | CSRF, addFilters, Authentication Test, Authorization Test      |
| API Pattern         | Security, Error, Test, Quality Gate                            |
| API Testing         | Contract Verification, Regression, Defect Report               |

---

### [실무]

Cross Reference 사용 예시:

```text
Topic: Request Body
Required References:
- Part03 Request Body Contract
- Part04 Validation
- Part05 Security Input / Authorization
- Part09 Controller Test
```

Cross Reference 사용 예시:

```text
Topic: Error Response
Required References:
- Part02 Status Code
- Part03 Error Response Schema
- Part06 Troubleshooting
- Part07 Error Quality Gate
- Part09 Error Response Test
```

Cross Reference 사용 예시:

```text
Topic: Rate Limiting
Required References:
- Part05 Rate Limiting
- Part06 429 Troubleshooting
- Part07 Security Quality Gate
- Part09 Rate Limiting Test
```

Cross Reference 사용 예시:

```text
Topic: Batch Delete
Required References:
- Part08 Batch API Pattern
- Part08 Batch Delete Compatibility
- Part02 HTTP Method
- Part09 Contract Verification
```

---

### [FAQ]

Q. Cross Reference Matrix는 무엇인가?

A. API Design Topic 사이의 연관 관계를 정의한 검색 연결 표이다.

Q. API 설계에서 Cross Reference가 필요한 이유는 무엇인가?

A. API 설계는 URI, Method, Request, Response, Security, Test가 함께 연결되기 때문이다.

Q. Error Response를 설계할 때 함께 봐야 할 Topic은 무엇인가?

A. Status Code, Error Response Schema, Troubleshooting, Error Quality Gate, Error Response Test이다.

---

# 5. PM Agent Usage Guide

## 5.1 PM Agent Retrieval Rule

### [개념]

PM Agent는 사용자 요구사항을 API Use Case, Resource, Endpoint 후보, Access Level로 변환한다.

PM Agent는 구현 코드보다 API 필요성, 기능 누락, 화면 흐름, 요구사항 충족 여부를 우선 검수한다.

---

### [핵심]

- PM Agent는 기능 요구사항을 Resource로 변환한다.
- PM Agent는 사용자 화면 흐름을 API 흐름으로 변환한다.
- PM Agent는 필요한 CRUD, Search, Filter, Action API를 식별한다.
- PM Agent는 Public / Protected / Admin API를 구분한다.
- PM Agent는 API 누락과 중복을 탐지한다.
- PM Agent는 Frontend 화면에 필요한 Response Field를 식별한다.
- PM Agent는 Rate Limit, External API, Batch 처리 같은 비기능 요구도 식별한다.

---

### [실무]

PM Agent 검색 우선순위:

```text
1. Part08 Practical API Patterns
2. Part01 API Core & REST Foundation
3. Part02 URI / Method / Status Code
4. Part05 Authentication / Authorization / Rate Limiting
5. Part07 PM Agent Review
6. Part10 Retrieval Index
```

PM Agent 출력 기준:

```text
Feature:
Resource:
Required APIs:
Access Level:
Request Contract:
Response Contract:
Error Contract:
Frontend Need:
Rate Limit Need:
External API Need:
Missing API Risk:
Review Note:
```

---

### [FAQ]

Q. PM Agent는 어떤 API 문서를 우선 검색해야 하는가?

A. Part08 Practical API Patterns와 Part01 API Core, Part02 URI Design을 우선 검색해야 한다.

Q. PM Agent의 핵심 역할은 무엇인가?

A. 요구사항을 API Use Case와 Resource로 변환하고 API 누락 여부를 검수하는 것이다.

Q. PM Agent가 Security도 확인해야 하는가?

A. 확인해야 한다. Public / Protected / Admin 구분은 요구사항 단계에서 먼저 정리해야 한다.

---

# 6. Backend Agent Usage Guide

## 6.1 Backend Agent Retrieval Rule

### [개념]

Backend Agent는 API Contract를 Spring Boot 3.x Controller, DTO, Service, Repository, Exception Handling 구현으로 변환한다.

Backend Agent는 API 설계와 Backend Layer 구현이 일치하는지 확인해야 한다.

---

### [핵심]

- Backend Agent는 Controller Mapping을 생성한다.
- Backend Agent는 Request DTO와 Response DTO를 분리한다.
- Backend Agent는 Validation Annotation을 적용한다.
- Backend Agent는 Service Business Validation을 구현한다.
- Backend Agent는 Repository Query와 Pagination을 구현한다.
- Backend Agent는 ErrorCode와 GlobalExceptionHandler를 연결한다.
- Backend Agent는 SecurityContext 기반 currentUser 사용을 적용한다.
- Backend Agent는 Rate Limit, External API Error Mapping, Idempotency 구현 필요성을 확인한다.

---

### [실무]

Backend Agent 검색 우선순위:

```text
1. Part03 Request / Response Contract
2. Part04 Validation / Pagination
3. Part05 Authentication / Authorization / Idempotency / Rate Limiting
4. Part08 Practical API Patterns
5. Part09 Controller / Service / Repository Test
6. Part06 Troubleshooting / OpenAPI Edge Case
7. Part07 Backend Agent Review
```

Backend Agent 구현 출력 기준:

```text
Controller:
Request DTO:
Response DTO:
Service Method:
Repository Method:
Validation:
ErrorCode:
Status Code:
Security:
Idempotency:
Rate Limiting:
External API Policy:
Test Case:
Review Checklist:
```

---

### [FAQ]

Q. Backend Agent는 어떤 API 문서를 우선 검색해야 하는가?

A. Part03 Request / Response Contract, Part04 Validation / Pagination, Part08 Practical API Patterns를 우선 검색해야 한다.

Q. Backend Agent의 핵심 역할은 무엇인가?

A. API Contract를 Controller, DTO, Service, Repository, Exception Handling으로 구현하는 것이다.

Q. Backend Agent가 Entity를 직접 Response로 반환해도 되는가?

A. 안 된다. Response DTO로 변환해야 한다.

---

# 7. Review Agent Usage Guide

## 7.1 Review Agent Retrieval Rule

### [개념]

Review Agent는 API 설계와 구현의 결함을 탐지하고 Release 가능 여부를 판단한다.

Review Agent는 Contract Mismatch, Security Issue, Status Code 오류, Error Response 불일치, Validation 누락, Pagination 누락을 우선 검수한다.

---

### [핵심]

- Review Agent는 Security Issue를 최우선 검수한다.
- Review Agent는 Contract Mismatch를 탐지한다.
- Review Agent는 Status Code와 Error Code 의미 일치를 검수한다.
- Review Agent는 Authentication / Authorization / Ownership 누락을 검수한다.
- Review Agent는 목록 API Pagination 누락을 검수한다.
- Review Agent는 Rate Limiting 누락을 고위험 API에서 검수한다.
- Review Agent는 Batch Delete, External API Error, MockMvc Security 같은 Edge Case를 검수한다.
- Review Agent는 Breaking Change 위험을 검수한다.
- Review Agent는 문제, 영향, 원인, 수정 방향을 출력한다.

---

### [실무]

Review Agent 검색 우선순위:

```text
1. Part07 Agent Review & Quality Gate
2. Part10 Final Retrieval Index
3. Part06 Troubleshooting / Contract Mismatch
4. Part05 Security / Idempotency / Breaking Change / Rate Limiting
5. Part03 Request / Response / Error Contract
6. Part08 Practical API Patterns
7. Part09 Testing / Contract Verification
```

Review Agent 출력 기준:

```text
# API Review Result

Score:
Release Decision:
Critical Issues:
Major Issues:
Minor Issues:

## Issue

Severity:
Problem:
Impact:
Cause:
Fix:
Reference Topic:
Retest:
```

---

### [FAQ]

Q. Review Agent는 어떤 API 문서를 우선 검색해야 하는가?

A. Part07 Agent Review와 Part10 Retrieval Index, Part06 Troubleshooting을 우선 검색해야 한다.

Q. Review Agent가 가장 먼저 확인할 문제는 무엇인가?

A. Security Issue와 Contract Mismatch를 가장 먼저 확인해야 한다.

Q. Review Agent 출력에는 무엇이 포함되어야 하는가?

A. Severity, Problem, Impact, Cause, Fix, Score, Release Decision이 포함되어야 한다.

---

# 8. API Design Answer Pattern

## 8.1 Agent Answer Template

### [개념]

API Design Answer Pattern은 Agent가 API 설계 질문에 답변할 때 사용하는 표준 출력 구조이다.

이 Template은 설계, 구현, 검수, 테스트를 한 번에 연결하여 API 답변 품질을 안정화한다.

---

### [핵심]

- API 답변은 Endpoint만 제시하면 부족하다.
- Request Contract를 포함해야 한다.
- Response Contract를 포함해야 한다.
- Error Contract를 포함해야 한다.
- Security Contract를 포함해야 한다.
- Validation Rule을 포함해야 한다.
- Rate Limiting 또는 Idempotency 필요성을 검토해야 한다.
- Test Case를 포함하면 구현 안정성이 높아진다.

---

### [실무]

API Design Answer Template:

```text
# API Design Result

## 1. Endpoint

Method:
URI:
Access Level:

## 2. Request Contract

Header:
Path Variable:
Query Parameter:
Request Body:

## 3. Response Contract

Success Status:
Success Body:
Error Response:

## 4. Validation

Request Validation:
Business Validation:

## 5. Security

Authentication:
Authorization:
Ownership:

## 6. Reliability

Idempotency:
Rate Limiting:
External API Policy:

## 7. Implementation Guide

Controller:
Service:
Repository:
DTO:

## 8. Test Case

Success:
Validation Fail:
Authentication Fail:
Authorization Fail:
Not Found:
Conflict:
Rate Limit:
External Error:

## 9. Review Checklist

Contract:
Security:
Error:
Pagination:
OpenAPI:
Testing:
```

---

### [FAQ]

Q. API Design 답변에는 무엇이 포함되어야 하는가?

A. Endpoint, Request Contract, Response Contract, Error Contract, Security, Validation, Test Case가 포함되어야 한다.

Q. Endpoint만 답변하면 부족한 이유는 무엇인가?

A. API 품질은 URI뿐 아니라 Request, Response, Error, Security, Test Contract로 결정되기 때문이다.

Q. API 설계 답변에 Test Case도 포함해야 하는가?

A. 가능하면 포함하는 것이 좋다. 구현 후 검증 기준을 함께 제공할 수 있기 때문이다.

---

# 9. API Review Answer Pattern

## 9.1 Review Answer Template

### [개념]

API Review Answer Pattern은 Agent가 API 설계 또는 구현을 검수할 때 사용하는 표준 출력 구조이다.

Review 답변은 단순 지적이 아니라 수정 가능한 Issue 단위로 작성해야 한다.

---

### [핵심]

- Review 결과에는 Score를 포함한다.
- Release Decision을 포함한다.
- Critical Issue를 분리한다.
- 각 Issue는 Severity를 가진다.
- 각 Issue는 Problem, Impact, Cause, Fix를 포함한다.
- Fix 이후 Retest 방법을 포함한다.
- Reference Topic을 연결하면 Retrieval 품질이 좋아진다.
- Edge Case는 놓치기 쉬우므로 별도 Issue로 표시한다.

---

### [실무]

API Review Answer Template:

```text
# API Review Result

## Summary

Score:
Release Decision:
Critical:
Major:
Minor:

---

## Issues

### Issue 1

Severity:
Problem:
Impact:
Cause:
Fix:
Reference Topic:
Retest:

---

## Final Decision

Release:
Required Fix:
Next Review:
```

Severity 기준:

| Severity | 기준                                                                        |
| -------- | --------------------------------------------------------------------------- |
| Critical | 인증 누락, 권한 누락, 민감 정보 노출, 데이터 손실, 결제 중복                |
| Major    | Contract Mismatch, Status Code 오류, Error Response 불일치, Pagination 누락 |
| Minor    | Naming, Example 누락, 문서 설명 부족                                        |
| Info     | 개선 제안, Convention 보완                                                  |

Edge Case Review 대상:

```text
Swagger @ApiResponse import conflict
DELETE Body compatibility
MockMvc CSRF false positive 403
Missing 429 Rate Limit Contract
Missing 502 / 503 / 504 External API Policy
```

---

### [FAQ]

Q. API Review 답변에는 무엇이 포함되어야 하는가?

A. Score, Release Decision, Severity, Problem, Impact, Cause, Fix, Retest가 포함되어야 한다.

Q. Critical Issue는 무엇인가?

A. 인증 누락, 권한 누락, 민감 정보 노출, 데이터 손실, 결제 중복처럼 배포를 차단해야 하는 문제이다.

Q. Review 답변이 유용하려면 무엇이 필요한가?

A. 문제뿐 아니라 영향, 원인, 수정 방향, 재검수 방법이 명확해야 한다.

---

# 10. API Troubleshooting Answer Pattern

## 10.1 Troubleshooting Answer Template

### [개념]

API Troubleshooting Answer Pattern은 API 오류 원인을 분석하고 해결 방향을 제시하는 표준 출력 구조이다.

Troubleshooting 답변은 Status Code, Request, Response, Server Log, Security Config, DB 상태를 연결해야 한다.

---

### [핵심]

- 문제를 Status Code 기준으로 분류한다.
- Request URL과 Method를 확인한다.
- Header, Query Parameter, Body를 확인한다.
- Response Body와 Error Code를 확인한다.
- Server Log를 확인한다.
- Security Config를 확인한다.
- DB Resource 존재 여부를 확인한다.
- External API Provider 상태를 확인한다.
- 재현 방법과 수정 방법을 제공한다.

---

### [실무]

Troubleshooting Answer Template:

```text
# API Troubleshooting Result

## 1. Symptom

Status Code:
Error Code:
API:
Scenario:

## 2. Likely Cause

Cause 1:
Cause 2:
Cause 3:

## 3. Check Order

1. Request URL / Method
2. Header
3. Query Parameter
4. Request Body
5. Response Body
6. Server Log
7. Controller Mapping
8. Security Config
9. Service Logic
10. DB Data
11. External Provider Log
12. OpenAPI Contract

## 4. Fix

Fix 1:
Fix 2:

## 5. Retest

Swagger UI:
Postman:
Frontend Network:
MockMvc:
```

Status Code 기반 원인:

```text
400 → Request / Validation / JSON / Type 문제
401 → Authentication / Token 문제
403 → Authorization / Role / Ownership / CSRF 문제
404 → URI Mapping 또는 Resource 없음
409 → 중복 / 상태 충돌 / Business Rule 문제
429 → Rate Limit 초과
500 → Server Exception / DB / RuntimeException
502 → External Provider Bad Response
503 → External Provider Unavailable
504 → External Provider Timeout
```

---

### [FAQ]

Q. API Troubleshooting 답변에는 무엇이 포함되어야 하는가?

A. 증상, 가능 원인, 확인 순서, 수정 방법, 재검수 방법이 포함되어야 한다.

Q. API 오류는 무엇을 기준으로 먼저 분류하는가?

A. Status Code와 Error Code를 기준으로 먼저 분류한다.

Q. Frontend API 오류에서 가장 먼저 볼 것은 무엇인가?

A. Browser Network Tab의 Request URL, Method, Header, Payload, Status Code, Response Body이다.

---

# 11. Final API Quality Score

## 11.1 Quality Score Rule

### [개념]

Final API Quality Score는 API 설계와 구현이 실무 적용 가능한 수준인지 정량적으로 판단하는 기준이다.

Score는 단순 코드 품질이 아니라 Contract, Security, Error, Pagination, OpenAPI, Test를 함께 평가한다.

---

### [핵심]

|    Score | 기준                 |
| -------: | -------------------- |
| 97 ~ 100 | Agent 실무 적용 최적 |
|  95 ~ 96 | 실무 적용 가능       |
|  90 ~ 94 | 경미한 보완 필요     |
|  80 ~ 89 | 구현 전 보완 필요    |
|  70 ~ 79 | Contract 오류 다수   |
|  70 미만 | API 재설계 필요      |

Critical Issue가 있으면 점수와 관계없이 Release Blocked이다.

---

### [실무]

Score 평가 항목:

| 항목                                          | 배점 |
| --------------------------------------------- | ---: |
| Resource / URI / Method                       |   15 |
| Request / Response Contract                   |   15 |
| Status Code / Error Response                  |   15 |
| Security / Authorization                      |   20 |
| Pagination / Filtering / Sorting              |   10 |
| Validation / Business Rule                    |   10 |
| OpenAPI / Swagger                             |    5 |
| Testing / Verification                        |    5 |
| Breaking Change / Idempotency / Rate Limiting |    5 |

Critical Issue:

- Protected API 공개
- Admin API 권한 누락
- Ownership 검증 누락
- 민감 정보 Response 노출
- 결제 / 주문 중복 처리 누락
- Error Response 전역 불일치
- 대량 목록 API Pagination 누락
- Breaking Change 미검토
- Provider Secret 또는 API Key 노출
- Rate Limit 필요한 고위험 API 무제한 공개

---

### [FAQ]

Q. Final API Quality Score는 무엇인가?

A. API 설계와 구현이 실무 적용 가능한 수준인지 정량적으로 판단하는 기준이다.

Q. API Review 목표 점수는 몇 점인가?

A. 최소 95점 이상, 목표는 97점 이상이다.

Q. Critical Issue가 있으면 점수가 높아도 배포 가능한가?

A. 아니다. Critical Issue가 있으면 점수와 관계없이 Release Blocked이다.

---

# 12. Final Agent Checklist

## 12.1 Final Checklist

### [Checklist]

API Design Final Checklist:

- API 목적이 명확한가?
- Resource가 명확한가?
- URI가 명사 기반인가?
- URI가 복수형 Resource를 사용하는가?
- URI에 불필요한 동사가 없는가?
- HTTP Method가 역할에 맞는가?
- Status Code가 상황에 맞는가?
- Error Code가 Status Code와 의미상 일치하는가?
- Request Header가 문서화되어 있는가?
- Path Variable 이름이 구체적인가?
- Query Parameter가 검색 조건으로 분리되어 있는가?
- Request DTO와 Entity가 분리되어 있는가?
- Response DTO와 Entity가 분리되어 있는가?
- Request Validation이 적용되어 있는가?
- Business Validation이 Service Layer에 있는가?
- Success Response Schema가 통일되어 있는가?
- Error Response Schema가 통일되어 있는가?
- Validation Error가 Field Error를 포함하는가?
- Authentication 필요 여부가 명확한가?
- Authorization 조건이 명확한가?
- Ownership 검증이 필요한 API에 적용되어 있는가?
- Public / Protected / Admin API가 구분되어 있는가?
- Access Token을 Authorization Header로 전달하는가?
- Request Body의 userId를 신뢰하지 않는가?
- 목록 API에 Pagination이 적용되어 있는가?
- Filtering Parameter가 문서화되어 있는가?
- Sorting 기준이 문서화되어 있는가?
- 기본 Sort 기준이 있는가?
- size 최대값 제한이 있는가?
- Cursor 기준과 Sort 기준이 일치하는가?
- Idempotency가 필요한 API에 중복 요청 처리가 있는가?
- Rate Limiting이 필요한 API가 식별되어 있는가?
- Rate Limit 초과 시 429 Error Contract가 있는가?
- File Upload API에 Size / MIME / Extension 검증이 있는가?
- Batch API에 부분 성공 / 실패 정책이 있는가?
- Batch Delete에서 DELETE Body 호환성을 검토했는가?
- External API Proxy에서 Provider Error Mapping이 있는가?
- OpenAPI 문서가 실제 구현과 일치하는가?
- Swagger UI에서 테스트 가능한가?
- Swagger `@ApiResponse`와 프로젝트 `ApiResponse<T>` import 충돌이 없는가?
- Error Response가 OpenAPI에 문서화되어 있는가?
- 인증 필요 API에 Security Requirement가 있는가?
- Frontend Axios URL과 Backend Mapping이 일치하는가?
- Response Field가 Frontend 사용 Field와 일치하는가?
- Date Time Format이 통일되어 있는가?
- Breaking Change 여부를 검토했는가?
- Regression Test가 필요한 API를 식별했는가?
- MockMvc Security Test에서 CSRF / addFilters 설정을 검토했는가?

---

### [실무]

Final Agent 판단 기준:

```text
All Critical Pass
+ Contract Score >= 95
+ Security Gate Pass
+ Error Gate Pass
+ OpenAPI Gate Pass
+ Test Gate Pass
= API Ready
```

Release Blocked 조건:

```text
Critical Security Issue
OR Contract Mismatch
OR Entity Sensitive Field Exposure
OR Missing Authorization
OR Missing Error Response
OR Missing Pagination on Large List
OR Breaking Change Without Migration
OR Provider Secret Exposure
OR Payment Duplicate Risk
```

---

### [FAQ]

Q. Final Agent Checklist는 언제 사용하는가?

A. API 설계 완료 후, 구현 완료 후, Frontend 연동 전, 배포 전 최종 검수에 사용한다.

Q. API Ready 조건은 무엇인가?

A. Critical Issue가 없고 Contract, Security, Error, OpenAPI, Test Gate를 통과해야 한다.

Q. Release Blocked 조건은 무엇인가?

A. 인증 누락, 권한 누락, 민감 정보 노출, Contract Mismatch, Error Response 누락, Breaking Change 미검토이다.

---

# 13. API Design Document Quality Gate

## 13.1 RAG Document Quality

### [개념]

API Design Document Quality Gate는 API Design RAG 문서 자체가 Agent Retrieval에 적합한지 검수하는 기준이다.

문서 품질은 Agent의 API 설계, 코드 생성, 리뷰, 테스트 품질에 직접 영향을 준다.

---

### [핵심]

- 각 Part는 독립 검색 가능해야 한다.
- 각 Chunk는 하나의 개념만 설명해야 한다.
- `[개념]`, `[핵심]`, `[실무]`, `[FAQ]`가 포함되어야 한다.
- Retrieval Queries Block이 포함되어야 한다.
- API 핵심 용어가 반복되어야 한다.
- 용어는 문서 전체에서 통일되어야 한다.
- FAQ는 Query Pattern Matching을 강화해야 한다.
- 예제는 짧고 직접적이어야 한다.
- 긴 서론과 장문 설명은 피해야 한다.
- Edge Case는 별도 Keyword로 검색 가능해야 한다.

---

### [실무]

RAG 문서 검수 기준:

| 항목              | 기준                                                   |
| ----------------- | ------------------------------------------------------ |
| Chunk 독립성      | 단일 Chunk만 검색되어도 의미 유지                      |
| Keyword 반복      | API, REST, URI, Status Code, Validation 등 핵심어 포함 |
| FAQ 품질          | Q + A 구조, 짧고 직접적                                |
| Code Example      | 짧은 snippet, 실무 연결                                |
| Cross Reference   | 관련 Part 연결 가능                                    |
| Retrieval Queries | 문서 마지막 필수 포함                                  |
| 용어 통일         | Request DTO, Response DTO, ErrorResponse 등 일관성     |
| Edge Case 검색성  | 429, CSRF, DELETE Body, ApiResponse Conflict 등 포함   |
| Agent 사용성      | PM / Backend / Review Agent가 바로 사용 가능           |

---

### [Checklist]

RAG Document Quality Checklist:

- Markdown 구조가 유지되었는가?
- Section Header가 명확한가?
- Chunk가 너무 길지 않은가?
- 하나의 Chunk에 여러 개념이 섞이지 않았는가?
- `[FAQ]`가 충분한가?
- `Q only`가 없는가?
- Retrieval Queries Block이 있는가?
- API 핵심 Keyword가 반복되는가?
- Domain Rules를 반영했는가?
- Master Rules를 반영했는가?
- Project Progress와 Agent 목적에 맞는가?
- 오타와 용어 혼용이 없는가?
- Legacy 기술 설명이 불필요하게 포함되지 않았는가?
- 2026 실무 기준과 맞는가?
- 재작업 Patch 항목이 Cross Reference에 반영되었는가?

---

### [FAQ]

Q. API Design Document Quality Gate는 무엇인가?

A. API Design RAG 문서 자체가 Agent Retrieval에 적합한지 검수하는 기준이다.

Q. RAG 문서에서 FAQ가 중요한 이유는 무엇인가?

A. 사용자 질문과 Agent Retrieval Query가 FAQ 형태와 잘 매칭되기 때문이다.

Q. RAG 문서 품질 목표는 무엇인가?

A. 최소 95점 이상, 목표 97점 이상이다.

---

# 14. Common Retrieval Mistakes

## 14.1 Retrieval Failure Pattern

### [Troubleshooting]

문제: Agent가 API 질문에 일반론만 답변한다.

원인: Query Routing이 없고 관련 Part를 연결하지 않았다.

해결: Part10 Retrieval Index에서 Primary Part와 Secondary Part를 선택한다.

---

문제: Agent가 Endpoint만 만들고 Error Response를 누락한다.

원인: Part02 URI / Method만 검색하고 Part03 Error Response와 Part07 Error Gate를 연결하지 않았다.

해결: API 설계 답변 시 Request, Response, Error, Security, Test를 함께 출력한다.

---

문제: Agent가 좋아요 API를 `/likeFestival`로 설계한다.

원인: REST Resource와 Toggle Pattern 검색이 누락되었다.

해결: Part02 URI Design과 Part08 Toggle Pattern을 함께 검색한다.

---

문제: Agent가 인증 실패와 권한 실패를 혼동한다.

원인: Status Code, Authentication, Authorization 문서 연결이 부족하다.

해결: Part02 Status Code, Part05 Authentication / Authorization, Part06 Troubleshooting을 함께 검색한다.

---

문제: Agent가 Rate Limit 초과를 403으로 답변한다.

원인: Rate Limiting과 Authorization 문서를 구분하지 않았다.

해결: Part05 Rate Limiting, Part06 429 Troubleshooting, Part09 Rate Limiting Test를 함께 검색한다.

---

문제: Agent가 목록 API에 Pagination을 적용하지 않는다.

원인: Collection Query Pattern과 Pagination Quality Gate 검색이 누락되었다.

해결: Part04 Pagination, Part08 Collection Query Pattern, Part07 Pagination Gate를 함께 검색한다.

---

문제: Agent가 Batch Delete를 무조건 `DELETE + Body`로 생성한다.

원인: Batch Delete Compatibility 검색이 누락되었다.

해결: Part08 Batch Delete Compatibility와 Command API Pattern을 함께 검색한다.

---

문제: Agent가 MockMvc 403을 권한 문제로만 판단한다.

원인: CSRF와 Security Filter 테스트 문서 검색이 누락되었다.

해결: Part09 MockMvc Security Test와 Part06 403 Troubleshooting을 함께 검색한다.

---

문제: Agent가 외부 API Timeout을 무조건 500으로 처리한다.

원인: External API Error Mapping 검색이 누락되었다.

해결: Part06 External API Error Troubleshooting, Part08 External API Proxy Pattern, Part09 External API Integration Test를 함께 검색한다.

---

문제: Agent가 테스트 케이스를 정상 케이스만 작성한다.

원인: Part09 Error Response Test와 Security Test 검색이 누락되었다.

해결: Success, Validation Fail, Authentication Fail, Authorization Fail, Not Found, Conflict, Rate Limit, External Error Test를 포함한다.

---

문제: Agent가 API 변경의 Breaking Change를 놓친다.

원인: Versioning, Backward Compatibility, Breaking Change Gate 검색이 누락되었다.

해결: Part05 Breaking Change와 Part07 Breaking Change Gate, Part09 Regression Test를 함께 검색한다.

---

### [FAQ]

Q. API Retrieval에서 가장 흔한 실패는 무엇인가?

A. Endpoint만 검색하고 Request, Response, Error, Security, Test 문서를 연결하지 않는 것이다.

Q. Retrieval 실패를 줄이는 방법은 무엇인가?

A. Part10 Topic Routing과 Cross Reference Matrix를 사용해 Primary Part와 Secondary Part를 함께 검색한다.

Q. Agent가 일반론만 답변하면 어떻게 보완하는가?

A. Practical Pattern, Quality Gate, Test 문서를 함께 검색하도록 Routing을 강화한다.

---

# Retrieval Queries

### [FAQ]

Q. API Design Retrieval Index는 무엇인가?
A. API Design 문서 전체를 Agent가 빠르게 검색하고 연결하기 위한 최종 색인 문서이다.

Q. API Design 문서는 어떻게 구성되는가?
A. API Core, URI, Request Response, Pagination, Security, OpenAPI, Review, Pattern, Testing, Retrieval Index로 구성된다.

Q. Endpoint 설계 질문은 어떤 Part를 검색하는가?
A. Part02 URI / Method / Status Code와 Part08 Practical API Patterns를 우선 검색한다.

Q. Request Response 질문은 어떤 Part를 검색하는가?
A. Part03 Request, Response & Contract Design을 우선 검색한다.

Q. Pagination 질문은 어떤 Part를 검색하는가?
A. Part04 Pagination과 Part06 Pagination Troubleshooting, Part09 Pagination Test를 함께 검색한다.

Q. 인증 권한 질문은 어떤 Part를 검색하는가?
A. Part05 Authentication / Authorization과 Part06 Troubleshooting, Part09 Authentication / Authorization Test를 검색한다.

Q. Rate Limit 질문은 어떤 Part를 검색하는가?
A. Part05 Rate Limiting, Part06 429 Troubleshooting, Part09 Rate Limiting Test를 검색한다.

Q. OpenAPI Swagger 질문은 어떤 Part를 검색하는가?
A. Part06 OpenAPI, Swagger & Troubleshooting을 우선 검색한다.

Q. Swagger ApiResponse 충돌 질문은 어떤 Part를 검색하는가?
A. Part06 Swagger ApiResponse Name Conflict와 Part03 Response Wrapper를 검색한다.

Q. Batch Delete 질문은 어떤 Part를 검색하는가?
A. Part08 Batch Delete Compatibility, Part02 HTTP Method, Part09 Contract Verification을 검색한다.

Q. MockMvc 403 질문은 어떤 Part를 검색하는가?
A. Part09 MockMvc Security Test, Part06 Authorization Troubleshooting, Part05 Security를 검색한다.

Q. External API Error 질문은 어떤 Part를 검색하는가?
A. Part06 External API Error Troubleshooting, Part08 External API Proxy Pattern, Part09 External API Integration Test를 검색한다.

Q. API Review 질문은 어떤 Part를 검색하는가?
A. Part07 Agent Review와 Part10 Final Retrieval Index를 우선 검색한다.

Q. API 테스트 질문은 어떤 Part를 검색하는가?
A. Part09 API Testing & Contract Verification을 우선 검색한다.

Q. Topic Routing Rule은 무엇인가?
A. 사용자 질문을 API Design 세부 Topic으로 분류하고 관련 문서를 연결하는 규칙이다.

Q. Cross Reference Matrix는 무엇인가?
A. API Design Topic 사이의 연관 관계를 정의한 검색 연결 표이다.

Q. PM Agent는 어떤 문서를 우선 검색하는가?
A. Part08 Practical API Patterns, Part01 API Core, Part02 URI Design을 우선 검색한다.

Q. Backend Agent는 어떤 문서를 우선 검색하는가?
A. Part03 Request / Response Contract, Part04 Validation / Pagination, Part08 Practical API Patterns를 우선 검색한다.

Q. Review Agent는 어떤 문서를 우선 검색하는가?
A. Part07 Agent Review, Part10 Retrieval Index, Part06 Troubleshooting을 우선 검색한다.

Q. API Design 답변에는 무엇이 포함되어야 하는가?
A. Endpoint, Request Contract, Response Contract, Error Contract, Security, Validation, Test Case가 포함되어야 한다.

Q. API Review 답변에는 무엇이 포함되어야 하는가?
A. Score, Release Decision, Severity, Problem, Impact, Cause, Fix, Retest가 포함되어야 한다.

Q. API Troubleshooting 답변에는 무엇이 포함되어야 하는가?
A. 증상, 가능 원인, 확인 순서, 수정 방법, 재검수 방법이 포함되어야 한다.

Q. Final API Quality Score는 무엇인가?
A. API 설계와 구현이 실무 적용 가능한 수준인지 정량적으로 판단하는 기준이다.

Q. API Review 목표 점수는 몇 점인가?
A. 최소 95점 이상, 목표는 97점 이상이다.

Q. Critical Issue가 있으면 점수가 높아도 배포 가능한가?
A. 아니다. Critical Issue가 있으면 점수와 관계없이 Release Blocked이다.

Q. Final Agent Checklist는 언제 사용하는가?
A. API 설계 완료 후, 구현 완료 후, Frontend 연동 전, 배포 전 최종 검수에 사용한다.

Q. API Ready 조건은 무엇인가?
A. Critical Issue가 없고 Contract, Security, Error, OpenAPI, Test Gate를 통과해야 한다.

Q. RAG Document Quality Gate는 무엇인가?
A. API Design RAG 문서 자체가 Agent Retrieval에 적합한지 검수하는 기준이다.

Q. RAG 문서에서 FAQ가 중요한 이유는 무엇인가?
A. 사용자 질문과 Agent Retrieval Query가 FAQ 형태와 잘 매칭되기 때문이다.

Q. API Retrieval에서 가장 흔한 실패는 무엇인가?
A. Endpoint만 검색하고 Request, Response, Error, Security, Test 문서를 연결하지 않는 것이다.

Q. Retrieval 실패를 줄이는 방법은 무엇인가?
A. Part10 Topic Routing과 Cross Reference Matrix를 사용해 Primary Part와 Secondary Part를 함께 검색한다.

Q. Agent가 API 질문에 일반론만 답변하면 어떻게 보완하는가?
A. Practical Pattern, Quality Gate, Test 문서를 함께 검색하도록 Routing을 강화한다.
