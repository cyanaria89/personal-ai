# LLM Core & API Integration Part06 - Function Calling & Tool Calling

---

# 1. Function Calling / Tool Calling

## 1.1 Function Calling

### [개념]

Function Calling은 LLM이 사용자 요청을 처리하기 위해 호출해야 할 외부 함수를 선택하고, 함수 실행에 필요한 Arguments를 구조화해서 생성하는 방식이다.

LLM은 함수를 직접 실행하지 않는다.

LLM은 다음을 생성한다.

- Function Name
- Function Arguments
- Tool Call Request
- Intermediate Reasoning Result
- Final Response Candidate

Function Calling 기본 Flow:

```text
User Request
→ LLM Analyzes Intent
→ LLM Selects Function
→ LLM Generates Arguments
→ Application Validates Arguments
→ Application Executes Function
→ Function Result Returned to LLM
→ LLM Generates Final Response
```

---

### [핵심]

- Function Calling은 LLM이 외부 기능을 사용할 수 있게 하는 구조이다.
- LLM은 Function을 직접 실행하지 않고 호출 요청을 생성한다.
- 실제 실행은 Application 또는 Tool Runtime이 담당한다.
- Function Arguments는 반드시 검증해야 한다.
- Function Result는 다시 LLM Context로 전달될 수 있다.
- 위험 작업은 사용자 승인 절차가 필요하다.
- Function Calling은 Agent Workflow의 핵심 기반이다.

---

### [실무]

2026 실무 기준 Function Calling은 Agent, RAG, Backend Automation, Personal AI Server에서 핵심 기능으로 사용된다.

대표 사용 사례:

| 사용 사례   | Function           |
| ----------- | ------------------ |
| 문서 검색   | `search_documents` |
| DB 조회     | `query_database`   |
| 파일 읽기   | `read_file`        |
| 코드 실행   | `run_code`         |
| 일정 조회   | `search_calendar`  |
| 이메일 검색 | `search_email`     |
| 웹 검색     | `web_search`       |
| RAG 검색    | `retrieve_context` |
| 코드 리뷰   | `analyze_code`     |

Function Calling 설계 기준:

```text
Tool Definition
→ Function Schema
→ Argument Validation
→ Permission Check
→ Function Execution
→ Result Validation
→ Tool Message
→ Final Response
```

주의:

- LLM이 생성한 Function Arguments를 그대로 실행하지 않는다.
- 파일 삭제, 결제, 배포, 이메일 전송, DB 수정은 승인 절차가 필요하다.
- Function Result에 Secret이 포함될 수 있으므로 Redaction이 필요하다.
- Function이 실패했을 때 실패 상태를 명확히 LLM에게 전달해야 한다.
- Function 수가 너무 많으면 Tool Selection 품질이 낮아질 수 있다.

---

### [FAQ]

Q. Function Calling이 뭐야?

A. LLM이 외부 함수를 선택하고 실행에 필요한 Arguments를 생성하는 구조다.

Q. LLM이 Function을 직접 실행해?

A. 아니다. LLM은 호출 요청을 만들고 실제 실행은 Application이나 Tool Runtime이 수행한다.

Q. Function Arguments는 왜 검증해야 해?

A. 잘못된 인자나 위험한 인자가 실행되면 오류, 비용 발생, 보안 문제가 생길 수 있기 때문이다.

Q. Function Calling은 Agent에 왜 중요해?

A. Agent가 검색, 파일 처리, API 호출, 코드 실행 같은 외부 작업을 수행할 수 있게 해주기 때문이다.

---

## 1.2 Tool Calling

### [개념]

Tool Calling은 LLM이 외부 Tool을 선택하고 Tool Arguments를 생성해 Tool Runtime이 실행하도록 만드는 구조이다.

Tool Calling은 Function Calling보다 넓은 개념으로 사용할 수 있다.

Tool은 함수뿐 아니라 외부 시스템, API, 검색기, DB, 파일 시스템, 코드 실행기, 브라우저, RAG Retriever를 포함할 수 있다.

Tool Calling 구성 요소:

- Tool Definition
- Tool Name
- Tool Description
- Tool Parameters
- Tool Arguments
- Tool Choice
- Tool Result
- Tool Message
- Final Response

Tool Calling Flow:

```text
User Request
→ LLM Chooses Tool
→ LLM Generates Tool Arguments
→ Validate Arguments
→ Execute Tool
→ Return Tool Result
→ LLM Uses Result
→ Final Response
```

---

### [핵심]

- Tool Calling은 LLM이 외부 시스템을 사용할 수 있게 한다.
- Tool Description은 Tool 선택 품질에 직접 영향을 준다.
- Tool Arguments는 Schema 기반으로 제한해야 한다.
- Tool Result는 검증 후 LLM에게 전달해야 한다.
- Tool Calling은 RAG, Agent, Automation의 핵심 기능이다.
- Tool 실패, 빈 결과, 권한 오류를 명확히 처리해야 한다.
- Tool이 너무 많으면 LLM의 Tool 선택 정확도가 낮아질 수 있다.

---

### [실무]

Tool Calling 대표 구조:

```json
{
  "name": "search_documents",
  "description": "Search RAG documents by semantic query.",
  "parameters": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string"
      },
      "topK": {
        "type": "integer",
        "minimum": 1,
        "maximum": 10
      }
    },
    "required": ["query"]
  }
}
```

Tool Calling 처리 기준:

| 단계                | 처리                       |
| ------------------- | -------------------------- |
| Tool Selection      | LLM이 Tool 선택            |
| Argument Generation | LLM이 Arguments 생성       |
| Schema Validation   | 타입, 필수 필드 검증       |
| Business Validation | 권한, 범위, 위험도 검증    |
| Execution           | Application이 Tool 실행    |
| Result Validation   | Null, Error, Secret 검증   |
| Tool Message        | LLM에게 결과 전달          |
| Final Answer        | Tool Result 기반 답변 생성 |

주의:

- Tool Description은 짧고 명확해야 한다.
- 비슷한 Tool이 많으면 선택 오류가 증가한다.
- Tool Arguments에 사용자 입력이 포함될 수 있으므로 Injection을 고려한다.
- Tool Result를 사실 데이터로 사용하되 최신성, 권한, 오류 여부를 확인한다.
- Tool 실행 로그에는 Secret을 남기지 않는다.

---

### [FAQ]

Q. Tool Calling이 뭐야?

A. LLM이 외부 도구를 선택하고 인자를 생성해 Application이 실행하도록 만드는 구조다.

Q. Tool과 Function 차이는?

A. Function은 코드 함수 중심이고, Tool은 검색기, DB, API, 파일 시스템 같은 외부 기능까지 포함하는 더 넓은 개념이다.

Q. Tool Description이 중요한 이유는?

A. LLM이 어떤 Tool을 선택할지 판단할 때 Tool Description을 참고하기 때문이다.

Q. Tool Calling에서 가장 중요한 보안 기준은?

A. Tool Arguments 검증, 권한 확인, 위험 작업 승인, Secret Redaction이다.

---

## 1.3 Tool Choice

### [개념]

Tool Choice는 LLM이 어떤 Tool을 사용할지 또는 Tool을 사용할지 말지를 결정하는 방식이다.

Tool Choice는 자동 선택, 특정 Tool 강제, Tool 사용 금지, 병렬 Tool 호출 같은 형태로 설계할 수 있다.

Tool Choice 유형:

- Auto Tool Choice
- Required Tool Choice
- Forced Tool Choice
- No Tool
- Parallel Tool Calls
- Sequential Tool Calls

---

### [핵심]

- Auto Tool Choice는 LLM이 Tool 사용 여부를 판단한다.
- Forced Tool Choice는 특정 Tool을 반드시 사용하게 한다.
- No Tool은 LLM이 Tool 없이 답변하게 한다.
- Tool이 필요한 작업과 필요 없는 작업을 구분해야 한다.
- Tool 선택 실패는 잘못된 답변이나 불필요한 비용을 만든다.
- Tool Choice 기준은 Agent Role과 작업 유형별로 다르게 설정한다.

---

### [실무]

Tool Choice 판단 기준:

| 요청 유형      | Tool Choice             |
| -------------- | ----------------------- |
| 문서 기반 질의 | RAG Search Tool         |
| 최신 정보 확인 | Web Search Tool         |
| 계산           | Calculator Tool         |
| 파일 내용 분석 | File Read Tool          |
| 코드 실행 검증 | Code Execution Tool     |
| 단순 설명      | No Tool 가능            |
| 위험 작업      | Human Confirmation 필요 |

Tool Choice Flow:

```text
User Request
→ Need External Data?
→ Need Current Data?
→ Need User Data?
→ Need Execution?
→ Need Approval?
→ Select Tool or No Tool
```

Tool Choice 예:

```json
{
  "tool_choice": {
    "type": "function",
    "function": {
      "name": "search_documents"
    }
  }
}
```

주의:

- 최신 정보가 필요한 질문에 No Tool로 답하면 오답 가능성이 높다.
- 문서 근거가 필요한 RAG 질문은 Retrieval Tool을 우선 사용한다.
- 위험 작업은 Tool Choice 이전에 승인 필요 여부를 확인한다.
- Tool 사용이 불필요한 질문에 Tool을 호출하면 비용과 Latency가 증가한다.
- Tool Choice 실패 로그를 분석해 Tool Description을 개선한다.

---

### [FAQ]

Q. Tool Choice가 뭐야?

A. LLM이 Tool을 사용할지, 어떤 Tool을 사용할지 결정하는 방식이다.

Q. Auto Tool Choice는 뭐야?

A. LLM이 사용자 요청을 보고 Tool 사용 여부와 Tool 종류를 자동으로 선택하는 방식이다.

Q. Forced Tool Choice는 언제 써?

A. 반드시 특정 Tool을 사용해야 하는 RAG 검색, DB 조회, 검증 작업에서 사용할 수 있다.

Q. Tool을 안 써도 되는 경우는?

A. 외부 정보나 실행이 필요 없는 일반 개념 설명, 단순 요약, 이미 제공된 텍스트 처리에는 Tool 없이 가능하다.

---

# 2. Tool Definition Design

## 2.1 Tool Definition

### [개념]

Tool Definition은 LLM에게 사용 가능한 Tool의 이름, 목적, 입력 Schema, 제한 조건을 알려주는 명세이다.

Tool Definition이 명확할수록 LLM의 Tool Selection과 Argument Generation 품질이 좋아진다.

Tool Definition 구성:

- name
- description
- parameters
- required fields
- enum
- validation rules
- safety rules
- examples

---

### [핵심]

- Tool Name은 짧고 의미가 분명해야 한다.
- Tool Description은 Tool 사용 목적을 명확히 설명해야 한다.
- Parameters는 JSON Schema 형태로 제한하는 것이 좋다.
- Required Field는 최소화한다.
- Enum은 가능한 값만 허용한다.
- 위험한 옵션은 Tool Definition에서 제한한다.
- Tool Definition은 실제 Tool 기능과 일치해야 한다.

---

### [실무]

좋은 Tool Definition 예:

```json
{
  "name": "retrieve_rag_context",
  "description": "Retrieve relevant RAG document chunks for a user query. Use this when the answer must be grounded in uploaded RAG documents.",
  "parameters": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "Search query for semantic retrieval."
      },
      "domain": {
        "type": "string",
        "enum": [
          "LLM_Core_API_Integration",
          "Prompt_Engineering",
          "Vector_Database_RAG"
        ]
      },
      "topK": {
        "type": "integer",
        "minimum": 1,
        "maximum": 10
      }
    },
    "required": ["query"]
  }
}
```

나쁜 Tool Definition 예:

```json
{
  "name": "do_stuff",
  "description": "Do something.",
  "parameters": {}
}
```

Tool Definition Checklist:

```text
Tool 이름이 명확한가?
Tool Description이 사용 조건을 포함하는가?
Arguments Schema가 제한적인가?
Required Field가 과도하지 않은가?
Enum으로 허용 값을 제한했는가?
위험 작업이 포함되어 있으면 승인 조건이 있는가?
실제 Tool 기능과 Description이 일치하는가?
```

주의:

- Tool 이름을 모호하게 만들지 않는다.
- 하나의 Tool에 너무 많은 기능을 넣지 않는다.
- Tool Description에 실제 불가능한 기능을 쓰지 않는다.
- LLM이 자유 문자열로 위험 작업을 지정하게 두지 않는다.
- Tool Definition 변경 시 테스트 케이스를 갱신한다.

---

### [FAQ]

Q. Tool Definition이 뭐야?

A. LLM에게 Tool의 이름, 목적, 입력 Schema, 사용 조건을 알려주는 명세다.

Q. 좋은 Tool Definition의 기준은?

A. 이름이 명확하고, 설명이 구체적이며, Arguments Schema가 제한적이고 검증 가능해야 한다.

Q. Tool Description은 길수록 좋아?

A. 아니다. 짧고 명확하게 Tool의 목적과 사용 조건을 설명하는 것이 좋다.

Q. Tool Definition이 나쁘면 어떻게 돼?

A. LLM이 잘못된 Tool을 선택하거나 잘못된 Arguments를 생성할 가능성이 높아진다.

---

## 2.2 Function Schema

### [개념]

Function Schema는 Function Calling 또는 Tool Calling에서 Arguments의 구조, 타입, 필수 필드, 허용 값을 정의하는 Schema이다.

Function Schema는 LLM Output을 제한하고 Application Validation의 기준이 된다.

Function Schema 요소:

- type
- properties
- required
- enum
- minimum
- maximum
- items
- description
- additionalProperties

---

### [핵심]

- Function Schema는 Arguments 구조를 제한한다.
- Required Field는 최소한으로 지정한다.
- Enum은 잘못된 값 생성을 줄인다.
- 숫자 범위는 minimum과 maximum으로 제한한다.
- 문자열은 의미와 금지 조건을 description에 작성한다.
- Schema가 복잡할수록 생성 실패 가능성이 높아진다.
- Schema Validation은 실행 전 필수이다.

---

### [실무]

Function Schema 예:

```json
{
  "type": "object",
  "properties": {
    "query": {
      "type": "string",
      "description": "User query for document search. Must not be empty."
    },
    "topK": {
      "type": "integer",
      "description": "Number of chunks to retrieve.",
      "minimum": 1,
      "maximum": 10
    },
    "includeCode": {
      "type": "boolean",
      "description": "Whether code snippets should be prioritized."
    }
  },
  "required": ["query"]
}
```

Schema 설계 기준:

| 항목                 | 권장 기준             |
| -------------------- | --------------------- |
| Required             | 꼭 필요한 필드만      |
| String               | 빈 문자열 금지 검증   |
| Integer              | 최소/최대 범위 지정   |
| Enum                 | 가능한 값 제한        |
| Boolean              | 의미 명확히 설명      |
| Array                | 최대 길이 제한        |
| Object               | 깊은 중첩 최소화      |
| additionalProperties | 불필요 필드 차단 검토 |

주의:

- Schema만으로 보안 검증이 끝나지 않는다.
- Business Rule Validation을 별도로 수행한다.
- 파일 경로, URL, SQL, Shell Command는 추가 검증이 필요하다.
- Schema가 너무 깊으면 LLM이 필드를 누락할 수 있다.
- Provider별 JSON Schema 지원 범위가 다를 수 있다.

---

### [FAQ]

Q. Function Schema가 뭐야?

A. Tool 또는 Function Arguments의 구조, 타입, 필수 필드, 허용 값을 정의하는 Schema다.

Q. Function Schema는 왜 필요해?

A. LLM이 생성하는 Arguments를 제한하고 실행 전 검증하기 위해 필요하다.

Q. Required Field는 많이 넣을수록 좋아?

A. 아니다. 꼭 필요한 필드만 Required로 지정하는 것이 안정적이다.

Q. Schema Validation만 하면 안전해?

A. 아니다. 권한, 위험 작업, 파일 경로, 업무 규칙 같은 Business Validation이 추가로 필요하다.

---

## 2.3 Tool Granularity

### [개념]

Tool Granularity는 Tool을 얼마나 작고 구체적인 단위로 나눌지 결정하는 설계 기준이다.

Tool이 너무 크면 위험하고 모호해진다.

Tool이 너무 작으면 Tool 수가 많아져 선택 품질이 떨어질 수 있다.

---

### [핵심]

- Tool은 하나의 명확한 책임을 가져야 한다.
- 너무 많은 기능을 가진 Tool은 Argument가 복잡해진다.
- 너무 작은 Tool이 많으면 LLM이 Tool을 잘못 선택할 수 있다.
- 위험 작업과 읽기 작업은 분리해야 한다.
- 조회 Tool과 수정 Tool은 분리하는 것이 안전하다.
- Agent Role별 Tool Set을 제한하는 것이 좋다.

---

### [실무]

Tool Granularity 예:

좋은 분리:

```text
search_documents
read_document
summarize_document
validate_json_output
create_draft_email
send_email
```

나쁜 통합:

```text
manage_everything
handle_file_and_email_and_db
execute_any_command
```

권장 분리 기준:

| Tool 유형         | 권장                |
| ----------------- | ------------------- |
| Read Tool         | 안전한 조회 전용    |
| Write Tool        | 승인 또는 권한 필요 |
| Delete Tool       | 강한 승인 필요      |
| Search Tool       | Query와 Filter 중심 |
| Execution Tool    | Sandbox 제한        |
| External API Tool | Rate Limit 고려     |
| User Data Tool    | Privacy 기준 필요   |

Agent별 Tool Set 예:

```text
PM Agent
→ search_documents
→ summarize_requirements

Backend Agent
→ search_documents
→ read_code_file
→ generate_code_patch

Review Agent
→ analyze_code
→ validate_output
→ run_tests

DevOps Agent
→ read_config
→ validate_deploy_plan
```

주의:

- 모든 Agent에게 모든 Tool을 주지 않는다.
- 위험 Tool은 기본 Tool Set에서 제외한다.
- Tool이 많아질수록 Tool Router가 필요할 수 있다.
- Tool 선택 실패 로그를 기반으로 Tool Description과 Granularity를 개선한다.
- 읽기 전용 Tool과 쓰기 Tool을 같은 이름으로 묶지 않는다.

---

### [FAQ]

Q. Tool Granularity가 뭐야?

A. Tool을 어느 정도 크기와 책임 단위로 나눌지 정하는 설계 기준이다.

Q. Tool은 작을수록 좋아?

A. 항상 그렇지 않다. 너무 작으면 Tool 수가 많아져 선택 오류가 늘 수 있다.

Q. Tool이 너무 크면 뭐가 문제야?

A. 기능이 모호해지고 Arguments가 복잡해져 안전성과 선택 품질이 낮아진다.

Q. 조회 Tool과 수정 Tool은 분리해야 해?

A. 권장한다. 읽기 작업과 쓰기 작업은 위험도가 다르기 때문이다.

---

# 3. Tool Argument Validation

## 3.1 Argument Validation

### [개념]

Argument Validation은 LLM이 생성한 Tool Arguments가 실행 가능한지, 안전한지, Schema와 업무 규칙을 만족하는지 확인하는 과정이다.

Argument Validation은 Tool Calling 안전성의 핵심이다.

Validation 종류:

- JSON Parse Validation
- Schema Validation
- Required Field Validation
- Type Validation
- Range Validation
- Enum Validation
- Business Rule Validation
- Permission Validation
- Safety Validation

---

### [핵심]

- Tool Arguments는 절대 그대로 신뢰하지 않는다.
- Schema Validation은 실행 전 필수이다.
- 업무 규칙 검증은 Schema Validation과 별도로 필요하다.
- 위험 작업은 사용자 승인 여부를 확인한다.
- Secret 포함 여부를 검사한다.
- 파일 경로, SQL, Shell Command, URL은 추가 검증이 필요하다.
- Validation 실패 시 Tool을 실행하지 않는다.

---

### [실무]

Argument Validation Flow:

```text
LLM Tool Call
→ Parse Arguments
→ Schema Validation
→ Required Field Check
→ Type / Range / Enum Check
→ Business Rule Check
→ Permission Check
→ Safety Check
→ Execute Tool or Reject
```

Validation 예:

```json
{
  "tool": "retrieve_rag_context",
  "arguments": {
    "query": "Streaming Response 처리 방법",
    "topK": 5,
    "domain": "LLM_Core_API_Integration"
  }
}
```

검증 기준:

| Argument | Validation                |
| -------- | ------------------------- |
| query    | 빈 문자열 금지, 길이 제한 |
| topK     | 1 이상 10 이하            |
| domain   | 허용 Enum만               |
| filePath | 허용 디렉터리 내부        |
| url      | 허용 Domain 또는 Protocol |
| sql      | Read-only 여부            |
| command  | Sandbox 허용 명령만       |
| emailTo  | 유효한 주소와 승인 여부   |

Validation 실패 응답 예:

```json
{
  "status": "failed",
  "errorCode": "invalid_tool_arguments",
  "message": "topK must be between 1 and 10.",
  "toolExecuted": false
}
```

주의:

- Validation 실패 시 Tool을 부분 실행하지 않는다.
- LLM에게 실패 원인을 구조화해서 전달한다.
- 재시도는 Max Retry를 둔다.
- 위험 인자를 자동 수정해 실행하지 않는다.
- Validation 로그에는 Secret이나 민감한 사용자 입력을 남기지 않는다.

---

### [FAQ]

Q. Argument Validation이 뭐야?

A. LLM이 생성한 Tool Arguments가 Schema, 업무 규칙, 보안 기준을 만족하는지 확인하는 과정이다.

Q. Tool Arguments를 그대로 실행하면 안 돼?

A. 안 된다. 잘못된 인자가 파일 삭제, 비용 발생, 보안 문제를 만들 수 있다.

Q. Schema Validation과 Business Rule Validation 차이는?

A. Schema Validation은 타입과 구조를 확인하고, Business Rule Validation은 권한, 위험도, 업무 규칙을 확인한다.

Q. Validation 실패 시 Tool을 실행해도 돼?

A. 안 된다. 실패 원인을 반환하고 Tool 실행을 중단해야 한다.

---

## 3.2 Permission Check

### [개념]

Permission Check는 Tool 실행 전에 사용자가 해당 작업을 수행할 권한이 있는지 확인하는 과정이다.

Tool Calling에서 Permission Check는 데이터 보호, 사용자 안전, 시스템 안정성에 필수이다.

권한 확인 대상:

- User Role
- Workspace Permission
- File Access
- Database Access
- Email Access
- Calendar Access
- External API Permission
- Production Environment Access

---

### [핵심]

- Tool 실행 전 권한을 확인해야 한다.
- 읽기 권한과 쓰기 권한은 분리한다.
- 사용자 데이터 접근은 최소 권한 원칙을 적용한다.
- Production 환경 작업은 추가 승인 또는 차단이 필요하다.
- 권한 부족 시 Tool을 실행하지 않는다.
- 권한 오류는 명확히 반환한다.

---

### [실무]

Permission Check Flow:

```text
Tool Request
→ Identify User
→ Check Role
→ Check Resource Permission
→ Check Operation Type
→ Check Environment
→ Allow or Deny
```

권한 기준 예:

| 작업        | 권한 기준                   |
| ----------- | --------------------------- |
| 문서 검색   | Workspace Read              |
| 파일 읽기   | File Read Permission        |
| 파일 수정   | File Write Permission       |
| DB 조회     | Read-only DB Permission     |
| DB 수정     | Write Permission + Approval |
| 이메일 전송 | User Confirmation           |
| 배포        | DevOps Role + Approval      |
| 결제        | Strong Confirmation         |

권한 실패 응답 예:

```json
{
  "status": "failed",
  "errorCode": "permission_denied",
  "message": "User does not have permission to execute this tool.",
  "toolExecuted": false
}
```

주의:

- LLM의 판단으로 권한을 대체하지 않는다.
- 사용자가 요청했다고 해서 모든 권한이 있는 것은 아니다.
- 권한 확인 결과를 우회할 수 없게 서버에서 검증한다.
- 민감 데이터 접근은 로그와 감사 기록을 남긴다.
- 권한 실패 시 세부 내부 정책을 과도하게 노출하지 않는다.

---

### [FAQ]

Q. Permission Check가 뭐야?

A. Tool 실행 전에 사용자가 해당 리소스와 작업에 대한 권한을 갖고 있는지 확인하는 과정이다.

Q. LLM이 권한을 판단해도 돼?

A. 안 된다. 권한 판단은 Application 또는 서버 권한 시스템이 수행해야 한다.

Q. 읽기 권한과 쓰기 권한은 분리해야 해?

A. 그렇다. 조회와 수정은 위험도가 다르므로 분리하는 것이 안전하다.

Q. 권한이 없으면 어떻게 처리해?

A. Tool을 실행하지 않고 permission_denied 상태를 반환해야 한다.

---

## 3.3 Safety Check

### [개념]

Safety Check는 Tool Arguments와 Tool Execution이 위험 작업, 민감정보 노출, 시스템 손상, 비용 발생, 보안 사고를 유발하지 않는지 확인하는 과정이다.

Safety Check는 Schema와 Permission을 통과한 뒤에도 별도로 필요하다.

위험 유형:

- Destructive Operation
- External Side Effect
- Secret Exposure
- Prompt Injection
- Data Exfiltration
- Production Change
- Payment / Cost Trigger
- Email / Message Sending
- File Delete / Overwrite

---

### [핵심]

- Safety Check는 위험 작업을 차단하거나 승인 단계로 보낸다.
- 삭제, 결제, 배포, 전송은 강한 승인 대상이다.
- Secret이 Arguments나 Result에 포함되면 차단한다.
- Prompt Injection이 Tool Arguments에 섞일 수 있다.
- 외부 전송은 데이터 유출 위험을 확인해야 한다.
- Tool Result에도 민감정보가 있을 수 있다.

---

### [실무]

Safety Check Flow:

```text
Validated Arguments
→ Detect Destructive Operation
→ Detect External Side Effect
→ Detect Secret
→ Detect Production Target
→ Detect Data Export
→ Require Confirmation or Reject
```

위험 작업 분류:

| 작업              | 처리             |
| ----------------- | ---------------- |
| 파일 읽기         | 허용 가능        |
| 파일 수정         | 권한 확인        |
| 파일 삭제         | 사용자 승인 필요 |
| 이메일 Draft 생성 | 허용 가능        |
| 이메일 전송       | 사용자 승인 필요 |
| DB Select         | 허용 가능        |
| DB Update/Delete  | 승인 필요        |
| 결제 요청         | 강한 승인 필요   |
| 배포 실행         | 강한 승인 필요   |
| 외부 API 전송     | 데이터 검토 필요 |

Safety 실패 응답 예:

```json
{
  "status": "human_confirmation_required",
  "reason": "The requested tool operation may modify production resources.",
  "toolExecuted": false,
  "requiredConfirmation": "Confirm production deployment."
}
```

주의:

- 위험 작업을 자동으로 실행하지 않는다.
- 승인 전에는 Tool을 실행하지 않는다.
- 승인 메시지는 작업 대상과 영향을 명확히 설명해야 한다.
- Secret은 LLM Context와 로그에서 제거한다.
- Tool Result를 다시 LLM에게 전달하기 전 Redaction을 수행한다.

---

### [FAQ]

Q. Safety Check가 뭐야?

A. Tool 실행이 위험 작업, Secret 노출, 시스템 손상, 비용 발생을 유발하지 않는지 확인하는 과정이다.

Q. Schema와 Permission을 통과해도 Safety Check가 필요해?

A. 필요하다. 구조와 권한이 맞아도 작업 자체가 위험할 수 있기 때문이다.

Q. 어떤 작업은 사용자 승인이 필요해?

A. 파일 삭제, DB 수정, 이메일 전송, 결제, 배포, Production 설정 변경이 승인 대상이다.

Q. Secret이 Tool Arguments에 있으면?

A. Tool 실행을 차단하거나 Secret을 제거하고 보안 이벤트로 처리해야 한다.

---

# 4. Tool Execution and Result Handling

## 4.1 Tool Execution

### [개념]

Tool Execution은 검증된 Tool Call을 Application이 실제 외부 함수, API, DB, 파일 시스템, 검색기, 코드 실행기에 전달해 수행하는 단계이다.

LLM은 Tool Execution을 직접 수행하지 않는다.

Tool Execution Flow:

```text
Validated Tool Call
→ Execute Tool Runtime
→ Capture Result
→ Capture Error
→ Normalize Response
→ Return Tool Result
```

---

### [핵심]

- Tool Execution은 Application 책임이다.
- 실행 전 Arguments와 권한 검증이 완료되어야 한다.
- Tool 실행은 Timeout을 가져야 한다.
- Tool 실패는 구조화된 Error로 반환한다.
- Tool 실행 결과는 표준 Response Format으로 정규화한다.
- Tool 실행 로그에는 requestId와 toolName을 포함한다.
- Secret은 로그에 남기지 않는다.

---

### [실무]

Tool Execution Response 표준 예:

```json
{
  "status": "success",
  "toolName": "retrieve_rag_context",
  "data": {
    "chunks": [
      {
        "document": "LLM_Core_API_Integration_Part05",
        "section": "Streaming Response",
        "content": "Streaming Response는 Chunk를 순차적으로 전달한다."
      }
    ]
  },
  "error": null
}
```

Tool Error Response 예:

```json
{
  "status": "failed",
  "toolName": "retrieve_rag_context",
  "data": null,
  "error": {
    "code": "timeout",
    "message": "Document retrieval timed out."
  }
}
```

실행 기준:

| 항목          | 기준                        |
| ------------- | --------------------------- |
| Timeout       | 필수                        |
| Retry         | 제한적 적용                 |
| Idempotency   | 쓰기 작업에서 중요          |
| Logging       | requestId, toolName, status |
| Error Mapping | 사용자 친화적 오류          |
| Result Limit  | 과도한 결과 제한            |
| Redaction     | Secret 제거                 |

주의:

- Tool Timeout이 없으면 Agent Loop가 멈출 수 있다.
- Tool 실패를 빈 결과와 구분한다.
- Tool Runtime 오류를 LLM에게 그대로 노출하지 않는다.
- 쓰기 작업은 Idempotency와 중복 실행을 고려한다.
- Tool 실행 결과가 너무 크면 요약하거나 필드 선택을 수행한다.

---

### [FAQ]

Q. Tool Execution은 누가 수행해?

A. LLM이 아니라 Application 또는 Tool Runtime이 수행한다.

Q. Tool Execution 전에 무엇을 해야 해?

A. Arguments 검증, 권한 확인, Safety Check를 완료해야 한다.

Q. Tool 실행 결과는 어떻게 반환해?

A. success, data, error를 포함한 표준 구조로 반환하는 것이 좋다.

Q. Tool Timeout은 왜 필요해?

A. Tool이 무한 대기하면 Agent Workflow 전체가 멈출 수 있기 때문이다.

---

## 4.2 Tool Result

### [개념]

Tool Result는 Tool Execution 이후 생성된 결과 데이터이다.

Tool Result는 LLM에게 Tool Message로 전달되어 최종 답변 또는 다음 Tool 호출의 근거로 사용된다.

Tool Result 유형:

- Search Result
- RAG Retrieved Context
- Database Result
- File Content
- API Response
- Code Execution Output
- Test Result
- Error Result

---

### [핵심]

- Tool Result는 LLM이 최종 답변을 생성하는 근거가 된다.
- Tool Result도 검증해야 한다.
- Tool Result가 비어 있으면 Empty Result로 처리한다.
- Tool 실패와 검색 결과 없음은 구분해야 한다.
- Tool Result는 필요한 필드만 LLM에게 전달한다.
- Secret과 개인정보는 전달 전 제거한다.
- Tool Result가 너무 길면 요약 또는 Field Selection을 적용한다.

---

### [실무]

Tool Result 처리 Flow:

```text
Raw Tool Result
→ Check Status
→ Check Empty Result
→ Check Error
→ Redact Secret
→ Select Relevant Fields
→ Format Tool Message
→ Send to LLM
```

Tool Result Message 예:

```json
{
  "role": "tool",
  "name": "retrieve_rag_context",
  "content": {
    "status": "success",
    "chunks": [
      {
        "document": "LLM_Core_API_Integration_Part05",
        "section": "Streaming Response",
        "summary": "Streaming Response는 Chunk를 순차적으로 전달하는 방식이다."
      }
    ]
  }
}
```

Tool Result 상태 기준:

| 상태                  | 의미                      |
| --------------------- | ------------------------- |
| success               | 정상 결과 있음            |
| empty                 | 정상 실행됐지만 결과 없음 |
| failed                | Tool 실행 실패            |
| timeout               | 시간 초과                 |
| permission_denied     | 권한 없음                 |
| validation_failed     | 인자 검증 실패            |
| confirmation_required | 승인 필요                 |

주의:

- Tool Result 전체 원문을 무조건 Context에 넣지 않는다.
- 검색 결과 없음과 Tool 실패를 혼동하지 않는다.
- Tool Result에 포함된 HTML, Script, Prompt Injection 문구를 주의한다.
- Result가 긴 경우 Chunk, Summary, Metadata 중심으로 전달한다.
- Tool Result와 사용자 요청을 명확히 구분한다.

---

### [FAQ]

Q. Tool Result가 뭐야?

A. Tool 실행 후 생성된 결과 데이터이며 LLM의 최종 답변 근거로 사용된다.

Q. Tool Result도 검증해야 해?

A. 그렇다. 빈 결과, 실패, Secret 포함, 타입 오류, 오래된 정보 여부를 확인해야 한다.

Q. Tool 실패와 결과 없음은 같아?

A. 아니다. 실패는 실행 오류이고 결과 없음은 정상 실행됐지만 매칭 데이터가 없는 상태다.

Q. Tool Result 전체를 LLM에게 전달해도 돼?

A. 권장하지 않는다. 필요한 필드만 선택하고 Secret을 제거해 전달해야 한다.

---

## 4.3 Tool Message

### [개념]

Tool Message는 Tool Result를 LLM에게 전달하는 Message Role이다.

Tool Message는 LLM이 외부 실행 결과를 참고해 최종 답변을 생성하거나 다음 행동을 결정하게 한다.

Tool Message 구성:

- role
- tool_call_id
- name
- content
- status
- result
- error

---

### [핵심]

- Tool Message는 Tool Result를 LLM Context에 넣는 역할이다.
- Tool Message는 User Message와 구분해야 한다.
- Tool Message에는 검증된 결과만 넣는다.
- 실패 결과도 명확한 상태로 전달한다.
- Tool Message가 너무 길면 Context Window를 낭비한다.
- Tool Message에 Secret을 포함하지 않는다.

---

### [실무]

Tool Message 예:

```json
{
  "role": "tool",
  "tool_call_id": "call_001",
  "name": "search_documents",
  "content": "{\"status\":\"success\",\"summary\":\"Function Calling requires argument validation.\"}"
}
```

실패 Tool Message 예:

```json
{
  "role": "tool",
  "tool_call_id": "call_002",
  "name": "search_documents",
  "content": "{\"status\":\"empty\",\"message\":\"No matching documents found.\"}"
}
```

Tool Message 작성 기준:

| 항목         | 기준                   |
| ------------ | ---------------------- |
| status       | success, empty, failed |
| summary      | 짧은 요약              |
| data         | 필요한 결과            |
| error        | 실패 원인              |
| source       | 출처 식별자            |
| token length | 제한                   |
| redaction    | Secret 제거            |

주의:

- Tool Message에 사용자 명령처럼 보이는 문구가 포함될 수 있다.
- Tool Result 내부 Prompt Injection에 주의한다.
- Tool Message는 사실 데이터로 취급하되 검증된 범위로 제한한다.
- Tool Message를 System Rule보다 우선하지 않는다.
- Tool Message가 길면 Summary와 Source Reference로 압축한다.

---

### [FAQ]

Q. Tool Message가 뭐야?

A. Tool 실행 결과를 LLM에게 전달하는 Message Role이다.

Q. Tool Message와 User Message는 달라?

A. 다르다. User Message는 사용자 요청이고 Tool Message는 외부 Tool 실행 결과다.

Q. Tool Message에 실패 결과도 넣어?

A. 그렇다. 실패 상태와 원인을 명확히 전달해야 LLM이 다음 행동을 결정할 수 있다.

Q. Tool Message에 무엇을 넣으면 안 돼?

A. API Key, Secret, 개인정보, 과도한 원문, 검증되지 않은 위험 데이터를 넣으면 안 된다.

---

# 5. Tool Calling in RAG

## 5.1 RAG Retrieval Tool

### [개념]

RAG Retrieval Tool은 사용자 Query와 관련된 문서 Chunk를 검색해 LLM에게 Retrieved Context로 제공하는 Tool이다.

RAG Retrieval Tool은 Embedding Search, Keyword Search, Hybrid Search, Reranking을 사용할 수 있다.

RAG Retrieval Tool Flow:

```text
User Query
→ Query Rewrite
→ Retrieval Tool Call
→ Vector Search
→ Keyword Search
→ Reranking
→ Retrieved Context
→ LLM Grounded Answer
```

---

### [핵심]

- RAG Retrieval Tool은 문서 기반 답변의 근거를 제공한다.
- Query는 검색 친화적으로 변환할 수 있다.
- 검색 결과는 Context Filtering이 필요하다.
- Top-K는 과도하게 높이지 않는다.
- Retrieval Score만 믿지 않고 Chunk 적합성을 검토한다.
- Retrieved Context가 부족하면 Missing Information으로 처리한다.
- RAG Tool Result는 출처 Metadata를 포함하는 것이 좋다.

---

### [실무]

RAG Retrieval Tool Definition 예:

```json
{
  "name": "retrieve_rag_context",
  "description": "Retrieve relevant RAG document chunks for a query. Use when the answer must be based on RAG documents.",
  "parameters": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string"
      },
      "domain": {
        "type": "string"
      },
      "topK": {
        "type": "integer",
        "minimum": 1,
        "maximum": 10
      }
    },
    "required": ["query"]
  }
}
```

RAG Tool Result 예:

```json
{
  "status": "success",
  "chunks": [
    {
      "document": "LLM_Core_API_Integration_Part03",
      "section": "Retrieved Context",
      "content": "Retrieved Context는 RAG에서 검색된 문서 Chunk를 Prompt에 포함한 정보이다.",
      "score": 0.87
    }
  ]
}
```

실무 기준:

| 항목          | 기준                  |
| ------------- | --------------------- |
| Query Rewrite | 검색 적합성 개선      |
| Top-K         | 제한                  |
| Domain Filter | 문서 범위 제한        |
| Reranking     | 관련도 재정렬         |
| Deduplication | 중복 Chunk 제거       |
| Metadata      | 문서명, 섹션 포함     |
| Missing Rule  | 근거 없으면 추측 금지 |

주의:

- RAG Tool이 빈 결과를 반환하면 LLM이 일반 지식으로 답하지 않도록 한다.
- Retrieved Context와 User Question을 Prompt에서 분리한다.
- Tool Result가 오래되었거나 충돌하면 우선순위 기준을 적용한다.
- 검색 결과가 많으면 요약하지 말고 관련 Chunk를 선별한다.
- RAG 문서 변경 후 Embedding 재생성을 고려한다.

---

### [FAQ]

Q. RAG Retrieval Tool이 뭐야?

A. 사용자 Query와 관련된 문서 Chunk를 검색해 LLM에게 근거 Context로 제공하는 Tool이다.

Q. RAG Retrieval Tool은 언제 사용해?

A. 답변이 업로드된 문서나 RAG 문서에 근거해야 할 때 사용한다.

Q. RAG Tool Result에 무엇을 포함해야 해?

A. 문서명, 섹션, Chunk 내용, Score, Metadata를 포함하는 것이 좋다.

Q. RAG Tool이 빈 결과를 반환하면?

A. 문서에서 확인되지 않는다고 답하거나 추가 검색을 수행해야 한다.

---

## 5.2 Query Rewrite Tool

### [개념]

Query Rewrite Tool은 사용자 질문을 검색에 적합한 Query로 변환하는 Tool 또는 Agent 단계이다.

사용자 질문은 대화형 표현, 생략, 오타, 모호한 표현을 포함할 수 있다.

Query Rewrite는 RAG Retrieval 품질을 높인다.

Query Rewrite Flow:

```text
User Question
→ Extract Intent
→ Extract Keywords
→ Resolve Context
→ Build Search Query
→ Retrieve Documents
```

---

### [핵심]

- Query Rewrite는 검색 적중률을 높인다.
- 사용자 질문의 핵심 의도를 보존해야 한다.
- Domain Keyword를 포함하면 검색 품질이 좋아질 수 있다.
- 대화 맥락의 생략된 지시어를 보완한다.
- 원래 질문의 의미를 임의로 바꾸면 안 된다.
- Query Rewrite 결과도 검증 가능해야 한다.

---

### [실무]

Query Rewrite 예:

```text
User Question:
"이거 스트리밍에서 중간에 끊기면 어떻게 해?"

Rewritten Query:
"LLM Streaming Response Stream Failure Timeout Partial Output Handling"
```

RAG 문서용 Query Rewrite 예:

```json
{
  "originalQuestion": "Tool 인자 검증은 왜 필요해?",
  "rewrittenQuery": "Tool Calling Argument Validation Schema Validation Safety Check",
  "domain": "LLM_Core_API_Integration"
}
```

Rewrite 기준:

| 사용자 표현 | 보강 키워드                    |
| ----------- | ------------------------------ |
| 이거        | 현재 주제                      |
| 끊김        | Timeout, Failure, Cancellation |
| 이상함      | Error Handling, Validation     |
| 문서 근거   | Retrieved Context, RAG         |
| 도구 실행   | Tool Calling, Tool Execution   |
| 인자        | Arguments, Schema Validation   |

주의:

- Query Rewrite가 사용자의 의도를 바꾸면 안 된다.
- 검색 Query를 너무 길게 만들면 노이즈가 늘 수 있다.
- Query Rewrite 결과와 원문 질문을 함께 보관한다.
- 답변 생성에는 원문 질문을 유지하고 검색에는 Rewrite Query를 사용한다.
- 사용자 질문이 충분히 명확하면 Rewrite를 최소화한다.

---

### [FAQ]

Q. Query Rewrite Tool이 뭐야?

A. 사용자 질문을 RAG 검색에 더 적합한 Query로 변환하는 Tool 또는 단계다.

Q. Query Rewrite는 왜 필요해?

A. 사용자 질문은 생략이나 대화체가 많아 문서 검색에 바로 적합하지 않을 수 있기 때문이다.

Q. Query Rewrite에서 조심할 점은?

A. 사용자의 원래 의도를 바꾸지 않고 검색 키워드만 보강해야 한다.

Q. 답변에는 Rewrite Query를 써?

A. 검색에는 Rewrite Query를 사용하고, 최종 답변은 원문 질문 의도를 기준으로 작성한다.

---

# 6. Tool Calling in Agent Workflow

## 6.1 Agent Tool Use

### [개념]

Agent Tool Use는 Agent가 목표를 달성하기 위해 LLM을 통해 Tool을 선택하고 실행 결과를 다음 상태에 반영하는 구조이다.

Agent는 Tool Calling을 통해 단순 대화 모델에서 실행 가능한 Workflow 시스템으로 확장된다.

Agent Tool Use Flow:

```text
Agent State
→ Decide Need for Tool
→ Select Tool
→ Generate Arguments
→ Validate Arguments
→ Execute Tool
→ Update Agent State
→ Continue or Finalize
```

---

### [핵심]

- Agent는 필요할 때만 Tool을 사용해야 한다.
- Tool 사용 여부는 Agent Role과 Task에 따라 다르다.
- Agent State에 Tool Result를 반영한다.
- Tool Result는 다음 Agent 입력이 될 수 있다.
- Tool 실패 시 Recovery Strategy가 필요하다.
- Agent Loop에는 Max Step과 Stop Condition이 필요하다.
- Review Agent는 Tool 사용 결과를 검증할 수 있다.

---

### [실무]

Agent별 Tool Use 예:

| Agent          | Tool                                             |
| -------------- | ------------------------------------------------ |
| PM Agent       | requirement_parser, search_documents             |
| Backend Agent  | search_documents, read_code_file, generate_patch |
| Frontend Agent | search_documents, read_component_file            |
| Review Agent   | analyze_code, run_tests, validate_schema         |
| DevOps Agent   | read_config, validate_dockerfile                 |
| AI Agent       | retrieve_rag_context, evaluate_rag_answer        |

Agent Tool Use State 예:

```json
{
  "agent": "ReviewAgent",
  "currentTask": "Validate LLM API client code",
  "toolUsed": "analyze_code",
  "toolStatus": "success",
  "resultSummary": "Timeout handling is missing.",
  "nextAction": "Request fix from BackendAgent"
}
```

주의:

- Agent에게 불필요한 Tool을 많이 주지 않는다.
- Tool Result를 검증하지 않고 다음 Agent로 넘기지 않는다.
- Tool 실패 시 같은 요청을 무한 반복하지 않는다.
- Tool Arguments에 사용자 입력이 포함될 경우 Injection을 고려한다.
- Agent Output과 Tool Result를 Schema 기반으로 관리한다.

---

### [FAQ]

Q. Agent Tool Use가 뭐야?

A. Agent가 목표 달성을 위해 Tool을 선택하고 실행 결과를 상태에 반영하는 구조다.

Q. 모든 Agent에게 모든 Tool을 줘도 돼?

A. 권장하지 않는다. Agent Role에 필요한 Tool만 제공해야 선택 품질과 안전성이 좋아진다.

Q. Tool 실패 시 Agent는 어떻게 해야 해?

A. 실패 상태를 기록하고 재시도, 다른 Tool 선택, 사용자 확인, 안전 실패 중 하나로 분기해야 한다.

Q. Agent Loop에서 Tool Calling이 위험한 이유는?

A. 잘못 설계하면 같은 Tool을 반복 호출해 비용 증가와 무한 Loop가 발생할 수 있다.

---

## 6.2 Tool Calling Loop Control

### [개념]

Tool Calling Loop Control은 Agent가 Tool을 반복 호출할 때 무한 반복, 비용 폭증, 상태 오류를 방지하는 제어 방식이다.

Agent는 Tool Result를 보고 다시 Tool을 호출할 수 있지만 반드시 종료 조건이 있어야 한다.

Loop Control 요소:

- Max Steps
- Max Tool Calls
- Stop Condition
- Retry Limit
- Error Count
- State Change Check
- Human Confirmation
- Finalization Rule

---

### [핵심]

- Agent Loop는 무한 반복을 방지해야 한다.
- Max Tool Calls를 설정한다.
- 같은 Tool과 같은 Arguments 반복을 감지한다.
- Tool 실패 횟수를 제한한다.
- 상태가 변하지 않으면 Loop를 중단한다.
- 위험 작업은 승인 없이는 반복하지 않는다.
- Final Response 조건을 명확히 정의한다.

---

### [실무]

Loop Control Flow:

```text
Start Agent Step
→ Tool Call Count Check
→ Execute Tool
→ Compare State Change
→ Check Stop Condition
→ Continue or Finalize
```

Loop 제한 예:

```json
{
  "maxSteps": 8,
  "maxToolCalls": 5,
  "maxRetriesPerTool": 2,
  "stopConditions": [
    "final_answer_ready",
    "missing_information",
    "human_confirmation_required",
    "validation_failed"
  ]
}
```

반복 감지 기준:

| 문제                | 대응                |
| ------------------- | ------------------- |
| 같은 Tool 반복      | 중단 또는 다른 전략 |
| 같은 Arguments 반복 | 중단                |
| 연속 Timeout        | 실패 처리           |
| 결과 없음 반복      | Missing Information |
| 권한 오류 반복      | Permission Denied   |
| 위험 작업 반복      | Human Confirmation  |

주의:

- Retry와 Loop를 구분한다.
- Tool 실패가 반복되면 Prompt를 다시 생성하지 말고 상태를 종료한다.
- 비용이 큰 Tool은 호출 횟수를 낮게 제한한다.
- Agent가 Final Answer를 생성할 조건을 명확히 한다.
- Loop 종료 이유를 로그로 남긴다.

---

### [FAQ]

Q. Tool Calling Loop Control이 뭐야?

A. Agent가 Tool을 반복 호출할 때 무한 반복과 비용 폭증을 막는 제어 방식이다.

Q. Max Tool Calls가 왜 필요해?

A. 잘못된 Agent가 Tool을 무한 호출하는 것을 막기 위해 필요하다.

Q. 같은 Tool을 계속 호출하면 어떻게 해?

A. 같은 Arguments 반복 여부를 확인하고 상태 변화가 없으면 중단해야 한다.

Q. Tool 결과가 계속 없으면?

A. Missing Information으로 처리하거나 사용자 확인 단계로 넘긴다.

---

# 7. Error Handling and Retry

## 7.1 Tool Error Handling

### [개념]

Tool Error Handling은 Tool 호출, 검증, 실행, 결과 처리 중 발생하는 오류를 분류하고 안전하게 복구하는 방식이다.

Tool 오류는 LLM 오류와 다르게 외부 시스템 상태, 권한, 입력값, 네트워크, 데이터 상태와 관련될 수 있다.

Tool Error 유형:

- Invalid Arguments
- Permission Denied
- Safety Blocked
- Timeout
- Rate Limit
- Network Error
- External API Error
- Empty Result
- Parsing Error
- Execution Error

---

### [핵심]

- Tool Error는 유형별로 다르게 처리해야 한다.
- Invalid Arguments는 재생성 또는 실패 처리한다.
- Permission Denied는 Retry하지 않는다.
- Safety Blocked는 사용자 승인 또는 차단 처리한다.
- Timeout과 5xx는 제한적 Retry 가능하다.
- Empty Result는 실패가 아니라 결과 없음일 수 있다.
- Error Response는 구조화해서 LLM에게 전달한다.

---

### [실무]

Tool Error Mapping:

| Error             | Retry  | 처리                    |
| ----------------- | ------ | ----------------------- |
| invalid_arguments | 제한적 | Arguments 재생성        |
| permission_denied | 금지   | 권한 오류               |
| safety_blocked    | 금지   | 승인 필요 또는 차단     |
| timeout           | 가능   | Backoff 후 재시도       |
| rate_limit        | 가능   | Retry-After / Backoff   |
| network_error     | 가능   | 제한적 재시도           |
| external_5xx      | 가능   | 제한적 재시도           |
| empty_result      | 금지   | Missing Information     |
| parsing_error     | 제한적 | Parser 확인 또는 재요청 |

Error Response 예:

```json
{
  "status": "failed",
  "error": {
    "code": "permission_denied",
    "message": "The user does not have permission to read this file.",
    "retryable": false
  },
  "toolExecuted": false
}
```

주의:

- 모든 오류를 Retry하지 않는다.
- 인증과 권한 오류는 Retry로 해결되지 않는다.
- Empty Result를 실패로 처리하지 않는다.
- Tool Error를 LLM이 무시하지 않도록 명확한 status를 포함한다.
- Error Message에 Secret이나 내부 Stack Trace를 노출하지 않는다.

---

### [FAQ]

Q. Tool Error Handling이 뭐야?

A. Tool 검증, 실행, 결과 처리 중 발생하는 오류를 분류하고 안전하게 처리하는 방식이다.

Q. 모든 Tool Error를 Retry하면 돼?

A. 아니다. 권한 오류, 안전 차단, 잘못된 요청은 Retry하면 안 된다.

Q. Empty Result는 실패야?

A. 아니다. Tool은 정상 실행됐지만 결과가 없는 상태일 수 있다.

Q. Tool Error는 LLM에게 어떻게 전달해?

A. status, errorCode, message, retryable 같은 구조화된 형태로 전달한다.

---

## 7.2 Tool Retry

### [개념]

Tool Retry는 일시적 Tool 실패가 발생했을 때 제한된 횟수 안에서 다시 실행하는 전략이다.

Retry는 안정성을 높일 수 있지만 비용, 부하, 중복 실행 위험을 증가시킬 수 있다.

Retry 가능 오류:

- Timeout
- Network Error
- 429 Rate Limit
- 500 / 502 / 503 / 504
- Temporary External API Error

Retry 금지 오류:

- Invalid Permission
- 401 Unauthorized
- 403 Forbidden
- Safety Blocked
- Destructive Operation
- Invalid Arguments
- Empty Result

---

### [핵심]

- Retry는 제한적으로 적용한다.
- Exponential Backoff를 사용한다.
- Jitter를 적용해 동시 재시도 폭증을 줄인다.
- Max Retry를 반드시 설정한다.
- Idempotency 없는 작업은 Retry하지 않는다.
- 429는 Retry-After Header를 확인한다.
- Retry 횟수와 결과를 로그로 남긴다.

---

### [실무]

Retry Flow:

```text
Tool Execution Failed
→ Is Retryable?
→ Check Idempotency
→ Check Retry Count
→ Wait Backoff
→ Retry
→ Success or Final Failure
```

Retry 설정 예:

```json
{
  "maxRetries": 3,
  "backoff": "exponential",
  "jitter": true,
  "retryableErrors": ["timeout", "network_error", "rate_limit", "external_5xx"]
}
```

Idempotency 기준:

| 작업              | Retry 가능성                    |
| ----------------- | ------------------------------- |
| 문서 검색         | 가능                            |
| 파일 읽기         | 가능                            |
| DB Select         | 가능                            |
| 이메일 Draft 생성 | 주의                            |
| 이메일 전송       | 금지 또는 Idempotency 필요      |
| 결제              | 금지 또는 강한 Idempotency 필요 |
| DB Update         | 주의                            |
| 배포              | 금지 또는 명시적 제어 필요      |

주의:

- Retry가 비용을 증가시킬 수 있다.
- 같은 Tool Arguments로 무제한 Retry하지 않는다.
- 쓰기 작업은 중복 실행 문제가 발생할 수 있다.
- Rate Limit 상황에서 즉시 Retry하면 상황이 악화된다.
- Retry 실패 후 Agent Loop가 다시 같은 Tool을 호출하지 않도록 상태를 기록한다.

---

### [FAQ]

Q. Tool Retry가 뭐야?

A. 일시적 Tool 실패가 발생했을 때 제한된 횟수 안에서 다시 실행하는 전략이다.

Q. 어떤 오류는 Retry해도 돼?

A. Timeout, Network Error, Rate Limit, 5xx 같은 일시적 오류는 제한적으로 Retry할 수 있다.

Q. 어떤 오류는 Retry하면 안 돼?

A. 권한 오류, 인증 오류, Safety Blocked, 잘못된 인자, 결과 없음은 Retry하면 안 된다.

Q. Idempotency가 왜 중요해?

A. Retry로 같은 작업이 여러 번 실행될 수 있어 중복 전송, 중복 결제, 중복 수정이 발생할 수 있기 때문이다.

---

# 8. Tool Calling Common Mistakes

## 8.1 Common Mistakes

### [개념]

Tool Calling Common Mistakes는 LLM이 외부 Tool을 사용할 때 발생하는 설계, 검증, 보안, 비용, Workflow 관련 실수이다.

---

### [핵심]

자주 발생하는 실수:

- Tool Arguments를 검증 없이 실행
- Tool Description이 모호함
- 하나의 Tool에 너무 많은 기능을 넣음
- 모든 Agent에게 모든 Tool 제공
- 읽기 Tool과 쓰기 Tool을 분리하지 않음
- 위험 작업에 사용자 승인 없음
- Permission Check 누락
- Safety Check 누락
- Tool Result에 Secret 포함
- Tool 실패와 Empty Result를 혼동
- Tool Error를 모두 Retry
- Idempotency 없는 쓰기 작업 Retry
- Tool Loop 무한 반복
- 같은 Arguments로 같은 Tool 반복 호출
- Tool Result를 전체 원문 그대로 Context에 삽입
- Prompt Injection이 포함된 Tool Result를 그대로 신뢰
- RAG Tool 빈 결과에서 일반 지식으로 추측

---

### [실무]

문제 진단 Flow:

```text
Tool Calling Problem
→ Check Tool Definition
→ Check Tool Selection
→ Check Arguments Schema
→ Check Validation
→ Check Permission
→ Check Safety
→ Check Execution Result
→ Check Tool Message
→ Check Loop Control
```

해결 기준:

| 문제             | 해결                          |
| ---------------- | ----------------------------- |
| 잘못된 Tool 선택 | Tool Description 개선         |
| 잘못된 Arguments | Schema와 Validation 강화      |
| 위험 작업 실행   | Human Confirmation 추가       |
| 권한 오류        | Permission Check 추가         |
| Secret 노출      | Redaction 추가                |
| Tool 결과 과다   | Field Selection 적용          |
| 무한 Loop        | Max Tool Calls 설정           |
| Retry 폭증       | Backoff와 Max Retry 설정      |
| RAG 오답         | Missing Information Rule 적용 |

검수 Checklist:

```text
Tool Definition이 명확한가?
Function Schema가 제한적인가?
Required Field가 과도하지 않은가?
Tool Arguments를 실행 전 검증하는가?
Permission Check가 있는가?
Safety Check가 있는가?
위험 작업에 사용자 승인 절차가 있는가?
Tool Execution Timeout이 있는가?
Tool Result를 검증하는가?
Tool Result에서 Secret을 제거하는가?
Tool Message가 구조화되어 있는가?
Tool Loop에 Max Step이 있는가?
Retry는 오류 유형별로 제한되는가?
Empty Result와 Failed Result를 구분하는가?
```

---

### [FAQ]

Q. Tool Calling에서 가장 흔한 실수는?

A. LLM이 생성한 Tool Arguments를 검증 없이 실행하는 것이다.

Q. 위험 Tool은 어떻게 처리해야 해?

A. 사용자 승인 절차를 두고 승인 전에는 실행하지 않아야 한다.

Q. 모든 Agent에게 모든 Tool을 줘도 돼?

A. 권장하지 않는다. Agent Role에 필요한 Tool만 제공해야 선택 품질과 안전성이 좋아진다.

Q. Tool Result를 그대로 LLM에게 넣어도 돼?

A. 권장하지 않는다. 필요한 필드만 추출하고 Secret을 제거한 뒤 전달해야 한다.

Q. Tool Calling Loop가 위험한 이유는?

A. 같은 Tool을 반복 호출해 비용 폭증, Rate Limit, 무한 Loop가 발생할 수 있기 때문이다.

---

# Retrieval Queries

### [FAQ]

Q. Function Calling이 뭐야?
A. LLM이 외부 함수를 선택하고 실행에 필요한 Arguments를 생성하는 구조다.

Q. Tool Calling이 뭐야?
A. LLM이 외부 Tool을 선택하고 인자를 생성해 Application이 실행하도록 만드는 구조다.

Q. Function Calling과 Tool Calling 차이는?
A. Function Calling은 코드 함수 중심이고 Tool Calling은 검색기, DB, API, 파일 시스템 같은 외부 기능까지 포함한다.

Q. LLM이 Tool을 직접 실행해?
A. 아니다. LLM은 Tool Call 요청을 만들고 실제 실행은 Application 또는 Tool Runtime이 수행한다.

Q. Tool Choice가 뭐야?
A. LLM이 Tool을 사용할지, 어떤 Tool을 사용할지 결정하는 방식이다.

Q. Auto Tool Choice는 뭐야?
A. LLM이 사용자 요청을 보고 Tool 사용 여부와 Tool 종류를 자동으로 선택하는 방식이다.

Q. Forced Tool Choice는 언제 써?
A. 반드시 특정 Tool을 사용해야 하는 RAG 검색, DB 조회, 검증 작업에서 사용할 수 있다.

Q. Tool Definition이 뭐야?
A. LLM에게 Tool의 이름, 목적, 입력 Schema, 사용 조건을 알려주는 명세다.

Q. 좋은 Tool Definition 기준은?
A. 이름이 명확하고 Description이 구체적이며 Arguments Schema가 제한적이고 검증 가능해야 한다.

Q. Function Schema가 뭐야?
A. Tool 또는 Function Arguments의 구조, 타입, 필수 필드, 허용 값을 정의하는 Schema다.

Q. Tool Granularity가 뭐야?
A. Tool을 어느 정도 크기와 책임 단위로 나눌지 정하는 설계 기준이다.

Q. Tool은 작을수록 좋아?
A. 항상 그렇지 않다. 너무 작으면 Tool 수가 많아져 선택 오류가 늘 수 있다.

Q. 조회 Tool과 수정 Tool은 분리해야 해?
A. 권장한다. 읽기 작업과 쓰기 작업은 위험도가 다르기 때문이다.

Q. Argument Validation이 뭐야?
A. LLM이 생성한 Tool Arguments가 Schema, 업무 규칙, 보안 기준을 만족하는지 확인하는 과정이다.

Q. Tool Arguments를 그대로 실행하면 안 되는 이유는?
A. 잘못된 인자가 파일 삭제, 비용 발생, 보안 문제를 만들 수 있기 때문이다.

Q. Permission Check가 뭐야?
A. Tool 실행 전에 사용자가 해당 리소스와 작업에 대한 권한을 갖고 있는지 확인하는 과정이다.

Q. Safety Check가 뭐야?
A. Tool 실행이 위험 작업, Secret 노출, 시스템 손상, 비용 발생을 유발하지 않는지 확인하는 과정이다.

Q. 어떤 Tool 작업은 사용자 승인이 필요해?
A. 파일 삭제, DB 수정, 이메일 전송, 결제, 배포, Production 설정 변경이 승인 대상이다.

Q. Tool Execution은 누가 수행해?
A. LLM이 아니라 Application 또는 Tool Runtime이 수행한다.

Q. Tool Result가 뭐야?
A. Tool 실행 후 생성된 결과 데이터이며 LLM의 최종 답변 근거로 사용된다.

Q. Tool Result도 검증해야 해?
A. 그렇다. 빈 결과, 실패, Secret 포함, 타입 오류, 오래된 정보 여부를 확인해야 한다.

Q. Tool Message가 뭐야?
A. Tool 실행 결과를 LLM에게 전달하는 Message Role이다.

Q. RAG Retrieval Tool이 뭐야?
A. 사용자 Query와 관련된 문서 Chunk를 검색해 LLM에게 근거 Context로 제공하는 Tool이다.

Q. Query Rewrite Tool이 뭐야?
A. 사용자 질문을 RAG 검색에 더 적합한 Query로 변환하는 Tool 또는 단계다.

Q. Agent Tool Use가 뭐야?
A. Agent가 목표 달성을 위해 Tool을 선택하고 실행 결과를 상태에 반영하는 구조다.

Q. Tool Calling Loop Control이 뭐야?
A. Agent가 Tool을 반복 호출할 때 무한 반복과 비용 폭증을 막는 제어 방식이다.

Q. Max Tool Calls가 왜 필요해?
A. 잘못된 Agent가 Tool을 무한 호출하는 것을 막기 위해 필요하다.

Q. Tool Error Handling이 뭐야?
A. Tool 검증, 실행, 결과 처리 중 발생하는 오류를 분류하고 안전하게 처리하는 방식이다.

Q. Tool Retry는 언제 가능해?
A. Timeout, Network Error, Rate Limit, 5xx 같은 일시적 오류는 제한적으로 Retry할 수 있다.

Q. Tool Retry를 하면 안 되는 경우는?
A. 권한 오류, 인증 오류, Safety Blocked, 잘못된 인자, 결과 없음은 Retry하면 안 된다.

Q. Idempotency가 왜 중요해?
A. Retry로 같은 작업이 여러 번 실행될 수 있어 중복 전송, 중복 결제, 중복 수정이 발생할 수 있기 때문이다.

Q. Tool Calling에서 가장 위험한 실수는?
A. LLM이 생성한 Tool Arguments를 검증 없이 실행하는 것이다.

Q. RAG Tool 빈 결과에서는 어떻게 해야 해?
A. 일반 지식으로 추측하지 말고 문서에서 확인되지 않는다고 답하거나 추가 검색을 수행해야 한다.
