# LLM Core & API Integration Part09 - Error Handling, Retry & Rate Limit

---

# 1. LLM API Error Handling

## 1.1 Error Handling

### [개념]

Error Handling은 LLM API 호출, 응답 파싱, 출력 검증, Tool 실행, RAG 검색 과정에서 발생하는 오류를 분류하고 안전하게 처리하는 구조이다.

LLM API 연동에서 오류는 단순 HTTP 실패뿐 아니라 Empty Response, Invalid JSON, Truncated Output, Rate Limit, Timeout, Tool Failure, Hallucination까지 포함한다.

Error Handling 기본 Flow:

```text
Call LLM API
→ Check HTTP Status
→ Parse Response
→ Validate Output
→ Handle Error
→ Return Safe Result
```

---

### [핵심]

- LLM API 오류는 유형별로 분리한다.
- HTTP 200이어도 유효한 응답이 아닐 수 있다.
- Error Body와 Success Body 구조가 다를 수 있다.
- 사용자에게는 안전하고 이해 가능한 오류 메시지를 반환한다.
- 로그에는 분석 가능한 Metadata를 남긴다.
- Secret, API Key, 개인정보, Prompt 전문은 로그에서 제거한다.
- Retry 가능한 오류와 Retry 금지 오류를 구분한다.
- Agent Workflow에서는 오류 상태를 구조화해야 한다.

---

### [실무]

오류 분류 기준:

| 오류 유형            | 예                               |
| -------------------- | -------------------------------- |
| Authentication Error | 401 Unauthorized                 |
| Authorization Error  | 403 Forbidden                    |
| Validation Error     | 400 Bad Request                  |
| Rate Limit Error     | 429 Too Many Requests            |
| Timeout Error        | Connection Timeout, Read Timeout |
| Server Error         | 500, 502, 503, 504               |
| Network Error        | DNS, Connection Reset            |
| Empty Response       | choices 없음, content 없음       |
| Invalid Output       | Invalid JSON, Schema 불일치      |
| Truncated Output     | finish_reason=length             |
| Safety Error         | Content Filter, Policy Block     |
| Tool Error           | Tool Timeout, Permission Denied  |
| RAG Error            | Empty Retrieval, Low Confidence  |

Error Handling 구조:

```text
HTTP Client
→ Provider Adapter
→ Error Mapper
→ Retry Handler
→ Response Validator
→ Service Result
```

표준 Error Response 예:

```json
{
  "status": "failed",
  "errorCode": "llm_timeout",
  "message": "LLM API request timed out.",
  "retryable": true,
  "details": null
}
```

주의:

- 모든 오류를 같은 메시지로 처리하지 않는다.
- 인증 오류를 Retry로 해결하려 하지 않는다.
- Rate Limit 오류는 Backoff가 필요하다.
- Empty Response를 정상 답변으로 처리하지 않는다.
- Error Body를 사용자에게 그대로 노출하지 않는다.
- 내부 Stack Trace를 외부 응답에 포함하지 않는다.

---

### [FAQ]

Q. LLM API Error Handling이 뭐야?

A. LLM API 호출과 응답 처리 중 발생하는 오류를 분류하고 안전하게 처리하는 구조다.

Q. HTTP 200이면 성공으로 봐도 돼?

A. 아니다. HTTP 200이어도 content가 비어 있거나 JSON Schema가 틀리거나 출력이 잘렸을 수 있다.

Q. 오류를 왜 유형별로 나눠야 해?

A. Retry 가능 여부, 사용자 메시지, 로그, 복구 방식이 오류 유형마다 다르기 때문이다.

Q. Error Body를 그대로 사용자에게 보여줘도 돼?

A. 권장하지 않는다. 내부 정보나 민감정보가 포함될 수 있으므로 안전한 메시지로 변환해야 한다.

---

## 1.2 HTTP Status Error

### [개념]

HTTP Status Error는 LLM API Provider가 HTTP 상태 코드로 요청 결과를 반환하는 오류이다.

LLM API Client는 HTTP Status Code를 확인하고 오류 유형에 맞게 분기해야 한다.

대표 Status Code:

- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found
- 408 Request Timeout
- 409 Conflict
- 422 Unprocessable Entity
- 429 Too Many Requests
- 500 Internal Server Error
- 502 Bad Gateway
- 503 Service Unavailable
- 504 Gateway Timeout

---

### [핵심]

- 4xx는 대부분 Client 요청 문제이다.
- 401은 API Key 인증 실패이다.
- 403은 권한 부족 또는 정책 차단이다.
- 429는 Rate Limit 초과이다.
- 5xx는 Provider 또는 Gateway 문제일 수 있다.
- 429와 일부 5xx는 제한적 Retry 가능하다.
- 400, 401, 403은 일반적으로 Retry하지 않는다.

---

### [실무]

Status Code 처리 기준:

| Status | 의미            | Retry | 처리                  |
| ------ | --------------- | ----- | --------------------- |
| 400    | 잘못된 요청     | 금지  | Request Body 확인     |
| 401    | 인증 실패       | 금지  | API Key 확인          |
| 403    | 권한 없음       | 금지  | 권한/정책 확인        |
| 404    | Endpoint 없음   | 금지  | Base URL/Path 확인    |
| 408    | 요청 Timeout    | 가능  | 제한적 Retry          |
| 422    | 검증 실패       | 금지  | Schema 확인           |
| 429    | Rate Limit      | 가능  | Retry-After / Backoff |
| 500    | 서버 오류       | 가능  | 제한적 Retry          |
| 502    | Gateway 오류    | 가능  | 제한적 Retry          |
| 503    | 서비스 불가     | 가능  | 제한적 Retry          |
| 504    | Gateway Timeout | 가능  | 제한적 Retry          |

HTTP Error Mapping 예:

```json
{
  "httpStatus": 429,
  "errorCode": "rate_limit_exceeded",
  "retryable": true,
  "recommendedAction": "Apply exponential backoff and check Retry-After header."
}
```

Spring Error Mapping 예:

```java
.retrieve()
.onStatus(
    status -> status.value() == 429,
    response -> response.bodyToMono(String.class)
        .map(body -> new LlmRateLimitException("LLM rate limit exceeded"))
)
.onStatus(
    status -> status.is4xxClientError(),
    response -> response.bodyToMono(String.class)
        .map(body -> new LlmClientException("LLM client error"))
)
.onStatus(
    status -> status.is5xxServerError(),
    response -> response.bodyToMono(String.class)
        .map(body -> new LlmServerException("LLM server error"))
)
```

주의:

- Provider Error Body 구조는 다를 수 있다.
- 401 오류는 API Key Rotation, 환경변수 누락, Header 오류를 확인한다.
- 429는 즉시 반복 호출하면 상황이 악화된다.
- 5xx도 무제한 Retry하면 비용과 부하가 증가한다.
- Error Body를 로그에 남길 때 Secret Redaction을 적용한다.

---

### [FAQ]

Q. HTTP Status Error는 뭐야?

A. LLM API Provider가 HTTP 상태 코드로 요청 실패 원인을 알려주는 오류다.

Q. 401 Unauthorized는 어떻게 처리해?

A. API Key 누락, 잘못된 Key, Authorization Header, Secret Rotation 여부를 확인한다.

Q. 429 Rate Limit은 어떻게 처리해?

A. Retry-After를 확인하고 Exponential Backoff, Queue, Throttling을 적용한다.

Q. 500 계열 오류는 Retry해도 돼?

A. 제한적으로 가능하다. Max Retry와 Backoff를 적용해야 한다.

Q. 400 Bad Request는 Retry하면 돼?

A. 아니다. Request Body, Parameter, Provider 지원 필드를 수정해야 한다.

---

## 1.3 Provider Error Format

### [개념]

Provider Error Format은 LLM API Provider가 오류 응답을 표현하는 JSON 구조이다.

Provider마다 Error Body의 필드명, 코드, 메시지, 세부 정보가 다를 수 있다.

Provider Error Format 예:

```json
{
  "error": {
    "message": "Invalid API key",
    "type": "authentication_error",
    "code": "invalid_api_key"
  }
}
```

---

### [핵심]

- Provider마다 Error Format이 다르다.
- Error Body는 Success Response와 구조가 다르다.
- Error Code와 HTTP Status를 함께 봐야 한다.
- Provider Adapter에서 표준 Error로 변환하는 것이 좋다.
- Error Message는 사용자에게 그대로 노출하지 않는다.
- Error Body에 Request 정보나 민감정보가 포함될 수 있다.

---

### [실무]

표준 Error DTO 예:

```json
{
  "status": "failed",
  "provider": "openai-compatible",
  "httpStatus": 401,
  "errorCode": "authentication_failed",
  "message": "LLM API authentication failed.",
  "retryable": false
}
```

Provider Error Mapping Flow:

```text
Provider Error Body
→ Parse Provider Error
→ Map HTTP Status
→ Map Error Code
→ Determine Retryable
→ Redact Sensitive Fields
→ Return Standard Error
```

Mapping 기준:

| Provider Error          | Standard Error         |
| ----------------------- | ---------------------- |
| invalid_api_key         | authentication_failed  |
| insufficient_quota      | quota_exceeded         |
| rate_limit_exceeded     | rate_limit_exceeded    |
| context_length_exceeded | context_limit_exceeded |
| invalid_request_error   | invalid_request        |
| server_error            | provider_server_error  |
| model_not_found         | model_not_found        |

주의:

- Error Body 파싱 실패도 처리해야 한다.
- Provider Error Code가 없을 수 있다.
- HTTP Status와 Error Code가 불일치할 수 있다.
- Provider 메시지에 내부 정보가 포함될 수 있다.
- Standard Error는 Service와 Agent가 이해 가능한 형태여야 한다.

---

### [FAQ]

Q. Provider Error Format이 뭐야?

A. LLM API Provider가 오류 정보를 JSON으로 표현하는 구조다.

Q. Provider마다 Error Format이 달라?

A. 그렇다. 필드명, error code, message 구조가 다를 수 있다.

Q. Provider Error를 왜 표준 Error로 바꿔?

A. Service, Agent, UI가 Provider 차이와 무관하게 일관된 오류 처리를 하기 위해서다.

Q. Provider Error Message를 그대로 보여줘도 돼?

A. 권장하지 않는다. 내부 정보나 민감정보가 포함될 수 있으므로 안전한 메시지로 변환해야 한다.

---

# 2. Timeout Handling

## 2.1 Timeout

### [개념]

Timeout은 LLM API 요청이 일정 시간 안에 완료되지 않을 때 실패로 처리하는 기준이다.

Timeout은 무한 대기, Thread 점유, Connection 고갈, 사용자 경험 저하를 막기 위해 필수이다.

Timeout 종류:

- Connection Timeout
- Read Timeout
- Write Timeout
- Pool Timeout
- Total Timeout
- Streaming Timeout
- Tool Timeout

---

### [핵심]

- Timeout 없는 HTTP 요청은 금지한다.
- LLM 응답은 길 수 있으므로 작업 유형별 Timeout이 필요하다.
- Streaming은 일반 요청과 Timeout 기준이 다르다.
- Timeout 발생 시 사용자에게 명확한 실패 응답을 반환한다.
- Timeout은 Retry 정책과 함께 설계한다.
- Timeout이 너무 짧으면 정상 응답도 실패한다.
- Timeout이 너무 길면 자원이 오래 점유된다.

---

### [실무]

Timeout Flow:

```text
API Request
→ Wait Until Timeout
→ Abort Request
→ Mark Timeout Error
→ Retry if Retryable
→ Return Safe Error
```

Timeout 기준:

| Timeout            | 설명                          |
| ------------------ | ----------------------------- |
| Connection Timeout | 서버 연결까지 대기 시간       |
| Read Timeout       | 응답 데이터 수신 대기 시간    |
| Write Timeout      | 요청 Body 전송 대기 시간      |
| Pool Timeout       | Connection Pool 대기 시간     |
| Total Timeout      | 전체 요청 최대 시간           |
| Streaming Timeout  | Stream 연결과 Chunk 대기 시간 |
| Tool Timeout       | Tool 실행 최대 시간           |

Python httpx Timeout 예:

```python
timeout = httpx.Timeout(
    connect=5.0,
    read=30.0,
    write=10.0,
    pool=5.0
)
```

Spring `.block()` Timeout 예:

```java
LlmChatResponse response = webClient.post()
        .uri("/chat/completions")
        .bodyValue(request)
        .retrieve()
        .bodyToMono(LlmChatResponse.class)
        .block(Duration.ofSeconds(30));
```

주의:

- Timeout을 너무 길게 잡아 장애를 숨기지 않는다.
- 긴 문서 생성은 Streaming 또는 비동기 작업을 고려한다.
- Timeout 발생 시 같은 요청을 무조건 재시도하지 않는다.
- Timeout 로그에는 latency, model, input size, retry count를 남긴다.
- Prompt 전문과 API Key는 로그에서 제거한다.

---

### [FAQ]

Q. Timeout이 뭐야?

A. API 요청이 일정 시간 안에 완료되지 않으면 실패로 처리하는 기준이다.

Q. LLM API 호출에 Timeout이 꼭 필요해?

A. 필요하다. Timeout이 없으면 요청이 무한 대기해 Thread나 Connection을 점유할 수 있다.

Q. Timeout을 길게 잡으면 안전해?

A. 항상 그렇지 않다. 너무 길면 장애 감지가 늦고 자원 점유가 길어진다.

Q. Streaming Timeout은 일반 Timeout과 달라?

A. 그렇다. 전체 시간뿐 아니라 첫 Chunk와 Chunk 간 대기 시간도 고려해야 한다.

---

## 2.2 Timeout Strategy

### [개념]

Timeout Strategy는 작업 유형, 모델 크기, Context 길이, Streaming 여부, 사용자 경험 기준에 따라 Timeout 값을 설계하는 방식이다.

LLM API는 작업마다 응답 시간이 크게 달라질 수 있으므로 고정 Timeout 하나만으로는 부족할 수 있다.

---

### [핵심]

- 짧은 FAQ와 긴 문서 생성의 Timeout은 달라야 한다.
- Local LLM은 API LLM보다 느릴 수 있다.
- 긴 Context와 긴 Output은 Timeout을 늘려야 할 수 있다.
- Streaming은 First Token Timeout과 Total Timeout을 분리한다.
- Tool Calling은 Tool별 Timeout을 별도로 둔다.
- Timeout은 사용자 경험과 서버 자원 보호의 균형이다.

---

### [실무]

작업별 Timeout 기준:

| 작업            | Timeout 기준        |
| --------------- | ------------------- |
| 짧은 FAQ        | 짧게                |
| 일반 Chat       | 중간                |
| RAG 답변        | 중간                |
| 긴 코드 리뷰    | 길게                |
| 문서 생성       | 길게 또는 Part 분할 |
| Embedding Batch | Batch 크기에 따라   |
| Streaming       | First Token + Total |
| Local LLM       | 더 길게 필요 가능   |
| Tool Execution  | Tool별 별도 기준    |

Timeout 설계 예:

```json
{
  "shortAnswerTimeoutSeconds": 15,
  "ragAnswerTimeoutSeconds": 45,
  "codeReviewTimeoutSeconds": 90,
  "streamTotalTimeoutSeconds": 180,
  "toolTimeoutSeconds": 30
}
```

Timeout Decision Flow:

```text
Task Type
→ Estimate Input Tokens
→ Estimate Output Tokens
→ Check Model Type
→ Check Streaming
→ Set Timeout
→ Log Actual Latency
→ Tune
```

주의:

- Timeout 설정은 모니터링 데이터로 조정한다.
- 모든 요청에 긴 Timeout을 주면 장애 시 자원 고갈 위험이 커진다.
- 너무 짧은 Timeout은 Retry 폭증을 만든다.
- Retry와 Timeout을 함께 고려해 전체 최대 대기 시간을 제한한다.
- Agent Loop에서는 Tool Timeout과 LLM Timeout이 누적될 수 있다.

---

### [FAQ]

Q. Timeout Strategy가 뭐야?

A. 작업 유형과 모델 특성에 따라 Timeout 값을 다르게 설계하는 방식이다.

Q. 모든 LLM 요청에 같은 Timeout을 써도 돼?

A. 권장하지 않는다. 짧은 답변, 긴 코드 리뷰, Streaming, Local LLM은 응답 시간이 다르다.

Q. Local LLM Timeout은 더 길어야 해?

A. 모델 크기와 하드웨어에 따라 API LLM보다 길게 필요할 수 있다.

Q. Timeout 값은 어떻게 개선해?

A. 실제 Latency 로그를 보고 작업 유형별로 조정한다.

---

## 2.3 Timeout Error Response

### [개념]

Timeout Error Response는 LLM API 또는 Tool이 Timeout으로 실패했을 때 Application이 반환하는 표준 오류 응답이다.

Timeout 오류는 사용자에게 명확히 전달하되 내부 구현이나 Secret은 노출하지 않는다.

---

### [핵심]

- Timeout은 실패 원인을 명확히 표시해야 한다.
- Retry 가능 여부를 포함할 수 있다.
- Partial Output 여부를 구분한다.
- Streaming Timeout은 partial 상태가 있을 수 있다.
- Agent Workflow에서는 timeout 상태를 다음 분기 조건으로 사용한다.
- Timeout 로그에는 원인 분석 Metadata를 남긴다.

---

### [실무]

Timeout Error Response 예:

```json
{
  "status": "failed",
  "errorCode": "llm_timeout",
  "message": "LLM API request timed out. Please try again with a shorter request.",
  "retryable": true,
  "partialOutput": false
}
```

Streaming Timeout Response 예:

```json
{
  "status": "partial",
  "errorCode": "stream_timeout",
  "message": "Streaming response timed out before completion.",
  "retryable": true,
  "partialOutput": true
}
```

Agent Timeout State 예:

```json
{
  "status": "failed",
  "agent": "ReviewAgent",
  "errorCode": "tool_timeout",
  "nextAction": "retry_with_smaller_context"
}
```

주의:

- Timeout 발생 시 사용자에게 완료된 답변처럼 보여주지 않는다.
- Partial Output은 completed와 분리한다.
- Timeout 오류에 내부 URL, API Key, Stack Trace를 포함하지 않는다.
- Retry 가능 여부를 정확히 설정한다.
- 반복 Timeout은 Context 축소 또는 작업 분할이 필요하다.

---

### [FAQ]

Q. Timeout Error Response는 뭐야?

A. LLM API나 Tool이 Timeout으로 실패했을 때 반환하는 표준 오류 응답이다.

Q. Timeout이 나면 사용자에게 어떻게 알려야 해?

A. 요청이 시간 초과되었고, 짧은 요청이나 재시도가 필요할 수 있다고 명확히 알려야 한다.

Q. Streaming Timeout은 일반 Timeout과 뭐가 달라?

A. 일부 응답이 이미 생성되었을 수 있으므로 partial 상태를 구분해야 한다.

Q. Timeout 응답에 내부 오류를 그대로 넣어도 돼?

A. 안 된다. 내부 URL, API Key, Stack Trace 같은 정보는 노출하지 않는다.

---

# 3. Retry Strategy

## 3.1 Retry

### [개념]

Retry는 일시적 오류가 발생했을 때 동일하거나 수정된 요청을 제한된 횟수 안에서 다시 시도하는 전략이다.

Retry는 안정성을 높일 수 있지만 비용, Latency, Rate Limit, 중복 실행 문제를 증가시킬 수 있다.

Retry 기본 Flow:

```text
Request Failed
→ Check Retryable
→ Check Retry Count
→ Wait Backoff
→ Retry Request
→ Success or Final Failure
```

---

### [핵심]

- Retry는 제한적으로 적용한다.
- Retry 가능한 오류와 금지 오류를 구분한다.
- Max Retry를 반드시 설정한다.
- Exponential Backoff를 적용한다.
- Jitter를 적용하면 동시 재시도 폭증을 줄일 수 있다.
- Idempotency 없는 작업은 Retry에 주의한다.
- Retry는 비용과 Token 사용량을 증가시킨다.
- Retry 결과를 로그로 남긴다.

---

### [실무]

Retry 가능 오류:

| 오류                    | Retry |
| ----------------------- | ----- |
| Timeout                 | 가능  |
| Network Error           | 가능  |
| 429 Rate Limit          | 가능  |
| 500 Server Error        | 가능  |
| 502 Bad Gateway         | 가능  |
| 503 Service Unavailable | 가능  |
| 504 Gateway Timeout     | 가능  |

Retry 금지 오류:

| 오류                   | Retry            |
| ---------------------- | ---------------- |
| 400 Bad Request        | 금지             |
| 401 Unauthorized       | 금지             |
| 403 Forbidden          | 금지             |
| 404 Not Found          | 금지             |
| 422 Validation Error   | 금지             |
| Invalid Tool Arguments | 금지 또는 재생성 |
| Safety Blocked         | 금지             |
| Empty Retrieval Result | 금지             |
| Permission Denied      | 금지             |

Retry 설정 예:

```json
{
  "maxRetries": 3,
  "backoff": "exponential",
  "jitter": true,
  "retryableErrors": ["timeout", "network_error", "rate_limit", "provider_5xx"]
}
```

주의:

- 무제한 Retry는 금지한다.
- 인증 오류는 Retry하지 않는다.
- 같은 잘못된 Request Body를 반복하지 않는다.
- Retry가 Rate Limit을 악화시킬 수 있다.
- Retry 실패 후 Agent Loop가 같은 요청을 다시 반복하지 않도록 상태를 기록한다.

---

### [FAQ]

Q. Retry가 뭐야?

A. 일시적 오류가 발생했을 때 요청을 제한된 횟수 안에서 다시 시도하는 전략이다.

Q. 모든 오류를 Retry하면 돼?

A. 아니다. Timeout, Network Error, 429, 5xx만 제한적으로 Retry하고 인증/권한/검증 오류는 Retry하지 않는다.

Q. Max Retry는 왜 필요해?

A. 무한 재시도로 비용, 부하, 지연이 폭증하는 것을 막기 위해 필요하다.

Q. Retry는 비용에 영향을 줘?

A. 그렇다. 같은 요청을 다시 호출하므로 Token 비용과 API 비용이 증가할 수 있다.

---

## 3.2 Exponential Backoff and Jitter

### [개념]

Exponential Backoff는 Retry 간 대기 시간을 점점 늘리는 전략이다.

Jitter는 Retry 대기 시간에 무작위성을 추가해 여러 Client가 동시에 재시도하는 문제를 줄이는 기법이다.

Backoff Flow:

```text
1st Failure
→ Wait 1s
→ Retry

2nd Failure
→ Wait 2s
→ Retry

3rd Failure
→ Wait 4s
→ Retry
```

---

### [핵심]

- Exponential Backoff는 일시적 장애 회복에 유리하다.
- Jitter는 재시도 요청이 한꺼번에 몰리는 것을 줄인다.
- 429 Rate Limit에서는 Retry-After Header를 우선 고려한다.
- Backoff 최대 대기 시간을 제한한다.
- Retry 전체 최대 시간을 제한한다.
- Backoff는 오류 유형별로 다르게 적용할 수 있다.

---

### [실무]

Backoff 설정 예:

```json
{
  "initialDelayMs": 500,
  "maxDelayMs": 8000,
  "multiplier": 2.0,
  "jitter": true,
  "maxRetries": 3
}
```

Backoff 계산 예:

```text
retry 1 → 500ms
retry 2 → 1000ms
retry 3 → 2000ms
maxDelay → 8000ms
```

Retry-After 처리 Flow:

```text
429 Response
→ Check Retry-After Header
→ If Exists, Wait Retry-After
→ Else, Apply Backoff
→ Retry if Max Retry not exceeded
```

주의:

- Backoff 없이 즉시 Retry하면 Rate Limit이 악화된다.
- Backoff가 너무 길면 사용자 경험이 나빠진다.
- 전체 요청 시간 제한을 초과하지 않도록 한다.
- Retry-After Header가 있으면 우선 적용한다.
- Backoff 설정은 Provider 정책에 맞게 조정한다.

---

### [FAQ]

Q. Exponential Backoff가 뭐야?

A. Retry할 때마다 대기 시간을 점점 늘리는 전략이다.

Q. Jitter는 뭐야?

A. 여러 요청이 동시에 재시도되는 것을 줄이기 위해 대기 시간에 무작위성을 추가하는 방식이다.

Q. 429 오류에서는 어떻게 대기해?

A. Retry-After Header가 있으면 그 값을 우선 사용하고, 없으면 Backoff를 적용한다.

Q. Backoff 없이 바로 Retry하면 안 돼?

A. 권장하지 않는다. Rate Limit이나 장애 상황을 더 악화시킬 수 있다.

---

## 3.3 Idempotency

### [개념]

Idempotency는 같은 요청을 여러 번 실행해도 결과가 한 번 실행한 것과 동일하게 유지되는 성질이다.

Retry가 있는 시스템에서는 Idempotency가 매우 중요하다.

Idempotency가 없는 작업을 Retry하면 중복 생성, 중복 전송, 중복 결제, 중복 수정이 발생할 수 있다.

---

### [핵심]

- 읽기 작업은 보통 Idempotent하다.
- 쓰기 작업은 Idempotency 보장이 필요하다.
- 이메일 전송, 결제, 배포, DB 수정은 Retry에 주의한다.
- Idempotency-Key를 사용할 수 있다.
- Tool Calling에서 쓰기 Tool은 Retry를 제한한다.
- 중복 실행 방지 로그가 필요하다.

---

### [실무]

작업별 Idempotency 기준:

| 작업           | Idempotency | Retry                 |
| -------------- | ----------- | --------------------- |
| 문서 검색      | 높음        | 가능                  |
| 파일 읽기      | 높음        | 가능                  |
| DB Select      | 높음        | 가능                  |
| Embedding 생성 | 중간        | 가능                  |
| Draft 생성     | 중간        | 주의                  |
| 이메일 전송    | 낮음        | 금지 또는 Key 필요    |
| 결제           | 낮음        | 강한 Idempotency 필요 |
| DB Update      | 낮음        | 주의                  |
| 파일 삭제      | 낮음        | 금지                  |
| 배포           | 낮음        | 강한 제어 필요        |

Idempotency-Key 예:

```text
Idempotency-Key: req-20260630-user123-task456
```

Retry Decision Flow:

```text
Operation Failed
→ Is Retryable Error?
→ Is Operation Idempotent?
→ Has Idempotency Key?
→ Retry or Stop
```

주의:

- 같은 Tool Call을 무작정 Retry하지 않는다.
- 쓰기 작업은 중복 실행 여부를 저장해야 한다.
- 결제나 이메일 전송은 Provider의 Idempotency 지원 여부를 확인한다.
- Agent Loop가 같은 쓰기 작업을 반복하지 않도록 한다.
- Idempotency-Key 자체에 개인정보를 직접 넣지 않는다.

---

### [FAQ]

Q. Idempotency가 뭐야?

A. 같은 요청을 여러 번 실행해도 결과가 한 번 실행한 것과 동일하게 유지되는 성질이다.

Q. Retry와 Idempotency는 왜 같이 봐야 해?

A. Retry가 같은 작업을 여러 번 실행할 수 있기 때문에 중복 부작용을 막아야 한다.

Q. 어떤 작업은 Retry하면 위험해?

A. 이메일 전송, 결제, DB 수정, 파일 삭제, 배포 같은 외부 부작용이 있는 작업이다.

Q. Idempotency-Key는 뭐야?

A. 중복 요청을 식별해 같은 작업이 여러 번 실행되지 않도록 돕는 고유 키다.

---

# 4. Rate Limit Handling

## 4.1 Rate Limit

### [개념]

Rate Limit은 LLM API Provider가 일정 시간 동안 허용하는 요청 수, Token 수, 동시 요청 수를 제한하는 정책이다.

Rate Limit을 초과하면 일반적으로 429 Too Many Requests 오류가 발생한다.

Rate Limit 기준:

- Requests Per Minute
- Tokens Per Minute
- Requests Per Day
- Concurrent Requests
- Model-specific Limit
- Organization Limit
- User Limit

---

### [핵심]

- Rate Limit은 요청 수 또는 Token 수 기준으로 적용될 수 있다.
- 병렬 호출은 Rate Limit을 빠르게 소모한다.
- 긴 RAG Context는 Token Limit을 빠르게 소모한다.
- Retry가 Rate Limit을 악화시킬 수 있다.
- 429 오류는 Backoff와 Queue로 대응한다.
- 사용량 모니터링이 필요하다.
- 사용자별 Rate Limit도 별도로 둘 수 있다.

---

### [실무]

Rate Limit Handling Flow:

```text
API Call
→ 429 Rate Limit
→ Check Retry-After
→ Queue or Backoff
→ Retry if Allowed
→ Fail Safely if Exceeded
```

Rate Limit 관리 전략:

| 전략              | 설명              |
| ----------------- | ----------------- |
| Token Budget      | 요청당 Token 제한 |
| Max Tokens Limit  | 출력 Token 제한   |
| Queue             | 요청을 순차 처리  |
| Throttling        | 요청 속도 제한    |
| Concurrency Limit | 동시 요청 수 제한 |
| Backoff           | Retry 대기        |
| Caching           | 반복 요청 감소    |
| Model Routing     | 작은 모델로 분산  |
| Usage Logging     | 사용량 추적       |

Rate Limit Response 예:

```json
{
  "status": "failed",
  "errorCode": "rate_limit_exceeded",
  "message": "LLM API rate limit exceeded. Request will be retried after backoff.",
  "retryable": true
}
```

주의:

- 429 발생 직후 즉시 Retry하지 않는다.
- 대량 Embedding 작업은 Queue 기반으로 처리한다.
- Agent 병렬 실행은 Rate Limit을 고려해 제한한다.
- 사용자 요청 폭주와 시스템 Batch 작업을 분리한다.
- Rate Limit 정책은 Provider와 모델별로 다를 수 있다.

---

### [FAQ]

Q. Rate Limit이 뭐야?

A. Provider가 일정 시간 동안 허용하는 요청 수, Token 수, 동시 요청 수를 제한하는 정책이다.

Q. 429 Too Many Requests는 뭐야?

A. Rate Limit을 초과했을 때 발생하는 HTTP 오류다.

Q. Rate Limit은 어떻게 처리해?

A. Retry-After, Exponential Backoff, Queue, Throttling, Token Budget으로 처리한다.

Q. Retry가 Rate Limit을 악화시킬 수 있어?

A. 그렇다. 즉시 반복 Retry는 요청 수를 더 늘려 Rate Limit을 악화시킬 수 있다.

---

## 4.2 Throttling and Queue

### [개념]

Throttling은 요청 속도를 제한하는 방식이다.

Queue는 요청을 즉시 실행하지 않고 순서대로 대기시켜 Rate Limit과 시스템 부하를 제어하는 구조이다.

Throttling과 Queue는 대량 Embedding, Multi-Agent Workflow, 동시 사용자 요청 처리에 필요하다.

---

### [핵심]

- Throttling은 초당 또는 분당 요청 수를 제한한다.
- Queue는 요청을 대기열에 넣고 순차 처리한다.
- Rate Limit 초과를 사전에 줄일 수 있다.
- 대량 작업과 사용자 실시간 요청은 Queue 우선순위를 다르게 둘 수 있다.
- Queue에는 Timeout과 Max Size가 필요하다.
- 실패 작업은 Retry Queue로 분리할 수 있다.

---

### [실무]

Queue 처리 Flow:

```text
Incoming Request
→ Check Priority
→ Enqueue
→ Rate Limit Scheduler
→ Execute API Call
→ Success or Retry Queue
```

Queue 설계 기준:

| 항목              | 기준               |
| ----------------- | ------------------ |
| Priority          | 사용자 요청 우선   |
| Max Queue Size    | 무한 대기 방지     |
| Worker Count      | Rate Limit에 맞게  |
| Retry Queue       | 일시 실패 재시도   |
| Dead Letter Queue | 반복 실패 격리     |
| Timeout           | 대기 시간 제한     |
| Monitoring        | 대기 수, 처리 속도 |

사용 사례:

| 작업                 | Queue 필요성 |
| -------------------- | ------------ |
| 대량 Embedding       | 높음         |
| RAG 문서 재색인      | 높음         |
| 실시간 Chat          | 중간         |
| Streaming Response   | 중간         |
| Agent 병렬 Tool 호출 | 높음         |
| 짧은 단일 요청       | 낮음         |

주의:

- Queue가 무한히 쌓이지 않도록 Max Size를 둔다.
- 오래된 요청은 Expire 처리할 수 있다.
- 사용자 실시간 요청과 Batch 작업을 같은 우선순위로 두지 않는다.
- Queue 대기 시간이 길면 사용자에게 상태를 알려야 한다.
- Worker 수를 Rate Limit보다 크게 늘리면 429가 증가한다.

---

### [FAQ]

Q. Throttling이 뭐야?

A. API 요청 속도를 제한해 Rate Limit 초과와 시스템 과부하를 막는 방식이다.

Q. Queue는 왜 필요해?

A. 요청을 순서대로 처리해 Rate Limit과 동시 요청 부하를 제어하기 위해 필요하다.

Q. 대량 Embedding에는 Queue가 필요해?

A. 필요하다. Batch 작업은 Rate Limit과 실패 재처리를 고려해야 한다.

Q. Queue가 너무 길어지면?

A. Max Queue Size, Timeout, 우선순위, Dead Letter Queue를 적용해야 한다.

---

## 4.3 Usage Limit

### [개념]

Usage Limit은 LLM API 사용량을 비용, 사용자, 조직, 기능, 모델 단위로 제한하는 정책이다.

Usage Limit은 비용 폭주, 남용, Rate Limit 초과, 시스템 자원 고갈을 방지한다.

Usage Limit 기준:

- User Daily Limit
- Workspace Limit
- Token Budget
- Cost Budget
- Model-specific Limit
- Feature-specific Limit
- Concurrent Request Limit

---

### [핵심]

- Usage Limit은 비용 관리에 필요하다.
- 사용자별 Token 사용량을 추적할 수 있다.
- 기능별 모델 사용 제한을 둘 수 있다.
- 무료/관리자/고급 사용자별 제한을 다르게 설정할 수 있다.
- Local LLM도 자원 사용 제한이 필요하다.
- Limit 초과 시 명확한 Error Response를 반환한다.

---

### [실무]

Usage Limit 예:

```json
{
  "userId": "user-001",
  "dailyTokenLimit": 100000,
  "usedTokens": 75200,
  "remainingTokens": 24800,
  "model": "model-name"
}
```

Limit Check Flow:

```text
Receive Request
→ Estimate Token Cost
→ Check User Limit
→ Check Workspace Limit
→ Check Feature Limit
→ Allow or Reject
```

Limit 초과 응답 예:

```json
{
  "status": "failed",
  "errorCode": "usage_limit_exceeded",
  "message": "Daily LLM usage limit exceeded.",
  "retryable": false
}
```

제한 기준:

| 제한             | 목적                  |
| ---------------- | --------------------- |
| User Limit       | 사용자별 남용 방지    |
| Workspace Limit  | 팀/프로젝트 비용 관리 |
| Model Limit      | 비싼 모델 사용 제한   |
| Feature Limit    | 고비용 기능 제한      |
| Concurrent Limit | 동시 요청 제어        |
| Batch Limit      | 대량 작업 보호        |

주의:

- Token 사용량은 Provider Usage와 내부 추정치를 함께 고려한다.
- Usage 정보가 없는 Provider는 추정 로직이 필요할 수 있다.
- Limit 초과를 Retry로 처리하지 않는다.
- 관리자 우회 정책을 명확히 한다.
- Usage Limit 로그에는 사용자 식별 정보 보호가 필요하다.

---

### [FAQ]

Q. Usage Limit이 뭐야?

A. 사용자, 기능, 모델, 비용 기준으로 LLM API 사용량을 제한하는 정책이다.

Q. Usage Limit은 왜 필요해?

A. 비용 폭주, 남용, Rate Limit 초과, 시스템 자원 고갈을 막기 위해 필요하다.

Q. Limit 초과는 Retry하면 돼?

A. 아니다. 정책상 제한이므로 Retry하지 않고 명확한 오류를 반환해야 한다.

Q. Usage 정보가 없는 Provider는 어떻게 해?

A. 내부 Token 추정 또는 요청 크기 기반 사용량 추적을 적용할 수 있다.

---

# 5. Response Validation Error

## 5.1 Invalid JSON Output

### [개념]

Invalid JSON Output은 LLM이 JSON 형식으로 응답해야 하지만 유효하지 않은 JSON을 생성한 상태이다.

Invalid JSON은 Agent Workflow, Tool Calling, 자동 파싱, Structured Output에서 치명적인 오류가 될 수 있다.

발생 원인:

- 설명 문장이 JSON 밖에 포함됨
- Markdown Code Block으로 감쌈
- JSON이 중간에 잘림
- 따옴표 누락
- 쉼표 오류
- Schema가 너무 복잡함
- Max Tokens 부족
- Streaming Buffer 미완성

---

### [핵심]

- JSON Output은 반드시 JSON Parse를 통과해야 한다.
- JSON Mode가 있어도 Schema Validation이 필요하다.
- Streaming JSON은 최종 Buffer 기준으로 파싱한다.
- `finish_reason=length`이면 JSON이 잘렸을 가능성이 높다.
- Invalid JSON은 후속 Agent나 Tool에 전달하지 않는다.
- 재요청은 Max Retry를 제한한다.
- Schema를 단순화하면 성공률이 높아질 수 있다.

---

### [실무]

Invalid JSON 처리 Flow:

```text
LLM Response
→ Finish Reason Check
→ JSON Parse
→ Parse Failed
→ Check Truncation
→ Retry or Fail
```

Invalid JSON 예:

```json
{
  "status": "success",
  "items": [
    {
      "name": "retry"
```

재요청 Prompt 예:

```text
Return valid JSON only.
Do not include Markdown.
Do not include explanation outside JSON.
Follow the required schema exactly.
```

처리 기준:

| 상황                     | 처리                |
| ------------------------ | ------------------- |
| 설명 문장 포함           | JSON only 재요청    |
| Markdown Code Block 포함 | Extract 또는 재요청 |
| 출력 잘림                | Max Tokens 조정     |
| Schema 복잡              | Schema 단순화       |
| Required 누락            | Schema 강조         |
| 반복 실패                | 안전 실패 처리      |

주의:

- 잘린 JSON을 임의로 보완하지 않는다.
- JSON Parser 실패를 무시하지 않는다.
- 후속 Tool Arguments로 사용하지 않는다.
- 반복 재요청은 비용을 증가시킨다.
- Invalid JSON 로그에 민감한 원문을 남기지 않는다.

---

### [FAQ]

Q. Invalid JSON Output이 뭐야?

A. LLM이 JSON으로 응답해야 하지만 유효하지 않은 JSON을 생성한 상태다.

Q. JSON Mode를 쓰면 Invalid JSON이 없어져?

A. 줄일 수는 있지만 Schema 불일치나 내용 오류는 여전히 발생할 수 있다.

Q. JSON이 잘렸으면 어떻게 해?

A. 잘린 JSON을 사용하지 말고 Max Tokens, Context 길이, Schema 복잡도를 조정해 재요청한다.

Q. Invalid JSON을 자동으로 고쳐서 써도 돼?

A. 권장하지 않는다. 특히 Tool Arguments나 Agent Output은 재요청하거나 실패 처리해야 한다.

---

## 5.2 Schema Validation Error

### [개념]

Schema Validation Error는 LLM Output이 유효한 JSON이지만 사전에 정의한 Schema와 맞지 않는 상태이다.

Schema Validation Error는 필수 필드 누락, 타입 불일치, Enum 불일치, 배열 구조 오류, 중첩 객체 오류로 발생한다.

---

### [핵심]

- JSON Parse 성공이 Schema Validation 성공을 의미하지 않는다.
- Required Field를 확인해야 한다.
- Enum 값이 허용 범위 안에 있는지 확인한다.
- 숫자와 문자열 타입 불일치를 확인한다.
- 배열 길이와 객체 구조를 확인한다.
- Business Rule Validation은 Schema Validation 이후 별도로 수행한다.

---

### [실무]

Schema Validation Error 예:

```json
{
  "status": "done",
  "summary": "Review completed",
  "issues": "none"
}
```

기대 Schema:

```json
{
  "status": "success | needs_fix | failed",
  "summary": "string",
  "issues": []
}
```

오류 분석:

```text
status=done
→ 허용 Enum 아님

issues="none"
→ Array가 아니라 String
```

처리 Flow:

```text
Valid JSON
→ Schema Validation
→ Validation Error
→ Retry with Schema Hint
→ If Repeated, Fail Safely
```

주의:

- Schema Validation 실패 Output을 다음 Agent로 넘기지 않는다.
- Optional Field와 Required Field 기준을 명확히 한다.
- Schema가 너무 복잡하면 실패 가능성이 증가한다.
- Tool Arguments는 Schema Validation 실패 시 실행하지 않는다.
- 재요청 시 실패 원인을 구체적으로 제공할 수 있다.

---

### [FAQ]

Q. Schema Validation Error가 뭐야?

A. JSON은 유효하지만 필수 필드, 타입, Enum, 배열 구조가 Schema와 맞지 않는 오류다.

Q. JSON Parse가 성공하면 충분해?

A. 아니다. Schema Validation과 Business Rule Validation이 추가로 필요하다.

Q. Schema Validation 실패 시 어떻게 해?

A. 실패 원인을 기준으로 재요청하거나 안전 실패 처리한다.

Q. Tool Arguments가 Schema Validation에 실패하면?

A. Tool을 실행하지 않아야 한다.

---

## 5.3 Truncated Output

### [개념]

Truncated Output은 LLM 응답이 Max Tokens, Context Window, Timeout, Stream Failure 때문에 중간에서 잘린 상태이다.

Truncated Output은 Markdown 문서, JSON Output, 코드 생성, Agent Output에서 심각한 문제를 만들 수 있다.

---

### [핵심]

- `finish_reason=length`는 Truncated Output 신호이다.
- JSON Output이 잘리면 Parse 실패가 발생한다.
- 코드가 잘리면 컴파일 실패가 발생할 수 있다.
- Markdown 문서가 잘리면 Required Section이 누락된다.
- Truncated Output은 완료 결과로 사용하면 안 된다.
- 반복 발생 시 작업 분할이 필요하다.

---

### [실무]

Truncation Detection Flow:

```text
LLM Response
→ Check finish_reason
→ Check Required Sections
→ Check JSON Parse
→ Check Code Completeness
→ Mark Truncated if Incomplete
```

출력 유형별 확인:

| Output Type  | Truncation Check       |
| ------------ | ---------------------- |
| JSON         | Parse 실패, 닫힘 누락  |
| Markdown     | 섹션 누락, 문장 중단   |
| Code         | 괄호 누락, 함수 미완성 |
| RAG Answer   | 결론 누락              |
| Agent Output | status/nextAction 누락 |
| Streaming    | Done Event 없음        |

처리 기준:

```text
Truncated
→ Do not use as final
→ Reduce Context
→ Increase Max Tokens if safe
→ Split Task
→ Regenerate
```

주의:

- 잘린 JSON을 임의로 닫아서 사용하지 않는다.
- 잘린 코드를 임의로 보완해 완료 처리하지 않는다.
- 문서 생성에서는 필수 섹션 검수를 수행한다.
- Output Reserve를 확보한다.
- 긴 결과물은 Part 단위로 생성한다.

---

### [FAQ]

Q. Truncated Output이 뭐야?

A. LLM 응답이 Token 제한, Timeout, Stream Failure 등으로 중간에서 잘린 상태다.

Q. `finish_reason=length`는 무슨 뜻이야?

A. Max Tokens 또는 Context 제한 때문에 출력이 잘렸을 가능성이 있다는 의미다.

Q. 잘린 JSON을 고쳐서 써도 돼?

A. 권장하지 않는다. 재요청하거나 작업 범위를 줄여 다시 생성해야 한다.

Q. Truncated Output이 반복되면?

A. Context를 줄이고 Output Reserve를 확보하거나 작업을 Part 단위로 나눈다.

---

# 6. Agent Error Recovery

## 6.1 Agent Error State

### [개념]

Agent Error State는 Agent Workflow에서 오류가 발생했을 때 현재 상태, 오류 원인, 복구 가능 여부, 다음 행동을 구조화한 데이터이다.

Agent는 LLM API, Tool, RAG, Validation, Permission, Timeout 오류를 상태로 관리해야 한다.

Agent Error State 구성:

- status
- agent
- step
- errorCode
- message
- retryable
- retryCount
- partialResult
- nextAction
- recoveryStrategy

---

### [핵심]

- Agent 오류는 자연어만으로 처리하지 않는다.
- 오류 상태는 구조화해야 한다.
- Retry 가능 여부를 명확히 표시한다.
- Partial Result와 Final Result를 구분한다.
- Recovery Strategy를 포함한다.
- 오류가 다음 Agent로 잘못 전파되지 않도록 차단한다.
- Review Agent는 Error State를 검토할 수 있다.

---

### [실무]

Agent Error State 예:

```json
{
  "status": "failed",
  "agent": "BackendAgent",
  "step": "generate_llm_client",
  "errorCode": "schema_validation_failed",
  "message": "Generated output does not match required schema.",
  "retryable": true,
  "retryCount": 1,
  "partialResult": null,
  "nextAction": "retry_with_simplified_schema",
  "recoveryStrategy": "regenerate_structured_output"
}
```

Agent Error Flow:

```text
Agent Step Failed
→ Create Error State
→ Determine Retryable
→ Select Recovery Strategy
→ Retry or Route
→ Stop if Max Retry Exceeded
```

Recovery Strategy:

| 오류              | Recovery                   |
| ----------------- | -------------------------- |
| Invalid JSON      | 재요청, Schema 단순화      |
| Timeout           | Context 축소, 재시도       |
| Rate Limit        | Backoff, Queue             |
| Tool Failure      | 대체 Tool 또는 실패        |
| Missing Info      | 추가 검색 또는 사용자 확인 |
| Permission Denied | 중단                       |
| Safety Blocked    | 사용자 승인 또는 차단      |
| Validation Failed | Review Agent로 전달        |

주의:

- Agent가 오류를 무시하고 다음 단계로 진행하지 않게 한다.
- Error State도 Schema Validation 대상이다.
- 반복 오류는 Max Retry 이후 중단한다.
- Partial Result를 Final Output처럼 전달하지 않는다.
- 오류 로그에 Secret을 포함하지 않는다.

---

### [FAQ]

Q. Agent Error State가 뭐야?

A. Agent Workflow에서 발생한 오류와 복구 전략을 구조화한 상태 데이터다.

Q. Agent 오류를 자연어로만 처리하면 안 돼?

A. 권장하지 않는다. 다음 단계 분기와 자동 복구를 위해 구조화된 상태가 필요하다.

Q. Partial Result와 Final Result는 왜 구분해?

A. 부분 결과를 완료 결과로 오해하면 잘못된 출력이 다음 Agent로 전파될 수 있기 때문이다.

Q. Agent Error가 반복되면?

A. Max Retry 이후 중단하거나 사용자 확인 단계로 넘겨야 한다.

---

## 6.2 Fallback Strategy

### [개념]

Fallback Strategy는 기본 LLM 호출, Tool, RAG 검색, Agent 단계가 실패했을 때 대체 경로로 처리하는 전략이다.

Fallback은 시스템 안정성을 높이지만 무분별한 대체는 품질 저하와 비용 증가를 만들 수 있다.

Fallback 대상:

- Model Fallback
- Provider Fallback
- Tool Fallback
- Retrieval Fallback
- Prompt Fallback
- Output Format Fallback
- Human Confirmation

---

### [핵심]

- Fallback은 실패 유형별로 다르게 적용한다.
- 비싼 모델로 무조건 Fallback하지 않는다.
- RAG 검색 실패를 일반 지식 답변으로 Fallback하면 위험하다.
- Tool 실패 시 대체 Tool을 사용할 수 있다.
- Structured Output 실패 시 Schema를 단순화할 수 있다.
- Safety Blocked는 Fallback하지 않고 차단 또는 승인 단계로 보낸다.
- Fallback 결과도 검증해야 한다.

---

### [실무]

Fallback Flow:

```text
Primary Path Failed
→ Classify Error
→ Check Fallback Policy
→ Execute Fallback
→ Validate Result
→ Return or Fail
```

Fallback Policy 예:

| 실패              | Fallback                |
| ----------------- | ----------------------- |
| Model Timeout     | 작은 Context로 재요청   |
| Provider 5xx      | 다른 Provider 사용      |
| Invalid JSON      | Schema 단순화           |
| Retrieval Empty   | Query Rewrite 후 재검색 |
| Retrieval Failed  | Keyword Search          |
| Tool Timeout      | Retry 또는 대체 Tool    |
| Rate Limit        | Queue 또는 Local LLM    |
| Safety Blocked    | 차단 또는 승인          |
| Permission Denied | Fallback 금지           |

Fallback Response 예:

```json
{
  "status": "success",
  "fallbackUsed": true,
  "fallbackType": "query_rewrite_retrieval",
  "answer": "검색 Query를 보강해 관련 문서를 찾았습니다."
}
```

주의:

- Fallback 사용 여부를 로그로 남긴다.
- Fallback 결과가 원래 요구사항을 만족하는지 확인한다.
- 문서 기반 답변을 일반 지식으로 대체하지 않는다.
- Provider Fallback은 응답 품질과 비용 차이를 고려한다.
- Fallback이 반복되면 근본 원인을 수정한다.

---

### [FAQ]

Q. Fallback Strategy가 뭐야?

A. 기본 경로가 실패했을 때 대체 모델, Tool, 검색, Prompt로 처리하는 전략이다.

Q. RAG 검색 실패 시 일반 지식으로 답해도 돼?

A. 문서 기반 답변이 목적이라면 안 된다. Query Rewrite, 추가 검색, Missing Information을 우선해야 한다.

Q. Provider 장애 시 Fallback은 가능해?

A. 가능하다. 다른 Provider나 Local LLM을 사용할 수 있지만 결과 검증이 필요하다.

Q. Fallback 결과도 검증해야 해?

A. 반드시 필요하다. 대체 경로도 오류나 품질 저하가 있을 수 있다.

---

# 7. Logging and Observability for Errors

## 7.1 Error Logging

### [개념]

Error Logging은 LLM API 호출 실패, Tool 오류, RAG 검색 실패, Validation 오류를 분석 가능한 형태로 기록하는 작업이다.

Error Logging은 장애 분석, 비용 관리, 품질 개선, 보안 감사에 필요하다.

---

### [핵심]

- Error Log에는 requestId가 필요하다.
- 오류 유형과 errorCode를 기록한다.
- HTTP Status, provider, model을 기록한다.
- Latency와 retryCount를 기록한다.
- Token Usage가 있으면 기록한다.
- Secret과 개인정보는 Redaction한다.
- Prompt 전문 저장은 보안 정책이 필요하다.

---

### [실무]

Error Log 예:

```json
{
  "requestId": "req-20260630-001",
  "provider": "openai-compatible",
  "model": "model-name",
  "errorCode": "rate_limit_exceeded",
  "httpStatus": 429,
  "retryable": true,
  "retryCount": 2,
  "latencyMs": 1240,
  "inputTokens": 1800,
  "outputTokens": 0
}
```

Log Field 기준:

| Field        | 설명             |
| ------------ | ---------------- |
| requestId    | 요청 추적        |
| userIdHash   | 사용자 식별 Hash |
| provider     | Provider 이름    |
| model        | 모델명           |
| errorCode    | 표준 오류 코드   |
| httpStatus   | HTTP 상태        |
| retryable    | 재시도 가능 여부 |
| retryCount   | 재시도 횟수      |
| latencyMs    | 응답 지연        |
| tokenUsage   | 비용 추적        |
| finishReason | 출력 종료 사유   |

Redaction 대상:

```text
API Key
Authorization Header
Secret
Password
Token
Personal Information
Raw Sensitive Prompt
Tool Arguments with Secret
```

주의:

- Authorization Header를 절대 로그에 남기지 않는다.
- Error Body 전체를 무조건 저장하지 않는다.
- 사용자의 민감한 Prompt는 마스킹하거나 저장하지 않는다.
- 로그가 너무 많으면 비용과 개인정보 위험이 증가한다.
- 보안 이벤트는 별도 Audit Log로 분리할 수 있다.

---

### [FAQ]

Q. Error Logging이 뭐야?

A. LLM API, Tool, RAG, Validation 오류를 분석 가능한 형태로 기록하는 작업이다.

Q. Error Log에는 무엇을 남겨?

A. requestId, provider, model, errorCode, httpStatus, retryCount, latency, tokenUsage를 남긴다.

Q. 로그에 절대 남기면 안 되는 것은?

A. API Key, Authorization Header, Secret, 개인정보, 민감한 Prompt 내용이다.

Q. Prompt 전문을 로그로 남겨도 돼?

A. 보안 정책이 있을 때만 제한적으로 가능하며 기본적으로는 권장하지 않는다.

---

## 7.2 Error Metrics

### [개념]

Error Metrics는 LLM API 연동 시스템의 오류율, Timeout 비율, Retry 횟수, Rate Limit 발생률, Validation 실패율을 수치로 관측하는 지표이다.

Error Metrics는 운영 안정성과 품질 개선에 사용된다.

---

### [핵심]

- 오류율은 시스템 안정성을 나타낸다.
- Timeout 비율은 성능과 Context 길이 문제를 보여준다.
- Rate Limit 발생률은 요청량과 Queue 정책을 조정하는 기준이다.
- Validation 실패율은 Prompt와 Schema 품질을 보여준다.
- Retry 성공률은 Retry 정책의 유효성을 보여준다.
- Model별 오류율을 비교할 수 있다.

---

### [실무]

권장 Metrics:

```text
llm_request_total
llm_request_failed_total
llm_timeout_total
llm_rate_limit_total
llm_retry_total
llm_retry_success_total
llm_invalid_json_total
llm_schema_validation_failed_total
llm_truncated_output_total
llm_empty_response_total
llm_latency_ms
llm_token_usage_total
```

Metrics 활용 기준:

| Metric                | 활용                      |
| --------------------- | ------------------------- |
| timeout rate          | Timeout 조정              |
| rate limit rate       | Queue/Throttling 조정     |
| invalid JSON rate     | Prompt/Schema 개선        |
| retry success rate    | Retry 정책 평가           |
| truncated output rate | Max Tokens/Context 조정   |
| empty response rate   | Provider/Prompt 문제 확인 |
| latency p95           | UX 개선                   |
| token usage           | 비용 관리                 |

주의:

- Metrics Label에 개인정보를 넣지 않는다.
- Model, provider, feature 기준 Label은 유용하다.
- 과도한 Label Cardinality는 모니터링 비용을 높인다.
- 오류율만 보지 말고 Latency와 비용도 함께 본다.
- Agent별 Metrics를 분리하면 병목을 찾기 쉽다.

---

### [FAQ]

Q. Error Metrics가 뭐야?

A. LLM API 오류율, Timeout, Retry, Rate Limit, Validation 실패를 수치로 관측하는 지표다.

Q. Validation 실패율은 왜 봐야 해?

A. Prompt, JSON Schema, Output Control 품질을 개선하는 기준이 되기 때문이다.

Q. Rate Limit Metrics는 어디에 써?

A. Queue, Throttling, Token Budget, 동시 요청 제한을 조정하는 데 사용한다.

Q. Metrics에 userId를 그대로 넣어도 돼?

A. 권장하지 않는다. Hash 처리하거나 개인정보를 제외해야 한다.

---

# 8. Common Mistakes

## 8.1 Error Handling Common Mistakes

### [개념]

Error Handling Common Mistakes는 LLM API 연동에서 오류를 제대로 분류하지 않거나 Retry, Timeout, Rate Limit, Validation을 잘못 설계해 발생하는 문제이다.

---

### [핵심]

자주 발생하는 실수:

- HTTP 200을 무조건 성공으로 처리
- HTTP Status Code 확인 누락
- Provider Error Body를 그대로 사용자에게 노출
- 모든 오류를 같은 메시지로 처리
- 모든 오류를 Retry
- 인증 오류를 Retry
- Rate Limit에서 즉시 Retry
- Timeout 없이 API 호출
- Timeout을 너무 길게 설정
- Max Retry 없이 무한 재시도
- Idempotency 없는 쓰기 작업 Retry
- `finish_reason=length` 무시
- Invalid JSON을 후속 Agent에 전달
- Schema Validation 실패를 무시
- Empty Retrieval에서 일반 지식으로 추측
- Partial Output을 Final Output으로 저장
- Error Log에 API Key 또는 Prompt 전문 저장
- Error Metrics 수집 누락

---

### [실무]

문제 진단 Flow:

```text
LLM Integration Failure
→ Check HTTP Status
→ Check Provider Error
→ Check Timeout
→ Check Retry Count
→ Check Rate Limit
→ Check Response Validation
→ Check Error Log
→ Check Metrics
```

해결 기준:

| 문제              | 해결                            |
| ----------------- | ------------------------------- |
| 인증 실패 반복    | API Key와 환경변수 확인         |
| Rate Limit 증가   | Queue, Throttling, Backoff      |
| Timeout 증가      | Context 축소, Timeout 조정      |
| Invalid JSON 증가 | Schema 단순화, Prompt 수정      |
| Truncation 증가   | Max Tokens 조정, Part 분할      |
| Retry 폭증        | Retryable Error 제한            |
| 비용 증가         | Retry/Token Usage 확인          |
| RAG 오답          | Missing Rule, Answer Validation |
| Agent Loop 오류   | Max Step, Error State           |

검수 Checklist:

```text
HTTP Status Code를 확인하는가?
Provider Error를 표준 Error로 변환하는가?
Timeout이 설정되어 있는가?
Retry 가능 오류와 금지 오류가 구분되는가?
Exponential Backoff와 Jitter가 있는가?
Rate Limit 대응이 있는가?
Idempotency 없는 작업을 Retry하지 않는가?
Empty Response를 검증하는가?
Invalid JSON을 차단하는가?
Schema Validation 실패를 처리하는가?
Truncated Output을 완료 결과로 쓰지 않는가?
Agent Error State가 구조화되어 있는가?
Fallback 결과도 검증하는가?
Secret Redaction이 적용되는가?
Error Metrics를 수집하는가?
```

---

### [FAQ]

Q. Error Handling에서 가장 흔한 실수는?

A. HTTP 200을 무조건 성공으로 보고 Response Validation을 하지 않는 것이다.

Q. Retry에서 가장 위험한 실수는?

A. 모든 오류를 Retry하거나 Idempotency 없는 쓰기 작업을 반복 실행하는 것이다.

Q. Rate Limit에서 가장 흔한 실수는?

A. 429 오류 직후 Backoff 없이 즉시 재시도하는 것이다.

Q. Timeout에서 가장 흔한 실수는?

A. Timeout을 아예 설정하지 않거나 모든 작업에 동일한 Timeout을 사용하는 것이다.

Q. Validation 오류에서 가장 위험한 실수는?

A. Invalid JSON이나 Schema 불일치 Output을 다음 Agent 또는 Tool에 전달하는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. LLM API Error Handling이 뭐야?
A. LLM API 호출과 응답 처리 중 발생하는 오류를 분류하고 안전하게 처리하는 구조다.

Q. HTTP 200이면 성공으로 봐도 돼?
A. 아니다. HTTP 200이어도 content가 비어 있거나 JSON Schema가 틀리거나 출력이 잘렸을 수 있다.

Q. HTTP Status Error는 뭐야?
A. LLM API Provider가 HTTP 상태 코드로 요청 실패 원인을 알려주는 오류다.

Q. 401 Unauthorized는 어떻게 처리해?
A. API Key 누락, 잘못된 Key, Authorization Header, Secret Rotation 여부를 확인한다.

Q. 403 Forbidden은 Retry해도 돼?
A. 일반적으로 Retry하지 않는다. 권한 부족이나 정책 차단을 확인해야 한다.

Q. 429 Rate Limit은 어떻게 처리해?
A. Retry-After를 확인하고 Exponential Backoff, Queue, Throttling을 적용한다.

Q. 500 계열 오류는 Retry해도 돼?
A. 제한적으로 가능하다. Max Retry와 Backoff를 적용해야 한다.

Q. 400 Bad Request는 Retry하면 돼?
A. 아니다. Request Body, Parameter, Provider 지원 필드를 수정해야 한다.

Q. Provider Error Format이 뭐야?
A. LLM API Provider가 오류 정보를 JSON으로 표현하는 구조다.

Q. Provider Error를 왜 표준 Error로 바꿔?
A. Service, Agent, UI가 Provider 차이와 무관하게 일관된 오류 처리를 하기 위해서다.

Q. Timeout이 뭐야?
A. API 요청이 일정 시간 안에 완료되지 않으면 실패로 처리하는 기준이다.

Q. LLM API 호출에 Timeout이 꼭 필요해?
A. 필요하다. Timeout이 없으면 요청이 무한 대기해 Thread나 Connection을 점유할 수 있다.

Q. Timeout Strategy가 뭐야?
A. 작업 유형과 모델 특성에 따라 Timeout 값을 다르게 설계하는 방식이다.

Q. 모든 LLM 요청에 같은 Timeout을 써도 돼?
A. 권장하지 않는다. 짧은 답변, 긴 코드 리뷰, Streaming, Local LLM은 응답 시간이 다르다.

Q. Timeout Error Response는 뭐야?
A. LLM API나 Tool이 Timeout으로 실패했을 때 반환하는 표준 오류 응답이다.

Q. Streaming Timeout은 일반 Timeout과 뭐가 달라?
A. 일부 응답이 이미 생성되었을 수 있으므로 partial 상태를 구분해야 한다.

Q. Retry가 뭐야?
A. 일시적 오류가 발생했을 때 요청을 제한된 횟수 안에서 다시 시도하는 전략이다.

Q. 모든 오류를 Retry하면 돼?
A. 아니다. Timeout, Network Error, 429, 5xx만 제한적으로 Retry하고 인증/권한/검증 오류는 Retry하지 않는다.

Q. Max Retry는 왜 필요해?
A. 무한 재시도로 비용, 부하, 지연이 폭증하는 것을 막기 위해 필요하다.

Q. Exponential Backoff가 뭐야?
A. Retry할 때마다 대기 시간을 점점 늘리는 전략이다.

Q. Jitter는 뭐야?
A. 여러 요청이 동시에 재시도되는 것을 줄이기 위해 대기 시간에 무작위성을 추가하는 방식이다.

Q. Retry-After Header는 언제 봐?
A. 429 Rate Limit 응답을 받았을 때 우선 확인한다.

Q. Idempotency가 뭐야?
A. 같은 요청을 여러 번 실행해도 결과가 한 번 실행한 것과 동일하게 유지되는 성질이다.

Q. Retry와 Idempotency는 왜 같이 봐야 해?
A. Retry가 같은 작업을 여러 번 실행할 수 있기 때문에 중복 부작용을 막아야 한다.

Q. 어떤 작업은 Retry하면 위험해?
A. 이메일 전송, 결제, DB 수정, 파일 삭제, 배포 같은 외부 부작용이 있는 작업이다.

Q. Rate Limit이 뭐야?
A. Provider가 일정 시간 동안 허용하는 요청 수, Token 수, 동시 요청 수를 제한하는 정책이다.

Q. 429 Too Many Requests는 뭐야?
A. Rate Limit을 초과했을 때 발생하는 HTTP 오류다.

Q. Throttling이 뭐야?
A. API 요청 속도를 제한해 Rate Limit 초과와 시스템 과부하를 막는 방식이다.

Q. Queue는 왜 필요해?
A. 요청을 순서대로 처리해 Rate Limit과 동시 요청 부하를 제어하기 위해 필요하다.

Q. Usage Limit이 뭐야?
A. 사용자, 기능, 모델, 비용 기준으로 LLM API 사용량을 제한하는 정책이다.

Q. Usage Limit은 왜 필요해?
A. 비용 폭주, 남용, Rate Limit 초과, 시스템 자원 고갈을 막기 위해 필요하다.

Q. Invalid JSON Output이 뭐야?
A. LLM이 JSON으로 응답해야 하지만 유효하지 않은 JSON을 생성한 상태다.

Q. JSON Mode를 쓰면 Invalid JSON이 없어져?
A. 줄일 수는 있지만 Schema 불일치나 내용 오류는 여전히 발생할 수 있다.

Q. Schema Validation Error가 뭐야?
A. JSON은 유효하지만 필수 필드, 타입, Enum, 배열 구조가 Schema와 맞지 않는 오류다.

Q. Truncated Output이 뭐야?
A. LLM 응답이 Token 제한, Timeout, Stream Failure 등으로 중간에서 잘린 상태다.

Q. `finish_reason=length`는 무슨 뜻이야?
A. Max Tokens 또는 Context 제한 때문에 출력이 잘렸을 가능성이 있다는 의미다.

Q. Agent Error State가 뭐야?
A. Agent Workflow에서 발생한 오류와 복구 전략을 구조화한 상태 데이터다.

Q. Fallback Strategy가 뭐야?
A. 기본 경로가 실패했을 때 대체 모델, Tool, 검색, Prompt로 처리하는 전략이다.

Q. RAG 검색 실패 시 일반 지식으로 답해도 돼?
A. 문서 기반 답변이 목적이라면 안 된다. Query Rewrite, 추가 검색, Missing Information을 우선해야 한다.

Q. Error Logging이 뭐야?
A. LLM API, Tool, RAG, Validation 오류를 분석 가능한 형태로 기록하는 작업이다.

Q. Error Log에는 무엇을 남겨?
A. requestId, provider, model, errorCode, httpStatus, retryCount, latency, tokenUsage를 남긴다.

Q. 로그에 절대 남기면 안 되는 것은?
A. API Key, Authorization Header, Secret, 개인정보, 민감한 Prompt 내용이다.

Q. Error Metrics가 뭐야?
A. LLM API 오류율, Timeout, Retry, Rate Limit, Validation 실패를 수치로 관측하는 지표다.

Q. Error Handling에서 가장 흔한 실수는?
A. HTTP 200을 무조건 성공으로 보고 Response Validation을 하지 않는 것이다.

Q. Retry에서 가장 위험한 실수는?
A. 모든 오류를 Retry하거나 Idempotency 없는 쓰기 작업을 반복 실행하는 것이다.

Q. Validation 오류에서 가장 위험한 실수는?
A. Invalid JSON이나 Schema 불일치 Output을 다음 Agent 또는 Tool에 전달하는 것이다.
