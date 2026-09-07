# LLM Core & API Integration Domain Rules

---

# 1. Domain Purpose

LLM Core & API Integration Domain 문서는 AI Agent / Backend Agent / Review Agent용 RAG 문서 제작 규칙이다.

목적:

- LLM 기본 개념 이해
- LLM API 연동 코드 작성 지원
- Chat Completion / Text Generation 구조 이해
- System / User / Assistant Message 구조 이해
- Token / Context Window 관리
- Parameter 설정 기준 제공
- Streaming Response 처리
- Structured Output / JSON Output 처리
- API Error Handling / Retry / Timeout 기준 제공
- Agent / RAG 시스템과 LLM API 연결 지원

우선순위:

1. LLM Core Concept
2. API Request / Response Structure
3. Token / Context Management
4. Parameter Control
5. Structured Output
6. Error Handling
7. Integration Reliability

---

# 2. Scope

포함 범위:

- LLM Core
- Transformer 기초 개념
- Token
- Context Window
- Prompt
- System Message
- User Message
- Assistant Message
- Chat Completion
- Text Generation
- Model Selection
- Temperature
- Top-p
- Max Tokens
- Stop Sequence
- Streaming
- Structured Output
- JSON Output
- Function Calling / Tool Calling 기초
- Embedding API 기초
- API Key 관리
- Environment Variable
- HTTP Client
- Timeout
- Retry
- Rate Limit
- Error Handling
- Logging
- Cost / Latency 관리
- RAG Integration
- Agent Integration

제외 범위:

- LLM 학습 원리 심화
- Transformer 수학적 구조 심화
- Fine-Tuning 상세
- Model Quantization 상세
- Vector Database 구현 상세
- LangGraph Workflow 상세
- MLOps 운영 상세
- Agentic RAG 심화

---

# 3. Section Priority

## Required

- [개념]
- [핵심]
- [실무]
- [FAQ]

---

## Strongly Recommended

- [Flow]
- [예제]
- [주의]
- [Best Practice]
- [Troubleshooting]
- [Checklist]
- [Comparison]

---

# 4. LLM Core Rules

LLM Core 문서는 API 사용에 필요한 기본 개념 중심으로 작성한다.

반드시 포함:

- LLM이 무엇인가
- Token 기반 입력/출력
- Prompt와 Context의 역할
- Model은 확률적으로 다음 Token을 생성함
- Context Window 제한
- Parameter가 출력 품질에 미치는 영향
- LLM은 외부 사실을 항상 정확히 아는 것이 아님
- RAG / Tool Calling으로 한계를 보완 가능

기본 Flow:

```text
Prompt
→ Tokenization
→ Model Inference
→ Token Generation
→ Response
```

금지:

- LLM을 완전한 지식 DB처럼 설명
- Token / Context 제한을 무시한 설명
- Temperature만 조정하면 모든 문제가 해결된다는 설명
- API 호출 예제 없이 이론만 나열

---

# 5. Token Rules

Token은 LLM API 사용의 핵심 개념이다.

필수 포함:

- Token
- Input Token
- Output Token
- Total Token
- Token Limit
- Context Window
- Token Cost
- Token Truncation

반드시 설명:

- LLM은 문자를 Token 단위로 처리
- 입력 Prompt와 출력 Response 모두 Token을 사용
- Context Window를 초과하면 일부 정보가 누락되거나 요청이 실패할 수 있음
- Token 수는 비용과 Latency에 직접 영향
- 긴 문서는 요약 / Chunking / Retrieval이 필요

예시 Flow:

```text
System Prompt
+ User Prompt
+ Retrieved Context
+ Conversation History
→ Input Tokens
→ Model Response
→ Output Tokens
```

주의:

- 긴 대화 전체를 무조건 넣지 말 것
- RAG Context를 과도하게 넣지 말 것
- 출력 길이를 제한하지 않으면 비용과 Latency 증가
- Token Limit 초과 시 실패 처리 필요

---

# 6. Context Window Rules

Context Window 문서는 입력 정보 관리 중심으로 작성한다.

필수 포함:

- Context Window
- Conversation History
- Retrieved Context
- System Instruction
- Token Budget
- Context Truncation
- Context Compression

기본 구조:

```text
System Instruction
→ Conversation Summary
→ Retrieved Documents
→ User Task
```

반드시 설명:

- Context Window는 모델이 한 번에 참고할 수 있는 최대 범위
- 중요한 지시는 앞부분 또는 명확한 위치에 배치
- 관련 없는 Context는 제거
- 긴 대화는 요약 또는 최근 대화 중심으로 관리
- RAG에서는 Top-K와 Chunk 길이가 Context 사용량에 영향

주의:

- Context가 길수록 항상 좋은 것은 아님
- 관련 없는 문서가 많으면 답변 품질 저하
- 오래된 정보와 최신 정보 충돌 주의
- 중요한 제약이 잘리지 않도록 관리

---

# 7. Message Structure Rules

LLM API 문서는 Message 구조를 반드시 포함한다.

필수 포함:

- System Message
- User Message
- Assistant Message
- Tool Message
- Role
- Content
- Conversation History

기본 Flow:

```text
System Message
→ User Message
→ Assistant Message
→ User Message
→ Assistant Message
```

반드시 설명:

- System Message는 모델의 상위 행동 규칙
- User Message는 현재 사용자 요청
- Assistant Message는 이전 모델 응답
- Tool Message는 도구 실행 결과를 모델에 전달할 때 사용
- Conversation History는 문맥 유지에 사용되지만 Token을 소비

예시:

```json
[
  {
    "role": "system",
    "content": "You are an AI assistant for backend development."
  },
  {
    "role": "user",
    "content": "Spring Service 코드를 리뷰해줘."
  }
]
```

주의:

- System Message에 일회성 작업을 과도하게 넣지 말 것
- User Message와 Context를 혼동하지 말 것
- 이전 Assistant 응답이 잘못되었으면 그대로 재사용하지 않도록 주의
- Tool 결과는 사실 데이터로 취급하되 검증 필요

---

# 8. Chat Completion Rules

Chat Completion 문서는 대화형 LLM API의 기본 사용 방식으로 설명한다.

필수 포함:

- Request Body
- Model
- Messages
- Temperature
- Max Tokens
- Response
- Usage
- Finish Reason

기본 Flow:

```text
Client
→ Build Messages
→ Call LLM API
→ Receive Response
→ Parse Content
→ Handle Usage / Error
```

예시 구조:

```json
{
  "model": "model-name",
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful AI assistant."
    },
    {
      "role": "user",
      "content": "Summarize this document."
    }
  ],
  "temperature": 0.2
}
```

반드시 설명:

- Chat Completion은 messages 배열을 기반으로 응답 생성
- Response에는 생성된 content와 usage 정보가 포함될 수 있음
- Finish Reason으로 출력 종료 원인을 확인 가능
- API Provider마다 필드명과 응답 구조가 다를 수 있음

주의:

- Provider별 API 차이를 일반화하지 말 것
- Usage 정보가 항상 제공된다고 가정하지 말 것
- 응답 Content가 비어 있을 수 있음
- Finish Reason이 length이면 출력이 잘렸을 수 있음

---

# 9. Model Selection Rules

Model Selection 문서는 작업 목적 기준으로 작성한다.

필수 포함:

- General Chat Model
- Code Model
- Reasoning Model
- Vision Model
- Embedding Model
- Local LLM
- API LLM
- Latency
- Cost
- Context Window
- Tool Support

비교 기준:

| 기준           | 설명                                |
| -------------- | ----------------------------------- |
| 작업 유형      | 일반 답변, 코드, 추론, 요약, Vision |
| Context Window | 긴 문서 처리 가능 여부              |
| Latency        | 응답 속도                           |
| Cost           | API 비용 또는 로컬 자원             |
| Tool Support   | Function / Tool Calling 지원 여부   |
| Accuracy       | 작업 품질                           |

반드시 설명:

- 모든 작업에 하나의 모델만 쓰는 것이 최선은 아님
- 코드 생성은 Code Model 또는 강한 Reasoning Model이 유리
- 문서 검색은 Embedding Model이 필요
- 이미지 입력은 Vision Model 필요
- 로컬 LLM은 비용과 프라이버시에 장점이 있으나 성능과 속도 제한 가능

주의:

- 최신 모델명에 과도하게 의존하지 말 것
- Provider별 모델 기능 차이 확인
- 작업 목적과 비용을 함께 고려
- Local Model은 하드웨어 제약 고려

---

# 10. Parameter Rules

LLM Parameter 문서는 출력 제어 중심으로 작성한다.

필수 포함:

- Temperature
- Top-p
- Max Tokens
- Stop Sequence
- Frequency Penalty
- Presence Penalty
- Seed
- Determinism

기본 설명:

| Parameter     | 의미                 | 사용 기준             |
| ------------- | -------------------- | --------------------- |
| Temperature   | 무작위성 조절        | 낮을수록 일관적       |
| Top-p         | 후보 Token 범위 조절 | 확률 질량 기준 샘플링 |
| Max Tokens    | 출력 길이 제한       | 비용/길이 제어        |
| Stop Sequence | 출력 중단 조건       | 형식 제어             |
| Seed          | 재현성 보조          | 지원 시 사용          |

반드시 설명:

- 정확성과 일관성이 중요하면 Temperature를 낮게 설정
- 창의적 생성은 Temperature를 높일 수 있음
- Max Tokens는 출력 잘림과 비용에 영향
- Parameter는 모델/Provider마다 지원 범위가 다를 수 있음

주의:

- Temperature 0이어도 완전한 결정론을 보장하지 않을 수 있음
- Top-p와 Temperature를 동시에 크게 조정하면 예측 어려움
- Max Tokens가 너무 작으면 답변이 잘림
- Stop Sequence가 잘못되면 필요한 내용도 잘릴 수 있음

---

# 11. Temperature Rules

Temperature는 출력 다양성을 조절한다.

필수 포함:

- Low Temperature
- High Temperature
- Deterministic Output
- Creative Output
- Code Generation
- Review Task
- Brainstorming

추천 기준:

| 작업          | 추천 방향 |
| ------------- | --------- |
| 코드 생성     | 낮게      |
| 코드 리뷰     | 낮게      |
| RAG 답변      | 낮게      |
| 요약          | 낮게~중간 |
| 아이디어 발산 | 중간~높게 |
| 창작          | 높게      |

반드시 설명:

- 낮은 Temperature는 일관성과 안정성에 유리
- 높은 Temperature는 다양성과 창의성에 유리
- 개발 Agent / Review Agent는 낮은 Temperature 선호
- PM Agent의 기획 브레인스토밍은 중간값도 가능

주의:

- 높은 Temperature는 Hallucination 가능성 증가
- 낮은 Temperature가 항상 정확성을 보장하지는 않음
- RAG 기반 사실 답변은 낮게 유지 권장

---

# 12. Structured Output Rules

Structured Output은 Agent Workflow에서 매우 중요하다.

필수 포함:

- JSON Output
- Markdown Output
- Schema
- Required Field
- Validation
- Parsing
- Error Field

기본 Flow:

```text
Prompt
→ Model Response
→ Parse Structured Output
→ Validate Schema
→ Use in Next Step
```

JSON 예시:

```json
{
  "status": "success",
  "summary": "Task completed",
  "items": []
}
```

반드시 설명:

- 구조화 출력은 후속 Agent / Tool 처리에 유리
- JSON 출력은 자동 파싱 가능해야 함
- Markdown은 사람에게 보여줄 최종 응답에 적합
- Schema를 명확히 지정하면 출력 안정성이 올라감

주의:

- JSON 출력에 설명 문장이 섞이면 파싱 실패
- Schema가 너무 복잡하면 실패 가능성 증가
- 출력 검증 로직 필요
- 모델 출력은 신뢰하지 말고 파싱/검증 필요

---

# 13. JSON Mode / JSON Schema Rules

JSON Output 문서는 유효성 검증 중심으로 작성한다.

필수 포함:

- JSON Mode
- JSON Schema
- Required Fields
- Enum
- Array
- Object
- Validation Error
- Retry on Invalid Output

예시 Schema:

```json
{
  "type": "object",
  "properties": {
    "answer": {
      "type": "string"
    },
    "confidence": {
      "type": "number"
    }
  },
  "required": ["answer"]
}
```

반드시 설명:

- JSON Mode는 유효한 JSON 출력을 유도
- JSON Schema는 필드 구조를 제한
- Schema 검증 실패 시 재시도 전략 가능
- Provider마다 JSON Mode / Structured Output 지원 방식이 다름

주의:

- JSON Mode가 내용 정확성을 보장하지 않음
- Schema가 너무 복잡하면 응답 실패 가능
- 숫자/문자 타입 불일치 주의
- Optional Field 처리 기준 필요

---

# 14. Streaming Rules

Streaming은 긴 응답의 체감 속도를 개선한다.

필수 포함:

- Streaming Response
- Token Stream
- Chunk
- Server-Sent Events
- Partial Output
- Accumulation
- Cancellation

기본 Flow:

```text
Client Request
→ LLM Starts Generation
→ Receive Token Chunks
→ Append Output
→ Complete Response
```

반드시 설명:

- Streaming은 응답 전체를 기다리지 않고 부분 결과를 받는 방식
- 사용자 체감 속도 개선에 유리
- 긴 답변 / 채팅 UI에 적합
- 최종 결과 조립 로직 필요

주의:

- Streaming 중간 결과는 불완전함
- JSON 출력과 Streaming은 파싱이 까다로울 수 있음
- 중간 취소 / 오류 처리 필요
- 로그 저장 시 최종 조립본 기준 고려

---

# 15. Function Calling / Tool Calling Rules

Function Calling / Tool Calling은 LLM이 외부 도구를 선택하고 호출하도록 만드는 구조이다.

필수 포함:

- Tool Definition
- Function Schema
- Arguments
- Tool Choice
- Tool Result
- Tool Message
- Validation
- Error Handling

기본 Flow:

```text
User Request
→ LLM Chooses Tool
→ Tool Arguments
→ Execute Tool
→ Return Tool Result
→ LLM Final Response
```

예시 Tool Schema:

```json
{
  "name": "search_documents",
  "description": "Search RAG documents",
  "parameters": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string"
      }
    },
    "required": ["query"]
  }
}
```

반드시 설명:

- Tool Calling은 모델이 직접 작업하지 않고 외부 함수를 호출하게 함
- Tool Arguments는 검증해야 함
- Tool Result는 다시 모델 Context로 전달 가능
- Agent Workflow의 핵심 기능

주의:

- Tool 호출 인자를 그대로 신뢰하지 말 것
- 파일 삭제 / 결제 / 배포 같은 위험 작업은 승인 절차 필요
- Tool Result가 실패했을 때 재시도 또는 사용자 확인 필요
- Tool이 너무 많으면 선택 품질 저하 가능

---

# 16. Embedding API Rules

Embedding API는 문서 검색과 RAG에 사용된다.

필수 포함:

- Embedding
- Vector
- Semantic Similarity
- Query Embedding
- Document Embedding
- Chunk Embedding
- Vector Database
- RAG

기본 Flow:

```text
Document Chunk
→ Embedding Model
→ Vector
→ Vector DB
→ Query Embedding
→ Similarity Search
→ Retrieved Context
```

반드시 설명:

- Embedding은 텍스트 의미를 Vector로 변환
- RAG는 Query와 문서 Chunk의 Semantic Similarity를 이용
- Embedding Model은 Chat Model과 역할이 다름
- 문서 Chunk 품질이 검색 품질에 큰 영향

주의:

- Embedding Model과 Vector Dimension 불일치 주의
- 문서 변경 시 Embedding 재생성 필요
- 너무 긴 Chunk는 검색 품질 저하 가능
- Embedding은 답변 생성이 아니라 검색용

---

# 17. API Key / Secret Rules

LLM API 문서는 API Key 보안 기준을 반드시 포함한다.

필수 포함:

- API Key
- Secret
- Environment Variable
- `.env`
- Secret Rotation
- `.gitignore`
- Least Privilege
- Usage Limit

예시:

```python
import os

api_key = os.environ.get("LLM_API_KEY")
if not api_key:
    raise ValueError("LLM_API_KEY is required")
```

반드시 설명:

- API Key는 코드에 하드코딩하지 않음
- `.env` 파일은 Git에 올리지 않음
- 운영 환경에서는 Secret Manager 사용 가능
- API Key 노출 시 즉시 폐기/재발급 필요
- 비용 폭주 방지를 위해 사용량 제한 고려

주의:

- API Key 로그 출력 금지
- GitHub에 Secret 커밋 금지
- Frontend 코드에 Secret 포함 금지
- 공유 문서에 Key 붙여넣기 금지

---

# 18. HTTP Client Integration Rules

API Integration 문서는 HTTP Client 사용 기준을 포함한다.

필수 포함:

- requests
- httpx
- fetch
- axios
- Spring WebClient
- Timeout
- Header
- JSON Body
- Status Code
- Response Parsing

Python 예시:

```python
import requests

response = requests.post(
    "https://api.example.com/v1/chat",
    headers={"Authorization": f"Bearer {api_key}"},
    json={"messages": messages},
    timeout=30
)

response.raise_for_status()
data = response.json()
```

반드시 설명:

- LLM API는 일반적으로 HTTP 기반으로 호출
- Authorization Header에 API Key 사용
- Timeout 설정 필수
- Status Code와 Error Body를 확인
- Response 구조는 Provider별로 다름

주의:

- Timeout 없는 HTTP 요청 금지
- 응답 구조를 고정 가정하지 말 것
- 네트워크 오류 / Rate Limit / 인증 오류 처리 필요
- Secret을 Request Log에 남기지 말 것

---

# 19. Timeout Rules

Timeout은 API 안정성에 필수이다.

필수 포함:

- Connection Timeout
- Read Timeout
- Total Timeout
- Streaming Timeout
- Retry Timeout

기본 Flow:

```text
API Request
→ Wait Until Timeout
→ Fail Fast
→ Retry or Error Response
```

반드시 설명:

- Timeout이 없으면 요청이 무기한 대기할 수 있음
- LLM 응답은 길 수 있으므로 작업 유형별 Timeout 설정 필요
- Streaming은 일반 요청과 Timeout 기준이 다를 수 있음
- Timeout 발생 시 사용자에게 명확한 실패 응답 필요

주의:

- Timeout을 너무 짧게 잡으면 정상 응답도 실패
- 너무 길게 잡으면 Thread / Connection 점유 증가
- Retry와 Timeout을 함께 고려
- 장기 작업은 비동기 처리 검토

---

# 20. Retry Rules

Retry는 일시적 오류 대응에 사용한다.

필수 포함:

- Retryable Error
- Non-Retryable Error
- Exponential Backoff
- Jitter
- Max Retry
- Idempotency
- Rate Limit Retry

Retry 가능 예:

- 일시적 네트워크 오류
- 429 Rate Limit
- 500 / 502 / 503 / 504
- Timeout 일부

Retry 금지 예:

- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 잘못된 Tool Arguments
- 잘못된 Prompt Schema

반드시 설명:

- Retry는 실패를 줄이지만 비용과 부하를 증가시킬 수 있음
- Exponential Backoff와 Max Retry 필요
- 429는 Retry-After Header 확인 가능
- Idempotency 없는 작업은 재시도 주의

주의:

- 무제한 Retry 금지
- 인증 오류를 Retry로 해결하려 하지 말 것
- 같은 잘못된 요청을 반복하지 말 것
- Retry 비용을 기록/관측

---

# 21. Rate Limit Rules

Rate Limit 문서는 API 사용 제한 대응 중심으로 작성한다.

필수 포함:

- Request Limit
- Token Limit
- 429 Error
- Retry-After
- Backoff
- Queue
- Throttling
- Usage Monitoring

기본 Flow:

```text
API Call
→ Rate Limit Exceeded
→ 429 Response
→ Wait / Backoff
→ Retry or Fail
```

반드시 설명:

- Provider는 요청 수 또는 Token 기준으로 제한 가능
- Rate Limit 초과 시 429 응답 발생 가능
- 병렬 호출은 Rate Limit을 빠르게 소모
- 작업 Queue / Throttling 전략 필요

주의:

- 대량 문서 처리 시 Rate Limit 고려
- Retry가 Rate Limit을 악화시킬 수 있음
- 사용자에게 지연 가능성을 알려야 할 수 있음
- 사용량 모니터링 필요

---

# 22. Error Handling Rules

LLM API Error Handling은 안정적 통합에 필수이다.

필수 포함:

- Authentication Error
- Authorization Error
- Rate Limit Error
- Timeout Error
- Validation Error
- Server Error
- Network Error
- Invalid JSON Output
- Empty Response
- Content Filter / Safety Error

기본 Flow:

```text
Call LLM API
→ Check HTTP Status
→ Parse Response
→ Validate Output
→ Handle Error
→ Return Safe Result
```

반드시 설명:

- API 오류는 사용자 친화적 메시지로 변환
- 로그에는 원인 분석 정보 포함
- Secret / Prompt 민감정보는 로그에서 제외
- Invalid Output은 재요청 또는 안전 실패 처리

주의:

- 모든 오류를 같은 메시지로 처리 금지
- 401 / 403은 인증 설정 확인 필요
- 429는 Backoff 필요
- 빈 응답 / 잘린 응답 처리 필요

---

# 23. Response Validation Rules

LLM 응답은 검증해야 한다.

필수 포함:

- Empty Response Check
- Finish Reason Check
- JSON Parse
- Schema Validation
- Required Field Check
- Content Safety
- Citation / Evidence Check
- Hallucination Check

기본 Flow:

```text
LLM Response
→ Empty Check
→ Finish Reason Check
→ Parse
→ Validate Schema
→ Validate Content
→ Use Result
```

반드시 설명:

- LLM Output은 항상 신뢰하면 안 됨
- JSON Output은 파싱/스키마 검증 필요
- RAG 답변은 근거 문서와 일치하는지 확인
- finish_reason이 length이면 출력이 잘렸을 수 있음

주의:

- 유효한 JSON이어도 내용이 맞다는 보장은 없음
- 모델이 Required Field를 누락할 수 있음
- 검증 실패 시 재시도 또는 사용자 확인 필요

---

# 24. Cost Management Rules

LLM API 비용 관리는 실무에서 중요하다.

필수 포함:

- Input Token Cost
- Output Token Cost
- Model Pricing
- Token Budget
- Caching
- Prompt Compression
- Context Filtering
- Usage Logging

비용 절감 방법:

```text
Reduce Irrelevant Context
→ Limit Output Tokens
→ Use Smaller Model When Possible
→ Cache Repeated Results
→ Batch Carefully
```

반드시 설명:

- 비용은 보통 입력/출력 Token에 따라 증가
- 큰 모델은 품질이 좋을 수 있지만 비용과 Latency 증가
- RAG Context가 길면 비용 증가
- 반복 질의는 Cache 고려 가능

주의:

- 비용 절감만으로 품질을 과도하게 희생하지 말 것
- Cache된 답변의 최신성 문제 확인
- 대량 문서 처리 전 예상 비용 계산
- 사용량 모니터링 필요

---

# 25. Latency Management Rules

LLM API Latency는 사용자 경험에 큰 영향을 준다.

필수 포함:

- Model Latency
- Network Latency
- Token Generation Time
- Streaming
- Context Length
- Output Length
- Parallel Request
- Queue

기본 Flow:

```text
Request Build
→ API Call
→ Model Inference
→ Token Generation
→ Response Transfer
```

반드시 설명:

- 긴 Prompt와 긴 Output은 Latency 증가
- 큰 모델은 느릴 수 있음
- Streaming은 체감 Latency 개선
- 병렬 호출은 Rate Limit과 비용을 증가시킬 수 있음

주의:

- Latency 개선을 위해 Context를 무리하게 줄이면 정확도 저하
- 병렬화는 Rate Limit 고려
- 느린 응답에는 Timeout과 사용자 안내 필요

---

# 26. RAG Integration Rules

LLM API Integration 문서는 RAG 연결 기준을 포함한다.

필수 포함:

- Query
- Retrieval
- Retrieved Context
- Prompt Assembly
- Grounded Answer
- Citation / Reference
- Missing Information
- Context Limit

기본 Flow:

```text
User Query
→ Query Rewrite
→ Retrieve Documents
→ Select Context
→ Build Prompt
→ Call LLM
→ Validate Answer
```

반드시 설명:

- RAG는 LLM이 외부 문서를 참고하게 만드는 구조
- Retrieved Context는 Prompt에 주입
- 문서에 없는 내용은 없다고 답하게 해야 함
- Retrieval 품질과 Prompt 조립이 답변 품질에 영향

주의:

- 검색 결과를 너무 많이 넣지 말 것
- 관련 없는 Chunk는 오답을 유발
- RAG 답변은 문서 근거와 일반 추론을 구분
- Context 누락 시 추가 검색 또는 사용자 확인 필요

---

# 27. Agent Integration Rules

LLM API는 Agent Workflow의 핵심 실행 엔진으로 설명한다.

필수 포함:

- Agent Role
- Prompt Template
- Tool Calling
- Memory / State
- Intermediate Result
- Review Loop
- Final Response
- Error Recovery

기본 Flow:

```text
Agent State
→ Build Prompt
→ Call LLM
→ Parse Response
→ Tool Call if Needed
→ Update State
→ Next Agent or Final
```

반드시 설명:

- Agent는 LLM API 호출을 반복적으로 사용
- 각 Agent별 System Prompt와 Output Schema가 필요
- Tool Calling 결과를 다시 Context에 넣을 수 있음
- Review Agent는 LLM Output을 검증하는 역할 가능

주의:

- Agent Loop 무한 반복 방지
- Intermediate Result 누락 주의
- Agent 간 출력 Schema 통일
- 실패 시 fallback / retry / human confirmation 필요

---

# 28. Local LLM Integration Rules

Local LLM 문서는 로컬 모델 사용 기준을 포함한다.

필수 포함:

- Ollama
- Local API
- Model Loading
- VRAM / RAM
- Quantization
- Latency
- Privacy
- Offline Usage
- Hardware Constraint

기본 Flow:

```text
Local Client
→ Local LLM Server
→ Model Inference
→ Response
```

반드시 설명:

- Local LLM은 비용 절감과 프라이버시에 장점
- 모델 크기와 하드웨어에 따라 속도 차이 큼
- API LLM보다 품질이 낮을 수 있음
- 로컬 Embedding Model과 Chat Model 역할 구분

주의:

- 모델이 메모리에 상주하면 RAM / VRAM 사용
- 동시 요청 처리 한계 고려
- 큰 Context는 성능 저하 가능
- 로컬 모델도 Hallucination 가능

---

# 29. Logging Rules

LLM API Logging은 디버깅과 비용 관리에 필요하다.

필수 포함:

- Request ID
- Model Name
- Token Usage
- Latency
- Error Code
- Retry Count
- User Request Metadata
- Redaction

로그 권장 항목:

```text
requestId
model
inputTokens
outputTokens
latencyMs
status
errorCode
retryCount
```

반드시 설명:

- LLM API 호출 로그는 장애 분석과 비용 추적에 유용
- Prompt 전문을 저장할지 여부는 보안/프라이버시 기준 필요
- API Key와 민감정보는 로그에서 제거
- Error Response는 원인 분석에 필요한 범위로 기록

주의:

- 사용자 개인정보 / Secret / API Key 로그 금지
- Prompt 전체 로그 저장은 보안 정책 필요
- 응답 내용에 민감정보가 있을 수 있음
- 로그 저장 비용 고려

---

# 30. Testing Rules

LLM API Integration 문서에는 테스트 기준을 포함한다.

필수 포함:

- Unit Test
- Mock API
- Integration Test
- Contract Test
- Schema Validation Test
- Retry Test
- Timeout Test
- Rate Limit Test

테스트 대상:

```text
Prompt Builder
Response Parser
Schema Validator
Retry Handler
Error Mapper
Tool Call Handler
```

반드시 설명:

- 실제 LLM API 호출 없이 테스트 가능한 부분을 분리
- Prompt Builder와 Response Parser는 Unit Test 가능
- API 호출은 Mocking 권장
- JSON Schema 검증 테스트 필요
- 비용이 발생하는 테스트는 제한적으로 수행

주의:

- 테스트마다 실제 API 호출 금지
- 모델 출력은 비결정적일 수 있으므로 테스트 기준 설계 필요
- Secret이 테스트 로그에 남지 않도록 주의

---

# 31. Troubleshooting Rules

반드시 포함 추천.

형식:

```md
문제:

원인:

해결:
```

---

## 401 Unauthorized

문제:

- LLM API 인증 실패

원인:

- API Key 누락
- 잘못된 API Key
- 환경변수 미설정
- 만료 또는 폐기된 Key

해결:

- 환경변수 확인
- API Key 재발급
- Authorization Header 확인
- Secret 로그 출력 여부 점검

---

## 429 Rate Limit

문제:

- API 요청 제한 초과

원인:

- 너무 많은 요청
- 너무 많은 Token 사용
- 병렬 호출 과다
- Retry 폭증

해결:

- Exponential Backoff 적용
- Retry-After 확인
- 요청 Queue 도입
- Token 사용량 감소
- 병렬 요청 제한

---

## Timeout

문제:

- LLM API 응답 대기 중 Timeout 발생

원인:

- 모델 응답 지연
- Prompt가 너무 김
- 출력이 너무 김
- 네트워크 문제

해결:

- Timeout 조정
- Context 축소
- Max Tokens 제한
- Streaming 적용 검토
- 재시도 정책 적용

---

## Invalid JSON Output

문제:

- JSON 파싱 실패

원인:

- 모델이 설명 문장을 섞음
- Schema가 복잡함
- 출력이 중간에 잘림
- JSON Mode 미사용

해결:

- JSON Schema 단순화
- Valid JSON only 제약 추가
- finish_reason 확인
- 재요청 / 복구 파서 고려

---

## Hallucinated Answer

문제:

- 문서에 없는 내용을 답변함

원인:

- RAG Grounding 규칙 부족
- Retrieved Context 부족
- Prompt가 일반 지식을 허용
- 검증 단계 없음

해결:

- 문서 근거 우선 규칙 추가
- Missing Information Rule 추가
- Retrieved Context 개선
- Answer Validation 추가

---

## High Cost

문제:

- LLM API 비용이 예상보다 높음

원인:

- 긴 Prompt
- 긴 RAG Context
- 긴 Output
- 비싼 Model 사용
- 반복 호출

해결:

- Token Usage 기록
- Context Filtering
- Max Tokens 제한
- 작은 Model 사용 검토
- Cache 적용 검토

---

# 32. Best Practice Rules

Best Practice:

- API Key는 환경변수로 관리
- Timeout을 반드시 설정
- Retry는 제한적으로 적용
- Rate Limit 대응 설계
- Prompt와 Context를 분리
- Token Budget을 관리
- RAG Context는 관련 Chunk만 넣기
- Temperature는 작업 목적에 맞게 설정
- JSON Output은 Schema 검증
- Tool Arguments는 검증 후 실행
- LLM 응답은 항상 검증
- Usage / Latency / Error 로그 기록
- 실제 API 호출 테스트는 제한
- Provider별 차이를 문서화

---

# 33. Comparison Rules

LLM API 문서는 비교 기준을 포함한다.

필수 비교 대상:

- Chat Completion vs Text Completion
- Chat Model vs Embedding Model
- Local LLM vs API LLM
- Low Temperature vs High Temperature
- JSON Output vs Markdown Output
- Streaming vs Non-Streaming
- Retry vs No Retry
- RAG Answer vs General Answer
- Function Calling vs Plain Text Response

예시:

| 비교   | Chat Model                   | Embedding Model         |
| ------ | ---------------------------- | ----------------------- |
| 목적   | 답변 생성                    | 의미 벡터 생성          |
| 입력   | Message / Prompt             | Text                    |
| 출력   | Text / JSON                  | Vector                  |
| 사용처 | Chat, Agent, Code Generation | Search, RAG, Similarity |

---

# 34. Checklist Rules

LLM API Integration 문서에는 Checklist를 포함할 수 있다.

예시:

```md
### [Checklist]

- [ ] API Key를 환경변수로 관리하는가?
- [ ] Timeout이 설정되어 있는가?
- [ ] Retry 정책이 제한적인가?
- [ ] Rate Limit 대응이 있는가?
- [ ] Token 사용량을 기록하는가?
- [ ] Temperature 설정 기준이 있는가?
- [ ] Response Schema를 검증하는가?
- [ ] JSON Output 파싱 실패 처리가 있는가?
- [ ] RAG Context가 과도하지 않은가?
- [ ] Tool Calling 인자를 검증하는가?
- [ ] Secret이 로그에 남지 않는가?
```

---

# 35. Retrieval Optimization Rules

강조 대상 키워드:

- LLM
- LLM Core
- LLM API Integration
- Chat Completion
- Text Generation
- Token
- Context Window
- System Message
- User Message
- Assistant Message
- Tool Message
- Temperature
- Top-p
- Max Tokens
- Stop Sequence
- Structured Output
- JSON Mode
- JSON Schema
- Streaming
- Function Calling
- Tool Calling
- Embedding API
- API Key
- Environment Variable
- Timeout
- Retry
- Rate Limit
- Error Handling
- Response Validation
- Cost Management
- Latency Management
- RAG Integration
- Agent Integration
- Local LLM
- Ollama

키워드 반복 허용.

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

예:

- LLM API는 어떻게 호출해?
- Token이 뭐야?
- Context Window가 뭐야?
- Temperature는 어떻게 설정해?
- System Message와 User Message 차이는?
- JSON Output은 어떻게 받아?
- Streaming은 언제 써?
- Tool Calling은 뭐야?
- Embedding API는 뭐에 써?
- Rate Limit은 어떻게 처리해?
- LLM API 비용은 어떻게 줄여?
- RAG와 LLM API는 어떻게 연결해?
- 로컬 LLM과 API LLM 차이는?

---

# 36. Version Rules

기준:

- Modern LLM API
- Chat Completion 기반 구조
- Structured Output / JSON Schema 지원 모델 기준
- Tool Calling / Function Calling 가능 구조
- Embedding API 기반 RAG
- Local LLM API 연동 가능 구조
- Python 3.11+
- Java 21 / Spring Boot 3.x 연동 가능성 고려
- Ollama / OpenAI-compatible API 구조 고려

Legacy 제외:

- 단순 Text Completion만 중심으로 설명
- API Key 하드코딩 예제
- Timeout 없는 API 호출 예제
- 응답 검증 없는 LLM 사용 방식
- Token / Context Window를 고려하지 않는 방식

---

# 37. Common Mistakes

자주 발생:

- API Key를 코드에 하드코딩
- Timeout 없이 API 호출
- Rate Limit 대응 없음
- Token 사용량 기록 없음
- Context Window를 초과하는 Prompt 작성
- RAG Context를 너무 많이 넣음
- Temperature를 작업 목적과 무관하게 설정
- JSON Output을 검증하지 않음
- Tool Arguments를 검증하지 않고 실행
- LLM 응답을 사실로 바로 사용
- Streaming 중간 결과를 완성 결과처럼 처리
- Provider별 응답 구조 차이를 무시
- 비용 계산 없이 대량 호출
- Error Handling 없이 성공 응답만 가정

---

# 38. Final Goal

LLM Core & API Integration RAG 문서는 Agent가 아래를 수행 가능해야 한다.

- LLM 기본 개념 설명
- Token / Context Window 관리
- Chat Completion 구조 이해
- System / User / Assistant Message 설계
- LLM API 호출 코드 작성
- Parameter 설정 기준 제안
- Structured Output / JSON Output 처리
- Streaming 처리 기준 제안
- Function Calling / Tool Calling 기초 설계
- Embedding API와 Chat API 역할 구분
- RAG와 LLM API 연결
- Agent Workflow와 LLM API 연결
- Timeout / Retry / Rate Limit 처리
- API 비용 / Latency 관리
- LLM API 오류 Troubleshooting
- LLM Integration Code Review

문서 품질이 AI Agent와 RAG 시스템의 안정성을 결정한다.

---

# Retrieval Queries

### [FAQ]

Q. LLM이 뭐야?

A.
LLM은 대량의 텍스트를 학습해 Prompt를 입력받고 다음 Token을 생성하는 언어 모델이다.

Q. LLM API는 왜 사용해?

A.
직접 모델을 운영하지 않고도 Chat, 요약, 코드 생성, 분석, Agent 응답 생성을 사용할 수 있기 때문이다.

Q. Token이 뭐야?

A.
LLM이 텍스트를 처리하는 단위다. 입력과 출력 모두 Token으로 계산되며 비용과 Context Limit에 영향을 준다.

Q. Context Window가 뭐야?

A.
모델이 한 번에 참고할 수 있는 입력과 출력의 최대 Token 범위다.

Q. System Message와 User Message 차이는?

A.
System Message는 모델의 상위 행동 규칙이고, User Message는 현재 사용자의 작업 요청이다.

Q. Assistant Message는 왜 포함해?

A.
이전 모델 응답을 대화 문맥으로 유지하기 위해 포함한다. 단, Token을 소비한다.

Q. Temperature는 어떻게 설정해?

A.
코드 생성, RAG, 리뷰처럼 정확성과 일관성이 중요한 작업은 낮게 설정하고, 창의적 아이디어 생성은 높일 수 있다.

Q. Max Tokens는 왜 설정해?

A.
출력 길이와 비용을 제어하고, 너무 긴 응답을 방지하기 위해 설정한다.

Q. JSON Output은 어떻게 받아?

A.
JSON Schema 또는 명확한 출력 형식을 지정하고, 응답을 파싱한 뒤 Schema 검증을 수행한다.

Q. Streaming은 언제 써?

A.
긴 답변이나 채팅 UI처럼 사용자가 빠른 반응을 체감해야 할 때 사용한다.

Q. Function Calling과 Tool Calling은 뭐야?

A.
LLM이 외부 함수나 도구를 선택해 인자를 생성하고, 실행 결과를 다시 답변에 활용하는 구조다.

Q. Tool Calling에서 가장 중요한 건 뭐야?

A.
Tool Arguments를 검증하고, 위험 작업에는 승인 절차나 안전장치를 두는 것이다.

Q. Embedding API는 뭐에 써?

A.
문서나 Query를 Vector로 변환해 Semantic Search와 RAG 검색에 사용한다.

Q. Chat Model과 Embedding Model 차이는?

A.
Chat Model은 답변을 생성하고, Embedding Model은 검색을 위한 Vector를 생성한다.

Q. LLM API 호출 시 Timeout은 꼭 필요해?

A.
필요하다. Timeout이 없으면 요청이 무기한 대기해 Thread나 Connection을 점유할 수 있다.

Q. 429 Rate Limit은 어떻게 처리해?

A.
Exponential Backoff, Retry-After 확인, 요청 Queue, Token 사용량 감소로 대응한다.

Q. LLM API 비용은 어떻게 줄여?

A.
관련 없는 Context를 줄이고, Max Tokens를 제한하며, 작은 모델이나 Cache를 사용할 수 있다.

Q. LLM API 응답은 그대로 믿어도 돼?

A.
안 된다. JSON Schema, 근거 문서, 필수 필드, finish_reason 등을 검증해야 한다.

Q. RAG와 LLM API는 어떻게 연결해?

A.
사용자 Query로 문서를 검색하고, 검색된 Context를 Prompt에 넣어 LLM API에 전달한다.

Q. Local LLM과 API LLM 차이는?

A.
Local LLM은 비용과 프라이버시에 장점이 있지만 하드웨어 제약이 있고, API LLM은 품질과 편의성이 좋지만 비용과 외부 의존성이 있다.
