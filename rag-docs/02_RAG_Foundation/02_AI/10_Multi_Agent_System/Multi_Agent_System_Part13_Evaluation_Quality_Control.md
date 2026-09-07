# Multi-Agent System Part13 - Evaluation and Quality Control

---

# 1. Evaluation Core

## 1.1 Evaluation Definition

### [개념]

Evaluation은 Multi-Agent System에서 Agent Output, Handoff, Workflow, RAG Retrieval, Review-Fix 결과의 품질을 측정하고 개선하는 과정이다.

Evaluation은 단순히 결과가 맞는지 확인하는 것이 아니라, 요구사항 충족, 역할 준수, Context 사용, Tool Permission 준수, Review 품질, 최종 결과 품질을 함께 검토한다.

Evaluation의 핵심은 Agent 시스템이 반복적으로 안정적인 결과를 내는지 확인하는 것이다.

기본 구조:

```text
User Request
→ Agent Workflow
→ Agent Outputs
→ Review
→ Metrics
→ Quality Decision
→ Improvement
```

개인 AI 개발팀 기준 Evaluation 구조:

```text
PM Agent Plan
→ Handoff Quality
→ Specialist Output Quality
→ Review Quality
→ Fix Quality
→ Final Output Quality
→ Workflow Quality
```

---

### [핵심]

- Evaluation은 Multi-Agent System 품질 측정 과정이다.
- Agent별 Output 품질을 평가한다.
- Handoff 품질을 평가한다.
- RAG Retrieval 품질을 평가한다.
- Review Agent의 Findings 품질을 평가한다.
- Fix Agent의 수정 품질을 평가한다.
- Workflow 전체 안정성을 평가한다.
- Tool Permission 준수 여부를 평가한다.
- Shared State 일관성을 평가한다.
- 평가 결과는 개선 Action으로 연결해야 한다.

---

### [실무]

2026 실무 기준에서 Multi-Agent Evaluation은 다음 기준으로 나눈다.

```text
Output Evaluation
→ 산출물 자체 품질

Process Evaluation
→ Workflow 수행 과정 품질

Retrieval Evaluation
→ RAG 검색 품질

Safety Evaluation
→ Tool Permission / Approval 준수

Review Evaluation
→ Review Finding 품질

Fix Evaluation
→ 수정 반영 품질

System Evaluation
→ 전체 안정성 / 반복성
```

Evaluation 대상:

| 대상             | 평가 기준                                      |
| ---------------- | ---------------------------------------------- |
| PM Agent         | 요구사항 분석, Task 분해, Routing, Handoff     |
| Specialist Agent | Domain Output, Scope 준수, Assumption 표시     |
| Review Agent     | Severity, Evidence, Fix Direction, Pass / Fail |
| Fix Agent        | Finding 반영, 요구사항 보존, Regression Risk   |
| RAG Retrieval    | Relevance, Sufficiency, Context Precision      |
| Shared State     | 최신성, 일관성, 결정사항 기록                  |
| Tool Permission  | 권한 준수, 승인 필요 작업 차단                 |
| Final Output     | 사용자 요청 충족, 명확성, 실사용 가능성        |

---

### [FAQ]

Q. Evaluation이 뭐야?
A. Multi-Agent System에서 Agent Output, Handoff, Workflow, RAG Retrieval, Review-Fix 품질을 측정하고 개선하는 과정이다.

Q. Evaluation이 필요한 이유는?
A. Agent 결과가 우연히 한 번 잘 나온 것이 아니라 반복적으로 안정적인 품질을 내는지 확인하기 위해 필요하다.

Q. Multi-Agent Evaluation은 무엇을 평가해?
A. PM Agent, Specialist Agent, Review Agent, Fix Agent, RAG Retrieval, Shared State, Tool Permission, Final Output을 평가한다.

Q. Evaluation 결과는 어디에 사용해?
A. Agent Role 수정, Handoff Template 개선, RAG Scope 조정, Review Criteria 보강, Workflow Pattern 개선에 사용한다.

---

# 2. Agent Output Evaluation

## 2.1 Agent Output Quality

### [개념]

Agent Output Quality는 각 Agent가 자신의 Role과 Handoff 기준에 맞는 산출물을 만들었는지 평가하는 기준이다.

Agent Output은 단순히 길거나 자세한 것이 좋은 것이 아니라, 요구사항을 충족하고, Scope를 지키며, 다음 Agent가 사용할 수 있도록 구조화되어야 한다.

기본 구조:

```text
Handoff
→ Agent Output
→ Requirement Coverage
→ Scope Compliance
→ Structure Quality
→ Risk / Assumption Check
```

---

### [핵심]

- Agent Output은 Handoff를 기준으로 평가한다.
- Requirements 반영 여부를 확인한다.
- Constraints 준수 여부를 확인한다.
- Agent Scope 밖 작업이 있는지 확인한다.
- Expected Output을 충족했는지 확인한다.
- Done Criteria를 충족했는지 확인한다.
- Assumptions가 표시되었는지 확인한다.
- Risks와 Open Questions가 표시되었는지 확인한다.
- 다음 Agent가 사용할 수 있는 구조인지 확인한다.
- 불확실한 내용을 확정처럼 작성하지 않았는지 확인한다.

---

### [실무]

Agent Output Quality Checklist:

```md
## Agent Output Quality Checklist

- [ ] Handoff Task를 충족했는가?
- [ ] Requirements가 모두 반영되었는가?
- [ ] Constraints가 지켜졌는가?
- [ ] Agent Scope를 벗어나지 않았는가?
- [ ] Expected Output이 포함되었는가?
- [ ] Done Criteria를 충족했는가?
- [ ] Output 구조가 명확한가?
- [ ] Decisions가 표시되었는가?
- [ ] Assumptions가 표시되었는가?
- [ ] Risks가 표시되었는가?
- [ ] Open Questions가 표시되었는가?
- [ ] 다음 Agent가 사용할 수 있는가?
```

Agent Output Score 예시:

```json
{
  "target": "Backend Agent Output",
  "requirementCoverage": 0.9,
  "constraintCompliance": 0.85,
  "scopeCompliance": 1.0,
  "structureQuality": 0.9,
  "riskDisclosure": 0.8,
  "overallQuality": 0.89,
  "decision": "pass_with_notes"
}
```

---

### [FAQ]

Q. Agent Output Quality가 뭐야?
A. Agent가 Handoff, Requirements, Constraints, Scope, Done Criteria에 맞는 산출물을 만들었는지 평가하는 기준이다.

Q. 좋은 Agent Output은 어떤 형태야?
A. 요구사항을 충족하고, 구조화되어 있으며, Decisions, Assumptions, Risks, Open Questions를 포함한다.

Q. Output이 길면 좋은 거야?
A. 아니다. 길이보다 요구사항 충족, 정확성, 구조화, 다음 Agent 사용 가능성이 중요하다.

Q. Agent Output 평가는 누가 해?
A. Review Agent가 주로 수행하고 PM Agent가 최종 통합 시 다시 확인한다.

---

## 2.2 Requirement Coverage Evaluation

### [개념]

Requirement Coverage Evaluation은 Agent Output이 사용자 요청과 PM Agent Handoff의 요구사항을 얼마나 충족했는지 평가하는 과정이다.

Requirement Coverage가 낮으면 산출물이 아무리 잘 정리되어 있어도 실제 목적을 달성하지 못한다.

기본 구조:

```text
Requirements
→ Output Mapping
→ Covered
→ Missing
→ Partial
→ Coverage Score
```

---

### [핵심]

- Requirement Coverage는 요구사항 충족률이다.
- 각 Requirement가 Output에 반영되었는지 확인한다.
- 완전 반영, 부분 반영, 누락을 구분한다.
- 핵심 Requirement 누락은 Critical 또는 Major이다.
- 부가 Requirement 누락은 Minor일 수 있다.
- Coverage는 Review Findings와 연결해야 한다.
- Coverage가 낮으면 Fix Agent 수정 대상이다.

---

### [실무]

Requirement Coverage Matrix:

```md
## Requirement Coverage Matrix

| Requirement        | Output Evidence                            | Status  | Severity |
| ------------------ | ------------------------------------------ | ------- | -------- |
| 리뷰 작성 API      | POST /reviews 정의됨                       | Covered | -        |
| 리뷰 목록 조회 API | GET /festivals/{festivalId}/reviews 정의됨 | Covered | -        |
| 리뷰 수정 API      | PATCH /reviews/{reviewId} 정의됨           | Covered | -        |
| 리뷰 삭제 API      | DELETE API 없음                            | Missing | Major    |
| 작성자 본인 확인   | 설명 없음                                  | Missing | Critical |
| Slice 목록 응답    | Slice 사용 명시                            | Covered | -        |
```

Coverage Score 예시:

```json
{
  "totalRequirements": 6,
  "covered": 4,
  "partial": 0,
  "missing": 2,
  "coverageScore": 0.67,
  "criticalMissing": ["작성자 본인 확인"],
  "decision": "fail"
}
```

Coverage 평가 기준:

```text
Covered
→ 명확히 반영됨

Partial
→ 일부만 반영됨

Missing
→ 반영되지 않음

Not Applicable
→ 현재 Agent Scope 밖
```

---

### [FAQ]

Q. Requirement Coverage Evaluation이 뭐야?
A. Agent Output이 사용자 요청과 Handoff 요구사항을 얼마나 충족했는지 평가하는 과정이다.

Q. Requirement Coverage가 낮으면 어떻게 해?
A. Review Finding을 만들고 Fix Agent가 누락된 요구사항을 반영해야 한다.

Q. 핵심 요구사항 누락은 어떤 문제야?
A. Critical 또는 Major Issue로 분류해야 한다.

Q. Agent Scope 밖 요구사항은 어떻게 처리해?
A. Not Applicable로 표시하고 PM Agent가 다른 Agent에게 전달해야 한다.

---

## 2.3 Scope Compliance Evaluation

### [개념]

Scope Compliance Evaluation은 Agent가 자기 Role과 Scope 안에서 작업했는지 평가하는 과정이다.

Agent가 Scope 밖 작업을 수행하면 Role Overlap, 잘못된 Output, Tool Permission 위반, Workflow 혼선이 발생할 수 있다.

기본 구조:

```text
Agent Role
→ Allowed Scope
→ Output
→ Scope Match Check
→ Scope Violation Finding
```

---

### [핵심]

- Agent는 자기 Scope 안에서 작업해야 한다.
- PM Agent는 직접 구현을 과도하게 하면 안 된다.
- Specialist Agent는 자기 Domain 밖 작업을 확정하면 안 된다.
- Review Agent는 직접 수정하지 않는 것이 원칙이다.
- Fix Agent는 Review Findings 범위 안에서 수정해야 한다.
- DevOps Agent는 승인 없이 배포 실행하면 안 된다.
- Scope 위반은 Review Finding으로 기록한다.
- Scope 위반이 반복되면 Agent Definition을 수정해야 한다.

---

### [실무]

Scope Compliance Matrix:

```md
## Scope Compliance Matrix

| Agent         | Allowed Scope          | Output Behavior           | Status    |
| ------------- | ---------------------- | ------------------------- | --------- |
| SQL Agent     | Schema / Query / Index | Table 구조 제안           | Compliant |
| Backend Agent | API / DTO / Service    | React Component 설계 포함 | Violation |
| Review Agent  | 검토 / Finding         | 직접 코드 수정            | Violation |
| Fix Agent     | Review Finding 반영    | 새 기능 요구사항 추가     | Violation |
```

Scope Violation Finding 예시:

```md
## Review Finding

### Severity

Major

### Category

Scope Compliance

### Issue

Backend Agent Output에 React Component 구조 설계가 포함됨

### Evidence

Backend Agent Output에 ReviewList, ReviewForm Component 설계가 포함되어 있음

### Impact

Frontend Agent Scope와 책임이 충돌하고 API Contract 기반 Frontend 설계가 흐려질 수 있음

### Fix Direction

Backend Agent Output에서는 API Contract까지만 유지하고 Component 설계는 Frontend Agent Handoff로 분리
```

---

### [FAQ]

Q. Scope Compliance Evaluation이 뭐야?
A. Agent가 자기 Role과 Scope 안에서 작업했는지 평가하는 과정이다.

Q. Agent가 Scope 밖 작업을 하면 왜 문제야?
A. 역할 충돌, 잘못된 Output, Tool Permission 위반, Workflow 혼선이 생길 수 있다.

Q. Review Agent가 직접 수정하면 Scope 위반이야?
A. 원칙적으로 그렇다. Review Agent는 Findings를 작성하고 Fix Agent가 수정해야 한다.

Q. Scope 위반이 반복되면 어떻게 해?
A. Agent Definition, Handoff Template, Tool Permission, Review Criteria를 수정해야 한다.

---

# 3. Handoff Evaluation

## 3.1 Handoff Quality Evaluation

### [개념]

Handoff Quality Evaluation은 Source Agent가 Target Agent에게 전달한 Handoff가 작업 수행에 충분한지 평가하는 과정이다.

Handoff 품질은 Specialist Output 품질에 직접 영향을 준다.

좋은 Handoff는 Task, Context, Requirements, Constraints, RAG Scope, Tool Permission, Expected Output, Done Criteria가 명확하다.

기본 구조:

```text
Handoff
→ Completeness Check
→ Clarity Check
→ Scope Check
→ Output Criteria Check
→ Quality Score
```

---

### [핵심]

- Handoff는 Agent Output 품질의 출발점이다.
- Task가 명확해야 한다.
- Target Agent가 적절해야 한다.
- Requirements가 충분해야 한다.
- Constraints가 분리되어 있어야 한다.
- Context가 충분해야 한다.
- RAG Scope가 명시되어야 한다.
- Tool Permission이 명시되어야 한다.
- Expected Output이 구체적이어야 한다.
- Done Criteria가 검증 가능해야 한다.
- Open Questions가 표시되어야 한다.

---

### [실무]

Handoff Quality Evaluation Checklist:

```md
## Handoff Quality Evaluation Checklist

- [ ] Source Agent가 명확한가?
- [ ] Target Agent가 명확한가?
- [ ] Task가 한 문장으로 설명 가능한가?
- [ ] Task가 Target Agent Scope 안인가?
- [ ] Requirements가 누락되지 않았는가?
- [ ] Constraints가 Requirements와 분리되어 있는가?
- [ ] Context가 충분한가?
- [ ] RAG Scope가 지정되어 있는가?
- [ ] Tool Permission이 지정되어 있는가?
- [ ] Expected Output이 구체적인가?
- [ ] Done Criteria가 검증 가능한가?
- [ ] Assumptions가 표시되어 있는가?
- [ ] Open Questions가 표시되어 있는가?
```

Handoff Quality Score 예시:

```json
{
  "handoffId": "H-001",
  "targetAgent": "Backend Agent",
  "taskClarity": 0.9,
  "requirementCompleteness": 0.8,
  "constraintClarity": 0.9,
  "contextSufficiency": 0.7,
  "ragScopeQuality": 0.8,
  "expectedOutputClarity": 0.9,
  "doneCriteriaQuality": 0.8,
  "overallScore": 0.83
}
```

---

### [FAQ]

Q. Handoff Quality Evaluation이 뭐야?
A. Source Agent가 Target Agent에게 전달한 Handoff가 작업 수행에 충분한지 평가하는 과정이다.

Q. Handoff 품질이 중요한 이유는?
A. Handoff가 부실하면 Specialist Agent가 추측으로 작업하고 Output 품질이 떨어지기 때문이다.

Q. 좋은 Handoff 기준은?
A. Task, Requirements, Constraints, Context, RAG Scope, Tool Permission, Expected Output, Done Criteria가 명확해야 한다.

Q. Handoff 품질은 누가 평가해?
A. PM Agent가 전달 전 평가하고 Review Agent가 Workflow 검토 시 평가할 수 있다.

---

## 3.2 Handoff Failure Evaluation

### [개념]

Handoff Failure Evaluation은 Handoff 문제로 인해 Agent Output 실패가 발생했는지 평가하는 과정이다.

Agent Output이 나쁘다고 해서 항상 Target Agent만의 문제는 아니다. 원인이 Poor Handoff일 수 있다.

기본 구조:

```text
Bad Output
→ Check Agent Skill
→ Check Handoff
→ Identify Root Cause
→ Fix Handoff or Output
```

---

### [핵심]

- Agent Output 실패 원인은 Handoff일 수 있다.
- Requirements 누락은 Output 누락으로 이어진다.
- Constraints 누락은 규칙 위반으로 이어진다.
- Context 부족은 Hallucination으로 이어진다.
- Expected Output 누락은 비구조화 결과로 이어진다.
- RAG Scope 누락은 잘못된 Retrieval로 이어진다.
- Handoff 실패는 PM Agent 수정 대상이다.
- Output 실패와 Handoff 실패를 구분해야 한다.

---

### [실무]

Handoff Failure Root Cause 예시:

```md
## Handoff Failure Evaluation

### Observed Output Failure

Backend Agent Output에 DELETE API가 누락됨

### Handoff Check

Handoff Requirements에 리뷰 삭제 요구사항이 없음

### Root Cause

Backend Agent의 누락이 아니라 PM Agent Handoff의 Requirement 누락

### Fix Target

PM Agent Handoff

### Fix Direction

Handoff Requirements에 "Review author can delete own review" 추가 후 Backend Agent 재실행
```

Handoff vs Agent Failure 구분:

| 현상            | Handoff 원인            | Agent 원인                         |
| --------------- | ----------------------- | ---------------------------------- |
| 요구사항 누락   | Handoff에 요구사항 없음 | Handoff에는 있었지만 Output에 없음 |
| 제약 위반       | Handoff에 제약 없음     | 제약 있었지만 무시                 |
| 비구조화 Output | Expected Output 없음    | Template 무시                      |
| 잘못된 Domain   | Target Agent 오류       | Agent가 Scope 위반                 |
| 추측 증가       | Context 부족            | Assumption 표시 실패               |

---

### [FAQ]

Q. Handoff Failure Evaluation이 뭐야?
A. Agent Output 실패가 Handoff 문제에서 비롯되었는지 평가하는 과정이다.

Q. Agent Output이 나쁘면 항상 Agent 잘못이야?
A. 아니다. Handoff에 요구사항, 제약, Context가 부족했을 수 있다.

Q. Handoff 실패와 Agent 실패는 왜 구분해야 해?
A. 수정 대상이 다르기 때문이다. Handoff 실패는 PM Agent가, Agent 실패는 Specialist Agent 또는 Fix Agent가 수정해야 한다.

Q. Handoff 실패를 줄이려면?
A. Handoff Quality Checklist와 Done Criteria를 적용해야 한다.

---

# 4. RAG Retrieval Evaluation

## 4.1 Retrieval Relevance Evaluation

### [개념]

Retrieval Relevance Evaluation은 RAG 검색 결과가 현재 Task와 얼마나 관련 있는지 평가하는 과정이다.

RAG 검색 결과가 많아도 Task와 관련 없으면 Agent Output 품질을 떨어뜨린다.

기본 구조:

```text
Retrieval Query
→ Retrieved Context
→ Relevance Check
→ Use / Exclude
→ Query Adjust
```

---

### [핵심]

- Retrieval Relevance는 검색 결과 관련성이다.
- 검색 결과가 Target Agent Domain과 맞아야 한다.
- 검색 결과가 Task Type과 맞아야 한다.
- 검색 결과가 Requirements 해결에 도움이 되어야 한다.
- 관련 없는 Context는 제외해야 한다.
- Relevance가 낮으면 Query Narrowing이 필요하다.
- 필요한 Context가 없으면 Query Expansion이 필요하다.
- Review Agent는 사용된 RAG Context의 적절성을 검토할 수 있다.

---

### [실무]

Retrieval Relevance 평가 기준:

| Score | 기준                                           |
| ----: | ---------------------------------------------- |
|   1.0 | Task와 직접 관련, Output 생성에 바로 사용 가능 |
|  0.75 | 관련성 높음, 일부 보조 정리 필요               |
|   0.5 | 부분 관련, 제한적으로 사용 가능                |
|  0.25 | 약한 관련, 사용 주의                           |
|   0.0 | 무관, 제외 필요                                |

Retrieval Relevance Evaluation 예시:

```json
{
  "query": "Backend Agent API Design ApiResponse Slice",
  "retrievedContexts": [
    {
      "document": "API Design Domain Rules",
      "relevance": 1.0,
      "decision": "use"
    },
    {
      "document": "React Component Design",
      "relevance": 0.25,
      "decision": "exclude"
    },
    {
      "document": "Security Advanced Domain Rules",
      "relevance": 0.75,
      "decision": "use_for_authorization"
    }
  ]
}
```

---

### [FAQ]

Q. Retrieval Relevance Evaluation이 뭐야?
A. RAG 검색 결과가 현재 Task와 얼마나 관련 있는지 평가하는 과정이다.

Q. 검색 결과가 많으면 좋은 거야?
A. 아니다. 관련 없는 검색 결과가 많으면 Agent가 잘못된 Context를 사용할 수 있다.

Q. Relevance가 낮으면 어떻게 해?
A. Query Narrowing으로 Domain과 Task를 좁혀야 한다.

Q. 필요한 문서가 검색되지 않으면?
A. Query Expansion 또는 RAG Scope 확장을 수행해야 한다.

---

## 4.2 Retrieval Sufficiency Evaluation

### [개념]

Retrieval Sufficiency Evaluation은 검색된 RAG Context가 현재 Task를 수행하기에 충분한지 평가하는 과정이다.

검색 결과가 관련 있어도 필요한 내용이 부족하면 Agent는 추측으로 빈 부분을 채울 수 있다.

기본 구조:

```text
Task Requirements
→ Retrieved Context
→ Required Knowledge Check
→ Sufficiency Decision
→ Expand if Needed
```

---

### [핵심]

- Sufficiency는 검색 결과의 충분성이다.
- 관련성만으로는 충분하지 않다.
- Requirements 해결에 필요한 정보가 있는지 확인한다.
- Constraints 확인에 필요한 규칙이 있는지 확인한다.
- Output Format 작성에 필요한 기준이 있는지 확인한다.
- Context가 부족하면 Missing Context로 표시한다.
- 필요한 경우 Query Expansion을 수행한다.
- 필요한 경우 PM Agent가 추가 RAG Scope를 지정한다.

---

### [실무]

Retrieval Sufficiency Checklist:

```md
## Retrieval Sufficiency Checklist

- [ ] Requirements를 해결할 정보가 있는가?
- [ ] Constraints를 확인할 규칙이 있는가?
- [ ] Output Format 기준이 있는가?
- [ ] Domain Rules가 포함되었는가?
- [ ] Master Rules가 필요한 경우 포함되었는가?
- [ ] 예외 / 위험 / 실패 기준이 포함되었는가?
- [ ] FAQ 또는 Retrieval Query 표현이 포함되었는가?
- [ ] Missing Context가 남아 있는가?
```

Sufficiency Evaluation 예시:

```json
{
  "task": "RAG Document Part13 Evaluation 작성",
  "retrievedContext": [
    "Master RAG Rules",
    "Multi-Agent System Domain Rules",
    "Previous Part Documents"
  ],
  "requiredKnowledge": [
    "Evaluation concept",
    "Agent Output Evaluation",
    "Handoff Evaluation",
    "RAG Retrieval Evaluation",
    "Metrics",
    "Quality Control"
  ],
  "sufficiency": "sufficient",
  "missingContext": []
}
```

Insufficient 예시:

```json
{
  "task": "Security Review Agent 기준 작성",
  "retrievedContext": ["API Design Rules"],
  "sufficiency": "insufficient",
  "missingContext": [
    "Security Advanced Domain Rules",
    "JWT Authorization Rules"
  ],
  "action": "Expand RAG Scope to Security Advanced"
}
```

---

### [FAQ]

Q. Retrieval Sufficiency Evaluation이 뭐야?
A. 검색된 RAG Context가 현재 Task를 수행하기에 충분한지 평가하는 과정이다.

Q. Relevance와 Sufficiency는 달라?
A. 다르다. Relevance는 관련성이고 Sufficiency는 작업 수행에 필요한 정보가 충분한지이다.

Q. Sufficiency가 낮으면 어떻게 해?
A. Query Expansion, RAG Scope 확장, Missing Context 표시를 수행해야 한다.

Q. 검색 결과가 관련 있지만 부족하면?
A. Partial로 표시하고 추가 검색이나 PM Agent 보강을 요청해야 한다.

---

## 4.3 Retrieval Precision and Recall

### [개념]

Retrieval Precision과 Recall은 RAG 검색 품질을 평가하는 기본 지표이다.

Precision은 검색된 Context 중 실제로 유용한 Context 비율이고, Recall은 필요한 Context 중 실제로 검색된 Context 비율이다.

기본 구조:

```text
Precision
→ 검색된 것 중 맞는 비율

Recall
→ 필요한 것 중 검색된 비율
```

---

### [핵심]

- Precision은 검색 결과의 정확도이다.
- Recall은 필요한 문서 회수율이다.
- Precision이 낮으면 관련 없는 문서가 많다.
- Recall이 낮으면 필요한 문서가 누락된다.
- RAG Scope가 너무 넓으면 Precision이 낮아질 수 있다.
- RAG Scope가 너무 좁으면 Recall이 낮아질 수 있다.
- Query Narrowing은 Precision을 높인다.
- Query Expansion은 Recall을 높인다.
- Agent 작업 유형에 따라 Precision과 Recall 균형이 달라진다.

---

### [실무]

Precision / Recall 예시:

```text
Task:
Backend Review API 설계

필요 문서:
- Spring Boot Domain Rules
- JPA Advanced Domain Rules
- API Design Domain Rules
- Security Advanced Domain Rules

검색 문서:
- Spring Boot Domain Rules
- JPA Advanced Domain Rules
- React Component Design
- Docker Domain Rules

Relevant Retrieved:
- Spring Boot
- JPA

Precision:
2 relevant / 4 retrieved = 0.5

Recall:
2 retrieved relevant / 4 needed = 0.5
```

개선 방향:

```text
Precision 낮음
→ Query Narrowing
→ 불필요 Domain 제거

Recall 낮음
→ Query Expansion
→ Additional RAG Scope 추가
```

RAG 평가 Matrix:

| 문제             | 현상                        | 개선                  |
| ---------------- | --------------------------- | --------------------- |
| Low Precision    | 관련 없는 문서 많음         | Query Narrowing       |
| Low Recall       | 필요한 문서 누락            | Query Expansion       |
| Low Relevance    | 검색 결과가 Task와 안 맞음  | Domain 키워드 보강    |
| Low Sufficiency  | 관련 있지만 부족함          | Scope 확장            |
| Context Conflict | 검색 결과가 Decision과 충돌 | Context Priority 적용 |

---

### [FAQ]

Q. Retrieval Precision이 뭐야?
A. 검색된 Context 중 실제로 유용한 Context의 비율이다.

Q. Retrieval Recall이 뭐야?
A. 필요한 Context 중 실제로 검색된 Context의 비율이다.

Q. Precision이 낮으면 어떻게 해?
A. Query Narrowing으로 검색 범위를 좁힌다.

Q. Recall이 낮으면 어떻게 해?
A. Query Expansion 또는 RAG Scope 확장으로 필요한 문서를 더 검색한다.

---

# 5. Review Evaluation

## 5.1 Review Quality Evaluation

### [개념]

Review Quality Evaluation은 Review Agent가 작성한 Review Findings와 Review Report가 검토 기준에 맞는지 평가하는 과정이다.

좋은 Review는 문제를 찾는 것뿐 아니라 Severity, Evidence, Impact, Fix Direction을 명확히 제공해야 한다.

기본 구조:

```text
Review Target
→ Review Criteria
→ Findings
→ Evidence
→ Fix Direction
→ Pass / Fail
```

---

### [핵심]

- Review는 기준 기반이어야 한다.
- Review Finding에는 Severity가 있어야 한다.
- Review Finding에는 Evidence가 있어야 한다.
- Impact가 설명되어야 한다.
- Fix Direction이 있어야 한다.
- Pass / Fail이 명확해야 한다.
- 취향성 비판은 결함처럼 작성하면 안 된다.
- Context 부족 상태에서 단정하면 안 된다.
- Review Criteria는 반복 중 바뀌면 안 된다.
- Review 결과는 Fix Agent가 바로 사용할 수 있어야 한다.

---

### [실무]

Review Quality Checklist:

```md
## Review Quality Checklist

- [ ] Review Target이 명확한가?
- [ ] Review Criteria가 명확한가?
- [ ] Findings가 기준 기반인가?
- [ ] 각 Finding에 Severity가 있는가?
- [ ] 각 Finding에 Evidence가 있는가?
- [ ] 각 Finding에 Impact가 있는가?
- [ ] 각 Finding에 Fix Direction이 있는가?
- [ ] Pass / Fail이 명확한가?
- [ ] Missing Context를 단정하지 않았는가?
- [ ] 취향성 비판을 결함처럼 작성하지 않았는가?
- [ ] Fix Agent가 바로 사용할 수 있는가?
```

나쁜 Review 예시:

```text
전체적으로 별로임. 더 깔끔하게 고쳐야 함.
```

문제:

- Severity 없음
- Evidence 없음
- Impact 없음
- Fix Direction 없음
- 취향성 표현

좋은 Review 예시:

```md
## Review Finding

### Severity

Major

### Category

Requirement Coverage

### Issue

Handoff에는 Review Delete API가 요구되었으나 Backend Output에 DELETE endpoint가 없음

### Evidence

Requirements: "Review author can delete own review"
Output: POST /reviews, GET /reviews, PATCH /reviews/{reviewId}만 포함

### Impact

리뷰 삭제 요구사항이 충족되지 않음

### Fix Direction

DELETE /reviews/{reviewId} API Contract와 작성자 권한 검증 조건을 추가
```

---

### [FAQ]

Q. Review Quality Evaluation이 뭐야?
A. Review Agent의 Review Findings와 Review Report가 기준, 근거, 수정 방향을 갖추었는지 평가하는 과정이다.

Q. 좋은 Review Finding에는 뭐가 있어야 해?
A. Severity, Category, Issue, Evidence, Impact, Fix Direction이 있어야 한다.

Q. 취향성 비판도 Review Finding이 될 수 있어?
A. 아니다. 명확한 기준과 근거가 있어야 한다.

Q. Review Quality가 낮으면 어떻게 해?
A. Review Agent Prompt, Review Criteria, Finding Template을 개선해야 한다.

---

## 5.2 Review Accuracy Evaluation

### [개념]

Review Accuracy Evaluation은 Review Agent가 실제 문제를 정확히 발견했는지, 없는 문제를 잘못 지적하지 않았는지 평가하는 과정이다.

Review Agent가 문제를 놓치면 False Negative이고, 문제가 아닌 것을 문제로 지적하면 False Positive이다.

기본 구조:

```text
Actual Issues
→ Review Findings
→ True Positive
→ False Positive
→ False Negative
```

---

### [핵심]

- Review Accuracy는 검토 정확도이다.
- True Positive는 실제 문제를 정확히 찾은 것이다.
- False Positive는 문제가 아닌 것을 문제로 지적한 것이다.
- False Negative는 실제 문제를 놓친 것이다.
- Critical False Negative는 매우 위험하다.
- False Positive가 많으면 Fix Agent가 불필요한 수정을 한다.
- Review Criteria가 불명확하면 Accuracy가 낮아진다.
- Review Accuracy는 반복 테스트로 개선한다.

---

### [실무]

Review Accuracy Matrix:

```md
## Review Accuracy Matrix

| Actual Issue           | Review Finding              | Result         |
| ---------------------- | --------------------------- | -------------- |
| DELETE API 누락        | DELETE API 누락 지적        | True Positive  |
| 작성자 권한 검증 누락  | 지적 없음                   | False Negative |
| DTO 구조 정상          | DTO 구조 문제라고 지적      | False Positive |
| Retrieval Queries 누락 | Retrieval Queries 누락 지적 | True Positive  |
```

Review Accuracy Metrics:

```json
{
  "truePositive": 8,
  "falsePositive": 2,
  "falseNegative": 1,
  "precision": 0.8,
  "recall": 0.89,
  "criticalFalseNegative": 0,
  "decision": "acceptable_with_improvement"
}
```

개선 방향:

| 문제                | 개선                        |
| ------------------- | --------------------------- |
| False Positive 많음 | Review Criteria 구체화      |
| False Negative 많음 | Checklist 보강              |
| Critical 누락       | Severity 기준 강화          |
| 근거 부족           | Evidence 필수화             |
| Fix 불가 Finding    | Fix Direction Template 적용 |

---

### [FAQ]

Q. Review Accuracy Evaluation이 뭐야?
A. Review Agent가 실제 문제를 정확히 찾고 잘못된 지적을 줄였는지 평가하는 과정이다.

Q. False Positive가 뭐야?
A. 문제가 아닌 것을 문제로 잘못 지적한 것이다.

Q. False Negative가 뭐야?
A. 실제 문제를 놓친 것이다.

Q. Critical False Negative가 위험한 이유는?
A. 보안, 데이터 손상, 요구사항 실패 같은 중요한 문제가 최종 출력으로 전달될 수 있기 때문이다.

---

# 6. Fix Evaluation

## 6.1 Fix Quality Evaluation

### [개념]

Fix Quality Evaluation은 Fix Agent가 Review Findings를 정확히 반영했는지, 기존 요구사항을 보존했는지, 새로운 문제를 만들지 않았는지 평가하는 과정이다.

Fix는 단순히 변경이 아니라 Review Finding 해결과 요구사항 보존을 동시에 만족해야 한다.

기본 구조:

```text
Review Findings
→ Fix Output
→ Applied Fix Check
→ Preserve Requirement Check
→ Regression Risk Check
→ Re-review Decision
```

---

### [핵심]

- Fix는 Review Findings를 해결해야 한다.
- Critical Finding은 반드시 해결되어야 한다.
- Major Finding은 해결하거나 PM Decision으로 분리해야 한다.
- Fix Scope를 지켜야 한다.
- 기존 요구사항을 보존해야 한다.
- 새 요구사항을 임의로 추가하면 안 된다.
- Change Summary가 있어야 한다.
- Regression Risk가 표시되어야 한다.
- Re-review 필요 여부가 표시되어야 한다.
- Fix 후 Review Agent가 재검토할 수 있어야 한다.

---

### [실무]

Fix Quality Checklist:

```md
## Fix Quality Checklist

- [ ] Review Findings가 모두 확인되었는가?
- [ ] Critical Findings가 해결되었는가?
- [ ] Major Findings가 해결 또는 Decision으로 분리되었는가?
- [ ] Fix Scope를 벗어나지 않았는가?
- [ ] 기존 Requirements가 보존되었는가?
- [ ] PM Agent Decisions가 보존되었는가?
- [ ] 새 요구사항을 임의로 추가하지 않았는가?
- [ ] Change Summary가 작성되었는가?
- [ ] Regression Risk가 표시되었는가?
- [ ] Re-review 필요 여부가 표시되었는가?
```

Fix Evaluation Matrix:

```md
## Fix Evaluation Matrix

| Review Finding         | Applied Fix               | Status          | Note               |
| ---------------------- | ------------------------- | --------------- | ------------------ |
| DELETE API 누락        | DELETE /reviews/{id} 추가 | Fixed           | -                  |
| 작성자 권한 검증 누락  | owner check 추가          | Fixed           | -                  |
| 중복 리뷰 정책 불명확  | Open Question 유지        | Decision Needed | PM 확인 필요       |
| Rating Validation 누락 | 0~5 validation 추가       | Fixed           | Frontend 검증 영향 |
```

---

### [FAQ]

Q. Fix Quality Evaluation이 뭐야?
A. Fix Agent가 Review Findings를 정확히 반영하고 기존 요구사항을 보존했는지 평가하는 과정이다.

Q. Fix가 성공했다는 기준은?
A. Critical / Major Findings가 해결되고 기존 요구사항이 보존되며 Regression Risk가 표시된 상태다.

Q. Fix Scope를 벗어나면 어떻게 돼?
A. Over-fixing으로 분류하고 Review Agent가 다시 Finding을 작성해야 한다.

Q. Fix 후 Re-review가 필요한 경우는?
A. Critical 또는 Major Issue를 수정했거나 API Contract, DB Schema, Output Format이 변경된 경우다.

---

## 6.2 Regression Evaluation

### [개념]

Regression Evaluation은 Fix가 기존 요구사항, 기능, API Contract, Agent Output, RAG 문서 구조에 부정적 영향을 주었는지 평가하는 과정이다.

Fix가 Review Finding을 해결했더라도 기존 기능을 깨뜨리면 전체 품질은 낮아진다.

기본 구조:

```text
Applied Fix
→ Affected Area
→ Existing Requirement Check
→ New Conflict Check
→ Regression Decision
```

---

### [핵심]

- Regression은 수정으로 인한 부작용이다.
- 기존 요구사항이 유지되었는지 확인한다.
- 기존 API Contract가 무단 변경되지 않았는지 확인한다.
- 기존 Agent Output과 충돌하지 않는지 확인한다.
- Shared State Decision과 충돌하지 않는지 확인한다.
- RAG 문서 구조가 깨지지 않았는지 확인한다.
- Tool Permission 위반이 생기지 않았는지 확인한다.
- Regression Risk는 Re-review에서 반드시 확인한다.

---

### [실무]

Regression Evaluation Checklist:

```md
## Regression Evaluation Checklist

- [ ] 기존 Functional Requirements가 유지되었는가?
- [ ] 기존 Constraints가 유지되었는가?
- [ ] API Contract가 무단 변경되지 않았는가?
- [ ] DTO / Response Field가 기존 Frontend와 충돌하지 않는가?
- [ ] DB Schema 변경이 기존 Query와 충돌하지 않는가?
- [ ] Shared State Decisions가 유지되었는가?
- [ ] RAG 문서 Required Section이 유지되었는가?
- [ ] Retrieval Queries가 유지되었는가?
- [ ] Tool Permission 위반이 없는가?
- [ ] 새로운 Critical / Major Issue가 생기지 않았는가?
```

Regression Finding 예시:

```md
## Regression Finding

### Severity

Major

### Category

Regression

### Issue

Fix 과정에서 기존 GET /festivals/{festivalId}/reviews API가 제거됨

### Evidence

Updated Output에는 POST, PATCH, DELETE만 포함됨

### Impact

리뷰 목록 조회 요구사항이 훼손됨

### Fix Direction

GET API를 복구하고 기존 Slice 응답 조건을 유지
```

---

### [FAQ]

Q. Regression Evaluation이 뭐야?
A. Fix가 기존 요구사항, 기능, API Contract, 문서 구조에 부정적 영향을 주었는지 평가하는 과정이다.

Q. Fix가 Finding을 해결했는데 기존 기능이 깨지면 성공이야?
A. 아니다. Regression이 발생한 것이므로 다시 수정해야 한다.

Q. Regression Evaluation은 언제 해?
A. Fix Agent가 Updated Output을 만든 후 Re-review 단계에서 수행한다.

Q. RAG 문서에서도 Regression이 있어?
A. 있다. Fix 과정에서 Required Section, FAQ, Retrieval Queries가 깨질 수 있다.

---

# 7. Workflow Evaluation

## 7.1 Workflow Quality Evaluation

### [개념]

Workflow Quality Evaluation은 Multi-Agent Workflow 전체가 적절한 Pattern으로 실행되었는지, 각 Step이 안정적으로 연결되었는지 평가하는 과정이다.

Workflow Quality는 개별 Agent Output만으로 판단할 수 없다. Routing, Handoff, Shared State, Review-Fix, Tool Permission, Final Integration을 함께 봐야 한다.

기본 구조:

```text
Workflow Pattern
→ Step Execution
→ State Update
→ Review-Fix
→ Final Output
→ Workflow Quality
```

---

### [핵심]

- Workflow Pattern이 요청에 적합했는지 평가한다.
- Step 순서가 적절했는지 확인한다.
- Agent Routing이 적절했는지 확인한다.
- Handoff가 Step마다 충분했는지 확인한다.
- Shared State가 갱신되었는지 확인한다.
- Review-Fix가 필요한 곳에 적용되었는지 확인한다.
- Tool Permission이 준수되었는지 확인한다.
- 중간 실패가 숨겨지지 않았는지 확인한다.
- Final Output이 요구사항을 충족했는지 확인한다.

---

### [실무]

Workflow Quality Checklist:

```md
## Workflow Quality Checklist

- [ ] 요청에 맞는 Workflow Pattern이 선택되었는가?
- [ ] 필요한 Agent가 모두 포함되었는가?
- [ ] 불필요한 Agent가 과도하게 포함되지 않았는가?
- [ ] Step 순서가 의존성과 일치하는가?
- [ ] 각 Step의 Output이 Shared State에 반영되었는가?
- [ ] Blocked / Failed 상태가 숨겨지지 않았는가?
- [ ] Review-Fix가 필요한 곳에 적용되었는가?
- [ ] Human Approval이 필요한 작업을 차단했는가?
- [ ] Final Integration이 수행되었는가?
- [ ] Final Output이 사용자 요청을 충족하는가?
```

Workflow Quality Score 예시:

```json
{
  "workflowPattern": "Sequential Workflow",
  "patternFit": 0.95,
  "routingAccuracy": 0.9,
  "stepCompleteness": 0.85,
  "stateConsistency": 0.9,
  "reviewFixQuality": 0.8,
  "toolPermissionCompliance": 1.0,
  "finalOutputQuality": 0.88,
  "overallWorkflowQuality": 0.9
}
```

---

### [FAQ]

Q. Workflow Quality Evaluation이 뭐야?
A. Multi-Agent Workflow 전체가 적절한 Pattern으로 실행되고 각 Step이 안정적으로 연결되었는지 평가하는 과정이다.

Q. Workflow 품질은 개별 Agent Output만 보면 돼?
A. 아니다. Routing, Handoff, Shared State, Review-Fix, Tool Permission, Final Output을 함께 봐야 한다.

Q. Workflow Pattern이 잘못 선택되면 어떻게 돼?
A. 불필요한 Agent가 실행되거나 필요한 Agent가 누락되어 품질과 효율이 떨어진다.

Q. Workflow Quality가 낮으면 무엇을 개선해?
A. Pattern Selection, Agent Routing, Handoff Template, Shared State Update, Review-Fix 기준을 개선한다.

---

## 7.2 Workflow Metrics

### [개념]

Workflow Metrics는 Multi-Agent Workflow 품질을 수치 또는 상태로 평가하기 위한 지표이다.

Metrics는 시스템 개선을 위해 사용하며, 단순 점수보다 어떤 부분이 실패했는지 추적하는 것이 중요하다.

기본 구조:

```text
Metric
→ Measurement
→ Threshold
→ Decision
→ Improvement Action
```

---

### [핵심]

- Metrics는 품질 추적 지표이다.
- Routing Accuracy를 측정한다.
- Handoff Completeness를 측정한다.
- Requirement Coverage를 측정한다.
- Retrieval Relevance를 측정한다.
- Review Finding Quality를 측정한다.
- Fix Success Rate를 측정한다.
- Regression Rate를 측정한다.
- Tool Permission Compliance를 측정한다.
- Final Output Acceptance를 측정한다.
- Metrics는 개선 Action과 연결되어야 한다.

---

### [실무]

추천 Workflow Metrics:

| Metric                     | 의미                     | 개선 대상         |
| -------------------------- | ------------------------ | ----------------- |
| Routing Accuracy           | 올바른 Agent 선택 비율   | Router / PM Agent |
| Handoff Completeness       | Handoff 필수 필드 충족률 | Handoff Template  |
| Requirement Coverage       | 요구사항 반영률          | PM / Specialist   |
| Retrieval Relevance        | 검색 결과 관련성         | RAG Query         |
| Retrieval Sufficiency      | 검색 결과 충분성         | RAG Scope         |
| Review Precision           | Review Finding 정확도    | Review Agent      |
| Review Recall              | 실제 문제 발견률         | Review Checklist  |
| Fix Success Rate           | Finding 해결률           | Fix Agent         |
| Regression Rate            | 수정 후 새 문제 발생률   | Fix Scope         |
| Tool Permission Compliance | 권한 준수율              | Tool Policy       |
| Final Output Acceptance    | 사용자 목적 충족률       | 전체 Workflow     |

Metrics Record 예시:

```json
{
  "workflowId": "WF-013",
  "metrics": {
    "routingAccuracy": 1.0,
    "handoffCompleteness": 0.92,
    "requirementCoverage": 0.95,
    "retrievalRelevance": 0.88,
    "retrievalSufficiency": 0.9,
    "reviewFindingQuality": 0.85,
    "fixSuccessRate": 0.9,
    "regressionRate": 0.05,
    "toolPermissionCompliance": 1.0,
    "finalOutputAcceptance": 0.95
  },
  "improvementActions": [
    "Add Open Questions field to all Handoff templates",
    "Expand Review Agent checklist for Regression"
  ]
}
```

---

### [FAQ]

Q. Workflow Metrics가 뭐야?
A. Multi-Agent Workflow 품질을 수치 또는 상태로 평가하기 위한 지표다.

Q. 중요한 Workflow Metrics는?
A. Routing Accuracy, Handoff Completeness, Requirement Coverage, Retrieval Relevance, Review Quality, Fix Success Rate, Tool Permission Compliance다.

Q. Metrics는 점수만 기록하면 돼?
A. 아니다. 점수와 함께 개선 Action을 기록해야 한다.

Q. 개인 AI 개발팀에서 처음부터 모든 Metrics를 측정해야 해?
A. 아니다. 초기에는 Handoff Completeness, Requirement Coverage, Review-Fix 결과부터 측정하면 충분하다.

---

# 8. Quality Control

## 8.1 Quality Gate

### [개념]

Quality Gate는 다음 Workflow Step으로 넘어가기 전에 충족해야 하는 품질 기준이다.

Quality Gate는 불완전한 Output이 다음 Agent로 전달되는 것을 막는다.

기본 구조:

```text
Step Output
→ Quality Gate
→ Pass
→ Next Step

Step Output
→ Quality Gate
→ Fail
→ Fix / Re-run / PM Decision
```

---

### [핵심]

- Quality Gate는 단계 이동 전 검수 기준이다.
- Handoff 전 Quality Gate가 필요하다.
- Agent Output 후 Quality Gate가 필요하다.
- Review-Fix 후 Quality Gate가 필요하다.
- Dangerous Tool 실행 전 Quality Gate가 필요하다.
- Critical Issue가 있으면 다음 단계로 넘어가면 안 된다.
- Blocked 상태를 Completed처럼 처리하면 안 된다.
- Quality Gate 기준은 명확해야 한다.

---

### [실무]

Quality Gate 예시:

```md
## Quality Gate - Specialist Output

### Pass Criteria

- Requirements Coverage 80% 이상
- Critical Issue 없음
- Agent Scope 위반 없음
- Required Output Section 포함
- Risks와 Open Questions 표시

### Fail Criteria

- Critical Requirement 누락
- Tool Permission 위반
- Output Status가 Blocked 또는 Failed
- Missing Context를 확정처럼 작성
- Done Criteria 미충족
```

RAG Document Quality Gate:

```md
## Quality Gate - RAG Document

### Pass Criteria

- Required Section 포함
- [개념], [핵심], [실무], [FAQ] 포함
- Retrieval Queries 포함
- Master Rules / Domain Rules 준수
- Writing Block Output Format 준수

### Fail Criteria

- Retrieval Queries 누락
- Required Section 누락
- FAQ 형식 위반
- Output Format 위반
- 현재 사용자 요청 위반
```

---

### [FAQ]

Q. Quality Gate가 뭐야?
A. 다음 Workflow Step으로 넘어가기 전에 충족해야 하는 품질 기준이다.

Q. Quality Gate가 필요한 이유는?
A. 불완전한 Output이 다음 Agent로 전달되어 오류가 전파되는 것을 막기 위해서다.

Q. Quality Gate에서 Fail이면 어떻게 해?
A. Fix, Re-run, Plan Revision, PM Decision, 사용자 확인 중 하나로 처리한다.

Q. RAG 문서 Quality Gate의 핵심 기준은?
A. Required Section, FAQ, Retrieval Queries, Master Rules, Domain Rules, Output Format 준수다.

---

## 8.2 Continuous Improvement

### [개념]

Continuous Improvement는 Evaluation 결과를 바탕으로 Agent Definition, Handoff Template, RAG Scope, Review Criteria, Workflow Pattern을 지속적으로 개선하는 과정이다.

Multi-Agent System은 한 번 설계하고 끝나는 구조가 아니라, 실패 사례와 평가 결과를 반영해 점진적으로 안정화해야 한다.

기본 구조:

```text
Evaluation Result
→ Failure Pattern
→ Root Cause
→ Improvement Action
→ Updated Rules
→ Re-evaluation
```

---

### [핵심]

- Evaluation 결과는 개선으로 연결해야 한다.
- 반복 실패 패턴을 기록한다.
- Root Cause를 분석한다.
- Agent Definition을 보강한다.
- Handoff Template을 개선한다.
- RAG Scope를 조정한다.
- Review Checklist를 보강한다.
- Tool Permission을 조정한다.
- Workflow Pattern 선택 기준을 개선한다.
- 개선 후 다시 평가한다.

---

### [실무]

Continuous Improvement 예시:

```md
## Improvement Record

### Observed Failure

Backend Agent Output에서 Security Rule 누락 반복

### Root Cause

Backend Agent Handoff의 constraints에 Security 기준이 누락됨

### Improvement Action

- Backend Handoff Template에 Security Requirements 필드 추가
- Backend Agent RAG Scope에 Security Advanced 조건부 추가
- Review Agent Checklist에 Authorization Rule 항목 추가

### Expected Effect

작성자 권한 검증 누락 감소

### Re-evaluation

다음 Backend API 설계 Workflow에서 확인
```

개선 대상 Matrix:

| 반복 문제           | 개선 대상                       |
| ------------------- | ------------------------------- |
| Routing 오류        | Routing Rule, Domain Detection  |
| Output 누락         | Handoff Template, Done Criteria |
| RAG 검색 실패       | Retrieval Query, RAG Scope      |
| Review 부정확       | Review Checklist, Severity 기준 |
| Fix 과도 수정       | Fix Scope, Regression Checklist |
| Tool 권한 위반      | Tool Permission Matrix          |
| Workflow 반복 실패  | Workflow Pattern Selection      |
| Final Output 불만족 | PM Agent Integration 기준       |

---

### [FAQ]

Q. Continuous Improvement가 뭐야?
A. Evaluation 결과를 바탕으로 Agent Definition, Handoff, RAG Scope, Review Criteria, Workflow Pattern을 지속적으로 개선하는 과정이다.

Q. Multi-Agent System은 한 번 설계하면 끝이야?
A. 아니다. 실패 사례와 평가 결과를 반영해 점진적으로 안정화해야 한다.

Q. 반복 실패가 발생하면 무엇을 봐야 해?
A. Root Cause가 Agent 자체인지, Handoff인지, RAG Scope인지, Review 기준인지 확인해야 한다.

Q. 개선 후에는 무엇을 해야 해?
A. 다음 Workflow에서 같은 문제가 줄어드는지 Re-evaluation해야 한다.

---

# 9. RAG Document Evaluation

## 9.1 RAG Document Quality Evaluation

### [개념]

RAG Document Quality Evaluation은 RAG 문서가 AI Agent Retrieval에 적합한 구조와 내용을 갖추었는지 평가하는 과정이다.

RAG 문서의 목적은 사람에게 읽기 좋은 장문 설명이 아니라, Agent가 필요한 정보를 검색하고 사용할 수 있도록 만드는 것이다.

기본 구조:

```text
RAG Document
→ Required Structure Check
→ FAQ Check
→ Retrieval Queries Check
→ Chunk Independence Check
→ Quality Decision
```

---

### [핵심]

- RAG 문서는 Retrieval 최적화가 우선이다.
- Required Section을 확인한다.
- `[개념]`, `[핵심]`, `[실무]`, `[FAQ]`를 확인한다.
- Retrieval Queries를 확인한다.
- FAQ가 실제 사용자 질문 표현을 포함하는지 확인한다.
- 용어 통일을 확인한다.
- Chunk가 독립 검색 가능한지 확인한다.
- 중복이 과도하지 않은지 확인한다.
- 오타와 구조 오류를 확인한다.
- 관련 Domain Rules를 반영했는지 확인한다.

---

### [실무]

RAG Document Evaluation Checklist:

```md
## RAG Document Evaluation Checklist

- [ ] FileName이 명확한가?
- [ ] Document Title이 명확한가?
- [ ] Required Section이 포함되었는가?
- [ ] `[개념]`이 포함되었는가?
- [ ] `[핵심]`이 포함되었는가?
- [ ] `[실무]`가 포함되었는가?
- [ ] `[FAQ]`가 포함되었는가?
- [ ] Retrieval Queries가 포함되었는가?
- [ ] FAQ가 Q/A 형식인가?
- [ ] Retrieval Queries가 사용자 검색 표현을 포함하는가?
- [ ] Domain 용어가 통일되었는가?
- [ ] Chunk가 독립적으로 검색 가능한가?
- [ ] Master Rules와 Domain Rules가 반영되었는가?
- [ ] 중복과 오타가 과도하지 않은가?
```

RAG Document Score 예시:

```json
{
  "document": "Multi_Agent_System_Part13_Evaluation_Quality_Control.md",
  "requiredStructure": 1.0,
  "faqQuality": 0.9,
  "retrievalQueriesQuality": 0.9,
  "terminologyConsistency": 0.95,
  "chunkIndependence": 0.85,
  "domainRuleCompliance": 0.95,
  "overallQuality": 0.93,
  "decision": "pass"
}
```

---

### [FAQ]

Q. RAG Document Quality Evaluation이 뭐야?
A. RAG 문서가 AI Agent Retrieval에 적합한 구조와 내용을 갖추었는지 평가하는 과정이다.

Q. RAG 문서 평가에서 가장 중요한 것은?
A. Required Section, FAQ, Retrieval Queries, 용어 통일, Chunk 독립성이다.

Q. RAG 문서는 사람용 설명이 길수록 좋아?
A. 아니다. Agent Retrieval에 필요한 구조화된 정보와 검색 가능한 FAQ가 중요하다.

Q. RAG 문서 품질이 낮으면 어떻게 해?
A. Documentation Agent 또는 Fix Agent가 구조, FAQ, Retrieval Queries, 용어를 보강해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Evaluation이 뭐야?
A. Multi-Agent System에서 Agent Output, Handoff, Workflow, RAG Retrieval, Review-Fix 품질을 측정하고 개선하는 과정이다.

Q. Multi-Agent Evaluation은 무엇을 평가해?
A. PM Agent, Specialist Agent, Review Agent, Fix Agent, RAG Retrieval, Shared State, Tool Permission, Final Output을 평가한다.

Q. Evaluation 결과는 어디에 사용해?
A. Agent Role 수정, Handoff Template 개선, RAG Scope 조정, Review Criteria 보강, Workflow Pattern 개선에 사용한다.

Q. Agent Output Quality가 뭐야?
A. Agent가 Handoff, Requirements, Constraints, Scope, Done Criteria에 맞는 산출물을 만들었는지 평가하는 기준이다.

Q. 좋은 Agent Output은 어떤 형태야?
A. 요구사항을 충족하고, 구조화되어 있으며, Decisions, Assumptions, Risks, Open Questions를 포함한다.

Q. Requirement Coverage Evaluation이 뭐야?
A. Agent Output이 사용자 요청과 Handoff 요구사항을 얼마나 충족했는지 평가하는 과정이다.

Q. Requirement Coverage가 낮으면 어떻게 해?
A. Review Finding을 만들고 Fix Agent가 누락된 요구사항을 반영해야 한다.

Q. Scope Compliance Evaluation이 뭐야?
A. Agent가 자기 Role과 Scope 안에서 작업했는지 평가하는 과정이다.

Q. Agent가 Scope 밖 작업을 하면 왜 문제야?
A. 역할 충돌, 잘못된 Output, Tool Permission 위반, Workflow 혼선이 생길 수 있다.

Q. Handoff Quality Evaluation이 뭐야?
A. Source Agent가 Target Agent에게 전달한 Handoff가 작업 수행에 충분한지 평가하는 과정이다.

Q. 좋은 Handoff 기준은?
A. Task, Requirements, Constraints, Context, RAG Scope, Tool Permission, Expected Output, Done Criteria가 명확해야 한다.

Q. Handoff Failure Evaluation이 뭐야?
A. Agent Output 실패가 Handoff 문제에서 비롯되었는지 평가하는 과정이다.

Q. Agent Output이 나쁘면 항상 Agent 잘못이야?
A. 아니다. Handoff에 요구사항, 제약, Context가 부족했을 수 있다.

Q. Retrieval Relevance Evaluation이 뭐야?
A. RAG 검색 결과가 현재 Task와 얼마나 관련 있는지 평가하는 과정이다.

Q. 검색 결과가 많으면 좋은 거야?
A. 아니다. 관련 없는 검색 결과가 많으면 Agent가 잘못된 Context를 사용할 수 있다.

Q. Retrieval Sufficiency Evaluation이 뭐야?
A. 검색된 RAG Context가 현재 Task를 수행하기에 충분한지 평가하는 과정이다.

Q. Relevance와 Sufficiency는 달라?
A. 다르다. Relevance는 관련성이고 Sufficiency는 작업 수행에 필요한 정보가 충분한지이다.

Q. Retrieval Precision이 뭐야?
A. 검색된 Context 중 실제로 유용한 Context의 비율이다.

Q. Retrieval Recall이 뭐야?
A. 필요한 Context 중 실제로 검색된 Context의 비율이다.

Q. Precision이 낮으면 어떻게 해?
A. Query Narrowing으로 검색 범위를 좁힌다.

Q. Recall이 낮으면 어떻게 해?
A. Query Expansion 또는 RAG Scope 확장으로 필요한 문서를 더 검색한다.

Q. Review Quality Evaluation이 뭐야?
A. Review Agent의 Review Findings와 Review Report가 기준, 근거, 수정 방향을 갖추었는지 평가하는 과정이다.

Q. 좋은 Review Finding에는 뭐가 있어야 해?
A. Severity, Category, Issue, Evidence, Impact, Fix Direction이 있어야 한다.

Q. Review Accuracy Evaluation이 뭐야?
A. Review Agent가 실제 문제를 정확히 찾고 잘못된 지적을 줄였는지 평가하는 과정이다.

Q. False Positive가 뭐야?
A. 문제가 아닌 것을 문제로 잘못 지적한 것이다.

Q. False Negative가 뭐야?
A. 실제 문제를 놓친 것이다.

Q. Fix Quality Evaluation이 뭐야?
A. Fix Agent가 Review Findings를 정확히 반영하고 기존 요구사항을 보존했는지 평가하는 과정이다.

Q. Fix가 성공했다는 기준은?
A. Critical / Major Findings가 해결되고 기존 요구사항이 보존되며 Regression Risk가 표시된 상태다.

Q. Regression Evaluation이 뭐야?
A. Fix가 기존 요구사항, 기능, API Contract, 문서 구조에 부정적 영향을 주었는지 평가하는 과정이다.

Q. Fix가 Finding을 해결했는데 기존 기능이 깨지면 성공이야?
A. 아니다. Regression이 발생한 것이므로 다시 수정해야 한다.

Q. Workflow Quality Evaluation이 뭐야?
A. Multi-Agent Workflow 전체가 적절한 Pattern으로 실행되고 각 Step이 안정적으로 연결되었는지 평가하는 과정이다.

Q. Workflow 품질은 개별 Agent Output만 보면 돼?
A. 아니다. Routing, Handoff, Shared State, Review-Fix, Tool Permission, Final Output을 함께 봐야 한다.

Q. Workflow Metrics가 뭐야?
A. Multi-Agent Workflow 품질을 수치 또는 상태로 평가하기 위한 지표다.

Q. 중요한 Workflow Metrics는?
A. Routing Accuracy, Handoff Completeness, Requirement Coverage, Retrieval Relevance, Review Quality, Fix Success Rate, Tool Permission Compliance다.

Q. Quality Gate가 뭐야?
A. 다음 Workflow Step으로 넘어가기 전에 충족해야 하는 품질 기준이다.

Q. Quality Gate에서 Fail이면 어떻게 해?
A. Fix, Re-run, Plan Revision, PM Decision, 사용자 확인 중 하나로 처리한다.

Q. Continuous Improvement가 뭐야?
A. Evaluation 결과를 바탕으로 Agent Definition, Handoff, RAG Scope, Review Criteria, Workflow Pattern을 지속적으로 개선하는 과정이다.

Q. 반복 실패가 발생하면 무엇을 봐야 해?
A. Root Cause가 Agent 자체인지, Handoff인지, RAG Scope인지, Review 기준인지 확인해야 한다.

Q. RAG Document Quality Evaluation이 뭐야?
A. RAG 문서가 AI Agent Retrieval에 적합한 구조와 내용을 갖추었는지 평가하는 과정이다.

Q. RAG 문서 평가에서 가장 중요한 것은?
A. Required Section, FAQ, Retrieval Queries, 용어 통일, Chunk 독립성이다.

Q. 개인 AI 개발팀에서 초기 Evaluation은 무엇부터 하면 돼?
A. Handoff Completeness, Requirement Coverage, Review Finding Quality, Fix Success 여부부터 평가하면 된다.

Q. 개인 AI 개발팀에서 Evaluation 결과는 어떻게 활용해?
A. PM Agent Handoff Template, Specialist Agent Scope, Review Checklist, RAG Scope, Workflow Pattern을 개선하는 데 활용한다.
