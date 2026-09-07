# Multi-Agent System Part02 - Agent Role Design

---

# 1. Agent Role Design Core

## 1.1 Agent Role Definition

### [개념]

Agent Role은 Multi-Agent System에서 각 Agent가 수행해야 하는 역할 정의이다.

Agent Role은 단순히 Agent 이름을 정하는 것이 아니라, Responsibility, Scope, Input, Output, Tool Permission, RAG Scope, Done Criteria를 명확히 지정하는 작업이다.

좋은 Agent Role은 다음 질문에 답할 수 있어야 한다.

```text
이 Agent는 무엇을 하는가?
이 Agent는 무엇을 하지 않는가?
이 Agent는 어떤 입력을 받는가?
이 Agent는 어떤 출력을 만드는가?
이 Agent는 어떤 Tool을 사용할 수 있는가?
이 Agent는 어떤 RAG 문서를 참조하는가?
이 Agent의 작업 완료 기준은 무엇인가?
```

Agent Role 기본 구조:

```text
Agent Name
→ Role
→ Responsibility
→ Scope
→ Input
→ Output
→ Tool Permission
→ RAG Scope
→ Done Criteria
```

---

### [핵심]

- Agent Role은 Multi-Agent System 품질의 핵심이다.
- Agent 이름만 다르고 책임이 같으면 Multi-Agent가 아니다.
- Responsibility와 Scope를 분리해야 한다.
- Agent가 해야 할 일과 하지 말아야 할 일을 모두 정의해야 한다.
- Input과 Output은 다음 Agent가 사용할 수 있도록 구조화해야 한다.
- Tool Permission은 최소 권한 원칙을 적용해야 한다.
- RAG Scope는 Agent Domain에 맞게 제한해야 한다.
- Done Criteria가 없으면 작업 완료 기준이 흔들린다.

---

### [실무]

2026 실무 기준에서 Agent Role은 Workflow 안정성과 비용 절감을 위해 명확히 설계한다.

나쁜 Agent Role 예시:

```md
## Backend Expert Agent

Spring Boot 전문가로서 백엔드 작업을 잘 수행한다.
```

문제:

- Responsibility 불명확
- Scope 불명확
- Input / Output 없음
- Tool Permission 없음
- RAG Scope 없음
- Done Criteria 없음
- PM Agent와 역할 충돌 가능

좋은 Agent Role 예시:

```md
## Agent Definition

### Name

Backend Agent

### Role

Spring Boot Backend 구현 담당 Agent

### Responsibility

- API 설계
- DTO 설계
- Service Layer 설계
- Controller 설계
- Transaction 기준 반영
- Exception Handling 기준 반영

### Scope

- Backend Application Layer
- Backend Domain Logic
- REST API Contract

### Out of Scope

- Frontend UI 구현
- 배포 실행
- DB 직접 변경
- 운영 서버 수정

### Input

- PM Agent Task
- Requirement
- API Contract
- Domain Rules
- Relevant RAG Context

### Output

- Backend Implementation Plan
- Code Snippets
- API Contract Notes
- Risks
- Assumptions

### Tool Permission

- RAG Search
- File Read
- Code Search

### RAG Scope

- Java
- Spring Boot
- JPA Advanced
- Security Advanced
- API Design

### Done Criteria

- 요구사항 충족
- API Contract 명시
- 예외 처리 기준 포함
- Review 가능한 구조로 출력
```

---

### [FAQ]

Q. Agent Role이 뭐야?
A. Multi-Agent System에서 각 Agent가 어떤 책임을 가지고 어떤 입력을 받아 어떤 출력을 만드는지 정의한 것이다.

Q. Agent 이름만 다르게 만들면 Multi-Agent야?
A. 아니다. 역할, 책임, 입력, 출력, 권한, 완료 기준이 분리되어야 Multi-Agent 구조라고 할 수 있다.

Q. Agent Role에서 가장 중요한 요소는?
A. Responsibility, Scope, Input, Output, Tool Permission, RAG Scope, Done Criteria다.

Q. Agent가 하지 말아야 할 일도 정의해야 해?
A. 해야 한다. Out of Scope를 정의하지 않으면 Agent 간 책임 충돌이 발생하기 쉽다.

---

# 2. Responsibility and Scope

## 2.1 Responsibility

### [개념]

Responsibility는 Agent가 반드시 수행해야 하는 책임이다.

Responsibility는 Agent의 핵심 작업 목록이며, PM Agent가 해당 Agent에게 어떤 작업을 맡길 수 있는지 판단하는 기준이다.

예시:

```text
Backend Agent Responsibility
→ API 설계
→ Service Layer 설계
→ DTO 설계
→ Exception Handling 설계
→ Transaction 기준 반영
```

Responsibility는 구체적인 동사 중심으로 작성해야 한다.

좋은 표현:

- API Contract 작성
- Request DTO 설계
- Service Method 설계
- Validation Rule 검토
- Review Finding 작성

나쁜 표현:

- 백엔드 잘하기
- 전체 개발 담당
- 전문가처럼 판단
- 알아서 처리

---

### [핵심]

- Responsibility는 Agent가 해야 하는 일이다.
- Responsibility는 구체적이어야 한다.
- 추상적인 역할 표현은 피한다.
- 동사 중심으로 작성한다.
- PM Agent가 Routing 기준으로 사용할 수 있어야 한다.
- Review Agent가 책임 수행 여부를 검증할 수 있어야 한다.
- Responsibility가 겹치면 Agent 결과 충돌이 발생할 수 있다.

---

### [실무]

Agent Responsibility 작성 기준:

```text
Domain + Action + Output
```

예시:

| Agent          | Responsibility                                       |
| -------------- | ---------------------------------------------------- |
| PM Agent       | 요구사항 분석, 작업 분해, Agent Routing, 결과 통합   |
| SQL Agent      | Table 설계, Query 설계, Index 후보 제안              |
| Backend Agent  | API 설계, Service 설계, DTO 설계, Exception 설계     |
| Frontend Agent | Component 설계, State 설계, API 연동 설계            |
| DevOps Agent   | Docker 구성, 배포 절차 설계, 운영 위험 검토          |
| AI Agent       | RAG Workflow 설계, Prompt 설계, Tool Calling 설계    |
| Review Agent   | 요구사항 검토, Domain Rules 검토, 일관성 검토        |
| Fix Agent      | Review Finding 반영, 변경 요약, Regression Risk 표시 |

Responsibility 검수 질문:

```text
이 Agent가 실제로 수행할 작업이 명확한가?
PM Agent가 이 책임을 기준으로 Routing할 수 있는가?
Review Agent가 책임 수행 여부를 검토할 수 있는가?
다른 Agent와 책임이 겹치지 않는가?
Output으로 이어질 수 있는 책임인가?
```

---

### [FAQ]

Q. Responsibility가 뭐야?
A. Agent가 반드시 수행해야 하는 구체적인 작업 책임이다.

Q. Responsibility는 어떻게 작성해?
A. Domain + Action + Output 기준으로 구체적인 동사 중심으로 작성한다.

Q. Responsibility가 모호하면 어떻게 돼?
A. Agent 간 역할이 겹치고, 같은 작업을 반복하거나 서로 다른 결과를 만들 수 있다.

Q. PM Agent가 Responsibility를 왜 알아야 해?
A. PM Agent가 요청을 적절한 Specialist Agent에게 Routing하기 위해 필요하다.

---

## 2.2 Scope

### [개념]

Scope는 Agent가 작업할 수 있는 범위이다.

Responsibility가 Agent가 해야 하는 일이라면, Scope는 Agent가 다룰 수 있는 영역과 다루면 안 되는 영역을 구분한다.

Scope 구조:

```text
In Scope
→ Agent가 다룰 수 있는 범위

Out of Scope
→ Agent가 다루면 안 되는 범위
```

예시:

```md
## Backend Agent Scope

### In Scope

- REST API
- Controller
- Service
- DTO
- Transaction
- Exception Handling

### Out of Scope

- React Component 구현
- Docker 배포 실행
- Production DB 변경
- UI 디자인 결정
```

---

### [핵심]

- Scope는 Agent 작업 범위를 제한한다.
- In Scope와 Out of Scope를 모두 정의해야 한다.
- Scope가 없으면 Agent가 다른 Domain까지 침범할 수 있다.
- Scope 제한은 결과 충돌을 줄인다.
- Scope 제한은 Tool Permission 제한과 연결된다.
- Scope 제한은 RAG Scope 제한과 연결된다.
- Scope는 PM Agent Routing 기준으로 사용된다.

---

### [실무]

Scope는 Agent별 책임 충돌을 막기 위해 명확히 작성한다.

예시:

| Agent          | In Scope                   | Out of Scope                 |
| -------------- | -------------------------- | ---------------------------- |
| SQL Agent      | Schema, Query, Index       | Controller 구현, UI 구현     |
| Backend Agent  | API, Service, DTO          | React UI, 배포 실행          |
| Frontend Agent | Component, State, API 호출 | DB Schema 변경, Backend 로직 |
| DevOps Agent   | Docker, Deploy Plan, Infra | Business Logic 구현          |
| Review Agent   | 검토, 위험 식별, 수정 방향 | 직접 대규모 구현             |
| Fix Agent      | Review 범위 수정           | 새 요구사항 생성             |

Scope 검수 질문:

```text
이 Agent가 다룰 수 있는 범위가 명확한가?
이 Agent가 다루면 안 되는 범위가 명확한가?
다른 Agent와 Scope가 겹치지 않는가?
Scope와 Tool Permission이 일치하는가?
Scope와 RAG Scope가 일치하는가?
```

---

### [FAQ]

Q. Scope가 뭐야?
A. Agent가 작업할 수 있는 범위와 작업하면 안 되는 범위를 구분한 것이다.

Q. Scope와 Responsibility는 달라?
A. 다르다. Responsibility는 해야 할 일이고, Scope는 다룰 수 있는 영역이다.

Q. Out of Scope가 필요한 이유는?
A. Agent가 다른 Domain을 침범하거나 위험 작업을 수행하는 것을 막기 위해 필요하다.

Q. Scope는 Tool Permission과 연결돼?
A. 연결된다. Scope 밖 작업에 필요한 Tool은 해당 Agent에게 주지 않는 것이 좋다.

---

# 3. Input and Output Design

## 3.1 Agent Input

### [개념]

Agent Input은 Agent가 작업을 수행하기 위해 받는 정보이다.

Agent Input이 부족하면 Agent는 추측으로 결과를 만들 수 있다.

Agent Input 기본 구성:

```text
Task
→ Requirements
→ Constraints
→ Context
→ RAG Context
→ Tool Result
→ Expected Output
→ Done Criteria
```

Input은 PM Agent Handoff와 Shared State를 통해 전달된다.

---

### [핵심]

- Agent Input은 구조화되어야 한다.
- Task는 명확해야 한다.
- Requirements와 Constraints를 분리해야 한다.
- RAG Context는 관련 문서만 포함해야 한다.
- Tool Result는 출처와 상태를 포함해야 한다.
- Expected Output을 명시해야 한다.
- Done Criteria를 함께 전달해야 한다.
- 불확실한 정보는 Assumption 또는 Open Question으로 표시해야 한다.

---

### [실무]

Agent Input Template:

```json
{
  "task": "Design review API",
  "requirements": [
    "Authenticated user can write review",
    "Rating range is 0 to 5",
    "Review list uses pagination"
  ],
  "constraints": [
    "Spring Boot",
    "JPA",
    "ApiResponse format",
    "Use Slice for list response"
  ],
  "context": ["Festival entity exists", "Users entity exists"],
  "ragScope": ["Spring Boot", "JPA Advanced", "API Design"],
  "expectedOutput": [
    "API Contract",
    "DTO Design",
    "Service Method Plan",
    "Risk"
  ],
  "doneCriteria": [
    "Request/Response defined",
    "Validation included",
    "Exception cases included"
  ],
  "assumptions": [],
  "openQuestions": []
}
```

나쁜 Input 예시:

```text
리뷰 API 만들어줘.
```

문제:

- 인증 여부 불명확
- Entity 관계 불명확
- Response 형식 불명확
- Pagination 기준 불명확
- Validation 기준 불명확
- 완료 기준 없음

---

### [FAQ]

Q. Agent Input이 뭐야?
A. Agent가 작업을 수행하기 위해 받는 Task, Requirement, Constraint, Context, RAG Context, Expected Output 등의 정보다.

Q. Agent Input이 부족하면 어떻게 돼?
A. Agent가 존재하지 않는 구조를 만들거나 요구사항을 잘못 해석할 수 있다.

Q. Agent Input에는 뭐가 들어가야 해?
A. Task, Requirements, Constraints, Context, RAG Scope, Expected Output, Done Criteria, Assumptions, Open Questions가 들어가야 한다.

Q. Input은 누가 만들어?
A. 보통 PM Agent가 Handoff 형태로 생성하고 Shared State를 참조해 보강한다.

---

## 3.2 Agent Output

### [개념]

Agent Output은 Agent가 작업 결과로 반환하는 구조화된 산출물이다.

Agent Output은 사용자가 바로 읽는 최종 답변일 수도 있지만, 대부분 다음 Agent가 사용할 중간 결과이다.

Output은 다음 Agent가 이해하고 검토할 수 있도록 구조화해야 한다.

기본 구조:

```text
Task Summary
→ Result
→ Decision
→ Assumption
→ Risk
→ Open Question
→ Next Step
```

---

### [핵심]

- Agent Output은 구조화되어야 한다.
- 작업 결과와 판단 근거를 분리해야 한다.
- Assumption을 명시해야 한다.
- Risk를 표시해야 한다.
- 다음 Agent가 사용할 수 있어야 한다.
- Review Agent가 검토할 수 있어야 한다.
- 불확실한 결과를 확정처럼 쓰면 안 된다.
- 실패한 작업은 실패 상태로 반환해야 한다.

---

### [실무]

Agent Output Template:

```md
## Agent Output

### Source Agent

Backend Agent

### Task

Review API 설계

### Result

- POST /reviews
- GET /festivals/{festivalId}/reviews
- PATCH /reviews/{reviewId}
- DELETE /reviews/{reviewId}

### Decisions

- 목록 조회는 Slice 사용
- Rating은 0~5 범위 검증
- 작성자 본인만 수정/삭제 가능

### Assumptions

- Users Entity와 Festivals Entity가 존재함
- 인증 정보는 SecurityContext에서 조회함

### Risks

- 중복 리뷰 허용 여부 확인 필요
- 삭제 정책이 Soft Delete인지 Hard Delete인지 확인 필요

### Open Questions

- 한 유저가 같은 축제에 리뷰를 여러 개 작성할 수 있는가?

### Next Step

Review Agent 검토 필요
```

실패 Output 예시:

```md
## Agent Output

### Status

Failed

### Reason

Festival Entity 구조가 제공되지 않아 정확한 연관관계 설계 불가

### Required Context

- Festivals Entity
- Users Entity
- 기존 Review 정책

### Suggested Next Step

PM Agent가 프로젝트 구조를 확인한 뒤 재요청
```

---

### [FAQ]

Q. Agent Output이 뭐야?
A. Agent가 작업 결과로 반환하는 구조화된 산출물이다.

Q. Agent Output은 왜 구조화해야 해?
A. 다음 Agent가 이어서 작업하고 Review Agent가 검토할 수 있어야 하기 때문이다.

Q. Agent Output에 Assumption이 필요한 이유는?
A. 추정한 부분과 확정된 부분을 구분해 오류 전파를 막기 위해서다.

Q. 실패한 작업도 Output으로 남겨야 해?
A. 남겨야 한다. 실패 이유, 필요한 Context, 다음 조치를 기록해야 Workflow가 안정적이다.

---

# 4. Done Criteria

## 4.1 Done Criteria Definition

### [개념]

Done Criteria는 Agent 작업이 완료되었다고 판단하는 기준이다.

Done Criteria가 없으면 Agent가 언제 작업을 끝내야 하는지 불명확해지고, Review Agent도 검토 기준을 잡기 어렵다.

Done Criteria는 Agent별로 다르게 정의한다.

예시:

```text
Backend Agent Done Criteria
→ API Contract 정의
→ DTO 구조 정의
→ Service 책임 정의
→ Exception Case 포함
→ Review 가능한 Output 생성
```

---

### [핵심]

- Done Criteria는 작업 완료 기준이다.
- Agent마다 Done Criteria가 달라야 한다.
- Done Criteria는 Review Criteria와 연결된다.
- Done Criteria가 없으면 결과 품질이 흔들린다.
- Done Criteria는 구체적이고 검증 가능해야 한다.
- “충분히 잘 작성” 같은 표현은 피한다.
- Pass / Fail 판단이 가능해야 한다.

---

### [실무]

Agent별 Done Criteria 예시:

| Agent          | Done Criteria                                                             |
| -------------- | ------------------------------------------------------------------------- |
| PM Agent       | 요구사항 분석, 작업 분해, Agent 선택, Handoff 작성 완료                   |
| SQL Agent      | Table, PK/FK, Index 후보, Query Risk 제시 완료                            |
| Backend Agent  | API Contract, DTO, Service, Exception, Transaction 기준 제시 완료         |
| Frontend Agent | Component, State, API Call, Loading/Error UX 기준 제시 완료               |
| DevOps Agent   | 실행 절차, 설정, 위험 요소, Rollback 기준 제시 완료                       |
| Review Agent   | Findings, Severity, Fix Direction, Pass/Fail 제시 완료                    |
| Fix Agent      | Applied Fix, Change Summary, Regression Risk, Re-review Request 제시 완료 |

검증 가능한 Done Criteria 예시:

```md
## Done Criteria

- [ ] Requirement가 Output에 반영됨
- [ ] Constraint 위반이 없음
- [ ] Assumption이 표시됨
- [ ] Risk가 표시됨
- [ ] 다음 Agent가 사용할 수 있는 구조임
- [ ] Review 가능한 형태임
```

---

### [FAQ]

Q. Done Criteria가 뭐야?
A. Agent 작업이 완료되었다고 판단하는 기준이다.

Q. Done Criteria가 왜 필요해?
A. Agent의 완료 기준과 Review Agent의 검토 기준을 명확히 하기 위해 필요하다.

Q. Done Criteria는 모든 Agent가 같아도 돼?
A. 아니다. Agent 역할과 Output에 따라 다르게 정의해야 한다.

Q. 좋은 Done Criteria 조건은?
A. 구체적이고 검증 가능하며 Pass / Fail 판단이 가능해야 한다.

---

# 5. Agent Definition Template

## 5.1 Standard Agent Definition Template

### [개념]

Agent Definition Template은 Agent Role을 일관되게 정의하기 위한 표준 형식이다.

Template을 사용하면 Agent별 책임, 범위, 입력, 출력, 권한, 완료 기준을 빠짐없이 관리할 수 있다.

표준 Template:

```md
## Agent Definition

### Name

### Role

### Responsibility

### Scope

### Out of Scope

### Input

### Output

### Tool Permission

### RAG Scope

### Done Criteria

### Failure Handling
```

---

### [핵심]

- Template은 Agent Role 누락을 줄인다.
- 모든 Agent에 동일한 정의 형식을 적용한다.
- PM Agent Routing 기준으로 사용할 수 있다.
- Review Agent 검토 기준으로 사용할 수 있다.
- Tool Permission과 RAG Scope를 명시한다.
- Failure Handling을 포함해야 한다.
- Template은 Agent 추가 시 반복 사용한다.

---

### [실무]

권장 Agent Definition Template:

```md
## Agent Definition

### Name

<Agent Name>

### Role

<Agent의 핵심 역할>

### Responsibility

- <수행 책임 1>
- <수행 책임 2>
- <수행 책임 3>

### Scope

- <작업 가능 범위 1>
- <작업 가능 범위 2>

### Out of Scope

- <작업 금지 범위 1>
- <작업 금지 범위 2>

### Input

- PM Agent Task
- Requirements
- Constraints
- Relevant RAG Context
- Shared State

### Output

- Structured Result
- Decisions
- Assumptions
- Risks
- Open Questions

### Tool Permission

- RAG Search
- File Read

### RAG Scope

- <Domain RAG 1>
- <Domain RAG 2>

### Done Criteria

- <완료 기준 1>
- <완료 기준 2>

### Failure Handling

- Missing Context 발생 시 Assumption 또는 Open Question 표시
- Tool Failure 발생 시 실패 상태 반환
- Scope 밖 요청은 PM Agent에게 반환
```

---

### [FAQ]

Q. Agent Definition Template이 뭐야?
A. Agent의 역할, 책임, 범위, 입력, 출력, 권한, 완료 기준을 일관되게 정의하는 표준 형식이다.

Q. Agent Definition Template이 필요한 이유는?
A. Agent별 역할 누락과 책임 충돌을 줄이기 위해 필요하다.

Q. 모든 Agent에 같은 Template을 써도 돼?
A. 기본 Template은 같게 쓰고, 내용은 Agent 역할에 맞게 다르게 작성한다.

Q. Failure Handling도 Agent Definition에 넣어야 해?
A. 넣는 것이 좋다. 실패 시 재시도, 중단, PM 반환 기준을 명확히 할 수 있다.

---

## 5.2 Backend Agent Definition Example

### [개념]

Backend Agent는 Spring Boot 기반 Backend 작업을 담당하는 Specialist Agent이다.

Backend Agent는 API, Service, DTO, Transaction, Exception Handling을 중심으로 작업한다.

Backend Agent는 Frontend UI 구현, DB 직접 변경, 배포 실행을 담당하지 않는다.

---

### [핵심]

- Backend Agent는 Backend Application Layer를 담당한다.
- Spring Boot, JPA, Security, API Design RAG를 주로 참조한다.
- API Contract와 Service 책임을 명확히 출력해야 한다.
- DTO와 Validation 기준을 포함해야 한다.
- Exception Handling 기준을 포함해야 한다.
- Transaction 기준을 표시해야 한다.
- Frontend 구현과 DevOps 실행은 Scope 밖이다.

---

### [실무]

Backend Agent Definition:

```md
## Agent Definition

### Name

Backend Agent

### Role

Spring Boot Backend 구현 및 설계 담당 Specialist Agent

### Responsibility

- REST API 설계
- Controller 구조 설계
- Service Layer 책임 설계
- DTO 설계
- Validation 기준 설계
- Transaction 기준 검토
- Exception Handling 기준 설계
- Security 적용 지점 검토

### Scope

- Backend API
- Application Service
- DTO
- JPA 연동 기준
- Security 적용 기준
- Error Response

### Out of Scope

- React Component 구현
- DB 직접 변경
- 운영 서버 배포
- UI 디자인 결정
- 모델 Fine-Tuning

### Input

- PM Agent Task
- Requirements
- API Contract
- Entity Context
- Domain Rules
- Relevant RAG Context

### Output

- API Contract
- Backend Implementation Plan
- DTO Design
- Service Method Design
- Exception Cases
- Assumptions
- Risks

### Tool Permission

- RAG Search
- File Read
- Code Search

### RAG Scope

- Java
- Spring Boot
- JPA Advanced
- Security Advanced
- API Design
- Testing

### Done Criteria

- 요구사항이 API 설계에 반영됨
- Request / Response 구조가 명확함
- Service 책임이 분리됨
- Validation 기준이 포함됨
- Exception Case가 포함됨
- Review Agent가 검토 가능한 Output 생성

### Failure Handling

- Entity 구조가 없으면 Assumption 표시
- API Contract가 불명확하면 Open Question 표시
- Scope 밖 요청은 PM Agent에게 반환
```

---

### [FAQ]

Q. Backend Agent는 뭐 하는 Agent야?
A. Spring Boot 기반 API, Service, DTO, Exception, Transaction 기준을 설계하고 구현 방향을 제시하는 Agent다.

Q. Backend Agent가 Frontend 코드도 작성해?
A. 원칙적으로 작성하지 않는다. Frontend 작업은 Frontend Agent가 담당한다.

Q. Backend Agent의 주요 RAG Scope는?
A. Java, Spring Boot, JPA Advanced, Security Advanced, API Design, Testing이다.

Q. Backend Agent Output에는 뭐가 있어야 해?
A. API Contract, DTO Design, Service Method Design, Exception Cases, Assumptions, Risks가 있어야 한다.

---

## 5.3 Review Agent Definition Example

### [개념]

Review Agent는 Agent 산출물을 독립적으로 검증하는 Specialist Agent이다.

Review Agent는 요구사항, Domain Rules, 일관성, 위험 요소, 완료 기준을 검토한다.

Review Agent는 단순 취향이 아니라 명확한 기준으로 Findings를 작성해야 한다.

---

### [핵심]

- Review Agent는 독립 검증 담당이다.
- 요구사항 충족 여부를 확인한다.
- Domain Rules 위반 여부를 확인한다.
- Agent 결과 간 일관성을 확인한다.
- Risk와 Missing Context를 확인한다.
- Severity 기준을 적용한다.
- Fix Direction을 제공한다.
- Pass / Fail을 명확히 표시한다.

---

### [실무]

Review Agent Definition:

```md
## Agent Definition

### Name

Review Agent

### Role

Multi-Agent 산출물 품질 검증 담당 Agent

### Responsibility

- Requirement Match 검토
- Domain Rules Compliance 검토
- Cross-domain Consistency 검토
- API Contract Consistency 검토
- Security Risk 검토
- Missing Context 검토
- Severity 분류
- Fix Direction 작성
- Pass / Fail 판단

### Scope

- Agent Output Review
- Requirement Review
- Domain Rules Review
- Consistency Review
- Risk Review

### Out of Scope

- 대규모 구현 직접 수행
- 새로운 요구사항 생성
- 근거 없는 취향성 지적
- 사용자 승인 없는 위험 작업 실행

### Input

- Original User Request
- PM Agent Plan
- Specialist Agent Output
- Shared State
- Domain Rules
- Done Criteria

### Output

- Review Findings
- Severity
- Root Cause
- Impact
- Fix Direction
- Pass / Fail
- Re-review Need

### Tool Permission

- RAG Search
- File Read
- Test Result Read

### RAG Scope

- Master Rules
- Domain Rules
- Project Rules
- Related Domain RAG

### Done Criteria

- Critical Issue 식별 완료
- Major Issue 식별 완료
- Minor Issue 구분 완료
- Fix Direction 포함
- Pass / Fail 명시
- 근거 없는 지적 없음

### Failure Handling

- Context 부족 시 단정하지 않고 Missing Context로 표시
- Review 기준 불명확 시 PM Agent에게 기준 요청
- Scope 밖 구현 요청은 Fix Agent 또는 PM Agent에게 반환
```

---

### [FAQ]

Q. Review Agent는 뭐 하는 Agent야?
A. Agent 산출물을 요구사항, Domain Rules, 일관성, 위험 기준으로 검증하는 Agent다.

Q. Review Agent가 직접 수정해도 돼?
A. 원칙적으로 수정은 Fix Agent가 담당한다. Review Agent는 Findings와 Fix Direction을 제공한다.

Q. Review Agent의 Output에는 뭐가 있어야 해?
A. Findings, Severity, Root Cause, Impact, Fix Direction, Pass / Fail이 있어야 한다.

Q. Review Agent가 주의해야 할 점은?
A. 근거 없는 지적, 취향성 비판, 수정 방향 없는 비판을 피해야 한다.

---

# 6. Role Conflict Prevention

## 6.1 Role Overlap Prevention

### [개념]

Role Overlap은 여러 Agent가 같은 책임을 가지고 동일 작업을 반복하거나 서로 다른 결과를 만드는 문제이다.

Role Overlap은 Multi-Agent System에서 가장 흔한 실패 원인 중 하나이다.

예시:

```text
SQL Agent가 Schema를 설계함
Backend Agent가 다른 Entity 관계를 가정함
Frontend Agent가 다른 Response Field를 가정함
→ API Contract 충돌 발생
```

---

### [핵심]

- Role Overlap은 책임 경계 부족 때문에 발생한다.
- Agent Definition을 먼저 작성해야 한다.
- Responsibility와 Scope를 분리해야 한다.
- API Contract와 Schema Decision은 Shared State에 기록해야 한다.
- PM Agent가 결정사항을 통합해야 한다.
- Review Agent가 Cross-domain Consistency를 검토해야 한다.
- 충돌 발생 시 PM Agent가 최종 기준을 확정한다.

---

### [실무]

Role Overlap 방지 절차:

```text
Agent Definition 작성
→ Responsibility 분리
→ Scope / Out of Scope 정의
→ RAG Scope 제한
→ Tool Permission 제한
→ Shared State에 결정사항 기록
→ Review Agent가 충돌 검토
```

작업 소유권 예시:

| 작업              | Primary Agent  | Support Agent             |
| ----------------- | -------------- | ------------------------- |
| 요구사항 분석     | PM Agent       | Review Agent              |
| DB Schema 설계    | SQL Agent      | Backend Agent             |
| API Contract 설계 | Backend Agent  | PM Agent                  |
| UI 연동 설계      | Frontend Agent | Backend Agent             |
| 배포 계획         | DevOps Agent   | PM Agent                  |
| 품질 검토         | Review Agent   | Domain Agent              |
| 수정 반영         | Fix Agent      | Original Specialist Agent |

---

### [FAQ]

Q. Role Overlap이 뭐야?
A. 여러 Agent의 책임이 겹쳐 같은 작업을 반복하거나 서로 다른 결과를 만드는 문제다.

Q. Role Overlap은 왜 위험해?
A. API Contract, Schema, 구현 방향이 충돌해 최종 결과 품질이 떨어지기 때문이다.

Q. Role Overlap은 어떻게 막아?
A. Agent Definition, Responsibility 분리, Scope 제한, Shared State 기록, Review 검토로 막는다.

Q. 충돌이 발생하면 누가 최종 결정해?
A. PM Agent가 Shared State와 요구사항을 기준으로 최종 결정을 정리해야 한다.

---

## 6.2 Role Boundary Checklist

### [개념]

Role Boundary Checklist는 Agent 역할 경계가 명확한지 검수하는 체크리스트이다.

Agent를 추가하기 전, 기존 Agent와 책임이 겹치지 않는지 확인해야 한다.

Role Boundary가 명확하지 않으면 Multi-Agent System은 복잡한 Single Agent 묶음처럼 동작한다.

---

### [핵심]

- Agent 추가 전 Role Boundary를 검토한다.
- 기존 Agent와 Responsibility가 겹치는지 확인한다.
- Scope와 Out of Scope가 명확한지 확인한다.
- Input과 Output이 다음 단계와 연결되는지 확인한다.
- Tool Permission이 과도하지 않은지 확인한다.
- RAG Scope가 너무 넓거나 좁지 않은지 확인한다.
- Done Criteria가 검증 가능한지 확인한다.

---

### [실무]

Role Boundary Checklist:

```md
## Role Boundary Checklist

- [ ] Agent Name이 명확한가?
- [ ] Role이 구체적인가?
- [ ] Responsibility가 동사 중심으로 작성되었는가?
- [ ] Scope가 명확한가?
- [ ] Out of Scope가 정의되었는가?
- [ ] Input이 구조화되어 있는가?
- [ ] Output이 다음 Agent가 사용할 수 있는 형태인가?
- [ ] Tool Permission이 최소 권한인가?
- [ ] RAG Scope가 Domain에 맞게 제한되었는가?
- [ ] Done Criteria가 검증 가능한가?
- [ ] 기존 Agent와 책임이 겹치지 않는가?
- [ ] 충돌 발생 시 PM Agent가 결정할 수 있는가?
```

Agent 추가 판단 기준:

```text
새 Agent가 기존 Agent와 다른 책임을 가지는가?
새 Agent가 독립적인 Output을 만드는가?
새 Agent가 별도 RAG Scope를 필요로 하는가?
새 Agent가 별도 Tool Permission을 필요로 하는가?
새 Agent를 추가하면 품질이 실제로 좋아지는가?
```

---

### [FAQ]

Q. Role Boundary Checklist가 뭐야?
A. Agent 역할 경계가 명확한지 검수하는 체크리스트다.

Q. Agent를 추가하기 전에 뭘 확인해야 해?
A. 기존 Agent와 책임이 겹치지 않는지, Output이 독립적인지, 별도 RAG Scope와 Tool Permission이 필요한지 확인해야 한다.

Q. Agent를 많이 만들면 더 좋아?
A. 아니다. 책임이 명확하지 않은 Agent는 복잡도와 Latency만 증가시킬 수 있다.

Q. Role Boundary가 불명확하면 어떻게 돼?
A. Agent 결과 충돌, 작업 반복, Handoff 실패, Review-Fix 반복이 발생할 수 있다.

---

# 7. Personal AI Development Team Role Set

## 7.1 Minimal Role Set

### [개념]

Minimal Role Set은 개인 AI 개발팀을 시작하기 위한 최소 Agent 구성이다.

처음부터 모든 Agent를 만들지 않고, PM Agent, Specialist Agent, Review Agent 중심으로 시작한다.

권장 최소 구조:

```text
User
→ PM Agent
→ Backend Agent
→ Review Agent
→ Final Output
```

또는 RAG 문서 제작 기준:

```text
User
→ PM Agent
→ Documentation Agent
→ Review Agent
→ Final Output
```

---

### [핵심]

- 초기에는 Agent 수를 최소화한다.
- PM Agent는 요구사항 분석과 작업 분해를 담당한다.
- 하나의 Specialist Agent로 실제 작업을 수행한다.
- Review Agent로 품질을 검증한다.
- Fix Agent는 Review-Fix Loop가 필요해질 때 추가한다.
- Tool Permission은 읽기 중심으로 시작한다.
- RAG Scope는 좁게 시작하고 필요 시 확장한다.

---

### [실무]

개인 AI 개발팀 초기 구성:

| Agent               | Role                            | 필요도                |
| ------------------- | ------------------------------- | --------------------- |
| PM Agent            | 요청 분석, 작업 분해, 결과 통합 | 필수                  |
| Backend Agent       | Backend 작업 수행               | Backend 개발 시 필수  |
| Documentation Agent | RAG 문서 작성                   | RAG 문서 제작 시 필수 |
| Review Agent        | 산출물 검토                     | 권장                  |
| Fix Agent           | Review 결과 수정                | 선택                  |

초기에는 아래 기준을 만족하면 충분하다.

```text
PM Agent가 요청을 분해한다.
Specialist Agent가 Domain Rules를 참조한다.
Review Agent가 산출물을 검토한다.
최종 결과가 사용자에게 정리되어 전달된다.
```

---

### [FAQ]

Q. 개인 AI 개발팀은 처음에 몇 개 Agent로 시작해?
A. PM Agent, Specialist Agent, Review Agent 중심의 최소 구조로 시작하는 것이 좋다.

Q. Fix Agent는 처음부터 필요해?
A. 필수는 아니다. Review-Fix Loop가 필요해지면 추가해도 된다.

Q. RAG 문서 제작용 최소 Agent는?
A. PM Agent, Documentation Agent, Review Agent 구조가 적합하다.

Q. 초기 Agent 수를 줄이는 이유는?
A. 역할 충돌, Latency 증가, Handoff 복잡도 증가를 줄이기 위해서다.

---

## 7.2 Expanded Role Set

### [개념]

Expanded Role Set은 개인 AI 개발팀을 확장할 때 사용하는 Agent 구성이다.

Backend, Frontend, DevOps, AI 작업이 늘어나면 Domain별 Specialist Agent를 추가한다.

확장 구조:

```text
User
→ PM Agent
→ SQL Agent
→ Backend Agent
→ Frontend Agent
→ DevOps Agent
→ AI Agent
→ Review Agent
→ Fix Agent
→ Final Output
```

---

### [핵심]

- 확장 Agent는 필요할 때만 추가한다.
- SQL Agent는 Schema와 Query 중심이다.
- Backend Agent는 API와 Service 중심이다.
- Frontend Agent는 UI와 API 연동 중심이다.
- DevOps Agent는 실행 환경과 배포 중심이다.
- AI Agent는 RAG, Prompt, Tool Calling, Agent Workflow 중심이다.
- Review Agent는 전체 산출물을 독립 검증한다.
- Fix Agent는 Review 결과를 반영한다.

---

### [실무]

확장 Role Set 예시:

| Agent          | Responsibility                                     | RAG Scope                                        |
| -------------- | -------------------------------------------------- | ------------------------------------------------ |
| PM Agent       | 요구사항 분석, 작업 분해, Agent Routing, 결과 통합 | Master Rules, Project Progress, Agent Rules      |
| SQL Agent      | Schema, Query, Index, Data Consistency             | SQL, JPA, QueryDSL                               |
| Backend Agent  | API, Service, DTO, Security, Exception             | Java, Spring Boot, JPA, Security, API Design     |
| Frontend Agent | Component, State, API 연동, UX 상태 처리           | HTML, CSS, JavaScript, TypeScript, React         |
| DevOps Agent   | Docker, Linux, CI/CD, Deploy Plan                  | Git, Docker, Linux, CI/CD                        |
| AI Agent       | RAG, Prompt, Agent Workflow, Tool Calling          | Prompt Engineering, RAG, LangGraph, Tool Calling |
| Review Agent   | Requirement, Domain Rules, Consistency, Risk 검토  | Master Rules, Domain Rules, Project Rules        |
| Fix Agent      | Review Findings 반영, Change Summary 작성          | 관련 Domain RAG                                  |

확장 판단 기준:

```text
현재 Agent가 책임 과부하 상태인가?
새 Domain 지식이 필요한가?
별도 RAG Scope가 필요한가?
별도 Tool Permission이 필요한가?
Review에서 반복적으로 같은 Domain 문제가 발생하는가?
```

---

### [FAQ]

Q. Expanded Role Set은 언제 필요해?
A. Backend, Frontend, DevOps, AI처럼 Domain 작업이 분리될 만큼 복잡해졌을 때 필요하다.

Q. SQL Agent와 Backend Agent를 분리하는 이유는?
A. Schema, Query, Index 설계와 API, Service 설계의 책임이 다르기 때문이다.

Q. DevOps Agent는 언제 추가해?
A. Docker, Linux, CI/CD, 배포, 운영 환경 작업이 필요할 때 추가한다.

Q. AI Agent는 어떤 작업을 담당해?
A. RAG, Prompt Engineering, Tool Calling, Agent Workflow, Agent 시스템 고도화 작업을 담당한다.

---

# Retrieval Queries

### [FAQ]

Q. Agent Role이 뭐야?
A. Multi-Agent System에서 각 Agent가 어떤 책임을 가지고 어떤 입력을 받아 어떤 출력을 만드는지 정의한 것이다.

Q. Agent Role 설계에 필요한 요소는?
A. Name, Role, Responsibility, Scope, Out of Scope, Input, Output, Tool Permission, RAG Scope, Done Criteria가 필요하다.

Q. Agent 이름만 다르면 Multi-Agent야?
A. 아니다. 역할, 책임, 입력, 출력, 권한, 완료 기준이 분리되어야 한다.

Q. Responsibility가 뭐야?
A. Agent가 반드시 수행해야 하는 구체적인 작업 책임이다.

Q. Responsibility는 어떻게 작성해?
A. Domain + Action + Output 기준으로 구체적인 동사 중심으로 작성한다.

Q. Scope가 뭐야?
A. Agent가 작업할 수 있는 범위와 작업하면 안 되는 범위를 구분한 것이다.

Q. Responsibility와 Scope 차이는?
A. Responsibility는 해야 할 일이고, Scope는 다룰 수 있는 영역이다.

Q. Out of Scope가 왜 필요해?
A. Agent가 다른 Domain을 침범하거나 위험 작업을 수행하는 것을 막기 위해 필요하다.

Q. Agent Input이 뭐야?
A. Agent가 작업을 수행하기 위해 받는 Task, Requirements, Constraints, Context, RAG Context, Expected Output 등의 정보다.

Q. Agent Input에는 뭐가 들어가야 해?
A. Task, Requirements, Constraints, Context, RAG Scope, Expected Output, Done Criteria, Assumptions, Open Questions가 들어가야 한다.

Q. Agent Output이 뭐야?
A. Agent가 작업 결과로 반환하는 구조화된 산출물이다.

Q. Agent Output에는 뭐가 있어야 해?
A. Task Summary, Result, Decisions, Assumptions, Risks, Open Questions, Next Step이 있어야 한다.

Q. Agent Output에 Assumption이 필요한 이유는?
A. 추정한 부분과 확정된 부분을 구분해 오류 전파를 막기 위해서다.

Q. 실패한 작업도 Output으로 남겨야 해?
A. 남겨야 한다. 실패 이유, 필요한 Context, 다음 조치를 기록해야 Workflow가 안정적이다.

Q. Done Criteria가 뭐야?
A. Agent 작업이 완료되었다고 판단하는 기준이다.

Q. Done Criteria가 왜 필요해?
A. Agent의 완료 기준과 Review Agent의 검토 기준을 명확히 하기 위해 필요하다.

Q. 좋은 Done Criteria 조건은?
A. 구체적이고 검증 가능하며 Pass / Fail 판단이 가능해야 한다.

Q. Agent Definition Template이 뭐야?
A. Agent의 역할, 책임, 범위, 입력, 출력, 권한, 완료 기준을 일관되게 정의하는 표준 형식이다.

Q. Agent Definition Template 항목은?
A. Name, Role, Responsibility, Scope, Out of Scope, Input, Output, Tool Permission, RAG Scope, Done Criteria, Failure Handling이다.

Q. Backend Agent는 뭐 하는 Agent야?
A. Spring Boot 기반 API, Service, DTO, Exception, Transaction 기준을 설계하고 구현 방향을 제시하는 Agent다.

Q. Backend Agent의 RAG Scope는?
A. Java, Spring Boot, JPA Advanced, Security Advanced, API Design, Testing이다.

Q. Review Agent는 뭐 하는 Agent야?
A. Agent 산출물을 요구사항, Domain Rules, 일관성, 위험 기준으로 검증하는 Agent다.

Q. Review Agent Output에는 뭐가 있어야 해?
A. Findings, Severity, Root Cause, Impact, Fix Direction, Pass / Fail이 있어야 한다.

Q. Role Overlap이 뭐야?
A. 여러 Agent의 책임이 겹쳐 같은 작업을 반복하거나 서로 다른 결과를 만드는 문제다.

Q. Role Overlap은 왜 위험해?
A. API Contract, Schema, 구현 방향이 충돌해 최종 결과 품질이 떨어지기 때문이다.

Q. Role Overlap은 어떻게 막아?
A. Agent Definition, Responsibility 분리, Scope 제한, Shared State 기록, Review 검토로 막는다.

Q. Role Boundary Checklist가 뭐야?
A. Agent 역할 경계가 명확한지 검수하는 체크리스트다.

Q. Agent를 추가하기 전에 뭘 확인해야 해?
A. 기존 Agent와 책임이 겹치지 않는지, 독립 Output이 있는지, 별도 RAG Scope와 Tool Permission이 필요한지 확인해야 한다.

Q. 개인 AI 개발팀은 처음에 몇 개 Agent로 시작해?
A. PM Agent, Specialist Agent, Review Agent 중심의 최소 구조로 시작하는 것이 좋다.

Q. RAG 문서 제작용 최소 Agent는?
A. PM Agent, Documentation Agent, Review Agent 구조가 적합하다.

Q. Expanded Role Set은 언제 필요해?
A. Backend, Frontend, DevOps, AI처럼 Domain 작업이 분리될 만큼 복잡해졌을 때 필요하다.

Q. 개인 AI 개발팀 확장 Agent 구성은?
A. PM Agent, SQL Agent, Backend Agent, Frontend Agent, DevOps Agent, AI Agent, Review Agent, Fix Agent 구조다.

Q. SQL Agent와 Backend Agent를 분리하는 이유는?
A. Schema, Query, Index 설계와 API, Service 설계의 책임이 다르기 때문이다.

Q. AI Agent는 어떤 작업을 담당해?
A. RAG, Prompt Engineering, Tool Calling, Agent Workflow, Agent 시스템 고도화 작업을 담당한다.
