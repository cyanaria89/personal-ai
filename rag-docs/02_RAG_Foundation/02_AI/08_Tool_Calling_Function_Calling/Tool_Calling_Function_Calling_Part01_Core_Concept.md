# Tool Calling & Function Calling Part01 - Core Concept

---

# 1. Tool Calling Core Concept

## 1.1 Tool Calling Definition

### [개념]

Tool Calling은 LLM이 외부 기능을 직접 실행하지 않고, 필요한 Tool을 선택하고 실행에 필요한 Tool Arguments를 생성한 뒤, Agent Runtime이 Tool을 실행하도록 연결하는 구조이다.

Tool Calling은 LLM 단독 답변의 한계를 보완한다.

LLM은 다음 작업을 직접 처리하지 않고 Tool을 통해 수행할 수 있다.

- 문서 검색
- 파일 읽기
- 파일 쓰기
- API 호출
- 데이터베이스 조회
- 데이터베이스 변경
- 계산
- 코드 실행
- 테스트 실행
- 로그 조회
- 외부 시스템 상태 확인

Tool Calling의 핵심은 “LLM은 판단하고 Runtime은 실행한다”는 구조이다.

---

### [핵심]

- Tool Calling은 LLM과 외부 기능을 연결하는 Agent 실행 구조이다.
- LLM은 Tool Need 판단, Tool Choice, Tool Arguments 생성을 담당한다.
- 실제 Tool Execution은 Agent Runtime 또는 Backend System이 담당한다.
- Tool Arguments는 실행 명령이 아니라 검증 대상이다.
- Tool Result는 다시 LLM Context 또는 다음 Agent에게 전달될 수 있다.
- LLM은 Tool Result를 바탕으로 Final Answer를 생성한다.
- Tool Calling은 RAG, File, API, Database, Code Execution, Test Tool과 연결된다.
- Tool Calling은 Multi-Agent System의 핵심 실행 방식이다.
- Tool Calling은 단순 함수 호출이 아니라 검증, 실행, 결과 처리, 오류 처리를 포함한다.

---

### [실무]

2026 실무 기준으로 Tool Calling은 단순 함수 호출 문법이 아니라 Agent Workflow의 실행 단위로 설계한다.

실무 Tool Calling 기본 구조:

```text
User Request
→ LLM Determines Tool Need
→ Select Tool
→ Generate Tool Arguments
→ Validate Tool Arguments
→ Check Permission
→ Check Risk Level
→ Execute Tool
→ Return Tool Result
→ Generate Final Answer
```

Tool Calling 설계 시 필수 기준:

- Tool Name
- Tool Description
- Tool Parameters
- Tool Schema
- Required Fields
- Tool Arguments Validation
- Permission Level
- Risk Level
- Side Effect
- Human Confirmation
- Tool Execution Timeout
- Tool Result Structure
- Error Handling
- Audit Log
- Agent Handoff Format

Tool Calling은 “모델이 알아서 실행하는 구조”가 아니다.

LLM이 생성한 Tool Arguments는 신뢰하지 않는다.

실행 전 반드시 검증한다.

---

### [FAQ]

Q. Tool Calling이 뭐야?
A. LLM이 외부 Tool을 선택하고 필요한 인자를 생성해 Runtime이 검색, 파일 처리, API 호출 같은 작업을 실행하도록 연결하는 구조다.

Q. Tool Calling에서 LLM이 직접 실행해?
A. 아니다. LLM은 Tool 선택과 Tool Arguments 생성을 담당하고 실제 실행은 Agent Runtime이나 Backend System이 담당한다.

Q. Tool Calling은 왜 필요해?
A. LLM 단독으로는 최신 정보, 파일 내용, DB 상태, API 결과, 테스트 결과를 알 수 없기 때문이다.

Q. Tool Calling은 RAG랑 관련 있어?
A. 있다. RAG Search Tool은 Tool Calling의 대표적인 사용 사례다.

Q. 모든 질문에 Tool Calling을 써야 해?
A. 아니다. 일반 개념 설명이나 단순 답변은 Tool 없이 직접 답변할 수 있다.

---

# 2. Function Calling Core Concept

## 2.1 Function Calling Definition

### [개념]

Function Calling은 LLM이 특정 Function Schema에 맞춰 Function Arguments를 생성하고, Runtime이 해당 함수를 실행하도록 연결하는 구조이다.

Function Calling은 Tool Calling의 한 형태로 볼 수 있다.

단, Provider마다 Function Calling, Tool Calling, Action, Tool Use 같은 용어와 API 구조가 다를 수 있다.

Function Calling은 주로 “구조화된 arguments 생성”과 “함수 schema 기반 호출”에 초점을 둔다.

---

### [핵심]

- Function Calling은 함수 호출 중심 구조이다.
- Function Calling은 Tool Calling보다 범위가 좁다.
- Function Calling은 Function Schema와 Arguments 생성에 초점이 있다.
- Function Calling은 JSON Schema 기반 arguments 생성에 강점이 있다.
- Function Calling은 API 호출, 검색 함수, DB 조회 함수와 연결 가능하다.
- Provider마다 function, tool, action, tool_use 등 용어가 다를 수 있다.
- Agent 시스템에서는 Tool Calling이라는 용어가 더 넓게 사용된다.
- Function Calling도 실행 전 arguments validation이 필요하다.
- 내부 RAG 문서에서는 Function Calling과 Tool Calling의 용어 기준을 일관되게 유지한다.

---

### [실무]

실무에서는 Function Calling을 단독 기능이 아니라 Tool Calling 구조의 일부로 다룬다.

Function Definition 예시:

```json
{
  "name": "search_rag_documents",
  "description": "Search relevant RAG documents for a user query.",
  "parameters": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "Search query."
      },
      "topK": {
        "type": "integer",
        "description": "Number of document chunks to retrieve.",
        "default": 5
      }
    },
    "required": ["query"]
  }
}
```

LLM이 생성할 수 있는 Function Arguments:

```json
{
  "query": "Tool Calling input validation",
  "topK": 5
}
```

Function Arguments 검증 항목:

- Required Field Check
- Type Check
- Range Check
- Enum Check
- Null Check
- Empty String Check
- Business Validation
- Permission Check
- Risk Check

Function Calling도 Tool Calling과 동일하게 Runtime 검증을 통과해야 한다.

---

### [FAQ]

Q. Function Calling이 뭐야?
A. LLM이 함수 schema에 맞춰 arguments를 만들고 Runtime이 그 함수를 실행하도록 연결하는 구조다.

Q. Function Calling은 함수 실행이야?
A. 정확히는 LLM이 함수 실행에 필요한 구조화된 arguments를 생성하는 방식에 가깝다.

Q. Function Calling은 Tool Calling이랑 같아?
A. 완전히 같지는 않다. Function Calling은 Tool Calling의 한 형태로 볼 수 있다.

Q. Function Calling의 핵심은 뭐야?
A. JSON Schema 기반으로 Function Arguments를 안정적으로 생성하는 것이다.

Q. Function Calling도 검증이 필요해?
A. 필요하다. LLM이 만든 Function Arguments도 실행 전 Runtime 검증을 거쳐야 한다.

---

# 3. Function Calling vs Tool Calling

## 3.1 Concept Difference

### [개념]

Function Calling과 Tool Calling은 모두 LLM이 외부 기능과 연결되는 방식이다.

차이는 범위이다.

Function Calling은 함수 schema와 arguments 생성에 초점을 둔다.

Tool Calling은 Tool 선택, 실행, 결과 처리, 오류 처리, 권한 제어, 위험도 판단, Agent Handoff까지 포함한다.

---

### [핵심]

| 구분         | Function Calling            | Tool Calling                              |
| ------------ | --------------------------- | ----------------------------------------- |
| 의미         | 함수 호출 구조              | 외부 도구 호출 전체 구조                  |
| 중심         | Function Schema / Arguments | Tool 선택 / 실행 / 결과 처리              |
| 범위         | 좁음                        | 넓음                                      |
| 실행 주체    | Runtime                     | Agent Runtime / Backend System            |
| 주요 관심사  | 구조화된 arguments 생성     | 안전 실행 / 검증 / 오류 처리              |
| 예시         | searchDocuments(query)      | RAG Search, File Read, API Call, DB Query |
| 위험도 관리  | 제한적                      | Permission / Risk / Confirmation 포함     |
| Agent 적합성 | 단일 기능 호출              | Multi-Agent Workflow                      |

---

### [실무]

실무 Agent 설계에서는 Tool Calling을 기준 용어로 문서화하는 것이 좋다.

이유:

- Agent는 함수 하나만 호출하지 않는다.
- RAG Search Tool, File Tool, API Tool, Database Tool, Code Execution Tool을 함께 사용한다.
- Tool별 Risk Level이 다르다.
- Tool별 Permission Level이 다르다.
- Tool별 Human Confirmation 기준이 다르다.
- Tool Result를 다음 Agent에게 전달해야 한다.
- Tool 실패 시 Workflow 복구가 필요하다.
- Review Agent가 Tool Result와 Error Handling을 검증해야 한다.

Function Calling은 주로 Tool Schema 작성과 Tool Arguments 생성 단계에서 사용한다.

Tool Calling은 Agent Workflow 전체 설계에서 사용한다.

---

### [FAQ]

Q. Function Calling과 Tool Calling 차이는?
A. Function Calling은 함수 호출 구조이고, Tool Calling은 검색, 파일, API, DB, 코드 실행, 결과 처리, 권한 제어까지 포함하는 더 넓은 구조다.

Q. Agent 문서에서는 어떤 용어를 쓰는 게 좋아?
A. Multi-Agent System에서는 Tool Calling을 기준 용어로 쓰는 것이 좋다.

Q. Function Calling은 Tool Calling에 포함돼?
A. 포함된다고 볼 수 있다. Function Calling은 Tool Calling의 한 구현 방식이다.

Q. Tool Calling이 더 넓은 이유는?
A. Tool 선택, Tool Execution, Tool Result, Error Handling, Permission, Human Confirmation까지 포함하기 때문이다.

Q. Provider마다 용어가 다르면 어떻게 해?
A. 구현 시 Provider 문서를 확인하고, 내부 RAG 문서에서는 Tool Calling / Function Calling 용어를 일관되게 매핑한다.

---

# 4. Core Terms

## 4.1 Terminology Standard

### [개념]

Core Terms는 Tool Calling & Function Calling 문서 전체에서 일관되게 사용할 표준 용어이다.

용어가 흔들리면 RAG 검색 품질과 Agent 판단 품질이 떨어진다.

Part01에서 정의한 용어는 Part02 ~ Part07 전체에서 동일하게 사용한다.

---

### [핵심]

- Tool Calling은 외부 Tool 호출 전체 구조이다.
- Function Calling은 Function Schema 기반 호출 구조이다.
- Tool은 Agent Runtime이 실행 가능한 외부 기능이다.
- Function은 Tool의 구현 형태 중 하나이다.
- Tool Definition은 Tool을 설명하는 구조이다.
- Tool Schema는 Tool Arguments 구조를 제한하는 schema이다.
- Tool Arguments는 LLM이 생성한 Tool 입력값이다.
- Tool Execution은 Runtime이 Tool을 실제 실행하는 단계이다.
- Tool Result는 Tool Execution 결과이다.
- Tool Message는 Tool Result를 LLM Context에 전달하는 메시지이다.
- Agent Runtime은 Tool 검증과 실행을 담당하는 실행 환경이다.
- Final Output은 사용자에게 전달되는 최종 답변 또는 산출물이다.

---

### [실무]

표준 용어표:

| 용어               | 정의                                        | 사용 위치       |
| ------------------ | ------------------------------------------- | --------------- |
| Tool Calling       | LLM과 외부 Tool 연결 구조                   | 전체            |
| Function Calling   | Function Schema 기반 호출 구조              | Part01 / Part02 |
| Tool               | Agent Runtime이 실행하는 외부 기능          | 전체            |
| Function           | Tool의 함수형 구현 단위                     | Part01 / Part02 |
| Tool Definition    | Tool 이름, 설명, 입력, 결과, 위험도 정의    | Part02          |
| Tool Schema        | Tool Arguments 검증 구조                    | Part02 / Part03 |
| Tool Arguments     | LLM이 생성한 Tool 입력값                    | Part03          |
| Tool Execution     | Runtime이 Tool을 실제 실행하는 단계         | Part03          |
| Tool Result        | Tool 실행 결과                              | Part04          |
| Tool Message       | Tool Result를 LLM Context에 전달하는 메시지 | Part03 / Part04 |
| Permission Check   | Agent / User 권한 확인                      | Part03 / Part06 |
| Risk Check         | Tool 위험도 판단                            | Part03 / Part05 |
| Human Confirmation | 위험 작업 전 사용자 승인                    | Part05          |
| Agent Handoff      | Agent 간 결과 전달 구조                     | Part06          |
| Tool Observability | Tool 호출 추적과 관측                       | Part06 / Part07 |

비권장 혼용:

```text
Tool Result / Function Result / Response / Output 무분별 혼용
```

권장 기준:

```text
Tool Result = Tool 실행 결과
Final Output = 사용자에게 전달되는 최종 산출물
```

---

### [FAQ]

Q. Tool과 Function은 같은 말이야?
A. 완전히 같지는 않다. Function은 Tool의 구현 형태 중 하나이고, Tool은 검색, 파일, API, DB 같은 외부 기능 전체를 포함한다.

Q. Tool Arguments와 Tool Result는 달라?
A. 다르다. Tool Arguments는 실행 입력값이고 Tool Result는 실행 결과다.

Q. Tool Message는 뭐야?
A. Tool Result를 LLM Context에 전달하는 메시지다.

Q. Agent Runtime은 뭐야?
A. Tool Arguments 검증, 권한 확인, Tool Execution, Tool Result Mapping을 담당하는 실행 환경이다.

Q. Final Output과 Tool Result는 달라?
A. 다르다. Tool Result는 Tool 실행 결과이고 Final Output은 사용자에게 전달되는 최종 답변 또는 산출물이다.

---

# 5. Tool Calling Basic Flow

## 5.1 Standard Flow

### [개념]

Tool Calling Flow는 사용자 요청을 받아 Tool 필요 여부를 판단하고, 안전하게 실행한 뒤, 결과를 다시 LLM 답변 또는 다음 Agent에게 반영하는 절차이다.

Tool Calling Flow는 단순히 “함수 호출”로 끝나지 않는다.

검증, 권한, 위험도, 결과 구조화, 오류 처리까지 포함한다.

---

### [핵심]

- Tool Need를 먼저 판단한다.
- Tool이 필요 없으면 직접 답변한다.
- Tool이 필요하면 적절한 Tool을 선택한다.
- LLM이 Tool Arguments를 생성한다.
- Runtime이 Tool Arguments를 검증한다.
- Permission Check와 Risk Check를 수행한다.
- 검증 실패 시 Tool을 실행하지 않는다.
- Tool Execution 결과는 Tool Result로 구조화한다.
- Tool Result는 Tool Message로 전달될 수 있다.
- LLM은 Tool Result를 근거로 Final Answer를 생성한다.

---

### [실무]

Standard Tool Calling Flow:

```text
User Request
→ Tool Need 판단
→ Tool Choice
→ Tool Arguments 생성
→ Schema Validation
→ Business Validation
→ Permission Check
→ Risk Check
→ Human Confirmation if needed
→ Tool Execution
→ Tool Result Mapping
→ Tool Message
→ Final Answer
```

Layer 기반 Flow:

```text
Planning Layer
→ Tool Selection Layer
→ Argument Generation Layer
→ Validation Layer
→ Permission Layer
→ Risk Control Layer
→ Execution Layer
→ Result Mapping Layer
→ Final Response Layer
```

각 Layer의 역할:

| Layer                     | 역할                                 |
| ------------------------- | ------------------------------------ |
| Planning Layer            | 요청 분석                            |
| Tool Selection Layer      | 필요한 Tool 선택                     |
| Argument Generation Layer | Tool Arguments 생성                  |
| Validation Layer          | Schema / Business Validation         |
| Permission Layer          | Agent / User 권한 확인               |
| Risk Control Layer        | Risk Level / Human Confirmation 판단 |
| Execution Layer           | 실제 Tool 실행                       |
| Result Mapping Layer      | 결과 구조화                          |
| Final Response Layer      | 사용자 답변 생성                     |

Tool Calling Flow를 분리하면 Review Agent가 각 단계를 검증하기 쉽다.

---

### [FAQ]

Q. Tool Calling 기본 흐름은?
A. 요청 분석 → Tool 선택 → arguments 생성 → 검증 → 권한 확인 → 위험도 판단 → 실행 → 결과 반환 → 최종 답변 순서다.

Q. Tool Arguments 검증은 언제 해?
A. Tool Execution 직전에 반드시 수행한다.

Q. Tool Result 검증도 필요해?
A. 필요하다. 외부 API나 파일 결과도 잘못됐거나 불완전할 수 있다.

Q. Tool이 필요 없는 요청은 어떻게 해?
A. Tool을 호출하지 않고 LLM이 직접 답변한다.

Q. Tool 실행 실패 시 어떻게 해?
A. 실패 결과를 구조화하고, 원인과 재시도 가능 여부를 판단한다.

---

# 6. Tool Need Decision

## 6.1 Tool Need Criteria

### [개념]

Tool Need Decision은 사용자 요청에 Tool Calling이 필요한지 판단하는 단계이다.

모든 요청에 Tool이 필요한 것은 아니다.

Tool이 필요 없는 요청은 직접 답변하고, 외부 정보나 실제 상태 확인이 필요한 요청은 Tool을 사용한다.

---

### [핵심]

- 문서 검색이 필요하면 RAG Search Tool을 사용한다.
- 파일 내용 확인이 필요하면 File Read Tool을 사용한다.
- 현재 정보 확인이 필요하면 Web / API Tool을 사용한다.
- 계산이 필요하면 Calculator Tool을 사용한다.
- 코드 실행이 필요하면 Code Execution Tool을 사용한다.
- DB 상태 확인이 필요하면 Database Read Tool을 사용한다.
- 데이터 변경이 필요하면 Database Write Tool과 Human Confirmation을 사용한다.
- 위험 작업이면 Tool 실행 전 Human Confirmation이 필요하다.
- 일반 개념 설명은 Tool 없이 직접 답변 가능하다.

---

### [실무]

Tool Need 판단 기준:

```text
질문이 문서 검색 필요 → RAG Search Tool
파일 내용 확인 필요 → File Read Tool
현재 정보 필요 → Web/API Tool
정확한 계산 필요 → Calculator Tool
코드 실행 필요 → Code Execution Tool
DB 조회 필요 → Database Read Tool
DB 변경 필요 → Database Write Tool + Confirmation
파일 수정 필요 → File Write Tool + Confirmation if overwrite
이메일 발송 필요 → Email Send Tool + Confirmation
배포 필요 → Deployment Tool + Confirmation
일반 설명 요청 → No Tool
```

No Tool이 적절한 경우:

- 일반 개념 설명
- 용어 차이 설명
- 안정적인 원리 설명
- 사용자가 제공한 텍스트 요약
- 이미 Context에 있는 내용 정리

Tool이 필요한 경우:

- 최신 정보
- 파일 실제 내용
- DB 실제 상태
- API 실제 결과
- 코드 실행 결과
- 테스트 결과
- 로그 상태
- 외부 시스템 변경 작업

---

### [FAQ]

Q. 모든 요청에 Tool을 써야 해?
A. 아니다. Tool이 필요 없는 일반 설명은 직접 답변해도 된다.

Q. Tool이 필요한 요청은 어떤 요청이야?
A. 문서 검색, 파일 확인, API 호출, DB 조회, 계산, 코드 실행, 테스트 실행, 최신 정보 확인이 필요한 요청이다.

Q. RAG 문서 기반 답변은 Tool이 필요해?
A. 실제 RAG 문서 검색이 필요한 경우 RAG Search Tool을 사용한다.

Q. 파일 수정 요청은 Tool이 필요해?
A. 필요하다. File Write Tool이 필요하며 덮어쓰기나 삭제는 Human Confirmation이 필요하다.

Q. 배포 요청은 Tool 없이 답해도 돼?
A. 실제 배포 상태 확인이나 실행이 필요하면 DevOps Tool과 Human Confirmation이 필요하다.

---

# 7. Tool Calling Use Cases

## 7.1 Common Tool Types

### [개념]

Tool Calling은 Agent가 외부 정보와 시스템 기능을 사용할 때 적용한다.

Tool Type은 목적과 위험도에 따라 분류한다.

대표 Tool Type은 RAG Search Tool, File Tool, API Tool, Database Tool, Code Execution Tool, Test Tool, Observability Tool이다.

---

### [핵심]

| Tool Type           | 목적               | 기본 위험도   |
| ------------------- | ------------------ | ------------- |
| RAG Search Tool     | 문서 검색          | Low           |
| File Read Tool      | 파일 읽기          | Low           |
| File Write Tool     | 파일 수정          | Medium ~ High |
| API Tool            | 외부 API 호출      | Medium        |
| Database Read Tool  | DB 조회            | Medium        |
| Database Write Tool | DB 변경            | High          |
| Calculator Tool     | 계산               | Low           |
| Code Execution Tool | 코드 실행          | High          |
| Test Execution Tool | 테스트 실행        | Medium        |
| Observability Tool  | 로그 / metric 조회 | Low ~ Medium  |
| Email Send Tool     | 이메일 발송        | High          |
| Deployment Tool     | 배포 실행          | High          |

---

### [실무]

Agent별 Tool 사용 예시:

| Agent          | 주요 Tool                                                   |
| -------------- | ----------------------------------------------------------- |
| PM Agent       | RAG Search, Task Routing                                    |
| Backend Agent  | Backend RAG Search, File Read, Code Search, Test Tool       |
| Frontend Agent | Frontend RAG Search, File Read, Component Search, Test Tool |
| Review Agent   | RAG Search, Static Analysis, Test Result Read               |
| DevOps Agent   | Log Search, Infra Status, Deployment Read                   |
| AI/ML Agent    | RAG Search, Vector Search, Evaluation Tool                  |

PM Agent는 직접 위험 Tool을 실행하지 않고 라우팅 중심으로 동작하는 것이 안전하다.

Domain Agent는 자신의 역할에 필요한 Tool만 사용한다.

Review Agent는 결과 검증 중심으로 Tool을 사용한다.

---

### [FAQ]

Q. RAG Search Tool은 언제 써?
A. 답변 전 관련 문서 검색이 필요할 때 사용한다.

Q. File Tool은 언제 써?
A. 파일 내용을 읽거나 문서를 수정해야 할 때 사용한다.

Q. Database Tool은 위험해?
A. 조회는 중간 위험, 변경은 높은 위험으로 본다.

Q. Code Execution Tool은 왜 위험해?
A. 임의 코드가 파일, 네트워크, 리소스, Secret에 접근할 수 있기 때문이다.

Q. Agent마다 Tool 권한을 나눠야 해?
A. 그렇다. 최소 권한 원칙에 따라 Agent별 Tool 접근 범위를 제한해야 한다.

---

# 8. Safe Tool Calling Principle

## 8.1 Safety Principle

### [개념]

Safe Tool Calling은 Tool Calling 과정에서 입력값, 권한, 위험도, 실행 결과, 오류 처리를 통제하는 원칙이다.

Tool Calling은 외부 시스템에 실제 영향을 줄 수 있으므로 안전 기준이 필수이다.

LLM이 생성한 Tool Name, Tool Arguments, Tool Plan은 신뢰하지 않는다.

---

### [핵심]

- LLM Output은 검증 대상이다.
- Tool Arguments는 실행 전 검증한다.
- 위험 Tool은 Human Confirmation이 필요하다.
- Side Effect가 있는 작업은 Audit Log를 남긴다.
- File Path, URL, SQL, Shell Command는 특히 주의한다.
- API Key, Secret, Token은 로그에 남기지 않는다.
- Tool 실패를 성공처럼 처리하지 않는다.
- Non-Idempotent 작업은 중복 실행을 방지한다.
- Tool Result는 success / error / blocked / partial을 구분한다.
- Permission Check는 Runtime에서 강제한다.

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

High Risk Tool 예시:

- File Delete Tool
- File Overwrite Tool
- Database Write Tool
- Shell Command Tool
- Email Send Tool
- Payment Tool
- Deployment Tool
- Account Modification Tool

High Risk 작업 전 확인 항목:

- 실행 대상
- 변경 내용
- 영향 범위
- 되돌리기 가능 여부
- Preview 결과
- 사용자 승인 여부
- Audit Log 필요 여부

---

### [FAQ]

Q. Tool Calling에서 가장 중요한 안전 원칙은?
A. LLM이 생성한 입력을 신뢰하지 않고 실행 전 검증하는 것이다.

Q. 위험 Tool은 자동 실행해도 돼?
A. 안 된다. 삭제, 결제, 발송, 배포, DB 변경 같은 작업은 Human Confirmation이 필요하다.

Q. Tool 실패를 숨겨도 돼?
A. 안 된다. 실패 상태와 원인을 구조화해서 반환해야 한다.

Q. Non-Idempotent 작업은 왜 조심해야 해?
A. 재시도나 중복 실행으로 이메일 중복 발송, 결제 중복 요청, 데이터 중복 변경이 발생할 수 있다.

Q. Tool Calling 로그에는 무엇을 남겨야 해?
A. Tool Name, Agent ID, 상태, 실행 시간, 오류 유형, Trace ID를 남기고 Secret은 마스킹해야 한다.

---

# 9. Multi-Agent Integration

## 9.1 Multi-Agent Tool Calling

### [개념]

Multi-Agent Integration은 Tool Calling을 PM Agent, Backend Agent, Frontend Agent, Review Agent, DevOps Agent, AI/ML Agent가 역할별로 사용하는 구조이다.

Multi-Agent System에서는 Agent별 Tool 권한과 Handoff Format이 중요하다.

Tool Result는 다음 Agent가 검증할 수 있도록 source, status, metadata를 유지해야 한다.

---

### [핵심]

- PM Agent는 Request Analysis와 Task Routing 중심이다.
- Backend Agent는 Backend 관련 Tool을 사용한다.
- Frontend Agent는 Frontend 관련 Tool을 사용한다.
- Review Agent는 검증 Tool 중심으로 사용한다.
- DevOps Agent는 Infra / Log / Deployment 관련 Tool을 제한적으로 사용한다.
- AI/ML Agent는 RAG / Vector Search / Evaluation Tool을 사용한다.
- Agent별 allowedTools와 deniedTools를 분리한다.
- Tool Result는 Agent Handoff에 포함한다.
- Review Agent는 Tool Result와 Error Handling을 검증한다.

---

### [실무]

Multi-Agent Tool Calling Flow:

```text
User Request
→ PM Agent
→ Domain Agent
→ Tool Calling
→ Tool Result
→ Agent Handoff
→ Review Agent
→ Fix if Needed
→ Final Output
```

Agent별 Tool 권한 예시:

| Agent          | 권장 Tool                                     | 제한 Tool                              |
| -------------- | --------------------------------------------- | -------------------------------------- |
| PM Agent       | RAG Search, Task Routing                      | File Write, DB Write, Deploy           |
| Backend Agent  | Backend RAG, File Read, Test Tool             | Production Deploy                      |
| Frontend Agent | Frontend RAG, File Read, Component Search     | DB Write                               |
| Review Agent   | RAG Search, Static Analysis, Test Result Read | File Write, Email Send                 |
| DevOps Agent   | Log Search, Infra Status, Deploy Read         | Production Deploy without Confirmation |
| AI/ML Agent    | Vector Search, Retrieval Evaluation           | File Delete, DB Write                  |

Agent Handoff 기본 구조:

```json
{
  "fromAgent": "backend-agent",
  "toAgent": "review-agent",
  "task": "Validate Tool Arguments section",
  "status": "completed",
  "toolResults": [
    {
      "toolName": "search_rag_documents",
      "status": "success",
      "source": "Tool_Calling_Function_Calling_Domain_Rules.md"
    }
  ],
  "knownIssues": [],
  "requiresReview": true
}
```

---

### [FAQ]

Q. Multi-Agent에서 Tool Calling은 어떻게 쓰여?
A. 각 Agent가 역할에 맞는 Tool을 사용하고 Tool Result를 Handoff하여 Review Agent가 검증하는 방식으로 사용된다.

Q. PM Agent는 Tool을 직접 실행해도 돼?
A. 검색과 라우팅 중심은 가능하지만 위험 Tool 직접 실행은 제한하는 것이 좋다.

Q. Review Agent는 무엇을 검증해?
A. Tool Result status, source, metadata, error handling, safety policy, 테스트 결과를 검증한다.

Q. Agent Handoff에는 무엇이 필요해?
A. fromAgent, toAgent, task, status, toolResults, knownIssues, requiresReview가 필요하다.

Q. Agent별 Tool 권한은 왜 분리해?
A. 최소 권한 원칙을 적용해 위험 Tool 오작동 피해를 줄이기 위해서다.

---

# 10. Series Linkage

## 10.1 Part Linkage

### [개념]

Series Linkage는 Tool Calling & Function Calling 문서 세트가 서로 어떤 기준으로 연결되는지 정의하는 부분이다.

Part01은 전체 개념과 용어를 정의하고, Part02 ~ Part07은 Tool Calling의 세부 실행 기준을 나누어 설명한다.

이 섹션은 별도의 Document Position 형식이 아니라, Part01 내부에서 전체 문서 흐름을 정리하는 연계 기준이다.

---

### [핵심]

- Part01은 Core Concept와 용어 기준이다.
- Part02는 Tool Definition과 Tool Schema 기준이다.
- Part03은 Tool Arguments Validation과 Tool Execution 기준이다.
- Part04는 Tool Result와 Error Handling 기준이다.
- Part05는 Safe Execution과 Human Confirmation 기준이다.
- Part06은 Agent Tool Routing과 Multi-Agent Tool Use 기준이다.
- Part07은 Tool Types, Testing, Troubleshooting, Final Checklist 기준이다.
- Part01의 용어는 전체 Part에서 동일하게 사용한다.
- Part02 ~ Part07은 Part01의 Tool Calling Flow를 세분화한다.

---

### [실무]

전체 Part 구성:

| Part   | 파일명                                                                     | 핵심 역할                              |
| ------ | -------------------------------------------------------------------------- | -------------------------------------- |
| Part01 | Tool_Calling_Function_Calling_Part01_Core_Concept.md                       | Core Concept / 용어 / 기본 Flow        |
| Part02 | Tool_Calling_Function_Calling_Part02_Tool_Definition_Schema.md             | Tool Definition / Schema               |
| Part03 | Tool_Calling_Function_Calling_Part03_Arguments_Validation_Execution.md     | Arguments Validation / Execution       |
| Part04 | Tool_Calling_Function_Calling_Part04_Result_Error_Handling.md              | Result / Error Handling                |
| Part05 | Tool_Calling_Function_Calling_Part05_Safe_Execution_Human_Confirmation.md  | Safe Execution / Confirmation          |
| Part06 | Tool_Calling_Function_Calling_Part06_Agent_Tool_Routing_Multi_Agent.md     | Agent Routing / Multi-Agent            |
| Part07 | Tool_Calling_Function_Calling_Part07_Tool_Types_Testing_Troubleshooting.md | Tool Types / Testing / Troubleshooting |

전체 연계 Flow:

```text
User Request
→ Agent 판단
→ Tool Need 판단
→ Tool Choice
→ Tool Arguments 생성
→ Tool Arguments Validation
→ Permission Check
→ Risk Check
→ Tool Execution
→ Tool Result Mapping
→ Error Handling
→ Agent Handoff
→ Review
→ Final Output
```

---

### [FAQ]

Q. Tool Calling 문서 세트는 몇 개 Part야?
A. 총 7개 Part로 구성한다.

Q. Part01은 어떤 역할이야?
A. 전체 개념, 용어, 기본 Flow, Part 간 연계 기준을 정의한다.

Q. Part02는 어떤 역할이야?
A. Tool Definition, Tool Schema, Parameters, Required Fields, Return Type 기준을 정의한다.

Q. Part03은 어떤 역할이야?
A. LLM이 생성한 Tool Arguments를 검증하고 Runtime이 Tool을 실행하는 기준을 정의한다.

Q. Part04는 어떤 역할이야?
A. Tool Result, Error Result, Blocked Result, Partial Result, Error Handling 기준을 정의한다.

Q. Part05는 어떤 역할이야?
A. Safe Execution, Risk Level, Side Effect, Human Confirmation, Approval Scope, Audit Log 기준을 정의한다.

Q. Part06은 어떤 역할이야?
A. Agent Tool Routing, Agent Permission, Multi-Agent Tool Use, Agent Handoff, Shared State 기준을 정의한다.

Q. Part07은 어떤 역할이야?
A. Tool Type, Tool Testing, Troubleshooting, Common Mistakes, Final Integration Checklist 기준을 정의한다.

---

# 11. RAG Document Writing Rules

## 11.1 Retrieval Optimized Writing

### [개념]

Tool Calling RAG 문서는 사람이 읽기 좋은 설명서보다 Agent가 검색하고 적용하기 좋은 구조로 작성한다.

각 Chunk는 독립 검색되어도 의미가 유지되어야 한다.

Tool Calling 문서는 개념, 구조, Flow, 안전 기준, 오류 처리, Agent 권한 분리를 반복적으로 검색 가능하게 작성한다.

---

### [핵심]

- 제목에 핵심 키워드를 포함한다.
- Tool Calling, Function Calling, Tool Schema, Tool Arguments 키워드를 반복한다.
- Chunk마다 하나의 개념만 설명한다.
- Flow는 text arrow 형식으로 작성한다.
- FAQ는 실제 사용자 질문 형태로 작성한다.
- Retrieval Queries는 문서 마지막에 반드시 포함한다.
- Tool Safety, Human Confirmation, Error Handling 키워드를 포함한다.
- Function Calling과 Tool Calling 차이를 명확히 반복한다.
- Provider별 용어 차이 주의 문장을 포함한다.
- 전체 Part 간 용어를 통일한다.

---

### [실무]

좋은 Chunk 예시:

```md
## Tool Arguments Validation

### [개념]

Tool Arguments Validation은 LLM이 생성한 arguments를 실행 전에 검증하는 과정이다.
```

나쁜 Chunk 예시:

```md
## 기타 설명

Tool도 있고 함수도 있고 API도 있는데 상황에 따라 잘 쓰면 된다.
```

Tool Calling RAG 문서는 다음 검색 질문에 바로 매칭되어야 한다.

- Tool Calling이 뭐야?
- Function Calling과 Tool Calling 차이는?
- Tool Schema는 어떻게 만들어?
- Tool Arguments는 왜 검증해야 해?
- Tool Result는 어떤 구조가 좋아?
- 위험 Tool은 어떻게 처리해?
- Human Confirmation은 언제 필요해?
- Agent별 Tool 권한은 어떻게 나눠?
- Tool 실패는 어떻게 처리해?
- Multi-Agent에서 Tool Result는 어떻게 전달해?

---

### [FAQ]

Q. Tool Calling 문서는 사람용으로 길게 써야 해?
A. 아니다. RAG Retrieval과 Agent Code Generation에 맞게 짧고 구조적으로 작성한다.

Q. FAQ를 왜 많이 넣어?
A. 실제 사용자 질문과 검색 query matching을 강화하기 위해서다.

Q. Tool Calling 문서에서 가장 중요한 키워드는?
A. Tool Calling, Function Calling, Tool Schema, Tool Arguments, Tool Result, Safe Execution이다.

Q. Flow는 왜 필요해?
A. Agent가 실행 순서와 책임 분리를 이해하기 쉽게 하기 위해 필요하다.

Q. Retrieval Queries는 왜 필요해?
A. 사용자의 질문 표현과 문서 내용을 직접 연결해 검색 적중률을 높이기 위해 필요하다.

---

# Retrieval Queries

### [FAQ]

Q. Tool Calling이 뭐야?
A. LLM이 외부 Tool을 선택하고 필요한 Tool Arguments를 생성해 Runtime이 검색, 파일 처리, API 호출 같은 작업을 실행하도록 연결하는 구조다.

Q. Function Calling이 뭐야?
A. LLM이 Function Schema에 맞는 Function Arguments를 생성하고 Runtime이 해당 함수를 실행하도록 연결하는 구조다.

Q. Function Calling과 Tool Calling 차이는?
A. Function Calling은 함수 호출 중심이고, Tool Calling은 Tool 선택, 실행, 결과 처리, 오류 처리, 권한 제어까지 포함하는 더 넓은 구조다.

Q. Function Calling은 Tool Calling에 포함돼?
A. 포함된다고 볼 수 있다. Function Calling은 Tool Calling의 한 구현 방식이다.

Q. Provider마다 Function Calling과 Tool Calling 용어가 다르면 어떻게 해?
A. Provider 문서를 확인하고 내부 RAG 문서에서는 Tool Calling, Function Calling, Tool Arguments, Tool Result 용어를 일관되게 매핑한다.

Q. Tool Calling에서 LLM은 무엇을 담당해?
A. Tool 필요 여부 판단, Tool Choice, Tool Arguments 생성을 담당한다.

Q. Tool Calling에서 Runtime은 무엇을 담당해?
A. Tool Arguments 검증, 권한 확인, 위험도 판단, Tool Execution, Tool Result Mapping, Error Handling을 담당한다.

Q. Tool Arguments는 왜 검증해야 해?
A. LLM이 생성한 인자는 틀리거나 위험할 수 있으므로 실행 전 Schema, Business Rule, Permission, Risk 검증이 필요하다.

Q. Tool Result는 왜 구조화해야 해?
A. LLM과 다음 Agent가 success, error, blocked, partial, data, source, metadata를 명확히 이해해야 하기 때문이다.

Q. Tool Message가 뭐야?
A. Tool Result를 LLM Context에 전달하는 메시지다.

Q. Tool Calling 기본 Flow는?
A. User Request → Tool Need 판단 → Tool Choice → Arguments 생성 → 검증 → 권한 확인 → 위험도 판단 → 실행 → Result 반환 → Final Answer 순서다.

Q. Tool Calling은 언제 사용해?
A. 문서 검색, 파일 읽기, API 호출, DB 조회, 계산, 코드 실행, 테스트 실행처럼 외부 기능이나 실제 상태 확인이 필요할 때 사용한다.

Q. Tool Calling이 필요 없는 경우는?
A. 일반 개념 설명, 안정적인 원리 설명, 사용자가 제공한 텍스트 정리에는 Tool 없이 직접 답변할 수 있다.

Q. RAG Search Tool은 Tool Calling이야?
A. 맞다. RAG Search Tool은 문서 검색을 수행하는 대표적인 Tool Calling 사례다.

Q. File Tool은 안전해?
A. 파일 읽기는 비교적 안전하지만, 파일 쓰기, 덮어쓰기, 삭제는 위험하므로 검증과 승인 절차가 필요하다.

Q. Database Tool은 어떻게 나눠야 해?
A. Database Read Tool과 Database Write Tool을 분리하고, Write 작업은 권한 확인과 Human Confirmation을 적용한다.

Q. Code Execution Tool은 왜 고위험 Tool이야?
A. 임의 코드가 파일, 네트워크, 리소스, Secret에 접근할 수 있어 Sandbox, Timeout, Resource Limit이 필요하기 때문이다.

Q. Human Confirmation은 언제 필요해?
A. 파일 삭제, DB 변경, 이메일 발송, 결제, 배포처럼 되돌리기 어렵거나 외부 시스템에 영향을 주는 작업 전에 필요하다.

Q. Tool Calling에서 Idempotency는 왜 중요해?
A. Retry나 중복 실행 시 안전한 작업인지 판단하기 위해 필요하다.

Q. Tool 실패는 어떻게 처리해야 해?
A. 실패 원인, error type, retryable 여부를 구조화하고 성공처럼 답변하지 않아야 한다.

Q. Agent별 Tool 권한은 왜 나눠야 해?
A. 최소 권한 원칙을 적용해 위험 작업을 제한하고 Agent 오작동의 피해 범위를 줄이기 위해서다.

Q. PM Agent는 어떤 Tool을 사용해야 해?
A. PM Agent는 RAG Search와 Task Routing 중심으로 사용하고 위험 Tool 직접 실행은 제한하는 것이 좋다.

Q. Backend Agent는 어떤 Tool을 사용해야 해?
A. Backend RAG Search, File Read, Code Search, Test Tool, 제한적 File Write Tool을 사용할 수 있다.

Q. Frontend Agent는 어떤 Tool을 사용해야 해?
A. Frontend RAG Search, File Read, Component Search, Router Search, Test Tool을 사용할 수 있다.

Q. Review Agent는 Tool Calling에서 어떤 역할을 해?
A. Tool Result, 코드 변경, 테스트 결과, 오류 처리, 안전 정책 준수 여부를 검증하는 역할을 한다.

Q. DevOps Agent는 어떤 Tool을 사용해야 해?
A. Log Search, Infra Status, Deployment Read, 제한적 Deploy Tool을 사용할 수 있으며 Production Deploy는 Confirmation이 필요하다.

Q. AI/ML Agent는 어떤 Tool을 사용해야 해?
A. RAG Search, Vector Search, Retrieval Evaluation, Query Rewrite Tool을 사용할 수 있다.

Q. Agent Handoff에는 무엇이 필요해?
A. fromAgent, toAgent, task, status, toolResults, source, knownIssues, requiresReview가 필요하다.

Q. Tool Calling 문서 세트는 어떻게 구성돼?
A. Part01 Core Concept, Part02 Tool Definition, Part03 Arguments Validation, Part04 Result Handling, Part05 Safe Execution, Part06 Agent Routing, Part07 Tool Types와 Testing으로 구성된다.

Q. Tool Calling 문서의 최종 목표는 뭐야?
A. Agent가 외부 도구를 정확하고 안전하게 호출하고, 실패와 위험 작업을 통제하며 Multi-Agent Workflow에서 검증 가능한 결과를 만들게 하는 것이다.
