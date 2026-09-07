# RAG Evaluation & Retrieval Optimization Part02 Retrieval Evaluation

---

# 1. Retrieval Evaluation Core

## 1.1 Retrieval Evaluation 기본 개념

### [개념]

Retrieval Evaluation은 사용자 Query에 대해 RAG 시스템이 필요한 문서, Section, Chunk를 검색 결과로 가져오는지 평가하는 과정이다.

RAG 답변 품질은 Retrieval 품질에 크게 의존한다.

Retrieval이 실패하면 LLM은 올바른 근거를 받지 못하고, Generation 단계에서 Hallucination 또는 불완전한 답변이 발생할 가능성이 높다.

```text
User Query
→ Retrieve Top-K Chunks
→ Compare Expected Document
→ Compare Expected Chunk
→ Measure Retrieval Quality
→ Record Failure
→ Improve Query / Chunk / Metadata
```

---

### [핵심]

- Retrieval Evaluation은 검색 단계의 품질을 평가한다.
- 핵심 질문은 “필요한 문서를 찾았는가?”이다.
- Expected Document가 검색 결과에 포함되는지 확인한다.
- Expected Chunk가 검색 결과에 포함되는지 확인한다.
- 검색 결과의 순위와 관련도를 함께 평가한다.
- 관련 없는 Chunk가 많으면 Precision이 낮다.
- 필요한 Chunk가 누락되면 Recall이 낮다.
- Retrieval 실패는 Generation 실패와 분리해서 기록한다.

---

### [실무]

2026 실무 기준 RAG 검수에서는 최종 답변보다 먼저 검색 결과를 확인한다.

Retrieval Evaluation은 아래 항목을 기준으로 수행한다.

| 평가 항목         | 의미                    | 사용 목적                 |
| ----------------- | ----------------------- | ------------------------- |
| Query             | 사용자 질문             | 검색 입력 확인            |
| Expected Document | 검색되어야 하는 문서    | 문서 단위 Hit 평가        |
| Expected Section  | 검색되어야 하는 Section | Section 단위 정확도 평가  |
| Expected Chunk    | 검색되어야 하는 Chunk   | Chunk 단위 Retrieval 평가 |
| Retrieved Chunks  | 실제 검색 결과          | 검색 결과 품질 확인       |
| Top-K             | 검색 결과 개수          | Recall / Precision 조정   |
| Ranking           | 관련 문서 순위          | 상위 배치 품질 확인       |
| Failure Cause     | 실패 원인               | 개선 대상 결정            |

Retrieval Evaluation은 감으로 수행하지 않는다.

Golden Query와 Expected Document를 기준으로 반복 평가한다.

---

### [FAQ]

Q. Retrieval Evaluation은 뭐야?

A. 사용자 질문에 대해 기대 문서나 기대 Chunk가 검색 결과에 포함되는지 평가하는 과정이다.

Q. Retrieval Evaluation의 핵심 질문은 뭐야?

A. 필요한 문서를 찾았는가이다.

Q. Retrieval이 실패하면 왜 답변도 틀려져?

A. LLM이 올바른 근거를 받지 못하기 때문에 문서 기반 답변을 만들기 어렵다.

Q. Retrieval Evaluation은 최종 답변을 평가하는 거야?

A. 아니다. 검색 결과 자체를 평가한다.

Q. Retrieval 실패와 Generation 실패는 왜 나눠야 해?

A. 검색 실패와 생성 실패는 원인과 개선 방법이 다르기 때문이다.

---

## 1.2 Retrieval Evaluation 필수 구성 요소

### [개념]

Retrieval Evaluation은 Query, Expected Document, Expected Chunk, Retrieved Chunks, Score, Failure Cause를 함께 기록해야 의미가 있다.

기대 문서 없이 검색 결과만 보면 검색 성공 여부를 객관적으로 판단하기 어렵다.

---

### [핵심]

- Query는 실제 사용자 질문 형태로 작성한다.
- Expected Document는 검색되어야 하는 문서 파일명이다.
- Expected Section은 문서 내 핵심 위치다.
- Expected Chunk는 검색되어야 하는 최소 근거 단위다.
- Retrieved Chunks는 실제 검색된 결과다.
- Score는 Hit@K, Precision, Recall, MRR 등으로 기록한다.
- Failure Cause는 Query, Chunk, Metadata, Top-K, Index 문제로 분류한다.

---

### [실무]

Retrieval Evaluation 기록 예시:

```md
# Retrieval Evaluation Case

## Query

RAG 품질은 어떻게 평가해?

## Expected

- Expected Document: RAG_Evaluation_Retrieval_Optimization_Part01_Core.md
- Expected Section: RAG Evaluation Core
- Expected Chunk: Retrieval Evaluation과 Generation Evaluation을 분리 평가한다

## Retrieved

| Rank | Document                                             | Section             | Relevant |
| ---: | ---------------------------------------------------- | ------------------- | -------- |
|    1 | RAG_Evaluation_Retrieval_Optimization_Part01_Core.md | RAG Evaluation Core | Yes      |
|    2 | Vector_Database_RAG_Part03_Retrieval.md              | Similarity Search   | Partial  |
|    3 | Prompt_Engineering_Part07_Evaluation.md              | Prompt Evaluation   | No       |

## Score

- Hit@1: 1
- Hit@3: 1
- Precision@3: 0.67
- Recall: Partial

## Result

- Retrieval Success
- Minor Noise Exists
```

이 형식은 RAG Agent가 실패 원인을 검색하고 개선 방향을 판단하기 쉽다.

---

### [FAQ]

Q. Retrieval Evaluation에는 무엇을 기록해야 해?

A. Query, Expected Document, Expected Chunk, Retrieved Chunks, Score, Failure Cause를 기록한다.

Q. Expected Document가 없으면 왜 문제야?

A. 어떤 문서가 검색되어야 하는지 기준이 없어서 성공 여부를 판단하기 어렵다.

Q. Expected Chunk는 꼭 필요해?

A. Chunk 단위 품질을 확인하려면 필요하다.

Q. Retrieved Chunks는 왜 기록해?

A. 검색된 문서의 관련도, 노이즈, 순위를 분석하기 위해 기록한다.

Q. Failure Cause는 왜 남겨야 해?

A. 반복 실패를 줄이고 문서 개선 우선순위를 정하기 위해 필요하다.

---

# 2. Expected Document and Expected Chunk

## 2.1 Expected Document

### [개념]

Expected Document는 특정 Query에 대해 반드시 검색되어야 하는 기준 문서다.

Golden Query는 Expected Document와 연결되어야 Retrieval 품질을 평가할 수 있다.

---

### [핵심]

- Expected Document는 Query가 검색해야 하는 목표 문서다.
- 파일명 기준으로 명확하게 지정한다.
- 하나의 Query에 여러 Expected Document가 있을 수 있다.
- 여러 문서가 필요한 경우 우선순위를 정한다.
- Expected Document가 Top-K 안에 있으면 Hit로 판단한다.
- Expected Document가 누락되면 Retrieval Failure로 기록한다.

---

### [실무]

Expected Document 정의 예시:

```json
{
  "query": "검색 결과는 맞는데 답변이 틀리면 어디를 봐?",
  "expectedDocuments": [
    {
      "document": "RAG_Evaluation_Retrieval_Optimization_Part01_Core.md",
      "priority": 1,
      "reason": "Retrieval Failure와 Generation Failure 구분 설명"
    },
    {
      "document": "RAG_Evaluation_Retrieval_Optimization_Part03_Generation_Evaluation.md",
      "priority": 2,
      "reason": "Generation Evaluation과 Grounding 검증 설명"
    }
  ]
}
```

Expected Document 우선순위 기준:

| 우선순위 | 의미           | 판단              |
| -------: | -------------- | ----------------- |
|        1 | 핵심 정답 문서 | 반드시 Top-K 포함 |
|        2 | 보조 근거 문서 | 포함되면 좋음     |
|        3 | 확장 설명 문서 | 필요 시 참조      |

---

### [FAQ]

Q. Expected Document는 뭐야?

A. 특정 Query에 대해 검색되어야 하는 기준 문서다.

Q. 하나의 Query에 Expected Document가 여러 개일 수 있어?

A. 가능하다. 복합 질문은 여러 문서가 필요할 수 있다.

Q. Expected Document 우선순위는 왜 필요해?

A. 핵심 문서와 보조 문서를 구분해야 검색 성공 여부를 정확히 판단할 수 있다.

Q. Expected Document가 Top-K에 없으면 어떻게 해?

A. Retrieval Failure로 기록하고 Query, Chunk, Metadata, Index를 점검한다.

Q. Expected Document는 파일명으로 적어야 해?

A. RAG 문서 운영에서는 파일명 기준으로 명확히 적는 것이 좋다.

---

## 2.2 Expected Section

### [개념]

Expected Section은 Expected Document 내부에서 Query에 답하기 위해 검색되어야 하는 구체적인 Section이다.

Expected Document가 검색되더라도 관련 없는 Section이 검색되면 Chunk 품질은 낮을 수 있다.

---

### [핵심]

- Expected Section은 문서 내부의 목표 위치다.
- Header 기준으로 지정한다.
- 문서 단위 Hit보다 더 정밀한 평가가 가능하다.
- Expected Section이 검색되지 않으면 Section Retrieval 실패로 본다.
- Section Header가 불명확하면 검색 실패가 발생할 수 있다.
- Section은 Query Intent와 연결되어야 한다.

---

### [실무]

Expected Section 기록 예시:

```md
## Expected

- Expected Document: RAG_Evaluation_Retrieval_Optimization_Part02_Retrieval_Evaluation.md
- Expected Section: 3.1 Hit@K
- Expected Intent: 기대 문서가 Top-K 안에 포함되는지 평가
```

Section 평가 기준:

| 상태                               | 판단      | 조치                    |
| ---------------------------------- | --------- | ----------------------- |
| 문서와 Section 모두 검색됨         | 성공      | 유지                    |
| 문서는 검색되었지만 Section이 다름 | 부분 실패 | Header / FAQ 보강       |
| Section과 관련 없는 Chunk 검색     | 실패      | Chunk 분리              |
| 유사 Section이 여러 개 검색        | 혼선      | Naming Consistency 개선 |

---

### [FAQ]

Q. Expected Section은 뭐야?

A. 기대 문서 내부에서 검색되어야 하는 구체적인 Section이다.

Q. Expected Document가 검색되면 충분하지 않아?

A. 아니다. 관련 없는 Section이 검색되면 답변 근거가 약할 수 있다.

Q. Expected Section은 어떻게 지정해?

A. 문서의 Header 이름이나 번호를 기준으로 지정한다.

Q. Section 검색 실패는 왜 생겨?

A. Header가 모호하거나 Chunk 안에 여러 개념이 섞였기 때문이다.

Q. Section 평가가 필요한 이유는?

A. 문서 단위 Hit보다 정확한 Retrieval 품질을 확인하기 위해 필요하다.

---

## 2.3 Expected Chunk

### [개념]

Expected Chunk는 Query에 답하기 위해 검색되어야 하는 최소 근거 단위다.

Expected Chunk가 검색되어야 LLM이 정확하고 Grounded한 답변을 생성할 가능성이 높다.

---

### [핵심]

- Expected Chunk는 답변 근거가 되는 최소 문서 단위다.
- 하나의 Query에 여러 Expected Chunk가 필요할 수 있다.
- Expected Chunk는 Section보다 더 정밀한 평가 기준이다.
- Expected Chunk 누락은 답변 누락 또는 Hallucination으로 이어질 수 있다.
- Chunk는 단일 개념 중심이어야 평가가 쉽다.
- Chunk가 너무 크면 정확한 관련도 판단이 어렵다.
- Chunk가 너무 작으면 문맥이 부족할 수 있다.

---

### [실무]

Expected Chunk 정의 예시:

```json
{
  "query": "Precision과 Recall 차이는?",
  "expectedDocument": "RAG_Evaluation_Retrieval_Optimization_Part02_Retrieval_Evaluation.md",
  "expectedSection": "Precision and Recall",
  "expectedChunks": [
    "Precision은 검색된 결과 중 관련 Chunk 비율이다.",
    "Recall은 필요한 관련 Chunk 중 검색된 Chunk 비율이다.",
    "Top-K를 높이면 Recall은 올라갈 수 있지만 Precision은 낮아질 수 있다."
  ]
}
```

Expected Chunk 평가 기준:

| 검색 결과                               | 판단           |
| --------------------------------------- | -------------- |
| 모든 Expected Chunk 검색                | 성공           |
| 일부 Expected Chunk 검색                | 부분 성공      |
| 문서는 검색되었지만 Expected Chunk 누락 | Chunk 실패     |
| 유사하지만 의미가 다른 Chunk 검색       | 관련도 실패    |
| 관련 없는 Chunk 검색                    | Retrieval 실패 |

---

### [FAQ]

Q. Expected Chunk는 뭐야?

A. Query 답변에 필요한 최소 근거 Chunk다.

Q. Expected Chunk가 왜 중요해?

A. 정확한 Chunk가 검색되어야 LLM이 문서 근거 기반 답변을 만들 수 있다.

Q. Expected Chunk가 일부만 검색되면 어떻게 평가해?

A. 부분 성공으로 기록하고 누락된 Chunk를 보강한다.

Q. Expected Chunk가 너무 크면 왜 문제야?

A. 여러 개념이 섞여 관련도 평가가 어려워진다.

Q. Expected Chunk가 너무 작으면 왜 문제야?

A. 답변에 필요한 문맥이 부족할 수 있다.

---

# 3. Hit@K and Retrieval Hit Rate

## 3.1 Hit@K

### [개념]

Hit@K는 Expected Document 또는 Expected Chunk가 Top-K 검색 결과 안에 포함되는지 평가하는 Retrieval 지표다.

```text
Hit@K = Expected Document 또는 Expected Chunk가 Top-K 안에 있으면 1, 없으면 0
```

---

### [핵심]

- Hit@K는 Retrieval 성공 여부를 빠르게 확인하는 기본 지표다.
- Hit@1은 기대 문서가 1순위에 있는지 평가한다.
- Hit@3은 기대 문서가 상위 3개 안에 있는지 평가한다.
- Hit@5는 기대 문서가 상위 5개 안에 있는지 평가한다.
- Hit@K는 순위 품질을 단순화해서 본다.
- Hit@K가 높아도 노이즈가 많으면 Precision은 낮을 수 있다.
- Hit@K가 낮으면 Query, Chunk, Metadata, Index를 점검한다.

---

### [실무]

Hit@K 평가 예시:

```md
# Hit@K Evaluation

Query:
Top-K는 어떻게 조정해?

Expected Document:
RAG_Evaluation_Retrieval_Optimization_Part04_Retrieval_Optimization.md

Retrieved Top-5:

| Rank | Document                                                               | Hit |
| ---: | ---------------------------------------------------------------------- | --- |
|    1 | Vector_Database_RAG_Part02_Similarity_Search.md                        | 0   |
|    2 | RAG_Evaluation_Retrieval_Optimization_Part04_Retrieval_Optimization.md | 1   |
|    3 | RAG_Evaluation_Retrieval_Optimization_Part01_Core.md                   | 0   |
|    4 | Prompt_Engineering_Part08_Context.md                                   | 0   |
|    5 | Agent_Workflow_Design_Part03_Routing.md                                | 0   |

Result:

- Hit@1: 0
- Hit@3: 1
- Hit@5: 1
```

이 경우 검색 성공은 했지만 Rank 2이므로 Ranking Quality 개선 여지가 있다.

---

### [FAQ]

Q. Hit@K가 뭐야?

A. 기대 문서나 기대 Chunk가 Top-K 검색 결과 안에 포함되는지 확인하는 지표다.

Q. Hit@1은 뭐야?

A. 기대 문서가 검색 결과 1순위에 있는지 확인하는 지표다.

Q. Hit@3은 뭐야?

A. 기대 문서가 상위 3개 검색 결과 안에 포함되는지 확인하는 지표다.

Q. Hit@5는 뭐야?

A. 기대 문서가 상위 5개 검색 결과 안에 포함되는지 확인하는 지표다.

Q. Hit@K가 높으면 Retrieval이 완벽해?

A. 아니다. 기대 문서가 포함되어도 노이즈가 많거나 순위가 낮으면 품질 개선이 필요하다.

---

## 3.2 Retrieval Hit Rate

### [개념]

Retrieval Hit Rate는 여러 Golden Query 중 Expected Document 또는 Expected Chunk가 Top-K 안에 포함된 비율이다.

```text
Retrieval Hit Rate@K = Hit@K 성공 Query 수 / 전체 Query 수
```

---

### [핵심]

- Retrieval Hit Rate는 검색 성공률을 나타낸다.
- Golden Query Dataset 단위로 계산한다.
- Hit@1, Hit@3, Hit@5를 분리해서 기록한다.
- Hit Rate가 낮으면 문서 검색성이 부족한 것이다.
- Hit Rate가 높아도 Precision과 Ranking을 함께 봐야 한다.
- Query 표현 변형을 포함해야 실제 품질에 가깝다.

---

### [실무]

Retrieval Hit Rate 평가 예시:

```md
# Retrieval Hit Rate Report

## Dataset

- Domain: RAG Evaluation
- Query Count: 20
- Top-K: 5

## Result

| Metric | Score |
| ------ | ----: |
| Hit@1  |  0.65 |
| Hit@3  |  0.85 |
| Hit@5  |  0.95 |

## Interpretation

- Hit@5는 높음
- Hit@1은 개선 필요
- 관련 문서가 검색되지만 상위 배치가 약함
- Ranking Quality 또는 Reranking 검토 필요
```

Hit@5가 높고 Hit@1이 낮으면 문서는 검색되지만 최상위 정렬이 약하다는 뜻이다.

---

### [FAQ]

Q. Retrieval Hit Rate는 뭐야?

A. 여러 Query 중 기대 문서가 Top-K 안에 검색된 비율이다.

Q. Hit@K와 Retrieval Hit Rate는 뭐가 달라?

A. Hit@K는 단일 Query 기준이고, Retrieval Hit Rate는 여러 Query의 성공 비율이다.

Q. Hit@1이 낮고 Hit@5가 높으면 무슨 뜻이야?

A. 기대 문서는 검색되지만 상위 순위에 잘 배치되지 않는다는 뜻이다.

Q. Retrieval Hit Rate가 낮으면 어떻게 해?

A. Query Rewrite, Header 보강, FAQ 추가, Metadata 점검, Reindex를 수행한다.

Q. Hit Rate가 높으면 Generation도 잘 돼?

A. 보장되지 않는다. Generation Evaluation을 별도로 해야 한다.

---

# 4. Precision and Recall

## 4.1 Precision

### [개념]

Precision은 검색된 결과 중 실제로 Query와 관련 있는 Chunk의 비율이다.

```text
Precision = Relevant Retrieved Chunks / Retrieved Chunks
```

Precision이 낮으면 LLM에 불필요한 Context가 많이 들어가고, 답변 품질이 흔들릴 수 있다.

---

### [핵심]

- Precision은 검색 결과의 정확도를 평가한다.
- 관련 없는 Chunk가 많으면 Precision이 낮다.
- Top-K를 크게 하면 Precision이 낮아질 수 있다.
- Chunk에 여러 개념이 섞이면 Precision이 낮아질 수 있다.
- Metadata Filter가 없으면 다른 Domain 문서가 섞일 수 있다.
- Similarity Threshold가 낮으면 노이즈가 증가할 수 있다.
- Reranking은 Precision 개선에 도움될 수 있다.

---

### [실무]

Precision 진단 예시:

```md
# Precision Evaluation

Query:
Groundedness가 뭐야?

Retrieved Top-5:

| Rank | Chunk                | Relevant |
| ---: | -------------------- | -------- |
|    1 | Groundedness 정의    | Yes      |
|    2 | Faithfulness와 차이  | Yes      |
|    3 | Prompt 작성법        | No       |
|    4 | Vector DB Index 설정 | No       |
|    5 | Hallucination Check  | Partial  |

Relevant Count:
2.5 / 5

Precision@5:
0.50
```

Precision이 낮을 때 조치:

| 원인           | 조치                      |
| -------------- | ------------------------- |
| Top-K 과다     | Top-K 감소                |
| Threshold 낮음 | Similarity Threshold 상향 |
| Chunk 혼합     | Chunk 분리                |
| Domain 혼선    | Metadata Filter 적용      |
| 순위 불안정    | Reranking 적용            |
| 중복 Chunk     | Deduplication 적용        |

---

### [FAQ]

Q. Precision은 뭐야?

A. 검색된 결과 중 실제로 관련 있는 Chunk의 비율이다.

Q. Precision이 낮다는 건 무슨 뜻이야?

A. 검색 결과에 관련 없는 문서나 Chunk가 많이 섞였다는 뜻이다.

Q. Precision이 낮으면 답변에 어떤 문제가 생겨?

A. LLM이 노이즈 Context에 영향을 받아 부정확한 답변을 만들 수 있다.

Q. Precision을 높이려면 어떻게 해?

A. Top-K 감소, Threshold 조정, Metadata Filter, Chunk 분리, Reranking을 검토한다.

Q. Precision만 높이면 충분해?

A. 아니다. Precision만 높이면 필요한 문서를 놓쳐 Recall이 낮아질 수 있다.

---

## 4.2 Recall

### [개념]

Recall은 Query에 답하기 위해 필요한 관련 Chunk 중 실제로 검색된 Chunk의 비율이다.

```text
Recall = Retrieved Relevant Chunks / Total Relevant Chunks
```

Recall이 낮으면 답변에 필요한 핵심 근거가 누락될 수 있다.

---

### [핵심]

- Recall은 검색 결과의 포괄성을 평가한다.
- 필요한 Chunk가 누락되면 Recall이 낮다.
- Top-K를 높이면 Recall이 올라갈 수 있다.
- Query Expansion은 Recall 개선에 도움될 수 있다.
- Metadata Filter가 너무 강하면 Recall이 낮아질 수 있다.
- Chunk 제목이 약하면 필요한 Chunk가 검색되지 않을 수 있다.
- FAQ와 Retrieval Queries는 Recall 개선에 중요하다.

---

### [실무]

Recall 진단 예시:

```md
# Recall Evaluation

Query:
Top-K는 어떻게 조정해?

Total Relevant Chunks:

| Expected Chunk      | Retrieved |
| ------------------- | --------- |
| Top-K 증가 기준     | Yes       |
| Top-K 감소 기준     | No        |
| Context Budget 고려 | Yes       |
| Reranking 고려      | No        |

Retrieved Relevant:
2 / 4

Recall:
0.50
```

Recall이 낮을 때 조치:

| 원인         | 조치                 |
| ------------ | -------------------- |
| Top-K 부족   | Top-K 증가           |
| Query가 짧음 | Query Rewrite        |
| 표현 불일치  | Query Expansion      |
| Header 약함  | Header 보강          |
| FAQ 부족     | 사용자형 FAQ 추가    |
| Filter 과도  | Metadata Filter 완화 |
| Index 미반영 | Reindex 수행         |

---

### [FAQ]

Q. Recall은 뭐야?

A. 필요한 관련 Chunk 중 실제 검색에 성공한 Chunk의 비율이다.

Q. Recall이 낮다는 건 무슨 뜻이야?

A. 답변에 필요한 문서나 Chunk가 검색되지 않았다는 뜻이다.

Q. Recall을 높이려면 어떻게 해?

A. Top-K 증가, Query Expansion, FAQ 보강, Metadata Filter 완화, Reindex를 검토한다.

Q. Recall이 낮으면 답변에 어떤 문제가 생겨?

A. 핵심 근거가 빠져 답변이 불완전하거나 틀릴 수 있다.

Q. Recall만 높이면 충분해?

A. 아니다. Recall만 높이면 노이즈가 늘어 Precision이 낮아질 수 있다.

---

## 4.3 Precision vs Recall

### [개념]

Precision과 Recall은 Retrieval 품질을 서로 다른 관점에서 평가한다.

Precision은 검색 결과가 얼마나 정확한지 보고, Recall은 필요한 문서를 얼마나 놓치지 않았는지 본다.

---

### [핵심]

- Precision은 검색 결과의 정확도다.
- Recall은 검색 결과의 포괄성이다.
- Precision이 높아도 Recall이 낮으면 필요한 문서를 놓칠 수 있다.
- Recall이 높아도 Precision이 낮으면 노이즈가 많아진다.
- Top-K 증가는 Recall 개선에 유리하지만 Precision 저하를 유발할 수 있다.
- Threshold 상향은 Precision 개선에 유리하지만 Recall 저하를 유발할 수 있다.
- RAG는 Context Budget 안에서 Precision과 Recall 균형을 맞춰야 한다.

---

### [실무]

Precision / Recall 비교표:

| 비교         | Precision                     | Recall                           |
| ------------ | ----------------------------- | -------------------------------- |
| 핵심 질문    | 검색된 결과가 관련 있는가?    | 필요한 문서를 놓치지 않았는가?   |
| 낮을 때 문제 | 노이즈가 많음                 | 근거 누락                        |
| 주요 원인    | Top-K 과다, Threshold 낮음    | Top-K 부족, Query 약함           |
| 개선 방법    | Filter, Reranking, Chunk 분리 | Query Expansion, FAQ, Top-K 증가 |
| 위험         | 답변이 노이즈에 흔들림        | 답변이 불완전함                  |

판단 기준:

```text
관련 없는 문서가 많음
→ Precision 개선 필요

필요한 문서가 빠짐
→ Recall 개선 필요

둘 다 낮음
→ Chunk 구조, Metadata, Query 설계 재검토
```

---

### [FAQ]

Q. Precision과 Recall 차이는 뭐야?

A. Precision은 검색 결과의 정확도이고 Recall은 필요한 문서를 얼마나 놓치지 않았는지 보는 포괄성이다.

Q. Precision이 높고 Recall이 낮으면 뭐가 문제야?

A. 검색 결과는 깔끔하지만 필요한 문서를 놓칠 수 있다.

Q. Recall이 높고 Precision이 낮으면 뭐가 문제야?

A. 필요한 문서는 포함되지만 관련 없는 문서가 많이 섞인다.

Q. Precision과 Recall 중 뭐가 더 중요해?

A. 목적에 따라 다르지만 RAG에서는 Context Budget 안에서 균형이 중요하다.

Q. Top-K 조정은 Precision과 Recall에 어떤 영향을 줘?

A. Top-K를 높이면 Recall은 올라갈 수 있지만 Precision은 낮아질 수 있다.

---

# 5. Ranking Quality

## 5.1 Ranking Quality 기본 개념

### [개념]

Ranking Quality는 관련 문서나 Chunk가 검색 결과에서 얼마나 상위에 배치되는지 평가하는 기준이다.

RAG 검색은 Expected Document가 Top-K 안에 포함되는 것뿐 아니라, 상위 순위에 배치되는 것이 중요하다.

---

### [핵심]

- Ranking Quality는 검색 결과 순위 품질을 평가한다.
- 관련 문서가 Top-1에 가까울수록 좋다.
- Rank가 낮으면 Context Assembly에서 누락될 수 있다.
- 관련 문서가 뒤쪽에 있으면 LLM 답변 영향력이 낮아질 수 있다.
- MRR은 첫 번째 관련 문서의 순위를 평가한다.
- NDCG는 여러 관련 문서의 순위 품질을 평가한다.
- 순위가 불안정하면 Reranking을 검토한다.

---

### [실무]

Ranking Quality 진단 예시:

```md
# Ranking Quality Evaluation

Query:
Hallucination은 어떻게 확인해?

Expected Document:
RAG_Evaluation_Retrieval_Optimization_Part03_Generation_Evaluation.md

Retrieved:

| Rank | Document                                                              | Relevant |
| ---: | --------------------------------------------------------------------- | -------- |
|    1 | Prompt_Engineering_Part09_Output_Control.md                           | Partial  |
|    2 | RAG_Evaluation_Retrieval_Optimization_Part01_Core.md                  | Partial  |
|    3 | RAG_Evaluation_Retrieval_Optimization_Part03_Generation_Evaluation.md | Yes      |

Result:

- Hit@3: 1
- Hit@1: 0
- Ranking Quality: Medium
- Action: Header / FAQ 보강 또는 Reranking 검토
```

기대 문서가 Top-K에 있더라도 Rank가 낮으면 개선 대상이다.

---

### [FAQ]

Q. Ranking Quality는 뭐야?

A. 관련 문서가 검색 결과에서 얼마나 상위에 배치되는지 평가하는 기준이다.

Q. 기대 문서가 Top-K 안에 있으면 순위는 상관없어?

A. 아니다. 순위가 낮으면 답변에 충분히 반영되지 않을 수 있다.

Q. Ranking Quality가 낮으면 어떻게 해?

A. Header, FAQ, Keyword Placement를 보강하거나 Reranking을 검토한다.

Q. Top-1이 중요한 이유는 뭐야?

A. 가장 관련 있는 문서가 먼저 들어와야 Context 품질과 답변 정확도가 좋아진다.

Q. 순위가 매번 달라지면 어떻게 해?

A. 평가 Dataset, Index 상태, 중복 문서, Reranking 설정을 점검한다.

---

## 5.2 MRR

### [개념]

MRR은 Mean Reciprocal Rank의 약자이며, 첫 번째 관련 문서가 검색 결과에서 얼마나 상위에 있는지 평가하는 지표다.

```text
Reciprocal Rank = 1 / 첫 번째 관련 문서 순위
MRR = 여러 Query의 Reciprocal Rank 평균
```

---

### [핵심]

- MRR은 첫 번째 관련 문서의 순위를 평가한다.
- 관련 문서가 1위면 점수는 1이다.
- 관련 문서가 2위면 점수는 0.5다.
- 관련 문서가 5위면 점수는 0.2다.
- MRR이 낮으면 관련 문서가 뒤쪽에 배치되는 것이다.
- RAG에서 MRR은 Top Rank 품질 확인에 유용하다.

---

### [실무]

MRR 계산 예시:

```md
# MRR Example

| Query | First Relevant Rank | Reciprocal Rank |
| ----- | ------------------: | --------------: |
| Q1    |                   1 |            1.00 |
| Q2    |                   2 |            0.50 |
| Q3    |                   5 |            0.20 |
| Q4    |           Not Found |            0.00 |

MRR:
(1.00 + 0.50 + 0.20 + 0.00) / 4 = 0.425
```

MRR 해석:

| MRR 상태 | 해석                         | 조치                           |
| -------- | ---------------------------- | ------------------------------ |
| 높음     | 관련 문서가 상위에 있음      | 유지                           |
| 중간     | 검색은 되지만 순위 개선 필요 | Header / FAQ 보강              |
| 낮음     | 관련 문서가 뒤쪽 또는 누락   | Query / Chunk / Reranking 개선 |

---

### [FAQ]

Q. MRR은 뭐야?

A. 첫 번째 관련 문서가 검색 결과에서 얼마나 상위에 있는지 평가하는 지표다.

Q. MRR이 높다는 건 무슨 뜻이야?

A. 관련 문서가 검색 결과 상위에 잘 배치된다는 뜻이다.

Q. 관련 문서가 1위면 Reciprocal Rank는 얼마야?

A. 1이다.

Q. 관련 문서가 5위면 Reciprocal Rank는 얼마야?

A. 0.2다.

Q. MRR은 언제 유용해?

A. 기대 문서가 Top-K에 포함되는지뿐 아니라 얼마나 상위에 있는지 평가할 때 유용하다.

---

## 5.3 NDCG

### [개념]

NDCG는 Normalized Discounted Cumulative Gain의 약자이며, 여러 관련 문서의 순위 품질을 평가하는 지표다.

RAG 문서 평가에서는 복잡한 수식보다 “중요한 문서가 더 상위에 있는가?”를 판단하는 실무 해석 중심으로 사용한다.

---

### [핵심]

- NDCG는 여러 관련 문서의 순위 품질을 평가한다.
- 더 중요한 문서가 상위에 있으면 점수가 높다.
- 관련도 등급을 사용할 수 있다.
- 핵심 문서와 보조 문서를 구분할 때 유용하다.
- 복합 Query 평가에 적합하다.
- 개인 RAG 운영에서는 기초 해석 중심으로 사용한다.

---

### [실무]

NDCG형 실무 평가 예시:

```md
# NDCG-style Ranking Review

Query:
RAG 답변 품질은 어떻게 평가해?

Expected Relevance:

| Document                                                              | Relevance |
| --------------------------------------------------------------------- | --------: |
| RAG_Evaluation_Retrieval_Optimization_Part01_Core.md                  |         3 |
| RAG_Evaluation_Retrieval_Optimization_Part03_Generation_Evaluation.md |         3 |
| RAG_Evaluation_Retrieval_Optimization_Part02_Retrieval_Evaluation.md  |         2 |
| Prompt_Engineering_Part08_Context.md                                  |         1 |

Retrieved:

| Rank | Document                                                              | Relevance |
| ---: | --------------------------------------------------------------------- | --------: |
|    1 | RAG_Evaluation_Retrieval_Optimization_Part03_Generation_Evaluation.md |         3 |
|    2 | RAG_Evaluation_Retrieval_Optimization_Part01_Core.md                  |         3 |
|    3 | Prompt_Engineering_Part08_Context.md                                  |         1 |
|    4 | RAG_Evaluation_Retrieval_Optimization_Part02_Retrieval_Evaluation.md  |         2 |

Review:

- 핵심 문서 2개가 상위에 있음
- 보조 문서 순위는 개선 여지 있음
- Overall Ranking Quality: Good
```

NDCG는 복잡한 Benchmark보다 복합 Query의 순위 품질 점검용으로 사용한다.

---

### [FAQ]

Q. NDCG는 뭐야?

A. 여러 관련 문서가 중요도에 맞게 상위에 배치되었는지 평가하는 지표다.

Q. NDCG는 MRR과 뭐가 달라?

A. MRR은 첫 번째 관련 문서 순위를 보고, NDCG는 여러 관련 문서의 전체 순위 품질을 본다.

Q. 개인 RAG 문서 평가에서 NDCG 수식을 꼭 써야 해?

A. 필수는 아니다. 실무에서는 중요 문서가 상위에 있는지 해석 중심으로 써도 된다.

Q. NDCG는 언제 유용해?

A. 하나의 질문에 여러 문서가 필요한 복합 Query를 평가할 때 유용하다.

Q. NDCG가 낮으면 어떻게 해?

A. 핵심 문서 Header, FAQ, Metadata, Keyword Placement를 보강하고 Reranking을 검토한다.

---

# 6. Retrieval Failure Analysis

## 6.1 Retrieval Failure 유형

### [개념]

Retrieval Failure는 필요한 문서나 Chunk가 검색되지 않거나, 검색되더라도 순위와 관련도가 낮아 답변 근거로 사용하기 어려운 상태다.

Retrieval Failure는 원인을 분류해야 개선할 수 있다.

---

### [핵심]

- Expected Document가 Top-K에 없음
- Expected Section이 검색되지 않음
- Expected Chunk가 누락됨
- 관련 없는 Chunk가 상위에 있음
- 관련 문서 순위가 낮음
- Metadata Filter가 필요한 문서를 제외함
- Query가 너무 짧거나 모호함
- 문서 Header와 FAQ가 약함
- Reindex가 누락됨

---

### [실무]

Retrieval Failure 분류표:

| 실패 유형     | 증상                       | 원인                       | 우선 조치                    |
| ------------- | -------------------------- | -------------------------- | ---------------------------- |
| Document Miss | 기대 문서 없음             | Query-문서 표현 불일치     | FAQ / Retrieval Queries 보강 |
| Section Miss  | 문서는 있으나 Section 다름 | Header 불명확              | Section Header 개선          |
| Chunk Miss    | 핵심 Chunk 누락            | Chunk 분리 문제            | Chunk 재구성                 |
| Low Precision | 노이즈 많음                | Top-K 과다, Threshold 낮음 | Top-K / Threshold 조정       |
| Low Recall    | 필요한 문서 누락           | Query 약함, Filter 과도    | Query Expansion, Filter 완화 |
| Low Ranking   | 기대 문서 순위 낮음        | 키워드 위치 약함           | Header / Keyword 보강        |
| Filter Error  | 특정 문서 제외             | Metadata 오류              | Metadata 검수                |
| Stale Index   | 수정 반영 안 됨            | Reindex 누락               | Reindex 수행                 |

---

### [FAQ]

Q. Retrieval Failure는 뭐야?

A. 필요한 문서나 Chunk가 검색되지 않거나 검색 품질이 낮아 답변 근거로 쓰기 어려운 상태다.

Q. Expected Document가 안 나오면 무슨 실패야?

A. Document Miss 유형의 Retrieval Failure다.

Q. Expected Section만 안 나오면 어떻게 봐?

A. Section Miss로 보고 Header와 Chunk 구조를 점검한다.

Q. 관련 없는 Chunk가 많으면 무슨 문제야?

A. Low Precision 문제다.

Q. 필요한 Chunk가 빠지면 무슨 문제야?

A. Low Recall 또는 Chunk Miss 문제다.

---

## 6.2 Retrieval Failure 진단 Flow

### [개념]

Retrieval Failure 진단 Flow는 검색 실패가 Query, Chunk, Metadata, Top-K, Index 중 어디에서 발생했는지 확인하는 절차다.

---

### [핵심]

- 먼저 Expected Document가 Top-K에 있는지 확인한다.
- 다음으로 Expected Section과 Expected Chunk를 확인한다.
- 검색 결과의 관련 없는 Chunk 비율을 확인한다.
- Metadata Filter가 필요한 문서를 제외했는지 확인한다.
- Query 표현과 문서 표현의 차이를 확인한다.
- 문서 수정 후 Reindex 여부를 확인한다.
- 개선 후 같은 Golden Query로 재평가한다.

---

### [실무]

Retrieval Failure 진단 Flow:

```text
Failure Query
→ Check Top-K Results
→ Is Expected Document Found?
  → No: Document Miss
  → Yes: Check Expected Section
→ Is Expected Section Found?
  → No: Section Miss
  → Yes: Check Expected Chunk
→ Is Expected Chunk Found?
  → No: Chunk Miss
  → Yes: Check Precision / Ranking
→ Check Metadata Filter
→ Check Query Expression
→ Check Reindex Status
→ Apply Fix
→ Retest
```

진단 결과별 우선 조치:

| 진단 결과      | 우선 조치                     |
| -------------- | ----------------------------- |
| Document Miss  | Retrieval Queries 추가        |
| Section Miss   | Header 명확화                 |
| Chunk Miss     | Chunk 분리 / 내용 보강        |
| Low Precision  | Top-K 감소 / Threshold 상향   |
| Low Recall     | Top-K 증가 / Query Expansion  |
| Low Ranking    | Keyword Placement / Reranking |
| Metadata Error | Metadata 수정                 |
| Stale Index    | Reindex                       |

---

### [FAQ]

Q. Retrieval Failure는 어디부터 확인해?

A. Expected Document가 Top-K 검색 결과에 있는지부터 확인한다.

Q. 문서는 검색됐는데 답변에 필요한 내용이 없으면?

A. Expected Section 또는 Expected Chunk 누락으로 보고 Chunk 구조를 개선한다.

Q. 검색 결과에 노이즈가 많으면 어디를 봐?

A. Precision, Top-K, Similarity Threshold, Metadata Filter를 확인한다.

Q. 필요한 문서가 필터 때문에 빠질 수 있어?

A. 가능하다. Metadata Filter가 너무 강하거나 값이 틀리면 문서가 제외될 수 있다.

Q. 개선 후에는 무엇을 해야 해?

A. Reindex 후 같은 Golden Query로 재평가한다.

---

# 7. Retrieval Evaluation Report

## 7.1 Retrieval Evaluation Report 형식

### [개념]

Retrieval Evaluation Report는 검색 품질 평가 결과를 기록하고, 실패 원인과 개선 조치를 추적하는 문서다.

Agent는 Report를 통해 어떤 Query가 실패했고 어떤 문서를 개선해야 하는지 판단한다.

---

### [핵심]

- Evaluation Date를 기록한다.
- Dataset 이름을 기록한다.
- Query Count를 기록한다.
- Hit@1, Hit@3, Hit@5를 기록한다.
- Precision / Recall 결과를 기록한다.
- Common Failure를 요약한다.
- Failure Case를 표로 남긴다.
- Improvement Action을 기록한다.
- Retest Result를 기록한다.

---

### [실무]

Retrieval Evaluation Report 예시:

```md
# Retrieval Evaluation Report

## Summary

- Evaluation Date: 2026-06-30
- Dataset: RAG Evaluation Golden Query Set v1
- Query Count: 30
- Hit@1: 0.70
- Hit@3: 0.86
- Hit@5: 0.93
- Main Failure: Section Miss, Low Ranking
- Next Action: Header / FAQ / Retrieval Queries 보강

## Metric Summary

| Metric      | Score | Interpretation        |
| ----------- | ----: | --------------------- |
| Hit@1       |  0.70 | 상위 배치 개선 필요   |
| Hit@3       |  0.86 | 검색 후보 포함 양호   |
| Hit@5       |  0.93 | Recall 양호           |
| Precision@5 |  0.62 | 노이즈 개선 필요      |
| Recall@5    |  0.88 | 주요 문서 대부분 포함 |

## Failure Cases

| Query                      | Expected Document   | Retrieved Rank | Failure Type  | Cause             | Fix                    |
| -------------------------- | ------------------- | -------------: | ------------- | ----------------- | ---------------------- |
| Top-K는 어떻게 조정해?     | Part04 Optimization |              4 | Low Ranking   | Header 약함       | FAQ 보강               |
| 문서에 있는데 검색이 안 돼 | Part02 Retrieval    |      Not Found | Document Miss | Query 표현 불일치 | Retrieval Queries 추가 |
| Precision과 Recall 차이는? | Part02 Retrieval    |              2 | Low Precision | 노이즈 과다       | Threshold 조정         |

## Retest Plan

- Modify Document:
- Reindex:
- Retest Query Set:
- Compare Hit@K:
- Compare Precision / Recall:
```

Report는 검색 품질 개선 전후 비교를 위해 누적 관리한다.

---

### [FAQ]

Q. Retrieval Evaluation Report는 뭐야?

A. 검색 품질 평가 결과, 실패 원인, 개선 조치, 재평가 계획을 기록하는 문서다.

Q. Report에는 어떤 지표를 넣어야 해?

A. Hit@1, Hit@3, Hit@5, Precision, Recall, Failure Type, Fix를 넣는다.

Q. Failure Case는 왜 표로 기록해?

A. Query별 실패 원인과 개선 조치를 빠르게 검색하기 위해서다.

Q. Retest Result는 왜 필요해?

A. 수정 후 실제로 검색 품질이 개선되었는지 확인하기 위해 필요하다.

Q. Report는 사람용 문서야?

A. 주 목적은 Agent가 검색 실패와 개선 우선순위를 판단하도록 돕는 것이다.

---

# 8. Retrieval Evaluation Best Practice

## 8.1 Best Practice

### [개념]

Retrieval Evaluation Best Practice는 RAG 검색 품질을 안정적으로 측정하고 개선하기 위한 운영 규칙이다.

평가는 단발성 점검이 아니라 Golden Query 기반 반복 루프로 수행한다.

---

### [핵심]

- Golden Query를 먼저 정의한다.
- Expected Document와 Expected Chunk를 명확히 지정한다.
- Retrieval과 Generation을 분리 평가한다.
- Hit@K만 보지 않고 Precision / Recall을 함께 본다.
- Ranking Quality를 확인한다.
- 실패 유형을 Document Miss, Section Miss, Chunk Miss로 분류한다.
- Query 표현 변형을 포함한다.
- Metadata Filter를 과도하게 적용하지 않는다.
- 문서 수정 후 Reindex한다.
- 같은 Query로 재평가한다.
- 개선 전후 Report를 비교한다.

---

### [실무]

Retrieval Evaluation Checklist:

```md
### [Checklist]

- [ ] Golden Query가 실제 사용자 질문 형태인가?
- [ ] Expected Document가 파일명 기준으로 지정되었는가?
- [ ] Expected Section이 Header 기준으로 지정되었는가?
- [ ] Expected Chunk가 최소 근거 단위로 정의되었는가?
- [ ] Retrieved Chunks를 직접 확인했는가?
- [ ] Hit@1, Hit@3, Hit@5를 기록했는가?
- [ ] Precision과 Recall을 함께 확인했는가?
- [ ] Ranking Quality를 확인했는가?
- [ ] Retrieval Failure 유형을 분류했는가?
- [ ] Metadata Filter가 과도하지 않은가?
- [ ] Query Rewrite 필요 여부를 판단했는가?
- [ ] Header / FAQ / Retrieval Queries 개선 여부를 판단했는가?
- [ ] 문서 수정 후 Reindex했는가?
- [ ] 같은 Golden Query로 재평가했는가?
```

---

### [FAQ]

Q. Retrieval Evaluation에서 가장 중요한 Best Practice는 뭐야?

A. Golden Query와 Expected Document를 기준으로 검색 결과를 반복 평가하는 것이다.

Q. Hit@K만 보면 안 되는 이유는?

A. 기대 문서가 포함되어도 노이즈가 많거나 순위가 낮을 수 있기 때문이다.

Q. Query 표현 변형은 왜 필요해?

A. 실제 사용자는 문서 제목 그대로 질문하지 않기 때문이다.

Q. Metadata Filter는 강하게 걸수록 좋아?

A. 아니다. 너무 강하면 필요한 문서가 제외되어 Recall이 낮아질 수 있다.

Q. Retrieval 개선 후 반드시 해야 할 일은?

A. Reindex 후 같은 Golden Query로 재평가하고 Report에 기록해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Retrieval Evaluation은 뭐야?
A. 사용자 Query에 대해 기대 문서나 기대 Chunk가 검색 결과에 포함되는지 평가하는 과정이다.

Q. Retrieval Evaluation의 핵심 질문은 뭐야?
A. 필요한 문서를 찾았는가이다.

Q. Retrieval 품질은 어떻게 평가해?
A. Expected Document, Expected Chunk, Hit@K, Precision, Recall, Ranking Quality를 기준으로 평가한다.

Q. Expected Document는 뭐야?
A. 특정 Query에 대해 검색되어야 하는 기준 문서다.

Q. Expected Section은 뭐야?
A. 기대 문서 내부에서 검색되어야 하는 구체적인 Section이다.

Q. Expected Chunk는 뭐야?
A. Query 답변에 필요한 최소 근거 Chunk다.

Q. Expected Document가 Top-K에 없으면 어떻게 해?
A. Retrieval Failure로 기록하고 Query, Chunk, Metadata, Reindex 여부를 점검한다.

Q. 문서는 검색됐는데 필요한 내용이 없으면 어떻게 해?
A. Expected Section 또는 Expected Chunk 누락으로 보고 Header와 Chunk 구조를 개선한다.

Q. Hit@K가 뭐야?
A. 기대 문서나 기대 Chunk가 Top-K 검색 결과 안에 포함되는지 확인하는 지표다.

Q. Hit@1은 뭐야?
A. 기대 문서가 검색 결과 1순위에 있는지 확인하는 지표다.

Q. Hit@3은 뭐야?
A. 기대 문서가 상위 3개 검색 결과 안에 포함되는지 확인하는 지표다.

Q. Hit@5는 뭐야?
A. 기대 문서가 상위 5개 검색 결과 안에 포함되는지 확인하는 지표다.

Q. Retrieval Hit Rate는 뭐야?
A. 여러 Query 중 기대 문서가 Top-K 안에 검색된 비율이다.

Q. Hit@K와 Retrieval Hit Rate 차이는?
A. Hit@K는 단일 Query 기준이고 Retrieval Hit Rate는 여러 Query의 성공 비율이다.

Q. Hit@1이 낮고 Hit@5가 높으면 무슨 뜻이야?
A. 기대 문서는 검색되지만 상위 순위에 잘 배치되지 않는다는 뜻이다.

Q. Precision은 뭐야?
A. 검색된 결과 중 실제로 관련 있는 Chunk의 비율이다.

Q. Recall은 뭐야?
A. 필요한 관련 Chunk 중 실제 검색에 성공한 Chunk의 비율이다.

Q. Precision과 Recall 차이는 뭐야?
A. Precision은 검색 결과의 정확도이고 Recall은 필요한 문서를 놓치지 않았는지 보는 포괄성이다.

Q. Precision이 낮으면 무슨 문제야?
A. 검색 결과에 관련 없는 문서나 Chunk가 많이 섞였다는 뜻이다.

Q. Recall이 낮으면 무슨 문제야?
A. 답변에 필요한 문서나 Chunk가 검색되지 않았다는 뜻이다.

Q. Precision을 높이려면 어떻게 해?
A. Top-K 감소, Threshold 조정, Metadata Filter, Chunk 분리, Reranking을 검토한다.

Q. Recall을 높이려면 어떻게 해?
A. Top-K 증가, Query Expansion, FAQ 보강, Metadata Filter 완화, Reindex를 검토한다.

Q. Top-K를 높이면 Precision과 Recall은 어떻게 변해?
A. Recall은 올라갈 수 있지만 Precision은 낮아질 수 있다.

Q. Ranking Quality는 뭐야?
A. 관련 문서가 검색 결과에서 얼마나 상위에 배치되는지 평가하는 기준이다.

Q. Ranking Quality가 낮으면 어떻게 해?
A. Header, FAQ, Keyword Placement를 보강하거나 Reranking을 검토한다.

Q. MRR은 뭐야?
A. 첫 번째 관련 문서가 검색 결과에서 얼마나 상위에 있는지 평가하는 지표다.

Q. NDCG는 뭐야?
A. 여러 관련 문서가 중요도에 맞게 상위에 배치되었는지 평가하는 지표다.

Q. MRR과 NDCG 차이는?
A. MRR은 첫 번째 관련 문서 순위를 보고 NDCG는 여러 관련 문서의 전체 순위 품질을 본다.

Q. Retrieval Failure는 뭐야?
A. 필요한 문서나 Chunk가 검색되지 않거나 검색 품질이 낮아 답변 근거로 쓰기 어려운 상태다.

Q. Document Miss는 뭐야?
A. Expected Document가 Top-K 검색 결과에 없는 Retrieval Failure다.

Q. Section Miss는 뭐야?
A. Expected Document는 검색되었지만 Expected Section이 검색되지 않은 실패다.

Q. Chunk Miss는 뭐야?
A. Query 답변에 필요한 Expected Chunk가 검색되지 않은 실패다.

Q. Low Precision은 뭐야?
A. 검색 결과에 관련 없는 Chunk가 많이 포함된 상태다.

Q. Low Recall은 뭐야?
A. 필요한 관련 Chunk가 검색 결과에서 누락된 상태다.

Q. Metadata Filter 때문에 Retrieval이 실패할 수 있어?
A. 가능하다. 필터가 너무 강하거나 값이 틀리면 필요한 문서가 제외될 수 있다.

Q. 문서 수정 후 검색 결과가 그대로면 왜 그래?
A. Reindex가 누락되어 Vector Index에 수정 내용이 반영되지 않았을 수 있다.

Q. Retrieval Evaluation Report는 뭐야?
A. 검색 품질 평가 결과, 실패 원인, 개선 조치, 재평가 계획을 기록하는 문서다.

Q. Retrieval Evaluation Report에는 무엇을 적어?
A. Evaluation Date, Dataset, Query Count, Hit@K, Precision, Recall, Failure Type, Fix, Retest Result를 적는다.

Q. Retrieval 개선 후 무엇을 해야 해?
A. Reindex 후 같은 Golden Query로 Hit@K, Precision, Recall, Ranking Quality를 재평가한다.
