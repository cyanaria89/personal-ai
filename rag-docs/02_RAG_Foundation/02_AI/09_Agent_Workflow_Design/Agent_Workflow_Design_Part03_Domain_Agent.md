# Agent Workflow Design Part03 Domain Agent

---

# 1. Domain Agent Core

## 1.1 Domain Agent Definition

### [개념]

Domain Agent는 특정 전문 영역의 작업을 수행하는 실행 Agent이다.

Domain Agent는 PM Agent가 전달한 Handoff를 기준으로 자기 Domain에 해당하는 작업만 수행한다.
Domain Agent는 범용 해결사가 아니라, Role, Input, Output, Constraints, Done Criteria가 명확한 전문 담당 Agent이다.

Domain Agent 예시:

- SQL Agent
- Backend Agent
- Frontend Agent
- DevOps Agent
- AI Agent
- Security Agent
- Testing Agent
- Documentation Agent

---

### [핵심]

- Domain Agent는 특정 전문 영역에 집중한다.
- Domain Agent는 PM Agent Handoff를 입력으로 받는다.
- Domain Agent는 관련 Domain Rules와 RAG 문서를 우선 참조한다.
- Domain Agent는 자기 영역 밖 작업을 임의로 수행하지 않는다.
- Domain Agent는 Review 가능한 구조로 산출물을 작성한다.
- Domain Agent는 Decisions, Assumptions, Open Issues를 구분한다.
- Domain Agent는 Done Criteria 충족 여부를 표시한다.
- Domain Agent는 Review Agent와 Fix Agent 역할을 대신하지 않는다.

---

### [실무]

2026 실무 기준 Domain Agent는 개인 AI 개발팀의 전문 실행 담당자 역할을 수행한다.

기본 Flow:

```text
Task Input
→ Load Domain Rules
→ Retrieve Related RAG
→ Analyze Context
→ Execute Domain Task
→ Produce Structured Output
→ Return to PM Agent or Review Agent
```

Domain Agent 공통 입력:

| Input              | 설명                        |
| ------------------ | --------------------------- |
| Task               | PM Agent가 배정한 작업      |
| Context            | 작업에 필요한 프로젝트 정보 |
| Constraints        | 반드시 지켜야 할 제약 조건  |
| Domain Rules       | 해당 Domain 작업 규칙       |
| Existing Artifacts | 기존 코드, 문서, 설계       |
| Expected Output    | 기대 산출물 형식            |
| Done Criteria      | 완료 판단 기준              |

Domain Agent 공통 출력:

| Output              | 설명                       |
| ------------------- | -------------------------- |
| Summary             | 수행한 작업 요약           |
| Details             | 세부 결과                  |
| Decisions           | 확정한 판단                |
| Assumptions         | 가정                       |
| Open Issues         | 미확정 또는 차단 항목      |
| Artifacts           | 코드, 설계, 문서 등 산출물 |
| Done Criteria Check | 완료 기준 충족 여부        |
| Review Target       | 검토가 필요한 대상         |
| Next Step           | 다음 단계                  |

금지:

- 다른 Domain까지 임의 수정
- Review Agent처럼 최종 Pass / Fail 판정
- Fix Agent처럼 Review Finding 없이 임의 수정
- 존재하지 않는 프로젝트 구조 생성
- PM Agent Handoff 범위 초과
- 불확실한 정보를 사실처럼 확정
- Done Criteria 없이 완료 선언

---

### [FAQ]

Q. Domain Agent는 뭐야?
A. Backend, Frontend, SQL, DevOps, AI처럼 특정 전문 영역의 작업을 수행하는 실행 Agent이다.

Q. Domain Agent는 무엇을 입력으로 받아?
A. PM Agent의 Handoff, Task, Context, Constraints, Domain Rules, Expected Output, Done Criteria를 입력으로 받는다.

Q. Domain Agent가 모든 작업을 처리해도 돼?
A. 아니다. Domain Agent는 자기 전문 영역에 집중하고 범위를 벗어난 작업은 Open Issue나 Handoff Request로 반환해야 한다.

Q. Domain Agent 결과는 어떻게 작성해야 해?
A. Review Agent가 검증할 수 있도록 Summary, Details, Decisions, Assumptions, Open Issues, Artifacts 구조로 작성해야 한다.

---

# 2. Domain Agent Role Design

## 2.1 Role Design Principle

### [개념]

Domain Agent Role Design은 각 Domain Agent의 책임, 금지 범위, 입력, 출력, Tool 권한, 완료 기준을 정의하는 과정이다.

Role이 불명확하면 Agent 간 책임이 겹치고 Workflow가 깨진다.

---

### [핵심]

- Role은 Domain 단위로 정의한다.
- Responsibility는 수행 가능한 작업 중심으로 정의한다.
- Not Responsible은 하지 말아야 할 작업으로 정의한다.
- Input과 Output을 명확히 한다.
- Tool Access는 필요한 최소 권한만 부여한다.
- Done Criteria를 명확히 한다.
- Review Criteria와 연결 가능해야 한다.
- Cross-Domain 이슈는 직접 처리하지 않고 Handoff Request로 반환한다.

---

### [실무]

Domain Agent Role Template:

```md
## Domain Agent Role

### Agent Name

### Domain

### Responsibility

### Not Responsible

### Required Input

### Required Context

### Tool Access

### Expected Output

### Done Criteria

### Review Target
```

예시:

```md
## Domain Agent Role

### Agent Name

Backend Agent

### Domain

Spring Boot, Java, REST API, Service Layer

### Responsibility

- DTO 설계
- Service Flow 설계
- Controller Endpoint 설계
- Exception Flow 설계
- Repository 사용 흐름 검토

### Not Responsible

- Frontend UI 구현
- Docker 배포 설정
- DB Migration 직접 실행
- Security 정책 최종 승인
- Review Pass / Fail 최종 판정

### Required Input

- PM Agent Handoff
- Existing Entity / DTO / Controller
- Backend Domain Rules

### Required Context

- Spring Boot Version
- Java Version
- ApiResponse<T> 사용 여부
- GlobalExceptionHandler 사용 여부

### Tool Access

- Code Search
- RAG Retrieval

### Expected Output

- Backend Agent Output
- Code Snippet
- Service Flow
- Exception Cases

### Done Criteria

- 요구사항 충족
- 제약 조건 준수
- Review 가능한 구조

### Review Target

- API 일관성
- Validation 적절성
- Exception Flow 적절성
- 기존 구조와 충돌 없음
```

주의:

- Role을 너무 넓게 잡지 않는다.
- Tool 권한을 역할보다 넓게 주지 않는다.
- Agent 이름과 실제 책임이 다르면 안 된다.
- Review Target 없이 Domain Agent를 설계하지 않는다.

---

### [FAQ]

Q. Domain Agent Role Design은 뭐야?
A. Domain Agent의 책임, 권한, 입력, 출력, 금지 범위, 완료 기준을 정의하는 과정이다.

Q. Role Design에서 가장 중요한 것은?
A. Responsibility, Not Responsible, Expected Output, Done Criteria를 명확히 하는 것이다.

Q. Not Responsible이 왜 필요해?
A. Agent가 자기 영역을 넘어 임의로 작업하는 것을 막기 위해 필요하다.

Q. Domain Agent마다 Tool 권한을 다르게 줘야 해?
A. 그렇다. Agent 역할에 필요한 최소 Tool 권한만 부여하는 것이 안전하다.

---

# 3. Domain Agent Input

## 3.1 Domain Agent Input Definition

### [개념]

Domain Agent Input은 Domain Agent가 작업을 수행하기 위해 필요한 입력 정보이다.

Domain Agent는 사용자 요청 원문만 받아서는 안 된다.
PM Agent가 정리한 Task, Context, Constraints, Expected Output, Done Criteria를 입력으로 받아야 한다.

---

### [핵심]

- Domain Agent Input은 Handoff 기반이어야 한다.
- Task는 실행 가능한 단위여야 한다.
- Context는 작업에 필요한 정보만 포함한다.
- Constraints는 반드시 포함한다.
- Expected Output은 결과 형식을 고정한다.
- Done Criteria는 완료 판단 기준이다.
- Assumption과 Open Question은 구분한다.
- Existing Artifacts는 기존 구조와 충돌을 막기 위해 필요하다.

---

### [실무]

Domain Agent Input Template:

```md
## Domain Agent Input

### Task

### Goal

### Context

### Constraints

### Existing Artifacts

### Domain Rules

### Expected Output

### Done Criteria

### Assumptions

### Open Questions
```

예시:

```md
## Domain Agent Input

### Task

회원가입 Service Flow 설계

### Goal

사용자 회원가입 요청을 검증하고 User를 생성하는 Backend 흐름 설계

### Context

- Spring Boot 3.x
- Java 21
- ApiResponse<T> 직접 반환
- GlobalExceptionHandler 사용

### Constraints

- Password 평문 저장 금지
- 중복 이메일 처리 필요
- Entity 임의 변경 금지

### Existing Artifacts

- Users Entity
- AuthController
- SignUpReqDto

### Domain Rules

- Backend Domain Rules
- Security Domain Rules
- API Design Domain Rules

### Expected Output

- Service Flow
- Method Signature
- Exception Cases
- Validation Points

### Done Criteria

- Password Encoding 포함
- 중복 이메일 예외 포함
- Review Agent가 검증 가능한 구조

### Assumptions

- 이메일은 unique 값으로 사용

### Open Questions

- 이메일 인증 필수 여부 미확정
```

좋은 Input 조건:

- Domain Agent가 바로 작업 가능
- 불필요한 전체 대화 없음
- 제약 조건 누락 없음
- 산출물 형식 명확
- 미확정 사항 분리

---

### [FAQ]

Q. Domain Agent Input은 뭐야?
A. Domain Agent가 작업을 수행하기 위해 받는 Task, Context, Constraints, Expected Output, Done Criteria이다.

Q. 사용자 요청 원문만 Domain Agent에게 주면 안 돼?
A. 원문만 주면 제약, 산출물 형식, 완료 기준이 불명확해져 결과 품질이 낮아질 수 있다.

Q. Domain Agent Input에 반드시 들어가야 하는 것은?
A. Task, Context, Constraints, Expected Output, Done Criteria, Assumptions, Open Questions이다.

Q. Existing Artifacts는 왜 필요해?
A. 기존 코드나 문서 구조와 충돌하지 않도록 하기 위해 필요하다.

---

# 4. Domain Agent Output

## 4.1 Domain Agent Output Definition

### [개념]

Domain Agent Output은 Domain Agent가 작업 후 반환하는 구조화된 중간 산출물이다.

Domain Agent Output은 최종 사용자 답변이 아니다.
Review Agent와 PM Agent가 검증하고 통합할 수 있도록 작성해야 한다.

---

### [핵심]

- Output은 구조화되어야 한다.
- Summary와 Details를 분리한다.
- Decisions와 Assumptions를 구분한다.
- Open Issues를 숨기지 않는다.
- Artifacts는 명확히 표시한다.
- Done Criteria 충족 여부를 표시한다.
- Review Target을 지정한다.
- Next Step을 포함한다.
- Pass / Fail 최종 판정은 Review Agent 역할이다.

---

### [실무]

Domain Agent Output Template:

```md
## Domain Agent Output

### Agent

### Task

### Summary

### Details

### Decisions

### Assumptions

### Open Issues

### Artifacts

### Done Criteria Check

### Review Target

### Next Step
```

예시:

```md
## Backend Agent Output

### Agent

Backend Agent

### Task

회원가입 Service Flow 설계

### Summary

회원가입 요청 검증, 중복 이메일 확인, Password Encoding, User 저장 흐름을 설계함.

### Details

- SignUpReqDto validation 사용
- userRepository.existsByEmail(email)로 중복 확인
- passwordEncoder.encode(password) 적용
- User Entity 생성 후 저장
- UserResDto 반환

### Decisions

- Password는 BCrypt Encoding 사용
- 중복 이메일은 BusinessException 처리
- Controller는 ApiResponse<UserResDto> 직접 반환

### Assumptions

- 이메일은 unique 값으로 사용
- 이메일 인증은 이번 범위에서 제외

### Open Issues

- 이메일 인증 필수 여부 미확정

### Artifacts

- Service Flow
- Method Signature
- Exception Cases

### Done Criteria Check

- Password Encoding 포함: Yes
- 중복 이메일 처리 포함: Yes
- Review 가능한 구조: Yes

### Review Target

- Security
- Validation
- Exception Flow
- API Response Consistency

### Next Step

Review Agent 검토 필요
```

주의:

- 최종 답변처럼 작성하지 않는다.
- 코드만 제공하고 판단 근거를 생략하지 않는다.
- Review Target을 누락하지 않는다.
- Open Issue를 숨기지 않는다.
- Done Criteria를 충족하지 못했으면 완료로 표시하지 않는다.

---

### [FAQ]

Q. Domain Agent Output은 뭐야?
A. Domain Agent가 작업 후 Review Agent와 PM Agent에게 전달하는 구조화된 중간 산출물이다.

Q. Domain Agent Output은 최종 답변이야?
A. 아니다. 최종 답변 전 검증과 통합을 위한 중간 산출물이다.

Q. Domain Agent Output에 무엇을 넣어야 해?
A. Summary, Details, Decisions, Assumptions, Open Issues, Artifacts, Done Criteria Check, Review Target을 넣어야 한다.

Q. Open Issue를 왜 적어야 해?
A. 미확정 사항이나 차단 요소를 숨기지 않아야 Review와 PM 통합 단계에서 정확히 처리할 수 있다.

---

# 5. SQL Agent

## 5.1 SQL Agent Role

### [개념]

SQL Agent는 DB Schema, SQL Query, Index, Constraint, Transaction, Data Integrity를 담당하는 Domain Agent이다.

SQL Agent는 Backend Agent가 안전하게 Entity, Repository, Service를 설계할 수 있도록 DB 관점의 근거를 제공한다.

---

### [핵심]

- SQL Agent는 DB Schema와 Query를 검토한다.
- Table, Column, Primary Key, Foreign Key, Unique Constraint를 확인한다.
- Index와 Query 성능을 검토한다.
- Transaction 경계와 Data Integrity를 고려한다.
- Backend Agent가 사용할 Repository 조건을 제안할 수 있다.
- 실제 DB 변경은 사용자 승인 또는 별도 Tool 권한이 필요하다.
- SQL Agent는 DB 관점 제안만 수행하고 Backend 구현은 Backend Agent에게 넘긴다.

---

### [실무]

SQL Agent Responsibility:

| 항목               | 설명                                     |
| ------------------ | ---------------------------------------- |
| Schema Review      | 테이블, 컬럼, 제약 조건 검토             |
| Query Design       | SELECT, INSERT, UPDATE, DELETE 쿼리 설계 |
| Index Review       | 조회 조건과 정렬 기준에 맞는 Index 검토  |
| Constraint Review  | PK, FK, Unique, Not Null 검토            |
| Transaction Review | 정합성이 필요한 작업 단위 검토           |
| Repository Support | JPA Repository Method 설계 지원          |

SQL Agent Output Template:

```md
## SQL Agent Output

### Summary

### Schema Findings

### Query / Repository Suggestion

### Index Consideration

### Constraint Check

### Transaction Consideration

### Risks

### Open Issues

### Review Target
```

예시:

```md
## SQL Agent Output

### Summary

회원가입 기능을 위해 users.email unique constraint와 password 저장 정책 검토가 필요함.

### Schema Findings

- users.email 컬럼 필요
- email unique constraint 권장
- password 컬럼은 encoded password 저장 전제

### Query / Repository Suggestion

- existsByEmail(String email)
- save(Users user)

### Index Consideration

- email unique index 권장

### Constraint Check

- email: NOT NULL + UNIQUE
- password: NOT NULL

### Transaction Consideration

- 회원가입 저장은 단일 transaction 처리

### Risks

- unique constraint가 없으면 동시 가입 시 중복 이메일 가능

### Open Issues

- 실제 users table에 unique constraint가 있는지 확인 필요

### Review Target

- Schema Constraint
- Repository Method
- Transaction Boundary
```

주의:

- DB 변경을 확정하지 않고 제안으로 표시한다.
- Backend Entity와 실제 Table 구조 충돌 가능성을 확인한다.
- Query 성능을 무시하지 않는다.
- 동시성 위험을 검토한다.
- 실제 DB 수정은 Human-in-the-loop 대상이다.

---

### [FAQ]

Q. SQL Agent는 뭐야?
A. DB Schema, SQL Query, Index, Constraint, Transaction, Data Integrity를 담당하는 Domain Agent이다.

Q. SQL Agent는 언제 필요해?
A. 테이블 설계, 쿼리 작성, Repository Method, 인덱스, 제약 조건, 트랜잭션 검토가 필요할 때 필요하다.

Q. SQL Agent가 직접 DB를 변경해도 돼?
A. 기본적으로 안 된다. 실제 DB 변경은 사용자 승인 또는 별도 Tool 권한이 필요하다.

Q. SQL Agent Output에는 무엇이 들어가?
A. Schema Findings, Query Suggestion, Index Consideration, Constraint Check, Transaction Consideration, Risks가 들어간다.

---

# 6. Backend Agent

## 6.1 Backend Agent Role

### [개념]

Backend Agent는 Spring Boot, Java, REST API, Service Layer, Entity, DTO, Repository, Exception Flow를 담당하는 Domain Agent이다.

Backend Agent는 PM Agent Handoff와 Backend Domain Rules를 기준으로 Backend 산출물을 생성하거나 검토한다.

---

### [핵심]

- Backend Agent는 API와 비즈니스 흐름을 설계한다.
- DTO, Service, Controller, Repository 사용 흐름을 다룬다.
- Entity 변경은 기존 구조와 영향 범위를 확인해야 한다.
- Exception Flow와 Response Format을 일관되게 유지한다.
- Security, SQL, Frontend 영역은 필요 시 Handoff Request 또는 Review Target으로 분리한다.
- Backend Agent는 Security 정책 최종 승인이나 DB 변경 실행을 담당하지 않는다.
- 코드 생성 결과는 Review Agent가 검증 가능한 구조여야 한다.

---

### [실무]

Backend Agent Responsibility:

| 항목                | 설명                                           |
| ------------------- | ---------------------------------------------- |
| DTO Design          | Request / Response DTO 설계                    |
| Service Flow        | 비즈니스 로직 흐름 설계                        |
| Controller Endpoint | REST API endpoint 설계                         |
| Repository Usage    | Repository method 사용 흐름                    |
| Exception Flow      | BusinessException, GlobalExceptionHandler 연계 |
| Response Format     | ApiResponse<T>, ResponseEntity 사용 기준       |
| Validation          | 입력값 검증 기준                               |
| Integration Point   | SQL, Security, Frontend 연계 지점              |

Backend Agent Output Template:

```md
## Backend Agent Output

### Summary

### API Design

### DTO Design

### Service Flow

### Repository Usage

### Exception Cases

### Validation Points

### Assumptions

### Open Issues

### Review Target
```

예시:

```md
## Backend Agent Output

### Summary

회원가입 API의 DTO, Service Flow, Controller Endpoint를 설계함.

### API Design

POST /auth/signup

### DTO Design

- SignUpReqDto
- UserResDto

### Service Flow

1. SignUpReqDto validation
2. email 중복 확인
3. password encoding
4. Users entity 생성
5. userRepository.save()
6. UserResDto 반환

### Repository Usage

- existsByEmail(String email)
- save(Users user)

### Exception Cases

- DuplicateEmailException
- ValidationException

### Validation Points

- email not blank + email format
- password length
- nickname not blank

### Assumptions

- 이메일 인증은 이번 범위 제외

### Open Issues

- 이메일 인증 필수 여부 미확정

### Review Target

- API Consistency
- Validation
- Exception Flow
- Security Integration
```

주의:

- 존재하지 않는 Entity나 Repository를 임의 생성하지 않는다.
- 기존 Response Format과 충돌하지 않는다.
- Security 관련 처리는 Security Agent 검토 대상으로 분리한다.
- DB Schema 변경 필요 시 SQL Agent와 연결한다.
- Frontend 요청 형식 영향은 명시한다.

---

### [FAQ]

Q. Backend Agent는 뭐야?
A. Spring Boot, Java, REST API, Service Layer, DTO, Repository, Exception Flow를 담당하는 Domain Agent이다.

Q. Backend Agent는 무엇을 출력해?
A. API Design, DTO Design, Service Flow, Repository Usage, Exception Cases, Validation Points를 출력한다.

Q. Backend Agent가 Security까지 모두 처리해도 돼?
A. 기본 흐름은 설계할 수 있지만 인증/인가, Password, JWT 등은 Security Agent 검토가 필요하다.

Q. Backend Agent가 DB 구조를 바꿔도 돼?
A. 임의 변경하면 안 된다. DB 변경은 SQL Agent 검토와 사용자 승인 또는 명확한 요구사항이 필요하다.

---

# 7. Frontend Agent

## 7.1 Frontend Agent Role

### [개념]

Frontend Agent는 UI, Component, State, Routing, API Integration, Form Handling, Error / Loading UX를 담당하는 Domain Agent이다.

Frontend Agent는 Backend API 계약을 기준으로 사용자가 실제로 조작하는 화면과 상태 흐름을 설계하거나 구현한다.

---

### [핵심]

- Frontend Agent는 사용자 화면과 상호작용을 담당한다.
- Component 구조, State, Props, Event Flow를 설계한다.
- Backend API 계약과 Request / Response 형식을 확인한다.
- Form Validation과 Error Handling을 포함한다.
- Loading UX와 Empty State를 고려한다.
- 인증이 필요한 API는 Token Flow를 고려한다.
- Backend API를 임의로 변경하지 않는다.
- API 변경 필요성은 Open Issue 또는 Handoff Request로 반환한다.

---

### [실무]

Frontend Agent Responsibility:

| 항목             | 설명                                    |
| ---------------- | --------------------------------------- |
| Component Design | 화면과 Component 구조                   |
| State Management | local state, server state, global state |
| API Integration  | Axios, fetch, REST API 연동             |
| Form Handling    | 입력값 관리와 validation                |
| Routing          | React Router 등 화면 이동               |
| Error UX         | 실패 메시지, fallback                   |
| Loading UX       | 로딩 상태                               |
| Auth Flow        | Token 포함 요청, 로그인 상태            |

Frontend Agent Output Template:

```md
## Frontend Agent Output

### Summary

### Component Structure

### State Design

### API Integration

### Form Validation

### Error Handling

### Loading / Empty State

### Assumptions

### Open Issues

### Review Target
```

예시:

```md
## Frontend Agent Output

### Summary

회원가입 화면의 Form, API 호출, Error / Loading 상태를 설계함.

### Component Structure

- SignupPage
- SignupForm
- FormInput
- ErrorMessage

### State Design

- email
- password
- nickname
- loading
- error

### API Integration

POST /auth/signup

### Form Validation

- email format
- password length
- nickname required

### Error Handling

- duplicate email message
- validation error message
- network error fallback

### Loading / Empty State

- submit 중 button disabled
- loading text 표시

### Assumptions

- Backend 응답은 ApiResponse<UserResDto> 형식

### Open Issues

- 회원가입 성공 후 이동 경로 미확정

### Review Target

- API Contract
- UX Flow
- Error Handling
```

주의:

- Backend API 계약을 임의로 변경하지 않는다.
- 인증 상태와 Token 필요 여부를 확인한다.
- UI 스타일보다 기능 흐름과 API 연동을 우선한다.
- Error / Loading 상태를 누락하지 않는다.
- 접근성 기본 요소를 고려한다.

---

### [FAQ]

Q. Frontend Agent는 뭐야?
A. UI, Component, State, Routing, API Integration, Form Handling, Error / Loading UX를 담당하는 Domain Agent이다.

Q. Frontend Agent는 언제 필요해?
A. React 화면, 컴포넌트 설계, API 연동, 폼 처리, 사용자 UX 흐름이 필요할 때 필요하다.

Q. Frontend Agent가 Backend API를 바꿔도 돼?
A. 안 된다. API 변경 필요성이 있으면 PM Agent와 Backend Agent에게 이슈로 전달해야 한다.

Q. Frontend Agent Output에는 무엇이 들어가?
A. Component Structure, State Design, API Integration, Form Validation, Error Handling, Loading State가 들어간다.

---

# 8. DevOps Agent

## 8.1 DevOps Agent Role

### [개념]

DevOps Agent는 Docker, CI/CD, Deployment, Runtime Config, Environment Variable, Monitoring, Server Operation을 담당하는 Domain Agent이다.

DevOps Agent는 애플리케이션을 실행, 배포, 운영하기 위한 환경과 절차를 설계하거나 검토한다.

---

### [핵심]

- DevOps Agent는 실행 환경과 배포 흐름을 담당한다.
- Dockerfile, docker-compose, environment variable을 검토한다.
- CI/CD pipeline과 배포 전략을 설계한다.
- 서버 운영, 로그, 모니터링, 백업을 고려한다.
- 비용 발생, 외부 배포, 서버 변경은 사용자 승인 대상이다.
- 보안 Secret은 노출하지 않는다.
- 실제 배포 실행은 Tool 권한과 사용자 승인이 필요하다.

---

### [실무]

DevOps Agent Responsibility:

| 항목        | 설명                            |
| ----------- | ------------------------------- |
| Docker      | Dockerfile, docker-compose 구성 |
| Environment | .env, Secret, Config 관리       |
| Deployment  | 배포 절차, 서버 구성            |
| CI/CD       | Build, Test, Deploy Pipeline    |
| Runtime     | Port, Volume, Network           |
| Monitoring  | Log, Health Check, Metrics      |
| Backup      | DB Backup, Recovery             |
| Security    | Secret 관리, 권한 최소화        |

DevOps Agent Output Template:

```md
## DevOps Agent Output

### Summary

### Runtime Environment

### Docker / Compose Design

### Environment Variables

### Deployment Flow

### CI/CD Consideration

### Monitoring / Logging

### Risks

### User Confirmation Required

### Review Target
```

예시:

```md
## DevOps Agent Output

### Summary

Spring Boot + MySQL 배포를 위한 docker-compose 구성 검토.

### Runtime Environment

- Java 21
- Spring Boot 3.x
- MySQL 8.x

### Docker / Compose Design

- app service
- mysql service
- persistent volume

### Environment Variables

- DB_URL
- DB_USERNAME
- DB_PASSWORD
- JWT_SECRET

### Deployment Flow

1. build jar
2. build image
3. compose up
4. health check

### CI/CD Consideration

- test stage
- build stage
- deploy stage

### Monitoring / Logging

- container logs
- health endpoint

### Risks

- Secret 노출 위험
- DB volume 삭제 위험
- port 충돌 가능성

### User Confirmation Required

실제 서버 배포 또는 DB volume 삭제 시 필요

### Review Target

- Config Safety
- Secret Handling
- Deployment Risk
```

주의:

- Secret 값을 출력하지 않는다.
- 실제 서버 변경은 사용자 승인 필요.
- 파일 삭제, volume 삭제, DB 초기화는 위험 작업이다.
- 로컬 개발 환경과 운영 환경을 구분한다.
- 비용 발생 가능성을 표시한다.

---

### [FAQ]

Q. DevOps Agent는 뭐야?
A. Docker, CI/CD, Deployment, Runtime Config, Environment Variable, Monitoring, Server Operation을 담당하는 Domain Agent이다.

Q. DevOps Agent는 언제 필요해?
A. Docker 구성, 배포, 서버 운영, CI/CD, 환경변수 관리, 로그와 모니터링 설계가 필요할 때 필요하다.

Q. DevOps Agent가 실제 배포를 실행해도 돼?
A. 사용자 승인과 Tool 권한이 있을 때만 가능하다.

Q. DevOps Agent가 주의해야 할 것은?
A. Secret 노출, DB volume 삭제, 서버 변경, 비용 발생, 권한 과다 부여를 주의해야 한다.

---

# 9. AI Agent

## 9.1 AI Agent Role

### [개념]

AI Agent는 RAG, LLM, Prompt Engineering, Tool Calling, Agent Workflow, Memory, Evaluation을 담당하는 Domain Agent이다.

AI Agent는 개인 AI 서버와 Multi-Agent System의 AI 기능 설계와 개선을 담당한다.

---

### [핵심]

- AI Agent는 RAG와 LLM 연동을 설계한다.
- Prompt, System Instruction, Retrieval Query를 개선한다.
- Tool Calling 구조와 Tool Result 검증을 설계한다.
- Agent Workflow와 Handoff를 설계한다.
- Memory와 Shared State 사용 기준을 정리한다.
- RAG Evaluation과 Retrieval Optimization을 검토한다.
- 모델 한계와 불확실성을 명시한다.
- AI Agent는 Review Agent의 품질 판정을 대신하지 않는다.

---

### [실무]

AI Agent Responsibility:

| 항목               | 설명                                           |
| ------------------ | ---------------------------------------------- |
| RAG Design         | 문서 검색, Chunk, Retrieval 구조               |
| Prompt Engineering | System Prompt, Instruction, Output Format      |
| Agent Workflow     | PM, Domain, Review, Fix 흐름                   |
| Tool Calling       | Tool 선택, 실행, 결과 검증                     |
| Memory             | Short-term, Long-term, Shared State            |
| Evaluation         | Answer Quality, Retrieval Quality              |
| Model Strategy     | Local LLM, Embedding, Context Window           |
| Failure Handling   | Retrieval Failure, Hallucination, Tool Failure |

AI Agent Output Template:

```md
## AI Agent Output

### Summary

### AI Architecture

### RAG Strategy

### Prompt / Instruction Design

### Tool Calling Design

### Memory / State Design

### Evaluation Criteria

### Risks

### Open Issues

### Review Target
```

예시:

```md
## AI Agent Output

### Summary

개인 AI 개발팀을 위한 PM Agent 중심 Workflow와 RAG 검색 전략을 설계함.

### AI Architecture

- PM Agent
- SQL Agent
- Backend Agent
- Review Agent

### RAG Strategy

- Domain Rules 우선 검색
- 관련 Part 문서 검색
- Retrieval Queries 기반 Query 확장

### Prompt / Instruction Design

- Role 고정
- Output Format 고정
- Assumption 표시 의무화

### Tool Calling Design

- 위험 Tool은 Human Confirmation 필요
- Tool Result 검증 후 Shared State 반영

### Memory / State Design

- Short-term State: 현재 작업
- Long-term Memory: 프로젝트 결정 사항

### Evaluation Criteria

- Retrieval Hit
- Grounded Answer
- Review Pass Rate
- Failure Rate

### Risks

- Agent 수 증가에 따른 Latency
- RAG 검색 실패 시 환각 위험

### Open Issues

- LangGraph 상세 구현 여부 미확정

### Review Target

- Workflow Stability
- RAG Grounding
- Failure Handling
```

주의:

- 검색 실패를 숨기지 않는다.
- 일반 지식을 RAG 근거처럼 표현하지 않는다.
- 모델 한계를 명시한다.
- Agent 수를 과도하게 늘리지 않는다.
- Tool 권한을 Agent별로 제한한다.

---

### [FAQ]

Q. AI Agent는 뭐야?
A. RAG, LLM, Prompt Engineering, Tool Calling, Agent Workflow, Memory, Evaluation을 담당하는 Domain Agent이다.

Q. AI Agent는 언제 필요해?
A. RAG 구조, Agent Workflow, Prompt, Tool Calling, Memory, Evaluation 설계가 필요할 때 필요하다.

Q. AI Agent가 주의해야 할 것은?
A. Retrieval 실패, Hallucination, Tool 결과 오해, Agent 복잡도 증가, 모델 한계를 주의해야 한다.

Q. AI Agent Output에는 무엇이 들어가?
A. AI Architecture, RAG Strategy, Prompt Design, Tool Calling Design, Memory Design, Evaluation Criteria가 들어간다.

---

# 10. Security Agent

## 10.1 Security Agent Role

### [개념]

Security Agent는 Authentication, Authorization, JWT, OAuth2, Password Encoding, Access Control, Security Risk를 담당하는 Domain Agent이다.

Security Agent는 Backend Agent와 DevOps Agent의 결과를 보안 관점에서 검토하거나 보안 흐름을 설계한다.

Security Agent는 Review Agent가 아니다.
Security Agent는 보안 Domain 관점의 산출물과 위험 분석을 제공하고, 최종 Review Pass / Fail은 Review Agent가 수행한다.

---

### [핵심]

- Security Agent는 인증과 인가 흐름을 검토한다.
- Password는 평문 저장 금지.
- JWT, Access Token, Refresh Token 흐름을 검토한다.
- 권한별 접근 제어를 확인한다.
- Security Filter Chain과 CORS 정책을 검토한다.
- Secret과 환경변수 노출을 주의한다.
- 보안 위험은 Review Target으로 명확히 전달한다.
- 최종 Severity 판정은 Review Agent 기준과 연결한다.

---

### [실무]

Security Agent Responsibility:

| 항목            | 설명                        |
| --------------- | --------------------------- |
| Authentication  | 로그인, 인증 흐름           |
| Authorization   | 권한 확인, Role 기반 접근   |
| Password        | BCrypt 등 Encoding          |
| JWT             | Access Token, Refresh Token |
| OAuth2          | 소셜 로그인 흐름            |
| Filter Chain    | Spring Security Filter 구조 |
| CORS / CSRF     | 요청 보안 정책              |
| Secret Handling | JWT Secret, API Key 보호    |
| Security Risk   | 취약점과 위험 요소 식별     |

Security Agent Output Template:

```md
## Security Agent Output

### Summary

### Authentication Check

### Authorization Check

### Password Policy

### Token Flow

### Security Risks

### Required Fix Candidates

### Assumptions

### Open Issues

### Review Target
```

예시:

```md
## Security Agent Output

### Summary

회원가입 Flow에서 Password Encoding과 Endpoint 접근 정책을 보안 관점에서 검토함.

### Authentication Check

- 회원가입 자체는 인증 전 접근 허용 가능

### Authorization Check

- /auth/signup endpoint는 permitAll 대상

### Password Policy

- Password 평문 저장 금지
- BCrypt Encoding 적용 필요

### Token Flow

- 회원가입 완료 시 Token 발급 여부는 정책 결정 필요

### Security Risks

- Password Encoding 누락 시 심각한 보안 위험
- 회원가입 후 Token 자동 발급 정책 미정

### Required Fix Candidates

- passwordEncoder.encode() 적용
- 회원가입 후 로그인 요구 또는 Token 발급 정책 명확화

### Assumptions

- JWT 발급은 로그인 API에서 처리

### Open Issues

- 회원가입 직후 Token 발급 여부 미확정

### Review Target

- Password Encoding
- Endpoint Access Rule
- Token Policy
```

주의:

- 보안 위험을 취향 문제처럼 취급하지 않는다.
- Secret 값을 출력하지 않는다.
- 인증과 인가를 혼동하지 않는다.
- 보안 정책 미확정 사항은 Open Issue로 표시한다.
- 실제 권한 변경은 영향 범위를 표시한다.

---

### [FAQ]

Q. Security Agent는 뭐야?
A. Authentication, Authorization, JWT, OAuth2, Password Encoding, Access Control, Security Risk를 담당하는 Domain Agent이다.

Q. Security Agent는 언제 필요해?
A. 로그인, 회원가입, JWT, 권한, Password, Security Filter Chain, CORS, Secret 관리가 포함될 때 필요하다.

Q. Password는 어떻게 처리해야 해?
A. 평문 저장 금지이며 BCrypt 같은 Password Encoder를 사용해 저장해야 한다.

Q. Security Agent와 Review Agent는 같아?
A. 아니다. Security Agent는 보안 Domain 분석을 수행하고, Review Agent는 전체 산출물을 기준에 따라 최종 검증한다.

---

# 11. Testing Agent

## 11.1 Testing Agent Role

### [개념]

Testing Agent는 테스트 전략, 테스트 케이스, 단위 테스트, 통합 테스트, Mock, Test Data, Pass / Fail Criteria를 담당하는 Domain Agent이다.

Testing Agent는 Domain Agent 산출물이 실제 요구사항을 검증할 수 있도록 테스트 관점의 산출물을 만든다.

Testing Agent는 Review Agent가 아니다.
Testing Agent는 테스트 설계와 검증 케이스를 만들고, 최종 산출물 품질 판정은 Review Agent가 수행한다.

---

### [핵심]

- Testing Agent는 테스트 대상과 기준을 정의한다.
- 성공 케이스와 실패 케이스를 모두 포함한다.
- Repository, Service, Controller 테스트 전략을 구분한다.
- Mock, Test Data, Expected Result를 명확히 한다.
- Pass / Fail Criteria를 포함한다.
- 보안, 예외, Validation 케이스를 누락하지 않는다.
- 테스트 불가 항목은 Open Issue로 표시한다.
- 테스트 결과와 테스트 설계를 구분한다.

---

### [실무]

Testing Agent Responsibility:

| 항목             | 설명                       |
| ---------------- | -------------------------- |
| Test Strategy    | 테스트 범위와 방식         |
| Test Case        | 성공/실패 케이스           |
| Unit Test        | Service, Utility 등        |
| Repository Test  | DB Query, JPA Method       |
| Controller Test  | MockMvc, API 응답          |
| Integration Test | 실제 흐름 통합 검증        |
| Test Data        | 입력값과 기대 결과         |
| Pass Criteria    | 통과 기준                  |
| Defect Candidate | 결함 후보와 확인 필요 항목 |

Testing Agent Output Template:

```md
## Testing Agent Output

### Summary

### Test Scope

### Test Strategy

### Test Cases

| ID  | Target | Scenario | Input | Expected Result | Priority |
| --- | ------ | -------- | ----- | --------------- | -------- |

### Test Data

### Pass / Fail Criteria

### Open Issues

### Review Target
```

예시:

```md
## Testing Agent Output

### Summary

회원가입 API 테스트 케이스를 성공, 중복 이메일, Validation 실패, Password Encoding 기준으로 작성함.

### Test Scope

- AuthController
- UserService
- UserRepository

### Test Strategy

- Service: JUnit + Mockito
- Controller: MockMvc
- Repository: @DataJpaTest

### Test Cases

| ID     | Target     | Scenario          | Input                | Expected Result       | Priority |
| ------ | ---------- | ----------------- | -------------------- | --------------------- | -------- |
| TC-001 | Service    | 정상 회원가입     | valid email/password | User 저장 성공        | P1       |
| TC-002 | Service    | 중복 이메일       | existing email       | BusinessException     | P1       |
| TC-003 | Controller | Validation 실패   | invalid email        | 400 response          | P1       |
| TC-004 | Service    | Password Encoding | raw password         | encoded password 저장 | P1       |

### Pass / Fail Criteria

- 모든 P1 테스트 통과
- Password 평문 저장 없음
- 예외 응답 형식 일관성 유지

### Open Issues

- 이메일 인증 테스트는 정책 미확정으로 제외

### Review Target

- Test Coverage
- Failure Case
- Security Case
```

주의:

- 성공 케이스만 작성하지 않는다.
- 테스트 우선순위를 표시한다.
- 실제 확인 불가능한 항목은 가정으로 처리하지 않는다.
- 단위 테스트와 통합 테스트를 혼동하지 않는다.
- 테스트 설계와 Review Finding을 혼동하지 않는다.

---

### [FAQ]

Q. Testing Agent는 뭐야?
A. 테스트 전략, 테스트 케이스, 단위 테스트, 통합 테스트, Mock, Test Data, Pass / Fail Criteria를 담당하는 Domain Agent이다.

Q. Testing Agent는 언제 필요해?
A. 기능 검증, 테스트 케이스 작성, Controller / Service / Repository 테스트 전략이 필요할 때 필요하다.

Q. 테스트 케이스에는 무엇이 들어가야 해?
A. Target, Scenario, Input, Expected Result, Priority, Pass / Fail Criteria가 들어가야 한다.

Q. Testing Agent와 Review Agent는 같아?
A. 아니다. Testing Agent는 테스트 설계 담당이고, Review Agent는 산출물 품질 검증 담당이다.

---

# 12. Documentation Agent

## 12.1 Documentation Agent Role

### [개념]

Documentation Agent는 RAG 문서, API 문서, README, 개발 규칙 문서, 운영 문서, 변경 기록을 담당하는 Domain Agent이다.

Documentation Agent는 사람용 장문 문서보다 검색 가능하고 검증 가능한 구조화 문서를 우선한다.

---

### [핵심]

- Documentation Agent는 문서를 구조화한다.
- RAG 문서는 Retrieval 최적화를 우선한다.
- API 문서는 Endpoint, Request, Response, Error를 포함한다.
- 운영 문서는 절차, 위험, 복구 방법을 포함한다.
- 변경 기록은 결정 사항과 영향 범위를 기록한다.
- FAQ와 Retrieval Queries를 강화한다.
- 용어 통일과 중복 제거를 수행한다.
- Documentation Agent는 문서 품질 기준을 제공하고 Review Agent는 최종 검증한다.

---

### [실무]

Documentation Agent Responsibility:

| 항목              | 설명                               |
| ----------------- | ---------------------------------- |
| RAG Document      | Agent Retrieval 최적화 문서        |
| API Document      | Endpoint, Request, Response, Error |
| README            | 실행 방법, 환경 구성               |
| Operation Guide   | 배포, 백업, 장애 대응              |
| Change Log        | 변경 사항과 영향                   |
| Domain Rules      | 기술 도메인별 작성 규칙            |
| FAQ               | Query Pattern Matching             |
| Retrieval Queries | 검색 최적화 블록                   |

Documentation Agent Output Template:

```md
## Documentation Agent Output

### Summary

### Document Type

### Target Reader / Target Agent

### Structure

### Key Terms

### FAQ

### Retrieval Queries

### Consistency Check

### Open Issues

### Review Target
```

예시:

```md
## Documentation Agent Output

### Summary

Backend API Design RAG 문서 구조를 Retrieval 최적화 기준으로 정리함.

### Document Type

RAG Domain Document

### Target Reader / Target Agent

Backend Agent, Review Agent

### Structure

- [개념]
- [핵심]
- [실무]
- [FAQ]
- Retrieval Queries

### Key Terms

- REST API
- Controller
- Service
- DTO
- ApiResponse<T>
- GlobalExceptionHandler

### FAQ

- Q/A 형식
- 1~4줄 답변
- 실제 사용자 질문 표현 포함

### Retrieval Queries

- API 설계는 어떻게 해?
- Controller 응답은 뭘 반환해?
- ApiResponse<T>는 언제 사용해?

### Consistency Check

- 용어 통일
- 중복 설명 제거
- Chunk 단위 독립성 확인

### Open Issues

- 프로젝트별 API 응답 표준 추가 필요

### Review Target

- Retrieval Quality
- Naming Consistency
- FAQ Coverage
```

주의:

- 사람용 에세이형 문서 금지
- FAQ 없이 문서 종료 금지
- Retrieval Queries 누락 금지
- 중복 설명 과다 금지
- 긴 문단보다 구조화된 Chunk 우선

---

### [FAQ]

Q. Documentation Agent는 뭐야?
A. RAG 문서, API 문서, README, 개발 규칙 문서, 운영 문서, 변경 기록을 담당하는 Domain Agent이다.

Q. Documentation Agent는 RAG 문서를 어떻게 작성해?
A. Header, Code Block, Table, FAQ, Retrieval Queries를 사용해 검색 친화적으로 작성한다.

Q. 사람용 문서와 RAG 문서는 달라?
A. 다르다. RAG 문서는 사람이 처음부터 끝까지 읽기보다 Agent Retrieval과 검증을 우선한다.

Q. Documentation Agent Output에는 무엇이 들어가?
A. Document Type, Target Agent, Structure, Key Terms, FAQ, Retrieval Queries, Consistency Check가 들어간다.

---

# 13. Domain Agent RAG Usage

## 13.1 RAG Usage Definition

### [개념]

Domain Agent RAG Usage는 Domain Agent가 작업 수행 전 관련 RAG 문서와 Domain Rules를 검색하고 사용하는 방식이다.

Domain Agent는 자기 Domain에 맞는 문서를 우선 검색해야 한다.
검색 실패 시 일반 지식을 확정 답변처럼 사용하지 않고 Retrieval Failure 또는 Assumption으로 표시해야 한다.

---

### [핵심]

- Domain Agent는 작업 전 관련 RAG를 검색한다.
- Domain Rules를 우선 참조한다.
- Project Rules와 충돌하면 현재 요청과 최신 결정 사항을 우선한다.
- 검색 범위는 Domain 기준으로 제한한다.
- 검색 결과는 Output의 근거로 사용한다.
- Retrieval 실패는 숨기지 않는다.
- 관련 없는 Context 과다 주입을 피한다.

---

### [실무]

Domain RAG Retrieval Flow:

```text
Task Input
→ Identify Domain
→ Generate Search Query
→ Retrieve Domain Rules
→ Retrieve Related Part Documents
→ Filter Relevant Context
→ Execute Task
→ Produce Grounded Output
```

Search Query Template:

```md
## Search Query Generation

### Domain

### Task

### Required Concepts

### Query Candidates

### Excluded Scope
```

예시:

```md
## Search Query Generation

### Domain

Backend, Security

### Task

회원가입 API 설계

### Required Concepts

- DTO Validation
- Password Encoding
- BusinessException
- ApiResponse<T>
- GlobalExceptionHandler

### Query Candidates

- 회원가입 API 설계 DTO Service Controller
- Spring Boot password encoding signup
- ApiResponse GlobalExceptionHandler 회원가입
- 중복 이메일 BusinessException 처리

### Excluded Scope

- Frontend 화면 구현
- Docker 배포
```

주의:

- 모든 RAG Context를 그대로 주입하지 않는다.
- 관련 Chunk만 선택한다.
- 오래된 문서와 최신 Project Progress가 충돌하면 최신 결정 우선.
- 검색 실패를 성공처럼 처리하지 않는다.
- 출처 없는 내용을 확정 규칙처럼 사용하지 않는다.

---

### [FAQ]

Q. Domain Agent는 RAG를 어떻게 사용해?
A. 작업 Domain을 식별하고 Domain Rules와 관련 Part 문서를 검색한 뒤, 필요한 Context만 사용한다.

Q. Domain Rules와 일반 RAG 문서 중 무엇을 먼저 봐야 해?
A. Domain Rules를 먼저 보고, 이후 관련 Part 문서를 참조한다.

Q. 검색 결과가 없으면 어떻게 해?
A. Retrieval Failure로 표시하고, 필요한 경우 Assumption을 명시한 제한적 답변을 생성한다.

Q. 관련 없는 RAG Context를 많이 넣으면 좋아?
A. 아니다. 핵심 제약이 묻히고 Token 낭비가 발생해 결과 품질이 낮아질 수 있다.

---

# 14. Domain Agent Tool Usage

## 14.1 Tool Usage Definition

### [개념]

Domain Agent Tool Usage는 Domain Agent가 외부 시스템, 코드 검색, 파일, DB, API, 배포 도구 등을 사용할 때의 기준이다.

Tool은 Agent가 직접 알 수 없는 정보나 외부 작업을 수행하기 위해 사용한다.
Tool 사용 결과는 검증 후 Shared State에 반영해야 한다.

---

### [핵심]

- Tool은 필요할 때만 사용한다.
- Tool 권한은 Agent 역할에 맞게 제한한다.
- Tool 실행 전 입력값을 검증한다.
- Tool Result는 검증 후 사용한다.
- Tool Failure는 숨기지 않는다.
- Side Effect가 있는 Tool은 사용자 확인이 필요하다.
- 위험 Tool은 Human-in-the-loop를 적용한다.

---

### [실무]

Tool Usage Flow:

```text
Need External Action
→ Select Tool
→ Validate Arguments
→ Check Permission
→ Execute Tool
→ Validate Result
→ Update Shared State
→ Continue or Stop
```

Tool Usage Template:

```md
## Tool Usage

### Tool Need

### Selected Tool

### Permission Check

### Arguments

### Expected Result

### Risk

### User Confirmation Required

### Tool Result

### Validation

### State Update
```

Tool 사용 기준:

| Tool Type        | 예시                       | 확인 필요 |
| ---------------- | -------------------------- | --------- |
| Read-only Tool   | 코드 검색, 문서 검색       | 낮음      |
| Write Tool       | 파일 수정, Draft 생성      | 중간      |
| External Action  | 이메일 전송, 배포, DB 변경 | 높음      |
| Destructive Tool | 삭제, 초기화, volume 제거  | 매우 높음 |

주의:

- Tool 결과를 무조건 신뢰하지 않는다.
- 실패한 Tool을 성공처럼 처리하지 않는다.
- 삭제, 배포, 비용 발생 작업은 승인 필요.
- Agent 역할과 무관한 Tool 사용 금지.
- Tool Result를 Output에 근거로 표시한다.

---

### [FAQ]

Q. Domain Agent는 Tool을 언제 사용해?
A. 코드 검색, 문서 검색, 파일 확인, DB 조회, API 호출, 배포처럼 외부 정보나 작업이 필요할 때 사용한다.

Q. Tool 권한은 Agent마다 달라야 해?
A. 그렇다. 각 Agent 역할에 필요한 최소 권한만 부여해야 한다.

Q. Tool Result는 바로 믿어도 돼?
A. 아니다. Tool Result를 검증하고, 실패나 불일치는 Failure Handling으로 처리해야 한다.

Q. 위험 Tool은 어떻게 처리해?
A. 파일 삭제, DB 변경, 배포, 비용 발생 작업은 사용자 확인 후 진행해야 한다.

---

# 15. Domain Agent Scope Control

## 15.1 Scope Control Definition

### [개념]

Domain Agent Scope Control은 Domain Agent가 PM Agent Handoff 범위를 벗어나지 않도록 제한하는 규칙이다.

Domain Agent는 자기 Domain의 Task만 수행하고, 다른 Domain 작업이나 요청 범위 밖의 기능 추가를 임의로 진행하지 않는다.

---

### [핵심]

- PM Agent Handoff의 In Scope를 따른다.
- Out of Scope 작업은 수행하지 않는다.
- 다른 Domain 이슈는 Open Issue 또는 Handoff Request로 반환한다.
- 기존 구조 변경 시 영향 범위를 명시한다.
- 기능 확장은 Deferred Task로 분리한다.
- 위험 작업은 사용자 승인 필요 대상으로 표시한다.
- Done Criteria를 벗어난 작업을 임의로 추가하지 않는다.

---

### [실무]

Domain Scope Control Template:

```md
## Domain Scope Control

### In Scope

### Out of Scope

### Detected Cross-Domain Issues

### Deferred Tasks

### Risky Changes

### Handoff Request

### User Confirmation Required
```

예시:

```md
## Domain Scope Control

### In Scope

- 회원가입 Service Flow
- DTO Validation
- Controller Endpoint

### Out of Scope

- Frontend 회원가입 화면
- 이메일 인증 구현
- Docker 배포

### Detected Cross-Domain Issues

- Password Encoding은 Security Agent 검토 필요
- users.email unique constraint는 SQL Agent 검토 필요

### Deferred Tasks

- 이메일 인증 정책 결정 후 추가 설계

### Risky Changes

- users table 구조 변경 필요 가능성

### Handoff Request

- To: SQL Agent
- Task: users.email unique constraint 확인

### User Confirmation Required

No
```

금지:

- 요청하지 않은 기능 추가
- 다른 Agent 책임 범위 침범
- 기존 API 계약 임의 변경
- DB Schema 임의 변경
- 배포 또는 삭제 작업 자동 실행

---

### [FAQ]

Q. Domain Agent Scope Control은 뭐야?
A. Domain Agent가 PM Agent Handoff 범위와 자기 Domain을 벗어나지 않도록 제한하는 규칙이다.

Q. 다른 Domain 문제가 발견되면 어떻게 해?
A. 직접 처리하지 않고 Open Issue, Deferred Task, Handoff Request로 반환한다.

Q. Domain Agent가 기능을 추가로 제안해도 돼?
A. 제안은 가능하지만 임의 구현은 안 된다. Deferred Task로 분리해야 한다.

Q. 기존 API나 DB 구조 변경이 필요하면?
A. 영향 범위를 명시하고 PM Agent 또는 관련 Domain Agent에게 Handoff해야 한다.

---

# 16. Domain Agent Done Criteria

## 16.1 Done Criteria Definition

### [개념]

Domain Agent Done Criteria는 Domain Agent 작업이 완료되었는지 판단하는 기준이다.

Done Criteria가 없으면 Agent가 불완전한 결과를 완료로 표시할 수 있다.

---

### [핵심]

- Done Criteria는 PM Agent Handoff에 포함되어야 한다.
- Domain Agent는 Done Criteria 충족 여부를 Output에 표시한다.
- Critical 누락이 있으면 완료로 표시하지 않는다.
- Open Issue가 있으면 완료와 미완료를 구분한다.
- Review Agent가 Done Criteria를 기준으로 검증한다.
- Done Criteria는 구체적이고 확인 가능해야 한다.

---

### [실무]

Done Criteria Template:

```md
## Done Criteria Check

| Criteria | Status             | Evidence | Note |
| -------- | ------------------ | -------- | ---- |
|          | Yes / No / Partial |          |      |
```

예시:

```md
## Done Criteria Check

| Criteria                 | Status  | Evidence                            | Note                 |
| ------------------------ | ------- | ----------------------------------- | -------------------- |
| DTO Validation 포함      | Yes     | SignUpReqDto validation 정의        |                      |
| Password Encoding 포함   | Yes     | passwordEncoder.encode() 흐름 포함  | Security Review 필요 |
| 중복 이메일 처리 포함    | Yes     | existsByEmail() + BusinessException |                      |
| ApiResponse<T> 형식 유지 | Yes     | Controller 반환 형식 명시           |                      |
| 이메일 인증 정책 반영    | Partial | 정책 미확정                         | Open Issue           |
```

완료 상태:

```text
completed
partial
blocked
failed
review_required
```

주의:

- Partial을 completed로 표시하지 않는다.
- Evidence 없이 Yes 처리하지 않는다.
- Open Issue가 Critical이면 blocked로 표시한다.
- Done Criteria가 바뀌면 PM Agent가 업데이트해야 한다.

---

### [FAQ]

Q. Done Criteria는 뭐야?
A. Domain Agent 작업이 완료되었는지 판단하는 구체적 기준이다.

Q. Done Criteria는 누가 정해?
A. PM Agent가 Handoff에 포함하고, Domain Agent와 Review Agent가 이를 기준으로 작업과 검증을 수행한다.

Q. Done Criteria를 충족하지 못하면?
A. partial, blocked, failed, review_required 중 하나로 표시해야 한다.

Q. Evidence가 왜 필요해?
A. Review Agent가 완료 여부를 검증할 수 있어야 하기 때문이다.

---

# 17. Domain Agent Anti-Patterns

## 17.1 Domain Agent Anti-Patterns Definition

### [개념]

Domain Agent Anti-Patterns는 Domain Agent 설계와 실행에서 피해야 하는 잘못된 패턴이다.

대부분의 문제는 역할 범위 초과, Context 부족, Output 비구조화, Review 불가능한 결과에서 발생한다.

---

### [핵심]

- 자기 Domain 밖 작업을 임의 수행
- Handoff 없이 사용자 요청만 보고 작업
- Constraints 무시
- Existing Artifacts 확인 없이 구조 생성
- 불확실한 정보를 사실처럼 확정
- Output Format 없이 장문 설명
- Open Issue 숨김
- Done Criteria 없이 완료 선언
- Tool 결과 검증 없이 사용
- Review Target 누락
- Review Agent 역할 침범
- Fix Agent 역할 침범
- 실패를 성공처럼 처리

---

### [실무]

Anti-Pattern:

```text
Backend Agent가 회원가입 요청을 받고 DB Schema, Frontend Form, Docker 배포까지 모두 설계함
```

문제:

- Backend Agent 책임 범위 초과
- SQL / Frontend / DevOps Agent 역할 침범
- Review 기준 불명확
- Scope Control 실패

개선:

```text
Backend Agent
→ Backend Flow만 설계
→ SQL 이슈는 SQL Agent Handoff Request
→ Frontend 이슈는 Frontend Agent Handoff Request
→ DevOps 이슈는 Deferred Task
```

Anti-Pattern:

```md
## Backend Agent Output

회원가입은 이메일과 비밀번호를 받아 저장하면 됩니다.
```

문제:

- DTO 없음
- Service Flow 없음
- Exception Case 없음
- Password Encoding 언급 없음
- Review 불가능

개선:

```md
## Backend Agent Output

### Summary

### DTO Design

### Service Flow

### Repository Usage

### Exception Cases

### Validation Points

### Review Target
```

Anti-Pattern:

```text
Security Agent가 보안 분석 후 Review Pass를 최종 선언함
```

문제:

- Security Agent가 Review Agent 역할을 침범
- 전체 요구사항 기준 검증 누락 가능
- PM Agent Final Integration 기준 불명확

개선:

```text
Security Agent
→ Security Risks와 Required Fix Candidates 제공
→ Review Agent가 전체 산출물 기준으로 Pass / Fail 판정
```

---

### [FAQ]

Q. Domain Agent의 가장 흔한 실수는?
A. 자기 Domain 밖 작업을 임의로 수행하거나 Handoff 없이 사용자 요청만 보고 작업하는 것이다.

Q. Domain Agent Output이 장문 설명이면 왜 문제야?
A. Review Agent와 PM Agent가 검증하고 통합하기 어렵기 때문이다.

Q. Domain Agent가 불확실한 내용을 확정하면 어떻게 돼?
A. 잘못된 결정이 Shared State에 퍼지고 이후 Agent 작업 전체가 흔들릴 수 있다.

Q. Domain Agent Anti-Pattern을 막으려면?
A. Role, Input, Output, Constraints, Done Criteria, Review Target을 명확히 해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Domain Agent는 뭐야?
A. Backend, Frontend, SQL, DevOps, AI처럼 특정 전문 영역의 작업을 수행하는 실행 Agent이다.

Q. Domain Agent의 핵심 역할은?
A. PM Agent가 전달한 Handoff를 기준으로 자기 Domain 작업을 수행하고 Review 가능한 산출물을 만드는 것이다.

Q. Domain Agent는 무엇을 입력으로 받아?
A. Task, Context, Constraints, Existing Artifacts, Domain Rules, Expected Output, Done Criteria를 입력으로 받는다.

Q. Domain Agent Output에는 무엇이 들어가?
A. Summary, Details, Decisions, Assumptions, Open Issues, Artifacts, Done Criteria Check, Review Target이 들어간다.

Q. Domain Agent가 모든 작업을 처리해도 돼?
A. 아니다. 자기 전문 영역에 집중하고 다른 Domain 작업은 Handoff Request 또는 Open Issue로 반환해야 한다.

Q. Domain Agent와 Review Agent는 같아?
A. 아니다. Domain Agent는 전문 영역 작업을 수행하고, Review Agent는 산출물의 품질과 기준 충족 여부를 검증한다.

Q. Domain Agent와 Fix Agent는 같아?
A. 아니다. Domain Agent는 전문 작업 산출물을 만들고, Fix Agent는 Review Finding을 기준으로 수정한다.

Q. Domain Agent Role Design은 뭐야?
A. Domain Agent의 책임, 권한, 입력, 출력, 금지 범위, 완료 기준을 정의하는 과정이다.

Q. Domain Agent Role Design에서 중요한 것은?
A. Responsibility, Not Responsible, Expected Output, Done Criteria, Review Target을 명확히 하는 것이다.

Q. Not Responsible이 왜 필요해?
A. Agent가 자기 영역을 넘어 임의로 작업하는 것을 막기 위해 필요하다.

Q. SQL Agent는 뭐야?
A. DB Schema, SQL Query, Index, Constraint, Transaction, Data Integrity를 담당하는 Domain Agent이다.

Q. SQL Agent는 언제 필요해?
A. 테이블 설계, 쿼리 작성, Repository Method, 인덱스, 제약 조건, 트랜잭션 검토가 필요할 때 필요하다.

Q. SQL Agent가 직접 DB를 변경해도 돼?
A. 기본적으로 안 된다. 실제 DB 변경은 사용자 승인 또는 별도 Tool 권한이 필요하다.

Q. Backend Agent는 뭐야?
A. Spring Boot, Java, REST API, Service Layer, DTO, Repository, Exception Flow를 담당하는 Domain Agent이다.

Q. Backend Agent는 무엇을 출력해?
A. API Design, DTO Design, Service Flow, Repository Usage, Exception Cases, Validation Points를 출력한다.

Q. Backend Agent가 Security까지 모두 처리해도 돼?
A. 기본 흐름은 설계할 수 있지만 인증/인가, Password, JWT 등은 Security Agent 검토가 필요하다.

Q. Frontend Agent는 뭐야?
A. UI, Component, State, Routing, API Integration, Form Handling, Error / Loading UX를 담당하는 Domain Agent이다.

Q. Frontend Agent가 Backend API를 바꿔도 돼?
A. 안 된다. API 변경 필요성이 있으면 PM Agent와 Backend Agent에게 이슈로 전달해야 한다.

Q. DevOps Agent는 뭐야?
A. Docker, CI/CD, Deployment, Runtime Config, Environment Variable, Monitoring, Server Operation을 담당하는 Domain Agent이다.

Q. DevOps Agent가 실제 배포를 실행해도 돼?
A. 사용자 승인과 Tool 권한이 있을 때만 가능하다.

Q. AI Agent는 뭐야?
A. RAG, LLM, Prompt Engineering, Tool Calling, Agent Workflow, Memory, Evaluation을 담당하는 Domain Agent이다.

Q. AI Agent는 언제 필요해?
A. RAG 구조, Agent Workflow, Prompt, Tool Calling, Memory, Evaluation 설계가 필요할 때 필요하다.

Q. Security Agent는 뭐야?
A. Authentication, Authorization, JWT, OAuth2, Password Encoding, Access Control, Security Risk를 담당하는 Domain Agent이다.

Q. Security Agent와 Review Agent는 같아?
A. 아니다. Security Agent는 보안 Domain 분석을 수행하고, Review Agent는 전체 산출물을 기준에 따라 최종 검증한다.

Q. Testing Agent는 뭐야?
A. 테스트 전략, 테스트 케이스, 단위 테스트, 통합 테스트, Mock, Test Data, Pass / Fail Criteria를 담당하는 Domain Agent이다.

Q. Testing Agent와 Review Agent는 같아?
A. 아니다. Testing Agent는 테스트 설계 담당이고, Review Agent는 산출물 품질 검증 담당이다.

Q. Documentation Agent는 뭐야?
A. RAG 문서, API 문서, README, 개발 규칙 문서, 운영 문서, 변경 기록을 담당하는 Domain Agent이다.

Q. Documentation Agent는 RAG 문서를 어떻게 작성해?
A. Header, Code Block, Table, FAQ, Retrieval Queries를 사용해 검색 친화적으로 작성한다.

Q. Domain Agent는 RAG를 어떻게 사용해?
A. 작업 Domain을 식별하고 Domain Rules와 관련 Part 문서를 검색한 뒤, 필요한 Context만 사용한다.

Q. Domain Rules와 일반 RAG 문서 중 무엇을 먼저 봐야 해?
A. Domain Rules를 먼저 보고, 이후 관련 Part 문서를 참조한다.

Q. Domain Agent는 Tool을 언제 사용해?
A. 코드 검색, 문서 검색, 파일 확인, DB 조회, API 호출, 배포처럼 외부 정보나 작업이 필요할 때 사용한다.

Q. Tool 권한은 Agent마다 달라야 해?
A. 그렇다. 각 Agent 역할에 필요한 최소 권한만 부여해야 한다.

Q. Domain Agent Scope Control은 뭐야?
A. Domain Agent가 PM Agent Handoff 범위와 자기 Domain을 벗어나지 않도록 제한하는 규칙이다.

Q. 다른 Domain 문제가 발견되면 어떻게 해?
A. 직접 처리하지 않고 Open Issue, Deferred Task, Handoff Request로 반환한다.

Q. Domain Agent Done Criteria는 뭐야?
A. Domain Agent 작업이 완료되었는지 판단하는 구체적 기준이다.

Q. Done Criteria를 충족하지 못하면?
A. partial, blocked, failed, review_required 중 하나로 표시해야 한다.

Q. Domain Agent의 가장 흔한 실수는?
A. 자기 Domain 밖 작업을 임의로 수행하거나 Handoff 없이 사용자 요청만 보고 작업하는 것이다.

Q. Domain Agent Anti-Pattern을 막으려면?
A. Role, Input, Output, Constraints, Done Criteria, Review Target을 명확히 해야 한다.
