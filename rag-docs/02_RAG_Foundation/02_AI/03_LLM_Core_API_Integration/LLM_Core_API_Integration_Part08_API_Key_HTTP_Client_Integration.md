# LLM Core & API Integration Part08 - API Key & HTTP Client Integration

---

# 1. API Key and Secret Management

## 1.1 API Key

### [개념]

API Key는 LLM API Provider가 Client를 인증하고 사용량을 추적하기 위해 발급하는 Secret 값이다.

API Key는 외부 서비스 호출 권한을 가진 민감정보이다.

API Key는 코드, Frontend Bundle, Git Repository, 로그, 공유 문서에 노출되면 안 된다.

API Key 사용 Flow:

```text
Application
→ Load API Key from Environment Variable
→ Set Authorization Header
→ Call LLM API
→ Track Usage
```

---

### [핵심]

- API Key는 Secret이다.
- API Key는 코드에 하드코딩하지 않는다.
- API Key는 환경변수 또는 Secret Manager로 관리한다.
- API Key는 Frontend에 포함하지 않는다.
- API Key는 로그에 출력하지 않는다.
- API Key 노출 시 즉시 폐기하고 재발급한다.
- API Key에는 사용량 제한과 권한 제한을 적용한다.
- API Key 사용량은 비용 관리와 보안 모니터링에 필요하다.

---

### [실무]

Python API Key 로딩 예:

```python
import os

api_key = os.environ.get("LLM_API_KEY")

if not api_key:
    raise ValueError("LLM_API_KEY is required")
```

Spring Boot 설정 예:

```properties
llm.api-key=${LLM_API_KEY}
```

Spring Boot 주입 예:

```java
@Service
public class LlmClient {

    private final String apiKey;

    public LlmClient(@Value("${llm.api-key}") String apiKey) {
        if (apiKey == null || apiKey.isBlank()) {
            throw new IllegalStateException("LLM API key is required");
        }

        this.apiKey = apiKey;
    }
}
```

금지 예:

```java
private static final String API_KEY = "sk-live-secret-key";
```

API Key 관리 기준:

| 항목              | 기준                            |
| ----------------- | ------------------------------- |
| Local Development | `.env`, OS 환경변수             |
| Production        | Secret Manager, CI/CD Secret    |
| Git               | `.gitignore` 적용               |
| Logging           | Authorization Header 제거       |
| Rotation          | 노출 또는 주기 정책에 따라 교체 |
| Usage Limit       | 비용 폭주 방지                  |
| Permission        | 최소 권한 적용                  |
| Frontend          | 절대 포함 금지                  |

주의:

- `.env` 파일은 Git에 올리지 않는다.
- API Key를 Slack, Notion, 문서, 캡처 이미지에 노출하지 않는다.
- Frontend 환경변수는 Browser Bundle에 포함될 수 있다.
- Error Log에 Request Header가 남지 않도록 Redaction한다.
- 테스트 코드에도 실제 API Key를 하드코딩하지 않는다.

---

### [FAQ]

Q. API Key가 뭐야?

A. LLM API Provider가 Client를 인증하고 사용량을 추적하기 위해 발급하는 Secret 값이다.

Q. API Key를 코드에 넣어도 돼?

A. 안 된다. 코드에 하드코딩하면 Git, 빌드 결과, 로그를 통해 노출될 수 있다.

Q. API Key는 어디에 저장해야 해?

A. 환경변수, `.env`, Secret Manager, CI/CD Secret에 저장해야 한다.

Q. API Key가 노출되면 어떻게 해?

A. 즉시 폐기하고 새 Key를 발급한 뒤 노출 경로와 사용 로그를 확인해야 한다.

Q. Frontend에 API Key를 넣으면 왜 위험해?

A. Browser Bundle과 Network 요청에서 사용자에게 API Key가 노출될 수 있기 때문이다.

---

## 1.2 Environment Variable

### [개념]

Environment Variable은 운영체제나 실행 환경에서 Application에 전달하는 설정 값이다.

LLM API Integration에서는 API Key, Base URL, Model Name, Timeout, Rate Limit 설정을 환경변수로 관리할 수 있다.

Environment Variable 사용 대상:

- LLM_API_KEY
- LLM_BASE_URL
- LLM_MODEL
- LLM_TIMEOUT_SECONDS
- LLM_MAX_RETRIES
- EMBEDDING_MODEL
- VECTOR_DB_URL

---

### [핵심]

- 환경변수는 코드와 설정 값을 분리한다.
- 환경별 설정을 다르게 관리할 수 있다.
- Secret은 환경변수나 Secret Manager로 주입한다.
- 환경변수가 없을 때 Fail Fast 처리한다.
- 기본값을 줄 수 있는 값과 반드시 필요한 값을 구분한다.
- 환경변수 이름은 일관되게 관리한다.

---

### [실무]

`.env` 예:

```env
LLM_API_KEY=your-secret-key
LLM_BASE_URL=https://api.example.com/v1
LLM_MODEL=model-name
LLM_TIMEOUT_SECONDS=30
LLM_MAX_RETRIES=3
```

Python 설정 로딩 예:

```python
import os

class LlmSettings:
    def __init__(self):
        self.api_key = os.environ.get("LLM_API_KEY")
        self.base_url = os.environ.get("LLM_BASE_URL", "https://api.example.com/v1")
        self.model = os.environ.get("LLM_MODEL", "model-name")
        self.timeout_seconds = int(os.environ.get("LLM_TIMEOUT_SECONDS", "30"))

        if not self.api_key:
            raise ValueError("LLM_API_KEY is required")
```

Spring Boot `application.yml` 예:

```yaml
llm:
  api-key: ${LLM_API_KEY}
  base-url: ${LLM_BASE_URL:https://api.example.com/v1}
  model: ${LLM_MODEL:model-name}
  timeout-seconds: ${LLM_TIMEOUT_SECONDS:30}
```

`.gitignore` 예:

```gitignore
.env
.env.local
.env.production
application-secret.yml
```

환경변수 분류:

| 설정                | Secret 여부 | 기본값 가능 |
| ------------------- | ----------- | ----------- |
| LLM_API_KEY         | Secret      | 불가        |
| LLM_BASE_URL        | Non-Secret  | 가능        |
| LLM_MODEL           | Non-Secret  | 가능        |
| LLM_TIMEOUT_SECONDS | Non-Secret  | 가능        |
| LLM_MAX_RETRIES     | Non-Secret  | 가능        |
| VECTOR_DB_API_KEY   | Secret      | 불가        |

주의:

- Secret 환경변수 값을 로그에 출력하지 않는다.
- `.env`는 로컬 개발용이며 운영에서는 Secret Manager를 우선한다.
- Frontend의 `REACT_APP_`, `VITE_` 환경변수는 사용자에게 노출될 수 있다.
- 환경변수 누락은 Application 시작 시점에 감지하는 것이 좋다.
- Config 변경 시 재시작 또는 Reload 정책을 정한다.

---

### [FAQ]

Q. Environment Variable은 뭐야?

A. 실행 환경에서 Application에 전달하는 설정 값이다.

Q. LLM API 연동에서 환경변수는 왜 필요해?

A. API Key와 환경별 설정을 코드와 분리해 안전하게 관리하기 위해 필요하다.

Q. 환경변수가 없으면 어떻게 처리해?

A. 필수 Secret이 없으면 Application 시작 또는 API 호출 전에 Fail Fast 처리해야 한다.

Q. `.env` 파일은 Git에 올려도 돼?

A. 안 된다. `.env`에는 Secret이 포함될 수 있으므로 `.gitignore`에 추가해야 한다.

Q. Frontend 환경변수는 안전해?

A. 아니다. Frontend 빌드에 포함되는 환경변수는 Browser에서 노출될 수 있다.

---

## 1.3 Secret Rotation

### [개념]

Secret Rotation은 API Key, Token, Password 같은 Secret 값을 폐기하고 새 값으로 교체하는 운영 절차이다.

Secret Rotation은 노출 사고 대응, 보안 정책 준수, 권한 관리에 필요하다.

Rotation 대상:

- LLM API Key
- Embedding API Key
- Vector DB API Key
- OAuth Client Secret
- Database Password
- CI/CD Deploy Token

---

### [핵심]

- API Key 노출 시 즉시 Rotation한다.
- 정기 Rotation 정책을 둘 수 있다.
- Rotation 중 서비스 중단을 최소화해야 한다.
- 이전 Key와 새 Key의 동시 유효 기간을 짧게 관리한다.
- Rotation 후 사용 로그를 확인한다.
- 노출된 Key는 반드시 폐기한다.
- Rotation 절차는 문서화한다.

---

### [실무]

Secret Rotation Flow:

```text
Detect Exposure
→ Disable Old Key
→ Create New Key
→ Update Secret Store
→ Restart or Reload Application
→ Verify API Call
→ Audit Usage Logs
```

운영 Rotation Flow:

```text
Create New Key
→ Store New Key
→ Deploy Application
→ Verify New Key Usage
→ Disable Old Key
→ Monitor Error Rate
```

Rotation Checklist:

```text
새 API Key를 발급했는가?
Secret Manager 또는 환경변수를 갱신했는가?
Application이 새 Key를 사용하는가?
기존 Key를 폐기했는가?
401 오류가 증가하지 않는가?
비정상 사용량이 없는가?
노출 원인을 제거했는가?
```

주의:

- 새 Key 적용 전에 기존 Key를 폐기하면 장애가 발생할 수 있다.
- Rotation 후 Application 재시작이 필요할 수 있다.
- CI/CD Secret과 Runtime Secret을 모두 확인한다.
- 노출된 Key를 단순히 숨기는 것으로 끝내면 안 된다.
- Rotation 로그에는 Key 값을 직접 기록하지 않는다.

---

### [FAQ]

Q. Secret Rotation이 뭐야?

A. API Key 같은 Secret을 폐기하고 새 값으로 교체하는 운영 절차다.

Q. API Key가 노출되면 Rotation이 필요해?

A. 반드시 필요하다. 노출된 Key는 더 이상 신뢰할 수 없다.

Q. Rotation 중 장애를 줄이려면?

A. 새 Key를 먼저 적용하고 정상 동작을 확인한 뒤 기존 Key를 폐기한다.

Q. Rotation 후 무엇을 확인해야 해?

A. API 호출 성공 여부, 401 오류, 사용량 로그, 비정상 호출 여부를 확인해야 한다.

---

# 2. HTTP Client Integration

## 2.1 HTTP Client

### [개념]

HTTP Client는 Application이 LLM API Provider로 HTTP Request를 보내고 Response를 받기 위해 사용하는 구성 요소이다.

LLM API는 일반적으로 HTTPS 기반 REST API 또는 OpenAI-compatible API 구조를 제공한다.

HTTP Client가 처리하는 항목:

- Base URL
- Endpoint
- Method
- Header
- Authorization
- JSON Body
- Timeout
- Retry
- Response Parsing
- Error Mapping
- Logging

---

### [핵심]

- LLM API 호출은 HTTP Client 계층으로 분리한다.
- Authorization Header에 API Key를 넣는다.
- JSON Request Body를 전송한다.
- Timeout을 반드시 설정한다.
- HTTP Status Code를 확인한다.
- Error Body를 안전하게 처리한다.
- Response DTO와 Error DTO를 분리한다.
- Provider별 차이는 Adapter로 흡수한다.

---

### [실무]

HTTP Request 기본 구조:

```text
POST /v1/chat/completions
Host: api.example.com
Authorization: Bearer ${LLM_API_KEY}
Content-Type: application/json

{
  "model": "model-name",
  "messages": []
}
```

HTTP Client 계층 구조:

```text
Controller
→ Service
→ LlmClient
→ HttpClient
→ LLM Provider API
```

HTTP Client 책임:

| 책임            | 설명                        |
| --------------- | --------------------------- |
| Request Build   | URL, Header, Body 구성      |
| Secret Handling | API Key 주입, 로그 제거     |
| Timeout         | 무한 대기 방지              |
| Status Check    | 2xx, 4xx, 5xx 분기          |
| Response Parse  | 성공 응답 파싱              |
| Error Mapping   | 오류 응답 변환              |
| Retry           | 일시적 오류 재시도          |
| Logging         | Usage, Latency, Status 기록 |

주의:

- Controller에서 직접 LLM API를 호출하지 않는다.
- API Key를 Service 여러 곳에 흩뿌리지 않는다.
- Timeout 없는 HTTP 요청을 만들지 않는다.
- Provider 응답 구조를 Domain Service가 직접 알게 하지 않는다.
- Error Body에 민감정보가 있을 수 있으므로 로그를 제한한다.

---

### [FAQ]

Q. HTTP Client는 뭐야?

A. Application이 LLM API로 HTTP Request를 보내고 Response를 받는 구성 요소다.

Q. LLM API 호출을 별도 Client로 분리해야 해?

A. 권장한다. 인증, Timeout, Error Handling, Logging을 한 곳에서 관리할 수 있기 때문이다.

Q. Authorization Header에는 무엇을 넣어?

A. 일반적으로 `Bearer {API_KEY}` 형식으로 API Key를 넣는다.

Q. Controller에서 바로 LLM API를 호출해도 돼?

A. 가능은 하지만 권장하지 않는다. Client 계층으로 분리하는 것이 유지보수와 테스트에 좋다.

---

## 2.2 Request Header

### [개념]

Request Header는 HTTP 요청의 Metadata를 전달하는 영역이다.

LLM API 호출에서는 Authorization, Content-Type, Accept, Request ID 같은 Header가 중요하다.

주요 Header:

- Authorization
- Content-Type
- Accept
- User-Agent
- X-Request-ID
- Idempotency-Key
- Retry-After
- Accept-Encoding

---

### [핵심]

- Authorization Header는 API Key 인증에 사용한다.
- Content-Type은 보통 `application/json`이다.
- Streaming 요청은 Accept Header에 `text/event-stream`을 사용할 수 있다.
- Request ID는 추적과 로깅에 유용하다.
- Idempotency-Key는 중복 실행 방지에 사용할 수 있다.
- Authorization Header는 로그에서 반드시 제거한다.

---

### [실무]

일반 Chat Completion Header 예:

```text
Authorization: Bearer ${LLM_API_KEY}
Content-Type: application/json
Accept: application/json
X-Request-ID: req-20260630-001
```

Streaming Header 예:

```text
Authorization: Bearer ${LLM_API_KEY}
Content-Type: application/json
Accept: text/event-stream
X-Request-ID: req-stream-001
```

Header 처리 기준:

| Header          | 용도                 |
| --------------- | -------------------- |
| Authorization   | API 인증             |
| Content-Type    | 요청 Body 형식       |
| Accept          | 응답 형식            |
| X-Request-ID    | 요청 추적            |
| Idempotency-Key | 중복 실행 방지       |
| User-Agent      | Client 식별          |
| Retry-After     | Rate Limit 대기 기준 |

Spring WebClient Header 예:

```java
webClient.post()
        .uri("/chat/completions")
        .header(HttpHeaders.AUTHORIZATION, "Bearer " + apiKey)
        .contentType(MediaType.APPLICATION_JSON)
        .accept(MediaType.APPLICATION_JSON)
        .bodyValue(request);
```

주의:

- Authorization Header를 로그로 남기지 않는다.
- API Key를 Query Parameter로 전달하지 않는다.
- Streaming 요청과 일반 요청의 Accept Header를 구분한다.
- Idempotency-Key가 필요한 쓰기 작업은 중복 요청을 고려한다.
- Provider별 Custom Header 요구사항을 문서화한다.

---

### [FAQ]

Q. Request Header는 뭐야?

A. HTTP 요청의 인증, 형식, 추적 정보 같은 Metadata를 전달하는 영역이다.

Q. LLM API에서 가장 중요한 Header는?

A. Authorization과 Content-Type이다.

Q. Streaming 요청에서는 어떤 Header가 필요해?

A. 일반적으로 `Accept: text/event-stream`을 사용할 수 있다.

Q. API Key를 Query Parameter로 보내도 돼?

A. 권장하지 않는다. URL 로그나 브라우저 기록에 노출될 수 있다.

Q. Authorization Header는 로그에 남겨도 돼?

A. 안 된다. 반드시 Redaction해야 한다.

---

## 2.3 JSON Request Body

### [개념]

JSON Request Body는 LLM API에 전달되는 요청 데이터이다.

Chat Completion, Embedding, Tool Calling, Streaming 요청은 대부분 JSON Body로 전송된다.

주요 Body 요소:

- model
- messages
- input
- temperature
- max_tokens
- stream
- tools
- tool_choice
- response_format
- metadata

---

### [핵심]

- JSON Body는 API Provider Schema에 맞아야 한다.
- 필수 필드 누락 시 400 Bad Request가 발생할 수 있다.
- Provider가 지원하지 않는 필드를 보내면 실패할 수 있다.
- Request DTO를 사용해 Body 구조를 통제한다.
- Secret은 Body에 넣지 않는다.
- User Input과 System Rule을 구분한다.

---

### [실무]

Chat Completion Request Body 예:

```json
{
  "model": "model-name",
  "messages": [
    {
      "role": "system",
      "content": "You are a backend development assistant."
    },
    {
      "role": "user",
      "content": "LLM API Timeout 처리 방법을 설명해줘."
    }
  ],
  "temperature": 0.2,
  "max_tokens": 1200
}
```

Embedding Request Body 예:

```json
{
  "model": "embedding-model-name",
  "input": [
    "Embedding은 텍스트를 Vector로 변환한다.",
    "RAG는 검색된 Context를 Prompt에 넣는다."
  ]
}
```

Tool Calling Request Body 예:

```json
{
  "model": "model-name",
  "messages": [],
  "tools": [
    {
      "name": "retrieve_rag_context",
      "description": "Retrieve RAG document chunks.",
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
  ]
}
```

Request Body 검증 기준:

| 항목            | 검증                  |
| --------------- | --------------------- |
| model           | 허용 모델인지 확인    |
| messages        | 비어 있지 않은지 확인 |
| input           | Empty Text 제외       |
| temperature     | 허용 범위             |
| max_tokens      | 허용 범위             |
| tools           | Schema 유효성         |
| response_format | Provider 지원 여부    |
| stream          | Boolean 값            |

주의:

- User Input을 검증 없이 System Message에 넣지 않는다.
- Prompt Injection이 Request Body에 포함될 수 있다.
- `max_tokens`를 너무 작게 설정하지 않는다.
- JSON Output 요청은 응답 검증까지 함께 설계한다.
- Provider별 Request Body 차이를 Adapter로 분리한다.

---

### [FAQ]

Q. JSON Request Body는 뭐야?

A. LLM API에 전달하는 모델, 메시지, 파라미터, Tool 정의 같은 요청 데이터다.

Q. Request Body 검증이 왜 필요해?

A. 필수 필드 누락, 지원하지 않는 필드, 잘못된 Parameter를 사전에 막기 위해 필요하다.

Q. Secret을 Request Body에 넣어도 돼?

A. 안 된다. API Key와 Secret은 Authorization Header나 Secret 관리 체계에서 처리해야 한다.

Q. Provider마다 Request Body가 달라?

A. 그렇다. OpenAI-compatible 구조라도 세부 필드와 지원 기능이 다를 수 있다.

---

# 3. Python HTTP Integration

## 3.1 Python requests Client

### [개념]

Python `requests` Client는 Python Application에서 LLM API를 호출하는 간단한 HTTP Client 구현 방식이다.

`requests`는 동기 방식이며 Chat Completion, Embedding, Tool Calling 요청에 사용할 수 있다.

---

### [핵심]

- API Key는 환경변수에서 읽는다.
- Authorization Header를 설정한다.
- JSON Body를 전송한다.
- Timeout을 반드시 설정한다.
- `raise_for_status()`로 HTTP 오류를 감지한다.
- Response JSON을 파싱하고 검증한다.
- Secret을 로그에 남기지 않는다.

---

### [실무]

Python Chat Completion Client 예:

```python
import os
import requests

class LlmClient:
    def __init__(self):
        self.api_key = os.environ.get("LLM_API_KEY")
        self.base_url = os.environ.get("LLM_BASE_URL", "https://api.example.com/v1")
        self.model = os.environ.get("LLM_MODEL", "model-name")

        if not self.api_key:
            raise ValueError("LLM_API_KEY is required")

    def chat(self, messages: list[dict]) -> str:
        response = requests.post(
            f"{self.base_url}/chat/completions",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": self.model,
                "messages": messages,
                "temperature": 0.2,
                "max_tokens": 1200
            },
            timeout=30
        )

        response.raise_for_status()
        data = response.json()

        choices = data.get("choices") or []
        if not choices:
            raise ValueError("Empty choices")

        message = choices[0].get("message") or {}
        content = message.get("content")

        if not content:
            raise ValueError("Empty LLM content")

        finish_reason = choices[0].get("finish_reason")
        if finish_reason == "length":
            raise ValueError("LLM response was truncated")

        return content
```

Embedding Client 예:

```python
def embed_text(text: str) -> list[float]:
    if not text or not text.strip():
        raise ValueError("Embedding input text is empty")

    response = requests.post(
        f"{base_url}/embeddings",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": "embedding-model-name",
            "input": text
        },
        timeout=30
    )

    response.raise_for_status()
    data = response.json()

    embedding = data["data"][0]["embedding"]
    if not embedding:
        raise ValueError("Empty embedding vector")

    return embedding
```

주의:

- `requests.post()`에 Timeout을 반드시 넣는다.
- `response.json()` 실패를 처리한다.
- `choices[0]` 직접 접근 전 검증한다.
- Production에서는 Error Mapping 계층을 둔다.
- Retry는 `tenacity` 같은 라이브러리로 제한적으로 적용할 수 있다.

---

### [FAQ]

Q. Python에서 LLM API는 어떻게 호출해?

A. `requests` 또는 `httpx`로 Authorization Header, JSON Body, Timeout을 설정해 호출한다.

Q. `requests` Client에서 가장 중요한 설정은?

A. API Key 환경변수 로딩, Timeout, HTTP Status 확인, Response Validation이다.

Q. `response.raise_for_status()`는 왜 사용해?

A. 4xx와 5xx HTTP 오류를 예외로 처리하기 위해 사용한다.

Q. `choices[0]`를 바로 읽어도 돼?

A. 권장하지 않는다. choices가 비어 있을 수 있으므로 먼저 검증해야 한다.

---

## 3.2 Python httpx Client

### [개념]

Python `httpx` Client는 동기와 비동기를 모두 지원하는 HTTP Client이다.

`httpx`는 Async LLM API 호출, 동시 요청, Timeout 제어, Connection Pool 관리에 유용하다.

---

### [핵심]

- `httpx.Client` 또는 `httpx.AsyncClient`를 사용할 수 있다.
- Timeout을 세밀하게 설정할 수 있다.
- Async 작업에 적합하다.
- Connection Pool을 재사용할 수 있다.
- Streaming Response도 처리할 수 있다.
- Response Validation은 별도로 필요하다.

---

### [실무]

Async Chat Client 예:

```python
import os
import httpx

class AsyncLlmClient:
    def __init__(self):
        self.api_key = os.environ.get("LLM_API_KEY")
        self.base_url = os.environ.get("LLM_BASE_URL", "https://api.example.com/v1")
        self.model = os.environ.get("LLM_MODEL", "model-name")

        if not self.api_key:
            raise ValueError("LLM_API_KEY is required")

    async def chat(self, messages: list[dict]) -> str:
        timeout = httpx.Timeout(connect=5.0, read=30.0, write=10.0, pool=5.0)

        async with httpx.AsyncClient(timeout=timeout) as client:
            response = await client.post(
                f"{self.base_url}/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": self.model,
                    "messages": messages,
                    "temperature": 0.2,
                    "max_tokens": 1200
                }
            )

        response.raise_for_status()
        data = response.json()

        choices = data.get("choices") or []
        if not choices:
            raise ValueError("Empty choices")

        content = choices[0].get("message", {}).get("content")
        if not content:
            raise ValueError("Empty content")

        return content
```

Timeout 구성:

| Timeout | 설명                      |
| ------- | ------------------------- |
| connect | 서버 연결 시간            |
| read    | 응답 읽기 시간            |
| write   | 요청 전송 시간            |
| pool    | Connection Pool 대기 시간 |

사용 기준:

| 상황                | 권장              |
| ------------------- | ----------------- |
| 간단한 Script       | requests 가능     |
| Async Web Server    | httpx AsyncClient |
| 동시 Embedding 처리 | httpx AsyncClient |
| Streaming 처리      | httpx stream      |
| 세밀한 Timeout      | httpx             |

주의:

- Async 환경에서 동기 `requests`를 남용하지 않는다.
- AsyncClient를 요청마다 생성하면 Connection 재사용 이점이 줄어든다.
- Batch 요청은 Rate Limit을 고려한다.
- 비동기 호출도 Retry와 Timeout을 반드시 설정한다.
- Error Response를 사용자에게 그대로 노출하지 않는다.

---

### [FAQ]

Q. httpx는 언제 사용해?

A. 비동기 LLM API 호출, 동시 요청, 세밀한 Timeout 제어, Streaming 처리가 필요할 때 사용한다.

Q. requests와 httpx 차이는?

A. requests는 동기 중심이고 httpx는 동기와 비동기를 모두 지원한다.

Q. AsyncClient를 쓰면 자동으로 빠르고 안전해져?

A. 아니다. Timeout, Rate Limit, Retry, Response Validation을 별도로 설계해야 한다.

Q. httpx Timeout은 어떻게 나눠?

A. connect, read, write, pool Timeout을 분리해서 설정할 수 있다.

---

# 4. Java / Spring HTTP Integration

## 4.1 Spring WebClient

### [개념]

Spring WebClient는 Spring Framework에서 제공하는 HTTP Client이다.

WebClient는 비동기, Non-blocking, Streaming 응답 처리를 지원한다.

LLM API 연동에서는 Chat Completion, Embedding, Streaming, Tool Calling 요청을 WebClient로 처리할 수 있다.

---

### [핵심]

- WebClient는 LLM API 호출 Client로 적합하다.
- Base URL과 공통 Header를 설정할 수 있다.
- Request DTO와 Response DTO를 분리한다.
- Timeout 설정이 필요하다.
- Error Status Mapping이 필요하다.
- Streaming은 `Flux`로 처리할 수 있다.
- `.block()` 사용 여부는 Application 구조에 맞게 결정한다.

---

### [실무]

WebClient Bean 설정 예:

```java
@Configuration
public class LlmWebClientConfig {

    @Bean
    public WebClient llmWebClient(
            WebClient.Builder builder,
            @Value("${llm.base-url}") String baseUrl,
            @Value("${llm.api-key}") String apiKey
    ) {
        return builder
                .baseUrl(baseUrl)
                .defaultHeader(HttpHeaders.AUTHORIZATION, "Bearer " + apiKey)
                .defaultHeader(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_JSON_VALUE)
                .build();
    }
}
```

LlmClient 예:

```java
@Service
public class LlmClient {

    private final WebClient llmWebClient;
    private final String model;

    public LlmClient(
            WebClient llmWebClient,
            @Value("${llm.model}") String model
    ) {
        this.llmWebClient = llmWebClient;
        this.model = model;
    }

    public String chat(List<LlmMessage> messages) {
        LlmChatRequest request = new LlmChatRequest(
                model,
                messages,
                0.2,
                1200
        );

        LlmChatResponse response = llmWebClient.post()
                .uri("/chat/completions")
                .bodyValue(request)
                .retrieve()
                .onStatus(
                        status -> status.is4xxClientError() || status.is5xxServerError(),
                        clientResponse -> clientResponse.bodyToMono(String.class)
                                .map(body -> new LlmApiException("LLM API error: " + clientResponse.statusCode()))
                )
                .bodyToMono(LlmChatResponse.class)
                .block(Duration.ofSeconds(30));

        if (response == null || response.choices() == null || response.choices().isEmpty()) {
            throw new LlmApiException("Empty LLM response");
        }

        LlmChoice choice = response.choices().get(0);

        if ("length".equals(choice.finishReason())) {
            throw new LlmApiException("LLM response was truncated");
        }

        return choice.message().content();
    }
}
```

DTO 예:

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
        String finishReason
) {
}

public record LlmUsage(
        Integer prompt_tokens,
        Integer completion_tokens,
        Integer total_tokens
) {
}
```

주의:

- API Key를 Bean 설정 로그에 출력하지 않는다.
- `block()`은 WebFlux 이벤트 루프에서 사용하지 않는다.
- Timeout은 HTTP Client Connector 수준에서도 설정하는 것이 좋다.
- Provider Error Body를 그대로 사용자에게 노출하지 않는다.
- Response DTO는 Provider별 필드명 차이를 고려한다.

---

### [FAQ]

Q. Spring WebClient는 뭐야?

A. Spring에서 HTTP API를 호출하기 위한 Client이며 비동기와 Streaming 처리를 지원한다.

Q. Spring Boot에서 LLM API 연동에는 WebClient가 좋아?

A. 적합하다. Timeout, Header, Streaming, Error Mapping을 체계적으로 관리할 수 있다.

Q. `.block()`을 써도 돼?

A. Servlet 기반 동기 Service에서는 사용할 수 있지만 WebFlux 이벤트 루프에서는 피해야 한다.

Q. WebClient에서 Error Handling은 어디서 해?

A. `.retrieve().onStatus()` 또는 Exchange Filter에서 Status Code별로 처리할 수 있다.

---

## 4.2 Spring RestClient

### [개념]

Spring RestClient는 Spring Framework 6.1+에서 제공하는 동기 HTTP Client이다.

RestClient는 RestTemplate보다 현대적인 동기 API이며, Servlet 기반 Spring Boot Application에서 LLM API를 단순하게 호출할 때 사용할 수 있다.

---

### [핵심]

- RestClient는 동기 HTTP 호출에 적합하다.
- Servlet 기반 Application에서 사용하기 쉽다.
- Request DTO와 Response DTO를 사용할 수 있다.
- Timeout 설정이 필요하다.
- Error Status Mapping이 필요하다.
- Streaming 처리에는 WebClient가 더 적합하다.

---

### [실무]

RestClient Bean 예:

```java
@Configuration
public class LlmRestClientConfig {

    @Bean
    public RestClient llmRestClient(
            RestClient.Builder builder,
            @Value("${llm.base-url}") String baseUrl,
            @Value("${llm.api-key}") String apiKey
    ) {
        return builder
                .baseUrl(baseUrl)
                .defaultHeader(HttpHeaders.AUTHORIZATION, "Bearer " + apiKey)
                .defaultHeader(HttpHeaders.CONTENT_TYPE, MediaType.APPLICATION_JSON_VALUE)
                .build();
    }
}
```

RestClient 호출 예:

```java
@Service
public class LlmRestClient {

    private final RestClient restClient;
    private final String model;

    public LlmRestClient(
            RestClient restClient,
            @Value("${llm.model}") String model
    ) {
        this.restClient = restClient;
        this.model = model;
    }

    public String chat(List<LlmMessage> messages) {
        LlmChatRequest request = new LlmChatRequest(
                model,
                messages,
                0.2,
                1200
        );

        LlmChatResponse response = restClient.post()
                .uri("/chat/completions")
                .body(request)
                .retrieve()
                .body(LlmChatResponse.class);

        if (response == null || response.choices() == null || response.choices().isEmpty()) {
            throw new LlmApiException("Empty LLM response");
        }

        return response.choices().get(0).message().content();
    }
}
```

WebClient와 RestClient 비교:

| 항목           | WebClient             | RestClient |
| -------------- | --------------------- | ---------- |
| 방식           | 비동기 / Non-blocking | 동기       |
| Streaming      | 적합                  | 제한적     |
| Servlet App    | 사용 가능             | 적합       |
| WebFlux App    | 적합                  | 부적합     |
| 구현 난이도    | 중간                  | 낮음       |
| 대량 동시 요청 | 유리                  | 제한적     |

주의:

- RestClient도 Timeout 설정이 필요하다.
- Streaming이 필요하면 WebClient를 우선한다.
- 동기 호출은 Thread 점유를 고려해야 한다.
- Error Mapping을 생략하지 않는다.
- API Key가 로그에 노출되지 않도록 한다.

---

### [FAQ]

Q. Spring RestClient는 뭐야?

A. Spring Framework 6.1+에서 제공하는 현대적인 동기 HTTP Client다.

Q. RestClient는 언제 좋아?

A. Servlet 기반 Spring Boot에서 단순 동기 LLM API 호출을 구현할 때 좋다.

Q. RestClient와 WebClient 중 뭐가 좋아?

A. Streaming이나 비동기 처리가 필요하면 WebClient, 단순 동기 호출은 RestClient가 적합하다.

Q. RestClient도 Timeout이 필요해?

A. 필요하다. Timeout이 없으면 외부 API 지연 시 Thread가 오래 점유될 수 있다.

---

## 4.3 Spring ConfigurationProperties

### [개념]

ConfigurationProperties는 Spring Boot에서 설정 값을 타입 안전하게 바인딩하는 방식이다.

LLM API Integration에서는 API Key, Base URL, Model, Timeout, Retry, Embedding Model 설정을 하나의 설정 객체로 관리할 수 있다.

---

### [핵심]

- 설정 값을 타입 안전하게 관리할 수 있다.
- `@Value` 남용을 줄일 수 있다.
- 설정 그룹을 명확히 분리할 수 있다.
- Validation Annotation을 적용할 수 있다.
- 테스트에서 설정 객체를 주입하기 쉽다.
- Secret 값은 로그 출력에서 제외한다.

---

### [실무]

`application.yml` 예:

```yaml
llm:
  api-key: ${LLM_API_KEY}
  base-url: ${LLM_BASE_URL:https://api.example.com/v1}
  model: ${LLM_MODEL:model-name}
  embedding-model: ${EMBEDDING_MODEL:embedding-model-name}
  timeout-seconds: ${LLM_TIMEOUT_SECONDS:30}
  max-retries: ${LLM_MAX_RETRIES:3}
```

ConfigurationProperties 예:

```java
@ConfigurationProperties(prefix = "llm")
@Validated
public record LlmProperties(
        @NotBlank
        String apiKey,

        @NotBlank
        String baseUrl,

        @NotBlank
        String model,

        @NotBlank
        String embeddingModel,

        @Min(1)
        int timeoutSeconds,

        @Min(0)
        int maxRetries
) {
}
```

설정 활성화 예:

```java
@Configuration
@EnableConfigurationProperties(LlmProperties.class)
public class LlmConfig {
}
```

사용 예:

```java
@Service
public class LlmClient {

    private final LlmProperties properties;

    public LlmClient(LlmProperties properties) {
        this.properties = properties;
    }
}
```

주의:

- `toString()`으로 Secret이 로그에 찍히지 않도록 주의한다.
- Validation 실패는 Application 시작 시점에 발견하는 것이 좋다.
- Secret 기본값을 코드에 넣지 않는다.
- Profile별 설정이 충돌하지 않도록 한다.
- 운영 Secret은 `application.yml`에 직접 쓰지 않는다.

---

### [FAQ]

Q. ConfigurationProperties는 뭐야?

A. Spring Boot 설정 값을 타입 안전한 객체로 바인딩하는 방식이다.

Q. LLM 설정에 ConfigurationProperties를 쓰면 뭐가 좋아?

A. API Key, Base URL, Model, Timeout, Retry 설정을 한 곳에서 검증하고 관리할 수 있다.

Q. `@Value`와 뭐가 달라?

A. `@Value`는 개별 값 주입이고 ConfigurationProperties는 관련 설정을 객체로 묶어 관리한다.

Q. Secret 값이 로그에 찍히지 않게 하려면?

A. 설정 객체의 `toString()` 출력과 로그 설정을 주의하고 Secret을 직접 출력하지 않는다.

---

# 5. JavaScript / Node.js HTTP Integration

## 5.1 Node.js Fetch Client

### [개념]

Node.js Fetch Client는 Node.js Backend에서 `fetch`를 사용해 LLM API를 호출하는 방식이다.

Node.js Backend는 API Key를 서버 환경변수로 보호할 수 있다.

---

### [핵심]

- API Key는 `process.env`에서 읽는다.
- Browser가 아닌 Server Runtime에서 호출한다.
- Authorization Header를 설정한다.
- JSON Body를 전송한다.
- HTTP Status를 확인한다.
- Empty Response와 Finish Reason을 검증한다.
- Timeout 또는 AbortController를 사용한다.

---

### [실무]

Node.js Fetch Client 예:

```javascript
const apiKey = process.env.LLM_API_KEY;
const baseUrl = process.env.LLM_BASE_URL || "https://api.example.com/v1";
const model = process.env.LLM_MODEL || "model-name";

if (!apiKey) {
  throw new Error("LLM_API_KEY is required");
}

export async function chat(messages) {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), 30000);

  try {
    const response = await fetch(`${baseUrl}/chat/completions`, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${apiKey}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        model,
        messages,
        temperature: 0.2,
        max_tokens: 1200,
      }),
      signal: controller.signal,
    });

    if (!response.ok) {
      throw new Error(`LLM API failed with status ${response.status}`);
    }

    const data = await response.json();
    const choice = data.choices?.[0];

    if (!choice?.message?.content) {
      throw new Error("Empty LLM response");
    }

    if (choice.finish_reason === "length") {
      throw new Error("LLM response was truncated");
    }

    return choice.message.content;
  } finally {
    clearTimeout(timeoutId);
  }
}
```

Node.js Backend 구조:

```text
React Frontend
→ Node.js Backend API
→ LLM Provider API
→ Node.js Backend
→ React Frontend
```

주의:

- Browser에서 직접 LLM Provider를 호출하지 않는다.
- API Key를 `NEXT_PUBLIC_`, `VITE_`, `REACT_APP_` 환경변수에 넣지 않는다.
- AbortController로 Timeout과 사용자 취소를 처리한다.
- Error Message에 Secret을 포함하지 않는다.
- Provider 응답 구조를 검증한다.

---

### [FAQ]

Q. Node.js에서 LLM API는 어떻게 호출해?

A. 서버 환경에서 `fetch`로 Authorization Header, JSON Body, Timeout을 설정해 호출한다.

Q. Node.js에서는 API Key를 어디에 둬?

A. `process.env` 또는 Secret Manager에서 읽는다.

Q. Browser Fetch로 LLM API를 직접 호출해도 돼?

A. 안 된다. API Key가 사용자에게 노출될 수 있다.

Q. Node.js Fetch에서 Timeout은 어떻게 처리해?

A. AbortController와 setTimeout을 사용해 요청을 중단할 수 있다.

---

## 5.2 Axios Client

### [개념]

Axios Client는 JavaScript 또는 Node.js에서 HTTP API를 호출하는 라이브러리이다.

LLM API Integration에서는 Node.js Backend에서 Axios를 사용해 Chat Completion, Embedding, Tool Calling API를 호출할 수 있다.

---

### [핵심]

- Axios Instance로 Base URL과 Header를 관리한다.
- Request Interceptor에서 API Key를 주입할 수 있다.
- Response Interceptor에서 Error Mapping을 할 수 있다.
- Timeout 설정이 필요하다.
- Browser Axios에 LLM API Key를 넣으면 안 된다.
- Error Log에서 Authorization Header를 제거해야 한다.

---

### [실무]

Axios Instance 예:

```javascript
import axios from "axios";

const apiKey = process.env.LLM_API_KEY;

if (!apiKey) {
  throw new Error("LLM_API_KEY is required");
}

export const llmApi = axios.create({
  baseURL: process.env.LLM_BASE_URL || "https://api.example.com/v1",
  timeout: 30000,
  headers: {
    Authorization: `Bearer ${apiKey}`,
    "Content-Type": "application/json",
  },
});
```

Chat 호출 예:

```javascript
export async function chat(messages) {
  const response = await llmApi.post("/chat/completions", {
    model: process.env.LLM_MODEL || "model-name",
    messages,
    temperature: 0.2,
    max_tokens: 1200,
  });

  const choice = response.data?.choices?.[0];

  if (!choice?.message?.content) {
    throw new Error("Empty LLM response");
  }

  if (choice.finish_reason === "length") {
    throw new Error("LLM response was truncated");
  }

  return choice.message.content;
}
```

Interceptor Redaction 예:

```javascript
llmApi.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.config?.headers?.Authorization) {
      error.config.headers.Authorization = "[REDACTED]";
    }

    return Promise.reject(error);
  },
);
```

주의:

- Axios Error 객체에 Request Config가 포함될 수 있다.
- Request Header 로그에 API Key가 남지 않도록 Redaction한다.
- Browser Axios Instance에 Provider API Key를 넣지 않는다.
- Timeout과 Retry를 구분해서 설계한다.
- Streaming Response는 Fetch Stream이 더 적합할 수 있다.

---

### [FAQ]

Q. Axios로 LLM API를 호출해도 돼?

A. 가능하다. Node.js Backend에서 Axios Instance를 만들어 호출할 수 있다.

Q. Axios Instance를 쓰는 이유는?

A. Base URL, Header, Timeout, Error Handling을 공통으로 관리하기 위해서다.

Q. Axios Error 로그에서 주의할 점은?

A. Authorization Header와 API Key가 Error Config에 포함될 수 있으므로 Redaction해야 한다.

Q. Browser Axios에 API Key를 넣어도 돼?

A. 안 된다. Browser 코드에 포함된 API Key는 사용자에게 노출된다.

---

## 5.3 Frontend Proxy Pattern

### [개념]

Frontend Proxy Pattern은 React, Vue, Next.js Client가 LLM Provider API를 직접 호출하지 않고 Backend API를 통해 간접 호출하는 구조이다.

이 패턴은 API Key 보호, 권한 검증, Rate Limit, Logging, Response Validation에 필요하다.

Frontend Proxy Flow:

```text
Browser Frontend
→ Backend LLM Endpoint
→ LLM Provider API
→ Backend Validation
→ Browser Frontend
```

---

### [핵심]

- Frontend에는 LLM API Key를 넣지 않는다.
- Backend가 API Key를 보호한다.
- Backend가 사용자 인증과 권한을 확인한다.
- Backend가 Rate Limit을 적용한다.
- Backend가 Prompt와 Response를 검증한다.
- Backend가 Usage Logging을 수행한다.
- Streaming도 Backend를 통해 전달한다.

---

### [실무]

React 호출 예:

```javascript
async function askLlm(message) {
  const response = await fetch("/api/llm/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message }),
  });

  if (!response.ok) {
    throw new Error("LLM request failed");
  }

  return await response.json();
}
```

Backend 처리 Flow:

```text
Receive Frontend Request
→ Authenticate User
→ Validate User Input
→ Build Prompt
→ Call LLM API with Server API Key
→ Validate LLM Response
→ Return Safe Response
```

Frontend Proxy 책임 분리:

| 계층             | 책임                         |
| ---------------- | ---------------------------- |
| Frontend         | 사용자 입력, UI 표시         |
| Backend          | 인증, API Key 보호, LLM 호출 |
| LLM Client       | HTTP 통신, Timeout, Retry    |
| Validation Layer | 응답 검증, 안전 처리         |
| Logging Layer    | Usage, Latency, Error 기록   |

주의:

- CORS 우회 목적으로 Frontend에 API Key를 넣지 않는다.
- Backend 없이 Provider API를 직접 호출하지 않는다.
- 사용자별 Rate Limit을 Backend에서 적용한다.
- Prompt Injection과 과도한 입력 길이를 Backend에서 검증한다.
- Streaming Proxy는 Client Disconnect 처리까지 포함한다.

---

### [FAQ]

Q. Frontend Proxy Pattern이 뭐야?

A. Frontend가 LLM Provider를 직접 호출하지 않고 Backend를 통해 간접 호출하는 구조다.

Q. Frontend에서 직접 LLM API를 호출하면 안 되는 이유는?

A. API Key가 Browser에 노출되고 권한, 비용, Rate Limit 제어가 어렵기 때문이다.

Q. Backend는 어떤 역할을 해?

A. API Key 보호, 사용자 인증, 입력 검증, LLM 호출, 응답 검증, Usage Logging을 담당한다.

Q. Streaming도 Proxy Pattern을 써야 해?

A. 그렇다. Backend가 Provider Stream을 받아 Frontend로 전달하는 구조가 안전하다.

---

# 6. Provider Adapter and OpenAI-Compatible API

## 6.1 Provider Adapter

### [개념]

Provider Adapter는 LLM Provider마다 다른 Request Body, Response Body, Error Format, Streaming Format을 Application 내부 표준 형식으로 변환하는 계층이다.

Provider Adapter는 OpenAI, Ollama, Anthropic, Google, Local LLM, OpenAI-compatible Server 간 차이를 흡수한다.

---

### [핵심]

- Provider마다 API 필드와 응답 구조가 다를 수 있다.
- Provider Adapter는 외부 API 차이를 내부 Service에서 숨긴다.
- 내부 표준 Request와 Response DTO를 정의한다.
- Provider별 Error Mapping을 분리한다.
- Streaming Parser도 Provider별로 다를 수 있다.
- Provider 변경 시 Business Logic 수정을 최소화한다.

---

### [실무]

Adapter 구조:

```text
Application Service
→ LlmGateway Interface
→ OpenAiAdapter
→ OllamaAdapter
→ LocalLlmAdapter
→ Provider API
```

Interface 예:

```java
public interface LlmGateway {

    LlmResult chat(LlmPrompt prompt);

    EmbeddingResult embed(String text);
}
```

표준 Response 예:

```json
{
  "status": "success",
  "content": "LLM API 연동 결과",
  "finishReason": "stop",
  "usage": {
    "inputTokens": 500,
    "outputTokens": 120,
    "totalTokens": 620
  },
  "rawProvider": "provider-name"
}
```

Adapter 책임:

| 책임             | 설명                         |
| ---------------- | ---------------------------- |
| Request Mapping  | 내부 DTO → Provider Request  |
| Response Mapping | Provider Response → 내부 DTO |
| Error Mapping    | Provider Error → 표준 Error  |
| Streaming Parse  | Provider Stream → 표준 Chunk |
| Usage Mapping    | Token Usage 표준화           |
| Tool Mapping     | Tool Call 구조 변환          |
| Capability Check | 지원 기능 확인               |

주의:

- Provider 응답 구조를 Service 계층에 노출하지 않는다.
- Adapter는 Secret을 로그에 남기지 않는다.
- Provider별 기능 차이를 Capability로 관리한다.
- OpenAI-compatible이라고 모든 기능이 동일하다고 가정하지 않는다.
- Local LLM Adapter는 API LLM과 Latency, Error 특성이 다를 수 있다.

---

### [FAQ]

Q. Provider Adapter가 뭐야?

A. Provider마다 다른 API 요청, 응답, 오류 구조를 내부 표준 형식으로 변환하는 계층이다.

Q. Provider Adapter는 왜 필요해?

A. LLM Provider를 바꾸거나 Local LLM을 추가해도 Business Logic 변경을 줄이기 위해 필요하다.

Q. OpenAI-compatible이면 Adapter가 필요 없어?

A. 아니다. 호환 API라도 Streaming, Tool Calling, Usage, Error 구조가 다를 수 있다.

Q. Adapter가 담당해야 하는 것은?

A. Request Mapping, Response Mapping, Error Mapping, Streaming Parse, Usage Mapping을 담당한다.

---

## 6.2 OpenAI-Compatible API

### [개념]

OpenAI-Compatible API는 OpenAI Chat Completion, Embedding, Tool Calling 형식과 유사한 HTTP API 구조를 제공하는 방식이다.

Ollama, vLLM, LM Studio, Local LLM Server, 일부 Cloud Provider는 OpenAI-compatible Endpoint를 제공할 수 있다.

---

### [핵심]

- OpenAI-compatible API는 연동 비용을 줄인다.
- `/chat/completions`, `/embeddings` 같은 Endpoint를 사용할 수 있다.
- Request Body가 유사해도 기능 지원 범위는 다를 수 있다.
- Tool Calling, JSON Schema, Streaming, Usage 제공 여부가 다를 수 있다.
- Local LLM은 API LLM보다 응답 속도와 품질이 다를 수 있다.
- Provider별 Capability 확인이 필요하다.

---

### [실무]

OpenAI-Compatible Chat Request 예:

```json
{
  "model": "qwen2.5:14b",
  "messages": [
    {
      "role": "system",
      "content": "You are a backend assistant."
    },
    {
      "role": "user",
      "content": "LLM API 연동 구조를 설명해줘."
    }
  ],
  "temperature": 0.2
}
```

OpenAI-Compatible Embedding Request 예:

```json
{
  "model": "bge-m3",
  "input": "Embedding은 텍스트를 Vector로 변환한다."
}
```

Capability Checklist:

```text
Chat Completion 지원 여부
Embedding 지원 여부
Streaming 지원 여부
Tool Calling 지원 여부
JSON Mode 지원 여부
JSON Schema 지원 여부
Usage Token 제공 여부
Finish Reason 제공 여부
Context Window 크기
Max Tokens 설정 지원 여부
```

주의:

- OpenAI-compatible은 완전 동일을 의미하지 않는다.
- Local Model은 모델명, Context Window, Parameter 지원 범위가 다를 수 있다.
- Usage Token이 제공되지 않을 수 있다.
- Tool Calling이 Provider별로 다르게 동작할 수 있다.
- JSON Schema 기능은 모델과 서버 구현에 따라 차이가 크다.

---

### [FAQ]

Q. OpenAI-Compatible API가 뭐야?

A. OpenAI Chat Completion이나 Embedding API와 유사한 요청/응답 구조를 제공하는 API 방식이다.

Q. OpenAI-compatible이면 모든 기능이 같아?

A. 아니다. Tool Calling, Streaming, Usage, JSON Schema 지원 여부가 다를 수 있다.

Q. Local LLM도 OpenAI-Compatible API로 쓸 수 있어?

A. 가능하다. Ollama, vLLM, LM Studio 같은 서버가 유사 Endpoint를 제공할 수 있다.

Q. OpenAI-Compatible API를 쓸 때 무엇을 확인해야 해?

A. 모델명, Context Window, Streaming, Tool Calling, Usage, JSON Output 지원 여부를 확인해야 한다.

---

# 7. Local LLM HTTP Integration

## 7.1 Ollama API Integration

### [개념]

Ollama API Integration은 로컬 Ollama Server를 HTTP API로 호출해 Local LLM을 사용하는 방식이다.

Ollama는 로컬 모델 실행, Chat Completion, Text Generation, Embedding 기능을 제공할 수 있다.

Ollama Integration Flow:

```text
Application
→ Ollama Local API
→ Local Model Inference
→ Response
```

---

### [핵심]

- Ollama는 Local LLM Server로 사용할 수 있다.
- API Key 비용 없이 로컬 모델을 호출할 수 있다.
- 모델 크기와 하드웨어에 따라 속도가 달라진다.
- Chat Model과 Embedding Model을 구분한다.
- Local LLM도 Hallucination이 발생할 수 있다.
- Timeout과 Error Handling은 여전히 필요하다.
- 동시 요청 처리 한계를 고려해야 한다.

---

### [실무]

Ollama Chat 호출 예:

```bash
curl http://localhost:11434/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen2.5:14b",
    "messages": [
      {
        "role": "user",
        "content": "LLM API 연동 구조를 설명해줘."
      }
    ],
    "stream": false
  }'
```

Ollama Embedding 호출 예:

```bash
curl http://localhost:11434/api/embed \
  -H "Content-Type: application/json" \
  -d '{
    "model": "bge-m3",
    "input": "Embedding은 텍스트를 Vector로 변환한다."
  }'
```

Docker Container에서 Host Ollama 접근 예:

```text
http://host.docker.internal:11434
```

Local LLM 설정 기준:

| 항목            | 기준                       |
| --------------- | -------------------------- |
| Chat Model      | Qwen, Llama, Code Model    |
| Embedding Model | BGE-M3 등                  |
| Context Window  | 모델 설정 확인             |
| RAM / VRAM      | 모델 크기 고려             |
| Timeout         | API LLM보다 길게 필요 가능 |
| Streaming       | UI에 유용                  |
| Privacy         | 외부 전송 없음             |
| Quality         | 모델별 평가 필요           |

주의:

- Local LLM은 무료처럼 보여도 하드웨어 자원을 사용한다.
- 큰 모델은 RAM과 VRAM을 많이 사용한다.
- Docker 내부에서 localhost는 Container 자신을 의미할 수 있다.
- Local LLM 응답 품질은 API LLM보다 낮을 수 있다.
- Local LLM도 Response Validation과 RAG Grounding이 필요하다.

---

### [FAQ]

Q. Ollama API Integration이 뭐야?

A. 로컬 Ollama Server를 HTTP API로 호출해 Local LLM을 사용하는 방식이다.

Q. Ollama를 쓰면 API Key가 필요 없어?

A. 로컬 Ollama 호출 자체에는 보통 외부 Provider API Key가 필요 없다.

Q. Docker Container에서 Ollama는 어떻게 호출해?

A. Host에서 실행 중인 Ollama는 보통 `host.docker.internal:11434`로 접근할 수 있다.

Q. Local LLM은 Hallucination이 없어?

A. 아니다. Local LLM도 근거 없는 답변을 생성할 수 있으므로 RAG와 검증이 필요하다.

---

## 7.2 Local LLM Resource Management

### [개념]

Local LLM Resource Management는 로컬 모델 실행 시 RAM, VRAM, CPU, GPU, Context Window, 동시 요청 수를 관리하는 작업이다.

Local LLM은 외부 API 비용은 줄일 수 있지만 하드웨어 자원을 직접 사용한다.

---

### [핵심]

- 모델 크기가 클수록 RAM과 VRAM 사용량이 증가한다.
- Context Window가 길수록 메모리 사용량이 늘어난다.
- 동시 요청은 Latency와 메모리 사용량을 증가시킨다.
- Quantization은 메모리 사용량을 줄일 수 있지만 품질에 영향을 줄 수 있다.
- Embedding Model과 Chat Model은 역할과 자원 사용이 다르다.
- Local LLM 운영에는 모니터링이 필요하다.

---

### [실무]

로컬 AI 서버 구성 예:

```text
Chat / Code Generation
→ Qwen2.5 14B

Embedding / Semantic Search
→ BGE-M3

Vision / Image Input
→ Qwen2.5-VL 7B

Runtime
→ Ollama

RAG Platform
→ AnythingLLM
```

Resource 관리 기준:

| 항목             | 기준                            |
| ---------------- | ------------------------------- |
| RAM              | 모델 로딩과 Context 사용량 고려 |
| VRAM / UMA       | 모델 가속 가능 범위             |
| CPU              | Token 생성 속도 영향            |
| Context Window   | 길수록 자원 증가                |
| Parallel Request | 제한 필요                       |
| Model Loading    | 첫 요청 지연 가능               |
| Quantization     | 메모리 절약                     |
| Monitoring       | 사용량 관찰                     |

운영 기준:

```text
Large Model
→ 낮은 동시성
→ 긴 Timeout
→ Streaming 권장
→ Context 제한

Embedding Model
→ Batch 처리
→ Rate / Queue 관리
→ Vector Dimension 검증
```

주의:

- Local LLM은 동시 요청이 많으면 급격히 느려질 수 있다.
- Context를 크게 잡으면 메모리 사용량이 증가한다.
- 모델을 여러 개 동시에 올리면 RAM 부족이 발생할 수 있다.
- Embedding 작업과 Chat 응답을 동시에 많이 실행하면 지연이 커질 수 있다.
- API LLM과 Local LLM을 Router로 분리할 수 있다.

---

### [FAQ]

Q. Local LLM Resource Management가 뭐야?

A. 로컬 모델 실행 시 RAM, VRAM, CPU, Context Window, 동시 요청 수를 관리하는 작업이다.

Q. Local LLM은 왜 느릴 수 있어?

A. 모델 크기, Quantization, CPU/GPU 성능, RAM, Context Length, 동시 요청 수 영향을 받기 때문이다.

Q. Context Window를 크게 잡으면 어떤 문제가 있어?

A. 메모리 사용량과 Latency가 증가할 수 있다.

Q. Chat Model과 Embedding Model을 같이 돌려도 돼?

A. 가능하지만 메모리와 동시 요청 부하를 고려해야 한다.

---

# 8. Common Mistakes

## 8.1 API Key and HTTP Client Common Mistakes

### [개념]

API Key and HTTP Client Common Mistakes는 LLM API 연동 시 인증, Secret 관리, HTTP 호출, Provider 차이, Local LLM 연결에서 자주 발생하는 오류이다.

---

### [핵심]

자주 발생하는 실수:

- API Key를 코드에 하드코딩
- API Key를 Git에 커밋
- API Key를 Frontend 환경변수에 저장
- Authorization Header를 로그로 출력
- `.env` 파일을 `.gitignore`에 추가하지 않음
- API Key 노출 후 Rotation하지 않음
- Timeout 없이 HTTP 요청
- Controller에서 직접 Provider API 호출
- Provider Response를 검증 없이 사용
- HTTP Status Code 확인 누락
- Error Body를 그대로 사용자에게 노출
- Provider별 API 차이 무시
- OpenAI-compatible API를 완전 동일하게 가정
- Streaming 응답을 일반 JSON DTO로 파싱
- Docker Container에서 Host Ollama를 `localhost`로 호출
- Local LLM 자원 한계를 고려하지 않음
- Usage Logging 누락
- Secret Redaction 누락

---

### [실무]

문제 진단 Flow:

```text
LLM API Call Failed
→ Check API Key
→ Check Environment Variable
→ Check Base URL
→ Check Request Header
→ Check Request Body
→ Check Timeout
→ Check HTTP Status
→ Check Provider Response Format
→ Check Error Mapping
```

해결 기준:

| 문제                    | 해결                           |
| ----------------------- | ------------------------------ |
| 401 Unauthorized        | API Key, Header, Rotation 확인 |
| 403 Forbidden           | 권한, Provider 설정 확인       |
| Timeout                 | Timeout 조정, Context 축소     |
| 400 Bad Request         | Request Body Schema 확인       |
| Empty Response          | Response Validation 추가       |
| Streaming 파싱 실패     | Stream Parser 분리             |
| Docker Ollama 연결 실패 | host.docker.internal 사용      |
| Secret 로그 노출        | Redaction 적용                 |
| Frontend Key 노출       | Backend Proxy Pattern 적용     |

검수 Checklist:

```text
API Key가 환경변수 또는 Secret Manager로 관리되는가?
API Key가 코드와 Git에 없는가?
Frontend Bundle에 Secret이 포함되지 않는가?
Authorization Header가 로그에서 제거되는가?
HTTP Client 계층이 분리되어 있는가?
Timeout이 설정되어 있는가?
HTTP Status Code를 확인하는가?
Response Body를 검증하는가?
Provider Adapter가 있는가?
OpenAI-compatible 기능 차이를 확인했는가?
Local LLM Base URL이 환경에 맞는가?
Usage, Latency, Error 로그를 남기는가?
```

---

### [FAQ]

Q. LLM API 연동에서 가장 흔한 보안 실수는?

A. API Key를 코드, Git, Frontend, 로그에 노출하는 것이다.

Q. LLM API 호출에서 가장 흔한 안정성 실수는?

A. Timeout과 Error Handling 없이 성공 응답만 가정하는 것이다.

Q. OpenAI-compatible API를 쓸 때 흔한 실수는?

A. 모든 Provider가 Tool Calling, Streaming, Usage, JSON Schema를 동일하게 지원한다고 가정하는 것이다.

Q. Docker에서 Ollama 연결이 안 되면?

A. Container 내부의 `localhost`는 Container 자신이므로 Host Ollama는 `host.docker.internal:11434` 같은 주소를 확인해야 한다.

Q. API Key 노출을 막는 가장 기본 원칙은?

A. Backend에서만 Secret을 사용하고 Frontend와 로그에는 절대 노출하지 않는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. API Key가 뭐야?
A. LLM API Provider가 Client를 인증하고 사용량을 추적하기 위해 발급하는 Secret 값이다.

Q. API Key를 코드에 넣어도 돼?
A. 안 된다. 코드에 하드코딩하면 Git, 빌드 결과, 로그를 통해 노출될 수 있다.

Q. API Key는 어디에 저장해야 해?
A. 환경변수, `.env`, Secret Manager, CI/CD Secret에 저장해야 한다.

Q. API Key가 노출되면 어떻게 해?
A. 즉시 폐기하고 새 Key를 발급한 뒤 노출 경로와 사용 로그를 확인해야 한다.

Q. Frontend에 API Key를 넣으면 왜 위험해?
A. Browser Bundle과 Network 요청에서 사용자에게 API Key가 노출될 수 있기 때문이다.

Q. Environment Variable은 뭐야?
A. 실행 환경에서 Application에 전달하는 설정 값이다.

Q. LLM API 연동에서 환경변수는 왜 필요해?
A. API Key와 환경별 설정을 코드와 분리해 안전하게 관리하기 위해 필요하다.

Q. `.env` 파일은 Git에 올려도 돼?
A. 안 된다. `.env`에는 Secret이 포함될 수 있으므로 `.gitignore`에 추가해야 한다.

Q. Secret Rotation이 뭐야?
A. API Key 같은 Secret을 폐기하고 새 값으로 교체하는 운영 절차다.

Q. API Key가 노출되면 Rotation이 필요해?
A. 반드시 필요하다. 노출된 Key는 더 이상 신뢰할 수 없다.

Q. HTTP Client는 뭐야?
A. Application이 LLM API로 HTTP Request를 보내고 Response를 받는 구성 요소다.

Q. LLM API 호출을 별도 Client로 분리해야 해?
A. 권장한다. 인증, Timeout, Error Handling, Logging을 한 곳에서 관리할 수 있기 때문이다.

Q. Authorization Header에는 무엇을 넣어?
A. 일반적으로 `Bearer {API_KEY}` 형식으로 API Key를 넣는다.

Q. Request Header는 뭐야?
A. HTTP 요청의 인증, 형식, 추적 정보 같은 Metadata를 전달하는 영역이다.

Q. LLM API에서 가장 중요한 Header는?
A. Authorization과 Content-Type이다.

Q. API Key를 Query Parameter로 보내도 돼?
A. 권장하지 않는다. URL 로그나 브라우저 기록에 노출될 수 있다.

Q. JSON Request Body는 뭐야?
A. LLM API에 전달하는 모델, 메시지, 파라미터, Tool 정의 같은 요청 데이터다.

Q. Request Body 검증이 왜 필요해?
A. 필수 필드 누락, 지원하지 않는 필드, 잘못된 Parameter를 사전에 막기 위해 필요하다.

Q. Python에서 LLM API는 어떻게 호출해?
A. `requests` 또는 `httpx`로 Authorization Header, JSON Body, Timeout을 설정해 호출한다.

Q. requests Client에서 가장 중요한 설정은?
A. API Key 환경변수 로딩, Timeout, HTTP Status 확인, Response Validation이다.

Q. httpx는 언제 사용해?
A. 비동기 LLM API 호출, 동시 요청, 세밀한 Timeout 제어, Streaming 처리가 필요할 때 사용한다.

Q. Spring WebClient는 뭐야?
A. Spring에서 HTTP API를 호출하기 위한 Client이며 비동기와 Streaming 처리를 지원한다.

Q. Spring Boot에서 LLM API 연동에는 WebClient가 좋아?
A. 적합하다. Timeout, Header, Streaming, Error Mapping을 체계적으로 관리할 수 있다.

Q. Spring RestClient는 뭐야?
A. Spring Framework 6.1+에서 제공하는 현대적인 동기 HTTP Client다.

Q. RestClient와 WebClient 중 뭐가 좋아?
A. Streaming이나 비동기 처리가 필요하면 WebClient, 단순 동기 호출은 RestClient가 적합하다.

Q. ConfigurationProperties는 뭐야?
A. Spring Boot 설정 값을 타입 안전한 객체로 바인딩하는 방식이다.

Q. LLM 설정에 ConfigurationProperties를 쓰면 뭐가 좋아?
A. API Key, Base URL, Model, Timeout, Retry 설정을 한 곳에서 검증하고 관리할 수 있다.

Q. Node.js에서 LLM API는 어떻게 호출해?
A. 서버 환경에서 `fetch`로 Authorization Header, JSON Body, Timeout을 설정해 호출한다.

Q. Browser Fetch로 LLM API를 직접 호출해도 돼?
A. 안 된다. API Key가 사용자에게 노출될 수 있다.

Q. Axios로 LLM API를 호출해도 돼?
A. 가능하다. Node.js Backend에서 Axios Instance를 만들어 호출할 수 있다.

Q. Axios Error 로그에서 주의할 점은?
A. Authorization Header와 API Key가 Error Config에 포함될 수 있으므로 Redaction해야 한다.

Q. Frontend Proxy Pattern이 뭐야?
A. Frontend가 LLM Provider를 직접 호출하지 않고 Backend를 통해 간접 호출하는 구조다.

Q. Backend는 어떤 역할을 해?
A. API Key 보호, 사용자 인증, 입력 검증, LLM 호출, 응답 검증, Usage Logging을 담당한다.

Q. Provider Adapter가 뭐야?
A. Provider마다 다른 API 요청, 응답, 오류 구조를 내부 표준 형식으로 변환하는 계층이다.

Q. Provider Adapter는 왜 필요해?
A. LLM Provider를 바꾸거나 Local LLM을 추가해도 Business Logic 변경을 줄이기 위해 필요하다.

Q. OpenAI-Compatible API가 뭐야?
A. OpenAI Chat Completion이나 Embedding API와 유사한 요청/응답 구조를 제공하는 API 방식이다.

Q. OpenAI-compatible이면 모든 기능이 같아?
A. 아니다. Tool Calling, Streaming, Usage, JSON Schema 지원 여부가 다를 수 있다.

Q. Ollama API Integration이 뭐야?
A. 로컬 Ollama Server를 HTTP API로 호출해 Local LLM을 사용하는 방식이다.

Q. Docker Container에서 Ollama는 어떻게 호출해?
A. Host에서 실행 중인 Ollama는 보통 `host.docker.internal:11434`로 접근할 수 있다.

Q. Local LLM Resource Management가 뭐야?
A. 로컬 모델 실행 시 RAM, VRAM, CPU, Context Window, 동시 요청 수를 관리하는 작업이다.

Q. Local LLM은 왜 느릴 수 있어?
A. 모델 크기, Quantization, CPU/GPU 성능, RAM, Context Length, 동시 요청 수 영향을 받기 때문이다.

Q. LLM API 연동에서 가장 흔한 보안 실수는?
A. API Key를 코드, Git, Frontend, 로그에 노출하는 것이다.

Q. LLM API 호출에서 가장 흔한 안정성 실수는?
A. Timeout과 Error Handling 없이 성공 응답만 가정하는 것이다.
