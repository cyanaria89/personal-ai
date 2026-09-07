# Python for AI Automation Part08 - Type Hint Dataclass OOP

---

# 1. Type Hint Overview

## 1.1 Type Hint Role

### [개념]

Type Hint는 Python 코드에서 변수, 함수 Parameter, Return Value의 예상 타입을 명시하는 문법이다.

Python for AI Automation에서 Type Hint는 Agent가 코드 구조를 이해하고, Function Input / Output을 검증하고, 자동화 스크립트의 유지보수성과 리뷰 품질을 높이는 데 중요하다.

Part07의 Structured Error Result는 Part08에서 `TypedDict` 또는 `dataclass`로 타입 구조를 명확히 표현할 수 있다.

기본 Flow:

```text
Function Input
→ Type Hint
→ Processing
→ Return Type
→ Agent Code Review
```

---

### [핵심]

- Type Hint는 런타임 타입 강제가 아니다.
- Type Hint는 코드 이해와 정적 분석을 돕는다.
- Function Parameter와 Return Type에 우선 적용한다.
- Agent Tool Script는 입력과 출력 타입이 명확해야 한다.
- RAG Document Automation에서는 `Path`, `dict`, `list`, `str`, `bool` 타입이 자주 사용된다.
- 복잡한 dict는 `TypedDict` 또는 `dataclass`를 고려한다.
- Part07의 `status`, `result`, `error` 구조는 Part08에서 타입화할 수 있다.
- Type Hint와 실제 반환값이 다르면 코드 신뢰성이 떨어진다.

---

### [실무]

2026 실무 기준 Python 자동화에서는 Type Hint를 기본 품질 기준으로 사용한다.

권장 예시:

```python
from pathlib import Path

def read_document(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def has_retrieval_queries(text: str) -> bool:
    return "# Retrieval Queries" in text


def build_result(file_name: str, is_valid: bool) -> dict:
    return {
        "file_name": file_name,
        "is_valid": is_valid,
    }
```

Agent가 이해하기 좋은 함수 구조:

```python
from pathlib import Path

def validate_markdown_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")

    return {
        "status": "success",
        "result": {
            "file_name": path.name,
            "has_faq": "### [FAQ]" in text,
            "has_retrieval_queries": "# Retrieval Queries" in text,
        },
        "error": None,
    }
```

Part07 Error Result와 Part08 Type 구조 연결:

```text
Part07
→ Structured Error Result
→ status / result / error

Part08
→ TypedDict
→ dataclass
→ Literal Status
→ Agent Tool Output Type
```

---

### [FAQ]

Q. Type Hint는 Python에서 필수야?

A. 문법적으로 필수는 아니지만 자동화 코드, Agent Tool Script, 코드 리뷰 품질을 위해 권장한다.

Q. Type Hint는 런타임에 타입을 강제해?

A. 아니다. 기본 Python Type Hint는 런타임 타입 강제가 아니라 코드 이해와 정적 분석을 돕는다.

Q. Type Hint는 어디에 먼저 적용해야 해?

A. Function Parameter와 Return Type에 먼저 적용하는 것이 좋다.

Q. Agent Tool Script에 Type Hint가 중요한 이유는?

A. Agent가 Tool Input과 Output 구조를 더 명확히 이해하고 검증할 수 있기 때문이다.

Q. Part07의 Structured Error Result와 Part08은 어떻게 연결돼?

A. Part07의 `status`, `result`, `error` 구조를 Part08에서 `TypedDict`, `Literal`, `dataclass`로 명확히 타입화할 수 있다.

---

# 2. Basic Type Hint

## 2.1 Primitive Type Hint

### [개념]

Primitive Type Hint는 `str`, `int`, `float`, `bool`, `None` 같은 기본 타입을 명시하는 방식이다.

자동화 코드에서는 파일명, 점수, 개수, 성공 여부, 오류 없음 상태를 표현할 때 사용한다.

```python
def normalize_title(title: str) -> str:
    return title.strip()
```

---

### [핵심]

- `str`은 문자열 타입이다.
- `int`는 정수 타입이다.
- `float`는 실수 타입이다.
- `bool`은 참/거짓 타입이다.
- `None`은 값 없음 또는 반환값 없음에 사용한다.
- 반환값이 없는 함수는 `-> None`을 사용한다.
- Type Hint는 실제 반환값과 일치해야 한다.
- 자동화 코드에서는 `bool` 반환 함수 이름을 명확히 작성한다.

---

### [실무]

문자열 처리:

```python
def clean_file_name(file_name: str) -> str:
    return file_name.strip()
```

숫자 검증:

```python
def validate_chunk_size(chunk_size: int) -> None:
    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive")
```

Boolean 반환:

```python
def is_markdown_file(file_name: str) -> bool:
    return file_name.endswith(".md")
```

점수 계산:

```python
def calculate_quality_score(valid_count: int, total_count: int) -> float:
    if total_count == 0:
        return 0.0

    return valid_count / total_count * 100
```

---

### [FAQ]

Q. 반환값이 없는 함수는 Type Hint를 어떻게 써?

A. `-> None`을 사용한다.

Q. bool Type Hint는 언제 사용해?

A. 검증 성공 여부, 파일 존재 여부, 필수 섹션 포함 여부처럼 참/거짓 결과를 반환할 때 사용한다.

Q. int와 float는 어떻게 구분해?

A. 개수, 순서, 크기는 int를 쓰고 점수, 비율, 소수 계산은 float를 사용한다.

Q. Type Hint와 실제 반환값이 다르면 문제야?

A. 그렇다. Agent와 개발자가 코드를 잘못 이해할 수 있고 정적 분석 결과도 신뢰하기 어렵다.

---

## 2.2 Collection Type Hint

### [개념]

Collection Type Hint는 `list`, `dict`, `tuple`, `set` 같은 Collection Data Type의 내부 타입을 명시하는 방식이다.

Python 3.9+에서는 `list[str]`, `dict[str, int]` 같은 표기를 사용할 수 있다.

```python
def find_missing_sections(text: str, sections: list[str]) -> list[str]:
    return [
        section for section in sections
        if section not in text
    ]
```

---

### [핵심]

- `list[str]`는 문자열 list이다.
- `dict[str, str]`는 key와 value가 문자열인 dict이다.
- `dict[str, object]`는 다양한 value 타입을 가진 dict에 사용할 수 있다.
- `tuple[str, str]`는 문자열 2개로 구성된 tuple이다.
- `set[str]`는 문자열 set이다.
- 복잡한 dict는 `TypedDict` 또는 `dataclass`를 고려한다.
- `list`만 쓰는 것보다 `list[str]`처럼 내부 타입을 명시하는 것이 좋다.
- Agent Tool Output처럼 구조가 고정된 dict는 일반 `dict`보다 `TypedDict`가 더 명확하다.

---

### [실무]

list Type Hint:

```python
def scan_file_names() -> list[str]:
    return ["part01.md", "part02.md"]
```

dict Type Hint:

```python
def build_metadata(file_name: str) -> dict[str, str]:
    return {
        "file_name": file_name,
        "domain": "Python for AI Automation",
    }
```

복합 dict:

```python
def build_validation_result(
    file_name: str,
    is_valid: bool,
    missing_sections: list[str],
) -> dict[str, object]:
    return {
        "file_name": file_name,
        "is_valid": is_valid,
        "missing_sections": missing_sections,
    }
```

set Type Hint:

```python
def find_duplicate_keywords(keywords: list[str]) -> set[str]:
    seen: set[str] = set()
    duplicates: set[str] = set()

    for keyword in keywords:
        if keyword in seen:
            duplicates.add(keyword)
        seen.add(keyword)

    return duplicates
```

---

### [FAQ]

Q. list Type Hint는 어떻게 써?

A. 문자열 목록이면 `list[str]`, 정수 목록이면 `list[int]`처럼 작성한다.

Q. dict Type Hint는 어떻게 써?

A. key와 value 타입을 명시해 `dict[str, str]`, `dict[str, object]`처럼 작성한다.

Q. dict[str, object]는 언제 사용해?

A. value에 str, bool, list처럼 여러 타입이 섞인 dict를 반환할 때 사용할 수 있다.

Q. 복잡한 dict도 Type Hint만으로 충분해?

A. 복잡한 구조라면 `TypedDict` 또는 `dataclass`를 사용하는 것이 더 명확하다.

---

# 3. Optional Union Literal Callable

## 3.1 Optional and None

### [개념]

`Optional`은 값이 특정 타입이거나 `None`일 수 있음을 표현하는 Type Hint이다.

Python 3.10+에서는 `str | None` 형태를 권장할 수 있다.

```python
def find_error_message() -> str | None:
    return None
```

---

### [핵심]

- 값이 없을 수 있으면 `| None`을 명시한다.
- `str | None`은 문자열 또는 None을 의미한다.
- `Path | None`은 Path 객체 또는 None을 의미한다.
- Optional 값은 사용 전 None 체크가 필요하다.
- Agent Tool Output의 `error`는 `str | None` 형태가 자주 사용된다.
- `result`도 실패 시 `None`이 될 수 있다.
- Optional 구조는 Part07 Error Result와 직접 연결된다.

---

### [실무]

오류 메시지:

```python
def build_success_result() -> dict[str, object]:
    return {
        "status": "success",
        "result": {},
        "error": None,
    }
```

None 가능 반환:

```python
def extract_first_header(text: str) -> str | None:
    for line in text.splitlines():
        if line.startswith("#"):
            return line

    return None
```

None 체크:

```python
header = extract_first_header("# Title")

if header is None:
    raise ValueError("Header not found")
```

환경변수:

```python
import os

def get_env(name: str) -> str | None:
    return os.environ.get(name)
```

---

### [FAQ]

Q. `str | None`은 무슨 뜻이야?

A. 값이 문자열이거나 None일 수 있다는 의미이다.

Q. Optional 값은 바로 사용해도 돼?

A. 아니다. None 가능성이 있으므로 사용 전 None 체크를 하는 것이 좋다.

Q. error 필드는 어떤 Type Hint가 좋아?

A. 성공 시 None, 실패 시 문자열이므로 `str | None` 구조가 적합하다.

Q. Python 3.10 이전에는 Optional을 어떻게 썼어?

A. `from typing import Optional` 후 `Optional[str]`처럼 사용했다.

---

## 3.2 Union

### [개념]

Union은 값이 여러 타입 중 하나일 수 있음을 표현하는 Type Hint이다.

Python 3.10+에서는 `str | int`처럼 `|` 연산자를 사용한다.

```python
def normalize_value(value: str | int) -> str:
    return str(value)
```

---

### [핵심]

- Union은 여러 가능한 타입을 표현한다.
- Python 3.10+에서는 `A | B` 표기를 사용할 수 있다.
- 지나치게 많은 Union은 코드 이해를 어렵게 만든다.
- 가능하면 입력 타입을 단순하게 유지한다.
- 외부 JSON 값 처리에서 Union이 필요할 수 있다.
- `str | Path`는 파일 경로 처리에서 자주 사용된다.

---

### [실무]

문자열 또는 숫자 처리:

```python
def to_text(value: str | int | float) -> str:
    return str(value)
```

Path 또는 문자열 처리:

```python
from pathlib import Path

def normalize_path(path: str | Path) -> Path:
    return Path(path)
```

JSON 값 타입:

```python
JsonPrimitive = str | int | float | bool | None

def stringify_json_value(value: JsonPrimitive) -> str:
    return str(value)
```

---

### [FAQ]

Q. Union은 언제 사용해?

A. 입력값이 여러 타입 중 하나일 수 있을 때 사용한다.

Q. `str | Path`는 무슨 뜻이야?

A. 문자열 경로나 Path 객체 둘 다 받을 수 있다는 의미이다.

Q. Union 타입을 많이 쓰면 좋아?

A. 아니다. 너무 많은 타입을 허용하면 코드 검증과 이해가 어려워진다.

Q. JSON 값 처리에 Union이 필요한 이유는?

A. JSON value는 문자열, 숫자, bool, null 등 여러 타입이 될 수 있기 때문이다.

---

## 3.3 Literal

### [개념]

`Literal`은 특정 문자열이나 값만 허용하는 Type Hint이다.

상태값, 옵션, 실행 모드, 출력 형식처럼 허용 값이 정해진 경우에 사용한다.

```python
from typing import Literal

Status = Literal["success", "error", "partial_success"]
```

---

### [핵심]

- Literal은 허용 값을 제한한다.
- Agent Tool Output의 status 값에 유용하다.
- 실행 모드 `dry_run`, `execute` 같은 값에 사용할 수 있다.
- 파일 형식 `json`, `csv`, `markdown` 같은 값에 사용할 수 있다.
- 허용 값이 많아지면 Enum 사용도 고려한다.
- Part07, Part10의 `status`, `result`, `error` 구조는 `Status` Literal로 통일하는 것이 좋다.

---

### [실무]

Status Literal:

```python
from typing import Literal

Status = Literal["success", "error", "partial_success"]

def build_result(status: Status, result: dict | None, error: str | None) -> dict:
    return {
        "status": status,
        "result": result,
        "error": error,
    }
```

Mode Literal:

```python
from typing import Literal

RunMode = Literal["dry_run", "execute"]

def run_file_update(mode: RunMode) -> None:
    if mode == "dry_run":
        print("Preview only")
    elif mode == "execute":
        print("Execute update")
```

Format Literal:

```python
from typing import Literal

OutputFormat = Literal["json", "csv", "markdown"]

def save_report(format: OutputFormat) -> None:
    ...
```

---

### [FAQ]

Q. Literal은 언제 사용해?

A. 허용 가능한 문자열이나 값이 정해져 있을 때 사용한다.

Q. Agent Tool Output status에 Literal을 써도 돼?

A. 좋다. `success`, `error`, `partial_success` 같은 값으로 제한할 수 있다.

Q. 실행 모드에 Literal을 써도 돼?

A. 좋다. `dry_run`, `execute`처럼 위험 작업 모드를 제한할 수 있다.

Q. Literal과 Enum 중 무엇을 써?

A. 단순한 값 제한은 Literal, 더 구조적인 상수 관리가 필요하면 Enum을 고려한다.

---

## 3.4 Callable

### [개념]

`Callable`은 함수 자체를 인자로 받거나 반환할 때 사용하는 Type Hint이다.

Python 자동화에서는 validator, transformer, callback, filter function을 전달할 때 사용할 수 있다.

```python
from collections.abc import Callable

def apply_transform(text: str, transform: Callable[[str], str]) -> str:
    return transform(text)
```

---

### [핵심]

- Callable은 호출 가능한 객체 타입이다.
- 함수형 처리에 사용할 수 있다.
- Validator Function 주입에 유용하다.
- Transformer Function 주입에 유용하다.
- 너무 복잡한 Callable 타입은 가독성을 낮출 수 있다.
- 간단한 자동화에서는 직접 함수 호출이 더 명확할 수 있다.
- Callable 구조가 커지면 Protocol을 고려할 수 있다.

---

### [실무]

Transformer Function:

```python
from collections.abc import Callable

def clean_markdown_title(title: str) -> str:
    return title.strip().replace("#", "").strip()


def apply_title_transform(
    title: str,
    transform: Callable[[str], str],
) -> str:
    return transform(title)
```

Validator Function:

```python
from collections.abc import Callable

def validate_not_empty(text: str) -> bool:
    return bool(text.strip())


def run_validation(
    text: str,
    validator: Callable[[str], bool],
) -> bool:
    return validator(text)
```

Batch Transform:

```python
from collections.abc import Callable

def transform_items(
    items: list[str],
    transform: Callable[[str], str],
) -> list[str]:
    return [transform(item) for item in items]
```

---

### [FAQ]

Q. Callable은 언제 사용해?

A. 함수 자체를 인자로 전달하거나 Validator, Transformer를 교체 가능하게 만들 때 사용한다.

Q. Callable[[str], str]은 무슨 뜻이야?

A. 문자열 하나를 입력받고 문자열을 반환하는 함수라는 뜻이다.

Q. Callable은 자동화에서 필수야?

A. 필수는 아니지만 변환 로직이나 검증 로직을 주입할 때 유용하다.

Q. Callable 타입이 너무 복잡하면 어떻게 해?

A. Type Alias를 만들거나 일반 함수 호출 구조로 단순화한다.

---

# 4. TypedDict

## 4.1 TypedDict Role

### [개념]

`TypedDict`는 dict의 key와 value 타입을 명시하는 Type Hint이다.

Agent Tool Output, Validation Result, Document Metadata처럼 dict 구조가 정해져 있을 때 사용한다.

```python
from typing import TypedDict

class ValidationResult(TypedDict):
    file_name: str
    is_valid: bool
    missing_sections: list[str]
```

---

### [핵심]

- TypedDict는 dict 구조를 명시한다.
- key 이름과 value 타입을 정의한다.
- JSON 호환 결과 구조에 적합하다.
- Agent Tool Output 타입 표현에 유용하다.
- 런타임 검증을 자동으로 수행하지는 않는다.
- 복잡한 중첩 구조는 dataclass와 비교해 선택한다.
- `status`는 `Literal["success", "error", "partial_success"]`로 통일하면 좋다.
- Part07 Error Result, Part10 Agent Tool Output과 직접 연결된다.

---

### [실무]

Validation Result:

```python
from typing import TypedDict

class ValidationResult(TypedDict):
    file_name: str
    is_valid: bool
    missing_sections: list[str]
    has_retrieval_queries: bool


def validate_document(text: str, file_name: str) -> ValidationResult:
    required_sections = ["### [개념]", "### [핵심]", "### [실무]", "### [FAQ]"]

    missing_sections = [
        section for section in required_sections
        if section not in text
    ]

    return {
        "file_name": file_name,
        "is_valid": len(missing_sections) == 0,
        "missing_sections": missing_sections,
        "has_retrieval_queries": "# Retrieval Queries" in text,
    }
```

Agent Tool Output 표준 구조:

```python
from typing import Literal, TypedDict

Status = Literal["success", "error", "partial_success"]

class ToolOutput(TypedDict):
    status: Status
    result: dict | None
    error: str | None
```

Document Metadata:

```python
from typing import TypedDict

class DocumentMetadata(TypedDict):
    file_name: str
    title: str
    domain: str
    part: int
```

---

### [FAQ]

Q. TypedDict는 언제 사용해?

A. dict 구조가 고정되어 있고 key와 value 타입을 명확히 하고 싶을 때 사용한다.

Q. TypedDict는 런타임 검증을 해?

A. 아니다. Type Hint 용도이며 런타임 검증은 별도 코드가 필요하다.

Q. Agent Tool Output에 TypedDict를 써도 돼?

A. 좋다. `status`, `result`, `error` 구조를 명확히 표현할 수 있다.

Q. TypedDict와 dataclass 차이는?

A. TypedDict는 dict 구조 타입 힌트이고, dataclass는 실제 데이터 객체를 생성한다.

Q. ToolOutput의 status 타입은 어떻게 통일하는 게 좋아?

A. `Literal["success", "error", "partial_success"]` 기반 `Status` 타입으로 통일하는 것이 좋다.

---

## 4.2 ToolOutput Standard Type

### [개념]

ToolOutput Standard Type은 Agent Tool Script가 반환하는 결과 구조를 표준화한 타입이다.

Python for AI Automation에서는 Part07의 Structured Error Result와 Part10의 Agent Tool Script 출력을 동일한 구조로 맞추는 것이 중요하다.

표준 구조:

```python
{
    "status": "success | error | partial_success",
    "result": {},
    "error": None
}
```

---

### [핵심]

- Tool Output은 JSON 호환 dict 구조를 사용한다.
- `status`는 `success`, `error`, `partial_success`로 제한한다.
- `result`는 성공 결과 또는 부분 결과이다.
- `error`는 성공 시 `None`, 실패 시 문자열이다.
- 실패 시 `error_type`, `file_path`, `status_code`를 추가할 수 있다.
- 모든 Part에서 ToolOutput 구조를 동일하게 유지한다.
- Agent가 후속 처리를 하기 쉽게 출력 구조를 고정한다.

---

### [실무]

표준 ToolOutput:

```python
from typing import Literal, TypedDict

Status = Literal["success", "error", "partial_success"]

class ToolOutput(TypedDict):
    status: Status
    result: dict | None
    error: str | None
```

확장 Error Output:

```python
class ErrorToolOutput(TypedDict):
    status: Literal["error"]
    result: None
    error: str
    error_type: str
```

생성 함수:

```python
def build_tool_output(
    status: Status,
    result: dict | None,
    error: str | None,
) -> ToolOutput:
    return {
        "status": status,
        "result": result,
        "error": error,
    }
```

성공 Output:

```python
output = build_tool_output(
    status="success",
    result={"is_valid": True},
    error=None,
)
```

실패 Output:

```python
output = build_tool_output(
    status="error",
    result=None,
    error="File not found: docs/example.md",
)
```

---

### [FAQ]

Q. ToolOutput Standard Type은 왜 필요해?

A. Agent가 Tool 실행 결과를 일관되게 해석하고 후속 작업을 안정적으로 수행하기 위해 필요하다.

Q. ToolOutput의 status는 어떤 값이 좋아?

A. `success`, `error`, `partial_success`로 통일하는 것이 좋다.

Q. 실패 시 result는 무엇이 좋아?

A. 보통 `None`을 사용하고, 부분 결과가 있으면 `partial_success`에서 별도 구조로 표현한다.

Q. error_type은 필수야?

A. 필수는 아니지만 오류 종류별 후속 처리가 필요하면 추가하는 것이 좋다.

---

# 5. Dataclass

## 5.1 Dataclass Role

### [개념]

Dataclass는 Python에서 구조화된 데이터 객체를 간단하게 정의하기 위한 기능이다.

Python for AI Automation에서는 Document Metadata, Validation Result, Config, Chunk Metadata, Agent Tool Result 같은 구조화된 데이터를 표현할 때 유용하다.

```python
from dataclasses import dataclass

@dataclass
class DocumentMeta:
    file_name: str
    title: str
    domain: str
```

---

### [핵심]

- dataclass는 단순 데이터 객체에 적합하다.
- boilerplate 코드를 줄인다.
- 필드 타입을 명확히 표현한다.
- 설정값, 메타데이터, 처리 결과 표현에 유용하다.
- `asdict()`로 dict 변환이 가능하다.
- JSON 저장 전 dict 변환이 필요하다.
- 복잡한 비즈니스 로직을 dataclass에 과도하게 넣지 않는다.
- Agent Tool Output을 JSON으로 반환할 때는 `asdict()` 변환을 고려한다.

---

### [실무]

Document Metadata:

```python
from dataclasses import dataclass

@dataclass
class DocumentMeta:
    file_name: str
    title: str
    domain: str
    part: int
```

Validation Result:

```python
from dataclasses import dataclass

@dataclass
class ValidationResult:
    file_name: str
    is_valid: bool
    missing_sections: list[str]
    has_retrieval_queries: bool
```

사용:

```python
result = ValidationResult(
    file_name="part08.md",
    is_valid=True,
    missing_sections=[],
    has_retrieval_queries=True,
)
```

dict 변환:

```python
from dataclasses import asdict

result_dict = asdict(result)
```

---

### [FAQ]

Q. dataclass는 언제 사용해?

A. 문서 메타데이터, 설정값, 검증 결과처럼 구조가 정해진 데이터를 표현할 때 사용한다.

Q. dataclass는 dict보다 좋은가?

A. 구조가 명확하고 필드 타입을 표현할 수 있어 복잡한 데이터에는 dict보다 유리할 수 있다.

Q. dataclass를 JSON으로 바로 저장할 수 있어?

A. 보통 `asdict()`로 dict 변환 후 JSON 저장한다.

Q. dataclass에 복잡한 로직을 넣어도 돼?

A. 권장하지 않는다. dataclass는 단순 데이터 표현 중심으로 사용하는 것이 좋다.

---

## 5.2 field and default_factory

### [개념]

`field`는 dataclass 필드의 기본값, 생성 방식, 메타데이터를 세부 설정하는 기능이다.

`default_factory`는 list, dict, set 같은 mutable 기본값을 안전하게 생성할 때 사용한다.

```python
from dataclasses import dataclass, field

@dataclass
class ValidationResult:
    file_name: str
    missing_sections: list[str] = field(default_factory=list)
```

---

### [핵심]

- mutable default에는 `default_factory`를 사용한다.
- list 기본값은 `field(default_factory=list)`를 사용한다.
- dict 기본값은 `field(default_factory=dict)`를 사용한다.
- 직접 `missing_sections: list[str] = []`처럼 쓰면 안 된다.
- 기본값이 있는 필드는 기본값 없는 필드 뒤에 둔다.
- dataclass는 Config, Metadata, Result 객체에 적합하다.
- Agent Tool Result의 list / dict 필드에도 default_factory를 사용한다.

---

### [실무]

list default_factory:

```python
from dataclasses import dataclass, field

@dataclass
class ValidationResult:
    file_name: str
    is_valid: bool
    missing_sections: list[str] = field(default_factory=list)
```

dict default_factory:

```python
from dataclasses import dataclass, field

@dataclass
class AgentToolResult:
    status: str
    result: dict = field(default_factory=dict)
    error: str | None = None
```

Chunk Metadata:

```python
from dataclasses import dataclass, field

@dataclass
class ChunkMeta:
    title: str
    text: str
    keywords: list[str] = field(default_factory=list)
```

---

### [FAQ]

Q. default_factory는 왜 필요해?

A. list, dict 같은 mutable 기본값이 객체 간 공유되는 문제를 막기 위해 필요하다.

Q. dataclass에서 `list = []`를 기본값으로 써도 돼?

A. 안 된다. `field(default_factory=list)`를 사용해야 한다.

Q. dict 기본값은 어떻게 설정해?

A. `field(default_factory=dict)`를 사용한다.

Q. 기본값이 있는 필드는 어디에 둬?

A. 기본값 없는 필드 뒤에 둔다.

---

## 5.3 frozen Dataclass

### [개념]

Frozen Dataclass는 생성 후 필드 값을 변경할 수 없는 불변 데이터 객체이다.

설정값, 고정 메타데이터, 변경되면 안 되는 Config를 표현할 때 유용하다.

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class AppConfig:
    base_url: str
    timeout: int
```

---

### [핵심]

- `frozen=True`는 객체를 불변으로 만든다.
- 생성 후 필드 수정이 불가능하다.
- Config 객체에 적합하다.
- 안정적인 상태 유지에 유리하다.
- 완전한 보안 기능은 아니다.
- 내부 mutable 필드가 있으면 주의가 필요하다.
- Part06의 Config Object를 frozen dataclass로 표현할 수 있다.

---

### [실무]

Config Dataclass:

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class LlmConfig:
    base_url: str
    model: str
    timeout: int
```

사용:

```python
config = LlmConfig(
    base_url="https://api.example.com",
    model="qwen2.5",
    timeout=60,
)
```

수정 시도:

```python
# FrozenInstanceError 발생
# config.timeout = 30
```

권장 사용:

```text
API Config
→ frozen dataclass

Document Metadata
→ normal dataclass

Validation Result
→ normal dataclass or TypedDict
```

---

### [FAQ]

Q. frozen dataclass는 언제 사용해?

A. 생성 후 바뀌면 안 되는 Config, 고정 설정값, 불변 메타데이터에 사용한다.

Q. frozen=True를 쓰면 완전히 안전해?

A. 불필요한 필드 수정을 막지만 보안 기능은 아니다.

Q. Validation Result도 frozen으로 해야 해?

A. 보통은 필요 없다. 결과 객체는 생성 후 수정하지 않는 구조라면 고려할 수 있다.

Q. Config에는 frozen dataclass가 좋아?

A. 좋다. 설정값이 실행 중 변경되는 것을 방지할 수 있다.

---

# 6. Class and OOP Basics

## 6.1 Class Role

### [개념]

Class는 상태와 동작을 하나로 묶는 Python 구조이다.

Python for AI Automation에서는 API Client, Markdown Processor, RAG Document Validator, Report Builder, Agent Tool Executor처럼 상태와 메서드가 함께 필요한 경우 Class를 사용할 수 있다.

```python
class MarkdownProcessor:
    def __init__(self, required_sections: list[str]):
        self.required_sections = required_sections
```

---

### [핵심]

- Class는 상태와 동작을 묶는다.
- `__init__`은 객체 생성 시 초기 상태를 설정한다.
- Method는 Class 내부 Function이다.
- 단순 자동화는 Function만으로 충분할 수 있다.
- 상태가 필요한 구조는 Class가 유용하다.
- 모든 코드를 Class로 만들 필요는 없다.
- 상속보다 조합을 우선 고려한다.
- API Client Class는 Part06과 연결된다.
- RAG Document Validator Class는 Part10과 연결된다.

---

### [실무]

Markdown Validator Class:

```python
class MarkdownValidator:
    def __init__(self, required_sections: list[str]):
        self.required_sections = required_sections

    def find_missing_sections(self, text: str) -> list[str]:
        return [
            section for section in self.required_sections
            if section not in text
        ]

    def validate(self, text: str) -> dict:
        missing_sections = self.find_missing_sections(text)

        return {
            "is_valid": len(missing_sections) == 0,
            "missing_sections": missing_sections,
            "has_retrieval_queries": "# Retrieval Queries" in text,
        }
```

사용:

```python
validator = MarkdownValidator(
    required_sections=["### [개념]", "### [핵심]", "### [실무]", "### [FAQ]"]
)

result = validator.validate(document_text)
```

---

### [FAQ]

Q. Class는 언제 사용해?

A. 상태와 동작을 함께 관리해야 할 때 사용한다.

Q. Python 자동화는 반드시 Class로 만들어야 해?

A. 아니다. 단순 자동화는 Function 중심이 더 명확할 수 있다.

Q. Class가 유용한 자동화 영역은?

A. API Client, Markdown Processor, Validator, Report Builder처럼 설정과 메서드를 함께 쓰는 영역이다.

Q. 모든 Function을 Class 안에 넣어도 돼?

A. 권장하지 않는다. 상태가 필요 없는 로직은 Function으로 두는 것이 단순하다.

---

## 6.2 Instance Method

### [개념]

Instance Method는 Class 객체가 가진 상태를 사용하거나 변경하는 Method이다.

첫 번째 Parameter로 `self`를 받으며, `self`를 통해 Instance 속성에 접근한다.

```python
class Processor:
    def __init__(self, name: str):
        self.name = name

    def run(self) -> str:
        return self.name
```

---

### [핵심]

- Instance Method는 `self`를 첫 번째 Parameter로 가진다.
- `self`는 현재 객체 자신을 의미한다.
- Instance 속성은 `self.attribute`로 접근한다.
- 객체별 상태를 사용할 수 있다.
- 상태가 필요 없는 Method는 일반 Function 또는 staticmethod를 고려한다.
- Method Return Type도 명확히 작성한다.

---

### [실무]

API Client Method:

```python
import requests

class ApiClient:
    def __init__(self, base_url: str, timeout: int):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def get_json(self, path: str) -> dict:
        response = requests.get(
            f"{self.base_url}{path}",
            timeout=self.timeout,
        )
        response.raise_for_status()
        return response.json()
```

Report Builder Method:

```python
class ReportBuilder:
    def __init__(self, title: str):
        self.title = title

    def build_markdown(self, rows: list[dict]) -> str:
        lines = [f"# {self.title}", ""]

        for row in rows:
            lines.append(f"- {row}")

        return "\n".join(lines)
```

---

### [FAQ]

Q. self는 무엇이야?

A. 현재 Instance 객체 자신을 가리키는 Parameter이다.

Q. Instance Method는 언제 사용해?

A. 객체가 가진 설정값이나 상태를 사용해 작업할 때 사용한다.

Q. self를 생략해도 돼?

A. Instance Method에서는 생략할 수 없다.

Q. 상태가 필요 없는 함수도 Method로 만들어야 해?

A. 아니다. 상태가 필요 없으면 일반 Function이 더 단순할 수 있다.

---

## 6.3 Property

### [개념]

Property는 Class 내부 값을 메서드처럼 계산하되 외부에서는 속성처럼 접근하게 하는 기능이다.

계산된 값, 읽기 전용 값, Config 기반 Derived Value를 표현할 때 사용할 수 있다.

```python
class Document:
    def __init__(self, file_name: str):
        self.file_name = file_name

    @property
    def extension(self) -> str:
        return self.file_name.split(".")[-1]
```

---

### [핵심]

- `@property`는 Method를 속성처럼 접근하게 한다.
- 계산된 값을 표현할 수 있다.
- 읽기 전용 속성을 만들 수 있다.
- 복잡한 계산은 Method로 두는 것이 명확할 수 있다.
- Property 내부에서 무거운 I/O 작업은 피한다.
- API URL, file name, extension 같은 가벼운 파생값에 적합하다.

---

### [실무]

Document Property:

```python
from pathlib import Path

class DocumentFile:
    def __init__(self, path: Path):
        self.path = path

    @property
    def file_name(self) -> str:
        return self.path.name

    @property
    def extension(self) -> str:
        return self.path.suffix

    @property
    def is_markdown(self) -> bool:
        return self.path.suffix == ".md"
```

Config Property:

```python
class ApiConfig:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    @property
    def chat_url(self) -> str:
        return f"{self.base_url}/v1/chat"
```

---

### [FAQ]

Q. property는 언제 사용해?

A. 객체 상태에서 계산되는 값을 속성처럼 제공하고 싶을 때 사용한다.

Q. property와 일반 Method 차이는?

A. property는 `obj.value`처럼 접근하고 Method는 `obj.method()`처럼 호출한다.

Q. property 안에서 파일 읽기를 해도 돼?

A. 권장하지 않는다. 무거운 I/O 작업은 명시적인 Method로 두는 것이 좋다.

Q. property는 읽기 전용 값에 적합해?

A. 그렇다. 계산된 읽기 전용 값을 표현하기 좋다.

---

# 7. Composition Protocol Inheritance

## 7.1 Composition

### [개념]

Composition은 하나의 객체가 다른 객체를 포함해 기능을 조합하는 설계 방식이다.

Python 자동화에서는 File Reader, Markdown Validator, Report Builder, API Client를 조합해 Agent Tool을 구성할 수 있다.

```text
AgentTool
→ FileReader
→ MarkdownValidator
→ ReportBuilder
```

---

### [핵심]

- Composition은 객체를 조합해 기능을 만든다.
- 상속보다 유연하다.
- 각 Class의 책임을 분리할 수 있다.
- 테스트하기 쉽다.
- 자동화 파이프라인 구성에 적합하다.
- 복잡한 상속 구조를 피할 수 있다.
- Mock이나 Test Double로 구성 요소를 교체하기 쉽다.

---

### [실무]

구성 요소 Class:

```python
from pathlib import Path

class FileReader:
    def read_text(self, path: Path) -> str:
        return path.read_text(encoding="utf-8")


class MarkdownValidator:
    def validate(self, text: str) -> dict:
        return {
            "has_faq": "### [FAQ]" in text,
            "has_retrieval_queries": "# Retrieval Queries" in text,
        }


class DocumentCheckTool:
    def __init__(self, reader: FileReader, validator: MarkdownValidator):
        self.reader = reader
        self.validator = validator

    def run(self, path: Path) -> dict:
        text = self.reader.read_text(path)
        result = self.validator.validate(text)

        return {
            "file_name": path.name,
            "result": result,
        }
```

사용:

```python
tool = DocumentCheckTool(
    reader=FileReader(),
    validator=MarkdownValidator(),
)
```

---

### [FAQ]

Q. Composition은 무엇이야?

A. 여러 객체를 포함하고 조합해서 기능을 구성하는 방식이다.

Q. Python 자동화에서 Composition은 왜 좋아?

A. File Reader, Validator, Report Builder처럼 역할을 분리해 조합할 수 있기 때문이다.

Q. Composition은 테스트에 유리해?

A. 그렇다. 구성 요소를 Mock이나 Test Double로 교체하기 쉽다.

Q. 상속보다 Composition을 우선하라는 뜻은?

A. 복잡한 부모-자식 구조보다 필요한 객체를 조합하는 방식이 더 단순하고 유연한 경우가 많다는 뜻이다.

---

## 7.2 Protocol

### [개념]

`Protocol`은 특정 객체가 어떤 Method나 속성을 가져야 하는지 구조적으로 표현하는 Type Hint 방식이다.

Python 자동화에서는 Validator, Reader, Writer처럼 구현체를 교체할 수 있는 구조를 표현할 때 유용하다.

```python
from typing import Protocol

class Validator(Protocol):
    def validate(self, text: str) -> dict:
        ...
```

---

### [핵심]

- Protocol은 구조적 타입을 표현한다.
- 상속 없이도 같은 Method를 가진 객체를 같은 타입처럼 다룰 수 있다.
- Composition 구조와 잘 어울린다.
- 테스트에서 Mock 객체를 주입하기 쉽다.
- Validator, Reader, Writer, Client Interface에 사용할 수 있다.
- 초급 자동화에서는 필수는 아니다.
- 구조가 커진 Agent Tool 시스템에서는 선택적으로 유용하다.

---

### [실무]

Validator Protocol:

```python
from typing import Protocol

class Validator(Protocol):
    def validate(self, text: str) -> dict:
        ...


class MarkdownValidator:
    def validate(self, text: str) -> dict:
        return {
            "has_faq": "### [FAQ]" in text,
            "has_retrieval_queries": "# Retrieval Queries" in text,
        }


def run_validation(text: str, validator: Validator) -> dict:
    return validator.validate(text)
```

Reader Protocol:

```python
from pathlib import Path
from typing import Protocol

class TextReader(Protocol):
    def read_text(self, path: Path) -> str:
        ...


class FileReader:
    def read_text(self, path: Path) -> str:
        return path.read_text(encoding="utf-8")
```

Agent Tool 구성:

```python
class DocumentTool:
    def __init__(self, reader: TextReader, validator: Validator):
        self.reader = reader
        self.validator = validator
```

---

### [FAQ]

Q. Protocol은 언제 사용해?

A. 여러 구현체가 같은 Method 구조를 가져야 하고, 상속 없이 타입만 맞추고 싶을 때 사용한다.

Q. Protocol은 자동화 코드에 필수야?

A. 아니다. 작은 자동화 스크립트에는 필요 없지만 Agent Tool 구조가 커지면 유용하다.

Q. Protocol과 상속의 차이는?

A. Protocol은 구조가 맞으면 타입이 호환되고, 상속은 명시적인 부모-자식 관계를 만든다.

Q. Protocol은 테스트에 도움이 돼?

A. 그렇다. 같은 Method를 가진 Mock 객체나 Fake 객체를 쉽게 주입할 수 있다.

---

## 7.3 Inheritance Basics

### [개념]

Inheritance는 기존 Class를 기반으로 새로운 Class를 만드는 OOP 방식이다.

공통 동작을 부모 Class에 두고, 세부 동작을 자식 Class에서 재사용하거나 확장할 수 있다.

```python
class BaseValidator:
    def validate(self, text: str) -> dict:
        raise NotImplementedError
```

---

### [핵심]

- Inheritance는 부모 Class 기능을 자식 Class가 물려받는다.
- 공통 Interface를 만들 때 사용할 수 있다.
- 과도한 상속은 구조를 복잡하게 만든다.
- 자동화 코드에서는 Composition을 우선 고려한다.
- 명확한 공통 규약이 있을 때만 상속을 사용한다.
- 추상 구조가 필요하면 Protocol 또는 ABC도 고려할 수 있다.
- 단순 Validator 구조에서는 Protocol이 더 가벼울 수 있다.

---

### [실무]

Base Validator:

```python
class BaseValidator:
    def validate(self, text: str) -> dict:
        raise NotImplementedError("Subclasses must implement validate")
```

Markdown Validator:

```python
class MarkdownValidator(BaseValidator):
    def validate(self, text: str) -> dict:
        return {
            "has_faq": "### [FAQ]" in text,
            "has_retrieval_queries": "# Retrieval Queries" in text,
        }
```

JSON Validator:

```python
class JsonValidator(BaseValidator):
    def validate(self, text: str) -> dict:
        import json

        try:
            json.loads(text)
            return {"is_valid": True}
        except json.JSONDecodeError as error:
            return {
                "is_valid": False,
                "error": str(error),
            }
```

---

### [FAQ]

Q. Inheritance는 언제 사용해?

A. 여러 Class가 같은 Interface나 공통 동작을 공유해야 할 때 사용한다.

Q. 자동화 코드에서 상속을 많이 쓰는 게 좋아?

A. 아니다. 과도한 상속은 구조를 복잡하게 하므로 Composition을 우선 고려한다.

Q. Base Class는 무엇이야?

A. 공통 Method나 규약을 제공하는 부모 Class이다.

Q. NotImplementedError는 왜 사용해?

A. 자식 Class가 반드시 구현해야 하는 Method임을 표시하기 위해 사용한다.

---

# 8. Function vs Class vs Dataclass vs TypedDict

## 8.1 Selection Criteria

### [개념]

Function, Class, Dataclass, TypedDict는 목적에 따라 선택해야 한다.

Python for AI Automation에서는 단순 로직은 Function, 상태가 필요한 처리기는 Class, 데이터 객체는 Dataclass, JSON 호환 dict 타입은 TypedDict를 우선 고려한다.

---

### [핵심]

| 구조      | 목적                 | 사용 예                           |
| --------- | -------------------- | --------------------------------- |
| Function  | 단일 작업 실행       | 파일 읽기, 문자열 정리, 섹션 검사 |
| Class     | 상태 + 동작 묶기     | API Client, Validator, Processor  |
| Dataclass | 구조화된 데이터 객체 | Config, Metadata, Result          |
| TypedDict | dict 구조 타입 명시  | Agent Tool Output, JSON Result    |
| Protocol  | 구조적 Interface     | Validator, Reader, Writer         |

---

### [실무]

선택 기준:

```text
단순 변환
→ Function

반복 사용되는 설정과 Method
→ Class

문서 메타데이터 객체
→ Dataclass

JSON으로 바로 반환할 dict 구조
→ TypedDict

Agent Tool Output
→ TypedDict

고정 Config
→ frozen dataclass

구현체 교체 가능 구조
→ Protocol
```

예시:

```python
from dataclasses import dataclass
from typing import Literal, TypedDict

Status = Literal["success", "error", "partial_success"]

@dataclass(frozen=True)
class Config:
    input_dir: str
    output_dir: str


class ToolOutput(TypedDict):
    status: Status
    result: dict | None
    error: str | None


def normalize_title(title: str) -> str:
    return title.strip()


class MarkdownValidator:
    def validate(self, text: str) -> dict:
        return {
            "has_faq": "### [FAQ]" in text,
        }
```

---

### [FAQ]

Q. Function과 Class 중 무엇을 먼저 써야 해?

A. 상태가 필요 없다면 Function을 먼저 사용한다.

Q. Class는 언제 필요해?

A. 설정값이나 상태를 유지하면서 여러 Method를 함께 사용할 때 필요하다.

Q. Dataclass는 언제 써?

A. 구조가 정해진 데이터 객체를 명확히 표현할 때 사용한다.

Q. TypedDict는 언제 써?

A. JSON 호환 dict 구조의 key와 value 타입을 명시하고 싶을 때 사용한다.

Q. Protocol은 언제 고려해?

A. Validator, Reader, Writer처럼 구현체를 바꿔 끼울 수 있는 구조가 필요할 때 고려한다.

---

# 9. Type Hint Dataclass OOP Best Practice

## 9.1 Best Practice

### [개념]

Type Hint Dataclass OOP Best Practice는 Python 자동화 코드의 구조 명확성, Agent 이해도, 코드 리뷰 품질, 테스트 가능성을 높이는 기준이다.

목표:

```text
Clear Type
→ Structured Data
→ Small Function
→ Simple Class
→ Agent-Friendly Output
```

---

### [핵심]

- Function Parameter와 Return Type에 Type Hint를 적용한다.
- `list[str]`, `dict[str, object]`처럼 Collection 내부 타입을 명시한다.
- None 가능성은 `str | None`처럼 표현한다.
- 제한된 문자열 값은 `Literal`을 고려한다.
- ToolOutput의 `status`는 `Literal["success", "error", "partial_success"]`로 통일한다.
- 복잡한 dict 구조는 `TypedDict`를 사용한다.
- 구조화된 데이터 객체는 `dataclass`를 사용한다.
- mutable default에는 `field(default_factory=...)`를 사용한다.
- 변경되면 안 되는 Config는 `frozen=True`를 고려한다.
- 상태가 없으면 Class보다 Function을 우선한다.
- 상태와 동작이 함께 필요하면 Class를 사용한다.
- 상속보다 Composition을 우선 고려한다.
- 구현체 교체가 필요하면 Protocol을 고려한다.
- Agent Tool Output은 `status`, `result`, `error` 구조로 통일한다.

---

### [실무]

통합 예시:

```python
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Literal, TypedDict

Status = Literal["success", "error", "partial_success"]


@dataclass(frozen=True)
class DocumentCheckConfig:
    required_sections: list[str]
    require_retrieval_queries: bool = True


@dataclass
class ValidationResult:
    file_name: str
    is_valid: bool
    missing_sections: list[str] = field(default_factory=list)
    has_retrieval_queries: bool = False


class ToolOutput(TypedDict):
    status: Status
    result: dict | None
    error: str | None


class MarkdownValidator:
    def __init__(self, config: DocumentCheckConfig):
        self.config = config

    def validate(self, path: Path) -> ValidationResult:
        text = path.read_text(encoding="utf-8")

        missing_sections = [
            section for section in self.config.required_sections
            if section not in text
        ]

        has_retrieval_queries = "# Retrieval Queries" in text

        is_valid = len(missing_sections) == 0

        if self.config.require_retrieval_queries:
            is_valid = is_valid and has_retrieval_queries

        return ValidationResult(
            file_name=path.name,
            is_valid=is_valid,
            missing_sections=missing_sections,
            has_retrieval_queries=has_retrieval_queries,
        )


def run_document_check(path: Path, validator: MarkdownValidator) -> ToolOutput:
    try:
        result = validator.validate(path)

        return {
            "status": "success",
            "result": asdict(result),
            "error": None,
        }

    except Exception as error:
        return {
            "status": "error",
            "result": None,
            "error": str(error),
        }
```

검수 Checklist:

```text
- Function Parameter Type Hint 적용
- Return Type Hint 적용
- None 가능성 명시
- Collection 내부 타입 명시
- ToolOutput status Literal 통일
- TypedDict 또는 dataclass 사용 검토
- mutable default 방지
- Config 변경 방지 필요 시 frozen 사용
- Class 남용 없음
- Composition 우선
- Protocol 선택 고려
- Agent Tool Output 구조 통일
```

---

### [FAQ]

Q. Type Hint Dataclass OOP Best Practice는 무엇이야?

A. Type Hint로 입력과 출력을 명확히 하고, dataclass와 TypedDict로 데이터 구조를 표현하며, Class는 필요한 경우에만 사용하는 기준이다.

Q. Agent가 이해하기 좋은 Python 구조는?

A. Type Hint가 명확하고, Function 책임이 작고, Output이 dict 또는 JSON 구조로 통일된 코드이다.

Q. dataclass와 TypedDict 중 무엇을 써야 해?

A. 객체로 다루고 싶으면 dataclass, JSON 호환 dict 구조를 명시하고 싶으면 TypedDict를 사용한다.

Q. Class를 많이 만들수록 좋은 구조야?

A. 아니다. 상태가 필요 없으면 Function을 우선하고, 상태와 동작이 함께 필요할 때 Class를 사용한다.

Q. Agent Tool Output status는 어떻게 통일해?

A. `Literal["success", "error", "partial_success"]` 기반 `Status` 타입으로 통일하는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. Python Type Hint는 무엇이야?
A. 변수, 함수 Parameter, Return Value의 예상 타입을 명시하는 문법이다.

Q. Python Type Hint는 왜 필요해?
A. Agent가 코드 구조를 이해하고 자동화 코드 리뷰와 유지보수를 쉽게 하기 위해 필요하다.

Q. Type Hint는 런타임 타입을 강제해?
A. 아니다. 기본 Type Hint는 런타임 타입 강제가 아니라 코드 이해와 정적 분석을 돕는다.

Q. Type Hint는 어디에 먼저 적용해야 해?
A. Function Parameter와 Return Type에 먼저 적용하는 것이 좋다.

Q. Agent Tool Script에 Type Hint가 중요한 이유는?
A. Agent가 Tool Input과 Output 구조를 더 명확히 이해하고 검증할 수 있기 때문이다.

Q. Part07의 Structured Error Result와 Part08은 어떻게 연결돼?
A. Part07의 `status`, `result`, `error` 구조를 Part08에서 `TypedDict`, `Literal`, `dataclass`로 명확히 타입화할 수 있다.

Q. Python 반환값이 없는 함수는 Type Hint를 어떻게 써?
A. `-> None`을 사용한다.

Q. Python bool Type Hint는 언제 사용해?
A. 검증 성공 여부, 파일 존재 여부, 필수 섹션 포함 여부처럼 참/거짓 결과를 반환할 때 사용한다.

Q. Python int와 float는 어떻게 구분해?
A. 개수, 순서, 크기는 int를 쓰고 점수, 비율, 소수 계산은 float를 사용한다.

Q. Python list Type Hint는 어떻게 써?
A. 문자열 목록이면 `list[str]`, 정수 목록이면 `list[int]`처럼 작성한다.

Q. Python dict Type Hint는 어떻게 써?
A. key와 value 타입을 명시해 `dict[str, str]`, `dict[str, object]`처럼 작성한다.

Q. dict[str, object]는 언제 사용해?
A. value에 str, bool, list처럼 여러 타입이 섞인 dict를 반환할 때 사용할 수 있다.

Q. 복잡한 dict도 Type Hint만으로 충분해?
A. 복잡한 구조라면 `TypedDict` 또는 `dataclass`를 사용하는 것이 더 명확하다.

Q. Python `str | None`은 무슨 뜻이야?
A. 값이 문자열이거나 None일 수 있다는 의미이다.

Q. Optional 값은 바로 사용해도 돼?
A. 아니다. None 가능성이 있으므로 사용 전 None 체크를 하는 것이 좋다.

Q. error 필드는 어떤 Type Hint가 좋아?
A. 성공 시 None, 실패 시 문자열이므로 `str | None` 구조가 적합하다.

Q. Python Union은 언제 사용해?
A. 입력값이 여러 타입 중 하나일 수 있을 때 사용한다.

Q. `str | Path`는 무슨 뜻이야?
A. 문자열 경로나 Path 객체 둘 다 받을 수 있다는 의미이다.

Q. Union 타입을 많이 쓰면 좋아?
A. 아니다. 너무 많은 타입을 허용하면 코드 검증과 이해가 어려워진다.

Q. JSON 값 처리에 Union이 필요한 이유는?
A. JSON value는 문자열, 숫자, bool, null 등 여러 타입이 될 수 있기 때문이다.

Q. Python Literal은 언제 사용해?
A. 허용 가능한 문자열이나 값이 정해져 있을 때 사용한다.

Q. Agent Tool Output status에 Literal을 써도 돼?
A. 좋다. `success`, `error`, `partial_success` 같은 값으로 제한할 수 있다.

Q. 실행 모드에 Literal을 써도 돼?
A. 좋다. `dry_run`, `execute`처럼 위험 작업 모드를 제한할 수 있다.

Q. Literal과 Enum 중 무엇을 써?
A. 단순한 값 제한은 Literal, 더 구조적인 상수 관리가 필요하면 Enum을 고려한다.

Q. Python Callable은 언제 사용해?
A. 함수 자체를 인자로 전달하거나 Validator, Transformer를 교체 가능하게 만들 때 사용한다.

Q. Callable[[str], str]은 무슨 뜻이야?
A. 문자열 하나를 입력받고 문자열을 반환하는 함수라는 뜻이다.

Q. Callable은 자동화에서 필수야?
A. 필수는 아니지만 변환 로직이나 검증 로직을 주입할 때 유용하다.

Q. Python TypedDict는 언제 사용해?
A. dict 구조가 고정되어 있고 key와 value 타입을 명확히 하고 싶을 때 사용한다.

Q. TypedDict는 런타임 검증을 해?
A. 아니다. Type Hint 용도이며 런타임 검증은 별도 코드가 필요하다.

Q. Agent Tool Output에 TypedDict를 써도 돼?
A. 좋다. `status`, `result`, `error` 구조를 명확히 표현할 수 있다.

Q. TypedDict와 dataclass 차이는?
A. TypedDict는 dict 구조 타입 힌트이고, dataclass는 실제 데이터 객체를 생성한다.

Q. ToolOutput의 status 타입은 어떻게 통일하는 게 좋아?
A. `Literal["success", "error", "partial_success"]` 기반 `Status` 타입으로 통일하는 것이 좋다.

Q. ToolOutput Standard Type은 왜 필요해?
A. Agent가 Tool 실행 결과를 일관되게 해석하고 후속 작업을 안정적으로 수행하기 위해 필요하다.

Q. ToolOutput의 status는 어떤 값이 좋아?
A. `success`, `error`, `partial_success`로 통일하는 것이 좋다.

Q. 실패 시 result는 무엇이 좋아?
A. 보통 `None`을 사용하고, 부분 결과가 있으면 `partial_success`에서 별도 구조로 표현한다.

Q. Python dataclass는 언제 사용해?
A. 문서 메타데이터, 설정값, 검증 결과처럼 구조가 정해진 데이터를 표현할 때 사용한다.

Q. dataclass는 dict보다 좋은가?
A. 구조가 명확하고 필드 타입을 표현할 수 있어 복잡한 데이터에는 dict보다 유리할 수 있다.

Q. dataclass를 JSON으로 바로 저장할 수 있어?
A. 보통 `asdict()`로 dict 변환 후 JSON 저장한다.

Q. dataclass에 복잡한 로직을 넣어도 돼?
A. 권장하지 않는다. dataclass는 단순 데이터 표현 중심으로 사용하는 것이 좋다.

Q. dataclass default_factory는 왜 필요해?
A. list, dict 같은 mutable 기본값이 객체 간 공유되는 문제를 막기 위해 필요하다.

Q. dataclass에서 `list = []`를 기본값으로 써도 돼?
A. 안 된다. `field(default_factory=list)`를 사용해야 한다.

Q. dataclass dict 기본값은 어떻게 설정해?
A. `field(default_factory=dict)`를 사용한다.

Q. frozen dataclass는 언제 사용해?
A. 생성 후 바뀌면 안 되는 Config, 고정 설정값, 불변 메타데이터에 사용한다.

Q. Config에는 frozen dataclass가 좋아?
A. 좋다. 설정값이 실행 중 변경되는 것을 방지할 수 있다.

Q. Python Class는 언제 사용해?
A. 상태와 동작을 함께 관리해야 할 때 사용한다.

Q. Python 자동화는 반드시 Class로 만들어야 해?
A. 아니다. 단순 자동화는 Function 중심이 더 명확할 수 있다.

Q. Class가 유용한 자동화 영역은?
A. API Client, Markdown Processor, Validator, Report Builder처럼 설정과 메서드를 함께 쓰는 영역이다.

Q. Python self는 무엇이야?
A. 현재 Instance 객체 자신을 가리키는 Parameter이다.

Q. Instance Method는 언제 사용해?
A. 객체가 가진 설정값이나 상태를 사용해 작업할 때 사용한다.

Q. Python property는 언제 사용해?
A. 객체 상태에서 계산되는 값을 속성처럼 제공하고 싶을 때 사용한다.

Q. property 안에서 파일 읽기를 해도 돼?
A. 권장하지 않는다. 무거운 I/O 작업은 명시적인 Method로 두는 것이 좋다.

Q. Python Composition은 무엇이야?
A. 여러 객체를 포함하고 조합해서 기능을 구성하는 방식이다.

Q. Python 자동화에서 Composition은 왜 좋아?
A. File Reader, Validator, Report Builder처럼 역할을 분리해 조합할 수 있기 때문이다.

Q. Python Protocol은 언제 사용해?
A. 여러 구현체가 같은 Method 구조를 가져야 하고, 상속 없이 타입만 맞추고 싶을 때 사용한다.

Q. Protocol은 자동화 코드에 필수야?
A. 아니다. 작은 자동화 스크립트에는 필요 없지만 Agent Tool 구조가 커지면 유용하다.

Q. Protocol과 상속의 차이는?
A. Protocol은 구조가 맞으면 타입이 호환되고, 상속은 명시적인 부모-자식 관계를 만든다.

Q. Python Inheritance는 언제 사용해?
A. 여러 Class가 같은 Interface나 공통 동작을 공유해야 할 때 사용한다.

Q. 자동화 코드에서 상속을 많이 쓰는 게 좋아?
A. 아니다. 과도한 상속은 구조를 복잡하게 하므로 Composition을 우선 고려한다.

Q. Function과 Class 중 무엇을 먼저 써야 해?
A. 상태가 필요 없다면 Function을 먼저 사용한다.

Q. Class는 언제 필요해?
A. 설정값이나 상태를 유지하면서 여러 Method를 함께 사용할 때 필요하다.

Q. Dataclass와 TypedDict 중 무엇을 써야 해?
A. 객체로 다루고 싶으면 dataclass, JSON 호환 dict 구조를 명시하고 싶으면 TypedDict를 사용한다.

Q. Agent가 이해하기 좋은 Python 구조는?
A. Type Hint가 명확하고, Function 책임이 작고, Output이 dict 또는 JSON 구조로 통일된 코드이다.

Q. Type Hint Dataclass OOP Best Practice는 무엇이야?
A. Type Hint로 입력과 출력을 명확히 하고, dataclass와 TypedDict로 데이터 구조를 표현하며, Class는 필요한 경우에만 사용하는 기준이다.

Q. Agent Tool Output status는 어떻게 통일해?
A. `Literal["success", "error", "partial_success"]` 기반 `Status` 타입으로 통일하는 것이 좋다.
