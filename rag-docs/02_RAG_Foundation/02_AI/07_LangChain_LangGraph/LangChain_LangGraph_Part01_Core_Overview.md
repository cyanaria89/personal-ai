# LangChain & LangGraph Part01 Core Overview

---

# 1. LLM Application Core

## 1.1 LLM Application 기본 구조

### [개념]

LLM Application은 LLM에게 질문을 보내고 답변만 받는 단순 Chatbot 구조가 아니다.

LLM Application은 Prompt, Chat Model, Output Parser, Retriever, Tool, State, Workflow를 조합해 사용자 요청을 처리하는 시스템이다.

기본 Pipeline:

```text
User Input
→ Prompt Template
→ Chat Model
→ Output Parser
→ Final Output
```

RAG Pipeline:

```text
User Query
→ Retriever
→ Retrieved Context
→ Prompt Template
→ Chat Model
→ Grounded Answer
```

Agent Workflow:

```text
User Task
→ Agent
→ Tool Selection
→ Tool Execution
→ Observation
→ Final Answer
```

LangChain과 LangGraph는 LLM Application을 구조화하기 위한 Framework다.

LangChain은 LLM 구성 요소를 연결하는 데 적합하고, LangGraph는 State 기반 Agent Workflow를 제어하는 데 적합하다.

---

### [핵심]

- LLM Application은 Prompt + Model + Parser + Retriever + Tool + Workflow 조합이다.
- 단순 LLM 호출은 Chat Model 중심으로 구성할 수 있다.
- 반복 가능한 Pipeline은 LangChain Runnable로 구성한다.
- 문서 기반 답변은 LangChain RAG Chain으로 구성한다.
- 조건 분기와 반복이 필요한 Agent Workflow는 LangGraph로 구성한다.
- Multi-Agent Workflow는 LangGraph의 State, Node, Edge 구조가 적합하다.
- LangGraph Node 내부에서 LangChain Runnable, Chain, RAG Chain, Tool Chain을 실행할 수 있다.

---

### [실무]

2026 실무 기준 LLM Application은 다음 기준으로 구분한다.

| 목적               | 적합한 구조                       |
| ------------------ | --------------------------------- |
| 단순 질문 답변     | Chat Model                        |
| 고정 순서 Pipeline | LangChain Runnable                |
| 문서 기반 답변     | LangChain RAG Chain               |
| JSON 출력 안정화   | Output Parser / Structured Output |
| 외부 기능 실행     | Tool Calling                      |
| 조건 분기          | LangGraph Conditional Edge        |
| 반복 검토          | LangGraph Review / Fix Loop       |
| 사용자 승인        | LangGraph Interrupt + Checkpoint  |
| Multi-Agent        | LangGraph StateGraph              |

개인 AI 개발팀에서는 사용자가 PM Agent에게 요청하고, PM Agent가 필요한 Domain Agent로 라우팅한다.

초기 구조:

```text
User
→ PM Agent
→ Backend Agent
→ Review Agent
→ Final Output
```

확장 구조:

```text
User
→ PM Agent
→ SQL Agent
→ Backend Agent
→ Frontend Agent
→ Review Agent
→ Fix Agent
→ Final Output
```

---

### [FAQ]

Q. LLM Application이 뭐야?

A.
Prompt, Model, Parser, Retriever, Tool, Workflow를 조합해 사용자 요청을 처리하는 시스템이다.

Q. LLM Application은 Chatbot이랑 같아?

A.
아니다. Chatbot은 단순 대화 중심이고 LLM Application은 RAG, Tool Calling, Agent Workflow까지 포함할 수 있다.

Q. LangChain과 LangGraph는 왜 필요해?

A.
LLM 호출만으로는 복잡한 RAG, Tool Calling, Multi-Agent Workflow를 안정적으로 관리하기 어렵기 때문이다.

Q. 단순 Pipeline은 무엇으로 구성해?

A.
LangChain Runnable과 Chain으로 구성하는 것이 적합하다.

Q. 복잡한 Agent Workflow는 무엇으로 구성해?

A.
LangGraph의 State, Node, Edge, Conditional Routing 구조로 구성하는 것이 적합하다.

---

# 2. LangChain Core

## 2.1 LangChain 기본 역할

### [개념]

LangChain은 LLM Application 구성 요소를 연결하기 위한 Framework다.

LangChain은 LLM 자체가 아니다.

LangChain은 Prompt Template, Chat Model, Output Parser, Retriever, Tool을 연결해 재사용 가능한 Pipeline을 만든다.

기본 Flow:

```text
Input
→ Prompt Template
→ Chat Model
→ Output Parser
→ Output
```

RAG Flow:

```text
Question
→ Retriever
→ Retrieved Documents
→ Prompt Template
→ Chat Model
→ Output Parser
→ Answer with Source
```

---

### [핵심]

- LangChain은 LLM 구성 요소 연결 Framework다.
- Prompt Template은 입력을 Prompt로 구조화한다.
- Chat Model은 Prompt를 받아 LLM 응답을 생성한다.
- Output Parser는 LLM 응답 형식을 안정화한다.
- Retriever는 관련 문서를 검색한다.
- Tool은 외부 기능 실행 인터페이스다.
- Runnable은 LangChain의 실행 가능한 구성 단위다.
- LangChain은 RAG Chain, Tool Chain, 간단한 Agent 구성에 적합하다.

---

### [실무]

LangChain 적용 대상:

| 작업              | LangChain 구성 요소             |
| ----------------- | ------------------------------- |
| Prompt 재사용     | Prompt Template                 |
| LLM 호출          | Chat Model                      |
| 문자열 답변       | String Output Parser            |
| JSON 답변         | JSON Parser / Structured Output |
| 문서 검색         | Retriever                       |
| 문서 기반 답변    | RAG Chain                       |
| 외부 기능 연결    | Tool                            |
| 순차 Pipeline     | RunnableSequence                |
| 간단한 Tool Agent | Tool Calling Agent              |

LangChain이 적합한 경우:

```text
요약
분류
문서 기반 답변
JSON 생성
단순 Tool 호출
고정 순서 Pipeline
```

LangChain만으로 부족한 경우:

```text
조건 분기
반복 루프
Review / Fix Loop
Human Approval
긴 Workflow 중단 / 재개
복수 Agent 라우팅
```

---

### [FAQ]

Q. LangChain이 뭐야?

A.
LLM, Prompt, Retriever, Tool, Output Parser를 연결해 LLM Application을 만들기 쉽게 해주는 Framework다.

Q. LangChain은 LLM이야?

A.
아니다. LangChain은 LLM 자체가 아니라 LLM과 주변 구성 요소를 연결하는 Framework다.

Q. LangChain으로 RAG를 만들 수 있어?

A.
가능하다. Retriever, Prompt Template, Chat Model, Output Parser를 연결해 RAG Chain을 구성할 수 있다.

Q. LangChain의 핵심 개념은 뭐야?

A.
Runnable, Prompt Template, Chat Model, Output Parser, Retriever, Tool이다.

Q. LangChain만으로 Multi-Agent Workflow를 만들면 안 돼?

A.
간단한 Agent는 가능하지만 조건 분기, 반복, 상태 관리가 복잡해지면 LangGraph가 더 적합하다.

---

# 3. LangGraph Core

## 3.1 LangGraph 기본 역할

### [개념]

LangGraph는 State 기반 Agent Workflow를 설계하기 위한 Framework다.

LangGraph는 작업을 Node로 나누고 Node 사이를 Edge로 연결한다.

State는 Node들이 공유하는 실행 상태 데이터다.

기본 Flow:

```text
State
→ Node Execution
→ State Update
→ Edge
→ Next Node
→ Final State
```

LangGraph는 단순 순차 Pipeline보다 조건 분기, 반복, 중단, 재개, Multi-Agent Workflow에 적합하다.

---

### [핵심]

- LangGraph는 State 기반 Workflow Framework다.
- State는 Node 간 공유되는 실행 상태다.
- Node는 하나의 작업 단위다.
- Edge는 다음 실행 단계를 연결한다.
- Conditional Edge는 State 값에 따라 다음 Node를 선택한다.
- Checkpoint는 중단과 재개를 지원한다.
- Human-in-the-loop는 사용자 승인과 선택을 Workflow에 포함한다.
- Review / Fix Loop는 LangGraph의 대표적 반복 패턴이다.
- Multi-Agent Workflow는 Agent를 Node로 표현해 구성할 수 있다.

---

### [실무]

LangGraph 적용 대상:

| 작업        | LangGraph 구성                 |
| ----------- | ------------------------------ |
| 요청 분석   | PM Node                        |
| 작업 분기   | Router Node / Conditional Edge |
| 문서 검색   | RAG Node                       |
| Tool 실행   | Tool Node                      |
| Domain 작업 | Domain Agent Node              |
| 결과 검토   | Review Node                    |
| 수정 반복   | Fix Node                       |
| 사용자 승인 | Approval Node / Interrupt      |
| 최종 정리   | Final Node                     |
| 오류 처리   | Error Node                     |

기본 Agent Graph:

```text
START
→ PM Node
→ Domain Agent Node
→ Review Node
→ Final Node
→ END
```

Review / Fix Graph:

```text
Draft Node
→ Review Node
→ if pass: Final Node
→ if fail and fix_count < max_fix_count: Fix Node
→ Review Node
→ END
```

Multi-Agent Graph:

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

---

### [FAQ]

Q. LangGraph가 뭐야?

A.
State, Node, Edge 기반으로 Agent Workflow와 Multi-Agent Workflow를 설계하는 Framework다.

Q. LangGraph는 Chain이야?

A.
아니다. LangGraph는 Graph 구조로 Workflow를 제어하는 Framework다.

Q. LangGraph에서 State는 뭐야?

A.
Node들이 읽고 업데이트하는 공유 실행 상태 데이터다.

Q. LangGraph에서 Node는 뭐야?

A.
하나의 작업 단위다. Agent, Tool 실행, Review, Fix 같은 작업을 Node로 표현할 수 있다.

Q. LangGraph에서 Edge는 뭐야?

A.
Node 다음에 어떤 Node를 실행할지 정의하는 연결이다.

Q. Conditional Edge는 왜 필요해?

A.
State 값에 따라 Backend Agent, Frontend Agent, Review Agent처럼 다음 단계를 다르게 선택하기 위해 필요하다.

---

# 4. LangChain vs LangGraph

## 4.1 역할 비교

### [개념]

LangChain과 LangGraph는 경쟁 관계가 아니라 역할이 다른 Framework다.

LangChain은 LLM 구성 요소 연결에 강하다.

LangGraph는 Agent Workflow 제어에 강하다.

LangGraph Node 내부에서 LangChain Runnable, RAG Chain, Tool Chain을 실행할 수 있다.

비교:

| 구분           | LangChain                         | LangGraph                                |
| -------------- | --------------------------------- | ---------------------------------------- |
| 핵심 목적      | LLM 구성 요소 연결                | State 기반 Workflow 제어                 |
| 구조           | Runnable / Chain                  | State / Node / Edge                      |
| 흐름           | 순차 Pipeline 중심                | 조건 분기 / 반복 / 중단 가능             |
| 상태 관리      | 상대적으로 단순                   | State 중심                               |
| 적합한 작업    | RAG Chain, 요약, 분류, Tool Chain | Multi-Agent, Review Loop, Human Approval |
| 중단 / 재개    | 제한적                            | Checkpoint 가능                          |
| 복잡한 Routing | 직접 구현 필요                    | Conditional Edge 적합                    |
| 사용 관계      | Node 내부 구성 요소               | 전체 Workflow 제어                       |

---

### [핵심]

- LangChain은 Prompt, Model, Parser, Retriever, Tool 연결에 적합하다.
- LangGraph는 State, Node, Edge 기반 Workflow 제어에 적합하다.
- 단순 RAG는 LangChain만으로 가능하다.
- Review / Fix Loop는 LangGraph가 적합하다.
- Human Approval이 필요하면 LangGraph가 적합하다.
- Multi-Agent Workflow는 LangGraph가 적합하다.
- LangGraph Node 내부에서 LangChain을 함께 사용할 수 있다.

---

### [실무]

선택 기준:

```text
단순 LLM 호출
→ Chat Model

Prompt + Model + Parser
→ LangChain Runnable

문서 기반 답변
→ LangChain RAG Chain

Tool 호출 Pipeline
→ LangChain Tool Chain

조건 분기 필요
→ LangGraph

반복 검토 필요
→ LangGraph Review / Fix Loop

사용자 승인 필요
→ LangGraph Human-in-the-loop

Multi-Agent 필요
→ LangGraph
```

조합 예시:

```text
PM Node
→ LangGraph Node

Backend RAG Search
→ LangChain Retriever

Backend Answer Generation
→ LangChain RAG Chain

Review / Fix 분기
→ LangGraph Conditional Edge

Checkpoint / Resume
→ LangGraph Checkpoint
```

---

### [FAQ]

Q. LangChain과 LangGraph 차이는?

A.
LangChain은 LLM 구성 요소를 연결하는 Runnable / Chain 중심이고, LangGraph는 State 기반 Workflow와 조건 분기, 반복에 강하다.

Q. LangGraph가 LangChain을 대체해?

A.
아니다. LangGraph는 Workflow 제어를 담당하고, Node 내부에서는 LangChain Runnable이나 Chain을 사용할 수 있다.

Q. 단순 RAG에도 LangGraph가 필요해?

A.
필수는 아니다. 단순 RAG는 LangChain만으로도 충분하다.

Q. Multi-Agent를 만들려면 LangGraph가 좋아?

A.
좋다. Agent를 Node로 구성하고 State와 Edge로 실행 흐름을 제어할 수 있기 때문이다.

Q. 처음부터 LangGraph로 가야 해?

A.
단순 Pipeline이나 RAG는 LangChain으로 시작하고 조건 분기, Review / Fix Loop, Multi-Agent가 필요할 때 LangGraph로 확장하는 것이 좋다.

---

# 5. Core Architecture Pattern

## 5.1 RAG Chain Pattern

### [개념]

RAG Chain은 Retriever와 LLM을 연결해 문서 기반 답변을 생성하는 구조다.

RAG Chain은 검색과 생성을 결합한다.

기본 Flow:

```text
User Query
→ Retriever
→ Retrieved Documents
→ Context Formatting
→ Prompt Template
→ Chat Model
→ Output Parser
→ Answer with Source
```

RAG Chain의 핵심은 LLM의 일반 지식이 아니라 검색된 Context에 근거해 답변하는 것이다.

---

### [핵심]

- RAG Chain은 검색 단계와 생성 단계를 연결한다.
- Retriever는 관련 문서를 검색한다.
- Retrieved Context는 Prompt에 주입된다.
- Prompt는 문서 기반 답변 규칙을 포함해야 한다.
- Chat Model은 Context 기반 답변을 생성한다.
- Output Parser는 답변 형식을 안정화한다.
- Source를 함께 반환하면 검증 가능성이 높아진다.
- 검색 실패와 생성 실패를 구분해야 한다.

---

### [실무]

RAG Chain 품질 기준:

| 항목               | 기준                               |
| ------------------ | ---------------------------------- |
| Loader             | 원본 문서 구조 보존                |
| Chunk              | 하나의 개념 단위 분리              |
| Metadata           | source, domain, part, section 유지 |
| Embedding          | 문서 언어와 도메인에 적합          |
| Retriever          | Golden Query Hit                   |
| Context Formatting | Source와 Section 구분              |
| Prompt             | Grounding Rule 포함                |
| Output             | Answer + Source 구조화             |

RAG 실패 패턴:

```text
Question
→ 관련 없는 Chunk 검색
→ 노이즈 Context 삽입
→ LLM이 부정확한 답변 생성
→ Source 검증 실패
```

RAG 개선 패턴:

```text
Question
→ Query Rewrite
→ Metadata Filter
→ Retriever
→ Context Formatting
→ Grounded Prompt
→ Answer with Source
```

---

### [FAQ]

Q. RAG Chain이 뭐야?

A.
사용자 질문으로 관련 문서를 검색하고 검색된 Context를 LLM에 넣어 문서 기반 답변을 생성하는 구조다.

Q. RAG Chain에서 가장 중요한 것은?

A.
Retriever와 Chunk 품질이다. 잘못된 문서를 가져오면 LLM 답변도 부정확해진다.

Q. Grounded Answer가 뭐야?

A.
검색된 문서 Context에 근거해 생성된 답변이다.

Q. RAG 답변에 Source가 필요한 이유는?

A.
답변이 어떤 문서 근거에서 나왔는지 검증하기 위해 필요하다.

Q. 문서에 없는 내용은 어떻게 처리해야 해?

A.
LLM이 추측하지 않고 문서에서 확인되지 않는다고 답하도록 Prompt에 명시해야 한다.

---

# 6. Agent Workflow Pattern

## 6.1 Agent 기본 구조

### [개념]

Agent는 LLM이 Prompt, Tool, State, Memory를 활용해 목표를 수행하는 구조다.

Agent는 모든 작업을 자동으로 수행해도 되는 존재가 아니다.

Agent에는 역할, 권한, Tool 범위, Stop Condition, Error Handling, Human Approval 기준이 필요하다.

기본 Flow:

```text
User Task
→ Agent Prompt
→ Tool Selection
→ Tool Execution
→ Observation
→ Final Answer
```

LangGraph Agent Flow:

```text
State
→ Agent Node
→ Tool Node if needed
→ Review Node
→ Final Node
```

---

### [핵심]

- Agent는 LLM + Prompt + Tool + State 조합이다.
- Agent Prompt는 역할과 제한을 정의한다.
- Tool은 Agent가 외부 기능을 사용하는 수단이다.
- Tool Arguments는 실행 전 검증해야 한다.
- Tool Result는 성공과 실패를 구조화해야 한다.
- Stop Condition이 없으면 Tool Loop가 무한 반복될 수 있다.
- 위험 Tool은 Human Approval이 필요하다.
- Agent Output은 Review Node에서 검증해야 한다.

---

### [실무]

Agent 구성 요소:

| 구성 요소      | 역할                  |
| -------------- | --------------------- |
| Agent Prompt   | 역할, 목표, 제한 정의 |
| Tool           | 외부 기능 실행        |
| State          | 현재 Workflow 상태    |
| Memory         | 과거 정보 재사용      |
| Output Parser  | Agent 결과 구조화     |
| Stop Condition | 종료 조건             |
| Error Handling | 실패 처리             |
| Review Node    | 결과 검증             |

개인 AI 개발팀 Agent:

| Agent          | 역할                                |
| -------------- | ----------------------------------- |
| PM Agent       | 요청 분석, 작업 분해, 라우팅        |
| SQL Agent      | DB 설계, SQL, QueryDSL              |
| Backend Agent  | Spring Boot, JPA, Security, API     |
| Frontend Agent | React, API 연동, UI                 |
| DevOps Agent   | Docker, 배포, 서버 운영             |
| AI Agent       | RAG, Agent, LangGraph, Tool Calling |
| Review Agent   | 품질 검증, 오류 탐지                |
| Fix Agent      | Review 결과 기반 수정               |
| Final Agent    | 사용자용 결과 정리                  |

---

### [FAQ]

Q. Agent가 뭐야?

A.
LLM이 Prompt, Tool, State를 활용해 목표를 수행하는 구조다.

Q. Agent와 일반 Chat Model은 뭐가 달라?

A.
Chat Model은 답변 생성 중심이고, Agent는 Tool 사용과 상태 기반 의사결정을 포함한다.

Q. Agent는 자동으로 모든 작업을 해도 돼?

A.
아니다. Tool 권한 제한, Stop Condition, Human Approval, Review가 필요하다.

Q. Agent Output은 왜 검증해야 해?

A.
Agent가 잘못된 Tool을 사용하거나 문서에 없는 내용을 생성할 수 있기 때문이다.

Q. 로컬 LLM에서 Multi-Agent는 어떻게 운영하는 게 좋아?

A.
병렬보다 순차 실행이 현실적이다. RAM, 응답 속도, Context 관리 제약을 고려해야 한다.

---

# 7. State-Based Workflow Pattern

## 7.1 State 기반 Workflow

### [개념]

State-Based Workflow는 각 Node가 공유 State를 읽고 필요한 필드만 업데이트하면서 진행되는 Workflow다.

State는 현재 Workflow 상태이고 Memory는 과거 정보를 재사용하기 위한 구조다.

기본 Flow:

```text
Initial State
→ PM Node updates task_type
→ Domain Node updates agent_outputs
→ Review Node updates review_findings
→ Final Node updates final_output
```

State Schema가 명확해야 Node 간 데이터 충돌을 줄일 수 있다.

---

### [핵심]

- State는 Node 간 공유 실행 상태다.
- State Schema는 필드명과 타입을 정의한다.
- 각 Node는 자신이 담당하는 필드만 업데이트한다.
- Routing은 task_type, status, review_result 같은 State 값으로 수행한다.
- Review / Fix Loop는 review_result, review_findings, fix_count를 사용한다.
- State가 너무 커지면 Context 품질이 낮아진다.
- 민감정보는 State에 저장하지 않는다.

---

### [실무]

기본 State 예시:

```python
from typing import TypedDict, Literal

class AgentState(TypedDict):
    user_request: str
    task_type: Literal["sql", "backend", "frontend", "devops", "ai", "mixed", "unknown"]
    requirements: list[str]
    required_agents: list[str]
    metadata_filter: dict
    retrieved_context: list[dict]
    agent_outputs: dict[str, str]
    review_result: Literal["pass", "fail", "warning", "unknown"]
    review_findings: list[str]
    fix_count: int
    max_fix_count: int
    final_output: str
    status: Literal["running", "waiting_approval", "pass", "fail", "error"]
    error: str | None
```

State 관리 기준:

| 기준            | 설명                                  |
| --------------- | ------------------------------------- |
| Field Ownership | Node별 수정 필드 제한                 |
| Enum Routing    | task_type, status, review_result 제한 |
| Context Control | retrieved_context 무제한 누적 금지    |
| Error Field     | 오류 상태 명시                        |
| Loop Count      | 반복 횟수 저장                        |
| Source Tracking | RAG 근거 유지                         |
| Sensitive Data  | API Key, Token 저장 금지              |

---

### [FAQ]

Q. State-Based Workflow가 뭐야?

A.
Node들이 공유 State를 읽고 필요한 필드를 업데이트하며 진행되는 Workflow다.

Q. State Schema는 왜 필요해?

A.
Node 간 입력과 출력 형식을 안정화하고 Routing 오류를 줄이기 위해 필요하다.

Q. State와 Memory는 달라?

A.
다르다. State는 현재 Workflow 실행 상태이고 Memory는 과거 정보를 재사용하기 위한 구조다.

Q. State에 모든 중간 결과를 저장하면 좋아?

A.
좋지 않다. State가 커지면 Context 품질과 실행 속도가 낮아진다.

Q. Routing에는 어떤 State 필드를 사용해?

A.
task_type, status, review_result, approval_required, error_type 같은 필드를 사용한다.

---

# 8. Review / Fix Loop Pattern

## 8.1 검토와 수정 반복 구조

### [개념]

Review / Fix Loop는 초안을 생성한 뒤 검토하고, 문제가 있으면 수정 후 다시 검토하는 반복 Workflow다.

LangGraph는 Conditional Edge와 State를 사용해 Review / Fix Loop를 안정적으로 구성할 수 있다.

기본 Flow:

```text
Draft Node
→ Review Node
→ if pass: Final Node
→ if fail and fix_count < max_fix_count: Fix Node
→ Review Node
→ if max reached: Final With Warning
```

---

### [핵심]

- Review Node는 고정된 기준으로 결과를 검토한다.
- Review Result는 pass, fail, warning으로 구조화한다.
- Review Findings는 Fix Node의 입력이 된다.
- Fix Node는 Review Findings 기준으로 수정한다.
- Fix 후에는 다시 Review Node로 보낸다.
- Max Iteration은 무한 반복을 방지한다.
- Max Iteration 도달 시 Final With Warning으로 종료할 수 있다.

---

### [실무]

Review 기준:

| 기준              | 설명                    |
| ----------------- | ----------------------- |
| Requirement Match | 사용자 요구사항 충족    |
| RAG Grounding     | 문서 근거 기반          |
| Output Format     | 요구 출력 형식 준수     |
| Code Correctness  | 코드 동작 가능성        |
| Security Risk     | 위험 작업 여부          |
| Completeness      | 누락 여부               |
| Consistency       | 이전 Part와 용어 일관성 |
| Maintainability   | 유지보수성              |

Review State 예시:

```python
from typing import TypedDict, Literal

class ReviewState(TypedDict):
    draft_output: str
    review_result: Literal["pass", "fail", "warning"]
    severity: Literal["none", "minor", "major", "critical"]
    review_findings: list[str]
    fix_count: int
    max_fix_count: int
    status: str
```

Review Router:

```text
if review_result == "pass":
    → Final Node

if review_result == "fail" and fix_count < max_fix_count:
    → Fix Node

if fix_count >= max_fix_count:
    → Final With Warning
```

---

### [FAQ]

Q. Review / Fix Loop가 뭐야?

A.
초안을 검토하고 문제가 있으면 수정한 뒤 다시 검토하는 반복 Workflow다.

Q. Review / Fix Loop는 왜 LangGraph에 적합해?

A.
State, Conditional Edge, 반복 횟수, 종료 조건을 명확히 설계할 수 있기 때문이다.

Q. Max Iteration은 왜 필요해?

A.
무한 수정 루프를 방지하기 위해 필요하다.

Q. Fix Node는 무엇을 기준으로 수정해?

A.
Review Node가 State에 저장한 review_findings를 기준으로 수정한다.

Q. Max Iteration에 도달하면 어떻게 해?

A.
Final With Warning으로 종료하고 남은 문제를 사용자에게 보고한다.

---

# 9. Human-in-the-loop Pattern

## 9.1 사용자 승인 구조

### [개념]

Human-in-the-loop는 Agent Workflow 중 사용자 승인, 선택, 확인이 필요한 지점에서 Workflow를 중단하고 사용자의 결정을 받은 뒤 재개하는 구조다.

위험 작업은 자동 실행하지 않는다.

기본 Flow:

```text
Agent Proposes Action
→ Interrupt
→ Save Checkpoint
→ User Approval
→ Resume Workflow
→ Execute or Cancel
```

---

### [핵심]

- 위험 작업 전 사용자 승인이 필요하다.
- 승인 대기 상태는 Checkpoint로 저장한다.
- 사용자 결정은 State에 반영한다.
- 승인 범위는 approval_scope에 저장한다.
- 승인 범위를 넘어서는 실행은 금지한다.
- 승인 후에도 Review Node가 결과를 검증할 수 있다.
- 오래된 Checkpoint는 재개 전 검증한다.

---

### [실무]

Human Approval 대상:

| 작업               | 승인 이유   |
| ------------------ | ----------- |
| 파일 수정          | 원본 변경   |
| 파일 삭제          | 데이터 손실 |
| DB 변경            | 데이터 손상 |
| Production 배포    | 운영 장애   |
| 외부 이메일 발송   | 외부 영향   |
| 비용 발생 API 호출 | 금전 비용   |
| 권한 변경          | 보안 위험   |
| 대량 코드 수정     | 범위 오류   |

Approval State 예시:

```json
{
  "status": "waiting_approval",
  "approval_required": true,
  "proposed_action": "write_file",
  "approval_scope": {
    "operation": "modify",
    "path": "Backend/src/main/java/.../AuthService.java",
    "risk_level": "medium"
  },
  "user_decision": null
}
```

Approval + Review Flow:

```text
Proposal
→ Approval Node
→ Checkpoint
→ User Decision
→ Tool Execution
→ Review Node
→ Final Node
```

---

### [FAQ]

Q. Human-in-the-loop가 뭐야?

A.
Agent Workflow 중 사용자 승인이나 선택이 필요한 지점에서 중단하고 결정 후 재개하는 구조다.

Q. 언제 Human Approval이 필요해?

A.
파일 수정, DB 변경, 배포, 비용 발생, 외부 발송처럼 Side Effect가 있는 작업 전에 필요하다.

Q. Checkpoint는 왜 필요해?

A.
승인 대기 상태를 저장하고 사용자 결정 후 이어서 실행하기 위해 필요하다.

Q. 승인받으면 바로 실행해도 돼?

A.
승인 범위 안에서만 실행해야 하며 실행 후 Review가 필요할 수 있다.

Q. 승인 범위를 초과하면 어떻게 해?

A.
Critical Issue로 처리하고 사용자에게 보고해야 한다.

---

# 10. Debugging / Testing Overview

## 10.1 Debugging과 Testing 기본 기준

### [개념]

Agent Workflow는 LLM 응답, RAG 검색, Tool 실행, State Update, Conditional Routing이 함께 동작한다.

따라서 Debugging과 Testing은 단계별로 분리해야 한다.

기본 Debugging Flow:

```text
User Request
→ PM Output
→ State Update
→ Routing Result
→ RAG Result
→ Tool Result
→ Agent Output
→ Review Result
→ Final Output
```

기본 Testing Flow:

```text
Prompt Test
→ Retriever Test
→ Parser Test
→ Tool Test
→ Node Test
→ Router Test
→ Graph Test
```

---

### [핵심]

- Node Input과 Node Output을 확인한다.
- State Update를 확인한다.
- Routing 결과를 확인한다.
- Tool Arguments와 Tool Result를 확인한다.
- Retrieved Context와 Source를 확인한다.
- Review Findings를 확인한다.
- Graph가 END에 도달하는지 확인한다.
- LLM 호출 없이 테스트 가능한 부분을 분리한다.
- 민감정보는 로그와 Trace에 저장하지 않는다.

---

### [실무]

테스트 대상:

| 대상              | 테스트 기준                           |
| ----------------- | ------------------------------------- |
| Prompt Template   | 변수 누락 여부                        |
| Retriever         | Golden Query Hit                      |
| Output Parser     | 잘못된 JSON 처리                      |
| Tool Function     | Args Schema, Permission               |
| Node Function     | State Reads / Writes                  |
| Router Function   | task_type, status, review_result 분기 |
| Review / Fix Loop | Max Iteration                         |
| Graph             | START부터 END까지 State 전이          |

Debugging 우선순위:

```text
1. PM Node Output 확인
2. Router 결과 확인
3. RAG Retrieved Context 확인
4. Tool Call Arguments 확인
5. Agent Output 확인
6. Review Findings 확인
7. Final Output 확인
```

---

### [FAQ]

Q. Agent Workflow는 왜 디버깅이 어려워?

A.
LLM 응답, Tool 실행, RAG 검색, State Update, 조건 분기가 함께 발생하기 때문이다.

Q. 가장 먼저 확인할 것은?

A.
PM Node가 task_type, requirements, required_agents를 올바르게 생성했는지 확인한다.

Q. Retriever는 어떻게 테스트해?

A.
Golden Query를 사용해 예상 문서가 검색되는지 확인한다.

Q. Tool은 어떻게 테스트해?

A.
Args Schema, Permission, Error Result를 Mock 또는 dry-run으로 테스트한다.

Q. Graph Test는 왜 필요해?

A.
Workflow가 올바른 State 전이를 거쳐 END에 도달하는지 확인하기 위해 필요하다.

---

# 11. Common Mistakes

## 11.1 자주 발생하는 설계 오류

### [개념]

LangChain과 LangGraph에서 가장 흔한 문제는 역할 혼동이다.

LangChain은 구성 요소 연결 Framework이고 LangGraph는 Workflow 제어 Framework다.

또 다른 문제는 State, Node, Edge, Tool 권한, Stop Condition 없이 Agent Workflow를 구성하는 것이다.

---

### [핵심]

- LangChain을 LLM 자체로 설명하면 안 된다.
- LangGraph를 단순 Chain 실행 도구로 설명하면 안 된다.
- State Schema 없이 Graph를 만들면 안 된다.
- Node 책임을 너무 크게 만들면 안 된다.
- Conditional Edge에 fallback이 없으면 안 된다.
- Review / Fix Loop에 Max Iteration이 없으면 안 된다.
- Tool Arguments 검증을 생략하면 안 된다.
- 위험 Tool을 승인 없이 실행하면 안 된다.
- Retriever 품질 확인 없이 RAG Chain을 운영하면 안 된다.
- State와 Memory를 혼동하면 안 된다.
- 민감정보를 State, Memory, Trace에 저장하면 안 된다.

---

### [실무]

금지 패턴:

```text
User Request
→ All Agents
→ Final Output
```

문제:

- 모든 요청을 모든 Agent에게 전달
- 비용과 시간 증가
- Agent 결과 충돌
- Review 기준 모호

권장 패턴:

```text
User Request
→ PM Node
→ Route by task_type
→ Domain Agent Node
→ Review Node
→ Final Node
```

금지 패턴:

```text
Review Node
→ Fix Node
→ Review Node
→ Fix Node
→ ...
```

문제:

- Max Iteration 없음
- Stop Condition 없음
- 무한 반복 위험

권장 패턴:

```text
Review Node
→ if pass: Final Node
→ if fail and fix_count < max_fix_count: Fix Node
→ else: Final With Warning
```

---

### [FAQ]

Q. LangChain과 LangGraph에서 가장 흔한 실수는?

A.
LangChain과 LangGraph의 역할을 혼동하고 단순 Chain으로 복잡한 Agent Workflow를 억지 구현하는 것이다.

Q. 모든 요청을 모든 Agent에 보내도 돼?

A.
권장하지 않는다. PM Node가 요청을 분석하고 필요한 Domain Agent로 라우팅해야 한다.

Q. State 없이 Graph를 만들어도 돼?

A.
권장하지 않는다. State Schema가 없으면 Node 간 데이터 흐름이 불안정해진다.

Q. Conditional Edge에 fallback이 필요한 이유는?

A.
예상하지 못한 State 값이나 모호한 요청에서 Workflow 중단을 막기 위해 필요하다.

Q. Tool Arguments 검증은 왜 필요해?

A.
LLM이 생성한 Tool Arguments는 틀릴 수 있고 위험한 실행을 유발할 수 있기 때문이다.

---

# 12. Part01 Checklist

## 12.1 Core Overview Checklist

### [Checklist]

- [ ] LLM Application을 Chatbot보다 넓은 구조로 설명했는가?
- [ ] LangChain을 LLM 자체가 아니라 구성 요소 연결 Framework로 설명했는가?
- [ ] LangGraph를 State 기반 Workflow Framework로 설명했는가?
- [ ] LangChain과 LangGraph의 역할 차이를 명확히 설명했는가?
- [ ] LangGraph Node 내부에서 LangChain을 사용할 수 있음을 설명했는가?
- [ ] RAG Chain 기본 Flow를 포함했는가?
- [ ] Agent Workflow 기본 Flow를 포함했는가?
- [ ] State와 Memory를 구분했는가?
- [ ] Review / Fix Loop 구조를 포함했는가?
- [ ] Human-in-the-loop 기준을 포함했는가?
- [ ] Debugging / Testing 개요를 포함했는가?
- [ ] Common Mistakes를 포함했는가?
- [ ] 개인 AI 개발팀 초기 구조와 확장 구조를 포함했는가?
- [ ] FAQ와 Retrieval Queries를 포함했는가?

---

# Retrieval Queries

### [FAQ]

Q. LangChain이 뭐야?
A. LangChain은 LLM, Prompt, Retriever, Tool, Output Parser를 연결해 LLM Application을 구성하는 Framework다.

Q. LangGraph가 뭐야?
A. LangGraph는 State, Node, Edge 기반으로 Agent Workflow와 Multi-Agent Workflow를 설계하는 Framework다.

Q. LangChain과 LangGraph 차이는?
A. LangChain은 Runnable과 Chain 중심의 구성 요소 연결 도구이고, LangGraph는 State 기반 Workflow 제어 도구다.

Q. LangChain과 LangGraph는 같이 써?
A. 같이 쓴다. LangGraph Node 내부에서 LangChain Runnable, RAG Chain, Tool Chain을 실행할 수 있다.

Q. LLM Application이 뭐야?
A. Prompt, Model, Parser, Retriever, Tool, Workflow를 조합해 사용자 요청을 처리하는 시스템이다.

Q. LLM Application은 Chatbot이랑 같아?
A. 아니다. Chatbot은 단순 대화 중심이고 LLM Application은 RAG, Tool Calling, Agent Workflow까지 포함할 수 있다.

Q. Runnable이 뭐야?
A. Runnable은 입력을 받아 출력을 만드는 LangChain의 실행 가능한 구성 단위다.

Q. Chain은 언제 써?
A. 요약, 분류, RAG 답변 생성처럼 순차 Pipeline이 필요한 작업에 사용한다.

Q. Graph는 언제 써?
A. 조건 분기, 반복, Review / Fix Loop, Multi-Agent, Human Approval, Checkpoint가 필요한 Workflow에 사용한다.

Q. 단순 RAG에도 LangGraph가 필요해?
A. 필수는 아니다. 단순 RAG는 LangChain RAG Chain만으로도 충분하다.

Q. Multi-Agent를 만들려면 LangGraph가 좋아?
A. 좋다. Agent를 Node로 구성하고 State와 Edge로 실행 흐름을 제어할 수 있기 때문이다.

Q. RAG Chain은 어떻게 구성해?
A. User Query를 Retriever로 검색하고 Retrieved Context를 Prompt에 넣어 LLM이 답변하도록 구성한다.

Q. RAG에서 Retriever가 중요한 이유는?
A. Retriever가 잘못된 문서를 가져오면 LLM 답변도 부정확해지기 때문이다.

Q. Grounded Answer가 뭐야?
A. 검색된 문서 Context에 근거해 생성된 답변이다.

Q. 문서에 없는 내용은 어떻게 답해야 해?
A. 추측하지 않고 문서에서 확인되지 않는다고 답해야 한다.

Q. LangGraph State가 뭐야?
A. LangGraph State는 Node들이 읽고 업데이트하는 공유 실행 상태 데이터다.

Q. State Schema는 왜 필요해?
A. Node 간 입력과 출력 형식을 안정화하고 Workflow 오류를 줄이기 위해 필요하다.

Q. State와 Memory 차이는?
A. State는 현재 Workflow 실행 상태이고 Memory는 과거 정보를 재사용하기 위한 구조다.

Q. Node는 뭐야?
A. Node는 LangGraph에서 하나의 작업 단위이며 Agent, Tool 실행, Review, Fix를 표현할 수 있다.

Q. Edge는 뭐야?
A. Edge는 Node 다음에 어떤 Node를 실행할지 연결하는 Workflow 흐름이다.

Q. Conditional Edge는 언제 써?
A. State 값에 따라 Backend Agent, Frontend Agent, AI Agent처럼 다음 단계를 다르게 선택할 때 사용한다.

Q. Checkpoint는 왜 필요해?
A. 긴 Workflow를 중간 저장하고 실패나 사용자 승인 대기 후 이어서 실행하기 위해 필요하다.

Q. Human-in-the-loop는 언제 필요해?
A. 파일 수정, DB 변경, 배포, 비용 발생, 외부 발송처럼 위험 작업 전 사용자 승인이 필요할 때 사용한다.

Q. Review / Fix Loop는 어떻게 만들어?
A. Draft Node 이후 Review Node가 pass/fail을 판단하고 fail이면 Fix Node로 보내 다시 Review Node로 돌아오게 만든다.

Q. Review / Fix Loop에서 무한 반복을 막으려면?
A. Max Iteration과 Stop Condition을 반드시 설정해야 한다.

Q. Multi-Agent Workflow는 어떻게 구성해?
A. PM Node가 요청을 분석하고 Domain Agent Node가 작업하며 Review Node가 검증하고 Final Node가 결과를 정리한다.

Q. 개인 AI 개발팀 초기 구조는?
A. User → PM Agent → Backend Agent → Review Agent → Final Output 구조로 시작하는 것이 현실적이다.

Q. 개인 AI 개발팀 확장 구조는?
A. User → PM Agent → SQL Agent → Backend Agent → Frontend Agent → Review Agent → Fix Agent → Final Output 구조로 확장할 수 있다.

Q. 로컬 LLM 환경에서 Multi-Agent는 병렬이 좋아?
A. 보통은 순차 실행이 더 현실적이다. RAM, 응답 속도, 모델 상주 제약을 고려해야 한다.

Q. Agent Workflow는 어떻게 디버깅해?
A. Node Input, Node Output, State Update, Tool Call Arguments, Retrieved Context, Routing 결과를 추적한다.

Q. Retriever 테스트는 어떻게 해?
A. Golden Query를 사용해 예상 문서가 검색되는지 확인한다.

Q. Tool Arguments 검증은 왜 필요해?
A. LLM이 생성한 Tool Arguments가 틀릴 수 있고 위험 작업을 유발할 수 있기 때문이다.

Q. Agent Workflow에서 위험한 작업은 어떻게 처리해?
A. Human Approval Node 또는 Interrupt를 두고 사용자 승인 후 실행해야 한다.

Q. LangChain & LangGraph Part01의 핵심 목표는?
A. LangChain과 LangGraph의 역할을 구분하고 RAG Chain, Agent Workflow, State 기반 Graph 설계의 기초를 잡는 것이다.
