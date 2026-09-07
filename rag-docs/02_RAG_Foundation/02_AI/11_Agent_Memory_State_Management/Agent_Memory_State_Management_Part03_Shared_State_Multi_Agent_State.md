# Agent Memory & State Management Part03 - Shared State & Multi-Agent State

---

# 1. Shared State Foundation

## 1.1 Shared State 기본 개념

### [개념]

Shared State는 Multi-Agent Workflow에서 여러 Agent가 함께 참조하는 공통 작업 상태이다.

Shared State는 PM Agent, Backend Agent, Frontend Agent, Review Agent, DevOps Agent, AI/ML Agent가 같은 요구사항과 결정 사항을 기준으로 작업하게 만든다.

```text
Shared State = 여러 Agent가 공유하는 Workflow 기준 상태
```

Shared State는 Agent 간 Handoff, Review, Fix, Final Output의 기준 데이터이다.

기본 Flow:

```text
User Request
→ PM Agent creates Shared State
→ Domain Agent updates output
→ Review Agent adds findings
→ Fix Agent updates result
→ PM Agent finalizes output
```

---

### [핵심]

- Shared State는 Agent 간 공통 작업 기록이다.
- PM Agent가 초기 Shared State를 구성한다.
- Domain Agent는 자기 작업 결과를 Shared State에 추가한다.
- Review Agent는 검토 결과를 Shared State에 추가한다.
- Fix Agent는 수정 결과를 Shared State에 반영한다.
- 최종 PM Agent가 Shared State를 통합해 Final Output을 만든다.
- Agent별 Local State와 Shared State는 구분해야 한다.
- Shared State가 없으면 Agent 간 요구사항 충돌이 발생한다.

---

### [실무]

2026 실무 기준 Multi-Agent System에서는 Shared State를 단순 대화 문자열로 관리하지 않는다.

Shared State는 구조화된 Schema로 관리한다.

예시:

```json
{
  "workflowId": "rag-doc-amsm-part03",
  "userRequest": "Agent Memory State Management Part03 작성",
  "taskPlan": [
    "Shared State 개념 작성",
    "Multi-Agent State 구조 작성",
    "Handoff State 작성",
    "Review State 작성",
    "Final State 작성"
  ],
  "assignedAgents": ["PM Agent", "AI Domain Agent", "Review Agent"],
  "sharedRequirements": [
    "MASTER_RAG_RULES 적용",
    "DOMAIN_RULES 적용",
    "FAQ 강화",
    "Retrieval Queries 포함"
  ],
  "sharedConstraints": [
    "사람용 문서보다 Retrieval 최적화 우선",
    "용어 통일",
    "중간 응답 금지",
    "최종 결과만 writing block으로 출력"
  ],
  "intermediateOutputs": {},
  "reviewStatus": "pending",
  "finalStatus": "in_progress"
}
```

Shared State는 현재 Workflow의 기준점이다.

모든 Agent가 같은 Shared State를 읽고 필요한 필드만 갱신해야 한다.

---

### [FAQ]

Q. Shared State가 뭐야?
A. 여러 Agent가 같은 요구사항, 제약, 결정, 중간 결과를 기준으로 작업하기 위해 공유하는 공통 Workflow 상태다.

Q. Shared State는 왜 필요해?
A. Agent마다 다른 기준으로 작업하지 않도록 요구사항과 결정 사항을 통일하기 위해 필요하다.

Q. Shared State는 누가 만들어?
A. 일반적으로 PM Agent가 사용자 요청을 분석해 초기 Shared State를 만든다.

Q. Shared State에는 무엇을 넣어?
A. userRequest, workflowId, taskPlan, assignedAgents, sharedRequirements, sharedConstraints, intermediateOutputs, reviewStatus, finalStatus를 넣는다.

Q. Shared State와 Memory는 같아?
A. 아니다. Shared State는 현재 Workflow 상태이고, Memory는 과거 정보를 재사용하기 위한 저장 정보다.

---

# 2. Shared State Required Fields

## 2.1 Shared State 필수 필드

### [개념]

Shared State는 Multi-Agent Workflow에서 공통으로 참조해야 하는 필드를 포함해야 한다.

필드가 불명확하면 Agent가 서로 다른 요구사항을 기준으로 작업할 수 있다.

필수 필드:

```text
userRequest
workflowId
taskPlan
assignedAgents
sharedRequirements
sharedConstraints
apiContract
domainDecisions
intermediateOutputs
reviewStatus
finalStatus
```

---

### [핵심]

- userRequest는 원본 사용자 요청이다.
- workflowId는 현재 Workflow 식별자이다.
- taskPlan은 작업 단계 목록이다.
- assignedAgents는 참여 Agent 목록이다.
- sharedRequirements는 모든 Agent가 지켜야 할 요구사항이다.
- sharedConstraints는 작업 제한 조건이다.
- apiContract는 Backend와 Frontend 간 계약이다.
- domainDecisions는 Domain별 확정 결정이다.
- intermediateOutputs는 Agent별 중간 결과이다.
- reviewStatus는 검토 상태이다.
- finalStatus는 전체 Workflow 완료 상태이다.

---

### [실무]

Shared State Schema 예시:

```json
{
  "userRequest": "string",
  "workflowId": "string",
  "taskPlan": ["string"],
  "assignedAgents": ["string"],
  "sharedRequirements": ["string"],
  "sharedConstraints": ["string"],
  "apiContract": {
    "endpoints": [],
    "requestDtos": [],
    "responseDtos": [],
    "authRules": []
  },
  "domainDecisions": [
    {
      "domain": "string",
      "decision": "string",
      "reason": "string",
      "status": "active"
    }
  ],
  "intermediateOutputs": {
    "pmAgent": {},
    "backendAgent": {},
    "frontendAgent": {},
    "reviewAgent": {}
  },
  "reviewStatus": "pending",
  "finalStatus": "in_progress"
}
```

RAG 문서 제작 Workflow에서는 apiContract가 없을 수 있다.

이 경우 apiContract는 optional 또는 empty object로 유지한다.

---

### [FAQ]

Q. Shared State 필수 필드는 뭐야?
A. userRequest, workflowId, taskPlan, assignedAgents, sharedRequirements, sharedConstraints, intermediateOutputs, reviewStatus, finalStatus가 핵심이다.

Q. apiContract는 항상 필요해?
A. Backend와 Frontend 연동 작업에서는 중요하지만, RAG 문서 작성처럼 API가 없는 작업에서는 optional로 둘 수 있다.

Q. domainDecisions는 왜 필요해?
A. Domain별 확정 결정을 Shared State에 남겨 Agent 간 기준 충돌을 줄이기 위해 필요하다.

Q. intermediateOutputs에는 무엇을 저장해?
A. Agent별 중간 결과, 초안, 검토 대상 결과, 수정 결과를 저장한다.

Q. finalStatus는 왜 필요해?
A. Workflow가 진행 중인지, 검토 중인지, 완료되었는지 명확히 하기 위해 필요하다.

---

# 3. Multi-Agent State Foundation

## 3.1 Global State와 Local State

### [개념]

Multi-Agent State는 여러 Agent가 참여하는 Workflow의 상태 관리 구조이다.

Multi-Agent System에서는 Global State, Shared State, Agent Local State를 구분한다.

```text
Global State = 전체 Workflow 상태
Shared State = Agent들이 공유하는 공통 상태
Agent Local State = 개별 Agent의 내부 작업 상태
```

기본 구조:

```text
Global State
├ Shared State
├ PM Agent Local State
├ Backend Agent Local State
├ Frontend Agent Local State
├ Review Agent Local State
├ DevOps Agent Local State
└ Final Output State
```

---

### [핵심]

- Global State는 전체 Workflow를 관리한다.
- Shared State는 Agent 간 공통 기준을 제공한다.
- Agent Local State는 개별 Agent의 작업 정보를 저장한다.
- Local State 전체를 Global State에 넣으면 복잡해진다.
- 공유해야 할 정보와 내부 임시 정보를 구분해야 한다.
- Agent Output과 Final Output은 구분해야 한다.
- Review State는 품질 검증 결과를 관리한다.
- Final State는 사용자에게 전달할 최종 결과를 관리한다.

---

### [실무]

Multi-Agent Workflow 예시:

```text
User Request
→ PM Agent
  → Global State 생성
  → Shared State 초기화
→ Backend Agent
  → Backend Local State 생성
  → Backend Output 작성
  → Shared State에 결과 요약 반영
→ Frontend Agent
  → Frontend Local State 생성
  → API Contract 기준 화면 작성
  → Shared State에 결과 요약 반영
→ Review Agent
  → Shared State 기준 검토
  → Review Findings 추가
→ Fix Agent
  → Review Findings 기준 수정
→ PM Agent
  → Final State 정리
  → Final Output 생성
```

중요 원칙:

```text
Local State 전체 공유 금지
필요한 Output Summary만 Shared State에 반영
Review Findings는 Append
Current Step은 Replace
Decision은 Versioned Update
```

---

### [FAQ]

Q. Multi-Agent State가 뭐야?
A. 여러 Agent가 참여하는 Workflow에서 전체 상태, 공유 상태, 개별 Agent 상태를 관리하는 구조다.

Q. Global State와 Shared State 차이는?
A. Global State는 전체 Workflow 상태이고, Shared State는 여러 Agent가 함께 참조하는 공통 상태다.

Q. Agent Local State는 뭐야?
A. 개별 Agent가 자기 작업을 수행하는 동안 사용하는 내부 작업 상태다.

Q. Local State를 모두 Shared State에 넣어도 돼?
A. 아니다. 필요한 결과 요약만 Shared State에 반영해야 Context가 커지지 않는다.

Q. Multi-Agent State에서 가장 중요한 점은?
A. 공유해야 할 정보와 개별 Agent의 임시 정보를 분리하는 것이다.

---

# 4. PM Agent State

## 4.1 PM Agent의 State 책임

### [개념]

PM Agent State는 전체 Workflow를 계획하고 조율하기 위한 상태이다.

PM Agent는 사용자 요청을 분석하고 Shared State를 초기화하며 Agent별 작업을 분배한다.

```text
PM Agent State = Workflow 기획, 분배, 통합 상태
```

---

### [핵심]

PM Agent State 포함 대상:

- userRequestAnalysis
- taskPlan
- agentAssignment
- sharedRequirements
- sharedConstraints
- scopeDecision
- priorityDecision
- workflowStatus
- finalIntegrationPlan

PM Agent 책임:

- 사용자 요청 분석
- 작업 범위 결정
- Agent 배정
- Shared State 생성
- 공통 요구사항 정리
- Agent Output 통합
- 최종 결과 품질 확인

---

### [실무]

PM Agent State 예시:

```json
{
  "agent": "PM Agent",
  "userRequestAnalysis": {
    "taskType": "rag_document_creation",
    "targetDocument": "Agent Memory State Management Part03",
    "outputFormat": "writing_block_document"
  },
  "taskPlan": [
    "Shared State 작성",
    "Multi-Agent State 작성",
    "Handoff State 작성",
    "Review State 작성",
    "Final State 작성"
  ],
  "agentAssignment": {
    "domainAgent": "AI Domain Agent",
    "reviewAgent": "Review Agent"
  },
  "sharedRequirements": [
    "MASTER_RAG_RULES 적용",
    "DOMAIN_RULES 적용",
    "Retrieval Queries 포함"
  ],
  "workflowStatus": "in_progress",
  "finalIntegrationPlan": "각 Section을 RAG 최적화 구조로 통합"
}
```

PM Agent는 Shared State의 owner 역할을 한다.

다만 모든 필드를 PM Agent만 수정하는 것은 아니다.

각 Agent는 자신에게 할당된 필드만 갱신한다.

---

### [FAQ]

Q. PM Agent State는 뭐야?
A. PM Agent가 사용자 요청을 분석하고 Workflow를 계획, 분배, 통합하기 위해 사용하는 상태다.

Q. PM Agent는 Shared State를 왜 만들어?
A. 모든 Agent가 같은 요구사항과 제약을 기준으로 작업하도록 하기 위해 만든다.

Q. PM Agent State에는 무엇이 들어가?
A. userRequestAnalysis, taskPlan, agentAssignment, sharedRequirements, sharedConstraints, workflowStatus가 들어간다.

Q. PM Agent가 모든 작업을 직접 처리해?
A. 아니다. PM Agent는 계획과 통합을 담당하고 Domain Agent와 Review Agent에 작업을 분배한다.

Q. PM Agent가 최종적으로 하는 일은?
A. Agent Output을 통합하고 Final State를 기준으로 최종 결과를 만든다.

---

# 5. Domain Agent State

## 5.1 Domain Agent의 State 책임

### [개념]

Domain Agent State는 특정 기술 영역 또는 문서 영역을 처리하는 Agent의 작업 상태이다.

Backend Agent, Frontend Agent, DevOps Agent, AI/ML Agent, AI Domain Agent는 각자 Local State를 가진다.

```text
Domain Agent State = 특정 Domain 작업 수행 상태
```

---

### [핵심]

Domain Agent State 포함 대상:

- assignedTask
- domainScope
- retrievedDomainRules
- domainConstraints
- candidateOutput
- validationResult
- domainAssumptions
- domainWarnings
- outputSummary

Domain Agent 책임:

- Domain Rules 적용
- Domain 지식 기반 초안 생성
- Domain별 제약 반영
- 중간 결과 작성
- Shared State에 결과 요약 반영
- Review 대상 Output 제공

---

### [실무]

AI Domain Agent State 예시:

```json
{
  "agent": "AI Domain Agent",
  "assignedTask": "Shared State & Multi-Agent State RAG 문서 작성",
  "domainScope": [
    "Shared State",
    "Global State",
    "Agent Local State",
    "Handoff State",
    "Review State",
    "Final State"
  ],
  "retrievedDomainRules": [
    "Agent Memory & State Management Domain Rules",
    "MASTER_RAG_RULES",
    "Project Progress"
  ],
  "domainConstraints": [
    "State와 Memory 구분",
    "Multi-Agent Workflow 기준",
    "Retrieval 최적화",
    "FAQ 강화"
  ],
  "candidateOutput": "draft_document",
  "validationResult": "pending",
  "outputSummary": "Part03 초안 작성 완료"
}
```

Domain Agent는 Local State의 모든 정보를 Shared State에 복사하지 않는다.

최종적으로 필요한 outputSummary, domainDecisions, openIssues만 Shared State에 반영한다.

---

### [FAQ]

Q. Domain Agent State는 뭐야?
A. 특정 기술 영역이나 문서 영역을 맡은 Agent가 자기 작업을 수행하기 위해 사용하는 Local State다.

Q. Domain Agent State에는 무엇을 넣어?
A. assignedTask, domainScope, retrievedDomainRules, domainConstraints, candidateOutput, validationResult, outputSummary를 넣는다.

Q. Domain Agent 결과는 어떻게 공유해?
A. 전체 Local State가 아니라 outputSummary와 필요한 결정 사항만 Shared State에 반영한다.

Q. Domain Agent는 Memory를 직접 업데이트해?
A. 가능하지만 보통 PM Agent 또는 Memory Manager가 검토 후 장기 Memory Update를 수행하는 구조가 안정적이다.

Q. Domain Agent State와 Shared State 차이는?
A. Domain Agent State는 개별 Agent 내부 상태이고, Shared State는 여러 Agent가 함께 보는 공통 상태다.

---

# 6. Handoff State

## 6.1 Agent 간 Handoff 기준

### [개념]

Handoff State는 한 Agent가 다음 Agent에게 작업을 넘길 때 전달하는 상태 요약이다.

Handoff State는 Agent 간 작업 연속성을 보장한다.

```text
Handoff State = Agent 간 작업 인계 상태
```

Handoff는 전체 Local State 전달이 아니라 필요한 정보 전달이다.

---

### [핵심]

Handoff State 포함 대상:

- taskSummary
- completedSteps
- pendingSteps
- importantRequirements
- importantConstraints
- decisions
- outputLocation
- knownIssues
- nextAgentInstruction
- validationNeeded

Handoff State 규칙:

- 필요한 정보만 전달한다.
- 결정 사항과 제약은 누락하지 않는다.
- 실패와 오류를 숨기지 않는다.
- 다음 Agent가 해야 할 일을 명확히 한다.
- 추정과 확정 사실을 구분한다.

---

### [실무]

Handoff State 예시:

```json
{
  "fromAgent": "AI Domain Agent",
  "toAgent": "Review Agent",
  "taskSummary": "Agent Memory State Management Part03 초안 작성",
  "completedSteps": [
    "Shared State 개념 작성",
    "Multi-Agent State 구조 작성",
    "PM Agent State 작성",
    "Domain Agent State 작성"
  ],
  "pendingSteps": [
    "Review 검수",
    "Retrieval Queries 중복 확인",
    "FAQ 품질 확인"
  ],
  "importantRequirements": [
    "MASTER_RAG_RULES 적용",
    "FAQ 포함",
    "Retrieval Queries 포함"
  ],
  "importantConstraints": [
    "State와 Memory 혼동 금지",
    "사람용 문서보다 Retrieval 최적화 우선"
  ],
  "decisions": ["Part03은 Shared State와 Multi-Agent State 중심으로 작성"],
  "knownIssues": [],
  "nextAgentInstruction": "문서 구조, 용어 통일, FAQ 품질, Retrieval Queries를 검수한다.",
  "validationNeeded": true
}
```

Handoff State가 부실하면 Review Agent가 잘못된 기준으로 검토한다.

---

### [FAQ]

Q. Handoff State가 뭐야?
A. 한 Agent가 다음 Agent에게 작업을 넘길 때 필요한 요약 상태다.

Q. Handoff State는 왜 필요해?
A. Agent 간 작업 연속성을 유지하고 요구사항, 제약, 결정 누락을 방지하기 위해 필요하다.

Q. Handoff State에는 무엇을 넣어?
A. taskSummary, completedSteps, pendingSteps, requirements, constraints, decisions, knownIssues, nextAgentInstruction을 넣는다.

Q. Local State 전체를 Handoff해야 해?
A. 아니다. 다음 Agent가 필요한 핵심 정보만 전달한다.

Q. Handoff에서 가장 중요한 것은?
A. 결정 사항, 제약, 남은 작업, 알려진 문제를 명확히 전달하는 것이다.

---

# 7. Review State

## 7.1 Review Agent의 검토 상태

### [개념]

Review State는 Review Agent가 작업 결과를 검토하면서 기록하는 품질 검증 상태이다.

Review State는 오류, 누락, 규칙 위반, 개선 사항을 구조화한다.

```text
Review State = 검토 결과와 수정 필요 사항을 기록하는 상태
```

Review State는 Fix Loop의 기준이 된다.

---

### [핵심]

Review State 포함 대상:

- reviewTarget
- reviewCriteria
- checklistResults
- findings
- severity
- requiredFixes
- optionalImprovements
- passStatus
- reviewedBy
- reviewedAt

Review 기준:

- Master Rules 적용 여부
- Domain Rules 적용 여부
- Required Section 포함 여부
- FAQ 품질
- Retrieval Queries 포함 여부
- 용어 통일
- 중복 설명 최소화
- 치명적 문제 여부

---

### [실무]

Review State 예시:

```json
{
  "reviewTarget": "Agent_Memory_State_Management_Part03",
  "reviewCriteria": [
    "MASTER_RAG_RULES",
    "Agent Memory State Management Domain Rules",
    "Project Progress Alignment",
    "Output Format Compliance"
  ],
  "checklistResults": {
    "hasConceptSections": true,
    "hasCoreSections": true,
    "hasPracticeSections": true,
    "hasFAQSections": true,
    "hasRetrievalQueries": true,
    "terminologyConsistent": true,
    "criticalIssueFound": false
  },
  "findings": [],
  "severity": "none",
  "requiredFixes": [],
  "optionalImprovements": [],
  "passStatus": "pass"
}
```

Review Findings는 Append 방식으로 누적한다.

수정 완료 후 Review State를 다시 갱신한다.

---

### [FAQ]

Q. Review State가 뭐야?
A. Review Agent가 작업 결과를 검토하며 오류, 누락, 개선 사항, 통과 여부를 기록하는 상태다.

Q. Review State에는 무엇을 넣어?
A. reviewTarget, reviewCriteria, checklistResults, findings, severity, requiredFixes, passStatus를 넣는다.

Q. Review Findings는 어떻게 업데이트해?
A. 기존 내용을 덮어쓰지 않고 Append 방식으로 누적하는 것이 좋다.

Q. Review State는 왜 중요해?
A. Fix Agent가 무엇을 수정해야 하는지 명확히 알 수 있기 때문이다.

Q. Review State의 핵심 기준은?
A. 규칙 적용 여부, 필수 Section 포함 여부, FAQ 품질, Retrieval Queries 포함 여부, 치명적 문제 여부다.

---

# 8. Fix State

## 8.1 Fix Loop 상태 관리

### [개념]

Fix State는 Review Findings를 기준으로 수정 작업을 수행할 때 사용하는 상태이다.

Fix State는 어떤 문제를 수정했는지, 어떤 문제를 남겼는지, 재검토가 필요한지 기록한다.

```text
Fix State = Review Findings 기반 수정 상태
```

---

### [핵심]

Fix State 포함 대상:

- sourceReviewFindings
- fixTargets
- appliedFixes
- unresolvedIssues
- regressionRisk
- retestNeeded
- fixStatus
- nextReviewRequired

Fix State 규칙:

- Review Findings와 Fix 결과를 연결한다.
- 수정한 항목과 수정하지 않은 항목을 구분한다.
- 수정 후 새로운 문제가 생겼는지 확인한다.
- 필요 시 Review Agent로 다시 보낸다.
- 치명적 문제는 unresolved 상태로 두지 않는다.

---

### [실무]

Fix State 예시:

```json
{
  "sourceReviewFindings": [
    {
      "id": "RF-001",
      "issue": "FAQ 부족",
      "severity": "medium"
    }
  ],
  "fixTargets": ["FAQ 추가", "Retrieval Queries 강화"],
  "appliedFixes": [
    {
      "findingId": "RF-001",
      "fix": "각 Section FAQ와 Retrieval Queries를 추가"
    }
  ],
  "unresolvedIssues": [],
  "regressionRisk": "low",
  "retestNeeded": true,
  "fixStatus": "completed",
  "nextReviewRequired": true
}
```

Fix State는 Review State와 함께 Fix Loop를 안정화한다.

---

### [FAQ]

Q. Fix State가 뭐야?
A. Review Findings를 기준으로 수정 작업을 수행하고 수정 결과를 기록하는 상태다.

Q. Fix State에는 무엇을 넣어?
A. sourceReviewFindings, fixTargets, appliedFixes, unresolvedIssues, retestNeeded, fixStatus를 넣는다.

Q. 수정 완료 후 바로 Final Output으로 가도 돼?
A. 치명적 문제나 중요한 수정이 있었다면 재검토 후 Final Output으로 가는 것이 안정적이다.

Q. unresolvedIssues는 왜 기록해?
A. 남은 문제를 숨기지 않고 다음 Review 또는 사용자 판단에 넘기기 위해 필요하다.

Q. Fix State의 핵심은?
A. Review Findings와 실제 수정 결과를 명확히 연결하는 것이다.

---

# 9. Final State

## 9.1 Final Output 기준 상태

### [개념]

Final State는 Workflow 완료 직전에 최종 결과를 정리하는 상태이다.

Final State는 사용자에게 전달할 결과가 요구사항을 만족하는지 확인한다.

```text
Final State = 최종 출력 전 완료 상태
```

---

### [핵심]

Final State 포함 대상:

- finalOutput
- satisfiedRequirements
- appliedConstraints
- reviewPassStatus
- unresolvedIssues
- deliveryFormat
- completionStatus
- memoryUpdateCandidates
- nextStepCandidates

Final State 규칙:

- 요구사항 충족 여부를 확인한다.
- 출력 형식이 현재 요청과 일치해야 한다.
- Review 통과 여부를 확인한다.
- 치명적 문제를 남기지 않는다.
- 필요한 경우 Memory Update 후보를 기록한다.
- 사용자에게는 Final Output만 전달할 수 있다.

---

### [실무]

Final State 예시:

```json
{
  "finalOutput": "Agent Memory State Management Part03 문서",
  "satisfiedRequirements": [
    "writing block document 형식",
    "MASTER_RAG_RULES 적용",
    "DOMAIN_RULES 적용",
    "FAQ 강화",
    "Retrieval Queries 포함"
  ],
  "appliedConstraints": [
    "중간 응답 없음",
    "사람용 문서보다 RAG Retrieval 최적화 우선",
    "용어 통일"
  ],
  "reviewPassStatus": "pass",
  "unresolvedIssues": [],
  "deliveryFormat": "writing_block",
  "completionStatus": "completed",
  "memoryUpdateCandidates": ["Part03 완료 상태"],
  "nextStepCandidates": ["Part04 Checkpoint / Resume / Rollback"]
}
```

Final State는 사용자에게 그대로 노출하지 않을 수 있다.

최종 출력물은 Final State를 기준으로 생성한다.

---

### [FAQ]

Q. Final State가 뭐야?
A. Workflow 완료 직전에 최종 결과, 충족 요구사항, 검토 상태, 남은 문제를 정리하는 상태다.

Q. Final State에는 무엇을 넣어?
A. finalOutput, satisfiedRequirements, appliedConstraints, reviewPassStatus, unresolvedIssues, deliveryFormat, completionStatus를 넣는다.

Q. Final State와 Final Output은 같아?
A. 아니다. Final State는 최종 출력 준비 상태이고, Final Output은 사용자에게 전달되는 결과물이다.

Q. unresolvedIssues가 있으면 어떻게 해?
A. 치명적 문제는 수정 후 재검토하고, 남은 문제가 있다면 명확히 표시해야 한다.

Q. Final State의 핵심은?
A. 최종 결과가 사용자 요청과 규칙을 충족하는지 확인하는 것이다.

---

# 10. State Update Ownership

## 10.1 Agent별 State 수정 권한

### [개념]

State Update Ownership은 어떤 Agent가 어떤 State 필드를 수정할 수 있는지 정하는 규칙이다.

Owner가 불명확하면 여러 Agent가 같은 필드를 덮어써 충돌이 발생한다.

```text
State Update Ownership = State 필드별 수정 책임 규칙
```

---

### [핵심]

권장 Ownership:

| State Field         | Owner Agent             | Update 방식               |
| ------------------- | ----------------------- | ------------------------- |
| userRequest         | PM Agent                | Replace 금지              |
| taskPlan            | PM Agent                | Versioned Update          |
| sharedRequirements  | PM Agent                | Merge                     |
| sharedConstraints   | PM Agent                | Merge                     |
| domainDecisions     | PM Agent + Domain Agent | Versioned Update          |
| intermediateOutputs | Domain Agent            | Append / Replace by Owner |
| reviewFindings      | Review Agent            | Append                    |
| appliedFixes        | Fix Agent               | Append                    |
| finalOutput         | PM Agent                | Replace                   |
| finalStatus         | PM Agent                | Replace                   |

---

### [실무]

좋은 Update 방식:

```text
Review Agent:
reviewFindings 필드에 Append

Fix Agent:
appliedFixes 필드에 Append

PM Agent:
finalStatus 필드 Replace

Domain Agent:
자기 domainOutput만 Replace
```

나쁜 Update 방식:

```text
Backend Agent가 sharedRequirements 전체 덮어쓰기
Frontend Agent가 apiContract 임의 변경
Review Agent가 finalOutput 직접 수정
Fix Agent가 reviewFindings 삭제
```

중요한 필드는 versioned update가 적합하다.

---

### [FAQ]

Q. State Update Ownership이 뭐야?
A. 어떤 Agent가 어떤 State 필드를 수정할 수 있는지 정하는 책임 규칙이다.

Q. 왜 State 수정 권한이 필요해?
A. 여러 Agent가 같은 필드를 동시에 덮어써 충돌하는 것을 막기 위해 필요하다.

Q. Review Findings는 어떻게 업데이트해?
A. Review Agent가 Append 방식으로 추가한다.

Q. Current Step은 어떻게 업데이트해?
A. 현재 진행 단계이므로 Replace 방식이 적합하다.

Q. 중요한 결정은 어떻게 업데이트해?
A. Versioned Update로 변경 이력을 남기는 것이 좋다.

---

# 11. Shared State Conflict

## 11.1 Agent 간 State 충돌 처리

### [개념]

Shared State Conflict는 여러 Agent가 서로 다른 기준이나 결과를 Shared State에 반영해 충돌하는 상황이다.

충돌 처리는 Multi-Agent Workflow 안정성의 핵심이다.

```text
Shared State Conflict = Agent 간 공유 상태 불일치
```

---

### [핵심]

충돌 발생 원인:

- Agent가 서로 다른 요구사항을 참조
- apiContract 불일치
- Domain Decision 충돌
- 같은 필드에 동시 Update
- Review Findings 삭제
- 오래된 State 기준 작업
- Local State를 Shared State로 잘못 반영
- Memory와 현재 요청 충돌

충돌 우선순위:

```text
Current User Request
→ Explicit User Correction
→ Latest Project Decision
→ PM Agent Shared Requirements
→ Review Agent Findings
→ Domain Agent Output
→ Long-term Memory
```

---

### [실무]

문제:

```text
Backend Agent:
POST /api/posts 응답은 PostResponse

Frontend Agent:
POST /api/posts 응답은 ApiResponse<PostResponse>
```

원인:

```text
apiContract가 Shared State에 명확히 저장되지 않음
```

해결:

```text
PM Agent가 apiContract 확정
→ Shared State에 반영
→ Backend / Frontend Agent 재작업
→ Review Agent가 Cross-domain Consistency 검토
```

문제:

```text
Review Agent가 발견한 오류를 Fix Agent가 수정 없이 삭제
```

해결:

```text
reviewFindings는 Append-only
→ Fix Agent는 appliedFixes에 수정 결과 기록
→ Review Agent가 passStatus 갱신
```

---

### [FAQ]

Q. Shared State Conflict가 뭐야?
A. 여러 Agent가 서로 다른 기준이나 결과를 Shared State에 반영해 상태가 불일치하는 문제다.

Q. Shared State Conflict는 왜 생겨?
A. 공통 요구사항, API 계약, 결정 사항, 수정 권한이 명확하지 않을 때 발생한다.

Q. 충돌이 생기면 무엇을 우선해?
A. 현재 사용자 요청, 명시적 정정, 최신 프로젝트 결정, PM Agent Shared Requirements 순으로 우선한다.

Q. apiContract 충돌은 어떻게 해결해?
A. PM Agent가 계약을 확정하고 Backend와 Frontend Agent가 그 기준으로 다시 맞춘다.

Q. Review Findings를 삭제해도 돼?
A. 아니다. Review Findings는 Append 방식으로 보존하고 수정 결과는 appliedFixes에 기록한다.

---

# 12. Common Mistakes

## 12.1 Shared State 설계 실수

### [개념]

Shared State 설계 실수는 Multi-Agent Workflow에서 요구사항 누락, Agent 간 충돌, 잘못된 최종 결과를 만든다.

Shared State는 단순 로그가 아니라 Agent 협업의 기준 상태이다.

---

### [핵심]

자주 발생하는 실수:

- Shared State 없이 Agent별 Local State만 사용
- userRequest 원본을 보존하지 않음
- sharedRequirements와 sharedConstraints 누락
- apiContract를 대화 중 임시 텍스트로만 관리
- Review Findings를 덮어쓰기
- Agent Output과 Final Output을 혼동
- Local State 전체를 Shared State에 저장
- State Update Owner를 정하지 않음
- 오래된 State로 Resume
- Memory를 현재 Shared State보다 우선

---

### [실무]

문제:

```text
Review Agent가 검토 기준을 잘못 적용함
```

원인:

```text
Shared State에 reviewCriteria와 sharedRequirements가 없음
```

해결:

```text
PM Agent가 sharedRequirements 정의
→ Review Agent가 reviewCriteria로 사용
→ Review State에 checklistResults 기록
```

문제:

```text
Final Output이 사용자 요청 형식과 다름
```

원인:

```text
deliveryFormat이 Shared State 또는 Final State에 반영되지 않음
```

해결:

```text
Current User Request에서 outputFormat 추출
→ Shared Constraints에 저장
→ Final State에서 deliveryFormat 검증
```

---

### [FAQ]

Q. Shared State 설계에서 가장 흔한 실수는?
A. Shared State 없이 Agent별 Local State만 사용해 Agent 간 기준이 달라지는 것이다.

Q. userRequest 원본을 왜 보존해야 해?
A. 최종 검수 시 현재 사용자 요청을 정확히 기준으로 삼기 위해 필요하다.

Q. Agent Output과 Final Output은 달라?
A. 다르다. Agent Output은 중간 결과이고 Final Output은 PM Agent가 통합한 최종 결과다.

Q. Local State 전체를 Shared State에 넣으면 왜 문제야?
A. Context가 커지고 임시 정보가 공통 사실처럼 오염될 수 있다.

Q. Shared State 설계 핵심은?
A. 공통 요구사항, 제약, 결정, 중간 결과, 검토 상태를 구조화해 관리하는 것이다.

---

# 13. Best Practice

## 13.1 Shared State & Multi-Agent State 설계 원칙

### [개념]

좋은 Shared State 설계는 Agent 간 협업 기준을 명확히 하고, Local State와 Global State를 분리한다.

Multi-Agent System은 상태 공유와 상태 분리를 동시에 잘해야 안정적으로 동작한다.

---

### [핵심]

Best Practice:

- PM Agent가 초기 Shared State를 생성한다.
- userRequest 원본을 보존한다.
- sharedRequirements와 sharedConstraints를 명확히 기록한다.
- Agent별 Local State와 Shared State를 구분한다.
- Local State 전체를 Shared State에 복사하지 않는다.
- 필요한 outputSummary만 Shared State에 반영한다.
- Review Findings는 Append 방식으로 누적한다.
- Current Step과 Status는 Replace 방식으로 갱신한다.
- 중요한 Decision은 Versioned Update로 관리한다.
- apiContract는 Backend / Frontend 연동 기준으로 Shared State에 저장한다.
- State Update Ownership을 정의한다.
- Conflict 발생 시 현재 요청과 최신 결정을 우선한다.
- Final State에서 요구사항 충족 여부를 검증한다.

---

### [실무]

권장 구조:

```text
Global State
├ userRequest
├ workflowId
├ Shared State
│ ├ sharedRequirements
│ ├ sharedConstraints
│ ├ apiContract
│ ├ domainDecisions
│ ├ intermediateOutputs
│ ├ reviewFindings
│ └ finalStatus
├ Agent Local States
│ ├ PM Agent State
│ ├ Backend Agent State
│ ├ Frontend Agent State
│ ├ Review Agent State
│ └ Fix Agent State
└ Final State
  ├ finalOutput
  ├ satisfiedRequirements
  ├ reviewPassStatus
  └ unresolvedIssues
```

권장 Workflow:

```text
PM Agent
→ Create Shared State
→ Assign Domain Agent
→ Domain Agent Updates Output Summary
→ Review Agent Appends Findings
→ Fix Agent Appends Applied Fixes
→ PM Agent Updates Final State
→ Final Output
```

---

### [FAQ]

Q. 좋은 Shared State 설계 기준은?
A. 모든 Agent가 공유해야 할 요구사항, 제약, 결정, 중간 결과, 검토 상태를 구조화하는 것이다.

Q. Shared State에서 가장 중요한 필드는?
A. userRequest, sharedRequirements, sharedConstraints, domainDecisions, intermediateOutputs, reviewFindings, finalStatus가 중요하다.

Q. Multi-Agent State에서 가장 중요한 분리는?
A. Global State, Shared State, Agent Local State, Final State의 분리다.

Q. State Update 방식은 어떻게 정해?
A. Review Findings는 Append, Current Step은 Replace, 중요한 Decision은 Versioned Update가 적합하다.

Q. Shared State 설계의 최종 목표는?
A. 여러 Agent가 같은 기준으로 작업하고 검토하며 일관된 Final Output을 만들게 하는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Shared State가 뭐야?
A. 여러 Agent가 같은 요구사항, 제약, 결정, 중간 결과를 기준으로 작업하기 위해 공유하는 공통 Workflow 상태다.

Q. Shared State는 왜 필요해?
A. Agent마다 다른 기준으로 작업하지 않도록 요구사항과 결정 사항을 통일하기 위해 필요하다.

Q. Shared State에는 무엇을 넣어?
A. userRequest, workflowId, taskPlan, assignedAgents, sharedRequirements, sharedConstraints, intermediateOutputs, reviewStatus, finalStatus를 넣는다.

Q. PM Agent는 Shared State에서 무슨 역할을 해?
A. 사용자 요청을 분석하고 초기 Shared State를 생성하며 Agent별 작업을 분배하고 최종 결과를 통합한다.

Q. Multi-Agent State가 뭐야?
A. 여러 Agent가 참여하는 Workflow에서 전체 상태, 공유 상태, 개별 Agent 상태를 관리하는 구조다.

Q. Global State와 Shared State 차이는?
A. Global State는 전체 Workflow 상태이고, Shared State는 여러 Agent가 함께 참조하는 공통 상태다.

Q. Agent Local State는 뭐야?
A. 개별 Agent가 자기 작업을 수행하는 동안 사용하는 내부 작업 상태다.

Q. Agent Local State를 모두 Shared State에 넣어도 돼?
A. 아니다. 필요한 결과 요약만 Shared State에 반영해야 Context가 커지지 않는다.

Q. PM Agent State는 뭐야?
A. PM Agent가 사용자 요청을 분석하고 Workflow를 계획, 분배, 통합하기 위해 사용하는 상태다.

Q. Domain Agent State는 뭐야?
A. 특정 기술 영역이나 문서 영역을 맡은 Agent가 자기 작업을 수행하기 위해 사용하는 Local State다.

Q. Handoff State가 뭐야?
A. 한 Agent가 다음 Agent에게 작업을 넘길 때 필요한 요약 상태다.

Q. Handoff State에는 무엇을 넣어?
A. taskSummary, completedSteps, pendingSteps, requirements, constraints, decisions, knownIssues, nextAgentInstruction을 넣는다.

Q. Review State가 뭐야?
A. Review Agent가 작업 결과를 검토하며 오류, 누락, 개선 사항, 통과 여부를 기록하는 상태다.

Q. Fix State가 뭐야?
A. Review Findings를 기준으로 수정 작업을 수행하고 수정 결과를 기록하는 상태다.

Q. Final State가 뭐야?
A. Workflow 완료 직전에 최종 결과, 충족 요구사항, 검토 상태, 남은 문제를 정리하는 상태다.

Q. Final State와 Final Output은 같아?
A. 아니다. Final State는 최종 출력 준비 상태이고, Final Output은 사용자에게 전달되는 결과물이다.

Q. State Update Ownership이 뭐야?
A. 어떤 Agent가 어떤 State 필드를 수정할 수 있는지 정하는 책임 규칙이다.

Q. Review Findings는 어떻게 업데이트해?
A. Review Agent가 Append 방식으로 누적하고 Fix Agent는 수정 결과를 appliedFixes에 기록한다.

Q. Shared State Conflict가 뭐야?
A. 여러 Agent가 서로 다른 기준이나 결과를 Shared State에 반영해 상태가 불일치하는 문제다.

Q. Shared State Conflict는 어떻게 해결해?
A. 현재 사용자 요청, 명시적 정정, 최신 프로젝트 결정, PM Agent Shared Requirements 순으로 우선해 해결한다.

Q. apiContract 충돌은 어떻게 해결해?
A. PM Agent가 계약을 확정하고 Backend와 Frontend Agent가 그 기준으로 다시 맞춘다.

Q. Agent Output과 Final Output 차이는?
A. Agent Output은 중간 결과이고 Final Output은 PM Agent가 통합한 사용자 전달 결과다.

Q. Shared State 설계에서 가장 흔한 실수는?
A. Shared State 없이 Agent별 Local State만 사용해 Agent 간 기준이 달라지는 것이다.

Q. Shared State 설계의 핵심은?
A. 공통 요구사항, 제약, 결정, 중간 결과, 검토 상태를 구조화해 관리하는 것이다.

Q. Multi-Agent State 설계의 핵심은?
A. Global State, Shared State, Agent Local State, Review State, Final State를 분리하는 것이다.

Q. 좋은 Shared State Workflow는?
A. PM Agent가 Shared State를 만들고 Domain Agent가 결과를 추가하며 Review Agent가 검토하고 PM Agent가 Final Output을 만든다.
