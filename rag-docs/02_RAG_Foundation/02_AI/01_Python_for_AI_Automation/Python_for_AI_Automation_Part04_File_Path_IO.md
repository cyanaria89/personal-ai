# Python for AI Automation Part04 - File Path I/O

---

# 1. File I/O Overview

## 1.1 File I/O Role

### [개념]

File I/O는 Python에서 파일을 읽고 쓰는 작업이다.

Python for AI Automation에서 File I/O는 RAG 문서 처리, Markdown 파일 검사, JSON 설정 저장, CSV 메타데이터 생성, 로그 파일 기록, Agent Tool Result 저장의 핵심 기능이다.

기본 Flow:

```text
File Path
→ Open / Read / Write
→ Process Text or Data
→ Save Result
→ Handle Error
```

---

### [핵심]

- File I/O는 자동화 스크립트의 기본 작업이다.
- Markdown, JSON, CSV, YAML, Log 파일 처리에 사용된다.
- 파일 읽기에는 encoding 명시를 권장한다.
- 한글 문서는 UTF-8 기준으로 처리한다.
- `with` 구문은 파일 자원을 안전하게 닫기 위해 사용한다.
- Modern Python에서는 `pathlib.Path` 사용을 우선한다.
- 파일 덮어쓰기 전 원본 백업 또는 검증 로직을 고려한다.

---

### [실무]

2026 실무 기준 Python 자동화에서는 `open()`보다 `pathlib.Path` 기반 File I/O를 우선 사용한다.

권장:

```python
from pathlib import Path

path = Path("docs/example.md")
text = path.read_text(encoding="utf-8")
```

저장:

```python
from pathlib import Path

path = Path("reports/result.md")
path.write_text("# Report\n\n검증 완료", encoding="utf-8")
```

사용 영역:

- RAG 문서 일괄 읽기
- Markdown 필수 섹션 검사
- Retrieval Queries 존재 여부 확인
- 검증 결과 리포트 저장
- JSON Config 저장
- CSV Metadata 저장
- 자동화 로그 저장

---

### [FAQ]

Q. File I/O는 Python 자동화에서 왜 중요해?

A. RAG 문서, 설정 파일, 검증 결과, 로그, 메타데이터를 읽고 저장하는 기본 작업이기 때문이다.

Q. Python에서 파일 읽기 시 encoding을 명시해야 해?

A. 권장한다. 한글 Markdown, CSV, 로그 파일에서 인코딩 오류를 줄이기 위해 `encoding="utf-8"`을 명시한다.

Q. Python에서 파일 처리는 open과 pathlib 중 무엇을 우선해?

A. Modern Python에서는 `pathlib.Path`를 우선 권장한다.

Q. 파일 덮어쓰기는 바로 해도 돼?

A. 위험하다. 원본 백업, dry-run, 검증 통과 후 저장 같은 보호 로직을 고려해야 한다.

---

# 2. open and with Statement

## 2.1 open Basics

### [개념]

`open()`은 Python에서 파일을 열기 위한 기본 함수이다.

파일을 열 때 mode를 지정해 읽기, 쓰기, 추가 작업을 수행한다.

```python
with open("docs/example.md", "r", encoding="utf-8") as file:
    text = file.read()
```

---

### [핵심]

- `open()`은 파일을 연다.
- `"r"`은 읽기 모드이다.
- `"w"`는 쓰기 모드이다.
- `"a"`는 추가 모드이다.
- `encoding="utf-8"`을 명시한다.
- `with`를 사용하면 파일이 자동으로 닫힌다.
- 파일을 직접 열고 닫는 방식보다 `with` 구문이 안전하다.

---

### [실무]

파일 읽기:

```python
with open("docs/example.md", "r", encoding="utf-8") as file:
    text = file.read()
```

파일 쓰기:

```python
with open("reports/result.md", "w", encoding="utf-8") as file:
    file.write("# Validation Report\n")
```

파일 추가:

```python
with open("logs/process.log", "a", encoding="utf-8") as file:
    file.write("Processing completed\n")
```

권장:

```text
Read File
→ Process
→ Validate
→ Write Result
```

---

### [FAQ]

Q. open 함수는 무엇을 해?

A. 파일을 읽거나 쓰기 위해 파일을 여는 Python 기본 함수이다.

Q. with 구문은 왜 사용해?

A. 파일 작업이 끝난 뒤 자동으로 파일을 닫아 자원 누수를 줄이기 위해 사용한다.

Q. 파일 읽기 모드는 무엇이야?

A. `"r"` 모드이다.

Q. 파일 쓰기 모드는 무엇이야?

A. `"w"` 모드이다. 기존 파일 내용이 덮어쓰기 될 수 있으므로 주의해야 한다.

Q. 파일 추가 모드는 무엇이야?

A. `"a"` 모드이다. 기존 내용 뒤에 새 내용을 추가한다.

---

## 2.2 File Mode

### [개념]

File Mode는 파일을 어떤 방식으로 열지 지정하는 값이다.

Python File I/O에서 mode를 잘못 지정하면 파일을 읽지 못하거나 기존 파일을 덮어쓸 수 있다.

---

### [핵심]

| Mode | 의미          | 주의                |
| ---- | ------------- | ------------------- |
| `r`  | 읽기          | 파일이 없으면 오류  |
| `w`  | 쓰기          | 기존 내용 덮어쓰기  |
| `a`  | 추가          | 기존 내용 뒤에 추가 |
| `x`  | 새 파일 생성  | 파일이 있으면 오류  |
| `rb` | 바이너리 읽기 | 이미지, PDF 등      |
| `wb` | 바이너리 쓰기 | 바이너리 저장       |

---

### [실무]

읽기 모드:

```python
with open("docs/input.md", "r", encoding="utf-8") as file:
    text = file.read()
```

쓰기 모드:

```python
with open("reports/output.md", "w", encoding="utf-8") as file:
    file.write("result")
```

추가 모드:

```python
with open("logs/app.log", "a", encoding="utf-8") as file:
    file.write("new log\n")
```

새 파일 생성 모드:

```python
with open("reports/new_report.md", "x", encoding="utf-8") as file:
    file.write("new report")
```

---

### [FAQ]

Q. `w` 모드는 왜 조심해야 해?

A. 기존 파일 내용이 즉시 덮어쓰기 되기 때문이다.

Q. 파일이 없을 때만 새로 만들려면 어떤 모드를 써?

A. `x` 모드를 사용한다.

Q. 로그 파일에는 어떤 모드를 써?

A. 기존 로그 뒤에 추가하는 `a` 모드를 자주 사용한다.

Q. 이미지 파일이나 PDF는 어떤 모드를 써?

A. 바이너리 모드인 `rb`, `wb`를 사용한다.

---

# 3. pathlib Path Handling

## 3.1 pathlib Overview

### [개념]

`pathlib`은 Python에서 파일 경로를 객체로 다루는 표준 라이브러리이다.

`Path` 객체를 사용하면 Windows, Linux, macOS 경로 차이를 줄이고 파일 탐색, 존재 확인, 읽기, 쓰기 작업을 안전하게 처리할 수 있다.

```python
from pathlib import Path

path = Path("docs/example.md")
```

---

### [핵심]

- `pathlib`은 Modern Python 경로 처리 기본 방식이다.
- `Path`는 파일 경로를 객체로 표현한다.
- 문자열 결합보다 안전하다.
- Windows와 Linux 경로 차이를 줄인다.
- File I/O 기능도 함께 제공한다.
- RAG 문서 폴더 스캔에 `rglob()`를 사용할 수 있다.

---

### [실무]

권장 방식:

```python
from pathlib import Path

base_dir = Path("RAG_Documents")
file_path = base_dir / "Python_for_AI_Automation_Part04_File_Path_IO.md"
```

비권장 방식:

```python
base_dir = "RAG_Documents"
file_path = base_dir + "/" + "Python_for_AI_Automation_Part04_File_Path_IO.md"
```

파일 읽기:

```python
text = file_path.read_text(encoding="utf-8")
```

파일 쓰기:

```python
file_path.write_text("content", encoding="utf-8")
```

---

### [FAQ]

Q. pathlib은 왜 사용해?

A. OS별 경로 차이를 줄이고 파일 존재 확인, 폴더 생성, 파일 탐색을 안전하게 처리할 수 있기 때문이다.

Q. Path 객체는 문자열이야?

A. 아니다. 파일 경로를 표현하는 객체이다.

Q. Path와 문자열을 합칠 때 `+`를 써도 돼?

A. 권장하지 않는다. `base_dir / "file.md"` 형태를 사용한다.

Q. pathlib은 설치해야 해?

A. 아니다. Python 표준 라이브러리이다.

---

## 3.2 Path Properties

### [개념]

Path Properties는 파일 경로에서 파일명, 확장자, 부모 폴더, 이름 일부를 추출하는 기능이다.

RAG 문서 자동화에서는 파일명 규칙 검사와 메타데이터 추출에 자주 사용한다.

---

### [핵심]

| 속성             | 의미                   |
| ---------------- | ---------------------- |
| `path.name`      | 파일명 전체            |
| `path.stem`      | 확장자를 제외한 파일명 |
| `path.suffix`    | 확장자                 |
| `path.parent`    | 부모 폴더              |
| `path.parts`     | 경로 구성 요소         |
| `path.exists()`  | 존재 여부              |
| `path.is_file()` | 파일 여부              |
| `path.is_dir()`  | 폴더 여부              |

---

### [실무]

파일명 정보 추출:

```python
from pathlib import Path

path = Path("docs/Python_for_AI_Automation_Part04_File_Path_IO.md")

print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
```

파일 확장자 검사:

```python
if path.suffix == ".md":
    print("Markdown file")
```

메타데이터 생성:

```python
metadata = {
    "file_name": path.name,
    "document_id": path.stem,
    "extension": path.suffix,
    "directory": str(path.parent),
}
```

---

### [FAQ]

Q. path.name은 무엇을 반환해?

A. 확장자를 포함한 파일명 전체를 반환한다.

Q. path.stem은 무엇을 반환해?

A. 확장자를 제외한 파일명을 반환한다.

Q. path.suffix는 무엇을 반환해?

A. 파일 확장자를 반환한다.

Q. path.parent는 무엇을 반환해?

A. 해당 파일의 부모 폴더 경로를 반환한다.

---

## 3.3 exists, is_file, is_dir

### [개념]

`exists`, `is_file`, `is_dir`은 경로가 존재하는지, 파일인지, 폴더인지 확인하는 Path 메서드이다.

자동화 스크립트는 파일이나 폴더가 없을 때 명확한 오류를 반환해야 한다.

---

### [핵심]

- `exists()`는 경로 존재 여부를 확인한다.
- `is_file()`은 파일 여부를 확인한다.
- `is_dir()`은 폴더 여부를 확인한다.
- 파일 읽기 전 존재 여부 검사를 권장한다.
- 폴더 스캔 전 폴더 여부 검사를 권장한다.
- 잘못된 경로는 명확한 예외 메시지로 처리한다.

---

### [실무]

파일 존재 확인:

```python
from pathlib import Path

path = Path("docs/example.md")

if not path.exists():
    raise FileNotFoundError(f"File not found: {path}")
```

파일 여부 확인:

```python
if not path.is_file():
    raise ValueError(f"Path is not a file: {path}")
```

폴더 여부 확인:

```python
base_dir = Path("docs")

if not base_dir.is_dir():
    raise NotADirectoryError(f"Directory not found: {base_dir}")
```

검증 함수:

```python
from pathlib import Path

def validate_input_file(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    if not path.is_file():
        raise ValueError(f"Path is not a file: {path}")
```

---

### [FAQ]

Q. 파일 읽기 전에 exists를 확인해야 해?

A. 권장한다. 파일이 없을 때 명확한 오류 메시지를 반환할 수 있기 때문이다.

Q. exists와 is_file 차이는?

A. exists는 경로 존재 여부만 확인하고, is_file은 해당 경로가 파일인지 확인한다.

Q. 폴더인지 확인하려면 무엇을 써?

A. `is_dir()`을 사용한다.

Q. 경로가 없으면 어떤 예외를 쓰면 좋아?

A. 파일이면 `FileNotFoundError`, 폴더면 `NotADirectoryError`를 사용할 수 있다.

---

# 4. Directory Handling

## 4.1 mkdir

### [개념]

`mkdir()`은 폴더를 생성하는 Path 메서드이다.

자동화 결과를 저장하기 전에 출력 폴더가 없으면 생성해야 한다.

```python
from pathlib import Path

output_dir = Path("reports")
output_dir.mkdir(exist_ok=True)
```

---

### [핵심]

- `mkdir()`은 폴더를 생성한다.
- `exist_ok=True`는 폴더가 이미 있어도 오류를 발생시키지 않는다.
- `parents=True`는 중간 폴더까지 함께 생성한다.
- 결과 리포트, 로그, 변환 파일 저장 전에 출력 폴더를 준비한다.
- 입력 폴더와 출력 폴더를 혼동하지 않는다.

---

### [실무]

단일 폴더 생성:

```python
from pathlib import Path

output_dir = Path("reports")
output_dir.mkdir(exist_ok=True)
```

중첩 폴더 생성:

```python
output_dir = Path("reports/validation/python")
output_dir.mkdir(parents=True, exist_ok=True)
```

결과 파일 저장:

```python
report_path = output_dir / "validation_report.md"
report_path.write_text("# Report\n", encoding="utf-8")
```

---

### [FAQ]

Q. mkdir은 무엇을 해?

A. 폴더를 생성한다.

Q. exist_ok=True는 왜 사용해?

A. 폴더가 이미 존재해도 오류가 발생하지 않도록 하기 위해 사용한다.

Q. parents=True는 언제 사용해?

A. 중간 경로의 폴더까지 함께 생성해야 할 때 사용한다.

Q. 출력 파일 저장 전에 폴더를 만들어야 해?

A. 그렇다. 폴더가 없으면 파일 저장 시 오류가 발생한다.

---

## 4.2 glob and rglob

### [개념]

`glob()`와 `rglob()`는 특정 패턴에 맞는 파일을 찾는 Path 메서드이다.

RAG Document Automation에서는 Markdown 파일을 일괄 스캔하기 위해 자주 사용한다.

```python
from pathlib import Path

base_dir = Path("docs")
md_files = list(base_dir.rglob("*.md"))
```

---

### [핵심]

- `glob(pattern)`은 현재 폴더 기준으로 패턴을 찾는다.
- `rglob(pattern)`은 하위 폴더까지 재귀적으로 찾는다.
- Markdown 문서 검색에는 `rglob("*.md")`가 유용하다.
- 결과는 정렬해서 사용하는 것이 안정적이다.
- 대량 파일 처리 시 파일 수와 처리 시간을 고려한다.

---

### [실무]

현재 폴더 Markdown 검색:

```python
from pathlib import Path

base_dir = Path("docs")
md_files = list(base_dir.glob("*.md"))
```

하위 폴더 포함 Markdown 검색:

```python
md_files = sorted(base_dir.rglob("*.md"))
```

파일명 출력:

```python
for md_file in md_files:
    print(md_file.name)
```

RAG 문서 스캔 함수:

```python
from pathlib import Path

def scan_markdown_files(base_dir: Path) -> list[Path]:
    if not base_dir.is_dir():
        raise NotADirectoryError(f"Directory not found: {base_dir}")

    return sorted(base_dir.rglob("*.md"))
```

---

### [FAQ]

Q. glob와 rglob 차이는?

A. glob는 현재 폴더 기준 검색이고, rglob는 하위 폴더까지 재귀 검색한다.

Q. Markdown 파일 전체를 찾으려면 무엇을 써?

A. `Path.rglob("*.md")`를 사용한다.

Q. rglob 결과는 정렬해야 해?

A. 권장한다. 처리 순서가 안정적이어야 결과 비교와 리포트 생성이 쉽다.

Q. 하위 폴더까지 모두 검사하려면?

A. `base_dir.rglob("*.md")`를 사용한다.

---

# 5. Reading Files

## 5.1 read_text

### [개념]

`read_text()`는 Path 객체에서 텍스트 파일을 읽는 메서드이다.

Markdown, JSON, YAML, TXT, Log 파일 같은 텍스트 파일 처리에 적합하다.

```python
from pathlib import Path

text = Path("docs/example.md").read_text(encoding="utf-8")
```

---

### [핵심]

- `read_text()`는 파일 전체를 문자열로 읽는다.
- encoding을 명시한다.
- 작은 Markdown 문서나 설정 파일에 적합하다.
- 대용량 파일은 한 번에 읽지 않는 방식을 고려한다.
- 파일 존재 여부를 먼저 확인하면 오류 메시지가 명확해진다.

---

### [실무]

Markdown 파일 읽기:

```python
from pathlib import Path

path = Path("docs/example.md")
text = path.read_text(encoding="utf-8")
```

안전한 읽기 함수:

```python
from pathlib import Path

def read_text_file(path: Path) -> str:
    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")

    return path.read_text(encoding="utf-8")
```

필수 섹션 검사와 연결:

```python
text = read_text_file(Path("docs/example.md"))
has_faq = "### [FAQ]" in text
```

---

### [FAQ]

Q. read_text는 무엇을 해?

A. 텍스트 파일 전체를 문자열로 읽는다.

Q. read_text에 encoding을 넣어야 해?

A. 권장한다. 한글 문서 처리에서는 `encoding="utf-8"`을 명시하는 것이 좋다.

Q. read_text는 대용량 파일에도 적합해?

A. 대용량 파일에는 부적합할 수 있다. 줄 단위 처리나 chunk 처리를 고려해야 한다.

Q. Markdown 파일 읽기에 read_text를 써도 돼?

A. 적합하다. Markdown은 텍스트 파일이므로 read_text로 읽을 수 있다.

---

## 5.2 readlines and Line Processing

### [개념]

Line Processing은 파일을 줄 단위로 읽고 처리하는 방식이다.

Header 검사, 로그 분석, 대용량 텍스트 처리에서는 줄 단위 처리가 유용하다.

```python
with open("docs/example.md", "r", encoding="utf-8") as file:
    lines = file.readlines()
```

---

### [핵심]

- `readlines()`는 파일을 줄 목록으로 읽는다.
- 파일 객체를 직접 순회하면 줄 단위 처리할 수 있다.
- Header, Section, Log Line 검사에 유용하다.
- 대용량 파일은 전체 read보다 줄 단위 처리가 안전하다.
- 줄 끝의 `\n` 처리를 고려해야 한다.

---

### [실무]

줄 목록 읽기:

```python
from pathlib import Path

path = Path("docs/example.md")
lines = path.read_text(encoding="utf-8").splitlines()
```

파일 객체 순회:

```python
with open("docs/example.md", "r", encoding="utf-8") as file:
    for line in file:
        if line.startswith("#"):
            print(line.strip())
```

Header 추출:

```python
def extract_headers(text: str) -> list[str]:
    return [
        line.strip()
        for line in text.splitlines()
        if line.startswith("#")
    ]
```

---

### [FAQ]

Q. 파일을 줄 단위로 처리하려면 어떻게 해?

A. 파일 객체를 for 문으로 순회하거나 `splitlines()`를 사용할 수 있다.

Q. read_text와 readlines 차이는?

A. read_text는 전체를 문자열로 읽고, readlines는 줄 목록으로 읽는다.

Q. Header 추출에는 줄 단위 처리가 좋아?

A. 그렇다. 각 줄이 Header인지 검사하기 쉽다.

Q. 줄 끝 개행 문자는 어떻게 처리해?

A. `strip()` 또는 `splitlines()`를 사용해 제거할 수 있다.

---

# 6. Writing Files

## 6.1 write_text

### [개념]

`write_text()`는 Path 객체를 사용해 텍스트 파일을 쓰는 메서드이다.

검증 리포트, 변환된 Markdown, JSON 문자열, 로그성 결과 저장에 사용할 수 있다.

```python
from pathlib import Path

Path("reports/result.md").write_text("# Result\n", encoding="utf-8")
```

---

### [핵심]

- `write_text()`는 파일에 문자열을 저장한다.
- 기존 파일이 있으면 덮어쓴다.
- encoding을 명시한다.
- 저장 전 출력 폴더 존재 여부를 확인한다.
- 원본 문서에 직접 쓰기 전 백업 또는 검증을 고려한다.

---

### [실무]

리포트 저장:

```python
from pathlib import Path

output_dir = Path("reports")
output_dir.mkdir(exist_ok=True)

report_path = output_dir / "validation_report.md"
report_path.write_text("# Validation Report\n", encoding="utf-8")
```

검증 결과 저장 함수:

```python
from pathlib import Path

def save_report(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
```

원본 덮어쓰기 방지:

```python
def safe_write_text(path: Path, content: str, overwrite: bool = False) -> None:
    if path.exists() and not overwrite:
        raise FileExistsError(f"File already exists: {path}")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
```

---

### [FAQ]

Q. write_text는 무엇을 해?

A. 문자열을 텍스트 파일로 저장한다.

Q. write_text는 기존 파일을 덮어써?

A. 그렇다. 기존 파일이 있으면 내용이 덮어쓰기 된다.

Q. write_text 전에 폴더를 만들어야 해?

A. 필요하다. 부모 폴더가 없으면 저장 시 오류가 발생한다.

Q. 원본 파일을 안전하게 저장하려면?

A. 덮어쓰기 여부를 확인하거나 백업 파일을 만든 뒤 저장한다.

---

## 6.2 Append File

### [개념]

Append는 기존 파일 내용 뒤에 새 내용을 추가하는 파일 쓰기 방식이다.

로그 기록, 처리 이력 저장, 누적 리포트 작성에 사용할 수 있다.

```python
with open("logs/process.log", "a", encoding="utf-8") as file:
    file.write("Processing completed\n")
```

---

### [핵심]

- append는 기존 내용을 유지한다.
- `"a"` 모드를 사용한다.
- 로그 파일에 자주 사용한다.
- 줄바꿈 문자를 명시해야 한다.
- 무한히 커지는 로그 파일은 관리가 필요하다.

---

### [실무]

로그성 텍스트 추가:

```python
from pathlib import Path

log_path = Path("logs/process.log")
log_path.parent.mkdir(parents=True, exist_ok=True)

with open(log_path, "a", encoding="utf-8") as file:
    file.write("RAG document validation completed\n")
```

추가 함수:

```python
from pathlib import Path

def append_text(path: Path, line: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "a", encoding="utf-8") as file:
        file.write(line + "\n")
```

---

### [FAQ]

Q. append는 언제 사용해?

A. 로그, 처리 이력, 누적 결과를 기존 파일 뒤에 추가할 때 사용한다.

Q. append 모드는 기존 내용을 지워?

A. 아니다. 기존 내용 뒤에 새 내용을 추가한다.

Q. append에서 줄바꿈은 자동으로 들어가?

A. 아니다. `\n`을 직접 추가해야 한다.

Q. 로그 파일이 너무 커지면 어떻게 해?

A. 로그 로테이션, 날짜별 로그 파일, logging 설정을 고려한다.

---

# 7. File Safety

## 7.1 Backup Before Overwrite

### [개념]

Backup Before Overwrite는 원본 파일을 수정하거나 덮어쓰기 전에 백업을 만드는 안전 처리 방식이다.

RAG 문서 자동 수정, Markdown 변환, 대량 파일 처리에서는 원본 보존이 중요하다.

---

### [핵심]

- 원본 파일 자동 수정 전 백업을 고려한다.
- 덮어쓰기 전에 검증 결과를 확인한다.
- 백업 파일명은 원본과 연결되게 작성한다.
- 같은 백업 파일명이 이미 있는지 확인한다.
- 위험 작업은 dry-run 옵션을 제공할 수 있다.

---

### [실무]

백업 파일 생성:

```python
from pathlib import Path
import shutil

def backup_file(path: Path) -> Path:
    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")

    backup_path = path.with_suffix(path.suffix + ".backup")
    shutil.copy2(path, backup_path)

    return backup_path
```

수정 전 백업:

```python
path = Path("docs/example.md")
backup_path = backup_file(path)

new_text = path.read_text(encoding="utf-8").replace("old", "new")
path.write_text(new_text, encoding="utf-8")
```

---

### [FAQ]

Q. 원본 파일을 수정하기 전에 백업해야 해?

A. 권장한다. 자동화 오류로 원본 문서가 훼손될 수 있기 때문이다.

Q. 백업 파일은 어떻게 만들 수 있어?

A. `shutil.copy2()`를 사용해 원본 파일을 복사할 수 있다.

Q. dry-run은 무엇이야?

A. 실제 파일을 수정하지 않고 어떤 작업이 수행될지 미리 확인하는 실행 방식이다.

Q. 대량 파일 처리에서 가장 위험한 작업은?

A. 원본 파일을 백업 없이 덮어쓰기 하는 작업이다.

---

## 7.2 Safe Delete

### [개념]

Safe Delete는 파일 삭제 작업에서 실수로 중요한 파일을 제거하지 않도록 보호하는 기준이다.

Agent Tool Script나 자동화 스크립트는 임의 삭제를 기본 동작으로 삼으면 안 된다.

---

### [핵심]

- 파일 삭제는 위험 작업이다.
- 삭제 전 대상 경로를 검증한다.
- 사용자 입력 경로를 그대로 삭제하지 않는다.
- dry-run 또는 확인 옵션을 둔다.
- 가능하면 삭제보다 archive 또는 move를 우선 고려한다.
- Agent Tool은 파일 삭제 권한을 제한해야 한다.

---

### [실무]

삭제 전 검증:

```python
from pathlib import Path

def delete_file(path: Path, confirm: bool = False) -> None:
    if not confirm:
        raise PermissionError("Delete requires confirm=True")

    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")

    path.unlink()
```

삭제 대신 archive:

```python
from pathlib import Path
import shutil

def archive_file(path: Path, archive_dir: Path) -> Path:
    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")

    archive_dir.mkdir(parents=True, exist_ok=True)
    target_path = archive_dir / path.name
    shutil.move(str(path), str(target_path))

    return target_path
```

---

### [FAQ]

Q. Python 자동화에서 파일 삭제는 바로 해도 돼?

A. 권장하지 않는다. 삭제 전 경로 검증, confirm 옵션, dry-run을 고려해야 한다.

Q. unlink는 무엇을 해?

A. 파일을 삭제한다.

Q. 삭제보다 안전한 방식은?

A. archive 폴더로 이동하거나 백업 후 삭제하는 방식이 안전하다.

Q. Agent Tool에서 파일 삭제 기능을 넣어도 돼?

A. 위험하다. 꼭 필요할 때만 제한된 경로와 명시적 확인 조건을 둬야 한다.

---

# 8. File Error Handling

## 8.1 Common File Errors

### [개념]

File Error Handling은 파일 처리 중 발생하는 오류를 명확하게 처리하는 기준이다.

자동화 스크립트는 실패 원인과 실패 파일을 알 수 있어야 한다.

---

### [핵심]

| Error                | 원인                | 처리                |
| -------------------- | ------------------- | ------------------- |
| `FileNotFoundError`  | 파일 없음           | 경로 확인           |
| `NotADirectoryError` | 폴더가 아님         | 입력 경로 검증      |
| `IsADirectoryError`  | 파일 대신 폴더 읽기 | 파일 여부 확인      |
| `PermissionError`    | 권한 부족           | 권한 확인           |
| `UnicodeDecodeError` | 인코딩 불일치       | encoding 확인       |
| `FileExistsError`    | 이미 파일 있음      | overwrite 정책 확인 |

---

### [실무]

파일 읽기 예외 처리:

```python
from pathlib import Path

def read_document(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        raise FileNotFoundError(f"Document not found: {path}")
    except UnicodeDecodeError:
        raise UnicodeDecodeError(
            "utf-8",
            b"",
            0,
            1,
            f"Encoding error while reading: {path}",
        )
```

구조화된 오류 결과:

```python
from pathlib import Path

def safe_read_document(path: Path) -> dict:
    try:
        text = path.read_text(encoding="utf-8")
        return {
            "status": "success",
            "path": str(path),
            "text": text,
            "error": None,
        }
    except Exception as error:
        return {
            "status": "error",
            "path": str(path),
            "text": None,
            "error": str(error),
        }
```

---

### [FAQ]

Q. FileNotFoundError는 언제 발생해?

A. 지정한 파일 경로가 존재하지 않을 때 발생한다.

Q. UnicodeDecodeError는 언제 발생해?

A. 파일 인코딩과 읽기 encoding이 맞지 않을 때 발생한다.

Q. PermissionError는 언제 발생해?

A. 파일이나 폴더에 접근 권한이 없을 때 발생한다.

Q. 파일 처리 오류는 무시해도 돼?

A. 안 된다. 실패 파일과 원인을 알 수 있게 메시지나 구조화된 결과로 남겨야 한다.

---

# 9. File I/O Best Practice

## 9.1 Best Practice

### [개념]

File I/O Best Practice는 Python 자동화에서 파일 처리 안정성, 재현성, 원본 보호, Agent 검증 가능성을 높이는 기준이다.

목표:

```text
Safe Path
→ Safe Read
→ Safe Process
→ Safe Write
→ Structured Result
```

---

### [핵심]

- `pathlib.Path`를 우선 사용한다.
- 파일 경로는 문자열 결합보다 `/` 연산자로 구성한다.
- 파일 읽기와 쓰기에는 UTF-8 encoding을 명시한다.
- 파일 읽기 전 존재 여부와 파일 여부를 확인한다.
- 출력 파일 저장 전 부모 폴더를 생성한다.
- 원본 덮어쓰기 전 백업을 고려한다.
- 위험 작업에는 dry-run 또는 confirm 옵션을 둔다.
- 대량 파일 처리 시 정렬된 파일 목록을 사용한다.
- 오류 발생 시 파일 경로와 원인을 함께 남긴다.
- Agent Tool Output은 파일 처리 결과를 dict 또는 JSON으로 반환한다.

---

### [실무]

안전한 RAG 문서 파일 처리 예시:

```python
from pathlib import Path

def scan_markdown_files(base_dir: Path) -> list[Path]:
    if not base_dir.is_dir():
        raise NotADirectoryError(f"Directory not found: {base_dir}")

    return sorted(base_dir.rglob("*.md"))


def read_markdown(path: Path) -> str:
    if not path.is_file():
        raise FileNotFoundError(f"Markdown file not found: {path}")

    return path.read_text(encoding="utf-8")


def save_text(path: Path, content: str, overwrite: bool = False) -> None:
    if path.exists() and not overwrite:
        raise FileExistsError(f"File already exists: {path}")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def validate_file_io(base_dir: Path) -> dict:
    files = scan_markdown_files(base_dir)

    return {
        "status": "success",
        "base_dir": str(base_dir),
        "file_count": len(files),
        "files": [file.name for file in files],
    }
```

---

### [FAQ]

Q. Python File I/O Best Practice는 무엇이야?

A. pathlib 사용, encoding 명시, 경로 검증, 부모 폴더 생성, 백업, 구조화된 결과 반환이다.

Q. RAG 문서 자동화에서 파일 처리 순서는?

A. 폴더 확인 → Markdown 파일 스캔 → 파일 읽기 → 검증 → 결과 저장 순서가 좋다.

Q. 파일 처리 결과는 어떻게 반환하는 게 좋아?

A. Agent가 이해하기 쉽도록 `status`, `file_count`, `files`, `error` 같은 dict 구조가 좋다.

Q. 대량 Markdown 파일 처리에서 중요한 점은?

A. 파일 목록을 정렬하고, 실패 파일과 실패 원인을 개별적으로 기록하는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Python File I/O는 무엇이야?
A. Python에서 파일을 읽고 쓰는 작업이며 RAG 문서, 설정 파일, 로그, 검증 결과 처리에 사용된다.

Q. Python 자동화에서 File I/O는 왜 중요해?
A. 자동화 스크립트가 문서, 데이터, 설정, 리포트를 읽고 저장해야 하기 때문이다.

Q. Python 파일 읽기에서 encoding은 왜 명시해?
A. 한글 Markdown, CSV, 로그 파일에서 인코딩 오류를 줄이기 위해 `encoding="utf-8"`을 명시한다.

Q. Python에서 파일 처리는 open과 pathlib 중 무엇을 권장해?
A. Modern Python에서는 `pathlib.Path`를 우선 권장한다.

Q. Python open 함수는 무엇을 해?
A. 파일을 읽거나 쓰기 위해 파일을 여는 기본 함수이다.

Q. Python with 구문은 왜 사용해?
A. 파일 작업이 끝난 후 자동으로 파일을 닫아 자원 누수를 줄이기 위해 사용한다.

Q. Python 파일 읽기 모드는 무엇이야?
A. `"r"` 모드이다.

Q. Python 파일 쓰기 모드는 무엇이야?
A. `"w"` 모드이며 기존 파일 내용이 덮어쓰기 될 수 있다.

Q. Python 파일 추가 모드는 무엇이야?
A. `"a"` 모드이며 기존 내용 뒤에 새 내용을 추가한다.

Q. Python `w` 모드는 왜 조심해야 해?
A. 기존 파일 내용이 즉시 덮어쓰기 되기 때문이다.

Q. Python 파일이 없을 때만 새로 만들려면?
A. `x` 모드를 사용한다.

Q. Python 로그 파일에는 어떤 모드를 사용해?
A. 기존 내용 뒤에 추가하는 `a` 모드를 자주 사용한다.

Q. Python에서 이미지 파일이나 PDF는 어떤 모드를 사용해?
A. 바이너리 모드인 `rb`, `wb`를 사용한다.

Q. Python pathlib은 왜 사용해?
A. OS별 경로 차이를 줄이고 파일 존재 확인, 폴더 생성, 파일 탐색을 안전하게 처리할 수 있기 때문이다.

Q. Python Path 객체는 문자열이야?
A. 아니다. 파일 경로를 표현하는 객체이다.

Q. Python Path와 문자열 경로를 합칠 때 무엇을 사용해?
A. `base_dir / "file.md"` 형태를 사용한다.

Q. Python path.name은 무엇을 반환해?
A. 확장자를 포함한 파일명 전체를 반환한다.

Q. Python path.stem은 무엇을 반환해?
A. 확장자를 제외한 파일명을 반환한다.

Q. Python path.suffix는 무엇을 반환해?
A. 파일 확장자를 반환한다.

Q. Python path.parent는 무엇을 반환해?
A. 해당 파일의 부모 폴더 경로를 반환한다.

Q. Python exists와 is_file 차이는?
A. exists는 경로 존재 여부를 확인하고, is_file은 해당 경로가 파일인지 확인한다.

Q. Python 폴더인지 확인하려면?
A. `is_dir()`을 사용한다.

Q. Python 경로가 없으면 어떤 예외를 사용해?
A. 파일이면 `FileNotFoundError`, 폴더면 `NotADirectoryError`를 사용할 수 있다.

Q. Python mkdir은 무엇을 해?
A. 폴더를 생성한다.

Q. Python exist_ok=True는 왜 사용해?
A. 폴더가 이미 존재해도 오류가 발생하지 않도록 하기 위해 사용한다.

Q. Python parents=True는 언제 사용해?
A. 중간 경로의 폴더까지 함께 생성해야 할 때 사용한다.

Q. Python glob와 rglob 차이는?
A. glob는 현재 폴더 기준 검색이고, rglob는 하위 폴더까지 재귀 검색한다.

Q. Python Markdown 파일 전체를 찾으려면?
A. `Path.rglob("*.md")`를 사용한다.

Q. Python rglob 결과는 정렬해야 해?
A. 권장한다. 처리 순서가 안정적이어야 결과 비교와 리포트 생성이 쉽다.

Q. Python read_text는 무엇을 해?
A. 텍스트 파일 전체를 문자열로 읽는다.

Q. Python read_text는 대용량 파일에도 적합해?
A. 대용량 파일에는 부적합할 수 있으므로 줄 단위 처리나 chunk 처리를 고려해야 한다.

Q. Python 파일을 줄 단위로 처리하려면?
A. 파일 객체를 for 문으로 순회하거나 `splitlines()`를 사용할 수 있다.

Q. Python read_text와 readlines 차이는?
A. read_text는 전체를 문자열로 읽고, readlines는 줄 목록으로 읽는다.

Q. Python Header 추출에는 줄 단위 처리가 좋아?
A. 그렇다. 각 줄이 Header인지 검사하기 쉽다.

Q. Python write_text는 무엇을 해?
A. 문자열을 텍스트 파일로 저장한다.

Q. Python write_text는 기존 파일을 덮어써?
A. 그렇다. 기존 파일이 있으면 내용이 덮어쓰기 된다.

Q. Python write_text 전에 폴더를 만들어야 해?
A. 필요하다. 부모 폴더가 없으면 저장 시 오류가 발생한다.

Q. Python 원본 파일을 안전하게 저장하려면?
A. 덮어쓰기 여부를 확인하거나 백업 파일을 만든 뒤 저장한다.

Q. Python append는 언제 사용해?
A. 로그, 처리 이력, 누적 결과를 기존 파일 뒤에 추가할 때 사용한다.

Q. Python append 모드는 기존 내용을 지워?
A. 아니다. 기존 내용 뒤에 새 내용을 추가한다.

Q. Python append에서 줄바꿈은 자동으로 들어가?
A. 아니다. `\n`을 직접 추가해야 한다.

Q. Python 원본 파일 수정 전에 백업해야 해?
A. 권장한다. 자동화 오류로 원본 문서가 훼손될 수 있기 때문이다.

Q. Python 백업 파일은 어떻게 만들 수 있어?
A. `shutil.copy2()`를 사용해 원본 파일을 복사할 수 있다.

Q. Python dry-run은 무엇이야?
A. 실제 파일을 수정하지 않고 어떤 작업이 수행될지 미리 확인하는 실행 방식이다.

Q. Python 파일 삭제는 바로 해도 돼?
A. 권장하지 않는다. 삭제 전 경로 검증, confirm 옵션, dry-run을 고려해야 한다.

Q. Python unlink는 무엇을 해?
A. 파일을 삭제한다.

Q. Python 삭제보다 안전한 방식은?
A. archive 폴더로 이동하거나 백업 후 삭제하는 방식이 안전하다.

Q. Python FileNotFoundError는 언제 발생해?
A. 지정한 파일 경로가 존재하지 않을 때 발생한다.

Q. Python UnicodeDecodeError는 언제 발생해?
A. 파일 인코딩과 읽기 encoding이 맞지 않을 때 발생한다.

Q. Python PermissionError는 언제 발생해?
A. 파일이나 폴더에 접근 권한이 없을 때 발생한다.

Q. Python 파일 처리 오류는 무시해도 돼?
A. 안 된다. 실패 파일과 원인을 알 수 있게 메시지나 구조화된 결과로 남겨야 한다.

Q. Python File I/O Best Practice는 무엇이야?
A. pathlib 사용, encoding 명시, 경로 검증, 부모 폴더 생성, 백업, 구조화된 결과 반환이다.

Q. Python RAG 문서 자동화에서 파일 처리 순서는?
A. 폴더 확인 → Markdown 파일 스캔 → 파일 읽기 → 검증 → 결과 저장 순서가 좋다.

Q. Python 파일 처리 결과는 어떻게 반환하는 게 좋아?
A. Agent가 이해하기 쉽도록 `status`, `file_count`, `files`, `error` 같은 dict 구조가 좋다.
