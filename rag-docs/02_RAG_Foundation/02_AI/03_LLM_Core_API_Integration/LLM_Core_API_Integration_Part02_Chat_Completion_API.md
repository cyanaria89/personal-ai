# LLM Core & API Integration Part02 - Chat Completion API

---

# 1. Chat Completion API

## 1.1 Chat Completion

### [개념]

Chat Completion은 Message 배열을 입력받아 Assistant Response를 생성하는 LLM API 방식이다.

Chat Completion은 단일 Prompt 문자열보다 대화 구조를 명확하게 표현할 수 있다.

기본 구성:

- Model
- Messages
- System Message
- User Message
- Assistant Message
- Tool Message
- Parameters
- Response
- Usage
- Finish Reason

기본 Flow:

```text
Client
→ Build Messages
→ Call Chat Completion API
→ Receive Response
→ Parse Content
→ Validate Output
→ Return Result
```

---

### [핵심]

- Chat Completion은 `messages` 배열을 중심으로 동작한다.
- `system`은 모델의 상위 행동 규칙을 정의한다.
- `user`는 현재 사용자 요청을 전달한다.
- `assistant`는 이전 모델 응답 또는 생성 결과를 나타낸다.
- `tool`은 외부 도구 실행 결과를 모델에게 전달한다.
- 응답에는 `content`, `finish_reason`, `usage` 등이 포함될 수 있다.
- Provider마다 요청/응답 필드명이 다를 수 있다.

---

### [실무]

2026 실무 기준 Chat Completion은 Backend, RAG, Agent Workflow에서 기본 LLM 호출 방식으로 사용된다.

일반 요청 구조:

```json
{
  "model": "model-name",
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful backend development assistant."
    },
    {
      "role": "user",
      "content": "Spring Boot Service 코드를 리뷰해줘."
    }
  ],
  "temperature": 0.2,
  "max_tokens": 1000
}
```

권장 처리 흐름:

```text
User Request
→ Prompt Template 적용
→ Messages 생성
→ Parameter 설정
→ API 호출
→ HTTP Status 확인
→ Response Body 파싱
→ Empty Response 확인
→ Finish Reason 확인
→ Output Validation
→ Final Response 반환
```

실무 체크 항목:

- API Key는 환경변수로 관리한다.
- Timeout을 반드시 설정한다.
- HTTP Status Code를 확인한다.
- 응답 Content가 비어 있을 수 있음을 처리한다.
- `finish_reason`이 `length`이면 출력 잘림으로 처리한다.
- Usage 정보가 없을 수 있으므로 Optional 처리한다.
- Provider별 응답 구조 차이를 Adapter로 분리한다.

---

### [FAQ]

Q. Chat Completion이 뭐야?

A.
Message 배열을 입력받아 대화형 Assistant Response를 생성하는 LLM API 방식이다.

Q. Chat Completion과 단순 Text Generation 차이는?

A.
Chat Completion은 role 기반 Message 구조를 사용하고, Text Generation은 보통 단일 Prompt 문자열 중심이다.

Q. Chat Completion에서 가장 중요한 필드는 뭐야?

A.
`model`, `messages`, `temperature`, `max_tokens`, `response content`, `finish_reason`이다.

Q. Chat Completion 응답은 항상 같은 구조야?

A.
아니다. API Provider마다 필드명, usage 제공 여부, tool 호출 방식이 다를 수 있다.

---

## 1.2 Request Body

### [개념]

Request Body는 LLM API에 전달되는 JSON 요청 데이터이다.

Chat Completion Request Body는 모델, 메시지, 파라미터, 출력 형식, Tool 정의를 포함할 수 있다.

대표 필드:

- `model`
- `messages`
- `temperature`
- `top_p`
- `max_tokens`
- `stop`
- `stream`
- `response_format`
- `tools`
- `tool_choice`

---

### [핵심]

- `model`은 사용할 LLM 모델을 지정한다.
- `messages`는 role과 content로 구성된 대화 입력이다.
- `temperature`는 출력 다양성을 조절한다.
- `max_tokens`는 출력 길이를 제한한다.
- `stream`은 Streaming Response 사용 여부를 지정한다.
- `response_format`은 JSON Output 또는 Structured Output에 사용될 수 있다.
- `tools`는 Function Calling 또는 Tool Calling에 사용된다.
- 모든 Provider가 동일한 필드를 지원하지 않는다.

---

### [실무]

기본 Request Body 예:

```json
{
  "model": "qwen2.5:14b",
  "messages": [
    {
      "role": "system",
      "content": "You are a Korean backend code review assistant."
    },
    {
      "role": "user",
      "content": "다음 Controller 코드를 리뷰해줘."
    }
  ],
  "temperature": 0.2,
  "max_tokens": 1200
}
```

RAG Request Body 예:

```json
{
  "model": "model-name",
  "messages": [
    {
      "role": "system",
      "content": "Answer only using the retrieved context. If not found, say it is not found in the documents."
    },
    {
      "role": "user",
      "content": "Question: JWT 인증 흐름은?\n\nRetrieved Context:\n..."
    }
  ],
  "temperature": 0.1,
  "max_tokens": 1500
}
```

Structured Output Request Body 예:

```json
{
  "model": "model-name",
  "messages": [
    {
      "role": "system",
      "content": "Return valid JSON only."
    },
    {
      "role": "user",
      "content": "다음 요구사항을 API 설계 JSON으로 변환해줘."
    }
  ],
  "temperature": 0.1,
  "response_format": {
    "type": "json_object"
  }
}
```

주의:

- `messages`가 비어 있으면 요청 실패 가능성이 높다.
- `max_tokens`가 너무 작으면 응답이 잘린다.
- `temperature`를 작업 목적과 무관하게 높게 설정하지 않는다.
- JSON Output은 응답 파싱과 Schema Validation이 필요하다.
- Provider가 지원하지 않는 필드를 보내면 400 Bad Request가 발생할 수 있다.

---

### [FAQ]

Q. Request Body는 뭐야?

A.
LLM API에 전달하는 JSON 요청 데이터이며 모델, 메시지, 파라미터를 포함한다.

Q. `messages`에는 무엇을 넣어?

A.
System Message, User Message, Assistant Message, Tool Message를 role 기반으로 넣는다.

Q. `max_tokens`는 왜 필요해?

A.
응답 길이, 비용, Latency를 제한하고 출력이 과도하게 길어지는 것을 막기 위해 필요하다.

Q. Provider마다 Request Body가 달라?

A.
그렇다. OpenAI-compatible 구조를 지원해도 세부 필드와 기능 지원 범위는 다를 수 있다.

---

## 1.3 Response Body

### [개념]

Response Body는 LLM API 호출 결과로 반환되는 JSON 응답 데이터이다.

Response Body에는 생성된 Assistant Message, 종료 사유, Token Usage, Tool Call 정보, Error 정보가 포함될 수 있다.

대표 필드:

- `id`
- `model`
- `choices`
- `message`
- `content`
- `finish_reason`
- `usage`
- `prompt_tokens`
- `completion_tokens`
- `total_tokens`
- `tool_calls`
- `error`

---

### [핵심]

- 생성된 답변은 보통 `choices[0].message.content`에 들어간다.
- `finish_reason`은 응답 종료 원인을 나타낸다.
- `usage`는 Token 사용량 추적에 사용된다.
- Tool Calling 응답은 `content` 대신 `tool_calls`를 포함할 수 있다.
- 응답 Content가 비어 있을 수 있다.
- Error Response는 정상 Response와 구조가 다를 수 있다.

---

### [실무]

일반 Response Body 예:

```json
{
  "id": "chatcmpl-xxx",
  "model": "model-name",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "JWT 인증은 Access Token을 검증해 사용자를 인증하는 방식입니다."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 500,
    "completion_tokens": 120,
    "total_tokens": 620
  }
}
```

응답 처리 Flow:

```text
Response Body
→ choices 존재 확인
→ message 존재 확인
→ content 또는 tool_calls 확인
→ finish_reason 확인
→ usage 기록
→ output 검증
```

`finish_reason` 처리 기준:

| finish_reason  | 의미                                  | 처리                   |
| -------------- | ------------------------------------- | ---------------------- |
| stop           | 정상 종료                             | 정상 처리              |
| length         | Max Tokens 또는 Context 제한으로 잘림 | 재요청 또는 잘림 표시  |
| tool_calls     | Tool 호출 필요                        | Tool 실행 단계로 이동  |
| content_filter | 안전 정책으로 차단                    | 안전 실패 처리         |
| null           | Streaming 중간 상태 가능              | 최종 응답 조립 후 확인 |

주의:

- `choices`가 비어 있을 수 있다.
- `message.content`가 빈 문자열일 수 있다.
- `usage`가 항상 제공된다고 가정하지 않는다.
- `finish_reason=length`이면 완성된 답변으로 사용하지 않는다.
- JSON Output은 Content 문자열을 다시 JSON 파싱해야 한다.

---

### [FAQ]

Q. Response Body는 뭐야?

A.
LLM API 호출 후 반환되는 JSON 응답이며 생성 결과, 종료 사유, Token 사용량 등을 포함한다.

Q. 답변 텍스트는 어디에 있어?

A.
OpenAI-compatible 구조에서는 보통 `choices[0].message.content`에 있다.

Q. `finish_reason`은 왜 확인해?

A.
응답이 정상 종료되었는지, 길이 제한으로 잘렸는지, Tool 호출이 필요한지 판단하기 위해 확인한다.

Q. `usage`는 항상 있어?

A.
아니다. Provider나 호출 방식에 따라 없을 수 있으므로 Optional로 처리해야 한다.

---

# 2. Model and Message Design

## 2.1 Model Field

### [개념]

`model` 필드는 Chat Completion 요청에서 사용할 LLM 모델을 지정한다.

모델 선택은 응답 품질, 비용, 속도, Context Window, Tool Support에 영향을 준다.

모델 유형:

- General Chat Model
- Code Model
- Reasoning Model
- Vision Model
- Embedding Model
- Local LLM
- API LLM

---

### [핵심]

- 모든 작업에 하나의 모델만 사용하는 것이 최선은 아니다.
- 코드 생성은 Code Model 또는 Reasoning Model이 유리하다.
- 문서 검색에는 Embedding Model이 필요하다.
- RAG 답변 생성에는 Chat Model이 필요하다.
- 이미지 입력에는 Vision Model이 필요하다.
- Local LLM은 비용과 프라이버시에 장점이 있다.
- API LLM은 품질과 편의성에 장점이 있다.

---

### [실무]

작업별 모델 선택 기준:

| 작업               | 권장 모델                       |
| ------------------ | ------------------------------- |
| 일반 질의응답      | General Chat Model              |
| 코드 생성          | Code Model                      |
| 코드 리뷰          | Reasoning Model 또는 Code Model |
| RAG 답변           | Chat Model                      |
| 문서 검색          | Embedding Model                 |
| 이미지 분석        | Vision Model                    |
| Agent Tool Calling | Tool Support Model              |
| 로컬 개인 서버     | Local LLM                       |

개인 AI 서버 예:

```text
Chat / Code Generation
→ Qwen2.5 14B

Embedding / Semantic Search
→ BGE-M3

Vision / Image Input
→ Qwen2.5-VL 7B

RAG Workspace
→ AnythingLLM

Local Model Runtime
→ Ollama
```

모델 선택 체크리스트:

- 작업이 코드 중심인가?
- 긴 Context Window가 필요한가?
- Tool Calling을 지원하는가?
- 응답 속도가 중요한가?
- 비용 제한이 있는가?
- 로컬 하드웨어에서 실행 가능한가?
- 한국어 응답 품질이 충분한가?

---

### [FAQ]

Q. `model` 필드는 뭐야?

A.
LLM API 요청에서 사용할 모델 이름을 지정하는 필드다.

Q. Chat Model과 Embedding Model 차이는?

A.
Chat Model은 답변을 생성하고, Embedding Model은 검색을 위한 Vector를 생성한다.

Q. 코드 생성은 어떤 모델이 좋아?

A.
Code Model 또는 강한 Reasoning Model이 유리하다.

Q. Local LLM과 API LLM 중 뭐가 좋아?

A.
Local LLM은 비용과 프라이버시에 좋고, API LLM은 품질과 관리 편의성에 좋다.

---

## 2.2 Messages Field

### [개념]

`messages` 필드는 Chat Completion의 핵심 입력이다.

`messages`는 role과 content를 가진 객체 배열로 구성된다.

기본 Message Role:

- `system`
- `user`
- `assistant`
- `tool`

기본 구조:

```json
[
  {
    "role": "system",
    "content": "You are a backend development assistant."
  },
  {
    "role": "user",
    "content": "Spring Boot Controller 코드를 리뷰해줘."
  }
]
```

---

### [핵심]

- `system`은 모델의 상위 행동 규칙이다.
- `user`는 현재 사용자 요청이다.
- `assistant`는 이전 모델 응답 또는 대화 이력이다.
- `tool`은 외부 도구 실행 결과이다.
- Message 순서는 모델 응답에 영향을 줄 수 있다.
- Conversation History가 길면 Token 비용이 증가한다.
- 잘못된 이전 응답을 넣으면 오류가 누적될 수 있다.

---

### [실무]

일반 Chat Message 구성:

```text
System Message
→ User Message
```

대화형 Message 구성:

```text
System Message
→ User Message
→ Assistant Message
→ User Message
```

RAG Message 구성:

```text
System Message:
RAG 답변 규칙

User Message:
현재 질문 + Retrieved Context
```

Agent Message 구성:

```text
System Message:
Agent Role + Global Rules

User Message:
Current Task + State Summary + Output Schema

Tool Message:
Tool Result
```

권장 Message Template:

```json
[
  {
    "role": "system",
    "content": "You are a RAG-based assistant. Use only retrieved context."
  },
  {
    "role": "user",
    "content": "Question:\n{question}\n\nRetrieved Context:\n{context}"
  }
]
```

주의:

- System Message에 너무 많은 일회성 정보를 넣지 않는다.
- User Message에 Secret이나 API Key를 넣지 않는다.
- Retrieved Context와 User Question을 명확히 분리한다.
- Tool Result는 검증된 데이터만 전달한다.
- Conversation History는 요약 후 삽입한다.

---

### [FAQ]

Q. `messages` 필드는 왜 중요해?

A.
Chat Completion은 `messages` 배열을 기반으로 응답을 생성하기 때문이다.

Q. `system` role은 언제 사용해?

A.
모델의 역할, 응답 규칙, 금지 조건, 출력 형식을 지정할 때 사용한다.

Q. `assistant` role은 언제 넣어?

A.
이전 모델 응답을 대화 이력으로 유지해야 할 때 넣는다.

Q. `tool` role은 언제 사용해?

A.
외부 도구 실행 결과를 모델에게 전달할 때 사용한다.

---

# 3. Parameter Control

## 3.1 Temperature

### [개념]

Temperature는 LLM 출력의 무작위성과 다양성을 조절하는 Parameter이다.

Temperature가 낮으면 응답이 일관적이고 보수적이다.

Temperature가 높으면 응답이 다양하고 창의적이지만 Hallucination 가능성이 증가한다.

---

### [핵심]

- 낮은 Temperature는 정확성과 일관성에 유리하다.
- 높은 Temperature는 창의성과 다양성에 유리하다.
- 코드 생성, 코드 리뷰, RAG 답변은 낮은 Temperature가 적합하다.
- 기획 아이디어나 창작은 중간~높은 Temperature를 사용할 수 있다.
- Temperature 0이어도 완전한 결정론을 보장하지 않는다.

---

### [실무]

작업별 Temperature 기준:

| 작업          | 권장 방향 |
| ------------- | --------- |
| 코드 생성     | 낮게      |
| 코드 리뷰     | 낮게      |
| RAG 답변      | 낮게      |
| JSON Output   | 낮게      |
| 문서 요약     | 낮게~중간 |
| 요구사항 정리 | 낮게~중간 |
| 아이디어 발산 | 중간      |
| 창작          | 높게      |

권장 예:

```json
{
  "temperature": 0.1
}
```

개발 Agent 기준:

```text
Backend Agent
→ temperature 낮게

Review Agent
→ temperature 낮게

PM Agent Brainstorming
→ temperature 중간 가능

RAG Answer Agent
→ temperature 낮게
```

주의:

- Temperature를 높이면 근거 없는 생성 가능성이 증가한다.
- 낮은 Temperature가 사실 정확성을 자동 보장하지 않는다.
- RAG 답변은 Temperature보다 Retrieved Context 품질이 더 중요할 수 있다.
- JSON Output은 낮은 Temperature와 Schema Validation을 함께 적용한다.

---

### [FAQ]

Q. Temperature가 뭐야?

A.
LLM 출력의 무작위성과 다양성을 조절하는 Parameter다.

Q. 코드 생성에는 Temperature를 어떻게 설정해?

A.
낮게 설정하는 것이 좋다. 일관성과 재현성이 중요하기 때문이다.

Q. RAG 답변에는 Temperature를 어떻게 설정해?

A.
낮게 설정한다. 문서 근거 중심으로 안정적인 답변을 생성해야 하기 때문이다.

Q. Temperature 0이면 항상 같은 답이 나와?

A.
아니다. 구현, 모델, 서버 환경에 따라 완전한 결정론이 보장되지 않을 수 있다.

---

## 3.2 Top-p

### [개념]

Top-p는 Nucleus Sampling이라고도 하며, 누적 확률이 특정 값에 도달할 때까지의 후보 Token 집합에서 다음 Token을 선택하는 Parameter이다.

Top-p는 Temperature와 함께 출력 다양성에 영향을 준다.

---

### [핵심]

- Top-p는 후보 Token 범위를 확률 질량 기준으로 제한한다.
- 낮은 Top-p는 선택 가능한 Token 범위를 줄인다.
- 높은 Top-p는 더 다양한 Token을 허용한다.
- Temperature와 Top-p를 동시에 크게 조정하면 출력 예측이 어려워진다.
- 실무에서는 기본값을 유지하거나 한쪽만 조정하는 경우가 많다.

---

### [실무]

일반 기준:

| 작업        | Top-p 기준       |
| ----------- | ---------------- |
| 코드 생성   | 기본값 또는 낮게 |
| 코드 리뷰   | 기본값 또는 낮게 |
| RAG 답변    | 기본값 또는 낮게 |
| JSON Output | 기본값 또는 낮게 |
| 창의적 생성 | 중간~높게        |

예시:

```json
{
  "temperature": 0.2,
  "top_p": 0.9
}
```

권장 방식:

```text
정확성 중심 작업
→ Temperature 낮게
→ Top-p 기본값 유지

창의성 중심 작업
→ Temperature 또는 Top-p 중 하나만 조정
→ 결과 품질 테스트
```

주의:

- Top-p 지원 여부는 Provider마다 다르다.
- Temperature와 Top-p를 동시에 공격적으로 조정하지 않는다.
- RAG와 코드 작업에서는 출력 다양성보다 근거성과 일관성이 중요하다.

---

### [FAQ]

Q. Top-p가 뭐야?

A.
다음 Token 후보를 누적 확률 기준으로 제한하는 Sampling Parameter다.

Q. Temperature와 Top-p 차이는?

A.
Temperature는 확률 분포의 날카로움을 조절하고, Top-p는 후보 Token 범위를 제한한다.

Q. Top-p는 꼭 설정해야 해?

A.
아니다. 기본값을 유지하고 Temperature만 조정하는 방식도 많이 사용된다.

Q. 코드 생성에서 Top-p를 높게 잡아도 돼?

A.
권장하지 않는다. 코드 생성은 다양성보다 일관성과 정확성이 중요하다.

---

## 3.3 Max Tokens

### [개념]

Max Tokens는 LLM이 생성할 수 있는 최대 Output Token 수를 제한하는 Parameter이다.

Max Tokens는 응답 길이, 비용, Latency, 출력 잘림에 직접 영향을 준다.

---

### [핵심]

- Max Tokens는 출력 길이를 제한한다.
- 값이 너무 작으면 응답이 중간에 잘린다.
- 값이 너무 크면 비용과 Latency가 증가한다.
- `finish_reason=length`이면 Max Tokens 제한으로 출력이 잘렸을 수 있다.
- JSON Output에서는 잘림이 발생하면 파싱 실패 가능성이 높다.

---

### [실무]

작업별 Max Tokens 기준:

| 작업          | 기준                       |
| ------------- | -------------------------- |
| 짧은 FAQ 답변 | 작게                       |
| 코드 리뷰     | 중간                       |
| 긴 문서 요약  | 중간~크게                  |
| 코드 생성     | 중간~크게                  |
| JSON Output   | Schema 크기에 맞게         |
| RAG 답변      | Context와 출력 요구에 맞게 |

예시:

```json
{
  "max_tokens": 1500
}
```

Output Reserve 설계:

```text
Context Window
→ System Message
→ User Message
→ Retrieved Context
→ Output Reserve
```

주의:

- Max Tokens는 입력 Token 제한이 아니라 출력 Token 제한이다.
- Context Window 전체 한도도 함께 고려해야 한다.
- 긴 RAG Context와 긴 Output을 동시에 요구하면 실패할 수 있다.
- 출력이 잘리면 사용자에게 완성 답변처럼 보여주면 안 된다.

---

### [FAQ]

Q. Max Tokens가 뭐야?

A.
LLM이 생성할 수 있는 최대 Output Token 수를 제한하는 Parameter다.

Q. Max Tokens를 크게 하면 좋아?

A.
항상 그렇지 않다. 비용과 Latency가 증가하고 불필요하게 긴 응답이 나올 수 있다.

Q. Max Tokens가 너무 작으면 어떻게 돼?

A.
응답이 중간에 잘리고 `finish_reason=length`가 발생할 수 있다.

Q. JSON Output에서 Max Tokens가 중요한 이유는?

A.
출력이 잘리면 JSON 구조가 깨져 파싱 실패가 발생할 수 있기 때문이다.

---

## 3.4 Stop Sequence

### [개념]

Stop Sequence는 LLM이 특정 문자열을 생성하면 출력을 중단하도록 하는 Parameter이다.

Stop Sequence는 출력 형식 제어, 불필요한 후속 문장 방지, 섹션 경계 제어에 사용할 수 있다.

---

### [핵심]

- Stop Sequence는 출력 중단 조건이다.
- 특정 문자열이 나오면 모델 생성을 멈춘다.
- 형식 제어에 유용하다.
- 잘못 설정하면 필요한 내용도 잘릴 수 있다.
- Provider마다 지원 방식이 다를 수 있다.

---

### [실무]

예시:

```json
{
  "stop": ["\nUser:", "\nSystem:"]
}
```

사용 사례:

```text
대화 재현 방지
→ "\nUser:"에서 중단

섹션 경계 제어
→ "---END---"에서 중단

불필요한 추가 답변 방지
→ 특정 종료 Marker 사용
```

주의:

- Stop Sequence가 응답 본문에 자연스럽게 등장하면 출력이 잘릴 수 있다.
- JSON Output에서는 Stop Sequence 사용을 신중히 결정한다.
- Markdown 문서 생성 시 일반 구분자 `---`를 Stop Sequence로 쓰면 위험하다.
- Stop Sequence는 Schema Validation을 대체하지 않는다.

---

### [FAQ]

Q. Stop Sequence가 뭐야?

A.
모델이 특정 문자열을 생성하면 출력을 중단하도록 하는 Parameter다.

Q. Stop Sequence는 언제 사용해?

A.
대화 경계, 섹션 종료, 불필요한 추가 출력을 막고 싶을 때 사용한다.

Q. Stop Sequence를 잘못 설정하면?

A.
필요한 답변이 중간에서 잘릴 수 있다.

Q. JSON Output에서 Stop Sequence를 써도 돼?

A.
가능하지만 JSON이 중간에서 잘릴 수 있으므로 신중하게 사용해야 한다.

---

# 4. Chat Completion Implementation

## 4.1 Python HTTP Client

### [개념]

Python HTTP Client는 LLM API를 호출하기 위한 Python 기반 요청 코드이다.

대표 라이브러리:

- `requests`
- `httpx`

LLM API 호출에는 Header, JSON Body, Timeout, Error Handling이 필요하다.

---

### [핵심]

- Authorization Header에 API Key를 넣는다.
- API Key는 환경변수에서 읽는다.
- 요청 Body는 JSON으로 전송한다.
- Timeout을 반드시 설정한다.
- HTTP Status Code를 확인한다.
- Response Body를 파싱하고 검증한다.
- Secret을 로그에 남기지 않는다.

---

### [실무]

Python `requests` 예시:

```python
import os
import requests

api_key = os.environ.get("LLM_API_KEY")
if not api_key:
    raise ValueError("LLM_API_KEY is required")

response = requests.post(
    "https://api.example.com/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    },
    json={
        "model": "model-name",
        "messages": [
            {
                "role": "system",
                "content": "You are a backend development assistant."
            },
            {
                "role": "user",
                "content": "Spring Boot Service 코드를 리뷰해줘."
            }
        ],
        "temperature": 0.2,
        "max_tokens": 1000
    },
    timeout=30
)

response.raise_for_status()
data = response.json()

content = data["choices"][0]["message"]["content"]
print(content)
```

안전 처리 기준:

```text
API Key 확인
→ Request 생성
→ Timeout 설정
→ Status Code 확인
→ JSON Parse
→ choices/message/content 확인
→ finish_reason 확인
→ 반환
```

주의:

- API Key를 코드에 하드코딩하지 않는다.
- Timeout 없는 요청을 만들지 않는다.
- `data["choices"][0]`를 검증 없이 접근하지 않는다.
- Production에서는 예외를 사용자 친화적 메시지로 변환한다.
- Prompt 전문 로그 저장은 보안 기준을 먼저 정한다.

---

### [FAQ]

Q. Python에서 LLM API는 어떻게 호출해?

A.
`requests` 또는 `httpx`로 Authorization Header, JSON Body, Timeout을 설정해 호출한다.

Q. API Key는 어디에 둬야 해?

A.
환경변수 또는 Secret Manager에 둔다. 코드에 하드코딩하면 안 된다.

Q. `response.raise_for_status()`는 왜 사용해?

A.
HTTP 오류 상태를 예외로 처리하기 위해 사용한다.

Q. 응답 Content를 바로 써도 돼?

A.
권장하지 않는다. Empty Response, finish_reason, Schema 등을 검증해야 한다.

---

## 4.2 Java Spring WebClient

### [개념]

Spring WebClient는 Spring Boot에서 HTTP API를 호출하기 위한 Non-blocking HTTP Client이다.

LLM API 연동에서는 WebClient로 Chat Completion Endpoint를 호출할 수 있다.

---

### [핵심]

- API Key는 환경변수 또는 설정 파일에서 주입한다.
- Authorization Header를 설정한다.
- Request DTO와 Response DTO를 분리한다.
- Timeout 설정이 필요하다.
- Error Status 처리가 필요하다.
- Response Body는 DTO로 파싱한다.
- Retry는 제한적으로 적용한다.

---

### [실무]

Spring WebClient 예시:

```java
@Service
public class LlmClient {

    private final WebClient webClient;
    private final String apiKey;

    public LlmClient(
            WebClient.Builder webClientBuilder,
            @Value("${llm.api-key}") String apiKey
    ) {
        this.webClient = webClientBuilder
                .baseUrl("https://api.example.com/v1")
                .build();
        this.apiKey = apiKey;
    }

    public String chat(List<LlmMessage> messages) {
        LlmChatRequest request = new LlmChatRequest(
                "model-name",
                messages,
                0.2,
                1000
        );

        LlmChatResponse response = webClient.post()
                .uri("/chat/completions")
                .header(HttpHeaders.AUTHORIZATION, "Bearer " + apiKey)
                .contentType(MediaType.APPLICATION_JSON)
                .bodyValue(request)
                .retrieve()
                .bodyToMono(LlmChatResponse.class)
                .block(Duration.ofSeconds(30));

        if (response == null || response.choices().isEmpty()) {
            throw new IllegalStateException("Empty LLM response");
        }

        return response.choices().get(0).message().content();
    }
}
```

DTO 예시:

```java
public record LlmMessage(
        String role,
        String content
) {
}

public record LlmChatRequest(
        String model,
        List<LlmMessage> messages,
        double temperature,
        int max_tokens
) {
}

public record LlmChatResponse(
        List<LlmChoice> choices,
        LlmUsage usage
) {
}

public record LlmChoice(
        int index,
        LlmMessage message,
        String finish_reason
) {
}

public record LlmUsage(
        Integer prompt_tokens,
        Integer completion_tokens,
        Integer total_tokens
) {
}
```

운영 기준:

- `@Value` 또는 ConfigurationProperties로 Secret을 주입한다.
- API Key는 Git에 올리지 않는다.
- Timeout은 Connection Timeout과 Read Timeout을 함께 고려한다.
- `finish_reason` 확인 로직을 추가한다.
- 429, 500 계열 오류는 Retry 정책을 분리한다.
- 400, 401, 403은 Retry하지 않는다.

주의:

- `.block()` 사용은 호출 위치와 Thread 모델을 고려해야 한다.
- WebFlux 전체 구조가 아니라면 동기 처리 기준을 명확히 한다.
- Error Body를 로깅할 때 Prompt와 Secret 노출을 피한다.
- DTO는 Provider별 응답 구조 변화에 대비한다.

---

### [FAQ]

Q. Spring Boot에서 LLM API는 어떻게 호출해?

A.
WebClient 또는 RestClient를 사용해 Authorization Header와 JSON Body를 보내 호출한다.

Q. WebClient에서 Timeout은 꼭 필요해?

A.
필요하다. Timeout이 없으면 요청이 오래 대기하며 Thread나 Connection을 점유할 수 있다.

Q. Request DTO와 Response DTO를 분리해야 해?

A.
권장한다. API 요청 구조와 응답 구조가 다르기 때문이다.

Q. LLM API 오류는 Controller에서 바로 처리해도 돼?

A.
가능하지만 Client 계층에서 예외를 분류하고 Service 또는 GlobalExceptionHandler에서 변환하는 구조가 좋다.

---

## 4.3 JavaScript Fetch / Axios

### [개념]

JavaScript Fetch 또는 Axios는 Frontend나 Node.js Backend에서 LLM API를 호출할 때 사용할 수 있는 HTTP Client이다.

단, Browser Frontend에서 Secret API Key를 직접 사용하면 안 된다.

---

### [핵심]

- API Key는 Frontend 코드에 포함하면 안 된다.
- Browser에서 LLM Provider로 직접 호출하면 Secret이 노출된다.
- Frontend는 Backend API를 호출하고 Backend가 LLM API를 호출하는 구조가 안전하다.
- Node.js Backend에서는 환경변수로 API Key를 관리한다.
- Axios Interceptor에는 Secret 로그가 남지 않도록 주의한다.

---

### [실무]

권장 구조:

```text
React Frontend
→ Backend API
→ LLM API
→ Backend Response
→ React UI
```

Node.js Fetch 예시:

```javascript
const apiKey = process.env.LLM_API_KEY;

if (!apiKey) {
  throw new Error("LLM_API_KEY is required");
}

const response = await fetch("https://api.example.com/v1/chat/completions", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${apiKey}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    model: "model-name",
    messages: [
      {
        role: "system",
        content: "You are a helpful assistant.",
      },
      {
        role: "user",
        content: "Summarize this text.",
      },
    ],
    temperature: 0.2,
    max_tokens: 1000,
  }),
});

if (!response.ok) {
  throw new Error(`LLM API failed: ${response.status}`);
}

const data = await response.json();
const content = data.choices?.[0]?.message?.content;

if (!content) {
  throw new Error("Empty LLM response");
}

console.log(content);
```

React에서 금지되는 구조:

```text
React Frontend
→ LLM Provider API 직접 호출
→ Browser Bundle에 API Key 포함
→ Secret 노출
```

주의:

- `.env`에 넣은 Frontend 환경변수는 빌드 결과에 노출될 수 있다.
- `REACT_APP_`, `VITE_` 접두사의 값은 Browser에서 접근 가능하다.
- LLM API Key는 반드시 Backend에서 보호한다.
- CORS 우회 목적으로 Secret을 Frontend에 넣지 않는다.

---

### [FAQ]

Q. React에서 LLM API Key를 `.env`에 넣어도 돼?

A.
안 된다. React 빌드에 포함되는 환경변수는 Browser에서 노출될 수 있다.

Q. Frontend에서 LLM API를 직접 호출하면 안 되는 이유는?

A.
API Key가 사용자 브라우저에 노출되기 때문이다.

Q. 안전한 구조는 뭐야?

A.
Frontend는 Backend API만 호출하고, Backend가 LLM Provider API를 호출하는 구조다.

Q. Node.js Backend에서는 API Key를 어디에 둬?

A.
환경변수 또는 Secret Manager에 둔다.

---

# 5. Response Parsing and Validation

## 5.1 Content Parsing

### [개념]

Content Parsing은 LLM API 응답에서 실제 Assistant 답변을 추출하는 과정이다.

Chat Completion 응답은 중첩 구조이므로 안전한 접근과 검증이 필요하다.

---

### [핵심]

- `choices` 존재 여부를 확인한다.
- 첫 번째 Choice가 항상 있다고 가정하지 않는다.
- `message` 존재 여부를 확인한다.
- `content`가 비어 있을 수 있다.
- Tool Calling 응답은 `content` 대신 `tool_calls`를 포함할 수 있다.
- Streaming 응답은 Chunk를 누적해 최종 Content를 만든다.

---

### [실무]

안전 파싱 Flow:

```text
Response
→ choices 존재 확인
→ choices[0] 존재 확인
→ message 존재 확인
→ content 또는 tool_calls 확인
→ finish_reason 확인
→ content 반환
```

Python 안전 파싱 예:

```python
def extract_content(data: dict) -> str:
    choices = data.get("choices") or []
    if not choices:
        raise ValueError("LLM response has no choices")

    message = choices[0].get("message") or {}
    content = message.get("content")

    if not content:
        raise ValueError("LLM response content is empty")

    finish_reason = choices[0].get("finish_reason")
    if finish_reason == "length":
        raise ValueError("LLM response was truncated")

    return content
```

검증 항목:

- Empty Response
- Missing Choices
- Missing Message
- Empty Content
- Finish Reason Length
- Invalid JSON
- Missing Required Field
- Tool Calls Without Tool Execution

주의:

- LLM Output은 항상 신뢰하면 안 된다.
- JSON 문자열은 다시 JSON 파싱해야 한다.
- Markdown 응답과 JSON 응답 처리 로직을 분리한다.
- Validation 실패 시 재요청 또는 안전 실패 처리한다.

---

### [FAQ]

Q. Content Parsing이 뭐야?

A.
LLM API 응답에서 실제 Assistant 답변 텍스트를 추출하는 과정이다.

Q. `choices[0]`를 바로 접근해도 돼?

A.
권장하지 않는다. `choices`가 비어 있거나 응답 구조가 다를 수 있다.

Q. Content가 비어 있으면 어떻게 해?

A.
Empty Response로 처리하고 재요청 또는 실패 응답을 반환한다.

Q. Tool Calling 응답도 Content가 있어?

A.
항상 그렇지 않다. Tool 호출 응답은 `tool_calls`만 포함할 수 있다.

---

## 5.2 Finish Reason Validation

### [개념]

Finish Reason Validation은 LLM 응답이 어떤 이유로 종료되었는지 확인하는 검증 과정이다.

`finish_reason`은 응답을 정상적으로 사용할 수 있는지 판단하는 핵심 필드이다.

---

### [핵심]

- `stop`은 정상 종료이다.
- `length`는 출력이 잘렸을 가능성이 높다.
- `tool_calls`는 Tool 실행이 필요하다는 의미이다.
- `content_filter`는 안전 정책에 의해 차단된 응답일 수 있다.
- Streaming에서는 최종 Chunk까지 확인해야 한다.
- Provider마다 Finish Reason 값이 다를 수 있다.

---

### [실무]

Finish Reason 처리 Flow:

```text
finish_reason 확인
→ stop이면 정상 처리
→ length이면 출력 잘림 처리
→ tool_calls이면 Tool 실행
→ content_filter이면 안전 실패 처리
→ 알 수 없는 값이면 보수적 실패 처리
```

예시 처리 기준:

```python
def validate_finish_reason(finish_reason: str | None) -> None:
    if finish_reason == "stop":
        return

    if finish_reason == "length":
        raise ValueError("LLM response was truncated")

    if finish_reason == "tool_calls":
        raise ValueError("Tool call required")

    if finish_reason == "content_filter":
        raise ValueError("LLM response was blocked by content filter")

    raise ValueError(f"Unexpected finish_reason: {finish_reason}")
```

주의:

- `finish_reason=length`인 응답을 완성 답변으로 사용하지 않는다.
- Tool Calling 단계에서는 `content`가 없어도 정상일 수 있다.
- Finish Reason이 없을 수 있으므로 Optional 처리한다.
- Provider별 Finish Reason 값을 문서화한다.

---

### [FAQ]

Q. Finish Reason이 뭐야?

A.
LLM 응답이 어떤 이유로 종료되었는지 나타내는 값이다.

Q. `finish_reason=stop`은 무슨 뜻이야?

A.
정상적으로 응답 생성이 종료되었다는 의미다.

Q. `finish_reason=length`는 무슨 뜻이야?

A.
Max Tokens나 Context 제한으로 응답이 중간에 잘렸을 수 있다는 의미다.

Q. Finish Reason은 꼭 확인해야 해?

A.
그렇다. 잘린 응답이나 Tool 호출 필요 상태를 구분해야 하기 때문이다.

---

## 5.3 Usage Logging

### [개념]

Usage Logging은 LLM API 호출에서 사용된 Token 수, 모델명, Latency, Error Code 등을 기록하는 작업이다.

Usage Logging은 비용 관리, 장애 분석, 성능 최적화에 필요하다.

---

### [핵심]

- Token Usage는 비용 추적에 필요하다.
- Latency는 사용자 경험과 성능 분석에 필요하다.
- Model Name은 품질 비교와 비용 비교에 필요하다.
- Request ID는 장애 추적에 필요하다.
- Retry Count는 API 안정성 분석에 필요하다.
- API Key와 Prompt 내 민감정보는 로그에 남기면 안 된다.

---

### [실무]

권장 로그 항목:

```text
requestId
model
inputTokens
outputTokens
totalTokens
latencyMs
status
finishReason
errorCode
retryCount
```

로그 예:

```json
{
  "requestId": "req-123",
  "model": "model-name",
  "inputTokens": 500,
  "outputTokens": 120,
  "totalTokens": 620,
  "latencyMs": 1350,
  "status": "success",
  "finishReason": "stop",
  "retryCount": 0
}
```

로그 Redaction 기준:

```text
API Key
Secret
Authorization Header
Personal Information
Raw Prompt
Sensitive User Input
Tool Arguments with Secret
```

주의:

- Prompt 전문을 항상 저장하지 않는다.
- Secret이 Error Log에 포함되지 않도록 한다.
- LLM 응답에도 민감정보가 포함될 수 있다.
- Usage가 없는 Provider에서는 별도 추정 또는 Null 처리한다.

---

### [FAQ]

Q. Usage Logging이 뭐야?

A.
LLM API 호출의 Token 사용량, 모델, Latency, 오류 정보를 기록하는 작업이다.

Q. Token Usage를 왜 기록해?

A.
비용 분석과 Context 최적화를 위해 필요하다.

Q. Prompt 전체를 로그로 남겨도 돼?

A.
권장하지 않는다. 개인정보, Secret, 내부 문서가 포함될 수 있기 때문이다.

Q. 로그에 절대 남기면 안 되는 것은?

A.
API Key, Authorization Header, Secret, 개인정보, 민감한 Prompt 내용이다.

---

# 6. Common Mistakes

## 6.1 Chat Completion Common Mistakes

### [개념]

Chat Completion Common Mistakes는 LLM API 요청/응답 구조를 잘못 이해해 발생하는 연동 오류이다.

---

### [핵심]

자주 발생하는 실수:

- API Key를 코드에 하드코딩
- Frontend에서 LLM API Key 직접 사용
- Timeout 없이 API 호출
- HTTP Status Code 확인 누락
- `choices[0]` 검증 없이 접근
- Empty Response 처리 누락
- `finish_reason=length` 무시
- Usage 정보가 항상 있다고 가정
- Provider별 응답 구조 차이 무시
- Temperature를 과도하게 높임
- Max Tokens를 너무 작게 설정
- JSON Output을 파싱/검증하지 않음
- Tool Calling 응답을 일반 Content 응답처럼 처리
- Prompt와 Retrieved Context를 구분하지 않음
- Secret을 로그에 남김

---

### [실무]

문제 해결 Flow:

```text
LLM API 호출 실패
→ HTTP Status 확인
→ Error Body 확인
→ API Key 확인
→ Request Body 확인
→ Timeout 확인
→ Rate Limit 확인
→ Provider 문서 확인
```

응답 이상 해결 Flow:

```text
LLM 응답 이상
→ choices 확인
→ content 확인
→ finish_reason 확인
→ usage 확인
→ Prompt 확인
→ Parameter 확인
→ Retrieved Context 확인
→ Output Validation 확인
```

예방 기준:

- API Client 계층을 분리한다.
- Request DTO와 Response DTO를 만든다.
- Provider Adapter를 둔다.
- 공통 Error Mapper를 만든다.
- Retry 정책을 오류 유형별로 분리한다.
- Output Validation을 필수화한다.
- Usage Logging을 적용한다.

---

### [FAQ]

Q. Chat Completion 연동에서 가장 흔한 실수는?

A.
Timeout, 응답 검증, finish_reason 확인, Error Handling을 누락하는 것이다.

Q. Frontend에서 API Key를 쓰면 왜 위험해?

A.
Browser Bundle이나 Network 요청을 통해 API Key가 사용자에게 노출될 수 있기 때문이다.

Q. 응답이 잘렸는지 어떻게 확인해?

A.
`finish_reason`이 `length`인지 확인한다.

Q. Tool Calling 응답을 일반 응답처럼 처리하면 어떻게 돼?

A.
`content`가 비어 있거나 Tool 실행 단계가 누락되어 Workflow가 깨질 수 있다.

---

# Retrieval Queries

### [FAQ]

Q. Chat Completion이 뭐야?
A. Message 배열을 입력받아 Assistant Response를 생성하는 대화형 LLM API 방식이다.

Q. Chat Completion API는 어떻게 호출해?
A. Model, Messages, Parameter를 포함한 JSON Request Body를 HTTP로 전송해 호출한다.

Q. Chat Completion Request Body에는 뭐가 들어가?
A. `model`, `messages`, `temperature`, `top_p`, `max_tokens`, `stream`, `tools`, `response_format` 등이 들어갈 수 있다.

Q. Chat Completion Response Body에는 뭐가 들어가?
A. `choices`, `message`, `content`, `finish_reason`, `usage`, `tool_calls`, `error` 등이 포함될 수 있다.

Q. `messages` 필드는 뭐야?
A. System, User, Assistant, Tool Message를 role 기반으로 전달하는 배열이다.

Q. `system` role은 뭐야?
A. 모델의 상위 행동 규칙, 역할, 출력 형식, 금지 조건을 지정하는 Message Role이다.

Q. `user` role은 뭐야?
A. 현재 사용자 요청이나 작업 지시를 전달하는 Message Role이다.

Q. `assistant` role은 뭐야?
A. 이전 모델 응답이나 대화 이력을 표현하는 Message Role이다.

Q. `tool` role은 뭐야?
A. 외부 Tool 실행 결과를 모델에게 전달하는 Message Role이다.

Q. `model` 필드는 뭐야?
A. Chat Completion 요청에 사용할 LLM 모델 이름을 지정하는 필드다.

Q. Temperature는 어떻게 설정해?
A. 코드 생성, 코드 리뷰, RAG 답변, JSON Output은 낮게 설정하고 창의적 작업은 중간 이상을 사용할 수 있다.

Q. Top-p는 뭐야?
A. 다음 Token 후보를 누적 확률 기준으로 제한하는 Sampling Parameter다.

Q. Max Tokens는 뭐야?
A. LLM이 생성할 수 있는 최대 Output Token 수를 제한하는 Parameter다.

Q. Stop Sequence는 뭐야?
A. 특정 문자열이 생성되면 출력을 중단시키는 Parameter다.

Q. Chat Completion 응답 텍스트는 어디에 있어?
A. OpenAI-compatible 구조에서는 보통 `choices[0].message.content`에 있다.

Q. `finish_reason`은 왜 확인해?
A. 응답이 정상 종료되었는지, 잘렸는지, Tool 호출이 필요한지 판단하기 위해 필요하다.

Q. `finish_reason=length`는 뭐야?
A. Max Tokens 또는 Context 제한으로 응답이 중간에 잘렸을 가능성이 있다는 의미다.

Q. Usage Logging은 왜 필요해?
A. Token 비용, Latency, 모델별 성능, 오류 분석을 위해 필요하다.

Q. Python에서 LLM API는 어떻게 호출해?
A. `requests` 또는 `httpx`로 Authorization Header, JSON Body, Timeout을 설정해 호출한다.

Q. Spring Boot에서 LLM API는 어떻게 호출해?
A. WebClient 또는 RestClient로 Request DTO를 전송하고 Response DTO를 파싱한다.

Q. JavaScript에서 LLM API 호출 시 주의할 점은?
A. Browser Frontend에 API Key를 넣지 말고 Backend를 통해 호출해야 한다.

Q. React `.env`에 LLM API Key를 넣어도 돼?
A. 안 된다. Frontend 환경변수는 빌드 결과에서 노출될 수 있다.

Q. Chat Completion 응답은 그대로 믿어도 돼?
A. 안 된다. Empty Response, Finish Reason, JSON Schema, Required Field를 검증해야 한다.

Q. Provider별 응답 구조 차이는 어떻게 처리해?
A. Provider Adapter 또는 Client 계층을 분리해 요청/응답 구조 차이를 흡수한다.

Q. Chat Completion 연동에서 가장 중요한 실무 기준은?
A. API Key 보안, Timeout, Error Handling, Response Validation, Usage Logging이다.
