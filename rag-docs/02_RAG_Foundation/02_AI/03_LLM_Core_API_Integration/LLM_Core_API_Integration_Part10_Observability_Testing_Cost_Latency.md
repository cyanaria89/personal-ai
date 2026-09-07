# LLM Core & API Integration Part10 - Observability, Testing, Cost & Latency

---

# 1. AI Observability

## 1.1 AI Observability

### [개념]

AI Observability는 LLM API 호출, RAG Retrieval, Tool Calling, Agent Workflow, Token 사용량, Latency, Error, Output 품질을 관측하는 체계이다.

일반 Backend Observability가 HTTP 요청, DB, 서버 상태를 본다면 AI Observability는 모델 입력과 출력, Retrieval 품질, Agent 의사결정, Token 비용까지 함께 본다.

AI Observability 대상:

- LLM Request
- LLM Response
- Prompt
- Model
- Token Usage
- Latency
- Finish Reason
- Error Code
- Retry Count
- Retrieved Context
- Tool Call
- Agent Step
- Validation Result
- Cost
- User Feedback

AI Observability Flow:

```text
User Request
→ Prompt Build
→ Retrieval
→ LLM Call
→ Tool Call
→ Validation
→ Final Response
→ Logging / Metrics / Trace
```

---

### [핵심]

- AI Observability는 LLM 시스템의 품질, 비용, 속도, 안정성을 추적한다.
- LLM API 호출 로그는 requestId 기준으로 추적한다.
- Token Usage는 비용 분석의 핵심이다.
- Latency는 사용자 경험과 시스템 병목 분석에 필요하다.
- Retrieval Log는 RAG 답변 품질 개선에 필요하다.
- Tool Call Log는 Agent 안전성과 실행 추적에 필요하다.
- Validation Log는 Hallucination과 Invalid Output 개선에 필요하다.
- Secret과 개인정보는 로그에서 제거해야 한다.

---

### [실무]

2026 실무 기준 LLM 시스템은 단순 API 호출 로그만으로 운영하기 어렵다.

권장 Trace 구조:

```text
requestId
→ userRequest
→ promptTemplateVersion
→ retrievalQuery
→ retrievedChunks
→ model
→ parameters
→ response
→ validationResult
→ finalOutput
```

AI Observability 핵심 지표:

| 지표                    | 목적                        |
| ----------------------- | --------------------------- |
| Request Count           | 사용량 확인                 |
| Token Usage             | 비용 추적                   |
| Latency                 | 성능 분석                   |
| Error Rate              | 안정성 분석                 |
| Retry Count             | 외부 API 품질 확인          |
| Rate Limit Count        | 호출량 조정                 |
| Finish Reason           | 출력 잘림 확인              |
| Invalid JSON Rate       | Structured Output 품질 확인 |
| Retrieval Hit Rate      | RAG 검색 품질 확인          |
| Tool Call Success Rate  | Agent 실행 안정성 확인      |
| Validation Failure Rate | 출력 품질 확인              |
| User Feedback           | 실제 만족도 확인            |

권장 로그 구조:

```json
{
  "requestId": "req-20260630-001",
  "feature": "rag_answer",
  "model": "qwen2.5:14b",
  "promptTemplateVersion": "llm-core-v1",
  "inputTokens": 2400,
  "outputTokens": 520,
  "latencyMs": 1850,
  "finishReason": "stop",
  "retryCount": 0,
  "status": "success"
}
```

주의:

- Prompt 전문 저장은 보안 정책이 필요하다.
- API Key, Authorization Header, Secret은 절대 로그에 남기지 않는다.
- RAG 문서 원문이 민감할 수 있으므로 저장 범위를 제한한다.
- Tool Arguments에는 개인정보나 Secret이 포함될 수 있다.
- 로그가 많아지면 저장 비용과 개인정보 위험이 증가한다.

---

### [FAQ]

Q. AI Observability가 뭐야?

A. LLM 호출, RAG 검색, Tool 실행, Agent 단계, Token, Latency, Error, 품질을 관측하는 체계다.

Q. 일반 Observability와 뭐가 달라?

A. 일반 서버 지표뿐 아니라 Prompt, Token, Retrieval, Tool Call, Validation, Output 품질까지 추적한다.

Q. AI Observability가 왜 필요해?

A. LLM 답변 품질, 비용, 속도, 오류 원인을 분석하고 개선하기 위해 필요하다.

Q. AI Observability에서 절대 로그에 남기면 안 되는 것은?

A. API Key, Authorization Header, Secret, 개인정보, 민감한 Prompt 원문이다.

---

## 1.2 Request Trace

### [개념]

Request Trace는 하나의 사용자 요청이 LLM API, RAG Retrieval, Tool Calling, Agent Workflow를 거쳐 최종 응답으로 변환되는 전체 과정을 추적하는 기록이다.

Request Trace는 장애 분석, 품질 개선, 비용 분석, Agent 디버깅에 필요하다.

Trace 구성:

- requestId
- userIdHash
- sessionId
- featureName
- agentName
- stepName
- model
- promptTemplateVersion
- retrievalQuery
- toolName
- latencyMs
- status
- errorCode
- finalResult

---

### [핵심]

- 모든 LLM 요청에는 requestId가 있어야 한다.
- Multi-Agent Workflow에서는 agentStepId가 필요하다.
- RAG 검색과 LLM 호출을 같은 Trace에 연결해야 한다.
- Tool Call과 Tool Result도 같은 Trace에 포함한다.
- Retry는 원 요청과 연결해야 한다.
- 사용자 식별자는 Hash 또는 내부 ID로 관리한다.
- Trace는 디버깅 가능하되 Secret을 포함하면 안 된다.

---

### [실무]

Request Trace 예:

```json
{
  "requestId": "req-001",
  "sessionId": "session-abc",
  "feature": "rag_document_review",
  "steps": [
    {
      "step": "query_rewrite",
      "status": "success",
      "latencyMs": 120
    },
    {
      "step": "retrieval",
      "status": "success",
      "topK": 5,
      "latencyMs": 80
    },
    {
      "step": "llm_generation",
      "status": "success",
      "model": "qwen2.5:14b",
      "inputTokens": 3200,
      "outputTokens": 900,
      "latencyMs": 2200
    },
    {
      "step": "validation",
      "status": "success",
      "latencyMs": 40
    }
  ]
}
```

Trace 설계 기준:

| 항목             | 기준                               |
| ---------------- | ---------------------------------- |
| requestId        | 전체 요청 추적                     |
| stepId           | Agent / Tool / Retrieval 단계 추적 |
| model            | 모델별 품질 비교                   |
| tokenUsage       | 비용 분석                          |
| latencyMs        | 병목 분석                          |
| retryCount       | 안정성 분석                        |
| errorCode        | 오류 분류                          |
| validationResult | 출력 품질 확인                     |
| redaction        | 민감정보 제거                      |

Trace Flow:

```text
Request Start
→ Generate requestId
→ Log Prompt Build Step
→ Log Retrieval Step
→ Log LLM Call Step
→ Log Tool Step
→ Log Validation Step
→ Log Final Result
```

주의:

- Trace에 Raw API Key를 포함하지 않는다.
- 사용자 원문 Prompt 저장 여부는 보안 정책에 따라 결정한다.
- Agent 내부 Chain-of-Thought를 저장하지 않는다.
- Tool Result 전체 원문 저장은 민감정보 위험이 있다.
- Trace ID를 사용자 응답에 노출할지 여부는 정책으로 정한다.

---

### [FAQ]

Q. Request Trace가 뭐야?

A. 사용자 요청이 Retrieval, LLM, Tool, Agent, Validation을 거쳐 최종 응답이 되는 전체 과정을 추적하는 기록이다.

Q. requestId는 왜 필요해?

A. 하나의 요청에서 발생한 로그, 오류, Token 사용량, Tool 호출을 연결하기 위해 필요하다.

Q. Agent Workflow에는 어떤 Trace가 필요해?

A. agentName, stepName, toolName, status, latency, errorCode, retryCount, validationResult가 필요하다.

Q. Trace에 사용자 입력을 그대로 저장해도 돼?

A. 보안 정책이 있을 때만 제한적으로 가능하며 기본적으로는 민감정보 Redaction이 필요하다.

---

## 1.3 Metrics

### [개념]

Metrics는 LLM 시스템 상태를 숫자로 집계한 지표이다.

Metrics는 운영 상태, 비용, 성능, 오류율, 품질 추세를 대시보드와 알림으로 관리하는 데 사용한다.

LLM Metrics 대상:

- Request Count
- Error Count
- Latency
- Token Usage
- Cost
- Retry Count
- Rate Limit Count
- Timeout Count
- Validation Failure Count
- Retrieval Empty Count
- Tool Failure Count
- Agent Step Count

---

### [핵심]

- Metrics는 추세 분석에 적합하다.
- Latency p50, p95, p99를 본다.
- Token Usage는 모델별, 기능별로 집계한다.
- Error Rate는 Provider와 Model 기준으로 나눠 본다.
- Validation Failure Rate는 Prompt와 Schema 품질을 보여준다.
- Retrieval Empty Rate는 RAG 문서 품질과 Query Rewrite 품질을 보여준다.
- Tool Failure Rate는 Agent 안정성을 보여준다.
- Metrics Label에 개인정보를 넣지 않는다.

---

### [실무]

권장 Metrics:

```text
llm_request_total
llm_request_failed_total
llm_latency_ms
llm_input_tokens_total
llm_output_tokens_total
llm_total_tokens_total
llm_retry_total
llm_timeout_total
llm_rate_limit_total
llm_invalid_json_total
llm_schema_validation_failed_total
llm_truncated_output_total
rag_retrieval_total
rag_retrieval_empty_total
rag_retrieval_latency_ms
tool_call_total
tool_call_failed_total
agent_step_total
agent_step_failed_total
```

Label 기준:

| Label      | 설명                   |
| ---------- | ---------------------- |
| provider   | LLM Provider           |
| model      | 모델명                 |
| feature    | 기능명                 |
| agent      | Agent 이름             |
| status     | success / failed       |
| errorCode  | 표준 오류 코드         |
| outputType | markdown / json / code |
| toolName   | Tool 이름              |
| domain     | RAG 문서 도메인        |

Metrics 활용:

| 지표                 | 개선 방향                          |
| -------------------- | ---------------------------------- |
| latency p95 증가     | Context 축소, 모델 변경, Streaming |
| token usage 증가     | Prompt 압축, Top-K 조정            |
| invalid JSON 증가    | Schema 단순화, Prompt 개선         |
| retrieval empty 증가 | Chunk 개선, Query Rewrite          |
| timeout 증가         | Timeout 조정, 작업 분할            |
| rate limit 증가      | Queue, Throttling                  |
| tool failure 증가    | Tool Validation 개선               |

주의:

- Label Cardinality를 과도하게 높이지 않는다.
- userId, email, prompt text를 Metrics Label에 넣지 않는다.
- Metrics는 원인 분석의 시작점이지 전체 답은 아니다.
- 로그와 Trace를 함께 봐야 구체 원인을 찾을 수 있다.
- Local LLM은 하드웨어 Metrics도 함께 본다.

---

### [FAQ]

Q. Metrics가 뭐야?

A. LLM 시스템의 요청 수, 오류율, Latency, Token 사용량, 비용, 품질 실패율을 숫자로 집계한 지표다.

Q. LLM 시스템에서 중요한 Metrics는?

A. Request Count, Error Rate, Latency, Token Usage, Cost, Retry, Rate Limit, Validation Failure, Retrieval Empty Rate다.

Q. Metrics Label에 userId를 넣어도 돼?

A. 권장하지 않는다. 개인정보 위험과 Label Cardinality 문제가 있으므로 Hash 또는 집계 기준을 사용한다.

Q. Retrieval Empty Rate는 왜 중요해?

A. RAG 검색이 사용자의 질문에 맞는 문서를 찾지 못하는 비율을 보여주기 때문이다.

---

# 2. Usage Logging

## 2.1 Token Usage Logging

### [개념]

Token Usage Logging은 LLM API 호출에서 사용된 Input Token, Output Token, Total Token을 기록하는 작업이다.

Token Usage는 비용, Latency, Context 최적화, 사용자별 사용량 제한의 핵심 데이터이다.

Token Usage 항목:

- inputTokens
- outputTokens
- totalTokens
- promptTokens
- completionTokens
- cachedTokens
- reasoningTokens
- embeddingTokens

---

### [핵심]

- Token Usage는 비용 계산에 필요하다.
- Input Token은 Prompt, Context, History, Retrieved Context를 포함한다.
- Output Token은 모델이 생성한 응답이다.
- RAG에서는 Retrieved Context가 Input Token의 큰 비중을 차지한다.
- Agent Workflow에서는 여러 번 LLM 호출하므로 Token이 누적된다.
- Provider가 Usage를 제공하지 않으면 내부 추정이 필요할 수 있다.
- Token Usage는 모델별, 기능별, 사용자별로 집계한다.

---

### [실무]

Token Usage Log 예:

```json
{
  "requestId": "req-001",
  "feature": "rag_answer",
  "model": "model-name",
  "inputTokens": 3200,
  "outputTokens": 850,
  "totalTokens": 4050,
  "retrievedContextTokens": 2100,
  "conversationTokens": 400,
  "systemPromptTokens": 300
}
```

Token Usage 집계 기준:

| 기준        | 목적                   |
| ----------- | ---------------------- |
| model       | 모델별 비용 비교       |
| feature     | 기능별 비용 분석       |
| userIdHash  | 사용자별 사용량 제한   |
| workspaceId | 프로젝트별 비용 관리   |
| agent       | Agent별 비용 분석      |
| domain      | RAG 도메인별 비용 분석 |
| date        | 일별/월별 비용 추세    |

Token Logging Flow:

```text
LLM Response
→ Extract Usage
→ Normalize Field Names
→ Estimate Missing Usage if Needed
→ Save Usage Log
→ Aggregate Cost
```

주의:

- Usage 필드명은 Provider마다 다를 수 있다.
- Streaming에서는 Usage가 없거나 마지막 이벤트에만 있을 수 있다.
- Local LLM은 Token Usage를 직접 제공하지 않을 수 있다.
- Token 추정치는 실제 비용과 차이가 있을 수 있다.
- Prompt 원문 없이도 Token 통계는 남길 수 있다.

---

### [FAQ]

Q. Token Usage Logging이 뭐야?

A. LLM API 호출에서 사용된 Input Token, Output Token, Total Token을 기록하는 작업이다.

Q. Token Usage를 왜 기록해?

A. 비용 관리, Context 최적화, 사용자별 제한, 성능 분석에 필요하기 때문이다.

Q. Provider가 Usage를 제공하지 않으면?

A. 내부 Tokenizer 또는 문자열 길이 기반 추정치를 사용할 수 있다.

Q. Streaming에서도 Token Usage를 기록할 수 있어?

A. Provider에 따라 가능하다. 마지막 이벤트에 제공되거나 제공되지 않을 수 있으므로 Optional 처리해야 한다.

---

## 2.2 Usage Log Schema

### [개념]

Usage Log Schema는 LLM API 사용량을 일관된 형태로 저장하기 위한 데이터 구조이다.

Usage Log는 비용 계산, 분석, 제한 정책, 대시보드, 감사 로그에 사용된다.

Usage Log 구성:

- requestId
- userIdHash
- workspaceId
- feature
- provider
- model
- inputTokens
- outputTokens
- totalTokens
- estimatedCost
- latencyMs
- status
- errorCode
- createdAt

---

### [핵심]

- Usage Log는 표준 Schema로 저장한다.
- Provider별 Usage 필드는 내부 표준 필드로 변환한다.
- userId는 직접 저장보다 Hash 또는 내부 ID를 사용한다.
- 비용 계산을 위해 model과 token 단가가 필요하다.
- 실패 요청도 Usage가 발생할 수 있으므로 기록한다.
- Retry 요청은 원 요청과 연결한다.
- Embedding 사용량도 별도 기록한다.

---

### [실무]

Usage Log Schema 예:

```json
{
  "requestId": "req-20260630-001",
  "parentRequestId": null,
  "userIdHash": "u_hash_001",
  "workspaceId": "personal-ai",
  "feature": "llm_chat",
  "provider": "local_ollama",
  "model": "qwen2.5:14b",
  "inputTokens": 1800,
  "outputTokens": 420,
  "totalTokens": 2220,
  "estimatedCost": 0,
  "latencyMs": 2100,
  "status": "success",
  "errorCode": null,
  "createdAt": "2026-06-30T00:00:00+09:00"
}
```

DB Table 예:

```sql
CREATE TABLE llm_usage_logs (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    request_id VARCHAR(100) NOT NULL,
    parent_request_id VARCHAR(100),
    user_id_hash VARCHAR(100),
    workspace_id VARCHAR(100),
    feature VARCHAR(100) NOT NULL,
    provider VARCHAR(100) NOT NULL,
    model VARCHAR(100) NOT NULL,
    input_tokens BIGINT DEFAULT 0,
    output_tokens BIGINT DEFAULT 0,
    total_tokens BIGINT DEFAULT 0,
    estimated_cost DECIMAL(18, 8) DEFAULT 0,
    latency_ms BIGINT,
    status VARCHAR(50) NOT NULL,
    error_code VARCHAR(100),
    created_at TIMESTAMP NOT NULL
);
```

Schema 설계 기준:

| 필드              | 목적                    |
| ----------------- | ----------------------- |
| request_id        | 요청 추적               |
| parent_request_id | Retry / Agent Step 연결 |
| feature           | 기능별 비용 분석        |
| provider          | Provider별 비교         |
| model             | 모델별 비용 분석        |
| tokens            | 사용량 계산             |
| estimated_cost    | 비용 계산               |
| latency_ms        | 성능 분석               |
| status            | 성공/실패 분석          |
| error_code        | 오류 유형 분석          |

주의:

- Prompt 원문을 Usage Log에 저장하지 않는다.
- 사용자 개인정보는 Hash 처리하거나 별도 관리한다.
- Local LLM 비용은 0 또는 내부 자원 비용으로 계산할 수 있다.
- Retry 요청은 별도 Row로 저장하되 parentRequestId로 연결한다.
- Usage Log 보관 기간을 정한다.

---

### [FAQ]

Q. Usage Log Schema가 뭐야?

A. LLM API 사용량을 일관된 형태로 저장하기 위한 데이터 구조다.

Q. 실패 요청도 Usage Log에 남겨야 해?

A. 그렇다. 실패해도 Token 비용이나 Latency가 발생할 수 있고 장애 분석에 필요하다.

Q. Retry 요청은 어떻게 저장해?

A. 별도 요청으로 저장하되 parentRequestId로 원 요청과 연결한다.

Q. Usage Log에 Prompt 원문을 저장해도 돼?

A. 권장하지 않는다. 보안과 개인정보 위험이 있으므로 별도 정책이 필요하다.

---

## 2.3 Cost Calculation

### [개념]

Cost Calculation은 Token Usage와 모델별 단가를 기준으로 LLM API 비용을 계산하는 작업이다.

비용 계산은 API LLM, Embedding API, Reranking API, Tool API, Agent Workflow 전체 비용을 추적하는 데 필요하다.

Cost 구성:

- Input Token Cost
- Output Token Cost
- Embedding Token Cost
- Reranking Cost
- Tool API Cost
- Retry Cost
- Agent Step Cost
- Local Resource Cost

---

### [핵심]

- 모델마다 Token 단가가 다르다.
- Input Token과 Output Token 단가가 다를 수 있다.
- Output Token이 더 비싼 경우가 많다.
- Retry는 비용을 추가로 발생시킨다.
- Agent Workflow는 여러 LLM 호출 비용이 합산된다.
- RAG는 Retrieval 자체보다 LLM Context Token 비용이 커질 수 있다.
- Local LLM도 전기, 하드웨어, 성능 비용이 있다.

---

### [실무]

비용 계산 공식:

```text
inputCost = inputTokens * inputTokenUnitPrice
outputCost = outputTokens * outputTokenUnitPrice
totalCost = inputCost + outputCost + toolCost + retryCost
```

Cost Log 예:

```json
{
  "requestId": "req-001",
  "model": "model-name",
  "inputTokens": 3000,
  "outputTokens": 700,
  "inputCost": 0.003,
  "outputCost": 0.0021,
  "totalCost": 0.0051
}
```

Agent Workflow 비용 예:

```text
PM Agent Call
+ RAG Retrieval
+ Backend Agent Call
+ Review Agent Call
+ Retry
= Total Workflow Cost
```

비용 최적화 기준:

| 전략               | 효과                   |
| ------------------ | ---------------------- |
| Prompt Compression | Input Token 감소       |
| Top-K 제한         | Retrieved Context 감소 |
| Model Routing      | 고비용 모델 사용 감소  |
| Caching            | 반복 요청 비용 감소    |
| Retry 제한         | 중복 비용 감소         |
| Output Limit       | Output Token 감소      |
| Local LLM 사용     | 외부 API 비용 감소     |
| Batch Embedding    | 요청 효율 개선         |

주의:

- 가격 정보는 Provider별로 변경될 수 있으므로 설정값으로 관리한다.
- 비용 계산에 하드코딩 단가를 넣지 않는다.
- Usage가 누락되면 추정치임을 표시한다.
- Retry 비용을 누락하면 실제 비용보다 낮게 보인다.
- Local LLM은 API 비용은 없지만 시스템 자원을 사용한다.

---

### [FAQ]

Q. Cost Calculation이 뭐야?

A. Token 사용량과 모델별 단가를 기준으로 LLM API 비용을 계산하는 작업이다.

Q. LLM 비용은 무엇으로 결정돼?

A. Input Token, Output Token, 모델 단가, Retry, Tool API 호출, Agent 호출 횟수에 따라 결정된다.

Q. RAG에서 비용이 많이 드는 부분은?

A. Retrieved Context가 길어지면서 Input Token이 증가하는 부분이 크다.

Q. 비용 계산 단가는 코드에 하드코딩해도 돼?

A. 권장하지 않는다. Provider 가격은 바뀔 수 있으므로 설정값으로 관리해야 한다.

---

# 3. Latency Management

## 3.1 Latency

### [개념]

Latency는 사용자 요청부터 최종 응답까지 걸리는 시간이다.

LLM 시스템의 Latency는 일반 API보다 변동성이 크며 Prompt 길이, 모델 크기, Output 길이, Retrieval, Tool Call, Streaming 여부에 영향을 받는다.

Latency 구성:

- Network Latency
- Queue Wait Time
- Retrieval Latency
- Prompt Build Latency
- LLM First Token Latency
- LLM Generation Latency
- Tool Call Latency
- Validation Latency
- Total Response Latency

---

### [핵심]

- Latency는 사용자 경험에 직접 영향을 준다.
- Input Token이 많으면 처리 시간이 증가한다.
- Output Token이 많으면 생성 시간이 증가한다.
- 큰 모델은 보통 느리다.
- RAG는 Retrieval 시간이 추가된다.
- Tool Calling은 외부 API 지연을 추가한다.
- Streaming은 전체 시간이 아니라 체감 시간을 개선한다.
- Latency는 p50보다 p95, p99를 함께 봐야 한다.

---

### [실무]

Latency Breakdown 예:

```json
{
  "requestId": "req-001",
  "totalLatencyMs": 3200,
  "retrievalLatencyMs": 180,
  "promptBuildLatencyMs": 30,
  "firstTokenLatencyMs": 900,
  "generationLatencyMs": 1900,
  "validationLatencyMs": 80,
  "loggingLatencyMs": 10
}
```

Latency 개선 전략:

| 문제             | 개선                           |
| ---------------- | ------------------------------ |
| Retrieval 느림   | Index 최적화, Top-K 조정       |
| Prompt 길이 큼   | Context Filtering, Compression |
| 첫 Token 느림    | 모델 변경, Streaming           |
| Output 생성 느림 | Max Tokens 제한                |
| Tool Call 느림   | Timeout, Cache, 병렬화         |
| Agent Step 많음  | Workflow 단순화                |
| Queue 대기       | Worker 조정, Rate Limit 관리   |

Latency 측정 기준:

```text
request_start
→ retrieval_done
→ llm_request_sent
→ first_token_received
→ llm_response_done
→ validation_done
→ response_sent
```

주의:

- 평균 Latency만 보면 긴 꼬리 지연을 놓칠 수 있다.
- Streaming은 first token latency와 total latency를 모두 기록한다.
- Tool Calling Latency는 LLM Latency와 분리해서 봐야 한다.
- Local LLM은 모델 로딩 지연이 발생할 수 있다.
- Latency 최적화가 답변 품질을 해치지 않도록 한다.

---

### [FAQ]

Q. Latency가 뭐야?

A. 사용자 요청부터 최종 응답까지 걸리는 시간이다.

Q. LLM Latency는 왜 길어질 수 있어?

A. 긴 Prompt, 긴 Output, 큰 모델, RAG Retrieval, Tool Calling, Rate Limit, Local LLM 성능 때문이다.

Q. Streaming은 Latency를 줄여?

A. 전체 생성 시간을 줄이기보다 첫 응답을 빨리 보여줘 체감 Latency를 개선한다.

Q. Latency는 평균만 보면 돼?

A. 아니다. p50, p95, p99를 함께 봐야 긴 지연 문제를 찾을 수 있다.

---

## 3.2 First Token Latency

### [개념]

First Token Latency는 LLM API 요청을 보낸 뒤 첫 번째 Token 또는 Chunk를 받기까지 걸리는 시간이다.

Streaming UX에서는 First Token Latency가 사용자의 체감 속도를 결정한다.

First Token Latency 구성:

- Network Round Trip
- Queue Wait
- Prompt Processing
- Retrieval Preprocessing
- Model Scheduling
- Initial Generation

---

### [핵심]

- First Token Latency는 Streaming UX의 핵심 지표이다.
- Prompt가 길수록 첫 Token이 늦어질 수 있다.
- 모델이 클수록 첫 Token이 늦을 수 있다.
- Local LLM은 모델 로딩 상태에 따라 첫 Token이 크게 늦어질 수 있다.
- Queue 대기가 있으면 첫 Token Latency가 증가한다.
- Retrieval이 끝난 후 LLM 호출을 시작해야 하므로 RAG는 전처리 지연이 추가된다.

---

### [실무]

First Token Latency 측정 Flow:

```text
Request Sent
→ Stream Opened
→ First Chunk Received
→ Record firstTokenLatencyMs
```

개선 전략:

| 문제                   | 개선                         |
| ---------------------- | ---------------------------- |
| Prompt 길이 큼         | Prompt Compression           |
| RAG 검색 느림          | Retrieval 최적화             |
| 모델 큼                | Model Routing                |
| Queue 대기             | Queue 우선순위               |
| Local Model Cold Start | 모델 사전 로딩               |
| Streaming Buffering    | Proxy Buffering 비활성화     |
| Network 지연           | 가까운 Region 또는 Local LLM |

First Token Log 예:

```json
{
  "requestId": "req-stream-001",
  "model": "qwen2.5:14b",
  "firstTokenLatencyMs": 1250,
  "totalLatencyMs": 6200,
  "streaming": true
}
```

주의:

- First Token이 빨라도 전체 응답이 느릴 수 있다.
- Proxy가 Buffering하면 Streaming이 한 번에 도착할 수 있다.
- RAG에서는 Retrieval 단계가 First Token 이전에 완료되어야 한다.
- Local LLM은 첫 요청에서 모델 로딩 시간이 포함될 수 있다.
- First Token Latency와 Total Latency를 분리해서 기록한다.

---

### [FAQ]

Q. First Token Latency가 뭐야?

A. LLM API 요청 후 첫 번째 Token 또는 Chunk를 받기까지 걸리는 시간이다.

Q. First Token Latency는 왜 중요해?

A. Streaming UI에서 사용자가 응답이 시작됐다고 느끼는 속도를 결정하기 때문이다.

Q. First Token Latency를 줄이려면?

A. Prompt를 줄이고, Retrieval을 최적화하고, 모델 라우팅과 Streaming 설정을 점검한다.

Q. Local LLM에서 첫 Token이 늦는 이유는?

A. 모델 로딩, 하드웨어 성능, Context 길이, Queue 대기 영향 때문이다.

---

## 3.3 Latency Optimization

### [개념]

Latency Optimization은 LLM 시스템의 응답 시간을 줄이기 위해 Prompt, Retrieval, Model, Tool, Streaming, Cache, Queue를 조정하는 작업이다.

Latency Optimization은 비용과 품질을 함께 고려해야 한다.

---

### [핵심]

- Latency 최적화는 Token 최적화와 연결된다.
- Prompt가 짧아지면 처리 시간이 줄 수 있다.
- Output 길이를 제한하면 생성 시간이 줄어든다.
- 작은 모델은 빠르지만 품질이 낮을 수 있다.
- Cache는 반복 요청에 효과적이다.
- Streaming은 체감 속도 개선에 효과적이다.
- Tool Call 병렬화는 가능하지만 안전성과 Rate Limit을 고려해야 한다.
- RAG Retrieval 최적화는 전체 응답 시간에 중요하다.

---

### [실무]

Latency Optimization Checklist:

```text
Prompt가 불필요하게 길지 않은가?
Retrieved Context가 과도하지 않은가?
Top-K가 너무 높지 않은가?
Output Max Tokens가 적절한가?
작업 난이도에 맞는 모델인가?
반복 요청 Cache가 가능한가?
Streaming이 필요한 UX인가?
Tool Call Timeout이 있는가?
Agent Step이 과도하지 않은가?
```

최적화 전략:

| 전략                 | 효과               | 주의           |
| -------------------- | ------------------ | -------------- |
| Prompt Compression   | Input 처리 감소    | 정보 손실 주의 |
| Context Filtering    | RAG 비용/속도 개선 | 근거 누락 주의 |
| Model Routing        | 빠른 모델 활용     | 품질 차이      |
| Output Limit         | 생성 시간 감소     | 답변 부족      |
| Streaming            | 체감 속도 개선     | 검증 필요      |
| Cache                | 반복 요청 빠름     | 최신성         |
| Parallel Retrieval   | 검색 속도 개선     | 복잡도 증가    |
| Agent Step Reduction | 전체 시간 감소     | 검증 약화 주의 |

Latency 최적화 Flow:

```text
Measure
→ Identify Bottleneck
→ Optimize One Factor
→ Compare Metrics
→ Validate Quality
→ Rollout
```

주의:

- Latency만 줄이다가 답변 품질을 잃으면 안 된다.
- RAG Context를 너무 줄이면 Hallucination이 증가할 수 있다.
- 작은 모델로 라우팅할 때 품질 기준을 둔다.
- Cache된 답변은 최신성 검증이 필요하다.
- 최적화 전후 Metrics를 비교한다.

---

### [FAQ]

Q. Latency Optimization이 뭐야?

A. LLM 시스템 응답 시간을 줄이기 위해 Prompt, Retrieval, Model, Tool, Streaming, Cache를 조정하는 작업이다.

Q. Latency를 줄이는 가장 기본 방법은?

A. 불필요한 Context를 줄이고, Output 길이를 제한하고, 작업에 맞는 모델을 선택하는 것이다.

Q. 작은 모델을 쓰면 항상 좋아?

A. 속도는 좋아질 수 있지만 품질이 낮아질 수 있으므로 작업 유형별 기준이 필요하다.

Q. Latency 최적화에서 주의할 점은?

A. 속도만 줄이다가 근거 부족, 품질 저하, 검증 누락이 발생하지 않도록 해야 한다.

---

# 4. Testing Strategy

## 4.1 LLM Integration Test

### [개념]

LLM Integration Test는 Application이 LLM API와 정상적으로 연동되는지 검증하는 테스트이다.

LLM Integration Test는 HTTP Client, Request Body, Response Parsing, Timeout, Error Mapping, Validation을 포함한다.

테스트 대상:

- API Key Loading
- Request Body Build
- HTTP Client Call
- Response Parsing
- Finish Reason Handling
- Error Mapping
- Timeout Handling
- Retry Policy
- JSON Output Validation
- Usage Logging

---

### [핵심]

- LLM Output 전체 문자열을 exact match로 테스트하지 않는다.
- 구조, 상태, 필수 필드, 오류 처리 기준을 테스트한다.
- 외부 API 호출 테스트와 Mock 테스트를 분리한다.
- 비용이 발생하는 테스트는 제한한다.
- Timeout과 Error Response를 Mock으로 재현한다.
- Provider Adapter별 테스트가 필요하다.
- Local LLM과 API LLM 테스트 기준을 분리한다.

---

### [실무]

테스트 분류:

| 테스트                | 목적                              |
| --------------------- | --------------------------------- |
| Unit Test             | Prompt Builder, Parser, Validator |
| Mock Integration Test | HTTP 응답 파싱, Error Mapping     |
| Live API Test         | 실제 Provider 연결 확인           |
| Contract Test         | Request/Response Schema 검증      |
| RAG Test              | Retrieval 품질 확인               |
| Agent Test            | Step, Tool, State 검증            |
| Regression Test       | Prompt 변경 영향 확인             |

Response Parser 테스트 예:

```python
def test_extract_content_success():
    data = {
        "choices": [
            {
                "message": {
                    "content": "hello"
                },
                "finish_reason": "stop"
            }
        ]
    }

    assert extract_content(data) == "hello"
```

Invalid Response 테스트 예:

```python
def test_extract_content_empty_choices():
    data = {
        "choices": []
    }

    with pytest.raises(ValueError):
        extract_content(data)
```

주의:

- 실제 LLM 응답은 비결정적이므로 문장 전체 일치 테스트를 피한다.
- Live API Test는 CI에서 기본 비활성화하거나 제한한다.
- 테스트 API Key와 운영 API Key를 분리한다.
- 테스트 로그에 Secret을 남기지 않는다.
- Provider 장애로 테스트가 흔들리지 않게 Mock을 사용한다.

---

### [FAQ]

Q. LLM Integration Test가 뭐야?

A. Application이 LLM API와 정상적으로 연동되는지 검증하는 테스트다.

Q. LLM 응답 전체를 exact match로 테스트해도 돼?

A. 권장하지 않는다. LLM 출력은 변동 가능하므로 구조, 필수 필드, 상태를 검증하는 것이 좋다.

Q. Live API Test는 항상 실행해도 돼?

A. 비용과 Provider 상태 영향을 받으므로 제한적으로 실행하는 것이 좋다.

Q. 무엇을 Unit Test로 분리해야 해?

A. Prompt Builder, Response Parser, Schema Validator, Error Mapper, Token Estimator를 분리해 테스트한다.

---

## 4.2 Prompt Test

### [개념]

Prompt Test는 Prompt Template이 의도한 출력 형식, 제약 조건, 역할, RAG Grounding, JSON Schema 요구사항을 잘 반영하는지 검증하는 테스트이다.

Prompt 변경은 LLM 출력 품질에 큰 영향을 주므로 버전 관리와 회귀 테스트가 필요하다.

---

### [핵심]

- Prompt Template은 버전 관리한다.
- Prompt 변경 전후 결과를 비교한다.
- JSON Output Prompt는 Schema Validation으로 검증한다.
- RAG Prompt는 문서 근거 밖으로 답하지 않는지 확인한다.
- Agent Prompt는 status, nextAction, issues 같은 필수 필드를 확인한다.
- Prompt Injection 방어 규칙을 테스트한다.
- Prompt Test는 자동 평가와 수동 검토를 함께 사용할 수 있다.

---

### [실무]

Prompt Test Case 예:

```json
{
  "testName": "rag_missing_information",
  "input": "문서에 없는 Provider 가격을 알려줘",
  "expected": {
    "status": "missing_information",
    "mustContain": "문서에서 확인되지 않습니다"
  }
}
```

Prompt Regression 기준:

| 테스트         | 검증                     |
| -------------- | ------------------------ |
| Output Format  | Markdown / JSON 형식     |
| Required Field | 필수 필드 존재           |
| Missing Rule   | 문서에 없으면 추측 금지  |
| Safety Rule    | 위험 작업 차단           |
| Tool Rule      | Tool Arguments 생성 기준 |
| Language Rule  | 한국어 답변              |
| Length Rule    | 과도한 장문 방지         |
| Role Rule      | Agent 역할 유지          |

Prompt Version 예:

```text
promptName: rag_answer_prompt
version: 2026-06-30-v1
owner: AI Agent
purpose: Grounded RAG answer generation
```

주의:

- Prompt를 수정하면 관련 테스트를 함께 갱신한다.
- Prompt에 모든 규칙을 과도하게 넣으면 Token 비용이 증가한다.
- Prompt Test 결과는 모델 버전에 따라 달라질 수 있다.
- 문서 기반 답변은 Retrieval Context도 함께 테스트한다.
- Prompt Injection 테스트를 누락하지 않는다.

---

### [FAQ]

Q. Prompt Test가 뭐야?

A. Prompt Template이 원하는 출력 형식, 규칙, 제약, 역할을 제대로 반영하는지 검증하는 테스트다.

Q. Prompt도 버전 관리해야 해?

A. 그렇다. Prompt 변경은 출력 품질에 직접 영향을 주므로 버전 관리가 필요하다.

Q. Prompt Test에서 exact match를 써도 돼?

A. 일반 자연어 답변에는 권장하지 않는다. 필수 문구, 구조, Schema, 상태값 중심으로 검증한다.

Q. RAG Prompt Test에서 중요한 것은?

A. 문서에 없는 내용을 추측하지 않고 Missing Information으로 처리하는지 확인하는 것이다.

---

## 4.3 RAG Evaluation

### [개념]

RAG Evaluation은 RAG 시스템이 사용자 질문에 대해 올바른 문서를 검색하고, 검색된 Context에 근거해 정확한 답변을 생성하는지 평가하는 과정이다.

RAG Evaluation은 Retrieval 품질과 Generation 품질을 분리해서 본다.

평가 대상:

- Query Rewrite
- Retrieval Hit
- Top-K Precision
- Context Relevance
- Answer Groundedness
- Missing Information Handling
- Citation Accuracy
- Hallucination Rate

---

### [핵심]

- RAG 평가는 검색과 답변을 분리한다.
- Retrieval이 실패하면 Generation이 좋아도 답변 품질이 낮다.
- 답변이 좋아 보여도 문서 근거가 없으면 실패이다.
- 문서에 없는 질문은 Missing Information으로 답해야 한다.
- FAQ와 Retrieval Queries는 검색 적중률을 높인다.
- Evaluation Set을 만들어 반복 평가한다.
- Domain별 평가 기준이 필요하다.

---

### [실무]

RAG Evaluation Dataset 예:

```json
{
  "question": "Embedding Model과 Chat Model 차이는?",
  "expectedDocuments": [
    "LLM_Core_API_Integration_Part07_Embedding_API_RAG_Integration.md"
  ],
  "expectedSections": ["Embedding"],
  "expectedAnswerKeywords": [
    "Embedding Model",
    "검색용 Vector",
    "Chat Model",
    "답변 생성"
  ]
}
```

RAG 평가 지표:

| 지표               | 설명                           |
| ------------------ | ------------------------------ |
| Retrieval Hit Rate | 정답 문서 검색 여부            |
| Precision@K        | Top-K 결과 중 관련 Chunk 비율  |
| Recall@K           | 필요한 Chunk를 찾은 비율       |
| MRR                | 정답 Chunk 순위                |
| Context Relevance  | Context와 질문 관련성          |
| Groundedness       | 답변이 Context에 근거하는 정도 |
| Faithfulness       | 문서 왜곡 없이 답했는가        |
| Missing Accuracy   | 문서에 없는 질문을 거절했는가  |

Evaluation Flow:

```text
Prepare Test Questions
→ Run Retrieval
→ Check Expected Documents
→ Generate Answer
→ Validate Groundedness
→ Record Score
→ Improve Chunk / Query / Prompt
```

주의:

- LLM 답변만 보고 RAG 품질을 판단하지 않는다.
- Retrieval 결과를 별도로 저장하고 분석한다.
- Evaluation Set에는 문서에 없는 질문도 포함한다.
- Chunk 수정 후 Embedding 재생성이 필요할 수 있다.
- Domain Rules와 Master Rules를 평가 기준에 포함한다.

---

### [FAQ]

Q. RAG Evaluation이 뭐야?

A. RAG가 올바른 문서를 검색하고 문서 근거에 맞는 답변을 생성하는지 평가하는 과정이다.

Q. RAG 평가는 무엇을 나눠서 봐야 해?

A. Retrieval 품질과 Answer Generation 품질을 분리해서 봐야 한다.

Q. 답변이 좋아 보이면 성공이야?

A. 아니다. Retrieved Context에 근거하지 않으면 RAG 답변으로는 실패다.

Q. Evaluation Set에는 어떤 질문을 넣어야 해?

A. 정답 문서가 있는 질문, 실무 질문, 코드 질문, 문서에 없는 질문을 포함해야 한다.

---

## 4.4 Agent Evaluation

### [개념]

Agent Evaluation은 Agent가 역할에 맞게 작업을 수행하고, Tool을 안전하게 사용하며, Output Schema와 Workflow 규칙을 지키는지 평가하는 과정이다.

Agent Evaluation은 단일 LLM 답변 평가보다 Tool Use, State Transition, Error Recovery, Loop Control까지 포함한다.

평가 대상:

- Agent Role Compliance
- Output Schema
- Tool Selection
- Argument Validation
- Tool Result Handling
- State Transition
- Error Recovery
- Stop Condition
- Final Output Quality
- Safety Rule

---

### [핵심]

- Agent는 역할별로 평가 기준이 다르다.
- PM Agent는 요구사항 분해 품질을 본다.
- Backend Agent는 코드 생성과 규칙 준수를 본다.
- Review Agent는 오류 탐지와 검증 품질을 본다.
- Tool Calling Agent는 Tool 선택과 인자 검증을 본다.
- Agent Loop는 Max Step과 Stop Condition을 지켜야 한다.
- Agent Output은 Schema Validation을 통과해야 한다.

---

### [실무]

Agent Evaluation Case 예:

```json
{
  "agent": "ReviewAgent",
  "task": "Validate LLM API client error handling",
  "input": {
    "codeSummary": "Client has no timeout and no finish_reason check."
  },
  "expected": {
    "mustDetect": [
      "timeout missing",
      "finish_reason missing",
      "empty response handling missing"
    ],
    "status": "needs_fix"
  }
}
```

Agent 평가 지표:

| 지표              | 설명                     |
| ----------------- | ------------------------ |
| Task Success      | 작업 목표 달성           |
| Schema Validity   | Output Schema 준수       |
| Tool Accuracy     | 올바른 Tool 선택         |
| Argument Validity | Tool Arguments 검증 가능 |
| Safety Compliance | 위험 작업 차단           |
| State Correctness | 상태 전이 정확성         |
| Loop Control      | 무한 반복 방지           |
| Error Recovery    | 오류 복구 적절성         |
| Review Accuracy   | 문제 탐지 정확도         |

Agent Workflow 평가 Flow:

```text
Prepare Scenario
→ Run Agent
→ Capture Steps
→ Validate Tool Calls
→ Validate State
→ Validate Output
→ Score Result
```

주의:

- Agent가 결과를 맞혀도 위험 Tool을 잘못 사용하면 실패이다.
- Tool Arguments가 Schema에 맞지 않으면 실패이다.
- Agent가 무한 Loop에 빠지면 실패이다.
- Review Agent는 실제 문제 근거를 제시해야 한다.
- Final Output만 보지 말고 중간 Step도 평가한다.

---

### [FAQ]

Q. Agent Evaluation이 뭐야?

A. Agent가 역할, Tool 사용, 상태 전이, 출력 형식, 안전 규칙을 지키는지 평가하는 과정이다.

Q. Agent 평가는 일반 LLM 답변 평가와 뭐가 달라?

A. Tool Call, State, Error Recovery, Loop Control, Schema Validation까지 평가한다.

Q. Agent Output에서 가장 중요한 검증은?

A. Schema Validity, status 값, nextAction, Tool Arguments, Safety Rule 준수다.

Q. Agent가 답은 맞았지만 위험 Tool을 실행했다면?

A. 실패로 봐야 한다. Agent는 결과뿐 아니라 안전한 과정도 중요하다.

---

# 5. Cost Optimization

## 5.1 Token Optimization

### [개념]

Token Optimization은 LLM API 호출에서 불필요한 Input Token과 Output Token을 줄여 비용과 Latency를 개선하는 작업이다.

Token Optimization은 Prompt, Conversation History, Retrieved Context, Tool Result, Output Length를 대상으로 한다.

---

### [핵심]

- Input Token과 Output Token은 모두 비용과 Latency에 영향을 준다.
- System Prompt는 짧고 명확하게 유지한다.
- Conversation History는 요약한다.
- Retrieved Context는 관련 Chunk만 포함한다.
- Tool Result는 필요한 필드만 전달한다.
- Output Format을 명확히 지정해 불필요한 장문을 줄인다.
- Max Tokens를 작업별로 제한한다.

---

### [실무]

Token Optimization Flow:

```text
Measure Token Usage
→ Identify Large Token Source
→ Compress Prompt
→ Filter Context
→ Limit Output
→ Validate Quality
```

최적화 대상:

| 대상                 | 최적화             |
| -------------------- | ------------------ |
| System Prompt        | 핵심 규칙만 유지   |
| User Prompt          | 작업 범위 명확화   |
| Conversation History | Summary 사용       |
| Retrieved Context    | Top-K, Reranking   |
| Tool Result          | Field Selection    |
| Agent State          | Structured Summary |
| Output               | 형식과 길이 제한   |
| Repeated Query       | Cache 사용         |

Token 절감 예:

```text
Before:
긴 대화 전체 + 검색 Chunk 20개 + 긴 출력 요구

After:
Conversation Summary + Reranked Chunk 5개 + Output Schema
```

주의:

- Token을 줄이면서 필수 근거를 제거하면 안 된다.
- RAG Context를 과도하게 줄이면 Hallucination이 증가할 수 있다.
- Prompt 압축 후 Regression Test를 수행한다.
- Output을 너무 짧게 제한하면 답변 품질이 낮아진다.
- 비용 최적화는 품질 평가와 함께 진행한다.

---

### [FAQ]

Q. Token Optimization이 뭐야?

A. 불필요한 입력과 출력 Token을 줄여 비용과 Latency를 개선하는 작업이다.

Q. Token을 줄이는 가장 기본 방법은?

A. Conversation History를 요약하고, Retrieved Context를 선별하고, Output 길이를 제한하는 것이다.

Q. RAG Context를 줄이면 항상 좋아?

A. 아니다. 필요한 근거까지 제거하면 답변 품질이 떨어질 수 있다.

Q. Token Optimization 후 무엇을 확인해야 해?

A. 답변 품질, RAG Groundedness, Schema Validity, 사용자 요구 충족 여부를 확인해야 한다.

---

## 5.2 Model Routing

### [개념]

Model Routing은 작업 유형, 난이도, 비용, Latency, 품질 요구에 따라 적절한 LLM 모델을 선택하는 전략이다.

모든 작업에 가장 크고 비싼 모델을 사용하는 것은 비효율적이다.

Model Routing 기준:

- Task Type
- Complexity
- Required Accuracy
- Context Length
- Output Type
- Tool Support
- Latency Requirement
- Cost Budget
- Privacy Requirement
- Local vs API

---

### [핵심]

- 단순 작업은 작은 모델로 처리할 수 있다.
- 복잡한 코드 리뷰는 강한 모델이 필요하다.
- RAG 답변은 문서 근거 품질이 중요하다.
- Tool Calling은 Tool Support 모델이 필요하다.
- Embedding은 Embedding Model을 사용한다.
- Vision 입력은 Vision Model이 필요하다.
- Local LLM과 API LLM을 목적에 따라 분리한다.
- Model Routing 결과는 Metrics로 평가한다.

---

### [실무]

Model Routing 예:

```text
Simple FAQ
→ Small Chat Model

RAG Answer
→ Chat Model + Retrieved Context

Code Generation
→ Code Model or Reasoning Model

Embedding Search
→ Embedding Model

Image Input
→ Vision Model

Private Local Task
→ Local LLM

High Accuracy Review
→ Strong Reasoning Model
```

개인 AI 서버 예:

```text
Qwen2.5 14B
→ Chat / Code Generation

BGE-M3
→ Embedding / Semantic Search

Qwen2.5-VL 7B
→ Vision / Image Input

Ollama
→ Local Runtime

AnythingLLM
→ RAG Workspace
```

Routing Policy 예:

```json
{
  "taskType": "code_review",
  "complexity": "high",
  "requiresToolCalling": false,
  "requiresPrivacy": true,
  "selectedModel": "local-code-model"
}
```

주의:

- 작은 모델로 품질이 부족한 작업을 처리하지 않는다.
- 큰 모델을 남용하면 비용과 Latency가 증가한다.
- Routing 실패율을 관측해야 한다.
- 모델별 Context Window와 Tool Support를 확인한다.
- Local LLM은 하드웨어 한계를 고려한다.

---

### [FAQ]

Q. Model Routing이 뭐야?

A. 작업 유형과 요구사항에 따라 적절한 LLM 모델을 선택하는 전략이다.

Q. 모든 작업에 가장 좋은 모델을 쓰면 안 돼?

A. 비용과 Latency가 증가하므로 단순 작업은 작은 모델이나 Local LLM으로 처리하는 것이 효율적이다.

Q. Embedding 작업에는 어떤 모델을 써?

A. Chat Model이 아니라 Embedding Model을 사용해야 한다.

Q. Model Routing 품질은 어떻게 확인해?

A. 작업 성공률, Latency, 비용, Validation Failure, 사용자 피드백을 기준으로 평가한다.

---

## 5.3 Cache Strategy

### [개념]

Cache Strategy는 반복되는 LLM 요청, Embedding 결과, Retrieval 결과, Tool Result를 재사용해 비용과 Latency를 줄이는 전략이다.

Cache는 동일하거나 유사한 요청이 반복될 때 효과적이다.

Cache 대상:

- Embedding Vector
- RAG Retrieval Result
- Static FAQ Answer
- Tool Result
- Model Capability Check
- Prompt Template
- Parsed Document Chunk
- Evaluation Result

---

### [핵심]

- Cache는 비용과 Latency를 줄인다.
- Embedding 결과는 문서가 변경되지 않으면 재사용 가능하다.
- Retrieval 결과는 Query와 문서 버전에 의존한다.
- LLM 답변 Cache는 최신성과 사용자 맥락을 주의해야 한다.
- Tool Result Cache는 데이터 변경 가능성을 고려한다.
- Cache Key 설계가 중요하다.
- Cache Invalidation 정책이 필요하다.

---

### [실무]

Cache Key 예:

```text
embedding:{model}:{documentVersion}:{chunkHash}
retrieval:{domain}:{queryHash}:{indexVersion}:topK:{topK}
llm_answer:{model}:{promptVersion}:{inputHash}
tool_result:{toolName}:{argumentHash}:{dataVersion}
```

Cache 적용 기준:

| 대상                 | Cache 적합성       |
| -------------------- | ------------------ |
| Embedding Vector     | 높음               |
| Static RAG Chunk     | 높음               |
| Retrieval Result     | 중간~높음          |
| FAQ Answer           | 중간               |
| User-specific Answer | 낮음~중간          |
| 최신 정보            | 낮음               |
| Tool Result          | 데이터 성격에 따라 |
| Agent Final Output   | 주의               |

Invalidation 기준:

| 변경                 | Cache 무효화                |
| -------------------- | --------------------------- |
| 문서 내용 변경       | Embedding / Retrieval Cache |
| Embedding Model 변경 | Embedding Cache             |
| Prompt Template 변경 | LLM Answer Cache            |
| User Context 변경    | User-specific Cache         |
| Tool Data 변경       | Tool Result Cache           |
| Index Version 변경   | Retrieval Cache             |

주의:

- Cache된 답변이 오래된 정보를 제공할 수 있다.
- 사용자별 정보가 섞이지 않게 Cache Key를 분리한다.
- RAG 문서 변경 후 Retrieval Cache를 무효화한다.
- LLM 답변 Cache는 품질 검증 후 사용한다.
- Cache Hit Rate와 Stale Response Rate를 관측한다.

---

### [FAQ]

Q. Cache Strategy가 뭐야?

A. 반복되는 LLM 요청, Embedding, Retrieval, Tool Result를 재사용해 비용과 Latency를 줄이는 전략이다.

Q. 무엇을 Cache하기 좋아?

A. Embedding Vector, 정적 문서 Chunk, Retrieval Result, 반복 FAQ, Tool Result가 적합하다.

Q. Cache에서 가장 중요한 것은?

A. Cache Key 설계와 Invalidation 정책이다.

Q. RAG 문서가 바뀌면 Cache는 어떻게 해?

A. Embedding Cache, Retrieval Cache, 관련 Answer Cache를 무효화해야 한다.

---

# 6. Production Checklist

## 6.1 LLM API Production Checklist

### [개념]

LLM API Production Checklist는 LLM API를 실제 서비스 또는 개인 AI 서버 운영 환경에 적용하기 전 확인해야 할 항목이다.

Checklist는 보안, 안정성, 비용, 품질, 관측성, 테스트를 포함한다.

---

### [핵심]

운영 전 필수 확인:

- API Key Secret 관리
- Environment Variable 검증
- HTTP Client 계층 분리
- Timeout 설정
- Retry / Backoff 설정
- Rate Limit 대응
- Response Validation
- JSON Schema Validation
- Finish Reason Check
- Error Mapping
- Usage Logging
- Latency Metrics
- Cost Tracking
- Prompt Versioning
- RAG Evaluation
- Tool Argument Validation
- Agent Loop Control
- Secret Redaction
- Test Coverage

---

### [실무]

Production Checklist:

```text
[Security]
API Key는 Secret Manager 또는 환경변수로 관리하는가?
Frontend에 API Key가 노출되지 않는가?
Authorization Header가 로그에서 제거되는가?
Tool Arguments에서 Secret을 차단하는가?

[Stability]
HTTP Timeout이 있는가?
Retry 가능한 오류와 금지 오류가 구분되는가?
Rate Limit 대응이 있는가?
Provider Error를 표준 Error로 변환하는가?

[Validation]
Empty Response를 검증하는가?
finish_reason=length를 처리하는가?
JSON Output을 Schema Validation하는가?
RAG 답변을 Retrieved Context와 검증하는가?

[Cost]
Token Usage를 기록하는가?
모델별 비용 계산이 가능한가?
Retry 비용을 추적하는가?
Usage Limit이 있는가?

[Latency]
Latency p95를 추적하는가?
First Token Latency를 추적하는가?
Streaming Timeout이 있는가?
Tool Latency를 분리해서 보는가?

[RAG]
Chunk Metadata가 충분한가?
Retrieval Queries가 있는가?
Top-K와 Reranking 기준이 있는가?
Missing Information Rule이 있는가?

[Agent]
Agent Output Schema가 있는가?
Tool Arguments를 실행 전 검증하는가?
Max Step / Max Tool Calls가 있는가?
Error State와 Fallback Strategy가 있는가?
```

주의:

- Checklist는 한 번 작성하고 끝내는 문서가 아니다.
- 모델, Provider, Prompt, RAG 문서 변경 시 다시 확인한다.
- 운영 로그에 민감정보가 없는지 주기적으로 점검한다.
- 비용과 Latency는 실제 사용량 기반으로 조정한다.
- Agent 기능이 늘어나면 Tool 안전성 검토를 다시 수행한다.

---

### [FAQ]

Q. LLM API Production Checklist가 뭐야?

A. LLM API를 운영 환경에 적용하기 전 보안, 안정성, 비용, 품질, 테스트를 확인하는 목록이다.

Q. 운영 전 가장 중요한 항목은?

A. API Key 보안, Timeout, Error Handling, Response Validation, Usage Logging이다.

Q. Agent 운영 전에는 무엇을 확인해야 해?

A. Tool Argument Validation, Permission Check, Safety Check, Max Step, Error State, Output Schema를 확인해야 한다.

Q. RAG 운영 전에는 무엇을 확인해야 해?

A. Chunk 품질, Metadata, Retrieval Queries, Missing Information Rule, RAG Answer Validation을 확인해야 한다.

---

## 6.2 Common Mistakes

### [개념]

Common Mistakes는 LLM API Observability, Testing, Cost, Latency 운영에서 자주 발생하는 설계 오류이다.

---

### [핵심]

자주 발생하는 실수:

- Token Usage를 기록하지 않음
- Latency를 평균만 확인
- p95 / p99 Latency를 보지 않음
- Prompt 변경 이력을 관리하지 않음
- LLM Output을 exact match로 테스트
- RAG 검색 결과를 평가하지 않음
- 답변만 보고 Retrieval 품질을 판단
- Agent 중간 Step을 기록하지 않음
- Tool Call 실패율을 보지 않음
- Cost Calculation을 하지 않음
- Retry 비용을 누락
- Cache Invalidation 없이 Cache 사용
- Metrics Label에 개인정보를 넣음
- Prompt 전문을 무분별하게 로그로 저장
- API Key와 Authorization Header를 로그에 남김
- Latency 최적화 중 RAG 근거를 과도하게 제거
- 작은 모델로 모든 작업을 처리
- 큰 모델로 모든 작업을 처리

---

### [실무]

문제 진단 Flow:

```text
LLM System Quality Problem
→ Check Trace
→ Check Token Usage
→ Check Latency Breakdown
→ Check Retrieval Logs
→ Check Validation Logs
→ Check Tool Logs
→ Check Cost Logs
→ Check User Feedback
```

해결 기준:

| 문제          | 해결                                   |
| ------------- | -------------------------------------- |
| 비용 증가     | Token Usage, Retry, Model Routing 확인 |
| Latency 증가  | Breakdown, Context, Tool Latency 확인  |
| RAG 오답      | Retrieval Hit, Groundedness 평가       |
| JSON 실패     | Prompt Test, Schema 단순화             |
| Agent 불안정  | Step Trace, Tool Validation 확인       |
| Cache 오답    | Invalidation 정책 확인                 |
| 테스트 불안정 | exact match 제거, 구조 검증            |
| 보안 위험     | Redaction, Secret Scan                 |

검수 Checklist:

```text
Token Usage Logging이 있는가?
Cost Calculation이 가능한가?
Latency Breakdown이 있는가?
First Token Latency를 기록하는가?
Prompt Versioning이 있는가?
Prompt Test가 있는가?
RAG Evaluation Set이 있는가?
Agent Evaluation Case가 있는가?
Tool Call Trace가 있는가?
Response Validation 로그가 있는가?
Cache Invalidation 정책이 있는가?
Secret Redaction이 적용되는가?
Metrics Label에 개인정보가 없는가?
```

---

### [FAQ]

Q. Observability에서 가장 흔한 실수는?

A. Token Usage, Latency Breakdown, Retrieval Log, Tool Trace를 남기지 않는 것이다.

Q. Testing에서 가장 흔한 실수는?

A. 비결정적인 LLM 자연어 응답을 exact match로 테스트하는 것이다.

Q. Cost 관리에서 가장 흔한 실수는?

A. Retry 비용과 Agent 단계별 비용을 누락하는 것이다.

Q. Latency 관리에서 가장 흔한 실수는?

A. 평균 Latency만 보고 p95, p99, First Token Latency를 보지 않는 것이다.

Q. RAG 품질 평가에서 가장 흔한 실수는?

A. 최종 답변만 보고 검색된 Context가 맞는지 확인하지 않는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. AI Observability가 뭐야?
A. LLM 호출, RAG 검색, Tool 실행, Agent 단계, Token, Latency, Error, 품질을 관측하는 체계다.

Q. 일반 Observability와 AI Observability 차이는?
A. AI Observability는 Prompt, Token, Retrieval, Tool Call, Validation, Output 품질까지 추적한다.

Q. AI Observability가 왜 필요해?
A. LLM 답변 품질, 비용, 속도, 오류 원인을 분석하고 개선하기 위해 필요하다.

Q. Request Trace가 뭐야?
A. 사용자 요청이 Retrieval, LLM, Tool, Agent, Validation을 거쳐 최종 응답이 되는 전체 과정을 추적하는 기록이다.

Q. requestId는 왜 필요해?
A. 하나의 요청에서 발생한 로그, 오류, Token 사용량, Tool 호출을 연결하기 위해 필요하다.

Q. Metrics가 뭐야?
A. LLM 시스템의 요청 수, 오류율, Latency, Token 사용량, 비용, 품질 실패율을 숫자로 집계한 지표다.

Q. LLM 시스템에서 중요한 Metrics는?
A. Request Count, Error Rate, Latency, Token Usage, Cost, Retry, Rate Limit, Validation Failure, Retrieval Empty Rate다.

Q. Token Usage Logging이 뭐야?
A. LLM API 호출에서 사용된 Input Token, Output Token, Total Token을 기록하는 작업이다.

Q. Token Usage를 왜 기록해?
A. 비용 관리, Context 최적화, 사용자별 제한, 성능 분석에 필요하기 때문이다.

Q. Usage Log Schema가 뭐야?
A. LLM API 사용량을 일관된 형태로 저장하기 위한 데이터 구조다.

Q. 실패 요청도 Usage Log에 남겨야 해?
A. 그렇다. 실패해도 Token 비용이나 Latency가 발생할 수 있고 장애 분석에 필요하다.

Q. Cost Calculation이 뭐야?
A. Token 사용량과 모델별 단가를 기준으로 LLM API 비용을 계산하는 작업이다.

Q. LLM 비용은 무엇으로 결정돼?
A. Input Token, Output Token, 모델 단가, Retry, Tool API 호출, Agent 호출 횟수에 따라 결정된다.

Q. RAG에서 비용이 많이 드는 부분은?
A. Retrieved Context가 길어지면서 Input Token이 증가하는 부분이 크다.

Q. Latency가 뭐야?
A. 사용자 요청부터 최종 응답까지 걸리는 시간이다.

Q. LLM Latency는 왜 길어질 수 있어?
A. 긴 Prompt, 긴 Output, 큰 모델, RAG Retrieval, Tool Calling, Rate Limit, Local LLM 성능 때문이다.

Q. First Token Latency가 뭐야?
A. LLM API 요청 후 첫 번째 Token 또는 Chunk를 받기까지 걸리는 시간이다.

Q. First Token Latency는 왜 중요해?
A. Streaming UI에서 사용자가 응답이 시작됐다고 느끼는 속도를 결정하기 때문이다.

Q. Latency Optimization이 뭐야?
A. LLM 시스템 응답 시간을 줄이기 위해 Prompt, Retrieval, Model, Tool, Streaming, Cache를 조정하는 작업이다.

Q. Latency를 줄이는 가장 기본 방법은?
A. 불필요한 Context를 줄이고, Output 길이를 제한하고, 작업에 맞는 모델을 선택하는 것이다.

Q. LLM Integration Test가 뭐야?
A. Application이 LLM API와 정상적으로 연동되는지 검증하는 테스트다.

Q. LLM 응답 전체를 exact match로 테스트해도 돼?
A. 권장하지 않는다. LLM 출력은 변동 가능하므로 구조, 필수 필드, 상태를 검증하는 것이 좋다.

Q. Prompt Test가 뭐야?
A. Prompt Template이 원하는 출력 형식, 규칙, 제약, 역할을 제대로 반영하는지 검증하는 테스트다.

Q. Prompt도 버전 관리해야 해?
A. 그렇다. Prompt 변경은 출력 품질에 직접 영향을 주므로 버전 관리가 필요하다.

Q. RAG Evaluation이 뭐야?
A. RAG가 올바른 문서를 검색하고 문서 근거에 맞는 답변을 생성하는지 평가하는 과정이다.

Q. RAG 평가는 무엇을 나눠서 봐야 해?
A. Retrieval 품질과 Answer Generation 품질을 분리해서 봐야 한다.

Q. Agent Evaluation이 뭐야?
A. Agent가 역할, Tool 사용, 상태 전이, 출력 형식, 안전 규칙을 지키는지 평가하는 과정이다.

Q. Agent 평가는 일반 LLM 답변 평가와 뭐가 달라?
A. Tool Call, State, Error Recovery, Loop Control, Schema Validation까지 평가한다.

Q. Token Optimization이 뭐야?
A. 불필요한 입력과 출력 Token을 줄여 비용과 Latency를 개선하는 작업이다.

Q. Token을 줄이는 가장 기본 방법은?
A. Conversation History를 요약하고, Retrieved Context를 선별하고, Output 길이를 제한하는 것이다.

Q. Model Routing이 뭐야?
A. 작업 유형과 요구사항에 따라 적절한 LLM 모델을 선택하는 전략이다.

Q. 모든 작업에 가장 좋은 모델을 쓰면 안 돼?
A. 비용과 Latency가 증가하므로 단순 작업은 작은 모델이나 Local LLM으로 처리하는 것이 효율적이다.

Q. Cache Strategy가 뭐야?
A. 반복되는 LLM 요청, Embedding, Retrieval, Tool Result를 재사용해 비용과 Latency를 줄이는 전략이다.

Q. Cache에서 가장 중요한 것은?
A. Cache Key 설계와 Invalidation 정책이다.

Q. LLM API Production Checklist가 뭐야?
A. LLM API를 운영 환경에 적용하기 전 보안, 안정성, 비용, 품질, 테스트를 확인하는 목록이다.

Q. 운영 전 가장 중요한 항목은?
A. API Key 보안, Timeout, Error Handling, Response Validation, Usage Logging이다.

Q. Agent 운영 전에는 무엇을 확인해야 해?
A. Tool Argument Validation, Permission Check, Safety Check, Max Step, Error State, Output Schema를 확인해야 한다.

Q. RAG 운영 전에는 무엇을 확인해야 해?
A. Chunk 품질, Metadata, Retrieval Queries, Missing Information Rule, RAG Answer Validation을 확인해야 한다.

Q. Observability에서 가장 흔한 실수는?
A. Token Usage, Latency Breakdown, Retrieval Log, Tool Trace를 남기지 않는 것이다.

Q. Testing에서 가장 흔한 실수는?
A. 비결정적인 LLM 자연어 응답을 exact match로 테스트하는 것이다.

Q. Cost 관리에서 가장 흔한 실수는?
A. Retry 비용과 Agent 단계별 비용을 누락하는 것이다.

Q. Latency 관리에서 가장 흔한 실수는?
A. 평균 Latency만 보고 p95, p99, First Token Latency를 보지 않는 것이다.

Q. RAG 품질 평가에서 가장 흔한 실수는?
A. 최종 답변만 보고 검색된 Context가 맞는지 확인하지 않는 것이다.
