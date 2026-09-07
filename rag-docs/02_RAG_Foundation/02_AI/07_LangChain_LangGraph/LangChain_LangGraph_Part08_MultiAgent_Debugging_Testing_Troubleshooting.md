# LangChain & LangGraph Part08 MultiAgent Debugging Testing Troubleshooting

---

# 1. Multi-Agent Workflow Core

## 1.1 Multi-Agent Workflow 기본 개념

### [개념]

Multi-Agent Workflow는 여러 Agent를 역할별 Node로 분리하고, State와 Edge를 통해 실행 흐름을 제어하는 구조다.

Multi-Agent는 단순히 여러 LLM을 동시에 호출하는 구조가 아니다.

Multi-Agent의 핵심은 역할 분리, State 공유, 조건 라우팅, Agent 간 Handoff, Review / Fix Loop, Final Output 정리다.

기본 Flow:

```text
User Request
→ PM Agent
→ Domain Agent
→ Review Agent
→ Fix Agent if needed
→ Final Agent
→ Final Output
```

LangGraph 표현:

```text
START
→ PM Node
→ Router
→ Domain Agent Node
→ Review Node
→ Conditional Edge
→ Final Node
→ END
```

Part08은 Part01~Part07의 내용을 통합해 Multi-Agent Workflow 운영, Debugging, Testing, Troubleshooting 기준을 정리한다.

---

### [핵심]

- Multi-Agent Workflow는 Agent 역할 분리 구조다.
- PM Agent는 요청 분석과 라우팅을 담당한다.
- Domain Agent는 전문 작업을 담당한다.
- Review Agent는 결과 검증을 담당한다.
- Fix Agent는 Review Findings를 반영한다.
- Final Agent는 사용자용 결과를 정리한다.
- State는 Agent 간 공유 상태를 관리한다.
- Conditional Edge는 다음 Agent를 선택한다.
- Checkpoint는 긴 Workflow의 중단과 재개를 지원한다.
- Human Approval은 위험 작업을 제어한다.
- 모든 요청을 모든 Agent에게 보내지 않는다.

---

### [실무]

2026 실무 기준 Multi-Agent Workflow는 처음부터 복잡하게 만들지 않는다.

권장 확장 순서:

```text
Single Chain
→ RAG Chain
→ Single Agent
→ Review / Fix Loop
→ PM Router
→ Multi-Agent Workflow
→ Human Approval
→ Checkpoint / Resume
```

초기 권장 구조:

```text
User
→ PM Agent
→ Backend Agent
→ Review Agent
→ Final Agent
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
→ Final Agent
```

최종 확장 구조:

```text
User
→ PM Agent
→ SQL Agent
→ Backend Agent
→ Frontend Agent
→ DevOps Agent
→ AI Agent
→ Review Agent
→ Fix Agent
→ Final Agent
```

Agent별 책임:

| Agent          | 책임                                    |
| -------------- | --------------------------------------- |
| PM Agent       | 요청 분석, 작업 분해, 라우팅            |
| SQL Agent      | DB 설계, SQL, QueryDSL                  |
| Backend Agent  | Spring Boot, JPA, Security, API         |
| Frontend Agent | React, API 연동, UI                     |
| DevOps Agent   | Docker, 배포, 서버 운영                 |
| AI Agent       | RAG, LangChain, LangGraph, Tool Calling |
| Review Agent   | 품질 검증, 누락, 오류 탐지              |
| Fix Agent      | Review 결과 기반 수정                   |
| Final Agent    | 사용자용 최종 응답 정리                 |

---

### [FAQ]

Q. Multi-Agent Workflow가 뭐야?

A.
여러 Agent를 역할별 Node로 나누고 State와 Edge로 실행 흐름을 제어하는 구조다.

Q. Multi-Agent는 여러 LLM을 동시에 호출하는 거야?

A.
아니다. 핵심은 역할 분리, State 공유, Routing, Review / Fix Workflow다.

Q. PM Agent는 왜 필요해?

A.
사용자 요청을 분석하고 필요한 Agent만 선택해 불필요한 실행과 결과 충돌을 줄이기 위해 필요하다.

Q. Review Agent는 왜 필요해?

A.
Domain Agent 결과의 요구사항 충족, 문서 근거, 코드 정확성, 누락, 위험 요소를 검증하기 위해 필요하다.

Q. 처음부터 모든 Agent를 만들어야 해?

A.
권장하지 않는다. PM, Domain, Review 중심으로 시작하고 점진적으로 확장하는 것이 좋다.

---

# 2. Personal AI Development Team

## 2.1 개인 AI 개발팀 구조

### [개념]

개인 AI 개발팀은 사용자가 PM Agent에게만 요청하고, 내부 Agent Workflow가 작업을 분해해 순차적으로 처리하는 구조다.

사용자는 내부 Agent 실행 과정을 모두 직접 제어하지 않고 최종 결과를 확인한다.

기본 목표:

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

로컬 LLM 환경에서는 병렬 실행보다 순차 실행이 현실적이다.

개인 AI 개발팀은 단순 RAG Chatbot이 아니라 RAG 기반 Agent Workflow를 가진 개발 보조 시스템이다.

---

### [핵심]

- 사용자는 PM Agent에게만 요청한다.
- PM Agent가 작업을 분해한다.
- 필요한 Domain Agent만 실행한다.
- Agent 실행 순서는 작업 유형에 따라 달라진다.
- Domain Agent는 RAG 문서를 우선 참조한다.
- RAG 검색은 Metadata Filter로 Domain을 제한한다.
- Review Agent는 최종 품질을 검증한다.
- Fix Agent는 Review Findings를 반영한다.
- Final Agent는 사용자에게 필요한 결과만 제공한다.
- 로컬 LLM 환경에서는 순차 실행을 우선한다.

---

### [실무]

개인 AI 개발팀 기본 State:

```python
from typing import TypedDict, Literal

class PersonalAIDevTeamState(TypedDict):
    user_request: str
    task_type: Literal["sql", "backend", "frontend", "devops", "ai", "mixed", "unknown"]
    requirements: list[str]
    required_agents: list[str]
    current_agent: str
    completed_agents: list[str]
    metadata_filter: dict
    retrieved_context: list[dict]
    tool_results: list[dict]
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

요청 유형별 Agent 실행 예시:

| 사용자 요청      | 실행 순서                                            |
| ---------------- | ---------------------------------------------------- |
| SQL 설계         | PM → SQL → Review → Final                            |
| Backend API 구현 | PM → Backend → Review → Final                        |
| React 화면 구현  | PM → Frontend → Review → Final                       |
| RAG Agent 설계   | PM → AI → Review → Final                             |
| Docker 배포 구성 | PM → DevOps → Review → Final                         |
| 풀스택 기능 구현 | PM → SQL → Backend → Frontend → Review → Fix → Final |
| 위험 작업 포함   | PM → Approval → Domain → Review → Final              |

로컬 LLM 운영 기준:

- 병렬보다 순차 실행 우선
- Agent별 Context 최소화
- RAG Metadata Filter 사용
- 긴 Tool Result는 요약 저장
- Review / Fix 반복 횟수 제한
- 위험 작업은 Human Approval 사용
- Trace에는 민감정보 저장 금지

---

### [FAQ]

Q. 개인 AI 개발팀 구조는 뭐야?

A.
사용자가 PM Agent에게 요청하면 PM이 작업을 분해하고 Domain Agent와 Review Agent가 순차적으로 처리하는 구조다.

Q. 사용자는 모든 Agent에게 직접 요청해야 해?

A.
아니다. 사용자는 PM Agent에게만 요청하고 내부 Routing은 PM Agent가 담당하는 구조가 좋다.

Q. 로컬 LLM 환경에서 병렬 실행이 좋아?

A.
대부분은 순차 실행이 더 현실적이다. RAM, 응답 속도, Context 관리 제약을 고려해야 한다.

Q. Domain Agent는 RAG를 어떻게 써?

A.
자신의 Domain에 맞는 Metadata Filter로 관련 RAG 문서를 검색해 근거로 사용한다.

Q. Final Agent는 무엇을 해?

A.
내부 Agent 결과와 Review 결과를 사용자에게 필요한 최종 응답으로 정리한다.

---

# 3. Multi-Agent Handoff

## 3.1 Agent 간 결과 전달

### [개념]

Handoff는 한 Agent의 결과를 다음 Agent가 사용할 수 있는 형태로 전달하는 과정이다.

Multi-Agent Workflow에서 Handoff가 불명확하면 다음 Agent가 잘못된 입력을 받아 오류가 발생한다.

기본 Flow:

```text
Agent A Output
→ Structured Handoff
→ State Update
→ Agent B Input
```

Handoff는 자유로운 긴 문장보다 구조화된 Output이 안정적이다.

Handoff는 State의 `agent_outputs`, `sources`, `assumptions`, `open_issues` 같은 필드로 관리할 수 있다.

---

### [핵심]

- Agent Output은 다음 Agent가 사용할 수 있어야 한다.
- Handoff 결과는 구조화하는 것이 좋다.
- requirements, assumptions, output, issues를 분리한다.
- Source와 Retrieved Context를 함께 유지한다.
- 불확실한 내용은 uncertainty로 표시한다.
- Agent별 책임 범위를 넘는 내용은 다음 Agent에게 넘긴다.
- Handoff 결과는 State에 저장한다.
- Handoff는 Review Agent의 검토 대상이다.

---

### [실무]

Backend Agent Handoff 예시:

```json
{
  "agent": "backend",
  "status": "completed",
  "requirements_covered": [
    "JWT 인증 흐름 설명",
    "Controller-Service-Repository 책임 분리"
  ],
  "output": "Backend 구현 초안",
  "sources": [
    {
      "source": "Security Advanced Part04 JWT",
      "section": "JWT Authentication Flow"
    }
  ],
  "assumptions": ["Refresh Token 저장소는 Redis 사용 가능"],
  "open_issues": ["Frontend Token 저장 방식은 Frontend Agent 확인 필요"],
  "risks": ["Refresh Token 저장소 미확정"],
  "next_recommended_agent": "frontend"
}
```

Handoff Schema 권장 필드:

| 필드                   | 목적                             |
| ---------------------- | -------------------------------- |
| agent                  | 결과 생성 Agent                  |
| status                 | 완료, 실패, 대기 상태            |
| requirements_covered   | 충족한 요구사항                  |
| output                 | 실제 결과                        |
| sources                | RAG 근거                         |
| assumptions            | 가정                             |
| open_issues            | 다음 Agent 또는 사용자 확인 필요 |
| risks                  | 위험 요소                        |
| next_recommended_agent | 다음 Agent 제안                  |

Handoff 금지:

- 자유 문장 하나로 전체 결과 전달
- Source 제거
- 가정과 사실 혼합
- 오류를 숨기고 completed로 표시
- 다음 Agent가 필요한 정보를 누락
- 민감정보 포함
- Review Findings를 무시하고 다음 Agent로 진행

---

### [FAQ]

Q. Handoff가 뭐야?

A.
한 Agent의 결과를 다음 Agent가 사용할 수 있는 구조로 전달하는 과정이다.

Q. Handoff를 구조화해야 하는 이유는?

A.
다음 Agent가 요구사항, 결과, Source, 가정, 남은 문제를 명확히 이해해야 하기 때문이다.

Q. Handoff에 Source가 필요한 이유는?

A.
Review Agent가 결과의 문서 근거를 검증할 수 있게 하기 위해 필요하다.

Q. assumptions는 왜 분리해?

A.
사실과 가정을 구분하지 않으면 다음 Agent가 추측을 확정된 정보로 사용할 수 있기 때문이다.

Q. Handoff 실패는 어떤 문제를 만들 수 있어?

A.
Agent 간 요구사항 누락, 결과 충돌, 잘못된 구현, Review 실패를 만들 수 있다.

---

# 4. Cross-domain Consistency

## 4.1 도메인 간 일관성 검토

### [개념]

Cross-domain Consistency는 SQL, Backend, Frontend, DevOps, AI Agent 결과가 서로 충돌하지 않는지 검토하는 기준이다.

Multi-Agent Workflow에서는 각 Agent가 자신의 Domain만 보고 작업하기 때문에 전체 결과 간 불일치가 발생할 수 있다.

기본 Flow:

```text
SQL Output
→ Backend Output
→ Frontend Output
→ Review Agent
→ Consistency Check
```

Review Agent는 Domain 간 연결 지점을 검토해야 한다.

---

### [핵심]

- SQL Schema와 Backend Entity가 일치해야 한다.
- Backend API와 Frontend API 호출이 일치해야 한다.
- Backend Security 정책과 Frontend 인증 흐름이 일치해야 한다.
- DevOps 환경 변수와 Backend 설정이 일치해야 한다.
- AI Agent RAG Tool과 Vector Store 설정이 일치해야 한다.
- Agent별 용어와 파일명이 일관되어야 한다.
- Handoff의 assumptions와 open_issues를 검토해야 한다.
- 충돌이 있으면 Review Findings로 기록한다.

---

### [실무]

Cross-domain Check Matrix:

| 연결 지점           | 검토 기준                            |
| ------------------- | ------------------------------------ |
| SQL ↔ Backend       | 테이블명, 컬럼명, 타입, 관계         |
| Backend ↔ Frontend  | URL, Method, Request, Response       |
| Backend ↔ Security  | 인증 필요 여부, Role, Token          |
| Backend ↔ DevOps    | profile, env, DB URL, port           |
| Frontend ↔ Security | Token 저장, Authorization Header     |
| AI ↔ RAG DB         | Embedding Model, Dimension, Metadata |
| AI ↔ Agent Workflow | State Schema, Tool Schema, Routing   |
| DevOps ↔ AI Server  | Ollama URL, Vector DB URL, Volume    |

API 일관성 예시:

```json
{
  "backend_api": {
    "method": "GET",
    "path": "/api/posts/{postId}",
    "response": "PostResDto"
  },
  "frontend_call": {
    "method": "GET",
    "path": "/api/post/{id}"
  },
  "consistency_result": "fail",
  "finding": "Backend path는 /api/posts/{postId}인데 Frontend는 /api/post/{id}를 호출함"
}
```

Review Agent 검토 질문:

- SQL 컬럼과 Entity 필드명이 일치하는가?
- DTO 필드와 Frontend 사용 필드가 일치하는가?
- API 경로와 Method가 일치하는가?
- 인증이 필요한 API에 Token이 포함되는가?
- 환경 변수명이 배포 설정과 일치하는가?
- RAG Metadata Filter가 실제 Metadata와 일치하는가?
- Tool Schema와 Tool Call Arguments가 일치하는가?
- Approval Scope와 Tool Result가 일치하는가?

---

### [FAQ]

Q. Cross-domain Consistency가 뭐야?

A.
여러 Domain Agent 결과가 서로 충돌하지 않고 연결 지점이 일치하는지 검토하는 기준이다.

Q. 왜 도메인 간 일관성 검토가 필요해?

A.
각 Agent가 자기 Domain만 보고 작업하면 API, DTO, DB, 설정 간 불일치가 생길 수 있기 때문이다.

Q. Backend와 Frontend는 무엇을 맞춰야 해?

A.
API URL, HTTP Method, Request Body, Response DTO, 인증 헤더를 맞춰야 한다.

Q. SQL과 Backend는 무엇을 맞춰야 해?

A.
테이블명, 컬럼명, 데이터 타입, 관계, 제약조건, Entity 매핑을 맞춰야 한다.

Q. Cross-domain 문제는 누가 찾는 게 좋아?

A.
Review Agent가 전체 Agent Output과 Handoff를 기준으로 검토하는 것이 좋다.

---

# 5. Workflow Debugging

## 5.1 Agent Workflow Debugging

### [개념]

Workflow Debugging은 Agent Workflow의 각 단계에서 State, Node Input, Node Output, Tool Call, Retrieved Context, Routing 결과를 추적하는 과정이다.

Agent Workflow는 LLM 응답, Tool 실행, RAG 검색, State Update, Conditional Routing이 함께 동작하므로 단순 로그만으로 원인 파악이 어렵다.

기본 Flow:

```text
User Request
→ PM Output
→ State Update
→ Routing Result
→ Agent Output
→ Review Result
→ Final Output
```

Debugging은 어느 단계에서 실패했는지 분리하는 것이 핵심이다.

---

### [핵심]

- Node Input을 확인한다.
- Node Output을 확인한다.
- State Update를 확인한다.
- Routing 결과를 확인한다.
- Tool Call Arguments를 확인한다.
- Tool Result를 확인한다.
- Retrieved Context를 확인한다.
- Review Findings를 확인한다.
- Final Output이 요구사항을 반영하는지 확인한다.
- 민감정보는 로그에 남기지 않는다.

---

### [실무]

Debugging 대상:

| 대상         | 확인 내용                                 |
| ------------ | ----------------------------------------- |
| PM Node      | task_type, requirements, required_agents  |
| Router       | 선택된 다음 Node                          |
| RAG Node     | query, metadata_filter, retrieved_context |
| Tool Node    | tool_name, args, permission, result       |
| Domain Agent | output, assumptions, sources              |
| Review Node  | review_result, findings, severity         |
| Fix Node     | fix_count, fixed_output                   |
| Final Node   | final_output, warnings                    |
| State        | 필드 누락, 타입 불일치, 과도한 크기       |
| Checkpoint   | 재개 가능 상태인지 확인                   |

Trace Log 예시:

```json
{
  "step": "rag_node",
  "input": {
    "query": "LangGraph State 설계",
    "metadata_filter": {
      "domain": "AI",
      "document": "LangChain_LangGraph"
    }
  },
  "output": {
    "retrieved_count": 5,
    "top_source": "07_LangChain_LangGraph_Part06_State_Node_Edge_Routing.md",
    "missing_context": false
  },
  "state_update": ["retrieved_context", "sources"]
}
```

로그 금지 데이터:

- API Key
- Access Token
- Refresh Token
- 비밀번호
- Secret 환경 변수
- 개인정보
- 민감한 파일 원문 전체
- 승인되지 않은 외부 발송 내용

---

### [FAQ]

Q. Workflow Debugging이 뭐야?

A.
Agent Workflow의 State, Node, Tool, RAG, Routing, Review 결과를 단계별로 추적하는 과정이다.

Q. Agent Workflow는 왜 디버깅이 어려워?

A.
LLM 응답, Tool 실행, RAG 검색, State Update, 조건 분기가 함께 발생하기 때문이다.

Q. 가장 먼저 확인할 것은?

A.
PM Node가 task_type, requirements, required_agents를 올바르게 생성했는지 확인한다.

Q. RAG Node 디버깅은 무엇을 확인해?

A.
query, metadata_filter, retrieved_context, source, missing_context를 확인한다.

Q. 로그에 남기면 안 되는 것은?

A.
API Key, Token, 비밀번호, Secret, 개인정보, 민감한 파일 원문 전체는 로그에 남기면 안 된다.

---

# 6. Tracing

## 6.1 Trace 기반 실행 추적

### [개념]

Tracing은 Agent Workflow 실행 과정을 시간 순서대로 기록해 어느 Node와 Tool에서 어떤 입력과 출력이 발생했는지 추적하는 방식이다.

Tracing은 Debugging보다 실행 흐름 전체를 보는 데 초점을 둔다.

기본 구조:

```text
Trace ID
→ Step 1: PM Node
→ Step 2: Router
→ Step 3: RAG Node
→ Step 4: Agent Node
→ Step 5: Review Node
→ Final
```

Trace는 재현 가능한 오류 분석과 성능 병목 분석에 유용하다.

Trace ID는 실행 추적용이고, Thread ID는 Checkpoint와 Workflow 재개 식별용이다.

---

### [핵심]

- Trace ID는 하나의 Workflow 실행을 식별한다.
- Thread ID는 Checkpoint와 재개 대상 Workflow를 식별한다.
- 각 Node 실행 시간을 기록한다.
- 각 Node의 입력과 출력 요약을 기록한다.
- Tool Call과 Tool Result를 기록한다.
- Retriever 검색 결과 요약을 기록한다.
- Error 발생 위치를 기록한다.
- Trace에는 민감정보를 저장하지 않는다.
- Trace는 너무 상세하면 분석이 어려워진다.

---

### [실무]

Trace Event 예시:

```json
{
  "trace_id": "trace-20260630-001",
  "thread_id": "devteam-workflow-001",
  "step": 4,
  "node": "review_node",
  "started_at": "2026-06-30T10:15:00+09:00",
  "ended_at": "2026-06-30T10:15:08+09:00",
  "duration_ms": 8000,
  "input_summary": {
    "requirements_count": 5,
    "agent_output_exists": true
  },
  "output_summary": {
    "review_result": "fail",
    "findings_count": 2,
    "severity": "major"
  },
  "error": null
}
```

Trace 활용 기준:

| 목적             | 활용                    |
| ---------------- | ----------------------- |
| 오류 위치 확인   | 실패 Node 식별          |
| 성능 분석        | 느린 Node 확인          |
| Tool 문제 확인   | Tool Call / Result 추적 |
| RAG 문제 확인    | 검색 결과와 Source 확인 |
| Review 문제 확인 | Findings 변화 확인      |
| 재현 테스트      | 동일 Input으로 재실행   |
| 감사 기록        | 승인, 실행, 변경 기록   |

Trace 보존 기준:

- 민감정보 제외
- 요약 중심 저장
- 오래된 Trace TTL 적용
- 오류 Trace 우선 보존
- 승인 / 배포 / 파일 변경 Trace 별도 보존 가능
- Prompt 전문 저장은 보안 검토 후 결정
- Tool Result 전체 저장보다 요약 저장 우선

---

### [FAQ]

Q. Tracing이 뭐야?

A.
Workflow 실행 과정을 시간 순서대로 기록해 Node, Tool, RAG, Review 흐름을 추적하는 방식이다.

Q. Trace ID는 왜 필요해?

A.
하나의 Workflow 실행을 식별하고 관련 로그를 연결하기 위해 필요하다.

Q. Trace ID와 Thread ID는 달라?

A.
다르다. Trace ID는 실행 추적용이고 Thread ID는 Checkpoint 재개 대상 식별용이다.

Q. Debugging과 Tracing은 뭐가 달라?

A.
Debugging은 원인 분석이고, Tracing은 실행 흐름 전체 기록과 추적에 가깝다.

Q. Trace에 Prompt 전체를 저장해도 돼?

A.
권장하지 않는다. 민감정보와 보안 위험이 있어 요약 저장을 우선한다.

---

# 7. Testing Strategy

## 7.1 Agent Workflow 테스트 전략

### [개념]

Testing Strategy는 Agent Workflow의 Prompt, Retriever, Parser, Tool, Node, Router, Graph를 분리해 검증하는 기준이다.

Agent Workflow는 LLM 출력이 비결정적이므로 모든 테스트를 실제 LLM 호출에 의존하면 불안정하다.

기본 Flow:

```text
Unit Test
→ Node Test
→ Router Test
→ Retriever Test
→ Graph Test
→ Evaluation Test
```

LLM 호출 없이 테스트 가능한 부분을 먼저 분리한다.

---

### [핵심]

- Prompt Template 변수 누락을 테스트한다.
- Retriever는 Golden Query로 테스트한다.
- Parser는 잘못된 JSON을 테스트한다.
- Tool은 Args Schema와 Permission을 테스트한다.
- Node는 State 입력과 State Update를 테스트한다.
- Router는 조건별 다음 Node를 테스트한다.
- Review / Fix Loop는 종료 조건을 테스트한다.
- Graph는 전체 State 전이를 테스트한다.
- 실제 LLM 호출 테스트는 제한적으로 수행한다.
- 위험 Tool은 Mock 또는 dry-run으로 테스트한다.

---

### [실무]

테스트 대상별 기준:

| 테스트 대상     | 검증 내용                             |
| --------------- | ------------------------------------- |
| Prompt Test     | 변수 누락, 출력 형식 지시             |
| Retriever Test  | Golden Query Hit                      |
| Parser Test     | JSON 파싱, 실패 처리                  |
| Tool Test       | Args Schema, Permission, Error Result |
| Node Test       | Reads / Writes, State Update          |
| Router Test     | task_type, review_result 분기         |
| Loop Test       | max_fix_count, max_tool_calls         |
| Graph Test      | START부터 END까지 흐름                |
| Review Test     | findings 구조, severity 판단          |
| Evaluation Test | Grounding, Source Accuracy            |
| Approval Test   | approval_scope, 승인 범위 검증        |

테스트 우선순위:

```text
1. Tool Args Validation
2. Router Function
3. Node State Update
4. Retriever Golden Query
5. Parser Error Handling
6. Review / Fix Loop Stop Condition
7. Approval Scope Validation
8. Full Graph Smoke Test
```

테스트 금지:

- 모든 테스트에서 실제 LLM API 호출
- 위험 Tool을 실제 실행
- Production DB 대상 테스트
- API Key를 테스트 로그에 출력
- 비결정적 LLM 문장을 exact match로 검증
- 삭제 / 배포 / 외부 발송 Tool 실사용

---

### [FAQ]

Q. Agent Workflow 테스트는 어떻게 해?

A.
Prompt, Retriever, Parser, Tool, Node, Router, Graph를 분리해 테스트한다.

Q. 모든 테스트에서 실제 LLM을 호출해도 돼?

A.
권장하지 않는다. 비용과 비결정성 때문에 Mock, Stub, Golden Query를 우선 사용한다.

Q. Router Test는 무엇을 확인해?

A.
task_type, review_result, error_type 같은 State 값에 따라 올바른 Node로 이동하는지 확인한다.

Q. Node Test는 무엇을 확인해?

A.
입력 State를 받아 예상 State Update를 반환하는지 확인한다.

Q. Loop Test는 왜 필요해?

A.
Review / Fix Loop, Tool Calling Loop, Retry Loop가 무한 반복되지 않는지 확인하기 위해 필요하다.

---

# 8. Graph Testing

## 8.1 State Transition 테스트

### [개념]

Graph Testing은 LangGraph Workflow가 START에서 END까지 올바른 State 전이를 수행하는지 검증하는 테스트다.

Graph Test는 Node 단위 테스트보다 넓은 범위의 통합 테스트다.

기본 Flow:

```text
Initial State
→ Graph Run
→ Intermediate State Check
→ Final State Check
```

Graph Testing은 Routing, Loop, Error Path, Approval Path, Final Output을 함께 검증한다.

---

### [핵심]

- Initial State를 명확히 정의한다.
- 예상 Routing 경로를 정의한다.
- 각 Node 이후 State Update를 확인한다.
- Conditional Edge가 올바르게 작동하는지 확인한다.
- Error Path를 테스트한다.
- Approval Path를 테스트한다.
- Loop Stop Condition을 테스트한다.
- Final State가 요구사항을 충족하는지 확인한다.
- 위험 Tool은 Mock으로 대체한다.

---

### [실무]

Graph Test Case 예시:

| Test Case     | Initial State                | Expected Path                                  |
| ------------- | ---------------------------- | ---------------------------------------------- |
| Backend 요청  | task_type=backend            | PM → Backend → Review → Final                  |
| Frontend 요청 | task_type=frontend           | PM → Frontend → Review → Final                 |
| Mixed 요청    | task_type=mixed              | PM → SQL → Backend → Frontend → Review → Final |
| Review 실패   | review_result=fail           | Review → Fix → Review                          |
| Max Fix 도달  | fix_count=max                | Review → Final With Warning                    |
| 승인 필요     | approval_required=true       | Approval Node                                  |
| 검색 실패     | missing_context=true         | Final Missing Context                          |
| Parser Error  | error_type=parser_error      | Retry Node                                     |
| 권한 오류     | error_type=permission_denied | Approval or Error Node                         |

State Transition Assertion 예시:

```json
{
  "initial_state": {
    "user_request": "Backend JWT API 설계",
    "task_type": "backend",
    "status": "running"
  },
  "expected_updates": {
    "requirements": "not_empty",
    "agent_outputs.backend": "exists",
    "review_result": "pass_or_fail",
    "final_output": "exists"
  },
  "expected_end_state": "END"
}
```

Graph Test 점검 항목:

- START 경로 존재
- END 경로 존재
- fallback 경로 존재
- error path 존재
- approval path 존재
- max iteration 동작
- State 필드 타입 유지
- Agent Output 누락 없음
- Review 결과 반영
- Final Output 생성

---

### [FAQ]

Q. Graph Testing이 뭐야?

A.
LangGraph Workflow가 START에서 END까지 올바른 State 전이를 수행하는지 검증하는 테스트다.

Q. Graph Test는 Node Test와 뭐가 달라?

A.
Node Test는 개별 Node 검증이고, Graph Test는 Node, Edge, Routing, Loop를 함께 검증한다.

Q. Graph Test에서 무엇을 확인해?

A.
Routing 경로, State Update, Error Path, Approval Path, Loop 종료, Final State를 확인한다.

Q. 위험 Tool은 Graph Test에서 어떻게 처리해?

A.
실제 실행하지 않고 Mock이나 dry-run으로 대체한다.

Q. Graph Test에서 END 경로를 확인해야 하는 이유는?

A.
Workflow가 무한 반복되거나 중간에 멈추지 않고 종료되는지 확인하기 위해 필요하다.

---

# 9. Golden Query & Evaluation Set

## 9.1 평가용 Query Set 설계

### [개념]

Golden Query & Evaluation Set은 RAG와 Agent Workflow를 검증하기 위해 미리 정해둔 질문과 기대 결과 세트다.

Golden Query는 Retriever가 예상 문서를 찾는지 확인한다.

Evaluation Set은 Agent가 요구사항에 맞는 결과를 생성하는지 확인한다.

기본 Flow:

```text
Evaluation Query
→ Retriever / Agent Workflow
→ Output
→ Expected Result Compare
```

Golden Query는 검색 평가에 집중하고, Evaluation Set은 Workflow 출력 평가까지 포함한다.

---

### [핵심]

- Golden Query는 Retriever 품질 검증에 사용한다.
- Evaluation Set은 Agent Workflow 품질 검증에 사용한다.
- Query는 실제 사용자 질문 표현을 반영한다.
- Expected Source를 명시한다.
- Expected Behavior를 명시한다.
- Must Not Include를 명시해 잘못된 답변을 차단한다.
- 실패 Query는 문서 보강에 반영한다.
- 문서 수정 후 재평가한다.
- Embedding Model 변경 후 재평가한다.

---

### [실무]

LangChain & LangGraph Golden Query 예시:

| Query                                 | Expected Source                                     |
| ------------------------------------- | --------------------------------------------------- |
| LangChain과 LangGraph 차이는?         | Part01 Core Overview                                |
| Runnable이 뭐야?                      | Part02 Runnable Prompt Model Parser                 |
| Document Loader가 뭐야?               | Part03 Document Retrieval Foundation                |
| RAG Chain은 어떻게 구성해?            | Part04 RAG Chain Retrieval Optimization             |
| Tool Calling이 뭐야?                  | Part05 Tool ToolCalling Agent                       |
| State Schema는 어떻게 설계해?         | Part06 State Node Edge Routing                      |
| Checkpoint와 Memory 차이는?           | Part07 Checkpoint Memory Human ReviewFix            |
| Multi-Agent Workflow는 어떻게 만들어? | Part08 MultiAgent Debugging Testing Troubleshooting |

Evaluation Set 예시:

```json
{
  "query": "개인 AI 개발팀 기본 구조 알려줘",
  "expected_behavior": [
    "PM Agent 중심 구조 설명",
    "Domain Agent 순차 실행 설명",
    "Review Agent 포함",
    "로컬 LLM에서는 순차 실행 권장"
  ],
  "expected_sources": ["Part01 Core Overview", "Part08 MultiAgent"],
  "must_not_include": [
    "모든 Agent 병렬 실행 권장",
    "Review 생략",
    "Human Approval 없이 위험 Tool 실행"
  ]
}
```

평가 기준:

| 항목              | 기준                        |
| ----------------- | --------------------------- |
| Retrieval Hit     | Expected Source 포함        |
| Requirement Match | 요구사항 반영               |
| Grounding         | 문서 근거 기반              |
| No Contradiction  | 이전 Part와 충돌 없음       |
| Output Format     | 요구 형식 준수              |
| Safety            | 위험 작업 자동 실행 금지    |
| Completeness      | 필수 요소 누락 없음         |
| Source Accuracy   | Source가 실제 근거인지 확인 |

---

### [FAQ]

Q. Golden Query와 Evaluation Set은 뭐가 달라?

A.
Golden Query는 검색 품질 검증이고, Evaluation Set은 Agent Workflow 출력 품질 검증이다.

Q. Evaluation Set에는 무엇을 넣어?

A.
사용자 질문, expected behavior, expected source, must_not_include를 넣는 것이 좋다.

Q. 실패한 Query는 어떻게 처리해?

A.
FAQ, Retrieval Queries, Header, Chunk 내용을 보강하고 Re-embedding 후 재평가한다.

Q. 문서 수정 후 Evaluation을 다시 해야 해?

A.
해야 한다. Chunk와 Embedding 결과가 바뀌어 검색 품질이 달라질 수 있다.

Q. must_not_include는 왜 필요해?

A.
Agent가 잘못된 권장사항이나 문서에 없는 내용을 생성하지 않도록 검증하기 위해 필요하다.

---

# 10. Troubleshooting

## 10.1 Multi-Agent Workflow 문제 해결

### [개념]

Multi-Agent Workflow 문제는 Routing, State, Tool, RAG, Review, Loop, Handoff 단계에서 발생할 수 있다.

문제 해결은 실패한 단계를 먼저 분리하는 방식으로 진행한다.

기본 Flow:

```text
Workflow Failure
→ Identify Failed Stage
→ Inspect State
→ Inspect Node Output
→ Fix Rule / Prompt / Tool / Routing
→ Retest
```

Troubleshooting은 감으로 수정하는 것이 아니라 Trace, State, Node Contract, Evaluation 결과를 기준으로 수행한다.

---

### [핵심]

문제:

- 잘못된 Agent로 라우팅됨
- State 필드가 누락됨
- Tool Arguments가 틀림
- RAG 검색 결과가 부정확함
- Review / Fix Loop가 무한 반복됨
- Agent Output이 서로 충돌함
- Final Output이 내부 결과를 반영하지 않음
- 승인 없이 위험 Tool 실행 시도

원인:

- PM Node task_type 판단 오류
- State Schema 불명확
- Node Contract 없음
- Tool Description 모호
- Metadata Filter 오류
- Stop Condition 없음
- Handoff Schema 부족
- Review 기준 불명확
- Approval Path 누락

해결:

- PM Routing Matrix 보강
- State Schema enum 적용
- Node Reads / Writes 정의
- Tool Description 개선
- Golden Query Test 수행
- Max Iteration 추가
- Handoff Schema 구조화
- Review Criteria 고정
- Approval Node 추가

---

### [실무]

Troubleshooting Matrix:

| 증상                | 원인                 | 해결                     |
| ------------------- | -------------------- | ------------------------ |
| 엉뚱한 Agent 실행   | task_type 오류       | PM Prompt, Router Test   |
| State 누락          | Schema 불명확        | State Contract 추가      |
| Tool 실패           | Args 오류            | Args Schema 검증         |
| RAG 실패            | Chunk / Filter 문제  | Golden Query Test        |
| 무한 반복           | Stop Condition 없음  | max_fix_count 추가       |
| Agent 결과 충돌     | Handoff 불명확       | Handoff Schema 적용      |
| Review 누락         | Review Criteria 부족 | Review Checklist 고정    |
| Final 부정확        | Final Node 입력 누락 | Final Node Contract 정의 |
| 위험 Tool 자동 실행 | Approval Path 없음   | Human Approval 추가      |

문제 해결 순서:

```text
1. User Request 확인
2. PM Node Output 확인
3. task_type / required_agents 확인
4. Routing 결과 확인
5. Domain Agent Input 확인
6. RAG Retrieved Context 확인
7. Tool Call / Result 확인
8. Agent Output 확인
9. Handoff 구조 확인
10. Review Findings 확인
11. Final Output 확인
12. Graph Test 재실행
```

단계별 실패 구분:

| 실패 단계    | 확인 대상                                |
| ------------ | ---------------------------------------- |
| PM 실패      | task_type, requirements, required_agents |
| Routing 실패 | Conditional Edge, fallback               |
| RAG 실패     | retrieved_context, metadata_filter       |
| Tool 실패    | tool_args, permission, tool_result       |
| Review 실패  | review_result, findings, severity        |
| Loop 실패    | fix_count, max_fix_count                 |
| Final 실패   | final_output, warnings, sources          |

---

### [FAQ]

Q. Multi-Agent Workflow 문제가 생기면 무엇부터 확인해?

A.
PM Node가 task_type, requirements, required_agents를 올바르게 생성했는지 먼저 확인한다.

Q. 엉뚱한 Agent가 실행되는 이유는?

A.
PM Node의 task_type 판단이나 Router 조건이 잘못되었을 가능성이 높다.

Q. State 필드 누락은 어떻게 막아?

A.
State Schema와 Node Input Output Contract를 명확히 정의하고 Node Test를 수행한다.

Q. Agent 결과가 서로 충돌하면 어떻게 해?

A.
Handoff Schema를 확인하고 Review Agent가 Cross-domain Consistency를 검토하도록 한다.

Q. Final Output이 이상하면 무엇을 봐야 해?

A.
Final Node가 agent_outputs, review_findings, warnings를 제대로 읽고 있는지 확인해야 한다.

---

# 11. Best Practice

## 11.1 LangChain & LangGraph 최종 Best Practice

### [개념]

Best Practice는 LangChain과 LangGraph를 함께 사용해 RAG Agent와 Multi-Agent Workflow를 안정적으로 설계하기 위한 기준이다.

목표는 복잡한 Agent를 한 번에 만드는 것이 아니라 검증 가능한 작은 Workflow에서 시작해 점진적으로 확장하는 것이다.

기본 원칙:

```text
Simple Chain
→ RAG Chain
→ Single Agent
→ Review Loop
→ Multi-Agent Workflow
```

LangChain은 구성 요소 연결에 사용하고, LangGraph는 State 기반 Workflow 제어에 사용한다.

---

### [핵심]

- 단순 Pipeline은 LangChain Runnable로 시작한다.
- 문서 기반 답변은 RAG Chain으로 구성한다.
- 복잡한 Workflow는 LangGraph로 설계한다.
- State Schema를 먼저 정의한다.
- Node 책임을 작게 유지한다.
- Conditional Edge에는 fallback을 둔다.
- Review / Fix Loop에는 Max Iteration을 둔다.
- Tool Arguments는 실행 전 검증한다.
- 위험 Tool은 Human Approval을 거친다.
- Checkpoint로 긴 Workflow를 복구 가능하게 한다.
- Retriever는 Golden Query로 검증한다.
- Review Agent로 최종 결과를 검증한다.
- 민감정보는 State, Memory, Checkpoint, Trace에 저장하지 않는다.

---

### [실무]

권장 구축 순서:

| 단계 | 구축 대상                              |
| ---- | -------------------------------------- |
| 1    | Prompt → Model → Parser Pipeline       |
| 2    | Document Loader → Splitter → Retriever |
| 3    | RAG Chain                              |
| 4    | RAG Evaluation                         |
| 5    | Tool Calling                           |
| 6    | Single Agent                           |
| 7    | LangGraph State / Node / Edge          |
| 8    | Review / Fix Loop                      |
| 9    | Human Approval                         |
| 10   | Multi-Agent Workflow                   |
| 11   | Debugging / Tracing                    |
| 12   | Full Graph Testing                     |

운영 기준:

- 작은 Graph부터 시작한다.
- 모든 Node의 입출력을 기록한다.
- RAG Source를 유지한다.
- Agent Output은 구조화한다.
- Error Path를 반드시 둔다.
- Approval Path를 반드시 둔다.
- 권한 없는 Side Effect를 금지한다.
- 테스트 가능한 부분은 LLM 없이 테스트한다.
- 비결정적 LLM 출력은 exact match로 테스트하지 않는다.
- 변경 후 Golden Query와 Graph Test를 반복한다.

최종 구조 기준:

```text
START
→ PM Node
→ Domain Agent Node
→ Review Node
→ Fix Node if needed
→ Final Node
→ END
```

확장 구조 기준:

```text
START
→ PM Node
→ SQL Node
→ Backend Node
→ Frontend Node
→ DevOps Node if needed
→ AI Node if needed
→ Review Node
→ Fix Node if needed
→ Final Node
→ END
```

---

### [FAQ]

Q. LangChain과 LangGraph를 어떻게 같이 쓰는 게 좋아?

A.
LangChain은 RAG Chain과 Tool Chain에 쓰고, LangGraph는 State 기반 Workflow와 Multi-Agent 제어에 쓰는 것이 좋다.

Q. 처음부터 Multi-Agent를 만들면 좋아?

A.
권장하지 않는다. 단순 Chain, RAG Chain, Single Agent, Review Loop 순서로 확장하는 것이 안정적이다.

Q. LangGraph 설계에서 가장 중요한 것은?

A.
State Schema, Node 책임 분리, Conditional Edge, Error Path, Stop Condition이다.

Q. RAG 품질은 어떻게 유지해?

A.
Golden Query, Retrieval Evaluation, Source 검증, 문서 수정 후 Re-embedding으로 유지한다.

Q. Agent Workflow 운영에서 가장 중요한 안전 기준은?

A.
Tool 권한 제한, Human Approval, 민감정보 저장 금지, Review Agent 검증이다.

---

# 12. Final Integration Checklist

## 12.1 Part01~Part08 연계 검수

### [Checklist]

- [ ] Part01이 LangChain과 LangGraph 역할 차이를 설명하는가?
- [ ] Part02가 Runnable, Prompt, Model, Parser 기반 Pipeline을 설명하는가?
- [ ] Part03이 Document Loader, Splitter, Embedding, Retriever 기반을 설명하는가?
- [ ] Part04가 RAG Chain과 Retrieval Optimization을 설명하는가?
- [ ] Part05가 Tool, Tool Calling, Agent 구조를 설명하는가?
- [ ] Part06이 State, Node, Edge, Routing을 설명하는가?
- [ ] Part07이 Checkpoint, Memory, Human Approval, Review / Fix를 설명하는가?
- [ ] Part08이 Multi-Agent, Debugging, Testing, Troubleshooting을 통합하는가?
- [ ] LangChain은 구성 요소 연결 Framework로 일관되게 설명되는가?
- [ ] LangGraph는 State 기반 Workflow Framework로 일관되게 설명되는가?
- [ ] State, Memory, Checkpoint 용어가 혼동되지 않는가?
- [ ] RAG 검색과 답변 생성 단계가 구분되는가?
- [ ] Tool 권한과 Human Approval 기준이 일관되는가?
- [ ] Review / Fix Loop에 Max Iteration 기준이 있는가?
- [ ] Multi-Agent 구조에서 PM Agent가 Routing을 담당하는가?
- [ ] 모든 Agent Output은 Review Agent 검증 대상인가?
- [ ] Debugging과 Testing 기준이 실제 Workflow 단계와 연결되는가?
- [ ] Golden Query와 Evaluation Set이 문서 품질 개선에 연결되는가?
- [ ] 민감정보 저장 금지 기준이 State, Memory, Checkpoint, Trace에 적용되는가?
- [ ] 개인 AI 개발팀 구조와 로컬 LLM 순차 실행 기준이 반영되는가?

---

# 13. Part08 Checklist

## 13.1 Multi-Agent Debugging Testing Checklist

### [Checklist]

- [ ] Multi-Agent Workflow에서 Agent 역할이 분리되었는가?
- [ ] PM Agent가 요청 분석과 라우팅을 담당하는가?
- [ ] 모든 요청을 모든 Agent에게 보내지 않는가?
- [ ] Domain Agent 책임 범위가 명확한가?
- [ ] Review Agent가 최종 결과를 검증하는가?
- [ ] Fix Agent가 Review Findings를 기준으로 수정하는가?
- [ ] Final Agent가 사용자용 결과를 정리하는가?
- [ ] 로컬 LLM 환경에서 순차 실행을 우선하는가?
- [ ] Agent Handoff Schema가 정의되어 있는가?
- [ ] Handoff에 Source, Assumption, Open Issue가 포함되는가?
- [ ] Cross-domain Consistency 검토 기준이 있는가?
- [ ] Workflow Debugging 대상이 정의되어 있는가?
- [ ] Node Input / Output / State Update를 추적하는가?
- [ ] Tool Call Arguments와 Result를 추적하는가?
- [ ] Retrieved Context와 Source를 추적하는가?
- [ ] Trace ID와 Thread ID를 구분해 사용하는가?
- [ ] Trace에 민감정보를 저장하지 않는가?
- [ ] Prompt, Retriever, Parser, Tool, Node, Router를 분리 테스트하는가?
- [ ] Graph Test로 START부터 END까지 검증하는가?
- [ ] Error Path를 테스트하는가?
- [ ] Approval Path를 테스트하는가?
- [ ] Loop Stop Condition을 테스트하는가?
- [ ] Golden Query와 Evaluation Set을 관리하는가?
- [ ] 문서 수정 후 Re-embedding과 재평가를 수행하는가?
- [ ] Best Practice 기준을 전체 Part와 일관되게 유지하는가?

---

# Retrieval Queries

### [FAQ]

Q. Multi-Agent Workflow가 뭐야?
A. 여러 Agent를 역할별 Node로 나누고 State와 Edge로 실행 흐름을 제어하는 구조다.

Q. Multi-Agent는 여러 LLM을 동시에 호출하는 거야?
A. 아니다. 핵심은 역할 분리, State 공유, Routing, Review / Fix Workflow다.

Q. PM Agent는 왜 필요해?
A. 사용자 요청을 분석하고 필요한 Agent만 선택해 불필요한 실행과 결과 충돌을 줄이기 위해 필요하다.

Q. Review Agent는 왜 필요해?
A. Domain Agent 결과의 요구사항 충족, 문서 근거, 코드 정확성, 누락, 위험 요소를 검증하기 위해 필요하다.

Q. 처음부터 모든 Agent를 만들어야 해?
A. 권장하지 않는다. PM, Domain, Review 중심으로 시작하고 점진적으로 확장하는 것이 좋다.

Q. 개인 AI 개발팀 구조는 뭐야?
A. 사용자가 PM Agent에게 요청하면 PM이 작업을 분해하고 Domain Agent와 Review Agent가 순차적으로 처리하는 구조다.

Q. 사용자는 모든 Agent에게 직접 요청해야 해?
A. 아니다. 사용자는 PM Agent에게만 요청하고 내부 Routing은 PM Agent가 담당하는 구조가 좋다.

Q. 로컬 LLM 환경에서 병렬 실행이 좋아?
A. 대부분은 순차 실행이 더 현실적이다. RAM, 응답 속도, Context 관리 제약을 고려해야 한다.

Q. Domain Agent는 RAG를 어떻게 써?
A. 자신의 Domain에 맞는 Metadata Filter로 관련 RAG 문서를 검색해 근거로 사용한다.

Q. Final Agent는 무엇을 해?
A. 내부 Agent 결과와 Review 결과를 사용자에게 필요한 최종 응답으로 정리한다.

Q. Handoff가 뭐야?
A. 한 Agent의 결과를 다음 Agent가 사용할 수 있는 구조로 전달하는 과정이다.

Q. Handoff를 구조화해야 하는 이유는?
A. 다음 Agent가 요구사항, 결과, Source, 가정, 남은 문제를 명확히 이해해야 하기 때문이다.

Q. Handoff에 Source가 필요한 이유는?
A. Review Agent가 결과의 문서 근거를 검증할 수 있게 하기 위해 필요하다.

Q. assumptions는 왜 분리해?
A. 사실과 가정을 구분하지 않으면 다음 Agent가 추측을 확정된 정보로 사용할 수 있기 때문이다.

Q. Handoff 실패는 어떤 문제를 만들 수 있어?
A. Agent 간 요구사항 누락, 결과 충돌, 잘못된 구현, Review 실패를 만들 수 있다.

Q. Cross-domain Consistency가 뭐야?
A. 여러 Domain Agent 결과가 서로 충돌하지 않고 연결 지점이 일치하는지 검토하는 기준이다.

Q. 왜 도메인 간 일관성 검토가 필요해?
A. 각 Agent가 자기 Domain만 보고 작업하면 API, DTO, DB, 설정 간 불일치가 생길 수 있기 때문이다.

Q. Backend와 Frontend는 무엇을 맞춰야 해?
A. API URL, HTTP Method, Request Body, Response DTO, 인증 헤더를 맞춰야 한다.

Q. SQL과 Backend는 무엇을 맞춰야 해?
A. 테이블명, 컬럼명, 데이터 타입, 관계, 제약조건, Entity 매핑을 맞춰야 한다.

Q. Cross-domain 문제는 누가 찾는 게 좋아?
A. Review Agent가 전체 Agent Output과 Handoff를 기준으로 검토하는 것이 좋다.

Q. Workflow Debugging이 뭐야?
A. Agent Workflow의 State, Node, Tool, RAG, Routing, Review 결과를 단계별로 추적하는 과정이다.

Q. Agent Workflow는 왜 디버깅이 어려워?
A. LLM 응답, Tool 실행, RAG 검색, State Update, 조건 분기가 함께 발생하기 때문이다.

Q. 가장 먼저 확인할 것은?
A. PM Node가 task_type, requirements, required_agents를 올바르게 생성했는지 확인한다.

Q. RAG Node 디버깅은 무엇을 확인해?
A. query, metadata_filter, retrieved_context, source, missing_context를 확인한다.

Q. 로그에 남기면 안 되는 것은?
A. API Key, Token, 비밀번호, Secret, 개인정보, 민감한 파일 원문 전체는 로그에 남기면 안 된다.

Q. Tracing이 뭐야?
A. Workflow 실행 과정을 시간 순서대로 기록해 Node, Tool, RAG, Review 흐름을 추적하는 방식이다.

Q. Trace ID는 왜 필요해?
A. 하나의 Workflow 실행을 식별하고 관련 로그를 연결하기 위해 필요하다.

Q. Trace ID와 Thread ID는 달라?
A. 다르다. Trace ID는 실행 추적용이고 Thread ID는 Checkpoint 재개 대상 식별용이다.

Q. Debugging과 Tracing은 뭐가 달라?
A. Debugging은 원인 분석이고, Tracing은 실행 흐름 전체 기록과 추적에 가깝다.

Q. Trace에는 무엇을 기록해?
A. Node 이름, 실행 시간, 입력 요약, 출력 요약, Tool Call, Retriever 결과, Error 위치를 기록한다.

Q. Trace에 Prompt 전체를 저장해도 돼?
A. 권장하지 않는다. 민감정보와 보안 위험이 있어 요약 저장을 우선한다.

Q. Agent Workflow 테스트는 어떻게 해?
A. Prompt, Retriever, Parser, Tool, Node, Router, Graph를 분리해 테스트한다.

Q. 모든 테스트에서 실제 LLM을 호출해도 돼?
A. 권장하지 않는다. 비용과 비결정성 때문에 Mock, Stub, Golden Query를 우선 사용한다.

Q. Router Test는 무엇을 확인해?
A. task_type, review_result, error_type 같은 State 값에 따라 올바른 Node로 이동하는지 확인한다.

Q. Node Test는 무엇을 확인해?
A. 입력 State를 받아 예상 State Update를 반환하는지 확인한다.

Q. Loop Test는 왜 필요해?
A. Review / Fix Loop, Tool Calling Loop, Retry Loop가 무한 반복되지 않는지 확인하기 위해 필요하다.

Q. Graph Testing이 뭐야?
A. LangGraph Workflow가 START에서 END까지 올바른 State 전이를 수행하는지 검증하는 테스트다.

Q. Graph Test는 Node Test와 뭐가 달라?
A. Node Test는 개별 Node 검증이고, Graph Test는 Node, Edge, Routing, Loop를 함께 검증한다.

Q. Graph Test에서 무엇을 확인해?
A. Routing 경로, State Update, Error Path, Approval Path, Loop 종료, Final State를 확인한다.

Q. 위험 Tool은 Graph Test에서 어떻게 처리해?
A. 실제 실행하지 않고 Mock이나 dry-run으로 대체한다.

Q. Graph Test에서 END 경로를 확인해야 하는 이유는?
A. Workflow가 무한 반복되거나 중간에 멈추지 않고 종료되는지 확인하기 위해 필요하다.

Q. Golden Query와 Evaluation Set은 뭐가 달라?
A. Golden Query는 검색 품질 검증이고, Evaluation Set은 Agent Workflow 출력 품질 검증이다.

Q. Evaluation Set에는 무엇을 넣어?
A. 사용자 질문, expected behavior, expected source, must_not_include를 넣는 것이 좋다.

Q. 실패한 Query는 어떻게 처리해?
A. FAQ, Retrieval Queries, Header, Chunk 내용을 보강하고 Re-embedding 후 재평가한다.

Q. 문서 수정 후 Evaluation을 다시 해야 해?
A. 해야 한다. Chunk와 Embedding 결과가 바뀌어 검색 품질이 달라질 수 있다.

Q. must_not_include는 왜 필요해?
A. Agent가 잘못된 권장사항이나 문서에 없는 내용을 생성하지 않도록 검증하기 위해 필요하다.

Q. Multi-Agent Workflow 문제가 생기면 무엇부터 확인해?
A. PM Node가 task_type, requirements, required_agents를 올바르게 생성했는지 먼저 확인한다.

Q. 엉뚱한 Agent가 실행되는 이유는?
A. PM Node의 task_type 판단이나 Router 조건이 잘못되었을 가능성이 높다.

Q. State 필드 누락은 어떻게 막아?
A. State Schema와 Node Input Output Contract를 명확히 정의하고 Node Test를 수행한다.

Q. Agent 결과가 서로 충돌하면 어떻게 해?
A. Handoff Schema를 확인하고 Review Agent가 Cross-domain Consistency를 검토하도록 한다.

Q. Final Output이 이상하면 무엇을 봐야 해?
A. Final Node가 agent_outputs, review_findings, warnings를 제대로 읽고 있는지 확인해야 한다.

Q. LangChain과 LangGraph를 어떻게 같이 쓰는 게 좋아?
A. LangChain은 RAG Chain과 Tool Chain에 쓰고, LangGraph는 State 기반 Workflow와 Multi-Agent 제어에 쓰는 것이 좋다.

Q. 처음부터 Multi-Agent를 만들면 좋아?
A. 권장하지 않는다. 단순 Chain, RAG Chain, Single Agent, Review Loop 순서로 확장하는 것이 안정적이다.

Q. LangGraph 설계에서 가장 중요한 것은?
A. State Schema, Node 책임 분리, Conditional Edge, Error Path, Stop Condition이다.

Q. RAG 품질은 어떻게 유지해?
A. Golden Query, Retrieval Evaluation, Source 검증, 문서 수정 후 Re-embedding으로 유지한다.

Q. Agent Workflow 운영에서 가장 중요한 안전 기준은?
A. Tool 권한 제한, Human Approval, 민감정보 저장 금지, Review Agent 검증이다.

Q. Part08의 역할은 뭐야?
A. Part01~Part07의 LangChain, RAG, Tool, State, Checkpoint, Review 개념을 Multi-Agent 운영과 검증 기준으로 통합하는 것이다.
