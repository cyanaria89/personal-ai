# Multi-Agent System Part07 - Router, Planner, and Executor

---

# 1. Router Planner Executor Core

## 1.1 Router Planner Executor Definition

### [개념]

Router, Planner, Executor는 Multi-Agent System에서 요청을 분류하고, 실행 계획을 만들고, 실제 작업을 수행하는 역할 구조이다.

Router는 어떤 Agent가 작업해야 하는지 선택한다.
Planner는 작업을 어떤 순서와 단위로 수행할지 계획한다.
Executor는 계획된 작업을 실행하고 결과를 반환한다.

Router, Planner, Executor는 Workflow Pattern 자체가 아니라 Workflow를 구성하는 기능적 역할이다.

기본 구조:

```text
User Request
→ Router
→ Planner
→ Executor
→ Result
→ PM Agent
```

PM Agent 중심 구조:

```text
User Request
→ PM Agent
→ Routing Decision
→ Plan
→ Agent Execution
→ Result Integration
```

---

### [핵심]

- Router는 요청을 분류하고 Target Agent를 선택한다.
- Planner는 작업 순서와 실행 단위를 만든다.
- Executor는 계획된 작업을 수행한다.
- Router, Planner, Executor는 Agent로 분리할 수도 있고 PM Agent 내부 기능으로 둘 수도 있다.
- 초기 개인 AI 개발팀에서는 PM Agent가 Router와 Planner 역할을 겸할 수 있다.
- Agent 수가 늘어나면 Router Agent 분리를 검토한다.
- 작업 복잡도가 높아지면 Planner Agent 분리를 검토한다.
- 자동 실행이 필요해지면 Executor Agent 분리를 검토한다.
- Router, Planner, Executor는 Shared State와 연결되어야 한다.
- Tool Permission과 Human Approval 기준을 반드시 따라야 한다.

---

### [실무]

2026 실무 기준에서 Router, Planner, Executor는 처음부터 독립 Agent로 만들 필요가 없다.

초기 구조:

```text
PM Agent
- Requirement Analysis
- Routing
- Planning
- Handoff
- Result Integration
```

확장 구조:

```text
PM Agent
→ Router Agent
→ Planner Agent
→ Executor Agent
→ Review Agent
→ PM Agent
```

분리 기준:

| 역할     | 분리 전                    | 분리 시점                            |
| -------- | -------------------------- | ------------------------------------ |
| Router   | PM Agent 내부 기능         | Agent 수가 많고 Routing 실패가 늘 때 |
| Planner  | PM Agent 내부 기능         | 복잡한 다단계 작업이 많을 때         |
| Executor | Specialist Agent 실행 흐름 | Tool 실행 자동화가 필요할 때         |

---

### [FAQ]

Q. Router, Planner, Executor는 뭐야?
A. Router는 Agent 선택, Planner는 실행 계획 수립, Executor는 계획 실행을 담당하는 역할이다.

Q. Router, Planner, Executor는 Workflow Pattern이야?
A. 아니다. Workflow Pattern을 구성하는 기능적 역할이다.

Q. 처음부터 Router Agent와 Planner Agent를 따로 만들어야 해?
A. 아니다. 초기에는 PM Agent가 Router와 Planner 역할을 겸하는 것이 안정적이다.

Q. 언제 Router Agent를 분리해?
A. Agent 수가 늘고 Routing 오류가 반복될 때 분리한다.

---

# 2. Router Agent

## 2.1 Router Agent Definition

### [개념]

Router Agent는 사용자 요청 또는 PM Agent의 작업 지시를 분석해 적절한 Target Agent를 선택하는 역할이다.

Router Agent의 목적은 요청의 Intent, Domain, Risk, Required Tool을 기준으로 작업을 올바른 Agent에게 보내는 것이다.

기본 구조:

```text
Input Request
→ Intent Classification
→ Domain Detection
→ Risk Check
→ Target Agent Selection
→ Routing Result
```

---

### [핵심]

- Router Agent는 요청 분류 담당이다.
- Intent를 분석한다.
- Domain을 감지한다.
- Target Agent를 선택한다.
- Routing Confidence를 표시한다.
- 복합 요청이면 PM Agent 또는 Planner Agent에게 분해를 요청한다.
- 위험 작업이면 Human Approval 필요 여부를 표시한다.
- RAG Scope와 Tool Permission이 Target Agent와 맞는지 확인한다.
- 낮은 Confidence에서 무리하게 Routing하지 않는다.
- Routing Result는 Shared State에 기록할 수 있다.

---

### [실무]

Router Agent Output Template:

```json
{
  "routingId": "ROUTE-001",
  "input": "리뷰 API 설계해줘",
  "intent": "backend_api_design",
  "detectedDomains": ["Backend", "API Design"],
  "targetAgent": "Backend Agent",
  "confidence": "high",
  "reason": "Spring Boot API 설계 요청이며 DB나 UI 작업은 명시되지 않음",
  "requiredRagScope": [
    "Spring Boot Domain Rules",
    "API Design Domain Rules",
    "Security Advanced Domain Rules"
  ],
  "toolPermissionCheck": "read_only",
  "approvalRequired": false,
  "fallback": null
}
```

Routing Confidence 기준:

| Confidence | 의미                 | 처리                             |
| ---------- | -------------------- | -------------------------------- |
| High       | Target Agent 명확    | Routing 수행                     |
| Medium     | 후보 Agent 일부 경합 | PM Agent 확인 또는 복합 Handoff  |
| Low        | Target 불명확        | PM Agent 재분석 또는 사용자 확인 |
| Conflict   | Domain 충돌          | Task Decomposition 필요          |

---

### [FAQ]

Q. Router Agent는 뭐야?
A. 요청의 Intent와 Domain을 분석해 어떤 Agent가 작업해야 하는지 선택하는 Agent다.

Q. Router Agent Output에는 뭐가 있어야 해?
A. Intent, Detected Domain, Target Agent, Confidence, Reason, RAG Scope, Tool Permission Check가 있어야 한다.

Q. Routing Confidence가 낮으면 어떻게 해?
A. 무리하게 실행하지 않고 PM Agent 재분석, 사용자 확인, Task Decomposition을 수행한다.

Q. Router Agent가 작업을 직접 수행해도 돼?
A. 아니다. Router Agent는 분류와 Agent 선택을 담당하고 실행은 Target Agent가 수행한다.

---

## 2.2 Routing Criteria

### [개념]

Routing Criteria는 Router Agent가 Target Agent를 선택할 때 사용하는 판단 기준이다.

Routing Criteria는 Intent, Domain, Keyword, Required Output, Required Tool, Risk Level, User Constraint를 함께 고려한다.

기본 구조:

```text
Intent
→ Domain
→ Required Output
→ Required Tool
→ Risk
→ Target Agent
```

---

### [핵심]

- Intent만으로 Routing하면 부족하다.
- Domain Detection이 필요하다.
- Required Output을 확인해야 한다.
- Required Tool을 확인해야 한다.
- 위험 작업 여부를 확인해야 한다.
- 복합 Domain 요청은 단일 Agent에게 보내지 않는다.
- User Constraint가 있으면 우선 반영한다.
- 현재 User Request가 오래된 Memory보다 우선이다.

---

### [실무]

Routing Criteria Matrix:

| 요청 단서                                        | Domain        | Target Agent        |
| ------------------------------------------------ | ------------- | ------------------- |
| table, schema, FK, index, query                  | SQL           | SQL Agent           |
| Java, Spring Boot, Controller, Service, API, JPA | Backend       | Backend Agent       |
| React, Component, State, Axios, Form, UI         | Frontend      | Frontend Agent      |
| Docker, Ubuntu, Linux, Deploy, Container, CI/CD  | DevOps        | DevOps Agent        |
| RAG, Prompt, Agent, Tool Calling, Embedding      | AI            | AI Agent            |
| 문서 작성, RAG 문서, Markdown, FAQ               | Documentation | Documentation Agent |
| 검수, 리뷰, 문제점 확인                          | Review        | Review Agent        |
| 수정, 보완, 반영                                 | Fix           | Fix Agent           |

Routing Rule 예시:

```json
{
  "rules": [
    {
      "condition": "request includes DB schema or query design",
      "targetAgent": "SQL Agent"
    },
    {
      "condition": "request includes Spring Boot API or Service design",
      "targetAgent": "Backend Agent"
    },
    {
      "condition": "request includes React UI or API integration",
      "targetAgent": "Frontend Agent"
    },
    {
      "condition": "request includes deploy, docker, linux, server operation",
      "targetAgent": "DevOps Agent"
    },
    {
      "condition": "request includes RAG document creation",
      "targetAgent": "Documentation Agent"
    }
  ]
}
```

---

### [FAQ]

Q. Routing Criteria가 뭐야?
A. Router Agent가 Target Agent를 선택할 때 사용하는 Intent, Domain, Output, Tool, Risk 기준이다.

Q. Keyword만 보고 Routing해도 돼?
A. 부족하다. Intent, Domain, Required Output, Risk까지 함께 봐야 한다.

Q. 복합 Domain 요청은 어떻게 처리해?
A. PM Agent 또는 Planner Agent가 Task Decomposition을 수행한 뒤 여러 Agent에게 나누어 전달한다.

Q. 위험 작업이 포함되면 어떻게 Routing해?
A. Target Agent를 선택하되 Human Approval 필요 여부를 함께 표시해야 한다.

---

## 2.3 Routing Failure

### [개념]

Routing Failure는 Router Agent가 잘못된 Target Agent를 선택하거나, 복합 요청을 분해하지 않거나, 낮은 Confidence 상태에서 잘못된 Routing을 수행하는 실패이다.

Routing Failure는 잘못된 RAG Scope, 잘못된 Tool Permission, 잘못된 Agent Output으로 이어진다.

기본 구조:

```text
Wrong Routing
→ Wrong Agent
→ Wrong RAG Scope
→ Wrong Output
→ Review Finding
```

---

### [핵심]

- Wrong Target Agent는 Output 실패로 이어진다.
- 복합 요청을 단일 Agent에게 보내면 누락이 발생한다.
- 낮은 Confidence에서 강행하면 오류 가능성이 높다.
- RAG Scope와 Agent Role이 불일치하면 Retrieval 품질이 떨어진다.
- Tool Permission이 맞지 않으면 위험 작업 가능성이 커진다.
- Routing Failure는 PM Agent가 재분석해야 한다.
- Review Agent는 Routing Failure를 Finding으로 기록할 수 있다.

---

### [실무]

Routing Failure 예시:

```md
## Routing Failure

### Failure Type

Wrong Target Agent

### Issue

React Component 수정 요청이 Backend Agent에게 전달됨

### Root Cause

Domain Detection에서 React / Component 키워드를 무시함

### Impact

Backend Agent가 Scope 밖 작업을 추측하거나 잘못된 Output을 생성할 수 있음

### Fix Direction

Target Agent를 Frontend Agent로 변경하고 RAG Scope를 React / API Integration으로 재설정

### Re-run Required

Yes
```

Routing Failure Prevention Checklist:

```md
## Routing Failure Prevention Checklist

- [ ] Intent가 명확한가?
- [ ] Primary Domain이 명확한가?
- [ ] 복합 Domain 요청인가?
- [ ] Target Agent가 Domain과 일치하는가?
- [ ] Routing Confidence가 표시되었는가?
- [ ] Confidence가 낮을 때 Fallback이 있는가?
- [ ] RAG Scope가 Target Agent와 일치하는가?
- [ ] Tool Permission이 Target Agent와 일치하는가?
```

---

### [FAQ]

Q. Routing Failure는 뭐야?
A. 잘못된 Target Agent 선택, 복합 요청 미분해, 낮은 Confidence 강행으로 발생하는 Routing 실패다.

Q. Routing Failure가 왜 위험해?
A. 잘못된 Agent가 잘못된 RAG Scope와 Tool Permission으로 작업해 Output 품질이 떨어지기 때문이다.

Q. Routing Failure는 어떻게 고쳐?
A. PM Agent가 Intent와 Domain을 재분석하고 Target Agent, RAG Scope, Handoff를 재설정해야 한다.

Q. Routing Failure를 줄이려면?
A. Routing Criteria, Confidence, Fallback, RAG Scope Check를 적용해야 한다.

---

# 3. Planner Agent

## 3.1 Planner Agent Definition

### [개념]

Planner Agent는 사용자 요청 또는 PM Agent Handoff를 실행 가능한 작업 단계로 나누고 순서를 정하는 역할이다.

Planner Agent는 무엇을 먼저 하고, 어떤 Agent에게 전달하며, 어떤 Output이 다음 Step의 Input이 되는지 계획한다.

Planner Agent는 직접 실행하지 않고 실행 계획을 만든다.

기본 구조:

```text
User Request
→ Task Decomposition
→ Step Ordering
→ Agent Assignment
→ Dependency Check
→ Plan Output
```

---

### [핵심]

- Planner Agent는 작업 계획 담당이다.
- 복합 요청을 작은 Task로 분해한다.
- Task 순서를 정한다.
- 각 Step의 Target Agent를 지정한다.
- Step 간 의존성을 확인한다.
- 각 Step의 Expected Output을 정의한다.
- Done Criteria를 정의한다.
- 위험 작업과 Approval 필요 여부를 표시한다.
- Planner Agent는 작업을 직접 실행하지 않는다.
- 실행은 Executor 또는 Specialist Agent가 담당한다.

---

### [실무]

Planner Agent Output Template:

```json
{
  "planId": "PLAN-001",
  "goal": "리뷰 기능 DB부터 Frontend까지 설계",
  "workflowType": "sequential",
  "steps": [
    {
      "step": 1,
      "agent": "SQL Agent",
      "task": "Design reviews table schema",
      "dependsOn": [],
      "expectedOutput": [
        "Table Design",
        "PK / FK",
        "Constraints",
        "Index Candidates"
      ],
      "doneCriteria": [
        "Review to User relationship defined",
        "Review to Festival relationship defined",
        "Rating constraint defined"
      ]
    },
    {
      "step": 2,
      "agent": "Backend Agent",
      "task": "Design review API contract",
      "dependsOn": ["SQL Agent Output"],
      "expectedOutput": [
        "API Contract",
        "DTO Design",
        "Service Method Plan",
        "Security Rules"
      ],
      "doneCriteria": ["CRUD endpoints defined", "Authorization rules defined"]
    },
    {
      "step": 3,
      "agent": "Frontend Agent",
      "task": "Design review UI integration",
      "dependsOn": ["Backend API Contract"],
      "expectedOutput": [
        "Component Structure",
        "State Design",
        "API Call Flow"
      ],
      "doneCriteria": [
        "Loading / Error / Empty state included",
        "API fields aligned"
      ]
    }
  ],
  "reviewRequired": true,
  "approvalRequired": false
}
```

계획 단계 기준:

```text
작업 분해
→ Agent 배정
→ 순서 결정
→ 의존성 확인
→ Output 정의
→ 완료 기준 정의
→ 위험 확인
```

---

### [FAQ]

Q. Planner Agent는 뭐야?
A. 복합 요청을 실행 가능한 단계로 분해하고 순서, 담당 Agent, 의존성, 완료 기준을 정하는 Agent다.

Q. Planner Agent가 직접 실행해?
A. 아니다. Planner Agent는 계획을 만들고 실행은 Executor 또는 Specialist Agent가 담당한다.

Q. Planner Agent는 언제 필요해?
A. DB, Backend, Frontend처럼 여러 단계와 의존성이 있는 복합 작업에서 필요하다.

Q. Planner Output에는 뭐가 있어야 해?
A. Goal, Steps, Target Agent, Dependency, Expected Output, Done Criteria, Review 필요 여부가 있어야 한다.

---

## 3.2 Plan Quality

### [개념]

Plan Quality는 Planner Agent가 만든 실행 계획이 요청을 수행하기에 충분히 명확하고 안정적인지 평가하는 기준이다.

좋은 Plan은 단계가 작고 명확하며, 순서와 의존성이 자연스럽고, 각 Step의 Output과 Done Criteria가 분명하다.

기본 구조:

```text
Plan
→ Step Clarity
→ Dependency Check
→ Agent Assignment Check
→ Done Criteria Check
→ Risk Check
```

---

### [핵심]

- Plan의 Step은 실행 가능한 단위여야 한다.
- Step 순서는 의존성과 맞아야 한다.
- Target Agent가 적절해야 한다.
- 각 Step의 Expected Output이 있어야 한다.
- Done Criteria가 있어야 한다.
- Review 필요 여부가 표시되어야 한다.
- Approval 필요 여부가 표시되어야 한다.
- Open Questions가 표시되어야 한다.
- 너무 큰 Step은 분해해야 한다.
- 너무 작은 Step은 불필요한 비용을 만든다.

---

### [실무]

Plan Quality Checklist:

```md
## Plan Quality Checklist

- [ ] Goal이 명확한가?
- [ ] Step이 실행 가능한 단위인가?
- [ ] Step 순서가 의존성과 맞는가?
- [ ] 각 Step의 Target Agent가 적절한가?
- [ ] 각 Step의 Expected Output이 명확한가?
- [ ] 각 Step의 Done Criteria가 있는가?
- [ ] 중간 Output이 다음 Step Input으로 연결되는가?
- [ ] Review가 필요한 Step이 표시되었는가?
- [ ] Approval이 필요한 Step이 표시되었는가?
- [ ] Open Questions가 표시되었는가?
```

나쁜 Plan 예시:

```text
1. 리뷰 기능 전체 구현
2. 검토
```

문제:

- Step이 너무 큼
- Agent 배정 없음
- 의존성 없음
- Expected Output 없음
- Done Criteria 없음

좋은 Plan 예시:

```text
1. SQL Agent: reviews table 설계
2. Backend Agent: Review API Contract 설계
3. Frontend Agent: Review UI/API 연동 설계
4. Review Agent: DB/API/UI 일관성 검토
5. Fix Agent: Review Findings 반영
```

---

### [FAQ]

Q. Plan Quality가 뭐야?
A. 실행 계획이 요청 수행에 충분히 명확하고 안정적인지 평가하는 기준이다.

Q. 좋은 Plan의 조건은?
A. Step이 작고 명확하며, 의존성, Target Agent, Expected Output, Done Criteria가 있어야 한다.

Q. Step이 너무 크면 왜 문제야?
A. Agent가 한 번에 너무 많은 작업을 처리하면서 요구사항 누락과 Scope 위반이 발생할 수 있다.

Q. Plan Quality는 누가 검토해?
A. PM Agent 또는 Review Agent가 검토할 수 있다.

---

## 3.3 Plan Revision

### [개념]

Plan Revision은 실행 중 실패, Missing Context, Approval 필요, Scope 변경, User Request 변경이 발생했을 때 기존 계획을 수정하는 작업이다.

Plan은 고정된 것이 아니라 실행 결과에 따라 안전하게 수정될 수 있어야 한다.

기본 구조:

```text
Execution Result
→ Blocked / Failed / Changed Requirement
→ Plan Revision
→ Updated Plan
→ Continue
```

---

### [핵심]

- Plan Revision은 계획 수정이다.
- 중간 Step이 Blocked이면 Plan Revision이 필요하다.
- Missing Context가 있으면 필요한 Context 확보 Step을 추가한다.
- 위험 작업이 생기면 Approval Step을 추가한다.
- User Request가 변경되면 Plan을 다시 검토한다.
- Step 순서를 변경할 수 있다.
- Target Agent를 변경할 수 있다.
- 기존 완료 결과를 무효화할 수도 있다.
- Plan 변경 이유를 기록해야 한다.
- Plan Revision은 PM Agent가 승인하는 것이 안전하다.

---

### [실무]

Plan Revision Template:

```json
{
  "planId": "PLAN-001",
  "revisionId": "REV-001",
  "reason": "Frontend Agent blocked because Backend API response fields are missing",
  "change": [
    {
      "action": "insert_step",
      "step": "Backend Agent must provide ReviewResDto field list before Frontend step"
    },
    {
      "action": "pause_step",
      "step": "Frontend Agent execution"
    }
  ],
  "updatedPlanStatus": "in_progress",
  "approvalRequired": false
}
```

Plan Revision 발생 조건:

| 조건                    | 처리                             |
| ----------------------- | -------------------------------- |
| Missing Context         | Context 확보 Step 추가           |
| Agent Failure           | 해당 Step 재실행 또는 Agent 변경 |
| Handoff Failure         | Handoff 수정 후 재실행           |
| Tool Permission Issue   | Approval Step 추가               |
| User Request 변경       | Plan 재검토                      |
| Critical Review Finding | Fix Step 추가                    |
| Scope 변경              | PM Agent Decision 필요           |

---

### [FAQ]

Q. Plan Revision이 뭐야?
A. 실행 중 실패나 변경이 발생했을 때 기존 실행 계획을 수정하는 작업이다.

Q. 언제 Plan Revision이 필요해?
A. Missing Context, Agent Failure, Tool Permission 문제, User Request 변경, Critical Finding이 있을 때 필요하다.

Q. Plan Revision은 누가 승인해?
A. 일반적으로 PM Agent가 승인하는 것이 안전하다.

Q. Plan Revision 기록에는 뭐가 있어야 해?
A. 변경 이유, 변경 내용, 영향 Step, Approval 필요 여부가 있어야 한다.

---

# 4. Executor Agent

## 4.1 Executor Agent Definition

### [개념]

Executor Agent는 Planner가 만든 Step 또는 PM Agent가 지정한 작업을 실제로 실행하는 역할이다.

Executor Agent는 직접 작업을 수행하거나 Specialist Agent를 호출해 실행 결과를 수집할 수 있다.

Executor의 핵심은 계획된 범위 안에서 실행하고, 실행 결과와 실패 상태를 정확히 기록하는 것이다.

기본 구조:

```text
Plan Step
→ Permission Check
→ Execute
→ Result Record
→ Status Update
```

---

### [핵심]

- Executor Agent는 실행 담당이다.
- Plan Step 기준으로 작업한다.
- 실행 전 Tool Permission을 확인한다.
- 위험 작업은 Human Approval 전 실행하지 않는다.
- 실행 결과를 기록한다.
- 실패 상태를 숨기지 않는다.
- Partial Result를 표시한다.
- Scope 밖 작업은 PM Agent에게 반환한다.
- Executor는 계획을 임의로 크게 변경하지 않는다.
- 필요한 경우 Plan Revision을 요청한다.

---

### [실무]

Executor Agent Output Template:

```json
{
  "executionId": "EXEC-001",
  "planId": "PLAN-001",
  "step": 2,
  "agent": "Backend Agent",
  "task": "Design review API contract",
  "status": "completed",
  "resultSummary": [
    "POST /reviews",
    "GET /festivals/{festivalId}/reviews",
    "PATCH /reviews/{reviewId}",
    "DELETE /reviews/{reviewId}"
  ],
  "decisions": ["Review author can update/delete own review"],
  "assumptions": ["Authenticated user is resolved from SecurityContext"],
  "risks": ["Duplicate review policy is not confirmed"],
  "openQuestions": [
    "Can one user write multiple reviews for the same festival?"
  ],
  "nextStep": "Frontend Agent"
}
```

Execution Status:

| Status            | 의미                 |
| ----------------- | -------------------- |
| completed         | 정상 완료            |
| partial           | 일부 완료            |
| blocked           | 필수 Context 부족    |
| failed            | 실행 실패            |
| skipped           | 조건상 실행하지 않음 |
| approval_required | 승인 필요            |
| cancelled         | 취소됨               |

---

### [FAQ]

Q. Executor Agent는 뭐야?
A. Planner가 만든 Step 또는 PM Agent가 지정한 작업을 실제로 실행하고 결과를 기록하는 Agent다.

Q. Executor Agent가 Plan을 마음대로 바꿔도 돼?
A. 안 된다. 필요한 경우 Plan Revision을 요청해야 한다.

Q. Executor Agent가 위험 Tool을 실행할 수 있어?
A. Human Approval이 필요한 작업은 승인 전 실행하면 안 된다.

Q. Executor Output에는 뭐가 있어야 해?
A. Execution ID, Plan ID, Step, Agent, Task, Status, Result Summary, Decisions, Risks, Open Questions가 있어야 한다.

---

## 4.2 Execution Control

### [개념]

Execution Control은 Executor Agent가 작업을 실행할 때 Scope, Permission, Status, Failure, Retry를 관리하는 기준이다.

Execution Control이 없으면 Agent가 계획 밖 작업을 실행하거나, 실패 상태를 숨기거나, 위험 Tool을 승인 없이 실행할 수 있다.

기본 구조:

```text
Execution Request
→ Scope Check
→ Permission Check
→ Context Check
→ Execute
→ Result / Failure
```

---

### [핵심]

- 실행 전 Scope를 확인한다.
- 실행 전 Tool Permission을 확인한다.
- 실행 전 Required Context를 확인한다.
- 실행 중 실패를 기록한다.
- 실행 결과를 Shared State에 반영한다.
- 위험 작업은 승인 상태를 확인한다.
- Retry 여부를 판단한다.
- Retry가 위험하면 중단한다.
- Partial Result와 Failed Result를 구분한다.
- 실행 후 Review 필요 여부를 표시한다.

---

### [실무]

Execution Control Checklist:

```md
## Execution Control Checklist

- [ ] Plan Step이 명확한가?
- [ ] Task가 Executor Scope 안인가?
- [ ] Required Context가 충분한가?
- [ ] Tool Permission이 허용되는가?
- [ ] Dangerous Tool이 포함되는가?
- [ ] Approval State가 필요한가?
- [ ] 실패 시 Retry 가능한가?
- [ ] 결과를 Shared State에 기록할 수 있는가?
- [ ] Review가 필요한가?
```

Execution Failure Example:

```md
## Execution Failure

### Execution ID

EXEC-003

### Step

Frontend Agent - Review UI Integration

### Status

Blocked

### Reason

Backend API Response Field가 확정되지 않음

### Required Context

- ReviewResDto field list
- Slice response format

### Suggested Action

Plan Revision을 통해 Backend Agent Step을 보강한 뒤 Frontend Step 재실행
```

---

### [FAQ]

Q. Execution Control이 뭐야?
A. Executor Agent가 작업 실행 전후로 Scope, Permission, Context, Status, Failure를 관리하는 기준이다.

Q. 실행 전 반드시 확인할 것은?
A. Plan Step, Scope, Required Context, Tool Permission, Approval 필요 여부다.

Q. 실행 중 필수 Context가 없으면?
A. Blocked 상태를 반환하고 Plan Revision 또는 PM Agent 보강을 요청해야 한다.

Q. 실행 결과는 어디에 기록해?
A. Shared State의 Agent Output, Tool Result, Execution Result에 기록한다.

---

# 5. Router Planner Executor Coordination

## 5.1 Coordination Flow

### [개념]

Router, Planner, Executor Coordination은 요청 분류, 계획 수립, 실행 결과 기록이 서로 연결되는 흐름이다.

Router가 Target Agent를 잘못 고르면 Planner의 계획도 틀어지고, Executor가 잘못된 작업을 실행할 수 있다.

기본 구조:

```text
Router Decision
→ Planner Plan
→ Executor Execution
→ Shared State Update
→ Review
```

---

### [핵심]

- Router 결과는 Planner 입력이 된다.
- Planner 결과는 Executor 입력이 된다.
- Executor 결과는 Shared State에 반영된다.
- Shared State는 다음 Routing과 Planning에 사용된다.
- 각 단계의 Status를 기록해야 한다.
- Routing Confidence가 낮으면 Planning을 강행하지 않는다.
- Plan이 불완전하면 Execution을 강행하지 않는다.
- Execution이 실패하면 Plan Revision이 필요할 수 있다.
- PM Agent는 전체 조율과 최종 결정을 담당한다.

---

### [실무]

Coordination State 예시:

```json
{
  "workflowId": "WF-001",
  "router": {
    "status": "completed",
    "targetAgents": ["SQL Agent", "Backend Agent", "Frontend Agent"],
    "confidence": "high"
  },
  "planner": {
    "status": "completed",
    "planId": "PLAN-001",
    "steps": [
      "SQL schema design",
      "Backend API design",
      "Frontend UI integration"
    ]
  },
  "executor": {
    "status": "in_progress",
    "currentStep": "Backend API design",
    "completedSteps": ["SQL schema design"]
  },
  "reviewRequired": true
}
```

Coordination 원칙:

```text
Routing이 불확실하면 Plan 생성 보류
Plan이 불완전하면 Execution 보류
Execution이 실패하면 Plan Revision
Critical Review Finding이 있으면 Fix 또는 Re-plan
```

---

### [FAQ]

Q. Router Planner Executor Coordination이 뭐야?
A. Router의 Agent 선택, Planner의 실행 계획, Executor의 실행 결과를 연결해 관리하는 흐름이다.

Q. Router 결과가 틀리면 어떻게 돼?
A. Planner가 잘못된 Agent 기준으로 계획을 만들고 Executor가 잘못된 작업을 실행할 수 있다.

Q. Plan이 불완전하면 실행해도 돼?
A. 안 된다. Expected Output, Dependency, Done Criteria가 부족하면 보강 후 실행해야 한다.

Q. PM Agent는 이 흐름에서 무엇을 해?
A. 전체 조율, 최종 결정, Shared State 관리, 결과 통합을 담당한다.

---

## 5.2 State Integration

### [개념]

State Integration은 Router, Planner, Executor의 결과를 Shared State에 반영하는 작업이다.

State Integration이 없으면 각 단계의 결정과 실행 결과가 분리되어 다음 Agent가 최신 정보를 사용할 수 없다.

기본 구조:

```text
Routing Result
→ Plan Result
→ Execution Result
→ Shared State
```

---

### [핵심]

- Routing Result를 Shared State에 기록한다.
- Plan Result를 Shared State에 기록한다.
- Execution Result를 Shared State에 기록한다.
- Current Step을 갱신한다.
- Status를 갱신한다.
- Decisions를 기록한다.
- Risks와 Open Questions를 기록한다.
- 실패 상태를 숨기지 않는다.
- Review Agent가 참조할 수 있게 구조화한다.

---

### [실무]

State Integration Template:

```json
{
  "workflowId": "WF-001",
  "routingResult": {
    "targetAgents": ["SQL Agent", "Backend Agent", "Frontend Agent"],
    "confidence": "high"
  },
  "planResult": {
    "planId": "PLAN-001",
    "workflowType": "sequential",
    "steps": [
      {
        "step": 1,
        "agent": "SQL Agent",
        "status": "completed"
      },
      {
        "step": 2,
        "agent": "Backend Agent",
        "status": "in_progress"
      }
    ]
  },
  "executionResults": {
    "SQL Agent": {
      "status": "completed",
      "summary": "reviews table design completed"
    }
  },
  "currentStep": "Backend Agent",
  "status": "in_progress",
  "openQuestions": []
}
```

State Integration 실패 예시:

```md
## State Integration Failure

### Issue

Planner는 Frontend Agent Step을 생성했지만 Shared State currentStep에 반영되지 않음

### Impact

Executor가 다음 실행 대상을 찾지 못함

### Fix Direction

Plan Result를 Shared State에 반영하고 currentStep을 갱신
```

---

### [FAQ]

Q. State Integration이 뭐야?
A. Router, Planner, Executor의 결과를 Shared State에 반영하는 작업이다.

Q. State Integration이 왜 필요해?
A. 다음 Agent가 최신 Routing, Plan, Execution 결과를 기준으로 작업할 수 있게 하기 위해서다.

Q. State Integration에 기록할 것은?
A. Routing Result, Plan Result, Execution Result, Current Step, Status, Decisions, Risks, Open Questions다.

Q. State Integration이 누락되면?
A. 다음 Agent가 최신 상태를 모르고 잘못된 Step을 실행할 수 있다.

---

# 6. Router Planner Executor Failure Handling

## 6.1 Router Planner Executor Failure Cases

### [개념]

Router, Planner, Executor Failure는 요청 분류, 계획 수립, 실행 단계에서 발생하는 실패 유형이다.

이 실패는 Workflow 전체 실패로 이어질 수 있으므로 각 단계별로 Root Cause를 분리해 분석해야 한다.

주요 실패 구조:

```text
Routing Failure
→ Wrong Plan
→ Wrong Execution
→ Final Output Failure
```

---

### [핵심]

- Router Failure는 잘못된 Target Agent 선택이다.
- Planner Failure는 잘못된 작업 분해 또는 순서 오류이다.
- Executor Failure는 실행 실패 또는 상태 기록 실패이다.
- Routing Confidence가 낮으면 Planning을 보류한다.
- Plan Quality가 낮으면 Execution을 보류한다.
- Execution Failure는 Plan Revision으로 이어질 수 있다.
- 단계별 Failure Type을 분리해야 한다.
- PM Agent가 최종 Recovery를 조율한다.

---

### [실무]

Failure Case Matrix:

| Failure Type             | Symptom                    | Handling               |
| ------------------------ | -------------------------- | ---------------------- |
| Wrong Target Agent       | 엉뚱한 Agent가 작업        | Routing 재수행         |
| Low Confidence Routing   | Target 불명확              | PM Agent 재분석        |
| Missing Step             | 필요한 Agent Step 누락     | Plan Revision          |
| Wrong Step Order         | 의존성 순서 오류           | Plan 순서 수정         |
| No Done Criteria         | 완료 판단 불가             | Plan 보강              |
| Executor Scope Violation | 실행 Agent가 Scope 밖 작업 | 실행 중단              |
| Permission Failure       | Tool 권한 없음             | Approval 또는 Deny     |
| Missing Execution Result | 결과 기록 없음             | State Integration 보강 |

Failure Record 예시:

```md
## Router Planner Executor Failure

### Failure Type

Wrong Step Order

### Symptom

Frontend Agent가 Backend API Contract 없이 먼저 실행됨

### Root Cause

Planner가 Step Dependency를 확인하지 않음

### Impact

Frontend State와 API Call Flow가 추측 기반으로 작성됨

### Immediate Fix

Backend Agent Step을 Frontend Agent Step보다 먼저 배치

### Prevention Rule

Planner는 각 Step의 dependsOn 필드를 필수로 작성한다
```

---

### [FAQ]

Q. Router Planner Executor Failure는 뭐야?
A. 요청 분류, 계획 수립, 실행 단계에서 발생하는 실패 유형이다.

Q. Router Failure와 Planner Failure는 어떻게 달라?
A. Router Failure는 Target Agent 선택 문제이고, Planner Failure는 Step 분해와 순서 문제다.

Q. Executor Failure는 무엇을 포함해?
A. 실행 실패, Scope 위반, Permission 문제, Execution Result 누락을 포함한다.

Q. 이 Failure는 누가 복구해?
A. PM Agent가 Routing 재수행, Plan Revision, Execution 재시도 여부를 결정한다.

---

## 6.2 Recovery Strategy

### [개념]

Recovery Strategy는 Router, Planner, Executor 단계에서 실패가 발생했을 때 Workflow를 복구하는 방법이다.

Recovery는 무조건 재실행이 아니라, 실패 단계에 따라 Routing 재수행, Plan Revision, Execution Retry, Human Approval, Workflow 중단을 선택한다.

기본 구조:

```text
Failure Detection
→ Failure Type
→ Recovery Strategy
→ State Update
→ Re-run / Stop
```

---

### [핵심]

- 실패 단계에 따라 Recovery 방법이 다르다.
- Router 실패는 재분류한다.
- Planner 실패는 Plan Revision을 수행한다.
- Executor 실패는 Retry 또는 Blocked 처리한다.
- Tool Permission 실패는 Approval Request로 전환한다.
- Missing Context는 Required Context 확보 후 재실행한다.
- Critical Failure는 Workflow를 중단할 수 있다.
- Recovery 결과를 Shared State에 기록한다.

---

### [실무]

Recovery Strategy Matrix:

| Failure                  | Recovery                         |
| ------------------------ | -------------------------------- |
| Wrong Target Agent       | Routing 재수행                   |
| Low Confidence           | PM Agent 재분석 또는 사용자 확인 |
| Missing Step             | Plan Revision                    |
| Wrong Step Order         | Plan Revision                    |
| Missing Context          | Context 확보 Step 추가           |
| Permission Denied        | Approval Request 또는 Deny       |
| Tool Failure             | Retry / Fallback / Stop          |
| Executor Scope Violation | Execution 중단 후 PM Agent 반환  |
| Critical Review Finding  | Fix Step 추가 또는 Re-plan       |
| Repeated Failure         | Workflow 중단 후 Troubleshooting |

Recovery Record Template:

```md
## Recovery Record

### Failure

Wrong Step Order

### Recovery Strategy

Plan Revision

### Action

Backend API Contract Step을 Frontend UI Integration Step 이전으로 이동

### Updated State

currentStep: Backend Agent

### Re-run Required

Yes

### Re-review Required

Yes
```

---

### [FAQ]

Q. Recovery Strategy가 뭐야?
A. Router, Planner, Executor 단계에서 실패가 발생했을 때 Workflow를 복구하는 방법이다.

Q. 모든 실패는 재실행하면 돼?
A. 아니다. 실패 유형에 따라 Routing 재수행, Plan Revision, Approval Request, 중단을 선택해야 한다.

Q. Missing Context는 어떻게 복구해?
A. Required Context 확보 Step을 추가한 뒤 해당 Step을 재실행한다.

Q. 반복 실패가 발생하면?
A. Workflow를 중단하고 Troubleshooting Report를 작성해야 한다.

---

# 7. Personal AI Project Application

## 7.1 Initial Application Strategy

### [개념]

Initial Application Strategy는 개인 AI 개발팀에서 Router, Planner, Executor를 처음 적용하는 방식이다.

처음부터 Router Agent, Planner Agent, Executor Agent를 모두 분리하는 것보다 PM Agent 내부 기능으로 시작하고, 필요할 때 분리하는 것이 안정적이다.

기본 구조:

```text
초기
PM Agent = Router + Planner + Coordinator

확장
PM Agent + Router Agent + Planner Agent + Executor Agent
```

---

### [핵심]

- 초기에는 PM Agent가 Router 역할을 겸한다.
- 초기에는 PM Agent가 Planner 역할을 겸한다.
- Executor는 각 Specialist Agent 실행으로 대체할 수 있다.
- 독립 Executor Agent는 Tool 자동화 이후 검토한다.
- 먼저 Handoff와 Shared State를 안정화한다.
- 이후 Routing 실패가 늘면 Router Agent를 분리한다.
- 복잡한 계획 실패가 늘면 Planner Agent를 분리한다.
- 자동 실행이 필요하면 Executor Agent를 분리한다.

---

### [실무]

개인 AI 개발팀 초기 적용:

```text
User
→ PM Agent
   - 요청 분석
   - Routing
   - 간단한 Planning
   - Handoff 생성
→ Specialist Agent
→ Review Agent
→ Fix Agent
→ PM Agent Final Output
```

확장 판단 기준:

```md
## Separation Decision Checklist

### Router Agent 분리

- [ ] Agent 수가 6개 이상인가?
- [ ] Routing Failure가 반복되는가?
- [ ] Domain Detection 기준이 복잡한가?

### Planner Agent 분리

- [ ] 다단계 작업이 많아졌는가?
- [ ] Step 순서 오류가 반복되는가?
- [ ] Plan Revision이 자주 필요한가?

### Executor Agent 분리

- [ ] Tool 실행 자동화가 필요한가?
- [ ] Step별 실행 상태 관리가 필요한가?
- [ ] Human Approval과 Tool Result 기록이 복잡한가?
```

---

### [FAQ]

Q. 개인 AI 프로젝트에서 Router, Planner, Executor를 처음부터 분리해야 해?
A. 아니다. 초기에는 PM Agent 내부 기능으로 두고 필요해질 때 분리하는 것이 좋다.

Q. Router Agent는 언제 분리해?
A. Agent 수가 늘고 Routing Failure가 반복될 때 분리한다.

Q. Planner Agent는 언제 분리해?
A. 복잡한 다단계 작업이 많아지고 Step 순서 오류가 반복될 때 분리한다.

Q. Executor Agent는 언제 분리해?
A. Tool 실행 자동화와 Step별 실행 상태 관리가 필요할 때 분리한다.

---

# 8. Router Planner Executor Checklist

## 8.1 Router Checklist

### [개념]

Router Checklist는 Router Agent 또는 PM Agent의 Routing 기능이 요청을 올바른 Agent에게 전달하는지 검수하는 기준이다.

---

### [핵심]

- Intent를 확인한다.
- Domain을 확인한다.
- Target Agent를 확인한다.
- 복합 Domain 여부를 확인한다.
- Routing Confidence를 표시한다.
- RAG Scope 일치를 확인한다.
- Tool Permission 일치를 확인한다.
- Fallback을 확인한다.

---

### [실무]

Router Checklist:

```md
## Router Checklist

- [ ] User Intent가 명확한가?
- [ ] Primary Domain이 명확한가?
- [ ] Secondary Domain이 있는가?
- [ ] 복합 요청이면 Task Decomposition이 필요한가?
- [ ] Target Agent가 Domain과 일치하는가?
- [ ] Routing Confidence가 표시되었는가?
- [ ] Confidence가 Low일 때 Fallback이 있는가?
- [ ] RAG Scope가 Target Agent와 일치하는가?
- [ ] Tool Permission이 Target Agent와 일치하는가?
- [ ] 위험 작업이면 Approval 필요 여부가 표시되었는가?
```

---

### [FAQ]

Q. Router Checklist가 뭐야?
A. 요청이 올바른 Agent에게 전달되는지 검수하는 기준이다.

Q. Router Checklist에서 가장 중요한 항목은?
A. Intent, Domain, Target Agent, Confidence, RAG Scope, Tool Permission이다.

Q. 복합 요청이면 Router가 바로 하나의 Agent를 선택해도 돼?
A. 아니다. Task Decomposition 또는 Planner Agent로 넘겨야 한다.

Q. 위험 작업이면 Routing 단계에서 무엇을 표시해야 해?
A. Human Approval 필요 여부를 표시해야 한다.

---

## 8.2 Planner Checklist

### [개념]

Planner Checklist는 Planner Agent 또는 PM Agent의 Planning 기능이 실행 가능한 계획을 만들었는지 검수하는 기준이다.

---

### [핵심]

- Goal을 확인한다.
- Step 단위를 확인한다.
- Step 순서를 확인한다.
- Dependency를 확인한다.
- Target Agent를 확인한다.
- Expected Output을 확인한다.
- Done Criteria를 확인한다.
- Approval 필요 여부를 확인한다.
- Review 필요 여부를 확인한다.

---

### [실무]

Planner Checklist:

```md
## Planner Checklist

- [ ] Goal이 명확한가?
- [ ] Step이 실행 가능한 크기인가?
- [ ] Step 순서가 의존성과 일치하는가?
- [ ] 각 Step의 Target Agent가 명확한가?
- [ ] 각 Step의 dependsOn이 명확한가?
- [ ] 각 Step의 Expected Output이 있는가?
- [ ] 각 Step의 Done Criteria가 있는가?
- [ ] Missing Context가 있는가?
- [ ] Approval Required Step이 표시되었는가?
- [ ] Review Required Step이 표시되었는가?
```

---

### [FAQ]

Q. Planner Checklist가 뭐야?
A. 실행 계획이 명확하고 실행 가능한지 검수하는 기준이다.

Q. Planner Checklist에서 가장 중요한 항목은?
A. Step, Dependency, Target Agent, Expected Output, Done Criteria다.

Q. Step 순서가 틀리면 어떻게 해?
A. Plan Revision을 수행해야 한다.

Q. Missing Context가 있으면 어떻게 해?
A. Context 확보 Step을 추가하거나 해당 Step을 Blocked로 표시한다.

---

## 8.3 Executor Checklist

### [개념]

Executor Checklist는 Executor Agent 또는 Specialist Agent가 계획된 작업을 안전하게 실행하고 결과를 기록했는지 검수하는 기준이다.

---

### [핵심]

- Plan Step을 확인한다.
- Scope를 확인한다.
- Required Context를 확인한다.
- Tool Permission을 확인한다.
- Approval 필요 여부를 확인한다.
- Execution Status를 기록한다.
- Result Summary를 기록한다.
- Failure Reason을 기록한다.
- Shared State 업데이트 필요 여부를 확인한다.

---

### [실무]

Executor Checklist:

```md
## Executor Checklist

- [ ] Plan Step이 명확한가?
- [ ] Task가 Executor Scope 안인가?
- [ ] Required Context가 충분한가?
- [ ] Tool Permission이 허용되는가?
- [ ] Dangerous Tool이 포함되는가?
- [ ] Approval State가 approved인가?
- [ ] Execution Status가 기록되었는가?
- [ ] Result Summary가 작성되었는가?
- [ ] Failure가 숨겨지지 않았는가?
- [ ] Decisions / Risks / Open Questions가 기록되었는가?
- [ ] Shared State 업데이트가 필요한가?
- [ ] Review가 필요한가?
```

---

### [FAQ]

Q. Executor Checklist가 뭐야?
A. 계획된 작업을 안전하게 실행하고 결과를 기록했는지 검수하는 기준이다.

Q. Executor Checklist에서 가장 중요한 항목은?
A. Plan Step, Scope, Required Context, Tool Permission, Status, Result Summary다.

Q. 실행 실패는 숨겨도 돼?
A. 안 된다. Failure Reason과 Suggested Action을 기록해야 한다.

Q. 실행 결과는 어디에 반영해?
A. Shared State의 Execution Result, Agent Output, Tool Result에 반영한다.

---

# Retrieval Queries

### [FAQ]

Q. Router Planner Executor는 뭐야?
A. Router는 Agent 선택, Planner는 실행 계획 수립, Executor는 계획 실행을 담당하는 Multi-Agent System의 기능적 역할이다.

Q. Router Planner Executor는 Workflow Pattern이야?
A. 아니다. Workflow Pattern을 구성하는 기능적 역할이다.

Q. 처음부터 Router Agent와 Planner Agent를 따로 만들어야 해?
A. 아니다. 초기에는 PM Agent가 Router와 Planner 역할을 겸하는 것이 안정적이다.

Q. Router Agent는 뭐야?
A. 요청의 Intent와 Domain을 분석해 어떤 Agent가 작업해야 하는지 선택하는 Agent다.

Q. Router Agent Output에는 뭐가 있어야 해?
A. Intent, Detected Domain, Target Agent, Confidence, Reason, RAG Scope, Tool Permission Check가 있어야 한다.

Q. Routing Confidence가 낮으면 어떻게 해?
A. 무리하게 실행하지 않고 PM Agent 재분석, 사용자 확인, Task Decomposition을 수행한다.

Q. Routing Criteria가 뭐야?
A. Router Agent가 Target Agent를 선택할 때 사용하는 Intent, Domain, Output, Tool, Risk 기준이다.

Q. 복합 Domain 요청은 어떻게 처리해?
A. PM Agent 또는 Planner Agent가 Task Decomposition을 수행한 뒤 여러 Agent에게 나누어 전달한다.

Q. Routing Failure는 뭐야?
A. 잘못된 Target Agent 선택, 복합 요청 미분해, 낮은 Confidence 강행으로 발생하는 Routing 실패다.

Q. Routing Failure는 어떻게 고쳐?
A. PM Agent가 Intent와 Domain을 재분석하고 Target Agent, RAG Scope, Handoff를 재설정해야 한다.

Q. Planner Agent는 뭐야?
A. 복합 요청을 실행 가능한 단계로 분해하고 순서, 담당 Agent, 의존성, 완료 기준을 정하는 Agent다.

Q. Planner Agent가 직접 실행해?
A. 아니다. Planner Agent는 계획을 만들고 실행은 Executor 또는 Specialist Agent가 담당한다.

Q. Planner Output에는 뭐가 있어야 해?
A. Goal, Steps, Target Agent, Dependency, Expected Output, Done Criteria, Review 필요 여부가 있어야 한다.

Q. Plan Quality가 뭐야?
A. 실행 계획이 요청 수행에 충분히 명확하고 안정적인지 평가하는 기준이다.

Q. 좋은 Plan의 조건은?
A. Step이 작고 명확하며, 의존성, Target Agent, Expected Output, Done Criteria가 있어야 한다.

Q. Step이 너무 크면 왜 문제야?
A. Agent가 한 번에 너무 많은 작업을 처리하면서 요구사항 누락과 Scope 위반이 발생할 수 있다.

Q. Plan Revision이 뭐야?
A. 실행 중 실패나 변경이 발생했을 때 기존 실행 계획을 수정하는 작업이다.

Q. 언제 Plan Revision이 필요해?
A. Missing Context, Agent Failure, Tool Permission 문제, User Request 변경, Critical Finding이 있을 때 필요하다.

Q. Executor Agent는 뭐야?
A. Planner가 만든 Step 또는 PM Agent가 지정한 작업을 실제로 실행하고 결과를 기록하는 Agent다.

Q. Executor Agent가 Plan을 마음대로 바꿔도 돼?
A. 안 된다. 필요한 경우 Plan Revision을 요청해야 한다.

Q. Executor Output에는 뭐가 있어야 해?
A. Execution ID, Plan ID, Step, Agent, Task, Status, Result Summary, Decisions, Risks, Open Questions가 있어야 한다.

Q. Execution Control이 뭐야?
A. Executor Agent가 작업 실행 전후로 Scope, Permission, Context, Status, Failure를 관리하는 기준이다.

Q. 실행 전 반드시 확인할 것은?
A. Plan Step, Scope, Required Context, Tool Permission, Approval 필요 여부다.

Q. Router Planner Executor Coordination이 뭐야?
A. Router의 Agent 선택, Planner의 실행 계획, Executor의 실행 결과를 연결해 관리하는 흐름이다.

Q. Router 결과가 틀리면 어떻게 돼?
A. Planner가 잘못된 Agent 기준으로 계획을 만들고 Executor가 잘못된 작업을 실행할 수 있다.

Q. State Integration이 뭐야?
A. Router, Planner, Executor의 결과를 Shared State에 반영하는 작업이다.

Q. State Integration에 기록할 것은?
A. Routing Result, Plan Result, Execution Result, Current Step, Status, Decisions, Risks, Open Questions다.

Q. Router Planner Executor Failure는 뭐야?
A. 요청 분류, 계획 수립, 실행 단계에서 발생하는 실패 유형이다.

Q. Router Failure와 Planner Failure는 어떻게 달라?
A. Router Failure는 Target Agent 선택 문제이고, Planner Failure는 Step 분해와 순서 문제다.

Q. Recovery Strategy가 뭐야?
A. Router, Planner, Executor 단계에서 실패가 발생했을 때 Workflow를 복구하는 방법이다.

Q. 모든 실패는 재실행하면 돼?
A. 아니다. 실패 유형에 따라 Routing 재수행, Plan Revision, Approval Request, 중단을 선택해야 한다.

Q. 개인 AI 프로젝트에서 Router, Planner, Executor를 처음부터 분리해야 해?
A. 아니다. 초기에는 PM Agent 내부 기능으로 두고 필요해질 때 분리하는 것이 좋다.

Q. Router Agent는 언제 분리해?
A. Agent 수가 늘고 Routing Failure가 반복될 때 분리한다.

Q. Planner Agent는 언제 분리해?
A. 복잡한 다단계 작업이 많아지고 Step 순서 오류가 반복될 때 분리한다.

Q. Executor Agent는 언제 분리해?
A. Tool 실행 자동화와 Step별 실행 상태 관리가 필요할 때 분리한다.

Q. Router Checklist가 뭐야?
A. 요청이 올바른 Agent에게 전달되는지 검수하는 기준이다.

Q. Planner Checklist가 뭐야?
A. 실행 계획이 명확하고 실행 가능한지 검수하는 기준이다.

Q. Executor Checklist가 뭐야?
A. 계획된 작업을 안전하게 실행하고 결과를 기록했는지 검수하는 기준이다.

Q. Part07과 Part12의 차이는 뭐야?
A. Part07은 Router, Planner, Executor 역할 자체를 다루고, Part12는 여러 Workflow Pattern의 종류와 선택 기준을 다룬다.
