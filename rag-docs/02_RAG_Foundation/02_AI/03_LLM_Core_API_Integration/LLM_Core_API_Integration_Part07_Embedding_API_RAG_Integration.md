# LLM Core & API Integration Part07 - Embedding API & RAG Integration

---

# 1. Embedding API

## 1.1 Embedding

### [개념]

Embedding은 텍스트를 의미 기반 Vector로 변환하는 기술이다.

Embedding Model은 문장, 문서, Query, 코드 조각을 고차원 숫자 배열로 변환한다.

Embedding은 답변 생성용이 아니라 검색, 유사도 비교, 추천, 분류, RAG Retrieval에 사용한다.

Embedding 기본 Flow:

```text
Text
→ Embedding Model
→ Vector
→ Similarity Search
→ Retrieved Context
```

---

### [핵심]

- Embedding은 텍스트 의미를 Vector로 변환한다.
- Embedding Model은 Chat Model과 역할이 다르다.
- Chat Model은 답변을 생성한다.
- Embedding Model은 검색용 Vector를 생성한다.
- Semantic Search는 Query Vector와 Document Vector의 유사도를 비교한다.
- RAG는 Embedding 기반 검색 결과를 LLM Prompt에 넣어 답변을 생성한다.
- 문서 Chunk 품질이 Embedding 검색 품질에 직접 영향을 준다.

---

### [실무]

2026 실무 기준 Embedding은 RAG 시스템의 검색 엔진 역할을 담당한다.

일반 구조:

```text
Document
→ Chunking
→ Embedding API
→ Vector DB 저장
→ User Query
→ Query Embedding
→ Similarity Search
→ Retrieved Context
→ Chat Completion
→ Grounded Answer
```

Embedding 사용처:

| 사용처              | 설명                    |
| ------------------- | ----------------------- |
| Semantic Search     | 의미 기반 문서 검색     |
| RAG Retrieval       | LLM 답변 근거 문서 검색 |
| Similarity Matching | 문장/문서 유사도 비교   |
| Recommendation      | 유사 문서 추천          |
| Clustering          | 문서 그룹화             |
| Deduplication       | 중복 문서 탐지          |
| Memory Retrieval    | Agent Memory 검색       |
| Code Search         | 코드 조각 의미 검색     |

실무 기준:

- Chat Model과 Embedding Model을 분리한다.
- Document Chunk와 Query는 같은 Embedding Model로 변환한다.
- Embedding Dimension은 Vector DB Schema와 일치해야 한다.
- 문서 수정 시 Embedding 재생성을 고려한다.
- Chunk는 독립 검색 가능하게 작성한다.
- FAQ와 Retrieval Queries를 포함해 Query Matching을 강화한다.

---

### [FAQ]

Q. Embedding이 뭐야?

A.
Embedding은 텍스트를 의미 기반 숫자 Vector로 변환하는 기술이다.

Q. Embedding API는 뭐에 써?

A.
문서 검색, Semantic Search, RAG Retrieval, 유사도 비교, Agent Memory 검색에 사용한다.

Q. Embedding Model과 Chat Model 차이는?

A.
Embedding Model은 검색용 Vector를 만들고, Chat Model은 답변을 생성한다.

Q. Embedding은 답변을 생성해?

A.
아니다. Embedding은 답변 생성이 아니라 의미 검색과 유사도 비교에 사용된다.

---

## 1.2 Embedding API Request

### [개념]

Embedding API Request는 텍스트 입력을 Embedding Model에 전달해 Vector를 생성하는 요청이다.

Embedding API는 일반적으로 Model 이름과 Input Text를 포함한다.

Request 구성:

- model
- input
- encoding_format
- dimensions
- user metadata

---

### [핵심]

- `model`은 사용할 Embedding Model을 지정한다.
- `input`은 Vector로 변환할 텍스트이다.
- 하나의 요청에 단일 텍스트 또는 여러 텍스트를 보낼 수 있다.
- Provider마다 입력 길이 제한이 있다.
- 긴 문서는 Chunking 후 Embedding해야 한다.
- Empty Text는 Embedding하지 않는다.
- Input Text 정규화 기준을 정해야 한다.

---

### [실무]

Embedding Request 예:

```json
{
  "model": "embedding-model-name",
  "input": "LLM API에서 Timeout은 요청이 무한 대기하지 않도록 설정한다."
}
```

Batch Embedding Request 예:

```json
{
  "model": "embedding-model-name",
  "input": [
    "Chat Completion은 messages 배열을 기반으로 응답을 생성한다.",
    "Embedding은 텍스트를 Vector로 변환해 Semantic Search에 사용한다.",
    "RAG는 검색된 Context를 Prompt에 넣어 답변을 생성한다."
  ]
}
```

요청 처리 기준:

```text
Validate Input Text
→ Normalize Text
→ Split Long Text
→ Call Embedding API
→ Validate Vector
→ Store Vector
```

Input 검증 항목:

| 항목           | 기준                        |
| -------------- | --------------------------- |
| Empty Text     | Embedding 금지              |
| Text Length    | 모델 입력 제한 확인         |
| Encoding       | UTF-8 기준                  |
| Duplicate Text | 필요 시 중복 제거           |
| Sensitive Data | 저장 정책 확인              |
| Metadata       | 문서명, 섹션, Chunk ID 포함 |

주의:

- 긴 문서를 통째로 Embedding하지 않는다.
- API Key를 코드에 하드코딩하지 않는다.
- Timeout 없이 Embedding API를 호출하지 않는다.
- Batch 요청은 Rate Limit과 Payload Size를 고려한다.
- 입력 전처리 방식이 바뀌면 기존 Embedding과 검색 품질이 달라질 수 있다.

---

### [FAQ]

Q. Embedding API Request에는 뭐가 들어가?

A.
Embedding Model 이름과 Vector로 변환할 Input Text가 들어간다.

Q. 긴 문서를 한 번에 Embedding해도 돼?

A.
권장하지 않는다. Chunking 후 각 Chunk를 Embedding하는 것이 좋다.

Q. Batch Embedding은 뭐야?

A.
여러 텍스트를 한 번의 요청으로 Embedding하는 방식이다.

Q. Empty Text도 Embedding해도 돼?

A.
안 된다. 빈 문자열은 검색 품질을 해치므로 제외해야 한다.

---

## 1.3 Embedding API Response

### [개념]

Embedding API Response는 입력 텍스트에 대한 Vector 값을 반환하는 응답이다.

Embedding Vector는 숫자 배열이며 Vector DB에 저장하거나 유사도 계산에 사용한다.

Response 구성:

- object
- data
- embedding
- index
- model
- usage

---

### [핵심]

- Embedding Vector는 숫자 배열이다.
- Vector Dimension은 모델마다 다르다.
- Vector Dimension은 Vector DB Index와 일치해야 한다.
- Usage 정보는 Token 비용 추적에 사용한다.
- 응답 Vector가 비어 있거나 Dimension이 다르면 실패 처리한다.
- Batch Embedding에서는 입력 순서와 응답 index를 매칭해야 한다.

---

### [실무]

Embedding Response 예:

```json
{
  "object": "list",
  "data": [
    {
      "object": "embedding",
      "index": 0,
      "embedding": [0.012, -0.034, 0.087]
    }
  ],
  "model": "embedding-model-name",
  "usage": {
    "prompt_tokens": 12,
    "total_tokens": 12
  }
}
```

Response Validation Flow:

```text
Embedding Response
→ data exists
→ embedding exists
→ vector not empty
→ dimension match
→ numeric values valid
→ index match
→ store vector
```

검증 항목:

| 항목      | 검증                   |
| --------- | ---------------------- |
| data      | 비어 있지 않아야 함    |
| embedding | 숫자 배열              |
| dimension | Vector DB 설정과 일치  |
| index     | Batch 입력 순서와 일치 |
| usage     | Optional 처리          |
| model     | 기대 모델과 일치       |
| error     | 오류 응답 분리         |

주의:

- Vector Dimension 불일치는 저장 실패 또는 검색 오류를 만든다.
- Batch Response에서 index를 무시하면 문서와 Vector가 잘못 매핑될 수 있다.
- Usage가 항상 제공된다고 가정하지 않는다.
- Vector를 로그에 과도하게 남기지 않는다.
- Model 변경 시 기존 Vector 재생성이 필요할 수 있다.

---

### [FAQ]

Q. Embedding API Response는 뭐야?

A.
입력 텍스트를 Vector로 변환한 숫자 배열과 Metadata를 반환하는 응답이다.

Q. Vector Dimension은 왜 중요해?

A.
Vector Dimension이 Vector DB Index와 일치해야 저장과 검색이 정상 동작하기 때문이다.

Q. Batch Embedding 응답에서 index는 왜 봐야 해?

A.
입력 텍스트와 반환된 Vector를 정확히 매칭해야 하기 때문이다.

Q. Embedding Response도 검증해야 해?

A.
그렇다. Empty Vector, Dimension 불일치, index 불일치, 오류 응답을 확인해야 한다.

---

# 2. Vector and Similarity Search

## 2.1 Vector

### [개념]

Vector는 Embedding Model이 생성한 숫자 배열이다.

Vector는 텍스트의 의미를 수치 공간에 표현한다.

의미가 비슷한 텍스트는 Vector 공간에서 가까운 위치에 배치된다.

Vector Search 기본 구조:

```text
Query Text
→ Query Vector
→ Compare with Document Vectors
→ Similarity Score
→ Top-K Results
```

---

### [핵심]

- Vector는 텍스트 의미를 나타내는 숫자 배열이다.
- Vector Dimension은 Embedding Model에 의해 결정된다.
- Query와 Document는 같은 모델로 Embedding해야 한다.
- Vector Search는 유사도 점수로 관련 문서를 찾는다.
- Vector 자체는 사람이 읽기 어렵다.
- Vector와 원본 Chunk Metadata를 함께 저장해야 한다.

---

### [실무]

Vector 저장 구조 예:

```json
{
  "id": "chunk-001",
  "document": "LLM_Core_API_Integration_Part07",
  "section": "Embedding",
  "content": "Embedding은 텍스트를 의미 기반 Vector로 변환한다.",
  "embedding": [0.012, -0.034, 0.087],
  "metadata": {
    "domain": "LLM_Core_API_Integration",
    "part": "Part07",
    "type": "concept"
  }
}
```

Vector 저장 기준:

| 항목      | 설명                     |
| --------- | ------------------------ |
| id        | Chunk 고유 식별자        |
| content   | 원본 Chunk Text          |
| embedding | Vector 값                |
| metadata  | 문서명, 섹션, 도메인     |
| model     | Embedding Model 이름     |
| dimension | Vector Dimension         |
| version   | 문서 또는 Embedding 버전 |

주의:

- Vector만 저장하고 원본 Text를 잃으면 답변 근거를 구성하기 어렵다.
- Metadata가 부족하면 검색 결과 필터링이 어렵다.
- Embedding Model이 바뀌면 기존 Vector와 신규 Vector를 섞지 않는다.
- Vector DB Index 설정은 Dimension과 Metric에 맞춰야 한다.

---

### [FAQ]

Q. Vector가 뭐야?

A.
Embedding Model이 텍스트 의미를 숫자 배열로 표현한 데이터다.

Q. Vector만 있으면 RAG 답변이 가능해?

A.
아니다. Vector는 검색용이고, 최종 답변에는 원본 Chunk Text가 필요하다.

Q. Query와 문서는 같은 Embedding Model을 써야 해?

A.
그렇다. 같은 Vector 공간에서 비교해야 유사도 검색이 의미를 가진다.

Q. Vector와 Metadata를 같이 저장해야 하는 이유는?

A.
검색 결과의 문서명, 섹션, 출처, 필터링 기준을 유지하기 위해 필요하다.

---

## 2.2 Similarity Search

### [개념]

Similarity Search는 Query Vector와 Document Vector 간의 유사도를 계산해 관련 문서를 찾는 검색 방식이다.

Similarity Search는 RAG Retrieval의 핵심 단계이다.

대표 Similarity Metric:

- Cosine Similarity
- Dot Product
- Euclidean Distance
- Inner Product

---

### [핵심]

- Similarity Search는 의미적으로 가까운 Chunk를 검색한다.
- 유사도 점수가 높다고 항상 답변에 적합한 것은 아니다.
- Metric은 Vector DB와 Embedding Model 특성에 맞춰 선택한다.
- Top-K 결과는 Reranking과 Filtering이 필요할 수 있다.
- Keyword가 중요한 질의는 Vector Search만으로 부족할 수 있다.
- Hybrid Search를 사용하면 Keyword와 Semantic Search를 함께 활용할 수 있다.

---

### [실무]

Similarity Search Flow:

```text
User Query
→ Query Embedding
→ Vector DB Search
→ Similarity Score
→ Top-K Candidates
→ Reranking
→ Context Filtering
→ Retrieved Context
```

검색 결과 예:

```json
{
  "results": [
    {
      "chunkId": "chunk-017",
      "score": 0.89,
      "document": "LLM_Core_API_Integration_Part05",
      "section": "Streaming Response",
      "content": "Streaming Response는 Chunk를 순차적으로 전달한다."
    }
  ]
}
```

Similarity Search 판단 기준:

| 기준            | 설명                     |
| --------------- | ------------------------ |
| Score           | 의미 유사도              |
| Keyword Match   | 핵심 용어 포함 여부      |
| Section Match   | 질문 의도와 섹션 적합성  |
| Metadata Filter | Domain, Part, Version    |
| Freshness       | 문서 최신성              |
| Completeness    | 답변 가능 정보 포함 여부 |
| Redundancy      | 중복 결과 여부           |

주의:

- Score만 기준으로 최종 Context를 선택하지 않는다.
- 유사도는 높지만 질문 의도와 맞지 않는 Chunk가 있을 수 있다.
- 숫자, 코드, 설정값, API 필드명은 Keyword Search가 더 중요할 수 있다.
- Top-K를 과도하게 높이면 Context Window를 낭비한다.
- 검색 결과 없음과 시스템 오류를 구분한다.

---

### [FAQ]

Q. Similarity Search가 뭐야?

A.
Query Vector와 Document Vector의 유사도를 계산해 관련 문서를 찾는 검색 방식이다.

Q. 유사도 점수가 높으면 무조건 좋은 결과야?

A.
아니다. 질문 의도, 키워드, 섹션, 최신성, 답변 가능성을 함께 봐야 한다.

Q. Vector Search만 쓰면 충분해?

A.
항상 그렇지 않다. API 필드명, 코드, 정확한 키워드는 Keyword Search나 Hybrid Search가 필요할 수 있다.

Q. Top-K는 높을수록 좋아?

A.
아니다. 관련 없는 Chunk가 늘어나면 답변 품질과 비용이 나빠질 수 있다.

---

## 2.3 Similarity Metric

### [개념]

Similarity Metric은 Vector 간 유사도를 계산하는 기준이다.

Metric 선택은 검색 결과 순위와 RAG 답변 품질에 영향을 준다.

대표 Metric:

- Cosine Similarity
- Dot Product
- Euclidean Distance
- Inner Product

---

### [핵심]

- Cosine Similarity는 Vector 방향의 유사도를 본다.
- Dot Product는 Vector 크기와 방향을 함께 반영할 수 있다.
- Euclidean Distance는 Vector 간 거리를 계산한다.
- Embedding Model과 Vector DB가 권장하는 Metric을 우선한다.
- Metric이 잘못 설정되면 검색 품질이 낮아진다.
- 기존 Index의 Metric을 바꾸면 재색인이 필요할 수 있다.

---

### [실무]

Metric 비교:

| Metric             | 기준        | 사용                       |
| ------------------ | ----------- | -------------------------- |
| Cosine Similarity  | 방향 유사도 | 일반 Semantic Search       |
| Dot Product        | 내적 점수   | 일부 Embedding Model       |
| Inner Product      | 내적 기반   | Vector DB 설정에 따라 사용 |
| Euclidean Distance | 거리 기반   | 특정 Vector 공간           |

Metric 선택 Flow:

```text
Check Embedding Model Recommendation
→ Check Vector DB Support
→ Create Index with Metric
→ Evaluate Retrieval Quality
→ Tune if Needed
```

주의:

- Embedding Model의 권장 Metric을 확인한다.
- 같은 Vector를 다른 Metric으로 검색하면 결과가 달라질 수 있다.
- Vector Normalization 여부가 Metric 선택에 영향을 준다.
- 운영 중 Metric 변경은 기존 Vector Index 재구성이 필요할 수 있다.
- Metric보다 Chunk 품질이 더 큰 영향을 주는 경우도 많다.

---

### [FAQ]

Q. Similarity Metric이 뭐야?

A.
Vector 간 의미적 가까움을 계산하는 기준이다.

Q. Cosine Similarity는 뭐야?

A.
Vector의 방향이 얼마나 비슷한지 계산하는 유사도 방식이다.

Q. Metric은 아무거나 써도 돼?

A.
아니다. Embedding Model과 Vector DB가 권장하는 Metric을 사용하는 것이 좋다.

Q. Metric을 바꾸면 기존 Vector를 그대로 써도 돼?

A.
가능한 경우도 있지만 검색 품질이 달라지므로 재평가와 재색인이 필요할 수 있다.

---

# 3. Document Embedding Pipeline

## 3.1 Document Chunking

### [개념]

Document Chunking은 긴 문서를 검색 가능한 작은 단위로 나누는 과정이다.

RAG에서 검색은 보통 Chunk 단위로 이루어진다.

Chunk 품질은 Retrieval 품질과 LLM 답변 품질을 결정한다.

Chunking Flow:

```text
Document
→ Section Split
→ Chunk Split
→ Metadata Attach
→ Embedding
→ Vector Store
```

---

### [핵심]

- Chunk는 독립 검색되어도 의미를 유지해야 한다.
- 하나의 Chunk에는 하나의 핵심 개념이 적합하다.
- 너무 긴 Chunk는 검색 정밀도를 낮춘다.
- 너무 짧은 Chunk는 맥락 부족을 만든다.
- Heading, FAQ, Retrieval Queries는 검색 적중률을 높인다.
- 코드 예제는 짧고 직접적으로 포함한다.
- Metadata는 문서명, 섹션, 도메인, Part를 포함한다.

---

### [실무]

권장 Chunk 구조:

```text
## 1.1 Embedding

### [개념]
Embedding 정의

### [핵심]
핵심 bullet

### [실무]
실무 기준

### [FAQ]
Q/A
```

Chunk Metadata 예:

```json
{
  "chunkId": "llm-core-part07-001",
  "document": "LLM_Core_API_Integration_Part07",
  "section": "Embedding",
  "domain": "LLM_Core_API_Integration",
  "part": "Part07",
  "category": "concept"
}
```

Chunking 기준:

| 항목       | 기준                    |
| ---------- | ----------------------- |
| Chunk Size | 300~1200 tokens 권장    |
| Concept    | 하나의 핵심 개념        |
| Heading    | 명확한 검색 키워드 포함 |
| FAQ        | 실제 사용자 질문 형태   |
| Code       | 짧은 핵심 Snippet       |
| Metadata   | 문서 추적 가능          |
| Overlap    | 필요한 문맥만           |

주의:

- 긴 문서를 통째로 Embedding하지 않는다.
- 서로 다른 개념을 하나의 Chunk에 과도하게 섞지 않는다.
- Chunk가 너무 작으면 검색 후 답변 근거가 부족하다.
- 중복 Chunk가 많으면 Context Window를 낭비한다.
- RAG 문서는 사람용 에세이보다 Retrieval 품질을 우선한다.

---

### [FAQ]

Q. Document Chunking이 뭐야?

A.
긴 문서를 검색 가능한 작은 단위로 나누는 과정이다.

Q. Chunk가 중요한 이유는?

A.
RAG 검색은 Chunk 단위로 이루어지므로 Chunk 품질이 답변 품질을 결정하기 때문이다.

Q. 좋은 Chunk 기준은?

A.
하나의 개념을 명확한 제목, 핵심 설명, 실무 기준, FAQ로 독립 검색 가능하게 구성하는 것이다.

Q. Chunk가 너무 길면 어떻게 돼?

A.
검색 정밀도가 낮아지고 Context Window를 많이 사용한다.

---

## 3.2 Chunk Embedding

### [개념]

Chunk Embedding은 문서 Chunk를 Embedding Model로 Vector화하는 과정이다.

각 Chunk는 원본 Text, Metadata, Vector를 함께 저장해야 한다.

Chunk Embedding Flow:

```text
Chunk Text
+ Metadata
→ Embedding API
→ Vector
→ Validate Dimension
→ Store in Vector DB
```

---

### [핵심]

- Chunk 단위로 Embedding해야 검색 결과가 세밀해진다.
- Chunk Text와 Metadata를 함께 저장한다.
- Embedding Model 이름과 버전을 기록한다.
- Vector Dimension을 검증한다.
- 중복 Chunk는 필요 시 제거한다.
- 문서가 변경되면 해당 Chunk의 Embedding을 갱신한다.
- 실패한 Chunk는 재처리 Queue에 넣는다.

---

### [실무]

Chunk Embedding Pipeline:

```text
Load Markdown Files
→ Parse Sections
→ Build Chunks
→ Attach Metadata
→ Batch Embedding
→ Validate Vectors
→ Upsert Vector DB
→ Log Result
```

Chunk 저장 예:

```json
{
  "id": "chunk-llm-007-embedding",
  "text": "Embedding은 텍스트를 의미 기반 Vector로 변환한다.",
  "vector": [0.012, -0.034, 0.087],
  "metadata": {
    "fileName": "LLM_Core_API_Integration_Part07_Embedding_API_RAG_Integration.md",
    "title": "Embedding API",
    "domain": "LLM_Core_API_Integration",
    "embeddingModel": "bge-m3"
  }
}
```

Batch 처리 기준:

| 항목         | 기준                       |
| ------------ | -------------------------- |
| Batch Size   | API 제한과 Rate Limit 고려 |
| Retry        | 일시적 오류만 제한적 적용  |
| Failed Chunk | 재처리 대상                |
| Duplicate    | Hash로 탐지 가능           |
| Version      | 문서 버전 기록             |
| Logging      | 성공/실패 수 기록          |

주의:

- Batch 실패 시 전체를 성공으로 처리하지 않는다.
- 일부 Chunk 실패를 누락하면 검색 공백이 생긴다.
- Embedding Model이 변경되면 기존 Vector와 혼합하지 않는다.
- Metadata 누락은 검색 필터링과 출처 표시를 어렵게 한다.
- Embedding API 비용과 Rate Limit을 고려한다.

---

### [FAQ]

Q. Chunk Embedding이 뭐야?

A.
문서 Chunk를 Embedding Model로 Vector화하는 과정이다.

Q. Chunk Text와 Metadata를 같이 저장해야 해?

A.
그렇다. 최종 답변에 원본 근거와 출처를 제공하려면 필요하다.

Q. 문서가 수정되면 Embedding도 다시 해야 해?

A.
수정된 Chunk는 Embedding을 재생성해야 검색 결과가 최신 문서를 반영한다.

Q. Batch Embedding 실패 시 어떻게 해?

A.
실패한 Chunk를 기록하고 재처리해야 한다.

---

## 3.3 Embedding Versioning

### [개념]

Embedding Versioning은 Embedding Model, 문서 버전, Chunking 방식, Vector Index 설정의 변경 이력을 관리하는 것이다.

Embedding Versioning은 검색 품질 유지와 재색인 판단에 필요하다.

Versioning 대상:

- Embedding Model
- Model Version
- Vector Dimension
- Similarity Metric
- Chunking Rule
- Document Version
- Metadata Schema
- Vector Index Version

---

### [핵심]

- Embedding Model이 바뀌면 Vector 공간이 달라질 수 있다.
- 서로 다른 Embedding Model의 Vector를 같은 Index에 섞으면 검색 품질이 나빠진다.
- Chunking Rule이 바뀌면 기존 Chunk ID와 검색 결과가 달라진다.
- Vector Dimension이 바뀌면 기존 Index와 호환되지 않을 수 있다.
- 문서 변경 시 변경된 Chunk만 재Embedding할 수 있다.
- Version Metadata가 없으면 문제 추적이 어렵다.

---

### [실무]

Version Metadata 예:

```json
{
  "chunkId": "llm-part07-001",
  "documentVersion": "2026-06-30",
  "embeddingModel": "bge-m3",
  "embeddingVersion": "v1",
  "chunkingRuleVersion": "rag-master-v3",
  "dimension": 1024,
  "metric": "cosine"
}
```

재Embedding 필요 상황:

| 변경                  | 재Embedding 필요                 |
| --------------------- | -------------------------------- |
| 문서 내용 수정        | 해당 Chunk 필요                  |
| Chunking Rule 변경    | 전체 또는 관련 문서 필요         |
| Embedding Model 변경  | 전체 필요                        |
| Vector Dimension 변경 | 전체 필요                        |
| Metadata만 추가       | Vector 재생성 불필요 가능        |
| 오타 수정             | 검색 영향 있으면 해당 Chunk 필요 |

운영 기준:

```text
Document Change Detected
→ Identify Changed Chunks
→ Compare Version
→ Re-embed Changed Chunks
→ Update Vector DB
→ Remove Old Chunks
```

주의:

- 새 Embedding과 기존 Embedding을 무분별하게 섞지 않는다.
- Vector DB Upsert 시 old chunk 삭제 기준이 필요하다.
- Version 정보 없이 검색 품질 저하 원인을 찾기 어렵다.
- Model 변경은 비용과 시간 계획이 필요하다.
- 운영 중 Reindex는 점진적으로 처리할 수 있다.

---

### [FAQ]

Q. Embedding Versioning이 뭐야?

A.
Embedding Model, 문서 버전, Chunking Rule, Vector Index 설정 변경 이력을 관리하는 것이다.

Q. Embedding Model이 바뀌면 다시 Embedding해야 해?

A.
일반적으로 필요하다. Vector 공간이 달라져 기존 Vector와 섞으면 검색 품질이 떨어질 수 있다.

Q. 문서 일부만 수정되면 전체를 다시 해야 해?

A.
변경된 Chunk만 재Embedding할 수 있다.

Q. Version Metadata가 왜 필요해?

A.
검색 품질 저하, 문서 변경, 모델 변경 원인을 추적하기 위해 필요하다.

---

# 4. Query Embedding and Retrieval

## 4.1 Query Embedding

### [개념]

Query Embedding은 사용자 질문이나 검색 Query를 Embedding Model로 Vector화하는 과정이다.

Query Vector는 Document Chunk Vector와 비교되어 관련 문서를 찾는 데 사용된다.

Query Embedding Flow:

```text
User Query
→ Query Rewrite
→ Query Embedding
→ Vector Search
→ Retrieved Chunks
```

---

### [핵심]

- Query와 Document는 같은 Embedding Model을 사용해야 한다.
- Query가 모호하면 Query Rewrite가 필요할 수 있다.
- 대화 맥락이 생략된 질문은 Context를 보강해야 한다.
- Query Embedding 입력은 검색 의도를 명확히 담아야 한다.
- 너무 긴 Query는 핵심 키워드 중심으로 정리할 수 있다.
- Query Embedding 결과도 Vector Dimension을 검증한다.

---

### [실무]

Query Rewrite 예:

```text
Original Query:
"이거 스트리밍에서 끊기면?"

Rewritten Query:
"LLM Streaming Response Timeout Stream Failure Partial Output Handling"
```

Query Embedding 처리 기준:

```text
Receive User Query
→ Resolve Conversation Context
→ Rewrite Query if Needed
→ Validate Query
→ Generate Query Embedding
→ Search Vector DB
```

Query 보강 기준:

| 상황           | 보강                                       |
| -------------- | ------------------------------------------ |
| 지시어 생략    | 현재 주제 추가                             |
| 대화체 표현    | 도메인 키워드 추가                         |
| 오타           | 교정 가능                                  |
| 너무 짧은 질문 | 핵심 개념 확장                             |
| 코드 질문      | 파일명, 클래스명, 메서드명 포함            |
| 실무 질문      | Best Practice, Troubleshooting 키워드 포함 |

주의:

- Query Rewrite가 사용자 의도를 바꾸면 안 된다.
- 검색 Query와 최종 답변 기준 질문을 구분한다.
- Query를 너무 많은 키워드로 확장하면 노이즈가 생길 수 있다.
- Query Embedding 실패 시 검색을 진행하지 않는다.
- 최신 정보가 필요한 Query는 RAG 검색보다 Web Search Tool이 필요할 수 있다.

---

### [FAQ]

Q. Query Embedding이 뭐야?

A.
사용자 질문을 Embedding Model로 Vector화해 문서 Vector와 비교할 수 있게 만드는 과정이다.

Q. Query와 Document는 같은 Embedding Model을 써야 해?

A.
그렇다. 같은 Vector 공간에서 비교해야 검색이 의미를 가진다.

Q. Query Rewrite는 왜 필요해?

A.
사용자 질문이 짧거나 모호하거나 대화체일 때 검색 품질을 높이기 위해 필요하다.

Q. Query Rewrite가 원래 질문을 바꿔도 돼?

A.
안 된다. 검색 키워드를 보강하되 사용자 의도는 유지해야 한다.

---

## 4.2 Top-K Retrieval

### [개념]

Top-K Retrieval은 Similarity Search 결과 중 유사도 점수가 높은 상위 K개의 Chunk를 선택하는 과정이다.

Top-K는 RAG Prompt에 포함될 Retrieved Context 양을 결정한다.

Top-K Retrieval Flow:

```text
Query Vector
→ Similarity Search
→ Sort by Score
→ Select Top-K
→ Filter / Rerank
→ Context
```

---

### [핵심]

- Top-K가 높으면 더 많은 Chunk를 가져온다.
- Top-K가 낮으면 필요한 근거를 놓칠 수 있다.
- Top-K가 너무 높으면 관련 없는 Context가 늘어난다.
- Retrieved Context가 많으면 비용과 Latency가 증가한다.
- Top-K 결과는 Reranking과 Filtering이 필요할 수 있다.
- 질문 유형에 따라 Top-K를 다르게 설정한다.

---

### [실무]

Top-K 기준:

| 질문 유형       | Top-K 기준                   |
| --------------- | ---------------------------- |
| 단순 정의       | 3~5                          |
| 실무 방법       | 5~8                          |
| 코드 생성       | 5~10                         |
| Troubleshooting | 5~10                         |
| 비교 질문       | 6~10                         |
| 긴 문서 요약    | Section 단위 Retrieval       |
| Multi-hop 질문  | Query 분해 후 개별 Retrieval |

Top-K 처리 예:

```json
{
  "query": "LLM API Timeout 처리 방법",
  "topK": 5,
  "filters": {
    "domain": "LLM_Core_API_Integration"
  }
}
```

동적 Top-K 전략:

```text
Simple Query
→ Low Top-K

Complex Query
→ Query Decomposition
→ Multiple Retrieval
→ Reranking
→ Final Context Selection
```

주의:

- Top-K를 무조건 높게 설정하지 않는다.
- Top-K 결과를 그대로 Prompt에 모두 넣지 않는다.
- 중복 Chunk는 제거한다.
- Score가 낮은 Chunk는 제외한다.
- Context Window와 Output Reserve를 함께 고려한다.

---

### [FAQ]

Q. Top-K Retrieval이 뭐야?

A.
검색 결과 중 유사도 점수가 높은 상위 K개의 Chunk를 선택하는 과정이다.

Q. Top-K는 높을수록 좋아?

A.
아니다. 관련 없는 Chunk가 늘어나면 비용과 Hallucination이 증가할 수 있다.

Q. Top-K는 어떻게 정해?

A.
질문 복잡도, 답변 유형, Context Window, RAG 품질 기준에 따라 조정한다.

Q. Top-K 결과는 그대로 Prompt에 넣어도 돼?

A.
권장하지 않는다. Reranking, Filtering, Deduplication 후 넣는 것이 좋다.

---

## 4.3 Reranking

### [개념]

Reranking은 1차 검색된 Candidate Chunk를 Query 의도에 맞게 다시 정렬하는 과정이다.

Reranking은 Vector Search의 한계를 보완하고 최종 Context 품질을 높인다.

Reranking Flow:

```text
Initial Top-K Results
→ Evaluate Relevance
→ Reorder Results
→ Remove Low Relevance
→ Select Final Context
```

---

### [핵심]

- Reranking은 검색 결과 순위를 재정렬한다.
- Vector Similarity만으로 부족한 경우 유용하다.
- Query Intent, Keyword Match, Section Match를 반영할 수 있다.
- Cross-Encoder Reranker 또는 LLM 기반 Reranking을 사용할 수 있다.
- Reranking은 비용과 Latency를 증가시킬 수 있다.
- 최종 Context 품질이 RAG 답변 품질에 중요하다.

---

### [실무]

Reranking 기준:

| 기준            | 설명                                |
| --------------- | ----------------------------------- |
| Query Intent    | 질문 의도와 직접 관련               |
| Keyword Match   | 핵심 용어 포함                      |
| Section Type    | [실무], [FAQ], [Troubleshooting] 등 |
| Source Priority | MASTER → DOMAIN → PART              |
| Freshness       | 최신 문서 우선                      |
| Completeness    | 답변에 필요한 정보 포함             |
| Redundancy      | 중복 제거                           |

Reranking 예:

```text
Query:
"Tool Arguments 검증은 왜 필요해?"

Initial Results:
1. Tool Calling 개념
2. Tool Result 처리
3. Argument Validation

Reranked:
1. Argument Validation
2. Safety Check
3. Tool Calling 개념
```

주의:

- Reranking 비용이 큰 경우 모든 요청에 적용하지 않는다.
- 간단한 FAQ는 Vector Search만으로 충분할 수 있다.
- Reranking 결과가 원문 Query 의도와 맞는지 검증한다.
- Reranking 후에도 Missing Information이 가능하다.
- Reranking 로그를 통해 Retrieval 품질을 개선한다.

---

### [FAQ]

Q. Reranking이 뭐야?

A.
1차 검색 결과를 Query 의도에 맞게 다시 정렬하는 과정이다.

Q. Reranking은 왜 필요해?

A.
Vector 유사도만으로는 가장 적합한 Chunk가 상위에 오지 않을 수 있기 때문이다.

Q. Reranking은 항상 해야 해?

A.
아니다. 복잡한 질문이나 검색 품질이 낮은 경우에 우선 적용한다.

Q. Reranking 기준은 뭐야?

A.
질문 의도, 키워드 일치, 섹션 적합성, 문서 우선순위, 최신성, 중복 여부를 본다.

---

# 5. RAG Prompt Integration

## 5.1 Retrieved Context Assembly

### [개념]

Retrieved Context Assembly는 검색된 Chunk를 LLM Prompt에 넣기 적합한 형태로 구성하는 과정이다.

Retrieved Context Assembly는 RAG 답변의 근거성과 안정성에 직접 영향을 준다.

Assembly Flow:

```text
Retrieved Chunks
→ Deduplicate
→ Sort / Rerank
→ Attach Metadata
→ Trim Context
→ Build Prompt Context
```

---

### [핵심]

- Retrieved Context는 User Question과 명확히 구분한다.
- 각 Chunk에는 출처 Metadata를 포함하는 것이 좋다.
- 관련 없는 Chunk는 제거한다.
- 중복 Chunk는 제거한다.
- Context Window와 Output Reserve를 고려해 길이를 제한한다.
- 문서 우선순위를 반영한다.
- 답변 생성 전 Context가 충분한지 확인한다.

---

### [실무]

Retrieved Context Format 예:

```text
[Document]
LLM_Core_API_Integration_Part07_Embedding_API_RAG_Integration.md

[Section]
Embedding API

[Content]
Embedding은 텍스트를 의미 기반 Vector로 변환한다.
Embedding Model은 Chat Model과 역할이 다르다.

[Metadata]
domain=LLM_Core_API_Integration
part=Part07
score=0.91
```

Prompt Assembly 예:

```text
System:
You are a RAG-based assistant.
Answer only using Retrieved Context.

Retrieved Context:
{retrieved_context}

User Question:
{user_question}

Rule:
If the answer is not found in Retrieved Context, say "문서에서 확인되지 않습니다."
```

Context Assembly 기준:

| 항목          | 기준      |
| ------------- | --------- |
| Document Name | 포함 권장 |
| Section Title | 포함 권장 |
| Chunk Content | 필수      |
| Score         | 선택      |
| Domain        | 필터링용  |
| Version       | 충돌 처리 |
| Token Length  | 제한      |
| Deduplication | 필수      |

주의:

- Retrieved Context와 User Question을 한 문단에 섞지 않는다.
- Context가 길면 RAG 답변 품질이 항상 좋아지는 것은 아니다.
- Chunk 순서가 답변에 영향을 줄 수 있다.
- 서로 충돌하는 Context는 충돌을 명시하거나 우선순위를 적용한다.
- Context 부족 시 Missing Information으로 처리한다.

---

### [FAQ]

Q. Retrieved Context Assembly가 뭐야?

A.
검색된 Chunk를 LLM Prompt에 넣기 적합한 형태로 구성하는 과정이다.

Q. Retrieved Context에 Metadata가 필요한 이유는?

A.
출처 표시, 문서 우선순위, 필터링, 충돌 처리에 필요하기 때문이다.

Q. Retrieved Context와 User Question은 분리해야 해?

A.
그렇다. 모델이 근거 문서와 사용자 요청을 혼동하지 않도록 분리해야 한다.

Q. Context가 부족하면 어떻게 해?

A.
추가 검색을 하거나 문서에서 확인되지 않는다고 답해야 한다.

---

## 5.2 Grounded Prompt

### [개념]

Grounded Prompt는 LLM이 Retrieved Context에 근거해서만 답변하도록 제한하는 Prompt 구조이다.

Grounded Prompt는 RAG Hallucination을 줄이는 핵심 장치이다.

Grounded Prompt 구성:

- Role
- Retrieved Context
- User Question
- Grounding Rule
- Missing Information Rule
- Output Format
- Citation Rule

---

### [핵심]

- LLM은 Retrieved Context를 우선해야 한다.
- 문서에 없는 내용은 추측하지 않는다.
- 일반 지식을 사용할지 여부를 명확히 지정한다.
- Missing Information Rule을 포함한다.
- 답변 형식과 길이를 제한한다.
- 가능하면 출처나 문서명을 함께 제공한다.

---

### [실무]

Grounded Prompt 예:

```text
You are a RAG-based assistant for LLM API integration.

Rules:
- Answer only using Retrieved Context.
- Do not guess.
- Do not use outside knowledge unless explicitly allowed.
- If the answer is missing, say "문서에서 확인되지 않습니다."
- Keep the answer concise.

Retrieved Context:
{context}

User Question:
{question}

Output Format:
- Answer
- Evidence
- Missing Information
```

JSON Grounded Output 예:

```json
{
  "status": "success",
  "answer": "Embedding은 텍스트를 의미 기반 Vector로 변환해 Semantic Search에 사용한다.",
  "evidence": [
    {
      "document": "LLM_Core_API_Integration_Part07",
      "section": "Embedding"
    }
  ],
  "missingInformation": []
}
```

주의:

- Grounded Prompt가 있어도 검증은 필요하다.
- Retrieved Context가 부정확하면 답변도 부정확할 수 있다.
- 일반 지식을 허용할 경우 문서 근거와 구분한다.
- 답변이 Context 밖으로 확장되면 Review 단계에서 차단한다.
- Citation이 필요한 시스템은 Chunk ID를 보존한다.

---

### [FAQ]

Q. Grounded Prompt가 뭐야?

A.
LLM이 검색된 문서 Context에 근거해서만 답변하도록 제한하는 Prompt 구조다.

Q. Grounded Prompt는 왜 필요해?

A.
RAG 답변에서 Hallucination과 근거 없는 추측을 줄이기 위해 필요하다.

Q. 문서에 없는 내용은 어떻게 답해야 해?

A.
문서에서 확인되지 않는다고 답해야 한다.

Q. Grounded Prompt만 있으면 검증이 필요 없어?

A.
아니다. 최종 답변이 Retrieved Context와 일치하는지 검증해야 한다.

---

## 5.3 RAG Answer Validation

### [개념]

RAG Answer Validation은 LLM이 생성한 답변이 Retrieved Context와 일치하는지 검증하는 과정이다.

RAG Answer Validation은 근거 없는 답변, 문서 왜곡, Hallucination을 줄인다.

Validation Flow:

```text
Generated Answer
→ Extract Claims
→ Compare with Retrieved Context
→ Check Missing Claims
→ Check Contradictions
→ Approve or Reject
```

---

### [핵심]

- 답변의 핵심 Claim을 추출한다.
- 각 Claim이 Retrieved Context에 근거하는지 확인한다.
- 문서에 없는 Claim은 제거하거나 Missing Information으로 처리한다.
- 문서와 충돌하는 Claim은 실패 처리한다.
- 답변 형식이 요구사항에 맞는지 확인한다.
- Citation이 필요한 경우 Claim과 Source를 연결한다.

---

### [실무]

검증 기준:

| 검증 항목     | 설명                          |
| ------------- | ----------------------------- |
| Claim Support | 답변 주장이 Context에 있는가  |
| Contradiction | Context와 충돌하지 않는가     |
| Completeness  | 질문에 충분히 답하는가        |
| Missing Info  | 없는 정보를 추측하지 않았는가 |
| Source Match  | 출처가 맞는가                 |
| Output Format | 요구 형식을 지켰는가          |
| Safety        | 위험한 지시가 없는가          |

Validation 예:

```text
Answer:
"Embedding Model은 답변을 생성한다."

Retrieved Context:
"Embedding은 답변 생성이 아니라 검색용 Vector 생성에 사용된다."

Validation:
Contradiction
→ Reject
```

처리 기준:

```text
Supported
→ Return Answer

Partially Supported
→ Limit Answer + Missing Information

Unsupported
→ Return Missing Information

Contradicted
→ Reject and Regenerate
```

주의:

- 그럴듯한 답변도 근거가 없으면 통과시키지 않는다.
- Source가 틀리면 Citation 오류가 발생한다.
- 문서 기반 Agent는 일반 지식을 근거처럼 사용하면 안 된다.
- 검증 실패 시 무조건 재생성보다 Context 개선이 먼저일 수 있다.
- 반복 실패 시 Retrieval 품질을 점검한다.

---

### [FAQ]

Q. RAG Answer Validation이 뭐야?

A.
LLM 답변이 Retrieved Context와 일치하는지 확인하는 검증 과정이다.

Q. 왜 RAG 답변도 검증해야 해?

A.
RAG를 사용해도 LLM이 문서에 없는 내용을 생성할 수 있기 때문이다.

Q. 답변이 일부만 근거 있으면?

A.
근거 있는 부분만 답하고 부족한 정보는 Missing Information으로 표시한다.

Q. 문서와 답변이 충돌하면?

A.
답변을 거부하거나 재생성해야 한다.

---

# 6. RAG Retrieval Optimization

## 6.1 Hybrid Search

### [개념]

Hybrid Search는 Semantic Vector Search와 Keyword Search를 함께 사용하는 검색 방식이다.

Hybrid Search는 의미 기반 검색과 정확한 키워드 매칭의 장점을 결합한다.

Hybrid Search Flow:

```text
User Query
→ Vector Search
→ Keyword Search
→ Merge Results
→ Rerank
→ Final Context
```

---

### [핵심]

- Vector Search는 의미 유사도에 강하다.
- Keyword Search는 정확한 용어, API 필드명, 코드명 검색에 강하다.
- Hybrid Search는 RAG 검색 품질을 높일 수 있다.
- 점수 결합 방식이 필요하다.
- 결과 중복 제거가 필요하다.
- Query 유형에 따라 Vector와 Keyword 가중치를 다르게 줄 수 있다.

---

### [실무]

Hybrid Search가 유리한 질문:

| 질문             | 이유                 |
| ---------------- | -------------------- |
| API 필드명 검색  | 정확한 Keyword 필요  |
| 에러 코드 검색   | 정확한 문자열 필요   |
| 코드 메서드 검색 | 이름 매칭 중요       |
| 개념 설명        | Semantic Search 유리 |
| Troubleshooting  | 두 방식 모두 필요    |
| 설정값 검색      | Keyword Search 유리  |
| 유사 개념 질문   | Vector Search 유리   |

Score Merge 예:

```text
finalScore
= vectorScore * 0.7
+ keywordScore * 0.3
```

검색 전략:

```text
Concept Query
→ Vector Search 우선

Exact Field Query
→ Keyword Search 우선

Troubleshooting Query
→ Hybrid Search

Code Query
→ Keyword + Vector Search
```

주의:

- Hybrid Search는 구현 복잡도가 증가한다.
- Score Scale이 다르면 정규화가 필요하다.
- Keyword Search만 사용하면 표현이 다른 문서를 놓칠 수 있다.
- Vector Search만 사용하면 정확한 필드명 검색이 약할 수 있다.
- Merge 후 Reranking이 중요하다.

---

### [FAQ]

Q. Hybrid Search가 뭐야?

A.
Vector Search와 Keyword Search를 함께 사용해 문서를 검색하는 방식이다.

Q. Hybrid Search는 왜 필요해?

A.
의미 검색과 정확한 키워드 검색의 장점을 함께 사용하기 위해 필요하다.

Q. Vector Search만으로 부족한 경우는?

A.
API 필드명, 에러 코드, 설정값, 클래스명, 메서드명처럼 정확한 문자열이 중요한 경우다.

Q. Keyword Search만으로 부족한 경우는?

A.
사용자 질문 표현과 문서 표현이 다르지만 의미가 같은 경우다.

---

## 6.2 Metadata Filtering

### [개념]

Metadata Filtering은 Vector Search 결과를 문서명, 도메인, 섹션, 버전, 태그 같은 Metadata 기준으로 제한하는 방식이다.

Metadata Filtering은 검색 범위를 줄이고 관련도 높은 Context를 선택하는 데 도움을 준다.

Metadata 예:

- domain
- part
- document
- section
- category
- version
- language
- createdAt
- updatedAt
- sourceType

---

### [핵심]

- Metadata Filtering은 검색 범위를 제한한다.
- Domain 기반 검색에 유용하다.
- 문서 버전 충돌을 줄일 수 있다.
- Agent별 필요한 문서 범위를 제한할 수 있다.
- Metadata가 부정확하면 필요한 문서를 놓칠 수 있다.
- Metadata Schema를 일관되게 유지해야 한다.

---

### [실무]

Metadata Filter 예:

```json
{
  "query": "Tool Calling Argument Validation",
  "filters": {
    "domain": "LLM_Core_API_Integration",
    "category": "tool_calling",
    "version": "2026"
  },
  "topK": 5
}
```

Metadata 설계 기준:

| Metadata   | 용도                          |
| ---------- | ----------------------------- |
| domain     | 도메인 문서 제한              |
| part       | Part 단위 필터                |
| section    | 특정 주제 검색                |
| category   | 개념/실무/FAQ 분류            |
| version    | 최신 문서 우선                |
| sourceType | Rule, Document, Code          |
| language   | 한국어/영어 구분              |
| priority   | Master, Domain, Part 우선순위 |

Agent별 Filtering 예:

```text
Backend Agent
→ domain: SpringBoot, JPA, Security, API_Design

AI Agent
→ domain: LLM_Core_API_Integration, RAG, Agent_Workflow

Review Agent
→ sourceType: Rule + Best Practice + Troubleshooting
```

주의:

- Metadata가 누락되면 Filtering 품질이 낮아진다.
- 필터가 너무 강하면 검색 결과가 없어질 수 있다.
- 필터가 너무 약하면 관련 없는 Chunk가 섞인다.
- 문서 구조 변경 시 Metadata 업데이트가 필요하다.
- Master Rules와 Domain Rules 우선순위를 Metadata로 관리할 수 있다.

---

### [FAQ]

Q. Metadata Filtering이 뭐야?

A.
문서명, 도메인, 섹션, 버전 같은 Metadata 기준으로 검색 범위를 제한하는 방식이다.

Q. Metadata Filtering은 왜 필요해?

A.
관련 없는 문서를 줄이고 Agent나 도메인에 맞는 Context를 선택하기 위해 필요하다.

Q. 필터를 강하게 걸면 좋은가?

A.
항상 그렇지 않다. 너무 강하면 필요한 문서가 검색되지 않을 수 있다.

Q. Metadata에는 무엇을 넣어야 해?

A.
domain, document, section, part, version, category, sourceType 같은 정보를 넣는 것이 좋다.

---

## 6.3 Retrieval Queries

### [개념]

Retrieval Queries는 RAG 문서 마지막에 실제 사용자 질문 형태로 작성하는 검색 최적화 블록이다.

Retrieval Queries는 Query Pattern Matching과 Semantic Retrieval을 강화한다.

Retrieval Queries는 FAQ 형식을 사용한다.

---

### [핵심]

- Retrieval Queries는 실제 사용자가 물어볼 표현을 포함한다.
- FAQ 형태의 Q/A는 검색 적중률을 높인다.
- 동일 개념을 다양한 질문 표현으로 보강할 수 있다.
- 짧고 명확한 답변을 포함해야 한다.
- Retrieval Queries는 문서 마지막에 배치한다.
- Domain 핵심 키워드를 반복해도 된다.

---

### [실무]

Retrieval Queries 예:

```md
# Retrieval Queries

### [FAQ]

Q. Embedding API는 뭐에 써?
A. 문서나 Query를 Vector로 변환해 Semantic Search와 RAG 검색에 사용한다.

Q. Chat Model과 Embedding Model 차이는?
A. Chat Model은 답변을 생성하고 Embedding Model은 검색용 Vector를 생성한다.
```

작성 기준:

| 항목      | 기준                  |
| --------- | --------------------- |
| 질문 표현 | 실제 사용자 질문 형태 |
| 답변 길이 | 1~3줄                 |
| 키워드    | 핵심 용어 포함        |
| 중복      | 의미 있는 변형 허용   |
| 위치      | 문서 마지막           |
| 형식      | [FAQ] Q/A             |
| 목적      | Retrieval Hit 강화    |

주의:

- Q만 작성하지 않는다.
- A는 반드시 포함한다.
- 장문 답변을 쓰지 않는다.
- 문서 본문과 충돌하는 답변을 쓰지 않는다.
- Retrieval Queries는 사람용 요약이 아니라 검색 최적화 장치이다.

---

### [FAQ]

Q. Retrieval Queries가 뭐야?

A.
RAG 검색 적중률을 높이기 위해 문서 마지막에 실제 질문 형태로 작성하는 Q/A 블록이다.

Q. Retrieval Queries는 왜 필요해?

A.
사용자 질문 표현과 문서 Chunk가 더 잘 매칭되도록 돕기 때문이다.

Q. Retrieval Queries는 어디에 둬?

A.
문서 마지막에 `# Retrieval Queries` 섹션으로 둔다.

Q. Retrieval Queries에는 답변도 있어야 해?

A.
그렇다. Q만 쓰면 안 되고 짧은 A를 반드시 포함해야 한다.

---

# 7. Embedding and RAG Error Handling

## 7.1 Embedding Error Handling

### [개념]

Embedding Error Handling은 Embedding API 호출, Vector 생성, 저장, 검색 과정에서 발생하는 오류를 처리하는 방식이다.

Embedding 오류는 RAG 검색 공백과 답변 품질 저하로 이어질 수 있다.

오류 유형:

- Empty Input
- Token Limit Exceeded
- API Timeout
- Rate Limit
- Authentication Error
- Invalid Response
- Dimension Mismatch
- Vector DB Insert Failed
- Metadata Missing
- Duplicate Chunk
- Model Version Mismatch

---

### [핵심]

- Empty Input은 Embedding하지 않는다.
- Token Limit 초과 시 Chunk를 분할한다.
- Timeout과 5xx는 제한적 Retry 가능하다.
- 인증 오류는 Retry하지 않는다.
- Dimension Mismatch는 저장 전 차단한다.
- Metadata Missing은 검색 품질을 떨어뜨린다.
- 실패 Chunk는 재처리 Queue에 넣는다.
- 오류 로그에는 Chunk ID와 원인 정보를 남긴다.

---

### [실무]

Embedding Error Handling Flow:

```text
Embedding Job
→ Validate Input
→ Call Embedding API
→ Validate Response
→ Validate Dimension
→ Store Vector
→ If Failed, Log and Retry Queue
```

Error Mapping:

| Error              | Retry | 처리             |
| ------------------ | ----- | ---------------- |
| Empty Input        | 금지  | Chunk 제외       |
| Token Limit        | 금지  | Chunk 재분할     |
| Timeout            | 가능  | Backoff Retry    |
| Rate Limit         | 가능  | Retry-After      |
| 401 Unauthorized   | 금지  | API Key 확인     |
| Dimension Mismatch | 금지  | Model/Index 확인 |
| Metadata Missing   | 금지  | Metadata 재생성  |
| Insert Failed      | 가능  | DB 상태 확인     |
| Duplicate Chunk    | 금지  | Upsert 또는 Skip |

오류 로그 예:

```json
{
  "jobId": "embed-20260630-001",
  "chunkId": "llm-part07-003",
  "status": "failed",
  "errorCode": "dimension_mismatch",
  "expectedDimension": 1024,
  "actualDimension": 768,
  "retryable": false
}
```

주의:

- 실패 Chunk를 조용히 무시하지 않는다.
- Vector 저장 실패를 성공으로 기록하지 않는다.
- Rate Limit 오류를 즉시 무한 Retry하지 않는다.
- API Key나 원문 민감정보를 로그에 남기지 않는다.
- Dimension 오류는 재시도보다 설정 확인이 먼저다.

---

### [FAQ]

Q. Embedding Error Handling이 뭐야?

A.
Embedding API 호출, Vector 생성, 저장 중 발생하는 오류를 분류하고 처리하는 방식이다.

Q. Dimension Mismatch는 뭐야?

A.
Embedding Vector 차원이 Vector DB Index가 기대하는 차원과 다른 오류다.

Q. Embedding 실패 Chunk는 어떻게 해?

A.
Chunk ID와 오류 원인을 기록하고 재처리 Queue에 넣어야 한다.

Q. Token Limit 오류는 Retry하면 돼?

A.
아니다. Chunk를 더 작게 나눈 뒤 다시 Embedding해야 한다.

---

## 7.2 Retrieval Error Handling

### [개념]

Retrieval Error Handling은 RAG 검색 과정에서 발생하는 오류와 결과 없음 상태를 처리하는 방식이다.

Retrieval 실패와 검색 결과 없음은 다르게 처리해야 한다.

Retrieval 상태:

- success
- empty
- failed
- timeout
- permission_denied
- index_not_ready
- stale_index
- low_confidence

---

### [핵심]

- 검색 결과 없음은 Tool 실패가 아니다.
- Vector DB 오류는 Retrieval Failed이다.
- 권한 없는 문서는 검색 결과에서 제외해야 한다.
- Index가 최신이 아니면 stale 상태를 표시할 수 있다.
- 검색 점수가 낮으면 low confidence로 처리한다.
- 결과가 부족하면 Query Rewrite 또는 추가 검색을 수행할 수 있다.
- 그래도 부족하면 Missing Information으로 답한다.

---

### [실무]

Retrieval Handling Flow:

```text
Run Retrieval
→ Check Vector DB Status
→ Apply Permission Filter
→ Search
→ Check Empty Result
→ Check Score Threshold
→ Rerank
→ Return Context or Missing
```

Retrieval Response 예:

```json
{
  "status": "empty",
  "query": "unknown provider-specific field",
  "results": [],
  "message": "No matching chunks found."
}
```

상태별 처리:

| 상태              | 처리                                   |
| ----------------- | -------------------------------------- |
| success           | Context Assembly                       |
| empty             | Missing Information 또는 Query Rewrite |
| failed            | Error Response                         |
| timeout           | 제한적 Retry                           |
| permission_denied | 권한 오류                              |
| index_not_ready   | Index 상태 확인                        |
| stale_index       | Reindex 권장                           |
| low_confidence    | 추가 검색 또는 제한적 답변             |

주의:

- Empty Result에서 일반 지식으로 추측하지 않는다.
- Low Score 결과를 근거처럼 사용하지 않는다.
- 권한 없는 문서를 Retrieved Context에 넣지 않는다.
- Index 최신성 문제가 있으면 답변 신뢰도가 낮아진다.
- Retrieval 오류와 LLM 생성 오류를 구분한다.

---

### [FAQ]

Q. Retrieval Error Handling이 뭐야?

A.
RAG 검색 중 발생하는 오류와 결과 없음 상태를 분류하고 처리하는 방식이다.

Q. 검색 결과 없음은 실패야?

A.
아니다. Tool은 정상 실행됐지만 관련 문서가 없는 empty 상태다.

Q. 검색 결과가 없으면 어떻게 답해?

A.
추가 검색을 하거나 문서에서 확인되지 않는다고 답해야 한다.

Q. Low Confidence 결과는 어떻게 처리해?

A.
추가 검색, Query Rewrite, 제한적 답변, Missing Information 중 하나로 처리한다.

---

# 8. Embedding and RAG Common Mistakes

## 8.1 Common Mistakes

### [개념]

Embedding and RAG Common Mistakes는 Embedding API, Vector Search, RAG Retrieval, Prompt Integration 과정에서 자주 발생하는 설계 오류이다.

---

### [핵심]

자주 발생하는 실수:

- Chat Model과 Embedding Model 역할 혼동
- Query와 Document를 다른 Embedding Model로 Vector화
- Vector Dimension 불일치
- 긴 문서를 통째로 Embedding
- Chunk Metadata 누락
- 문서 수정 후 Embedding 미갱신
- Embedding Model 변경 후 기존 Vector와 혼합
- Top-K를 무작정 높임
- Similarity Score만 믿고 Context 선택
- Retrieved Context와 User Question을 혼합
- RAG 답변에 Missing Information Rule 없음
- 검색 결과 없음에서 일반 지식으로 추측
- RAG Answer Validation 누락
- Hybrid Search 없이 정확한 필드명 검색을 Vector Search에만 의존
- Metadata Filtering이 너무 강하거나 너무 약함
- Retrieval Queries 누락
- 실패 Chunk를 조용히 무시
- Vector DB Index 상태를 확인하지 않음

---

### [실무]

문제 진단 Flow:

```text
RAG Answer Quality Problem
→ Check Query
→ Check Query Rewrite
→ Check Embedding Model
→ Check Chunk Quality
→ Check Vector Search
→ Check Top-K
→ Check Reranking
→ Check Retrieved Context
→ Check Grounded Prompt
→ Check Answer Validation
```

해결 기준:

| 문제             | 해결                                 |
| ---------------- | ------------------------------------ |
| 검색 결과 부정확 | Chunk 개선, Query Rewrite, Reranking |
| 관련 문서 누락   | Metadata Filter 완화, Hybrid Search  |
| 오답 생성        | Grounded Prompt, Missing Rule        |
| 비용 증가        | Top-K 제한, Context Filtering        |
| 오래된 답변      | Re-embedding, Versioning             |
| Dimension 오류   | Model/Index 설정 확인                |
| 코드 검색 약함   | Keyword Search 추가                  |
| 문서 근거 없음   | Missing Information 처리             |

검수 Checklist:

```text
Embedding Model과 Chat Model 역할이 분리되었는가?
Query와 Document가 같은 Embedding Model을 사용하는가?
Vector Dimension이 Index와 일치하는가?
Chunk가 독립 검색 가능한가?
Chunk Metadata가 충분한가?
문서 변경 시 재Embedding 기준이 있는가?
Top-K가 과도하지 않은가?
Reranking 또는 Filtering이 있는가?
Retrieved Context와 User Question이 분리되는가?
Grounded Prompt가 있는가?
Missing Information Rule이 있는가?
RAG Answer Validation이 있는가?
Retrieval Queries가 문서 마지막에 있는가?
Embedding 오류와 Retrieval 오류를 구분하는가?
```

---

### [FAQ]

Q. Embedding과 RAG에서 가장 흔한 실수는?

A.
Chat Model과 Embedding Model 역할을 혼동하고, Chunk 품질과 Metadata를 제대로 관리하지 않는 것이다.

Q. Query와 Document를 다른 Embedding Model로 처리하면?

A.
Vector 공간이 달라져 Similarity Search 품질이 크게 떨어질 수 있다.

Q. 문서 수정 후 Embedding을 다시 안 하면?

A.
검색 결과가 오래된 문서를 기준으로 나오거나 수정된 내용이 검색되지 않을 수 있다.

Q. RAG 답변에서 가장 위험한 실수는?

A.
검색 결과가 없는데도 일반 지식으로 추측해 답변하는 것이다.

Q. RAG 품질을 높이는 핵심은?

A.
좋은 Chunk, 정확한 Metadata, 적절한 Top-K, Reranking, Grounded Prompt, Answer Validation이다.

---

# Retrieval Queries

### [FAQ]

Q. Embedding이 뭐야?
A. Embedding은 텍스트를 의미 기반 숫자 Vector로 변환하는 기술이다.

Q. Embedding API는 뭐에 써?
A. 문서나 Query를 Vector로 변환해 Semantic Search와 RAG Retrieval에 사용한다.

Q. Embedding Model과 Chat Model 차이는?
A. Embedding Model은 검색용 Vector를 만들고 Chat Model은 답변을 생성한다.

Q. Embedding은 답변을 생성해?
A. 아니다. Embedding은 답변 생성이 아니라 의미 검색과 유사도 비교에 사용된다.

Q. Embedding API Request에는 뭐가 들어가?
A. Embedding Model 이름과 Vector로 변환할 Input Text가 들어간다.

Q. 긴 문서를 한 번에 Embedding해도 돼?
A. 권장하지 않는다. Chunking 후 각 Chunk를 Embedding하는 것이 좋다.

Q. Batch Embedding이 뭐야?
A. 여러 텍스트를 한 번의 요청으로 Embedding하는 방식이다.

Q. Embedding API Response는 뭐야?
A. 입력 텍스트를 Vector로 변환한 숫자 배열과 Metadata를 반환하는 응답이다.

Q. Vector가 뭐야?
A. Embedding Model이 텍스트 의미를 숫자 배열로 표현한 데이터다.

Q. Vector Dimension은 왜 중요해?
A. Vector Dimension이 Vector DB Index와 일치해야 저장과 검색이 정상 동작하기 때문이다.

Q. Query와 Document는 같은 Embedding Model을 써야 해?
A. 그렇다. 같은 Vector 공간에서 비교해야 Similarity Search가 의미를 가진다.

Q. Similarity Search가 뭐야?
A. Query Vector와 Document Vector의 유사도를 계산해 관련 문서를 찾는 검색 방식이다.

Q. Similarity Metric이 뭐야?
A. Vector 간 의미적 가까움을 계산하는 기준이다.

Q. Cosine Similarity는 뭐야?
A. Vector의 방향이 얼마나 비슷한지 계산하는 유사도 방식이다.

Q. Document Chunking이 뭐야?
A. 긴 문서를 검색 가능한 작은 단위로 나누는 과정이다.

Q. 좋은 Chunk 기준은?
A. 하나의 개념을 명확한 제목, 핵심 설명, 실무 기준, FAQ로 독립 검색 가능하게 구성하는 것이다.

Q. Chunk Embedding이 뭐야?
A. 문서 Chunk를 Embedding Model로 Vector화하는 과정이다.

Q. Chunk Metadata에는 무엇을 넣어?
A. 문서명, 섹션, 도메인, Part, 버전, Chunk ID, Embedding Model 정보를 넣는다.

Q. 문서가 수정되면 Embedding도 다시 해야 해?
A. 수정된 Chunk는 Embedding을 재생성해야 검색 결과가 최신 문서를 반영한다.

Q. Embedding Versioning이 뭐야?
A. Embedding Model, 문서 버전, Chunking Rule, Vector Index 설정 변경 이력을 관리하는 것이다.

Q. Embedding Model이 바뀌면 다시 Embedding해야 해?
A. 일반적으로 필요하다. Vector 공간이 달라져 기존 Vector와 섞으면 검색 품질이 떨어질 수 있다.

Q. Query Embedding이 뭐야?
A. 사용자 질문을 Embedding Model로 Vector화해 문서 Vector와 비교할 수 있게 만드는 과정이다.

Q. Query Rewrite는 왜 필요해?
A. 사용자 질문이 짧거나 모호하거나 대화체일 때 검색 품질을 높이기 위해 필요하다.

Q. Top-K Retrieval이 뭐야?
A. 검색 결과 중 유사도 점수가 높은 상위 K개의 Chunk를 선택하는 과정이다.

Q. Top-K는 높을수록 좋아?
A. 아니다. 관련 없는 Chunk가 늘어나면 비용과 Hallucination이 증가할 수 있다.

Q. Reranking이 뭐야?
A. 1차 검색 결과를 Query 의도에 맞게 다시 정렬하는 과정이다.

Q. Retrieved Context Assembly가 뭐야?
A. 검색된 Chunk를 LLM Prompt에 넣기 적합한 형태로 구성하는 과정이다.

Q. Grounded Prompt가 뭐야?
A. LLM이 검색된 문서 Context에 근거해서만 답변하도록 제한하는 Prompt 구조다.

Q. RAG Answer Validation이 뭐야?
A. LLM 답변이 Retrieved Context와 일치하는지 확인하는 검증 과정이다.

Q. Hybrid Search가 뭐야?
A. Vector Search와 Keyword Search를 함께 사용해 문서를 검색하는 방식이다.

Q. Vector Search만으로 부족한 경우는?
A. API 필드명, 에러 코드, 설정값, 클래스명, 메서드명처럼 정확한 문자열이 중요한 경우다.

Q. Metadata Filtering이 뭐야?
A. 문서명, 도메인, 섹션, 버전 같은 Metadata 기준으로 검색 범위를 제한하는 방식이다.

Q. Retrieval Queries가 뭐야?
A. RAG 검색 적중률을 높이기 위해 문서 마지막에 실제 질문 형태로 작성하는 Q/A 블록이다.

Q. Embedding Error Handling이 뭐야?
A. Embedding API 호출, Vector 생성, 저장 중 발생하는 오류를 분류하고 처리하는 방식이다.

Q. Dimension Mismatch는 뭐야?
A. Embedding Vector 차원이 Vector DB Index가 기대하는 차원과 다른 오류다.

Q. Retrieval Error Handling이 뭐야?
A. RAG 검색 중 발생하는 오류와 결과 없음 상태를 분류하고 처리하는 방식이다.

Q. 검색 결과 없음은 실패야?
A. 아니다. Tool은 정상 실행됐지만 관련 문서가 없는 empty 상태다.

Q. 검색 결과가 없으면 어떻게 답해?
A. 추가 검색을 하거나 문서에서 확인되지 않는다고 답해야 한다.

Q. RAG 답변에서 가장 위험한 실수는?
A. 검색 결과가 없는데도 일반 지식으로 추측해 답변하는 것이다.

Q. RAG 품질을 높이는 핵심은?
A. 좋은 Chunk, 정확한 Metadata, 적절한 Top-K, Reranking, Grounded Prompt, Answer Validation이다.
