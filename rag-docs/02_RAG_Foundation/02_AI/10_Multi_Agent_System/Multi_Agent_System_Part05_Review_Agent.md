# Multi-Agent System Part05 - Review Agent

---

# 1. Review Agent Core

## 1.1 Review Agent Definition

### [개념]

Review Agent는 Multi-Agent System에서 다른 Agent가 만든 산출물을 독립적으로 검증하는 Agent이다.

Review Agent는 단순히 비판하는 Agent가 아니라, 요구사항, Domain Rules, Shared State, Handoff, Done Criteria, 위험 요소를 기준으로 산출물 품질을 확인한다.

Review Agent의 핵심은 문제를 찾는 것뿐 아니라 문제의 원인, 영향, Severity, 수정 방향을 구조화해서 Fix Agent 또는 PM Agent가 바로 사용할 수 있게 만드는 것이다.

기본 구조:

```text
Specialist Agent Output
→ Review Agent
→ Requirement Check
→ Domain Rules Check
→ Consistency Check
→ Risk Check
→ Findings
→ Pass / Fail
```

Review-Fix 구조:

```text
Draft Output
→ Review Agent
→ Review Findings
→ Fix Agent
→ Updated Output
→ Re-review
→ Final Output
```

---

### [핵심]

- Review Agent는 독립 검증 담당 Agent이다.
- Specialist Agent Output을 요구사항 기준으로 검토한다.
- Domain Rules 준수 여부를 확인한다.
- Shared State의 결정사항과 충돌하는지 확인한다.
- Agent Output 간 일관성을 확인한다.
- Risk, Missing Context, Assumption 누락을 확인한다.
- Findings는 Severity 기준으로 분류한다.
- Fix Direction을 반드시 포함한다.
- Pass / Fail을 명확히 표시한다.
- 근거 없는 취향성 지적은 금지한다.
- 수정 방향 없는 비판은 금지한다.

---

### [실무]

2026 실무 기준에서 Review Agent는 Multi-Agent Workflow의 품질 게이트 역할을 한다.

Review Agent 주요 책임:

```text
Requirement Match
→ Domain Rules Compliance
→ Output Structure Check
→ Cross-domain Consistency
→ Risk Detection
→ Severity Classification
→ Fix Direction
→ Pass / Fail Decision
```

Review Agent가 검토해야 하는 대상:

- PM Agent Plan
- Specialist Agent Output
- SQL Agent Schema Decision
- Backend Agent API Contract
- Frontend Agent API Integration
- DevOps Agent Deploy Plan
- AI Agent Workflow Design
- Documentation Agent RAG Document
- Fix Agent Updated Output
- Final Output Draft

Review Agent는 직접 대규모 수정을 수행하지 않는다. 수정은 Fix Agent가 담당하고, Review Agent는 검토 결과와 수정 방향을 제공한다.

---

### [FAQ]

Q. Review Agent는 뭐 하는 Agent야?
A. Agent 산출물을 요구사항, Domain Rules, 일관성, 위험 기준으로 독립 검증하는 Agent다.

Q. Review Agent는 단순 비판 Agent야?
A. 아니다. 문제, 원인, 영향, Severity, 수정 방향을 구조화해 Fix Agent가 사용할 수 있게 만드는 Agent다.

Q. Review Agent가 직접 수정해도 돼?
A. 원칙적으로 직접 수정하지 않는다. 수정은 Fix Agent가 담당하고 Review Agent는 Findings와 Fix Direction을 제공한다.

Q. Review Agent가 중요한 이유는?
A. Multi-Agent 결과의 누락, 충돌, 규칙 위반, 위험 요소를 최종 출력 전에 줄일 수 있기 때문이다.

---

# 2. Review Input

## 2.1 Review Input Definition

### [개념]

Review Input은 Review Agent가 검토를 수행하기 위해 받는 정보이다.

Review Agent는 산출물만 보고 검토하지 않는다. Original User Request, PM Agent Plan, Handoff, Shared State, Domain Rules, Done Criteria를 함께 참조해야 한다.

Review Input 기본 구조:

```text
Original User Request
→ PM Agent Plan
→ Handoff
→ Specialist Agent Output
→ Shared State
→ Domain Rules
→ Done Criteria
→ Review Criteria
```

Review Input이 부족하면 Review Agent는 요구사항 누락, Domain Rules 위반, Agent 간 충돌을 정확히 판단하기 어렵다.

---

### [핵심]

- Review Agent는 산출물만 보고 검토하지 않는다.
- Original User Request를 확인해야 한다.
- PM Agent Plan을 확인해야 한다.
- Handoff의 Requirements와 Constraints를 확인해야 한다.
- Shared State의 Decisions를 확인해야 한다.
- 관련 Domain Rules를 확인해야 한다.
- Done Criteria를 확인해야 한다.
- Review Criteria를 기준으로 Findings를 작성해야 한다.
- Context가 부족하면 단정하지 않고 Missing Context로 표시해야 한다.

---

### [실무]

Review Input Template:

```json
{
  "reviewTarget": "Backend Agent Output",
  "originalUserRequest": "축제 리뷰 API 설계",
  "pmPlan": {
    "requiredAgents": ["SQL Agent", "Backend Agent", "Review Agent"],
    "workflowType": "Sequential"
  },
  "handoff": {
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
    "doneCriteria": [
      "API Contract defined",
      "DTO design included",
      "Exception cases included",
      "Security rules included"
    ]
  },
  "sharedState": {
    "decisions": ["Rating range is 0 to 5", "Review list uses Slice"],
    "openQuestions": [
      "Can one user write multiple reviews for the same festival?"
    ]
  },
  "domainRules": [
    "Master Rules",
    "Multi-Agent System Domain Rules",
    "API Design Domain Rules",
    "Security Advanced Domain Rules"
  ]
}
```

Review Input 부족 예시:

```text
Review Target만 있음
→ 원래 요구사항 없음
→ Handoff 없음
→ Done Criteria 없음
→ Domain Rules 없음
→ 정확한 Review 불가
```

---

### [FAQ]

Q. Review Input이 뭐야?
A. Review Agent가 검토를 수행하기 위해 받는 Original User Request, Handoff, Agent Output, Shared State, Domain Rules, Done Criteria 등의 정보다.

Q. Review Agent는 산출물만 보고 검토해도 돼?
A. 아니다. 요구사항, 제약, 결정사항, Domain Rules를 함께 봐야 정확히 검토할 수 있다.

Q. Review Input이 부족하면 어떻게 해?
A. 단정하지 않고 Missing Context로 표시해야 한다.

Q. Review Agent가 가장 먼저 확인할 것은?
A. Original User Request와 Handoff의 Requirements / Constraints / Done Criteria다.

---

## 2.2 Review Context Priority

### [개념]

Review Context Priority는 Review Agent가 여러 Context 중 무엇을 우선 기준으로 삼을지 정하는 우선순위이다.

Multi-Agent System에서는 User Request, Project Rules, Domain Rules, Shared State, Agent Output이 서로 충돌할 수 있다. Review Agent는 우선순위를 기준으로 충돌을 판단해야 한다.

권장 우선순위:

```text
Current User Request
→ Explicit PM Agent Decision
→ Master Rules
→ Domain Rules
→ Shared State
→ Specialist Agent Output
→ Long-term Memory
```

---

### [핵심]

- 현재 사용자 요청이 가장 우선이다.
- 명시된 PM Agent Decision은 Agent 간 기준점이다.
- Master Rules는 문서 구조와 공통 품질 기준이다.
- Domain Rules는 도메인별 검토 기준이다.
- Shared State는 현재 Workflow의 결정사항을 제공한다.
- Specialist Agent Output은 검토 대상이다.
- Long-term Memory는 보조 정보이며 현재 요청과 충돌하면 후순위다.
- 충돌이 발생하면 Review Findings에 명시한다.

---

### [실무]

Context 충돌 예시:

```text
Current User Request:
- "RAG 문서 제작/검수 전용"
- "중간 응답 금지"
- "작업 완료 후 결과만 출력"

Specialist Agent Output:
- 중간 진행 설명 포함
- 사용자용 긴 설명 포함

Review Finding:
- Domain Rules와 Current User Request 위반
- Final Output에서 중간 설명 제거 필요
```

충돌 해결 기준:

```md
## Context Conflict Resolution

### Conflict

Specialist Output이 Domain Rules와 충돌함

### Priority

Domain Rules > Specialist Output

### Decision

Domain Rules 기준으로 수정 필요

### Fix Direction

Fix Agent가 Specialist Output에서 위반된 구조를 제거하고 Required Section을 복구
```

---

### [FAQ]

Q. Review Context Priority가 뭐야?
A. Review Agent가 여러 Context 중 무엇을 우선 기준으로 삼을지 정하는 순서다.

Q. 현재 사용자 요청과 과거 Memory가 충돌하면 뭐가 우선이야?
A. 현재 사용자 요청이 우선이다.

Q. Domain Rules와 Specialist Output이 충돌하면?
A. Domain Rules를 우선하고 Specialist Output을 수정 대상으로 표시한다.

Q. 충돌을 발견하면 어떻게 기록해?
A. Conflict, Priority, Decision, Fix Direction으로 구조화해 기록한다.

---

# 3. Review Criteria

## 3.1 Requirement Match Review

### [개념]

Requirement Match Review는 Agent Output이 Original User Request와 PM Agent Handoff의 요구사항을 충족하는지 확인하는 검토이다.

Requirement Match는 Review Agent의 가장 기본적인 검토 기준이다.

검토 구조:

```text
Original Requirement
→ Handoff Requirement
→ Agent Output
→ Coverage Check
→ Missing Requirement Finding
```

Requirement Match가 실패하면 산출물이 아무리 잘 작성되어도 목적을 충족하지 못한다.

---

### [핵심]

- Agent Output이 원래 요구사항을 충족하는지 확인한다.
- Handoff Requirements가 Output에 반영되었는지 확인한다.
- Constraints가 지켜졌는지 확인한다.
- Done Criteria가 충족되었는지 확인한다.
- 누락 요구사항은 Finding으로 기록한다.
- 요구사항과 무관한 과도한 작업도 표시한다.
- 불확실한 요구사항은 Open Question으로 표시한다.

---

### [실무]

Requirement Match Checklist:

```md
## Requirement Match Checklist

- [ ] Original User Request가 반영되었는가?
- [ ] Functional Requirements가 반영되었는가?
- [ ] Non-functional Requirements가 반영되었는가?
- [ ] Constraints가 지켜졌는가?
- [ ] Done Criteria가 충족되었는가?
- [ ] Output이 요청 범위를 벗어나지 않았는가?
- [ ] 누락 요구사항이 명시되었는가?
- [ ] 불확실한 요구사항이 Open Question으로 표시되었는가?
```

Review Finding 예시:

```md
## Review Finding

### Severity

Major

### Category

Requirement Match

### Issue

Handoff에는 리뷰 삭제 기능이 요구되었지만 Backend Agent Output에 DELETE API가 없음

### Evidence

Requirements: "Review author can delete own review"
Backend Output: POST /reviews, GET /reviews만 포함

### Impact

사용자 요구사항 중 삭제 기능이 누락되어 API 설계가 불완전함

### Fix Direction

Backend Agent Output에 DELETE /reviews/{reviewId} API Contract, 권한 조건, 예외 케이스를 추가
```

---

### [FAQ]

Q. Requirement Match Review가 뭐야?
A. Agent Output이 원래 사용자 요청과 Handoff 요구사항을 충족하는지 확인하는 검토다.

Q. 요구사항이 누락되면 어떤 Severity야?
A. 핵심 기능 누락이면 Critical 또는 Major로 분류한다.

Q. Constraints 위반도 Requirement Match에 포함돼?
A. 포함된다. 제약사항을 지키지 않으면 요구사항 충족 실패로 볼 수 있다.

Q. 요구사항이 불명확하면 어떻게 해?
A. 단정하지 않고 Open Question 또는 Assumption Risk로 표시한다.

---

## 3.2 Domain Rules Compliance Review

### [개념]

Domain Rules Compliance Review는 Agent Output이 해당 Domain Rules를 지키는지 확인하는 검토이다.

Domain Rules는 Agent가 산출물을 만들 때 따라야 하는 도메인별 기준이다.

검토 구조:

```text
Agent Output
→ Domain Rules
→ Rule Match Check
→ Violation Finding
→ Fix Direction
```

RAG 문서 제작에서는 MASTER_RAG_RULES와 Target DOMAIN_RULES 준수 여부가 핵심 검토 기준이다.

---

### [핵심]

- Agent Output이 Domain Rules를 지키는지 확인한다.
- Master Rules 위반 여부를 확인한다.
- Target Domain Rules 위반 여부를 확인한다.
- Required Section 누락 여부를 확인한다.
- Output Format 위반 여부를 확인한다.
- FAQ와 Retrieval Queries 포함 여부를 확인한다.
- 용어 통일 여부를 확인한다.
- 규칙 위반은 Evidence와 함께 기록한다.

---

### [실무]

RAG 문서 Review 기준:

```md
## RAG Document Domain Rules Review

- [ ] MASTER_RAG_RULES 적용
- [ ] Target DOMAIN_RULES 적용
- [ ] PROJECT_PROGRESS 참고
- [ ] Required Section 포함
- [ ] [개념] 포함
- [ ] [핵심] 포함
- [ ] [실무] 포함
- [ ] [FAQ] 포함
- [ ] Retrieval Queries 포함
- [ ] 사람용 장문 문서가 아닌 Retrieval 최적화 문서인가?
- [ ] 용어가 통일되었는가?
- [ ] FAQ가 충분한가?
- [ ] 오타와 중복이 최소화되었는가?
```

Review Finding 예시:

```md
## Review Finding

### Severity

Critical

### Category

Domain Rules Compliance

### Issue

Retrieval Queries Block이 누락됨

### Evidence

MASTER_RAG_RULES는 모든 문서 마지막에 Retrieval Queries Block을 필수로 요구함

### Impact

RAG 검색 최적화와 User Query Matching 성능이 떨어짐

### Fix Direction

문서 마지막에 `# Retrieval Queries`와 `[FAQ]` 형식의 Q/A Block을 추가
```

---

### [FAQ]

Q. Domain Rules Compliance Review가 뭐야?
A. Agent Output이 Master Rules와 Target Domain Rules를 지키는지 확인하는 검토다.

Q. RAG 문서 검토에서 가장 중요한 규칙은?
A. Required Section, FAQ, Retrieval Queries, 용어 통일, Retrieval 최적화 구조다.

Q. Retrieval Queries가 없으면 문제야?
A. 문제다. RAG 문서에서는 Retrieval Queries가 검색 매칭을 강화하는 필수 요소다.

Q. 규칙 위반은 어떻게 기록해?
A. Severity, Category, Issue, Evidence, Impact, Fix Direction으로 기록한다.

---

## 3.3 Consistency Review

### [개념]

Consistency Review는 Agent Output 내부 또는 여러 Agent Output 간의 일관성을 확인하는 검토이다.

Multi-Agent System에서는 SQL Agent, Backend Agent, Frontend Agent가 서로 다른 가정을 만들 수 있기 때문에 Consistency Review가 중요하다.

검토 구조:

```text
SQL Agent Output
→ Backend Agent Output
→ Frontend Agent Output
→ Shared State Decisions
→ Consistency Check
→ Conflict Finding
```

---

### [핵심]

- Agent Output 내부 일관성을 확인한다.
- Agent Output 간 일관성을 확인한다.
- Shared State의 Decisions와 충돌하는지 확인한다.
- API Contract 일관성을 확인한다.
- DB Schema와 DTO Field 일관성을 확인한다.
- Backend Response와 Frontend State 일관성을 확인한다.
- Security Rule이 Backend와 Frontend 흐름에 반영되었는지 확인한다.
- 충돌은 Fix Direction과 함께 기록한다.

---

### [실무]

Consistency Review 대상:

| 대상                        | 확인 내용                                   |
| --------------------------- | ------------------------------------------- |
| SQL ↔ Backend               | Table / Entity / DTO Field 일치             |
| Backend ↔ Frontend          | API Path / Method / Request / Response 일치 |
| Backend ↔ Security          | 인증 / 인가 조건 반영                       |
| PM ↔ Specialist             | 요구사항과 Output 일치                      |
| Shared State ↔ Agent Output | 결정사항 위반 여부                          |
| Review ↔ Fix                | Review Findings 반영 여부                   |
| RAG Document ↔ Domain Rules | 문서 구조와 규칙 일치                       |

Consistency Finding 예시:

```md
## Review Finding

### Severity

Major

### Category

Consistency

### Issue

SQL Agent Output에는 rating 컬럼이 있으나 Backend Agent DTO에 rating 필드가 없음

### Evidence

SQL Output: reviews.rating
Backend Output: ReviewCreateReqDto에 content만 포함

### Impact

리뷰 평점 저장 요구사항이 API 입력에서 누락됨

### Fix Direction

ReviewCreateReqDto와 Validation Rule에 rating 필드를 추가하고 0~5 범위 검증을 포함
```

---

### [FAQ]

Q. Consistency Review가 뭐야?
A. Agent Output 내부와 여러 Agent Output 간의 일관성을 확인하는 검토다.

Q. Multi-Agent에서 일관성 검토가 중요한 이유는?
A. Agent별로 다른 가정을 만들면 API, DB, UI가 서로 맞지 않을 수 있기 때문이다.

Q. API Contract 일관성은 누가 검토해?
A. Review Agent가 Backend Agent Output과 Frontend Agent Output을 비교해 검토한다.

Q. Shared State와 Agent Output이 충돌하면?
A. Shared State Decisions를 기준으로 충돌 Finding을 작성하고 수정 방향을 제시한다.

---

## 3.4 Risk Review

### [개념]

Risk Review는 Agent Output에 포함된 보안, 데이터, 운영, 유지보수, 오류 가능성을 검토하는 과정이다.

Risk Review는 당장 실행되지 않는 설계 단계에서도 필요하다.

위험 유형:

```text
Security Risk
Data Consistency Risk
Operational Risk
Tool Permission Risk
Missing Context Risk
Regression Risk
Cost / Latency Risk
```

---

### [핵심]

- 보안 위험을 확인한다.
- 데이터 일관성 위험을 확인한다.
- 운영 위험을 확인한다.
- Tool Permission 위험을 확인한다.
- Missing Context로 인한 추측 위험을 확인한다.
- 수정으로 인한 Regression Risk를 확인한다.
- Agent 수 증가에 따른 Latency / Cost 위험을 확인한다.
- 위험은 Severity와 함께 기록한다.

---

### [실무]

Risk Review Checklist:

```md
## Risk Review Checklist

- [ ] 인증 / 인가 누락이 있는가?
- [ ] 민감정보 노출 위험이 있는가?
- [ ] DB 변경 위험이 있는가?
- [ ] 데이터 정합성 문제가 있는가?
- [ ] 운영 서버 변경 위험이 있는가?
- [ ] 삭제 / 배포 / 결제 / 이메일 발송 등 위험 Tool이 포함되는가?
- [ ] Missing Context를 확정처럼 작성했는가?
- [ ] 기존 기능 영향 범위가 표시되었는가?
- [ ] Agent 결과가 Latency / Cost를 과도하게 증가시키는가?
```

Risk Finding 예시:

```md
## Review Finding

### Severity

Critical

### Category

Security Risk

### Issue

리뷰 수정 API에 작성자 본인 확인 조건이 누락됨

### Evidence

PATCH /reviews/{reviewId}는 정의되어 있으나 author check 조건이 없음

### Impact

다른 사용자의 리뷰를 수정할 수 있는 권한 상승 문제가 발생할 수 있음

### Fix Direction

Service Layer에서 authenticatedUserId와 review.userId를 비교하고 불일치 시 AccessDenied 예외 처리
```

---

### [FAQ]

Q. Risk Review가 뭐야?
A. Agent Output에 포함된 보안, 데이터, 운영, Tool 권한, Missing Context 위험을 검토하는 과정이다.

Q. 가장 중요한 Risk는 뭐야?
A. 인증 / 인가 누락, 데이터 손상, 운영 서버 변경, 위험 Tool 실행이다.

Q. Missing Context도 Risk야?
A. 맞다. 필요한 정보가 없는데 추측으로 작성하면 오류가 전파될 수 있다.

Q. Risk Finding에는 뭐가 있어야 해?
A. Severity, Category, Issue, Evidence, Impact, Fix Direction이 있어야 한다.

---

# 4. Severity Classification

## 4.1 Severity Definition

### [개념]

Severity는 Review Agent가 발견한 문제의 심각도를 분류하는 기준이다.

Severity는 Fix Agent가 어떤 문제를 먼저 수정해야 하는지 판단하는 기준이 된다.

기본 Severity:

```text
Critical
→ 반드시 수정

Major
→ 수정 권장 또는 일반적으로 수정 필요

Minor
→ 보고 후 종료 가능

Info
→ 참고 정보
```

Severity가 없으면 Review-Fix Loop의 우선순위가 불명확해지고 무한 반복 가능성이 증가한다.

---

### [핵심]

- Severity는 수정 우선순위를 결정한다.
- Critical은 반드시 수정해야 한다.
- Major는 기능 품질이나 일관성에 영향을 준다.
- Minor는 작은 개선 사항이다.
- Info는 참고 정보다.
- Severity 기준은 Review 전에 정해야 한다.
- 반복마다 Severity 기준이 바뀌면 안 된다.
- Pass Criteria와 연결해야 한다.

---

### [실무]

Severity 기준표:

| Severity | 기준                                                  | 처리              |
| -------- | ----------------------------------------------------- | ----------------- |
| Critical | 요구사항 실패, 보안 위험, 실행 불가, 데이터 손상 가능 | 반드시 수정       |
| Major    | 주요 기능 누락, API Contract 불일치, 중요한 제약 위반 | 수정 권장         |
| Minor    | 네이밍, 표현, 작은 구조 개선                          | 보고 후 종료 가능 |
| Info     | 참고 의견, 향후 개선                                  | 수정 필수 아님    |

예시:

```md
## Severity Examples

### Critical

- 인증이 필요한 API에 인증 조건 없음
- 데이터 삭제 위험 작업을 승인 없이 실행
- Retrieval Queries 전체 누락
- 요구한 파일 형식 완전 위반

### Major

- API Response Field 불일치
- 주요 Exception Case 누락
- Handoff의 요구사항 일부 누락
- Domain Rules 일부 위반

### Minor

- 변수명 일관성 개선
- FAQ 표현 보강
- 중복 문장 일부 존재

### Info

- 향후 확장 시 고려사항
- 성능 최적화 후보
```

---

### [FAQ]

Q. Severity가 뭐야?
A. Review Agent가 발견한 문제의 심각도를 분류하는 기준이다.

Q. Critical은 어떤 문제야?
A. 요구사항 실패, 보안 위험, 실행 불가, 데이터 손상 가능성처럼 반드시 수정해야 하는 문제다.

Q. Minor Issue도 반드시 수정해야 해?
A. 아니다. Minor Issue는 보고 후 종료할 수 있다.

Q. Severity가 필요한 이유는?
A. Fix Agent가 수정 우선순위를 정하고 Review-Fix Loop를 종료하기 위해 필요하다.

---

## 4.2 Pass / Fail Criteria

### [개념]

Pass / Fail Criteria는 Review Agent가 산출물을 통과시킬지 수정이 필요한지 판단하는 기준이다.

Pass / Fail Criteria는 Severity와 연결된다.

기본 기준:

```text
Critical 0개
→ Pass 가능

Critical 1개 이상
→ Fail

Major 다수
→ Conditional Pass 또는 Fail

Minor만 존재
→ Pass with Notes 가능
```

---

### [핵심]

- Pass / Fail 기준은 명확해야 한다.
- Critical Issue가 있으면 Fail이다.
- Major Issue가 많으면 Fail 또는 Conditional Pass다.
- Minor Issue만 있으면 Pass 가능하다.
- Pass with Notes를 사용할 수 있다.
- Fail이면 Fix Direction이 반드시 필요하다.
- Review 결과는 Fix Agent가 바로 사용할 수 있어야 한다.

---

### [실무]

Pass / Fail Decision 예시:

```md
## Review Decision

### Status

Fail

### Reason

Critical Issue 1개 발견

### Critical

- 리뷰 수정 API에 작성자 본인 확인 조건 없음

### Required Fix

- authenticatedUserId와 review.userId 비교 로직 추가

### Re-review Required

Yes
```

Conditional Pass 예시:

```md
## Review Decision

### Status

Conditional Pass

### Reason

Critical Issue 없음, Major Issue 1개 존재

### Major

- 중복 리뷰 허용 정책이 불명확함

### Required Action

- PM Agent가 정책 결정 후 Shared State에 기록

### Re-review Required

Optional
```

Pass with Notes 예시:

```md
## Review Decision

### Status

Pass with Notes

### Reason

Critical / Major Issue 없음

### Notes

- FAQ 표현 일부 보강 가능
- 네이밍 일관성 추가 검토 가능

### Re-review Required

No
```

---

### [FAQ]

Q. Pass / Fail Criteria가 뭐야?
A. Review Agent가 산출물을 통과시킬지 수정이 필요한지 판단하는 기준이다.

Q. Critical Issue가 있으면 Pass 가능해?
A. 아니다. Critical Issue가 있으면 Fail이다.

Q. Minor Issue만 있으면 어떻게 해?
A. Pass with Notes로 처리할 수 있다.

Q. Fail이면 반드시 필요한 것은?
A. Fix Direction과 Re-review 필요 여부가 반드시 있어야 한다.

---

# 5. Review Output

## 5.1 Review Finding Structure

### [개념]

Review Finding은 Review Agent가 발견한 문제를 구조화한 검토 결과이다.

Review Finding은 단순 지적이 아니라 Fix Agent가 바로 수정할 수 있는 작업 단위여야 한다.

기본 구조:

```text
Severity
→ Category
→ Issue
→ Evidence
→ Impact
→ Root Cause
→ Fix Direction
```

---

### [핵심]

- Review Finding은 구조화되어야 한다.
- Severity를 포함해야 한다.
- Category를 포함해야 한다.
- Issue를 명확히 작성해야 한다.
- Evidence를 포함해야 한다.
- Impact를 설명해야 한다.
- Root Cause를 가능하면 포함한다.
- Fix Direction을 반드시 포함한다.
- 근거 없는 지적은 금지한다.
- 수정 방향 없는 Finding은 피한다.

---

### [실무]

Review Finding Template:

```md
## Review Finding

### Severity

<Critical | Major | Minor | Info>

### Category

<Requirement Match | Domain Rules Compliance | Consistency | Risk | Output Structure>

### Issue

<문제 설명>

### Evidence

<문제 근거>

### Impact

<영향>

### Root Cause

<원인>

### Fix Direction

<수정 방향>

### Re-review Required

<Yes | No>
```

Finding 예시:

```md
## Review Finding

### Severity

Major

### Category

Output Structure

### Issue

Specialist Agent Output에 Assumptions와 Risks가 없음

### Evidence

Output에는 API Contract만 있고 Assumptions / Risks Section이 존재하지 않음

### Impact

불확실한 정보가 확정처럼 전달되어 PM Agent 통합과 Fix Agent 수정 과정에서 오류가 발생할 수 있음

### Root Cause

Specialist Agent Output Template 미적용

### Fix Direction

Output에 Assumptions, Risks, Open Questions Section을 추가

### Re-review Required

Yes
```

---

### [FAQ]

Q. Review Finding이 뭐야?
A. Review Agent가 발견한 문제를 Severity, Evidence, Impact, Fix Direction으로 구조화한 검토 결과다.

Q. Review Finding에 Evidence가 필요한 이유는?
A. 근거 없는 취향성 지적을 막고 Fix Agent가 정확히 수정할 수 있게 하기 위해서다.

Q. Review Finding에 Fix Direction이 반드시 필요해?
A. 필요하다. 수정 방향 없는 비판은 Fix Agent가 활용하기 어렵다.

Q. Review Finding은 누가 사용해?
A. Fix Agent, PM Agent, Specialist Agent가 사용한다.

---

## 5.2 Review Report Structure

### [개념]

Review Report는 여러 Review Finding을 하나의 검토 결과로 정리한 문서이다.

Review Report는 PM Agent가 Workflow를 계속 진행할지, Fix Agent에게 전달할지, 사용자에게 확인할지 판단하는 근거가 된다.

기본 구조:

```text
Review Summary
→ Review Target
→ Findings by Severity
→ Pass / Fail
→ Required Fixes
→ Open Questions
→ Re-review Need
```

---

### [핵심]

- Review Report는 전체 검토 결과이다.
- Review Target을 명확히 표시한다.
- Findings를 Severity별로 정리한다.
- Pass / Fail을 표시한다.
- Required Fixes를 분리한다.
- Open Questions를 표시한다.
- Re-review 필요 여부를 표시한다.
- PM Agent가 바로 판단할 수 있어야 한다.

---

### [실무]

Review Report Template:

```md
# Review Report

## Review Target

Backend Agent Output - Festival Review API

## Review Summary

요구사항 대부분 반영됨. 단, 작성자 권한 검증과 중복 리뷰 정책이 불명확함.

## Findings

### Critical

- 리뷰 수정 / 삭제 API에 작성자 본인 확인 조건 누락

### Major

- 중복 리뷰 허용 정책 불명확
- ReviewCreateReqDto Validation 기준 부족

### Minor

- API 설명에 Response 예시 보강 가능

## Required Fixes

- 작성자 본인 확인 조건 추가
- 중복 리뷰 정책을 PM Agent Decision으로 확정
- Rating Validation 기준 추가

## Open Questions

- 한 사용자가 같은 축제에 여러 리뷰를 작성할 수 있는가?
- 삭제 정책은 Soft Delete인가 Hard Delete인가?

## Review Decision

Fail

## Re-review Required

Yes
```

RAG 문서 Review Report 예시:

```md
# Review Report

## Review Target

Multi_Agent_System_Part05_Review_Agent.md

## Review Summary

Required Section과 Retrieval Queries가 포함되어 있음. FAQ 구조도 적합함.

## Findings

### Critical

- 없음

### Major

- 없음

### Minor

- 일부 FAQ 표현 중복 가능

## Review Decision

Pass with Notes

## Re-review Required

No
```

---

### [FAQ]

Q. Review Report가 뭐야?
A. 여러 Review Finding을 모아 전체 검토 결과와 Pass / Fail 판단을 정리한 문서다.

Q. Review Report에는 뭐가 있어야 해?
A. Review Target, Summary, Findings, Required Fixes, Open Questions, Review Decision, Re-review Required가 있어야 한다.

Q. Review Report는 누가 사용해?
A. PM Agent가 Workflow 진행 여부를 판단하고 Fix Agent가 수정 작업을 수행할 때 사용한다.

Q. Review Report와 Review Finding 차이는?
A. Review Finding은 개별 문제이고, Review Report는 전체 검토 결과다.

---

# 6. Review-Fix Loop

## 6.1 Review-Fix Loop Definition

### [개념]

Review-Fix Loop는 Review Agent가 산출물을 검토하고, Fix Agent가 Review Findings를 반영한 뒤, 필요하면 다시 Review Agent가 검토하는 반복 구조이다.

Review-Fix Loop는 품질을 높이는 데 유용하지만 종료 조건이 없으면 무한 반복될 수 있다.

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

- Review-Fix Loop는 품질 개선 구조이다.
- Review Agent는 Findings를 작성한다.
- Fix Agent는 Findings를 반영한다.
- 수정 후 Re-review가 가능하다.
- Max Iteration이 필요하다.
- Stop Condition이 필요하다.
- Severity 기준이 필요하다.
- Minor Issue는 보고 후 종료할 수 있다.
- Review 기준은 반복 중 바뀌면 안 된다.

---

### [실무]

권장 Review-Fix 정책:

```text
Max Iteration: 2
Critical: 반드시 수정
Major: 수정 권장
Minor: 보고 후 종료 가능
Info: 참고만
```

Review-Fix Loop 예시:

```text
1차 Review:
- Critical 1개
- Major 2개
→ Fail

Fix Agent:
- Critical 수정
- Major 1개 수정
- Major 1개는 PM Decision 필요로 표시

2차 Review:
- Critical 0개
- Major 1개 Open Question
→ Conditional Pass
```

Stop Condition 예시:

```md
## Stop Condition

- Critical Issue가 0개
- 남은 Major Issue가 PM Decision 또는 Open Question으로 분리됨
- Minor Issue만 남음
- Max Iteration에 도달함
- 사용자 확인이 필요한 상태로 전환됨
```

---

### [FAQ]

Q. Review-Fix Loop가 뭐야?
A. Review Agent가 검토하고 Fix Agent가 수정한 뒤 필요하면 다시 검토하는 품질 개선 반복 구조다.

Q. Review-Fix Loop가 필요한 이유는?
A. 생성 결과의 누락, 오류, 규칙 위반을 수정해 최종 품질을 높이기 위해서다.

Q. Review-Fix Loop가 위험한 이유는?
A. 종료 조건이 없으면 무한 반복될 수 있기 때문이다.

Q. Review-Fix Loop에는 무엇이 필요해?
A. Max Iteration, Stop Condition, Severity 기준, Pass Criteria가 필요하다.

---

## 6.2 Infinite Loop Prevention

### [개념]

Infinite Loop Prevention은 Review-Fix Loop가 끝없이 반복되지 않도록 종료 기준을 설정하는 것이다.

Review Agent와 Fix Agent가 매번 새로운 기준을 추가하거나 Minor Issue까지 계속 수정하면 Workflow가 종료되지 않는다.

무한 반복 원인:

```text
No Max Iteration
No Stop Condition
Changing Review Criteria
Over-fixing Minor Issues
Unclear Pass Criteria
New Requirements During Fix
```

---

### [핵심]

- Max Iteration을 설정한다.
- Stop Condition을 설정한다.
- Severity 기준을 고정한다.
- Review Criteria를 반복 중 변경하지 않는다.
- Minor Issue는 보고 후 종료할 수 있다.
- Fix Agent는 새 요구사항을 만들지 않는다.
- PM Agent는 반복 종료 여부를 판단할 수 있어야 한다.
- 사용자 확인이 필요한 항목은 Open Question으로 분리한다.

---

### [실무]

Infinite Loop 방지 규칙:

```md
## Review-Fix Loop Rules

- Max Iteration은 기본 2회
- Critical Issue는 반드시 수정
- Major Issue는 수정하거나 PM Decision으로 분리
- Minor Issue는 Pass with Notes 가능
- 반복 중 Review Criteria 변경 금지
- Fix Agent는 Review Finding 범위 밖 대규모 수정 금지
- 새로운 요구사항 발견 시 PM Agent에게 반환
- 사용자 확인 필요 항목은 Open Question으로 전환
```

무한 반복 방지 예시:

```text
Review 1:
- Minor: FAQ 표현 개선 가능

Fix 1:
- FAQ 표현 일부 수정

Review 2:
- Minor: 더 자연스러운 표현 가능

잘못된 처리:
→ 계속 수정 반복

올바른 처리:
→ Pass with Notes
→ Minor Issue는 향후 개선으로 기록
```

---

### [FAQ]

Q. Review-Fix Loop가 무한 반복되는 이유는?
A. Max Iteration, Stop Condition, Severity 기준이 없거나 Review 기준이 계속 바뀌기 때문이다.

Q. 무한 반복을 막으려면?
A. Max Iteration, Stop Condition, Pass Criteria, Severity 기준을 설정해야 한다.

Q. Minor Issue는 계속 고쳐야 해?
A. 아니다. Minor Issue만 남으면 Pass with Notes로 종료할 수 있다.

Q. Fix Agent가 새로운 요구사항을 추가해도 돼?
A. 안 된다. 새로운 요구사항은 PM Agent에게 반환해야 한다.

---

# 7. Review Agent Failure Handling

## 7.1 Review Agent Failure Cases

### [개념]

Review Agent Failure는 Review Agent가 잘못된 기준으로 검토하거나, 근거 없는 지적을 하거나, 수정 방향 없는 비판을 하거나, Context 부족 상태에서 단정할 때 발생한다.

주요 실패 유형:

```text
No Review Criteria
No Evidence
No Fix Direction
Over-critical Review
Taste-based Criticism
Missing Context Assumption
Changing Criteria
No Pass / Fail
```

---

### [핵심]

- Review Criteria 없이 검토하면 안 된다.
- Evidence 없는 지적은 피해야 한다.
- Fix Direction 없는 Finding은 피해야 한다.
- 취향성 비판을 결함처럼 표현하면 안 된다.
- Context 부족 상태에서 단정하면 안 된다.
- 반복마다 기준을 바꾸면 안 된다.
- Pass / Fail을 명확히 표시해야 한다.
- Review Agent는 산출물 전체를 다시 구현하지 않는다.

---

### [실무]

Review Agent Failure 예시:

```md
## Bad Review Finding

이 코드는 별로임. 더 깔끔하게 고쳐야 함.
```

문제:

- Severity 없음
- Category 없음
- Evidence 없음
- Impact 없음
- Fix Direction 없음
- 취향성 비판

Good Review Finding:

```md
## Review Finding

### Severity

Major

### Category

Exception Handling

### Issue

Review update API에서 Review Not Found 예외 케이스가 누락됨

### Evidence

PATCH /reviews/{reviewId} API Contract에는 성공 응답만 있고 실패 응답이 없음

### Impact

존재하지 않는 reviewId 요청 시 API Error Response 기준이 불명확함

### Fix Direction

Review Not Found 예외 케이스와 Error Response Format을 추가
```

Context 부족 시 처리:

```md
## Review Finding

### Severity

Info

### Category

Missing Context

### Issue

기존 ApiResponse 규칙이 제공되지 않아 응답 형식 정확성은 단정 불가

### Fix Direction

PM Agent가 기존 ApiResponse 문서 또는 예시를 제공하면 재검토 가능
```

---

### [FAQ]

Q. Review Agent Failure는 언제 발생해?
A. 기준 없이 검토하거나, 근거 없이 지적하거나, 수정 방향 없이 비판하거나, Context 부족 상태에서 단정할 때 발생한다.

Q. 취향성 비판도 Review Finding이 될 수 있어?
A. 아니다. 명확한 기준과 Evidence가 없는 취향성 비판은 Finding으로 작성하면 안 된다.

Q. Context가 부족하면 Review Agent는 어떻게 해야 해?
A. 단정하지 않고 Missing Context 또는 Info로 표시해야 한다.

Q. Review Agent Output에 반드시 있어야 하는 것은?
A. Severity, Category, Issue, Evidence, Impact, Fix Direction, Pass / Fail이다.

---

## 7.2 Review Agent Checklist

### [개념]

Review Agent Checklist는 Review Agent가 검토 전후에 기준, 근거, 결과 구조를 확인하는 체크리스트이다.

Checklist를 사용하면 근거 없는 지적, Domain Rules 누락, Pass / Fail 누락을 줄일 수 있다.

---

### [핵심]

- Review 전 Input을 확인한다.
- Review Criteria를 확인한다.
- Domain Rules를 확인한다.
- Shared State Decisions를 확인한다.
- Evidence를 포함한다.
- Severity를 분류한다.
- Fix Direction을 작성한다.
- Pass / Fail을 명시한다.
- Re-review 필요 여부를 표시한다.
- Missing Context는 단정하지 않는다.

---

### [실무]

Review Agent Pre-Review Checklist:

```md
## Review Agent Pre-Review Checklist

- [ ] Original User Request를 확인했는가?
- [ ] PM Agent Plan을 확인했는가?
- [ ] Handoff Requirements를 확인했는가?
- [ ] Handoff Constraints를 확인했는가?
- [ ] Done Criteria를 확인했는가?
- [ ] Shared State Decisions를 확인했는가?
- [ ] Target Domain Rules를 확인했는가?
- [ ] Review Criteria를 확인했는가?
- [ ] Review Target이 명확한가?
```

Review Agent Final Checklist:

```md
## Review Agent Final Checklist

- [ ] Requirement Match를 검토했는가?
- [ ] Domain Rules Compliance를 검토했는가?
- [ ] Consistency를 검토했는가?
- [ ] Risk를 검토했는가?
- [ ] 각 Finding에 Severity가 있는가?
- [ ] 각 Finding에 Evidence가 있는가?
- [ ] 각 Finding에 Impact가 있는가?
- [ ] 각 Finding에 Fix Direction이 있는가?
- [ ] Pass / Fail을 명시했는가?
- [ ] Re-review 필요 여부를 표시했는가?
- [ ] Missing Context를 단정하지 않았는가?
- [ ] 취향성 비판을 결함처럼 쓰지 않았는가?
```

---

### [FAQ]

Q. Review Agent Checklist가 뭐야?
A. Review Agent가 검토 전후에 기준, 근거, 결과 구조를 확인하는 체크리스트다.

Q. Review 전에 확인해야 할 것은?
A. Original User Request, PM Plan, Handoff, Done Criteria, Shared State, Domain Rules, Review Target이다.

Q. Review 후 확인해야 할 것은?
A. Requirement Match, Domain Rules Compliance, Consistency, Risk, Severity, Evidence, Fix Direction, Pass / Fail이다.

Q. Checklist가 필요한 이유는?
A. 근거 없는 지적, 누락된 Review 기준, 불명확한 Pass / Fail을 줄이기 위해서다.

---

# 8. RAG Document Review Agent

## 8.1 RAG Document Review

### [개념]

RAG Document Review는 Documentation Agent가 작성한 RAG 문서가 Retrieval 최적화 기준을 충족하는지 검토하는 작업이다.

RAG 문서 검토에서는 사람용 가독성보다 Retrieval Hit, Chunk Quality, Semantic Similarity, FAQ 품질, Retrieval Queries 품질을 우선한다.

RAG Document Review 구조:

```text
RAG Document Draft
→ Master Rules Check
→ Domain Rules Check
→ Required Section Check
→ FAQ Check
→ Retrieval Queries Check
→ Naming Consistency Check
→ Final Pass / Fail
```

---

### [핵심]

- RAG 문서는 사람용 에세이가 아니다.
- Retrieval 최적화가 우선이다.
- MASTER_RAG_RULES를 적용한다.
- Target DOMAIN_RULES를 적용한다.
- PROJECT_PROGRESS를 참고한다.
- Required Section을 확인한다.
- `[개념]`, `[핵심]`, `[실무]`, `[FAQ]` 포함 여부를 확인한다.
- FAQ는 Q + A 형식이어야 한다.
- Retrieval Queries는 문서 마지막에 있어야 한다.
- 용어 통일을 확인한다.
- 중복 설명과 오타를 최소화한다.

---

### [실무]

RAG Document Review Checklist:

```md
## RAG Document Review Checklist

- [ ] FileName이 명확한가?
- [ ] Document Title이 명확한가?
- [ ] MASTER_RAG_RULES를 적용했는가?
- [ ] Target DOMAIN_RULES를 적용했는가?
- [ ] PROJECT_PROGRESS와 충돌하지 않는가?
- [ ] Required Section이 포함되었는가?
- [ ] `[개념]`이 포함되었는가?
- [ ] `[핵심]`이 포함되었는가?
- [ ] `[실무]`가 포함되었는가?
- [ ] `[FAQ]`가 포함되었는가?
- [ ] FAQ가 Q + A 형식인가?
- [ ] Retrieval Queries가 마지막에 포함되었는가?
- [ ] Retrieval Queries가 실제 사용자 질문 표현을 포함하는가?
- [ ] 용어가 통일되었는가?
- [ ] Chunk가 독립 검색 가능하게 구성되었는가?
- [ ] 장문 에세이형 설명을 피했는가?
- [ ] 오타와 중복이 최소화되었는가?
```

RAG Document Review Decision 예시:

```md
## Review Decision

### Status

Pass

### Reason

Required Section, FAQ, Retrieval Queries, Domain Rules 구조가 충족됨

### Notes

- 일부 FAQ 표현은 향후 Retrieval 테스트 후 보강 가능

### Re-review Required

No
```

---

### [FAQ]

Q. RAG Document Review가 뭐야?
A. RAG 문서가 Retrieval 최적화 기준, Master Rules, Domain Rules를 충족하는지 검토하는 작업이다.

Q. RAG 문서 검토에서 가장 중요한 기준은?
A. Required Section, FAQ, Retrieval Queries, 용어 통일, Chunk Quality, Retrieval 최적화다.

Q. RAG 문서는 사람용 문서처럼 길게 쓰는 게 좋아?
A. 아니다. AI Agent Retrieval을 위해 짧고 구조화된 Chunk 중심으로 작성하는 것이 좋다.

Q. Retrieval Queries는 왜 검토해야 해?
A. 사용자 질문 매칭과 Semantic Retrieval 성능에 직접 영향을 주기 때문이다.

---

# Retrieval Queries

### [FAQ]

Q. Review Agent는 뭐야?
A. Agent 산출물을 요구사항, Domain Rules, 일관성, 위험 기준으로 독립 검증하는 Agent다.

Q. Review Agent의 핵심 역할은?
A. 문제를 찾고 Severity, Evidence, Impact, Fix Direction을 구조화해 Fix Agent가 사용할 수 있게 만드는 것이다.

Q. Review Agent가 직접 수정해도 돼?
A. 원칙적으로 직접 수정하지 않는다. 수정은 Fix Agent가 담당한다.

Q. Review Agent가 중요한 이유는?
A. Multi-Agent 결과의 누락, 충돌, 규칙 위반, 위험 요소를 최종 출력 전에 줄일 수 있기 때문이다.

Q. Review Input이 뭐야?
A. Review Agent가 검토를 수행하기 위해 받는 Original User Request, Handoff, Agent Output, Shared State, Domain Rules, Done Criteria 등의 정보다.

Q. Review Agent는 산출물만 보고 검토해도 돼?
A. 아니다. 요구사항, 제약, 결정사항, Domain Rules를 함께 봐야 정확히 검토할 수 있다.

Q. Review Context Priority가 뭐야?
A. Review Agent가 여러 Context 중 무엇을 우선 기준으로 삼을지 정하는 순서다.

Q. 현재 사용자 요청과 과거 Memory가 충돌하면 뭐가 우선이야?
A. 현재 사용자 요청이 우선이다.

Q. Requirement Match Review가 뭐야?
A. Agent Output이 원래 사용자 요청과 Handoff 요구사항을 충족하는지 확인하는 검토다.

Q. 요구사항이 누락되면 어떤 Severity야?
A. 핵심 기능 누락이면 Critical 또는 Major로 분류한다.

Q. Domain Rules Compliance Review가 뭐야?
A. Agent Output이 Master Rules와 Target Domain Rules를 지키는지 확인하는 검토다.

Q. RAG 문서 검토에서 가장 중요한 규칙은?
A. Required Section, FAQ, Retrieval Queries, 용어 통일, Retrieval 최적화 구조다.

Q. Consistency Review가 뭐야?
A. Agent Output 내부와 여러 Agent Output 간의 일관성을 확인하는 검토다.

Q. Multi-Agent에서 일관성 검토가 중요한 이유는?
A. Agent별로 다른 가정을 만들면 API, DB, UI가 서로 맞지 않을 수 있기 때문이다.

Q. Risk Review가 뭐야?
A. Agent Output에 포함된 보안, 데이터, 운영, Tool 권한, Missing Context 위험을 검토하는 과정이다.

Q. Missing Context도 Risk야?
A. 맞다. 필요한 정보가 없는데 추측으로 작성하면 오류가 전파될 수 있다.

Q. Severity가 뭐야?
A. Review Agent가 발견한 문제의 심각도를 분류하는 기준이다.

Q. Critical은 어떤 문제야?
A. 요구사항 실패, 보안 위험, 실행 불가, 데이터 손상 가능성처럼 반드시 수정해야 하는 문제다.

Q. Minor Issue도 반드시 수정해야 해?
A. 아니다. Minor Issue는 보고 후 종료할 수 있다.

Q. Pass / Fail Criteria가 뭐야?
A. Review Agent가 산출물을 통과시킬지 수정이 필요한지 판단하는 기준이다.

Q. Critical Issue가 있으면 Pass 가능해?
A. 아니다. Critical Issue가 있으면 Fail이다.

Q. Review Finding이 뭐야?
A. Review Agent가 발견한 문제를 Severity, Evidence, Impact, Fix Direction으로 구조화한 검토 결과다.

Q. Review Finding에 Evidence가 필요한 이유는?
A. 근거 없는 취향성 지적을 막고 Fix Agent가 정확히 수정할 수 있게 하기 위해서다.

Q. Review Finding에 Fix Direction이 반드시 필요해?
A. 필요하다. 수정 방향 없는 비판은 Fix Agent가 활용하기 어렵다.

Q. Review Report가 뭐야?
A. 여러 Review Finding을 모아 전체 검토 결과와 Pass / Fail 판단을 정리한 문서다.

Q. Review Report에는 뭐가 있어야 해?
A. Review Target, Summary, Findings, Required Fixes, Open Questions, Review Decision, Re-review Required가 있어야 한다.

Q. Review-Fix Loop가 뭐야?
A. Review Agent가 검토하고 Fix Agent가 수정한 뒤 필요하면 다시 검토하는 품질 개선 반복 구조다.

Q. Review-Fix Loop가 필요한 이유는?
A. 생성 결과의 누락, 오류, 규칙 위반을 수정해 최종 품질을 높이기 위해서다.

Q. Review-Fix Loop가 무한 반복되는 이유는?
A. Max Iteration, Stop Condition, Severity 기준이 없거나 Review 기준이 계속 바뀌기 때문이다.

Q. Review-Fix Loop 무한 반복을 막으려면?
A. Max Iteration, Stop Condition, Pass Criteria, Severity 기준을 설정해야 한다.

Q. Review Agent Failure는 언제 발생해?
A. 기준 없이 검토하거나, 근거 없이 지적하거나, 수정 방향 없이 비판하거나, Context 부족 상태에서 단정할 때 발생한다.

Q. 취향성 비판도 Review Finding이 될 수 있어?
A. 아니다. 명확한 기준과 Evidence가 없는 취향성 비판은 Finding으로 작성하면 안 된다.

Q. Review Agent Checklist가 뭐야?
A. Review Agent가 검토 전후에 기준, 근거, 결과 구조를 확인하는 체크리스트다.

Q. Review 전에 확인해야 할 것은?
A. Original User Request, PM Plan, Handoff, Done Criteria, Shared State, Domain Rules, Review Target이다.

Q. RAG Document Review가 뭐야?
A. RAG 문서가 Retrieval 최적화 기준, Master Rules, Domain Rules를 충족하는지 검토하는 작업이다.

Q. RAG 문서 검토에서 가장 중요한 기준은?
A. Required Section, FAQ, Retrieval Queries, 용어 통일, Chunk Quality, Retrieval 최적화다.

Q. RAG 문서는 사람용 문서처럼 길게 쓰는 게 좋아?
A. 아니다. AI Agent Retrieval을 위해 짧고 구조화된 Chunk 중심으로 작성하는 것이 좋다.

Q. 개인 AI 개발팀에서 Review Agent는 언제 사용해?
A. Specialist Agent Output 생성 후, Fix Agent 수정 후, Final Output 생성 전에 사용한다.
