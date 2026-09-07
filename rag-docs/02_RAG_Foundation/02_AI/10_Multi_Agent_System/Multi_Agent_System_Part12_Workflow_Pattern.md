# Multi-Agent System Part12 - Workflow Pattern

---

# 1. Workflow Pattern Core

## 1.1 Workflow Pattern Definition

### [개념]

Workflow Pattern은 Multi-Agent System에서 Agent들이 어떤 순서와 조건으로 협업하는지 정의한 실행 구조이다.

Workflow Pattern은 Agent Role, Handoff, Shared State, RAG Scope, Tool Permission, Review-Fix 기준을 연결해 하나의 작업 흐름을 만든다.

Workflow Pattern의 목적은 사용자 요청의 복잡도, Domain 수, 위험도, Review 필요 여부에 따라 적절한 Agent 실행 구조를 선택하는 것이다.

기본 구조:

```text
User Request
→ Workflow Pattern Selection
→ Agent Execution
→ Review / Fix
→ Final Output
```

개인 AI 개발팀 기준 기본 구조:

```text
User
→ PM Agent
→ Specialist Agent
→ Review Agent
→ Fix Agent
→ PM Agent Final Integration
```

---

### [핵심]

- Workflow Pattern은 Agent 협업 실행 구조이다.
- 모든 요청에 같은 Workflow를 사용하면 비효율적이다.
- 단순 요청은 단순 Workflow로 처리한다.
- 복합 요청은 여러 Agent로 분해한다.
- 의존성이 있는 작업은 순차 실행한다.
- 위험 Tool이 포함되면 Human Approval 절차를 포함한다.
- 품질 검토가 필요하면 Review-Fix 구조를 포함한다.
- Workflow Pattern은 Shared State에 기록할 수 있다.
- Pattern 선택은 PM Agent가 담당하는 것이 안정적이다.
- Part07은 Router, Planner, Executor 역할 자체를 다루고, Part12는 실행 흐름 Pattern을 다룬다.

---

### [실무]

Workflow Pattern 선택 기준:

```text
Request Complexity
→ Domain Count
→ Dependency
→ Risk Level
→ Tool Permission
→ Review Need
→ Approval Need
→ Workflow Pattern
```

주요 Workflow Pattern:

| Pattern                               | 사용 상황                      |
| ------------------------------------- | ------------------------------ |
| Single Agent Workflow                 | 단순 질문, 개념 설명           |
| PM-Specialist Workflow                | 단일 Domain 작업               |
| Sequential Workflow                   | 의존성이 있는 복합 작업        |
| Router-based Workflow                 | 요청 Domain 분기가 필요한 경우 |
| Review-Fix Workflow                   | 품질 검토와 수정이 필요한 경우 |
| Human-in-the-Loop Workflow            | 위험 Tool 또는 승인 필요 작업  |
| RAG Document Workflow                 | RAG 문서 제작 / 검수 / 수정    |
| Personal AI Development Team Workflow | 개인 개발팀형 통합 Workflow    |

Workflow Pattern Selection 예시:

```json
{
  "userRequest": "리뷰 기능 DB부터 화면까지 설계해줘",
  "complexity": "medium",
  "domainCount": 3,
  "dependencies": [
    "DB schema before Backend API",
    "Backend API before Frontend integration"
  ],
  "riskLevel": "medium",
  "reviewRequired": true,
  "approvalRequired": false,
  "selectedPattern": "Sequential Workflow"
}
```

---

### [FAQ]

Q. Workflow Pattern이 뭐야?
A. Multi-Agent System에서 Agent들이 어떤 순서와 조건으로 협업하는지 정의한 실행 구조다.

Q. Workflow Pattern이 필요한 이유는?
A. 요청 유형마다 필요한 Agent, 실행 순서, Review, 승인 기준이 다르기 때문이다.

Q. Part07과 Part12 차이는 뭐야?
A. Part07은 Router, Planner, Executor 역할 자체를 다루고, Part12는 Agent 실행 흐름의 Pattern을 다룬다.

Q. Workflow Pattern은 누가 선택해?
A. 일반적으로 PM Agent가 사용자 요청을 분석해 선택한다.

---

# 2. Single Agent Workflow

## 2.1 Single Agent Workflow Definition

### [개념]

Single Agent Workflow는 하나의 Agent가 요청을 분석하고 응답까지 처리하는 가장 단순한 Workflow Pattern이다.

단순 질문, 개념 설명, 위험도 낮은 단일 응답에 적합하다.

기본 구조:

```text
User Request
→ Single Agent
→ Final Answer
```

PM Agent 중심 구조:

```text
User Request
→ PM Agent
→ Direct Answer
```

---

### [핵심]

- Single Agent Workflow는 가장 단순한 실행 흐름이다.
- Handoff가 필요하지 않다.
- Shared State가 거의 필요하지 않다.
- Latency가 낮다.
- 단순 개념 설명에 적합하다.
- 복합 Domain 작업에는 부적합하다.
- Review-Fix가 필요한 작업에는 부적합하다.
- 위험 Tool 실행이 포함된 작업에는 부적합하다.

---

### [실무]

적합한 요청:

```text
"PM Agent가 뭐야?"
"Review Agent와 Fix Agent 차이가 뭐야?"
"RAG Scope가 뭐야?"
"Workflow Pattern이 뭐야?"
```

부적합한 요청:

```text
"DB부터 Frontend까지 기능 설계해줘"
"문서 검수하고 수정까지 해줘"
"배포까지 실행해줘"
"코드 수정하고 테스트까지 해줘"
```

Single Agent Output 기준:

```md
## Answer

<질문에 대한 직접 답변>

## Key Points

- <핵심 1>
- <핵심 2>

## Related Concepts

- <관련 개념>
```

---

### [FAQ]

Q. Single Agent Workflow가 뭐야?
A. 하나의 Agent가 요청을 분석하고 응답까지 처리하는 가장 단순한 Workflow다.

Q. Single Agent Workflow는 언제 사용해?
A. 단순 질문, 개념 설명, 위험도 낮은 단일 응답에 사용한다.

Q. Single Agent Workflow의 장점은?
A. 구조가 단순하고 응답이 빠르다.

Q. Single Agent Workflow의 한계는?
A. 복합 Domain 작업, Review-Fix 작업, 위험 Tool 작업에는 부적합하다.

---

# 3. PM-Specialist Workflow

## 3.1 PM-Specialist Workflow Definition

### [개념]

PM-Specialist Workflow는 PM Agent가 사용자 요청을 분석하고 하나의 Specialist Agent에게 작업을 전달한 뒤 결과를 통합하는 Workflow Pattern이다.

단일 Domain 작업이지만 요구사항 분석, Handoff, 결과 정리가 필요한 경우에 사용한다.

기본 구조:

```text
User Request
→ PM Agent
→ Handoff
→ Specialist Agent
→ Specialist Output
→ PM Agent
→ Final Output
```

---

### [핵심]

- PM Agent가 요청을 분석한다.
- PM Agent가 Target Specialist Agent를 선택한다.
- PM Agent가 Handoff를 생성한다.
- Specialist Agent가 Domain 작업을 수행한다.
- PM Agent가 결과를 정리한다.
- 단일 Domain 작업에 적합하다.
- Review가 필요하면 Review Agent를 추가한다.
- 복합 Domain 작업이면 Sequential Workflow로 확장한다.

---

### [실무]

PM-Specialist Workflow 적용 예시:

| 요청                      | Target Specialist   |
| ------------------------- | ------------------- |
| SQL Query 설계            | SQL Agent           |
| Spring Boot API 설계      | Backend Agent       |
| React Component 구조 설계 | Frontend Agent      |
| Docker Compose 검토       | DevOps Agent        |
| Prompt Template 설계      | AI Agent            |
| RAG 문서 작성             | Documentation Agent |

Handoff 예시:

```json
{
  "from": "PM Agent",
  "to": "Backend Agent",
  "workflowPattern": "PM-Specialist",
  "task": "Design review API",
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
    "Use Slice"
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
    "Security rule included"
  ]
}
```

---

### [FAQ]

Q. PM-Specialist Workflow가 뭐야?
A. PM Agent가 요청을 분석하고 하나의 Specialist Agent에게 작업을 전달한 뒤 결과를 통합하는 Workflow다.

Q. PM-Specialist Workflow는 언제 사용해?
A. 단일 Domain 작업이지만 요구사항 분석과 구조화된 Handoff가 필요한 경우에 사용한다.

Q. PM-Specialist Workflow에 Review Agent가 꼭 필요해?
A. 필수는 아니지만 품질 검토가 필요한 작업이면 추가하는 것이 좋다.

Q. 복합 Domain 작업이면 어떻게 해?
A. SQL, Backend, Frontend 등으로 나누어 Sequential Workflow를 사용한다.

---

# 4. Sequential Workflow

## 4.1 Sequential Workflow Definition

### [개념]

Sequential Workflow는 여러 Agent가 정해진 순서대로 작업을 수행하는 Workflow Pattern이다.

이전 Agent의 Output이 다음 Agent의 Input이 되는 의존성 있는 작업에 적합하다.

기본 구조:

```text
PM Agent
→ Agent A
→ Agent B
→ Agent C
→ Review Agent
→ Fix Agent
→ Final Output
```

개인 AI 개발팀 기능 개발 구조:

```text
PM Agent
→ SQL Agent
→ Backend Agent
→ Frontend Agent
→ Review Agent
→ Fix Agent
→ PM Agent Final Integration
```

---

### [핵심]

- Sequential Workflow는 순차 실행 구조이다.
- 이전 Agent Output이 다음 Agent Input이 된다.
- 의존성이 있는 작업에 적합하다.
- DB Schema는 Backend API보다 먼저 필요할 수 있다.
- Backend API Contract는 Frontend 연동보다 먼저 필요할 수 있다.
- 각 Step의 Output은 Shared State에 기록해야 한다.
- 중간 실패 시 다음 Step을 강행하지 않는다.
- Review Agent는 전체 일관성을 검토한다.
- Fix Agent는 Review Findings를 반영한다.

---

### [실무]

기능 개발 Sequential Workflow:

```text
User Request:
"축제 리뷰 기능을 DB부터 화면까지 설계해줘"

Step 1. PM Agent
- 요구사항 분석
- Workflow Pattern 선택
- Task Decomposition

Step 2. SQL Agent
- reviews table 설계
- PK / FK / Constraint / Index 후보 제안

Step 3. Backend Agent
- Review API Contract 설계
- DTO / Service / Exception / Security 설계

Step 4. Frontend Agent
- Component 구조 설계
- State / API Call Flow 설계

Step 5. Review Agent
- SQL / Backend / Frontend 일관성 검토

Step 6. Fix Agent
- Review Findings 반영

Step 7. PM Agent
- Final Output 통합
```

Sequential Workflow State 예시:

```json
{
  "workflowPattern": "Sequential Workflow",
  "currentStep": "backend_design",
  "steps": [
    {
      "step": 1,
      "agent": "SQL Agent",
      "status": "completed",
      "output": "Review Schema"
    },
    {
      "step": 2,
      "agent": "Backend Agent",
      "status": "in_progress",
      "output": null
    },
    {
      "step": 3,
      "agent": "Frontend Agent",
      "status": "pending",
      "dependsOn": ["Backend API Contract"]
    }
  ]
}
```

---

### [FAQ]

Q. Sequential Workflow가 뭐야?
A. 여러 Agent가 정해진 순서대로 작업하고 이전 Agent Output을 다음 Agent Input으로 사용하는 Workflow다.

Q. Sequential Workflow는 언제 사용해?
A. DB → Backend → Frontend처럼 작업 의존성이 있는 경우에 사용한다.

Q. 중간 Step이 실패하면 다음 Step을 실행해도 돼?
A. 안 된다. Blocked 또는 Failed 상태를 기록하고 PM Agent가 Plan Revision을 해야 한다.

Q. Sequential Workflow에서 Shared State가 중요한 이유는?
A. 각 Agent Output과 Decision을 다음 Agent가 일관되게 참조해야 하기 때문이다.

---

## 4.2 Sequential Workflow Quality Gate

### [개념]

Sequential Workflow Quality Gate는 다음 Step으로 넘어가기 전에 이전 Step의 Output이 충분한지 확인하는 검수 기준이다.

순차 구조에서는 앞 단계의 오류가 뒤 단계 전체로 전파될 수 있으므로 Step별 Gate가 필요하다.

기본 구조:

```text
Step Output
→ Quality Gate
→ Pass
→ Next Step

Step Output
→ Quality Gate
→ Fail
→ Fix / Re-run / Plan Revision
```

---

### [핵심]

- 다음 Step 실행 전 이전 Step을 검수한다.
- 이전 Step이 completed 상태인지 확인한다.
- 다음 Agent에게 필요한 Output이 있는지 확인한다.
- Open Question이 다음 Step을 막는지 확인한다.
- Agent Output이 Shared State에 반영되었는지 확인한다.
- Critical Issue가 있으면 다음 Step으로 넘기지 않는다.
- Blocked 상태를 completed처럼 처리하지 않는다.

---

### [실무]

Sequential Quality Gate Checklist:

```md
## Sequential Workflow Quality Gate

- [ ] 이전 Step이 completed 상태인가?
- [ ] 이전 Step Output이 Shared State에 기록되었는가?
- [ ] 다음 Step의 Required Input이 충족되었는가?
- [ ] Open Questions가 다음 Step을 막지 않는가?
- [ ] Critical Issue가 없는가?
- [ ] Agent Output이 Scope를 준수했는가?
- [ ] 다음 Agent의 Handoff가 충분한가?
```

Failure 예시:

```md
## Sequential Workflow Failure

### Failure Type

Missing Previous Output

### Issue

Frontend Agent가 Backend API Response Field 없이 Review UI State를 설계함

### Impact

Frontend State와 Backend Response가 불일치할 수 있음

### Fix Direction

Backend Agent Output에 ReviewResDto Field를 보강하고 Frontend Step을 재실행
```

---

### [FAQ]

Q. Sequential Workflow Quality Gate가 뭐야?
A. 순차 Workflow에서 다음 Step으로 넘어가기 전에 이전 Step Output이 충분한지 검수하는 기준이다.

Q. Quality Gate가 필요한 이유는?
A. 앞 단계 오류가 뒤 단계로 전파되는 것을 막기 위해 필요하다.

Q. Quality Gate에서 실패하면 어떻게 해?
A. Fix, Re-run, Plan Revision 중 하나로 처리한다.

Q. Blocked 상태를 completed처럼 처리해도 돼?
A. 안 된다. 다음 Step 실행 전에 Blocked 원인을 해결해야 한다.

---

# 5. Router-based Workflow

## 5.1 Router-based Workflow Definition

### [개념]

Router-based Workflow는 요청의 Intent와 Domain을 분석해 적절한 Agent 또는 Workflow로 분기하는 실행 패턴이다.

Router-based Workflow는 Agent 수가 많고 요청 유형이 다양할 때 유용하다.

기본 구조:

```text
User Request
→ PM Agent or Router Agent
→ Routing Decision
→ Target Agent or Workflow
→ Result
```

---

### [핵심]

- Router-based Workflow는 요청 분기 중심이다.
- PM Agent가 Router 역할을 겸할 수 있다.
- 독립 Router Agent를 둘 수도 있다.
- Intent와 Domain을 분석한다.
- Routing Confidence를 표시한다.
- 복합 요청이면 단일 Agent가 아니라 복합 Workflow로 보낸다.
- 위험 작업이면 Approval 필요 여부를 표시한다.
- Routing 결과는 Shared State에 기록할 수 있다.

---

### [실무]

Router-based Workflow 예시:

```json
{
  "userRequest": "리뷰 기능 DB부터 화면까지 설계해줘",
  "routingResult": {
    "intent": "feature_design",
    "detectedDomains": ["SQL", "Backend", "Frontend"],
    "targetWorkflow": "Sequential Workflow",
    "targetAgents": ["SQL Agent", "Backend Agent", "Frontend Agent"],
    "confidence": "high",
    "reviewRequired": true
  }
}
```

Routing 대상:

| 요청 유형        | Routing 결과                  |
| ---------------- | ----------------------------- |
| 단순 개념 설명   | Single Agent Workflow         |
| 단일 Backend API | Backend Agent                 |
| DB + API + UI    | Sequential Workflow           |
| 문서 작성        | RAG Document Workflow         |
| 문서 검수        | Review-Fix Workflow           |
| 배포 실행        | Human-in-the-Loop Workflow    |
| Agent 구조 설계  | PM-Specialist 또는 Sequential |

---

### [FAQ]

Q. Router-based Workflow가 뭐야?
A. 요청의 Intent와 Domain을 분석해 적절한 Agent 또는 Workflow로 분기하는 실행 패턴이다.

Q. Router Agent와 Router-based Workflow는 같아?
A. 아니다. Router Agent는 역할이고 Router-based Workflow는 그 역할을 활용한 실행 패턴이다.

Q. 초기 개인 AI 개발팀에도 Router Agent가 필요해?
A. 필수는 아니다. 초기에는 PM Agent가 Router 역할을 겸할 수 있다.

Q. 복합 요청을 Router가 하나의 Agent에게 보내도 돼?
A. 아니다. 복합 요청은 Sequential Workflow나 Planner 기반 흐름으로 보내야 한다.

---

# 6. Review-Fix Workflow

## 6.1 Review-Fix Workflow Definition

### [개념]

Review-Fix Workflow는 Review Agent가 산출물을 검토하고 Fix Agent가 Review Findings를 반영하는 품질 개선 Workflow Pattern이다.

Review-Fix Workflow는 문서, 코드, 설계, Agent Output의 품질을 안정화하는 데 사용한다.

기본 구조:

```text
Draft Output
→ Review Agent
→ Review Findings
→ Fix Agent
→ Updated Output
→ Re-review
→ Pass
```

---

### [핵심]

- Review-Fix Workflow는 품질 개선 구조이다.
- Review Agent는 Findings를 작성한다.
- Fix Agent는 Findings를 반영한다.
- Review Agent는 직접 수정하지 않는다.
- Fix Agent는 새 요구사항을 만들지 않는다.
- Critical Issue는 반드시 수정한다.
- Major Issue는 수정하거나 PM Decision으로 분리한다.
- Minor Issue만 남으면 Pass with Notes 가능하다.
- Max Iteration과 Stop Condition이 필요하다.
- Review Criteria는 반복 중 바꾸지 않는다.

---

### [실무]

Review-Fix Loop 정책:

```json
{
  "workflowPattern": "Review-Fix Workflow",
  "maxIteration": 2,
  "severityPolicy": {
    "critical": "must_fix",
    "major": "fix_or_pm_decision",
    "minor": "pass_with_notes",
    "info": "optional"
  },
  "stopCondition": [
    "Critical Issue 0",
    "Major Issue handled or converted to Open Question",
    "Minor Issue only",
    "Max iteration reached"
  ]
}
```

Review-Fix 적용 대상:

| 대상             | Review 기준                                      |
| ---------------- | ------------------------------------------------ |
| RAG 문서         | Master Rules, Domain Rules, Retrieval Queries    |
| Backend API 설계 | API Contract, Security, Exception, Transaction   |
| Frontend 설계    | API Contract 일치, Loading / Error / Empty State |
| DevOps 계획      | Risk, Approval, Rollback Plan                    |
| Agent Workflow   | Role Separation, Handoff, State, Tool Permission |

---

### [FAQ]

Q. Review-Fix Workflow가 뭐야?
A. Review Agent가 검토하고 Fix Agent가 수정한 뒤 필요하면 다시 검토하는 품질 개선 Workflow다.

Q. Review-Fix Workflow는 언제 사용해?
A. 문서 검수, 코드 검토, 설계 검토, 규칙 준수 확인, 위험 감소가 필요한 작업에 사용한다.

Q. Review-Fix Workflow에 Max Iteration이 필요한 이유는?
A. 무한 반복을 막기 위해 필요하다.

Q. Fix Agent가 새 요구사항을 추가해도 돼?
A. 안 된다. 새 요구사항은 PM Agent에게 반환해야 한다.

---

## 6.2 Review-Fix Failure Control

### [개념]

Review-Fix Failure Control은 Review-Fix Loop가 무한 반복되거나 Fix Scope가 과도하게 확장되는 것을 막는 기준이다.

Review-Fix Workflow는 품질 개선에 유용하지만 종료 조건이 없으면 계속 반복될 수 있다.

기본 구조:

```text
Review
→ Fix
→ Re-review
→ Stop Condition Check
→ Pass or PM Decision
```

---

### [핵심]

- Review Criteria를 고정한다.
- Max Iteration을 설정한다.
- Minor Issue만 남으면 종료할 수 있다.
- Fix Scope를 Review Findings로 제한한다.
- 새 요구사항은 PM Agent에게 반환한다.
- 기존 요구사항을 훼손하지 않는다.
- Regression Risk를 확인한다.
- Pass / Fail 기준을 명확히 한다.

---

### [실무]

Review-Fix Stop Rules:

```md
## Review-Fix Stop Rules

- [ ] Max Iteration 기본 2회
- [ ] Critical Issue 0개
- [ ] Major Issue 해결 또는 PM Decision으로 분리
- [ ] Minor Issue만 남으면 Pass with Notes
- [ ] Review Criteria 변경 금지
- [ ] 새 요구사항은 PM Agent에게 반환
- [ ] Fix 후 Regression Risk 확인
```

Failure 예시:

```md
## Review-Fix Failure

### Failure Type

Changing Review Criteria

### Issue

1차 Review에서는 문서 구조만 검토했으나 2차 Review에서 새 기술 범위까지 추가 요구함

### Impact

Fix Scope가 계속 증가해 Workflow가 종료되지 않음

### Fix Direction

초기 Review Criteria로 돌아가고 새 기술 범위는 PM Agent에게 별도 요구사항으로 반환
```

---

### [FAQ]

Q. Review-Fix Failure Control이 뭐야?
A. Review-Fix Loop가 무한 반복되거나 Fix Scope가 과도하게 확장되는 것을 막는 기준이다.

Q. Review-Fix Loop가 무한 반복되는 이유는?
A. Max Iteration과 Stop Condition이 없거나 Review Criteria가 계속 바뀌기 때문이다.

Q. Minor Issue만 남으면 어떻게 해?
A. Pass with Notes로 종료할 수 있다.

Q. 새 요구사항이 발견되면 어떻게 해?
A. Fix하지 않고 PM Agent에게 별도 요구사항으로 반환한다.

---

# 7. Human-in-the-Loop Workflow

## 7.1 Human-in-the-Loop Workflow Definition

### [개념]

Human-in-the-Loop Workflow는 위험하거나 외부 영향이 있는 작업을 수행하기 전에 사용자 확인 또는 승인을 포함하는 Workflow Pattern이다.

Human-in-the-Loop Workflow는 Tool Permission의 Human Approval 규칙을 실제 실행 흐름에 포함한 것이다.

기본 구조:

```text
Risky Action Detected
→ Approval Request
→ User Decision
→ Execute / Cancel
→ Result Record
```

---

### [핵심]

- Human-in-the-Loop Workflow는 승인 포함 실행 흐름이다.
- Dangerous Tool 실행 전에 사용한다.
- 파일 삭제, DB 변경, 배포, 재시작, 이메일 발송, 결제 작업에 필요하다.
- Approval Request에는 Action, Target, Impact, Risk, Rollback Plan이 필요하다.
- 승인 전에는 실행하지 않는다.
- 승인 범위 밖 작업은 별도 승인이 필요하다.
- 거절되면 실행을 중단한다.
- 실행 결과는 Tool Result State에 기록한다.

---

### [실무]

Human-in-the-Loop 적용 대상:

| 작업                    | Approval 필요 |
| ----------------------- | ------------- |
| 새 문서 초안 생성       | 보통 불필요   |
| 기존 문서 덮어쓰기      | 필요          |
| 파일 삭제               | 필요          |
| DB Migration            | 필요          |
| 운영 배포               | 필요          |
| Docker Container 재시작 | 필요          |
| 이메일 발송             | 필요          |
| 결제 실행               | 필요          |
| 외부 API 대량 호출      | 필요          |

Approval Request 예시:

```md
## Human Approval Request

### Action

Production backend deploy

### Target

backend production container

### Reason

Review API 변경사항 적용 필요

### Expected Impact

서비스가 일시적으로 중단될 수 있음

### Risks

- 배포 실패 시 서비스 장애 가능
- DB Migration과 API 버전 불일치 가능

### Rollback Plan

- 이전 image tag로 rollback
- 기존 container 재시작

### Approval Required

Yes
```

---

### [FAQ]

Q. Human-in-the-Loop Workflow가 뭐야?
A. 위험하거나 외부 영향이 있는 작업 전에 사용자 확인 또는 승인을 포함하는 Workflow다.

Q. Human Approval과 Human-in-the-Loop Workflow 차이는?
A. Human Approval은 승인 규칙이고, Human-in-the-Loop Workflow는 그 승인 절차를 포함한 실행 흐름이다.

Q. 어떤 작업에 Human-in-the-Loop가 필요해?
A. 파일 삭제, DB 변경, 배포, 서비스 재시작, 결제, 이메일 발송, 운영 설정 변경이다.

Q. 사용자가 거절하면 어떻게 해?
A. 실행을 중단하고 Safe Alternative 또는 계획만 제공한다.

---

# 8. RAG Document Workflow

## 8.1 RAG Document Workflow Definition

### [개념]

RAG Document Workflow는 RAG 문서 제작, 검수, 수정, 최종 출력에 특화된 Workflow Pattern이다.

RAG Document Workflow의 목적은 AI Agent Retrieval에 적합한 Markdown 문서를 안정적으로 생산하는 것이다.

기본 구조:

```text
User Request
→ PM Agent
→ Documentation Agent
→ Review Agent
→ Fix Agent
→ Final RAG Document
```

---

### [핵심]

- RAG Document Workflow는 문서 제작 특화 Workflow이다.
- PM Agent가 Part Topic과 적용 Rules를 정리한다.
- Documentation Agent가 초안을 작성한다.
- Review Agent가 Master Rules와 Domain Rules 기준으로 검토한다.
- Fix Agent가 Review Findings를 반영한다.
- 최종 결과는 RAG Retrieval 최적화 문서여야 한다.
- `[개념]`, `[핵심]`, `[실무]`, `[FAQ]` 구조를 유지한다.
- Retrieval Queries를 포함한다.
- 사용자가 최종 결과만 요청하면 중간 설명을 출력하지 않는다.

---

### [실무]

RAG Document Workflow Step:

```text
1. PM Agent
   - Target Part 결정
   - Required Rules 확인
   - Output Format 확인

2. Documentation Agent
   - RAG 문서 초안 작성
   - Required Section 구성
   - FAQ 작성
   - Retrieval Queries 작성

3. Review Agent
   - MASTER_RAG_RULES 검토
   - DOMAIN_RULES 검토
   - Output Format 검토
   - Retrieval Quality 검토

4. Fix Agent
   - 누락 Section 보강
   - FAQ 보강
   - Retrieval Queries 보강
   - 용어 통일

5. PM Agent
   - 최종 결과 통합
   - 최종 Output 제공
```

RAG Document Quality Gate:

```md
## RAG Document Quality Gate

- [ ] FileName이 명확한가?
- [ ] Document Title이 명확한가?
- [ ] Required Section이 포함되었는가?
- [ ] `[개념]`, `[핵심]`, `[실무]`, `[FAQ]`가 포함되었는가?
- [ ] Retrieval Queries가 포함되었는가?
- [ ] Domain Rules가 반영되었는가?
- [ ] Output Format을 지켰는가?
```

---

### [FAQ]

Q. RAG Document Workflow가 뭐야?
A. RAG 문서 제작, 검수, 수정, 최종 출력에 특화된 Workflow Pattern이다.

Q. RAG Document Workflow의 목적은?
A. AI Agent Retrieval에 최적화된 Markdown 문서를 만드는 것이다.

Q. RAG Document Workflow에는 어떤 Agent가 필요해?
A. PM Agent, Documentation Agent, Review Agent, Fix Agent가 필요하다.

Q. RAG 문서 제작에서 가장 중요한 Output 조건은?
A. Required Section, FAQ, Retrieval Queries, 용어 통일, 최종 Output 형식 준수다.

---

# 9. Personal AI Development Team Workflow

## 9.1 Personal AI Development Team Workflow Definition

### [개념]

Personal AI Development Team Workflow는 개인 AI 서버를 PM Agent 중심의 개발 보조 팀처럼 운영하기 위한 통합 Workflow Pattern이다.

사용자는 PM Agent에게만 요청하고, PM Agent가 필요한 Specialist Agent를 호출하며, 최종 결과를 통합한다.

기본 구조:

```text
User
→ PM Agent
→ Specialist Agent
→ Review Agent
→ Fix Agent
→ PM Agent
→ Final Output
```

기능 개발 구조:

```text
User
→ PM Agent
→ SQL Agent
→ Backend Agent
→ Frontend Agent
→ Review Agent
→ Fix Agent
→ Final Output
```

---

### [핵심]

- 사용자는 PM Agent에게만 요청한다.
- PM Agent가 Workflow Pattern을 선택한다.
- PM Agent가 요구사항 분석과 Task Decomposition을 수행한다.
- SQL Agent는 DB와 Query를 담당한다.
- Backend Agent는 API와 Service를 담당한다.
- Frontend Agent는 UI와 API 연동을 담당한다.
- DevOps Agent는 배포와 운영 계획을 담당한다.
- AI Agent는 RAG, Prompt, Agent Workflow를 담당한다.
- Review Agent는 전체 결과를 검토한다.
- Fix Agent는 Review Findings를 반영한다.
- 최종 결과는 PM Agent가 통합한다.

---

### [실무]

개인 AI 개발팀 요청별 Workflow:

| 요청 유형                    | 권장 Workflow                          |
| ---------------------------- | -------------------------------------- |
| 단순 개념 질문               | Single Agent Workflow                  |
| 단일 Backend 설계            | PM-Specialist Workflow                 |
| DB + Backend + Frontend 설계 | Sequential Workflow                    |
| RAG 문서 작성                | RAG Document Workflow                  |
| 문서 검수 및 수정            | Review-Fix Workflow                    |
| 배포 실행                    | Human-in-the-Loop Workflow             |
| Agent 구조 개선              | PM-Specialist 또는 Sequential Workflow |

개인 AI 개발팀 기능 개발 예시:

```text
User Request
→ PM Agent Requirement Analysis
→ SQL Agent Schema Design
→ Backend Agent API Design
→ Frontend Agent UI Integration Design
→ Review Agent Cross-domain Review
→ Fix Agent Finding Fix
→ PM Agent Final Integration
→ Final Output
```

---

### [FAQ]

Q. Personal AI Development Team Workflow가 뭐야?
A. 사용자가 PM Agent에게 요청하면 PM Agent가 SQL, Backend, Frontend, Review, Fix Agent로 작업을 분배하고 최종 결과를 통합하는 Workflow다.

Q. 사용자가 모든 Agent에게 직접 요청해야 해?
A. 아니다. 사용자는 PM Agent에게만 요청하고 PM Agent가 Agent를 선택하는 구조가 안정적이다.

Q. 개인 AI 개발팀에서 가장 기본 Agent는?
A. PM Agent, Specialist Agent, Review Agent, Fix Agent다.

Q. 개인 AI 개발팀 Workflow의 장점은?
A. 역할 분리, 품질 검토, RAG Scope 제한, 최종 결과 통합이 가능하다는 점이다.

---

# 10. Workflow Pattern Selection

## 10.1 Selection Matrix

### [개념]

Workflow Pattern Selection은 PM Agent가 사용자 요청을 분석해 적절한 Workflow Pattern을 선택하는 단계이다.

Workflow Pattern Selection은 요청 복잡도, Domain 수, 의존성, 위험도, Review 필요 여부, Approval 필요 여부를 기준으로 한다.

기본 구조:

```text
User Request
→ Complexity Check
→ Domain Count Check
→ Dependency Check
→ Risk Check
→ Review Need Check
→ Approval Need Check
→ Selected Pattern
```

---

### [핵심]

- PM Agent가 Workflow Pattern을 선택한다.
- 단순 질문은 Single Agent Workflow를 사용한다.
- 단일 Domain 작업은 PM-Specialist Workflow를 사용한다.
- 의존성 있는 복합 작업은 Sequential Workflow를 사용한다.
- 요청 분기가 필요하면 Router-based Workflow를 사용한다.
- 품질 검토가 필요하면 Review-Fix Workflow를 추가한다.
- 위험 작업이 있으면 Human-in-the-Loop Workflow를 사용한다.
- RAG 문서 제작은 RAG Document Workflow를 사용한다.
- Pattern 선택 결과는 Shared State에 기록한다.

---

### [실무]

Workflow Pattern Selection Matrix:

| Request Type            | Domain Count | Dependency | Risk   | Recommended Pattern         |
| ----------------------- | -----------: | ---------- | ------ | --------------------------- |
| 단순 개념 질문          |            1 | Low        | Low    | Single Agent                |
| 단일 API 설계           |            1 | Low        | Medium | PM-Specialist               |
| DB + Backend + Frontend |            3 | High       | Medium | Sequential                  |
| 문서 검수 후 수정       |            1 | Medium     | Low    | Review-Fix                  |
| 배포 실행               |            1 | High       | High   | Human-in-the-Loop           |
| RAG 문서 작성           |            1 | Medium     | Low    | RAG Document                |
| Agent 구조 설계         |     Multiple | Medium     | Medium | PM-Specialist or Sequential |
| 자동 실행 계획          |     Multiple | High       | High   | Router-based + HITL         |

Selection Output 예시:

```json
{
  "userRequest": "RAG 문서 검수 후 수정해줘",
  "complexity": "medium",
  "domainCount": 1,
  "dependency": "medium",
  "riskLevel": "low",
  "reviewRequired": true,
  "approvalRequired": false,
  "selectedPattern": "Review-Fix Workflow",
  "targetAgents": ["Review Agent", "Fix Agent"]
}
```

---

### [FAQ]

Q. Workflow Pattern Selection이 뭐야?
A. PM Agent가 사용자 요청을 분석해 적절한 Workflow Pattern을 선택하는 단계다.

Q. Workflow Pattern 선택 기준은?
A. 요청 복잡도, Domain 수, 의존성, 위험도, Review 필요 여부, Approval 필요 여부다.

Q. RAG 문서 작성 요청은 어떤 Pattern을 사용해?
A. RAG Document Workflow를 사용한다.

Q. 배포 실행 요청은 어떤 Pattern을 사용해?
A. Human-in-the-Loop Workflow를 사용해야 한다.

---

# 11. Workflow Failure Handling

## 11.1 Workflow Failure Cases

### [개념]

Workflow Failure는 잘못된 Pattern 선택, Step 누락, 순서 오류, Review 누락, Approval 누락, Final Integration 실패로 인해 Workflow 품질이 떨어지는 문제이다.

Workflow Failure는 개별 Agent Output이 좋아도 전체 결과를 실패하게 만들 수 있다.

주요 실패 구조:

```text
Wrong Pattern
→ Wrong Steps
→ Missing Output
→ Review Failure
→ Final Output Failure
```

---

### [핵심]

- Wrong Workflow Pattern은 요구사항 누락을 만든다.
- 복합 작업을 Single Agent로 처리하면 누락이 발생한다.
- 단순 작업에 복잡한 Workflow를 쓰면 비효율적이다.
- Step 순서 오류는 의존성 문제를 만든다.
- Review 누락은 품질 문제를 Final Output으로 전달한다.
- Approval 누락은 위험 작업 사고로 이어질 수 있다.
- Final Integration 실패는 사용자에게 충돌된 결과를 전달한다.
- PM Agent가 Recovery를 조율한다.

---

### [실무]

Workflow Failure Matrix:

| Failure Type              | Symptom                  | Handling             |
| ------------------------- | ------------------------ | -------------------- |
| Wrong Pattern             | 필요한 Agent 누락        | Pattern 재선택       |
| Missing Step              | DB/API/UI 중 일부 누락   | Plan 보강            |
| Wrong Step Order          | Frontend가 API 없이 설계 | Step 순서 수정       |
| Missing Review            | 품질 검수 없이 Final     | Review Step 추가     |
| Missing Approval          | 위험 작업 승인 누락      | HITL 추가            |
| Infinite Review-Fix       | Loop 반복                | Stop Condition 적용  |
| Final Integration Failure | 결과 간 충돌             | PM Agent 통합 재수행 |
| Stale State               | 이전 Workflow 기준 사용  | State 재초기화       |

Workflow Failure Record:

```md
## Workflow Failure

### Failure Type

Wrong Workflow Pattern

### Issue

DB, Backend, Frontend가 필요한 기능 개발 요청을 Single Agent Workflow로 처리함

### Impact

DB Schema, API Contract, Frontend 연동 일관성 검토가 누락됨

### Fix Direction

Sequential Workflow로 변경하고 SQL → Backend → Frontend → Review 순서로 재실행

### Prevention Rule

Domain Count가 2개 이상이고 의존성이 있으면 Sequential Workflow를 우선 검토
```

---

### [FAQ]

Q. Workflow Failure는 뭐야?
A. 잘못된 Pattern 선택, Step 누락, 순서 오류, Review 누락, Approval 누락, Final Integration 실패로 인해 전체 Workflow 품질이 떨어지는 문제다.

Q. 개별 Agent Output이 좋아도 Workflow가 실패할 수 있어?
A. 가능하다. Step 순서, 통합, Review, Approval이 잘못되면 전체 결과가 실패할 수 있다.

Q. 복합 개발 작업을 Single Agent로 처리하면 왜 문제야?
A. DB, Backend, Frontend 의존성과 일관성 검토가 누락될 수 있다.

Q. Workflow Failure는 누가 복구해?
A. PM Agent가 Pattern 재선택, Plan Revision, Review 추가, Approval 요청을 조율한다.

---

# Retrieval Queries

### [FAQ]

Q. Workflow Pattern이 뭐야?
A. Multi-Agent System에서 Agent들이 어떤 순서와 조건으로 협업하는지 정의한 실행 구조다.

Q. Workflow Pattern이 필요한 이유는?
A. 요청 유형마다 필요한 Agent, 실행 순서, Review, 승인 기준이 다르기 때문이다.

Q. Part07과 Part12 차이는 뭐야?
A. Part07은 Router, Planner, Executor 역할 자체를 다루고, Part12는 Agent 실행 흐름의 Pattern을 다룬다.

Q. Workflow Pattern은 누가 선택해?
A. 일반적으로 PM Agent가 사용자 요청을 분석해 선택한다.

Q. Single Agent Workflow가 뭐야?
A. 하나의 Agent가 요청을 분석하고 응답까지 처리하는 가장 단순한 Workflow다.

Q. Single Agent Workflow는 언제 사용해?
A. 단순 질문, 개념 설명, 위험도 낮은 단일 응답에 사용한다.

Q. PM-Specialist Workflow가 뭐야?
A. PM Agent가 요청을 분석하고 하나의 Specialist Agent에게 작업을 전달한 뒤 결과를 통합하는 Workflow다.

Q. PM-Specialist Workflow는 언제 사용해?
A. 단일 Domain 작업이지만 요구사항 분석과 구조화된 Handoff가 필요한 경우에 사용한다.

Q. Sequential Workflow가 뭐야?
A. 여러 Agent가 정해진 순서대로 작업하고 이전 Agent Output을 다음 Agent Input으로 사용하는 Workflow다.

Q. Sequential Workflow는 언제 사용해?
A. DB → Backend → Frontend처럼 작업 의존성이 있는 경우에 사용한다.

Q. Sequential Workflow Quality Gate가 뭐야?
A. 순차 Workflow에서 다음 Step으로 넘어가기 전에 이전 Step Output이 충분한지 검수하는 기준이다.

Q. Quality Gate에서 실패하면 어떻게 해?
A. Fix, Re-run, Plan Revision 중 하나로 처리한다.

Q. Router-based Workflow가 뭐야?
A. 요청의 Intent와 Domain을 분석해 적절한 Agent 또는 Workflow로 분기하는 실행 패턴이다.

Q. Router Agent와 Router-based Workflow는 같아?
A. 아니다. Router Agent는 역할이고 Router-based Workflow는 그 역할을 활용한 실행 패턴이다.

Q. Review-Fix Workflow가 뭐야?
A. Review Agent가 검토하고 Fix Agent가 수정한 뒤 필요하면 다시 검토하는 품질 개선 Workflow다.

Q. Review-Fix Workflow는 언제 사용해?
A. 문서 검수, 코드 검토, 설계 검토, 규칙 준수 확인, 위험 감소가 필요한 작업에 사용한다.

Q. Review-Fix Workflow에 Max Iteration이 필요한 이유는?
A. 무한 반복을 막기 위해 필요하다.

Q. Review-Fix Failure Control이 뭐야?
A. Review-Fix Loop가 무한 반복되거나 Fix Scope가 과도하게 확장되는 것을 막는 기준이다.

Q. Human-in-the-Loop Workflow가 뭐야?
A. 위험하거나 외부 영향이 있는 작업 전에 사용자 확인 또는 승인을 포함하는 Workflow다.

Q. Human Approval과 Human-in-the-Loop Workflow 차이는?
A. Human Approval은 승인 규칙이고, Human-in-the-Loop Workflow는 그 승인 절차를 포함한 실행 흐름이다.

Q. 어떤 작업에 Human-in-the-Loop가 필요해?
A. 파일 삭제, DB 변경, 배포, 서비스 재시작, 결제, 이메일 발송, 운영 설정 변경이다.

Q. RAG Document Workflow가 뭐야?
A. RAG 문서 제작, 검수, 수정, 최종 출력에 특화된 Workflow Pattern이다.

Q. RAG Document Workflow의 목적은?
A. AI Agent Retrieval에 최적화된 Markdown 문서를 만드는 것이다.

Q. RAG Document Workflow에는 어떤 Agent가 필요해?
A. PM Agent, Documentation Agent, Review Agent, Fix Agent가 필요하다.

Q. Personal AI Development Team Workflow가 뭐야?
A. 사용자가 PM Agent에게 요청하면 PM Agent가 SQL, Backend, Frontend, Review, Fix Agent로 작업을 분배하고 최종 결과를 통합하는 Workflow다.

Q. 사용자가 모든 Agent에게 직접 요청해야 해?
A. 아니다. 사용자는 PM Agent에게만 요청하고 PM Agent가 Agent를 선택하는 구조가 안정적이다.

Q. 개인 AI 개발팀에서 가장 기본 Agent는?
A. PM Agent, Specialist Agent, Review Agent, Fix Agent다.

Q. Workflow Pattern Selection이 뭐야?
A. PM Agent가 사용자 요청을 분석해 적절한 Workflow Pattern을 선택하는 단계다.

Q. Workflow Pattern 선택 기준은?
A. 요청 복잡도, Domain 수, 의존성, 위험도, Review 필요 여부, Approval 필요 여부다.

Q. RAG 문서 작성 요청은 어떤 Pattern을 사용해?
A. RAG Document Workflow를 사용한다.

Q. 배포 실행 요청은 어떤 Pattern을 사용해?
A. Human-in-the-Loop Workflow를 사용해야 한다.

Q. Workflow Failure는 뭐야?
A. 잘못된 Pattern 선택, Step 누락, 순서 오류, Review 누락, Approval 누락, Final Integration 실패로 인해 전체 Workflow 품질이 떨어지는 문제다.

Q. 개별 Agent Output이 좋아도 Workflow가 실패할 수 있어?
A. 가능하다. Step 순서, 통합, Review, Approval이 잘못되면 전체 결과가 실패할 수 있다.

Q. 개인 AI 개발팀에서 기능 개발 요청은 어떤 Workflow가 적합해?
A. DB, Backend, Frontend 의존성이 있으므로 Sequential Workflow가 적합하다.

Q. 개인 AI 개발팀에서 문서 제작 요청은 어떤 Workflow가 적합해?
A. RAG Document Workflow가 적합하다.
