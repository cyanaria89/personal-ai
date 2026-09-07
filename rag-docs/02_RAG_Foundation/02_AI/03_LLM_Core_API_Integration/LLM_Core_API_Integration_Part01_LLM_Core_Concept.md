# LLM Core & API Integration Part01 - LLM Core Concept

---

# 1. LLM Core Concept

## 1.1 LLM

### [개념]

LLM(Large Language Model)은 대량의 텍스트 데이터를 학습한 언어 모델이다.

LLM은 Prompt를 입력받고 다음 Token을 확률적으로 예측해 Response를 생성한다.

LLM은 지식 DB가 아니다.

LLM은 다음 작업에 사용된다.

- Chat
- Summarization
- Code Generation
- Code Review
- Document Analysis
- RAG Answer Generation
- Agent Reasoning
- Tool Calling Decision

기본 Flow:

```text
Prompt
→ Tokenization
→ Model Inference
→ Token Generation
→ Response
```

---

### [핵심]

- LLM은 입력 Prompt를 Token 단위로 처리한다.
- LLM은 다음 Token을 확률적으로 생성한다.
- LLM은 항상 최신 정보와 정확한 사실을 보장하지 않는다.
- LLM은 Context Window 안의 정보만 직접 참고할 수 있다.
- LLM의 약점은 RAG, Tool Calling, Response Validation으로 보완한다.
- Agent 시스템에서 LLM은 판단, 생성, 요약, 라우팅, 검토 역할을 수행한다.

---

### [실무]

2026 실무 기준 LLM은 단독 지식 엔진이 아니라 Workflow Engine에 가깝게 사용한다.

권장 구조:

```text
User Request
→ Prompt Builder
→ Retrieved Context
→ LLM Call
→ Response Validation
→ Final Response
```

실무에서는 LLM을 아래와 같이 분리해서 사용한다.

| 역할        | 사용 모델                       |
| ----------- | ------------------------------- |
| 답변 생성   | Chat Model                      |
| 코드 생성   | Code Model 또는 Reasoning Model |
| 문서 검색   | Embedding Model                 |
| 이미지 입력 | Vision Model                    |
| 로컬 실행   | Local LLM                       |
| 복잡한 추론 | Reasoning Model                 |
| Agent 실행  | Tool Calling 지원 모델          |

LLM을 사용할 때 반드시 고려할 요소:

- Token Limit
- Context Window
- Temperature
- Max Tokens
- Prompt Quality
- Retrieved Context Quality
- API Timeout
- Retry
- Rate Limit
- Response Validation
- Cost
- Latency

---

### [FAQ]

Q. LLM이 뭐야?

A.
LLM은 Prompt를 입력받고 다음 Token을 예측해 자연어, 코드, JSON 등을 생성하는 대형 언어 모델이다.

Q. LLM은 데이터베이스야?

A.
아니다. LLM은 학습된 패턴을 기반으로 응답을 생성하는 모델이며, 정확한 사실 저장소가 아니다.

Q. LLM은 왜 틀린 답을 할 수 있어?

A.
LLM은 확률적으로 Token을 생성하고, 최신 정보나 외부 문서를 기본적으로 알지 못하기 때문이다.

Q. LLM의 한계는 어떻게 보완해?

A.
RAG로 외부 문서를 넣고, Tool Calling으로 외부 기능을 호출하며, Response Validation으로 출력을 검증한다.

---

## 1.2 Token

### [개념]

Token은 LLM이 텍스트를 처리하는 기본 단위이다.

문장, 단어, 부분 단어, 기호가 Token으로 분리될 수 있다.

LLM API에서 Token은 비용, 속도, Context Window, 출력 길이에 직접 영향을 준다.

Token 종류:

- Input Token
- Output Token
- Total Token
- Prompt Token
- Completion Token

Token Flow:

```text
System Message
+ User Message
+ Conversation History
+ Retrieved Context
→ Input Tokens
→ LLM Generation
→ Output Tokens
→ Total Tokens
```

---

### [핵심]

- LLM은 문자나 문장을 그대로 읽지 않고 Token 단위로 처리한다.
- 입력 Prompt는 Input Token을 사용한다.
- 모델 응답은 Output Token을 사용한다.
- Input Token + Output Token = Total Token이다.
- Token 수가 많을수록 비용과 Latency가 증가한다.
- Token Limit을 초과하면 요청 실패, Context 누락, Response Truncation이 발생할 수 있다.

---

### [실무]

LLM API 연동 시 Token Budget을 관리해야 한다.

권장 Token Budget 구조:

```text
System Instruction
→ Conversation Summary
→ Retrieved Context
→ User Task
→ Output Reserve
```

실무 기준:

- System Instruction은 짧고 명확하게 작성한다.
- Conversation History는 전체 대화가 아니라 요약본 중심으로 넣는다.
- Retrieved Context는 관련 Chunk만 넣는다.
- Max Tokens로 출력 길이를 제한한다.
- 긴 문서는 Chunking 후 Retrieval로 처리한다.
- 비용 추적을 위해 Token Usage를 로그로 남긴다.

Token 관리 예:

```text
전체 Context Window: 32000 tokens
System Instruction: 1000 tokens
Conversation Summary: 2000 tokens
Retrieved Context: 12000 tokens
User Task: 1000 tokens
Output Reserve: 4000 tokens
Safety Margin: 12000 tokens
```

주의:

- RAG Context를 많이 넣는다고 답변 품질이 항상 좋아지지 않는다.
- 관련 없는 Context는 Hallucination을 증가시킨다.
- 긴 출력은 비용과 Latency를 증가시킨다.
- Token Limit 초과 상황을 Error Handling에 포함해야 한다.

---

### [FAQ]

Q. Token이 뭐야?

A.
Token은 LLM이 텍스트를 읽고 생성할 때 사용하는 처리 단위다.

Q. Token이 왜 중요해?

A.
Token은 비용, 응답 속도, Context Window, 출력 길이에 직접 영향을 준다.

Q. Input Token과 Output Token 차이는?

A.
Input Token은 모델에 입력되는 Prompt이고, Output Token은 모델이 생성한 응답이다.

Q. Token Limit을 넘으면 어떻게 돼?

A.
요청이 실패하거나, 일부 Context가 잘리거나, 응답이 중간에서 끊길 수 있다.

---

## 1.3 Context Window

### [개념]

Context Window는 LLM이 한 번의 요청에서 참고할 수 있는 최대 Token 범위이다.

Context Window에는 다음 정보가 포함된다.

- System Message
- User Message
- Assistant Message
- Tool Message
- Conversation History
- Retrieved Context
- Output Tokens

기본 구조:

```text
System Instruction
→ Conversation Summary
→ Retrieved Documents
→ Current User Task
→ Model Response
```

---

### [핵심]

- Context Window는 모델이 한 번에 볼 수 있는 작업 공간이다.
- Context Window가 크다고 모든 정보를 넣는 것이 좋은 것은 아니다.
- 관련 없는 Context는 답변 품질을 낮춘다.
- 중요한 지시는 명확한 위치에 배치해야 한다.
- RAG에서는 Top-K와 Chunk Size가 Context Window 사용량에 직접 영향을 준다.
- 긴 대화는 요약 또는 최근 대화 중심으로 압축한다.

---

### [실무]

Agent Workflow에서는 Context Window를 State 관리와 함께 설계한다.

권장 구조:

```text
Agent Role
→ Task Goal
→ Required Rules
→ Retrieved Context
→ Previous Step Summary
→ Current Task
→ Output Schema
```

RAG 기반 LLM 호출에서는 다음 기준을 적용한다.

| 항목                 | 기준               |
| -------------------- | ------------------ |
| System Instruction   | 짧고 고정된 규칙   |
| Conversation History | 전체 원문보다 요약 |
| Retrieved Context    | 관련 Chunk만 포함  |
| User Task            | 현재 요청 중심     |
| Output Schema        | 명확하게 지정      |
| Safety Margin        | 남겨둘 것          |

Context 관리 실패 예:

```text
긴 대화 전체 삽입
+ 관련 없는 RAG 문서 다수 삽입
+ 긴 출력 요구
→ Context Window 초과
→ 응답 누락 또는 품질 저하
```

권장 대응:

- Query Rewrite
- Context Filtering
- Chunk Reranking
- Conversation Summary
- Context Compression
- Output Token Limit
- Missing Information Rule

---

### [FAQ]

Q. Context Window가 뭐야?

A.
Context Window는 LLM이 한 번에 참고할 수 있는 입력과 출력의 최대 Token 범위다.

Q. Context Window가 크면 무조건 좋아?

A.
아니다. 관련 없는 정보가 많으면 오히려 답변 품질이 낮아질 수 있다.

Q. RAG에서 Context Window는 왜 중요해?

A.
검색된 문서 Chunk가 Context Window를 차지하므로, 관련 Chunk만 선택해야 한다.

Q. 긴 대화는 어떻게 처리해?

A.
전체 대화를 계속 넣지 말고 Conversation Summary 또는 최근 핵심 문맥만 넣는다.

---

# 2. Prompt and Message Structure

## 2.1 Prompt

### [개념]

Prompt는 LLM에게 전달하는 입력 지시문이다.

Prompt는 모델이 수행할 작업, 참고할 정보, 출력 형식, 제약 조건을 정의한다.

Prompt 구성 요소:

- Role
- Task
- Context
- Constraint
- Output Format
- Example
- Validation Rule

기본 구조:

```text
Role
→ Task
→ Context
→ Constraints
→ Output Format
```

---

### [핵심]

- Prompt는 LLM의 행동을 제어하는 입력이다.
- 좋은 Prompt는 역할, 작업, 맥락, 제약, 출력 형식이 명확하다.
- RAG Prompt는 Retrieved Context와 User Task를 구분해야 한다.
- Agent Prompt는 Agent Role과 Output Schema를 포함해야 한다.
- Prompt가 길수록 비용과 Latency가 증가한다.
- 모호한 Prompt는 일관성 없는 응답을 만든다.

---

### [실무]

실무 Prompt는 Template으로 관리한다.

예시:

```text
You are a Backend Review Agent.

Task:
Review the provided Spring Boot service code.

Context:
{retrieved_context}

User Request:
{user_request}

Output Format:
- Summary
- Issues
- Recommended Fix
```

RAG Prompt 권장 구조:

```text
System Rule:
Answer only using retrieved context.

Retrieved Context:
{documents}

User Question:
{question}

Missing Information Rule:
If the answer is not in the context, say it is not found in the documents.
```

Agent Prompt 권장 구조:

```text
Agent Role:
{agent_role}

Current State:
{state_summary}

Task:
{task}

Available Tools:
{tools}

Output Schema:
{schema}
```

주의:

- Prompt에 API Key, Secret, 개인정보를 넣지 않는다.
- System Message에 일회성 작업을 과도하게 넣지 않는다.
- User Message와 Retrieved Context를 혼합하지 않는다.
- Prompt Template 변경 시 테스트 케이스를 갱신한다.

---

### [FAQ]

Q. Prompt가 뭐야?

A.
Prompt는 LLM에게 작업 지시, 맥락, 제약, 출력 형식을 전달하는 입력이다.

Q. 좋은 Prompt의 기준은?

A.
역할, 작업, 참고 정보, 금지 조건, 출력 형식이 명확한 Prompt가 좋다.

Q. RAG Prompt에서 중요한 건 뭐야?

A.
Retrieved Context와 User Question을 분리하고, 문서에 없는 내용은 없다고 답하게 하는 것이다.

Q. Agent Prompt는 일반 Prompt와 뭐가 달라?

A.
Agent Prompt는 역할, 상태, 도구, 다음 행동, 출력 Schema를 포함한다.

---

## 2.2 Message Structure

### [개념]

Message Structure는 Chat Completion API에서 대화를 구성하는 Role 기반 입력 구조이다.

주요 Message Role:

- System Message
- User Message
- Assistant Message
- Tool Message

기본 Flow:

```text
System Message
→ User Message
→ Assistant Message
→ User Message
→ Assistant Message
```

예시:

```json
[
  {
    "role": "system",
    "content": "You are a backend development assistant."
  },
  {
    "role": "user",
    "content": "Spring Service 코드를 리뷰해줘."
  }
]
```

---

### [핵심]

- System Message는 모델의 상위 행동 규칙이다.
- User Message는 현재 사용자의 요청이다.
- Assistant Message는 이전 모델 응답이다.
- Tool Message는 Tool 실행 결과를 모델에 전달한다.
- Conversation History는 문맥 유지에 도움이 되지만 Token을 소비한다.
- 잘못된 이전 Assistant Message를 그대로 넣으면 오류가 누적될 수 있다.

---

### [실무]

실무에서는 Message를 목적별로 분리한다.

권장 배치:

```text
System Message:
Agent Role + Global Rules

User Message:
Current Task + User Request

Tool Message:
Tool Result or Retrieved Data

Assistant Message:
Previous Response Summary
```

RAG 연동 예:

```json
[
  {
    "role": "system",
    "content": "Answer using only the retrieved context."
  },
  {
    "role": "user",
    "content": "Question: JWT 인증 흐름 설명해줘.\n\nRetrieved Context:\n..."
  }
]
```

Tool Calling 연동 예:

```text
User Request
→ Assistant selects Tool
→ Tool executes
→ Tool Message returns result
→ Assistant generates final answer
```

주의:

- System Message는 자주 변경하지 않는다.
- User Message에 모든 규칙을 몰아넣지 않는다.
- Tool Result는 사실 데이터로 취급하되 검증한다.
- Conversation History가 길면 Summary로 대체한다.
- Prompt Injection 방어를 위해 User Content와 System Rule을 구분한다.

---

### [FAQ]

Q. System Message와 User Message 차이는?

A.
System Message는 모델의 상위 행동 규칙이고, User Message는 현재 사용자의 요청이다.

Q. Assistant Message는 왜 넣어?

A.
이전 모델 응답을 대화 문맥으로 유지하기 위해 넣는다.

Q. Tool Message는 뭐야?

A.
외부 도구 실행 결과를 모델에게 전달하는 메시지다.

Q. Conversation History를 전부 넣어도 돼?

A.
권장하지 않는다. Token을 많이 쓰고 오래된 오류가 누적될 수 있으므로 요약해서 넣는 것이 좋다.

---

# 3. LLM Output Behavior

## 3.1 Probabilistic Generation

### [개념]

LLM은 정답을 검색해서 그대로 반환하는 시스템이 아니다.

LLM은 입력 Context를 기반으로 다음 Token의 확률 분포를 계산하고 Token을 선택해 응답을 생성한다.

생성 과정:

```text
Input Tokens
→ Probability Distribution
→ Token Sampling
→ Next Token
→ Repeat
→ Final Response
```

---

### [핵심]

- LLM 출력은 확률적이다.
- 같은 Prompt라도 설정과 환경에 따라 다른 응답이 나올 수 있다.
- Temperature와 Top-p는 출력 다양성에 영향을 준다.
- 낮은 Temperature는 일관성에 유리하다.
- 높은 Temperature는 창의성에 유리하지만 Hallucination 가능성이 증가한다.
- 개발 Agent와 Review Agent는 낮은 Temperature가 적합하다.

---

### [실무]

작업별 Temperature 권장 기준:

| 작업          | 권장 방향 |
| ------------- | --------- |
| 코드 생성     | 낮게      |
| 코드 리뷰     | 낮게      |
| RAG 답변      | 낮게      |
| 문서 요약     | 낮게~중간 |
| 기획 아이디어 | 중간      |
| 창작          | 높게      |

실무 기준:

- 정확성이 중요한 작업은 Temperature를 낮게 설정한다.
- JSON Output은 낮은 Temperature와 Schema Validation을 함께 사용한다.
- RAG 답변은 근거 문서 중심으로 생성하도록 제한한다.
- Review Agent는 보수적으로 판단하도록 설정한다.
- 창의적 브레인스토밍은 PM Agent에서만 제한적으로 허용한다.

주의:

- Temperature 0이어도 완전한 결정론을 보장하지 않는다.
- 낮은 Temperature가 항상 사실 정확성을 보장하지 않는다.
- 출력은 항상 검증해야 한다.

---

### [FAQ]

Q. LLM은 왜 같은 질문에도 답이 달라질 수 있어?

A.
LLM은 확률적으로 다음 Token을 생성하기 때문에 설정과 상황에 따라 응답이 달라질 수 있다.

Q. Temperature는 뭐야?

A.
Temperature는 LLM 출력의 무작위성과 다양성을 조절하는 Parameter다.

Q. 코드 생성에는 Temperature를 어떻게 설정해?

A.
코드 생성, 코드 리뷰, RAG 답변은 낮은 Temperature가 적합하다.

Q. Temperature를 낮추면 항상 정확해져?

A.
아니다. 일관성은 높아질 수 있지만 사실 정확성은 RAG와 검증으로 보완해야 한다.

---

## 3.2 Hallucination

### [개념]

Hallucination은 LLM이 사실이 아니거나 근거 없는 내용을 그럴듯하게 생성하는 현상이다.

Hallucination 발생 원인:

- Context 부족
- 최신 정보 부족
- 잘못된 Prompt
- 관련 없는 Retrieved Context
- 높은 Temperature
- 검증 단계 부재
- 모델의 확률적 생성 특성

---

### [핵심]

- LLM은 모르는 내용을 추론해서 답할 수 있다.
- RAG가 있어도 Retrieved Context가 부정확하면 Hallucination이 발생한다.
- Tool Result가 틀리면 최종 답변도 틀릴 수 있다.
- Response Validation이 없으면 잘못된 응답이 그대로 사용자에게 전달된다.
- 문서 기반 답변은 근거 문서와 일치 여부를 확인해야 한다.

---

### [실무]

Hallucination 대응 Flow:

```text
User Query
→ Retrieve Context
→ Build Grounded Prompt
→ Generate Answer
→ Validate Against Context
→ Return Answer or Missing Information
```

권장 대응:

- Missing Information Rule 적용
- Retrieved Context 제한
- Citation 또는 Reference 확인
- Response Validation
- JSON Schema Validation
- Tool Result Validation
- 낮은 Temperature 사용
- Review Agent 검토

RAG Prompt 예:

```text
Use only the retrieved context.
If the answer is not found in the retrieved context, answer:
"문서에서 확인되지 않습니다."
```

주의:

- RAG를 사용한다고 Hallucination이 자동으로 사라지지 않는다.
- 검색 결과가 부정확하면 오답 가능성이 높다.
- 근거 문서와 일반 추론을 구분해야 한다.
- 최신 정보는 Web Search 또는 Tool Calling으로 확인해야 한다.

---

### [FAQ]

Q. Hallucination이 뭐야?

A.
LLM이 근거 없거나 사실이 아닌 내용을 그럴듯하게 생성하는 현상이다.

Q. RAG를 쓰면 Hallucination이 없어져?

A.
아니다. RAG는 줄여줄 수 있지만 검색 문서 품질과 검증이 부족하면 여전히 발생한다.

Q. Hallucination을 줄이는 방법은?

A.
관련 Context만 넣고, 문서에 없는 내용은 없다고 답하게 하며, 응답을 검증해야 한다.

Q. 문서 기반 답변에서 가장 중요한 규칙은?

A.
Retrieved Context에 근거가 없으면 추측하지 않고 없다고 답하는 것이다.

---

# 4. LLM in RAG and Agent System

## 4.1 LLM in RAG

### [개념]

RAG(Retrieval-Augmented Generation)는 LLM이 외부 문서를 검색해 참고하도록 만드는 구조이다.

LLM은 검색된 문서 Chunk를 Prompt에 포함받고, 해당 Context를 기반으로 답변을 생성한다.

RAG Flow:

```text
User Query
→ Query Rewrite
→ Document Retrieval
→ Retrieved Context
→ Prompt Assembly
→ LLM Generation
→ Answer Validation
```

---

### [핵심]

- RAG는 LLM의 지식 한계를 외부 문서로 보완한다.
- Embedding Model은 문서 검색에 사용된다.
- Chat Model은 검색된 Context를 바탕으로 답변을 생성한다.
- Chunk 품질이 RAG 답변 품질을 결정한다.
- Top-K가 높다고 항상 좋은 답변이 나오지 않는다.
- Retrieval Queries와 FAQ는 검색 적중률을 높인다.

---

### [실무]

RAG 문서 제작 기준:

- 하나의 Chunk는 하나의 개념만 설명한다.
- 제목은 검색 친화적으로 작성한다.
- FAQ는 실제 사용자 질문 표현을 포함한다.
- Retrieval Queries를 문서 마지막에 포함한다.
- 코드 예제는 짧고 직접적으로 작성한다.
- 동일 개념의 용어를 문서 전체에서 통일한다.
- RAG 답변은 문서 근거와 일반 추론을 구분한다.

RAG Prompt 구조:

```text
System:
You are a RAG-based assistant.
Answer using only retrieved documents.

Retrieved Context:
{retrieved_chunks}

User Question:
{query}

Rule:
If context is insufficient, say the information is not found.
```

주의:

- Retrieved Context가 길면 비용과 Latency가 증가한다.
- 관련 없는 Chunk는 답변 품질을 낮춘다.
- 문서 변경 후 Embedding 재생성이 필요할 수 있다.
- RAG 문서는 사람용 학습 문서보다 검색 최적화가 중요하다.

---

### [FAQ]

Q. RAG에서 LLM은 무슨 역할이야?

A.
LLM은 검색된 문서 Context를 바탕으로 최종 답변을 생성하는 역할을 한다.

Q. Embedding Model과 Chat Model 차이는?

A.
Embedding Model은 검색용 Vector를 만들고, Chat Model은 답변을 생성한다.

Q. RAG에서 Chunk가 중요한 이유는?

A.
검색은 Chunk 단위로 이루어지므로 Chunk 품질이 답변 품질에 직접 영향을 준다.

Q. RAG 답변에서 문서에 없는 내용은 어떻게 처리해?

A.
추측하지 말고 문서에서 확인되지 않는다고 답해야 한다.

---

## 4.2 LLM in Agent System

### [개념]

Agent System에서 LLM은 단순 답변 생성기가 아니라 의사결정과 실행 흐름을 담당한다.

Agent는 LLM을 사용해 다음 작업을 수행한다.

- Task Understanding
- Planning
- Tool Selection
- Tool Arguments Generation
- Intermediate Result Summary
- Code Generation
- Review
- Final Response Generation

Agent Flow:

```text
Agent State
→ Build Prompt
→ Call LLM
→ Parse Response
→ Tool Call if Needed
→ Update State
→ Next Agent or Final Response
```

---

### [핵심]

- Agent는 LLM API 호출을 반복적으로 사용한다.
- Agent마다 Role과 Output Schema가 필요하다.
- Tool Calling은 Agent가 외부 기능을 사용하게 만든다.
- Agent State는 작업 흐름과 중간 결과를 유지한다.
- Review Agent는 LLM 출력 검증을 담당할 수 있다.
- Agent Loop는 무한 반복을 방지해야 한다.

---

### [실무]

개인 AI 개발팀 구조 예:

```text
User Request
→ PM Agent
→ Backend Agent
→ Frontend Agent
→ Review Agent
→ DevOps Agent
→ AI/ML Agent
→ Final Output
```

Agent별 LLM 사용 기준:

| Agent          | 주요 역할                          | LLM 사용               |
| -------------- | ---------------------------------- | ---------------------- |
| PM Agent       | 요구사항 정리, 작업 분해           | Planning, Summary      |
| Backend Agent  | API, Service, Repository 코드 생성 | Code Generation        |
| Frontend Agent | Component, State, API 연동         | Code Generation        |
| Review Agent   | 오류 검토, 보안 검토, 품질 검토    | Validation             |
| DevOps Agent   | 배포, Docker, CI/CD                | Procedure Generation   |
| AI/ML Agent    | RAG, Agent, LLM API 설계           | Architecture Reasoning |

Agent 설계 필수 요소:

- Agent Role
- System Prompt
- Input Schema
- Output Schema
- Tool List
- State Structure
- Error Handling
- Retry Policy
- Stop Condition
- Review Loop

주의:

- Agent 간 출력 형식을 통일해야 한다.
- Tool Arguments는 실행 전 검증해야 한다.
- 파일 삭제, 결제, 배포 같은 위험 작업은 승인 절차가 필요하다.
- Agent Loop가 무한 반복되지 않도록 Max Step을 둔다.
- LLM 출력은 다음 Agent에 넘기기 전 검증한다.

---

### [FAQ]

Q. Agent에서 LLM은 무슨 역할이야?

A.
LLM은 작업 이해, 계획, 도구 선택, 코드 생성, 검토, 최종 응답 생성을 담당한다.

Q. Agent마다 Prompt가 달라야 해?

A.
그렇다. PM Agent, Backend Agent, Review Agent는 역할과 출력 형식이 다르므로 Prompt도 달라야 한다.

Q. Tool Calling은 Agent에 왜 필요해?

A.
LLM이 직접 할 수 없는 검색, 파일 작업, API 호출, 계산 등을 외부 도구로 실행하기 위해 필요하다.

Q. Agent 시스템에서 가장 위험한 문제는?

A.
검증 없는 Tool 실행, 무한 Loop, 잘못된 중간 결과 전파, Schema 불일치가 위험하다.

---

# 5. Common Mistakes

## 5.1 LLM Core Common Mistakes

### [개념]

LLM Core Common Mistakes는 LLM을 API 또는 Agent 시스템에 연동할 때 자주 발생하는 설계 오류이다.

---

### [핵심]

자주 발생하는 실수:

- LLM을 정확한 지식 DB처럼 사용
- Token Limit을 고려하지 않음
- Context Window를 무제한으로 가정
- 긴 Conversation History를 계속 삽입
- Retrieved Context를 과도하게 삽입
- Temperature를 작업 목적과 무관하게 설정
- RAG 없이 최신 정보를 답하게 함
- JSON Output을 검증하지 않음
- Tool Arguments를 검증하지 않음
- LLM 응답을 바로 사실로 사용
- Timeout 없이 API 호출
- Rate Limit 대응 없이 병렬 호출
- 비용 계산 없이 대량 호출
- Prompt와 Context를 혼합
- System Message와 User Message 역할을 혼동

---

### [실무]

문제 대응 Checklist:

```text
LLM 응답이 이상함
→ Prompt 확인
→ Context 확인
→ Retrieved Chunk 확인
→ Parameter 확인
→ Token 사용량 확인
→ Output 검증 확인
→ 로그 확인
```

설계 기준:

- LLM은 생성 엔진으로 사용한다.
- 사실 확인은 RAG 또는 Tool Calling으로 보완한다.
- 모든 LLM Output은 검증한다.
- API 호출에는 Timeout과 Retry 정책을 둔다.
- Token Usage와 Latency를 기록한다.
- Agent 간 Output Schema를 통일한다.

---

### [FAQ]

Q. LLM을 그냥 DB처럼 쓰면 안 돼?

A.
안 된다. LLM은 학습된 패턴을 기반으로 응답을 생성하며 정확한 사실 저장소가 아니다.

Q. 가장 흔한 LLM API 설계 실수는?

A.
Token, Timeout, Rate Limit, Response Validation을 고려하지 않는 것이다.

Q. RAG에서 흔한 실수는?

A.
관련 없는 Chunk를 너무 많이 넣고, 문서에 없는 내용을 LLM이 추측하게 두는 것이다.

Q. Agent에서 흔한 실수는?

A.
Tool Arguments 검증 없이 실행하거나, Agent 간 Output Schema를 통일하지 않는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. LLM이 뭐야?
A. LLM은 Prompt를 입력받고 다음 Token을 확률적으로 생성하는 대형 언어 모델이다.

Q. LLM은 데이터베이스야?
A. 아니다. LLM은 정확한 사실 저장소가 아니라 확률 기반 생성 모델이다.

Q. LLM은 어떻게 답변을 생성해?
A. Prompt를 Token으로 변환하고 다음 Token을 반복 생성해 Response를 만든다.

Q. Token이 뭐야?
A. Token은 LLM이 텍스트를 처리하는 기본 단위이며 비용, 속도, Context Window에 영향을 준다.

Q. Input Token과 Output Token 차이는?
A. Input Token은 모델에 입력되는 Prompt이고 Output Token은 모델이 생성한 응답이다.

Q. Context Window가 뭐야?
A. Context Window는 LLM이 한 번에 참고할 수 있는 최대 Token 범위다.

Q. Context Window가 크면 무조건 좋아?
A. 아니다. 관련 없는 Context가 많으면 답변 품질이 낮아질 수 있다.

Q. Prompt가 뭐야?
A. Prompt는 LLM에게 작업, 맥락, 제약, 출력 형식을 전달하는 입력이다.

Q. 좋은 Prompt는 어떻게 작성해?
A. 역할, 작업, 참고 정보, 제약 조건, 출력 형식을 명확히 작성한다.

Q. System Message와 User Message 차이는?
A. System Message는 상위 행동 규칙이고 User Message는 현재 사용자 요청이다.

Q. Assistant Message는 왜 필요해?
A. 이전 모델 응답을 대화 문맥으로 유지하기 위해 사용한다.

Q. Tool Message는 뭐야?
A. Tool Message는 외부 도구 실행 결과를 모델에게 전달하는 메시지다.

Q. LLM 답변은 왜 매번 다를 수 있어?
A. LLM은 확률적으로 Token을 생성하기 때문에 같은 요청에도 다른 응답이 나올 수 있다.

Q. Temperature는 뭐야?
A. Temperature는 LLM 출력의 무작위성과 다양성을 조절하는 Parameter다.

Q. 코드 생성에는 Temperature를 어떻게 설정해?
A. 코드 생성, 코드 리뷰, RAG 답변은 낮은 Temperature가 적합하다.

Q. Hallucination이 뭐야?
A. Hallucination은 LLM이 근거 없거나 사실이 아닌 내용을 그럴듯하게 생성하는 현상이다.

Q. Hallucination은 어떻게 줄여?
A. RAG Context를 사용하고, 문서에 없는 내용은 없다고 답하게 하며, 응답을 검증한다.

Q. RAG에서 LLM은 무슨 역할이야?
A. LLM은 검색된 문서 Context를 바탕으로 최종 답변을 생성한다.

Q. Embedding Model과 Chat Model 차이는?
A. Embedding Model은 검색용 Vector를 만들고 Chat Model은 답변을 생성한다.

Q. RAG에서 Chunk가 중요한 이유는?
A. 검색은 Chunk 단위로 수행되므로 Chunk 품질이 검색 결과와 답변 품질을 결정한다.

Q. Agent에서 LLM은 무슨 역할이야?
A. Agent에서 LLM은 작업 이해, 계획, 도구 선택, 코드 생성, 검토, 최종 응답 생성을 담당한다.

Q. Agent Prompt는 왜 따로 필요해?
A. Agent마다 역할, 입력, 출력 Schema, Tool 사용 기준이 다르기 때문이다.

Q. LLM API 연동에서 가장 중요한 검증은?
A. Empty Response, Finish Reason, JSON Schema, 근거 문서 일치 여부, Tool Arguments 검증이다.

Q. LLM을 실무에서 안전하게 쓰려면?
A. RAG, Tool Calling, Timeout, Retry, Rate Limit, Response Validation, Logging을 함께 설계해야 한다.
