# RAG Evaluation & Retrieval Optimization Part03 Generation Evaluation

---

# 1. Generation Evaluation Core

## 1.1 Generation Evaluation 기본 개념

### [개념]

Generation Evaluation은 LLM이 Retrieved Context를 근거로 정확하고 일관된 답변을 생성했는지 평가하는 과정이다.

Retrieval이 성공해도 Generation이 Context를 왜곡하거나 문서에 없는 내용을 생성하면 RAG 답변 품질은 낮다.

```text
Retrieved Context
→ Generated Answer
→ Claim Extraction
→ Evidence Match
→ Groundedness Check
→ Faithfulness Check
→ Hallucination Check
→ Revision
```

---

### [핵심]

- Generation Evaluation은 생성 답변의 품질을 평가한다.
- 핵심 질문은 “검색 문서에 근거해 답했는가?”이다.
- 답변의 주요 Claim을 Retrieved Context와 대조한다.
- 문서에 근거가 있는 Claim은 Supported Claim이다.
- 문서에 근거가 없는 Claim은 Unsupported Claim이다.
- Context 내용을 왜곡하면 Faithfulness가 낮다.
- 질문 의도와 맞지 않으면 Answer Relevance가 낮다.
- 핵심 정보를 누락하면 Answer Completeness가 낮다.

---

### [실무]

2026 실무 기준 RAG 답변 검수는 문장 단위보다 Claim 단위로 수행한다.

Generation Evaluation 기본 평가 항목은 아래와 같다.

| 평가 항목                    | 의미                              | 실패 예시                     |
| ---------------------------- | --------------------------------- | ----------------------------- |
| Answer Correctness           | 답변 내용이 정확한가              | 개념을 잘못 설명              |
| Groundedness                 | 문서 근거가 있는가                | 문서에 없는 설정값 생성       |
| Faithfulness                 | Context를 왜곡하지 않는가         | 조건, 예외, 범위를 바꿈       |
| Answer Relevance             | 질문 의도와 관련 있는가           | 불필요한 일반론 포함          |
| Answer Completeness          | 필요한 내용을 빠짐없이 포함했는가 | 핵심 절차 누락                |
| Citation Match               | 출처와 답변 내용이 일치하는가     | Citation은 있으나 근거 불일치 |
| Missing Information Handling | 정보 부족을 올바르게 처리하는가   | 근거 없이 확정 답변           |

Generation Evaluation은 Retrieval Evaluation 이후 수행한다.

Retrieved Context 자체가 틀렸다면 Generation을 평가하기 전에 Retrieval Failure로 분류해야 한다.

---

### [FAQ]

Q. Generation Evaluation은 뭐야?

A. LLM 답변이 Retrieved Context에 근거하고 질문 의도에 맞게 생성되었는지 평가하는 과정이다.

Q. Generation Evaluation의 핵심 질문은 뭐야?

A. 검색 문서에 근거해 답했는가이다.

Q. Retrieval이 성공했는데 답변이 틀리면 뭐가 문제야?

A. Prompt, Context Assembly, Grounding Rule, Hallucination Check 문제일 수 있다.

Q. Generation Evaluation은 최종 답변만 보면 돼?

A. 아니다. 답변의 주요 Claim을 Context와 대조해야 한다.

Q. Retrieved Context가 틀렸는데 답변도 틀리면 뭐부터 봐야 해?

A. 먼저 Retrieval Failure로 분류하고 검색 단계부터 개선해야 한다.

---

## 1.2 Generation Evaluation 입력과 출력

### [개념]

Generation Evaluation은 Retrieved Context, Generated Answer, User Query, Expected Answer를 함께 사용해 답변 품질을 평가한다.

답변만 단독으로 보면 RAG 근거 여부를 판단할 수 없다.

---

### [핵심]

- User Query는 답변 의도를 판단하는 기준이다.
- Retrieved Context는 답변 근거를 판단하는 기준이다.
- Generated Answer는 평가 대상이다.
- Expected Answer는 정답 방향과 필수 키워드 기준이다.
- Evaluation Result는 Pass, Partial, Fail로 기록할 수 있다.
- Failure Type은 Grounding Failure, Faithfulness Failure, Relevance Failure, Completeness Failure로 분류한다.

---

### [실무]

Generation Evaluation Case 형식:

```md
# Generation Evaluation Case

## User Query

RAG 답변이 문서에 근거했는지 어떻게 확인해?

## Retrieved Context

- Document: RAG_Evaluation_Retrieval_Optimization_Part03_Generation_Evaluation.md
- Section: Groundedness Check
- Evidence: 답변의 주요 Claim을 Retrieved Context와 대조한다.

## Generated Answer

답변의 주요 주장을 문서 근거와 비교하고, 근거 없는 내용은 Unsupported Claim으로 표시한다.

## Expected Answer Keywords

- Claim Extraction
- Evidence Match
- Supported Claim
- Unsupported Claim
- Groundedness

## Evaluation Result

- Groundedness: Pass
- Faithfulness: Pass
- Relevance: Pass
- Completeness: Pass
- Result: Pass
```

Generation Evaluation 기록은 RAG Quality Report와 연결한다.

---

### [FAQ]

Q. Generation Evaluation에는 어떤 입력이 필요해?

A. User Query, Retrieved Context, Generated Answer, Expected Answer가 필요하다.

Q. 답변만 보고 평가하면 왜 안 돼?

A. 답변이 문서 근거에 기반했는지 확인할 수 없기 때문이다.

Q. Expected Answer는 꼭 필요해?

A. Golden Query 기반 평가에서는 필요하다. 정답 방향과 필수 키워드를 판단하기 위해서다.

Q. Evaluation Result는 어떻게 기록해?

A. Groundedness, Faithfulness, Relevance, Completeness 기준으로 Pass, Partial, Fail을 기록한다.

Q. Generation 실패 유형은 어떻게 나눠?

A. Grounding Failure, Faithfulness Failure, Relevance Failure, Completeness Failure 등으로 나눈다.

---

# 2. Claim Extraction

## 2.1 Claim Extraction 기본 개념

### [개념]

Claim Extraction은 Generated Answer에서 검증 가능한 주요 주장이나 판단을 분리하는 과정이다.

RAG 답변은 문장 전체가 아니라 Claim 단위로 근거를 확인해야 한다.

---

### [핵심]

- Claim은 답변 안의 검증 가능한 주장이다.
- 하나의 문장에 여러 Claim이 포함될 수 있다.
- 절차, 조건, 수치, 설정값, 클래스명, 파일명은 Claim으로 분리한다.
- 문서에 있는 Claim은 Supported Claim으로 표시한다.
- 문서에 없는 Claim은 Unsupported Claim으로 표시한다.
- 추정이 필요한 Claim은 Assumption으로 표시한다.

---

### [실무]

Claim Extraction 예시:

```md
Generated Answer:

Top-K는 필요한 문서가 누락될 때 늘리고, 관련 없는 문서가 많을 때 줄인다.
또한 Reranking을 사용하면 관련 문서를 상위로 재정렬할 수 있다.

Extracted Claims:

| Claim                                     | Type            |
| ----------------------------------------- | --------------- |
| 필요한 문서가 누락될 때 Top-K를 늘린다    | Decision Rule   |
| 관련 없는 문서가 많을 때 Top-K를 줄인다   | Decision Rule   |
| Reranking은 관련 문서를 상위로 재정렬한다 | Technical Claim |
```

Claim Extraction 대상:

| 대상           | Claim 처리    |
| -------------- | ------------- |
| 개념 정의      | Claim         |
| 판단 기준      | Claim         |
| 수치 / 임계값  | Claim         |
| 코드 클래스명  | Claim         |
| 설정값         | Claim         |
| 파일명 / 경로  | Claim         |
| 추정 표현      | Assumption    |
| 일반 배경 설명 | 필요 시 Claim |

---

### [FAQ]

Q. Claim Extraction은 뭐야?

A. Generated Answer에서 검증 가능한 주요 주장을 분리하는 과정이다.

Q. 왜 Claim 단위로 평가해야 해?

A. 답변 일부는 맞고 일부는 근거가 없을 수 있기 때문이다.

Q. 어떤 내용을 Claim으로 봐야 해?

A. 개념 정의, 판단 기준, 수치, 설정값, 파일명, 코드 요소처럼 검증 가능한 내용을 Claim으로 본다.

Q. 추정도 Claim이야?

A. 추정은 Assumption으로 표시하고 문서 근거와 구분해야 한다.

Q. Claim Extraction을 안 하면 어떤 문제가 생겨?

A. Unsupported Claim이나 Hallucination을 놓치기 쉽다.

---

## 2.2 Supported Claim and Unsupported Claim

### [개념]

Supported Claim은 Retrieved Context에 근거가 있는 답변 주장이다.

Unsupported Claim은 Retrieved Context에서 근거를 찾을 수 없는 답변 주장이다.

RAG 답변은 Supported Claim 중심으로 구성되어야 한다.

---

### [핵심]

- Supported Claim은 문서 근거와 일치한다.
- Unsupported Claim은 문서에 없는 내용이다.
- Unsupported Claim은 Hallucination 위험 신호다.
- 일반 지식으로 맞아도 Retrieved Context에 없으면 RAG 근거는 부족하다.
- Unsupported Claim은 삭제, 축소, 또는 Assumption 표시가 필요하다.
- 근거가 부족하면 “문서 기준으로는 확인되지 않는다”고 답해야 한다.

---

### [실무]

Claim 검증 예시:

```md
# Claim Verification

| Claim                                  | Evidence in Context | Result      | Action |
| -------------------------------------- | ------------------- | ----------- | ------ |
| Retrieval과 Generation은 분리 평가한다 | 있음                | Supported   | 유지   |
| Top-K는 항상 10으로 설정한다           | 없음                | Unsupported | 삭제   |
| 문서 수정 후 Reindex가 필요하다        | 있음                | Supported   | 유지   |
| Citation이 있으면 검증이 끝난다        | 없음                | Unsupported | 수정   |
```

Unsupported Claim 처리 기준:

| 상황                               | 처리                          |
| ---------------------------------- | ----------------------------- |
| 문서에 근거 없음                   | 삭제                          |
| 추정이 필요함                      | Assumption 표시               |
| 일반 지식이지만 문서 근거 없음     | 문서 기준 확인 불가 표시      |
| 사용자 질문에 꼭 필요함            | 추가 검색 또는 근거 부족 답변 |
| 코드 생성에서 존재하지 않는 파일명 | 생성 금지                     |

---

### [FAQ]

Q. Supported Claim은 뭐야?

A. Retrieved Context에서 근거를 확인할 수 있는 답변 주장이다.

Q. Unsupported Claim은 뭐야?

A. Retrieved Context에서 근거를 찾을 수 없는 답변 주장이다.

Q. 일반 지식으로 맞으면 Unsupported Claim이어도 괜찮아?

A. RAG 평가에서는 낮게 본다. 검색 문서 근거가 없기 때문이다.

Q. Unsupported Claim은 어떻게 처리해?

A. 삭제하거나 Assumption으로 표시하거나 문서 기준으로 확인 불가라고 답한다.

Q. Unsupported Claim이 많으면 어떤 문제야?

A. Hallucination 가능성이 높고 Groundedness가 낮다.

---

# 3. Groundedness Evaluation

## 3.1 Groundedness 기본 개념

### [개념]

Groundedness는 답변의 주요 Claim이 Retrieved Context에 근거하고 있는지 평가하는 기준이다.

RAG에서는 답변이 사실처럼 보여도 문서 근거가 없으면 Groundedness가 낮다.

---

### [핵심]

- Groundedness는 문서 근거 존재 여부를 평가한다.
- Claim마다 Evidence Match를 확인한다.
- 근거가 있으면 Supported Claim이다.
- 근거가 없으면 Unsupported Claim이다.
- Citation이 있어도 실제 근거와 일치해야 한다.
- 문서에 정보가 부족하면 부족하다고 답해야 한다.
- Groundedness가 낮으면 RAG 답변 신뢰도도 낮다.

---

### [실무]

Groundedness Evaluation Flow:

```text
Generated Answer
→ Extract Claims
→ Find Evidence in Retrieved Context
→ Mark Supported Claim
→ Mark Unsupported Claim
→ Check Citation Match
→ Revise Answer
```

Groundedness 평가표:

| Claim                                        | Evidence | Groundedness | Note |
| -------------------------------------------- | -------- | ------------ | ---- |
| RAG 평가는 Retrieval과 Generation을 분리한다 | 있음     | High         | 유지 |
| Hit@K는 Generation 품질을 평가한다           | 없음     | Low          | 오류 |
| 문서 수정 후 Reindex가 필요하다              | 있음     | High         | 유지 |
| Reranking은 순위 개선에 사용할 수 있다       | 있음     | High         | 유지 |

Groundedness 판단 기준:

| 상태                        | 평가   |
| --------------------------- | ------ |
| 모든 핵심 Claim에 근거 있음 | High   |
| 일부 핵심 Claim 근거 없음   | Medium |
| 주요 Claim 대부분 근거 없음 | Low    |
| 문서와 반대되는 Claim 포함  | Fail   |

---

### [FAQ]

Q. Groundedness가 뭐야?

A. 답변의 주요 주장이 Retrieved Context에 근거하는지 평가하는 기준이다.

Q. Groundedness가 낮다는 건 무슨 뜻이야?

A. 답변에 문서 근거가 부족하거나 근거 없는 주장이 포함됐다는 뜻이다.

Q. Citation이 있으면 Groundedness가 높은 거야?

A. 아니다. Citation 내용이 실제 답변 주장과 일치해야 한다.

Q. 답변이 사실이어도 문서 근거가 없으면 어떻게 평가해?

A. RAG 기준에서는 Groundedness가 낮다.

Q. Groundedness를 높이려면 어떻게 해?

A. 답변 Claim을 Retrieved Context와 대조하고 Unsupported Claim을 제거해야 한다.

---

## 3.2 Evidence Match

### [개념]

Evidence Match는 답변 Claim과 Retrieved Context의 근거가 실제로 일치하는지 확인하는 과정이다.

Citation이나 출처가 존재하더라도 Claim과 근거 내용이 다르면 Evidence Match 실패다.

---

### [핵심]

- Evidence Match는 Claim과 Context의 의미 일치를 확인한다.
- 같은 단어가 있어도 의미가 다르면 Match가 아니다.
- Context에 조건이 있으면 답변도 조건을 유지해야 한다.
- Context의 범위를 확장하면 Evidence Match가 낮다.
- Context의 예외를 누락하면 Evidence Match가 낮다.
- Citation이 있어도 근거 문장이 Claim을 직접 지원해야 한다.

---

### [실무]

Evidence Match 평가 예시:

```md
# Evidence Match Review

Claim:
Top-K는 무조건 크게 설정해야 한다.

Retrieved Evidence:
Top-K가 높으면 Recall은 올라갈 수 있지만 Precision은 낮아질 수 있다.

Evaluation:

- Evidence Match: Fail
- Reason: Context는 조건부 조정을 말하지만 Claim은 무조건 증가를 말함
- Fix: 필요한 문서가 누락되면 Top-K 증가를 검토하고, 노이즈가 많으면 감소 또는 Reranking을 검토한다.
```

Evidence Match 실패 유형:

| 실패 유형          | 설명                 |
| ------------------ | -------------------- |
| No Evidence        | 근거 없음            |
| Weak Evidence      | 간접 근거만 있음     |
| Contradiction      | Context와 반대       |
| Overgeneralization | 조건부 내용을 일반화 |
| Missing Condition  | 조건 누락            |
| Missing Exception  | 예외 누락            |
| Wrong Citation     | 출처 내용 불일치     |

---

### [FAQ]

Q. Evidence Match는 뭐야?

A. 답변 Claim과 Retrieved Context의 근거가 실제로 일치하는지 확인하는 과정이다.

Q. 같은 키워드가 있으면 Evidence Match야?

A. 아니다. 의미와 조건이 일치해야 한다.

Q. Wrong Citation은 뭐야?

A. Citation은 있지만 해당 출처가 답변 Claim을 지원하지 않는 상태다.

Q. Evidence Match가 실패하면 어떻게 해?

A. Claim을 수정하거나 삭제하고 문서 근거에 맞게 답변을 제한한다.

Q. 조건이 있는 Context를 일반화하면 문제야?

A. 문제다. Overgeneralization으로 Faithfulness와 Groundedness가 낮아진다.

---

# 4. Faithfulness Evaluation

## 4.1 Faithfulness 기본 개념

### [개념]

Faithfulness는 답변이 Retrieved Context의 의미, 조건, 범위, 예외를 왜곡하지 않고 충실하게 반영하는지 평가하는 기준이다.

Groundedness가 근거 존재 여부를 본다면, Faithfulness는 근거를 정확하게 반영했는지 본다.

---

### [핵심]

- Faithfulness는 Context Consistency를 평가한다.
- Context 의미를 바꾸면 Faithfulness가 낮다.
- 조건부 내용을 절대 규칙처럼 말하면 문제다.
- 예외나 제한을 누락하면 문제다.
- 여러 Context를 합칠 때 충돌을 확인해야 한다.
- 요약 과정에서 의미가 바뀌면 Faithfulness 실패다.
- 코드 설명에서 조건, 책임, 예외를 누락하면 왜곡될 수 있다.

---

### [실무]

Faithfulness Evaluation Flow:

```text
Retrieved Context
→ Extract Context Conditions
→ Compare Answer Claims
→ Check Contradiction
→ Check Missing Condition
→ Check Overgeneralization
→ Revise Answer
```

Faithfulness 검수표:

| Context                           | Answer                   | Faithfulness | Issue              |
| --------------------------------- | ------------------------ | ------------ | ------------------ |
| Top-K는 평가 결과를 보고 조정한다 | Top-K는 항상 크게 한다   | Low          | Overgeneralization |
| 문서 수정 후 Reindex 필요         | 문서 수정 후 재평가 필요 | Medium       | Reindex 누락       |
| Citation도 실제 근거 확인 필요    | Citation이 있으면 충분   | Low          | Contradiction      |
| 정보 부족 시 부족하다고 답한다    | 확정 답변 생성           | Low          | Unsupported Claim  |

---

### [FAQ]

Q. Faithfulness가 뭐야?

A. 답변이 Retrieved Context를 왜곡하지 않고 충실하게 반영하는지 평가하는 기준이다.

Q. Groundedness와 Faithfulness 차이는 뭐야?

A. Groundedness는 근거가 있는지 보고, Faithfulness는 근거 내용을 왜곡하지 않았는지 본다.

Q. Faithfulness가 낮은 답변은 어떤 답변이야?

A. Context 조건, 범위, 예외를 바꾸거나 과장한 답변이다.

Q. 요약 답변도 Faithfulness 문제가 생길 수 있어?

A. 가능하다. 요약하면서 조건이나 예외를 빼면 의미가 바뀔 수 있다.

Q. Faithfulness를 높이려면 어떻게 해?

A. Context의 조건, 범위, 예외를 유지하고 Claim을 근거와 비교해야 한다.

---

## 4.2 Contradiction and Misinterpretation

### [개념]

Contradiction은 답변이 Retrieved Context와 반대되는 내용을 말하는 것이다.

Misinterpretation은 Context를 잘못 해석하여 원래 의미와 다른 답변을 생성하는 것이다.

---

### [핵심]

- Contradiction은 Context와 명확히 충돌하는 답변이다.
- Misinterpretation은 Context 의미를 잘못 해석한 답변이다.
- 둘 다 Faithfulness 실패다.
- 충돌하는 Context가 있으면 우선순위 기준이 필요하다.
- 최신 문서, 상위 Domain Rules, Project Progress 기준을 우선 적용한다.
- 모호하면 확정하지 않고 조건부로 답한다.

---

### [실무]

Contradiction / Misinterpretation 예시:

```md
# Contradiction Example

Retrieved Context:
Top-K는 평가 결과를 보고 조정한다.

Generated Answer:
Top-K는 항상 크게 설정하는 것이 좋다.

Result:

- Contradiction: Yes
- Faithfulness: Fail
- Fix: Top-K는 필요 문서 누락 시 증가를 검토하고, 노이즈가 많으면 감소 또는 Reranking을 검토한다.
```

충돌 해결 우선순위:

| 우선순위 | 기준                  |
| -------: | --------------------- |
|        1 | MASTER_RAG_RULES      |
|        2 | DOMAIN_RULES          |
|        3 | PART RULES            |
|        4 | 최신 Project Progress |
|        5 | 개별 예시 문서        |

---

### [FAQ]

Q. Contradiction은 뭐야?

A. 답변이 Retrieved Context와 반대되는 내용을 말하는 것이다.

Q. Misinterpretation은 뭐야?

A. Context를 잘못 해석해 원래 의미와 다른 답변을 생성하는 것이다.

Q. Contradiction이 있으면 어떻게 평가해?

A. Faithfulness 실패로 평가한다.

Q. Context끼리 충돌하면 어떻게 해?

A. MASTER_RAG_RULES, DOMAIN_RULES, PART RULES, 최신 Project Progress 순으로 우선순위를 적용한다.

Q. 확실하지 않으면 어떻게 답해야 해?

A. Assumption 또는 문서 기준 불확실성을 표시하고 확정 답변을 피한다.

---

# 5. Answer Relevance and Completeness

## 5.1 Answer Relevance

### [개념]

Answer Relevance는 Generated Answer가 User Query의 의도와 직접 관련 있는지 평가하는 기준이다.

RAG 답변은 문서에 근거하더라도 질문과 무관한 내용을 많이 포함하면 품질이 낮다.

---

### [핵심]

- Answer Relevance는 질문 의도와 답변의 관련도를 평가한다.
- 질문에 직접 답해야 한다.
- 관련 없는 배경 설명은 줄인다.
- 문서에 있는 내용이라도 질문과 무관하면 노이즈다.
- 복합 질문은 각 Intent에 대응해야 한다.
- Query Intent를 잘못 파악하면 Relevance가 낮다.
- 답변이 길수록 좋은 것은 아니다.

---

### [실무]

Answer Relevance 평가 예시:

```md
# Answer Relevance Review

User Query:
Precision과 Recall 차이는?

Low Relevance Answer:
RAG는 Retrieval과 Generation으로 구성되며 Vector Database를 사용한다.

High Relevance Answer:
Precision은 검색된 결과 중 관련 Chunk 비율이고, Recall은 필요한 관련 Chunk 중 검색된 비율이다.

Evaluation:

- Low Relevance Answer: 질문 핵심에 직접 답하지 않음
- High Relevance Answer: 질문 의도에 직접 대응
```

Relevance 실패 유형:

| 실패 유형      | 설명                              |
| -------------- | --------------------------------- |
| Off-topic      | 질문과 무관한 내용                |
| Over-answering | 불필요하게 넓은 답변              |
| Wrong Intent   | 질문 의도 오해                    |
| Generic Answer | 구체 질문에 일반론 답변           |
| Context Dump   | 검색 문서 내용을 그대로 과다 나열 |

---

### [FAQ]

Q. Answer Relevance는 뭐야?

A. 답변이 사용자 질문 의도와 직접 관련 있는지 평가하는 기준이다.

Q. 문서에 있는 내용을 많이 넣으면 좋은 답변이야?

A. 아니다. 질문과 무관하면 노이즈가 된다.

Q. 답변이 너무 일반적이면 왜 문제야?

A. 사용자 질문의 구체 의도에 답하지 못하기 때문이다.

Q. Answer Relevance를 높이려면 어떻게 해?

A. Query Intent를 먼저 파악하고 질문에 필요한 내용만 답변에 포함한다.

Q. Context Dump는 뭐야?

A. 검색된 문서 내용을 질문과 무관하게 과도하게 나열하는 답변이다.

---

## 5.2 Answer Completeness

### [개념]

Answer Completeness는 Generated Answer가 User Query에 답하기 위해 필요한 핵심 정보를 빠짐없이 포함했는지 평가하는 기준이다.

답변이 문서에 근거해도 핵심 단계나 조건이 빠지면 품질은 낮다.

---

### [핵심]

- Answer Completeness는 답변의 충분성을 평가한다.
- 질문에 필요한 핵심 개념을 포함해야 한다.
- 절차형 질문은 단계가 빠지면 안 된다.
- 비교형 질문은 비교 기준을 포함해야 한다.
- 원인 분석 질문은 원인과 조치를 함께 포함해야 한다.
- 문서에 정보가 부족하면 부족하다고 말해야 한다.
- Completeness는 장문 여부가 아니라 필수 정보 포함 여부다.

---

### [실무]

Completeness 평가 예시:

```md
# Answer Completeness Review

User Query:
Retrieval 실패는 어떻게 고쳐?

Incomplete Answer:
FAQ를 보강한다.

Complete Answer:
Expected Document 누락 여부를 확인하고, Query Rewrite, Header 보강, FAQ 추가, Retrieval Queries 보강, Metadata 점검, Reindex 후 재평가를 수행한다.

Evaluation:

- Incomplete: 일부 조치만 포함
- Complete: 진단과 개선, 재평가까지 포함
```

Completeness 기준:

| 질문 유형      | 필수 포함 요소   |
| -------------- | ---------------- |
| 정의 질문      | 핵심 정의        |
| 차이 질문      | 비교 기준        |
| 절차 질문      | 순서             |
| 문제 해결 질문 | 원인 + 해결      |
| 평가 질문      | 지표 + 판단 기준 |
| 개선 질문      | 조치 + 재평가    |

---

### [FAQ]

Q. Answer Completeness는 뭐야?

A. 답변이 질문에 필요한 핵심 정보를 빠짐없이 포함했는지 평가하는 기준이다.

Q. 답변이 짧으면 Completeness가 낮아?

A. 항상 그렇지는 않다. 필수 정보가 있으면 짧아도 충분할 수 있다.

Q. 긴 답변이면 Completeness가 높아?

A. 아니다. 길어도 핵심 정보가 빠지면 낮다.

Q. 절차형 질문에서 Completeness는 어떻게 봐?

A. 필요한 단계가 순서대로 포함되었는지 확인한다.

Q. 문서에 정보가 부족하면 어떻게 해?

A. 부족한 정보를 명확히 말하고 확정 답변을 피한다.

---

# 6. Hallucination Check

## 6.1 Hallucination 기본 개념

### [개념]

Hallucination은 LLM이 Retrieved Context에 없는 내용을 사실처럼 생성하는 현상이다.

RAG에서 Hallucination은 Unsupported Claim, Fabricated Detail, Wrong Citation, Missing Evidence 형태로 나타난다.

---

### [핵심]

- 문서에 없는 내용을 확정적으로 말하면 Hallucination이다.
- 존재하지 않는 클래스명, 파일명, 설정값 생성은 위험하다.
- Citation이 있어도 내용이 맞지 않으면 Wrong Citation이다.
- 답변의 주요 Claim마다 근거를 확인해야 한다.
- 근거가 없으면 답변을 제한해야 한다.
- 추정은 Assumption으로 표시해야 한다.
- 정보 부족 상황에서는 부족하다고 답해야 한다.

---

### [실무]

Hallucination Check Flow:

```text
Generated Answer
→ Extract Claims
→ Match Claims with Retrieved Context
→ Mark Unsupported Claims
→ Check Fabricated Details
→ Check Wrong Citation
→ Mark Assumption
→ Revise Answer
```

Hallucination 유형:

| 유형               | 설명                 | 예시                        |
| ------------------ | -------------------- | --------------------------- |
| Unsupported Claim  | 근거 없는 주장       | 문서에 없는 운영 규칙 단정  |
| Fabricated Detail  | 조작된 세부사항      | 없는 파일명 생성            |
| Wrong Citation     | 잘못된 출처 연결     | 출처와 답변 내용 불일치     |
| Overgeneralization | 조건부 내용을 일반화 | 항상, 무조건                |
| Missing Evidence   | 핵심 주장 근거 없음  | 근거 없이 성능 향상 단정    |
| Contradiction      | Context와 반대       | 문서 수정 후 Reindex 불필요 |

---

### [FAQ]

Q. Hallucination은 뭐야?

A. LLM이 Retrieved Context에 없는 내용을 사실처럼 생성하는 현상이다.

Q. RAG에서도 Hallucination이 발생해?

A. 발생한다. 검색 문서가 있어도 답변이 근거 없는 내용을 추가할 수 있다.

Q. Hallucination은 어떻게 확인해?

A. 답변의 주요 Claim을 Retrieved Context와 대조해 근거 없는 내용을 찾는다.

Q. Fabricated Detail은 뭐야?

A. 문서에 없는 파일명, 클래스명, 수치, 설정값 같은 세부사항을 만들어내는 것이다.

Q. Hallucination을 줄이려면 어떻게 해?

A. Grounding Rule을 강화하고 Unsupported Claim을 제거해야 한다.

---

## 6.2 Missing Information Handling

### [개념]

Missing Information Handling은 Retrieved Context에 답변 근거가 부족할 때, 부족함을 명확히 표시하고 확정 답변을 피하는 처리 방식이다.

RAG 답변에서 정보 부족을 인정하는 것은 실패가 아니라 올바른 Grounded Answer일 수 있다.

---

### [핵심]

- 문서에 정보가 없으면 없다고 말한다.
- 근거가 부족한 내용을 확정하지 않는다.
- 추정은 Assumption으로 분리한다.
- 추가 정보가 필요한 경우 필요한 정보를 명시한다.
- 문서 기준 답변과 일반 지식을 구분한다.
- Missing Information을 숨기면 Hallucination 위험이 커진다.

---

### [실무]

Missing Information 답변 패턴:

```text
문서 기준으로는 해당 내용이 확인되지 않는다.
현재 Retrieved Context에서는 [부족한 정보]가 없다.
따라서 확정 답변은 어렵고, 확인 가능한 범위는 [근거 있는 내용]이다.
```

평가 예시:

| 상황               | 나쁜 답변            | 좋은 답변                          |
| ------------------ | -------------------- | ---------------------------------- |
| 문서에 설정값 없음 | 기본값은 10이다      | 문서 기준 기본값은 확인되지 않는다 |
| 파일명 근거 없음   | 해당 파일은 Part04다 | 문서 기준 파일명은 확인되지 않는다 |
| 절차 일부 누락     | 전체 절차는 A-B-C다  | 현재 문서에는 A-B까지만 확인된다   |

---

### [FAQ]

Q. Missing Information Handling은 뭐야?

A. 문서에 답변 근거가 부족할 때 부족함을 명확히 표시하고 확정 답변을 피하는 방식이다.

Q. 모른다고 답하면 RAG 실패야?

A. 아니다. 문서에 정보가 없을 때 부족하다고 답하는 것은 올바른 Grounded Answer일 수 있다.

Q. 정보가 부족한데 추정해도 돼?

A. 추정이 필요하면 Assumption으로 표시해야 한다.

Q. 문서 기준 답변과 일반 지식은 구분해야 해?

A. 반드시 구분해야 한다. RAG 답변은 검색 문서 근거가 우선이다.

Q. 정보 부족을 숨기면 어떤 문제가 생겨?

A. Hallucination 또는 Unsupported Claim이 발생할 수 있다.

---

# 7. Generation Failure Analysis

## 7.1 Generation Failure 유형

### [개념]

Generation Failure는 Retrieved Context가 적절하지만 Generated Answer가 문서 근거와 다르거나 질문 의도에 맞지 않는 실패다.

Generation Failure는 Retrieval Failure와 구분해야 한다.

---

### [핵심]

- Retrieved Context는 맞지만 답변이 틀린다.
- Context를 왜곡한다.
- 근거 없는 Claim을 생성한다.
- Citation과 답변 내용이 맞지 않는다.
- 질문 의도와 무관한 답변을 한다.
- 핵심 정보를 누락한다.
- 정보 부족 상황에서 확정 답변을 한다.
- 충돌하는 Context를 잘못 통합한다.

---

### [실무]

Generation Failure 분류표:

| 실패 유형            | 증상           | 원인                          | 우선 조치                |
| -------------------- | -------------- | ----------------------------- | ------------------------ |
| Grounding Failure    | 근거 없는 주장 | Grounding Rule 부족           | Claim 검증               |
| Faithfulness Failure | Context 왜곡   | 조건 / 예외 누락              | Context Consistency 확인 |
| Hallucination        | 없는 내용 생성 | Unsupported Claim             | 근거 없는 내용 삭제      |
| Wrong Citation       | 출처 불일치    | Citation 검증 부족            | Evidence Match 확인      |
| Relevance Failure    | 질문과 무관    | Intent 파악 실패              | Query Intent 추출        |
| Completeness Failure | 핵심 정보 누락 | Context 압축 / 답변 구조 문제 | 필수 요소 체크           |
| Missing Info Failure | 정보 부족 숨김 | 확정 답변 강제                | 부족함 명시              |

---

### [FAQ]

Q. Generation Failure는 뭐야?

A. Retrieved Context는 적절하지만 답변이 문서 근거와 다르거나 질문 의도에 맞지 않는 실패다.

Q. Generation Failure와 Retrieval Failure는 뭐가 달라?

A. Retrieval Failure는 필요한 문서 검색 실패이고, Generation Failure는 검색된 문서를 잘못 사용한 실패다.

Q. Grounding Failure는 뭐야?

A. 답변 Claim이 Retrieved Context에 근거하지 않는 실패다.

Q. Faithfulness Failure는 뭐야?

A. 답변이 Retrieved Context의 의미, 조건, 예외를 왜곡하는 실패다.

Q. Completeness Failure는 뭐야?

A. 질문에 필요한 핵심 정보가 답변에서 누락된 실패다.

---

## 7.2 Generation Failure 진단 Flow

### [개념]

Generation Failure 진단 Flow는 답변 오류가 Grounding, Faithfulness, Relevance, Completeness, Hallucination 중 어디에서 발생했는지 확인하는 절차다.

---

### [핵심]

- 먼저 Retrieved Context가 적절한지 확인한다.
- Context가 틀리면 Retrieval Failure로 분류한다.
- Context가 맞으면 Answer Claim을 추출한다.
- Claim마다 Evidence Match를 확인한다.
- Unsupported Claim을 찾는다.
- Context 왜곡과 조건 누락을 확인한다.
- 질문 의도와 답변 관련도를 확인한다.
- 필수 정보 누락 여부를 확인한다.

---

### [실무]

Generation Failure 진단 Flow:

```text
Generated Answer
→ Check Retrieved Context
→ Is Context Relevant?
  → No: Retrieval Failure
  → Yes: Extract Claims
→ Check Evidence Match
→ Any Unsupported Claim?
  → Yes: Grounding Failure
→ Check Context Consistency
→ Any Distortion?
  → Yes: Faithfulness Failure
→ Check Query Intent
→ Off-topic?
  → Yes: Relevance Failure
→ Check Required Elements
→ Missing Core Info?
  → Yes: Completeness Failure
→ Check Missing Information Handling
→ Revise Answer
```

진단 결과별 우선 조치:

| 진단 결과                   | 우선 조치                |
| --------------------------- | ------------------------ |
| Grounding Failure           | Unsupported Claim 제거   |
| Faithfulness Failure        | Context 조건 / 예외 복원 |
| Hallucination               | Fabricated Detail 삭제   |
| Wrong Citation              | Evidence Match 재검증    |
| Relevance Failure           | Query Intent 반영        |
| Completeness Failure        | 필수 요소 추가           |
| Missing Information Failure | 정보 부족 표시           |

---

### [FAQ]

Q. Generation Failure는 어디부터 확인해?

A. 먼저 Retrieved Context가 질문과 관련 있는지 확인한다.

Q. Context가 관련 없으면 Generation Failure야?

A. 아니다. 그 경우는 Retrieval Failure로 봐야 한다.

Q. Context가 맞는데 답변이 틀리면?

A. Claim Extraction 후 Evidence Match, Groundedness, Faithfulness를 확인한다.

Q. 질문과 무관한 답변은 어떤 실패야?

A. Relevance Failure다.

Q. 핵심 정보가 빠진 답변은 어떤 실패야?

A. Completeness Failure다.

---

# 8. Generation Evaluation Report

## 8.1 Generation Evaluation Report 형식

### [개념]

Generation Evaluation Report는 생성 답변의 Groundedness, Faithfulness, Relevance, Completeness, Hallucination 여부를 기록하는 평가 리포트다.

Agent는 Report를 통해 답변 생성 단계의 실패 원인과 개선 조치를 추적한다.

---

### [핵심]

- Evaluation Date를 기록한다.
- Query와 Retrieved Context를 기록한다.
- Generated Answer 요약을 기록한다.
- Claim Verification 결과를 기록한다.
- Groundedness 평가를 기록한다.
- Faithfulness 평가를 기록한다.
- Relevance와 Completeness를 기록한다.
- Hallucination 여부를 기록한다.
- Failure Type과 Fix를 기록한다.
- Retest Result를 기록한다.

---

### [실무]

Generation Evaluation Report 예시:

```md
# Generation Evaluation Report

## Summary

- Evaluation Date: 2026-06-30
- Dataset: RAG Generation Golden Query Set v1
- Query Count: 20
- Main Failure: Unsupported Claim, Completeness Failure
- Next Action: Grounding Rule 강화, Claim 검증 추가

## Case Review

| Query                           | Groundedness | Faithfulness | Relevance | Completeness | Hallucination | Result  |
| ------------------------------- | ------------ | ------------ | --------- | ------------ | ------------- | ------- |
| RAG 품질은 어떻게 평가해?       | Pass         | Pass         | Pass      | Pass         | No            | Pass    |
| Top-K는 어떻게 조정해?          | Pass         | Partial      | Pass      | Partial      | No            | Partial |
| 문서에 없는 정보는 어떻게 답해? | Fail         | Fail         | Pass      | Partial      | Yes           | Fail    |

## Claim Verification

| Query                           | Claim                  | Evidence Match | Issue              | Fix                        |
| ------------------------------- | ---------------------- | -------------- | ------------------ | -------------------------- |
| Top-K는 어떻게 조정해?          | Top-K는 항상 크게 한다 | Fail           | Overgeneralization | 조건부 조정으로 수정       |
| 문서에 없는 정보는 어떻게 답해? | 기본값은 10이다        | Fail           | Fabricated Detail  | 문서 기준 확인 불가로 수정 |

## Retest Plan

- Update Prompt:
- Add Grounding Rule:
- Add Claim Check:
- Retest Dataset:
- Compare Failure Rate:
```

Generation Evaluation Report는 Retrieval Evaluation Report와 분리해서 관리한다.

---

### [FAQ]

Q. Generation Evaluation Report는 뭐야?

A. 생성 답변의 Groundedness, Faithfulness, Relevance, Completeness, Hallucination 여부를 기록하는 리포트다.

Q. Generation Evaluation Report에는 무엇을 적어?

A. Query, Retrieved Context, Generated Answer, Claim Verification, Failure Type, Fix, Retest Result를 적는다.

Q. Retrieval Evaluation Report와 분리해야 해?

A. 권장한다. 검색 실패와 생성 실패는 원인과 개선 방법이 다르기 때문이다.

Q. Claim Verification은 왜 Report에 넣어?

A. 어떤 답변 주장이 근거 부족인지 추적하기 위해서다.

Q. Report 작성 후 무엇을 해야 해?

A. Prompt, Grounding Rule, Context Assembly를 개선하고 같은 Query로 재평가한다.

---

# 9. Generation Evaluation Best Practice

## 9.1 Best Practice

### [개념]

Generation Evaluation Best Practice는 RAG 답변이 Retrieved Context에 근거하고, 질문 의도에 맞으며, Hallucination 없이 생성되도록 검수하는 운영 규칙이다.

Generation Evaluation은 Retrieval 성공 이후 수행해야 한다.

---

### [핵심]

- Retrieval Evaluation과 Generation Evaluation을 분리한다.
- Retrieved Context가 적절한지 먼저 확인한다.
- 답변을 Claim 단위로 분해한다.
- 각 Claim의 Evidence Match를 확인한다.
- Unsupported Claim을 제거한다.
- Groundedness를 검증한다.
- Faithfulness를 검증한다.
- Citation Match를 확인한다.
- 질문 의도와 Relevance를 확인한다.
- 필수 정보 포함 여부를 확인한다.
- 문서에 없는 정보는 부족하다고 답한다.
- 실패 유형과 개선 조치를 Report에 기록한다.

---

### [실무]

Generation Evaluation Checklist:

```md
### [Checklist]

- [ ] Retrieved Context가 Query와 관련 있는가?
- [ ] Retrieval Failure와 Generation Failure를 구분했는가?
- [ ] Generated Answer에서 Claim을 추출했는가?
- [ ] 각 Claim의 Evidence Match를 확인했는가?
- [ ] Unsupported Claim을 표시했는가?
- [ ] Fabricated Detail이 없는가?
- [ ] Wrong Citation이 없는가?
- [ ] Context 조건과 예외를 유지했는가?
- [ ] Groundedness를 평가했는가?
- [ ] Faithfulness를 평가했는가?
- [ ] Answer Relevance를 평가했는가?
- [ ] Answer Completeness를 평가했는가?
- [ ] 정보 부족 상황을 명확히 표시했는가?
- [ ] 실패 유형과 Fix를 Report에 기록했는가?
- [ ] 같은 Query로 재평가했는가?
```

---

### [FAQ]

Q. Generation Evaluation에서 가장 중요한 Best Practice는 뭐야?

A. 답변을 Claim 단위로 나누고 각 Claim이 Retrieved Context에 근거하는지 확인하는 것이다.

Q. Retrieval이 실패했는데 Generation Evaluation을 해도 돼?

A. 먼저 Retrieval Failure를 해결해야 한다. Context가 틀리면 Generation 평가 의미가 낮다.

Q. Unsupported Claim을 줄이려면 어떻게 해?

A. 답변 Claim을 Context와 대조하고 근거 없는 내용을 삭제하거나 Assumption으로 표시한다.

Q. Faithfulness를 높이려면 어떻게 해?

A. Context의 조건, 범위, 예외를 답변에서 유지해야 한다.

Q. Generation 개선 후 무엇을 해야 해?

A. 같은 Golden Query로 재평가하고 Generation Evaluation Report에 결과를 기록한다.

---

# Retrieval Queries

### [FAQ]

Q. Generation Evaluation은 뭐야?
A. LLM 답변이 Retrieved Context에 근거하고 질문 의도에 맞게 생성되었는지 평가하는 과정이다.

Q. Generation Evaluation의 핵심 질문은 뭐야?
A. 검색 문서에 근거해 답했는가이다.

Q. Generation Evaluation은 언제 수행해?
A. Retrieval Evaluation으로 Retrieved Context가 적절하다고 확인한 뒤 수행한다.

Q. Retrieval이 성공했는데 답변이 틀리면 어디를 봐?
A. Prompt, Context Assembly, Grounding Rule, Claim Verification, Hallucination Check를 확인한다.

Q. Retrieved Context가 틀렸는데 답변도 틀리면 무슨 실패야?
A. Generation Failure가 아니라 Retrieval Failure로 먼저 분류한다.

Q. Claim Extraction은 뭐야?
A. Generated Answer에서 검증 가능한 주요 주장을 분리하는 과정이다.

Q. Claim 단위로 평가해야 하는 이유는?
A. 답변 일부는 맞고 일부는 근거가 없을 수 있기 때문이다.

Q. Supported Claim은 뭐야?
A. Retrieved Context에서 근거를 확인할 수 있는 답변 주장이다.

Q. Unsupported Claim은 뭐야?
A. Retrieved Context에서 근거를 찾을 수 없는 답변 주장이다.

Q. Unsupported Claim은 어떻게 처리해?
A. 삭제하거나 Assumption으로 표시하거나 문서 기준으로 확인 불가라고 답한다.

Q. Groundedness가 뭐야?
A. 답변의 주요 주장이 Retrieved Context에 근거하는지 평가하는 기준이다.

Q. Groundedness가 낮다는 건 무슨 뜻이야?
A. 답변에 문서 근거가 부족하거나 근거 없는 주장이 포함됐다는 뜻이다.

Q. Groundedness를 높이려면 어떻게 해?
A. 답변 Claim을 Retrieved Context와 대조하고 Unsupported Claim을 제거해야 한다.

Q. Evidence Match는 뭐야?
A. 답변 Claim과 Retrieved Context의 근거가 실제로 일치하는지 확인하는 과정이다.

Q. Wrong Citation은 뭐야?
A. Citation은 있지만 해당 출처가 답변 Claim을 지원하지 않는 상태다.

Q. Evidence Match가 실패하면 어떻게 해?
A. Claim을 수정하거나 삭제하고 문서 근거에 맞게 답변을 제한한다.

Q. Faithfulness가 뭐야?
A. 답변이 Retrieved Context를 왜곡하지 않고 충실하게 반영하는지 평가하는 기준이다.

Q. Groundedness와 Faithfulness 차이는 뭐야?
A. Groundedness는 근거 존재 여부를 보고 Faithfulness는 근거 내용을 왜곡하지 않았는지 본다.

Q. Faithfulness가 낮은 답변은 어떤 답변이야?
A. Context 조건, 범위, 예외를 바꾸거나 과장한 답변이다.

Q. Contradiction은 뭐야?
A. 답변이 Retrieved Context와 반대되는 내용을 말하는 것이다.

Q. Misinterpretation은 뭐야?
A. Context를 잘못 해석해 원래 의미와 다른 답변을 생성하는 것이다.

Q. Context끼리 충돌하면 어떻게 해?
A. MASTER_RAG_RULES, DOMAIN_RULES, PART RULES, 최신 Project Progress 순으로 우선순위를 적용한다.

Q. Answer Relevance는 뭐야?
A. 답변이 사용자 질문 의도와 직접 관련 있는지 평가하는 기준이다.

Q. Answer Relevance가 낮은 답변은 뭐야?
A. 질문과 무관하거나 너무 일반적인 답변이다.

Q. Context Dump는 뭐야?
A. 검색된 문서 내용을 질문과 무관하게 과도하게 나열하는 답변이다.

Q. Answer Completeness는 뭐야?
A. 답변이 질문에 필요한 핵심 정보를 빠짐없이 포함했는지 평가하는 기준이다.

Q. Completeness Failure는 뭐야?
A. 질문에 필요한 핵심 정보가 답변에서 누락된 실패다.

Q. Hallucination은 뭐야?
A. LLM이 Retrieved Context에 없는 내용을 사실처럼 생성하는 현상이다.

Q. RAG에서도 Hallucination이 발생해?
A. 검색 문서가 있어도 답변이 근거 없는 내용을 추가하면 발생한다.

Q. Hallucination은 어떻게 확인해?
A. 답변의 주요 Claim을 Retrieved Context와 대조해 근거 없는 내용을 찾는다.

Q. Fabricated Detail은 뭐야?
A. 문서에 없는 파일명, 클래스명, 수치, 설정값 같은 세부사항을 만들어내는 것이다.

Q. Missing Information Handling은 뭐야?
A. 문서에 답변 근거가 부족할 때 부족함을 명확히 표시하고 확정 답변을 피하는 방식이다.

Q. 모른다고 답하면 RAG 실패야?
A. 아니다. 문서에 정보가 없을 때 부족하다고 답하는 것은 올바른 Grounded Answer일 수 있다.

Q. 정보가 부족한데 추정해도 돼?
A. 추정이 필요하면 Assumption으로 표시해야 한다.

Q. Generation Failure는 뭐야?
A. Retrieved Context는 적절하지만 답변이 문서 근거와 다르거나 질문 의도에 맞지 않는 실패다.

Q. Generation Failure와 Retrieval Failure 차이는?
A. Retrieval Failure는 필요한 문서 검색 실패이고 Generation Failure는 검색된 문서를 잘못 사용한 실패다.

Q. Grounding Failure는 뭐야?
A. 답변 Claim이 Retrieved Context에 근거하지 않는 실패다.

Q. Faithfulness Failure는 뭐야?
A. 답변이 Retrieved Context의 의미, 조건, 예외를 왜곡하는 실패다.

Q. Relevance Failure는 뭐야?
A. 답변이 사용자 질문 의도와 직접 관련되지 않는 실패다.

Q. Generation Failure는 어디부터 확인해?
A. 먼저 Retrieved Context가 질문과 관련 있는지 확인한다.

Q. Generation Evaluation Report는 뭐야?
A. 생성 답변의 Groundedness, Faithfulness, Relevance, Completeness, Hallucination 여부를 기록하는 리포트다.

Q. Generation Evaluation Report에는 무엇을 적어?
A. Query, Retrieved Context, Generated Answer, Claim Verification, Failure Type, Fix, Retest Result를 적는다.

Q. Generation 개선 후 무엇을 해야 해?
A. 같은 Golden Query로 재평가하고 Generation Evaluation Report에 결과를 기록한다.
