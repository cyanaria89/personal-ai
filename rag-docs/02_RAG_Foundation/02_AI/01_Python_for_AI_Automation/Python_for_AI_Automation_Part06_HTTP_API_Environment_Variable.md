# Python for AI Automation Part06 - HTTP API Environment Variable

---

# 1. HTTP API Request Overview

## 1.1 HTTP API Request Role

### [개념]

HTTP API Request는 Python 자동화 스크립트가 외부 서비스, LLM API, Embedding API, Vector Database API, Backend API, Agent Tool Server와 통신하는 방식이다.

Python for AI Automation에서 API Request는 데이터를 요청하고, JSON Response를 처리하고, Agent Workflow에 필요한 외부 기능을 호출하는 핵심 작업이다.

Part06의 JSON 검증은 **HTTP API Response 중심**이다.
Part05의 JSON 검증은 **파일 기반 Config / Report / Tool Output 저장 구조 중심**이다.

기본 Flow:

```text
Python Script
→ Build Request
→ Send HTTP Request
→ Receive Response
→ Validate Status Code
→ Parse JSON Response
→ Return Structured Result
```

---

### [핵심]

- HTTP API Request는 외부 시스템과 데이터를 주고받는 기본 방식이다.
- Python에서는 `requests` 또는 `httpx`를 사용할 수 있다.
- API 호출에는 Timeout 설정이 필수이다.
- Status Code를 확인해야 한다.
- JSON Response는 `dict` 또는 `list`로 처리한다.
- API Response JSON은 Status Code, Header, Body 구조를 함께 확인한다.
- API Key는 코드에 직접 작성하지 않는다.
- 오류 응답은 구조화된 결과로 반환하는 것이 좋다.
- 무제한 Retry는 금지한다.
- `429 Too Many Requests`는 Rate Limit 정책에 따라 처리한다.
- 민감정보를 로그에 출력하지 않는다.

---

### [실무]

2026 실무 기준 Python 자동화에서 API Request는 다음 영역에 자주 사용된다.

- LLM API 호출
- Embedding API 호출
- Vector Database Search 호출
- Backend REST API 호출
- GitHub API 호출
- Slack / Discord Webhook 호출
- Agent Tool Server 호출
- 문서 검증 결과 전송
- 자동화 리포트 업로드
- 외부 데이터 수집

권장 API 처리 흐름:

```text
Input Parameters
→ Validate Parameters
→ Load API Key from Environment Variable
→ Build Headers
→ Send Request with Timeout
→ Check Status Code
→ Parse JSON
→ Validate Response Structure
→ Return Dict Result
```

파일 JSON과 API JSON의 차이:

```text
Part05 JSON
→ Local File
→ Config / Report / Saved Tool Output
→ json.load / json.dump 중심

Part06 JSON
→ HTTP Response Body
→ Status Code / Header / Body 함께 검증
→ response.json() 중심
```

---

### [FAQ]

Q. Python 자동화에서 HTTP API Request는 왜 필요해?

A. LLM API, Backend API, 외부 데이터 API, Agent Tool Server와 통신하기 위해 필요하다.

Q. Python API 호출에서 가장 중요한 설정은?

A. Timeout, Status Code 확인, API Key 보안, 오류 처리이다.

Q. API Response는 Python에서 어떤 타입으로 처리해?

A. JSON Response는 보통 dict 또는 list로 처리한다.

Q. API Key는 코드에 직접 넣어도 돼?

A. 안 된다. 환경변수나 `.env`로 관리해야 한다.

Q. API 호출 실패는 어떻게 처리해야 해?

A. 실패 원인, Status Code, 오류 메시지를 구조화된 dict로 반환하는 것이 좋다.

Q. Part05 JSON 검증과 Part06 JSON 검증은 어떻게 달라?

A. Part05는 파일 기반 JSON 검증이고, Part06은 HTTP API Response JSON 검증이다.

---

# 2. requests

## 2.1 requests Basics

### [개념]

`requests`는 Python에서 HTTP API를 쉽게 호출하기 위한 외부 라이브러리이다.

GET, POST, PUT, DELETE 요청을 간단하게 작성할 수 있으며 JSON Response 처리에 자주 사용된다.

```python
import requests

response = requests.get(
    "https://api.example.com/items",
    timeout=10,
)

response.raise_for_status()
data = response.json()
```

---

### [핵심]

- `requests`는 외부 패키지이다.
- `pip install requests`로 설치한다.
- `requests.get()`은 GET 요청을 보낸다.
- `requests.post()`는 POST 요청을 보낸다.
- `timeout`을 반드시 설정한다.
- `response.status_code`로 응답 상태를 확인한다.
- `response.json()`으로 JSON Response를 Python 객체로 변환한다.
- `response.raise_for_status()`는 HTTP 오류 상태에서 예외를 발생시킨다.
- 단순 동기 API 호출에는 requests가 충분히 적합하다.

---

### [실무]

GET 요청:

```python
import requests

def fetch_items() -> dict:
    response = requests.get(
        "https://api.example.com/items",
        timeout=10,
    )
    response.raise_for_status()
    return response.json()
```

POST 요청:

```python
import requests

def create_item(payload: dict) -> dict:
    response = requests.post(
        "https://api.example.com/items",
        json=payload,
        timeout=10,
    )
    response.raise_for_status()
    return response.json()
```

구조화된 결과 반환:

```python
import requests

def safe_get_json(url: str) -> dict:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        return {
            "status": "success",
            "result": response.json(),
            "error": None,
        }
    except requests.RequestException as error:
        return {
            "status": "error",
            "result": None,
            "error": str(error),
        }
```

---

### [FAQ]

Q. requests는 Python 표준 라이브러리야?

A. 아니다. 별도 설치가 필요한 외부 패키지이다.

Q. requests는 언제 사용해?

A. 외부 REST API, LLM API, Backend API, Webhook을 호출할 때 사용한다.

Q. requests에서 timeout은 왜 필요해?

A. API 서버가 응답하지 않을 때 스크립트가 무한 대기하는 것을 막기 위해 필요하다.

Q. response.json은 무엇을 해?

A. JSON Response Body를 Python dict 또는 list로 변환한다.

Q. raise_for_status는 왜 사용해?

A. 4xx, 5xx HTTP 오류를 명확히 예외로 처리하기 위해 사용한다.

---

## 2.2 GET Request

### [개념]

GET Request는 서버에서 데이터를 조회하기 위한 HTTP 요청 방식이다.

Python 자동화에서는 검색, 목록 조회, 상태 확인, 메타데이터 조회에 자주 사용한다.

```python
import requests

response = requests.get(
    "https://api.example.com/documents",
    params={"limit": 10},
    timeout=10,
)
```

---

### [핵심]

- GET은 데이터 조회에 사용한다.
- Query Parameter는 `params`로 전달한다.
- Header는 `headers`로 전달한다.
- GET 요청에는 일반적으로 Body를 사용하지 않는다.
- 응답 Status Code를 확인한다.
- JSON 응답 구조를 검증한다.
- 민감정보를 Query Parameter에 넣지 않는다.
- Query Parameter는 URL 로그에 남을 수 있다.

---

### [실무]

Query Parameter 사용:

```python
import requests

def search_documents(keyword: str, limit: int = 10) -> dict:
    response = requests.get(
        "https://api.example.com/documents/search",
        params={
            "keyword": keyword,
            "limit": limit,
        },
        timeout=10,
    )

    response.raise_for_status()
    return response.json()
```

Header 사용:

```python
import requests

def get_current_user(api_key: str) -> dict:
    response = requests.get(
        "https://api.example.com/me",
        headers={
            "Authorization": f"Bearer {api_key}",
        },
        timeout=10,
    )

    response.raise_for_status()
    return response.json()
```

구조화된 GET 결과:

```python
import requests

def get_json(url: str, params: dict | None = None) -> dict:
    try:
        response = requests.get(
            url,
            params=params,
            timeout=10,
        )
        response.raise_for_status()

        return {
            "status": "success",
            "status_code": response.status_code,
            "result": response.json(),
            "error": None,
        }
    except requests.RequestException as error:
        return {
            "status": "error",
            "status_code": None,
            "result": None,
            "error": str(error),
        }
```

---

### [FAQ]

Q. GET Request는 언제 사용해?

A. 서버에서 데이터를 조회할 때 사용한다.

Q. GET Query Parameter는 어떻게 전달해?

A. `params={...}` 형태로 전달한다.

Q. GET Request에 Body를 넣어도 돼?

A. 일반적으로 사용하지 않는다. 조회 조건은 Query Parameter로 전달한다.

Q. API Key를 Query Parameter로 넣어도 돼?

A. 가능하더라도 권장하지 않는다. Header나 환경변수 기반 설정을 우선한다.

---

## 2.3 POST Request

### [개념]

POST Request는 서버에 데이터를 생성하거나 작업 실행을 요청하기 위한 HTTP 요청 방식이다.

Python 자동화에서는 LLM API 호출, Agent Tool 실행, 문서 검증 결과 전송, Webhook 전송에 자주 사용한다.

```python
import requests

response = requests.post(
    "https://api.example.com/generate",
    json={"prompt": "Summarize this document"},
    timeout=30,
)
```

---

### [핵심]

- POST는 데이터 생성 또는 작업 실행에 사용한다.
- JSON Body는 `json={...}`로 전달한다.
- Form Data는 `data={...}`로 전달한다.
- Header는 `headers={...}`로 전달한다.
- LLM API 호출은 대부분 POST를 사용한다.
- 요청 Body에 민감정보를 넣을 때 로그 출력에 주의한다.
- 응답 구조를 검증한다.
- 긴 생성 작업은 Timeout을 더 길게 설정할 수 있다.

---

### [실무]

LLM API 요청 구조 예시:

```python
import requests

def call_llm_api(api_key: str, prompt: str) -> dict:
    response = requests.post(
        "https://api.example.com/v1/chat",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": "qwen2.5",
            "messages": [
                {"role": "user", "content": prompt},
            ],
        },
        timeout=60,
    )

    response.raise_for_status()
    return response.json()
```

Agent Tool 실행 요청:

```python
import requests

def run_agent_tool(tool_url: str, payload: dict) -> dict:
    response = requests.post(
        tool_url,
        json=payload,
        timeout=30,
    )

    response.raise_for_status()
    return response.json()
```

Webhook 전송:

```python
import requests

def send_webhook(webhook_url: str, message: str) -> dict:
    response = requests.post(
        webhook_url,
        json={"text": message},
        timeout=10,
    )

    response.raise_for_status()

    return {
        "status": "success",
        "status_code": response.status_code,
        "error": None,
    }
```

---

### [FAQ]

Q. POST Request는 언제 사용해?

A. 서버에 데이터를 생성하거나 작업 실행을 요청할 때 사용한다.

Q. JSON Body는 어떻게 보내?

A. `json=payload` 인자를 사용한다.

Q. LLM API 호출은 GET이야 POST야?

A. 대부분 POST를 사용한다.

Q. POST 요청에서 Content-Type은 무엇이야?

A. 요청 Body 형식을 나타내며 JSON 전송 시 `application/json`을 사용한다.

Q. POST 요청 Body를 로그에 출력해도 돼?

A. 민감정보가 포함될 수 있으므로 그대로 출력하지 않는다.

---

# 3. httpx

## 3.1 httpx Basics

### [개념]

`httpx`는 동기와 비동기 HTTP 요청을 모두 지원하는 Python HTTP Client 라이브러리이다.

`requests`와 비슷한 방식으로 사용할 수 있으며, Async API Call이 필요한 자동화에서 유용하다.

```python
import httpx

response = httpx.get(
    "https://api.example.com/items",
    timeout=10,
)
response.raise_for_status()
data = response.json()
```

---

### [핵심]

- `httpx`는 외부 패키지이다.
- 동기 요청과 비동기 요청을 모두 지원한다.
- `requests`와 유사한 API를 제공한다.
- Timeout 설정을 지원한다.
- 대량 API 호출이나 비동기 워크플로우에 적합하다.
- 단순 자동화는 requests로 충분한 경우가 많다.
- Async 사용 시 `async` / `await` 구조를 이해해야 한다.

---

### [실무]

동기 요청:

```python
import httpx

def fetch_json(url: str) -> dict:
    response = httpx.get(url, timeout=10)
    response.raise_for_status()
    return response.json()
```

Client 사용:

```python
import httpx

def fetch_with_client(url: str) -> dict:
    with httpx.Client(timeout=10) as client:
        response = client.get(url)
        response.raise_for_status()
        return response.json()
```

비동기 요청:

```python
import httpx

async def fetch_json_async(url: str) -> dict:
    async with httpx.AsyncClient(timeout=10) as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()
```

---

### [FAQ]

Q. httpx는 무엇이야?

A. 동기와 비동기 HTTP 요청을 모두 지원하는 Python HTTP Client 라이브러리이다.

Q. httpx는 표준 라이브러리야?

A. 아니다. 별도 설치가 필요한 외부 패키지이다.

Q. requests와 httpx 차이는?

A. requests는 단순 동기 요청에 적합하고, httpx는 동기와 비동기 요청을 모두 지원한다.

Q. httpx는 언제 사용해?

A. 비동기 API 호출, 대량 요청, Async Agent Workflow가 필요할 때 사용할 수 있다.

---

## 3.2 requests vs httpx

### [개념]

`requests`와 `httpx`는 Python HTTP API Request에 사용하는 대표 라이브러리이다.

자동화 목적, 동기/비동기 필요성, 프로젝트 구조에 따라 선택한다.

---

### [핵심]

| 비교           | requests    | httpx |
| -------------- | ----------- | ----- |
| 설치           | 필요        | 필요  |
| 동기 요청      | 지원        | 지원  |
| 비동기 요청    | 기본 미지원 | 지원  |
| 사용 난이도    | 쉬움        | 쉬움  |
| 단순 자동화    | 적합        | 적합  |
| Async Workflow | 부적합      | 적합  |
| 기존 자료      | 많음        | 많음  |

---

### [실무]

선택 기준:

```text
단순 API 호출
→ requests

LLM API 1회 호출
→ requests

Webhook 전송
→ requests

동시 API 호출
→ httpx AsyncClient

Async Agent Tool
→ httpx

기존 코드가 requests 기반
→ requests 유지 가능
```

requests 예시:

```python
import requests

response = requests.get(
    "https://api.example.com/health",
    timeout=10,
)
```

httpx 예시:

```python
import httpx

response = httpx.get(
    "https://api.example.com/health",
    timeout=10,
)
```

---

### [FAQ]

Q. requests와 httpx 중 무엇을 먼저 배우면 돼?

A. 단순 자동화 기준에서는 requests를 먼저 배우면 충분하다.

Q. httpx가 requests보다 항상 좋아?

A. 아니다. 비동기 요청이 필요하지 않으면 requests도 충분히 좋다.

Q. Async API Call이 필요하면 무엇을 써?

A. httpx의 AsyncClient를 사용할 수 있다.

Q. Agent Tool Script에서는 무엇을 쓰면 좋아?

A. 단순 Tool은 requests, 비동기 Tool이나 대량 호출은 httpx를 고려한다.

---

# 4. HTTP Request Components

## 4.1 Header

### [개념]

Header는 HTTP Request에 포함되는 부가 정보이다.

API Key, 인증 토큰, Content-Type, Accept, User-Agent 같은 요청 메타데이터를 전달한다.

```python
headers = {
    "Authorization": "Bearer API_KEY",
    "Content-Type": "application/json",
}
```

---

### [핵심]

- Header는 요청 메타데이터이다.
- 인증에는 `Authorization` Header를 자주 사용한다.
- JSON 요청에는 `Content-Type: application/json`을 사용한다.
- JSON 응답을 기대할 때 `Accept: application/json`을 사용할 수 있다.
- API Key나 Token을 로그에 출력하지 않는다.
- Header 값은 환경변수에서 불러오는 것이 좋다.
- Header 전체를 debug 로그에 그대로 출력하지 않는다.

---

### [실무]

Authorization Header:

```python
import requests

def fetch_private_data(api_key: str) -> dict:
    response = requests.get(
        "https://api.example.com/private",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Accept": "application/json",
        },
        timeout=10,
    )

    response.raise_for_status()
    return response.json()
```

Content-Type Header:

```python
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}
```

Header 생성 함수:

```python
def build_auth_headers(api_key: str) -> dict:
    if not api_key:
        raise ValueError("api_key is required")

    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
```

---

### [FAQ]

Q. HTTP Header는 무엇이야?

A. 요청에 포함되는 인증, 데이터 형식, 응답 형식 같은 부가 정보이다.

Q. Authorization Header는 언제 사용해?

A. API Key, Bearer Token, Access Token 같은 인증 정보를 보낼 때 사용한다.

Q. Content-Type은 무엇이야?

A. 요청 Body의 데이터 형식을 나타낸다.

Q. API Key가 들어간 Header를 로그로 남겨도 돼?

A. 안 된다. 민감정보이므로 마스킹하거나 출력하지 않아야 한다.

---

## 4.2 Query Parameter

### [개념]

Query Parameter는 URL 뒤에 붙는 key-value 형태의 요청 조건이다.

GET Request에서 검색어, 페이지 번호, 정렬 기준, 필터 조건을 전달할 때 자주 사용한다.

```text
https://api.example.com/search?keyword=rag&limit=10
```

Python에서는 `params` 인자로 전달한다.

```python
params = {
    "keyword": "rag",
    "limit": 10,
}
```

---

### [핵심]

- Query Parameter는 조회 조건 전달에 사용한다.
- Python requests에서는 `params`로 전달한다.
- URL 문자열에 직접 붙이지 않는 것이 좋다.
- 검색어, 페이지, 정렬, 필터에 자주 사용한다.
- Secret 값은 Query Parameter로 전달하지 않는 것이 좋다.
- Parameter 값은 호출 전 검증한다.

---

### [실무]

검색 API 호출:

```python
import requests

def search_api(keyword: str, limit: int = 10) -> dict:
    response = requests.get(
        "https://api.example.com/search",
        params={
            "keyword": keyword,
            "limit": limit,
        },
        timeout=10,
    )

    response.raise_for_status()
    return response.json()
```

페이지 조회:

```python
params = {
    "page": 1,
    "size": 20,
    "sort": "createdAt,desc",
}
```

검증:

```python
def validate_search_params(keyword: str, limit: int) -> None:
    if not keyword.strip():
        raise ValueError("keyword is required")

    if limit <= 0:
        raise ValueError("limit must be positive")
```

---

### [FAQ]

Q. Query Parameter는 무엇이야?

A. URL에 붙어 검색 조건, 페이지 번호, 필터 조건을 전달하는 key-value 값이다.

Q. Python에서 Query Parameter는 어떻게 전달해?

A. `params={...}` 인자로 전달한다.

Q. URL 문자열에 직접 Query Parameter를 붙여도 돼?

A. 가능하지만 권장하지 않는다. `params`를 사용하면 인코딩과 가독성이 좋아진다.

Q. Secret을 Query Parameter로 전달해도 돼?

A. 권장하지 않는다. URL 로그에 남을 수 있기 때문이다.

---

## 4.3 JSON Body

### [개념]

JSON Body는 POST, PUT, PATCH 요청에서 서버로 전달하는 JSON 형식의 데이터 본문이다.

Python requests에서는 `json` 인자를 사용하면 dict를 JSON Body로 전송할 수 있다.

```python
payload = {
    "title": "RAG Document",
    "content": "Markdown text",
}
```

---

### [핵심]

- JSON Body는 생성, 수정, 작업 실행 요청에 사용한다.
- `json=payload`를 사용하면 JSON 직렬화와 Content-Type 설정이 처리된다.
- payload는 dict 또는 list 형태로 구성한다.
- 요청 전 필수 key를 검증한다.
- 민감정보가 포함된 Body는 로그 출력하지 않는다.
- LLM API 요청은 JSON Body 기반인 경우가 많다.

---

### [실무]

문서 생성 요청:

```python
import requests

def create_document(api_url: str, payload: dict) -> dict:
    response = requests.post(
        api_url,
        json=payload,
        timeout=30,
    )

    response.raise_for_status()
    return response.json()
```

LLM 요청 Body:

```python
payload = {
    "model": "qwen2.5",
    "messages": [
        {
            "role": "user",
            "content": "Generate RAG document outline",
        },
    ],
    "temperature": 0.2,
}
```

payload 검증:

```python
def validate_document_payload(payload: dict) -> None:
    required_keys = ["title", "content"]

    missing_keys = [
        key for key in required_keys
        if key not in payload
    ]

    if missing_keys:
        raise ValueError(f"Missing payload keys: {missing_keys}")
```

---

### [FAQ]

Q. JSON Body는 언제 사용해?

A. POST, PUT, PATCH 요청에서 데이터를 생성하거나 수정하거나 작업을 실행할 때 사용한다.

Q. Python requests에서 JSON Body는 어떻게 보내?

A. `json=payload` 인자를 사용한다.

Q. JSON Body에 dict를 넣어도 돼?

A. 가능하다. requests가 JSON 문자열로 변환해 전송한다.

Q. payload 검증은 왜 필요해?

A. 필수 key가 없으면 API 요청이 실패하거나 잘못된 작업이 실행될 수 있기 때문이다.

---

# 5. Response Handling

## 5.1 Status Code

### [개념]

Status Code는 HTTP 응답 결과를 나타내는 숫자 코드이다.

API 호출 결과가 성공인지 실패인지 판단하는 기본 기준이다.

---

### [핵심]

| Status Code | 의미                  |
| ----------- | --------------------- |
| 200         | OK                    |
| 201         | Created               |
| 204         | No Content            |
| 400         | Bad Request           |
| 401         | Unauthorized          |
| 403         | Forbidden             |
| 404         | Not Found             |
| 409         | Conflict              |
| 429         | Too Many Requests     |
| 500         | Internal Server Error |
| 503         | Service Unavailable   |

---

### [실무]

Status Code 확인:

```python
import requests

response = requests.get(
    "https://api.example.com/items",
    timeout=10,
)

if response.status_code == 200:
    data = response.json()
else:
    raise RuntimeError(f"API failed: {response.status_code}")
```

raise_for_status 사용:

```python
response.raise_for_status()
```

구조화된 응답:

```python
def build_response_result(response) -> dict:
    return {
        "status_code": response.status_code,
        "ok": response.ok,
        "content_type": response.headers.get("Content-Type"),
    }
```

---

### [FAQ]

Q. HTTP Status Code는 무엇이야?

A. API 응답 성공 또는 실패 상태를 나타내는 숫자 코드이다.

Q. 200은 무슨 뜻이야?

A. 요청이 정상 처리되었다는 의미이다.

Q. 401은 무슨 뜻이야?

A. 인증 정보가 없거나 잘못되었다는 의미이다.

Q. 403은 무슨 뜻이야?

A. 인증은 되었지만 접근 권한이 없다는 의미이다.

Q. 429는 무슨 뜻이야?

A. 요청 횟수 제한을 초과했다는 의미이다.

---

## 5.2 JSON Response Parsing

### [개념]

JSON Response Parsing은 API 응답 Body를 Python dict 또는 list로 변환하는 작업이다.

Python requests와 httpx에서는 `response.json()`을 사용한다.

Part06의 JSON Response Parsing은 단순 JSON 파싱뿐 아니라 **Status Code, Content-Type, Response Body 구조 검증**과 함께 처리한다.

```python
data = response.json()
```

---

### [핵심]

- JSON Response는 `response.json()`으로 변환한다.
- JSON Object는 dict가 된다.
- JSON Array는 list가 된다.
- 응답이 JSON이 아니면 오류가 발생할 수 있다.
- Content-Type 확인이 도움이 된다.
- 응답 구조가 예상과 같은지 검증한다.
- API Response는 성공 응답과 오류 응답의 구조가 다를 수 있다.

---

### [실무]

JSON Response 처리:

```python
import requests

def fetch_json_data(url: str) -> dict:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    if not isinstance(data, dict):
        raise ValueError("Response JSON root must be object")

    return data
```

Content-Type 확인:

```python
content_type = response.headers.get("Content-Type", "")

if "application/json" not in content_type:
    raise ValueError(f"Expected JSON response: {content_type}")
```

필수 key 검증:

```python
def validate_api_response(data: dict) -> None:
    required_keys = ["status", "result"]

    missing_keys = [
        key for key in required_keys
        if key not in data
    ]

    if missing_keys:
        raise ValueError(f"Missing response keys: {missing_keys}")
```

안전한 JSON Response 처리:

```python
import requests

def safe_parse_json_response(response: requests.Response) -> dict:
    content_type = response.headers.get("Content-Type", "")

    if "application/json" not in content_type:
        return {
            "status": "error",
            "result": None,
            "error": f"Expected JSON response: {content_type}",
        }

    return {
        "status": "success",
        "result": response.json(),
        "error": None,
    }
```

---

### [FAQ]

Q. response.json은 무엇을 해?

A. API 응답 Body의 JSON을 Python dict 또는 list로 변환한다.

Q. 응답이 JSON이 아니면 어떻게 돼?

A. JSON 파싱 오류가 발생할 수 있다.

Q. Content-Type은 왜 확인해?

A. 응답 Body가 JSON인지 확인하기 위해 사용한다.

Q. API Response key 검증은 왜 필요해?

A. 예상한 구조가 아니면 이후 자동화 로직이 실패할 수 있기 때문이다.

Q. API Response JSON과 파일 JSON 검증은 같은가?

A. 기본 JSON 구조 검증은 비슷하지만 API Response는 Status Code, Header, Body를 함께 고려해야 한다.

---

# 6. Timeout Retry Rate Limit

## 6.1 Timeout

### [개념]

Timeout은 API 응답을 기다리는 최대 시간이다.

Python 자동화에서는 Timeout을 설정하지 않으면 네트워크 문제나 API 서버 지연으로 스크립트가 멈춘 것처럼 보일 수 있다.

```python
requests.get(
    "https://api.example.com/items",
    timeout=10,
)
```

---

### [핵심]

- API 호출에는 Timeout을 반드시 설정한다.
- Timeout 없는 요청은 금지한다.
- 짧은 조회 API는 5~10초를 사용할 수 있다.
- LLM API나 긴 작업은 30~120초를 고려한다.
- Timeout 발생 시 재시도 가능 여부를 판단한다.
- Timeout 오류는 로그와 구조화된 결과에 남긴다.
- Timeout은 너무 짧아도 실패율이 증가할 수 있다.

---

### [실무]

기본 Timeout:

```python
import requests

response = requests.get(
    "https://api.example.com/health",
    timeout=5,
)
```

LLM API Timeout:

```python
import requests

response = requests.post(
    "https://api.example.com/v1/chat",
    json={"prompt": "Generate document"},
    timeout=60,
)
```

Timeout 오류 처리:

```python
import requests

def safe_fetch(url: str) -> dict:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        return {
            "status": "success",
            "result": response.json(),
            "error": None,
        }
    except requests.Timeout:
        return {
            "status": "error",
            "result": None,
            "error": "API timeout",
        }
```

---

### [FAQ]

Q. API Timeout은 무엇이야?

A. API 응답을 기다리는 최대 시간이다.

Q. Timeout을 설정하지 않으면 왜 위험해?

A. API 서버가 응답하지 않을 때 스크립트가 무한 대기할 수 있기 때문이다.

Q. 일반 API Timeout은 몇 초가 적당해?

A. 단순 조회는 5~10초 정도를 사용할 수 있다.

Q. LLM API Timeout은 길게 잡아도 돼?

A. 가능하다. 생성 작업은 오래 걸릴 수 있으므로 30~120초를 고려할 수 있다.

---

## 6.2 Retry

### [개념]

Retry는 일시적인 API 실패가 발생했을 때 요청을 제한적으로 다시 시도하는 방식이다.

네트워크 오류, Timeout, 429 Rate Limit, 503 Service Unavailable 같은 상황에서 사용할 수 있다.

---

### [핵심]

- Retry는 제한적으로 사용한다.
- 무제한 Retry는 금지한다.
- Retry 횟수는 명확히 제한한다.
- Retry 간 대기 시간을 둔다.
- 400, 401, 403 같은 요청 오류는 보통 Retry 대상이 아니다.
- 429, 500, 502, 503, 504는 Retry 대상이 될 수 있다.
- API Rate Limit 정책을 존중한다.
- LLM API는 비용과 Rate Limit을 함께 고려한다.

---

### [실무]

단순 Retry:

```python
import time
import requests

def get_with_retry(url: str, max_retries: int = 3) -> dict:
    last_error = None

    for attempt in range(1, max_retries + 1):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as error:
            last_error = error
            time.sleep(attempt)

    raise RuntimeError(f"API request failed after retries: {last_error}")
```

Retry 대상 Status Code:

```python
RETRYABLE_STATUS_CODES = {429, 500, 502, 503, 504}
```

Status Code 기반 Retry:

```python
import time
import requests

RETRYABLE_STATUS_CODES = {429, 500, 502, 503, 504}

def get_with_status_retry(url: str, max_retries: int = 3) -> dict:
    for attempt in range(1, max_retries + 1):
        response = requests.get(url, timeout=10)

        if response.status_code not in RETRYABLE_STATUS_CODES:
            response.raise_for_status()
            return response.json()

        time.sleep(attempt)

    raise RuntimeError("Retry limit exceeded")
```

---

### [FAQ]

Q. Retry는 언제 사용해?

A. Timeout, 네트워크 오류, 429, 500, 503 같은 일시적 실패에 사용할 수 있다.

Q. 무제한 Retry를 하면 안 되는 이유는?

A. 스크립트가 끝나지 않거나 API 서버에 과도한 부담을 줄 수 있기 때문이다.

Q. 401 오류도 Retry해야 해?

A. 보통 아니다. 인증 정보 오류이므로 API Key나 Token을 확인해야 한다.

Q. 429 오류는 무엇을 의미해?

A. 요청 횟수 제한을 초과했다는 의미이며 대기 후 재시도할 수 있다.

---

## 6.3 Rate Limit and Retry-After

### [개념]

Rate Limit은 API 제공자가 일정 시간 동안 허용하는 요청 수 제한이다.

`429 Too Many Requests` 응답은 요청 횟수 제한을 초과했다는 의미이며, 일부 API는 `Retry-After` Header로 재시도까지 기다려야 할 시간을 알려준다.

---

### [핵심]

- 429 응답은 Rate Limit 초과를 의미한다.
- 429 발생 시 즉시 반복 Retry하지 않는다.
- `Retry-After` Header를 확인한다.
- `Retry-After`가 있으면 해당 시간만큼 대기 후 재시도한다.
- `Retry-After`가 없으면 점진적 backoff를 적용한다.
- LLM API는 비용과 Rate Limit을 함께 고려한다.
- Batch API 호출은 요청 간 간격을 둔다.
- Rate Limit 오류는 로그와 결과에 명확히 남긴다.

---

### [실무]

Retry-After 확인:

```python
retry_after = response.headers.get("Retry-After")
```

Retry-After 기반 대기:

```python
import time

def sleep_for_retry_after(response) -> None:
    retry_after = response.headers.get("Retry-After")

    if retry_after is None:
        time.sleep(1)
        return

    try:
        seconds = int(retry_after)
    except ValueError:
        seconds = 1

    time.sleep(seconds)
```

Rate Limit 처리 예시:

```python
import time
import requests

def get_with_rate_limit_handling(url: str, max_retries: int = 3) -> dict:
    for attempt in range(1, max_retries + 1):
        response = requests.get(url, timeout=10)

        if response.status_code == 429:
            sleep_for_retry_after(response)
            continue

        response.raise_for_status()
        return response.json()

    raise RuntimeError("Rate limit retry exceeded")
```

Batch 요청 간 간격:

```python
import time

for item in items:
    call_api(item)
    time.sleep(0.5)
```

---

### [FAQ]

Q. Rate Limit은 무엇이야?

A. API 제공자가 일정 시간 동안 허용하는 요청 수 제한이다.

Q. 429 응답이 오면 바로 다시 요청해도 돼?

A. 권장하지 않는다. `Retry-After` Header를 확인하거나 backoff를 적용해야 한다.

Q. Retry-After Header는 무엇이야?

A. API가 다시 요청하기 전 기다려야 할 시간을 알려주는 Header이다.

Q. LLM API에서 Rate Limit이 중요한 이유는?

A. 요청 제한과 비용이 함께 영향을 주기 때문에 Batch 호출과 Retry 정책을 조심해야 한다.

---

# 7. Environment Variable

## 7.1 Environment Variable Role

### [개념]

Environment Variable은 코드 외부에서 설정값과 Secret을 주입하기 위한 운영 환경 변수이다.

Python for AI Automation에서는 API Key, Token, Base URL, Timeout, Model Name, 실행 환경을 환경변수로 관리한다.

기본 Flow:

```text
.env / OS Environment
→ Load Environment Variable
→ Validate Required Config
→ Build API Client
→ Execute Request
```

---

### [핵심]

- API Key는 코드에 직접 작성하지 않는다.
- 환경별 설정은 환경변수로 분리한다.
- Secret은 Git에 올리지 않는다.
- `.env` 파일은 `.gitignore`에 포함한다.
- 환경변수 누락 시 명확한 오류를 발생시킨다.
- Secret을 로그에 출력하지 않는다.
- 운영 환경에서는 Secret Manager 사용을 고려한다.
- `.env.example`은 필요한 환경변수 이름만 공유한다.

---

### [실무]

환경변수 사용 대상:

- `LLM_API_KEY`
- `LLM_BASE_URL`
- `VECTOR_DB_URL`
- `AGENT_TOOL_URL`
- `DEFAULT_TIMEOUT`
- `MODEL_NAME`
- `ENV`

보안 기준:

```text
API Key
→ Environment Variable
→ Validate
→ Use in Header
→ Never Log Secret
```

`.env`와 `.env.example` 역할:

```text
.env
→ 실제 로컬 Secret 저장
→ Git 제외

.env.example
→ 필요한 환경변수 이름 공유
→ 실제 Secret 미포함
→ Git 포함 가능
```

---

### [FAQ]

Q. Environment Variable은 왜 사용해?

A. API Key와 환경별 설정을 코드와 분리해 보안성과 재사용성을 높이기 위해 사용한다.

Q. API Key를 코드에 직접 작성하면 안 되는 이유는?

A. Git 업로드, 로그, 공유 과정에서 Secret이 노출될 수 있기 때문이다.

Q. `.env` 파일은 Git에 올려도 돼?

A. 안 된다. `.gitignore`에 포함해야 한다.

Q. 환경변수 누락 시 어떻게 처리해?

A. 명확한 오류 메시지를 발생시켜 설정 문제를 빠르게 찾도록 한다.

Q. `.env.example`은 왜 필요해?

A. 실제 Secret 없이 필요한 환경변수 이름과 기본 설정 구조를 공유하기 위해 필요하다.

---

## 7.2 os.environ

### [개념]

`os.environ`은 Python에서 OS 환경변수를 읽는 표준 방식이다.

환경변수에서 API Key, URL, 실행 설정을 가져올 수 있다.

```python
import os

api_key = os.environ.get("LLM_API_KEY")
```

---

### [핵심]

- `os.environ.get("KEY")`로 환경변수를 읽는다.
- 값이 없으면 `None`을 반환한다.
- 필수 환경변수는 누락 여부를 검사한다.
- 기본값이 안전한 경우만 default를 사용한다.
- Secret 기본값을 코드에 넣지 않는다.
- 환경변수는 문자열로 읽히므로 숫자는 변환이 필요하다.

---

### [실무]

환경변수 읽기:

```python
import os

api_key = os.environ.get("LLM_API_KEY")

if not api_key:
    raise ValueError("LLM_API_KEY is required")
```

기본값 사용:

```python
import os

timeout = int(os.environ.get("DEFAULT_TIMEOUT", "30"))
model_name = os.environ.get("MODEL_NAME", "qwen2.5")
```

필수 환경변수 함수:

```python
import os

def get_required_env(name: str) -> str:
    value = os.environ.get(name)

    if not value:
        raise ValueError(f"{name} is required")

    return value
```

---

### [FAQ]

Q. os.environ은 무엇이야?

A. Python에서 OS 환경변수를 읽고 사용할 수 있는 표준 기능이다.

Q. os.environ.get은 값이 없으면 어떻게 돼?

A. 기본적으로 None을 반환한다.

Q. 필수 환경변수는 어떻게 처리해?

A. 값이 없으면 ValueError를 발생시켜 명확히 실패시키는 것이 좋다.

Q. Secret 기본값을 코드에 넣어도 돼?

A. 안 된다. Secret은 기본값으로도 코드에 넣지 않는다.

Q. 환경변수 숫자값은 바로 int로 사용할 수 있어?

A. 아니다. 환경변수는 문자열로 읽히므로 `int()` 같은 변환이 필요하다.

---

## 7.3 python-dotenv

### [개념]

`python-dotenv`는 `.env` 파일의 값을 Python 환경변수로 로드하는 외부 패키지이다.

로컬 개발 환경에서 API Key, Base URL, Timeout 같은 설정값을 쉽게 관리할 수 있다.

```python
from dotenv import load_dotenv

load_dotenv()
```

---

### [핵심]

- `python-dotenv`는 외부 패키지이다.
- `.env` 파일 값을 환경변수로 로드한다.
- 로컬 개발 환경에서 유용하다.
- 운영 환경에서는 OS 환경변수 또는 Secret Manager를 우선한다.
- `.env` 파일은 Git에 커밋하지 않는다.
- `.env.example`은 공유 가능하다.
- `.env.example`에는 실제 API Key를 넣지 않는다.

---

### [실무]

설치:

```bash
pip install python-dotenv
```

`.env` 예시:

```text
LLM_API_KEY=your-api-key
LLM_BASE_URL=https://api.example.com
DEFAULT_TIMEOUT=30
MODEL_NAME=qwen2.5
```

Python 로드:

```python
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("LLM_API_KEY")
```

`.env.example` 예시:

```text
LLM_API_KEY=
LLM_BASE_URL=
DEFAULT_TIMEOUT=30
MODEL_NAME=qwen2.5
```

`.gitignore` 예시:

```text
.env
.venv
__pycache__/
```

---

### [FAQ]

Q. python-dotenv는 무엇이야?

A. `.env` 파일 값을 Python 환경변수로 로드하는 외부 패키지이다.

Q. python-dotenv는 운영 환경에서도 필수야?

A. 아니다. 운영 환경에서는 OS 환경변수나 Secret Manager를 우선한다.

Q. `.env` 파일은 Git에 올려도 돼?

A. 안 된다. Secret이 포함될 수 있으므로 `.gitignore`에 추가해야 한다.

Q. `.env.example`은 왜 만들어?

A. 필요한 환경변수 목록을 공유하되 실제 Secret은 제외하기 위해 만든다.

---

# 8. Secret Management

## 8.1 API Key Protection

### [개념]

API Key Protection은 API Key, Token, Secret, Credential 같은 민감정보를 코드, 로그, 문서, Git 저장소에 노출하지 않는 보안 기준이다.

Python 자동화 스크립트는 외부 API를 자주 호출하므로 Secret 관리가 필수이다.

---

### [핵심]

- API Key 하드코딩 금지
- Secret 로그 출력 금지
- `.env` Git 커밋 금지
- Secret이 포함된 오류 메시지 출력 금지
- Query Parameter로 Secret 전달 지양
- Header 기반 인증 우선
- Secret Masking 적용 고려
- 공유 문서에는 예시 Key만 사용
- 유출된 API Key는 즉시 폐기하고 재발급
- API Request 실패 로그에도 Secret이 포함되지 않게 한다.

---

### [실무]

나쁜 예:

```python
api_key = "sk-real-secret-key"
```

좋은 예:

```python
api_key = get_required_env("LLM_API_KEY")
```

Secret 마스킹:

```python
def mask_secret(secret: str) -> str:
    if len(secret) <= 8:
        return "****"

    return secret[:4] + "****" + secret[-4:]
```

로그 출력 시 주의:

```python
api_key = get_required_env("LLM_API_KEY")
masked_key = mask_secret(api_key)

print(f"Using API Key: {masked_key}")
```

---

### [FAQ]

Q. API Key를 코드에 직접 넣으면 왜 안 돼?

A. Git, 로그, 화면 공유, 문서 공유 과정에서 Secret이 노출될 수 있기 때문이다.

Q. Secret을 로그에 출력해도 돼?

A. 안 된다. 필요하면 마스킹해서 일부만 표시한다.

Q. API Key가 유출되면 어떻게 해야 해?

A. 즉시 폐기하고 새 Key를 발급해야 한다.

Q. Secret은 Query Parameter보다 Header가 좋아?

A. 일반적으로 Header 기반 인증이 더 적합하다.

---

## 8.2 Config Object

### [개념]

Config Object는 환경변수에서 읽은 설정값을 코드 내부에서 구조화해 사용하는 방식이다.

API Key, Base URL, Timeout, Model Name 같은 값을 하나의 설정 객체로 묶으면 API Client와 Agent Tool Script에서 재사용하기 쉽다.

---

### [핵심]

- 설정값을 흩어두지 않는다.
- 환경변수 로딩과 검증을 한 곳에서 처리한다.
- API Client는 Config Object를 받아 사용한다.
- Secret은 출력하지 않는다.
- Timeout은 int로 변환한다.
- Config 값 누락 시 명확한 오류를 반환한다.
- Config Object는 Part08의 dataclass 또는 TypedDict와 연결할 수 있다.

---

### [실무]

dict 기반 Config:

```python
import os

def load_config() -> dict:
    api_key = os.environ.get("LLM_API_KEY")

    if not api_key:
        raise ValueError("LLM_API_KEY is required")

    return {
        "api_key": api_key,
        "base_url": os.environ.get("LLM_BASE_URL", "https://api.example.com"),
        "timeout": int(os.environ.get("DEFAULT_TIMEOUT", "30")),
        "model": os.environ.get("MODEL_NAME", "qwen2.5"),
    }
```

Config 사용:

```python
import requests

def call_api(config: dict, prompt: str) -> dict:
    response = requests.post(
        f"{config['base_url']}/v1/chat",
        headers={
            "Authorization": f"Bearer {config['api_key']}",
        },
        json={
            "model": config["model"],
            "messages": [
                {"role": "user", "content": prompt},
            ],
        },
        timeout=config["timeout"],
    )

    response.raise_for_status()
    return response.json()
```

---

### [FAQ]

Q. Config Object는 왜 필요해?

A. 환경변수 로딩, 검증, API Client 설정을 한 곳에서 관리하기 위해 필요하다.

Q. Config에 API Key를 넣어도 돼?

A. 코드 내부 객체로 사용할 수는 있지만 출력하거나 로그로 남기면 안 된다.

Q. Timeout은 왜 int로 변환해야 해?

A. 환경변수는 문자열이므로 API 호출 옵션에 맞게 숫자로 변환해야 한다.

Q. Config 값 누락은 어디서 처리해?

A. Config 로딩 단계에서 처리하는 것이 좋다.

---

# 9. API Client Pattern

## 9.1 API Client Function

### [개념]

API Client Function은 특정 API 호출 로직을 재사용 가능한 Function으로 분리한 구조이다.

Python 자동화에서는 API 호출, Header 생성, Timeout 설정, Response 검증을 Function으로 캡슐화한다.

---

### [핵심]

- API 호출 코드를 Function으로 분리한다.
- Base URL과 API Key는 Config에서 받는다.
- Header 생성 로직을 분리한다.
- Timeout을 설정한다.
- Status Code를 확인한다.
- Response JSON 구조를 검증한다.
- 오류를 구조화해 반환할 수 있다.
- Agent Tool Script에서 재사용하기 좋다.

---

### [실무]

API Client Function:

```python
import requests

def build_headers(api_key: str) -> dict:
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }


def call_chat_api(config: dict, messages: list[dict]) -> dict:
    response = requests.post(
        f"{config['base_url']}/v1/chat",
        headers=build_headers(config["api_key"]),
        json={
            "model": config["model"],
            "messages": messages,
        },
        timeout=config["timeout"],
    )

    response.raise_for_status()
    return response.json()
```

안전한 API Client Function:

```python
import requests

def safe_call_chat_api(config: dict, messages: list[dict]) -> dict:
    try:
        data = call_chat_api(config, messages)

        return {
            "status": "success",
            "result": data,
            "error": None,
        }
    except requests.RequestException as error:
        return {
            "status": "error",
            "result": None,
            "error": str(error),
        }
```

---

### [FAQ]

Q. API Client Function은 왜 필요해?

A. API 호출 로직을 재사용하고 Header, Timeout, 오류 처리를 일관되게 적용하기 위해 필요하다.

Q. Header 생성은 분리하는 게 좋아?

A. 좋다. 인증 방식이 바뀌어도 Header 생성 함수만 수정하면 된다.

Q. API Client Function은 무엇을 반환하면 좋아?

A. 성공 시 API Response dict, 실패 시 구조화된 error dict를 반환하는 것이 좋다.

Q. API Client Function에서 Config를 받는 이유는?

A. Base URL, API Key, Timeout, Model Name을 외부 설정으로 관리하기 위해서이다.

---

## 9.2 API Client Class

### [개념]

API Client Class는 API 호출에 필요한 설정과 메서드를 하나의 객체로 묶는 구조이다.

여러 API Endpoint를 반복 호출하거나 인증 Header, Base URL, Timeout을 공유해야 할 때 유용하다.

---

### [핵심]

- Class는 API 상태와 동작을 묶을 때 사용한다.
- Base URL, API Key, Timeout을 Instance 속성으로 둔다.
- Endpoint별 Method를 만든다.
- 단순 API 호출은 Function만으로도 충분하다.
- 여러 Endpoint와 공통 설정이 있으면 Class가 유용하다.
- Secret을 `__repr__`이나 로그에 노출하지 않는다.
- Part08의 OOP / dataclass 구조와 연결된다.

---

### [실무]

API Client Class:

```python
import requests

class LlmApiClient:
    def __init__(self, base_url: str, api_key: str, timeout: int = 30):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.timeout = timeout

    def build_headers(self) -> dict:
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def chat(self, messages: list[dict], model: str) -> dict:
        response = requests.post(
            f"{self.base_url}/v1/chat",
            headers=self.build_headers(),
            json={
                "model": model,
                "messages": messages,
            },
            timeout=self.timeout,
        )

        response.raise_for_status()
        return response.json()
```

사용:

```python
client = LlmApiClient(
    base_url="https://api.example.com",
    api_key=get_required_env("LLM_API_KEY"),
    timeout=60,
)

result = client.chat(
    messages=[
        {"role": "user", "content": "Generate RAG document"},
    ],
    model="qwen2.5",
)
```

---

### [FAQ]

Q. API Client Class는 언제 사용해?

A. 여러 Endpoint를 호출하고 Base URL, API Key, Timeout 같은 설정을 공유할 때 사용한다.

Q. 단순 API 호출에도 Class가 필요해?

A. 아니다. 단순 호출은 Function으로 충분하다.

Q. API Key를 Class 속성으로 저장해도 돼?

A. 내부 사용은 가능하지만 출력하거나 로그에 노출하면 안 된다.

Q. API Client Class의 장점은?

A. 공통 설정과 API 호출 메서드를 한 곳에 묶어 재사용하기 쉽다.

---

# 10. HTTP API Environment Best Practice

## 10.1 Best Practice

### [개념]

HTTP API Environment Best Practice는 Python 자동화에서 외부 API를 안전하고 안정적으로 호출하기 위한 기준이다.

목표:

```text
Load Config
→ Build Request
→ Send with Timeout
→ Validate Response
→ Handle Error
→ Protect Secret
→ Return Structured Result
```

---

### [핵심]

- API Key는 환경변수로 관리한다.
- `.env`는 로컬 개발용으로만 사용한다.
- `.env`는 Git에 올리지 않는다.
- `.env.example`로 필요한 변수 목록을 공유한다.
- API 호출에는 Timeout을 설정한다.
- Status Code를 확인한다.
- JSON Response 구조를 검증한다.
- API 오류는 구조화된 dict로 반환한다.
- Secret은 로그에 출력하지 않는다.
- Retry는 제한적으로 적용한다.
- 401, 403은 설정 문제로 보고 즉시 확인한다.
- 429는 Rate Limit 정책에 따라 `Retry-After` 확인 후 재시도한다.
- API Client Function 또는 Class로 호출 로직을 분리한다.
- Part05 파일 JSON 검증과 Part06 API JSON 검증의 역할을 구분한다.

---

### [실무]

통합 예시:

```python
import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_required_env(name: str) -> str:
    value = os.environ.get(name)

    if not value:
        raise ValueError(f"{name} is required")

    return value


def load_config() -> dict:
    return {
        "api_key": get_required_env("LLM_API_KEY"),
        "base_url": os.environ.get("LLM_BASE_URL", "https://api.example.com"),
        "model": os.environ.get("MODEL_NAME", "qwen2.5"),
        "timeout": int(os.environ.get("DEFAULT_TIMEOUT", "60")),
    }


def build_headers(api_key: str) -> dict:
    return {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }


def call_llm(config: dict, prompt: str) -> dict:
    try:
        response = requests.post(
            f"{config['base_url']}/v1/chat",
            headers=build_headers(config["api_key"]),
            json={
                "model": config["model"],
                "messages": [
                    {"role": "user", "content": prompt},
                ],
            },
            timeout=config["timeout"],
        )

        response.raise_for_status()

        return {
            "status": "success",
            "result": response.json(),
            "error": None,
        }
    except requests.RequestException as error:
        return {
            "status": "error",
            "result": None,
            "error": str(error),
        }
```

운영 Checklist:

```text
- API Key 하드코딩 없음
- .env Git 제외
- .env.example 제공
- Timeout 설정
- Status Code 확인
- JSON Response 검증
- Secret 로그 출력 없음
- Retry 횟수 제한
- 429 Retry-After 확인
- Error Result 구조화
```

---

### [FAQ]

Q. Python API 호출 Best Practice는 무엇이야?

A. 환경변수 기반 Secret 관리, Timeout 설정, Status Code 확인, JSON 구조 검증, 구조화된 오류 반환이다.

Q. API Key는 어디에 저장해야 해?

A. 환경변수, `.env`, Secret Manager에 저장하고 코드에는 직접 작성하지 않는다.

Q. `.env.example`에는 무엇을 넣어?

A. 필요한 환경변수 이름과 예시 기본값을 넣고 실제 Secret은 넣지 않는다.

Q. API 호출 결과는 어떻게 반환하는 게 좋아?

A. `status`, `result`, `error`를 포함한 dict 구조가 좋다.

Q. Retry는 항상 넣어야 해?

A. 아니다. 일시적 실패에만 제한적으로 적용한다.

Q. 429 응답은 어떻게 처리해?

A. `Retry-After` Header를 확인하고, 없으면 제한된 backoff 후 재시도한다.

---

# Retrieval Queries

### [FAQ]

Q. Python HTTP API Request는 무엇이야?
A. Python 자동화 스크립트가 외부 서비스, LLM API, Backend API, Agent Tool Server와 통신하는 방식이다.

Q. Python 자동화에서 HTTP API Request는 왜 필요해?
A. LLM API, Backend API, 외부 데이터 API, Agent Tool Server와 통신하기 위해 필요하다.

Q. Python API 호출에서 가장 중요한 설정은?
A. Timeout, Status Code 확인, API Key 보안, 오류 처리이다.

Q. Python API Response는 어떤 타입으로 처리해?
A. JSON Response는 보통 dict 또는 list로 처리한다.

Q. Python API Key는 코드에 직접 넣어도 돼?
A. 안 된다. 환경변수나 `.env`로 관리해야 한다.

Q. Python API 호출 실패는 어떻게 처리해?
A. 실패 원인, Status Code, 오류 메시지를 구조화된 dict로 반환하는 것이 좋다.

Q. Part05 JSON 검증과 Part06 JSON 검증은 어떻게 달라?
A. Part05는 파일 기반 JSON 검증이고, Part06은 HTTP API Response JSON 검증이다.

Q. Python requests는 무엇이야?
A. HTTP API를 쉽게 호출하기 위한 Python 외부 라이브러리이다.

Q. requests는 Python 표준 라이브러리야?
A. 아니다. 별도 설치가 필요한 외부 패키지이다.

Q. requests는 언제 사용해?
A. 외부 REST API, LLM API, Backend API, Webhook을 호출할 때 사용한다.

Q. requests에서 timeout은 왜 필요해?
A. API 서버가 응답하지 않을 때 스크립트가 무한 대기하는 것을 막기 위해 필요하다.

Q. response.json은 무엇을 해?
A. JSON Response Body를 Python dict 또는 list로 변환한다.

Q. raise_for_status는 왜 사용해?
A. 4xx, 5xx HTTP 오류를 명확히 예외로 처리하기 위해 사용한다.

Q. Python GET Request는 언제 사용해?
A. 서버에서 데이터를 조회할 때 사용한다.

Q. Python GET Query Parameter는 어떻게 전달해?
A. `params={...}` 형태로 전달한다.

Q. GET Request에 Body를 넣어도 돼?
A. 일반적으로 사용하지 않는다. 조회 조건은 Query Parameter로 전달한다.

Q. API Key를 Query Parameter로 넣어도 돼?
A. 가능하더라도 권장하지 않는다. Header나 환경변수 기반 설정을 우선한다.

Q. Python POST Request는 언제 사용해?
A. 서버에 데이터를 생성하거나 작업 실행을 요청할 때 사용한다.

Q. Python JSON Body는 어떻게 보내?
A. `json=payload` 인자를 사용한다.

Q. LLM API 호출은 GET이야 POST야?
A. 대부분 POST를 사용한다.

Q. POST 요청에서 Content-Type은 무엇이야?
A. 요청 Body 형식을 나타내며 JSON 전송 시 `application/json`을 사용한다.

Q. POST 요청 Body를 로그에 출력해도 돼?
A. 민감정보가 포함될 수 있으므로 그대로 출력하지 않는다.

Q. Python httpx는 무엇이야?
A. 동기와 비동기 HTTP 요청을 모두 지원하는 Python HTTP Client 라이브러리이다.

Q. httpx는 표준 라이브러리야?
A. 아니다. 별도 설치가 필요한 외부 패키지이다.

Q. requests와 httpx 차이는?
A. requests는 단순 동기 요청에 적합하고, httpx는 동기와 비동기 요청을 모두 지원한다.

Q. httpx는 언제 사용해?
A. 비동기 API 호출, 대량 요청, Async Agent Workflow가 필요할 때 사용할 수 있다.

Q. requests와 httpx 중 무엇을 먼저 배우면 돼?
A. 단순 자동화 기준에서는 requests를 먼저 배우면 충분하다.

Q. httpx가 requests보다 항상 좋아?
A. 아니다. 비동기 요청이 필요하지 않으면 requests도 충분히 좋다.

Q. Async API Call이 필요하면 무엇을 써?
A. httpx의 AsyncClient를 사용할 수 있다.

Q. Agent Tool Script에서는 requests와 httpx 중 무엇을 써?
A. 단순 Tool은 requests, 비동기 Tool이나 대량 호출은 httpx를 고려한다.

Q. HTTP Header는 무엇이야?
A. 요청에 포함되는 인증, 데이터 형식, 응답 형식 같은 부가 정보이다.

Q. Authorization Header는 언제 사용해?
A. API Key, Bearer Token, Access Token 같은 인증 정보를 보낼 때 사용한다.

Q. Content-Type은 무엇이야?
A. 요청 Body의 데이터 형식을 나타낸다.

Q. API Key가 들어간 Header를 로그로 남겨도 돼?
A. 안 된다. 민감정보이므로 마스킹하거나 출력하지 않아야 한다.

Q. Query Parameter는 무엇이야?
A. URL에 붙어 검색 조건, 페이지 번호, 필터 조건을 전달하는 key-value 값이다.

Q. Python에서 Query Parameter는 어떻게 전달해?
A. `params={...}` 인자로 전달한다.

Q. URL 문자열에 직접 Query Parameter를 붙여도 돼?
A. 가능하지만 권장하지 않는다. `params`를 사용하면 인코딩과 가독성이 좋아진다.

Q. Secret을 Query Parameter로 전달해도 돼?
A. 권장하지 않는다. URL 로그에 남을 수 있기 때문이다.

Q. JSON Body는 언제 사용해?
A. POST, PUT, PATCH 요청에서 데이터를 생성하거나 수정하거나 작업을 실행할 때 사용한다.

Q. Python requests에서 JSON Body는 어떻게 보내?
A. `json=payload` 인자를 사용한다.

Q. JSON Body에 dict를 넣어도 돼?
A. 가능하다. requests가 JSON 문자열로 변환해 전송한다.

Q. payload 검증은 왜 필요해?
A. 필수 key가 없으면 API 요청이 실패하거나 잘못된 작업이 실행될 수 있기 때문이다.

Q. HTTP Status Code는 무엇이야?
A. API 응답 성공 또는 실패 상태를 나타내는 숫자 코드이다.

Q. HTTP 200은 무슨 뜻이야?
A. 요청이 정상 처리되었다는 의미이다.

Q. HTTP 401은 무슨 뜻이야?
A. 인증 정보가 없거나 잘못되었다는 의미이다.

Q. HTTP 403은 무슨 뜻이야?
A. 인증은 되었지만 접근 권한이 없다는 의미이다.

Q. HTTP 429는 무슨 뜻이야?
A. 요청 횟수 제한을 초과했다는 의미이다.

Q. JSON Response Parsing은 무엇이야?
A. API 응답 Body를 Python dict 또는 list로 변환하는 작업이다.

Q. 응답이 JSON이 아니면 어떻게 돼?
A. JSON 파싱 오류가 발생할 수 있다.

Q. Content-Type은 왜 확인해?
A. 응답 Body가 JSON인지 확인하기 위해 사용한다.

Q. API Response key 검증은 왜 필요해?
A. 예상한 구조가 아니면 이후 자동화 로직이 실패할 수 있기 때문이다.

Q. API Response JSON과 파일 JSON 검증은 같은가?
A. 기본 JSON 구조 검증은 비슷하지만 API Response는 Status Code, Header, Body를 함께 고려해야 한다.

Q. API Timeout은 무엇이야?
A. API 응답을 기다리는 최대 시간이다.

Q. Timeout을 설정하지 않으면 왜 위험해?
A. API 서버가 응답하지 않을 때 스크립트가 무한 대기할 수 있기 때문이다.

Q. 일반 API Timeout은 몇 초가 적당해?
A. 단순 조회는 5~10초 정도를 사용할 수 있다.

Q. LLM API Timeout은 길게 잡아도 돼?
A. 가능하다. 생성 작업은 오래 걸릴 수 있으므로 30~120초를 고려할 수 있다.

Q. API Retry는 언제 사용해?
A. Timeout, 네트워크 오류, 429, 500, 503 같은 일시적 실패에 사용할 수 있다.

Q. 무제한 Retry를 하면 안 되는 이유는?
A. 스크립트가 끝나지 않거나 API 서버에 과도한 부담을 줄 수 있기 때문이다.

Q. 401 오류도 Retry해야 해?
A. 보통 아니다. 인증 정보 오류이므로 API Key나 Token을 확인해야 한다.

Q. 429 오류는 무엇을 의미해?
A. 요청 횟수 제한을 초과했다는 의미이며 대기 후 재시도할 수 있다.

Q. Rate Limit은 무엇이야?
A. API 제공자가 일정 시간 동안 허용하는 요청 수 제한이다.

Q. 429 응답이 오면 바로 다시 요청해도 돼?
A. 권장하지 않는다. Retry-After Header를 확인하거나 backoff를 적용해야 한다.

Q. Retry-After Header는 무엇이야?
A. API가 다시 요청하기 전 기다려야 할 시간을 알려주는 Header이다.

Q. LLM API에서 Rate Limit이 중요한 이유는?
A. 요청 제한과 비용이 함께 영향을 주기 때문에 Batch 호출과 Retry 정책을 조심해야 한다.

Q. Environment Variable은 왜 사용해?
A. API Key와 환경별 설정을 코드와 분리해 보안성과 재사용성을 높이기 위해 사용한다.

Q. API Key를 코드에 직접 작성하면 안 되는 이유는?
A. Git 업로드, 로그, 공유 과정에서 Secret이 노출될 수 있기 때문이다.

Q. `.env` 파일은 Git에 올려도 돼?
A. 안 된다. `.gitignore`에 포함해야 한다.

Q. 환경변수 누락 시 어떻게 처리해?
A. 명확한 오류 메시지를 발생시켜 설정 문제를 빠르게 찾도록 한다.

Q. `.env.example`은 왜 필요해?
A. 실제 Secret 없이 필요한 환경변수 이름과 기본 설정 구조를 공유하기 위해 필요하다.

Q. os.environ은 무엇이야?
A. Python에서 OS 환경변수를 읽고 사용할 수 있는 표준 기능이다.

Q. os.environ.get은 값이 없으면 어떻게 돼?
A. 기본적으로 None을 반환한다.

Q. 필수 환경변수는 어떻게 처리해?
A. 값이 없으면 ValueError를 발생시켜 명확히 실패시키는 것이 좋다.

Q. Secret 기본값을 코드에 넣어도 돼?
A. 안 된다. Secret은 기본값으로도 코드에 넣지 않는다.

Q. 환경변수 숫자값은 바로 int로 사용할 수 있어?
A. 아니다. 환경변수는 문자열로 읽히므로 `int()` 같은 변환이 필요하다.

Q. python-dotenv는 무엇이야?
A. `.env` 파일 값을 Python 환경변수로 로드하는 외부 패키지이다.

Q. python-dotenv는 운영 환경에서도 필수야?
A. 아니다. 운영 환경에서는 OS 환경변수나 Secret Manager를 우선한다.

Q. `.env.example`은 왜 만들어?
A. 필요한 환경변수 목록을 공유하되 실제 Secret은 제외하기 위해 만든다.

Q. API Key를 코드에 직접 넣으면 왜 안 돼?
A. Git, 로그, 화면 공유, 문서 공유 과정에서 Secret이 노출될 수 있기 때문이다.

Q. Secret을 로그에 출력해도 돼?
A. 안 된다. 필요하면 마스킹해서 일부만 표시한다.

Q. API Key가 유출되면 어떻게 해야 해?
A. 즉시 폐기하고 새 Key를 발급해야 한다.

Q. Config Object는 왜 필요해?
A. 환경변수 로딩, 검증, API Client 설정을 한 곳에서 관리하기 위해 필요하다.

Q. Config에 API Key를 넣어도 돼?
A. 코드 내부 객체로 사용할 수는 있지만 출력하거나 로그로 남기면 안 된다.

Q. Timeout은 왜 int로 변환해야 해?
A. 환경변수는 문자열이므로 API 호출 옵션에 맞게 숫자로 변환해야 한다.

Q. API Client Function은 왜 필요해?
A. API 호출 로직을 재사용하고 Header, Timeout, 오류 처리를 일관되게 적용하기 위해 필요하다.

Q. API Client Class는 언제 사용해?
A. 여러 Endpoint를 호출하고 Base URL, API Key, Timeout 같은 설정을 공유할 때 사용한다.

Q. Python API 호출 Best Practice는 무엇이야?
A. 환경변수 기반 Secret 관리, Timeout 설정, Status Code 확인, JSON 구조 검증, 구조화된 오류 반환이다.

Q. API 호출 결과는 어떻게 반환하는 게 좋아?
A. `status`, `result`, `error`를 포함한 dict 구조가 좋다.

Q. 429 응답은 어떻게 처리해?
A. `Retry-After` Header를 확인하고, 없으면 제한된 backoff 후 재시도한다.
