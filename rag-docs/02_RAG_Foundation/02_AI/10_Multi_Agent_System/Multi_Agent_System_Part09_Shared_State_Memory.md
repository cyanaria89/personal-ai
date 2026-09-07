# Multi-Agent System Part09 - Shared State and Memory

---

# 1. Shared State Core

## 1.1 Shared State Definition

### [개념]

Shared State는 Multi-Agent System에서 현재 Workflow의 작업 상태를 Agent들이 공통으로 참조할 수 있도록 구조화한 정보이다.

Shared State는 현재 User Request, Requirements, Constraints, Decisions, Agent Outputs, Review Findings, Fix Results, Risks, Open Questions, Status를 저장한다.

Shared State의 목적은 Agent 간 기준을 통일하고, 이전 Step의 결과가 다음 Step에 정확히 전달되도록 하는 것이다.

기본 구조:

```text
User Request
→ Requirements
→ Constraints
→ Decisions
→ Agent Outputs
→ Review Findings
→ Fix Results
→ Final Output
```

PM Agent 중심 구조:

```text
PM Agent
→ Shared State 생성
→ Specialist Agent 참조
→ Review Agent 참조
→ Fix Agent 갱신
→ PM Agent 최종 통합
```

---

### [핵심]

- Shared State는 현재 Workflow의 공통 작업 상태이다.
- PM Agent가 주로 생성하고 관리한다.
- Agent들은 Shared State를 기준으로 작업 일관성을 유지한다.
- Requirements와 Constraints를 저장한다.
- Decisions를 저장한다.
- Agent Outputs를 저장한다.
- Review Findings와 Fix Results를 저장한다.
- Risks와 Open Questions를 저장한다.
- 현재 Step과 Status를 저장한다.
- 오래된 State가 현재 User Request를 덮어쓰면 안 된다.
- 모든 대화 원문을 저장하는 것은 Shared State가 아니다.

---

### [실무]

2026 실무 기준에서 Shared State는 Agent Workflow의 기준점으로 사용한다.

Shared State 예시:

```json
{
  "workflowId": "WF-001",
  "status": "in_progress",
  "currentStep": "backend_design",
  "currentUserRequest": "축제 리뷰 기능을 DB부터 화면까지 설계",
  "requirements": ["리뷰 작성", "리뷰 목록 조회", "리뷰 수정", "리뷰 삭제"],
  "constraints": [
    "JWT Authentication",
    "ApiResponse format",
    "Use Slice for list response"
  ],
  "decisions": [
    "Rating range is 0 to 5",
    "Review author can update/delete own review"
  ],
  "agentOutputs": {
    "SQL Agent": "reviews table design",
    "Backend Agent": "review API contract draft"
  },
  "reviewFindings": [],
  "fixResults": [],
  "risks": ["Duplicate review policy is not confirmed"],
  "openQuestions": [
    "Can one user write multiple reviews for the same festival?"
  ],
  "finalResult": null
}
```

Shared State에 저장할 정보:

```text
현재 사용자 요청
확정 요구사항
명시된 제약사항
PM Agent 결정사항
Agent별 핵심 Output
Review Findings
Fix Results
Risks
Open Questions
Current Step
Status
```

Shared State에 저장하지 않을 정보:

```text
전체 대화 원문
불필요한 잡담
현재 Workflow와 무관한 오래된 정보
검증되지 않은 추측
민감정보
Agent 내부 추론 과정
중복 Context
```

---

### [FAQ]

Q. Shared State가 뭐야?
A. Multi-Agent Workflow에서 현재 요청, 요구사항, 결정사항, Agent 결과, Review 결과를 공통으로 관리하는 작업 상태다.

Q. Shared State는 누가 관리해?
A. 일반적으로 PM Agent가 관리하고 각 Agent가 필요한 범위에서 참조한다.

Q. Shared State에 모든 대화를 저장해야 해?
A. 아니다. 현재 Workflow에 필요한 요구사항, 결정사항, Agent 결과, Review Findings만 저장해야 한다.

Q. Shared State가 중요한 이유는?
A. Agent 간 기준을 통일하고 다음 Agent가 이전 결과를 정확히 이어받게 하기 위해 중요하다.

---

## 1.2 Shared State vs Agent Output

### [개념]

Shared State와 Agent Output은 다르다.

Agent Output은 특정 Agent가 수행한 작업 결과이다.
Shared State는 여러 Agent Output 중 현재 Workflow에 필요한 핵심 상태를 정리한 공통 기준이다.

기본 구조:

```text
Agent Output
→ PM Agent Extract
→ Shared State Update
→ Next Agent Reference
```

---

### [핵심]

- Agent Output은 개별 Agent 산출물이다.
- Shared State는 Workflow 공통 기준이다.
- Agent Output 전체를 그대로 Shared State에 넣지 않는다.
- 필요한 Decisions, Risks, Open Questions, Output Summary만 추출한다.
- Shared State는 다음 Agent가 바로 사용할 수 있어야 한다.
- Agent Output이 Shared State Decision과 충돌하면 PM Agent가 정리한다.

---

### [실무]

Agent Output 예시:

```md
## Backend Agent Output

### API Contract

- POST /reviews
- GET /festivals/{festivalId}/reviews
- PATCH /reviews/{reviewId}
- DELETE /reviews/{reviewId}

### Risks

- Duplicate review policy is not confirmed

### Open Questions

- Can one user write multiple reviews for same festival?
```

Shared State 반영 예시:

```json
{
  "agentOutputs": {
    "Backend Agent": "Review API Contract completed"
  },
  "decisions": ["Review author can update/delete own review"],
  "risks": ["Duplicate review policy is not confirmed"],
  "openQuestions": ["Can one user write multiple reviews for same festival?"],
  "currentStep": "frontend_design"
}
```

---

### [FAQ]

Q. Agent Output과 Shared State는 같아?
A. 아니다. Agent Output은 개별 산출물이고 Shared State는 여러 산출물 중 현재 Workflow 기준으로 정리한 공통 상태다.

Q. Agent Output 전체를 Shared State에 넣어도 돼?
A. 권장하지 않는다. 핵심 Summary, Decisions, Risks, Open Questions만 추출하는 것이 좋다.

Q. Shared State는 다음 Agent에게 어떤 역할을 해?
A. 다음 Agent가 이전 Step의 확정 사항과 필요한 Context를 정확히 참조하게 해준다.

Q. Agent Output과 Shared State가 충돌하면?
A. PM Agent가 현재 User Request와 Decision 우선순위에 따라 정리해야 한다.

---

# 2. Shared State Schema

## 2.1 Core State Fields

### [개념]

Core State Fields는 Shared State를 구성하는 핵심 항목이다.

Core State Fields는 Workflow 진행 상황, 요구사항, 결정사항, Agent Output, Review-Fix 상태를 추적하기 위해 필요하다.

기본 Field:

```text
workflowId
status
currentStep
currentUserRequest
requirements
constraints
decisions
assumptions
agentOutputs
reviewFindings
fixResults
risks
openQuestions
finalResult
```

---

### [핵심]

- workflowId는 작업 단위 식별자이다.
- status는 Workflow 상태이다.
- currentStep은 현재 진행 단계이다.
- currentUserRequest는 현재 사용자 요청이다.
- requirements는 수행해야 할 요구사항이다.
- constraints는 지켜야 할 제약사항이다.
- decisions는 확정된 결정사항이다.
- assumptions는 임시 가정이다.
- agentOutputs는 Agent별 산출물 요약이다.
- reviewFindings는 검토 결과이다.
- fixResults는 수정 결과이다.
- risks는 위험 요소이다.
- openQuestions는 미확정 사항이다.
- finalResult는 최종 산출물이다.

---

### [실무]

Core Shared State Template:

```json
{
  "workflowId": "WF-001",
  "status": "initialized",
  "currentStep": "requirement_analysis",
  "currentUserRequest": "",
  "requirements": [],
  "constraints": [],
  "decisions": [],
  "assumptions": [],
  "agentOutputs": {},
  "toolResults": {},
  "reviewFindings": [],
  "fixResults": [],
  "risks": [],
  "openQuestions": [],
  "finalResult": null,
  "lastUpdatedBy": "PM Agent"
}
```

Status 예시:

| Status            | 의미              |
| ----------------- | ----------------- |
| initialized       | Workflow 시작     |
| in_progress       | 작업 진행 중      |
| blocked           | 필수 Context 부족 |
| review_required   | Review 필요       |
| fix_required      | Fix 필요          |
| approval_required | 사용자 승인 필요  |
| completed         | 완료              |
| failed            | 실패              |
| partial           | 일부 완료         |

Current Step 예시:

```text
requirement_analysis
task_decomposition
routing
planning
sql_design
backend_design
frontend_design
review
fix
final_integration
completed
```

---

### [FAQ]

Q. Core State Fields가 뭐야?
A. Shared State를 구성하는 workflowId, status, currentStep, requirements, decisions, agentOutputs 같은 핵심 항목이다.

Q. status는 왜 필요해?
A. Workflow가 진행 중인지, 막혔는지, 검토가 필요한지, 완료되었는지 구분하기 위해 필요하다.

Q. currentStep은 왜 필요해?
A. 현재 어떤 Agent 단계 또는 작업 단계에 있는지 추적하기 위해 필요하다.

Q. openQuestions는 왜 필요해?
A. 미확정 사항이 확정 결정처럼 사용되는 것을 막기 위해 필요하다.

---

## 2.2 Requirement Constraint Decision State

### [개념]

Requirement, Constraint, Decision State는 Shared State에서 가장 중요한 기준 정보이다.

Requirement는 해야 할 일이다.
Constraint는 지켜야 할 조건이다.
Decision은 Workflow 중 확정된 선택이다.

기본 구분:

```text
Requirement
→ What to do

Constraint
→ What rule to follow

Decision
→ What has been decided
```

---

### [핵심]

- Requirement는 기능 또는 작업 요구사항이다.
- Constraint는 기술, 형식, 보안, 출력 제약이다.
- Decision은 PM Agent 또는 Workflow에서 확정한 기준이다.
- Requirement와 Constraint를 섞으면 Handoff 품질이 떨어진다.
- 미확정 사항은 Decision이 아니라 Open Question이다.
- 임시 추정은 Decision이 아니라 Assumption이다.
- Review Agent는 Requirement Coverage와 Constraint Compliance를 검토한다.
- Fix Agent는 Decision을 보존해야 한다.

---

### [실무]

구분 예시:

```json
{
  "requirements": [
    "Authenticated user can create review",
    "User can view review list by festival",
    "Review author can update own review",
    "Review author can delete own review"
  ],
  "constraints": [
    "Use Spring Boot",
    "Use JPA",
    "Use ApiResponse format",
    "Use Slice for list response",
    "JWT Authentication required"
  ],
  "decisions": [
    "Rating range is 0 to 5",
    "Review author can update/delete only own review"
  ],
  "assumptions": ["Authenticated user is resolved from SecurityContext"],
  "openQuestions": ["Can one user write multiple reviews for same festival?"]
}
```

Decision State Template:

```json
{
  "decisionId": "D-001",
  "topic": "Review list pagination",
  "decision": "Use Slice",
  "reason": "Infinite scroll and lightweight list response",
  "source": "PM Agent",
  "affectedAgents": ["Backend Agent", "Frontend Agent", "Review Agent"],
  "status": "accepted"
}
```

Decision 변경 Template:

```json
{
  "decisionId": "D-002",
  "topic": "Review delete policy",
  "previousDecision": "Hard Delete",
  "newDecision": "Soft Delete",
  "reason": "Audit and recovery requirement added",
  "impact": [
    "reviews table needs deleted_at column",
    "Backend delete logic changes",
    "Review list query must exclude deleted reviews"
  ],
  "affectedAgents": [
    "SQL Agent",
    "Backend Agent",
    "Frontend Agent",
    "Review Agent"
  ],
  "status": "changed"
}
```

---

### [FAQ]

Q. Requirement, Constraint, Decision 차이는 뭐야?
A. Requirement는 해야 할 일, Constraint는 지켜야 할 조건, Decision은 확정된 선택이다.

Q. 미확정 사항도 Decision에 저장해?
A. 아니다. 미확정 사항은 Open Questions에 저장해야 한다.

Q. Assumption과 Decision은 어떻게 달라?
A. Assumption은 임시 가정이고 Decision은 확정된 기준이다.

Q. Decision을 변경하면 어떻게 해야 해?
A. 이전 결정, 새 결정, 변경 이유, 영향 범위, 영향받는 Agent를 기록해야 한다.

---

## 2.3 Agent Output State

### [개념]

Agent Output State는 각 Agent가 생성한 산출물의 핵심 요약을 Shared State에 저장한 정보이다.

Agent Output State는 PM Agent의 최종 통합, Review Agent의 검토, Fix Agent의 수정에 사용된다.

기본 구조:

```text
Source Agent
→ Task
→ Status
→ Output Summary
→ Decisions
→ Risks
→ Open Questions
```

---

### [핵심]

- Agent Output State는 Agent별 작업 결과 요약이다.
- Source Agent를 명확히 표시한다.
- Task와 Status를 포함한다.
- Output Summary를 저장한다.
- Decisions를 추출한다.
- Assumptions를 저장한다.
- Risks를 저장한다.
- Open Questions를 저장한다.
- 다음 Agent가 사용할 수 있는 형태여야 한다.
- 전체 원문보다 핵심 상태 중심으로 저장한다.

---

### [실무]

Agent Output State Template:

```json
{
  "agent": "Backend Agent",
  "task": "Festival Review API Design",
  "status": "completed",
  "outputSummary": [
    "POST /reviews",
    "GET /festivals/{festivalId}/reviews",
    "PATCH /reviews/{reviewId}",
    "DELETE /reviews/{reviewId}"
  ],
  "decisions": [
    "Review author can update/delete own review",
    "Rating validation is required"
  ],
  "assumptions": ["Authenticated user is resolved from SecurityContext"],
  "risks": ["Duplicate review policy not confirmed"],
  "openQuestions": ["Can one user write multiple reviews for same festival?"],
  "nextStep": "Review Agent"
}
```

Agent Output State 연결 예시:

```text
SQL Agent Output State
→ Backend Agent Entity / Repository 설계에 사용

Backend Agent Output State
→ Frontend Agent API Integration 설계에 사용

Frontend Agent Output State
→ Review Agent Cross-Domain Consistency 검토에 사용

Review Agent Output State
→ Fix Agent 수정 범위 결정에 사용
```

---

### [FAQ]

Q. Agent Output State가 뭐야?
A. 각 Agent가 생성한 산출물의 핵심 요약을 Shared State에 저장한 정보다.

Q. Agent Output State에는 뭐가 있어야 해?
A. Source Agent, Task, Status, Output Summary, Decisions, Assumptions, Risks, Open Questions가 있어야 한다.

Q. Agent Output State는 누가 사용해?
A. PM Agent, Review Agent, Fix Agent, 다음 Specialist Agent가 사용한다.

Q. Agent Output 전체 원문을 저장해야 해?
A. 아니다. 핵심 Summary와 상태 정보를 저장하는 것이 좋다.

---

# 3. Shared State Lifecycle

## 3.1 State Initialization

### [개념]

State Initialization은 새로운 Workflow가 시작될 때 Shared State를 생성하는 단계이다.

PM Agent는 Current User Request를 분석해 초기 Requirements, Constraints, Assumptions, Open Questions, Workflow Pattern을 기록한다.

기본 구조:

```text
User Request
→ PM Agent Analysis
→ Initial Shared State
→ Routing / Planning
```

---

### [핵심]

- Workflow 시작 시 Shared State를 초기화한다.
- Current User Request를 최우선으로 저장한다.
- Requirements를 추출한다.
- Constraints를 추출한다.
- Assumptions를 표시한다.
- Open Questions를 저장한다.
- 초기 Status와 Current Step을 설정한다.
- 이전 Workflow State를 그대로 재사용하지 않는다.
- 관련 Project Memory만 선별 참조한다.

---

### [실무]

State Initialization Template:

```json
{
  "workflowId": "WF-NEW",
  "status": "initialized",
  "currentStep": "requirement_analysis",
  "currentUserRequest": "Multi-Agent System Part09 재작업",
  "requirements": [
    "Shared State and Memory 문서 재작성",
    "오타 수정",
    "파일 간 중복 축소",
    "RAG Retrieval optimized document 유지"
  ],
  "constraints": [
    "Use required document structure",
    "Keep terminology consistent",
    "Output final document only"
  ],
  "assumptions": ["Part09 topic remains Shared State and Memory"],
  "openQuestions": [],
  "decisions": ["Current user request has highest priority"],
  "agentOutputs": {},
  "reviewFindings": [],
  "fixResults": []
}
```

초기화 시 주의:

```text
현재 User Request 우선
→ 관련 Memory만 참조
→ 이전 State 선별
→ 무관한 오래된 정보 제거
→ 충돌 정보는 Conflict로 기록
```

---

### [FAQ]

Q. State Initialization이 뭐야?
A. 새 Workflow가 시작될 때 Current User Request를 기준으로 Shared State를 생성하는 단계다.

Q. 이전 Workflow State를 그대로 써도 돼?
A. 아니다. 현재 요청과 관련 있는 정보만 선별해서 사용해야 한다.

Q. 초기 State에서 가장 중요한 것은?
A. Current User Request, Requirements, Constraints, Decisions, Open Questions다.

Q. 초기 State는 누가 만들어?
A. 일반적으로 PM Agent가 만든다.

---

## 3.2 State Update

### [개념]

State Update는 Workflow 진행 중 새로운 Agent Output, Review Findings, Fix Results, Decisions, Tool Results를 Shared State에 반영하는 단계이다.

State Update는 각 Agent가 최신 기준을 참조할 수 있게 만드는 핵심 작업이다.

기본 구조:

```text
Agent Result
→ Extract Summary
→ Extract Decisions
→ Extract Risks
→ Extract Open Questions
→ Update Shared State
```

---

### [핵심]

- State는 Workflow 진행 중 계속 갱신된다.
- Agent Output 수신 후 업데이트한다.
- Review Report 수신 후 업데이트한다.
- Fix Result 수신 후 업데이트한다.
- Tool Result 수신 후 업데이트한다.
- 새로운 Decision을 기록한다.
- 새로운 Risk를 기록한다.
- Open Question을 갱신한다.
- Status와 Current Step을 갱신한다.
- 오래된 값이 최신 값을 덮어쓰면 안 된다.
- 업데이트 출처를 기록하는 것이 좋다.

---

### [실무]

State Update Template:

```json
{
  "updateId": "UPD-001",
  "workflowId": "WF-001",
  "from": "Backend Agent",
  "updateType": "agent_output",
  "updates": {
    "currentStep": "backend_design_completed",
    "status": "review_required",
    "agentOutputs": {
      "Backend Agent": "Review API Contract Draft"
    },
    "decisions": ["Review author can update/delete own review"],
    "risks": ["Duplicate review policy not confirmed"],
    "openQuestions": ["Can one user write multiple reviews for same festival?"]
  }
}
```

업데이트 시점:

| 시점                    | 업데이트 대상                            |
| ----------------------- | ---------------------------------------- |
| Requirement Analysis 후 | requirements, constraints, assumptions   |
| Routing 후              | targetAgents, ragScope, workflowPattern  |
| Planning 후             | plannedSteps, dependencies, doneCriteria |
| Specialist Output 후    | agentOutputs, decisions, risks           |
| Review Report 후        | reviewFindings, status                   |
| Fix Result 후           | fixResults, regressionRisks, status      |
| Final Integration 후    | finalResult, status                      |

---

### [FAQ]

Q. State Update가 뭐야?
A. Workflow 진행 중 Agent Output, Review Findings, Fix Results, Decisions를 Shared State에 반영하는 단계다.

Q. State Update는 언제 해?
A. 요구사항 분석 후, Agent 결과 수신 후, Review 완료 후, Fix 완료 후, 최종 통합 후 수행한다.

Q. State Update에서 중요한 것은?
A. 최신 정보가 오래된 정보에 덮이지 않도록 하고 출처와 변경 내용을 명확히 하는 것이다.

Q. Tool Result도 Shared State에 반영해?
A. 중요한 Tool Result는 요약해서 반영해야 한다.

---

## 3.3 State Finalization

### [개념]

State Finalization은 Workflow가 완료될 때 최종 결과, 결정사항, 남은 Risk, Open Questions, Memory Candidate를 정리하는 단계이다.

State Finalization은 Final Output 생성과 다음 Workflow를 위한 정리 작업에 사용된다.

기본 구조:

```text
Agent Outputs
→ Review Findings
→ Fix Results
→ Final Integration
→ Final State
→ Final Output
```

---

### [핵심]

- Workflow 완료 시 State를 정리한다.
- Final Result를 저장한다.
- 최종 Decisions를 정리한다.
- 해결된 Review Findings를 표시한다.
- 남은 Risk를 표시한다.
- Open Questions를 표시한다.
- Status를 completed, partial, failed 중 하나로 설정한다.
- 장기 Memory 후보를 분리한다.
- 임시 State를 장기 Memory로 저장하지 않는다.

---

### [실무]

State Finalization Template:

```json
{
  "workflowId": "WF-001",
  "status": "completed",
  "finalResult": "Multi-Agent System Part09 Shared State and Memory document",
  "finalDecisions": [
    "Shared State is current workflow state",
    "Memory is long-term reusable information",
    "Current User Request has highest priority"
  ],
  "resolvedFindings": ["Typo fixed", "Duplicated workflow details compressed"],
  "remainingRisks": [],
  "openQuestions": [],
  "memoryCandidates": [
    "User prefers concise rework for files with duplication issues"
  ]
}
```

Finalization Checklist:

```md
## State Finalization Checklist

- [ ] Final Result가 저장되었는가?
- [ ] Final Decisions가 정리되었는가?
- [ ] Review Findings 처리 여부가 표시되었는가?
- [ ] Fix Results가 반영되었는가?
- [ ] Remaining Risks가 표시되었는가?
- [ ] Open Questions가 정리되었는가?
- [ ] Status가 완료 상태로 변경되었는가?
- [ ] 장기 Memory 후보와 임시 State를 구분했는가?
```

---

### [FAQ]

Q. State Finalization이 뭐야?
A. Workflow가 완료될 때 최종 결과, 결정사항, 남은 Risk, Open Questions를 정리하는 단계다.

Q. Final State에는 뭐가 있어야 해?
A. finalResult, finalDecisions, resolvedFindings, remainingRisks, openQuestions, status가 있어야 한다.

Q. 모든 State를 Memory로 저장해도 돼?
A. 아니다. 장기적으로 재사용 가능한 정보만 Memory 후보로 분리해야 한다.

Q. State Finalization은 왜 필요해?
A. Workflow 완료 상태를 명확히 하고 다음 작업에 필요한 정보와 임시 정보를 분리하기 위해 필요하다.

---

# 4. Memory Core

## 4.1 Memory Definition

### [개념]

Memory는 Multi-Agent System이 현재 Workflow를 넘어 장기적으로 재사용할 수 있는 정보이다.

Memory는 사용자의 장기 선호, 프로젝트 기술 스택, 반복되는 규칙, 장기 결정사항, Agent 운영 기준을 저장한다.

Memory는 Shared State와 다르다.

```text
Shared State
→ 현재 Workflow의 작업 상태

Memory
→ 장기적으로 재사용할 정보
```

---

### [핵심]

- Memory는 장기 재사용 정보이다.
- Shared State는 현재 작업 상태이다.
- Memory는 현재 User Request보다 우선하지 않는다.
- 현재 User Request와 충돌하면 현재 요청이 우선이다.
- 오래된 Memory는 검증 후 사용한다.
- 민감정보는 저장하지 않거나 제한한다.
- 임시 Assumption을 Memory로 저장하면 안 된다.
- Project Memory는 장기 프로젝트에 유용하다.
- User Preference Memory는 출력 스타일과 작업 방식에 유용하다.

---

### [실무]

Memory에 적합한 정보:

```text
사용자의 장기 프로젝트 목표
개인 AI 서버 기술 스택
RAG 문서 출력 형식 선호
프로젝트 디렉터리 구조
Agent 구성 결정
반복적으로 사용하는 문서 규칙
장기적으로 유지되는 Workflow 기준
```

Memory에 부적합한 정보:

```text
임시 대화 흐름
일회성 Assumption
검증되지 않은 추측
오래된 오류 상태
민감정보
단기 작업 중간 결과
사용자가 저장을 원하지 않는 정보
```

Memory 예시:

```json
{
  "memoryType": "project_memory",
  "topic": "Personal AI Development Team",
  "content": "User is building a local Multi-Agent System with PM Agent, SQL Agent, Backend Agent, Frontend Agent, Review Agent, Fix Agent.",
  "usage": "Use when discussing personal AI project agent architecture",
  "priority": "supporting_context"
}
```

---

### [FAQ]

Q. Memory가 뭐야?
A. 현재 Workflow를 넘어 장기적으로 재사용할 수 있는 사용자 선호, 프로젝트 정보, 장기 결정사항이다.

Q. Shared State와 Memory 차이는?
A. Shared State는 현재 Workflow의 작업 상태이고 Memory는 장기적으로 재사용할 정보다.

Q. Memory가 현재 요청보다 우선이야?
A. 아니다. 현재 User Request가 가장 우선이다.

Q. 모든 작업 정보를 Memory에 저장해야 해?
A. 아니다. 장기적으로 재사용할 가치가 있는 정보만 저장해야 한다.

---

## 4.2 Memory Types

### [개념]

Memory Types는 Multi-Agent System에서 장기 정보와 임시 정보를 목적에 따라 구분한 것이다.

Memory를 유형별로 나누면 필요한 정보만 검색하고, 오래된 정보나 민감한 정보를 줄일 수 있다.

주요 Memory Type:

```text
Short-term Memory
Working Memory
Long-term Memory
Project Memory
User Preference Memory
Agent Memory
Tool Memory
```

---

### [핵심]

- Short-term Memory는 짧은 대화 흐름에 사용한다.
- Working Memory는 현재 작업 처리에 사용한다.
- Long-term Memory는 장기적으로 유지되는 정보이다.
- Project Memory는 프로젝트 기술 스택, 구조, 결정사항이다.
- User Preference Memory는 출력 형식과 작업 방식 선호이다.
- Agent Memory는 Agent 운영 기준과 실패 사례이다.
- Tool Memory는 Tool 설정, 권한, 사용 기준이다.
- Memory Type에 따라 저장 기준이 달라야 한다.

---

### [실무]

Memory Type 비교:

| Memory Type            | 목적                | 예시                        | 저장 기간     |
| ---------------------- | ------------------- | --------------------------- | ------------- |
| Short-term Memory      | 현재 대화 흐름 유지 | 방금 말한 요구사항          | 짧음          |
| Working Memory         | 현재 작업 처리      | 현재 문서 Part Topic        | Workflow 동안 |
| Long-term Memory       | 장기 재사용         | 개인 AI 프로젝트 목표       | 길음          |
| Project Memory         | 프로젝트 정보       | AnythingLLM, Ollama, BGE-M3 | 길음          |
| User Preference Memory | 사용자 선호         | RAG 문서 출력 스타일        | 길음          |
| Agent Memory           | Agent 운영 기준     | PM Agent 중심 구조          | 중간~길음     |
| Tool Memory            | Tool 사용 기준      | 위험 Tool 승인 필요         | 중간~길음     |

Memory Type 사용 예시:

```json
{
  "shortTermMemory": ["Current document is Part09"],
  "workingMemory": ["Use RAG document writing block format"],
  "projectMemory": [
    "Personal AI Development Team uses PM Agent-centered workflow"
  ],
  "userPreferenceMemory": [
    "User prefers final result only for this RAG document production flow"
  ]
}
```

---

### [FAQ]

Q. Memory Type이 뭐야?
A. Memory를 Short-term, Working, Long-term, Project, User Preference처럼 목적별로 나눈 것이다.

Q. Project Memory는 뭐야?
A. 프로젝트 목표, 기술 스택, 구조, 장기 결정사항을 저장하는 Memory다.

Q. User Preference Memory는 뭐야?
A. 사용자의 출력 형식, 작업 방식, 선호 규칙을 저장하는 Memory다.

Q. Working Memory와 Shared State는 같아?
A. 다르다. Working Memory는 현재 작업 중 임시 정보이고 Shared State는 Agent들이 공유하는 구조화된 Workflow 상태다.

---

# 5. Shared State vs Memory

## 5.1 Difference Between Shared State and Memory

### [개념]

Shared State와 Memory는 모두 Context 관리에 사용되지만 목적과 수명이 다르다.

Shared State는 현재 Workflow의 실행 상태이다.
Memory는 다음 Workflow에서도 재사용할 수 있는 장기 정보이다.

비교 구조:

```text
Shared State
→ Current Workflow
→ Temporary / Active
→ Step / Decision / Output 중심

Memory
→ Long-term Reuse
→ Persistent / Selective
→ Preference / Project / Pattern 중심
```

---

### [핵심]

- Shared State는 현재 작업 상태이다.
- Memory는 장기 재사용 정보이다.
- Shared State는 Workflow 완료 후 정리된다.
- Memory는 다음 Workflow에서 참조될 수 있다.
- Shared State는 최신성이 중요하다.
- Memory는 정확성과 민감정보 관리가 중요하다.
- Shared State는 Agent 간 동기화에 사용한다.
- Memory는 PM Agent의 Context 보강에 사용한다.
- 현재 User Request는 Shared State와 Memory보다 우선한다.

---

### [실무]

Shared State vs Memory 비교:

| 구분      | Shared State                     | Memory                                |
| --------- | -------------------------------- | ------------------------------------- |
| 목적      | 현재 Workflow 관리               | 장기 정보 재사용                      |
| 수명      | 작업 중                          | 장기                                  |
| 내용      | 요구사항, 결정사항, Agent Output | 프로젝트 목표, 사용자 선호, 장기 규칙 |
| 관리 주체 | PM Agent                         | PM Agent 또는 Memory Manager          |
| 사용 대상 | 현재 Agent Workflow              | 이후 Workflow                         |
| 위험      | 오래된 State 사용                | 오래된 Memory 오신뢰                  |
| 우선순위  | 현재 작업 기준                   | 보조 Context                          |
| 저장 범위 | 필요한 현재 상태                 | 선별된 장기 정보                      |

예시:

```text
Shared State:
- 현재 문서는 Part09 재작업이다.
- 이번 출력은 writing block만 사용한다.
- Part09 오타와 중복을 수정해야 한다.

Memory:
- 사용자는 RAG 문서 제작 시 Retrieval 최적화를 우선한다.
- 개인 AI 프로젝트는 PM Agent 중심 Multi-Agent 구조를 목표로 한다.
```

---

### [FAQ]

Q. Shared State와 Memory 차이는 뭐야?
A. Shared State는 현재 Workflow의 작업 상태이고 Memory는 장기적으로 재사용할 정보다.

Q. Shared State는 작업이 끝나면 어떻게 해?
A. Finalization을 통해 정리하고, 장기적으로 필요한 정보만 Memory 후보로 분리한다.

Q. Memory는 항상 믿어도 돼?
A. 아니다. 오래된 Memory는 현재 요청과 충돌할 수 있으므로 검증해야 한다.

Q. 현재 요청과 Memory가 충돌하면?
A. 현재 User Request가 우선이다.

---

## 5.2 State Memory Conflict

### [개념]

State Memory Conflict는 현재 Shared State와 장기 Memory가 서로 충돌하는 상황이다.

State Memory Conflict는 오래된 프로젝트 정보, 바뀐 사용자 선호, 이전 Workflow 결정사항이 현재 요청과 맞지 않을 때 발생한다.

예시:

```text
Memory:
- 중간 진행 업데이트 제공 선호

Current Shared State:
- 중간 응답 금지
- 작업 완료 후 결과만 출력

Decision:
- Current User Request와 Current Shared State 우선
```

---

### [핵심]

- State와 Memory는 충돌할 수 있다.
- 현재 User Request가 가장 우선이다.
- Current Shared State는 현재 Workflow 기준이다.
- Memory는 보조 Context이다.
- 충돌 시 Memory를 무조건 적용하면 안 된다.
- 충돌은 명시적으로 기록할 수 있다.
- 반복 충돌이 발생하면 Memory Update가 필요할 수 있다.
- 민감하거나 불확실한 Memory는 사용하지 않는다.

---

### [실무]

Conflict Priority:

```text
Current User Request
→ Current Shared State
→ Explicit PM Agent Decision
→ Master Rules
→ Domain Rules
→ Project Memory
→ User Preference Memory
→ Older Memory
```

State Memory Conflict Record:

```md
## State Memory Conflict

### Conflict

Older Memory는 진행 업데이트를 권장하지만 Current User Request는 중간 응답 금지를 요구함

### Priority

Current User Request > Older Memory

### Decision

RAG 문서 제작 응답에서는 중간 응답 없이 최종 결과만 출력

### Memory Update Candidate

User prefers no intermediate response in this RAG document production workflow
```

충돌 처리 기준:

| Conflict Type                 | Handling                |
| ----------------------------- | ----------------------- |
| 현재 요청 vs Memory           | 현재 요청 우선          |
| Shared State vs 오래된 Memory | Shared State 우선       |
| Domain Rules vs Memory        | Domain Rules 우선       |
| Memory가 틀림                 | Memory Update 또는 무시 |
| Memory가 민감함               | 사용 제한               |
| Memory가 불확실함             | Assumption으로 표시     |

---

### [FAQ]

Q. State Memory Conflict가 뭐야?
A. 현재 Shared State와 장기 Memory가 서로 충돌하는 상황이다.

Q. State와 Memory가 충돌하면 뭐가 우선이야?
A. 현재 User Request와 Current Shared State가 우선이다.

Q. 오래된 Memory는 어떻게 처리해?
A. 현재 요청과 맞는지 검증하고, 충돌하면 사용하지 않거나 업데이트 후보로 분리한다.

Q. 반복되는 Memory 충돌은 어떻게 해?
A. Memory Update 기준에 따라 오래된 Memory를 수정하거나 새로운 선호로 갱신한다.

---

# 6. Memory Retrieval and Update

## 6.1 Memory Retrieval

### [개념]

Memory Retrieval은 현재 Workflow에 필요한 장기 정보를 Memory에서 검색하는 과정이다.

Memory Retrieval은 현재 요청과 관련된 정보만 가져와야 하며, 모든 Memory를 Context로 넣으면 안 된다.

기본 구조:

```text
Current Task
→ Memory Query
→ Relevant Memory Retrieval
→ Conflict Check
→ Context Packaging
→ Agent Use
```

---

### [핵심]

- Memory Retrieval은 필요한 정보만 검색한다.
- 현재 Task와 관련된 Memory만 사용한다.
- 오래된 Memory는 검증한다.
- 현재 User Request와 충돌하는 Memory는 사용하지 않는다.
- Memory는 출처와 최신성을 확인하는 것이 좋다.
- 관련 없는 Memory는 Context에 넣지 않는다.
- 과도한 Memory 사용은 Token 낭비와 지시 혼선을 만든다.
- Memory Retrieval 결과는 보조 Context로 사용한다.

---

### [실무]

Memory Retrieval 예시:

```json
{
  "currentTask": "Create Multi-Agent System RAG document",
  "memoryQuery": "User RAG document output preference and personal AI project agent structure",
  "retrievedMemory": [
    "User prefers RAG documents optimized for AI Agent Retrieval, not human essay",
    "User's personal AI development team uses PM Agent-centered workflow",
    "User wants final result only for this RAG document production flow"
  ],
  "conflictCheck": {
    "conflict": false
  },
  "usage": [
    "Apply output format",
    "Use PM Agent-centered examples",
    "Avoid intermediate explanation"
  ]
}
```

나쁜 Memory Retrieval 예시:

```text
현재 작업:
- RAG 문서 Part09 작성

잘못된 Retrieval:
- 과거 FestaPick 프로젝트 코드 오류
- 빅분기 시험 메모
- 카카오맵 API 문제
- Docker 과거 실패 로그 전체

문제:
- Context 과다
- 현재 작업과 무관
- 핵심 지시 희석
```

---

### [FAQ]

Q. Memory Retrieval이 뭐야?
A. 현재 Workflow에 필요한 장기 정보를 Memory에서 검색하는 과정이다.

Q. 모든 Memory를 Context에 넣어도 돼?
A. 아니다. 현재 Task와 관련된 Memory만 선별해야 한다.

Q. Memory Retrieval 후 반드시 해야 할 것은?
A. 현재 User Request와 충돌하는지 확인해야 한다.

Q. 관련 없는 Memory를 넣으면 어떻게 돼?
A. Token 낭비가 발생하고 Agent가 잘못된 Context를 참조할 수 있다.

---

## 6.2 Memory Update

### [개념]

Memory Update는 Workflow 결과 중 장기적으로 재사용할 가치가 있는 정보를 Memory에 저장하거나 기존 Memory를 수정하는 작업이다.

Memory Update는 모든 정보를 저장하는 것이 아니라, 장기 프로젝트 정보, 사용자 선호, 반복 규칙, 안정된 결정사항만 선별해야 한다.

기본 구조:

```text
Workflow Finalization
→ Memory Candidate Selection
→ Sensitivity Check
→ Conflict Check
→ Update Memory
```

---

### [핵심]

- Memory Update는 선별적으로 수행한다.
- 장기적으로 재사용할 정보만 저장한다.
- 임시 Assumption은 저장하지 않는다.
- 검증되지 않은 추측은 저장하지 않는다.
- 민감정보는 저장하지 않거나 제한한다.
- 현재 사용자 요청에서 명시한 선호는 저장 후보가 될 수 있다.
- 기존 Memory와 충돌하면 갱신 또는 무시한다.
- Memory Update 기준이 없으면 Memory 품질이 떨어진다.

---

### [실무]

Memory Update 후보:

```text
장기 프로젝트 목표
→ 저장 가능

반복 출력 형식 선호
→ 저장 가능

Agent 구성 결정
→ 저장 가능

이번 작업의 임시 Part 번호
→ 저장하지 않음

불확실한 추측
→ 저장하지 않음

민감정보
→ 저장 제한
```

Memory Update Template:

```json
{
  "memoryCandidate": {
    "type": "user_preference",
    "content": "For RAG document production, user prefers final output only in writing block format.",
    "reason": "User repeatedly requested final document output without extra explanation",
    "sensitivity": "low",
    "duration": "long-term",
    "conflictCheck": "no conflict"
  },
  "action": "store_or_update"
}
```

Memory Update 거절 예시:

```json
{
  "memoryCandidate": {
    "type": "temporary_state",
    "content": "Current document is Part09",
    "reason": "Temporary workflow state",
    "duration": "short-term"
  },
  "action": "do_not_store"
}
```

---

### [FAQ]

Q. Memory Update가 뭐야?
A. Workflow 결과 중 장기적으로 재사용할 가치가 있는 정보를 Memory에 저장하거나 기존 Memory를 수정하는 작업이다.

Q. 어떤 정보를 Memory에 저장해?
A. 장기 프로젝트 목표, 사용자 선호, 반복 규칙, 안정된 결정사항을 저장한다.

Q. 어떤 정보는 저장하면 안 돼?
A. 임시 Assumption, 검증되지 않은 추측, 일회성 상태, 민감정보는 저장하지 않는 것이 좋다.

Q. Memory Update 기준이 필요한 이유는?
A. 불필요하거나 오래된 정보가 쌓이면 Agent 품질이 떨어지기 때문이다.

---

# 7. State and Memory Failure Handling

## 7.1 Shared State Failure

### [개념]

Shared State Failure는 Shared State가 누락, 오래됨, 충돌, 과다 저장, 잘못된 업데이트로 인해 Agent Workflow 품질을 떨어뜨리는 문제이다.

Shared State Failure는 Agent 간 일관성 오류와 Review-Fix Loop 반복의 원인이 된다.

주요 실패 유형:

```text
Missing Requirement State
Stale State
Decision Conflict
State Overload
Wrong Status
Missing Agent Output
Missing Review Finding
Untracked Open Question
```

---

### [핵심]

- 요구사항 State가 누락되면 Agent가 요구사항을 놓친다.
- 오래된 State는 최신 요청과 충돌할 수 있다.
- Decision Conflict는 PM Agent가 정리해야 한다.
- State Overload는 핵심 정보를 묻히게 한다.
- Status가 틀리면 Workflow가 잘못 진행된다.
- Agent Output 누락은 다음 Agent 작업을 방해한다.
- Review Finding 누락은 Fix Agent 작업을 방해한다.
- Open Question 누락은 불확실한 내용을 확정처럼 만들 수 있다.

---

### [실무]

Shared State Failure 대응 기준:

| Failure Type              | Cause              | Handling                   |
| ------------------------- | ------------------ | -------------------------- |
| Missing Requirement State | 요구사항 기록 누락 | PM Agent가 State 보강      |
| Stale State               | 오래된 정보 사용   | Current User Request 우선  |
| Decision Conflict         | 상충 결정 존재     | PM Agent Decision으로 정리 |
| State Overload            | 전체 대화 저장     | Context Packaging 적용     |
| Wrong Status              | 상태 갱신 오류     | Status 재설정              |
| Missing Agent Output      | 결과 기록 누락     | Agent Output State 추가    |
| Missing Review Finding    | 검토 결과 누락     | Review Report 연결         |
| Untracked Open Question   | 미확정 사항 누락   | Open Questions에 기록      |

Shared State Failure Output 예시:

```md
## Shared State Failure

### Failure Type

Decision Conflict

### Issue

Shared State에는 Review list uses Slice로 기록되어 있으나 Backend Agent Output은 Page를 사용함

### Impact

Frontend Agent가 Pagination 구조를 잘못 설계할 수 있음

### Fix Direction

PM Agent가 Slice 사용 Decision을 재확인하고 Backend Agent Output을 수정 대상으로 전달

### Re-review Required

Yes
```

---

### [FAQ]

Q. Shared State Failure는 언제 발생해?
A. State가 누락, 오래됨, 충돌, 과다 저장, 잘못된 업데이트 상태일 때 발생한다.

Q. Stale State가 뭐야?
A. 오래된 State가 최신 User Request 또는 최신 Decision과 맞지 않는 상태다.

Q. Decision Conflict는 누가 정리해?
A. PM Agent가 최종 Decision을 정리하고 Shared State를 갱신해야 한다.

Q. State Overload는 왜 문제야?
A. 너무 많은 정보가 저장되어 핵심 요구사항과 결정사항이 묻히기 때문이다.

---

## 7.2 Memory Failure

### [개념]

Memory Failure는 오래된 Memory, 잘못된 Memory, 과도한 Memory, 민감정보 저장, 현재 요청과 충돌하는 Memory 사용으로 인해 Agent 품질이 떨어지는 문제이다.

Memory Failure는 장기 프로젝트에서 점진적으로 누적될 수 있다.

주요 실패 유형:

```text
Stale Memory
Wrong Memory
Overloaded Memory
Sensitive Memory
Memory Conflict
Unverified Memory
Memory Overtrust
```

---

### [핵심]

- 오래된 Memory는 현재 상황과 맞지 않을 수 있다.
- 잘못 저장된 Memory는 반복 오류를 만든다.
- 과도한 Memory는 Retrieval 품질을 떨어뜨린다.
- 민감정보 저장은 위험하다.
- 현재 요청과 충돌하는 Memory는 사용하면 안 된다.
- 검증되지 않은 Memory를 확정처럼 사용하면 안 된다.
- Memory는 보조 Context이지 절대 기준이 아니다.
- 반복 오류가 발생하면 Memory를 수정해야 한다.

---

### [실무]

Memory Failure 대응 기준:

| Failure Type      | Cause                       | Handling                   |
| ----------------- | --------------------------- | -------------------------- |
| Stale Memory      | 오래된 프로젝트 정보        | 최신 정보 확인             |
| Wrong Memory      | 잘못 저장된 정보            | Memory 수정 또는 무시      |
| Overloaded Memory | 너무 많은 저장              | Memory 정리                |
| Sensitive Memory  | 민감정보 저장               | 저장 제한 또는 삭제        |
| Memory Conflict   | 현재 요청과 충돌            | 현재 요청 우선             |
| Unverified Memory | 출처 불명확                 | Assumption으로 취급        |
| Memory Overtrust  | Memory를 절대 기준으로 사용 | User Request 우선순위 적용 |

Memory Failure 예시:

```md
## Memory Failure

### Failure Type

Memory Conflict

### Issue

Memory는 Open WebUI 기반 구성을 참조하지만 현재 프로젝트는 AnythingLLM 기반으로 변경됨

### Impact

잘못된 플랫폼 기준으로 Agent 설계가 진행될 수 있음

### Fix Direction

현재 Project Memory에서 AnythingLLM + Ollama + BGE-M3 기준을 우선하고 Open WebUI 정보는 Legacy Context로만 사용
```

---

### [FAQ]

Q. Memory Failure는 언제 발생해?
A. 오래된 Memory, 잘못된 Memory, 과도한 Memory, 현재 요청과 충돌하는 Memory를 사용할 때 발생한다.

Q. Memory Overtrust가 뭐야?
A. Memory를 현재 요청보다 우선하는 절대 기준처럼 사용하는 문제다.

Q. Memory가 틀렸으면 어떻게 해?
A. 현재 정보 기준으로 수정하거나 해당 Memory를 사용하지 않아야 한다.

Q. 민감정보는 Memory에 저장해도 돼?
A. 원칙적으로 저장하지 않거나 사용자 명시 요청이 있을 때만 제한적으로 저장해야 한다.

---

# 8. State Memory Checklist

## 8.1 Shared State Checklist

### [개념]

Shared State Checklist는 Shared State가 현재 Workflow를 정확히 반영하는지 검수하는 기준이다.

Checklist를 적용하면 State 누락, 오래된 결정, Agent Output 누락, Review Finding 누락을 줄일 수 있다.

---

### [핵심]

- Current User Request가 저장되었는지 확인한다.
- Requirements가 저장되었는지 확인한다.
- Constraints가 저장되었는지 확인한다.
- Decisions가 저장되었는지 확인한다.
- Current Step이 정확한지 확인한다.
- Status가 정확한지 확인한다.
- Agent Outputs가 반영되었는지 확인한다.
- Review Findings가 반영되었는지 확인한다.
- Fix Results가 반영되었는지 확인한다.
- Open Questions가 누락되지 않았는지 확인한다.
- 오래된 State가 최신 요청을 덮지 않았는지 확인한다.

---

### [실무]

Shared State Checklist:

```md
## Shared State Checklist

- [ ] Current User Request가 저장되었는가?
- [ ] Functional Requirements가 저장되었는가?
- [ ] Constraints가 저장되었는가?
- [ ] Assumptions가 표시되었는가?
- [ ] Decisions가 명확한가?
- [ ] 미확정 사항이 Open Questions로 분리되었는가?
- [ ] Current Step이 정확한가?
- [ ] Status가 정확한가?
- [ ] Agent Outputs가 최신 상태인가?
- [ ] Review Findings가 반영되었는가?
- [ ] Fix Results가 반영되었는가?
- [ ] Risks가 기록되었는가?
- [ ] 오래된 State가 최신 요청을 덮지 않았는가?
- [ ] 다음 Agent가 사용할 수 있는 형태인가?
```

---

### [FAQ]

Q. Shared State Checklist가 뭐야?
A. Shared State가 현재 Workflow의 요구사항, 결정사항, Agent 결과, Review 결과를 정확히 반영하는지 검수하는 기준이다.

Q. Shared State에서 가장 중요한 항목은?
A. Current User Request, Requirements, Constraints, Decisions, Status, Agent Outputs, Review Findings다.

Q. Open Questions를 State에 저장해야 해?
A. 저장해야 한다. 미확정 사항이 확정처럼 처리되는 것을 막기 위해 필요하다.

Q. 오래된 State는 어떻게 확인해?
A. Current User Request와 최신 PM Decision을 기준으로 충돌 여부를 검토한다.

---

## 8.2 Memory Checklist

### [개념]

Memory Checklist는 Memory Retrieval과 Memory Update가 안전하고 정확하게 수행되는지 검수하는 기준이다.

Checklist를 적용하면 오래된 Memory 사용, 과도한 Memory 저장, 민감정보 저장, 현재 요청과의 충돌을 줄일 수 있다.

---

### [핵심]

- 현재 Task와 관련된 Memory만 검색한다.
- Memory 최신성을 확인한다.
- 현재 User Request와 충돌하는지 확인한다.
- Memory를 절대 기준으로 사용하지 않는다.
- 장기적으로 재사용할 정보만 저장한다.
- 임시 Assumption은 저장하지 않는다.
- 민감정보 저장을 제한한다.
- 잘못된 Memory는 갱신하거나 무시한다.
- Memory Update 후보와 Temporary State를 구분한다.

---

### [실무]

Memory Retrieval Checklist:

```md
## Memory Retrieval Checklist

- [ ] 현재 Task와 관련된 Memory인가?
- [ ] Memory가 최신 정보인가?
- [ ] Current User Request와 충돌하지 않는가?
- [ ] Shared State와 충돌하지 않는가?
- [ ] Domain Rules와 충돌하지 않는가?
- [ ] 민감정보를 포함하지 않는가?
- [ ] 필요한 만큼만 Context에 포함했는가?
- [ ] Memory를 확정 사실처럼 과신하지 않았는가?
```

Memory Update Checklist:

```md
## Memory Update Checklist

- [ ] 장기적으로 재사용할 정보인가?
- [ ] 사용자 선호 또는 프로젝트 결정인가?
- [ ] 일회성 State가 아닌가?
- [ ] 검증되지 않은 추측이 아닌가?
- [ ] 민감정보가 아닌가?
- [ ] 기존 Memory와 충돌하지 않는가?
- [ ] 저장 이유가 명확한가?
- [ ] 저장 범위가 과도하지 않은가?
```

---

### [FAQ]

Q. Memory Checklist가 뭐야?
A. Memory Retrieval과 Memory Update가 안전하고 정확하게 수행되는지 검수하는 기준이다.

Q. Memory Retrieval에서 가장 중요한 것은?
A. 현재 Task와 관련 있고, 현재 User Request와 충돌하지 않는 Memory만 사용하는 것이다.

Q. Memory Update에서 가장 중요한 것은?
A. 장기적으로 재사용할 가치가 있고 민감하지 않은 정보만 저장하는 것이다.

Q. 임시 작업 상태도 Memory에 저장해?
A. 아니다. 임시 작업 상태는 Shared State에 두고 장기 Memory에는 저장하지 않는다.

---

# Retrieval Queries

### [FAQ]

Q. Shared State가 뭐야?
A. Multi-Agent Workflow에서 현재 요청, 요구사항, 결정사항, Agent 결과, Review 결과를 공통으로 관리하는 작업 상태다.

Q. Shared State는 누가 관리해?
A. 일반적으로 PM Agent가 관리하고 각 Agent가 필요한 범위에서 참조한다.

Q. Shared State에 모든 대화를 저장해야 해?
A. 아니다. 현재 Workflow에 필요한 요구사항, 결정사항, Agent 결과, Review Findings만 저장해야 한다.

Q. Shared State가 중요한 이유는?
A. Agent 간 기준을 통일하고 다음 Agent가 이전 결과를 정확히 이어받게 하기 위해 중요하다.

Q. Agent Output과 Shared State는 같아?
A. 아니다. Agent Output은 개별 산출물이고 Shared State는 여러 산출물 중 현재 Workflow 기준으로 정리한 공통 상태다.

Q. Agent Output 전체를 Shared State에 넣어도 돼?
A. 권장하지 않는다. 핵심 Summary, Decisions, Risks, Open Questions만 추출하는 것이 좋다.

Q. Core State Fields가 뭐야?
A. Shared State를 구성하는 workflowId, status, currentStep, requirements, decisions, agentOutputs 같은 핵심 항목이다.

Q. Shared State status는 왜 필요해?
A. Workflow가 진행 중인지, 막혔는지, 검토가 필요한지, 완료되었는지 구분하기 위해 필요하다.

Q. Requirement, Constraint, Decision 차이는 뭐야?
A. Requirement는 해야 할 일, Constraint는 지켜야 할 조건, Decision은 확정된 선택이다.

Q. 미확정 사항도 Decision에 저장해?
A. 아니다. 미확정 사항은 Open Questions에 저장해야 한다.

Q. Assumption과 Decision은 어떻게 달라?
A. Assumption은 임시 가정이고 Decision은 확정된 기준이다.

Q. Decision을 변경하면 어떻게 해야 해?
A. 이전 결정, 새 결정, 변경 이유, 영향 범위, 영향받는 Agent를 기록해야 한다.

Q. Agent Output State가 뭐야?
A. 각 Agent가 생성한 산출물의 핵심 요약을 Shared State에 저장한 정보다.

Q. Agent Output State에는 뭐가 있어야 해?
A. Source Agent, Task, Status, Output Summary, Decisions, Assumptions, Risks, Open Questions가 있어야 한다.

Q. State Initialization이 뭐야?
A. 새 Workflow가 시작될 때 Current User Request를 기준으로 Shared State를 생성하는 단계다.

Q. 이전 Workflow State를 그대로 써도 돼?
A. 아니다. 현재 요청과 관련 있는 정보만 선별해서 사용해야 한다.

Q. State Update가 뭐야?
A. Workflow 진행 중 Agent Output, Review Findings, Fix Results, Decisions를 Shared State에 반영하는 단계다.

Q. State Update는 언제 해?
A. 요구사항 분석 후, Agent 결과 수신 후, Review 완료 후, Fix 완료 후, 최종 통합 후 수행한다.

Q. State Finalization이 뭐야?
A. Workflow가 완료될 때 최종 결과, 결정사항, 남은 Risk, Open Questions를 정리하는 단계다.

Q. Memory가 뭐야?
A. 현재 Workflow를 넘어 장기적으로 재사용할 수 있는 사용자 선호, 프로젝트 정보, 장기 결정사항이다.

Q. Shared State와 Memory 차이는?
A. Shared State는 현재 Workflow의 작업 상태이고 Memory는 장기적으로 재사용할 정보다.

Q. Memory가 현재 요청보다 우선이야?
A. 아니다. 현재 User Request가 가장 우선이다.

Q. 모든 작업 정보를 Memory에 저장해야 해?
A. 아니다. 장기적으로 재사용할 가치가 있는 정보만 저장해야 한다.

Q. Memory Type이 뭐야?
A. Memory를 Short-term, Working, Long-term, Project, User Preference처럼 목적별로 나눈 것이다.

Q. Project Memory는 뭐야?
A. 프로젝트 목표, 기술 스택, 구조, 장기 결정사항을 저장하는 Memory다.

Q. User Preference Memory는 뭐야?
A. 사용자의 출력 형식, 작업 방식, 선호 규칙을 저장하는 Memory다.

Q. Working Memory와 Shared State는 같아?
A. 다르다. Working Memory는 현재 작업 중 임시 정보이고 Shared State는 Agent들이 공유하는 구조화된 Workflow 상태다.

Q. State Memory Conflict가 뭐야?
A. 현재 Shared State와 장기 Memory가 서로 충돌하는 상황이다.

Q. State와 Memory가 충돌하면 뭐가 우선이야?
A. 현재 User Request와 Current Shared State가 우선이다.

Q. 오래된 Memory는 어떻게 처리해?
A. 현재 요청과 맞는지 검증하고, 충돌하면 사용하지 않거나 업데이트 후보로 분리한다.

Q. Memory Retrieval이 뭐야?
A. 현재 Workflow에 필요한 장기 정보를 Memory에서 검색하는 과정이다.

Q. 모든 Memory를 Context에 넣어도 돼?
A. 아니다. 현재 Task와 관련된 Memory만 선별해야 한다.

Q. Memory Retrieval 후 반드시 해야 할 것은?
A. 현재 User Request와 충돌하는지 확인해야 한다.

Q. Memory Update가 뭐야?
A. Workflow 결과 중 장기적으로 재사용할 가치가 있는 정보를 Memory에 저장하거나 기존 Memory를 수정하는 작업이다.

Q. 어떤 정보를 Memory에 저장해?
A. 장기 프로젝트 목표, 사용자 선호, 반복 규칙, 안정된 결정사항을 저장한다.

Q. 어떤 정보는 Memory에 저장하면 안 돼?
A. 임시 Assumption, 검증되지 않은 추측, 일회성 상태, 민감정보는 저장하지 않는 것이 좋다.

Q. Shared State Failure는 언제 발생해?
A. State가 누락, 오래됨, 충돌, 과다 저장, 잘못된 업데이트 상태일 때 발생한다.

Q. Stale State가 뭐야?
A. 오래된 State가 최신 User Request 또는 최신 Decision과 맞지 않는 상태다.

Q. Decision Conflict는 누가 정리해?
A. PM Agent가 최종 Decision을 정리하고 Shared State를 갱신해야 한다.

Q. Memory Failure는 언제 발생해?
A. 오래된 Memory, 잘못된 Memory, 과도한 Memory, 현재 요청과 충돌하는 Memory를 사용할 때 발생한다.

Q. Memory Overtrust가 뭐야?
A. Memory를 현재 요청보다 우선하는 절대 기준처럼 사용하는 문제다.

Q. Shared State Checklist가 뭐야?
A. Shared State가 현재 Workflow의 요구사항, 결정사항, Agent 결과, Review 결과를 정확히 반영하는지 검수하는 기준이다.

Q. Memory Checklist가 뭐야?
A. Memory Retrieval과 Memory Update가 안전하고 정확하게 수행되는지 검수하는 기준이다.

Q. 개인 AI 개발팀에서 Shared State는 어디에 쓰여?
A. PM Agent가 요구사항, 결정사항, Agent Output, Review Findings, Fix Results를 관리하는 데 사용한다.

Q. 개인 AI 개발팀에서 Memory는 어디에 쓰여?
A. 장기 프로젝트 목표, Agent 구조, RAG 문서 제작 선호, 반복 Workflow 규칙을 재사용하는 데 사용한다.
