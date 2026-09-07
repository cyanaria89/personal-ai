# Agent Workflow Design Part01 Core

---

# 1. Agent Workflow Core

## 1.1 Agent Workflow Definition

### [개념]

Agent Workflow는 사용자 요청을 Agent가 처리 가능한 단계로 나누고, 각 단계의 입력·출력·상태·검증·종료 조건을 연결한 실행 구조이다.

Agent Workflow는 단순한 프롬프트 모음이 아니다.
Agent Workflow는 역할, 책임, 순서, 상태, 검증 기준을 포함한다.

기본 구성:

- User Request
- Task Analysis
- Agent Routing
- Agent Execution
- Intermediate Output
- Review
- Fix
- Final Output
- Stop Condition
- Failure Handling

---

### [핵심]

- Agent Workflow는 LLM 호출을 책임과 순서에 따라 연결한 구조이다.
- Agent는 명확한 Role과 Responsibility를 가져야 한다.
- Workflow는 Input, Output, State, Stop Condition을 가져야 한다.
- 복잡한 작업은 Task Decomposition 후 처리한다.
- 산출물은 Review 가능한 구조로 작성한다.
- Review / Fix Loop는 품질 검증과 수정에 사용한다.
- Stop Condition이 없으면 무한 반복 위험이 있다.
- Failure Handling이 없으면 실패 결과를 성공처럼 처리할 수 있다.

---

### [실무]

2026 실무 기준 Agent Workflow는 다음 흐름을 기본으로 한다.

```text
User Request
→ Task Analysis
→ Agent Routing
→ Agent Execution
→ Intermediate Output
→ Review
→ Fix
→ Final Output
```

개인 AI 개발팀 구조에서는 사용자가 PM Agent에게 요청하고, PM Agent가 필요한 Domain Agent에게 작업을 분배한다.

권장 기준:

- 단순 질의는 Single Agent Workflow 사용
- 복잡한 개발 작업은 Multi-Agent Workflow 사용
- 코드 생성 작업은 Review 단계 포함
- 위험 작업은 Human-in-the-loop 적용
- RAG 기반 작업은 Domain Rules 우선 검색
- 로컬 LLM 환경은 순차 실행 우선
- 최종 출력 전 Review Passed 상태 확인

금지:

- Agent를 단순 프롬프트 모음으로만 설계
- 모든 Agent가 모든 일을 하게 설계
- 종료 조건 없는 반복 구조
- Review 없이 자동 완료
- Tool 실패를 성공처럼 처리
- 검색 실패를 숨기고 확정 답변 생성

---

### [FAQ]

Q. Agent Workflow가 뭐야?
A. 사용자 요청을 분석하고, 필요한 Agent가 순서대로 작업하며, 검토와 수정을 거쳐 최종 결과를 만드는 실행 흐름이다.

Q. Agent Workflow는 프롬프트 체인이야?
A. 아니다. 프롬프트뿐 아니라 역할, 상태, 입력, 출력, 검증, 종료 조건을 포함한다.

Q. Agent Workflow가 필요한 이유는?
A. 복잡한 작업을 분해하고 검증 가능한 구조로 처리해 결과 품질을 높이기 위해 필요하다.

Q. 모든 작업에 Agent Workflow가 필요해?
A. 아니다. 단순 질의응답은 Single Agent로 충분하고, 복잡한 개발·검증 작업에 Workflow가 적합하다.

---

# 2. Standard Workflow Flow

## 2.1 Basic Flow

### [개념]

Standard Workflow Flow는 Agent Workflow의 기본 실행 순서이다.

각 단계는 다음 단계가 사용할 수 있는 구조화된 산출물을 만들어야 한다.

기본 Flow:

```text
User Request
→ Understand Goal
→ Identify Task Type
→ Select Agent
→ Execute Task
→ Produce Intermediate Output
→ Review Output
→ Fix Issues
→ Generate Final Output
```

---

### [핵심]

- User Request는 Workflow의 시작점이다.
- Task Analysis는 목표와 제약을 식별한다.
- Agent Routing은 담당 Agent를 선택한다.
- Agent Execution은 실제 작업 수행 단계이다.
- Intermediate Output은 다음 Agent가 사용할 중간 산출물이다.
- Review는 요구사항과 규칙 기준으로 검증한다.
- Fix는 Review Finding을 반영한다.
- Final Output은 사용자에게 필요한 형태로 정리한다.

---

### [실무]

권장 단계별 산출물:

| 단계                | 산출물                             |
| ------------------- | ---------------------------------- |
| Task Analysis       | Goal, Requirement, Constraint      |
| Agent Routing       | Selected Agent, Routing Reason     |
| Agent Execution     | Draft Output, Decision, Assumption |
| Intermediate Output | Summary, Details, Open Issues      |
| Review              | Finding, Severity, Fix Direction   |
| Fix                 | Updated Output, Change Summary     |
| Final Output        | User-facing Answer or Artifact     |

간단한 작업:

```text
User Request
→ Single Agent
→ Self Check
→ Final Output
```

복잡한 작업:

```text
User Request
→ PM Agent
→ Domain Agent
→ Review Agent
→ Fix Agent
→ Final Output
```

주의:

- 중간 산출물 없이 최종 답변만 만들지 않는다.
- Review 기준 없이 검토하지 않는다.
- Fix 후 Re-review 필요 여부를 판단한다.
- Final Output은 Review 결과를 반영해야 한다.

---

### [FAQ]

Q. Agent Workflow의 기본 순서는?
A. User Request → Task Analysis → Agent Routing → Agent Execution → Review → Fix → Final Output 순서이다.

Q. 중간 산출물이 왜 필요해?
A. 다음 Agent가 이전 작업을 검증하고 이어받을 수 있어야 하기 때문이다.

Q. Review는 항상 필요해?
A. 단순 작업은 Self Check로 충분할 수 있지만, 개발·보안·배포·DB 작업은 Review가 권장된다.

Q. Fix는 언제 실행해?
A. Review Agent가 Critical 또는 Major Finding을 발견했을 때 실행한다.

---

# 3. Agent Role Overview

## 3.1 Role Separation

### [개념]

Agent Role Separation은 Agent의 책임 범위를 명확히 나누는 설계 원칙이다.

Agent가 모든 작업을 동시에 처리하면 책임이 불명확해지고, Review 품질과 Handoff 품질이 낮아진다.

기본 Agent 역할:

- PM Agent
- Domain Agent
- Review Agent
- Fix Agent
- Final Response Agent

---

### [핵심]

- PM Agent는 요청 분석, 작업 분해, 라우팅, 최종 통합을 담당한다.
- Domain Agent는 특정 전문 영역의 작업을 수행한다.
- Review Agent는 산출물을 검증한다.
- Fix Agent는 Review Finding을 수정한다.
- Final Response Agent는 사용자 출력 형태로 정리한다.
- Agent 역할이 겹치면 Workflow 품질이 낮아진다.
- 각 Agent는 Input, Output, Done Criteria를 가져야 한다.

---

### [실무]

Agent 역할 요약:

| Agent                | Core Responsibility           | Main Output                  |
| -------------------- | ----------------------------- | ---------------------------- |
| PM Agent             | 분석, 분해, 라우팅, 통합      | Task Plan, Handoff           |
| SQL Agent            | Schema, Query, Constraint     | SQL Review, Query Suggestion |
| Backend Agent        | API, DTO, Service, Controller | Backend Output               |
| Frontend Agent       | UI, State, API Integration    | Frontend Output              |
| DevOps Agent         | Docker, Deploy, Runtime       | DevOps Output                |
| AI Agent             | RAG, LLM, Tool Calling, Agent | AI Workflow Output           |
| Review Agent         | 검증, Finding, Severity       | Review Finding               |
| Fix Agent            | 수정, Change Summary          | Updated Output               |
| Final Response Agent | 최종 사용자 응답 정리         | Final Answer                 |

초기 개인 AI 개발팀 권장 구성:

```text
User
→ PM Agent
→ Backend Agent
→ Review Agent
→ Final Output
```

확장 구성:

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

주의:

- PM Agent가 구현까지 모두 담당하지 않는다.
- Domain Agent가 다른 Domain을 임의 수정하지 않는다.
- Review Agent가 구현을 직접 담당하지 않는다.
- Fix Agent가 Review 범위를 넘어 임의 확장하지 않는다.

---

### [FAQ]

Q. Agent 역할을 왜 나눠야 해?
A. 각 Agent가 자기 책임에 집중해야 작업 품질과 검증 품질이 높아지기 때문이다.

Q. PM Agent는 무엇을 담당해?
A. 사용자 요청 분석, 작업 분해, Agent Routing, Handoff, 최종 통합을 담당한다.

Q. Domain Agent는 무엇을 담당해?
A. Backend, Frontend, SQL, DevOps, AI처럼 특정 전문 영역의 작업을 수행한다.

Q. Review Agent와 Fix Agent는 왜 분리해?
A. Review는 검증, Fix는 수정에 집중해야 책임이 명확해진다.

---

# 4. Single Agent Workflow

## 4.1 Single Agent Workflow Definition

### [개념]

Single Agent Workflow는 하나의 Agent가 사용자 요청 분석부터 최종 답변까지 처리하는 구조이다.

기본 Flow:

```text
User Request
→ Agent Analyze
→ Retrieve Context if Needed
→ Use Tool if Needed
→ Generate Answer
→ Self Check
→ Final Output
```

Single Agent Workflow는 단순하고 빠르지만 복잡한 개발 작업에는 검증 한계가 있다.

---

### [핵심]

- 하나의 Agent가 전체 작업을 처리한다.
- 구조가 단순하고 실행 속도가 빠르다.
- 작은 작업에 적합하다.
- Self Check는 가능하지만 독립 Review보다 약하다.
- 복잡한 작업에서는 책임이 과도하게 집중된다.
- Handoff가 필요 없는 작업에 적합하다.

---

### [실무]

적합한 경우:

- 단순 질의응답
- 짧은 코드 설명
- 간단한 문서 요약
- 단일 파일 기준 검토
- 작은 함수 리팩토링
- 간단한 RAG 질의

부적합한 경우:

- Backend + Frontend + DB 연동 작업
- 보안 검토가 필요한 작업
- 배포나 DB 변경 포함 작업
- 복잡한 코드 생성
- 독립 Review가 필요한 작업
- 여러 Domain의 의존성이 있는 작업

권장 Output:

```md
## Single Agent Output

### Summary

### Answer

### Assumptions

### Self Check

### Final
```

---

### [FAQ]

Q. Single Agent Workflow는 언제 써?
A. 단순 질의응답, 짧은 코드 설명, 간단한 문서 요약처럼 역할 분리가 필요 없는 작업에 사용한다.

Q. Single Agent의 장점은?
A. 구조가 단순하고 빠르며 운영 비용이 낮다.

Q. Single Agent의 단점은?
A. 복잡한 작업에서 분석, 실행, 검증 책임이 한 Agent에 몰려 품질이 낮아질 수 있다.

Q. Self Check만으로 충분해?
A. 간단한 작업은 가능하지만 복잡한 개발 작업은 독립 Review Agent가 더 안정적이다.

---

# 5. Multi-Agent Workflow

## 5.1 Multi-Agent Workflow Definition

### [개념]

Multi-Agent Workflow는 여러 Agent가 역할을 나누어 작업하는 구조이다.

기본 Flow:

```text
User Request
→ PM Agent
→ Task Decomposition
→ Domain Agent
→ Review Agent
→ Fix Agent
→ Final Output
```

Multi-Agent Workflow는 복잡한 작업을 전문 영역별로 분리하고 Review / Fix Loop를 통해 품질을 높이는 데 적합하다.

---

### [핵심]

- 여러 Agent가 역할을 나누어 처리한다.
- PM Agent가 요청을 분석하고 작업을 분해한다.
- Domain Agent가 전문 작업을 수행한다.
- Review Agent가 결과를 검증한다.
- Fix Agent가 문제를 수정한다.
- Final Output은 사용자 목적에 맞게 통합한다.
- Agent가 많을수록 Latency와 복잡도가 증가한다.

---

### [실무]

적합한 경우:

- 회원가입 기능 전체 설계
- DB Schema + Backend API + Frontend Form 연동
- Docker 기반 배포 구성
- RAG 기반 AI 기능 설계
- 프로젝트 코드 리뷰
- 테스트 케이스 작성 및 검증
- 보안이 포함된 인증/인가 설계

예시:

```text
User Request:
회원가입 기능 만들어줘

Workflow:
PM Agent
→ SQL Agent: users table 검토
→ Backend Agent: DTO / Service / Controller 설계
→ Security Agent: Password Encoding / Validation 검토
→ Testing Agent: 테스트 케이스 작성
→ Review Agent: 전체 검증
→ Fix Agent: 수정 반영
→ Final Output
```

주의:

- Agent 수를 처음부터 과도하게 늘리지 않는다.
- Handoff Template을 통일한다.
- Shared State에 결정 사항을 기록한다.
- Review / Fix Loop에는 Max Iteration을 둔다.
- Stop Condition을 명확히 정의한다.
- 로컬 LLM 환경에서는 순차 실행을 우선한다.

---

### [FAQ]

Q. Multi-Agent Workflow는 언제 써?
A. 작업이 복잡하거나 Backend, Frontend, SQL, DevOps, Review처럼 전문 영역을 나누는 것이 품질에 도움이 될 때 사용한다.

Q. Multi-Agent가 항상 더 좋아?
A. 아니다. Agent가 많으면 실행 시간이 길어지고 설계 복잡도가 증가한다.

Q. Multi-Agent의 핵심은?
A. 역할 분리, Task Decomposition, Handoff, Shared State, Review / Fix Loop이다.

Q. 개인 AI 개발팀에 Multi-Agent가 적합해?
A. 적합하다. 단, 초기에는 순차 실행 기반의 단순 Workflow로 시작하는 것이 현실적이다.

---

# 6. Task Decomposition Overview

## 6.1 Task Decomposition Definition

### [개념]

Task Decomposition은 큰 사용자 요청을 실행 가능한 작은 작업 단위로 나누는 과정이다.

Task Decomposition은 PM Agent의 핵심 책임이며, Multi-Agent Workflow의 시작점이다.

필수 요소:

- Goal
- Subtask
- Dependency
- Priority
- Owner Agent
- Expected Output
- Done Criteria

---

### [핵심]

- 큰 요청은 실행 가능한 단위로 나눈다.
- 각 Subtask는 담당 Agent가 명확해야 한다.
- 각 Subtask는 기대 산출물과 완료 기준이 있어야 한다.
- 선행 작업과 후행 작업 의존성을 고려한다.
- 병렬 가능 작업과 순차 작업을 구분한다.
- 너무 작게 쪼개면 오버헤드가 증가한다.
- 너무 크게 유지하면 Agent가 놓치는 부분이 증가한다.

---

### [실무]

Task Decomposition 기본 예시:

```text
User Request:
회원가입 기능 만들어줘

Task Decomposition:
1. SQL Agent: users table 제약 조건 검토
2. Backend Agent: DTO / Service / Controller 설계
3. Security Agent: Password Encoding / 인증 정책 검토
4. Testing Agent: 테스트 케이스 작성
5. Review Agent: 전체 산출물 검증
```

권장 Template:

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

주의:

- Task를 사람 기준이 아니라 산출물 기준으로 나눈다.
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

# 7. Agent Routing Overview

## 7.1 Agent Routing Definition

### [개념]

Agent Routing은 분석된 작업을 적절한 Agent에게 배정하는 과정이다.

Routing은 PM Agent의 핵심 책임이다.

Routing 기준:

- Task Type
- Domain
- Required Expertise
- Required Tool
- Priority
- Risk
- Fallback Agent

---

### [핵심]

- 작업 Domain에 맞는 Agent를 선택한다.
- 하나의 요청이 여러 Domain에 걸치면 순서를 정한다.
- 필요한 Tool 권한을 함께 고려한다.
- 담당 Agent가 실패하면 fallback을 사용한다.
- 모호한 요청은 PM Agent가 먼저 정리한다.
- Routing 결과는 Handoff로 이어져야 한다.

---

### [실무]

기본 Routing Rule:

```text
SQL / DB Schema → SQL Agent
Spring Boot / REST API → Backend Agent
React / UI → Frontend Agent
Docker / Deploy → DevOps Agent
RAG / LLM / Agent → AI Agent
Authentication / Authorization → Security Agent
Test Case / Verification → Testing Agent
Quality Review → Review Agent
Fix Review Finding → Fix Agent
```

Routing Decision Template:

```md
## Routing Decision

### Task

### Selected Agent

### Reason

### Required Context

### Expected Output

### Fallback Agent
```

주의:

- 하나의 요청을 무조건 하나의 Agent에게만 맡기지 않는다.
- 역할이 겹치는 경우 책임 기준을 정한다.
- Tool 권한이 없는 Agent에게 Tool 작업을 배정하지 않는다.
- Review Agent는 구현 담당이 아니라 검증 담당으로 사용한다.

---

### [FAQ]

Q. Agent Routing은 뭐야?
A. 작업 유형과 Domain에 따라 적절한 Agent를 선택하는 과정이다.

Q. Routing 기준은?
A. Task Type, Domain, 필요한 전문성, 필요한 Tool, 우선순위, 위험도를 기준으로 한다.

Q. 여러 Agent가 필요한 작업은 어떻게 해?
A. PM Agent가 작업 순서와 의존성을 정해 순차 또는 병렬로 배정한다.

Q. Routing 실패는 어떻게 처리해?
A. Fallback Agent를 사용하거나 PM Agent가 재분석한다.

---

# 8. Handoff Overview

## 8.1 Handoff Definition

### [개념]

Handoff는 한 Agent가 다음 Agent에게 작업을 전달하는 구조화된 형식이다.

Handoff는 다음 Agent가 바로 작업할 수 있도록 Task, Context, Constraints, Expected Output을 명확히 전달해야 한다.

필수 요소:

- Source Agent
- Target Agent
- Task
- Context
- Input
- Output Format
- Constraints
- Assumptions
- Open Questions

---

### [핵심]

- Handoff는 Agent 간 작업 전달 문서이다.
- Task와 Context를 분리한다.
- Expected Output을 명확히 지정한다.
- Constraints를 반드시 포함한다.
- Assumptions와 Open Questions를 구분한다.
- 이전 Agent의 추정을 사실처럼 넘기지 않는다.
- Handoff 형식이 다르면 Workflow가 깨질 수 있다.

---

### [실무]

Handoff Template:

```md
## Handoff

From: PM Agent
To: Backend Agent

### Task

회원가입 API 설계

### Context

- Spring Boot 3.x
- Java 21
- ApiResponse<T> 직접 반환
- GlobalExceptionHandler 사용

### Expected Output

- DTO
- Service Flow
- Controller Endpoint
- Exception Cases

### Constraints

- Entity 임의 생성 금지
- 기존 API 계약 변경 시 영향 명시

### Assumptions

- 이메일은 unique 값으로 사용

### Open Questions

- 이메일 인증 필수 여부 확인 필요
```

좋은 Handoff 조건:

- 다음 Agent가 바로 작업 가능
- 작업 범위가 명확함
- 출력 형식이 명확함
- 제약 조건이 누락되지 않음
- 미확정 사항이 표시됨

---

### [FAQ]

Q. Handoff가 뭐야?
A. 한 Agent가 다음 Agent에게 Task, Context, Constraints, Expected Output을 전달하는 구조화된 작업 전달이다.

Q. 좋은 Handoff에는 뭐가 들어가?
A. Source Agent, Target Agent, Task, Context, Input, Output Format, Constraints, Assumptions, Open Questions가 들어간다.

Q. Handoff가 모호하면 어떻게 돼?
A. 다음 Agent가 임의 추정하거나 잘못된 결과를 생성할 가능성이 높아진다.

Q. Handoff에 전체 대화를 다 넣어야 해?
A. 아니다. 필요한 Context만 압축해서 전달해야 한다.

---

# 9. Shared State Overview

## 9.1 Shared State Definition

### [개념]

Shared State는 Workflow 전체에서 유지되는 공통 작업 상태이다.

Shared State는 Agent 간 공통 기억 역할을 하며, 요구사항·결정 사항·중간 결과·검토 결과를 구조화해서 저장한다.

필수 포함:

- User Request
- Requirements
- Constraints
- Decisions
- Assumptions
- Current Task
- Agent Outputs
- Review Findings
- Open Questions
- Status

---

### [핵심]

- Shared State는 Workflow의 공통 작업 기록이다.
- 요구사항과 결정 사항을 유지한다.
- Agent Output을 구조화해서 저장한다.
- Review Finding과 Fix 결과를 반영한다.
- 최신 요구사항이 오래된 State보다 우선한다.
- 불필요한 전체 대화 저장은 Token 낭비이다.
- 민감정보 저장을 최소화한다.

---

### [실무]

기본 구조:

```json
{
  "userRequest": "",
  "requirements": [],
  "constraints": [],
  "decisions": [],
  "assumptions": [],
  "currentTask": "",
  "agentOutputs": {},
  "reviewFindings": [],
  "openQuestions": [],
  "status": "in_progress"
}
```

상태 값 예시:

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

주의:

- 오래된 State가 최신 요청을 덮어쓰지 않게 한다.
- Agent별 Output은 구조화한다.
- Review / Fix Loop 결과를 누락하지 않는다.
- State가 커지면 필요한 정보만 압축한다.

---

### [FAQ]

Q. Shared State가 뭐야?
A. Workflow 전체에서 공유되는 요구사항, 결정 사항, 중간 결과, Review 결과, 현재 상태를 저장하는 구조이다.

Q. Shared State와 대화 기록은 같아?
A. 아니다. Shared State는 작업에 필요한 핵심 정보만 구조화한 상태이다.

Q. Shared State에는 무엇을 저장해?
A. User Request, Requirements, Constraints, Decisions, Agent Outputs, Review Findings, Status를 저장한다.

Q. Shared State가 없으면 어떻게 돼?
A. Agent 간 결정 사항이 누락되고 Review와 Fix 단계가 이전 결과를 정확히 이어받기 어렵다.

---

# 10. Context Passing Overview

## 10.1 Context Passing Definition

### [개념]

Context Passing은 Shared State에서 다음 Agent에게 필요한 정보만 선별하여 전달하는 과정이다.

모든 Context를 넘기는 것이 항상 좋은 것은 아니다.
작업에 필요한 정보만 전달해야 Token 낭비를 줄이고 핵심 지시를 유지할 수 있다.

---

### [핵심]

- 작업에 필요한 Context만 전달한다.
- 중요한 제약과 결정 사항은 반드시 포함한다.
- Assumption과 Decision을 구분한다.
- 오래된 정보와 최신 정보가 충돌하면 최신 정보를 우선한다.
- 출처 없는 정보는 신뢰도를 낮게 취급한다.
- Context 과다 주입은 핵심 지시를 흐릴 수 있다.
- Context 누락은 Agent의 임의 추정을 유발한다.

---

### [실무]

Context Passing Flow:

```text
Full State
→ Select Relevant Context
→ Compress Context
→ Attach Source / Decision
→ Send to Next Agent
```

Context Passing Template:

```md
## Context Passing

### Relevant Context

### Required Constraints

### Decisions

### Assumptions

### Excluded Context

### Source
```

예시:

```md
## Context Passing

### Relevant Context

회원가입 API 설계 작업

### Required Constraints

- Spring Boot 3.x
- Java 21
- ApiResponse<T> 직접 반환
- GlobalExceptionHandler 사용

### Decisions

- Password는 BCrypt Encoding 사용
- 이메일 중복은 BusinessException 처리

### Assumptions

- 이메일 인증 여부는 미확정

### Excluded Context

- Frontend UI 상세는 이번 작업 범위 제외
```

---

### [FAQ]

Q. Context Passing이 뭐야?
A. 다음 Agent가 작업하는 데 필요한 Context만 Shared State에서 선별해 전달하는 과정이다.

Q. 모든 Context를 전달하면 안 돼?
A. 모든 Context를 전달하면 Token 낭비가 생기고 핵심 제약이 묻힐 수 있다.

Q. Context Passing에서 가장 중요한 것은?
A. 필요한 정보, 확정된 결정, 제약 조건, 가정을 구분해 전달하는 것이다.

Q. 오래된 정보와 최신 정보가 충돌하면?
A. 최신 사용자 요청과 최신 결정 사항을 우선한다.

---

# 11. Intermediate Output Overview

## 11.1 Intermediate Output Definition

### [개념]

Intermediate Output은 Agent가 다음 단계에서 사용할 수 있도록 생성하는 구조화된 중간 산출물이다.

Intermediate Output은 최종 사용자 답변이 아니다.
Review Agent, Fix Agent, PM Agent가 검증하고 통합할 수 있게 작성한다.

---

### [핵심]

- 중간 결과는 다음 Agent가 사용할 수 있어야 한다.
- Review 가능한 구조로 작성한다.
- 결정과 추정을 구분한다.
- 누락된 부분을 숨기지 않는다.
- 필요한 Artifact를 명확히 표시한다.
- Open Issue를 포함한다.
- Final Output과 구분한다.

---

### [실무]

Intermediate Output Template:

```md
## Agent Output

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

좋은 Intermediate Output 조건:

- 다음 Agent가 바로 검토 가능
- Review Criteria와 연결 가능
- 수정 대상이 명확함
- Open Issue가 숨겨지지 않음
- Done Criteria 충족 여부가 표시됨
- Final Output과 구분됨

주의:

- 코드만 던지고 판단 근거를 생략하지 않는다.
- Open Issue를 숨기지 않는다.
- Done Criteria를 충족하지 못했으면 완료로 표시하지 않는다.
- 최종 답변처럼 작성하지 않는다.

---

### [FAQ]

Q. Intermediate Output은 뭐야?
A. Agent가 다음 단계에서 사용할 수 있도록 생성하는 구조화된 중간 산출물이다.

Q. Intermediate Output과 Final Output은 달라?
A. 다르다. Intermediate Output은 Agent 간 전달용이고 Final Output은 사용자에게 보여주는 결과이다.

Q. Intermediate Output에 무엇을 넣어야 해?
A. Summary, Details, Decisions, Assumptions, Open Issues, Artifacts, Done Criteria Check, Review Target을 넣는다.

Q. 중간 결과가 비구조적이면 어떻게 돼?
A. Review Agent와 Fix Agent가 결과를 정확히 검증하거나 수정하기 어려워진다.

---

# 12. Stop Condition Overview

## 12.1 Stop Condition Definition

### [개념]

Stop Condition은 Agent Workflow가 언제 종료되는지 정의하는 기준이다.

Stop Condition은 완료, 실패, 보류, 사용자 확인 필요 상태를 구분한다.

필수 Stop Condition:

- Task Completed
- Review Passed
- Max Iteration Reached
- Missing Information
- User Confirmation Required
- Tool Failure
- Unsafe Action Detected

---

### [핵심]

- Workflow에는 명확한 종료 조건이 필요하다.
- 완료, 실패, 보류 상태를 구분한다.
- Review Passed 상태에서 Final Output을 생성한다.
- 정보 부족은 사용자 확인 필요로 종료할 수 있다.
- 위험 작업은 승인 대기로 중단한다.
- Max Iteration 도달 시 무한 반복을 멈춘다.
- 실패 상태를 성공으로 표시하지 않는다.

---

### [실무]

Stop Condition Template:

```md
## Stop Condition

### Completed

- Required output generated
- Review passed
- No blocking issue remains

### Blocked

- Missing critical information
- Tool unavailable
- User confirmation required

### Failed

- Invalid output repeated
- Unsafe action detected
- Max iteration reached without pass
```

상태 예시:

```text
completed
blocked
failed
user_confirmation_required
tool_failure
unsafe_action_detected
```

금지:

- 종료 조건 없는 Agent Loop
- 실패 상태를 성공으로 표시
- 불완전한 결과를 완료로 처리
- 위험 작업을 승인 없이 실행
- Max Iteration 없는 Review / Fix 반복

---

### [FAQ]

Q. Stop Condition이 뭐야?
A. Agent Workflow가 언제 완료, 실패, 보류, 사용자 확인 필요 상태로 끝나는지 정하는 종료 기준이다.

Q. Stop Condition이 왜 필요해?
A. Agent가 무한 반복하지 않고 안전하게 종료되도록 하기 위해 필요하다.

Q. Review가 Fail이면 종료해?
A. 수정 가능하면 Fix 단계로 이동하고, 수정 불가하거나 Max Iteration에 도달하면 blocked 또는 failed로 종료한다.

Q. 정보가 부족하면 어떻게 해?
A. Missing Information으로 표시하고 사용자 확인 필요 상태로 종료할 수 있다.

---

# 13. Failure Handling Overview

## 13.1 Failure Handling Definition

### [개념]

Failure Handling은 Agent Workflow에서 발생하는 실패를 분류하고 처리하는 구조이다.

Agent Workflow는 실패를 예외 상황이 아니라 정상적인 상태 중 하나로 다뤄야 한다.

주요 실패 유형:

- Missing Context
- Invalid Routing
- Handoff Failure
- Retrieval Failure
- Tool Failure
- Invalid Output
- Review Failure
- Fix Failure
- Timeout
- Unsafe Action

---

### [핵심]

- 실패 유형을 명확히 분류한다.
- 재시도 가능한 실패와 중단해야 하는 실패를 나눈다.
- Tool Failure는 구조화된 에러로 기록한다.
- Retrieval Failure는 숨기지 않는다.
- 안전 문제는 즉시 중단한다.
- 실패를 성공처럼 처리하지 않는다.
- 잘못된 결과를 기반으로 다음 Agent를 실행하지 않는다.

---

### [실무]

Failure Handling Flow:

```text
Failure Detected
→ Classify Failure
→ Identify Cause
→ Assess Impact
→ Retry / Fallback / Ask User / Stop
→ Update State
→ Continue or Stop
```

Failure Handling Template:

```md
## Failure Handling

### Failure Type

### Detected At

### Cause

### Impact

### Recovery Option

Retry / Fallback / Ask User / Stop

### State Update

### Next Step
```

Failure 처리 기준:

| Failure Type      | 처리                            |
| ----------------- | ------------------------------- |
| Missing Context   | Assumption 또는 사용자 확인     |
| Invalid Routing   | PM Agent 재분석 후 재라우팅     |
| Handoff Failure   | Handoff 재작성                  |
| Retrieval Failure | 검색 실패 표시, 제한적 답변     |
| Tool Failure      | 원인 기록, 재시도 또는 중단     |
| Invalid Output    | Output Format 재요청            |
| Review Failure    | Fix Agent로 전달                |
| Fix Failure       | Scope 재정의 또는 PM Escalation |
| Unsafe Action     | Stop 또는 Human Confirmation    |

---

### [FAQ]

Q. Failure Handling이 뭐야?
A. Agent Workflow에서 발생하는 실패를 분류하고 Retry, Fallback, 사용자 확인, Stop 중 하나로 처리하는 구조이다.

Q. Retrieval Failure는 어떻게 처리해?
A. 검색 실패를 표시하고, 필요한 경우 Assumption을 명시한 제한적 답변을 생성한다.

Q. Tool Failure는 어떻게 처리해?
A. 실패 원인과 영향을 기록하고, 재시도 가능 여부를 판단한 뒤 중단 또는 대체 경로를 선택한다.

Q. 실패한 결과를 다음 Agent에게 넘겨도 돼?
A. 안 된다. 잘못된 결과를 기반으로 다음 Agent를 실행하면 오류가 연쇄적으로 확산된다.

---

# 14. Workflow Pattern Overview

## 14.1 Basic Workflow Patterns

### [개념]

Workflow Pattern은 Agent Workflow에서 반복적으로 사용하는 실행 구조이다.

기본 Pattern:

- Sequential Workflow
- Router Workflow
- Review-Fix Workflow
- Planner-Executor Workflow
- Human Approval Workflow
- Tool-Using Workflow

Pattern은 작업 목적과 위험도에 맞게 선택한다.

---

### [핵심]

- Sequential Workflow는 단순하고 안정적이다.
- Router Workflow는 작업 종류별 Agent 분기에 적합하다.
- Review-Fix Workflow는 품질 검증에 적합하다.
- Planner-Executor Workflow는 복잡한 작업 분해에 적합하다.
- Human Approval Workflow는 위험 작업에 필요하다.
- Tool-Using Workflow는 외부 시스템 작업에 필요하다.
- 여러 Pattern은 조합 가능하다.

---

### [실무]

Pattern 예시:

```text
Sequential:
A → B → C → Final
```

```text
Router:
PM Agent → Backend Agent or Frontend Agent or DevOps Agent
```

```text
Review-Fix:
Draft → Review → Fix → Re-review → Final
```

```text
Planner-Executor:
PM Agent → Plan → Domain Agent Execution → Integration
```

```text
Human Approval:
Risk Detection → User Approval → Execute or Stop
```

```text
Tool-Using:
Need Tool → Select Tool → Execute Tool → Validate Result → Continue
```

Pattern 선택 기준:

| 상황                  | 권장 Pattern              |
| --------------------- | ------------------------- |
| 단순 순차 작업        | Sequential Workflow       |
| Domain 분기 필요      | Router Workflow           |
| 코드 품질 검증 필요   | Review-Fix Workflow       |
| 복잡한 작업 분해 필요 | Planner-Executor Workflow |
| 위험 작업 포함        | Human Approval Workflow   |
| 외부 시스템 호출      | Tool-Using Workflow       |

---

### [FAQ]

Q. Workflow Pattern이 뭐야?
A. Agent Workflow에서 자주 반복되는 실행 구조이다.

Q. 가장 기본 Pattern은?
A. Sequential Workflow와 Review-Fix Workflow이다.

Q. Router Workflow는 언제 써?
A. 작업 Domain에 따라 Backend, Frontend, DevOps, AI Agent 등으로 분기해야 할 때 사용한다.

Q. Pattern을 여러 개 섞어도 돼?
A. 가능하다. 예를 들어 Planner-Executor + Review-Fix + Tool-Using Workflow를 함께 사용할 수 있다.

---

# 15. Personal AI Development Team Overview

## 15.1 Personal AI Development Team Workflow

### [개념]

Personal AI Development Team은 개인 로컬 AI 서버에서 여러 Agent를 개발팀처럼 구성하는 구조이다.

사용자는 PM Agent에게만 요청하고, PM Agent가 필요한 Agent로 작업을 분해한다.

기본 구조:

```text
User
→ PM Agent
→ Backend Agent
→ Review Agent
→ Fix Agent
→ Final Output
```

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
→ Final Output
```

---

### [핵심]

- 사용자는 PM Agent에게만 요청한다.
- PM Agent가 작업을 분해하고 라우팅한다.
- 각 Agent는 Domain Rules와 RAG 문서를 참조한다.
- Review Agent가 최종 품질을 검증한다.
- 사용자는 최종 결과만 확인할 수 있다.
- 초기에는 순차 실행이 현실적이다.
- 병렬 Agent 실행은 복잡도와 자원 사용량이 증가한다.
- 로컬 LLM 환경에서는 속도와 메모리 제약을 고려한다.

---

### [실무]

초기 추천 구조:

```text
User
→ PM Agent
→ Backend Agent
→ Review Agent
→ Final Output
```

Backend Foundation 이후 확장 구조:

```text
User
→ PM Agent
→ SQL Agent
→ Backend Agent
→ Testing Agent
→ Review Agent
→ Fix Agent
→ Final Output
```

최종 목표 구조:

```text
User
→ PM Agent
→ SQL Agent
→ Backend Agent
→ Frontend Agent
→ DevOps Agent
→ AI/ML Agent
→ Review Agent
→ Fix Agent
→ Final Output
```

운영 기준:

- Agent 수보다 역할 명확성이 우선
- RAG 검색 범위는 Domain 기준으로 제한
- Agent별 Tool 권한 분리
- Review / Fix Loop는 최대 반복 횟수 설정
- Shared State에 결정 사항 기록
- 최종 결과만 사용자에게 제공 가능

---

### [FAQ]

Q. 개인 AI 개발팀 Workflow는 어떻게 구성해?
A. User가 PM Agent에게 요청하고, PM Agent가 SQL, Backend, Frontend, DevOps, AI, Review Agent로 작업을 나눈 뒤 최종 결과를 통합한다.

Q. 처음부터 많은 Agent를 만들어야 해?
A. 아니다. 초기에는 PM Agent, Backend Agent, Review Agent 중심의 순차 실행 구조가 현실적이다.

Q. 로컬 LLM에서도 Multi-Agent가 가능해?
A. 가능하다. 단, 속도와 메모리 제약 때문에 순차 실행과 역할 최소화가 적합하다.

Q. 사용자는 모든 Agent 결과를 봐야 해?
A. 아니다. 사용자는 최종 결과만 확인하고, 중간 결과는 Workflow 내부에서 검증용으로 사용할 수 있다.

---

# 16. Common Mistakes Overview

## 16.1 Agent Workflow Common Mistakes

### [개념]

Agent Workflow Common Mistakes는 Agent Workflow 설계에서 자주 발생하는 오류이다.

주요 오류는 역할 불명확, Handoff 누락, Shared State 부재, Stop Condition 부재, Review 기준 부재에서 발생한다.

---

### [핵심]

- Agent 역할이 겹침
- PM Agent가 구현까지 담당
- Handoff가 모호함
- Shared State가 없음
- 중간 결과가 비구조적임
- Stop Condition이 없음
- Review / Fix Loop가 무한 반복됨
- Review 기준이 모호함
- Tool 권한이 너무 넓음
- RAG 검색 범위가 너무 넓음
- 실패 처리 없이 성공으로 가정함
- 사용자 확인이 필요한 작업을 자동 실행함
- Agent 수를 너무 많이 늘림

---

### [실무]

대표 문제와 해결:

| 문제                          | 원인                  | 해결                                |
| ----------------------------- | --------------------- | ----------------------------------- |
| Agent가 엉뚱한 작업 수행      | Role / Task 불명확    | Role, Handoff, Expected Output 개선 |
| Workflow가 끝나지 않음        | Stop Condition 없음   | Max Iteration, Pass Condition 추가  |
| Agent 간 결과가 이어지지 않음 | Shared State 부재     | Intermediate Output Schema 통일     |
| Review가 쓸데없는 지적 반복   | Review Criteria 없음  | Severity Rule, Pass Condition 정의  |
| PM Agent가 모든 구현 수행     | 역할 분리 실패        | PM Agent를 라우팅 중심으로 제한     |
| Tool 실패를 성공 처리         | Failure Handling 없음 | Tool Result 검증 후 State 반영      |

주의:

- Agent 수를 늘리기 전에 Role과 Handoff를 먼저 정리한다.
- Review 기준을 먼저 만들고 Review Agent를 실행한다.
- 실패를 숨기지 않고 Workflow 개선 데이터로 사용한다.

---

### [FAQ]

Q. Agent Workflow에서 가장 흔한 실수는?
A. Agent 역할을 명확히 나누지 않고 PM Agent가 모든 일을 하게 만드는 것이다.

Q. Workflow가 끝나지 않는 이유는?
A. Stop Condition과 Max Iteration이 없거나 Review 기준이 계속 바뀌기 때문이다.

Q. Agent 간 결과가 이어지지 않는 이유는?
A. Handoff와 Intermediate Output 형식이 불명확하고 Shared State가 없기 때문이다.

Q. Agent 수를 많이 만들면 품질이 좋아져?
A. 항상 그렇지 않다. 역할과 책임이 불명확하면 Agent 수가 많을수록 복잡도와 실패 가능성이 증가한다.

---

# Retrieval Queries

### [FAQ]

Q. Agent Workflow가 뭐야?
A. 사용자 요청을 분석하고, 필요한 Agent가 순서대로 작업하며, 검토와 수정을 거쳐 최종 결과를 만드는 실행 흐름이다.

Q. Agent Workflow는 왜 필요해?
A. 복잡한 작업을 분해하고, 담당 Agent와 검증 단계를 분리해 결과 품질을 높이기 위해 필요하다.

Q. Agent Workflow 기본 흐름은?
A. User Request → Task Analysis → Agent Routing → Agent Execution → Review → Fix → Final Output 순서이다.

Q. Agent Workflow와 Prompt Chain 차이는?
A. Prompt Chain은 프롬프트 연결 중심이고, Agent Workflow는 역할, 상태, 검증, 종료 조건까지 포함한다.

Q. Single Agent Workflow는 언제 사용해?
A. 단순 질의응답, 짧은 코드 설명, 간단한 문서 요약처럼 역할 분리가 필요 없는 작업에 사용한다.

Q. Multi-Agent Workflow는 언제 사용해?
A. Backend, Frontend, SQL, DevOps, Review처럼 전문 영역을 나누는 것이 품질에 도움이 될 때 사용한다.

Q. PM Agent는 무슨 역할이야?
A. 사용자 요청을 분석하고 작업을 분해하며, 적절한 Agent에게 라우팅하고 최종 결과를 통합한다.

Q. Domain Agent는 무슨 역할이야?
A. Backend, Frontend, SQL, AI, DevOps처럼 특정 전문 영역의 작업을 수행한다.

Q. Review Agent는 왜 필요해?
A. Domain Agent의 결과를 요구사항과 Domain Rules 기준으로 검증하고 문제, 원인, 수정 방향을 제시하기 위해 필요하다.

Q. Fix Agent는 무슨 역할이야?
A. Review Agent가 발견한 문제를 기준으로 산출물을 수정한다.

Q. Task Decomposition은 뭐야?
A. 큰 사용자 요청을 실행 가능한 작은 작업으로 나누고 담당 Agent와 완료 기준을 정하는 과정이다.

Q. Agent Routing은 뭐야?
A. 작업 유형과 Domain에 따라 적절한 Agent를 선택하는 과정이다.

Q. Agent Routing 기준은?
A. Task Type, Domain, 필요한 전문성, 필요한 Tool, 우선순위, 위험도를 기준으로 한다.

Q. Handoff는 뭐야?
A. 한 Agent가 다음 Agent에게 Task, Context, Constraints, Expected Output을 전달하는 구조화된 작업 전달이다.

Q. 좋은 Handoff에는 뭐가 들어가야 해?
A. Source Agent, Target Agent, Task, Context, Input, Output Format, Constraints, Assumptions, Open Questions가 들어가야 한다.

Q. Shared State는 뭐야?
A. Workflow 전체에서 공유되는 요구사항, 결정 사항, 중간 결과, Review 결과, 현재 상태를 저장하는 구조이다.

Q. Context Passing은 뭐야?
A. 다음 Agent가 작업하는 데 필요한 Context만 Shared State에서 선별해 전달하는 과정이다.

Q. Intermediate Output은 뭐야?
A. Agent가 다음 단계에서 사용할 수 있도록 생성하는 구조화된 중간 산출물이다.

Q. Stop Condition은 왜 필요해?
A. Agent가 무한 반복하지 않고 완료, 실패, 보류, 사용자 확인 필요 상태를 명확히 판단하기 위해 필요하다.

Q. Failure Handling은 뭐야?
A. Agent Workflow에서 발생하는 실패를 분류하고 Retry, Fallback, 사용자 확인, Stop 중 하나로 처리하는 구조이다.

Q. Workflow Pattern에는 뭐가 있어?
A. Sequential Workflow, Router Workflow, Review-Fix Workflow, Planner-Executor Workflow, Human Approval Workflow, Tool-Using Workflow가 있다.

Q. 개인 AI 개발팀 Workflow는 어떻게 구성해?
A. User가 PM Agent에게 요청하고, PM Agent가 SQL, Backend, Frontend, DevOps, AI, Review Agent로 작업을 나눈 뒤 최종 결과를 통합한다.

Q. 처음부터 복잡한 Multi-Agent를 만들어야 해?
A. 아니다. 초기에는 순차 실행 기반의 단순 Workflow로 시작하고, 필요할 때 Agent와 Review Loop를 확장하는 것이 좋다.

Q. Agent가 무한 반복하면 어떻게 해?
A. Max Iteration, Severity 기준, Pass 조건, Stop Condition을 추가한다.

Q. Agent가 엉뚱한 일을 하면 어떻게 해?
A. Role과 책임 범위를 명확히 하고, Handoff Template과 Expected Output을 개선한다.

Q. PM Agent가 일을 너무 많이 하면 어떻게 해?
A. PM Agent를 분석, 분해, 라우팅 중심으로 제한하고 Domain Agent에게 명확히 Handoff한다.

Q. Agent 간 결과가 이어지지 않으면 어떻게 해?
A. Shared State를 사용하고, Intermediate Output과 Handoff 형식을 통일한다.

Q. Agent 수가 많으면 항상 좋은가?
A. 아니다. Agent가 많으면 Latency와 복잡도가 증가하므로 역할 명확성과 필요성을 기준으로 늘려야 한다.
