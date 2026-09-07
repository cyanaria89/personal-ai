# Python for AI Automation Part03 - Function Module Package

---

# 1. Function Design

## 1.1 Function Role

### [개념]

Function은 Python 자동화 코드에서 반복 가능한 작업을 하나의 이름으로 묶는 실행 단위이다.

Python for AI Automation에서 Function은 File Processing, API Request, Markdown Validation, JSON Transformation, Agent Tool Execution을 재사용 가능한 로직으로 분리하기 위해 사용한다.

기본 Flow:

```text
Input
→ Function
→ Processing
→ Return
```

---

### [핵심]

- Function은 하나의 책임만 가지는 것이 좋다.
- Function 이름은 동작을 명확히 표현해야 한다.
- Function 입력값과 반환값은 예측 가능해야 한다.
- Type Hint를 사용하면 Agent가 코드 구조를 이해하기 쉽다.
- Function은 자동화 스크립트의 테스트 단위가 된다.
- Function이 너무 길어지면 여러 Function으로 분리한다.
- Agent Tool Script는 Function 기반으로 작성하면 재사용성과 검증성이 좋아진다.

---

### [실무]

2026 실무 기준 Python 자동화 코드는 단일 긴 Script보다 Function 중심 구조가 안전하다.

좋은 Function 예시:

```python
from pathlib import Path

def read_markdown_file(path: Path) -> str:
    """Read a Markdown file as UTF-8 text."""
    return path.read_text(encoding="utf-8")
```

나쁜 Function 예시:

```python
def process():
    text = open("a.md").read()
    print(text)
    # validate
    # save
    # call api
    # log
```

문제점:

- Function 이름이 모호함
- 입력값이 없음
- 반환값이 없음
- 파일 경로 하드코딩
- 여러 책임이 섞임
- 테스트 어려움

---

### [FAQ]

Q. Python 자동화에서 Function은 왜 중요해?

A. 반복 작업을 재사용하고 테스트 가능한 단위로 분리할 수 있기 때문이다.

Q. Function은 하나의 일만 해야 해?

A. 그렇다. 하나의 Function은 하나의 책임을 가지는 것이 좋다.

Q. Function 이름은 어떻게 작성하는 게 좋아?

A. `read_file`, `validate_document`, `extract_sections`, `build_result`처럼 동작이 드러나게 작성한다.

Q. Function이 너무 길어지면 어떻게 해야 해?

A. 입력 처리, 변환, 검증, 출력 생성을 별도 Function으로 분리한다.

---

## 1.2 Parameter and Return

### [개념]

Parameter는 Function에 전달되는 입력값이고, Return은 Function이 처리 후 돌려주는 출력값이다.

자동화 Function은 입력과 출력이 명확해야 Agent가 재사용하고 검증하기 쉽다.

```python
def add_prefix(text: str, prefix: str) -> str:
    return f"{prefix}{text}"
```

---

### [핵심]

- Parameter는 Function이 처리할 입력값이다.
- Return은 Function 처리 결과이다.
- 입력값과 반환값이 명확해야 테스트하기 쉽다.
- 반환값이 없는 Function은 자동화 흐름에서 추적이 어렵다.
- Agent Tool Function은 구조화된 반환값을 사용하는 것이 좋다.
- 반환값은 `dict`, `list`, `str`, `bool` 등 명확한 형태가 좋다.

---

### [실무]

문서 검증 Function:

```python
def has_retrieval_queries(text: str) -> bool:
    return "# Retrieval Queries" in text
```

구조화된 결과 반환:

```python
def build_validation_result(
    file_name: str,
    is_valid: bool,
    missing_sections: list[str],
) -> dict:
    return {
        "file_name": file_name,
        "is_valid": is_valid,
        "missing_sections": missing_sections,
    }
```

권장 반환 구조:

```text
Function Input
→ Validate
→ Process
→ Return Structured Result
```

---

### [FAQ]

Q. Function에는 Parameter가 꼭 필요해?

A. 항상 필요한 것은 아니지만, 외부 값을 하드코딩하지 않고 Parameter로 받는 것이 재사용에 유리하다.

Q. Function은 항상 Return이 있어야 해?

A. 출력이 필요한 자동화 Function은 Return을 명확히 두는 것이 좋다.

Q. 자동화 Function의 반환값은 어떤 형태가 좋아?

A. Agent가 처리하기 쉬운 dict, list, bool, str 같은 명확한 형태가 좋다.

Q. print만 하고 Return이 없는 Function은 좋은 구조야?

A. 검증과 재사용이 어려우므로 핵심 로직에서는 Return을 사용하는 것이 좋다.

---

## 1.3 Default Parameter and Keyword Argument

### [개념]

Default Parameter는 Function Parameter에 기본값을 지정하는 방식이다.

Keyword Argument는 Parameter 이름을 명시해서 값을 전달하는 방식이다.

```python
def read_text(path: str, encoding: str = "utf-8") -> str:
    with open(path, "r", encoding=encoding) as file:
        return file.read()
```

---

### [핵심]

- Default Parameter는 자주 쓰는 기본값을 지정할 때 사용한다.
- Keyword Argument는 호출 의도를 명확히 한다.
- 파일 encoding, timeout, retry count 같은 값에 기본값을 둘 수 있다.
- mutable default는 피해야 한다.
- `list`, `dict`, `set`을 Default Parameter로 직접 쓰지 않는다.

---

### [실무]

encoding 기본값:

```python
from pathlib import Path

def read_text_file(path: Path, encoding: str = "utf-8") -> str:
    return path.read_text(encoding=encoding)
```

Keyword Argument 사용:

```python
text = read_text_file(
    path=Path("docs/example.md"),
    encoding="utf-8",
)
```

잘못된 mutable default:

```python
def add_result(result: dict, results: list = []) -> list:
    results.append(result)
    return results
```

권장 방식:

```python
def add_result(result: dict, results: list | None = None) -> list:
    if results is None:
        results = []

    results.append(result)
    return results
```

---

### [FAQ]

Q. Default Parameter는 언제 사용해?

A. encoding, timeout, retry count처럼 기본값이 명확한 옵션에 사용한다.

Q. Keyword Argument는 왜 좋아?

A. 어떤 Parameter에 어떤 값이 들어가는지 명확해져 가독성과 안정성이 좋아진다.

Q. list를 Default Parameter로 쓰면 안 되는 이유는?

A. Function 호출 간에 같은 list 객체가 공유되어 예기치 않은 결과가 발생할 수 있기 때문이다.

Q. mutable default 대신 무엇을 써야 해?

A. 기본값을 `None`으로 두고 Function 내부에서 새 list나 dict를 생성한다.

---

# 2. Function Quality Rules

## 2.1 Single Responsibility Function

### [개념]

Single Responsibility Function은 하나의 Function이 하나의 역할만 수행하도록 작성하는 원칙이다.

Python 자동화에서는 입력, 읽기, 변환, 검증, 저장, 출력 생성을 분리하는 것이 좋다.

---

### [핵심]

- 하나의 Function은 하나의 작업만 수행한다.
- 파일 읽기와 검증을 하나의 Function에 과도하게 섞지 않는다.
- API 호출과 결과 저장을 무분별하게 섞지 않는다.
- Function 이름만 보고 역할을 알 수 있어야 한다.
- 테스트 가능한 작은 단위로 나눈다.

---

### [실무]

나쁜 구조:

```python
def process_document(path: str) -> dict:
    text = open(path, "r", encoding="utf-8").read()
    missing = []
    for section in ["[개념]", "[핵심]", "[실무]", "[FAQ]"]:
        if section not in text:
            missing.append(section)
    print(missing)
    return {"missing": missing}
```

좋은 구조:

```python
from pathlib import Path

REQUIRED_SECTIONS = ["[개념]", "[핵심]", "[실무]", "[FAQ]"]

def read_document(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def find_missing_sections(text: str, sections: list[str]) -> list[str]:
    return [
        section for section in sections
        if section not in text
    ]


def build_validation_result(
    file_name: str,
    missing_sections: list[str],
) -> dict:
    return {
        "file_name": file_name,
        "is_valid": len(missing_sections) == 0,
        "missing_sections": missing_sections,
    }
```

---

### [FAQ]

Q. Single Responsibility Function은 왜 중요해?

A. Function을 재사용하고 테스트하고 수정하기 쉬워지기 때문이다.

Q. 파일 읽기와 검증을 같은 Function에 넣어도 돼?

A. 간단한 스크립트에서는 가능하지만, RAG 문서 자동화에서는 분리하는 것이 좋다.

Q. Function을 많이 나누면 복잡하지 않아?

A. 역할이 명확하면 오히려 Agent와 개발자가 흐름을 이해하기 쉬워진다.

Q. 좋은 Function 분리 기준은?

A. 읽기, 변환, 검증, 저장, 결과 생성 단위로 분리하는 것이다.

---

## 2.2 Pure Function

### [개념]

Pure Function은 같은 입력에 대해 항상 같은 출력을 반환하고 외부 상태를 변경하지 않는 Function이다.

자동화 코드에서는 검증, 변환, 추출 로직을 Pure Function으로 만들면 테스트와 디버깅이 쉬워진다.

```text
Same Input
→ Same Output
→ No External Side Effect
```

---

### [핵심]

- 같은 입력이면 항상 같은 결과를 반환한다.
- 외부 파일, 전역 변수, 네트워크 상태에 의존하지 않는다.
- 원본 데이터를 직접 변경하지 않는다.
- 테스트 작성이 쉽다.
- Agent Tool 내부의 핵심 변환 로직은 Pure Function이 좋다.

---

### [실무]

Pure Function 예시:

```python
def normalize_title(title: str) -> str:
    return title.strip().replace("#", "").strip()
```

Pure Function 검증 예시:

```python
def find_missing_sections(text: str, required_sections: list[str]) -> list[str]:
    return [
        section for section in required_sections
        if section not in text
    ]
```

Side Effect가 있는 Function 예시:

```python
from pathlib import Path

def save_report(path: Path, report: str) -> None:
    path.write_text(report, encoding="utf-8")
```

권장:

- 텍스트 변환은 Pure Function
- 파일 저장은 별도 Function
- API 호출은 별도 Function
- 검증 결과 생성은 Pure Function

---

### [FAQ]

Q. Pure Function은 무엇이 좋아?

A. 같은 입력에 같은 결과를 반환하므로 테스트와 디버깅이 쉽다.

Q. 파일 읽기 Function은 Pure Function이야?

A. 아니다. 파일 시스템 상태에 의존하므로 Side Effect 또는 외부 의존성이 있다.

Q. 자동화 코드에서 Pure Function은 어디에 쓰면 좋아?

A. 문자열 정리, Section 검사, Metadata 변환, 결과 생성 로직에 사용하면 좋다.

Q. 모든 Function을 Pure Function으로 만들어야 해?

A. 아니다. 파일 저장, API 호출, 로그 기록처럼 Side Effect가 필요한 Function도 있다.

---

## 2.3 Function Error Handling

### [개념]

Function Error Handling은 Function 내부에서 발생할 수 있는 오류를 명확히 처리하거나 호출자에게 전달하는 기준이다.

자동화 스크립트는 실패 지점을 추적할 수 있어야 한다.

---

### [핵심]

- 예상 가능한 오류는 구체적인 예외로 처리한다.
- 모든 예외를 무조건 숨기지 않는다.
- 실패 원인이 드러나는 메시지를 사용한다.
- Function 내부에서 처리할 오류와 호출자에게 전달할 오류를 구분한다.
- Agent Tool Function은 실패 결과를 구조화해서 반환할 수 있다.

---

### [실무]

파일 읽기 오류 처리:

```python
from pathlib import Path

def read_document(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    return path.read_text(encoding="utf-8")
```

구조화된 실패 결과:

```python
def build_error_result(file_name: str, message: str) -> dict:
    return {
        "status": "error",
        "file_name": file_name,
        "error": message,
    }
```

검증 Function에서는 오류를 숨기지 않는다:

```python
def require_text(text: str) -> None:
    if not text.strip():
        raise ValueError("Document text is empty")
```

---

### [FAQ]

Q. Function 내부에서 예외를 모두 잡아야 해?

A. 아니다. 처리할 수 있는 예외만 잡고, 나머지는 호출자가 알 수 있게 전달하는 것이 좋다.

Q. except 후 pass를 써도 돼?

A. 권장하지 않는다. 오류 원인을 숨겨 자동화 실패를 추적하기 어렵다.

Q. Agent Tool Function은 오류를 어떻게 반환하면 좋아?

A. `status`, `result`, `error`를 포함한 dict 형태로 구조화하는 것이 좋다.

Q. FileNotFoundError는 언제 발생해?

A. 지정한 파일 경로가 존재하지 않을 때 발생한다.

---

# 3. Module

## 3.1 Module Basics

### [개념]

Module은 Python 파일 단위의 코드 묶음이다.

하나의 `.py` 파일은 하나의 Module로 사용될 수 있다.

자동화 프로젝트에서는 기능별로 Module을 분리해 코드 재사용성과 유지보수성을 높인다.

```text
file_utils.py
markdown_validator.py
api_client.py
config.py
```

---

### [핵심]

- Module은 Python 파일 단위이다.
- 관련 Function을 하나의 Module에 모은다.
- 파일 처리 Function은 `file_utils.py`에 둘 수 있다.
- Markdown 검증 Function은 `markdown_validator.py`에 둘 수 있다.
- API 호출 Function은 `api_client.py`에 둘 수 있다.
- Module 이름은 역할을 표현해야 한다.

---

### [실무]

권장 Module 분리:

```text
python_ai_automation
├ main.py
├ config.py
├ file_utils.py
├ markdown_validator.py
├ json_utils.py
├ api_client.py
└ report_builder.py
```

`file_utils.py`:

```python
from pathlib import Path

def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")
```

`markdown_validator.py`:

```python
REQUIRED_SECTIONS = ["[개념]", "[핵심]", "[실무]", "[FAQ]"]

def find_missing_sections(text: str) -> list[str]:
    return [
        section for section in REQUIRED_SECTIONS
        if section not in text
    ]
```

---

### [FAQ]

Q. Python Module은 무엇이야?

A. 하나의 `.py` 파일이 Module이며, Function과 Class를 재사용 가능한 단위로 묶는다.

Q. Module을 왜 나눠야 해?

A. 기능별로 코드를 분리하면 유지보수, 테스트, 재사용이 쉬워진다.

Q. Module 이름은 어떻게 정해?

A. `file_utils`, `api_client`, `markdown_validator`처럼 역할이 드러나게 작성한다.

Q. 모든 Function을 하나의 파일에 넣어도 돼?

A. 작은 실습은 가능하지만 자동화 프로젝트에서는 기능별 Module 분리를 권장한다.

---

## 3.2 Import Module

### [개념]

Import는 다른 Module의 Function, Class, Constant를 현재 Module에서 사용하기 위한 문법이다.

```python
from pathlib import Path
from file_utils import read_text
```

---

### [핵심]

- `import module`은 Module 전체를 가져온다.
- `from module import name`은 특정 이름만 가져온다.
- 표준 라이브러리 Import와 프로젝트 내부 Import를 구분한다.
- 순환 Import를 피한다.
- 사용하지 않는 Import는 제거한다.

---

### [실무]

Module 전체 Import:

```python
import json
import logging
```

특정 Function Import:

```python
from pathlib import Path
from file_utils import read_text
from markdown_validator import find_missing_sections
```

사용 예시:

```python
from pathlib import Path
from file_utils import read_text
from markdown_validator import find_missing_sections

path = Path("docs/example.md")
text = read_text(path)
missing_sections = find_missing_sections(text)

print(missing_sections)
```

Import 정렬 기준:

```text
Standard Library
→ Third Party Library
→ Local Application Module
```

예시:

```python
from pathlib import Path
import json
import logging

import requests

from file_utils import read_text
from markdown_validator import find_missing_sections
```

---

### [FAQ]

Q. import module과 from module import name 차이는?

A. import module은 Module 전체를 가져오고, from import는 특정 Function이나 Class만 가져온다.

Q. 사용하지 않는 import는 제거해야 해?

A. 그렇다. 불필요한 Import는 가독성과 코드 품질을 낮춘다.

Q. 순환 Import는 무엇이야?

A. A Module이 B를 Import하고 B Module이 다시 A를 Import하는 구조이다.

Q. 순환 Import는 왜 피해야 해?

A. 실행 시점에 Module 초기화 문제가 생겨 ImportError가 발생할 수 있기 때문이다.

---

# 4. Package

## 4.1 Package Basics

### [개념]

Package는 여러 Module을 폴더 구조로 묶은 Python 코드 단위이다.

자동화 코드가 커지면 Script 하나가 아니라 Package 구조로 관리하는 것이 좋다.

```text
python_ai_automation
├ __init__.py
├ file_utils.py
├ markdown_validator.py
└ api_client.py
```

---

### [핵심]

- Package는 여러 Module을 묶는 디렉터리이다.
- `__init__.py`는 해당 디렉터리를 Package로 인식시키는 파일이다.
- Python 3에서는 Namespace Package도 가능하지만 명시적 `__init__.py`를 권장한다.
- 기능별 하위 Package를 만들 수 있다.
- Package 구조는 테스트와 배포에 유리하다.

---

### [실무]

권장 Package 구조:

```text
python_ai_automation
├ pyproject.toml
├ README.md
├ src
│  └ ai_automation
│     ├ __init__.py
│     ├ config.py
│     ├ file_utils.py
│     ├ markdown
│     │  ├ __init__.py
│     │  ├ parser.py
│     │  └ validator.py
│     ├ api
│     │  ├ __init__.py
│     │  └ client.py
│     └ report
│        ├ __init__.py
│        └ builder.py
└ tests
   ├ test_markdown_validator.py
   └ test_file_utils.py
```

간단한 단계에서는 다음 구조도 가능하다:

```text
python_ai_automation
├ main.py
├ file_utils.py
├ markdown_validator.py
├ api_client.py
└ tests
```

---

### [FAQ]

Q. Package는 언제 필요해?

A. Module이 많아지고 기능별 분리가 필요할 때 Package 구조가 좋다.

Q. `__init__.py`는 꼭 필요해?

A. Python 3에서는 없는 경우도 가능하지만 명시적으로 두는 것을 권장한다.

Q. 자동화 스크립트도 Package로 만들어야 해?

A. 작으면 단일 Script로 충분하지만, RAG 문서 자동화처럼 기능이 많아지면 Package 구조가 좋다.

Q. src 구조는 왜 사용해?

A. 프로젝트 코드와 테스트 코드, 설정 파일을 명확히 분리하기 위해 사용한다.

---

## 4.2 Relative Import and Absolute Import

### [개념]

Absolute Import는 Package 최상위 기준으로 Module을 가져오는 방식이다.

Relative Import는 현재 Module 위치를 기준으로 상대 경로처럼 가져오는 방식이다.

---

### [핵심]

- Absolute Import는 경로가 명확하다.
- Relative Import는 같은 Package 내부에서 짧게 사용할 수 있다.
- 복잡한 프로젝트에서는 Absolute Import를 우선 권장한다.
- Script 직접 실행과 Package 실행 방식에 따라 Import 오류가 발생할 수 있다.
- 실행 위치와 Python Path를 고려해야 한다.

---

### [실무]

Absolute Import 예시:

```python
from ai_automation.markdown.validator import find_missing_sections
```

Relative Import 예시:

```python
from .parser import parse_markdown_sections
```

권장:

```text
Package 내부 재사용 → Absolute Import 우선
같은 하위 Package 내부 짧은 참조 → Relative Import 가능
초기 학습/단순 자동화 → 같은 폴더 Module Import
```

실행 방식:

```bash
python main.py
```

Package 실행 방식:

```bash
python -m ai_automation.main
```

---

### [FAQ]

Q. Absolute Import는 뭐야?

A. Package 최상위 경로부터 Module을 명확히 지정해 Import하는 방식이다.

Q. Relative Import는 뭐야?

A. 현재 Module 위치를 기준으로 `.` 또는 `..`를 사용해 Import하는 방식이다.

Q. 어떤 Import 방식을 권장해?

A. 자동화 프로젝트에서는 명확한 Absolute Import를 우선 권장한다.

Q. ImportError가 나는 이유는?

A. 실행 위치, Python Path, Package 구조, 순환 Import가 맞지 않을 수 있다.

---

# 5. Script Entry Point

## 5.1 Main Function

### [개념]

Main Function은 Python Script의 실행 흐름을 시작하는 Function이다.

자동화 Script에서는 `main()`을 사용해 전체 작업 순서를 명확히 한다.

```python
def main() -> None:
    print("Processing started")


if __name__ == "__main__":
    main()
```

---

### [핵심]

- `main()`은 실행 흐름을 담당한다.
- 핵심 로직은 별도 Function으로 분리한다.
- `main()`은 입력 수집, Function 호출, 결과 출력 정도만 담당하는 것이 좋다.
- `if __name__ == "__main__":`는 직접 실행 시에만 실행되도록 한다.
- 테스트 대상 로직은 `main()` 밖에 둔다.

---

### [실무]

좋은 Entry Point:

```python
from pathlib import Path

from file_utils import read_text
from markdown_validator import find_missing_sections

def validate_document(path: Path) -> dict:
    text = read_text(path)
    missing_sections = find_missing_sections(text)

    return {
        "file_name": path.name,
        "is_valid": len(missing_sections) == 0,
        "missing_sections": missing_sections,
    }


def main() -> None:
    path = Path("docs/example.md")
    result = validate_document(path)
    print(result)


if __name__ == "__main__":
    main()
```

---

### [FAQ]

Q. main 함수는 왜 사용해?

A. Script 실행 흐름을 명확히 하고 테스트 가능한 구조로 만들기 위해 사용한다.

Q. main 안에 모든 로직을 넣어도 돼?

A. 권장하지 않는다. 핵심 로직은 별도 Function으로 분리한다.

Q. `if __name__ == "__main__"`는 왜 사용해?

A. 해당 파일이 직접 실행될 때만 main을 실행하기 위해 사용한다.

Q. 테스트 대상 로직은 어디에 둬야 해?

A. main 밖의 독립 Function에 둬야 한다.

---

## 5.2 Script vs Module

### [개념]

Script는 직접 실행되는 Python 파일이고, Module은 다른 코드에서 Import되어 재사용되는 Python 파일이다.

하나의 파일도 직접 실행되면 Script이고, Import되면 Module로 동작할 수 있다.

---

### [핵심]

- Script는 실행 목적이 강하다.
- Module은 재사용 목적이 강하다.
- 자동화 프로젝트에서는 실행용 Script와 재사용 Module을 분리한다.
- `main.py`는 실행 흐름을 담당한다.
- `file_utils.py`, `validator.py`, `api_client.py`는 재사용 Module로 둔다.

---

### [실무]

권장 분리:

```text
main.py → 실행 흐름
file_utils.py → 파일 처리 Function
markdown_validator.py → 문서 검증 Function
report_builder.py → 결과 보고서 생성 Function
api_client.py → API 호출 Function
```

`main.py`:

```python
from pathlib import Path

from file_utils import read_text
from markdown_validator import find_missing_sections

def main() -> None:
    path = Path("docs/example.md")
    text = read_text(path)
    missing_sections = find_missing_sections(text)
    print(missing_sections)


if __name__ == "__main__":
    main()
```

---

### [FAQ]

Q. Script와 Module 차이는?

A. Script는 직접 실행 목적이고, Module은 Import되어 재사용되는 목적이다.

Q. main.py에는 무엇을 넣어야 해?

A. 입력 수집, Function 호출, 결과 출력 같은 실행 흐름을 넣는다.

Q. 유틸 Function은 어디에 둬야 해?

A. `file_utils.py`, `json_utils.py`, `markdown_validator.py` 같은 Module에 둔다.

Q. 하나의 파일에 전부 작성하면 안 돼?

A. 작은 테스트는 가능하지만 유지보수와 테스트를 위해 기능별 분리를 권장한다.

---

# 6. Project Structure

## 6.1 Small Automation Structure

### [개념]

Small Automation Structure는 단순한 Python 자동화 스크립트를 위한 최소 구조이다.

초기 단계에서는 Package 구조보다 적은 파일로 시작할 수 있다.

---

### [핵심]

- 작은 자동화는 `main.py` 중심으로 시작한다.
- 기능이 늘어나면 Module을 분리한다.
- 테스트 파일은 `tests` 폴더에 둔다.
- 설정값은 `config.py` 또는 환경변수로 분리한다.
- 파일 경로 하드코딩을 줄인다.

---

### [실무]

작은 RAG 문서 검사 구조:

```text
rag_doc_checker
├ main.py
├ config.py
├ file_utils.py
├ markdown_validator.py
└ tests
   └ test_markdown_validator.py
```

`config.py`:

```python
REQUIRED_SECTIONS = ["[개념]", "[핵심]", "[실무]", "[FAQ]"]
RETRIEVAL_QUERY_TITLE = "# Retrieval Queries"
```

`markdown_validator.py`:

```python
from config import REQUIRED_SECTIONS, RETRIEVAL_QUERY_TITLE

def find_missing_sections(text: str) -> list[str]:
    return [
        section for section in REQUIRED_SECTIONS
        if section not in text
    ]


def has_retrieval_queries(text: str) -> bool:
    return RETRIEVAL_QUERY_TITLE in text
```

---

### [FAQ]

Q. 작은 자동화 프로젝트는 어떤 구조로 시작하면 돼?

A. `main.py`, `config.py`, 기능별 Module, `tests` 폴더 정도로 시작하면 된다.

Q. config.py에는 무엇을 넣어?

A. 필수 섹션 목록, 기본 경로, 기본 timeout, 고정 문자열 같은 설정값을 넣을 수 있다.

Q. 처음부터 src Package 구조가 필요해?

A. 작은 자동화라면 필수는 아니다. 기능이 커지면 src 구조로 확장하면 된다.

Q. tests 폴더는 꼭 필요해?

A. 자동화 품질을 높이려면 핵심 검증 Function 테스트용으로 두는 것이 좋다.

---

## 6.2 Scalable Automation Structure

### [개념]

Scalable Automation Structure는 자동화 프로젝트가 커졌을 때 유지보수와 테스트를 쉽게 하기 위한 Package 기반 구조이다.

RAG Document Automation, Agent Tool Script, API Integration이 함께 들어가면 Package 구조가 적합하다.

---

### [핵심]

- 기능별 Package를 분리한다.
- 파일 처리, Markdown 처리, API 처리, Report 생성을 나눈다.
- 설정과 실행 코드를 분리한다.
- tests를 별도로 관리한다.
- pyproject.toml 또는 requirements.txt로 의존성을 관리한다.

---

### [실무]

확장 가능한 구조:

```text
python_ai_automation
├ pyproject.toml
├ README.md
├ .env
├ .gitignore
├ src
│  └ ai_automation
│     ├ __init__.py
│     ├ config.py
│     ├ main.py
│     ├ file
│     │  ├ __init__.py
│     │  └ io.py
│     ├ markdown
│     │  ├ __init__.py
│     │  ├ parser.py
│     │  └ validator.py
│     ├ api
│     │  ├ __init__.py
│     │  └ client.py
│     ├ agent_tool
│     │  ├ __init__.py
│     │  └ document_check_tool.py
│     └ report
│        ├ __init__.py
│        └ builder.py
└ tests
   ├ test_file_io.py
   ├ test_markdown_validator.py
   └ test_document_check_tool.py
```

구조 기준:

```text
file → File I/O
markdown → Markdown Parsing / Validation
api → HTTP API Request
agent_tool → Agent Tool Script
report → Validation Report
tests → Unit Test
```

---

### [FAQ]

Q. 확장 가능한 Python 자동화 구조는 언제 필요해?

A. 파일 처리, Markdown 검증, API 호출, Agent Tool Script, 테스트가 함께 필요해질 때 적합하다.

Q. src 구조는 왜 좋아?

A. 프로젝트 코드와 테스트 코드, 설정 파일을 분리해 Import와 배포 구조를 명확히 할 수 있다.

Q. agent_tool 폴더에는 무엇을 넣어?

A. Agent가 호출할 수 있는 구조화된 Tool Function 또는 CLI Script를 넣는다.

Q. report 폴더에는 무엇을 넣어?

A. 검증 결과를 Markdown, JSON, CSV 등으로 만드는 Report Builder를 넣는다.

---

# 7. Function Module Package Best Practice

## 7.1 Best Practice

### [개념]

Function Module Package Best Practice는 Python 자동화 코드의 재사용성, 검증성, 유지보수성을 높이는 작성 기준이다.

목표:

```text
Small Function
→ Clear Module
→ Scalable Package
→ Testable Automation
→ Agent-Friendly Structure
```

---

### [핵심]

- Function은 하나의 책임만 가진다.
- Function 입력과 출력은 명확히 작성한다.
- Type Hint를 사용한다.
- Function 이름은 동작 중심으로 작성한다.
- Module은 기능 단위로 분리한다.
- Package는 확장 가능한 구조로 관리한다.
- 실행용 Script와 재사용 Module을 분리한다.
- `main()`은 실행 흐름만 담당한다.
- Import 순서를 정리한다.
- 순환 Import를 피한다.
- 하드코딩된 경로를 줄인다.
- 테스트 가능한 Pure Function을 늘린다.

---

### [실무]

권장 작성 순서:

```text
1. 핵심 작업을 Function으로 분리
2. Function 입력과 반환값 정의
3. Type Hint 추가
4. 관련 Function을 Module로 이동
5. 실행 흐름을 main.py에 구성
6. 설정값을 config.py로 분리
7. 테스트 대상 Function 선정
8. Package 구조로 확장
```

Agent-Friendly Function 예시:

```python
def validate_document_text(text: str) -> dict:
    required_sections = ["[개념]", "[핵심]", "[실무]", "[FAQ]"]

    missing_sections = [
        section for section in required_sections
        if section not in text
    ]

    return {
        "status": "success",
        "is_valid": len(missing_sections) == 0,
        "missing_sections": missing_sections,
    }
```

---

### [FAQ]

Q. Agent-Friendly Python 구조는 어떤 구조야?

A. Function 입력과 출력이 명확하고, 결과가 dict 또는 JSON 형태로 구조화된 구조이다.

Q. Function, Module, Package의 관계는?

A. Function은 실행 단위, Module은 Python 파일, Package는 여러 Module을 묶은 폴더 구조이다.

Q. Python 자동화에서 가장 먼저 분리할 것은?

A. 파일 읽기, 데이터 변환, 검증, 결과 생성 Function을 먼저 분리한다.

Q. Package 구조는 언제 도입해?

A. Module이 많아지고 테스트, API, Agent Tool 기능이 늘어날 때 도입한다.

---

# Retrieval Queries

### [FAQ]

Q. Python Function은 무엇이야?
A. 반복 가능한 작업을 이름으로 묶어 재사용하는 실행 단위이다.

Q. Python 자동화에서 Function은 왜 중요해?
A. 반복 로직을 재사용하고 테스트 가능한 단위로 분리할 수 있기 때문이다.

Q. Python Function 이름은 어떻게 작성해?
A. `read_file`, `validate_document`, `extract_sections`, `build_result`처럼 동작이 드러나게 작성한다.

Q. Python Function은 하나의 일만 해야 해?
A. 그렇다. 하나의 Function은 하나의 책임만 가지는 것이 좋다.

Q. Python Function Parameter는 뭐야?
A. Function에 전달되는 입력값이다.

Q. Python Function Return은 뭐야?
A. Function이 처리 후 돌려주는 출력값이다.

Q. Python 자동화 Function 반환값은 어떤 형태가 좋아?
A. Agent가 처리하기 쉬운 dict, list, bool, str 같은 명확한 형태가 좋다.

Q. Python Function에서 print만 쓰면 안 좋아?
A. 핵심 로직은 Return을 사용해야 재사용과 테스트가 쉽다.

Q. Python Default Parameter는 언제 사용해?
A. encoding, timeout, retry count처럼 기본값이 명확한 옵션에 사용한다.

Q. Python Keyword Argument는 왜 좋아?
A. 어떤 Parameter에 어떤 값이 들어가는지 명확해져 가독성과 안정성이 좋아진다.

Q. Python에서 list를 Default Parameter로 쓰면 안 돼?
A. Function 호출 간 같은 list 객체가 공유되어 예기치 않은 결과가 발생할 수 있으므로 피해야 한다.

Q. Python mutable default 대신 무엇을 써?
A. 기본값을 `None`으로 두고 Function 내부에서 새 list나 dict를 생성한다.

Q. Python Single Responsibility Function은 뭐야?
A. 하나의 Function이 하나의 역할만 수행하도록 작성하는 원칙이다.

Q. Python Function을 분리하는 기준은?
A. 읽기, 변환, 검증, 저장, 결과 생성 단위로 분리한다.

Q. Python Pure Function은 뭐야?
A. 같은 입력에 항상 같은 출력을 반환하고 외부 상태를 변경하지 않는 Function이다.

Q. Python Pure Function은 어디에 사용해?
A. 문자열 정리, Section 검사, Metadata 변환, 결과 생성 로직에 사용하면 좋다.

Q. Python 파일 읽기 Function은 Pure Function이야?
A. 아니다. 파일 시스템 상태에 의존하므로 Pure Function이 아니다.

Q. Python Function Error Handling은 왜 필요해?
A. 자동화 실패 지점을 명확히 추적하고 안정적으로 처리하기 위해 필요하다.

Q. Python Function에서 except pass를 써도 돼?
A. 권장하지 않는다. 오류 원인을 숨겨 자동화 실패를 추적하기 어렵다.

Q. Python Agent Tool Function 오류는 어떻게 반환해?
A. `status`, `result`, `error`를 포함한 dict 형태로 구조화하는 것이 좋다.

Q. Python Module은 뭐야?
A. 하나의 `.py` 파일이 Module이며 Function과 Class를 재사용 가능한 단위로 묶는다.

Q. Python Module은 왜 나눠?
A. 기능별로 코드를 분리하면 유지보수, 테스트, 재사용이 쉬워진다.

Q. Python Module 이름은 어떻게 정해?
A. `file_utils`, `api_client`, `markdown_validator`처럼 역할이 드러나게 작성한다.

Q. Python import module과 from module import name 차이는?
A. import module은 Module 전체를 가져오고, from import는 특정 Function이나 Class만 가져온다.

Q. Python Import 순서는 어떻게 정리해?
A. Standard Library → Third Party Library → Local Application Module 순서로 정리한다.

Q. Python 순환 Import는 뭐야?
A. A Module이 B를 Import하고 B Module이 다시 A를 Import하는 구조이다.

Q. Python 순환 Import는 왜 피해야 해?
A. Module 초기화 문제가 생겨 ImportError가 발생할 수 있기 때문이다.

Q. Python Package는 뭐야?
A. 여러 Module을 폴더 구조로 묶은 Python 코드 단위이다.

Q. Python Package는 언제 필요해?
A. Module이 많아지고 기능별 분리가 필요할 때 Package 구조가 좋다.

Q. Python `__init__.py`는 왜 사용해?
A. 해당 디렉터리를 Package로 인식시키기 위해 사용한다.

Q. Python src 구조는 왜 사용해?
A. 프로젝트 코드와 테스트 코드, 설정 파일을 명확히 분리하기 위해 사용한다.

Q. Python Absolute Import는 뭐야?
A. Package 최상위 경로부터 Module을 명확히 지정해 Import하는 방식이다.

Q. Python Relative Import는 뭐야?
A. 현재 Module 위치를 기준으로 `.` 또는 `..`를 사용해 Import하는 방식이다.

Q. Python 자동화 프로젝트에서 어떤 Import 방식을 권장해?
A. 명확한 Absolute Import를 우선 권장한다.

Q. Python ImportError는 왜 발생해?
A. 실행 위치, Python Path, Package 구조, 순환 Import가 맞지 않을 수 있다.

Q. Python main 함수는 왜 사용해?
A. Script 실행 흐름을 명확히 하고 테스트 가능한 구조로 만들기 위해 사용한다.

Q. Python main 안에 모든 로직을 넣어도 돼?
A. 권장하지 않는다. 핵심 로직은 별도 Function으로 분리한다.

Q. Python `if __name__ == "__main__"`는 왜 사용해?
A. 해당 파일이 직접 실행될 때만 main을 실행하기 위해 사용한다.

Q. Python Script와 Module 차이는?
A. Script는 직접 실행 목적이고 Module은 Import되어 재사용되는 목적이다.

Q. Python main.py에는 무엇을 넣어?
A. 입력 수집, Function 호출, 결과 출력 같은 실행 흐름을 넣는다.

Q. Python 유틸 Function은 어디에 둬?
A. `file_utils.py`, `json_utils.py`, `markdown_validator.py` 같은 Module에 둔다.

Q. 작은 Python 자동화 프로젝트 구조는 어떻게 시작해?
A. `main.py`, `config.py`, 기능별 Module, `tests` 폴더로 시작하면 된다.

Q. Python config.py에는 무엇을 넣어?
A. 필수 섹션 목록, 기본 경로, 기본 timeout, 고정 문자열 같은 설정값을 넣는다.

Q. Python 확장 자동화 프로젝트 구조는 어떻게 잡아?
A. src 기반 Package 구조로 file, markdown, api, agent_tool, report, tests를 분리한다.

Q. Python agent_tool 폴더에는 무엇을 넣어?
A. Agent가 호출할 수 있는 구조화된 Tool Function 또는 CLI Script를 넣는다.

Q. Python report 폴더에는 무엇을 넣어?
A. 검증 결과를 Markdown, JSON, CSV 등으로 만드는 Report Builder를 넣는다.

Q. Python Agent-Friendly 구조는 무엇이야?
A. Function 입력과 출력이 명확하고 결과가 dict 또는 JSON 형태로 구조화된 구조이다.

Q. Python Function Module Package 관계는?
A. Function은 실행 단위, Module은 Python 파일, Package는 여러 Module을 묶은 폴더 구조이다.

Q. Python 자동화 코드에서 가장 먼저 분리할 것은?
A. 파일 읽기, 데이터 변환, 검증, 결과 생성 Function을 먼저 분리한다.
