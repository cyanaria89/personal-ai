# Python for AI Automation Part02 - Data Structure Processing

---

# 1. String Processing

## 1.1 String Basics

### [개념]

String Processing은 Python for AI Automation에서 텍스트 데이터를 정리하고 변환하는 핵심 처리 방식이다.

RAG Document Automation, Markdown Processing, API Response Processing, Log Processing에서는 대부분의 입력값이 문자열로 들어온다.

기본 Flow:

```text
Raw Text
→ Clean Text
→ Split Text
→ Transform Text
→ Validate Text
→ Output Text
```

---

### [핵심]

- `str`은 Python 문자열 자료형이다.
- Markdown 문서, JSON 값, CSV 값, API Response, 로그 메시지는 문자열 처리 대상이다.
- 문자열은 원본 훼손 가능성이 있으므로 처리 전 기준을 명확히 한다.
- RAG 문서 전처리에서는 Header, Section, Code Block, Retrieval Queries를 문자열 기준으로 검사한다.
- 문자열 처리 결과는 검색 품질과 Chunk 품질에 직접 영향을 준다.

---

### [실무]

2026 실무 기준 Python 자동화에서 문자열 처리는 다음 작업에 자주 사용된다.

- Markdown 제목 정리
- 파일명 규칙 검사
- Section Header 추출
- Code Block 포함 여부 검사
- Retrieval Queries 존재 여부 확인
- API Response Message 파싱
- 로그 메시지 생성
- CSV Cell 값 정리
- JSON 필드 값 검증

예시:

```python
title = "  # Python Basics  "
clean_title = title.strip().replace("#", "").strip()

print(clean_title)
```

출력:

```text
Python Basics
```

---

### [FAQ]

Q. Python 자동화에서 문자열 처리가 중요한 이유는?

A. Markdown 문서, API 응답, CSV 값, 로그 메시지, 설정값이 대부분 문자열로 처리되기 때문이다.

Q. RAG 문서에서 문자열 처리는 어디에 사용해?

A. Header 추출, 필수 섹션 검사, Retrieval Queries 검사, Code Block 보호, Chunk 분리에 사용한다.

Q. 문자열 처리에서 가장 주의할 점은?

A. 원본 텍스트를 의도하지 않게 훼손하지 않는 것이다.

Q. 문자열 처리는 검색 품질에 영향을 줘?

A. 그렇다. 제목, 섹션명, 키워드가 잘 정리되어야 Retrieval Matching 품질이 좋아진다.

---

## 1.2 strip, replace, split, join

### [개념]

`strip`, `replace`, `split`, `join`은 Python 문자열 처리에서 가장 자주 사용하는 기본 메서드이다.

```python
text = "  Python, RAG, Agent  "

clean_text = text.strip()
items = clean_text.split(",")
normalized_items = [item.strip() for item in items]
result = " | ".join(normalized_items)
```

---

### [핵심]

- `strip()`은 앞뒤 공백을 제거한다.
- `replace(old, new)`는 문자열 일부를 다른 문자열로 바꾼다.
- `split(separator)`은 문자열을 나눈다.
- `join(iterable)`은 문자열 목록을 하나로 합친다.
- Markdown, CSV, Log, Config 처리에서 자주 사용된다.
- 처리 순서를 잘못 잡으면 원본 의미가 바뀔 수 있다.

---

### [실무]

Markdown Header 정리:

```python
raw_header = "  ## 1.1 Python Basics  "
clean_header = raw_header.strip().replace("#", "").strip()

print(clean_header)
```

CSV Cell 정리:

```python
raw_value = "  backend, ai, rag  "
tags = [tag.strip() for tag in raw_value.split(",")]

print(tags)
```

문서 키워드 생성:

```python
keywords = ["Python", "RAG", "Automation"]
query_text = " ".join(keywords)

print(query_text)
```

---

### [FAQ]

Q. strip은 언제 써?

A. 문자열 앞뒤 공백, 줄바꿈, 불필요한 여백을 제거할 때 사용한다.

Q. replace는 언제 써?

A. 특정 문자나 패턴을 다른 값으로 바꿀 때 사용한다.

Q. split은 언제 써?

A. 쉼표, 줄바꿈, 구분자 기준으로 문자열을 여러 조각으로 나눌 때 사용한다.

Q. join은 언제 써?

A. 문자열 목록을 하나의 문자열로 합칠 때 사용한다.

Q. replace를 많이 쓰면 문제가 될 수 있어?

A. 그렇다. 의도하지 않은 부분까지 바뀔 수 있으므로 변환 대상과 범위를 확인해야 한다.

---

## 1.3 startswith, endswith, in Keyword

### [개념]

`startswith`, `endswith`, `in`은 문자열에 특정 패턴이 포함되었는지 검사하는 메서드와 연산자이다.

```python
line = "# Retrieval Queries"

is_header = line.startswith("#")
is_md_file = "example.md".endswith(".md")
has_queries = "Retrieval Queries" in line
```

---

### [핵심]

- `startswith()`는 문자열 시작 패턴을 검사한다.
- `endswith()`는 문자열 끝 패턴을 검사한다.
- `in`은 특정 문자열 포함 여부를 검사한다.
- Markdown Header 검사에 `startswith("#")`를 사용할 수 있다.
- 파일 확장자 검사에 `endswith(".md")`를 사용할 수 있다.
- 필수 섹션 존재 여부 검사에 `in`을 사용할 수 있다.

---

### [실무]

Markdown Header 감지:

```python
line = "## 1.1 String Processing"

if line.startswith("#"):
    print("header")
```

파일 확장자 검사:

```python
file_name = "Python_Part02.md"

if file_name.endswith(".md"):
    print("markdown file")
```

필수 섹션 검사:

```python
document_text = "# Title\n\n### [FAQ]\n\nQ. 질문\nA. 답변"

has_faq = "### [FAQ]" in document_text
```

---

### [FAQ]

Q. startswith는 어디에 사용해?

A. Markdown Header, 특정 Prefix, 로그 레벨, 파일명 접두사 검사에 사용한다.

Q. endswith는 어디에 사용해?

A. 파일 확장자, 특정 Suffix, 백업 파일 여부 검사에 사용한다.

Q. in 키워드는 어디에 사용해?

A. 필수 섹션 존재 여부, 특정 키워드 포함 여부, 문자열 검증에 사용한다.

Q. Header 검사는 startswith만 쓰면 충분해?

A. 간단한 검사는 가능하지만 Code Block 내부 Header 오탐을 막으려면 추가 로직이 필요하다.

---

## 1.4 Regular Expression Basics

### [개념]

Regular Expression은 문자열에서 특정 패턴을 검색, 추출, 검증, 치환하기 위한 표현식이다.

Python에서는 `re` 모듈을 사용한다.

```python
import re

text = "Part01, Part02, Part03"
parts = re.findall(r"Part\d+", text)

print(parts)
```

---

### [핵심]

- 정규식은 복잡한 문자열 패턴 처리에 사용한다.
- 단순 처리는 `split`, `replace`, `startswith`를 우선한다.
- 파일명 규칙 검사에 정규식을 사용할 수 있다.
- Markdown Section 추출에 정규식을 사용할 수 있다.
- 과도하게 복잡한 정규식은 유지보수를 어렵게 만든다.

---

### [실무]

파일명 규칙 검사:

```python
import re

file_name = "Python_for_AI_Automation_Part02_Data_Structure_Processing.md"
pattern = r"^Python_for_AI_Automation_Part\d{2}_.+\.md$"

is_valid = bool(re.match(pattern, file_name))
print(is_valid)
```

섹션 제목 추출:

```python
import re

text = """
### [개념]
내용

### [핵심]
내용
"""

sections = re.findall(r"^### \[(.+?)\]", text, flags=re.MULTILINE)
print(sections)
```

---

### [FAQ]

Q. 정규식은 언제 사용해?

A. 파일명 규칙 검사, Section Header 추출, 특정 패턴 검색처럼 단순 문자열 메서드로 부족할 때 사용한다.

Q. 모든 문자열 처리를 정규식으로 해도 돼?

A. 아니다. 단순 처리는 `strip`, `split`, `replace`, `in`을 우선 사용한다.

Q. 정규식에서 가장 주의할 점은?

A. 너무 복잡하게 작성하면 Agent와 개발자가 이해하기 어렵고 유지보수가 어려워진다.

Q. Markdown Header 추출에 정규식을 써도 돼?

A. 가능하다. 단 Code Block 내부의 `#`를 Header로 오인하지 않도록 주의해야 한다.

---

# 2. List Processing

## 2.1 List Basics

### [개념]

List는 순서가 있는 여러 값을 저장하는 Python Collection Data Type이다.

RAG Document Automation에서는 파일 목록, 섹션 목록, 검증 결과 목록, Chunk 목록을 list로 관리한다.

```python
files = ["part01.md", "part02.md", "part03.md"]
```

---

### [핵심]

- list는 순서를 유지한다.
- list는 값을 추가, 수정, 삭제할 수 있다.
- 여러 파일을 순차 처리할 때 적합하다.
- API Response의 배열 데이터는 list로 처리된다.
- RAG Chunk 목록도 list로 표현할 수 있다.

---

### [실무]

Markdown 파일 목록:

```python
md_files = [
    "Python_for_AI_Automation_Part01_Foundation.md",
    "Python_for_AI_Automation_Part02_Data_Structure_Processing.md",
]
```

검증 결과 목록:

```python
results = [
    {"file_name": "part01.md", "is_valid": True},
    {"file_name": "part02.md", "is_valid": False},
]
```

Chunk 목록:

```python
chunks = [
    {"title": "String Processing", "text": "내용"},
    {"title": "List Processing", "text": "내용"},
]
```

---

### [FAQ]

Q. list는 자동화에서 어디에 많이 사용해?

A. 파일 목록, 문서 목록, API 결과 목록, Chunk 목록, 검증 결과 목록에 사용한다.

Q. list는 순서가 있어?

A. 있다. 입력 순서가 유지된다.

Q. list 안에 dict를 넣어도 돼?

A. 가능하다. 문서 메타데이터나 검증 결과 목록을 표현할 때 자주 사용한다.

Q. RAG Chunk 목록은 list로 관리해도 돼?

A. 그렇다. Chunk 순서와 메타데이터를 함께 관리하기 좋다.

---

## 2.2 append, extend, remove

### [개념]

`append`, `extend`, `remove`는 list 값을 추가하거나 제거하는 기본 메서드이다.

```python
files = []

files.append("part01.md")
files.extend(["part02.md", "part03.md"])
files.remove("part02.md")
```

---

### [핵심]

- `append(value)`는 값을 하나 추가한다.
- `extend(values)`는 여러 값을 펼쳐서 추가한다.
- `remove(value)`는 해당 값을 제거한다.
- `append(list)`는 list 자체를 하나의 값으로 추가한다.
- `extend(list)`는 list 내부 값을 각각 추가한다.

---

### [실무]

검증 결과 추가:

```python
results = []

results.append({
    "file_name": "part01.md",
    "is_valid": True,
})
```

파일 목록 병합:

```python
backend_docs = ["sql.md", "java.md"]
ai_docs = ["python.md", "rag.md"]

all_docs = []
all_docs.extend(backend_docs)
all_docs.extend(ai_docs)

print(all_docs)
```

잘못된 append 사용:

```python
all_docs = []
all_docs.append(backend_docs)

print(all_docs)
```

결과:

```text
[['sql.md', 'java.md']]
```

---

### [FAQ]

Q. append와 extend 차이는?

A. append는 값을 하나 추가하고, extend는 여러 값을 펼쳐서 추가한다.

Q. list에 dict를 append해도 돼?

A. 가능하다. 검증 결과나 메타데이터를 추가할 때 자주 사용한다.

Q. remove는 안전해?

A. 값이 없으면 ValueError가 발생하므로 제거 전 포함 여부를 확인하는 것이 좋다.

Q. append로 list를 넣으면 어떻게 돼?

A. list 내부 값이 아니라 list 자체가 하나의 요소로 추가된다.

---

## 2.3 List Comprehension

### [개념]

List Comprehension은 list를 간결하게 생성하거나 변환하는 Python 문법이다.

```python
files = ["part01.md", "part02.txt", "part03.md"]

md_files = [file for file in files if file.endswith(".md")]
```

---

### [핵심]

- list 변환과 필터링을 짧게 작성할 수 있다.
- 간단한 조건 처리에 적합하다.
- 너무 복잡한 comprehension은 가독성을 낮춘다.
- RAG 문서 목록 필터링에 자주 사용된다.
- 문서 메타데이터 추출에도 사용할 수 있다.

---

### [실무]

Markdown 파일만 필터링:

```python
files = ["part01.md", "part02.txt", "part03.md"]

md_files = [file for file in files if file.endswith(".md")]
print(md_files)
```

문서 제목 목록 추출:

```python
documents = [
    {"title": "Python", "domain": "AI"},
    {"title": "Spring Boot", "domain": "Backend"},
]

titles = [doc["title"] for doc in documents]
print(titles)
```

누락 섹션 추출:

```python
required_sections = ["[개념]", "[핵심]", "[실무]", "[FAQ]"]
document_text = "### [개념]\n### [핵심]"

missing_sections = [
    section for section in required_sections
    if section not in document_text
]

print(missing_sections)
```

---

### [FAQ]

Q. List Comprehension은 언제 써?

A. list에서 값을 변환하거나 특정 조건에 맞는 값만 필터링할 때 사용한다.

Q. List Comprehension이 항상 좋은가?

A. 아니다. 조건이 복잡하면 일반 for 문으로 분리하는 것이 좋다.

Q. 누락 섹션 검사에 List Comprehension을 쓸 수 있어?

A. 가능하다. 필수 섹션 중 문서에 없는 항목만 추출할 수 있다.

Q. Agent가 이해하기 좋은 List Comprehension은?

A. 한 줄 또는 짧은 여러 줄로 읽히는 단순한 변환과 필터링이다.

---

## 2.4 Sorting List

### [개념]

Sorting은 list 값을 특정 기준에 따라 정렬하는 처리이다.

Python에서는 `sorted()` 또는 `list.sort()`를 사용한다.

```python
files = ["part10.md", "part02.md", "part01.md"]

sorted_files = sorted(files)
```

---

### [핵심]

- `sorted(list)`는 정렬된 새 list를 반환한다.
- `list.sort()`는 원본 list를 직접 정렬한다.
- 정렬 기준은 `key`로 지정할 수 있다.
- 문서 처리 순서를 보장하려면 파일명 정렬이 중요하다.
- Part 문서는 Part 번호 기준으로 정렬해야 한다.

---

### [실무]

파일명 정렬:

```python
files = ["Part03.md", "Part01.md", "Part02.md"]

sorted_files = sorted(files)
print(sorted_files)
```

dict list 정렬:

```python
documents = [
    {"file_name": "part02.md", "score": 91},
    {"file_name": "part01.md", "score": 98},
]

sorted_docs = sorted(
    documents,
    key=lambda doc: doc["score"],
    reverse=True,
)

print(sorted_docs)
```

Part 번호 기준 정렬:

```python
import re

files = ["Part10.md", "Part02.md", "Part01.md"]

def extract_part_number(file_name: str) -> int:
    match = re.search(r"Part(\d+)", file_name)
    return int(match.group(1)) if match else 0

sorted_files = sorted(files, key=extract_part_number)
print(sorted_files)
```

---

### [FAQ]

Q. sorted와 sort 차이는?

A. sorted는 새 list를 반환하고, sort는 원본 list를 직접 변경한다.

Q. 문서 자동화에서 정렬이 중요한 이유는?

A. Part01, Part02, Part03 순서를 보장해야 처리 결과와 보고서가 안정적이기 때문이다.

Q. dict list는 어떻게 정렬해?

A. `key=lambda item: item["field"]` 형태로 정렬 기준을 지정한다.

Q. Part10이 Part2보다 먼저 나오는 문제는 어떻게 해결해?

A. 파일명에서 숫자를 추출해 숫자 기준으로 정렬한다.

---

# 3. Dict Processing

## 3.1 Dict Basics

### [개념]

Dict는 key-value 구조로 데이터를 저장하는 Python Collection Data Type이다.

JSON Object, API Response, Config, Document Metadata, Validation Result는 대부분 dict로 표현된다.

```python
metadata = {
    "file_name": "part01.md",
    "domain": "Python for AI Automation",
    "is_valid": True,
}
```

---

### [핵심]

- dict는 key-value 구조이다.
- key로 값을 조회한다.
- JSON Object는 Python dict로 변환된다.
- 설정값, 메타데이터, 검증 결과 표현에 적합하다.
- Agent Tool Output은 dict 또는 JSON 형태가 좋다.

---

### [실무]

문서 메타데이터:

```python
document_meta = {
    "file_name": "Python_for_AI_Automation_Part02_Data_Structure_Processing.md",
    "title": "Python for AI Automation Part02 - Data Structure Processing",
    "domain": "Python for AI Automation",
    "level": 2,
}
```

검증 결과:

```python
validation_result = {
    "file_name": "part02.md",
    "is_valid": True,
    "missing_sections": [],
    "has_retrieval_queries": True,
}
```

Agent Tool Output:

```python
tool_output = {
    "status": "success",
    "result": validation_result,
    "error": None,
}
```

---

### [FAQ]

Q. dict는 자동화에서 왜 중요해?

A. JSON 데이터, API Response, 설정값, 문서 메타데이터, 검증 결과가 대부분 key-value 구조이기 때문이다.

Q. dict는 JSON과 같은 거야?

A. Python 내부에서는 dict로 다루고, 파일이나 API 전송 시 JSON 문자열로 변환한다.

Q. Agent Tool Output은 dict로 만들어도 돼?

A. 좋다. dict는 JSON으로 변환하기 쉽고 Agent가 처리하기 좋다.

Q. dict key는 어떻게 작성하는 게 좋아?

A. `file_name`, `is_valid`, `missing_sections`처럼 의미가 명확한 snake_case를 권장한다.

---

## 3.2 get, update, keys, values, items

### [개념]

dict 메서드는 key-value 데이터를 안전하게 조회하고 수정하는 데 사용한다.

```python
config = {
    "model": "qwen2.5",
    "temperature": 0.2,
}

model = config.get("model")
config.update({"timeout": 30})
```

---

### [핵심]

- `dict["key"]`는 key가 없으면 `KeyError`가 발생한다.
- `dict.get("key")`는 key가 없어도 에러를 발생시키지 않는다.
- `update()`는 dict 값을 추가하거나 수정한다.
- `keys()`는 key 목록을 반환한다.
- `values()`는 value 목록을 반환한다.
- `items()`는 key-value 쌍을 반환한다.

---

### [실무]

안전한 값 조회:

```python
response = {
    "status": "success",
    "data": {"count": 3},
}

status = response.get("status")
error = response.get("error")

print(status)
print(error)
```

기본값 사용:

```python
config = {
    "timeout": 10,
}

timeout = config.get("timeout", 30)
retry_count = config.get("retry_count", 3)

print(timeout)
print(retry_count)
```

dict 순회:

```python
metadata = {
    "file_name": "part02.md",
    "domain": "Python",
}

for key, value in metadata.items():
    print(key, value)
```

---

### [FAQ]

Q. dict.get은 왜 사용해?

A. key가 없을 때 KeyError를 피하고 기본값을 지정할 수 있기 때문이다.

Q. dict["key"]는 언제 써?

A. 반드시 존재해야 하는 key를 조회할 때 사용한다.

Q. update는 언제 써?

A. 기존 dict에 새 값을 추가하거나 기존 값을 수정할 때 사용한다.

Q. items는 언제 써?

A. dict의 key와 value를 함께 순회할 때 사용한다.

---

## 3.3 Nested Dict

### [개념]

Nested Dict는 dict 안에 dict 또는 list가 들어간 중첩 구조이다.

API Response, LLM Response, RAG 문서 메타데이터는 중첩 dict 구조인 경우가 많다.

```python
response = {
    "status": "success",
    "data": {
        "file_name": "part02.md",
        "sections": ["[개념]", "[핵심]"],
    },
}
```

---

### [핵심]

- Nested Dict는 API Response 처리에서 자주 등장한다.
- 중첩 값 접근 시 key 존재 여부를 확인해야 한다.
- `get()`을 연속으로 사용하면 KeyError를 줄일 수 있다.
- 구조가 복잡하면 dataclass 또는 TypedDict를 고려한다.
- Agent Tool Output은 너무 깊은 중첩을 피하는 것이 좋다.

---

### [실무]

중첩 값 접근:

```python
response = {
    "status": "success",
    "data": {
        "document": {
            "file_name": "part02.md",
            "score": 98,
        }
    },
}

file_name = response.get("data", {}).get("document", {}).get("file_name")
print(file_name)
```

중첩 구조 검증:

```python
def extract_score(response: dict) -> int | None:
    document = response.get("data", {}).get("document", {})
    return document.get("score")
```

---

### [FAQ]

Q. Nested Dict는 어디에 많이 나와?

A. API Response, LLM Response, 설정 파일, 문서 메타데이터에서 자주 나온다.

Q. 중첩 dict 접근에서 가장 흔한 오류는?

A. 존재하지 않는 key에 접근해서 KeyError가 발생하는 것이다.

Q. 중첩 dict를 안전하게 조회하려면?

A. `get()`과 기본값 `{}`를 함께 사용한다.

Q. 중첩이 너무 깊으면 어떻게 해?

A. dataclass, TypedDict, 별도 변환 함수로 구조를 정리하는 것이 좋다.

---

# 4. Set and Tuple Processing

## 4.1 Set Processing

### [개념]

Set은 중복 없는 값을 저장하는 Python Collection Data Type이다.

필수 섹션 검사, 중복 제거, 포함 여부 검사에 유용하다.

```python
required_sections = {"[개념]", "[핵심]", "[실무]", "[FAQ]"}
found_sections = {"[개념]", "[핵심]"}

missing_sections = required_sections - found_sections
```

---

### [핵심]

- set은 중복 값을 허용하지 않는다.
- 순서는 보장하지 않는다.
- 포함 여부 검사가 빠르다.
- 차집합, 교집합, 합집합 연산이 가능하다.
- 필수 항목 누락 검사에 적합하다.

---

### [실무]

중복 제거:

```python
tags = ["Python", "RAG", "Python", "Agent"]
unique_tags = set(tags)

print(unique_tags)
```

필수 섹션 누락 검사:

```python
required_sections = {"[개념]", "[핵심]", "[실무]", "[FAQ]"}
found_sections = {"[개념]", "[핵심]", "[FAQ]"}

missing_sections = required_sections - found_sections
print(missing_sections)
```

교집합 검사:

```python
required_keywords = {"Python", "Automation", "RAG"}
document_keywords = {"Python", "Agent", "RAG"}

matched_keywords = required_keywords & document_keywords
print(matched_keywords)
```

---

### [FAQ]

Q. set은 언제 사용해?

A. 중복 제거, 포함 여부 검사, 필수 항목 누락 검사에 사용한다.

Q. set은 순서가 있어?

A. 순서를 보장하지 않는다.

Q. 필수 섹션 검사에 set을 써도 돼?

A. 좋다. 필수 섹션과 발견된 섹션의 차집합으로 누락 항목을 찾을 수 있다.

Q. set 결과를 JSON으로 바로 저장할 수 있어?

A. 아니다. JSON 저장 전 list로 변환해야 한다.

---

## 4.2 Tuple Processing

### [개념]

Tuple은 순서가 있고 변경할 수 없는 Python Collection Data Type이다.

고정된 값 묶음, 변경하지 않을 설정, 함수 반환값에 사용할 수 있다.

```python
position = (10, 20)
```

---

### [핵심]

- tuple은 순서가 있다.
- tuple은 생성 후 값을 변경할 수 없다.
- 변경되지 않아야 하는 값에 적합하다.
- 함수가 여러 값을 반환할 때 사용할 수 있다.
- list보다 불변성을 표현하기 좋다.

---

### [실무]

고정 설정:

```python
allowed_extensions = (".md", ".txt", ".json")

file_name = "example.md"

if file_name.endswith(allowed_extensions):
    print("allowed file")
```

함수 반환값:

```python
def split_file_name(file_name: str) -> tuple[str, str]:
    name, extension = file_name.rsplit(".", 1)
    return name, extension
```

---

### [FAQ]

Q. tuple은 언제 사용해?

A. 변경하지 않을 값 묶음이나 함수에서 여러 값을 반환할 때 사용한다.

Q. list와 tuple 차이는?

A. list는 변경 가능하고 tuple은 변경할 수 없다.

Q. 파일 확장자 검사에 tuple을 쓸 수 있어?

A. 가능하다. `endswith((".md", ".txt"))`처럼 사용할 수 있다.

Q. tuple은 JSON 저장에 적합해?

A. JSON으로 저장하면 배열로 변환되므로 의미상 list와 구분되지 않는다.

---

# 5. Data Structure Selection

## 5.1 list vs tuple vs dict vs set

### [개념]

Data Structure Selection은 처리 목적에 맞는 자료구조를 선택하는 기준이다.

AI Automation Script에서는 자료구조 선택이 코드 가독성, 안정성, Agent 이해도에 영향을 준다.

---

### [핵심]

| 자료구조 | 특징                 | 주요 사용                        |
| -------- | -------------------- | -------------------------------- |
| list     | 순서 있음, 변경 가능 | 파일 목록, 결과 목록, Chunk 목록 |
| tuple    | 순서 있음, 변경 불가 | 고정 값, 함수 반환값             |
| dict     | key-value 구조       | JSON, Config, Metadata, Result   |
| set      | 중복 없음, 순서 없음 | 중복 제거, 포함 검사, 누락 검사  |

---

### [실무]

목적별 선택:

```text
파일 목록 처리 → list
문서 메타데이터 → dict
검증 결과 → dict
필수 섹션 누락 검사 → set
고정 확장자 목록 → tuple
Chunk 목록 → list[dict]
Agent Tool Output → dict
```

예시:

```python
required_sections = {"[개념]", "[핵심]", "[실무]", "[FAQ]"}

document_result = {
    "file_name": "part02.md",
    "missing_sections": [],
    "is_valid": True,
}

chunk_list = [
    {"title": "String Processing", "text": "내용"},
    {"title": "Dict Processing", "text": "내용"},
]
```

---

### [FAQ]

Q. 파일 목록은 어떤 자료구조가 좋아?

A. 순서가 필요한 경우가 많으므로 list가 적합하다.

Q. 문서 메타데이터는 어떤 자료구조가 좋아?

A. key-value 구조인 dict가 적합하다.

Q. 필수 섹션 누락 검사는 어떤 자료구조가 좋아?

A. set을 사용하면 차집합으로 누락 항목을 쉽게 찾을 수 있다.

Q. Agent Tool Output은 어떤 자료구조가 좋아?

A. JSON 변환이 쉬운 dict가 적합하다.

---

# 6. Data Structure Best Practice

## 6.1 Safe Data Processing

### [개념]

Safe Data Processing은 list, dict, set, tuple을 사용할 때 오류와 원본 훼손을 줄이는 작성 기준이다.

자동화 스크립트는 반복 실행되므로 데이터 구조 처리 결과가 예측 가능해야 한다.

기본 Flow:

```text
Input Data
→ Validate Structure
→ Transform Data
→ Preserve Original When Needed
→ Return Structured Result
```

---

### [핵심]

- 원본 데이터 변경 여부를 의식한다.
- dict key 존재 여부를 확인한다.
- list 처리 순서를 보장한다.
- set은 순서가 필요 없는 경우에만 사용한다.
- JSON 저장 전 set은 list로 변환한다.
- 중첩 dict는 안전하게 조회한다.
- 복잡한 변환은 함수로 분리한다.
- Agent가 이해하기 쉬운 구조를 우선한다.

---

### [실무]

안전한 dict 조회:

```python
def get_file_name(result: dict) -> str | None:
    return result.get("file_name")
```

set을 JSON 저장용 list로 변환:

```python
missing_sections = {"[실무]", "[FAQ]"}

result = {
    "missing_sections": sorted(list(missing_sections)),
}
```

복잡한 변환 함수 분리:

```python
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

Q. 자동화 코드에서 원본 데이터 변경을 주의해야 하는 이유는?

A. 반복 실행 시 결과가 달라지거나 원본 문서가 훼손될 수 있기 때문이다.

Q. dict key 오류를 줄이려면?

A. `get()`을 사용하거나 필수 key 검증 함수를 둔다.

Q. set을 결과에 넣을 때 주의할 점은?

A. JSON 저장 전 list로 변환해야 한다.

Q. 복잡한 list/dict 처리는 어떻게 관리해?

A. 변환 함수를 별도로 만들고 입력과 출력을 명확히 한다.

---

# Retrieval Queries

### [FAQ]

Q. Python 문자열 처리는 왜 중요해?
A. Markdown 문서, API 응답, CSV 값, 로그 메시지, 설정값이 대부분 문자열로 처리되기 때문이다.

Q. Python에서 strip은 언제 사용해?
A. 문자열 앞뒤 공백, 줄바꿈, 불필요한 여백을 제거할 때 사용한다.

Q. Python에서 replace는 언제 사용해?
A. 특정 문자나 문자열을 다른 값으로 바꿀 때 사용한다.

Q. Python에서 split은 언제 사용해?
A. 쉼표, 줄바꿈, 구분자 기준으로 문자열을 여러 조각으로 나눌 때 사용한다.

Q. Python에서 join은 언제 사용해?
A. 문자열 목록을 하나의 문자열로 합칠 때 사용한다.

Q. Python에서 startswith는 어디에 사용해?
A. Markdown Header, Prefix, 로그 레벨, 파일명 접두사 검사에 사용한다.

Q. Python에서 endswith는 어디에 사용해?
A. 파일 확장자, Suffix, 백업 파일 여부 검사에 사용한다.

Q. Python에서 in 키워드는 어디에 사용해?
A. 필수 섹션 존재 여부, 특정 키워드 포함 여부, 문자열 검증에 사용한다.

Q. Python 정규식은 언제 사용해?
A. 파일명 규칙 검사, Section Header 추출, 특정 패턴 검색처럼 단순 문자열 메서드로 부족할 때 사용한다.

Q. Python에서 list는 언제 사용해?
A. 파일 목록, 문서 목록, API 결과 목록, Chunk 목록, 검증 결과 목록에 사용한다.

Q. Python list는 순서가 있어?
A. 있다. 입력 순서가 유지된다.

Q. Python list에 dict를 넣어도 돼?
A. 가능하다. 문서 메타데이터나 검증 결과 목록을 표현할 때 자주 사용한다.

Q. Python append와 extend 차이는?
A. append는 값을 하나 추가하고, extend는 여러 값을 펼쳐서 추가한다.

Q. Python List Comprehension은 언제 사용해?
A. list에서 값을 변환하거나 특정 조건에 맞는 값만 필터링할 때 사용한다.

Q. Python List Comprehension은 항상 좋은가?
A. 아니다. 조건이 복잡하면 일반 for 문이나 함수로 분리하는 것이 좋다.

Q. Python에서 sorted와 sort 차이는?
A. sorted는 정렬된 새 list를 반환하고, sort는 원본 list를 직접 변경한다.

Q. Python 문서 자동화에서 정렬이 중요한 이유는?
A. Part01, Part02, Part03 순서를 보장해야 처리 결과와 보고서가 안정적이기 때문이다.

Q. Python에서 dict는 언제 사용해?
A. JSON 데이터, API Response, 설정값, 문서 메타데이터, 검증 결과를 key-value 구조로 다룰 때 사용한다.

Q. Python dict는 JSON과 같은 거야?
A. Python 내부에서는 dict로 다루고 파일 저장이나 API 전송 시 JSON 문자열로 변환한다.

Q. Python dict.get은 왜 사용해?
A. key가 없을 때 KeyError를 피하고 기본값을 지정할 수 있기 때문이다.

Q. Python dict["key"]는 언제 사용해?
A. 반드시 존재해야 하는 key를 조회할 때 사용한다.

Q. Python update는 언제 사용해?
A. 기존 dict에 새 값을 추가하거나 기존 값을 수정할 때 사용한다.

Q. Python items는 언제 사용해?
A. dict의 key와 value를 함께 순회할 때 사용한다.

Q. Python Nested Dict는 어디에 많이 나와?
A. API Response, LLM Response, 설정 파일, 문서 메타데이터에서 자주 나온다.

Q. Python 중첩 dict를 안전하게 조회하려면?
A. `get()`과 기본값 `{}`를 함께 사용한다.

Q. Python set은 언제 사용해?
A. 중복 제거, 포함 여부 검사, 필수 항목 누락 검사에 사용한다.

Q. Python set은 순서가 있어?
A. 순서를 보장하지 않는다.

Q. Python 필수 섹션 검사에 set을 써도 돼?
A. 좋다. 필수 섹션과 발견된 섹션의 차집합으로 누락 항목을 찾을 수 있다.

Q. Python set을 JSON으로 바로 저장할 수 있어?
A. 아니다. JSON 저장 전 list로 변환해야 한다.

Q. Python tuple은 언제 사용해?
A. 변경하지 않을 값 묶음이나 함수에서 여러 값을 반환할 때 사용한다.

Q. Python list와 tuple 차이는?
A. list는 변경 가능하고 tuple은 변경할 수 없다.

Q. Python 파일 확장자 검사에 tuple을 쓸 수 있어?
A. 가능하다. `endswith((".md", ".txt"))`처럼 사용할 수 있다.

Q. Python 파일 목록은 어떤 자료구조가 좋아?
A. 순서가 필요한 경우가 많으므로 list가 적합하다.

Q. Python 문서 메타데이터는 어떤 자료구조가 좋아?
A. key-value 구조인 dict가 적합하다.

Q. Python 필수 섹션 누락 검사는 어떤 자료구조가 좋아?
A. set을 사용하면 차집합으로 누락 항목을 쉽게 찾을 수 있다.

Q. Python Agent Tool Output은 어떤 자료구조가 좋아?
A. JSON 변환이 쉬운 dict가 적합하다.

Q. Python 자동화에서 원본 데이터 변경을 주의해야 하는 이유는?
A. 반복 실행 시 결과가 달라지거나 원본 문서가 훼손될 수 있기 때문이다.

Q. Python dict key 오류를 줄이려면?
A. `get()`을 사용하거나 필수 key 검증 함수를 둔다.

Q. Python 복잡한 list/dict 처리는 어떻게 관리해?
A. 변환 함수를 별도로 만들고 입력과 출력을 명확히 한다.
