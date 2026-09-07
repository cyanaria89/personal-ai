# RAG Evaluation & Retrieval Optimization Part06 Top-K / Threshold / Reranking / Context Optimization

---

# 1. Context Retrieval Control Core

## 1.1 Retrieval Control 기본 개념

### [개념]

Retrieval Control은 RAG 검색 결과의 양, 품질, 순위, Context 전달 방식을 조정하는 과정이다.

Top-K, Similarity Threshold, Reranking, Deduplication, Context Assembly는 Retrieval 결과를 LLM 답변에 적합한 Context로 만드는 핵심 제어 요소다.

```text
User Query
→ Retrieve Candidate Chunks
→ Apply Top-K
→ Apply Similarity Threshold
→ Apply Reranking
→ Deduplicate Context
→ Assemble Context
→ Generate Grounded Answer
```

---

### [핵심]

- Top-K는 검색 결과 개수를 제어한다.
- Similarity Threshold는 최소 관련도 기준을 제어한다.
- Reranking은 검색 결과 순위를 재정렬한다.
- Deduplication은 중복 Context를 제거한다.
- Context Assembly는 LLM에 전달할 Context를 구성한다.
- Context Optimization은 Token Budget 안에서 근거 품질을 높인다.
- Retrieval Control은 Precision과 Recall 균형을 맞추기 위한 작업이다.
- 감으로 조정하지 않고 Evaluation Result 기반으로 조정한다.

---

### [실무]

2026 실무 기준 RAG 검색 품질 개선은 Top-K만 조정하지 않는다.

검색 결과가 많아도 LLM에 전달되는 Context가 노이즈와 중복으로 채워지면 답변 품질은 낮아진다.

| 조정 대상            | 주요 목적              | 실패 시 증상                |
| -------------------- | ---------------------- | --------------------------- |
| Top-K                | 검색 후보 개수 조정    | 누락 또는 노이즈 증가       |
| Similarity Threshold | 낮은 관련도 Chunk 제거 | 검색 결과 과다 또는 빈 결과 |
| Reranking            | 관련 Chunk 상위 배치   | 기대 문서 순위 낮음         |
| Deduplication        | 중복 제거              | 같은 내용 반복              |
| Context Assembly     | 답변용 근거 구성       | 근거 누락 또는 혼선         |
| Context Compression  | 긴 Context 압축        | 조건 / 예외 누락            |

Retrieval Control은 Retrieval Evaluation과 Generation Evaluation 결과를 함께 보고 조정한다.

---

### [FAQ]

Q. Retrieval Control은 뭐야?

A. Top-K, Threshold, Reranking, Context Assembly를 조정해 검색 결과를 답변에 적합하게 만드는 과정이다.

Q. Top-K만 조정하면 충분해?

A. 아니다. Threshold, Reranking, Deduplication, Context Assembly도 함께 봐야 한다.

Q. 검색 결과가 많으면 좋은 거야?

A. 아니다. 관련 없는 Chunk가 많으면 Precision이 낮아지고 답변 품질이 흔들릴 수 있다.

Q. Retrieval Control은 무엇을 기준으로 조정해?

A. Hit@K, Precision, Recall, Ranking Quality, Groundedness 평가 결과를 기준으로 조정한다.

Q. 검색 결과는 좋은데 답변이 틀리면 어디를 봐?

A. Context Assembly, Context Order, Grounding Rule, Faithfulness Check를 확인한다.

---

## 1.2 Precision / Recall Balance

### [개념]

Precision / Recall Balance는 검색 결과의 정확도와 포괄성을 동시에 고려하는 기준이다.

RAG에서는 필요한 문서를 놓치지 않으면서, 관련 없는 노이즈를 줄이는 균형이 중요하다.

---

### [핵심]

- Precision은 검색 결과 중 관련 Chunk 비율이다.
- Recall은 필요한 관련 Chunk 중 검색된 비율이다.
- Top-K를 높이면 Recall은 올라갈 수 있다.
- Top-K를 높이면 Precision은 낮아질 수 있다.
- Threshold를 높이면 Precision은 올라갈 수 있다.
- Threshold를 높이면 Recall은 낮아질 수 있다.
- Reranking은 Precision과 Ranking Quality 개선에 도움된다.
- Context Budget 안에서 균형을 맞춰야 한다.

---

### [실무]

Precision / Recall 조정 기준:

| 증상                    | 판단                  | 우선 조치                   |
| ----------------------- | --------------------- | --------------------------- |
| 기대 문서가 누락됨      | Recall 낮음           | Top-K 증가, Query Expansion |
| 관련 없는 문서가 많음   | Precision 낮음        | Top-K 감소, Threshold 상향  |
| 기대 문서가 뒤쪽에 있음 | Ranking 낮음          | Reranking, Header 보강      |
| 검색 결과가 비어 있음   | Threshold 과도        | Threshold 완화              |
| Context가 너무 김       | Token Budget 초과     | Deduplication, Compression  |
| 답변 근거가 약함        | Context Assembly 문제 | Source Priority 재정렬      |

판단 Flow:

```text
Expected Document Missing
→ Recall Issue
→ Increase Top-K or Expand Query

Noise Chunks Too Many
→ Precision Issue
→ Reduce Top-K or Increase Threshold

Expected Document Found but Low Rank
→ Ranking Issue
→ Apply Reranking
```

---

### [FAQ]

Q. Precision / Recall Balance는 뭐야?

A. 검색 결과의 정확도와 필요한 문서 누락 방지를 함께 고려하는 균형이다.

Q. Top-K를 높이면 무조건 좋아?

A. 아니다. Recall은 좋아질 수 있지만 Precision은 낮아질 수 있다.

Q. Threshold를 높이면 무조건 좋아?

A. 아니다. Precision은 좋아질 수 있지만 필요한 문서가 빠져 Recall이 낮아질 수 있다.

Q. 기대 문서가 안 나오면 무엇을 조정해?

A. Top-K 증가, Query Expansion, Header / FAQ 보강을 검토한다.

Q. 관련 없는 문서가 많으면 무엇을 조정해?

A. Top-K 감소, Threshold 상향, Metadata Filter, Reranking을 검토한다.

---

# 2. Top-K Optimization

## 2.1 Top-K 기본 개념

### [개념]

Top-K는 Retrieval 단계에서 검색 결과로 가져올 Chunk 개수다.

Top-K는 필요한 문서를 포함할 가능성과 Context 노이즈 양을 동시에 결정한다.

```text
Top-K = 검색 결과로 반환할 상위 K개 Chunk
```

---

### [핵심]

- Top-K는 Retrieval 후보 개수를 결정한다.
- Top-K가 낮으면 필요한 문서가 누락될 수 있다.
- Top-K가 높으면 관련 없는 Chunk가 섞일 수 있다.
- Top-K 증가는 Recall 개선에 도움될 수 있다.
- Top-K 감소는 Precision 개선에 도움될 수 있다.
- Top-K는 Context Window와 Token Budget을 고려해 조정한다.
- Top-K는 Evaluation Result 기반으로 조정한다.
- 무조건 큰 Top-K는 좋은 설정이 아니다.

---

### [실무]

Top-K 조정 기준:

| 상태                                | Top-K 조정                 |
| ----------------------------------- | -------------------------- |
| Expected Document가 Top-K 밖에 있음 | 증가 검토                  |
| Expected Chunk가 일부 누락됨        | 증가 검토                  |
| 관련 없는 Chunk가 많음              | 감소 검토                  |
| 중복 Chunk가 많음                   | 감소 또는 Deduplication    |
| Context Window 초과                 | 감소 또는 Compression      |
| Rank는 낮지만 포함됨                | Reranking 우선 검토        |
| 검색 결과가 비어 있음               | Threshold 완화도 함께 검토 |

Top-K 설정 예시:

```text
초기 평가:
Top-K = 5

Recall 낮음:
Top-K = 8 또는 10 검토

Precision 낮음:
Top-K = 3 또는 Threshold 상향 검토

Reranking 사용:
Candidate Top-K = 20
Final Top-K = 5
```

---

### [FAQ]

Q. Top-K는 뭐야?

A. Retrieval 단계에서 검색 결과로 가져올 상위 Chunk 개수다.

Q. Top-K를 높이면 뭐가 좋아져?

A. 필요한 문서가 포함될 가능성이 커져 Recall이 올라갈 수 있다.

Q. Top-K를 높이면 뭐가 나빠져?

A. 관련 없는 Chunk도 함께 들어와 Precision이 낮아질 수 있다.

Q. Top-K는 몇으로 설정해야 해?

A. 고정값보다 Evaluation Result, Context Budget, Domain 특성에 따라 조정해야 한다.

Q. Top-K가 높아도 답변이 틀릴 수 있어?

A. 가능하다. 노이즈 Context가 많으면 LLM 답변이 흔들릴 수 있다.

---

## 2.2 Top-K Increase

### [개념]

Top-K Increase는 필요한 문서나 Chunk가 검색 결과에 누락될 때 검색 후보 개수를 늘리는 조정이다.

Top-K Increase는 Recall 개선에 도움될 수 있지만 Precision 저하를 유발할 수 있다.

---

### [핵심]

- Expected Document가 누락될 때 Top-K 증가를 검토한다.
- Expected Chunk가 일부 누락될 때 Top-K 증가를 검토한다.
- 복합 Query에서 여러 문서가 필요하면 Top-K 증가가 필요할 수 있다.
- Top-K 증가 후 Precision 하락을 확인해야 한다.
- Top-K 증가로도 개선되지 않으면 Query / Chunk / Metadata 문제를 점검한다.
- Top-K 증가는 Reindex 누락 문제를 해결하지 못한다.

---

### [실무]

Top-K Increase 판단표:

| 증상                              | Top-K 증가 여부               | 추가 확인               |
| --------------------------------- | ----------------------------- | ----------------------- |
| Expected Document가 Rank 6에 있음 | 증가 효과 가능                | Ranking도 확인          |
| Expected Document가 전혀 없음     | 증가 전 Query / Metadata 확인 | Document Miss 원인 분석 |
| 복합 질문에 일부 문서만 검색      | 증가 검토                     | Context Budget 확인     |
| Precision이 이미 낮음             | 주의                          | Reranking 병행          |
| Threshold가 너무 높음             | Threshold 완화 우선           | 빈 결과 확인            |

Top-K Increase Retest 예시:

```md
# Top-K Increase Retest

## Query

Groundedness와 Faithfulness 차이는?

## Before

- Top-K: 3
- Expected Document Rank: 5
- Hit@3: Fail

## After

- Top-K: 5
- Expected Document Rank: 5
- Hit@5: Pass
- Precision@5: 0.60

## Result

- Recall improved
- Precision needs monitoring
```

---

### [FAQ]

Q. Top-K Increase는 뭐야?

A. 필요한 문서 누락을 줄이기 위해 검색 결과 개수를 늘리는 조정이다.

Q. Top-K는 언제 늘려?

A. Expected Document나 Expected Chunk가 검색 결과 밖에 있을 때 늘리는 것을 검토한다.

Q. Top-K를 늘렸는데도 문서가 안 나오면?

A. Query, Header, FAQ, Metadata, Reindex 문제를 확인해야 한다.

Q. Top-K를 늘리면 Precision은 어떻게 돼?

A. 관련 없는 Chunk가 늘어 Precision이 낮아질 수 있다.

Q. 복합 질문에는 Top-K를 늘려야 해?

A. 여러 문서가 필요하면 늘릴 수 있지만 Context Budget과 노이즈를 함께 봐야 한다.

---

## 2.3 Top-K Decrease

### [개념]

Top-K Decrease는 검색 결과에 관련 없는 Chunk가 많이 섞일 때 검색 후보 개수를 줄이는 조정이다.

Top-K Decrease는 Precision 개선에 도움될 수 있지만 Recall 저하를 유발할 수 있다.

---

### [핵심]

- 관련 없는 Chunk가 많으면 Top-K 감소를 검토한다.
- Context Window가 노이즈로 채워지면 Top-K 감소를 검토한다.
- 중복 Chunk가 많으면 Deduplication도 함께 검토한다.
- Top-K 감소 후 Expected Document 누락 여부를 확인한다.
- Top-K 감소는 Recall 저하 위험이 있다.
- Precision 낮음의 원인이 Chunk 혼합이면 Chunk Optimization이 우선일 수 있다.

---

### [실무]

Top-K Decrease 판단표:

| 증상                                 | Top-K 감소 여부             | 추가 확인            |
| ------------------------------------ | --------------------------- | -------------------- |
| Precision@10 낮음                    | 감소 검토                   | Threshold도 확인     |
| Top-3는 좋고 이후 노이즈 많음        | 감소 가능                   | Final Top-K 분리     |
| 중복 Chunk 반복                      | 감소보다 Deduplication 우선 | Chunk Boundary 확인  |
| Expected Document가 낮은 Rank에 있음 | 감소 주의                   | Reranking 우선       |
| Recall 낮음                          | 감소 비권장                 | Query Expansion 검토 |

Top-K Decrease Retest 예시:

```md
# Top-K Decrease Retest

## Query

Precision과 Recall 차이는?

## Before

- Top-K: 10
- Precision@10: 0.40
- Expected Document Rank: 1

## After

- Top-K: 5
- Precision@5: 0.80
- Expected Document Rank: 1
- Hit@5: Pass

## Result

- Precision improved
- Recall still acceptable
```

---

### [FAQ]

Q. Top-K Decrease는 뭐야?

A. 검색 결과에 노이즈가 많을 때 검색 결과 개수를 줄이는 조정이다.

Q. Top-K는 언제 줄여?

A. 관련 없는 Chunk가 많이 검색되고 Expected Document는 상위에 있을 때 줄일 수 있다.

Q. Top-K를 줄이면 뭐가 좋아져?

A. 노이즈가 줄어 Precision이 높아질 수 있다.

Q. Top-K를 줄이면 뭐가 나빠져?

A. 필요한 문서가 누락되어 Recall이 낮아질 수 있다.

Q. 중복 Chunk가 많으면 Top-K를 줄이면 돼?

A. Deduplication과 Chunk Boundary 점검도 함께 필요하다.

---

# 3. Similarity Threshold Optimization

## 3.1 Similarity Threshold 기본 개념

### [개념]

Similarity Threshold는 검색 결과로 인정할 최소 유사도 기준이다.

Threshold보다 낮은 관련도 Chunk는 검색 결과에서 제외할 수 있다.

```text
Retrieved Chunk Similarity >= Threshold
→ Include

Retrieved Chunk Similarity < Threshold
→ Exclude
```

---

### [핵심]

- Similarity Threshold는 낮은 관련도 Chunk를 제거한다.
- Threshold가 낮으면 검색 결과가 많아질 수 있다.
- Threshold가 낮으면 노이즈가 증가할 수 있다.
- Threshold가 높으면 Precision이 좋아질 수 있다.
- Threshold가 높으면 필요한 문서가 제외될 수 있다.
- Threshold가 너무 높으면 검색 결과가 비어 있을 수 있다.
- Threshold는 Domain, Embedding Model, Chunk 구조에 따라 달라진다.

---

### [실무]

Threshold 조정 기준:

| 상태                                 | Threshold 조정          |
| ------------------------------------ | ----------------------- |
| 관련 없는 문서가 많음                | 상향 검토               |
| 검색 결과가 너무 많음                | 상향 검토               |
| 검색 결과가 비어 있음                | 하향 검토               |
| Expected Document가 낮은 점수로 제외 | 하향 검토               |
| Precision 낮음                       | 상향 또는 Reranking     |
| Recall 낮음                          | 하향 또는 Top-K 증가    |
| Embedding 점수 분포 불명확           | Score Distribution 확인 |

Threshold 운영 예시:

```md
# Threshold Review

## Query

문서에 있는데 검색이 안 돼

## Result

- Expected Document Score: 0.68
- Current Threshold: 0.70
- Expected Document Excluded

## Action

- Threshold 0.65 검토
- Retest Precision / Recall
```

---

### [FAQ]

Q. Similarity Threshold는 뭐야?

A. 검색 결과로 인정할 최소 유사도 기준이다.

Q. Threshold를 높이면 뭐가 좋아져?

A. 관련 없는 Chunk가 줄어 Precision이 좋아질 수 있다.

Q. Threshold를 높이면 뭐가 나빠져?

A. 필요한 문서가 제외되어 Recall이 낮아질 수 있다.

Q. Threshold를 낮추면 뭐가 좋아져?

A. 더 많은 문서가 검색되어 Recall이 높아질 수 있다.

Q. Threshold를 낮추면 뭐가 나빠져?

A. 관련 없는 문서가 늘어나 Precision이 낮아질 수 있다.

---

## 3.2 Threshold Increase

### [개념]

Threshold Increase는 검색 결과에 관련 없는 Chunk가 많이 포함될 때 최소 유사도 기준을 높이는 조정이다.

Threshold Increase는 Precision 개선에 도움될 수 있다.

---

### [핵심]

- Low Precision 상황에서 Threshold Increase를 검토한다.
- 노이즈 Chunk가 낮은 Score에 몰려 있으면 효과적이다.
- Threshold를 올리면 낮은 관련도 Chunk를 제거할 수 있다.
- Threshold를 올린 후 Expected Document 제외 여부를 확인한다.
- Threshold를 과도하게 올리면 검색 결과가 비어 있을 수 있다.
- Threshold Increase는 Chunk 혼합 문제를 완전히 해결하지 못한다.

---

### [실무]

Threshold Increase Retest 예시:

```md
# Threshold Increase Retest

## Query

검색 결과에 엉뚱한 문서가 많아

## Before

- Threshold: 0.60
- Retrieved: 10
- Precision@10: 0.30

## After

- Threshold: 0.72
- Retrieved: 5
- Precision@5: 0.80
- Expected Document: Included

## Result

- Precision improved
- Recall acceptable
```

Threshold Increase 주의:

| 위험                   | 대응                                |
| ---------------------- | ----------------------------------- |
| Expected Document 제외 | Threshold 완화                      |
| 검색 결과 0개          | Threshold 완화 또는 Query Expansion |
| 관련 Chunk도 함께 제거 | Score Distribution 확인             |
| 일부 Query 성능 하락   | Regression Check                    |

---

### [FAQ]

Q. Threshold Increase는 뭐야?

A. 노이즈 Chunk를 줄이기 위해 최소 유사도 기준을 높이는 조정이다.

Q. Threshold는 언제 높여?

A. 검색 결과에 관련 없는 Chunk가 많이 섞일 때 높이는 것을 검토한다.

Q. Threshold를 높이면 항상 Precision이 좋아져?

A. 대체로 도움될 수 있지만 필요한 문서도 제거될 수 있어 Retest가 필요하다.

Q. Threshold를 너무 높이면 어떻게 돼?

A. 검색 결과가 비거나 필요한 문서가 누락될 수 있다.

Q. Threshold를 올린 후 무엇을 확인해?

A. Expected Document 포함 여부, Precision, Recall, Regression을 확인한다.

---

## 3.3 Threshold Decrease

### [개념]

Threshold Decrease는 필요한 문서가 유사도 기준 때문에 제외되거나 검색 결과가 비어 있을 때 최소 유사도 기준을 낮추는 조정이다.

Threshold Decrease는 Recall 개선에 도움될 수 있다.

---

### [핵심]

- 검색 결과가 비어 있으면 Threshold Decrease를 검토한다.
- Expected Document가 Threshold 아래에 있으면 Decrease를 검토한다.
- Threshold를 낮추면 더 많은 Chunk가 검색될 수 있다.
- Threshold를 낮추면 Recall이 올라갈 수 있다.
- Threshold를 낮추면 Precision이 낮아질 수 있다.
- Threshold Decrease 후 노이즈 증가 여부를 확인해야 한다.

---

### [실무]

Threshold Decrease Retest 예시:

```md
# Threshold Decrease Retest

## Query

Expected Document가 검색 결과에 없어

## Before

- Threshold: 0.75
- Expected Document Score: 0.69
- Retrieved: 2
- Hit@5: Fail

## After

- Threshold: 0.65
- Expected Document Rank: 4
- Hit@5: Pass
- Precision@5: 0.60

## Result

- Recall improved
- Precision monitoring required
```

Threshold Decrease 주의:

| 위험                 | 대응                  |
| -------------------- | --------------------- |
| 노이즈 증가          | Reranking 적용        |
| Context 과다         | Final Top-K 제한      |
| 낮은 품질 Chunk 포함 | Metadata Filter 적용  |
| 답변 흔들림          | Context Assembly 강화 |

---

### [FAQ]

Q. Threshold Decrease는 뭐야?

A. 필요한 문서가 제외될 때 최소 유사도 기준을 낮추는 조정이다.

Q. Threshold는 언제 낮춰?

A. 검색 결과가 비어 있거나 Expected Document가 점수 기준 때문에 제외될 때 낮춘다.

Q. Threshold를 낮추면 뭐가 좋아져?

A. 더 많은 문서가 검색되어 Recall이 좋아질 수 있다.

Q. Threshold를 낮추면 뭐가 나빠져?

A. 관련 없는 Chunk가 늘어 Precision이 낮아질 수 있다.

Q. Threshold를 낮춘 후 무엇을 해야 해?

A. Precision, Recall, 노이즈 비율, 답변 Groundedness를 재평가해야 한다.

---

# 4. Reranking Optimization

## 4.1 Reranking 기본 개념

### [개념]

Reranking은 초기 Retrieval 결과를 다시 평가해 관련도 높은 Chunk를 상위로 재정렬하는 과정이다.

Reranking은 Expected Document가 검색 결과에 포함되지만 순위가 낮을 때 효과적이다.

```text
Initial Retrieval Top-N
→ Reranker Scoring
→ Reorder Chunks
→ Select Final Top-K
→ Context Assembly
```

---

### [핵심]

- Reranking은 검색 결과 순위를 개선한다.
- 초기 검색에서 넓게 후보를 가져온 뒤 재정렬한다.
- Expected Document가 낮은 Rank에 있을 때 유용하다.
- MRR과 Ranking Quality 개선에 도움된다.
- Reranking은 노이즈를 줄이는 데 도움될 수 있다.
- Reranking은 검색 누락 자체를 해결하지 못한다.
- Candidate Top-N과 Final Top-K를 분리할 수 있다.

---

### [실무]

Reranking 적용 예시:

```md
# Reranking Example

## Query

Hallucination은 어떻게 확인해?

## Initial Retrieval Top-5

| Rank | Document                     | Relevant |
| ---: | ---------------------------- | -------- |
|    1 | Prompt_Output_Control.md     | Partial  |
|    2 | Vector_Search.md             | No       |
|    3 | RAG_Generation_Evaluation.md | Yes      |
|    4 | RAG_Core.md                  | Partial  |
|    5 | Metadata_Optimization.md     | No       |

## After Reranking

| Rank | Document                     | Relevant |
| ---: | ---------------------------- | -------- |
|    1 | RAG_Generation_Evaluation.md | Yes      |
|    2 | RAG_Core.md                  | Partial  |
|    3 | Prompt_Output_Control.md     | Partial  |

## Result

- Hit@1 improved
- MRR improved
```

Reranking 적용 판단:

| 상태                                   | Reranking 적합성        |
| -------------------------------------- | ----------------------- |
| 기대 문서가 Top-K에 있으나 순위 낮음   | 높음                    |
| 관련 문서와 노이즈가 섞임              | 높음                    |
| Expected Document가 전혀 검색되지 않음 | 낮음                    |
| Query가 모호함                         | Query Rewrite 선행      |
| Chunk가 너무 혼합됨                    | Chunk Optimization 선행 |

---

### [FAQ]

Q. Reranking은 뭐야?

A. 초기 검색 결과를 다시 평가해 관련도 높은 Chunk를 상위로 재정렬하는 과정이다.

Q. Reranking은 언제 유용해?

A. 기대 문서가 검색되지만 순위가 낮거나 노이즈가 섞일 때 유용하다.

Q. Reranking이 검색 누락을 해결해?

A. 아니다. 초기 검색 결과에 없는 문서는 재정렬할 수 없다.

Q. Reranking은 어떤 지표를 개선해?

A. MRR, Ranking Quality, Hit@1 개선에 도움될 수 있다.

Q. Reranking 전에 무엇을 확인해야 해?

A. Expected Document가 초기 Retrieval 후보 안에 포함되는지 확인해야 한다.

---

## 4.2 Candidate Top-N and Final Top-K

### [개념]

Candidate Top-N은 Reranking 전에 넓게 가져오는 초기 검색 후보 개수다.

Final Top-K는 Reranking 후 LLM Context에 전달할 최종 Chunk 개수다.

---

### [핵심]

- Candidate Top-N은 Recall 확보를 위한 후보 집합이다.
- Final Top-K는 Context 품질을 위한 최종 선택이다.
- Candidate Top-N은 Final Top-K보다 크게 설정할 수 있다.
- Reranking은 Candidate Top-N 안에서만 작동한다.
- Candidate가 너무 작으면 필요한 문서가 후보에 없다.
- Final Top-K가 너무 크면 노이즈가 늘어난다.
- Candidate와 Final을 분리하면 Recall과 Precision 균형에 유리하다.

---

### [실무]

Candidate / Final 설정 예시:

| 설정                 | 목적                  |
| -------------------- | --------------------- |
| Candidate Top-N = 20 | 필요한 문서 후보 확보 |
| Reranking 적용       | 관련도 기준 재정렬    |
| Final Top-K = 5      | LLM Context 품질 유지 |

Flow:

```text
Retrieve Candidate Top-20
→ Rerank Top-20
→ Select Final Top-5
→ Deduplicate
→ Assemble Context
```

판단 기준:

| 증상                                                  | 조정                                   |
| ----------------------------------------------------- | -------------------------------------- |
| Expected Document가 Candidate에 없음                  | Candidate Top-N 증가                   |
| Expected Document는 Candidate에 있으나 Final에서 제외 | Reranker 기준 확인                     |
| Final Context에 노이즈 많음                           | Final Top-K 감소                       |
| Final Context에 근거 부족                             | Final Top-K 증가 또는 Compression 개선 |
| 처리 비용 과다                                        | Candidate Top-N 감소                   |

---

### [FAQ]

Q. Candidate Top-N은 뭐야?

A. Reranking 전에 넓게 가져오는 초기 검색 후보 개수다.

Q. Final Top-K는 뭐야?

A. Reranking 후 LLM Context에 전달할 최종 Chunk 개수다.

Q. Candidate Top-N과 Final Top-K를 왜 나눠?

A. 후보는 넓게 확보하고 최종 Context는 정제하기 위해서다.

Q. Expected Document가 Candidate에 없으면 Reranking으로 해결돼?

A. 안 된다. Candidate 안에 없는 문서는 Reranking할 수 없다.

Q. Final Top-K가 너무 크면 어떻게 돼?

A. 노이즈가 늘고 Context Budget을 낭비할 수 있다.

---

## 4.3 Reranking Failure

### [개념]

Reranking Failure는 Reranking 적용 후에도 관련 문서가 상위에 배치되지 않거나, 오히려 관련 문서가 밀려나는 실패다.

Reranking Failure는 Reranker 기준, Query 표현, Chunk 품질, Candidate 구성 문제로 발생할 수 있다.

---

### [핵심]

- Candidate에 Expected Document가 없으면 Reranking이 불가능하다.
- Reranker가 Query Intent를 잘못 판단할 수 있다.
- Chunk에 여러 개념이 섞이면 재정렬 품질이 낮아진다.
- Query가 모호하면 Reranking도 불안정하다.
- 관련 문서가 Final Top-K에서 제외될 수 있다.
- Reranking 후 Regression Check가 필요하다.

---

### [실무]

Reranking Failure 진단표:

| 실패 증상                            | 원인                | 조치                          |
| ------------------------------------ | ------------------- | ----------------------------- |
| Expected Document가 Candidate에 없음 | 초기 Retrieval 실패 | Candidate 증가, Query Rewrite |
| Candidate에는 있으나 Final에서 제외  | Reranker 판단 실패  | Reranker 설정, Query 개선     |
| 노이즈가 상위로 올라옴               | Chunk 혼합          | Chunk 분리                    |
| 순위가 매번 흔들림                   | Query 모호          | Intent 명확화                 |
| 비용 증가                            | Candidate 과다      | Candidate 축소                |
| 관련 문서가 밀림                     | Keyword 약함        | Header / FAQ 보강             |

Reranking Retest 예시:

```md
# Reranking Retest

## Query

검색 결과는 맞는데 순서가 이상해

## Before Reranking

- Expected Document Rank: 5
- Hit@1: Fail

## After Reranking

- Expected Document Rank: 1
- Hit@1: Pass

## Regression Check

- Core Query Set: Pass
```

---

### [FAQ]

Q. Reranking Failure는 뭐야?

A. Reranking 후에도 관련 문서가 상위에 오지 않거나 오히려 밀려나는 실패다.

Q. Reranking이 안 먹히는 이유는 뭐야?

A. Candidate에 기대 문서가 없거나 Query Intent, Chunk 품질, Reranker 기준이 맞지 않을 수 있다.

Q. Reranking 전 가장 먼저 확인할 것은 뭐야?

A. Expected Document가 Candidate Top-N 안에 포함되는지 확인해야 한다.

Q. Reranking 후에도 순위가 낮으면 어떻게 해?

A. Query Rewrite, Header 보강, Chunk 분리, Reranker 설정을 점검한다.

Q. Reranking도 Regression Check가 필요해?

A. 필요하다. 일부 Query의 순위가 나빠질 수 있기 때문이다.

---

# 5. Context Optimization

## 5.1 Context Assembly

### [개념]

Context Assembly는 검색된 Chunk를 LLM 답변에 사용할 수 있도록 정렬, 필터링, 병합해 Prompt Context로 구성하는 과정이다.

검색된 결과를 모두 넣는 것이 항상 좋은 것은 아니다.

```text
Retrieved Chunks
→ Remove Low Relevance
→ Deduplicate
→ Sort by Relevance / Priority
→ Resolve Conflict
→ Build Prompt Context
```

---

### [핵심]

- Context Assembly는 LLM 입력 Context를 구성한다.
- 관련도 낮은 Chunk는 제거한다.
- 중복 Chunk는 제거한다.
- 핵심 근거 Chunk를 우선 배치한다.
- Source Priority를 적용한다.
- 충돌하는 문서가 있으면 우선순위를 정한다.
- Context 순서는 답변 품질에 영향을 줄 수 있다.
- Context에 근거가 부족하면 부족하다고 답해야 한다.

---

### [실무]

Context Assembly 기준:

| 단계 | 작업                                      |
| ---- | ----------------------------------------- |
| 1    | Retrieved Chunks 확인                     |
| 2    | Low Relevance Chunk 제거                  |
| 3    | Duplicate Chunk 제거                      |
| 4    | Expected Document 우선 배치               |
| 5    | Domain Rules / Master Rules 우선순위 적용 |
| 6    | 충돌 Context 표시                         |
| 7    | Token Budget 내 Context 구성              |
| 8    | Grounding Prompt와 연결                   |

Context Assembly 예시:

```md
# Context Assembly

## Input Chunks

- Chunk A: Groundedness 정의
- Chunk B: Faithfulness 정의
- Chunk C: 관련 없는 Vector DB 설정
- Chunk D: Groundedness 정의 중복

## Action

- Keep: Chunk A, Chunk B
- Remove: Chunk C
- Deduplicate: Chunk D
- Order: Chunk A → Chunk B

## Result

- Context supports comparison answer
```

---

### [FAQ]

Q. Context Assembly는 뭐야?

A. 검색된 Chunk를 LLM 답변에 사용할 수 있도록 정렬, 필터링, 병합하는 과정이다.

Q. 검색 결과를 전부 넣으면 좋은 거야?

A. 아니다. 관련 없는 Chunk와 중복 Chunk는 답변 품질을 낮출 수 있다.

Q. Context 순서가 답변에 영향을 줘?

A. 영향을 줄 수 있다. 핵심 근거와 우선순위 높은 문서를 앞에 배치하는 것이 좋다.

Q. 충돌하는 Context가 있으면 어떻게 해?

A. Master Rules, Domain Rules, 최신 문서, Source Priority 기준으로 해결한다.

Q. Context에 근거가 부족하면 어떻게 답해야 해?

A. 문서 기준 정보가 부족하다고 명확히 답해야 한다.

---

## 5.2 Deduplication

### [개념]

Deduplication은 검색 결과에서 동일하거나 거의 같은 의미의 Chunk를 제거하는 과정이다.

중복 Context는 Token Budget을 낭비하고 LLM 답변을 반복적으로 만들 수 있다.

---

### [핵심]

- Deduplication은 중복 Chunk를 제거한다.
- 같은 문서의 Overlap 중복을 줄인다.
- 유사한 FAQ 반복을 정리한다.
- Token Budget 낭비를 줄인다.
- 다양한 근거 Chunk를 포함할 여지를 만든다.
- 중복 제거 후 핵심 근거가 빠지지 않았는지 확인한다.
- Deduplication은 Context Assembly 전에 수행하는 것이 좋다.

---

### [실무]

Deduplication 판단 기준:

| 중복 유형             | 처리                             |
| --------------------- | -------------------------------- |
| 완전 동일 Chunk       | 하나만 유지                      |
| Overlap으로 일부 중복 | 더 완전한 Chunk 유지             |
| FAQ와 본문 중복       | 근거가 더 명확한 Chunk 우선      |
| 구버전 / 신버전 중복  | 최신 Version 우선                |
| 같은 개념 다른 표현   | 질문 의도와 더 가까운 Chunk 우선 |

Deduplication 예시:

```md
# Deduplication Example

## Retrieved

- Chunk 1: Top-K 정의
- Chunk 2: Top-K 정의 + 조정 기준
- Chunk 3: Top-K 조정 FAQ
- Chunk 4: Metadata Filter

## Keep

- Chunk 2
- Chunk 3
- Chunk 4

## Remove

- Chunk 1

## Reason

- Chunk 2가 Chunk 1보다 완전한 근거를 포함
```

---

### [FAQ]

Q. Deduplication은 뭐야?

A. 검색 결과에서 동일하거나 거의 같은 의미의 Chunk를 제거하는 과정이다.

Q. 중복 Context는 왜 문제야?

A. Token Budget을 낭비하고 답변 반복이나 근거 편향을 만들 수 있다.

Q. 중복 Chunk는 무조건 삭제해?

A. 아니다. 더 완전하고 질문 의도와 가까운 Chunk를 남긴다.

Q. FAQ와 본문이 중복되면 무엇을 남겨?

A. 질문 의도와 근거 명확성이 높은 Chunk를 우선한다.

Q. Deduplication 후 무엇을 확인해?

A. 핵심 근거 Chunk가 빠지지 않았는지 확인해야 한다.

---

## 5.3 Relevance Ordering

### [개념]

Relevance Ordering은 Context에 포함할 Chunk를 질문 의도와 근거 중요도에 따라 정렬하는 과정이다.

관련도가 높은 Chunk를 앞에 배치하면 LLM이 핵심 근거를 우선 반영할 가능성이 높아진다.

---

### [핵심]

- 관련도 높은 Chunk를 앞에 배치한다.
- Expected Document Chunk를 우선 배치한다.
- Domain Rules와 Master Rules는 충돌 시 우선한다.
- 최신 Version 문서를 우선할 수 있다.
- 정의 → 판단 기준 → 예시 → FAQ 순서가 유용할 수 있다.
- 비교 질문은 비교 대상 Chunk를 인접 배치한다.
- 문제 해결 질문은 증상 → 원인 → 해결 순서가 좋다.

---

### [실무]

Relevance Ordering 예시:

```md
# Relevance Ordering

## Query

Precision과 Recall 차이는?

## Candidate Chunks

- Chunk A: Precision 정의
- Chunk B: Recall 정의
- Chunk C: Top-K 조정 기준
- Chunk D: Vector DB 내부 알고리즘

## Context Order

1. Chunk A
2. Chunk B
3. Chunk C

## Removed

- Chunk D

## Reason

- Query Intent는 metric comparison
- Precision과 Recall 정의를 먼저 배치
- Top-K 영향은 보조 근거로 배치
```

Query 유형별 Context Order:

| Query 유형 | 권장 순서               |
| ---------- | ----------------------- |
| 정의 질문  | 정의 → 핵심             |
| 비교 질문  | A 정의 → B 정의 → 차이  |
| 절차 질문  | Step 순서               |
| 문제 해결  | 증상 → 원인 → 해결      |
| 오해 교정  | 오해 부정 → 조건부 기준 |
| 평가 질문  | 지표 → 판단 기준 → 예시 |

---

### [FAQ]

Q. Relevance Ordering은 뭐야?

A. Context Chunk를 질문 의도와 근거 중요도에 따라 정렬하는 과정이다.

Q. Context 순서가 왜 중요해?

A. LLM이 앞쪽 Context를 더 강하게 반영할 수 있기 때문이다.

Q. 비교 질문에서는 Context를 어떻게 배치해?

A. 비교 대상의 정의와 차이점 Chunk를 인접하게 배치한다.

Q. 문제 해결 질문에서는 Context를 어떻게 배치해?

A. 증상, 원인, 해결 순서로 배치하는 것이 좋다.

Q. 관련 없는 Chunk는 뒤에 두면 돼?

A. 아니다. 가능하면 Context에서 제거해야 한다.

---

## 5.4 Source Priority and Conflict Resolution

### [개념]

Source Priority는 여러 문서가 충돌할 때 어떤 근거를 우선할지 정하는 기준이다.

Conflict Resolution은 서로 다른 Context가 충돌할 때 답변 기준을 선택하거나 불확실성을 표시하는 과정이다.

---

### [핵심]

- Master Rules는 Domain Rules보다 우선한다.
- Domain Rules는 Part 문서보다 우선한다.
- 최신 Project Progress는 오래된 진행 문서보다 우선한다.
- 최신 Version 문서를 우선한다.
- Source가 불명확한 문서는 낮은 우선순위로 둔다.
- 충돌이 해결되지 않으면 확정 답변을 피한다.
- 충돌 사실을 표시하고 확인 가능한 범위만 답한다.

---

### [실무]

Source Priority 기준:

| 우선순위 | Source                     |
| -------: | -------------------------- |
|        1 | MASTER_RAG_RULES           |
|        2 | DOMAIN_RULES               |
|        3 | PROJECT_PROGRESS 최신본    |
|        4 | 같은 Domain 최신 Part 문서 |
|        5 | 오래된 Part 문서           |
|        6 | 예시 / 임시 메모           |

Conflict Resolution 예시:

```md
# Conflict Resolution

## Conflict

- Old Document: FAQ Section optional
- Master Rules: FAQ required

## Priority

- MASTER_RAG_RULES 우선

## Answer

- FAQ는 필수 Section으로 적용한다.
```

불확실성 처리:

```text
문서 기준으로는 두 Context가 충돌한다.
우선순위상 MASTER_RAG_RULES를 따른다.
다만 Part 문서의 세부 예시는 최신화가 필요하다.
```

---

### [FAQ]

Q. Source Priority는 뭐야?

A. 여러 문서가 충돌할 때 어떤 근거를 우선할지 정하는 기준이다.

Q. Master Rules와 Domain Rules가 충돌하면 무엇을 따라?

A. Master Rules를 우선한다.

Q. Domain Rules와 Part 문서가 충돌하면 무엇을 따라?

A. Domain Rules를 우선한다.

Q. 오래된 문서와 최신 문서가 충돌하면?

A. 최신 Version과 UpdatedAt을 우선 확인한다.

Q. 충돌을 해결할 수 없으면 어떻게 답해?

A. 확정하지 않고 충돌 사실과 확인 가능한 범위를 명확히 표시한다.

---

## 5.5 Context Compression

### [개념]

Context Compression은 긴 Retrieved Context를 LLM Token Budget 안에 맞게 핵심 근거 중심으로 줄이는 과정이다.

Compression은 핵심 조건, 예외, 판단 기준을 보존해야 한다.

---

### [핵심]

- Compression은 Token Budget 절약에 사용된다.
- 핵심 근거 Claim을 유지해야 한다.
- 조건과 예외를 제거하면 Faithfulness가 낮아진다.
- Source와 Section 정보를 유지하는 것이 좋다.
- 중복 설명을 제거한다.
- 관련 없는 배경 설명을 제거한다.
- 압축 후 Answer Completeness를 확인한다.

---

### [실무]

Context Compression 기준:

| 제거 가능         | 보존 필요 |
| ----------------- | --------- |
| 반복 설명         | 정의      |
| 장문 배경         | 판단 기준 |
| 관련 없는 예시    | 조건      |
| 중복 FAQ          | 예외      |
| 낮은 관련도 Chunk | Source    |
| 일반론            | 필수 절차 |

Compression 예시:

```md
# Before Compression

Top-K는 검색 결과 개수다. Top-K를 늘리면 더 많은 문서를 가져온다.
그 결과 필요한 문서가 포함될 가능성이 높아질 수 있다.
하지만 관련 없는 문서도 함께 들어와 Precision이 낮아질 수 있다.
따라서 Top-K는 평가 결과에 따라 조정해야 한다.

# After Compression

Top-K는 검색 결과 개수다.
필요 문서가 누락되면 증가를 검토하고, 노이즈가 많으면 감소를 검토한다.
Top-K 증가는 Recall을 높일 수 있지만 Precision을 낮출 수 있다.
```

---

### [FAQ]

Q. Context Compression은 뭐야?

A. 긴 Retrieved Context를 Token Budget 안에 맞게 핵심 근거 중심으로 줄이는 과정이다.

Q. Compression에서 무엇을 보존해야 해?

A. 정의, 판단 기준, 조건, 예외, Source 정보를 보존해야 한다.

Q. Compression에서 무엇을 제거해도 돼?

A. 반복 설명, 관련 없는 배경, 중복 FAQ, 낮은 관련도 Chunk를 제거할 수 있다.

Q. Compression이 잘못되면 어떤 문제가 생겨?

A. 조건이나 예외가 빠져 Faithfulness와 Completeness가 낮아질 수 있다.

Q. Compression 후 무엇을 확인해?

A. 핵심 근거가 유지되었는지, Answer Completeness가 충분한지 확인한다.

---

# 6. Token Budget Optimization

## 6.1 Token Budget 기본 개념

### [개념]

Token Budget은 LLM에 전달할 수 있는 Query, Context, Instruction, Answer 공간의 총 토큰 한계다.

RAG에서는 Token Budget 안에서 가장 관련도 높은 근거를 선택해야 한다.

---

### [핵심]

- Context가 길면 비용과 지연이 증가한다.
- Context가 길어도 답변 품질이 항상 좋아지는 것은 아니다.
- Token Budget 안에 핵심 근거를 우선 배치한다.
- 중복 Context는 제거한다.
- 낮은 관련도 Chunk는 제거한다.
- 필요한 경우 Context Compression을 적용한다.
- 답변 생성 공간도 남겨야 한다.

---

### [실무]

Token Budget 구성 예시:

| 영역               | 설명           |
| ------------------ | -------------- |
| System Instruction | 답변 규칙      |
| User Query         | 사용자 질문    |
| Retrieved Context  | 검색 근거      |
| Formatting Rule    | 출력 형식      |
| Answer Budget      | 생성 답변 공간 |

Token Budget 조정 기준:

| 문제               | 조치                             |
| ------------------ | -------------------------------- |
| Context가 너무 김  | Deduplication, Compression       |
| 핵심 근거 누락     | Relevance Ordering 재조정        |
| 답변이 중간에 끊김 | Context 축소, Answer Budget 확보 |
| 노이즈가 많음      | Threshold, Reranking, Filter     |
| 비용 / 지연 증가   | Candidate / Final Top-K 조정     |

---

### [FAQ]

Q. Token Budget은 뭐야?

A. LLM에 전달할 수 있는 Query, Context, Instruction, Answer 공간의 총 토큰 한계다.

Q. Context를 길게 넣으면 항상 좋아?

A. 아니다. 노이즈와 중복이 많으면 답변 품질이 낮아질 수 있다.

Q. Token Budget을 아끼려면 어떻게 해?

A. Deduplication, Relevance Ordering, Context Compression을 적용한다.

Q. 답변 생성 공간도 고려해야 해?

A. 필요하다. Context가 너무 길면 답변을 생성할 공간이 부족해질 수 있다.

Q. Token Budget 부족이 생기면 무엇을 줄여?

A. 관련도 낮은 Chunk, 중복 Context, 장문 배경 설명을 줄인다.

---

## 6.2 Context Window vs Context Quality

### [개념]

Context Window는 LLM이 한 번에 처리할 수 있는 최대 입력 길이다.

Context Quality는 입력된 Context가 질문에 적합한 근거로 구성되었는지의 품질이다.

Context Window가 커도 Context Quality가 낮으면 답변 품질은 낮다.

---

### [핵심]

- 큰 Context Window는 많은 문서를 넣을 수 있게 한다.
- 많은 문서를 넣는 것이 항상 좋은 것은 아니다.
- Context Quality가 답변 품질에 직접 영향을 준다.
- 노이즈 Context는 Hallucination을 유발할 수 있다.
- 중복 Context는 Token Budget을 낭비한다.
- 관련도 높은 근거를 우선 선택해야 한다.
- Context Window 확장보다 Retrieval 품질 개선이 우선일 수 있다.

---

### [실무]

Context Window와 Context Quality 비교:

| 비교      | Context Window        | Context Quality                  |
| --------- | --------------------- | -------------------------------- |
| 의미      | 입력 가능한 최대 길이 | 근거의 관련도와 정합성           |
| 개선 방법 | 모델 / 설정 변경      | Retrieval / Reranking / Assembly |
| 위험      | 비용 증가             | 낮으면 오답 증가                 |
| 오해      | 크면 무조건 좋음      | 작아도 핵심 근거면 충분          |
| 평가      | Token 수              | Groundedness, Faithfulness       |

판단 기준:

```text
Context Window는 충분한데 답변이 틀림
→ Context Quality 문제 가능

Context Window가 부족해 근거가 잘림
→ Token Budget / Compression 문제 가능

Context가 많지만 노이즈가 많음
→ Precision / Assembly 문제 가능
```

---

### [FAQ]

Q. Context Window는 뭐야?

A. LLM이 한 번에 처리할 수 있는 최대 입력 길이다.

Q. Context Quality는 뭐야?

A. 입력된 Context가 질문에 적합한 근거로 구성되었는지의 품질이다.

Q. Context Window가 크면 RAG 품질이 좋아져?

A. 반드시 그렇지는 않다. 관련 없는 Context가 많으면 품질이 낮아질 수 있다.

Q. Context Quality는 어떻게 높여?

A. Reranking, Deduplication, Relevance Ordering, Context Assembly를 개선한다.

Q. 답변이 틀릴 때 Context Window부터 늘리면 돼?

A. 먼저 Retrieval 품질과 Context Quality를 확인해야 한다.

---

# 7. End-to-End Optimization Flow

## 7.1 Retrieval to Context Optimization Flow

### [개념]

Retrieval to Context Optimization Flow는 검색 후보 생성부터 최종 Context 구성까지 품질을 개선하는 전체 절차다.

이 Flow는 Retrieval Evaluation과 Generation Evaluation을 연결한다.

---

### [핵심]

- Query를 최적화한다.
- Candidate Retrieval을 수행한다.
- Top-K와 Threshold를 조정한다.
- Reranking으로 순위를 개선한다.
- Deduplication으로 중복을 제거한다.
- Relevance Ordering으로 근거 순서를 정한다.
- Context Compression으로 Token Budget을 맞춘다.
- Groundedness와 Faithfulness를 검증한다.
- 실패를 Report에 기록한다.

---

### [실무]

End-to-End Optimization Flow:

```text
Raw Query
→ Intent Extraction
→ Query Rewrite / Expansion
→ Retrieve Candidate Top-N
→ Apply Similarity Threshold
→ Rerank Candidate
→ Select Final Top-K
→ Deduplicate
→ Apply Source Priority
→ Compress Context
→ Generate Answer
→ Check Groundedness
→ Check Faithfulness
→ Record Report
→ Retest
```

Flow별 주요 지표:

| 단계                | 주요 지표                   |
| ------------------- | --------------------------- |
| Query Optimization  | Hit@K 변화                  |
| Candidate Retrieval | Recall                      |
| Threshold           | Precision / Recall          |
| Reranking           | MRR / Ranking Quality       |
| Final Top-K         | Context Precision           |
| Deduplication       | Token 절약                  |
| Context Assembly    | Groundedness                |
| Compression         | Completeness / Faithfulness |
| Answer Generation   | Relevance / Hallucination   |

---

### [FAQ]

Q. End-to-End Optimization Flow는 뭐야?

A. Query 개선부터 Context 구성과 답변 검증까지 연결한 전체 RAG 최적화 절차다.

Q. Retrieval Optimization과 Context Optimization은 연결돼?

A. 연결된다. 검색 결과가 좋아도 Context Assembly가 나쁘면 답변 품질이 낮아질 수 있다.

Q. Reranking은 어느 단계에서 적용해?

A. Candidate Retrieval 이후 Final Top-K 선택 전에 적용한다.

Q. Deduplication은 언제 해?

A. Reranking 후 또는 Context Assembly 전에 수행한다.

Q. 최종적으로 무엇을 평가해?

A. Hit@K, Precision, Recall, Ranking Quality, Groundedness, Faithfulness를 함께 평가한다.

---

## 7.2 Optimization Report 연결

### [개념]

Optimization Report는 Top-K, Threshold, Reranking, Context Assembly 조정 결과를 기록하는 문서다.

Optimization Report는 RAG Quality Report와 연결되어야 한다.

---

### [핵심]

- 조정 전 설정을 기록한다.
- 조정 후 설정을 기록한다.
- 변경 이유를 기록한다.
- 개선 대상 Query를 기록한다.
- Hit@K 변화를 기록한다.
- Precision / Recall 변화를 기록한다.
- Generation 품질 변화를 기록한다.
- Regression 여부를 기록한다.
- 다음 조치를 기록한다.

---

### [실무]

Optimization Report 예시:

```md
# Optimization Report

## Target

- Query: 문서에 있는데 검색이 안 돼
- Failure Type: Document Miss
- Expected Document: Part02_Retrieval_Evaluation

## Before

- Top-K: 5
- Threshold: 0.72
- Reranking: Off
- Hit@5: Fail
- Precision@5: 0.40
- Recall@5: 0.00

## Change

- Top-K: 10
- Threshold: 0.65
- Reranking: On
- Reason: Expected Document score below threshold and low ranking

## After

- Hit@5: Pass
- Expected Document Rank: 2
- Precision@5: 0.70
- Recall@5: 0.80
- Groundedness: Pass

## Regression

- Core Query Set: Pass
- Retrieval Query Set: Pass

## Next Action

- Header / FAQ 추가 보강
```

---

### [FAQ]

Q. Optimization Report는 뭐야?

A. Top-K, Threshold, Reranking, Context Assembly 조정 결과를 기록하는 문서다.

Q. Optimization Report에는 무엇을 기록해?

A. 변경 전후 설정, 이유, 지표 변화, Regression 여부, 다음 조치를 기록한다.

Q. Optimization Report는 왜 필요해?

A. 어떤 조정이 품질 개선에 효과가 있었는지 추적하기 위해 필요하다.

Q. Optimization Report는 Quality Report와 연결해야 해?

A. 연결해야 한다. 실패 원인과 개선 조치의 이력을 관리하기 위해서다.

Q. 조정 후 결과가 나빠지면 어떻게 해?

A. 변경을 되돌리거나 Failure Type을 다시 분석하고 다른 Target을 개선한다.

---

# 8. Common Mistakes

## 8.1 Top-K / Threshold / Context Optimization 실수

### [개념]

Top-K / Threshold / Reranking / Context Optimization에서 가장 흔한 실수는 검색 결과의 품질을 확인하지 않고 설정값만 크게 또는 작게 바꾸는 것이다.

Retrieval 설정은 반드시 Golden Query 평가 결과와 연결해서 조정해야 한다.

---

### [핵심]

- Top-K를 무조건 크게 설정한다.
- Threshold를 감으로 조정한다.
- Precision / Recall 변화를 기록하지 않는다.
- Expected Document가 Candidate에 없는 상태에서 Reranking을 기대한다.
- Reranking 후 Regression Check를 하지 않는다.
- 중복 Context를 그대로 넣는다.
- 관련 없는 Context를 모두 LLM에 전달한다.
- Source Priority 없이 충돌 문서를 섞는다.
- Compression 과정에서 조건과 예외를 제거한다.
- Token Budget을 고려하지 않는다.
- 조정 결과를 Report에 기록하지 않는다.

---

### [실무]

실수 방지 Checklist:

```md
### [Checklist]

- [ ] Top-K 변경 전 Expected Document Rank를 확인했는가?
- [ ] Top-K 변경 후 Precision / Recall을 비교했는가?
- [ ] Threshold 변경 전 Score Distribution을 확인했는가?
- [ ] Threshold 변경 후 빈 검색 결과가 발생하지 않는가?
- [ ] Reranking 전 Candidate Top-N에 Expected Document가 있는가?
- [ ] Final Top-K에 핵심 근거가 포함되는가?
- [ ] Deduplication을 수행했는가?
- [ ] Context Order가 Query Intent와 맞는가?
- [ ] Source Priority를 적용했는가?
- [ ] Compression 후 조건과 예외가 유지되는가?
- [ ] Token Budget 안에 답변 생성 공간이 남는가?
- [ ] Regression Check를 수행했는가?
- [ ] Optimization Report를 작성했는가?
```

---

### [FAQ]

Q. Top-K / Threshold 조정에서 가장 흔한 실수는 뭐야?

A. 평가 결과 없이 감으로 값을 크게 또는 작게 바꾸는 것이다.

Q. Top-K를 무조건 크게 하면 왜 문제야?

A. 노이즈 Chunk가 늘어 Precision과 답변 품질이 낮아질 수 있다.

Q. Threshold를 무조건 높이면 왜 문제야?

A. 필요한 문서가 제외되어 Recall이 낮아질 수 있다.

Q. Reranking에 대한 흔한 오해는 뭐야?

A. 초기 검색에 없는 문서도 Reranking으로 찾을 수 있다고 생각하는 것이다.

Q. Context Compression에서 가장 위험한 실수는 뭐야?

A. 조건과 예외를 제거해 답변이 Context를 왜곡하게 만드는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Retrieval Control은 뭐야?
A. Top-K, Threshold, Reranking, Context Assembly를 조정해 검색 결과를 답변에 적합하게 만드는 과정이다.

Q. Top-K는 뭐야?
A. Retrieval 단계에서 검색 결과로 가져올 상위 Chunk 개수다.

Q. Top-K를 높이면 뭐가 좋아져?
A. 필요한 문서가 포함될 가능성이 커져 Recall이 올라갈 수 있다.

Q. Top-K를 높이면 뭐가 나빠져?
A. 관련 없는 Chunk도 함께 들어와 Precision이 낮아질 수 있다.

Q. Top-K는 언제 늘려?
A. Expected Document나 Expected Chunk가 검색 결과 밖에 있을 때 늘리는 것을 검토한다.

Q. Top-K는 언제 줄여?
A. 관련 없는 Chunk가 많이 검색되고 Expected Document는 상위에 있을 때 줄일 수 있다.

Q. Top-K를 늘렸는데도 문서가 안 나오면?
A. Query, Header, FAQ, Metadata, Reindex 문제를 확인해야 한다.

Q. Top-K를 줄이면 뭐가 좋아져?
A. 노이즈가 줄어 Precision이 높아질 수 있다.

Q. Similarity Threshold는 뭐야?
A. 검색 결과로 인정할 최소 유사도 기준이다.

Q. Threshold를 높이면 뭐가 좋아져?
A. 관련 없는 Chunk가 줄어 Precision이 좋아질 수 있다.

Q. Threshold를 높이면 뭐가 나빠져?
A. 필요한 문서가 제외되어 Recall이 낮아질 수 있다.

Q. Threshold를 낮추면 뭐가 좋아져?
A. 더 많은 문서가 검색되어 Recall이 높아질 수 있다.

Q. Threshold를 낮추면 뭐가 나빠져?
A. 관련 없는 문서가 늘어나 Precision이 낮아질 수 있다.

Q. Threshold는 언제 높여?
A. 검색 결과에 관련 없는 Chunk가 많이 섞일 때 높이는 것을 검토한다.

Q. Threshold는 언제 낮춰?
A. 검색 결과가 비어 있거나 Expected Document가 점수 기준 때문에 제외될 때 낮춘다.

Q. Reranking은 뭐야?
A. 초기 검색 결과를 다시 평가해 관련도 높은 Chunk를 상위로 재정렬하는 과정이다.

Q. Reranking은 언제 유용해?
A. 기대 문서가 검색되지만 순위가 낮거나 노이즈가 섞일 때 유용하다.

Q. Reranking이 검색 누락을 해결해?
A. 아니다. 초기 검색 결과에 없는 문서는 재정렬할 수 없다.

Q. Reranking은 어떤 지표를 개선해?
A. MRR, Ranking Quality, Hit@1 개선에 도움될 수 있다.

Q. Candidate Top-N은 뭐야?
A. Reranking 전에 넓게 가져오는 초기 검색 후보 개수다.

Q. Final Top-K는 뭐야?
A. Reranking 후 LLM Context에 전달할 최종 Chunk 개수다.

Q. Candidate Top-N과 Final Top-K를 왜 나눠?
A. 후보는 넓게 확보하고 최종 Context는 정제하기 위해서다.

Q. Expected Document가 Candidate에 없으면 Reranking으로 해결돼?
A. 안 된다. Candidate 안에 없는 문서는 Reranking할 수 없다.

Q. Reranking Failure는 뭐야?
A. Reranking 후에도 관련 문서가 상위에 오지 않거나 오히려 밀려나는 실패다.

Q. Reranking이 안 먹히는 이유는?
A. Candidate에 기대 문서가 없거나 Query Intent, Chunk 품질, Reranker 기준이 맞지 않을 수 있다.

Q. Context Assembly는 뭐야?
A. 검색된 Chunk를 LLM 답변에 사용할 수 있도록 정렬, 필터링, 병합하는 과정이다.

Q. 검색 결과를 전부 넣으면 좋은 거야?
A. 아니다. 관련 없는 Chunk와 중복 Chunk는 답변 품질을 낮출 수 있다.

Q. Context 순서가 답변에 영향을 줘?
A. 영향을 줄 수 있다. 핵심 근거와 우선순위 높은 문서를 앞에 배치하는 것이 좋다.

Q. Deduplication은 뭐야?
A. 검색 결과에서 동일하거나 거의 같은 의미의 Chunk를 제거하는 과정이다.

Q. 중복 Context는 왜 문제야?
A. Token Budget을 낭비하고 답변 반복이나 근거 편향을 만들 수 있다.

Q. Relevance Ordering은 뭐야?
A. Context Chunk를 질문 의도와 근거 중요도에 따라 정렬하는 과정이다.

Q. Source Priority는 뭐야?
A. 여러 문서가 충돌할 때 어떤 근거를 우선할지 정하는 기준이다.

Q. Master Rules와 Domain Rules가 충돌하면 무엇을 따라?
A. Master Rules를 우선한다.

Q. Domain Rules와 Part 문서가 충돌하면 무엇을 따라?
A. Domain Rules를 우선한다.

Q. Context Compression은 뭐야?
A. 긴 Retrieved Context를 Token Budget 안에 맞게 핵심 근거 중심으로 줄이는 과정이다.

Q. Compression에서 무엇을 보존해야 해?
A. 정의, 판단 기준, 조건, 예외, Source 정보를 보존해야 한다.

Q. Compression이 잘못되면 어떤 문제가 생겨?
A. 조건이나 예외가 빠져 Faithfulness와 Completeness가 낮아질 수 있다.

Q. Token Budget은 뭐야?
A. LLM에 전달할 수 있는 Query, Context, Instruction, Answer 공간의 총 토큰 한계다.

Q. Context를 길게 넣으면 항상 좋아?
A. 아니다. 노이즈와 중복이 많으면 답변 품질이 낮아질 수 있다.

Q. Context Window는 뭐야?
A. LLM이 한 번에 처리할 수 있는 최대 입력 길이다.

Q. Context Quality는 뭐야?
A. 입력된 Context가 질문에 적합한 근거로 구성되었는지의 품질이다.

Q. Context Window가 크면 RAG 품질이 좋아져?
A. 반드시 그렇지는 않다. 관련 없는 Context가 많으면 품질이 낮아질 수 있다.

Q. End-to-End Optimization Flow는 뭐야?
A. Query 개선부터 Context 구성과 답변 검증까지 연결한 전체 RAG 최적화 절차다.

Q. Optimization Report는 뭐야?
A. Top-K, Threshold, Reranking, Context Assembly 조정 결과를 기록하는 문서다.

Q. Optimization Report에는 무엇을 기록해?
A. 변경 전후 설정, 이유, 지표 변화, Regression 여부, 다음 조치를 기록한다.

Q. Top-K / Threshold 조정에서 가장 흔한 실수는?
A. 평가 결과 없이 감으로 값을 크게 또는 작게 바꾸는 것이다.

Q. Reranking에 대한 흔한 오해는?
A. 초기 검색에 없는 문서도 Reranking으로 찾을 수 있다고 생각하는 것이다.

Q. Context Compression에서 가장 위험한 실수는?
A. 조건과 예외를 제거해 답변이 Context를 왜곡하게 만드는 것이다.

Q. Top-K / Threshold / Reranking 개선 후 무엇을 해야 해?
A. 같은 Golden Query로 Retest하고 Precision, Recall, Ranking, Groundedness 변화를 Report에 기록한다.
