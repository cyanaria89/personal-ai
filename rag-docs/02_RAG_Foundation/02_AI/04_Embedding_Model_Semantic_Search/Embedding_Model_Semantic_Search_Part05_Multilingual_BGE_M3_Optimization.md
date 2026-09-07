# Embedding Model & Semantic Search Part05 Multilingual BGE-M3 Optimization

---

# 1. Multilingual Retrieval Core

## 1.1 Multilingual Retrieval

### [개념]

Multilingual Retrieval은 여러 언어가 섞인 문서와 Query를 검색하는 방식이다.

개발 문서는 보통 한국어 설명과 영어 기술 용어가 함께 등장한다.
따라서 한국어 Query와 영어 Keyword를 모두 처리할 수 있는 Embedding Model과 문서 구조가 필요하다.

예시:

```text
한국어 Query:
청크 크기는 어떻게 정해야 해?

영어 기술 용어:
Chunk Size
Chunk Overlap
Semantic Chunking
```

Multilingual Retrieval의 목적:

- 한국어 자연어 질문 검색
- 영어 기술 용어 검색
- 한국어 설명 + 영어 Keyword 혼합 검색
- RAG 문서 검색 품질 개선
- Agent가 사용자 질문을 Domain 문서와 안정적으로 연결

---

### [핵심]

- 개발 RAG 문서는 한국어와 영어가 섞인다.
- 한국어 Query만으로 영어 기술 용어 문서를 찾기 어려울 수 있다.
- 영어 Keyword만으로 한국어 설명 문서를 찾기 어려울 수 있다.
- 핵심 용어는 한글 + 영어 병기가 좋다.
- Multilingual Embedding Model은 한국어/영어 혼합 검색에 유리하다.
- BGE-M3는 Multilingual Retrieval에 활용할 수 있다.
- FAQ와 Retrieval Queries에는 실제 한국어 질문을 포함한다.
- Header에는 영어 기술 용어를 포함하는 것이 좋다.

---

### [실무]

2026 실무 기준에서 개인 RAG 문서는 다음 구조를 권장한다.

```text
한국어 설명
+ 영어 기술 용어
+ 실제 사용자 질문 FAQ
+ Retrieval Queries
+ Metadata tags
```

좋은 문서 표현:

```md
# Query Embedding / 사용자 질문 벡터화

### [개념]

Query Embedding은 사용자 질문(User Query)을 Embedding Model로 Vector로 변환하는 과정이다.
```

좋은 이유:

- 한국어 Query와 매칭 가능
- 영어 기술 용어와 매칭 가능
- Agent가 개념과 원어를 함께 인식 가능
- Semantic Search와 Keyword Search 모두에 유리

나쁜 문서 표현:

```md
# 질문 처리

질문을 숫자로 바꿔서 검색한다.
```

나쁜 이유:

- Query Embedding Keyword 없음
- Vector Keyword 없음
- Embedding Model Keyword 없음
- 영어 기술 용어 검색 약함
- Retrieval 품질 낮음

---

### [주의]

- 한국어 번역어만 사용하지 않는다.
- 영어 기술 용어만 사용하지 않는다.
- 핵심 Keyword를 Header에서 누락하지 않는다.
- FAQ를 너무 추상적으로 작성하지 않는다.
- Query Expansion이 원래 사용자 의도를 바꾸지 않도록 한다.
- Multilingual Embedding Model을 사용해도 Chunk 구조가 나쁘면 검색 품질은 낮다.
- 한국어 검색 실패를 무조건 Model 문제로 판단하지 않는다.

---

### [FAQ]

Q. Multilingual Retrieval은 뭐야?

A.
한국어와 영어처럼 여러 언어가 섞인 Query와 Document를 검색하는 방식이다.

Q. 개발 문서에서 Multilingual Retrieval이 왜 중요해?

A.
개발 문서는 한국어 설명과 영어 기술 용어가 함께 등장하므로 두 언어를 모두 검색할 수 있어야 한다.

Q. 한국어 Query로 영어 기술 용어 문서를 찾으려면 어떻게 해?

A.
핵심 용어를 한글 + 영어로 병기하고 FAQ와 Retrieval Queries에 실제 한국어 질문을 추가한다.

Q. Multilingual Embedding Model만 쓰면 해결돼?

A.
아니다. Chunk 제목, 용어 병기, Metadata, FAQ 품질도 함께 좋아야 한다.

---

# 2. Korean English Mixed Document

## 2.1 Korean English Term Pairing

### [개념]

Korean English Term Pairing은 핵심 개념을 한국어 표현과 영어 기술 용어로 함께 작성하는 규칙이다.

예시:

```text
의미 검색 / Semantic Search
사용자 질문 벡터화 / Query Embedding
문서 벡터화 / Document Embedding
청크 크기 / Chunk Size
유사도 점수 / Similarity Score
```

이 구조는 한국어 Query와 영어 Keyword 검색을 동시에 강화한다.

---

### [핵심]

- 핵심 용어는 한글 + 영어 병기한다.
- Header에 영어 기술 용어를 포함한다.
- 본문 첫 문장에 한국어 설명과 영어 용어를 함께 배치한다.
- FAQ에는 실제 한국어 질문을 넣는다.
- Retrieval Queries에는 한국어 질문과 영어 Keyword를 함께 포함한다.
- Metadata tags에는 영어 Keyword 중심으로 넣는다.
- 클래스명, 메서드명, 에러명은 원문을 유지한다.
- 번역어가 어색하면 영어 원문을 우선 유지한다.

---

### [실무]

권장 용어 병기 예시:

| 한국어 표현        | 영어 기술 용어       |
| ------------------ | -------------------- |
| 임베딩             | Embedding            |
| 임베딩 모델        | Embedding Model      |
| 의미 검색          | Semantic Search      |
| 키워드 검색        | Keyword Search       |
| 하이브리드 검색    | Hybrid Search        |
| 사용자 질문 벡터화 | Query Embedding      |
| 문서 벡터화        | Document Embedding   |
| 청크               | Chunk                |
| 청크 크기          | Chunk Size           |
| 청크 중복          | Chunk Overlap        |
| 메타데이터         | Metadata             |
| 상위 K개 검색      | Top-K Retrieval      |
| 유사도 임계값      | Similarity Threshold |
| 재정렬             | Reranking            |
| 중복 제거          | Deduplication        |
| 검색 평가          | Retrieval Evaluation |

문서 작성 예시:

```md
# Similarity Threshold / 유사도 임계값

### [개념]

Similarity Threshold는 유사도 점수가 낮은 검색 결과를 제외하는 기준이다.
```

FAQ 예시:

```md
Q. 유사도 임계값은 뭐야?

A.  
Similarity Threshold는 관련도가 낮은 Chunk를 제외해 RAG Context 품질을 높이는 기준이다.
```

---

### [주의]

- 한글 번역어와 영어 용어를 문서마다 다르게 쓰지 않는다.
- `청크`, `Chunk`, `분할 단위`를 무분별하게 혼용하지 않는다.
- `유사도 임계값`, `Threshold`, `Minimum Score`를 문맥 없이 섞지 않는다.
- FAQ 질문은 실제 사용자가 입력할 표현으로 작성한다.
- Metadata tags에는 공백과 대소문자 규칙을 통일한다.
- 영어 원문이 중요한 기술 용어는 번역하지 않고 유지한다.

---

### [FAQ]

Q. 한글과 영어 용어를 왜 같이 써?

A.
한국어 Query와 영어 기술 용어 검색을 모두 강화하기 위해서다.

Q. 모든 용어를 한글로 번역하면 안 돼?

A.
권장하지 않는다. 개발 문서는 영어 기술 용어가 많아 원문 Keyword 검색이 중요하다.

Q. 모든 용어를 영어로만 쓰면 안 돼?

A.
한국어 질문과 매칭이 약해질 수 있으므로 핵심 개념은 한글 설명도 함께 쓰는 것이 좋다.

Q. Metadata tags는 한글로 써야 해 영어로 써야 해?

A.
일반적으로 영어 Keyword 중심으로 쓰고, 필요한 경우 한국어 Keyword를 보조로 추가한다.

---

# 3. BGE-M3 Core

## 3.1 BGE-M3

### [개념]

BGE-M3는 Multilingual Embedding Model로 사용할 수 있는 Embedding Model이다.

BGE-M3는 한국어와 영어가 섞인 RAG 문서 검색에 활용할 수 있다.
개발 문서에서는 한국어 설명, 영어 기술 용어, 코드 Keyword가 함께 등장하므로 BGE-M3 같은 Multilingual Embedding Model이 유용하다.

활용 대상:

- Korean Retrieval
- English Technical Term Retrieval
- Mixed Language Document Search
- Dense Retrieval
- Sparse Retrieval
- Multi-vector Retrieval
- RAG Document Search

---

### [핵심]

- BGE-M3는 Multilingual Embedding Model로 활용할 수 있다.
- 한국어 RAG 문서 검색에 사용할 수 있다.
- 한국어 설명 + 영어 기술 용어 혼합 검색에 유리하다.
- Dense Retrieval 중심으로 사용할 수 있다.
- Hybrid Search와 Reranking으로 품질을 보완할 수 있다.
- Local 환경에서는 모델 로딩 시간과 자원 사용량을 고려한다.
- BGE-M3를 사용해도 Chunk 구조가 나쁘면 검색 품질은 낮다.
- BGE-M3는 Chat Model이 아니라 Embedding Model이다.

---

### [실무]

개인 AI 서버 구성 예시:

```text
Chat Model:
Qwen2.5 14B

Embedding Model:
BGE-M3

RAG Use Case:
한국어 개발 문서 검색
AI Agent 문서 검색
Backend / Frontend / DevOps / AI Domain 문서 검색
```

BGE-M3 적용 기준:

```text
문서 언어:
한국어 + 영어 기술 용어 혼합

검색 목적:
RAG Retrieval

문서 구조:
Markdown Header
[개념] / [핵심] / [실무] / [FAQ]
Retrieval Queries

검색 전략:
Dense Retrieval 기본
Keyword Search 보완
Hybrid Search 확장 가능
Reranking 적용 가능
```

좋은 BGE-M3 대상 문서:

```md
# Hybrid Search / 하이브리드 검색

### [개념]

Hybrid Search는 Keyword Search와 Semantic Search를 결합해 정확한 기술 용어 검색과 의미 검색을 함께 수행하는 방식이다.
```

좋은 이유:

- 영어 Keyword 포함
- 한국어 설명 포함
- Domain 개념 명확
- Query Matching 가능
- Semantic Search와 Keyword Search 모두 유리

---

### [주의]

- BGE-M3는 답변 생성 모델이 아니다.
- BGE-M3를 사용해도 Hallucination이 자동으로 해결되지 않는다.
- BGE-M3를 사용해도 문서 구조가 나쁘면 Retrieval 품질이 낮다.
- Embedding Model 변경 시 기존 Vector 재사용을 피한다.
- Model 변경 후 Vector Dimension과 Index 호환성을 확인한다.
- 문서 수정 후 재Embedding이 필요하다.
- Local 환경에서는 응답 속도와 리소스 사용량을 확인한다.

---

### [FAQ]

Q. BGE-M3는 뭐야?

A.
한국어와 영어를 포함한 다국어 검색에 활용할 수 있는 Multilingual Embedding Model이다.

Q. BGE-M3는 어디에 써?

A.
한국어/영어 혼합 문서 검색, Dense Retrieval, RAG 검색에 사용할 수 있다.

Q. BGE-M3가 답변도 생성해?

A.
아니다. BGE-M3는 Embedding Model이며 검색용 Vector를 생성한다.

Q. BGE-M3를 쓰면 RAG 품질이 무조건 좋아져?

A.
아니다. Chunk 구조, Metadata, FAQ, Retrieval Queries, Query 품질도 함께 좋아야 한다.

---

# 4. Dense Sparse Multi-Vector

## 4.1 Dense Retrieval

### [개념]

Dense Retrieval은 Text를 Dense Vector로 변환해 의미 유사도 기반으로 검색하는 방식이다.

Dense Vector는 대부분의 값이 숫자로 채워진 연속적인 Vector다.
Semantic Search에서 일반적으로 사용된다.

기본 Flow:

```text
Text
→ Dense Embedding
→ Dense Vector
→ Similarity Search
→ Retrieved Chunks
```

---

### [핵심]

- Dense Retrieval은 의미 기반 검색에 강하다.
- 표현이 달라도 의미가 비슷하면 검색될 수 있다.
- 자연어 질문 검색에 유리하다.
- Embedding Model 품질에 영향을 받는다.
- Chunk 구조가 검색 품질에 큰 영향을 준다.
- 정확한 에러명, 클래스명 검색은 Keyword Search 보완이 필요할 수 있다.
- BGE-M3는 Dense Retrieval에 활용할 수 있다.

---

### [실무]

Dense Retrieval에 적합한 Query:

```text
RAG 검색 품질을 높이려면 문서를 어떻게 작성해야 해?
Chunk를 어떻게 나누면 검색이 잘 돼?
의미 기반 검색은 어떻게 동작해?
```

Dense Retrieval에 약할 수 있는 Query:

```text
SecurityFilterChain
NullPointerException
application.properties
findByUserIdAndStatus
```

실무 기준:

```text
자연어 개념 질문
→ Dense Retrieval 우선

정확한 기술 용어
→ Keyword Search 보완

개념 + 기술 용어 혼합
→ Hybrid Search 검토
```

---

### [주의]

- Dense Retrieval은 정확한 Keyword 검색에 약할 수 있다.
- Chunk가 너무 크면 의미가 흐려질 수 있다.
- Chunk가 너무 작으면 문맥이 부족할 수 있다.
- Similarity Score를 정답 확률로 해석하지 않는다.
- Dense Retrieval 결과는 필요 시 Reranking한다.

---

### [FAQ]

Q. Dense Retrieval은 뭐야?

A.
Text를 Dense Vector로 변환해 의미 유사도 기반으로 관련 문서를 찾는 검색 방식이다.

Q. Dense Retrieval은 언제 좋아?

A.
개념 질문이나 자연어 질문처럼 표현이 다양할 수 있는 검색에 유리하다.

Q. Dense Retrieval만 쓰면 충분해?

A.
정확한 기술 용어 검색에는 약할 수 있어 Keyword Search나 Hybrid Search를 함께 고려한다.

---

## 4.2 Sparse Retrieval

### [개념]

Sparse Retrieval은 Keyword나 Token 중요도를 기반으로 문서를 검색하는 방식이다.

Sparse Vector는 대부분의 값이 0이고 일부 Keyword만 의미 있는 값을 가진다.
Keyword Search와 유사한 성격을 가진다.

---

### [핵심]

- Sparse Retrieval은 정확한 Keyword 검색에 강하다.
- 에러명, 클래스명, 메서드명 검색에 유리하다.
- 단어가 다르면 검색이 약할 수 있다.
- 자연어 의미 검색은 Dense Retrieval이 유리할 수 있다.
- BGE-M3는 Sparse Retrieval 기능을 함께 설명할 수 있다.
- 기술 문서 RAG에서는 Dense와 Sparse를 조합할 수 있다.

---

### [실무]

Sparse Retrieval에 적합한 Query:

```text
BGE-M3
Top-K
Similarity Threshold
SecurityFilterChain
@Transactional
NullPointerException
```

Sparse Retrieval이 약할 수 있는 Query:

```text
문서를 잘 나누는 방법 알려줘
검색 결과가 이상할 때 어떻게 고쳐?
```

실무 판단:

```text
정확한 Keyword가 중요함
→ Sparse Retrieval / Keyword Search

표현이 다양한 자연어 질문
→ Dense Retrieval

둘 다 필요함
→ Hybrid Retrieval
```

---

### [주의]

- Sparse Retrieval은 의미가 비슷하지만 단어가 다른 문서를 놓칠 수 있다.
- 오타와 표현 차이에 약할 수 있다.
- 한국어 조사, 띄어쓰기, 복합어 처리에 영향을 받을 수 있다.
- Sparse Retrieval만으로 RAG 전체 검색을 구성하면 개념 질문이 약할 수 있다.
- Dense Retrieval과 함께 사용하는 것이 실무적으로 유리할 수 있다.

---

### [FAQ]

Q. Sparse Retrieval은 뭐야?

A.
Keyword나 Token 중요도를 기반으로 문서를 검색하는 방식이다.

Q. Sparse Retrieval은 언제 좋아?

A.
에러명, 클래스명, 메서드명, 설정 키처럼 정확한 단어 검색이 중요할 때 좋다.

Q. Sparse Retrieval과 Dense Retrieval은 뭐가 달라?

A.
Sparse Retrieval은 Keyword 중심이고, Dense Retrieval은 의미 유사도 중심이다.

---

## 4.3 Multi-Vector Retrieval

### [개념]

Multi-Vector Retrieval은 하나의 문서나 Chunk를 여러 Vector 표현으로 검색하는 방식이다.

하나의 Text를 단일 Vector로만 표현하면 세부 의미를 놓칠 수 있다.
Multi-Vector 방식은 복합 의미를 더 잘 표현하기 위해 사용할 수 있다.

---

### [핵심]

- Multi-Vector Retrieval은 하나의 문서를 여러 Vector로 표현할 수 있다.
- 긴 문서나 복합 의미 검색에 도움이 될 수 있다.
- 검색 품질을 높일 수 있지만 저장량과 계산량이 증가한다.
- Chunk 품질이 낮으면 Multi-Vector도 한계가 있다.
- 개인 RAG 초기 단계에서는 Dense Retrieval부터 안정화하는 것이 좋다.
- 고도화 단계에서 Hybrid Search, Reranking과 함께 검토한다.

---

### [실무]

Multi-Vector가 필요한 경우:

| 상황                            | 이유                                |
| ------------------------------- | ----------------------------------- |
| 하나의 Chunk에 여러 의미가 있음 | 단일 Vector로 표현이 부족할 수 있음 |
| 긴 문서 검색 품질이 낮음        | 세부 의미 검색이 어려움             |
| 복합 질문이 많음                | 여러 관점의 검색 필요               |
| Reranking 전 후보 품질 개선     | 후보 검색 Recall 향상 가능          |

초기 적용 우선순위:

```text
1. Chunk 구조 개선
2. Metadata 보강
3. Dense Retrieval 안정화
4. Hybrid Search 적용
5. Reranking 적용
6. Multi-Vector Retrieval 검토
```

---

### [주의]

- Multi-Vector는 시스템 복잡도를 높인다.
- 저장 공간과 검색 비용이 증가할 수 있다.
- Chunking이 나쁘면 Multi-Vector로도 품질 개선이 제한적이다.
- 개인 로컬 환경에서는 리소스 사용량을 고려한다.
- 초기 RAG 문서 제작 단계에서는 과도한 구조보다 기본 검색 품질이 우선이다.

---

### [FAQ]

Q. Multi-Vector Retrieval은 뭐야?

A.
하나의 문서나 Chunk를 여러 Vector로 표현해 검색하는 방식이다.

Q. Multi-Vector Retrieval은 언제 필요해?

A.
긴 문서, 복합 의미, 복합 질문 검색에서 단일 Vector 표현이 부족할 때 검토한다.

Q. 개인 RAG에서 Multi-Vector부터 써야 해?

A.
아니다. 먼저 Chunk 구조, Metadata, Dense Retrieval, Hybrid Search, Reranking을 안정화하는 것이 좋다.

---

# 5. Query Optimization

## 5.1 Korean Query Rewrite

### [개념]

Korean Query Rewrite는 한국어 사용자 질문을 Retrieval에 적합하게 명확히 다시 쓰는 과정이다.

짧고 모호한 한국어 질문은 Embedding 검색에서 의도가 약할 수 있다.

예시:

```text
Original Query:
검색 안 돼

Rewritten Query:
RAG Retrieval 검색 결과가 안 나올 때 Query, Chunk, Metadata, Threshold, Embedding 재생성 문제를 어떻게 점검해야 하는가?
```

---

### [핵심]

- Query Rewrite는 검색 의도를 명확히 한다.
- 짧은 한국어 Query는 Domain Keyword를 보강한다.
- 영어 기술 용어를 함께 추가할 수 있다.
- 원래 의도를 바꾸면 안 된다.
- Query Rewrite는 No Result와 Low Rank 개선에 도움될 수 있다.
- Query가 너무 넓으면 관련 없는 Chunk가 검색될 수 있다.
- Query Rewrite는 Retrieval 전 단계에서 수행한다.

---

### [실무]

Rewrite가 필요한 Query:

| Original Query     | Rewritten Query                                                         |
| ------------------ | ----------------------------------------------------------------------- |
| 검색 안 돼         | RAG Retrieval 검색 결과가 안 나올 때 원인과 해결 방법은?                |
| 크기 어떻게 해?    | RAG Chunk Size와 Chunk Overlap은 어떻게 정해야 하는가?                  |
| 점수 높으면 맞아?  | Similarity Score가 높으면 무조건 관련 문서인지 어떻게 판단하는가?       |
| 한국어 검색 별로야 | 한국어 Query와 영어 기술 용어가 섞인 RAG 검색 품질을 어떻게 개선하는가? |

Rewrite 기준:

```text
사용자 원래 의도 유지
+ Domain Keyword 추가
+ 영어 기술 용어 보강
+ 검색 대상 명확화
```

---

### [주의]

- Query Rewrite가 사용자 의도를 바꾸면 안 된다.
- 너무 많은 Keyword를 추가하면 관련 없는 문서가 검색될 수 있다.
- Query Rewrite로 모든 검색 실패를 해결할 수는 없다.
- 문서 자체에 관련 Keyword가 없으면 Rewrite 효과가 제한적이다.
- Rewrite 결과는 Golden Query로 평가한다.

---

### [FAQ]

Q. Korean Query Rewrite는 뭐야?

A.
한국어 사용자 질문을 Retrieval에 적합하도록 더 명확하게 다시 쓰는 과정이다.

Q. Query Rewrite는 언제 필요해?

A.
질문이 짧거나 모호해서 검색 의도가 약할 때 필요하다.

Q. Query Rewrite할 때 영어 용어를 넣어도 돼?

A.
가능하다. 개발 문서 검색에서는 Chunk Size, Embedding, Retrieval 같은 영어 기술 용어를 함께 넣는 것이 도움이 된다.

---

## 5.2 Query Expansion

### [개념]

Query Expansion은 원래 Query에 관련 Keyword를 추가해 검색 누락을 줄이는 방식이다.

예시:

```text
Original Query:
검색 결과가 이상해

Expanded Query:
RAG Retrieval 검색 결과가 이상할 때 Top-K, Similarity Threshold, Chunking, Metadata, Reranking 문제를 어떻게 점검해야 하는가?
```

---

### [핵심]

- Query Expansion은 Recall 개선에 도움될 수 있다.
- 관련 Keyword를 추가해 검색 범위를 넓힌다.
- Domain Term을 추가하면 검색 누락을 줄일 수 있다.
- 과도한 Expansion은 관련 없는 Chunk를 늘릴 수 있다.
- Query Rewrite는 의도 명확화, Query Expansion은 검색 범위 확장에 가깝다.
- Expansion Keyword는 문서의 Header, FAQ, Metadata와 맞아야 한다.

---

### [실무]

Expansion Keyword 예시:

| 사용자 표현      | Expansion Keyword                                |
| ---------------- | ------------------------------------------------ |
| 검색 안 됨       | Retrieval, No Result, Query Rewrite, Metadata    |
| 이상한 문서 나옴 | Irrelevant Result, Top-K, Threshold, Reranking   |
| 중복 검색        | Duplicate Result, Chunk Overlap, Deduplication   |
| 한국어 검색      | Korean Retrieval, Multilingual Embedding, BGE-M3 |
| 점수             | Similarity Score, Cosine Similarity, Threshold   |
| 순위             | Ranking, MRR, Reranking, Low Rank                |

Query Expansion Flow:

```text
Original Query
→ Intent 확인
→ Domain Keyword 추가
→ 영어 기술 용어 추가
→ 검색 실행
→ 결과 품질 확인
```

---

### [주의]

- Expansion Keyword를 무분별하게 많이 넣지 않는다.
- 관련 없는 Domain Keyword를 추가하지 않는다.
- Expansion은 Precision을 낮출 수 있다.
- Query Expansion 적용 후 Reranking이 필요할 수 있다.
- 원래 Query를 보존하고 확장 Query를 별도 관리하는 것이 좋다.

---

### [FAQ]

Q. Query Expansion은 뭐야?

A.
원래 질문에 관련 Keyword를 추가해 검색 누락을 줄이는 방식이다.

Q. Query Expansion과 Query Rewrite는 뭐가 달라?

A.
Query Rewrite는 질문 의도를 명확히 하고, Query Expansion은 관련 Keyword를 추가해 검색 범위를 넓힌다.

Q. Query Expansion은 항상 좋아?

A.
아니다. 과도하게 확장하면 관련 없는 Chunk가 많이 검색될 수 있다.

---

# 6. Document Optimization for BGE-M3

## 6.1 Header and FAQ Optimization

### [개념]

BGE-M3를 활용한 RAG 검색 품질은 Embedding Model뿐 아니라 문서 구조에 크게 의존한다.

Header, FAQ, Retrieval Queries, Metadata가 명확해야 한국어/영어 혼합 Query와 잘 매칭된다.

---

### [핵심]

- Header에 핵심 영어 기술 용어를 포함한다.
- 첫 문장에 한국어 설명과 영어 용어를 함께 둔다.
- FAQ는 실제 한국어 질문 형태로 작성한다.
- Retrieval Queries에는 다양한 사용자 표현을 포함한다.
- Metadata tags에는 영어 Keyword를 넣는다.
- Chunk는 하나의 개념만 다룬다.
- Code Block과 설명은 같은 Chunk에 유지한다.
- 문서 수정 후 재Embedding한다.

---

### [실무]

좋은 Header:

```md
# Query Embedding / 사용자 질문 벡터화

# Document Embedding / 문서 벡터화

# Similarity Threshold / 유사도 임계값

# Reranking / 검색 결과 재정렬
```

좋은 FAQ:

```md
Q. 한국어 질문으로 영어 기술 용어 문서를 잘 찾으려면 어떻게 해?

A.  
핵심 용어를 한글 + 영어로 병기하고 FAQ, Retrieval Queries, Metadata tags를 보강한다.
```

좋은 Retrieval Queries:

```md
Q. BGE-M3는 한국어 RAG 검색에 좋아?
A. BGE-M3는 한국어/영어 혼합 문서 검색에 활용할 수 있지만 Chunk 구조와 Metadata 품질도 중요하다.

Q. 한국어 검색 결과가 안 나오면 어떻게 해?
A. 한글/영어 용어 병기, FAQ 추가, Query Rewrite, Metadata, 재Embedding 여부를 확인한다.
```

---

### [주의]

- Header가 모호하면 BGE-M3를 사용해도 검색 품질이 낮다.
- FAQ가 실제 질문과 다르면 Query Matching 효과가 낮다.
- Metadata tags가 부실하면 필터링과 Agent Routing이 약해진다.
- 같은 질문을 모든 문서에 반복하면 중복 검색이 늘어난다.
- Chunk에 여러 개념을 섞지 않는다.

---

### [FAQ]

Q. BGE-M3용 문서 최적화에서 가장 중요한 것은?

A.
Header, FAQ, Retrieval Queries, Metadata에 한글과 영어 핵심 용어를 명확히 포함하는 것이다.

Q. Header에 영어 기술 용어를 넣어야 해?

A.
넣는 것이 좋다. 개발 문서 검색에서는 영어 Keyword가 Retrieval 품질에 중요하다.

Q. FAQ는 어떤 식으로 작성해야 해?

A.
실제 사용자가 물어볼 한국어 질문 형태로 작성하고 답변에는 영어 기술 용어를 함께 포함한다.

---

# 7. Local RAG Optimization

## 7.1 Local Embedding Performance

### [개념]

Local RAG 환경에서는 Embedding Model 품질뿐 아니라 로딩 시간, 처리 속도, 메모리 사용량도 고려해야 한다.

BGE-M3 같은 Embedding Model을 로컬에서 사용할 경우 문서 수, Chunk 수, 재Embedding 주기에 따라 리소스 사용량이 달라진다.

---

### [핵심]

- Local Embedding은 리소스 사용량을 고려해야 한다.
- Chunk 수가 많을수록 Embedding 생성 시간이 증가한다.
- 문서 수정 후 재Embedding 비용을 고려한다.
- Model 변경 시 전체 Vector 재생성이 필요할 수 있다.
- 너무 많은 중복 Chunk는 저장 공간과 검색 비용을 증가시킨다.
- Chunk 품질을 높이면 불필요한 Top-K 증가를 줄일 수 있다.
- Reranking은 품질을 높일 수 있지만 Latency가 증가한다.

---

### [실무]

Local RAG 운영 기준:

```text
문서 작성 단계:
Chunk 품질 우선

Embedding 단계:
문서 수정 후 재Embedding

검색 단계:
Top-K 과다 증가 지양

최적화 단계:
Golden Query 기반 평가

고도화 단계:
Hybrid Search / Reranking 검토
```

리소스 최적화 기준:

| 항목         | 최적화 방향                    |
| ------------ | ------------------------------ |
| Chunk 수     | 중복 Chunk 제거                |
| Chunk Size   | 너무 작은 Chunk 과다 생성 방지 |
| Overlap      | 과도한 Overlap 축소            |
| Metadata     | 필터링 가능한 구조 유지        |
| Top-K        | 필요한 만큼만 사용             |
| Reranking    | 품질 필요 시 적용              |
| Re-Embedding | 변경 문서 중심으로 수행        |

---

### [주의]

- 문서 품질이 낮은 상태에서 Model만 키우지 않는다.
- Top-K를 크게 해서 검색 품질을 억지로 보완하지 않는다.
- Overlap을 과도하게 설정하지 않는다.
- 중복 Retrieval Queries를 여러 문서에 반복하지 않는다.
- 재Embedding 누락으로 오래된 Vector를 사용하지 않는다.
- Local 환경에서는 Latency와 품질의 균형을 본다.

---

### [FAQ]

Q. Local RAG에서 BGE-M3를 쓸 때 무엇을 봐야 해?

A.
검색 품질뿐 아니라 모델 로딩 시간, Chunk 수, 재Embedding 비용, 검색 Latency를 함께 봐야 한다.

Q. Chunk 수가 많으면 무조건 좋아?

A.
아니다. 중복 Chunk가 많으면 저장 공간과 검색 비용이 늘고 중복 검색 문제가 발생할 수 있다.

Q. Local RAG 최적화는 어디서 시작해?

A.
Model 변경보다 Chunk 구조, FAQ, Retrieval Queries, Metadata 품질 개선부터 시작하는 것이 좋다.

---

# 8. Korean Retrieval Troubleshooting

## 8.1 Korean Query Search Failure

### [개념]

Korean Query Search Failure는 한국어 질문이 관련 문서를 찾지 못하거나 낮은 순위로 검색되는 문제다.

한국어 Query와 영어 기술 용어 문서의 표현 차이가 주요 원인일 수 있다.

---

### [Troubleshooting]

문제:

- 한국어 질문으로 관련 문서가 검색되지 않음
- 영어 Keyword로는 검색되지만 한국어 Query로는 약함
- 한국어 Query가 관련 없는 Chunk를 검색함

원인:

- 한글/영어 용어 병기 부족
- Header에 영어 기술 용어만 있음
- FAQ에 실제 한국어 질문 없음
- Retrieval Queries 부족
- Query가 너무 짧거나 모호함
- Metadata tags가 영어만 있고 문서 본문 설명이 약함
- Chunk에 여러 개념 혼합
- Embedding 재생성 누락

해결:

- 핵심 용어 한글 + 영어 병기
- Header에 한국어 설명 보조 추가
- FAQ에 실제 한국어 질문 추가
- Retrieval Queries 강화
- Query Rewrite 적용
- Query Expansion 적용
- Metadata tags 보강
- Chunk를 하나의 개념 중심으로 분리
- 문서 재Embedding

---

### [실무]

점검 Flow:

```text
한국어 Query 실패 확인
→ 영어 Keyword Query로 검색 테스트
→ Expected Chunk Header 확인
→ 한글 설명 포함 여부 확인
→ FAQ / Retrieval Queries 확인
→ Query Rewrite 적용
→ 문서 수정
→ 재Embedding
→ Golden Query 재평가
```

예시:

```text
실패 Query:
청크 크기는 어떻게 잡아?

기존 Header:
# Chunk Size

개선 Header:
# Chunk Size / 청크 크기

추가 FAQ:
Q. 청크 크기는 어떻게 잡아?

A.
Chunk Size는 하나의 개념이 독립적으로 이해될 정도로 유지하되 여러 개념이 섞이지 않도록 조정한다.
```

---

### [FAQ]

Q. 한국어 검색 결과가 안 나오면 어떻게 해?

A.
한글/영어 용어 병기, Header, FAQ, Retrieval Queries, Query Rewrite, 재Embedding 여부를 확인한다.

Q. 영어 Keyword로는 검색되는데 한국어 질문으로는 안 돼. 왜 그래?

A.
문서에 한국어 질문 표현이나 한글 설명이 부족해 Query와 Chunk의 의미 매칭이 약할 수 있다.

Q. 한국어 Query 검색 품질은 어떻게 개선해?

A.
핵심 용어를 한글 + 영어로 병기하고 실제 한국어 FAQ와 Retrieval Queries를 추가한다.

---

## 8.2 Technical Term Search Failure

### [개념]

Technical Term Search Failure는 영어 기술 용어, 클래스명, 메서드명, 에러명 검색이 제대로 되지 않는 문제다.

Semantic Search만으로 정확한 Keyword 검색이 부족할 수 있으므로 Keyword Search 또는 Hybrid Search를 고려한다.

---

### [Troubleshooting]

문제:

- 클래스명 검색이 안 됨
- 메서드명 검색이 안 됨
- 에러명 검색 결과가 약함
- 영어 기술 용어가 포함된 Chunk가 낮은 순위에 있음

원인:

- 문서에 정확한 Keyword가 없음
- Header에 기술 용어 누락
- Code Block과 설명이 분리됨
- Keyword Search 미사용
- Hybrid Search 미사용
- Metadata tags에 기술 용어 없음
- 오타 또는 표기 불일치

해결:

- 정확한 기술 용어를 Header에 포함
- FAQ에 기술 용어 질문 추가
- Metadata tags에 Keyword 추가
- Code Block과 설명을 같은 Chunk에 유지
- Keyword Search 적용
- Hybrid Search 적용
- Reranking 적용
- 표기 통일

---

### [실무]

기술 용어 검색 강화 예시:

```md
# SecurityFilterChain

### [개념]

SecurityFilterChain은 Spring Security에서 요청 보안 필터 체인을 구성하는 핵심 설정 객체다.

### [FAQ]

Q. SecurityFilterChain은 어디에 써?

A.  
Spring Security에서 인증, 인가, CSRF, 세션 정책 같은 보안 필터 체인을 정의할 때 사용한다.
```

Embedding / Retrieval 문서 예시:

```md
# Similarity Threshold

### [FAQ]

Q. Similarity Threshold는 어디에 써?

A.  
관련도가 낮은 검색 결과를 제외해 RAG Context 품질을 높이는 데 사용한다.
```

---

### [FAQ]

Q. 영어 기술 용어 검색이 안 되면 어떻게 해?

A.
Header, FAQ, Metadata tags에 정확한 기술 용어를 포함하고 Keyword Search 또는 Hybrid Search를 적용한다.

Q. 클래스명이나 메서드명은 Semantic Search로 충분해?

A.
항상 충분하지 않다. 정확한 단어 매칭이 중요하므로 Keyword Search가 유리할 수 있다.

Q. 기술 용어 표기는 어떻게 관리해?

A.
문서 전체에서 같은 표기를 유지하고 Header, 본문, FAQ, Metadata tags에 일관되게 사용한다.

---

# 9. BGE-M3 Evaluation

## 9.1 Multilingual Golden Query

### [개념]

Multilingual Golden Query는 한국어 Query와 영어 기술 용어 Query를 함께 포함한 Retrieval 평가 Query Set이다.

BGE-M3 기반 RAG에서는 한국어 질문과 영어 Keyword 검색이 모두 잘 되는지 평가해야 한다.

---

### [핵심]

- 한국어 자연어 Query를 포함한다.
- 영어 기술 용어 Query를 포함한다.
- 한국어 + 영어 혼합 Query를 포함한다.
- Expected Document와 Expected Section을 지정한다.
- 검색 결과의 Hit Rate와 Ranking을 확인한다.
- 한국어 Query 실패와 영어 Keyword 실패를 분리한다.
- 문서 개선 후 재Embedding하고 재평가한다.

---

### [실무]

Multilingual Golden Query 예시:

| Query Type     | Golden Query                      | Expected Section     |
| -------------- | --------------------------------- | -------------------- |
| 한국어 자연어  | 청크 크기는 어떻게 정해?          | Chunk Size           |
| 영어 기술 용어 | Chunk Size                        | Chunk Size           |
| 혼합 Query     | Chunk Size 청크 크기 기준         | Chunk Size           |
| 한국어 자연어  | 검색 결과가 안 나올 때 어떻게 해? | No Result            |
| 영어 기술 용어 | Similarity Threshold              | Similarity Threshold |
| 혼합 Query     | BGE-M3 한국어 RAG 검색            | BGE-M3               |
| 한국어 자연어  | 유사도 점수가 높으면 무조건 맞아? | Semantic Similarity  |
| 영어 기술 용어 | Reranking                         | Reranker             |

평가 Flow:

```text
한국어 Query 평가
→ 영어 Keyword Query 평가
→ 혼합 Query 평가
→ Expected Section Hit 확인
→ Ranking 확인
→ 실패 유형 분류
→ 문서 수정
→ 재Embedding
→ 재평가
```

---

### [주의]

- 한국어 Query만 평가하지 않는다.
- 영어 Keyword만 평가하지 않는다.
- 혼합 Query도 평가한다.
- Expected Section을 명확히 지정한다.
- Query Type별 실패 원인을 따로 분석한다.
- 문서 수정 후 재Embedding을 반드시 수행한다.

---

### [FAQ]

Q. Multilingual Golden Query는 뭐야?

A.
한국어 질문, 영어 기술 용어, 한국어+영어 혼합 Query를 포함한 Retrieval 평가 Query Set이다.

Q. BGE-M3 평가에서 무엇을 봐야 해?

A.
한국어 Query, 영어 Keyword Query, 혼합 Query가 Expected Document와 Section을 잘 찾는지 확인한다.

Q. 한국어 Query와 영어 Query를 따로 평가해야 해?

A.
그렇다. 실패 원인이 다를 수 있으므로 Query Type별로 나누어 평가하는 것이 좋다.

---

# 10. Best Practice

## 10.1 Multilingual BGE-M3 Best Practice

### [Best Practice]

Multilingual Retrieval Best Practice:

- 핵심 용어를 한글 + 영어로 병기
- Header에 영어 기술 용어 포함
- Header에 필요한 경우 한국어 보조 표현 추가
- 첫 문장에 한국어 설명과 영어 용어 함께 배치
- FAQ는 실제 한국어 질문 형태로 작성
- Retrieval Queries에 한국어 질문, 영어 Keyword, 혼합 Query 포함
- Metadata tags는 영어 Keyword 중심으로 작성
- 클래스명, 메서드명, 에러명은 원문 유지
- Query Rewrite로 짧은 한국어 질문을 명확히 변환
- Query Expansion으로 관련 Domain Keyword 보강
- Dense Retrieval 기본 적용
- 정확한 기술 용어는 Keyword Search 보완
- 복합 Query는 Hybrid Search 검토
- Low Rank는 Reranking 검토
- 중복 검색은 Deduplication 적용
- 한국어 Query와 영어 Keyword를 Golden Query로 따로 평가
- 문서 수정 후 재Embedding
- Model 변경 시 전체 Vector 재생성 검토

---

### [Checklist]

- [ ] 핵심 용어를 한글 + 영어로 병기했는가?
- [ ] Header에 영어 기술 용어가 포함되어 있는가?
- [ ] Header가 한국어 Query와도 매칭 가능한가?
- [ ] 첫 문장에 개념 설명과 영어 용어가 함께 있는가?
- [ ] FAQ가 실제 한국어 질문 형태인가?
- [ ] Retrieval Queries에 한국어 질문이 포함되어 있는가?
- [ ] Retrieval Queries에 영어 Keyword Query가 포함되어 있는가?
- [ ] Retrieval Queries에 한국어+영어 혼합 Query가 포함되어 있는가?
- [ ] Metadata tags에 핵심 영어 Keyword가 포함되어 있는가?
- [ ] 클래스명, 메서드명, 에러명을 원문으로 유지했는가?
- [ ] Query Rewrite 기준이 있는가?
- [ ] Query Expansion 기준이 있는가?
- [ ] Dense Retrieval과 Keyword Search 역할을 구분했는가?
- [ ] Hybrid Search 적용 기준이 있는가?
- [ ] Reranking 적용 기준이 있는가?
- [ ] 한국어 Query Golden Query가 있는가?
- [ ] 영어 Keyword Golden Query가 있는가?
- [ ] 문서 수정 후 재Embedding 규칙이 있는가?
- [ ] BGE-M3가 Chat Model이 아니라 Embedding Model임을 명확히 했는가?

---

### [FAQ]

Q. Multilingual BGE-M3 Best Practice 핵심은 뭐야?

A.
한글 + 영어 용어 병기, 실제 한국어 FAQ, 영어 Keyword Header, Metadata tags, Golden Query 평가를 함께 적용하는 것이다.

Q. 한국어 RAG 문서에서 영어 용어는 얼마나 넣어야 해?

A.
핵심 기술 용어는 Header, 본문 첫 문장, FAQ, Retrieval Queries, Metadata tags에 일관되게 포함하는 것이 좋다.

Q. BGE-M3 기반 RAG 최적화는 어디서 시작해?

A.
Model 변경보다 Chunk 구조, 한글/영어 용어 병기, FAQ, Retrieval Queries, Metadata 개선부터 시작한다.

Q. 한국어 검색 품질 개선 후 무엇을 해야 해?

A.
문서를 재Embedding하고 Multilingual Golden Query로 Hit Rate와 Ranking을 다시 평가한다.

---

# Retrieval Queries

### [FAQ]

Q. Multilingual Retrieval은 뭐야?
A. 한국어와 영어처럼 여러 언어가 섞인 Query와 Document를 검색하는 방식이다.

Q. 개발 문서에서 Multilingual Retrieval이 왜 중요해?
A. 개발 문서는 한국어 설명과 영어 기술 용어가 함께 등장하므로 두 언어를 모두 검색할 수 있어야 한다.

Q. 한국어 Query로 영어 기술 용어 문서를 찾으려면 어떻게 해?
A. 핵심 용어를 한글 + 영어로 병기하고 FAQ와 Retrieval Queries에 실제 한국어 질문을 추가한다.

Q. 한글과 영어 용어를 왜 같이 써?
A. 한국어 Query와 영어 기술 용어 검색을 모두 강화하기 위해서다.

Q. 모든 용어를 한글로 번역하면 안 돼?
A. 권장하지 않는다. 개발 문서는 영어 기술 용어가 많아 원문 Keyword 검색이 중요하다.

Q. 모든 용어를 영어로만 쓰면 안 돼?
A. 한국어 질문과 매칭이 약해질 수 있으므로 핵심 개념은 한글 설명도 함께 쓰는 것이 좋다.

Q. BGE-M3는 뭐야?
A. 한국어와 영어를 포함한 다국어 검색에 활용할 수 있는 Multilingual Embedding Model이다.

Q. BGE-M3는 어디에 써?
A. 한국어/영어 혼합 문서 검색, Dense Retrieval, RAG 검색에 사용할 수 있다.

Q. BGE-M3가 답변도 생성해?
A. 아니다. BGE-M3는 Embedding Model이며 검색용 Vector를 생성한다.

Q. BGE-M3를 쓰면 RAG 품질이 무조건 좋아져?
A. 아니다. Chunk 구조, Metadata, FAQ, Retrieval Queries, Query 품질도 함께 좋아야 한다.

Q. Dense Retrieval은 뭐야?
A. Text를 Dense Vector로 변환해 의미 유사도 기반으로 관련 문서를 찾는 검색 방식이다.

Q. Dense Retrieval은 언제 좋아?
A. 개념 질문이나 자연어 질문처럼 표현이 다양할 수 있는 검색에 유리하다.

Q. Sparse Retrieval은 뭐야?
A. Keyword나 Token 중요도를 기반으로 문서를 검색하는 방식이다.

Q. Sparse Retrieval은 언제 좋아?
A. 에러명, 클래스명, 메서드명, 설정 키처럼 정확한 단어 검색이 중요할 때 좋다.

Q. Sparse Retrieval과 Dense Retrieval은 뭐가 달라?
A. Sparse Retrieval은 Keyword 중심이고, Dense Retrieval은 의미 유사도 중심이다.

Q. Multi-Vector Retrieval은 뭐야?
A. 하나의 문서나 Chunk를 여러 Vector로 표현해 검색하는 방식이다.

Q. Multi-Vector Retrieval은 언제 필요해?
A. 긴 문서, 복합 의미, 복합 질문 검색에서 단일 Vector 표현이 부족할 때 검토한다.

Q. Korean Query Rewrite는 뭐야?
A. 한국어 사용자 질문을 Retrieval에 적합하도록 더 명확하게 다시 쓰는 과정이다.

Q. Query Rewrite는 언제 필요해?
A. 질문이 짧거나 모호해서 검색 의도가 약할 때 필요하다.

Q. Query Rewrite할 때 영어 용어를 넣어도 돼?
A. 가능하다. 개발 문서 검색에서는 Chunk Size, Embedding, Retrieval 같은 영어 기술 용어를 함께 넣는 것이 도움이 된다.

Q. Query Expansion은 뭐야?
A. 원래 질문에 관련 Keyword를 추가해 검색 누락을 줄이는 방식이다.

Q. Query Expansion과 Query Rewrite는 뭐가 달라?
A. Query Rewrite는 질문 의도를 명확히 하고, Query Expansion은 관련 Keyword를 추가해 검색 범위를 넓힌다.

Q. BGE-M3용 문서 최적화에서 가장 중요한 것은?
A. Header, FAQ, Retrieval Queries, Metadata에 한글과 영어 핵심 용어를 명확히 포함하는 것이다.

Q. Header에 영어 기술 용어를 넣어야 해?
A. 넣는 것이 좋다. 개발 문서 검색에서는 영어 Keyword가 Retrieval 품질에 중요하다.

Q. Local RAG에서 BGE-M3를 쓸 때 무엇을 봐야 해?
A. 검색 품질뿐 아니라 모델 로딩 시간, Chunk 수, 재Embedding 비용, 검색 Latency를 함께 봐야 한다.

Q. Chunk 수가 많으면 무조건 좋아?
A. 아니다. 중복 Chunk가 많으면 저장 공간과 검색 비용이 늘고 중복 검색 문제가 발생할 수 있다.

Q. 한국어 검색 결과가 안 나오면 어떻게 해?
A. 한글/영어 용어 병기, Header, FAQ, Retrieval Queries, Query Rewrite, 재Embedding 여부를 확인한다.

Q. 영어 Keyword로는 검색되는데 한국어 질문으로는 안 돼. 왜 그래?
A. 문서에 한국어 질문 표현이나 한글 설명이 부족해 Query와 Chunk의 의미 매칭이 약할 수 있다.

Q. 영어 기술 용어 검색이 안 되면 어떻게 해?
A. Header, FAQ, Metadata tags에 정확한 기술 용어를 포함하고 Keyword Search 또는 Hybrid Search를 적용한다.

Q. 클래스명이나 메서드명은 Semantic Search로 충분해?
A. 항상 충분하지 않다. 정확한 단어 매칭이 중요하므로 Keyword Search가 유리할 수 있다.

Q. Multilingual Golden Query는 뭐야?
A. 한국어 질문, 영어 기술 용어, 한국어+영어 혼합 Query를 포함한 Retrieval 평가 Query Set이다.

Q. BGE-M3 평가에서 무엇을 봐야 해?
A. 한국어 Query, 영어 Keyword Query, 혼합 Query가 Expected Document와 Section을 잘 찾는지 확인한다.

Q. Multilingual BGE-M3 Best Practice 핵심은 뭐야?
A. 한글 + 영어 용어 병기, 실제 한국어 FAQ, 영어 Keyword Header, Metadata tags, Golden Query 평가를 함께 적용하는 것이다.

Q. BGE-M3 기반 RAG 최적화는 어디서 시작해?
A. Model 변경보다 Chunk 구조, 한글/영어 용어 병기, FAQ, Retrieval Queries, Metadata 개선부터 시작한다.

Q. 한국어 검색 품질 개선 후 무엇을 해야 해?
A. 문서를 재Embedding하고 Multilingual Golden Query로 Hit Rate와 Ranking을 다시 평가한다.
