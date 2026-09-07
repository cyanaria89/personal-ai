# Agent Memory & State Management Part04 - Checkpoint, Resume & Rollback

---

# 1. Checkpoint Foundation

## 1.1 Checkpoint 기본 개념

### [개념]

Checkpoint는 긴 Agent Workflow를 중간 저장하는 기준점이다.

Checkpoint는 작업 실패, 중단, Context 손실, Agent 오류가 발생했을 때 이전 정상 상태에서 Resume할 수 있게 만든다.

```text
Checkpoint = Workflow 중간 저장 지점
```

Checkpoint는 Memory와 다르다.

Memory는 과거 정보 재사용을 위한 저장 정보이고, Checkpoint는 현재 Workflow 복구를 위한 State Snapshot이다.

기본 Flow:

```text
Workflow Running
→ Important Step Completed
→ Save Checkpoint
→ Failure Occurs
→ Load Checkpoint
→ Validate Relevance
→ Resume Workflow
```

---

### [핵심]

- Checkpoint는 긴 Workflow의 복구 지점이다.
- Checkpoint는 State Snapshot을 저장한다.
- Checkpoint는 실패 후 Resume 기준이 된다.
- Checkpoint는 Memory가 아니라 Workflow State 백업이다.
- Checkpoint에는 현재 단계, 완료 단계, 중간 결과, 오류, 다음 작업을 포함한다.
- Checkpoint는 주요 단계 완료 후 저장한다.
- Checkpoint는 최신 사용자 요청과 충돌하는지 검증 후 사용한다.
- Checkpoint에 민감정보를 저장하지 않는다.

---

### [실무]

2026 실무 기준 Multi-Agent System에서는 긴 작업을 Checkpoint 없이 실행하지 않는다.

특히 RAG 문서 제작, 코드 생성, Review/Fix Loop, Agent Workflow 실행은 Checkpoint가 필요하다.

Checkpoint 예시:

```json
{
  "checkpointId": "rag-doc-amsm-part04-cp01",
  "workflowId": "rag-doc-agent-memory-state-management",
  "currentStep": "part04_draft_completed",
  "completedSteps": [
    "Part01 State vs Memory Foundation",
    "Part02 Memory Types",
    "Part03 Shared State & Multi-Agent State"
  ],
  "pendingSteps": [
    "Part04 Review",
    "Part04 Final Output",
    "Part05 State Schema & State Update"
  ],
  "stateSnapshot": {
    "currentTask": "Agent Memory State Management Part04 작성",
    "requirements": [
      "MASTER_RAG_RULES 적용",
      "DOMAIN_RULES 적용",
      "FAQ 강화",
      "Retrieval Queries 포함"
    ],
    "constraints": [
      "writing block document 출력",
      "중간 응답 금지",
      "사람용 문서보다 RAG Retrieval 최적화 우선"
    ],
    "decisions": ["Part04는 Checkpoint, Resume, Rollback 중심으로 작성"]
  },
  "agentOutputs": {
    "domainAgent": "Part04 draft generated"
  },
  "reviewFindings": [],
  "errors": [],
  "resumePoint": "part04_review"
}
```

Checkpoint는 전체 Tool Result나 임시 추론을 모두 저장하지 않는다.

필요한 State만 저장한다.

---

### [FAQ]

Q. Checkpoint가 뭐야?
A. 긴 Workflow 중간 상태를 저장해 실패하거나 중단되었을 때 이어서 진행할 수 있게 하는 저장 지점이다.

Q. Checkpoint는 왜 필요해?
A. Agent 작업이 길어질 때 실패, 중단, 오류 발생 후 이전 정상 상태에서 Resume하기 위해 필요하다.

Q. Checkpoint와 Memory는 같아?
A. 아니다. Checkpoint는 현재 Workflow 복구용 State Snapshot이고, Memory는 과거 정보 재사용용 저장 정보다.

Q. Checkpoint에는 무엇을 저장해?
A. checkpointId, currentStep, completedSteps, pendingSteps, stateSnapshot, agentOutputs, errors, resumePoint를 저장한다.

Q. Checkpoint는 언제 저장해?
A. 주요 단계 완료, Agent Handoff 직전, Review 전후, 위험 작업 전후에 저장한다.

---

# 2. Checkpoint Required Fields

## 2.1 Checkpoint 필수 필드

### [개념]

Checkpoint는 Resume 가능한 구조로 저장해야 한다.

단순 로그나 텍스트 요약만 저장하면 정확한 Workflow 복구가 어렵다.

필수 필드:

```text
checkpointId
workflowId
createdAt
currentStep
stateSnapshot
agentOutputs
toolResults
decisions
errors
resumePoint
```

---

### [핵심]

Checkpoint 필드 기준:

- checkpointId는 Checkpoint 식별자이다.
- workflowId는 어떤 Workflow의 Checkpoint인지 나타낸다.
- createdAt은 저장 시점이다.
- currentStep은 저장 당시 현재 단계이다.
- stateSnapshot은 복구에 필요한 State 요약이다.
- agentOutputs는 Agent별 주요 산출물이다.
- toolResults는 필요한 Tool 결과만 요약 저장한다.
- decisions는 현재까지 확정된 결정이다.
- errors는 발생한 오류와 실패 원인이다.
- resumePoint는 재개 위치이다.

---

### [실무]

권장 Checkpoint Schema:

```json
{
  "checkpointId": "string",
  "workflowId": "string",
  "createdAt": "datetime",
  "currentStep": "string",
  "stateSnapshot": {
    "userRequest": "string",
    "requirements": [],
    "constraints": [],
    "decisions": [],
    "currentStatus": "string"
  },
  "agentOutputs": {
    "pmAgent": {},
    "domainAgent": {},
    "reviewAgent": {},
    "fixAgent": {}
  },
  "toolResults": {
    "summaryOnly": true,
    "results": []
  },
  "decisions": [
    {
      "decision": "string",
      "reason": "string",
      "status": "active"
    }
  ],
  "errors": [
    {
      "step": "string",
      "error": "string",
      "status": "resolved_or_unresolved"
    }
  ],
  "resumePoint": "string"
}
```

Tool Result는 전체 원문보다 필요한 결과만 저장한다.

대용량 로그, 민감정보, 임시 추론 데이터는 Checkpoint에서 제외한다.

---

### [FAQ]

Q. Checkpoint 필수 필드는 뭐야?
A. checkpointId, workflowId, createdAt, currentStep, stateSnapshot, agentOutputs, toolResults, decisions, errors, resumePoint가 필요하다.

Q. stateSnapshot에는 무엇을 넣어?
A. userRequest, requirements, constraints, decisions, currentStatus처럼 복구에 필요한 핵심 State를 넣는다.

Q. toolResults는 전부 저장해?
A. 아니다. Resume에 필요한 핵심 결과만 요약 저장한다.

Q. errors는 왜 저장해?
A. 같은 실패를 반복하지 않고 Resume 전에 원인을 확인하기 위해 필요하다.

Q. resumePoint는 왜 중요해?
A. Workflow를 어느 단계부터 다시 시작할지 결정하는 기준이기 때문이다.

---

# 3. Checkpoint Timing

## 3.1 Checkpoint 저장 시점

### [개념]

Checkpoint Timing은 Workflow 중 언제 중간 저장을 수행할지 정하는 기준이다.

Checkpoint를 너무 적게 저장하면 복구 지점이 부족하고, 너무 자주 저장하면 관리 부담과 Context 비용이 증가한다.

```text
Checkpoint Timing = Workflow 중간 저장 시점 기준
```

---

### [핵심]

Checkpoint 저장 권장 시점:

- 사용자 요청 분석 완료 후
- PM Agent가 Shared State 생성 후
- Domain Agent 작업 완료 후
- Agent Handoff 직전
- Review Agent 검토 완료 후
- Fix Agent 수정 완료 후
- 위험 작업 실행 전
- 외부 Tool 실행 전후
- 긴 문서 Part 완료 후
- Final Output 직전

Checkpoint 저장 비추천 시점:

- 매우 작은 단일 응답 작업
- 임시 후보안이 검증되지 않은 상태
- 민감정보가 포함된 원시 Tool Result 직후
- 사용자가 명시적으로 중단한 작업 직후
- 실패 원인이 정리되지 않은 오류 상태

---

### [실무]

RAG 문서 제작 Workflow Checkpoint 예시:

```text
User Request: Part04 작성
→ CP01: 요구사항 분석 완료
→ CP02: 초안 작성 완료
→ CP03: Master Rules 검수 완료
→ CP04: Domain Rules 검수 완료
→ CP05: Retrieval Queries 검수 완료
→ CP06: Final Output 직전
```

Multi-Agent 개발 Workflow Checkpoint 예시:

```text
PM Planning 완료
→ Backend Agent Output 완료
→ Frontend Agent Output 완료
→ Review Findings 작성 완료
→ Fix Applied 완료
→ Final Integration 완료
```

Checkpoint는 주요 완료 단위 중심으로 저장한다.

---

### [FAQ]

Q. Checkpoint는 언제 저장해?
A. 주요 단계 완료 후, Agent Handoff 전후, Review/Fix 전후, 위험 작업 전후에 저장한다.

Q. Checkpoint를 너무 자주 저장하면?
A. 관리 부담이 커지고 불필요한 State가 많아질 수 있다.

Q. Checkpoint를 너무 적게 저장하면?
A. 실패 후 복구 지점이 부족해 많은 작업을 다시 해야 할 수 있다.

Q. RAG 문서 제작에서는 언제 저장해?
A. 초안 완료, 검수 완료, Retrieval Queries 검수 완료, Final Output 직전에 저장하면 좋다.

Q. 위험 작업 전 Checkpoint가 필요한 이유는?
A. 실패나 Side Effect 발생 시 이전 정상 상태를 확인하고 복구하기 위해 필요하다.

---

# 4. Resume Foundation

## 4.1 Resume 기본 개념

### [개념]

Resume은 중단되거나 실패한 Workflow를 Checkpoint 기준으로 이어가는 과정이다.

Resume은 단순히 이전 상태를 그대로 반복하는 것이 아니다.

현재 사용자 요청, 최신 Memory, Checkpoint 유효성을 검증한 뒤 이어가야 한다.

```text
Resume = Checkpoint 기반 Workflow 재개
```

기본 Flow:

```text
Load Checkpoint
→ Validate Current Relevance
→ Identify Completed Steps
→ Identify Pending Steps
→ Check Errors
→ Update State if Needed
→ Resume Workflow
```

---

### [핵심]

- Resume은 Last Checkpoint에서 시작한다.
- Resume 전 현재 요청과 Checkpoint가 일치하는지 확인한다.
- 완료된 단계와 남은 단계를 구분한다.
- 실패 원인을 확인한다.
- 오래된 Checkpoint는 최신성 검증이 필요하다.
- 현재 사용자 요청이 바뀌면 기존 State를 수정해야 한다.
- Resume은 동일 작업 반복이 아니라 안전한 이어가기이다.

---

### [실무]

Resume State 예시:

```json
{
  "resumeFrom": "rag-doc-amsm-part04-cp03",
  "lastCheckpointStep": "domain_rules_review_completed",
  "completedSteps": ["Draft 작성", "Master Rules 검수", "Domain Rules 검수"],
  "pendingSteps": ["Retrieval Queries 강화", "Final QA", "Final Output"],
  "validationBeforeResume": {
    "currentRequestMatchesCheckpoint": true,
    "rulesStillValid": true,
    "criticalErrorExists": false,
    "userChangedDirection": false
  },
  "resumeAction": "continue_from_retrieval_queries_review"
}
```

Resume 전 검증이 없으면 오래된 State로 잘못된 결과를 만들 수 있다.

---

### [FAQ]

Q. Resume은 뭐야?
A. 마지막 Checkpoint를 기준으로 중단되거나 실패한 Workflow를 이어가는 과정이다.

Q. Resume 전에 무엇을 확인해?
A. 현재 요청과 Checkpoint 일치 여부, 완료 단계, 남은 단계, 오류, 최신성, 방향 변경 여부를 확인한다.

Q. Resume은 이전 상태를 그대로 실행하면 돼?
A. 아니다. 최신 요청과 충돌하는지 검증한 뒤 필요한 State를 수정하고 이어가야 한다.

Q. 오래된 Checkpoint로 Resume해도 돼?
A. 가능하지만 Recency Check와 Conflict Check를 먼저 수행해야 한다.

Q. Resume에서 가장 중요한 것은?
A. 이미 완료된 작업과 남은 작업을 정확히 구분하는 것이다.

---

# 5. Resume Validation

## 5.1 Resume 전 검증 기준

### [개념]

Resume Validation은 Checkpoint를 불러온 뒤 현재 작업에 그대로 사용할 수 있는지 확인하는 과정이다.

Resume Validation이 없으면 오래된 상태, 실패 원인, 변경된 요구사항을 기준으로 작업을 이어갈 수 있다.

```text
Resume Validation = 재개 전 Checkpoint 유효성 검증
```

---

### [핵심]

Resume Validation 필수 확인:

- Current Request Match
- User Correction Check
- Latest Decision Check
- Project Progress Check
- Memory Conflict Check
- Error Status Check
- Completed Steps Check
- Pending Steps Check
- Output Format Check
- Tool Result Validity Check

우선순위:

```text
Current User Request
→ Explicit User Correction
→ Latest Project Decision
→ Last Valid Checkpoint
→ Long-term Memory
```

---

### [실무]

Resume Validation Checklist:

```md
### [Checklist]

- [ ] 현재 사용자 요청과 Checkpoint 목적이 일치하는가?
- [ ] 사용자가 방향을 바꾸지 않았는가?
- [ ] 최신 Project Progress와 충돌하지 않는가?
- [ ] 기존 Memory와 충돌하는 내용이 있는가?
- [ ] 실패 원인이 unresolved 상태로 남아 있지 않은가?
- [ ] 완료된 단계와 남은 단계가 명확한가?
- [ ] 출력 형식이 현재 요청과 일치하는가?
- [ ] Tool Result가 여전히 유효한가?
- [ ] 민감정보가 포함되어 있지 않은가?
```

Resume Action 결정:

```text
Valid Checkpoint → Continue
Minor Conflict → Update State and Continue
Major Conflict → Ask / Replan
Critical Error → Fix First
Outdated Checkpoint → Ignore or Rebuild State
```

RAG 문서 제작에서는 현재 출력 형식과 Domain Rules 최신성이 특히 중요하다.

---

### [FAQ]

Q. Resume Validation이 뭐야?
A. Checkpoint를 불러온 뒤 현재 작업에 그대로 사용할 수 있는지 검증하는 과정이다.

Q. Resume Validation에서 가장 먼저 확인할 것은?
A. 현재 사용자 요청과 Checkpoint 목적이 일치하는지 확인해야 한다.

Q. 최신 사용자 요청과 Checkpoint가 충돌하면?
A. 현재 사용자 요청을 우선하고 Checkpoint State를 수정하거나 재계획한다.

Q. 실패 원인이 남아 있으면 Resume해도 돼?
A. 아니다. 같은 오류 반복을 막기 위해 실패 원인을 먼저 해결해야 한다.

Q. Tool Result는 왜 검증해?
A. 외부 정보나 파일 상태가 바뀌었을 수 있어 그대로 사용하면 오류가 발생할 수 있기 때문이다.

---

# 6. Rollback Foundation

## 6.1 Rollback 기본 개념

### [개념]

Rollback은 잘못된 상태 변경이나 실패한 작업을 이전 정상 상태로 되돌리는 과정이다.

Rollback은 Agent State Rollback과 실제 파일, DB, 이메일, API 호출 같은 Side Effect Rollback을 구분해야 한다.

```text
Rollback = 이전 정상 상태로 되돌리기
```

기본 Flow:

```text
Bad Update
→ Identify Last Valid State
→ Restore State
→ Mark Failed Change
→ Validate Restored State
→ Continue or Stop
```

---

### [핵심]

- Rollback은 잘못된 State Update를 복구한다.
- Last Valid Checkpoint를 기준으로 복구한다.
- 실패한 변경 사항을 기록한다.
- State Rollback과 실제 Side Effect Rollback은 다르다.
- 파일 삭제, DB 변경, 이메일 발송은 단순 State Rollback으로 복구되지 않는다.
- Rollback 전 현재 상태 백업이 필요할 수 있다.
- 위험 작업은 Rollback 가능 여부를 사전에 확인해야 한다.

---

### [실무]

Rollback State 예시:

```json
{
  "rollbackTarget": "rag-doc-amsm-part04-cp04",
  "failedChange": {
    "step": "retrieval_queries_generation",
    "issue": "FAQ 중복 과다 및 Output Format 위반",
    "severity": "high"
  },
  "lastValidState": "domain_rules_review_completed",
  "restorePoint": "rag-doc-amsm-part04-cp03",
  "sideEffects": [],
  "rollbackAction": "restore_state_snapshot",
  "validationAfterRollback": {
    "requirementsRestored": true,
    "formatValid": true,
    "criticalIssueRemoved": true
  }
}
```

실제 Side Effect가 없는 문서 초안 작업은 State Rollback으로 충분할 수 있다.

하지만 파일 저장, DB 변경, 이메일 발송은 별도 복구 절차가 필요하다.

---

### [FAQ]

Q. Rollback은 뭐야?
A. 잘못된 State 업데이트나 실패한 변경을 이전 정상 상태로 되돌리는 작업이다.

Q. Rollback은 Checkpoint와 어떤 관계야?
A. Rollback은 마지막 정상 Checkpoint를 Restore Point로 사용해 상태를 되돌린다.

Q. State Rollback과 실제 파일 Rollback은 같아?
A. 아니다. State Rollback은 Agent 상태 복구이고, 실제 파일이나 DB 변경은 별도 복구가 필요하다.

Q. Rollback 전에 무엇을 확인해?
A. 마지막 정상 상태, 실패한 변경, Side Effect, 복구 가능 여부를 확인한다.

Q. Rollback 후에는 무엇을 해야 해?
A. 복구된 상태가 요구사항을 만족하는지 검증하고 계속 진행할지 중단할지 결정한다.

---

# 7. Rollback Types

## 7.1 Rollback 유형 구분

### [개념]

Rollback은 대상에 따라 여러 유형으로 나눈다.

Rollback 유형을 구분해야 실제 복구 가능 범위와 필요한 조치를 정확히 판단할 수 있다.

```text
Rollback Type = 복구 대상별 Rollback 분류
```

---

### [핵심]

Rollback Types:

- State Rollback
- Memory Rollback
- Document Rollback
- File Rollback
- Database Rollback
- API Side Effect Rollback
- Communication Rollback
- Workflow Rollback

비교:

| Rollback Type            | 대상            | 복구 방식            | 주의                  |
| ------------------------ | --------------- | -------------------- | --------------------- |
| State Rollback           | Agent State     | Checkpoint 복원      | Side Effect 복구 아님 |
| Memory Rollback          | 저장된 Memory   | 이전 Memory 복원     | 충돌 이력 필요        |
| Document Rollback        | 문서 초안       | 이전 Draft 복원      | 변경 이유 기록        |
| File Rollback            | 파일 시스템     | 백업 / 버전관리      | 삭제 복구 주의        |
| Database Rollback        | DB 데이터       | Transaction / Backup | 실제 데이터 손상 주의 |
| API Side Effect Rollback | 외부 API        | 보상 작업            | 취소 불가 가능        |
| Communication Rollback   | 이메일 / 메시지 | 회수 어려움          | 발송 전 확인 필요     |
| Workflow Rollback        | 전체 작업 흐름  | 이전 단계로 복귀     | 완료 단계 중복 주의   |

---

### [실무]

State Rollback 예시:

```text
Review Findings가 실수로 삭제됨
→ Last Valid Checkpoint 확인
→ reviewFindings 복원
→ Fix Agent는 appliedFixes만 갱신
```

Memory Rollback 예시:

```text
임시 아이디어가 Decision Memory로 저장됨
→ Memory 상태를 draft 또는 deprecated로 변경
→ 확정 결정 목록에서 제거
```

File Rollback 예시:

```text
잘못된 md 파일을 덮어씀
→ Git 이전 커밋 또는 백업 파일에서 복구
→ 변경 내역 검토
```

Communication Rollback 예시:

```text
이메일을 잘못 발송함
→ State Rollback으로는 복구 불가
→ 후속 정정 메일 필요
```

---

### [FAQ]

Q. Rollback 유형은 왜 나눠야 해?
A. State 복구와 실제 파일, DB, 외부 API 복구는 방법과 위험이 다르기 때문이다.

Q. State Rollback은 무엇을 복구해?
A. Agent Workflow 상태, Review Findings, Current Step 같은 State 정보를 복구한다.

Q. Memory Rollback은 언제 필요해?
A. 잘못 저장된 Memory, 오래된 결정, 임시 아이디어가 장기 기억에 들어갔을 때 필요하다.

Q. 파일 변경도 State Rollback으로 복구돼?
A. 아니다. 파일 변경은 Git, 백업, 버전 관리로 별도 복구해야 한다.

Q. 이메일 발송은 Rollback 가능해?
A. 일반적으로 발송 후 완전한 Rollback이 어렵기 때문에 발송 전 확인이 중요하다.

---

# 8. Rollback Safety Rules

## 8.1 Rollback 안전 기준

### [개념]

Rollback Safety Rules는 Rollback 과정에서 추가 손상이나 데이터 손실을 막기 위한 기준이다.

Rollback은 복구 작업이지만 잘못 수행하면 정상 상태까지 훼손할 수 있다.

```text
Rollback Safety = 복구 중 추가 손상 방지 기준
```

---

### [핵심]

Rollback 전 확인:

- Last Valid State 존재 여부
- Failed Change 범위
- Side Effect 발생 여부
- Current State 백업 필요 여부
- User Confirmation 필요 여부
- Rollback 후 검증 기준
- 복구 불가능한 작업 여부

Rollback 금지 또는 주의:

- 사용자 승인 없는 실제 파일 삭제 복구
- 사용자 승인 없는 DB 변경 Rollback
- 발송된 이메일을 복구 가능하다고 단정
- 실패 원인 미확인 상태에서 반복 실행
- 민감정보가 포함된 Checkpoint 복원
- 오래된 Checkpoint를 검증 없이 복원

---

### [실무]

Rollback Safety Checklist:

```md
### [Checklist]

- [ ] 마지막 정상 Checkpoint가 확인되었는가?
- [ ] 실패한 변경 사항이 명확한가?
- [ ] 실제 Side Effect가 발생했는가?
- [ ] 현재 상태 백업이 필요한가?
- [ ] 사용자 승인 없이 실제 변경을 되돌리지 않는가?
- [ ] 복구 후 검증 기준이 있는가?
- [ ] 오래된 Checkpoint와 현재 요청이 충돌하지 않는가?
- [ ] 민감정보가 Checkpoint에 포함되지 않았는가?
```

Rollback Decision:

```text
State-only issue → Restore Checkpoint
Document draft issue → Restore Draft or Regenerate
File issue → Use Version Control
DB issue → Transaction / Backup / User Approval
External side effect → Compensation Action
Communication issue → Correction Message
```

---

### [FAQ]

Q. Rollback Safety Rules는 뭐야?
A. Rollback 중 추가 손상이나 데이터 손실을 막기 위한 안전 기준이다.

Q. Rollback 전에 가장 중요한 확인은?
A. 마지막 정상 상태와 실패한 변경 범위를 명확히 확인하는 것이다.

Q. 실제 파일이나 DB도 자동 Rollback해도 돼?
A. 사용자 승인과 복구 계획 없이 자동 Rollback하면 안 된다.

Q. 오래된 Checkpoint를 복원하면 위험해?
A. 최신 사용자 요청이나 프로젝트 결정과 충돌할 수 있어 검증이 필요하다.

Q. Rollback 후 검증은 왜 필요해?
A. 복구된 상태가 실제로 정상인지 확인하지 않으면 같은 오류가 반복될 수 있다.

---

# 9. Checkpoint vs Memory

## 9.1 Checkpoint와 Memory 비교

### [개념]

Checkpoint와 Memory는 모두 정보를 저장하지만 목적이 다르다.

Checkpoint는 현재 Workflow 복구를 위한 State Snapshot이다.

Memory는 과거 정보를 이후 작업에서 재사용하기 위한 저장 정보이다.

```text
Checkpoint = 복구용 현재 상태 저장
Memory = 재사용용 과거 정보 저장
```

---

### [핵심]

| 구분      | Checkpoint                       | Memory                                   |
| --------- | -------------------------------- | ---------------------------------------- |
| 목적      | Workflow 복구                    | 과거 정보 재사용                         |
| 기준      | 현재 작업 상태                   | 장기 맥락 / 선호 / 결정                  |
| 수명      | Workflow 중심                    | 단기 또는 장기                           |
| 예시      | currentStep, resumePoint, errors | project stack, user preference, decision |
| 사용 시점 | 실패, 중단, 재개                 | 문맥 필요 시 Retrieval                   |
| 위험      | 오래되면 잘못 Resume             | 오래되면 잘못된 답변                     |
| 검증      | Resume Validation                | Memory Validation                        |
| 저장 대상 | State Snapshot                   | 재사용 가치 정보                         |

---

### [실무]

Checkpoint로 저장할 것:

```text
- 현재 작업 단계
- 완료된 단계
- 남은 단계
- Review Findings
- Fix Status
- Resume Point
- 오류 상태
```

Memory로 저장할 것:

```text
- 프로젝트 목표
- 기술 스택
- RAG 문서 규칙
- 사용자 출력 선호
- 확정 결정
- 반복 사용 패턴
```

저장하면 안 되는 것:

```text
- API Key
- Password
- Token
- 민감한 개인정보
- 임시 추론 전체
- 불확실한 후보안
```

---

### [FAQ]

Q. Checkpoint와 Memory 차이는?
A. Checkpoint는 현재 Workflow 복구용 State Snapshot이고, Memory는 과거 정보를 재사용하기 위한 저장 정보다.

Q. Checkpoint를 Long-term Memory처럼 써도 돼?
A. 아니다. Checkpoint는 특정 Workflow 복구용이라 장기 지식처럼 사용하면 안 된다.

Q. Memory를 Checkpoint처럼 써도 돼?
A. 아니다. Memory에는 현재 작업 단계와 Resume Point가 없을 수 있어 복구 기준으로 부족하다.

Q. Checkpoint와 Memory 모두 검증이 필요해?
A. 그렇다. Checkpoint는 Resume Validation, Memory는 Recency / Conflict Validation이 필요하다.

Q. 둘 다 저장 금지되는 정보는?
A. API Key, Password, Token, 민감한 개인정보, 불필요한 임시 추론 데이터는 저장하지 않는다.

---

# 10. Resume vs Rollback

## 10.1 Resume과 Rollback 비교

### [개념]

Resume과 Rollback은 모두 Workflow 복구와 관련되지만 목적이 다르다.

Resume은 중단된 Workflow를 이어가는 작업이다.

Rollback은 잘못된 변경을 이전 정상 상태로 되돌리는 작업이다.

```text
Resume = 이어가기
Rollback = 되돌리기
```

---

### [핵심]

| 구분      | Resume                  | Rollback                     |
| --------- | ----------------------- | ---------------------------- |
| 목적      | 중단된 작업 재개        | 잘못된 변경 복구             |
| 시작점    | Last Checkpoint         | Last Valid State             |
| 기준      | 완료 단계 / 남은 단계   | 실패 변경 / 복구 지점        |
| 주요 검증 | 현재 요청과 일치 여부   | Side Effect 여부             |
| 결과      | Workflow 계속 진행      | 이전 정상 상태 복원          |
| 위험      | 오래된 State로 재개     | 정상 변경까지 되돌림         |
| 사용 상황 | 세션 중단, 실패 후 재개 | 오류, 잘못된 수정, 상태 오염 |

---

### [실무]

Resume 예시:

```text
Part04 초안 작성 완료 후 중단
→ 마지막 Checkpoint 확인
→ 검수 단계부터 이어서 진행
```

Rollback 예시:

```text
Part04 검수 중 Retrieval Queries를 잘못 삭제
→ 삭제 전 Checkpoint 확인
→ Retrieval Queries 복원
→ 다시 검수
```

선택 기준:

```text
작업이 멈춤 → Resume
잘못된 변경이 발생 → Rollback
오래된 상태가 문제 → Rebuild State
요구사항이 바뀜 → Replan
```

---

### [FAQ]

Q. Resume과 Rollback 차이는?
A. Resume은 중단된 작업을 이어가는 것이고, Rollback은 잘못된 변경을 이전 정상 상태로 되돌리는 것이다.

Q. 언제 Resume을 사용해?
A. 작업이 중단되었지만 이전 상태가 유효하고 계속 이어갈 수 있을 때 사용한다.

Q. 언제 Rollback을 사용해?
A. 잘못된 수정, 상태 오염, 오류가 발생해 이전 정상 상태로 되돌려야 할 때 사용한다.

Q. Resume 전에 검증할 것은?
A. 현재 요청과 Checkpoint 일치 여부, 완료 단계, 남은 단계, 오류 상태를 확인한다.

Q. Rollback 전에 검증할 것은?
A. 마지막 정상 상태, 실패한 변경, Side Effect, 복구 가능 여부를 확인한다.

---

# 11. Common Mistakes

## 11.1 Checkpoint, Resume, Rollback 실수

### [개념]

Checkpoint, Resume, Rollback 실수는 긴 Agent Workflow에서 반복 작업, 상태 오염, 잘못된 복구를 만든다.

이 영역은 Multi-Agent Workflow 안정성과 직접 연결된다.

---

### [핵심]

자주 발생하는 실수:

- Checkpoint 없이 긴 Workflow 실행
- Checkpoint를 단순 로그처럼 저장
- Resume Point 없이 Checkpoint 저장
- 실패 원인을 기록하지 않음
- 오래된 Checkpoint를 검증 없이 Resume
- 완료 단계와 남은 단계를 구분하지 않음
- Rollback과 Resume을 혼동
- State Rollback으로 실제 파일 변경까지 복구된다고 착각
- Side Effect를 기록하지 않음
- Review Findings를 삭제 방식으로 수정
- 민감정보가 포함된 Checkpoint 저장
- 임시 Working Memory를 Checkpoint에 과도하게 저장

---

### [실무]

문제:

```text
Agent가 중단 후 처음부터 같은 문서를 다시 작성함
```

원인:

```text
Checkpoint와 Resume Point가 없음
```

해결:

```text
Part 완료마다 Checkpoint 저장
→ completedSteps와 pendingSteps 기록
→ resumePoint 기준으로 이어가기
```

문제:

```text
오래된 Checkpoint 기준으로 현재 요청과 다른 형식 출력
```

원인:

```text
Resume Validation 누락
```

해결:

```text
Current User Request 확인
→ Output Format Check
→ Checkpoint State 수정 후 Resume
```

문제:

```text
파일을 삭제했는데 State Rollback으로 복구된다고 판단
```

원인:

```text
State Rollback과 실제 Side Effect Rollback 혼동
```

해결:

```text
Side Effect 기록
→ 파일은 Git / Backup으로 복구
→ State는 별도 복구
```

---

### [FAQ]

Q. Checkpoint 관련 가장 흔한 실수는?
A. Checkpoint 없이 긴 Workflow를 실행하거나 Resume Point 없이 저장하는 것이다.

Q. Resume 관련 가장 흔한 실수는?
A. 오래된 Checkpoint를 현재 요청과 비교하지 않고 그대로 사용하는 것이다.

Q. Rollback 관련 가장 흔한 실수는?
A. State Rollback으로 실제 파일, DB, 이메일 같은 Side Effect까지 복구된다고 착각하는 것이다.

Q. 실패 원인을 기록하지 않으면?
A. Resume 후 같은 오류를 반복할 수 있다.

Q. 해결 핵심은?
A. Checkpoint를 구조화하고, Resume 전 검증하며, Rollback 대상과 Side Effect를 구분하는 것이다.

---

# 12. Troubleshooting

## 12.1 Checkpoint / Resume / Rollback 문제 해결

### [개념]

Troubleshooting은 Checkpoint, Resume, Rollback 과정에서 발생하는 대표 문제를 원인과 해결 기준으로 정리한다.

문제 해결은 상태 복구보다 먼저 원인 식별이 필요하다.

---

### [핵심]

Troubleshooting 형식:

```md
문제:

원인:

해결:
```

주요 문제:

- Checkpoint가 없음
- Resume 후 같은 오류 반복
- Rollback 후 상태가 더 꼬임
- 오래된 Checkpoint로 재개
- Side Effect 복구 실패
- Review Findings 누락
- Final Output 형식 불일치

---

### [실무]

문제:

```text
Checkpoint가 없어 작업을 이어갈 수 없음
```

원인:

```text
주요 단계 완료 후 State Snapshot을 저장하지 않음
```

해결:

```text
현재 Context에서 최소 State 재구성
→ completedSteps / pendingSteps 정리
→ 새 Checkpoint 생성
→ 이후 단계부터 저장 기준 적용
```

문제:

```text
Resume 후 같은 오류가 반복됨
```

원인:

```text
errors 필드와 failureReason을 검토하지 않음
```

해결:

```text
Last Checkpoint의 errors 확인
→ 원인 해결
→ Fix State 기록
→ Resume
```

문제:

```text
Rollback 후 정상 변경까지 사라짐
```

원인:

```text
failedChange 범위를 정확히 식별하지 않음
```

해결:

```text
Last Valid State와 Failed Change 범위 분리
→ 필요한 필드만 선택 복구
→ 복구 후 검증
```

문제:

```text
오래된 Checkpoint로 현재 출력 형식이 깨짐
```

원인:

```text
Current Request Priority 미적용
```

해결:

```text
현재 사용자 요청 우선
→ outputFormat 갱신
→ Checkpoint State 수정
→ Resume
```

문제:

```text
Side Effect 복구가 안 됨
```

원인:

```text
State Rollback과 실제 시스템 변경을 혼동
```

해결:

```text
Side Effect 목록 확인
→ 파일은 버전관리
→ DB는 Transaction / Backup
→ 이메일은 정정 메시지
→ State는 별도 복구
```

---

### [FAQ]

Q. Checkpoint가 없으면 어떻게 해?
A. 현재 Context에서 최소 State를 재구성하고 completedSteps, pendingSteps, nextAction을 정리해 새 Checkpoint를 만든다.

Q. Resume 후 같은 오류가 반복되면?
A. Checkpoint의 errors와 failureReason을 확인하고 원인을 먼저 해결한 뒤 Resume한다.

Q. Rollback 후 상태가 더 꼬이면?
A. failedChange 범위를 다시 식별하고 마지막 정상 State에서 필요한 필드만 선택 복구한다.

Q. 오래된 Checkpoint가 현재 요청과 다르면?
A. 현재 요청을 우선해 State를 수정하거나 Checkpoint를 폐기하고 재구성한다.

Q. Side Effect 복구 실패는 어떻게 처리해?
A. State Rollback과 실제 복구를 분리하고 파일, DB, 외부 API, 이메일별 복구 방식을 적용한다.

---

# 13. Best Practice

## 13.1 Checkpoint, Resume, Rollback 설계 원칙

### [개념]

좋은 Checkpoint, Resume, Rollback 설계는 긴 Agent Workflow를 안정적으로 이어가고 잘못된 상태를 안전하게 복구한다.

복구 가능한 Agent Workflow는 State를 구조화하고 주요 지점마다 Snapshot을 남긴다.

---

### [핵심]

Best Practice:

- 긴 Workflow에는 Checkpoint를 사용한다.
- Checkpoint는 주요 단계 완료 후 저장한다.
- Checkpoint에는 resumePoint를 반드시 포함한다.
- completedSteps와 pendingSteps를 구분한다.
- errors와 failureReason을 기록한다.
- Tool Result는 필요한 핵심만 요약 저장한다.
- 민감정보와 Secret은 Checkpoint에 저장하지 않는다.
- Resume 전 Validation을 수행한다.
- 현재 사용자 요청을 Checkpoint보다 우선한다.
- 오래된 Checkpoint는 Recency Check 후 사용한다.
- Rollback 전 Last Valid State를 확인한다.
- State Rollback과 Side Effect Rollback을 구분한다.
- 실제 파일, DB, 이메일 작업은 별도 복구 절차를 둔다.
- Rollback 후 Validation을 수행한다.
- Review Findings는 삭제하지 않고 Fix 결과와 연결한다.

---

### [실무]

권장 Workflow:

```text
PM Agent creates Shared State
→ Checkpoint CP01
→ Domain Agent completes output
→ Checkpoint CP02
→ Review Agent adds findings
→ Checkpoint CP03
→ Fix Agent applies fixes
→ Checkpoint CP04
→ Final State validation
→ Checkpoint CP05
→ Final Output
```

권장 Resume Flow:

```text
Load Last Checkpoint
→ Current Request Match
→ Completed / Pending Steps Check
→ Error Check
→ Conflict Check
→ State Update
→ Continue
```

권장 Rollback Flow:

```text
Detect Bad Update
→ Identify Failed Change
→ Identify Last Valid Checkpoint
→ Check Side Effect
→ Restore State
→ Validate
→ Continue or Stop
```

RAG 문서 제작에서는 Part 단위 Checkpoint가 유용하다.

Multi-Agent 개발에서는 Agent Handoff 단위 Checkpoint가 유용하다.

---

### [FAQ]

Q. 좋은 Checkpoint 설계 기준은?
A. 주요 단계 완료 시 State Snapshot, 완료 단계, 남은 단계, 오류, resumePoint를 구조화해 저장하는 것이다.

Q. 좋은 Resume 설계 기준은?
A. 현재 요청과 Checkpoint 일치 여부를 검증하고 완료 단계와 남은 단계를 구분해 이어가는 것이다.

Q. 좋은 Rollback 설계 기준은?
A. 실패한 변경과 마지막 정상 상태를 분리하고 Side Effect 여부를 확인한 뒤 복구하는 것이다.

Q. Checkpoint 저장의 핵심은?
A. 나중에 정확히 이어갈 수 있도록 resumePoint와 필요한 State를 남기는 것이다.

Q. Checkpoint, Resume, Rollback의 최종 목표는?
A. 긴 Agent Workflow를 중단, 실패, 오류 이후에도 안전하고 일관되게 이어가게 만드는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Checkpoint가 뭐야?
A. 긴 Workflow 중간 상태를 저장해 실패하거나 중단되었을 때 이어서 진행할 수 있게 하는 저장 지점이다.

Q. Checkpoint는 왜 필요해?
A. Agent 작업이 길어질 때 실패, 중단, 오류 발생 후 이전 정상 상태에서 Resume하기 위해 필요하다.

Q. Checkpoint와 Memory 차이는?
A. Checkpoint는 현재 Workflow 복구용 State Snapshot이고, Memory는 과거 정보를 재사용하기 위한 저장 정보다.

Q. Checkpoint에는 무엇을 저장해?
A. checkpointId, workflowId, currentStep, stateSnapshot, agentOutputs, toolResults, decisions, errors, resumePoint를 저장한다.

Q. Checkpoint는 언제 저장해?
A. 주요 단계 완료 후, Agent Handoff 전후, Review/Fix 전후, 위험 작업 전후에 저장한다.

Q. Resume은 뭐야?
A. 마지막 Checkpoint를 기준으로 중단되거나 실패한 Workflow를 이어가는 과정이다.

Q. Resume 전에 무엇을 확인해?
A. 현재 요청과 Checkpoint 일치 여부, 완료 단계, 남은 단계, 오류, 최신성, 방향 변경 여부를 확인한다.

Q. Resume Validation이 뭐야?
A. Checkpoint를 불러온 뒤 현재 작업에 그대로 사용할 수 있는지 검증하는 과정이다.

Q. 오래된 Checkpoint로 Resume해도 돼?
A. 가능하지만 Recency Check와 Conflict Check를 먼저 수행해야 한다.

Q. Resume에서 가장 중요한 것은?
A. 이미 완료된 작업과 남은 작업을 정확히 구분하는 것이다.

Q. Rollback은 뭐야?
A. 잘못된 State 업데이트나 실패한 변경을 이전 정상 상태로 되돌리는 작업이다.

Q. Rollback은 Checkpoint와 어떤 관계야?
A. Rollback은 마지막 정상 Checkpoint를 Restore Point로 사용해 상태를 되돌린다.

Q. State Rollback과 실제 파일 Rollback은 같아?
A. 아니다. State Rollback은 Agent 상태 복구이고 실제 파일, DB, 이메일 변경은 별도 복구가 필요하다.

Q. Rollback 전에 무엇을 확인해?
A. 마지막 정상 상태, 실패한 변경, Side Effect, 복구 가능 여부를 확인한다.

Q. Rollback 후에는 무엇을 해야 해?
A. 복구된 상태가 요구사항을 만족하는지 검증하고 계속 진행할지 중단할지 결정한다.

Q. Rollback 유형은 뭐가 있어?
A. State Rollback, Memory Rollback, Document Rollback, File Rollback, Database Rollback, API Side Effect Rollback, Communication Rollback, Workflow Rollback이 있다.

Q. Memory Rollback은 언제 필요해?
A. 잘못 저장된 Memory, 오래된 결정, 임시 아이디어가 장기 기억에 들어갔을 때 필요하다.

Q. 파일 변경도 State Rollback으로 복구돼?
A. 아니다. 파일 변경은 Git, 백업, 버전 관리로 별도 복구해야 한다.

Q. 이메일 발송은 Rollback 가능해?
A. 일반적으로 발송 후 완전한 Rollback이 어렵기 때문에 발송 전 확인이 중요하다.

Q. Resume과 Rollback 차이는?
A. Resume은 중단된 작업을 이어가는 것이고, Rollback은 잘못된 변경을 이전 정상 상태로 되돌리는 것이다.

Q. 언제 Resume을 사용해?
A. 작업이 중단되었지만 이전 상태가 유효하고 계속 이어갈 수 있을 때 사용한다.

Q. 언제 Rollback을 사용해?
A. 잘못된 수정, 상태 오염, 오류가 발생해 이전 정상 상태로 되돌려야 할 때 사용한다.

Q. Checkpoint가 없으면 어떻게 해?
A. 현재 Context에서 최소 State를 재구성하고 completedSteps, pendingSteps, nextAction을 정리해 새 Checkpoint를 만든다.

Q. Resume 후 같은 오류가 반복되면?
A. Checkpoint의 errors와 failureReason을 확인하고 원인을 먼저 해결한 뒤 Resume한다.

Q. Side Effect 복구 실패는 어떻게 처리해?
A. State Rollback과 실제 복구를 분리하고 파일, DB, 외부 API, 이메일별 복구 방식을 적용한다.

Q. Checkpoint 설계의 핵심은?
A. 나중에 정확히 이어갈 수 있도록 resumePoint와 필요한 State를 구조화해 남기는 것이다.

Q. Checkpoint, Resume, Rollback의 최종 목표는?
A. 긴 Agent Workflow를 중단, 실패, 오류 이후에도 안전하고 일관되게 이어가게 만드는 것이다.
