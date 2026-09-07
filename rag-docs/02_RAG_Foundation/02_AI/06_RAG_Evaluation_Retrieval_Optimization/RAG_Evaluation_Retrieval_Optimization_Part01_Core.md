# RAG Evaluation & Retrieval Optimization Part01 Core

---

# 1. RAG Evaluation Core

## 1.1 RAG Evaluation 기본 구조

### [개념]

RAG Evaluation은 RAG 시스템이 사용자 질문에 대해 올바른 문서를 검색하고, 검색된 문서에 근거하여 답변을 생성하는지 평가하는 과정이다.

RAG 품질 평가는 반드시 Retrieval Evaluation과 Generation Evaluation을 분리한다.

```text
User Query
→ Retrieval Evaluation
→ Context Evaluation
→ Generation Evaluation
→ Grounding Check
→ Improvement
```

---

### [핵심]

- RAG Evaluation은 검색 품질과 답변 품질을 분리 평가한다.
- Retrieval Evaluation은 필요한 문서나 Chunk가 검색되었는지 확인한다.
- Generation Evaluation은 답변이 검색 문서에 근거하는지 확인한다.
- Context Evaluation은 검색된 Chunk가 LLM 답변에 적합한지 확인한다.
- Grounding Check는 답변의 주요 주장이 문서 근거와 일치하는지 검증한다.
- 개선 결과는 Chunk, Metadata, Query, Top-K, Prompt에 반영한다.

---

### [실무]

2026년 기준 RAG 시스템 검수는 최종 답변만 보고 판단하지 않는다.

실무에서는 아래 순서로 문제를 분리한다.

```text
질문이 나쁨
→ Query Rewrite 필요

문서가 검색되지 않음
→ Retrieval 실패

문서는 검색됨
→ Context 구성 확인

Context는 맞음
→ Generation / Prompt 문제

답변은 맞아 보임
→ Groundedness / Faithfulness 검증
```

Agent는 답변 실패를 발견하면 먼저 검색 결과를 확인해야 한다.

검색 결과 확인 없이 모델 성능 문제로 단정하면 안 된다.

---

### [FAQ]

Q. RAG Evaluation은 뭐야?

A. RAG가 필요한 문서를 검색하고, 그 문서에 근거해 올바르게 답변하는지 평가하는 과정이다.

Q. RAG 평가는 왜 Retrieval과 Generation을 나눠야 해?

A. 검색 실패와 생성 실패는 원인과 해결 방법이 다르기 때문이다.

Q. 답변이 맞으면 RAG 품질도 좋은 거야?

A. 아니다. 답변이 맞아 보여도 검색 문서에 근거하지 않으면 RAG 품질은 낮다.

Q. RAG 답변 실패는 어디부터 확인해?

A. 먼저 Retrieved Chunks를 확인하고, 기대 문서가 검색되었는지 확인한다.

Q. 검색 결과를 보지 않고 모델 문제라고 판단해도 돼?

A. 안 된다. Retrieval 실패인지 Generation 실패인지 먼저 분리해야 한다.

---

## 1.2 Retrieval Evaluation

### [개념]

Retrieval Evaluation은 사용자 Query에 대해 기대 문서 또는 기대 Chunk가 검색 결과에 포함되는지 평가하는 과정이다.

검색 단계가 실패하면 LLM은 올바른 근거를 받지 못하므로 정확한 답변을 생성하기 어렵다.

```text
Golden Query
→ Retrieve Top-K Chunks
→ Check Expected Document
→ Check Expected Chunk
→ Score Retrieval
→ Record Failure
```

---

### [핵심]

- Retrieval Evaluation의 핵심 질문은 “필요한 문서를 찾았는가?”이다.
- Expected Document가 Top-K 안에 있는지 확인한다.
- Expected Chunk가 검색되었는지 확인한다.
- Retrieved Chunk가 Query 의도와 맞는지 확인한다.
- 관련 없는 Chunk가 많으면 Precision이 낮다.
- 필요한 Chunk가 빠지면 Recall이 낮다.
- 관련 문서 순위가 낮으면 Ranking Quality가 낮다.

---

### [실무]

Retrieval Evaluation은 Golden Query 기반으로 수행한다.

기본 평가 단위는 아래와 같다.

| 평가 항목         | 의미                  | 확인 기준                        |
| ----------------- | --------------------- | -------------------------------- |
| Query             | 사용자 질문           | 실제 사용자 표현과 유사한가      |
| Expected Document | 검색되어야 하는 문서  | Top-K에 포함되는가               |
| Expected Chunk    | 검색되어야 하는 Chunk | 정확한 Section이 검색되는가      |
| Retrieved Chunks  | 실제 검색 결과        | 관련 문서와 노이즈 비율은 어떤가 |
| Hit@K             | Top-K 포함 여부       | 기대 문서가 K개 안에 있는가      |
| Precision         | 검색 결과 정확도      | 관련 없는 Chunk가 적은가         |
| Recall            | 검색 결과 포괄성      | 필요한 Chunk가 누락되지 않았는가 |

검색 실패가 반복되면 문서 제목, FAQ, Retrieval Queries, Metadata, Chunk Size를 점검한다.

---

### [FAQ]

Q. Retrieval Evaluation은 뭐야?

A. 사용자 질문에 대해 기대 문서나 기대 Chunk가 검색 결과에 포함되는지 평가하는 것이다.

Q. 기대 문서가 Top-K에 있으면 검색 성공이야?

A. 기본적으로 성공이지만, 순위가 너무 낮거나 관련 없는 Chunk가 많으면 품질은 낮을 수 있다.

Q. 문서가 있는데 검색이 안 되면 왜 그래?

A. Query 표현과 문서 표현이 다르거나, Chunk 제목이 불명확하거나, Metadata 필터가 잘못되었을 수 있다.

Q. Retrieval 실패는 어떻게 고쳐?

A. Header, FAQ, Retrieval Queries, 핵심 키워드, Metadata를 보강하고 Reindex 후 재평가한다.

Q. Top-K를 늘리면 Retrieval 문제가 해결돼?

A. 필요한 문서가 누락될 때는 도움이 될 수 있지만, 노이즈도 증가할 수 있다.

---

## 1.3 Generation Evaluation

### [개념]

Generation Evaluation은 LLM 답변이 Retrieved Context에 근거하여 정확하고 충실하게 생성되었는지 평가하는 과정이다.

Retrieval이 성공해도 Generation이 문서를 왜곡하거나 근거 없는 내용을 추가하면 RAG 답변 품질은 낮다.

```text
Retrieved Context
→ Generated Answer
→ Check Evidence
→ Check Hallucination
→ Check Completeness
→ Revise Answer
```

---

### [핵심]

- Generation Evaluation의 핵심 질문은 “문서에 근거해 답했는가?”이다.
- 답변의 주요 주장이 Retrieved Context와 일치해야 한다.
- 문서에 없는 내용을 확정하면 Hallucination이다.
- 질문에 필요한 핵심 내용을 빠뜨리면 Completeness가 낮다.
- 관련 없는 내용을 많이 포함하면 Relevance가 낮다.
- Context를 과장하거나 왜곡하면 Faithfulness가 낮다.
- 근거가 부족하면 부족하다고 답하는 것이 올바르다.

---

### [실무]

Generation Evaluation은 답변 단위가 아니라 Claim 단위로 검증한다.

```text
Generated Answer
→ Extract Claims
→ Match Claims with Retrieved Context
→ Mark Supported Claim
→ Mark Unsupported Claim
→ Revise Answer
```

검증 기준은 아래와 같다.

| 평가 항목      | 의미                      | 실패 예시                     |
| -------------- | ------------------------- | ----------------------------- |
| Correctness    | 답변 내용이 맞는가        | 잘못된 개념 설명              |
| Groundedness   | 문서 근거가 있는가        | 문서에 없는 설정값 생성       |
| Faithfulness   | Context를 왜곡하지 않는가 | 조건이나 예외 누락            |
| Relevance      | 질문과 관련 있는가        | 불필요한 일반론 포함          |
| Completeness   | 핵심 내용을 포함했는가    | 해결 절차 일부 누락           |
| Citation Match | 출처와 내용이 맞는가      | Citation은 있으나 근거 불일치 |

RAG Agent는 문서 근거가 없는 일반 지식 답변을 낮은 품질로 판단해야 한다.

---

### [FAQ]

Q. Generation Evaluation은 뭐야?

A. LLM 답변이 검색된 문서에 근거하고 질문 의도에 맞게 생성되었는지 평가하는 것이다.

Q. Retrieval은 성공했는데 답변이 틀리면 뭐가 문제야?

A. Prompt, Context Assembly, Grounding Rule, 답변 검증 과정 문제일 수 있다.

Q. 문서에 없는 내용을 말하면 무조건 문제야?

A. RAG 답변에서는 문제다. 추정이 필요하면 Assumption으로 표시해야 한다.

Q. 답변이 길면 좋은 답변이야?

A. 아니다. 길어도 근거가 없거나 질문과 관련 없는 내용이 많으면 품질이 낮다.

Q. 정보가 부족할 때는 어떻게 답해야 해?

A. 문서에 정보가 부족하다고 명확히 말하고 확정 답변을 피해야 한다.

---

# 2. RAG Failure Classification

## 2.1 Retrieval Failure

### [개념]

Retrieval Failure는 사용자의 질문에 필요한 문서나 Chunk가 검색 결과에 포함되지 않는 실패다.

LLM이 답변을 잘 생성하더라도 필요한 근거가 없으면 정확한 RAG 답변을 만들기 어렵다.

---

### [핵심]

- Expected Document가 Top-K에 없다.
- Expected Chunk가 검색되지 않는다.
- 검색 결과가 질문 의도와 다르다.
- 관련 없는 Chunk가 많이 섞인다.
- Metadata Filter가 필요한 문서를 제외한다.
- Query가 너무 짧거나 모호하다.
- Chunk 제목이나 내용에 핵심 키워드가 부족하다.

---

### [실무]

Retrieval Failure 진단 순서는 아래와 같다.

```text
Failure Query
→ Check Expected Document
→ Check Retrieved Chunks
→ Check Metadata Filter
→ Check Query Terms
→ Check Chunk Header
→ Check FAQ / Retrieval Queries
→ Reindex
→ Retest
```

대표 원인과 해결 방법은 아래와 같다.

| 문제                    | 원인                     | 해결                    |
| ----------------------- | ------------------------ | ----------------------- |
| 기대 문서 누락          | Query와 문서 표현 불일치 | Query Rewrite, FAQ 보강 |
| 관련 없는 문서 과다     | Top-K 과다, Chunk 혼합   | Top-K 조정, Chunk 분리  |
| 특정 Domain 문서만 누락 | Metadata 오류            | Metadata 값 검수        |
| 오래된 문서 우선 검색   | Version 관리 부족        | UpdatedAt, Version 보강 |
| 질문 표현 변형에 취약   | Retrieval Queries 부족   | 사용자형 FAQ 추가       |

---

### [FAQ]

Q. Retrieval Failure는 뭐야?

A. 필요한 문서나 Chunk가 검색 결과에 포함되지 않는 실패다.

Q. 문서가 있는데 검색이 안 되는 가장 흔한 이유는?

A. 사용자 Query와 문서의 제목, 키워드, FAQ 표현이 맞지 않기 때문이다.

Q. Retrieval Failure를 모델 문제로 봐도 돼?

A. 먼저 Chunk, Query, Metadata, Top-K, Reindex 여부를 확인해야 한다.

Q. 검색 결과가 엉뚱한 문서로 채워지면 어떻게 해?

A. Chunk를 분리하고 Metadata Filter, Similarity Threshold, Reranking을 검토한다.

Q. 문서 수정 후 바로 좋아져?

A. 아니다. 문서 수정 후 반드시 Reindex하고 같은 Golden Query로 재평가해야 한다.

---

## 2.2 Generation Failure

### [개념]

Generation Failure는 필요한 Context가 검색되었지만 LLM 답변이 문서 근거와 다르거나 질문에 맞지 않게 생성되는 실패다.

Generation Failure는 Prompt, Context Assembly, Grounding Rule, 답변 검증 부족에서 자주 발생한다.

---

### [핵심]

- Retrieved Context는 맞지만 답변이 틀린다.
- Context 내용을 왜곡한다.
- 문서에 없는 세부사항을 생성한다.
- 질문에 필요한 핵심 조건을 누락한다.
- 여러 Context 간 충돌을 해결하지 못한다.
- Citation이 실제 근거와 맞지 않는다.
- 근거 부족 상황에서 확정 답변을 한다.

---

### [실무]

Generation Failure 진단 순서는 아래와 같다.

```text
Retrieved Context
→ Check Answer Claims
→ Check Evidence Match
→ Check Unsupported Claims
→ Check Prompt Rule
→ Check Context Order
→ Revise Answer
```

대표 원인과 해결 방법은 아래와 같다.

| 문제            | 원인                     | 해결                       |
| --------------- | ------------------------ | -------------------------- |
| 근거 없는 답변  | Grounding Rule 부족      | 문서 근거 우선 Prompt 적용 |
| Context 왜곡    | 요약 과정 오류           | Claim 단위 검증            |
| 핵심 조건 누락  | Context Compression 오류 | 압축 기준 개선             |
| 출처 불일치     | Citation 검증 부족       | Source Match 확인          |
| 불필요한 일반론 | Relevance 제어 부족      | 질문 중심 답변 규칙 강화   |

---

### [FAQ]

Q. Generation Failure는 뭐야?

A. 검색된 문서는 맞지만 답변이 문서 근거와 다르거나 질문 의도에 맞지 않는 실패다.

Q. 검색 결과가 맞는데 답변이 틀리면 어디를 봐?

A. Prompt, Context Assembly, Grounding Rule, Hallucination Check를 확인한다.

Q. Generation Failure는 Chunk 문제가 아니야?

A. 항상 그런 것은 아니다. Context가 맞으면 Prompt나 생성 검증 문제일 가능성이 높다.

Q. Citation이 있으면 Grounded 답변이야?

A. 아니다. Citation의 실제 내용이 답변 주장과 일치해야 한다.

Q. 문서 근거가 부족하면 어떻게 해야 해?

A. 부족하다고 답하고 Unsupported Claim을 만들지 않아야 한다.

---

# 3. Core Evaluation Metrics

## 3.1 Hit@K

### [개념]

Hit@K는 기대 문서 또는 기대 Chunk가 Top-K 검색 결과 안에 포함되는지 확인하는 Retrieval 평가 지표다.

```text
Hit@K = Expected Document가 Top-K 안에 있으면 성공
```

---

### [핵심]

- Hit@1은 가장 관련 있는 문서가 첫 번째인지 확인한다.
- Hit@3은 상위 3개 안에 기대 문서가 있는지 확인한다.
- Hit@5는 검색 후보에 기대 문서가 포함되는지 확인한다.
- Hit@K는 Retrieval 성공 여부를 빠르게 판단하는 기본 지표다.
- Hit@K가 낮으면 Query, Chunk, Metadata, Embedding, Reindex를 점검한다.

---

### [실무]

Hit@K는 Golden Query 테스트에서 기본 지표로 사용한다.

예시 평가표:

| Query                      | Expected Document                     | Hit@1 | Hit@3 | Hit@5 | Note             |
| -------------------------- | ------------------------------------- | ----: | ----: | ----: | ---------------- |
| RAG 품질은 어떻게 평가해?  | RAG_Evaluation_Part01_Core.md         |     1 |     1 |     1 | 정상             |
| Top-K는 어떻게 조정해?     | RAG_Evaluation_Part04_Optimization.md |     0 |     1 |     1 | 순위 개선 필요   |
| 답변 근거는 어떻게 확인해? | RAG_Evaluation_Part03_Generation.md   |     0 |     0 |     1 | Header 보강 필요 |

Hit@K는 검색 성공 여부만 확인한다.

관련 없는 문서가 많이 섞이는지 확인하려면 Precision도 함께 봐야 한다.

---

### [FAQ]

Q. Hit@K가 뭐야?

A. 기대 문서나 기대 Chunk가 Top-K 검색 결과 안에 포함되는지 확인하는 지표다.

Q. Hit@1은 뭐야?

A. 기대 문서가 검색 결과 첫 번째에 나오는지 확인하는 지표다.

Q. Hit@5가 높으면 충분해?

A. 아니다. 기대 문서가 포함되어도 관련 없는 문서가 많으면 Precision이 낮을 수 있다.

Q. Hit@K가 낮으면 무엇을 고쳐야 해?

A. Query Rewrite, Chunk Header, FAQ, Retrieval Queries, Metadata, Reindex 여부를 점검한다.

Q. Hit@K는 Generation 품질도 평가해?

A. 아니다. Hit@K는 Retrieval 품질 평가 지표다.

---

## 3.2 Precision and Recall

### [개념]

Precision과 Recall은 Retrieval 품질을 정확도와 포괄성 관점에서 평가하는 지표다.

```text
Precision = 검색된 결과 중 관련 Chunk 비율
Recall = 필요한 관련 Chunk 중 검색된 Chunk 비율
```

---

### [핵심]

- Precision이 낮으면 관련 없는 Chunk가 많이 검색된다.
- Recall이 낮으면 필요한 Chunk가 누락된다.
- Top-K를 높이면 Recall은 올라갈 수 있다.
- Top-K를 높이면 Precision은 낮아질 수 있다.
- Chunk 구조가 나쁘면 Precision과 Recall이 모두 낮아질 수 있다.
- RAG는 Context Budget 안에서 Precision과 Recall 균형이 중요하다.

---

### [실무]

Precision / Recall 진단 기준은 아래와 같다.

| 상태                       | 의미                          | 조치                                   |
| -------------------------- | ----------------------------- | -------------------------------------- |
| Precision 낮음             | 노이즈 문서가 많음            | Top-K 감소, Threshold 조정, Chunk 분리 |
| Recall 낮음                | 필요한 문서 누락              | Top-K 증가, Query Expansion, FAQ 보강  |
| 둘 다 낮음                 | 문서 구조 또는 Embedding 문제 | Chunk 재설계, Metadata 정비            |
| Precision 높고 Recall 낮음 | 너무 좁게 검색                | Query Expansion, Filter 완화           |
| Recall 높고 Precision 낮음 | 너무 넓게 검색                | Reranking, Threshold 적용              |

실무에서는 Hit@K만 보지 않고 Precision / Recall을 함께 확인한다.

---

### [FAQ]

Q. Precision은 뭐야?

A. 검색된 결과 중 실제로 관련 있는 Chunk의 비율이다.

Q. Recall은 뭐야?

A. 필요한 관련 Chunk 중 검색에 성공한 Chunk의 비율이다.

Q. Precision이 낮으면 뭐가 문제야?

A. 검색 결과에 관련 없는 문서가 많이 섞이는 문제다.

Q. Recall이 낮으면 뭐가 문제야?

A. 답변에 필요한 문서나 Chunk가 검색되지 않는 문제다.

Q. Top-K를 올리면 Precision과 Recall은 어떻게 변해?

A. Recall은 올라갈 수 있지만 Precision은 낮아질 수 있다.

---

## 3.3 Groundedness and Faithfulness

### [개념]

Groundedness는 답변의 주요 주장이 검색 문서에 근거하는지 평가하는 기준이다.

Faithfulness는 답변이 제공된 Context를 왜곡하지 않고 충실하게 반영하는지 평가하는 기준이다.

---

### [핵심]

- Groundedness는 근거 존재 여부를 확인한다.
- Faithfulness는 Context 일치 여부를 확인한다.
- 문서에 없는 주장은 Unsupported Claim이다.
- Context 의미를 바꾸면 Faithfulness가 낮다.
- Citation이 있어도 실제 근거와 맞는지 확인해야 한다.
- 일반 지식 답변도 문서 근거가 없으면 RAG 품질은 낮다.

---

### [실무]

Groundedness / Faithfulness 검증은 Claim 단위로 수행한다.

```text
Answer Claim
→ Check Retrieved Context
→ Supported / Unsupported
→ Check Context Consistency
→ Mark Groundedness
→ Mark Faithfulness
```

검수 예시:

| Answer Claim                           | Evidence Match | Groundedness | Faithfulness | Result |
| -------------------------------------- | -------------- | ------------ | ------------ | ------ |
| Retrieval과 Generation은 분리 평가한다 | 있음           | 높음         | 높음         | 통과   |
| Top-K는 항상 크게 설정한다             | 없음           | 낮음         | 낮음         | 실패   |
| 문서 수정 후 Reindex가 필요하다        | 있음           | 높음         | 높음         | 통과   |
| Citation만 있으면 검증 완료다          | 없음           | 낮음         | 낮음         | 실패   |

---

### [FAQ]

Q. Groundedness가 뭐야?

A. 답변의 주요 주장이 검색된 문서에 근거하는지 평가하는 기준이다.

Q. Faithfulness가 뭐야?

A. 답변이 제공된 Context를 왜곡하지 않고 충실하게 반영하는지 평가하는 기준이다.

Q. Groundedness와 Faithfulness는 뭐가 달라?

A. Groundedness는 근거가 있는지 보고, Faithfulness는 근거 내용을 왜곡하지 않았는지 본다.

Q. 문서에 없는 내용이지만 사실이면 괜찮아?

A. RAG 답변에서는 낮게 평가한다. 검색 문서 근거가 없기 때문이다.

Q. Citation이 있으면 Groundedness가 높은 거야?

A. Citation 내용이 실제 답변 주장과 일치해야 Groundedness가 높다.

---

# 4. Evaluation Workflow

## 4.1 Golden Query 기반 평가

### [개념]

Golden Query는 RAG 품질 평가를 위해 미리 정의한 기준 질문이다.

Golden Query는 실제 사용자가 물어볼 법한 질문이어야 하며, Expected Document, Expected Section, Expected Answer Keyword를 포함해야 한다.

---

### [핵심]

- Golden Query는 실제 사용자 표현과 유사해야 한다.
- 각 Query에는 Expected Document를 연결한다.
- Expected Section 또는 Expected Chunk를 지정한다.
- Expected Answer Keyword를 정의한다.
- 쉬운 질문, 모호한 질문, 복합 질문을 포함한다.
- 실패 Query는 개선 후 재평가에 사용한다.

---

### [실무]

Golden Query 기본 구조:

```json
{
  "query": "RAG 품질은 어떻게 평가해?",
  "expectedDocument": "RAG_Evaluation_Retrieval_Optimization_Part01_Core.md",
  "expectedSection": "RAG Evaluation Core",
  "expectedAnswerKeywords": [
    "Retrieval Evaluation",
    "Generation Evaluation",
    "Groundedness",
    "Faithfulness"
  ],
  "difficulty": "basic",
  "domain": "RAG Evaluation",
  "intent": "evaluation_core"
}
```

평가 Flow:

```text
Create Golden Query
→ Run Retrieval
→ Check Expected Document
→ Check Expected Section
→ Generate Answer
→ Check Groundedness
→ Record Failure
→ Improve Document
→ Reindex
→ Retest
```

---

### [FAQ]

Q. Golden Query가 뭐야?

A. RAG 검색 품질을 평가하기 위해 미리 정의한 기준 질문이다.

Q. Golden Query는 문서 제목 그대로 만들면 돼?

A. 아니다. 실제 사용자가 물어볼 법한 표현으로 만들어야 한다.

Q. Golden Query에는 무엇을 넣어야 해?

A. Query, Expected Document, Expected Section, Expected Answer Keyword, Difficulty, Domain, Intent를 넣는다.

Q. 실패한 Query는 버려도 돼?

A. 아니다. 실패 Query는 문서 개선과 재평가 기준으로 사용한다.

Q. Golden Query가 너무 적으면 어떻게 돼?

A. 실제 사용자 질문 변형을 충분히 검증하지 못한다.

---

## 4.2 Evaluation Loop

### [개념]

Evaluation Loop는 RAG 품질을 반복적으로 측정하고 개선하는 운영 흐름이다.

RAG 문서는 한 번 작성하고 끝나는 것이 아니라, 실패 Query를 기반으로 계속 개선한다.

---

### [핵심]

- 평가 기준을 먼저 고정한다.
- Golden Query로 검색 결과를 확인한다.
- Retrieval 실패와 Generation 실패를 분리한다.
- 실패 원인을 기록한다.
- 문서 구조, Query, Metadata, Top-K, Prompt를 개선한다.
- 문서 수정 후 Reindex한다.
- 같은 Query로 재평가한다.
- 개선 전후 결과를 비교한다.

---

### [실무]

Evaluation Loop 기본 흐름:

```text
Define Golden Query Dataset
→ Run Retrieval Test
→ Run Generation Test
→ Analyze Failure
→ Improve RAG Document
→ Reindex
→ Retest
→ Write Quality Report
```

개선 대상 매핑:

| 실패 유형              | 우선 개선 대상                       |
| ---------------------- | ------------------------------------ |
| Expected Document 누락 | Header, FAQ, Retrieval Queries       |
| 관련 없는 Chunk 과다   | Chunk 분리, Metadata, Threshold      |
| 순위 낮음              | Reranking, Keyword Placement         |
| 답변 근거 부족         | Grounding Prompt, Citation Check     |
| Context 왜곡           | Faithfulness Check, Claim 검증       |
| 정보 누락              | Context Assembly, Completeness Check |

---

### [FAQ]

Q. Evaluation Loop는 뭐야?

A. RAG 품질을 평가하고 실패 원인을 개선한 뒤 다시 테스트하는 반복 과정이다.

Q. 문서 수정 후 왜 Reindex가 필요해?

A. Vector Index가 수정된 문서를 다시 반영해야 검색 결과가 바뀌기 때문이다.

Q. 개선 효과는 어떻게 확인해?

A. 같은 Golden Query로 재평가하고 Hit@K, Precision, Recall, Groundedness 변화를 비교한다.

Q. 실패 원인을 기록해야 해?

A. 반드시 기록해야 한다. 반복 실패와 개선 우선순위를 판단하기 위해 필요하다.

Q. 감으로 Top-K를 조정해도 돼?

A. 안 된다. 평가 결과를 보고 조정해야 한다.

---

# 5. RAG Quality Report

## 5.1 품질 리포트 기본 형식

### [개념]

RAG Quality Report는 RAG 평가 결과, 실패 원인, 개선 조치, 재평가 결과를 기록하는 문서다.

Agent는 Quality Report를 통해 RAG 시스템의 현재 품질과 개선 우선순위를 파악한다.

---

### [핵심]

- Evaluation Date를 기록한다.
- Dataset과 Query Count를 기록한다.
- Hit@K 결과를 기록한다.
- Retrieval 실패와 Generation 실패를 분리한다.
- Common Failure를 요약한다.
- Improvement Actions를 기록한다.
- Retest Result를 기록한다.
- 다음 개선 대상을 명확히 남긴다.

---

### [실무]

RAG Quality Report 예시:

```md
# RAG Quality Report

## Summary

- Evaluation Date:
- Dataset:
- Query Count:
- Hit@1:
- Hit@3:
- Hit@5:
- Main Failure:
- Next Action:

## Failure Cases

| Query                      | Expected     | Retrieved     | Failure Type | Cause       | Fix                 |
| -------------------------- | ------------ | ------------- | ------------ | ----------- | ------------------- |
| RAG 품질은 어떻게 평가해?  | Part01 Core  | Other Chunk   | Retrieval    | Header 약함 | FAQ 보강            |
| 답변 근거는 어떻게 확인해? | Groundedness | Correct Chunk | Generation   | Prompt 약함 | Grounding Rule 강화 |

## Retest Result

- Reindex:
- Retest Date:
- Improved:
- Remaining Issue:
```

Quality Report는 개선 이력 관리용이며, RAG Agent와 Review Agent가 공통으로 참조할 수 있어야 한다.

---

### [FAQ]

Q. RAG Quality Report는 뭐야?

A. RAG 평가 결과와 실패 원인, 개선 조치, 재평가 결과를 기록하는 리포트다.

Q. Quality Report에는 무엇을 적어야 해?

A. 평가 날짜, Query 수, Hit@K, 실패 유형, 원인, 수정 조치, 재평가 결과를 적는다.

Q. Quality Report는 왜 필요해?

A. RAG 품질 개선 이력을 관리하고 반복 실패를 줄이기 위해 필요하다.

Q. 실패 사례를 기록하지 않으면 어떻게 돼?

A. 같은 문제가 반복되고 개선 효과를 비교하기 어렵다.

Q. Quality Report는 사람이 보기 위한 문서야?

A. 주 목적은 Agent가 품질 상태와 개선 우선순위를 검색하기 위한 것이다.

---

# 6. Common Mistakes

## 6.1 RAG Evaluation 자주 발생하는 실수

### [개념]

RAG Evaluation에서 가장 흔한 실수는 최종 답변만 보고 품질을 판단하는 것이다.

RAG는 검색, Context 구성, 답변 생성, 근거 검증이 모두 연결된 시스템이므로 각 단계를 분리해서 평가해야 한다.

---

### [핵심]

- 최종 답변만 보고 RAG 품질을 판단한다.
- 검색 결과를 확인하지 않고 모델 문제로 단정한다.
- Golden Query 없이 감으로 평가한다.
- Hit@K만 보고 Precision / Recall을 무시한다.
- 답변이 맞아 보이면 근거 검증을 생략한다.
- Top-K를 무조건 크게 설정한다.
- Chunk 구조 문제를 LLM 문제로 오해한다.
- Metadata Filter를 너무 강하게 적용한다.
- 문서 수정 후 Reindex하지 않는다.
- 실패 사례를 기록하지 않는다.
- 개선 후 재평가하지 않는다.

---

### [실무]

실무 검수 Checklist:

```md
### [Checklist]

- [ ] Retrieval과 Generation을 분리 평가했는가?
- [ ] Golden Query가 실제 사용자 질문 형태인가?
- [ ] Expected Document가 정의되어 있는가?
- [ ] Expected Chunk가 정의되어 있는가?
- [ ] Hit@K를 확인했는가?
- [ ] Precision / Recall을 함께 확인했는가?
- [ ] Retrieved Chunks를 직접 확인했는가?
- [ ] 답변의 Unsupported Claim을 확인했는가?
- [ ] Groundedness를 검증했는가?
- [ ] Faithfulness를 검증했는가?
- [ ] 실패 원인을 기록했는가?
- [ ] 문서 수정 후 Reindex했는가?
- [ ] 같은 Golden Query로 재평가했는가?
```

---

### [FAQ]

Q. RAG 평가에서 가장 큰 실수는 뭐야?

A. 최종 답변만 보고 RAG 품질을 판단하는 것이다.

Q. 검색 결과를 확인하지 않으면 왜 위험해?

A. Retrieval 실패인지 Generation 실패인지 구분할 수 없기 때문이다.

Q. Golden Query 없이 평가해도 돼?

A. 권장하지 않는다. 기준 질문이 없으면 개선 전후 비교가 어렵다.

Q. Top-K를 크게 하면 무조건 좋아?

A. 아니다. Recall은 늘 수 있지만 노이즈가 증가해 Precision이 낮아질 수 있다.

Q. 문서 수정 후 바로 테스트하면 돼?

A. Reindex 후 같은 Golden Query로 재평가해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. RAG Evaluation은 뭐야?
A. RAG가 필요한 문서를 검색하고 검색 문서에 근거해 답변하는지 평가하는 과정이다.

Q. RAG 품질은 어떻게 평가해?
A. Retrieval Evaluation과 Generation Evaluation을 분리하고 Groundedness와 Faithfulness를 검증한다.

Q. Retrieval Evaluation은 뭐야?
A. 사용자 Query에 대해 기대 문서나 기대 Chunk가 검색 결과에 포함되는지 평가하는 것이다.

Q. Generation Evaluation은 뭐야?
A. LLM 답변이 Retrieved Context에 근거하고 질문에 맞게 생성되었는지 평가하는 것이다.

Q. RAG 실패는 어떻게 구분해?
A. 기대 문서가 검색되지 않으면 Retrieval Failure, 검색 문서는 맞지만 답변이 틀리면 Generation Failure로 본다.

Q. Retrieval Failure는 뭐야?
A. 필요한 문서나 Chunk가 Top-K 검색 결과 안에 포함되지 않는 실패다.

Q. Generation Failure는 뭐야?
A. 필요한 Context가 검색되었지만 답변이 문서 근거와 다르거나 질문 의도와 맞지 않는 실패다.

Q. Hit@K가 뭐야?
A. 기대 문서나 기대 Chunk가 Top-K 검색 결과 안에 포함되는지 확인하는 Retrieval 지표다.

Q. Hit@1은 뭐야?
A. 기대 문서가 검색 결과 첫 번째에 나오는지 확인하는 지표다.

Q. Hit@3은 뭐야?
A. 기대 문서가 상위 3개 검색 결과 안에 포함되는지 확인하는 지표다.

Q. Hit@5는 뭐야?
A. 기대 문서가 상위 5개 검색 결과 안에 포함되는지 확인하는 지표다.

Q. Precision은 뭐야?
A. 검색된 결과 중 실제로 관련 있는 Chunk의 비율이다.

Q. Recall은 뭐야?
A. 필요한 관련 Chunk 중 검색에 성공한 Chunk의 비율이다.

Q. Precision과 Recall 차이는?
A. Precision은 검색 결과의 정확도이고 Recall은 필요한 문서를 얼마나 놓치지 않았는지 보는 포괄성이다.

Q. Top-K를 높이면 뭐가 좋아져?
A. 필요한 문서가 포함될 가능성이 높아져 Recall이 올라갈 수 있다.

Q. Top-K를 높이면 뭐가 나빠져?
A. 관련 없는 문서도 함께 들어와 Precision이 낮아질 수 있다.

Q. Groundedness가 뭐야?
A. 답변의 주요 주장이 검색된 문서에 근거하는지 평가하는 기준이다.

Q. Faithfulness가 뭐야?
A. 답변이 제공된 Context를 왜곡하지 않고 충실하게 반영하는지 평가하는 기준이다.

Q. Groundedness와 Faithfulness 차이는?
A. Groundedness는 근거 존재 여부를 보고 Faithfulness는 근거 내용을 왜곡하지 않았는지 본다.

Q. 답변이 맞아 보이면 RAG 평가 통과야?
A. 아니다. RAG에서는 답변이 검색 문서에 근거하는지도 확인해야 한다.

Q. 문서에 없는 내용을 말하면 어떻게 평가해?
A. Unsupported Claim 또는 Hallucination으로 보고 품질을 낮게 평가한다.

Q. 검색 결과는 맞는데 답변이 틀리면 어디를 봐?
A. Prompt, Context Assembly, Grounding Rule, Hallucination Check를 확인한다.

Q. 문서에 있는데 검색이 안 되면 어떻게 해?
A. Chunk 제목, FAQ, Retrieval Queries, 핵심 키워드, Metadata, Reindex 여부를 확인한다.

Q. Golden Query가 뭐야?
A. RAG 검색 품질을 테스트하기 위해 미리 정의한 기준 질문이다.

Q. Golden Query에는 무엇이 필요해?
A. Query, Expected Document, Expected Section, Expected Answer Keyword, Difficulty, Domain, Intent가 필요하다.

Q. Golden Query는 어떻게 만들어?
A. 실제 사용자가 물어볼 법한 표현으로 만들고 기대 문서와 기대 답변 키워드를 연결한다.

Q. Evaluation Loop는 뭐야?
A. 평가, 실패 분석, 문서 개선, Reindex, 재평가를 반복하는 RAG 품질 개선 흐름이다.

Q. 문서 수정 후 Reindex가 왜 필요해?
A. Vector Index에 수정된 문서 내용이 반영되어야 검색 결과가 개선되기 때문이다.

Q. RAG Quality Report는 뭐야?
A. RAG 평가 결과, 실패 원인, 개선 조치, 재평가 결과를 기록하는 품질 리포트다.

Q. RAG Quality Report는 왜 필요해?
A. 검색 실패 원인과 개선 이력을 관리하고 재평가 기준을 유지하기 위해 필요하다.

Q. RAG 평가에서 가장 흔한 실수는?
A. 검색 결과를 확인하지 않고 최종 답변만 보고 품질을 판단하는 것이다.

Q. RAG 개선 후 무엇을 해야 해?
A. Reindex하고 같은 Golden Query로 Hit@K, Precision, Recall, Groundedness, Faithfulness를 재평가한다.
