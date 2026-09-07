# Agent Memory & State Management Part05 - State Schema, State Update & State Compression

---

# 1. State Schema Foundation

## 1.1 State Schema 기본 개념

### [개념]

State Schema는 Agent State에 어떤 필드가 있고, 각 필드가 어떤 타입과 규칙을 가지는지 정의한 구조이다.

State Schema는 Multi-Agent Workflow에서 Agent 간 상태 형식 불일치를 줄인다.

```text
State Schema = Agent State의 필드, 타입, 규칙 정의
```

State Schema가 없으면 Agent마다 다른 필드명, 다른 타입, 다른 상태 값을 사용해 Workflow가 불안정해진다.

기본 구성:

```text
Field Name
Type
Required / Optional
Default Value
Update Rule
Owner Agent
Validation Rule
```

---

### [핵심]

- State Schema는 Agent State의 구조를 정의한다.
- 필드명과 타입을 명확히 한다.
- Required와 Optional 필드를 구분한다.
- Default Value를 지정할 수 있다.
- Update Rule을 정의한다.
- Owner Agent를 지정한다.
- Validation Rule을 포함한다.
- State Schema는 Agent 간 Handoff 안정성을 높인다.
- Schema가 너무 복잡하면 유지보수가 어려워진다.

---

### [실무]

2026 실무 기준 Multi-Agent System에서는 자유 텍스트 State보다 구조화된 Schema를 우선한다.

권장 State Schema 예시:

```json
{
  "workflowId": "string",
  "userRequest": "string",
  "currentTask": "string",
  "currentStep": "string",
  "status": "planned | in_progress | review | fix | completed | failed",
  "requirements": ["string"],
  "constraints": ["string"],
  "decisions": [
    {
      "decision": "string",
      "reason": "string",
      "status": "active | deprecated | draft"
    }
  ],
  "assumptions": ["string"],
  "agentOutputs": {
    "pmAgent": {},
    "domainAgent": {},
    "reviewAgent": {},
    "fixAgent": {}
  },
  "reviewFindings": [
    {
      "id": "string",
      "issue": "string",
      "severity": "low | medium | high | critical",
      "status": "open | fixed | accepted"
    }
  ],
  "errors": [
    {
      "step": "string",
      "message": "string",
      "status": "resolved | unresolved"
    }
  ],
  "nextAction": "string"
}
```

State Schema는 현재 Workflow에 필요한 만큼만 정의한다.

모든 프로젝트에서 거대한 Schema를 강제하지 않는다.

---

### [FAQ]

Q. State Schema가 뭐야?
A. Agent State에 어떤 필드가 있고 각 필드가 어떤 타입과 업데이트 규칙을 가지는지 정의한 구조다.

Q. State Schema는 왜 필요해?
A. Agent 간 상태 형식 불일치와 필드 누락을 줄여 Workflow 안정성을 높이기 위해 필요하다.

Q. State Schema에는 무엇을 정의해?
A. Field Name, Type, Required 여부, Default Value, Update Rule, Owner Agent, Validation Rule을 정의한다.

Q. 자유 텍스트 State만 써도 돼?
A. 간단한 작업은 가능하지만 Multi-Agent Workflow에서는 후속 처리와 검증이 어려워진다.

Q. State Schema가 너무 복잡하면?
A. 유지보수가 어려워지고 Agent가 불필요한 필드를 채우느라 Context를 낭비할 수 있다.

---

# 2. Core State Fields

## 2.1 핵심 State 필드 정의

### [개념]

Core State Fields는 대부분의 Agent Workflow에서 공통으로 필요한 필드이다.

이 필드는 현재 작업 진행, 요구사항 유지, Agent Handoff, Review/Fix Loop에 사용된다.

```text
Core State Fields = 대부분의 Workflow에서 필요한 기본 상태 필드
```

---

### [핵심]

Core State Fields:

- workflowId
- userRequest
- currentTask
- currentStep
- status
- requirements
- constraints
- decisions
- assumptions
- agentOutputs
- toolResults
- reviewFindings
- errors
- nextAction

필드 기준:

| Field          | 목적           | Required | Update 방식      |
| -------------- | -------------- | -------: | ---------------- |
| workflowId     | Workflow 식별  |      Yes | Replace 금지     |
| userRequest    | 원본 요청      |      Yes | Replace 금지     |
| currentTask    | 현재 작업      |      Yes | Replace          |
| currentStep    | 현재 단계      |      Yes | Replace          |
| status         | 진행 상태      |      Yes | Replace          |
| requirements   | 요구사항       |      Yes | Merge            |
| constraints    | 제약사항       |      Yes | Merge            |
| decisions      | 결정 사항      | Optional | Versioned Update |
| assumptions    | 가정           | Optional | Append           |
| agentOutputs   | Agent 결과     | Optional | Owner Replace    |
| toolResults    | Tool 결과 요약 | Optional | Append / Replace |
| reviewFindings | 검토 결과      | Optional | Append           |
| errors         | 오류           | Optional | Append           |
| nextAction     | 다음 작업      | Optional | Replace          |

---

### [실무]

RAG 문서 제작 State 예시:

```json
{
  "workflowId": "rag-doc-agent-memory-state-management",
  "userRequest": "Agent Memory State Management Part05 작업",
  "currentTask": "Part05 State Schema, Update, Compression 작성",
  "currentStep": "final_output",
  "status": "completed",
  "requirements": [
    "MASTER_RAG_RULES 적용",
    "DOMAIN_RULES 적용",
    "FAQ 강화",
    "Retrieval Queries 포함"
  ],
  "constraints": [
    "writing block document 출력",
    "중간 응답 금지",
    "사람용 문서보다 Retrieval 최적화 우선"
  ],
  "decisions": [
    {
      "decision": "Part05는 State Schema, State Update, State Compression 중심으로 작성",
      "reason": "Domain Rules의 State Schema Rules, State Update Rules, State Compression Rules를 반영",
      "status": "active"
    }
  ],
  "reviewFindings": [],
  "errors": [],
  "nextAction": "Part06 Memory Retrieval, Update, Validation 작성"
}
```

Core State Fields는 PM Agent와 Review Agent가 검증하기 쉬운 형태로 유지한다.

---

### [FAQ]

Q. Core State Fields는 뭐야?
A. 대부분의 Agent Workflow에서 공통으로 필요한 기본 상태 필드다.

Q. Agent State에 꼭 필요한 필드는?
A. workflowId, userRequest, currentTask, currentStep, status, requirements, constraints, nextAction이 핵심이다.

Q. reviewFindings는 필수야?
A. Review/Fix Loop가 있는 Workflow에서는 중요하지만 단순 작업에서는 optional로 둘 수 있다.

Q. userRequest는 왜 Replace 금지야?
A. 원본 요청은 최종 검수 기준이므로 임의로 덮어쓰면 안 된다.

Q. requirements와 constraints는 어떻게 업데이트해?
A. 기존 값을 지우지 않고 Merge 방식으로 누락 없이 갱신한다.

---

# 3. Required vs Optional State

## 3.1 필수 필드와 선택 필드 구분

### [개념]

State Schema에서는 Required Field와 Optional Field를 구분해야 한다.

Required Field는 Workflow 진행에 반드시 필요한 필드이다.

Optional Field는 작업 유형에 따라 필요한 경우에만 사용하는 필드이다.

```text
Required Field = 없으면 Workflow가 깨지는 필드
Optional Field = 작업 유형에 따라 사용하는 필드
```

---

### [핵심]

Required Field 후보:

- workflowId
- userRequest
- currentTask
- currentStep
- status
- requirements
- constraints

Optional Field 후보:

- decisions
- assumptions
- agentOutputs
- toolResults
- reviewFindings
- errors
- apiContract
- memoryUpdateCandidates
- checkpointId
- rollbackTarget

구분 기준:

- 없으면 다음 Agent가 작업을 이어갈 수 없는가?
- 없으면 최종 검수 기준이 사라지는가?
- 없으면 현재 단계 판단이 불가능한가?
- 특정 Domain 작업에서만 필요한가?
- Review/Fix Loop 여부에 따라 필요한가?

---

### [실무]

단순 RAG 문서 작성 Required State:

```json
{
  "workflowId": "string",
  "userRequest": "string",
  "currentTask": "string",
  "currentStep": "string",
  "status": "string",
  "requirements": [],
  "constraints": []
}
```

Backend / Frontend 연동 작업 Optional 확장:

```json
{
  "apiContract": {
    "endpoint": "string",
    "method": "GET | POST | PUT | PATCH | DELETE",
    "request": {},
    "response": {},
    "authRequired": true
  },
  "integrationIssues": [],
  "crossDomainReview": {}
}
```

위험 작업 Optional 확장:

```json
{
  "checkpointId": "string",
  "rollbackTarget": "string",
  "sideEffects": [],
  "userApprovalRequired": true
}
```

State는 작업 유형에 맞게 확장한다.

모든 Optional Field를 항상 채우지 않는다.

---

### [FAQ]

Q. Required Field와 Optional Field 차이는?
A. Required Field는 없으면 Workflow가 깨지는 필드이고 Optional Field는 작업 유형에 따라 사용하는 필드다.

Q. Required Field는 어떻게 정해?
A. 다음 Agent가 작업을 이어가는 데 반드시 필요한 정보인지 기준으로 정한다.

Q. Optional Field를 많이 넣으면 좋아?
A. 아니다. 불필요한 필드가 많으면 State가 커지고 유지보수가 어려워진다.

Q. apiContract는 Required야?
A. Backend / Frontend 연동 작업에서는 중요하지만 RAG 문서 작성에서는 optional이다.

Q. checkpointId는 언제 필요해?
A. 긴 Workflow, 위험 작업, Resume/Rollback이 필요한 작업에서 필요하다.

---

# 4. State Status Enum

## 4.1 Status 값 표준화

### [개념]

State Status Enum은 Workflow 진행 상태를 표준화한 값이다.

Status 값이 통일되지 않으면 Agent마다 완료, 진행, 실패 상태를 다르게 해석한다.

```text
State Status Enum = Workflow 진행 상태 표준값
```

---

### [핵심]

권장 Status Enum:

```text
planned
in_progress
waiting
review
fix
blocked
completed
failed
cancelled
```

Status 의미:

| Status      | 의미                          |
| ----------- | ----------------------------- |
| planned     | 작업 계획됨                   |
| in_progress | 작업 진행 중                  |
| waiting     | 외부 입력 또는 Tool 결과 대기 |
| review      | 검토 중                       |
| fix         | 수정 중                       |
| blocked     | 진행 차단                     |
| completed   | 완료                          |
| failed      | 실패                          |
| cancelled   | 취소                          |

주의:

- done, complete, finished를 혼용하지 않는다.
- error, failed, blocked를 구분한다.
- waiting과 blocked를 구분한다.
- completed는 Final State 검증 후 사용한다.

---

### [실무]

상태 전이 예시:

```text
planned
→ in_progress
→ review
→ fix
→ review
→ completed
```

오류 발생 상태 전이:

```text
in_progress
→ blocked
→ fix
→ review
→ completed
```

실패 종료 상태 전이:

```text
in_progress
→ failed
```

Status Update 예시:

```json
{
  "currentStep": "retrieval_queries_review",
  "status": "review",
  "nextAction": "fix_duplicate_faq_queries"
}
```

Status는 Replace 방식으로 갱신한다.

---

### [FAQ]

Q. State Status Enum이 뭐야?
A. Workflow 진행 상태를 Agent들이 동일하게 해석하도록 만든 표준 상태 값이다.

Q. 권장 Status 값은?
A. planned, in_progress, waiting, review, fix, blocked, completed, failed, cancelled를 사용한다.

Q. blocked와 failed 차이는?
A. blocked는 해결하면 진행 가능한 차단 상태이고 failed는 작업이 실패로 종료된 상태다.

Q. waiting과 blocked 차이는?
A. waiting은 외부 입력이나 결과를 기다리는 상태이고 blocked는 진행을 막는 문제가 있는 상태다.

Q. completed는 언제 사용해?
A. Final State 검증까지 통과한 뒤 사용한다.

---

# 5. State Update Foundation

## 5.1 State Update 기본 개념

### [개념]

State Update는 Agent Workflow 진행 중 State 필드를 갱신하는 과정이다.

State Update는 모든 필드를 덮어쓰는 방식이 아니다.

필드 성격에 따라 Append, Replace, Merge, Versioned Update를 구분해야 한다.

```text
State Update = Workflow 중 State 필드 갱신
```

---

### [핵심]

State Update 방식:

| Update 방식      | 용도                              |
| ---------------- | --------------------------------- |
| Append           | Review Findings, Logs, Errors     |
| Replace          | Current Step, Status, Next Action |
| Merge            | Requirements, Constraints         |
| Versioned Update | Project Decision, API Contract    |
| Owner Replace    | Agent별 Output                    |
| Ignore           | 무관한 Update 요청                |

원칙:

- 모든 Update가 덮어쓰기는 아니다.
- Review 결과는 Append가 적합하다.
- 현재 단계와 상태는 Replace가 적합하다.
- 요구사항과 제약은 Merge가 적합하다.
- 중요한 결정은 Versioned Update가 적합하다.
- 업데이트 후 Validation이 필요하다.

---

### [실무]

Append 예시:

```json
{
  "reviewFindings": [
    {
      "id": "RF-001",
      "issue": "FAQ 누락",
      "severity": "medium",
      "status": "open"
    }
  ]
}
```

Replace 예시:

```json
{
  "currentStep": "final_review",
  "status": "review",
  "nextAction": "validate_retrieval_queries"
}
```

Merge 예시:

```json
{
  "requirements": [
    "MASTER_RAG_RULES 적용",
    "DOMAIN_RULES 적용",
    "Retrieval Queries 포함"
  ]
}
```

Versioned Update 예시:

```json
{
  "decisions": [
    {
      "version": 1,
      "decision": "FAQ는 각 Section마다 포함한다.",
      "status": "deprecated"
    },
    {
      "version": 2,
      "decision": "FAQ는 각 주요 Section에 포함하고 Retrieval Queries에 통합 FAQ를 강화한다.",
      "status": "active"
    }
  ]
}
```

---

### [FAQ]

Q. State Update가 뭐야?
A. Agent Workflow 진행 중 currentStep, requirements, reviewFindings 같은 State 필드를 갱신하는 과정이다.

Q. State Update는 전부 덮어쓰기야?
A. 아니다. 필드 성격에 따라 Append, Replace, Merge, Versioned Update를 구분해야 한다.

Q. Append는 언제 써?
A. Review Findings, Errors, Logs처럼 누적되어야 하는 정보에 사용한다.

Q. Replace는 언제 써?
A. currentStep, status, nextAction처럼 현재 값 하나만 의미 있는 필드에 사용한다.

Q. Versioned Update는 언제 써?
A. 결정 사항, API 계약, 프로젝트 정책처럼 변경 이력이 중요한 필드에 사용한다.

---

# 6. Append Update Rules

## 6.1 Append 방식 적용 기준

### [개념]

Append Update는 기존 값을 지우지 않고 새 항목을 뒤에 추가하는 방식이다.

Append는 변경 이력과 누적 기록이 중요한 필드에 사용한다.

```text
Append Update = 기존 값 보존 + 새 항목 추가
```

---

### [핵심]

Append 적합 필드:

- reviewFindings
- errors
- logs
- warnings
- auditTrail
- appliedFixes
- checkpoints
- conversationEvents

Append 규칙:

- 기존 항목을 삭제하지 않는다.
- 각 항목에 id를 부여한다.
- severity, status, createdAt을 포함할 수 있다.
- 해결된 항목은 삭제하지 않고 status를 fixed로 변경한다.
- 중복 항목은 병합하거나 linkedIssue로 연결한다.

---

### [실무]

Review Findings Append 예시:

```json
{
  "reviewFindings": [
    {
      "id": "RF-001",
      "issue": "Retrieval Queries 부족",
      "severity": "medium",
      "status": "open",
      "createdAt": "2026-07-01"
    },
    {
      "id": "RF-002",
      "issue": "State Update 방식 설명 누락",
      "severity": "high",
      "status": "open",
      "createdAt": "2026-07-01"
    }
  ]
}
```

Fix 후 Append 예시:

```json
{
  "appliedFixes": [
    {
      "findingId": "RF-001",
      "fix": "Retrieval Queries FAQ 항목 추가",
      "status": "applied"
    }
  ],
  "reviewFindings": [
    {
      "id": "RF-001",
      "issue": "Retrieval Queries 부족",
      "severity": "medium",
      "status": "fixed"
    }
  ]
}
```

Review Findings를 삭제하면 Fix Loop 추적이 어려워진다.

---

### [FAQ]

Q. Append Update는 뭐야?
A. 기존 값을 지우지 않고 새 항목을 추가하는 State Update 방식이다.

Q. Append는 어디에 사용해?
A. reviewFindings, errors, logs, appliedFixes처럼 누적 기록이 필요한 필드에 사용한다.

Q. 해결된 Review Finding은 삭제해도 돼?
A. 삭제하지 않고 status를 fixed로 변경하는 것이 좋다.

Q. Append 항목에는 무엇을 넣어?
A. id, 내용, severity, status, createdAt, 관련 findingId를 넣을 수 있다.

Q. Append의 장점은?
A. 변경 이력과 문제 해결 과정을 추적할 수 있다.

---

# 7. Replace Update Rules

## 7.1 Replace 방식 적용 기준

### [개념]

Replace Update는 기존 값을 새 값으로 교체하는 방식이다.

Replace는 현재 값 하나만 의미 있는 필드에 사용한다.

```text
Replace Update = 기존 값 교체
```

---

### [핵심]

Replace 적합 필드:

- currentStep
- status
- nextAction
- currentTask
- finalOutput
- reviewPassStatus
- completionStatus

Replace 규칙:

- 이전 값이 필요하면 history에 별도 기록한다.
- userRequest 원본은 Replace하지 않는다.
- finalOutput은 PM Agent 또는 Finalizer가 교체한다.
- status는 표준 Enum으로만 교체한다.
- Replace 후 State Validation을 수행한다.

---

### [실무]

currentStep Replace 예시:

```json
{
  "before": {
    "currentStep": "draft_generation",
    "status": "in_progress"
  },
  "after": {
    "currentStep": "final_review",
    "status": "review"
  }
}
```

nextAction Replace 예시:

```json
{
  "nextAction": "generate_final_output"
}
```

주의 예시:

```text
금지:
userRequest를 요약문으로 Replace

허용:
userRequest 원본 보존
requestSummary 별도 추가
```

userRequest는 최종 검수 기준이므로 원본을 유지한다.

---

### [FAQ]

Q. Replace Update는 뭐야?
A. 기존 값을 새 값으로 교체하는 State Update 방식이다.

Q. Replace는 어디에 사용해?
A. currentStep, status, nextAction처럼 현재 값 하나만 의미 있는 필드에 사용한다.

Q. userRequest도 Replace해도 돼?
A. 아니다. 원본 사용자 요청은 최종 검수 기준이므로 보존해야 한다.

Q. 이전 currentStep 이력은 어떻게 보관해?
A. stepHistory 같은 별도 Append 필드에 기록할 수 있다.

Q. Replace 후 무엇을 해야 해?
A. Status 값, nextAction, 필수 필드 누락 여부를 검증해야 한다.

---

# 8. Merge Update Rules

## 8.1 Merge 방식 적용 기준

### [개념]

Merge Update는 기존 값과 새 값을 합치고 중복을 정리하는 방식이다.

Merge는 요구사항, 제약, 태그, 참조 문서처럼 누락 없이 유지해야 하는 목록에 사용한다.

```text
Merge Update = 기존 값 + 새 값 병합
```

---

### [핵심]

Merge 적합 필드:

- requirements
- constraints
- referenceDocuments
- retrievalKeywords
- assignedAgents
- validationCriteria
- allowedDomains

Merge 규칙:

- 기존 값을 보존한다.
- 새 값을 추가한다.
- 중복을 제거한다.
- 충돌 항목은 자동 병합하지 않고 Conflict로 분리한다.
- 최신 사용자 요청에서 추가된 제약은 우선 반영한다.

---

### [실무]

Requirements Merge 예시:

```json
{
  "before": ["MASTER_RAG_RULES 적용", "FAQ 포함"],
  "incoming": ["DOMAIN_RULES 적용", "FAQ 포함", "Retrieval Queries 포함"],
  "after": [
    "MASTER_RAG_RULES 적용",
    "DOMAIN_RULES 적용",
    "FAQ 포함",
    "Retrieval Queries 포함"
  ]
}
```

Constraints Conflict 예시:

```json
{
  "before": ["간단히 출력"],
  "incoming": ["상세 문서로 출력"],
  "conflict": {
    "field": "constraints",
    "old": "간단히 출력",
    "new": "상세 문서로 출력",
    "resolution": "Current User Request 우선"
  }
}
```

Merge는 단순 결합이 아니다.

충돌이 있으면 우선순위 규칙으로 해결한다.

---

### [FAQ]

Q. Merge Update는 뭐야?
A. 기존 값과 새 값을 합치고 중복을 정리하는 State Update 방식이다.

Q. Merge는 어디에 사용해?
A. requirements, constraints, referenceDocuments, validationCriteria처럼 누락되면 안 되는 목록에 사용한다.

Q. Merge와 Append 차이는?
A. Append는 단순 누적이고 Merge는 중복 제거와 충돌 확인을 포함한다.

Q. 충돌하는 constraints는 어떻게 해?
A. 자동으로 섞지 않고 Current User Request 우선순위에 따라 해결한다.

Q. Merge 후 검증할 것은?
A. 중복 제거, 누락 여부, 충돌 여부, 최신 요청 반영 여부를 확인한다.

---

# 9. Versioned Update Rules

## 9.1 Versioned Update 적용 기준

### [개념]

Versioned Update는 중요한 결정이나 계약이 변경될 때 이전 값을 보존하고 새 버전을 활성화하는 방식이다.

Versioned Update는 변경 이력이 중요한 필드에 사용한다.

```text
Versioned Update = 변경 이력 보존 + 최신 버전 활성화
```

---

### [핵심]

Versioned Update 적합 필드:

- decisions
- apiContract
- architectureDecision
- projectPolicy
- outputFormatPolicy
- memoryPolicy
- securityPolicy

Versioned Update 규칙:

- 이전 버전을 삭제하지 않는다.
- 새 버전에 version 값을 부여한다.
- active, deprecated, draft 상태를 구분한다.
- 변경 이유를 기록한다.
- 적용 범위를 기록한다.
- 최신 active 버전을 우선한다.

---

### [실무]

Decision Versioned Update 예시:

```json
{
  "decisions": [
    {
      "version": 1,
      "decision": "Agent와 RAG 문서를 같은 폴더에서 관리한다.",
      "reason": "초기 단순 구조",
      "status": "deprecated",
      "date": "2026-06-20"
    },
    {
      "version": 2,
      "decision": "Agent와 RAG 문서는 역할이 다르므로 분리해서 관리한다.",
      "reason": "실행 구조와 검색 문서의 목적이 다르기 때문",
      "status": "active",
      "date": "2026-07-01"
    }
  ]
}
```

API Contract Versioned Update 예시:

```json
{
  "apiContract": [
    {
      "version": 1,
      "endpoint": "GET /festival/detail/{id}",
      "response": "FestivalDetailDto",
      "status": "deprecated"
    },
    {
      "version": 2,
      "endpoint": "GET /festival/detail/{id}",
      "response": "ApiResponse<FestivalDetailDto>",
      "status": "active"
    }
  ]
}
```

Versioned Update는 Review Agent가 변경 이유를 추적하는 데 유용하다.

---

### [FAQ]

Q. Versioned Update는 뭐야?
A. 중요한 결정이나 계약이 변경될 때 이전 값을 보존하고 새 버전을 활성화하는 Update 방식이다.

Q. Versioned Update는 어디에 사용해?
A. decisions, apiContract, architectureDecision, projectPolicy처럼 변경 이력이 중요한 필드에 사용한다.

Q. 이전 버전은 삭제해도 돼?
A. 삭제하지 않고 deprecated 상태로 남기는 것이 좋다.

Q. 최신 값은 어떻게 판단해?
A. status가 active인 최신 version을 우선한다.

Q. Versioned Update의 장점은?
A. 결정 변경 이력과 이유를 추적할 수 있어 Review와 Rollback이 쉬워진다.

---

# 10. State Validation

## 10.1 State Update 후 검증

### [개념]

State Validation은 State Update 후 상태가 Schema와 Workflow 규칙을 만족하는지 확인하는 과정이다.

State Validation이 없으면 필드 누락, 타입 오류, 상태 충돌, Agent 간 불일치가 누적된다.

```text
State Validation = State Update 후 유효성 검증
```

---

### [핵심]

State Validation 기준:

- Required Field 존재 여부
- Field Type 일치 여부
- Status Enum 유효성
- Current Step과 Status 일관성
- Requirements 누락 여부
- Constraints 충돌 여부
- Owner Agent 권한 위반 여부
- Review Findings 상태 일관성
- Final Output 준비 여부
- 민감정보 포함 여부

검증 Flow:

```text
State Update
→ Schema Validation
→ Conflict Check
→ Ownership Check
→ Safety Check
→ Pass / Fix / Rollback
```

---

### [실무]

Validation Checklist:

```md
### [Checklist]

- [ ] workflowId가 존재하는가?
- [ ] userRequest 원본이 보존되었는가?
- [ ] currentStep과 status가 일치하는가?
- [ ] status가 표준 Enum인가?
- [ ] requirements가 누락되지 않았는가?
- [ ] constraints가 현재 요청과 충돌하지 않는가?
- [ ] reviewFindings가 삭제되지 않았는가?
- [ ] decisions의 active 버전이 명확한가?
- [ ] Agent가 수정 권한 없는 필드를 변경하지 않았는가?
- [ ] 민감정보가 State에 포함되지 않았는가?
```

Validation 실패 처리:

```text
Minor Issue → Fix State
Schema Error → Correct Field
Conflict → Apply Priority Rule
Unauthorized Update → Reject Update
Critical Corruption → Rollback
```

---

### [FAQ]

Q. State Validation이 뭐야?
A. State Update 후 상태가 Schema와 Workflow 규칙을 만족하는지 확인하는 과정이다.

Q. State Validation은 언제 해?
A. 중요한 State Update 후, Agent Handoff 전, Review 전, Final Output 전에 수행한다.

Q. State Validation에서 무엇을 확인해?
A. 필수 필드, 타입, Status Enum, 요구사항 누락, 제약 충돌, 수정 권한, 민감정보 여부를 확인한다.

Q. Validation 실패하면 어떻게 해?
A. 사소한 문제는 Fix하고, 심각한 State 오염은 Rollback한다.

Q. State Validation의 핵심은?
A. 잘못된 상태가 다음 Agent나 Final Output으로 전달되지 않게 막는 것이다.

---

# 11. State Compression Foundation

## 11.1 State Compression 기본 개념

### [개념]

State Compression은 State가 길어졌을 때 현재 작업에 필요한 핵심 정보만 남기고 압축하는 과정이다.

State Compression은 Context Window 낭비를 줄이고 Agent 응답 품질을 유지한다.

```text
State Compression = 긴 State를 핵심 정보 중심으로 압축
```

기본 Flow:

```text
Large State
→ Extract Requirements
→ Extract Decisions
→ Extract Open Issues
→ Summarize Completed Steps
→ Keep Active Context
→ Archive or Drop Temporary Data
```

---

### [핵심]

State Compression 포함 대상:

- Summarization
- Key Decision Extraction
- Completed Step Compression
- Error Summary
- Open Issue Summary
- Token Budget
- Tool Result Summary
- Final Relevant Context

Compression 원칙:

- 완료된 단계는 요약한다.
- 현재 작업에 필요한 정보는 유지한다.
- 결정 사항과 제약은 누락하지 않는다.
- 열린 이슈와 오류는 유지한다.
- Tool Result는 필요한 필드만 보존한다.
- 임시 추론과 후보안은 제거한다.
- 압축 후 Validation을 수행한다.

---

### [실무]

압축 전 State 예시:

```text
- Part01 작성 과정 전체
- Part02 작성 과정 전체
- Part03 작성 과정 전체
- Part04 작성 과정 전체
- 각 Part별 초안 후보
- Review 중간 메모
- 수정 로그 전체
- 최종 결정 사항
- 다음 작업
```

압축 후 State 예시:

```json
{
  "completedStepsSummary": [
    "Part01 State vs Memory Foundation 완료",
    "Part02 Memory Types 완료",
    "Part03 Shared State & Multi-Agent State 완료",
    "Part04 Checkpoint, Resume & Rollback 완료"
  ],
  "activeRequirements": [
    "MASTER_RAG_RULES 적용",
    "DOMAIN_RULES 적용",
    "FAQ 강화",
    "Retrieval Queries 포함"
  ],
  "activeDecisions": [
    "문서는 RAG Retrieval 최적화 구조로 작성",
    "출력은 writing block document 형식 유지"
  ],
  "openIssues": [],
  "nextAction": "Part05 State Schema, State Update, State Compression 완료 후 Part06 진행"
}
```

Compression은 삭제가 아니라 현재 작업에 맞춘 요약과 정리이다.

---

### [FAQ]

Q. State Compression이 뭐야?
A. State가 길어졌을 때 현재 작업에 필요한 핵심 정보만 남기고 압축하는 과정이다.

Q. State Compression은 왜 필요해?
A. Context Window 낭비를 줄이고 Agent 응답 품질을 유지하기 위해 필요하다.

Q. 무엇을 압축해?
A. 완료된 단계, 긴 Tool Result, 오래된 중간 메모, 반복 로그를 요약한다.

Q. 압축하면 안 되는 것은?
A. 현재 요구사항, 핵심 제약, 확정 결정, 열린 이슈, 미해결 오류는 누락하면 안 된다.

Q. Compression 후 무엇을 해야 해?
A. 압축된 State가 요구사항과 결정을 누락하지 않았는지 Validation해야 한다.

---

# 12. State Compression Rules

## 12.1 압축 기준과 유지 기준

### [개념]

State Compression Rules는 어떤 정보를 유지하고 어떤 정보를 요약하거나 제거할지 정하는 기준이다.

압축 기준이 없으면 중요한 제약이 사라지거나 불필요한 정보가 계속 누적된다.

```text
Compression Rules = State 압축 시 유지 / 요약 / 제거 기준
```

---

### [핵심]

반드시 유지:

- Current User Request
- Active Requirements
- Active Constraints
- Active Decisions
- Current Step
- Current Status
- Open Issues
- Unresolved Errors
- Next Action
- Review Findings not fixed

요약 가능:

- Completed Steps
- Resolved Errors
- Old Review Logs
- Tool Result Details
- Agent Local Drafts
- Historical Discussion
- Previous Candidate Outputs

제거 가능:

- Duplicate Logs
- Rejected Candidate Solutions
- Temporary Reasoning Data
- Irrelevant Memory
- Stale Tool Raw Output
- Repeated Explanations

---

### [실무]

Compression Decision Table:

| 정보                  | 처리           | 이유             |
| --------------------- | -------------- | ---------------- |
| 현재 사용자 요청      | 유지           | 최종 검수 기준   |
| 활성 요구사항         | 유지           | 작업 품질 기준   |
| 완료된 Part 목록      | 요약           | 진행 상태 유지   |
| 오래된 초안 후보      | 제거           | 현재 작업 불필요 |
| Review Finding 미해결 | 유지           | Fix 필요         |
| Review Finding 해결됨 | 요약           | 이력만 필요      |
| Tool Result 원문      | 요약           | Token 절약       |
| 민감정보              | 제거           | Safety 기준      |
| 결정 변경 이력        | 요약 또는 보존 | 추적 필요        |

압축 후 State 예시:

```json
{
  "activeContext": {
    "userRequest": "다음",
    "currentTask": "Agent Memory State Management Part05 작성",
    "outputFormat": "writing_block_document"
  },
  "compressedHistory": [
    "Part01 완료: State vs Memory",
    "Part02 완료: Memory Types",
    "Part03 완료: Shared State & Multi-Agent State",
    "Part04 완료: Checkpoint / Resume / Rollback"
  ],
  "activeRules": [
    "MASTER_RAG_RULES",
    "Agent Memory State Management Domain Rules",
    "Project Progress alignment"
  ],
  "openIssues": [],
  "nextAction": "Part06 Memory Retrieval / Update / Validation"
}
```

---

### [FAQ]

Q. State Compression에서 반드시 유지할 것은?
A. 현재 요청, 활성 요구사항, 활성 제약, 확정 결정, 열린 이슈, 미해결 오류, 다음 작업이다.

Q. 요약 가능한 것은?
A. 완료된 단계, 해결된 오류, 오래된 Review 로그, Tool Result 세부사항, 이전 후보안이다.

Q. 제거 가능한 것은?
A. 중복 로그, 거절된 후보안, 임시 추론 데이터, 무관한 Memory, 오래된 Tool 원문이다.

Q. Compression 중 가장 위험한 실수는?
A. 핵심 제약이나 확정 결정을 누락하는 것이다.

Q. Compression은 언제 수행해?
A. State가 길어져 Context 품질이 떨어지거나 Agent Handoff 전에 수행한다.

---

# 13. State Token Budget

## 13.1 Token Budget 기준

### [개념]

State Token Budget은 Agent State가 Context Window에서 차지할 수 있는 최대 비중을 정하는 기준이다.

State가 너무 길면 RAG 검색 결과, 사용자 요청, 최종 출력에 사용할 Context가 줄어든다.

```text
State Token Budget = State가 사용할 수 있는 Context 예산
```

---

### [핵심]

Token Budget 원칙:

- State는 현재 작업에 필요한 만큼만 유지한다.
- 완료된 단계는 압축한다.
- Tool Result 원문을 과도하게 유지하지 않는다.
- Agent Local State 전체를 Shared State에 넣지 않는다.
- Retrieval Context와 Final Output 공간을 남긴다.
- Token Budget 초과 시 Compression을 수행한다.

권장 비중:

| Context 영역                |   권장 비중 |
| --------------------------- | ----------: |
| Current User Request        |       5~10% |
| Active State                |      10~20% |
| Retrieved Context           |      30~50% |
| Draft / Reasoning Workspace |      20~30% |
| Final Output                | 필요량 확보 |

---

### [실무]

나쁜 구조:

```text
State 70%
Retrieved Context 10%
Final Output 20%
```

문제:

- RAG 검색 결과 반영 부족
- 현재 요청 반영 약화
- 문서 생성 품질 저하
- 오래된 상태에 과적합

좋은 구조:

```text
Current Request 5%
Active State 15%
Retrieved Context 40%
Draft Workspace 20%
Final Output 20%
```

긴 Multi-Agent 작업에서는 Agent별 Local State를 별도 보관하고 Shared State에는 요약만 둔다.

---

### [FAQ]

Q. State Token Budget이 뭐야?
A. Agent State가 Context Window에서 차지할 수 있는 최대 비중을 정하는 기준이다.

Q. State가 너무 길면 왜 문제야?
A. RAG 검색 결과와 최종 출력에 사용할 Context가 줄어들어 답변 품질이 떨어진다.

Q. State는 어느 정도가 적당해?
A. 일반적으로 Active State는 전체 Context의 10~20% 수준으로 유지하는 것이 좋다.

Q. Token Budget을 초과하면?
A. 완료된 단계, 오래된 로그, Tool Result 원문을 압축한다.

Q. Shared State에 Agent Local State 전체를 넣어도 돼?
A. 아니다. 필요한 outputSummary만 넣어야 한다.

---

# 14. Common Mistakes

## 14.1 State Schema / Update / Compression 실수

### [개념]

State Schema, State Update, State Compression 실수는 Agent Workflow의 일관성을 무너뜨린다.

필드 구조가 불명확하거나 업데이트 방식이 잘못되면 Agent 간 충돌과 잘못된 최종 출력이 발생한다.

---

### [핵심]

자주 발생하는 실수:

- State Schema 없이 자유 텍스트만 사용
- Required Field와 Optional Field를 구분하지 않음
- Status 값을 제각각 사용
- 모든 State Update를 Replace로 처리
- Review Findings를 삭제
- userRequest 원본을 덮어씀
- requirements를 덮어써서 기존 제약 누락
- decisions 변경 이력을 남기지 않음
- Local State 전체를 Shared State에 저장
- Compression 중 핵심 제약 삭제
- Tool Result 전체를 계속 유지
- State Validation 없이 다음 Agent로 Handoff

---

### [실무]

문제:

```text
Review Agent가 이전 검토 결과를 잃어버림
```

원인:

```text
reviewFindings를 Append하지 않고 Replace함
```

해결:

```text
reviewFindings는 Append
→ 해결 시 status를 fixed로 변경
→ appliedFixes와 findingId 연결
```

문제:

```text
최종 결과가 사용자 요청과 다른 형식으로 출력됨
```

원인:

```text
userRequest 원본과 outputFormat constraint가 State Compression 중 삭제됨
```

해결:

```text
Current User Request 유지
→ outputFormat은 activeConstraints에 보존
→ Final State에서 deliveryFormat 검증
```

문제:

```text
Backend Agent와 Frontend Agent가 다른 API 계약을 사용함
```

원인:

```text
apiContract 변경을 Versioned Update로 관리하지 않음
```

해결:

```text
apiContract를 versioned field로 관리
→ active version 명시
→ Review Agent가 Cross-domain Consistency 검토
```

---

### [FAQ]

Q. State Schema 관련 가장 흔한 실수는?
A. Schema 없이 자유 텍스트로만 상태를 관리해 Agent 간 형식 불일치가 발생하는 것이다.

Q. State Update 관련 가장 흔한 실수는?
A. 모든 필드를 Replace로 처리해 Review Findings나 요구사항을 잃어버리는 것이다.

Q. State Compression 관련 가장 흔한 실수는?
A. 핵심 제약, 현재 요청, 확정 결정까지 요약 중 누락하는 것이다.

Q. userRequest를 덮어쓰면 왜 문제야?
A. 최종 결과가 원래 사용자 요청을 기준으로 검수되지 못한다.

Q. 해결 핵심은?
A. Schema 정의, Update 방식 구분, Compression 후 Validation을 적용하는 것이다.

---

# 15. Troubleshooting

## 15.1 State Schema / Update / Compression 문제 해결

### [개념]

Troubleshooting은 State Schema, State Update, State Compression 과정에서 발생하는 문제를 원인과 해결 기준으로 정리한다.

상태 문제는 출력 오류보다 먼저 구조 오류를 확인해야 한다.

---

### [핵심]

Troubleshooting 형식:

```md
문제:

원인:

해결:
```

주요 문제:

- 필수 필드 누락
- Status 값 혼용
- Review Findings 삭제
- requirements 누락
- Decision 충돌
- Compression 후 출력 형식 불일치
- State가 너무 커짐
- Agent가 수정 권한 없는 필드 변경

---

### [실무]

문제:

```text
필수 필드가 누락되어 다음 Agent가 작업을 이어갈 수 없음
```

원인:

```text
State Schema에 Required Field가 정의되지 않음
```

해결:

```text
workflowId, userRequest, currentTask, currentStep, status, requirements, constraints를 Required로 정의
→ State Validation 수행
```

문제:

```text
Status 값이 complete, done, finished로 섞임
```

원인:

```text
Status Enum 표준이 없음
```

해결:

```text
planned, in_progress, waiting, review, fix, blocked, completed, failed, cancelled로 통일
→ 기존 값 매핑
```

문제:

```text
requirements가 새 요청으로 덮어써져 기존 제약이 사라짐
```

원인:

```text
requirements에 Replace Update 적용
```

해결:

```text
requirements는 Merge Update 적용
→ 중복 제거
→ 충돌 항목은 Conflict로 분리
```

문제:

```text
Compression 후 중요한 Decision이 사라짐
```

원인:

```text
Compression 기준 없이 오래된 정보로 판단해 삭제함
```

해결:

```text
Active Decision은 반드시 유지
→ Deprecated Decision만 요약
→ Compression 후 Validation 수행
```

문제:

```text
State가 너무 커져 Retrieval Context가 부족함
```

원인:

```text
Tool Result 원문과 Agent Local State 전체를 Shared State에 저장함
```

해결:

```text
Tool Result 요약
→ Local State는 개별 보관
→ Shared State에는 outputSummary만 반영
→ Token Budget 적용
```

---

### [FAQ]

Q. 필수 필드 누락 문제는 어떻게 해결해?
A. Required Field를 Schema에 정의하고 State Validation으로 누락 여부를 확인한다.

Q. Status 값 혼용은 어떻게 해결해?
A. 표준 Status Enum을 정하고 기존 값을 매핑해 통일한다.

Q. Review Findings가 사라졌다면?
A. 마지막 Checkpoint에서 복구하고 이후 reviewFindings는 Append 방식으로 관리한다.

Q. Compression 후 중요한 정보가 사라지면?
A. Active Requirements, Constraints, Decisions를 복구하고 Compression Rule을 강화한다.

Q. State가 너무 크면?
A. 완료 단계, Tool Result 원문, Agent Local State를 요약하고 Active Context만 유지한다.

---

# 16. Best Practice

## 16.1 State Schema, Update, Compression 설계 원칙

### [개념]

좋은 State Management는 명확한 Schema, 올바른 Update 방식, 안전한 Compression으로 구성된다.

State는 Agent Workflow를 안정화하는 실행 기준이다.

---

### [핵심]

Best Practice:

- State Schema를 정의한다.
- Required Field와 Optional Field를 구분한다.
- Status Enum을 표준화한다.
- userRequest 원본은 보존한다.
- requirements와 constraints는 Merge 방식으로 업데이트한다.
- reviewFindings와 errors는 Append 방식으로 업데이트한다.
- currentStep, status, nextAction은 Replace 방식으로 업데이트한다.
- decisions와 apiContract는 Versioned Update로 관리한다.
- State Update 후 Validation을 수행한다.
- Agent별 Update Ownership을 정의한다.
- Agent Local State 전체를 Shared State에 저장하지 않는다.
- State가 길어지면 Compression을 수행한다.
- Compression 중 Active Requirements, Constraints, Decisions는 유지한다.
- Tool Result는 필요한 핵심만 요약한다.
- Token Budget을 관리한다.
- 민감정보와 Secret은 State에 저장하지 않는다.

---

### [실무]

권장 State Management Flow:

```text
Create State Schema
→ Initialize Required Fields
→ Execute Agent Step
→ Apply Correct Update Type
→ Validate State
→ Compress if Needed
→ Handoff or Finalize
```

권장 Update Mapping:

```text
reviewFindings → Append
errors → Append
appliedFixes → Append
currentStep → Replace
status → Replace
nextAction → Replace
requirements → Merge
constraints → Merge
decisions → Versioned Update
apiContract → Versioned Update
agentOutputs → Owner Replace
```

권장 Compression Flow:

```text
Detect Large State
→ Preserve Current Request
→ Preserve Active Requirements
→ Preserve Active Constraints
→ Preserve Active Decisions
→ Summarize Completed Steps
→ Summarize Tool Results
→ Remove Temporary Data
→ Validate Compressed State
```

---

### [FAQ]

Q. 좋은 State Schema 기준은?
A. 필드명, 타입, 필수 여부, 기본값, 업데이트 방식, Owner Agent, 검증 규칙이 명확한 구조다.

Q. 좋은 State Update 기준은?
A. 필드 성격에 따라 Append, Replace, Merge, Versioned Update를 구분하는 것이다.

Q. 좋은 State Compression 기준은?
A. 현재 요청, 활성 요구사항, 활성 제약, 확정 결정, 열린 이슈는 유지하고 완료된 단계와 Tool Result는 요약하는 것이다.

Q. State Management의 핵심은?
A. 구조화된 Schema, 안전한 Update, 검증 가능한 Compression을 적용하는 것이다.

Q. State Schema, Update, Compression의 최종 목표는?
A. Multi-Agent Workflow가 상태를 잃지 않고 일관된 Final Output을 만들도록 하는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. State Schema가 뭐야?
A. Agent State에 어떤 필드가 있고 각 필드가 어떤 타입과 업데이트 규칙을 가지는지 정의한 구조다.

Q. State Schema는 왜 필요해?
A. Agent 간 상태 형식 불일치와 필드 누락을 줄여 Workflow 안정성을 높이기 위해 필요하다.

Q. State Schema에는 무엇을 정의해?
A. Field Name, Type, Required 여부, Default Value, Update Rule, Owner Agent, Validation Rule을 정의한다.

Q. Agent State에 꼭 필요한 필드는?
A. workflowId, userRequest, currentTask, currentStep, status, requirements, constraints, nextAction이 핵심이다.

Q. Required Field와 Optional Field 차이는?
A. Required Field는 없으면 Workflow가 깨지는 필드이고 Optional Field는 작업 유형에 따라 사용하는 필드다.

Q. State Status Enum이 뭐야?
A. Workflow 진행 상태를 Agent들이 동일하게 해석하도록 만든 표준 상태 값이다.

Q. 권장 Status 값은?
A. planned, in_progress, waiting, review, fix, blocked, completed, failed, cancelled를 사용한다.

Q. blocked와 failed 차이는?
A. blocked는 해결하면 진행 가능한 차단 상태이고 failed는 작업이 실패로 종료된 상태다.

Q. State Update가 뭐야?
A. Agent Workflow 진행 중 currentStep, requirements, reviewFindings 같은 State 필드를 갱신하는 과정이다.

Q. State Update 방식은 뭐가 있어?
A. Append, Replace, Merge, Versioned Update, Owner Replace 방식이 있다.

Q. Append Update는 뭐야?
A. 기존 값을 지우지 않고 새 항목을 추가하는 State Update 방식이다.

Q. Append는 어디에 사용해?
A. reviewFindings, errors, logs, appliedFixes처럼 누적 기록이 필요한 필드에 사용한다.

Q. Replace Update는 뭐야?
A. 기존 값을 새 값으로 교체하는 State Update 방식이다.

Q. Replace는 어디에 사용해?
A. currentStep, status, nextAction처럼 현재 값 하나만 의미 있는 필드에 사용한다.

Q. Merge Update는 뭐야?
A. 기존 값과 새 값을 합치고 중복을 정리하는 State Update 방식이다.

Q. Merge는 어디에 사용해?
A. requirements, constraints, referenceDocuments, validationCriteria처럼 누락되면 안 되는 목록에 사용한다.

Q. Versioned Update는 뭐야?
A. 중요한 결정이나 계약이 변경될 때 이전 값을 보존하고 새 버전을 활성화하는 Update 방식이다.

Q. Versioned Update는 어디에 사용해?
A. decisions, apiContract, architectureDecision, projectPolicy처럼 변경 이력이 중요한 필드에 사용한다.

Q. State Validation이 뭐야?
A. State Update 후 상태가 Schema와 Workflow 규칙을 만족하는지 확인하는 과정이다.

Q. State Validation에서 무엇을 확인해?
A. 필수 필드, 타입, Status Enum, 요구사항 누락, 제약 충돌, 수정 권한, 민감정보 여부를 확인한다.

Q. State Compression이 뭐야?
A. State가 길어졌을 때 현재 작업에 필요한 핵심 정보만 남기고 압축하는 과정이다.

Q. State Compression은 왜 필요해?
A. Context Window 낭비를 줄이고 Agent 응답 품질을 유지하기 위해 필요하다.

Q. State Compression에서 반드시 유지할 것은?
A. 현재 요청, 활성 요구사항, 활성 제약, 확정 결정, 열린 이슈, 미해결 오류, 다음 작업이다.

Q. State Compression에서 제거 가능한 것은?
A. 중복 로그, 거절된 후보안, 임시 추론 데이터, 무관한 Memory, 오래된 Tool 원문이다.

Q. State Token Budget이 뭐야?
A. Agent State가 Context Window에서 차지할 수 있는 최대 비중을 정하는 기준이다.

Q. State가 너무 길면 왜 문제야?
A. RAG 검색 결과와 최종 출력에 사용할 Context가 줄어들어 답변 품질이 떨어진다.

Q. userRequest를 Replace하면 안 되는 이유는?
A. 원본 사용자 요청은 최종 검수 기준이므로 임의로 덮어쓰면 안 된다.

Q. Review Findings는 어떻게 업데이트해?
A. 삭제하지 않고 Append 방식으로 누적하며 해결 시 status를 fixed로 변경한다.

Q. requirements는 어떻게 업데이트해?
A. Replace가 아니라 Merge 방식으로 기존 요구사항을 보존하고 새 요구사항을 추가한다.

Q. decisions는 어떻게 업데이트해?
A. Versioned Update로 이전 결정을 보존하고 최신 active 결정을 명확히 한다.

Q. State Schema, Update, Compression의 최종 목표는?
A. Multi-Agent Workflow가 상태를 잃지 않고 일관된 Final Output을 만들도록 하는 것이다.
