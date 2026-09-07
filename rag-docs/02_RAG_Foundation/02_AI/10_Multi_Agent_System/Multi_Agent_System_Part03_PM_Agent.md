# Multi-Agent System Part03 - PM Agent

---

# 1. PM Agent Core

## 1.1 PM Agent Definition

### [개념]

PM Agent는 Multi-Agent System의 중심 조율자이다.

PM Agent는 사용자의 요청을 직접 처리하는 대표 Agent이며, 요구사항 분석, 작업 분해, Agent 선택, Handoff 생성, 결과 통합, 최종 응답 생성을 담당한다.

PM Agent의 핵심은 직접 구현이 아니라 전체 Workflow를 안정적으로 운영하는 것이다.

기본 구조:

```text
User Request
→ PM Agent
→ Requirement Analysis
→ Task Decomposition
→ Agent Routing
→ Handoff
→ Specialist Agent
→ Review Agent
→ Final Output
```

개인 AI 개발팀 기준:

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

- PM Agent는 Multi-Agent System의 Coordinator이다.
- 사용자는 PM Agent에게만 요청한다.
- PM Agent는 User Request를 분석한다.
- PM Agent는 요구사항과 제약사항을 분리한다.
- PM Agent는 작업을 Agent 단위로 분해한다.
- PM Agent는 필요한 Specialist Agent를 선택한다.
- PM Agent는 Handoff를 생성한다.
- PM Agent는 Agent 결과를 통합한다.
- PM Agent는 최종 출력 품질에 책임을 가진다.
- PM Agent는 모든 Domain 작업을 직접 구현하지 않는다.

---

### [실무]

2026 실무 기준에서 PM Agent는 개발팀의 Project Manager, Tech Lead, Coordinator 역할을 합친 형태로 설계한다.

PM Agent 주요 책임:

- User Request Understanding
- Requirement Analysis
- Constraint Extraction
- Task Decomposition
- Agent Selection
- RAG Scope Selection
- Tool Permission Decision
- Handoff Generation
- Shared State Update
- Result Integration
- Review Request
- Final Output Generation

PM Agent는 사용자 요청을 그대로 Specialist Agent에게 넘기지 않는다.

나쁜 흐름:

```text
User: 회원가입 기능 만들어줘
→ PM Agent: Backend Agent에게 "회원가입 만들어줘" 전달
→ Backend Agent가 인증 방식, DTO, Validation, Response 형식을 추측
```

좋은 흐름:

```text
User: 회원가입 기능 만들어줘
→ PM Agent: 요구사항 분석
→ PM Agent: 인증 방식, DTO, Validation, Response Format 정리
→ PM Agent: Backend Agent에게 구조화된 Handoff 전달
→ Backend Agent: 명확한 Output 생성
→ Review Agent: 기준 검토
→ PM Agent: 최종 통합
```

---

### [FAQ]

Q. PM Agent는 뭐 하는 Agent야?
A. 사용자 요청을 분석하고 작업을 분해하며, 적절한 Agent에게 전달하고 최종 결과를 통합하는 조율자다.

Q. PM Agent가 직접 구현하면 안 돼?
A. 간단한 작업은 가능하지만, Multi-Agent 구조에서는 구현보다 분석, 분해, 라우팅, 통합에 집중하는 것이 좋다.

Q. 사용자는 어떤 Agent에게 요청해야 해?
A. 개인 AI 개발팀 구조에서는 사용자가 PM Agent에게만 요청하는 것이 가장 안정적이다.

Q. PM Agent가 중요한 이유는?
A. PM Agent의 요구사항 분석과 Handoff 품질이 전체 Agent 결과 품질을 결정하기 때문이다.

---

# 2. PM Agent Responsibility

## 2.1 User Request Understanding

### [개념]

User Request Understanding은 PM Agent가 사용자의 요청 의도, 작업 범위, 필요한 결과물을 파악하는 단계이다.

PM Agent는 사용자의 문장을 그대로 실행하지 않고, 요청의 Domain, 작업 유형, 제약사항, 누락 정보를 분석해야 한다.

분석 대상:

```text
User Intent
→ Task Type
→ Domain
→ Output Type
→ Constraints
→ Missing Context
→ Risk
```

---

### [핵심]

- PM Agent는 사용자의 요청 의도를 파악한다.
- 요청이 단순 질문인지 개발 작업인지 구분한다.
- 요청에 포함된 Domain을 감지한다.
- 필요한 Agent를 판단하기 위한 정보를 추출한다.
- 명시된 요구사항과 암묵적 요구사항을 구분한다.
- 누락된 Context를 식별한다.
- 위험 작업 여부를 판단한다.
- 현재 요청이 기존 Memory나 Shared State보다 우선한다.

---

### [실무]

User Request 분석 예시:

```text
User Request:
"리뷰 API 만들어줘"

PM Agent Analysis:
- Intent: Backend API 설계 또는 구현
- Domain: Backend, JPA, API Design, Security
- Required Agents: Backend Agent, Review Agent
- Possible Additional Agent: SQL Agent
- Missing Context:
  - Review Entity 존재 여부
  - 한 유저가 같은 축제에 리뷰를 여러 개 작성 가능한지
  - 인증 필요 여부
  - Response Format
- Risk:
  - Entity 구조를 추측할 가능성
  - API Contract 누락 가능성
```

PM Agent는 Missing Context가 있어도 모든 경우에 질문으로 멈추지 않는다.

처리 기준:

```text
치명적 누락 → 사용자 확인
일반적 누락 → Assumption 표시 후 진행
프로젝트 구조 관련 누락 → RAG / File Search 우선
위험 작업 관련 누락 → 사용자 승인 필요
```

---

### [FAQ]

Q. User Request Understanding이 뭐야?
A. PM Agent가 사용자의 요청 의도, Domain, 작업 유형, 제약, 누락 정보를 파악하는 단계다.

Q. PM Agent는 사용자 요청을 그대로 넘기면 안 돼?
A. 안 된다. 요청을 분석하지 않고 넘기면 Specialist Agent가 추측으로 결과를 만들 수 있다.

Q. 누락 정보가 있으면 무조건 질문해야 해?
A. 아니다. 치명적 누락은 확인하고, 일반적 누락은 Assumption으로 표시한 뒤 진행할 수 있다.

Q. 현재 요청과 기존 Memory가 충돌하면 뭐가 우선이야?
A. 현재 사용자 요청이 우선이다.

---

## 2.2 Requirement Analysis

### [개념]

Requirement Analysis는 PM Agent가 사용자의 요청에서 실제 요구사항을 추출하고 정리하는 단계이다.

요구사항은 기능 요구사항, 비기능 요구사항, 제약사항, 완료 기준으로 분리한다.

Requirement 구조:

```text
Functional Requirement
→ Non-functional Requirement
→ Constraint
→ Assumption
→ Done Criteria
```

---

### [핵심]

- 요구사항은 명확히 분리해야 한다.
- 기능 요구사항과 제약사항을 구분해야 한다.
- 암묵적 요구사항을 식별해야 한다.
- 완료 기준을 함께 정의해야 한다.
- 불확실한 내용은 Assumption으로 표시해야 한다.
- 위험한 내용은 Human Confirmation 대상으로 분류해야 한다.
- 요구사항은 Shared State에 기록해야 한다.

---

### [실무]

Requirement Analysis Template:

```json
{
  "functionalRequirements": [
    "사용자는 리뷰를 작성할 수 있다",
    "사용자는 리뷰 목록을 조회할 수 있다",
    "작성자는 자신의 리뷰를 수정할 수 있다",
    "작성자는 자신의 리뷰를 삭제할 수 있다"
  ],
  "nonFunctionalRequirements": [
    "목록 조회는 페이지네이션을 사용한다",
    "응답 형식은 ApiResponse를 따른다"
  ],
  "constraints": ["Spring Boot", "JPA", "JWT 인증", "MySQL"],
  "assumptions": [
    "인증 사용자는 SecurityContext에서 조회한다",
    "Review Entity는 Festivals, Users와 연관된다"
  ],
  "doneCriteria": [
    "API Contract 정의",
    "Request / Response DTO 정의",
    "Validation 기준 포함",
    "Exception Case 포함"
  ]
}
```

요구사항 분석 실패 예시:

```text
요청:
"리뷰 기능 만들어줘"

잘못된 분석:
- 리뷰 기능 구현

문제:
- 작성 / 조회 / 수정 / 삭제 범위 불명확
- 인증 여부 불명확
- Validation 기준 없음
- Response Format 없음
- Review Agent가 검토할 기준 없음
```

---

### [FAQ]

Q. Requirement Analysis가 뭐야?
A. 사용자 요청에서 기능 요구사항, 비기능 요구사항, 제약사항, 완료 기준을 분리해 정리하는 단계다.

Q. 요구사항과 제약사항은 달라?
A. 다르다. 요구사항은 해야 할 일이고, 제약사항은 작업을 수행할 때 지켜야 하는 조건이다.

Q. Done Criteria를 요구사항 분석에 포함해야 해?
A. 포함하는 것이 좋다. 완료 기준이 있어야 Agent 결과를 검토할 수 있다.

Q. Assumption은 왜 필요해?
A. 확정되지 않은 내용을 추정했을 때 오류 전파를 막기 위해 필요하다.

---

# 3. Task Decomposition

## 3.1 Task Decomposition Definition

### [개념]

Task Decomposition은 PM Agent가 하나의 사용자 요청을 여러 Agent가 수행할 수 있는 작은 작업 단위로 나누는 단계이다.

Multi-Agent System에서 Task Decomposition 품질은 전체 Workflow 품질을 결정한다.

기본 구조:

```text
User Request
→ Analyze Requirement
→ Split by Domain
→ Split by Dependency
→ Assign Agent
→ Define Expected Output
```

---

### [핵심]

- 복잡한 요청은 Agent 단위로 분해해야 한다.
- Domain 기준으로 작업을 나눈다.
- 작업 의존성을 고려한다.
- 각 작업마다 담당 Agent를 지정한다.
- 각 작업마다 Expected Output을 지정한다.
- 각 작업마다 Done Criteria를 지정한다.
- 분해된 Task는 Handoff로 전달된다.
- 작업 순서는 Sequential / Parallel 기준에 따라 결정한다.

---

### [실무]

Task Decomposition 예시:

```text
User Request:
"축제 리뷰 기능을 DB부터 화면까지 만들어줘"

Task Decomposition:
1. SQL Agent
   - reviews table 설계
   - FK / Index 후보 제안
   - 중복 리뷰 정책 Risk 표시

2. Backend Agent
   - Review API Contract 설계
   - DTO 설계
   - Service Method 설계
   - Validation / Exception 기준 작성

3. Frontend Agent
   - Review Component 구조 설계
   - Review Form State 설계
   - API 호출 흐름 설계
   - Loading / Error UX 설계

4. Review Agent
   - DB / API / Frontend Contract 일관성 검토
   - Security Risk 검토
   - Missing Requirement 검토

5. Fix Agent
   - Review Findings 반영
   - 변경 요약 작성
```

작업 의존성:

```text
DB Schema
→ Backend API Contract
→ Frontend API Integration
→ Review
→ Fix
```

---

### [FAQ]

Q. Task Decomposition이 뭐야?
A. 하나의 사용자 요청을 여러 Agent가 수행할 수 있는 작은 작업 단위로 나누는 것이다.

Q. Task는 어떤 기준으로 나눠?
A. Domain, 작업 의존성, Output, 책임 Agent 기준으로 나눈다.

Q. 작업 의존성이 있으면 어떻게 해야 해?
A. Sequential Multi-Agent 구조로 순서대로 실행하는 것이 안전하다.

Q. Task Decomposition이 나쁘면 어떻게 돼?
A. Agent가 중복 작업을 하거나 필요한 작업이 누락되고 결과 통합이 어려워진다.

---

## 3.2 Task Granularity

### [개념]

Task Granularity는 PM Agent가 작업을 얼마나 잘게 나눌지 결정하는 기준이다.

작업이 너무 크면 Specialist Agent가 추측을 많이 하게 되고, 작업이 너무 작으면 Handoff와 Latency가 증가한다.

적절한 Task Granularity는 Agent가 독립적으로 수행하고 Review Agent가 검토할 수 있는 크기이다.

---

### [핵심]

- Task는 너무 크면 안 된다.
- Task는 너무 작아도 비효율적이다.
- 하나의 Task는 하나의 주요 책임을 가져야 한다.
- 하나의 Task는 명확한 Output을 가져야 한다.
- 하나의 Task는 하나의 Done Criteria를 가져야 한다.
- Task는 Review 가능한 단위여야 한다.
- Agent 간 의존성을 고려해 분리해야 한다.

---

### [실무]

나쁜 Task Granularity:

```text
"전체 서비스 만들어줘"
```

문제:

- Domain 범위 과도함
- DB / Backend / Frontend / DevOps 혼합
- Output 불명확
- Review 기준 없음
- 실패 지점 추적 어려움

너무 작은 Task Granularity:

```text
1. DTO 이름 정하기
2. DTO 필드 하나 정하기
3. Controller 메서드 이름 정하기
4. Service 메서드 이름 정하기
```

문제:

- Handoff 과다
- Latency 증가
- PM Agent 통합 부담 증가
- 전체 흐름 파악 어려움

적절한 Task Granularity:

```text
1. Review DB Schema 설계
2. Review Backend API 설계
3. Review Frontend 연동 설계
4. Review-Fix 검토
```

---

### [FAQ]

Q. Task Granularity가 뭐야?
A. PM Agent가 작업을 얼마나 잘게 나눌지 결정하는 기준이다.

Q. 작업을 너무 크게 나누면 어떻게 돼?
A. Agent가 많은 내용을 추측하고 결과 품질이 떨어질 수 있다.

Q. 작업을 너무 작게 나누면 어떻게 돼?
A. Handoff와 Latency가 증가하고 PM Agent 통합 부담이 커진다.

Q. 좋은 Task 크기는?
A. 하나의 주요 책임과 명확한 Output을 가지며 Review 가능한 크기다.

---

# 4. Agent Routing

## 4.1 Agent Routing Definition

### [개념]

Agent Routing은 PM Agent가 분석된 작업을 적절한 Agent에게 배정하는 과정이다.

Routing 기준은 Domain, Task Type, Required Tool, RAG Scope, Risk, Confidence이다.

기본 Routing 구조:

```text
Task
→ Domain Detection
→ Task Type Classification
→ Agent Selection
→ RAG Scope Selection
→ Tool Permission Check
→ Handoff
```

---

### [핵심]

- PM Agent는 Task별로 담당 Agent를 선택한다.
- Routing은 Domain 기준으로 수행한다.
- 복합 요청은 여러 Agent로 나눈다.
- Confidence가 낮으면 Assumption 또는 Open Question을 표시한다.
- 위험 작업은 Human Confirmation 대상으로 분류한다.
- Agent별 RAG Scope를 함께 지정한다.
- Agent별 Tool Permission을 확인한다.
- Routing 결과는 Shared State에 기록할 수 있다.

---

### [실무]

Routing 기준 예시:

| Request / Task                            | Target Agent   |
| ----------------------------------------- | -------------- |
| DB Schema, Query, Index                   | SQL Agent      |
| Spring Boot, API, JPA, Security           | Backend Agent  |
| React, Component, State, API 연동         | Frontend Agent |
| Docker, Linux, Deploy, CI/CD              | DevOps Agent   |
| RAG, Prompt, Tool Calling, Agent Workflow | AI Agent       |
| 코드 검토, 문서 검수, 위험 확인           | Review Agent   |
| Review Findings 반영                      | Fix Agent      |
| 요구사항 분석, 작업 분해, 통합            | PM Agent       |

Routing 예시:

```text
User Request:
"회원가입 API랑 화면 연결까지 만들어줘"

PM Routing:
- Backend API 설계 → Backend Agent
- Frontend 연동 설계 → Frontend Agent
- API Contract 일관성 검토 → Review Agent
```

---

### [FAQ]

Q. Agent Routing이 뭐야?
A. PM Agent가 작업의 Domain과 유형을 판단해 적절한 Agent에게 배정하는 과정이다.

Q. Routing 기준은 뭐야?
A. Domain, Task Type, Required Tool, RAG Scope, Risk, Confidence다.

Q. 복합 요청은 하나의 Agent에게 보내면 돼?
A. 아니다. Domain별로 Task를 분해해 여러 Agent에게 보내는 것이 좋다.

Q. Routing 결과도 기록해야 해?
A. 기록하는 것이 좋다. Shared State에 남기면 추적과 Review가 쉬워진다.

---

## 4.2 Routing Confidence

### [개념]

Routing Confidence는 PM Agent가 특정 Task를 특정 Agent에게 배정하는 판단의 신뢰도이다.

Confidence가 낮으면 잘못된 Agent에게 작업을 보내거나 필요한 Agent를 누락할 수 있다.

Confidence 기준:

```text
High
→ Agent 명확
→ 바로 Handoff 가능

Medium
→ Agent는 추정 가능
→ Assumption 표시 후 진행

Low
→ Agent 불명확
→ 사용자 확인 또는 PM 재분석 필요
```

---

### [핵심]

- Routing에는 Confidence 판단이 필요하다.
- Confidence가 높으면 바로 Agent에게 전달한다.
- Confidence가 중간이면 Assumption을 표시한다.
- Confidence가 낮으면 확인 또는 재분석이 필요하다.
- Confidence가 낮은 상태에서 강행하면 오류 전파 가능성이 높다.
- Routing Confidence는 Handoff에 포함할 수 있다.

---

### [실무]

Routing Confidence 예시:

```json
{
  "task": "Design review API",
  "targetAgent": "Backend Agent",
  "routingConfidence": "High",
  "reason": "Spring Boot API 설계 요청이 명확함"
}
```

```json
{
  "task": "Fix deployment issue",
  "targetAgent": "DevOps Agent",
  "routingConfidence": "Medium",
  "reason": "배포 문제로 보이나 로그 정보가 부족함",
  "assumption": "Docker container 실행 문제로 가정"
}
```

```json
{
  "task": "이거 안 돼",
  "targetAgent": "Unknown",
  "routingConfidence": "Low",
  "reason": "Domain과 증상이 불명확함",
  "openQuestion": "오류 메시지, 관련 코드, 실행 환경 확인 필요"
}
```

---

### [FAQ]

Q. Routing Confidence가 뭐야?
A. PM Agent가 특정 작업을 특정 Agent에게 배정하는 판단의 신뢰도다.

Q. Confidence가 낮으면 어떻게 해?
A. 사용자 확인, 추가 Context 검색, PM 재분석을 수행해야 한다.

Q. Confidence가 중간이면 진행해도 돼?
A. 가능하다. 다만 Assumption을 명시하고 Review 단계에서 확인해야 한다.

Q. Routing Confidence를 Handoff에 넣어야 해?
A. 넣는 것이 좋다. 다음 Agent가 불확실성을 인지하고 작업할 수 있다.

---

# 5. PM Agent Handoff

## 5.1 Handoff Generation

### [개념]

Handoff Generation은 PM Agent가 Specialist Agent에게 전달할 작업 메시지를 구조화하는 단계이다.

PM Agent Handoff는 다음 Agent가 바로 작업할 수 있도록 Task, Context, Requirements, Constraints, RAG Scope, Tool Permission, Expected Output, Done Criteria를 포함해야 한다.

기본 Handoff 구조:

```json
{
  "from": "PM Agent",
  "to": "Backend Agent",
  "task": "",
  "requirements": [],
  "constraints": [],
  "context": [],
  "ragScope": [],
  "toolPermission": [],
  "expectedOutput": [],
  "doneCriteria": [],
  "assumptions": [],
  "openQuestions": []
}
```

---

### [핵심]

- Handoff는 Agent 간 작업 전달 형식이다.
- PM Agent는 자연어 요청을 구조화된 작업으로 변환한다.
- Task와 Context를 분리해야 한다.
- Requirements와 Constraints를 분리해야 한다.
- Expected Output을 명확히 지정해야 한다.
- Done Criteria를 포함해야 한다.
- Assumptions와 Open Questions를 포함해야 한다.
- RAG Scope와 Tool Permission을 지정해야 한다.

---

### [실무]

Backend Agent Handoff 예시:

```json
{
  "from": "PM Agent",
  "to": "Backend Agent",
  "task": "Design review API for festival review feature",
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
  "context": [
    "Festivals Entity exists",
    "Users Entity exists",
    "Rating range is 0 to 5"
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
    "Request DTO Design",
    "Response DTO Design",
    "Service Method Plan",
    "Exception Cases",
    "Risks"
  ],
  "doneCriteria": [
    "All endpoints defined",
    "Validation rule included",
    "Authentication rule included",
    "Exception case included",
    "Reviewable output generated"
  ],
  "assumptions": ["Authenticated user is resolved from SecurityContext"],
  "openQuestions": [
    "Can one user write multiple reviews for the same festival?"
  ]
}
```

---

### [FAQ]

Q. Handoff Generation이 뭐야?
A. PM Agent가 Specialist Agent에게 전달할 작업 메시지를 구조화하는 단계다.

Q. PM Agent Handoff에는 뭐가 들어가야 해?
A. Task, Requirements, Constraints, Context, RAG Scope, Tool Permission, Expected Output, Done Criteria, Assumptions, Open Questions가 들어가야 한다.

Q. Handoff가 부실하면 어떻게 돼?
A. Specialist Agent가 요구사항을 추측하고 결과 품질이 떨어질 수 있다.

Q. PM Agent가 Handoff에 RAG Scope도 넣어야 해?
A. 넣는 것이 좋다. Agent가 관련 문서만 검색하도록 도와준다.

---

## 5.2 Handoff Quality Check

### [개념]

Handoff Quality Check는 PM Agent가 Handoff를 전달하기 전에 누락, 모호성, 충돌, 과도한 범위를 검토하는 단계이다.

Handoff 품질이 낮으면 Specialist Agent와 Review Agent의 품질도 낮아진다.

검토 구조:

```text
Handoff
→ Missing Requirement Check
→ Constraint Check
→ Scope Check
→ Expected Output Check
→ Done Criteria Check
→ Risk Check
```

---

### [핵심]

- Handoff는 전달 전 검수해야 한다.
- Task가 명확한지 확인한다.
- 요구사항과 제약사항이 분리되었는지 확인한다.
- Scope가 과도하지 않은지 확인한다.
- Expected Output이 명확한지 확인한다.
- Done Criteria가 검증 가능한지 확인한다.
- Assumption이 표시되었는지 확인한다.
- Open Question이 누락되지 않았는지 확인한다.

---

### [실무]

Handoff Quality Checklist:

```md
## Handoff Quality Checklist

- [ ] Target Agent가 명확한가?
- [ ] Task가 한 문장으로 설명 가능한가?
- [ ] Requirements가 분리되어 있는가?
- [ ] Constraints가 분리되어 있는가?
- [ ] Context가 충분한가?
- [ ] RAG Scope가 적절한가?
- [ ] Tool Permission이 Scope와 일치하는가?
- [ ] Expected Output이 구체적인가?
- [ ] Done Criteria가 검증 가능한가?
- [ ] Assumptions가 표시되어 있는가?
- [ ] Open Questions가 표시되어 있는가?
- [ ] 위험 작업 여부가 확인되었는가?
```

Poor Handoff 예시:

```text
Backend Agent에게 회원가입 만들어달라고 전달
```

Good Handoff 예시:

```json
{
  "to": "Backend Agent",
  "task": "Design email signup API",
  "requirements": [
    "Email and password signup",
    "Duplicate email check",
    "Password validation"
  ],
  "constraints": ["Spring Boot", "JPA", "ApiResponse format"],
  "expectedOutput": ["API Contract", "DTO", "Service Plan", "Exception Cases"],
  "doneCriteria": [
    "Validation included",
    "Duplicate check included",
    "Error response included"
  ]
}
```

---

### [FAQ]

Q. Handoff Quality Check가 뭐야?
A. PM Agent가 Handoff를 전달하기 전에 누락, 모호성, 충돌, 범위를 검토하는 단계다.

Q. Handoff는 왜 검수해야 해?
A. Handoff 품질이 낮으면 다음 Agent 결과도 부정확해지기 때문이다.

Q. 좋은 Handoff 기준은?
A. Target Agent, Task, Requirements, Constraints, Expected Output, Done Criteria가 명확해야 한다.

Q. Handoff에 Open Question이 있으면 실패야?
A. 아니다. 불확실한 정보를 숨기지 않고 표시하는 것이 더 안전하다.

---

# 6. PM Agent and Shared State

## 6.1 Shared State Update

### [개념]

PM Agent는 Multi-Agent Workflow의 Shared State를 관리한다.

Shared State는 요구사항, 제약사항, 결정사항, Agent Output, Review Findings, 현재 상태를 기록하는 작업 상태이다.

PM Agent는 각 단계가 끝날 때 Shared State를 갱신해야 한다.

기본 구조:

```json
{
  "status": "in_progress",
  "currentStep": "task_decomposition",
  "requirements": [],
  "constraints": [],
  "decisions": [],
  "agentOutputs": {},
  "reviewFindings": [],
  "openQuestions": [],
  "finalResult": null
}
```

---

### [핵심]

- PM Agent는 Shared State 관리 책임을 가진다.
- 요구사항은 Shared State에 기록한다.
- 결정사항은 Shared State에 기록한다.
- Agent Output은 Shared State에 연결한다.
- Review Findings는 Shared State에 반영한다.
- Fix 결과는 Shared State를 업데이트해야 한다.
- 오래된 State가 최신 요청을 덮어쓰면 안 된다.
- 현재 User Request가 우선이다.

---

### [실무]

Shared State 업데이트 예시:

```json
{
  "status": "review_required",
  "currentStep": "backend_output_completed",
  "userRequest": "축제 리뷰 API 설계",
  "requirements": ["리뷰 작성", "리뷰 목록 조회", "리뷰 수정", "리뷰 삭제"],
  "constraints": ["JWT 인증", "ApiResponse 형식", "Slice 목록 응답"],
  "decisions": [
    "Rating range is 0 to 5",
    "Review author can update/delete own review"
  ],
  "agentOutputs": {
    "Backend Agent": "Review API Contract Draft"
  },
  "reviewFindings": [],
  "openQuestions": ["한 사용자가 같은 축제에 여러 리뷰를 작성할 수 있는가?"]
}
```

업데이트 시점:

```text
User Request 분석 후
→ requirements / constraints 기록

Task Decomposition 후
→ plannedTasks 기록

Agent Output 수신 후
→ agentOutputs 기록

Review 완료 후
→ reviewFindings 기록

Fix 완료 후
→ decisions / finalResult 갱신
```

---

### [FAQ]

Q. PM Agent가 Shared State를 관리해?
A. 그렇다. PM Agent는 Workflow의 요구사항, 결정사항, Agent 결과, Review 결과를 관리한다.

Q. Shared State에는 뭐가 들어가?
A. User Request, Requirements, Constraints, Decisions, Agent Outputs, Review Findings, Status가 들어간다.

Q. Shared State는 언제 업데이트해?
A. 요구사항 분석, 작업 분해, Agent 결과 수신, Review 완료, Fix 완료 시 업데이트한다.

Q. 오래된 Shared State와 현재 요청이 충돌하면?
A. 현재 요청이 우선이다.

---

## 6.2 Decision Management

### [개념]

Decision Management는 PM Agent가 Workflow 중 확정된 결정사항을 관리하는 작업이다.

Multi-Agent System에서는 Agent마다 다른 가정을 만들 수 있기 때문에, PM Agent가 최종 결정사항을 Shared State에 기록해야 한다.

결정사항 예시:

```text
API 경로
DTO 필드
DB 관계
인증 방식
응답 형식
Pagination 방식
삭제 정책
Review-Fix 기준
```

---

### [핵심]

- PM Agent는 결정사항을 기록해야 한다.
- 결정사항은 Agent 간 충돌을 줄인다.
- 결정사항은 Shared State에 저장한다.
- Specialist Agent는 기존 결정사항을 우선 따라야 한다.
- 결정사항 변경 시 영향 범위를 표시해야 한다.
- 충돌 발생 시 PM Agent가 최종 기준을 정리한다.
- Review Agent는 결정사항 위반 여부를 검토한다.

---

### [실무]

Decision Record 예시:

```json
{
  "decisionId": "D-001",
  "topic": "Review list pagination",
  "decision": "Use Slice instead of Page",
  "reason": "Infinite scroll and lightweight pagination",
  "affectedAgents": ["Backend Agent", "Frontend Agent", "Review Agent"],
  "status": "accepted"
}
```

Decision 변경 예시:

```json
{
  "decisionId": "D-002",
  "topic": "Review delete policy",
  "previousDecision": "Hard Delete",
  "newDecision": "Soft Delete",
  "reason": "Audit and recovery requirement added",
  "impact": [
    "Backend delete logic change",
    "Review list filter required",
    "DB column deleted_at required"
  ],
  "status": "changed"
}
```

---

### [FAQ]

Q. Decision Management가 뭐야?
A. PM Agent가 Workflow 중 확정된 API, DB, 인증, 응답 형식 같은 결정사항을 관리하는 작업이다.

Q. 결정사항은 왜 기록해야 해?
A. Agent 간 가정이 충돌하는 것을 막고 Review 기준으로 사용하기 위해서다.

Q. 결정사항은 어디에 저장해?
A. Shared State에 저장하는 것이 좋다.

Q. 결정사항을 바꿔도 돼?
A. 가능하지만 변경 이유와 영향 범위를 기록해야 한다.

---

# 7. PM Agent Result Integration

## 7.1 Agent Output Integration

### [개념]

Agent Output Integration은 PM Agent가 여러 Agent의 결과를 통합해 일관된 최종 결과로 정리하는 단계이다.

PM Agent는 Specialist Agent 결과를 단순히 붙여넣지 않고, 요구사항, 결정사항, Review Findings 기준으로 정리해야 한다.

통합 구조:

```text
Collect Agent Outputs
→ Check Requirement Coverage
→ Check Decision Consistency
→ Resolve Conflicts
→ Apply Review Findings
→ Generate Final Output
```

---

### [핵심]

- PM Agent는 Agent 결과를 통합한다.
- 단순 병합이 아니라 일관성 검토가 필요하다.
- 요구사항 충족 여부를 확인한다.
- 결정사항과 충돌하는 결과를 수정해야 한다.
- Agent 결과 간 API Contract 충돌을 확인한다.
- Review Findings를 반영해야 한다.
- 최종 출력은 사용자 목적에 맞게 정리해야 한다.
- 불확실한 내용은 Assumption 또는 Open Question으로 표시한다.

---

### [실무]

통합 검토 예시:

```text
SQL Agent Output:
- reviews table에 rating 컬럼 존재
- festival_id, user_id FK 존재

Backend Agent Output:
- ReviewReqDto에 rating 없음

PM Agent Integration Finding:
- Backend DTO가 DB Schema와 불일치
- Review Agent에게 검토 요청 또는 Backend Agent에게 수정 요청
```

PM Agent 통합 기준:

```md
## Integration Checklist

- [ ] Original Requirement가 모두 반영되었는가?
- [ ] Agent별 Output이 서로 충돌하지 않는가?
- [ ] API Contract가 Backend / Frontend에서 일치하는가?
- [ ] DB Schema와 Entity / DTO가 일치하는가?
- [ ] Security 요구사항이 반영되었는가?
- [ ] Review Findings가 처리되었는가?
- [ ] 남은 Open Question이 표시되었는가?
- [ ] Final Output이 사용자 목적에 맞는가?
```

---

### [FAQ]

Q. Agent Output Integration이 뭐야?
A. PM Agent가 여러 Agent의 결과를 요구사항과 결정사항 기준으로 통합하는 단계다.

Q. PM Agent는 Agent 결과를 그냥 합치면 돼?
A. 아니다. 충돌, 누락, 결정사항 위반, Review Findings 반영 여부를 확인해야 한다.

Q. 통합 단계에서 가장 중요한 것은?
A. 요구사항 충족과 Agent 결과 간 일관성이다.

Q. 충돌이 발견되면 어떻게 해?
A. PM Agent가 결정사항을 기준으로 조정하거나 Review / Fix Agent에게 전달해야 한다.

---

## 7.2 Final Output Generation

### [개념]

Final Output Generation은 PM Agent가 통합된 결과를 사용자에게 전달 가능한 형태로 정리하는 단계이다.

Final Output은 Agent 내부 로그 전체가 아니라 사용자가 이해하고 활용할 수 있는 최종 산출물이어야 한다.

출력 기준:

```text
User Goal
→ Final Result
→ Key Decisions
→ Implementation Summary
→ Risks
→ Next Steps
```

---

### [핵심]

- Final Output은 사용자 목적 중심이어야 한다.
- 내부 Agent 로그를 그대로 노출하지 않는다.
- 핵심 결정사항을 요약한다.
- 최종 산출물을 명확히 제공한다.
- 남은 Risk와 Open Question을 표시한다.
- 필요한 경우 다음 작업을 제안한다.
- 실패한 경우 실패 이유를 숨기지 않는다.
- 불확실한 내용은 확정처럼 말하지 않는다.

---

### [실무]

개발 작업 Final Output 예시:

```md
## Final Output

### Result

Review API 설계 완료

### API Contract

- POST /reviews
- GET /festivals/{festivalId}/reviews
- PATCH /reviews/{reviewId}
- DELETE /reviews/{reviewId}

### Key Decisions

- 목록 조회는 Slice 사용
- 작성자 본인만 수정 / 삭제 가능
- Rating은 0~5 범위 검증

### Risks

- 중복 리뷰 허용 정책 확인 필요
- Soft Delete 여부 확인 필요

### Next Step

Backend 구현 후 Review Agent 검토 권장
```

실패 Final Output 예시:

```md
## Final Output

### Status

Partial

### Completed

- 요구사항 분석 완료
- 필요한 Agent 식별 완료

### Blocked Reason

- Entity 구조와 API 응답 규칙이 제공되지 않음

### Required Context

- Users Entity
- Festivals Entity
- 기존 ApiResponse 규칙

### Next Step

프로젝트 구조 확인 후 Backend Agent 작업 진행
```

---

### [FAQ]

Q. Final Output Generation이 뭐야?
A. PM Agent가 통합된 Agent 결과를 사용자에게 전달 가능한 최종 산출물로 정리하는 단계다.

Q. Final Output에 Agent 내부 로그를 모두 넣어야 해?
A. 아니다. 사용자가 필요한 최종 결과, 결정사항, 위험, 다음 단계 중심으로 정리해야 한다.

Q. 작업이 실패하면 어떻게 출력해?
A. 실패 이유, 완료된 부분, 필요한 Context, 다음 조치를 명확히 표시해야 한다.

Q. PM Agent의 최종 책임은 뭐야?
A. 사용자가 이해하고 활용할 수 있는 정확하고 일관된 최종 결과를 제공하는 것이다.

---

# 8. PM Agent Failure Handling

## 8.1 PM Agent Failure Cases

### [개념]

PM Agent Failure는 요구사항 분석, 작업 분해, Routing, Handoff, 통합 과정에서 발생하는 실패이다.

PM Agent가 실패하면 전체 Multi-Agent Workflow의 결과가 흔들린다.

주요 실패 유형:

```text
Requirement Misread
Task Decomposition Failure
Wrong Routing
Poor Handoff
Shared State Conflict
Output Integration Failure
Unclear Final Output
```

---

### [핵심]

- PM Agent 실패는 전체 Workflow 실패로 이어진다.
- 요구사항 오해는 잘못된 Task 분해를 만든다.
- 잘못된 Routing은 부적절한 Agent 결과를 만든다.
- Poor Handoff는 Specialist Agent의 추측을 증가시킨다.
- Shared State 충돌은 Agent 결과 불일치를 만든다.
- 통합 실패는 최종 결과 품질을 낮춘다.
- 실패는 숨기지 않고 상태로 기록해야 한다.

---

### [실무]

PM Agent 실패 사례:

| 실패 유형                  | 원인                   | 해결                             |
| -------------------------- | ---------------------- | -------------------------------- |
| Requirement Misread        | 사용자 의도 오해       | 요구사항 재분석, Assumption 표시 |
| Task Decomposition Failure | Domain 분해 실패       | Domain별 Task 재분해             |
| Wrong Routing              | Agent 선택 오류        | Routing Rule 보강                |
| Poor Handoff               | Context / Output 누락  | Handoff Template 사용            |
| Shared State Conflict      | 오래된 결정사항 사용   | 현재 요청 우선, State 갱신       |
| Integration Failure        | Agent 결과 충돌 미검토 | Integration Checklist 적용       |
| Final Output Failure       | 내부 로그 중심 출력    | 사용자 목적 중심 재정리          |

Failure Flow:

```text
Failure Detected
→ Classify Failure
→ Update Shared State
→ Retry / Reroute / Ask User / Stop
→ Continue or Finalize
```

---

### [FAQ]

Q. PM Agent Failure가 뭐야?
A. PM Agent가 요구사항 분석, 작업 분해, Routing, Handoff, 통합 과정에서 실패하는 것이다.

Q. PM Agent 실패가 위험한 이유는?
A. PM Agent가 전체 Workflow를 조율하기 때문에 한 번의 오판이 모든 Agent 결과에 영향을 줄 수 있다.

Q. Poor Handoff는 PM Agent 실패야?
A. 대부분 그렇다. PM Agent가 Task, Context, Output 기준을 제대로 전달하지 못한 경우다.

Q. PM Agent 실패는 어떻게 처리해?
A. 실패 유형을 분류하고 Shared State에 기록한 뒤 Retry, Reroute, 사용자 확인, 중단 중 하나를 선택한다.

---

## 8.2 PM Agent Checklist

### [개념]

PM Agent Checklist는 PM Agent가 Workflow를 시작하고 완료하기 전에 확인해야 하는 검수 기준이다.

Checklist는 요구사항 누락, Agent 선택 오류, Handoff 부실, 통합 실패를 줄이기 위해 사용한다.

---

### [핵심]

- PM Agent는 작업 전 요구사항을 확인한다.
- PM Agent는 Agent 선택 근거를 확인한다.
- PM Agent는 Handoff 품질을 확인한다.
- PM Agent는 Shared State를 갱신한다.
- PM Agent는 Review 필요 여부를 판단한다.
- PM Agent는 최종 결과의 일관성을 확인한다.
- PM Agent는 위험 작업에 Human Confirmation을 적용한다.

---

### [실무]

PM Agent Pre-Execution Checklist:

```md
## PM Agent Pre-Execution Checklist

- [ ] User Request 의도를 파악했는가?
- [ ] Domain을 식별했는가?
- [ ] Functional Requirement를 분리했는가?
- [ ] Non-functional Requirement를 분리했는가?
- [ ] Constraints를 분리했는가?
- [ ] Missing Context를 식별했는가?
- [ ] Assumption을 표시했는가?
- [ ] 필요한 Agent를 선택했는가?
- [ ] Task Dependency를 확인했는가?
- [ ] Sequential / Parallel 실행 기준을 정했는가?
- [ ] Handoff를 구조화했는가?
- [ ] RAG Scope를 지정했는가?
- [ ] Tool Permission을 확인했는가?
- [ ] 위험 작업 여부를 확인했는가?
```

PM Agent Final Checklist:

```md
## PM Agent Final Checklist

- [ ] Original Requirement가 모두 반영되었는가?
- [ ] Agent Output 간 충돌이 없는가?
- [ ] Shared State 결정사항과 일치하는가?
- [ ] Review Findings가 반영되었는가?
- [ ] 남은 Risk가 표시되었는가?
- [ ] Open Question이 표시되었는가?
- [ ] Final Output이 사용자 목적에 맞는가?
- [ ] 불확실한 내용을 확정처럼 말하지 않았는가?
```

---

### [FAQ]

Q. PM Agent Checklist가 뭐야?
A. PM Agent가 요구사항 분석, Agent 선택, Handoff, 통합, 최종 출력을 검수하기 위한 기준이다.

Q. PM Agent Checklist는 언제 사용해?
A. Workflow 시작 전과 최종 출력 전 모두 사용한다.

Q. PM Agent가 반드시 확인해야 하는 것은?
A. 요구사항, 제약사항, Agent 선택, Handoff 품질, Shared State, Review 결과, 최종 출력 일관성이다.

Q. 위험 작업은 PM Agent가 어떻게 처리해?
A. Human Confirmation 대상으로 분류하고 사용자 승인 전에는 실행하지 않는다.

---

# Retrieval Queries

### [FAQ]

Q. PM Agent는 뭐야?
A. 사용자 요청을 분석하고 작업을 분해하며, 적절한 Agent에게 전달하고 최종 결과를 통합하는 Coordinator Agent다.

Q. PM Agent의 핵심 역할은?
A. Requirement Analysis, Task Decomposition, Agent Routing, Handoff Generation, Shared State Update, Result Integration, Final Output Generation이다.

Q. PM Agent가 직접 구현해도 돼?
A. 간단한 작업은 가능하지만 Multi-Agent 구조에서는 구현보다 조율, 분해, 라우팅, 통합에 집중하는 것이 좋다.

Q. 사용자는 어떤 Agent에게 요청해야 해?
A. 개인 AI 개발팀 구조에서는 사용자가 PM Agent에게만 요청하는 것이 가장 안정적이다.

Q. User Request Understanding이 뭐야?
A. PM Agent가 사용자의 요청 의도, Domain, 작업 유형, 제약, 누락 정보를 파악하는 단계다.

Q. PM Agent는 사용자 요청을 그대로 Specialist Agent에게 넘겨도 돼?
A. 안 된다. 요구사항과 제약을 구조화한 뒤 Handoff로 전달해야 한다.

Q. Requirement Analysis가 뭐야?
A. 사용자 요청에서 기능 요구사항, 비기능 요구사항, 제약사항, 완료 기준을 분리해 정리하는 단계다.

Q. 요구사항과 제약사항 차이는?
A. 요구사항은 해야 할 일이고, 제약사항은 작업을 수행할 때 지켜야 하는 조건이다.

Q. Task Decomposition이 뭐야?
A. 하나의 사용자 요청을 여러 Agent가 수행할 수 있는 작은 작업 단위로 나누는 것이다.

Q. Task는 어떤 기준으로 분해해?
A. Domain, 작업 의존성, Output, 담당 Agent 기준으로 분해한다.

Q. Task Granularity가 뭐야?
A. PM Agent가 작업을 얼마나 잘게 나눌지 결정하는 기준이다.

Q. 좋은 Task 크기는?
A. 하나의 주요 책임과 명확한 Output을 가지며 Review 가능한 크기다.

Q. Agent Routing이 뭐야?
A. PM Agent가 작업의 Domain과 유형을 판단해 적절한 Agent에게 배정하는 과정이다.

Q. Agent Routing 기준은?
A. Domain, Task Type, Required Tool, RAG Scope, Risk, Confidence다.

Q. Routing Confidence가 뭐야?
A. PM Agent가 특정 작업을 특정 Agent에게 배정하는 판단의 신뢰도다.

Q. Routing Confidence가 낮으면 어떻게 해?
A. 사용자 확인, 추가 Context 검색, PM 재분석을 수행해야 한다.

Q. PM Agent Handoff가 뭐야?
A. PM Agent가 Specialist Agent에게 전달할 Task, Requirements, Constraints, Context, RAG Scope, Expected Output, Done Criteria를 구조화한 메시지다.

Q. PM Agent Handoff에는 뭐가 들어가야 해?
A. Task, Requirements, Constraints, Context, RAG Scope, Tool Permission, Expected Output, Done Criteria, Assumptions, Open Questions가 들어가야 한다.

Q. Handoff Quality Check가 뭐야?
A. PM Agent가 Handoff를 전달하기 전에 누락, 모호성, 충돌, 범위를 검토하는 단계다.

Q. PM Agent가 Shared State를 관리해?
A. 그렇다. PM Agent는 Workflow의 요구사항, 결정사항, Agent 결과, Review 결과를 관리한다.

Q. Shared State는 언제 업데이트해?
A. 요구사항 분석, 작업 분해, Agent 결과 수신, Review 완료, Fix 완료 시 업데이트한다.

Q. Decision Management가 뭐야?
A. PM Agent가 Workflow 중 확정된 API, DB, 인증, 응답 형식 같은 결정사항을 관리하는 작업이다.

Q. 결정사항은 왜 기록해야 해?
A. Agent 간 가정이 충돌하는 것을 막고 Review 기준으로 사용하기 위해서다.

Q. Agent Output Integration이 뭐야?
A. PM Agent가 여러 Agent의 결과를 요구사항과 결정사항 기준으로 통합하는 단계다.

Q. PM Agent는 Agent 결과를 그냥 합치면 돼?
A. 아니다. 충돌, 누락, 결정사항 위반, Review Findings 반영 여부를 확인해야 한다.

Q. Final Output Generation이 뭐야?
A. PM Agent가 통합된 Agent 결과를 사용자에게 전달 가능한 최종 산출물로 정리하는 단계다.

Q. Final Output에는 Agent 내부 로그를 모두 넣어야 해?
A. 아니다. 사용자가 필요한 최종 결과, 결정사항, 위험, 다음 단계 중심으로 정리해야 한다.

Q. PM Agent Failure가 뭐야?
A. PM Agent가 요구사항 분석, 작업 분해, Routing, Handoff, 통합 과정에서 실패하는 것이다.

Q. PM Agent 실패가 위험한 이유는?
A. PM Agent가 전체 Workflow를 조율하기 때문에 한 번의 오판이 모든 Agent 결과에 영향을 줄 수 있기 때문이다.

Q. PM Agent Checklist가 뭐야?
A. PM Agent가 요구사항 분석, Agent 선택, Handoff, 통합, 최종 출력을 검수하기 위한 기준이다.

Q. PM Agent가 위험 작업을 발견하면 어떻게 해?
A. Human Confirmation 대상으로 분류하고 사용자 승인 전에는 실행하지 않는다.

Q. 개인 AI 개발팀에서 PM Agent가 중요한 이유는?
A. 사용자가 PM Agent에게만 요청하고, PM Agent가 SQL, Backend, Frontend, DevOps, AI, Review Agent로 작업을 분배하기 때문이다.
