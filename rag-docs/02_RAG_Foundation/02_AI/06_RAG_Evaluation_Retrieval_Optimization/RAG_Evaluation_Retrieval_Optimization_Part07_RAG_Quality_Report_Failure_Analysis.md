# RAG Evaluation & Retrieval Optimization Part07 RAG Quality Report & Failure Analysis

---

# 1. RAG Quality Report Core

## 1.1 RAG Quality Report 기본 개념

### [개념]

RAG Quality Report는 RAG 시스템의 검색 품질, 답변 품질, 실패 원인, 개선 조치, 재평가 결과를 기록하는 품질 관리 문서다.

RAG Quality Report는 단순 결과 요약이 아니라 Agent가 RAG 시스템을 진단하고 개선 우선순위를 판단하기 위한 Retrieval 최적화 문서다.

```text
Evaluation Dataset
→ Retrieval Evaluation
→ Generation Evaluation
→ Failure Analysis
→ Improvement Action
→ Reindex
→ Retest
→ Quality Report Update
```

---

### [핵심]

- RAG Quality Report는 평가 결과와 개선 이력을 기록한다.
- Retrieval Evaluation과 Generation Evaluation을 분리해서 기록한다.
- Hit@K, Precision, Recall, MRR, Groundedness, Faithfulness를 포함한다.
- Failure Type을 명확히 분류한다.
- Failure Cause와 Fix Action을 함께 기록한다.
- 개선 후 Reindex와 Retest 여부를 기록한다.
- 동일 Golden Query 기준으로 개선 전후를 비교한다.
- Agent가 다음 개선 대상을 찾을 수 있어야 한다.

---

### [실무]

2026 실무 기준 RAG Quality Report는 아래 목적을 가진다.

| 목적          | 설명                                              |
| ------------- | ------------------------------------------------- |
| 품질 추적     | RAG 검색 / 답변 품질 변화 기록                    |
| 실패 분석     | Retrieval Failure와 Generation Failure 분리       |
| 개선 우선순위 | 반복 실패 Query와 주요 원인 식별                  |
| 회귀 테스트   | 기존 정상 Query가 깨졌는지 확인                   |
| 운영 기준     | Top-K, Threshold, Metadata, Prompt 조정 근거 관리 |
| Agent 참조    | Review Agent / RAG Agent가 개선 작업 판단         |

RAG Quality Report는 문서 수정 후 반드시 업데이트한다.

---

### [FAQ]

Q. RAG Quality Report는 뭐야?

A. RAG 평가 결과, 실패 원인, 개선 조치, 재평가 결과를 기록하는 품질 관리 문서다.

Q. RAG Quality Report는 왜 필요해?

A. RAG 품질을 감으로 판단하지 않고 평가 결과와 개선 이력으로 관리하기 위해 필요하다.

Q. Quality Report는 최종 답변 품질만 기록하면 돼?

A. 아니다. Retrieval Evaluation과 Generation Evaluation을 분리해서 기록해야 한다.

Q. Quality Report는 사람용 문서야?

A. 주 목적은 Agent가 RAG 품질 상태와 개선 우선순위를 검색하기 위한 것이다.

Q. Quality Report는 언제 업데이트해?

A. 평가 수행 후, 문서 수정 후, Reindex 후, Retest 후 업데이트한다.

---

## 1.2 Quality Report 필수 구성 요소

### [개념]

Quality Report는 평가 기준, 평가 데이터셋, 지표 결과, 실패 사례, 개선 조치, 재평가 결과를 포함해야 한다.

필수 구성 요소가 없으면 개선 전후 비교와 실패 원인 추적이 어렵다.

---

### [핵심]

- Evaluation Date를 기록한다.
- Dataset Name과 Dataset Version을 기록한다.
- Query Count를 기록한다.
- Retrieval Metrics를 기록한다.
- Generation Metrics를 기록한다.
- Common Failure를 요약한다.
- Failure Cases를 표로 기록한다.
- Improvement Actions를 기록한다.
- Reindex 여부를 기록한다.
- Retest Result를 기록한다.
- Next Action을 명확히 기록한다.

---

### [실무]

Quality Report 기본 템플릿:

```md
# RAG Quality Report

## Summary

- Evaluation Date:
- Dataset Name:
- Dataset Version:
- Query Count:
- Domain:
- Document Set:
- Main Failure:
- Overall Status:
- Next Action:

## Retrieval Metrics

| Metric      | Score | Note |
| ----------- | ----: | ---- |
| Hit@1       |       |      |
| Hit@3       |       |      |
| Hit@5       |       |      |
| Precision@5 |       |      |
| Recall@5    |       |      |
| MRR         |       |      |

## Generation Metrics

| Metric                        | Score | Note |
| ----------------------------- | ----: | ---- |
| Groundedness Pass Rate        |       |      |
| Faithfulness Pass Rate        |       |      |
| Answer Relevance Pass Rate    |       |      |
| Answer Completeness Pass Rate |       |      |
| Hallucination Rate            |       |      |

## Failure Cases

| Query | Expected | Retrieved | Failure Type | Cause | Fix |
| ----- | -------- | --------- | ------------ | ----- | --- |

## Improvement Actions

| Action | Target | Reason | Status |
| ------ | ------ | ------ | ------ |

## Retest Result

- Reindex:
- Retest Date:
- Improved:
- Remaining Issue:
```

---

### [FAQ]

Q. Quality Report에 반드시 들어가야 하는 항목은 뭐야?

A. Evaluation Date, Dataset Version, Metrics, Failure Cases, Fix Action, Retest Result가 필요하다.

Q. Dataset Version을 왜 기록해?

A. Dataset이 바뀌면 평가 결과도 달라져서 개선 전후 비교 기준이 흔들리기 때문이다.

Q. Query Count는 왜 필요해?

A. 평가 규모와 지표 신뢰도를 판단하기 위해 필요하다.

Q. Failure Cases는 왜 표로 기록해?

A. 실패 Query, 원인, 조치를 Agent가 빠르게 검색하고 재평가할 수 있도록 하기 위해서다.

Q. Next Action은 왜 필요해?

A. 다음 개선 작업의 우선순위를 명확히 하기 위해 필요하다.

---

# 2. Retrieval Quality Reporting

## 2.1 Retrieval Metrics Report

### [개념]

Retrieval Metrics Report는 검색 품질을 Hit@K, Precision, Recall, MRR, Ranking Quality 기준으로 기록하는 리포트 영역이다.

Retrieval Metrics는 필요한 문서가 검색되었는지와 검색 결과가 얼마나 정확한지 판단한다.

---

### [핵심]

- Hit@1은 기대 문서가 1순위에 있는지 확인한다.
- Hit@3은 기대 문서가 상위 3개 안에 있는지 확인한다.
- Hit@5는 기대 문서가 상위 5개 안에 있는지 확인한다.
- Precision은 검색 결과 중 관련 Chunk 비율이다.
- Recall은 필요한 관련 Chunk 중 검색된 비율이다.
- MRR은 첫 번째 관련 문서의 순위 품질이다.
- Ranking Quality는 관련 문서가 상위에 배치되는지 평가한다.
- Retrieval Metrics는 Generation Metrics와 분리한다.

---

### [실무]

Retrieval Metrics Report 예시:

```md
# Retrieval Metrics Report

## Summary

- Dataset: RAG_Evaluation_Golden_Query_Set_v1
- Query Count: 30
- Top-K: 5

## Metrics

| Metric      | Score | Interpretation                |
| ----------- | ----: | ----------------------------- |
| Hit@1       |  0.70 | 핵심 문서 상위 배치 개선 필요 |
| Hit@3       |  0.86 | 검색 후보 포함 양호           |
| Hit@5       |  0.93 | Recall 양호                   |
| Precision@5 |  0.62 | 노이즈 개선 필요              |
| Recall@5    |  0.88 | 주요 근거 대부분 검색         |
| MRR         |  0.74 | Ranking 개선 여지 있음        |

## Interpretation

- Expected Document는 대부분 Top-5 안에 포함됨
- Hit@1이 낮아 Reranking 또는 Header 보강 필요
- Precision@5가 낮아 Threshold / Metadata Filter 검토 필요
```

Retrieval Metrics는 개선 조치와 연결한다.

| 낮은 지표      | 의미                     | 우선 조치                         |
| -------------- | ------------------------ | --------------------------------- |
| Hit@1 낮음     | 기대 문서 상위 배치 약함 | Header / FAQ / Reranking          |
| Hit@5 낮음     | 기대 문서 누락           | Query Expansion / Chunk 보강      |
| Precision 낮음 | 노이즈 많음              | Threshold / Metadata / Top-K 감소 |
| Recall 낮음    | 필요한 문서 누락         | Top-K 증가 / Query Rewrite        |
| MRR 낮음       | 관련 문서 순위 낮음      | Reranking / Keyword Placement     |

---

### [FAQ]

Q. Retrieval Metrics Report는 뭐야?

A. 검색 품질을 Hit@K, Precision, Recall, MRR 기준으로 기록하는 리포트 영역이다.

Q. Hit@1이 낮으면 무슨 뜻이야?

A. 기대 문서가 검색되더라도 1순위에 잘 배치되지 않는다는 뜻이다.

Q. Hit@5가 낮으면 무슨 뜻이야?

A. 기대 문서가 검색 후보 안에 들어오지 않는 경우가 많다는 뜻이다.

Q. Precision이 낮으면 무엇을 고쳐야 해?

A. Top-K 감소, Threshold 상향, Metadata Filter, Chunk 분리를 검토한다.

Q. Recall이 낮으면 무엇을 고쳐야 해?

A. Top-K 증가, Query Expansion, Header / FAQ 보강, Filter 완화를 검토한다.

---

## 2.2 Retrieval Failure Case Report

### [개념]

Retrieval Failure Case Report는 검색 실패 Query와 원인을 개별 Case 단위로 기록하는 영역이다.

검색 실패는 Document Miss, Section Miss, Chunk Miss, Low Precision, Low Recall, Low Ranking, Filter Error, Stale Index로 분류한다.

---

### [핵심]

- Query를 원문 그대로 기록한다.
- Expected Document를 기록한다.
- Expected Section 또는 Expected Chunk를 기록한다.
- Retrieved Result를 기록한다.
- Failure Type을 기록한다.
- Cause를 기록한다.
- Fix Action을 기록한다.
- Retest Result를 기록한다.

---

### [실무]

Retrieval Failure Case Report 예시:

```md
# Retrieval Failure Case Report

| Query                          | Expected Document           | Retrieved Rank | Failure Type  | Cause                  | Fix                          | Retest  |
| ------------------------------ | --------------------------- | -------------: | ------------- | ---------------------- | ---------------------------- | ------- |
| 문서에 있는데 검색이 안 돼     | Part02_Retrieval_Evaluation |      Not Found | Document Miss | Retrieval Queries 부족 | FAQ / Retrieval Queries 추가 | Pass    |
| 관련 문서가 뒤쪽에 나와        | Part02_Retrieval_Evaluation |              5 | Low Ranking   | Header Keyword 약함    | Header 보강 / Reranking      | Partial |
| 검색 결과에 엉뚱한 문서가 많아 | Part05_Query_Chunk_Metadata |              1 | Low Precision | Filter 없음            | Metadata Filter 적용         | Pass    |
```

Failure Type별 기록 기준:

| Failure Type  | 기록 기준                                 |
| ------------- | ----------------------------------------- |
| Document Miss | Expected Document가 Top-K에 없음          |
| Section Miss  | 문서는 검색됐지만 Expected Section이 없음 |
| Chunk Miss    | Expected Chunk가 검색되지 않음            |
| Low Precision | 관련 없는 Chunk가 많음                    |
| Low Recall    | 필요한 Chunk가 누락됨                     |
| Low Ranking   | 기대 문서 순위가 낮음                     |
| Filter Error  | Metadata Filter가 문서를 제외             |
| Stale Index   | 수정 내용이 Index에 반영되지 않음         |

---

### [FAQ]

Q. Retrieval Failure Case Report는 뭐야?

A. 검색 실패 Query와 실패 원인, 개선 조치, 재평가 결과를 기록하는 영역이다.

Q. Retrieval Failure는 어떻게 분류해?

A. Document Miss, Section Miss, Chunk Miss, Low Precision, Low Recall, Low Ranking, Filter Error, Stale Index로 분류한다.

Q. Query는 원문 그대로 기록해야 해?

A. 기록하는 것이 좋다. 실제 사용자 표현을 보존해야 재평가와 Query Rewrite에 활용할 수 있다.

Q. Retrieved Rank는 왜 기록해?

A. 기대 문서가 검색되지 않았는지, 낮은 순위에 있는지 구분하기 위해 필요하다.

Q. Retest 결과는 왜 기록해?

A. 개선 조치가 실제 효과가 있었는지 확인하기 위해 필요하다.

---

# 3. Generation Quality Reporting

## 3.1 Generation Metrics Report

### [개념]

Generation Metrics Report는 생성 답변이 Retrieved Context에 근거하고 질문 의도에 맞는지 평가한 결과를 기록하는 영역이다.

Generation Metrics는 Groundedness, Faithfulness, Answer Relevance, Answer Completeness, Hallucination Rate를 중심으로 관리한다.

---

### [핵심]

- Groundedness는 답변 Claim이 문서 근거를 가지는지 평가한다.
- Faithfulness는 답변이 Context를 왜곡하지 않는지 평가한다.
- Answer Relevance는 답변이 질문 의도와 직접 관련 있는지 평가한다.
- Answer Completeness는 답변이 필요한 핵심 정보를 포함하는지 평가한다.
- Hallucination Rate는 Unsupported Claim 발생 비율이다.
- Missing Information Handling은 정보 부족을 올바르게 처리하는지 평가한다.
- Generation Metrics는 Retrieval 성공 Case 기준으로 평가하는 것이 좋다.

---

### [실무]

Generation Metrics Report 예시:

```md
# Generation Metrics Report

## Summary

- Dataset: RAG_Generation_Golden_Query_Set_v1
- Query Count: 20
- Evaluated Cases: Retrieval Success Cases

## Metrics

| Metric                 | Score | Interpretation              |
| ---------------------- | ----: | --------------------------- |
| Groundedness Pass Rate |  0.85 | 일부 Unsupported Claim 존재 |
| Faithfulness Pass Rate |  0.80 | 조건 / 예외 누락 개선 필요  |
| Relevance Pass Rate    |  0.90 | 질문 의도 대응 양호         |
| Completeness Pass Rate |  0.75 | 핵심 절차 누락 개선 필요    |
| Hallucination Rate     |  0.10 | Fabricated Detail 일부 발생 |

## Interpretation

- 답변 관련도는 양호함
- Completeness와 Faithfulness 개선 필요
- Claim Verification 강화 필요
```

Generation Metrics와 개선 조치 매핑:

| 낮은 지표          | 의미                   | 우선 조치                    |
| ------------------ | ---------------------- | ---------------------------- |
| Groundedness 낮음  | 근거 없는 Claim 많음   | Claim Verification 강화      |
| Faithfulness 낮음  | Context 왜곡           | 조건 / 예외 유지             |
| Relevance 낮음     | 질문 의도 불일치       | Intent Extraction 개선       |
| Completeness 낮음  | 핵심 정보 누락         | Expected Answer Pattern 보강 |
| Hallucination 높음 | Unsupported Claim 많음 | Grounding Rule 강화          |

---

### [FAQ]

Q. Generation Metrics Report는 뭐야?

A. 생성 답변의 Groundedness, Faithfulness, Relevance, Completeness, Hallucination 결과를 기록하는 영역이다.

Q. Groundedness Pass Rate는 뭐야?

A. 답변 Claim이 Retrieved Context에 근거한 비율이다.

Q. Faithfulness Pass Rate는 뭐야?

A. 답변이 Context를 왜곡하지 않고 충실하게 반영한 비율이다.

Q. Hallucination Rate가 높으면 무엇을 고쳐야 해?

A. Claim Verification, Grounding Rule, Missing Information Handling을 강화해야 한다.

Q. Generation Metrics는 Retrieval 실패 Case에도 평가해?

A. Retrieval 실패 Case는 먼저 Retrieval Failure로 분류하고, Generation 평가는 Retrieval 성공 Case 중심으로 수행하는 것이 좋다.

---

## 3.2 Generation Failure Case Report

### [개념]

Generation Failure Case Report는 Retrieved Context가 적절했지만 Generated Answer가 문서 근거와 다르거나 질문 의도에 맞지 않았던 실패를 기록하는 영역이다.

Generation Failure는 Grounding Failure, Faithfulness Failure, Relevance Failure, Completeness Failure, Hallucination, Wrong Citation, Missing Information Failure로 분류한다.

---

### [핵심]

- Query를 기록한다.
- Retrieved Context를 기록한다.
- Generated Answer 요약을 기록한다.
- Failed Claim을 기록한다.
- Evidence Match 결과를 기록한다.
- Failure Type을 기록한다.
- Fix Action을 기록한다.
- Retest Result를 기록한다.

---

### [실무]

Generation Failure Case Report 예시:

```md
# Generation Failure Case Report

| Query                           | Failed Claim               | Evidence Match | Failure Type         | Cause               | Fix                          | Retest |
| ------------------------------- | -------------------------- | -------------- | -------------------- | ------------------- | ---------------------------- | ------ |
| Top-K는 무조건 크게 하면 돼?    | Top-K는 항상 크게 설정한다 | Fail           | Faithfulness Failure | 조건부 기준 왜곡    | Precision / Recall 조건 추가 | Pass   |
| 문서에 없는 정보는 어떻게 답해? | 기본값은 10이다            | Fail           | Hallucination        | Fabricated Detail   | 문서 기준 확인 불가 처리     | Pass   |
| 답변 근거는 어떻게 확인해?      | Citation이 있으면 충분하다 | Fail           | Wrong Citation       | Evidence Match 누락 | Citation Match 검증 추가     | Pass   |
```

Generation Failure 분류 기준:

| Failure Type                | 기준                         |
| --------------------------- | ---------------------------- |
| Grounding Failure           | Claim 근거 없음              |
| Faithfulness Failure        | Context 조건 / 예외 왜곡     |
| Relevance Failure           | 질문 의도와 답변 불일치      |
| Completeness Failure        | 핵심 정보 누락               |
| Hallucination               | 문서에 없는 내용 생성        |
| Wrong Citation              | 출처와 Claim 불일치          |
| Missing Information Failure | 정보 부족을 숨기고 확정 답변 |

---

### [FAQ]

Q. Generation Failure Case Report는 뭐야?

A. 생성 답변 실패 Claim과 원인, 개선 조치, 재평가 결과를 기록하는 영역이다.

Q. Failed Claim은 왜 기록해?

A. 어떤 답변 주장이 문서 근거와 맞지 않았는지 추적하기 위해 필요하다.

Q. Evidence Match는 왜 필요해?

A. 답변 Claim과 Retrieved Context가 실제로 일치하는지 확인하기 위해 필요하다.

Q. Generation Failure는 어떻게 분류해?

A. Grounding Failure, Faithfulness Failure, Relevance Failure, Completeness Failure, Hallucination, Wrong Citation 등으로 분류한다.

Q. Retest는 어떻게 해?

A. 같은 Query와 같은 Expected Answer 기준으로 답변을 다시 생성하고 Claim 검증을 수행한다.

---

# 4. Failure Analysis

## 4.1 Failure Analysis 기본 개념

### [개념]

Failure Analysis는 RAG 실패가 검색 문제인지, 생성 문제인지, Context 구성 문제인지, 문서 구조 문제인지 분류하고 원인을 찾는 과정이다.

RAG 실패는 최종 답변만 보고 판단하지 않는다.

```text
Failed Answer
→ Check Retrieval Result
→ Check Expected Document
→ Check Retrieved Context
→ Check Generated Claims
→ Classify Failure Type
→ Identify Root Cause
→ Define Fix Action
```

---

### [핵심]

- 실패 분석은 Retrieval부터 시작한다.
- Expected Document가 없으면 Retrieval Failure다.
- Expected Context가 맞는데 답변이 틀리면 Generation Failure다.
- Context가 맞지만 순서나 압축이 나쁘면 Context Assembly 문제다.
- 문서에 핵심 키워드가 없으면 Chunk Optimization 대상이다.
- Metadata Filter가 문서를 제외하면 Filter Error다.
- 실패 원인은 Fix Action과 연결되어야 한다.
- 실패 분석 후 같은 Query로 Retest한다.

---

### [실무]

Failure Analysis Decision Tree:

```text
User Query Failed
→ Is Expected Document in Top-K?
  → No: Retrieval Failure
  → Yes: Check Expected Chunk
→ Is Expected Chunk present?
  → No: Chunk Miss
  → Yes: Check Context Assembly
→ Is Context used correctly?
  → No: Context Assembly Failure
  → Yes: Check Generated Answer
→ Are Claims supported?
  → No: Grounding Failure
  → Yes: Check Faithfulness
→ Is Context distorted?
  → Yes: Faithfulness Failure
  → No: Check Relevance / Completeness
```

Failure Analysis 결과 기록:

| 항목          | 기록 내용                        |
| ------------- | -------------------------------- |
| Failed Query  | 실제 실패 Query                  |
| Expected      | 기대 문서 / Section / Chunk      |
| Observed      | 실제 검색 / 답변 결과            |
| Failure Layer | Retrieval / Context / Generation |
| Failure Type  | 세부 실패 유형                   |
| Root Cause    | 근본 원인                        |
| Fix Action    | 수정 조치                        |
| Retest Query  | 재평가 Query                     |

---

### [FAQ]

Q. Failure Analysis는 뭐야?

A. RAG 실패 원인이 검색, 생성, Context 구성, 문서 구조 중 어디에 있는지 분석하는 과정이다.

Q. RAG 실패는 어디부터 분석해?

A. 먼저 Expected Document가 검색 결과에 있는지 확인한다.

Q. Expected Document가 없으면 무슨 실패야?

A. Retrieval Failure다.

Q. Context는 맞는데 답변이 틀리면 무슨 실패야?

A. Generation Failure 또는 Context Assembly Failure다.

Q. Failure Analysis 후 무엇을 해야 해?

A. Root Cause에 맞는 Fix Action을 적용하고 같은 Query로 Retest한다.

---

## 4.2 Root Cause Analysis

### [개념]

Root Cause Analysis는 RAG 실패의 표면 증상보다 근본 원인을 찾는 과정이다.

예를 들어 Hit@K 실패는 Top-K 문제처럼 보일 수 있지만 실제 원인은 Header 불명확, FAQ 부족, Metadata 오류, Reindex 누락일 수 있다.

---

### [핵심]

- 증상과 원인을 구분한다.
- 단일 실패에 여러 원인이 있을 수 있다.
- Top-K 조정만으로 해결되지 않는 실패가 많다.
- 문서 구조 문제는 반복 실패를 만든다.
- Metadata 오류는 특정 Agent / Domain 검색 실패를 만든다.
- Reindex 누락은 수정 후에도 검색 결과가 변하지 않는 원인이다.
- Root Cause는 Fix Action과 직접 연결한다.

---

### [실무]

Root Cause Mapping:

| 증상                   | 가능한 Root Cause            | 확인 방법                      |
| ---------------------- | ---------------------------- | ------------------------------ |
| Expected Document 누락 | Header 약함                  | Header에 핵심 용어 있는지 확인 |
| Expected Document 누락 | Retrieval Queries 부족       | 사용자형 Query 포함 여부 확인  |
| Expected Document 누락 | Metadata Filter 오류         | Domain / Level / Tags 확인     |
| 검색 결과 변화 없음    | Reindex 누락                 | Index 업데이트 여부 확인       |
| 노이즈 많음            | Chunk 혼합                   | Single Concept Chunk 여부 확인 |
| 답변 근거 없음         | Grounding Rule 약함          | Claim Verification 확인        |
| 답변 왜곡              | Context 조건 누락            | Faithfulness Check 확인        |
| 답변 누락              | Expected Answer Pattern 없음 | Completeness 기준 확인         |

Root Cause 기록 예시:

```md
# Root Cause Analysis

## Failed Query

문서에 있는데 검색이 안 돼

## Symptom

Expected Document가 Top-5에 없음

## Candidate Causes

- Header Keyword 부족
- Retrieval Queries에 사용자형 질문 없음
- Metadata domain 값 불일치
- Reindex 누락

## Confirmed Root Cause

- Retrieval Queries 부족
- Reindex 누락

## Fix Action

- Retrieval Queries에 문제 상황형 Query 추가
- Reindex 수행
- 같은 Query로 Retest
```

---

### [FAQ]

Q. Root Cause Analysis는 뭐야?

A. RAG 실패의 표면 증상보다 근본 원인을 찾는 과정이다.

Q. Hit@K가 낮으면 무조건 Top-K 문제야?

A. 아니다. Header, FAQ, Metadata, Query, Reindex 문제일 수 있다.

Q. 검색 결과가 수정 후에도 그대로면 원인이 뭐야?

A. Reindex 누락 가능성이 높다.

Q. 노이즈가 많은 검색 결과의 원인은 뭐야?

A. Chunk 혼합, Top-K 과다, Threshold 낮음, Metadata Filter 부족일 수 있다.

Q. Root Cause는 왜 Fix Action과 연결해야 해?

A. 원인과 무관한 조치를 하면 개선 효과가 낮기 때문이다.

---

# 5. Improvement Action Tracking

## 5.1 Improvement Action 기본 개념

### [개념]

Improvement Action은 Failure Analysis 결과에 따라 수행할 구체적인 개선 조치다.

Improvement Action은 Query, Chunk, Metadata, Top-K, Threshold, Reranking, Context Assembly, Prompt, Grounding Rule 중 하나 이상을 대상으로 한다.

---

### [핵심]

- Improvement Action은 Failure Type과 연결한다.
- 조치 대상 문서나 설정을 명확히 기록한다.
- 조치 이유를 기록한다.
- 조치 상태를 기록한다.
- Reindex 필요 여부를 기록한다.
- Retest 대상 Query를 기록한다.
- 조치 후 Regression Check를 수행한다.

---

### [실무]

Improvement Action Tracking 예시:

```md
# Improvement Action Tracking

| Action ID | Failure Type  | Target            | Action                      | Reindex | Retest Query                    | Status      |
| --------- | ------------- | ----------------- | --------------------------- | ------- | ------------------------------- | ----------- |
| IA-001    | Document Miss | Part02 Retrieval  | Retrieval Queries 추가      | Yes     | 문서에 있는데 검색이 안 돼      | Done        |
| IA-002    | Low Ranking   | Part03 Generation | Header Keyword 보강         | Yes     | Hallucination은 어떻게 확인해?  | In Progress |
| IA-003    | Hallucination | Prompt Rule       | Unsupported Claim 금지 추가 | No      | 문서에 없는 정보는 어떻게 답해? | Done        |
| IA-004    | Low Precision | Metadata          | Domain Filter 적용          | No      | 검색 결과에 엉뚱한 문서가 많아  | Planned     |
```

Improvement Action 매핑:

| Failure Type         | Action                                        |
| -------------------- | --------------------------------------------- |
| Document Miss        | Header / FAQ / Retrieval Queries 보강         |
| Section Miss         | Section Header 개선                           |
| Chunk Miss           | Chunk 분리 / Keyword Placement                |
| Low Precision        | Threshold 상향 / Metadata Filter / Top-K 감소 |
| Low Recall           | Top-K 증가 / Query Expansion / Filter 완화    |
| Low Ranking          | Reranking / Header 보강                       |
| Grounding Failure    | Claim Verification / Prompt 강화              |
| Faithfulness Failure | 조건 / 예외 유지 규칙 강화                    |
| Hallucination        | Unsupported Claim 제거 규칙 추가              |
| Completeness Failure | Expected Answer Pattern 보강                  |

---

### [FAQ]

Q. Improvement Action은 뭐야?

A. Failure Analysis 결과에 따라 수행할 구체적인 개선 조치다.

Q. Improvement Action은 무엇과 연결해야 해?

A. Failure Type, Target, Reason, Retest Query와 연결해야 한다.

Q. 문서 수정 Action에는 Reindex가 필요해?

A. 필요하다. 문서 내용이 바뀌면 Vector Index를 다시 반영해야 한다.

Q. Prompt 수정도 Reindex가 필요해?

A. 보통 문서 Index 수정은 아니므로 필요하지 않지만 Retest는 필요하다.

Q. Improvement Action 후 무엇을 해야 해?

A. 같은 Golden Query로 Retest하고 Regression Check를 수행한다.

---

## 5.2 Reindex and Retest Tracking

### [개념]

Reindex and Retest Tracking은 문서 수정이 Vector Index에 반영되었는지와 개선 효과가 평가로 확인되었는지 기록하는 과정이다.

문서 수정만 하고 Reindex를 하지 않으면 Retrieval 품질은 개선되지 않을 수 있다.

---

### [핵심]

- 문서 내용 수정 후 Reindex가 필요하다.
- FAQ, Retrieval Queries, Header 수정도 Reindex 대상이다.
- Metadata 수정 후 Index 반영 여부를 확인한다.
- Retest는 같은 Golden Query로 수행한다.
- Retest 결과를 Baseline과 비교한다.
- 개선되지 않으면 Root Cause를 다시 분석한다.
- Reindex 상태는 Quality Report에 반드시 기록한다.

---

### [실무]

Reindex / Retest 기록 예시:

```md
# Reindex and Retest Tracking

## Modified Document

RAG_Evaluation_Retrieval_Optimization_Part05_Query_Chunk_Metadata_Optimization.md

## Change

- Retrieval Queries 추가
- Metadata tags 보강
- Header Keyword 수정

## Reindex

- Required: Yes
- Completed: Yes
- Reindex Date: 2026-06-30

## Retest

| Query                        | Before     | After      | Result     |
| ---------------------------- | ---------- | ---------- | ---------- |
| Query Rewrite는 뭐야?        | Hit@3 Pass | Hit@3 Pass | Maintained |
| 문서에 있는데 검색이 안 돼   | Hit@5 Fail | Hit@3 Pass | Improved   |
| Metadata Filter는 왜 필요해? | Hit@3 Pass | Hit@3 Fail | Regression |

## Action

- Regression Query 기준 Metadata Header 재검토
```

---

### [FAQ]

Q. Reindex Tracking은 뭐야?

A. 문서 수정 내용이 Vector Index에 반영되었는지 기록하는 과정이다.

Q. Retest Tracking은 뭐야?

A. 개선 후 같은 Query로 품질이 좋아졌는지 기록하는 과정이다.

Q. FAQ만 수정해도 Reindex가 필요해?

A. 필요하다. FAQ도 검색 대상 문서 내용이기 때문이다.

Q. Retest는 왜 같은 Golden Query로 해야 해?

A. 같은 조건에서 개선 전후를 비교해야 하기 때문이다.

Q. Retest에서 Regression이 나오면 어떻게 해?

A. 영향을 받은 Query 기준으로 수정 범위를 재검토하고 다시 Reindex / Retest한다.

---

# 6. Regression Report

## 6.1 Regression Report 기본 개념

### [개념]

Regression Report는 개선 작업 이후 기존에 정상 동작하던 Query의 검색 품질이나 답변 품질이 나빠졌는지 기록하는 리포트다.

RAG 문서 개선은 특정 Query를 개선하면서 다른 Query를 악화시킬 수 있다.

---

### [핵심]

- 기존 통과 Query를 다시 평가한다.
- 같은 Domain의 인접 Part Query를 포함한다.
- Core Query Set을 포함한다.
- Failure-based Query를 포함한다.
- Hit@K 하락 여부를 확인한다.
- Precision / Recall 하락 여부를 확인한다.
- Groundedness / Faithfulness 하락 여부를 확인한다.
- Regression 발생 시 원인을 기록한다.
- Regression Fix 후 다시 Retest한다.

---

### [실무]

Regression Report 예시:

```md
# Regression Report

## Change Summary

- Modified Document: Part05 Query / Chunk / Metadata Optimization
- Change Type: Metadata Tags Update
- Reindex: Completed

## Regression Query Set

| Query                        | Before     | After      | Status     |
| ---------------------------- | ---------- | ---------- | ---------- |
| Query Rewrite는 뭐야?        | Hit@3 Pass | Hit@3 Pass | Maintained |
| Chunk Optimization은 뭐야?   | Hit@3 Pass | Hit@3 Pass | Maintained |
| Metadata Filter는 왜 필요해? | Hit@3 Pass | Hit@3 Fail | Regression |
| 문서 수정 후 무엇을 해야 해? | Hit@3 Pass | Hit@3 Pass | Maintained |

## Regression Analysis

- Regression Type: Metadata Filter Failure
- Root Cause: tag value mismatch
- Fix Action: Metadata tag normalization
- Retest Required: Yes
```

Regression 대상 Query:

| Query Set               | 이유                       |
| ----------------------- | -------------------------- |
| Core Query Set          | 핵심 문서 검색성 유지      |
| Modified Document Query | 수정 문서 내부 검색성 확인 |
| Adjacent Part Query     | 문서 간 충돌 확인          |
| Metadata Filter Query   | 필터 부작용 확인           |
| Failure-based Query     | 과거 실패 재발 방지        |

---

### [FAQ]

Q. Regression Report는 뭐야?

A. 개선 작업 이후 기존 정상 Query의 품질이 나빠졌는지 기록하는 리포트다.

Q. Regression Check는 왜 필요해?

A. 특정 Query를 개선하면서 다른 Query 검색성이 나빠질 수 있기 때문이다.

Q. Regression Query Set에는 무엇을 넣어?

A. Core Query, 수정 문서 Query, 인접 Part Query, Metadata Filter Query, Failure-based Query를 넣는다.

Q. Regression이 발생하면 어떻게 해?

A. Root Cause를 분석하고 수정 후 Reindex와 Retest를 다시 수행한다.

Q. Regression Report는 Quality Report와 분리해?

A. 분리해도 되고 Quality Report 내부 Section으로 포함해도 된다.

---

# 7. Quality Score and Status

## 7.1 Quality Score 기준

### [개념]

Quality Score는 RAG 문서 세트의 검색 품질과 답변 품질을 종합적으로 판단하기 위한 점수다.

Quality Score는 단순 평균이 아니라 Retrieval, Generation, Failure, Regression 상태를 함께 반영해야 한다.

---

### [핵심]

- Retrieval Metrics를 반영한다.
- Generation Metrics를 반영한다.
- Hallucination Rate를 반영한다.
- Failure Case 수를 반영한다.
- Regression 발생 여부를 반영한다.
- 치명적 실패는 별도로 표시한다.
- 점수보다 실패 유형과 Next Action이 더 중요하다.

---

### [실무]

Quality Score 예시:

```md
# Quality Score

## Score Summary

| Area                 | Weight | Score |
| -------------------- | -----: | ----: |
| Retrieval Quality    |     35 |    30 |
| Generation Quality   |     35 |    29 |
| Failure Handling     |     15 |    12 |
| Regression Stability |     15 |    13 |
| Total                |    100 |    84 |

## Status

- Quality Status: Needs Improvement
- Critical Issue: No
- Main Weakness: Precision@5 low, Completeness partial
- Next Action: Metadata Filter and Expected Answer Pattern 개선
```

Quality Status 기준:

|  Score | Status            | 의미                   |
| -----: | ----------------- | ---------------------- |
| 95~100 | Excellent         | 운영 가능, 안정적      |
|  90~94 | Good              | 일부 개선 후 운영 가능 |
|  80~89 | Needs Improvement | 개선 필요              |
|  70~79 | Risky             | 주요 실패 반복         |
|   0~69 | Fail              | 운영 투입 부적합       |

치명적 실패는 Score와 별도로 기록한다.

---

### [FAQ]

Q. Quality Score는 뭐야?

A. RAG 문서 세트의 검색 품질과 답변 품질을 종합적으로 판단하기 위한 점수다.

Q. Quality Score만 보면 충분해?

A. 아니다. Failure Type, Critical Issue, Next Action을 함께 봐야 한다.

Q. 높은 점수라도 치명적 실패가 있으면 괜찮아?

A. 아니다. 치명적 실패는 점수와 별도로 우선 처리해야 한다.

Q. 95점 이상이면 어떤 상태야?

A. 검색과 답변 품질이 안정적인 Excellent 상태로 볼 수 있다.

Q. 80점대면 어떻게 해야 해?

A. 운영 전 주요 Failure Case를 개선하고 Regression Check를 수행해야 한다.

---

## 7.2 Critical Issue 기준

### [개념]

Critical Issue는 RAG 문서 세트의 운영 신뢰도를 크게 떨어뜨리는 치명적 문제다.

Critical Issue가 있으면 전체 Quality Score가 높아도 우선 해결해야 한다.

---

### [핵심]

- Expected Document가 반복적으로 검색되지 않으면 Critical Issue다.
- Hallucination이 반복되면 Critical Issue다.
- Master Rules와 충돌하는 문서가 있으면 Critical Issue다.
- Domain Rules와 Part 문서가 충돌하면 Critical Issue다.
- 문서 수정 후 Reindex가 누락되면 Critical Issue다.
- Metadata Filter가 핵심 문서를 제외하면 Critical Issue다.
- 동일 실패가 반복되면 Critical Issue 후보로 본다.

---

### [실무]

Critical Issue 분류표:

| Critical Issue         | 기준                       | 우선 조치                             |
| ---------------------- | -------------------------- | ------------------------------------- |
| Core Document Miss     | 핵심 문서 반복 누락        | Header / FAQ / Retrieval Queries 보강 |
| Unsupported Claim 반복 | 근거 없는 답변 반복        | Grounding Rule 강화                   |
| Hallucination 반복     | 없는 파일명 / 설정값 생성  | Claim Verification 강화               |
| Rule Conflict          | Master / Domain Rules 충돌 | 상위 Rule 기준 수정                   |
| Stale Index            | 수정 반영 안 됨            | Reindex 수행                          |
| Metadata Exclusion     | 필터로 핵심 문서 제외      | Metadata Schema 수정                  |
| Regression 반복        | 기존 Query 계속 악화       | 수정 범위 재검토                      |

Critical Issue Report 예시:

```md
# Critical Issue Report

## Issue

Core Document Miss

## Evidence

- Query: RAG 품질은 어떻게 평가해?
- Expected Document: Part01_Core
- Result: Top-5 Not Found
- Occurrence: 3 / 5 Retest

## Impact

- Core Evaluation Query 검색 실패
- Agent가 RAG Evaluation 기본 구조를 찾지 못함

## Fix

- Part01 Header 보강
- FAQ 추가
- Retrieval Queries 보강
- Reindex
- Retest Core Query Set
```

---

### [FAQ]

Q. Critical Issue는 뭐야?

A. RAG 문서 세트의 운영 신뢰도를 크게 떨어뜨리는 치명적 문제다.

Q. Quality Score가 높아도 Critical Issue가 있으면 괜찮아?

A. 아니다. Critical Issue는 점수와 별도로 우선 해결해야 한다.

Q. 어떤 문제가 Critical Issue야?

A. 핵심 문서 반복 누락, Hallucination 반복, Rule 충돌, Reindex 누락, Metadata Exclusion 등이 있다.

Q. Critical Issue는 어떻게 기록해?

A. Issue, Evidence, Impact, Fix, Retest 결과를 기록한다.

Q. Critical Issue 해결 후 무엇을 해야 해?

A. 관련 Golden Query와 Regression Query Set으로 재평가해야 한다.

---

# 8. Final Review Workflow

## 8.1 문서 세트 최종 검수 Flow

### [개념]

Final Review Workflow는 RAG 문서 세트 제작 후 품질, 연결성, 규칙 준수, 치명적 문제를 최종 확인하는 절차다.

최종 검수는 단일 문서가 아니라 문서 세트 전체 기준으로 수행한다.

---

### [핵심]

- MASTER_RAG_RULES 준수 여부를 확인한다.
- DOMAIN_RULES 준수 여부를 확인한다.
- PROJECT_PROGRESS와 문서 위치를 확인한다.
- Part 간 역할 중복과 누락을 확인한다.
- 용어 일관성을 확인한다.
- FAQ와 Retrieval Queries를 확인한다.
- Code Block에 불필요한 id 속성이 없는지 확인한다.
- Retrieval / Generation / Optimization / Report 흐름이 연결되는지 확인한다.
- Critical Issue가 없는지 확인한다.

---

### [실무]

Final Review Checklist:

```md
### [Checklist]

- [ ] MASTER_RAG_RULES를 준수했는가?
- [ ] DOMAIN_RULES를 준수했는가?
- [ ] PROJECT_PROGRESS의 Level / Domain 구조와 맞는가?
- [ ] 모든 문서에 [개념], [핵심], [실무], [FAQ]가 있는가?
- [ ] 모든 문서에 Retrieval Queries가 있는가?
- [ ] FAQ는 Q + A 구조인가?
- [ ] FAQ 내부에 무분별한 구분선이 없는가?
- [ ] Code Block에 id 속성이 없는가?
- [ ] Retrieval Evaluation과 Generation Evaluation이 분리되었는가?
- [ ] Golden Query와 Quality Report가 연결되는가?
- [ ] Query / Chunk / Metadata / Top-K / Context Optimization 흐름이 연결되는가?
- [ ] Part 간 중복이 과도하지 않은가?
- [ ] Part 간 핵심 개념 누락이 없는가?
- [ ] 용어가 일관되는가?
- [ ] Critical Issue가 없는가?
```

최종 검수 통과 기준:

| 항목     | 기준                            |
| -------- | ------------------------------- |
| 구조     | 필수 Section 모두 포함          |
| 검색성   | FAQ / Retrieval Queries 충분    |
| 연결성   | Part 간 Flow 연결               |
| 정확성   | Domain Rules 위반 없음          |
| 안정성   | Critical Issue 없음             |
| 재평가성 | Golden Query / Report 기준 존재 |

---

### [FAQ]

Q. Final Review Workflow는 뭐야?

A. RAG 문서 세트 제작 후 규칙 준수, 연결성, 검색성, 치명적 문제를 최종 확인하는 절차다.

Q. 최종 검수는 단일 문서만 보면 돼?

A. 아니다. 문서 세트 전체의 역할 분담과 연결성을 함께 확인해야 한다.

Q. Code Block id 속성은 왜 확인해?

A. 출력 규칙상 코드블록 id 속성을 제거해야 하기 때문이다.

Q. Part 간 연결성은 어떻게 확인해?

A. Core → Retrieval → Generation → Golden Query → Optimization → Report 흐름이 이어지는지 확인한다.

Q. 최종 검수에서 Critical Issue가 있으면?

A. 작업 완료로 보지 않고 해당 문제를 수정한 뒤 재검수한다.

---

## 8.2 Part 간 연계 기준

### [개념]

Part 간 연계 기준은 RAG Evaluation & Retrieval Optimization 문서 세트의 각 Part가 어떤 역할을 담당하고 어떻게 연결되는지 정의하는 기준이다.

문서 세트는 독립 검색 가능해야 하면서도 전체 평가 / 개선 흐름이 이어져야 한다.

---

### [핵심]

- Part01은 전체 Core와 평가 구조를 담당한다.
- Part02는 Retrieval Evaluation을 담당한다.
- Part03은 Generation Evaluation을 담당한다.
- Part04는 Golden Query와 Test Dataset을 담당한다.
- Part05는 Query / Chunk / Metadata Optimization을 담당한다.
- Part06은 Top-K / Threshold / Reranking / Context Optimization을 담당한다.
- Part07은 Quality Report와 Failure Analysis를 담당한다.
- 모든 Part는 Retrieval Queries로 상호 검색 가능해야 한다.

---

### [실무]

Part 간 연계표:

| Part                            | 역할                     | 연결 대상              |
| ------------------------------- | ------------------------ | ---------------------- |
| Part01 Core                     | 전체 평가 구조           | Part02, Part03, Part07 |
| Part02 Retrieval Evaluation     | 검색 품질 평가           | Part04, Part05, Part06 |
| Part03 Generation Evaluation    | 답변 품질 평가           | Part04, Part06, Part07 |
| Part04 Golden Query             | 평가 데이터셋            | Part02, Part03, Part07 |
| Part05 Query / Chunk / Metadata | 문서 / Query 개선        | Part02, Part06, Part07 |
| Part06 Top-K / Context          | 검색 제어 / Context 구성 | Part02, Part03, Part07 |
| Part07 Quality Report           | 실패 분석 / 개선 이력    | 전체 Part              |

End-to-End 연결 Flow:

```text
Part04 Golden Query
→ Part02 Retrieval Evaluation
→ Part03 Generation Evaluation
→ Part07 Failure Analysis
→ Part05 Query / Chunk / Metadata Optimization
→ Part06 Top-K / Context Optimization
→ Part07 Quality Report
→ Retest
```

---

### [FAQ]

Q. Part 간 연계 기준은 뭐야?

A. 각 Part의 역할과 평가 / 개선 흐름에서의 연결 관계를 정의하는 기준이다.

Q. Part01은 어떤 역할이야?

A. RAG Evaluation 전체 구조와 Core 개념을 담당한다.

Q. Part04는 어디와 연결돼?

A. Retrieval Evaluation, Generation Evaluation, Quality Report와 연결된다.

Q. Part07은 어떤 역할이야?

A. 실패 분석, 개선 조치, Retest 결과, Quality Report를 담당한다.

Q. 문서 세트 전체 Flow는 어떻게 이어져?

A. Golden Query → Evaluation → Failure Analysis → Optimization → Retest → Quality Report 순서로 이어진다.

---

# 9. Common Mistakes

## 9.1 Quality Report / Failure Analysis 실수

### [개념]

Quality Report와 Failure Analysis에서 가장 흔한 실수는 실패 원인을 기록하지 않고 점수만 남기는 것이다.

점수만 있는 Report는 Agent가 무엇을 고쳐야 하는지 판단하기 어렵다.

---

### [핵심]

- Retrieval과 Generation을 섞어서 기록한다.
- Dataset Version을 기록하지 않는다.
- Query Count를 기록하지 않는다.
- Failure Type을 분류하지 않는다.
- Root Cause 없이 증상만 기록한다.
- Fix Action이 모호하다.
- Reindex 여부를 기록하지 않는다.
- Retest 결과를 기록하지 않는다.
- Regression Check를 생략한다.
- Quality Score만 보고 Critical Issue를 무시한다.
- Part 간 연결성을 확인하지 않는다.

---

### [실무]

나쁜 Report 예시:

```md
# RAG Report

검색 품질 괜찮음.
몇 개는 실패함.
나중에 수정 필요.
```

문제:

- Dataset 없음
- Query Count 없음
- 지표 없음
- Failure Type 없음
- Root Cause 없음
- Fix Action 없음
- Retest 기준 없음

개선된 Report 예시:

```md
# RAG Quality Report

- Dataset: RAG_Evaluation_Golden_Query_Set_v1
- Query Count: 30
- Hit@3: 0.86
- Main Failure: Section Miss
- Root Cause: Header Clarity 부족
- Fix Action: Section Header / FAQ 보강
- Reindex: Required
- Retest Query: 문서에 있는데 검색이 안 돼
```

---

### [FAQ]

Q. Quality Report에서 가장 흔한 실수는 뭐야?

A. 점수만 기록하고 Failure Type, Root Cause, Fix Action을 기록하지 않는 것이다.

Q. Retrieval과 Generation을 섞어서 기록하면 왜 문제야?

A. 검색 실패와 생성 실패의 원인과 해결 방법이 다르기 때문이다.

Q. Dataset Version을 빼면 왜 문제야?

A. 평가 기준이 무엇인지 알 수 없어 개선 전후 비교가 어렵다.

Q. Root Cause 없이 Fix Action을 쓰면 왜 위험해?

A. 원인과 맞지 않는 조치를 해서 개선 효과가 없을 수 있다.

Q. Critical Issue를 점수로 덮어도 돼?

A. 안 된다. Critical Issue는 점수와 별도로 우선 처리해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. RAG Quality Report는 뭐야?
A. RAG 평가 결과, 실패 원인, 개선 조치, 재평가 결과를 기록하는 품질 관리 문서다.

Q. RAG Quality Report는 왜 필요해?
A. RAG 품질을 감이 아니라 평가 결과와 개선 이력으로 관리하기 위해 필요하다.

Q. Quality Report에는 무엇을 기록해?
A. Evaluation Date, Dataset Version, Metrics, Failure Cases, Fix Action, Reindex, Retest Result를 기록한다.

Q. Quality Report는 사람용 문서야?
A. 주 목적은 Agent가 RAG 품질 상태와 개선 우선순위를 검색하기 위한 것이다.

Q. Dataset Version을 왜 기록해?
A. Dataset이 바뀌면 평가 결과도 달라져 개선 전후 비교 기준이 흔들리기 때문이다.

Q. Query Count는 왜 필요해?
A. 평가 규모와 지표 신뢰도를 판단하기 위해 필요하다.

Q. Retrieval Metrics Report는 뭐야?
A. 검색 품질을 Hit@K, Precision, Recall, MRR 기준으로 기록하는 리포트 영역이다.

Q. Hit@1이 낮으면 무슨 뜻이야?
A. 기대 문서가 검색되더라도 1순위에 잘 배치되지 않는다는 뜻이다.

Q. Hit@5가 낮으면 무슨 뜻이야?
A. 기대 문서가 검색 후보 안에 들어오지 않는 경우가 많다는 뜻이다.

Q. Precision이 낮으면 무엇을 고쳐야 해?
A. Top-K 감소, Threshold 상향, Metadata Filter, Chunk 분리를 검토한다.

Q. Recall이 낮으면 무엇을 고쳐야 해?
A. Top-K 증가, Query Expansion, Header / FAQ 보강, Filter 완화를 검토한다.

Q. Retrieval Failure Case Report는 뭐야?
A. 검색 실패 Query와 실패 원인, 개선 조치, 재평가 결과를 기록하는 영역이다.

Q. Retrieval Failure는 어떻게 분류해?
A. Document Miss, Section Miss, Chunk Miss, Low Precision, Low Recall, Low Ranking, Filter Error, Stale Index로 분류한다.

Q. Document Miss는 뭐야?
A. Expected Document가 Top-K 검색 결과에 없는 Retrieval Failure다.

Q. Section Miss는 뭐야?
A. Expected Document는 검색되었지만 Expected Section이 검색되지 않은 실패다.

Q. Chunk Miss는 뭐야?
A. Query 답변에 필요한 Expected Chunk가 검색되지 않은 실패다.

Q. Filter Error는 뭐야?
A. Metadata Filter가 필요한 문서를 검색 결과에서 제외하는 실패다.

Q. Stale Index는 뭐야?
A. 문서 수정 내용이 Vector Index에 반영되지 않은 상태다.

Q. Generation Metrics Report는 뭐야?
A. 생성 답변의 Groundedness, Faithfulness, Relevance, Completeness, Hallucination 결과를 기록하는 영역이다.

Q. Groundedness Pass Rate는 뭐야?
A. 답변 Claim이 Retrieved Context에 근거한 비율이다.

Q. Faithfulness Pass Rate는 뭐야?
A. 답변이 Context를 왜곡하지 않고 충실하게 반영한 비율이다.

Q. Hallucination Rate가 높으면 무엇을 고쳐야 해?
A. Claim Verification, Grounding Rule, Missing Information Handling을 강화해야 한다.

Q. Generation Failure Case Report는 뭐야?
A. 생성 답변 실패 Claim과 원인, 개선 조치, 재평가 결과를 기록하는 영역이다.

Q. Failed Claim은 왜 기록해?
A. 어떤 답변 주장이 문서 근거와 맞지 않았는지 추적하기 위해 필요하다.

Q. Evidence Match는 왜 필요해?
A. 답변 Claim과 Retrieved Context가 실제로 일치하는지 확인하기 위해 필요하다.

Q. Generation Failure는 어떻게 분류해?
A. Grounding Failure, Faithfulness Failure, Relevance Failure, Completeness Failure, Hallucination, Wrong Citation 등으로 분류한다.

Q. Failure Analysis는 뭐야?
A. RAG 실패 원인이 검색, 생성, Context 구성, 문서 구조 중 어디에 있는지 분석하는 과정이다.

Q. RAG 실패는 어디부터 분석해?
A. 먼저 Expected Document가 검색 결과에 있는지 확인한다.

Q. Expected Document가 없으면 무슨 실패야?
A. Retrieval Failure다.

Q. Context는 맞는데 답변이 틀리면 무슨 실패야?
A. Generation Failure 또는 Context Assembly Failure다.

Q. Root Cause Analysis는 뭐야?
A. RAG 실패의 표면 증상보다 근본 원인을 찾는 과정이다.

Q. Hit@K가 낮으면 무조건 Top-K 문제야?
A. 아니다. Header, FAQ, Metadata, Query, Reindex 문제일 수 있다.

Q. 검색 결과가 수정 후에도 그대로면 원인이 뭐야?
A. Reindex 누락 가능성이 높다.

Q. Root Cause는 왜 Fix Action과 연결해야 해?
A. 원인과 무관한 조치를 하면 개선 효과가 낮기 때문이다.

Q. Improvement Action은 뭐야?
A. Failure Analysis 결과에 따라 수행할 구체적인 개선 조치다.

Q. Improvement Action은 무엇과 연결해야 해?
A. Failure Type, Target, Reason, Retest Query와 연결해야 한다.

Q. 문서 수정 Action에는 Reindex가 필요해?
A. 필요하다. 문서 내용이 바뀌면 Vector Index를 다시 반영해야 한다.

Q. Prompt 수정도 Reindex가 필요해?
A. 보통 문서 Index 수정은 아니므로 필요하지 않지만 Retest는 필요하다.

Q. Reindex Tracking은 뭐야?
A. 문서 수정 내용이 Vector Index에 반영되었는지 기록하는 과정이다.

Q. Retest Tracking은 뭐야?
A. 개선 후 같은 Query로 품질이 좋아졌는지 기록하는 과정이다.

Q. FAQ만 수정해도 Reindex가 필요해?
A. 필요하다. FAQ도 검색 대상 문서 내용이기 때문이다.

Q. Retest는 왜 같은 Golden Query로 해야 해?
A. 같은 조건에서 개선 전후를 비교해야 하기 때문이다.

Q. Regression Report는 뭐야?
A. 개선 작업 이후 기존 정상 Query의 품질이 나빠졌는지 기록하는 리포트다.

Q. Regression Check는 왜 필요해?
A. 특정 Query를 개선하면서 다른 Query 검색성이 나빠질 수 있기 때문이다.

Q. Regression Query Set에는 무엇을 넣어?
A. Core Query, 수정 문서 Query, 인접 Part Query, Metadata Filter Query, Failure-based Query를 넣는다.

Q. Regression이 발생하면 어떻게 해?
A. Root Cause를 분석하고 수정 후 Reindex와 Retest를 다시 수행한다.

Q. Quality Score는 뭐야?
A. RAG 문서 세트의 검색 품질과 답변 품질을 종합적으로 판단하기 위한 점수다.

Q. Quality Score만 보면 충분해?
A. 아니다. Failure Type, Critical Issue, Next Action을 함께 봐야 한다.

Q. Critical Issue는 뭐야?
A. RAG 문서 세트의 운영 신뢰도를 크게 떨어뜨리는 치명적 문제다.

Q. Quality Score가 높아도 Critical Issue가 있으면 괜찮아?
A. 아니다. Critical Issue는 점수와 별도로 우선 해결해야 한다.

Q. 어떤 문제가 Critical Issue야?
A. 핵심 문서 반복 누락, Hallucination 반복, Rule 충돌, Reindex 누락, Metadata Exclusion 등이 있다.

Q. Final Review Workflow는 뭐야?
A. RAG 문서 세트 제작 후 규칙 준수, 연결성, 검색성, 치명적 문제를 최종 확인하는 절차다.

Q. 최종 검수는 단일 문서만 보면 돼?
A. 아니다. 문서 세트 전체의 역할 분담과 연결성을 함께 확인해야 한다.

Q. Code Block id 속성은 왜 확인해?
A. 출력 규칙상 코드블록 id 속성을 제거해야 하기 때문이다.

Q. Part 간 연결성은 어떻게 확인해?
A. Core → Retrieval → Generation → Golden Query → Optimization → Report 흐름이 이어지는지 확인한다.

Q. Part 간 연계 기준은 뭐야?
A. 각 Part의 역할과 평가 / 개선 흐름에서의 연결 관계를 정의하는 기준이다.

Q. Part07은 어떤 역할이야?
A. 실패 분석, 개선 조치, Retest 결과, Quality Report를 담당한다.

Q. 문서 세트 전체 Flow는 어떻게 이어져?
A. Golden Query → Evaluation → Failure Analysis → Optimization → Retest → Quality Report 순서로 이어진다.

Q. Quality Report에서 가장 흔한 실수는?
A. 점수만 기록하고 Failure Type, Root Cause, Fix Action을 기록하지 않는 것이다.

Q. Retrieval과 Generation을 섞어서 기록하면 왜 문제야?
A. 검색 실패와 생성 실패의 원인과 해결 방법이 다르기 때문이다.

Q. Root Cause 없이 Fix Action을 쓰면 왜 위험해?
A. 원인과 맞지 않는 조치를 해서 개선 효과가 없을 수 있다.

Q. RAG Quality Report 작성 후 무엇을 해야 해?
A. Reindex 여부와 Retest 결과를 확인하고 Regression Check와 Next Action을 기록해야 한다.
