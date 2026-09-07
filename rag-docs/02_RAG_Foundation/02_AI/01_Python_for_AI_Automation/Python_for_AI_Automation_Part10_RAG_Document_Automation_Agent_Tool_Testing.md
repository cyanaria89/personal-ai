# Python for AI Automation Part10 - RAG Document Automation Agent Tool Testing

---

# 1. RAG Document Automation Overview

## 1.1 RAG Document Automation Role

### [개념]

RAG Document Automation은 Python으로 Markdown 기반 RAG 문서를 스캔하고, 파일명 규칙, 필수 섹션, FAQ Q/A, Retrieval Queries, Code Block, Chunk 구조를 자동 검증하는 작업이다.

Python for AI Automation에서 RAG Document Automation은 AI Agent가 사용할 지식 문서의 품질을 유지하고, Retrieval 성능 저하를 막기 위한 핵심 자동화 영역이다.

Part10은 앞선 문서들의 최종 연결 지점이다.

```text
Part04 File I/O
→ Markdown File Read / Write

Part05 Markdown / JSON / CSV Processing
→ RAG Document Parsing / Report Save

Part06 API / Environment Variable
→ Agent Tool Server / External API Integration

Part07 Exception Handling / Logging
→ Structured Error Result / Failure Tracking

Part08 Type Hint / Dataclass / TypedDict
→ ToolOutput / ValidationResult Type Structure

Part09 CLI / Dependency / venv
→ CLI Execution / JSON stdout / Exit Code
```

기본 Flow:

```text
RAG Folder
→ Scan Markdown Files
→ Validate File Naming
→ Validate Required Sections
→ Validate FAQ Q/A
→ Validate Retrieval Queries
→ Check Code Blocks
→ Generate Report
```

---

### [핵심]

- RAG 문서는 Markdown 기준으로 관리한다.
- Python은 RAG 문서 품질 검사 자동화에 적합하다.
- 필수 섹션은 `[개념]`, `[핵심]`, `[실무]`, `[FAQ]`이다.
- 모든 문서 마지막에는 `# Retrieval Queries`가 필요하다.
- FAQ는 Q/A 쌍으로 구성되어야 한다.
- Code Block 내부 Header를 실제 Header로 오인하면 안 된다.
- 검증 결과는 dict, JSON, CSV, Markdown Report로 저장할 수 있다.
- Agent Tool Script는 검증 결과를 구조화된 JSON으로 반환하는 것이 좋다.
- 실제 운영에서는 `REQUIRED_SECTIONS`를 `config.py`, YAML Config, Domain Rules 중 하나에서 중앙 관리한다.
- Part08의 `ToolOutput` 표준 구조와 맞춰 `status`, `result`, `error`를 사용한다.
- Part09의 CLI 실행 구조와 연결하려면 JSON stdout과 Exit Code를 제공한다.

---

### [실무]

2026 실무 기준 RAG Document Automation은 단순 파일 검사보다 Agent Retrieval 품질 유지에 초점을 둔다.

검증 대상:

- 파일명 규칙
- Markdown 확장자
- Document Title 존재 여부
- Required Section 존재 여부
- FAQ Q/A 쌍 존재 여부
- Retrieval Queries 존재 여부
- Code Block 닫힘 여부
- Header Level 구조
- 금지 섹션명 사용 여부
- Chunk 과대 크기
- 중복 Header
- Agent Tool Output 구조

검증 결과 예시:

```python
{
    "status": "success",
    "result": {
        "file_name": "Python_for_AI_Automation_Part10_RAG_Document_Automation_Agent_Tool_Testing.md",
        "is_valid": True,
        "missing_sections": [],
        "has_retrieval_queries": True,
        "has_unclosed_code_block": False
    },
    "error": None
}
```

운영 구조 예시:

```text
config.py
→ REQUIRED_SECTIONS
→ FORBIDDEN_SECTIONS
→ FILE_NAME_PATTERN
→ MAX_CHUNK_CHARS

markdown_scanner.py
→ scan_markdown_files

markdown_validator.py
→ validate_document_text
→ validate_document_file

report_builder.py
→ build_json_report
→ build_markdown_report

agent_tool.py
→ run_document_validation_tool

cli.py
→ parse_args
→ print_json
→ return_exit_code
```

---

### [FAQ]

Q. RAG Document Automation은 무엇을 자동화해?

A. Markdown RAG 문서의 파일명, 필수 섹션, FAQ, Retrieval Queries, Code Block, Chunk 구조 검사를 자동화한다.

Q. RAG 문서 검증을 Python으로 하는 이유는?

A. 많은 Markdown 문서를 반복 검수하고 품질 리포트를 일관되게 만들 수 있기 때문이다.

Q. RAG 문서 자동화에서 가장 중요한 검사는?

A. 필수 섹션 존재 여부, FAQ Q/A 쌍, Retrieval Queries 존재 여부, Code Block 닫힘 여부이다.

Q. 검증 결과는 어떤 형태가 좋아?

A. Agent가 처리하기 쉬운 dict 또는 JSON 구조가 좋다.

Q. REQUIRED_SECTIONS는 어디에서 관리하는 게 좋아?

A. 실제 운영에서는 `config.py`, YAML Config, Domain Rules 중 하나에서 중앙 관리하는 것이 좋다.

---

# 2. Markdown File Scan

## 2.1 Markdown File Scan

### [개념]

Markdown File Scan은 지정한 RAG 문서 폴더에서 `.md` 파일을 찾는 작업이다.

RAG Document Automation의 첫 단계이며, 이후 모든 검증은 스캔된 Markdown 파일 목록을 기준으로 수행된다.

```text
Base Directory
→ rglob("*.md")
→ Sort Files
→ Return Markdown File List
```

---

### [핵심]

- `pathlib.Path`를 사용한다.
- 하위 폴더까지 검사하려면 `rglob("*.md")`를 사용한다.
- 처리 순서 안정성을 위해 정렬한다.
- 입력 폴더 존재 여부를 먼저 확인한다.
- Markdown 파일이 없으면 명확한 결과를 반환한다.
- 스캔 결과는 `list[Path]`로 관리한다.
- `.venv`, `node_modules`, `.git` 같은 폴더는 제외할 수 있다.
- 파일 스캔 결과는 Report Summary에 포함한다.

---

### [실무]

Markdown 파일 스캔 함수:

```python
from pathlib import Path

def scan_markdown_files(base_dir: Path) -> list[Path]:
    if not base_dir.is_dir():
        raise NotADirectoryError(f"Directory not found: {base_dir}")

    ignored_parts = {".git", ".venv", "node_modules", "__pycache__"}

    files = [
        path for path in base_dir.rglob("*.md")
        if not ignored_parts.intersection(path.parts)
    ]

    return sorted(files)
```

스캔 결과 생성:

```python
from pathlib import Path

def build_scan_result(base_dir: Path) -> dict:
    files = scan_markdown_files(base_dir)

    return {
        "status": "success",
        "base_dir": str(base_dir),
        "file_count": len(files),
        "files": [file.name for file in files],
    }
```

빈 폴더 처리:

```python
from pathlib import Path

def require_markdown_files(files: list[Path]) -> None:
    if not files:
        raise FileNotFoundError("No Markdown files found")
```

---

### [FAQ]

Q. Markdown 파일 스캔은 어떻게 해?

A. `Path.rglob("*.md")`를 사용해 하위 폴더까지 Markdown 파일을 찾는다.

Q. 스캔 결과를 정렬해야 해?

A. 권장한다. Part01, Part02 순서처럼 처리 순서가 안정적이어야 리포트 비교가 쉽다.

Q. 입력 폴더가 없으면 어떻게 처리해?

A. `NotADirectoryError`를 발생시키거나 구조화된 error result를 반환한다.

Q. Markdown 파일이 하나도 없으면 어떻게 해?

A. 빈 결과를 반환하거나 `FileNotFoundError`로 명확히 실패시킨다.

Q. `.venv`나 `.git` 폴더도 스캔해야 해?

A. 보통 제외한다. RAG 문서 검증 대상이 아니며 불필요한 파일이 섞일 수 있기 때문이다.

---

# 3. File Naming Validation

## 3.1 File Naming Rule

### [개념]

File Naming Validation은 RAG 문서 파일명이 정해진 규칙을 따르는지 검사하는 작업이다.

파일명이 일관되면 Agent Retrieval, 문서 정렬, Part 연결, 유지보수성이 좋아진다.

예시 규칙:

```text
Python_for_AI_Automation_Part10_RAG_Document_Automation_Agent_Tool_Testing.md
```

---

### [핵심]

- 파일명은 Domain, Part Number, Topic을 포함한다.
- Part 번호는 `Part01`, `Part02`처럼 두 자리 형식을 권장한다.
- 확장자는 `.md`를 사용한다.
- 공백보다 `_`를 사용한다.
- 파일명은 문서 제목과 연결되어야 한다.
- 파일명 검사는 정규식으로 처리할 수 있다.
- 실제 운영에서는 파일명 패턴을 Config로 관리한다.
- Part 번호 중복과 누락을 검사할 수 있다.

---

### [실무]

파일명 패턴 검사:

```python
import re
from pathlib import Path

FILE_NAME_PATTERN = r"^Python_for_AI_Automation_Part\d{2}_.+\.md$"

def validate_file_name(path: Path) -> dict:
    is_valid = bool(re.match(FILE_NAME_PATTERN, path.name))

    return {
        "file_name": path.name,
        "is_valid_file_name": is_valid,
    }
```

Part 번호 추출:

```python
import re

def extract_part_number(file_name: str) -> int | None:
    match = re.search(r"Part(\d{2})", file_name)

    if not match:
        return None

    return int(match.group(1))
```

Part 번호 중복 검사:

```python
from pathlib import Path

def find_duplicate_part_numbers(paths: list[Path]) -> list[int]:
    seen = set()
    duplicates = set()

    for path in paths:
        part_number = extract_part_number(path.name)

        if part_number is None:
            continue

        if part_number in seen:
            duplicates.add(part_number)

        seen.add(part_number)

    return sorted(duplicates)
```

파일명 검증 결과:

```python
{
    "file_name": "Python_for_AI_Automation_Part10_RAG_Document_Automation_Agent_Tool_Testing.md",
    "is_valid_file_name": True,
    "part_number": 10
}
```

---

### [FAQ]

Q. RAG 문서 파일명 규칙은 왜 중요해?

A. 문서 정렬, Part 연결, 검색 결과 식별, 유지보수성을 높이기 위해 중요하다.

Q. Part 번호는 왜 두 자리로 쓰는 게 좋아?

A. Part01, Part02, Part10 순서가 안정적으로 정렬되기 때문이다.

Q. 파일명 검사는 어떻게 해?

A. 정규식으로 Domain, Part 번호, Topic, `.md` 확장자를 검사할 수 있다.

Q. 파일명에 공백을 써도 돼?

A. 가능하지만 자동화와 경로 처리를 위해 `_` 사용을 권장한다.

Q. Part 번호 중복도 검사해야 해?

A. 권장한다. 중복 Part 번호는 문서 순서와 검색 결과 관리에 혼선을 줄 수 있다.

---

# 4. Required Section Validation

## 4.1 Required Section Check

### [개념]

Required Section Validation은 RAG 문서에 필수 섹션이 모두 포함되어 있는지 검사하는 작업이다.

Python for AI Automation RAG 문서는 `[개념]`, `[핵심]`, `[실무]`, `[FAQ]` 섹션을 우선 포함해야 한다.

실제 운영에서는 필수 섹션 목록을 코드에 흩어두지 않고 `config.py`, YAML Config, Domain Rules에서 중앙 관리하는 것이 좋다.

---

### [핵심]

- 필수 섹션은 문서 품질의 최소 기준이다.
- `[개념]`은 정의와 목적을 제공한다.
- `[핵심]`은 Retrieval Keyword 중심 요약을 제공한다.
- `[실무]`는 실전 적용 기준을 제공한다.
- `[FAQ]`는 사용자 질문 패턴 매칭을 강화한다.
- 누락 섹션은 `missing_sections`로 반환한다.
- 필수 섹션 검사는 문서 전체 텍스트 기준으로 수행할 수 있다.
- Code Block 내부의 섹션 문자열은 실제 섹션으로 오인하지 않는 것이 좋다.

---

### [실무]

Config 기준 필수 섹션:

```python
REQUIRED_SECTIONS = ["### [개념]", "### [핵심]", "### [실무]", "### [FAQ]"]
```

필수 섹션 검사:

```python
def find_missing_sections(text: str, required_sections: list[str]) -> list[str]:
    return [
        section for section in required_sections
        if section not in text
    ]
```

검증 결과:

```python
def validate_required_sections(text: str) -> dict:
    missing_sections = find_missing_sections(
        text=text,
        required_sections=REQUIRED_SECTIONS,
    )

    return {
        "has_required_sections": len(missing_sections) == 0,
        "missing_sections": missing_sections,
    }
```

문서 파일 검증:

```python
from pathlib import Path

def validate_file_required_sections(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    result = validate_required_sections(text)

    return {
        "file_name": path.name,
        **result,
    }
```

---

### [FAQ]

Q. RAG 문서 필수 섹션은 무엇이야?

A. `[개념]`, `[핵심]`, `[실무]`, `[FAQ]`이다.

Q. 필수 섹션 검사는 왜 필요해?

A. 모든 문서가 동일한 Retrieval 구조를 갖도록 보장하기 위해 필요하다.

Q. 누락 섹션은 어떻게 반환해?

A. `missing_sections` list로 반환하는 것이 좋다.

Q. 필수 섹션이 하나라도 없으면 실패로 봐야 해?

A. 기본적으로 실패로 보고 수정 대상으로 분류하는 것이 좋다.

Q. REQUIRED_SECTIONS는 어디에서 관리하는 게 좋아?

A. 실제 운영에서는 `config.py`, YAML Config, Domain Rules 중 하나에서 중앙 관리하는 것이 좋다.

---

# 5. FAQ Validation

## 5.1 FAQ Q/A Pair Check

### [개념]

FAQ Validation은 `[FAQ]` 섹션과 `# Retrieval Queries` 영역에 Q/A 쌍이 정상적으로 작성되어 있는지 검사하는 작업이다.

FAQ는 RAG Retrieval에서 사용자 질문 패턴과 문서 내용을 연결하는 핵심 구조이다.

---

### [핵심]

- FAQ는 반드시 Q와 A가 함께 있어야 한다.
- Q만 있는 FAQ는 금지한다.
- A는 짧고 명확해야 한다.
- `[FAQ]` 섹션 내부에 무분별한 `---` 사용을 피한다.
- Retrieval Queries에도 FAQ 형식 질문을 포함한다.
- FAQ는 실제 사용자가 검색할 질문 표현을 포함해야 한다.
- FAQ는 Semantic Search와 Query Pattern Matching을 강화한다.
- Code Block 내부의 `Q.`, `A.`는 실제 FAQ로 오인하지 않는 것이 좋다.

---

### [실무]

단순 Q/A 검사:

```python
def has_faq_qa_pair(text: str) -> bool:
    return "Q." in text and "A." in text
```

FAQ 개수 검사:

```python
def count_faq_questions(text: str) -> int:
    return sum(
        1 for line in text.splitlines()
        if line.strip().startswith("Q.")
    )


def count_faq_answers(text: str) -> int:
    return sum(
        1 for line in text.splitlines()
        if line.strip().startswith("A.")
    )
```

FAQ 균형 검사:

```python
def validate_faq_balance(text: str) -> dict:
    question_count = count_faq_questions(text)
    answer_count = count_faq_answers(text)

    return {
        "question_count": question_count,
        "answer_count": answer_count,
        "is_balanced": question_count == answer_count and question_count > 0,
    }
```

Code Block 제거 후 FAQ 검사:

````python
def remove_code_blocks(text: str) -> str:
    lines = []
    in_code_block = False

    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            continue

        if not in_code_block:
            lines.append(line)

    return "\n".join(lines)
````

---

### [FAQ]

Q. FAQ Validation은 왜 필요해?

A. FAQ는 실제 사용자 질문과 문서 검색 매칭을 강화하므로 Q/A 구조가 반드시 필요하다.

Q. FAQ에 Q만 있어도 돼?

A. 안 된다. 반드시 Q와 A가 함께 있어야 한다.

Q. FAQ 답변은 길어도 돼?

A. 권장하지 않는다. A는 짧고 명확하게 작성하는 것이 Retrieval에 유리하다.

Q. Retrieval Queries에도 FAQ가 필요한가?

A. 필요하다. 문서 마지막에 실제 검색 질문 패턴을 강화하기 위해 포함한다.

Q. Code Block 내부 Q/A도 FAQ로 세야 해?

A. 아니다. 예제 텍스트일 수 있으므로 실제 FAQ 구조와 구분하는 것이 좋다.

---

# 6. Retrieval Queries Validation

## 6.1 Retrieval Queries Check

### [개념]

Retrieval Queries Validation은 문서 마지막에 `# Retrieval Queries` 블록이 존재하고, 실제 사용자 질문 패턴을 포함하는지 검사하는 작업이다.

Retrieval Queries는 RAG 검색에서 Query Matching과 Semantic Similarity를 강화하는 필수 블록이다.

---

### [핵심]

- 모든 RAG 문서 마지막에 `# Retrieval Queries`가 있어야 한다.
- Retrieval Queries에는 `[FAQ]` 형식 질문을 포함한다.
- 질문은 실제 사용자가 물어볼 표현으로 작성한다.
- 답변은 짧고 명확해야 한다.
- 문서 핵심 키워드를 반복해도 된다.
- Retrieval Queries가 없으면 문서 검색 성능이 떨어질 수 있다.
- Retrieval Queries는 문서 본문과 연결되어야 한다.
- 문서 중간이 아니라 마지막 영역에 위치하는 것이 좋다.

---

### [실무]

Retrieval Queries 존재 검사:

```python
def has_retrieval_queries(text: str) -> bool:
    return "# Retrieval Queries" in text
```

문서 마지막 위치 검사:

```python
def is_retrieval_queries_near_end(text: str) -> bool:
    index = text.rfind("# Retrieval Queries")

    if index == -1:
        return False

    tail_ratio = index / max(len(text), 1)
    return tail_ratio >= 0.7
```

Retrieval Queries 검증:

```python
def validate_retrieval_queries(text: str) -> dict:
    return {
        "has_retrieval_queries": has_retrieval_queries(text),
        "is_near_end": is_retrieval_queries_near_end(text),
    }
```

Retrieval Queries 내부 FAQ 검사:

```python
def extract_retrieval_queries_block(text: str) -> str:
    marker = "# Retrieval Queries"
    index = text.rfind(marker)

    if index == -1:
        return ""

    return text[index:]


def validate_retrieval_queries_faq(text: str) -> dict:
    block = extract_retrieval_queries_block(text)

    return {
        "has_retrieval_queries_faq": "Q." in block and "A." in block,
        "retrieval_queries_question_count": count_faq_questions(block),
    }
```

---

### [FAQ]

Q. Retrieval Queries는 왜 필요해?

A. 실제 사용자 질문 패턴과 문서 내용을 연결해 검색 매칭을 강화하기 위해 필요하다.

Q. Retrieval Queries는 문서 어디에 있어야 해?

A. 문서 마지막에 두는 것이 좋다.

Q. Retrieval Queries 답변은 길게 써도 돼?

A. 권장하지 않는다. 짧고 명확한 답변이 검색 매칭에 유리하다.

Q. Retrieval Queries가 없으면 어떻게 처리해?

A. 검증 실패로 보고 수정 대상에 포함한다.

Q. Retrieval Queries 내부에도 FAQ Q/A가 있어야 해?

A. 권장한다. 실제 검색 질문 패턴을 강화하기 위해 Q/A 구조를 포함하는 것이 좋다.

---

# 7. Code Block Validation

## 7.1 Code Block Check

### [개념]

Code Block Validation은 Markdown 문서의 코드 블록이 정상적으로 열리고 닫혔는지 검사하는 작업이다.

Code Block이 깨지면 문서 파싱, Header 추출, Chunk 분리, RAG 검색 품질에 문제가 생길 수 있다.

---

### [핵심]

- Markdown Code Block은 `로 시작하고 `로 끝난다.
- Code Block Fence 개수는 기본적으로 짝수여야 한다.
- Code Block 내부 Header를 실제 Header로 오인하면 안 된다.
- Code Block 내부 Q/A를 실제 FAQ로 오인하면 안 된다.
- Code Block이 닫히지 않으면 Chunk 분리에 문제가 생긴다.
- 단순 검사는 Fence 개수 기반으로 가능하다.
- 복잡한 Markdown에서는 단순 Fence Count가 오탐을 만들 수 있다.
- 실제 운영에서는 Markdown Parser 또는 Fence Language / indentation 기준을 함께 고려할 수 있다.

---

### [실무]

닫히지 않은 Code Block 검사:

````python
def has_unclosed_code_block(text: str) -> bool:
    fence_count = sum(
        1 for line in text.splitlines()
        if line.strip().startswith("```")
    )

    return fence_count % 2 != 0
````

Code Block 제외 Header 추출:

````python
def extract_headers_outside_code_block(text: str) -> list[str]:
    headers = []
    in_code_block = False

    for line in text.splitlines():
        stripped = line.strip()

        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue

        if not in_code_block and stripped.startswith("#"):
            headers.append(stripped)

    return headers
````

Code Block 검증 결과:

```python
def validate_code_blocks(text: str) -> dict:
    return {
        "has_unclosed_code_block": has_unclosed_code_block(text),
    }
```

단순 Fence Count 한계:

```text
단순 Fence Count
→ 빠르고 구현 쉬움
→ 일반 Markdown RAG 문서에 충분히 유용

복잡한 Markdown Parser
→ nested fence / indentation / escape case 대응 가능
→ 구현 복잡도 증가
```

---

### [FAQ]

Q. Code Block Validation은 왜 필요해?

A. Code Block이 깨지면 Header 추출, Chunk 분리, Markdown 파싱에 문제가 생기기 때문이다.

Q. Code Block이 닫히지 않았는지 어떻게 검사해?

A. Fence 개수를 세고 홀수이면 닫히지 않은 것으로 판단할 수 있다.

Q. Code Block 내부 Header는 실제 Header야?

A. 아니다. Code Block 내부의 `#`는 코드나 예시 텍스트일 수 있다.

Q. Code Block 내부 Q/A를 FAQ로 세면 안 되는 이유는?

A. 예제 코드나 텍스트일 수 있으므로 실제 문서 FAQ 구조와 구분해야 한다.

Q. Fence Count 방식은 항상 정확해?

A. 아니다. 단순 검증에는 유용하지만 복잡한 Markdown에서는 오탐 가능성이 있어 Parser 사용도 고려한다.

---

# 8. Chunk Preparation Validation

## 8.1 Chunk Quality Check

### [개념]

Chunk Preparation Validation은 RAG 문서가 검색 가능한 독립 Chunk로 분리되기 적합한 구조인지 검사하는 작업이다.

좋은 Chunk는 하나의 개념을 담고, 제목이 명확하며, 독립적으로 검색되어도 의미가 유지되어야 한다.

---

### [핵심]

- Header는 Chunk 경계 후보이다.
- 하나의 Chunk에는 하나의 개념만 담는 것이 좋다.
- Chunk는 독립 검색되어도 의미가 유지되어야 한다.
- Code Block은 중간에 잘리면 안 된다.
- 너무 긴 Section은 Sub Section으로 분리한다.
- 권장 Chunk Size는 300~1200 tokens이다.
- FAQ Chunk는 Retrieval Matching에 중요하다.
- Chunk Metadata에는 file_name, title, section, keywords를 포함할 수 있다.

---

### [실무]

문자 수 기반 간단 검사:

```python
def estimate_chunk_size(text: str) -> int:
    return len(text)


def is_chunk_too_large(text: str, max_chars: int = 6000) -> bool:
    return estimate_chunk_size(text) > max_chars
```

Header 기반 섹션 분리:

```python
def split_by_level_2_headers(text: str) -> list[str]:
    chunks = []
    current_lines = []

    for line in text.splitlines():
        if line.startswith("## ") and current_lines:
            chunks.append("\n".join(current_lines))
            current_lines = []

        current_lines.append(line)

    if current_lines:
        chunks.append("\n".join(current_lines))

    return chunks
```

Chunk 검증 결과:

```python
def validate_chunk_candidates(text: str) -> dict:
    chunks = split_by_level_2_headers(text)

    oversized_chunks = [
        index + 1 for index, chunk in enumerate(chunks)
        if is_chunk_too_large(chunk)
    ]

    return {
        "chunk_count": len(chunks),
        "oversized_chunks": oversized_chunks,
        "has_oversized_chunks": len(oversized_chunks) > 0,
    }
```

Chunk Metadata 예시:

```python
{
    "file_name": "Python_for_AI_Automation_Part10_RAG_Document_Automation_Agent_Tool_Testing.md",
    "title": "Agent Tool Script",
    "section": "Agent Tool Script Role",
    "keywords": ["Agent Tool", "Tool Input", "Tool Output", "JSON Result"]
}
```

---

### [FAQ]

Q. Chunk Preparation Validation은 왜 필요해?

A. RAG 문서가 검색 가능한 독립 단위로 잘 분리될 수 있는지 확인하기 위해 필요하다.

Q. 좋은 Chunk 조건은 무엇이야?

A. 하나의 개념, 명확한 제목, 독립 검색 가능성, 깨지지 않은 Code Block이다.

Q. 너무 긴 Chunk는 왜 문제야?

A. Retrieval 정확도가 떨어지고 핵심 정보가 희석될 수 있기 때문이다.

Q. FAQ Chunk는 왜 중요해?

A. 실제 사용자 질문과 문서 내용을 직접 연결해 Retrieval Matching을 강화하기 때문이다.

Q. Chunk Metadata에는 무엇을 넣으면 좋아?

A. `file_name`, `title`, `section`, `keywords`, `part_number` 같은 정보를 넣으면 검색 결과 추적에 유리하다.

---

# 9. Agent Tool Script

## 9.1 Agent Tool Script Role

### [개념]

Agent Tool Script는 AI Agent가 특정 작업을 수행하기 위해 호출할 수 있는 Python 자동화 도구이다.

Python for AI Automation에서 Agent Tool Script는 입력 검증, 작업 실행, 구조화된 출력, 오류 처리, 재현 가능한 실행을 갖춰야 한다.

Part08의 `ToolOutput` 표준 구조와 Part09의 CLI JSON 출력 구조를 함께 적용하면 Agent Tool Runner가 결과를 안정적으로 해석할 수 있다.

기본 Flow:

```text
Agent Request
→ Validate Tool Input
→ Execute Python Tool
→ Build Structured Output
→ Return JSON Result
```

---

### [핵심]

- Agent Tool은 입력과 출력이 명확해야 한다.
- Tool Input은 검증해야 한다.
- Tool Output은 JSON 호환 dict가 좋다.
- 실패 시 `status`, `result`, `error`를 반환한다.
- `status`는 `success`, `error`, `partial_success`로 통일한다.
- 같은 입력에는 같은 결과를 반환하는 것이 좋다.
- 위험 작업은 dry-run을 지원한다.
- 파일 삭제, 덮어쓰기, Secret 출력은 제한한다.
- 예외 발생 시 구조화된 실패 결과를 반환한다.
- 최상위 Tool Boundary에서만 마지막 안전망으로 `Exception` catch를 사용할 수 있다.

---

### [실무]

Tool Input 검증:

```python
from pathlib import Path

def validate_tool_input(data: dict) -> Path:
    file_path = data.get("file_path")

    if not file_path:
        raise ValueError("file_path is required")

    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(f"File not found: {path}")

    return path
```

Tool Output 생성:

```python
from typing import Literal

Status = Literal["success", "error", "partial_success"]

def build_tool_output(
    status: Status,
    result: dict | None,
    error: str | None,
) -> dict:
    return {
        "status": status,
        "result": result,
        "error": error,
    }
```

문서 검증 Tool:

```python
def run_document_validation_tool(input_data: dict) -> dict:
    try:
        path = validate_tool_input(input_data)
        text = path.read_text(encoding="utf-8")

        result = {
            "file_name": path.name,
            "missing_sections": find_missing_sections(text, REQUIRED_SECTIONS),
            "has_retrieval_queries": has_retrieval_queries(text),
            "has_unclosed_code_block": has_unclosed_code_block(text),
        }

        return build_tool_output(
            status="success",
            result=result,
            error=None,
        )

    except (ValueError, FileNotFoundError, UnicodeDecodeError) as error:
        return build_tool_output(
            status="error",
            result=None,
            error=str(error),
        )
```

---

### [FAQ]

Q. Agent Tool Script는 무엇이야?

A. AI Agent가 특정 작업을 수행하기 위해 호출할 수 있는 Python 자동화 도구이다.

Q. Agent Tool Input은 왜 검증해야 해?

A. 잘못된 입력으로 파일 오류, 보안 문제, 잘못된 결과가 발생할 수 있기 때문이다.

Q. Agent Tool Output은 어떤 구조가 좋아?

A. `status`, `result`, `error`를 포함한 JSON 호환 dict 구조가 좋다.

Q. Agent Tool Script에서 위험 작업은 어떻게 보호해?

A. dry-run, confirm, overwrite 옵션을 두고 제한된 경로에서만 실행되게 한다.

Q. Agent Tool Output status는 어떻게 통일해?

A. `success`, `error`, `partial_success`로 통일하는 것이 좋다.

---

## 9.2 Deterministic Output and Idempotency

### [개념]

Deterministic Output은 같은 입력에 대해 같은 출력을 반환하는 특성이다.

Idempotency는 같은 작업을 여러 번 실행해도 결과가 불필요하게 달라지지 않는 특성이다.

Agent Tool Script는 Agent Workflow 안정성을 위해 Deterministic Output과 Idempotency를 고려해야 한다.

---

### [핵심]

- 같은 입력에는 같은 결과를 반환하는 것이 좋다.
- 현재 시간, 랜덤값, 외부 상태 의존을 최소화한다.
- 파일 수정 Tool은 반복 실행 결과를 고려해야 한다.
- 검증 Tool은 보통 Deterministic해야 한다.
- Report 생성은 동일 입력이면 동일 출력이 좋다.
- 위험 작업은 dry-run으로 사전 확인한다.
- 중복 실행 시 결과 파일 덮어쓰기 정책을 명확히 한다.
- Agent Workflow에서는 반복 호출 가능성을 항상 고려한다.

---

### [실무]

Deterministic 검증 Tool:

```python
def validate_text(text: str) -> dict:
    missing_sections = find_missing_sections(text, REQUIRED_SECTIONS)

    return {
        "is_valid": len(missing_sections) == 0,
        "missing_sections": missing_sections,
        "has_retrieval_queries": "# Retrieval Queries" in text,
    }
```

Idempotent 저장 정책:

```python
from pathlib import Path

def save_report(path: Path, content: str, overwrite: bool = True) -> None:
    if path.exists() and not overwrite:
        raise FileExistsError(f"File already exists: {path}")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
```

Dry-run Output:

```python
def build_dry_run_result(target_path: str, planned_action: str) -> dict:
    return {
        "status": "success",
        "mode": "dry_run",
        "target_path": target_path,
        "planned_action": planned_action,
        "changed": False,
    }
```

---

### [FAQ]

Q. Deterministic Output은 왜 중요해?

A. Agent가 같은 입력에 대해 예측 가능한 결과를 받아야 Workflow가 안정적이기 때문이다.

Q. Idempotency는 왜 중요해?

A. 같은 작업을 반복 실행해도 파일이나 결과가 불필요하게 달라지지 않아야 하기 때문이다.

Q. 문서 검증 Tool은 Deterministic해야 해?

A. 그렇다. 같은 문서 입력이면 같은 검증 결과를 반환해야 한다.

Q. 파일 수정 Tool은 어떻게 안전하게 만들어?

A. dry-run, overwrite 정책, 백업, 변경 여부 표시를 포함하는 것이 좋다.

---

# 10. Testing Basics

## 10.1 Testing Role

### [개념]

Testing은 Python 자동화 코드가 기대한 대로 동작하는지 검증하는 작업이다.

Python for AI Automation에서는 파일 처리, 문자열 전처리, JSON 변환, Markdown 검증, Agent Tool Output을 테스트해야 한다.

기본 Flow:

```text
Function
→ Test Input
→ Execute
→ Assert Expected Output
→ Pass / Fail
```

---

### [핵심]

- 자동화 스크립트도 테스트가 필요하다.
- Pure Function은 테스트하기 쉽다.
- 파일 처리 함수는 임시 파일로 테스트한다.
- API 호출은 Mocking을 고려한다.
- Agent Tool Output 구조를 테스트한다.
- 위험 작업은 실제 파일 삭제 없이 테스트한다.
- 테스트는 핵심 로직부터 작성한다.
- 성공 케이스와 실패 케이스를 모두 테스트한다.

---

### [실무]

테스트 대상:

- `find_missing_sections`
- `has_retrieval_queries`
- `has_unclosed_code_block`
- `validate_file_name`
- `build_tool_output`
- `validate_tool_input`
- `scan_markdown_files`
- `save_report`
- `parse_args`

단순 테스트 예시:

```python
def test_has_retrieval_queries():
    text = "# Title\n\n# Retrieval Queries\n\nQ. 질문\nA. 답변"

    assert has_retrieval_queries(text) is True
```

누락 섹션 테스트:

```python
def test_find_missing_sections():
    text = "### [개념]\n### [핵심]"

    missing_sections = find_missing_sections(text, REQUIRED_SECTIONS)

    assert "### [실무]" in missing_sections
    assert "### [FAQ]" in missing_sections
```

ToolOutput 테스트:

```python
def test_build_tool_output_success():
    output = build_tool_output(
        status="success",
        result={"is_valid": True},
        error=None,
    )

    assert output["status"] == "success"
    assert output["result"]["is_valid"] is True
    assert output["error"] is None
```

---

### [FAQ]

Q. Python 자동화 코드도 테스트해야 해?

A. 해야 한다. 파일 처리, 문서 검증, API 응답 처리 오류가 실제 자동화 실패로 이어질 수 있기 때문이다.

Q. 어떤 함수부터 테스트하면 좋아?

A. 문자열 처리, 섹션 검사, Retrieval Queries 검사, Tool Output 생성 같은 Pure Function부터 테스트한다.

Q. 파일 처리 테스트는 어떻게 해?

A. 임시 파일을 만들어 읽기, 쓰기, 검증 로직을 테스트한다.

Q. API 호출 테스트는 어떻게 해?

A. 실제 API를 매번 호출하지 말고 Mocking을 고려한다.

Q. Agent Tool Output 테스트에서는 무엇을 봐야 해?

A. `status`, `result`, `error` 구조와 성공/실패 상태를 확인해야 한다.

---

# 11. pytest Basics

## 11.1 pytest Role

### [개념]

pytest는 Python 테스트를 간단하게 작성하고 실행할 수 있는 외부 테스트 프레임워크이다.

Python for AI Automation에서는 RAG 문서 검증 함수, 파일 처리 함수, Agent Tool Script의 결과 구조를 테스트하는 데 사용할 수 있다.

---

### [핵심]

- pytest는 외부 패키지이다.
- 테스트 파일명은 보통 `test_*.py` 형식을 사용한다.
- 테스트 함수명은 `test_`로 시작한다.
- `assert`로 기대 결과를 검증한다.
- `tmp_path` fixture로 임시 파일 테스트를 할 수 있다.
- 예외 발생은 `pytest.raises`로 테스트한다.
- 테스트는 빠르고 독립적이어야 한다.
- 실제 RAG 원본 파일을 수정하지 않아야 한다.

---

### [실무]

설치:

```bash
python -m pip install pytest
```

실행:

```bash
python -m pytest
```

테스트 파일 구조:

```text
tests
├ test_markdown_validator.py
├ test_file_utils.py
└ test_agent_tool.py
```

pytest 기본 테스트:

```python
def test_build_tool_output_success():
    output = build_tool_output(
        status="success",
        result={"is_valid": True},
        error=None,
    )

    assert output["status"] == "success"
    assert output["result"]["is_valid"] is True
    assert output["error"] is None
```

예외 테스트:

```python
import pytest

def test_validate_chunk_size_raises_error():
    with pytest.raises(ValueError):
        validate_chunk_size(0)
```

---

### [FAQ]

Q. pytest는 무엇이야?

A. Python 테스트를 작성하고 실행하기 위한 외부 테스트 프레임워크이다.

Q. pytest는 표준 라이브러리야?

A. 아니다. 별도 설치가 필요한 외부 패키지이다.

Q. pytest 테스트 함수명은 어떻게 작성해?

A. `test_`로 시작하는 함수명으로 작성한다.

Q. pytest 실행 명령은 무엇이야?

A. `python -m pytest`를 사용한다.

---

## 11.2 Temporary File Test

### [개념]

Temporary File Test는 실제 프로젝트 파일을 건드리지 않고 임시 파일과 임시 폴더를 사용해 파일 처리 로직을 검증하는 테스트 방식이다.

pytest에서는 `tmp_path` fixture를 사용할 수 있다.

---

### [핵심]

- 실제 RAG 원본 문서를 테스트 중 수정하지 않는다.
- `tmp_path`는 임시 폴더 Path를 제공한다.
- 임시 파일을 만들고 읽기/쓰기 함수를 테스트한다.
- 테스트 종료 후 임시 파일은 정리된다.
- 파일 삭제, 덮어쓰기 테스트는 임시 파일에서 수행한다.
- 자동화 파일 처리 함수 테스트에 적합하다.

---

### [실무]

임시 Markdown 파일 테스트:

```python
def test_read_markdown_file(tmp_path):
    path = tmp_path / "example.md"
    path.write_text("# Title\n\n### [FAQ]\n\nQ. 질문\nA. 답변", encoding="utf-8")

    text = path.read_text(encoding="utf-8")

    assert "# Title" in text
    assert "### [FAQ]" in text
```

Markdown 스캔 테스트:

```python
def test_scan_markdown_files(tmp_path):
    (tmp_path / "part01.md").write_text("# Part01", encoding="utf-8")
    (tmp_path / "part02.txt").write_text("text", encoding="utf-8")

    files = scan_markdown_files(tmp_path)

    assert len(files) == 1
    assert files[0].name == "part01.md"
```

저장 함수 테스트:

```python
def test_save_report(tmp_path):
    output_path = tmp_path / "reports" / "result.md"

    save_report(output_path, "# Result")

    assert output_path.exists()
    assert output_path.read_text(encoding="utf-8") == "# Result"
```

---

### [FAQ]

Q. tmp_path는 무엇이야?

A. pytest가 제공하는 임시 폴더 Path fixture이다.

Q. 파일 처리 테스트에 tmp_path를 쓰는 이유는?

A. 실제 프로젝트 파일을 수정하지 않고 안전하게 테스트하기 위해 사용한다.

Q. 임시 파일은 직접 삭제해야 해?

A. 보통 pytest가 테스트 종료 후 정리한다.

Q. 파일 삭제 테스트도 tmp_path에서 해야 해?

A. 그렇다. 실제 파일 삭제 위험을 피하기 위해 임시 파일에서 테스트한다.

---

# 12. Mocking Basics

## 12.1 Mocking Role

### [개념]

Mocking은 외부 API, 파일 시스템, 시간, 환경변수 같은 외부 의존성을 가짜 객체나 가짜 응답으로 대체해 테스트하는 방식이다.

Python for AI Automation에서는 API 호출 테스트, Agent Tool 외부 의존성 테스트, 실패 상황 재현에 유용하다.

---

### [핵심]

- 실제 API를 테스트마다 호출하지 않는다.
- Mock으로 성공 응답과 실패 응답을 재현한다.
- Timeout, HTTPError 같은 오류 상황을 테스트할 수 있다.
- 환경변수도 Mock 또는 monkeypatch로 테스트할 수 있다.
- Mocking은 외부 의존성을 줄여 테스트를 빠르고 안정적으로 만든다.
- 과도한 Mocking은 실제 동작과 차이를 만들 수 있다.
- Agent Tool Input / Output 자체는 Mock 없이 직접 테스트하는 것이 좋다.

---

### [실무]

환경변수 테스트:

```python
def test_get_required_env(monkeypatch):
    monkeypatch.setenv("LLM_API_KEY", "test-key")

    value = get_required_env("LLM_API_KEY")

    assert value == "test-key"
```

환경변수 누락 테스트:

```python
import pytest

def test_get_required_env_missing(monkeypatch):
    monkeypatch.delenv("LLM_API_KEY", raising=False)

    with pytest.raises(ValueError):
        get_required_env("LLM_API_KEY")
```

API Client는 실제 API 호출 대신 응답 객체를 Mocking할 수 있다.

```text
API Function
→ Mock Response
→ Validate Success Path
→ Mock Error
→ Validate Error Path
```

---

### [FAQ]

Q. Mocking은 왜 필요해?

A. 실제 API나 외부 시스템에 의존하지 않고 빠르고 안정적인 테스트를 만들기 위해 필요하다.

Q. API 테스트에서 실제 API를 호출하면 안 돼?

A. 매번 호출하는 것은 권장하지 않는다. 비용, 속도, 네트워크 상태, Rate Limit 문제가 생길 수 있다.

Q. 환경변수 테스트는 어떻게 해?

A. pytest의 monkeypatch로 환경변수를 설정하거나 제거해 테스트할 수 있다.

Q. Mocking을 너무 많이 쓰면 문제야?

A. 실제 동작과 테스트가 멀어질 수 있으므로 핵심 외부 의존성에만 적절히 사용한다.

---

# 13. Integrated RAG Document Checker

## 13.1 Integrated Checker Structure

### [개념]

Integrated RAG Document Checker는 Markdown 파일 스캔, 문서 읽기, 필수 섹션 검사, FAQ 검사, Retrieval Queries 검사, Code Block 검사, 결과 리포트 생성을 하나의 자동화 흐름으로 연결한 구조이다.

이 구조는 Python for AI Automation Domain의 최종 실무 패턴이다.

---

### [핵심]

- 입력은 RAG 문서 폴더이다.
- 출력은 검증 결과 JSON 또는 Markdown Report이다.
- 각 검증 로직은 작은 함수로 분리한다.
- Batch 작업은 Partial Success를 지원한다.
- 실패 파일과 실패 원인을 기록한다.
- CLI Script 또는 Agent Tool Script로 실행할 수 있다.
- 테스트 가능한 Pure Function을 우선 분리한다.
- ToolOutput 구조는 Part08 기준으로 통일한다.
- CLI 실행은 Part09 기준으로 JSON stdout과 Exit Code를 제공한다.

---

### [실무]

통합 구조 예시:

```python
from pathlib import Path

REQUIRED_SECTIONS = ["### [개념]", "### [핵심]", "### [실무]", "### [FAQ]"]

def validate_document_text(text: str) -> dict:
    missing_sections = [
        section for section in REQUIRED_SECTIONS
        if section not in text
    ]

    return {
        "has_required_sections": len(missing_sections) == 0,
        "missing_sections": missing_sections,
        "has_retrieval_queries": "# Retrieval Queries" in text,
        "has_unclosed_code_block": has_unclosed_code_block(text),
    }


def validate_document_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    result = validate_document_text(text)

    is_valid = (
        result["has_required_sections"]
        and result["has_retrieval_queries"]
        and not result["has_unclosed_code_block"]
    )

    return {
        "file_name": path.name,
        "is_valid": is_valid,
        **result,
    }


def validate_rag_folder(base_dir: Path) -> dict:
    files = scan_markdown_files(base_dir)

    successes = []
    failures = []

    for file_path in files:
        try:
            successes.append(validate_document_file(file_path))
        except Exception as error:
            failures.append({
                "file_name": file_path.name,
                "error": str(error),
                "error_type": type(error).__name__,
            })

    status = "success"

    if successes and failures:
        status = "partial_success"
    elif failures:
        status = "error"

    return {
        "status": status,
        "summary": {
            "total_count": len(files),
            "success_count": len(successes),
            "failure_count": len(failures),
        },
        "successes": successes,
        "failures": failures,
    }
```

---

### [FAQ]

Q. Integrated RAG Document Checker는 무엇이야?

A. RAG 문서 폴더를 스캔하고 필수 구조를 자동 검증해 리포트를 만드는 Python 자동화 도구이다.

Q. 통합 Checker의 입력은 무엇이야?

A. Markdown RAG 문서가 들어 있는 폴더 또는 파일 경로이다.

Q. 통합 Checker의 출력은 무엇이 좋아?

A. Agent가 처리하기 쉬운 JSON 구조와 사람이 확인 가능한 Markdown Report가 좋다.

Q. 일부 파일만 실패하면 어떻게 해?

A. `partial_success` 상태로 성공 목록과 실패 목록을 분리해 반환하는 것이 좋다.

Q. Integrated Checker는 CLI와 Agent Tool 둘 다로 쓸 수 있어?

A. 가능하다. 핵심 검증 로직을 함수로 분리하고 CLI Wrapper와 Agent Tool Wrapper를 따로 두면 된다.

---

# 14. Testing Best Practice

## 14.1 Best Practice

### [개념]

Testing Best Practice는 Python 자동화 코드의 신뢰성을 보장하기 위해 테스트 대상을 분리하고, 외부 의존성을 줄이며, 위험 작업을 안전하게 검증하는 기준이다.

목표:

```text
Pure Function Test
→ Temporary File Test
→ Error Case Test
→ Agent Tool Output Test
→ CLI Exit Code Test
```

---

### [핵심]

- Pure Function을 먼저 테스트한다.
- 파일 처리는 `tmp_path`로 테스트한다.
- API 호출은 Mocking한다.
- 환경변수는 monkeypatch로 테스트한다.
- 성공 케이스와 실패 케이스를 모두 테스트한다.
- Agent Tool Output 구조를 테스트한다.
- 오류 메시지와 error_type을 테스트한다.
- CLI는 Exit Code와 출력 형식을 테스트한다.
- 테스트는 실제 RAG 원본 파일을 수정하지 않아야 한다.

---

### [실무]

권장 테스트 목록:

```text
test_find_missing_sections
test_has_retrieval_queries
test_has_unclosed_code_block
test_validate_file_name
test_scan_markdown_files
test_validate_document_text_success
test_validate_document_text_missing_sections
test_build_tool_output_success
test_build_tool_output_error
test_cli_invalid_input
```

Agent Tool Output 테스트:

```python
def test_document_validation_tool_success(tmp_path):
    path = tmp_path / "doc.md"
    path.write_text(
        "# Title\n\n### [개념]\n\n### [핵심]\n\n### [실무]\n\n### [FAQ]\n\nQ. 질문\nA. 답변\n\n# Retrieval Queries",
        encoding="utf-8",
    )

    output = run_document_validation_tool({
        "file_path": str(path),
    })

    assert output["status"] == "success"
    assert output["error"] is None
    assert output["result"]["has_retrieval_queries"] is True
```

실패 테스트:

```python
def test_document_validation_tool_file_not_found():
    output = run_document_validation_tool({
        "file_path": "missing.md",
    })

    assert output["status"] == "error"
    assert output["result"] is None
    assert "File not found" in output["error"]
```

---

### [FAQ]

Q. Testing Best Practice는 무엇이야?

A. Pure Function, 임시 파일, 실패 케이스, Agent Tool Output, CLI Exit Code를 안전하게 검증하는 기준이다.

Q. 성공 케이스만 테스트하면 돼?

A. 아니다. 실패 케이스와 예외 케이스도 테스트해야 한다.

Q. 실제 RAG 문서 파일로 테스트해도 돼?

A. 권장하지 않는다. tmp_path로 임시 파일을 만들어 테스트하는 것이 안전하다.

Q. Agent Tool Output 테스트에서 무엇을 확인해야 해?

A. `status`, `result`, `error` 구조와 성공/실패 상태를 확인해야 한다.

---

# 15. Final Best Practice

## 15.1 Python for AI Automation Final Pattern

### [개념]

Python for AI Automation Final Pattern은 Python 기본 문법, 파일 처리, JSON/CSV/YAML/Markdown 처리, API 호출, 예외 처리, 로깅, Type Hint, CLI, RAG 자동화, Agent Tool, Testing을 하나의 실무 자동화 구조로 연결하는 기준이다.

최종 목표:

```text
Readable Script
→ Safe Automation
→ Structured Output
→ RAG Quality Validation
→ Agent Tool Integration
→ Tested Workflow
```

---

### [핵심]

- Python 3.11+ 기준으로 작성한다.
- Python 3.12를 권장한다.
- `pathlib.Path`를 우선 사용한다.
- 파일 처리에는 UTF-8 encoding을 명시한다.
- API 호출에는 Timeout을 설정한다.
- API Key는 환경변수로 관리한다.
- 오류는 구체적으로 처리한다.
- 로그에는 Secret을 남기지 않는다.
- Type Hint로 Input / Output을 명확히 한다.
- dataclass 또는 TypedDict로 구조화된 데이터를 표현한다.
- CLI는 argparse로 작성한다.
- Agent Tool Output은 `status`, `result`, `error` 구조로 통일한다.
- RAG 문서는 필수 섹션과 Retrieval Queries를 검증한다.
- 테스트는 pytest로 작성한다.
- 위험 작업은 dry-run, confirm, backup을 고려한다.
- REQUIRED_SECTIONS는 Config 또는 Domain Rules에서 중앙 관리한다.
- Code Block 검증은 단순 Fence Count의 한계를 인지한다.

---

### [실무]

최종 자동화 구조:

```text
python_ai_automation
├ main.py
├ config.py
├ file_utils.py
├ markdown_validator.py
├ report_builder.py
├ agent_tool.py
├ requirements.txt
├ .env.example
├ .gitignore
└ tests
   ├ test_markdown_validator.py
   ├ test_file_utils.py
   └ test_agent_tool.py
```

최종 실행 Flow:

```text
CLI Input
→ Validate Arguments
→ Scan Markdown Files
→ Validate RAG Documents
→ Build JSON Result
→ Save Report
→ Print JSON Summary
→ Return Exit Code
```

최종 Agent Tool Flow:

```text
Agent Request
→ Validate Tool Input
→ Run Document Checker
→ Return Structured JSON
→ Agent Review / Fix
```

최종 검수 Checklist:

```text
- Python 3.11+ 기준
- pathlib 사용
- encoding 명시
- Type Hint 적용
- 환경변수 사용
- Timeout 설정
- 예외 처리 구체화
- logging 적용
- Secret 로그 금지
- CLI 인자 검증
- JSON stdout 지원
- Exit Code 반환
- Agent Tool Output 구조화
- RAG 필수 섹션 검사
- Retrieval Queries 검사
- FAQ Q/A 검사
- Code Block 검사
- Chunk 구조 검사
- pytest 테스트 작성
```

---

### [FAQ]

Q. Python for AI Automation의 최종 목표는 무엇이야?

A. Agent가 자동화 스크립트 작성, RAG 문서 검증, API 호출, Tool Script 실행, 코드 리뷰를 안정적으로 수행하게 하는 것이다.

Q. Python 자동화 최종 구조에서 가장 중요한 것은?

A. 안전한 파일 처리, 구조화된 출력, 명확한 오류 처리, 테스트 가능한 함수 분리이다.

Q. Agent Tool Output은 어떻게 통일해?

A. `status`, `result`, `error`를 기본 구조로 사용한다.

Q. RAG 문서 자동화에서 최종 검수 항목은?

A. 필수 섹션, FAQ Q/A, Retrieval Queries, Code Block, 파일명, Chunk 구조, 테스트 가능성이다.

Q. Part10이 Python for AI Automation에서 하는 역할은?

A. 앞선 Python 자동화 요소를 RAG 문서 검증과 Agent Tool 실행 구조로 통합하는 최종 실무 패턴 역할을 한다.

---

# Retrieval Queries

### [FAQ]

Q. Python RAG Document Automation은 무엇이야?
A. Markdown RAG 문서의 파일명, 필수 섹션, FAQ, Retrieval Queries, Code Block, Chunk 구조를 자동 검증하는 작업이다.

Q. Python으로 RAG 문서 검증을 하는 이유는?
A. 많은 Markdown 문서를 반복 검수하고 품질 리포트를 일관되게 만들 수 있기 때문이다.

Q. RAG 문서 자동화에서 가장 중요한 검사는?
A. 필수 섹션 존재 여부, FAQ Q/A 쌍, Retrieval Queries 존재 여부, Code Block 닫힘 여부이다.

Q. RAG 문서 검증 결과는 어떤 형태가 좋아?
A. Agent가 처리하기 쉬운 dict 또는 JSON 구조가 좋다.

Q. REQUIRED_SECTIONS는 어디에서 관리하는 게 좋아?
A. 실제 운영에서는 `config.py`, YAML Config, Domain Rules 중 하나에서 중앙 관리하는 것이 좋다.

Q. Markdown 파일 스캔은 어떻게 해?
A. `Path.rglob("*.md")`를 사용해 하위 폴더까지 Markdown 파일을 찾는다.

Q. Markdown 스캔 결과를 정렬해야 해?
A. 권장한다. Part01, Part02 순서처럼 처리 순서가 안정적이어야 리포트 비교가 쉽다.

Q. `.venv`나 `.git` 폴더도 스캔해야 해?
A. 보통 제외한다. RAG 문서 검증 대상이 아니며 불필요한 파일이 섞일 수 있기 때문이다.

Q. RAG 문서 파일명 규칙은 왜 중요해?
A. 문서 정렬, Part 연결, 검색 결과 식별, 유지보수성을 높이기 위해 중요하다.

Q. RAG 문서 Part 번호는 왜 두 자리로 써?
A. Part01, Part02, Part10 순서가 안정적으로 정렬되기 때문이다.

Q. RAG 문서 파일명 검사는 어떻게 해?
A. 정규식으로 Domain, Part 번호, Topic, `.md` 확장자를 검사할 수 있다.

Q. Part 번호 중복도 검사해야 해?
A. 권장한다. 중복 Part 번호는 문서 순서와 검색 결과 관리에 혼선을 줄 수 있다.

Q. RAG 문서 필수 섹션은 무엇이야?
A. `[개념]`, `[핵심]`, `[실무]`, `[FAQ]`이다.

Q. RAG 문서 필수 섹션 검사는 왜 필요해?
A. 모든 문서가 동일한 Retrieval 구조를 갖도록 보장하기 위해 필요하다.

Q. RAG 문서 누락 섹션은 어떻게 반환해?
A. `missing_sections` list로 반환하는 것이 좋다.

Q. RAG 문서 FAQ Validation은 왜 필요해?
A. FAQ는 실제 사용자 질문과 문서 검색 매칭을 강화하므로 Q/A 구조가 반드시 필요하다.

Q. RAG 문서 FAQ에 Q만 있어도 돼?
A. 안 된다. 반드시 Q와 A가 함께 있어야 한다.

Q. RAG 문서 FAQ 답변은 길어도 돼?
A. 권장하지 않는다. A는 짧고 명확하게 작성하는 것이 Retrieval에 유리하다.

Q. Code Block 내부 Q/A도 FAQ로 세야 해?
A. 아니다. 예제 텍스트일 수 있으므로 실제 FAQ 구조와 구분하는 것이 좋다.

Q. Retrieval Queries는 왜 필요해?
A. 실제 사용자 질문 패턴과 문서 내용을 연결해 검색 매칭을 강화하기 위해 필요하다.

Q. Retrieval Queries는 문서 어디에 있어야 해?
A. 문서 마지막에 두는 것이 좋다.

Q. Retrieval Queries가 없으면 어떻게 처리해?
A. 검증 실패로 보고 수정 대상에 포함한다.

Q. Retrieval Queries 내부에도 FAQ Q/A가 있어야 해?
A. 권장한다. 실제 검색 질문 패턴을 강화하기 위해 Q/A 구조를 포함하는 것이 좋다.

Q. Code Block Validation은 왜 필요해?
A. Code Block이 깨지면 Header 추출, Chunk 분리, Markdown 파싱에 문제가 생기기 때문이다.

Q. Code Block이 닫히지 않았는지 어떻게 검사해?
A. Fence 개수를 세고 홀수이면 닫히지 않은 것으로 판단할 수 있다.

Q. Code Block 내부 Header는 실제 Header야?
A. 아니다. Code Block 내부의 `#`는 코드나 예시 텍스트일 수 있다.

Q. Code Block 내부 Q/A를 FAQ로 세면 안 되는 이유는?
A. 예제 코드나 텍스트일 수 있으므로 실제 문서 FAQ 구조와 구분해야 한다.

Q. Fence Count 방식은 항상 정확해?
A. 아니다. 단순 검증에는 유용하지만 복잡한 Markdown에서는 오탐 가능성이 있어 Parser 사용도 고려한다.

Q. Chunk Preparation Validation은 왜 필요해?
A. RAG 문서가 검색 가능한 독립 단위로 잘 분리될 수 있는지 확인하기 위해 필요하다.

Q. 좋은 RAG Chunk 조건은 무엇이야?
A. 하나의 개념, 명확한 제목, 독립 검색 가능성, 깨지지 않은 Code Block이다.

Q. 너무 긴 Chunk는 왜 문제야?
A. Retrieval 정확도가 떨어지고 핵심 정보가 희석될 수 있기 때문이다.

Q. FAQ Chunk는 왜 중요해?
A. 실제 사용자 질문과 문서 내용을 직접 연결해 Retrieval Matching을 강화하기 때문이다.

Q. Chunk Metadata에는 무엇을 넣으면 좋아?
A. `file_name`, `title`, `section`, `keywords`, `part_number` 같은 정보를 넣으면 검색 결과 추적에 유리하다.

Q. Agent Tool Script는 무엇이야?
A. AI Agent가 특정 작업을 수행하기 위해 호출할 수 있는 Python 자동화 도구이다.

Q. Agent Tool Input은 왜 검증해야 해?
A. 잘못된 입력으로 파일 오류, 보안 문제, 잘못된 결과가 발생할 수 있기 때문이다.

Q. Agent Tool Output은 어떤 구조가 좋아?
A. `status`, `result`, `error`를 포함한 JSON 호환 dict 구조가 좋다.

Q. Agent Tool Script에서 위험 작업은 어떻게 보호해?
A. dry-run, confirm, overwrite 옵션을 두고 제한된 경로에서만 실행되게 한다.

Q. Agent Tool Output status는 어떻게 통일해?
A. `success`, `error`, `partial_success`로 통일하는 것이 좋다.

Q. Deterministic Output은 왜 중요해?
A. Agent가 같은 입력에 대해 예측 가능한 결과를 받아야 Workflow가 안정적이기 때문이다.

Q. Idempotency는 왜 중요해?
A. 같은 작업을 반복 실행해도 파일이나 결과가 불필요하게 달라지지 않아야 하기 때문이다.

Q. 문서 검증 Tool은 Deterministic해야 해?
A. 그렇다. 같은 문서 입력이면 같은 검증 결과를 반환해야 한다.

Q. 파일 수정 Tool은 어떻게 안전하게 만들어?
A. dry-run, overwrite 정책, 백업, 변경 여부 표시를 포함하는 것이 좋다.

Q. Python 자동화 코드도 테스트해야 해?
A. 해야 한다. 파일 처리, 문서 검증, API 응답 처리 오류가 실제 자동화 실패로 이어질 수 있기 때문이다.

Q. 어떤 Python 자동화 함수부터 테스트하면 좋아?
A. 문자열 처리, 섹션 검사, Retrieval Queries 검사, Tool Output 생성 같은 Pure Function부터 테스트한다.

Q. Python 파일 처리 테스트는 어떻게 해?
A. 임시 파일을 만들어 읽기, 쓰기, 검증 로직을 테스트한다.

Q. API 호출 테스트는 어떻게 해?
A. 실제 API를 매번 호출하지 말고 Mocking을 고려한다.

Q. Agent Tool Output 테스트에서는 무엇을 봐야 해?
A. `status`, `result`, `error` 구조와 성공/실패 상태를 확인해야 한다.

Q. pytest는 무엇이야?
A. Python 테스트를 작성하고 실행하기 위한 외부 테스트 프레임워크이다.

Q. pytest는 표준 라이브러리야?
A. 아니다. 별도 설치가 필요한 외부 패키지이다.

Q. pytest 테스트 함수명은 어떻게 작성해?
A. `test_`로 시작하는 함수명으로 작성한다.

Q. pytest 실행 명령은 무엇이야?
A. `python -m pytest`를 사용한다.

Q. tmp_path는 무엇이야?
A. pytest가 제공하는 임시 폴더 Path fixture이다.

Q. 파일 처리 테스트에 tmp_path를 쓰는 이유는?
A. 실제 프로젝트 파일을 수정하지 않고 안전하게 테스트하기 위해 사용한다.

Q. Mocking은 왜 필요해?
A. 실제 API나 외부 시스템에 의존하지 않고 빠르고 안정적인 테스트를 만들기 위해 필요하다.

Q. API 테스트에서 실제 API를 호출하면 안 돼?
A. 매번 호출하는 것은 권장하지 않는다. 비용, 속도, 네트워크 상태, Rate Limit 문제가 생길 수 있다.

Q. 환경변수 테스트는 어떻게 해?
A. pytest의 monkeypatch로 환경변수를 설정하거나 제거해 테스트할 수 있다.

Q. Integrated RAG Document Checker는 무엇이야?
A. RAG 문서 폴더를 스캔하고 필수 구조를 자동 검증해 리포트를 만드는 Python 자동화 도구이다.

Q. 통합 Checker의 입력은 무엇이야?
A. Markdown RAG 문서가 들어 있는 폴더 또는 파일 경로이다.

Q. 통합 Checker의 출력은 무엇이 좋아?
A. Agent가 처리하기 쉬운 JSON 구조와 사람이 확인 가능한 Markdown Report가 좋다.

Q. 일부 RAG 문서 파일만 실패하면 어떻게 해?
A. `partial_success` 상태로 성공 목록과 실패 목록을 분리해 반환하는 것이 좋다.

Q. Integrated Checker는 CLI와 Agent Tool 둘 다로 쓸 수 있어?
A. 가능하다. 핵심 검증 로직을 함수로 분리하고 CLI Wrapper와 Agent Tool Wrapper를 따로 두면 된다.

Q. Testing Best Practice는 무엇이야?
A. Pure Function, 임시 파일, 실패 케이스, Agent Tool Output, CLI Exit Code를 안전하게 검증하는 기준이다.

Q. 성공 케이스만 테스트하면 돼?
A. 아니다. 실패 케이스와 예외 케이스도 테스트해야 한다.

Q. 실제 RAG 문서 파일로 테스트해도 돼?
A. 권장하지 않는다. tmp_path로 임시 파일을 만들어 테스트하는 것이 안전하다.

Q. Python for AI Automation의 최종 목표는 무엇이야?
A. Agent가 자동화 스크립트 작성, RAG 문서 검증, API 호출, Tool Script 실행, 코드 리뷰를 안정적으로 수행하게 하는 것이다.

Q. Python 자동화 최종 구조에서 가장 중요한 것은?
A. 안전한 파일 처리, 구조화된 출력, 명확한 오류 처리, 테스트 가능한 함수 분리이다.

Q. RAG 문서 자동화에서 최종 검수 항목은?
A. 필수 섹션, FAQ Q/A, Retrieval Queries, Code Block, 파일명, Chunk 구조, 테스트 가능성이다.

Q. Part10이 Python for AI Automation에서 하는 역할은?
A. 앞선 Python 자동화 요소를 RAG 문서 검증과 Agent Tool 실행 구조로 통합하는 최종 실무 패턴 역할을 한다.
