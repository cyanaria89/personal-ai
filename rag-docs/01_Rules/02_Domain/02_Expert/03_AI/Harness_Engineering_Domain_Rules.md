# Harness Engineering Domain Rules

---

# 1. Domain Purpose

## 1.1 Harness Engineering 문서 목적

### [개념]

Harness Engineering은 LLM Agent가 실제 작업을 수행할 수 있도록 모델 주변의 실행 기반을 설계하는 영역이다.

Harness는 모델 자체가 아니라 Agent 실행을 둘러싼 도구, 권한, 상태, 메모리, 입력 검증, 출력 검증, 로그, 실패 처리, 안전장치, 실행 환경을 포함한다.

Harness Engineering Domain 문서는 AI Agent / PM Agent / Backend Agent / Frontend Agent / Review Agent / DevOps Agent / AI Agent가 안정적으로 작업하기 위한 RAG 문서 제작 규칙이다.

---

### [핵심]

- Harness Engineering은 Agent 실행 기반 설계이다.
- Prompt Engineering은 지시 설계이다.
- Context Engineering은 문맥 설계이다.
- Tool Calling은 도구 호출 기술이다.
- Harness Engineering은 Tool, Memory, State, Permission, Validation, Logging, Guardrail을 통합한다.
- Harness는 Agent가 실제 파일, 코드, API, DB, 테스트, 로그와 상호작용하는 실행 장치이다.
- Harness Engineering은 Level 4 AI Expert 문서에 속한다.

---

### [실무]

2026 실무 기준 Harness Engineering 문서는 단순 개념 설명이 아니라 Agent가 실제 개발 업무를 수행할 때 필요한 실행 제어 기준을 제공해야 한다.

실무 Harness는 다음을 포함한다.

- Tool Registry
- Tool Permission
- Tool Input Validation
- Tool Output Schema
- State Store
- Memory Access Policy
- Execution Sandbox
- File Access Policy
- Command Execution Policy
- Human Approval Policy
- Error Handling
- Retry Policy
- Logging
- Trace
- Audit
- Guardrails
- Result Validation
- Rollback Policy

---

### [FAQ]

Q. Harness Engineering은 뭐야?

A. LLM Agent가 실제 작업을 수행할 수 있도록 도구, 권한, 상태, 메모리, 검증, 로그, 안전장치를 설계하는 영역이다.

Q. Harness는 모델이야?

A. 아니다. Harness는 모델 주변의 실행 환경과 제어 장치이다.

Q. Harness Engineering은 Prompt Engineering이랑 달라?

A. 다르다. Prompt Engineering은 지시문 설계이고, Harness Engineering은 Agent 실행 기반 설계이다.

Q. Harness Engineering은 Level 2에 넣어야 해?

A. 아니다. Tool Calling, Agent Workflow, Memory를 통합하는 상위 개념이므로 Level 4 AI Expert에 넣는 것이 적절하다.

---

# 2. Scope

## 2.1 포함 범위

### [개념]

Harness Engineering 문서는 Agent 실행 환경과 제어 구조를 다룬다.

포함 범위는 Agent가 도구를 안전하게 사용하고, 상태를 유지하며, 실패를 감지하고, 작업 결과를 검증하는 데 필요한 규칙이다.

---

### [핵심]

포함 범위:

- Agent Harness
- Tool Registry
- Tool Calling Control
- Function Calling Control
- Tool Permission
- Tool Access Policy
- Input Validation
- Output Validation
- Structured Output
- State Management
- Memory Access Policy
- Context Injection Policy
- Execution Sandbox
- File System Access
- Shell Command Policy
- Code Execution Policy
- API Access Policy
- Database Access Policy
- Human-in-the-Loop Approval
- Error Handling
- Retry Policy
- Timeout Policy
- Rate Limit Policy
- Logging
- Tracing
- Audit Trail
- Observability Hook
- Guardrails
- Security Policy
- Rollback Policy
- Deterministic Execution
- Idempotency
- Tool Failure Recovery
- Agent Result Verification

---

### [실무]

Harness Engineering 문서는 개인 AI 개발팀 구조에 맞춰 작성한다.

대상 Agent:

- PM Agent
- Backend Agent
- Frontend Agent
- SQL Agent
- Review Agent
- DevOps Agent
- AI/ML Agent

각 Agent는 서로 다른 Harness를 가질 수 있다.

예시:

- Backend Agent Harness: 코드 읽기, 코드 수정, 빌드 실행, 테스트 실행, 로그 분석
- SQL Agent Harness: 스키마 조회, SELECT 실행, DDL 검토, 위험 쿼리 차단
- Frontend Agent Harness: 컴포넌트 파일 수정, 빌드 실행, 라우팅 검증
- Review Agent Harness: diff 분석, 규칙 검증, 테스트 결과 검토
- PM Agent Harness: 작업 분해, Agent 호출, 결과 취합, 승인 요청

---

### [FAQ]

Q. Harness Engineering 문서에는 Tool Calling도 포함해?

A. 포함한다. 단, Tool Calling 기본 문법이 아니라 도구 등록, 권한, 검증, 실패 처리, 실행 정책 중심으로 다룬다.

Q. Harness Engineering과 Agent Memory는 무슨 관계야?

A. Agent Memory는 Harness가 접근하고 제어하는 구성요소 중 하나이다.

Q. Harness Engineering과 Guardrails는 무슨 관계야?

A. Guardrails는 Harness 내부의 안전 제어 계층으로 볼 수 있다.

Q. Harness Engineering 문서는 어느 Agent에게 가장 중요해?

A. 파일 수정, 코드 실행, DB 접근, 배포 작업을 수행하는 Backend Agent, SQL Agent, DevOps Agent, Review Agent에게 특히 중요하다.

---

# 3. Exclusion Scope

## 3.1 제외 범위

### [개념]

Harness Engineering 문서는 Agent 실행 기반을 다루지만, 모델 학습이나 알고리즘 자체를 깊게 다루지는 않는다.

---

### [핵심]

제외 범위:

- Prompt Engineering 기본 이론
- Context Engineering 기본 이론
- Embedding 모델 구조 상세
- Vector Database 기본 사용법
- RAG Chunking 기본 이론
- Fine-Tuning 학습 과정 상세
- Model Quantization 알고리즘 상세
- MLOps 전체 운영 체계 상세
- Kubernetes 운영 심화
- LangGraph 기본 튜토리얼
- LLM 내부 Transformer 구조
- 머신러닝 모델 학습 알고리즘
- 프론트엔드 UI 구현 상세
- 백엔드 비즈니스 로직 구현 상세

---

### [실무]

Harness Engineering 문서에서 LangGraph, MCP, Tool Calling, Memory, Observability를 언급할 수 있지만, 각 도메인의 상세 구현 문서로 확장하지 않는다.

연계 기준:

- Tool Calling 기본은 `Tool Calling & Function Calling`
- Tool Reliability 심화는 `Tool Calling & Function Calling Reliability`
- 반복 실행 구조는 `Loop Engineering`
- 장기 기억은 `Long-Term Memory`
- 관찰 가능성은 `AI Observability`
- 보안 정책은 `AI Guardrails & Security`
- 다중 Agent 연결은 `Advanced Multi-Agent Orchestration`

---

### [FAQ]

Q. Harness Engineering에서 Fine-Tuning을 다뤄?

A. 아니다. Fine-Tuning은 모델 학습 영역이고 Harness Engineering은 실행 기반 설계 영역이다.

Q. Harness Engineering에서 LangGraph 사용법을 자세히 다뤄?

A. 기본 개념과 Harness 위치는 다룰 수 있지만, LangGraph 상세 사용법은 별도 문서에서 다룬다.

Q. Harness Engineering에서 RAG 검색 알고리즘을 다뤄?

A. 아니다. 검색 품질 최적화는 RAG Evaluation & Retrieval Optimization 문서에서 다룬다.

Q. Harness Engineering에서 보안을 다뤄?

A. 다룬다. 다만 보안 정책의 상세 기준은 AI Guardrails & Security와 연계한다.

---

# 4. Section Priority

## 4.1 Required Sections

### [개념]

Harness Engineering 문서는 반드시 Agent 실행 기반 중심으로 작성한다.

---

### [핵심]

필수 Section:

- [개념]
- [핵심]
- [실무]
- [FAQ]

강력 권장 Section:

- [Flow]
- [예제]
- [주의]
- [Best Practice]
- [Checklist]
- [Troubleshooting]
- [Comparison]

선택 Section:

- [Policy]
- [Schema]
- [Failure Case]
- [Review Point]
- [Security]
- [Observability]

---

### [실무]

Harness Engineering 문서는 RAG 검색에 강해야 한다.

각 Chunk는 다음 키워드 중 하나 이상을 포함하는 것이 좋다.

- Harness Engineering
- Agent Harness
- Tool Registry
- Tool Permission
- Tool Validation
- State Management
- Memory Access
- Execution Sandbox
- Human Approval
- Error Handling
- Retry Policy
- Logging
- Tracing
- Audit Trail
- Guardrails
- Agent Safety
- Tool Failure Recovery

---

### [FAQ]

Q. Harness Engineering 문서에 [Flow]가 필요해?

A. 필요하다. Agent 실행 흐름, Tool 호출 흐름, 실패 처리 흐름은 Flow로 표현해야 검색과 추론에 유리하다.

Q. Harness Engineering 문서에 [예제]가 필요해?

A. 필요하다. Tool Registry, Permission Policy, Error Result, Approval Flow 같은 짧은 예제가 있어야 Agent가 적용하기 쉽다.

Q. Harness Engineering 문서에 [Checklist]가 필요해?

A. 권장한다. Harness는 누락 항목이 위험으로 이어질 수 있으므로 체크리스트가 유용하다.

Q. Harness Engineering 문서에 [Troubleshooting]이 필요해?

A. 권장한다. Tool 실패, 권한 오류, 상태 불일치, 무한 반복, 로그 누락 같은 문제를 빠르게 검색할 수 있어야 한다.

---

# 5. Core Concept Rules

## 5.1 Agent Harness

### [개념]

Agent Harness는 LLM Agent가 도구를 사용하고, 상태를 유지하고, 실행 결과를 검증하며, 실패를 처리할 수 있게 만드는 실행 프레임이다.

Agent Harness는 모델의 출력이 실제 작업으로 연결되는 중간 제어 계층이다.

---

### [핵심]

Agent Harness 구성요소:

- LLM
- System Prompt
- Context Provider
- Tool Registry
- Tool Executor
- Permission Layer
- State Store
- Memory Store
- Validation Layer
- Guardrail Layer
- Logging Layer
- Observability Layer
- Human Approval Layer
- Result Verifier

---

### [Flow]

```text
User Request
→ Agent
→ Harness
→ Context Load
→ Tool Selection
→ Permission Check
→ Tool Execution
→ Result Validation
→ State Update
→ Response Generation
```

---

### [실무]

개인 AI 개발팀에서 Harness는 Agent별로 분리하는 것이 좋다.

예시:

- PM Agent Harness는 작업 분해와 Agent 호출 중심
- Backend Agent Harness는 코드 수정과 테스트 실행 중심
- SQL Agent Harness는 DB 조회와 위험 쿼리 차단 중심
- Review Agent Harness는 결과 검증과 피드백 중심
- DevOps Agent Harness는 배포, 로그, 인프라 명령 권한 제어 중심

---

### [FAQ]

Q. Agent Harness는 왜 필요해?

A. LLM 출력만으로는 실제 파일 수정, 도구 실행, 검증, 권한 제어를 안전하게 처리하기 어렵기 때문이다.

Q. Agent Harness가 없으면 어떤 문제가 생겨?

A. 도구 오사용, 파일 훼손, 잘못된 명령 실행, 상태 불일치, 실패 원인 추적 불가 문제가 생길 수 있다.

Q. Agent마다 Harness가 달라야 해?

A. 가능하면 달라야 한다. Agent 역할마다 허용 도구, 권한, 검증 기준이 다르기 때문이다.

Q. Harness는 Agent Workflow와 같아?

A. 아니다. Workflow는 작업 흐름이고 Harness는 그 흐름을 실행하고 통제하는 기반이다.

---

# 6. Tool Registry Rules

## 6.1 Tool Registry 설계

### [개념]

Tool Registry는 Agent가 사용할 수 있는 도구 목록과 각 도구의 설명, 입력 스키마, 출력 스키마, 권한, 위험도, 실행 조건을 관리하는 구조이다.

---

### [핵심]

Tool Registry 필수 항목:

- toolName
- description
- inputSchema
- outputSchema
- permissionLevel
- riskLevel
- allowedAgent
- timeout
- retryLimit
- requiresApproval
- sideEffect
- idempotent
- logPolicy

---

### [예제]

```json
{
  "toolName": "run_tests",
  "description": "Run project test command",
  "permissionLevel": "write",
  "riskLevel": "medium",
  "allowedAgent": ["BackendAgent", "ReviewAgent"],
  "timeout": 120,
  "retryLimit": 1,
  "requiresApproval": false,
  "sideEffect": true,
  "idempotent": true
}
```

---

### [실무]

Tool Registry는 단순 목록이 아니라 Agent 안전성의 핵심이다.

실무 기준:

- 읽기 도구와 쓰기 도구를 분리
- 위험 작업은 approval 필요
- 삭제, 배포, DB 변경 도구는 고위험으로 분류
- 도구별 timeout 필수
- 도구별 retryLimit 필수
- 출력은 구조화된 JSON 권장
- 도구 실행 로그 필수

---

### [FAQ]

Q. Tool Registry는 왜 필요해?

A. Agent가 사용할 수 있는 도구와 권한을 명확히 제한하기 위해 필요하다.

Q. Tool Registry에 riskLevel이 필요한 이유는?

A. 파일 수정, DB 변경, 배포처럼 위험도가 다른 작업을 구분해야 하기 때문이다.

Q. Tool Registry에 outputSchema가 필요한 이유는?

A. Agent가 도구 실행 결과를 안정적으로 해석하고 다음 작업을 결정하기 위해 필요하다.

Q. Tool Registry는 Tool Calling이랑 같은 거야?

A. 아니다. Tool Calling은 호출 방식이고 Tool Registry는 호출 가능한 도구의 관리 체계이다.

---

# 7. Tool Permission Rules

## 7.1 Tool Permission 설계

### [개념]

Tool Permission은 Agent가 어떤 도구를 어떤 조건에서 사용할 수 있는지 제한하는 권한 정책이다.

---

### [핵심]

권한 레벨 예시:

| Level | 이름        | 허용 작업                         |
| ----- | ----------- | --------------------------------- |
| 0     | none        | 도구 사용 불가                    |
| 1     | read        | 파일 읽기, 검색, 조회             |
| 2     | write       | 파일 생성, 파일 수정              |
| 3     | execute     | 테스트 실행, 빌드 실행, 명령 실행 |
| 4     | destructive | 삭제, DB 변경, 배포 변경          |
| 5     | admin       | 시스템 설정, 인프라 변경          |

---

### [실무]

Agent별 권한 예시:

| Agent          | 권장 권한                       |
| -------------- | ------------------------------- |
| PM Agent       | read, delegate                  |
| Backend Agent  | read, write, test execute       |
| Frontend Agent | read, write, build execute      |
| SQL Agent      | read, select query              |
| Review Agent   | read, test execute, diff review |
| DevOps Agent   | read, execute, limited deploy   |
| AI/ML Agent    | read, experiment execute        |

---

### [주의]

- 모든 Agent에게 write 권한 부여 금지
- 모든 Agent에게 shell command 권한 부여 금지
- DB 변경 권한은 기본 차단
- 삭제 작업은 human approval 필수
- 배포 작업은 별도 승인 필요
- Secret 접근 권한은 최소화
- 권한 상승 자동화 금지

---

### [FAQ]

Q. Agent에게 모든 도구 권한을 줘도 돼?

A. 안 된다. 최소 권한 원칙을 적용해야 한다.

Q. SQL Agent는 UPDATE나 DELETE를 실행해도 돼?

A. 기본적으로 금지해야 한다. 필요한 경우 dry-run, review, human approval 이후 허용한다.

Q. Backend Agent에게 shell command 권한을 줘도 돼?

A. 테스트와 빌드처럼 제한된 명령만 허용하는 것이 좋다.

Q. DevOps Agent 권한은 어떻게 관리해?

A. 배포, 인프라, 삭제 작업은 high risk로 분류하고 human approval을 요구해야 한다.

---

# 8. Input Validation Rules

## 8.1 Tool Input Validation

### [개념]

Input Validation은 Agent가 도구를 호출하기 전에 입력값이 안전하고 유효한지 확인하는 과정이다.

---

### [핵심]

필수 검증:

- Required Field 존재 여부
- Type Validation
- Enum Validation
- Path Validation
- Command Allowlist
- URL Validation
- SQL Query Validation
- File Extension Validation
- Size Limit
- Secret Masking
- Prompt Injection Pattern Check

---

### [Flow]

```text
Tool Call Request
→ Input Schema Check
→ Permission Check
→ Safety Check
→ Execute Tool
→ Return Result
```

---

### [실무]

파일 경로 입력은 반드시 검증한다.

검증 기준:

- 허용된 workspace 내부 경로인지 확인
- `../` path traversal 차단
- 숨김 파일 접근 제한
- `.env`, secret 파일 접근 제한
- 허용 확장자만 처리
- 파일 크기 제한 적용
- 삭제/덮어쓰기 전 승인 확인

---

### [FAQ]

Q. Tool Input Validation은 왜 필요해?

A. 잘못된 입력이 파일 훼손, 명령 오작동, 보안 사고로 이어질 수 있기 때문이다.

Q. 파일 경로 검증에서 가장 중요한 것은?

A. workspace 밖으로 나가는 path traversal을 차단하는 것이다.

Q. SQL 입력 검증은 어떻게 해야 해?

A. SELECT 중심으로 제한하고 UPDATE, DELETE, DROP, TRUNCATE 같은 위험 명령은 차단한다.

Q. Command 입력 검증은 어떻게 해야 해?

A. 자유 명령 실행을 금지하고 allowlist 기반으로 허용된 명령만 실행한다.

---

# 9. Output Validation Rules

## 9.1 Tool Output Validation

### [개념]

Output Validation은 도구 실행 결과가 기대한 형식과 의미를 만족하는지 확인하는 과정이다.

---

### [핵심]

필수 검증:

- Output Schema 일치
- success / failure 상태 포함
- errorCode 포함
- errorMessage 포함
- resultData 포함
- sideEffect 결과 명시
- fileChanged 여부 명시
- testResult 여부 명시
- executionTime 포함
- warning 포함

---

### [예제]

```json
{
  "success": false,
  "errorCode": "TEST_FAILED",
  "errorMessage": "Unit tests failed",
  "resultData": {
    "passed": 12,
    "failed": 2
  },
  "warnings": [],
  "executionTimeMs": 18300
}
```

---

### [실무]

Agent Tool Output은 항상 구조화해야 한다.

권장 Output Field:

- success
- status
- errorCode
- message
- data
- warnings
- logs
- changedFiles
- nextAction
- retryable
- requiresHumanReview

---

### [FAQ]

Q. Tool Output은 자연어로 반환해도 돼?

A. 가능하지만 권장하지 않는다. Agent가 안정적으로 처리하려면 JSON 같은 구조화된 출력이 좋다.

Q. 실패 결과에도 data가 필요해?

A. 필요할 수 있다. 실패 원인, 로그, 재시도 가능 여부를 포함해야 다음 행동을 결정할 수 있다.

Q. retryable 필드는 왜 필요해?

A. Agent가 재시도할 수 있는 실패와 즉시 중단해야 하는 실패를 구분하기 위해 필요하다.

Q. changedFiles 필드는 왜 필요해?

A. 파일 변경 여부를 추적하고 Review Agent가 검토할 수 있게 하기 위해 필요하다.

---

# 10. State Management Rules

## 10.1 Harness State Management

### [개념]

State Management는 Agent 작업 중 현재 목표, 단계, 도구 실행 결과, 실패 이력, 변경 파일, 승인 상태를 유지하는 구조이다.

---

### [핵심]

State에 포함할 수 있는 정보:

- taskId
- userRequest
- currentStep
- plan
- agentRole
- toolCalls
- toolResults
- changedFiles
- errors
- retryCount
- approvalStatus
- memoryReferences
- finalStatus

---

### [Flow]

```text
Task Start
→ Initialize State
→ Execute Step
→ Save Tool Result
→ Update State
→ Validate Progress
→ Continue or Stop
```

---

### [실무]

State는 Agent Loop와 Multi-Agent Orchestration에서 중요하다.

실무 기준:

- taskId로 작업 단위 추적
- stepId로 단계 추적
- toolCallId로 도구 실행 추적
- 실패 이력 저장
- 변경 파일 목록 저장
- 승인 여부 저장
- 최종 결과와 중간 결과 구분
- Agent 간 전달 가능한 상태 구조 유지

---

### [FAQ]

Q. Harness에서 State가 왜 중요해?

A. Agent가 현재 작업 단계, 실행 결과, 실패 이력, 변경 내용을 추적해야 하기 때문이다.

Q. State와 Memory는 같아?

A. 아니다. State는 현재 작업의 진행 상태이고 Memory는 과거 경험이나 장기 정보를 저장한다.

Q. State를 저장하지 않으면 어떤 문제가 생겨?

A. Agent가 같은 작업을 반복하거나 실패 원인을 잃어버리고 잘못된 다음 행동을 선택할 수 있다.

Q. Multi-Agent에서 State는 어떻게 쓰여?

A. PM Agent가 작업 상태를 관리하고 각 Agent의 결과를 취합하는 데 사용된다.

---

# 11. Memory Access Rules

## 11.1 Memory Access Policy

### [개념]

Memory Access Policy는 Agent가 어떤 기억을 언제, 어떤 조건으로 읽거나 쓸 수 있는지 정의하는 규칙이다.

---

### [핵심]

Memory 구분:

- Short-Term Memory
- Working Memory
- Long-Term Memory
- Project Memory
- User Preference Memory
- Error Pattern Memory
- Decision History
- Codebase Knowledge
- Retrieval History

---

### [실무]

Harness는 Memory 접근을 통제해야 한다.

실무 기준:

- 모든 Agent가 모든 Memory에 접근하지 않음
- 작업 목적과 관련된 Memory만 검색
- 민감 정보는 기본 비공개
- Memory write는 검증 후 수행
- 임시 상태를 Long-Term Memory에 저장하지 않음
- 실패 패턴은 Error Pattern Memory로 저장 가능
- 프로젝트 결정사항은 Decision History로 저장 가능

---

### [주의]

- 불확실한 정보를 Memory에 저장 금지
- 사용자 승인 없는 민감 정보 저장 금지
- 오래된 Memory를 무조건 신뢰하지 않음
- 현재 코드와 충돌하는 Memory는 재검증
- Agent hallucination을 Memory로 저장 금지

---

### [FAQ]

Q. Harness가 Memory 접근을 관리해야 해?

A. 그렇다. Agent가 불필요하거나 위험한 기억을 참조하지 않도록 제한해야 한다.

Q. State와 Long-Term Memory 차이는?

A. State는 현재 작업 상태이고 Long-Term Memory는 미래 작업에 재사용할 장기 정보이다.

Q. 실패 사례를 Memory에 저장해도 돼?

A. 가능하다. 반복 오류 방지에 도움이 된다. 단, 원인과 조건이 명확해야 한다.

Q. 모든 대화 내용을 Memory에 저장해야 해?

A. 아니다. 장기적으로 유용하고 검증된 정보만 저장해야 한다.

---

# 12. Execution Sandbox Rules

## 12.1 Execution Sandbox 설계

### [개념]

Execution Sandbox는 Agent가 코드, 명령어, 테스트, 파일 작업을 안전하게 실행할 수 있도록 격리된 환경을 제공하는 구조이다.

---

### [핵심]

Sandbox 설계 기준:

- Workspace 제한
- File Access 제한
- Network Access 제한
- Command Allowlist
- Timeout
- Resource Limit
- Secret Masking
- Temporary Directory
- Dry-Run Mode
- Rollback Support
- Execution Log

---

### [실무]

개발 Agent는 실행 권한이 필요하지만, 무제한 실행 권한은 위험하다.

권장:

- 테스트 명령 허용
- 빌드 명령 허용
- 패키지 설치 제한
- 시스템 설정 변경 금지
- 홈 디렉터리 접근 제한
- `.env` 직접 출력 금지
- 외부 네트워크 호출 제한
- 삭제 명령 차단
- 배포 명령 승인 필요

---

### [주의]

위험 명령 예시:

```bash
rm -rf /
sudo rm -rf
drop database
truncate table
chmod -R 777
curl | bash
```

위 명령은 기본 차단한다.

---

### [FAQ]

Q. Agent에게 코드 실행 권한을 줘도 돼?

A. 제한된 Sandbox 안에서만 허용하는 것이 좋다.

Q. Shell Command는 어떻게 제한해야 해?

A. allowlist 기반으로 테스트, 빌드, lint 같은 안전 명령만 허용한다.

Q. Sandbox에 timeout이 필요한 이유는?

A. 무한 실행, 무한 루프, 장시간 빌드로 시스템 자원을 낭비하지 않기 위해 필요하다.

Q. Dry-Run Mode는 왜 필요해?

A. 실제 변경 전에 Agent 행동을 검토하고 위험 작업을 사전에 차단하기 위해 필요하다.

---

# 13. File Access Rules

## 13.1 File Access Policy

### [개념]

File Access Policy는 Agent가 어떤 파일을 읽고, 쓰고, 수정하고, 삭제할 수 있는지 제한하는 규칙이다.

---

### [핵심]

파일 접근 정책:

- Read Allowlist
- Write Allowlist
- Protected Files
- Secret Files
- Generated Files
- Backup Policy
- Diff Required
- Human Approval Required
- Max File Size
- Extension Allowlist

---

### [실무]

파일 접근 권장 기준:

| 파일 유형                    | 기본 정책                    |
| ---------------------------- | ---------------------------- |
| `.md` 문서                   | read/write 가능              |
| `.java`, `.js`, `.ts`, `.py` | Agent 역할에 따라 write 가능 |
| `.env`                       | read 제한, write 금지        |
| secret 파일                  | 접근 금지                    |
| build output                 | read 가능, write 제한        |
| lock file                    | 자동 수정 주의               |
| migration file               | human review 필요            |
| config file                  | 수정 전 승인 권장            |

---

### [주의]

- 원본 파일 자동 삭제 금지
- 대량 파일 수정 전 승인
- Generated Code와 Source Code 구분
- Secret 파일 출력 금지
- Binary 파일 무분별 수정 금지
- 파일 수정 후 diff 생성 권장

---

### [FAQ]

Q. Agent가 모든 파일을 수정해도 돼?

A. 안 된다. 역할별 write allowlist를 지정해야 한다.

Q. `.env` 파일은 Agent가 읽어도 돼?

A. 기본적으로 제한해야 한다. Secret 노출 위험이 있기 때문이다.

Q. 파일 수정 후 diff가 필요한 이유는?

A. Review Agent와 사용자가 변경 내용을 검토할 수 있어야 하기 때문이다.

Q. 대량 파일 수정은 어떻게 처리해야 해?

A. 변경 계획을 먼저 제시하고 승인 후 실행하는 것이 좋다.

---

# 14. Command Execution Rules

## 14.1 Command Execution Policy

### [개념]

Command Execution Policy는 Agent가 실행 가능한 명령어와 금지 명령어를 정의하는 규칙이다.

---

### [핵심]

허용 가능 명령 예시:

- `npm test`
- `npm run build`
- `npm run lint`
- `python -m pytest`
- `./gradlew test`
- `./gradlew build`
- `mvn test`
- `git diff`
- `git status`

제한 또는 금지 명령 예시:

- `sudo`
- `rm -rf`
- `chmod -R`
- `chown -R`
- `curl | bash`
- `wget | sh`
- `docker system prune`
- `drop database`
- `truncate table`

---

### [Flow]

```text
Command Request
→ Parse Command
→ Check Allowlist
→ Check Risk
→ Require Approval if Needed
→ Execute with Timeout
→ Capture Output
→ Return Structured Result
```

---

### [실무]

명령 실행은 Harness에서 가장 위험한 영역 중 하나이다.

실무 기준:

- 자유 shell 실행 금지
- 명령 allowlist 사용
- timeout 필수
- stdout / stderr 캡처
- exit code 확인
- 민감 정보 마스킹
- destructive command 차단
- 실행 로그 저장
- 실패 시 retry 제한

---

### [FAQ]

Q. Agent에게 자유롭게 명령어 실행을 허용해도 돼?

A. 안 된다. allowlist 기반으로 제한해야 한다.

Q. `git diff`는 허용해도 돼?

A. 일반적으로 허용 가능하다. 변경 검토에 필요하기 때문이다.

Q. `rm -rf`는 허용해도 돼?

A. 기본적으로 금지해야 한다.

Q. 명령 실행 결과는 어떻게 반환해야 해?

A. exitCode, stdout, stderr, success, executionTime을 포함한 구조화된 결과로 반환한다.

---

# 15. API Access Rules

## 15.1 API Access Policy

### [개념]

API Access Policy는 Agent가 외부 API 또는 내부 API를 호출할 때 사용하는 권한, 인증, 제한, 오류 처리 규칙이다.

---

### [핵심]

API Harness 필수 항목:

- Base URL
- Auth Policy
- Timeout
- Retry
- Rate Limit
- Request Schema
- Response Schema
- Error Handling
- Secret Masking
- Logging Policy
- Idempotency Key
- Circuit Breaker

---

### [실무]

Agent가 API를 호출할 때는 API Key와 사용자 데이터를 보호해야 한다.

실무 기준:

- API Key 하드코딩 금지
- Secret 로그 출력 금지
- Timeout 필수
- 무제한 retry 금지
- 4xx와 5xx 오류 구분
- Rate Limit 감지
- 민감 Request Body 로그 제한
- POST / PUT / DELETE는 위험도 분류
- 외부 API 비용 발생 가능성 고려

---

### [FAQ]

Q. Agent가 외부 API를 호출해도 돼?

A. 가능하지만 인증, 비용, rate limit, 개인정보, timeout 정책이 필요하다.

Q. API Key는 어디에 둬야 해?

A. 환경변수나 Secret Manager에 두고 Harness가 직접 노출하지 않도록 관리한다.

Q. API 호출 실패는 어떻게 처리해?

A. 상태 코드, 오류 메시지, retry 가능 여부를 구조화해 반환한다.

Q. DELETE API 호출은 어떻게 해야 해?

A. 기본적으로 human approval을 요구하는 것이 안전하다.

---

# 16. Database Access Rules

## 16.1 Database Access Policy

### [개념]

Database Access Policy는 Agent가 DB에 접근할 때 허용되는 쿼리, 금지되는 쿼리, 검증 방식, 승인 절차를 정의하는 규칙이다.

---

### [핵심]

권장 기본 정책:

- SELECT 허용
- EXPLAIN 허용
- INSERT 제한
- UPDATE 제한
- DELETE 제한
- DROP 금지
- TRUNCATE 금지
- ALTER 제한
- Migration은 Review 필요
- Production DB 직접 접근 금지

---

### [실무]

SQL Agent Harness는 DB 안전성이 핵심이다.

실무 기준:

- Read-only 계정 우선
- Production DB 직접 수정 금지
- Query Timeout 설정
- Row Limit 설정
- Slow Query 감지
- DDL 변경은 human approval
- DML 변경은 transaction + rollback 계획 필요
- Migration Script는 Review Agent 검토 필요
- 쿼리 실행 전 위험도 분석

---

### [주의]

위험 SQL 예시:

```sql
DELETE FROM users;
DROP TABLE orders;
TRUNCATE TABLE logs;
UPDATE users SET role = 'ADMIN';
ALTER TABLE payments DROP COLUMN status;
```

위 쿼리는 기본 차단하거나 승인 절차를 요구한다.

---

### [FAQ]

Q. SQL Agent가 DB를 직접 수정해도 돼?

A. 기본적으로 안 된다. SELECT 중심으로 제한하고 수정 쿼리는 승인 후 실행해야 한다.

Q. Production DB에 Agent를 연결해도 돼?

A. 권장하지 않는다. 최소한 read-only 계정과 강한 제한이 필요하다.

Q. Query Timeout은 왜 필요해?

A. 무거운 쿼리로 DB 자원을 고갈시키는 것을 막기 위해 필요하다.

Q. DDL 변경은 어떻게 처리해야 해?

A. Migration Script 생성, Review Agent 검토, human approval 이후 적용하는 것이 좋다.

---

# 17. Human-in-the-Loop Rules

## 17.1 Human Approval Policy

### [개념]

Human-in-the-Loop은 Agent가 위험하거나 되돌리기 어려운 작업을 수행하기 전에 사람의 승인을 받는 구조이다.

---

### [핵심]

승인 필요 작업:

- 파일 대량 수정
- 파일 삭제
- DB DML 실행
- DB DDL 실행
- 배포 실행
- Secret 변경
- 권한 변경
- 결제 API 호출
- 외부 사용자에게 메시지 발송
- 비용 발생 API 대량 호출
- Production 환경 변경

---

### [Flow]

```text
Agent Plan
→ Risk Detection
→ Approval Request
→ Human Decision
→ Execute or Abort
→ Log Decision
```

---

### [실무]

승인 요청에는 충분한 정보가 있어야 한다.

승인 요청 필수 정보:

- 작업 목적
- 변경 대상
- 예상 영향
- 위험도
- Rollback 가능 여부
- 실행 명령
- 변경 파일 목록
- 테스트 계획
- 대안

---

### [FAQ]

Q. 모든 작업에 human approval이 필요해?

A. 아니다. 위험하거나 되돌리기 어려운 작업에 필요하다.

Q. 파일 수정도 승인 받아야 해?

A. 소규모 수정은 Agent가 수행할 수 있지만, 대량 수정이나 설정 파일 수정은 승인 권장이다.

Q. 배포 작업은 승인 받아야 해?

A. 반드시 승인 절차를 두는 것이 안전하다.

Q. 승인 결과도 로그로 남겨야 해?

A. 그렇다. 추적성과 책임성을 위해 승인 여부와 이유를 기록해야 한다.

---

# 18. Error Handling Rules

## 18.1 Harness Error Handling

### [개념]

Harness Error Handling은 Agent 도구 실행 중 발생하는 오류를 분류하고, 복구 가능 여부를 판단하고, 다음 행동을 결정하는 규칙이다.

---

### [핵심]

오류 분류:

- ValidationError
- PermissionError
- ToolExecutionError
- TimeoutError
- RateLimitError
- NetworkError
- AuthenticationError
- FileAccessError
- CommandExecutionError
- TestFailure
- BuildFailure
- SchemaMismatchError
- UnknownError

---

### [실무]

오류는 자연어만으로 반환하지 않는다.

권장 Error Result:

```json
{
  "success": false,
  "errorType": "PermissionError",
  "errorMessage": "Agent does not have permission to modify .env file",
  "retryable": false,
  "requiresHumanReview": true
}
```

---

### [Flow]

```text
Tool Failure
→ Classify Error
→ Check Retryable
→ Check Approval Required
→ Update State
→ Return Structured Error
→ Decide Next Action
```

---

### [FAQ]

Q. Harness에서 오류 분류가 왜 중요해?

A. 재시도할 오류와 중단해야 할 오류를 구분해야 하기 때문이다.

Q. UnknownError는 어떻게 처리해?

A. 즉시 무한 재시도하지 말고 로그를 남기고 human review를 요구하는 것이 좋다.

Q. TestFailure는 실패야?

A. 도구 실행 실패가 아니라 검증 실패일 수 있다. 수정 루프로 연결할 수 있다.

Q. PermissionError는 재시도해도 돼?

A. 일반적으로 재시도하면 안 된다. 권한 정책이나 승인 절차가 필요하다.

---

# 19. Retry Policy Rules

## 19.1 Retry Policy 설계

### [개념]

Retry Policy는 실패한 작업을 언제, 몇 번, 어떤 조건으로 다시 실행할지 정의하는 규칙이다.

---

### [핵심]

Retry 가능 오류:

- 일시적 네트워크 오류
- Rate Limit 일부
- Timeout 일부
- 임시 파일 lock
- 외부 API 일시 장애

Retry 금지 오류:

- PermissionError
- ValidationError
- SchemaMismatchError
- Destructive Command Blocked
- Secret Access Denied
- Syntax Error without Fix
- Human Approval Rejected

---

### [실무]

Retry 기준:

- retryLimit 필수
- exponential backoff 권장
- 같은 실패 반복 시 중단
- 상태 저장 후 retry
- retry 로그 기록
- 비용 발생 작업 retry 주의
- destructive 작업 retry 금지

---

### [주의]

무제한 retry 금지.

나쁜 Flow:

```text
Tool Failure
→ Retry
→ Failure
→ Retry
→ Failure
→ Retry Forever
```

좋은 Flow:

```text
Tool Failure
→ Classify Error
→ Retryable Check
→ Retry 1~2 Times
→ Stop
→ Report Failure
```

---

### [FAQ]

Q. Retry는 몇 번이 적절해?

A. 작업에 따라 다르지만 일반적으로 1~3회로 제한한다.

Q. 모든 오류를 retry하면 안 돼?

A. 안 된다. 권한 오류, 입력 오류, 보안 차단은 retry해도 해결되지 않는다.

Q. Rate Limit은 retry해도 돼?

A. 가능하지만 backoff와 최대 재시도 횟수가 필요하다.

Q. 파일 삭제 같은 작업도 retry해도 돼?

A. 위험하다. destructive 작업은 자동 retry를 피해야 한다.

---

# 20. Logging and Tracing Rules

## 20.1 Logging / Tracing 설계

### [개념]

Logging은 Agent와 Tool 실행 기록을 남기는 것이고, Tracing은 요청이 Agent, Tool, Memory, RAG, API를 거치는 전체 경로를 추적하는 것이다.

---

### [핵심]

필수 로그:

- taskId
- agentName
- toolName
- inputSummary
- outputSummary
- success
- errorType
- executionTime
- changedFiles
- approvalStatus
- retryCount
- timestamp

---

### [실무]

로그 정책:

- 민감 정보 마스킹
- Secret 출력 금지
- 전체 Prompt 무분별 저장 금지
- Tool Input은 요약 저장
- Tool Output은 구조화 저장
- 오류는 원인 파악 가능하게 저장
- 작업 단위 taskId 유지
- Multi-Agent 호출 관계 추적

---

### [예제]

```json
{
  "taskId": "task-2026-001",
  "agentName": "BackendAgent",
  "toolName": "run_tests",
  "success": false,
  "errorType": "TestFailure",
  "executionTimeMs": 22000,
  "retryCount": 0
}
```

---

### [FAQ]

Q. Harness에서 로그가 왜 중요해?

A. Agent가 어떤 도구를 왜 실행했고 어떤 결과가 나왔는지 추적해야 하기 때문이다.

Q. Prompt 전체를 로그로 남겨도 돼?

A. 주의해야 한다. 민감 정보나 사용자 데이터가 포함될 수 있으므로 요약 저장이 안전하다.

Q. Tool Input 전체를 저장해도 돼?

A. 필요 시 저장할 수 있지만 Secret과 개인정보는 마스킹해야 한다.

Q. Tracing은 언제 필요해?

A. Multi-Agent, RAG, Tool Calling이 섞인 복잡한 작업에서 원인 추적에 필요하다.

---

# 21. Guardrails Rules

## 21.1 Harness Guardrails

### [개념]

Harness Guardrails는 Agent가 위험한 행동을 하지 않도록 입력, 도구 호출, 파일 접근, 명령 실행, 출력 단계에서 적용하는 안전 제어 규칙이다.

---

### [핵심]

Guardrails 적용 지점:

- User Input
- Retrieved Context
- Tool Call
- Tool Input
- Tool Output
- Command Execution
- File Access
- API Access
- Database Access
- Final Answer

---

### [실무]

Harness Guardrails 예시:

- Prompt Injection 감지
- Secret 요청 차단
- 위험 명령 차단
- DB 변경 차단
- Production 배포 차단
- 개인정보 출력 제한
- 외부 전송 전 승인
- 파일 삭제 승인 요구
- Tool Output Schema 검증
- Hallucinated Tool 차단

---

### [주의]

Guardrails는 Agent 능력을 제한하는 것이 아니라 안전한 실행 범위를 정의하는 장치이다.

금지:

- 없는 도구 호출
- 권한 없는 파일 수정
- 승인 없는 배포
- 승인 없는 DB 변경
- Secret 노출
- 검증 없는 외부 API 호출
- 실패 로그 없는 무시

---

### [FAQ]

Q. Harness Guardrails는 AI Guardrails와 같아?

A. 일부 겹치지만 Harness Guardrails는 도구 실행과 시스템 행동 제어에 더 초점을 둔다.

Q. Prompt Injection은 Harness에서 막아야 해?

A. 그렇다. Retrieved Context나 사용자 입력이 도구 실행 정책을 우회하지 못하게 해야 한다.

Q. 없는 도구를 Agent가 호출하면 어떻게 해?

A. Tool Registry에 없는 도구는 실행하지 않고 오류를 반환해야 한다.

Q. Guardrails가 너무 많으면 Agent가 못 움직이지 않아?

A. 위험도 기반으로 조정해야 한다. 읽기 작업은 넓게, 쓰기와 실행 작업은 엄격하게 제한한다.

---

# 22. Result Verification Rules

## 22.1 Agent Result Verification

### [개념]

Result Verification은 Agent가 수행한 작업이 사용자 요구사항과 시스템 규칙을 만족하는지 확인하는 과정이다.

---

### [핵심]

검증 대상:

- 요구사항 충족 여부
- 파일 변경 정확성
- 테스트 통과 여부
- 빌드 성공 여부
- 코드 스타일
- 보안 규칙
- RAG 문서 구조
- 출력 형식
- Retrieval Queries 포함 여부
- 실패 처리 여부

---

### [Flow]

```text
Agent Output
→ Requirement Check
→ Tool Result Check
→ Test Result Check
→ Rule Check
→ Final Approval
```

---

### [실무]

개인 AI 개발팀 구조에서는 Review Agent가 Result Verification을 담당할 수 있다.

Review Agent 검증 항목:

- 작업 범위 초과 여부
- 파일 변경 타당성
- 테스트 결과
- 빌드 결과
- Domain Rules 준수
- 보안 위험
- 문서 출력 형식
- 치명적 문제 여부

---

### [FAQ]

Q. Harness에서 결과 검증이 왜 필요해?

A. Agent가 작업을 완료했다고 말해도 실제 요구사항을 만족하지 않을 수 있기 때문이다.

Q. 테스트 통과만 하면 검증 완료야?

A. 아니다. 요구사항, 보안, 변경 범위, 문서 규칙도 함께 확인해야 한다.

Q. Review Agent는 Harness에 포함돼?

A. Review Agent 자체는 별도 Agent지만, Harness는 Review Agent가 검증할 정보를 제공해야 한다.

Q. Result Verification 실패 시 어떻게 해?

A. Loop Engineering과 연계해 수정 단계로 돌아가거나 human review를 요청한다.

---

# 23. Rollback Rules

## 23.1 Rollback Policy

### [개념]

Rollback Policy는 Agent 작업이 실패하거나 위험한 결과를 만들었을 때 이전 상태로 되돌리는 규칙이다.

---

### [핵심]

Rollback 대상:

- 파일 변경
- 설정 변경
- DB 변경
- 배포 변경
- 생성된 임시 리소스
- Agent State
- Memory Write

---

### [실무]

Rollback 기준:

- 파일 수정 전 diff 또는 backup 확보
- DB 변경 전 transaction 사용
- Migration은 rollback script 준비
- 배포 전 이전 버전 확인
- Memory write는 검증 후 수행
- 실패 시 변경 파일 목록 제공
- 자동 rollback과 수동 rollback 구분

---

### [주의]

- Rollback 불가능 작업은 실행 전 승인 필수
- DB destructive 작업은 자동 실행 금지
- 외부 API 호출은 rollback 불가능할 수 있음
- 사용자에게 이미 발송된 메시지는 회수 불가
- 비용 발생 작업은 rollback 불가

---

### [FAQ]

Q. Harness에 Rollback Policy가 필요한 이유는?

A. Agent 작업 실패 시 피해를 줄이고 이전 상태로 복구하기 위해 필요하다.

Q. 모든 작업이 rollback 가능해?

A. 아니다. 외부 전송, 결제, 배포, DB 삭제 같은 작업은 rollback이 어렵거나 불가능하다.

Q. 파일 수정 rollback은 어떻게 해?

A. 변경 전 backup, git diff, patch, version control을 활용한다.

Q. Memory write도 rollback 대상이야?

A. 그렇다. 잘못 저장된 Memory는 이후 Agent 판단을 오염시킬 수 있다.

---

# 24. Harness Design Pattern Rules

## 24.1 기본 Harness Pattern

### [개념]

Harness Design Pattern은 Agent 실행 기반을 반복적으로 설계할 수 있도록 정리한 구조 패턴이다.

---

### [핵심]

기본 Pattern:

```text
Request
→ Agent
→ Context Provider
→ Planner
→ Tool Selector
→ Permission Checker
→ Tool Executor
→ Output Validator
→ State Updater
→ Result Verifier
→ Response
```

---

### [실무]

Agent별 Harness Pattern 예시:

Backend Agent Harness:

```text
User Task
→ Load Project Context
→ Read Files
→ Plan Code Change
→ Modify Files
→ Run Tests
→ Validate Result
→ Return Diff Summary
```

SQL Agent Harness:

```text
User Query
→ Load Schema
→ Generate SQL
→ Validate SQL Safety
→ Execute Read-Only Query
→ Analyze Result
→ Return Explanation
```

Review Agent Harness:

```text
Agent Output
→ Load Rules
→ Check Diff
→ Check Test Result
→ Check Risk
→ Generate Review
```

---

### [FAQ]

Q. Harness Pattern은 모든 Agent에 동일하게 적용해?

A. 기본 구조는 비슷하지만 Tool, Permission, Validation은 Agent 역할에 맞게 달라져야 한다.

Q. Backend Agent Harness의 핵심은 뭐야?

A. 코드 수정 권한, 테스트 실행, diff 검증, 실패 복구이다.

Q. SQL Agent Harness의 핵심은 뭐야?

A. 쿼리 안전성 검증, read-only 접근, 위험 SQL 차단이다.

Q. Review Agent Harness의 핵심은 뭐야?

A. 결과 검증, 규칙 준수 확인, 위험 분석이다.

---

# 25. Comparison Rules

## 25.1 관련 개념 비교

### [개념]

Harness Engineering은 여러 AI Agent 개념과 연결되지만 동일하지 않다.

---

### [Comparison]

| 개념                      | 의미                 | Harness와 관계                         |
| ------------------------- | -------------------- | -------------------------------------- |
| Prompt Engineering        | 모델 지시문 설계     | Harness 내부 입력 중 하나              |
| Context Engineering       | 문맥 구성 설계       | Harness가 Context Provider를 통해 사용 |
| Tool Calling              | 도구 호출 기술       | Harness가 통제하는 실행 기능           |
| Function Calling          | 함수 호출 인터페이스 | Harness의 Tool Execution 대상          |
| Agent Workflow            | Agent 작업 흐름      | Harness가 실행하고 관리                |
| Loop Engineering          | 반복 실행 구조       | Harness 상태와 검증을 사용             |
| Multi-Agent Orchestration | 여러 Agent 협업      | Agent별 Harness를 연결                 |
| Long-Term Memory          | 장기 기억            | Harness가 접근 정책을 제어             |
| Guardrails                | 안전 규칙            | Harness 내부 안전 계층                 |
| Observability             | 관찰 가능성          | Harness 로그와 trace 기반              |

---

### [실무]

문서 작성 시 혼동 방지:

- Harness Engineering을 Tool Calling 기본 문법으로 축소하지 않는다.
- Harness Engineering을 LangGraph 사용법으로 축소하지 않는다.
- Harness Engineering을 Guardrails 보안 문서로만 다루지 않는다.
- Harness Engineering은 Agent 실행 기반 전체를 다룬다.

---

### [FAQ]

Q. Harness Engineering과 Tool Calling 차이는?

A. Tool Calling은 도구 호출 방식이고 Harness Engineering은 도구 등록, 권한, 검증, 실행, 로그까지 포함하는 실행 기반 설계이다.

Q. Harness Engineering과 Loop Engineering 차이는?

A. Harness는 실행 기반이고 Loop는 반복 실행 구조이다.

Q. Harness Engineering과 Multi-Agent Orchestration 차이는?

A. Harness는 Agent 하나의 실행 기반이고 Orchestration은 여러 Agent를 연결하는 지휘 구조이다.

Q. Harness Engineering과 AI Observability 차이는?

A. Observability는 관찰과 분석이고 Harness는 관찰 데이터를 생성하는 실행 계층을 포함한다.

---

# 26. Best Practice Rules

## 26.1 Harness Engineering Best Practice

### [개념]

Best Practice는 Agent Harness를 안전하고 재현 가능하며 검증 가능한 구조로 만들기 위한 기준이다.

---

### [Best Practice]

- Agent별 Tool Registry 분리
- Tool Input Schema 필수화
- Tool Output Schema 필수화
- 최소 권한 원칙 적용
- Read Tool과 Write Tool 분리
- 위험 작업 Human Approval 적용
- Command Allowlist 사용
- File Access Allowlist 사용
- Secret Masking 적용
- Timeout 필수 설정
- Retry Limit 필수 설정
- Structured Error 반환
- State 저장
- Tool Execution Log 저장
- Diff 기반 변경 검토
- Result Verification 적용
- Rollback 가능성 확인
- Memory Write 검증
- Production 접근 제한
- Destructive 작업 기본 차단

---

### [실무]

개인 AI 개발팀 기준 우선 적용 순서:

1. Tool Registry
2. Tool Permission
3. Input Validation
4. Output Validation
5. Command Allowlist
6. File Access Policy
7. State Management
8. Logging
9. Human Approval
10. Result Verification
11. Retry Policy
12. Rollback Policy
13. Observability 연계
14. Memory Access Policy

---

### [FAQ]

Q. Harness Engineering에서 가장 먼저 만들어야 할 것은?

A. Tool Registry와 Permission Policy를 먼저 만드는 것이 좋다.

Q. Harness를 처음부터 완벽하게 만들어야 해?

A. 아니다. 읽기 도구, 쓰기 도구, 테스트 실행 도구부터 작게 시작하고 점진적으로 확장한다.

Q. 개인 AI 서버에서도 Harness가 필요해?

A. 필요하다. 개인 프로젝트라도 파일 수정, 명령 실행, DB 접근은 위험할 수 있기 때문이다.

Q. Harness Best Practice의 핵심은 뭐야?

A. 최소 권한, 구조화된 입출력, 검증, 로그, 승인, 복구 가능성이다.

---

# 27. Common Mistakes

## 27.1 Harness Engineering 자주 발생하는 실수

### [개념]

Harness Engineering에서 가장 흔한 문제는 Agent에게 너무 많은 권한을 주거나 실행 결과를 검증하지 않는 것이다.

---

### [핵심]

자주 발생하는 실수:

- 모든 Agent에게 모든 도구 허용
- Tool Registry 없이 도구 실행
- Input Schema 없이 Tool 호출
- Output Schema 없이 자연어 결과만 반환
- 권한 검증 없음
- File Access 제한 없음
- Shell Command 자유 실행
- Timeout 없음
- 무제한 Retry
- Error Classification 없음
- 로그 저장 없음
- Secret Masking 없음
- Human Approval 없음
- DB 변경 자동 실행
- Production 환경 직접 수정
- State 저장 없음
- 실패 후 같은 작업 반복
- 변경 파일 목록 누락
- Rollback 계획 없음
- Memory에 검증 안 된 정보 저장

---

### [주의]

치명적 실수:

- `.env` 내용 출력
- `rm -rf` 실행 허용
- Production DB에 DELETE 실행
- 승인 없는 배포
- Tool 실패를 성공으로 처리
- 테스트 실패를 무시
- 없는 도구를 hallucination으로 호출
- 외부 API 비용 폭증
- Agent가 권한 정책을 우회

---

### [FAQ]

Q. Harness Engineering에서 가장 위험한 실수는?

A. Agent에게 자유로운 shell command와 파일 수정 권한을 주는 것이다.

Q. Tool Output Schema가 없으면 왜 문제야?

A. Agent가 실패를 성공으로 오해하거나 다음 행동을 잘못 결정할 수 있다.

Q. Timeout이 없으면 어떤 문제가 생겨?

A. 도구가 무한 실행되거나 시스템 자원을 고갈시킬 수 있다.

Q. State 저장이 없으면 어떤 문제가 생겨?

A. Agent가 진행 상황을 잃고 같은 작업을 반복하거나 실패 원인을 추적하지 못한다.

---

# 28. Troubleshooting Rules

## 28.1 Tool Permission Error

### [Troubleshooting]

문제:

- Agent가 도구를 호출했지만 권한 오류가 발생함

원인:

- Agent 역할에 해당 도구 권한 없음
- Tool Registry 설정 누락
- 위험도 높은 작업에 승인 없음
- 권한 정책이 너무 엄격함

해결:

- Agent Role 확인
- Tool Registry 확인
- Permission Level 확인
- 승인 필요 작업인지 확인
- 권한을 넓히기 전에 작업 위험도 검토

---

## 28.2 Tool Schema Mismatch

### [Troubleshooting]

문제:

- Tool Input 또는 Output이 Schema와 맞지 않음

원인:

- 필수 필드 누락
- 타입 불일치
- 도구 버전 변경
- Agent가 잘못된 인자 생성
- Output 형식이 자연어로 변경됨

해결:

- inputSchema 확인
- outputSchema 확인
- Validation Error를 구조화
- Agent Prompt에 Schema 명시
- Tool Wrapper에서 변환 처리

---

## 28.3 Command Blocked

### [Troubleshooting]

문제:

- Agent 명령 실행이 차단됨

원인:

- allowlist에 없는 명령
- destructive command 감지
- shell injection 위험
- 승인 필요 명령
- 권한 부족

해결:

- 허용 명령 목록 확인
- 명령을 안전한 대체 명령으로 변경
- 위험 작업은 approval 요청
- 자유 shell 실행 대신 Tool로 캡슐화
- 실행 목적과 영향을 명확히 기록

---

## 28.4 Infinite Retry

### [Troubleshooting]

문제:

- Agent가 같은 도구를 계속 재시도함

원인:

- retryLimit 없음
- retryable 판단 오류
- State 업데이트 누락
- 실패 원인 분류 없음
- Loop 종료 조건 없음

해결:

- retryLimit 설정
- Error Classification 적용
- retryable 필드 사용
- State에 실패 이력 저장
- Loop Engineering 종료 조건 추가

---

## 28.5 Secret Leakage

### [Troubleshooting]

문제:

- 로그나 출력에 API Key, Token, Secret이 노출됨

원인:

- Secret Masking 없음
- `.env` 파일 직접 출력
- Tool Input 전체 로그 저장
- 오류 메시지에 인증 정보 포함

해결:

- Secret Masking 적용
- `.env` 접근 제한
- 로그 저장 전 민감정보 제거
- Auth Header 출력 금지
- Secret 파일은 read 제한

---

## 28.6 State Lost

### [Troubleshooting]

문제:

- Agent가 이전 단계 결과를 잃어버림

원인:

- State Store 없음
- Tool Result 저장 누락
- taskId 없음
- Multi-Agent 전달 구조 없음
- 실패 후 초기화됨

해결:

- taskId 기반 State 저장
- stepId와 toolCallId 기록
- Tool Result 구조화 저장
- Agent 간 전달 State 정의
- 실패 시 State 보존

---

# 29. Checklist Rules

## 29.1 Harness Engineering Checklist

### [Checklist]

- [ ] Agent Harness 목적을 설명했는가?
- [ ] Tool Registry 기준을 포함했는가?
- [ ] Tool Permission 기준을 포함했는가?
- [ ] Input Validation을 포함했는가?
- [ ] Output Validation을 포함했는가?
- [ ] State Management를 포함했는가?
- [ ] Memory Access Policy를 포함했는가?
- [ ] Execution Sandbox를 포함했는가?
- [ ] File Access Policy를 포함했는가?
- [ ] Command Execution Policy를 포함했는가?
- [ ] API Access Policy를 포함했는가?
- [ ] Database Access Policy를 포함했는가?
- [ ] Human Approval 기준을 포함했는가?
- [ ] Error Handling 기준을 포함했는가?
- [ ] Retry Policy를 포함했는가?
- [ ] Logging / Tracing 기준을 포함했는가?
- [ ] Guardrails 적용 지점을 포함했는가?
- [ ] Result Verification을 포함했는가?
- [ ] Rollback Policy를 포함했는가?
- [ ] Agent별 Harness 예시를 포함했는가?
- [ ] Tool Calling과 Harness 차이를 설명했는가?
- [ ] Loop Engineering과의 관계를 설명했는가?
- [ ] Multi-Agent Orchestration과의 관계를 설명했는가?
- [ ] Retrieval Queries를 포함했는가?

---

### [FAQ]

Q. Harness Engineering 문서 검수에서 가장 중요한 항목은?

A. Tool Permission, Input Validation, Output Validation, Logging, Human Approval, Result Verification이다.

Q. Checklist를 문서에 넣어도 돼?

A. 가능하다. Harness는 누락 위험이 크므로 Checklist가 RAG 검색과 검수에 유용하다.

Q. Agent별 Harness 예시는 필수야?

A. 강력 권장이다. 개인 AI 개발팀 구조에서는 Agent별 권한과 도구가 다르기 때문이다.

Q. Rollback Policy도 체크해야 해?

A. 해야 한다. Agent 작업 실패 시 복구 가능성이 중요하다.

---

# 30. Retrieval Optimization Rules

## 30.1 Retrieval Keyword Rules

### [개념]

Harness Engineering 문서는 Agent 실행 기반 검색에 최적화되어야 한다.

---

### [핵심]

강조 키워드:

- Harness Engineering
- Agent Harness
- LLM Harness
- Agent Runtime
- Agent Execution Environment
- Tool Registry
- Tool Calling Control
- Function Calling Control
- Tool Permission
- Tool Access Policy
- Input Validation
- Output Validation
- Tool Output Schema
- State Management
- Agent State
- Memory Access Policy
- Execution Sandbox
- File Access Policy
- Command Execution Policy
- API Access Policy
- Database Access Policy
- Human-in-the-Loop
- Human Approval
- Error Handling
- Retry Policy
- Timeout Policy
- Logging
- Tracing
- Audit Trail
- Guardrails
- Agent Safety
- Result Verification
- Rollback Policy
- Tool Failure Recovery
- Multi-Agent Harness
- Backend Agent Harness
- SQL Agent Harness
- Review Agent Harness
- DevOps Agent Harness

---

### [실무]

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

포함할 질문 패턴:

- Harness Engineering이 뭐야?
- Agent Harness가 뭐야?
- Tool Calling이랑 Harness 차이 뭐야?
- Agent 도구 권한은 어떻게 제한해?
- Agent가 파일 수정해도 돼?
- Agent가 명령어 실행해도 돼?
- Agent가 DB 수정해도 돼?
- Tool Registry는 어떻게 설계해?
- Tool Output Schema는 왜 필요해?
- Agent State는 왜 필요해?
- Human Approval은 언제 필요해?
- Agent 로그는 뭘 남겨야 해?
- Retry Policy는 어떻게 잡아?
- Guardrails는 Harness 어디에 들어가?
- Harness와 Loop Engineering 차이는?
- Multi-Agent에서 Harness는 어떻게 쓰여?

---

### [FAQ]

Q. Harness Engineering 문서는 검색 키워드를 반복해도 돼?

A. 가능하다. RAG 문서는 검색 최적화가 우선이므로 핵심 용어 반복이 허용된다.

Q. Retrieval Queries에는 어떤 질문을 넣어야 해?

A. 사용자가 실제로 물어볼 질문과 Agent가 검색할 가능성이 높은 질문을 넣어야 한다.

Q. Harness Engineering 문서는 사람용 학습 문서처럼 길게 써야 해?

A. 아니다. Agent 검색과 실행 규칙 적용에 유리하도록 짧고 구조적으로 작성해야 한다.

Q. 용어는 영어와 한글을 섞어도 돼?

A. 가능하지만 핵심 개념명은 일관되게 유지해야 한다. 예: Harness Engineering, Agent Harness, Tool Registry.

---

# 31. Version Rules

## 31.1 기준 버전

### [개념]

Harness Engineering 문서는 2026년 기준 AI Agent 시스템 설계를 기준으로 작성한다.

---

### [핵심]

기준:

- 2026 AI Agent System
- LLM Agent
- Agentic Workflow
- Tool Calling
- Function Calling
- LangGraph 기반 Agent Workflow 참고 가능
- MCP 기반 Tool Integration 참고 가능
- RAG 기반 Context Provider 참고 가능
- Structured Output
- Observability Hook
- Guardrails
- Human-in-the-Loop
- Multi-Agent System

---

### [실무]

Legacy 제외:

- 단일 Prompt만으로 모든 작업 처리
- 도구 권한 없는 무제한 Agent
- 자연어 Tool Output만 사용
- 로그 없는 Agent 실행
- 검증 없는 자동 파일 수정
- 승인 없는 배포 자동화
- 권한 없는 DB 변경
- 모든 Memory 무제한 참조
- 테스트 없는 코드 수정 Agent

---

### [FAQ]

Q. Harness Engineering은 2026년 기준으로 중요한 개념이야?

A. 중요하다. Agent가 실제 도구와 시스템을 다룰수록 Harness 설계가 안정성과 안전성을 결정한다.

Q. Legacy Agent 방식은 뭐가 문제야?

A. Prompt만으로 제어하고 권한, 검증, 로그, 승인 구조가 없으면 위험한 행동을 막기 어렵다.

Q. LangGraph를 쓰면 Harness가 자동으로 해결돼?

A. 아니다. LangGraph는 Workflow 구현 도구이고 Harness 정책은 별도로 설계해야 한다.

Q. MCP를 쓰면 Harness가 필요 없어?

A. 아니다. MCP는 도구 연결 표준에 가깝고, 권한, 검증, 로그, 승인 정책은 Harness에서 설계해야 한다.

---

# 32. File Relationship Rules

## 32.1 연계 문서

### [개념]

Harness Engineering은 Level 4 AI Expert 문서이며, Level 2 Agent 기초 문서와 Level 4 심화 문서를 연결한다.

---

### [핵심]

선행 문서:

- Prompt Engineering
- Context Engineering
- LLM Core & API Integration
- Tool Calling & Function Calling
- Agent Workflow Design
- Agent Memory & State Management
- Agent Evaluation & Guardrails
- LangChain & LangGraph

연계 문서:

- Agentic RAG
- Loop Engineering
- Advanced Multi-Agent Orchestration
- Long-Term Memory
- Tool Calling & Function Calling Reliability
- AI Guardrails & Security
- AI Observability
- MLOps
- RAG Evaluation & Retrieval Optimization

---

### [실무]

문서 간 역할:

- `Tool Calling & Function Calling`은 도구 호출 기본을 다룬다.
- `Harness Engineering`은 도구 실행 기반과 권한 제어를 다룬다.
- `Loop Engineering`은 반복 실행과 완료 조건을 다룬다.
- `Advanced Multi-Agent Orchestration`은 여러 Agent 연결을 다룬다.
- `AI Observability`는 Harness 로그와 trace 분석을 다룬다.
- `AI Guardrails & Security`는 Harness 보안 정책을 심화한다.

---

### [FAQ]

Q. Harness Engineering 전에 어떤 문서를 보면 좋아?

A. Tool Calling & Function Calling, Agent Workflow Design, Agent Memory & State Management를 먼저 보면 좋다.

Q. Harness Engineering 다음에는 어떤 문서가 자연스러워?

A. Loop Engineering, Advanced Multi-Agent Orchestration, AI Observability가 자연스럽다.

Q. Harness Engineering과 Tool Calling Reliability는 어떻게 연결돼?

A. Harness가 Tool 실행을 관리하고, Tool Calling Reliability는 도구 호출 실패와 신뢰성 문제를 더 깊게 다룬다.

Q. Harness Engineering과 Long-Term Memory는 어떻게 연결돼?

A. Harness가 Memory 접근 권한과 Memory write 검증을 제어한다.

---

# 33. Final Goal

## 33.1 Harness Engineering RAG 문서 최종 목표

### [개념]

Harness Engineering RAG 문서는 Agent가 실제 개발 환경에서 안전하게 도구를 사용하고, 상태를 유지하고, 실패를 복구하고, 결과를 검증할 수 있도록 만드는 기준 문서이다.

---

### [핵심]

최종적으로 Agent는 Harness Engineering 문서를 통해 아래를 수행할 수 있어야 한다.

- Agent Harness 개념 이해
- Tool Registry 설계
- Tool Permission 설계
- Tool Input Validation 적용
- Tool Output Validation 적용
- State Management 설계
- Memory Access Policy 설계
- Execution Sandbox 설계
- File Access Policy 설계
- Command Execution Policy 설계
- API Access Policy 설계
- Database Access Policy 설계
- Human Approval 기준 판단
- Error Handling 구조화
- Retry Policy 적용
- Logging / Tracing 설계
- Guardrails 적용
- Result Verification 수행
- Rollback Policy 판단
- Agent별 Harness 차이 이해
- Loop Engineering과 연계
- Multi-Agent Orchestration과 연계
- AI Observability와 연계

---

### [실무]

개인 AI 개발팀에서 Harness Engineering의 최종 목표는 단순 자동화가 아니다.

목표:

```text
Agent가 작업한다
→ Harness가 권한과 입력을 검증한다
→ Tool이 안전하게 실행된다
→ 결과가 구조화된다
→ State가 업데이트된다
→ 실패가 분류된다
→ 로그가 남는다
→ 필요 시 승인을 요청한다
→ 결과를 검증한다
→ 안전하게 다음 단계로 진행한다
```

---

### [FAQ]

Q. Harness Engineering 문서의 최종 목표는 뭐야?

A. Agent가 도구, 파일, 명령, DB, API를 안전하게 사용하고 결과를 검증할 수 있도록 실행 기반 규칙을 제공하는 것이다.

Q. Harness Engineering은 개인 AI 개발팀에서 꼭 필요해?

A. 필요하다. Agent가 실제 개발 작업을 수행하려면 권한, 검증, 로그, 실패 처리, 승인 구조가 있어야 한다.

Q. Harness Engineering 문서는 Agent 성능에 영향을 줘?

A. 영향을 준다. Harness 품질이 낮으면 Agent가 도구를 잘못 쓰거나 실패를 추적하지 못한다.

Q. Harness Engineering의 핵심 한 줄 요약은?

A. Harness Engineering은 LLM Agent를 안전하고 검증 가능한 실행 시스템으로 만드는 설계 영역이다.

---

# Retrieval Queries

### [FAQ]

Q. Harness Engineering이 뭐야?

A. LLM Agent가 실제 작업을 수행할 수 있도록 도구, 권한, 상태, 메모리, 검증, 로그, 안전장치를 설계하는 영역이다.

Q. Agent Harness가 뭐야?

A. Agent Harness는 모델 출력이 실제 도구 실행과 작업 결과로 이어지도록 제어하는 실행 기반이다.

Q. Harness는 모델이야?

A. 아니다. Harness는 모델 주변의 Tool, State, Memory, Permission, Validation, Logging, Guardrails를 포함하는 실행 환경이다.

Q. Harness Engineering은 Prompt Engineering과 뭐가 달라?

A. Prompt Engineering은 지시문 설계이고 Harness Engineering은 Agent 실행 기반 설계이다.

Q. Harness Engineering은 Context Engineering과 뭐가 달라?

A. Context Engineering은 문맥 구성이고 Harness Engineering은 도구 실행, 권한, 상태, 검증, 로그를 관리한다.

Q. Harness Engineering은 Tool Calling과 뭐가 달라?

A. Tool Calling은 도구 호출 방식이고 Harness Engineering은 도구 등록, 권한, 입력 검증, 실행, 출력 검증, 로그까지 포함한다.

Q. Harness Engineering은 Loop Engineering과 뭐가 달라?

A. Harness는 실행 기반이고 Loop Engineering은 실행, 검증, 수정, 재실행을 반복하는 구조이다.

Q. Harness Engineering은 Multi-Agent Orchestration과 뭐가 달라?

A. Harness는 각 Agent의 실행 기반이고 Multi-Agent Orchestration은 여러 Agent를 연결하고 조율하는 구조이다.

Q. Harness Engineering은 Level 2야 Level 4야?

A. Level 4가 적절하다. Tool Calling, Agent Workflow, Memory, Guardrails를 통합하는 상위 심화 개념이기 때문이다.

Q. Harness Engineering 문서에는 무엇을 포함해야 해?

A. Tool Registry, Tool Permission, Input Validation, Output Validation, State Management, Memory Access, Sandbox, Logging, Guardrails, Rollback을 포함한다.

Q. Tool Registry는 뭐야?

A. Agent가 사용할 수 있는 도구 목록과 입력 스키마, 출력 스키마, 권한, 위험도, 실행 조건을 관리하는 구조이다.

Q. Tool Permission은 왜 필요해?

A. Agent가 권한 없는 파일 수정, 명령 실행, DB 변경, 배포 작업을 하지 못하게 제한하기 위해 필요하다.

Q. Agent에게 모든 도구 권한을 줘도 돼?

A. 안 된다. 최소 권한 원칙을 적용해야 한다.

Q. Tool Input Validation은 왜 필요해?

A. 잘못된 입력이 파일 훼손, 명령 오작동, 보안 사고로 이어지는 것을 막기 위해 필요하다.

Q. Tool Output Validation은 왜 필요해?

A. Agent가 도구 결과를 안정적으로 해석하고 실패를 성공으로 오해하지 않도록 하기 위해 필요하다.

Q. Tool Output은 자연어로 반환해도 돼?

A. 권장하지 않는다. success, errorCode, message, data, retryable을 포함한 구조화된 JSON 출력이 좋다.

Q. Agent State는 왜 필요해?

A. 현재 작업 단계, 도구 실행 결과, 실패 이력, 변경 파일, 승인 상태를 추적하기 위해 필요하다.

Q. State와 Memory는 뭐가 달라?

A. State는 현재 작업 진행 상태이고 Memory는 장기적으로 재사용할 정보이다.

Q. Memory Access Policy는 왜 필요해?

A. Agent가 불필요하거나 위험한 기억을 참조하거나 잘못된 정보를 저장하지 않게 제어하기 위해 필요하다.

Q. Execution Sandbox는 왜 필요해?

A. Agent의 코드 실행, 명령 실행, 파일 작업을 안전한 범위 안에서 제한하기 위해 필요하다.

Q. Agent가 파일을 수정해도 돼?

A. 역할과 권한에 따라 가능하다. 단, write allowlist, diff, backup, human approval 기준이 필요하다.

Q. `.env` 파일을 Agent가 읽어도 돼?

A. 기본적으로 제한해야 한다. API Key와 Secret 노출 위험이 있기 때문이다.

Q. Agent가 shell command를 실행해도 돼?

A. 제한된 allowlist 기반으로 테스트, 빌드, lint 같은 안전 명령만 허용하는 것이 좋다.

Q. `rm -rf` 명령을 Agent에게 허용해도 돼?

A. 기본적으로 금지해야 한다. destructive command는 human approval이 필요하다.

Q. Agent가 DB를 수정해도 돼?

A. 기본적으로 금지해야 한다. SELECT 중심으로 제한하고 DML, DDL은 승인과 검토 후 실행해야 한다.

Q. SQL Agent Harness의 핵심은 뭐야?

A. read-only 접근, 위험 SQL 차단, Query Timeout, Row Limit, Migration Review이다.

Q. Backend Agent Harness의 핵심은 뭐야?

A. 코드 읽기, 코드 수정, 테스트 실행, 빌드 실행, diff 검증, 실패 처리이다.

Q. Review Agent Harness의 핵심은 뭐야?

A. Agent 결과, 변경 파일, 테스트 결과, 규칙 위반, 보안 위험을 검증하는 것이다.

Q. Human-in-the-Loop은 언제 필요해?

A. 파일 삭제, 대량 수정, DB 변경, 배포, Secret 변경, 비용 발생 작업처럼 위험하거나 되돌리기 어려운 작업에 필요하다.

Q. Retry Policy는 어떻게 잡아야 해?

A. retryable 오류만 제한된 횟수로 재시도하고 PermissionError, ValidationError, destructive 작업은 자동 재시도하지 않는다.

Q. Timeout Policy는 왜 필요해?

A. 도구 실행이 무한 대기하거나 시스템 자원을 고갈시키는 것을 막기 위해 필요하다.

Q. Harness Logging에는 무엇을 남겨야 해?

A. taskId, agentName, toolName, success, errorType, executionTime, changedFiles, approvalStatus, retryCount를 남기는 것이 좋다.

Q. Secret은 로그에 남겨도 돼?

A. 안 된다. API Key, Token, Password, `.env` 값은 반드시 마스킹하거나 저장하지 않아야 한다.

Q. Harness Guardrails는 어디에 적용해?

A. User Input, Retrieved Context, Tool Call, Tool Input, Tool Output, File Access, Command Execution, API Access, DB Access, Final Answer에 적용한다.

Q. 없는 도구를 Agent가 호출하면 어떻게 해?

A. Tool Registry에 없는 도구는 실행하지 않고 구조화된 오류를 반환해야 한다.

Q. Result Verification은 왜 필요해?

A. Agent가 완료했다고 말해도 실제 요구사항, 테스트, 보안, 문서 규칙을 만족하지 않을 수 있기 때문이다.

Q. Rollback Policy는 왜 필요해?

A. Agent 작업 실패나 위험한 변경 발생 시 이전 상태로 복구하기 위해 필요하다.

Q. Harness Engineering과 AI Observability는 어떻게 연결돼?

A. Harness가 Tool 실행 로그와 trace를 생성하고 AI Observability가 이를 분석한다.

Q. Harness Engineering과 AI Guardrails & Security는 어떻게 연결돼?

A. Harness가 실행 단계의 안전 제어를 담당하고 AI Guardrails & Security가 보안 정책을 심화한다.

Q. Harness Engineering과 Long-Term Memory는 어떻게 연결돼?

A. Harness가 Long-Term Memory 접근 권한, 검색 조건, 저장 검증을 제어한다.

Q. Harness Engineering을 처음 도입할 때 무엇부터 만들면 돼?

A. Tool Registry, Permission Policy, Input Validation, Output Validation, Logging부터 만드는 것이 좋다.

Q. 개인 AI 서버에서도 Harness Engineering이 필요해?

A. 필요하다. 개인 프로젝트라도 Agent가 파일, 명령, DB, API를 다루면 안전한 실행 기반이 필요하다.

Q. Harness Engineering의 핵심 한 줄 요약은?

A. Harness Engineering은 LLM Agent를 안전하고 검증 가능한 실행 시스템으로 만드는 설계 영역이다.
