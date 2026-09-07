# Python for AI Automation Part05 - JSON CSV YAML Markdown Processing

---

# 1. Data File Processing Overview

## 1.1 JSON CSV YAML Markdown Role

### [개념]

JSON, CSV, YAML, Markdown은 Python for AI Automation에서 가장 자주 다루는 데이터 파일 형식이다.

AI Automation Script는 설정값, API Response 저장본, 문서 메타데이터, RAG 문서 본문, 검증 결과, 리포트를 다양한 파일 형식으로 읽고 저장한다.

Part05의 핵심은 **파일 기반 데이터 처리**이다.

Part06에서 다루는 JSON 검증은 **HTTP API Response 중심**이고, Part05의 JSON 검증은 **파일 기반 Config / Report / Tool Output 저장 구조 중심**이다.

기본 Flow:

```text
Input File
→ Read
→ Parse
→ Validate
→ Transform
→ Save
```

---

### [핵심]

- JSON은 Config, Report, Agent Tool Output 저장에 자주 사용된다.
- CSV는 표 형태 데이터, 문서 목록, 검증 결과, 메타데이터 관리에 사용된다.
- YAML은 사람이 직접 수정하는 설정 파일, 워크플로우 정의, 환경별 옵션 관리에 사용된다.
- Markdown은 RAG 문서 본문, Retrieval Queries, Agent Knowledge Document에 사용된다.
- 파일 처리 시 `encoding="utf-8"`을 명시한다.
- 외부 입력 파일은 구조 검증 후 처리한다.
- Agent Tool Output은 JSON 호환 dict 구조를 우선한다.
- 파일 형식별 목적을 혼동하지 않는다.

---

### [실무]

2026 실무 기준 Python 자동화에서는 파일 형식별 역할을 분리해 처리한다.

| 파일 형식 | 주요 사용                                        | Python 처리         |
| --------- | ------------------------------------------------ | ------------------- |
| JSON      | Config, Report, Tool Output, API Response 저장본 | `json`              |
| CSV       | Table Data, Metadata, Validation Report          | `csv`, `pandas`     |
| YAML      | Config, Workflow, Tool Settings                  | `yaml.safe_load`    |
| Markdown  | RAG Document, Prompt Rule, Report                | `read_text`, Parser |

사용 예시:

```text
RAG Document
→ Markdown Read
→ Section Validation
→ Metadata Extract
→ JSON Result
→ CSV Report
```

파일 기반 JSON과 API Response JSON의 역할 차이:

```text
Part05 JSON
→ Config File
→ Report File
→ Tool Output File
→ Local Validation Result

Part06 JSON
→ HTTP Response Body
→ API Error Response
→ Remote Service Result
→ Status Code 기반 처리
```

---

### [FAQ]

Q. Python 자동화에서 JSON은 어디에 사용해?

A. Config 파일, 검증 결과 저장, Agent Tool Output 저장, API Response 저장본에 사용한다.

Q. Python 자동화에서 CSV는 어디에 사용해?

A. 문서 목록, 메타데이터, 표 형태 검증 결과, 분석용 데이터 저장에 사용한다.

Q. Python 자동화에서 YAML은 어디에 사용해?

A. 설정 파일, 워크플로우 정의, 문서 생성 옵션, Agent 설정에 사용한다.

Q. Python 자동화에서 Markdown은 어디에 사용해?

A. RAG 문서, Prompt Rule, Domain Rules, 검증 리포트 작성에 사용한다.

Q. Part05 JSON과 Part06 JSON의 차이는?

A. Part05는 파일 기반 JSON Config / Report / Tool Output 저장 중심이고, Part06은 HTTP API Response 처리 중심이다.

Q. Agent Tool Output은 어떤 형식이 좋아?

A. JSON 변환이 쉬운 dict 구조가 좋다.

---

# 2. JSON Processing

## 2.1 JSON Basics

### [개념]

JSON은 key-value 구조와 배열을 표현하는 텍스트 기반 데이터 형식이다.

Python에서는 JSON Object를 `dict`, JSON Array를 `list`로 처리한다.

```json
{
  "file_name": "part05.md",
  "is_valid": true,
  "missing_sections": []
}
```

---

### [핵심]

- JSON은 Config, Report, Tool Output 저장에 적합하다.
- JSON Object는 Python `dict`로 변환된다.
- JSON Array는 Python `list`로 변환된다.
- JSON의 `true`, `false`, `null`은 Python에서 `True`, `False`, `None`으로 변환된다.
- Agent Tool Output은 JSON 호환 구조를 권장한다.
- JSON에는 `set`, `Path`, `datetime` 객체를 그대로 저장할 수 없다.
- JSON 저장 전 비직렬화 객체는 문자열, list, dict 등으로 변환한다.

---

### [실무]

Python dict:

```python
result = {
    "file_name": "Python_for_AI_Automation_Part05_JSON_CSV_YAML_Markdown_Processing.md",
    "is_valid": True,
    "missing_sections": [],
    "error": None,
}
```

JSON 변환 대상:

```text
dict → JSON Object
list → JSON Array
str → JSON String
int / float → JSON Number
bool → JSON Boolean
None → JSON null
```

Agent Tool Output 구조:

```python
tool_output = {
    "status": "success",
    "result": {
        "file_count": 10,
        "valid_count": 10,
    },
    "error": None,
}
```

비직렬화 객체 변환:

```python
from pathlib import Path

result = {
    "path": str(Path("docs/example.md")),
    "missing_sections": sorted(list({"[FAQ]", "# Retrieval Queries"})),
}
```

---

### [FAQ]

Q. JSON은 Python에서 어떤 타입으로 다뤄?

A. JSON Object는 dict, JSON Array는 list로 다룬다.

Q. JSON의 null은 Python에서 뭐야?

A. Python의 `None`으로 변환된다.

Q. JSON의 true와 false는 Python에서 뭐야?

A. Python의 `True`, `False`로 변환된다.

Q. Python set은 JSON으로 바로 저장돼?

A. 아니다. JSON 저장 전 list로 변환해야 한다.

Q. Path 객체는 JSON으로 바로 저장돼?

A. 아니다. `str(path)`로 문자열 변환 후 저장해야 한다.

---

## 2.2 json.load and json.loads

### [개념]

`json.load()`와 `json.loads()`는 JSON 데이터를 Python 객체로 변환하는 함수이다.

`json.load()`는 파일 객체에서 JSON을 읽고, `json.loads()`는 JSON 문자열을 읽는다.

---

### [핵심]

- `json.load(file)`은 JSON 파일을 Python 객체로 변환한다.
- `json.loads(text)`는 JSON 문자열을 Python 객체로 변환한다.
- JSON Object는 dict로 변환된다.
- JSON Array는 list로 변환된다.
- 외부 JSON 파일은 key 존재 여부를 검증해야 한다.
- JSON 구조가 잘못되면 `json.JSONDecodeError`가 발생한다.
- Config JSON은 루트 구조가 dict인지 확인하는 것이 좋다.

---

### [실무]

JSON 파일 읽기:

```python
import json
from pathlib import Path

path = Path("config.json")

with open(path, "r", encoding="utf-8") as file:
    config = json.load(file)
```

JSON 문자열 읽기:

```python
import json

text = '{"model": "qwen2.5", "temperature": 0.2}'
config = json.loads(text)
```

안전한 Config 읽기:

```python
import json
from pathlib import Path

def read_json_file(path: Path) -> dict:
    if not path.is_file():
        raise FileNotFoundError(f"JSON file not found: {path}")

    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, dict):
        raise ValueError("JSON root must be an object")

    return data
```

---

### [FAQ]

Q. json.load와 json.loads 차이는?

A. json.load는 파일 객체에서 읽고, json.loads는 JSON 문자열에서 읽는다.

Q. JSON 파일을 읽으면 어떤 타입이 돼?

A. JSON 구조에 따라 dict 또는 list가 된다.

Q. JSON 구조가 잘못되면 어떤 오류가 발생해?

A. `json.JSONDecodeError`가 발생한다.

Q. JSON 루트가 dict인지 확인해야 해?

A. 설정 파일이나 Tool Output처럼 key-value 구조를 기대한다면 확인하는 것이 좋다.

---

## 2.3 json.dump and json.dumps

### [개념]

`json.dump()`와 `json.dumps()`는 Python 객체를 JSON 형식으로 변환하는 함수이다.

`json.dump()`는 파일에 저장하고, `json.dumps()`는 JSON 문자열을 반환한다.

---

### [핵심]

- `json.dump(data, file)`은 Python 객체를 JSON 파일로 저장한다.
- `json.dumps(data)`는 Python 객체를 JSON 문자열로 변환한다.
- 한글 저장 시 `ensure_ascii=False`를 권장한다.
- 사람이 읽기 쉬운 JSON은 `indent=2`를 사용한다.
- JSON 저장 전 비직렬화 객체를 변환해야 한다.
- `set`, `Path`, `datetime`은 기본 JSON 직렬화가 불가능하다.
- Agent Tool Output 저장 시 JSON 구조를 유지한다.

---

### [실무]

JSON 파일 저장:

```python
import json
from pathlib import Path

data = {
    "file_name": "part05.md",
    "is_valid": True,
    "missing_sections": [],
}

path = Path("reports/result.json")
path.parent.mkdir(parents=True, exist_ok=True)

with open(path, "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=2)
```

JSON 문자열 생성:

```python
import json

text = json.dumps(data, ensure_ascii=False, indent=2)
```

Path 변환:

```python
from pathlib import Path

result = {
    "path": str(Path("docs/example.md")),
    "status": "success",
}
```

set 변환:

```python
missing_sections = {"[FAQ]", "# Retrieval Queries"}

result = {
    "missing_sections": sorted(list(missing_sections)),
}
```

---

### [FAQ]

Q. json.dump와 json.dumps 차이는?

A. json.dump는 파일에 저장하고, json.dumps는 JSON 문자열을 반환한다.

Q. ensure_ascii=False는 왜 사용해?

A. 한글이 유니코드 이스케이프가 아니라 읽을 수 있는 문자로 저장되게 하기 위해 사용한다.

Q. indent=2는 왜 사용해?

A. JSON을 사람이 읽기 쉬운 형태로 저장하기 위해 사용한다.

Q. JSON 저장 전 Path는 어떻게 처리해?

A. `str(path)`로 문자열 변환한다.

Q. JSON 저장 전 set은 어떻게 처리해?

A. list로 변환한 뒤 저장한다.

---

## 2.4 JSON File Structure Validation

### [개념]

JSON File Structure Validation은 JSON 파일이 기대한 구조를 가지는지 검사하는 작업이다.

Part05의 JSON 검증은 파일 기반 Config, Report, Agent Tool Output 저장 구조를 중심으로 한다.

Part06의 API JSON 검증은 HTTP Status Code, Response Header, Response Body 구조와 함께 처리한다.

---

### [핵심]

- 외부 JSON 파일은 신뢰하지 않고 검증한다.
- 필수 key 존재 여부를 확인한다.
- value type을 확인한다.
- Agent Tool Output은 `status`, `result`, `error` 구조를 권장한다.
- Config JSON은 필수 설정 누락 시 명확한 오류를 반환한다.
- 간단한 검증은 직접 코드로 작성할 수 있다.
- 복잡한 구조는 JSON Schema 라이브러리를 고려한다.
- 파일 기반 JSON 검증과 API Response JSON 검증을 구분한다.

---

### [실무]

필수 key 검증:

```python
def validate_tool_output(data: dict) -> None:
    required_keys = ["status", "result", "error"]

    missing_keys = [
        key for key in required_keys
        if key not in data
    ]

    if missing_keys:
        raise ValueError(f"Missing keys: {missing_keys}")
```

타입 검증:

```python
def validate_config(config: dict) -> None:
    if not isinstance(config.get("timeout"), int):
        raise TypeError("timeout must be int")

    if not isinstance(config.get("model"), str):
        raise TypeError("model must be str")
```

Agent Tool Output 권장 구조:

```python
{
    "status": "success",
    "result": {},
    "error": None,
}
```

오류 Output 권장 구조:

```python
{
    "status": "error",
    "result": None,
    "error": "File not found: docs/example.md",
}
```

---

### [FAQ]

Q. JSON File Structure Validation은 왜 필요해?

A. JSON 파일 구조가 예상과 다르면 자동화 코드와 Agent Tool 실행이 실패할 수 있기 때문이다.

Q. Agent Tool Output에 필요한 key는?

A. 기본적으로 `status`, `result`, `error`를 권장한다.

Q. Config JSON은 무엇을 검증해야 해?

A. 필수 key 존재 여부, value type, 허용 값, 보안 설정 누락 여부를 검증해야 한다.

Q. JSON 검증은 라이브러리가 꼭 필요해?

A. 간단한 검증은 직접 코드로 가능하고, 복잡한 구조는 JSON Schema 라이브러리를 고려한다.

Q. Part05 JSON 검증과 Part06 JSON 검증은 어떻게 달라?

A. Part05는 파일 기반 Config / Report 검증이고, Part06은 HTTP API Response 검증이다.

---

# 3. CSV Processing

## 3.1 CSV Basics

### [개념]

CSV는 Comma-Separated Values 형식의 표 형태 텍스트 파일이다.

Python for AI Automation에서는 문서 목록, 검증 결과, Chunk 메타데이터, 파일 처리 결과, 분석용 데이터 저장에 사용한다.

```csv
file_name,is_valid,missing_count
part01.md,true,0
part02.md,false,1
```

---

### [핵심]

- CSV는 행과 열로 구성된 표 형태 데이터이다.
- 첫 줄은 header로 사용하는 경우가 많다.
- Python 표준 라이브러리 `csv`로 처리할 수 있다.
- 분석과 가공이 많으면 pandas를 사용할 수 있다.
- 한글 CSV는 encoding 문제를 주의한다.
- 저장 시 index 저장 여부를 확인해야 한다.
- CSV는 nested dict 표현에는 적합하지 않다.
- 구조가 복잡하면 JSON을 우선 고려한다.

---

### [실무]

CSV 사용 영역:

- RAG 문서 목록
- 파일명 검증 결과
- 필수 섹션 누락 리포트
- Retrieval Queries 포함 여부
- Chunk 길이 측정 결과
- Agent Tool 실행 결과 요약
- API 수집 데이터 저장본

CSV 구조 예시:

```text
file_name,has_concept,has_core,has_practice,has_faq,has_retrieval_queries,is_valid
Python_Part01.md,true,true,true,true,true,true
Python_Part02.md,true,true,true,true,true,true
```

---

### [FAQ]

Q. CSV는 언제 사용해?

A. 문서 목록, 검증 결과, 메타데이터, 표 형태 리포트 저장에 사용한다.

Q. CSV 첫 줄은 무엇이야?

A. 일반적으로 컬럼명을 나타내는 header이다.

Q. CSV 처리에 pandas가 꼭 필요해?

A. 아니다. 간단한 CSV는 표준 `csv` 모듈로 충분하다.

Q. CSV에서 한글이 깨질 수 있어?

A. 가능하다. encoding을 확인하고 UTF-8 또는 CP949를 고려해야 한다.

Q. 복잡한 중첩 데이터도 CSV가 좋아?

A. 아니다. 중첩 dict나 복잡한 구조는 JSON이 더 적합하다.

---

## 3.2 csv DictReader and DictWriter

### [개념]

`csv.DictReader`와 `csv.DictWriter`는 CSV 행을 dict 형태로 읽고 쓰는 Python 표준 기능이다.

컬럼명을 key로 사용하므로 자동화 결과 처리에 적합하다.

---

### [핵심]

- `DictReader`는 CSV 행을 dict로 읽는다.
- `DictWriter`는 dict 목록을 CSV로 저장한다.
- `fieldnames`는 CSV 컬럼명 목록이다.
- 각 행은 key-value 구조로 처리된다.
- CSV 컬럼 누락과 오타를 주의한다.
- newline 처리를 위해 `newline=""`을 사용한다.
- 저장할 row의 key와 fieldnames가 맞아야 한다.

---

### [실무]

CSV 읽기:

```python
import csv
from pathlib import Path

path = Path("reports/validation.csv")

with open(path, "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    rows = list(reader)
```

CSV 쓰기:

```python
import csv
from pathlib import Path

rows = [
    {"file_name": "part01.md", "is_valid": "true"},
    {"file_name": "part02.md", "is_valid": "false"},
]

fieldnames = ["file_name", "is_valid"]

path = Path("reports/validation.csv")
path.parent.mkdir(parents=True, exist_ok=True)

with open(path, "w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
```

검증 결과 CSV 저장 함수:

```python
import csv
from pathlib import Path

def write_validation_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        raise ValueError("rows must not be empty")

    fieldnames = list(rows[0].keys())
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
```

---

### [FAQ]

Q. DictReader는 무엇을 해?

A. CSV 각 행을 컬럼명 기반 dict로 읽는다.

Q. DictWriter는 무엇을 해?

A. dict 데이터를 CSV 행으로 저장한다.

Q. fieldnames는 무엇이야?

A. CSV에 저장할 컬럼명 목록이다.

Q. CSV 파일 open에서 newline=""은 왜 사용해?

A. 플랫폼별 줄바꿈 문제와 빈 줄 생성을 줄이기 위해 사용한다.

Q. CSV row의 key가 fieldnames와 다르면 어떻게 돼?

A. 저장 오류가 나거나 의도하지 않은 컬럼 누락이 발생할 수 있으므로 key를 맞춰야 한다.

---

## 3.3 Pandas CSV Basics

### [개념]

pandas는 표 형태 데이터를 처리하는 Python 라이브러리이다.

CSV 데이터가 크거나 필터링, 그룹화, 정렬, 결측치 처리, 통계 계산이 필요한 경우 pandas를 사용할 수 있다.

---

### [핵심]

- pandas는 표 형태 데이터 처리에 적합하다.
- `read_csv()`로 CSV를 DataFrame으로 읽는다.
- `to_csv()`로 DataFrame을 CSV로 저장한다.
- `head()`, `info()`, `columns`로 데이터를 확인한다.
- `fillna()`, `dropna()`로 결측값을 처리한다.
- `groupby()`, `sort_values()`로 데이터를 집계하고 정렬한다.
- 저장 시 `index=False`를 확인한다.
- 간단한 CSV 저장만 필요하면 표준 `csv` 모듈로 충분하다.

---

### [실무]

CSV 읽기:

```python
import pandas as pd

df = pd.read_csv("reports/validation.csv")
```

기본 확인:

```python
print(df.head())
print(df.info())
print(df.columns)
```

필터링:

```python
invalid_docs = df[df["is_valid"] == False]
```

정렬:

```python
sorted_df = df.sort_values("missing_count", ascending=False)
```

CSV 저장:

```python
sorted_df.to_csv("reports/validation_sorted.csv", index=False)
```

---

### [FAQ]

Q. pandas는 언제 사용해?

A. CSV 데이터 필터링, 정렬, 그룹화, 결측치 처리, 분석이 필요할 때 사용한다.

Q. read_csv는 무엇을 해?

A. CSV 파일을 pandas DataFrame으로 읽는다.

Q. to_csv에서 index=False는 왜 중요해?

A. 불필요한 index 컬럼이 CSV에 저장되는 것을 방지하기 위해 사용한다.

Q. pandas는 모든 CSV 처리에 필수야?

A. 아니다. 간단한 CSV 읽기/쓰기는 표준 csv 모듈로 충분하다.

---

# 4. YAML Processing

## 4.1 YAML Basics

### [개념]

YAML은 사람이 읽기 쉬운 설정 파일 형식이다.

Python for AI Automation에서는 Config, Workflow, Agent 설정, 문서 생성 옵션, 환경별 설정 관리에 사용할 수 있다.

```yaml
model: qwen2.5
temperature: 0.2
enabled: true
```

---

### [핵심]

- YAML은 설정 파일에 자주 사용된다.
- JSON보다 사람이 읽고 수정하기 쉽다.
- 들여쓰기가 구조를 의미한다.
- Python에서는 PyYAML 라이브러리를 사용할 수 있다.
- 외부 YAML은 `safe_load()`로 읽는다.
- Secret 값을 YAML에 직접 저장하지 않는다.
- API Key, Token, Password는 환경변수 또는 Secret Manager로 관리한다.

---

### [실무]

YAML 사용 영역:

- RAG 문서 생성 설정
- Agent Workflow 설정
- 모델 이름과 옵션
- 입력 폴더와 출력 폴더
- 필수 섹션 목록
- 검증 기준
- 환경별 Config

YAML 예시:

```yaml
rag_document:
  input_dir: docs
  output_dir: reports
  required_sections:
    - "[개념]"
    - "[핵심]"
    - "[실무]"
    - "[FAQ]"
  require_retrieval_queries: true
```

---

### [FAQ]

Q. YAML은 어디에 사용해?

A. 설정 파일, 워크플로우 정의, 문서 생성 옵션, Agent 설정에 사용한다.

Q. YAML은 JSON보다 좋은가?

A. 설정 파일처럼 사람이 직접 수정하는 경우 YAML이 읽기 쉽다.

Q. YAML에서 들여쓰기는 중요해?

A. 중요하다. YAML은 들여쓰기로 구조를 표현한다.

Q. YAML에 API Key를 저장해도 돼?

A. 권장하지 않는다. Secret은 환경변수나 별도 Secret 관리 방식을 사용한다.

---

## 4.2 yaml.safe_load and safe_dump

### [개념]

`yaml.safe_load()`는 YAML 문자열이나 파일 내용을 안전하게 Python 객체로 변환한다.

`yaml.safe_dump()`는 Python 객체를 YAML 문자열로 변환한다.

`yaml.load()`는 Loader 설정 없이 사용하면 위험할 수 있으므로, 외부 입력에는 `yaml.safe_load()`를 우선 사용한다.

---

### [핵심]

- PyYAML 설치가 필요하다.
- `safe_load()`는 안전한 YAML 읽기 방식이다.
- `safe_dump()`는 Python 객체를 YAML로 저장한다.
- `yaml.load()`는 Loader 설정 없이 사용할 경우 보안상 위험할 수 있다.
- 외부 YAML은 반드시 `safe_load()`를 우선한다.
- 한글 저장 시 encoding과 `allow_unicode=True`를 고려한다.
- Secret 값은 YAML 파일에 직접 저장하지 않는다.

---

### [실무]

YAML 읽기:

```python
from pathlib import Path
import yaml

path = Path("config.yml")
text = path.read_text(encoding="utf-8")
config = yaml.safe_load(text)
```

YAML 저장:

```python
from pathlib import Path
import yaml

config = {
    "model": "qwen2.5",
    "temperature": 0.2,
    "enabled": True,
}

path = Path("config.yml")
path.write_text(
    yaml.safe_dump(config, allow_unicode=True, sort_keys=False),
    encoding="utf-8",
)
```

YAML Config 검증:

```python
def validate_yaml_config(config: dict) -> None:
    required_keys = ["input_dir", "output_dir", "required_sections"]

    missing_keys = [
        key for key in required_keys
        if key not in config
    ]

    if missing_keys:
        raise ValueError(f"Missing config keys: {missing_keys}")
```

---

### [FAQ]

Q. PyYAML은 표준 라이브러리야?

A. 아니다. 별도 설치가 필요한 외부 패키지이다.

Q. yaml.safe_load는 왜 사용해?

A. 외부 YAML을 더 안전하게 읽기 위해 사용한다.

Q. yaml.load는 사용하면 안 돼?

A. Loader 설정 없이 사용하면 위험할 수 있으므로, 외부 입력에는 yaml.safe_load를 우선 사용한다.

Q. YAML 저장 시 한글을 유지하려면?

A. `allow_unicode=True`를 사용하고 UTF-8 encoding으로 저장한다.

---

# 5. Markdown Processing

## 5.1 Markdown Role in RAG

### [개념]

Markdown은 RAG Document 제작과 관리의 기본 문서 형식이다.

RAG 문서는 Header, Section, Code Block, FAQ, Retrieval Queries를 Markdown 구조로 작성하고, Python 자동화로 구조를 검사할 수 있다.

기본 Flow:

```text
Markdown File
→ Read Text
→ Parse Header
→ Extract Section
→ Validate Required Blocks
→ Check Retrieval Queries
→ Generate Report
```

---

### [핵심]

- RAG 문서는 Markdown 기준으로 관리한다.
- Header는 Chunk 경계로 사용할 수 있다.
- `[개념]`, `[핵심]`, `[실무]`, `[FAQ]`는 필수 섹션이다.
- `# Retrieval Queries`는 문서 마지막에 포함한다.
- Code Block 내부의 `#`를 Header로 오인하지 않아야 한다.
- Markdown 자동 수정 전 원본 백업을 고려한다.
- FAQ는 Retrieval Matching 강화에 중요하다.

---

### [실무]

RAG Markdown 검사 항목:

- 파일명 규칙
- Document Title 존재 여부
- Required Section 존재 여부
- FAQ Q/A 쌍 존재 여부
- Retrieval Queries 존재 여부
- Code Block 깨짐 여부
- Header Level 구조
- Chunk 크기
- 중복 섹션
- 금지 표현 여부

필수 섹션:

```text
### [개념]
### [핵심]
### [실무]
### [FAQ]
```

Retrieval Queries:

```text
# Retrieval Queries

### [FAQ]

Q. 질문
A. 답변
```

---

### [FAQ]

Q. RAG 문서는 왜 Markdown으로 관리해?

A. Header, Code Block, Section 구조가 명확하고 Chunk 분리와 Retrieval 최적화에 유리하기 때문이다.

Q. Markdown Header는 왜 중요해?

A. 검색 단위와 Chunk 경계를 만드는 기준으로 사용할 수 있기 때문이다.

Q. RAG 문서 필수 섹션은 무엇이야?

A. `[개념]`, `[핵심]`, `[실무]`, `[FAQ]`이다.

Q. Retrieval Queries는 왜 필요해?

A. 실제 사용자 질문 패턴과 문서 검색 매칭을 강화하기 위해 필요하다.

---

## 5.2 Markdown Header Parsing

### [개념]

Markdown Header Parsing은 `#`, `##`, `###` 같은 Header를 추출해 문서 구조를 파악하는 작업이다.

RAG Document Automation에서는 Header를 기준으로 문서 섹션과 Chunk 후보를 식별한다.

---

### [핵심]

- Header는 `#` 문자로 시작한다.
- Header Level은 `#` 개수로 구분한다.
- `# FileName`, `# Document Title`, Main Section, Sub Section 구조를 검사할 수 있다.
- Code Block 내부의 `#`는 Header로 처리하면 안 된다.
- Header 추출 결과는 문서 구조 리포트에 사용할 수 있다.
- 단순 Parser는 충분히 유용하지만, 복잡한 Markdown은 Markdown Parser 라이브러리도 고려한다.

---

### [실무]

단순 Header 추출:

```python
def extract_headers(text: str) -> list[str]:
    return [
        line.strip()
        for line in text.splitlines()
        if line.startswith("#")
    ]
```

Code Block 보호 Header 추출:

````python
def extract_markdown_headers(text: str) -> list[str]:
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

Header Metadata 생성:

```python
def build_header_metadata(headers: list[str]) -> list[dict]:
    result = []

    for header in headers:
        level = len(header) - len(header.lstrip("#"))
        title = header.lstrip("#").strip()

        result.append({
            "level": level,
            "title": title,
            "raw": header,
        })

    return result
```

---

### [FAQ]

Q. Markdown Header Parsing은 왜 필요해?

A. 문서 구조를 파악하고 Chunk 경계와 필수 섹션 위치를 찾기 위해 필요하다.

Q. Code Block 내부 Header를 조심해야 하는 이유는?

A. Code Block 안의 `#`는 문서 Header가 아니라 코드나 예시 텍스트일 수 있기 때문이다.

Q. Header Level은 어떻게 계산해?

A. 줄 시작 부분의 `#` 개수를 세어 계산한다.

Q. Header Metadata는 어디에 사용해?

A. 문서 구조 리포트, Chunk 분리, 섹션 검증에 사용한다.

---

## 5.3 Markdown Section Validation

### [개념]

Markdown Section Validation은 RAG 문서에 필요한 필수 섹션과 구조가 존재하는지 검사하는 작업이다.

필수 섹션은 `[개념]`, `[핵심]`, `[실무]`, `[FAQ]`이며, 문서 마지막에는 `# Retrieval Queries`가 필요하다.

---

### [핵심]

- Required Section 존재 여부를 검사한다.
- Retrieval Queries 존재 여부를 검사한다.
- FAQ에 Q/A 쌍이 있는지 확인한다.
- 중복 섹션을 검사할 수 있다.
- 금지 섹션명을 검사할 수 있다.
- 검사 결과는 dict 또는 JSON으로 반환한다.
- 실제 운영에서는 Required Section 목록을 `config.py` 또는 Domain Rules에서 관리한다.

---

### [실무]

필수 섹션 검사:

```python
REQUIRED_SECTIONS = ["### [개념]", "### [핵심]", "### [실무]", "### [FAQ]"]

def find_missing_sections(text: str) -> list[str]:
    return [
        section for section in REQUIRED_SECTIONS
        if section not in text
    ]
```

Retrieval Queries 검사:

```python
def has_retrieval_queries(text: str) -> bool:
    return "# Retrieval Queries" in text
```

FAQ Q/A 검사:

```python
def has_faq_qa_pair(text: str) -> bool:
    return "Q." in text and "A." in text
```

Validation Result:

```python
def validate_rag_markdown(text: str) -> dict:
    missing_sections = find_missing_sections(text)

    return {
        "is_valid": len(missing_sections) == 0 and has_retrieval_queries(text),
        "missing_sections": missing_sections,
        "has_retrieval_queries": has_retrieval_queries(text),
        "has_faq_qa_pair": has_faq_qa_pair(text),
    }
```

---

### [FAQ]

Q. Markdown Section Validation은 무엇을 검사해?

A. 필수 섹션, Retrieval Queries, FAQ Q/A 쌍, 중복 섹션, 금지 섹션명을 검사한다.

Q. RAG 문서 필수 섹션은 무엇이야?

A. `[개념]`, `[핵심]`, `[실무]`, `[FAQ]`이다.

Q. Retrieval Queries는 반드시 있어야 해?

A. 그렇다. 사용자 질문 패턴과 검색 매칭을 강화하기 위해 필수이다.

Q. FAQ에는 Q만 있어도 돼?

A. 안 된다. 반드시 Q와 A가 함께 있어야 한다.

Q. REQUIRED_SECTIONS는 어디에서 관리하는 게 좋아?

A. 실제 운영에서는 `config.py`, YAML Config, Domain Rules 중 하나로 중앙 관리하는 것이 좋다.

---

## 5.4 Code Block Detection

### [개념]

Code Block Detection은 Markdown 문서에서 코드 블록 영역을 감지하는 작업이다.

RAG Document Automation에서는 Code Block 내부의 Header, FAQ, Section 표현을 실제 문서 구조로 오인하지 않도록 처리해야 한다.

---

### [핵심]

- Markdown Code Block은 `로 시작하고 `로 끝난다.
- Code Block 내부 텍스트는 문서 Header로 처리하지 않는다.
- Code Block 내부의 `#`, `Q.`, `A.`는 구조 검사에서 제외할 수 있다.
- Code Block이 닫히지 않으면 문서 파싱 오류가 발생한다.
- 자동화 검증에서 Code Block 개수와 닫힘 여부를 확인할 수 있다.
- 단순 검사는 Fence 개수 기반으로 가능하지만, 실제 운영에서는 Markdown Parser 또는 Fence Language 기준을 함께 고려한다.

---

### [실무]

Code Block 감지:

````python
def find_code_block_ranges(text: str) -> list[dict]:
    ranges = []
    in_code_block = False
    start_line = None

    for index, line in enumerate(text.splitlines(), start=1):
        if line.strip().startswith("```"):
            if not in_code_block:
                in_code_block = True
                start_line = index
            else:
                ranges.append({
                    "start": start_line,
                    "end": index,
                })
                in_code_block = False
                start_line = None

    if in_code_block:
        ranges.append({
            "start": start_line,
            "end": None,
        })

    return ranges
````

Code Block 닫힘 검사:

````python
def has_unclosed_code_block(text: str) -> bool:
    fence_count = sum(
        1 for line in text.splitlines()
        if line.strip().startswith("```")
    )

    return fence_count % 2 != 0
````

Header 추출 시 Code Block 제외:

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

---

### [FAQ]

Q. Code Block Detection은 왜 필요해?

A. Code Block 내부의 `#`, `Q.`, `A.`를 실제 문서 구조로 오인하지 않기 위해 필요하다.

Q. Markdown Code Block은 어떻게 시작해?

A. 보통 `로 시작하고 `로 끝난다.

Q. Code Block이 닫히지 않으면 문제야?

A. 그렇다. 문서 파싱과 Chunk 분리에 문제가 생길 수 있다.

Q. Header 추출에서 Code Block을 제외해야 해?

A. 그렇다. Code Block 내부의 Header 형식 텍스트는 실제 Header가 아닐 수 있다.

Q. Fence 개수만 세면 항상 정확해?

A. 단순 검증에는 유용하지만 복잡한 Markdown에서는 오탐 가능성이 있어 Markdown Parser 사용도 고려한다.

---

## 5.5 Chunk Preparation

### [개념]

Chunk Preparation은 RAG 문서를 검색 가능한 독립 단위로 나누기 전 구조를 정리하는 작업이다.

좋은 Chunk는 하나의 개념을 담고, 제목이 명확하며, 독립 검색되어도 의미가 유지되어야 한다.

---

### [핵심]

- Header는 Chunk 경계로 사용할 수 있다.
- 하나의 Chunk에는 하나의 개념만 담는다.
- Chunk는 독립적으로 검색되어도 의미가 있어야 한다.
- Code Block은 중간에 잘리지 않도록 주의한다.
- FAQ는 Retrieval Matching 강화용 Chunk로 중요하다.
- 권장 Chunk Size는 300~1200 tokens이다.
- 너무 긴 Section은 Sub Section으로 분리한다.
- 파일 형식 처리 결과는 Chunk Metadata로 연결할 수 있다.

---

### [실무]

Chunk 후보 구조:

```python
chunk = {
    "file_name": "Python_for_AI_Automation_Part05_JSON_CSV_YAML_Markdown_Processing.md",
    "title": "JSON Processing",
    "section": "json.dump and json.dumps",
    "text": "본문 내용",
    "keywords": ["JSON", "json.dump", "json.dumps", "Agent Tool Output"],
}
```

Header 기반 Chunk 분리 기준:

```text
# Document Title
→ Metadata

## Major Section
→ Chunk Group

### [개념] / [핵심] / [실무] / [FAQ]
→ Retrieval Unit
```

Chunk 검증 기준:

```text
- 제목이 명확한가?
- 하나의 개념만 포함하는가?
- FAQ가 포함되어 있는가?
- Code Block이 깨지지 않았는가?
- Retrieval Queries와 연결되는가?
```

---

### [FAQ]

Q. Chunk Preparation은 왜 필요해?

A. RAG 검색 품질을 높이기 위해 문서를 독립 검색 가능한 단위로 정리해야 하기 때문이다.

Q. 좋은 Chunk 조건은 무엇이야?

A. 하나의 개념, 명확한 제목, 짧은 예제, 독립 검색 가능성이다.

Q. Code Block은 Chunk 분리 시 어떻게 처리해?

A. Code Block이 중간에 잘리지 않도록 유지해야 한다.

Q. FAQ는 Chunk로 중요해?

A. 중요하다. FAQ는 실제 사용자 질문과 Retrieval Matching을 강화한다.

---

# 6. Data File Processing Best Practice

## 6.1 Best Practice

### [개념]

Data File Processing Best Practice는 JSON, CSV, YAML, Markdown을 안전하고 일관되게 처리하기 위한 기준이다.

AI Automation Script는 파일 형식별 목적을 명확히 하고, 입력 검증, 구조 변환, 결과 저장을 분리해야 한다.

목표:

```text
Read
→ Parse
→ Validate
→ Transform
→ Save
→ Return Structured Result
```

---

### [핵심]

- JSON은 Config, Report, Agent Tool Output 저장에 우선 사용한다.
- CSV는 표 형태 리포트와 문서 메타데이터 목록에 사용한다.
- YAML은 사람이 수정하는 설정 파일에 사용한다.
- Markdown은 RAG 문서 본문과 리포트에 사용한다.
- 파일 읽기와 쓰기에는 encoding을 명시한다.
- 외부 입력 파일은 구조를 검증한다.
- JSON 저장 시 `ensure_ascii=False`, `indent=2`를 권장한다.
- CSV 저장 시 `newline=""`과 header를 확인한다.
- pandas `to_csv()` 저장 시 `index=False`를 확인한다.
- YAML은 `safe_load()`를 우선 사용한다.
- Markdown 파싱 시 Code Block 내부 구조 오탐을 방지한다.
- Agent Tool Result는 JSON 직렬화 가능한 dict로 반환한다.
- 파일 기반 JSON 검증과 API Response JSON 검증을 구분한다.

---

### [실무]

통합 검증 결과 구조:

```python
result = {
    "status": "success",
    "file_name": "Python_for_AI_Automation_Part05_JSON_CSV_YAML_Markdown_Processing.md",
    "format": "markdown",
    "checks": {
        "has_required_sections": True,
        "has_retrieval_queries": True,
        "has_unclosed_code_block": False,
    },
    "error": None,
}
```

JSON 저장:

```python
import json
from pathlib import Path

def save_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
```

CSV 저장:

```python
import csv
from pathlib import Path

def save_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        raise ValueError("rows must not be empty")

    path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys())

    with open(path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
```

Markdown 검사:

```python
def validate_markdown_document(text: str) -> dict:
    required_sections = ["### [개념]", "### [핵심]", "### [실무]", "### [FAQ]"]

    missing_sections = [
        section for section in required_sections
        if section not in text
    ]

    return {
        "has_required_sections": len(missing_sections) == 0,
        "missing_sections": missing_sections,
        "has_retrieval_queries": "# Retrieval Queries" in text,
    }
```

---

### [FAQ]

Q. Data File Processing Best Practice는 무엇이야?

A. 파일 형식별 목적을 분리하고, 읽기, 파싱, 검증, 변환, 저장, 구조화된 결과 반환을 일관되게 처리하는 기준이다.

Q. JSON 저장 시 가장 중요한 옵션은?

A. 한글 저장을 위한 `ensure_ascii=False`와 가독성을 위한 `indent=2`이다.

Q. CSV 저장 시 가장 중요한 옵션은?

A. `newline=""`, fieldnames, header, pandas 사용 시 `index=False` 확인이다.

Q. YAML 처리 시 가장 중요한 보안 기준은?

A. 외부 YAML은 `safe_load()`로 읽고 Secret을 YAML에 직접 저장하지 않는 것이다.

Q. Markdown 처리 시 가장 중요한 검증 기준은?

A. 필수 섹션, Retrieval Queries, FAQ Q/A, Code Block 닫힘 여부, Header 구조이다.

---

# Retrieval Queries

### [FAQ]

Q. Python에서 JSON은 어디에 사용해?
A. Config 파일, 검증 결과 저장, Agent Tool Output 저장, API Response 저장본에 사용한다.

Q. Python에서 CSV는 어디에 사용해?
A. 문서 목록, 메타데이터, 표 형태 검증 결과, 분석용 데이터 저장에 사용한다.

Q. Python에서 YAML은 어디에 사용해?
A. 설정 파일, 워크플로우 정의, 문서 생성 옵션, Agent 설정에 사용한다.

Q. Python에서 Markdown은 어디에 사용해?
A. RAG 문서, Prompt Rule, Domain Rules, 검증 리포트 작성에 사용한다.

Q. Part05 JSON과 Part06 JSON의 차이는?
A. Part05는 파일 기반 JSON Config / Report / Tool Output 저장 중심이고, Part06은 HTTP API Response 처리 중심이다.

Q. Python Agent Tool Output은 어떤 형식이 좋아?
A. JSON 변환이 쉬운 dict 구조가 좋다.

Q. JSON은 Python에서 어떤 타입으로 다뤄?
A. JSON Object는 dict, JSON Array는 list로 다룬다.

Q. JSON의 null은 Python에서 뭐야?
A. Python의 `None`으로 변환된다.

Q. JSON의 true와 false는 Python에서 뭐야?
A. Python의 `True`, `False`로 변환된다.

Q. Python set은 JSON으로 바로 저장돼?
A. 아니다. JSON 저장 전 list로 변환해야 한다.

Q. Python Path 객체는 JSON으로 바로 저장돼?
A. 아니다. `str(path)`로 문자열 변환 후 저장해야 한다.

Q. json.load와 json.loads 차이는?
A. json.load는 파일 객체에서 읽고, json.loads는 JSON 문자열에서 읽는다.

Q. JSON 파일을 읽으면 어떤 타입이 돼?
A. JSON 구조에 따라 dict 또는 list가 된다.

Q. JSON 구조가 잘못되면 어떤 오류가 발생해?
A. `json.JSONDecodeError`가 발생한다.

Q. JSON 루트가 dict인지 확인해야 해?
A. 설정 파일이나 Tool Output처럼 key-value 구조를 기대한다면 확인하는 것이 좋다.

Q. json.dump와 json.dumps 차이는?
A. json.dump는 파일에 저장하고, json.dumps는 JSON 문자열을 반환한다.

Q. ensure_ascii=False는 왜 사용해?
A. 한글이 유니코드 이스케이프가 아니라 읽을 수 있는 문자로 저장되게 하기 위해 사용한다.

Q. indent=2는 왜 사용해?
A. JSON을 사람이 읽기 쉬운 형태로 저장하기 위해 사용한다.

Q. JSON 저장 전 set은 어떻게 처리해?
A. list로 변환한 뒤 저장한다.

Q. JSON File Structure Validation은 왜 필요해?
A. JSON 파일 구조가 예상과 다르면 자동화 코드와 Agent Tool 실행이 실패할 수 있기 때문이다.

Q. Agent Tool Output에 필요한 key는?
A. 기본적으로 `status`, `result`, `error`를 권장한다.

Q. Config JSON은 무엇을 검증해야 해?
A. 필수 key 존재 여부, value type, 허용 값, 보안 설정 누락 여부를 검증해야 한다.

Q. CSV는 언제 사용해?
A. 문서 목록, 검증 결과, 메타데이터, 표 형태 리포트 저장에 사용한다.

Q. CSV 첫 줄은 무엇이야?
A. 일반적으로 컬럼명을 나타내는 header이다.

Q. CSV 처리에 pandas가 꼭 필요해?
A. 아니다. 간단한 CSV는 표준 `csv` 모듈로 충분하다.

Q. CSV에서 한글이 깨질 수 있어?
A. 가능하다. encoding을 확인하고 UTF-8 또는 CP949를 고려해야 한다.

Q. 복잡한 중첩 데이터도 CSV가 좋아?
A. 아니다. 중첩 dict나 복잡한 구조는 JSON이 더 적합하다.

Q. DictReader는 무엇을 해?
A. CSV 각 행을 컬럼명 기반 dict로 읽는다.

Q. DictWriter는 무엇을 해?
A. dict 데이터를 CSV 행으로 저장한다.

Q. fieldnames는 무엇이야?
A. CSV에 저장할 컬럼명 목록이다.

Q. CSV 파일 open에서 newline=""은 왜 사용해?
A. 플랫폼별 줄바꿈 문제와 빈 줄 생성을 줄이기 위해 사용한다.

Q. pandas는 언제 사용해?
A. CSV 데이터 필터링, 정렬, 그룹화, 결측치 처리, 분석이 필요할 때 사용한다.

Q. pandas read_csv는 무엇을 해?
A. CSV 파일을 pandas DataFrame으로 읽는다.

Q. pandas to_csv에서 index=False는 왜 중요해?
A. 불필요한 index 컬럼이 CSV에 저장되는 것을 방지하기 위해 사용한다.

Q. YAML은 어디에 사용해?
A. 설정 파일, 워크플로우 정의, 문서 생성 옵션, Agent 설정에 사용한다.

Q. YAML은 JSON보다 좋은가?
A. 설정 파일처럼 사람이 직접 수정하는 경우 YAML이 읽기 쉽다.

Q. YAML에서 들여쓰기는 중요해?
A. 중요하다. YAML은 들여쓰기로 구조를 표현한다.

Q. YAML에 API Key를 저장해도 돼?
A. 권장하지 않는다. Secret은 환경변수나 별도 Secret 관리 방식을 사용한다.

Q. PyYAML은 표준 라이브러리야?
A. 아니다. 별도 설치가 필요한 외부 패키지이다.

Q. yaml.safe_load는 왜 사용해?
A. 외부 YAML을 더 안전하게 읽기 위해 사용한다.

Q. yaml.load는 사용하면 안 돼?
A. Loader 설정 없이 사용하면 위험할 수 있으므로, 외부 입력에는 yaml.safe_load를 우선 사용한다.

Q. YAML 저장 시 한글을 유지하려면?
A. `allow_unicode=True`를 사용하고 UTF-8 encoding으로 저장한다.

Q. RAG 문서는 왜 Markdown으로 관리해?
A. Header, Code Block, Section 구조가 명확하고 Chunk 분리와 Retrieval 최적화에 유리하기 때문이다.

Q. Markdown Header는 왜 중요해?
A. 검색 단위와 Chunk 경계를 만드는 기준으로 사용할 수 있기 때문이다.

Q. RAG 문서 필수 섹션은 무엇이야?
A. `[개념]`, `[핵심]`, `[실무]`, `[FAQ]`이다.

Q. Retrieval Queries는 왜 필요해?
A. 실제 사용자 질문 패턴과 문서 검색 매칭을 강화하기 위해 필요하다.

Q. Markdown Header Parsing은 왜 필요해?
A. 문서 구조를 파악하고 Chunk 경계와 필수 섹션 위치를 찾기 위해 필요하다.

Q. Code Block 내부 Header를 조심해야 하는 이유는?
A. Code Block 안의 `#`는 문서 Header가 아니라 코드나 예시 텍스트일 수 있기 때문이다.

Q. Header Level은 어떻게 계산해?
A. 줄 시작 부분의 `#` 개수를 세어 계산한다.

Q. Markdown Section Validation은 무엇을 검사해?
A. 필수 섹션, Retrieval Queries, FAQ Q/A 쌍, 중복 섹션, 금지 섹션명을 검사한다.

Q. REQUIRED_SECTIONS는 어디에서 관리하는 게 좋아?
A. 실제 운영에서는 `config.py`, YAML Config, Domain Rules 중 하나로 중앙 관리하는 것이 좋다.

Q. Retrieval Queries는 반드시 있어야 해?
A. 그렇다. 사용자 질문 패턴과 검색 매칭을 강화하기 위해 필수이다.

Q. FAQ에는 Q만 있어도 돼?
A. 안 된다. 반드시 Q와 A가 함께 있어야 한다.

Q. Code Block Detection은 왜 필요해?
A. Code Block 내부의 `#`, `Q.`, `A.`를 실제 문서 구조로 오인하지 않기 위해 필요하다.

Q. Markdown Code Block은 어떻게 시작해?
A. 보통 `로 시작하고 `로 끝난다.

Q. Code Block이 닫히지 않으면 문제야?
A. 그렇다. 문서 파싱과 Chunk 분리에 문제가 생길 수 있다.

Q. Header 추출에서 Code Block을 제외해야 해?
A. 그렇다. Code Block 내부의 Header 형식 텍스트는 실제 Header가 아닐 수 있다.

Q. Fence 개수만 세면 항상 정확해?
A. 단순 검증에는 유용하지만 복잡한 Markdown에서는 오탐 가능성이 있어 Markdown Parser 사용도 고려한다.

Q. Chunk Preparation은 왜 필요해?
A. RAG 검색 품질을 높이기 위해 문서를 독립 검색 가능한 단위로 정리해야 하기 때문이다.

Q. 좋은 Chunk 조건은 무엇이야?
A. 하나의 개념, 명확한 제목, 짧은 예제, 독립 검색 가능성이다.

Q. Code Block은 Chunk 분리 시 어떻게 처리해?
A. Code Block이 중간에 잘리지 않도록 유지해야 한다.

Q. FAQ는 Chunk로 중요해?
A. 중요하다. FAQ는 실제 사용자 질문과 Retrieval Matching을 강화한다.

Q. Data File Processing Best Practice는 무엇이야?
A. 파일 형식별 목적을 분리하고, 읽기, 파싱, 검증, 변환, 저장, 구조화된 결과 반환을 일관되게 처리하는 기준이다.

Q. JSON 저장 시 가장 중요한 옵션은?
A. 한글 저장을 위한 `ensure_ascii=False`와 가독성을 위한 `indent=2`이다.

Q. CSV 저장 시 가장 중요한 옵션은?
A. `newline=""`, fieldnames, header, pandas 사용 시 `index=False` 확인이다.

Q. YAML 처리 시 가장 중요한 보안 기준은?
A. 외부 YAML은 `safe_load()`로 읽고 Secret을 YAML에 직접 저장하지 않는 것이다.

Q. Markdown 처리 시 가장 중요한 검증 기준은?
A. 필수 섹션, Retrieval Queries, FAQ Q/A, Code Block 닫힘 여부, Header 구조이다.
