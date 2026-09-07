# Tool Calling & Function Calling Part04 - Result & Error Handling

---

# 1. Tool Result

## 1.1 Tool Result Concept

### [개념]

Tool Result는 Tool Execution 이후 Runtime이 LLM 또는 다음 Agent에게 전달하는 구조화된 실행 결과이다.

Tool Result는 단순 문자열이 아니라 성공, 실패, 차단, 일부 성공, 데이터, 오류, 출처, 실행 메타데이터를 구분하는 구조여야 한다.

Tool Result는 LLM Final Answer와 Review Agent 검증의 근거가 된다.

Tool Result가 불명확하면 LLM은 실패한 Tool Execution을 성공처럼 답하거나, 출처 없는 데이터를 신뢰할 수 있다.

---

### [핵심]

- Tool Result는 Tool Execution 결과이다.
- Tool Result는 status 필드를 포함한다.
- status는 success / error / blocked / partial을 사용한다.
- 성공 결과는 data 필드에 저장한다.
- 실패 결과는 error 필드에 저장한다.
- 차단 결과는 reason과 requiredAction을 포함할 수 있다.
- 일부 성공 결과는 successItems와 failedItems를 분리한다.
- metadata에는 toolName, executionTimeMs, source, traceId를 포함할 수 있다.
- Tool Result는 다음 Agent가 재사용 가능해야 한다.
- Tool Result에 Secret, Token, 개인정보를 그대로 포함하지 않는다.

---

### [실무]

2026 실무 기준 Tool Result 기본 구조:

```json
{
  "status": "success",
  "data": {},
  "message": "Tool execution completed.",
  "metadata": {
    "toolName": "search_rag_documents",
    "executionTimeMs": 120,
    "source": "rag-index",
    "traceId": "trace_001"
  }
}
```

실패 구조:

```json
{
  "status": "error",
  "error": {
    "type": "ValidationError",
    "code": "REQUIRED_FIELD_MISSING",
    "message": "query is required.",
    "retryable": false
  },
  "metadata": {
    "toolName": "search_rag_documents",
    "executionTimeMs": 3,
    "traceId": "trace_002"
  }
}
```

차단 구조:

```json
{
  "status": "blocked",
  "reason": "HumanConfirmationRequired",
  "message": "This operation requires user confirmation.",
  "requiredAction": {
    "type": "confirm",
    "target": "docs/tool-calling.md",
    "operation": "overwrite"
  },
  "metadata": {
    "toolName": "write_project_file",
    "riskLevel": "high"
  }
}
```

권장 필드:

| 필드            | 목적                                     |
| --------------- | ---------------------------------------- |
| status          | success / error / blocked / partial 구분 |
| data            | 성공 데이터                              |
| error           | 실패 정보                                |
| reason          | blocked 또는 partial 이유                |
| message         | 요약 메시지                              |
| requiredAction  | 승인 / 재입력 / 재시도 등 필요 조치      |
| metadata        | 실행 정보                                |
| source          | 출처                                     |
| confidence      | 신뢰도                                   |
| executionTimeMs | 실행 시간                                |
| traceId         | 추적 ID                                  |
| retryCount      | 재시도 횟수                              |

---

### [FAQ]

Q. Tool Result가 뭐야?
A. Tool Execution 이후 Runtime이 LLM이나 다음 Agent에게 전달하는 구조화된 실행 결과다.

Q. Tool Result는 왜 구조화해야 해?
A. 성공, 실패, 차단, 일부 성공, 데이터, 오류, 출처를 명확히 구분해야 LLM과 Agent가 안정적으로 후속 처리를 할 수 있기 때문이다.

Q. Tool Result에 status가 필요한 이유는?
A. Tool 실행이 성공했는지, 실패했는지, 차단되었는지, 일부만 성공했는지 명확히 판단하기 위해 필요하다.

Q. Tool Result에 metadata는 왜 필요해?
A. Tool Name, 실행 시간, traceId, source를 추적해 디버깅, Review, 감사에 활용하기 위해 필요하다.

Q. Tool Result가 너무 크면 어떻게 해?
A. 필요한 필드만 남기고 요약하며 source metadata는 유지한다.

---

# 2. Success Result

## 2.1 Success Result Structure

### [개념]

Success Result는 Tool Execution이 정상적으로 완료되었을 때 반환하는 결과 구조이다.

Success Result는 status: success를 사용한다.

Success Result는 data 필드에 실제 결과를 담고, metadata 필드에 실행 정보를 담는다.

Success Result는 LLM이 Final Answer를 만들 수 있을 만큼 충분하지만, Context Window를 낭비하지 않을 만큼 제한되어야 한다.

---

### [핵심]

- Success Result는 status: success를 사용한다.
- data에는 실제 결과만 담는다.
- metadata에는 실행 정보를 담는다.
- source가 있는 결과는 출처를 포함한다.
- confidence가 필요한 경우 신뢰도를 포함한다.
- 결과가 없으면 empty result를 명확히 표현한다.
- 성공 결과라도 Output Validation을 통과해야 한다.
- 성공 결과에 민감정보가 포함되면 마스킹한다.
- Success Result를 Error Result나 Blocked Result와 혼동하지 않는다.

---

### [실무]

RAG Search Tool Success Result:

```json
{
  "status": "success",
  "data": {
    "documents": [
      {
        "title": "Tool Arguments Validation",
        "source": "Tool_Calling_Function_Calling_Part03_Arguments_Validation_Execution.md",
        "score": 0.89,
        "chunk": "Tool Arguments는 실행 전 검증해야 한다."
      }
    ]
  },
  "metadata": {
    "toolName": "search_rag_documents",
    "executionTimeMs": 118,
    "topK": 5
  }
}
```

File Read Tool Success Result:

```json
{
  "status": "success",
  "data": {
    "filePath": "docs/tool-calling.md",
    "contentPreview": "# Tool Calling\n...",
    "sizeBytes": 4821
  },
  "metadata": {
    "toolName": "read_project_file",
    "executionTimeMs": 9
  }
}
```

Empty Result 예시:

```json
{
  "status": "success",
  "data": {
    "documents": []
  },
  "message": "No relevant documents found.",
  "metadata": {
    "toolName": "search_rag_documents",
    "executionTimeMs": 96
  }
}
```

Empty Result는 Tool 실패가 아니다.

단, LLM은 “검색 결과 없음”을 근거로 fallback, query rewrite, filter 완화, 또는 “문서에 없음” 판단을 수행해야 한다.

---

### [FAQ]

Q. Success Result는 어떤 구조가 좋아?
A. status: success, data, metadata를 기본으로 하고 source와 confidence를 필요에 따라 포함하는 구조가 좋다.

Q. 검색 결과가 0개면 실패야?
A. 아니다. Tool이 정상 실행되었지만 결과가 없는 상태이므로 success + empty data로 표현할 수 있다.

Q. Success Result에도 검증이 필요해?
A. 필요하다. 결과가 너무 크거나 민감정보가 포함될 수 있기 때문이다.

Q. data에는 무엇을 넣어야 해?
A. Tool의 실제 실행 결과만 넣고 실행 시간, 출처, traceId 같은 정보는 metadata에 분리한다.

Q. Success Result가 너무 길면 어떻게 해?
A. 핵심 필드만 남기고 요약하며 source metadata를 유지한다.

---

# 3. Error Result

## 3.1 Error Result Structure

### [개념]

Error Result는 Tool Arguments 검증 실패, 권한 실패, Tool Execution 실패, 외부 API 실패, Timeout 등으로 Tool 요청이 실패했을 때 반환하는 구조화된 실패 결과이다.

Error Result는 실패 원인, 오류 유형, 사용자 메시지, 재시도 가능 여부를 명확히 포함해야 한다.

Error Result를 구조화하지 않으면 LLM이 실패를 성공처럼 해석할 수 있다.

---

### [핵심]

- Error Result는 status: error를 사용한다.
- error.type은 오류 분류를 나타낸다.
- error.code는 시스템 처리용 오류 코드를 나타낸다.
- error.message는 안전한 설명을 제공한다.
- error.retryable은 재시도 가능 여부를 나타낸다.
- Raw Exception은 그대로 노출하지 않는다.
- Stack Trace는 사용자 또는 LLM Context에 그대로 전달하지 않는다.
- Secret, Token, 내부 경로는 마스킹한다.
- Error Result는 Review Agent가 검증할 수 있어야 한다.

---

### [실무]

표준 Error Result:

```json
{
  "status": "error",
  "error": {
    "type": "PermissionError",
    "code": "PATH_OUTSIDE_ALLOWED_DIRECTORY",
    "message": "The requested file path is outside the allowed directory.",
    "retryable": false
  },
  "metadata": {
    "toolName": "read_project_file",
    "executionTimeMs": 4,
    "traceId": "trace_004"
  }
}
```

Error Result 필드:

| 필드      | 설명             |
| --------- | ---------------- |
| type      | 오류 유형        |
| code      | 오류 코드        |
| message   | 안전한 오류 설명 |
| retryable | 재시도 가능 여부 |
| detail    | 내부용 상세 정보 |
| metadata  | Tool 실행 정보   |

Raw Exception 금지 예시:

```text
java.sql.SQLException: Access denied for user 'admin' with password 'secret123'
```

안전한 변환 예시:

```json
{
  "status": "error",
  "error": {
    "type": "AuthenticationError",
    "code": "DATABASE_AUTH_FAILED",
    "message": "Database authentication failed.",
    "retryable": false
  }
}
```

---

### [FAQ]

Q. Error Result가 뭐야?
A. Tool 검증 실패 또는 Tool 실행 실패를 구조화해서 반환하는 결과다.

Q. Error Result에는 무엇이 들어가야 해?
A. error type, code, message, retryable, metadata가 들어가야 한다.

Q. Raw Exception을 그대로 보여줘도 돼?
A. 안 된다. Secret, 내부 경로, Stack Trace가 포함될 수 있으므로 안전한 메시지로 변환해야 한다.

Q. retryable은 왜 필요해?
A. Agent Runtime이 재시도 가능한 오류와 재시도하면 안 되는 오류를 구분하기 위해 필요하다.

Q. Tool 실패를 LLM에게 숨겨도 돼?
A. 안 된다. 실패 상태를 명확히 전달해야 LLM이 성공처럼 답하지 않는다.

---

# 4. Standard Error Type

## 4.1 Error Type Standard

### [개념]

Error Type은 Tool 실패 원인을 표준화해서 분류하는 기준이다.

Error Type이 표준화되어 있으면 Agent Runtime, Review Agent, Observability System이 실패를 안정적으로 분석할 수 있다.

Error Type 기준은 Tool Testing과 Troubleshooting에서도 동일하게 사용한다.

---

### [핵심]

- ValidationError는 입력값 검증 실패이다.
- PermissionError는 권한 부족 또는 허용 범위 위반이다.
- NotFoundError는 대상 리소스가 없는 경우이다.
- TimeoutError는 실행 제한 시간을 초과한 경우이다.
- RateLimitError는 호출 제한에 걸린 경우이다.
- AuthenticationError는 인증 실패이다.
- ExternalApiError는 외부 API 실패이다.
- ExecutionError는 실행 중 오류이다.
- DangerousOperationError는 위험 작업 차단 또는 위험 패턴 감지이다.
- UnknownError는 분류되지 않은 예외이다.
- UnknownError는 최소화한다.

---

### [실무]

표준 Error Type:

| Error Type              | 의미                       | Retry  |
| ----------------------- | -------------------------- | ------ |
| ValidationError         | 입력값 형식 / 필수값 오류  | false  |
| PermissionError         | 권한 없음 / 허용 범위 위반 | false  |
| NotFoundError           | 대상 없음                  | false  |
| TimeoutError            | 실행 시간 초과             | 조건부 |
| RateLimitError          | 호출 제한                  | true   |
| AuthenticationError     | 인증 실패                  | false  |
| ExternalApiError        | 외부 API 오류              | 조건부 |
| ExecutionError          | 실행 중 오류               | 조건부 |
| DangerousOperationError | 위험 작업 차단             | false  |
| UnknownError            | 알 수 없는 오류            | 조건부 |

Error Type 선택 기준:

```text
입력값 문제 → ValidationError
권한 문제 → PermissionError
대상 없음 → NotFoundError
시간 초과 → TimeoutError
호출 제한 → RateLimitError
인증 실패 → AuthenticationError
외부 API 실패 → ExternalApiError
실행 중 예외 → ExecutionError
위험 작업 차단 → DangerousOperationError
분류 불가 → UnknownError
```

UnknownError는 최소화한다.

모든 오류를 UnknownError로 처리하면 Troubleshooting, Retry 판단, Observability 품질이 떨어진다.

---

### [FAQ]

Q. Error Type은 왜 표준화해야 해?
A. Agent Runtime과 Review Agent가 오류 원인, 재시도 여부, 후속 조치를 안정적으로 판단하기 위해 필요하다.

Q. ValidationError는 언제 발생해?
A. Required Field 누락, Type 오류, Enum 오류, Range 오류처럼 입력값이 잘못되었을 때 발생한다.

Q. PermissionError는 언제 발생해?
A. Agent 권한이 없거나 허용 디렉터리, 허용 API, 허용 DB 범위를 벗어났을 때 발생한다.

Q. TimeoutError는 항상 Retry 가능해?
A. 아니다. Side Effect가 있는 작업은 실제 실행 여부를 확인한 뒤 재시도해야 한다.

Q. UnknownError를 많이 써도 돼?
A. 권장하지 않는다. 가능한 구체적인 Error Type으로 분류해야 한다.

---

# 5. Validation Error

## 5.1 Validation Error Handling

### [개념]

ValidationError는 Tool Arguments가 Schema Validation 또는 Business Validation을 통과하지 못했을 때 발생하는 오류이다.

ValidationError는 Tool Execution 전에 발생해야 한다.

ValidationError가 발생하면 Tool을 실행하지 않는다.

---

### [핵심]

- ValidationError는 입력값 오류이다.
- Required Field 누락 시 발생한다.
- Type 오류 시 발생한다.
- Enum 오류 시 발생한다.
- Range 오류 시 발생한다.
- 빈 문자열, null 값 정책 위반 시 발생한다.
- Business Rule 위반 시 발생할 수 있다.
- ValidationError는 retryable false가 기본이다.
- ValidationError 발생 시 Tool Execution을 중단한다.
- ValidationError는 LLM이 Tool Arguments를 다시 생성하는 계기가 될 수 있다.

---

### [실무]

ValidationError 예시:

```json
{
  "status": "error",
  "error": {
    "type": "ValidationError",
    "code": "REQUIRED_FIELD_MISSING",
    "message": "query is required.",
    "retryable": false
  },
  "metadata": {
    "toolName": "search_rag_documents"
  }
}
```

Enum 오류 예시:

```json
{
  "status": "error",
  "error": {
    "type": "ValidationError",
    "code": "INVALID_ENUM_VALUE",
    "message": "mode must be one of: read, write, append.",
    "retryable": false
  }
}
```

ValidationError 처리 Flow:

```text
Generated Tool Arguments
→ Schema Validation Failed
→ Create ValidationError
→ Do Not Execute Tool
→ Return Error Result
```

ValidationError는 일반적인 Tool Retry 대상이 아니다.

단, LLM이 arguments를 수정해 새로운 Tool Call을 생성할 수 있다.

---

### [FAQ]

Q. ValidationError가 뭐야?
A. Tool Arguments가 필수값, 타입, enum, 범위, 업무 규칙을 만족하지 못했을 때 발생하는 입력값 오류다.

Q. ValidationError가 발생하면 Tool을 실행해도 돼?
A. 안 된다. 실행하지 않고 Error Result를 반환해야 한다.

Q. ValidationError는 Retry 가능해?
A. 일반적인 Tool Retry는 불가능하다. 다만 LLM이 arguments를 수정해 새 Tool Call을 만들 수는 있다.

Q. Required Field 누락은 어떤 Error Type이야?
A. ValidationError다.

Q. Business Validation 실패도 ValidationError야?
A. 업무 규칙 위반이면 ValidationError로 처리할 수 있고, 권한 또는 허용 범위 위반이면 PermissionError로 처리할 수 있다.

---

# 6. Permission Error

## 6.1 Permission Error Handling

### [개념]

PermissionError는 Agent, User, Tool이 해당 작업을 수행할 권한이 없거나 허용 범위를 벗어났을 때 발생하는 오류이다.

PermissionError는 최소 권한 원칙과 Tool Security를 지키기 위한 핵심 오류이다.

PermissionError는 Runtime에서 강제해야 한다.

---

### [핵심]

- PermissionError는 권한 부족 오류이다.
- Agent Tool Permission 위반 시 발생한다.
- 허용 디렉터리 밖 파일 접근 시 발생한다.
- 허용되지 않은 API endpoint 호출 시 발생한다.
- 허용되지 않은 DB table 접근 시 발생한다.
- Secret 또는 민감 파일 접근 시 발생한다.
- PermissionError는 retryable false가 기본이다.
- PermissionError 발생 시 Tool Execution을 중단한다.
- PermissionError는 Prompt 수정으로 우회하면 안 된다.

---

### [실무]

파일 접근 PermissionError:

```json
{
  "status": "error",
  "error": {
    "type": "PermissionError",
    "code": "PATH_OUTSIDE_ALLOWED_DIRECTORY",
    "message": "filePath is outside the allowed directory.",
    "retryable": false
  },
  "metadata": {
    "toolName": "read_project_file"
  }
}
```

Agent 권한 PermissionError:

```json
{
  "status": "error",
  "error": {
    "type": "PermissionError",
    "code": "AGENT_TOOL_PERMISSION_DENIED",
    "message": "Review Agent does not have permission to write project files.",
    "retryable": false
  }
}
```

PermissionError 처리 Flow:

```text
Validated Tool Arguments
→ Permission Check Failed
→ Create PermissionError
→ Do Not Execute Tool
→ Return Error Result
```

PermissionError는 Prompt 수정으로 우회하면 안 된다.

권한 정책은 Agent Runtime 또는 Backend System에서 강제해야 한다.

---

### [FAQ]

Q. PermissionError가 뭐야?
A. Agent나 User가 해당 Tool 또는 리소스를 사용할 권한이 없을 때 발생하는 오류다.

Q. PermissionError는 재시도해도 돼?
A. 아니다. 권한 부족은 재시도해도 해결되지 않으므로 retryable false가 기본이다.

Q. 허용 디렉터리 밖 파일 접근은 어떤 오류야?
A. PermissionError로 처리하는 것이 적절하다.

Q. Review Agent가 write Tool을 호출하면 어떻게 해?
A. 권한 정책에 따라 PermissionError를 반환하고 실행하지 않는다.

Q. PermissionError는 어디서 강제해야 해?
A. LLM Prompt가 아니라 Agent Runtime 또는 Backend System에서 강제해야 한다.

---

# 7. Timeout Error

## 7.1 Timeout Error Handling

### [개념]

TimeoutError는 Tool Execution이 지정된 제한 시간 안에 완료되지 않았을 때 발생하는 오류이다.

TimeoutError는 외부 API 지연, DB 쿼리 지연, 코드 무한 루프, 대용량 파일 처리 등에서 발생할 수 있다.

TimeoutError는 Idempotency와 Side Effect 여부에 따라 retryable 값이 달라진다.

---

### [핵심]

- TimeoutError는 실행 시간 초과 오류이다.
- 모든 Tool에는 Timeout이 필요하다.
- TimeoutError는 조건부 retryable이다.
- Idempotent Tool은 Retry가 비교적 안전하다.
- Non-Idempotent Tool은 Retry 전에 실제 실행 여부를 확인한다.
- TimeoutError에는 timeoutMs와 executionTimeMs를 포함하는 것이 좋다.
- Timeout 이후 Side Effect 발생 여부를 확인해야 한다.
- TimeoutError는 Retry / Idempotency와 연결된다.

---

### [실무]

TimeoutError 예시:

```json
{
  "status": "error",
  "error": {
    "type": "TimeoutError",
    "code": "TOOL_EXECUTION_TIMEOUT",
    "message": "Tool execution timed out after 10000ms.",
    "retryable": true
  },
  "metadata": {
    "toolName": "call_external_api",
    "timeoutMs": 10000,
    "executionTimeMs": 10000
  }
}
```

Non-Idempotent Timeout 예시:

```json
{
  "status": "error",
  "error": {
    "type": "TimeoutError",
    "code": "PAYMENT_TIMEOUT_UNKNOWN_STATE",
    "message": "Payment request timed out. Verify payment status before retry.",
    "retryable": false
  },
  "metadata": {
    "toolName": "request_payment",
    "requiresStateCheck": true
  }
}
```

Timeout 처리 Flow:

```text
Tool Timeout
→ Check Tool Idempotency
→ Check Side Effect Possibility
→ Decide retryable
→ Return TimeoutError
```

---

### [FAQ]

Q. TimeoutError가 뭐야?
A. Tool 실행이 제한 시간 안에 끝나지 않았을 때 발생하는 오류다.

Q. TimeoutError는 항상 재시도 가능해?
A. 아니다. 검색이나 읽기 작업은 재시도 가능하지만 결제, 이메일 발송, DB 변경은 상태 확인이 먼저 필요하다.

Q. TimeoutError Result에는 무엇을 넣어야 해?
A. error type, timeoutMs, executionTimeMs, retryable 여부를 포함하는 것이 좋다.

Q. Timeout 후 Side Effect를 왜 확인해?
A. 요청은 Timeout됐지만 실제 외부 시스템에서는 실행되었을 수 있기 때문이다.

Q. Code Execution Tool에서 TimeoutError는 왜 중요해?
A. 무한 루프와 과도한 리소스 사용을 차단하기 위해 중요하다.

---

# 8. Rate Limit Error

## 8.1 Rate Limit Error Handling

### [개념]

RateLimitError는 외부 API, LLM Provider, Search Tool, Database Proxy 등이 허용된 호출량을 초과했을 때 발생하는 오류이다.

RateLimitError는 일시적 오류일 수 있으므로 Backoff 기반 Retry를 제한적으로 적용할 수 있다.

---

### [핵심]

- RateLimitError는 호출 제한 오류이다.
- 429 응답과 연결되는 경우가 많다.
- Retry-After 헤더가 있으면 우선 사용한다.
- Backoff를 적용한다.
- 무제한 Retry는 금지한다.
- retryCount를 metadata에 기록한다.
- 사용량 제한을 초과한 원인을 로그로 남긴다.
- 사용자에게 지연 또는 제한 상태를 명확히 설명한다.
- RateLimitError가 반복되면 fallback을 고려한다.

---

### [실무]

RateLimitError 예시:

```json
{
  "status": "error",
  "error": {
    "type": "RateLimitError",
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Rate limit exceeded. Retry after 30 seconds.",
    "retryable": true
  },
  "metadata": {
    "toolName": "call_external_api",
    "retryAfterSeconds": 30,
    "retryCount": 0
  }
}
```

Retry Flow:

```text
RateLimitError
→ Check Retry-After
→ Apply Backoff
→ Retry Within Limit
→ Return Final Result
```

Backoff 예시:

```text
1st retry: 1s
2nd retry: 2s
3rd retry: 4s
Stop after max retry count
```

RateLimitError 반복 시 fallback:

- cache result 사용
- lower topK 사용
- request batching
- graceful degradation
- 사용자에게 제한 상태 안내

---

### [FAQ]

Q. RateLimitError가 뭐야?
A. API나 Tool 호출량이 허용 한도를 초과했을 때 발생하는 오류다.

Q. RateLimitError는 Retry 가능해?
A. 가능하다. 단, Retry-After와 Backoff를 적용하고 최대 재시도 횟수를 제한해야 한다.

Q. 429 오류는 어떤 Error Type이야?
A. 일반적으로 RateLimitError로 처리한다.

Q. RateLimitError를 무제한 Retry해도 돼?
A. 안 된다. 외부 시스템 부하를 악화시키고 차단될 수 있다.

Q. RateLimitError가 계속되면 어떻게 해?
A. Cache, fallback, 요청 축소, 사용자 안내를 적용한다.

---

# 9. External API Error

## 9.1 External API Error Handling

### [개념]

ExternalApiError는 외부 API 호출 중 발생하는 오류이다.

외부 API는 네트워크, 인증, 요청 형식, Rate Limit, 서버 오류, 응답 Schema 변경 등 다양한 이유로 실패할 수 있다.

ExternalApiError는 내부 Tool Error로 구조화해서 반환해야 한다.

---

### [핵심]

- ExternalApiError는 외부 API 실패를 나타낸다.
- HTTP status code를 확인한다.
- Response Schema를 검증한다.
- Timeout을 설정한다.
- Retry 가능 status와 불가능 status를 구분한다.
- API Key, Token은 로그에 남기지 않는다.
- 외부 API 오류 메시지를 그대로 사용자에게 노출하지 않는다.
- fallback 또는 degrade 전략을 준비한다.
- External API Raw Output은 Tool Result Mapping을 거쳐야 한다.

---

### [실무]

HTTP Status 처리 기준:

| Status | Error Type                      | Retry  |
| ------ | ------------------------------- | ------ |
| 400    | ValidationError                 | false  |
| 401    | AuthenticationError             | false  |
| 403    | PermissionError                 | false  |
| 404    | NotFoundError                   | false  |
| 408    | TimeoutError                    | 조건부 |
| 429    | RateLimitError                  | true   |
| 500    | ExternalApiError                | true   |
| 502    | ExternalApiError                | true   |
| 503    | ExternalApiError                | true   |
| 504    | TimeoutError / ExternalApiError | true   |

ExternalApiError 예시:

```json
{
  "status": "error",
  "error": {
    "type": "ExternalApiError",
    "code": "UPSTREAM_SERVICE_UNAVAILABLE",
    "message": "External API is temporarily unavailable.",
    "retryable": true
  },
  "metadata": {
    "toolName": "call_external_api",
    "httpStatus": 503,
    "provider": "external-service"
  }
}
```

Response Schema 오류:

```json
{
  "status": "error",
  "error": {
    "type": "ExternalApiError",
    "code": "INVALID_UPSTREAM_RESPONSE",
    "message": "External API returned an unexpected response format.",
    "retryable": false
  }
}
```

---

### [FAQ]

Q. ExternalApiError가 뭐야?
A. 외부 API 호출 중 네트워크, 서버 오류, 응답 형식 오류 등이 발생했을 때 사용하는 오류다.

Q. 외부 API 오류 메시지를 그대로 보여줘도 돼?
A. 안 된다. API Key, 내부 정보, Provider 상세 오류가 포함될 수 있으므로 안전한 메시지로 변환해야 한다.

Q. 500, 502, 503 오류는 Retry 가능해?
A. 일반적으로 가능하지만 최대 재시도 횟수와 Backoff를 적용해야 한다.

Q. 401 오류는 Retry 가능해?
A. 아니다. 인증 정보 문제이므로 AuthenticationError로 처리하고 retryable false가 적절하다.

Q. 외부 API 응답도 검증해야 해?
A. 그렇다. Response Schema가 예상과 다르면 ExternalApiError로 처리해야 한다.

---

# 10. Blocked Result

## 10.1 Blocked Result Concept

### [개념]

Blocked Result는 Tool Execution이 실패한 것이 아니라 안전 정책, 권한 정책, Human Confirmation 필요성 때문에 실행되지 않은 상태이다.

Blocked Result는 Error Result와 구분한다.

Blocked Result는 위험 작업을 자동 실행하지 않기 위한 안전 장치이다.

---

### [핵심]

- Blocked Result는 실행 차단 상태이다.
- status: blocked를 사용한다.
- 위험 Tool은 Human Confirmation 전 blocked가 될 수 있다.
- Dangerous Operation은 blocked가 될 수 있다.
- blocked에는 reason을 포함한다.
- blocked에는 requiredAction을 포함하는 것이 좋다.
- blocked는 Tool을 실행하지 않은 상태이다.
- blocked는 사용자 승인 요청 또는 Workflow 재계획으로 이어질 수 있다.
- blocked는 Safe Execution과 직접 연결된다.

---

### [실무]

Human Confirmation Required 예시:

```json
{
  "status": "blocked",
  "reason": "HumanConfirmationRequired",
  "message": "This operation may overwrite an existing file and requires user confirmation.",
  "requiredAction": {
    "type": "confirm",
    "preview": {
      "target": "docs/tool-calling.md",
      "operation": "overwrite"
    }
  },
  "metadata": {
    "toolName": "write_project_file",
    "riskLevel": "high"
  }
}
```

Dangerous Operation Blocked 예시:

```json
{
  "status": "blocked",
  "reason": "DangerousOperationBlocked",
  "message": "DELETE without WHERE is not allowed.",
  "metadata": {
    "toolName": "execute_database_write",
    "riskLevel": "high"
  }
}
```

Blocked 처리 Flow:

```text
Risk Check
→ Human Confirmation Required
→ Return Blocked Result
→ Wait for Approval or Replan
```

Blocked Result는 실패가 아니다.

Blocked Result는 안전 정책이 정상 작동한 결과이다.

---

### [FAQ]

Q. Blocked Result가 뭐야?
A. Tool이 실패한 것이 아니라 안전 정책이나 승인 필요 때문에 실행되지 않은 상태다.

Q. blocked와 error는 달라?
A. 다르다. error는 검증 실패 또는 실행 실패이고, blocked는 실행 전 정책에 의해 차단된 상태다.

Q. Human Confirmation이 필요한 작업은 어떤 status가 좋아?
A. status: blocked와 reason: HumanConfirmationRequired로 표현하는 것이 좋다.

Q. blocked 상태에서 Tool은 실행된 거야?
A. 아니다. 실행되지 않은 상태다.

Q. Blocked Result는 왜 필요해?
A. 위험 작업을 자동 실행하지 않고 사용자 승인 또는 재계획으로 넘기기 위해 필요하다.

---

# 11. Partial Result

## 11.1 Partial Result Concept

### [개념]

Partial Result는 Tool Execution이 일부만 성공했거나 결과 일부만 사용 가능한 상태를 나타낸다.

Partial Result는 전체 실패와 구분해야 한다.

Multi-Agent Workflow에서는 Partial Result를 명확히 표현해야 다음 Agent가 누락된 부분을 보완할 수 있다.

---

### [핵심]

- Partial Result는 일부 성공 상태이다.
- status: partial을 사용한다.
- 성공한 항목과 실패한 항목을 분리한다.
- failedItems에는 실패 이유를 포함한다.
- partial result는 Review Agent 검토 대상이다.
- partial result는 fallback 또는 추가 Tool Call로 이어질 수 있다.
- partial result를 success처럼 처리하지 않는다.
- partial result는 Multi-Agent Failure Handling과 연결된다.

---

### [실무]

Partial Result 예시:

```json
{
  "status": "partial",
  "data": {
    "successItems": [
      {
        "filePath": "docs/part01.md",
        "status": "success"
      },
      {
        "filePath": "docs/part02.md",
        "status": "success"
      }
    ],
    "failedItems": [
      {
        "filePath": "docs/part03.md",
        "error": {
          "type": "PermissionError",
          "message": "File access denied."
        }
      }
    ]
  },
  "message": "2 files processed, 1 file failed.",
  "metadata": {
    "toolName": "batch_read_files",
    "executionTimeMs": 42
  }
}
```

Partial Result 처리 Flow:

```text
Partial Result
→ Separate Success Items
→ Separate Failed Items
→ Review Missing Data
→ Retry Safe Items or Replan
```

Partial Result 사용 예시:

| 상황                    | 처리                              |
| ----------------------- | --------------------------------- |
| 일부 파일 읽기 성공     | 실패 파일만 재검토                |
| 일부 API 응답 실패      | 성공 데이터 사용 + 실패 원인 표시 |
| 일부 테스트 실패        | pass / fail 분리                  |
| 일부 RAG 검색 결과 부족 | Query Rewrite 수행                |

---

### [FAQ]

Q. Partial Result가 뭐야?
A. Tool 실행이 일부만 성공했거나 결과 일부만 사용 가능한 상태다.

Q. Partial Result는 success야 error야?
A. 둘 중 하나로 단순 처리하지 않고 status: partial로 구분하는 것이 좋다.

Q. Partial Result는 왜 중요해?
A. 일부 성공 데이터를 버리지 않고 실패한 부분만 보완할 수 있기 때문이다.

Q. Partial Result를 최종 답변에 그대로 써도 돼?
A. 사용할 수 있지만 일부 누락 또는 실패가 있었다는 점을 명확히 해야 한다.

Q. Partial Result 후에는 무엇을 해?
A. 실패 항목을 재시도할지, fallback을 사용할지, 사용자 확인이 필요한지 판단한다.

---

# 12. Tool Result Mapping

## 12.1 Result Mapping Concept

### [개념]

Tool Result Mapping은 Raw Tool Output을 LLM과 Agent가 사용할 수 있는 표준 Tool Result 구조로 변환하는 과정이다.

Raw Output은 형식이 일정하지 않고, 너무 크거나, 민감정보를 포함하거나, 실패 상태가 불명확할 수 있다.

Result Mapping은 Tool Output을 안전하고 일관된 구조로 변환한다.

---

### [핵심]

- Raw Output을 그대로 전달하지 않는다.
- status, data, error, metadata 구조로 변환한다.
- success / error / blocked / partial을 명확히 구분한다.
- 민감정보를 마스킹한다.
- 큰 결과는 요약한다.
- source metadata를 유지한다.
- 외부 API 응답은 내부 표준 Error Type으로 변환한다.
- Result Mapping은 Tool별로 일관되게 적용한다.
- Result Mapping은 Agent Handoff 품질에 직접 영향을 준다.

---

### [실무]

Result Mapping Flow:

```text
Raw Tool Output
→ Detect Success / Error / Blocked / Partial
→ Validate Output Schema
→ Mask Sensitive Data
→ Limit Result Size
→ Add Metadata
→ Return Standard Tool Result
```

외부 API Raw Output:

```json
{
  "error": "Invalid API key: sk-xxxx",
  "status": 401
}
```

Mapped Tool Result:

```json
{
  "status": "error",
  "error": {
    "type": "AuthenticationError",
    "code": "API_AUTH_FAILED",
    "message": "External API authentication failed.",
    "retryable": false
  },
  "metadata": {
    "httpStatus": 401
  }
}
```

RAG Raw Result Mapping:

| Raw Field     | Mapped Field |
| ------------- | ------------ |
| document_name | title        |
| file          | source       |
| similarity    | score        |
| text          | chunk        |
| metadata      | metadata     |

Result Mapping이 없으면 Agent마다 Tool Result 해석 방식이 달라진다.

---

### [FAQ]

Q. Tool Result Mapping이 뭐야?
A. Raw Tool Output을 status, data, error, metadata가 있는 표준 Tool Result 구조로 변환하는 과정이다.

Q. Raw Output을 그대로 전달하면 안 돼?
A. 권장하지 않는다. 형식이 불안정하고 민감정보나 불필요한 데이터가 포함될 수 있다.

Q. Result Mapping에서 가장 중요한 것은?
A. 성공/실패/차단/일부 성공 구분, 민감정보 제거, source metadata 유지, 표준 Error Type 변환이다.

Q. 외부 API 오류는 어떻게 Mapping해?
A. HTTP status와 응답 내용을 내부 Error Type으로 변환한다.

Q. Result Mapping은 왜 Multi-Agent에서 중요해?
A. 여러 Agent가 동일한 구조로 Tool Result를 이해하고 검증할 수 있게 하기 때문이다.

---

# 13. Error Handling Flow

## 13.1 Standard Error Handling Flow

### [개념]

Error Handling Flow는 Tool 실패를 감지하고, 오류를 분류하고, 재시도 가능 여부를 판단하고, 안전한 결과로 반환하는 절차이다.

Tool Error Handling은 Agent Workflow 안정성의 핵심이다.

---

### [핵심]

- Tool Error는 숨기지 않는다.
- Tool Error는 표준 Error Type으로 분류한다.
- Retry 가능 여부를 판단한다.
- Non-Idempotent 작업은 중복 실행을 방지한다.
- 사용자에게 필요한 수준으로 설명한다.
- 내부 Stack Trace는 숨긴다.
- Review Agent가 오류를 검토할 수 있게 metadata를 남긴다.
- 실패 후 fallback 또는 replan을 수행할 수 있다.

---

### [실무]

기본 Error Handling Flow:

```text
Tool Failure
→ Capture Error
→ Classify Error Type
→ Mask Sensitive Data
→ Decide retryable
→ Check Idempotency
→ Retry or Stop
→ Return Error Result
→ Replan or Final Response
```

재시도 판단 Flow:

```text
Error Result
→ retryable true?
→ Idempotent?
→ retryCount < maxRetry?
→ Backoff
→ Retry
```

재시도 금지 Flow:

```text
ValidationError / PermissionError / AuthenticationError
→ retryable false
→ Do Not Retry
→ Return Error Result
```

위험 작업 실패 Flow:

```text
High Risk Tool Failure
→ Check Unknown Side Effect
→ Do Not Auto Retry
→ Require Status Verification
→ Return Safe Error Result
```

---

### [FAQ]

Q. Tool Error Handling 기본 흐름은?
A. 오류 캡처 → 오류 유형 분류 → 민감정보 제거 → Retry 판단 → Error Result 반환 순서다.

Q. Tool Error를 숨기면 안 되는 이유는?
A. LLM이 실패를 성공처럼 답하거나 다음 Agent가 잘못된 결과를 검토할 수 있기 때문이다.

Q. 어떤 오류는 Retry하면 안 돼?
A. ValidationError, PermissionError, AuthenticationError, 위험 작업, Non-Idempotent 작업은 Retry하면 안 된다.

Q. High Risk Tool 실패 후 자동 Retry해도 돼?
A. 안 된다. 실제 Side Effect 발생 여부를 먼저 확인해야 한다.

Q. Error Handling 결과는 어디에 전달돼?
A. Tool Message 형태로 LLM Context 또는 다음 Agent에게 전달된다.

---

# 14. User Facing Error Message

## 14.1 Safe User Message

### [개념]

User Facing Error Message는 Tool Error를 사용자에게 설명하기 위한 안전한 메시지이다.

사용자 메시지는 내부 구현, Stack Trace, Secret, Token, 상세 시스템 경로를 노출하지 않아야 한다.

사용자에게 필요한 수준으로 원인과 다음 조치를 제공한다.

---

### [핵심]

- 사용자 메시지는 짧고 명확해야 한다.
- 내부 Stack Trace를 노출하지 않는다.
- Secret, API Key, Token을 노출하지 않는다.
- 기술적 오류는 사용자 언어로 변환한다.
- 필요한 경우 재시도 가능 여부를 알려준다.
- 사용자가 조치할 수 있는 항목을 제시한다.
- 불확실한 상태는 명확히 표시한다.
- User Facing Message와 internal detail을 분리한다.

---

### [실무]

나쁜 메시지:

```text
java.io.FileNotFoundException: /home/app/secrets/.env at FileReader.java:42
```

좋은 메시지:

```text
요청한 파일을 찾을 수 없습니다. 파일 경로를 확인해 주세요.
```

나쁜 메시지:

```text
OpenAI API key sk-xxxx is invalid.
```

좋은 메시지:

```text
외부 API 인증에 실패했습니다. API Key 설정을 확인해야 합니다.
```

불확실한 상태 메시지:

```text
요청 시간이 초과되었습니다. 작업이 실제로 처리되었는지 확인한 뒤 다시 시도해야 합니다.
```

사용자 메시지는 Tool Result의 error.message와 다를 수 있다.

내부 처리용 detail은 사용자에게 노출하지 않는다.

---

### [FAQ]

Q. User Facing Error Message가 뭐야?
A. Tool Error를 사용자에게 안전하고 이해하기 쉽게 설명하는 메시지다.

Q. Stack Trace를 사용자에게 보여줘도 돼?
A. 안 된다. 내부 구현 정보와 민감정보가 포함될 수 있다.

Q. API Key 오류를 어떻게 말해야 해?
A. 실제 Key를 노출하지 않고 “API 인증에 실패했습니다”처럼 안전하게 설명한다.

Q. Timeout 오류는 어떻게 설명해?
A. 시간이 초과되었고, Side Effect 가능성이 있으면 실제 처리 여부 확인이 필요하다고 설명한다.

Q. 사용자 메시지에 retryable 정보를 넣어도 돼?
A. 가능하다. 단, 위험 작업은 무조건 재시도를 권장하지 않는다.

---

# 15. Result & Error Checklist

## 15.1 Result Handling Checklist

### [개념]

Result & Error Checklist는 Tool Result와 Error Handling 구조가 안전하고 재사용 가능한지 검수하는 기준이다.

Tool Result는 Agent Workflow의 근거 데이터이므로 표준화와 검증이 필수이다.

이 Checklist는 Final Integration Checklist와 연결된다.

---

### [핵심]

- status가 명확한가?
- success, error, blocked, partial이 구분되는가?
- data와 error가 분리되어 있는가?
- Error Type이 표준화되어 있는가?
- retryable 여부가 포함되어 있는가?
- metadata가 포함되어 있는가?
- source가 유지되는가?
- Raw Exception이 제거되었는가?
- Secret과 개인정보가 마스킹되었는가?
- 큰 결과가 제한되었는가?
- Tool Message로 전달 가능한 구조인가?
- 다음 Agent가 검증 가능한 구조인가?

---

### [실무]

Result & Error Checklist:

```md
### [Checklist]

- [ ] Tool Result에 status가 있는가?
- [ ] status 값이 success / error / blocked / partial 중 하나인가?
- [ ] 성공 결과는 data에 저장되는가?
- [ ] 실패 결과는 error에 저장되는가?
- [ ] blocked 결과는 reason과 requiredAction을 포함하는가?
- [ ] partial 결과는 successItems와 failedItems를 구분하는가?
- [ ] error.type이 표준 Error Type인가?
- [ ] error.code가 포함되어 있는가?
- [ ] error.message가 안전한 메시지인가?
- [ ] error.retryable이 명확한가?
- [ ] metadata.toolName이 포함되어 있는가?
- [ ] executionTimeMs가 포함되어 있는가?
- [ ] traceId 또는 requestId가 필요한 경우 포함되어 있는가?
- [ ] source metadata가 유지되는가?
- [ ] Raw Exception이 노출되지 않는가?
- [ ] Secret / Token / 개인정보가 마스킹되었는가?
- [ ] 큰 Tool Result가 요약 또는 제한되었는가?
- [ ] Partial Result가 success로 오해되지 않는가?
- [ ] Blocked Result가 실행 실패와 구분되는가?
- [ ] Retry 가능 여부가 Idempotency와 함께 판단되는가?
- [ ] User Facing Error Message가 안전한가?
```

Checklist 실패 시 Tool Result Mapping 또는 Error Handling Rule을 수정한다.

---

### [FAQ]

Q. Result & Error Checklist는 왜 필요해?
A. Tool Result와 Error Handling이 Agent Workflow에서 안전하게 재사용될 수 있는지 검수하기 위해 필요하다.

Q. 가장 중요한 Checklist 항목은?
A. status 구분, data/error 분리, Error Type 표준화, retryable 여부, 민감정보 마스킹이다.

Q. blocked와 error를 꼭 구분해야 해?
A. 구분하는 것이 좋다. blocked는 정책상 실행하지 않은 상태이고 error는 검증 실패 또는 실행 실패 상태다.

Q. Partial Result는 어떻게 검수해?
A. 성공 항목과 실패 항목이 분리되어 있는지 확인한다.

Q. Checklist 실패 시 어떻게 해?
A. Tool Result 구조, Error Mapping, User Facing Message를 수정한 뒤 다시 검수한다.

---

# Retrieval Queries

### [FAQ]

Q. Tool Result가 뭐야?
A. Tool Execution 이후 Runtime이 LLM이나 다음 Agent에게 전달하는 구조화된 실행 결과다.

Q. Tool Result는 왜 구조화해야 해?
A. 성공, 실패, 차단, 일부 성공, 데이터, 오류, 출처를 명확히 구분해 LLM과 Agent가 안정적으로 후속 처리하기 위해 필요하다.

Q. Tool Result 기본 구조는?
A. status, data, error, message, metadata, source, executionTimeMs, traceId를 포함하는 구조가 좋다.

Q. Tool Result status는 무엇을 구분해야 해?
A. success, error, blocked, partial을 구분해야 한다.

Q. Success Result는 어떻게 작성해?
A. status: success를 사용하고 실제 결과는 data에, 실행 정보는 metadata에 저장한다.

Q. 검색 결과가 없으면 Tool 실패야?
A. 아니다. Tool이 정상 실행되었으면 success와 empty data로 표현할 수 있다.

Q. Error Result는 어떻게 작성해?
A. status: error를 사용하고 error.type, error.code, error.message, error.retryable을 포함한다.

Q. Tool Error를 구조화하지 않으면 어떻게 돼?
A. LLM이 실패를 성공처럼 해석하거나 다음 Agent가 잘못된 결과를 검토할 수 있다.

Q. Raw Exception을 그대로 노출해도 돼?
A. 안 된다. Stack Trace, Secret, 내부 경로가 포함될 수 있으므로 안전한 메시지로 변환해야 한다.

Q. 표준 Error Type에는 뭐가 있어?
A. ValidationError, PermissionError, NotFoundError, TimeoutError, RateLimitError, AuthenticationError, ExternalApiError, ExecutionError, DangerousOperationError, UnknownError가 있다.

Q. ValidationError는 언제 발생해?
A. Required Field 누락, Type 오류, Enum 오류, Range 오류, Business Rule 위반 시 발생한다.

Q. PermissionError는 언제 발생해?
A. Agent 권한 부족, 허용 디렉터리 밖 접근, 허용되지 않은 API 또는 DB 접근 시 발생한다.

Q. TimeoutError는 항상 Retry 가능해?
A. 아니다. Side Effect가 있는 작업은 실제 실행 여부를 확인한 뒤 재시도해야 한다.

Q. RateLimitError는 어떻게 처리해?
A. Retry-After와 Backoff를 적용하고 최대 재시도 횟수를 제한한다.

Q. ExternalApiError는 어떻게 처리해?
A. HTTP status와 응답을 내부 표준 Error Type으로 Mapping하고 민감정보를 제거한다.

Q. Blocked Result가 뭐야?
A. Tool이 실패한 것이 아니라 안전 정책이나 Human Confirmation 필요 때문에 실행되지 않은 상태다.

Q. blocked와 error 차이는?
A. blocked는 실행 전 정책 차단이고 error는 검증 실패 또는 실행 실패다.

Q. Partial Result가 뭐야?
A. Tool 실행이 일부만 성공했거나 일부 결과만 사용 가능한 상태다.

Q. Partial Result는 어떻게 표현해?
A. status: partial을 사용하고 성공 항목과 실패 항목을 분리한다.

Q. Tool Result Mapping이 뭐야?
A. Raw Tool Output을 status, data, error, metadata가 있는 표준 Tool Result 구조로 변환하는 과정이다.

Q. Raw Output을 그대로 전달하면 안 되는 이유는?
A. 형식이 불안정하고 민감정보, 불필요한 데이터, 내부 오류 정보가 포함될 수 있기 때문이다.

Q. Tool Error Handling 기본 Flow는?
A. Tool Failure → Capture Error → Classify Error Type → Mask Sensitive Data → Decide retryable → Return Error Result 순서다.

Q. High Risk Tool 실패 후 자동 Retry해도 돼?
A. 안 된다. 실제 Side Effect 발생 여부를 먼저 확인해야 한다.

Q. User Facing Error Message는 어떻게 작성해?
A. 내부 Stack Trace와 Secret을 제거하고 사용자가 이해할 수 있는 짧고 안전한 설명으로 작성한다.

Q. Tool Result에 source가 왜 필요해?
A. LLM과 Review Agent가 답변 근거와 데이터 출처를 검증할 수 있게 하기 위해 필요하다.

Q. Tool Result에 executionTimeMs가 왜 필요해?
A. Tool Latency 분석, Timeout 원인 파악, Observability에 필요하다.

Q. Result & Error Checklist에는 무엇이 들어가야 해?
A. status 구분, data/error 분리, Error Type 표준화, retryable 여부, metadata, source, 민감정보 마스킹을 확인해야 한다.

Q. Tool Result & Error Handling의 최종 목표는 뭐야?
A. Agent가 Tool 실행 결과와 실패 원인을 정확히 이해하고 안전하게 후속 판단을 할 수 있게 만드는 것이다.
