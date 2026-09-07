# Tool Calling & Function Calling Part03 - Arguments Validation & Execution

---

# 1. Tool Arguments

## 1.1 Tool Arguments Concept

### [개념]

Tool Arguments는 LLM이 Tool Execution을 위해 생성하는 입력값이다.

Tool Arguments는 Tool Definition의 parameters / JSON Schema를 기준으로 생성된다.

Tool Arguments는 실행 가능한 명령이 아니라 검증 대상이다.

LLM이 생성한 Tool Arguments는 누락, 타입 오류, 범위 오류, 권한 오류, 위험 입력값을 포함할 수 있다.

---

### [핵심]

- Tool Arguments는 Tool Execution 입력값이다.
- Tool Arguments는 LLM이 생성하지만 신뢰하지 않는다.
- Tool Arguments는 JSON Schema 기준으로 검증한다.
- Tool Arguments는 Business Validation을 통과해야 한다.
- Tool Arguments는 Permission Check를 통과해야 한다.
- Tool Arguments는 Risk Check를 통과해야 한다.
- 파일 경로, URL, SQL, Shell Command는 고위험 입력값이다.
- Tool Arguments가 유효하지 않으면 Tool Execution을 중단한다.
- Tool Arguments 검증 실패는 ValidationError 또는 PermissionError로 반환한다.

---

### [실무]

2026 실무 기준 Tool Arguments 처리 Flow:

```text
Generated Tool Arguments
→ Required Field Check
→ Type Check
→ Range Check
→ Enum Check
→ Null / Empty Check
→ Business Validation
→ Permission Check
→ Risk Check
→ Tool Execution
```

Tool Arguments 예시:

```json
{
  "query": "Tool Calling input validation",
  "topK": 5,
  "domainFilter": "AI"
}
```

검증 대상:

| 검증 항목            | 설명                                              |
| -------------------- | ------------------------------------------------- |
| Required Field Check | 필수값 존재 여부                                  |
| Type Check           | string, integer, boolean, array, object 타입 확인 |
| Range Check          | minimum, maximum 범위 확인                        |
| Enum Check           | 허용된 값인지 확인                                |
| Null Check           | null 허용 여부 확인                               |
| Empty Check          | 빈 문자열 허용 여부 확인                          |
| Business Validation  | 업무 규칙 확인                                    |
| Permission Check     | Agent / User 권한 확인                            |
| Risk Check           | 위험도와 승인 필요 여부 확인                      |

Tool Arguments는 Runtime에서 검증한다.

LLM Prompt만으로 검증을 대체하지 않는다.

---

### [FAQ]

Q. Tool Arguments가 뭐야?
A. LLM이 Tool 실행을 위해 생성하는 입력값이다.

Q. Tool Arguments는 신뢰해도 돼?
A. 안 된다. LLM이 만든 입력값은 반드시 실행 전에 검증해야 한다.

Q. Tool Arguments 검증은 어디서 해?
A. Agent Runtime 또는 Backend System에서 Tool Execution 직전에 수행한다.

Q. Tool Arguments가 잘못되면 어떻게 해?
A. Tool을 실행하지 않고 ValidationError 또는 PermissionError를 반환한다.

Q. Tool Arguments에서 특히 위험한 값은?
A. 파일 경로, URL, SQL, Shell Command, DB 변경 조건, 이메일 수신자, 결제 금액이다.

---

# 2. Schema Validation

## 2.1 Schema Validation Concept

### [개념]

Schema Validation은 Tool Arguments가 Tool Definition의 JSON Schema에 맞는지 확인하는 1차 검증이다.

Schema Validation은 Tool Execution 전에 수행한다.

Schema Validation은 type, required, enum, minimum, maximum, array item type, object structure를 확인한다.

---

### [핵심]

- Schema Validation은 형식 검증이다.
- Tool Arguments는 JSON Schema와 일치해야 한다.
- Required Field가 없으면 실행하지 않는다.
- Type이 다르면 실행하지 않는다.
- Enum에 없는 값이면 실행하지 않는다.
- Range를 벗어나면 실행하지 않는다.
- Schema Validation은 안전 실행의 1차 방어선이다.
- Schema Validation만으로는 Safe Execution이 완성되지 않는다.
- Schema Validation 이후 Business Validation / Permission Check / Risk Check가 필요하다.

---

### [실무]

JSON Schema 예시:

```json
{
  "type": "object",
  "properties": {
    "filePath": {
      "type": "string",
      "description": "Target file path."
    },
    "mode": {
      "type": "string",
      "enum": ["read", "write", "append"]
    }
  },
  "required": ["filePath", "mode"]
}
```

유효한 Tool Arguments:

```json
{
  "filePath": "docs/rag.md",
  "mode": "read"
}
```

유효하지 않은 Tool Arguments:

```json
{
  "filePath": "docs/rag.md",
  "mode": "delete"
}
```

Schema Validation 실패 결과:

```json
{
  "status": "error",
  "error": {
    "type": "ValidationError",
    "code": "INVALID_ENUM_VALUE",
    "message": "mode must be one of: read, write, append",
    "retryable": false
  },
  "metadata": {
    "toolName": "read_project_file"
  }
}
```

Schema Validation 이후 Flow:

```text
Schema Validation
→ Business Validation
→ Permission Check
→ Risk Check
→ Tool Execution
```

---

### [FAQ]

Q. Schema Validation이 뭐야?
A. Tool Arguments가 JSON Schema의 type, required, enum, range 조건에 맞는지 확인하는 검증이다.

Q. Schema Validation은 언제 해?
A. Tool Execution 전에 반드시 수행한다.

Q. Schema Validation만 하면 충분해?
A. 아니다. 업무 규칙, 권한, 위험도, 경로 검증은 별도로 해야 한다.

Q. enum 검증은 왜 필요해?
A. 허용되지 않은 mode, action, domainFilter 값이 실행되는 것을 막기 위해 필요하다.

Q. Schema Validation 실패 시 Retry해도 돼?
A. 일반적인 Tool Retry는 하지 않는다. 대신 LLM이 올바른 Arguments를 다시 생성할 수 있다.

---

# 3. Business Validation

## 3.1 Business Validation Concept

### [개념]

Business Validation은 Tool Arguments가 기술적으로 올바를 뿐 아니라 실제 업무 규칙과 허용 범위에 맞는지 확인하는 검증이다.

JSON Schema가 통과되어도 Business Validation에서 실패할 수 있다.

예를 들어 filePath가 string이어도 허용 디렉터리 밖이면 실행하면 안 된다.

---

### [핵심]

- Business Validation은 업무 규칙 검증이다.
- Schema Validation 이후 수행한다.
- Tool별 실행 조건을 확인한다.
- Agent 권한과 사용자 요청 범위를 확인한다.
- 허용 디렉터리, 허용 도메인, 허용 테이블을 확인한다.
- 위험한 입력값을 차단한다.
- Business Validation 실패 시 Tool Execution을 중단한다.
- Business Validation 결과는 ValidationError 또는 PermissionError로 매핑한다.

---

### [실무]

Business Validation 예시:

| Tool            | Business Validation                 |
| --------------- | ----------------------------------- |
| RAG Search Tool | query가 빈 문자열이 아닌지 확인     |
| File Read Tool  | 허용 디렉터리 내부 파일인지 확인    |
| File Write Tool | 덮어쓰기 여부와 승인 필요 여부 확인 |
| API Tool        | 허용된 endpoint인지 확인            |
| Database Tool   | 허용된 table / column인지 확인      |
| Email Tool      | 수신자와 본문 preview 확인          |
| Deployment Tool | 대상 environment와 승인 여부 확인   |

File Tool 검증 예시:

```text
filePath = "../../secrets/.env"

Schema Validation
→ string type 통과

Business Validation
→ Path Traversal 위험
→ PermissionError 반환
→ 실행 중단
```

Business Validation 실패 결과:

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

---

### [FAQ]

Q. Business Validation이 뭐야?
A. Tool Arguments가 업무 규칙, 허용 범위, 실행 조건에 맞는지 확인하는 검증이다.

Q. Schema Validation과 Business Validation 차이는?
A. Schema Validation은 형식 검증이고, Business Validation은 실행해도 되는 값인지 판단하는 규칙 검증이다.

Q. filePath가 string이면 실행해도 돼?
A. 아니다. 허용 디렉터리 내부인지, Path Traversal 위험이 없는지 확인해야 한다.

Q. API endpoint도 검증해야 해?
A. 그렇다. 허용된 endpoint와 method만 호출해야 한다.

Q. Business Validation 실패 시 어떻게 해?
A. Tool을 실행하지 않고 ValidationError 또는 PermissionError를 반환한다.

---

# 4. Permission Check

## 4.1 Permission Check Concept

### [개념]

Permission Check는 현재 Agent 또는 User가 해당 Tool을 실행할 권한이 있는지 확인하는 절차이다.

Tool Calling에서는 Agent별 최소 권한 원칙을 적용해야 한다.

Permission Check는 Tool Execution 전 필수 단계이다.

Permission Check는 permissionLevel과 Agent Tool Permission을 기준으로 수행한다.

---

### [핵심]

- Permission Check는 Agent / User 권한을 확인한다.
- 모든 Agent가 모든 Tool을 사용할 수 없어야 한다.
- read, validate, write, execute, admin 권한을 분리한다.
- 위험 Tool은 제한된 Agent만 사용할 수 있다.
- PM Agent는 직접 실행보다 라우팅 중심이 적절하다.
- Review Agent는 read / validate 중심이 적절하다.
- 권한이 없으면 Tool Execution을 중단한다.
- PermissionError는 retryable false로 처리한다.

---

### [실무]

권한 확인 Flow:

```text
Validated Tool Arguments
→ Identify Agent Role
→ Check Tool Permission Policy
→ Check User Permission
→ Check Risk Level
→ Execute or Reject
```

Agent Tool Permission 예시:

| Agent          | 허용 권한                       | 제한                         |
| -------------- | ------------------------------- | ---------------------------- |
| PM Agent       | read, route                     | write, deploy, db_write 제한 |
| Backend Agent  | read, validate, limited write   | production deploy 제한       |
| Frontend Agent | read, validate, limited write   | db_write 제한                |
| Review Agent   | read, validate                  | write 제한                   |
| DevOps Agent   | read, validate, limited execute | production deploy 승인 필요  |
| AI/ML Agent    | read, validate, evaluation      | destructive tool 제한        |

PermissionError 예시:

```json
{
  "status": "error",
  "error": {
    "type": "PermissionError",
    "code": "AGENT_TOOL_PERMISSION_DENIED",
    "message": "Review Agent does not have permission to write project files.",
    "retryable": false
  },
  "metadata": {
    "toolName": "write_project_file",
    "agent": "review-agent"
  }
}
```

---

### [FAQ]

Q. Permission Check가 뭐야?
A. 현재 Agent나 User가 해당 Tool을 실행할 권한이 있는지 확인하는 절차다.

Q. Agent별 Tool 권한을 왜 나눠?
A. 최소 권한 원칙으로 오작동이나 위험 작업의 피해 범위를 줄이기 위해서다.

Q. PM Agent가 파일 수정 Tool을 실행해도 돼?
A. 권장하지 않는다. PM Agent는 라우팅과 검색 중심으로 제한하는 것이 안전하다.

Q. Review Agent가 파일을 수정해도 돼?
A. 기본적으로 read / validate 권한 중심이 적절하고, 수정은 승인된 Domain Agent 또는 별도 Fix 단계에서 수행하는 것이 좋다.

Q. PermissionError는 재시도해도 돼?
A. 아니다. 권한 부족은 재시도해도 해결되지 않으므로 retryable false로 처리한다.

---

# 5. Risk Check

## 5.1 Risk Check Concept

### [개념]

Risk Check는 Tool Execution이 외부 시스템, 파일, DB, 비용, 사용자 계정, 배포 환경에 영향을 줄 수 있는지 판단하는 절차이다.

Risk Check는 sideEffect, riskLevel, requiresConfirmation을 기준으로 수행한다.

Risk Check는 Safe Execution과 Human Confirmation의 진입점이다.

---

### [핵심]

- Risk Check는 Tool Execution 전 수행한다.
- Low Risk는 자동 실행 가능하다.
- Medium Risk는 검증과 로그가 필요하다.
- High Risk는 Human Confirmation이 필요하다.
- Side Effect가 있는 Tool은 위험도 분류가 필요하다.
- Non-Idempotent Tool은 중복 실행 방지 기준이 필요하다.
- Risk Level은 Tool Definition에 포함하는 것이 좋다.
- Risk Check 실패 또는 승인 필요 시 실행하지 않고 blocked를 반환한다.

---

### [실무]

위험도 기준:

```text
Low Risk
→ Auto Execute

Medium Risk
→ Validate + Log

High Risk
→ Human Confirmation Required
```

Risk Level 예시:

| Tool                   | riskLevel     | 처리                                 |
| ---------------------- | ------------- | ------------------------------------ |
| search_rag_documents   | low           | Auto Execute                         |
| read_project_file      | low           | Auto Execute + Path Validation       |
| write_project_file     | medium ~ high | Validate + Confirmation if overwrite |
| execute_database_write | high          | Confirmation + Transaction           |
| send_email_message     | high          | Preview + Confirmation               |
| request_payment        | high          | Confirmation + Idempotency Key       |
| deploy_application     | high          | Approval + Audit Log                 |

Risk Check 결과 예시:

```json
{
  "status": "blocked",
  "reason": "HumanConfirmationRequired",
  "message": "This tool may overwrite an existing file and requires user confirmation.",
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

---

### [FAQ]

Q. Risk Check가 뭐야?
A. Tool 실행이 외부 시스템이나 데이터에 영향을 주는지 판단하고 실행 방식을 결정하는 절차다.

Q. Low Risk Tool은 자동 실행해도 돼?
A. 일반적으로 가능하지만 입력값 검증은 필요하다.

Q. High Risk Tool은 어떻게 처리해?
A. 사용자 확인, Preview, Audit Log, Undo 가능 여부 확인 후 실행해야 한다.

Q. Side Effect Tool은 모두 위험해?
A. 대체로 중간 이상 위험으로 분류한다. 특히 삭제, 발송, 결제, 배포는 고위험이다.

Q. Risk Check 결과 blocked면 어떻게 해?
A. Tool을 실행하지 않고 사용자 승인 또는 추가 검증을 요구한다.

---

# 6. Tool Execution

## 6.1 Tool Execution Concept

### [개념]

Tool Execution은 검증된 Tool Call을 Agent Runtime 또는 Backend System이 실제로 수행하는 단계이다.

Tool Execution은 LLM이 직접 수행하지 않는다.

Tool Execution은 Timeout, Retry, Error Capture, Result Capture, Audit Log 기준을 포함해야 한다.

---

### [핵심]

- Tool Execution은 검증 이후에만 수행한다.
- Tool Execution은 Runtime이 담당한다.
- Tool Execution 전 precondition을 확인한다.
- Tool Execution에는 Timeout을 설정한다.
- Tool Execution 결과와 오류를 모두 캡처한다.
- Tool Execution 결과는 Tool Result로 구조화한다.
- Side Effect Tool Execution은 Audit Log를 남긴다.
- 실패한 실행을 성공처럼 처리하지 않는다.
- Tool Execution 결과는 Result Mapping 기준으로 변환한다.

---

### [실무]

Tool Execution 기본 Flow:

```text
Validated Tool Call
→ Precondition Check
→ Permission Check
→ Risk Check
→ Execute with Timeout
→ Capture Result
→ Capture Error
→ Validate Output
→ Map to Tool Result
```

실행 결과 성공 예시:

```json
{
  "status": "success",
  "data": {
    "result": "Tool executed successfully."
  },
  "metadata": {
    "toolName": "execute_test_suite",
    "executionTimeMs": 8420
  }
}
```

실행 결과 실패 예시:

```json
{
  "status": "error",
  "error": {
    "type": "TimeoutError",
    "code": "TOOL_EXECUTION_TIMEOUT",
    "message": "Tool execution exceeded timeout.",
    "retryable": true
  },
  "metadata": {
    "toolName": "execute_test_suite",
    "executionTimeMs": 30000
  }
}
```

Tool Execution 금지:

- 검증 없는 실행
- 무기한 실행
- 위험 Tool 자동 실행
- Raw Exception 그대로 노출
- Secret / Token 로그 출력
- 실패 결과를 success로 반환

---

### [FAQ]

Q. Tool Execution은 누가 해?
A. LLM이 아니라 Agent Runtime 또는 Backend System이 수행한다.

Q. Tool Execution 전 반드시 해야 하는 것은?
A. Schema Validation, Business Validation, Permission Check, Risk Check를 수행해야 한다.

Q. Tool Execution에 Timeout이 필요한 이유는?
A. 무한 실행, 외부 API 지연, 코드 무한 루프, 리소스 낭비를 막기 위해 필요하다.

Q. Tool Execution 실패 시 어떻게 해?
A. error type, message, retryable 여부를 포함한 구조화된 Tool Result를 반환한다.

Q. Raw Exception을 그대로 사용자에게 보여줘도 돼?
A. 안 된다. 민감정보나 내부 구현 정보가 포함될 수 있으므로 안전한 메시지로 변환해야 한다.

---

# 7. Timeout

## 7.1 Timeout Rules

### [개념]

Timeout은 Tool Execution이 지정된 시간 안에 완료되지 않으면 중단하는 제한이다.

Timeout은 Agent Runtime 안정성과 리소스 보호를 위해 필수이다.

Tool별 Timeout은 Risk Level과 작업 특성에 맞게 설정한다.

---

### [핵심]

- 모든 Tool Execution에는 Timeout이 필요하다.
- API Tool은 네트워크 지연을 고려한다.
- Code Execution Tool은 무한 루프 방지를 위해 Timeout이 필수이다.
- Database Tool은 Query Timeout이 필요하다.
- File Tool은 대용량 파일 처리 Timeout이 필요하다.
- Timeout 발생 시 TimeoutError를 반환한다.
- TimeoutError는 Idempotency와 Side Effect에 따라 retryable 여부가 달라진다.
- Timeout 이후 Non-Idempotent 작업은 상태 확인이 필요하다.

---

### [실무]

Timeout 기준 예시:

| Tool                | Timeout 예시 | 비고               |
| ------------------- | -----------: | ------------------ |
| RAG Search Tool     |       3~10초 | 검색 지연 방지     |
| File Read Tool      |       3~10초 | 대용량 파일 제한   |
| API Tool            |       5~30초 | 외부 API 지연 고려 |
| Database Read Tool  |       3~15초 | Query Timeout      |
| Code Execution Tool |       5~60초 | Sandbox 제한       |
| Test Execution Tool |     30~300초 | 테스트 규모별 조정 |
| Deployment Tool     |    별도 정책 | 승인 및 로그 필수  |

Timeout 결과 예시:

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

Timeout 이후 확인:

- 실제 작업이 수행되었는지 확인
- Side Effect가 발생했는지 확인
- Retry 가능 여부 확인
- 중복 실행 위험 확인

---

### [FAQ]

Q. Timeout이 뭐야?
A. Tool 실행이 지정된 시간 안에 끝나지 않으면 중단하는 제한이다.

Q. 모든 Tool에 Timeout이 필요해?
A. 필요하다. 검색, API, DB, 파일, 코드 실행 모두 Timeout을 설정해야 한다.

Q. TimeoutError는 항상 Retry 가능해?
A. 아니다. Side Effect가 있는 작업은 실제 실행 여부를 확인하지 않고 Retry하면 중복 실행 위험이 있다.

Q. Code Execution Tool에 Timeout이 중요한 이유는?
A. 무한 루프와 과도한 리소스 사용을 막기 위해 필수이다.

Q. Timeout 후 무엇을 확인해야 해?
A. 작업이 실제로 수행되었는지, Side Effect가 발생했는지, 재시도해도 안전한지 확인해야 한다.

---

# 8. Retry

## 8.1 Retry Rules

### [개념]

Retry는 Tool Execution 실패 후 같은 작업을 다시 시도하는 절차이다.

Retry는 일시적 오류에만 제한적으로 적용해야 한다.

Retry는 Idempotent 작업 중심으로 안전하게 수행한다.

Retry 판단 기준은 Error Handling과 Safe Execution 기준과 연결된다.

---

### [핵심]

- Retry는 무제한으로 수행하지 않는다.
- Retry 가능 오류와 불가능 오류를 구분한다.
- Idempotent Tool은 Retry가 비교적 안전하다.
- Non-Idempotent Tool은 Retry에 주의한다.
- ValidationError는 Retry하지 않는다.
- PermissionError는 Retry하지 않는다.
- AuthenticationError는 Retry하지 않는다.
- NotFoundError는 보통 Retry하지 않는다.
- RateLimitError와 일부 5xx 오류는 Retry 가능하다.
- Retry에는 Backoff를 적용한다.

---

### [실무]

Retry 가능:

| Error Type                | Retry       |
| ------------------------- | ----------- |
| NetworkError              | 가능        |
| TimeoutError              | 조건부 가능 |
| RateLimitError            | 가능        |
| ExternalApiError          | 조건부 가능 |
| 500 Internal Server Error | 가능        |
| 502 Bad Gateway           | 가능        |
| 503 Service Unavailable   | 가능        |
| 504 Gateway Timeout       | 가능        |
| Temporary File Lock       | 가능        |

Retry 금지:

| Error Type                 | Retry     |
| -------------------------- | --------- |
| ValidationError            | 금지      |
| PermissionError            | 금지      |
| NotFoundError              | 보통 금지 |
| AuthenticationError        | 금지      |
| DangerousOperationError    | 금지      |
| Non-Idempotent without Key | 금지      |

Retry Flow:

```text
Tool Failure
→ Check Error Type
→ Check Idempotency
→ Check Side Effect
→ Check Retry Count
→ Apply Backoff
→ Retry
→ Return Final Tool Result
```

Retry 결과 metadata:

```json
{
  "metadata": {
    "toolName": "call_external_api",
    "retryCount": 2,
    "finalStatus": "success"
  }
}
```

---

### [FAQ]

Q. Retry는 언제 해?
A. 네트워크 오류, 429 Rate Limit, 5xx 오류, 일부 Timeout처럼 일시적 오류에서 제한적으로 수행한다.

Q. Retry하면 안 되는 오류는?
A. ValidationError, PermissionError, AuthenticationError, 위험 작업, Idempotency가 없는 Non-Idempotent 작업은 Retry하면 안 된다.

Q. Retry를 무제한으로 해도 돼?
A. 안 된다. Retry Count와 Backoff를 설정해야 한다.

Q. Non-Idempotent Tool은 왜 Retry가 위험해?
A. 이메일 중복 발송, 결제 중복 요청, DB 중복 변경이 발생할 수 있기 때문이다.

Q. Retry 결과에는 무엇을 남겨야 해?
A. retryCount, errorType, finalStatus, executionTimeMs 같은 metadata를 남기는 것이 좋다.

---

# 9. Idempotency

## 9.1 Idempotency Concept

### [개념]

Idempotency는 같은 Tool Call을 여러 번 실행해도 결과가 안전하게 동일한지 판단하는 기준이다.

Tool Retry와 중복 실행 방지를 위해 Idempotency는 매우 중요하다.

Idempotency는 Side Effect Control과 연결된다.

---

### [핵심]

- Idempotency는 중복 실행 안전성 기준이다.
- 검색과 읽기 작업은 대체로 Idempotent하다.
- 이메일 발송, 결제, 삭제, 배포는 Non-Idempotent하다.
- Non-Idempotent 작업은 Retry에 주의한다.
- Request ID 또는 Deduplication Key를 사용할 수 있다.
- Tool Result에 requestId를 포함할 수 있다.
- 실패 후 실제 실행 여부를 확인해야 한다.
- Side Effect Tool은 Idempotency 확인 없이 자동 Retry하지 않는다.

---

### [실무]

Idempotency 분류:

| 작업        | Idempotency       | 설명                                 |
| ----------- | ----------------- | ------------------------------------ |
| RAG 검색    | Idempotent        | 반복 조회 안전                       |
| 파일 읽기   | 대체로 Idempotent | 파일 변경 시 결과는 달라질 수 있음   |
| DB SELECT   | 대체로 Idempotent | 데이터 변경 시 결과는 달라질 수 있음 |
| 테스트 실행 | 조건부 Idempotent | 테스트가 외부 상태를 바꾸면 위험     |
| 파일 쓰기   | 조건부 Idempotent | 동일 내용 저장은 조건부 안전         |
| 이메일 발송 | Non-Idempotent    | 중복 발송 위험                       |
| 결제 요청   | Non-Idempotent    | 중복 결제 위험                       |
| DB INSERT   | Non-Idempotent    | 중복 row 생성 위험                   |
| 파일 삭제   | Non-Idempotent    | 복구 불가 위험                       |
| 배포 실행   | Non-Idempotent    | 환경 변경 위험                       |

Non-Idempotent Tool 실행 시 권장:

```text
Generate Request ID
→ Check Deduplication Key
→ Preview Action
→ Human Confirmation
→ Execute Once
→ Store Execution Result
```

---

### [FAQ]

Q. Idempotency가 뭐야?
A. 같은 Tool 호출을 여러 번 실행해도 결과가 안전하게 동일한지 판단하는 기준이다.

Q. Idempotency는 왜 중요해?
A. Retry나 중복 실행 시 이메일 중복 발송, 결제 중복 요청, DB 중복 변경을 막기 위해 중요하다.

Q. 검색 Tool은 Idempotent해?
A. 대체로 그렇다. 같은 query를 반복 검색해도 시스템 상태를 바꾸지 않는다.

Q. 이메일 발송 Tool은 Idempotent해?
A. 아니다. 같은 요청을 반복하면 이메일이 중복 발송될 수 있다.

Q. Non-Idempotent Tool은 어떻게 처리해?
A. Request ID, Deduplication Key, Preview, Human Confirmation, 실행 결과 저장을 적용한다.

---

# 10. Output Validation

## 10.1 Output Validation Concept

### [개념]

Output Validation은 Tool Execution 결과가 기대한 Return Type과 품질 기준을 만족하는지 확인하는 단계이다.

외부 API, 파일, DB, 코드 실행 결과도 잘못되거나 불완전할 수 있다.

Tool Result는 LLM Context 또는 다음 Agent에게 전달되기 전에 검증되어야 한다.

Output Validation은 Result Mapping의 직전 단계이다.

---

### [핵심]

- Output Validation은 Tool Execution 결과 검증이다.
- status, data, error 구조를 확인한다.
- 필수 metadata가 있는지 확인한다.
- 외부 API 응답 schema를 검증한다.
- DB 조회 결과 수량 제한을 확인한다.
- 파일 결과 크기를 제한한다.
- 민감정보가 포함되어 있는지 확인한다.
- 너무 큰 결과는 요약하거나 제한한다.
- Output Validation 이후 Tool Result Mapping을 수행한다.

---

### [실무]

Output Validation Flow:

```text
Raw Tool Output
→ Return Type Validation
→ Size Limit Check
→ Sensitive Data Masking
→ Source Metadata Check
→ Result Mapping
→ Tool Message
```

검증 대상:

| 대상         | 검증                                    |
| ------------ | --------------------------------------- |
| API Response | status code, schema, required field     |
| DB Result    | row limit, column whitelist             |
| File Content | size limit, extension, secret 포함 여부 |
| Code Output  | stdout/stderr 크기, error 포함 여부     |
| RAG Result   | source, score, chunk length             |
| Test Result  | pass/fail, error summary                |

큰 결과 처리:

```text
Large Result
→ Summarize
→ Keep Source Metadata
→ Return Relevant Fields Only
```

민감정보 처리:

```text
Raw Output Contains Secret
→ Mask Secret
→ Log Safe Summary Only
→ Do Not Expose Raw Output
```

---

### [FAQ]

Q. Output Validation이 뭐야?
A. Tool 실행 결과가 기대한 구조와 안전 기준을 만족하는지 확인하는 단계다.

Q. Tool Result도 검증해야 해?
A. 그렇다. 외부 API, 파일, DB 결과도 잘못됐거나 민감정보를 포함할 수 있다.

Q. 큰 Tool Result는 어떻게 처리해?
A. 필요한 필드만 남기고 요약하며 source metadata는 유지한다.

Q. 민감정보가 Tool Result에 있으면 어떻게 해?
A. 마스킹하고 Raw Output을 그대로 LLM이나 사용자에게 전달하지 않는다.

Q. RAG Search Result는 무엇을 검증해?
A. source, score, chunk length, domain filter, relevance를 확인한다.

---

# 11. Tool Message

## 11.1 Tool Message Concept

### [개념]

Tool Message는 Tool Execution 결과를 LLM Context 또는 다음 Agent에게 전달하는 메시지이다.

Tool Message는 LLM이 Final Answer를 생성하거나 Review Agent가 결과를 검증하는 근거가 된다.

Tool Message는 성공 결과뿐 아니라 실패, 차단, 일부 성공 결과도 전달할 수 있다.

---

### [핵심]

- Tool Message는 Tool Result를 전달한다.
- Tool Message는 Tool Call ID를 포함할 수 있다.
- Tool Message는 Tool Name을 포함한다.
- Tool Message는 status를 포함한다.
- Tool Message는 structured data를 포함한다.
- Tool Message는 error result를 포함할 수 있다.
- Tool Message는 blocked / partial result를 포함할 수 있다.
- Tool Message는 source reference를 포함하는 것이 좋다.
- Tool Message는 너무 길면 요약해야 한다.

---

### [실무]

Tool Message 예시:

```json
{
  "toolCallId": "call_001",
  "toolName": "search_rag_documents",
  "status": "success",
  "data": {
    "documents": [
      {
        "title": "Tool Arguments Validation",
        "source": "Tool_Calling_Function_Calling_Part03_Arguments_Validation_Execution.md",
        "score": 0.89
      }
    ]
  },
  "metadata": {
    "executionTimeMs": 120
  }
}
```

실패 Tool Message 예시:

```json
{
  "toolCallId": "call_002",
  "toolName": "read_project_file",
  "status": "error",
  "error": {
    "type": "PermissionError",
    "message": "filePath is outside the allowed directory.",
    "retryable": false
  }
}
```

Tool Message 주의:

- Tool 결과를 왜곡하지 않는다.
- 실패 결과를 숨기지 않는다.
- blocked 결과를 실행 성공처럼 처리하지 않는다.
- partial 결과를 완전 성공처럼 처리하지 않는다.
- 큰 결과를 그대로 넣지 않는다.
- 민감정보를 제거한다.
- source metadata를 유지한다.

---

### [FAQ]

Q. Tool Message가 뭐야?
A. Tool Execution 결과를 LLM Context 또는 다음 Agent에게 전달하는 구조화된 메시지다.

Q. Tool Message에는 무엇이 들어가야 해?
A. Tool Call ID, Tool Name, status, data, error, metadata, source reference가 들어가면 좋다.

Q. Tool 실패도 Tool Message로 전달해?
A. 그렇다. 실패 원인을 구조화해서 LLM이 성공처럼 답하지 않도록 해야 한다.

Q. blocked나 partial도 Tool Message로 전달해?
A. 그렇다. 차단 또는 일부 성공 상태를 다음 Agent가 알 수 있어야 한다.

Q. Tool Message가 너무 길면 어떻게 해?
A. 요약하거나 필요한 필드만 전달하고 source metadata는 유지한다.

---

# 12. Execution Checklist

## 12.1 Tool Execution Checklist

### [개념]

Tool Execution Checklist는 Tool 실행 전후에 검수해야 하는 기준이다.

Tool Execution Checklist는 안전 실행, 오류 처리, 재시도 판단, 결과 구조화를 보장한다.

이 Checklist는 Final Integration Checklist와 연결된다.

---

### [핵심]

- Arguments가 Schema Validation을 통과했는가?
- Business Validation을 통과했는가?
- Permission Check를 통과했는가?
- Risk Check를 통과했는가?
- Human Confirmation이 필요한 작업인가?
- Timeout이 설정되어 있는가?
- Retry 가능 오류인지 구분되는가?
- Idempotency가 확인되었는가?
- Tool Result가 구조화되었는가?
- Output Validation을 수행했는가?
- 민감정보가 제거되었는가?
- Audit Log가 필요한 작업인가?
- Tool Message가 다음 Agent에게 전달 가능한가?

---

### [실무]

Tool Execution Checklist:

```md
### [Checklist]

- [ ] Tool Arguments가 존재하는가?
- [ ] Required Field가 모두 존재하는가?
- [ ] 빈 문자열 / null 값이 허용 조건에 맞는가?
- [ ] Type Check를 통과했는가?
- [ ] Range Check를 통과했는가?
- [ ] Enum Check를 통과했는가?
- [ ] Business Validation을 통과했는가?
- [ ] Path Traversal 위험이 없는가?
- [ ] SQL Injection 위험이 없는가?
- [ ] Command Injection 위험이 없는가?
- [ ] Permission Check를 통과했는가?
- [ ] Risk Level이 확인되었는가?
- [ ] Human Confirmation이 필요한지 확인했는가?
- [ ] Timeout이 설정되었는가?
- [ ] Retry 정책이 적용되었는가?
- [ ] Idempotency가 확인되었는가?
- [ ] Tool Result가 success / error / blocked / partial을 구분하는가?
- [ ] Output Validation을 수행했는가?
- [ ] 민감정보를 마스킹했는가?
- [ ] Tool Message가 구조화되었는가?
- [ ] 필요한 경우 Audit Log를 남겼는가?
```

Checklist 실패 시 Tool을 실행하지 않는다.

---

### [FAQ]

Q. Tool Execution Checklist는 왜 필요해?
A. Tool 실행 전후의 검증 누락을 막고 안전한 Agent Runtime을 만들기 위해 필요하다.

Q. Checklist 중 가장 중요한 항목은?
A. Arguments Validation, Permission Check, Risk Check, Timeout, Output Validation이다.

Q. Checklist 실패 시 실행해도 돼?
A. 안 된다. 실패 항목을 수정하거나 사용자 확인을 받은 뒤 실행해야 한다.

Q. 위험 작업은 Checklist 외에 뭐가 필요해?
A. Preview, Human Confirmation, Audit Log, Undo 가능 여부 확인이 필요하다.

Q. Tool Execution Checklist는 누가 사용해?
A. Agent Runtime, Backend Agent, Review Agent, AI/ML Agent가 Tool 연결과 실행 검수에 사용한다.

---

# Retrieval Queries

### [FAQ]

Q. Tool Arguments가 뭐야?
A. LLM이 Tool 실행을 위해 생성하는 입력값이며, 실행 전 반드시 검증해야 하는 값이다.

Q. Tool Arguments는 왜 신뢰하면 안 돼?
A. LLM이 누락, 타입 오류, 범위 오류, 위험한 파일 경로, 잘못된 SQL 같은 값을 생성할 수 있기 때문이다.

Q. Tool Arguments 검증 순서는?
A. Required Field Check → Type Check → Range Check → Enum Check → Business Validation → Permission Check → Risk Check 순서가 좋다.

Q. Schema Validation이 뭐야?
A. Tool Arguments가 JSON Schema의 type, required, enum, range 조건에 맞는지 확인하는 검증이다.

Q. Schema Validation만으로 충분해?
A. 아니다. Business Validation, Permission Check, Risk Check가 추가로 필요하다.

Q. Business Validation이 뭐야?
A. Tool Arguments가 업무 규칙, 허용 범위, 실행 조건에 맞는지 확인하는 검증이다.

Q. filePath 검증은 왜 필요해?
A. Path Traversal, 허용 디렉터리 밖 접근, 민감 파일 접근을 막기 위해 필요하다.

Q. Permission Check가 뭐야?
A. 현재 Agent 또는 User가 해당 Tool을 실행할 권한이 있는지 확인하는 절차다.

Q. Agent별 Tool 권한은 왜 분리해?
A. 최소 권한 원칙으로 위험 작업과 오작동 피해를 제한하기 위해서다.

Q. Risk Check가 뭐야?
A. Tool 실행이 외부 시스템, 파일, DB, 비용, 배포 환경에 영향을 주는지 판단하는 절차다.

Q. Risk Check 결과 blocked면 무엇을 의미해?
A. Tool이 실패한 것이 아니라 사용자 승인이나 정책 확인 전까지 실행이 차단된 상태를 의미한다.

Q. High Risk Tool은 어떻게 처리해?
A. Human Confirmation, Preview, Audit Log, Undo 가능 여부 확인 후 실행한다.

Q. Tool Execution은 누가 수행해?
A. LLM이 아니라 Agent Runtime 또는 Backend System이 수행한다.

Q. Tool Execution 전 반드시 필요한 검증은?
A. Schema Validation, Business Validation, Permission Check, Risk Check가 필요하다.

Q. Tool Execution에 Timeout이 필요한 이유는?
A. 무한 실행, 외부 API 지연, 코드 무한 루프, 리소스 낭비를 막기 위해 필요하다.

Q. TimeoutError는 항상 Retry 가능해?
A. 아니다. Side Effect가 있는 작업은 실제 실행 여부를 확인하지 않고 Retry하면 중복 실행 위험이 있다.

Q. Retry는 언제 가능해?
A. 네트워크 오류, 429 Rate Limit, 5xx 오류, 일부 Timeout처럼 일시적 오류에서 제한적으로 가능하다.

Q. Retry하면 안 되는 오류는?
A. ValidationError, PermissionError, AuthenticationError, Dangerous Operation, Idempotency 없는 Non-Idempotent 작업은 Retry하면 안 된다.

Q. Idempotency가 뭐야?
A. 같은 Tool 호출을 여러 번 실행해도 결과가 안전하게 동일한지 판단하는 기준이다.

Q. Non-Idempotent Tool 예시는?
A. 이메일 발송, 결제 요청, DB INSERT, 파일 삭제, 배포 실행이다.

Q. Output Validation이 뭐야?
A. Tool 실행 결과가 기대한 Return Type과 안전 기준을 만족하는지 확인하는 단계다.

Q. Tool Result도 검증해야 해?
A. 그렇다. 외부 API, 파일, DB, 코드 실행 결과도 잘못되거나 민감정보를 포함할 수 있다.

Q. Tool Message가 뭐야?
A. Tool Execution 결과를 LLM Context 또는 다음 Agent에게 전달하는 구조화된 메시지다.

Q. Tool 실패도 Tool Message로 전달해야 해?
A. 그렇다. 실패 상태와 원인을 전달해야 LLM이 성공처럼 답하지 않는다.

Q. blocked나 partial도 Tool Message로 전달해야 해?
A. 그렇다. 다음 Agent가 차단 상태나 일부 성공 상태를 정확히 알 수 있어야 한다.

Q. Tool Execution Checklist에는 무엇이 들어가야 해?
A. Arguments Validation, Permission Check, Risk Check, Timeout, Retry, Idempotency, Output Validation, Audit Log 확인이 들어가야 한다.

Q. Tool Arguments Validation의 최종 목표는 뭐야?
A. LLM이 생성한 입력값을 안전하게 검증해 잘못된 Tool Execution과 위험 작업을 방지하는 것이다.
