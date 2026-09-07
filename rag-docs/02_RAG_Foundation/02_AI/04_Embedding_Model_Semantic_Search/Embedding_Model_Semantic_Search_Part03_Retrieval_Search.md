# Embedding Model & Semantic Search Part03 Retrieval Search

---

# 1. Retrieval Core

## 1.1 RAG Retrieval

### [개념]

Retrieval은 User Query와 관련된 Document Chunk를 검색하는 과정이다.

RAG에서 Retrieval은 답변 생성 전 단계다.
Chat Model은 Retrieved Context를 기반으로 답변을 생성한다.

기본 Flow:

```text
User Query
→ Query Embedding
→ Vector Search
→ Top-K Retrieval
→ Filter / Rerank
→ Retrieved Context
→ Chat Model Answer
```

Retrieval 품질이 낮으면 Chat Model이 좋아도 Grounded Answer 품질이 낮아진다.

---

### [핵심]

- Retrieval은 RAG 답변의 근거 Chunk를 찾는 단계다.
- Query Embedding과 Document Embedding을 비교해 관련 Chunk를 찾는다.
- Retrieved Context가 Chat Model의 답변 근거가 된다.
- Retrieval 실패는 답변 실패로 이어질 수 있다.
- Retrieval 품질은 Chunk, Metadata, Query, Embedding Model, Top-K, Threshold에 의존한다.
- Retrieval 결과는 LLM 답변 전 검토되어야 한다.
- 검색 결과가 부족하면 Missing Information을 명시해야 한다.
- 검색 실패를 Chat Model 문제로만 판단하지 않는다.

---

### [실무]

2026 실무 기준 RAG Retrieval Pipeline:

```text
User Query
→ Query Rewrite
→ Query Embedding
→ Vector Search
→ Top-K Candidate Retrieval
→ Metadata Filter
→ Similarity Threshold
→ Reranking
→ Deduplication
→ Context Assembly
→ Grounded Answer
```

Retrieval 결과 점검 기준:

| 점검 항목 | 확인 내용                           |
| --------- | ----------------------------------- |
| Query     | 질문 의도가 명확한가                |
| Chunk     | 하나의 개념만 다루는가              |
| Metadata  | domain / level / section이 정확한가 |
| Top-K     | 필요한 문서가 포함되는가            |
| Threshold | 관련 없는 문서를 제거하는가         |
| Reranking | 최종 순서가 질문 의도와 맞는가      |
| Context   | 답변 생성에 충분한 근거인가         |

Retrieval 실패 분석 Flow:

```text
답변 오류 발생
→ Retrieved Chunks 확인
→ 기대 문서가 Top-K 안에 있는지 확인
→ Query 표현 확인
→ Chunk 제목과 FAQ 확인
→ Metadata 필터 확인
→ Threshold / Top-K 확인
→ Reranking 필요 여부 확인
```

---

### [주의]

- Vector DB를 연결했다고 Retrieval 품질이 자동으로 좋아지지 않는다.
- Top-K를 크게 하는 것만으로 검색 문제가 해결되지 않는다.
- Similarity Score가 높은 Chunk도 질문 의도와 다를 수 있다.
- Metadata Filter가 잘못되면 필요한 문서가 제외될 수 있다.
- Retrieved Context가 너무 많으면 관련 없는 정보가 섞인다.
- Retrieved Context가 너무 적으면 답변 근거가 부족하다.
- LLM이 Retrieval 실패를 일반 지식으로 덮어쓰지 않게 해야 한다.

---

### [FAQ]

Q. Retrieval이 뭐야?

A.
User Query와 관련된 Document Chunk를 검색해 Chat Model에 전달할 근거 Context를 만드는 과정이다.

Q. RAG에서 Retrieval이 왜 중요해?

A.
Chat Model은 Retrieved Context를 근거로 답변하므로 검색 품질이 낮으면 답변 품질도 낮아진다.

Q. Retrieval 실패는 Chat Model 문제야?

A.
항상 그렇지 않다. Chunk 구조, Query 표현, Metadata, Top-K, Threshold 문제가 원인일 수 있다.

Q. 검색 결과가 부족하면 어떻게 해야 해?

A.
문서에 근거가 부족하다고 명시하고 Query Rewrite, Chunk 개선, Metadata 보강을 검토한다.

---

# 2. Top-K Retrieval

## 2.1 Top-K

### [개념]

Top-K Retrieval은 User Query와 가장 유사한 상위 K개의 Chunk를 검색하는 방식이다.

Top-K는 검색 결과로 가져올 Chunk 개수다.

예시:

```text
Top-K = 5
→ Query와 가장 유사한 Chunk 5개 검색
```

Top-K는 Retrieval Recall, Precision, Context Budget에 영향을 준다.

---

### [핵심]

- Top-K는 검색 결과 Chunk 개수를 의미한다.
- Top-K가 작으면 필요한 문서가 누락될 수 있다.
- Top-K가 크면 관련 없는 문서가 섞일 수 있다.
- Top-K는 Context Window와 Token Budget을 함께 고려한다.
- Top-K는 Domain과 문서 구조에 따라 달라진다.
- 검색 품질이 낮으면 Top-K 조정보다 Chunk / Query 개선이 먼저일 수 있다.
- Top-K 결과는 필요 시 Reranking과 Deduplication을 거친다.
- Top-K는 Recall과 Precision의 균형 문제다.

---

### [실무]

Top-K 설정 기준:

| Top-K | 장점        | 단점                  | 적합                              |
| ----- | ----------- | --------------------- | --------------------------------- |
| 작음  | 정밀도 높음 | 필요한 문서 누락 가능 | FAQ, 단일 개념 검색               |
| 중간  | 균형 좋음   | 튜닝 필요             | 일반 RAG 문서                     |
| 큼    | 누락 감소   | 관련 없는 문서 증가   | 복합 질문, Reranking 전 후보 검색 |

실무 판단 Flow:

```text
단일 개념 질문인가?
→ Top-K 작게 시작

복합 질문인가?
→ Top-K 중간 이상 검토

기대 문서가 자주 누락되는가?
→ Top-K 증가 전 Query / Chunk 점검

관련 없는 Chunk가 많이 섞이는가?
→ Top-K 축소 또는 Threshold / Reranking 적용
```

예시:

```text
질문:
Chunk Size는 어떻게 정해?

Top-K 후보:
1. Chunk Size Strategy
2. Chunking Core
3. Chunk Overlap Strategy
4. Metadata
5. Reranking

판단:
1, 2번은 직접 관련
3번은 부분 관련
4, 5번은 낮은 관련
```

---

### [주의]

- Top-K를 무조건 크게 설정하지 않는다.
- 관련 없는 Chunk가 많으면 LLM 답변 품질이 낮아진다.
- 중복 Chunk가 Top-K를 차지하면 다양한 근거를 놓칠 수 있다.
- Top-K를 줄이면 필요한 문서가 누락될 수 있다.
- Chunk 품질이 낮으면 Top-K 튜닝 효과가 제한적이다.
- Top-K는 Threshold, Reranking, Metadata Filter와 함께 조정한다.

---

### [FAQ]

Q. Top-K는 뭐야?

A.
User Query와 유사한 상위 K개의 Chunk를 검색 결과로 가져오는 설정이다.

Q. Top-K는 몇 개가 좋아?

A.
고정 정답은 없다. 필요한 문서가 누락되지 않으면서 관련 없는 문서가 과도하게 섞이지 않도록 조정한다.

Q. Top-K를 크게 하면 검색 품질이 좋아져?

A.
항상 그렇지 않다. 관련 없는 Chunk가 많이 섞여 답변 품질이 낮아질 수 있다.

Q. 기대 문서가 검색되지 않으면 Top-K부터 늘리면 돼?

A.
먼저 Query 표현, Chunk 제목, Metadata, Embedding 생성 여부를 점검한 뒤 Top-K 조정을 검토한다.

---

# 3. Similarity Threshold

## 3.1 Threshold

### [개념]

Similarity Threshold는 유사도 점수가 낮은 검색 결과를 제외하는 기준이다.

Threshold는 검색된 Chunk 중 관련도가 낮은 결과를 제거해 RAG Context 품질을 높이는 데 사용한다.

기본 구조:

```text
Retrieved Chunk Score >= Threshold
→ Include

Retrieved Chunk Score < Threshold
→ Exclude
```

---

### [핵심]

- Similarity Threshold는 낮은 관련도 Chunk를 제외하는 기준이다.
- Threshold가 너무 높으면 필요한 문서가 누락된다.
- Threshold가 너무 낮으면 관련 없는 문서가 포함된다.
- Score 기준은 Embedding Model, Index, Normalization 방식에 따라 달라진다.
- Threshold는 고정값보다 평가 기반으로 조정하는 것이 좋다.
- 검색 결과가 없을 때 Fallback 규칙이 필요하다.
- Threshold는 Top-K, Metadata Filter, Reranking과 함께 조정한다.
- Threshold는 정답 판정 기준이 아니라 Context 품질 관리 기준이다.

---

### [실무]

Threshold 적용 Flow:

```text
Top-K Candidate Retrieval
→ Similarity Score 확인
→ Threshold 미만 제거
→ Metadata Filter 적용
→ Reranking
→ Final Context
```

Threshold 설정 시 확인할 것:

```text
Golden Query 검색 결과 확인
→ 기대 Chunk Score 분포 확인
→ 관련 없는 Chunk Score 분포 확인
→ 초기 Threshold 설정
→ 실패 사례 수집
→ Threshold 재조정
```

Fallback 예시:

```text
검색 결과 없음
→ Threshold 완화
→ Query Rewrite
→ Hybrid Search
→ Metadata Filter 완화
→ 그래도 없으면 Missing Information 명시
```

실무 판단 예시:

| 상황                       | 조치                |
| -------------------------- | ------------------- |
| 관련 문서가 자주 누락      | Threshold 낮춤 검토 |
| 관련 없는 문서가 많이 포함 | Threshold 높임 검토 |
| Score 분포가 불안정        | Golden Query 평가   |
| 문서별 Score 차이가 작음   | Reranking 검토      |
| 검색 결과 없음             | Fallback 적용       |

---

### [주의]

- Threshold를 절대 점수처럼 해석하지 않는다.
- Embedding Model이 바뀌면 Threshold 기준도 달라질 수 있다.
- Vector DB나 Similarity Metric이 바뀌면 Score 분포가 달라질 수 있다.
- 평가 없이 Threshold를 높이면 검색 결과가 사라질 수 있다.
- Threshold가 낮으면 Hallucination 위험 Context가 늘어날 수 있다.
- 검색 실패 시 사용자에게 정보 부족을 명시해야 한다.

---

### [FAQ]

Q. Similarity Threshold는 뭐야?

A.
유사도 점수가 낮은 검색 결과를 제외해 RAG Context 품질을 높이는 기준이다.

Q. Threshold를 높이면 좋은 거야?

A.
항상 그렇지 않다. 너무 높으면 필요한 문서가 검색 결과에서 제외될 수 있다.

Q. Threshold를 낮추면 좋은 거야?

A.
항상 그렇지 않다. 너무 낮으면 관련 없는 Chunk가 Context에 포함될 수 있다.

Q. Threshold 값은 고정하면 돼?

A.
권장하지 않는다. Embedding Model, 문서 구조, Score 분포, Golden Query 평가에 따라 조정해야 한다.

---

# 4. Similarity Metric

## 4.1 Cosine Similarity

### [개념]

Cosine Similarity는 두 Vector의 방향이 얼마나 비슷한지 측정하는 방식이다.

Embedding 기반 Semantic Search에서 자주 사용되는 Similarity Metric이다.

기본 의미:

```text
두 Vector의 방향이 비슷함
→ 의미적으로 유사할 가능성 높음
```

---

### [핵심]

- Cosine Similarity는 Vector 방향 유사도를 측정한다.
- Text 길이나 Vector 크기보다 방향 유사도에 집중한다.
- Semantic Search에서 자주 사용된다.
- Vector Normalization 여부에 따라 Score 해석이 달라질 수 있다.
- Score는 절대 정답 확률이 아니다.
- Cosine Similarity는 Ranking 기준으로 사용한다.
- 높은 Score라도 질문 의도와 맞는지 검토해야 한다.

---

### [실무]

Cosine Similarity 활용 Flow:

```text
Query Vector
+ Chunk Vector
→ Cosine Similarity 계산
→ Score 기반 Ranking
→ Top-K Candidate 선택
```

예시:

```text
Query:
Embedding Model과 Chat Model 차이는?

Chunk A:
Chat Model vs Embedding Model
Score: 0.88

Chunk B:
Chunk Overlap Strategy
Score: 0.52
```

판단:

```text
Chunk A:
질문 의도와 직접 관련

Chunk B:
Embedding 문서와 간접 관련 가능하지만 질문 핵심과는 거리 있음
```

실무 기준:

- Score만 보지 않고 제목과 Section 확인
- Metadata의 domain / level / section 확인
- Similarity Metric 변경 시 Score 분포 재평가
- Threshold는 Metric별로 별도 튜닝
- Golden Query로 기대 문서 Ranking 확인

---

### [주의]

- Cosine Similarity Score를 정답 확률로 해석하지 않는다.
- Score 기준은 Model과 Index 설정에 따라 달라질 수 있다.
- 같은 Score라도 Domain에 따라 의미가 다를 수 있다.
- Vector Normalization 방식이 바뀌면 Score 해석이 달라질 수 있다.
- 높은 Score라도 문서 최신성이나 Version이 낮을 수 있다.

---

### [FAQ]

Q. Cosine Similarity는 뭐야?

A.
두 Vector의 방향이 얼마나 비슷한지 측정해 의미 유사도를 계산하는 방식이다.

Q. Cosine Similarity가 높으면 무조건 정답 문서야?

A.
아니다. 질문 의도, Section, Metadata, Chunk 내용까지 함께 확인해야 한다.

Q. Cosine Similarity는 어디에 써?

A.
Query Vector와 Document Chunk Vector의 유사도를 계산해 검색 결과 Ranking에 사용한다.

Q. Similarity Metric이 바뀌면 Threshold도 바뀌어?

A.
그럴 수 있다. Metric에 따라 Score 분포가 달라지므로 Threshold를 다시 평가해야 한다.

---

## 4.2 Dot Product

### [개념]

Dot Product는 두 Vector의 곱을 합산해 유사도를 계산하는 방식이다.

Vector 방향과 크기가 모두 Score에 영향을 줄 수 있다.

기본 구조:

```text
Query Vector · Document Vector
→ Dot Product Score
```

---

### [핵심]

- Dot Product는 Vector 간 곱의 합으로 유사도를 계산한다.
- Vector 크기와 방향이 Score에 영향을 줄 수 있다.
- Normalized Vector에서는 Cosine Similarity와 유사하게 동작할 수 있다.
- Embedding Model과 Vector DB 설정에 따라 Dot Product를 사용할 수 있다.
- Score 해석은 Index 설정과 Normalization 여부에 의존한다.
- Dot Product Score도 정답 확률이 아니다.

---

### [실무]

Dot Product 사용 시 확인할 것:

```text
Embedding Model 출력 Vector가 Normalized 상태인가?
→ Vector DB Index Metric이 Dot Product인가?
→ Score 분포가 Golden Query에서 안정적인가?
→ Threshold 기준을 따로 설정했는가?
```

실무 판단:

| 조건                  | 확인                       |
| --------------------- | -------------------------- |
| Vector Normalized     | Cosine과 유사한 결과 가능  |
| Vector Not Normalized | Vector 크기 영향 확인 필요 |
| Threshold 사용        | Metric별 Score 분포 확인   |
| Model 변경            | 전체 Score 기준 재평가     |

---

### [주의]

- Dot Product와 Cosine Similarity Score를 같은 기준으로 비교하지 않는다.
- Normalization 여부를 확인하지 않고 Threshold를 설정하지 않는다.
- Dot Product Score가 높다고 항상 관련 Chunk는 아니다.
- Embedding Model 변경 시 Score 분포가 달라질 수 있다.
- Vector DB 설정과 Model 문서를 함께 확인해야 한다.

---

### [FAQ]

Q. Dot Product는 뭐야?

A.
두 Vector의 곱을 합산해 유사도를 계산하는 방식이다.

Q. Dot Product와 Cosine Similarity는 같아?

A.
같지 않다. 다만 Vector가 Normalized되어 있으면 유사하게 동작할 수 있다.

Q. Dot Product Score는 어떻게 해석해?

A.
Embedding Model, Vector Normalization, Vector DB Metric 설정에 따라 달라지므로 평가 기반으로 해석해야 한다.

---

## 4.3 Euclidean Distance

### [개념]

Euclidean Distance는 두 Vector 사이의 직선 거리를 계산하는 방식이다.

거리가 가까울수록 의미적으로 유사할 가능성이 높다.

기본 의미:

```text
Distance 작음
→ Vector가 가까움
→ 의미적으로 유사할 가능성 높음
```

---

### [핵심]

- Euclidean Distance는 Vector 간 거리를 측정한다.
- Similarity Score와 달리 값이 낮을수록 가까운 경우가 많다.
- Distance 기반 검색에서는 Ranking 방향을 주의해야 한다.
- Vector Scale과 Normalization이 결과에 영향을 줄 수 있다.
- Cosine Similarity와 Score 해석 방식이 다르다.
- Threshold 기준도 Distance Metric에 맞게 별도로 설정한다.

---

### [실무]

Euclidean Distance 검색 Flow:

```text
Query Vector
+ Document Vector
→ Distance 계산
→ Distance가 낮은 Chunk 우선 Ranking
→ Top-K 선택
```

실무 체크:

```text
Metric이 Similarity인지 Distance인지 확인
→ 높은 값이 좋은지 낮은 값이 좋은지 확인
→ Threshold 방향 확인
→ Golden Query로 Ranking 검증
```

예시:

| Metric             | 좋은 결과 방향     |
| ------------------ | ------------------ |
| Cosine Similarity  | 높을수록 유사      |
| Dot Product        | 보통 높을수록 유사 |
| Euclidean Distance | 낮을수록 가까움    |

---

### [주의]

- Distance 값이 낮을수록 좋은 Metric인지 확인한다.
- Similarity Threshold와 Distance Threshold를 혼동하지 않는다.
- Metric에 따라 Ranking 방향이 달라진다.
- Score UI가 Distance를 Similarity처럼 표시하는지 확인한다.
- Vector Scale이 Distance 결과에 영향을 줄 수 있다.

---

### [FAQ]

Q. Euclidean Distance는 뭐야?

A.
두 Vector 사이의 직선 거리를 계산하는 방식이다.

Q. Euclidean Distance는 높을수록 좋아?

A.
보통 아니다. Distance 기반에서는 값이 낮을수록 Vector가 가까운 경우가 많다.

Q. Similarity Metric과 Distance Metric은 뭐가 달라?

A.
Similarity는 높을수록 유사한 경우가 많고, Distance는 낮을수록 가까운 경우가 많다.

---

# 5. Keyword Search

## 5.1 Keyword Search

### [개념]

Keyword Search는 Query와 Document에 포함된 단어 일치를 기반으로 검색하는 방식이다.

기술 문서에서는 에러명, 클래스명, 메서드명, 설정 키, 파일명 검색에 강하다.

예시:

```text
NullPointerException
@Transactional
SecurityFilterChain
application.properties
```

---

### [핵심]

- Keyword Search는 정확한 단어 매칭에 강하다.
- 에러명, 클래스명, 메서드명 검색에 유리하다.
- 표현이 다르면 검색이 약할 수 있다.
- 의미가 비슷해도 단어가 다르면 검색되지 않을 수 있다.
- 기술 문서 RAG에서는 Keyword Search가 중요하다.
- Semantic Search와 결합하면 검색 품질을 보완할 수 있다.
- BM25는 대표적인 Keyword Search Ranking 방식이다.

---

### [실무]

Keyword Search에 적합한 Query:

```text
SecurityFilterChain 설정
NullPointerException 원인
findByUserIdAndStatus JPA
docker-compose.yml
BGE-M3
Top-K
```

Keyword Search에 약한 Query:

```text
검색이 잘 안 될 때 어떻게 해?
문서를 잘 나누는 방법 알려줘
질문이랑 문서를 의미로 비교하는 방식 뭐야?
```

실무 기준:

```text
정확한 기술 용어 / 에러명 / 클래스명
→ Keyword Search 유리

개념 질문 / 자연어 질문
→ Semantic Search 유리

정확한 용어 + 개념 설명
→ Hybrid Search 검토
```

---

### [주의]

- Keyword Search만 사용하면 표현이 다른 문서를 놓칠 수 있다.
- 한국어 설명과 영어 기술 용어가 섞인 문서에서는 용어 병기가 필요하다.
- 오타가 있으면 검색 실패 가능성이 높다.
- 동의어와 유사 표현 검색에는 약하다.
- Keyword Search 결과도 Ranking 검증이 필요하다.
- 모든 문서를 키워드 반복으로만 채우면 Chunk 품질이 낮아질 수 있다.

---

### [FAQ]

Q. Keyword Search는 뭐야?

A.
Query와 Document에 포함된 단어 일치를 기반으로 문서를 찾는 검색 방식이다.

Q. Keyword Search는 언제 좋아?

A.
에러명, 클래스명, 메서드명, 설정 키, 파일명처럼 정확한 용어를 찾을 때 좋다.

Q. Keyword Search만 쓰면 안 돼?

A.
개념 질문이나 표현이 다른 문서 검색에는 약하므로 Semantic Search와 함께 쓰는 것이 좋다.

Q. BM25는 뭐야?

A.
문서 내 단어 빈도와 중요도를 기반으로 검색 결과를 Ranking하는 대표적인 Keyword Search 방식이다.

---

# 6. Semantic Search

## 6.1 Semantic Search Strategy

### [개념]

Semantic Search는 Query와 Document의 의미 유사도를 기반으로 검색하는 방식이다.

단어가 정확히 일치하지 않아도 의미가 비슷하면 관련 Chunk를 찾을 수 있다.

기본 Flow:

```text
User Query
→ Query Embedding
→ Query Vector
→ Compare with Document Vectors
→ Similarity Ranking
→ Retrieved Chunks
```

---

### [핵심]

- Semantic Search는 의미 기반 검색이다.
- 자연어 질문에 강하다.
- 표현이 달라도 의미가 비슷하면 검색 가능하다.
- 정확한 키워드 검색은 Keyword Search보다 약할 수 있다.
- Embedding Model 품질에 영향을 받는다.
- Chunk 품질과 Header 품질이 중요하다.
- Similarity Score는 Ranking 기준이다.
- 기술 문서에서는 Keyword Search와 보완 관계다.

---

### [실무]

Semantic Search에 적합한 Query:

```text
RAG 검색 품질을 높이는 방법 알려줘
문서를 어떻게 나누면 검색이 잘 돼?
질문과 문서를 의미로 비교하는 방식이 뭐야?
```

검색 가능한 Chunk 예시:

```text
Chunking은 RAG 검색 품질의 핵심이다.
Chunk는 하나의 주제를 중심으로 구성해야 한다.
FAQ와 Retrieval Queries는 Query Matching을 강화한다.
```

실무 판단:

```text
사용자 질문이 자연어 중심
→ Semantic Search 우선

질문에 정확한 기술 용어 포함
→ Keyword Search 함께 고려

Semantic Search 결과가 넓게 퍼짐
→ Query Rewrite 또는 Metadata Filter 적용

Score는 높지만 관련 없음
→ Reranking 또는 Chunk 개선
```

---

### [주의]

- Semantic Search가 항상 정확한 것은 아니다.
- 의미가 비슷하지만 질문 의도와 다른 Chunk가 검색될 수 있다.
- 핵심 Keyword가 문서에 없으면 검색 품질이 낮아질 수 있다.
- 너무 큰 Chunk는 의미가 흐려질 수 있다.
- 너무 짧은 Query는 검색 의도가 약할 수 있다.
- Similarity Score를 정답 확률처럼 사용하지 않는다.

---

### [FAQ]

Q. Semantic Search는 뭐야?

A.
단어가 정확히 일치하지 않아도 의미가 비슷한 문서를 찾는 검색 방식이다.

Q. Semantic Search는 언제 좋아?

A.
개념 질문, 자연어 질문, 표현이 다른 문서 검색에 유리하다.

Q. Semantic Search만 쓰면 안 돼?

A.
기술 용어, 에러명, 클래스명처럼 정확한 단어 검색에는 약할 수 있어 Keyword Search와 함께 고려한다.

Q. Semantic Search 결과가 이상하면 어떻게 해?

A.
Query Rewrite, Chunk 제목 개선, Metadata Filter, Threshold, Reranking을 검토한다.

---

# 7. Hybrid Search

## 7.1 Hybrid Retrieval

### [개념]

Hybrid Search는 Keyword Search와 Semantic Search를 조합하는 검색 방식이다.

기술 문서 RAG에서는 정확한 용어 검색과 의미 기반 검색이 모두 필요하기 때문에 Hybrid Search가 유용하다.

기본 Flow:

```text
User Query
→ Keyword Search
→ Semantic Search
→ Score Fusion
→ Deduplication
→ Final Ranking
```

---

### [핵심]

- Hybrid Search는 Keyword Search와 Semantic Search를 결합한다.
- 정확한 기술 용어와 자연어 의미 검색을 함께 처리한다.
- 클래스명, 에러명, 메서드명 검색 품질을 보완한다.
- 개념 질문도 함께 처리할 수 있다.
- Score Fusion 기준이 필요하다.
- 중복 결과 제거가 필요하다.
- 시스템 복잡도와 Latency가 증가할 수 있다.
- Hybrid Search가 항상 필요한 것은 아니다.

---

### [실무]

Hybrid Search가 필요한 Query:

```text
SecurityFilterChain이 인증 필터에서 어떻게 동작해?
Chunk Size와 Top-K는 RAG 검색 품질에 어떤 영향을 줘?
BGE-M3로 한국어 RAG 검색할 때 Threshold는 어떻게 잡아?
```

분석:

```text
SecurityFilterChain
→ 정확한 Keyword Search 필요

인증 필터 동작
→ Semantic Search 필요

BGE-M3 / Threshold
→ Keyword + Semantic 둘 다 필요
```

Hybrid Search Pipeline:

```text
Keyword Candidate Retrieval
+ Semantic Candidate Retrieval
→ Candidate Merge
→ Duplicate Removal
→ Score Normalization
→ Score Fusion
→ Reranking
→ Final Context
```

Score Fusion 예시:

```text
Final Score
= Keyword Score Weight
+ Semantic Score Weight
+ Metadata Boost
```

Metadata Boost 예시:

```text
domain=AI
section=Retrieval
tags contains top-k
→ Boost
```

---

### [Comparison]

| 방식            | 장점                  | 단점                    | 적합                       |
| --------------- | --------------------- | ----------------------- | -------------------------- |
| Keyword Search  | 정확한 용어 검색 강함 | 표현 차이에 약함        | 에러명, 클래스명, 메서드명 |
| Semantic Search | 의미 기반 검색 강함   | 정확한 키워드 누락 가능 | 개념 질문, 자연어 질문     |
| Hybrid Search   | 두 방식 보완          | 구성 복잡도 증가        | 기술 문서 RAG              |

---

### [주의]

- Keyword Score와 Semantic Score를 단순 비교하지 않는다.
- Score Fusion 기준을 정의해야 한다.
- 중복 Chunk를 제거해야 한다.
- Hybrid Search는 Latency와 구현 복잡도를 증가시킬 수 있다.
- 문서 구조가 나쁘면 Hybrid Search도 한계가 있다.
- 정확한 용어는 문서 Header와 FAQ에 포함해야 한다.

---

### [FAQ]

Q. Hybrid Search는 뭐야?

A.
Keyword Search와 Semantic Search를 결합해 정확한 용어 검색과 의미 검색을 함께 수행하는 방식이다.

Q. Hybrid Search는 언제 필요해?

A.
에러명, 클래스명, 메서드명 같은 정확한 기술 용어와 개념 질문이 함께 필요한 경우 유용하다.

Q. Hybrid Search를 쓰면 항상 좋아?

A.
항상 그렇지 않다. 구현 복잡도와 Latency가 증가하므로 필요할 때 적용한다.

Q. Hybrid Search에서 중복 결과는 어떻게 해?

A.
Keyword Search와 Semantic Search 결과를 병합한 뒤 동일 Chunk를 Deduplication 처리한다.

---

# 8. Reranking

## 8.1 Reranker

### [개념]

Reranking은 1차 검색 결과를 다시 평가해 최종 순서를 재정렬하는 과정이다.

1차 검색은 후보 Chunk를 넓게 가져오고, Reranker는 Query와 Chunk의 관련성을 더 정밀하게 판단한다.

기본 Flow:

```text
Initial Retrieval
→ Candidate Chunks
→ Reranker
→ Reordered Results
→ Final Context Selection
```

---

### [핵심]

- Reranking은 검색 결과 순서를 개선하는 후처리다.
- 1차 Retrieval은 후보를 넓게 가져온다.
- Reranker는 후보 Chunk를 더 정밀하게 평가한다.
- 관련 없는 Chunk를 뒤로 밀 수 있다.
- 중요한 Chunk를 상위로 올릴 수 있다.
- 검색 품질 개선에 효과적일 수 있다.
- 비용과 Latency가 증가할 수 있다.
- Chunk 구조 문제를 완전히 해결하지는 못한다.

---

### [실무]

Reranking이 필요한 상황:

| 상황                                       | 이유                           |
| ------------------------------------------ | ------------------------------ |
| Top-K 안에 정답 Chunk는 있지만 순위가 낮음 | 최종 Context에서 누락 가능     |
| 관련 없는 Chunk가 상위에 있음              | 답변 품질 저하                 |
| Semantic Search 결과가 넓게 퍼짐           | 정밀 정렬 필요                 |
| Hybrid Search 결과 병합 후 순위 불안정     | 최종 Ranking 필요              |
| 복합 질문                                  | 여러 관점의 관련성 재평가 필요 |

Reranking Pipeline:

```text
Top-K = 20 Candidate Retrieval
→ Reranker 평가
→ Top-N = 5 Final Context 선택
→ Chat Model 답변
```

실무 기준:

```text
검색 후보 누락이 문제
→ Top-K / Query / Chunk 개선

후보는 있는데 순서가 문제
→ Reranking 적용

최종 Context가 중복됨
→ Deduplication 추가

Reranking 후에도 틀림
→ Chunk 내용 / Prompt Grounding 점검
```

---

### [주의]

- Reranker를 사용하면 응답 시간이 늘어날 수 있다.
- 후보 Chunk 수가 많으면 비용이 증가한다.
- Reranking은 누락된 문서를 새로 만들어내지 못한다.
- 1차 Retrieval에서 기대 문서가 후보에 없으면 Reranking이 해결할 수 없다.
- Reranking이 잘못된 Chunk 구조를 완전히 보정하지는 못한다.
- 최종 Context 선택 기준을 명확히 해야 한다.

---

### [FAQ]

Q. Reranking은 뭐야?

A.
1차 검색 결과를 다시 평가해 질문과 더 관련 있는 Chunk가 위로 오도록 재정렬하는 과정이다.

Q. Reranking은 언제 필요해?

A.
정답 Chunk가 검색되지만 순위가 낮거나 관련 없는 Chunk가 상위에 섞일 때 필요하다.

Q. Reranking을 쓰면 검색 누락이 해결돼?

A.
아니다. 1차 Retrieval 후보에 없는 문서는 Reranking으로 복구할 수 없다.

Q. Reranking의 단점은 뭐야?

A.
추가 모델 또는 계산이 필요해 Latency와 비용이 증가할 수 있다.

---

# 9. Deduplication

## 9.1 Duplicate Result Removal

### [개념]

Deduplication은 검색 결과에서 중복되거나 거의 같은 Chunk를 제거하는 과정이다.

Chunk Overlap, 반복 FAQ, 유사한 Retrieval Queries가 많으면 중복 결과가 Top-K를 차지할 수 있다.

---

### [핵심]

- Deduplication은 중복 Chunk를 제거한다.
- Top-K 결과 다양성을 높인다.
- 중복 Context로 인한 Token 낭비를 줄인다.
- 같은 문서의 유사 Chunk가 반복 검색되는 문제를 완화한다.
- Chunk Overlap이 클수록 Deduplication이 중요해진다.
- Hybrid Search 결과 병합 시 Deduplication이 필요하다.
- 중복 제거 기준은 fileName, section, chunkId, text similarity 등을 사용할 수 있다.

---

### [실무]

Deduplication 기준:

| 기준               | 설명                                   |
| ------------------ | -------------------------------------- |
| chunkId            | 완전히 동일한 Chunk 제거               |
| fileName + section | 같은 Section 중복 결과 제한            |
| Text Similarity    | 거의 같은 내용 제거                    |
| Metadata           | domain / part / section 기준 중복 조정 |
| Score              | 중복 후보 중 높은 Score만 유지         |

Deduplication Flow:

```text
Top-K Retrieved Chunks
→ Same chunkId 제거
→ Same section 과다 포함 제거
→ Text Similarity 기반 유사 Chunk 제거
→ Score 높은 Chunk 유지
→ Final Context 구성
```

중복 문제 예시:

```text
Top-K 결과:
1. Chunk Size FAQ
2. Chunk Size Retrieval Query
3. Chunk Size 설명
4. Chunk Size 중복 설명
5. Chunk Overlap 설명

문제:
Chunk Size 중복이 많아 Chunk Overlap 근거가 밀릴 수 있음
```

---

### [주의]

- Deduplication을 과하게 적용하면 필요한 관련 문서가 제거될 수 있다.
- 같은 Section에서도 서로 다른 세부 근거가 있을 수 있다.
- 중복 제거 전에 Score와 Section 의미를 확인한다.
- Retrieval Queries와 본문 Chunk가 둘 다 필요한 경우도 있다.
- Deduplication은 Chunk 구조 개선을 대체하지 않는다.

---

### [FAQ]

Q. Deduplication은 뭐야?

A.
검색 결과에서 중복되거나 거의 같은 Chunk를 제거해 Context 다양성을 높이는 과정이다.

Q. 중복 Chunk가 왜 문제야?

A.
Top-K를 중복 Chunk가 차지하면 다른 중요한 근거가 검색 결과에서 밀릴 수 있다.

Q. Deduplication은 언제 필요해?

A.
Chunk Overlap이 크거나 Hybrid Search 결과를 병합하거나 비슷한 FAQ가 반복 검색될 때 필요하다.

Q. 중복 제거를 강하게 하면 좋아?

A.
항상 그렇지 않다. 필요한 관련 근거까지 제거할 수 있으므로 기준을 조정해야 한다.

---

# 10. Context Assembly

## 10.1 Retrieved Context Assembly

### [개념]

Context Assembly는 검색된 Chunk를 Chat Model이 사용할 Prompt Context로 구성하는 과정이다.

Retrieval 결과를 그대로 모두 넣는 것이 아니라, 질문 의도와 Context Budget에 맞게 정리해야 한다.

기본 Flow:

```text
Retrieved Chunks
→ Filter
→ Rerank
→ Deduplicate
→ Order
→ Prompt Context
```

---

### [핵심]

- Context Assembly는 Retrieved Chunks를 답변용 Context로 구성한다.
- 관련도 높은 Chunk를 우선 배치한다.
- 중복 Chunk를 줄인다.
- 서로 충돌하는 Chunk는 Version과 우선순위를 확인한다.
- Context Budget을 초과하지 않게 조정한다.
- 문서 출처와 Section 정보를 유지한다.
- Chat Model이 근거를 잃지 않도록 Chunk를 과도하게 요약하지 않는다.
- Context Assembly는 답변 품질에 직접 영향을 준다.

---

### [실무]

Context Assembly 기준:

```text
1. 질문 의도와 직접 관련된 Chunk 우선
2. 최신 Version 우선
3. Foundation / Expert Level 우선순위 확인
4. 중복 Chunk 제거
5. Code Block과 설명 유지
6. Metadata 유지
7. Context Budget 초과 시 낮은 관련도 Chunk 제외
```

Prompt Context 예시:

```text
[Source]
fileName: Embedding_Model_Semantic_Search_Part03_Retrieval_Search.md
section: Top-K Retrieval

[Content]
Top-K Retrieval은 User Query와 가장 유사한 상위 K개의 Chunk를 검색하는 방식이다.
Top-K가 작으면 필요한 문서가 누락될 수 있고, 크면 관련 없는 문서가 섞일 수 있다.
```

충돌 Context 처리:

```text
Chunk A:
Top-K는 5를 기본값으로 사용

Chunk B:
Top-K는 문서 구조와 Context Window에 따라 조정

처리:
고정값보다 평가 기반 조정을 우선한다.
```

---

### [주의]

- Retrieved Chunks를 무조건 전부 Prompt에 넣지 않는다.
- Metadata를 제거하면 출처와 우선순위 판단이 어려워진다.
- Chunk를 과도하게 요약하면 근거가 손실될 수 있다.
- 관련 없는 Context가 포함되면 Hallucination 가능성이 높아진다.
- 충돌하는 Context가 있으면 Version과 Domain 우선순위를 확인한다.
- Code Block은 설명과 함께 유지한다.

---

### [FAQ]

Q. Context Assembly는 뭐야?

A.
검색된 Chunk를 Chat Model이 답변 근거로 사용할 수 있도록 정리해 Prompt Context로 구성하는 과정이다.

Q. 검색된 Chunk를 전부 넣으면 안 돼?

A.
관련 없는 정보와 중복이 섞이면 답변 품질이 낮아질 수 있으므로 선별해야 한다.

Q. Context Budget은 뭐야?

A.
Chat Model에 전달할 수 있는 Prompt Context의 Token 한계다.

Q. 충돌하는 문서가 검색되면 어떻게 해?

A.
Version, domain, level, section 우선순위를 확인하고 최신 또는 더 적합한 문서를 근거로 사용한다.

---

# 11. Search Strategy by Query Type

## 11.1 Query Type Routing

### [개념]

Query Type Routing은 사용자 질문 유형에 따라 검색 전략을 다르게 선택하는 방식이다.

모든 Query에 같은 Retrieval 전략을 적용하면 검색 품질이 떨어질 수 있다.

---

### [핵심]

- Query 유형에 따라 검색 전략을 다르게 적용한다.
- 자연어 개념 질문은 Semantic Search가 유리하다.
- 에러명, 클래스명, 메서드명은 Keyword Search가 유리하다.
- 복합 질문은 Hybrid Search와 Reranking이 유리할 수 있다.
- 질문이 모호하면 Query Rewrite가 필요하다.
- Domain이 명확하면 Metadata Filter를 적용할 수 있다.
- 검색 결과가 중복되면 Deduplication을 적용한다.

---

### [실무]

Query Type별 전략:

| Query Type  | 예시                     | 추천 전략                   |
| ----------- | ------------------------ | --------------------------- |
| 개념 질문   | Embedding이 뭐야?        | Semantic Search             |
| 정확한 용어 | BGE-M3, Top-K            | Keyword + Semantic          |
| 에러명      | NullPointerException     | Keyword Search              |
| 클래스명    | SecurityFilterChain      | Keyword Search              |
| 방법 질문   | 검색 품질 어떻게 개선해? | Semantic Search + Reranking |
| 복합 질문   | Chunk Size와 Top-K 관계  | Hybrid Search               |
| 모호한 질문 | 검색이 이상해            | Query Rewrite + Semantic    |
| 도메인 지정 | AI RAG 검색 기준         | Metadata Filter + Semantic  |

Routing Flow:

```text
User Query 분석
→ Domain Keyword 존재 여부 확인
→ 정확한 기술 용어 존재 여부 확인
→ 자연어 개념 질문 여부 확인
→ Query Rewrite 필요 여부 확인
→ Search Strategy 선택
→ Retrieval 실행
```

---

### [주의]

- 모든 질문을 Semantic Search만으로 처리하지 않는다.
- 모든 질문을 Keyword Search만으로 처리하지 않는다.
- Query Rewrite가 원래 의도를 바꾸지 않게 한다.
- Metadata Filter를 너무 강하게 적용하지 않는다.
- 복합 질문은 단일 검색으로 부족할 수 있다.
- Query Type Routing 결과는 Golden Query로 검증한다.

---

### [FAQ]

Q. Query Type Routing은 뭐야?

A.
사용자 질문 유형에 따라 Semantic Search, Keyword Search, Hybrid Search, Reranking 전략을 선택하는 방식이다.

Q. 자연어 질문에는 어떤 검색이 좋아?

A.
개념 설명이나 방법 질문은 Semantic Search가 유리하다.

Q. 에러명이나 클래스명 검색은 어떤 방식이 좋아?

A.
정확한 단어 매칭이 중요하므로 Keyword Search가 유리하다.

Q. 복합 질문은 어떻게 검색해?

A.
Hybrid Search로 후보를 넓게 찾고 Reranking으로 최종 관련도를 정렬하는 방식이 유용하다.

---

# 12. Retrieval Troubleshooting

## 12.1 Search Failure Troubleshooting

### [개념]

Retrieval Troubleshooting은 검색 실패 원인을 Query, Chunk, Metadata, Search Strategy, Threshold, Reranking 관점에서 분석하는 과정이다.

검색 실패는 단일 원인보다 여러 원인이 겹쳐 발생하는 경우가 많다.

---

### [Troubleshooting]

문제:

- 관련 문서가 검색되지 않음

원인:

- Query가 너무 짧거나 모호함
- Query와 문서 표현 불일치
- Chunk 제목이 불명확함
- 핵심 Keyword 누락
- Metadata Filter가 너무 강함
- Threshold가 너무 높음
- Embedding 미생성 또는 오래됨

해결:

- Query Rewrite 적용
- FAQ / Retrieval Queries 추가
- 핵심 용어 한글 + 영어 병기
- Chunk 제목 개선
- Metadata Filter 완화
- Threshold 완화
- 문서 재Embedding

문제:

- 관련 없는 문서가 검색됨

원인:

- Top-K가 너무 큼
- Threshold가 너무 낮음
- Chunk에 여러 개념 혼합
- Query가 너무 넓음
- Metadata Filter 없음
- Reranking 없음

해결:

- Top-K 축소
- Threshold 조정
- Chunk 주제 분리
- Query 구체화
- Metadata Filter 적용
- Reranking 적용

문제:

- 정답 Chunk가 낮은 순위에 있음

원인:

- Semantic Search Ranking 한계
- Keyword와 의미 검색 결과가 섞임
- Score Fusion 기준 부재
- Chunk 제목이 약함
- Reranking 없음

해결:

- Reranking 적용
- Header Keyword 개선
- Hybrid Search Score Fusion 조정
- Metadata Boost 적용
- Golden Query로 Ranking 검증

문제:

- 검색 결과가 중복됨

원인:

- Chunk Overlap 과다
- 동일 FAQ 반복
- Retrieval Queries 중복
- Hybrid Search 결과 병합 후 Deduplication 없음

해결:

- Deduplication 적용
- Overlap 축소
- 중복 FAQ 제거
- Retrieval Queries 차별화
- section 기준 중복 제한

문제:

- 검색은 됐지만 답변이 틀림

원인:

- Context Assembly 실패
- 관련 없는 Chunk 포함
- 필요한 Chunk 누락
- Prompt Grounding 부족
- 충돌 문서 포함

해결:

- Final Context 검수
- Reranking 적용
- Context 순서 조정
- 문서 우선순위 규칙 적용
- Grounding Prompt 강화

---

### [FAQ]

Q. 검색 결과가 안 나오면 어떻게 해?

A.
Query 표현, Chunk 제목, Metadata Filter, Threshold, Embedding 재생성 여부를 먼저 확인한다.

Q. 관련 없는 문서가 검색되면 어떻게 해?

A.
Top-K를 조정하고 Threshold, Metadata Filter, Reranking, Chunk 분리를 검토한다.

Q. 정답 Chunk가 낮은 순위에 있으면 어떻게 해?

A.
Reranking을 적용하고 Header Keyword, Metadata Boost, Hybrid Search Score Fusion을 개선한다.

Q. 검색은 됐는데 답변이 틀리면 어떻게 해?

A.
Context Assembly, Prompt Grounding, 충돌 문서, 필요한 Chunk 누락 여부를 점검한다.

---

# 13. Best Practice

## 13.1 Retrieval Search Best Practice

### [Best Practice]

Retrieval Best Practice:

- User Query를 그대로 검색하기 전에 Query Intent를 확인
- 짧고 모호한 Query는 Query Rewrite 적용
- 기술 용어는 Keyword Search와 Semantic Search를 함께 고려
- 자연어 질문은 Semantic Search 우선 적용
- 복합 질문은 Hybrid Search와 Reranking 검토
- Top-K는 Context Budget과 함께 조정
- Threshold는 Golden Query 평가 기반으로 조정
- Metadata Filter는 domain / level / section 기준으로 적용
- 중복 Chunk는 Deduplication 처리
- Retrieved Context는 답변 전 검토
- 검색 결과 부족 시 Missing Information 명시
- 검색 실패 사례를 문서 개선에 반영

---

### [Checklist]

- [ ] Query Type을 분류했는가?
- [ ] Query Rewrite가 필요한지 확인했는가?
- [ ] 정확한 기술 용어는 Keyword Search로 보완했는가?
- [ ] 자연어 개념 질문은 Semantic Search로 처리했는가?
- [ ] 복합 질문은 Hybrid Search를 검토했는가?
- [ ] Top-K가 너무 작거나 크지 않은가?
- [ ] Threshold가 Score 분포에 맞는가?
- [ ] Metadata Filter가 과도하지 않은가?
- [ ] Reranking 필요 여부를 확인했는가?
- [ ] 중복 Chunk를 제거했는가?
- [ ] Context Assembly에서 출처와 Section을 유지했는가?
- [ ] 검색 결과 부족 시 Fallback 규칙이 있는가?
- [ ] Golden Query로 Retrieval 품질을 검증했는가?

---

### [FAQ]

Q. Retrieval Search Best Practice 핵심은 뭐야?

A.
Query 유형에 맞는 검색 전략을 선택하고 Top-K, Threshold, Metadata Filter, Reranking을 평가 기반으로 조정하는 것이다.

Q. 검색 품질 튜닝은 어디서 시작해?

A.
Query, Chunk 제목, FAQ, Metadata, Top-K, Threshold, Reranking 순서로 점검한다.

Q. Hybrid Search와 Reranking은 항상 써야 해?

A.
아니다. 검색 품질, Latency, 복잡도를 고려해 필요한 경우 적용한다.

Q. Retrieval 품질은 어떻게 검증해?

A.
Golden Query와 Expected Document를 정하고 기대 Chunk가 Top-K 안에 들어오는지 평가한다.

---

# Retrieval Queries

### [FAQ]

Q. Retrieval이 뭐야?
A. User Query와 관련된 Document Chunk를 검색해 Chat Model에 전달할 근거 Context를 만드는 과정이다.

Q. RAG에서 Retrieval이 왜 중요해?
A. Chat Model은 Retrieved Context를 근거로 답변하므로 검색 품질이 낮으면 답변 품질도 낮아진다.

Q. Top-K는 뭐야?
A. User Query와 유사한 상위 K개의 Chunk를 검색 결과로 가져오는 설정이다.

Q. Top-K는 몇 개가 좋아?
A. 고정 정답은 없다. 필요한 문서가 누락되지 않으면서 관련 없는 문서가 과도하게 섞이지 않도록 조정한다.

Q. Top-K를 크게 하면 검색 품질이 좋아져?
A. 항상 그렇지 않다. 관련 없는 Chunk가 많이 섞여 답변 품질이 낮아질 수 있다.

Q. Similarity Threshold는 뭐야?
A. 유사도 점수가 낮은 검색 결과를 제외해 RAG Context 품질을 높이는 기준이다.

Q. Threshold를 높이면 좋은 거야?
A. 항상 그렇지 않다. 너무 높으면 필요한 문서가 검색 결과에서 제외될 수 있다.

Q. Threshold 값은 고정하면 돼?
A. 권장하지 않는다. Embedding Model, 문서 구조, Score 분포, Golden Query 평가에 따라 조정해야 한다.

Q. Cosine Similarity는 뭐야?
A. 두 Vector의 방향이 얼마나 비슷한지 측정해 의미 유사도를 계산하는 방식이다.

Q. Dot Product는 뭐야?
A. 두 Vector의 곱을 합산해 유사도를 계산하는 방식이다.

Q. Euclidean Distance는 뭐야?
A. 두 Vector 사이의 직선 거리를 계산하는 방식이다.

Q. Similarity Metric이 바뀌면 Threshold도 바뀌어?
A. 그럴 수 있다. Metric에 따라 Score 분포가 달라지므로 Threshold를 다시 평가해야 한다.

Q. Keyword Search는 뭐야?
A. Query와 Document에 포함된 단어 일치를 기반으로 문서를 찾는 검색 방식이다.

Q. Keyword Search는 언제 좋아?
A. 에러명, 클래스명, 메서드명, 설정 키, 파일명처럼 정확한 용어를 찾을 때 좋다.

Q. Semantic Search는 뭐야?
A. 단어가 정확히 일치하지 않아도 의미가 비슷한 문서를 찾는 검색 방식이다.

Q. Semantic Search는 언제 좋아?
A. 개념 질문, 자연어 질문, 표현이 다른 문서 검색에 유리하다.

Q. Hybrid Search는 뭐야?
A. Keyword Search와 Semantic Search를 결합해 정확한 용어 검색과 의미 검색을 함께 수행하는 방식이다.

Q. Hybrid Search는 언제 필요해?
A. 에러명, 클래스명, 메서드명 같은 정확한 기술 용어와 개념 질문이 함께 필요한 경우 유용하다.

Q. Reranking은 뭐야?
A. 1차 검색 결과를 다시 평가해 질문과 더 관련 있는 Chunk가 위로 오도록 재정렬하는 과정이다.

Q. Reranking은 언제 필요해?
A. 정답 Chunk가 검색되지만 순위가 낮거나 관련 없는 Chunk가 상위에 섞일 때 필요하다.

Q. Reranking을 쓰면 검색 누락이 해결돼?
A. 아니다. 1차 Retrieval 후보에 없는 문서는 Reranking으로 복구할 수 없다.

Q. Deduplication은 뭐야?
A. 검색 결과에서 중복되거나 거의 같은 Chunk를 제거해 Context 다양성을 높이는 과정이다.

Q. 중복 Chunk가 왜 문제야?
A. Top-K를 중복 Chunk가 차지하면 다른 중요한 근거가 검색 결과에서 밀릴 수 있다.

Q. Context Assembly는 뭐야?
A. 검색된 Chunk를 Chat Model이 답변 근거로 사용할 수 있도록 정리해 Prompt Context로 구성하는 과정이다.

Q. 검색된 Chunk를 전부 넣으면 안 돼?
A. 관련 없는 정보와 중복이 섞이면 답변 품질이 낮아질 수 있으므로 선별해야 한다.

Q. Query Type Routing은 뭐야?
A. 사용자 질문 유형에 따라 Semantic Search, Keyword Search, Hybrid Search, Reranking 전략을 선택하는 방식이다.

Q. 자연어 질문에는 어떤 검색이 좋아?
A. 개념 설명이나 방법 질문은 Semantic Search가 유리하다.

Q. 에러명이나 클래스명 검색은 어떤 방식이 좋아?
A. 정확한 단어 매칭이 중요하므로 Keyword Search가 유리하다.

Q. 검색 결과가 안 나오면 어떻게 해?
A. Query 표현, Chunk 제목, Metadata Filter, Threshold, Embedding 재생성 여부를 먼저 확인한다.

Q. 관련 없는 문서가 검색되면 어떻게 해?
A. Top-K를 조정하고 Threshold, Metadata Filter, Reranking, Chunk 분리를 검토한다.

Q. 정답 Chunk가 낮은 순위에 있으면 어떻게 해?
A. Reranking을 적용하고 Header Keyword, Metadata Boost, Hybrid Search Score Fusion을 개선한다.

Q. Retrieval 품질은 어떻게 검증해?
A. Golden Query와 Expected Document를 정하고 기대 Chunk가 Top-K 안에 들어오는지 평가한다.
