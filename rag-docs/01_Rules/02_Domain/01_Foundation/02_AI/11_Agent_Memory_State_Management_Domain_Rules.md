# Agent Memory & State Management Domain Rules

---

# 1. Domain Purpose

Agent Memory & State Management Domain 문서는 AI Agent / PM Agent / Review Agent / Multi-Agent System용 RAG 문서 제작 규칙이다.

목적:

- Agent Memory 기본 개념 이해
- Agent State와 Memory의 차이 설명
- Short-term Memory / Long-term Memory 설계 기준 제공
- Multi-Agent Workflow에서 Shared State 관리 기준 제공
- Project Memory / User Preference / Decision Log 관리 기준 제공
- Checkpoint / Resume / Rollback 기준 제공
- Memory Retrieval / Memory Update 기준 제공
- 오래된 Memory / 충돌 Memory / 민감정보 관리 기준 제공

우선순위:

1. State and Memory Separation
2. Context Consistency
3. Current Task Reliability
4. Long-term Knowledge Reuse
5. Memory Safety
6. Conflict Resolution
7. Workflow Continuity

---

# 2. Scope

포함 범위:

- Agent State
- Agent Memory
- Short-term Memory
- Long-term Memory
- Working Memory
- Shared State
- Project Memory
- User Preference Memory
- Decision Memory
- Conversation Summary
- Context Window
- Checkpoint
- Resume
- Rollback
- Memory Retrieval
- Memory Update
- Memory Validation
- Memory Conflict
- Memory Expiration
- Memory Privacy
- Multi-Agent State
- Workflow State
- LangGraph State 개념
- Agent Context Management

제외 범위:

- Database 내부 구현 심화
- Vector Database 상세 구현
- LangGraph 코드 구현 상세
- LangChain Memory 클래스 상세 사용법
- 개인정보 저장 정책 심화
- 보안 컴플라이언스 상세
- 대규모 Agent Platform Memory 운영

---

# 3. Section Priority

## Required

- [개념]
- [핵심]
- [실무]
- [FAQ]

---

## Strongly Recommended

- [Flow]
- [예제]
- [주의]
- [Best Practice]
- [Troubleshooting]
- [Checklist]
- [Comparison]

---

# 4. State vs Memory Core Rules

Agent State와 Agent Memory는 반드시 구분해서 설명한다.

핵심 비교:

| 구분 | State                             | Memory                                |
| ---- | --------------------------------- | ------------------------------------- |
| 목적 | 현재 작업 진행 상태 관리          | 과거 정보 재사용                      |
| 기간 | 현재 Workflow 중심                | 장기 보존 가능                        |
| 예시 | 현재 단계, 중간 결과, Review 결과 | 프로젝트 규칙, 사용자 선호, 과거 결정 |
| 위험 | 누락 시 Workflow 깨짐             | 오래되면 잘못된 답변 유발             |

기본 구조:

```text
Current Request
→ Workflow State
→ Agent Execution
→ Memory Retrieval if Needed
→ State Update
→ Final Output
→ Optional Memory Update
```

반드시 설명:

- State는 현재 실행 중인 작업의 상태
- Memory는 이전 대화나 프로젝트 정보를 재사용하기 위한 저장 정보
- 모든 State가 Memory가 되는 것은 아님
- 모든 Memory가 현재 작업에 필요한 것도 아님
- 현재 사용자 요청이 Memory보다 우선한다

금지:

- State와 Memory를 같은 것으로 설명
- 오래된 Memory를 무조건 사실로 사용하는 구조
- 모든 대화 내용을 장기 Memory에 저장하는 방식
- 민감정보를 무분별하게 Memory에 저장하는 방식

---

# 5. Agent State Rules

Agent State는 현재 Workflow 실행에 필요한 작업 상태이다.

필수 포함:

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

예시:

```json
{
  "status": "in_progress",
  "currentStep": "backend_review",
  "requirements": ["Spring Boot 3.x 기준"],
  "constraints": ["ApiResponse<T> 직접 반환"],
  "decisions": [],
  "agentOutputs": {},
  "reviewFindings": [],
  "errors": []
}
```

반드시 설명:

- State는 Agent 간 작업 연속성을 유지
- 현재 단계와 다음 작업을 명확히 함
- 요구사항, 제약, 결정 사항을 기록
- Review / Fix Loop에서 중요
- 실패와 오류도 State에 포함 가능

주의:

- State가 너무 커지면 Context Window를 낭비
- 오래된 State가 최신 요청을 덮어쓰지 않게 관리
- Agent Output과 Final Output을 구분
- 민감정보를 State에 넣을 때 주의

---

# 6. Shared State Rules

Shared State는 Multi-Agent Workflow에서 여러 Agent가 함께 참조하는 상태이다.

필수 포함:

- userRequest
- workflowId
- taskPlan
- assignedAgents
- sharedRequirements
- sharedConstraints
- apiContract
- domainDecisions
- intermediateOutputs
- reviewStatus
- finalStatus

기본 Flow:

```text
PM Agent
→ Create Shared State
→ Domain Agent Updates Output
→ Review Agent Adds Findings
→ Fix Agent Updates Result
→ PM Agent Finalizes
```

반드시 설명:

- Shared State는 Agent 간 공통 작업 기록
- PM Agent가 초기 Shared State를 구성
- Domain Agent는 자기 결과를 추가
- Review Agent는 검토 결과를 추가
- Fix Agent는 수정 결과를 반영
- 최종 PM Agent가 전체 상태를 통합

주의:

- Agent가 서로 다른 State를 보고 작업하면 충돌 발생
- Shared State Update 규칙 필요
- 누가 어떤 필드를 수정할 수 있는지 정의 가능
- 중간 실패 상태를 숨기지 말 것

---

# 7. Working Memory Rules

Working Memory는 현재 작업 중 Agent가 임시로 사용하는 정보이다.

필수 포함:

- Current Prompt Context
- Retrieved Context
- Tool Result
- Temporary Reasoning Data
- Candidate Solution
- Validation Result

기본 Flow:

```text
Agent Task
→ Retrieve Context
→ Store Temporary Context
→ Generate Candidate
→ Validate
→ Update State
```

반드시 설명:

- Working Memory는 현재 작업에만 필요한 임시 기억
- RAG 검색 결과, Tool 결과, 중간 후보안이 포함될 수 있음
- 작업 완료 후 장기 Memory로 저장할 필요가 없을 수 있음
- 최종 State에는 필요한 결과만 요약 반영

주의:

- Working Memory를 전부 Long-term Memory에 저장하지 말 것
- 임시 추론 데이터를 사실 결정으로 저장하지 않기
- Tool 실패 결과와 성공 결과를 구분

---

# 8. Short-term Memory Rules

Short-term Memory는 현재 대화나 현재 세션의 문맥 유지에 사용한다.

필수 포함:

- Conversation Context
- Recent User Request
- Recent Decisions
- Recent Corrections
- Session Summary
- Temporary Preference

반드시 설명:

- Short-term Memory는 현재 대화 흐름을 유지
- 사용자가 방금 수정한 내용은 우선 반영
- 현재 작업 완료 후 사라질 수 있음
- 장기적으로 유효한 정보만 Long-term Memory 후보가 됨

주의:

- 이전 발언과 현재 발언이 충돌하면 현재 발언 우선
- 짧은 농담이나 일시적 감정은 장기 저장하지 않음
- 세션 내 임시 결정과 프로젝트 공식 결정을 구분

---

# 9. Long-term Memory Rules

Long-term Memory는 장기적으로 재사용할 가치가 있는 정보를 저장한다.

필수 포함:

- User Preference
- Project Context
- Technical Stack
- Architecture Decision
- Naming Rule
- Workflow Preference
- Persistent Constraint
- Reusable Pattern

예시:

```json
{
  "type": "project_memory",
  "key": "personal_ai_stack",
  "value": "AnythingLLM + Ollama + Qwen2.5 + BGE-M3",
  "updatedAt": "2026-06-27"
}
```

반드시 설명:

- Long-term Memory는 반복적으로 유용한 정보만 저장
- 프로젝트 기술 스택, 폴더 구조, 문서 규칙은 저장 가치가 높음
- 사용자 선호도는 향후 답변 품질에 도움
- Memory는 업데이트와 삭제가 가능해야 함

주의:

- 민감정보 저장 금지 또는 제한
- 오래된 정보는 최신성 확인
- 사용자가 저장을 원하지 않는 정보는 저장하지 않음
- 일회성 정보는 Long-term Memory에 부적합

---

# 10. Project Memory Rules

Project Memory는 특정 프로젝트의 지속적인 맥락을 저장한다.

필수 포함:

- Project Goal
- Current Stack
- Hardware Context
- Folder Structure
- Agent Architecture
- RAG Document Rules
- Domain Rules
- Progress Status
- Pending Tasks
- Decisions

예시:

```text
Project:
Personal AI Development Team

Stack:
AnythingLLM, Ollama, Qwen2.5, BGE-M3

Goal:
PM Agent 중심 Multi-Agent System 구축
```

반드시 설명:

- Project Memory는 장기 프로젝트에서 매우 중요
- 기술 스택과 진행 상황을 유지
- 이전 결정 사항을 반복 설명하지 않게 함
- Agent Routing과 RAG Scope 결정에 도움

주의:

- 프로젝트 상황이 바뀌면 Memory 업데이트 필요
- 완료된 작업과 예정 작업을 구분
- 임시 아이디어와 확정 결정을 구분

---

# 11. User Preference Memory Rules

User Preference Memory는 사용자의 응답 선호와 작업 방식을 저장한다.

필수 포함:

- Language Preference
- Tone Preference
- Output Format Preference
- Document Style
- Workflow Preference
- Follow-up Preference

예시:

```json
{
  "language": "Korean",
  "tone": "casual but practical",
  "documentStyle": "RAG optimized Markdown",
  "prefersFinalReadyDraft": true
}
```

반드시 설명:

- 사용자 선호는 답변 형식과 톤을 조정하는 데 사용
- 문서 작업 선호, 코드 설명 방식, 출력 포맷은 유용한 Memory
- 사용자가 명시적으로 바꾸면 최신 선호 우선

주의:

- 민감한 개인 속성 저장 주의
- 일시적 기분을 장기 선호로 저장하지 말 것
- 현재 요청이 선호와 다르면 현재 요청 우선

---

# 12. Decision Memory Rules

Decision Memory는 프로젝트에서 확정된 결정을 저장한다.

필수 포함:

- Decision
- Reason
- Date
- Scope
- Alternatives
- Status
- UpdatedBy

예시:

```md
## Decision

- Agent는 문서와 분리해서 관리한다.
- Domain Rules도 RAG에 넣고 Agent가 참조하게 한다.
- Domain Rules에는 Retrieval Queries를 포함하는 B안을 사용한다.
```

반드시 설명:

- Decision Memory는 프로젝트 일관성을 유지
- 이전에 정한 방향을 반복 논의하지 않도록 도움
- 변경 가능한 결정은 status를 표시
- 결정 이유를 함께 저장하면 나중에 판단이 쉬움

주의:

- 논의 중인 아이디어를 확정 결정처럼 저장하지 않기
- 결정 변경 시 이전 결정과 충돌 처리
- 오래된 결정이 현재 목표와 맞는지 확인

---

# 13. Conversation Summary Rules

Conversation Summary는 긴 대화를 압축해 Context를 유지하는 방식이다.

필수 포함:

- Summary
- Key Decisions
- Current Task
- Open Questions
- Next Step
- Important Constraints

기본 Flow:

```text
Long Conversation
→ Extract Key Facts
→ Extract Decisions
→ Extract Pending Tasks
→ Create Summary
→ Use as Context
```

반드시 설명:

- 긴 대화는 Token Limit 때문에 요약 필요
- 요약은 사실, 결정, 진행 상황 중심
- 감정 표현이나 반복 내용은 줄임
- 다음 작업에 필요한 정보 위주로 유지

주의:

- 요약 과정에서 중요한 제약 누락 금지
- 추정을 사실처럼 요약하지 않기
- 오래된 요약은 최신 대화로 갱신 필요

---

# 14. Checkpoint Rules

Checkpoint는 Workflow를 중간 저장하는 기준이다.

필수 포함:

- Checkpoint ID
- Current Step
- State Snapshot
- Agent Outputs
- Tool Results
- Decisions
- Errors
- Resume Point

기본 Flow:

```text
Workflow Running
→ Important Step Completed
→ Save Checkpoint
→ Failure Occurs
→ Resume from Checkpoint
```

반드시 설명:

- Checkpoint는 실패 후 복구에 도움
- 긴 Multi-Agent 작업에서 특히 중요
- 각 주요 단계 완료 후 저장 가능
- Resume 시 동일 State에서 이어갈 수 있어야 함

주의:

- Checkpoint에 민감정보 저장 주의
- 너무 자주 저장하면 관리 부담 증가
- Checkpoint가 오래되면 최신 요구사항과 충돌 가능

---

# 15. Resume Rules

Resume은 중단된 Workflow를 이어가는 과정이다.

필수 포함:

- Last Checkpoint
- Completed Steps
- Pending Steps
- Current State
- Validation Before Resume
- User Confirmation if Needed

기본 Flow:

```text
Load Checkpoint
→ Validate Current Relevance
→ Identify Completed Steps
→ Identify Pending Steps
→ Resume Workflow
```

반드시 설명:

- Resume 전 현재 사용자 요청과 Checkpoint가 일치하는지 확인
- 이미 완료된 작업과 남은 작업을 구분
- 오래된 Checkpoint는 재검토 필요
- 사용자가 방향을 바꿨다면 기존 State를 수정해야 함

주의:

- 오래된 State로 그대로 재개 금지
- 실패 원인을 해결하지 않고 반복 실행 금지
- 완료된 작업을 중복 실행하지 않도록 주의

---

# 16. Rollback Rules

Rollback은 잘못된 상태나 변경을 이전 상태로 되돌리는 기준이다.

필수 포함:

- Previous State
- Failed Change
- Restore Point
- Side Effect
- Undo
- Manual Confirmation

기본 Flow:

```text
Bad Update
→ Identify Last Valid State
→ Restore State
→ Mark Failed Change
→ Continue or Stop
```

반드시 설명:

- State Rollback과 실제 파일/DB Rollback은 다름
- Agent State는 이전 Snapshot으로 되돌릴 수 있음
- 실제 Side Effect가 발생한 작업은 별도 복구 절차 필요
- 위험 작업은 Rollback 가능 여부를 사전에 확인

주의:

- 파일 삭제, DB 변경, 이메일 발송은 단순 State Rollback으로 복구 불가
- Rollback 전 현재 상태 백업 고려
- 사용자 승인 없이 실제 변경 Rollback 금지 가능

---

# 17. Memory Retrieval Rules

Memory Retrieval은 현재 요청에 필요한 Memory만 가져오는 과정이다.

필수 포함:

- Query
- Relevant Memory
- Memory Type
- Recency
- Source
- Confidence
- Conflict Check

기본 Flow:

```text
User Request
→ Identify Missing Context
→ Search Memory
→ Filter Relevant Memory
→ Check Recency
→ Use in Response
```

반드시 설명:

- 모든 Memory를 불러오지 말고 관련 있는 Memory만 사용
- 현재 작업에 필요한 정보인지 확인
- 최신성 확인
- 충돌하는 Memory가 있으면 현재 요청 우선
- Memory 사용 시 불확실하면 가정으로 표시

주의:

- 관련 없는 Memory로 답변을 오염시키지 않기
- 오래된 Memory를 최신 사실처럼 사용하지 않기
- Memory가 없으면 없다고 판단하고 현재 Context를 우선

---

# 18. Memory Update Rules

Memory Update는 어떤 정보를 장기 저장할지 결정하는 과정이다.

저장 후보:

- 장기 프로젝트 목표
- 기술 스택
- 폴더 구조
- 문서 규칙
- Agent 구조
- 반복 선호
- 확정 결정

저장 비추천:

- 일회성 감정
- 단기 일정
- 임시 농담
- 불확실한 추정
- 민감정보
- 사용자가 저장 원치 않는 정보

기본 Flow:

```text
New Information
→ Check Long-term Usefulness
→ Check Sensitivity
→ Check User Intent
→ Save / Do Not Save
```

반드시 설명:

- Memory Update는 신중해야 함
- 장기적으로 답변 품질을 높이는 정보만 저장
- 사용자가 명시적으로 기억하라고 하면 저장
- 사용자가 잊어달라고 하면 삭제 또는 비활성화

주의:

- 민감정보는 명시 요청 없이는 저장하지 않기
- 불확실한 정보를 확정 Memory로 저장하지 않기
- 현재 요청과 관련 없는 정보를 과도하게 저장하지 않기

---

# 19. Memory Validation Rules

Memory는 사용 전 검증이 필요하다.

필수 포함:

- Recency Check
- Conflict Check
- Source Check
- User Confirmation
- Confidence
- Validity

기본 Flow:

```text
Retrieved Memory
→ Check Recency
→ Compare Current Request
→ Detect Conflict
→ Use / Ask / Ignore
```

반드시 설명:

- Memory는 시간이 지나면 틀릴 수 있음
- 현재 요청과 충돌하면 현재 요청 우선
- 고위험 결정에는 사용자 확인 필요
- 확신이 낮은 Memory는 단정하지 않음

주의:

- 과거 기술 스택이 현재도 맞다고 단정 금지
- 프로젝트 진행 상태는 자주 바뀜
- 사용자가 정정한 내용은 즉시 반영

---

# 20. Memory Conflict Rules

Memory Conflict는 서로 다른 기억이 충돌하는 상황이다.

필수 포함:

- Old Memory
- New Information
- Conflict Type
- Priority Rule
- Resolution
- Update

우선순위:

```text
Current User Request
→ Explicit User Correction
→ Latest Project Decision
→ Recent Conversation
→ Long-term Memory
```

반드시 설명:

- 현재 사용자 발언이 가장 우선
- 명시적 정정은 기존 Memory를 덮어씀
- 프로젝트 결정은 최신 결정 우선
- 충돌이 명확하면 업데이트
- 애매하면 사용자에게 확인

주의:

- 충돌한 정보를 조합해서 임의 결론 내지 않기
- 오래된 Memory를 고집하지 않기
- 변경 이력을 남길 수 있음

---

# 21. Memory Expiration Rules

Memory는 필요에 따라 만료 또는 갱신되어야 한다.

필수 포함:

- Expiration
- Refresh
- Archive
- Deprecated Memory
- Active Memory
- Last Updated

만료 대상:

- 현재 진행 상황
- 예정 작업
- 임시 계획
- 버전 정보
- 환경 설정
- 프로젝트 상태

반드시 설명:

- 모든 Memory가 영구적일 필요는 없음
- 진행 상황은 자주 바뀌므로 갱신 필요
- 오래된 결정은 Deprecated 표시 가능
- 활성 Memory와 보관 Memory를 구분 가능

주의:

- 만료된 Memory를 현재 사실처럼 사용 금지
- 오래된 기술 버전 정보 주의
- Project Progress는 정기 갱신 필요

---

# 22. Privacy / Safety Rules

Memory와 State에는 개인정보와 민감정보 관리 기준이 필요하다.

필수 포함:

- Sensitive Information
- Secret
- API Key
- Credential
- Personal Data
- Health / Finance / Legal Sensitive Data
- User Consent
- Forget Request

금지 또는 주의:

- API Key 저장
- 비밀번호 저장
- 토큰 저장
- 주민번호 / 계좌번호 저장
- 민감한 개인 속성 저장
- 사적인 정보 과도 저장

반드시 설명:

- Secret은 Memory에 저장하지 않음
- 민감정보는 명시적 요청 없이는 저장하지 않음
- 사용자가 잊어달라고 하면 삭제해야 함
- Memory는 사용자에게 도움이 되는 범위로 제한

주의:

- 로그와 Memory에 Secret 노출 금지
- Tool Result에 민감정보가 섞일 수 있음
- 프로젝트 설정값과 Secret을 구분

---

# 23. Multi-Agent State Rules

Multi-Agent System에서는 State 관리가 더 중요하다.

필수 포함:

- Global State
- Agent Local State
- Shared State
- Agent Output
- Handoff State
- Review State
- Final State

구조:

```text
Global State
├ PM State
├ Backend Agent State
├ Frontend Agent State
├ Review Agent State
└ Final Output State
```

반드시 설명:

- Global State는 전체 Workflow 관리
- Agent Local State는 개별 Agent 작업 상태
- Shared State는 공통 요구사항과 결정 사항
- Review State는 품질 검증 결과
- Final State는 사용자에게 전달할 최종 결과

주의:

- Agent Local State를 모두 Global State에 넣으면 복잡해짐
- 공유해야 할 정보와 내부 임시 정보를 구분
- Agent 간 State 충돌 방지

---

# 24. LangGraph State Concept Rules

LangGraph 같은 Workflow 시스템의 State 개념을 기초 수준으로 설명할 수 있다.

필수 포함:

- State Graph
- Node
- Edge
- State Update
- Conditional Routing
- Checkpoint
- Resume

기본 Flow:

```text
State
→ Node Execution
→ State Update
→ Conditional Edge
→ Next Node
→ Final State
```

반드시 설명:

- Node는 Agent 또는 작업 단계
- Edge는 다음 단계 흐름
- State는 Node 간 공유되는 데이터
- Conditional Routing은 상태에 따라 다음 Agent를 선택
- Checkpoint는 중단 후 재개에 사용

주의:

- 구현 상세보다 개념 중심
- LangGraph 문서와 중복될 경우 여기서는 Foundation 수준만 다룸
- 실제 코드 예제는 LangChain / LangGraph Domain에서 상세화 가능

---

# 25. State Schema Rules

State는 Schema를 정의하면 안정성이 높아진다.

필수 포함:

- Field Name
- Type
- Required / Optional
- Default Value
- Update Rule
- Owner Agent

예시:

```json
{
  "userRequest": "string",
  "taskPlan": "array",
  "currentStep": "string",
  "agentOutputs": "object",
  "reviewFindings": "array",
  "status": "string"
}
```

반드시 설명:

- State Schema는 Agent 간 형식 불일치를 줄임
- 필수 필드와 선택 필드를 구분
- 어떤 Agent가 어떤 필드를 수정할 수 있는지 정의 가능
- Status 값은 enum으로 관리 가능

주의:

- Schema가 너무 복잡하면 유지보수 어려움
- 자유 텍스트만 있는 State는 후속 처리 어려움
- 상태 업데이트 시 기존 값 덮어쓰기 주의

---

# 26. State Update Rules

State Update는 명확한 규칙이 필요하다.

필수 포함:

- Append
- Replace
- Merge
- Version
- Timestamp
- Owner
- Validation

Update 방식:

| 방식             | 용도                           |
| ---------------- | ------------------------------ |
| Append           | Review Findings, Logs          |
| Replace          | Current Step, Status           |
| Merge            | Requirements, Decisions        |
| Versioned Update | Project Decision, API Contract |

반드시 설명:

- 모든 Update가 덮어쓰기는 아님
- Review 결과는 누적 Append가 적합
- 현재 단계는 Replace가 적합
- 결정 사항은 변경 이력을 남길 수 있음

주의:

- 중요한 결정이 실수로 삭제되지 않게 함
- 같은 필드에 여러 Agent가 동시에 쓰지 않도록 주의
- Update 후 State Validation 필요

---

# 27. State Compression Rules

State가 길어지면 압축이 필요하다.

필수 포함:

- Summarization
- Key Decision Extraction
- Completed Step Compression
- Error Summary
- Open Issue Summary
- Token Budget

기본 Flow:

```text
Large State
→ Extract Requirements
→ Extract Decisions
→ Extract Open Issues
→ Summarize Completed Steps
→ Keep Active Context
```

반드시 설명:

- 완료된 단계는 요약 가능
- 현재 작업에 필요한 정보는 원문 유지 가능
- 결정 사항과 제약은 절대 누락 금지
- Tool Result는 필요한 필드만 유지

주의:

- 압축 중 중요한 제약 삭제 금지
- 실패 원인 누락 시 같은 오류 반복
- 요약된 State와 원본 State 연결 가능하면 좋음

---

# 28. Troubleshooting Rules

반드시 포함 추천.

형식:

```md
문제:

원인:

해결:
```

---

## Agent가 이전 결정을 잊음

문제:

- 이전에 정한 구조나 규칙을 반영하지 않음

원인:

- Decision Memory 누락
- Shared State에 결정 사항 없음
- Context Passing에서 중요 정보 누락

해결:

- Decision Memory 저장
- Shared State에 decisions 필드 추가
- Handoff에 주요 결정 포함
- 오래된 Summary 갱신

---

## 오래된 정보로 답변함

문제:

- 현재와 맞지 않는 과거 프로젝트 상태를 기준으로 답변함

원인:

- Memory 최신성 확인 없음
- Project Progress 갱신 누락
- 현재 요청보다 Long-term Memory를 우선함

해결:

- Recency Check 수행
- 현재 사용자 요청 우선
- Project Memory 업데이트
- 불확실하면 사용자 확인

---

## Agent 간 상태가 충돌함

문제:

- Backend Agent와 Frontend Agent가 서로 다른 API 계약을 기준으로 작업함

원인:

- Shared State에 API Contract 없음
- Agent별 Local State만 존재
- PM Agent 통합 누락

해결:

- Shared State에 apiContract 저장
- PM Agent가 계약 확정
- Review Agent가 Cross-domain Consistency 확인

---

## State가 너무 커짐

문제:

- Context가 길어져 Agent 응답 품질이 떨어짐

원인:

- 모든 중간 결과 저장
- Tool Result 전체 저장
- 완료된 작업 압축 없음

해결:

- State Compression 적용
- 완료된 단계 요약
- 필요한 Tool Result만 보존
- Open Issue와 Decision 중심으로 유지

---

## Memory가 너무 많이 검색됨

문제:

- 관련 없는 과거 정보가 현재 답변에 섞임

원인:

- Memory Retrieval Filter 부족
- Query가 너무 넓음
- Memory Type 구분 없음

해결:

- Memory Type별 필터링
- 현재 작업과 관련된 Memory만 검색
- Recency / Relevance 기준 적용
- 불필요한 Memory 무시

---

## 민감정보가 Memory에 저장됨

문제:

- API Key, Token, 개인정보가 장기 Memory에 저장됨

원인:

- Memory Update 검증 없음
- Secret과 Config 구분 없음
- Tool Result를 그대로 저장

해결:

- Secret 저장 금지 규칙 추가
- Memory Update 전 민감정보 검사
- Tool Result Redaction
- 사용자 요청 시 삭제

---

# 29. Best Practice Rules

Best Practice:

- State와 Memory를 명확히 구분
- 현재 사용자 요청을 Memory보다 우선
- Shared State에 요구사항, 제약, 결정 사항 저장
- Decision Memory에는 이유와 날짜를 함께 기록
- Long-term Memory는 장기적으로 유용한 정보만 저장
- Working Memory는 작업 완료 후 필요한 내용만 요약 반영
- Checkpoint로 긴 Workflow 복구 가능하게 설계
- State Schema를 정의
- State Update 방식 Append / Replace / Merge 구분
- 오래된 Memory는 Recency Check
- 충돌 정보는 현재 요청 또는 최신 결정 우선
- 민감정보와 Secret은 Memory에 저장하지 않음
- State가 길어지면 Compression 적용

---

# 30. Comparison Rules

Agent Memory & State Management 문서는 비교 기준을 포함한다.

필수 비교 대상:

- State vs Memory
- Short-term Memory vs Long-term Memory
- Working Memory vs Shared State
- Project Memory vs User Preference Memory
- Decision Memory vs Conversation Summary
- Checkpoint vs Memory
- Resume vs Rollback
- Append Update vs Replace Update
- Context Passing vs Memory Retrieval

예시:

| 비교     | State                       | Memory                         |
| -------- | --------------------------- | ------------------------------ |
| 목적     | 현재 Workflow 진행          | 과거 정보 재사용               |
| 수명     | 작업 단위                   | 장기 가능                      |
| 예시     | currentStep, reviewFindings | project stack, user preference |
| 우선순위 | 현재 작업에서 높음          | 검증 후 사용                   |

---

# 31. Checklist Rules

Agent Memory & State Management 문서에는 Checklist를 포함할 수 있다.

예시:

```md
### [Checklist]

- [ ] State와 Memory를 구분했는가?
- [ ] Shared State Schema가 정의되어 있는가?
- [ ] 요구사항과 제약이 State에 저장되는가?
- [ ] 결정 사항이 Decision Memory에 기록되는가?
- [ ] 현재 요청이 Memory보다 우선되는가?
- [ ] 오래된 Memory를 검증하는가?
- [ ] 충돌 Memory 처리 기준이 있는가?
- [ ] Checkpoint / Resume 기준이 있는가?
- [ ] State Update 방식이 정의되어 있는가?
- [ ] State Compression 기준이 있는가?
- [ ] 민감정보 저장 금지 규칙이 있는가?
```

---

# 32. Retrieval Optimization Rules

강조 대상 키워드:

- Agent Memory
- Agent State
- State Management
- Memory Management
- Short-term Memory
- Long-term Memory
- Working Memory
- Shared State
- Project Memory
- User Preference Memory
- Decision Memory
- Conversation Summary
- Context Window
- Context Passing
- Checkpoint
- Resume
- Rollback
- Memory Retrieval
- Memory Update
- Memory Validation
- Memory Conflict
- Memory Expiration
- State Schema
- State Update
- State Compression
- LangGraph State
- Multi-Agent State

키워드 반복 허용.

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

예:

- Agent State가 뭐야?
- Agent Memory랑 State 차이는?
- Short-term Memory와 Long-term Memory 차이는?
- Shared State는 왜 필요해?
- Project Memory에는 뭘 저장해?
- Decision Memory는 어떻게 관리해?
- Checkpoint는 언제 저장해?
- 오래된 Memory는 어떻게 처리해?
- Memory 충돌은 어떻게 해결해?
- State가 너무 커지면 어떻게 해?
- LangGraph State는 뭐야?

---

# 33. Version Rules

기준:

- Modern LLM Agent
- Multi-Agent System Foundation
- RAG 기반 Agent
- Tool Calling 기반 Agent
- Shared State 기반 Workflow
- Checkpoint / Resume 가능 구조
- LangGraph State 개념 확장 가능
- 개인 AI 프로젝트 장기 진행 관리 기준

Legacy 제외:

- 전체 대화를 무조건 Prompt에 넣는 방식
- State와 Memory 구분 없는 방식
- 오래된 Memory를 검증 없이 사용하는 방식
- 민감정보를 Memory에 저장하는 방식
- 종료 후 모든 임시 정보를 장기 저장하는 방식
- Checkpoint 없는 긴 Agent Workflow

---

# 34. Common Mistakes

자주 발생:

- State와 Memory를 혼동
- 현재 요청보다 오래된 Memory를 우선
- 모든 대화 내용을 장기 Memory로 저장
- Decision을 기록하지 않음
- Shared State 없이 Agent 간 전달
- Agent Local State와 Global State 충돌
- State가 너무 커져 Context 품질 저하
- Checkpoint 없이 긴 Workflow 실행
- Resume 전 최신성 확인 없음
- Memory Conflict 처리 기준 없음
- 민감정보를 Memory에 저장
- Tool Result 전체를 State에 저장
- 완료된 작업을 압축하지 않음

---

# 35. Final Goal

Agent Memory & State Management RAG 문서는 Agent가 아래를 수행 가능해야 한다.

- State와 Memory 개념 구분
- Short-term / Long-term Memory 설명
- Working Memory / Shared State 구분
- Project Memory 설계
- User Preference Memory 설계
- Decision Memory 관리 기준 제안
- Conversation Summary 작성 기준 제안
- Checkpoint / Resume / Rollback 기준 설명
- Memory Retrieval / Update 기준 제안
- 오래된 Memory 검증
- Memory Conflict 해결
- State Schema 설계
- State Update 방식 제안
- State Compression 기준 제안
- Multi-Agent State 관리
- Memory / State 관련 문제 Troubleshooting

문서 품질이 장기 프로젝트 Agent의 일관성과 Multi-Agent Workflow 안정성을 결정한다.

---

# Retrieval Queries

### [FAQ]

Q. Agent State가 뭐야?

A.
현재 Workflow가 어느 단계에 있고 어떤 요구사항, 중간 결과, 오류, 다음 작업을 가지고 있는지 나타내는 현재 작업 상태다.

Q. Agent Memory가 뭐야?

A.
이전 대화나 프로젝트 정보를 저장해 이후 작업에서 재사용하는 장기 또는 단기 기억이다.

Q. Agent State와 Memory 차이는?

A.
State는 현재 작업 진행 상태이고, Memory는 과거 정보를 재사용하기 위한 저장 정보다.

Q. Short-term Memory는 뭐야?

A.
현재 대화나 세션 안에서 최근 요청, 수정, 결정 내용을 유지하는 기억이다.

Q. Long-term Memory는 뭐야?

A.
프로젝트 기술 스택, 사용자 선호, 확정 결정처럼 장기적으로 재사용할 가치가 있는 정보다.

Q. Working Memory는 뭐야?

A.
Agent가 현재 작업 중 임시로 사용하는 RAG 검색 결과, Tool 결과, 후보 답안 같은 정보다.

Q. Shared State는 왜 필요해?

A.
여러 Agent가 같은 요구사항, 결정, 중간 결과를 기준으로 작업하게 만들어 Agent 간 일관성을 유지하기 위해 필요하다.

Q. Project Memory에는 뭘 저장해?

A.
프로젝트 목표, 기술 스택, 폴더 구조, Agent 구조, RAG 문서 규칙, 진행 상황, 확정 결정을 저장한다.

Q. User Preference Memory에는 뭘 저장해?

A.
답변 언어, 톤, 문서 형식, 선호 출력 방식처럼 향후 답변 품질을 높이는 정보를 저장한다.

Q. Decision Memory는 왜 필요해?

A.
프로젝트에서 이미 결정한 방향을 유지하고 같은 논의를 반복하지 않기 위해 필요하다.

Q. Conversation Summary는 언제 필요해?

A.
대화가 길어져 Context Window를 많이 차지할 때 핵심 결정, 진행 상황, 다음 작업을 압축하기 위해 필요하다.

Q. Checkpoint는 뭐야?

A.
긴 Workflow 중간 상태를 저장해 실패하거나 중단되었을 때 이어서 진행할 수 있게 하는 저장 지점이다.

Q. Resume은 어떻게 해?

A.
마지막 Checkpoint를 불러오고 현재 요청과 일치하는지 확인한 뒤 완료된 단계와 남은 단계를 구분해 이어간다.

Q. Rollback은 뭐야?

A.
잘못된 State 업데이트나 실패한 변경을 이전 정상 상태로 되돌리는 작업이다.

Q. Memory Retrieval은 어떻게 해?

A.
현재 요청에 필요한 정보만 검색하고, 최신성, 관련성, 충돌 여부를 확인한 뒤 사용한다.

Q. Memory Update는 언제 해?

A.
장기적으로 유용한 프로젝트 결정, 기술 스택, 사용자 선호, 문서 규칙이 새로 확정되었을 때 수행한다.

Q. 오래된 Memory는 어떻게 처리해?

A.
Recency Check를 하고 현재 요청이나 최신 결정과 충돌하면 업데이트하거나 무시한다.

Q. Memory 충돌은 어떻게 해결해?

A.
현재 사용자 요청, 명시적 정정, 최신 프로젝트 결정, 최근 대화, 장기 Memory 순으로 우선순위를 둔다.

Q. State가 너무 커지면 어떻게 해?

A.
완료된 단계는 요약하고, 결정 사항과 열린 이슈 중심으로 압축하며, 불필요한 Tool Result는 제거한다.

Q. LangGraph State는 뭐야?

A.
Node와 Edge로 구성된 Workflow에서 각 Node가 읽고 업데이트하는 공유 상태 데이터다.

Q. 민감정보를 Memory에 저장해도 돼?

A.
API Key, 비밀번호, 토큰, 개인정보 같은 민감정보는 저장하지 않는 것이 원칙이다.

Q. Agent Memory & State Management의 최종 목표는 뭐야?

A.
Agent가 장기 프로젝트 맥락을 유지하면서도 현재 작업 상태를 안정적으로 관리하고, 오래된 정보나 충돌 정보를 안전하게 처리하게 만드는 것이다.
