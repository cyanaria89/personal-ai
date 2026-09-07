# LangChain & LangGraph Part06 State Node Edge Routing

---

# 1. LangGraph State Core

## 1.1 State 기본 개념

### [개념]

State는 LangGraph Workflow에서 Node 간 공유되는 실행 상태 데이터다.

State는 현재 사용자 요청, 작업 단계, 요구사항, 검색 결과, Tool 결과, Agent 출력, Review 결과, 오류 상태를 저장한다.

기본 Flow:

```text
Initial State
→ Node Execution
→ State Update
→ Edge
→ Next Node
→ Final State
```

State는 현재 Workflow의 실행 상태다.

Memory는 과거 정보를 재사용하기 위한 구조다.

Checkpoint는 현재 Workflow State Snapshot을 저장하는 구조다.

State, Memory, Checkpoint는 서로 다른 개념이다.

---

### [핵심]

- State는 Node들이 읽고 업데이트하는 공유 실행 상태다.
- State Schema는 Workflow 안정성을 높인다.
- Node는 State를 입력으로 받는다.
- Node는 전체 State가 아니라 변경할 필드만 반환할 수 있다.
- State는 현재 Workflow의 실행 상태를 저장한다.
- Memory는 과거 정보를 재사용하기 위한 구조다.
- Checkpoint는 State Snapshot을 저장해 중단과 재개에 사용한다.
- 최신 사용자 요청이 오래된 State보다 우선한다.
- State가 너무 커지면 Context 품질과 실행 속도가 낮아진다.
- 민감정보는 State에 저장하지 않는다.

---

### [실무]

2026 실무 기준 LangGraph Workflow는 State Schema를 먼저 정의하고 Node를 설계하는 방식이 안정적이다.

기본 State 예시:

```python
from typing import TypedDict, Literal

class AgentState(TypedDict):
    user_request: str
    current_step: str
    task_type: Literal["sql", "backend", "frontend", "devops", "ai", "mixed", "unknown"]
    requirements: list[str]
    required_agents: list[str]
    metadata_filter: dict
    retrieved_context: list[dict]
    tool_results: list[dict]
    agent_outputs: dict[str, str]
    review_result: Literal["pass", "fail", "warning", "unknown"]
    review_findings: list[str]
    fix_count: int
    max_fix_count: int
    final_output: str
    status: Literal["running", "waiting_approval", "pass", "fail", "error"]
    error_type: str | None
    error: str | None
```

State 설계 기준:

| 필드              | 목적                                         |
| ----------------- | -------------------------------------------- |
| user_request      | 원본 사용자 요청                             |
| current_step      | 현재 실행 단계                               |
| task_type         | sql, backend, frontend, ai 등 분기 기준      |
| requirements      | PM Agent가 추출한 요구사항                   |
| required_agents   | 실행할 Agent 목록                            |
| metadata_filter   | RAG 검색 범위 제한                           |
| retrieved_context | RAG 검색 결과                                |
| tool_results      | Tool 실행 결과 요약                          |
| agent_outputs     | Domain Agent 결과                            |
| review_result     | Review 결과                                  |
| review_findings   | Review 지적 사항                             |
| fix_count         | 수정 반복 횟수                               |
| max_fix_count     | 최대 수정 횟수                               |
| final_output      | 최종 사용자 응답                             |
| status            | running, waiting_approval, pass, fail, error |
| error_type        | 오류 유형                                    |
| error             | 오류 메시지                                  |

State 관리 금지:

```text
민감정보 저장
Tool 로그 전체 누적
Retrieved Context 무제한 누적
다른 Node의 필드 무단 덮어쓰기
오래된 State를 최신 요청보다 우선
```

---

### [FAQ]

Q. LangGraph State가 뭐야?

A.
LangGraph Workflow에서 Node들이 읽고 업데이트하는 공유 실행 상태 데이터다.

Q. State Schema는 왜 필요해?

A.
Node 간 입력과 출력 형식을 안정화하고 Workflow 오류를 줄이기 위해 필요하다.

Q. State와 Memory는 달라?

A.
다르다. State는 현재 Workflow 상태이고 Memory는 과거 정보를 재사용하기 위한 구조다.

Q. State와 Checkpoint는 달라?

A.
다르다. State는 현재 실행 상태이고 Checkpoint는 그 State Snapshot을 저장해 재개에 사용하는 구조다.

Q. State가 너무 커지면 왜 문제야?

A.
Context가 길어지고 Node 실행 품질, 응답 속도, 디버깅 가능성이 낮아질 수 있다.

---

# 2. State Schema Design

## 2.1 State Schema 설계 기준

### [개념]

State Schema는 Workflow에서 사용할 State 필드와 타입을 정의하는 데이터 계약이다.

State Schema가 명확하면 Node, Edge, Router, Review / Fix Loop, Error Routing이 안정적으로 동작한다.

기본 구조:

```text
State Schema
→ Node Input Contract
→ Node Output Contract
→ Routing Condition
→ Final State
```

State Schema는 Agent Workflow의 중심 설계 기준이다.

---

### [핵심]

- State Schema는 필드명과 타입을 명확히 정의한다.
- Node가 읽는 필드와 쓰는 필드를 구분한다.
- Routing에 사용할 필드는 enum 또는 제한된 값이 좋다.
- 오류 상태를 표현할 status, error_type, error 필드가 필요하다.
- 반복 루프에는 count 필드가 필요하다.
- Tool 결과는 필요한 정보만 저장한다.
- Retrieved Context는 무제한 누적하지 않는다.
- 민감정보는 State에 저장하지 않는다.
- State Schema 변경 시 Checkpoint 호환성을 고려한다.

---

### [실무]

개인 AI 개발팀 State 예시:

```python
from typing import TypedDict, Literal

class DevTeamState(TypedDict):
    user_request: str
    current_step: str
    task_type: Literal["sql", "backend", "frontend", "devops", "ai", "mixed", "unknown"]
    requirements: list[str]
    required_agents: list[str]
    current_agent: str
    completed_agents: list[str]
    metadata_filter: dict
    retrieved_context: list[dict]
    agent_outputs: dict[str, str]
    review_result: Literal["pass", "fail", "warning", "unknown"]
    review_findings: list[str]
    fix_count: int
    max_fix_count: int
    approval_required: bool
    approval_scope: dict
    final_output: str
    status: Literal["running", "waiting_approval", "pass", "fail", "error"]
    error_type: str | None
    error: str | None
```

State 필드 분리 기준:

| 유형        | 필드 예시                                 |
| ----------- | ----------------------------------------- |
| 요청 정보   | user_request, requirements                |
| 라우팅 정보 | task_type, required_agents, current_agent |
| 진행 정보   | current_step, completed_agents            |
| 검색 정보   | metadata_filter, retrieved_context        |
| 실행 결과   | agent_outputs, tool_results               |
| 검토 정보   | review_result, review_findings            |
| 반복 제어   | fix_count, max_fix_count                  |
| 승인 정보   | approval_required, approval_scope         |
| 종료 정보   | final_output, status                      |
| 오류 정보   | error_type, error                         |

State Schema 설계 금지:

- 여러 의미를 하나의 문자열 필드에 혼합
- task_type 값을 자유 문자열로 방치
- status 값을 임의 문자열로 방치
- error_type 없이 error 메시지만 저장
- 반복 횟수 없이 Loop 구성
- Tool Result 전체를 그대로 누적
- Retrieved Context 무제한 저장
- 민감정보 저장

---

### [FAQ]

Q. State Schema가 뭐야?

A.
Workflow에서 사용할 State 필드와 타입을 정의하는 데이터 구조다.

Q. State Schema는 언제 정의해야 해?

A.
Node와 Edge를 만들기 전에 먼저 정의하는 것이 좋다.

Q. Routing 필드는 어떻게 설계해?

A.
task_type, status, review_result처럼 제한된 enum 값으로 설계하는 것이 안정적이다.

Q. 반복 루프에는 어떤 State가 필요해?

A.
fix_count, max_fix_count, review_result, status 같은 필드가 필요하다.

Q. State Schema 변경 시 무엇을 주의해야 해?

A.
기존 Checkpoint와 호환되지 않을 수 있으므로 version 또는 migration 기준이 필요하다.

---

# 3. Node Core

## 3.1 Node 기본 개념

### [개념]

Node는 LangGraph에서 하나의 작업 단위다.

Node는 State를 입력받아 작업을 수행하고 State Update를 반환한다.

기본 Flow:

```text
State Input
→ Node Function
→ State Update
```

Node는 Function Node, Agent Node, RAG Node, Tool Node, Review Node, Fix Node, Final Node, Error Node로 구성할 수 있다.

Node의 핵심은 하나의 책임을 명확히 가지는 것이다.

---

### [핵심]

- Node는 하나의 책임을 가진 작업 단위다.
- Node는 State를 입력으로 받는다.
- Node는 작업 후 State Update를 반환한다.
- Agent 하나를 Node로 표현할 수 있다.
- RAG Chain도 Node 내부에서 실행할 수 있다.
- Tool 실행도 Node로 분리할 수 있다.
- Review와 Fix도 Node로 구성할 수 있다.
- Node 책임이 커질수록 디버깅과 재사용이 어려워진다.
- Node Output은 다음 Node가 사용할 수 있는 구조여야 한다.

---

### [실무]

Node 종류:

| Node                | 역할                                   |
| ------------------- | -------------------------------------- |
| PM Node             | 요청 분석, 작업 분해, 라우팅 정보 생성 |
| Router Node         | 다음 Agent 선택                        |
| RAG Node            | 문서 검색과 RAG 답변 생성              |
| Tool Node           | Tool 실행, 인자 검증, 권한 확인        |
| SQL Agent Node      | DB, SQL, QueryDSL 작업                 |
| Backend Agent Node  | Backend 작업 수행                      |
| Frontend Agent Node | Frontend 작업 수행                     |
| DevOps Agent Node   | Docker, 배포, 운영 작업                |
| AI Agent Node       | RAG, Agent, LangGraph 작업             |
| Review Node         | 결과 검토                              |
| Fix Node            | Review Findings 반영                   |
| Final Node          | 사용자용 최종 응답 생성                |
| Error Node          | 오류 처리                              |

Node 함수 예시:

```python
def pm_node(state: DevTeamState) -> dict:
    return {
        "task_type": "backend",
        "requirements": [
            "JWT 인증 흐름 설명",
            "Controller-Service-Repository 책임 분리"
        ],
        "required_agents": ["backend", "review"],
        "metadata_filter": {
            "domain": "Backend",
            "topics": ["Spring Security", "JWT"]
        },
        "current_step": "pm_done"
    }
```

Node 설계 기준:

- Node 하나는 하나의 책임만 담당한다.
- 입력으로 필요한 State 필드를 명확히 한다.
- 출력으로 업데이트할 State 필드를 명확히 한다.
- 실패 시 error_type과 error를 업데이트한다.
- Side Effect가 있는 Node는 승인 또는 검증을 거친다.
- Node Output은 다음 Node Input과 호환되어야 한다.
- 긴 결과는 요약하거나 구조화해 State에 저장한다.

---

### [FAQ]

Q. LangGraph Node가 뭐야?

A.
State를 입력받아 하나의 작업을 수행하고 State Update를 반환하는 작업 단위다.

Q. Agent 하나를 Node로 만들 수 있어?

A.
가능하다. PM Agent, Backend Agent, Review Agent를 각각 Node로 구성할 수 있다.

Q. RAG Chain도 Node로 만들 수 있어?

A.
가능하다. RAG Node 내부에서 LangChain Retriever, Prompt, Model, Parser를 실행할 수 있다.

Q. Tool 실행도 Node로 만들 수 있어?

A.
가능하다. Tool Node를 별도로 두면 인자 검증과 권한 확인을 중앙화할 수 있다.

Q. Node 책임은 크게 만들어도 돼?

A.
권장하지 않는다. Node 책임이 커질수록 디버깅과 재사용이 어려워진다.

---

# 4. Node Input Output Contract

## 4.1 Node 입출력 계약

### [개념]

Node Input Output Contract는 각 Node가 어떤 State 필드를 읽고 어떤 State 필드를 업데이트하는지 정의하는 규칙이다.

입출력 계약이 없으면 Node 간 데이터 흐름이 불명확해지고 Routing 오류가 발생한다.

기본 구조:

```text
Node
├ Reads: State fields
├ Writes: State fields
├ Errors: error fields
└ Next: routing fields
```

Node Contract는 Node Test와 Graph Test의 기준이 된다.

---

### [핵심]

- Node별 Read Fields를 정의한다.
- Node별 Write Fields를 정의한다.
- Node별 Error Fields를 정의한다.
- Node별 Routing 관련 필드를 정의한다.
- Node가 담당하지 않는 필드는 수정하지 않는다.
- Node Output은 다음 Node Input과 호환되어야 한다.
- 구조화된 Output을 사용하면 Review와 Routing이 쉬워진다.
- Node 입출력 계약은 테스트 기준이 된다.

---

### [실무]

Node Contract 예시:

| Node          | Reads                                              | Writes                                                    |
| ------------- | -------------------------------------------------- | --------------------------------------------------------- |
| PM Node       | user_request                                       | task_type, requirements, required_agents, metadata_filter |
| RAG Node      | user_request, task_type, metadata_filter           | retrieved_context, sources, missing_context               |
| SQL Node      | requirements, retrieved_context                    | agent_outputs.sql                                         |
| Backend Node  | requirements, retrieved_context, agent_outputs.sql | agent_outputs.backend                                     |
| Frontend Node | requirements, agent_outputs.backend                | agent_outputs.frontend                                    |
| Review Node   | requirements, agent_outputs, retrieved_context     | review_result, review_findings                            |
| Fix Node      | review_findings, agent_outputs, fix_count          | agent_outputs.fixed, fix_count                            |
| Final Node    | agent_outputs, review_result, review_findings      | final_output, status                                      |

Node Error Contract:

| 오류            | 기록 필드                            |
| --------------- | ------------------------------------ |
| 입력 누락       | error_type = "invalid_state"         |
| 검색 실패       | error_type = "retrieval_error"       |
| Tool 실패       | error_type = "tool_error"            |
| Parser 실패     | error_type = "parser_error"          |
| 권한 부족       | error_type = "permission_denied"     |
| 승인 필요       | status = "waiting_approval"          |
| 반복 한도 도달  | error_type = "max_iteration_reached" |
| 알 수 없는 오류 | error_type = "unknown_error"         |

Node Contract 문서화 예시:

```text
Node: Review Node

Reads:
- requirements
- agent_outputs
- retrieved_context
- approval_scope

Writes:
- review_result
- review_findings
- status

Errors:
- error
- error_type

Routing:
- review_result
- severity
```

---

### [FAQ]

Q. Node Input Output Contract가 뭐야?

A.
각 Node가 읽는 State 필드와 업데이트하는 State 필드를 정의하는 규칙이다.

Q. Node Contract는 왜 필요해?

A.
Node 간 데이터 흐름을 명확히 하고 State 충돌과 Routing 오류를 줄이기 위해 필요하다.

Q. Node가 담당하지 않는 State 필드를 수정해도 돼?

A.
권장하지 않는다. 다른 Node 결과를 덮어쓰면 Workflow가 불안정해질 수 있다.

Q. Node Output은 무엇과 맞아야 해?

A.
다음 Node가 읽는 State 필드와 Router가 판단하는 조건에 맞아야 한다.

Q. Node Contract는 테스트에 도움이 돼?

A.
도움이 된다. 입력 State와 예상 State Update를 기준으로 Node Test를 만들 수 있다.

---

# 5. Edge Core

## 5.1 Edge 기본 개념

### [개념]

Edge는 LangGraph에서 Node 간 실행 흐름을 연결하는 구조다.

Edge는 어떤 Node 다음에 어떤 Node를 실행할지 정의한다.

기본 Flow:

```text
START
→ Node A
→ Node B
→ END
```

Edge는 Normal Edge와 Conditional Edge로 나눌 수 있다.

Edge 설계에는 반드시 종료 경로와 오류 경로가 필요하다.

---

### [핵심]

- Edge는 Node 간 실행 순서를 정의한다.
- START는 Workflow 시작 지점이다.
- END는 Workflow 종료 지점이다.
- Normal Edge는 항상 같은 다음 Node로 이동한다.
- Conditional Edge는 State 값에 따라 다음 Node를 선택한다.
- Loop는 Edge를 통해 구성할 수 있다.
- Error Path도 Edge로 연결해야 한다.
- 모든 Workflow에는 종료 조건이 필요하다.

---

### [실무]

Normal Edge 예시:

```text
START
→ PM Node
→ Backend Node
→ Review Node
→ Final Node
→ END
```

Conditional Edge 예시:

```text
PM Node
→ if task_type == "backend": Backend Node
→ if task_type == "frontend": Frontend Node
→ if task_type == "ai": AI Node
→ else: Clarification Node
```

Review / Fix Loop Edge 예시:

```text
Review Node
→ if review_result == "pass": Final Node
→ if review_result == "fail" and fix_count < max_fix_count: Fix Node
→ if fix_count >= max_fix_count: Final With Warning
```

Error Edge 예시:

```text
Any Node
→ if status == "error": Error Node
→ if error_type == "parser_error": Retry Node
→ if error_type == "permission_denied": Approval Node
```

Edge 설계 기준:

- 모든 Node는 다음 이동 경로가 있어야 한다.
- 실패 상태를 처리하는 Edge가 필요하다.
- Conditional Edge에는 fallback이 필요하다.
- Loop에는 Max Iteration이 필요하다.
- END에 도달하는 경로가 반드시 있어야 한다.
- 승인 대기 상태는 Approval Node 또는 Interrupt로 연결한다.

---

### [FAQ]

Q. LangGraph Edge가 뭐야?

A.
Node 다음에 어떤 Node를 실행할지 연결하는 Workflow 흐름이다.

Q. Normal Edge는 뭐야?

A.
항상 정해진 다음 Node로 이동하는 단순 연결이다.

Q. Conditional Edge는 뭐야?

A.
State 값에 따라 다음 Node를 다르게 선택하는 조건부 연결이다.

Q. Loop도 Edge로 만들 수 있어?

A.
가능하다. Review Node에서 Fix Node로 갔다가 다시 Review Node로 돌아오는 구조를 만들 수 있다.

Q. Edge 설계에서 가장 중요한 것은?

A.
fallback, error path, stop condition, END 도달 경로를 반드시 두는 것이다.

---

# 6. Conditional Routing

## 6.1 조건 기반 라우팅

### [개념]

Conditional Routing은 State 값을 기준으로 다음 Node를 선택하는 방식이다.

PM Agent나 Router Node가 task_type, status, review_result, approval_required, error_type 같은 값을 State에 저장하면 Conditional Edge가 이를 기준으로 다음 Node를 선택한다.

기본 Flow:

```text
State
→ Router Function
→ Condition Check
→ Next Node
```

Conditional Routing은 Multi-Agent Workflow의 핵심이다.

---

### [핵심]

- Conditional Routing은 State 기반 분기다.
- task_type은 Domain Agent 선택에 사용된다.
- status는 성공, 실패, 승인 대기 분기에 사용된다.
- review_result는 Final 또는 Fix 분기에 사용된다.
- approval_required는 Human Approval 분기에 사용된다.
- missing_context는 RAG 검색 실패 처리에 사용된다.
- error_type은 Error Node 선택에 사용된다.
- fallback 경로가 반드시 필요하다.
- 조건이 모호하면 잘못된 Agent로 라우팅될 수 있다.

---

### [실무]

Router Function 예시:

```python
def route_by_task_type(state: DevTeamState) -> str:
    task_type = state.get("task_type", "unknown")

    if task_type == "sql":
        return "sql_node"
    if task_type == "backend":
        return "backend_node"
    if task_type == "frontend":
        return "frontend_node"
    if task_type == "ai":
        return "ai_node"
    if task_type == "devops":
        return "devops_node"
    if task_type == "mixed":
        return "multi_domain_node"

    return "clarification_node"
```

Review Router 예시:

```python
def route_after_review(state: DevTeamState) -> str:
    if state["review_result"] == "pass":
        return "final_node"

    if state["review_result"] == "fail" and state["fix_count"] < state["max_fix_count"]:
        return "fix_node"

    return "final_with_warning_node"
```

Approval Router 예시:

```python
def route_by_approval(state: DevTeamState) -> str:
    if state.get("approval_required") is True:
        return "approval_node"

    return "next_domain_node"
```

Conditional Routing 기준:

| State Field       | 분기 목적                        |
| ----------------- | -------------------------------- |
| task_type         | Domain Agent 선택                |
| required_agents   | 실행 Agent 목록                  |
| status            | running, error, waiting_approval |
| review_result     | pass, fail, warning              |
| approval_required | Human Approval 필요 여부         |
| missing_context   | RAG 검색 실패 처리               |
| error_type        | Error Node 선택                  |
| fix_count         | Review / Fix Loop 제어           |
| tool_call_count   | Tool Loop 제어                   |

---

### [FAQ]

Q. Conditional Routing이 뭐야?

A.
State 값에 따라 다음 Node를 선택하는 조건 기반 라우팅 방식이다.

Q. task_type은 어디에 써?

A.
sql, backend, frontend, ai, devops 같은 Domain Agent를 선택하는 데 사용한다.

Q. review_result는 어디에 써?

A.
Review 통과 시 Final Node로 보내고 실패 시 Fix Node로 보내는 분기에 사용한다.

Q. approval_required는 어디에 써?

A.
파일 수정, DB 변경, 배포 같은 위험 작업을 Approval Node로 보내는 데 사용한다.

Q. fallback이 왜 필요해?

A.
예상하지 못한 State 값이나 모호한 요청이 들어왔을 때 Workflow 중단을 막기 위해 필요하다.

---

# 7. PM Router Pattern

## 7.1 PM Node 기반 라우팅

### [개념]

PM Router Pattern은 PM Node가 사용자 요청을 분석하고 작업 유형, 요구사항, 필요한 Agent, Metadata Filter, 승인 필요 여부를 State에 기록한 뒤 다음 Node로 라우팅하는 구조다.

기본 Flow:

```text
User Request
→ PM Node
→ Task Decomposition
→ Routing State
→ Conditional Edge
→ Domain Agent Node
```

PM Node는 Multi-Agent Workflow의 입구 역할을 한다.

PM Node는 모든 요청을 모든 Agent에게 보내지 않고 필요한 Agent만 선택한다.

---

### [핵심]

- PM Node는 사용자 요청을 분석한다.
- PM Node는 작업을 분해한다.
- PM Node는 task_type을 결정한다.
- PM Node는 required_agents를 결정한다.
- PM Node는 requirements를 State에 저장한다.
- PM Node는 metadata_filter를 생성할 수 있다.
- PM Node는 Human Approval 필요 여부를 판단한다.
- PM Node는 모든 요청을 모든 Agent에게 보내지 않는다.
- PM Node 결과는 Conditional Routing의 기준이 된다.

---

### [실무]

PM Node Output Schema:

```json
{
  "task_type": "backend",
  "required_agents": ["backend", "review"],
  "requirements": [
    "JWT 인증 흐름 설명",
    "Controller-Service-Repository 책임 분리",
    "예외 처리 기준 포함"
  ],
  "metadata_filter": {
    "domain": "Backend",
    "topics": ["Spring Security", "JWT", "API Design"]
  },
  "approval_required": false
}
```

PM Routing Matrix:

| 사용자 요청      | task_type | required_agents                |
| ---------------- | --------- | ------------------------------ |
| SQL 쿼리 작성    | sql       | sql, review                    |
| Spring API 구현  | backend   | backend, review                |
| React 화면 구현  | frontend  | frontend, review               |
| Docker 배포 구성 | devops    | devops, review                 |
| RAG Agent 설계   | ai        | ai, review                     |
| 풀스택 기능 구현 | mixed     | sql, backend, frontend, review |
| 위험 작업 포함   | any       | approval, domain, review       |

PM Node 금지:

- 요청 분석 없이 모든 Agent 실행
- task_type을 자유 문자열로 방치
- 요구사항 추출 없이 Domain Agent 호출
- 승인 필요 작업을 바로 실행
- 검색 범위 없이 전체 RAG 문서 검색
- Review Agent 생략
- 사용자 요청에 없는 요구사항 추가

---

### [FAQ]

Q. PM Router Pattern이 뭐야?

A.
PM Node가 사용자 요청을 분석해 task_type, requirements, required_agents를 정하고 다음 Agent로 라우팅하는 구조다.

Q. PM Node는 왜 필요해?

A.
모든 요청을 모든 Agent에게 보내지 않고 필요한 Agent만 선택하기 위해 필요하다.

Q. PM Node는 무엇을 State에 저장해?

A.
task_type, required_agents, requirements, metadata_filter, approval_required 같은 값을 저장한다.

Q. PM Node가 Human Approval도 판단해?

A.
가능하다. 파일 삭제, DB 변경, 배포 같은 위험 작업이 포함되면 approval_required를 true로 설정한다.

Q. PM Node 없이 Multi-Agent를 만들어도 돼?

A.
가능하지만 요청 분해와 라우팅 기준이 약해져 Agent 충돌과 불필요한 실행이 증가할 수 있다.

---

# 8. Multi-Agent Routing

## 8.1 Domain Agent 라우팅

### [개념]

Multi-Agent Routing은 사용자 요청을 필요한 Domain Agent에게만 전달하는 구조다.

Domain Agent는 SQL, Backend, Frontend, DevOps, AI, Review처럼 역할별로 분리된다.

기본 Flow:

```text
PM Node
→ task_type 판단
→ Domain Agent Node
→ Review Node
→ Final Node
```

복합 요청은 여러 Domain Agent를 순차 실행할 수 있다.

로컬 LLM 환경에서는 병렬 실행보다 순차 실행이 안정적이다.

---

### [핵심]

- Multi-Agent Routing은 필요한 Agent만 실행한다.
- Domain Agent는 책임 범위가 명확해야 한다.
- PM Node가 작업 순서를 결정할 수 있다.
- 복합 작업은 순차 실행이 안정적이다.
- Domain Agent 결과는 agent_outputs에 저장한다.
- completed_agents로 진행 상태를 추적할 수 있다.
- Review Agent가 전체 결과를 검토한다.
- Cross-domain Consistency를 확인해야 한다.

---

### [실무]

Domain Agent 실행 순서 예시:

```text
Full-stack Feature Request
→ PM Node
→ SQL Node
→ Backend Node
→ Frontend Node
→ Review Node
→ Fix Node if needed
→ Final Node
```

Agent별 책임:

| Agent          | 책임                                |
| -------------- | ----------------------------------- |
| SQL Agent      | DB 설계, SQL, QueryDSL              |
| Backend Agent  | API, Service, Entity, Security      |
| Frontend Agent | React, Component, API 연동          |
| DevOps Agent   | Docker, 배포, 서버 운영             |
| AI Agent       | RAG, Agent, LangGraph, Tool Calling |
| Review Agent   | 품질 검증, 누락 확인                |
| Fix Agent      | Review 결과 반영                    |
| Final Agent    | 사용자용 결과 정리                  |

Multi-Agent Routing State 예시:

```json
{
  "task_type": "mixed",
  "required_agents": ["sql", "backend", "frontend", "review"],
  "current_agent": "backend",
  "completed_agents": ["sql"],
  "agent_outputs": {
    "sql": "SQL 설계 결과",
    "backend": ""
  }
}
```

로컬 LLM 환경 기준:

- 병렬 실행보다 순차 실행을 우선한다.
- Agent별 Context를 분리한다.
- 필요한 RAG Domain만 검색한다.
- 각 Agent 결과를 요약해 다음 Agent에 전달한다.
- Review Node에서 전체 일관성을 검토한다.
- 대형 작업은 기능 단위로 쪼갠다.

---

### [FAQ]

Q. Multi-Agent Routing이 뭐야?

A.
사용자 요청을 필요한 Domain Agent에게만 전달하고 순서대로 실행하는 구조다.

Q. 모든 요청을 모든 Agent에게 보내면 안 돼?

A.
권장하지 않는다. 비용과 시간이 늘고 Agent 결과가 충돌할 수 있다.

Q. 복합 작업은 어떻게 처리해?

A.
PM Node가 작업을 분해하고 SQL, Backend, Frontend, Review 순서처럼 필요한 Agent를 순차 실행한다.

Q. 로컬 LLM 환경에서는 병렬 실행이 좋아?

A.
대부분은 순차 실행이 더 현실적이다. RAM, 모델 응답 속도, Context 관리 제약을 고려해야 한다.

Q. Cross-domain Consistency는 누가 확인해?

A.
Review Agent가 SQL, Backend, Frontend 결과가 서로 일관되는지 검토한다.

---

# 9. Error Routing

## 9.1 오류 상태 기반 라우팅

### [개념]

Error Routing은 Node 실행 중 오류가 발생했을 때 State의 error_type과 status를 기준으로 다음 Node를 선택하는 구조다.

오류를 숨기지 않고 State에 기록해야 복구, 재시도, 사용자 보고가 가능하다.

기본 Flow:

```text
Node Error
→ State.error_type 기록
→ Error Router
→ Retry Node or Fallback Node or Final Error
```

Error Routing은 긴 Agent Workflow의 안정성을 높인다.

---

### [핵심]

- Node 실패는 State에 기록한다.
- error_type을 기준으로 복구 방법을 선택한다.
- 재시도 가능한 오류와 불가능한 오류를 구분한다.
- Parser Error는 재시도 가능할 수 있다.
- Permission Error는 Human Approval로 이동할 수 있다.
- Retrieval Error는 Fallback 답변으로 처리할 수 있다.
- Missing Context는 기술적 오류가 아니라 근거 부족 상태일 수 있다.
- 알 수 없는 오류는 Final Error로 보고한다.

---

### [실무]

Error Type 기준:

| error_type            | 원인                 | 라우팅                  |
| --------------------- | -------------------- | ----------------------- |
| invalid_state         | 필수 State 필드 누락 | Error Node              |
| retrieval_error       | 문서 검색 실패       | Fallback RAG Node       |
| missing_context       | 근거 문서 없음       | Final Missing Context   |
| parser_error          | JSON 파싱 실패       | Retry Node              |
| tool_error            | Tool 실행 실패       | Retry or Error Node     |
| permission_denied     | 권한 부족            | Human Approval or Error |
| timeout               | 응답 지연            | Retry Node              |
| max_iteration_reached | 반복 한도 도달       | Final With Warning      |
| unknown_error         | 알 수 없는 오류      | Final Error             |

Error Router 예시:

```python
def route_on_error(state: DevTeamState) -> str:
    error_type = state.get("error_type")

    if error_type == "parser_error":
        return "retry_node"
    if error_type == "permission_denied":
        return "approval_node"
    if error_type == "missing_context":
        return "final_missing_context_node"
    if error_type == "max_iteration_reached":
        return "final_with_warning_node"

    return "final_error_node"
```

오류 처리 금지:

- 예외를 숨기고 성공처럼 전달
- Tool 실패를 무시하고 Final 생성
- 무제한 Retry
- 오류 원인 없이 사용자에게 실패만 보고
- 위험 작업 권한 오류를 우회 실행
- 오래된 State로 재시도

---

### [FAQ]

Q. Error Routing이 뭐야?

A.
오류 발생 시 State의 error_type과 status를 기준으로 Retry, Fallback, Error Node로 분기하는 구조다.

Q. 오류는 왜 State에 기록해야 해?

A.
다음 Node가 오류 원인을 알고 복구하거나 사용자에게 정확히 보고할 수 있기 때문이다.

Q. Parser Error는 어떻게 라우팅해?

A.
재시도 가능한 경우 Retry Node로 보내고 반복 실패 시 Error Node로 이동한다.

Q. missing_context는 오류야?

A.
기술적 오류는 아니지만 답변 근거가 부족한 상태이므로 Final Missing Context로 처리할 수 있다.

Q. 무제한 Retry가 위험한 이유는?

A.
비용, 시간, 무한 루프 문제가 발생하고 원인 분석이 어려워지기 때문이다.

---

# 10. Loop Control

## 10.1 반복과 종료 조건

### [개념]

Loop Control은 Review / Fix Loop, Tool Calling Loop, Retry Loop 같은 반복 구조가 무한히 실행되지 않도록 제어하는 기준이다.

LangGraph는 Loop를 만들 수 있지만 모든 Loop에는 종료 조건이 필요하다.

기본 Flow:

```text
Loop Node
→ Condition Check
→ Continue or Stop
```

Loop Control이 없으면 Agent Workflow는 무한 반복될 수 있다.

---

### [핵심]

- 모든 Loop에는 Stop Condition이 필요하다.
- Review / Fix Loop에는 max_fix_count가 필요하다.
- Tool Calling Loop에는 max_tool_calls가 필요하다.
- Retry Loop에는 max_retry_count가 필요하다.
- 반복 횟수는 State에 저장한다.
- Max Count 도달 시 Final With Warning으로 종료할 수 있다.
- Loop 조건은 명확하고 테스트 가능해야 한다.
- Loop는 반드시 END 또는 Final 계열 Node로 빠지는 경로가 있어야 한다.

---

### [실무]

Review / Fix Loop:

```text
Review Node
→ if pass: Final Node
→ if fail and fix_count < max_fix_count: Fix Node
→ if fix_count >= max_fix_count: Final With Warning
```

Tool Calling Loop:

```text
Agent Node
→ if tool_needed and tool_call_count < max_tool_calls: Tool Node
→ if final_ready: Review Node
→ if max_tool_calls reached: Final With Warning
```

Retry Loop:

```text
Parser Error
→ if retry_count < max_retry_count: Retry Node
→ else: Error Node
```

Loop State 예시:

```python
class LoopState(TypedDict):
    fix_count: int
    max_fix_count: int
    tool_call_count: int
    max_tool_calls: int
    retry_count: int
    max_retry_count: int
    status: str
```

Loop 설계 금지:

- 종료 조건 없는 반복
- Review 기준이 매번 바뀌는 구조
- 반복 횟수를 State에 저장하지 않음
- 실패해도 계속 같은 Node를 재실행
- Max Count 도달 후 사용자에게 보고하지 않음
- Final / Error / Warning 경로 없이 Loop 구성

---

### [FAQ]

Q. Loop Control이 뭐야?

A.
반복 구조가 무한히 실행되지 않도록 종료 조건과 반복 횟수를 관리하는 기준이다.

Q. Review / Fix Loop에는 무엇이 필요해?

A.
review_result, fix_count, max_fix_count, Final With Warning 경로가 필요하다.

Q. Tool Calling Loop에는 무엇이 필요해?

A.
tool_call_count, max_tool_calls, final_ready 조건이 필요하다.

Q. Retry Loop에는 무엇이 필요해?

A.
retry_count, max_retry_count, retryable 여부가 필요하다.

Q. Max Count에 도달하면 어떻게 해?

A.
Final With Warning 또는 Error Node로 이동하고 현재 상태와 남은 문제를 사용자에게 보고한다.

---

# 11. Graph Assembly

## 11.1 Graph 구성 패턴

### [개념]

Graph Assembly는 State Schema, Node, Edge, Conditional Routing을 조합해 실행 가능한 LangGraph Workflow를 만드는 단계다.

Graph는 Node만 나열한다고 완성되지 않는다.

State Schema, Node Contract, Edge, Router, Error Path, Stop Condition이 함께 필요하다.

기본 Flow:

```text
Define State
→ Define Nodes
→ Define Edges
→ Define Conditional Routing
→ Add Error Path
→ Add Stop Condition
→ Compile Graph
→ Graph Test
```

Graph Assembly는 Part08의 Debugging과 Graph Testing 기준으로 검증한다.

---

### [핵심]

- Graph 구성 전 State Schema를 정의한다.
- Node별 책임과 입출력 계약을 정의한다.
- Normal Edge로 기본 흐름을 연결한다.
- Conditional Edge로 분기와 Loop를 구성한다.
- Error Routing을 포함한다.
- Approval Routing을 포함한다.
- END에 도달하는 경로를 확인한다.
- Graph Test로 State 전이를 검증한다.
- Node 내부에는 LangChain Runnable 또는 RAG Chain을 넣을 수 있다.

---

### [실무]

개인 AI 개발팀 기본 Graph:

```text
START
→ PM Node
→ Router
→ Domain Agent Node
→ Review Node
→ if pass: Final Node
→ if fail: Fix Node
→ Review Node
→ END
```

AI Agent 개발용 Graph:

```text
START
→ PM Node
→ AI RAG Node
→ AI Agent Node
→ Review Node
→ Fix Node if needed
→ Final Node
→ END
```

Full-stack 기능 개발 Graph:

```text
START
→ PM Node
→ SQL Node
→ Backend Node
→ Frontend Node
→ Review Node
→ Fix Node if needed
→ Final Node
→ END
```

Approval 포함 Graph:

```text
START
→ PM Node
→ Domain Agent Node
→ if approval_required: Approval Node
→ Tool Node
→ Review Node
→ Final Node
→ END
```

Graph Assembly Checklist:

| 구성 요소        | 확인                |
| ---------------- | ------------------- |
| State Schema     | 필드와 타입 정의    |
| Node             | 책임 분리           |
| Node Contract    | Reads / Writes 정의 |
| Edge             | 기본 흐름 연결      |
| Conditional Edge | 분기 조건 정의      |
| Fallback         | 모호한 상태 처리    |
| Error Path       | 오류 처리           |
| Approval Path    | 위험 작업 승인 처리 |
| Loop Control     | 반복 제한           |
| Final Node       | 사용자 응답 정리    |
| END              | 종료 경로 존재      |

---

### [FAQ]

Q. Graph Assembly가 뭐야?

A.
State Schema, Node, Edge, Router, Error Path를 조합해 실행 가능한 LangGraph Workflow를 만드는 단계다.

Q. Node만 만들면 Graph가 완성돼?

A.
아니다. Edge, Conditional Routing, Error Path, Stop Condition, END 경로가 필요하다.

Q. Graph 구성 전 무엇을 먼저 해야 해?

A.
State Schema와 Node별 입출력 계약을 먼저 정의하는 것이 좋다.

Q. Graph Test는 왜 필요해?

A.
State가 예상대로 업데이트되고 올바른 Node로 라우팅되는지 확인하기 위해 필요하다.

Q. 개인 AI 개발팀 기본 Graph는 어떻게 구성해?

A.
PM Node, Domain Agent Node, Review Node, Fix Node, Final Node 중심으로 구성한다.

---

# 12. Part06 Checklist

## 12.1 State Node Edge Routing Checklist

### [Checklist]

- [ ] State, Memory, Checkpoint를 구분했는가?
- [ ] State Schema가 정의되어 있는가?
- [ ] State 필드 타입이 명확한가?
- [ ] Routing 필드가 enum 또는 제한된 값인가?
- [ ] status, error_type, error 필드가 있는가?
- [ ] 반복 제어용 count 필드가 있는가?
- [ ] 승인 제어용 approval_required, approval_scope 필드가 있는가?
- [ ] Node 책임이 하나의 작업 단위로 분리되었는가?
- [ ] Node별 Reads / Writes가 정의되어 있는가?
- [ ] Node가 담당하지 않는 State 필드를 수정하지 않는가?
- [ ] Node 실패 시 error_type과 error를 업데이트하는가?
- [ ] Normal Edge와 Conditional Edge가 구분되는가?
- [ ] Conditional Edge에 fallback이 있는가?
- [ ] PM Node가 task_type과 required_agents를 생성하는가?
- [ ] PM Node가 metadata_filter를 생성하는가?
- [ ] 모든 요청을 모든 Agent에게 보내지 않는가?
- [ ] Multi-Agent 실행 순서가 명확한가?
- [ ] Error Routing이 정의되어 있는가?
- [ ] Retry 가능 오류와 불가능 오류를 구분하는가?
- [ ] Review / Fix Loop에 max_fix_count가 있는가?
- [ ] Tool Calling Loop에 max_tool_calls가 있는가?
- [ ] 모든 Loop에 Stop Condition이 있는가?
- [ ] Approval Path가 정의되어 있는가?
- [ ] END에 도달하는 경로가 존재하는가?
- [ ] Graph Test로 State 전이를 검증하는가?
- [ ] Part08 Debugging / Testing 기준과 연결되는가?

---

# Retrieval Queries

### [FAQ]

Q. LangGraph State가 뭐야?
A. LangGraph Workflow에서 Node들이 읽고 업데이트하는 공유 실행 상태 데이터다.

Q. State Schema는 왜 필요해?
A. Node 간 입력과 출력 형식을 안정화하고 Workflow 오류를 줄이기 위해 필요하다.

Q. State와 Memory는 달라?
A. 다르다. State는 현재 Workflow 상태이고 Memory는 과거 정보를 재사용하기 위한 구조다.

Q. State와 Checkpoint는 달라?
A. 다르다. State는 현재 실행 상태이고 Checkpoint는 그 State Snapshot을 저장해 재개에 사용하는 구조다.

Q. State가 너무 커지면 왜 문제야?
A. Context가 길어지고 Node 실행 품질, 응답 속도, 디버깅 가능성이 낮아질 수 있다.

Q. State Schema는 언제 정의해야 해?
A. Node와 Edge를 만들기 전에 먼저 정의하는 것이 좋다.

Q. Routing 필드는 어떻게 설계해?
A. task_type, status, review_result처럼 제한된 enum 값으로 설계하는 것이 안정적이다.

Q. 반복 루프에는 어떤 State가 필요해?
A. fix_count, max_fix_count, review_result, status 같은 필드가 필요하다.

Q. State Schema 변경 시 무엇을 주의해야 해?
A. 기존 Checkpoint와 호환되지 않을 수 있으므로 version 또는 migration 기준이 필요하다.

Q. LangGraph Node가 뭐야?
A. State를 입력받아 하나의 작업을 수행하고 State Update를 반환하는 작업 단위다.

Q. Agent 하나를 Node로 만들 수 있어?
A. 가능하다. PM Agent, Backend Agent, Review Agent를 각각 Node로 구성할 수 있다.

Q. RAG Chain도 Node로 만들 수 있어?
A. 가능하다. RAG Node 내부에서 LangChain Retriever, Prompt, Model, Parser를 실행할 수 있다.

Q. Tool 실행도 Node로 만들 수 있어?
A. 가능하다. Tool Node를 별도로 두면 인자 검증과 권한 확인을 중앙화할 수 있다.

Q. Node 책임은 크게 만들어도 돼?
A. 권장하지 않는다. Node 책임이 커질수록 디버깅과 재사용이 어려워진다.

Q. Node Input Output Contract가 뭐야?
A. 각 Node가 읽는 State 필드와 업데이트하는 State 필드를 정의하는 규칙이다.

Q. Node Contract는 왜 필요해?
A. Node 간 데이터 흐름을 명확히 하고 State 충돌과 Routing 오류를 줄이기 위해 필요하다.

Q. Node가 담당하지 않는 State 필드를 수정해도 돼?
A. 권장하지 않는다. 다른 Node 결과를 덮어쓰면 Workflow가 불안정해질 수 있다.

Q. LangGraph Edge가 뭐야?
A. Node 다음에 어떤 Node를 실행할지 연결하는 Workflow 흐름이다.

Q. Normal Edge는 뭐야?
A. 항상 정해진 다음 Node로 이동하는 단순 연결이다.

Q. Conditional Edge는 뭐야?
A. State 값에 따라 다음 Node를 다르게 선택하는 조건부 연결이다.

Q. Loop도 Edge로 만들 수 있어?
A. 가능하다. Review Node에서 Fix Node로 갔다가 다시 Review Node로 돌아오는 구조를 만들 수 있다.

Q. Edge 설계에서 가장 중요한 것은?
A. fallback, error path, stop condition, END 도달 경로를 반드시 두는 것이다.

Q. Conditional Routing이 뭐야?
A. State 값에 따라 다음 Node를 선택하는 조건 기반 라우팅 방식이다.

Q. task_type은 어디에 써?
A. sql, backend, frontend, ai, devops 같은 Domain Agent를 선택하는 데 사용한다.

Q. review_result는 어디에 써?
A. Review 통과 시 Final Node로 보내고 실패 시 Fix Node로 보내는 분기에 사용한다.

Q. approval_required는 어디에 써?
A. 파일 수정, DB 변경, 배포 같은 위험 작업을 Approval Node로 보내는 데 사용한다.

Q. fallback이 왜 필요해?
A. 예상하지 못한 State 값이나 모호한 요청이 들어왔을 때 Workflow 중단을 막기 위해 필요하다.

Q. PM Router Pattern이 뭐야?
A. PM Node가 사용자 요청을 분석해 task_type, requirements, required_agents를 정하고 다음 Agent로 라우팅하는 구조다.

Q. PM Node는 왜 필요해?
A. 모든 요청을 모든 Agent에게 보내지 않고 필요한 Agent만 선택하기 위해 필요하다.

Q. PM Node는 무엇을 State에 저장해?
A. task_type, required_agents, requirements, metadata_filter, approval_required 같은 값을 저장한다.

Q. PM Node가 Human Approval도 판단해?
A. 가능하다. 파일 삭제, DB 변경, 배포 같은 위험 작업이 포함되면 approval_required를 true로 설정한다.

Q. Multi-Agent Routing이 뭐야?
A. 사용자 요청을 필요한 Domain Agent에게만 전달하고 순서대로 실행하는 구조다.

Q. 모든 요청을 모든 Agent에게 보내면 안 돼?
A. 권장하지 않는다. 비용과 시간이 늘고 Agent 결과가 충돌할 수 있다.

Q. 복합 작업은 어떻게 처리해?
A. PM Node가 작업을 분해하고 SQL, Backend, Frontend, Review 순서처럼 필요한 Agent를 순차 실행한다.

Q. 로컬 LLM 환경에서는 병렬 실행이 좋아?
A. 대부분은 순차 실행이 더 현실적이다. RAM, 모델 응답 속도, Context 관리 제약을 고려해야 한다.

Q. Cross-domain Consistency는 누가 확인해?
A. Review Agent가 SQL, Backend, Frontend 결과가 서로 일관되는지 검토한다.

Q. Error Routing이 뭐야?
A. 오류 발생 시 State의 error_type과 status를 기준으로 Retry, Fallback, Error Node로 분기하는 구조다.

Q. 오류는 왜 State에 기록해야 해?
A. 다음 Node가 오류 원인을 알고 복구하거나 사용자에게 정확히 보고할 수 있기 때문이다.

Q. Parser Error는 어떻게 라우팅해?
A. 재시도 가능한 경우 Retry Node로 보내고 반복 실패 시 Error Node로 이동한다.

Q. missing_context는 오류야?
A. 기술적 오류는 아니지만 답변 근거가 부족한 상태이므로 Final Missing Context로 처리할 수 있다.

Q. Loop Control이 뭐야?
A. 반복 구조가 무한히 실행되지 않도록 종료 조건과 반복 횟수를 관리하는 기준이다.

Q. Review / Fix Loop에는 무엇이 필요해?
A. review_result, fix_count, max_fix_count, Final With Warning 경로가 필요하다.

Q. Tool Calling Loop에는 무엇이 필요해?
A. tool_call_count, max_tool_calls, final_ready 조건이 필요하다.

Q. Retry Loop에는 무엇이 필요해?
A. retry_count, max_retry_count, retryable 여부가 필요하다.

Q. Max Count에 도달하면 어떻게 해?
A. Final With Warning 또는 Error Node로 이동하고 현재 상태와 남은 문제를 사용자에게 보고한다.

Q. Graph Assembly가 뭐야?
A. State Schema, Node, Edge, Router, Error Path를 조합해 실행 가능한 LangGraph Workflow를 만드는 단계다.

Q. Node만 만들면 Graph가 완성돼?
A. 아니다. Edge, Conditional Routing, Error Path, Stop Condition, END 경로가 필요하다.

Q. Graph 구성 전 무엇을 먼저 해야 해?
A. State Schema와 Node별 입출력 계약을 먼저 정의하는 것이 좋다.

Q. Graph Test는 왜 필요해?
A. State가 예상대로 업데이트되고 올바른 Node로 라우팅되는지 확인하기 위해 필요하다.

Q. 개인 AI 개발팀 기본 Graph는 어떻게 구성해?
A. PM Node, Domain Agent Node, Review Node, Fix Node, Final Node 중심으로 구성한다.
