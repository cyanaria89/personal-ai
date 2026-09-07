# Tool Calling & Function Calling Part07 - Tool Types, Testing & Troubleshooting

---

# 1. Tool Type Design

## 1.1 Tool Type Concept

### [개념]

Tool Type Design은 Agent가 사용할 Tool을 목적, 위험도, Side Effect, 권한 기준에 따라 분류하는 설계이다.

Tool Calling 시스템에서는 모든 Tool을 동일하게 취급하지 않는다.

Tool Type에 따라 Schema, Validation, Permission, Risk Level, Human Confirmation, Testing 기준이 달라진다.

Part07은 Tool Calling & Function Calling 문서 세트의 최종 통합 문서로, Tool Type 분류, Tool Testing, Troubleshooting, Common Mistakes, Final Integration Checklist를 정리한다.

---

### [핵심]

- Tool Type은 Tool의 목적과 위험도를 기준으로 분류한다.
- RAG Search Tool은 문서 검색용 Tool이다.
- File Tool은 파일 읽기 / 쓰기 / 삭제 Tool이다.
- API Tool은 외부 API 호출 Tool이다.
- Database Tool은 DB 조회 / 변경 Tool이다.
- Code Execution Tool은 코드 실행 Tool이다.
- Test Execution Tool은 테스트 실행 Tool이다.
- Observability Tool은 로그 / metric / trace 확인 Tool이다.
- Deployment Tool은 배포 실행 또는 배포 상태 확인 Tool이다.
- Tool Type별 riskLevel, sideEffect, permissionLevel을 다르게 정의한다.

---

### [실무]

대표 Tool Type:

| Tool Type           | 목적             |     기본 Risk | Side Effect |
| ------------------- | ---------------- | ------------: | ----------: |
| RAG Search Tool     | 문서 검색        |           low |       false |
| File Read Tool      | 파일 읽기        |           low |       false |
| File Write Tool     | 파일 쓰기 / 수정 | medium ~ high |        true |
| File Delete Tool    | 파일 삭제        |          high |        true |
| API Tool            | 외부 API 호출    |        medium |      조건부 |
| Database Read Tool  | DB 조회          |        medium |       false |
| Database Write Tool | DB 변경          |          high |        true |
| Code Execution Tool | 코드 실행        |          high |      조건부 |
| Test Execution Tool | 테스트 실행      |        medium |      조건부 |
| Observability Tool  | 로그 / 상태 확인 |  low ~ medium |       false |
| Email Send Tool     | 이메일 발송      |          high |        true |
| Deployment Tool     | 배포 실행        |          high |        true |

Tool Type별 기본 설계 기준:

```text
Tool Type
→ Tool Definition
→ Tool Schema
→ Arguments Validation
→ Permission Check
→ Risk Check
→ Execution Policy
→ Result Mapping
→ Testing
→ Troubleshooting
```

Tool Type을 명확히 분류하면 Agent Tool Routing과 Safe Execution Policy를 만들기 쉽다.

---

### [FAQ]

Q. Tool Type Design이 뭐야?
A. Agent가 사용할 Tool을 목적, 위험도, Side Effect, 권한 기준에 따라 분류하는 설계다.

Q. Tool Type을 왜 나눠야 해?
A. 검색 Tool, 파일 Tool, DB Tool, 코드 실행 Tool은 위험도와 검증 기준이 다르기 때문이다.

Q. 가장 위험한 Tool Type은 뭐야?
A. File Delete Tool, Database Write Tool, Code Execution Tool, Email Send Tool, Deployment Tool이 고위험이다.

Q. Tool Type별로 다른 테스트가 필요해?
A. 필요하다. Tool의 입력, 출력, 권한, 위험도, 실패 조건이 다르기 때문이다.

Q. Part07의 역할은 뭐야?
A. 전체 Tool Calling 문서 세트의 최종 통합 문서로 Tool Type, Testing, Troubleshooting, Final Checklist를 정리한다.

---

# 2. RAG Search Tool

## 2.1 RAG Search Tool Concept

### [개념]

RAG Search Tool은 사용자의 질문이나 Agent의 작업 요청에 맞는 RAG 문서 Chunk를 검색하는 Tool이다.

RAG Search Tool은 Agent가 Domain Rules, Master Rules, Project Progress, 구현 규칙, 검수 기준을 검색할 때 사용한다.

RAG Search Tool은 일반적으로 Side Effect가 없는 Low Risk Tool이다.

---

### [핵심]

- RAG Search Tool은 문서 검색 Tool이다.
- query는 필수 입력값이다.
- topK는 검색 결과 수를 제한한다.
- domainFilter로 검색 범위를 제한할 수 있다.
- source metadata를 반환해야 한다.
- score 또는 relevance 정보를 포함하는 것이 좋다.
- 검색 결과가 없으면 success + empty data로 반환할 수 있다.
- 검색 결과는 LLM Final Answer의 근거가 된다.
- RAG Search Tool은 PM Agent, Domain Agent, Review Agent가 모두 사용할 수 있다.

---

### [실무]

RAG Search Tool Definition 예시:

```json
{
  "toolName": "search_rag_documents",
  "description": "Search relevant RAG documents for project rules, domain knowledge, implementation patterns, and validation criteria.",
  "parameters": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "Search query for RAG retrieval."
      },
      "topK": {
        "type": "integer",
        "description": "Number of chunks to retrieve.",
        "default": 5,
        "minimum": 1,
        "maximum": 20
      },
      "domainFilter": {
        "type": "string",
        "description": "Optional domain filter such as Backend, Frontend, AI, DevOps, Security."
      }
    },
    "required": ["query"]
  },
  "sideEffect": false,
  "riskLevel": "low",
  "permissionLevel": "read"
}
```

RAG Search Result 예시:

```json
{
  "status": "success",
  "data": {
    "documents": [
      {
        "title": "Tool Arguments Validation",
        "source": "Tool_Calling_Function_Calling_Part03_Arguments_Validation_Execution.md",
        "score": 0.91,
        "chunk": "Tool Arguments는 LLM이 생성하지만 신뢰하지 않는다."
      }
    ]
  },
  "metadata": {
    "toolName": "search_rag_documents",
    "topK": 5,
    "executionTimeMs": 82
  }
}
```

RAG Search Tool 검증 항목:

- query empty check
- topK range check
- domainFilter enum check
- source metadata check
- score threshold check
- result size limit
- duplicate chunk removal
- stale document check if needed

---

### [FAQ]

Q. RAG Search Tool이 뭐야?
A. Agent가 RAG 문서에서 관련 Chunk를 검색하기 위해 사용하는 Tool이다.

Q. RAG Search Tool의 필수 입력값은?
A. query가 필수 입력값이다.

Q. RAG Search 결과에는 무엇이 있어야 해?
A. title, source, score, chunk, metadata가 있으면 좋다.

Q. 검색 결과가 없으면 실패야?
A. 아니다. Tool이 정상 실행되었으면 success와 empty data로 반환할 수 있다.

Q. RAG Search Tool은 어떤 Agent가 사용해?
A. PM Agent, Backend Agent, Frontend Agent, Review Agent, DevOps Agent, AI/ML Agent가 모두 사용할 수 있다.

---

# 3. File Tool

## 3.1 File Tool Concept

### [개념]

File Tool은 프로젝트 파일을 읽거나, 쓰거나, 수정하거나, 삭제하는 Tool이다.

File Tool은 읽기 작업과 변경 작업의 위험도가 크게 다르다.

File Read Tool은 대체로 Low Risk이지만, File Write Tool과 File Delete Tool은 Side Effect가 있으므로 Medium 또는 High Risk로 분류한다.

---

### [핵심]

- File Read Tool은 파일 내용을 읽는다.
- File Write Tool은 파일을 생성하거나 수정한다.
- File Delete Tool은 파일을 삭제한다.
- filePath는 반드시 검증해야 한다.
- Path Traversal을 차단해야 한다.
- 허용 Workspace 밖 접근을 차단해야 한다.
- Secret 파일 접근을 제한해야 한다.
- File Write / Delete는 Human Confirmation이 필요할 수 있다.
- File Tool 결과에는 filePath, operation, metadata를 포함한다.

---

### [실무]

File Read Tool Definition 예시:

```json
{
  "toolName": "read_project_file",
  "description": "Read a project file inside the allowed workspace. This tool does not modify files.",
  "parameters": {
    "type": "object",
    "properties": {
      "filePath": {
        "type": "string",
        "description": "Target file path inside the allowed workspace."
      }
    },
    "required": ["filePath"]
  },
  "sideEffect": false,
  "riskLevel": "low",
  "permissionLevel": "read"
}
```

File Write Tool Definition 예시:

```json
{
  "toolName": "write_project_file",
  "description": "Write or overwrite a project file after path validation, preview, and confirmation when required.",
  "parameters": {
    "type": "object",
    "properties": {
      "filePath": {
        "type": "string",
        "description": "Target file path inside the allowed workspace."
      },
      "content": {
        "type": "string",
        "description": "Content to write."
      },
      "mode": {
        "type": "string",
        "enum": ["create", "append", "overwrite"],
        "description": "File write mode."
      }
    },
    "required": ["filePath", "content", "mode"]
  },
  "sideEffect": true,
  "riskLevel": "medium",
  "permissionLevel": "write",
  "requiresConfirmation": "when mode is overwrite or target exists"
}
```

File Tool Validation:

```text
filePath 입력
→ Normalize Path
→ Check Path Traversal
→ Check Allowed Workspace
→ Check File Extension
→ Check Secret Pattern
→ Check Permission
→ Check Risk
→ Execute
```

위험 filePath 예시:

```text
../../.env
/home/user/.ssh/id_rsa
/etc/passwd
C:\Users\user\.ssh\id_rsa
```

---

### [FAQ]

Q. File Tool이 뭐야?
A. 프로젝트 파일을 읽거나 쓰거나 삭제하는 Tool이다.

Q. File Read Tool은 안전해?
A. 비교적 안전하지만 허용 경로, Secret 파일 접근, 파일 크기 제한은 검증해야 한다.

Q. File Write Tool은 왜 위험해?
A. 기존 파일을 덮어쓰거나 잘못된 내용을 저장해 프로젝트를 손상시킬 수 있기 때문이다.

Q. File Delete Tool은 자동 실행해도 돼?
A. 안 된다. 삭제 작업은 High Risk로 보고 Human Confirmation을 요구해야 한다.

Q. File Tool에서 가장 중요한 검증은?
A. filePath 검증, Path Traversal 차단, 허용 Workspace 확인, Secret 접근 차단이다.

---

# 4. API Tool

## 4.1 API Tool Concept

### [개념]

API Tool은 외부 서비스 또는 내부 Backend API를 호출하는 Tool이다.

API Tool은 외부 네트워크, 인증, Rate Limit, 응답 Schema 변경, 비용 발생 가능성을 고려해야 한다.

API Tool은 단순 조회일 수도 있고, 외부 시스템 상태를 변경하는 Side Effect Tool일 수도 있다.

---

### [핵심]

- API Tool은 HTTP API 또는 외부 서비스를 호출한다.
- endpoint, method, parameters를 검증해야 한다.
- 허용된 domain과 endpoint만 호출한다.
- API Key와 Token은 노출하지 않는다.
- Timeout을 설정한다.
- Rate Limit을 처리한다.
- Response Schema를 검증한다.
- API 오류는 표준 Error Type으로 Mapping한다.
- Side Effect가 있는 API는 Human Confirmation이 필요할 수 있다.

---

### [실무]

API Tool Definition 예시:

```json
{
  "toolName": "call_external_api",
  "description": "Call an allowed external API endpoint with validated parameters and return a structured result.",
  "parameters": {
    "type": "object",
    "properties": {
      "endpointKey": {
        "type": "string",
        "description": "Predefined endpoint key instead of raw URL.",
        "enum": ["weather_current", "tour_api_search", "payment_status"]
      },
      "method": {
        "type": "string",
        "enum": ["GET", "POST"]
      },
      "params": {
        "type": "object",
        "description": "Validated request parameters."
      }
    },
    "required": ["endpointKey", "method"]
  },
  "sideEffect": "depends_on_endpoint",
  "riskLevel": "medium",
  "permissionLevel": "execute"
}
```

API Tool 실행 Flow:

```text
Validate endpointKey
→ Resolve Allowed Endpoint
→ Validate Method
→ Validate Params
→ Attach Secret from Secure Store
→ Execute with Timeout
→ Validate Response Schema
→ Map Result or Error
```

API Tool에서 Raw URL 직접 입력을 허용하지 않는 것이 안전하다.

권장:

```text
endpointKey = "tour_api_search"
```

비권장:

```text
url = "https://unknown-site.example.com/api"
```

HTTP Error Mapping:

| HTTP Status     | Error Type          |
| --------------- | ------------------- |
| 400             | ValidationError     |
| 401             | AuthenticationError |
| 403             | PermissionError     |
| 404             | NotFoundError       |
| 408             | TimeoutError        |
| 429             | RateLimitError      |
| 500 / 502 / 503 | ExternalApiError    |

---

### [FAQ]

Q. API Tool이 뭐야?
A. 외부 서비스나 내부 Backend API를 호출하는 Tool이다.

Q. API Tool에서 Raw URL을 받아도 돼?
A. 권장하지 않는다. predefined endpointKey를 사용해 허용된 endpoint만 호출하는 것이 안전하다.

Q. API Key는 Tool Arguments에 넣어도 돼?
A. 안 된다. API Key와 Token은 Secure Store에서 Runtime이 주입해야 한다.

Q. API Tool에서 가장 중요한 검증은?
A. endpoint 허용 여부, method 검증, params 검증, Timeout, Response Schema 검증이다.

Q. API Tool 오류는 어떻게 처리해?
A. HTTP Status와 응답을 표준 Error Type으로 Mapping한다.

---

# 5. Database Tool

## 5.1 Database Tool Concept

### [개념]

Database Tool은 데이터베이스를 조회하거나 변경하는 Tool이다.

Database Tool은 Read Tool과 Write Tool을 명확히 분리해야 한다.

Database Write Tool은 데이터 상태를 변경하므로 High Risk Tool로 분류하고, Permission Check, Dry Run, Transaction, Human Confirmation을 적용한다.

---

### [핵심]

- Database Read Tool과 Database Write Tool을 분리한다.
- SELECT는 Read Tool로 처리한다.
- INSERT, UPDATE, DELETE는 Write Tool로 처리한다.
- Raw SQL 직접 실행은 제한한다.
- 허용된 table과 column만 접근한다.
- Query Timeout을 설정한다.
- Row Limit을 적용한다.
- Database Write는 Transaction을 사용한다.
- DELETE / UPDATE without WHERE는 차단한다.
- Database Write는 Human Confirmation이 필요하다.

---

### [실무]

Database Read Tool 예시:

```json
{
  "toolName": "query_database_read",
  "description": "Run a validated read-only database query against allowed tables with row limit.",
  "parameters": {
    "type": "object",
    "properties": {
      "queryKey": {
        "type": "string",
        "description": "Predefined read query key.",
        "enum": ["find_user_by_id", "list_recent_posts", "count_notifications"]
      },
      "params": {
        "type": "object",
        "description": "Query parameters."
      },
      "limit": {
        "type": "integer",
        "default": 100,
        "minimum": 1,
        "maximum": 500
      }
    },
    "required": ["queryKey"]
  },
  "sideEffect": false,
  "riskLevel": "medium",
  "permissionLevel": "read"
}
```

Database Write Tool 예시:

```json
{
  "toolName": "execute_database_write",
  "description": "Execute an approved database write operation using predefined mutation keys, transaction, dry run, and user confirmation.",
  "parameters": {
    "type": "object",
    "properties": {
      "mutationKey": {
        "type": "string",
        "enum": ["update_user_status", "delete_expired_tokens"]
      },
      "params": {
        "type": "object"
      },
      "dryRun": {
        "type": "boolean",
        "default": true
      }
    },
    "required": ["mutationKey", "params"]
  },
  "sideEffect": true,
  "riskLevel": "high",
  "permissionLevel": "admin",
  "requiresConfirmation": true
}
```

Database Write Flow:

```text
Validate mutationKey
→ Validate params
→ Dry Run
→ Estimate affected rows
→ Human Confirmation
→ Begin Transaction
→ Execute
→ Verify Result
→ Commit or Rollback
→ Audit Log
```

Dangerous SQL Pattern:

```text
DELETE FROM users
UPDATE users SET role = 'ADMIN'
DROP TABLE users
TRUNCATE TABLE
```

---

### [FAQ]

Q. Database Tool은 어떻게 나눠야 해?
A. Database Read Tool과 Database Write Tool을 분리해야 한다.

Q. Raw SQL을 Tool Arguments로 받아도 돼?
A. 권장하지 않는다. queryKey나 mutationKey 기반으로 허용된 쿼리만 실행하는 것이 안전하다.

Q. Database Write Tool은 왜 High Risk야?
A. 실제 데이터 상태를 변경하고 복구가 어려울 수 있기 때문이다.

Q. DELETE without WHERE는 어떻게 처리해?
A. DangerousOperationBlocked로 차단해야 한다.

Q. Database Write 실행 전 무엇이 필요해?
A. Dry Run, affected rows 확인, Human Confirmation, Transaction, Audit Log가 필요하다.

---

# 6. Code Execution Tool

## 6.1 Code Execution Tool Concept

### [개념]

Code Execution Tool은 Agent가 생성하거나 사용자가 제공한 코드를 제한된 환경에서 실행하는 Tool이다.

Code Execution Tool은 매우 강력하지만 보안 위험이 크다.

코드는 파일 시스템, 네트워크, 환경 변수, Secret, CPU, Memory에 영향을 줄 수 있으므로 Sandbox와 Resource Limit이 필수이다.

---

### [핵심]

- Code Execution Tool은 High Risk Tool이다.
- Sandbox에서 실행해야 한다.
- Timeout을 설정해야 한다.
- CPU / Memory 제한을 설정해야 한다.
- Network 접근을 제한한다.
- File System 접근을 제한한다.
- Secret / Environment Variable 접근을 차단한다.
- stdout / stderr 크기를 제한한다.
- 실행 결과는 구조화한다.
- 위험 코드 패턴을 감지한다.

---

### [실무]

Code Execution Tool Definition 예시:

```json
{
  "toolName": "execute_code_sandbox",
  "description": "Execute code in a restricted sandbox with timeout, memory limit, and no secret access.",
  "parameters": {
    "type": "object",
    "properties": {
      "language": {
        "type": "string",
        "enum": ["python", "javascript", "bash"]
      },
      "code": {
        "type": "string",
        "description": "Code to execute in sandbox."
      },
      "timeoutMs": {
        "type": "integer",
        "default": 10000,
        "minimum": 1000,
        "maximum": 60000
      }
    },
    "required": ["language", "code"]
  },
  "sideEffect": "sandboxed",
  "riskLevel": "high",
  "permissionLevel": "execute",
  "requiresConfirmation": "when filesystem, network, or shell access is requested"
}
```

Sandbox 기준:

| 제한          | 기준                                |
| ------------- | ----------------------------------- |
| Timeout       | 필수                                |
| Memory Limit  | 필수                                |
| CPU Limit     | 필수                                |
| Network       | 기본 차단                           |
| File Write    | 기본 차단 또는 임시 디렉터리만 허용 |
| Env Access    | Secret 차단                         |
| Process Spawn | 제한                                |
| Output Size   | 제한                                |

위험 코드 패턴:

```text
os.remove
rm -rf
subprocess
eval
exec
curl | sh
open('/etc/passwd')
cat ~/.ssh/id_rsa
```

Code Execution Result 예시:

```json
{
  "status": "success",
  "data": {
    "stdout": "result: 42",
    "stderr": "",
    "exitCode": 0
  },
  "metadata": {
    "toolName": "execute_code_sandbox",
    "language": "python",
    "executionTimeMs": 214
  }
}
```

---

### [FAQ]

Q. Code Execution Tool이 뭐야?
A. Agent가 코드나 스크립트를 제한된 환경에서 실행하는 Tool이다.

Q. Code Execution Tool은 왜 위험해?
A. 코드가 파일, 네트워크, Secret, 리소스에 접근할 수 있기 때문이다.

Q. Code Execution Tool에는 무엇이 필요해?
A. Sandbox, Timeout, Memory Limit, Network 차단, File System 제한, Secret 차단이 필요하다.

Q. Bash 실행은 안전해?
A. 기본적으로 위험하다. Shell Command는 시스템에 직접 영향을 줄 수 있으므로 강한 제한이 필요하다.

Q. Code Execution Result에는 무엇을 포함해?
A. stdout, stderr, exitCode, executionTimeMs, language, errorType을 포함하는 것이 좋다.

---

# 7. Tool Testing

## 7.1 Tool Testing Concept

### [개념]

Tool Testing은 Tool Definition, Tool Schema, Arguments Validation, Permission Check, Risk Check, Tool Execution, Result Mapping, Error Handling이 정상 동작하는지 검증하는 절차이다.

Tool Testing은 Agent에 Tool을 연결하기 전에 반드시 수행해야 한다.

Tool Testing은 Unit Test, Integration Test, Security Test, Failure Test로 나눌 수 있다.

---

### [핵심]

- Tool Testing은 Tool 연결 전 필수이다.
- Tool Definition이 명확한지 테스트한다.
- JSON Schema Validation을 테스트한다.
- Required Field 누락을 테스트한다.
- PermissionError를 테스트한다.
- Risk Check와 blocked result를 테스트한다.
- Timeout과 Retry를 테스트한다.
- Result Mapping을 테스트한다.
- Error Handling을 테스트한다.
- High Risk Tool은 Human Confirmation 테스트가 필요하다.

---

### [실무]

Tool Testing 유형:

| Test Type           | 목적                                          |
| ------------------- | --------------------------------------------- |
| Schema Test         | Arguments 형식 검증                           |
| Validation Test     | Required / Type / Enum / Range 검증           |
| Permission Test     | Agent 권한 검증                               |
| Risk Test           | Risk Level / Side Effect 검증                 |
| Confirmation Test   | Human Confirmation 필요 여부 검증             |
| Execution Test      | Tool 실행 성공 검증                           |
| Error Test          | 실패 조건 검증                                |
| Timeout Test        | Timeout 처리 검증                             |
| Retry Test          | Retry 정책 검증                               |
| Result Mapping Test | 표준 Tool Result 변환 검증                    |
| Security Test       | Path Traversal / Injection / Secret 노출 검증 |

테스트 케이스 예시:

```md
### Tool Test Case

- Tool: read_project_file
- Case: filePath missing
- Input: {}
- Expected:
  - status: error
  - error.type: ValidationError
  - execution: not executed
```

High Risk Tool 테스트 예시:

```md
### Tool Test Case

- Tool: write_project_file
- Case: overwrite existing file
- Input:
  - filePath: docs/tool.md
  - mode: overwrite
- Expected:
  - status: blocked
  - reason: HumanConfirmationRequired
  - execution: not executed before confirmation
```

---

### [FAQ]

Q. Tool Testing이 뭐야?
A. Tool Definition, Validation, Permission, Risk, Execution, Result Mapping이 정상 동작하는지 검증하는 절차다.

Q. Tool Testing은 언제 해?
A. Agent Runtime에 Tool을 연결하기 전에 수행해야 한다.

Q. Tool Testing에서 가장 중요한 것은?
A. Validation, Permission, Risk Check, Error Handling, Result Mapping이다.

Q. High Risk Tool은 무엇을 테스트해야 해?
A. Human Confirmation 전에는 실행되지 않고 blocked result를 반환하는지 테스트해야 한다.

Q. Tool Testing 실패 시 어떻게 해?
A. Tool Definition, Schema, Runtime Policy, Result Mapping을 수정한 뒤 다시 테스트한다.

---

# 8. Tool Troubleshooting

## 8.1 Tool Troubleshooting Concept

### [개념]

Tool Troubleshooting은 Tool Calling 과정에서 발생하는 문제를 원인별로 분석하고 수정하는 절차이다.

Tool 문제는 Tool Choice 오류, Arguments 오류, Permission 오류, Risk 오류, Execution 오류, Result Mapping 오류, Handoff 오류로 나눌 수 있다.

Troubleshooting은 Tool Observability와 Audit Log를 기반으로 수행한다.

---

### [핵심]

- Tool Choice 오류는 Description이 모호할 때 발생한다.
- Arguments 오류는 Schema가 복잡하거나 설명이 부족할 때 발생한다.
- ValidationError는 필수값, 타입, enum, range 문제다.
- PermissionError는 Agent 권한 또는 허용 범위 문제다.
- blocked는 위험 작업 승인 또는 정책 문제다.
- TimeoutError는 실행 시간 또는 외부 의존성 문제다.
- ExternalApiError는 외부 API, 인증, 응답 Schema 문제다.
- Result Mapping 오류는 Raw Output 처리 문제다.
- Handoff 오류는 Agent 간 전달 정보 부족 문제다.

---

### [실무]

Troubleshooting Table:

| 증상                 | 가능 원인               | 조치                                |
| -------------------- | ----------------------- | ----------------------------------- |
| 잘못된 Tool 선택     | Description 모호        | Tool Description 수정               |
| Arguments 누락       | required 불명확         | Schema와 description 보강           |
| enum 오류            | 허용값 불명확           | enum description 추가               |
| ValidationError 반복 | Schema 과도하게 복잡    | Parameters 단순화                   |
| PermissionError      | Agent 권한 부족         | Agent Permission 재검토             |
| blocked 반복         | High Risk 정책          | Preview / Confirmation Flow 확인    |
| TimeoutError         | Tool 지연 / 무한 실행   | Timeout, query, resource limit 조정 |
| RateLimitError       | 호출량 초과             | Backoff, cache, batching 적용       |
| ExternalApiError     | 외부 API 장애           | fallback, response mapping 확인     |
| Raw Exception 노출   | Error Mapping 누락      | Safe Error Message 적용             |
| partial 누락         | Batch 결과 처리 미흡    | successItems / failedItems 분리     |
| Handoff 누락         | Agent Handoff 구조 부족 | toolResults / knownIssues 추가      |

Troubleshooting Flow:

```text
Issue Detected
→ Check Tool Observability
→ Check Tool Result status
→ Check Error Type
→ Check Arguments
→ Check Permission
→ Check Risk Policy
→ Check Execution Log
→ Check Result Mapping
→ Fix Tool Definition or Runtime Policy
```

---

### [FAQ]

Q. Tool Troubleshooting이 뭐야?
A. Tool Calling 과정에서 발생한 문제를 원인별로 분석하고 수정하는 절차다.

Q. 잘못된 Tool이 선택되면 무엇을 확인해?
A. Tool Name과 Tool Description이 모호하지 않은지 확인한다.

Q. ValidationError가 반복되면 어떻게 해?
A. JSON Schema를 단순화하고 Field Description과 Required Fields를 명확히 한다.

Q. PermissionError가 발생하면 어떻게 해?
A. Agent Permission과 allowedTools / deniedTools 정책을 확인한다.

Q. Tool 실패 원인을 어디서 확인해?
A. Tool Result, Error Type, Tool Observability, Audit Log, Agent Handoff에서 확인한다.

---

# 9. Common Mistakes

## 9.1 Common Tool Calling Mistakes

### [개념]

Common Mistakes는 Tool Calling과 Function Calling 설계에서 자주 발생하는 오류 패턴이다.

이 오류들은 Tool Choice 실패, 잘못된 Arguments, 위험 작업 자동 실행, Error Handling 실패, Agent Handoff 누락으로 이어진다.

Common Mistakes는 Tool Testing과 Review Agent 검수에서 반복적으로 확인해야 한다.

---

### [핵심]

- Tool Description을 너무 짧게 작성한다.
- Tool Name이 모호하다.
- JSON Schema가 너무 느슨하다.
- JSON Schema가 너무 복잡하다.
- Required Fields가 불명확하다.
- Tool Arguments를 검증하지 않는다.
- Permission Check 없이 Tool을 실행한다.
- High Risk Tool을 자동 실행한다.
- Raw Exception을 그대로 노출한다.
- Tool Result status를 구분하지 않는다.
- blocked / partial 상태를 success로 처리한다.
- Agent Handoff에 Tool Result를 포함하지 않는다.

---

### [실무]

Common Mistakes Table:

| 실수                           | 문제                  | 수정                        |
| ------------------------------ | --------------------- | --------------------------- |
| `description: "Use this tool"` | Tool Choice 오류      | 사용 시점과 제한 조건 작성  |
| `toolName: "manager"`          | 의미 불명확           | 동사 + 대상 이름 사용       |
| required 누락                  | Arguments 누락        | requiredFields 명시         |
| Raw URL 허용                   | SSRF / 외부 호출 위험 | endpointKey 사용            |
| Raw SQL 허용                   | DB 손상 위험          | queryKey / mutationKey 사용 |
| filePath 검증 없음             | Path Traversal 위험   | allowed workspace 검증      |
| Timeout 없음                   | 무한 실행 위험        | Tool별 Timeout 설정         |
| Retry 무제한                   | 외부 부하 / 중복 실행 | maxRetry + Backoff          |
| Result 문자열 반환             | 후속 처리 불안정      | status/data/error 구조화    |
| Error 숨김                     | LLM 오답              | Error Result 반환           |
| Secret 로그 출력               | 보안 사고             | Masking 적용                |
| Review 생략                    | 품질 저하             | Review Loop 적용            |

위험 작업 실수는 Part05 Safe Execution 기준으로 재검토한다.

Agent Routing 실수는 Part06 Agent Tool Routing 기준으로 재검토한다.

---

### [FAQ]

Q. Tool Calling에서 가장 흔한 실수는?
A. Tool Description을 모호하게 작성하고, LLM이 생성한 Arguments를 검증 없이 실행하는 것이다.

Q. Tool Result를 문자열로만 반환해도 돼?
A. 권장하지 않는다. status, data, error, metadata 구조로 반환해야 한다.

Q. blocked 상태를 success로 처리하면 왜 문제야?
A. 실제 실행되지 않은 작업을 성공으로 오해해 다음 Agent가 잘못된 판단을 할 수 있다.

Q. Raw SQL이나 Raw URL을 허용하면 왜 위험해?
A. SQL Injection, SSRF, 허용되지 않은 외부 호출, 데이터 손상 위험이 있다.

Q. Common Mistakes는 어디서 검수해?
A. Tool Testing, Review Agent 검수, Final Integration Checklist에서 확인한다.

---

# 10. Final Integration Checklist

## 10.1 Final Checklist

### [개념]

Final Integration Checklist는 Tool Calling & Function Calling 문서 세트의 최종 통합 검수 기준이다.

이 Checklist는 Tool을 실제 Agent Runtime에 연결하기 전, 전체 설계가 안전하고 일관적인지 확인하는 데 사용한다.

Part07의 Final Integration Checklist는 Part01 ~ Part06의 내용을 최종적으로 점검한다.

---

### [핵심]

- Tool Definition이 명확한가?
- Tool Name이 고유하고 목적을 드러내는가?
- Tool Description이 사용 시점과 제한 조건을 포함하는가?
- Parameters가 JSON Schema로 정의되어 있는가?
- Required Fields가 명확한가?
- Tool Arguments Validation이 Runtime에서 수행되는가?
- Permission Check가 Runtime에서 강제되는가?
- Risk Level과 Side Effect가 정의되어 있는가?
- High Risk Tool에 Human Confirmation이 적용되는가?
- Tool Result가 success / error / blocked / partial을 구분하는가?
- Error Type이 표준화되어 있는가?
- Agent Tool Routing과 Agent Permission이 정의되어 있는가?
- Review Loop와 Handoff가 정의되어 있는가?
- Tool Testing과 Troubleshooting 기준이 있는가?

---

### [실무]

Final Integration Checklist:

```md
### [Final Integration Checklist]

#### Tool Definition

- [ ] toolName이 고유하고 명확한가?
- [ ] description에 Tool 사용 시점이 있는가?
- [ ] description에 Tool 사용 금지 조건이 있는가?
- [ ] parameters가 JSON Schema로 정의되어 있는가?
- [ ] requiredFields가 명확한가?
- [ ] returnType이 정의되어 있는가?
- [ ] failureCases가 정의되어 있는가?

#### Validation & Execution

- [ ] Required Field Check가 있는가?
- [ ] Type Check가 있는가?
- [ ] Enum Check가 있는가?
- [ ] Range Check가 있는가?
- [ ] Business Validation이 있는가?
- [ ] Permission Check가 Runtime에서 강제되는가?
- [ ] Risk Check가 Runtime에서 강제되는가?
- [ ] Timeout이 설정되어 있는가?
- [ ] Retry 정책이 Idempotency와 연결되어 있는가?

#### Safety

- [ ] sideEffect 여부가 정의되어 있는가?
- [ ] riskLevel이 정의되어 있는가?
- [ ] High Risk Tool에 Human Confirmation이 적용되는가?
- [ ] Preview 또는 Dry Run이 가능한가?
- [ ] Approval Scope를 검증하는가?
- [ ] Dangerous Operation 차단 규칙이 있는가?
- [ ] Audit Log 기준이 있는가?
- [ ] Secret / Token / 개인정보가 마스킹되는가?

#### Result & Error

- [ ] Tool Result가 success / error / blocked / partial을 구분하는가?
- [ ] data와 error가 분리되어 있는가?
- [ ] Error Type이 표준화되어 있는가?
- [ ] retryable 여부가 포함되어 있는가?
- [ ] source metadata가 유지되는가?
- [ ] Raw Exception이 노출되지 않는가?
- [ ] User Facing Error Message가 안전한가?

#### Multi-Agent

- [ ] Agent별 allowedTools가 정의되어 있는가?
- [ ] Agent별 deniedTools가 정의되어 있는가?
- [ ] PM Agent가 위험 Tool 직접 실행을 피하는가?
- [ ] Review Agent가 검증 중심으로 동작하는가?
- [ ] Fix 작업은 원 담당 Domain Agent가 수행하는가?
- [ ] Agent Handoff에 toolResults가 포함되는가?
- [ ] Shared State에 workflowId / taskId가 유지되는가?
- [ ] blocked / partial 상태가 숨겨지지 않는가?
- [ ] Review Loop가 정의되어 있는가?

#### Testing & Troubleshooting

- [ ] Schema Test가 있는가?
- [ ] Validation Test가 있는가?
- [ ] Permission Test가 있는가?
- [ ] Risk Test가 있는가?
- [ ] Human Confirmation Test가 있는가?
- [ ] Error Handling Test가 있는가?
- [ ] Result Mapping Test가 있는가?
- [ ] Security Test가 있는가?
- [ ] Tool Observability 기준이 있는가?
- [ ] Troubleshooting Table이 있는가?
```

Checklist 실패 시 Agent Runtime에 Tool을 연결하지 않는다.

먼저 Tool Definition, Runtime Policy, Result Mapping, Agent Permission을 수정한 뒤 다시 검수한다.

---

### [FAQ]

Q. Final Integration Checklist가 뭐야?
A. Tool Calling & Function Calling 설계를 Agent Runtime에 연결하기 전 최종 검수하는 체크리스트다.

Q. Final Checklist는 언제 사용해?
A. Tool을 실제 Agent Workflow에 연결하기 전, 또는 문서 세트 최종 검수 때 사용한다.

Q. Final Checklist에서 가장 중요한 항목은?
A. Tool Definition, Arguments Validation, Permission Check, Risk Check, Human Confirmation, Result Mapping, Agent Handoff다.

Q. Checklist 실패 시 어떻게 해?
A. Tool Definition, Runtime Policy, Result Mapping, Agent Permission을 수정하고 다시 검수한다.

Q. Part07의 최종 목표는 뭐야?
A. Tool Calling 문서 세트 전체가 실제 Multi-Agent System에 안전하게 연결될 수 있는지 검수하는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Tool Type Design이 뭐야?
A. Agent가 사용할 Tool을 목적, 위험도, Side Effect, 권한 기준에 따라 분류하는 설계다.

Q. Tool Type은 왜 나눠야 해?
A. RAG Search, File, API, Database, Code Execution, Deployment Tool은 위험도와 검증 기준이 다르기 때문이다.

Q. 대표 Tool Type에는 뭐가 있어?
A. RAG Search Tool, File Tool, API Tool, Database Tool, Code Execution Tool, Test Execution Tool, Observability Tool, Deployment Tool이 있다.

Q. RAG Search Tool이 뭐야?
A. Agent가 RAG 문서에서 관련 Chunk를 검색하기 위해 사용하는 Tool이다.

Q. RAG Search Tool Result에는 무엇이 필요해?
A. title, source, score, chunk, metadata가 필요하다.

Q. 검색 결과가 없으면 Tool 실패야?
A. 아니다. Tool이 정상 실행되었으면 success와 empty data로 반환할 수 있다.

Q. File Tool이 뭐야?
A. 프로젝트 파일을 읽거나 쓰거나 삭제하는 Tool이다.

Q. File Tool에서 가장 중요한 검증은?
A. filePath 검증, Path Traversal 차단, 허용 Workspace 확인, Secret 파일 접근 차단이다.

Q. File Delete Tool은 자동 실행해도 돼?
A. 안 된다. File Delete Tool은 High Risk로 분류하고 Human Confirmation을 요구해야 한다.

Q. API Tool이 뭐야?
A. 외부 서비스나 내부 Backend API를 호출하는 Tool이다.

Q. API Tool에서 Raw URL을 받아도 돼?
A. 권장하지 않는다. predefined endpointKey를 사용해 허용된 endpoint만 호출하는 것이 안전하다.

Q. API Key를 Tool Arguments로 받아도 돼?
A. 안 된다. API Key와 Token은 Secure Store에서 Runtime이 주입해야 한다.

Q. Database Tool은 어떻게 나눠야 해?
A. Database Read Tool과 Database Write Tool을 분리해야 한다.

Q. Raw SQL을 Tool Arguments로 받아도 돼?
A. 권장하지 않는다. queryKey나 mutationKey 기반으로 허용된 쿼리만 실행하는 것이 안전하다.

Q. Database Write Tool은 왜 High Risk야?
A. 실제 데이터 상태를 변경하고 복구가 어려울 수 있기 때문이다.

Q. DELETE without WHERE는 어떻게 처리해?
A. DangerousOperationBlocked로 차단해야 한다.

Q. Code Execution Tool이 뭐야?
A. Agent가 코드나 스크립트를 제한된 환경에서 실행하는 Tool이다.

Q. Code Execution Tool에는 무엇이 필요해?
A. Sandbox, Timeout, Memory Limit, CPU Limit, Network 제한, File System 제한, Secret 차단이 필요하다.

Q. Tool Testing이 뭐야?
A. Tool Definition, Validation, Permission, Risk, Execution, Result Mapping이 정상 동작하는지 검증하는 절차다.

Q. Tool Testing은 언제 해?
A. Agent Runtime에 Tool을 연결하기 전에 수행해야 한다.

Q. High Risk Tool은 무엇을 테스트해야 해?
A. Human Confirmation 전에는 실행되지 않고 blocked result를 반환하는지 테스트해야 한다.

Q. Tool Troubleshooting이 뭐야?
A. Tool Calling 과정에서 발생한 문제를 원인별로 분석하고 수정하는 절차다.

Q. 잘못된 Tool이 선택되면 무엇을 확인해?
A. Tool Name과 Tool Description이 모호하지 않은지 확인한다.

Q. ValidationError가 반복되면 어떻게 해?
A. JSON Schema를 단순화하고 Field Description과 Required Fields를 명확히 한다.

Q. PermissionError가 발생하면 어떻게 해?
A. Agent Permission과 allowedTools / deniedTools 정책을 확인한다.

Q. Tool 실패 원인은 어디서 확인해?
A. Tool Result, Error Type, Tool Observability, Audit Log, Agent Handoff에서 확인한다.

Q. Tool Calling에서 흔한 실수는?
A. Tool Description을 모호하게 작성하고, LLM이 생성한 Arguments를 검증 없이 실행하는 것이다.

Q. Tool Result를 문자열로만 반환해도 돼?
A. 권장하지 않는다. status, data, error, metadata 구조로 반환해야 한다.

Q. blocked 상태를 success로 처리하면 왜 문제야?
A. 실제 실행되지 않은 작업을 성공으로 오해해 다음 Agent가 잘못된 판단을 할 수 있다.

Q. Common Mistakes는 어디서 검수해?
A. Tool Testing, Review Agent 검수, Final Integration Checklist에서 확인한다.

Q. Final Integration Checklist가 뭐야?
A. Tool Calling & Function Calling 설계를 Agent Runtime에 연결하기 전 최종 검수하는 체크리스트다.

Q. Final Checklist에서 가장 중요한 항목은?
A. Tool Definition, Arguments Validation, Permission Check, Risk Check, Human Confirmation, Result Mapping, Agent Handoff다.

Q. Part07의 최종 목표는 뭐야?
A. Tool Calling 문서 세트 전체가 실제 Multi-Agent System에 안전하게 연결될 수 있는지 검수하는 것이다.
