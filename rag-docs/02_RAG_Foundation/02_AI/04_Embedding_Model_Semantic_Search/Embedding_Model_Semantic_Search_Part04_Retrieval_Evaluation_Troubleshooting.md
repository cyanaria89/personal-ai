# Embedding Model & Semantic Search Part04 Retrieval Evaluation Troubleshooting

---

# 1. Retrieval Evaluation Core

## 1.1 Retrieval Evaluation

### [개념]

Retrieval Evaluation은 RAG 검색 품질을 측정하고 개선하기 위한 평가 과정이다.

RAG 답변 품질은 Retrieval 품질에 크게 의존한다.
검색된 Chunk가 질문과 맞지 않으면 Chat Model이 좋아도 Grounded Answer 품질이 낮아진다.

기본 Flow:

```text
Test Queries
→ Retrieve Documents
→ Compare Expected Documents
→ Analyze Failure Case
→ Improve Query / Chunk / Metadata / Search Strategy
```

Retrieval Evaluation의 목적:

- 관련 문서가 Top-K 안에 들어오는지 확인
- 검색 결과 순위가 질문 의도와 맞는지 확인
- 관련 없는 Chunk가 섞이는 원인 분석
- Chunking / Metadata / Query 개선 지점 발견
- RAG 문서 품질을 반복 개선

---

### [핵심]

- Retrieval Evaluation은 검색 품질 평가다.
- 답변 품질 평가와 Retrieval 품질 평가는 구분한다.
- Expected Document가 Top-K 안에 있는지 확인한다.
- Golden Query를 기준으로 반복 평가한다.
- 검색 실패 사례를 문서 개선에 반영한다.
- Chunk 품질, Metadata, Query 표현, Top-K, Threshold를 함께 평가한다.
- Retrieval 성공이 답변 성공을 보장하지는 않는다.
- Retrieval 실패는 Generation 단계에서 해결하기 어렵다.

---

### [실무]

2026 실무 기준 Retrieval Evaluation Pipeline:

```text
Golden Query Set 작성
→ Expected Document / Expected Section 정의
→ Top-K Retrieval 실행
→ Hit 여부 확인
→ Ranking 위치 확인
→ 관련 없는 Chunk 분석
→ Failure Case 기록
→ 문서 / Query / Metadata 개선
→ 재Embedding
→ 재평가
```

평가 대상:

| 평가 대상         | 확인 내용                           |
| ----------------- | ----------------------------------- |
| Query             | 실제 사용자가 물어볼 표현인가       |
| Expected Document | 정답 근거 문서가 명확한가           |
| Top-K             | 기대 Chunk가 포함되는가             |
| Ranking           | 기대 Chunk가 상위에 있는가          |
| Metadata          | domain / level / section이 정확한가 |
| Chunk             | 하나의 개념만 다루는가              |
| Threshold         | 필요한 Chunk를 제거하지 않는가      |
| Reranking         | 최종 순위가 개선되는가              |

검색 품질 개선 순서:

```text
1. Golden Query 정의
2. Expected Chunk 정의
3. 검색 결과 확인
4. 실패 원인 분류
5. Chunk 제목 / FAQ / Retrieval Queries 개선
6. Metadata 보강
7. Query Rewrite 적용
8. Top-K / Threshold 조정
9. Hybrid Search / Reranking 검토
10. 재Embedding 후 재평가
```

---

### [주의]

- 한두 개 Query만으로 전체 Retrieval 품질을 판단하지 않는다.
- Golden Query가 실제 사용자 질문과 다르면 평가 의미가 낮다.
- Expected Document가 불명확하면 평가 결과도 불명확하다.
- Retrieval Hit만 보고 답변 품질을 단정하지 않는다.
- 높은 Similarity Score가 항상 좋은 Retrieval은 아니다.
- 문서 수정 후 재Embedding 없이 평가하면 결과가 반영되지 않는다.
- Top-K를 늘리는 것만으로 품질 개선을 판단하지 않는다.

---

### [FAQ]

Q. Retrieval Evaluation은 뭐야?

A.
RAG 검색 결과가 사용자 질문에 맞는 문서를 잘 찾는지 평가하는 과정이다.

Q. Retrieval Evaluation은 왜 필요해?

A.
검색이 실패하면 Chat Model이 근거 있는 답변을 만들기 어렵기 때문이다.

Q. Retrieval 성공과 답변 성공은 같아?

A.
아니다. 검색이 성공해도 Prompt Grounding이나 Context Assembly가 나쁘면 답변이 틀릴 수 있다.

Q. Retrieval 품질은 어떻게 개선해?

A.
Golden Query로 실패 사례를 찾고 Chunk, Metadata, FAQ, Query Rewrite, Top-K, Reranking을 개선한다.

---

# 2. Golden Query

## 2.1 Golden Query Set

### [개념]

Golden Query는 Retrieval 품질을 평가하기 위해 미리 정의한 대표 사용자 질문이다.

Golden Query는 실제 사용자가 물어볼 가능성이 높은 질문이어야 한다.
각 Golden Query에는 Expected Document 또는 Expected Section을 연결한다.

예시:

```text
Golden Query:
Chunk Size는 어떻게 정해?

Expected Document:
Embedding_Model_Semantic_Search_Part02_Chunking_Metadata.md

Expected Section:
Chunk Size Strategy
```

---

### [핵심]

- Golden Query는 검색 품질 평가 기준 질문이다.
- 실제 사용자 질문 형태로 작성한다.
- 각 Query마다 Expected Document를 지정한다.
- Expected Section까지 지정하면 평가 정확도가 높아진다.
- 한국어 질문과 영어 기술 용어를 함께 포함한다.
- Golden Query는 문서 개선 후 재평가에 사용한다.
- Domain별로 Golden Query Set을 분리한다.
- Golden Query는 계속 업데이트한다.

---

### [실무]

Golden Query 작성 기준:

```text
실제 사용자 질문
+ 핵심 Domain Keyword
+ 문서에서 기대하는 답변 위치
+ Expected Document
+ Expected Section
```

Golden Query 예시:

| Golden Query                         | Expected Document                           | Expected Section               |
| ------------------------------------ | ------------------------------------------- | ------------------------------ |
| Embedding이 뭐야?                    | Part01_Core                                 | Embedding Core                 |
| Chat Model과 Embedding Model 차이는? | Part01_Core                                 | Chat Model vs Embedding Model  |
| Chunk Size는 어떻게 정해?            | Part02_Chunking_Metadata                    | Chunk Size Strategy            |
| Metadata는 왜 필요해?                | Part02_Chunking_Metadata                    | Metadata                       |
| Top-K는 몇 개가 좋아?                | Part03_Retrieval_Search                     | Top-K                          |
| Threshold는 어떻게 잡아?             | Part03_Retrieval_Search                     | Similarity Threshold           |
| Reranking은 언제 필요해?             | Part03_Retrieval_Search                     | Reranker                       |
| 검색 결과가 안 나오면 어떻게 해?     | Part04_Retrieval_Evaluation_Troubleshooting | Search Failure Troubleshooting |

Golden Query Template:

```md
### [Golden Query]

Query:
검색 결과가 안 나올 때 어떻게 해?

Expected Document:
Embedding_Model_Semantic_Search_Part04_Retrieval_Evaluation_Troubleshooting.md

Expected Section:
Search Failure Troubleshooting

Expected Answer:
Query 표현, Chunk 제목, Metadata, Threshold, Embedding 재생성 여부를 점검한다.
```

---

### [주의]

- Golden Query를 문서 제목과만 동일하게 만들지 않는다.
- 실제 사용자 표현을 반영한다.
- 너무 쉬운 Query만 넣지 않는다.
- 모호한 Query도 포함해 Query Rewrite 필요성을 평가한다.
- Expected Document가 여러 개인 경우 우선순위를 지정한다.
- 문서가 추가되면 Golden Query도 갱신한다.

---

### [FAQ]

Q. Golden Query는 뭐야?

A.
Retrieval 품질을 평가하기 위해 미리 정의한 대표 사용자 질문이다.

Q. Golden Query에는 무엇을 연결해야 해?

A.
Expected Document, Expected Section, 기대 답변 기준을 연결하는 것이 좋다.

Q. Golden Query는 실제 질문처럼 써야 해?

A.
그렇다. 실제 사용자 Query와 다르면 평가 결과의 의미가 낮아진다.

Q. Golden Query는 한 번 만들면 끝이야?

A.
아니다. 문서가 추가되거나 실패 사례가 발견되면 계속 업데이트해야 한다.

---

# 3. Retrieval Metrics

## 3.1 Retrieval Hit Rate

### [개념]

Retrieval Hit Rate는 Expected Document 또는 Expected Chunk가 검색 결과 안에 포함되었는지 측정하는 지표다.

기본 의미:

```text
Expected Document ∈ Retrieved Top-K
→ Hit

Expected Document ∉ Retrieved Top-K
→ Miss
```

Hit Rate는 RAG 검색이 필요한 근거 문서를 찾는지 확인하는 기본 지표다.

---

### [핵심]

- Hit Rate는 Expected Document 검색 성공률이다.
- Top-K 안에 기대 문서가 있으면 Hit로 본다.
- Hit Rate가 낮으면 검색 누락이 많다는 의미다.
- Hit Rate는 Ranking 품질까지 충분히 설명하지는 못한다.
- Top-K를 크게 하면 Hit Rate는 올라갈 수 있지만 Precision은 낮아질 수 있다.
- Hit Rate는 Golden Query Set 기준으로 측정한다.
- Expected Document 정의가 명확해야 한다.

---

### [실무]

Hit Rate 계산 예시:

```text
Golden Query 수: 10
Expected Document가 Top-K 안에 포함된 Query 수: 8

Hit Rate = 8 / 10 = 80%
```

평가 예시:

| Query                     | Expected Document        | Top-K Hit | Result |
| ------------------------- | ------------------------ | --------- | ------ |
| Embedding이 뭐야?         | Part01_Core              | 포함      | Hit    |
| Chunk Size는 어떻게 정해? | Part02_Chunking_Metadata | 포함      | Hit    |
| Reranking은 언제 필요해?  | Part03_Retrieval_Search  | 미포함    | Miss   |

Hit Rate 개선 방법:

```text
Miss Query 분석
→ Query 표현 확인
→ Expected Chunk 제목 확인
→ FAQ / Retrieval Queries 추가
→ Metadata 보강
→ 재Embedding
→ 재평가
```

---

### [주의]

- Hit Rate만으로 전체 Retrieval 품질을 판단하지 않는다.
- Top-K를 크게 하면 Hit Rate가 인위적으로 높아질 수 있다.
- Hit는 되었지만 낮은 순위면 Context Assembly에서 누락될 수 있다.
- Expected Document가 여러 개일 경우 평가 기준을 명확히 한다.
- Hit Rate와 Precision을 함께 본다.

---

### [FAQ]

Q. Retrieval Hit Rate는 뭐야?

A.
Expected Document가 Top-K 검색 결과 안에 포함되는 비율이다.

Q. Hit Rate가 높으면 Retrieval 품질이 좋은 거야?

A.
기본적으로 좋지만 충분하지는 않다. Ranking, Precision, Context 품질도 함께 봐야 한다.

Q. Hit Rate를 높이려면 어떻게 해?

A.
Chunk 제목, FAQ, Retrieval Queries, Metadata를 개선하고 Query Rewrite를 적용한다.

---

## 3.2 Precision and Recall

### [개념]

Precision은 검색 결과 중 실제로 관련 있는 Chunk 비율이다.
Recall은 필요한 관련 Chunk 중 검색 결과에 포함된 비율이다.

기본 의미:

```text
Precision:
검색된 Chunk 중 관련 있는 Chunk 비율

Recall:
필요한 Chunk 중 검색된 Chunk 비율
```

Precision과 Recall은 Trade-off 관계가 될 수 있다.

---

### [핵심]

- Precision은 검색 결과의 정확도다.
- Recall은 필요한 문서를 놓치지 않는 정도다.
- Top-K를 늘리면 Recall은 올라갈 수 있다.
- Top-K를 늘리면 Precision은 낮아질 수 있다.
- Threshold를 높이면 Precision은 올라갈 수 있다.
- Threshold를 높이면 Recall은 낮아질 수 있다.
- RAG에서는 Precision과 Recall 균형이 중요하다.

---

### [실무]

Precision 예시:

```text
Top-K 검색 결과: 5개
관련 Chunk: 3개

Precision = 3 / 5 = 60%
```

Recall 예시:

```text
필요한 Expected Chunk: 4개
검색 결과에 포함된 Expected Chunk: 3개

Recall = 3 / 4 = 75%
```

튜닝 기준:

| 상황                       | 해석                 | 조치                                  |
| -------------------------- | -------------------- | ------------------------------------- |
| Precision 낮음             | 관련 없는 Chunk 많음 | Threshold 상승, Top-K 축소, Reranking |
| Recall 낮음                | 필요한 Chunk 누락    | Query Rewrite, Top-K 증가, Chunk 개선 |
| Precision 높고 Recall 낮음 | 너무 좁게 검색       | Query Expansion, Threshold 완화       |
| Recall 높고 Precision 낮음 | 너무 넓게 검색       | Metadata Filter, Reranking            |

---

### [주의]

- Precision만 높이면 필요한 문서를 놓칠 수 있다.
- Recall만 높이면 관련 없는 Context가 많아질 수 있다.
- RAG에서는 Context Budget 때문에 무조건 Recall을 높일 수 없다.
- 평가 Query가 부족하면 Precision / Recall 해석이 왜곡된다.
- 관련 Chunk 판단 기준을 문서화해야 한다.

---

### [FAQ]

Q. Precision은 뭐야?

A.
검색된 Chunk 중 실제로 질문과 관련 있는 Chunk의 비율이다.

Q. Recall은 뭐야?

A.
필요한 관련 Chunk 중 검색 결과에 포함된 Chunk의 비율이다.

Q. Precision과 Recall 중 뭐가 더 중요해?

A.
둘 다 중요하다. RAG에서는 필요한 문서를 놓치지 않으면서 관련 없는 Context를 줄이는 균형이 필요하다.

---

## 3.3 MRR and NDCG

### [개념]

MRR은 Mean Reciprocal Rank의 약자로 정답 Chunk가 얼마나 높은 순위에 있는지 평가하는 지표다.

NDCG는 Normalized Discounted Cumulative Gain의 약자로 검색 결과 순위와 관련도 점수를 함께 평가하는 지표다.

RAG에서는 Expected Chunk가 Top-K 안에 있는 것뿐 아니라 상위에 있는지도 중요하다.

---

### [핵심]

- MRR은 첫 번째 정답 Chunk의 순위를 평가한다.
- 정답 Chunk가 1위에 가까울수록 MRR이 높다.
- NDCG는 여러 검색 결과의 관련도와 순위를 함께 평가한다.
- Ranking 품질 평가에 유용하다.
- Hit Rate보다 검색 순위 품질을 더 잘 본다.
- Reranking 효과를 평가할 때 유용하다.
- 복잡한 평가는 MRR / NDCG를 사용한다.

---

### [실무]

MRR 예시:

```text
Query A: 정답 Chunk 1위 → Reciprocal Rank = 1/1
Query B: 정답 Chunk 2위 → Reciprocal Rank = 1/2
Query C: 정답 Chunk 5위 → Reciprocal Rank = 1/5

MRR = 평균 Reciprocal Rank
```

NDCG 사용 상황:

```text
검색 결과 1위: 매우 관련 있음
검색 결과 2위: 부분 관련 있음
검색 결과 3위: 무관함

NDCG:
관련도 높은 문서가 상위에 있는지 평가
```

실무 적용:

| 상황                       | 추천 지표  |
| -------------------------- | ---------- |
| 기대 문서 포함 여부만 확인 | Hit Rate   |
| 관련 없는 결과 비율 확인   | Precision  |
| 필요한 문서 누락 확인      | Recall     |
| 정답 순위 평가             | MRR        |
| 여러 관련도 순위 평가      | NDCG       |
| Reranking 효과 확인        | MRR / NDCG |

---

### [주의]

- MRR은 첫 번째 정답 Chunk 중심이다.
- NDCG는 관련도 점수 기준이 필요하다.
- 소규모 개인 RAG에서는 Hit Rate와 Precision부터 시작해도 된다.
- 평가 지표가 좋아도 답변 품질이 항상 좋은 것은 아니다.
- Retrieval Evaluation과 Answer Evaluation을 분리한다.

---

### [FAQ]

Q. MRR은 뭐야?

A.
첫 번째 정답 Chunk가 검색 결과에서 얼마나 높은 순위에 있는지 평가하는 지표다.

Q. NDCG는 뭐야?

A.
검색 결과의 순위와 관련도 점수를 함께 평가하는 지표다.

Q. 개인 RAG에서도 MRR과 NDCG가 필요해?

A.
초기에는 Hit Rate와 Precision부터 시작하고, Reranking이나 고도화 단계에서 MRR / NDCG를 사용하면 좋다.

---

# 4. Failure Case Analysis

## 4.1 Retrieval Failure Case

### [개념]

Failure Case Analysis는 Retrieval 실패 사례를 수집하고 원인을 분류하는 과정이다.

검색 실패를 기록하지 않으면 같은 문제가 반복된다.
RAG 문서는 실패 사례를 기반으로 개선해야 한다.

---

### [핵심]

- Failure Case는 검색 품질 개선의 핵심 데이터다.
- 실패 Query를 기록한다.
- 검색된 Chunk와 기대 Chunk를 비교한다.
- Miss / Low Rank / Irrelevant / Duplicate 유형으로 분류한다.
- 실패 원인을 Query, Chunk, Metadata, Threshold, Reranking 관점에서 분석한다.
- 수정 후 재Embedding하고 다시 평가한다.
- 실패 사례는 Retrieval Queries 개선에 반영한다.

---

### [실무]

Failure Case 유형:

| 유형        | 설명                      | 주요 원인                        |
| ----------- | ------------------------- | -------------------------------- |
| Miss        | 기대 문서가 검색되지 않음 | Query 표현 불일치, Metadata 누락 |
| Low Rank    | 기대 문서가 낮은 순위     | Header 약함, Reranking 없음      |
| Irrelevant  | 관련 없는 문서 검색       | Top-K 과다, Threshold 낮음       |
| Duplicate   | 중복 Chunk 과다           | Overlap 과다, 중복 FAQ           |
| Fragmented  | Context가 너무 단편적     | Chunk 너무 작음                  |
| Mixed Topic | Chunk에 여러 주제 혼합    | Chunk 너무 큼                    |
| Stale Index | 수정 내용 미반영          | 재Embedding 누락                 |

Failure Case 기록 Template:

```md
### [Failure Case]

Query:
검색 결과가 안 나올 때 어떻게 해?

Expected:
Part04 Search Failure Troubleshooting

Actual:
Part03 Top-K Retrieval만 검색됨

Failure Type:
Miss / Low Rank

Cause:
Part04 문서의 Retrieval Queries 부족
검색 실패 관련 FAQ 표현 부족

Fix:
Search Failure, Retrieval Troubleshooting, 검색 결과 안 나옴 FAQ 추가
문서 재Embedding
```

개선 Flow:

```text
Failure Case 기록
→ Failure Type 분류
→ 원인 가설 작성
→ 문서 수정
→ Embedding 재생성
→ Golden Query 재평가
→ 개선 여부 기록
```

---

### [주의]

- 실패 Query를 삭제하지 말고 기록한다.
- 실제 검색 결과를 함께 보관한다.
- 원인을 하나로 단정하지 않는다.
- 문서 수정 후 재Embedding 여부를 반드시 확인한다.
- Top-K 증가만으로 실패를 덮지 않는다.
- 실패 사례를 Retrieval Queries에 반영한다.

---

### [FAQ]

Q. Failure Case Analysis는 뭐야?

A.
검색 실패 사례를 기록하고 원인을 분석해 RAG 문서를 개선하는 과정이다.

Q. 검색 실패 사례는 왜 기록해야 해?

A.
같은 실패를 반복하지 않고 Chunk, Metadata, Query, Retrieval Queries를 개선하기 위해 필요하다.

Q. Failure Case에는 무엇을 기록해?

A.
Query, Expected Document, Actual Result, Failure Type, Cause, Fix를 기록한다.

---

# 5. Search Failure Troubleshooting

## 5.1 No Result

### [개념]

No Result는 관련 문서가 존재하지만 검색 결과에 나타나지 않거나, 검색 결과가 비어 있는 문제다.

No Result는 Embedding Model 문제보다 Query 표현, Chunk 구조, Metadata, Threshold 문제인 경우가 많다.

---

### [Troubleshooting]

문제:

- 관련 문서가 있는데 Retrieval 결과에 나타나지 않음
- 검색 결과가 비어 있음
- Expected Document가 Top-K에 없음

원인:

- Query가 너무 짧거나 모호함
- Query와 문서 표현 불일치
- Chunk 제목이 불명확함
- FAQ / Retrieval Queries 부족
- 핵심 Keyword 누락
- Metadata Filter가 너무 강함
- Similarity Threshold가 너무 높음
- Embedding 미생성
- 문서 수정 후 재Embedding 누락
- Embedding Model과 Vector Index 불일치

해결:

- Query Rewrite 적용
- Query Expansion 적용
- Chunk 제목에 핵심 Keyword 추가
- FAQ / Retrieval Queries 추가
- 한글 + 영어 기술 용어 병기
- Metadata Filter 완화
- Threshold 완화
- Embedding 생성 여부 확인
- 문서 수정 후 재Embedding
- Vector Index와 Embedding Model 일치 확인

---

### [실무]

No Result 점검 Flow:

```text
1. Query가 너무 짧은지 확인
2. Query에 Domain Keyword가 있는지 확인
3. Expected Document에 관련 Header가 있는지 확인
4. FAQ / Retrieval Queries에 실제 질문 표현이 있는지 확인
5. Metadata Filter가 필요한 문서를 제외하는지 확인
6. Threshold가 너무 높은지 확인
7. 문서가 Embedding 되었는지 확인
8. 문서 수정 후 재Embedding 되었는지 확인
```

예시:

```text
Query:
검색 안 돼

Rewrite:
RAG Retrieval 검색 결과가 안 나올 때 Query, Chunk, Metadata, Threshold, Embedding 재생성 문제를 어떻게 점검해야 하는가?
```

---

### [FAQ]

Q. 검색 결과가 안 나오면 어떻게 해?

A.
Query 표현, Chunk 제목, Metadata Filter, Threshold, Embedding 생성 여부, 재Embedding 여부를 확인한다.

Q. 관련 문서가 있는데 검색이 안 되는 이유는?

A.
문서 표현과 Query 표현이 다르거나 FAQ, Retrieval Queries, Metadata가 부족할 수 있다.

Q. No Result는 Embedding Model 문제야?

A.
항상 그렇지 않다. 먼저 Query, Chunk, Metadata, Threshold, 재Embedding 여부를 점검해야 한다.

---

## 5.2 Irrelevant Result

### [개념]

Irrelevant Result는 User Query와 관련 없는 Chunk가 검색 결과에 포함되는 문제다.

관련 없는 Chunk가 Context에 들어가면 Chat Model 답변이 흔들릴 수 있다.

---

### [Troubleshooting]

문제:

- 질문과 관련 없는 Chunk가 Top-K에 포함됨
- 의미적으로 비슷하지만 의도와 다른 문서가 검색됨
- 다른 Domain 문서가 검색됨

원인:

- Top-K가 너무 큼
- Threshold가 너무 낮음
- Query가 너무 넓음
- Chunk에 여러 개념이 혼합됨
- Metadata Filter 없음
- Header가 모호함
- 공통 단어가 많음
- Reranking 없음

해결:

- Top-K 축소
- Threshold 조정
- Query 구체화
- Chunk를 하나의 개념 중심으로 분리
- Metadata Filter 적용
- Header에 Domain Keyword 추가
- Reranking 적용
- 공통 표현 중복 제거

---

### [실무]

Irrelevant Result 점검 Flow:

```text
검색 결과 확인
→ 관련 없는 Chunk의 공통점 확인
→ Top-K 과다 여부 확인
→ Threshold 낮음 여부 확인
→ Query가 너무 넓은지 확인
→ Chunk 주제 혼합 여부 확인
→ Metadata Filter 적용 가능성 확인
→ Reranking 필요 여부 확인
```

예시:

```text
Query:
Top-K는 몇 개가 좋아?

Irrelevant Result:
Vector Dimension Section 검색됨

원인:
Embedding / Vector 공통 단어가 많고 Top-K가 큼

Fix:
Top-K 관련 FAQ 강화
Top-K Section Header 개선
Reranking 적용
```

---

### [FAQ]

Q. 관련 없는 문서가 검색되면 어떻게 해?

A.
Top-K, Threshold, Query 구체화, Chunk 분리, Metadata Filter, Reranking을 점검한다.

Q. Semantic Search가 관련 없는 문서를 가져오는 이유는?

A.
의미적으로 비슷하지만 질문 의도와 다른 Chunk가 높은 Score를 받을 수 있기 때문이다.

Q. Irrelevant Result가 답변에 왜 위험해?

A.
관련 없는 Context가 Chat Model 답변에 섞여 부정확한 답변을 만들 수 있기 때문이다.

---

## 5.3 Low Rank

### [개념]

Low Rank는 Expected Chunk가 검색되긴 했지만 낮은 순위에 위치하는 문제다.

정답 Chunk가 Top-K 안에 있어도 최종 Context에 포함되지 않으면 답변에 활용되지 못할 수 있다.

---

### [Troubleshooting]

문제:

- Expected Chunk가 검색되지만 낮은 순위에 있음
- 정답 Chunk가 Top-K 끝부분에 위치함
- Reranking 후에도 핵심 Chunk가 상위로 오지 않음

원인:

- Header Keyword가 약함
- FAQ 질문 표현이 부족함
- Retrieval Queries 부족
- Query와 문서 표현 차이
- 유사한 문서가 많음
- Metadata Boost 없음
- Reranking 없음
- Chunk 내용이 너무 일반적임

해결:

- Header에 핵심 Keyword 추가
- FAQ에 실제 사용자 질문 추가
- Retrieval Queries 강화
- Query Rewrite 적용
- Metadata Boost 적용
- Reranking 적용
- Chunk 내용을 더 구체화
- 중복 Chunk 제거

---

### [실무]

Low Rank 개선 Flow:

```text
Expected Chunk 순위 확인
→ 상위 Chunk와 비교
→ Expected Chunk Header 확인
→ FAQ / Retrieval Queries 표현 확인
→ Metadata Boost 가능 여부 확인
→ Reranking 적용
→ 재평가
```

예시:

```text
Query:
Reranking은 언제 필요해?

Expected:
Reranker Section

Actual:
Semantic Search Section이 1위
Reranker Section이 6위

Fix:
Reranker Section FAQ 강화
"Reranking은 언제 필요해?" Retrieval Query 추가
Reranking Keyword Header 보강
```

---

### [FAQ]

Q. Low Rank는 뭐야?

A.
Expected Chunk가 검색되지만 낮은 순위에 위치해 최종 Context에서 누락될 수 있는 문제다.

Q. 정답 Chunk가 낮은 순위면 어떻게 해?

A.
Header, FAQ, Retrieval Queries를 강화하고 Metadata Boost와 Reranking을 검토한다.

Q. Reranking은 Low Rank 문제에 도움이 돼?

A.
도움이 될 수 있다. 1차 검색 후보에 정답 Chunk가 포함되어 있다면 순위를 개선할 수 있다.

---

## 5.4 Duplicate Result

### [개념]

Duplicate Result는 비슷하거나 동일한 Chunk가 검색 결과를 과도하게 차지하는 문제다.

중복 Chunk가 많으면 다른 중요한 근거가 Top-K에서 밀릴 수 있다.

---

### [Troubleshooting]

문제:

- 비슷한 Chunk가 Top-K 대부분을 차지함
- 같은 Section의 FAQ와 Retrieval Queries가 반복 검색됨
- Hybrid Search 결과 병합 후 중복이 많음

원인:

- Chunk Overlap 과다
- 동일 FAQ 반복
- Retrieval Queries 중복
- 같은 설명을 여러 문서에 반복
- Deduplication 없음
- fileName / section 기준 중복 제한 없음

해결:

- Chunk Overlap 줄이기
- 중복 FAQ 제거
- Retrieval Queries 문서별 차별화
- Deduplication 적용
- section 기준 중복 제한
- 중복 문장 정리
- 상위 Score Chunk만 유지

---

### [실무]

Duplicate Result 제거 Flow:

```text
Top-K 결과 확인
→ chunkId 중복 제거
→ fileName + section 중복 제한
→ Text Similarity 높은 Chunk 제거
→ Score 높은 Chunk 유지
→ Context 다양성 확인
```

중복 판단 기준:

| 기준                   | 설명                        |
| ---------------------- | --------------------------- |
| chunkId                | 동일 Chunk 제거             |
| fileName + section     | 같은 Section 과다 검색 제한 |
| Text Similarity        | 거의 같은 내용 제거         |
| FAQ 중복               | 같은 질문 반복 제거         |
| Retrieval Queries 중복 | 문서별 차별화               |

---

### [FAQ]

Q. Duplicate Result는 뭐야?

A.
동일하거나 매우 유사한 Chunk가 검색 결과를 과도하게 차지하는 문제다.

Q. 중복 Chunk가 많으면 왜 문제야?

A.
Top-K를 중복 Chunk가 차지해 다른 중요한 근거 문서가 밀릴 수 있다.

Q. 중복 검색 결과는 어떻게 줄여?

A.
Overlap 축소, 중복 FAQ 제거, Retrieval Queries 차별화, Deduplication을 적용한다.

---

# 6. Answer Failure from Retrieval

## 6.1 Retrieved But Wrong Answer

### [개념]

Retrieved But Wrong Answer는 검색 결과는 존재하지만 Chat Model 답변이 틀리는 문제다.

이 문제는 Retrieval 문제와 Generation 문제를 분리해서 분석해야 한다.

---

### [Troubleshooting]

문제:

- 검색 결과는 있지만 답변이 틀림
- Retrieved Context와 다른 답변을 생성함
- 문서에 없는 내용을 일반 지식으로 보완함
- 관련 없는 Chunk를 근거로 답변함

원인:

- Retrieved Context가 불충분함
- 필요한 Chunk가 일부 누락됨
- 관련 없는 Chunk가 포함됨
- Context Assembly 순서가 나쁨
- 충돌 문서가 포함됨
- Prompt Grounding 규칙 부족
- Chat Model이 문서 근거보다 일반 지식을 우선함

해결:

- Retrieved Context 직접 확인
- 필요한 Chunk 추가 검색
- 관련 없는 Chunk 제거
- Reranking / Deduplication 적용
- Context Assembly 순서 조정
- 문서 Version 우선순위 적용
- Prompt에 문서 근거 우선 규칙 추가
- 정보 부족 시 Missing Information 출력

---

### [실무]

분석 Flow:

```text
답변 오류 확인
→ Retrieved Context 확인
→ Context 안에 정답 근거가 있는지 확인
→ 근거가 없으면 Retrieval 문제
→ 근거가 있는데 답변이 틀리면 Generation / Prompt 문제
→ Context가 충돌하면 Version / 우선순위 문제
```

Grounding Prompt 예시:

```text
Retrieved Context에 없는 내용은 일반 지식으로 보완하지 않는다.
문서 근거가 부족하면 "문서에 없음" 또는 "추가 정보 필요"라고 답한다.
서로 충돌하는 Context가 있으면 최신 version과 domain 우선순위를 따른다.
```

---

### [FAQ]

Q. 검색은 됐는데 답변이 틀리면 어떻게 해?

A.
Retrieved Context에 정답 근거가 있는지 확인하고, 없으면 Retrieval 문제, 있으면 Prompt Grounding 문제로 분리한다.

Q. Chat Model이 문서에 없는 내용을 답하면 어떻게 해?

A.
Prompt에 문서 근거 우선 규칙과 Missing Information 출력 규칙을 추가한다.

Q. 관련 없는 Context가 답변에 섞이면 어떻게 해?

A.
Threshold, Reranking, Deduplication, Context Assembly를 개선한다.

---

# 7. Evaluation Loop

## 7.1 Continuous Retrieval Improvement

### [개념]

Evaluation Loop는 Retrieval 평가 결과를 문서 개선으로 연결하고 다시 평가하는 반복 개선 구조다.

RAG 문서는 한 번 작성하고 끝나는 문서가 아니다.
검색 실패 사례를 반영해 계속 개선해야 한다.

기본 Flow:

```text
Evaluate
→ Analyze Failure
→ Improve Document
→ Re-Embed
→ Re-Test
→ Record Result
```

---

### [핵심]

- Retrieval 품질은 반복 평가로 개선한다.
- 실패 Query를 Golden Query에 추가한다.
- 문서 수정 후 재Embedding한다.
- 개선 전후 Hit Rate와 Ranking을 비교한다.
- Chunk 제목, FAQ, Retrieval Queries를 우선 개선한다.
- Metadata 누락을 보완한다.
- Top-K / Threshold / Reranking은 평가 기반으로 조정한다.
- 개선 기록을 남긴다.

---

### [실무]

Evaluation Loop Template:

```md
### [Evaluation Log]

Date:
2026-06-30

Query:
Threshold는 어떻게 잡아?

Before:
Expected Section 미검색

Fix:
Similarity Threshold FAQ 추가
Retrieval Queries에 Threshold 질문 추가
Metadata tags에 threshold 추가

After:
Expected Section Top-3 진입

Result:
Improved
```

개선 우선순위:

```text
1. Query 표현과 문서 표현 정렬
2. Header Keyword 개선
3. FAQ 추가
4. Retrieval Queries 보강
5. Metadata 보강
6. Chunk 분리 / 병합
7. Top-K / Threshold 조정
8. Hybrid Search 적용
9. Reranking 적용
```

---

### [주의]

- 문서 수정 후 재Embedding을 누락하지 않는다.
- 개선 효과를 감으로 판단하지 않는다.
- 평가 전후 결과를 비교한다.
- 한 Query에 최적화하다가 다른 Query 성능을 떨어뜨릴 수 있다.
- 중복 FAQ를 과도하게 늘리지 않는다.
- Retrieval Queries는 문서별로 차별화한다.

---

### [FAQ]

Q. Evaluation Loop는 뭐야?

A.
검색 품질을 평가하고 실패 원인을 문서에 반영한 뒤 재Embedding하고 다시 평가하는 반복 개선 구조다.

Q. 문서 수정 후 왜 재Embedding해야 해?

A.
Vector Index가 수정된 내용을 반영하려면 새 Embedding이 필요하기 때문이다.

Q. 개선 효과는 어떻게 확인해?

A.
Golden Query의 Hit Rate, Ranking, Precision 변화를 비교해 확인한다.

---

# 8. Best Practice

## 8.1 Retrieval Evaluation Best Practice

### [Best Practice]

Retrieval Evaluation Best Practice:

- Golden Query Set을 먼저 만든다.
- Query마다 Expected Document와 Expected Section을 지정한다.
- Hit Rate로 기본 검색 성공 여부를 확인한다.
- Precision으로 관련 없는 Chunk 비율을 확인한다.
- Recall로 필요한 Chunk 누락 여부를 확인한다.
- MRR로 정답 Chunk 순위를 평가한다.
- NDCG로 여러 관련 Chunk의 Ranking 품질을 평가한다.
- Failure Case를 Miss / Low Rank / Irrelevant / Duplicate로 분류한다.
- 실패 Query를 Retrieval Queries 개선에 반영한다.
- 문서 수정 후 반드시 재Embedding한다.
- 개선 전후 결과를 기록한다.
- Retrieval Evaluation과 Answer Evaluation을 분리한다.

---

### [Checklist]

- [ ] Golden Query Set이 있는가?
- [ ] 각 Query에 Expected Document가 연결되어 있는가?
- [ ] Expected Section까지 정의되어 있는가?
- [ ] Top-K 안에 Expected Chunk가 들어오는가?
- [ ] Hit Rate를 측정했는가?
- [ ] Precision과 Recall을 구분했는가?
- [ ] 정답 Chunk 순위를 확인했는가?
- [ ] MRR / NDCG 사용 필요성을 검토했는가?
- [ ] Failure Case를 기록했는가?
- [ ] 실패 유형을 분류했는가?
- [ ] No Result 원인을 분석했는가?
- [ ] Irrelevant Result 원인을 분석했는가?
- [ ] Low Rank 원인을 분석했는가?
- [ ] Duplicate Result 원인을 분석했는가?
- [ ] 검색은 됐지만 답변이 틀린 사례를 분리했는가?
- [ ] 문서 수정 후 재Embedding했는가?
- [ ] 개선 전후 결과를 비교했는가?

---

### [FAQ]

Q. Retrieval Evaluation Best Practice 핵심은 뭐야?

A.
Golden Query와 Expected Document를 기준으로 Hit Rate, Ranking, 실패 유형을 반복 평가하는 것이다.

Q. 가장 먼저 봐야 할 Retrieval 지표는 뭐야?

A.
초기에는 Expected Document가 Top-K 안에 들어오는지 보는 Hit Rate부터 확인하는 것이 좋다.

Q. 고도화 단계에서 어떤 지표를 봐야 해?

A.
Precision, Recall, MRR, NDCG를 추가해 검색 정확도와 Ranking 품질을 평가한다.

Q. Retrieval 평가와 답변 평가는 분리해야 해?

A.
그렇다. 검색이 실패한 것인지, 검색은 됐지만 답변 생성이 실패한 것인지 구분해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Retrieval Evaluation은 뭐야?
A. RAG 검색 결과가 사용자 질문에 맞는 문서를 잘 찾는지 평가하는 과정이다.

Q. Retrieval Evaluation은 왜 필요해?
A. 검색이 실패하면 Chat Model이 근거 있는 답변을 만들기 어렵기 때문이다.

Q. Retrieval 성공과 답변 성공은 같아?
A. 아니다. 검색이 성공해도 Prompt Grounding이나 Context Assembly가 나쁘면 답변이 틀릴 수 있다.

Q. Golden Query는 뭐야?
A. Retrieval 품질을 평가하기 위해 미리 정의한 대표 사용자 질문이다.

Q. Golden Query에는 무엇을 연결해야 해?
A. Expected Document, Expected Section, 기대 답변 기준을 연결하는 것이 좋다.

Q. Golden Query는 실제 질문처럼 써야 해?
A. 그렇다. 실제 사용자 Query와 다르면 평가 결과의 의미가 낮아진다.

Q. Retrieval Hit Rate는 뭐야?
A. Expected Document가 Top-K 검색 결과 안에 포함되는 비율이다.

Q. Hit Rate가 높으면 Retrieval 품질이 좋은 거야?
A. 기본적으로 좋지만 충분하지는 않다. Ranking, Precision, Context 품질도 함께 봐야 한다.

Q. Precision은 뭐야?
A. 검색된 Chunk 중 실제로 질문과 관련 있는 Chunk의 비율이다.

Q. Recall은 뭐야?
A. 필요한 관련 Chunk 중 검색 결과에 포함된 Chunk의 비율이다.

Q. Precision과 Recall 중 뭐가 더 중요해?
A. 둘 다 중요하다. RAG에서는 필요한 문서를 놓치지 않으면서 관련 없는 Context를 줄이는 균형이 필요하다.

Q. MRR은 뭐야?
A. 첫 번째 정답 Chunk가 검색 결과에서 얼마나 높은 순위에 있는지 평가하는 지표다.

Q. NDCG는 뭐야?
A. 검색 결과의 순위와 관련도 점수를 함께 평가하는 지표다.

Q. Failure Case Analysis는 뭐야?
A. 검색 실패 사례를 기록하고 원인을 분석해 RAG 문서를 개선하는 과정이다.

Q. Failure Case에는 무엇을 기록해?
A. Query, Expected Document, Actual Result, Failure Type, Cause, Fix를 기록한다.

Q. 검색 결과가 안 나오면 어떻게 해?
A. Query 표현, Chunk 제목, Metadata Filter, Threshold, Embedding 생성 여부, 재Embedding 여부를 확인한다.

Q. 관련 문서가 있는데 검색이 안 되는 이유는?
A. 문서 표현과 Query 표현이 다르거나 FAQ, Retrieval Queries, Metadata가 부족할 수 있다.

Q. 관련 없는 문서가 검색되면 어떻게 해?
A. Top-K, Threshold, Query 구체화, Chunk 분리, Metadata Filter, Reranking을 점검한다.

Q. Semantic Search가 관련 없는 문서를 가져오는 이유는?
A. 의미적으로 비슷하지만 질문 의도와 다른 Chunk가 높은 Score를 받을 수 있기 때문이다.

Q. Low Rank는 뭐야?
A. Expected Chunk가 검색되지만 낮은 순위에 위치해 최종 Context에서 누락될 수 있는 문제다.

Q. 정답 Chunk가 낮은 순위면 어떻게 해?
A. Header, FAQ, Retrieval Queries를 강화하고 Metadata Boost와 Reranking을 검토한다.

Q. Duplicate Result는 뭐야?
A. 동일하거나 매우 유사한 Chunk가 검색 결과를 과도하게 차지하는 문제다.

Q. 중복 검색 결과는 어떻게 줄여?
A. Overlap 축소, 중복 FAQ 제거, Retrieval Queries 차별화, Deduplication을 적용한다.

Q. 검색은 됐는데 답변이 틀리면 어떻게 해?
A. Retrieved Context에 정답 근거가 있는지 확인하고, 없으면 Retrieval 문제, 있으면 Prompt Grounding 문제로 분리한다.

Q. Chat Model이 문서에 없는 내용을 답하면 어떻게 해?
A. Prompt에 문서 근거 우선 규칙과 Missing Information 출력 규칙을 추가한다.

Q. Evaluation Loop는 뭐야?
A. 검색 품질을 평가하고 실패 원인을 문서에 반영한 뒤 재Embedding하고 다시 평가하는 반복 개선 구조다.

Q. 문서 수정 후 왜 재Embedding해야 해?
A. Vector Index가 수정된 내용을 반영하려면 새 Embedding이 필요하기 때문이다.

Q. 개선 효과는 어떻게 확인해?
A. Golden Query의 Hit Rate, Ranking, Precision 변화를 비교해 확인한다.

Q. Retrieval Evaluation Best Practice 핵심은 뭐야?
A. Golden Query와 Expected Document를 기준으로 Hit Rate, Ranking, 실패 유형을 반복 평가하는 것이다.

Q. Retrieval 평가와 답변 평가는 분리해야 해?
A. 그렇다. 검색이 실패한 것인지, 검색은 됐지만 답변 생성이 실패한 것인지 구분해야 한다.
