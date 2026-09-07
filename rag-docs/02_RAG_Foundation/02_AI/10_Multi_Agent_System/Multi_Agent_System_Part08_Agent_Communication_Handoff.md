# Multi-Agent System Part08 - Agent Communication and Handoff

---

# 1. Agent Communication Core

## 1.1 Agent Communication Definition

### [개념]

Agent Communication은 Multi-Agent System에서 Agent 간 작업 정보, Context, 결정사항, 결과, 실패 상태를 전달하는 구조이다.

Agent Communication은 단순 대화 기록 전달이 아니라, 다음 Agent가 바로 작업할 수 있도록 구조화된 메시지를 전달하는 방식이다.

Agent Communication의 핵심은 누락 없는 정보 전달, 명확한 책임 구분, 추적 가능한 Handoff, 실패 상태의 정확한 공유이다.

기본 구조:

```text
Source Agent
→ Message
→ Target Agent
→ Context
→ Task
→ Expected Output
→ Result
```

Multi-Agent Workflow 기준:

```text
PM Agent
→ Handoff
→ Specialist Agent
→ Structured Output
→ Review Agent
→ Review Findings
→ Fix Agent
→ Updated Output
→ PM Agent
```

---

### [핵심]

- Agent Communication은 Agent 간 정보 전달 구조이다.
- 자연어 장문만 전달하면 누락과 오해가 발생한다.
- Source Agent와 Target Agent를 명확히 표시해야 한다.
- Task와 Context를 분리해야 한다.
- Requirements와 Constraints를 분리해야 한다.
- Expected Output을 명확히 지정해야 한다.
- Assumption과 Open Question을 포함해야 한다.
- 실패 상태를 성공처럼 전달하면 안 된다.
- Communication 기록은 Shared State와 연결될 수 있다.
- 좋은 Communication은 다음 Agent가 바로 작업할 수 있게 만든다.

---

### [실무]

2026 실무 기준에서 Agent Communication은 JSON, Markdown Section, Structured Message 형태로 관리한다.

나쁜 Communication 예시:

```text
Backend Agent한테 리뷰 기능 맡겨.
```

문제:

- Source / Target 불명확
- Task 범위 불명확
- Requirements 없음
- Constraints 없음
- Expected Output 없음
- Done Criteria 없음
- Review 기준 없음

좋은 Communication 예시:

```json
{
  "from": "PM Agent",
  "to": "Backend Agent",
  "messageType": "handoff",
  "task": "Design festival review API",
  "requirements": [
    "Authenticated user can create review",
    "User can view review list by festival",
    "Review author can update own review",
    "Review author can delete own review"
  ],
  "constraints": [
    "Spring Boot",
    "JPA",
    "JWT Authentication",
    "ApiResponse format",
    "Use Slice for list response"
  ],
  "expectedOutput": [
    "API Contract",
    "DTO Design",
    "Service Method Plan",
    "Exception Cases",
    "Risks"
  ],
  "doneCriteria": [
    "All endpoints defined",
    "Validation included",
    "Security rule included",
    "Reviewable output generated"
  ]
}
```

---

### [FAQ]

Q. Agent Communication이 뭐야?
A. Multi-Agent System에서 Agent 간 작업 정보, Context, 결과, 실패 상태를 구조화해서 전달하는 방식이다.

Q. Agent Communication이 중요한 이유는?
A. 다음 Agent가 필요한 정보를 정확히 받아야 작업 품질과 일관성이 유지되기 때문이다.

Q. 자연어 장문으로만 전달하면 안 돼?
A. 장문 자연어만 전달하면 요구사항, 제약, 완료 기준이 누락되기 쉽다.

Q. 좋은 Agent Communication 조건은?
A. Source, Target, Task, Context, Requirements, Constraints, Expected Output, Done Criteria가 명확해야 한다.

---

# 2. Message Structure

## 2.1 Message Field Definition

### [개념]

Message Field는 Agent 간 전달 메시지를 구성하는 항목이다.

Message Field는 Agent가 어떤 작업을 누구에게 어떤 기준으로 전달하는지 명확히 하기 위해 사용한다.

기본 Field:

```text
messageId
→ from
→ to
→ messageType
→ task
→ context
→ requirements
→ constraints
→ expectedOutput
→ doneCriteria
→ assumptions
→ openQuestions
```

---

### [핵심]

- messageId는 추적을 위해 사용한다.
- from은 Source Agent이다.
- to는 Target Agent이다.
- messageType은 메시지 종류이다.
- task는 수행할 작업이다.
- context는 작업 배경 정보이다.
- requirements는 해야 할 일이다.
- constraints는 지켜야 할 조건이다.
- expectedOutput은 반환해야 할 결과 형식이다.
- doneCriteria는 완료 기준이다.
- assumptions는 가정한 내용이다.
- openQuestions는 미확정 사항이다.

---

### [실무]

Message Field Template:

```json
{
  "messageId": "MSG-001",
  "from": "PM Agent",
  "to": "SQL Agent",
  "messageType": "handoff",
  "task": "Design review table schema",
  "context": ["Festival review feature", "Users and Festivals entities exist"],
  "requirements": [
    "Store review content",
    "Store rating",
    "Connect review to user and festival"
  ],
  "constraints": ["MySQL", "JPA compatible naming", "Rating range 0 to 5"],
  "expectedOutput": [
    "Table Design",
    "PK / FK",
    "Index Candidates",
    "Data Consistency Risks"
  ],
  "doneCriteria": [
    "PK and FK defined",
    "Index candidates included",
    "Risks included"
  ],
  "assumptions": ["reviews table does not exist yet"],
  "openQuestions": ["Can one user write multiple reviews for same festival?"]
}
```

Message Field 최소 기준:

```text
from
to
messageType
task
requirements
constraints
expectedOutput
doneCriteria
```

---

### [FAQ]

Q. Message Field가 뭐야?
A. Agent 간 메시지를 구성하는 from, to, task, context, requirements, expectedOutput 같은 항목이다.

Q. Message Field가 필요한 이유는?
A. Agent 간 전달 정보를 누락 없이 구조화하기 위해 필요하다.

Q. 최소 Message Field는 뭐야?
A. from, to, messageType, task, requirements, constraints, expectedOutput, doneCriteria다.

Q. messageId는 왜 필요해?
A. Handoff, Agent Output, Review Finding, Fix Result를 추적하기 위해 필요하다.

---

## 2.2 Message Type

### [개념]

Message Type은 Agent 간 전달 메시지의 목적을 구분하는 값이다.

Message Type을 구분하면 PM Agent, Specialist Agent, Review Agent, Fix Agent가 메시지를 다르게 처리할 수 있다.

기본 Message Type:

```text
handoff
result
review_request
review_report
fix_request
fix_result
state_update
clarification_request
approval_request
failure_report
```

---

### [핵심]

- messageType은 메시지 목적을 나타낸다.
- handoff는 작업 전달이다.
- result는 작업 결과이다.
- review_request는 검토 요청이다.
- review_report는 검토 결과이다.
- fix_request는 수정 요청이다.
- fix_result는 수정 결과이다.
- state_update는 Shared State 갱신이다.
- clarification_request는 확인 요청이다.
- approval_request는 사용자 승인 요청이다.
- failure_report는 실패 보고이다.

---

### [실무]

Message Type 예시:

```json
{
  "messageType": "review_request",
  "from": "PM Agent",
  "to": "Review Agent",
  "reviewTarget": "Backend Agent Output",
  "reviewCriteria": [
    "Requirement Match",
    "Domain Rules Compliance",
    "API Contract Consistency",
    "Security Risk"
  ],
  "expectedOutput": [
    "Review Findings",
    "Severity",
    "Fix Direction",
    "Pass / Fail"
  ]
}
```

```json
{
  "messageType": "failure_report",
  "from": "Frontend Agent",
  "to": "PM Agent",
  "status": "blocked",
  "reason": "Backend API Response Field is missing",
  "requiredContext": ["ReviewResDto", "Pagination response format"],
  "safeAlternative": "General component structure only"
}
```

Message Type 처리 기준:

| Message Type     | Primary Receiver  | Purpose        |
| ---------------- | ----------------- | -------------- |
| handoff          | Specialist Agent  | 작업 전달      |
| result           | PM Agent          | 작업 결과 반환 |
| review_request   | Review Agent      | 검토 요청      |
| review_report    | PM / Fix Agent    | 검토 결과 전달 |
| fix_request      | Fix Agent         | 수정 요청      |
| fix_result       | PM / Review Agent | 수정 결과 전달 |
| state_update     | PM Agent          | 상태 갱신      |
| approval_request | User / PM Agent   | 위험 작업 승인 |
| failure_report   | PM Agent          | 실패 상태 전달 |

---

### [FAQ]

Q. Message Type이 뭐야?
A. Agent 간 메시지가 Handoff, Result, Review, Fix, Approval, Failure 중 어떤 목적을 가지는지 구분하는 값이다.

Q. Message Type이 필요한 이유는?
A. 메시지 목적에 따라 수신 Agent가 다르게 처리해야 하기 때문이다.

Q. failure_report는 언제 사용해?
A. Agent가 Missing Context, Tool Failure, Scope Violation 등으로 작업을 완료할 수 없을 때 사용한다.

Q. approval_request는 언제 사용해?
A. 파일 삭제, DB 변경, 배포, 이메일 발송처럼 위험하거나 외부 영향이 있는 작업 전에 사용한다.

---

# 3. Agent Handoff

## 3.1 Handoff Definition

### [개념]

Agent Handoff는 Source Agent가 Target Agent에게 작업 수행에 필요한 정보를 구조화해서 전달하는 메시지이다.

Handoff는 Agent Communication의 핵심이며, Multi-Agent Workflow 품질을 결정한다.

Handoff의 목적은 Target Agent가 추가 추측 없이 작업을 시작할 수 있게 하는 것이다.

기본 Handoff 구조:

```text
Source Agent
→ Target Agent
→ Task
→ Context
→ Requirements
→ Constraints
→ RAG Scope
→ Tool Permission
→ Expected Output
→ Done Criteria
```

---

### [핵심]

- Handoff는 Agent 간 작업 전달이다.
- Handoff는 자연어 요청을 구조화한 결과이다.
- Target Agent를 명확히 지정해야 한다.
- Task는 한 문장으로 설명 가능해야 한다.
- Requirements와 Constraints를 분리해야 한다.
- Context는 필요한 정보만 포함해야 한다.
- RAG Scope를 지정해야 한다.
- Tool Permission을 지정해야 한다.
- Expected Output을 지정해야 한다.
- Done Criteria를 지정해야 한다.
- Assumptions와 Open Questions를 포함해야 한다.

---

### [실무]

Standard Handoff Template:

```json
{
  "handoffId": "H-001",
  "from": "PM Agent",
  "to": "Backend Agent",
  "task": "Design festival review API",
  "context": [
    "Festival review feature",
    "SQL Agent has proposed reviews table",
    "Users and Festivals entities exist"
  ],
  "requirements": [
    "Authenticated user can create review",
    "User can view review list by festival",
    "Review author can update own review",
    "Review author can delete own review"
  ],
  "constraints": [
    "Spring Boot",
    "JPA",
    "JWT Authentication",
    "ApiResponse format",
    "Use Slice for list response"
  ],
  "ragScope": [
    "Java",
    "Spring Boot",
    "JPA Advanced",
    "Security Advanced",
    "API Design"
  ],
  "toolPermission": ["RAG Search", "File Read", "Code Search"],
  "expectedOutput": [
    "API Contract",
    "DTO Design",
    "Service Method Plan",
    "Exception Cases",
    "Security Rules",
    "Risks"
  ],
  "doneCriteria": [
    "All endpoints defined",
    "Request / Response DTO included",
    "Validation included",
    "Security rules included",
    "Exception cases included"
  ],
  "assumptions": ["Authenticated user is resolved from SecurityContext"],
  "openQuestions": [
    "Can one user write multiple reviews for the same festival?"
  ]
}
```

---

### [FAQ]

Q. Agent Handoff가 뭐야?
A. Source Agent가 Target Agent에게 작업 수행에 필요한 Task, Context, Requirements, Constraints 등을 구조화해 전달하는 메시지다.

Q. Handoff의 목적은?
A. Target Agent가 추가 추측 없이 작업을 시작할 수 있게 하는 것이다.

Q. Handoff에는 뭐가 들어가야 해?
A. from, to, task, context, requirements, constraints, ragScope, toolPermission, expectedOutput, doneCriteria, assumptions, openQuestions가 들어가야 한다.

Q. Handoff 품질이 낮으면 어떻게 돼?
A. Specialist Agent가 추측으로 작업하고 Review 단계에서 누락과 충돌이 증가한다.

---

## 3.2 Handoff Quality

### [개념]

Handoff Quality는 Handoff가 Target Agent가 작업을 정확히 수행할 수 있을 만큼 명확하고 완전한지 나타내는 품질 기준이다.

Handoff Quality는 Agent Output 품질, Review 품질, Fix 품질에 직접 영향을 준다.

좋은 Handoff는 작업 범위, 요구사항, 제약, 출력 형식, 완료 기준이 명확하다.

---

### [핵심]

- Handoff Quality는 Multi-Agent 품질의 핵심이다.
- Task가 모호하면 안 된다.
- Context가 부족하면 추측이 증가한다.
- Requirements 누락은 기능 누락으로 이어진다.
- Constraints 누락은 규칙 위반으로 이어진다.
- Expected Output 누락은 비구조화 결과로 이어진다.
- Done Criteria 누락은 완료 판단 실패로 이어진다.
- RAG Scope 누락은 부정확한 Retrieval로 이어진다.
- Tool Permission 누락은 위험 작업 가능성을 높인다.

---

### [실무]

Handoff Quality Checklist:

```md
## Handoff Quality Checklist

- [ ] Source Agent가 명확한가?
- [ ] Target Agent가 명확한가?
- [ ] Task가 명확한가?
- [ ] Task가 Target Agent Scope 안인가?
- [ ] Context가 충분한가?
- [ ] Requirements가 분리되어 있는가?
- [ ] Constraints가 분리되어 있는가?
- [ ] RAG Scope가 지정되었는가?
- [ ] Tool Permission이 지정되었는가?
- [ ] Expected Output이 구체적인가?
- [ ] Done Criteria가 검증 가능한가?
- [ ] Assumptions가 표시되었는가?
- [ ] Open Questions가 표시되었는가?
- [ ] 위험 작업 여부가 표시되었는가?
```

Poor Handoff 예시:

```text
리뷰 기능 백엔드 만들어줘.
```

Good Handoff 예시:

```json
{
  "to": "Backend Agent",
  "task": "Design review create and list API",
  "requirements": [
    "Authenticated user can create review",
    "User can view review list by festival"
  ],
  "constraints": [
    "Use ApiResponse",
    "Use Slice for list response",
    "Rating range 0 to 5"
  ],
  "expectedOutput": [
    "API Contract",
    "DTO",
    "Service Method",
    "Exception Cases"
  ],
  "doneCriteria": [
    "POST and GET endpoints defined",
    "Validation included",
    "Error cases included"
  ]
}
```

---

### [FAQ]

Q. Handoff Quality가 뭐야?
A. Handoff가 Target Agent가 작업을 정확히 수행할 수 있을 만큼 명확하고 완전한지 나타내는 품질 기준이다.

Q. Handoff Quality가 중요한 이유는?
A. Handoff 품질이 낮으면 Agent Output, Review, Fix 품질이 모두 낮아지기 때문이다.

Q. Handoff Quality를 높이려면?
A. Task, Context, Requirements, Constraints, Expected Output, Done Criteria를 명확히 작성해야 한다.

Q. Handoff Quality는 누가 검토해?
A. PM Agent가 전달 전에 검토하고, Review Agent가 Workflow 검토 시 확인할 수 있다.

---

# 4. Communication Context

## 4.1 Context Packaging

### [개념]

Context Packaging은 Target Agent가 작업에 필요한 정보만 받을 수 있도록 Context를 선별, 압축, 구조화하는 작업이다.

모든 대화 기록을 전달하면 Token 낭비와 지시 혼선이 발생할 수 있다.

Context Packaging의 핵심은 필요한 정보는 누락하지 않고, 불필요한 정보는 제거하는 것이다.

기본 구조:

```text
Full Context
→ Filter Relevant Context
→ Compress
→ Attach Source
→ Mark Assumption
→ Pass to Target Agent
```

---

### [핵심]

- Context는 필요한 정보만 전달한다.
- 모든 대화 기록을 전달하지 않는다.
- 요구사항과 결정사항은 반드시 포함한다.
- 관련 없는 정보는 제거한다.
- Context는 Source를 표시하는 것이 좋다.
- 확정 정보와 추정 정보를 구분한다.
- 오래된 Context는 최신 요청보다 후순위다.
- 압축 과정에서 중요한 제약을 삭제하면 안 된다.
- Context 부족은 Hallucination을 유발한다.
- Context 과다는 핵심 지시를 묻히게 한다.

---

### [실무]

Context Packaging Template:

```json
{
  "contextPackageId": "CTX-001",
  "targetAgent": "Frontend Agent",
  "relevantContext": {
    "userRequest": "축제 리뷰 기능을 화면까지 설계",
    "decisions": [
      "Review list uses Slice",
      "Rating range is 0 to 5",
      "ApiResponse format required"
    ],
    "apiContract": [
      "GET /festivals/{festivalId}/reviews",
      "POST /reviews",
      "PATCH /reviews/{reviewId}",
      "DELETE /reviews/{reviewId}"
    ],
    "constraints": ["React", "Axios", "Loading / Error UX required"]
  },
  "excludedContext": [
    "DevOps deployment details",
    "Unrelated payment feature notes"
  ],
  "assumptions": ["ReviewResDto field names are not fully confirmed"],
  "openQuestions": ["Pagination response field name 확인 필요"]
}
```

Context Packaging 실패 예시:

```text
전체 대화 기록 모두 전달
→ Agent가 오래된 결정사항을 최신 요청으로 오해
→ Token 낭비 증가
→ 핵심 요구사항 누락
```

---

### [FAQ]

Q. Context Packaging이 뭐야?
A. Target Agent가 작업에 필요한 정보만 받을 수 있도록 Context를 선별, 압축, 구조화하는 작업이다.

Q. 모든 대화 기록을 넘기면 안 돼?
A. 안 된다. Token 낭비와 지시 혼선이 생기고 오래된 정보가 최신 요청을 덮을 수 있다.

Q. Context Packaging에서 중요한 것은?
A. 요구사항, 결정사항, 제약사항은 유지하고 관련 없는 정보는 제거하는 것이다.

Q. 압축 과정에서 주의할 점은?
A. 중요한 제약, PM Decision, Open Question을 삭제하면 안 된다.

---

## 4.2 Context Conflict

### [개념]

Context Conflict는 Agent에게 전달된 Context 간 내용이 서로 충돌하는 상태이다.

Context Conflict는 오래된 Memory, Shared State, PM Decision, User Request, Agent Output 사이에서 발생할 수 있다.

충돌 예시:

```text
Current User Request:
- 중간 응답 금지

Old Memory:
- 진행 상황을 자주 알려주기

Conflict:
- 현재 요청이 우선
```

---

### [핵심]

- Context Conflict는 명시적으로 처리해야 한다.
- 현재 User Request가 가장 우선이다.
- PM Agent Decision은 Workflow 기준점이다.
- Master Rules와 Domain Rules는 문서 품질 기준이다.
- Shared State는 현재 Workflow 결정사항이다.
- Agent Output은 검토 대상이지 절대 기준이 아니다.
- 오래된 Memory는 보조 정보이다.
- 충돌을 숨기면 Agent 결과가 흔들린다.

---

### [실무]

Context Priority 기준:

```text
Current User Request
→ Explicit PM Agent Decision
→ Master Rules
→ Domain Rules
→ Shared State
→ Current Agent Output
→ Long-term Memory
```

Context Conflict Record:

```md
## Context Conflict

### Conflict

Current User Request는 중간 응답 금지를 요구하지만 이전 운영 규칙은 진행 업데이트를 권장함

### Priority

Current User Request > General Operation Rule

### Decision

중간 응답 없이 최종 결과만 출력

### Impact

RAG 문서 제작 응답에서는 작업 과정 설명 제거
```

Agent Output 충돌 예시:

```md
## Context Conflict

### Conflict

SQL Agent는 reviews.rating을 필수 필드로 제안했지만 Backend Agent DTO에는 rating이 없음

### Priority

Requirement + SQL Agent Output + Shared State > Backend Agent Output

### Decision

Backend Agent Output 수정 필요

### Fix Direction

ReviewCreateReqDto와 ReviewUpdateReqDto에 rating 필드와 Validation 기준 추가
```

---

### [FAQ]

Q. Context Conflict가 뭐야?
A. Agent에게 전달된 User Request, PM Decision, Shared State, Agent Output, Memory가 서로 충돌하는 상태다.

Q. Context Conflict가 발생하면 뭐가 우선이야?
A. 현재 User Request가 가장 우선이고, 그 다음 PM Decision, Master Rules, Domain Rules 순으로 본다.

Q. Agent Output과 Shared State가 충돌하면?
A. Shared State의 명시된 Decision을 우선하고 Agent Output을 수정 대상으로 본다.

Q. Context Conflict는 어떻게 기록해?
A. Conflict, Priority, Decision, Impact, Fix Direction으로 구조화해 기록한다.

---

# 5. Communication Output

## 5.1 Structured Result Message

### [개념]

Structured Result Message는 Agent가 작업을 완료한 뒤 PM Agent 또는 다음 Agent에게 반환하는 구조화된 결과 메시지이다.

Structured Result Message는 작업 결과뿐 아니라 결정사항, 가정, 위험, 미확정 사항, 다음 단계를 포함해야 한다.

기본 구조:

```text
Source Agent
→ Task
→ Status
→ Result
→ Decisions
→ Assumptions
→ Risks
→ Open Questions
→ Next Step
```

---

### [핵심]

- Result Message는 구조화되어야 한다.
- Source Agent를 명확히 표시한다.
- Task를 표시한다.
- Status를 표시한다.
- Result를 명확히 제공한다.
- Decisions를 기록한다.
- Assumptions를 표시한다.
- Risks를 표시한다.
- Open Questions를 표시한다.
- Next Step을 제안한다.
- PM Agent가 Shared State에 반영할 수 있어야 한다.

---

### [실무]

Structured Result Message Template:

```md
## Agent Result

### Source Agent

Backend Agent

### Task

Festival Review API Design

### Status

Completed

### Result

- POST /reviews
- GET /festivals/{festivalId}/reviews
- PATCH /reviews/{reviewId}
- DELETE /reviews/{reviewId}

### Decisions

- Review list uses Slice
- Review author can update/delete own review
- Rating range is 0 to 5

### Assumptions

- Authenticated user is resolved from SecurityContext
- Reviews Entity is linked to Users and Festivals

### Risks

- Duplicate review policy is not confirmed
- Delete policy is not confirmed

### Open Questions

- Can one user write multiple reviews for the same festival?

### Next Step

Review Agent should check API Contract, Security Rules, and DTO consistency
```

상태 값 예시:

| Status         | 의미              |
| -------------- | ----------------- |
| Completed      | 작업 완료         |
| Partial        | 일부 완료         |
| Blocked        | 필수 Context 부족 |
| Failed         | 작업 실패         |
| Needs Review   | 검토 필요         |
| Needs Approval | 사용자 승인 필요  |

---

### [FAQ]

Q. Structured Result Message가 뭐야?
A. Agent가 작업을 완료한 뒤 결과, 결정사항, 가정, 위험, 다음 단계를 구조화해 반환하는 메시지다.

Q. Result Message에는 뭐가 들어가야 해?
A. Source Agent, Task, Status, Result, Decisions, Assumptions, Risks, Open Questions, Next Step이 들어가야 한다.

Q. Status가 필요한 이유는?
A. PM Agent가 작업 완료, 부분 완료, 실패, 승인 필요 상태를 구분하기 위해 필요하다.

Q. Result Message는 Shared State와 연결돼?
A. 연결된다. PM Agent는 Result Message의 Decisions, Risks, Open Questions를 Shared State에 반영할 수 있다.

---

## 5.2 Failure Message

### [개념]

Failure Message는 Agent가 작업을 완료할 수 없을 때 실패 상태, 실패 원인, 필요한 Context, 안전한 대안, 다음 조치를 전달하는 메시지이다.

Failure Message는 실패를 숨기지 않고 Workflow가 안전하게 중단, 재시도, 재분기될 수 있게 만든다.

기본 구조:

```text
Source Agent
→ Status
→ Failure Type
→ Reason
→ Required Context
→ Safe Alternative
→ Suggested Action
```

---

### [핵심]

- Failure Message는 실패 상태를 명확히 전달한다.
- 실패를 성공처럼 전달하면 안 된다.
- Failure Type을 표시한다.
- Reason을 설명한다.
- Required Context를 표시한다.
- Safe Alternative를 제공할 수 있다.
- Suggested Action을 포함한다.
- 위험 작업은 중단하고 Approval을 요청한다.
- PM Agent가 재시도, 재분기, 중단을 판단할 수 있어야 한다.

---

### [실무]

Failure Message Template:

```md
## Failure Message

### Source Agent

Frontend Agent

### Status

Blocked

### Failure Type

Missing Context

### Task

Design review UI integration

### Reason

Backend API Response Field가 확정되지 않아 정확한 State 구조를 설계할 수 없음

### Required Context

- ReviewResDto fields
- Pagination response format
- Error response format

### Safe Alternative

일반적인 ReviewList / ReviewForm Component 구조만 제안 가능

### Suggested Action

PM Agent가 Backend Agent Output을 보강한 뒤 Frontend Agent에 재전달
```

Failure Type 예시:

| Failure Type          | 의미                    |
| --------------------- | ----------------------- |
| Missing Context       | 필요한 정보 부족        |
| Scope Violation       | Agent Scope 밖 요청     |
| Tool Failure          | Tool 실행 실패          |
| Permission Required   | 승인 필요               |
| RAG Retrieval Failure | 관련 문서 검색 실패     |
| Conflict Detected     | Context / Decision 충돌 |
| Invalid Input         | 입력 형식 문제          |
| Unsafe Action         | 위험 작업 포함          |

---

### [FAQ]

Q. Failure Message가 뭐야?
A. Agent가 작업을 완료할 수 없을 때 실패 상태, 원인, 필요한 Context, 다음 조치를 전달하는 메시지다.

Q. 실패를 그냥 생략하면 안 돼?
A. 안 된다. 실패를 숨기면 다음 Agent가 잘못된 상태를 기준으로 작업한다.

Q. Failure Message에는 뭐가 들어가야 해?
A. Source Agent, Status, Failure Type, Reason, Required Context, Safe Alternative, Suggested Action이 들어가야 한다.

Q. Failure Message는 누가 사용해?
A. PM Agent가 재시도, 재분기, 사용자 확인, 중단 여부를 판단하는 데 사용한다.

---

# 6. Communication and Shared State

## 6.1 State Update Message

### [개념]

State Update Message는 Agent Communication 결과를 Shared State에 반영하기 위한 메시지이다.

State Update Message는 요구사항, 결정사항, Agent Output, Review Findings, Fix Result, Open Questions, Status를 최신 상태로 관리한다.

기본 구조:

```text
Agent Result
→ State Update Message
→ Shared State Update
→ Next Agent Reference
```

---

### [핵심]

- State Update Message는 Shared State 갱신용 메시지이다.
- PM Agent가 주로 관리한다.
- 결정사항을 기록한다.
- Agent Output 요약을 기록한다.
- Review Findings를 기록한다.
- Fix Result를 기록한다.
- Open Questions를 기록한다.
- 현재 Step과 Status를 갱신한다.
- 오래된 State가 최신 요청을 덮어쓰면 안 된다.

---

### [실무]

State Update Message Template:

```json
{
  "messageType": "state_update",
  "from": "PM Agent",
  "targetState": "workflowState",
  "updates": {
    "status": "review_required",
    "currentStep": "backend_output_completed",
    "decisions": [
      "Review list uses Slice",
      "Rating range is 0 to 5",
      "Review author can update/delete own review"
    ],
    "agentOutputs": {
      "Backend Agent": "Festival Review API Contract Draft"
    },
    "risks": ["Duplicate review policy not confirmed"],
    "openQuestions": [
      "Can one user write multiple reviews for the same festival?"
    ]
  }
}
```

Shared State 업데이트 시점:

```text
Requirement Analysis 완료
→ requirements / constraints 업데이트

Agent Result 수신
→ agentOutputs / decisions / risks 업데이트

Review Report 수신
→ reviewFindings / status 업데이트

Fix Result 수신
→ decisions / finalOutput / regressionRisk 업데이트
```

---

### [FAQ]

Q. State Update Message가 뭐야?
A. Agent Communication 결과를 Shared State에 반영하기 위한 메시지다.

Q. State Update Message에는 뭐가 들어가?
A. status, currentStep, decisions, agentOutputs, reviewFindings, risks, openQuestions가 들어간다.

Q. State Update는 누가 관리해?
A. 일반적으로 PM Agent가 관리한다.

Q. Shared State 업데이트가 중요한 이유는?
A. 다음 Agent가 최신 요구사항과 결정사항을 기준으로 작업할 수 있게 하기 위해서다.

---

## 6.2 Communication Trace

### [개념]

Communication Trace는 Agent 간 메시지 흐름을 추적하기 위한 기록이다.

Communication Trace는 어떤 Agent가 어떤 정보를 전달했고, 어떤 결과가 생성되었으며, 어디서 실패했는지 확인하는 데 사용한다.

기본 구조:

```text
Message ID
→ Source Agent
→ Target Agent
→ Message Type
→ Status
→ Timestamp
→ Related State
```

---

### [핵심]

- Communication Trace는 Agent 간 메시지 추적 기록이다.
- 문제 발생 시 실패 지점을 찾는 데 유용하다.
- messageId와 handoffId를 사용할 수 있다.
- Agent Output과 Review Finding을 연결할 수 있다.
- Fix Result와 Review Finding을 연결할 수 있다.
- Tool 사용 기록과 연결할 수 있다.
- 과도한 Trace 저장은 Token 낭비가 될 수 있다.
- 중요한 결정과 실패 중심으로 기록한다.

---

### [실무]

Communication Trace 예시:

```json
{
  "traceId": "TRACE-001",
  "messages": [
    {
      "messageId": "MSG-001",
      "from": "PM Agent",
      "to": "SQL Agent",
      "messageType": "handoff",
      "status": "sent"
    },
    {
      "messageId": "MSG-002",
      "from": "SQL Agent",
      "to": "PM Agent",
      "messageType": "result",
      "status": "completed"
    },
    {
      "messageId": "MSG-003",
      "from": "PM Agent",
      "to": "Backend Agent",
      "messageType": "handoff",
      "status": "sent"
    },
    {
      "messageId": "MSG-004",
      "from": "Backend Agent",
      "to": "PM Agent",
      "messageType": "result",
      "status": "completed"
    },
    {
      "messageId": "MSG-005",
      "from": "PM Agent",
      "to": "Review Agent",
      "messageType": "review_request",
      "status": "sent"
    }
  ]
}
```

Trace 활용:

```text
Review Finding 발생
→ 관련 Handoff 확인
→ 관련 Agent Output 확인
→ 원인 위치 확인
→ Fix Agent에게 정확한 수정 대상 전달
```

---

### [FAQ]

Q. Communication Trace가 뭐야?
A. Agent 간 메시지 흐름과 상태를 추적하기 위한 기록이다.

Q. Communication Trace가 필요한 이유는?
A. 실패 지점, 잘못된 Handoff, Agent Output 충돌 원인을 추적하기 위해 필요하다.

Q. 모든 대화를 Trace로 저장해야 해?
A. 아니다. 중요한 Handoff, 결정사항, 실패, Review Finding 중심으로 저장하는 것이 좋다.

Q. Trace는 Fix Agent에도 도움이 돼?
A. 도움이 된다. 어떤 Handoff와 Output에서 문제가 생겼는지 확인할 수 있다.

---

# 7. Communication Failure Handling

## 7.1 Communication Failure Cases

### [개념]

Communication Failure는 Agent 간 정보 전달이 누락, 왜곡, 충돌, 실패 상태 은폐로 인해 Workflow 품질을 떨어뜨리는 문제이다.

Communication Failure는 Multi-Agent System의 대표적인 실패 원인이다.

주요 실패 유형:

```text
Missing Requirement
Missing Constraint
Wrong Target Agent
Ambiguous Task
Unstructured Message
Context Overload
Context Loss
Hidden Failure
Stale State
Decision Conflict
```

---

### [핵심]

- 요구사항 누락은 기능 누락으로 이어진다.
- 제약사항 누락은 규칙 위반으로 이어진다.
- Target Agent 오류는 잘못된 Output으로 이어진다.
- Task가 모호하면 Agent가 추측한다.
- 비구조화 메시지는 Review와 Fix가 어렵다.
- Context 과다는 핵심 지시를 묻히게 한다.
- Context 손실은 Hallucination을 유발한다.
- 실패를 숨기면 다음 Agent가 오판한다.
- 오래된 State는 최신 요청과 충돌할 수 있다.
- 결정사항 충돌은 PM Agent가 정리해야 한다.

---

### [실무]

Communication Failure 대응 기준:

| Failure Type         | Cause                | Handling                         |
| -------------------- | -------------------- | -------------------------------- |
| Missing Requirement  | Handoff 누락         | PM Agent가 Handoff 재작성        |
| Missing Constraint   | 제약 누락            | Constraints 추가 후 재전달       |
| Wrong Target Agent   | Routing 오류         | PM Agent 재분석                  |
| Ambiguous Task       | Task 불명확          | Task를 실행 가능한 단위로 재작성 |
| Unstructured Message | Template 미사용      | Message Template 적용            |
| Context Overload     | 전체 대화 전달       | Context Packaging 적용           |
| Context Loss         | 중요 결정 누락       | Shared State 확인 후 보강        |
| Hidden Failure       | 실패를 성공처럼 전달 | Failure Message 작성             |
| Stale State          | 오래된 정보 사용     | Current User Request 우선        |
| Decision Conflict    | Agent 결과 충돌      | PM Agent Decision 기록           |

Communication Failure Output 예시:

```md
## Communication Failure

### Failure Type

Missing Constraint

### Issue

Backend Agent Handoff에 ApiResponse Format 제약이 누락됨

### Impact

Backend Agent Output이 기존 응답 규칙과 맞지 않을 수 있음

### Fix Direction

PM Agent가 Constraints에 ApiResponse Format을 추가하고 Backend Agent에게 Handoff 재전달

### Re-review Required

Yes
```

---

### [FAQ]

Q. Communication Failure가 뭐야?
A. Agent 간 정보 전달이 누락, 왜곡, 충돌, 실패 은폐로 인해 Workflow 품질을 떨어뜨리는 문제다.

Q. Communication Failure의 대표 원인은?
A. Missing Requirement, Missing Constraint, Wrong Target Agent, Ambiguous Task, Hidden Failure, Stale State다.

Q. 실패를 성공처럼 전달하면 왜 위험해?
A. 다음 Agent가 잘못된 상태를 기준으로 작업해 오류가 전파되기 때문이다.

Q. Communication Failure는 어떻게 줄여?
A. Handoff Template, Context Packaging, Failure Message, Shared State Update, Review Check를 적용한다.

---

## 7.2 Handoff Failure

### [개념]

Handoff Failure는 Handoff 메시지가 Target Agent에게 충분한 작업 정보를 제공하지 못해 Agent Output 품질이 낮아지는 문제이다.

Handoff Failure는 PM Agent의 Task Decomposition, Context Packaging, Expected Output 정의가 부실할 때 자주 발생한다.

주요 원인:

```text
Unclear Task
Missing Requirements
Missing Constraints
Missing Context
No Expected Output
No Done Criteria
No RAG Scope
No Tool Permission
No Open Questions
```

---

### [핵심]

- Handoff Failure는 Agent Output 실패로 이어진다.
- Task가 모호하면 Target Agent가 추측한다.
- Requirements가 없으면 기능이 누락된다.
- Constraints가 없으면 규칙 위반이 발생한다.
- Context가 없으면 Hallucination 가능성이 커진다.
- Expected Output이 없으면 결과 구조가 흔들린다.
- Done Criteria가 없으면 완료 판단이 불가능하다.
- RAG Scope가 없으면 검색 품질이 떨어진다.
- Open Question이 없으면 불확실한 내용이 확정처럼 전달된다.

---

### [실무]

Handoff Failure Review Checklist:

```md
## Handoff Failure Review Checklist

- [ ] Task가 명확한가?
- [ ] Target Agent가 올바른가?
- [ ] Requirements가 누락되지 않았는가?
- [ ] Constraints가 누락되지 않았는가?
- [ ] Context가 충분한가?
- [ ] Expected Output이 명확한가?
- [ ] Done Criteria가 있는가?
- [ ] RAG Scope가 지정되었는가?
- [ ] Tool Permission이 지정되었는가?
- [ ] Assumptions가 표시되었는가?
- [ ] Open Questions가 표시되었는가?
```

Handoff Failure 예시:

```md
## Handoff Failure

### Failure Type

No Done Criteria

### Issue

Frontend Agent Handoff에 완료 기준이 없음

### Impact

Frontend Agent가 Component 구조만 작성하고 Loading / Error UX를 누락할 수 있음

### Fix Direction

Done Criteria에 Component, State, API Call Flow, Loading / Error / Empty State 포함

### Updated Handoff Needed

Yes
```

---

### [FAQ]

Q. Handoff Failure가 뭐야?
A. Handoff 메시지가 Target Agent에게 충분한 작업 정보를 제공하지 못해 Output 품질이 낮아지는 문제다.

Q. Handoff Failure의 대표 원인은?
A. 불명확한 Task, Requirements 누락, Constraints 누락, Expected Output 누락, Done Criteria 누락이다.

Q. Handoff Failure는 누가 고쳐야 해?
A. 일반적으로 PM Agent가 Handoff를 재작성하고 Target Agent에게 재전달해야 한다.

Q. Handoff Failure를 막으려면?
A. Handoff Quality Checklist를 적용하고 Review Agent가 Handoff 품질도 검토해야 한다.

---

# 8. Communication Checklist

## 8.1 Agent Communication Checklist

### [개념]

Agent Communication Checklist는 Agent 간 메시지가 작업에 충분한 정보를 포함하는지 검수하는 기준이다.

이 Checklist는 PM Agent, Router Agent, Planner Agent, Specialist Agent, Review Agent가 모두 사용할 수 있다.

---

### [핵심]

- Source Agent를 확인한다.
- Target Agent를 확인한다.
- Message Type을 확인한다.
- Task를 확인한다.
- Context를 확인한다.
- Requirements를 확인한다.
- Constraints를 확인한다.
- Expected Output을 확인한다.
- Done Criteria를 확인한다.
- Assumptions를 확인한다.
- Open Questions를 확인한다.
- Status를 확인한다.
- Failure가 숨겨지지 않았는지 확인한다.

---

### [실무]

Agent Communication Checklist:

```md
## Agent Communication Checklist

- [ ] Source Agent가 명확한가?
- [ ] Target Agent가 명확한가?
- [ ] Message Type이 명확한가?
- [ ] Task가 명확한가?
- [ ] Context가 필요한 만큼 포함되었는가?
- [ ] Requirements가 분리되어 있는가?
- [ ] Constraints가 분리되어 있는가?
- [ ] RAG Scope가 필요한 경우 포함되었는가?
- [ ] Tool Permission이 필요한 경우 포함되었는가?
- [ ] Expected Output이 명확한가?
- [ ] Done Criteria가 검증 가능한가?
- [ ] Assumptions가 표시되었는가?
- [ ] Open Questions가 표시되었는가?
- [ ] Status가 표시되었는가?
- [ ] 실패 상태가 숨겨지지 않았는가?
- [ ] Shared State 업데이트가 필요한가?
```

---

### [FAQ]

Q. Agent Communication Checklist가 뭐야?
A. Agent 간 메시지가 작업에 충분한 정보를 포함하는지 검수하는 기준이다.

Q. Communication Checklist는 누가 사용해?
A. PM Agent, Router Agent, Planner Agent, Specialist Agent, Review Agent가 모두 사용할 수 있다.

Q. Checklist에서 가장 중요한 것은?
A. Source, Target, Task, Requirements, Constraints, Expected Output, Done Criteria, Status다.

Q. 실패 상태도 Checklist에서 확인해야 해?
A. 해야 한다. 실패 상태를 숨기면 다음 Agent가 잘못된 기준으로 작업한다.

---

## 8.2 RAG Document Communication Rules

### [개념]

RAG Document Communication Rules는 RAG 문서 제작 Workflow에서 Agent 간 전달해야 하는 정보를 정의하는 규칙이다.

RAG 문서 제작에서는 MASTER_RAG_RULES, DOMAIN_RULES, PROJECT_PROGRESS, Target Part Topic, Output Format이 Handoff에 반드시 포함되어야 한다.

기본 구조:

```text
PM Agent
→ Documentation Agent
→ Review Agent
→ Fix Agent
→ Final RAG Document
```

---

### [핵심]

- RAG 문서 제작 Handoff에는 Master Rules가 포함되어야 한다.
- Target Domain Rules가 포함되어야 한다.
- Project Progress는 참고 정보로 사용한다.
- Target Part Topic을 명확히 지정해야 한다.
- Output Format을 지켜야 한다.
- Required Section을 포함해야 한다.
- FAQ 강화 기준을 포함해야 한다.
- Retrieval Queries 필수 조건을 포함해야 한다.
- 중간 응답 금지 같은 사용자 요청이 있으면 최우선으로 반영한다.

---

### [실무]

RAG Document Handoff Template:

```json
{
  "from": "PM Agent",
  "to": "Documentation Agent",
  "messageType": "handoff",
  "task": "Create Multi-Agent System Part08 - Agent Communication and Handoff",
  "rules": [
    "Apply MASTER_RAG_RULES",
    "Apply Multi-Agent System Domain Rules",
    "Reference PROJECT_PROGRESS"
  ],
  "outputFormat": [
    "writing block only",
    "# FileName",
    "# Document Title",
    "Required Sections",
    "Retrieval Queries"
  ],
  "requirements": [
    "RAG Retrieval optimized document",
    "Not human essay",
    "Use [개념], [핵심], [실무], [FAQ]",
    "Strengthen FAQ",
    "Unify terminology",
    "Minimize typo and duplication"
  ],
  "constraints": [
    "No intermediate response",
    "Output final result only",
    "No random separators inside FAQ",
    "Use Markdown"
  ],
  "doneCriteria": [
    "Required Section included",
    "Retrieval Queries included",
    "FAQ Q/A format included",
    "Agent Communication and Handoff covered",
    "Critical structure issue absent"
  ]
}
```

RAG Communication Failure 예시:

```md
## RAG Communication Failure

### Failure Type

Output Format Violation

### Issue

Documentation Agent returned explanation outside writing block

### Impact

User-required RAG document output format was violated

### Fix Direction

Remove external explanation and output only the writing block document
```

---

### [FAQ]

Q. RAG Document Communication Rules가 뭐야?
A. RAG 문서 제작 Workflow에서 Agent 간 전달해야 하는 Rules, Topic, Output Format, Requirements를 정의하는 규칙이다.

Q. RAG 문서 Handoff에 반드시 들어가야 하는 것은?
A. MASTER_RAG_RULES, Target DOMAIN_RULES, PROJECT_PROGRESS, Target Part Topic, Output Format, Done Criteria다.

Q. RAG 문서 제작에서 현재 사용자 요청은 어디에 반영해?
A. Handoff Constraints와 Output Format에 최우선으로 반영한다.

Q. RAG Communication Failure 예시는?
A. Writing Block 밖 설명 출력, Retrieval Queries 누락, Required Section 누락, FAQ 형식 위반이 있다.

---

# Retrieval Queries

### [FAQ]

Q. Agent Communication이 뭐야?
A. Multi-Agent System에서 Agent 간 작업 정보, Context, 결과, 실패 상태를 구조화해서 전달하는 방식이다.

Q. Agent Communication이 중요한 이유는?
A. 다음 Agent가 필요한 정보를 정확히 받아야 작업 품질과 일관성이 유지되기 때문이다.

Q. Agent 간 자연어 장문만 전달하면 안 되는 이유는?
A. 요구사항, 제약, 완료 기준이 누락되기 쉽고 다음 Agent가 추측으로 작업할 수 있기 때문이다.

Q. 좋은 Agent Communication 조건은?
A. Source, Target, Task, Context, Requirements, Constraints, Expected Output, Done Criteria가 명확해야 한다.

Q. Message Field가 뭐야?
A. Agent 간 메시지를 구성하는 from, to, task, context, requirements, expectedOutput 같은 항목이다.

Q. Agent Communication 최소 Field는?
A. from, to, messageType, task, requirements, constraints, expectedOutput, doneCriteria다.

Q. Message Type이 뭐야?
A. Agent 간 메시지가 Handoff, Result, Review, Fix, Approval, Failure 중 어떤 목적을 가지는지 구분하는 값이다.

Q. messageType 종류는 뭐가 있어?
A. handoff, result, review_request, review_report, fix_request, fix_result, state_update, clarification_request, approval_request, failure_report가 있다.

Q. failure_report는 언제 사용해?
A. Agent가 Missing Context, Tool Failure, Scope Violation 등으로 작업을 완료할 수 없을 때 사용한다.

Q. approval_request는 언제 사용해?
A. 파일 삭제, DB 변경, 배포, 이메일 발송처럼 위험하거나 외부 영향이 있는 작업 전에 사용한다.

Q. Agent Handoff가 뭐야?
A. Source Agent가 Target Agent에게 작업 수행에 필요한 Task, Context, Requirements, Constraints 등을 구조화해 전달하는 메시지다.

Q. Handoff의 목적은?
A. Target Agent가 추가 추측 없이 작업을 시작할 수 있게 하는 것이다.

Q. Handoff에는 뭐가 들어가야 해?
A. from, to, task, context, requirements, constraints, ragScope, toolPermission, expectedOutput, doneCriteria, assumptions, openQuestions가 들어가야 한다.

Q. Handoff Quality가 뭐야?
A. Handoff가 Target Agent가 작업을 정확히 수행할 수 있을 만큼 명확하고 완전한지 나타내는 품질 기준이다.

Q. Handoff Quality가 낮으면 어떻게 돼?
A. Specialist Agent가 추측으로 작업하고 Review 단계에서 누락과 충돌이 증가한다.

Q. Context Packaging이 뭐야?
A. Target Agent가 작업에 필요한 정보만 받을 수 있도록 Context를 선별, 압축, 구조화하는 작업이다.

Q. 모든 대화 기록을 Agent에게 넘기면 안 되는 이유는?
A. Token 낭비와 지시 혼선이 생기고 오래된 정보가 최신 요청을 덮을 수 있기 때문이다.

Q. Context Packaging에서 중요한 것은?
A. 요구사항, 결정사항, 제약사항은 유지하고 관련 없는 정보는 제거하는 것이다.

Q. Context Conflict가 뭐야?
A. Agent에게 전달된 User Request, PM Decision, Shared State, Agent Output, Memory가 서로 충돌하는 상태다.

Q. Context Conflict가 발생하면 뭐가 우선이야?
A. 현재 User Request가 가장 우선이고, 그 다음 PM Decision, Master Rules, Domain Rules 순으로 본다.

Q. Structured Result Message가 뭐야?
A. Agent가 작업을 완료한 뒤 결과, 결정사항, 가정, 위험, 다음 단계를 구조화해 반환하는 메시지다.

Q. Result Message에는 뭐가 들어가야 해?
A. Source Agent, Task, Status, Result, Decisions, Assumptions, Risks, Open Questions, Next Step이 들어가야 한다.

Q. Failure Message가 뭐야?
A. Agent가 작업을 완료할 수 없을 때 실패 상태, 원인, 필요한 Context, 다음 조치를 전달하는 메시지다.

Q. 실패를 숨기면 안 되는 이유는?
A. 다음 Agent가 잘못된 상태를 기준으로 작업해 오류가 전파되기 때문이다.

Q. Failure Message에는 뭐가 들어가야 해?
A. Source Agent, Status, Failure Type, Reason, Required Context, Safe Alternative, Suggested Action이 들어가야 한다.

Q. State Update Message가 뭐야?
A. Agent Communication 결과를 Shared State에 반영하기 위한 메시지다.

Q. State Update Message에는 뭐가 들어가?
A. status, currentStep, decisions, agentOutputs, reviewFindings, risks, openQuestions가 들어간다.

Q. Communication Trace가 뭐야?
A. Agent 간 메시지 흐름과 상태를 추적하기 위한 기록이다.

Q. Communication Trace가 필요한 이유는?
A. 실패 지점, 잘못된 Handoff, Agent Output 충돌 원인을 추적하기 위해 필요하다.

Q. 모든 대화를 Trace로 저장해야 해?
A. 아니다. 중요한 Handoff, 결정사항, 실패, Review Finding 중심으로 저장하는 것이 좋다.

Q. Communication Failure가 뭐야?
A. Agent 간 정보 전달이 누락, 왜곡, 충돌, 실패 은폐로 인해 Workflow 품질을 떨어뜨리는 문제다.

Q. Communication Failure의 대표 원인은?
A. Missing Requirement, Missing Constraint, Wrong Target Agent, Ambiguous Task, Hidden Failure, Stale State다.

Q. Communication Failure는 어떻게 줄여?
A. Handoff Template, Context Packaging, Failure Message, Shared State Update, Review Check를 적용한다.

Q. Handoff Failure가 뭐야?
A. Handoff 메시지가 Target Agent에게 충분한 작업 정보를 제공하지 못해 Output 품질이 낮아지는 문제다.

Q. Handoff Failure의 대표 원인은?
A. 불명확한 Task, Requirements 누락, Constraints 누락, Expected Output 누락, Done Criteria 누락이다.

Q. Handoff Failure는 누가 고쳐야 해?
A. 일반적으로 PM Agent가 Handoff를 재작성하고 Target Agent에게 재전달해야 한다.

Q. Agent Communication Checklist가 뭐야?
A. Agent 간 메시지가 작업에 충분한 정보를 포함하는지 검수하는 기준이다.

Q. RAG Document Communication Rules가 뭐야?
A. RAG 문서 제작 Workflow에서 Agent 간 전달해야 하는 Rules, Topic, Output Format, Requirements를 정의하는 규칙이다.

Q. RAG 문서 Handoff에 반드시 들어가야 하는 것은?
A. MASTER_RAG_RULES, Target DOMAIN_RULES, PROJECT_PROGRESS, Target Part Topic, Output Format, Done Criteria다.

Q. RAG Communication Failure 예시는?
A. Writing Block 밖 설명 출력, Retrieval Queries 누락, Required Section 누락, FAQ 형식 위반이 있다.

Q. 개인 AI 개발팀에서 Agent Communication은 어디에 쓰여?
A. PM Agent Handoff, Specialist Agent Output, Review Report, Fix Result, Shared State Update에 사용된다.
