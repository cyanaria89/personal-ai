# LLM Core & API Integration Part05 - Streaming Response Processing

---

# 1. Streaming Response

## 1.1 Streaming Response

### [개념]

Streaming Response는 LLM이 전체 응답을 완성한 뒤 한 번에 반환하지 않고, 생성되는 Token 또는 Chunk를 순차적으로 전달하는 응답 방식이다.

Streaming은 긴 응답, 채팅 UI, 코드 생성, 문서 생성, RAG 답변에서 사용자 체감 속도를 개선한다.

기본 Flow:

```text
Client Request
→ LLM Starts Generation
→ Token Chunk Stream
→ Client Accumulates Chunks
→ Final Response
```

---

### [핵심]

- Streaming은 응답 전체를 기다리지 않고 부분 결과를 받는다.
- 사용자는 첫 Token 또는 첫 Chunk를 빠르게 볼 수 있다.
- 전체 처리 시간이 줄어드는 것이 아니라 체감 Latency가 줄어든다.
- Streaming 중간 출력은 불완전하다.
- 최종 결과 조립 로직이 필요하다.
- Streaming 응답도 Finish Reason과 Validation이 필요하다.
- JSON Output과 Streaming은 파싱이 까다롭다.

---

### [실무]

2026 실무 기준 Streaming은 Chat UI와 긴 답변 UX에서 기본 선택지로 사용된다.

권장 사용처:

| 사용처            | Streaming 적합성 |
| ----------------- | ---------------- |
| Chat UI           | 높음             |
| 긴 RAG 답변       | 높음             |
| 코드 생성         | 높음             |
| 문서 생성         | 높음             |
| 짧은 FAQ          | 낮음             |
| JSON Output       | 낮음~중간        |
| Tool Arguments    | 낮음             |
| 내부 Agent Output | 낮음~중간        |

Streaming 처리 구조:

```text
Frontend
→ Request Backend
→ Backend calls LLM Stream
→ Backend forwards chunks
→ Frontend renders partial output
→ Final validation after stream end
```

주의:

- Streaming 중간 Chunk를 완성 답변처럼 검증하면 안 된다.
- JSON Output은 전체 응답 조립 후 파싱해야 한다.
- 중간 취소, 네트워크 끊김, Timeout 처리가 필요하다.
- 로그 저장은 최종 조립본 기준으로 수행한다.
- 안전 검증이 필요한 응답은 최종 Validation 후 확정 처리한다.

---

### [FAQ]

Q. Streaming Response가 뭐야?

A. LLM이 응답을 한 번에 반환하지 않고 생성되는 Token 또는 Chunk를 순차적으로 전달하는 방식이다.

Q. Streaming을 쓰면 전체 응답 시간이 줄어?

A. 반드시 그렇지는 않다. 전체 생성 시간보다 사용자가 첫 응답을 보는 체감 시간이 줄어든다.

Q. Streaming 중간 출력은 믿어도 돼?

A. 아니다. 중간 출력은 불완전하므로 최종 조립 후 검증해야 한다.

Q. Streaming은 언제 써?

A. 긴 답변, 채팅 UI, 코드 생성, RAG 답변처럼 사용자가 빠른 반응을 체감해야 할 때 사용한다.

---

## 1.2 Token Stream

### [개념]

Token Stream은 LLM이 생성하는 Token 또는 Text Delta를 순차적으로 전달하는 데이터 흐름이다.

Provider에 따라 Token 단위, Text Delta 단위, Message Delta 단위, Event 단위로 전달될 수 있다.

Token Stream 구성 요소:

- Stream Event
- Delta
- Token Chunk
- Partial Content
- Finish Event
- Finish Reason
- Error Event

---

### [핵심]

- Token Stream은 작은 Chunk들이 연속으로 도착한다.
- 각 Chunk는 완전한 문장이나 완전한 JSON이 아닐 수 있다.
- Client는 Chunk를 누적해 최종 응답을 만든다.
- 마지막 Chunk에서 Finish Reason을 확인할 수 있다.
- Stream 중간에 오류가 발생할 수 있다.
- Provider별 Stream Format이 다르다.

---

### [실무]

Streaming 응답 처리 Flow:

```text
Open Stream
→ Receive Chunk
→ Extract Delta Content
→ Append Buffer
→ Render Partial Output
→ Receive Finish Event
→ Validate Final Output
→ Close Stream
```

Chunk 누적 예:

```text
Chunk 1: "JWT"
Chunk 2: " 인증은"
Chunk 3: " Access Token"
Chunk 4: "을 검증하는 방식입니다."
Final: "JWT 인증은 Access Token을 검증하는 방식입니다."
```

Stream Event 처리 기준:

| Event           | 처리                    |
| --------------- | ----------------------- |
| content delta   | Buffer에 누적           |
| tool call delta | Tool Call Buffer에 누적 |
| finish event    | 최종 응답 검증          |
| error event     | Stream 실패 처리        |
| heartbeat       | 연결 유지               |
| done marker     | Stream 종료             |

주의:

- Chunk 단위로 Markdown이나 JSON을 파싱하지 않는다.
- Multi-byte 문자 깨짐을 방지해야 한다.
- Chunk 순서를 보존해야 한다.
- 중복 Chunk 누적을 방지한다.
- Stream 종료 이벤트를 반드시 처리한다.

---

### [FAQ]

Q. Token Stream이 뭐야?

A. LLM이 생성하는 Token 또는 Text Delta가 순차적으로 전달되는 흐름이다.

Q. Chunk는 완전한 문장이야?

A. 아니다. Chunk는 단어 일부, 문장 일부, JSON 일부일 수 있다.

Q. Chunk는 어떻게 처리해?

A. 순서대로 Buffer에 누적하고 최종 종료 이벤트 후 전체 결과를 검증한다.

Q. Streaming에서 Finish Reason은 왜 필요해?

A. 응답이 정상 종료되었는지, 중간에 잘렸는지, Tool 호출이 필요한지 판단하기 위해 필요하다.

---

## 1.3 Server-Sent Events

### [개념]

Server-Sent Events는 서버가 클라이언트에게 단방향 이벤트 스트림을 지속적으로 전송하는 HTTP 기반 방식이다.

LLM Streaming API는 Server-Sent Events 형식을 사용하는 경우가 많다.

SSE 기본 형태:

```text
data: {"delta":"Hello"}

data: {"delta":" world"}

data: [DONE]
```

---

### [핵심]

- SSE는 HTTP 연결을 유지하면서 서버가 이벤트를 계속 보낸다.
- LLM Streaming에서 Chunk 전달 방식으로 자주 사용된다.
- Client는 이벤트를 읽고 data 필드를 파싱한다.
- `[DONE]` 같은 종료 Marker가 사용될 수 있다.
- SSE는 단방향 스트림이다.
- WebSocket과 다르게 양방향 통신이 목적은 아니다.

---

### [실무]

SSE 처리 Flow:

```text
Client sends request
→ Server opens SSE stream
→ Server sends data events
→ Client parses each event
→ Client appends content
→ Server sends done event
→ Client closes stream
```

SSE Chunk 예:

```text
data: {"choices":[{"delta":{"content":"LLM"}}]}

data: {"choices":[{"delta":{"content":" Streaming"}}]}

data: {"choices":[{"finish_reason":"stop"}]}

data: [DONE]
```

Backend 구현 기준:

- `Content-Type: text/event-stream`
- `Cache-Control: no-cache`
- 연결 유지 처리
- Chunk flush 처리
- Client disconnect 처리
- Timeout 설정
- Error Event 처리

Frontend 처리 기준:

- EventSource 또는 fetch stream 사용
- Chunk 단위 렌더링
- Buffer 누적
- AbortController로 취소 처리
- 최종 응답 검증 후 상태 확정

주의:

- Proxy나 Load Balancer가 Streaming을 Buffering할 수 있다.
- 긴 연결은 Timeout 설정이 중요하다.
- SSE는 Binary 전송보다 Text Event에 적합하다.
- 인증 Token이 Query String에 노출되지 않도록 주의한다.
- CORS와 Header 정책을 확인해야 한다.

---

### [FAQ]

Q. Server-Sent Events가 뭐야?

A. 서버가 클라이언트에게 HTTP 연결을 유지하며 이벤트를 계속 보내는 단방향 스트리밍 방식이다.

Q. LLM Streaming에서 SSE를 많이 써?

A. 그렇다. 많은 LLM API가 Streaming Response를 SSE 형식으로 제공한다.

Q. SSE와 WebSocket 차이는?

A. SSE는 서버에서 클라이언트로 보내는 단방향 스트림이고, WebSocket은 양방향 통신이다.

Q. SSE에서 `[DONE]`은 뭐야?

A. Stream이 끝났음을 알리는 종료 Marker로 사용될 수 있다.

---

# 2. Streaming API Request

## 2.1 Stream Parameter

### [개념]

Stream Parameter는 LLM API 요청에서 Streaming Response 사용 여부를 지정하는 설정값이다.

OpenAI-compatible API에서는 일반적으로 `stream: true` 형태로 사용한다.

Request Flow:

```text
Build Chat Completion Request
→ Set stream true
→ Send HTTP Request
→ Receive Streaming Response
```

---

### [핵심]

- `stream: true`는 Streaming 응답을 요청한다.
- `stream: false` 또는 생략은 일반 Non-Streaming 응답이다.
- Streaming 응답 구조는 Non-Streaming 응답 구조와 다를 수 있다.
- Usage 정보가 Stream 종료 시점에만 제공되거나 제공되지 않을 수 있다.
- Provider마다 Stream Option 지원 범위가 다르다.

---

### [실무]

Streaming Request 예:

```json
{
  "model": "model-name",
  "messages": [
    {
      "role": "system",
      "content": "You are a helpful assistant."
    },
    {
      "role": "user",
      "content": "LLM Streaming을 설명해줘."
    }
  ],
  "temperature": 0.2,
  "max_tokens": 1200,
  "stream": true
}
```

Non-Streaming과 Streaming 비교:

| 항목          | Non-Streaming          | Streaming           |
| ------------- | ---------------------- | ------------------- |
| 응답 방식     | 전체 응답 한 번에 반환 | Chunk 순차 반환     |
| UX            | 첫 응답까지 대기       | 빠른 첫 출력        |
| 구현 난이도   | 낮음                   | 높음                |
| JSON 파싱     | 쉬움                   | 최종 조립 필요      |
| 중간 취소     | 제한적                 | 가능                |
| Finish Reason | 응답 Body에서 확인     | 최종 Chunk에서 확인 |
| Usage         | 보통 응답에 포함       | Provider별 차이     |

주의:

- Streaming을 사용하면 Response Parser를 별도로 만들어야 한다.
- 기존 Non-Streaming DTO로 바로 파싱할 수 없을 수 있다.
- Stream 중간 오류와 연결 끊김을 처리해야 한다.
- Usage Logging 방식이 달라질 수 있다.

---

### [FAQ]

Q. `stream: true`는 뭐야?

A. LLM API가 응답을 Chunk 단위로 순차 전송하도록 요청하는 설정이다.

Q. Streaming Response는 일반 Response와 구조가 같아?

A. 아니다. Streaming은 Chunk/Event 형태로 오므로 별도 파서가 필요하다.

Q. Streaming에서도 Usage 정보를 받을 수 있어?

A. Provider마다 다르다. 종료 시점에 제공되거나 제공되지 않을 수 있다.

Q. 모든 모델이 Streaming을 지원해?

A. 아니다. Provider와 모델 기능에 따라 지원 여부가 다르다.

---

## 2.2 Streaming Request Design

### [개념]

Streaming Request Design은 Streaming 응답을 안정적으로 처리하기 위해 Request, Timeout, Cancellation, Output Format을 설계하는 과정이다.

Streaming은 단순히 `stream: true`만 추가하는 것이 아니라 연결, 취소, 검증, 로그 정책을 함께 설계해야 한다.

---

### [핵심]

- Streaming은 긴 연결을 유지한다.
- Timeout 기준이 Non-Streaming과 다르다.
- 사용자 취소 처리가 필요하다.
- 최종 응답 Buffer를 관리해야 한다.
- 안전 검증은 최종 조립 후 수행한다.
- 중간 Chunk 렌더링과 최종 확정 상태를 구분한다.

---

### [실무]

Streaming Request 설계 항목:

| 항목             | 기준                    |
| ---------------- | ----------------------- |
| Request Timeout  | 전체 연결 시간 기준     |
| Read Timeout     | Chunk 간 최대 대기 시간 |
| Cancellation     | 사용자 중단 지원        |
| Buffer           | 최종 응답 누적          |
| Partial Render   | UI 임시 출력            |
| Final Validation | 최종 응답 검증          |
| Error Handling   | 중간 실패 처리          |
| Logging          | 최종 조립본 기준        |

권장 Flow:

```text
User sends prompt
→ Backend opens LLM stream
→ Frontend receives partial chunks
→ User may cancel
→ Stream ends
→ Backend validates final response
→ Save final response
```

주의:

- Streaming 중 사용자에게 보이는 텍스트와 저장되는 최종 텍스트를 구분한다.
- 사용자가 취소하면 LLM API 요청도 중단해야 한다.
- 연결이 끊긴 경우 Partial Output을 완료 답변처럼 저장하지 않는다.
- 긴 Streaming 요청은 Rate Limit과 동시 연결 수에 영향을 준다.
- JSON Output이 필요한 내부 Agent 작업은 Non-Streaming이 더 안정적일 수 있다.

---

### [FAQ]

Q. Streaming Request Design은 뭐야?

A. Streaming 응답을 안정적으로 처리하기 위해 요청, Timeout, 취소, Buffer, 검증을 설계하는 것이다.

Q. Streaming에서 Timeout은 어떻게 봐야 해?

A. 전체 요청 시간과 Chunk 간 대기 시간을 구분해서 봐야 한다.

Q. 사용자가 중간에 취소하면?

A. Frontend 렌더링을 멈추고 Backend 또는 LLM API Stream도 중단해야 한다.

Q. Partial Output을 저장해도 돼?

A. 완료 상태와 구분해 저장해야 한다. 일반적으로 최종 응답만 확정 저장하는 것이 안전하다.

---

# 3. Streaming Client Implementation

## 3.1 Python Streaming Client

### [개념]

Python Streaming Client는 Python에서 LLM API의 Streaming Response를 읽고 Chunk를 누적하는 구현 방식이다.

Python에서는 `requests`, `httpx`, Provider SDK 등을 사용할 수 있다.

---

### [핵심]

- Streaming 요청은 일반 JSON 응답 파싱과 다르다.
- Response Body를 Line 또는 Event 단위로 읽는다.
- 각 Event에서 Delta Content를 추출한다.
- Buffer에 누적해 최종 응답을 만든다.
- `[DONE]` 또는 Finish Event를 처리한다.
- 중간 오류와 Timeout을 처리한다.

---

### [실무]

Python Streaming 처리 예:

```python
import json
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
            {"role": "user", "content": "Streaming을 설명해줘."}
        ],
        "stream": True
    },
    stream=True,
    timeout=60
)

response.raise_for_status()

buffer = []

for line in response.iter_lines(decode_unicode=True):
    if not line:
        continue

    if line.startswith("data: "):
        data = line.removeprefix("data: ").strip()

        if data == "[DONE]":
            break

        event = json.loads(data)
        delta = event["choices"][0].get("delta", {})
        content = delta.get("content")

        if content:
            buffer.append(content)
            print(content, end="", flush=True)

final_text = "".join(buffer)
```

개선 기준:

- JSON 파싱 예외 처리
- Finish Reason 확인
- Empty Final Response 검증
- Timeout 분리
- Retry 정책 제한
- Usage Logging
- Secret Redaction

주의:

- `iter_lines()` 결과가 항상 완전한 JSON이라고 가정하지 않는다.
- Provider별 Event 구조가 다를 수 있다.
- Stream 중간에 연결이 끊길 수 있다.
- 최종 Buffer가 비어 있으면 Empty Response로 처리한다.
- Streaming 중 출력한 내용과 최종 검증 결과가 다를 수 있다.

---

### [FAQ]

Q. Python에서 Streaming은 어떻게 처리해?

A. HTTP 응답을 Line 또는 Event 단위로 읽고 Delta Content를 Buffer에 누적한다.

Q. `[DONE]`은 어떻게 처리해?

A. Stream 종료 신호로 보고 읽기를 중단한다.

Q. Streaming 중 JSON 파싱 오류가 나면?

A. Event 구조를 확인하고 Provider별 파서를 분리해야 한다.

Q. 최종 응답은 어떻게 만들어?

A. 각 Chunk의 Content를 순서대로 누적한 Buffer를 join해서 만든다.

---

## 3.2 Spring WebClient Streaming

### [개념]

Spring WebClient Streaming은 Spring Boot에서 LLM Streaming Response를 Flux 기반으로 처리하는 방식이다.

WebClient는 Streaming 응답을 `Flux<String>` 또는 Provider별 Event DTO로 받을 수 있다.

---

### [핵심]

- Streaming 응답은 Flux로 처리할 수 있다.
- Backend는 LLM Stream을 Frontend로 다시 전달할 수 있다.
- `text/event-stream` 응답을 사용할 수 있다.
- Timeout과 Client Disconnect 처리가 필요하다.
- 최종 응답 저장이 필요하면 Buffer 누적 로직이 필요하다.
- Error Handling을 Stream 내부에 포함해야 한다.

---

### [실무]

Spring WebClient Streaming 예:

```java
@Service
public class LlmStreamingClient {

    private final WebClient webClient;
    private final String apiKey;

    public LlmStreamingClient(
            WebClient.Builder builder,
            @Value("${llm.api-key}") String apiKey
    ) {
        this.webClient = builder
                .baseUrl("https://api.example.com/v1")
                .build();
        this.apiKey = apiKey;
    }

    public Flux<String> streamChat(LlmChatRequest request) {
        return webClient.post()
                .uri("/chat/completions")
                .header(HttpHeaders.AUTHORIZATION, "Bearer " + apiKey)
                .contentType(MediaType.APPLICATION_JSON)
                .accept(MediaType.TEXT_EVENT_STREAM)
                .bodyValue(request.withStream(true))
                .retrieve()
                .bodyToFlux(String.class)
                .timeout(Duration.ofSeconds(60));
    }
}
```

Controller 예:

```java
@RestController
@RequestMapping("/api/llm")
public class LlmStreamController {

    private final LlmStreamingClient llmStreamingClient;

    public LlmStreamController(LlmStreamingClient llmStreamingClient) {
        this.llmStreamingClient = llmStreamingClient;
    }

    @PostMapping(value = "/stream", produces = MediaType.TEXT_EVENT_STREAM_VALUE)
    public Flux<String> stream(@RequestBody LlmChatRequest request) {
        return llmStreamingClient.streamChat(request);
    }
}
```

운영 기준:

- Request DTO에 `stream: true` 포함
- WebClient Read Timeout 설정
- Stream Error Mapping
- Client Disconnect 처리
- Backpressure 고려
- 최종 응답 저장 필요 시 별도 누적
- Secret 로그 출력 금지

주의:

- `.block()`으로 Streaming을 막지 않는다.
- Flux 내부 Error를 사용자 친화적 Event로 변환한다.
- Proxy Buffering 설정을 확인한다.
- 대량 동시 Streaming은 Connection 자원을 많이 사용한다.
- Spring MVC 환경에서는 ResponseEmitter 또는 SseEmitter를 사용할 수 있다.

---

### [FAQ]

Q. Spring Boot에서 LLM Streaming은 어떻게 처리해?

A. WebClient로 Streaming 응답을 Flux로 받고, Controller에서 `text/event-stream`으로 전달할 수 있다.

Q. Streaming에서 `.block()`을 써도 돼?

A. 권장하지 않는다. Streaming 흐름을 막을 수 있으므로 Flux 기반으로 처리하는 것이 좋다.

Q. Spring MVC에서도 Streaming이 가능해?

A. 가능하다. SseEmitter 또는 ResponseEmitter를 사용할 수 있다.

Q. WebClient Streaming에서 가장 중요한 설정은?

A. Timeout, Error Handling, `text/event-stream`, Client Disconnect 처리다.

---

## 3.3 JavaScript Streaming Client

### [개념]

JavaScript Streaming Client는 Browser 또는 Node.js에서 LLM Streaming Response를 받아 UI에 실시간 렌더링하는 구현 방식이다.

Browser에서는 `fetch` Stream, EventSource, ReadableStream을 사용할 수 있다.

---

### [핵심]

- Browser에서 LLM Provider API를 직접 호출하면 API Key가 노출된다.
- Frontend는 Backend Streaming Endpoint를 호출해야 한다.
- `fetch` Stream은 Chunk를 읽어 화면에 누적 렌더링할 수 있다.
- AbortController로 사용자 취소를 처리할 수 있다.
- 최종 응답과 Partial Output 상태를 구분해야 한다.

---

### [실무]

권장 구조:

```text
React Frontend
→ Backend Streaming API
→ LLM Provider Streaming API
→ Backend forwards chunks
→ React renders partial output
```

Browser Fetch Streaming 예:

```javascript
const controller = new AbortController();

const response = await fetch("/api/llm/stream", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    message: "Streaming 설명해줘.",
  }),
  signal: controller.signal,
});

if (!response.ok || !response.body) {
  throw new Error("Streaming request failed");
}

const reader = response.body.getReader();
const decoder = new TextDecoder("utf-8");

let finalText = "";

while (true) {
  const { value, done } = await reader.read();

  if (done) {
    break;
  }

  const chunk = decoder.decode(value, { stream: true });
  finalText += chunk;

  renderPartialText(finalText);
}

validateFinalText(finalText);
```

취소 처리 예:

```javascript
controller.abort();
```

주의:

- Frontend에 LLM API Key를 넣지 않는다.
- Chunk 경계가 JSON 경계와 일치한다고 가정하지 않는다.
- TextDecoder는 stream 옵션을 사용해 문자 깨짐을 줄인다.
- 네트워크 중단 시 Partial Output을 완료 답변으로 처리하지 않는다.
- React State 업데이트가 너무 잦으면 렌더링 성능 문제가 생길 수 있다.

---

### [FAQ]

Q. React에서 LLM Streaming을 직접 호출해도 돼?

A. LLM Provider API를 직접 호출하면 API Key가 노출되므로 Backend Streaming API를 통해 호출해야 한다.

Q. JavaScript에서 Streaming 응답은 어떻게 읽어?

A. `response.body.getReader()`로 Chunk를 읽고 TextDecoder로 문자열로 변환해 누적한다.

Q. 사용자가 Streaming을 취소할 수 있어?

A. AbortController를 사용해 취소할 수 있다.

Q. Chunk마다 React State를 업데이트해도 돼?

A. 가능하지만 너무 잦은 업데이트는 성능 문제가 생길 수 있어 조절이 필요하다.

---

# 4. Streaming Output Assembly

## 4.1 Chunk Accumulation

### [개념]

Chunk Accumulation은 Streaming Response로 받은 부분 Content를 순서대로 누적해 최종 응답을 만드는 과정이다.

Streaming Chunk는 완전한 문장, 완전한 Markdown, 완전한 JSON이 아닐 수 있다.

---

### [핵심]

- Chunk는 순서대로 누적해야 한다.
- 중복 Chunk를 방지해야 한다.
- 누적 Buffer와 UI 출력 상태를 구분해야 한다.
- 최종 응답은 Stream 종료 후 확정한다.
- Chunk 누적 중 오류가 발생하면 Partial Output 상태로 처리한다.
- 최종 응답 저장은 Validation 후 수행한다.

---

### [실무]

Chunk Accumulation Flow:

```text
Receive Chunk
→ Extract Content
→ Append Buffer
→ Render Partial
→ Check Stream End
→ Build Final Text
→ Validate Final Text
```

Buffer 관리 예:

```text
buffer = []

chunk content exists
→ buffer.append(content)

stream done
→ finalText = "".join(buffer)
→ validate(finalText)
```

상태 분리:

| 상태              | 설명           |
| ----------------- | -------------- |
| streaming         | Chunk 수신 중  |
| partial           | 일부 출력 존재 |
| completed         | 정상 종료      |
| cancelled         | 사용자 취소    |
| failed            | Stream 오류    |
| truncated         | 잘림 감지      |
| validation_failed | 최종 검증 실패 |

주의:

- Partial Output을 completed로 저장하지 않는다.
- Buffer가 비어 있으면 Empty Response로 처리한다.
- 중간 렌더링용 텍스트와 최종 저장용 텍스트를 구분한다.
- Markdown은 최종 응답 후 Required Section 검증이 필요할 수 있다.
- JSON은 최종 응답 후 Parse해야 한다.

---

### [FAQ]

Q. Chunk Accumulation이 뭐야?

A. Streaming으로 받은 부분 Content를 순서대로 누적해 최종 응답을 만드는 과정이다.

Q. Chunk마다 완전한 문장이라고 보면 돼?

A. 아니다. Chunk는 단어 일부나 문장 일부일 수 있다.

Q. Partial Output을 저장해도 돼?

A. 완료 상태와 구분해야 한다. 일반적으로 최종 검증된 응답만 확정 저장한다.

Q. Buffer가 비어 있으면?

A. Empty Response로 처리하고 재요청 또는 실패 처리를 한다.

---

## 4.2 Final Response Validation

### [개념]

Final Response Validation은 Streaming이 종료된 후 누적된 최종 응답이 사용 가능한지 검증하는 과정이다.

Streaming 중간 출력은 불완전하므로 최종 검증은 Stream 종료 후 수행해야 한다.

---

### [핵심]

- Streaming 응답도 Non-Streaming 응답처럼 검증해야 한다.
- Finish Reason을 확인한다.
- Empty Response를 확인한다.
- Markdown Required Section을 확인한다.
- JSON Output은 전체 Buffer를 파싱한다.
- RAG 답변은 Retrieved Context와 일치하는지 확인한다.
- 검증 실패 시 재요청, 작업 분할, 안전 실패 처리를 한다.

---

### [실무]

Final Validation Flow:

```text
Stream Done
→ Build Final Text
→ Empty Check
→ Finish Reason Check
→ Format Validation
→ Content Validation
→ Save or Return
```

검증 기준:

| Output Type  | Validation                   |
| ------------ | ---------------------------- |
| Plain Text   | Empty, Finish Reason         |
| Markdown     | Required Section, Code Block |
| JSON         | Parse, Schema Validation     |
| RAG Answer   | Context Match                |
| Code         | Syntax, Compile, Test        |
| Agent Output | Schema, Status, Next Action  |

RAG Streaming 검증 예:

```text
Final Answer Claim
→ Compare with Retrieved Context
→ Supported: return
→ Not Supported: missing information or regenerate
```

주의:

- Streaming 중 이미 사용자에게 보인 텍스트라도 최종 검증 실패가 가능하다.
- 검증 실패 시 UI에서 실패 상태를 명확히 표시한다.
- JSON Output Streaming은 최종 Buffer 기준으로만 파싱한다.
- `finish_reason=length`는 Truncated 상태로 처리한다.
- 최종 응답 저장 전 Secret 포함 여부를 확인한다.

---

### [FAQ]

Q. Final Response Validation이 뭐야?

A. Streaming 종료 후 누적된 최종 응답이 사용 가능한지 검증하는 과정이다.

Q. Streaming도 Finish Reason을 확인해야 해?

A. 그렇다. 정상 종료인지 잘림인지 확인해야 한다.

Q. JSON Streaming은 언제 파싱해?

A. 모든 Chunk를 누적한 최종 Buffer를 대상으로 파싱한다.

Q. RAG Streaming 답변은 어떻게 검증해?

A. 최종 답변의 핵심 주장과 Retrieved Context가 일치하는지 확인한다.

---

# 5. Streaming Error Handling

## 5.1 Streaming Timeout

### [개념]

Streaming Timeout은 Streaming 연결 또는 Chunk 수신이 일정 시간 안에 진행되지 않을 때 실패로 처리하는 기준이다.

Streaming은 긴 연결을 유지하므로 일반 API Timeout보다 세밀한 Timeout 설계가 필요하다.

Timeout 종류:

- Connection Timeout
- First Token Timeout
- Read Timeout
- Idle Timeout
- Total Stream Timeout
- Cancellation Timeout

---

### [핵심]

- Streaming은 전체 응답 시간이 길 수 있다.
- 첫 Token이 너무 늦으면 사용자 경험이 나쁘다.
- Chunk 간 대기 시간이 길면 연결 이상일 수 있다.
- Total Timeout이 없으면 연결이 무한 유지될 수 있다.
- Timeout 발생 시 Partial Output 상태를 명확히 처리해야 한다.

---

### [실무]

Streaming Timeout 기준:

| Timeout              | 설명                           |
| -------------------- | ------------------------------ |
| Connection Timeout   | 서버 연결까지 대기 시간        |
| First Token Timeout  | 첫 Chunk 수신까지 대기 시간    |
| Read Timeout         | Chunk 간 최대 대기 시간        |
| Idle Timeout         | 데이터 없이 연결 유지되는 시간 |
| Total Timeout        | 전체 Stream 최대 시간          |
| Cancellation Timeout | 취소 요청 후 종료 대기 시간    |

Timeout 처리 Flow:

```text
Open Stream
→ Wait First Chunk
→ Receive Chunks
→ Check Idle Time
→ Check Total Time
→ Timeout
→ Abort Stream
→ Mark Failed or Partial
```

처리 기준:

- Timeout 발생 시 LLM 요청을 중단한다.
- UI에 실패 또는 부분 완료 상태를 표시한다.
- 재시도는 Max Retry 내에서만 수행한다.
- 동일 요청 재시도 시 비용 중복 가능성을 고려한다.
- Timeout 로그에 model, latency, partial length를 기록한다.

주의:

- Timeout을 너무 짧게 잡으면 정상 긴 응답도 실패한다.
- Timeout을 너무 길게 잡으면 Connection 자원이 점유된다.
- Retry가 중복 응답과 중복 비용을 만들 수 있다.
- Streaming Timeout은 Provider별 응답 특성을 고려한다.

---

### [FAQ]

Q. Streaming Timeout이 뭐야?

A. Streaming 연결이나 Chunk 수신이 일정 시간 안에 진행되지 않을 때 실패로 처리하는 기준이다.

Q. Streaming Timeout은 일반 Timeout과 달라?

A. 그렇다. 전체 시간뿐 아니라 첫 Token, Chunk 간 대기 시간, Idle 시간을 따로 볼 수 있다.

Q. Timeout이 발생하면 Partial Output은 어떻게 해?

A. 완료 답변으로 처리하지 말고 partial 또는 failed 상태로 구분해야 한다.

Q. Timeout 후 Retry해도 돼?

A. 가능하지만 Max Retry를 제한하고 중복 비용과 중복 응답을 고려해야 한다.

---

## 5.2 Stream Cancellation

### [개념]

Stream Cancellation은 사용자가 Streaming 응답 생성을 중간에 중단하거나 시스템이 요청을 강제로 종료하는 처리이다.

Cancellation은 UX, 비용 절감, 서버 자원 보호에 필요하다.

---

### [핵심]

- 사용자는 긴 응답을 중간에 취소할 수 있어야 한다.
- Frontend 취소와 Backend 취소가 연결되어야 한다.
- Backend는 LLM Provider Stream도 중단해야 한다.
- 취소된 응답은 completed가 아니다.
- 취소 이벤트는 로그에 남긴다.

---

### [실무]

Cancellation Flow:

```text
User clicks Cancel
→ Frontend aborts request
→ Backend detects disconnect
→ Backend cancels LLM stream
→ Mark response cancelled
→ Release resources
```

상태 처리:

| 상태               | 처리               |
| ------------------ | ------------------ |
| user_cancelled     | 사용자가 취소      |
| server_cancelled   | 서버 정책으로 취소 |
| timeout_cancelled  | Timeout으로 취소   |
| provider_cancelled | Provider 연결 종료 |
| completed          | 정상 완료          |

Frontend 예:

```javascript
const controller = new AbortController();

fetch("/api/llm/stream", {
  method: "POST",
  body: JSON.stringify(payload),
  signal: controller.signal,
});

controller.abort();
```

주의:

- Frontend만 중단하고 Backend 요청을 유지하면 비용이 계속 발생할 수 있다.
- 취소된 Partial Output을 최종 답변으로 저장하지 않는다.
- 취소 후 재요청 시 이전 Partial Output과 새 Output을 구분한다.
- 취소 로그에 Secret이나 Prompt 전문을 남기지 않는다.

---

### [FAQ]

Q. Stream Cancellation이 뭐야?

A. Streaming 응답 생성을 중간에 중단하는 처리이다.

Q. 사용자가 취소하면 Backend도 멈춰야 해?

A. 그렇다. Backend와 LLM Provider 요청까지 중단해야 비용과 자원 낭비를 줄일 수 있다.

Q. 취소된 응답은 완료 답변이야?

A. 아니다. cancelled 상태로 구분해야 한다.

Q. 취소 후 다시 요청하면?

A. 새 요청으로 처리하고 이전 Partial Output과 혼합하지 않아야 한다.

---

## 5.3 Stream Failure

### [개념]

Stream Failure는 Streaming 중 네트워크 오류, Provider 오류, JSON 파싱 오류, 연결 끊김, Timeout 등이 발생하는 상황이다.

Stream Failure는 중간 출력이 존재할 수 있어 일반 API 실패보다 상태 관리가 중요하다.

---

### [핵심]

- Stream은 중간에 실패할 수 있다.
- 실패 시 Partial Output이 남을 수 있다.
- Partial Output을 완료 답변으로 처리하면 안 된다.
- Error Event와 Network Error를 구분한다.
- Retry는 비용과 중복 출력 가능성을 고려한다.
- 실패 로그에는 원인 분석 정보가 필요하다.

---

### [실무]

Stream Failure 처리 Flow:

```text
Receive Stream Error
→ Stop Accumulation
→ Mark Failed
→ Preserve Partial if Needed
→ Log Error Metadata
→ Retry or Return Failure
```

실패 유형:

| 유형              | 원인        | 처리                 |
| ----------------- | ----------- | -------------------- |
| Network Error     | 연결 끊김   | failed               |
| Timeout           | Chunk 지연  | timeout              |
| Provider Error    | 429, 500 등 | retry 가능 여부 판단 |
| Invalid Event     | 파싱 실패   | parser_error         |
| Content Filter    | 안전 정책   | blocked              |
| Client Disconnect | 사용자 이탈 | cancelled            |

Error Event 예:

```json
{
  "status": "failed",
  "errorCode": "stream_timeout",
  "message": "No chunk received within read timeout.",
  "partialLength": 820
}
```

주의:

- Retry 가능한 오류와 불가능한 오류를 구분한다.
- 400, 401, 403은 일반적으로 Retry하지 않는다.
- 429, 500, 502, 503, 504는 제한적 Retry 가능하다.
- 실패한 Stream의 Partial Output을 자동으로 이어붙이지 않는다.
- 장애 분석을 위해 requestId, model, latency, partialLength를 기록한다.

---

### [FAQ]

Q. Stream Failure는 뭐야?

A. Streaming 중 네트워크 오류, Provider 오류, Timeout, 파싱 오류 등이 발생하는 상황이다.

Q. Stream 실패 시 Partial Output은 어떻게 해?

A. 완료 답변으로 처리하지 않고 partial 또는 failed 상태로 구분한다.

Q. Stream 실패 후 Retry해도 돼?

A. 오류 유형에 따라 가능하다. 429, 500 계열은 제한적 Retry 가능하지만 인증 오류는 Retry하지 않는다.

Q. Stream Failure 로그에는 무엇을 남겨?

A. requestId, model, errorCode, latency, partialLength, retryCount를 남긴다.

---

# 6. Streaming with RAG and Agent

## 6.1 Streaming in RAG

### [개념]

Streaming in RAG는 검색된 문서 Context를 기반으로 생성되는 RAG 답변을 Streaming 방식으로 사용자에게 전달하는 구조이다.

RAG Streaming은 긴 설명형 답변에서 UX를 개선하지만, 최종 근거 검증이 필요하다.

RAG Streaming Flow:

```text
User Query
→ Retrieve Context
→ Build Grounded Prompt
→ Start Streaming
→ Render Partial Answer
→ Final Context Validation
→ Return Final State
```

---

### [핵심]

- RAG Streaming은 Retrieved Context를 먼저 확보한 뒤 시작한다.
- Streaming 중간 출력은 아직 검증되지 않은 상태이다.
- 최종 답변은 Retrieved Context와 일치해야 한다.
- 문서에 없는 내용이 생성되면 Missing Information 처리해야 한다.
- Citation 또는 Source 표시가 필요한 경우 최종 조립 후 처리한다.

---

### [실무]

RAG Streaming 설계 기준:

| 단계              | 처리                 |
| ----------------- | -------------------- |
| Query Rewrite     | Streaming 전 수행    |
| Retrieval         | Streaming 전 수행    |
| Context Filtering | Streaming 전 수행    |
| Prompt Assembly   | Streaming 전 수행    |
| Token Streaming   | 사용자에게 부분 출력 |
| Final Validation  | Streaming 후 수행    |
| Source Display    | 최종 응답 기준       |

Grounded Streaming Prompt 예:

```text
Rules:
- Answer only using Retrieved Context.
- Do not guess.
- If context is insufficient, say "문서에서 확인되지 않습니다."

Retrieved Context:
{context}

User Question:
{question}
```

주의:

- Retrieval 전에는 Streaming을 시작하지 않는다.
- Retrieved Context가 부족하면 Streaming 대신 Missing Information을 반환할 수 있다.
- 중간 출력에 Hallucination이 포함될 수 있으므로 최종 검증이 필요하다.
- Citation은 Chunk 누적 중간보다 최종 답변 기준으로 매핑한다.
- 긴 RAG 답변은 Max Tokens와 Timeout을 조정한다.

---

### [FAQ]

Q. RAG Streaming은 뭐야?

A. 검색된 문서 Context를 바탕으로 생성되는 답변을 Streaming 방식으로 전달하는 구조다.

Q. RAG Streaming은 언제 시작해?

A. Query Rewrite, Retrieval, Context Filtering이 끝난 뒤 시작한다.

Q. RAG Streaming도 검증이 필요해?

A. 그렇다. 최종 답변이 Retrieved Context와 일치하는지 확인해야 한다.

Q. Retrieved Context가 부족하면 Streaming을 해도 돼?

A. 보통은 Missing Information을 반환하거나 추가 검색을 수행하는 것이 안전하다.

---

## 6.2 Streaming in Agent Workflow

### [개념]

Streaming in Agent Workflow는 Agent가 생성하는 중간 결과 또는 최종 결과를 Streaming으로 사용자에게 전달하는 구조이다.

Agent Workflow에서는 모든 단계를 Streaming할 필요가 없다.

Streaming은 사용자에게 보여줄 최종 응답 또는 긴 생성 결과에 주로 적용한다.

---

### [핵심]

- 내부 Agent Output은 Non-Streaming JSON이 더 안정적일 수 있다.
- 사용자에게 보여줄 최종 답변은 Streaming에 적합하다.
- Tool Calling 결과는 Streaming 전에 완료되어야 할 수 있다.
- Agent Output Schema는 Streaming보다 완성 JSON이 안전하다.
- Review Agent 검증 전 Output을 확정하면 안 된다.

---

### [실무]

Agent Streaming 권장 구조:

```text
User Request
→ PM Agent Non-Streaming Structured Output
→ Tool / Retrieval
→ Backend Agent Non-Streaming or Streaming
→ Review Agent Non-Streaming Validation
→ Final Answer Streaming
```

적용 기준:

| Agent 작업               | Streaming 적합성 |
| ------------------------ | ---------------- |
| PM 계획 JSON             | 낮음             |
| Tool Arguments           | 낮음             |
| Search / Retrieval       | 낮음             |
| Code Generation          | 중간~높음        |
| Review JSON              | 낮음             |
| Final User Response      | 높음             |
| Long Document Generation | 높음             |

주의:

- 내부 Agent Schema Output은 Streaming 중 파싱이 어렵다.
- Tool Calling 인자가 Streaming 중간에 실행되면 위험하다.
- Review 전 코드를 사용자에게 확정 결과처럼 보여주지 않는다.
- Multi-Agent 상태 변경은 최종 검증 후 반영한다.
- Streaming은 UX 기능이지 검증 대체 수단이 아니다.

---

### [FAQ]

Q. Agent Workflow에서 Streaming은 어디에 쓰면 좋아?

A. 사용자에게 보여줄 최종 답변, 긴 코드 생성, 긴 문서 생성에 적합하다.

Q. Agent 내부 JSON Output도 Streaming하면 좋아?

A. 보통은 권장하지 않는다. 완성 JSON을 받은 뒤 Schema Validation하는 것이 안정적이다.

Q. Tool Calling과 Streaming을 같이 써도 돼?

A. 가능하지만 Tool Arguments는 완성 후 검증하고 실행해야 한다.

Q. Review Agent 전 결과를 Streaming으로 보여줘도 돼?

A. 보여줄 수는 있지만 확정 결과로 처리하면 안 된다.

---

# 7. Streaming Common Mistakes

## 7.1 Streaming Common Mistakes

### [개념]

Streaming Common Mistakes는 LLM Streaming Response를 처리할 때 발생하는 UX, 안정성, 파싱, 검증, 비용 관련 실수이다.

---

### [핵심]

자주 발생하는 실수:

- Streaming 중간 출력만 보고 완료 처리
- Chunk를 완전한 JSON으로 가정
- 최종 Buffer 조립 누락
- Finish Reason 확인 누락
- Empty Final Response 처리 누락
- Timeout 없이 긴 Stream 유지
- 사용자 취소 시 Backend Stream 미중단
- Partial Output을 최종 답변으로 저장
- JSON Output을 Chunk 단위로 파싱
- Tool Calling 인자를 Streaming 중간에 실행
- RAG Streaming에서 Retrieved Context 검증 누락
- Stream Failure와 User Cancellation을 구분하지 않음
- Frontend에 LLM API Key 노출
- Proxy Buffering으로 Streaming UX가 깨짐
- Usage Logging 누락

---

### [실무]

문제 진단 Flow:

```text
Streaming Output Problem
→ Check Request stream option
→ Check Response Content-Type
→ Check Chunk Parser
→ Check Buffer Accumulation
→ Check Finish Reason
→ Check Timeout
→ Check Cancellation
→ Check Final Validation
```

해결 기준:

| 문제               | 해결                                      |
| ------------------ | ----------------------------------------- |
| Chunk가 안 보임    | Proxy Buffering, Flush, Content-Type 확인 |
| JSON 파싱 실패     | 최종 Buffer 기준 파싱                     |
| 응답 중간 끊김     | Timeout, Network, Provider Error 확인     |
| 취소해도 비용 발생 | Backend와 Provider Stream도 중단          |
| Partial 저장됨     | 상태값 completed/cancelled/failed 분리    |
| RAG 오답           | Final Context Validation 적용             |
| Tool 실행 오류     | Tool Arguments 완성 후 검증               |
| UI 렌더링 느림     | State 업데이트 Throttling                 |

검수 Checklist:

```text
stream: true 설정이 명확한가?
Streaming Parser가 Provider Format에 맞는가?
Chunk Buffer를 순서대로 누적하는가?
Partial Output과 Final Output을 구분하는가?
Finish Reason을 확인하는가?
Timeout과 Cancellation이 있는가?
Final Response Validation이 있는가?
JSON Output은 최종 Buffer 기준으로 파싱하는가?
RAG 답변은 Retrieved Context와 일치하는가?
Tool Arguments는 완성 후 검증하는가?
API Key가 Frontend에 노출되지 않는가?
```

---

### [FAQ]

Q. Streaming 처리에서 가장 흔한 실수는?

A. 중간 Chunk를 완성 답변으로 처리하거나 최종 검증 없이 저장하는 것이다.

Q. Streaming JSON은 Chunk마다 파싱해도 돼?

A. 안 된다. 전체 Buffer를 조립한 뒤 최종 JSON을 파싱해야 한다.

Q. 사용자가 취소했는데 비용이 계속 나올 수 있어?

A. 가능하다. Backend와 LLM Provider Stream까지 중단하지 않으면 생성이 계속될 수 있다.

Q. Streaming이 안 되고 한 번에 출력되면?

A. Proxy Buffering, Content-Type, Flush 처리, Client Stream Parser를 확인해야 한다.

Q. Streaming은 검증을 대체해?

A. 아니다. Streaming은 UX 개선 방식이며 최종 응답 검증은 별도로 필요하다.

---

# Retrieval Queries

### [FAQ]

Q. Streaming Response가 뭐야?
A. LLM이 응답을 한 번에 반환하지 않고 Token 또는 Chunk를 순차적으로 전달하는 방식이다.

Q. Streaming을 쓰면 뭐가 좋아?
A. 긴 답변에서 사용자가 첫 출력까지 기다리는 체감 시간을 줄일 수 있다.

Q. Streaming은 전체 생성 시간을 줄여?
A. 반드시 그렇지는 않다. 전체 시간보다 첫 응답 체감 Latency를 줄이는 데 유리하다.

Q. Token Stream이 뭐야?
A. LLM이 생성하는 Token 또는 Text Delta가 순차적으로 전달되는 흐름이다.

Q. Chunk는 완전한 문장이야?
A. 아니다. Chunk는 단어 일부, 문장 일부, JSON 일부일 수 있다.

Q. Server-Sent Events가 뭐야?
A. 서버가 클라이언트에게 HTTP 연결을 유지하며 이벤트를 계속 보내는 단방향 스트리밍 방식이다.

Q. SSE와 WebSocket 차이는?
A. SSE는 서버에서 클라이언트로 보내는 단방향 스트림이고 WebSocket은 양방향 통신이다.

Q. `stream: true`는 뭐야?
A. LLM API가 응답을 Chunk 단위로 순차 전송하도록 요청하는 설정이다.

Q. Streaming Response는 일반 Response와 같아?
A. 아니다. Streaming은 Chunk 또는 Event 단위로 오므로 별도 파서가 필요하다.

Q. Streaming Request Design에서 중요한 것은?
A. Timeout, Cancellation, Buffer, Partial Render, Final Validation, Error Handling이다.

Q. Python에서 LLM Streaming은 어떻게 처리해?
A. 응답을 Line 또는 Event 단위로 읽고 Delta Content를 Buffer에 누적한다.

Q. Spring Boot에서 LLM Streaming은 어떻게 처리해?
A. WebClient로 Streaming 응답을 Flux로 받고 `text/event-stream`으로 전달할 수 있다.

Q. React에서 LLM Streaming을 직접 호출해도 돼?
A. LLM Provider API를 직접 호출하면 API Key가 노출되므로 Backend Streaming API를 통해 호출해야 한다.

Q. JavaScript에서 Streaming 응답은 어떻게 읽어?
A. `response.body.getReader()`와 TextDecoder로 Chunk를 읽고 누적한다.

Q. Chunk Accumulation이 뭐야?
A. Streaming으로 받은 부분 Content를 순서대로 누적해 최종 응답을 만드는 과정이다.

Q. Partial Output을 저장해도 돼?
A. 완료 상태와 구분해야 하며 일반적으로 최종 검증된 응답만 확정 저장한다.

Q. Final Response Validation이 뭐야?
A. Streaming 종료 후 누적된 최종 응답이 사용 가능한지 검증하는 과정이다.

Q. Streaming JSON은 언제 파싱해?
A. 모든 Chunk를 누적한 최종 Buffer를 대상으로 파싱한다.

Q. Streaming Timeout이 뭐야?
A. Streaming 연결이나 Chunk 수신이 일정 시간 안에 진행되지 않을 때 실패로 처리하는 기준이다.

Q. Stream Cancellation이 뭐야?
A. 사용자가 Streaming 응답 생성을 중간에 중단하거나 시스템이 요청을 종료하는 처리이다.

Q. 사용자가 취소하면 Backend도 멈춰야 해?
A. 그렇다. Backend와 LLM Provider 요청까지 중단해야 비용과 자원 낭비를 줄일 수 있다.

Q. Stream Failure는 뭐야?
A. Streaming 중 네트워크 오류, Provider 오류, Timeout, 파싱 오류 등이 발생하는 상황이다.

Q. Stream 실패 시 Partial Output은 어떻게 해?
A. 완료 답변으로 처리하지 않고 partial 또는 failed 상태로 구분한다.

Q. RAG Streaming은 뭐야?
A. 검색된 문서 Context를 바탕으로 생성되는 답변을 Streaming 방식으로 전달하는 구조다.

Q. RAG Streaming은 언제 시작해?
A. Query Rewrite, Retrieval, Context Filtering이 끝난 뒤 시작한다.

Q. RAG Streaming도 검증이 필요해?
A. 그렇다. 최종 답변이 Retrieved Context와 일치하는지 확인해야 한다.

Q. Agent Workflow에서 Streaming은 어디에 쓰면 좋아?
A. 사용자에게 보여줄 최종 답변, 긴 코드 생성, 긴 문서 생성에 적합하다.

Q. Agent 내부 JSON Output도 Streaming하면 좋아?
A. 보통은 권장하지 않는다. 완성 JSON을 받은 뒤 Schema Validation하는 것이 안정적이다.

Q. Tool Calling과 Streaming을 같이 써도 돼?
A. 가능하지만 Tool Arguments는 완성 후 검증하고 실행해야 한다.

Q. Streaming 처리에서 가장 흔한 실수는?
A. 중간 Chunk를 완성 답변으로 처리하거나 최종 검증 없이 저장하는 것이다.

Q. Streaming은 검증을 대체해?
A. 아니다. Streaming은 UX 개선 방식이며 최종 응답 검증은 별도로 필요하다.
