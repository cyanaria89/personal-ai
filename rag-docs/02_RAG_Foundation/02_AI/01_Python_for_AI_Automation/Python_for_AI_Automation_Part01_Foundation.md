# Python for AI Automation Part01 - Foundation

---

# 1. Python for AI Automation Overview

## 1.1 Python for AI Automation

### [개념]

Python for AI Automation은 AI Agent가 반복 작업, 파일 처리, API 호출, 데이터 전처리, RAG 문서 검증, Agent Tool Script 실행을 자동화하기 위해 사용하는 기본 실행 언어이다.

이 문서는 Python을 학습용 문법 나열이 아니라 AI Automation Script 작성, RAG Document Automation, Agent Tool Script 구현을 위한 Retrieval 기준 문서로 정리한다.

기본 Flow:

```text
Input
→ Python Script
→ Processing
→ Output
→ Logging / Error Handling
```

---

### [핵심]

- Python은 AI Automation에서 가장 많이 사용되는 범용 스크립트 언어이다.
- Python은 File I/O, JSON Processing, CSV Processing, Markdown Processing, API Request 자동화에 적합하다.
- Agent Tool Script는 Python 함수 또는 CLI Script 형태로 구현할 수 있다.
- RAG Document Automation은 Markdown 파일 스캔, 필수 섹션 검사, Retrieval Queries 검사, Chunk 준비로 구성된다.
- Python 문서는 Python 3.11+ 기준으로 작성한다.
- Python 3.12를 권장한다.
- Modern Python 기준으로 pathlib, Type Hint, dataclass, logging 사용을 우선한다.

---

### [실무]

2026 실무 기준 Python for AI Automation은 단순 문법보다 자동화 가능한 구조가 중요하다.

주요 사용 영역:

- RAG 문서 폴더 스캔
- Markdown Header Parsing
- Retrieval Queries 존재 여부 검사
- JSON 설정 파일 읽기
- CSV 메타데이터 처리
- API 호출 자동화
- LLM API Request 구성
- Agent Tool Input 검증
- Agent Tool Output JSON 반환
- 파일 변환 자동화
- 로그 기록
- 예외 처리
- 테스트 가능한 함수 분리

권장 구조:

```text
python_ai_automation
├ main.py
├ config.py
├ file_utils.py
├ api_client.py
├ markdown_processor.py
├ validators.py
└ tests
```

---

### [FAQ]

Q. Python for AI Automation은 무엇을 위한 문서인가?

A. AI Agent가 자동화 스크립트, RAG 문서 처리, API 호출, Agent Tool Script를 작성하고 검수하기 위한 Python 기준 문서이다.

Q. Python 문서를 문법 중심으로 작성하면 안 되는 이유는?

A. RAG 문서는 사람용 학습서가 아니라 Agent Retrieval, Code Generation, Review 지원용 문서이기 때문이다.

Q. Python for AI Automation에서 가장 중요한 기준은?

A. 파일 처리, 데이터 처리, API 호출, 예외 처리, 로깅, Agent Tool Output 구조화이다.

Q. Python 버전 기준은 무엇인가?

A. Python 3.11+를 기준으로 하며 Python 3.12를 권장한다.

Q. Python 자동화에서 pathlib을 우선 사용하는 이유는?

A. Windows와 Linux 경로 차이를 줄이고 파일 존재 확인, 확장자 확인, 폴더 탐색을 안전하게 처리할 수 있기 때문이다.

---

# 2. Python Basic Syntax

## 2.1 Variable

### [개념]

Variable은 값을 저장하고 재사용하기 위한 이름이다.

Python은 변수 선언 시 타입을 명시하지 않아도 된다.

```python
document_name = "Python_for_AI_Automation"
part_number = 1
enabled = True
```

---

### [핵심]

- Python 변수는 값을 대입하면 생성된다.
- 변수명은 의미 있게 작성한다.
- 변수명은 snake_case를 권장한다.
- 변수는 자동화 스크립트의 설정값, 파일명, 경로, 결과값 저장에 사용된다.
- 전역 변수 남용은 피한다.

---

### [실무]

자동화 스크립트에서는 변수명을 작업 의도와 연결해야 한다.

좋은 예:

```python
input_dir = "docs"
output_file = "report.json"
max_chunk_size = 1200
```

나쁜 예:

```python
a = "docs"
b = "report.json"
c = 1200
```

권장:

- `input_dir`
- `output_dir`
- `file_path`
- `document_title`
- `chunk_size`
- `api_response`
- `error_message`

---

### [FAQ]

Q. Python 변수는 타입을 꼭 써야 해?

A. 필수는 아니다. 다만 함수 입력과 출력에는 Type Hint를 쓰는 것이 좋다.

Q. Python 변수명은 어떻게 작성하는 게 좋아?

A. 자동화 목적이 드러나도록 snake_case로 작성하는 것이 좋다.

Q. 전역 변수는 사용해도 돼?

A. 설정 상수 정도는 가능하지만, 변경되는 상태값을 전역 변수로 남용하면 유지보수가 어려워진다.

Q. Agent가 이해하기 좋은 변수명은?

A. `file_path`, `document_text`, `section_title`, `api_result`처럼 역할이 명확한 이름이다.

---

# 3. Python Data Types

## 3.1 Primitive Data Types

### [개념]

Primitive Data Type은 Python에서 기본 값을 표현하는 자료형이다.

기본 자료형:

- `str`
- `int`
- `float`
- `bool`
- `None`

```python
title = "RAG Document"
count = 10
score = 97.5
is_valid = True
missing_value = None
```

---

### [핵심]

- `str`은 문자열이다.
- `int`는 정수이다.
- `float`는 실수이다.
- `bool`은 참/거짓 값이다.
- `None`은 값이 없음을 의미한다.
- API Response, Config, Validation Result에서 자주 사용된다.

---

### [실무]

자동화 스크립트에서 자료형은 결과 구조를 명확히 하기 위해 사용한다.

예시:

```python
file_name = "Python_Part01.md"
section_count = 5
quality_score = 98.0
has_retrieval_queries = True
error_message = None
```

검증 결과 표현 예시:

```python
result = {
    "file_name": file_name,
    "is_valid": has_retrieval_queries,
    "score": quality_score,
    "error": error_message,
}
```

---

### [FAQ]

Q. None은 언제 사용해?

A. 값이 아직 없거나 실패 원인이 없음을 표현할 때 사용한다.

Q. bool은 자동화에서 어디에 많이 쓰여?

A. 필수 섹션 존재 여부, 검증 성공 여부, 파일 존재 여부 같은 상태 판단에 사용된다.

Q. float는 어디에 사용해?

A. 품질 점수, 유사도 점수, 비율 계산 같은 값에 사용한다.

---

## 3.2 Collection Data Types

### [개념]

Collection Data Type은 여러 값을 저장하는 자료형이다.

기본 Collection:

- `list`
- `tuple`
- `dict`
- `set`

```python
files = ["part01.md", "part02.md"]

document_meta = {
    "title": "Python Foundation",
    "domain": "AI Automation",
    "level": 2,
}

required_sections = {"[개념]", "[핵심]", "[실무]", "[FAQ]"}
```

---

### [핵심]

- `list`는 순서 있는 여러 값이다.
- `tuple`은 변경하지 않을 값 묶음이다.
- `dict`는 key-value 구조이다.
- `set`은 중복 제거와 포함 여부 검사에 유용하다.
- JSON 데이터는 대부분 `dict`와 `list` 조합으로 처리된다.
- RAG 문서 메타데이터는 `dict` 또는 `dataclass`로 표현할 수 있다.

---

### [실무]

RAG Document Automation에서는 `list`, `dict`, `set`을 자주 사용한다.

파일 목록:

```python
md_files = ["Python_Part01.md", "Python_Part02.md"]
```

문서 메타데이터:

```python
metadata = {
    "file_name": "Python_for_AI_Automation_Part01_Foundation.md",
    "domain": "Python for AI Automation",
    "required_sections": ["[개념]", "[핵심]", "[실무]", "[FAQ]"],
}
```

필수 섹션 검사:

```python
required_sections = {"[개념]", "[핵심]", "[실무]", "[FAQ]"}
found_sections = {"[개념]", "[핵심]", "[실무]"}

missing_sections = required_sections - found_sections
```

---

### [FAQ]

Q. list는 언제 써?

A. 파일 목록, 문서 목록, 처리 결과 목록처럼 순서 있는 여러 값을 다룰 때 사용한다.

Q. dict는 언제 써?

A. JSON 데이터, 설정값, 문서 메타데이터, API Response를 처리할 때 사용한다.

Q. set은 언제 써?

A. 중복 제거, 필수 섹션 누락 검사, 포함 여부 확인에 사용한다.

Q. tuple은 언제 써?

A. 변경되지 않는 좌표, 고정 옵션, 함수 반환값 묶음에 사용할 수 있다.

Q. JSON 데이터는 Python에서 어떤 타입으로 다뤄?

A. JSON Object는 dict, JSON Array는 list로 다룬다.

---

# 4. Condition and Loop

## 4.1 Condition

### [개념]

Condition은 조건에 따라 다른 로직을 실행하는 문법이다.

```python
score = 97

if score >= 95:
    result = "pass"
else:
    result = "fail"
```

---

### [핵심]

- `if`는 조건이 참일 때 실행된다.
- `elif`는 추가 조건을 검사한다.
- `else`는 모든 조건이 거짓일 때 실행된다.
- Python은 들여쓰기로 Block을 구분한다.
- 자동화 스크립트에서는 검증 조건, 파일 존재 여부, API 응답 상태 판단에 사용된다.

---

### [실무]

파일 존재 여부 검사:

```python
from pathlib import Path

path = Path("docs/example.md")

if path.exists():
    text = path.read_text(encoding="utf-8")
else:
    raise FileNotFoundError(f"File not found: {path}")
```

필수 섹션 검사:

```python
required_section = "[FAQ]"

if required_section in document_text:
    is_valid = True
else:
    is_valid = False
```

---

### [FAQ]

Q. Python에서 조건문은 어디에 많이 사용해?

A. 파일 존재 여부, 필수 섹션 검사, API 응답 상태 확인, 설정값 누락 확인에 사용한다.

Q. Python 조건문에서 들여쓰기가 중요한 이유는?

A. Python은 중괄호가 아니라 들여쓰기로 실행 Block을 구분하기 때문이다.

Q. 조건이 많아지면 어떻게 해야 해?

A. 복잡한 조건은 함수로 분리하거나 검증 로직을 별도 Validator로 분리하는 것이 좋다.

---

## 4.2 Loop

### [개념]

Loop는 반복 작업을 처리하는 문법이다.

Python의 주요 반복문:

- `for`
- `while`

```python
files = ["part01.md", "part02.md"]

for file_name in files:
    print(file_name)
```

---

### [핵심]

- `for`는 목록을 순회할 때 사용한다.
- `while`은 조건이 참인 동안 반복한다.
- 자동화 스크립트에서는 파일 목록 처리, 문서 검증, API 결과 순회에 사용한다.
- 무한 반복을 피해야 한다.
- 반복 내부 로직이 길어지면 함수로 분리한다.

---

### [실무]

Markdown 파일 목록 처리:

```python
from pathlib import Path

base_dir = Path("docs")

for md_file in base_dir.rglob("*.md"):
    text = md_file.read_text(encoding="utf-8")
    print(md_file.name, len(text))
```

검증 결과 수집:

```python
results = []

for file_name in ["part01.md", "part02.md"]:
    results.append({
        "file_name": file_name,
        "checked": True,
    })
```

---

### [FAQ]

Q. for 문은 자동화에서 언제 사용해?

A. 여러 파일, 여러 문서, 여러 API 결과를 순서대로 처리할 때 사용한다.

Q. while 문은 자주 사용해?

A. 반복 종료 조건이 명확한 경우에 사용하지만, 파일 처리 자동화에서는 for 문이 더 자주 사용된다.

Q. 반복문 내부 코드가 길어지면 어떻게 해?

A. 반복 대상 처리 로직을 함수로 분리한다.

Q. rglob은 반복문과 같이 많이 써?

A. 그렇다. `Path.rglob("*.md")`로 Markdown 파일을 찾고 for 문으로 순회할 수 있다.

---

# 5. Function

## 5.1 Function Definition

### [개념]

Function은 반복 가능한 로직을 이름 붙여 재사용하는 단위이다.

```python
def clean_title(title: str) -> str:
    return title.strip().replace("#", "").strip()
```

---

### [핵심]

- 함수는 하나의 책임만 가지는 것이 좋다.
- 함수명은 동작을 설명해야 한다.
- 입력과 출력이 명확해야 한다.
- Type Hint를 사용한다.
- Docstring으로 함수 목적을 설명할 수 있다.
- 자동화 코드는 함수 단위로 나누면 테스트와 재사용이 쉬워진다.

---

### [실무]

파일 읽기 함수:

```python
from pathlib import Path

def read_text_file(path: Path) -> str:
    """Read a UTF-8 text file."""
    return path.read_text(encoding="utf-8")
```

필수 섹션 검사 함수:

```python
def has_required_sections(text: str, sections: list[str]) -> bool:
    """Check whether all required sections exist in text."""
    return all(section in text for section in sections)
```

검증 결과 반환 함수:

```python
def validate_document(text: str) -> dict:
    required_sections = ["[개념]", "[핵심]", "[실무]", "[FAQ]"]

    return {
        "has_required_sections": has_required_sections(text, required_sections),
        "has_retrieval_queries": "# Retrieval Queries" in text,
    }
```

---

### [FAQ]

Q. Python 자동화에서 함수는 왜 중요해?

A. 반복 로직을 재사용하고 테스트 가능한 단위로 분리할 수 있기 때문이다.

Q. 함수는 얼마나 작게 만들어야 해?

A. 하나의 함수는 하나의 책임만 갖는 것이 좋다.

Q. Type Hint는 함수에 꼭 필요해?

A. 필수는 아니지만 Agent 코드 생성과 리뷰 품질을 높이기 위해 권장한다.

Q. 함수명은 어떻게 작성해?

A. `read_text_file`, `validate_document`, `extract_sections`처럼 동작이 드러나게 작성한다.

Q. 함수가 dict를 반환해도 돼?

A. 가능하다. Agent Tool Output이나 Validation Result는 dict로 구조화하면 좋다.

---

# 6. Import and Module

## 6.1 Import

### [개념]

Import는 다른 Module의 기능을 현재 Python 파일에서 사용하기 위한 문법이다.

```python
from pathlib import Path
import json
import logging
```

---

### [핵심]

- Module은 Python 파일 단위이다.
- Package는 여러 Module을 묶은 구조이다.
- `import module` 형식으로 Module 전체를 가져올 수 있다.
- `from module import name` 형식으로 필요한 기능만 가져올 수 있다.
- 표준 라이브러리를 우선 활용한다.
- 불필요한 외부 패키지 추가를 피한다.

---

### [실무]

자동화 스크립트에서 자주 쓰는 Import:

```python
from pathlib import Path
import json
import csv
import logging
import os
```

API 호출용 Import:

```python
import requests
```

Type Hint용 Import:

```python
from typing import Optional
```

---

### [FAQ]

Q. import는 왜 필요해?

A. 파일 처리, JSON 처리, 로깅, API 호출 같은 기능을 재사용하기 위해 필요하다.

Q. pathlib은 어떻게 import해?

A. `from pathlib import Path`를 사용한다.

Q. json은 외부 설치가 필요해?

A. 아니다. json은 Python 표준 라이브러리이다.

Q. requests는 표준 라이브러리야?

A. 아니다. requests는 별도 설치가 필요한 외부 패키지이다.

Q. 사용하지 않는 import는 놔둬도 돼?

A. 제거하는 것이 좋다. 불필요한 import는 코드 가독성과 품질을 낮춘다.

---

# 7. Comment and Docstring

## 7.1 Comment

### [개념]

Comment는 코드 실행에는 영향을 주지 않고 설명을 남기는 문법이다.

```python
# Read Markdown document text
text = path.read_text(encoding="utf-8")
```

---

### [핵심]

- Comment는 복잡한 의도를 설명할 때 사용한다.
- 당연한 코드를 반복 설명하지 않는다.
- 코드와 맞지 않는 오래된 Comment는 제거한다.
- 자동화 스크립트에서는 주의사항, 위험 작업, 처리 기준을 남기는 데 유용하다.

---

### [실무]

좋은 Comment:

```python
# Do not overwrite the original document before validation passes.
backup_path = path.with_suffix(".backup.md")
```

나쁜 Comment:

```python
# Add 1 to count
count = count + 1
```

---

### [FAQ]

Q. Comment는 많이 쓰는 게 좋아?

A. 필요한 곳에만 쓰는 것이 좋다. 코드 자체가 명확하면 Comment를 줄일 수 있다.

Q. 자동화 코드에서 Comment가 필요한 곳은?

A. 파일 덮어쓰기, 삭제, 외부 API 호출, 위험 작업, 검증 기준처럼 의도를 명확히 해야 하는 곳이다.

Q. 오래된 Comment는 왜 위험해?

A. 실제 코드와 다르면 Agent나 개발자가 잘못 이해할 수 있기 때문이다.

---

## 7.2 Docstring

### [개념]

Docstring은 함수, 클래스, 모듈의 목적을 설명하는 문자열이다.

```python
def read_text_file(path: Path) -> str:
    """Read a UTF-8 text file from the given path."""
    return path.read_text(encoding="utf-8")
```

---

### [핵심]

- Docstring은 함수 목적을 짧게 설명한다.
- Agent가 함수 역할을 이해하는 데 도움이 된다.
- 테스트 대상 함수에는 Docstring을 권장한다.
- 긴 설명보다 입력, 출력, 목적을 명확히 작성한다.

---

### [실무]

Agent Tool 함수 Docstring 예시:

```python
def validate_rag_document(path: Path) -> dict:
    """Validate required RAG sections and return structured result."""
    text = path.read_text(encoding="utf-8")

    return {
        "file_name": path.name,
        "has_faq": "[FAQ]" in text,
        "has_retrieval_queries": "# Retrieval Queries" in text,
    }
```

---

### [FAQ]

Q. Docstring은 Comment와 뭐가 달라?

A. Comment는 코드 중간 설명이고, Docstring은 함수나 클래스의 공식 설명 문자열이다.

Q. 모든 함수에 Docstring을 써야 해?

A. 간단한 내부 함수는 생략 가능하지만, 재사용 함수와 Agent Tool 함수에는 권장한다.

Q. Docstring은 길게 써야 해?

A. 아니다. 목적과 반환 구조를 짧고 명확하게 쓰는 것이 좋다.

---

# 8. Indentation

## 8.1 Python Indentation

### [개념]

Indentation은 Python에서 코드 Block을 구분하는 문법 요소이다.

Python은 `{}`가 아니라 들여쓰기로 조건문, 반복문, 함수, 클래스 내부를 구분한다.

```python
if True:
    print("valid")
```

---

### [핵심]

- Python은 들여쓰기가 문법이다.
- 일반적으로 공백 4칸을 사용한다.
- 들여쓰기가 맞지 않으면 `IndentationError`가 발생한다.
- 조건문, 반복문, 함수 내부는 반드시 들여쓰기한다.
- 자동화 스크립트에서 들여쓰기 오류는 실행 실패로 이어진다.

---

### [실무]

올바른 예:

```python
def validate(text: str) -> bool:
    if "[FAQ]" in text:
        return True
    return False
```

잘못된 예:

```python
def validate(text: str) -> bool:
if "[FAQ]" in text:
return True
```

---

### [FAQ]

Q. Python에서 들여쓰기는 왜 중요해?

A. Python은 들여쓰기로 코드 Block을 구분하기 때문에 문법적으로 필수이다.

Q. 들여쓰기는 몇 칸을 쓰는 게 좋아?

A. 일반적으로 공백 4칸을 사용한다.

Q. 들여쓰기 오류는 어떤 에러를 발생시켜?

A. `IndentationError` 또는 `SyntaxError`가 발생할 수 있다.

Q. Tab과 Space를 섞어도 돼?

A. 섞지 않는 것이 좋다. 공백 4칸으로 통일한다.

---

# 9. Basic Script Structure

## 9.1 Script Entry Point

### [개념]

Script Entry Point는 Python 파일이 직접 실행될 때 시작되는 지점을 의미한다.

```python
def main() -> None:
    print("Processing started")


if __name__ == "__main__":
    main()
```

---

### [핵심]

- `main()` 함수는 실행 흐름을 명확히 한다.
- `if __name__ == "__main__":`는 직접 실행 여부를 확인한다.
- 함수와 실행 코드를 분리하면 테스트하기 쉽다.
- 자동화 스크립트는 Entry Point를 명확히 두는 것이 좋다.

---

### [실무]

RAG 문서 검사 스크립트 구조:

```python
from pathlib import Path

def validate_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")

    return {
        "file_name": path.name,
        "has_faq": "[FAQ]" in text,
        "has_retrieval_queries": "# Retrieval Queries" in text,
    }


def main() -> None:
    base_dir = Path("docs")

    for md_file in base_dir.rglob("*.md"):
        result = validate_file(md_file)
        print(result)


if __name__ == "__main__":
    main()
```

---

### [FAQ]

Q. main 함수는 꼭 필요해?

A. 필수는 아니지만 자동화 스크립트 구조를 명확히 하고 테스트하기 쉽게 만들기 위해 권장한다.

Q. `if __name__ == "__main__"`는 왜 써?

A. 해당 파일이 직접 실행될 때만 main 함수를 실행하기 위해 사용한다.

Q. 스크립트 맨 아래에 바로 코드를 작성하면 안 돼?

A. 가능하지만 코드 재사용과 테스트가 어려워지므로 main 함수로 분리하는 것이 좋다.

---

# 10. Foundation Best Practice

## 10.1 Python Foundation Best Practice

### [개념]

Python Foundation Best Practice는 AI Automation Script의 기본 품질을 보장하기 위한 최소 작성 기준이다.

목표:

```text
Readable Code
→ Reusable Function
→ Safe File Handling
→ Structured Result
→ Testable Script
```

---

### [핵심]

- Python 3.11+ 기준으로 작성한다.
- 변수명과 함수명은 의미 있게 작성한다.
- 파일 경로는 pathlib을 우선 사용한다.
- 파일 입출력에는 UTF-8 encoding을 명시한다.
- 반복 로직은 함수로 분리한다.
- 예외 발생 가능성을 고려한다.
- 출력 결과는 dict 또는 JSON 형태로 구조화한다.
- API Key는 코드에 직접 작성하지 않는다.
- 자동화 스크립트는 logging 사용을 고려한다.
- 핵심 로직은 테스트 가능하게 분리한다.

---

### [실무]

좋은 Foundation Script 기준:

```python
from pathlib import Path

REQUIRED_SECTIONS = ["[개념]", "[핵심]", "[실무]", "[FAQ]"]


def read_document(path: Path) -> str:
    """Read a Markdown document as UTF-8 text."""
    return path.read_text(encoding="utf-8")


def validate_required_sections(text: str) -> dict:
    """Validate required RAG sections."""
    missing_sections = [
        section for section in REQUIRED_SECTIONS
        if section not in text
    ]

    return {
        "is_valid": len(missing_sections) == 0,
        "missing_sections": missing_sections,
    }


def main() -> None:
    path = Path("docs/Python_for_AI_Automation_Part01_Foundation.md")
    text = read_document(path)
    result = validate_required_sections(text)
    print(result)


if __name__ == "__main__":
    main()
```

---

### [FAQ]

Q. Python Foundation 단계에서 반드시 알아야 하는 것은?

A. 변수, 자료형, 조건문, 반복문, 함수, import, 들여쓰기, 기본 스크립트 구조이다.

Q. Python 자동화 코드에서 가장 중요한 습관은?

A. 의미 있는 이름, 함수 분리, pathlib 사용, encoding 명시, 구조화된 결과 반환이다.

Q. 자동화 스크립트 결과는 어떤 형태가 좋아?

A. Agent가 처리하기 쉽도록 dict 또는 JSON 형태가 좋다.

Q. Foundation 단계에서 class까지 꼭 다뤄야 해?

A. 필수는 아니다. 기본 자동화는 함수 중심으로 충분하며 class는 상태와 동작을 묶을 때 사용한다.

Q. Python Foundation 문서에도 FAQ가 필요한가?

A. 필요하다. FAQ는 사용자 질문 패턴과 Retrieval Matching을 강화한다.

---

# Retrieval Queries

### [FAQ]

Q. Python for AI Automation이 뭐야?
A. AI Agent가 자동화 스크립트, 파일 처리, API 호출, RAG 문서 검증, Agent Tool Script 작성을 수행하기 위한 Python 활용 영역이다.

Q. Python for AI Automation 문서는 사람 공부용 문서야?
A. 아니다. AI Agent Retrieval, Code Generation, Review, Validation을 지원하기 위한 RAG 최적화 문서이다.

Q. Python 자동화 기본 흐름은 어떻게 돼?
A. Input → Python Script → Processing → Output → Logging / Error Handling 흐름으로 구성된다.

Q. Python 자동화에서 가장 많이 쓰는 작업은?
A. 파일 읽기, 폴더 스캔, JSON 처리, CSV 처리, Markdown 처리, API 호출, 결과 검증이다.

Q. Python for AI Automation 기준 버전은?
A. Python 3.11+ 기준이며 Python 3.12를 권장한다.

Q. Python 변수는 어떻게 선언해?
A. `name = "value"`처럼 값을 대입하면 변수가 생성된다.

Q. Python 변수명은 어떻게 짓는 게 좋아?
A. `file_path`, `document_text`, `section_title`처럼 역할이 명확한 snake_case 이름을 권장한다.

Q. Python 기본 자료형은 뭐가 있어?
A. str, int, float, bool, None이 있다.

Q. Python Collection 자료형은 뭐가 있어?
A. list, tuple, dict, set이 있다.

Q. Python에서 list는 언제 써?
A. 파일 목록, 문서 목록, API 결과 목록처럼 순서 있는 여러 값을 처리할 때 사용한다.

Q. Python에서 dict는 언제 써?
A. JSON 데이터, 설정값, 문서 메타데이터, 검증 결과를 key-value 구조로 다룰 때 사용한다.

Q. Python에서 set은 언제 써?
A. 중복 제거, 필수 섹션 누락 검사, 포함 여부 확인에 사용한다.

Q. Python에서 None은 무슨 뜻이야?
A. 값이 없음을 의미한다.

Q. Python 조건문은 어떻게 써?
A. `if`, `elif`, `else`를 사용해 조건에 따라 다른 코드를 실행한다.

Q. Python 조건문은 자동화에서 어디에 써?
A. 파일 존재 여부, 필수 섹션 검사, API 응답 상태 확인, 설정값 누락 확인에 사용한다.

Q. Python 반복문은 어떻게 써?
A. `for` 또는 `while`을 사용한다.

Q. Python for 문은 자동화에서 어디에 써?
A. 여러 파일, 여러 문서, 여러 API 결과를 순회할 때 사용한다.

Q. Python 함수는 왜 필요해?
A. 반복 로직을 재사용하고 테스트 가능한 단위로 분리하기 위해 필요하다.

Q. Python 함수는 어떻게 작성해?
A. `def function_name(parameter):` 형태로 작성하고 필요한 값을 return한다.

Q. Python 함수에 Type Hint를 써야 해?
A. 필수는 아니지만 Agent가 코드를 이해하고 리뷰하기 쉽게 하므로 권장한다.

Q. Python 함수명은 어떻게 짓는 게 좋아?
A. `read_text_file`, `validate_document`, `extract_sections`처럼 동작이 드러나게 작성한다.

Q. Python import는 왜 필요해?
A. pathlib, json, logging, requests 같은 Module 기능을 현재 파일에서 사용하기 위해 필요하다.

Q. pathlib은 어떻게 import해?
A. `from pathlib import Path`를 사용한다.

Q. Python에서 json은 설치해야 해?
A. 아니다. json은 Python 표준 라이브러리이다.

Q. Python에서 requests는 설치해야 해?
A. 그렇다. requests는 외부 패키지이므로 pip로 설치해야 한다.

Q. Python Comment는 언제 써?
A. 파일 덮어쓰기, 삭제, API 호출, 검증 기준처럼 의도를 명확히 해야 하는 부분에 사용한다.

Q. Python Docstring은 언제 써?
A. 재사용 함수, Agent Tool 함수, 검증 함수의 목적과 반환 구조를 설명할 때 사용한다.

Q. Python 들여쓰기는 왜 중요해?
A. Python은 들여쓰기로 코드 Block을 구분하기 때문에 문법적으로 필수이다.

Q. Python 들여쓰기는 몇 칸이 좋아?
A. 일반적으로 공백 4칸을 사용한다.

Q. Python에서 IndentationError는 왜 발생해?
A. 조건문, 반복문, 함수 내부의 들여쓰기가 맞지 않을 때 발생한다.

Q. Python main 함수는 왜 써?
A. 실행 흐름을 명확히 하고 테스트 가능한 구조로 만들기 위해 사용한다.

Q. `if __name__ == "__main__"`는 왜 써?
A. Python 파일이 직접 실행될 때만 main 함수를 실행하기 위해 사용한다.

Q. Python 자동화 스크립트 기본 구조는?
A. import → constant → function → main → entry point 구조를 권장한다.

Q. Python 자동화 코드에서 pathlib을 왜 우선해?
A. Windows와 Linux 경로 차이를 줄이고 파일 처리 기능을 안전하게 사용할 수 있기 때문이다.

Q. Python 파일 읽기에서 encoding은 왜 명시해?
A. 한글 Markdown, CSV, 로그 파일에서 인코딩 오류를 줄이기 위해 UTF-8을 명시한다.

Q. Python 자동화 결과는 어떤 형태가 좋아?
A. Agent가 처리하기 쉽도록 dict 또는 JSON 형태의 구조화된 결과가 좋다.

Q. Python Foundation 단계에서 class가 꼭 필요해?
A. 아니다. 기본 자동화는 함수 중심으로 충분하며 class는 상태와 동작을 묶을 때 사용한다.

Q. Python Foundation에서 가장 중요한 Best Practice는?
A. 의미 있는 이름, 함수 분리, pathlib 사용, encoding 명시, Type Hint, 구조화된 결과 반환이다.
