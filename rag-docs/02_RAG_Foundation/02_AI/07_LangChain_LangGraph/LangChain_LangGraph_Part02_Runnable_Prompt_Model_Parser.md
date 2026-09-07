# LangChain & LangGraph Part02 Runnable Prompt Model Parser

---

# 1. Runnable Core

## 1.1 Runnable 기본 개념

### [개념]

Runnable은 LangChain에서 실행 가능한 구성 단위다.

Runnable은 입력을 받아 처리하고 출력을 반환한다.

Prompt Template, Chat Model, Output Parser, Retriever, Tool은 Runnable처럼 연결될 수 있다.

기본 구조:

```text
Input
→ Runnable
→ Output
```

Runnable Pipeline:

```text
Runnable A
→ Runnable B
→ Runnable C
→ Result
```

LangChain의 현대적 구조는 Runnable 중심으로 이해하는 것이 적합하다.

---

### [핵심]

- Runnable은 입력을 받아 출력을 반환하는 실행 단위다.
- Prompt Template은 Prompt를 생성하는 Runnable로 볼 수 있다.
- Chat Model은 Prompt를 받아 LLM 응답을 생성하는 Runnable로 볼 수 있다.
- Output Parser는 LLM 응답을 원하는 형식으로 변환하는 Runnable로 볼 수 있다.
- Runnable은 `invoke`, `batch`, `stream` 방식으로 실행할 수 있다.
- Runnable은 pipe 구조로 연결할 수 있다.
- Runnable 연결 시 input / output 타입을 명확히 해야 한다.

---

### [실무]

2026 실무 기준 LangChain Pipeline은 Runnable 조합으로 설계한다.

기본 실행 방식:

| 실행 방식        | 목적                |
| ---------------- | ------------------- |
| invoke           | 단일 입력 실행      |
| batch            | 여러 입력 일괄 처리 |
| stream           | Streaming 출력 처리 |
| pipe             | Runnable 연결       |
| RunnableSequence | 순차 Pipeline 구성  |

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
→ Retrieved Documents
→ Prompt Template
→ Chat Model
→ Output Parser
→ Grounded Answer
```

Runnable 설계 기준:

- 각 Runnable의 입력 타입을 명확히 한다.
- 각 Runnable의 출력 타입을 명확히 한다.
- 중간 출력 형식이 다음 Runnable 입력과 맞는지 확인한다.
- 긴 Pipeline은 중간 결과 로깅을 추가한다.
- Parser 실패 가능성을 고려한다.

---

### [FAQ]

Q. Runnable이 뭐야?

A.
Runnable은 입력을 받아 출력을 만드는 LangChain의 실행 가능한 구성 단위다.

Q. Runnable은 왜 중요해?

A.
Prompt, Model, Parser, Retriever를 일관된 방식으로 연결해 Pipeline을 만들 수 있기 때문이다.

Q. invoke는 뭐야?

A.
단일 입력을 Runnable에 넣어 한 번 실행하는 방식이다.

Q. batch는 뭐야?

A.
여러 입력을 한 번에 처리하는 실행 방식이다.

Q. stream은 뭐야?

A.
LLM 응답이나 Pipeline 결과를 부분적으로 출력하는 실행 방식이다.

Q. Runnable 연결에서 가장 중요한 것은?

A.
이전 Runnable의 출력이 다음 Runnable의 입력 형식과 맞는지 확인하는 것이다.

---

# 2. Runnable Pipeline

## 2.1 RunnableSequence 구조

### [개념]

RunnableSequence는 여러 Runnable을 순서대로 연결한 Pipeline이다.

기본 Flow:

```text
Input
→ Runnable 1
→ Runnable 2
→ Runnable 3
→ Output
```

RunnableSequence는 정해진 순서로 실행되는 작업에 적합하다.

예시:

```text
Question
→ Prompt Template
→ Chat Model
→ String Parser
→ Answer
```

---

### [핵심]

- RunnableSequence는 순차 실행 Pipeline이다.
- Chain 구조를 Runnable 기반으로 표현할 수 있다.
- 입력과 출력 형식이 명확해야 재사용 가능하다.
- 요약, 분류, 변환, RAG 답변 생성에 적합하다.
- 복잡한 조건 분기와 반복은 LangGraph가 더 적합하다.

---

### [실무]

RunnableSequence 적용 대상:

| 작업      | 적용 방식                                        |
| --------- | ------------------------------------------------ |
| 문장 요약 | Text → Prompt → Model → Parser                   |
| 문서 분류 | Text → Prompt → Model → Label Parser             |
| JSON 생성 | Input → Prompt → Model → JSON Parser             |
| RAG 답변  | Query → Retriever → Prompt → Model → Parser      |
| 코드 리뷰 | Code → Review Prompt → Model → Structured Parser |

RunnableSequence 예시 구조:

```text
input: {"question": "LangChain이 뭐야?"}

Prompt Template:
"질문에 답변하라: {question}"

→ Chat Model

→ Output Parser

output:
"LangChain은 LLM Application 구성 요소를 연결하는 Framework다."
```

주의할 점:

- Prompt Template 변수 누락 금지
- Model 응답 형식 불안정 가능성 고려
- Parser가 요구하는 형식을 Prompt에 명확히 지정
- 긴 Chain은 Debugging 포인트 추가
- 실패 시 Retry 또는 Fallback 설계

---

### [FAQ]

Q. RunnableSequence가 뭐야?

A.
여러 Runnable을 순서대로 연결해 실행하는 Pipeline 구조다.

Q. RunnableSequence는 언제 써?

A.
요약, 분류, 변환, RAG 답변처럼 순차 흐름이 명확한 작업에 사용한다.

Q. RunnableSequence와 Chain은 같은 거야?

A.
현대 LangChain에서는 Chain을 Runnable 기반 Pipeline으로 이해하는 것이 적합하다.

Q. RunnableSequence가 복잡한 Agent Workflow에 적합해?

A.
조건 분기, 반복, Review / Fix Loop가 필요하면 LangGraph가 더 적합하다.

Q. RunnableSequence 디버깅은 어떻게 해?

A.
각 Runnable의 input, output, Parser 결과를 단계별로 확인한다.

---

# 3. Prompt Template

## 3.1 Prompt Template 기본 개념

### [개념]

Prompt Template은 입력 변수를 Prompt로 변환하는 구성 요소다.

Prompt Template은 반복되는 Prompt 구조를 안정화한다.

기본 구조:

```text
System:
You are a Backend Agent.

Context:
{context}

User Question:
{question}
```

Prompt Template은 정적 지시문과 동적 입력 변수를 분리한다.

RAG에서는 retrieved context와 user question을 명확히 분리해야 한다.

---

### [핵심]

- Prompt Template은 반복 Prompt를 구조화한다.
- 입력 변수를 사용해 동적 값을 주입한다.
- System Message와 User Message를 분리한다.
- RAG Prompt는 Context와 Question을 분리한다.
- Template 변수 누락을 검증해야 한다.
- 사용자 입력을 System Prompt에 직접 넣지 않는다.
- Placeholder 이름은 명확해야 한다.

---

### [실무]

Prompt Template 구성 요소:

| 요소                | 목적                          |
| ------------------- | ----------------------------- |
| System Message      | Agent 역할, 규칙, 제약 정의   |
| User Message        | 실제 사용자 요청              |
| Context             | RAG 검색 문서                 |
| Variables           | 동적 입력 값                  |
| Placeholder         | 대화 기록 또는 문서 삽입 위치 |
| Partial Variable    | 고정 값 사전 주입             |
| Template Validation | 변수 누락 검증                |

RAG Prompt 기본 구조:

```text
System:
너는 문서 기반으로 답변하는 RAG Agent다.
문서에 없는 내용은 없다고 답하라.

Context:
{context}

Question:
{question}

Answer:
```

Agent Prompt 기본 구조:

```text
System:
너는 Backend Agent다.
Spring Boot, JPA, Security 기준으로 답변하라.
위험한 작업은 실행하지 말고 사용자 승인을 요청하라.

Task:
{task}

Available Tools:
{tools}

Current State:
{state}
```

---

### [FAQ]

Q. Prompt Template이 뭐야?

A.
입력 변수를 Prompt 구조에 주입해 반복 가능한 Prompt를 만드는 구성 요소다.

Q. Prompt Template은 왜 필요해?

A.
Prompt 구조를 안정화하고, 입력 변수를 명확히 관리하기 위해 필요하다.

Q. RAG Prompt에서 Context와 Question을 분리해야 하는 이유는?

A.
문서 근거와 사용자 질문을 구분해야 LLM이 문서 기반으로 답변하기 쉽기 때문이다.

Q. 사용자 입력을 System Prompt에 넣어도 돼?

A.
권장하지 않는다. 사용자 입력은 User Message나 Question 영역에 넣어야 한다.

Q. Template Validation은 왜 필요해?

A.
필수 변수가 누락되면 Chain 실행 중 오류가 발생하기 때문이다.

---

# 4. Chat Prompt Template

## 4.1 Chat Message 구조

### [개념]

Chat Prompt Template은 Chat Model에 전달할 메시지 목록을 구성하는 Prompt Template이다.

Chat Model은 일반 문자열보다 역할이 구분된 Message 구조를 사용한다.

기본 구조:

```text
System Message
→ Human Message
→ AI Message
→ Human Message
```

대표 메시지 역할:

| Message        | 역할                            |
| -------------- | ------------------------------- |
| System Message | 모델의 역할과 규칙 설정         |
| Human Message  | 사용자 입력                     |
| AI Message     | 이전 모델 응답                  |
| Tool Message   | Tool 실행 결과                  |
| Placeholder    | 대화 기록 또는 동적 메시지 삽입 |

---

### [핵심]

- Chat Prompt Template은 Chat Model용 메시지 구조를 만든다.
- System Message는 역할과 제약을 정의한다.
- Human Message는 사용자 요청을 전달한다.
- Tool Message는 Tool 실행 결과를 전달한다.
- Placeholder는 대화 기록이나 동적 메시지를 삽입한다.
- 메시지 역할을 섞으면 응답 품질이 낮아질 수 있다.

---

### [실무]

Chat Prompt Template 권장 구조:

```text
System:
너는 개인 AI 개발팀의 PM Agent다.
요청을 분석하고 필요한 Domain Agent로 라우팅하라.

Messages:
{messages}

Current State:
{state}

User Request:
{user_request}
```

RAG Chat Prompt Template 권장 구조:

```text
System:
너는 RAG Agent다.
반드시 Context에 근거해 답변하라.
문서에 없으면 없다고 답하라.

Context:
{context}

Human:
{question}
```

Review Agent Chat Prompt Template:

```text
System:
너는 Review Agent다.
요구사항 충족, 코드 정확성, 보안 위험, 누락을 검토하라.
결과는 pass/fail과 findings로 반환하라.

Requirements:
{requirements}

Draft Output:
{draft_output}
```

주의:

- System Message에 사용자 원문을 직접 삽입하지 않는다.
- Context에는 검색된 문서만 넣는다.
- Question에는 사용자 질문만 넣는다.
- Tool Result는 Tool Message 또는 Observation 영역에 넣는다.
- 이전 대화 전체를 무조건 넣지 않는다.

---

### [FAQ]

Q. Chat Prompt Template이 뭐야?

A.
Chat Model에 전달할 System, Human, AI, Tool Message 구조를 만드는 Template이다.

Q. System Message는 무엇을 넣어?

A.
Agent 역할, 답변 규칙, 금지 사항, 출력 형식 같은 상위 지시를 넣는다.

Q. Human Message는 무엇을 넣어?

A.
사용자의 실제 질문이나 작업 요청을 넣는다.

Q. Tool Message는 무엇을 넣어?

A.
Tool 실행 결과나 Observation을 넣는다.

Q. Placeholder는 언제 써?

A.
대화 기록, 중간 메시지, 동적 메시지 목록을 삽입할 때 사용한다.

---

# 5. Chat Model

## 5.1 Chat Model 기본 개념

### [개념]

Chat Model은 Prompt 또는 Message를 입력받아 LLM 응답을 생성하는 구성 요소다.

Chat Model은 실제 LLM Provider 또는 Local LLM과 연결된다.

Chat Model은 LangChain Pipeline에서 Prompt Template 다음에 위치한다.

기본 Flow:

```text
Prompt Template
→ Chat Model
→ LLM Response
```

Chat Model은 LLM 자체라기보다 LLM 호출 인터페이스다.

---

### [핵심]

- Chat Model은 Prompt를 받아 답변을 생성한다.
- API LLM과 Local LLM을 구분해야 한다.
- Provider별 설정과 응답 구조가 다를 수 있다.
- Temperature는 응답의 창의성과 일관성에 영향을 준다.
- 개발, 리뷰, RAG 작업은 낮은 Temperature가 적합하다.
- Timeout과 Retry 정책이 필요하다.
- Streaming이 필요한 경우 stream 실행 방식을 고려한다.

---

### [실무]

Chat Model 설정 요소:

| 설정        | 목적                         |
| ----------- | ---------------------------- |
| model       | 사용할 모델명                |
| provider    | OpenAI, Anthropic, Ollama 등 |
| temperature | 출력 다양성 조절             |
| max_tokens  | 최대 출력 길이 제한          |
| timeout     | 응답 대기 시간 제한          |
| retry       | 일시적 실패 재시도           |
| streaming   | 토큰 단위 출력               |
| base_url    | Local LLM 또는 Proxy 연결    |
| api_key     | API 인증 정보                |

작업별 Temperature 기준:

| 작업          | 권장 Temperature |
| ------------- | ---------------- |
| 코드 생성     | 낮음             |
| 코드 리뷰     | 낮음             |
| RAG 답변      | 낮음             |
| JSON 출력     | 낮음             |
| 아이디어 발산 | 중간             |
| 창작 글쓰기   | 중간 이상        |

Local LLM 실무 기준:

- 하드웨어 제약을 고려한다.
- Context Window를 확인한다.
- 응답 속도와 품질을 테스트한다.
- Model 변경 시 Prompt와 Parser를 재검증한다.
- Embedding Model과 Chat Model 역할을 분리한다.

---

### [FAQ]

Q. Chat Model이 뭐야?

A.
Prompt 또는 Message를 입력받아 LLM 응답을 생성하는 LangChain 구성 요소다.

Q. Chat Model은 LLM 자체야?

A.
정확히는 LLM을 호출하는 인터페이스로 이해하는 것이 적합하다.

Q. Local LLM과 API LLM은 뭐가 달라?

A.
Local LLM은 내 서버에서 실행되고, API LLM은 외부 Provider API를 호출한다.

Q. RAG 작업에서 Temperature는 낮게 해야 해?

A.
권장한다. 문서 기반 답변은 일관성과 정확성이 중요하기 때문이다.

Q. Chat Model 설정에서 Timeout이 왜 필요해?

A.
LLM 응답 지연이나 장애가 전체 Workflow를 멈추지 않게 하기 위해 필요하다.

---

# 6. Output Parser

## 6.1 Output Parser 기본 개념

### [개념]

Output Parser는 LLM 응답을 원하는 형식으로 변환하거나 검증하는 구성 요소다.

기본 Flow:

```text
LLM Response
→ Output Parser
→ Structured Result
→ Validation
```

Output Parser는 문자열, JSON, Pydantic Schema, Structured Output 처리에 사용된다.

Output Parser는 형식을 안정화하지만 내용의 정확성을 보장하지는 않는다.

---

### [핵심]

- Output Parser는 LLM 응답 형식을 안정화한다.
- String Parser는 일반 텍스트 출력에 사용한다.
- JSON Parser는 JSON 응답 파싱에 사용한다.
- Pydantic Parser는 Schema 기반 검증에 사용한다.
- Structured Output은 Agent 간 Handoff에 유용하다.
- Parse Error 처리가 필요하다.
- Parser 실패 시 Retry 또는 Fallback을 설계한다.

---

### [실무]

Output Parser 종류:

| Parser            | 목적                 |
| ----------------- | -------------------- |
| String Parser     | 문자열 답변 반환     |
| JSON Parser       | JSON 구조 반환       |
| Pydantic Parser   | Schema 기반 검증     |
| List Parser       | 목록 구조 반환       |
| Enum Parser       | 제한된 선택지 반환   |
| Structured Output | Agent Handoff 구조화 |

Review Agent 출력 예시:

```json
{
  "result": "fail",
  "severity": "critical",
  "findings": [
    "JWT 검증 로직 설명이 누락됨",
    "Refresh Token 만료 처리 기준이 없음"
  ],
  "next_action": "fix"
}
```

PM Agent Routing 출력 예시:

```json
{
  "task_type": "backend",
  "required_agents": ["backend", "review"],
  "requirements": [
    "Spring Security JWT 인증 흐름 설명",
    "Controller-Service-Repository 책임 분리"
  ]
}
```

Parser 실패 처리 Flow:

```text
LLM Response
→ Parser
→ Parse Error
→ Retry with Format Instruction
→ Fallback or Error Node
```

---

### [FAQ]

Q. Output Parser가 뭐야?

A.
LLM 응답을 문자열, JSON, Schema 같은 원하는 형식으로 변환하거나 검증하는 구성 요소다.

Q. Output Parser는 왜 필요해?

A.
LLM 응답을 안정적인 데이터 구조로 바꿔 Chain이나 Graph에서 사용하기 위해 필요하다.

Q. Parser가 내용 정확성도 보장해?

A.
아니다. Parser는 형식을 검증하지만 내용의 사실성이나 정확성은 별도 검토가 필요하다.

Q. JSON Parser는 언제 써?

A.
Agent Routing, Review 결과, Tool Arguments처럼 구조화된 결과가 필요할 때 사용한다.

Q. Parse Error는 어떻게 처리해?

A.
형식 지시를 강화해 재요청하거나 fallback 또는 Error Node로 이동한다.

---

# 7. Structured Output

## 7.1 Schema 기반 출력

### [개념]

Structured Output은 LLM 응답을 미리 정의한 Schema에 맞게 생성하도록 만드는 방식이다.

Structured Output은 Agent Workflow에서 결과 전달 형식을 안정화하는 데 중요하다.

기본 구조:

```text
Prompt
→ Chat Model
→ Structured Output
→ Schema Validation
→ State Update
```

Structured Output은 PM Agent, Review Agent, Router Node, Tool Calling 결과에 유용하다.

---

### [핵심]

- Structured Output은 LLM 결과를 구조화한다.
- Schema는 출력 필드와 타입을 정의한다.
- Agent 간 Handoff 형식을 안정화한다.
- Router 결과를 State에 저장하기 쉽다.
- Review 결과를 pass/fail 형식으로 관리하기 쉽다.
- Schema가 너무 복잡하면 실패 가능성이 증가한다.
- 필수 필드와 선택 필드를 구분해야 한다.

---

### [실무]

PM Agent Output Schema:

```json
{
  "task_type": "backend",
  "priority": "high",
  "required_agents": ["backend", "review"],
  "requirements": ["JWT 인증 흐름 구현", "예외 처리 기준 포함"],
  "needs_human_approval": false
}
```

Review Agent Output Schema:

```json
{
  "result": "pass",
  "severity": "none",
  "findings": [],
  "fix_required": false
}
```

Error Output Schema:

```json
{
  "status": "error",
  "error_type": "parser_error",
  "message": "LLM output is not valid JSON",
  "retryable": true
}
```

Structured Output 설계 기준:

- 필드명은 명확하게 작성한다.
- enum 값은 제한한다.
- nullable 필드를 최소화한다.
- Agent별 출력 Schema를 분리한다.
- State 필드와 매핑 가능한 구조로 만든다.

---

### [FAQ]

Q. Structured Output이 뭐야?

A.
LLM 응답을 미리 정한 Schema에 맞게 구조화해서 반환하는 방식이다.

Q. Structured Output은 언제 필요해?

A.
Routing, Review, Tool Calling, Agent Handoff처럼 결과 형식이 중요할 때 필요하다.

Q. Schema가 복잡해도 괜찮아?

A.
너무 복잡하면 LLM이 형식을 지키지 못할 가능성이 증가한다.

Q. Review Agent 출력은 왜 구조화해야 해?

A.
pass/fail, findings, severity, next_action을 State에 안정적으로 저장하기 위해 필요하다.

Q. Structured Output과 Output Parser는 같은 거야?

A.
관련은 있지만 다르다. Structured Output은 구조화된 응답 생성 방식이고, Output Parser는 응답을 파싱하고 검증하는 구성 요소다.

---

# 8. Prompt-Model-Parser Pipeline

## 8.1 기본 Pipeline 설계

### [개념]

Prompt-Model-Parser Pipeline은 LangChain의 가장 기본적인 실행 구조다.

기본 Flow:

```text
Input
→ Prompt Template
→ Chat Model
→ Output Parser
→ Output
```

이 구조는 요약, 분류, 답변 생성, JSON 생성, 코드 리뷰에 활용된다.

---

### [핵심]

- Prompt Template은 입력을 Prompt로 변환한다.
- Chat Model은 Prompt를 받아 응답을 생성한다.
- Output Parser는 응답을 원하는 형식으로 변환한다.
- Pipeline 입력과 출력 타입을 명확히 한다.
- Parser가 필요한 작업은 Prompt에 출력 형식을 명시한다.
- 실패 시 Retry 또는 Fallback이 필요하다.

---

### [실무]

요약 Pipeline:

```text
Document
→ Summary Prompt
→ Chat Model
→ String Parser
→ Summary
```

분류 Pipeline:

```text
User Request
→ Classification Prompt
→ Chat Model
→ Enum Parser
→ task_type
```

Review Pipeline:

```text
Draft Output
→ Review Prompt
→ Chat Model
→ JSON Parser
→ Review Result
```

RAG Answer Pipeline:

```text
Question + Context
→ RAG Prompt
→ Chat Model
→ String Parser
→ Grounded Answer
```

Pipeline 검증 기준:

| 단계   | 검증                 |
| ------ | -------------------- |
| Input  | 필수 입력 존재 여부  |
| Prompt | 변수 누락 여부       |
| Model  | Timeout / Retry      |
| Parser | 형식 검증            |
| Output | State 매핑 가능 여부 |

---

### [FAQ]

Q. Prompt-Model-Parser Pipeline이 뭐야?

A.
입력을 Prompt로 바꾸고, LLM 응답을 생성한 뒤, Parser로 원하는 형식으로 변환하는 기본 Pipeline이다.

Q. 이 Pipeline은 어디에 써?

A.
요약, 분류, RAG 답변, 코드 리뷰, JSON 생성에 사용한다.

Q. Parser는 항상 필요해?

A.
일반 답변은 String Parser로 충분하지만, Routing이나 Review 결과는 JSON 또는 Schema Parser가 필요하다.

Q. Pipeline 실패는 어디서 많이 발생해?

A.
Prompt 변수 누락, Model Timeout, Parser 형식 오류에서 자주 발생한다.

Q. Pipeline 출력은 왜 State와 맞춰야 해?

A.
LangGraph Node에서 Pipeline 결과를 State에 저장하고 다음 Node가 사용해야 하기 때문이다.

---

# 9. RAG Prompt Pattern

## 9.1 문서 기반 답변 Prompt

### [개념]

RAG Prompt는 검색된 Context와 사용자 Question을 분리해 LLM이 문서 기반으로 답변하도록 만드는 Prompt다.

기본 구조:

```text
System:
문서 기반으로 답변하라.
문서에 없는 내용은 없다고 답하라.

Context:
{context}

Question:
{question}
```

RAG Prompt는 LLM의 추측을 줄이고 Grounded Answer를 생성하는 데 사용된다.

---

### [핵심]

- Context와 Question을 분리한다.
- 문서에 없는 내용은 없다고 답하도록 지시한다.
- Source 사용 기준을 명시한다.
- Retrieved Context를 과도하게 넣지 않는다.
- Context Formatting을 정리한다.
- 검색 실패와 생성 실패를 구분한다.

---

### [실무]

RAG Prompt 권장 템플릿:

```text
System:
너는 문서 기반 RAG Agent다.
반드시 제공된 Context에 근거해 답변하라.
Context에 없는 내용은 "문서에서 확인되지 않음"이라고 답하라.
추측으로 보완하지 마라.

Context:
{context}

Question:
{question}

Answer:
```

RAG Context Formatting:

```text
[Source: 07_LangChain_LangGraph_Part01_Core_Overview.md]
[Section: 4. LangChain vs LangGraph]
Content:
LangChain은 구성 요소 연결 Framework이고 LangGraph는 Workflow 제어 Framework다.
```

RAG Prompt 금지 패턴:

- Context와 Question을 하나의 긴 문단으로 섞기
- Source 정보 제거
- 검색 결과 전체를 무조건 삽입
- 문서에 없는 내용을 일반 지식으로 보완
- 사용자 질문을 System Message에 삽입

---

### [FAQ]

Q. RAG Prompt는 뭐가 달라?

A.
검색된 Context와 사용자 Question을 분리하고, 문서 기반으로 답변하도록 강제하는 Prompt다.

Q. RAG Prompt에서 가장 중요한 규칙은?

A.
Context에 없는 내용은 추측하지 않고 없다고 답하도록 지시하는 것이다.

Q. Context Formatting은 왜 중요해?

A.
Source, Section, Content가 정리되어야 LLM이 근거를 구분하고 답변하기 쉽기 때문이다.

Q. 검색 결과를 많이 넣으면 좋아?

A.
무조건 좋지 않다. 관련 없는 Context가 많으면 답변 품질이 낮아질 수 있다.

Q. RAG Prompt에 Source를 넣어야 해?

A.
권장한다. 답변 근거를 검증하고 Review Agent가 확인하기 쉽기 때문이다.

---

# 10. Agent Prompt Pattern

## 10.1 Agent 역할 Prompt

### [개념]

Agent Prompt는 특정 Agent가 어떤 역할, 권한, Tool, 출력 형식을 가져야 하는지 정의한다.

Agent Prompt는 단순 답변 Prompt보다 명확한 책임과 제한이 필요하다.

기본 구조:

```text
System:
너는 {agent_role} Agent다.
목표는 {goal}이다.
사용 가능한 Tool은 {tools}이다.
위험 작업은 승인 없이 실행하지 마라.

State:
{state}

Task:
{task}
```

Agent Prompt는 Tool Selection과 Final Answer 품질에 직접 영향을 준다.

---

### [핵심]

- Agent 역할을 명확히 정의한다.
- Agent 책임 범위를 제한한다.
- 사용 가능한 Tool을 명시한다.
- Tool 사용 조건을 설명한다.
- 출력 형식을 고정한다.
- 위험 작업은 Human Approval을 요구한다.
- Stop Condition을 포함한다.

---

### [실무]

PM Agent Prompt:

```text
System:
너는 개인 AI 개발팀의 PM Agent다.
사용자 요청을 분석하고 작업을 분해하라.
필요한 Domain Agent를 선택하라.
모든 요청을 모든 Agent에게 보내지 마라.

Output:
task_type
required_agents
requirements
needs_human_approval
```

Backend Agent Prompt:

```text
System:
너는 Backend Agent다.
Spring Boot, JPA, Security, API Design 문서를 우선 참조하라.
RAG 문서 근거를 기준으로 답변하라.
불확실한 내용은 명확히 표시하라.
```

Review Agent Prompt:

```text
System:
너는 Review Agent다.
요구사항 충족, 코드 정확성, 보안 위험, 누락, 일관성을 검토하라.
결과는 pass/fail과 findings로 반환하라.
```

Agent Prompt 주의:

- Agent에게 무제한 권한을 주지 않는다.
- Tool을 너무 많이 노출하지 않는다.
- 출력 형식을 모호하게 두지 않는다.
- Agent가 모든 Domain을 담당하게 하지 않는다.
- 위험 작업은 승인 Node로 라우팅한다.

---

### [FAQ]

Q. Agent Prompt가 뭐야?

A.
Agent의 역할, 책임, Tool 사용 조건, 출력 형식, 제한 사항을 정의하는 Prompt다.

Q. Agent Prompt는 일반 Prompt와 뭐가 달라?

A.
단순 답변보다 역할, 권한, Tool, Stop Condition, Human Approval 기준이 더 중요하다.

Q. PM Agent Prompt에는 무엇이 들어가야 해?

A.
요청 분석, 작업 분해, Agent 선택, Routing 출력 형식이 들어가야 한다.

Q. Review Agent Prompt에는 무엇이 들어가야 해?

A.
검토 기준, pass/fail 판단 기준, findings 출력 형식이 들어가야 한다.

Q. Agent Prompt에서 Tool을 많이 주면 좋아?

A.
무조건 좋지 않다. Tool이 많으면 선택 오류가 늘 수 있으므로 필요한 Tool만 제공한다.

---

# 11. Error Handling

## 11.1 Runnable Pipeline 오류 처리

### [개념]

Runnable Pipeline은 Prompt, Model, Parser, Retriever, Tool 단계에서 오류가 발생할 수 있다.

오류는 숨기지 말고 구조화해서 처리해야 한다.

기본 Flow:

```text
Pipeline Error
→ Record Error
→ Retry if Possible
→ Fallback
→ Error Output
```

LangGraph에서는 오류를 State에 기록하고 Error Node 또는 Fallback Node로 이동할 수 있다.

---

### [핵심]

- Prompt 변수 누락은 실행 전 검증한다.
- Model Timeout은 Retry 대상이다.
- Parser Error는 형식 지시 강화 후 재시도할 수 있다.
- Tool Error는 실패 결과를 구조화한다.
- Retrieval Error는 검색 실패와 연결 실패를 구분한다.
- 무제한 Retry를 금지한다.
- 복구 불가 오류는 사용자에게 명확히 보고한다.

---

### [실무]

오류 유형:

| 오류            | 원인                   | 처리                          |
| --------------- | ---------------------- | ----------------------------- |
| Prompt Error    | 변수 누락              | Template Validation           |
| Model Error     | Timeout, Rate Limit    | Retry, Fallback Model         |
| Parser Error    | JSON 형식 오류         | Retry with Format Instruction |
| Retrieval Error | 문서 없음, DB 오류     | No Context 처리               |
| Tool Error      | Args 오류, 권한 부족   | Tool Error Result             |
| State Error     | 필드 누락, 타입 불일치 | State Validation              |

Parser Error 처리:

```text
Invalid JSON
→ Parser Error
→ Retry Prompt:
  "반드시 valid JSON만 출력하라"
→ Parse Again
→ Fallback if Failed
```

Tool Error 처리:

```json
{
  "status": "error",
  "tool_name": "search_rag_documents",
  "error_type": "invalid_arguments",
  "message": "top_k must be integer",
  "retryable": true
}
```

---

### [FAQ]

Q. Runnable Pipeline 오류는 어디서 발생해?

A.
Prompt 변수 누락, Model Timeout, Parser 형식 오류, Retriever 실패, Tool Arguments 오류에서 발생한다.

Q. Parser Error는 어떻게 처리해?

A.
출력 형식 지시를 강화해 재시도하고, 반복 실패 시 Fallback 또는 Error Node로 이동한다.

Q. Tool Error는 숨겨도 돼?

A.
안 된다. Tool 실패 결과를 구조화해서 다음 Node나 사용자에게 전달해야 한다.

Q. Retry는 계속 해도 돼?

A.
안 된다. Max Retry를 정하고 실패 시 Fallback 처리해야 한다.

Q. LangGraph에서 오류는 어디에 기록해?

A.
State의 error 또는 errors 필드에 기록하고 Error Node로 라우팅할 수 있다.

---

# 12. Debugging Checklist

## 12.1 Runnable Debugging

### [Checklist]

- [ ] Runnable 입력 타입이 명확한가?
- [ ] Runnable 출력 타입이 다음 단계 입력과 맞는가?
- [ ] Prompt Template 필수 변수가 누락되지 않았는가?
- [ ] System Message와 User Message가 분리되었는가?
- [ ] RAG Context와 Question이 분리되었는가?
- [ ] Chat Model 설정이 작업 목적에 맞는가?
- [ ] Temperature가 RAG / Review 작업에 적합하게 낮은가?
- [ ] Timeout과 Retry 기준이 있는가?
- [ ] Output Parser가 필요한 작업에 적용되었는가?
- [ ] Parser Error 처리 기준이 있는가?
- [ ] Structured Output Schema가 너무 복잡하지 않은가?
- [ ] Agent Prompt에 역할과 책임이 명확한가?
- [ ] 위험 Tool 사용 전 Human Approval 기준이 있는가?
- [ ] Pipeline 중간 결과를 추적할 수 있는가?
- [ ] API Key, Secret, 개인정보가 로그에 남지 않는가?

---

# Retrieval Queries

### [FAQ]

Q. Runnable이 뭐야?
A. Runnable은 입력을 받아 출력을 만드는 LangChain의 실행 가능한 구성 단위다.

Q. Runnable은 왜 중요해?
A. Prompt, Model, Parser, Retriever, Tool을 일관된 방식으로 연결해 Pipeline을 만들 수 있기 때문이다.

Q. invoke는 뭐야?
A. invoke는 단일 입력을 Runnable에 넣어 한 번 실행하는 방식이다.

Q. batch는 뭐야?
A. batch는 여러 입력을 한 번에 처리하는 Runnable 실행 방식이다.

Q. stream은 뭐야?
A. stream은 응답이나 결과를 부분적으로 출력하는 실행 방식이다.

Q. RunnableSequence가 뭐야?
A. RunnableSequence는 여러 Runnable을 순서대로 연결해 실행하는 Pipeline 구조다.

Q. Chain과 RunnableSequence 차이는?
A. 현대 LangChain에서는 Chain을 Runnable 기반 Pipeline으로 이해하는 것이 적합하다.

Q. Runnable Pipeline은 언제 써?
A. 요약, 분류, 변환, RAG 답변, 코드 리뷰처럼 순차 흐름이 명확한 작업에 사용한다.

Q. Prompt Template이 뭐야?
A. 입력 변수를 Prompt 구조에 주입해 반복 가능한 Prompt를 만드는 구성 요소다.

Q. Prompt Template은 왜 필요해?
A. Prompt 구조를 안정화하고 입력 변수를 명확히 관리하기 위해 필요하다.

Q. Chat Prompt Template이 뭐야?
A. Chat Model에 전달할 System, Human, AI, Tool Message 구조를 만드는 Template이다.

Q. System Message에는 무엇을 넣어?
A. Agent 역할, 답변 규칙, 금지 사항, 출력 형식 같은 상위 지시를 넣는다.

Q. Human Message에는 무엇을 넣어?
A. 사용자의 실제 질문이나 작업 요청을 넣는다.

Q. Tool Message에는 무엇을 넣어?
A. Tool 실행 결과나 Observation을 넣는다.

Q. RAG Prompt에서 Context와 Question을 분리해야 하는 이유는?
A. 문서 근거와 사용자 질문을 구분해야 LLM이 문서 기반으로 답변하기 쉽기 때문이다.

Q. 사용자 입력을 System Prompt에 직접 넣어도 돼?
A. 권장하지 않는다. 사용자 입력은 User Message나 Question 영역에 넣어야 한다.

Q. Chat Model이 뭐야?
A. Prompt 또는 Message를 입력받아 LLM 응답을 생성하는 LangChain 구성 요소다.

Q. Chat Model은 LLM 자체야?
A. 정확히는 LLM을 호출하는 인터페이스로 이해하는 것이 적합하다.

Q. Local LLM과 API LLM 차이는?
A. Local LLM은 내 서버에서 실행되고 API LLM은 외부 Provider API를 호출한다.

Q. RAG 작업에서 Temperature는 낮게 해야 해?
A. 권장한다. 문서 기반 답변은 일관성과 정확성이 중요하기 때문이다.

Q. Timeout은 왜 필요해?
A. LLM 응답 지연이나 장애가 전체 Workflow를 멈추지 않게 하기 위해 필요하다.

Q. Output Parser가 뭐야?
A. LLM 응답을 문자열, JSON, Schema 같은 원하는 형식으로 변환하거나 검증하는 구성 요소다.

Q. Output Parser는 왜 필요해?
A. LLM 응답을 안정적인 데이터 구조로 바꿔 Chain이나 Graph에서 사용하기 위해 필요하다.

Q. Parser가 내용 정확성도 보장해?
A. 아니다. Parser는 형식을 검증하지만 내용의 사실성이나 정확성은 별도 검토가 필요하다.

Q. JSON Parser는 언제 써?
A. Agent Routing, Review 결과, Tool Arguments처럼 구조화된 결과가 필요할 때 사용한다.

Q. Structured Output이 뭐야?
A. LLM 응답을 미리 정한 Schema에 맞게 구조화해서 반환하는 방식이다.

Q. Structured Output은 언제 필요해?
A. Routing, Review, Tool Calling, Agent Handoff처럼 결과 형식이 중요할 때 필요하다.

Q. PM Agent Output Schema에는 무엇이 들어가?
A. task_type, required_agents, requirements, priority, needs_human_approval 같은 필드가 들어간다.

Q. Review Agent Output Schema에는 무엇이 들어가?
A. result, severity, findings, fix_required, next_action 같은 필드가 들어간다.

Q. Prompt-Model-Parser Pipeline이 뭐야?
A. 입력을 Prompt로 바꾸고 LLM 응답을 생성한 뒤 Parser로 원하는 형식으로 변환하는 기본 Pipeline이다.

Q. Parser는 항상 필요해?
A. 일반 답변은 String Parser로 충분하지만 Routing이나 Review 결과는 JSON 또는 Schema Parser가 필요하다.

Q. RAG Prompt는 뭐가 달라?
A. 검색된 Context와 사용자 Question을 분리하고 문서 기반으로 답변하도록 강제한다.

Q. RAG Prompt에서 가장 중요한 규칙은?
A. Context에 없는 내용은 추측하지 않고 없다고 답하도록 지시하는 것이다.

Q. Context Formatting은 왜 중요해?
A. Source, Section, Content가 정리되어야 LLM이 근거를 구분하고 답변하기 쉽기 때문이다.

Q. Agent Prompt가 뭐야?
A. Agent의 역할, 책임, Tool 사용 조건, 출력 형식, 제한 사항을 정의하는 Prompt다.

Q. PM Agent Prompt에는 무엇이 들어가?
A. 요청 분석, 작업 분해, Agent 선택, Routing 출력 형식이 들어가야 한다.

Q. Review Agent Prompt에는 무엇이 들어가?
A. 검토 기준, pass/fail 판단 기준, findings 출력 형식이 들어가야 한다.

Q. Agent Prompt에서 Tool을 많이 주면 좋아?
A. 무조건 좋지 않다. Tool이 많으면 선택 오류가 늘 수 있으므로 필요한 Tool만 제공한다.

Q. Runnable Pipeline 오류는 어디서 발생해?
A. Prompt 변수 누락, Model Timeout, Parser 형식 오류, Retriever 실패, Tool Arguments 오류에서 발생한다.

Q. Parser Error는 어떻게 처리해?
A. 출력 형식 지시를 강화해 재시도하고 반복 실패 시 Fallback 또는 Error Node로 이동한다.

Q. Tool Error는 숨겨도 돼?
A. 안 된다. Tool 실패 결과를 구조화해서 다음 Node나 사용자에게 전달해야 한다.

Q. Retry는 계속 해도 돼?
A. 안 된다. Max Retry를 정하고 실패 시 Fallback 처리해야 한다.

Q. LangGraph에서 오류는 어디에 기록해?
A. State의 error 또는 errors 필드에 기록하고 Error Node로 라우팅할 수 있다.
