# LLM Core & API Integration Part03 - Token & Context Management

---

# 1. Token Management

## 1.1 Token

### [개념]

Token은 LLM이 텍스트를 처리하는 기본 단위이다.

LLM은 문장 전체를 그대로 이해하는 것이 아니라 입력 텍스트를 Token으로 분리하고, Token 단위로 다음 출력을 생성한다.

Token은 비용, 속도, Context Window, 출력 길이, API 제한에 직접 영향을 준다.

Token 종류:

- Input Token
- Output Token
- Total Token
- Prompt Token
- Completion Token
- Retrieved Context Token
- Conversation History Token

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

- LLM은 텍스트를 Token 단위로 처리한다.
- Input Token은 모델에 전달되는 입력 전체이다.
- Output Token은 모델이 생성하는 응답이다.
- Total Token은 Input Token과 Output Token의 합이다.
- Token 수가 많을수록 비용과 Latency가 증가한다.
- Context Window를 초과하면 요청 실패 또는 정보 누락이 발생한다.
- RAG에서는 Retrieved Context가 Token 사용량의 큰 비중을 차지한다.
- Agent Workflow에서는 Agent State와 Intermediate Result도 Token을 소비한다.

---

### [실무]

2026 실무 기준 LLM API 연동에서는 Token Budget을 명시적으로 관리한다.

Token Budget 구성:

```text
Context Window
→ System Instruction
→ Conversation Summary
→ Retrieved Context
→ Current User Task
→ Output Reserve
→ Safety Margin
```

권장 설계:

| 항목                 | 설명                             |
| -------------------- | -------------------------------- |
| System Instruction   | 고정 규칙, 짧고 명확하게 유지    |
| Conversation Summary | 긴 대화 원문 대신 요약 사용      |
| Retrieved Context    | 관련 Chunk만 선별                |
| User Task            | 현재 요청 중심으로 작성          |
| Output Reserve       | 모델 응답 생성을 위한 여유 Token |
| Safety Margin        | 예상 초과 방지 여유 공간         |

Token 관리 예:

```text
전체 Context Window: 32000 tokens
System Instruction: 1000 tokens
Conversation Summary: 2000 tokens
Retrieved Context: 12000 tokens
Current User Task: 1000 tokens
Output Reserve: 4000 tokens
Safety Margin: 12000 tokens
```

실무 처리 기준:

- 긴 문서는 Chunking 후 Retrieval로 처리한다.
- Conversation History는 전체 원문을 계속 넣지 않는다.
- Retrieved Context는 Top-K와 Reranking으로 제한한다.
- Max Tokens로 출력 길이를 제한한다.
- Token Usage를 로그로 기록한다.
- Token Limit 초과 시 사용자 친화적 오류로 변환한다.
- RAG 답변은 관련 Chunk 중심으로 구성한다.
- Agent 간 전달 데이터는 Summary 또는 Structured Output으로 압축한다.

---

### [FAQ]

Q. Token이 뭐야?

A. Token은 LLM이 텍스트를 읽고 생성할 때 사용하는 처리 단위다.

Q. Token이 왜 중요해?

A. Token은 비용, 응답 속도, Context Window, 출력 길이에 직접 영향을 주기 때문이다.

Q. Input Token과 Output Token 차이는?

A. Input Token은 모델에 입력되는 내용이고, Output Token은 모델이 생성하는 응답이다.

Q. Total Token은 뭐야?

A. Input Token과 Output Token을 합친 전체 Token 사용량이다.

Q. RAG에서 Token을 많이 쓰는 부분은?

A. Retrieved Context가 많은 Token을 차지하는 경우가 많다.

Q. Agent 시스템에서 Token 관리는 왜 중요해?

A. Agent State, 이전 결과, Tool Result, RAG Context가 모두 Token을 소비하기 때문이다.

---

## 1.2 Token Cost

### [개념]

Token Cost는 LLM API 사용 비용을 Token 사용량 기준으로 계산하는 개념이다.

대부분의 LLM API는 Input Token과 Output Token 사용량에 따라 비용이 증가한다.

비용 증가 원인:

- 긴 System Prompt
- 긴 Conversation History
- 많은 Retrieved Context
- 긴 Output
- 반복 호출
- Agent Loop
- Retry
- 대량 문서 처리

---

### [핵심]

- Token Cost는 Input Token과 Output Token에 의해 결정된다.
- Output Token 비용이 Input Token보다 비싼 Provider도 있다.
- RAG Context가 길수록 비용이 증가한다.
- Agent Workflow는 여러 번 LLM을 호출하므로 비용이 누적된다.
- Retry가 많으면 동일 작업 비용이 증가한다.
- 비용 관리를 위해 Usage Logging이 필요하다.

---

### [실무]

비용 절감 Flow:

```text
Reduce Irrelevant Context
→ Limit Conversation History
→ Use Smaller Model When Possible
→ Limit Max Tokens
→ Cache Repeated Results
→ Track Usage
```

비용 관리 기준:

| 전략                 | 설명                         |
| -------------------- | ---------------------------- |
| Context Filtering    | 관련 없는 문서 제거          |
| Chunk Reranking      | 상위 관련 Chunk만 사용       |
| Prompt Compression   | 긴 지시문 압축               |
| Conversation Summary | 긴 대화 이력 요약            |
| Max Tokens Limit     | 출력 길이 제한               |
| Model Routing        | 작업 난이도에 따라 모델 분기 |
| Cache                | 반복 요청 결과 재사용        |
| Usage Logging        | Token 사용량 기록            |

Usage Logging 예:

```json
{
  "requestId": "req-001",
  "model": "model-name",
  "inputTokens": 1800,
  "outputTokens": 420,
  "totalTokens": 2220,
  "latencyMs": 1640,
  "status": "success"
}
```

주의:

- 비용 절감만을 위해 Context를 과도하게 줄이면 정확도가 낮아진다.
- Cache된 답변은 최신성 문제가 있을 수 있다.
- 대량 문서 처리 전 예상 Token Cost를 계산한다.
- Agent Loop에는 Max Step과 Stop Condition을 둔다.
- Retry는 Max Retry와 Backoff를 설정한다.

---

### [FAQ]

Q. Token Cost는 뭐야?

A. LLM API 사용량을 Token 기준으로 계산하는 비용 개념이다.

Q. LLM API 비용은 무엇 때문에 늘어나?

A. 긴 Prompt, 긴 RAG Context, 긴 Output, 반복 호출, Retry, Agent Loop 때문에 늘어난다.

Q. RAG 비용은 어떻게 줄여?

A. 관련 Chunk만 검색하고, Top-K를 제한하며, Conversation History를 요약한다.

Q. Agent 시스템은 왜 비용이 많이 들 수 있어?

A. 여러 Agent가 LLM API를 반복 호출하고 중간 결과를 계속 전달하기 때문이다.

Q. 비용 관리를 위해 반드시 기록할 것은?

A. Model Name, Input Token, Output Token, Total Token, Latency, Retry Count를 기록한다.

---

## 1.3 Token Latency

### [개념]

Token Latency는 LLM API가 Token을 처리하고 응답을 생성하는 데 걸리는 시간이다.

Latency는 사용자 경험, 시스템 처리량, Timeout, Streaming UX에 영향을 준다.

Latency 증가 원인:

- 긴 Prompt
- 긴 Retrieved Context
- 긴 Output
- 큰 모델 사용
- 느린 Local LLM
- 네트워크 지연
- 병렬 요청 증가
- Rate Limit 대기

---

### [핵심]

- Input Token이 많으면 요청 처리 시간이 증가한다.
- Output Token이 많으면 생성 시간이 증가한다.
- 큰 모델은 보통 더 느리다.
- Local LLM은 하드웨어 성능에 따라 속도 차이가 크다.
- Streaming은 체감 Latency를 줄일 수 있다.
- Timeout은 Token Latency를 고려해 설정해야 한다.

---

### [실무]

Latency 관리 Flow:

```text
Request Build
→ Context Length Check
→ Model Selection
→ API Call
→ Token Generation
→ Streaming or Full Response
→ Latency Logging
```

Latency 개선 기준:

| 방법              | 설명                         |
| ----------------- | ---------------------------- |
| Context Filtering | 불필요한 Token 제거          |
| Output Limit      | Max Tokens 제한              |
| Smaller Model     | 간단한 작업은 작은 모델 사용 |
| Streaming         | 긴 답변의 체감 속도 개선     |
| Cache             | 반복 요청 응답 재사용        |
| Queue             | Rate Limit과 병렬 요청 제어  |
| Timeout           | 무한 대기 방지               |
| Async Processing  | 긴 작업 분리                 |

실무 예:

```text
짧은 FAQ 답변
→ 작은 모델
→ 낮은 Max Tokens
→ Non-Streaming 가능

긴 코드 리뷰
→ 강한 모델
→ 관련 파일만 Context 포함
→ Streaming 또는 진행 상태 표시

RAG 문서 질의
→ Top-K 제한
→ Chunk Reranking
→ Max Tokens 제한
```

주의:

- Context를 무리하게 줄이면 답변 정확도가 낮아질 수 있다.
- Streaming은 최종 응답 검증이 끝나기 전까지 중간 출력이 불완전하다.
- 병렬 요청은 Rate Limit과 비용을 빠르게 소모한다.
- Local LLM은 RAM, VRAM, Quantization, Context Length에 따라 속도가 크게 달라진다.

---

### [FAQ]

Q. Token Latency는 뭐야?

A. LLM이 입력 Token을 처리하고 Output Token을 생성하는 데 걸리는 시간이다.

Q. Prompt가 길면 왜 느려져?

A. 모델이 처리해야 하는 Input Token 수가 많아지기 때문이다.

Q. Output이 길면 왜 느려져?

A. 모델이 Token을 순차적으로 생성하기 때문에 출력 길이가 늘수록 시간이 증가한다.

Q. Streaming은 Latency를 줄여?

A. 전체 처리 시간을 줄이기보다 사용자가 첫 응답을 더 빨리 보게 해 체감 Latency를 개선한다.

Q. Local LLM이 느린 이유는?

A. 모델 크기, Quantization, RAM, VRAM, CPU/GPU 성능, Context Length 영향을 받기 때문이다.

---

# 2. Context Window Management

## 2.1 Context Window

### [개념]

Context Window는 LLM이 한 번의 요청에서 참고할 수 있는 최대 Token 범위이다.

Context Window에는 입력 Token과 출력 Token이 함께 포함된다.

Context Window 구성 요소:

- System Instruction
- User Message
- Assistant Message
- Tool Message
- Conversation History
- Retrieved Context
- Output Reserve

기본 구조:

```text
System Instruction
→ Conversation Summary
→ Retrieved Documents
→ Current User Task
→ Output Reserve
```

---

### [핵심]

- Context Window는 LLM의 작업 공간이다.
- Context Window를 초과하면 요청 실패 또는 정보 누락이 발생한다.
- 큰 Context Window가 항상 높은 품질을 보장하지 않는다.
- 관련 없는 Context는 답변 품질을 낮춘다.
- RAG에서는 Top-K와 Chunk Size가 Context 사용량을 결정한다.
- Agent에서는 State와 Intermediate Result가 Context 사용량을 증가시킨다.

---

### [실무]

Context Window 설계 기준:

| 항목                 | 관리 기준                  |
| -------------------- | -------------------------- |
| System Instruction   | 핵심 규칙만 유지           |
| Conversation History | 요약 또는 최근 핵심만 유지 |
| Retrieved Context    | 관련 Chunk만 선별          |
| Tool Result          | 필요한 필드만 전달         |
| User Task            | 현재 요청 중심             |
| Output Reserve       | 응답 생성 여유 확보        |
| Safety Margin        | 예외 상황 대비             |

권장 Context 구성:

```text
System:
Agent Role + Global Rules

Memory:
Conversation Summary

Context:
Retrieved Documents

Task:
Current User Request

Output:
Required Format
```

Context 관리 실패 예:

```text
긴 대화 전체 삽입
+ 관련 없는 RAG 문서 다수 삽입
+ Tool Result 원문 전체 삽입
+ 긴 출력 요구
→ Context Window 초과
→ 응답 누락
→ 품질 저하
```

대응 방법:

- Conversation Summary
- Context Compression
- Retrieved Context Filtering
- Chunk Reranking
- Tool Result Field Selection
- Output Token Reserve
- Missing Information Rule

---

### [FAQ]

Q. Context Window가 뭐야?

A. LLM이 한 번에 참고할 수 있는 입력과 출력의 최대 Token 범위다.

Q. Context Window가 크면 무조건 좋아?

A. 아니다. 관련 없는 정보가 많으면 답변 품질이 낮아질 수 있다.

Q. Context Window에는 출력도 포함돼?

A. 그렇다. 입력 Token뿐 아니라 모델이 생성할 Output Token 여유도 필요하다.

Q. RAG에서 Context Window가 중요한 이유는?

A. 검색된 Chunk가 Context Window를 차지하므로 관련 문서만 넣어야 하기 때문이다.

Q. Agent에서 Context Window가 빨리 차는 이유는?

A. Agent State, 중간 결과, Tool Result, Conversation History가 계속 누적되기 때문이다.

---

## 2.2 Conversation History

### [개념]

Conversation History는 이전 User Message와 Assistant Message를 대화 문맥으로 유지하는 데이터이다.

Conversation History는 연속 대화에 필요하지만 Token을 지속적으로 소비한다.

포함 가능 정보:

- 이전 질문
- 이전 답변
- 사용자 선호
- 결정된 요구사항
- 이전 Agent 결과
- 작업 진행 상태

---

### [핵심]

- Conversation History는 문맥 유지에 도움이 된다.
- 긴 Conversation History는 Token 비용과 Latency를 증가시킨다.
- 오래된 오류가 반복 Context로 들어가면 오류가 누적된다.
- 전체 대화 원문보다 Summary가 효율적이다.
- 중요한 결정 사항은 Structured Memory로 분리하는 것이 좋다.
- 현재 작업과 무관한 History는 제거한다.

---

### [실무]

Conversation History 관리 Flow:

```text
New User Message
→ Load Recent Messages
→ Load Conversation Summary
→ Select Relevant History
→ Build Prompt
→ Generate Response
→ Update Summary
```

권장 전략:

| 전략             | 설명                                    |
| ---------------- | --------------------------------------- |
| Recent Window    | 최근 N개 대화만 유지                    |
| Summary Memory   | 긴 대화를 요약해 유지                   |
| Entity Memory    | 프로젝트명, 기술 스택 등 핵심 정보 저장 |
| Task State       | 진행 중 작업 상태만 유지                |
| Retrieval Memory | 과거 대화도 검색 대상으로 관리          |
| Expiration       | 오래된 단기 정보 제거                   |

Conversation Summary 예:

```text
User is creating RAG documents for LLM Core API Integration.
Output format must use writing block.
Current progress: Part01 and Part02 completed.
Next target: Token and Context Management.
```

주의:

- 전체 Conversation History를 계속 넣지 않는다.
- 잘못된 Assistant 응답은 요약에 포함하지 않는다.
- 민감정보를 장기 Memory에 저장하지 않는다.
- 현재 작업에 필요한 History와 개인화 Memory를 구분한다.
- Agent별로 필요한 History 범위를 다르게 설정한다.

---

### [FAQ]

Q. Conversation History는 뭐야?

A. 이전 대화 내용을 모델 Context에 포함해 문맥을 유지하는 데이터다.

Q. Conversation History를 전부 넣으면 안 돼?

A. Token 비용이 증가하고 오래된 오류나 관련 없는 정보가 답변 품질을 낮출 수 있다.

Q. 긴 대화는 어떻게 관리해?

A. 최근 대화 일부와 Conversation Summary를 함께 사용한다.

Q. Agent 시스템에서 History는 어떻게 관리해?

A. Agent State, Task Summary, 필요한 이전 결과만 선별해서 전달한다.

Q. 잘못된 이전 답변도 History에 넣어도 돼?

A. 권장하지 않는다. 오류가 다음 답변에 전파될 수 있다.

---

## 2.3 Retrieved Context

### [개념]

Retrieved Context는 RAG 시스템에서 사용자 Query와 관련된 문서 Chunk를 검색해 LLM Prompt에 포함한 정보이다.

Retrieved Context는 LLM이 외부 문서를 근거로 답변하도록 만드는 핵심 입력이다.

Retrieved Context 구성:

- Document Title
- Section Title
- Chunk Content
- Code Snippet
- Metadata
- Source Reference
- Retrieval Score

---

### [핵심]

- Retrieved Context는 RAG 답변의 근거이다.
- 관련 없는 Retrieved Context는 Hallucination을 유발할 수 있다.
- Top-K가 높다고 항상 좋은 답변이 나오지 않는다.
- Chunk Size가 너무 크면 검색 정밀도가 낮아질 수 있다.
- Chunk Size가 너무 작으면 필요한 맥락이 부족할 수 있다.
- Retrieved Context는 Prompt에서 User Question과 구분해야 한다.

---

### [실무]

RAG Context 구성 Flow:

```text
User Query
→ Query Rewrite
→ Embedding Search
→ Top-K Retrieval
→ Reranking
→ Context Filtering
→ Prompt Assembly
→ Grounded Answer
```

Retrieved Context Prompt 예:

```text
Retrieved Context:
[Document: LLM_Core_API_Integration_Part02]
Section: Chat Completion API
Content:
Chat Completion은 messages 배열을 기반으로 응답을 생성한다.

User Question:
Chat Completion에서 messages 필드는 뭐야?

Rule:
Answer only using Retrieved Context.
```

Retrieved Context 관리 기준:

| 항목              | 기준                      |
| ----------------- | ------------------------- |
| Top-K             | 과도하게 높이지 않음      |
| Chunk Size        | 독립 검색 가능한 크기     |
| Overlap           | 문맥 유지 목적            |
| Reranking         | 관련도 재정렬             |
| Source Metadata   | 출처 추적                 |
| Context Filtering | 중복/무관 Chunk 제거      |
| Missing Rule      | 문서에 없으면 없다고 답변 |

주의:

- Retrieved Context와 User Question을 혼합하지 않는다.
- 검색된 문서가 오래되었는지 확인한다.
- 중복 Chunk가 많으면 Context Window를 낭비한다.
- RAG 문서 변경 후 Embedding 재생성이 필요할 수 있다.
- Context 부족 시 추측하지 말고 Missing Information으로 처리한다.

---

### [FAQ]

Q. Retrieved Context가 뭐야?

A. RAG에서 검색된 문서 Chunk를 LLM Prompt에 포함한 근거 정보다.

Q. Retrieved Context는 왜 중요해?

A. LLM이 외부 문서에 근거해 답변하도록 만드는 핵심 정보이기 때문이다.

Q. Top-K를 높이면 항상 좋아?

A. 아니다. 관련 없는 Chunk가 많아지면 답변 품질이 떨어질 수 있다.

Q. Retrieved Context가 부족하면 어떻게 해?

A. 추가 검색하거나 문서에서 확인되지 않는다고 답해야 한다.

Q. Retrieved Context와 User Question은 분리해야 해?

A. 그렇다. 모델이 근거 문서와 사용자 요청을 혼동하지 않도록 분리해야 한다.

---

## 2.4 Tool Result Context

### [개념]

Tool Result Context는 Tool Calling 또는 Function Calling 실행 결과를 LLM에게 다시 전달하는 Context이다.

Tool Result는 외부 API, 검색, 파일 처리, 계산, DB 조회, 코드 실행 결과일 수 있다.

Tool Result Context 예:

- Web Search Result
- RAG Search Result
- Database Query Result
- File Read Result
- Code Execution Result
- Calendar Search Result
- Email Search Result
- API Response

---

### [핵심]

- Tool Result는 LLM이 직접 생성한 정보보다 근거성이 높을 수 있다.
- Tool Result도 검증이 필요하다.
- Tool Result 원문 전체를 그대로 넣으면 Token 낭비가 발생한다.
- 필요한 필드만 추출해 전달하는 것이 좋다.
- Tool 실패 결과도 명확히 전달해야 한다.
- Tool Result와 User Message를 구분해야 한다.

---

### [실무]

Tool Result 처리 Flow:

```text
LLM Tool Call
→ Validate Tool Arguments
→ Execute Tool
→ Validate Tool Result
→ Extract Relevant Fields
→ Build Tool Message
→ LLM Final Response
```

Tool Result Context 예:

```json
{
  "role": "tool",
  "content": {
    "status": "success",
    "result": {
      "documentTitle": "LLM Core API Integration Part02",
      "section": "Chat Completion",
      "summary": "Chat Completion uses role-based messages."
    }
  }
}
```

권장 기준:

| 항목        | 기준                      |
| ----------- | ------------------------- |
| Arguments   | 실행 전 검증              |
| Result Size | 필요한 필드만 전달        |
| Error       | 실패 원인 명확히 전달     |
| Secret      | 결과에서 제거             |
| Source      | 출처 또는 ID 포함         |
| Format      | JSON 또는 구조화된 텍스트 |
| Validation  | Null, Empty, Type 확인    |

주의:

- Tool Arguments를 그대로 신뢰하지 않는다.
- 파일 삭제, 결제, 배포 같은 위험 작업은 승인 절차가 필요하다.
- Tool Result에 Secret이 포함될 수 있으므로 Redaction이 필요하다.
- Tool Result가 너무 길면 Summary 또는 Field Selection을 사용한다.
- Tool 실패를 LLM이 성공으로 오해하지 않도록 상태 값을 명확히 넣는다.

---

### [FAQ]

Q. Tool Result Context는 뭐야?

A. Tool 실행 결과를 LLM에게 다시 전달해 최종 답변이나 다음 행동에 사용하게 하는 Context다.

Q. Tool Result는 그대로 믿어도 돼?

A. 아니다. Null, Error, Type, 권한, 최신성 등을 검증해야 한다.

Q. Tool Result 전체를 Prompt에 넣어도 돼?

A. 권장하지 않는다. 필요한 필드만 추출하거나 요약해서 넣는 것이 좋다.

Q. Tool 실패 결과는 어떻게 전달해?

A. `status`, `errorCode`, `message`처럼 실패 상태를 명확히 구조화해서 전달한다.

Q. Tool Result에 Secret이 있으면?

A. LLM Context나 로그에 넣기 전에 반드시 제거해야 한다.

---

# 3. Context Compression

## 3.1 Context Compression

### [개념]

Context Compression은 LLM Prompt에 넣을 정보를 줄이면서 핵심 의미를 유지하는 기법이다.

Context Compression은 Token Cost, Latency, Context Window 초과 문제를 줄이기 위해 사용한다.

대상:

- Conversation History
- Retrieved Context
- Tool Result
- Long Document
- Intermediate Agent Result
- Error Log
- Code Review Result

---

### [핵심]

- Context Compression은 정보 손실을 최소화해야 한다.
- 중요 제약 조건은 삭제하면 안 된다.
- 코드, API 스펙, 에러 메시지는 과도하게 요약하면 위험하다.
- RAG 문서는 Chunk 자체 품질을 먼저 개선해야 한다.
- Compression 결과도 검증해야 한다.
- Agent 간 전달은 Summary보다 Structured Output이 안정적인 경우가 많다.

---

### [실무]

Compression Flow:

```text
Raw Context
→ Remove Duplicates
→ Remove Irrelevant Content
→ Extract Key Facts
→ Preserve Constraints
→ Summarize
→ Validate Missing Critical Info
→ Build Prompt
```

Compression 방식:

| 방식                | 사용 대상                 |
| ------------------- | ------------------------- |
| Deduplication       | 중복 Chunk 제거           |
| Field Selection     | Tool Result, API Response |
| Summary             | Conversation History      |
| Key Fact Extraction | 요구사항, 결정 사항       |
| Code Slice          | 긴 코드 파일              |
| Error Snippet       | 로그 분석                 |
| Reranking           | Retrieved Context         |
| Schema Conversion   | Agent Intermediate Result |

예시:

```text
원문:
사용자가 여러 차례 RAG 문서 출력 형식을 지정했고 Part01, Part02를 완료했다.

압축:
RAG output style fixed. Part01 and Part02 completed. Next document must continue with same format.
```

주의:

- 압축 과정에서 금지 조건을 삭제하지 않는다.
- 날짜, 버전, API 필드명, 에러 메시지는 보존한다.
- 코드의 핵심 흐름을 임의로 생략하지 않는다.
- Summary가 원문과 충돌하면 원문 또는 최신 Tool Result를 우선한다.
- Compression 실패 시 원문 일부를 유지한다.

---

### [FAQ]

Q. Context Compression이 뭐야?

A. Prompt에 넣을 정보를 줄이면서 핵심 의미를 유지하는 작업이다.

Q. Context Compression은 왜 필요해?

A. Token 비용, Latency, Context Window 초과 문제를 줄이기 위해 필요하다.

Q. 무엇을 압축하면 좋아?

A. 긴 대화 이력, Tool Result, 중복 Retrieved Context, 긴 로그, 중간 Agent 결과를 압축할 수 있다.

Q. 압축하면 안 되는 정보는?

A. API 필드명, 에러 메시지, 보안 규칙, 출력 형식, 사용자 제약 조건, 코드 핵심 로직은 함부로 삭제하면 안 된다.

Q. Agent 간 전달에는 Summary만 쓰면 돼?

A. 항상 그렇지 않다. Output Schema가 필요한 경우 Structured Output이 더 안정적이다.

---

## 3.2 Conversation Summary

### [개념]

Conversation Summary는 긴 대화 이력을 짧은 요약으로 변환한 Context이다.

Conversation Summary는 장기 작업, 다단계 Agent Workflow, RAG 문서 제작, 코드 리뷰 누적 작업에 유용하다.

---

### [핵심]

- Conversation Summary는 Token 절약에 효과적이다.
- 현재 작업에 필요한 결정 사항을 보존해야 한다.
- 사용자 선호와 프로젝트 제약을 명확히 포함해야 한다.
- 오래된 임시 정보는 제거한다.
- 잘못된 결론은 Summary에 포함하지 않는다.
- Summary는 주기적으로 갱신해야 한다.

---

### [실무]

Conversation Summary 포함 항목:

| 항목            | 예                                  |
| --------------- | ----------------------------------- |
| Project Goal    | 개인 AI 개발팀 구축                 |
| Current Task    | LLM Core API Integration 문서 제작  |
| Completed Parts | Part01, Part02 완료                 |
| Output Format   | writing block 문서 형식             |
| Rules           | MASTER_RAG_RULES, DOMAIN_RULES 적용 |
| Constraints     | FAQ 강화, codeblock id 제거         |
| Next Step       | Part03 작성                         |

Conversation Summary 예:

```text
The user is creating RAG-optimized Markdown documents for LLM Core API Integration.
The output must use a writing block with document variant.
Part01 covered LLM Core Concept.
Part02 covered Chat Completion API.
Part03 should continue with Token and Context Management.
Apply MASTER_RAG_RULES and LLM Core API Integration Domain Rules.
Remove codeblock id attributes.
Optimize for retrieval, FAQ, and Agent usage.
```

갱신 Flow:

```text
After Final Output
→ Extract Completed Part
→ Extract New Rule
→ Remove Temporary Detail
→ Update Summary
→ Use in Next Prompt
```

주의:

- Summary에 민감정보를 저장하지 않는다.
- 사용자의 단기 감정 표현을 장기 규칙으로 저장하지 않는다.
- 완료된 파일명과 Part 번호는 정확히 유지한다.
- 출력 형식 관련 규칙은 누락하지 않는다.
- Summary와 최신 사용자 지시가 충돌하면 최신 지시를 우선한다.

---

### [FAQ]

Q. Conversation Summary는 뭐야?

A. 긴 대화 이력을 핵심 정보만 남긴 짧은 요약 Context다.

Q. Conversation Summary는 언제 필요해?

A. 긴 문서 제작, 코드 리뷰, Agent Workflow처럼 여러 단계가 이어질 때 필요하다.

Q. Summary에 무엇을 넣어야 해?

A. 목표, 완료된 작업, 현재 작업, 사용자 규칙, 출력 형식, 중요한 결정 사항을 넣는다.

Q. Summary에 넣으면 안 되는 것은?

A. 민감정보, 임시 감정 표현, 오래된 오류, 현재 작업과 무관한 정보는 넣지 않는다.

Q. Summary와 최신 요청이 충돌하면?

A. 최신 사용자 요청을 우선한다.

---

## 3.3 Retrieved Context Filtering

### [개념]

Retrieved Context Filtering은 RAG 검색 결과 중 답변에 필요한 Chunk만 선별하는 과정이다.

Filtering은 RAG 답변 품질, Token 비용, Latency, Hallucination 감소에 중요하다.

---

### [핵심]

- 검색 결과 전체를 Prompt에 넣지 않는다.
- 관련도 낮은 Chunk는 제거한다.
- 중복 Chunk는 제거한다.
- 오래된 Chunk와 최신 Chunk가 충돌하면 기준을 정한다.
- Query 의도와 맞는 Chunk를 우선한다.
- 필요한 경우 Reranking을 적용한다.

---

### [실무]

Filtering Flow:

```text
Search Results
→ Remove Low Score Chunks
→ Remove Duplicates
→ Check Query Intent
→ Rerank
→ Select Top Context
→ Build Prompt
```

Filtering 기준:

| 기준                | 설명                               |
| ------------------- | ---------------------------------- |
| Semantic Similarity | Query와 의미적으로 가까운가        |
| Keyword Match       | 핵심 용어가 포함되는가             |
| Section Match       | 질문 주제와 섹션이 맞는가          |
| Freshness           | 최신 기준과 충돌하지 않는가        |
| Source Priority     | Master, Domain, Part Rule 우선순위 |
| Redundancy          | 중복 내용이 아닌가                 |
| Completeness        | 답변에 필요한 정보가 충분한가      |

RAG 문서 우선순위:

```text
MASTER_RAG_RULES
→ DOMAIN_RULES
→ PART DOCUMENTS
→ General Knowledge
```

주의:

- 관련도 점수만 믿지 않는다.
- FAQ Chunk가 검색되었더라도 본문 근거가 필요할 수 있다.
- 코드 생성 작업은 코드 예제 Chunk를 우선한다.
- 개념 질문은 [개념], [핵심], [FAQ] Chunk를 우선한다.
- 실무 질문은 [실무], [주의], [Best Practice], [Troubleshooting] Chunk를 우선한다.

---

### [FAQ]

Q. Retrieved Context Filtering이 뭐야?

A. 검색된 RAG Chunk 중 답변에 필요한 내용만 골라 Prompt에 넣는 과정이다.

Q. 검색 결과를 전부 넣으면 안 돼?

A. 관련 없는 Chunk가 오답과 Hallucination을 유발하고 Token을 낭비할 수 있다.

Q. Filtering 기준은 뭐야?

A. 의미 유사도, 키워드 일치, 섹션 적합성, 최신성, 중복 여부, 문서 우선순위를 본다.

Q. FAQ Chunk만 있어도 답변해도 돼?

A. 간단한 질문은 가능하지만 코드 생성이나 실무 판단은 본문 Chunk도 함께 확인하는 것이 좋다.

Q. 문서 우선순위는 어떻게 잡아?

A. MASTER_RAG_RULES, DOMAIN_RULES, PART DOCUMENTS 순서로 규칙 우선순위를 적용한다.

---

# 4. Context Overflow Handling

## 4.1 Context Overflow

### [개념]

Context Overflow는 LLM 요청의 입력과 출력 예상 Token이 Context Window를 초과하는 상황이다.

Context Overflow는 요청 실패, Context Truncation, 응답 누락, 출력 잘림을 유발할 수 있다.

발생 원인:

- 너무 긴 User Prompt
- 긴 Conversation History
- 너무 많은 Retrieved Context
- Tool Result 원문 전체 삽입
- 긴 코드 파일 전체 삽입
- Output Reserve 부족
- Agent Intermediate Result 누적

---

### [핵심]

- Context Overflow는 사전에 예측해야 한다.
- 출력 Token Reserve를 남겨야 한다.
- 초과 시 중요한 규칙이 잘릴 수 있다.
- 일부 Provider는 자동 Truncation을 수행할 수 있다.
- 자동 Truncation은 중요한 Context 누락을 유발할 수 있다.
- Overflow 대응은 Error Handling과 Prompt Builder에 포함해야 한다.

---

### [실무]

Context Overflow 대응 Flow:

```text
Build Candidate Prompt
→ Estimate Token Count
→ Check Context Limit
→ Reserve Output Tokens
→ Compress or Filter Context
→ Retry Prompt Build
→ Call LLM
```

대응 전략:

| 문제                     | 대응                       |
| ------------------------ | -------------------------- |
| History가 김             | Conversation Summary 사용  |
| Retrieved Context가 많음 | Top-K 축소, Reranking      |
| Tool Result가 큼         | Field Selection, Summary   |
| 코드 파일이 큼           | 관련 함수/클래스만 추출    |
| 출력 요구가 김           | Part 분할, Max Tokens 조정 |
| 반복 Agent 결과 누적     | Intermediate Summary 사용  |

예시:

```text
입력 예상: 30000 tokens
출력 예약: 4000 tokens
모델 Context Window: 32000 tokens

결과:
30000 + 4000 > 32000
→ Context Overflow
→ Retrieved Context 축소 필요
```

주의:

- Output Reserve 없이 Context를 꽉 채우면 응답 생성 공간이 부족하다.
- 중요한 System Instruction이 잘리지 않도록 앞부분에 배치한다.
- 자동 Truncation에 의존하지 않는다.
- Overflow 발생 시 무작정 Max Tokens만 줄이지 않는다.
- 필요한 경우 작업을 Part 단위로 나눈다.

---

### [FAQ]

Q. Context Overflow가 뭐야?

A. 입력과 출력 예상 Token이 모델의 Context Window를 초과하는 상황이다.

Q. Context Overflow가 발생하면 어떻게 돼?

A. 요청 실패, Context 누락, 자동 Truncation, 응답 잘림이 발생할 수 있다.

Q. Output Reserve는 왜 필요해?

A. 모델이 응답을 생성할 Token 공간을 남겨야 하기 때문이다.

Q. Overflow는 어떻게 해결해?

A. 대화 이력을 요약하고, Retrieved Context를 줄이고, Tool Result를 필요한 필드만 남긴다.

Q. 자동 Truncation에 맡겨도 돼?

A. 권장하지 않는다. 중요한 규칙이나 근거 문서가 잘릴 수 있기 때문이다.

---

## 4.2 Context Truncation

### [개념]

Context Truncation은 Context Window 초과 또는 시스템 제한으로 인해 입력이나 출력 일부가 잘리는 현상이다.

Truncation은 명시적으로 처리하지 않으면 조용히 품질 저하를 만들 수 있다.

Truncation 종류:

- Input Truncation
- Output Truncation
- History Truncation
- Retrieved Context Truncation
- Tool Result Truncation
- JSON Output Truncation

---

### [핵심]

- Input Truncation은 중요한 지시나 근거 문서를 누락시킬 수 있다.
- Output Truncation은 응답이 중간에 끊긴 상태이다.
- JSON Output이 잘리면 파싱 실패가 발생한다.
- `finish_reason=length`는 Output Truncation 신호일 수 있다.
- Truncation은 사용자에게 완성 결과처럼 보여주면 안 된다.
- Truncation 로그와 재시도 정책이 필요하다.

---

### [실무]

Truncation Detection Flow:

```text
LLM Response
→ finish_reason 확인
→ content 완결성 확인
→ JSON Parse 확인
→ Required Section 확인
→ If Truncated, Retry or Split Task
```

출력 Truncation 대응:

| 상황               | 대응                    |
| ------------------ | ----------------------- |
| Markdown 응답 잘림 | 이어쓰기 또는 재생성    |
| JSON 응답 잘림     | 재요청, Max Tokens 증가 |
| 코드 응답 잘림     | 함수 단위 재요청        |
| RAG 답변 잘림      | 출력 범위 축소          |
| 문서 생성 잘림     | Part 분할               |
| Agent Output 잘림  | Schema 단순화           |

JSON Truncation 예:

```json
{
  "status": "success",
  "items": [
    {
      "name": "JWT"
```

처리:

```text
JSON Parse Failed
→ Check finish_reason
→ Retry with shorter context
→ Increase max_tokens if safe
→ Request valid JSON only
```

주의:

- 잘린 JSON을 임의로 보완하지 않는다.
- 잘린 코드에 임의로 닫는 괄호만 붙여서 완료 처리하지 않는다.
- 문서 생성에서는 Required Section 누락을 검수한다.
- Truncation이 반복되면 작업 범위를 나눈다.

---

### [FAQ]

Q. Context Truncation이 뭐야?

A. 입력이나 출력 일부가 Context Limit 또는 Max Tokens 제한으로 잘리는 현상이다.

Q. Output이 잘렸는지 어떻게 알아?

A. `finish_reason=length`, 불완전한 문장, 깨진 JSON, 누락된 섹션으로 확인할 수 있다.

Q. JSON Output이 잘리면 어떻게 해?

A. 잘린 JSON을 사용하지 말고 재요청하거나 Schema를 줄이고 Max Tokens를 조정한다.

Q. 코드가 잘렸으면 어떻게 해?

A. 잘린 코드를 완성본처럼 쓰지 말고 함수나 파일 단위로 다시 요청한다.

Q. Truncation이 반복되면?

A. 작업 범위를 분할하고 Context를 압축하거나 Retrieved Context를 줄인다.

---

# 5. Token and Context in RAG

## 5.1 RAG Token Budget

### [개념]

RAG Token Budget은 RAG 답변 생성에 필요한 Token 사용량을 분배하는 설계 기준이다.

RAG에서는 Retrieved Context가 입력 Token의 많은 부분을 차지한다.

RAG Token Budget 구성:

- System Rule
- User Query
- Query Rewrite
- Retrieved Context
- Source Metadata
- Answer Instruction
- Output Reserve

---

### [핵심]

- RAG Token Budget은 검색 품질과 답변 품질에 직접 영향을 준다.
- Retrieved Context를 많이 넣는 것이 항상 좋지는 않다.
- Chunk Size와 Top-K는 Token 사용량을 결정한다.
- Source Metadata는 짧고 유용해야 한다.
- Output Reserve를 반드시 확보해야 한다.
- Missing Information Rule은 짧지만 반드시 포함한다.

---

### [실무]

RAG Prompt Budget 예:

```text
System Rule: 500 tokens
User Query: 200 tokens
Retrieved Context: 8000 tokens
Source Metadata: 500 tokens
Answer Format: 300 tokens
Output Reserve: 2000 tokens
Safety Margin: 3000 tokens
```

RAG Context 선택 기준:

```text
Query Intent
→ Domain Rule Match
→ Section Match
→ Keyword Match
→ Semantic Similarity
→ Reranking
→ Deduplication
→ Final Context
```

RAG 답변 품질 개선:

- Chunk 제목을 명확히 작성한다.
- FAQ를 실제 질문 형태로 작성한다.
- Retrieval Queries를 문서 마지막에 추가한다.
- 코드 예제는 짧고 독립적으로 작성한다.
- Chunk는 300~1200 tokens 범위를 목표로 한다.
- 중복 설명을 줄인다.
- 동일 용어를 반복 사용한다.

주의:

- Top-K를 무작정 높이지 않는다.
- Chunk가 너무 길면 검색 정밀도가 낮아진다.
- Chunk가 너무 짧으면 답변 근거가 부족할 수 있다.
- 관련 없는 Chunk는 Hallucination을 증가시킨다.
- RAG 문서 변경 후 Embedding 재생성을 고려한다.

---

### [FAQ]

Q. RAG Token Budget이 뭐야?

A. RAG 답변 생성을 위해 System Rule, Query, Retrieved Context, Output Reserve에 Token을 배분하는 기준이다.

Q. RAG에서 Token을 가장 많이 쓰는 부분은?

A. Retrieved Context가 가장 많은 Token을 사용하는 경우가 많다.

Q. Top-K를 많이 올리면 답변이 좋아져?

A. 항상 그렇지 않다. 관련 없는 Chunk가 늘어나면 오히려 품질이 떨어질 수 있다.

Q. RAG에서 Output Reserve는 왜 필요해?

A. 모델이 답변을 생성할 Token 공간을 남겨야 하기 때문이다.

Q. RAG 문서에서 FAQ가 중요한 이유는?

A. 실제 사용자 질문과 검색 Query가 잘 매칭되어 Retrieval Hit를 높이기 때문이다.

---

## 5.2 Chunk Size and Context

### [개념]

Chunk Size는 RAG 문서를 검색 가능한 단위로 나눈 크기이다.

Chunk Size는 Retrieval 품질, Context Window 사용량, 답변 정확도에 영향을 준다.

좋은 Chunk는 독립 검색되어도 의미를 유지해야 한다.

---

### [핵심]

- Chunk는 하나의 개념만 포함하는 것이 좋다.
- 너무 긴 Chunk는 검색 정밀도를 낮춘다.
- 너무 짧은 Chunk는 맥락 부족을 만든다.
- 제목, 키워드, FAQ는 Retrieval 품질을 높인다.
- Code Snippet은 짧고 직접적이어야 한다.
- Chunk 간 중복은 최소화하되 필요한 문맥은 유지한다.

---

### [실무]

권장 Chunk 기준:

```text
Target Chunk Size
→ 300 ~ 1200 tokens

One Chunk
→ One Concept
→ Clear Title
→ Key Points
→ Practical Rule
→ FAQ
```

좋은 Chunk 구조:

```text
## 2.1 Context Window

### [개념]
Context Window 정의

### [핵심]
핵심 bullet

### [실무]
Prompt 구성 기준

### [FAQ]
사용자 질문 표현
```

나쁜 Chunk:

```text
LLM 개념
+ Token
+ Context Window
+ API 호출
+ Retry
+ Rate Limit
+ 비용 관리
→ 하나의 Chunk에 과도한 개념 혼합
```

주의:

- Part 문서 전체를 하나의 긴 Chunk처럼 작성하지 않는다.
- 불필요한 장문 서론을 피한다.
- 같은 용어를 여러 표현으로 섞지 않는다.
- 코드 예제는 전체 프로젝트 코드보다 핵심 Snippet 중심으로 작성한다.
- Retrieval Queries는 문서 마지막에 포함한다.

---

### [FAQ]

Q. Chunk Size는 뭐야?

A. RAG 문서를 검색 가능한 단위로 나눈 크기다.

Q. 좋은 Chunk의 기준은?

A. 하나의 개념을 명확한 제목, 핵심 설명, 짧은 예제, FAQ와 함께 담는 것이다.

Q. Chunk가 너무 길면?

A. 검색 정밀도가 낮아지고 Context Window를 많이 사용한다.

Q. Chunk가 너무 짧으면?

A. 필요한 맥락이 부족해 답변이 부정확해질 수 있다.

Q. RAG 문서에서 제목이 중요한 이유는?

A. 제목은 검색 Query와 Semantic Similarity에 영향을 주기 때문이다.

---

# 6. Token and Context in Agent Workflow

## 6.1 Agent State Context

### [개념]

Agent State Context는 Agent Workflow에서 현재 작업 상태, 이전 단계 결과, Tool Result, Memory를 LLM Prompt에 포함한 Context이다.

Agent State는 Multi-Agent System에서 작업 연속성을 유지하는 핵심 데이터이다.

Agent State 구성:

- User Request
- Current Goal
- Current Step
- Previous Agent Output
- Tool Result
- Memory
- Error State
- Review Result
- Final Output Candidate

---

### [핵심]

- Agent State는 Token을 지속적으로 소비한다.
- Agent State가 커지면 Context Window를 빠르게 초과한다.
- Agent 간 전달 데이터는 구조화해야 한다.
- 이전 Agent의 오류가 다음 Agent로 전파될 수 있다.
- Review Agent는 State 품질을 검증해야 한다.
- Agent State는 Summary와 Schema를 함께 사용하는 것이 좋다.

---

### [실무]

Agent State Flow:

```text
User Request
→ PM Agent State
→ Backend Agent Input
→ Backend Agent Output
→ Review Agent Input
→ Review Result
→ Final Response
```

Agent State 예:

```json
{
  "taskId": "task-001",
  "goal": "Create RAG document Part03",
  "currentPart": "Token and Context Management",
  "completedParts": ["Part01 LLM Core Concept", "Part02 Chat Completion API"],
  "rules": ["MASTER_RAG_RULES", "LLM Core API Integration Domain Rules"],
  "outputFormat": "writing block document"
}
```

권장 기준:

| 항목          | 기준                       |
| ------------- | -------------------------- |
| User Request  | 원문 보존                  |
| Agent Output  | Schema 기반                |
| Tool Result   | 필요한 필드만              |
| Error         | 상태와 원인 분리           |
| Review Result | 수정 필요 항목만           |
| Memory        | 장기 정보와 단기 정보 분리 |
| Final Output  | 검수 후 생성               |

주의:

- Agent State에 전체 대화 원문을 넣지 않는다.
- Agent Output은 다음 Agent가 파싱 가능해야 한다.
- State가 커지면 Summary 또는 Field Selection을 사용한다.
- 오류 있는 중간 결과는 Review 없이 전파하지 않는다.
- Max Step과 Stop Condition을 둔다.

---

### [FAQ]

Q. Agent State Context는 뭐야?

A. Agent가 현재 작업을 이어가기 위해 사용하는 상태, 이전 결과, Tool Result, Memory Context다.

Q. Agent State가 너무 커지면?

A. Context Window를 초과하거나 비용과 Latency가 증가한다.

Q. Agent 간 결과는 어떻게 전달해?

A. Summary 또는 JSON Schema 같은 Structured Output으로 전달하는 것이 좋다.

Q. Agent State에서 가장 중요한 것은?

A. 현재 목표, 완료된 단계, 다음 작업, 검증된 중간 결과, 오류 상태다.

Q. Agent State 오류는 왜 위험해?

A. 잘못된 중간 결과가 다음 Agent에 전파되어 전체 Workflow가 틀어질 수 있다.

---

## 6.2 Intermediate Result Compression

### [개념]

Intermediate Result Compression은 Agent Workflow 중간 결과를 다음 단계에 필요한 형태로 압축하는 작업이다.

중간 결과는 코드, 분석, 검색 결과, 리뷰 결과, 테스트 결과, 오류 로그일 수 있다.

---

### [핵심]

- Agent 중간 결과는 계속 누적되면 Token 비용이 증가한다.
- 다음 Agent에 필요한 정보만 전달해야 한다.
- 중간 결과의 원본이 필요한 경우 Reference를 남긴다.
- Review 결과는 수정 지시 중심으로 압축한다.
- 테스트 결과는 실패 케이스와 원인 중심으로 압축한다.
- 코드 생성 결과는 파일명, 변경 요약, 핵심 코드로 압축할 수 있다.

---

### [실무]

Compression Flow:

```text
Intermediate Result
→ Identify Next Agent Need
→ Extract Key Facts
→ Preserve Critical Details
→ Convert to Schema
→ Validate
→ Pass to Next Agent
```

Agent별 압축 기준:

| 이전 결과           | 다음 전달 내용                       |
| ------------------- | ------------------------------------ |
| PM Agent Plan       | 요구사항, 우선순위, 작업 단위        |
| Backend Agent Code  | 파일명, 메서드, 변경 요약, 위험 지점 |
| Frontend Agent Code | Component, State, API 연동 정보      |
| Review Agent Result | 문제, 심각도, 수정 지시              |
| Test Agent Result   | 실패 테스트, 원인, 재현 방법         |
| DevOps Agent Result | 환경, 명령어, 설정 파일, 오류        |

예시:

```json
{
  "status": "needs_fix",
  "summary": "Service method lacks timeout handling.",
  "issues": [
    {
      "severity": "high",
      "target": "LlmClient.chat",
      "problem": "No timeout handling for LLM API call",
      "recommendation": "Add timeout and error mapping"
    }
  ]
}
```

주의:

- 압축 과정에서 실패 원인을 삭제하지 않는다.
- 코드 리뷰에서는 파일명과 메서드명을 보존한다.
- 테스트 실패에서는 입력값과 기대값을 보존한다.
- 보안 이슈는 절대 단순 요약으로 흐리지 않는다.
- 다음 Agent가 실행 가능한 수준으로 구체성을 유지한다.

---

### [FAQ]

Q. Intermediate Result Compression은 뭐야?

A. Agent Workflow 중간 결과를 다음 단계에 필요한 정보만 남겨 압축하는 작업이다.

Q. 왜 중간 결과를 압축해야 해?

A. Token 비용과 Context Window 사용량을 줄이고 다음 Agent의 판단을 명확하게 하기 위해서다.

Q. 압축할 때 반드시 남길 것은?

A. 파일명, 메서드명, 오류 원인, 요구사항, 심각도, 수정 지시 같은 실행 가능한 정보다.

Q. Review 결과는 어떻게 압축해?

A. 문제, 심각도, 대상 위치, 수정 권장 사항 중심으로 구조화한다.

Q. 너무 압축하면 어떤 문제가 생겨?

A. 다음 Agent가 필요한 맥락을 잃어 잘못된 수정이나 판단을 할 수 있다.

---

# 7. Common Mistakes

## 7.1 Token and Context Common Mistakes

### [개념]

Token and Context Common Mistakes는 LLM API, RAG, Agent Workflow에서 Token과 Context를 잘못 관리해 발생하는 오류이다.

---

### [핵심]

자주 발생하는 실수:

- Token Limit을 고려하지 않음
- Context Window를 무제한으로 가정
- Output Reserve를 남기지 않음
- 긴 Conversation History를 계속 삽입
- Retrieved Context를 과도하게 삽입
- Tool Result 원문 전체를 삽입
- Agent State를 계속 누적
- Context Compression 없이 긴 작업 수행
- `finish_reason=length`를 무시
- JSON Truncation을 검증하지 않음
- Chunk Size를 너무 크게 작성
- FAQ와 Retrieval Queries를 누락
- Top-K를 무작정 높임
- 관련 없는 Chunk를 제거하지 않음
- 비용과 Latency를 로그로 남기지 않음

---

### [실무]

문제 진단 Flow:

```text
LLM 응답 품질 저하
→ Token Usage 확인
→ Context Length 확인
→ Retrieved Context 확인
→ Conversation History 확인
→ Tool Result 크기 확인
→ finish_reason 확인
→ Prompt 구조 확인
```

대응 기준:

| 문제            | 해결                                |
| --------------- | ----------------------------------- |
| 비용 증가       | Context Filtering, Max Tokens 제한  |
| Latency 증가    | Context 압축, 작은 모델 사용        |
| 응답 잘림       | Output Reserve 확보, 작업 분할      |
| RAG 오답        | Chunk Filtering, Reranking          |
| Agent 오류 전파 | Intermediate Result 검증            |
| JSON 파싱 실패  | Truncation 확인, Schema 단순화      |
| Context 초과    | Summary, Field Selection, Part 분할 |

검수 Checklist:

```text
Token Budget이 있는가?
Output Reserve가 있는가?
Conversation History를 요약했는가?
Retrieved Context가 관련 Chunk만 포함하는가?
Tool Result를 필요한 필드만 전달하는가?
finish_reason을 확인하는가?
JSON Output Truncation을 처리하는가?
Usage Logging이 있는가?
Agent State가 무한 누적되지 않는가?
```

---

### [FAQ]

Q. Token 관리에서 가장 흔한 실수는?

A. Context Window와 Output Reserve를 고려하지 않고 긴 Prompt를 보내는 것이다.

Q. RAG에서 가장 흔한 Context 실수는?

A. 검색된 Chunk를 너무 많이 넣거나 관련 없는 Chunk를 제거하지 않는 것이다.

Q. Agent Workflow에서 가장 흔한 Context 실수는?

A. Agent State와 중간 결과를 계속 누적해 Context Window를 초과하는 것이다.

Q. 응답이 중간에 잘리면 무엇을 확인해야 해?

A. `finish_reason`, Max Tokens, Output Reserve, Context Window 사용량을 확인해야 한다.

Q. Token 비용을 줄이는 가장 기본 방법은?

A. 관련 없는 Context를 줄이고, 출력 길이를 제한하고, 반복 결과를 Cache하는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Token이 뭐야?
A. Token은 LLM이 텍스트를 읽고 생성할 때 사용하는 기본 처리 단위다.

Q. Input Token이 뭐야?
A. Input Token은 System Message, User Message, Conversation History, Retrieved Context처럼 모델에 입력되는 Token이다.

Q. Output Token이 뭐야?
A. Output Token은 LLM이 응답으로 생성하는 Token이다.

Q. Total Token이 뭐야?
A. Total Token은 Input Token과 Output Token을 합친 전체 Token 사용량이다.

Q. Token은 왜 비용에 영향을 줘?
A. LLM API는 보통 입력과 출력 Token 사용량을 기준으로 비용이 계산되기 때문이다.

Q. Token은 왜 Latency에 영향을 줘?
A. 입력 Token이 많으면 처리 시간이 늘고 출력 Token이 많으면 생성 시간이 늘기 때문이다.

Q. Context Window가 뭐야?
A. Context Window는 LLM이 한 번에 참고할 수 있는 입력과 출력의 최대 Token 범위다.

Q. Context Window에는 출력도 포함돼?
A. 그렇다. 입력뿐 아니라 모델이 생성할 Output Token 공간도 필요하다.

Q. Output Reserve가 뭐야?
A. 모델이 응답을 생성할 수 있도록 남겨두는 출력 Token 여유 공간이다.

Q. Context Overflow가 뭐야?
A. 입력과 출력 예상 Token이 모델의 Context Window를 초과하는 상황이다.

Q. Context Truncation이 뭐야?
A. 입력이나 출력 일부가 Token 제한 때문에 잘리는 현상이다.

Q. `finish_reason=length`는 뭐야?
A. Max Tokens 또는 Context 제한으로 응답이 중간에 잘렸을 가능성이 있다는 의미다.

Q. Conversation History는 어떻게 관리해?
A. 전체 대화 원문 대신 최근 대화와 Conversation Summary를 사용한다.

Q. Conversation Summary는 뭐야?
A. 긴 대화 이력을 현재 작업에 필요한 핵심 정보로 압축한 Context다.

Q. Retrieved Context가 뭐야?
A. RAG에서 검색된 문서 Chunk를 LLM Prompt에 포함한 근거 정보다.

Q. Retrieved Context를 많이 넣으면 좋아?
A. 항상 그렇지 않다. 관련 없는 Chunk가 많으면 답변 품질이 떨어질 수 있다.

Q. Retrieved Context Filtering이 뭐야?
A. 검색된 Chunk 중 답변에 필요한 관련 Chunk만 선별하는 과정이다.

Q. Tool Result Context는 뭐야?
A. Tool Calling 실행 결과를 LLM에게 다시 전달하는 Context다.

Q. Tool Result는 어떻게 전달해야 해?
A. 필요한 필드만 추출하고 Secret을 제거한 뒤 구조화해서 전달해야 한다.

Q. Context Compression이 뭐야?
A. Prompt에 넣을 정보를 줄이면서 핵심 의미를 유지하는 작업이다.

Q. RAG Token Budget은 뭐야?
A. RAG 답변 생성을 위해 System Rule, Query, Retrieved Context, Output Reserve에 Token을 배분하는 기준이다.

Q. Chunk Size는 왜 중요해?
A. Chunk Size는 검색 정밀도, Context 사용량, RAG 답변 품질에 직접 영향을 준다.

Q. 좋은 Chunk 기준은?
A. 하나의 개념을 명확한 제목, 핵심 설명, 짧은 예제, FAQ로 독립 검색 가능하게 구성하는 것이다.

Q. Agent State Context는 뭐야?
A. Agent가 현재 작업을 이어가기 위해 사용하는 상태, 이전 결과, Tool Result, Memory Context다.

Q. Intermediate Result Compression은 뭐야?
A. Agent Workflow 중간 결과를 다음 단계에 필요한 정보만 남겨 압축하는 작업이다.

Q. Token 비용은 어떻게 줄여?
A. 관련 없는 Context를 제거하고, Conversation History를 요약하며, Max Tokens를 제한하고, Cache를 활용한다.

Q. Token Latency는 어떻게 줄여?
A. Context를 줄이고, 출력 길이를 제한하고, 작은 모델을 사용하거나 Streaming을 적용한다.

Q. RAG에서 Top-K를 무작정 높이면 안 되는 이유는?
A. 관련 없는 Chunk가 늘어나 Token을 낭비하고 Hallucination 가능성을 높일 수 있기 때문이다.

Q. Agent에서 Context Window 초과를 막으려면?
A. Agent State를 구조화하고 중간 결과를 압축하며 Max Step과 Stop Condition을 둔다.
