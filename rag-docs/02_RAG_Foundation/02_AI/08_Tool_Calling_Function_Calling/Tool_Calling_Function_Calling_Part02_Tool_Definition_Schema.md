# Tool Calling & Function Calling Part02 - Tool Definition & Schema

---

# 1. Tool Definition

## 1.1 Tool Definition Concept

### [개념]

Tool Definition은 LLM이 어떤 Tool을 언제 선택해야 하는지 이해하도록 제공하는 구조화된 설명이다.

Tool Definition은 Agent Runtime이 실행 가능한 Tool의 이름, 목적, 입력값, 결과, 권한, 위험도, 실패 가능성을 정의한다.

Tool Definition이 모호하면 LLM은 잘못된 Tool을 선택하거나 잘못된 Tool Arguments를 생성할 수 있다.

Tool Definition은 Tool Choice 품질과 Tool Execution 안전성을 결정한다.

---

### [핵심]

- Tool Definition은 LLM에게 Tool 사용 목적을 설명한다.
- Tool Definition은 Tool Choice의 기준이다.
- Tool Definition은 Tool Name, Description, Parameters를 포함한다.
- Tool Definition은 Required Fields를 명확히 지정한다.
- Tool Definition은 Return Type과 Failure Case를 포함한다.
- Tool Definition은 Side Effect 여부를 표시한다.
- Tool Definition은 Permission Level과 Risk Level을 포함하는 것이 좋다.
- Tool Definition은 Human Confirmation 필요 여부를 포함할 수 있다.
- Tool Definition이 명확할수록 Tool Choice 정확도가 높아진다.
- Tool Definition이 모호하면 잘못된 Tool 호출이 발생한다.

---

### [실무]

2026 실무 기준 Tool Definition은 단순 함수 설명이 아니라 Agent Runtime의 안전 실행 정책까지 포함해야 한다.

표준 Tool Definition 필드:

| 필드                  | 표준 표기            | 설명                  |
| --------------------- | -------------------- | --------------------- |
| Tool Name             | toolName             | Tool의 고유 이름      |
| Description           | description          | Tool 사용 시점과 목적 |
| Parameters            | parameters           | Tool Arguments 구조   |
| Required Fields       | requiredFields       | 필수 입력값           |
| Return Type           | returnType           | 반환 데이터 구조      |
| Side Effect           | sideEffect           | 외부 시스템 변경 여부 |
| Permission Level      | permissionLevel      | 실행 권한 수준        |
| Risk Level            | riskLevel            | Tool 위험도           |
| Requires Confirmation | requiresConfirmation | 사용자 승인 필요 여부 |
| Failure Cases         | failureCases         | 실패 가능한 조건      |

Tool Definition 예시:

```json
{
  "toolName": "search_rag_documents",
  "description": "Search relevant RAG documents when the user asks about project rules, domain knowledge, implementation patterns, or validation criteria.",
  "parameters": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "Search query for retrieving relevant RAG document chunks."
      },
      "topK": {
        "type": "integer",
        "description": "Maximum number of document chunks to retrieve.",
        "default": 5,
        "minimum": 1,
        "maximum": 20
      },
      "domainFilter": {
        "type": "string",
        "description": "Optional domain filter such as Backend, Frontend, AI, DevOps."
      }
    },
    "required": ["query"]
  },
  "requiredFields": ["query"],
  "returnType": "RetrievedDocumentList",
  "sideEffect": false,
  "permissionLevel": "read",
  "riskLevel": "low",
  "requiresConfirmation": false,
  "failureCases": ["ValidationError", "TimeoutError"]
}
```

Tool Definition은 LLM Prompt에만 존재하면 부족하다.

Agent Runtime에서도 Tool Policy로 검증 가능해야 한다.

---

### [FAQ]

Q. Tool Definition이 뭐야?
A. LLM이 Tool의 목적, 입력값, 사용 시점, 결과 구조, 위험도, 실패 조건을 이해하도록 제공하는 구조화된 설명이다.

Q. Tool Definition은 왜 중요해?
A. Tool Definition이 명확해야 LLM이 올바른 Tool을 선택하고 올바른 Tool Arguments를 생성할 수 있다.

Q. Tool Definition에는 뭐가 들어가야 해?
A. toolName, description, parameters, requiredFields, returnType, sideEffect, permissionLevel, riskLevel, requiresConfirmation, failureCases가 들어가면 좋다.

Q. Tool Definition은 LLM만 보면 돼?
A. 아니다. Runtime도 Tool Definition과 Tool Policy를 기준으로 검증해야 한다.

Q. Tool Definition이 모호하면 어떤 문제가 생겨?
A. 잘못된 Tool Choice, 잘못된 Arguments, 위험 Tool 오작동, Error Handling 실패가 발생할 수 있다.

---

# 2. Tool Name

## 2.1 Tool Name Design

### [개념]

Tool Name은 LLM과 Agent Runtime이 Tool을 식별하는 고유 이름이다.

Tool Name은 짧고 명확해야 하며 Tool의 목적을 직접 드러내야 한다.

Tool Name이 비슷하거나 모호하면 LLM이 잘못된 Tool을 선택할 수 있다.

---

### [핵심]

- Tool Name은 고유해야 한다.
- Tool Name은 짧고 명확해야 한다.
- Tool Name은 동사 + 대상 구조가 좋다.
- Tool Name은 Tool의 목적을 직접 표현해야 한다.
- 비슷한 Tool Name을 남발하지 않는다.
- read, search, create, update, delete 같은 동사를 일관되게 사용한다.
- 위험 Tool은 이름에서 변경 작업이 드러나야 한다.
- Tool Name은 Agent Tool Permission과 연결된다.

---

### [실무]

권장 Tool Name:

```text
search_rag_documents
read_project_file
write_project_file
append_project_file
delete_project_file
query_database_read
execute_database_write
call_external_api
execute_test_suite
read_test_result
send_email_message
deploy_application
```

비권장 Tool Name:

```text
tool1
process
handler
do_task
run
file_tool
api
manager
```

동사 기준:

| 동사     | 의미                 | 위험도        |
| -------- | -------------------- | ------------- |
| search   | 검색                 | Low           |
| read     | 읽기                 | Low           |
| list     | 목록 조회            | Low           |
| validate | 검증                 | Low           |
| create   | 생성                 | Medium        |
| append   | 추가                 | Medium        |
| update   | 수정                 | Medium ~ High |
| write    | 쓰기 / 덮어쓰기 가능 | Medium ~ High |
| delete   | 삭제                 | High          |
| send     | 발송                 | High          |
| deploy   | 배포                 | High          |
| execute  | 실행                 | Medium ~ High |

Tool Name과 위험도 예시:

```text
read_project_file      → Low Risk
write_project_file     → Medium ~ High Risk
delete_project_file    → High Risk
send_email_message     → High Risk
deploy_application     → High Risk
```

---

### [FAQ]

Q. Tool Name은 어떻게 지어야 해?
A. 짧고 명확하게 동사 + 대상 형태로 작성하는 것이 좋다.

Q. Tool Name이 모호하면 어떤 문제가 생겨?
A. LLM이 잘못된 Tool을 선택하거나 비슷한 Tool 사이에서 혼동할 수 있다.

Q. read와 write를 Tool Name에서 구분해야 해?
A. 반드시 구분하는 것이 좋다. read는 낮은 위험, write는 중간 이상 위험으로 처리해야 한다.

Q. delete Tool은 이름에 delete를 넣어야 해?
A. 그렇다. 위험 작업은 이름만 봐도 변경 또는 삭제임을 알 수 있어야 한다.

Q. Tool Name에 manager 같은 단어를 써도 돼?
A. 권장하지 않는다. manager는 역할이 모호해 Tool Choice 품질을 낮출 수 있다.

---

# 3. Tool Description

## 3.1 Tool Description Design

### [개념]

Tool Description은 LLM이 Tool을 선택할지 판단하는 기준 문장이다.

Tool Description은 Tool의 기능뿐 아니라 사용해야 하는 상황과 사용하지 말아야 하는 상황을 포함해야 한다.

Tool Description은 Tool Choice 정확도에 직접 영향을 준다.

---

### [핵심]

- Tool Description은 Tool의 목적을 설명한다.
- Tool Description은 Tool 사용 시점을 포함한다.
- Tool Description은 Tool 사용 금지 상황을 포함할 수 있다.
- Tool Description은 짧고 구체적으로 작성한다.
- Tool Description은 다른 Tool과의 차이를 드러내야 한다.
- Tool Description에 입력 조건을 명시하면 Arguments 품질이 좋아진다.
- 위험 Tool은 Description에 승인 필요 여부를 포함한다.
- Tool Description은 Troubleshooting의 주요 점검 대상이다.

---

### [실무]

좋은 Tool Description:

```json
{
  "toolName": "read_project_file",
  "description": "Read a project file when the user asks to inspect, review, summarize, or validate existing file content. This tool does not modify files."
}
```

나쁜 Tool Description:

```json
{
  "toolName": "read_project_file",
  "description": "Use this for files."
}
```

위험 Tool Description 예시:

```json
{
  "toolName": "write_project_file",
  "description": "Write or overwrite a project file after validating the file path and receiving user confirmation when the operation may replace existing content."
}
```

Tool Description 작성 기준:

| 포함 항목 | 예시                                                  |
| --------- | ----------------------------------------------------- |
| 기능      | Search relevant RAG documents                         |
| 사용 시점 | when the user asks about domain rules                 |
| 제한      | does not modify files                                 |
| 위험      | requires confirmation before overwrite                |
| 결과      | returns matching document chunks with source metadata |

---

### [FAQ]

Q. Tool Description에는 무엇을 써야 해?
A. Tool이 무엇을 하는지, 언제 써야 하는지, 무엇을 하지 않는지를 명확히 써야 한다.

Q. Tool Description이 너무 짧으면 문제야?
A. 그렇다. 사용 시점이 빠지면 LLM이 잘못된 상황에서 Tool을 선택할 수 있다.

Q. Tool Description에 금지 조건도 넣어야 해?
A. 필요하면 넣는 것이 좋다. 특히 read/write, search/delete처럼 위험도가 다른 Tool은 제한 조건이 중요하다.

Q. 위험 Tool Description에는 무엇을 추가해야 해?
A. 사용자 확인, 경로 검증, 권한 확인, 덮어쓰기 여부 같은 안전 조건을 포함해야 한다.

Q. Tool Description이 길수록 좋아?
A. 아니다. 짧고 구체적인 설명이 좋다. 장황한 설명은 Tool Choice 품질을 떨어뜨릴 수 있다.

---

# 4. Parameters and Tool Schema

## 4.1 Parameters Concept

### [개념]

Parameters는 Tool Execution에 필요한 입력값의 구조이다.

Parameters는 LLM이 어떤 Tool Arguments를 생성해야 하는지 알려준다.

Tool Calling에서 Parameters는 보통 JSON Schema 형태로 정의한다.

Parameters가 명확하지 않으면 필수값 누락, 타입 오류, 잘못된 enum 값, 위험한 입력값이 발생할 수 있다.

---

### [핵심]

- Parameters는 Tool Arguments의 구조를 정의한다.
- Parameters는 type, properties, required를 포함한다.
- 각 field에는 description을 작성한다.
- enum으로 허용 값을 제한할 수 있다.
- default로 기본값을 지정할 수 있다.
- nullable 여부를 명확히 한다.
- array와 object는 중첩 구조를 최소화한다.
- 복잡한 Parameters는 LLM 출력 실패 가능성을 높인다.
- Parameters는 Arguments Validation의 입력 기준이다.

---

### [실무]

Parameters 예시:

```json
{
  "type": "object",
  "properties": {
    "query": {
      "type": "string",
      "description": "Search query for the RAG document index."
    },
    "topK": {
      "type": "integer",
      "description": "Number of results to return.",
      "default": 5,
      "minimum": 1,
      "maximum": 20
    },
    "domainFilter": {
      "type": "string",
      "description": "Optional domain filter.",
      "enum": ["Backend", "Frontend", "AI", "DevOps", "Security"]
    }
  },
  "required": ["query"]
}
```

Parameters 설계 기준:

| 기준        | 설명                                   |
| ----------- | -------------------------------------- |
| 명확성      | Field 목적이 분명해야 함               |
| 제한성      | type, enum, min, max로 입력 제한       |
| 단순성      | 중첩 구조 최소화                       |
| 검증 가능성 | Runtime에서 쉽게 검증 가능해야 함      |
| 안전성      | 위험 입력값 제한 가능해야 함           |
| 검색성      | Field 이름이 RAG Query와 매칭되어야 함 |

---

### [FAQ]

Q. Parameters가 뭐야?
A. Tool 실행에 필요한 입력값 구조를 정의한 것이다.

Q. Parameters는 왜 JSON Schema로 작성해?
A. LLM이 구조화된 Tool Arguments를 생성하고 Runtime이 실행 전 검증하기 쉽기 때문이다.

Q. required는 왜 필요해?
A. Tool 실행에 반드시 필요한 값을 누락하지 않도록 제한하기 위해 필요하다.

Q. enum은 언제 써?
A. domainFilter, mode, actionType처럼 허용 가능한 값이 정해져 있을 때 사용한다.

Q. Parameters는 복잡하게 만들어도 돼?
A. 가능하지만 권장하지 않는다. 너무 복잡하면 LLM이 Arguments 형식을 틀릴 가능성이 커진다.

---

# 5. JSON Schema

## 5.1 JSON Schema Concept

### [개념]

JSON Schema는 Tool Arguments의 형식과 제약 조건을 정의하는 표준 구조이다.

Tool Calling에서 JSON Schema는 LLM 출력의 안정성을 높이고 Runtime 검증 기준을 제공한다.

JSON Schema는 Tool Arguments가 실행 가능한 형태인지 확인하는 1차 방어선이다.

---

### [핵심]

- JSON Schema는 Arguments의 type을 정의한다.
- JSON Schema는 properties를 정의한다.
- JSON Schema는 required field를 정의한다.
- JSON Schema는 enum으로 허용 값을 제한한다.
- JSON Schema는 minimum, maximum으로 수치 범위를 제한한다.
- JSON Schema는 array item type을 제한한다.
- JSON Schema는 object 중첩을 표현할 수 있다.
- JSON Schema 검증은 Tool Execution 전에 수행한다.
- JSON Schema만으로 Safe Execution이 완성되지는 않는다.

---

### [실무]

기본 JSON Schema:

```json
{
  "type": "object",
  "properties": {
    "filePath": {
      "type": "string",
      "description": "Target file path to read."
    },
    "mode": {
      "type": "string",
      "enum": ["read", "write", "append"],
      "description": "File operation mode."
    }
  },
  "required": ["filePath", "mode"]
}
```

실무 검증 Flow:

```text
Generated Tool Arguments
→ JSON Schema Validation
→ Business Validation
→ Permission Check
→ Risk Check
→ Tool Execution
```

JSON Schema 이후 추가 검증:

| 검증                | 설명             |
| ------------------- | ---------------- |
| Schema Validation   | 형식 검증        |
| Business Validation | 업무 규칙 검증   |
| Path Validation     | 경로 안전성 검증 |
| Permission Check    | 권한 검증        |
| Risk Check          | 위험도 검증      |
| Human Confirmation  | 사용자 승인      |

JSON Schema는 “입력 형식”을 제한한다.

Safe Tool Execution은 “실행 가능 여부”까지 판단한다.

---

### [FAQ]

Q. JSON Schema가 뭐야?
A. Tool Arguments의 타입, 필드, 필수값, 허용값, 범위를 정의하는 구조다.

Q. JSON Schema만 있으면 안전해?
A. 아니다. Schema 검증 외에도 Business Validation, Permission Check, Path Validation, Risk Check가 필요하다.

Q. JSON Schema는 언제 검증해?
A. Tool Execution 전에 반드시 검증한다.

Q. Schema가 너무 느슨하면 어떻게 돼?
A. 잘못된 입력값이나 위험한 Arguments가 실행 단계까지 전달될 수 있다.

Q. Schema가 너무 복잡하면 어떻게 돼?
A. LLM이 Arguments 형식을 틀리거나 필드를 누락할 가능성이 높아진다.

---

# 6. Required Fields

## 6.1 Required Fields Design

### [개념]

Required Fields는 Tool Execution에 반드시 필요한 입력값이다.

Required Fields가 누락되면 Tool은 실행하면 안 된다.

Required Fields는 LLM이 빠뜨리기 쉬운 핵심 입력값을 명확히 제한하는 역할을 한다.

---

### [핵심]

- Required Fields는 Tool Execution 최소 조건이다.
- Required Fields가 없으면 Tool Execution을 중단한다.
- Required Fields는 JSON Schema의 required 배열에 명시한다.
- 필수값이 빈 문자열이면 누락으로 처리할 수 있다.
- null 허용 여부를 명확히 한다.
- Optional Field와 Required Field를 구분한다.
- Required Fields는 너무 많지 않게 유지한다.
- Required Fields 누락은 ValidationError로 처리한다.

---

### [실무]

Required Fields 예시:

```json
{
  "type": "object",
  "properties": {
    "query": {
      "type": "string",
      "description": "Search query."
    },
    "topK": {
      "type": "integer",
      "description": "Number of results."
    }
  },
  "required": ["query"]
}
```

검증 기준:

```text
Required Field Missing
→ Return ValidationError
→ Do Not Execute Tool
```

빈 문자열 처리 예시:

```json
{
  "query": ""
}
```

위 입력은 형식상 string이지만 실무에서는 ValidationError로 처리하는 것이 좋다.

Optional Field 처리:

```json
{
  "query": "Tool Result structure"
}
```

topK가 optional이면 Runtime은 default 5를 적용할 수 있다.

---

### [FAQ]

Q. Required Fields가 뭐야?
A. Tool 실행에 반드시 필요한 입력값이다.

Q. Required Field가 빠지면 어떻게 해?
A. Tool을 실행하지 않고 ValidationError를 반환해야 한다.

Q. 빈 문자열도 Required Field 충족으로 봐도 돼?
A. 대부분의 경우 안 된다. query, filePath 같은 값은 빈 문자열이면 ValidationError로 처리한다.

Q. Required Fields는 많을수록 좋아?
A. 아니다. 너무 많으면 LLM이 누락할 가능성이 커진다. 실행에 꼭 필요한 값만 required로 지정한다.

Q. Optional Field는 어떻게 처리해?
A. 기본값을 지정하거나 누락 시 안전한 기본 동작을 사용한다.

---

# 7. Return Type

## 7.1 Return Type Design

### [개념]

Return Type은 Tool Execution 결과가 어떤 구조로 반환되는지 정의한다.

Return Type은 LLM과 다음 Agent가 Tool Result를 이해하기 위한 기준이다.

Return Type이 불명확하면 LLM은 Tool 결과를 잘못 해석하거나 실패 결과를 성공처럼 처리할 수 있다.

---

### [핵심]

- Return Type은 Tool Result 구조를 정의한다.
- Return Type은 Result Handling의 기준이다.
- 성공 결과와 실패 결과를 분리한다.
- status 필드를 포함하는 것이 좋다.
- data 필드에는 실제 결과를 담는다.
- error 필드에는 실패 정보를 담는다.
- metadata에는 source, executionTimeMs, toolName을 포함할 수 있다.
- Return Type은 다음 Agent가 재사용 가능해야 한다.
- Tool Result는 success / error / blocked / partial을 구분할 수 있어야 한다.

---

### [실무]

성공 Return Type 예시:

```json
{
  "status": "success",
  "data": {
    "documents": [
      {
        "title": "Tool Arguments Validation",
        "source": "Tool_Calling_Function_Calling_Part03_Arguments_Validation_Execution.md",
        "score": 0.87
      }
    ]
  },
  "metadata": {
    "toolName": "search_rag_documents",
    "executionTimeMs": 120
  }
}
```

실패 Return Type 예시:

```json
{
  "status": "error",
  "error": {
    "type": "ValidationError",
    "message": "query is required",
    "retryable": false
  },
  "metadata": {
    "toolName": "search_rag_documents",
    "executionTimeMs": 3
  }
}
```

Blocked Return Type 예시:

```json
{
  "status": "blocked",
  "reason": "HumanConfirmationRequired",
  "message": "File overwrite requires user confirmation.",
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

Return Type 권장 필드:

| 필드            | 목적                                     |
| --------------- | ---------------------------------------- |
| status          | success / error / blocked / partial 구분 |
| data            | 성공 데이터                              |
| error           | 실패 정보                                |
| message         | 사용자 또는 Agent용 요약                 |
| metadata        | Tool 실행 메타데이터                     |
| source          | 출처                                     |
| confidence      | 신뢰도                                   |
| executionTimeMs | 실행 시간                                |
| traceId         | 추적 ID                                  |

---

### [FAQ]

Q. Return Type이 뭐야?
A. Tool 실행 결과가 어떤 구조로 반환되는지 정의한 것이다.

Q. Tool Result에 status가 필요한 이유는?
A. 성공, 실패, 차단, 일부 성공 상태를 명확히 구분하기 위해서다.

Q. data와 error는 분리해야 해?
A. 그렇다. 성공 데이터와 실패 정보를 분리해야 후속 처리가 안정적이다.

Q. metadata에는 무엇을 넣어?
A. toolName, executionTimeMs, source, traceId, retryCount 같은 정보를 넣을 수 있다.

Q. Return Type은 왜 Agent 간 공유에 중요해?
A. 다음 Agent가 Tool Result를 검증하거나 재사용하려면 구조가 명확해야 하기 때문이다.

---

# 8. Side Effect

## 8.1 Side Effect Definition

### [개념]

Side Effect는 Tool Execution이 외부 시스템이나 데이터 상태를 변경하는 효과이다.

Tool Calling에서 Side Effect 여부는 Risk Level, Human Confirmation, Audit Log, Retry 가능 여부에 직접 영향을 준다.

Side Effect는 Tool Definition에 명시하는 것이 좋다.

---

### [핵심]

- Side Effect가 없는 Tool은 주로 읽기 / 검색 작업이다.
- Side Effect가 있는 Tool은 파일, DB, 이메일, 배포, 결제 등에 영향을 준다.
- Side Effect Tool은 Risk Level 분류가 필요하다.
- Side Effect Tool은 Human Confirmation이 필요할 수 있다.
- Side Effect Tool은 Audit Log를 남겨야 한다.
- Side Effect Tool은 Retry 시 중복 실행 위험이 있다.
- Side Effect 여부는 Tool Definition에 명시한다.
- Side Effect 기준은 Safe Execution과 연결된다.

---

### [실무]

Side Effect 기준:

| Tool                   | sideEffect | riskLevel     |
| ---------------------- | ---------: | ------------- |
| search_rag_documents   |      false | low           |
| read_project_file      |      false | low           |
| validate_code_style    |      false | low           |
| append_project_file    |       true | medium        |
| write_project_file     |       true | medium ~ high |
| delete_project_file    |       true | high          |
| execute_database_write |       true | high          |
| send_email_message     |       true | high          |
| request_payment        |       true | high          |
| deploy_application     |       true | high          |

Tool Definition 예시:

```json
{
  "toolName": "send_email_message",
  "description": "Send an email message after explicit user confirmation.",
  "sideEffect": true,
  "riskLevel": "high",
  "requiresConfirmation": true
}
```

Side Effect가 있는 Tool은 자동 실행하지 않는 것이 기본이다.

특히 다음 작업은 Human Confirmation 대상으로 분류한다.

- 삭제
- 덮어쓰기
- 이메일 발송
- 결제 요청
- 배포
- DB 변경
- 계정 설정 변경

---

### [FAQ]

Q. Side Effect가 뭐야?
A. Tool 실행이 파일, DB, 이메일, 배포, 결제처럼 외부 시스템 상태를 변경하는 효과다.

Q. Side Effect가 없는 Tool은 안전해?
A. 비교적 안전하지만 파일 경로, 권한, 민감정보 노출 여부는 여전히 검증해야 한다.

Q. Side Effect가 있는 Tool은 어떻게 처리해?
A. Risk Level 분류, 입력 검증, 권한 확인, Human Confirmation, Audit Log를 적용한다.

Q. Side Effect Tool은 Retry해도 돼?
A. 조심해야 한다. 중복 이메일 발송, 중복 결제, 중복 DB 변경이 발생할 수 있다.

Q. Side Effect는 Tool Definition에 넣어야 해?
A. 넣는 것이 좋다. Agent Runtime이 위험도와 승인 필요 여부를 판단하는 기준이 된다.

---

# 9. Permission Level

## 9.1 Permission Level Design

### [개념]

Permission Level은 Agent 또는 User가 Tool을 실행할 수 있는 작업 범위를 제한하는 권한 기준이다.

Tool Calling에서는 모든 Agent가 모든 Tool을 사용할 수 있게 하면 위험하다.

Permission Level은 최소 권한 원칙을 적용하기 위한 핵심 정보이다.

---

### [핵심]

- Permission Level은 Tool 접근 권한을 제한한다.
- Agent별로 사용할 수 있는 Tool을 다르게 설정한다.
- read, validate, write, execute, admin 권한을 분리한다.
- 위험 Tool은 제한된 Agent만 사용한다.
- PM Agent는 라우팅 중심으로 제한한다.
- Review Agent는 read / validate 중심으로 제한한다.
- Permission Level은 Tool Definition에 명시할 수 있다.
- Permission Level 기준은 Agent Tool Permission과 연결된다.

---

### [실무]

권한 레벨 예시:

| permissionLevel | 설명        | 예시 Tool                               |
| --------------- | ----------- | --------------------------------------- |
| none            | 사용 불가   | restricted tool                         |
| read            | 읽기 / 검색 | search_rag_documents, read_project_file |
| validate        | 검증        | run_static_analysis, validate_schema    |
| write           | 쓰기 / 수정 | write_project_file                      |
| execute         | 실행        | execute_test_suite                      |
| admin           | 고위험 실행 | deploy_application, delete_project_file |

Agent별 권한 예시:

| Agent          | 적정 권한                       |
| -------------- | ------------------------------- |
| PM Agent       | read, route                     |
| Backend Agent  | read, validate, limited write   |
| Frontend Agent | read, validate, limited write   |
| Review Agent   | read, validate                  |
| DevOps Agent   | read, validate, limited execute |
| AI/ML Agent    | read, validate, evaluation      |
| Admin Agent    | restricted high-risk tools      |

Tool Definition 예시:

```json
{
  "toolName": "deploy_application",
  "description": "Deploy the application after validation and explicit approval.",
  "permissionLevel": "admin",
  "sideEffect": true,
  "riskLevel": "high",
  "requiresConfirmation": true
}
```

---

### [FAQ]

Q. Permission Level이 뭐야?
A. Agent나 User가 수행할 수 있는 Tool 작업 범위를 제한하는 권한 기준이다.

Q. 모든 Agent가 모든 Tool을 써도 돼?
A. 안 된다. 최소 권한 원칙에 따라 Agent별 Tool 접근을 제한해야 한다.

Q. PM Agent는 어떤 권한이 적절해?
A. RAG Search와 Task Routing 중심의 read / route 권한이 적절하다.

Q. Review Agent는 write 권한이 필요해?
A. 기본적으로 검증 중심이므로 read / validate 권한이 적절하다. 수정 권한은 별도 Agent 또는 승인된 Domain Agent에 둘 수 있다.

Q. Permission Level은 어디에 정의해?
A. Tool Definition과 Agent Runtime의 Tool Access Policy에 정의한다.

---

# 10. Risk Level

## 10.1 Risk Level Design

### [개념]

Risk Level은 Tool Execution이 시스템, 데이터, 비용, 외부 서비스, 사용자 계정에 미칠 수 있는 영향을 기준으로 위험도를 분류한 값이다.

Risk Level은 Tool 실행 방식, Human Confirmation 필요 여부, Audit Log 필요 여부를 결정한다.

---

### [핵심]

- riskLevel은 low, medium, high로 분류한다.
- Low Risk Tool은 검색, 읽기, 계산, 검증 중심이다.
- Medium Risk Tool은 제한된 쓰기, append, 임시 파일 생성 같은 작업이다.
- High Risk Tool은 삭제, 덮어쓰기, 이메일 발송, 결제, 배포, DB 변경이다.
- Risk Level은 sideEffect와 함께 판단한다.
- High Risk Tool은 Human Confirmation이 필요하다.
- Risk Level은 Tool Definition에 포함하는 것이 좋다.
- Risk Level 기준은 Safe Execution과 연결된다.

---

### [실무]

Risk Level 기준:

| riskLevel | 설명                                           | 실행 정책                   |
| --------- | ---------------------------------------------- | --------------------------- |
| low       | 읽기 / 검색 / 계산 / 검증                      | Auto Execute 가능           |
| medium    | 제한된 쓰기 / append / 임시 생성               | Validate + Log              |
| high      | 삭제 / 덮어쓰기 / 발송 / 결제 / 배포 / DB 변경 | Human Confirmation Required |

Tool Definition 예시:

```json
{
  "toolName": "execute_database_write",
  "description": "Execute an approved database write operation after dry run and user confirmation.",
  "permissionLevel": "admin",
  "sideEffect": true,
  "riskLevel": "high",
  "requiresConfirmation": true
}
```

Risk Level 판단 Flow:

```text
Tool Definition
→ Check sideEffect
→ Check external state change
→ Check cost impact
→ Check reversibility
→ Check idempotency
→ Assign riskLevel
```

---

### [FAQ]

Q. Risk Level이 뭐야?
A. Tool 실행이 시스템, 데이터, 비용, 외부 서비스에 미치는 영향을 기준으로 나눈 위험도다.

Q. riskLevel은 어떻게 나눠?
A. low, medium, high로 나누고 high는 Human Confirmation을 요구한다.

Q. High Risk Tool에는 뭐가 있어?
A. 파일 삭제, 파일 덮어쓰기, DB 변경, 이메일 발송, 결제 요청, 배포, 계정 변경 작업이 있다.

Q. Risk Level과 Side Effect는 관계가 있어?
A. 있다. Side Effect가 큰 Tool일수록 medium 또는 high로 분류하는 것이 안전하다.

Q. Risk Level은 어디에 정의해?
A. Tool Definition과 Agent Runtime의 Tool Policy에 정의한다.

---

# 11. Failure Case

## 11.1 Failure Case Definition

### [개념]

Failure Case는 Tool이 실패할 수 있는 조건과 실패 처리 방식을 정의한 것이다.

Tool Definition에 Failure Case를 포함하면 LLM과 Agent Runtime이 실패를 예측하고 안정적으로 처리할 수 있다.

Failure Case는 Error Handling의 기준이 된다.

---

### [핵심]

- Failure Case는 Tool 실패 가능성을 명시한다.
- ValidationError, PermissionError, NotFoundError를 포함한다.
- TimeoutError, RateLimitError, ExternalApiError를 포함할 수 있다.
- 실패 시 status는 error로 반환한다.
- 실패 원인과 retryable 여부를 구분한다.
- 실패를 성공처럼 처리하지 않는다.
- Failure Case는 Troubleshooting과 연결된다.
- Failure Case가 없으면 Error Handling 품질이 떨어진다.

---

### [실무]

Failure Case 예시:

```json
{
  "toolName": "read_project_file",
  "failureCases": [
    {
      "type": "ValidationError",
      "condition": "filePath is missing or empty",
      "retryable": false
    },
    {
      "type": "PermissionError",
      "condition": "filePath is outside allowed directory",
      "retryable": false
    },
    {
      "type": "NotFoundError",
      "condition": "target file does not exist",
      "retryable": false
    },
    {
      "type": "TimeoutError",
      "condition": "file read operation exceeds timeout",
      "retryable": true
    }
  ]
}
```

실패 결과 예시:

```json
{
  "status": "error",
  "error": {
    "type": "NotFoundError",
    "message": "The requested file does not exist.",
    "retryable": false
  },
  "metadata": {
    "toolName": "read_project_file"
  }
}
```

Failure Case와 Error Type 매핑:

| Failure Case              | Error Type              |
| ------------------------- | ----------------------- |
| required missing          | ValidationError         |
| invalid enum              | ValidationError         |
| outside allowed directory | PermissionError         |
| resource missing          | NotFoundError           |
| execution timeout         | TimeoutError            |
| 429 limit                 | RateLimitError          |
| external API failure      | ExternalApiError        |
| dangerous pattern         | DangerousOperationError |

---

### [FAQ]

Q. Failure Case가 뭐야?
A. Tool이 실패할 수 있는 조건과 실패 처리 방식을 정의한 것이다.

Q. Failure Case를 왜 Tool Definition에 넣어?
A. Agent Runtime과 LLM이 실패를 예측하고 적절하게 처리할 수 있게 하기 위해서다.

Q. Tool 실패 시 status는 어떻게 해?
A. status를 error로 명확히 반환해야 한다.

Q. retryable은 왜 필요해?
A. 재시도 가능한 오류와 재시도하면 안 되는 오류를 구분하기 위해 필요하다.

Q. Tool 실패를 무시해도 돼?
A. 안 된다. 실패를 숨기면 LLM이 성공처럼 답변할 수 있다.

---

# 12. Complete Tool Definition Example

## 12.1 Integrated Tool Definition

### [개념]

Complete Tool Definition은 Tool Name, Description, Parameters, Required Fields, Return Type, Side Effect, Permission Level, Risk Level, Confirmation, Failure Case를 모두 포함한 통합 정의이다.

Complete Tool Definition은 Agent Runtime에 Tool을 연결하기 전 검수 기준으로 사용할 수 있다.

---

### [핵심]

- Complete Tool Definition은 실행 가능한 수준의 Tool 기준이다.
- Tool Choice와 Tool Arguments 생성을 지원한다.
- Runtime Validation을 지원한다.
- Permission Check와 Risk Check를 지원한다.
- Human Confirmation 필요 여부를 지원한다.
- Result Mapping과 Error Handling을 지원한다.
- Agent Tool Routing과 Tool Testing에 재사용할 수 있다.

---

### [실무]

Complete Tool Definition 예시:

```json
{
  "toolName": "write_project_file",
  "description": "Write, append, or overwrite a project file after validating path, permission, risk level, and confirmation requirement.",
  "parameters": {
    "type": "object",
    "properties": {
      "filePath": {
        "type": "string",
        "description": "Target project file path inside the allowed workspace."
      },
      "mode": {
        "type": "string",
        "enum": ["write", "append", "overwrite"],
        "description": "File write mode."
      },
      "content": {
        "type": "string",
        "description": "Content to write to the target file."
      },
      "dryRun": {
        "type": "boolean",
        "description": "If true, return preview without modifying the file.",
        "default": true
      }
    },
    "required": ["filePath", "mode", "content"]
  },
  "requiredFields": ["filePath", "mode", "content"],
  "returnType": {
    "status": ["success", "error", "blocked"],
    "data": {
      "filePath": "string",
      "operation": "string",
      "preview": "string"
    },
    "error": {
      "type": "string",
      "message": "string",
      "retryable": "boolean"
    },
    "metadata": {
      "toolName": "string",
      "executionTimeMs": "number",
      "riskLevel": "string"
    }
  },
  "sideEffect": true,
  "permissionLevel": "write",
  "riskLevel": "medium",
  "requiresConfirmation": "when mode is overwrite or target exists",
  "failureCases": [
    "ValidationError",
    "PermissionError",
    "DangerousOperationError",
    "TimeoutError"
  ]
}
```

Complete Tool Definition 검수 기준:

```text
Tool Definition
→ Tool Choice 가능?
→ Arguments 생성 가능?
→ Runtime Validation 가능?
→ Permission Check 가능?
→ Risk Check 가능?
→ Result Mapping 가능?
→ Error Handling 가능?
```

---

### [FAQ]

Q. Complete Tool Definition이 뭐야?
A. Tool 실행과 검증에 필요한 이름, 설명, schema, 권한, 위험도, 결과, 실패 조건을 모두 포함한 정의다.

Q. Complete Tool Definition은 언제 필요해?
A. Tool을 Agent Runtime에 연결하기 전 최종 검수할 때 필요하다.

Q. Complete Tool Definition에 riskLevel이 꼭 필요해?
A. Side Effect가 있거나 위험 가능성이 있는 Tool에는 반드시 필요하다.

Q. requiresConfirmation은 boolean만 가능해?
A. 단순 boolean도 가능하지만 “overwrite일 때 필요”처럼 조건부로 정의할 수 있다.

Q. Complete Tool Definition은 Tool Testing에 사용돼?
A. 그렇다. Tool Testing과 Final Integration Checklist의 기준이 된다.

---

# 13. Tool Definition Checklist

## 13.1 Definition Quality Checklist

### [개념]

Tool Definition Checklist는 Tool을 Agent에 연결하기 전 검수하는 기준이다.

Tool Definition은 실행 품질, 검색 품질, 안전성, 검증 가능성을 모두 만족해야 한다.

---

### [핵심]

- Tool Name이 명확한가?
- Tool Description에 사용 시점이 포함되어 있는가?
- Parameters가 JSON Schema로 정의되어 있는가?
- Required Fields가 명확한가?
- Field Description이 충분한가?
- Return Type이 구조화되어 있는가?
- Side Effect 여부가 표시되어 있는가?
- Permission Level이 정의되어 있는가?
- Risk Level이 정의되어 있는가?
- Requires Confirmation 기준이 정의되어 있는가?
- Failure Case가 정의되어 있는가?
- Tool Result가 success / error / blocked / partial을 구분하는가?

---

### [실무]

Tool Definition 검수 Checklist:

```md
### [Checklist]

- [ ] toolName은 고유하고 명확한가?
- [ ] toolName은 동사 + 대상 구조인가?
- [ ] description은 Tool 사용 시점을 포함하는가?
- [ ] description은 Tool 사용 금지 조건을 포함하는가?
- [ ] parameters는 JSON Schema로 정의되어 있는가?
- [ ] requiredFields가 명확한가?
- [ ] 각 Field에 description이 있는가?
- [ ] enum, minimum, maximum 등 제한이 필요한 곳에 적용되었는가?
- [ ] returnType이 success / error / blocked / partial을 구분하는가?
- [ ] sideEffect 여부가 정의되어 있는가?
- [ ] permissionLevel이 정의되어 있는가?
- [ ] riskLevel이 정의되어 있는가?
- [ ] requiresConfirmation 기준이 정의되어 있는가?
- [ ] failureCases가 정의되어 있는가?
- [ ] Tool Result에 metadata와 source가 포함되는가?
- [ ] Agent Tool Permission과 연결 가능한가?
- [ ] Tool Testing이 가능한 구조인가?
```

Checklist 실패 시 Agent Runtime에 연결하지 않는다.

---

### [FAQ]

Q. Tool Definition은 언제 검수해?
A. Agent Runtime에 Tool을 연결하기 전에 검수해야 한다.

Q. Tool Definition 검수에서 가장 중요한 항목은?
A. description, parameters, requiredFields, sideEffect, permissionLevel, riskLevel, failureCases다.

Q. Tool Definition에 Risk Level도 필요해?
A. 필요하다. 위험도에 따라 자동 실행, 로그, 사용자 확인 기준이 달라진다.

Q. Tool Result 구조도 검수 대상이야?
A. 그렇다. success / error / blocked / partial 구분과 metadata 포함 여부를 확인해야 한다.

Q. 검수에 실패한 Tool은 어떻게 해?
A. Agent에 연결하지 않고 Tool Definition을 수정한 뒤 다시 검수한다.

---

# Retrieval Queries

### [FAQ]

Q. Tool Definition이 뭐야?
A. LLM이 Tool의 이름, 목적, 입력값, 결과, 위험도, 실패 조건을 이해하도록 제공하는 구조화된 설명이다.

Q. Tool Definition에는 무엇이 들어가야 해?
A. toolName, description, parameters, requiredFields, returnType, sideEffect, permissionLevel, riskLevel, requiresConfirmation, failureCases가 들어가야 한다.

Q. Tool Name은 어떻게 지어야 해?
A. search_rag_documents, read_project_file처럼 짧고 명확한 동사 + 대상 구조로 짓는 것이 좋다.

Q. Tool Description은 어떻게 작성해야 해?
A. Tool이 무엇을 하는지, 언제 사용해야 하는지, 무엇을 하지 않는지를 짧고 구체적으로 작성한다.

Q. Tool Description이 모호하면 어떤 문제가 생겨?
A. LLM이 잘못된 Tool을 선택하거나 잘못된 Tool Arguments를 생성할 수 있다.

Q. Parameters는 뭐야?
A. Tool Execution에 필요한 Tool Arguments의 구조를 정의한 것이다.

Q. Tool Parameters는 왜 JSON Schema로 정의해?
A. LLM이 구조화된 Tool Arguments를 생성하고 Runtime이 실행 전 검증하기 쉽게 하기 위해서다.

Q. JSON Schema는 무엇을 정의해?
A. type, properties, required, enum, minimum, maximum, array item type 같은 입력 제약을 정의한다.

Q. JSON Schema만 있으면 안전해?
A. 아니다. Business Validation, Permission Check, Risk Check, Human Confirmation이 추가로 필요하다.

Q. Required Fields는 왜 필요해?
A. Tool 실행에 반드시 필요한 입력값을 누락하지 않도록 제한하기 위해 필요하다.

Q. Required Field가 누락되면 어떻게 해?
A. Tool을 실행하지 않고 ValidationError를 반환해야 한다.

Q. 빈 문자열도 Required Field로 인정해도 돼?
A. 대부분의 경우 안 된다. query, filePath 같은 값은 빈 문자열이면 ValidationError로 처리한다.

Q. Return Type은 왜 필요해?
A. Tool Execution 결과를 LLM과 다음 Agent가 안정적으로 해석할 수 있게 하기 위해 필요하다.

Q. Tool Result에는 어떤 필드가 좋아?
A. status, data, error, message, metadata, source, executionTimeMs, traceId를 포함하는 것이 좋다.

Q. Tool Result status는 무엇을 구분해야 해?
A. success, error, blocked, partial을 구분하는 것이 좋다.

Q. Side Effect가 뭐야?
A. Tool 실행이 파일, DB, 이메일, 배포, 결제처럼 외부 시스템 상태를 변경하는 효과다.

Q. Side Effect Tool은 어떻게 처리해?
A. Risk Level 분류, 입력 검증, 권한 확인, Human Confirmation, Audit Log를 적용한다.

Q. Permission Level은 왜 필요해?
A. Agent별 Tool 접근 권한을 제한하고 최소 권한 원칙을 적용하기 위해 필요하다.

Q. permissionLevel에는 어떤 값이 있어?
A. none, read, validate, write, execute, admin 같은 값을 사용할 수 있다.

Q. PM Agent는 어떤 Tool 권한이 적절해?
A. RAG Search와 Task Routing 중심의 read / route 권한이 적절하다.

Q. Review Agent는 어떤 Tool 권한이 적절해?
A. read와 validate 권한 중심이 적절하며, 직접 수정 권한은 제한하는 것이 좋다.

Q. Risk Level은 왜 필요해?
A. Tool 실행 위험도에 따라 자동 실행, 로그 기록, Human Confirmation 여부를 결정하기 위해 필요하다.

Q. riskLevel에는 어떤 값이 있어?
A. low, medium, high를 사용할 수 있다.

Q. High Risk Tool은 어떻게 처리해?
A. Human Confirmation, Preview, Audit Log, Approval Scope 검증을 적용한다.

Q. Failure Case는 왜 정의해야 해?
A. Tool 실패 조건을 예측하고 ValidationError, PermissionError, TimeoutError 같은 오류를 구조화하기 위해 필요하다.

Q. Tool 실패 시 retryable은 왜 필요해?
A. 재시도 가능한 오류와 재시도하면 안 되는 오류를 구분하기 위해 필요하다.

Q. Complete Tool Definition이 뭐야?
A. Tool Name, Description, Schema, Return Type, Side Effect, Permission, Risk, Confirmation, Failure Case를 모두 포함한 통합 정의다.

Q. Tool Definition 검수 Checklist에는 무엇이 있어야 해?
A. Tool Name, Description, Parameters, Required Fields, Return Type, Side Effect, Permission Level, Risk Level, Failure Case를 확인해야 한다.

Q. Tool Definition의 최종 목표는 뭐야?
A. LLM이 올바른 Tool을 선택하고 안전한 Tool Arguments를 생성하며 Runtime이 검증 가능한 방식으로 Tool을 실행하게 만드는 것이다.
