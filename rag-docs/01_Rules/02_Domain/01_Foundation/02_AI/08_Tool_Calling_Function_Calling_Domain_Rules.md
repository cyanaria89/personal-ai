# Tool Calling & Function Calling Domain Rules

---

# 1. Domain Purpose

Tool Calling & Function Calling Domain 문서는 AI Agent / Backend Agent / Review Agent용 RAG 문서 제작 규칙이다.

목적:

- LLM Tool Calling 기본 개념 이해
- Function Calling 구조 설계 지원
- Agent가 외부 도구를 안전하게 호출하는 기준 제공
- Tool Schema / Arguments / Result 구조 정의
- Tool Input Validation 기준 제공
- Tool Execution / Error Handling 기준 제공
- RAG Search Tool / File Tool / API Tool 설계 지원
- Multi-Agent Workflow에서 Tool 사용 기준 제공

우선순위:

1. Tool Calling Concept
2. Tool Schema Design
3. Input Validation
4. Safe Execution
5. Structured Result
6. Error Handling
7. Agent Workflow Integration

---

# 2. Scope

포함 범위:

- Tool Calling Core
- Function Calling Core
- Tool Definition
- Function Schema
- JSON Schema
- Tool Arguments
- Tool Choice
- Tool Execution
- Tool Result
- Tool Message
- Input Validation
- Output Validation
- Error Handling
- Retry
- Idempotency
- Safe Tool Execution
- Human Confirmation
- RAG Search Tool
- File Tool
- API Tool
- Database Tool
- Code Execution Tool
- Agent Tool Routing
- Multi-Agent Tool Use
- Tool Observability

제외 범위:

- LangGraph 상세 구현
- MCP Protocol 심화
- OS 보안 샌드박스 심화
- Kubernetes Operator 구현
- Production 권한 관리 시스템 심화
- Fine-Tuning 기반 Tool Use 학습
- 대규모 Agent Platform 운영 상세

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

# 4. Tool Calling Core Rules

Tool Calling 문서는 LLM이 외부 기능을 선택하고 실행하는 구조 중심으로 작성한다.

반드시 포함:

- LLM은 직접 모든 작업을 수행하지 않음
- 필요한 경우 외부 Tool을 호출할 수 있음
- Tool은 검색, 계산, 파일 처리, API 호출, 코드 실행 등을 담당
- LLM은 Tool 호출에 필요한 arguments를 생성
- 실제 Tool 실행은 시스템 또는 Agent Runtime이 담당
- Tool 결과는 다시 LLM Context로 전달될 수 있음

기본 Flow:

```text
User Request
→ LLM Determines Tool Need
→ Generate Tool Arguments
→ Validate Arguments
→ Execute Tool
→ Return Tool Result
→ LLM Generates Final Answer
```

금지:

- Tool Arguments를 무조건 신뢰하는 설명
- 위험 작업을 승인 없이 실행하는 구조
- Tool 실패를 무시하고 답변하는 방식
- Tool Result 검증 없이 최종 답변 생성
- Tool Calling을 단순 함수 실행 문법으로만 설명

---

# 5. Function Calling vs Tool Calling Rules

Function Calling과 Tool Calling의 관계를 설명한다.

비교:

| 구분 | Function Calling            | Tool Calling                         |
| ---- | --------------------------- | ------------------------------------ |
| 의미 | 함수 호출 구조              | 외부 도구 호출 전체 구조             |
| 중심 | Function Schema / Arguments | Tool 선택, 실행, 결과 처리           |
| 범위 | 좁음                        | 넓음                                 |
| 예시 | search_documents(query)     | 검색, 파일 읽기, API 호출, 코드 실행 |

반드시 설명:

- Function Calling은 Tool Calling의 한 형태로 볼 수 있음
- Tool Calling은 함수뿐 아니라 검색, 파일, API, DB, 실행 환경을 포함할 수 있음
- Agent 시스템에서는 Tool Calling이라는 용어가 더 넓게 사용됨

주의:

- Provider마다 용어와 API 구조가 다를 수 있음
- 같은 개념이라도 function, tool, action 등으로 표현될 수 있음

---

# 6. Tool Definition Rules

Tool Definition은 LLM이 Tool을 이해하고 선택하기 위한 설명이다.

필수 포함:

- Tool Name
- Description
- Parameters
- Required Fields
- Return Type
- Side Effect
- Permission Level
- Failure Case

예시:

```json
{
  "name": "search_rag_documents",
  "description": "Search relevant RAG documents for a user query.",
  "parameters": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "Search query"
      },
      "topK": {
        "type": "integer",
        "description": "Number of documents to retrieve"
      }
    },
    "required": ["query"]
  }
}
```

반드시 설명:

- Tool Name은 짧고 명확해야 함
- Description은 Tool이 언제 필요한지 설명해야 함
- Parameter 설명은 모델이 올바른 arguments를 만들게 도움
- Side Effect가 있는 Tool은 명확히 표시해야 함

주의:

- Tool 설명이 모호하면 잘못 선택될 수 있음
- 너무 많은 Tool은 선택 품질을 낮출 수 있음
- 이름이 비슷한 Tool이 많으면 혼동 가능

---

# 7. JSON Schema Rules

Tool Arguments는 JSON Schema 기반으로 정의하는 것이 좋다.

필수 포함:

- type
- properties
- required
- enum
- array
- object
- description
- default
- nullable

예시:

```json
{
  "type": "object",
  "properties": {
    "filePath": {
      "type": "string"
    },
    "mode": {
      "type": "string",
      "enum": ["read", "write", "append"]
    }
  },
  "required": ["filePath", "mode"]
}
```

반드시 설명:

- JSON Schema는 Tool 입력 구조를 제한
- Required Field를 명확히 지정
- enum은 허용 값을 제한하는 데 유용
- 복잡한 Schema는 모델 출력 실패 가능성을 높일 수 있음

주의:

- Schema가 너무 느슨하면 잘못된 입력 발생
- Schema가 너무 복잡하면 모델이 형식을 자주 틀림
- Schema 검증은 실제 실행 전에 반드시 수행

---

# 8. Tool Arguments Rules

Tool Arguments는 실행 전 검증해야 한다.

필수 포함:

- Required Field Check
- Type Check
- Range Check
- Enum Check
- Path Validation
- Permission Check
- Sanitization

기본 Flow:

```text
Generated Arguments
→ Schema Validation
→ Business Validation
→ Permission Check
→ Execute Tool
```

반드시 설명:

- LLM이 생성한 arguments는 신뢰하면 안 됨
- Schema 검증과 비즈니스 검증을 모두 수행
- 파일 경로, URL, SQL, Shell Command는 특히 주의
- 위험 작업은 사용자 확인 필요

주의:

- 잘못된 인자로 파일 삭제 / 덮어쓰기 위험
- Path Traversal 공격 주의
- SQL Injection / Command Injection 주의
- 빈 문자열 / null 처리 필요

---

# 9. Tool Choice Rules

Tool Choice는 어떤 도구를 사용할지 결정하는 과정이다.

필수 포함:

- Auto Tool Choice
- Forced Tool Choice
- No Tool
- Tool Routing
- Tool Selection Criteria
- Tool Priority

판단 기준:

```text
질문이 문서 검색 필요 → RAG Search Tool
파일 내용 확인 필요 → File Read Tool
현재 정보 필요 → Web/API Tool
계산 필요 → Calculator Tool
코드 실행 필요 → Code Execution Tool
위험 작업 필요 → Human Confirmation
```

반드시 설명:

- 모든 요청에 Tool이 필요한 것은 아님
- Tool이 필요 없는 일반 답변은 직접 답변 가능
- Tool 사용 비용과 위험을 고려
- Agent별로 사용할 수 있는 Tool 범위를 제한 가능

주의:

- 불필요한 Tool 호출은 Latency 증가
- Tool 없이 답하면 안 되는 최신 정보 요청 주의
- 위험 Tool은 자동 선택 제한

---

# 10. Tool Execution Rules

Tool Execution은 안전하고 추적 가능해야 한다.

필수 포함:

- Precondition Check
- Permission Check
- Execution
- Timeout
- Retry
- Result Capture
- Error Capture
- Audit Log

기본 Flow:

```text
Validated Tool Call
→ Check Permission
→ Execute with Timeout
→ Capture Result
→ Validate Output
→ Return Tool Message
```

반드시 설명:

- Tool 실행 전 조건 확인
- Timeout 설정 필요
- 실행 결과와 오류를 구조화
- Side Effect가 있는 작업은 로그 기록
- 실패 시 안전한 에러 결과 반환

주의:

- 무기한 실행 금지
- 위험 작업 자동 실행 금지
- 실패한 Tool 결과를 성공처럼 처리 금지
- 민감정보 로그 출력 금지

---

# 11. Tool Result Rules

Tool Result는 후속 LLM 처리가 가능하도록 구조화한다.

필수 포함:

- status
- data
- error
- message
- metadata
- source
- executionTime
- confidence

예시:

```json
{
  "status": "success",
  "data": {
    "documents": []
  },
  "metadata": {
    "tool": "search_rag_documents",
    "executionTimeMs": 120
  }
}
```

실패 예시:

```json
{
  "status": "error",
  "error": {
    "code": "FILE_NOT_FOUND",
    "message": "The requested file does not exist."
  }
}
```

반드시 설명:

- Tool Result는 성공/실패를 명확히 구분
- 실패 결과도 LLM에게 전달 가능
- data와 error를 분리
- Source / Metadata는 답변 근거와 디버깅에 도움

주의:

- Raw Exception을 그대로 노출하지 말 것
- Secret / Token을 결과에 포함하지 말 것
- Tool Result가 너무 크면 요약 또는 제한 필요

---

# 12. Tool Message Rules

Tool Message는 Tool 실행 결과를 LLM Context에 전달하는 메시지이다.

필수 포함:

- Tool Call ID
- Tool Name
- Tool Result
- Structured Data
- Error Result
- Source Reference

기본 Flow:

```text
LLM Tool Call
→ Runtime Executes Tool
→ Tool Message
→ LLM Final Response
```

반드시 설명:

- Tool Message는 LLM이 후속 답변을 생성하는 근거
- Tool 실패도 Tool Message로 전달할 수 있음
- Tool Message는 가능한 구조화된 형태가 좋음
- 큰 결과는 요약 또는 필요한 부분만 전달

주의:

- Tool 결과를 왜곡해서 전달하지 말 것
- 너무 긴 Tool Result는 Context Window를 낭비
- 민감정보 제거 후 전달

---

# 13. Safe Tool Execution Rules

Tool Calling 문서는 안전 실행 기준을 반드시 포함한다.

위험 Tool 예시:

- File Write Tool
- File Delete Tool
- Shell Command Tool
- Database Write Tool
- Payment Tool
- Email Send Tool
- Deployment Tool
- Account Modification Tool

안전 기준:

```text
Low Risk
→ Auto Execute

Medium Risk
→ Validate + Log

High Risk
→ Require Human Confirmation
```

반드시 설명:

- Side Effect가 큰 작업은 사용자 확인 필요
- 삭제, 결제, 배포, 이메일 발송은 자동 실행 금지 또는 제한
- dry-run 모드 제공 가능
- 권한 범위를 최소화해야 함

주의:

- LLM이 생성한 명령을 그대로 실행 금지
- 파일 경로, shell command, SQL은 검증 필수
- 복구 불가능한 작업은 승인 필요
- Tool Permission을 Agent별로 제한

---

# 14. Human Confirmation Rules

Human Confirmation은 위험 작업 전에 사용자 승인을 받는 절차이다.

필수 포함:

- Approval Required
- Action Summary
- Risk Explanation
- Preview
- Confirm / Cancel
- Dry Run
- Undo 가능 여부

예시:

```text
다음 작업은 파일을 수정합니다.

대상:
- docs/rag.md

변경:
- Retrieval Queries 추가

실행할까요?
```

반드시 설명:

- 위험 작업은 실행 전 요약 제공
- 사용자가 승인하기 전 실행하지 않음
- 변경 대상과 영향 범위를 명확히 표시
- 되돌릴 수 없는 작업은 특히 주의

주의:

- 애매한 동의로 실행하지 말 것
- 승인 범위를 넘어서는 추가 작업 금지
- 승인 후에도 검증은 필요

---

# 15. Idempotency Rules

Idempotency는 같은 Tool 호출을 여러 번 실행해도 결과가 안전한지 판단하는 기준이다.

필수 포함:

- Idempotent Operation
- Non-Idempotent Operation
- Duplicate Execution
- Retry Safety
- Request ID
- Deduplication Key

예시:

| 작업           | Idempotent 여부   |
| -------------- | ----------------- |
| 파일 읽기      | 대체로 Idempotent |
| 검색           | 대체로 Idempotent |
| 이메일 발송    | Non-Idempotent    |
| 결제 요청      | Non-Idempotent    |
| 파일 삭제      | Non-Idempotent    |
| 동일 내용 저장 | 조건부 Idempotent |

반드시 설명:

- Retry는 Idempotent 작업에 안전
- Non-Idempotent 작업은 중복 실행 방지 필요
- Request ID / Deduplication Key를 사용할 수 있음

주의:

- Retry로 이메일이 중복 발송될 수 있음
- 결제 / 주문 / 삭제 작업은 중복 실행 위험
- Tool 실패 후 실제로 실행됐는지 확인 필요

---

# 16. Retry Rules

Tool Retry는 실패 유형에 따라 제한적으로 적용한다.

Retry 가능:

- 일시적 네트워크 오류
- Timeout 일부
- 429 Rate Limit
- 500 / 502 / 503 / 504
- 임시 파일 Lock

Retry 금지:

- Validation Error
- Permission Error
- Not Found
- Authentication Error
- Dangerous Operation
- Non-Idempotent Operation without Key

기본 Flow:

```text
Tool Failure
→ Check Retryable
→ Backoff
→ Retry
→ Return Final Result
```

주의:

- 무제한 Retry 금지
- Retry마다 로그 기록
- Non-Idempotent 작업 Retry 금지 또는 중복 방지 필요
- Retry가 외부 시스템 부하를 악화시킬 수 있음

---

# 17. Error Handling Rules

Tool Error Handling은 Agent 안정성에 중요하다.

필수 포함:

- ValidationError
- PermissionError
- NotFoundError
- TimeoutError
- RateLimitError
- ExternalApiError
- ExecutionError
- UnknownError

에러 결과 구조:

```json
{
  "status": "error",
  "error": {
    "type": "ValidationError",
    "message": "query is required",
    "retryable": false
  }
}
```

반드시 설명:

- Tool 실패는 구조화해서 반환
- Retry 가능 여부를 구분
- 사용자에게 필요한 수준으로 설명
- 내부 Stack Trace는 사용자에게 그대로 노출하지 않음

주의:

- 에러를 숨기고 성공처럼 답변 금지
- 모든 에러를 Unknown으로 처리 금지
- 민감정보가 에러 메시지에 포함되지 않게 주의

---

# 18. RAG Search Tool Rules

RAG Search Tool은 문서 검색 Agent의 핵심 Tool이다.

필수 포함:

- query
- topK
- domainFilter
- levelFilter
- metadataFilter
- similarityThreshold
- retrievedDocuments
- source

Tool Input 예시:

```json
{
  "query": "Spring Transaction Boundary",
  "topK": 5,
  "domainFilter": "Backend"
}
```

Tool Result 예시:

```json
{
  "status": "success",
  "data": {
    "documents": [
      {
        "title": "Transaction Boundary",
        "source": "Advanced_Spring_Architecture_Part.md",
        "score": 0.83
      }
    ]
  }
}
```

반드시 설명:

- RAG Search Tool은 답변 전 관련 문서 검색에 사용
- domain / level filter로 검색 범위 제한 가능
- 검색 결과에는 source와 score 포함 권장
- 검색 결과가 없을 때 fallback 필요

주의:

- 검색 결과가 없으면 문서에 없다고 말하기
- Score만으로 정답 판단 금지
- 관련 없는 문서가 많으면 Query Rewrite / Filter 조정

---

# 19. File Tool Rules

File Tool은 파일 읽기/쓰기 자동화에 사용된다.

필수 포함:

- Read File
- Write File
- Append File
- List Directory
- Path Validation
- Extension Filter
- Backup
- Dry Run

안전 기준:

```text
Read
→ Low Risk

Write / Append
→ Medium Risk

Delete / Overwrite
→ High Risk
```

반드시 설명:

- 파일 읽기는 비교적 안전하지만 경로 검증 필요
- 파일 쓰기/덮어쓰기는 사용자 확인 또는 백업 권장
- 허용 디렉터리 밖 접근 제한
- 확장자 제한 가능

주의:

- Path Traversal 방지
- 원본 파일 덮어쓰기 전 백업
- 대량 파일 수정 전 dry-run
- 민감 파일 접근 금지

---

# 20. API Tool Rules

API Tool은 외부 API 호출에 사용된다.

필수 포함:

- Endpoint
- Method
- Header
- Query Parameter
- Body
- Timeout
- Retry
- Rate Limit
- Authentication
- Response Validation

반드시 설명:

- API Key는 환경변수로 관리
- Timeout 필수
- Status Code 확인
- Response Schema 검증
- 외부 API 오류는 구조화해 반환

주의:

- Secret 로그 출력 금지
- 무제한 Retry 금지
- Rate Limit 고려
- 외부 API 결과를 무조건 신뢰하지 말 것

---

# 21. Database Tool Rules

Database Tool은 조회와 변경을 분리해서 설명한다.

필수 포함:

- Read Query
- Write Query
- Parameter Binding
- Transaction
- Permission
- Query Timeout
- Result Limit
- Audit Log

안전 기준:

```text
SELECT
→ Validate + Limit

INSERT / UPDATE / DELETE
→ Validate + Permission + Confirmation
```

반드시 설명:

- DB Read Tool과 Write Tool은 분리 권장
- SQL Injection 방지 위해 Parameter Binding 사용
- SELECT에도 Result Limit 필요
- Write 작업은 승인과 Transaction 필요

주의:

- LLM이 만든 SQL을 그대로 실행 금지
- DELETE / UPDATE without WHERE 금지
- 대량 변경 전 Preview / Dry Run
- 운영 DB 접근 권한 제한

---

# 22. Code Execution Tool Rules

Code Execution Tool은 가장 신중하게 다뤄야 한다.

필수 포함:

- Sandbox
- Timeout
- Resource Limit
- File Access Limit
- Network Access Limit
- Dependency Limit
- Output Capture
- Error Capture

반드시 설명:

- 코드 실행은 격리된 환경에서 수행
- Timeout과 메모리 제한 필요
- 파일 시스템 접근 제한 필요
- 네트워크 접근 제한 가능
- 실행 결과와 오류를 구조화

주의:

- 사용자 입력 코드를 무제한 실행 금지
- Shell Command 실행 주의
- Secret 접근 차단
- 무한 루프 / 과도한 리소스 사용 방지

---

# 23. Tool Observability Rules

Tool Calling도 관측 가능해야 한다.

필수 포함:

- Tool Call Log
- Tool Name
- Arguments Summary
- Execution Time
- Status
- Error Type
- Retry Count
- User / Agent ID
- Trace ID

로그 항목 예시:

```text
toolName
toolCallId
status
latencyMs
errorType
retryCount
```

반드시 설명:

- Tool 호출 로그는 디버깅과 감사에 필요
- 위험 작업은 Audit Log 필요
- 민감한 Arguments는 Masking
- Latency와 Error Rate를 관측

주의:

- API Key / Secret 로그 금지
- 전체 파일 내용 로그 저장 주의
- 개인정보 포함 가능성 확인

---

# 24. Agent Tool Routing Rules

Agent별 Tool 접근 권한을 분리한다.

예시:

| Agent         | 허용 Tool                                     |
| ------------- | --------------------------------------------- |
| PM Agent      | Task Routing, RAG Search                      |
| Backend Agent | RAG Search, Code Search, File Read            |
| Review Agent  | RAG Search, Static Analysis, Test Result Read |
| DevOps Agent  | Log Search, Deployment Read, Infra Status     |
| AI Agent      | RAG Search, Vector Search, Evaluation Tool    |

반드시 설명:

- 모든 Agent가 모든 Tool을 사용할 필요 없음
- 역할별 최소 권한 원칙 적용
- 위험 Tool은 특정 Agent에게만 허용
- PM Agent는 직접 실행보다 라우팅 중심

주의:

- Agent 권한이 넓으면 위험 증가
- Review Agent가 수정까지 수행할지 분리 기준 필요
- Tool 접근 정책을 문서화

---

# 25. Multi-Agent Tool Use Rules

Multi-Agent Workflow에서는 Tool 결과를 공유할 수 있어야 한다.

기본 Flow:

```text
PM Agent
→ Assign Task
→ Domain Agent Uses Tool
→ Review Agent Checks Result
→ Fix Agent Uses Tool if Needed
→ Final Output
```

필수 포함:

- Shared State
- Tool Result Sharing
- Intermediate Output
- Review Loop
- Handoff Format
- Failure Handling

반드시 설명:

- Tool 결과는 다음 Agent가 이해할 수 있게 구조화
- 중간 산출물의 source와 status 유지
- Review Agent는 Tool 결과를 검증 가능해야 함
- 실패 시 PM Agent로 되돌릴 수 있음

주의:

- Agent 간 Tool Result 형식 불일치 주의
- 실패한 Tool 결과를 성공처럼 전달 금지
- 중간 결과 누락 시 Review 품질 저하

---

# 26. Tool Security Rules

Tool Calling 문서는 보안을 반드시 포함한다.

필수 포함:

- Least Privilege
- Permission Boundary
- Input Validation
- Secret Protection
- Path Traversal Prevention
- SQL Injection Prevention
- Command Injection Prevention
- Audit Log
- Human Approval

반드시 설명:

- Tool은 시스템에 실제 영향을 줄 수 있음
- 최소 권한 원칙 적용
- 입력값 검증 필수
- Secret과 개인정보 보호
- 위험 작업은 승인 필요

주의:

- LLM이 생성한 명령을 그대로 신뢰하지 않음
- Tool 결과에 민감정보가 포함될 수 있음
- 외부 API 응답도 검증 필요
- 권한 없는 파일 / DB / API 접근 차단

---

# 27. Tool Testing Rules

Tool은 독립적으로 테스트 가능해야 한다.

필수 포함:

- Unit Test
- Integration Test
- Mock Tool
- Schema Validation Test
- Error Case Test
- Timeout Test
- Permission Test
- Dry Run Test

테스트 대상:

```text
Schema Validator
Argument Parser
Permission Checker
Tool Executor
Result Mapper
Error Handler
```

반드시 설명:

- Tool 실행 로직은 LLM 없이 테스트 가능해야 함
- 정상 케이스보다 실패 케이스 테스트가 중요
- 위험 Tool은 dry-run 테스트 필요
- 외부 API Tool은 Mocking 권장

주의:

- 테스트에서 실제 결제 / 이메일 / 배포 금지
- 운영 데이터 변경 테스트 금지
- Secret이 테스트 로그에 남지 않도록 주의

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

## Tool이 잘못 선택됨

문제:

- LLM이 요청과 맞지 않는 Tool을 선택함

원인:

- Tool Description이 모호함
- 비슷한 Tool이 너무 많음
- Tool 선택 기준이 없음

해결:

- Tool Description 개선
- Tool 이름 명확화
- Tool Routing Rule 추가
- 불필요한 Tool 제거

---

## Tool Arguments가 잘못 생성됨

문제:

- 필수 인자가 빠지거나 타입이 틀림

원인:

- JSON Schema가 불명확함
- Required Field 누락
- Parameter Description 부족

해결:

- Schema 단순화
- Required Field 명시
- enum / type 제한 추가
- 실행 전 검증 강화

---

## Tool 실행 후 결과가 너무 김

문제:

- Tool Result가 Context Window를 과도하게 사용함

원인:

- 전체 파일 / 전체 검색 결과를 반환
- Result Limit 없음
- 요약 단계 없음

해결:

- Result Limit 추가
- 필요한 필드만 반환
- 큰 결과는 요약
- Pagination 적용

---

## 위험 작업이 자동 실행됨

문제:

- 삭제, 수정, 발송 같은 작업이 승인 없이 실행됨

원인:

- Risk Level 분류 없음
- Human Confirmation Rule 없음
- Agent 권한 과다

해결:

- Tool Risk Level 정의
- High Risk 작업 승인 필수화
- Agent별 Tool 권한 제한
- dry-run 추가

---

## Tool 실패를 LLM이 성공처럼 답함

문제:

- Tool은 실패했는데 최종 답변은 성공처럼 나옴

원인:

- Tool Result status 불명확
- Error Handling Prompt 부족
- LLM이 실패 메시지를 무시

해결:

- Tool Result에 status/error 명확히 포함
- 실패 시 답변 규칙 추가
- Error Result를 구조화
- Review 단계 추가

---

# 29. Best Practice Rules

Best Practice:

- Tool 이름은 짧고 명확하게 작성
- Tool Description에 사용 시점을 포함
- Arguments는 JSON Schema로 제한
- Tool Arguments는 실행 전 검증
- Tool Result는 성공/실패를 구조화
- Side Effect가 있는 Tool은 위험도 분류
- 위험 작업은 Human Confirmation 필요
- Tool 실행에는 Timeout 설정
- Retry는 Idempotent 작업 중심으로 제한
- Tool 호출 로그를 남김
- Agent별 Tool 권한을 최소화
- Tool은 LLM 없이도 테스트 가능하게 설계

---

# 30. Comparison Rules

Tool Calling 문서는 비교 기준을 포함한다.

필수 비교 대상:

- Function Calling vs Tool Calling
- Tool Calling vs Plain Text Answer
- Auto Tool Choice vs Forced Tool Choice
- Read Tool vs Write Tool
- Idempotent Tool vs Non-Idempotent Tool
- Safe Tool vs Dangerous Tool
- Tool Result JSON vs Plain Text
- Retryable Error vs Non-Retryable Error

예시:

| 비교 | Tool Calling                     | Plain Text Answer    |
| ---- | -------------------------------- | -------------------- |
| 목적 | 외부 기능 실행                   | 모델 지식 기반 응답  |
| 장점 | 최신 정보, 파일/API/DB 접근 가능 | 빠르고 단순          |
| 단점 | 보안/실패 처리 필요              | 실제 상태 확인 불가  |
| 적합 | 검색, 계산, 파일 처리, API 호출  | 일반 설명, 개념 정리 |

---

# 31. Checklist Rules

Tool Calling 문서에는 Checklist를 포함할 수 있다.

예시:

```md
### [Checklist]

- [ ] Tool 이름이 명확한가?
- [ ] Tool Description에 사용 시점이 있는가?
- [ ] Arguments Schema가 정의되어 있는가?
- [ ] Required Field가 명확한가?
- [ ] 실행 전 입력값 검증이 있는가?
- [ ] 위험도 분류가 있는가?
- [ ] Side Effect 작업에 승인 절차가 있는가?
- [ ] Timeout이 설정되어 있는가?
- [ ] Tool Result가 구조화되어 있는가?
- [ ] Error Result가 명확한가?
- [ ] Retry 가능 여부가 구분되어 있는가?
- [ ] Tool 호출 로그가 남는가?
```

---

# 32. Retrieval Optimization Rules

강조 대상 키워드:

- Tool Calling
- Function Calling
- Tool Definition
- Function Schema
- JSON Schema
- Tool Arguments
- Tool Choice
- Tool Execution
- Tool Result
- Tool Message
- Input Validation
- Output Validation
- Safe Tool Execution
- Human Confirmation
- Idempotency
- Retry
- Error Handling
- RAG Search Tool
- File Tool
- API Tool
- Database Tool
- Code Execution Tool
- Agent Tool Routing
- Multi-Agent Tool Use
- Tool Observability
- Tool Security
- Tool Testing

키워드 반복 허용.

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

예:

- Tool Calling이 뭐야?
- Function Calling이랑 Tool Calling 차이는?
- Tool Schema는 어떻게 만들어?
- Tool Arguments는 왜 검증해야 해?
- 위험한 Tool은 어떻게 처리해?
- Human Confirmation은 언제 필요해?
- Tool Result는 어떤 구조가 좋아?
- RAG Search Tool은 어떻게 설계해?
- File Tool은 안전하게 어떻게 써?
- Tool 실패는 어떻게 처리해?
- Agent별 Tool 권한은 어떻게 나눠?

---

# 33. Version Rules

기준:

- Modern LLM Tool Calling
- Function Calling 기반 API 구조
- JSON Schema 기반 Tool Arguments
- Agent Workflow 기반 Tool Use
- RAG Search Tool 연동
- Python Tool Script 연동
- Backend API Tool 연동
- Multi-Agent System 확장 가능 구조

Legacy 제외:

- LLM이 생성한 명령을 그대로 실행하는 방식
- Schema 없는 Tool Arguments
- 검증 없는 Tool Execution
- 실패를 무시하는 Tool Result
- 위험 작업 승인 없는 자동 실행
- Agent별 권한 구분 없는 Tool Access

---

# 34. Common Mistakes

자주 발생:

- Tool Description이 모호함
- Tool이 너무 많아 선택이 흔들림
- Required Field 누락
- Arguments 검증 없이 실행
- Tool Result가 비구조적임
- Tool 실패를 성공처럼 처리
- 위험 작업 승인 없이 실행
- Retry로 Non-Idempotent 작업 중복 실행
- File Path 검증 누락
- SQL / Shell Command 검증 누락
- API Key / Secret 로그 출력
- Agent별 Tool 권한 구분 없음
- Tool 테스트 없이 Agent에 연결

---

# 35. Final Goal

Tool Calling & Function Calling RAG 문서는 Agent가 아래를 수행 가능해야 한다.

- Tool Calling 기본 개념 설명
- Function Calling과 Tool Calling 구분
- Tool Definition 작성
- JSON Schema 기반 Arguments 설계
- Tool Choice 기준 제안
- Tool Arguments 검증 기준 제안
- Tool Result 구조 설계
- Tool Error Handling 설계
- Safe Tool Execution 기준 제안
- Human Confirmation 필요 여부 판단
- RAG Search / File / API / DB Tool 설계
- Agent별 Tool 권한 분리
- Multi-Agent Tool Workflow 설계
- Tool Calling 문제 Troubleshooting
- Tool Integration Code Review

문서 품질이 Agent의 실제 작업 수행 능력과 안전성을 결정한다.

---

# Retrieval Queries

### [FAQ]

Q. Tool Calling이 뭐야?

A.
LLM이 외부 도구를 선택하고 필요한 인자를 생성해 검색, 파일 처리, API 호출 같은 작업을 수행하도록 연결하는 구조다.

Q. Function Calling과 Tool Calling 차이는?

A.
Function Calling은 함수 호출 구조에 가깝고, Tool Calling은 검색, 파일, API, DB, 코드 실행까지 포함하는 더 넓은 개념이다.

Q. Tool Definition에는 뭐가 들어가야 해?

A.
Tool Name, Description, Parameters, Required Fields, Return Type, Side Effect, Failure Case가 들어가야 한다.

Q. Tool Schema는 왜 필요해?

A.
LLM이 올바른 인자를 생성하도록 제한하고, 실행 전 검증하기 위해 필요하다.

Q. Tool Arguments는 왜 검증해야 해?

A.
LLM이 생성한 입력은 틀릴 수 있고, 파일 삭제, SQL 실행, API 호출 같은 위험 작업으로 이어질 수 있기 때문이다.

Q. Tool Choice는 어떻게 정해?

A.
요청이 문서 검색, 파일 처리, API 호출, 계산, 코드 실행 중 무엇이 필요한지 판단해 적절한 Tool을 선택한다.

Q. 모든 요청에 Tool을 써야 해?

A.
아니다. 일반 개념 설명처럼 Tool이 필요 없는 요청은 직접 답변해도 된다.

Q. Tool Result는 어떤 구조가 좋아?

A.
status, data, error, metadata를 분리한 JSON 구조가 좋다.

Q. Tool 실패는 어떻게 처리해?

A.
실패 원인과 retry 가능 여부를 구조화해서 반환하고, LLM이 성공처럼 답하지 않도록 해야 한다.

Q. 위험한 Tool은 어떻게 처리해?

A.
파일 삭제, DB 변경, 이메일 발송, 결제, 배포 같은 작업은 Human Confirmation을 요구해야 한다.

Q. Human Confirmation은 언제 필요해?

A.
되돌리기 어렵거나 외부 시스템에 영향을 주는 작업, 비용이 발생하는 작업, 데이터 변경 작업 전에 필요하다.

Q. Idempotency는 왜 중요해?

A.
Retry나 중복 실행 시 결과가 안전한지 판단하기 위해 중요하다.

Q. Retry는 언제 가능해?

A.
일시적 네트워크 오류, 429, 5xx, 일부 Timeout처럼 재시도 가능한 오류에서 제한적으로 가능하다.

Q. File Tool은 어떻게 안전하게 설계해?

A.
경로 검증, 허용 디렉터리 제한, 확장자 제한, 백업, dry-run, 사용자 확인을 적용한다.

Q. API Tool은 어떻게 설계해?

A.
Endpoint, Method, Header, Body, Timeout, Retry, Rate Limit, Response Validation을 포함한다.

Q. Database Tool은 어떻게 안전하게 써?

A.
Read와 Write를 분리하고, Parameter Binding, Result Limit, Transaction, Permission, Confirmation을 적용한다.

Q. Code Execution Tool은 왜 위험해?

A.
임의 코드가 파일, 네트워크, 리소스, Secret에 접근할 수 있으므로 Sandbox와 제한이 필요하다.

Q. Agent별 Tool 권한은 어떻게 나눠?

A.
역할별 최소 권한 원칙에 따라 PM Agent는 라우팅 중심, Domain Agent는 필요한 Tool만, 위험 Tool은 제한된 Agent만 사용하게 한다.

Q. Tool Observability는 왜 필요해?

A.
어떤 Tool이 언제 어떤 결과로 실행되었는지 추적해야 디버깅, 감사, 성능 분석이 가능하기 때문이다.

Q. Tool Calling 문서의 최종 목표는 뭐야?

A.
Agent가 외부 도구를 정확하고 안전하게 호출하며, 실패와 위험 작업을 통제할 수 있게 만드는 것이다.
