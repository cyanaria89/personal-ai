# LangChain & LangGraph Part07 Checkpoint Memory Human ReviewFix

---

# 1. Checkpoint Core

## 1.1 Checkpoint 기본 개념

### [개념]

Checkpoint는 LangGraph Workflow의 중간 State를 저장하는 구조다.

Checkpoint는 긴 Agent Workflow에서 중단, 재개, 오류 복구, Human Approval 대기 상태를 관리하는 데 사용한다.

기본 Flow:

```text
Node Execution
→ State Update
→ Save Checkpoint
→ Resume Later
```

Checkpoint는 현재 Workflow의 State Snapshot을 저장한다.

Checkpoint는 Memory와 다르다.

Memory는 과거 정보를 재사용하기 위한 구조이고, Checkpoint는 현재 Workflow를 이어가기 위한 상태 저장이다.

---

### [핵심]

- Checkpoint는 Workflow 중간 State를 저장한다.
- Checkpoint는 중단 후 재개에 사용한다.
- Checkpoint는 Human-in-the-loop와 함께 사용하기 좋다.
- Checkpoint는 실패 복구에 도움을 준다.
- Thread ID 또는 Session ID 기준으로 관리할 수 있다.
- 오래된 Checkpoint는 재개 전 검증이 필요하다.
- 민감정보를 Checkpoint에 저장하지 않는다.

---

### [실무]

2026 실무 기준 LangGraph Agent Workflow는 긴 작업과 승인 대기 작업에 Checkpoint를 적용한다.

Checkpoint 적용 대상:

| 상황                 | Checkpoint 필요성 |
| -------------------- | ----------------- |
| Multi-Agent Workflow | 높음              |
| Review / Fix Loop    | 높음              |
| Human Approval 대기  | 높음              |
| 장시간 Tool 실행     | 중간              |
| 배포 전 승인         | 높음              |
| 파일 수정 전 승인    | 높음              |
| 단순 RAG 답변        | 낮음              |

Checkpoint 저장 데이터 예시:

```json
{
  "thread_id": "devteam-2026-001",
  "current_step": "waiting_approval",
  "user_request": "Backend API 파일 수정",
  "task_type": "backend",
  "requirements": [
    "Controller-Service-Repository 구조 유지",
    "JWT 인증 로직 유지"
  ],
  "agent_outputs": {
    "backend": "수정안 초안"
  },
  "approval_required": true,
  "status": "waiting_approval"
}
```

Checkpoint 재개 Flow:

```text
Load Checkpoint
→ Validate State
→ Compare with Latest User Request
→ Resume Node
→ Continue Workflow
```

---

### [FAQ]

Q. Checkpoint가 뭐야?

A.
LangGraph Workflow의 중간 State를 저장해 중단 후 재개하거나 오류를 복구하는 구조다.

Q. Checkpoint는 왜 필요해?

A.
긴 Agent Workflow, Human Approval 대기, 실패 복구, Review / Fix Loop 재개에 필요하다.

Q. Checkpoint와 Memory는 달라?

A.
다르다. Checkpoint는 현재 Workflow 상태 저장이고, Memory는 과거 정보를 재사용하기 위한 구조다.

Q. Checkpoint는 언제 저장해?

A.
Node 실행 후 State가 업데이트될 때, 승인 대기 전, 긴 작업 중간, 오류 복구 지점에서 저장한다.

Q. 오래된 Checkpoint를 바로 재개해도 돼?

A.
권장하지 않는다. 현재 사용자 요청과 충돌하지 않는지 State Validation 후 재개해야 한다.

---

# 2. Thread ID

## 2.1 Thread ID와 Workflow 식별

### [개념]

Thread ID는 Checkpoint를 특정 대화, 작업, Workflow와 연결하기 위한 식별자다.

LangGraph Workflow가 여러 사용자 요청이나 여러 작업을 동시에 처리하려면 Thread ID 기준으로 State를 구분해야 한다.

기본 구조:

```text
User / Session / Task
→ Thread ID
→ Checkpoint Store
→ State Snapshot
```

Thread ID가 없으면 서로 다른 Workflow의 State가 섞일 수 있다.

---

### [핵심]

- Thread ID는 Workflow 상태를 식별한다.
- 하나의 사용자 작업에는 하나의 Thread ID를 부여할 수 있다.
- Checkpoint는 Thread ID 기준으로 저장하고 조회한다.
- Human Approval 재개 시 Thread ID가 필요하다.
- Thread ID가 잘못되면 다른 작업의 State를 불러올 수 있다.
- Thread ID는 예측 불가능하거나 충돌 없는 값이 좋다.
- Thread ID에 민감정보를 직접 넣지 않는다.

---

### [실무]

Thread ID 사용 기준:

| 기준            | 설명                 |
| --------------- | -------------------- |
| user_session_id | 사용자 세션 기준     |
| task_id         | 작업 단위 기준       |
| workflow_id     | Graph 실행 단위 기준 |
| conversation_id | 대화 기준            |
| approval_id     | 승인 대기 기준       |

Thread ID 예시:

```text
devteam-workflow-20260630-0001
rag-review-thread-0007
backend-agent-task-0132
approval-request-0042
```

Thread ID 금지 예시:

```text
user-password-1234
api-key-sk-...
resident-id-...
private-email-body-...
```

Thread ID 설계 주의:

- 개인정보를 직접 포함하지 않는다.
- API Key, Token, Secret을 포함하지 않는다.
- 사람이 의미를 알 수 있는 최소 정보만 포함한다.
- 충돌 가능성을 낮춘다.
- 승인 재개 시 동일 Thread ID를 사용한다.

---

### [FAQ]

Q. Thread ID가 뭐야?

A.
Checkpoint를 특정 Workflow, 작업, 대화와 연결하기 위한 식별자다.

Q. Thread ID는 왜 필요해?

A.
여러 Workflow의 State가 섞이지 않도록 구분하고 중단된 작업을 정확히 재개하기 위해 필요하다.

Q. Human Approval에도 Thread ID가 필요해?

A.
필요하다. 승인 대기 중인 Workflow를 정확히 찾아 재개해야 하기 때문이다.

Q. Thread ID에 사용자 개인정보를 넣어도 돼?

A.
안 된다. 개인정보, API Key, Token, 민감정보는 Thread ID에 포함하지 않는다.

Q. Thread ID가 틀리면 어떻게 돼?

A.
다른 Workflow의 Checkpoint를 불러와 잘못된 작업이 실행될 수 있다.

---

# 3. Persistence

## 3.1 Checkpoint 저장소

### [개념]

Persistence는 Checkpoint와 Workflow State를 저장소에 유지하는 방식이다.

In-memory 저장은 프로세스가 종료되면 사라진다.

장기 실행 Agent Workflow나 Human Approval을 사용하려면 영속 저장소가 필요하다.

기본 Flow:

```text
State Snapshot
→ Checkpoint Saver
→ Persistent Store
→ Resume Workflow
```

---

### [핵심]

- Persistence는 Checkpoint를 저장소에 유지한다.
- In-memory는 테스트와 단기 실행에 적합하다.
- SQLite, PostgreSQL 같은 저장소는 재시작 후 재개에 유리하다.
- 장기 Workflow는 영속 저장소를 사용한다.
- 저장 전 민감정보 포함 여부를 확인한다.
- Checkpoint 보존 기간과 삭제 정책이 필요하다.
- 저장된 State는 버전 관리가 필요할 수 있다.

---

### [실무]

Checkpoint 저장소 선택 기준:

| 저장소         | 사용 기준                  |
| -------------- | -------------------------- |
| In-memory      | 로컬 테스트, 짧은 Workflow |
| SQLite         | 개인 서버, 단일 인스턴스   |
| PostgreSQL     | 운영 환경, 다중 Workflow   |
| Redis          | 빠른 임시 상태, TTL 필요   |
| File Store     | 단순 로컬 저장             |
| Object Storage | 장기 보관, 대용량 로그     |

Persistence 설계 기준:

| 항목           | 기준                        |
| -------------- | --------------------------- |
| durability     | 재시작 후 복구 가능 여부    |
| encryption     | 민감 데이터 보호            |
| ttl            | 오래된 Checkpoint 자동 정리 |
| version        | State Schema 변경 대응      |
| backup         | 복구 가능성                 |
| access_control | 권한 제한                   |
| audit          | 승인, 재개, 실패 기록       |

Checkpoint 저장 금지 데이터:

- API Key
- Access Token
- Refresh Token
- 비밀번호
- 주민번호
- 민감한 개인정보
- 외부 발송 전 원문 전체
- Secret 환경 변수
- 장기 보관 불필요한 Tool 로그

---

### [FAQ]

Q. Persistence가 뭐야?

A.
Checkpoint와 Workflow State를 저장소에 유지해 재시작 후에도 재개할 수 있게 하는 방식이다.

Q. In-memory Checkpoint는 언제 써?

A.
로컬 테스트나 짧은 Workflow처럼 재시작 후 복구가 필요 없는 경우에 사용한다.

Q. 개인 AI 서버에서는 어떤 저장소가 현실적이야?

A.
초기에는 SQLite나 파일 기반 저장이 현실적이고, 확장 시 PostgreSQL을 고려할 수 있다.

Q. Checkpoint 저장소에 민감정보를 저장해도 돼?

A.
안 된다. API Key, Token, 비밀번호, 개인정보는 저장하지 않거나 마스킹해야 한다.

Q. 오래된 Checkpoint는 어떻게 관리해?

A.
TTL, 보존 기간, 수동 정리, 완료 상태 삭제 정책을 정해야 한다.

---

# 4. Memory Core

## 4.1 Memory 기본 개념

### [개념]

Memory는 과거 대화, 사용자 선호, 작업 이력, 장기 지식을 재사용하기 위한 구조다.

Memory는 현재 Workflow의 실행 상태인 State와 다르다.

Memory는 Checkpoint와도 다르다.

구분:

```text
State
→ 현재 Workflow 실행 상태

Checkpoint
→ 현재 Workflow State Snapshot 저장

Memory
→ 과거 정보 재사용 구조
```

Memory는 Agent가 과거 정보를 참고할 수 있게 하지만, 오래된 정보는 검증이 필요하다.

---

### [핵심]

- Memory는 과거 정보를 재사용하기 위한 구조다.
- State는 현재 Workflow 실행 상태다.
- Checkpoint는 현재 Workflow 중간 저장이다.
- Memory는 무조건 대화 전체를 저장하는 것이 아니다.
- Summary Memory는 긴 대화를 요약해 저장한다.
- Retrieval Memory는 필요한 정보를 검색해 사용한다.
- 현재 사용자 요청이 Memory보다 우선한다.
- 민감정보는 Memory에 저장하지 않는다.

---

### [실무]

Memory 종류:

| Memory              | 목적                            |
| ------------------- | ------------------------------- |
| Conversation Memory | 최근 대화 맥락 유지             |
| Summary Memory      | 긴 대화 요약                    |
| Retrieval Memory    | 과거 정보 검색                  |
| Long-term Memory    | 장기 선호와 설정 저장           |
| Episodic Memory     | 특정 작업 이력 저장             |
| Semantic Memory     | 일반 지식 또는 사용자 지식 저장 |

Memory 사용 기준:

| 상황                      | Memory 사용    |
| ------------------------- | -------------- |
| 사용자 선호 반영          | 가능           |
| 이전 프로젝트 규칙 재사용 | 가능           |
| 과거 오류 패턴 참고       | 가능           |
| 현재 요청과 충돌          | 현재 요청 우선 |
| 오래된 기술 정보          | 검증 후 사용   |
| 민감정보                  | 저장 금지      |

Memory 관리 Flow:

```text
User Request
→ Relevant Memory Retrieve
→ Validate Freshness
→ Compare with Current Request
→ Use or Ignore
```

---

### [FAQ]

Q. Memory가 뭐야?

A.
과거 대화, 사용자 선호, 작업 이력을 재사용하기 위한 구조다.

Q. Memory와 State는 달라?

A.
다르다. State는 현재 Workflow 실행 상태이고 Memory는 과거 정보를 재사용하기 위한 구조다.

Q. Memory와 Checkpoint는 달라?

A.
다르다. Checkpoint는 현재 Workflow를 재개하기 위한 저장이고 Memory는 과거 정보를 참조하기 위한 저장이다.

Q. 대화 전체를 Memory에 저장하면 좋아?

A.
권장하지 않는다. 필요한 정보만 요약하거나 검색 가능한 형태로 저장해야 한다.

Q. 현재 요청과 Memory가 충돌하면 무엇을 우선해?

A.
현재 사용자 요청을 우선해야 한다.

---

# 5. Memory Design

## 5.1 Agent Memory 설계

### [개념]

Agent Memory Design은 Agent가 어떤 과거 정보를 저장하고, 언제 검색하고, 어떻게 사용할지 정의하는 설계다.

Memory는 Agent 성능을 높일 수 있지만, 부정확하거나 오래된 Memory는 오류를 만든다.

기본 Flow:

```text
Task
→ Retrieve Relevant Memory
→ Validate Memory
→ Inject into Prompt or State
→ Execute Agent
```

Memory는 필요할 때만 사용해야 한다.

---

### [핵심]

- Memory에 저장할 정보와 저장하지 않을 정보를 구분한다.
- Memory 검색 기준을 정의한다.
- Memory 최신성을 검증한다.
- 현재 요청과 충돌하는 Memory는 사용하지 않는다.
- Memory는 Prompt에 과도하게 넣지 않는다.
- Memory는 State와 분리해 관리한다.
- 민감정보 저장 금지 기준을 둔다.
- Memory 사용 내역을 추적할 수 있어야 한다.

---

### [실무]

개인 AI 개발팀 Memory 예시:

| Memory 유형        | 저장 가능 정보                    |
| ------------------ | --------------------------------- |
| Project Rules      | RAG 문서 제작 규칙                |
| Agent Preferences  | 순차 실행 우선, Review 필수       |
| Stack Context      | AnythingLLM, Ollama, Local LLM    |
| Hardware Context   | RAM, Local LLM 제약               |
| Document Structure | RAG Foundation, RAG Expert 구조   |
| Past Decisions     | LangGraph는 Agent Workflow에 사용 |
| Error Patterns     | Retriever 실패, Chunk 문제        |

Memory 저장 금지:

| 금지 정보          | 이유            |
| ------------------ | --------------- |
| API Key            | 보안 위험       |
| 비밀번호           | 보안 위험       |
| Access Token       | 계정 탈취 위험  |
| Refresh Token      | 장기 보안 위험  |
| 민감 개인정보      | 프라이버시 위험 |
| 임시 작업 내용     | 장기 가치 부족  |
| 검증되지 않은 추측 | 오류 전파       |

Memory Injection 기준:

```text
Relevant Memory
→ Short Summary
→ Current Request와 충돌 여부 확인
→ Prompt Context로 일부 사용
```

Memory 사용 금지 패턴:

- 오래된 Memory를 검증 없이 사용
- 현재 요청보다 Memory를 우선
- 모든 Memory를 Prompt에 삽입
- 민감정보를 장기 저장
- 프로젝트가 다른데 Memory를 혼합
- 임시 작업 상태를 장기 Memory로 저장

---

### [FAQ]

Q. Agent Memory Design이 뭐야?

A.
Agent가 어떤 과거 정보를 저장하고 언제 검색해 사용할지 정하는 설계다.

Q. Memory는 항상 사용해야 해?

A.
아니다. 현재 요청에 관련 있고 최신성이 확인된 Memory만 사용해야 한다.

Q. Memory를 Prompt에 많이 넣으면 좋아?

A.
좋지 않다. Context가 길어지고 관련 없는 정보가 Agent 판단을 흐릴 수 있다.

Q. 개인 AI 프로젝트에서 Memory에 저장할 만한 것은?

A.
RAG 문서 규칙, Agent 구조 결정, 로컬 LLM 제약, 프로젝트 디렉터리 구조 같은 장기 유효 정보다.

Q. Memory에 저장하면 안 되는 것은?

A.
API Key, 비밀번호, Token, 민감 개인정보, 검증되지 않은 추측, 임시 작업 상태다.

---

# 6. Human-in-the-loop Core

## 6.1 Human-in-the-loop 기본 개념

### [개념]

Human-in-the-loop는 Agent Workflow 중 사용자 승인, 선택, 확인이 필요한 지점에서 Workflow를 중단하고 사용자의 결정을 받은 뒤 재개하는 구조다.

Agent가 모든 작업을 자동으로 실행하면 위험할 수 있다.

특히 파일 변경, DB 변경, 배포, 비용 발생, 외부 발송 같은 Side Effect가 있는 작업은 Human Approval이 필요하다.

기본 Flow:

```text
Agent Proposes Action
→ Interrupt
→ User Approval
→ Resume Workflow
```

---

### [핵심]

- Human-in-the-loop는 사용자 결정을 Workflow에 포함한다.
- 위험 작업 전 사용자 승인이 필요하다.
- 정보가 부족하면 Clarification을 요청할 수 있다.
- 승인 대기 상태는 Checkpoint로 저장한다.
- 사용자 결정은 State에 반영한다.
- 승인 범위를 넘어서는 실행은 금지한다.
- 승인 후에도 Review가 필요할 수 있다.

---

### [실무]

Human Approval 대상:

| 작업               | 승인 필요 이유 |
| ------------------ | -------------- |
| 파일 수정          | 원본 변경      |
| 파일 삭제          | 데이터 손실    |
| DB 변경            | 데이터 손상    |
| Production 배포    | 운영 장애      |
| 외부 이메일 발송   | 외부 영향      |
| 비용 발생 API 호출 | 금전 비용      |
| 권한 변경          | 보안 위험      |
| 대량 코드 수정     | 범위 오류      |
| 테스트 데이터 삭제 | 복구 어려움    |

Human-in-the-loop State 예시:

```json
{
  "status": "waiting_approval",
  "approval_required": true,
  "proposed_action": "write_file",
  "approval_scope": {
    "path": "Backend/src/main/java/.../AuthController.java",
    "operation": "modify",
    "risk_level": "medium"
  },
  "user_decision": null
}
```

Approval Flow:

```text
Risk Detection
→ Approval Request
→ Save Checkpoint
→ User Decision
→ Resume
→ Execute or Cancel
```

---

### [FAQ]

Q. Human-in-the-loop가 뭐야?

A.
Agent Workflow 중 사용자 승인이나 선택이 필요한 지점에서 중단하고 결정 후 재개하는 구조다.

Q. 언제 Human Approval이 필요해?

A.
파일 수정, DB 변경, 배포, 비용 발생, 외부 발송처럼 Side Effect가 있는 작업 전에 필요하다.

Q. 승인 대기 상태는 어떻게 유지해?

A.
Checkpoint에 State를 저장하고 Thread ID 기준으로 재개한다.

Q. 사용자가 승인하면 바로 실행해도 돼?

A.
승인 범위 안에서만 실행해야 하며, 위험도에 따라 실행 후 Review가 필요할 수 있다.

Q. 승인 범위를 넘어서는 작업은 가능해?

A.
불가능하다. 사용자가 승인한 작업과 범위 안에서만 실행해야 한다.

---

# 7. Interrupt and Resume

## 7.1 중단과 재개 구조

### [개념]

Interrupt는 Workflow 실행 중 사용자 입력이나 승인이 필요할 때 실행을 중단하는 구조다.

Resume은 사용자의 결정이 들어온 뒤 저장된 Checkpoint에서 Workflow를 이어가는 구조다.

기본 Flow:

```text
Node Execution
→ Need Human Decision
→ Interrupt
→ Save Checkpoint
→ User Input
→ Resume
→ Continue Node
```

Interrupt와 Resume은 Human-in-the-loop 구현의 핵심이다.

---

### [핵심]

- Interrupt는 사용자 결정이 필요한 시점에 발생한다.
- Interrupt 전 State를 저장해야 한다.
- Resume 시 Checkpoint를 불러온다.
- Resume 전 State Validation을 수행한다.
- 사용자 결정은 State에 기록한다.
- 오래된 Checkpoint는 현재 요청과 충돌 여부를 확인한다.
- Resume 후 다음 Node가 명확해야 한다.

---

### [실무]

Interrupt 발생 조건:

| 조건                   | 예시                   |
| ---------------------- | ---------------------- |
| approval_required      | 파일 수정, 배포        |
| clarification_required | 요구사항 불명확        |
| missing_context        | 문서 근거 부족         |
| conflict_detected      | Source 간 충돌         |
| high_risk_tool         | DB 변경, 삭제          |
| max_iteration_reached  | Review / Fix 한도 도달 |

Resume State 예시:

```json
{
  "thread_id": "approval-request-0042",
  "status": "approved",
  "user_decision": "approve",
  "approval_scope": {
    "operation": "modify",
    "path": "Backend/src/main/java/.../AuthController.java"
  },
  "resume_node": "tool_node"
}
```

Resume 전 검증:

- Thread ID가 맞는가?
- Checkpoint가 존재하는가?
- 승인 범위가 명확한가?
- 현재 사용자 요청과 충돌하지 않는가?
- 위험 작업 범위가 바뀌지 않았는가?
- 다음 Node가 명확한가?

---

### [FAQ]

Q. Interrupt가 뭐야?

A.
Workflow 실행 중 사용자 승인이나 입력이 필요할 때 실행을 중단하는 구조다.

Q. Resume은 뭐야?

A.
사용자 결정 후 저장된 Checkpoint에서 Workflow를 이어가는 구조다.

Q. Interrupt 전 무엇을 해야 해?

A.
현재 State를 Checkpoint로 저장해야 한다.

Q. Resume 전 무엇을 확인해야 해?

A.
Thread ID, Checkpoint, 승인 범위, 현재 요청과의 충돌 여부, 다음 Node를 확인해야 한다.

Q. 오래된 Checkpoint를 재개하면 위험한 이유는?

A.
현재 요청이나 파일 상태가 바뀌었을 수 있어 잘못된 작업이 실행될 수 있기 때문이다.

---

# 8. Review / Fix Core

## 8.1 Review / Fix Loop 기본 개념

### [개념]

Review / Fix Loop는 Agent가 만든 초안을 검토하고, 문제가 있으면 수정한 뒤 다시 검토하는 반복 구조다.

LangGraph는 Review / Fix Loop에 적합하다.

기본 Flow:

```text
Draft Node
→ Review Node
→ if pass: Final Node
→ if fail: Fix Node
→ Review Node
```

Review / Fix Loop에는 반드시 Max Iteration과 Stop Condition이 필요하다.

---

### [핵심]

- Draft Node는 초안을 생성한다.
- Review Node는 초안을 검토한다.
- Fix Node는 Review Findings를 반영한다.
- Conditional Edge는 pass/fail을 기준으로 분기한다.
- Max Iteration은 무한 반복을 방지한다.
- Critical Issue와 Minor Issue를 구분한다.
- Max Iteration 도달 시 Final With Warning으로 종료할 수 있다.

---

### [실무]

Review / Fix Loop State 예시:

```python
from typing import TypedDict, Literal

class ReviewFixState(TypedDict):
    draft_output: str
    review_result: Literal["pass", "fail", "warning"]
    review_findings: list[str]
    severity: Literal["none", "minor", "major", "critical"]
    fix_count: int
    max_fix_count: int
    fixed_output: str
    status: str
```

Review Router 예시:

```text
if review_result == "pass":
    → Final Node

if review_result == "fail" and fix_count < max_fix_count:
    → Fix Node

if fix_count >= max_fix_count:
    → Final With Warning
```

Review 기준:

| 기준              | 설명                      |
| ----------------- | ------------------------- |
| Requirement Match | 사용자 요구사항 충족 여부 |
| RAG Grounding     | 문서 근거 기반 여부       |
| Code Correctness  | 코드 동작 가능성          |
| Security Risk     | 보안 위험 여부            |
| Consistency       | 용어, 구조, 스타일 일관성 |
| Completeness      | 누락 여부                 |
| Maintainability   | 유지보수성                |
| Output Format     | 요구 출력 형식 준수 여부  |

---

### [FAQ]

Q. Review / Fix Loop가 뭐야?

A.
초안을 생성한 뒤 검토하고, 실패하면 수정 후 다시 검토하는 반복 Workflow다.

Q. Review / Fix Loop는 왜 LangGraph에 적합해?

A.
조건 분기, 반복, State 관리, 종료 조건을 명확히 설계할 수 있기 때문이다.

Q. Max Iteration은 왜 필요해?

A.
무한 수정 루프를 방지하기 위해 필요하다.

Q. Review Node는 무엇을 검토해?

A.
요구사항 충족, RAG 근거, 코드 정확성, 보안 위험, 누락, 일관성, 출력 형식을 검토한다.

Q. Fix Node는 무엇을 기준으로 수정해?

A.
Review Node가 State에 저장한 review_findings를 기준으로 수정한다.

---

# 9. Review Node

## 9.1 Review Node 설계

### [개념]

Review Node는 Agent Output이나 Draft Output을 검토해 pass, fail, warning 상태를 판단하는 Node다.

Review Node는 단순 감상이 아니라 고정된 기준에 따라 검토 결과를 구조화해야 한다.

기본 Flow:

```text
Draft Output
→ Review Node
→ Review Criteria
→ Review Result
→ State Update
```

Review Node는 Review Findings를 State에 저장한다.

---

### [핵심]

- Review Node는 검토 기준을 고정한다.
- Review Result는 구조화한다.
- pass, fail, warning을 구분한다.
- Severity를 구분한다.
- Fix가 필요한 항목을 findings로 기록한다.
- Unsupported Claim을 탐지한다.
- 위험 변경이나 승인 누락을 검출한다.
- Review Node 자체도 출력 형식을 지켜야 한다.

---

### [실무]

Review Node Output Schema:

```json
{
  "review_result": "fail",
  "severity": "major",
  "findings": [
    {
      "type": "missing_requirement",
      "message": "Human Approval 기준이 누락됨",
      "target_section": "Tool Permission"
    },
    {
      "type": "unsupported_claim",
      "message": "문서 근거 없는 운영 심화 설명 포함",
      "target_section": "Production Agent Platform"
    }
  ],
  "fix_required": true,
  "next_action": "fix"
}
```

Review Severity 기준:

| Severity | 의미                    | 처리                    |
| -------- | ----------------------- | ----------------------- |
| none     | 문제 없음               | Final                   |
| minor    | 사소한 개선             | Warning 또는 Fix        |
| major    | 요구사항 누락           | Fix                     |
| critical | 안전, 보안, 데이터 위험 | Fix 또는 Human Approval |

Review Node 검토 항목:

| 항목      | 질문                                   |
| --------- | -------------------------------------- |
| 요구사항  | 사용자가 요청한 내용이 모두 반영됐는가 |
| 출력 형식 | 지정된 형식을 지켰는가                 |
| 문서 근거 | RAG Context 기반인가                   |
| 용어 통일 | 용어가 일관되는가                      |
| 안전성    | 위험 작업을 자동 실행하지 않는가       |
| 완전성    | 필수 Section이 누락되지 않았는가       |
| 연결성    | 이전 Part와 충돌하지 않는가            |

---

### [FAQ]

Q. Review Node가 뭐야?

A.
Agent Output을 고정된 기준으로 검토하고 pass, fail, warning 결과를 State에 저장하는 Node다.

Q. Review Result는 왜 구조화해야 해?

A.
Fix Node와 Conditional Edge가 결과를 안정적으로 사용할 수 있게 하기 위해 필요하다.

Q. Review Severity는 왜 필요해?

A.
사소한 문제와 치명적 문제를 구분해 Fix 또는 Final 경로를 결정하기 위해 필요하다.

Q. Unsupported Claim은 뭐야?

A.
검색된 문서나 요구사항에 근거하지 않은 주장이다.

Q. Review Node가 확인해야 할 핵심은?

A.
요구사항 충족, 출력 형식, 문서 근거, 누락, 안전성, 이전 Part와의 일관성이다.

---

# 10. Fix Node

## 10.1 Fix Node 설계

### [개념]

Fix Node는 Review Node가 발견한 문제를 기준으로 Draft Output을 수정하는 Node다.

Fix Node는 전체를 무작정 다시 생성하는 것이 아니라 Review Findings를 타깃으로 수정해야 한다.

기본 Flow:

```text
Draft Output
→ Review Findings
→ Fix Node
→ Fixed Output
→ Review Node
```

Fix Node는 수정 후 fix_count를 증가시키고 다시 Review Node로 보낸다.

---

### [핵심]

- Fix Node는 Review Findings를 기준으로 수정한다.
- 전체 재작성보다 타깃 수정이 안정적이다.
- Fix 후 fix_count를 증가시킨다.
- Fix 결과는 다시 Review Node로 보내야 한다.
- Fix가 새 문제를 만들 수 있으므로 재검토가 필요하다.
- Critical Issue는 우선 수정한다.
- Max Iteration 도달 시 Final With Warning으로 종료한다.

---

### [실무]

Fix Node Input:

```json
{
  "draft_output": "...",
  "review_findings": [
    {
      "type": "missing_requirement",
      "message": "Checkpoint와 Memory 차이 설명 부족",
      "target_section": "Memory Core"
    }
  ],
  "fix_count": 0,
  "max_fix_count": 2
}
```

Fix Node Output:

```json
{
  "fixed_output": "...",
  "fix_summary": [
    "Memory와 Checkpoint 차이 설명 추가",
    "FAQ에 Checkpoint vs Memory 질문 추가"
  ],
  "fix_count": 1,
  "status": "fixed"
}
```

Fix 우선순위:

| 우선순위 | 대상                 |
| -------- | -------------------- |
| 1        | 안전 문제, 보안 문제 |
| 2        | 사용자 요구사항 누락 |
| 3        | 출력 형식 위반       |
| 4        | 문서 근거 부족       |
| 5        | 용어 불일치          |
| 6        | 표현 개선            |

Fix 금지:

- Review Findings와 무관한 대규모 변경
- 출력 형식 임의 변경
- 요구사항 삭제
- Source 없는 주장 추가
- 기존 정상 Section 파괴
- fix_count 증가 누락

---

### [FAQ]

Q. Fix Node가 뭐야?

A.
Review Findings를 기준으로 Draft Output을 수정하는 Node다.

Q. Fix Node는 전체를 다시 생성해야 해?

A.
권장하지 않는다. Review Findings를 기준으로 필요한 부분을 타깃 수정하는 것이 안정적이다.

Q. Fix 후 다시 Review해야 해?

A.
해야 한다. 수정 과정에서 새 문제가 생길 수 있기 때문이다.

Q. fix_count는 왜 필요해?

A.
Review / Fix Loop가 무한 반복되지 않도록 반복 횟수를 관리하기 위해 필요하다.

Q. Fix Node가 하면 안 되는 것은?

A.
Review Findings와 무관한 대규모 변경, 요구사항 삭제, 출력 형식 변경, 근거 없는 주장 추가다.

---

# 11. Approval + Review Integration

## 11.1 승인과 검토 통합 구조

### [개념]

Approval + Review Integration은 위험 작업에 대해 사용자 승인을 받고, 실행 후 Review Node가 결과를 검증하는 구조다.

Human Approval은 실행 허가를 의미하지만 결과 품질 보장을 의미하지 않는다.

따라서 위험 작업은 승인 후 실행하고, 실행 결과를 Review Node에서 검토하는 것이 안전하다.

기본 Flow:

```text
Agent Proposal
→ Approval Node
→ User Approves
→ Tool Node
→ Review Node
→ Final Node
```

---

### [핵심]

- Human Approval은 실행 허가다.
- Review Node는 실행 결과 품질 검증이다.
- 승인과 검토는 역할이 다르다.
- 승인 범위를 State에 저장한다.
- Tool 실행 결과를 Review Node가 검토한다.
- 승인 범위를 초과한 실행은 실패로 처리한다.
- Critical Issue 발생 시 다시 사용자에게 보고한다.

---

### [실무]

승인 후 검토가 필요한 작업:

| 작업      | Review 기준               |
| --------- | ------------------------- |
| 파일 수정 | 변경 범위, 요구사항 충족  |
| DB 변경   | 영향 범위, 롤백 가능성    |
| 배포      | 환경, 로그, 실패 여부     |
| 외부 발송 | 수신자, 내용, 첨부        |
| 권한 변경 | 대상, 권한 범위           |
| 대량 수정 | 변경 파일 목록, 영향 범위 |

Approval + Review State 예시:

```json
{
  "approval_required": true,
  "user_decision": "approve",
  "approval_scope": {
    "operation": "modify",
    "allowed_paths": ["Backend/src/main/java/com/example/auth/AuthService.java"]
  },
  "tool_result": {
    "status": "success",
    "modified_files": [
      "Backend/src/main/java/com/example/auth/AuthService.java"
    ]
  },
  "review_result": "pass"
}
```

승인 범위 위반 예시:

```json
{
  "review_result": "fail",
  "severity": "critical",
  "findings": ["승인된 파일 외 다른 파일이 수정됨"],
  "next_action": "report_to_user"
}
```

---

### [FAQ]

Q. Human Approval을 받으면 Review가 필요 없어?

A.
아니다. 승인은 실행 허가이고 Review는 실행 결과 품질과 안전성 검증이다.

Q. 승인 범위는 어디에 저장해?

A.
State의 approval_scope 필드에 저장한다.

Q. 승인 범위를 초과하면 어떻게 해?

A.
Critical Issue로 처리하고 사용자에게 보고해야 한다.

Q. Tool 실행 결과는 누가 검토해?

A.
Review Node가 tool_result와 approval_scope를 기준으로 검토한다.

Q. 위험 작업의 안전한 흐름은?

A.
Proposal → Approval → Checkpoint → Tool Execution → Review → Final 순서다.

---

# 12. Part07 Checklist

## 12.1 Checkpoint Memory Human ReviewFix Checklist

### [Checklist]

- [ ] Checkpoint와 Memory를 구분했는가?
- [ ] Checkpoint와 State Snapshot의 관계를 설명했는가?
- [ ] Thread ID 기준으로 Workflow를 식별하는가?
- [ ] Checkpoint 재개 전 State Validation을 수행하는가?
- [ ] Checkpoint에 민감정보를 저장하지 않는가?
- [ ] Persistence 저장소 기준이 있는가?
- [ ] 오래된 Checkpoint 정리 기준이 있는가?
- [ ] Memory와 State를 구분했는가?
- [ ] Memory와 Checkpoint를 구분했는가?
- [ ] 현재 요청이 Memory보다 우선한다는 기준이 있는가?
- [ ] Memory에 저장할 정보와 금지 정보를 구분했는가?
- [ ] Human Approval이 필요한 작업 기준이 있는가?
- [ ] Interrupt 전 Checkpoint를 저장하는가?
- [ ] Resume 전 Thread ID와 승인 범위를 검증하는가?
- [ ] 승인 범위를 초과한 실행을 금지하는가?
- [ ] Review / Fix Loop에 Max Iteration이 있는가?
- [ ] Review Node Output이 구조화되어 있는가?
- [ ] Review Severity를 구분하는가?
- [ ] Fix Node가 Review Findings 기준으로 수정하는가?
- [ ] Fix 후 재검토를 수행하는가?
- [ ] Approval 후 Review Node가 실행 결과를 검증하는가?
- [ ] Critical Issue 발생 시 사용자에게 보고하는 경로가 있는가?

---

# Retrieval Queries

### [FAQ]

Q. Checkpoint가 뭐야?
A. LangGraph Workflow의 중간 State를 저장해 중단 후 재개하거나 오류를 복구하는 구조다.

Q. Checkpoint는 왜 필요해?
A. 긴 Agent Workflow, Human Approval 대기, 실패 복구, Review / Fix Loop 재개에 필요하다.

Q. Checkpoint와 Memory는 달라?
A. 다르다. Checkpoint는 현재 Workflow 상태 저장이고, Memory는 과거 정보를 재사용하기 위한 구조다.

Q. Checkpoint는 언제 저장해?
A. Node 실행 후 State가 업데이트될 때, 승인 대기 전, 긴 작업 중간, 오류 복구 지점에서 저장한다.

Q. 오래된 Checkpoint를 바로 재개해도 돼?
A. 권장하지 않는다. 현재 사용자 요청과 충돌하지 않는지 State Validation 후 재개해야 한다.

Q. Thread ID가 뭐야?
A. Checkpoint를 특정 Workflow, 작업, 대화와 연결하기 위한 식별자다.

Q. Thread ID는 왜 필요해?
A. 여러 Workflow의 State가 섞이지 않도록 구분하고 중단된 작업을 정확히 재개하기 위해 필요하다.

Q. Human Approval에도 Thread ID가 필요해?
A. 필요하다. 승인 대기 중인 Workflow를 정확히 찾아 재개해야 하기 때문이다.

Q. Thread ID에 사용자 개인정보를 넣어도 돼?
A. 안 된다. 개인정보, API Key, Token, 민감정보는 Thread ID에 포함하지 않는다.

Q. Persistence가 뭐야?
A. Checkpoint와 Workflow State를 저장소에 유지해 재시작 후에도 재개할 수 있게 하는 방식이다.

Q. In-memory Checkpoint는 언제 써?
A. 로컬 테스트나 짧은 Workflow처럼 재시작 후 복구가 필요 없는 경우에 사용한다.

Q. 개인 AI 서버에서는 어떤 Checkpoint 저장소가 현실적이야?
A. 초기에는 SQLite나 파일 기반 저장이 현실적이고, 확장 시 PostgreSQL을 고려할 수 있다.

Q. Checkpoint 저장소에 민감정보를 저장해도 돼?
A. 안 된다. API Key, Token, 비밀번호, 개인정보는 저장하지 않거나 마스킹해야 한다.

Q. Memory가 뭐야?
A. 과거 대화, 사용자 선호, 작업 이력을 재사용하기 위한 구조다.

Q. Memory와 State는 달라?
A. 다르다. State는 현재 Workflow 실행 상태이고 Memory는 과거 정보를 재사용하기 위한 구조다.

Q. Memory와 Checkpoint는 달라?
A. 다르다. Checkpoint는 현재 Workflow를 재개하기 위한 저장이고 Memory는 과거 정보를 참조하기 위한 저장이다.

Q. 대화 전체를 Memory에 저장하면 좋아?
A. 권장하지 않는다. 필요한 정보만 요약하거나 검색 가능한 형태로 저장해야 한다.

Q. 현재 요청과 Memory가 충돌하면 무엇을 우선해?
A. 현재 사용자 요청을 우선해야 한다.

Q. Agent Memory Design이 뭐야?
A. Agent가 어떤 과거 정보를 저장하고 언제 검색해 사용할지 정하는 설계다.

Q. Memory는 항상 사용해야 해?
A. 아니다. 현재 요청에 관련 있고 최신성이 확인된 Memory만 사용해야 한다.

Q. Memory를 Prompt에 많이 넣으면 좋아?
A. 좋지 않다. Context가 길어지고 관련 없는 정보가 Agent 판단을 흐릴 수 있다.

Q. 개인 AI 프로젝트에서 Memory에 저장할 만한 것은?
A. RAG 문서 규칙, Agent 구조 결정, 로컬 LLM 제약, 프로젝트 디렉터리 구조 같은 장기 유효 정보다.

Q. Memory에 저장하면 안 되는 것은?
A. API Key, 비밀번호, Token, 민감 개인정보, 검증되지 않은 추측, 임시 작업 상태다.

Q. Human-in-the-loop가 뭐야?
A. Agent Workflow 중 사용자 승인이나 선택이 필요한 지점에서 중단하고 결정 후 재개하는 구조다.

Q. 언제 Human Approval이 필요해?
A. 파일 수정, DB 변경, 배포, 비용 발생, 외부 발송처럼 Side Effect가 있는 작업 전에 필요하다.

Q. 승인 대기 상태는 어떻게 유지해?
A. Checkpoint에 State를 저장하고 Thread ID 기준으로 재개한다.

Q. 사용자가 승인하면 바로 실행해도 돼?
A. 승인 범위 안에서만 실행해야 하며, 위험도에 따라 실행 후 Review가 필요할 수 있다.

Q. 승인 범위를 넘어서는 작업은 가능해?
A. 불가능하다. 사용자가 승인한 작업과 범위 안에서만 실행해야 한다.

Q. Interrupt가 뭐야?
A. Workflow 실행 중 사용자 승인이나 입력이 필요할 때 실행을 중단하는 구조다.

Q. Resume은 뭐야?
A. 사용자 결정 후 저장된 Checkpoint에서 Workflow를 이어가는 구조다.

Q. Interrupt 전 무엇을 해야 해?
A. 현재 State를 Checkpoint로 저장해야 한다.

Q. Resume 전 무엇을 확인해야 해?
A. Thread ID, Checkpoint, 승인 범위, 현재 요청과의 충돌 여부, 다음 Node를 확인해야 한다.

Q. 오래된 Checkpoint를 재개하면 위험한 이유는?
A. 현재 요청이나 파일 상태가 바뀌었을 수 있어 잘못된 작업이 실행될 수 있기 때문이다.

Q. Review / Fix Loop가 뭐야?
A. 초안을 생성한 뒤 검토하고, 실패하면 수정 후 다시 검토하는 반복 Workflow다.

Q. Review / Fix Loop는 왜 LangGraph에 적합해?
A. 조건 분기, 반복, State 관리, 종료 조건을 명확히 설계할 수 있기 때문이다.

Q. Max Iteration은 왜 필요해?
A. 무한 수정 루프를 방지하기 위해 필요하다.

Q. Review Node는 무엇을 검토해?
A. 요구사항 충족, RAG 근거, 코드 정확성, 보안 위험, 누락, 일관성, 출력 형식을 검토한다.

Q. Fix Node는 무엇을 기준으로 수정해?
A. Review Node가 State에 저장한 review_findings를 기준으로 수정한다.

Q. Review Node가 뭐야?
A. Agent Output을 고정된 기준으로 검토하고 pass, fail, warning 결과를 State에 저장하는 Node다.

Q. Review Result는 왜 구조화해야 해?
A. Fix Node와 Conditional Edge가 결과를 안정적으로 사용할 수 있게 하기 위해 필요하다.

Q. Review Severity는 왜 필요해?
A. 사소한 문제와 치명적 문제를 구분해 Fix 또는 Final 경로를 결정하기 위해 필요하다.

Q. Unsupported Claim은 뭐야?
A. 검색된 문서나 요구사항에 근거하지 않은 주장이다.

Q. Fix Node가 뭐야?
A. Review Findings를 기준으로 Draft Output을 수정하는 Node다.

Q. Fix Node는 전체를 다시 생성해야 해?
A. 권장하지 않는다. Review Findings를 기준으로 필요한 부분을 타깃 수정하는 것이 안정적이다.

Q. Fix 후 다시 Review해야 해?
A. 해야 한다. 수정 과정에서 새 문제가 생길 수 있기 때문이다.

Q. fix_count는 왜 필요해?
A. Review / Fix Loop가 무한 반복되지 않도록 반복 횟수를 관리하기 위해 필요하다.

Q. Human Approval을 받으면 Review가 필요 없어?
A. 아니다. 승인은 실행 허가이고 Review는 실행 결과 품질과 안전성 검증이다.

Q. 승인 범위는 어디에 저장해?
A. State의 approval_scope 필드에 저장한다.

Q. 승인 범위를 초과하면 어떻게 해?
A. Critical Issue로 처리하고 사용자에게 보고해야 한다.

Q. Tool 실행 결과는 누가 검토해?
A. Review Node가 tool_result와 approval_scope를 기준으로 검토한다.

Q. 위험 작업의 안전한 흐름은?
A. Proposal → Approval → Checkpoint → Tool Execution → Review → Final 순서다.
