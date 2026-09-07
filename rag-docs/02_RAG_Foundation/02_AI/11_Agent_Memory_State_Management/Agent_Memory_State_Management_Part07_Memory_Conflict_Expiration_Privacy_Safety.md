# Agent Memory & State Management Part07 - Memory Conflict, Memory Expiration & Privacy / Safety

---

# 1. Memory Conflict Foundation

## 1.1 Memory Conflict 기본 개념

### [개념]

Memory Conflict는 서로 다른 Memory, 현재 요청, 최근 결정, 과거 정보가 충돌하는 상황이다.

Memory Conflict는 Agent가 오래된 정보와 최신 요청을 동시에 참조할 때 자주 발생한다.

```text
Memory Conflict = 서로 다른 기억이나 현재 요청이 충돌하는 상태
```

Memory Conflict는 자동으로 섞어 해결하지 않는다.

우선순위 규칙을 적용해 하나의 기준을 선택하거나, 필요한 경우 Memory를 Update / Deprecate / Ignore 처리한다.

기본 Flow:

```text
Retrieve Memory
→ Detect Conflict
→ Identify Conflict Type
→ Apply Priority Rule
→ Resolve Conflict
→ Update State
→ Optional Memory Update
```

---

### [핵심]

- Memory Conflict는 오래된 Memory와 최신 정보가 다를 때 발생한다.
- 현재 사용자 요청이 가장 우선한다.
- 명시적 사용자 정정은 기존 Memory를 덮어쓴다.
- 최신 프로젝트 결정은 오래된 Decision Memory보다 우선한다.
- 충돌 Memory를 임의로 조합하지 않는다.
- 충돌 해결 결과는 State에 명확히 반영한다.
- 오래된 Memory는 deprecated 처리할 수 있다.
- 불확실하면 단정하지 않고 확인 또는 보수적 사용을 한다.

---

### [실무]

2026 실무 기준 Agent는 Memory Conflict를 추론으로 뭉개지 않고 구조적으로 처리한다.

예시:

```json
{
  "conflictType": "project_progress_conflict",
  "oldMemory": "Agent Memory & State Management는 Planned 상태",
  "newInformation": "Part07 작성 진행 중",
  "priorityRule": "Current User Request > Project Progress",
  "resolution": "현재 작업 기준으로 in_progress 처리",
  "memoryAction": "update_or_deprecate_old_progress"
}
```

예시:

```json
{
  "conflictType": "output_format_conflict",
  "oldMemory": "일반 Markdown 출력",
  "newInformation": "writing block document 형식으로 최종 결과만 출력",
  "priorityRule": "Current User Request",
  "resolution": "writing block document 형식 적용",
  "memoryAction": "update_user_preference_memory"
}
```

Conflict 해결은 현재 작업 정확도를 높이고 오래된 Memory 오염을 막는다.

---

### [FAQ]

Q. Memory Conflict가 뭐야?
A. 서로 다른 Memory, 현재 요청, 최근 결정, 과거 정보가 충돌하는 상황이다.

Q. Memory Conflict는 왜 생겨?
A. 프로젝트 진행 상황, 사용자 선호, 결정 사항이 시간이 지나며 바뀌기 때문이다.

Q. 충돌 Memory를 섞어서 결론 내도 돼?
A. 아니다. 우선순위 규칙으로 해결하고 임의 조합은 피한다.

Q. Memory Conflict에서 가장 우선하는 것은?
A. 현재 사용자 요청과 명시적 사용자 정정이다.

Q. 충돌 해결 후 무엇을 해야 해?
A. State에 해결 결과를 반영하고 필요하면 오래된 Memory를 update 또는 deprecate 처리한다.

---

# 2. Conflict Priority Rules

## 2.1 Memory Conflict 우선순위

### [개념]

Conflict Priority Rules는 충돌하는 Memory 중 어떤 정보를 우선할지 정하는 기준이다.

우선순위가 없으면 Agent가 오래된 Memory를 현재 요청보다 우선하거나, 서로 다른 정보를 임의로 섞을 수 있다.

```text
Conflict Priority Rules = 충돌 정보 해결 우선순위
```

기본 우선순위:

```text
Current User Request
→ Explicit User Correction
→ Latest Project Decision
→ Recent Conversation
→ Active Project Progress
→ Domain Rules
→ Long-term Memory
→ Old Summary
→ Inferred Memory
```

---

### [핵심]

우선순위 기준:

- 현재 사용자 요청은 최우선이다.
- 명시적 사용자 정정은 기존 Memory를 덮어쓴다.
- 최신 프로젝트 결정은 이전 결정 Memory보다 우선한다.
- 최근 대화는 오래된 Long-term Memory보다 우선한다.
- Domain Rules는 문서 제작 기준으로 사용한다.
- Long-term Memory는 검증 후 사용한다.
- 추정 Memory는 낮은 우선순위로 처리한다.
- 민감정보는 우선순위와 관계없이 저장하거나 사용하지 않는다.

---

### [실무]

Conflict Resolution 예시:

```json
{
  "oldMemory": "총 6파트 구성",
  "recentDecision": "총 8파트 구성",
  "currentRequest": "다음",
  "resolution": "총 8파트 기준 Part07 작성",
  "priorityApplied": "Latest Project Decision"
}
```

Conflict Resolution 예시:

```json
{
  "oldPreference": "짧게 설명",
  "currentRequest": "RAG 문서 형식으로 작성",
  "resolution": "상세 RAG 문서 작성",
  "priorityApplied": "Current User Request"
}
```

Conflict Resolution 예시:

```json
{
  "oldDecision": "Agent와 문서를 섞어 관리",
  "latestDecision": "Agent와 문서는 분리 관리",
  "resolution": "분리 관리 기준 사용",
  "memoryAction": "oldDecision deprecated"
}
```

우선순위 적용 후에는 active 기준을 State에 반영한다.

---

### [FAQ]

Q. Memory Conflict 우선순위는?
A. Current User Request, Explicit User Correction, Latest Project Decision, Recent Conversation, Active Project Progress, Domain Rules, Long-term Memory 순서다.

Q. 현재 요청과 Long-term Memory가 충돌하면?
A. 현재 요청을 우선한다.

Q. 최신 결정과 오래된 결정이 충돌하면?
A. 최신 프로젝트 결정을 우선하고 오래된 결정은 deprecated 처리한다.

Q. 추정 Memory는 어떻게 처리해?
A. 낮은 신뢰도로 다루고 확정 사실처럼 사용하지 않는다.

Q. 우선순위 적용 후 무엇을 해야 해?
A. 해결된 기준을 State에 반영하고 필요한 Memory Update를 수행한다.

---

# 3. Conflict Types

## 3.1 Memory Conflict 유형

### [개념]

Memory Conflict는 충돌 원인에 따라 유형을 나눌 수 있다.

Conflict Type을 구분하면 해결 방식과 Memory Update 방식을 명확히 정할 수 있다.

```text
Conflict Type = Memory 충돌 원인별 분류
```

---

### [핵심]

주요 Conflict Types:

- Current Request vs Long-term Memory
- User Correction vs Old Memory
- Latest Decision vs Old Decision
- Project Progress vs Old Progress
- Domain Rules vs Generated Output
- User Preference vs Current Instruction
- Working Memory vs Decision Memory
- Project Memory Scope Conflict
- Tool Result vs Stored Memory
- Summary vs Original Decision
- Sensitive Data vs Memory Policy

---

### [실무]

Conflict Type 예시:

| Conflict Type                       | 예시                                       | 해결 기준              |
| ----------------------------------- | ------------------------------------------ | ---------------------- |
| Current Request vs Long-term Memory | 현재는 writing block, 과거는 일반 Markdown | 현재 요청 우선         |
| User Correction vs Old Memory       | 사용자가 “그건 아니야”라고 정정            | 명시적 정정 우선       |
| Latest Decision vs Old Decision     | 8파트 확정, 과거 6파트                     | 최신 결정 우선         |
| Project Progress vs Old Progress    | Part07 진행 중, 과거 Planned               | 현재 진행 상태 우선    |
| Domain Rules vs Output              | FAQ 누락                                   | Domain Rules 기준 수정 |
| Preference vs Instruction           | 짧게 선호하지만 상세 문서 요청             | 현재 지시 우선         |
| Working vs Decision                 | 후보안을 확정처럼 저장                     | Working Memory로 유지  |
| Scope Conflict                      | 웹 프로젝트 Memory가 RAG 문서에 섞임       | Project Scope 필터링   |
| Sensitive Data Conflict             | API Key 저장 후보                          | 저장 금지              |

Conflict 유형별 처리 예시:

```json
{
  "conflictType": "working_memory_vs_decision_memory",
  "issue": "검토 전 후보안이 확정 결정처럼 저장됨",
  "resolution": "candidate는 Working Memory로 유지하고 Decision Memory 저장 금지",
  "memoryAction": "ignore_as_decision"
}
```

---

### [FAQ]

Q. Memory Conflict Type은 왜 나눠?
A. 충돌 원인에 따라 해결 방식과 Memory Update 방식이 다르기 때문이다.

Q. User Preference와 Current Instruction이 충돌하면?
A. 현재 지시를 우선한다.

Q. Working Memory와 Decision Memory가 충돌하면?
A. 검토 전 후보안은 Decision Memory로 저장하지 않는다.

Q. Project Scope Conflict는 뭐야?
A. 다른 프로젝트 Memory가 현재 프로젝트 답변에 섞이는 문제다.

Q. Sensitive Data Conflict는 어떻게 처리해?
A. 민감정보 저장 정책을 우선하고 Memory 저장을 금지한다.

---

# 4. Conflict Resolution Flow

## 4.1 Memory Conflict 해결 절차

### [개념]

Conflict Resolution Flow는 충돌 Memory를 발견했을 때 해결하는 표준 절차이다.

충돌 정보는 감으로 선택하지 않고 단계적으로 검증한다.

```text
Conflict Resolution Flow = Memory 충돌 해결 절차
```

---

### [핵심]

Conflict Resolution Flow:

```text
Detect Conflict
→ Identify Sources
→ Identify Conflict Type
→ Compare Recency
→ Apply Priority Rule
→ Decide Resolution
→ Update Current State
→ Update / Deprecate / Ignore Memory
→ Validate Output
```

Resolution Actions:

- Use Current Request
- Use Latest Decision
- Update Old Memory
- Deprecate Old Memory
- Ignore Irrelevant Memory
- Delete Unsafe Memory
- Ask if High Risk
- Rebuild State

---

### [실무]

Conflict Resolution State 예시:

```json
{
  "conflictId": "MC-001",
  "detectedAt": "memory_retrieval",
  "sources": {
    "oldMemory": "Project Progress: Planned",
    "currentContext": "Part07 작성 요청"
  },
  "conflictType": "project_progress_conflict",
  "priorityApplied": "Current User Request",
  "resolution": "Part07 in_progress 기준 사용",
  "stateUpdate": {
    "currentTask": "Part07 Memory Conflict, Expiration, Privacy / Safety 작성",
    "status": "in_progress"
  },
  "memoryAction": "mark_old_progress_outdated"
}
```

High Risk Conflict 예시:

```json
{
  "conflictId": "MC-002",
  "conflictType": "privacy_safety_conflict",
  "memory": "API Key 저장 후보",
  "priorityApplied": "Privacy / Safety Rules",
  "resolution": "저장 금지",
  "memoryAction": "delete_or_redact"
}
```

Conflict Resolution은 Final Output 전에 검증해야 한다.

---

### [FAQ]

Q. Memory Conflict는 어떻게 해결해?
A. 출처, 충돌 유형, 최신성, 우선순위를 확인한 뒤 해결 기준을 State에 반영한다.

Q. 충돌 해결 Action은 뭐가 있어?
A. Use Current Request, Use Latest Decision, Update, Deprecate, Ignore, Delete, Rebuild State가 있다.

Q. High Risk Conflict는 뭐야?
A. 민감정보, 실제 파일 변경, DB 변경, 보안 정책처럼 잘못 처리하면 피해가 큰 충돌이다.

Q. High Risk Conflict는 어떻게 처리해?
A. 안전 규칙을 우선하고 필요한 경우 사용자 확인 또는 저장 금지를 적용한다.

Q. Conflict Resolution 후 검증이 필요한 이유는?
A. 해결 결과가 Final Output과 State에 일관되게 반영되었는지 확인하기 위해 필요하다.

---

# 5. Memory Expiration Foundation

## 5.1 Memory Expiration 기본 개념

### [개념]

Memory Expiration은 Memory가 시간이 지나 더 이상 active 기준으로 사용되면 안 되는 상태를 관리하는 기준이다.

모든 Memory가 영구적으로 유효한 것은 아니다.

```text
Memory Expiration = 오래되거나 유효하지 않은 Memory를 만료 또는 갱신하는 기준
```

Memory Expiration은 삭제만 의미하지 않는다.

Memory는 active, deprecated, archived, expired 상태로 관리할 수 있다.

---

### [핵심]

- Memory는 시간이 지나면 틀릴 수 있다.
- 진행 상태 Memory는 자주 갱신해야 한다.
- 기술 버전 Memory는 최신성 검증이 필요하다.
- 프로젝트 결정은 변경되면 이전 결정을 deprecated 처리한다.
- 오래된 Summary는 최신 대화로 갱신한다.
- 만료된 Memory를 현재 사실처럼 사용하지 않는다.
- Expiration은 삭제, 보관, 비활성화, 갱신으로 처리할 수 있다.

---

### [실무]

Memory Status 예시:

```text
active
deprecated
archived
expired
deleted
```

Status 의미:

| Status     | 의미                              | 사용 기준             |
| ---------- | --------------------------------- | --------------------- |
| active     | 현재 유효                         | 기본 사용 가능        |
| deprecated | 과거에는 유효했지만 현재는 비활성 | 참고만 가능           |
| archived   | 기록 보관                         | 검색 우선순위 낮음    |
| expired    | 유효기간 만료                     | 현재 사실로 사용 금지 |
| deleted    | 삭제됨                            | 사용 금지             |

Memory Expiration 예시:

```json
{
  "memory": "Agent Memory & State Management는 Planned",
  "oldStatus": "active",
  "newStatus": "deprecated",
  "reason": "Part07 작성 진행으로 상태 변경",
  "replacement": "Agent Memory & State Management Part01~Part07 진행"
}
```

---

### [FAQ]

Q. Memory Expiration이 뭐야?
A. 오래되거나 더 이상 유효하지 않은 Memory를 만료, 보관, 비활성화, 갱신하는 기준이다.

Q. 모든 Memory는 영구적으로 유지해도 돼?
A. 아니다. 진행 상태, 버전 정보, 임시 결정은 시간이 지나면 갱신 또는 만료가 필요하다.

Q. deprecated Memory는 삭제된 거야?
A. 아니다. 현재 기준으로 사용하지 않지만 과거 기록으로 참고할 수 있는 상태다.

Q. expired Memory는 사용할 수 있어?
A. 현재 사실로 사용하면 안 된다.

Q. Memory Expiration의 핵심은?
A. 오래된 Memory를 현재 사실처럼 사용하지 않게 만드는 것이다.

---

# 6. Expiration Targets

## 6.1 만료 또는 갱신 대상 Memory

### [개념]

Expiration Targets는 시간이 지나면 정확도가 떨어져 주기적으로 갱신하거나 만료해야 하는 Memory이다.

모든 Memory가 같은 만료 기준을 가지지 않는다.

```text
Expiration Targets = 만료 또는 갱신이 필요한 Memory 유형
```

---

### [핵심]

만료 또는 갱신 대상:

- Project Progress
- Pending Tasks
- Current Roadmap
- Technical Stack Version
- Agent Architecture
- Folder Structure
- API Contract
- Tool Result
- External Facts
- User Temporary Preference
- Conversation Summary
- Checkpoint
- Workflow State
- Draft Decision

상대적으로 오래 유지 가능한 Memory:

- Project Goal
- Stable User Preference
- Core RAG Document Rules
- Confirmed Architecture Decision
- Naming Rule
- Safety Rule
- Domain Concept Rule

---

### [실무]

Expiration 기준 예시:

| Memory               | Expiration 기준         | 처리                   |
| -------------------- | ----------------------- | ---------------------- |
| Project Progress     | 작업 완료 / 변경 시     | update                 |
| Pending Tasks        | 완료 / 취소 시          | update / archive       |
| Technical Version    | 버전 변경 시            | recency check          |
| API Contract         | 계약 변경 시            | versioned update       |
| Tool Result          | 외부 상태 변경 가능성   | revalidate             |
| Conversation Summary | 대화 길어짐 / 방향 변경 | refresh                |
| Checkpoint           | 요구사항 변경 / 오래됨  | validate before resume |
| Draft Decision       | 확정 안 됨              | keep draft / ignore    |
| Safety Rule          | 안정적                  | active 유지            |

Expiration Metadata 예시:

```json
{
  "key": "project_progress",
  "value": "Part01~Part07 진행",
  "status": "active",
  "updatedAt": "2026-07-01",
  "expiresOnCondition": ["Part08 completed", "project roadmap changed"],
  "refreshRequired": true
}
```

---

### [FAQ]

Q. 어떤 Memory가 만료 대상이야?
A. Project Progress, Pending Tasks, 기술 버전, API Contract, Tool Result, Conversation Summary, Checkpoint가 대표적이다.

Q. 어떤 Memory는 오래 유지 가능해?
A. 프로젝트 목표, 안정적인 사용자 선호, 핵심 RAG 규칙, 확정 Architecture Decision은 비교적 오래 유지 가능하다.

Q. Pending Task는 언제 갱신해?
A. 작업이 완료, 취소, 보류되었을 때 갱신한다.

Q. Tool Result는 왜 만료 대상이야?
A. 외부 상태나 파일 상태가 바뀔 수 있기 때문이다.

Q. Checkpoint는 만료돼?
A. 오래되거나 요구사항이 바뀌면 Resume 전 검증이 필요하며 사실상 만료될 수 있다.

---

# 7. Memory Refresh Rules

## 7.1 Memory 갱신 기준

### [개념]

Memory Refresh는 기존 Memory를 최신 상태로 갱신하는 과정이다.

Memory Refresh는 오래된 Memory를 삭제하는 것이 아니라 최신 정보로 대체하거나 버전 관리하는 작업이다.

```text
Memory Refresh = 기존 Memory를 최신 상태로 갱신
```

---

### [핵심]

Refresh가 필요한 경우:

- 사용자가 기존 정보를 정정함
- 프로젝트 진행 상태가 바뀜
- 문서 Part가 완료됨
- 기술 스택이 변경됨
- 폴더 구조가 변경됨
- 최신 결정이 이전 결정을 대체함
- Summary가 오래됨
- Checkpoint가 현재 요청과 맞지 않음

Refresh 방식:

- Replace
- Merge
- Versioned Update
- Deprecate Old Memory
- Archive Old Memory
- Rebuild Summary

---

### [실무]

Project Progress Refresh 예시:

```json
{
  "memoryType": "project_memory",
  "key": "agent_memory_state_management_progress",
  "before": "Part01~Part06 완료",
  "after": "Part01~Part07 완료, Part08 예정",
  "updateType": "replace",
  "reason": "Part07 작성 완료"
}
```

Decision Refresh 예시:

```json
{
  "memoryType": "decision_memory",
  "key": "part_count",
  "versions": [
    {
      "version": 1,
      "value": "총 6파트",
      "status": "deprecated"
    },
    {
      "version": 2,
      "value": "총 8파트",
      "status": "active"
    }
  ],
  "updateType": "versioned_update"
}
```

Summary Refresh 예시:

```text
Old Summary:
Part01~Part04 완료

New Summary:
Part01~Part07 완료, Part08 LangGraph State / Troubleshooting / Final Best Practice 예정
```

---

### [FAQ]

Q. Memory Refresh가 뭐야?
A. 기존 Memory를 최신 상태로 갱신하는 과정이다.

Q. Refresh는 언제 해?
A. 사용자가 정정했거나 프로젝트 진행 상태, 기술 스택, 문서 구조, 결정 사항이 바뀌었을 때 한다.

Q. Refresh와 Delete는 달라?
A. 다르다. Refresh는 최신 정보로 갱신하는 것이고 Delete는 Memory를 제거하는 것이다.

Q. 결정이 바뀌면 어떻게 Refresh해?
A. Versioned Update로 이전 결정을 deprecated 처리하고 최신 결정을 active로 둔다.

Q. Summary가 오래되면?
A. 핵심 결정, 진행 상태, 다음 작업 기준으로 Rebuild Summary를 수행한다.

---

# 8. Privacy / Safety Foundation

## 8.1 Memory Privacy & Safety 기본 개념

### [개념]

Memory Privacy & Safety는 Memory와 State에 민감정보, Secret, 개인정보, 위험한 정보가 저장되지 않도록 관리하는 기준이다.

Agent Memory는 장기적으로 재사용되므로 잘못 저장된 민감정보는 반복 노출 위험을 만든다.

```text
Memory Privacy / Safety = 민감정보와 Secret 저장 방지 기준
```

---

### [핵심]

저장 금지 또는 강한 주의 대상:

- API Key
- Password
- Access Token
- Refresh Token
- Session Cookie
- Private Key
- 주민번호
- 계좌번호
- 카드번호
- 정확한 주소
- 인증 코드
- 민감한 개인 속성
- 의료 / 법률 / 금융 민감정보
- 사적인 대화 원문
- 회사 내부 비밀
- 보안 취약점 악용 정보

원칙:

- Secret은 Memory에 저장하지 않는다.
- 민감정보는 명시적 요청 없이는 저장하지 않는다.
- 사용자가 잊어달라고 하면 삭제해야 한다.
- Tool Result에 민감정보가 포함될 수 있으므로 Redaction이 필요하다.
- Config와 Secret을 구분한다.
- 로그와 Checkpoint에도 Secret을 남기지 않는다.

---

### [실무]

안전한 Memory 예시:

```json
{
  "type": "project_memory",
  "key": "ai_stack",
  "value": "AnythingLLM + Ollama + Qwen2.5 + BGE-M3",
  "sensitivity": "safe",
  "status": "active"
}
```

저장 금지 예시:

```json
{
  "type": "secret",
  "key": "OPENAI_API_KEY",
  "value": "sk-...",
  "sensitivity": "secret",
  "action": "do_not_store_redact"
}
```

Redaction 예시:

```text
원본:
OPENAI_API_KEY=sk-abc123...

저장 가능 형태:
OPENAI_API_KEY is configured in environment variable.
Actual key value is not stored.
```

Privacy / Safety는 Memory Update보다 우선한다.

---

### [FAQ]

Q. Memory Privacy / Safety가 뭐야?
A. Memory와 State에 민감정보, Secret, 개인정보가 저장되지 않도록 관리하는 기준이다.

Q. API Key를 Memory에 저장해도 돼?
A. 안 된다. API Key, Password, Token, Cookie, Private Key는 저장하지 않는다.

Q. Config 정보는 저장해도 돼?
A. Secret 값이 아닌 일반 설정 구조나 사용 여부는 저장할 수 있다.

Q. Tool Result에 민감정보가 있으면?
A. 저장 전에 Redaction하고 원문 값은 Memory에 남기지 않는다.

Q. Privacy / Safety의 핵심은?
A. 장기 Memory와 State에 민감정보가 반복 노출되지 않게 하는 것이다.

---

# 9. Sensitive Information Rules

## 9.1 민감정보 분류와 처리

### [개념]

Sensitive Information Rules는 어떤 정보가 민감정보인지 분류하고 처리하는 기준이다.

민감정보는 Memory Update, Checkpoint, State Snapshot, Tool Result Summary에서 모두 주의해야 한다.

```text
Sensitive Information Rules = 민감정보 분류와 저장 처리 기준
```

---

### [핵심]

민감정보 분류:

| Category           | 예시                     | 처리                       |
| ------------------ | ------------------------ | -------------------------- |
| Secret             | API Key, Token, Password | 저장 금지                  |
| Credential         | 로그인 정보, 인증 코드   | 저장 금지                  |
| Financial          | 계좌번호, 카드번호       | 저장 금지                  |
| Identity           | 주민번호, 여권번호       | 저장 금지                  |
| Precise Location   | 상세 주소, 좌표          | 명시 요청 없으면 저장 금지 |
| Health             | 질병, 진단, 치료 기록    | 명시 요청 없으면 저장 금지 |
| Legal              | 사건 세부, 법적 분쟁     | 명시 요청 없으면 저장 주의 |
| Personal Attribute | 민감한 개인 속성         | 명시 요청 없으면 저장 금지 |
| Private Content    | 사적 대화 원문           | 필요 최소화                |
| Security Risk      | 악용 가능한 취약점 정보  | 저장 주의                  |

처리 방식:

- Do Not Store
- Redact
- Summarize Safely
- Ask if Explicit Consent Needed
- Delete on Forget Request
- Mark Sensitive
- Limit Scope

---

### [실무]

민감정보 처리 예시:

```json
{
  "input": "DB_PASSWORD=my-secret-password",
  "classification": "Secret",
  "memoryAction": "do_not_store",
  "safeSummary": "Database password is configured through environment variable."
}
```

민감정보 처리 예시:

```json
{
  "input": "사용자의 RAG 문서 출력 선호",
  "classification": "Safe Preference",
  "memoryAction": "store",
  "reason": "향후 응답 품질에 도움"
}
```

민감정보 처리 예시:

```json
{
  "input": "정확한 집 주소",
  "classification": "Precise Location",
  "memoryAction": "do_not_store_without_explicit_request",
  "safeSummary": "User may prefer local context when explicitly requested."
}
```

민감정보는 Memory 품질보다 Safety가 우선이다.

---

### [FAQ]

Q. Sensitive Information Rules는 뭐야?
A. 민감정보를 분류하고 Memory나 State에 저장할지 말지 결정하는 기준이다.

Q. Secret에는 뭐가 포함돼?
A. API Key, Token, Password, Cookie, Private Key 같은 인증 정보가 포함된다.

Q. 민감정보는 무조건 저장 금지야?
A. Secret은 저장 금지가 원칙이고, 민감한 개인 정보는 명시 요청 없이는 저장하지 않는다.

Q. Redaction은 뭐야?
A. 민감한 원문 값을 제거하고 안전한 요약만 남기는 처리다.

Q. 민감정보 처리의 핵심은?
A. 필요 최소화, Redaction, 저장 금지, 사용자 Forget Request 준수다.

---

# 10. Secret vs Config

## 10.1 Secret과 Config 구분

### [개념]

Secret과 Config는 구분해야 한다.

Secret은 인증, 접근 권한, 보안 위험과 직접 연결되는 값이다.

Config는 시스템 동작 설정이며 Secret 값을 포함하지 않는 경우 저장 가능하다.

```text
Secret = 저장 금지 값
Config = 구조나 설정 설명은 저장 가능
```

---

### [핵심]

Secret 예시:

- API Key 실제 값
- DB Password 실제 값
- JWT Secret 실제 값
- OAuth Client Secret 실제 값
- SSH Private Key
- Access Token
- Refresh Token
- Session Cookie

Config 예시:

- 환경변수 사용 여부
- 포트 번호
- 모델 이름
- 컨테이너 이름
- DB 종류
- Framework 설정 구조
- Secret을 환경변수로 주입한다는 규칙
- RAG chunk size 설정
- Agent Workflow 구조

저장 가능:

```text
Ollama는 host.docker.internal로 연결한다.
API Key는 환경변수로 관리한다.
DB는 PostgreSQL을 사용한다.
```

저장 금지:

```text
OPENAI_API_KEY=sk-...
DB_PASSWORD=...
JWT_SECRET=...
```

---

### [실무]

안전한 Config Memory 예시:

```json
{
  "type": "project_config_memory",
  "key": "secret_management_rule",
  "value": "API Key와 Password는 Memory에 저장하지 않고 환경변수로 관리한다.",
  "sensitivity": "safe"
}
```

위험한 Secret Memory 예시:

```json
{
  "type": "secret_memory",
  "key": "jwt_secret_value",
  "value": "actual-secret-value",
  "action": "delete_immediately"
}
```

Config 문서 작성 시에도 Secret 값은 placeholder로만 표현한다.

```properties
# Good
tourapi.service-key=${TOUR_API_SERVICE_KEY}

# Bad
tourapi.service-key=actual-secret-key
```

---

### [FAQ]

Q. Secret과 Config 차이는?
A. Secret은 인증이나 접근 권한과 연결된 실제 비밀 값이고, Config는 시스템 동작 설정이다.

Q. Secret은 Memory에 저장해도 돼?
A. 안 된다. 실제 API Key, Password, Token, Secret 값은 저장하지 않는다.

Q. Config는 저장해도 돼?
A. Secret 값이 포함되지 않은 설정 구조나 운영 규칙은 저장할 수 있다.

Q. 환경변수 이름은 저장해도 돼?
A. 일반적으로 실제 값이 아닌 환경변수 이름은 저장 가능하다.

Q. 문서 예제에서 Secret은 어떻게 표현해?
A. 실제 값 대신 `${ENV_NAME}` 또는 placeholder를 사용한다.

---

# 11. Forget Request Rules

## 11.1 Memory 삭제 요청 처리

### [개념]

Forget Request는 사용자가 특정 Memory를 삭제하거나 더 이상 사용하지 말라고 요청하는 상황이다.

Forget Request는 일반 Memory Update보다 우선한다.

```text
Forget Request = 사용자의 Memory 삭제 또는 비활성화 요청
```

---

### [핵심]

Forget Request 대상:

- 특정 사용자 선호
- 오래된 프로젝트 정보
- 잘못 저장된 결정
- 민감정보
- 잘못된 진행 상태
- 특정 대화 내용
- 특정 개인 정보
- 특정 프로젝트 Memory

처리 방식:

- Delete
- Deprecate
- Disable
- Redact
- Archive if deletion unavailable
- Stop using in current task
- Confirm if scope ambiguous

주의:

- 사용자가 명시적으로 잊어달라고 하면 우선 처리한다.
- 삭제 범위가 모호하면 범위를 확인한다.
- 민감정보는 삭제 또는 Redaction을 우선한다.
- 삭제된 Memory를 이후 Retrieval에서 사용하지 않는다.

---

### [실무]

Forget Request 예시:

```json
{
  "userRequest": "이전 출력 형식 기억하지 마",
  "targetMemory": "old_output_format_preference",
  "action": "delete_or_deprecate",
  "currentTaskImpact": "old format no longer used"
}
```

Forget Request 예시:

```json
{
  "userRequest": "API Key 관련 내용 잊어줘",
  "targetMemory": "secret_or_api_key_memory",
  "action": "delete_redact",
  "priority": "highest_safety"
}
```

Forget Request Scope 예시:

```text
명확한 요청:
"FestaPick 프로젝트 관련 기억은 이 채팅에서 쓰지 마"

처리:
현재 채팅 Scope에서 해당 Project Memory Retrieval 제외
```

Forget Request는 Memory Update Log에 안전하게 기록할 수 있지만, 삭제 대상 원문을 다시 저장하지 않는다.

---

### [FAQ]

Q. Forget Request가 뭐야?
A. 사용자가 특정 Memory를 삭제하거나 더 이상 사용하지 말라고 요청하는 상황이다.

Q. Forget Request는 우선순위가 높아?
A. 높다. 일반 Memory Update보다 우선 처리한다.

Q. 삭제 범위가 모호하면?
A. 어떤 Memory를 삭제할지 범위를 확인하거나 현재 작업에서 보수적으로 사용하지 않는다.

Q. 민감정보 Forget Request는 어떻게 처리해?
A. 삭제 또는 Redaction을 우선하고 이후 Retrieval에서 사용하지 않는다.

Q. 삭제한 Memory를 다시 요약해서 저장해도 돼?
A. 안 된다. 삭제 대상 원문이나 핵심 민감 값을 다시 저장하지 않는다.

---

# 12. Privacy / Safety in State and Checkpoint

## 12.1 State와 Checkpoint의 민감정보 관리

### [개념]

State와 Checkpoint도 Memory처럼 민감정보 관리가 필요하다.

State는 임시 정보라도 Agent 간 전달되거나 Checkpoint로 저장될 수 있기 때문에 Secret과 민감정보를 포함하지 않아야 한다.

```text
State / Checkpoint Privacy = State Snapshot과 복구 지점의 민감정보 저장 방지
```

---

### [핵심]

State / Checkpoint 저장 금지:

- API Key 실제 값
- Password 실제 값
- Token 실제 값
- Cookie
- Private Key
- 인증 코드
- 개인정보 원문
- 민감한 Tool Result 원문
- 삭제 요청된 Memory
- 보안상 위험한 세부 정보

State / Checkpoint 저장 가능:

- Secret이 환경변수로 관리된다는 사실
- 민감정보 제거 후 요약
- 작업 단계
- 요구사항
- 제약사항
- Review Findings
- 오류 유형
- Side Effect 여부
- 복구 지점

---

### [실무]

나쁜 Checkpoint 예시:

```json
{
  "checkpointId": "cp01",
  "toolResults": {
    "env": {
      "OPENAI_API_KEY": "sk-actual-value",
      "DB_PASSWORD": "actual-password"
    }
  }
}
```

좋은 Checkpoint 예시:

```json
{
  "checkpointId": "cp01",
  "toolResultsSummary": {
    "envValidation": "required environment variables exist",
    "secretValuesStored": false
  }
}
```

좋은 State 예시:

```json
{
  "constraints": [
    "API Key는 환경변수로 관리",
    "실제 Secret 값은 Memory와 Checkpoint에 저장 금지"
  ],
  "errors": [
    {
      "step": "config_validation",
      "message": "required environment variable missing",
      "secretValueIncluded": false
    }
  ]
}
```

State와 Checkpoint도 저장 전 Redaction을 수행한다.

---

### [FAQ]

Q. State에도 민감정보 저장을 피해야 해?
A. 그렇다. State는 Agent 간 전달되거나 Checkpoint로 저장될 수 있어 민감정보를 넣지 않아야 한다.

Q. Checkpoint에 Tool Result 원문을 저장해도 돼?
A. 민감정보가 포함될 수 있으므로 필요한 요약만 저장해야 한다.

Q. 환경변수 값은 Checkpoint에 저장해도 돼?
A. 실제 값은 저장하지 않고 존재 여부나 변수 이름 정도만 기록한다.

Q. 오류 로그에 Secret이 포함되면?
A. 저장 전에 Redaction해야 한다.

Q. State / Checkpoint Privacy의 핵심은?
A. 복구 가능성을 유지하면서 Secret과 민감정보 원문을 남기지 않는 것이다.

---

# 13. Common Mistakes

## 13.1 Memory Conflict / Expiration / Privacy 실수

### [개념]

Memory Conflict, Expiration, Privacy 실수는 Agent가 오래된 정보로 답변하거나 민감정보를 장기 저장하는 문제를 만든다.

이 영역은 Agent 신뢰성과 안전성에 직접 연결된다.

---

### [핵심]

자주 발생하는 실수:

- 현재 요청보다 오래된 Memory를 우선
- 충돌 Memory를 임의로 조합
- 최신 결정과 오래된 결정을 동시에 active로 둠
- Project Progress를 갱신하지 않음
- expired Memory를 현재 사실처럼 사용
- Conversation Summary를 갱신하지 않음
- Working Memory 후보안을 Decision Memory로 저장
- 사용자 Forget Request를 무시
- API Key를 Memory에 저장
- Token을 Checkpoint에 저장
- Tool Result 원문을 그대로 저장
- Secret과 Config를 구분하지 않음
- 민감정보를 안전 요약 없이 저장
- 삭제된 Memory를 다시 Retrieval에 사용

---

### [실무]

문제:

```text
Agent가 오래된 6파트 구성을 기준으로 다음 문서를 작성함
```

원인:

```text
Latest Decision과 Old Memory Conflict를 해결하지 않음
```

해결:

```text
최신 결정 8파트를 active로 사용
→ 6파트 Memory는 deprecated
→ State에 activeDecision 반영
```

문제:

```text
Part 진행 상태가 Planned로 계속 검색됨
```

원인:

```text
Project Progress Memory Expiration / Refresh 누락
```

해결:

```text
Project Progress Memory updatedAt 갱신
→ 완료 Part 목록 반영
→ old progress deprecated
```

문제:

```text
API Key가 Checkpoint에 저장됨
```

원인:

```text
Tool Result 원문을 Redaction 없이 저장
```

해결:

```text
Checkpoint에서 Secret 제거
→ env 존재 여부만 요약
→ Secret 저장 금지 규칙 적용
```

문제:

```text
사용자가 잊어달라고 한 정보를 다시 사용함
```

원인:

```text
Forget Request 처리 후 Retrieval Filter에 반영하지 않음
```

해결:

```text
해당 Memory delete/deprecate
→ Retrieval 제외
→ 현재 State에서도 제거
```

---

### [FAQ]

Q. Memory Conflict에서 가장 흔한 실수는?
A. 현재 요청보다 오래된 Memory를 우선하거나 충돌 Memory를 임의로 섞는 것이다.

Q. Memory Expiration에서 가장 흔한 실수는?
A. 오래된 Project Progress나 Summary를 최신 사실처럼 사용하는 것이다.

Q. Privacy / Safety에서 가장 흔한 실수는?
A. API Key, Token, Password 같은 Secret을 Memory나 Checkpoint에 저장하는 것이다.

Q. Secret과 Config를 혼동하면?
A. 실제 비밀 값이 장기 Memory에 남아 보안 위험이 생긴다.

Q. 해결 핵심은?
A. Conflict 우선순위, Expiration 상태, Privacy Redaction을 Memory 사용 전 적용하는 것이다.

---

# 14. Troubleshooting

## 14.1 Memory Conflict / Expiration / Privacy 문제 해결

### [개념]

Troubleshooting은 Memory Conflict, Expiration, Privacy / Safety 문제를 원인과 해결 기준으로 정리한다.

문제 해결은 먼저 현재 요청, 최신 결정, Memory 상태, 민감정보 여부를 확인해야 한다.

---

### [핵심]

Troubleshooting 형식:

```md
문제:

원인:

해결:
```

주요 문제:

- 충돌 Memory 해결 실패
- 오래된 Memory 사용
- deprecated Memory 사용
- Memory 갱신 누락
- Summary 오래됨
- Secret 저장
- 민감정보 Redaction 누락
- Forget Request 미반영
- 삭제된 Memory 재사용
- Scope 충돌

---

### [실무]

문제:

```text
충돌하는 두 Memory가 모두 active로 검색됨
```

원인:

```text
Decision Versioning과 deprecated 처리가 없음
```

해결:

```text
최신 결정을 active로 지정
→ 이전 결정은 deprecated
→ Retrieval에서 active 우선
```

문제:

```text
오래된 Summary가 현재 작업을 덮어씀
```

원인:

```text
Conversation Summary Refresh 누락
```

해결:

```text
현재 대화 기준 Summary Rebuild
→ 오래된 Summary archived
→ active summary updatedAt 갱신
```

문제:

```text
expired Memory가 현재 사실처럼 사용됨
```

원인:

```text
Memory Status Filter 없음
```

해결:

```text
active Memory만 기본 사용
→ deprecated / expired는 참고용으로만 표시
→ Recency Check 필수화
```

문제:

```text
Secret이 Memory에 저장됨
```

원인:

```text
Sensitivity Check 누락
```

해결:

```text
해당 Memory 삭제
→ Secret 값 Redaction
→ 저장 금지 패턴 추가
→ Checkpoint와 State도 재검사
```

문제:

```text
Forget Request 이후에도 관련 Memory가 검색됨
```

원인:

```text
삭제 요청이 Retrieval Filter에 반영되지 않음
```

해결:

```text
Memory delete/deprecate
→ Retrieval index 갱신
→ currentState에서 제거
→ 관련 Summary refresh
```

---

### [FAQ]

Q. 충돌하는 Memory가 모두 active면 어떻게 해?
A. 최신 결정과 현재 요청을 기준으로 하나만 active로 두고 나머지는 deprecated 처리한다.

Q. 오래된 Summary가 현재 작업과 다르면?
A. 현재 대화와 최신 결정 기준으로 Summary를 다시 작성하고 이전 Summary는 archive한다.

Q. expired Memory가 계속 검색되면?
A. Memory Status Filter를 적용해 active Memory를 기본 사용하고 expired Memory는 현재 사실로 사용하지 않는다.

Q. Secret이 Memory에 저장되었으면?
A. 즉시 삭제 또는 Redaction하고 State, Checkpoint, Summary에도 남아 있는지 확인한다.

Q. Forget Request가 반영되지 않으면?
A. Retrieval index와 currentState를 갱신해 해당 Memory가 다시 사용되지 않게 한다.

---

# 15. Best Practice

## 15.1 Memory Conflict, Expiration, Privacy / Safety 설계 원칙

### [개념]

좋은 Memory Safety 설계는 충돌 정보를 안전하게 해결하고, 오래된 Memory를 갱신하며, 민감정보를 저장하지 않는다.

Agent Memory는 장기 프로젝트 일관성을 높이기 위한 도구이지만 현재 요청과 안전 기준을 넘어서면 안 된다.

---

### [핵심]

Best Practice:

- 현재 사용자 요청을 Memory보다 우선한다.
- 명시적 사용자 정정은 기존 Memory를 덮어쓴다.
- 최신 프로젝트 결정을 active 기준으로 사용한다.
- 오래된 결정은 deprecated 처리한다.
- 충돌 Memory를 임의로 조합하지 않는다.
- Memory Conflict Type을 기록한다.
- Conflict Resolution 결과를 State에 반영한다.
- Project Progress는 자주 갱신한다.
- Pending Task는 완료 시 update 또는 archive한다.
- Conversation Summary는 오래되면 refresh한다.
- active / deprecated / archived / expired 상태를 구분한다.
- expired Memory를 현재 사실로 사용하지 않는다.
- Secret과 Config를 구분한다.
- API Key, Password, Token은 저장하지 않는다.
- Tool Result와 Checkpoint는 Redaction 후 저장한다.
- 민감정보는 필요 최소한으로 처리한다.
- Forget Request는 일반 Memory Update보다 우선한다.
- 삭제 또는 비활성화된 Memory는 Retrieval에서 제외한다.

---

### [실무]

권장 Conflict Flow:

```text
Retrieve Memory
→ Detect Conflict
→ Identify Conflict Type
→ Apply Priority Rule
→ Resolve
→ State Update
→ Memory Update / Deprecate
→ Validate Final Output
```

권장 Expiration Flow:

```text
Review Memory
→ Check updatedAt
→ Check status
→ Check current validity
→ active / deprecated / archived / expired 결정
→ Refresh if needed
```

권장 Privacy Flow:

```text
New Memory Candidate
→ Sensitivity Check
→ Secret Detection
→ Redaction if needed
→ Store Safe Summary only
→ Delete unsafe data
```

권장 Memory Metadata:

```json
{
  "type": "decision_memory",
  "scope": "Personal AI Project",
  "key": "part_count_decision",
  "value": "Agent Memory & State Management는 총 8파트 구성",
  "status": "active",
  "updatedAt": "2026-07-01",
  "source": "user_confirmed_decision",
  "sensitivity": "safe",
  "confidence": "high"
}
```

---

### [FAQ]

Q. 좋은 Memory Conflict 처리 기준은?
A. 현재 요청, 명시적 정정, 최신 결정 순으로 우선순위를 적용하고 오래된 Memory는 deprecated 처리하는 것이다.

Q. 좋은 Memory Expiration 기준은?
A. updatedAt, status, 현재 유효성을 기준으로 active, deprecated, archived, expired를 구분하는 것이다.

Q. 좋은 Privacy / Safety 기준은?
A. Secret과 민감정보를 저장하지 않고 필요한 경우 Redaction한 안전 요약만 저장하는 것이다.

Q. Forget Request는 어떻게 처리해?
A. 삭제 또는 비활성화하고 Retrieval과 State에서 해당 Memory를 제외한다.

Q. Memory Conflict, Expiration, Privacy / Safety의 최종 목표는?
A. 오래된 정보와 위험한 정보를 제거하고 현재 작업에 안전하고 유효한 Memory만 사용하게 만드는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Memory Conflict가 뭐야?
A. 서로 다른 Memory, 현재 요청, 최근 결정, 과거 정보가 충돌하는 상황이다.

Q. Memory Conflict는 왜 생겨?
A. 프로젝트 진행 상황, 사용자 선호, 결정 사항이 시간이 지나며 바뀌기 때문이다.

Q. Memory Conflict 우선순위는?
A. Current User Request, Explicit User Correction, Latest Project Decision, Recent Conversation, Active Project Progress, Domain Rules, Long-term Memory 순서다.

Q. 현재 요청과 Long-term Memory가 충돌하면?
A. 현재 요청을 우선한다.

Q. 최신 결정과 오래된 결정이 충돌하면?
A. 최신 프로젝트 결정을 우선하고 오래된 결정은 deprecated 처리한다.

Q. 충돌 Memory를 섞어서 결론 내도 돼?
A. 아니다. 우선순위 규칙으로 해결하고 임의 조합은 피한다.

Q. Memory Conflict Type은 뭐가 있어?
A. Current Request vs Long-term Memory, User Correction vs Old Memory, Latest Decision vs Old Decision, Project Progress vs Old Progress, Domain Rules vs Output 등이 있다.

Q. Project Scope Conflict는 뭐야?
A. 다른 프로젝트 Memory가 현재 프로젝트 답변에 섞이는 문제다.

Q. Sensitive Data Conflict는 어떻게 처리해?
A. 민감정보 저장 정책을 우선하고 Memory 저장을 금지한다.

Q. Memory Conflict는 어떻게 해결해?
A. 출처, 충돌 유형, 최신성, 우선순위를 확인한 뒤 해결 기준을 State에 반영한다.

Q. Conflict Resolution Action은 뭐가 있어?
A. Use Current Request, Use Latest Decision, Update, Deprecate, Ignore, Delete, Rebuild State가 있다.

Q. Memory Expiration이 뭐야?
A. 오래되거나 더 이상 유효하지 않은 Memory를 만료, 보관, 비활성화, 갱신하는 기준이다.

Q. 모든 Memory는 영구적으로 유지해도 돼?
A. 아니다. 진행 상태, 버전 정보, 임시 결정은 시간이 지나면 갱신 또는 만료가 필요하다.

Q. deprecated Memory는 삭제된 거야?
A. 아니다. 현재 기준으로 사용하지 않지만 과거 기록으로 참고할 수 있는 상태다.

Q. expired Memory는 사용할 수 있어?
A. 현재 사실로 사용하면 안 된다.

Q. 어떤 Memory가 만료 대상이야?
A. Project Progress, Pending Tasks, 기술 버전, API Contract, Tool Result, Conversation Summary, Checkpoint가 대표적이다.

Q. 어떤 Memory는 오래 유지 가능해?
A. 프로젝트 목표, 안정적인 사용자 선호, 핵심 RAG 규칙, 확정 Architecture Decision은 비교적 오래 유지 가능하다.

Q. Memory Refresh가 뭐야?
A. 기존 Memory를 최신 상태로 갱신하는 과정이다.

Q. Refresh는 언제 해?
A. 사용자가 정정했거나 프로젝트 진행 상태, 기술 스택, 문서 구조, 결정 사항이 바뀌었을 때 한다.

Q. 결정이 바뀌면 어떻게 Refresh해?
A. Versioned Update로 이전 결정을 deprecated 처리하고 최신 결정을 active로 둔다.

Q. Memory Privacy / Safety가 뭐야?
A. Memory와 State에 민감정보, Secret, 개인정보가 저장되지 않도록 관리하는 기준이다.

Q. API Key를 Memory에 저장해도 돼?
A. 안 된다. API Key, Password, Token, Cookie, Private Key는 저장하지 않는다.

Q. Config 정보는 저장해도 돼?
A. Secret 값이 아닌 일반 설정 구조나 사용 여부는 저장할 수 있다.

Q. Sensitive Information Rules는 뭐야?
A. 민감정보를 분류하고 Memory나 State에 저장할지 말지 결정하는 기준이다.

Q. Secret에는 뭐가 포함돼?
A. API Key, Token, Password, Cookie, Private Key 같은 인증 정보가 포함된다.

Q. Redaction은 뭐야?
A. 민감한 원문 값을 제거하고 안전한 요약만 남기는 처리다.

Q. Secret과 Config 차이는?
A. Secret은 인증이나 접근 권한과 연결된 실제 비밀 값이고, Config는 시스템 동작 설정이다.

Q. 환경변수 이름은 저장해도 돼?
A. 일반적으로 실제 값이 아닌 환경변수 이름은 저장 가능하다.

Q. Forget Request가 뭐야?
A. 사용자가 특정 Memory를 삭제하거나 더 이상 사용하지 말라고 요청하는 상황이다.

Q. Forget Request는 우선순위가 높아?
A. 높다. 일반 Memory Update보다 우선 처리한다.

Q. State에도 민감정보 저장을 피해야 해?
A. 그렇다. State는 Agent 간 전달되거나 Checkpoint로 저장될 수 있어 민감정보를 넣지 않아야 한다.

Q. Checkpoint에 Tool Result 원문을 저장해도 돼?
A. 민감정보가 포함될 수 있으므로 필요한 요약만 저장해야 한다.

Q. Memory Conflict에서 가장 흔한 실수는?
A. 현재 요청보다 오래된 Memory를 우선하거나 충돌 Memory를 임의로 섞는 것이다.

Q. Memory Expiration에서 가장 흔한 실수는?
A. 오래된 Project Progress나 Summary를 최신 사실처럼 사용하는 것이다.

Q. Privacy / Safety에서 가장 흔한 실수는?
A. API Key, Token, Password 같은 Secret을 Memory나 Checkpoint에 저장하는 것이다.

Q. Secret이 Memory에 저장되었으면?
A. 즉시 삭제 또는 Redaction하고 State, Checkpoint, Summary에도 남아 있는지 확인한다.

Q. Forget Request가 반영되지 않으면?
A. Retrieval index와 currentState를 갱신해 해당 Memory가 다시 사용되지 않게 한다.

Q. Memory Conflict, Expiration, Privacy / Safety의 최종 목표는?
A. 오래된 정보와 위험한 정보를 제거하고 현재 작업에 안전하고 유효한 Memory만 사용하게 만드는 것이다.
