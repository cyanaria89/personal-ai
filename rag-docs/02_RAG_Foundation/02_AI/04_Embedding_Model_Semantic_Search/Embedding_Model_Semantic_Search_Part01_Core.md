# Embedding Model & Semantic Search Part01 Core

---

# 1. Embedding Core

## 1.1 Embedding

### [개념]

Embedding은 Text를 의미 기반 숫자 Vector로 변환하는 과정이다.

Embedding Model은 문장을 읽고 답변을 생성하는 Chat Model이 아니다.
Embedding Model은 Query와 Document를 같은 Vector Space에 배치하여 Similarity Search가 가능하도록 만든다.

기본 구조:

```text
Text
→ Embedding Model
→ Vector
→ Similarity Search
→ Retrieved Documents
```

Embedding의 목적:

- 의미가 비슷한 Text를 가까운 Vector로 표현
- 사용자 Query와 문서 Chunk의 의미적 유사도 계산
- RAG에서 관련 문서 검색
- Semantic Search 기반 Retrieval 수행

---

### [핵심]

- Embedding은 Text를 Vector로 변환한다.
- Embedding Model은 검색용 모델이다.
- Chat Model은 답변 생성용 모델이다.
- Query와 Document는 같은 Embedding Model로 Vector화해야 한다.
- 의미가 비슷한 Text는 Vector Space에서 가깝게 표현된다.
- RAG 검색 품질은 Embedding 품질과 Chunk 품질에 크게 의존한다.
- Embedding만 좋다고 Retrieval이 항상 좋아지는 것은 아니다.
- Chunk 구조가 나쁘면 좋은 Embedding Model을 사용해도 검색 품질이 낮다.

---

### [실무]

2026 실무 기준에서 Embedding은 RAG 시스템의 Retrieval 품질을 결정하는 핵심 단계다.

RAG Pipeline에서 Embedding의 위치:

```text
User Query
→ Query Embedding
→ Vector Search
→ Retrieved Chunks
→ Prompt Context
→ LLM Answer
```

실무 기준:

- 한국어 문서가 많으면 Multilingual Embedding Model 사용
- 개발 문서는 한국어 설명 + 영어 기술 용어 병기
- 문서는 Chunk 단위로 Embedding
- Chunk마다 fileName, domain, level, section Metadata 연결
- 문서 수정 후 Embedding 재생성
- Embedding Model 변경 시 전체 Vector 재생성
- Query와 Document Embedding Model 통일
- Retrieval 실패 시 LLM보다 Chunk / Query / Metadata 먼저 점검

좋은 Embedding 대상 Text:

```text
# Chunking

Chunking은 긴 문서를 검색 가능한 단위로 나누는 과정이다.
Chunk는 하나의 개념을 중심으로 구성해야 한다.
Code Block과 설명은 가능하면 같은 Chunk에 유지한다.
```

나쁜 Embedding 대상 Text:

```text
이 기술은 여러 상황에서 유용하며 다양한 방식으로 사용할 수 있다.
```

문제:

- 제목 없음
- 핵심 용어 없음
- 검색 의도 불명확
- Retrieval Query Matching 약함

---

### [주의]

- Embedding Model을 Chat Model처럼 사용하지 않는다.
- Chat Model 출력 결과를 Vector처럼 직접 비교하지 않는다.
- 서로 다른 Embedding Model의 Vector를 같은 Index에서 비교하지 않는다.
- Vector Dimension이 다르면 같은 Vector DB Index에 섞지 않는다.
- 문서 전체를 하나의 Vector로 만들면 세부 검색 품질이 낮아진다.
- Similarity Score를 정답 점수처럼 해석하지 않는다.
- Vector만 저장하고 원문 Text와 Metadata를 잃어버리면 답변 근거 제시가 어렵다.

---

### [FAQ]

Q. Embedding이 뭐야?

A.
Text를 의미 기반 숫자 Vector로 변환하는 과정이다. 의미가 비슷한 Text는 Vector Space에서 가깝게 표현된다.

Q. Embedding Model은 뭐에 써?

A.
사용자 질문과 문서 Chunk를 Vector로 변환해 Semantic Search와 RAG 검색에 사용한다.

Q. Embedding Model이 답변도 생성해?

A.
아니다. Embedding Model은 검색용 Vector를 만들고, 답변 생성은 Chat Model이 수행한다.

Q. Embedding이 좋으면 RAG 품질도 무조건 좋아져?

A.
아니다. Chunk 구조, Metadata, Query 표현, Top-K, Reranking도 함께 중요하다.

---

# 2. Embedding Model

## 2.1 Chat Model vs Embedding Model

### [개념]

Chat Model은 Text를 생성하는 모델이다.
Embedding Model은 Text를 Vector로 변환하는 모델이다.

두 모델은 역할이 다르다.

| 구분      | Chat Model            | Embedding Model             |
| --------- | --------------------- | --------------------------- |
| 목적      | 답변 생성             | 검색용 Vector 생성          |
| 입력      | Prompt, Context       | Query, Document Chunk       |
| 출력      | Natural Language Text | Numeric Vector              |
| 사용 위치 | Generation 단계       | Retrieval 단계              |
| 예시      | Qwen, GPT, Claude     | BGE-M3, text-embedding 계열 |

---

### [핵심]

- Chat Model은 답변을 생성한다.
- Embedding Model은 검색용 Vector를 생성한다.
- RAG는 Retrieval과 Generation을 분리해서 설계한다.
- Embedding Model은 문서를 이해해서 답변하는 모델이 아니다.
- Embedding Model은 Query와 Chunk 간 유사도 계산을 가능하게 한다.
- Chat Model이 좋아도 Retrieval이 실패하면 답변 품질이 낮다.
- Embedding Model이 좋아도 Chunk 품질이 낮으면 Retrieval이 실패할 수 있다.

---

### [실무]

RAG 실무 구성:

```text
Embedding Model
- Query Embedding 생성
- Document Chunk Embedding 생성
- Vector Search 지원

Chat Model
- Retrieved Context 기반 답변 생성
- 문서 근거 기반 설명
- 부족한 정보 판단
```

로컬 AI 서버 예시:

```text
Chat Model:
- Qwen2.5 14B
- Qwen2.5-Coder 14B

Embedding Model:
- BGE-M3
```

역할 분리 기준:

```text
질문을 이해하고 답변 작성
→ Chat Model

질문과 문서의 의미 유사도 계산
→ Embedding Model
```

실무 설계 원칙:

- Chat Model과 Embedding Model을 혼동하지 않는다.
- Embedding Model은 Retrieval 최적화 기준으로 선택한다.
- Chat Model은 답변 품질과 지시 준수 능력 기준으로 선택한다.
- RAG 오류 분석 시 Retrieval 실패와 Generation 실패를 구분한다.

---

### [Comparison]

| 비교 항목   | Chat Model                   | Embedding Model               |
| ----------- | ---------------------------- | ----------------------------- |
| 질문 답변   | 가능                         | 불가능                        |
| 문서 검색   | 직접 수행 X                  | Vector Search 지원            |
| Vector 생성 | 일반적으로 목적 아님         | 핵심 목적                     |
| RAG 위치    | Generation                   | Retrieval                     |
| 오류 원인   | Hallucination, Context 무시  | 검색 누락, 유사도 오류        |
| 튜닝 포인트 | Prompt, Context, System Rule | Chunk, Metadata, Query, Model |

---

### [FAQ]

Q. Chat Model과 Embedding Model 차이는?

A.
Chat Model은 답변을 생성하고, Embedding Model은 검색을 위한 Vector를 생성한다.

Q. Qwen 같은 Chat Model로 Embedding을 만들면 안 돼?

A.
일반적으로 권장하지 않는다. 검색 품질을 위해 Embedding 전용 모델을 사용해야 한다.

Q. RAG에서 더 중요한 건 Chat Model이야 Embedding Model이야?

A.
둘 다 중요하다. Retrieval이 실패하면 Chat Model이 좋아도 근거 있는 답변을 만들기 어렵다.

Q. 검색은 잘 됐는데 답변이 틀리면 Embedding 문제야?

A.
항상 그렇지는 않다. Retrieved Context가 충분한데 답변이 틀리면 Prompt Grounding 또는 Chat Model 문제일 수 있다.

---

# 3. Text Embedding

## 3.1 Query Embedding

### [개념]

Query Embedding은 사용자 질문을 Embedding Model로 Vector화하는 과정이다.

사용자 질문:

```text
Chunk Size는 어떻게 정해야 해?
```

Query Embedding:

```text
"Chunk Size는 어떻게 정해야 해?"
→ Embedding Model
→ Query Vector
```

Query Vector는 Document Chunk Vector와 비교되어 유사한 Chunk를 찾는 데 사용된다.

기본 Flow:

```text
User Query
→ Query Normalization
→ Query Embedding
→ Vector Search
→ Retrieved Chunks
```

---

### [핵심]

- Query Embedding은 사용자 질문을 Vector로 변환한다.
- Query가 짧거나 모호하면 검색 품질이 낮아질 수 있다.
- Query에 핵심 Domain Keyword가 포함되면 Retrieval 품질이 좋아질 수 있다.
- 한국어 질문에는 영어 기술 용어를 함께 확장할 수 있다.
- Query Rewrite는 검색 의도를 명확히 하는 데 사용한다.
- Query Expansion은 관련 키워드를 추가해 검색 범위를 넓힌다.
- Query를 과도하게 바꾸면 원래 의도가 손상될 수 있다.

---

### [실무]

좋은 Query:

```text
RAG Chunk Size와 Chunk Overlap은 어떻게 정해야 해?
```

나쁜 Query:

```text
크기 어떻게 해?
```

나쁜 이유:

- 대상 Domain 불명확
- Chunk Size인지 File Size인지 알 수 없음
- Embedding 검색 의도 약함
- 관련 Chunk가 분산될 가능성 높음

Query Rewrite 예시:

```text
Original Query:
크기 어떻게 해?

Rewritten Query:
RAG 문서의 Chunk Size와 Chunk Overlap 기준은 어떻게 정해야 하는가?
```

Query Expansion 예시:

```text
Original Query:
검색이 안 돼

Expanded Query:
RAG Retrieval 검색 결과가 안 나올 때 원인, Query Embedding, Chunking, Metadata, Similarity Threshold 문제를 어떻게 점검해야 하는가?
```

한국어 + 영어 병기 예시:

```text
트랜잭션 경계
Transaction Boundary
@Transactional
```

실무 적용 기준:

- 사용자 질문이 짧으면 Domain Keyword 보강
- 기술 용어는 영어 원문 병기
- 에러명 / 클래스명 / 메서드명은 원문 유지
- Query Rewrite는 의미 보존 우선
- Query Expansion은 검색 누락 방지 목적
- Multi-Agent 환경에서는 PM Agent가 Query를 정규화할 수 있음

---

### [주의]

- Query를 너무 넓히면 관련 없는 Chunk가 검색될 수 있다.
- Query를 너무 좁히면 필요한 Chunk가 누락될 수 있다.
- 사용자의 원래 의도를 제거하면 안 된다.
- Query Embedding과 Document Embedding은 같은 Model로 생성해야 한다.
- 검색 실패를 무조건 Top-K 증가로 해결하지 않는다.
- 먼저 Query 표현과 문서 표현의 불일치를 점검한다.

---

### [FAQ]

Q. Query Embedding은 뭐야?

A.
사용자 질문을 Embedding Model로 Vector로 변환하는 과정이다.

Q. Query가 짧으면 왜 검색 품질이 낮아져?

A.
검색 의도와 Domain Keyword가 부족해서 관련 Chunk와의 의미 유사도가 약해질 수 있다.

Q. Query Rewrite는 언제 써?

A.
사용자 질문이 짧거나 모호해서 검색 의도를 명확히 해야 할 때 사용한다.

Q. Query Expansion은 뭐야?

A.
원래 질문에 관련 키워드와 Domain Term을 추가해 검색 누락을 줄이는 방식이다.

---

## 3.2 Document Embedding

### [개념]

Document Embedding은 문서 Chunk를 Embedding Model로 Vector화하는 과정이다.

긴 문서는 전체를 한 번에 Embedding하지 않는다.
RAG 문서는 Header와 Section 기준으로 Chunk를 나누고, 각 Chunk를 Embedding한다.

기본 Flow:

```text
Markdown Document
→ Split into Chunks
→ Add Metadata
→ Generate Chunk Embedding
→ Store Vector
```

Document Embedding 대상:

- 문서 제목
- Section 제목
- [개념]
- [핵심]
- [실무]
- [FAQ]
- Code Block
- Retrieval Queries
- Metadata

---

### [핵심]

- Document는 Chunk 단위로 Embedding한다.
- Chunk는 독립 검색되어도 의미가 유지되어야 한다.
- Chunk 제목은 검색 품질에 큰 영향을 준다.
- Code Block과 설명은 가능하면 같은 Chunk에 유지한다.
- FAQ는 실제 사용자 질문과 매칭되기 쉽다.
- Retrieval Queries는 Query Matching을 강화한다.
- Metadata는 검색 결과의 출처와 문맥을 보존한다.
- 문서 수정 후 Embedding 재생성이 필요하다.

---

### [실무]

좋은 Document Chunk:

```md
# Chunk Size

### [개념]

Chunk Size는 하나의 검색 단위가 포함하는 Token 양이다.

### [핵심]

- 너무 작으면 문맥이 부족하다.
- 너무 크면 여러 개념이 섞인다.
- Medium Chunk는 일반 RAG 문서에 적합하다.
```

좋은 이유:

- 제목 명확
- 핵심 용어 포함
- 하나의 개념만 설명
- Chunk 단독 검색 가능
- Query Matching 가능

나쁜 Document Chunk:

```md
# 기타

RAG는 여러 가지가 있고 검색도 중요하고 모델도 중요하다.
경우에 따라 다르게 하면 된다.
```

나쁜 이유:

- 제목 불명확
- 개념 혼합
- 핵심 키워드 부족
- Retrieval Query Matching 약함
- Agent가 근거로 사용하기 어려움

Metadata 예시:

```json
{
  "source": "RAG Doc",
  "fileName": "Embedding_Model_Semantic_Search_Part01_Core.md",
  "domain": "AI",
  "level": "Foundation",
  "part": "Part01",
  "section": "Document Embedding",
  "title": "Document Embedding",
  "tags": ["embedding", "document-embedding", "rag", "semantic-search"],
  "version": "2026.06"
}
```

실무 기준:

- Markdown Header를 Chunk 경계로 활용
- Section 단위로 Semantic Boundary 확인
- Code Block 중간 분리 금지
- FAQ는 사용자 질문 형태로 작성
- Retrieval Queries는 문서 마지막에 별도 구성
- Chunk별 Metadata 연결
- 문서 수정 후 재색인
- Embedding Model 변경 후 재색인

---

### [주의]

- 문서 전체를 하나의 Vector로 만들지 않는다.
- Chunk가 너무 작으면 문맥이 부족하다.
- Chunk가 너무 크면 주제가 섞인다.
- 제목 없는 Chunk는 검색 품질이 낮다.
- Metadata 없는 Vector는 출처 추적이 어렵다.
- Code Block과 설명이 분리되면 코드 생성 품질이 낮아질 수 있다.
- 같은 문장을 여러 문서에 과도하게 반복하면 중복 검색이 늘어난다.

---

### [FAQ]

Q. Document Embedding은 뭐야?

A.
문서 Chunk를 Embedding Model로 Vector로 변환해 검색 가능하게 저장하는 과정이다.

Q. 문서 전체를 한 번에 Embedding하면 안 돼?

A.
세부 개념 검색 품질이 낮아진다. RAG 문서는 Chunk 단위로 Embedding하는 것이 좋다.

Q. Chunk 제목이 왜 중요해?

A.
제목은 Chunk의 의미를 명확히 하고 Query Matching과 Retrieval 품질을 높인다.

Q. 문서 수정 후에는 뭘 해야 해?

A.
수정된 문서의 Embedding을 다시 생성하고 Vector Index를 갱신해야 한다.

---

# 4. Vector

## 4.1 Vector

### [개념]

Vector는 Embedding 결과를 표현하는 숫자 배열이다.

예시:

```text
"Semantic Search"
→ [0.12, -0.03, 0.87, 0.44, ...]
```

Vector는 사람이 직접 해석하기 어렵다.
하지만 Vector 간 거리나 방향을 계산하면 Text 간 의미적 유사도를 비교할 수 있다.

---

### [핵심]

- Vector는 Text의 의미를 숫자로 표현한 배열이다.
- Vector Dimension은 Vector 길이다.
- 같은 Embedding Model의 Vector끼리 비교해야 한다.
- Vector는 Similarity Search에 사용된다.
- Vector는 원본 Text와 Metadata에 연결되어야 한다.
- Vector 자체를 사람이 직접 수정하지 않는다.
- Vector Dimension 불일치 시 같은 Index에서 비교할 수 없다.

---

### [실무]

Vector 저장 구조:

```text
Chunk Text
+ Metadata
+ Embedding Vector
→ Vector Store
```

예시:

```json
{
  "id": "embedding-part01-core-001",
  "text": "Embedding은 Text를 의미 기반 숫자 Vector로 변환하는 과정이다.",
  "metadata": {
    "fileName": "Embedding_Model_Semantic_Search_Part01_Core.md",
    "section": "Embedding Core",
    "domain": "AI"
  },
  "vector": [0.12, -0.03, 0.87]
}
```

실무 기준:

- Vector만 저장하지 않는다.
- 원문 Text를 함께 저장하거나 참조 가능해야 한다.
- Metadata를 함께 저장한다.
- Embedding Model 이름과 Version을 기록한다.
- Vector Dimension을 Index 생성 시 고정한다.
- Embedding Model 변경 시 기존 Vector와 섞지 않는다.
- Vector DB Migration 시 Model / Dimension 호환성 확인

---

### [주의]

- 서로 다른 Embedding Model로 생성한 Vector를 같은 Index에 섞으면 안 된다.
- Dimension이 다른 Vector는 같은 Index에 저장할 수 없다.
- Vector만 있고 원문 Text가 없으면 답변 근거를 만들기 어렵다.
- Vector Score는 절대 정답 점수가 아니다.
- Vector 유사도는 검색 후보 선별 기준이다.
- RAG 답변 전 Retrieved Context 검증이 필요하다.

---

### [FAQ]

Q. Vector는 뭐야?

A.
Embedding Model이 Text를 변환한 숫자 배열이다. Similarity Search에서 의미 유사도를 계산하는 데 사용된다.

Q. Vector Dimension은 뭐야?

A.
Vector의 길이다. Embedding Model마다 Dimension이 다를 수 있다.

Q. 서로 다른 Embedding Model의 Vector를 비교해도 돼?

A.
안 된다. 같은 Embedding Model과 같은 Vector Space에서 생성된 Vector끼리 비교해야 한다.

Q. Vector만 저장하면 안 돼?

A.
안 된다. 원문 Text와 Metadata가 있어야 답변 근거와 출처를 제시할 수 있다.

---

## 4.2 Vector Dimension

### [개념]

Vector Dimension은 Embedding Vector의 길이다.

예시:

```text
Dimension 3:
[0.12, -0.03, 0.87]

Dimension 1024:
[0.12, -0.03, 0.87, ... 1024 values]
```

Embedding Model마다 출력 Vector Dimension이 다를 수 있다.

---

### [핵심]

- Vector Dimension은 Embedding Model 출력 크기다.
- Vector DB Index는 특정 Dimension 기준으로 생성된다.
- Dimension이 다르면 같은 Index에 저장할 수 없다.
- Embedding Model 변경 시 Dimension 변경 가능성이 있다.
- Dimension이 크다고 항상 검색 품질이 좋은 것은 아니다.
- 검색 품질은 Model 성능, Chunk 품질, Query 품질, Metadata에 함께 의존한다.

---

### [실무]

Embedding Model 변경 시 점검 Flow:

```text
Current Embedding Model 확인
→ Current Vector Dimension 확인
→ New Embedding Model Dimension 확인
→ 기존 Index 호환 여부 확인
→ 필요 시 Vector 재생성
→ Vector DB 재색인
```

실무 체크 항목:

```md
### [Checklist]

- [ ] 기존 Embedding Model 이름 확인
- [ ] 기존 Vector Dimension 확인
- [ ] 새 Embedding Model Dimension 확인
- [ ] 같은 Index 재사용 가능 여부 확인
- [ ] 기존 Vector 삭제 또는 별도 Index 분리
- [ ] 전체 문서 재Embedding
- [ ] Golden Query로 Retrieval 품질 검증
```

---

### [주의]

- Dimension 불일치를 무시하면 Vector DB 오류가 발생할 수 있다.
- Dimension이 같아도 Model이 다르면 같은 의미 공간이라고 볼 수 없다.
- Model만 바꾸고 기존 Vector를 재사용하면 검색 품질이 망가질 수 있다.
- Index를 재생성하면 기존 검색 결과 순위가 달라질 수 있다.
- 재색인 후 Golden Query로 품질을 확인해야 한다.

---

### [FAQ]

Q. Vector Dimension이 다르면 어떻게 돼?

A.
같은 Vector DB Index에 저장하거나 비교할 수 없다. Index를 새로 만들거나 Vector를 재생성해야 한다.

Q. Dimension이 크면 무조건 좋아?

A.
아니다. Dimension은 표현 크기일 뿐이고 검색 품질은 Model, Chunk, Query, Metadata에 함께 의존한다.

Q. Embedding Model을 바꾸면 기존 Vector를 써도 돼?

A.
일반적으로 안 된다. 새 Embedding Model로 문서를 다시 Embedding하고 재색인해야 한다.

---

# 5. Semantic Search

## 5.1 Semantic Search

### [개념]

Semantic Search는 단어가 정확히 일치하지 않아도 의미가 비슷한 문서를 찾는 검색 방식이다.

Keyword Search는 단어 일치를 기반으로 검색한다.
Semantic Search는 Query Vector와 Document Vector의 의미적 유사도를 기반으로 검색한다.

기본 Flow:

```text
User Query
→ Query Embedding
→ Compare with Document Vectors
→ Similarity Ranking
→ Retrieved Chunks
```

---

### [핵심]

- Semantic Search는 의미 기반 검색이다.
- Query와 Document를 Vector로 변환해 비교한다.
- 표현이 달라도 의미가 비슷하면 검색될 수 있다.
- 정확한 에러명, 클래스명, 메서드명 검색은 Keyword Search가 유리할 수 있다.
- 기술 문서 RAG는 Semantic Search와 Keyword Search를 함께 고려한다.
- Similarity Score는 검색 후보 정렬 기준이다.
- 높은 Score가 항상 정답 Chunk를 의미하지는 않는다.

---

### [실무]

Semantic Search에 적합한 질문:

```text
RAG 검색 품질을 높이려면 문서를 어떻게 나눠야 해?
```

찾을 수 있는 문서:

```text
Chunking은 RAG 검색 품질의 핵심이다.
Chunk는 하나의 주제를 중심으로 구성해야 한다.
```

단어가 완전히 같지 않아도 의미가 유사하므로 검색 가능하다.

Keyword Search에 적합한 질문:

```text
NullPointerException 원인
@Transactional 동작 조건
findByUserIdAndStatus 메서드
```

기술 문서 검색 기준:

```text
개념 질문
→ Semantic Search 우선

에러명 / 클래스명 / 메서드명
→ Keyword Search 우선

개념 + 정확한 용어 혼합
→ Hybrid Search 검토
```

---

### [Comparison]

| 검색 방식       | 기준          | 장점                    | 단점                    | 적합                       |
| --------------- | ------------- | ----------------------- | ----------------------- | -------------------------- |
| Keyword Search  | 단어 일치     | 정확한 용어 검색 강함   | 표현이 다르면 약함      | 에러명, 클래스명, 메서드명 |
| Semantic Search | 의미 유사도   | 표현이 달라도 검색 가능 | 정확한 키워드 누락 가능 | 개념 질문, 유사 의미 검색  |
| Hybrid Search   | 키워드 + 의미 | 두 방식 보완            | 구성 복잡도 증가        | 기술 문서 RAG              |

---

### [주의]

- Semantic Search만으로 모든 검색 문제가 해결되지 않는다.
- 기술 용어는 원문 Keyword를 문서에 포함해야 한다.
- 사용자 질문과 문서 표현이 너무 다르면 검색이 실패할 수 있다.
- Similarity Score가 높아도 질문 의도와 다를 수 있다.
- Similarity Score가 낮아도 필요한 문서일 수 있다.
- Retrieval 결과는 LLM 답변 전 검토되어야 한다.

---

### [FAQ]

Q. Semantic Search가 뭐야?

A.
단어가 정확히 일치하지 않아도 의미가 비슷한 문서를 찾는 검색 방식이다.

Q. Keyword Search와 Semantic Search 차이는?

A.
Keyword Search는 단어 일치 기반이고, Semantic Search는 의미 유사도 기반이다.

Q. 기술 문서에는 Semantic Search만 쓰면 돼?

A.
아니다. 에러명, 클래스명, 메서드명은 Keyword Search가 더 유리할 수 있어 Hybrid Search를 고려한다.

Q. Semantic Search가 틀린 문서를 가져올 수도 있어?

A.
그렇다. 의미적으로 비슷하지만 질문 의도와 다른 Chunk가 검색될 수 있다.

---

## 5.2 Semantic Similarity

### [개념]

Semantic Similarity는 Query Vector와 Document Vector가 의미적으로 얼마나 가까운지 계산하는 기준이다.

기본 Flow:

```text
Query Vector
+ Document Vector
→ Similarity Score
→ Rank Documents
```

대표 계산 방식:

- Cosine Similarity
- Dot Product
- Euclidean Distance

---

### [핵심]

- Semantic Similarity는 의미적 가까움을 수치화한다.
- Similarity Score는 검색 결과 Ranking에 사용된다.
- 높은 Score가 항상 정답을 의미하지 않는다.
- 낮은 Score라도 필요한 문서일 수 있다.
- Score 해석은 Model, Index, Normalization 방식에 따라 달라진다.
- Score는 절대 점수가 아니라 상대적 Ranking 기준으로 본다.

---

### [실무]

검색 결과 예시:

```text
Query:
Embedding Model과 Chat Model 차이는?

Retrieved Chunks:
1. Chat Model vs Embedding Model - score 0.87
2. Query Embedding - score 0.73
3. Vector Dimension - score 0.61
```

해석:

```text
1번 Chunk:
질문 의도와 직접 관련 높음

2번 Chunk:
Embedding 관련이지만 질문 핵심과 부분 관련

3번 Chunk:
Embedding 관련은 있으나 질문 의도와 거리 있음
```

실무 기준:

- Score만 보고 최종 Context를 결정하지 않는다.
- 제목, Section, Metadata를 함께 확인한다.
- Top-K 결과 중 중복 Chunk 제거
- 필요 시 Reranking 적용
- 낮은 Score가 반복되면 Query / Chunk / Metadata 개선
- 높은 Score인데 답변이 틀리면 Chunk 내용과 Prompt Grounding 점검

---

### [주의]

- Similarity Score를 정답 확률로 해석하지 않는다.
- Score 기준은 Embedding Model마다 달라질 수 있다.
- Score 분포를 확인하지 않고 Threshold를 고정하지 않는다.
- Score가 높아도 최신성, Domain, Section이 맞는지 확인한다.
- 검색 결과가 충돌하면 문서 우선순위 규칙이 필요하다.

---

### [FAQ]

Q. Semantic Similarity는 뭐야?

A.
Query와 Document의 의미적 가까움을 Vector 기준으로 계산한 값이다.

Q. Similarity Score가 높으면 무조건 좋은 문서야?

A.
아니다. 질문 의도와 맞는지 제목, Section, 내용, Metadata를 함께 확인해야 한다.

Q. Similarity Score는 정답 확률이야?

A.
아니다. 검색 후보의 의미 유사도 또는 Ranking 기준이다.

Q. Score가 낮으면 무조건 버려야 해?

A.
아니다. 필요한 문서일 수 있으므로 Threshold와 Context 상황을 함께 판단해야 한다.

---

# 6. RAG Integration

## 6.1 Embedding in RAG

### [개념]

RAG에서 Embedding은 Retrieval 단계에 사용된다.

RAG는 크게 Retrieval과 Generation으로 나뉜다.

```text
Retrieval:
User Query
→ Query Embedding
→ Vector Search
→ Retrieved Chunks

Generation:
Retrieved Chunks
→ Prompt Context
→ Chat Model
→ Grounded Answer
```

Embedding은 답변 생성 전 관련 문서를 찾는 단계다.

---

### [핵심]

- Embedding은 RAG의 Retrieval 단계에 사용된다.
- Query Embedding으로 사용자 질문을 Vector화한다.
- Document Embedding으로 문서 Chunk를 Vector화한다.
- Vector Search로 관련 Chunk를 찾는다.
- Retrieved Chunks가 Chat Model의 근거가 된다.
- Retrieval 실패는 Generation 품질 저하로 이어진다.
- RAG는 Retrieval과 Generation을 모두 관리해야 한다.

---

### [실무]

RAG 답변 생성 Flow:

```text
User Query
→ Query Rewrite
→ Query Embedding
→ Top-K Vector Search
→ Metadata Filter
→ Reranking
→ Context Assembly
→ Chat Model Answer
→ Grounding Check
```

Grounded Answer 기준:

- Retrieved Context 기반 답변
- 문서에 없는 내용은 추측하지 않음
- 정보 부족 시 Missing Information 명시
- 충돌하는 문서가 있으면 우선순위 기준 적용
- 필요한 경우 추가 Query 생성

RAG Prompt 규칙 예시:

```text
Retrieved Context에 없는 내용은 일반 지식으로 보완하지 않는다.
문서 근거가 부족하면 "문서에 없음" 또는 "추가 정보 필요"라고 답한다.
```

실무 오류 분리:

```text
검색 결과가 없음
→ Retrieval 문제

검색 결과는 있지만 관련 없음
→ Chunk / Query / Metadata 문제

검색 결과는 적절하지만 답변이 틀림
→ Prompt Grounding / Chat Model 문제

검색 결과가 서로 충돌
→ 문서 우선순위 / Version 문제
```

---

### [주의]

- RAG는 Vector DB만 붙이면 완성되는 구조가 아니다.
- 검색 결과가 부정확하면 LLM 답변도 부정확해진다.
- LLM이 검색 실패를 일반 지식으로 덮어쓰지 않도록 해야 한다.
- Retrieved Context가 너무 많으면 관련 없는 정보가 섞일 수 있다.
- Retrieved Context가 너무 적으면 답변 근거가 부족할 수 있다.
- Retrieval 결과와 답변 결과를 분리해서 평가해야 한다.

---

### [FAQ]

Q. RAG에서 Embedding은 어디에 쓰여?

A.
사용자 질문과 문서 Chunk를 Vector로 변환해 관련 문서를 검색하는 Retrieval 단계에 쓰인다.

Q. 검색 결과가 없으면 Chat Model이 알아서 답하면 안 돼?

A.
RAG 기준에서는 위험하다. 문서 근거가 없으면 정보 부족을 명시해야 한다.

Q. 검색은 됐는데 답변이 틀리면 어떻게 해?

A.
Retrieved Context 품질, Prompt Grounding, Chunk 부족, 충돌 문서 포함 여부를 점검한다.

Q. RAG 품질은 무엇에 의존해?

A.
Embedding Model, Chunk 구조, Metadata, Query 품질, Top-K, Reranking, Chat Model Grounding에 의존한다.

---

# 7. BGE-M3 Basic Usage

## 7.1 BGE-M3

### [개념]

BGE-M3는 Multilingual Embedding Model로 사용할 수 있는 Embedding Model이다.

BGE-M3는 한국어 / 영어 혼합 문서 검색에 활용 가능하다.
개발 문서 RAG에서는 한국어 설명과 영어 기술 용어가 함께 등장하므로 Multilingual Embedding 성능이 중요하다.

활용 대상:

- Korean Retrieval
- English Technical Term Retrieval
- Dense Retrieval
- Sparse Retrieval
- Multi-vector Retrieval
- RAG Document Search

---

### [핵심]

- BGE-M3는 Multilingual Embedding Model로 사용할 수 있다.
- 한국어 RAG 문서 검색에 활용 가능하다.
- 한국어 설명 + 영어 기술 용어 혼합 검색에 유리하다.
- Dense Retrieval 중심으로 사용할 수 있다.
- Hybrid Search / Reranking과 함께 품질 개선 가능하다.
- Local 환경에서는 모델 로딩 시간과 자원 사용량을 고려해야 한다.
- BGE-M3를 사용해도 Chunk 구조가 나쁘면 검색 품질은 낮아진다.

---

### [실무]

한국어 / 영어 혼합 문서 예시:

```md
# Query Embedding

Query Embedding은 사용자 질문을 Vector로 변환하는 과정이다.
User Query를 Embedding Model에 입력해 Query Vector를 생성한다.
```

검색 가능한 질문:

```text
Query Embedding이 뭐야?
사용자 질문을 벡터로 바꾸는 과정이 뭐야?
User Query Vector는 어디에 써?
```

BGE-M3 사용 기준:

```text
문서 언어:
한국어 + 영어 기술 용어 혼합

검색 목적:
RAG Retrieval

사용 방식:
Dense Retrieval 우선
필요 시 Hybrid Search / Reranking 확장

주의:
Chunk 품질과 Metadata 품질 동시 관리
```

실무 최적화:

- 핵심 용어 한글 + 영어 병기
- FAQ에 실제 한국어 질문 포함
- Section 제목에 영어 기술 용어 포함
- Retrieval Queries 강화
- Metadata에 domain / level / section 포함
- 검색 실패 Query를 문서 개선에 반영

---

### [주의]

- BGE-M3를 사용해도 Hallucination이 자동으로 해결되지는 않는다.
- Embedding Model은 답변 생성 모델이 아니다.
- Chunk가 너무 크면 검색 결과가 흐려질 수 있다.
- Chunk가 너무 작으면 문맥이 부족할 수 있다.
- 한국어 번역어만 쓰면 영어 기술 용어 검색이 약해질 수 있다.
- 영어 용어만 쓰면 한국어 Query Matching이 약해질 수 있다.
- Model 변경 시 기존 Vector 재생성이 필요할 수 있다.

---

### [FAQ]

Q. BGE-M3는 어디에 써?

A.
한국어/영어 혼합 문서 검색, Dense Retrieval, RAG 검색에 사용할 수 있는 Multilingual Embedding Model로 활용한다.

Q. BGE-M3를 쓰면 한국어 검색이 좋아져?

A.
한국어 검색에 유리할 수 있다. 다만 Chunk 구조, 용어 병기, Metadata가 함께 좋아야 한다.

Q. BGE-M3가 답변도 생성해?

A.
아니다. BGE-M3는 Embedding Model이며 검색용 Vector를 생성하는 역할이다.

Q. BGE-M3를 쓰면 Hallucination이 없어져?

A.
아니다. Retrieval 품질을 높일 수는 있지만 답변 생성과 Grounding 규칙은 별도로 관리해야 한다.

---

# 8. Common Mistakes

## 8.1 Embedding Common Mistakes

### [개념]

Embedding 기반 RAG에서 자주 발생하는 문제는 Model 문제가 아니라 문서 구조, Chunking, Metadata, Query 표현 문제인 경우가 많다.

---

### [핵심]

자주 발생하는 실수:

- Chat Model을 Embedding Model처럼 사용
- Embedding Model과 Chat Model 역할 혼동
- Embedding Model 변경 후 기존 Vector 재사용
- Vector Dimension 불일치
- 문서 전체를 하나의 Chunk로 Embedding
- 너무 큰 Chunk에 여러 개념 혼합
- 너무 작은 Chunk로 문맥 부족
- Code Block 중간에서 Chunk 분리
- Metadata 누락
- Top-K를 무조건 크게 설정
- Similarity Score를 절대 정답처럼 해석
- 한국어 / 영어 용어 병기 부족
- 문서 수정 후 Embedding 재생성 누락
- Retrieval 실패를 LLM 문제로만 판단

---

### [실무]

문제 분석 Flow:

```text
RAG 답변 실패
→ Retrieved Chunks 확인
→ 관련 문서 검색 여부 확인
→ Query 표현 확인
→ Chunk 제목 확인
→ Metadata 확인
→ Embedding 최신 여부 확인
→ Top-K / Threshold 확인
→ Reranking 필요 여부 확인
→ Prompt Grounding 확인
```

문제별 우선 점검:

| 문제                    | 우선 점검                               |
| ----------------------- | --------------------------------------- |
| 검색 결과 없음          | Query, Chunk 제목, Embedding 생성 여부  |
| 관련 없는 문서 검색     | Chunk 혼합, Top-K, Threshold            |
| 검색은 됐는데 답변 틀림 | Context 부족, Prompt Grounding          |
| 중복 문서 과다          | Chunk Overlap, 중복 설명                |
| 한국어 검색 약함        | 한글/영어 용어 병기, Multilingual Model |
| 코드 답변 부정확        | Code Block Preservation, 설명 연결      |

---

### [FAQ]

Q. RAG 검색이 안 되면 Embedding Model부터 바꿔야 해?

A.
아니다. 먼저 Query 표현, Chunk 구조, Metadata, Embedding 생성 여부를 점검해야 한다.

Q. Top-K를 크게 하면 검색 문제가 해결돼?

A.
항상 그렇지 않다. 관련 없는 Chunk가 더 많이 섞여 답변 품질이 낮아질 수 있다.

Q. 문서 수정 후 바로 검색 결과가 바뀌어?

A.
아니다. 수정된 문서를 다시 Embedding하고 Vector Index를 갱신해야 한다.

Q. Similarity Score가 높은데 답변이 틀리면 왜 그래?

A.
Score는 의미 유사도일 뿐이다. Chunk 내용 부족, 질문 의도 불일치, Prompt Grounding 문제가 있을 수 있다.

---

# 9. Checklist

## 9.1 Embedding Core Checklist

### [Checklist]

- [ ] Embedding과 Chat Model 역할을 구분했는가?
- [ ] Query와 Document를 같은 Embedding Model로 Vector화했는가?
- [ ] Vector Dimension이 Index와 일치하는가?
- [ ] 문서를 Chunk 단위로 Embedding했는가?
- [ ] Chunk가 하나의 개념만 다루는가?
- [ ] Chunk 제목이 명확한가?
- [ ] Code Block이 중간에 잘리지 않았는가?
- [ ] 핵심 용어를 한글 + 영어로 병기했는가?
- [ ] Metadata에 source / fileName / domain / level / section이 포함되었는가?
- [ ] FAQ가 실제 사용자 질문 형태인가?
- [ ] Retrieval Queries가 포함되었는가?
- [ ] 문서 수정 후 Embedding 재생성 규칙이 있는가?
- [ ] Embedding Model 변경 시 재색인 규칙이 있는가?
- [ ] Similarity Score를 절대 정답으로 해석하지 않도록 설명했는가?
- [ ] Retrieval 실패 원인을 LLM 문제와 분리했는가?

---

# Retrieval Queries

### [FAQ]

Q. Embedding이 뭐야?

A.
Text를 의미 기반 숫자 Vector로 변환하는 과정이다. 의미가 비슷한 Text는 Vector Space에서 가깝게 표현된다.

Q. Embedding Model은 뭐에 써?

A.
사용자 질문과 문서 Chunk를 Vector로 변환해 Semantic Search와 RAG 검색에 사용한다.

Q. Chat Model과 Embedding Model 차이는?

A.
Chat Model은 답변을 생성하고, Embedding Model은 검색을 위한 Vector를 생성한다.

Q. Embedding Model이 답변을 생성해?

A.
아니다. Embedding Model은 Retrieval 단계에서 검색용 Vector를 생성한다.

Q. RAG에서 Embedding은 어디에 쓰여?

A.
User Query와 Document Chunk를 Vector화해 관련 문서를 찾는 Retrieval 단계에 쓰인다.

Q. Query Embedding은 뭐야?

A.
사용자 질문을 Embedding Model로 Vector로 변환하는 과정이다.

Q. Document Embedding은 뭐야?

A.
문서 Chunk를 Embedding Model로 Vector로 변환해 검색 가능하게 저장하는 과정이다.

Q. Chunk Embedding은 뭐야?

A.
긴 문서를 Chunk 단위로 나눈 뒤 각 Chunk를 Vector로 변환하는 것이다.

Q. Vector는 뭐야?

A.
Embedding Model이 Text를 변환한 숫자 배열이다. Similarity Search에서 의미 유사도를 계산하는 데 사용된다.

Q. Vector Dimension은 뭐야?

A.
Vector의 길이다. Embedding Model마다 Dimension이 다를 수 있다.

Q. Embedding Model을 바꾸면 기존 Vector를 써도 돼?

A.
일반적으로 안 된다. 새 Embedding Model로 문서를 다시 Embedding하고 재색인해야 한다.

Q. 서로 다른 Embedding Model의 Vector를 비교해도 돼?

A.
안 된다. 같은 Embedding Model과 같은 Vector Space에서 생성된 Vector끼리 비교해야 한다.

Q. Semantic Search가 뭐야?

A.
단어가 정확히 일치하지 않아도 의미가 비슷한 문서를 찾는 검색 방식이다.

Q. Keyword Search와 Semantic Search 차이는?

A.
Keyword Search는 단어 일치 기반이고, Semantic Search는 의미 유사도 기반이다.

Q. 기술 문서에는 Semantic Search만 쓰면 돼?

A.
아니다. 에러명, 클래스명, 메서드명은 Keyword Search가 유리하므로 Hybrid Search를 고려한다.

Q. Semantic Similarity는 뭐야?

A.
Query Vector와 Document Vector가 의미적으로 얼마나 가까운지 계산하는 기준이다.

Q. Similarity Score가 높으면 무조건 좋은 문서야?

A.
아니다. Score는 의미 유사도일 뿐이고 질문 의도와 맞는지 검토해야 한다.

Q. Similarity Score는 정답 확률이야?

A.
아니다. 검색 후보를 정렬하기 위한 Ranking 기준이다.

Q. BGE-M3는 어디에 써?

A.
한국어/영어 혼합 문서 검색, Dense Retrieval, RAG 검색에 사용할 수 있는 Multilingual Embedding Model로 활용한다.

Q. BGE-M3가 답변도 생성해?

A.
아니다. BGE-M3는 Embedding Model이며 검색용 Vector를 생성한다.

Q. 한국어 RAG에는 어떤 Embedding Model이 좋아?

A.
한국어와 영어 기술 용어가 섞인 문서라면 Multilingual Embedding Model이 유리하다.

Q. 검색 결과가 안 나올 때 어떻게 해?

A.
Query 표현, Chunk 제목, Metadata, Embedding 생성 여부, 문서 수정 후 재색인 여부를 먼저 확인한다.

Q. 관련 없는 문서가 검색되면 어떻게 해?

A.
Chunk를 주제별로 나누고 Top-K, Similarity Threshold, Metadata Filter, Reranking을 검토한다.

Q. 검색은 됐는데 답변이 틀리면 어떻게 해?

A.
Retrieved Context 품질, Prompt Grounding, Chunk 부족, 충돌 문서 포함 여부를 점검한다.

Q. RAG 검색 품질은 어떻게 개선해?

A.
Chunk 구조 개선, Metadata 보강, Retrieval Queries 추가, Query Rewrite, Hybrid Search, Reranking을 단계적으로 적용한다.

Q. Embedding 품질보다 Chunk 품질이 중요한 경우가 있어?

A.
있다. Chunk가 너무 크거나 작고 제목과 Metadata가 부실하면 좋은 Embedding Model을 써도 검색 품질이 낮다.

Q. Vector만 저장하면 안 돼?

A.
안 된다. 원문 Text와 Metadata가 있어야 답변 근거와 출처를 제시할 수 있다.

Q. 문서 수정 후 바로 검색 결과가 바뀌어?

A.
아니다. 수정된 문서를 다시 Embedding하고 Vector Index를 갱신해야 한다.
