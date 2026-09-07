# Multi-Agent System Part14 - Failure and Troubleshooting

---

# 1. Failure Core

## 1.1 Failure Definition

### [개념]

Failure는 Multi-Agent System에서 Agent, Handoff, Shared State, RAG Retrieval, Tool Permission, Workflow Pattern 중 하나 이상이 기대한 기준을 충족하지 못해 결과 품질이 떨어지는 상태이다.

Failure는 단순 오류 메시지뿐 아니라 누락, 충돌, 과도한 추측, 역할 중복, 잘못된 Routing, 무한 Review-Fix Loop, 위험 Tool 실행 시도까지 포함한다.

Failure Troubleshooting의 핵심은 증상만 수정하는 것이 아니라 Root Cause를 찾고, 재발을 막기 위한 Agent Definition, Handoff Template, RAG Scope, Review Criteria, Tool Permission을 개선하는 것이다.

기본 구조:

```text
Failure Symptom
→ Failure Type
→ Root Cause
→ Impact
→ Fix Direction
→ Prevention Rule
```

Multi-Agent Failure 흐름:

```text
Poor Handoff
→ Wrong Specialist Output
→ Review Finding
→ Fix Scope Expansion
→ Workflow Delay
```

---

### [핵심]

- Failure는 Multi-Agent System의 실패 상태이다.
- 단순 실행 오류만 Failure가 아니다.
- 요구사항 누락도 Failure이다.
- Agent Role 충돌도 Failure이다.
- RAG Scope 오류도 Failure이다.
- Shared State 충돌도 Failure이다.
- Tool Permission 위반도 Failure이다.
- Review-Fix 무한 반복도 Failure이다.
- Failure는 Root Cause 기준으로 분석해야 한다.
- Failure 분석 결과는 재발 방지 규칙으로 연결해야 한다.

---

### [실무]

2026 실무 기준에서 Multi-Agent Failure는 다음 기준으로 분류한다.

```text
Role Failure
→ Agent 역할 경계 실패

Handoff Failure
→ Agent 간 작업 전달 실패

State Failure
→ Shared State 누락 / 충돌 / 오래됨

RAG Failure
→ 검색 범위 / 검색 결과 / Context 문제

Tool Failure
→ Tool 권한 / 실행 / 결과 기록 문제

Review-Fix Failure
→ 검토 / 수정 Loop 문제

Workflow Failure
→ Pattern 선택 / Step 순서 / 통합 실패

Final Output Failure
→ 최종 사용자 요구사항 충족 실패
```

Failure Record Template:

```md
## Failure Record

### Failure Type

<Failure Category>

### Symptom

<겉으로 보이는 문제>

### Root Cause

<근본 원인>

### Impact

<영향>

### Immediate Fix

<즉시 수정 방향>

### Prevention Rule

<재발 방지 규칙>

### Related Agent

<관련 Agent>

### Re-review Required

<Yes | No>
```

---

### [FAQ]

Q. Multi-Agent System에서 Failure는 뭐야?
A. Agent, Handoff, Shared State, RAG, Tool Permission, Workflow 중 하나 이상이 기준을 충족하지 못해 결과 품질이 떨어지는 상태다.

Q. Failure는 실행 오류만 의미해?
A. 아니다. 요구사항 누락, 역할 중복, 잘못된 Routing, RAG Scope 오류, Review-Fix 반복도 Failure다.

Q. Failure 분석에서 가장 중요한 것은?
A. 증상이 아니라 Root Cause를 찾는 것이다.

Q. Failure 분석 결과는 어디에 사용해?
A. Agent Definition, Handoff Template, RAG Scope, Review Criteria, Tool Permission, Workflow Pattern 개선에 사용한다.

---

# 2. Role Failure

## 2.1 Role Overlap

### [개념]

Role Overlap은 여러 Agent가 같은 책임을 중복 수행하거나, 한 Agent가 자기 Scope 밖 작업까지 수행하는 실패 유형이다.

Role Overlap이 발생하면 Agent Output이 충돌하고, PM Agent가 결과를 통합하기 어려워지며, Review-Fix Loop가 증가한다.

기본 구조:

```text
Agent A Scope
→ Agent B Scope
→ Overlap
→ Conflicting Output
→ Integration Failure
```

예시:

```text
Backend Agent
→ API Contract 작성

Frontend Agent
→ API Contract를 임의 변경

결과
→ Backend / Frontend API 불일치
```

---

### [핵심]

- Role Overlap은 Agent 책임 중복이다.
- Agent Scope가 불명확하면 발생한다.
- PM Agent가 직접 구현을 과도하게 하면 발생한다.
- Specialist Agent가 다른 Domain을 확정하면 발생한다.
- Review Agent가 직접 수정하면 역할 경계가 흐려진다.
- Fix Agent가 새 요구사항을 만들면 역할 위반이다.
- Role Overlap은 Output 충돌을 만든다.
- Role Overlap은 Agent Definition으로 방지한다.
- Handoff에 Agent Scope를 명시해야 한다.

---

### [실무]

Role Overlap 예시:

| 상황                                            | 문제                        |
| ----------------------------------------------- | --------------------------- |
| PM Agent가 Backend Code를 직접 상세 구현        | PM Agent Scope 초과         |
| Backend Agent가 React Component를 확정          | Frontend Agent Scope 침범   |
| Frontend Agent가 API Response Field를 임의 변경 | Backend Agent Output과 충돌 |
| Review Agent가 직접 문서 수정                   | Fix Agent 역할 침범         |
| Fix Agent가 새로운 기능 요구사항 추가           | PM Agent 역할 침범          |

Role Overlap Finding 예시:

```md
## Failure Record

### Failure Type

Role Overlap

### Symptom

Backend Agent Output에 React Component 구조가 포함됨

### Root Cause

Handoff에 Backend Agent Scope와 Output Boundary가 명확히 지정되지 않음

### Impact

Frontend Agent 책임과 충돌하고 API Contract 기반 흐름이 불명확해짐

### Immediate Fix

Backend Agent Output에서 React Component 설계를 제거하고 Frontend Agent Handoff로 분리

### Prevention Rule

Backend Agent Handoff에 `Do not define UI Component structure` 제약 추가
```

---

### [FAQ]

Q. Role Overlap이 뭐야?
A. 여러 Agent가 같은 책임을 중복 수행하거나 한 Agent가 자기 Scope 밖 작업을 수행하는 실패 유형이다.

Q. Role Overlap이 왜 문제야?
A. Agent Output 충돌, PM Agent 통합 실패, Review-Fix 반복 증가를 만든다.

Q. Role Overlap은 어떻게 줄여?
A. Agent Definition, Handoff Scope, Expected Output, Forbidden Scope를 명확히 정의해야 한다.

Q. Review Agent가 직접 수정하면 Role Overlap이야?
A. 원칙적으로 그렇다. Review Agent는 Finding을 작성하고 Fix Agent가 수정해야 한다.

---

## 2.2 PM Agent Implementation Creep

### [개념]

PM Agent Implementation Creep은 PM Agent가 조율자 역할을 넘어 Specialist Agent가 해야 할 구현 작업까지 직접 수행하는 실패 유형이다.

PM Agent는 요구사항 분석, Task Decomposition, Routing, Handoff, Result Integration을 담당해야 한다.

PM Agent가 구현 세부사항을 과도하게 확정하면 Specialist Agent의 역할이 약해지고, Domain 검토 품질이 떨어질 수 있다.

기본 구조:

```text
PM Agent
→ Requirement Analysis
→ Task Decomposition
→ Implementation Detail Overreach
→ Specialist Role Reduced
→ Quality Risk
```

---

### [핵심]

- PM Agent는 조율자이다.
- PM Agent는 Specialist Agent를 대체하지 않는다.
- PM Agent는 구현 세부사항을 과도하게 확정하면 안 된다.
- PM Agent는 요구사항과 제약을 정리한다.
- PM Agent는 Domain별 작업을 분배한다.
- PM Agent는 결과를 통합한다.
- 구현 상세는 Specialist Agent가 담당한다.
- PM Agent가 구현을 직접 하면 Domain Rules 누락 가능성이 증가한다.
- PM Agent Implementation Creep은 Role Definition으로 방지한다.

---

### [실무]

PM Agent 정상 역할:

```text
User Request 분석
→ 요구사항 정리
→ 작업 분해
→ Target Agent 선택
→ Handoff 작성
→ 결과 통합
```

PM Agent 역할 초과:

```text
Controller Code 직접 작성
Entity Field 상세 확정
React Component 내부 구현 확정
DB Index 확정
Docker 명령 실행
```

Troubleshooting 예시:

```md
## Failure Record

### Failure Type

PM Agent Implementation Creep

### Symptom

PM Agent가 Backend Agent 호출 없이 API Controller 세부 구현을 확정함

### Root Cause

PM Agent Role Definition에 Implementation Boundary가 부족함

### Impact

Backend Domain Rules, Security Rules, Exception Handling 검토가 누락될 수 있음

### Immediate Fix

PM Agent Output을 Handoff 수준으로 축소하고 Backend Agent에게 API 설계 작업을 전달

### Prevention Rule

PM Agent는 Implementation Detail을 확정하지 않고 Specialist Agent에게 위임한다
```

---

### [FAQ]

Q. PM Agent Implementation Creep이 뭐야?
A. PM Agent가 조율자 역할을 넘어 Specialist Agent의 구현 작업까지 직접 수행하는 실패다.

Q. PM Agent는 구현을 하면 안 돼?
A. 원칙적으로 상세 구현 확정은 Specialist Agent에게 맡기고 PM Agent는 요구사항, 분해, Handoff, 통합을 담당해야 한다.

Q. PM Agent가 구현을 직접 하면 왜 위험해?
A. Domain Rules, 보안, 예외 처리, 세부 검토가 누락될 수 있다.

Q. 어떻게 방지해?
A. PM Agent Role Definition에 Implementation Boundary와 Specialist Delegation 규칙을 명시한다.

---

# 3. Handoff Failure

## 3.1 Poor Handoff

### [개념]

Poor Handoff는 Source Agent가 Target Agent에게 충분하지 않거나 모호한 작업 정보를 전달하는 실패 유형이다.

Poor Handoff는 Multi-Agent System에서 가장 흔한 실패 원인이다.

기본 구조:

```text
Unclear Handoff
→ Agent Guessing
→ Incomplete Output
→ Review Finding
→ Rework
```

Poor Handoff 예시:

```text
"리뷰 기능 백엔드 만들어줘"
```

문제:

- Requirements 없음
- Constraints 없음
- Expected Output 없음
- Done Criteria 없음
- RAG Scope 없음

---

### [핵심]

- Poor Handoff는 부실한 작업 전달이다.
- Task가 모호하면 Agent가 추측한다.
- Requirements 누락은 기능 누락으로 이어진다.
- Constraints 누락은 규칙 위반으로 이어진다.
- Context 부족은 Hallucination을 유발한다.
- Expected Output 누락은 비구조화 Output을 만든다.
- Done Criteria 누락은 완료 판단 실패를 만든다.
- RAG Scope 누락은 잘못된 문서 검색으로 이어진다.
- Poor Handoff는 PM Agent가 수정해야 한다.

---

### [실무]

Poor Handoff 진단 Checklist:

```md
## Poor Handoff Diagnosis Checklist

- [ ] Task가 명확한가?
- [ ] Target Agent가 명확한가?
- [ ] Requirements가 충분한가?
- [ ] Constraints가 분리되어 있는가?
- [ ] Context가 충분한가?
- [ ] Expected Output이 명확한가?
- [ ] Done Criteria가 있는가?
- [ ] RAG Scope가 지정되어 있는가?
- [ ] Tool Permission이 지정되어 있는가?
- [ ] Open Questions가 표시되어 있는가?
```

Good Handoff로 수정 예시:

```json
{
  "from": "PM Agent",
  "to": "Backend Agent",
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
    "Security rule included"
  ]
}
```

---

### [FAQ]

Q. Poor Handoff가 뭐야?
A. Source Agent가 Target Agent에게 충분하지 않거나 모호한 작업 정보를 전달하는 실패 유형이다.

Q. Poor Handoff가 왜 위험해?
A. Target Agent가 추측으로 작업해 요구사항 누락, 규칙 위반, Output 충돌이 발생하기 때문이다.

Q. Poor Handoff의 대표 원인은?
A. Task 모호함, Requirements 누락, Constraints 누락, Expected Output 누락, Done Criteria 누락이다.

Q. Poor Handoff는 누가 고쳐야 해?
A. 일반적으로 PM Agent가 Handoff를 재작성해야 한다.

---

## 3.2 Missing Requirement Handoff

### [개념]

Missing Requirement Handoff는 Handoff에 필수 요구사항이 누락되어 Target Agent Output에서도 해당 기능이나 조건이 빠지는 실패 유형이다.

Missing Requirement는 Agent의 실수처럼 보일 수 있지만, 실제 Root Cause는 PM Agent Handoff일 수 있다.

기본 구조:

```text
User Request
→ PM Agent Handoff
→ Missing Requirement
→ Specialist Output Missing Feature
```

---

### [핵심]

- Handoff에 요구사항이 없으면 Agent가 누락할 가능성이 높다.
- Output 누락의 Root Cause가 Handoff일 수 있다.
- Review Agent는 Output만이 아니라 Handoff도 검토해야 한다.
- 필수 요구사항 누락은 Major 또는 Critical이다.
- Handoff 수정 후 Target Agent를 재실행해야 할 수 있다.
- Requirement Coverage Matrix를 사용하면 누락을 줄일 수 있다.

---

### [실무]

Missing Requirement 예시:

```md
## Failure Record

### Failure Type

Missing Requirement Handoff

### Symptom

Backend Agent Output에 리뷰 삭제 API가 없음

### Root Cause

PM Agent Handoff에 "Review author can delete own review" 요구사항이 누락됨

### Impact

리뷰 삭제 기능이 전체 Workflow에서 누락됨

### Immediate Fix

Handoff Requirements에 리뷰 삭제 요구사항을 추가하고 Backend Agent Output 재작성

### Prevention Rule

PM Agent는 Handoff 전 Requirement Coverage Checklist를 수행한다
```

Requirement Coverage Handoff Template:

```md
## Handoff Requirement Coverage

| User Requirement | Handoff Requirement                   | Status  |
| ---------------- | ------------------------------------- | ------- |
| 리뷰 작성        | Authenticated user can create review  | Covered |
| 리뷰 목록        | User can view review list by festival | Covered |
| 리뷰 수정        | Review author can update own review   | Covered |
| 리뷰 삭제        | 누락                                  | Missing |
```

---

### [FAQ]

Q. Missing Requirement Handoff가 뭐야?
A. Handoff에 필수 요구사항이 누락되어 Target Agent Output에서도 해당 기능이 빠지는 실패다.

Q. Output 누락은 항상 Specialist Agent 잘못이야?
A. 아니다. Handoff에 요구사항이 없었다면 PM Agent Handoff 문제가 Root Cause일 수 있다.

Q. 어떻게 방지해?
A. Handoff 전 Requirement Coverage Matrix를 작성해야 한다.

Q. 누락 요구사항이 발견되면 어떻게 해?
A. Handoff를 수정하고 Target Agent를 재실행하거나 Fix Agent가 보강해야 한다.

---

# 4. Shared State Failure

## 4.1 Shared State Conflict

### [개념]

Shared State Conflict는 Shared State에 서로 충돌하는 결정사항, Agent Output, 요구사항, Open Question이 존재하는 실패 유형이다.

Shared State Conflict가 해결되지 않으면 Agent들이 서로 다른 기준으로 작업하게 된다.

기본 구조:

```text
Decision A
→ Shared State

Decision B
→ Shared State

Conflict
→ Agent Output Inconsistency
```

예시:

```text
Shared State Decision:
- Review list uses Slice

Backend Agent Output:
- Page response 사용

Conflict:
- Pagination 기준 충돌
```

---

### [핵심]

- Shared State Conflict는 현재 Workflow 기준 충돌이다.
- 서로 다른 Agent Output이 충돌할 수 있다.
- 오래된 Decision과 최신 Decision이 충돌할 수 있다.
- 미확정 사항이 Decision처럼 저장되면 충돌한다.
- PM Agent가 최종 Decision을 정리해야 한다.
- Review Agent는 Conflict를 Finding으로 작성해야 한다.
- Fix Agent는 확정된 Decision을 기준으로 수정해야 한다.
- Conflict를 숨기면 Final Output 품질이 떨어진다.

---

### [실무]

Shared State Conflict Record:

```md
## Shared State Conflict

### Conflict

Shared State는 Slice 목록 응답을 요구하지만 Backend Agent Output은 Page를 사용함

### Conflicting Items

- Decision: Review list uses Slice
- Backend Output: Page<ReviewResDto>

### Priority

Shared State Decision > Backend Agent Output

### Impact

Frontend Agent가 Pagination 구조를 잘못 설계할 수 있음

### Resolution

Backend Agent Output을 Slice 기준으로 수정

### Re-review Required

Yes
```

Conflict 해결 Flow:

```text
Conflict Detection
→ Priority Check
→ PM Agent Decision
→ Shared State Update
→ Affected Agent Output Fix
→ Re-review
```

---

### [FAQ]

Q. Shared State Conflict가 뭐야?
A. Shared State에 서로 충돌하는 결정사항, Agent Output, 요구사항이 존재하는 실패 유형이다.

Q. Shared State Conflict는 누가 정리해?
A. PM Agent가 최종 Decision을 정리하고 Shared State를 업데이트해야 한다.

Q. Conflict를 숨기면 어떻게 돼?
A. Agent들이 서로 다른 기준으로 작업해 Final Output이 불일치할 수 있다.

Q. Fix Agent는 무엇을 기준으로 수정해?
A. PM Agent가 확정한 Shared State Decision을 기준으로 수정한다.

---

## 4.2 Stale State

### [개념]

Stale State는 Shared State에 저장된 오래된 정보가 현재 User Request, 최신 PM Decision, 최신 Agent Output과 맞지 않는 실패 유형이다.

Stale State는 이전 Workflow의 정보가 현재 Workflow에 잘못 적용될 때 자주 발생한다.

기본 구조:

```text
Old State
→ New User Request
→ State Not Updated
→ Wrong Agent Context
→ Wrong Output
```

---

### [핵심]

- Stale State는 오래된 상태 정보이다.
- 현재 User Request가 가장 우선이다.
- 최신 PM Decision이 오래된 State보다 우선이다.
- 이전 Workflow State를 그대로 재사용하면 위험하다.
- State Update 시 lastUpdatedBy와 update reason을 기록하는 것이 좋다.
- 오래된 State는 Context Packaging에서 제외해야 한다.
- Stale State가 반복되면 State Lifecycle 규칙을 보강해야 한다.

---

### [실무]

Stale State 예시:

```md
## Failure Record

### Failure Type

Stale State

### Symptom

Documentation Agent가 이전 Part Topic을 기준으로 새 문서를 작성함

### Root Cause

Shared State currentPart가 Part12로 남아 있고 Part13 요청 후 갱신되지 않음

### Impact

잘못된 FileName, Title, Section 구성이 생성됨

### Immediate Fix

Current User Request 기준으로 currentPart를 Part13으로 갱신하고 문서 재작성

### Prevention Rule

새 Part 요청 시 State Initialization에서 currentPart를 반드시 갱신
```

Stale State 방지 Checklist:

```md
## Stale State Prevention Checklist

- [ ] Current User Request가 반영되었는가?
- [ ] currentStep이 최신인가?
- [ ] currentPart 또는 currentTask가 최신인가?
- [ ] 이전 Workflow 정보가 섞이지 않았는가?
- [ ] 오래된 Decision이 최신 Decision을 덮지 않았는가?
- [ ] Context Packaging에서 오래된 정보가 제외되었는가?
```

---

### [FAQ]

Q. Stale State가 뭐야?
A. Shared State에 저장된 오래된 정보가 현재 요청이나 최신 결정과 맞지 않는 실패 유형이다.

Q. Stale State가 왜 위험해?
A. Agent가 오래된 정보를 기준으로 작업해 잘못된 Output을 만들 수 있기 때문이다.

Q. Stale State를 어떻게 방지해?
A. 새 Workflow 시작 시 State Initialization을 수행하고 Current User Request를 최우선으로 반영해야 한다.

Q. 이전 Workflow State를 그대로 재사용해도 돼?
A. 안 된다. 현재 요청과 관련 있는 정보만 선별해야 한다.

---

# 5. RAG Failure

## 5.1 RAG Scope Failure

### [개념]

RAG Scope Failure는 Agent가 잘못된 문서 범위를 검색하거나 필요한 문서를 누락하거나 관련 없는 문서를 근거로 사용하는 실패 유형이다.

RAG Scope Failure는 Hallucination, Domain Rules 위반, Output 품질 저하로 이어진다.

기본 구조:

```text
Wrong RAG Scope
→ Wrong Context
→ Wrong Agent Output
→ Review Failure
```

---

### [핵심]

- RAG Scope는 Agent Role과 일치해야 한다.
- Scope Too Broad는 관련 없는 Context를 섞는다.
- Scope Too Narrow는 필요한 문서를 누락한다.
- Wrong Domain Scope는 잘못된 Output을 만든다.
- Missing Master Rules는 공통 구조 위반을 만든다.
- Missing Domain Rules는 도메인 품질 저하를 만든다.
- RAG Context를 현재 요청보다 우선하면 안 된다.
- RAG Scope Failure는 Query Expansion, Query Narrowing, Scope 재설정으로 해결한다.

---

### [실무]

RAG Scope Failure 예시:

```md
## Failure Record

### Failure Type

RAG Scope Failure - Missing Domain Rules

### Symptom

RAG 문서가 Multi-Agent System Domain Rules 용어와 맞지 않음

### Root Cause

Documentation Agent RAG Scope에 Target Domain Rules가 포함되지 않음

### Impact

문서가 프로젝트 기준과 충돌하고 Retrieval 품질이 낮아짐

### Immediate Fix

RAG Scope에 Multi-Agent System Domain Rules를 추가하고 문서를 재검토

### Prevention Rule

RAG 문서 제작 Handoff에는 Master Rules, Target Domain Rules, Project Progress를 필수 포함
```

RAG Scope Troubleshooting:

| 증상                | 원인                 | 해결                     |
| ------------------- | -------------------- | ------------------------ |
| 관련 없는 문서 검색 | Scope Too Broad      | Query Narrowing          |
| 필요한 규칙 누락    | Scope Too Narrow     | Scope 확장               |
| Domain 용어 불일치  | Missing Domain Rules | Target Domain Rules 추가 |
| 문서 구조 위반      | Missing Master Rules | Master Rules 추가        |
| 오래된 기준 사용    | Stale RAG Context    | Current Decision 우선    |
| Agent 추측 증가     | Insufficient Context | Query Expansion          |

---

### [FAQ]

Q. RAG Scope Failure는 뭐야?
A. Agent가 잘못된 문서 범위를 검색하거나 필요한 문서를 누락하거나 관련 없는 문서를 근거로 사용하는 실패다.

Q. Scope Too Broad는 어떤 문제야?
A. 관련 없는 문서가 섞여 Agent Output이 흔들릴 수 있다.

Q. Scope Too Narrow는 어떤 문제야?
A. 필요한 문서가 검색되지 않아 Agent가 추측으로 작업할 수 있다.

Q. RAG Scope Failure는 어떻게 고쳐?
A. Query Expansion, Query Narrowing, Target Domain Rules 추가, RAG Scope 재설정을 수행한다.

---

## 5.2 Hallucination from Missing Context

### [개념]

Hallucination from Missing Context는 Agent가 필요한 Context 없이 누락된 정보를 추측으로 채우는 실패 유형이다.

Multi-Agent System에서는 Missing Context가 Handoff, RAG Retrieval, Shared State, Tool Result 어디에서든 발생할 수 있다.

기본 구조:

```text
Missing Context
→ Agent Assumption
→ Assumption Not Marked
→ False Output
```

---

### [핵심]

- Missing Context는 Hallucination 위험을 높인다.
- Agent는 없는 정보를 확정하면 안 된다.
- 부족한 정보는 Assumption 또는 Open Question으로 표시해야 한다.
- 필수 정보가 없으면 Blocked 상태를 반환해야 한다.
- RAG 검색 결과가 부족하면 Sufficiency를 낮게 표시해야 한다.
- Handoff Context가 부족하면 PM Agent에게 반환해야 한다.
- Tool Result가 없으면 실행 결과를 추측하면 안 된다.

---

### [실무]

Hallucination 예시:

```md
## Failure Record

### Failure Type

Hallucination from Missing Context

### Symptom

Frontend Agent가 존재하지 않는 Backend Response Field를 기준으로 State를 설계함

### Root Cause

Backend API Response DTO가 제공되지 않았지만 Agent가 필드명을 추측함

### Impact

Frontend와 Backend API Contract가 불일치할 수 있음

### Immediate Fix

ReviewResDto Field를 Required Context로 요청하고 추측한 필드를 Assumption으로 분리

### Prevention Rule

필수 API Contract가 없으면 Frontend Agent는 Blocked 또는 Partial 상태를 반환
```

Missing Context 처리 기준:

```text
필수 Context 없음
→ Blocked

일부 Context 부족
→ Partial + Assumption

검증되지 않은 정보
→ Assumption

사용자 결정 필요
→ Open Question

위험 작업 정보 부족
→ Stop + Approval Request
```

---

### [FAQ]

Q. Hallucination from Missing Context가 뭐야?
A. Agent가 필요한 Context 없이 누락된 정보를 추측으로 채우는 실패 유형이다.

Q. Missing Context가 있으면 어떻게 해야 해?
A. Assumption, Open Question, Partial, Blocked 중 하나로 명시해야 한다.

Q. 필수 Context가 없는데 작업을 계속해도 돼?
A. 위험하다. 필수 Context가 없으면 Blocked 상태로 반환해야 한다.

Q. Tool Result가 없으면 결과를 추측해도 돼?
A. 안 된다. Tool 실행 결과가 없으면 확정처럼 작성하면 안 된다.

---

# 6. Review-Fix Failure

## 6.1 Review-Fix Infinite Loop

### [개념]

Review-Fix Infinite Loop는 Review Agent와 Fix Agent가 반복적으로 새로운 문제와 수정을 만들며 Workflow가 종료되지 않는 실패 유형이다.

Review-Fix Infinite Loop는 Review Criteria가 고정되지 않았거나, Minor Issue를 계속 수정하거나, Fix Agent가 새 요구사항을 추가할 때 발생한다.

기본 구조:

```text
Review
→ Fix
→ New Criteria
→ New Fix
→ New Criteria
→ Infinite Loop
```

---

### [핵심]

- Review-Fix Infinite Loop는 무한 반복 문제이다.
- Max Iteration이 없으면 발생하기 쉽다.
- Stop Condition이 없으면 발생한다.
- Review Criteria가 반복 중 바뀌면 발생한다.
- Minor Issue를 계속 수정하면 발생한다.
- Fix Agent가 새 요구사항을 추가하면 발생한다.
- Critical Issue 0개이면 Pass 후보로 본다.
- Minor Issue만 남으면 Pass with Notes로 종료할 수 있다.
- 새 요구사항은 PM Agent에게 반환해야 한다.

---

### [실무]

Infinite Loop 예시:

```md
## Failure Record

### Failure Type

Review-Fix Infinite Loop

### Symptom

RAG 문서 Review와 Fix가 4회 이상 반복되며 매번 새로운 Minor 표현 개선이 추가됨

### Root Cause

Stop Condition과 Max Iteration이 설정되지 않음

### Impact

작업이 종료되지 않고 Token 비용과 Latency가 증가함

### Immediate Fix

Critical / Major Issue가 없으면 Pass with Notes로 종료

### Prevention Rule

Review-Fix Loop는 기본 Max Iteration 2회, Minor만 남으면 종료
```

Stop Condition Template:

```md
## Review-Fix Stop Condition

- [ ] Critical Issue 0개
- [ ] Major Issue 해결 또는 PM Decision으로 분리
- [ ] Minor Issue만 남음
- [ ] Max Iteration 도달
- [ ] 사용자 확인 필요 항목은 Open Question으로 분리
```

---

### [FAQ]

Q. Review-Fix Infinite Loop가 뭐야?
A. Review Agent와 Fix Agent가 반복적으로 새로운 문제와 수정을 만들며 Workflow가 종료되지 않는 실패다.

Q. 왜 무한 반복이 생겨?
A. Max Iteration, Stop Condition, 고정된 Review Criteria가 없기 때문이다.

Q. Minor Issue만 남으면 어떻게 해?
A. Pass with Notes로 종료할 수 있다.

Q. Fix Agent가 새 요구사항을 발견하면?
A. 직접 반영하지 말고 PM Agent에게 반환해야 한다.

---

## 6.2 Over-fixing

### [개념]

Over-fixing은 Fix Agent가 Review Findings를 해결하는 데 필요한 범위를 넘어 불필요하게 구조를 크게 변경하는 실패 유형이다.

Over-fixing은 기존 요구사항 훼손, Regression, Agent Output 충돌을 만들 수 있다.

기본 구조:

```text
Small Finding
→ Large Fix
→ Existing Requirement Broken
→ Regression
```

---

### [핵심]

- Over-fixing은 수정 범위 과다 확장이다.
- Fix Agent는 Review Findings 범위 안에서 수정해야 한다.
- 최소 수정 원칙을 적용한다.
- API Contract를 무단 변경하면 안 된다.
- DB Schema를 무단 변경하면 안 된다.
- 기존 요구사항을 삭제하면 안 된다.
- 새 요구사항을 만들면 안 된다.
- Over-fixing은 Regression Evaluation 대상이다.

---

### [실무]

Over-fixing 예시:

```md
## Failure Record

### Failure Type

Over-fixing

### Symptom

Rating Validation 누락을 고치는 과정에서 Review API Path 전체가 변경됨

### Root Cause

Fix Scope가 정의되지 않음

### Impact

Frontend Agent Output과 API Contract가 충돌함

### Immediate Fix

API Path 변경을 되돌리고 Rating Validation만 추가

### Prevention Rule

Fix Agent는 Review Finding별 Minimal Required Change를 정의한 뒤 수정
```

Minimal Fix 원칙:

```md
## Minimal Fix Principle

- Review Finding과 직접 관련된 부분만 수정
- 기존 API Contract 유지
- 기존 Requirements 유지
- 기존 Domain Rules 유지
- 영향 범위 표시
- Regression Risk 기록
```

---

### [FAQ]

Q. Over-fixing이 뭐야?
A. Fix Agent가 Review Findings를 해결하는 데 필요한 범위를 넘어 불필요하게 구조를 크게 변경하는 실패다.

Q. Over-fixing이 왜 위험해?
A. 기존 요구사항 훼손, API 충돌, Regression, Review-Fix 반복을 만든다.

Q. Over-fixing은 어떻게 방지해?
A. Fix Scope와 Minimal Required Change를 명확히 정의해야 한다.

Q. Over-fixing이 발생하면 어떻게 해?
A. 과도한 변경을 되돌리고 Review Finding과 직접 관련된 최소 수정만 적용한다.

---

# 7. Tool Permission Failure

## 7.1 Unauthorized Tool Use

### [개념]

Unauthorized Tool Use는 Agent가 권한이 없는 Tool을 사용하거나 위험 Tool을 승인 없이 실행하려는 실패 유형이다.

Tool Permission Failure는 데이터 손상, 서비스 중단, 비용 발생, 보안 사고로 이어질 수 있다.

기본 구조:

```text
Agent Request Tool
→ Permission Not Allowed
→ Tool Execution Attempt
→ Safety Failure
```

---

### [핵심]

- Agent는 권한 없는 Tool을 사용하면 안 된다.
- Dangerous Tool은 Human Approval이 필요하다.
- File Delete는 승인 대상이다.
- DB Write와 Migration은 승인 대상이다.
- Deploy와 Restart는 승인 대상이다.
- Email Send와 Payment는 승인 대상이다.
- 권한이 없으면 PM Agent에게 반환해야 한다.
- Tool Result는 기록해야 한다.
- Tool Failure를 숨기면 안 된다.

---

### [실무]

Unauthorized Tool Use 예시:

```md
## Failure Record

### Failure Type

Unauthorized Tool Use

### Symptom

Review Agent가 직접 파일 수정을 시도함

### Root Cause

Review Agent Tool Permission과 Fix Agent Tool Permission이 분리되지 않음

### Impact

Review와 Fix 책임 경계가 무너지고 변경 추적이 어려워짐

### Immediate Fix

Review Agent는 Review Findings만 작성하고 Fix Agent에게 수정 요청

### Prevention Rule

Review Agent Tool Permission에서 File Write와 Code Modify를 금지
```

Dangerous Tool 차단 예시:

```md
## Permission Block

### Requested Tool

Production Deploy

### Requested By

DevOps Agent

### Decision

Blocked

### Reason

Human Approval required

### Next Action

Approval Request 생성
```

---

### [FAQ]

Q. Unauthorized Tool Use가 뭐야?
A. Agent가 권한이 없는 Tool을 사용하거나 위험 Tool을 승인 없이 실행하려는 실패다.

Q. 위험 Tool은 어떤 것이 있어?
A. 파일 삭제, DB 변경, Migration, 배포, 서비스 재시작, 이메일 발송, 결제 실행 등이 있다.

Q. 위험 Tool을 실행하려면 뭐가 필요해?
A. Human Approval, Impact 설명, Risk 설명, Rollback Plan이 필요하다.

Q. 권한 없는 Tool 요청은 어떻게 처리해?
A. 실행하지 않고 PM Agent에게 반환하거나 Approval Request를 생성한다.

---

## 7.2 Tool Result Missing

### [개념]

Tool Result Missing은 Agent가 Tool을 사용했거나 사용해야 했는데 그 결과가 Shared State나 Agent Output에 기록되지 않는 실패 유형이다.

Tool Result가 누락되면 다음 Agent는 실제 실행 결과를 확인할 수 없고, 추측으로 작업할 가능성이 커진다.

기본 구조:

```text
Tool Call
→ Result
→ Not Recorded
→ Next Agent Missing Context
→ Wrong Output
```

---

### [핵심]

- Tool Result는 기록되어야 한다.
- 성공 결과와 실패 결과 모두 기록해야 한다.
- Partial Result도 표시해야 한다.
- Tool Failure를 숨기면 안 된다.
- 민감정보는 마스킹해야 한다.
- Tool Result가 없으면 확정 결과처럼 말하면 안 된다.
- 다음 Agent가 필요한 결과는 Shared State에 반영해야 한다.
- Tool Result Missing은 Review Agent가 검토해야 한다.

---

### [실무]

Tool Result Missing 예시:

```md
## Failure Record

### Failure Type

Tool Result Missing

### Symptom

DevOps Agent가 로그를 확인했다고 했지만 Log Result Summary가 없음

### Root Cause

Tool Result State 기록 규칙이 적용되지 않음

### Impact

Review Agent가 장애 원인 분석 근거를 검토할 수 없음

### Immediate Fix

Log Read 결과 요약, Status, Failure 여부를 Tool Result State에 기록

### Prevention Rule

Tool 사용 후 Tool Result State를 필수 작성
```

Tool Result State 최소 기준:

```json
{
  "toolCallId": "TOOL-001",
  "agent": "DevOps Agent",
  "tool": "Log Read",
  "status": "completed",
  "resultSummary": [
    "Backend container started successfully",
    "Database connection failed"
  ],
  "nextAction": "Check DB connection configuration"
}
```

---

### [FAQ]

Q. Tool Result Missing이 뭐야?
A. Agent가 Tool을 사용했거나 사용해야 했는데 그 결과가 기록되지 않는 실패 유형이다.

Q. Tool Result가 없으면 왜 문제야?
A. 다음 Agent가 실제 결과를 확인할 수 없어 추측으로 작업할 수 있다.

Q. Tool 실패도 기록해야 해?
A. 해야 한다. Failure Type, Reason, Required Permission, Next Action을 기록해야 한다.

Q. 민감정보가 있는 Tool Result는 어떻게 해?
A. 마스킹하거나 필요한 요약만 기록해야 한다.

---

# 8. Workflow Failure

## 8.1 Wrong Workflow Pattern

### [개념]

Wrong Workflow Pattern은 사용자 요청에 맞지 않는 Workflow Pattern을 선택해 불필요한 Agent가 실행되거나 필요한 Agent가 누락되는 실패 유형이다.

Workflow Pattern이 잘못 선택되면 Latency 증가, 요구사항 누락, 위험 작업 승인 누락, Final Output 품질 저하가 발생한다.

기본 구조:

```text
User Request
→ Wrong Pattern Selection
→ Wrong Agent Steps
→ Output Failure
```

---

### [핵심]

- Workflow Pattern은 요청 유형에 맞아야 한다.
- 단순 질문에 복잡한 Workflow를 쓰면 비효율적이다.
- 복합 개발 작업에 Single Agent를 쓰면 누락이 발생한다.
- 위험 작업에 Human-in-the-Loop이 없으면 위험하다.
- 문서 제작에 RAG Document Workflow가 없으면 Output Format 위반이 발생할 수 있다.
- Pattern Selection은 PM Agent가 수행한다.
- Pattern 선택 결과는 Shared State에 기록할 수 있다.

---

### [실무]

Wrong Pattern 예시:

```md
## Failure Record

### Failure Type

Wrong Workflow Pattern

### Symptom

DB, Backend, Frontend가 모두 필요한 기능 개발 요청을 Single Agent Workflow로 처리함

### Root Cause

PM Agent가 Domain Count와 Dependency를 평가하지 않음

### Impact

DB Schema, API Contract, Frontend 연동 일관성 검토가 누락됨

### Immediate Fix

Sequential Workflow로 변경하고 SQL → Backend → Frontend → Review 순서로 재실행

### Prevention Rule

Domain Count가 2개 이상이고 의존성이 있으면 Sequential Workflow를 우선 검토
```

Pattern Selection Troubleshooting:

| 증상                      | 잘못된 Pattern   | 권장 Pattern          |
| ------------------------- | ---------------- | --------------------- |
| 단순 질문인데 응답이 느림 | Sequential       | Single Agent          |
| DB/API/UI 누락            | Single Agent     | Sequential            |
| 배포 승인 없이 진행       | PM-Specialist    | HITL                  |
| 문서 형식 위반            | General Workflow | RAG Document Workflow |
| Agent 선택 오류           | Manual Selection | Router-based          |
| 복잡한 작업 계획 없음     | Direct Execution | Planner-Executor      |

---

### [FAQ]

Q. Wrong Workflow Pattern이 뭐야?
A. 사용자 요청에 맞지 않는 Workflow Pattern을 선택해 필요한 Agent가 누락되거나 불필요한 Agent가 실행되는 실패다.

Q. 복합 개발 작업에 Single Agent Workflow를 쓰면 왜 문제야?
A. DB, Backend, Frontend 의존성과 일관성 검토가 누락될 수 있다.

Q. 위험 작업에는 어떤 Workflow가 필요해?
A. Human-in-the-Loop Workflow가 필요하다.

Q. Wrong Workflow Pattern은 어떻게 방지해?
A. PM Agent가 Complexity, Domain Count, Risk, Review Need, Approval Need를 기준으로 Pattern을 선택해야 한다.

---

## 8.2 Final Integration Failure

### [개념]

Final Integration Failure는 PM Agent가 여러 Agent Output을 통합할 때 충돌, 누락, 중복, 미해결 Open Question을 정리하지 못하는 실패 유형이다.

Final Integration은 사용자에게 전달되는 최종 품질을 결정한다.

기본 구조:

```text
Agent Outputs
→ PM Agent Integration
→ Conflict Not Resolved
→ Final Output Failure
```

---

### [핵심]

- Final Integration은 PM Agent의 핵심 책임이다.
- Agent Output 간 충돌을 해결해야 한다.
- 중복 내용을 정리해야 한다.
- 누락 요구사항을 확인해야 한다.
- Review Findings가 반영되었는지 확인해야 한다.
- Open Questions를 숨기면 안 된다.
- Final Output은 사용자 요청 형식에 맞아야 한다.
- 미해결 Critical Issue가 있으면 Final Output으로 넘기면 안 된다.

---

### [실무]

Final Integration Failure 예시:

```md
## Failure Record

### Failure Type

Final Integration Failure

### Symptom

최종 결과에 SQL Agent와 Backend Agent의 필드명이 서로 다르게 포함됨

### Root Cause

PM Agent가 Agent Output 간 Consistency Check를 수행하지 않음

### Impact

사용자가 일관되지 않은 설계를 받게 됨

### Immediate Fix

Shared State Decision을 기준으로 필드명을 통일하고 Review Agent 재검토 수행

### Prevention Rule

Final Output 전 Cross-Agent Consistency Checklist를 수행
```

Final Integration Checklist:

```md
## Final Integration Checklist

- [ ] Original User Request가 충족되었는가?
- [ ] 모든 핵심 Requirements가 반영되었는가?
- [ ] Agent Output 간 충돌이 해결되었는가?
- [ ] Shared State Decisions와 일치하는가?
- [ ] Review Findings가 반영되었는가?
- [ ] Critical Issue가 남아 있지 않은가?
- [ ] Open Questions가 숨겨지지 않았는가?
- [ ] 사용자 요청 Output Format을 지켰는가?
- [ ] 중복과 불필요한 내용을 정리했는가?
```

---

### [FAQ]

Q. Final Integration Failure가 뭐야?
A. PM Agent가 여러 Agent Output을 통합할 때 충돌, 누락, 중복, 미해결 질문을 정리하지 못하는 실패다.

Q. Final Integration은 누가 담당해?
A. PM Agent가 담당한다.

Q. Final Output 전에 확인해야 할 것은?
A. 사용자 요청 충족, Agent Output 일관성, Review Findings 반영, Critical Issue 제거, Output Format 준수다.

Q. 미해결 Open Question은 숨겨도 돼?
A. 안 된다. Final Output에 명확히 표시하거나 사용자 확인 대상으로 분리해야 한다.

---

# 9. Troubleshooting Process

## 9.1 Troubleshooting Flow

### [개념]

Troubleshooting Flow는 Multi-Agent Failure가 발생했을 때 원인을 찾고 수정하는 표준 절차이다.

Troubleshooting은 증상만 보고 바로 수정하지 않고, 관련 Agent, Handoff, Shared State, RAG Scope, Tool Result, Review Findings를 순서대로 확인한다.

기본 구조:

```text
Symptom
→ Failure Type
→ Related Agent
→ Handoff Check
→ State Check
→ RAG Check
→ Tool Check
→ Root Cause
→ Fix
→ Prevention
```

---

### [핵심]

- 증상만 보고 바로 수정하지 않는다.
- Failure Type을 먼저 분류한다.
- 관련 Agent를 확인한다.
- Handoff를 확인한다.
- Shared State를 확인한다.
- RAG Scope와 Retrieved Context를 확인한다.
- Tool Permission과 Tool Result를 확인한다.
- Review Findings를 확인한다.
- Root Cause를 정리한다.
- Immediate Fix와 Prevention Rule을 분리한다.

---

### [실무]

Troubleshooting Checklist:

```md
## Troubleshooting Checklist

- [ ] Symptom이 무엇인가?
- [ ] Failure Type은 무엇인가?
- [ ] 관련 Agent는 누구인가?
- [ ] Handoff에 Requirements가 있었는가?
- [ ] Handoff에 Constraints가 있었는가?
- [ ] Shared State Decision과 충돌하는가?
- [ ] RAG Scope가 적절했는가?
- [ ] Retrieved Context가 충분했는가?
- [ ] Tool Permission 위반이 있는가?
- [ ] Tool Result가 기록되었는가?
- [ ] Review Findings가 있었는가?
- [ ] Fix Scope가 적절했는가?
- [ ] Root Cause는 무엇인가?
- [ ] 재발 방지 규칙은 무엇인가?
```

Troubleshooting Report Template:

```md
## Troubleshooting Report

### Symptom

<문제 증상>

### Failure Type

<분류>

### Related Agents

- <Agent>

### Root Cause

<근본 원인>

### Evidence

<근거>

### Impact

<영향>

### Immediate Fix

<즉시 수정>

### Prevention Rule

<재발 방지>

### Re-run Required

<Yes | No>

### Re-review Required

<Yes | No>
```

---

### [FAQ]

Q. Troubleshooting Flow가 뭐야?
A. Multi-Agent Failure가 발생했을 때 증상, Failure Type, Handoff, State, RAG, Tool, Root Cause를 순서대로 확인하는 절차다.

Q. Troubleshooting에서 가장 먼저 할 일은?
A. 증상을 기록하고 Failure Type을 분류하는 것이다.

Q. 바로 Fix부터 하면 안 돼?
A. Root Cause를 모르면 같은 문제가 반복될 수 있으므로 먼저 원인을 확인해야 한다.

Q. Troubleshooting 결과에는 뭐가 있어야 해?
A. Symptom, Failure Type, Root Cause, Evidence, Impact, Immediate Fix, Prevention Rule이 있어야 한다.

---

## 9.2 Failure Prevention Checklist

### [개념]

Failure Prevention Checklist는 Multi-Agent Workflow 실행 전후에 반복적인 실패를 예방하기 위한 검수 기준이다.

이 Checklist는 PM Agent, Review Agent, Fix Agent가 공통으로 사용할 수 있다.

---

### [핵심]

- Agent Role이 명확한지 확인한다.
- Handoff가 충분한지 확인한다.
- Shared State가 최신인지 확인한다.
- RAG Scope가 적절한지 확인한다.
- Tool Permission이 제한되어 있는지 확인한다.
- Review Criteria가 고정되어 있는지 확인한다.
- Fix Scope가 제한되어 있는지 확인한다.
- Workflow Pattern이 요청에 맞는지 확인한다.
- Final Integration 전에 충돌을 확인한다.

---

### [실무]

Failure Prevention Checklist:

```md
## Failure Prevention Checklist

### Agent Role

- [ ] Agent Role이 명확한가?
- [ ] Agent Scope가 명확한가?
- [ ] Forbidden Scope가 정의되었는가?

### Handoff

- [ ] Task가 명확한가?
- [ ] Requirements가 충분한가?
- [ ] Constraints가 분리되어 있는가?
- [ ] Expected Output이 명확한가?
- [ ] Done Criteria가 검증 가능한가?

### Shared State

- [ ] Current User Request가 최신인가?
- [ ] Decisions가 충돌하지 않는가?
- [ ] Open Questions가 분리되어 있는가?
- [ ] Stale State가 제거되었는가?

### RAG

- [ ] RAG Scope가 Agent Role과 맞는가?
- [ ] Master Rules가 필요한 경우 포함되었는가?
- [ ] Target Domain Rules가 포함되었는가?
- [ ] Retrieved Context가 충분한가?

### Tool

- [ ] Tool Permission이 Agent Role과 맞는가?
- [ ] Dangerous Tool이 Approval 대상으로 분리되었는가?
- [ ] Tool Result를 기록하는가?

### Review-Fix

- [ ] Review Criteria가 고정되어 있는가?
- [ ] Max Iteration이 있는가?
- [ ] Fix Scope가 제한되어 있는가?
- [ ] Regression Risk를 확인하는가?

### Final

- [ ] Agent Output 간 충돌이 해결되었는가?
- [ ] Critical Issue가 남아 있지 않은가?
- [ ] Final Output Format이 사용자 요청과 맞는가?
```

---

### [FAQ]

Q. Failure Prevention Checklist가 뭐야?
A. Multi-Agent Workflow 실행 전후에 반복적인 실패를 예방하기 위한 검수 기준이다.

Q. Failure Prevention Checklist는 누가 사용해?
A. PM Agent, Review Agent, Fix Agent가 공통으로 사용할 수 있다.

Q. 가장 중요한 예방 항목은?
A. Agent Role, Handoff Quality, Shared State 최신성, RAG Scope, Tool Permission, Review-Fix Stop Condition이다.

Q. Checklist를 매번 전부 써야 해?
A. 모든 항목을 장문으로 출력할 필요는 없지만 내부 검수 기준으로 적용하는 것이 좋다.

---

# 10. RAG Document Troubleshooting

## 10.1 RAG Document Failure

### [개념]

RAG Document Failure는 RAG 문서가 Retrieval 최적화 기준, Master Rules, Domain Rules, Output Format을 충족하지 못하는 실패 유형이다.

RAG 문서의 목적은 AI Agent가 검색하고 사용할 수 있는 지식 Chunk를 제공하는 것이므로, 문서 구조와 검색 표현이 중요하다.

주요 실패 유형:

```text
Required Section Missing
FAQ Missing
Retrieval Queries Missing
Output Format Violation
Domain Rules Not Applied
Human Essay Style
Terminology Inconsistency
Chunk Dependency Too High
```

---

### [핵심]

- RAG 문서는 Retrieval 최적화가 우선이다.
- Required Section 누락은 구조 실패이다.
- FAQ 누락은 검색 매칭 품질 저하를 만든다.
- Retrieval Queries 누락은 RAG 검색 성능 저하를 만든다.
- Output Format 위반은 사용자 요청 위반이다.
- Domain Rules 미적용은 도메인 품질 저하를 만든다.
- 사람용 에세이 스타일은 Agent Retrieval에 부적합할 수 있다.
- 용어 불일치는 검색과 응답 일관성을 떨어뜨린다.
- Chunk가 독립적이지 않으면 검색 결과 단독 활용이 어렵다.

---

### [실무]

RAG Document Failure 예시:

```md
## Failure Record

### Failure Type

RAG Document Failure - Retrieval Queries Missing

### Symptom

문서 마지막에 Retrieval Queries Block이 없음

### Root Cause

Documentation Agent Handoff에 Retrieval Queries 필수 조건이 명시되지 않음

### Impact

사용자 질문과 문서 Chunk 간 검색 매칭 성능이 낮아짐

### Immediate Fix

문서 마지막에 `# Retrieval Queries`와 Q/A FAQ Block 추가

### Prevention Rule

RAG Document Handoff Done Criteria에 Retrieval Queries 포함 여부를 필수 항목으로 추가
```

RAG Document Troubleshooting Matrix:

| 증상                   | 원인                    | 해결                  |
| ---------------------- | ----------------------- | --------------------- |
| Required Section 없음  | Master Rules 미적용     | Required Section 복구 |
| FAQ 약함               | 검색 질문 표현 부족     | Q/A 보강              |
| Retrieval Queries 없음 | Output 기준 누락        | 마지막 Block 추가     |
| 용어가 섞임            | Domain Rules 미적용     | 표준 용어 통일        |
| 문서가 장문 에세이     | RAG 최적화 기준 누락    | Chunk 구조로 재작성   |
| Output 밖 설명 있음    | 사용자 형식 위반        | Writing Block만 출력  |
| Part 주제 중복         | Project Progress 미확인 | Part Index 확인       |

---

### [FAQ]

Q. RAG Document Failure는 뭐야?
A. RAG 문서가 Retrieval 최적화 기준, Master Rules, Domain Rules, Output Format을 충족하지 못하는 실패다.

Q. RAG 문서에서 Retrieval Queries가 없으면 왜 문제야?
A. 사용자 질문 표현과 문서 Chunk 매칭이 약해져 검색 성능이 떨어질 수 있다.

Q. RAG 문서가 사람용 에세이처럼 작성되면 왜 문제야?
A. Agent가 필요한 정보를 독립 Chunk로 검색하고 사용하기 어렵기 때문이다.

Q. RAG Document Failure는 어떻게 줄여?
A. Required Section, FAQ, Retrieval Queries, Domain Rules, Output Format을 Quality Gate로 검수한다.

---

# Retrieval Queries

### [FAQ]

Q. Multi-Agent System에서 Failure는 뭐야?
A. Agent, Handoff, Shared State, RAG, Tool Permission, Workflow 중 하나 이상이 기준을 충족하지 못해 결과 품질이 떨어지는 상태다.

Q. Failure는 실행 오류만 의미해?
A. 아니다. 요구사항 누락, 역할 중복, 잘못된 Routing, RAG Scope 오류, Review-Fix 반복도 Failure다.

Q. Failure 분석에서 가장 중요한 것은?
A. 증상이 아니라 Root Cause를 찾는 것이다.

Q. Role Overlap이 뭐야?
A. 여러 Agent가 같은 책임을 중복 수행하거나 한 Agent가 자기 Scope 밖 작업을 수행하는 실패 유형이다.

Q. Role Overlap이 왜 문제야?
A. Agent Output 충돌, PM Agent 통합 실패, Review-Fix 반복 증가를 만든다.

Q. PM Agent Implementation Creep이 뭐야?
A. PM Agent가 조율자 역할을 넘어 Specialist Agent의 구현 작업까지 직접 수행하는 실패다.

Q. PM Agent가 구현을 직접 하면 왜 위험해?
A. Domain Rules, 보안, 예외 처리, 세부 검토가 누락될 수 있다.

Q. Poor Handoff가 뭐야?
A. Source Agent가 Target Agent에게 충분하지 않거나 모호한 작업 정보를 전달하는 실패 유형이다.

Q. Poor Handoff가 왜 위험해?
A. Target Agent가 추측으로 작업해 요구사항 누락, 규칙 위반, Output 충돌이 발생하기 때문이다.

Q. Missing Requirement Handoff가 뭐야?
A. Handoff에 필수 요구사항이 누락되어 Target Agent Output에서도 해당 기능이 빠지는 실패다.

Q. Output 누락은 항상 Specialist Agent 잘못이야?
A. 아니다. Handoff에 요구사항이 없었다면 PM Agent Handoff 문제가 Root Cause일 수 있다.

Q. Shared State Conflict가 뭐야?
A. Shared State에 서로 충돌하는 결정사항, Agent Output, 요구사항이 존재하는 실패 유형이다.

Q. Shared State Conflict는 누가 정리해?
A. PM Agent가 최종 Decision을 정리하고 Shared State를 업데이트해야 한다.

Q. Stale State가 뭐야?
A. Shared State에 저장된 오래된 정보가 현재 요청이나 최신 결정과 맞지 않는 실패 유형이다.

Q. Stale State가 왜 위험해?
A. Agent가 오래된 정보를 기준으로 작업해 잘못된 Output을 만들 수 있기 때문이다.

Q. RAG Scope Failure는 뭐야?
A. Agent가 잘못된 문서 범위를 검색하거나 필요한 문서를 누락하거나 관련 없는 문서를 근거로 사용하는 실패다.

Q. Scope Too Broad는 어떤 문제야?
A. 관련 없는 문서가 섞여 Agent Output이 흔들릴 수 있다.

Q. Scope Too Narrow는 어떤 문제야?
A. 필요한 문서가 검색되지 않아 Agent가 추측으로 작업할 수 있다.

Q. Hallucination from Missing Context가 뭐야?
A. Agent가 필요한 Context 없이 누락된 정보를 추측으로 채우는 실패 유형이다.

Q. Missing Context가 있으면 어떻게 해야 해?
A. Assumption, Open Question, Partial, Blocked 중 하나로 명시해야 한다.

Q. Review-Fix Infinite Loop가 뭐야?
A. Review Agent와 Fix Agent가 반복적으로 새로운 문제와 수정을 만들며 Workflow가 종료되지 않는 실패다.

Q. Review-Fix Loop가 무한 반복되는 이유는?
A. Max Iteration, Stop Condition, 고정된 Review Criteria가 없기 때문이다.

Q. Over-fixing이 뭐야?
A. Fix Agent가 Review Findings를 해결하는 데 필요한 범위를 넘어 불필요하게 구조를 크게 변경하는 실패다.

Q. Over-fixing이 왜 위험해?
A. 기존 요구사항 훼손, API 충돌, Regression, Review-Fix 반복을 만든다.

Q. Unauthorized Tool Use가 뭐야?
A. Agent가 권한이 없는 Tool을 사용하거나 위험 Tool을 승인 없이 실행하려는 실패다.

Q. 위험 Tool은 어떤 것이 있어?
A. 파일 삭제, DB 변경, Migration, 배포, 서비스 재시작, 이메일 발송, 결제 실행 등이 있다.

Q. Tool Result Missing이 뭐야?
A. Agent가 Tool을 사용했거나 사용해야 했는데 그 결과가 기록되지 않는 실패 유형이다.

Q. Tool Result가 없으면 왜 문제야?
A. 다음 Agent가 실제 결과를 확인할 수 없어 추측으로 작업할 수 있다.

Q. Wrong Workflow Pattern이 뭐야?
A. 사용자 요청에 맞지 않는 Workflow Pattern을 선택해 필요한 Agent가 누락되거나 불필요한 Agent가 실행되는 실패다.

Q. 복합 개발 작업에 Single Agent Workflow를 쓰면 왜 문제야?
A. DB, Backend, Frontend 의존성과 일관성 검토가 누락될 수 있다.

Q. Final Integration Failure가 뭐야?
A. PM Agent가 여러 Agent Output을 통합할 때 충돌, 누락, 중복, 미해결 질문을 정리하지 못하는 실패다.

Q. Final Output 전에 확인해야 할 것은?
A. 사용자 요청 충족, Agent Output 일관성, Review Findings 반영, Critical Issue 제거, Output Format 준수다.

Q. Troubleshooting Flow가 뭐야?
A. Multi-Agent Failure가 발생했을 때 증상, Failure Type, Handoff, State, RAG, Tool, Root Cause를 순서대로 확인하는 절차다.

Q. Troubleshooting에서 가장 먼저 할 일은?
A. 증상을 기록하고 Failure Type을 분류하는 것이다.

Q. Failure Prevention Checklist가 뭐야?
A. Multi-Agent Workflow 실행 전후에 반복적인 실패를 예방하기 위한 검수 기준이다.

Q. RAG Document Failure는 뭐야?
A. RAG 문서가 Retrieval 최적화 기준, Master Rules, Domain Rules, Output Format을 충족하지 못하는 실패다.

Q. RAG 문서에서 Retrieval Queries가 없으면 왜 문제야?
A. 사용자 질문 표현과 문서 Chunk 매칭이 약해져 검색 성능이 떨어질 수 있다.

Q. 개인 AI 개발팀에서 가장 자주 발생할 Failure는?
A. Poor Handoff, RAG Scope Failure, Shared State Conflict, Review-Fix Infinite Loop, PM Agent Implementation Creep이다.

Q. 개인 AI 개발팀에서 Failure를 줄이려면?
A. Agent Role, Handoff Template, Shared State, RAG Scope, Tool Permission, Review-Fix Stop Condition을 명확히 관리해야 한다.
