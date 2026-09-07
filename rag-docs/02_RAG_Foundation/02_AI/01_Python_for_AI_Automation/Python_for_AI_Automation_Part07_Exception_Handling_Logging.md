# Python for AI Automation Part07 - Exception Handling Logging

---

# 1. Exception Handling Overview

## 1.1 Exception Handling Role

### [개념]

Exception Handling은 Python 자동화 스크립트에서 오류 발생 시 실패 원인을 명확히 처리하고, 자동화 흐름이 잘못된 상태로 계속 진행되지 않도록 제어하는 방식이다.

Python for AI Automation에서 Exception Handling은 File I/O, JSON Parsing, API Request, Markdown Validation, Agent Tool Script 실행 안정성을 높이는 핵심 기준이다.

기본 Flow:

```text
Risky Operation
→ try
→ Success Result
→ except
→ Error Handling
→ Logging
→ Structured Error Result
```

---

### [핵심]

- Exception은 실행 중 발생하는 오류이다.
- `try / except`는 오류를 처리하는 기본 문법이다.
- 예상 가능한 오류는 구체적인 Exception으로 처리한다.
- `bare except`는 금지한다.
- `except Exception: pass`는 금지한다.
- 오류를 숨기지 말고 원인을 기록한다.
- Agent Tool Script는 실패 결과를 구조화된 dict 또는 JSON으로 반환한다.
- 자동화 스크립트는 실패 지점과 실패 파일을 추적할 수 있어야 한다.
- Agent Tool 최상위 Boundary에서는 예상하지 못한 실패를 구조화하기 위해 마지막에 `Exception`을 잡을 수 있다.
- 내부 로직에서는 구체적인 Exception 처리를 우선한다.

---

### [실무]

2026 실무 기준 Python 자동화에서 Exception Handling은 다음 영역에 필수로 적용한다.

- 파일 없음 처리
- 폴더 없음 처리
- 인코딩 오류 처리
- JSON 파싱 오류 처리
- YAML 파싱 오류 처리
- CSV 컬럼 누락 처리
- API Timeout 처리
- API Status Code 오류 처리
- 환경변수 누락 처리
- Markdown 필수 섹션 누락 처리
- Agent Tool Input Validation 실패 처리

권장 오류 처리 흐름:

```text
Input Validation
→ Execute Task
→ Catch Expected Error
→ Log Context
→ Return Structured Result
```

Exception 처리 기준:

```text
Low-level Function
→ 구체적인 Exception 발생
→ 실패 원인 명확화

Service / Processor Layer
→ 구체적인 Exception 처리
→ Context 추가

Agent Tool Boundary
→ 예상 가능한 Exception 우선 처리
→ 마지막에 Exception을 잡아 구조화된 Error Result 반환 가능
```

---

### [FAQ]

Q. Exception Handling은 왜 필요해?

A. 자동화 실패 원인을 명확히 추적하고 잘못된 결과가 정상 처리처럼 보이지 않게 하기 위해 필요하다.

Q. Python 자동화에서 오류를 무시해도 돼?

A. 안 된다. 오류를 무시하면 원본 파일 훼손, 잘못된 리포트, Agent Tool 오작동이 발생할 수 있다.

Q. Agent Tool Script에서 오류는 어떻게 처리해?

A. `status`, `result`, `error`를 포함한 구조화된 dict로 반환하는 것이 좋다.

Q. bare except는 왜 피해야 해?

A. 모든 오류를 무분별하게 잡아 실제 실패 원인을 숨기기 때문이다.

Q. `except Exception`은 항상 금지야?

A. 아니다. Agent Tool 최상위 Boundary에서는 예상하지 못한 실패도 구조화하기 위해 마지막 안전망으로 사용할 수 있다. 단, 내부 로직에서는 구체적인 Exception을 우선 처리해야 한다.

---

# 2. try except

## 2.1 try except Basics

### [개념]

`try / except`는 오류가 발생할 수 있는 코드를 실행하고, 오류 발생 시 대응 로직을 실행하는 Python 문법이다.

```python
try:
    result = risky_operation()
except ValueError as error:
    print(error)
```

---

### [핵심]

- `try` 블록에는 오류 가능성이 있는 코드를 둔다.
- `except` 블록에는 오류 처리 코드를 둔다.
- 구체적인 Exception Type을 지정한다.
- `as error`로 오류 객체를 받을 수 있다.
- 오류 메시지는 원인 파악이 가능해야 한다.
- 예상 가능한 오류와 예상 불가능한 오류를 구분한다.
- 오류를 단순히 출력하고 숨기지 않는다.
- 호출자가 실패를 알 수 있도록 다시 raise 하거나 구조화된 결과를 반환한다.

---

### [실무]

파일 읽기 오류 처리:

```python
from pathlib import Path

def read_document(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError as error:
        raise FileNotFoundError(f"Document not found: {path}") from error
```

JSON 파싱 오류 처리:

```python
import json
from pathlib import Path

def read_json_file(path: Path) -> dict:
    try:
        text = path.read_text(encoding="utf-8")
        data = json.loads(text)
    except json.JSONDecodeError as error:
        raise ValueError(f"Invalid JSON file: {path}") from error

    if not isinstance(data, dict):
        raise TypeError("JSON root must be object")

    return data
```

구조화된 오류 반환:

```python
from pathlib import Path

def safe_read_document(path: Path) -> dict:
    try:
        text = path.read_text(encoding="utf-8")

        return {
            "status": "success",
            "result": text,
            "error": None,
        }
    except FileNotFoundError as error:
        return {
            "status": "error",
            "result": None,
            "error": str(error),
        }
```

---

### [FAQ]

Q. try 블록에는 무엇을 넣어?

A. 파일 읽기, API 호출, JSON 파싱처럼 실패 가능성이 있는 코드를 넣는다.

Q. except 블록에는 무엇을 넣어?

A. 오류 원인을 기록하거나 구조화된 실패 결과를 반환하는 코드를 넣는다.

Q. except에서 Exception Type을 지정해야 해?

A. 지정하는 것이 좋다. 구체적인 오류를 처리해야 원인 추적이 쉽다.

Q. 오류를 print만 하고 넘어가도 돼?

A. 권장하지 않는다. 오류를 반환하거나 다시 발생시켜 호출자가 알 수 있게 해야 한다.

---

## 2.2 Multiple except

### [개념]

Multiple except는 서로 다른 오류 유형에 따라 다른 처리 로직을 적용하는 방식이다.

파일 처리, API 호출, JSON 파싱처럼 오류 원인이 다양한 자동화 작업에 적합하다.

```python
try:
    data = load_data()
except FileNotFoundError:
    ...
except ValueError:
    ...
```

---

### [핵심]

- 오류 유형별로 다른 처리가 가능하다.
- 구체적인 Exception을 먼저 작성한다.
- 일반적인 Exception은 마지막에 둔다.
- 오류별 메시지를 다르게 작성한다.
- 복구 가능한 오류와 불가능한 오류를 구분한다.
- API Timeout, HTTPError, ConnectionError는 분리하면 후속 대응이 쉬워진다.
- 파일 처리 오류는 파일 경로를 함께 기록한다.

---

### [실무]

파일 + JSON 처리:

```python
import json
from pathlib import Path

def safe_load_json(path: Path) -> dict:
    try:
        text = path.read_text(encoding="utf-8")
        data = json.loads(text)

        return {
            "status": "success",
            "result": data,
            "error": None,
        }

    except FileNotFoundError:
        return {
            "status": "error",
            "result": None,
            "error": f"File not found: {path}",
        }

    except UnicodeDecodeError:
        return {
            "status": "error",
            "result": None,
            "error": f"Encoding error: {path}",
        }

    except json.JSONDecodeError:
        return {
            "status": "error",
            "result": None,
            "error": f"Invalid JSON: {path}",
        }
```

API 오류 처리:

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

    except requests.Timeout:
        return {
            "status": "error",
            "result": None,
            "error": "API timeout",
        }

    except requests.HTTPError as error:
        return {
            "status": "error",
            "result": None,
            "error": f"HTTP error: {error}",
        }

    except requests.RequestException as error:
        return {
            "status": "error",
            "result": None,
            "error": f"Request error: {error}",
        }
```

---

### [FAQ]

Q. Multiple except는 언제 사용해?

A. 파일 없음, 인코딩 오류, JSON 파싱 오류처럼 원인별 처리가 다를 때 사용한다.

Q. except 순서는 중요해?

A. 중요하다. 구체적인 Exception을 먼저 두고 일반적인 Exception을 마지막에 둔다.

Q. 모든 오류를 Exception 하나로 처리해도 돼?

A. 가능하지만 원인별 대응이 어려워지므로 구체적인 Exception 처리를 권장한다.

Q. API Timeout과 HTTPError는 따로 처리하는 게 좋아?

A. 좋다. Timeout은 재시도 가능성이 있고 HTTPError는 상태 코드별 판단이 필요하다.

---

## 2.3 finally

### [개념]

`finally`는 오류 발생 여부와 관계없이 마지막에 실행되는 블록이다.

파일 정리, 임시 리소스 정리, 종료 로그 기록처럼 반드시 실행되어야 하는 작업에 사용한다.

```python
try:
    run_task()
finally:
    cleanup()
```

---

### [핵심]

- `finally`는 성공과 실패 모두에서 실행된다.
- 리소스 정리에 사용할 수 있다.
- 종료 로그 기록에 사용할 수 있다.
- 파일 처리는 `with` 구문을 우선한다.
- `finally`에서 또 다른 오류가 발생하지 않도록 주의한다.
- 자동화 스크립트에서는 임시 파일 정리와 상태 기록에 유용하다.

---

### [실무]

작업 종료 로그:

```python
import logging

logger = logging.getLogger(__name__)

def run_validation() -> None:
    try:
        logger.info("Validation started")
        validate_documents()
    finally:
        logger.info("Validation finished")
```

임시 파일 정리:

```python
from pathlib import Path

def process_temp_file(temp_path: Path) -> None:
    try:
        temp_path.write_text("temporary data", encoding="utf-8")
        process_file(temp_path)
    finally:
        if temp_path.exists():
            temp_path.unlink()
```

권장:

```text
File Open / Close
→ with 사용 우선

Temporary Resource Cleanup
→ finally 사용 가능
```

---

### [FAQ]

Q. finally는 언제 실행돼?

A. try 블록이 성공하든 실패하든 항상 실행된다.

Q. finally는 어디에 사용해?

A. 임시 파일 정리, 종료 로그 기록, 리소스 정리에 사용한다.

Q. 파일 닫기는 finally로 해야 해?

A. 일반 파일 처리는 `with` 구문이 더 안전하고 간단하다.

Q. finally 안에서 오류가 발생하면 어떻게 돼?

A. 원래 오류를 가릴 수 있으므로 finally 내부 로직은 단순하고 안전해야 한다.

---

## 2.4 raise

### [개념]

`raise`는 Python에서 의도적으로 Exception을 발생시키는 문법이다.

입력값이 잘못되었거나 필수 조건이 충족되지 않았을 때 명확한 실패를 만들기 위해 사용한다.

```python
if not file_name:
    raise ValueError("file_name is required")
```

---

### [핵심]

- `raise`는 오류를 직접 발생시킨다.
- 잘못된 입력은 초기에 실패시키는 것이 좋다.
- 필수 환경변수 누락 시 `raise`를 사용한다.
- 파일이나 폴더가 없을 때 명확한 Exception을 발생시킨다.
- `raise ... from error`는 원본 오류 연결에 유용하다.
- 오류 메시지에는 원인과 대상이 포함되어야 한다.
- 자동화 스크립트에서는 조용히 실패하는 것보다 명확한 실패가 안전하다.

---

### [실무]

입력값 검증:

```python
def validate_file_name(file_name: str) -> None:
    if not file_name.strip():
        raise ValueError("file_name is required")
```

환경변수 검증:

```python
import os

def get_required_env(name: str) -> str:
    value = os.environ.get(name)

    if not value:
        raise ValueError(f"{name} is required")

    return value
```

원본 오류 연결:

```python
import json

def parse_json(text: str) -> dict:
    try:
        data = json.loads(text)
    except json.JSONDecodeError as error:
        raise ValueError("Invalid JSON text") from error

    if not isinstance(data, dict):
        raise TypeError("JSON root must be object")

    return data
```

---

### [FAQ]

Q. raise는 언제 사용해?

A. 입력값 누락, 설정 누락, 파일 없음, 잘못된 데이터 구조처럼 명확히 실패해야 하는 상황에 사용한다.

Q. raise를 쓰면 프로그램이 멈춰?

A. 해당 Exception을 처리하지 않으면 실행이 중단된다.

Q. `raise ... from error`는 왜 사용해?

A. 새 오류 메시지를 제공하면서 원본 오류 추적 정보를 유지하기 위해 사용한다.

Q. 오류 메시지는 어떻게 작성해야 해?

A. 무엇이 문제인지, 어떤 값이나 파일에서 발생했는지 알 수 있게 작성한다.

---

# 3. Common Exceptions

## 3.1 FileNotFoundError

### [개념]

`FileNotFoundError`는 지정한 파일 경로가 존재하지 않을 때 발생하는 Exception이다.

File I/O 기반 자동화에서 가장 자주 발생하는 오류 중 하나이다.

---

### [핵심]

- 파일 경로가 틀리면 발생한다.
- 상대경로 기준 위치가 다르면 발생할 수 있다.
- 파일명 오타로 발생할 수 있다.
- 파일 읽기 전 `path.is_file()`로 확인할 수 있다.
- 오류 메시지에는 파일 경로를 포함한다.
- 입력 파일이 필수인 자동화에서는 즉시 실패시키는 것이 좋다.

---

### [실무]

파일 확인:

```python
from pathlib import Path

def require_file(path: Path) -> None:
    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")
```

파일 읽기:

```python
from pathlib import Path

def read_required_file(path: Path) -> str:
    require_file(path)
    return path.read_text(encoding="utf-8")
```

구조화된 결과:

```python
from pathlib import Path

def safe_read_file(path: Path) -> dict:
    try:
        return {
            "status": "success",
            "result": path.read_text(encoding="utf-8"),
            "error": None,
        }
    except FileNotFoundError:
        return {
            "status": "error",
            "result": None,
            "error": f"File not found: {path}",
        }
```

---

### [FAQ]

Q. FileNotFoundError는 언제 발생해?

A. 지정한 파일 경로가 존재하지 않을 때 발생한다.

Q. FileNotFoundError를 줄이려면?

A. 파일 읽기 전 `path.is_file()`로 확인한다.

Q. 상대경로 때문에 FileNotFoundError가 날 수 있어?

A. 가능하다. 현재 작업 디렉터리 기준이 다르면 파일을 찾지 못할 수 있다.

Q. 오류 메시지에 파일 경로를 넣어야 해?

A. 넣는 것이 좋다. 실패 대상을 바로 찾을 수 있기 때문이다.

---

## 3.2 UnicodeDecodeError

### [개념]

`UnicodeDecodeError`는 파일 인코딩과 읽기 encoding이 맞지 않을 때 발생하는 Exception이다.

한글 Markdown, CSV, 로그 파일 처리에서 자주 발생할 수 있다.

---

### [핵심]

- UTF-8이 아닌 파일을 UTF-8로 읽으면 발생할 수 있다.
- 한글 CSV는 CP949인 경우가 있다.
- 파일 읽기 시 encoding을 명시한다.
- 자동화 기준 인코딩은 UTF-8로 통일하는 것이 좋다.
- 오류 발생 시 파일 인코딩 확인이 필요하다.
- fallback 인코딩을 시도할 수 있지만, 최종 실패 시 명확한 오류를 반환한다.
- 직접 `UnicodeDecodeError(...)`를 생성하기보다 `ValueError` 또는 Custom Exception으로 감싸는 것이 실무적으로 더 자연스럽다.

---

### [실무]

UTF-8 읽기:

```python
from pathlib import Path

text = Path("docs/example.md").read_text(encoding="utf-8")
```

대체 인코딩 시도:

```python
from pathlib import Path

def read_text_with_fallback(path: Path) -> str:
    encodings = ["utf-8", "cp949"]

    for encoding in encodings:
        try:
            return path.read_text(encoding=encoding)
        except UnicodeDecodeError:
            continue

    raise ValueError(f"Unable to decode file with supported encodings: {path}")
```

권장:

```text
RAG Markdown
→ UTF-8 통일

외부 CSV
→ UTF-8 우선
→ 필요 시 CP949 확인

fallback 실패
→ ValueError 또는 Custom Exception으로 명확히 실패
```

---

### [FAQ]

Q. UnicodeDecodeError는 언제 발생해?

A. 파일 실제 인코딩과 Python에서 지정한 encoding이 맞지 않을 때 발생한다.

Q. 한글 CSV가 깨질 때 무엇을 확인해?

A. UTF-8인지 CP949인지 확인한다.

Q. RAG Markdown 인코딩은 무엇으로 통일하는 게 좋아?

A. UTF-8로 통일하는 것이 좋다.

Q. encoding을 생략해도 돼?

A. 권장하지 않는다. OS별 기본 인코딩 차이로 문제가 생길 수 있다.

Q. fallback 인코딩을 모두 실패하면 어떤 오류가 좋아?

A. 직접 UnicodeDecodeError를 만들기보다 `ValueError` 또는 Custom Exception으로 명확히 실패시키는 것이 좋다.

---

## 3.3 KeyError

### [개념]

`KeyError`는 dict에서 존재하지 않는 key에 직접 접근할 때 발생하는 Exception이다.

API Response, JSON Config, Agent Tool Output 처리에서 자주 발생한다.

```python
data = {}
value = data["missing_key"]
```

---

### [핵심]

- 존재하지 않는 key에 `dict["key"]`로 접근하면 발생한다.
- 외부 API Response 구조 변경 시 발생할 수 있다.
- JSON Config 필드 누락 시 발생할 수 있다.
- 선택 필드는 `dict.get()`을 사용한다.
- 필수 key는 검증 함수로 먼저 확인한다.
- Agent Tool Output은 key 구조를 표준화한다.

---

### [실무]

안전한 조회:

```python
data = {
    "status": "success",
}

result = data.get("result")
```

필수 key 검증:

```python
def require_keys(data: dict, required_keys: list[str]) -> None:
    missing_keys = [
        key for key in required_keys
        if key not in data
    ]

    if missing_keys:
        raise KeyError(f"Missing keys: {missing_keys}")
```

API Response 검증:

```python
def validate_tool_output(data: dict) -> None:
    require_keys(data, ["status", "result", "error"])
```

---

### [FAQ]

Q. KeyError는 언제 발생해?

A. dict에서 존재하지 않는 key를 직접 조회할 때 발생한다.

Q. KeyError를 줄이려면?

A. 선택 필드는 `get()`을 사용하고 필수 key는 사전에 검증한다.

Q. API Response에서 KeyError가 자주 나는 이유는?

A. 응답 구조가 예상과 다르거나 필드가 누락되었기 때문이다.

Q. 필수 key는 get으로만 처리하면 돼?

A. 필수 key는 누락 시 명확히 실패하도록 검증하는 것이 좋다.

---

## 3.4 ValueError and TypeError

### [개념]

`ValueError`는 값의 형식이나 의미가 잘못되었을 때 발생한다.

`TypeError`는 값의 타입이 기대와 다를 때 발생한다.

---

### [핵심]

- `ValueError`는 값은 들어왔지만 허용되지 않는 경우에 사용한다.
- `TypeError`는 타입 자체가 잘못된 경우에 사용한다.
- Config 값 검증에 자주 사용된다.
- Agent Tool Input 검증에 자주 사용된다.
- 오류 메시지에는 기대 조건을 포함한다.
- Part08 Type Hint와 연결하면 입력/출력 구조를 더 명확히 표현할 수 있다.

---

### [실무]

ValueError:

```python
def validate_chunk_size(chunk_size: int) -> None:
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")
```

TypeError:

```python
def validate_sections(sections: list[str]) -> None:
    if not isinstance(sections, list):
        raise TypeError("sections must be list[str]")
```

Agent Tool Input 검증:

```python
def validate_tool_input(data: dict) -> None:
    if not isinstance(data, dict):
        raise TypeError("tool input must be dict")

    if not data.get("file_path"):
        raise ValueError("file_path is required")
```

---

### [FAQ]

Q. ValueError는 언제 사용해?

A. 값이 존재하지만 허용 범위나 형식이 잘못된 경우 사용한다.

Q. TypeError는 언제 사용해?

A. 입력 타입이 기대와 다른 경우 사용한다.

Q. chunk_size가 0이면 어떤 오류가 적절해?

A. 값 조건이 잘못된 것이므로 ValueError가 적절하다.

Q. list가 와야 하는데 dict가 오면 어떤 오류가 적절해?

A. 타입이 잘못된 것이므로 TypeError가 적절하다.

---

## 3.5 requests Exceptions

### [개념]

requests Exceptions는 HTTP API 호출 중 발생하는 네트워크, Timeout, HTTP 오류를 처리하기 위한 Exception이다.

Python API 자동화에서는 requests 오류를 구체적으로 처리해야 한다.

---

### [핵심]

- `requests.Timeout`은 Timeout 발생 시 사용한다.
- `requests.HTTPError`는 `raise_for_status()`에서 발생한다.
- `requests.ConnectionError`는 연결 실패 시 발생한다.
- `requests.RequestException`은 requests 관련 상위 Exception이다.
- Timeout과 HTTPError는 별도 처리하는 것이 좋다.
- API 오류는 Status Code와 함께 기록한다.
- 429 Rate Limit은 Part06 기준으로 `Retry-After` 확인을 고려한다.

---

### [실무]

requests 오류 처리:

```python
import requests

def safe_api_call(url: str) -> dict:
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

    except requests.HTTPError as error:
        return {
            "status": "error",
            "result": None,
            "error": f"HTTP error: {error}",
        }

    except requests.ConnectionError:
        return {
            "status": "error",
            "result": None,
            "error": "API connection error",
        }

    except requests.RequestException as error:
        return {
            "status": "error",
            "result": None,
            "error": f"API request error: {error}",
        }
```

---

### [FAQ]

Q. requests.Timeout은 언제 발생해?

A. API 응답이 지정한 timeout 시간 안에 오지 않을 때 발생한다.

Q. requests.HTTPError는 언제 발생해?

A. `response.raise_for_status()` 호출 시 4xx, 5xx 응답에서 발생한다.

Q. requests.ConnectionError는 언제 발생해?

A. API 서버에 연결하지 못할 때 발생한다.

Q. requests.RequestException은 무엇이야?

A. requests 관련 오류의 상위 Exception이다.

---

# 4. Custom Exception

## 4.1 Custom Exception Role

### [개념]

Custom Exception은 자동화 도메인에 맞는 오류를 명확히 표현하기 위해 직접 정의하는 Exception이다.

RAG 문서 검증, Agent Tool Input 검증, Config 검증처럼 도메인 의미가 있는 실패를 표현할 때 유용하다.

```python
class DocumentValidationError(Exception):
    pass
```

---

### [핵심]

- Custom Exception은 오류 의미를 명확히 한다.
- 도메인별 오류를 구분할 수 있다.
- RAG 문서 검증 오류를 별도로 표현할 수 있다.
- Agent Tool 오류를 별도로 표현할 수 있다.
- Config 오류를 별도로 표현할 수 있다.
- 너무 많은 Custom Exception은 복잡도를 높인다.
- 기본 Exception으로 충분하면 무리하게 만들지 않는다.

---

### [실무]

RAG 문서 검증 오류:

```python
class DocumentValidationError(Exception):
    """Raised when RAG document validation fails."""
```

Config 오류:

```python
class ConfigError(Exception):
    """Raised when required config is missing or invalid."""
```

Encoding 처리 오류:

```python
class FileEncodingError(Exception):
    """Raised when file encoding cannot be decoded."""
```

사용:

```python
def validate_retrieval_queries(text: str) -> None:
    if "# Retrieval Queries" not in text:
        raise DocumentValidationError("Missing # Retrieval Queries")
```

구조화된 처리:

```python
def safe_validate_document(text: str) -> dict:
    try:
        validate_retrieval_queries(text)

        return {
            "status": "success",
            "result": {"is_valid": True},
            "error": None,
        }

    except DocumentValidationError as error:
        return {
            "status": "error",
            "result": {"is_valid": False},
            "error": str(error),
        }
```

---

### [FAQ]

Q. Custom Exception은 언제 사용해?

A. 기본 Exception만으로 도메인 오류 의미가 충분히 드러나지 않을 때 사용한다.

Q. RAG 문서 검증 오류에 Custom Exception을 써도 돼?

A. 좋다. `DocumentValidationError`처럼 의미 있는 오류로 표현할 수 있다.

Q. Custom Exception을 많이 만들면 좋아?

A. 아니다. 오류 구분이 필요한 경우에만 만든다.

Q. Custom Exception 이름은 어떻게 작성해?

A. `DocumentValidationError`, `ConfigError`, `AgentToolError`처럼 의미가 드러나게 작성한다.

---

# 5. Structured Error Result

## 5.1 Error Result Structure

### [개념]

Structured Error Result는 오류를 단순 문자열이나 print로 처리하지 않고, Agent가 해석 가능한 dict 또는 JSON 형태로 반환하는 방식이다.

Agent Tool Script, RAG Document Automation, API Client Function에서 중요하다.

기본 구조:

```python
{
    "status": "error",
    "result": None,
    "error": "File not found: docs/example.md"
}
```

---

### [핵심]

- 오류 결과는 구조화해서 반환한다.
- `status`는 성공 또는 실패 상태를 나타낸다.
- `result`는 성공 결과 또는 부분 결과를 담는다.
- `error`는 오류 메시지를 담는다.
- 필요하면 `error_type`, `file_path`, `status_code`를 추가한다.
- Agent가 후속 처리를 할 수 있도록 일관된 구조를 사용한다.
- Secret은 error에 포함하지 않는다.
- Part08에서는 이 구조를 `TypedDict` 또는 `dataclass`로 명확히 표현할 수 있다.

---

### [실무]

기본 Error Result:

```python
def build_error_result(message: str) -> dict:
    return {
        "status": "error",
        "result": None,
        "error": message,
    }
```

파일 처리 Error Result:

```python
from pathlib import Path

def build_file_error_result(path: Path, error: Exception) -> dict:
    return {
        "status": "error",
        "result": None,
        "error": str(error),
        "error_type": type(error).__name__,
        "file_path": str(path),
    }
```

API 처리 Error Result:

```python
def build_api_error_result(
    error: Exception,
    status_code: int | None = None,
) -> dict:
    return {
        "status": "error",
        "result": None,
        "error": str(error),
        "error_type": type(error).__name__,
        "status_code": status_code,
    }
```

표준 Output 구조:

```python
{
    "status": "success | error | partial_success",
    "result": {},
    "error": None,
}
```

---

### [FAQ]

Q. Structured Error Result는 왜 필요해?

A. Agent가 실패 원인을 이해하고 후속 처리나 사용자 응답을 안정적으로 만들 수 있기 때문이다.

Q. Error Result 기본 key는 무엇이 좋아?

A. `status`, `result`, `error`를 기본으로 권장한다.

Q. error_type은 왜 추가해?

A. 오류 종류에 따라 후속 처리를 다르게 하기 위해 추가할 수 있다.

Q. error에 API Key를 포함해도 돼?

A. 안 된다. Secret은 오류 메시지에도 포함하면 안 된다.

Q. Part08과 어떻게 연결돼?

A. Part07의 Structured Error Result는 Part08에서 TypedDict 또는 dataclass로 타입 구조를 명확히 할 수 있다.

---

## 5.2 Partial Success Result

### [개념]

Partial Success Result는 전체 자동화 작업 중 일부만 성공하고 일부는 실패했을 때 사용하는 결과 구조이다.

대량 RAG 문서 검증, 파일 일괄 처리, API Batch 처리에서 필요하다.

---

### [핵심]

- 일부 성공과 일부 실패를 구분한다.
- 전체 작업을 중단할지 계속할지 기준을 정한다.
- 성공 목록과 실패 목록을 분리한다.
- 실패 항목에는 원인과 대상 파일을 포함한다.
- Batch Automation에서는 Partial Success가 자주 발생한다.
- 최종 status는 `partial_success`로 표현할 수 있다.
- 성공한 결과와 실패한 결과를 혼합하지 않는다.

---

### [실무]

문서 일괄 검증 결과:

```python
def build_batch_result(successes: list[dict], failures: list[dict]) -> dict:
    if failures and successes:
        status = "partial_success"
    elif failures:
        status = "error"
    else:
        status = "success"

    return {
        "status": status,
        "summary": {
            "success_count": len(successes),
            "failure_count": len(failures),
        },
        "successes": successes,
        "failures": failures,
    }
```

파일별 검증:

```python
from pathlib import Path

def validate_files(paths: list[Path]) -> dict:
    successes = []
    failures = []

    for path in paths:
        try:
            text = path.read_text(encoding="utf-8")
            successes.append({
                "file_path": str(path),
                "length": len(text),
            })
        except Exception as error:
            failures.append({
                "file_path": str(path),
                "error": str(error),
                "error_type": type(error).__name__,
            })

    return build_batch_result(successes, failures)
```

주의:

```text
Batch Boundary
→ Exception catch 가능

Inner Validation Function
→ 구체적인 Exception 발생 권장
```

---

### [FAQ]

Q. Partial Success는 언제 필요해?

A. 여러 파일이나 여러 API 요청 중 일부만 실패했을 때 필요하다.

Q. 일부 파일이 실패하면 전체 작업을 중단해야 해?

A. 작업 목적에 따라 다르다. 검증 리포트 생성은 계속 진행하고 실패 목록을 기록하는 것이 좋다.

Q. Batch Result에는 무엇을 포함해야 해?

A. 성공 개수, 실패 개수, 성공 목록, 실패 목록, 실패 원인을 포함하는 것이 좋다.

Q. partial_success status를 써도 돼?

A. 가능하다. Agent가 전체 성공과 부분 성공을 구분하기 쉽다.

---

# 6. Logging Overview

## 6.1 Logging Role

### [개념]

Logging은 Python 자동화 스크립트의 실행 흐름, 상태, 경고, 오류를 기록하는 방식이다.

Python for AI Automation에서 Logging은 print보다 안정적인 운영성 기록 방식이며, Agent Tool Script, API Client, RAG Document Automation의 문제 추적에 사용한다.

기본 Flow:

```text
Task Start
→ INFO Log
→ Processing
→ WARNING Log
→ Error
→ ERROR Log
→ Task End
```

---

### [핵심]

- `print`는 임시 확인용이다.
- `logging`은 운영성 로그 기록에 적합하다.
- Log Level을 구분한다.
- 오류 발생 시 context를 포함한다.
- Secret을 로그에 출력하지 않는다.
- 대량 작업에서는 파일명과 작업 단계를 로그에 포함한다.
- 로그가 너무 많으면 가독성이 떨어진다.
- Agent Tool Script에서는 사용자 응답과 내부 로그를 구분한다.
- `logger.exception()`은 except 블록 내부에서 사용한다.

---

### [실무]

기본 logging 설정:

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Processing started")
```

작업 로그:

```python
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

def validate_document(path: Path) -> dict:
    logger.info("Validating document: %s", path.name)

    text = path.read_text(encoding="utf-8")
    is_valid = "# Retrieval Queries" in text

    if not is_valid:
        logger.warning("Missing Retrieval Queries: %s", path.name)

    return {
        "file_name": path.name,
        "is_valid": is_valid,
    }
```

오류 로그:

```python
import logging

logger = logging.getLogger(__name__)

try:
    run_task()
except Exception:
    logger.exception("Task failed")
    raise
```

`logger.exception()` 사용 기준:

```text
except 블록 내부
→ logger.exception 사용 가능
→ traceback 포함

일반 흐름
→ logger.info / logger.warning / logger.error 사용
```

---

### [FAQ]

Q. logging은 왜 필요해?

A. 자동화 실행 상태와 실패 원인을 추적하기 위해 필요하다.

Q. print와 logging 차이는?

A. print는 단순 출력이고 logging은 Level, Format, File 저장, 오류 추적을 지원한다.

Q. logger.exception은 언제 사용해?

A. except 블록 내부에서 Exception Traceback을 포함해 오류를 기록해야 할 때 사용한다.

Q. 로그에 Secret을 남겨도 돼?

A. 안 된다. API Key, Token, Credential은 로그에 남기면 안 된다.

---

# 7. Log Level

## 7.1 DEBUG INFO WARNING ERROR CRITICAL

### [개념]

Log Level은 로그 메시지의 중요도를 구분하는 기준이다.

Python logging은 DEBUG, INFO, WARNING, ERROR, CRITICAL Level을 제공한다.

---

### [핵심]

| Level    | 의미             | 사용 예                |
| -------- | ---------------- | ---------------------- |
| DEBUG    | 상세 디버깅 정보 | 변수 값, 세부 흐름     |
| INFO     | 정상 진행 정보   | 작업 시작, 완료        |
| WARNING  | 주의 필요        | 일부 누락, 비권장 설정 |
| ERROR    | 오류 발생        | 파일 실패, API 실패    |
| CRITICAL | 심각한 오류      | 전체 시스템 중단       |

---

### [실무]

Level 사용 예시:

```python
import logging

logger = logging.getLogger(__name__)

logger.debug("Parsed headers: %s", headers)
logger.info("Validation started")
logger.warning("Missing optional section: %s", section)
logger.error("Validation failed: %s", file_name)
logger.critical("Automation stopped due to critical error")
```

RAG 문서 검증 기준:

```text
INFO
→ 문서 검증 시작 / 완료

WARNING
→ Optional Section 누락

ERROR
→ Required Section 누락 / 파일 읽기 실패

CRITICAL
→ 전체 입력 폴더 없음 / Config 불가
```

---

### [FAQ]

Q. INFO는 언제 사용해?

A. 작업 시작, 작업 완료, 처리 개수 같은 정상 흐름 기록에 사용한다.

Q. WARNING은 언제 사용해?

A. 실행은 가능하지만 주의가 필요한 상태에 사용한다.

Q. ERROR는 언제 사용해?

A. 특정 작업이 실패했을 때 사용한다.

Q. DEBUG는 운영 환경에서 항상 켜야 해?

A. 아니다. 너무 많은 로그가 생성될 수 있으므로 필요한 경우에만 사용한다.

---

# 8. Logging Format

## 8.1 Log Format

### [개념]

Log Format은 로그에 시간, Level, Module, 메시지 같은 정보를 어떤 형태로 남길지 정하는 설정이다.

자동화 스크립트에서는 실패 시점과 실패 위치를 추적할 수 있는 Format이 중요하다.

---

### [핵심]

- 시간 정보를 포함한다.
- Log Level을 포함한다.
- Module 이름을 포함한다.
- 메시지를 포함한다.
- 파일명 또는 작업 ID 같은 Context를 추가할 수 있다.
- 너무 긴 Format은 가독성을 낮춘다.
- Secret은 Format이나 메시지에 포함하지 않는다.
- 대량 파일 처리에서는 file path, file name, step 정보를 포함하면 좋다.

---

### [실무]

기본 Format:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
)
```

사용:

```python
logger = logging.getLogger(__name__)
logger.info("Processing file: %s", "part07.md")
```

출력 예시:

```text
2026-06-30 10:30:00 INFO __main__ - Processing file: part07.md
```

Context 포함:

```python
logger.error(
    "Document validation failed: file=%s error=%s",
    file_name,
    error_message,
)
```

---

### [FAQ]

Q. Log Format에는 무엇을 넣는 게 좋아?

A. 시간, Level, Module 이름, 메시지를 포함하는 것이 좋다.

Q. 로그에 파일명을 포함해야 해?

A. 대량 파일 처리에서는 실패 대상을 찾기 위해 포함하는 것이 좋다.

Q. 로그 Format이 너무 길면 문제야?

A. 가독성이 떨어질 수 있으므로 필요한 정보만 포함한다.

Q. 로그 메시지에 API Key를 넣어도 돼?

A. 안 된다. Secret은 절대 로그에 포함하지 않는다.

---

## 8.2 File Logging

### [개념]

File Logging은 로그 메시지를 콘솔이 아니라 파일에 저장하는 방식이다.

장시간 자동화, Batch 검증, Agent Tool 실행 기록 보존에 유용하다.

---

### [핵심]

- 로그 파일은 실행 이력을 남긴다.
- 로그 폴더가 없으면 생성해야 한다.
- 파일 로그는 디버깅과 감사 추적에 유용하다.
- 로그 파일이 너무 커지지 않도록 관리한다.
- 날짜별 로그 파일 또는 Rotating Handler를 고려할 수 있다.
- Secret이 파일 로그에 남지 않도록 주의한다.
- 로그 파일 경로는 Config로 분리할 수 있다.

---

### [실무]

파일 로그 기본 설정:

```python
import logging
from pathlib import Path

log_dir = Path("logs")
log_dir.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
    filename=log_dir / "automation.log",
    encoding="utf-8",
)
```

콘솔 + 파일 로그:

```python
import logging
from pathlib import Path

def setup_logging() -> None:
    log_dir = Path("logs")
    log_dir.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s - %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(
                log_dir / "automation.log",
                encoding="utf-8",
            ),
        ],
    )
```

---

### [FAQ]

Q. File Logging은 언제 사용해?

A. 장시간 자동화, 대량 파일 검증, 실행 기록 보존이 필요할 때 사용한다.

Q. 로그 파일 저장 전 폴더를 만들어야 해?

A. 그렇다. 로그 폴더가 없으면 FileHandler 생성 시 오류가 발생할 수 있다.

Q. 콘솔과 파일에 동시에 로그를 남길 수 있어?

A. 가능하다. StreamHandler와 FileHandler를 함께 사용한다.

Q. 로그 파일이 커지면 어떻게 해?

A. 날짜별 로그 파일이나 RotatingFileHandler를 고려한다.

---

# 9. Secret Masking in Logs

## 9.1 Secret Masking

### [개념]

Secret Masking은 API Key, Token, Password 같은 민감정보가 로그에 그대로 남지 않도록 일부를 숨기는 처리이다.

Python API 자동화와 Agent Tool Script에서는 Secret 로그 노출을 반드시 방지해야 한다.

---

### [핵심]

- API Key를 로그에 그대로 출력하지 않는다.
- Token, Password, Credential도 로그에 출력하지 않는다.
- 필요하면 앞뒤 일부만 남기고 마스킹한다.
- 오류 메시지에 Secret이 포함되지 않게 한다.
- Request Header 전체를 로그로 출력하지 않는다.
- `.env` 내용을 로그로 출력하지 않는다.
- API Error Response에 Secret이 포함될 가능성도 고려한다.

---

### [실무]

Secret Masking 함수:

```python
def mask_secret(secret: str) -> str:
    if not secret:
        return ""

    if len(secret) <= 8:
        return "****"

    return secret[:4] + "****" + secret[-4:]
```

사용:

```python
import logging

logger = logging.getLogger(__name__)

api_key = "sk-example-secret-key"
logger.info("API Key loaded: %s", mask_secret(api_key))
```

Header 로그 금지:

```python
headers = {
    "Authorization": "Bearer secret-token",
}

logger.debug("Request headers prepared")
```

비권장:

```python
logger.debug("Request headers: %s", headers)
```

---

### [FAQ]

Q. Secret Masking은 왜 필요해?

A. 로그 파일, 콘솔 출력, 오류 리포트에 API Key나 Token이 노출되는 것을 막기 위해 필요하다.

Q. Header 전체를 로그로 출력해도 돼?

A. 안 된다. Authorization 값이 포함될 수 있다.

Q. `.env` 내용을 로그로 출력해도 돼?

A. 안 된다. Secret이 포함될 수 있다.

Q. Secret은 일부만 보여줘도 돼?

A. 필요한 경우 앞뒤 일부만 남기고 대부분을 `****`로 마스킹한다.

---

# 10. Exception Handling Logging Best Practice

## 10.1 Best Practice

### [개념]

Exception Handling Logging Best Practice는 Python 자동화 스크립트가 실패를 안전하게 처리하고, 실패 원인을 추적 가능하게 기록하며, Agent가 해석 가능한 결과를 반환하기 위한 기준이다.

목표:

```text
Detect Error
→ Handle Specific Exception
→ Log Context
→ Protect Secret
→ Return Structured Result
→ Stop or Continue by Policy
```

---

### [핵심]

- 예상 가능한 오류를 구체적인 Exception으로 처리한다.
- `bare except`를 사용하지 않는다.
- `except Exception: pass`를 사용하지 않는다.
- 오류 메시지에는 실패 대상과 원인을 포함한다.
- `raise ... from error`로 원본 오류를 연결할 수 있다.
- Batch 작업은 Partial Success Result를 지원한다.
- Agent Tool 오류는 구조화된 dict로 반환한다.
- logging을 사용해 작업 시작, 완료, 실패를 기록한다.
- `logger.exception()`은 except 블록 내부에서 사용한다.
- Log Level을 구분한다.
- Secret은 로그와 오류 메시지에 포함하지 않는다.
- 파일명, 경로, Status Code 같은 Context를 포함한다.
- 처리 가능 오류와 중단해야 할 오류를 구분한다.
- Agent Tool 최상위 Boundary에서만 마지막 안전망으로 `Exception` catch를 사용할 수 있다.

---

### [실무]

통합 예시:

```python
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

class DocumentValidationError(Exception):
    """Raised when RAG document validation fails."""


def read_document(path: Path) -> str:
    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")

    return path.read_text(encoding="utf-8")


def validate_document_text(text: str) -> None:
    required_sections = ["### [개념]", "### [핵심]", "### [실무]", "### [FAQ]"]

    missing_sections = [
        section for section in required_sections
        if section not in text
    ]

    if missing_sections:
        raise DocumentValidationError(f"Missing sections: {missing_sections}")

    if "# Retrieval Queries" not in text:
        raise DocumentValidationError("Missing # Retrieval Queries")


def validate_document_file(path: Path) -> dict:
    logger.info("Document validation started: %s", path.name)

    try:
        text = read_document(path)
        validate_document_text(text)

        logger.info("Document validation success: %s", path.name)

        return {
            "status": "success",
            "result": {
                "file_name": path.name,
                "is_valid": True,
            },
            "error": None,
        }

    except (FileNotFoundError, UnicodeDecodeError, DocumentValidationError) as error:
        logger.error(
            "Document validation failed: file=%s error=%s",
            path,
            error,
        )

        return {
            "status": "error",
            "result": {
                "file_name": path.name,
                "is_valid": False,
            },
            "error": str(error),
            "error_type": type(error).__name__,
        }
```

Agent Tool Boundary 예시:

```python
def run_agent_tool(input_data: dict) -> dict:
    try:
        return execute_tool(input_data)

    except (ValueError, FileNotFoundError, DocumentValidationError) as error:
        return {
            "status": "error",
            "result": None,
            "error": str(error),
            "error_type": type(error).__name__,
        }

    except Exception as error:
        logger.exception("Unexpected agent tool failure")

        return {
            "status": "error",
            "result": None,
            "error": "Unexpected tool failure",
            "error_type": type(error).__name__,
        }
```

검수 Checklist:

```text
- 구체적인 Exception 처리
- bare except 없음
- except pass 없음
- 실패 파일명 포함
- 오류 원인 포함
- logging 사용
- logger.exception은 except 블록 내부에서만 사용
- Secret 로그 출력 없음
- 구조화된 Error Result 반환
- Batch 처리 시 Partial Success 지원
- 최상위 Boundary에서만 Exception catch 허용
```

---

### [FAQ]

Q. Exception Handling Logging Best Practice는 무엇이야?

A. 구체적인 오류 처리, Context 포함 로그, Secret 보호, 구조화된 Error Result 반환을 적용하는 기준이다.

Q. 오류를 처리한 뒤 계속 진행해도 돼?

A. Batch 검증처럼 일부 실패를 허용하는 작업은 계속 진행하고 실패 목록을 기록할 수 있다.

Q. 어떤 오류는 즉시 중단해야 해?

A. 입력 폴더 없음, 필수 Config 누락, API Key 누락처럼 전체 작업 전제가 깨진 오류는 중단하는 것이 좋다.

Q. Agent Tool Script에서 가장 중요한 오류 처리 기준은?

A. 실패를 숨기지 않고 `status`, `result`, `error`, `error_type`으로 구조화해 반환하는 것이다.

Q. 최상위 Agent Tool에서 `Exception`을 잡아도 돼?

A. 가능하다. 예상하지 못한 실패를 구조화된 결과로 반환하기 위한 마지막 안전망으로만 사용한다.

---

# Retrieval Queries

### [FAQ]

Q. Python Exception Handling은 무엇이야?
A. 실행 중 발생하는 오류를 처리하고 실패 원인을 명확히 추적하기 위한 방식이다.

Q. Python 자동화에서 Exception Handling은 왜 필요해?
A. 파일 처리, API 호출, JSON 파싱, Agent Tool 실행 실패를 안전하게 처리하기 위해 필요하다.

Q. Python try except는 무엇이야?
A. 오류 가능성이 있는 코드를 실행하고 오류 발생 시 대응 로직을 실행하는 문법이다.

Q. Python try 블록에는 무엇을 넣어?
A. 파일 읽기, API 호출, JSON 파싱처럼 실패 가능성이 있는 코드를 넣는다.

Q. Python except 블록에는 무엇을 넣어?
A. 오류 원인을 기록하거나 구조화된 실패 결과를 반환하는 코드를 넣는다.

Q. Python except에서 Exception Type을 지정해야 해?
A. 지정하는 것이 좋다. 구체적인 오류를 처리해야 원인 추적이 쉽다.

Q. Python 오류를 print만 하고 넘어가도 돼?
A. 권장하지 않는다. 오류를 반환하거나 다시 발생시켜 호출자가 알 수 있게 해야 한다.

Q. Python Multiple except는 언제 사용해?
A. 파일 없음, 인코딩 오류, JSON 파싱 오류처럼 원인별 처리가 다를 때 사용한다.

Q. Python except 순서는 중요해?
A. 중요하다. 구체적인 Exception을 먼저 두고 일반적인 Exception을 마지막에 둔다.

Q. Python Timeout과 HTTPError는 따로 처리해야 해?
A. 좋다. Timeout은 재시도 가능성이 있고 HTTPError는 상태 코드별 판단이 필요하다.

Q. Python finally는 언제 실행돼?
A. try 블록이 성공하든 실패하든 항상 실행된다.

Q. Python finally는 어디에 사용해?
A. 임시 파일 정리, 종료 로그 기록, 리소스 정리에 사용한다.

Q. Python 파일 닫기는 finally로 해야 해?
A. 일반 파일 처리는 `with` 구문이 더 안전하고 간단하다.

Q. Python raise는 언제 사용해?
A. 입력값 누락, 설정 누락, 파일 없음, 잘못된 데이터 구조처럼 명확히 실패해야 하는 상황에 사용한다.

Q. Python `raise ... from error`는 왜 사용해?
A. 새 오류 메시지를 제공하면서 원본 오류 추적 정보를 유지하기 위해 사용한다.

Q. Python 오류 메시지는 어떻게 작성해야 해?
A. 무엇이 문제인지, 어떤 값이나 파일에서 발생했는지 알 수 있게 작성한다.

Q. FileNotFoundError는 언제 발생해?
A. 지정한 파일 경로가 존재하지 않을 때 발생한다.

Q. FileNotFoundError를 줄이려면?
A. 파일 읽기 전 `path.is_file()`로 확인한다.

Q. 상대경로 때문에 FileNotFoundError가 날 수 있어?
A. 가능하다. 현재 작업 디렉터리 기준이 다르면 파일을 찾지 못할 수 있다.

Q. UnicodeDecodeError는 언제 발생해?
A. 파일 실제 인코딩과 Python에서 지정한 encoding이 맞지 않을 때 발생한다.

Q. 한글 CSV가 깨질 때 무엇을 확인해?
A. UTF-8인지 CP949인지 확인한다.

Q. RAG Markdown 인코딩은 무엇으로 통일하는 게 좋아?
A. UTF-8로 통일하는 것이 좋다.

Q. Python encoding을 생략해도 돼?
A. 권장하지 않는다. OS별 기본 인코딩 차이로 문제가 생길 수 있다.

Q. fallback 인코딩을 모두 실패하면 어떤 오류가 좋아?
A. 직접 UnicodeDecodeError를 만들기보다 ValueError 또는 Custom Exception으로 명확히 실패시키는 것이 좋다.

Q. KeyError는 언제 발생해?
A. dict에서 존재하지 않는 key를 직접 조회할 때 발생한다.

Q. KeyError를 줄이려면?
A. 선택 필드는 `get()`을 사용하고 필수 key는 사전에 검증한다.

Q. API Response에서 KeyError가 자주 나는 이유는?
A. 응답 구조가 예상과 다르거나 필드가 누락되었기 때문이다.

Q. ValueError는 언제 사용해?
A. 값이 존재하지만 허용 범위나 형식이 잘못된 경우 사용한다.

Q. TypeError는 언제 사용해?
A. 입력 타입이 기대와 다른 경우 사용한다.

Q. chunk_size가 0이면 어떤 오류가 적절해?
A. 값 조건이 잘못된 것이므로 ValueError가 적절하다.

Q. list가 와야 하는데 dict가 오면 어떤 오류가 적절해?
A. 타입이 잘못된 것이므로 TypeError가 적절하다.

Q. requests.Timeout은 언제 발생해?
A. API 응답이 지정한 timeout 시간 안에 오지 않을 때 발생한다.

Q. requests.HTTPError는 언제 발생해?
A. `response.raise_for_status()` 호출 시 4xx, 5xx 응답에서 발생한다.

Q. requests.ConnectionError는 언제 발생해?
A. API 서버에 연결하지 못할 때 발생한다.

Q. requests.RequestException은 무엇이야?
A. requests 관련 오류의 상위 Exception이다.

Q. Python Custom Exception은 언제 사용해?
A. 기본 Exception만으로 도메인 오류 의미가 충분히 드러나지 않을 때 사용한다.

Q. RAG 문서 검증 오류에 Custom Exception을 써도 돼?
A. 좋다. `DocumentValidationError`처럼 의미 있는 오류로 표현할 수 있다.

Q. Custom Exception 이름은 어떻게 작성해?
A. `DocumentValidationError`, `ConfigError`, `AgentToolError`처럼 의미가 드러나게 작성한다.

Q. Structured Error Result는 왜 필요해?
A. Agent가 실패 원인을 이해하고 후속 처리나 사용자 응답을 안정적으로 만들 수 있기 때문이다.

Q. Error Result 기본 key는 무엇이 좋아?
A. `status`, `result`, `error`를 기본으로 권장한다.

Q. error_type은 왜 추가해?
A. 오류 종류에 따라 후속 처리를 다르게 하기 위해 추가할 수 있다.

Q. error에 API Key를 포함해도 돼?
A. 안 된다. Secret은 오류 메시지에도 포함하면 안 된다.

Q. Part08과 Structured Error Result는 어떻게 연결돼?
A. Part07의 Structured Error Result는 Part08에서 TypedDict 또는 dataclass로 타입 구조를 명확히 할 수 있다.

Q. Partial Success는 언제 필요해?
A. 여러 파일이나 여러 API 요청 중 일부만 실패했을 때 필요하다.

Q. 일부 파일이 실패하면 전체 작업을 중단해야 해?
A. 작업 목적에 따라 다르다. 검증 리포트 생성은 계속 진행하고 실패 목록을 기록하는 것이 좋다.

Q. Batch Result에는 무엇을 포함해야 해?
A. 성공 개수, 실패 개수, 성공 목록, 실패 목록, 실패 원인을 포함하는 것이 좋다.

Q. Python logging은 왜 필요해?
A. 자동화 실행 상태와 실패 원인을 추적하기 위해 필요하다.

Q. print와 logging 차이는?
A. print는 단순 출력이고 logging은 Level, Format, File 저장, 오류 추적을 지원한다.

Q. logger.exception은 언제 사용해?
A. except 블록 내부에서 Exception Traceback을 포함해 오류를 기록해야 할 때 사용한다.

Q. 로그에 Secret을 남겨도 돼?
A. 안 된다. API Key, Token, Credential은 로그에 남기면 안 된다.

Q. Python INFO 로그는 언제 사용해?
A. 작업 시작, 작업 완료, 처리 개수 같은 정상 흐름 기록에 사용한다.

Q. Python WARNING 로그는 언제 사용해?
A. 실행은 가능하지만 주의가 필요한 상태에 사용한다.

Q. Python ERROR 로그는 언제 사용해?
A. 특정 작업이 실패했을 때 사용한다.

Q. Python DEBUG 로그는 운영 환경에서 항상 켜야 해?
A. 아니다. 너무 많은 로그가 생성될 수 있으므로 필요한 경우에만 사용한다.

Q. Python Log Format에는 무엇을 넣는 게 좋아?
A. 시간, Level, Module 이름, 메시지를 포함하는 것이 좋다.

Q. Python 로그에 파일명을 포함해야 해?
A. 대량 파일 처리에서는 실패 대상을 찾기 위해 포함하는 것이 좋다.

Q. Python File Logging은 언제 사용해?
A. 장시간 자동화, 대량 파일 검증, 실행 기록 보존이 필요할 때 사용한다.

Q. 로그 파일 저장 전 폴더를 만들어야 해?
A. 그렇다. 로그 폴더가 없으면 FileHandler 생성 시 오류가 발생할 수 있다.

Q. 콘솔과 파일에 동시에 로그를 남길 수 있어?
A. 가능하다. StreamHandler와 FileHandler를 함께 사용한다.

Q. Secret Masking은 왜 필요해?
A. 로그 파일, 콘솔 출력, 오류 리포트에 API Key나 Token이 노출되는 것을 막기 위해 필요하다.

Q. Header 전체를 로그로 출력해도 돼?
A. 안 된다. Authorization 값이 포함될 수 있다.

Q. `.env` 내용을 로그로 출력해도 돼?
A. 안 된다. Secret이 포함될 수 있다.

Q. Exception Handling Logging Best Practice는 무엇이야?
A. 구체적인 오류 처리, Context 포함 로그, Secret 보호, 구조화된 Error Result 반환을 적용하는 기준이다.

Q. Agent Tool Script에서 가장 중요한 오류 처리 기준은?
A. 실패를 숨기지 않고 `status`, `result`, `error`, `error_type`으로 구조화해 반환하는 것이다.

Q. 최상위 Agent Tool에서 Exception을 잡아도 돼?
A. 가능하다. 예상하지 못한 실패를 구조화된 결과로 반환하기 위한 마지막 안전망으로만 사용한다.
