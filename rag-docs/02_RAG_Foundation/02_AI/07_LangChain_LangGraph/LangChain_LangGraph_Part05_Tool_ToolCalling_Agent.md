# LangChain & LangGraph Part05 Tool ToolCalling Agent

---

# 1. Tool Core

## 1.1 Tool 기본 개념

### [개념]

Tool은 Agent가 외부 기능을 사용할 수 있게 하는 실행 단위다.

LLM은 자체적으로 파일을 읽거나, API를 호출하거나, 테스트를 실행하거나, DB를 변경하지 못한다.

Agent는 Tool을 통해 검색, 파일 처리, API 호출, 코드 실행, 테스트 실행 같은 작업을 수행할 수 있다.

기본 Flow:

```text
User Task
→ Agent
→ Tool Selection
→ Tool Arguments
→ Tool Execution
→ Tool Result
→ Agent Response
```

Tool은 Agent의 행동 범위를 확장하지만, 동시에 위험도 증가시킨다.

---

### [핵심]

- Tool은 Agent가 외부 기능을 실행하는 인터페이스다.
- Tool은 이름, 설명, Args Schema, 실행 함수, 결과 형식이 필요하다.
- Tool Description은 Agent가 언제 Tool을 사용할지 판단하는 기준이다.
- Tool Arguments는 실행 전 검증해야 한다.
- Tool Result는 성공과 실패를 구분해 구조화해야 한다.
- 위험 Tool은 Human Approval이 필요하다.
- Tool이 많을수록 Agent의 선택 오류 가능성이 증가한다.

---

### [실무]

Tool 구성 요소:

| 구성 요소          | 설명                               |
| ------------------ | ---------------------------------- |
| Tool Name          | Tool 식별 이름                     |
| Description        | Tool 사용 목적과 조건              |
| Args Schema        | 입력 인자 구조                     |
| Permission         | 실행 권한                          |
| Execution Function | 실제 실행 로직                     |
| Tool Result        | 성공 결과                          |
| Tool Error         | 실패 결과                          |
| Side Effect        | 파일 변경, DB 변경, 비용 발생 여부 |

Tool 예시:

```text
search_rag_documents(query, top_k, metadata_filter)
read_file(path)
write_file(path, content)
run_test(command)
call_api(endpoint, payload)
create_git_commit(message)
deploy_service(environment)
```

Tool 위험도 분류:

| 위험도   | 예시                        | 처리                       |
| -------- | --------------------------- | -------------------------- |
| Low      | 문서 검색, 파일 읽기        | 자동 실행 가능             |
| Medium   | 테스트 실행, 코드 포맷팅    | 제한된 자동 실행           |
| High     | 파일 쓰기, DB 변경          | 승인 필요                  |
| Critical | 삭제, 배포, 결제, 외부 발송 | 명시적 Human Approval 필요 |

---

### [FAQ]

Q. Tool이 뭐야?

A.
Agent가 검색, 파일 처리, API 호출, 테스트 실행 같은 외부 기능을 사용할 수 있게 하는 실행 인터페이스다.

Q. Agent에게 Tool이 왜 필요해?

A.
LLM 자체는 외부 시스템을 직접 조작하지 못하므로 Tool을 통해 실제 작업을 수행해야 하기 때문이다.

Q. Tool Description은 왜 중요해?

A.
Agent가 어떤 상황에서 어떤 Tool을 사용할지 판단하는 기준이 되기 때문이다.

Q. Tool Arguments는 왜 검증해야 해?

A.
LLM이 생성한 인자는 틀리거나 위험할 수 있으므로 실행 전 검증이 필요하다.

Q. 위험 Tool은 어떻게 처리해?

A.
파일 삭제, DB 변경, 배포, 비용 발생 같은 Tool은 Human Approval 이후 실행해야 한다.

---

# 2. Tool Schema

## 2.1 Args Schema 설계

### [개념]

Args Schema는 Tool이 받을 입력 인자의 구조와 타입을 정의한다.

Tool Arguments는 LLM이 생성할 수 있으므로 명확한 Schema와 검증 규칙이 필요하다.

기본 구조:

```text
Tool Call
→ Args Schema Validation
→ Execute Tool
→ Tool Result
```

Args Schema가 모호하면 Agent가 잘못된 인자를 생성하거나 Tool 실행이 실패할 수 있다.

---

### [핵심]

- Args Schema는 Tool 입력 구조를 정의한다.
- 필수 인자와 선택 인자를 구분한다.
- 타입, 범위, enum 값을 명확히 제한한다.
- 위험 인자는 추가 검증이 필요하다.
- 경로, 명령어, URL, SQL은 특히 검증해야 한다.
- Schema는 단순할수록 안정적이다.
- Tool 실행 전 Validation을 반드시 수행한다.

---

### [실무]

RAG 검색 Tool Schema 예시:

```json
{
  "tool_name": "search_rag_documents",
  "args": {
    "query": "LangGraph State Node Edge Conditional Edge",
    "top_k": 5,
    "metadata_filter": {
      "domain": "AI",
      "document": "LangChain_LangGraph"
    }
  }
}
```

파일 읽기 Tool Schema 예시:

```json
{
  "tool_name": "read_file",
  "args": {
    "path": "RAG Foundation/AI/LangChain LangGraph/Part05.md"
  }
}
```

테스트 실행 Tool Schema 예시:

```json
{
  "tool_name": "run_test",
  "args": {
    "command": "./gradlew test",
    "working_directory": "Backend",
    "timeout_seconds": 120
  }
}
```

Schema 설계 기준:

| 항목            | 기준                               |
| --------------- | ---------------------------------- |
| query           | 빈 문자열 금지                     |
| top_k           | 정수, 상한 제한                    |
| metadata_filter | 허용 필드만 사용                   |
| path            | 허용된 workspace 내부로 제한       |
| command         | allowlist 기반 제한                |
| timeout         | 최대값 제한                        |
| environment     | dev, test, staging, prod enum 제한 |

---

### [FAQ]

Q. Args Schema가 뭐야?

A.
Tool이 받을 입력 인자의 이름, 타입, 필수 여부, 제한 조건을 정의하는 구조다.

Q. Args Schema는 왜 필요해?

A.
LLM이 생성한 Tool Arguments를 검증하고 잘못된 실행을 막기 위해 필요하다.

Q. Tool Schema는 복잡해도 돼?

A.
너무 복잡하면 Agent가 인자를 잘못 생성할 가능성이 증가하므로 단순하게 설계하는 것이 좋다.

Q. 어떤 인자를 특히 검증해야 해?

A.
파일 경로, 명령어, URL, SQL, API Payload, 배포 환경 같은 위험 인자를 검증해야 한다.

Q. top_k 같은 값도 제한해야 해?

A.
해야 한다. 너무 큰 top_k는 비용과 Context 노이즈를 증가시킬 수 있다.

---

# 3. Tool Result

## 3.1 Tool Result 구조화

### [개념]

Tool Result는 Tool 실행 결과를 Agent가 이해할 수 있는 구조로 반환하는 데이터다.

Tool Result는 성공과 실패를 명확히 구분해야 한다.

기본 Flow:

```text
Tool Execution
→ Success Result or Error Result
→ Agent Observation
→ Next Decision
```

Tool Result가 구조화되지 않으면 Agent가 실패 결과를 성공으로 오해할 수 있다.

---

### [핵심]

- Tool Result는 status를 포함해야 한다.
- 성공 결과와 실패 결과를 구분한다.
- 실패 원인과 재시도 가능 여부를 포함한다.
- Tool 실행 로그는 필요한 최소 정보만 포함한다.
- 민감정보는 Tool Result에 포함하지 않는다.
- Agent는 Tool Result를 Observation으로 사용한다.
- Tool Result는 State에 저장하거나 요약해 전달할 수 있다.

---

### [실무]

성공 Result 예시:

```json
{
  "status": "success",
  "tool_name": "search_rag_documents",
  "data": {
    "documents": [
      {
        "source": "07_LangChain_LangGraph_Part04_RAG_Chain_Retrieval_Optimization.md",
        "section": "5. Query Rewrite",
        "content": "Query Rewrite는 사용자 질문을 Retriever가 더 잘 검색할 수 있는 형태로 변환하는 단계다.",
        "score": 0.84
      }
    ]
  }
}
```

실패 Result 예시:

```json
{
  "status": "error",
  "tool_name": "run_test",
  "error_type": "timeout",
  "message": "Test command exceeded timeout_seconds.",
  "retryable": true
}
```

Tool Error 유형:

| error_type         | 설명                    |
| ------------------ | ----------------------- |
| invalid_arguments  | Args Schema 불일치      |
| permission_denied  | 권한 부족               |
| not_found          | 파일, 문서, 리소스 없음 |
| timeout            | 실행 시간 초과          |
| external_api_error | 외부 API 오류           |
| unsafe_action      | 승인 없는 위험 작업     |
| execution_failed   | Tool 내부 실행 실패     |

Tool Result 저장 기준:

| 결과           | State 저장 방식          |
| -------------- | ------------------------ |
| 짧은 검색 결과 | State에 직접 저장        |
| 긴 문서 내용   | 요약 또는 참조 저장      |
| 테스트 결과    | 실패 요약 저장           |
| 민감 로그      | 저장 금지                |
| 대용량 출력    | 파일 참조 또는 요약 저장 |

---

### [FAQ]

Q. Tool Result가 뭐야?

A.
Tool 실행 결과를 Agent가 이해할 수 있도록 반환하는 구조화된 데이터다.

Q. Tool Result에 status가 필요한 이유는?

A.
Agent가 성공과 실패를 명확히 구분해야 다음 행동을 결정할 수 있기 때문이다.

Q. Tool 실패 결과도 Agent에게 전달해야 해?

A.
해야 한다. 실패 원인과 retryable 여부를 알아야 재시도나 fallback을 결정할 수 있다.

Q. Tool Result에 민감정보를 넣어도 돼?

A.
안 된다. API Key, Secret, 개인정보, 민감 로그는 포함하지 않는다.

Q. 긴 Tool Result는 어떻게 처리해?

A.
State에 전체를 저장하지 말고 요약하거나 참조만 저장한다.

---

# 4. Tool Calling

## 4.1 Tool Calling 기본 개념

### [개념]

Tool Calling은 LLM이 사용자 요청을 분석해 필요한 Tool과 Arguments를 선택하고 실행 결과를 기반으로 답변하는 구조다.

Tool Calling은 단순 답변 생성이 아니라 Action Selection을 포함한다.

기본 Flow:

```text
User Task
→ LLM decides Tool Call
→ Tool Arguments
→ Tool Execution
→ Tool Result
→ LLM Final Answer
```

Tool Calling은 Agent 구현의 핵심 패턴이다.

---

### [핵심]

- Tool Calling은 LLM이 Tool 사용 여부를 판단한다.
- Tool Name과 Description이 정확해야 한다.
- Args Schema가 명확해야 한다.
- Tool 실행 결과를 Observation으로 전달한다.
- Tool 실패 시 재시도 또는 fallback이 필요하다.
- Tool Calling Loop에는 종료 조건이 필요하다.
- Side Effect가 큰 Tool은 승인 없이 실행하면 안 된다.

---

### [실무]

Tool Calling 사용 대상:

| 작업          | Tool Calling 필요성 |
| ------------- | ------------------- |
| RAG 문서 검색 | 높음                |
| 파일 읽기     | 높음                |
| 코드 분석     | 중간                |
| 테스트 실행   | 중간                |
| API 호출      | 중간                |
| 파일 수정     | 승인 필요           |
| DB 변경       | 승인 필요           |
| 배포          | 명시적 승인 필요    |

Tool Calling Loop:

```text
Agent
→ Tool Call
→ Observation
→ Need more info?
  → yes: Tool Call
  → no: Final Answer
```

Tool Calling 종료 조건:

| 조건                | 처리                     |
| ------------------- | ------------------------ |
| 필요한 정보 확보    | Final Answer             |
| Tool 실패 반복      | Error Node               |
| Max Tool Calls 도달 | Final With Warning       |
| 위험 작업 감지      | Human Approval           |
| 검색 결과 없음      | Missing Context Response |

---

### [FAQ]

Q. Tool Calling이 뭐야?

A.
LLM이 필요한 Tool과 Arguments를 선택하고 Tool 실행 결과를 바탕으로 답변하는 구조다.

Q. Tool Calling과 일반 LLM 답변은 뭐가 달라?

A.
일반 답변은 텍스트 생성만 하지만 Tool Calling은 외부 기능 실행과 결과 관찰을 포함한다.

Q. Tool Calling Loop에 종료 조건이 필요한 이유는?

A.
Agent가 계속 Tool을 호출하는 무한 루프를 막기 위해 필요하다.

Q. Tool Calling 실패 시 어떻게 해?

A.
실패 원인을 확인하고 재시도 가능하면 재시도하며, 불가능하면 fallback 또는 Error Node로 이동한다.

Q. Tool Calling은 위험할 수 있어?

A.
그렇다. 파일 수정, DB 변경, 배포 같은 Side Effect가 있는 Tool은 승인 없이 실행하면 안 된다.

---

# 5. Agent Core

## 5.1 Agent 기본 개념

### [개념]

Agent는 LLM이 Tool, Prompt, State, Memory를 활용해 목표를 수행하는 구조다.

Agent는 단순히 답변하는 LLM이 아니다.

Agent는 상황을 판단하고, 필요하면 Tool을 호출하고, 결과를 관찰한 뒤 다음 행동을 결정한다.

기본 Flow:

```text
User Task
→ Agent Prompt
→ Reasoning
→ Tool Selection
→ Tool Execution
→ Observation
→ Final Answer
```

LangGraph에서는 Agent를 하나의 Node로 표현할 수 있다.

---

### [핵심]

- Agent는 LLM + Tool + Prompt + State 조합이다.
- Agent는 목표를 수행하기 위해 Tool을 선택할 수 있다.
- Agent Prompt는 역할과 제한을 정의한다.
- State는 Agent의 현재 작업 상태를 제공한다.
- Memory는 과거 정보를 재사용할 때 사용한다.
- Stop Condition과 Max Tool Calls가 필요하다.
- Agent Output은 Review Agent가 검증해야 한다.

---

### [실무]

Agent 구성 요소:

| 구성 요소      | 역할             |
| -------------- | ---------------- |
| Agent Prompt   | 역할, 목표, 규칙 |
| Tools          | 실행 가능한 기능 |
| State          | 현재 작업 정보   |
| Memory         | 과거 정보        |
| Model          | 판단과 생성      |
| Parser         | 구조화된 출력    |
| Stop Condition | 종료 기준        |
| Error Handling | 실패 처리        |
| Review         | 결과 검증        |

Agent 종류 예시:

| Agent          | 역할                          |
| -------------- | ----------------------------- |
| PM Agent       | 요청 분석, 작업 분해, 라우팅  |
| RAG Agent      | 문서 검색 기반 답변           |
| Backend Agent  | Backend 코드/구조 작업        |
| Frontend Agent | UI/React/API 연동 작업        |
| DevOps Agent   | Docker, 배포, 운영 작업       |
| AI Agent       | RAG, Agent, LLM Workflow 작업 |
| Review Agent   | 결과 검증                     |
| Fix Agent      | Review 결과 반영              |

---

### [FAQ]

Q. Agent가 뭐야?

A.
LLM이 Tool, Prompt, State를 활용해 목표를 수행하는 구조다.

Q. Agent와 일반 Chat Model은 뭐가 달라?

A.
Chat Model은 답변 생성 중심이고, Agent는 Tool 사용과 상태 기반 의사결정을 포함한다.

Q. Agent는 모든 작업을 자동으로 해도 돼?

A.
아니다. 권한 제한, Stop Condition, Human Approval, Review가 필요하다.

Q. Agent Output은 왜 검증해야 해?

A.
Agent가 잘못된 Tool을 사용하거나 문서에 없는 내용을 생성할 수 있기 때문이다.

Q. LangGraph에서 Agent는 어떻게 표현해?

A.
Agent 하나를 Node로 표현하고 State를 입력받아 결과를 State에 업데이트하게 만들 수 있다.

---

# 6. Agent Prompt

## 6.1 Agent 역할과 제한 정의

### [개념]

Agent Prompt는 Agent가 어떤 역할을 수행하고, 어떤 Tool을 사용할 수 있으며, 어떤 제한을 지켜야 하는지 정의하는 지시문이다.

Agent Prompt는 일반 답변 Prompt보다 권한, 책임, 출력 형식, 위험 작업 기준이 중요하다.

기본 구조:

```text
System:
너는 {agent_role} Agent다.
목표는 {goal}이다.
사용 가능한 Tool은 {tools}이다.
위험 작업은 승인 없이 실행하지 마라.
결과는 {output_schema} 형식으로 반환하라.

State:
{state}

Task:
{task}
```

---

### [핵심]

- Agent 역할을 명확히 정의한다.
- Agent가 담당하지 않는 범위를 명시한다.
- 사용할 수 있는 Tool을 제한한다.
- Tool 사용 조건을 설명한다.
- 출력 형식을 고정한다.
- 위험 작업은 Human Approval로 라우팅한다.
- 불확실하면 추측하지 않고 근거 부족을 표시한다.

---

### [실무]

PM Agent Prompt 예시:

```text
System:
너는 개인 AI 개발팀의 PM Agent다.
사용자 요청을 분석하고 작업을 분해하라.
필요한 Domain Agent를 선택하라.
모든 요청을 모든 Agent에게 보내지 마라.
위험 작업이 포함되면 needs_human_approval=true로 표시하라.

Output:
{
  "task_type": "...",
  "required_agents": [],
  "requirements": [],
  "needs_human_approval": false
}
```

RAG Agent Prompt 예시:

```text
System:
너는 문서 기반 RAG Agent다.
반드시 RAG Tool로 검색한 Context를 근거로 답변하라.
문서에 없는 내용은 "문서에서 확인되지 않음"이라고 답하라.
Source를 포함하라.
```

Review Agent Prompt 예시:

```text
System:
너는 Review Agent다.
Agent Output을 요구사항, 문서 근거, 코드 정확성, 보안 위험, 누락 기준으로 검토하라.
결과는 pass/fail과 findings로 반환하라.
```

Agent Prompt 금지:

- 무제한 권한 부여
- Tool 사용 조건 생략
- 위험 작업 자동 실행 지시
- 출력 형식 미지정
- 모든 Domain을 한 Agent에게 맡김
- 문서 근거 없는 답변 허용

---

### [FAQ]

Q. Agent Prompt가 뭐야?

A.
Agent의 역할, 책임, Tool 사용 조건, 출력 형식, 제한 사항을 정의하는 Prompt다.

Q. Agent Prompt는 일반 Prompt와 뭐가 달라?

A.
역할뿐 아니라 Tool 권한, Stop Condition, Human Approval, Output Schema가 중요하다.

Q. PM Agent Prompt에는 무엇이 들어가?

A.
요청 분석, 작업 분해, Agent 선택, Routing 결과, 승인 필요 여부가 들어간다.

Q. RAG Agent Prompt에는 무엇이 들어가?

A.
문서 검색 우선, Context 기반 답변, Source 포함, 문서에 없는 내용 금지 규칙이 들어간다.

Q. Agent Prompt에서 가장 위험한 실수는?

A.
Agent에게 무제한 권한을 주고 위험 Tool을 승인 없이 실행하게 하는 것이다.

---

# 7. Agent State

## 7.1 Agent와 State 연결

### [개념]

Agent State는 Agent가 현재 작업을 수행하는 데 필요한 실행 상태다.

LangGraph에서 Agent Node는 State를 읽고 필요한 작업을 수행한 뒤 State 일부를 업데이트한다.

기본 Flow:

```text
State Input
→ Agent Node
→ Tool Calling
→ Agent Output
→ State Update
```

Agent State는 현재 Workflow의 실행 상태이고, Memory는 과거 정보를 재사용하기 위한 구조다.

---

### [핵심]

- Agent는 State를 입력으로 받는다.
- State는 사용자 요청, 요구사항, 검색 결과, Tool 결과, Agent 결과를 포함할 수 있다.
- Agent는 전체 State를 무조건 수정하지 않는다.
- Agent는 자신이 담당하는 필드만 업데이트한다.
- Tool Result는 필요한 정보만 State에 저장한다.
- State가 너무 커지면 Context 품질이 낮아진다.
- 최신 사용자 요청이 오래된 State보다 우선한다.

---

### [실무]

Agent State 예시:

```python
from typing import TypedDict

class AgentState(TypedDict):
    user_request: str
    task_type: str
    requirements: list[str]
    current_agent: str
    available_tools: list[str]
    tool_results: list[dict]
    retrieved_context: list[dict]
    agent_outputs: dict
    review_findings: list[str]
    status: str
    error: str | None
```

Agent별 State 사용 기준:

| Agent         | 읽는 State                      | 쓰는 State                 |
| ------------- | ------------------------------- | -------------------------- |
| PM Agent      | user_request                    | task_type, requirements    |
| RAG Agent     | user_request, task_type         | retrieved_context, sources |
| Backend Agent | requirements, retrieved_context | agent_outputs.backend      |
| Review Agent  | requirements, agent_outputs     | review_findings, status    |
| Fix Agent     | review_findings, agent_outputs  | agent_outputs.fixed        |
| Final Agent   | agent_outputs, review_findings  | final_output               |

State 관리 금지:

- 모든 Tool Result 전체 저장
- Retrieved Context 무제한 누적
- 다른 Agent의 필드 무단 수정
- 오래된 State를 최신 요청보다 우선
- 민감정보를 State에 저장

---

### [FAQ]

Q. Agent State가 뭐야?

A.
Agent가 현재 작업을 수행하기 위해 읽고 업데이트하는 실행 상태 데이터다.

Q. Agent는 State 전체를 수정해도 돼?

A.
권장하지 않는다. 자신이 담당하는 필드만 업데이트해야 한다.

Q. Tool Result는 State에 전부 저장해야 해?

A.
아니다. 필요한 정보만 저장하고 긴 결과는 요약하거나 참조로 저장한다.

Q. Agent State와 Memory는 달라?

A.
다르다. State는 현재 Workflow 상태이고 Memory는 과거 정보를 재사용하기 위한 구조다.

Q. State가 너무 커지면 왜 문제야?

A.
Context가 길어지고 Agent 판단 품질과 응답 속도가 낮아질 수 있다.

---

# 8. Tool Node

## 8.1 LangGraph Tool Node

### [개념]

Tool Node는 LangGraph에서 Tool 실행을 담당하는 Node다.

Agent Node가 Tool 사용 필요성을 판단하고, Tool Node가 실제 Tool을 실행한 뒤 결과를 State에 저장하는 구조로 설계할 수 있다.

기본 Flow:

```text
Agent Node
→ Tool Call Request
→ Tool Node
→ Tool Execution
→ Tool Result
→ State Update
→ Agent Node or Next Node
```

Tool Node를 분리하면 Tool 실행, 권한 검증, 오류 처리를 중앙화할 수 있다.

---

### [핵심]

- Tool Node는 Tool 실행을 담당한다.
- Agent Node와 Tool 실행 책임을 분리할 수 있다.
- Tool Node는 Args Schema를 검증한다.
- Tool Node는 Permission을 확인한다.
- Tool Node는 Tool Result를 구조화한다.
- Tool Node는 오류를 State에 기록한다.
- 위험 Tool은 Approval Node로 라우팅한다.

---

### [실무]

Tool Node State 예시:

```python
from typing import TypedDict

class ToolCallState(TypedDict):
    requested_tool: str
    tool_args: dict
    tool_permission: str
    approval_required: bool
    tool_result: dict
    error: str | None
```

Tool Node 실행 Flow:

```text
Tool Call Request
→ Validate Tool Name
→ Validate Args Schema
→ Check Permission
→ If risky: Approval Node
→ Execute Tool
→ Return Tool Result
→ Update State
```

Tool Node Routing:

| 상태                   | 다음 Node                 |
| ---------------------- | ------------------------- |
| success                | Agent Node or Review Node |
| invalid_arguments      | Agent Retry Node          |
| permission_denied      | Error Node                |
| approval_required      | Human Approval Node       |
| timeout                | Retry or Error Node       |
| unsafe_action          | Human Approval Node       |
| max_tool_calls_reached | Final With Warning        |

Tool Node 장점:

- Tool 실행 로직 중앙화
- 권한 검증 일관성
- 오류 처리 일관성
- Tool Result 구조 통일
- 위험 작업 승인 흐름 분리

---

### [FAQ]

Q. Tool Node가 뭐야?

A.
LangGraph에서 Tool 실행, 인자 검증, 권한 확인, 결과 저장을 담당하는 Node다.

Q. Agent Node와 Tool Node를 분리하는 이유는?

A.
Agent는 판단을 담당하고 Tool Node는 실행과 검증을 담당하게 해 책임을 분리하기 위해서다.

Q. Tool Node는 무엇을 검증해?

A.
Tool Name, Args Schema, Permission, 위험 작업 여부를 검증한다.

Q. 위험 Tool 요청은 어디로 보내?

A.
Human Approval Node로 라우팅해야 한다.

Q. Tool Node 결과는 어디에 저장해?

A.
State의 tool_result, tool_results, error 같은 필드에 저장한다.

---

# 9. Tool Permission

## 9.1 Tool 권한과 안전 실행

### [개념]

Tool Permission은 Agent가 어떤 Tool을 자동 실행할 수 있고, 어떤 Tool은 사용자 승인 후 실행해야 하는지 정의하는 기준이다.

Agent가 Tool을 사용할 수 있다고 해서 모든 Tool을 자유롭게 실행해도 되는 것은 아니다.

기본 Flow:

```text
Tool Request
→ Permission Check
→ Safe: Execute
→ Risky: Human Approval
→ Denied: Error
```

Tool Permission은 Agent Workflow의 안전성과 신뢰성을 결정한다.

---

### [핵심]

- Tool은 위험도에 따라 권한을 분리한다.
- 읽기 Tool은 상대적으로 안전하다.
- 쓰기 Tool은 승인 기준이 필요하다.
- 삭제, DB 변경, 배포, 외부 발송은 명시적 승인 대상이다.
- 비용 발생 Tool은 승인 또는 한도 설정이 필요하다.
- Agent Prompt와 Tool Node 모두 권한 기준을 포함해야 한다.
- 승인 범위를 넘어서는 실행은 금지한다.

---

### [실무]

권한 레벨 예시:

| Permission        | 설명             | 예시                                 |
| ----------------- | ---------------- | ------------------------------------ |
| read_only         | 읽기 전용        | search_rag_documents, read_file      |
| safe_execute      | 안전 실행        | run_lint, run_unit_test              |
| write_limited     | 제한적 쓰기      | create_draft, generate_file          |
| approval_required | 승인 필요        | write_file, modify_db                |
| critical_approval | 명시적 승인 필요 | delete_file, deploy_prod, send_email |
| denied            | 자동 실행 금지   | destructive_shell_command            |

승인 필요 Tool:

| Tool                | 승인 이유   |
| ------------------- | ----------- |
| write_file          | 파일 변경   |
| delete_file         | 데이터 손실 |
| modify_database     | 데이터 손상 |
| deploy_service      | 운영 장애   |
| send_external_email | 외부 영향   |
| call_paid_api       | 비용 발생   |
| change_permission   | 보안 위험   |

Permission Check 예시:

```json
{
  "requested_tool": "deploy_service",
  "environment": "prod",
  "permission": "critical_approval",
  "approval_required": true,
  "reason": "Production deployment can affect live service."
}
```

---

### [FAQ]

Q. Tool Permission이 뭐야?

A.
Agent가 Tool을 자동 실행할 수 있는지, 사용자 승인이 필요한지 판단하는 권한 기준이다.

Q. 읽기 Tool은 자동 실행해도 돼?

A.
대체로 가능하지만 민감 파일이나 개인정보 접근은 제한해야 한다.

Q. 쓰기 Tool은 왜 조심해야 해?

A.
파일 변경, 데이터 손상, 운영 장애 같은 Side Effect가 발생할 수 있기 때문이다.

Q. 배포 Tool은 자동 실행해도 돼?

A.
안 된다. 특히 production 배포는 명시적 사용자 승인이 필요하다.

Q. 승인 범위를 넘어서는 작업은 가능해?

A.
불가능하다. 사용자가 승인한 범위 안에서만 Tool을 실행해야 한다.

---

# 10. Agent Workflow

## 10.1 Tool Calling Agent Workflow

### [개념]

Tool Calling Agent Workflow는 Agent가 필요한 Tool을 선택하고 실행 결과를 관찰하며 목표를 완료하는 흐름이다.

단순 Chain은 정해진 순서로 실행되지만, Agent Workflow는 상태와 결과에 따라 다음 행동이 달라질 수 있다.

기본 Flow:

```text
User Task
→ Agent Node
→ Need Tool?
→ Tool Node
→ Observation
→ Continue or Final
```

LangGraph에서는 Agent Node, Tool Node, Review Node, Final Node를 연결해 Tool Calling Agent를 구성할 수 있다.

---

### [핵심]

- Agent는 사용자 요청과 State를 분석한다.
- 필요하면 Tool Call을 생성한다.
- Tool Node는 Tool을 실행하고 Result를 반환한다.
- Agent는 Observation을 바탕으로 다음 행동을 결정한다.
- 완료 조건을 만족하면 Final Answer를 생성한다.
- Tool 호출 횟수 제한이 필요하다.
- 실패 시 Retry, Fallback, Error Node로 분기한다.

---

### [실무]

Tool Calling Agent Graph:

```text
START
→ Agent Node
→ if tool_needed: Tool Node
→ Agent Node
→ if final_ready: Review Node
→ Final Node
→ END
```

Routing 조건 예시:

| 조건                         | 다음 Node           |
| ---------------------------- | ------------------- |
| tool_needed = true           | Tool Node           |
| tool_result.status = success | Agent Node          |
| tool_result.status = error   | Retry or Error Node |
| approval_required = true     | Human Approval Node |
| final_ready = true           | Review Node         |
| review_result = pass         | Final Node          |
| review_result = fail         | Fix Node            |

Max Tool Calls 기준:

```text
tool_call_count >= max_tool_calls
→ Stop Tool Loop
→ Final With Warning or Error Node
```

Tool Calling Agent State 예시:

```python
class ToolCallingAgentState(TypedDict):
    user_request: str
    current_step: str
    tool_needed: bool
    requested_tool: str | None
    tool_args: dict | None
    tool_result: dict | None
    tool_call_count: int
    max_tool_calls: int
    final_ready: bool
    agent_output: str
    error: str | None
```

---

### [FAQ]

Q. Tool Calling Agent Workflow가 뭐야?

A.
Agent가 필요한 Tool을 선택하고 실행 결과를 관찰하며 최종 답변까지 진행하는 Workflow다.

Q. Agent Workflow와 Chain은 뭐가 달라?

A.
Chain은 정해진 순서로 실행되고, Agent Workflow는 상태와 Tool 결과에 따라 다음 행동이 달라진다.

Q. Tool 호출 횟수 제한은 왜 필요해?

A.
무한 Tool Loop를 방지하고 비용과 시간을 제한하기 위해 필요하다.

Q. Tool 실패 시 다음 단계는?

A.
재시도 가능하면 Retry하고, 불가능하면 Error Node 또는 Final With Warning으로 이동한다.

Q. 최종 답변 전에 Review Node가 필요한 이유는?

A.
Agent Output이 요구사항을 충족하고 Tool Result에 근거하는지 검증하기 위해 필요하다.

---

# 11. Tool Calling Troubleshooting

## 11.1 Tool Calling 실패 처리

### [개념]

Tool Calling 실패는 Tool 선택 오류, Args Schema 오류, 권한 오류, 실행 오류, 결과 해석 오류로 나눌 수 있다.

오류 유형을 구분해야 Agent Workflow를 안정적으로 복구할 수 있다.

기본 Flow:

```text
Tool Calling Failure
→ Identify Error Type
→ Retry or Fallback
→ Update State
→ Continue or Stop
```

---

### [핵심]

문제:

- Agent가 잘못된 Tool을 선택함
- Tool Arguments가 Schema와 맞지 않음
- 승인 없이 위험 Tool을 호출함
- Tool 실행이 Timeout 됨
- Tool Result를 Agent가 잘못 해석함
- Tool Loop가 끝나지 않음

원인:

- Tool Description이 모호함
- Args Schema가 복잡함
- Permission 기준이 없음
- Error Result 구조가 불명확함
- Stop Condition 없음
- Tool이 너무 많음

해결:

- Tool Description 개선
- Args Schema 단순화
- Tool Arguments Validation 추가
- Permission Check 추가
- Tool Result Schema 통일
- Max Tool Calls 설정
- 위험 Tool은 Approval Node로 라우팅

---

### [실무]

Troubleshooting Matrix:

| 증상                 | 원인                | 해결                       |
| -------------------- | ------------------- | -------------------------- |
| 잘못된 Tool 선택     | Description 모호    | Tool 설명 보강             |
| Args 오류            | Schema 복잡         | Schema 단순화              |
| 권한 오류            | Permission 미정의   | Permission Table 추가      |
| 무한 Tool Loop       | Stop Condition 없음 | Max Tool Calls 설정        |
| 실패를 성공으로 처리 | Result 구조 불명확  | status 필드 필수화         |
| 위험 작업 자동 실행  | Approval 없음       | Human Approval Node 추가   |
| Tool 결과 누락       | State Update 오류   | Tool Result 저장 규칙 추가 |

Tool Calling 점검 Flow:

```text
1. Agent Prompt 확인
2. Tool Description 확인
3. Args Schema 확인
4. Tool Arguments Validation 확인
5. Permission Check 확인
6. Tool Result Schema 확인
7. State Update 확인
8. Stop Condition 확인
9. Review Node 검증 확인
```

---

### [FAQ]

Q. Agent가 잘못된 Tool을 선택하는 이유는?

A.
Tool Description이 모호하거나 Tool이 너무 많거나 Agent Prompt의 사용 기준이 부족하기 때문이다.

Q. Tool Arguments 오류는 어떻게 줄여?

A.
Args Schema를 단순화하고 필수 인자, enum, 범위 제한을 명확히 해야 한다.

Q. Tool Loop가 끝나지 않으면 어떻게 해?

A.
Max Tool Calls와 final_ready 조건을 추가해야 한다.

Q. Tool 실패를 Agent가 성공으로 오해하면 어떻게 해?

A.
Tool Result에 status, error_type, retryable 필드를 포함해 구조화해야 한다.

Q. 위험 Tool 자동 실행을 막으려면?

A.
Permission Check와 Human Approval Node를 추가해야 한다.

---

# 12. Part05 Checklist

## 12.1 Tool & Agent Checklist

### [Checklist]

- [ ] Tool Name이 명확한가?
- [ ] Tool Description이 사용 조건을 설명하는가?
- [ ] Args Schema가 단순하고 검증 가능한가?
- [ ] 필수 인자와 선택 인자가 구분되는가?
- [ ] 경로, 명령어, URL, SQL 인자를 검증하는가?
- [ ] Tool Result에 status가 포함되는가?
- [ ] Tool Error에 error_type과 retryable이 포함되는가?
- [ ] Tool Result에 민감정보가 포함되지 않는가?
- [ ] Tool 위험도와 Permission이 정의되었는가?
- [ ] 위험 Tool은 Human Approval Node로 라우팅되는가?
- [ ] Agent Prompt에 역할과 제한이 명확한가?
- [ ] Agent가 모든 Tool을 무제한 사용할 수 없도록 제한했는가?
- [ ] Agent State가 필요한 필드만 유지하는가?
- [ ] Tool Result를 State에 무제한 누적하지 않는가?
- [ ] Tool Node가 Args와 Permission을 검증하는가?
- [ ] Tool Calling Loop에 Stop Condition이 있는가?
- [ ] Max Tool Calls가 설정되었는가?
- [ ] Tool 실패 시 Retry / Fallback 기준이 있는가?
- [ ] Review Node가 Agent Output을 검증하는가?
- [ ] Tool Calling Troubleshooting 기준이 있는가?

---

# Retrieval Queries

### [FAQ]

Q. Tool이 뭐야?
A. Agent가 검색, 파일 처리, API 호출, 테스트 실행 같은 외부 기능을 사용할 수 있게 하는 실행 인터페이스다.

Q. Agent에게 Tool이 왜 필요해?
A. LLM 자체는 외부 시스템을 직접 조작하지 못하므로 Tool을 통해 실제 작업을 수행해야 하기 때문이다.

Q. Tool Description은 왜 중요해?
A. Agent가 어떤 상황에서 어떤 Tool을 사용할지 판단하는 기준이 되기 때문이다.

Q. Tool Arguments는 왜 검증해야 해?
A. LLM이 생성한 인자는 틀리거나 위험할 수 있으므로 실행 전 검증이 필요하다.

Q. 위험 Tool은 어떻게 처리해?
A. 파일 삭제, DB 변경, 배포, 비용 발생 같은 Tool은 Human Approval 이후 실행해야 한다.

Q. Args Schema가 뭐야?
A. Tool이 받을 입력 인자의 이름, 타입, 필수 여부, 제한 조건을 정의하는 구조다.

Q. Args Schema는 왜 필요해?
A. LLM이 생성한 Tool Arguments를 검증하고 잘못된 실행을 막기 위해 필요하다.

Q. Tool Schema는 복잡해도 돼?
A. 너무 복잡하면 Agent가 인자를 잘못 생성할 가능성이 증가하므로 단순하게 설계하는 것이 좋다.

Q. 어떤 Tool 인자를 특히 검증해야 해?
A. 파일 경로, 명령어, URL, SQL, API Payload, 배포 환경 같은 위험 인자를 검증해야 한다.

Q. Tool Result가 뭐야?
A. Tool 실행 결과를 Agent가 이해할 수 있도록 반환하는 구조화된 데이터다.

Q. Tool Result에 status가 필요한 이유는?
A. Agent가 성공과 실패를 명확히 구분해야 다음 행동을 결정할 수 있기 때문이다.

Q. Tool 실패 결과도 Agent에게 전달해야 해?
A. 해야 한다. 실패 원인과 retryable 여부를 알아야 재시도나 fallback을 결정할 수 있다.

Q. Tool Result에 민감정보를 넣어도 돼?
A. 안 된다. API Key, Secret, 개인정보, 민감 로그는 포함하지 않는다.

Q. 긴 Tool Result는 어떻게 처리해?
A. State에 전체를 저장하지 말고 요약하거나 참조만 저장한다.

Q. Tool Calling이 뭐야?
A. LLM이 필요한 Tool과 Arguments를 선택하고 Tool 실행 결과를 바탕으로 답변하는 구조다.

Q. Tool Calling과 일반 LLM 답변은 뭐가 달라?
A. 일반 답변은 텍스트 생성만 하지만 Tool Calling은 외부 기능 실행과 결과 관찰을 포함한다.

Q. Tool Calling Loop에 종료 조건이 필요한 이유는?
A. Agent가 계속 Tool을 호출하는 무한 루프를 막기 위해 필요하다.

Q. Tool Calling 실패 시 어떻게 해?
A. 실패 원인을 확인하고 재시도 가능하면 재시도하며, 불가능하면 fallback 또는 Error Node로 이동한다.

Q. Tool Calling은 위험할 수 있어?
A. 그렇다. 파일 수정, DB 변경, 배포 같은 Side Effect가 있는 Tool은 승인 없이 실행하면 안 된다.

Q. Agent가 뭐야?
A. LLM이 Tool, Prompt, State를 활용해 목표를 수행하는 구조다.

Q. Agent와 일반 Chat Model은 뭐가 달라?
A. Chat Model은 답변 생성 중심이고, Agent는 Tool 사용과 상태 기반 의사결정을 포함한다.

Q. Agent는 모든 작업을 자동으로 해도 돼?
A. 아니다. 권한 제한, Stop Condition, Human Approval, Review가 필요하다.

Q. Agent Output은 왜 검증해야 해?
A. Agent가 잘못된 Tool을 사용하거나 문서에 없는 내용을 생성할 수 있기 때문이다.

Q. LangGraph에서 Agent는 어떻게 표현해?
A. Agent 하나를 Node로 표현하고 State를 입력받아 결과를 State에 업데이트하게 만들 수 있다.

Q. Agent Prompt가 뭐야?
A. Agent의 역할, 책임, Tool 사용 조건, 출력 형식, 제한 사항을 정의하는 Prompt다.

Q. Agent Prompt는 일반 Prompt와 뭐가 달라?
A. 역할뿐 아니라 Tool 권한, Stop Condition, Human Approval, Output Schema가 중요하다.

Q. PM Agent Prompt에는 무엇이 들어가?
A. 요청 분석, 작업 분해, Agent 선택, Routing 결과, 승인 필요 여부가 들어간다.

Q. RAG Agent Prompt에는 무엇이 들어가?
A. 문서 검색 우선, Context 기반 답변, Source 포함, 문서에 없는 내용 금지 규칙이 들어간다.

Q. Agent Prompt에서 가장 위험한 실수는?
A. Agent에게 무제한 권한을 주고 위험 Tool을 승인 없이 실행하게 하는 것이다.

Q. Agent State가 뭐야?
A. Agent가 현재 작업을 수행하기 위해 읽고 업데이트하는 실행 상태 데이터다.

Q. Agent는 State 전체를 수정해도 돼?
A. 권장하지 않는다. 자신이 담당하는 필드만 업데이트해야 한다.

Q. Tool Result는 State에 전부 저장해야 해?
A. 아니다. 필요한 정보만 저장하고 긴 결과는 요약하거나 참조로 저장한다.

Q. Agent State와 Memory는 달라?
A. 다르다. State는 현재 Workflow 상태이고 Memory는 과거 정보를 재사용하기 위한 구조다.

Q. Tool Node가 뭐야?
A. LangGraph에서 Tool 실행, 인자 검증, 권한 확인, 결과 저장을 담당하는 Node다.

Q. Agent Node와 Tool Node를 분리하는 이유는?
A. Agent는 판단을 담당하고 Tool Node는 실행과 검증을 담당하게 해 책임을 분리하기 위해서다.

Q. Tool Node는 무엇을 검증해?
A. Tool Name, Args Schema, Permission, 위험 작업 여부를 검증한다.

Q. 위험 Tool 요청은 어디로 보내?
A. Human Approval Node로 라우팅해야 한다.

Q. Tool Permission이 뭐야?
A. Agent가 Tool을 자동 실행할 수 있는지, 사용자 승인이 필요한지 판단하는 권한 기준이다.

Q. 읽기 Tool은 자동 실행해도 돼?
A. 대체로 가능하지만 민감 파일이나 개인정보 접근은 제한해야 한다.

Q. 쓰기 Tool은 왜 조심해야 해?
A. 파일 변경, 데이터 손상, 운영 장애 같은 Side Effect가 발생할 수 있기 때문이다.

Q. 배포 Tool은 자동 실행해도 돼?
A. 안 된다. 특히 production 배포는 명시적 사용자 승인이 필요하다.

Q. Tool Calling Agent Workflow가 뭐야?
A. Agent가 필요한 Tool을 선택하고 실행 결과를 관찰하며 최종 답변까지 진행하는 Workflow다.

Q. Agent Workflow와 Chain은 뭐가 달라?
A. Chain은 정해진 순서로 실행되고, Agent Workflow는 상태와 Tool 결과에 따라 다음 행동이 달라진다.

Q. Tool 호출 횟수 제한은 왜 필요해?
A. 무한 Tool Loop를 방지하고 비용과 시간을 제한하기 위해 필요하다.

Q. Tool 실패 시 다음 단계는?
A. 재시도 가능하면 Retry하고, 불가능하면 Error Node 또는 Final With Warning으로 이동한다.

Q. 최종 답변 전에 Review Node가 필요한 이유는?
A. Agent Output이 요구사항을 충족하고 Tool Result에 근거하는지 검증하기 위해 필요하다.

Q. Agent가 잘못된 Tool을 선택하는 이유는?
A. Tool Description이 모호하거나 Tool이 너무 많거나 Agent Prompt의 사용 기준이 부족하기 때문이다.

Q. Tool Arguments 오류는 어떻게 줄여?
A. Args Schema를 단순화하고 필수 인자, enum, 범위 제한을 명확히 해야 한다.

Q. Tool Loop가 끝나지 않으면 어떻게 해?
A. Max Tool Calls와 final_ready 조건을 추가해야 한다.

Q. Tool 실패를 Agent가 성공으로 오해하면 어떻게 해?
A. Tool Result에 status, error_type, retryable 필드를 포함해 구조화해야 한다.

Q. 위험 Tool 자동 실행을 막으려면?
A. Permission Check와 Human Approval Node를 추가해야 한다.
