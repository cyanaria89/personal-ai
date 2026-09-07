# Tool Calling & Function Calling Reliability Domain Rules

---

# 1. Domain Purpose

## 1.1 Tool Calling & Function Calling Reliability 문서 목적

### [개념]

Tool Calling & Function Calling Reliability Domain 문서는 AI Agent / AI/ML Agent / Backend Agent / DevOps Agent / Review Agent / Architecture Review Agent가 LLM 기반 Tool Calling, Function Calling, API Calling, Structured Output, Agent Tool Workflow를 설계, 구현, 검토, 평가할 때 참조하는 RAG 제작 규칙 문서이다.

Tool Calling은 LLM이 외부 도구, 내부 함수, API, 검색기, DB, 파일 시스템, 코드 실행기, 캘린더, 이메일, 배포 도구 등을 호출해 작업을 수행하는 구조이다.

Function Calling은 Tool Calling의 한 형태로, 모델이 정해진 Schema에 맞춰 함수 이름과 인자를 생성하고 시스템이 해당 함수를 실행하는 방식이다.

Reliability는 Tool Call이 정확한 도구를 선택하고, 올바른 인자를 생성하고, 실행 결과를 검증하고, 실패 시 안전하게 복구하는 능력을 의미한다.

---

### [핵심]

- Tool Calling = LLM이 외부 도구나 시스템 기능을 호출하는 구조
- Function Calling = Schema 기반 함수 호출 구조
- Reliability = 정확한 도구 선택 + 인자 검증 + 실행 검증 + 오류 복구
- Tool Schema 품질이 호출 품질을 결정
- Input Validation 필수
- Output Validation 필수
- Permission Check 필수
- State Change Tool은 승인 기준 필요
- Retry / Fallback 기준 필요
- Idempotency 기준 필요
- Tool Result를 그대로 신뢰하지 않음
- Tool Call Trace와 Observability 필요
- Agentic RAG / Multi-Agent Orchestration / AI Observability와 연결 가능

---

### [실무]

2026 실무 기준 Tool Calling & Function Calling Reliability 문서는 다음 목적을 우선한다.

- Tool Calling 적용 여부 판단
- Tool Schema 설계 기준 제공
- Function Argument Validation 기준 제공
- Tool Selection 기준 제공
- Tool Execution Flow 제공
- Tool Result Validation 기준 제공
- Error Handling 기준 제공
- Retry / Fallback 기준 제공
- Permission / Approval 기준 제공
- State Change Tool 안전 기준 제공
- Tool Calling Evaluation 기준 제공
- Tool Observability 기준 제공
- Multi-Agent Tool Coordination 기준 제공

이 문서는 사람이 Function Calling API 문법을 공부하기 위한 문서가 아니라, Agent가 도구 호출을 안정적으로 수행하고 실패를 안전하게 처리할 수 있도록 돕는 운영 지식 문서로 작성한다.

---

### [FAQ]

Q. Tool Calling & Function Calling Reliability 문서는 무엇을 위한 문서인가?

A. Agent가 도구를 정확히 선택하고, 인자를 검증하고, 실행 결과를 확인하고, 실패 시 안전하게 복구할 수 있도록 기준을 제공하는 문서이다.

Q. Tool Calling과 Function Calling은 같은가?

A. Function Calling은 Tool Calling의 한 형태이다. Tool Calling은 검색, 파일, API, DB, 코드 실행, 상태 변경 도구 호출까지 더 넓게 포함한다.

Q. Tool Calling Reliability에서 가장 중요한 것은?

A. Tool Schema, 인자 검증, 권한 확인, 실행 결과 검증, 실패 처리, 상태 변경 안전성이다.

---

# 2. Scope

## 2.1 포함 범위

### [개념]

Tool Calling & Function Calling Reliability Domain 문서는 LLM과 Agent가 외부 도구를 안정적으로 호출하기 위한 Schema, Validation, Execution, Permission, Error Handling, Evaluation, Observability 기준을 포함한다.

---

### [핵심]

포함 범위:

- Tool Calling
- Function Calling
- Structured Output
- Tool Schema
- JSON Schema
- Function Signature
- Tool Selection
- Tool Routing
- Argument Generation
- Argument Validation
- Input Validation
- Output Validation
- Permission Check
- Approval Flow
- State Change Tool
- Read-Only Tool
- Idempotency
- Retry
- Fallback
- Timeout
- Rate Limit
- Error Handling
- Tool Result Verification
- Tool Call Trace
- Tool Evaluation
- Tool Observability
- Multi-Agent Tool Coordination
- Safety Guardrails

제외 범위:

- 특정 플랫폼 Function Calling API 전체 문서 복붙
- 모든 외부 API 사용법 사전식 정리
- 일반 HTTP API 설계 전체 설명
- 백엔드 인증 전체 상세
- DevOps 배포 도구 전체 매뉴얼
- 보안 정책 없는 자동 실행 권장
- 사용자 승인 없는 위험 작업 자동화 권장
- Tool Result 무검증 사용 권장

---

### [실무]

Tool Calling & Function Calling Reliability 문서는 아래 질문에 답할 수 있어야 한다.

- 이 작업에 Tool Calling이 필요한가?
- 어떤 Tool을 선택해야 하는가?
- Tool Schema는 어떻게 정의해야 하는가?
- Function Argument는 어떻게 검증해야 하는가?
- Tool 호출 전 권한 확인이 필요한가?
- Tool Result는 어떻게 검증해야 하는가?
- Tool 호출 실패 시 Retry해야 하는가?
- Retry하면 안 되는 도구는 무엇인가?
- 상태 변경 Tool은 언제 사용자 승인이 필요한가?
- Tool Call이 Agent State에 어떤 영향을 주는가?
- Tool Calling 품질은 어떻게 평가해야 하는가?

---

### [FAQ]

Q. Tool Calling 문서에 API 사용 예시만 넣어도 되는가?

A. 아니다. Tool 선택, Schema, Validation, Permission, Error Handling, Observability 기준을 함께 작성해야 한다.

Q. Tool Result는 항상 사실로 취급해도 되는가?

A. 아니다. Tool Result도 오류, 누락, 오래된 정보, 권한 문제, 포맷 문제를 가질 수 있으므로 검증해야 한다.

Q. 상태 변경 Tool은 왜 특별히 다뤄야 하는가?

A. 이메일 전송, 파일 삭제, DB 변경, 배포 실행처럼 되돌리기 어려운 결과를 만들 수 있기 때문이다.

---

# 3. Section Priority

## 3.1 필수 섹션 규칙

### [개념]

Tool Calling & Function Calling Reliability 문서는 모든 주요 Chunk에 `[개념]`, `[핵심]`, `[실무]`, `[FAQ]`를 우선 적용한다.

실행 흐름이 필요한 주제는 `[Flow]`를 추가한다.

검증이 필요한 주제는 `[Checklist]`를 추가한다.

오류 대응이 필요한 주제는 `[Troubleshooting]`을 추가한다.

보안과 권한이 필요한 주제는 `[주의]`, `[Guardrails]`를 추가한다.

---

### [핵심]

Required:

- [개념]
- [핵심]
- [실무]
- [FAQ]

Strongly Recommended:

- [Flow]
- [예제]
- [주의]
- [Best Practice]
- [Checklist]
- [Troubleshooting]
- [Comparison]

Optional:

- [Tool Schema]
- [Function Schema]
- [Validation Rule]
- [Permission Rule]
- [Evaluation]
- [Review Point]
- [Anti-Pattern]

---

### [실무]

Tool Calling & Function Calling Reliability 문서는 단순 개념 설명보다 실행 안전성과 검증 기준을 우선한다.

각 문서는 아래 정보 중 최소 2개 이상을 포함한다.

- Tool Schema 기준
- Tool Selection 기준
- Argument Validation 기준
- Permission Check 기준
- Tool Result Validation 기준
- Retry / Fallback 기준
- State Change Safety 기준
- Evaluation 기준
- Observability 기준
- Troubleshooting 기준

---

### [FAQ]

Q. Tool Calling 문서에 Flow가 필요한가?

A. 필요하다. Tool Call은 선택, 인자 생성, 검증, 실행, 결과 검증, State Update 흐름을 가진다.

Q. Tool Calling 문서에 Guardrails가 필요한 이유는?

A. Tool은 실제 외부 시스템에 영향을 줄 수 있으므로 권한, 승인, 상태 변경 안전 기준이 필요하다.

Q. Function Schema 섹션은 언제 필요한가?

A. 함수 이름, 설명, 인자, 타입, 필수값, 제약 조건을 명확히 정의해야 할 때 필요하다.

---

# 4. Core Concept Rules

## 4.1 Tool Calling 핵심 개념 작성 규칙

### [개념]

Tool Calling 핵심 개념은 일반 LLM 답변 생성, API 호출, Agent Workflow와 구분되도록 작성한다.

Tool Calling은 모델이 직접 모든 답을 생성하지 않고, 필요한 외부 기능을 호출해 정보를 얻거나 작업을 수행하는 구조이다.

Function Calling은 Tool Calling을 구조화된 Schema로 제한해 함수 이름과 인자를 안정적으로 생성하도록 하는 방식이다.

---

### [핵심]

반드시 포함할 개념:

- Tool Calling
- Function Calling
- Structured Output
- Tool Schema
- Function Signature
- JSON Schema
- Tool Selection
- Argument Generation
- Argument Validation
- Input Validation
- Output Validation
- Tool Execution
- Tool Result
- Permission Check
- Approval Flow
- Idempotency
- Retry
- Fallback
- Timeout
- Rate Limit
- Error Handling
- Tool Observability

용어 통일:

- Tool Calling
- Function Calling
- Tool Schema
- Function Schema
- Tool Selection
- Tool Input
- Tool Output
- Tool Result
- Argument Validation
- Tool Execution
- Tool Result Validation
- State Change Tool
- Read-Only Tool
- Tool Call Trace

---

### [실무]

Tool Calling 설명은 아래 구분을 반드시 포함한다.

```text
LLM Answer
→ 모델이 내부 지식과 Context로 답변 생성

RAG Retrieval
→ 외부 문서를 검색해 Context로 제공

Tool Calling
→ 외부 도구를 호출해 검색, 계산, 실행, 조회, 상태 변경 수행

Function Calling
→ 정해진 Function Schema에 맞춰 함수 이름과 인자를 생성하고 시스템이 실행
```

Tool Calling 문서는 “도구를 호출한다” 수준에서 멈추면 안 된다.

Agent가 언제 호출하고, 무엇을 호출하고, 어떤 인자를 넣고, 결과를 어떻게 검증하고, 실패 시 어떻게 복구할지 판단할 수 있어야 한다.

---

### [FAQ]

Q. Tool Calling이란?

A. LLM이나 Agent가 외부 도구, API, 함수, 검색기, DB, 코드 실행기 등을 호출해 정보를 얻거나 작업을 수행하는 구조이다.

Q. Function Calling이란?

A. 정해진 Function Schema에 따라 모델이 함수 이름과 인자를 생성하고 시스템이 해당 함수를 실행하는 방식이다.

Q. Tool Calling Reliability란?

A. 도구 선택, 인자 생성, 검증, 실행, 결과 확인, 오류 복구가 안정적으로 이루어지는 정도이다.

---

# 5. Tool Type Rules

## 5.1 Tool 유형 작성 규칙

### [개념]

Tool Type은 Agent가 호출할 수 있는 도구를 역할과 위험도에 따라 분류하는 기준이다.

Tool Type을 구분해야 권한, 승인, Retry, Logging, Validation 기준을 다르게 적용할 수 있다.

---

### [핵심]

대표 Tool Type:

- Search Tool
- File Search Tool
- Web Search Tool
- Calculator Tool
- Code Execution Tool
- Database Read Tool
- Database Write Tool
- API Read Tool
- API Write Tool
- Email Tool
- Calendar Tool
- File System Tool
- Deployment Tool
- Monitoring Tool
- Evaluation Tool
- Memory Tool

위험도 기준:

- Read-Only Tool: 조회만 수행
- Computation Tool: 계산 또는 변환 수행
- External Read Tool: 외부 시스템 조회
- State Change Tool: 외부 상태 변경
- Destructive Tool: 삭제, 덮어쓰기, 배포, 결제 등 위험 작업
- Sensitive Tool: 개인정보, 인증, 보안정보 접근 가능

---

### [실무]

Tool Type별 기준:

```text
Read-Only Tool:
- 검색, 조회, 계산
- 낮은 위험
- 결과 검증 필요

State Change Tool:
- 이메일 전송, 캘린더 생성, DB 수정
- 사용자 승인 또는 정책 확인 필요
- 실행 로그 필요

Destructive Tool:
- 파일 삭제, DB 삭제, 배포 실행, 권한 변경
- Human Review 또는 명시적 승인 필요
- Rollback 가능성 확인 필요
```

Tool Type을 명확히 정의하지 않으면 Agent가 위험 작업을 일반 조회처럼 처리할 수 있다.

---

### [FAQ]

Q. Tool Type을 나누는 이유는?

A. 도구 유형에 따라 권한, 승인, 검증, Retry, Rollback 기준이 다르기 때문이다.

Q. Read-Only Tool은 안전한가?

A. 상대적으로 안전하지만 결과 오류, 오래된 정보, 민감정보 노출 가능성이 있으므로 검증이 필요하다.

Q. Destructive Tool은 무엇인가?

A. 파일 삭제, DB 삭제, 배포 실행, 결제 처리처럼 되돌리기 어렵거나 위험한 상태 변경 도구이다.

---

# 6. Tool Selection Rules

## 6.1 Tool Selection 작성 규칙

### [개념]

Tool Selection은 Agent가 현재 작업을 해결하기 위해 어떤 도구를 호출할지 결정하는 과정이다.

Tool Selection이 잘못되면 불필요한 호출, 잘못된 결과, 비용 증가, 위험한 상태 변경이 발생한다.

---

### [핵심]

Tool Selection 기준:

- 사용자 요청 목적
- 필요한 정보 유형
- 현재 Context 충분성
- 최신성 필요 여부
- 계산 필요 여부
- 실행 검증 필요 여부
- 외부 시스템 조회 필요 여부
- 상태 변경 필요 여부
- 권한 필요 여부
- 위험도
- 비용
- 지연
- 대체 Tool 존재 여부

Tool 호출 필요 상황:

- 최신 정보 필요
- 정확한 계산 필요
- 파일 내용 확인 필요
- DB 조회 필요
- API 조회 필요
- 코드 실행 검증 필요
- 외부 상태 변경 요청
- RAG 검색 필요
- Evaluation 수행 필요

---

### [실무]

Tool Selection Flow:

```text
User Request
→ Task Classification
→ Context Sufficiency Check
→ Tool Need Check
→ Tool Candidate Selection
→ Risk Classification
→ Permission Check
→ Tool Call Decision
```

Tool Selection 예시:

```text
요청:
첨부된 로그 파일에서 에러 원인을 찾아줘

판단:
- 파일 내용 확인 필요
- File Read Tool 필요
- Read-Only 작업
- 검색 결과 기반 분석
- 상태 변경 없음
```

Tool을 호출하지 않아도 되는 상황에서는 호출하지 않는다.

불필요한 Tool Call은 비용, 지연, 오류 가능성을 증가시킨다.

---

### [FAQ]

Q. Tool Selection은 왜 중요한가?

A. 올바른 도구를 선택해야 정확한 결과를 얻고 불필요한 비용과 위험을 줄일 수 있기 때문이다.

Q. Tool Calling은 항상 필요한가?

A. 아니다. 제공된 Context나 RAG 문서만으로 충분하면 Tool Calling을 생략할 수 있다.

Q. 최신 정보가 필요한 경우에는 Tool Calling이 필요한가?

A. 필요할 수 있다. 최신성 요구가 있으면 Web Search, API, DB 같은 외부 조회 도구를 고려한다.

---

# 7. Tool Schema Rules

## 7.1 Tool Schema 작성 규칙

### [개념]

Tool Schema는 Tool의 이름, 설명, 입력 인자, 출력 형식, 제약 조건, 오류 조건을 정의하는 구조이다.

Tool Schema 품질은 Function Calling 정확도와 Tool Calling Reliability를 결정한다.

---

### [핵심]

Tool Schema 구성 요소:

- toolName
- description
- inputSchema
- outputSchema
- requiredFields
- optionalFields
- fieldType
- enumValues
- defaultValue
- constraints
- examples
- errorCases
- permissionLevel
- sideEffect
- idempotency
- timeout
- rateLimit

Schema 작성 기준:

- Tool 이름은 명확하게
- 설명은 짧고 구체적으로
- 인자 이름은 Domain 용어와 일치
- 필수값과 선택값 구분
- enum은 가능한 값 제한
- 위험한 기본값 금지
- 상태 변경 여부 명시
- 오류 조건 명시
- 예시는 짧고 정확하게

---

### [실무]

Tool Schema 예시:

```json
{
  "toolName": "search_documents",
  "description": "Search RAG documents by query and optional domain filter.",
  "inputSchema": {
    "query": "string",
    "domain": "string optional",
    "topK": "integer optional"
  },
  "requiredFields": ["query"],
  "outputSchema": {
    "results": "array",
    "source": "string",
    "score": "number"
  },
  "sideEffect": "none",
  "permissionLevel": "read"
}
```

나쁜 Schema 예시:

```text
toolName:
- do_task

description:
- 사용자의 요청을 처리한다.
```

Tool Schema는 모델이 도구를 선택하고 인자를 생성하는 기준이므로 모호하면 안 된다.

---

### [FAQ]

Q. Tool Schema는 왜 중요한가?

A. 모델은 Schema를 기준으로 도구를 선택하고 인자를 생성하므로 Schema가 모호하면 호출 오류가 증가한다.

Q. Tool description은 길수록 좋은가?

A. 아니다. 짧고 구체적으로 Tool의 목적과 사용 조건을 설명해야 한다.

Q. sideEffect를 표시해야 하는 이유는?

A. Tool이 외부 상태를 변경하는지 확인해야 권한과 승인 기준을 적용할 수 있기 때문이다.

---

# 8. Function Argument Rules

## 8.1 Function Argument 생성 / 검증 규칙

### [개념]

Function Argument는 모델이 Function Calling을 위해 생성하는 입력값이다.

Argument가 잘못되면 Tool 실행 실패, 잘못된 데이터 조회, 위험한 상태 변경이 발생할 수 있다.

---

### [핵심]

Argument 검증 항목:

- 필수값 존재 여부
- 타입 일치 여부
- enum 값 일치 여부
- 범위 제약
- 문자열 길이
- 날짜 형식
- ID 형식
- 이메일 형식
- URL 형식
- 파일 경로 유효성
- SQL Injection 위험
- Shell Injection 위험
- 권한 범위
- 민감정보 포함 여부

Argument 생성 기준:

- 사용자 요청에서 명시된 값 우선
- 추측으로 중요한 값 생성 금지
- 불확실한 값은 확인 필요
- 위험 작업 인자는 보수적으로 생성
- 기본값은 안전한 값 사용
- 상태 변경 인자는 승인 전 실행 금지

---

### [실무]

Argument Validation 예시:

```text
Function:
- create_calendar_event

Required:
- title
- startTime
- endTime

Validation:
- startTime < endTime
- timezone 존재
- attendee email 형식 확인
- 사용자가 명시하지 않은 참석자 추가 금지
```

검증 실패 예시:

```text
문제:
delete_file(path="/")

원인:
- 위험한 경로
- 삭제 범위 과도
- 사용자 승인 없음

처리:
- Tool Call 차단
- 사용자 확인 또는 안전한 대안 요청
```

---

### [FAQ]

Q. Function Argument Validation은 왜 필요한가?

A. 잘못된 인자는 실행 실패, 잘못된 조회, 데이터 변경, 보안 문제를 만들 수 있기 때문이다.

Q. 모델이 누락된 인자를 추측해도 되는가?

A. 중요하지 않은 안전한 기본값은 가능하지만, 상태 변경이나 위험 작업 인자는 추측하면 안 된다.

Q. enum 값은 왜 사용하는가?

A. 가능한 입력값을 제한해 잘못된 인자 생성과 실행 오류를 줄이기 위해 사용한다.

---

# 9. Structured Output Rules

## 9.1 Structured Output 작성 규칙

### [개념]

Structured Output은 LLM이 자유 텍스트가 아니라 JSON, XML, Markdown Schema, Function Argument 등 정해진 구조로 출력하는 방식이다.

Function Calling Reliability는 Structured Output 안정성에 크게 의존한다.

---

### [핵심]

Structured Output 대상:

- JSON
- JSON Schema
- Function Argument
- Tool Result Summary
- Agent Output Contract
- Evaluation Result
- Validation Report
- Error Report
- Retry Request
- Fix Request

Structured Output 기준:

- Schema 준수
- 필수 필드 포함
- 타입 일치
- 불필요한 필드 제거
- 중첩 구조 과도화 금지
- 문자열 Escape 확인
- null 허용 여부 명시
- 출력 전 Validation
- 파싱 실패 대응

---

### [실무]

Structured Output 예시:

```json
{
  "status": "failed",
  "errorType": "missing_required_argument",
  "missingFields": ["startTime"],
  "retryable": true,
  "nextAction": "request_missing_field"
}
```

Structured Output 실패 대응:

```text
문제:
JSON Parsing 실패

해결:
- Schema 단순화
- 필수 필드 명확화
- 출력 전 Validation
- Retry 시 오류 메시지와 기대 Schema 제공
```

---

### [FAQ]

Q. Structured Output은 왜 필요한가?

A. Agent와 Backend가 LLM 출력을 안정적으로 파싱하고 Tool Execution에 사용할 수 있게 하기 위해 필요하다.

Q. JSON 출력이 자주 깨지면 어떻게 해야 하는가?

A. Schema를 단순화하고, 필수 필드를 줄이고, Validation과 Retry 전략을 추가해야 한다.

Q. Structured Output과 Function Calling은 어떤 관계인가?

A. Function Calling은 Structured Output을 활용해 함수 이름과 인자를 안정적으로 생성하는 방식이다.

---

# 10. Input Validation Rules

## 10.1 Tool Input Validation 작성 규칙

### [개념]

Input Validation은 Tool 실행 전 입력값이 Schema, 권한, 보안, 범위, 상태 조건을 만족하는지 검증하는 과정이다.

Tool Calling에서는 LLM이 생성한 입력을 그대로 실행하면 안 된다.

---

### [핵심]

Input Validation 항목:

- Schema Validation
- Type Validation
- Required Field Validation
- Range Validation
- Format Validation
- Permission Validation
- Safety Validation
- Injection Validation
- State Validation
- Business Rule Validation

보안 검증:

- SQL Injection 방지
- Command Injection 방지
- Path Traversal 방지
- SSRF 방지
- Prompt Injection 영향 차단
- Secret 노출 방지
- 권한 없는 Resource 접근 차단

---

### [실무]

Input Validation Flow:

```text
Tool Input 생성
→ Schema Validation
→ Permission Check
→ Safety Check
→ Business Rule Check
→ Execute or Reject
```

Input Validation 예시:

```text
Tool:
- database_query

검증:
- read-only query인지 확인
- DROP / DELETE / UPDATE 차단
- parameter binding 사용
- 접근 가능한 table인지 확인
```

LLM이 생성한 Tool Input은 신뢰할 수 없는 입력으로 취급한다.

---

### [FAQ]

Q. Tool Input Validation은 왜 필요한가?

A. LLM이 생성한 입력이 잘못되거나 위험할 수 있으므로 실행 전 검증해야 한다.

Q. LLM이 만든 SQL을 바로 실행해도 되는가?

A. 안 된다. Read-only 제한, Parameter Binding, 권한 검증, 위험 명령 차단이 필요하다.

Q. Prompt Injection도 Tool Input에 영향을 줄 수 있는가?

A. 있다. 악의적 지시가 Tool Argument에 반영되지 않도록 검증해야 한다.

---

# 11. Output Validation Rules

## 11.1 Tool Output Validation 작성 규칙

### [개념]

Output Validation은 Tool 실행 결과가 기대한 형식, 범위, 상태, 신뢰도, 최신성 조건을 만족하는지 검증하는 과정이다.

Tool이 성공했다고 해서 결과가 항상 유효한 것은 아니다.

---

### [핵심]

Output Validation 항목:

- Output Schema 일치
- Null / Empty 결과 확인
- Error 포함 여부
- Partial Result 여부
- Timestamp 확인
- Source 확인
- Confidence 확인
- Data Range 확인
- Duplicate 확인
- Permission Error 확인
- Rate Limit Error 확인
- Stale Data 확인
- State Change 확인
- Result Consistency 확인

Output 처리 기준:

- 정상 결과 → 다음 단계 사용
- Empty 결과 → No Result 처리 또는 Re-Query
- Partial 결과 → 불완전 표시
- 오류 결과 → Error Handling
- 충돌 결과 → Review 또는 Verification
- 상태 변경 결과 → Audit Log 기록

---

### [실무]

Output Validation 예시:

```text
Tool:
- search_documents

Output:
- results: []

Validation:
- 검색 결과 없음
- Query Rewrite 필요
- 답변 생성 금지
- No Context 상태로 표시
```

Tool Result를 최종 답변에 반영하기 전에는 다음을 확인한다.

```text
- 결과가 현재 요청과 관련 있는가?
- 결과가 최신인가?
- 결과가 완전한가?
- 결과가 다른 Context와 충돌하지 않는가?
- 결과가 사용자에게 보여도 안전한가?
```

---

### [FAQ]

Q. Tool Output Validation은 왜 필요한가?

A. Tool이 성공해도 결과가 비어 있거나 오래되었거나 부분 결과일 수 있기 때문이다.

Q. Empty Result는 실패인가?

A. 항상 실패는 아니지만, 답변 생성 전에 Query Rewrite, 대체 Tool, No Result 처리를 검토해야 한다.

Q. Tool Output이 다른 Context와 충돌하면 어떻게 해야 하는가?

A. Source, Timestamp, 신뢰도를 확인하고 필요하면 추가 검증이나 Review Agent 검토를 수행한다.

---

# 12. Permission and Approval Rules

## 12.1 권한 / 승인 작성 규칙

### [개념]

Permission and Approval은 Tool이 사용 가능한 권한 범위와 실행 전 승인 필요 여부를 판단하는 규칙이다.

Tool Calling은 외부 시스템에 실제 영향을 줄 수 있으므로 권한과 승인 기준이 필수이다.

---

### [핵심]

권한 수준:

- Public Read
- User Data Read
- Sensitive Data Read
- State Change
- Destructive Change
- Deployment / Production Change
- Financial / Legal / High-Risk Action

승인 필요 상황:

- 이메일 전송
- 캘린더 생성 / 수정 / 삭제
- 파일 삭제
- DB 수정 / 삭제
- 결제 / 주문
- 배포 실행
- 권한 변경
- Production 설정 변경
- 민감정보 접근
- 되돌리기 어려운 작업
- 사용자 의도가 불명확한 작업

---

### [실무]

Permission Check Flow:

```text
Tool Call Candidate
→ Tool Risk Classification
→ User Permission Check
→ Approval Requirement Check
→ Execute or Request Approval
```

Approval Request 예시:

```text
승인 필요:
- Production DB Migration 실행

실행 전 확인:
- 대상 DB
- 변경 내용
- Backup 여부
- Rollback 가능 여부
- 예상 영향
```

Read-Only Tool도 사용자 데이터에 접근하면 권한 확인이 필요하다.

---

### [FAQ]

Q. Permission Check는 왜 필요한가?

A. Agent가 권한 없는 데이터에 접근하거나 위험한 상태 변경을 수행하지 않도록 막기 위해 필요하다.

Q. 상태 변경 Tool은 항상 승인받아야 하는가?

A. 위험도와 정책에 따라 다르지만, 되돌리기 어렵거나 사용자에게 직접 영향을 주는 작업은 명시적 승인이 필요하다.

Q. Read-Only Tool은 승인 없이 사용해도 되는가?

A. 공개 정보 조회는 가능하지만 사용자 데이터나 민감정보 조회는 권한 확인이 필요하다.

---

# 13. State Change Tool Rules

## 13.1 상태 변경 Tool 안전 규칙

### [개념]

State Change Tool은 외부 시스템의 상태를 변경하는 도구이다.

예를 들어 이메일 전송, 파일 생성 / 수정 / 삭제, DB 변경, 캘린더 이벤트 생성, 배포 실행 등이 State Change Tool에 해당한다.

---

### [핵심]

State Change Tool 예시:

- send_email
- create_calendar_event
- update_database
- delete_file
- create_file
- deploy_service
- restart_server
- modify_permissions
- create_payment
- update_user_profile
- publish_content

필수 기준:

- 사용자 의도 명확성
- 실행 대상 명확성
- 입력값 검증
- 권한 확인
- 승인 필요 여부 판단
- Idempotency 확인
- Rollback 가능성 확인
- 실행 결과 기록
- 실패 시 복구 계획
- Audit Log 기록

---

### [실무]

State Change Tool 실행 Flow:

```text
User Intent 확인
→ Target Resource 확인
→ Input Validation
→ Permission Check
→ Approval Check
→ Execute
→ Result Validation
→ Audit Log
→ User Confirmation
```

상태 변경 금지 예시:

```text
요청:
"그 파일 지워줘"

문제:
- 어떤 파일인지 불명확
- 삭제 범위 불명확
- 되돌리기 어려움

처리:
- 대상 파일 확인
- 삭제 영향 설명
- 명시적 승인 후 실행
```

---

### [FAQ]

Q. State Change Tool은 무엇인가?

A. 외부 시스템의 상태를 변경하는 도구이다. 이메일 전송, DB 수정, 파일 삭제, 배포 실행 등이 포함된다.

Q. State Change Tool에서 가장 중요한 것은?

A. 사용자 의도, 대상, 권한, 승인, Rollback, 실행 결과 기록이다.

Q. 상태 변경 Tool은 Retry해도 되는가?

A. Idempotency가 보장되지 않으면 무작정 Retry하면 안 된다. 중복 실행 위험이 있기 때문이다.

---

# 14. Idempotency Rules

## 14.1 Idempotency 작성 규칙

### [개념]

Idempotency는 같은 Tool Call을 여러 번 실행해도 결과가 한 번 실행한 것과 동일하게 유지되는 성질이다.

Retry가 필요한 Tool Calling에서는 Idempotency가 매우 중요하다.

---

### [핵심]

Idempotent 가능 작업:

- Read Query
- Search
- Status Check
- Safe Calculation
- Existing Resource 조회
- 동일 Key 기반 Upsert
- Idempotency Key가 있는 요청

Non-Idempotent 위험 작업:

- 이메일 전송
- 결제 생성
- 주문 생성
- 파일 삭제
- DB Insert
- 배포 실행
- 서버 재시작
- 외부 알림 전송

Idempotency 기준:

- idempotencyKey 사용
- 중복 실행 감지
- 실행 전 상태 확인
- 실행 후 결과 확인
- Retry 가능 여부 표시
- Side Effect 기록

---

### [실무]

Idempotency 처리 예시:

```text
Tool:
- send_email

문제:
- Retry 시 같은 이메일이 여러 번 전송될 수 있음

대응:
- messageId 또는 idempotencyKey 생성
- 전송 성공 여부 확인
- 실패 원인에 따라 Retry 제한
- 중복 전송 방지
```

Retry Policy는 Tool별 Idempotency 여부에 따라 달라야 한다.

---

### [FAQ]

Q. Idempotency란?

A. 같은 요청을 여러 번 실행해도 결과가 한 번 실행한 것과 동일하게 유지되는 성질이다.

Q. Idempotency가 중요한 이유는?

A. Retry 과정에서 중복 이메일, 중복 결제, 중복 DB 변경 같은 문제가 발생할 수 있기 때문이다.

Q. 모든 Tool은 Retry해도 되는가?

A. 아니다. Non-Idempotent Tool은 중복 실행 위험이 있으므로 Retry 전에 상태 확인과 승인 기준이 필요하다.

---

# 15. Error Handling Rules

## 15.1 Tool Error Handling 작성 규칙

### [개념]

Tool Error Handling은 Tool 호출 중 발생하는 오류를 분류하고 적절한 복구 전략을 선택하는 과정이다.

Tool Calling Reliability는 오류를 숨기지 않고 구조적으로 처리하는 능력에 의존한다.

---

### [핵심]

Error 유형:

- Schema Error
- Missing Argument
- Invalid Argument
- Permission Error
- Authentication Error
- Authorization Error
- Rate Limit Error
- Timeout Error
- Network Error
- Tool Runtime Error
- Empty Result
- Partial Result
- Conflict Error
- State Change Error
- Unknown Error

Error 처리 기준:

- 재시도 가능 여부
- 사용자 입력 필요 여부
- 권한 문제 여부
- 대체 Tool 가능 여부
- 상태 변경 여부
- Rollback 필요 여부
- Human Review 필요 여부
- 최종 답변에 오류 표시 필요 여부

---

### [실무]

Error Handling 형식:

```json
{
  "status": "failed",
  "errorType": "invalid_argument",
  "errorMessage": "startTime must be before endTime",
  "retryable": true,
  "requiresUserInput": true,
  "nextAction": "request_valid_time_range"
}
```

Error Handling Flow:

```text
Tool Error 발생
→ Error Type 분류
→ Retry 가능 여부 판단
→ Fallback 가능 여부 판단
→ User Input 필요 여부 판단
→ Recovery 또는 Failure Response
```

---

### [FAQ]

Q. Tool Error Handling은 왜 필요한가?

A. 오류 유형에 따라 Retry, Fallback, 사용자 확인, 중단, Rollback 중 다른 처리가 필요하기 때문이다.

Q. Timeout Error는 항상 Retry해야 하는가?

A. 아니다. Tool이 상태 변경 작업이면 중복 실행 위험이 있으므로 먼저 실행 여부를 확인해야 한다.

Q. Empty Result는 오류인가?

A. 상황에 따라 다르다. 검색 결과 없음은 Query Rewrite나 No Result 응답으로 처리할 수 있다.

---

# 16. Retry and Fallback Rules

## 16.1 Retry / Fallback 작성 규칙

### [개념]

Retry는 실패한 Tool Call을 수정된 조건으로 다시 시도하는 것이고, Fallback은 대체 Tool, 대체 Workflow, 사용자 확인, Human Review로 전환하는 것이다.

Retry는 무조건 반복하면 안 된다.

---

### [핵심]

Retry 적합 상황:

- 일시적 네트워크 오류
- Rate Limit 이후 대기 가능
- Timeout이지만 상태 변경 없음
- Schema Error 수정 가능
- Missing Argument 보완 가능
- Query Rewrite 가능
- Read-Only Tool 실패
- Idempotent Tool 실패

Retry 부적합 상황:

- 결제 / 주문 / 이메일 중복 위험
- 파일 삭제
- DB 변경
- 배포 실행
- 권한 부족
- 사용자 의도 불명확
- 위험 작업
- 같은 오류 반복

Fallback 방식:

- 대체 Tool 사용
- Query Rewrite
- 사용자에게 누락 정보 요청
- Human Review
- 부분 결과 제공
- 안전한 실패 응답
- 이전 상태로 Rollback

---

### [실무]

Retry / Fallback Flow:

```text
Tool Call 실패
→ Error Type 분류
→ Idempotency 확인
→ Retry 가능 여부 판단
→ Retry with Modified Input
→ 실패 반복 시 Fallback
→ 결과 보고
```

Retry 기준:

```text
- 동일 입력 반복 금지
- retryCount 제한
- 실패 원인 반영
- 상태 변경 Tool은 중복 실행 방지
- 반복 실패 시 Fallback 전환
```

---

### [FAQ]

Q. Retry는 언제 해야 하는가?

A. 일시적 오류, 수정 가능한 Schema 오류, Read-Only Tool 실패처럼 중복 실행 위험이 낮은 경우 수행한다.

Q. 같은 입력으로 계속 Retry해도 되는가?

A. 안 된다. 실패 원인을 반영해 입력, Query, Tool, Timeout을 수정해야 한다.

Q. Fallback은 언제 필요한가?

A. Retry가 실패하거나 권한 부족, 위험 작업, 사용자 확인 필요, Tool 사용 불가 상황에서 필요하다.

---

# 17. Tool Result Verification Rules

## 17.1 Tool Result 검증 규칙

### [개념]

Tool Result Verification은 Tool Output이 실제로 사용자 요청을 해결하는 데 적합한지, 다른 Context와 충돌하지 않는지, 최종 답변에 사용해도 되는지 확인하는 과정이다.

Tool Result를 그대로 최종 답변으로 사용하면 오류와 Hallucination이 발생할 수 있다.

---

### [핵심]

검증 대상:

- 결과 완전성
- 결과 최신성
- 결과 관련성
- Source 신뢰도
- 오류 포함 여부
- Partial Result 여부
- 다른 Tool Result와 일치 여부
- RAG Context와 일치 여부
- User Request와 일치 여부
- 상태 변경 성공 여부
- Rollback 필요 여부

검증 방식:

- Schema Validation
- Source Check
- Timestamp Check
- Cross-Check
- Consistency Check
- Review Agent Check
- User Confirmation
- Evaluation Tool 사용

---

### [실무]

Verification Flow:

```text
Tool Output 수신
→ Output Schema 확인
→ Error / Empty / Partial 확인
→ Source / Timestamp 확인
→ Context와 충돌 확인
→ 사용 가능 여부 판단
→ Answer Synthesis
```

검증 실패 예시:

```text
Tool Result:
- 검색 결과 없음

잘못된 처리:
- 검색 결과 없이 일반 지식으로 단정 답변

올바른 처리:
- Query Rewrite 또는 No Result 표시
- 필요한 경우 사용자에게 정보 부족 안내
```

---

### [FAQ]

Q. Tool Result Verification은 왜 필요한가?

A. Tool 결과도 오류, 누락, 오래된 정보, 불완전한 결과를 포함할 수 있기 때문이다.

Q. Tool Result와 RAG Context가 충돌하면 어떻게 해야 하는가?

A. Source, Timestamp, 신뢰도를 비교하고 필요하면 추가 검증이나 Review Agent 검토를 수행한다.

Q. 검색 결과가 없으면 답변하면 안 되는가?

A. 근거가 필요한 질문이라면 일반 지식으로 단정하지 말고 재검색하거나 정보 부족을 표시해야 한다.

---

# 18. Tool Call Observability Rules

## 18.1 Tool Call Trace 작성 규칙

### [개념]

Tool Call Observability는 Tool 호출의 입력, 출력, 상태, 오류, 지연, 비용, 권한, 검증 결과를 추적하는 구조이다.

Tool Calling 문제를 분석하려면 어떤 Tool이 왜 호출되었고 어떤 결과를 반환했는지 추적 가능해야 한다.

---

### [핵심]

Tool Call Trace 대상:

- traceId
- workflowId
- taskId
- agentName
- toolName
- toolVersion
- toolType
- toolInput
- toolOutputSummary
- inputValidationResult
- permissionCheckResult
- executionStatus
- outputValidationResult
- latencyMs
- cost
- retryCount
- errorType
- stateChange
- rollbackAvailable
- finalUsage

Metric:

- toolCallSuccessRate
- toolCallErrorRate
- invalidArgumentRate
- permissionDeniedRate
- timeoutRate
- retryRate
- fallbackRate
- toolLatency
- stateChangeFailureRate

---

### [실무]

Tool Call Trace 예시:

```text
traceId: TOOL-001
workflowId: WF-001
agentName: Review Agent
toolName: search_documents
toolType: Read-Only Tool
inputValidationResult: passed
executionStatus: success
outputValidationResult: passed
latencyMs: 180
retryCount: 0
finalUsage: used_for_context
```

상태 변경 Tool Trace에는 추가 정보가 필요하다.

```text
stateChange: true
approvalStatus: approved
rollbackAvailable: true
auditLogId: AUDIT-001
```

---

### [FAQ]

Q. Tool Call Observability는 왜 필요한가?

A. Tool 호출 실패, 잘못된 인자, 권한 오류, 지연, 중복 실행, 상태 변경 문제를 추적하기 위해 필요하다.

Q. Tool Input과 Output을 모두 저장해야 하는가?

A. 원인 분석에 필요한 수준으로 저장하되, 민감정보는 마스킹하거나 저장하지 않아야 한다.

Q. Tool Call Metric은 무엇을 봐야 하는가?

A. 성공률, 오류율, 인자 오류율, Retry 비율, Latency, 상태 변경 실패율을 본다.

---

# 19. Multi-Agent Tool Coordination Rules

## 19.1 Multi-Agent Tool Coordination 작성 규칙

### [개념]

Multi-Agent Tool Coordination은 여러 Agent가 같은 Tool 또는 서로 다른 Tool을 호출할 때 권한, 순서, 중복, 결과 공유, 상태 변경 충돌을 관리하는 규칙이다.

Multi-Agent 환경에서는 Tool Call이 중복되거나 서로 충돌할 수 있다.

---

### [핵심]

Coordination 대상:

- Tool 권한
- Tool 호출 순서
- Shared State 업데이트
- Tool Result 공유
- 중복 호출 방지
- State Change 충돌 방지
- Agent별 Tool Scope
- Tool Call Lock
- Approval Flow
- Audit Log
- Conflict Resolution

Agent별 기준:

- PM Agent: Tool 사용 승인과 Routing
- Specialist Agent: 자신의 Domain Tool 사용
- Review Agent: Tool Result 검증
- DevOps Agent: 배포 / 운영 Tool 관리
- Backend Agent: DB / API Tool 사용
- AI/ML Agent: Evaluation / Retrieval Tool 사용

---

### [실무]

Multi-Agent Tool Flow:

```text
PM Agent
→ Tool Need 판단
→ Specialist Agent에 Tool 권한 부여
→ Specialist Agent Tool Call
→ Tool Result Shared State 저장
→ Review Agent 검증
→ PM Agent 최종 결정
```

중복 호출 방지 예시:

```text
문제:
Backend Agent와 DevOps Agent가 동시에 배포 Tool 호출

해결:
- Deployment Tool은 DevOps Agent만 실행
- PM Agent 승인 필요
- Tool Call Lock 적용
- 실행 결과 Shared State에 기록
```

---

### [FAQ]

Q. Multi-Agent Tool Coordination은 왜 필요한가?

A. 여러 Agent가 같은 Tool을 중복 호출하거나 상태 변경을 충돌시키는 것을 방지하기 위해 필요하다.

Q. 모든 Agent가 모든 Tool을 사용할 수 있어야 하는가?

A. 아니다. Agent Role에 맞는 Tool만 최소 권한으로 허용해야 한다.

Q. Tool Result는 어떻게 공유해야 하는가?

A. Shared State에 요약과 검증 결과를 저장하고, 필요한 Agent만 접근하게 한다.

---

# 20. Security and Safety Rules

## 20.1 Tool Calling Security / Safety 규칙

### [개념]

Tool Calling Security / Safety는 Tool이 외부 시스템, 사용자 데이터, 파일, DB, API, 배포 환경에 접근할 때 보안과 안전성을 보장하기 위한 규칙이다.

Tool Calling은 LLM 출력보다 위험할 수 있다.

LLM이 잘못된 Tool Call을 생성하면 실제 시스템 변경이 발생할 수 있기 때문이다.

---

### [핵심]

보안 위험:

- Prompt Injection
- Tool Injection
- SQL Injection
- Command Injection
- Path Traversal
- SSRF
- Secret Leakage
- Unauthorized Access
- Data Exfiltration
- Privilege Escalation
- Unsafe State Change
- Destructive Action
- Supply Chain Risk

안전 기준:

- Least Privilege
- Allowlist 기반 Tool 사용
- Tool Input Validation
- Tool Output Validation
- Sensitive Data Masking
- Approval Flow
- Audit Logging
- Rate Limit
- Timeout
- Sandbox Execution
- Human Review
- Rollback Plan

---

### [실무]

Security Checklist:

```md
### [Checklist]

- Tool 권한이 최소 권한인가?
- Tool Input이 검증되었는가?
- 외부 URL / 파일 경로가 안전한가?
- SQL / Shell 명령이 안전하게 제한되었는가?
- Secret이 Tool Input / Output에 노출되지 않았는가?
- 상태 변경 Tool은 승인되었는가?
- Audit Log가 남는가?
- 실패 시 Rollback 가능한가?
```

Tool Calling에서는 사용자 입력과 LLM 생성 인자를 모두 신뢰하지 않는다.

Prompt Injection에 의해 Tool Argument가 조작될 수 있으므로 Tool Layer에서 별도 검증해야 한다.

---

### [FAQ]

Q. Tool Calling에서 가장 큰 보안 위험은?

A. Prompt Injection, 권한 없는 접근, 위험한 상태 변경, Secret 노출, SQL / Command Injection이다.

Q. LLM이 생성한 Tool Argument는 신뢰해도 되는가?

A. 안 된다. 반드시 별도 Validation과 Permission Check를 수행해야 한다.

Q. Least Privilege가 중요한 이유는?

A. Tool이 필요한 최소 권한만 가져야 오류나 공격 발생 시 피해 범위를 줄일 수 있기 때문이다.

---

# 21. Evaluation Rules

## 21.1 Tool Calling Reliability Evaluation 작성 규칙

### [개념]

Tool Calling Reliability Evaluation은 Agent가 올바른 도구를 선택하고, 올바른 인자를 생성하고, Tool Result를 검증하고, 오류를 안전하게 처리하는지 평가하는 기준이다.

Tool Calling 평가는 단순 실행 성공 여부만 보면 안 된다.

---

### [핵심]

평가 항목:

- Tool Selection Accuracy
- Function Argument Accuracy
- Schema Compliance
- Input Validation Pass Rate
- Output Validation Quality
- Permission Compliance
- State Change Safety
- Idempotency Handling
- Retry Quality
- Fallback Quality
- Error Classification Accuracy
- Tool Result Groundedness
- Tool Call Latency
- Tool Call Cost
- Security Compliance
- User Goal Completion

평가 Query 유형:

- Read-Only Query
- Calculation Query
- Search Query
- Missing Argument Query
- Invalid Argument Query
- Permission Required Query
- State Change Query
- Destructive Action Query
- Tool Failure Query
- No Tool Needed Query

---

### [실무]

Evaluation Checklist:

```md
### [Checklist]

- 필요한 상황에서만 Tool을 호출했는가?
- 올바른 Tool을 선택했는가?
- Function Argument가 Schema를 만족하는가?
- 누락된 인자를 추측하지 않았는가?
- Tool 호출 전 권한을 확인했는가?
- Tool Result를 검증했는가?
- 오류 유형을 올바르게 분류했는가?
- Retry가 안전하게 수행되었는가?
- 상태 변경 Tool에서 승인 기준을 지켰는가?
- Tool 호출이 필요 없는 상황에서 호출하지 않았는가?
```

Tool Calling Evaluation은 Unit Test, Scenario Test, Failure Test, Safety Test를 함께 사용한다.

---

### [FAQ]

Q. Tool Calling Evaluation은 무엇을 평가하는가?

A. Tool 선택, 인자 정확성, Schema 준수, 권한 확인, 결과 검증, Retry, Fallback, 상태 변경 안전성을 평가한다.

Q. Tool 실행 성공이면 평가도 성공인가?

A. 아니다. 잘못된 Tool을 성공적으로 실행했거나 결과를 잘못 사용했을 수 있다.

Q. No Tool Needed Query도 평가해야 하는가?

A. 필요하다. 도구가 필요 없는 상황에서 불필요한 Tool Call을 하지 않는지도 Reliability의 일부이다.

---

# 22. Troubleshooting Rules

## 22.1 Tool Calling 장애 대응 작성 규칙

### [개념]

Tool Calling Troubleshooting 문서는 도구 선택 오류, 인자 오류, Schema 불일치, 권한 오류, 실행 실패, Retry 실패, 상태 변경 오류를 해결하기 위한 규칙이다.

---

### [핵심]

자주 발생하는 문제:

- 잘못된 Tool 선택
- Tool이 필요 없는데 호출
- Tool이 필요한데 호출하지 않음
- Function Argument 누락
- Argument 타입 오류
- enum 값 오류
- JSON Parsing 실패
- Schema 과도하게 복잡함
- Tool Description 모호함
- Permission Error
- Rate Limit Error
- Timeout Error
- Empty Result
- Tool Result 미검증
- Non-Idempotent Tool 중복 실행
- State Change 승인 누락
- Prompt Injection으로 Tool Argument 오염
- Tool Call Trace 누락

---

### [실무]

Troubleshooting 형식:

```md
문제:
Function Calling에서 잘못된 인자 이름이 반복 생성됨

원인:

- Tool Schema의 fieldName이 Domain 용어와 다름
- Tool description이 모호함
- 예시가 부족함
- 필수 필드와 선택 필드 구분이 약함

해결:

- fieldName을 명확하게 변경
- description을 짧고 구체적으로 수정
- JSON Schema validation 추가
- 실패 시 expected schema를 포함해 Retry
```

문제 / 원인 / 해결 형식을 기본으로 작성한다.

---

### [FAQ]

Q. Tool Calling에서 가장 흔한 실패는?

A. 잘못된 Tool 선택, 인자 누락, Schema 불일치, 권한 오류, Tool Result 미검증, 상태 변경 중복 실행이다.

Q. JSON Parsing 실패가 자주 발생하면 어떻게 해야 하는가?

A. Schema를 단순화하고, 필수 필드를 줄이고, Validation과 Retry 전략을 추가해야 한다.

Q. Tool Result가 비어 있으면 어떻게 해야 하는가?

A. Query Rewrite, 대체 Tool, No Result 처리, 사용자 추가 정보 요청 중 하나를 선택한다.

---

# 23. Common Mistakes

## 23.1 자주 발생하는 작성 오류

### [개념]

Tool Calling & Function Calling Reliability 문서는 “LLM이 함수를 호출하는 방법”만 설명하는 문서가 아니다.

Agent가 도구 호출을 안전하게 선택, 검증, 실행, 복구, 추적할 수 있도록 작성해야 한다.

---

### [핵심]

금지 또는 주의:

- Tool Schema 없이 Tool 설명만 작성
- Tool description 모호함
- Function Argument 검증 누락
- Input Validation 누락
- Output Validation 누락
- Permission Check 누락
- State Change Tool 승인 기준 누락
- Idempotency 고려 누락
- Retry를 무조건 허용
- Tool Result를 그대로 신뢰
- Error Type 분류 누락
- Fallback 기준 누락
- Tool Call Trace 누락
- Security Guardrails 누락
- Multi-Agent Tool Coordination 누락
- Evaluation Checklist 누락
- 특정 API 문서 복붙 중심 작성
- 장문 이론 설명 중심 작성
- Retrieval Queries 누락

---

### [실무]

나쁜 문서 예시:

```text
Tool Calling은 LLM이 필요한 함수를 호출하는 기능이다.
함수 이름과 인자를 잘 만들면 된다.
```

좋은 문서 예시:

```text
Tool Calling Reliability는 Agent가 올바른 Tool을 선택하고, Schema에 맞는 인자를 생성하고, Input / Output을 검증하고, 권한을 확인하고, 실패 시 Retry / Fallback을 안전하게 수행하는 구조이다.

Flow:
Tool Need Check
→ Tool Selection
→ Argument Generation
→ Input Validation
→ Permission Check
→ Tool Execution
→ Output Validation
→ State Update
→ Observability
```

---

### [FAQ]

Q. Tool Calling 문서에서 가장 피해야 할 것은?

A. Tool Schema, Argument Validation, Permission, Error Handling, Observability 없이 함수 호출 예시만 작성하는 것이다.

Q. Tool Result를 그대로 답변에 쓰면 안 되는 이유는?

A. Tool Result도 오류, 누락, 오래된 정보, 권한 문제, 포맷 문제를 포함할 수 있기 때문이다.

Q. Retry를 무조건 허용하면 안 되는 이유는?

A. 이메일 전송, 결제, DB 변경 같은 Non-Idempotent Tool은 중복 실행 위험이 있기 때문이다.

---

# 24. Document Split Rules

## 24.1 Tool Calling & Function Calling Reliability 문서 분할 기준

### [개념]

Tool Calling & Function Calling Reliability는 Tool Schema, Tool Selection, Validation, Permission, State Change, Retry, Security, Evaluation 범위가 넓기 때문에 Part 단위로 분리한다.

각 Part는 독립 검색 가능해야 하며, 하나의 Part는 하나의 핵심 주제를 다룬다.

---

### [핵심]

권장 문서 분할:

```text
Tool_Calling_Function_Calling_Reliability_Part01_Core.md
Tool_Calling_Function_Calling_Reliability_Part02_Tool_Type_Selection.md
Tool_Calling_Function_Calling_Reliability_Part03_Tool_Schema_Function_Schema.md
Tool_Calling_Function_Calling_Reliability_Part04_Argument_Input_Output_Validation.md
Tool_Calling_Function_Calling_Reliability_Part05_Permission_State_Change_Idempotency.md
Tool_Calling_Function_Calling_Reliability_Part06_Error_Retry_Fallback.md
Tool_Calling_Function_Calling_Reliability_Part07_Observability_Multi_Agent_Coordination.md
Tool_Calling_Function_Calling_Reliability_Part08_Security_Evaluation_Troubleshooting.md
```

분할 기준:

- 하나의 Part는 하나의 핵심 주제
- Tool Type과 Selection은 함께 작성 가능
- Tool Schema와 Function Schema는 함께 작성 권장
- Argument / Input / Output Validation은 함께 작성 가능
- Permission / State Change / Idempotency는 연결 문서로 작성
- Error / Retry / Fallback은 함께 작성 권장
- Observability와 Multi-Agent Coordination은 함께 작성 가능
- Security와 Evaluation은 반드시 포함
- Troubleshooting은 문제 / 원인 / 해결 형식
- 각 Part는 FAQ 포함
- 각 Part는 Retrieval Queries 포함

---

### [실무]

Tool Calling & Function Calling Reliability 문서 Set은 AI Expert Level과 AgentOps / Backend Agent 구현에서 사용한다.

AI/ML Agent는 Tool Workflow와 Evaluation 기준을 참조하고, Backend Agent는 Tool Schema와 Validation 구현을 참조한다.

특정 구현 도구는 별도 문서로 분리한다.

예:

```text
Tool_Calling_Function_Calling_Reliability_Domain_Rules.md
OpenAI_Function_Calling_Part.md
LangGraph_Tool_Node_Part.md
Agent_Tool_Schema_Part.md
Tool_Security_Guardrails_Part.md
```

---

### [FAQ]

Q. Tool Calling & Function Calling Reliability 문서는 몇 개 Part로 나누는 것이 좋은가?

A. 7~8개 Part를 권장한다. Core, Tool Type, Schema, Validation, Permission, Error/Retry, Observability, Security/Evaluation으로 분리한다.

Q. 특정 Function Calling API 문서와 합쳐도 되는가?

A. 권장하지 않는다. Domain Rules는 구조와 신뢰성 기준 중심이고, 특정 API 구현은 별도 문서로 분리하는 것이 좋다.

Q. 각 Part에도 Retrieval Queries가 필요한가?

A. 필요하다. 각 문서가 독립 검색될 수 있어야 한다.

---

# 25. Agent Usage Rules

## 25.1 Agent별 사용 기준

### [개념]

Tool Calling & Function Calling Reliability Domain Rules는 여러 Agent가 도구 호출을 동일한 기준으로 설계, 실행, 검증, 복구하도록 돕는다.

각 Agent는 자신의 역할에 맞는 Tool Calling Chunk를 우선 검색한다.

---

### [핵심]

PM Agent:

- Tool Calling 필요 여부 판단
- Tool 위험도 판단
- 승인 필요 여부 판단
- Multi-Agent Tool Routing
- 최종 실행 결정

AI/ML Agent:

- Tool Selection 전략 설계
- Function Schema 설계
- Tool Calling Evaluation 설계
- Agent Tool Workflow 설계
- Retry / Fallback 기준 설계

Backend Agent:

- Tool Schema 구현
- Function Calling Handler 구현
- Input / Output Validation 구현
- Permission Check 구현
- Tool Result 저장 구조 구현

DevOps Agent:

- Deployment Tool 관리
- Monitoring Tool 연동
- Tool Timeout / Rate Limit 운영
- Tool Call Observability 구성
- Rollback 지원

Review Agent:

- Tool Result 검증
- 권한 / 승인 기준 검토
- State Change Safety 검토
- Tool Call Hallucination 검토
- Security Guardrails 검토

Architecture Review Agent:

- Tool Architecture 검토
- Tool Boundary 검토
- Multi-Agent Tool Coordination 검토
- 확장성 / 보안성 검토

---

### [실무]

Agent별 검색 우선순위:

```text
PM Agent
→ Tool Selection / Permission / Approval / State Change Risk

AI/ML Agent
→ Tool Workflow / Function Schema / Evaluation / Retry Fallback

Backend Agent
→ Tool Schema / Validation / Handler / Output Contract

DevOps Agent
→ Tool Observability / Timeout / Rate Limit / Deployment Safety

Review Agent
→ Output Validation / Security / State Change / Common Mistakes

Architecture Review Agent
→ Tool Boundary / Multi-Agent Coordination / Safety Architecture
```

Tool Calling은 AI/ML Agent 단독 영역이 아니다.

Backend Agent는 실행 구조와 Validation을 구현하고, DevOps Agent는 운영 안정성을 관리하며, Review Agent는 Tool Result와 위험 작업을 검증한다.

---

### [FAQ]

Q. Tool Calling & Function Calling Reliability Domain Rules는 어떤 Agent가 사용하는가?

A. PM Agent, AI/ML Agent, Backend Agent, DevOps Agent, Review Agent, Architecture Review Agent가 역할별로 사용한다.

Q. Backend Agent는 Tool Calling에서 무엇을 구현해야 하는가?

A. Tool Schema, Function Handler, Input / Output Validation, Permission Check, Error Handling을 구현해야 한다.

Q. Review Agent는 무엇을 검토해야 하는가?

A. Tool 선택 적절성, Tool Result 검증, 권한 / 승인 기준, 상태 변경 안전성, Security Guardrails를 검토해야 한다.

---

# 26. Final Goal

## 26.1 최종 목표

### [개념]

Tool Calling & Function Calling Reliability Domain Rules의 최종 목표는 Agent가 외부 도구와 함수를 정확하고 안전하게 호출하고, 결과를 검증하고, 실패를 복구하며, 상태 변경 작업을 신뢰성 있게 수행할 수 있도록 문서 제작 기준을 제공하는 것이다.

---

### [핵심]

최종 목표:

- Tool Calling 개념 검색 가능
- Function Calling 개념 검색 가능
- Tool Type 분류 가능
- Tool Selection 가능
- Tool Schema 설계 가능
- Function Schema 설계 가능
- Argument Validation 가능
- Input Validation 가능
- Output Validation 가능
- Permission Check 가능
- State Change Tool 안전 처리 가능
- Idempotency 판단 가능
- Error Handling 가능
- Retry / Fallback 가능
- Tool Result Verification 가능
- Tool Call Observability 가능
- Multi-Agent Tool Coordination 가능
- Security / Safety Guardrails 적용 가능
- Evaluation 가능
- Troubleshooting 가능

---

### [실무]

Tool Calling & Function Calling Reliability RAG Doc Set은 다음 작업을 지원해야 한다.

```text
User Request
→ Tool Need Check
→ Tool Selection
→ Tool Risk Classification
→ Function Argument Generation
→ Input Validation
→ Permission / Approval Check
→ Tool Execution
→ Output Validation
→ Tool Result Verification
→ State Update
→ Observability
→ Retry / Fallback if needed
```

문서 품질은 Agent가 도구를 잘못 선택하거나 위험하게 실행하지 않고, 검증 가능한 Tool Result를 기반으로 안정적으로 작업을 완료할 수 있는지로 결정된다.

---

### [FAQ]

Q. Tool Calling & Function Calling Reliability Domain Rules의 최종 목적은?

A. Agent가 도구와 함수를 정확하고 안전하게 호출하고, 결과를 검증하고, 실패를 복구할 수 있도록 문서 제작 기준을 제공하는 것이다.

Q. 이 문서는 사람 학습용인가?

A. 아니다. AI Agent Retrieval과 Tool Calling 운영 품질을 높이기 위한 문서이다.

Q. Tool Calling Reliability 문서 품질은 무엇으로 판단하는가?

A. Agent가 Tool 선택, Schema, Validation, Permission, Error Handling, Observability를 누락 없이 적용할 수 있는지로 판단한다.

---

# Retrieval Queries

### [FAQ]

Q. Tool Calling이란?
A. LLM이나 Agent가 외부 도구, API, 함수, 검색기, DB, 코드 실행기 등을 호출해 정보를 얻거나 작업을 수행하는 구조이다.

Q. Function Calling이란?
A. 정해진 Function Schema에 따라 모델이 함수 이름과 인자를 생성하고 시스템이 해당 함수를 실행하는 방식이다.

Q. Tool Calling과 Function Calling의 차이는?
A. Function Calling은 Schema 기반 함수 호출이고, Tool Calling은 검색, 파일, API, DB, 코드 실행, 상태 변경 도구 호출까지 포함하는 더 넓은 개념이다.

Q. Tool Calling Reliability란?
A. 도구 선택, 인자 생성, 검증, 실행, 결과 확인, 오류 복구가 안정적으로 이루어지는 정도이다.

Q. Tool Type을 나누는 이유는?
A. 도구 유형에 따라 권한, 승인, 검증, Retry, Rollback 기준이 다르기 때문이다.

Q. Read-Only Tool이란?
A. 검색, 조회, 계산처럼 외부 상태를 변경하지 않는 도구이다.

Q. State Change Tool이란?
A. 이메일 전송, DB 수정, 파일 삭제, 캘린더 생성, 배포 실행처럼 외부 상태를 변경하는 도구이다.

Q. Destructive Tool이란?
A. 파일 삭제, DB 삭제, 권한 변경, 배포 실행처럼 되돌리기 어렵거나 위험한 도구이다.

Q. Tool Selection이란?
A. 현재 작업을 해결하기 위해 어떤 도구를 호출할지 결정하는 과정이다.

Q. Tool Schema란?
A. Tool의 이름, 설명, 입력 인자, 출력 형식, 제약 조건, 오류 조건을 정의하는 구조이다.

Q. Function Argument Validation이란?
A. 모델이 생성한 함수 인자가 타입, 필수값, enum, 범위, 형식, 권한 조건을 만족하는지 검증하는 과정이다.

Q. Structured Output이란?
A. LLM이 자유 텍스트가 아니라 JSON, Function Argument, Agent Output Contract처럼 정해진 구조로 출력하는 방식이다.

Q. Input Validation은 왜 필요한가?
A. LLM이 생성한 입력이 잘못되거나 위험할 수 있으므로 Tool 실행 전 검증해야 한다.

Q. Output Validation은 왜 필요한가?
A. Tool이 성공해도 결과가 비어 있거나 오래되었거나 부분 결과일 수 있기 때문이다.

Q. Permission Check는 왜 필요한가?
A. Agent가 권한 없는 데이터에 접근하거나 위험한 상태 변경을 수행하지 않도록 막기 위해 필요하다.

Q. 상태 변경 Tool은 언제 승인이 필요한가?
A. 이메일 전송, 파일 삭제, DB 수정, 배포 실행, 결제 처리처럼 사용자에게 직접 영향을 주거나 되돌리기 어려운 작업에서 필요하다.

Q. Idempotency란?
A. 같은 요청을 여러 번 실행해도 결과가 한 번 실행한 것과 동일하게 유지되는 성질이다.

Q. Non-Idempotent Tool은 왜 주의해야 하는가?
A. Retry 과정에서 중복 이메일, 중복 결제, 중복 DB 변경 같은 문제가 발생할 수 있기 때문이다.

Q. Tool Error Handling은 무엇인가?
A. Tool 호출 중 발생하는 오류를 유형별로 분류하고 Retry, Fallback, 사용자 확인, 중단, Rollback을 선택하는 과정이다.

Q. Retry는 언제 가능한가?
A. 일시적 오류, 수정 가능한 Schema 오류, Read-Only Tool 실패처럼 중복 실행 위험이 낮은 경우 가능하다.

Q. Fallback은 언제 필요한가?
A. Retry가 실패하거나 권한 부족, 위험 작업, 사용자 확인 필요, Tool 사용 불가 상황에서 필요하다.

Q. Tool Result Verification이란?
A. Tool Output이 사용자 요청을 해결하는 데 적합하고 다른 Context와 충돌하지 않는지 확인하는 과정이다.

Q. Tool Call Observability란?
A. Tool 호출의 입력, 출력, 상태, 오류, 지연, 비용, 권한, 검증 결과를 추적하는 구조이다.

Q. Multi-Agent Tool Coordination이란?
A. 여러 Agent가 도구를 호출할 때 권한, 순서, 중복, 결과 공유, 상태 변경 충돌을 관리하는 규칙이다.

Q. Tool Calling에서 가장 큰 보안 위험은?
A. Prompt Injection, 권한 없는 접근, Secret 노출, SQL / Command Injection, 위험한 상태 변경이다.

Q. Tool Calling Evaluation은 무엇을 평가하는가?
A. Tool 선택, 인자 정확성, Schema 준수, 권한 확인, 결과 검증, Retry, Fallback, 상태 변경 안전성을 평가한다.

Q. Tool Calling에서 흔한 실패는?
A. 잘못된 Tool 선택, 인자 누락, Schema 불일치, 권한 오류, Tool Result 미검증, 상태 변경 중복 실행이다.

Q. Tool Calling 문서 분할은 어떻게 하는가?
A. Core, Tool Type, Schema, Validation, Permission, Error/Retry, Observability, Security/Evaluation으로 분리한다.

Q. Tool Calling 문서에서 피해야 할 것은?
A. Tool Schema, Argument Validation, Permission, Error Handling, Observability 없이 함수 호출 예시만 작성하는 것이다.

Q. Tool Calling & Function Calling Reliability Domain Rules는 어떤 Agent가 사용하는가?
A. PM Agent, AI/ML Agent, Backend Agent, DevOps Agent, Review Agent, Architecture Review Agent가 역할별로 사용한다.
