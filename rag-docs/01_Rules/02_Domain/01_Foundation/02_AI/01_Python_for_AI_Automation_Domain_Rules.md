# Python for AI Automation Domain Rules

---

# 1. Domain Purpose

Python for AI Automation Domain 문서는 AI Agent / Backend Agent / Review Agent용 RAG 문서 제작 규칙이다.

목적:

- Python 기본 문법 이해
- AI Automation Script 작성 지원
- File / Directory 처리 지원
- JSON / CSV / Markdown 처리 지원
- API 호출 자동화 지원
- Data Processing 기초 지원
- RAG 문서 전처리 지원
- Agent Tool Script 작성 지원
- Error Handling / Logging / Testing 기준 제공

우선순위:

1. Python Core Syntax
2. Practical Automation
3. File / Data Processing
4. API Integration
5. Agent Tool Support
6. Code Reliability
7. Maintainability

---

# 2. Scope

포함 범위:

- Python Basic Syntax
- Variable / Data Type
- List / Tuple / Dict / Set
- Condition / Loop
- Function
- Module / Package
- Class / OOP Basics
- Exception Handling
- File I/O
- Path Handling
- JSON / CSV / YAML / Markdown
- HTTP API Request
- Environment Variable
- Logging
- Type Hint
- Dataclass
- Virtual Environment
- Dependency Management
- Script Automation
- CLI Script
- Data Processing
- Pandas Basics
- RAG Document Preprocessing
- Agent Tool Script
- Testing Basics

제외 범위:

- Python Web Framework 심화
- Django / FastAPI 서버 구축 심화
- Machine Learning Algorithm 상세
- Deep Learning Training 상세
- MLOps 운영 상세
- Fine-Tuning 상세
- Model Quantization 상세
- OS Kernel 수준 자동화

---

# 3. Section Priority

## Required

- [개념]
- [핵심]
- [실무]
- [FAQ]

---

## Strongly Recommended

- [Flow]
- [예제]
- [주의]
- [Best Practice]
- [Troubleshooting]
- [Checklist]
- [Comparison]

---

# 4. Python Core Rules

Python 문서는 AI 자동화와 실무 스크립트 작성 중심으로 작성한다.

반드시 포함:

- Python이 왜 AI / Automation에서 많이 사용되는가
- 문법은 짧게, 실무 사용 예제 중심
- 파일 처리, JSON 처리, API 호출과 연결
- Agent Tool Script 작성에 필요한 패턴
- 예외 처리와 로그 기록
- 재사용 가능한 함수 구조

기본 Flow:

```text
Input
→ Python Script
→ Processing
→ Output
→ Logging / Error Handling
```

금지:

- 문법 설명만 장황하게 나열
- 실무 예제 없는 이론 설명
- 불필요한 알고리즘 심화
- AI 자동화 목적과 무관한 문법 확장
- 긴 전체 코드만 제공하고 설명 없음

---

# 5. Python Basic Syntax Rules

Python 기본 문법은 반드시 포함한다.

필수 포함:

- Variable
- Data Type
- Operator
- Condition
- Loop
- Function
- Import
- Comment
- Indentation

예시:

```python
name = "rag-doc"
count = 3

if count > 0:
    print(f"{name}: {count}")
```

반드시 설명:

- Python은 들여쓰기로 Block을 구분
- 변수 선언 시 타입을 명시하지 않아도 됨
- 조건문과 반복문은 자동화 스크립트의 기본
- 함수는 반복 로직을 재사용하기 위한 단위

주의:

- 들여쓰기 오류는 SyntaxError 발생
- 변수명은 의미 있게 작성
- 너무 긴 함수는 분리
- 전역 변수 남용 금지

---

# 6. Data Type Rules

Data Type 문서는 자동화에서 자주 쓰는 자료형 중심으로 작성한다.

필수 포함:

- str
- int
- float
- bool
- None
- list
- tuple
- dict
- set

예시:

```python
config = {
    "model": "qwen2.5",
    "temperature": 0.2,
    "enabled": True
}

files = ["part01.md", "part02.md"]
```

반드시 설명:

- list는 순서 있는 여러 값
- dict는 key-value 구조
- set은 중복 제거에 유용
- None은 값 없음 표현

실무 사용:

- JSON 데이터는 dict / list로 다룸
- 파일 목록은 list로 관리
- 설정값은 dict로 관리
- 중복 제거는 set 사용

---

# 7. String Processing Rules

String Processing은 RAG 문서 전처리에서 매우 중요하다.

필수 포함:

- f-string
- split
- join
- strip
- replace
- startswith / endswith
- in keyword
- regular expression 기초

예시:

```python
title = "  # Python Basics  "
clean_title = title.strip().replace("#", "").strip()
```

반드시 설명:

- Markdown / CSV / Log 처리에서 문자열 조작이 자주 사용됨
- f-string은 문자열 포맷팅 기본 방식
- strip은 공백 제거
- split / join은 텍스트 분리와 병합에 사용

주의:

- 원본 텍스트 훼손 주의
- replace를 과도하게 쓰기 전에 패턴 확인
- 정규식은 필요한 경우만 사용

---

# 8. List / Dict Processing Rules

List와 Dict는 Python 자동화의 핵심이다.

필수 포함:

- list append
- list comprehension
- dict get
- dict update
- items / keys / values
- nested dict
- sorting

예시:

```python
documents = [
    {"title": "Python", "level": "foundation"},
    {"title": "RAG", "level": "ai"}
]

titles = [doc["title"] for doc in documents]
```

반드시 설명:

- API Response는 dict/list 조합인 경우가 많음
- JSON 데이터 처리에 필수
- list comprehension은 간단한 변환에 유용
- dict.get은 KeyError 방지에 유용

주의:

- 중첩 dict 접근 시 None 체크
- 너무 복잡한 comprehension 금지
- 원본 데이터 변경 여부 주의

---

# 9. Function Rules

Function 문서는 재사용 가능한 자동화 로직 중심으로 작성한다.

필수 포함:

- Function Definition
- Parameter
- Return
- Default Parameter
- Keyword Argument
- Type Hint
- Docstring

예시:

```python
def read_text_file(path: str) -> str:
    """Read a UTF-8 text file."""
    with open(path, "r", encoding="utf-8") as file:
        return file.read()
```

반드시 설명:

- 함수는 하나의 책임만 가지는 것이 좋음
- 입력과 출력이 명확해야 함
- Type Hint는 Agent가 코드를 이해하는 데 도움
- Docstring은 함수 목적 설명에 유용

주의:

- 너무 많은 역할을 가진 함수 금지
- 반환값이 불명확한 함수 금지
- 예외 발생 가능성을 고려

---

# 10. Module / Package Rules

Module / Package 문서는 파일 분리와 재사용 중심으로 작성한다.

필수 포함:

- import
- from import
- module
- package
- `__init__.py`
- relative import 기본
- script entry point

예시:

```python
from pathlib import Path
import json
```

반드시 설명:

- Module은 Python 파일 단위
- Package는 여러 Module을 묶는 구조
- import는 코드 재사용을 위한 기본
- 자동화 프로젝트가 커지면 기능별 파일 분리 필요

권장 구조:

```text
python_ai_automation
├ main.py
├ config.py
├ file_utils.py
├ api_client.py
├ processors
│  └ markdown_processor.py
└ tests
```

---

# 11. File I/O Rules

File I/O는 Python AI Automation 문서의 핵심이다.

필수 포함:

- open
- read
- write
- append
- encoding
- with statement
- pathlib
- file exists check
- directory create

예시:

```python
from pathlib import Path

path = Path("docs/example.md")
text = path.read_text(encoding="utf-8")
```

반드시 설명:

- `with`는 파일 자원을 안전하게 닫기 위해 사용
- UTF-8 encoding 명시 권장
- pathlib은 경로 처리를 객체지향적으로 지원
- 파일 존재 여부 확인 후 처리

주의:

- 파일 덮어쓰기 주의
- 상대경로 / 절대경로 혼동 주의
- 한글 파일은 encoding 문제 주의
- 대용량 파일은 한 번에 읽지 않는 방식 고려

---

# 12. Path Handling Rules

Path Handling 문서는 OS 독립적인 경로 처리 중심으로 작성한다.

필수 포함:

- pathlib.Path
- exists
- is_file
- is_dir
- mkdir
- glob
- rglob
- suffix
- stem
- parent

예시:

```python
from pathlib import Path

base_dir = Path("RAG_Documents")
md_files = list(base_dir.rglob("*.md"))
```

반드시 설명:

- pathlib 사용을 우선 권장
- Windows / Linux 경로 차이를 줄일 수 있음
- RAG 문서 일괄 처리에 rglob 사용 가능

주의:

- 문자열로 경로를 직접 이어붙이는 방식 지양
- 파일명과 확장자 구분
- 존재하지 않는 폴더 처리 필요

---

# 13. JSON / CSV / YAML Rules

Data File 문서는 AI 자동화에서 자주 쓰는 파일 형식 중심으로 작성한다.

필수 포함:

- json load / dump
- csv DictReader / DictWriter
- yaml safe_load / safe_dump
- encoding
- schema validation 기초

JSON 예시:

```python
import json
from pathlib import Path

data = {"name": "agent", "enabled": True}
Path("config.json").write_text(
    json.dumps(data, ensure_ascii=False, indent=2),
    encoding="utf-8"
)
```

반드시 설명:

- JSON은 API와 설정 파일에서 자주 사용
- CSV는 표 형태 데이터 처리에 사용
- YAML은 설정 파일에서 자주 사용
- ensure_ascii=False는 한글 저장에 유용

주의:

- 외부 YAML 처리 시 안전한 loader 사용
- CSV header 누락 주의
- JSON key 존재 여부 확인

---

# 14. Markdown Processing Rules

Markdown Processing은 RAG 문서 제작과 직접 연결된다.

필수 포함:

- Markdown Header Parsing
- Code Block Detection
- Frontmatter
- Section Split
- Chunk Preparation
- Retrieval Queries Block Check

기본 Flow:

```text
Markdown File
→ Read Text
→ Split by Header
→ Extract Sections
→ Validate Required Blocks
→ Save Processed Result
```

반드시 설명:

- RAG 문서는 Markdown 기준으로 관리
- Header는 Chunk 경계로 사용 가능
- Code Block은 깨지지 않게 처리
- Retrieval Queries 존재 여부를 검사할 수 있음

주의:

- Code Block 내부의 `#`를 Header로 오인하지 말 것
- 문서 구조를 임의로 깨지 않도록 주의
- 원본 파일 백업 후 처리 권장

---

# 15. HTTP API Request Rules

HTTP API Request 문서는 LLM API / 외부 API 자동화 중심으로 작성한다.

필수 포함:

- requests
- httpx
- GET
- POST
- Header
- Query Parameter
- JSON Body
- Timeout
- Retry
- Status Code
- Error Handling

예시:

```python
import requests

response = requests.get(
    "https://api.example.com/items",
    timeout=10
)

response.raise_for_status()
data = response.json()
```

반드시 설명:

- 외부 API 호출에는 Timeout 필수
- Status Code 확인 필요
- JSON Response는 dict/list로 처리
- API Key는 환경변수로 관리

주의:

- Timeout 없는 요청 금지
- API Key 코드 하드코딩 금지
- 무제한 Retry 금지
- 민감정보 로그 출력 금지

---

# 16. Environment Variable Rules

Environment Variable 문서는 API Key / Config 관리 중심으로 작성한다.

필수 포함:

- os.environ
- dotenv
- API Key
- Config
- Secret Management
- `.env`
- `.gitignore`

예시:

```python
import os

api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is required")
```

반드시 설명:

- API Key는 코드에 직접 작성하지 않음
- 환경별 설정은 환경변수로 분리
- `.env` 파일은 Git에 올리지 않음
- 필요한 환경변수 누락 시 명확한 에러 출력

주의:

- Secret을 로그에 출력 금지
- `.env` 커밋 금지
- 기본값 설정 시 보안 위험 고려

---

# 17. Exception Handling Rules

Exception Handling은 자동화 스크립트 안정성에 필수이다.

필수 포함:

- try / except
- finally
- raise
- custom exception
- specific exception
- error message
- retryable error

예시:

```python
try:
    data = path.read_text(encoding="utf-8")
except FileNotFoundError:
    raise FileNotFoundError(f"File not found: {path}")
```

반드시 설명:

- 예상 가능한 예외는 구체적으로 처리
- 모든 예외를 무조건 무시하지 않음
- 실패 원인을 알 수 있는 메시지 필요
- 자동화 작업은 실패 지점을 명확히 기록해야 함

주의:

- bare except 금지
- except 후 pass 금지
- 예외를 삼키고 정상 처리처럼 보이게 하지 말 것
- 재시도 가능한 오류와 불가능한 오류 구분

---

# 18. Logging Rules

Logging 문서는 print보다 logging 사용을 권장한다.

필수 포함:

- logging
- log level
- format
- file logging
- console logging
- error logging

예시:

```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Processing started")
```

반드시 설명:

- print는 간단한 확인용
- 운영성 자동화 스크립트는 logging 사용
- INFO / WARNING / ERROR 레벨 구분
- 오류 발생 시 context 포함

주의:

- API Key / Token 로그 출력 금지
- 너무 많은 로그는 가독성 저하
- 에러 로그에는 원인 파악 정보 포함

---

# 19. Type Hint Rules

Type Hint는 Agent 코드 생성과 리뷰에 매우 중요하다.

필수 포함:

- str / int / bool
- list
- dict
- Optional
- Union
- Literal
- Callable 기초
- TypedDict
- dataclass

예시:

```python
from typing import Optional

def find_file(name: str) -> Optional[str]:
    ...
```

반드시 설명:

- Type Hint는 런타임 강제는 아니지만 코드 이해와 검증에 도움
- 함수 입력/출력 타입을 명확히 표현
- Agent가 코드 구조를 파악하는 데 유리
- 복잡한 dict는 TypedDict나 dataclass 고려

주의:

- 타입 힌트와 실제 반환값 불일치 주의
- 너무 복잡한 타입 선언은 가독성 저하
- None 가능성 명시

---

# 20. Dataclass Rules

Dataclass는 구조화된 데이터 표현에 유용하다.

필수 포함:

- dataclass
- field
- default
- default_factory
- asdict
- frozen

예시:

```python
from dataclasses import dataclass

@dataclass
class DocumentMeta:
    title: str
    path: str
    domain: str
```

반드시 설명:

- dataclass는 단순 데이터 객체에 적합
- 설정값, 메타데이터, 처리 결과 표현에 유용
- dict보다 구조가 명확함
- 불변 데이터는 frozen 고려

주의:

- 복잡한 비즈니스 로직을 dataclass에 과도하게 넣지 않음
- mutable default는 default_factory 사용

---

# 21. Class / OOP Basics Rules

Python OOP는 자동화 코드 구조화 중심으로 설명한다.

필수 포함:

- class
- instance
- method
- `__init__`
- property
- composition
- inheritance basics

예시:

```python
class MarkdownProcessor:
    def __init__(self, base_dir: str):
        self.base_dir = base_dir

    def process(self) -> list[str]:
        ...
```

반드시 설명:

- class는 상태와 동작을 묶을 때 사용
- 단순 스크립트는 함수만으로 충분할 수 있음
- Processor / Client / Service 같은 구조화에 유용
- 상속보다 조합을 우선 고려

주의:

- 모든 코드를 class로 만들 필요 없음
- 불필요한 OOP 남용 금지
- 책임이 너무 많은 class는 분리

---

# 22. Virtual Environment Rules

Python 프로젝트는 가상환경 기준으로 설명한다.

필수 포함:

- venv
- pip
- requirements.txt
- pyproject.toml 기초
- dependency version
- activate / deactivate

예시:

```bash
python -m venv .venv
source .venv/bin/activate
pip install requests
pip freeze > requirements.txt
```

Windows 예시:

```bash
.venv\Scripts\activate
```

반드시 설명:

- 프로젝트별 의존성 격리를 위해 venv 사용
- requirements.txt로 패키지 목록 관리
- OS별 activate 명령이 다름
- `.venv`는 Git에 올리지 않음

주의:

- 전역 Python 환경에 무분별한 설치 금지
- 패키지 버전 충돌 주의
- requirements.txt 갱신 누락 주의

---

# 23. Dependency Management Rules

Dependency Management 문서는 재현 가능한 실행 환경 중심으로 작성한다.

필수 포함:

- pip
- requirements.txt
- pyproject.toml
- version pinning
- dependency update
- security update

반드시 설명:

- 의존성 버전은 재현성에 중요
- 개발 환경과 실행 환경의 패키지 버전 차이 주의
- 주요 자동화 스크립트는 requirements.txt 포함 권장
- 불필요한 패키지 추가 금지

주의:

- 최신 버전만 무조건 사용 금지
- 사용하지 않는 패키지 방치 금지
- 보안 취약 패키지 업데이트 고려

---

# 24. CLI Script Rules

CLI Script는 반복 작업 자동화에 적합하다.

필수 포함:

- argparse
- command line argument
- option
- exit code
- help message

예시:

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True)
parser.add_argument("--output", required=True)

args = parser.parse_args()
```

반드시 설명:

- CLI는 수동 반복 작업 자동화에 유용
- 입력/출력 경로를 인자로 받게 설계
- help 메시지를 제공
- 실패 시 적절한 exit code 반환

주의:

- 하드코딩된 경로 남용 금지
- 인자 검증 필요
- 사용자 실수 시 명확한 에러 메시지 제공

---

# 25. Data Processing Rules

Data Processing 문서는 AI / RAG 자동화에서 필요한 기초 처리 중심으로 작성한다.

필수 포함:

- list processing
- dict processing
- filtering
- mapping
- sorting
- grouping
- deduplication
- pandas basics

예시:

```python
filtered_docs = [
    doc for doc in documents
    if doc["domain"] == "backend"
]
```

반드시 설명:

- 데이터 처리는 자동화 스크립트의 핵심
- 작은 데이터는 list/dict로 충분
- 표 형태 데이터는 pandas 사용 가능
- 중복 제거와 정렬 기준을 명확히 함

주의:

- 대용량 데이터를 메모리에 한 번에 올리지 않도록 주의
- 원본 데이터 변경 여부 확인
- 결측값 / 누락 Key 처리 필요

---

# 26. Pandas Basics Rules

Pandas는 CSV / Excel / 분석형 데이터 처리 기초만 포함한다.

필수 포함:

- DataFrame
- read_csv
- to_csv
- head
- info
- columns
- filter
- groupby
- sort_values
- fillna
- dropna

예시:

```python
import pandas as pd

df = pd.read_csv("data.csv")
result = df.groupby("category")["value"].mean()
```

반드시 설명:

- pandas는 표 형태 데이터 처리에 적합
- RAG 문서 메타데이터 관리에도 활용 가능
- 결측값 처리 기준을 명확히 함
- 파일 저장 시 index 여부 확인

주의:

- 대용량 CSV는 chunk 처리 고려
- 원본 컬럼명 변경 주의
- 인코딩 문제 확인
- index 저장 여부 확인

---

# 27. RAG Document Automation Rules

RAG 문서 자동화는 이 Domain의 핵심 목적 중 하나이다.

필수 포함:

- Markdown file scan
- Section validation
- Required section check
- Retrieval Queries check
- File naming validation
- Metadata extraction
- Chunk preparation

기본 Flow:

```text
RAG Folder
→ Scan Markdown Files
→ Validate Naming
→ Validate Required Sections
→ Extract Metadata
→ Generate Report
```

반드시 설명:

- Python으로 RAG 문서 품질 검사 가능
- 필수 섹션 누락 여부 확인
- 파일명 규칙 검사 가능
- 문서 길이 / Chunk 크기 점검 가능
- 자동 리포트 생성 가능

주의:

- 원본 문서 자동 수정 전 백업
- Code Block 내부 Header 오탐 주의
- 자동화 결과는 사람이 최종 확인

---

# 28. Agent Tool Script Rules

Python 문서는 Agent가 사용할 Tool Script 제작을 지원해야 한다.

필수 포함:

- Tool Input
- Tool Output
- JSON Schema 기초
- Validation
- Error Result
- Deterministic Output
- Idempotency

기본 Flow:

```text
Agent Request
→ Python Tool
→ Validate Input
→ Execute Task
→ Return Structured Output
```

반드시 설명:

- Agent Tool은 입력과 출력이 명확해야 함
- JSON 형태 결과가 Agent 처리에 유리
- 실패 시 에러 메시지를 구조화
- 같은 입력에 같은 결과를 반환하는 것이 좋음

주의:

- Tool이 임의로 파일 삭제하지 않도록 보호
- 위험 작업은 dry-run 지원 고려
- 민감정보 노출 금지
- 예외 발생 시 구조화된 실패 결과 반환

---

# 29. Testing Rules

Python 자동화 문서에는 테스트 기초를 포함한다.

필수 포함:

- assert
- pytest basics
- test function
- fixture basics
- temporary file test
- mocking basics

예시:

```python
def test_clean_title():
    assert clean_title("# Python") == "Python"
```

반드시 설명:

- 자동화 스크립트도 테스트 필요
- 파일 처리 함수는 임시 파일로 테스트 가능
- API 호출은 Mocking 고려
- 핵심 전처리 로직은 테스트 대상

주의:

- 실제 파일을 삭제/수정하는 테스트 주의
- 외부 API를 테스트마다 직접 호출하지 말 것
- 테스트 데이터와 실제 데이터 분리

---

# 30. Code Style Rules

Code Style은 Agent가 생성한 Python 코드의 품질을 높이기 위해 포함한다.

필수 포함:

- readable naming
- small function
- type hint
- docstring
- formatting
- linting basics
- black / ruff 기초

Best Practice:

- 함수명은 동작을 표현
- 변수명은 의미 있게 작성
- 하나의 함수는 하나의 책임
- 중복 코드는 함수화
- 복잡한 조건문은 분리
- Type Hint 사용
- 예외 메시지 명확히 작성

주의:

- 한 파일에 모든 코드 몰아넣기 금지
- 의미 없는 변수명 금지
- 과도한 축약어 금지
- 복잡한 one-liner 남용 금지

---

# 31. Security Rules

Python 자동화에서도 보안 기준을 포함한다.

필수 포함:

- API Key Protection
- Environment Variable
- Secret Masking
- Safe File Handling
- Path Traversal 주의
- Input Validation
- Dependency Security

주의:

- API Key 하드코딩 금지
- Secret 로그 출력 금지
- 사용자 입력 경로 그대로 사용 금지
- 파일 삭제/덮어쓰기 전 확인
- 외부 입력으로 shell command 실행 주의
- pickle 사용 주의

---

# 32. Troubleshooting Rules

반드시 포함 추천.

형식:

```md
문제:

원인:

해결:
```

---

## ModuleNotFoundError

문제:

- 설치한 패키지를 찾지 못함

원인:

- 가상환경 미활성화
- 다른 Python Interpreter 사용
- 패키지 미설치

해결:

- venv 활성화 확인
- `python -m pip install package` 사용
- IDE Interpreter 확인

---

## UnicodeDecodeError

문제:

- 파일 읽기 중 인코딩 오류 발생

원인:

- UTF-8이 아닌 파일을 UTF-8로 읽음
- 한글 CSV 인코딩 불일치

해결:

- encoding 확인
- `encoding="utf-8"` 또는 `encoding="cp949"` 검토
- 파일 저장 인코딩 통일

---

## FileNotFoundError

문제:

- 파일 경로를 찾지 못함

원인:

- 상대경로 기준 위치 착각
- 파일명 오타
- 작업 디렉터리 다름

해결:

- pathlib로 절대경로 확인
- `Path.cwd()` 출력
- 파일 존재 여부 검사

---

## KeyError

문제:

- dict에서 존재하지 않는 key 접근

원인:

- API Response 구조 변경
- JSON 필드 누락
- 오타

해결:

- `dict.get()` 사용
- 필수 key 검증
- Response Schema 확인

---

## API Timeout

문제:

- 외부 API 호출이 오래 걸리거나 실패함

원인:

- Timeout 미설정
- 네트워크 지연
- API 서버 장애

해결:

- Timeout 설정
- 제한적 Retry 적용
- 실패 로그 기록
- 사용자에게 실패 원인 반환

---

# 33. Best Practice Rules

Best Practice:

- Python 기본 문법은 실무 예제와 연결
- pathlib 우선 사용
- 파일 처리 시 encoding 명시
- API 요청에는 timeout 설정
- API Key는 환경변수로 관리
- 반복 로직은 함수화
- 입력과 출력 타입 명시
- 자동화 스크립트는 로그 남기기
- 실패 시 명확한 에러 메시지 제공
- 원본 파일 수정 전 백업 고려
- Agent Tool Output은 JSON 형태 권장
- 테스트 가능한 순수 함수로 분리

---

# 34. Comparison Rules

Python 문서는 비교 기준을 포함한다.

필수 비교 대상:

- list vs tuple
- dict vs dataclass
- print vs logging
- os.path vs pathlib
- requests vs httpx
- JSON vs CSV vs YAML
- Function vs Class
- Script vs Package
- Sync API Call vs Async API Call
- Manual Work vs Python Automation

예시:

| 비교      | print          | logging             |
| --------- | -------------- | ------------------- |
| 목적      | 간단한 출력    | 운영성 로그         |
| 레벨      | 없음           | INFO / WARN / ERROR |
| 파일 저장 | 직접 구현 필요 | 지원 가능           |
| 적합      | 임시 확인      | 자동화 스크립트     |

---

# 35. Checklist Rules

Python 문서에는 Checklist를 포함할 수 있다.

예시:

```md
### [Checklist]

- [ ] Python 기본 문법을 포함했는가?
- [ ] 파일 처리 예제를 포함했는가?
- [ ] JSON / CSV 처리 예제를 포함했는가?
- [ ] API 호출에 timeout을 설정했는가?
- [ ] API Key를 환경변수로 관리했는가?
- [ ] 예외 처리를 포함했는가?
- [ ] logging을 포함했는가?
- [ ] Type Hint를 포함했는가?
- [ ] RAG 문서 자동화 예제를 포함했는가?
- [ ] Agent Tool Script 기준을 포함했는가?
```

---

# 36. Retrieval Optimization Rules

강조 대상 키워드:

- Python
- Python Basic Syntax
- Python for AI Automation
- AI Automation
- Agent Tool Script
- File I/O
- pathlib
- JSON Processing
- CSV Processing
- Markdown Processing
- API Request
- requests
- httpx
- Environment Variable
- dotenv
- Exception Handling
- Logging
- Type Hint
- Dataclass
- Virtual Environment
- venv
- requirements.txt
- CLI Script
- argparse
- Data Processing
- pandas
- RAG Document Automation
- Markdown Section Validation
- Retrieval Queries Check
- Python Testing
- pytest

키워드 반복 허용.

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

예:

- Python 기본 문법 뭐부터 알아야 해?
- Python으로 파일 읽고 쓰는 방법은?
- Python에서 JSON 처리 어떻게 해?
- Python에서 API 호출 어떻게 해?
- API Key는 Python에서 어떻게 관리해?
- pathlib은 왜 써?
- Python 자동화 스크립트 구조는 어떻게 잡아?
- RAG 문서 검사를 Python으로 할 수 있어?
- Agent Tool Script는 어떻게 만들어?
- Python에서 예외 처리는 어떻게 해?
- print랑 logging 차이는?
- venv는 왜 써?

---

# 37. Version Rules

기준:

- Python 3.11+
- Python 3.12 권장
- Modern Python
- pathlib
- type hint
- dataclass
- requests / httpx
- pandas basics
- pytest basics
- AI Automation Script 기준

Legacy 제외:

- Python 2.x
- 오래된 `%` 문자열 포맷팅 중심 설명
- os.path만 사용하는 구식 경로 처리 중심
- 무분별한 global script 방식
- API Key 하드코딩 예제

---

# 38. Common Mistakes

자주 발생:

- 들여쓰기 오류
- 가상환경 미사용
- API Key 하드코딩
- Timeout 없는 API 요청
- bare except 사용
- 예외를 pass로 무시
- 파일 encoding 누락
- 상대경로 혼동
- JSON key 존재 여부 확인 안 함
- print만 사용하고 logging 없음
- Type Hint 없음
- 하나의 긴 script에 모든 로직 작성
- 원본 파일을 백업 없이 자동 수정
- pandas 사용 후 index 저장 실수
- 테스트 없이 자동화 스크립트 실행

---

# 39. Final Goal

Python for AI Automation RAG 문서는 Agent가 아래를 수행 가능해야 한다.

- Python 기본 문법 이해
- 자동화 스크립트 작성
- 파일 / 폴더 처리
- JSON / CSV / Markdown 처리
- API 호출 코드 작성
- API Key / 환경변수 관리
- 예외 처리 / 로깅 적용
- Type Hint 기반 코드 생성
- RAG 문서 전처리
- RAG 문서 구조 검증
- Agent Tool Script 작성
- Python 코드 리뷰
- 자동화 작업 Troubleshooting

문서 품질이 AI Automation과 Agent Tool 품질을 결정한다.

---

# Retrieval Queries

### [FAQ]

Q. Python for AI Automation 문서에는 Python 기본 문법도 포함해야 해?

A.
포함해야 한다. 변수, 자료형, 조건문, 반복문, 함수, 파일 처리 같은 기본 문법은 AI 자동화 스크립트 작성의 기반이다.

Q. Python 기본 문법은 어디까지 다루면 돼?

A.
Variable, Data Type, Condition, Loop, Function, Module, File I/O, Exception Handling까지는 Foundation 단계에서 다룬다.

Q. Python에서 list와 dict는 왜 중요해?

A.
API Response, JSON 데이터, 문서 메타데이터가 대부분 list와 dict 구조로 처리되기 때문이다.

Q. Python으로 파일을 읽고 쓰는 방법은?

A.
`pathlib.Path`의 `read_text`, `write_text` 또는 `open`과 `with` 구문을 사용한다. 한글 문서는 UTF-8 encoding을 명시하는 것이 좋다.

Q. pathlib은 왜 써?

A.
Windows와 Linux 경로 차이를 줄이고, 파일 존재 확인, 확장자 확인, 폴더 탐색을 더 안전하게 처리할 수 있기 때문이다.

Q. Python에서 JSON 처리는 어떻게 해?

A.
`json.load`, `json.loads`, `json.dump`, `json.dumps`를 사용한다. 한글 저장 시 `ensure_ascii=False`를 고려한다.

Q. Python에서 CSV 처리는 어떻게 해?

A.
간단한 CSV는 `csv` 모듈을 사용하고, 표 형태 데이터 분석이나 가공은 pandas를 사용할 수 있다.

Q. Python에서 API 호출은 어떻게 해?

A.
`requests` 또는 `httpx`를 사용한다. API 호출에는 반드시 timeout을 설정하고 status code를 확인해야 한다.

Q. API Key는 Python 코드에 직접 넣어도 돼?

A.
안 된다. API Key는 환경변수나 `.env`로 관리하고 Git에 올리지 않아야 한다.

Q. Python에서 예외 처리는 어떻게 해?

A.
`try / except`를 사용하되, 가능한 구체적인 예외를 처리하고 실패 원인을 알 수 있는 메시지를 남긴다.

Q. bare except는 왜 피해야 해?

A.
모든 오류를 무분별하게 잡아 실제 문제를 숨길 수 있기 때문이다.

Q. print와 logging 차이는?

A.
print는 임시 출력용이고, logging은 레벨, 포맷, 파일 저장이 가능한 운영성 로그 기록 방식이다.

Q. Type Hint는 왜 필요해?

A.
함수 입력과 출력이 명확해지고, Agent가 코드를 이해하고 리뷰하기 쉬워진다.

Q. dataclass는 언제 써?

A.
문서 메타데이터, 설정값, 처리 결과처럼 구조가 정해진 데이터를 표현할 때 사용한다.

Q. venv는 왜 써?

A.
프로젝트별 Python 패키지 의존성을 분리해 버전 충돌을 줄이기 위해 사용한다.

Q. requirements.txt는 왜 필요해?

A.
자동화 스크립트를 다른 환경에서 재현 가능하게 실행하기 위해 필요한 패키지 목록을 기록한다.

Q. Python으로 RAG 문서 검사를 할 수 있어?

A.
가능하다. Markdown 파일을 스캔하고 필수 섹션, 파일명 규칙, Retrieval Queries 존재 여부를 검사할 수 있다.

Q. Agent Tool Script는 어떤 구조가 좋아?

A.
입력 검증, 작업 실행, 구조화된 JSON 출력, 예외 처리, 로그 기록이 분리된 구조가 좋다.

Q. Python 자동화 스크립트에서 가장 주의할 점은?

A.
파일 삭제/덮어쓰기, API Key 노출, Timeout 없는 API 호출, 예외 무시, 원본 문서 훼손을 주의해야 한다.

Q. Python 자동화 코드는 테스트해야 해?

A.
해야 한다. 파일 처리, 문자열 전처리, JSON 변환, API 응답 처리 같은 핵심 로직은 pytest로 검증하는 것이 좋다.
