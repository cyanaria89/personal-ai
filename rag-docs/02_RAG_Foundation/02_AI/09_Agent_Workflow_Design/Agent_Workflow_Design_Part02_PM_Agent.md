# Agent Workflow Design Part02 PM Agent

---

# 1. PM Agent Core

## 1.1 PM Agent Definition

### [개념]

PM Agent는 Agent Workflow의 시작점이자 전체 조율자이다.

PM Agent는 사용자 요청을 직접 전부 구현하는 Agent가 아니다.
PM Agent는 사용자 요청을 분석하고, 작업을 실행 가능한 단위로 분해하며, 적절한 Domain Agent에게 라우팅하고, 결과를 통합하는 역할을 담당한다.

PM Agent 핵심 역할:

- User Request Analysis
- Requirement Clarification
- Task Decomposition
- Agent Routing
- Priority Decision
- Scope Control
- Handoff Generation
- Shared State Update
- Review Request
- Final Integration

---

### [핵심]

- PM Agent는 Workflow의 Entry Point이다.
- PM Agent는 요청 분석과 작업 분해를 담당한다.
- PM Agent는 직접 구현보다 조율이 핵심이다.
- PM Agent는 Domain Agent에게 명확한 Handoff를 전달한다.
- PM Agent는 작업 범위와 우선순위를 통제한다.
- PM Agent는 Review Agent에게 검증 요청을 보낸다.
- PM Agent는 최종 결과를 사용자 목적에 맞게 통합한다.
- PM Agent가 모든 구현을 직접 처리하면 Multi-Agent 구조가 무너진다.

---

### [실무]

2026 실무 기준 PM Agent는 개인 AI 개발팀의 프로젝트 매니저 역할을 수행한다.

기본 Flow:

```text
User Request
→ Understand Goal
→ Identify Domain
→ Split Tasks
→ Assign Agents
→ Collect Results
→ Request Review
→ Integrate Final Output
```

PM Agent가 반드시 수행할 판단:

| 판단 항목        | 설명                                          |
| ---------------- | --------------------------------------------- |
| Goal             | 사용자가 최종적으로 원하는 결과               |
| Domain           | SQL, Backend, Frontend, DevOps, AI, Review 등 |
| Scope            | 이번 작업에 포함할 범위                       |
| Priority         | 먼저 처리해야 할 작업                         |
| Dependency       | 선행 작업과 후행 작업 관계                    |
| Required Agent   | 필요한 담당 Agent                             |
| Required Context | Agent에게 전달할 Context                      |
| Risk             | 사용자 확인 또는 Review가 필요한 위험         |
| Stop Condition   | 완료, 보류, 실패 기준                         |

PM Agent가 피해야 할 행동:

- 직접 모든 코드를 구현
- Domain Agent 없이 단일 응답으로 처리
- 모호한 요구사항을 사실처럼 확정
- Handoff 없이 Agent 실행
- Review 없이 최종 완료 처리
- Scope를 임의로 확장
- 사용자 승인 없이 위험 작업 진행

---

### [FAQ]

Q. PM Agent는 뭐야?
A. 사용자 요청을 분석하고 작업을 분해하며, 적절한 Agent에게 라우팅하고 최종 결과를 통합하는 조율 Agent이다.

Q. PM Agent가 직접 구현해도 돼?
A. 원칙적으로 직접 구현보다 분석, 분해, 라우팅, 통합에 집중해야 한다.

Q. PM Agent가 중요한 이유는?
A. PM Agent가 작업 범위와 흐름을 정하기 때문에 전체 Agent Workflow 품질이 결정된다.

Q. PM Agent는 언제 사용자에게 질문해야 해?
A. 요구사항이 불명확하거나 위험 작업, 비용 발생, 외부 변경이 포함될 때 질문해야 한다.

---

# 2. User Request Analysis

## 2.1 User Request Analysis Definition

### [개념]

User Request Analysis는 사용자의 자연어 요청을 Agent Workflow에서 실행 가능한 작업 요구사항으로 변환하는 과정이다.

PM Agent는 사용자 요청에서 다음 요소를 추출한다.

- Goal
- Requested Output
- Domain
- Constraints
- Context
- Assumptions
- Missing Information
- Risk
- Required Agent
- Stop Condition

---

### [핵심]

- 사용자 요청의 표면 문장보다 최종 목적을 우선 파악한다.
- 요청된 산출물 형식을 확인한다.
- 작업 Domain을 식별한다.
- 현재 대화의 제약 조건을 반영한다.
- 기존 Project Rules와 충돌하는지 확인한다.
- 불명확한 요구사항은 Assumption 또는 Open Question으로 분리한다.
- 위험 작업은 Human-in-the-loop 대상으로 분류한다.

---

### [실무]

User Request Analysis Template:

```md
## User Request Analysis

### Original Request

### Goal

### Requested Output

### Domain

### Constraints

### Relevant Context

### Assumptions

### Missing Information

### Risk

### Required Agents

### Stop Condition
```

예시:

```md
## User Request Analysis

### Original Request

회원가입 기능 만들어줘

### Goal

회원가입 API와 관련 Backend 흐름 설계

### Requested Output

DTO, Service Flow, Controller Endpoint, Exception Cases

### Domain

Backend, Security, SQL

### Constraints

- Spring Boot 3.x
- Java 21
- ApiResponse<T> 직접 반환
- GlobalExceptionHandler 사용

### Assumptions

- 이메일은 unique 값으로 사용
- Password는 BCrypt Encoding 사용

### Missing Information

- 이메일 인증 필수 여부 미확정

### Required Agents

PM Agent, SQL Agent, Backend Agent, Security Agent, Review Agent

### Stop Condition

Review Passed 또는 Blocking Issue 없음
```

주의:

- 사용자 요청을 그대로 Agent에게 넘기지 않는다.
- 요구사항과 가정을 구분한다.
- Project Progress와 Domain Rules를 우선 반영한다.
- 모호한 부분을 숨기지 않는다.
- 질문이 필요한 부분과 가정으로 진행 가능한 부분을 구분한다.

---

### [FAQ]

Q. User Request Analysis는 뭐야?
A. 사용자의 요청을 Agent Workflow에서 실행 가능한 요구사항과 작업 단위로 변환하는 과정이다.

Q. PM Agent는 사용자 요청에서 무엇을 뽑아야 해?
A. Goal, Domain, Constraints, Required Output, Missing Information, Required Agent, Stop Condition을 뽑아야 한다.

Q. 사용자 요청이 모호하면 어떻게 해?
A. Assumption으로 표시하거나 Open Question으로 분리하고, 필요한 경우 사용자 확인을 요청한다.

Q. 사용자 요청을 그대로 Agent에게 전달하면 안 돼?
A. 그대로 전달하면 Domain, 제약, 산출물 형식이 불명확해져 Agent 품질이 떨어질 수 있다.

---

# 3. Requirement Clarification

## 3.1 Requirement Clarification Definition

### [개념]

Requirement Clarification은 사용자 요청에서 불명확한 요구사항을 명확히 하거나, 작업 가능한 가정으로 정리하는 과정이다.

PM Agent는 모든 상황에서 질문을 남발하지 않는다.
작업 진행에 치명적인 정보만 질문하고, 작은 불확실성은 Assumption으로 표시한 뒤 진행할 수 있다.

---

### [핵심]

- 불명확한 요구사항을 식별한다.
- 치명적 정보 부족과 경미한 정보 부족을 구분한다.
- 작업 가능한 경우 Assumption으로 진행한다.
- 위험 작업은 사용자 승인 후 진행한다.
- 질문은 구체적이고 선택 가능해야 한다.
- 현재 사용자 요청이 기존 규칙보다 우선한다.
- 확인 요청은 Workflow를 중단해야 할 때만 사용한다.

---

### [실무]

Clarification Decision Rule:

| 상황                                 | 처리                                |
| ------------------------------------ | ----------------------------------- |
| 산출물 형식이 불명확하지만 추정 가능 | Assumption 표시 후 진행             |
| Domain이 불명확함                    | PM Agent가 Task Analysis 후 Routing |
| DB 변경, 파일 삭제, 배포 포함        | 사용자 승인 필요                    |
| 비용 발생 API 대량 호출              | 사용자 승인 필요                    |
| 보안 위험 또는 정책 위험             | 중단 또는 확인                      |
| 필수 입력 누락                       | Open Question 또는 사용자 확인      |
| 기존 Project Rules와 충돌            | 충돌 내용 표시 후 최신 요청 우선    |

Clarification Template:

```md
## Requirement Clarification

### Ambiguous Requirement

### Impact

### Can Proceed With Assumption

Yes / No

### Assumption

### User Confirmation Required

Yes / No

### Question
```

예시:

```md
## Requirement Clarification

### Ambiguous Requirement

이메일 인증을 회원가입 필수 조건으로 둘지 미확정

### Impact

Service Flow와 Exception Case가 달라짐

### Can Proceed With Assumption

Yes

### Assumption

이메일 인증은 선택 기능으로 분리하고 기본 회원가입 Flow는 먼저 설계

### User Confirmation Required

No
```

금지:

- 모든 불확실성마다 질문
- 질문 없이 위험 작업 실행
- 불확실한 내용을 확정 사실처럼 전달
- 기존 결정과 충돌하는 요구사항을 무시

---

### [FAQ]

Q. Requirement Clarification은 뭐야?
A. 불명확한 요구사항을 확인하거나 작업 가능한 가정으로 정리하는 과정이다.

Q. 언제 사용자에게 질문해야 해?
A. 작업 진행에 필수 정보가 없거나 위험 작업, 비용 발생, 외부 변경이 포함될 때 질문해야 한다.

Q. 항상 질문하고 진행해야 해?
A. 아니다. 경미한 불확실성은 Assumption으로 표시하고 진행할 수 있다.

Q. Assumption은 왜 필요해?
A. 불확실한 내용을 숨기지 않고, Agent와 Review가 같은 기준으로 작업하게 하기 위해 필요하다.

---

# 4. Task Decomposition

## 4.1 Task Decomposition Definition

### [개념]

Task Decomposition은 큰 사용자 요청을 실행 가능한 작은 작업 단위로 나누는 과정이다.

PM Agent는 각 작업에 담당 Agent, 입력 Context, 기대 산출물, 완료 기준을 지정해야 한다.

Task Decomposition 필수 요소:

- Goal
- Subtask
- Dependency
- Priority
- Owner Agent
- Required Context
- Expected Output
- Done Criteria

---

### [핵심]

- 큰 요청은 실행 가능한 단위로 나눈다.
- 각 Subtask는 담당 Agent가 명확해야 한다.
- 각 Subtask는 산출물과 완료 기준이 있어야 한다.
- 선행 작업과 후행 작업의 의존성을 고려한다.
- 병렬 가능 작업과 순차 작업을 구분한다.
- 너무 작게 쪼개면 오버헤드가 증가한다.
- 너무 크게 유지하면 Agent가 놓치는 부분이 증가한다.

---

### [실무]

Task Decomposition Template:

```md
## Task Decomposition

### Goal

### Subtasks

| No  | Subtask | Owner Agent | Dependency | Expected Output | Done Criteria |
| --- | ------- | ----------- | ---------- | --------------- | ------------- |

### Execution Order

### Review Target

### Stop Condition
```

예시:

```md
## Task Decomposition

### Goal

회원가입 기능 설계

### Subtasks

| No  | Subtask                   | Owner Agent    | Dependency | Expected Output      | Done Criteria         |
| --- | ------------------------- | -------------- | ---------- | -------------------- | --------------------- |
| 1   | users table 요구사항 검토 | SQL Agent      | None       | Schema Check         | 필수 컬럼/제약 확인   |
| 2   | DTO 설계                  | Backend Agent  | 1          | Request/Response DTO | Validation 포함       |
| 3   | Service Flow 설계         | Backend Agent  | 1,2        | Register Flow        | 예외 흐름 포함        |
| 4   | Security 검토             | Security Agent | 2,3        | Password/Auth Review | BCrypt 적용 확인      |
| 5   | 테스트 케이스 작성        | Testing Agent  | 2,3,4      | Test Cases           | 성공/실패 케이스 포함 |
| 6   | 전체 검증                 | Review Agent   | 1~5        | Review Finding       | Blocking Issue 없음   |

### Execution Order

SQL → Backend → Security → Testing → Review

### Stop Condition

Review Passed
```

주의:

- Task를 Agent 관점이 아니라 산출물 기준으로 나눈다.
- Domain이 겹치면 Primary Owner를 지정한다.
- Review 대상과 완료 기준을 명확히 한다.
- 순차 실행이 필요한 의존성을 무시하지 않는다.

---

### [FAQ]

Q. Task Decomposition은 뭐야?
A. 큰 사용자 요청을 실행 가능한 작은 작업으로 나누고 담당 Agent와 완료 기준을 정하는 과정이다.

Q. Task Decomposition은 누가 해?
A. PM Agent가 수행한다.

Q. 좋은 Subtask 조건은?
A. 담당 Agent, 입력 Context, 기대 산출물, 완료 기준이 명확해야 한다.

Q. Task를 너무 많이 나누면 안 돼?
A. 너무 잘게 나누면 Handoff와 실행 오버헤드가 증가한다.

---

# 5. Priority Decision

## 5.1 Priority Decision Definition

### [개념]

Priority Decision은 여러 Subtask 중 어떤 작업을 먼저 처리할지 결정하는 과정이다.

PM Agent는 사용자 가치, 의존성, 위험도, Review 필요성, Tool 필요성을 기준으로 우선순위를 정한다.

---

### [핵심]

- 선행 의존성이 있는 작업을 먼저 처리한다.
- 사용자 목적에 직접 연결되는 작업을 우선한다.
- 위험도가 높은 작업은 먼저 식별한다.
- Review가 필요한 작업은 중간 산출물을 남긴다.
- Tool 사용이 필요한 작업은 권한과 실패 가능성을 확인한다.
- 불확실성이 큰 작업은 Assumption 또는 Clarification으로 분리한다.

---

### [실무]

Priority 기준:

| 우선순위 | 기준                                    |
| -------- | --------------------------------------- |
| P0       | 안전, 보안, 데이터 손실, 비용 발생 위험 |
| P1       | 핵심 요구사항, 선행 의존성              |
| P2       | 주요 기능 구현, 검증 필요 작업          |
| P3       | 품질 개선, 리팩토링, 문서 보강          |
| P4       | 선택 기능, 편의 기능, 스타일 개선       |

Priority Decision Template:

```md
## Priority Decision

### Priority Rules

### Ordered Tasks

| Priority | Task | Reason | Risk | Owner Agent |
| -------- | ---- | ------ | ---- | ----------- |

### Deferred Tasks

### Blocking Issues
```

예시:

```md
## Priority Decision

| Priority | Task                   | Reason                 | Risk                     | Owner Agent    |
| -------- | ---------------------- | ---------------------- | ------------------------ | -------------- |
| P1       | DB 제약 확인           | Backend 설계 선행 조건 | Schema 불일치            | SQL Agent      |
| P1       | 회원가입 Service Flow  | 핵심 기능              | 인증 흐름 오류           | Backend Agent  |
| P2       | Password Encoding 검토 | 보안 필수              | Plain Password 저장 위험 | Security Agent |
| P2       | 테스트 케이스 작성     | 검증 필요              | 누락 가능성              | Testing Agent  |
| P3       | 응답 메시지 개선       | 품질 개선              | 낮음                     | Backend Agent  |
```

주의:

- 구현 편의성보다 의존성과 위험도를 우선한다.
- 보안과 데이터 손실 위험은 항상 높은 우선순위로 처리한다.
- 낮은 우선순위 작업이 핵심 작업을 방해하지 않게 한다.
- Deferred Task를 숨기지 않는다.

---

### [FAQ]

Q. Priority Decision은 뭐야?
A. 여러 작업 중 어떤 작업을 먼저 처리할지 결정하는 과정이다.

Q. PM Agent는 우선순위를 어떻게 정해?
A. 의존성, 사용자 가치, 위험도, Review 필요성, Tool 필요성을 기준으로 정한다.

Q. 가장 먼저 처리해야 하는 것은?
A. 안전, 보안, 데이터 손실, 비용 발생 위험과 선행 의존성이 있는 작업이다.

Q. 선택 기능은 어떻게 처리해?
A. 핵심 작업 이후 Deferred Task 또는 낮은 우선순위로 분리한다.

---

# 6. Scope Control

## 6.1 Scope Control Definition

### [개념]

Scope Control은 Agent Workflow가 사용자 요청 범위를 벗어나지 않도록 작업 범위를 통제하는 과정이다.

PM Agent는 현재 작업에 포함할 내용과 제외할 내용을 명확히 해야 한다.

Scope Control 필수 요소:

- In Scope
- Out of Scope
- Constraints
- Assumptions
- Deferred Tasks
- Risky Expansion
- User Confirmation Required

---

### [핵심]

- 사용자 요청의 핵심 범위를 유지한다.
- 현재 작업에 포함하지 않을 범위를 명시한다.
- Agent가 임의로 구조를 확장하지 않게 한다.
- 기존 API, DTO, DB 계약 변경 시 영향을 표시한다.
- Deferred Task를 별도로 분리한다.
- 위험하거나 비용이 드는 확장은 사용자 확인이 필요하다.

---

### [실무]

Scope Control Template:

```md
## Scope Control

### In Scope

### Out of Scope

### Constraints

### Deferred Tasks

### Risky Expansion

### User Confirmation Required
```

예시:

```md
## Scope Control

### In Scope

- 회원가입 Request DTO
- 회원가입 Service Flow
- 회원가입 Controller Endpoint
- 예외 케이스

### Out of Scope

- 소셜 로그인
- 이메일 인증 구현
- Frontend 회원가입 화면
- 배포 설정

### Constraints

- 기존 users table 구조 우선
- ApiResponse<T> 직접 반환
- GlobalExceptionHandler 사용

### Deferred Tasks

- 이메일 인증 필수 여부 결정 후 추가 구현
- Frontend Form 연동

### User Confirmation Required

No
```

금지:

- 요청하지 않은 기능 추가
- 기존 프로젝트 구조 임의 변경
- Out of Scope 작업을 몰래 포함
- 위험 확장을 승인 없이 진행
- 불확실한 요구사항을 확정 처리

---

### [FAQ]

Q. Scope Control은 뭐야?
A. Agent Workflow가 사용자 요청 범위를 벗어나지 않도록 포함 범위와 제외 범위를 통제하는 과정이다.

Q. 왜 Scope Control이 필요해?
A. Agent가 요청하지 않은 기능을 추가하거나 기존 구조를 임의로 변경하는 것을 막기 위해 필요하다.

Q. Out of Scope는 왜 적어야 해?
A. 이번 작업에서 하지 않을 일을 명확히 해야 Agent가 범위를 넘지 않는다.

Q. Deferred Task는 뭐야?
A. 지금은 처리하지 않고 나중에 별도 작업으로 넘기는 항목이다.

---

# 7. PM Agent Handoff

## 7.1 PM Agent Handoff Definition

### [개념]

PM Agent Handoff는 PM Agent가 Domain Agent에게 작업을 넘기는 구조화된 전달 문서이다.

PM Agent Handoff는 다음 Agent가 바로 작업할 수 있을 만큼 명확해야 한다.

필수 요소:

- From
- To
- Task
- Goal
- Context
- Input
- Constraints
- Expected Output
- Done Criteria
- Assumptions
- Open Questions

---

### [핵심]

- PM Agent Handoff는 Agent Workflow 품질의 핵심이다.
- Task와 Context를 분리한다.
- Expected Output을 명확히 지정한다.
- Done Criteria를 포함한다.
- Assumptions와 Open Questions를 구분한다.
- 기존 Project Rules와 Domain Rules를 포함한다.
- 이전 추정을 사실처럼 넘기지 않는다.

---

### [실무]

PM Agent Handoff Template:

```md
## Handoff

From: PM Agent
To: Backend Agent

### Task

### Goal

### Context

### Input

### Constraints

### Expected Output

### Done Criteria

### Assumptions

### Open Questions

### Review Target
```

예시:

```md
## Handoff

From: PM Agent
To: Backend Agent

### Task

회원가입 API 설계

### Goal

회원가입 요청을 받아 User를 생성하는 Backend Flow 설계

### Context

- Spring Boot 3.x
- Java 21
- ApiResponse<T> 직접 반환
- GlobalExceptionHandler 사용
- Password는 BCrypt Encoding 필요

### Input

- User Request
- Existing Entity
- Backend Domain Rules
- Security Domain Rules

### Constraints

- Entity 임의 생성 금지
- 기존 API 계약 변경 시 영향 명시
- Password 평문 저장 금지

### Expected Output

- SignUpReqDto
- UserResDto
- Service Flow
- Controller Endpoint
- Exception Cases

### Done Criteria

- 필수 Validation 포함
- 중복 이메일 처리 포함
- Password Encoding 포함
- Review Agent가 검증 가능한 구조

### Assumptions

- 이메일은 unique 값으로 사용

### Open Questions

- 이메일 인증 필수 여부 미확정

### Review Target

Security, Validation, Exception Flow
```

주의:

- Handoff가 길어도 핵심 제약은 누락하지 않는다.
- 관련 없는 전체 대화는 전달하지 않는다.
- Output Format을 지정하지 않으면 결과 품질이 흔들린다.
- Domain Agent가 임의로 범위를 확장하지 않게 한다.

---

### [FAQ]

Q. PM Agent Handoff는 뭐야?
A. PM Agent가 Domain Agent에게 Task, Context, Constraints, Expected Output, Done Criteria를 전달하는 구조화된 문서이다.

Q. PM Agent Handoff에 가장 중요한 것은?
A. Task, Constraints, Expected Output, Done Criteria이다.

Q. Handoff에 Assumption을 왜 넣어?
A. 불확실한 내용을 사실과 구분하고 Review Agent가 검증할 수 있게 하기 위해 필요하다.

Q. Handoff가 부실하면 어떻게 돼?
A. Domain Agent가 임의 추정하거나 잘못된 범위의 결과를 만들 수 있다.

---

# 8. PM Agent Shared State Update

## 8.1 Shared State Update Definition

### [개념]

PM Agent Shared State Update는 Workflow 진행 중 요구사항, 결정 사항, Agent 결과, Review 결과를 공통 상태에 기록하는 과정이다.

PM Agent는 Workflow 전체 상태를 관리해야 한다.

기록 대상:

- User Request
- Requirements
- Constraints
- Decisions
- Assumptions
- Current Task
- Assigned Agents
- Agent Outputs
- Review Findings
- Open Questions
- Status

---

### [핵심]

- PM Agent는 Shared State의 관리자 역할을 한다.
- 사용자 요청과 확정된 결정을 기록한다.
- Agent별 중간 결과를 구조화한다.
- Review Finding과 Fix 결과를 반영한다.
- 최신 요청이 오래된 State보다 우선한다.
- 불필요한 전체 대화 저장은 피한다.
- 민감정보 저장은 최소화한다.

---

### [실무]

PM Shared State Template:

```json
{
  "userRequest": "",
  "requirements": [],
  "constraints": [],
  "decisions": [],
  "assumptions": [],
  "currentTask": "",
  "assignedAgents": [],
  "agentOutputs": {},
  "reviewFindings": [],
  "openQuestions": [],
  "status": "in_progress"
}
```

상태 값:

```text
in_progress
handoff_ready
agent_execution
review_required
fix_required
blocked
completed
failed
user_confirmation_required
```

예시:

```json
{
  "userRequest": "회원가입 기능 만들어줘",
  "requirements": [
    "회원가입 API 설계",
    "중복 이메일 처리",
    "Password Encoding"
  ],
  "constraints": [
    "Spring Boot 3.x",
    "ApiResponse<T> 직접 반환",
    "GlobalExceptionHandler 사용"
  ],
  "decisions": ["Password는 BCrypt 사용"],
  "assumptions": ["이메일은 unique 값으로 사용"],
  "currentTask": "Backend Agent Handoff",
  "assignedAgents": [
    "SQL Agent",
    "Backend Agent",
    "Security Agent",
    "Review Agent"
  ],
  "agentOutputs": {},
  "reviewFindings": [],
  "openQuestions": ["이메일 인증 필수 여부"],
  "status": "handoff_ready"
}
```

주의:

- Agent Output은 이름별로 분리한다.
- Review Finding은 수정 전까지 유지한다.
- Fix 완료 후 Change Summary를 추가한다.
- 완료 시 Final Result를 기록한다.
- State가 커지면 필요한 정보만 압축한다.

---

### [FAQ]

Q. PM Agent가 Shared State를 관리해야 해?
A. 그렇다. PM Agent는 요구사항, 결정 사항, Agent 결과, Review 결과를 공통 상태로 관리해야 한다.

Q. Shared State에는 무엇을 기록해?
A. User Request, Requirements, Constraints, Decisions, Assumptions, Agent Outputs, Review Findings, Status를 기록한다.

Q. 오래된 State와 최신 요청이 충돌하면?
A. 최신 사용자 요청과 최신 결정 사항을 우선한다.

Q. Shared State를 전체 대화로 저장해도 돼?
A. 권장하지 않는다. 작업에 필요한 핵심 정보만 구조화해서 저장해야 한다.

---

# 9. PM Agent Review Request

## 9.1 Review Request Definition

### [개념]

PM Agent Review Request는 Domain Agent 산출물을 Review Agent에게 검증 요청하는 과정이다.

PM Agent는 Review Agent에게 단순히 “검토해줘”라고 보내지 않는다.
검토 기준, 대상, 요구사항, 제약 조건, 중요 위험을 함께 전달해야 한다.

---

### [핵심]

- Review 대상 산출물을 명확히 지정한다.
- 검토 기준을 명확히 전달한다.
- 요구사항과 제약 조건을 함께 전달한다.
- Severity 기준을 지정한다.
- Review 결과 형식을 지정한다.
- Review Agent가 취향과 결함을 구분하게 한다.
- Review 후 Fix 필요 여부를 판단한다.

---

### [실무]

Review Request Template:

```md
## Review Request

From: PM Agent
To: Review Agent

### Review Target

### Original Requirement

### Constraints

### Domain Rules

### Review Criteria

### Severity Rule

### Expected Review Output

### Pass Condition
```

예시:

```md
## Review Request

From: PM Agent
To: Review Agent

### Review Target

Backend Agent의 회원가입 API 설계안

### Original Requirement

회원가입 기능 설계

### Constraints

- Spring Boot 3.x
- Java 21
- ApiResponse<T> 직접 반환
- GlobalExceptionHandler 사용
- Password 평문 저장 금지

### Domain Rules

- Backend Domain Rules
- Security Domain Rules
- API Design Domain Rules

### Review Criteria

- 요구사항 충족 여부
- Validation 누락 여부
- Password Encoding 적용 여부
- Exception Flow 적절성
- API 응답 일관성

### Severity Rule

- Critical: 보안/데이터 손실/실행 불가
- Major: 핵심 요구사항 누락
- Minor: 품질 개선
- Info: 참고 의견

### Expected Review Output

- Finding
- Severity
- Cause
- Impact
- Fix Direction
- Pass / Fail

### Pass Condition

Critical 또는 Major Issue 없음
```

주의:

- Review 기준 없이 검토 요청 금지
- 취향 기반 지적과 결함을 구분하도록 지시
- Fix Direction 없는 Finding은 품질이 낮음
- Review 기준이 중간에 바뀌면 Loop가 불안정해짐

---

### [FAQ]

Q. PM Agent Review Request는 뭐야?
A. PM Agent가 Domain Agent 산출물을 Review Agent에게 기준과 함께 검증 요청하는 과정이다.

Q. Review Request에 무엇을 넣어야 해?
A. Review Target, Original Requirement, Constraints, Domain Rules, Review Criteria, Severity Rule, Pass Condition을 넣어야 한다.

Q. 그냥 “검토해줘”라고 하면 안 돼?
A. 검토 기준이 없으면 Review Agent가 취향 기반 지적을 하거나 중요한 결함을 놓칠 수 있다.

Q. Review Pass 조건은 어떻게 정해?
A. 일반적으로 Critical 또는 Major Issue가 없으면 Pass로 처리한다.

---

# 10. Final Integration

## 10.1 Final Integration Definition

### [개념]

Final Integration은 PM Agent가 여러 Agent의 산출물과 Review 결과를 통합해 사용자에게 제공할 최종 결과로 정리하는 과정이다.

Final Integration은 내부 중간 결과를 그대로 나열하는 것이 아니다.
사용자 목적에 맞는 최종 산출물, 결정 사항, 주의점, 남은 이슈를 정리한다.

---

### [핵심]

- PM Agent는 Agent별 결과를 하나로 통합한다.
- 사용자 요청 목적에 맞는 형태로 정리한다.
- Review 결과를 반영한다.
- Fix 완료 여부를 확인한다.
- 남은 Open Issue를 숨기지 않는다.
- 내부 Handoff나 불필요한 중간 논리는 제거한다.
- 최종 산출물은 바로 사용할 수 있어야 한다.

---

### [실무]

Final Integration Template:

```md
## Final Integration

### Final Output

### Applied Decisions

### Included Scope

### Excluded Scope

### Remaining Issues

### Validation Result

### Next Recommended Step
```

예시:

```md
## Final Integration

### Final Output

회원가입 API 설계안 최종본

### Applied Decisions

- Password는 BCrypt Encoding 적용
- 중복 이메일은 BusinessException 처리
- ApiResponse<T> 직접 반환 유지

### Included Scope

- DTO
- Service Flow
- Controller Endpoint
- Exception Cases

### Excluded Scope

- 이메일 인증 구현
- Frontend Form 연동
- 소셜 로그인

### Remaining Issues

- 이메일 인증 필수 여부 미확정

### Validation Result

Review Passed
```

주의:

- Review에서 Fail된 결과를 최종본으로 통합하지 않는다.
- 내부 Agent 로그를 사용자에게 그대로 노출하지 않는다.
- 미확정 사항은 Remaining Issues로 표시한다.
- 사용자에게 필요한 최종 형식으로 재구성한다.
- 산출물과 설명을 섞어 흐리게 만들지 않는다.

---

### [FAQ]

Q. Final Integration은 뭐야?
A. 여러 Agent 산출물과 Review 결과를 통합해 사용자에게 제공할 최종 결과로 정리하는 과정이다.

Q. PM Agent가 최종 결과를 만들 때 무엇을 확인해?
A. 요구사항 충족 여부, Review Pass 여부, Fix 반영 여부, 남은 이슈를 확인한다.

Q. 중간 결과를 전부 사용자에게 보여줘야 해?
A. 아니다. 사용자는 최종 결과만 확인하고, 중간 결과는 내부 검증용으로 사용할 수 있다.

Q. 남은 이슈는 숨겨도 돼?
A. 안 된다. 미확정 사항이나 남은 위험은 명확히 표시해야 한다.

---

# 11. PM Agent Failure Handling

## 11.1 PM Agent Failure Handling Definition

### [개념]

PM Agent Failure Handling은 PM Agent가 Workflow 진행 중 발생하는 실패를 분류하고, 재시도·대체·사용자 확인·중단 중 하나로 처리하는 과정이다.

PM Agent는 실패를 숨기지 않고 Shared State에 기록해야 한다.

---

### [핵심]

- 실패 유형을 분류한다.
- 재시도 가능한 실패와 중단해야 하는 실패를 구분한다.
- Missing Information은 Clarification으로 연결한다.
- Tool Failure는 Tool Result와 함께 기록한다.
- Retrieval Failure는 근거 부족으로 표시한다.
- Review Failure는 Fix Agent에게 전달한다.
- Unsafe Action은 즉시 중단하거나 사용자 확인을 요구한다.

---

### [실무]

PM Failure Type:

| Failure Type         | 처리                             |
| -------------------- | -------------------------------- |
| Missing Information  | Assumption 또는 사용자 확인      |
| Invalid Routing      | PM Agent 재분석 후 재라우팅      |
| Handoff Failure      | Handoff 재작성                   |
| Domain Agent Failure | Retry 또는 Fallback Agent        |
| Retrieval Failure    | 검색 실패 표시, Assumption 제한  |
| Tool Failure         | 실패 원인 기록, 재시도 또는 중단 |
| Review Failure       | Fix Agent로 전달                 |
| Unsafe Action        | Stop 또는 Human Confirmation     |

PM Failure Handling Template:

```md
## PM Failure Handling

### Failure Type

### Detected At

### Cause

### Impact

### Recovery Option

Retry / Fallback / Ask User / Stop

### State Update

### Next Step
```

예시:

```md
## PM Failure Handling

### Failure Type

Invalid Routing

### Detected At

Backend Agent Output Review

### Cause

Security 관련 작업을 Backend Agent에만 배정함

### Impact

Password Encoding과 인증 흐름 검토 누락 가능

### Recovery Option

Fallback

### State Update

Security Agent 추가 배정

### Next Step

Security Agent에게 Review Handoff 전달
```

금지:

- 실패를 성공처럼 처리
- 실패 원인 기록 없이 재시도
- 같은 실패를 무제한 반복
- 위험 작업을 자동 진행
- Review Failure를 무시하고 Final Output 생성

---

### [FAQ]

Q. PM Agent Failure Handling은 뭐야?
A. Workflow 중 발생한 실패를 PM Agent가 분류하고 Retry, Fallback, 사용자 확인, Stop 중 하나로 처리하는 과정이다.

Q. Routing이 잘못되면 어떻게 해?
A. PM Agent가 재분석하고 올바른 Agent로 재라우팅해야 한다.

Q. Domain Agent가 실패하면 어떻게 해?
A. 재시도하거나 Fallback Agent를 사용하고, 실패 원인을 Shared State에 기록한다.

Q. Review Failure가 발생하면 어떻게 해?
A. Finding을 Fix Agent에게 전달하고 수정 후 재검토한다.

---

# 12. PM Agent Anti-Patterns

## 12.1 PM Agent Anti-Patterns Definition

### [개념]

PM Agent Anti-Patterns는 PM Agent 설계에서 피해야 하는 잘못된 패턴이다.

PM Agent는 조율자 역할을 해야 하며, 구현자·검토자·수정자 역할을 모두 독점하면 안 된다.

---

### [핵심]

- PM Agent가 모든 구현을 직접 수행
- Task Decomposition 없이 Domain Agent 호출
- Handoff 없이 사용자 요청만 전달
- Scope Control 없이 기능 확장
- Review 기준 없이 검토 요청
- Shared State 없이 중간 결정 누락
- 사용자 승인 없이 위험 작업 실행
- Open Question을 숨김
- 실패를 성공처럼 처리
- Final Output에 내부 중간 결과를 무분별하게 포함

---

### [실무]

Anti-Pattern:

```text
User Request
→ PM Agent가 전체 코드 작성
→ Review 없이 Final Output
```

문제:

- Domain Agent 역할 없음
- Review 품질 낮음
- 책임 분리 실패
- Multi-Agent 구조 의미 없음

개선:

```text
User Request
→ PM Agent Task Analysis
→ Domain Agent Handoff
→ Domain Agent Output
→ Review Agent
→ Fix Agent
→ PM Agent Final Integration
```

Anti-Pattern:

```text
PM Agent:
"Backend Agent야 회원가입 만들어줘."
```

문제:

- Context 없음
- Constraints 없음
- Expected Output 없음
- Done Criteria 없음

개선:

```md
## Handoff

From: PM Agent
To: Backend Agent

### Task

회원가입 API 설계

### Context

Spring Boot 3.x, Java 21, ApiResponse<T> 직접 반환

### Expected Output

DTO, Service Flow, Controller Endpoint, Exception Cases

### Done Criteria

Validation, Password Encoding, 중복 이메일 처리 포함
```

---

### [FAQ]

Q. PM Agent의 가장 큰 Anti-Pattern은?
A. PM Agent가 모든 구현을 직접 처리하고 Domain Agent와 Review Agent를 사용하지 않는 것이다.

Q. Handoff 없이 Agent를 호출하면 왜 문제야?
A. Context, 제약, 기대 산출물이 불명확해져 Agent가 임의로 작업할 가능성이 높아진다.

Q. PM Agent가 Review까지 직접 하면 안 돼?
A. Self-Check는 가능하지만, 복잡한 작업은 독립 Review Agent가 더 안정적이다.

Q. PM Agent가 Scope를 통제하지 않으면 어떻게 돼?
A. Agent가 요청하지 않은 기능을 추가하거나 기존 구조를 임의로 변경할 수 있다.

---

# Retrieval Queries

### [FAQ]

Q. PM Agent는 뭐야?
A. 사용자 요청을 분석하고 작업을 분해하며, 적절한 Agent에게 라우팅하고 최종 결과를 통합하는 조율 Agent이다.

Q. PM Agent의 핵심 역할은?
A. User Request Analysis, Requirement Clarification, Task Decomposition, Agent Routing, Scope Control, Handoff, Review Request, Final Integration이다.

Q. PM Agent가 직접 구현해도 돼?
A. 원칙적으로 직접 구현보다 분석, 분해, 라우팅, 통합에 집중해야 한다.

Q. PM Agent가 중요한 이유는?
A. PM Agent가 작업 범위와 흐름을 정하기 때문에 전체 Agent Workflow 품질이 결정된다.

Q. User Request Analysis는 뭐야?
A. 사용자의 요청을 Agent Workflow에서 실행 가능한 요구사항과 작업 단위로 변환하는 과정이다.

Q. PM Agent는 사용자 요청에서 무엇을 추출해?
A. Goal, Requested Output, Domain, Constraints, Assumptions, Missing Information, Required Agents, Stop Condition을 추출한다.

Q. Requirement Clarification은 뭐야?
A. 불명확한 요구사항을 확인하거나 작업 가능한 가정으로 정리하는 과정이다.

Q. 언제 사용자에게 질문해야 해?
A. 작업 진행에 필수 정보가 없거나 위험 작업, 비용 발생, 외부 변경이 포함될 때 질문해야 한다.

Q. 모든 불확실성마다 질문해야 해?
A. 아니다. 경미한 불확실성은 Assumption으로 표시하고 진행할 수 있다.

Q. Task Decomposition은 뭐야?
A. 큰 사용자 요청을 실행 가능한 작은 작업으로 나누고 담당 Agent와 완료 기준을 정하는 과정이다.

Q. Task Decomposition은 누가 해?
A. PM Agent가 수행한다.

Q. 좋은 Subtask 조건은?
A. 담당 Agent, 입력 Context, 기대 산출물, 완료 기준이 명확해야 한다.

Q. Priority Decision은 뭐야?
A. 여러 작업 중 어떤 작업을 먼저 처리할지 결정하는 과정이다.

Q. PM Agent는 우선순위를 어떻게 정해?
A. 의존성, 사용자 가치, 위험도, Review 필요성, Tool 필요성을 기준으로 정한다.

Q. Scope Control은 뭐야?
A. Agent Workflow가 사용자 요청 범위를 벗어나지 않도록 포함 범위와 제외 범위를 통제하는 과정이다.

Q. Out of Scope는 왜 필요해?
A. 이번 작업에서 하지 않을 일을 명확히 해야 Agent가 범위를 넘지 않는다.

Q. PM Agent Handoff는 뭐야?
A. PM Agent가 Domain Agent에게 Task, Context, Constraints, Expected Output, Done Criteria를 전달하는 구조화된 문서이다.

Q. PM Agent Handoff에 무엇을 넣어야 해?
A. From, To, Task, Goal, Context, Input, Constraints, Expected Output, Done Criteria, Assumptions, Open Questions를 넣어야 한다.

Q. Handoff가 부실하면 어떻게 돼?
A. Domain Agent가 임의 추정하거나 잘못된 범위의 결과를 만들 수 있다.

Q. PM Agent가 Shared State를 관리해야 해?
A. 그렇다. PM Agent는 요구사항, 결정 사항, Agent 결과, Review 결과를 공통 상태로 관리해야 한다.

Q. Shared State에는 무엇을 기록해?
A. User Request, Requirements, Constraints, Decisions, Assumptions, Agent Outputs, Review Findings, Status를 기록한다.

Q. PM Agent Review Request는 뭐야?
A. PM Agent가 Domain Agent 산출물을 Review Agent에게 기준과 함께 검증 요청하는 과정이다.

Q. Review Request에 무엇을 넣어야 해?
A. Review Target, Original Requirement, Constraints, Domain Rules, Review Criteria, Severity Rule, Pass Condition을 넣어야 한다.

Q. Final Integration은 뭐야?
A. 여러 Agent 산출물과 Review 결과를 통합해 사용자에게 제공할 최종 결과로 정리하는 과정이다.

Q. PM Agent가 최종 결과를 만들 때 무엇을 확인해?
A. 요구사항 충족 여부, Review Pass 여부, Fix 반영 여부, 남은 이슈를 확인한다.

Q. PM Agent Failure Handling은 뭐야?
A. Workflow 중 발생한 실패를 PM Agent가 분류하고 Retry, Fallback, 사용자 확인, Stop 중 하나로 처리하는 과정이다.

Q. Routing이 잘못되면 어떻게 해?
A. PM Agent가 재분석하고 올바른 Agent로 재라우팅해야 한다.

Q. PM Agent의 가장 큰 Anti-Pattern은?
A. PM Agent가 모든 구현을 직접 처리하고 Domain Agent와 Review Agent를 사용하지 않는 것이다.

Q. PM Agent가 일을 너무 많이 하면 어떻게 해?
A. PM Agent를 분석, 분해, 라우팅, 통합 중심으로 제한하고 Domain Agent에게 명확히 Handoff한다.
