# RAG Evaluation & Retrieval Optimization Part05 Query / Chunk / Metadata Optimization

---

# 1. Retrieval Optimization Core

## 1.1 Retrieval Optimization 기본 개념

### [개념]

Retrieval Optimization은 RAG 시스템이 사용자 Query에 맞는 문서, Section, Chunk를 더 정확하게 검색하도록 개선하는 과정이다.

Retrieval Optimization은 Query, Chunk, Metadata, Top-K, Threshold, Reranking을 함께 조정한다.

```text
Failure Query
→ Analyze Retrieval Result
→ Identify Failure Cause
→ Optimize Query
→ Optimize Chunk
→ Optimize Metadata
→ Reindex
→ Retest
```

---

### [핵심]

- Retrieval Optimization은 검색 실패를 줄이는 개선 작업이다.
- Query Optimization은 검색 입력을 개선한다.
- Chunk Optimization은 문서 구조를 개선한다.
- Metadata Optimization은 검색 범위와 Agent Routing을 개선한다.
- 문서 수정 후 Reindex가 필요하다.
- 개선 후 같은 Golden Query로 Retest한다.
- 감으로 조정하지 않고 Evaluation Result 기반으로 개선한다.

---

### [실무]

2026 실무 기준 Retrieval Optimization은 단일 설정 조정이 아니라 평가 기반 반복 루프다.

문제가 발생했을 때 우선순위는 아래와 같다.

| 증상                             | 우선 확인                      | 개선 대상                             |
| -------------------------------- | ------------------------------ | ------------------------------------- |
| 기대 문서가 검색되지 않음        | Query 표현 / Header            | Query Rewrite, FAQ, Retrieval Queries |
| 관련 없는 문서가 많음            | Top-K / Threshold / Chunk 혼합 | Chunk 분리, Metadata Filter           |
| 문서는 검색되지만 Section이 다름 | Header / Section 구조          | Header Clarity, Chunk 재구성          |
| 특정 Agent가 엉뚱한 문서 검색    | Metadata / Domain              | Domain, Level, Tags 정비              |
| 문서 수정 후 결과가 같음         | Index 상태                     | Reindex                               |
| 유사 문서가 중복 검색            | 중복 Chunk                     | Deduplication, Metadata 정비          |

Retrieval Optimization은 실패 Query를 기록하고, 수정 후 같은 Query로 개선 여부를 확인해야 한다.

---

### [FAQ]

Q. Retrieval Optimization은 뭐야?

A. RAG가 사용자 Query에 맞는 문서와 Chunk를 더 정확하게 검색하도록 개선하는 과정이다.

Q. Retrieval Optimization은 어디부터 시작해?

A. 실패 Query와 Retrieved Chunks를 확인하고 실패 원인을 분류하는 것부터 시작한다.

Q. Query만 고치면 Retrieval이 좋아져?

A. 일부 개선될 수 있지만 Chunk, Metadata, Top-K, Reindex도 함께 확인해야 한다.

Q. 문서 수정 후 바로 테스트하면 돼?

A. 아니다. 문서 수정 후 Reindex하고 같은 Golden Query로 Retest해야 한다.

Q. 감으로 Top-K나 Chunk를 조정해도 돼?

A. 안 된다. Evaluation Result와 Failure Case를 기준으로 조정해야 한다.

---

## 1.2 Optimization Target 분류

### [개념]

Optimization Target은 Retrieval 실패를 해결하기 위해 개선해야 하는 대상이다.

RAG 검색 실패는 Query 문제, Chunk 문제, Metadata 문제, Index 문제, Ranking 문제로 분류할 수 있다.

---

### [핵심]

- Query 문제는 사용자 질문과 문서 표현이 맞지 않는 상태다.
- Chunk 문제는 검색 단위가 너무 크거나 작거나 모호한 상태다.
- Metadata 문제는 필터링과 Routing 기준이 부정확한 상태다.
- Index 문제는 수정된 문서가 검색 인덱스에 반영되지 않은 상태다.
- Ranking 문제는 관련 문서가 검색되지만 상위에 배치되지 않는 상태다.
- Target을 잘못 잡으면 개선 효과가 낮다.

---

### [실무]

Optimization Target 분류표:

| 실패 유형         | 증상                         | Optimization Target                   |
| ----------------- | ---------------------------- | ------------------------------------- |
| Document Miss     | 기대 문서가 Top-K에 없음     | Query, Header, FAQ, Retrieval Queries |
| Section Miss      | 문서는 있으나 Section이 다름 | Header, Chunk Structure               |
| Chunk Miss        | 핵심 근거 Chunk 누락         | Chunk Size, Keyword Placement         |
| Low Precision     | 노이즈 문서가 많음           | Metadata, Threshold, Chunk 분리       |
| Low Recall        | 필요한 문서 누락             | Query Expansion, Top-K, FAQ           |
| Low Ranking       | 기대 문서 순위 낮음          | Keyword Placement, Reranking          |
| Filter Error      | 필요한 문서가 제외됨         | Metadata Schema, Filter Rule          |
| Stale Index       | 수정 내용 검색 안 됨         | Reindex                               |
| Duplicate Context | 중복 Chunk 반복 검색         | Deduplication, Chunk Boundary         |

진단 Flow:

```text
Failure Case
→ Check Expected Document
→ Check Expected Section
→ Check Expected Chunk
→ Check Noise Ratio
→ Check Metadata Filter
→ Check Index Status
→ Select Optimization Target
```

---

### [FAQ]

Q. Optimization Target은 뭐야?

A. Retrieval 실패를 해결하기 위해 개선해야 하는 대상이다.

Q. 기대 문서가 검색되지 않으면 무엇을 고쳐야 해?

A. Query, Header, FAQ, Retrieval Queries를 우선 확인한다.

Q. 관련 없는 문서가 많이 나오면 무엇을 고쳐야 해?

A. Metadata Filter, Similarity Threshold, Chunk 분리, Top-K를 확인한다.

Q. 문서는 검색되는데 Section이 다르면 뭐가 문제야?

A. Header가 모호하거나 Chunk 구조가 잘못되었을 가능성이 높다.

Q. 수정했는데 검색 결과가 그대로면 뭐가 문제야?

A. Reindex가 누락되었을 가능성이 높다.

---

# 2. Query Optimization

## 2.1 Query Optimization 기본 개념

### [개념]

Query Optimization은 사용자 Query를 검색에 더 적합한 형태로 개선하는 과정이다.

짧거나 모호한 Query는 Intent와 Domain Keyword가 부족해 Retrieval 실패를 유발할 수 있다.

```text
Raw User Query
→ Intent Extraction
→ Domain Keyword Injection
→ Query Rewrite
→ Query Expansion
→ Retrieve
```

---

### [핵심]

- Query Optimization은 검색 입력을 개선한다.
- 원래 사용자 의도를 유지해야 한다.
- 짧고 모호한 Query는 Intent를 추출한다.
- Domain Keyword를 추가해 검색 가능성을 높인다.
- 한국어 질문에는 영어 기술 용어 병기가 도움이 된다.
- Query Rewrite는 의미를 다시 쓰는 것이다.
- Query Expansion은 관련 키워드를 추가하는 것이다.
- 과도한 확장은 검색 의도를 흐릴 수 있다.

---

### [실무]

Query Optimization 예시:

| Raw Query             | 문제                          | Optimized Query                                                |
| --------------------- | ----------------------------- | -------------------------------------------------------------- |
| 검색이 이상해         | Intent 모호                   | Retrieval Failure Expected Document Chunk Metadata Reindex     |
| 답변이 이상해         | Retrieval / Generation 불명확 | Generation Failure Groundedness Faithfulness Unsupported Claim |
| 문서에 있는데 안 나와 | 검색 실패 표현                | Expected Document Hit@K Header FAQ Retrieval Queries Reindex   |
| 근거가 없어           | Grounding 표현 부족           | Groundedness Evidence Match Unsupported Claim Citation Match   |
| 너무 많이 나와        | Precision 문제                | Low Precision Top-K Threshold Metadata Filter Deduplication    |

주의:

```text
좋은 Query Rewrite:
"문서에 있는데 검색이 안 돼"
→ "Expected Document가 Top-K에 없는 Retrieval Failure Header FAQ Retrieval Queries Metadata Reindex"

나쁜 Query Rewrite:
"문서에 있는데 검색이 안 돼"
→ "LLM 모델 성능 문제 해결 방법"
```

나쁜 Query Rewrite는 사용자 의도를 바꿔 잘못된 문서를 검색하게 만든다.

---

### [FAQ]

Q. Query Optimization은 뭐야?

A. 사용자 Query를 검색에 더 적합한 형태로 개선하는 과정이다.

Q. Query Optimization은 언제 필요해?

A. 질문이 짧거나 모호해서 필요한 문서가 검색되지 않을 때 필요하다.

Q. Query Rewrite는 뭐야?

A. 원래 의도를 유지하면서 검색에 적합하게 Query를 다시 쓰는 것이다.

Q. Query Expansion은 뭐야?

A. 원래 Query에 관련 Domain Keyword나 동의어를 추가하는 것이다.

Q. Query를 많이 확장하면 좋아?

A. 아니다. 과도한 확장은 검색 의도를 흐려 관련 없는 문서를 가져올 수 있다.

---

## 2.2 Intent Extraction

### [개념]

Intent Extraction은 사용자 Query에서 실제 목적을 추출하는 과정이다.

Intent가 명확해야 Query Rewrite, Agent Routing, Retrieval Evaluation, Answer Relevance 평가가 가능하다.

---

### [핵심]

- Intent는 사용자 질문의 목적이다.
- 짧은 Query는 Intent가 숨겨져 있을 수 있다.
- 문제 상황형 Query는 실패 유형으로 변환한다.
- 비교형 Query는 비교 대상과 기준을 추출한다.
- 개선 요청형 Query는 Optimization Target을 추출한다.
- Intent가 틀리면 검색 문서도 틀릴 가능성이 높다.
- 모호한 Query는 여러 Intent 후보를 가질 수 있다.

---

### [실무]

Intent Extraction 예시:

| User Query            | Extracted Intent             | Target Document              |
| --------------------- | ---------------------------- | ---------------------------- |
| RAG 품질은 어떻게 봐? | evaluation_core              | Part01 Core                  |
| 검색이 안 돼          | retrieval_failure_diagnosis  | Part02 Retrieval Evaluation  |
| 답변이 문서랑 안 맞아 | generation_failure_diagnosis | Part03 Generation Evaluation |
| Query를 어떻게 고쳐?  | query_optimization           | Part05 Query Optimization    |
| Chunk를 어떻게 나눠?  | chunk_optimization           | Part05 Chunk Optimization    |
| Metadata는 왜 필요해? | metadata_optimization        | Part05 Metadata Optimization |
| Top-K는 언제 늘려?    | top_k_optimization           | Part06 Top-K Optimization    |

Intent 추출 Flow:

```text
User Query
→ Identify Problem Type
→ Identify Domain
→ Identify Expected Action
→ Map Intent
→ Build Optimized Query
```

---

### [FAQ]

Q. Intent Extraction은 뭐야?

A. 사용자 Query에서 실제 목적을 추출하는 과정이다.

Q. Intent가 왜 중요해?

A. 올바른 문서 검색, Agent Routing, 답변 관련도 평가에 필요하기 때문이다.

Q. 짧은 Query도 Intent를 추출해야 해?

A. 필요하다. 짧은 Query일수록 검색 의도가 모호할 수 있다.

Q. Intent가 틀리면 어떤 문제가 생겨?

A. 잘못된 문서를 검색하고 질문과 맞지 않는 답변을 생성할 수 있다.

Q. 모호한 Query는 어떻게 처리해?

A. Intent 후보를 만들고 Domain Keyword를 제한적으로 추가한다.

---

## 2.3 Domain Keyword Injection

### [개념]

Domain Keyword Injection은 Query에 기술 Domain의 핵심 용어를 추가해 검색 정확도를 높이는 방법이다.

RAG 문서는 기술 용어 기반으로 Chunk가 구성되므로, Query에 Domain Keyword가 포함되면 Retrieval 품질이 좋아질 수 있다.

---

### [핵심]

- Domain Keyword는 검색 연결성을 높인다.
- 한국어 질문에는 영어 기술 용어 병기가 효과적이다.
- Keyword는 Query Intent와 직접 관련 있어야 한다.
- 너무 많은 Keyword는 검색을 분산시킨다.
- 핵심 개념, 지표, 실패 유형, 개선 대상 중심으로 추가한다.
- 문서에서 실제 사용하는 용어와 일치해야 한다.

---

### [실무]

RAG Evaluation Domain Keyword 예시:

| Intent                | Domain Keyword                                               |
| --------------------- | ------------------------------------------------------------ |
| evaluation_core       | RAG Evaluation, Retrieval Evaluation, Generation Evaluation  |
| retrieval_failure     | Expected Document, Expected Chunk, Hit@K, Retrieval Failure  |
| generation_failure    | Groundedness, Faithfulness, Unsupported Claim, Hallucination |
| metric_definition     | Precision, Recall, MRR, NDCG                                 |
| query_optimization    | Query Rewrite, Query Expansion, Intent Extraction            |
| chunk_optimization    | Header Clarity, Single Concept Chunk, Chunk Size             |
| metadata_optimization | Domain, Level, Tags, Filtered Retrieval                      |
| context_optimization  | Context Assembly, Deduplication, Token Budget                |

예시:

```text
Raw Query:
"답변이 근거가 없어"

Keyword Injected Query:
"답변 근거 부족 Groundedness Evidence Match Unsupported Claim Citation Match RAG Generation Evaluation"
```

---

### [FAQ]

Q. Domain Keyword Injection은 뭐야?

A. Query에 기술 Domain의 핵심 용어를 추가해 검색 정확도를 높이는 방법이다.

Q. 한국어 Query에도 영어 키워드를 넣어야 해?

A. 기술 문서에서는 영어 용어 병기가 Retrieval 품질에 도움이 될 수 있다.

Q. Keyword는 많이 넣을수록 좋아?

A. 아니다. Query Intent와 직접 관련 있는 키워드만 넣어야 한다.

Q. 어떤 Keyword를 넣어야 해?

A. 문서에서 실제 사용하는 핵심 개념, 지표, 실패 유형, 개선 대상 용어를 넣는다.

Q. 잘못된 Keyword를 넣으면 어떻게 돼?

A. 검색 의도가 흐려져 관련 없는 문서가 검색될 수 있다.

---

## 2.4 Query Rewrite

### [개념]

Query Rewrite는 사용자 Query의 의도를 유지하면서 검색 시스템이 이해하기 쉬운 표현으로 다시 작성하는 과정이다.

Query Rewrite는 짧고 모호한 Query, 구어체 Query, 문제 상황형 Query에 효과적이다.

---

### [핵심]

- Query Rewrite는 원래 의도를 유지해야 한다.
- 모호한 표현을 명확한 기술 용어로 변환한다.
- 문제 상황을 Failure Type으로 변환한다.
- Query에 Expected Domain을 포함할 수 있다.
- Rewrite 후보를 여러 개 만들고 평가할 수 있다.
- Rewrite 후 검색 결과가 더 나빠질 수 있으므로 검증이 필요하다.

---

### [실무]

Query Rewrite 예시:

| User Query                   | Rewritten Query                                                     |
| ---------------------------- | ------------------------------------------------------------------- |
| 검색이 이상해                | Retrieval Failure Expected Document Expected Chunk Precision Recall |
| 문서에 있는데 안 나와        | Document Miss Header FAQ Retrieval Queries Metadata Reindex         |
| 답변이 지어낸 것 같아        | Hallucination Unsupported Claim Fabricated Detail Groundedness      |
| 근거가 맞는지 봐야 해        | Evidence Match Groundedness Citation Match Claim Verification       |
| 검색 결과는 맞는데 답이 틀려 | Generation Failure Faithfulness Grounding Rule Context Assembly     |
| 질문이 짧으면 어떻게 해?     | Query Rewrite Query Expansion Intent Extraction Domain Keyword      |

Rewrite 검증 기준:

```text
Original Query
→ Rewritten Query
→ Retrieve
→ Compare Expected Document
→ Compare Precision / Recall
→ Accept or Reject Rewrite
```

---

### [FAQ]

Q. Query Rewrite는 뭐야?

A. 사용자 Query의 의도를 유지하면서 검색에 더 적합한 표현으로 다시 쓰는 것이다.

Q. Query Rewrite는 언제 사용해?

A. Query가 짧거나 모호하거나 문제 상황만 표현할 때 사용한다.

Q. Query Rewrite에서 가장 중요한 것은 뭐야?

A. 원래 사용자 의도를 바꾸지 않는 것이다.

Q. Query Rewrite가 실패할 수도 있어?

A. 가능하다. 과도하게 바꾸면 다른 문서를 검색할 수 있다.

Q. Rewrite 결과는 어떻게 검증해?

A. Expected Document 검색 여부와 Precision / Recall 변화를 비교한다.

---

## 2.5 Query Expansion

### [개념]

Query Expansion은 원래 Query에 관련 키워드, 동의어, 영어 기술 용어, 실패 유형, 지표명을 추가해 검색 범위를 넓히는 방법이다.

Query Expansion은 Recall 개선에 도움이 될 수 있지만 Precision을 낮출 수 있다.

---

### [핵심]

- Query Expansion은 검색 범위를 넓힌다.
- 필요한 문서가 누락될 때 유용하다.
- 영어 기술 용어와 한국어 표현을 함께 사용할 수 있다.
- Synonym, Domain Term, Metric, Failure Type을 추가한다.
- 너무 넓게 확장하면 노이즈가 증가한다.
- Expansion 결과는 Hit@K와 Precision으로 검증한다.

---

### [실무]

Query Expansion 예시:

```text
Original Query:
"검색 결과에 필요한 문서가 없어"

Expansion:
"검색 결과 필요한 문서 누락 Expected Document Document Miss Retrieval Failure Hit@K Recall Header FAQ Retrieval Queries Reindex"
```

Expansion 후보 유형:

| 유형        | 예시                                        |
| ----------- | ------------------------------------------- |
| 동의어      | 검색 실패, Retrieval Failure, Document Miss |
| 지표명      | Hit@K, Recall, Precision                    |
| 구조 용어   | Header, FAQ, Retrieval Queries              |
| 운영 용어   | Reindex, Retest, Evaluation Report          |
| Domain 용어 | RAG Evaluation, Retrieval Evaluation        |

Expansion 적용 판단:

| 상태                   | 판단                  |
| ---------------------- | --------------------- |
| Expected Document 누락 | Expansion 검토        |
| Recall 낮음            | Expansion 검토        |
| Precision 낮음         | Expansion 주의        |
| 노이즈 많음            | Expansion 축소        |
| 검색 결과 분산         | Expansion 키워드 정리 |

---

### [FAQ]

Q. Query Expansion은 뭐야?

A. 원래 Query에 관련 키워드나 동의어를 추가해 검색 범위를 넓히는 방법이다.

Q. Query Expansion은 언제 써?

A. 필요한 문서가 검색되지 않거나 Recall이 낮을 때 사용한다.

Q. Query Expansion의 장점은 뭐야?

A. 다양한 표현의 문서를 검색해 필요한 Chunk를 찾을 가능성을 높인다.

Q. Query Expansion의 위험은 뭐야?

A. 관련 없는 문서가 섞여 Precision이 낮아질 수 있다.

Q. Query Rewrite와 Query Expansion 차이는?

A. Rewrite는 Query를 다시 쓰는 것이고 Expansion은 관련 키워드를 추가하는 것이다.

---

# 3. Chunk Optimization

## 3.1 Chunk Optimization 기본 개념

### [개념]

Chunk Optimization은 문서의 Chunk 구조를 개선해 Retrieval 품질을 높이는 작업이다.

RAG 문서는 사람이 읽는 장문보다, 독립 검색 가능한 Chunk 단위로 구성되어야 한다.

```text
Failure Query
→ Check Retrieved Chunks
→ Check Missing Chunk
→ Improve Header
→ Split or Merge Chunk
→ Add FAQ
→ Add Retrieval Queries
→ Reindex
→ Retest
```

---

### [핵심]

- Chunk는 하나의 개념 중심으로 작성한다.
- Chunk는 독립 검색되어도 의미가 유지되어야 한다.
- Header는 Chunk 내용을 명확히 나타내야 한다.
- FAQ는 사용자 Query와 Chunk를 연결한다.
- Retrieval Queries는 검색 표현 변형을 보강한다.
- Code Block은 핵심 예시 중심으로 짧게 유지한다.
- 너무 긴 Chunk는 검색 의도가 흐려질 수 있다.
- 너무 짧은 Chunk는 문맥 부족이 발생할 수 있다.

---

### [실무]

Chunk Optimization 점검 기준:

| 항목    | 좋은 Chunk            | 나쁜 Chunk      |
| ------- | --------------------- | --------------- |
| 개념 수 | 하나의 개념           | 여러 개념 혼합  |
| Header  | 명확한 기술 용어 포함 | 추상적 제목     |
| 길이    | 300~1200 tokens 권장  | 지나치게 김     |
| 독립성  | 단독 검색 가능        | 앞뒤 문맥 의존  |
| FAQ     | 실제 질문 포함        | Q만 있고 A 없음 |
| 키워드  | 핵심 용어 반복        | 용어 불일치     |
| 예시    | 짧고 직접적           | 긴 전체 코드    |

Chunk 개선 예시:

```text
나쁜 Header:
## 문제 해결

좋은 Header:
## Retrieval Failure Diagnosis

나쁜 Chunk:
Retrieval, Generation, Metadata, Prompt, Top-K를 한 번에 설명

좋은 Chunk:
Retrieval Failure 원인과 진단 Flow만 설명
```

---

### [FAQ]

Q. Chunk Optimization은 뭐야?

A. 문서의 Chunk 구조를 개선해 검색 품질을 높이는 작업이다.

Q. 좋은 Chunk는 어떤 Chunk야?

A. 하나의 개념만 담고, 독립 검색되어도 의미가 유지되는 Chunk다.

Q. Chunk가 너무 길면 왜 문제야?

A. 여러 개념이 섞여 Query 의도와의 관련도가 흐려질 수 있다.

Q. Chunk가 너무 짧으면 왜 문제야?

A. 답변에 필요한 문맥이 부족할 수 있다.

Q. Chunk 수정 후 무엇을 해야 해?

A. Reindex하고 같은 Golden Query로 Retest해야 한다.

---

## 3.2 Header Clarity

### [개념]

Header Clarity는 Section 제목이 Chunk의 핵심 개념과 검색 키워드를 명확히 드러내는 정도다.

Header는 Retrieval에서 중요한 신호로 작동하므로 모호한 제목은 검색 실패를 유발할 수 있다.

---

### [핵심]

- Header는 Chunk의 핵심 개념을 포함해야 한다.
- 기술 용어를 명확하게 사용한다.
- 한국어와 영어 핵심 용어를 병기할 수 있다.
- “개요”, “문제”, “기타” 같은 모호한 제목은 피한다.
- Header와 Chunk 내용이 일치해야 한다.
- 유사 Section은 Naming Consistency를 유지한다.
- Expected Section 검색 실패는 Header 문제일 수 있다.

---

### [실무]

Header 개선 예시:

| 나쁜 Header | 좋은 Header                         |
| ----------- | ----------------------------------- |
| 문제 해결   | Retrieval Failure Diagnosis         |
| 평가 방법   | RAG Evaluation Core                 |
| 지표        | Precision and Recall                |
| 답변 검증   | Groundedness and Faithfulness Check |
| 검색 개선   | Query Rewrite and Query Expansion   |
| 문서 관리   | Metadata Optimization               |
| 결과 기록   | RAG Quality Report                  |

Header 작성 규칙:

```text
Domain Term + Concept + Purpose

예:
Retrieval Failure Diagnosis
Generation Evaluation Report
Metadata Filter Optimization
Golden Query Test Dataset
```

---

### [FAQ]

Q. Header Clarity는 뭐야?

A. Section 제목이 Chunk의 핵심 개념과 검색 키워드를 명확히 드러내는 정도다.

Q. Header가 Retrieval에 영향을 줘?

A. 영향을 준다. Header가 명확하면 Query와 Chunk 연결성이 좋아진다.

Q. 나쁜 Header는 어떤 제목이야?

A. “개요”, “문제”, “기타”처럼 검색 의도가 드러나지 않는 제목이다.

Q. Header에는 영어 용어를 넣어도 돼?

A. 기술 문서에서는 영어 핵심 용어를 넣는 것이 Retrieval에 유리하다.

Q. Expected Section이 검색되지 않으면 무엇을 봐야 해?

A. Header가 명확한지, Section 내용과 제목이 일치하는지 확인한다.

---

## 3.3 Single Concept Chunk

### [개념]

Single Concept Chunk는 하나의 Chunk가 하나의 핵심 개념만 설명하도록 구성하는 원칙이다.

여러 개념이 한 Chunk에 섞이면 Query 의도가 분산되고 Precision이 낮아질 수 있다.

---

### [핵심]

- 하나의 Chunk에는 하나의 주제를 담는다.
- Retrieval Evaluation과 Generation Evaluation을 같은 Chunk에 과도하게 섞지 않는다.
- Query Optimization과 Chunk Optimization은 분리한다.
- 지표 정의와 실패 진단은 분리한다.
- 개념, 판단 기준, 예시는 같은 주제 안에서만 포함한다.
- 복합 개념은 Section을 나눠 Chunk Boundary를 명확히 한다.

---

### [실무]

Chunk 분리 예시:

```text
나쁜 Chunk:
RAG Evaluation, Golden Query, Top-K, Hallucination, Metadata를 한 번에 설명

좋은 Chunk:
1. RAG Evaluation Core
2. Golden Query Design
3. Top-K Optimization
4. Hallucination Check
5. Metadata Optimization
```

분리 기준:

| 혼합 상태                   | 분리 방향                                    |
| --------------------------- | -------------------------------------------- |
| 개념 + 지표 + 리포트 혼합   | 개념 / 지표 / 리포트 분리                    |
| Retrieval + Generation 혼합 | Retrieval / Generation 분리                  |
| Query + Chunk 개선 혼합     | Query Optimization / Chunk Optimization 분리 |
| 여러 실패 유형 혼합         | Failure Type별 분리                          |
| 코드 예시 과다              | 핵심 Snippet만 유지                          |

---

### [FAQ]

Q. Single Concept Chunk는 뭐야?

A. 하나의 Chunk가 하나의 핵심 개념만 설명하도록 구성하는 원칙이다.

Q. 여러 개념을 한 Chunk에 넣으면 왜 문제야?

A. Query 의도가 분산되어 관련 없는 검색 결과가 나올 수 있다.

Q. Retrieval과 Generation을 같은 Chunk에 넣으면 안 돼?

A. 핵심 비교는 가능하지만 세부 평가 기준은 분리하는 것이 좋다.

Q. Chunk 분리는 언제 해야 해?

A. 하나의 Chunk가 여러 질문 의도에 동시에 걸려 검색 노이즈를 만들 때 해야 한다.

Q. Chunk를 나누면 항상 좋아?

A. 아니다. 너무 잘게 나누면 문맥이 부족해질 수 있다.

---

## 3.4 Chunk Size and Overlap

### [개념]

Chunk Size는 하나의 검색 단위에 포함되는 토큰 양이다.

Chunk Overlap은 인접 Chunk 사이에 중복으로 포함되는 내용이다.

적절한 Chunk Size와 Overlap은 Retrieval 품질과 Context 품질에 영향을 준다.

---

### [핵심]

- 권장 Chunk Size는 300~1200 tokens 범위다.
- Chunk가 너무 크면 여러 개념이 섞인다.
- Chunk가 너무 작으면 문맥이 부족하다.
- Overlap은 경계 문맥 보존에 도움된다.
- Overlap이 너무 크면 중복 검색이 증가한다.
- Code Block은 가능한 보존되어야 한다.
- 문서 구조가 좋으면 과도한 Overlap이 필요하지 않다.

---

### [실무]

Chunk Size 판단 기준:

| 상태            | 증상                        | 조치            |
| --------------- | --------------------------- | --------------- |
| Chunk 너무 큼   | 관련 없는 Query에 자주 검색 | Section 분리    |
| Chunk 너무 작음 | 답변 근거가 부족            | 인접 설명 병합  |
| Overlap 부족    | 경계 정보 누락              | Overlap 증가    |
| Overlap 과다    | 중복 Chunk 반복 검색        | Overlap 감소    |
| Code Block 분리 | 예시가 깨짐                 | Code Block 보존 |
| FAQ 분산        | Q/A 연결 약함               | FAQ 단위 유지   |

권장 운영:

```text
개념 설명 Chunk:
300~800 tokens

절차 / Flow Chunk:
500~1000 tokens

예제 포함 Chunk:
600~1200 tokens

FAQ Chunk:
질문-답변 단위 유지
```

---

### [FAQ]

Q. Chunk Size는 뭐야?

A. 하나의 검색 단위에 포함되는 토큰 양이다.

Q. 권장 Chunk Size는 어느 정도야?

A. RAG 문서에서는 300~1200 tokens 범위를 권장한다.

Q. Chunk Overlap은 뭐야?

A. 인접 Chunk 사이에 중복으로 포함되는 문맥이다.

Q. Overlap이 너무 크면 왜 문제야?

A. 중복 Chunk가 반복 검색되어 Context Budget을 낭비할 수 있다.

Q. Code Block은 Chunk에서 어떻게 다뤄야 해?

A. 가능하면 핵심 예시가 깨지지 않도록 보존해야 한다.

---

## 3.5 FAQ Optimization

### [개념]

FAQ Optimization은 실제 사용자 질문 표현을 문서 내부에 포함해 Query와 Chunk의 연결성을 높이는 작업이다.

FAQ는 RAG 문서에서 검색 매칭을 강화하는 핵심 구조다.

---

### [핵심]

- FAQ는 반드시 Q와 A를 함께 포함한다.
- Q only는 금지한다.
- A는 짧고 명확하게 작성한다.
- 실제 사용자 질문 표현을 반영한다.
- 개념 질문, 비교 질문, 문제 상황 질문을 포함한다.
- FAQ는 Retrieval Queries와 함께 검색성을 강화한다.
- FAQ 내부에 무분별한 구분선을 넣지 않는다.

---

### [실무]

FAQ 개선 예시:

```md
### [FAQ]

Q. 문서에 있는데 검색이 안 되면 어떻게 해?

A. Header, FAQ, Retrieval Queries, Metadata, Reindex 여부를 확인한다.

Q. Top-K를 늘리면 무조건 좋아?

A. 아니다. Recall은 높아질 수 있지만 Precision은 낮아질 수 있다.
```

FAQ 작성 패턴:

| 질문 유형 | 예시                                    |
| --------- | --------------------------------------- |
| 개념      | Query Rewrite가 뭐야?                   |
| 차이      | Query Rewrite와 Query Expansion 차이는? |
| 문제 상황 | 문서에 있는데 검색이 안 돼              |
| 판단      | Top-K는 언제 늘려?                      |
| 오해 교정 | Top-K는 무조건 크게 하면 좋아?          |
| 실무 절차 | 문서 수정 후 무엇을 해야 해?            |

---

### [FAQ]

Q. FAQ Optimization은 뭐야?

A. 실제 사용자 질문 표현을 문서에 포함해 Query와 Chunk 연결성을 높이는 작업이다.

Q. FAQ가 Retrieval에 왜 중요해?

A. 사용자의 자연어 질문과 문서 내용을 직접 연결하기 때문이다.

Q. FAQ는 Q만 있어도 돼?

A. 안 된다. 반드시 Q와 A를 함께 작성해야 한다.

Q. FAQ 답변은 길게 써야 해?

A. 아니다. 1~4줄 정도로 짧고 명확하게 작성한다.

Q. FAQ에는 어떤 질문을 넣어야 해?

A. 개념, 비교, 문제 상황, 판단, 오해 교정, 실무 절차 질문을 넣는다.

---

## 3.6 Retrieval Queries Optimization

### [개념]

Retrieval Queries Optimization은 문서 마지막의 Retrieval Queries Block을 강화해 검색 표현 변형을 보강하는 작업이다.

Retrieval Queries는 RAG Agent가 실제 사용자 Query와 문서 내용을 매칭하는 데 도움을 준다.

---

### [핵심]

- 모든 문서 마지막에 Retrieval Queries Block을 포함한다.
- 실제 사용자 질문 표현을 넣는다.
- 핵심 개념별 FAQ를 반복 배치한다.
- 한글 질문과 영어 기술 용어를 함께 고려한다.
- 문제 상황형 Query를 반드시 포함한다.
- 짧고 모호한 Query 표현도 포함한다.
- 문서 전체의 주요 개념을 빠짐없이 커버한다.

---

### [실무]

Retrieval Queries 작성 예시:

```md
# Retrieval Queries

### [FAQ]

Q. 문서에 있는데 검색이 안 돼
A. Header, FAQ, Retrieval Queries, Metadata, Reindex 여부를 확인한다.

Q. Expected Document가 안 나와
A. Document Miss로 보고 Query Rewrite와 Chunk Optimization을 검토한다.

Q. 검색 결과에 엉뚱한 문서가 많아
A. Low Precision 문제로 보고 Top-K, Threshold, Metadata Filter를 조정한다.
```

Retrieval Queries 포함 대상:

| 대상      | 예시                                    |
| --------- | --------------------------------------- |
| 개념 질문 | Query Optimization은 뭐야?              |
| 실패 질문 | 검색이 안 돼                            |
| 비교 질문 | Query Rewrite와 Query Expansion 차이는? |
| 판단 질문 | Top-K는 언제 늘려?                      |
| 오해 질문 | FAQ만 넣으면 충분해?                    |
| 절차 질문 | 문서 수정 후 무엇을 해야 해?            |

---

### [FAQ]

Q. Retrieval Queries Optimization은 뭐야?

A. 문서 마지막의 Retrieval Queries Block을 강화해 검색 표현 변형을 보강하는 작업이다.

Q. Retrieval Queries는 왜 필요해?

A. 실제 사용자 Query와 문서 내용을 더 잘 매칭하기 위해 필요하다.

Q. Retrieval Queries에는 어떤 질문을 넣어?

A. 개념, 실패 상황, 비교, 판단, 오해 교정, 절차 질문을 넣는다.

Q. 짧고 모호한 Query도 넣어야 해?

A. 넣는 것이 좋다. 실제 사용자는 짧게 질문하는 경우가 많다.

Q. Retrieval Queries도 수정 후 Reindex가 필요해?

A. 필요하다. 수정 내용이 Vector Index에 반영되어야 한다.

---

# 4. Metadata Optimization

## 4.1 Metadata Optimization 기본 개념

### [개념]

Metadata Optimization은 문서와 Chunk에 Domain, Level, Category, Section, Source, Version, Tags, UpdatedAt 같은 정보를 부여해 검색 범위 제한과 Agent Routing을 개선하는 작업이다.

Metadata는 Filtered Retrieval과 검색 우선순위 판단에 사용된다.

---

### [핵심]

- Metadata는 검색 범위 제한에 유용하다.
- Agent별 Domain Routing에 사용된다.
- Level 기준으로 Foundation / Expert 문서를 구분할 수 있다.
- Version과 UpdatedAt은 최신 문서 우선순위에 도움된다.
- Tags는 유사 문서를 구분하는 데 도움된다.
- Metadata가 틀리면 필요한 문서가 제외될 수 있다.
- Metadata Filter가 너무 강하면 Recall이 낮아질 수 있다.

---

### [실무]

Metadata 기본 필드:

| 필드      | 의미         | 예시                              |
| --------- | ------------ | --------------------------------- |
| domain    | 기술 Domain  | RAG Evaluation                    |
| level     | 문서 Level   | Level 2                           |
| category  | 문서 범주    | AI / Agent AI                     |
| section   | 문서 Section | Query Optimization                |
| source    | 원천 규칙    | Domain Rules                      |
| version   | 문서 버전    | v1.0                              |
| tags      | 검색 태그    | query-rewrite, chunk-optimization |
| updatedAt | 수정일       | 2026-06-30                        |
| agent     | 대상 Agent   | RAG Agent, Review Agent           |

Metadata 예시:

```yaml
domain: RAG Evaluation & Retrieval Optimization
level: Level 2
category: AI / Agent AI
section: Query Optimization
source: 06_RAG_Evaluation_Retrieval_Optimization_Domain_Rules.md
version: v1.0
tags:
  - query-rewrite
  - query-expansion
  - retrieval-optimization
  - chunk-optimization
updatedAt: 2026-06-30
agent:
  - RAG Agent
  - Review Agent
```

---

### [FAQ]

Q. Metadata Optimization은 뭐야?

A. 문서와 Chunk에 검색 필터링과 Agent Routing용 정보를 부여하는 작업이다.

Q. Metadata는 왜 필요해?

A. 검색 범위를 제한하고 Agent가 필요한 Domain 문서를 찾도록 돕기 위해 필요하다.

Q. Metadata가 틀리면 어떤 문제가 생겨?

A. 필요한 문서가 검색에서 제외되거나 잘못된 Agent로 Routing될 수 있다.

Q. Metadata Filter는 강하게 걸수록 좋아?

A. 아니다. 너무 강하면 Recall이 낮아질 수 있다.

Q. Version과 UpdatedAt은 왜 필요해?

A. 최신 문서 우선순위와 변경 이력 관리에 도움된다.

---

## 4.2 Domain / Level / Category

### [개념]

Domain, Level, Category는 문서의 검색 범위와 Agent 참조 대상을 구분하는 핵심 Metadata다.

이 값이 일관되지 않으면 Agent Routing과 Filtered Retrieval이 불안정해진다.

---

### [핵심]

- Domain은 문서의 기술 영역이다.
- Level은 문서의 학습 / 운영 단계다.
- Category는 Backend, Frontend, AI, DevOps 같은 큰 분류다.
- 값 표기는 프로젝트 전체에서 통일한다.
- 같은 Domain에 여러 Part가 있으면 동일한 Domain 값을 사용한다.
- Foundation 문서와 Expert 문서를 Level로 구분한다.
- Agent별 검색 범위 제한에 사용된다.

---

### [실무]

권장 Metadata 값:

| 필드        | 값 예시                                 |
| ----------- | --------------------------------------- |
| domain      | RAG Evaluation & Retrieval Optimization |
| level       | Level 2                                 |
| category    | AI / Agent AI                           |
| documentSet | RAG_Evaluation_Retrieval_Optimization   |
| part        | Part05                                  |
| agentTarget | RAG Agent, Review Agent, AI Agent       |

잘못된 예시:

```yaml
domain: RAG
level: AI
category: Evaluation
```

문제:

- Domain 값이 너무 넓음
- Level 값이 Project Progress 구조와 맞지 않음
- Category가 일관되지 않음

개선 예시:

```yaml
domain: RAG Evaluation & Retrieval Optimization
level: Level 2
category: AI / Agent AI
```

---

### [FAQ]

Q. Domain Metadata는 뭐야?

A. 문서가 속한 기술 영역을 나타내는 값이다.

Q. Level Metadata는 뭐야?

A. 문서가 프로젝트 로드맵의 어느 단계에 속하는지 나타내는 값이다.

Q. Category Metadata는 뭐야?

A. AI, Backend, Frontend, DevOps 같은 큰 문서 분류다.

Q. Domain 값을 대충 적으면 왜 문제야?

A. 검색 필터링과 Agent Routing이 불안정해질 수 있다.

Q. 같은 문서 세트의 Part들은 Domain 값을 통일해야 해?

A. 반드시 통일하는 것이 좋다.

---

## 4.3 Tags and Keyword Metadata

### [개념]

Tags는 문서나 Chunk의 핵심 검색 키워드를 Metadata로 표현한 값이다.

Tags는 유사 문서 구분, Filtered Retrieval, Agent Routing, 검색 보조에 사용된다.

---

### [핵심]

- Tags는 핵심 개념 중심으로 작성한다.
- 너무 많은 Tags는 관리가 어렵다.
- 너무 적은 Tags는 검색 보조 효과가 낮다.
- 문서에서 실제 사용하는 용어와 맞춰야 한다.
- 한국어와 영어 용어를 혼합할 수 있다.
- 실패 유형, 지표, 개선 대상은 Tag로 유용하다.
- 유사 문서 구분이 필요한 경우 세부 Tag를 사용한다.

---

### [실무]

RAG Evaluation Domain Tag 예시:

| 영역         | Tags                                                         |
| ------------ | ------------------------------------------------------------ |
| Core         | rag-evaluation, retrieval-evaluation, generation-evaluation  |
| Retrieval    | expected-document, hit-at-k, precision, recall, mrr          |
| Generation   | groundedness, faithfulness, hallucination, unsupported-claim |
| Golden Query | golden-query, test-dataset, expected-answer                  |
| Query        | query-rewrite, query-expansion, intent-extraction            |
| Chunk        | chunk-optimization, header-clarity, faq-optimization         |
| Metadata     | metadata-filter, tags, version, updated-at                   |
| Report       | quality-report, failure-analysis, retest                     |

Tag 작성 예시:

```yaml
tags:
  - query-rewrite
  - query-expansion
  - intent-extraction
  - retrieval-failure
  - recall-improvement
```

Tag 안 좋은 예시:

```yaml
tags:
  - good
  - important
  - document
  - ai
```

문제:

- 의미가 넓고 검색 의도를 구체화하지 못한다.

---

### [FAQ]

Q. Tags Metadata는 뭐야?

A. 문서나 Chunk의 핵심 검색 키워드를 Metadata로 표현한 값이다.

Q. Tags는 왜 필요해?

A. 유사 문서 구분, 검색 필터링, Agent Routing에 도움을 주기 때문이다.

Q. Tags는 많이 넣을수록 좋아?

A. 아니다. 핵심 개념 중심으로 일관되게 넣어야 한다.

Q. 어떤 Tags가 좋아?

A. 문서에서 실제 사용하는 기술 용어, 지표, 실패 유형, 개선 대상 Tag가 좋다.

Q. 나쁜 Tags는 어떤 거야?

A. good, important, document처럼 의미가 넓고 검색 의도가 불명확한 Tag다.

---

## 4.4 Version and UpdatedAt

### [개념]

Version과 UpdatedAt은 문서의 변경 상태와 최신성을 관리하는 Metadata다.

RAG 시스템은 오래된 문서와 최신 문서가 함께 검색될 수 있으므로, Version과 UpdatedAt은 Source Priority 판단에 중요하다.

---

### [핵심]

- Version은 문서 변경 단위를 나타낸다.
- UpdatedAt은 마지막 수정일을 나타낸다.
- 최신 문서를 우선 검색하거나 답변 근거로 사용할 수 있다.
- Evaluation Report와 연결해 개선 이력을 추적한다.
- 문서 수정 후 Version 또는 UpdatedAt을 갱신한다.
- 오래된 문서가 최신 문서보다 앞서면 답변 충돌이 생길 수 있다.

---

### [실무]

Version / UpdatedAt 예시:

```yaml
version: v1.0
updatedAt: 2026-06-30
changeType: initial
```

변경 이력 예시:

```md
# Change Log

| Version | UpdatedAt  | Change            | Reason                 |
| ------- | ---------- | ----------------- | ---------------------- |
| v1.0    | 2026-06-30 | Initial document  | Domain 문서 제작       |
| v1.1    | 2026-07-03 | FAQ 추가          | Retrieval Failure 개선 |
| v1.2    | 2026-07-10 | Metadata Tag 보강 | Agent Routing 개선     |
```

최신성 충돌 처리:

| 상황                                | 처리                        |
| ----------------------------------- | --------------------------- |
| 같은 주제의 문서가 여러 버전        | 최신 Version 우선           |
| Domain Rules와 Part 문서 충돌       | Domain Rules 우선           |
| Project Progress와 오래된 문서 충돌 | 최신 Project Progress 확인  |
| 날짜 정보 없음                      | Source 신뢰도 낮음으로 표시 |

---

### [FAQ]

Q. Version Metadata는 뭐야?

A. 문서의 변경 단위를 나타내는 값이다.

Q. UpdatedAt은 뭐야?

A. 문서가 마지막으로 수정된 날짜다.

Q. Version과 UpdatedAt은 왜 필요해?

A. 최신 문서 우선순위와 변경 이력을 판단하기 위해 필요하다.

Q. 문서 수정 후 Version을 꼭 바꿔야 해?

A. 권장한다. 최소한 UpdatedAt은 갱신하는 것이 좋다.

Q. 오래된 문서가 검색되면 왜 문제야?

A. 최신 규칙과 충돌해 잘못된 답변을 생성할 수 있다.

---

# 5. Filtered Retrieval

## 5.1 Filtered Retrieval 기본 개념

### [개념]

Filtered Retrieval은 Metadata 조건을 사용해 검색 범위를 제한하는 방식이다.

Agent가 특정 Domain, Level, Category 문서만 검색해야 할 때 유용하다.

---

### [핵심]

- Filtered Retrieval은 검색 범위를 제한한다.
- Domain별 검색 품질을 높일 수 있다.
- Agent Routing에 유용하다.
- Level 1 / Level 2 / Expert 문서를 구분할 수 있다.
- 관련 없는 문서 노이즈를 줄여 Precision을 높일 수 있다.
- 필터가 너무 강하면 필요한 문서가 누락되어 Recall이 낮아진다.
- Metadata 값이 틀리면 검색 실패가 발생한다.

---

### [실무]

Filtered Retrieval 예시:

```json
{
  "query": "Groundedness가 뭐야?",
  "filters": {
    "domain": "RAG Evaluation & Retrieval Optimization",
    "level": "Level 2",
    "category": "AI / Agent AI"
  }
}
```

Filter 적용 판단:

| 상황                  | 적용 여부                |
| --------------------- | ------------------------ |
| 특정 Domain 질문      | 적용 권장                |
| 여러 Domain 복합 질문 | 약한 필터 또는 다중 검색 |
| Agent별 전용 검색     | 적용 권장                |
| Query Intent 불명확   | 강한 필터 주의           |
| Recall 낮음           | 필터 완화 검토           |
| Precision 낮음        | 필터 강화 검토           |

---

### [FAQ]

Q. Filtered Retrieval은 뭐야?

A. Metadata 조건을 사용해 검색 범위를 제한하는 방식이다.

Q. Filtered Retrieval은 언제 유용해?

A. 특정 Domain이나 Agent가 참조할 문서 범위를 제한할 때 유용하다.

Q. Filter를 쓰면 Precision이 좋아져?

A. 관련 없는 문서를 줄일 수 있어 Precision 개선에 도움이 될 수 있다.

Q. Filter를 강하게 걸면 항상 좋아?

A. 아니다. 필요한 문서가 제외되어 Recall이 낮아질 수 있다.

Q. Filtered Retrieval 실패는 왜 발생해?

A. Metadata 값이 틀리거나 필터 조건이 너무 강할 때 발생한다.

---

## 5.2 Metadata Filter Failure

### [개념]

Metadata Filter Failure는 필터 조건 때문에 필요한 문서가 검색 결과에서 제외되는 실패다.

Filter Failure는 문서가 존재하고 Query도 적절하지만 검색 결과에 나타나지 않는 형태로 발생한다.

---

### [핵심]

- Metadata 값이 잘못되면 필요한 문서가 제외된다.
- Domain 값 불일치가 흔한 원인이다.
- Level 값 불일치가 Agent Routing 실패를 유발한다.
- Tags 누락으로 세부 검색이 약해질 수 있다.
- 필터가 너무 강하면 Recall이 낮아진다.
- 복합 질문에 단일 Domain Filter만 적용하면 문서 누락이 발생할 수 있다.
- Filter Failure는 Retrieval Failure로 기록한다.

---

### [실무]

Metadata Filter Failure 진단 예시:

```md
# Metadata Filter Failure Case

## Query

Groundedness와 Faithfulness 차이는?

## Expected Document

RAG_Evaluation_Retrieval_Optimization_Part03_Generation_Evaluation.md

## Filter

domain: RAG
level: AI

## Problem

Expected Document metadata:
domain: RAG Evaluation & Retrieval Optimization
level: Level 2

## Result

- Domain Filter mismatch
- Level Filter mismatch
- Expected Document excluded

## Fix

- Filter 값 정규화
- Metadata Schema 통일
- Retest
```

진단 Checklist:

```md
### [Checklist]

- [ ] Expected Document가 실제로 존재하는가?
- [ ] Metadata domain 값이 필터와 일치하는가?
- [ ] Metadata level 값이 필터와 일치하는가?
- [ ] category 값이 프로젝트 구조와 일치하는가?
- [ ] tags가 누락되지 않았는가?
- [ ] 필터가 너무 강하지 않은가?
- [ ] 복합 질문에 단일 필터만 적용하지 않았는가?
```

---

### [FAQ]

Q. Metadata Filter Failure는 뭐야?

A. 필터 조건 때문에 필요한 문서가 검색 결과에서 제외되는 실패다.

Q. 문서가 있는데 필터 때문에 안 나올 수 있어?

A. 가능하다. Metadata 값과 Filter 조건이 맞지 않으면 제외된다.

Q. Filter Failure의 흔한 원인은 뭐야?

A. Domain, Level, Category 값 불일치와 과도한 필터 조건이다.

Q. Filter Failure는 어떤 실패로 기록해?

A. Retrieval Failure 중 Filter Error로 기록한다.

Q. Filter Failure를 줄이려면 어떻게 해?

A. Metadata Schema와 값 표기를 통일하고 필터 강도를 조정한다.

---

# 6. Optimization Evaluation

## 6.1 Optimization Retest

### [개념]

Optimization Retest는 Query, Chunk, Metadata 개선 후 같은 Golden Query로 검색 결과가 실제로 좋아졌는지 확인하는 과정이다.

개선 작업은 Retest를 통해 검증되어야 한다.

---

### [핵심]

- 개선 전 결과를 Baseline으로 기록한다.
- 같은 Golden Query로 Retest한다.
- Hit@K 변화를 비교한다.
- Precision / Recall 변화를 비교한다.
- Ranking 변화를 비교한다.
- Generation 품질 변화도 확인한다.
- 개선 후 부작용이 없는지 확인한다.
- Retest 결과는 Evaluation Report에 기록한다.

---

### [실무]

Optimization Retest 형식:

```md
# Optimization Retest

## Target Query

문서에 있는데 검색이 안 돼

## Baseline

- Expected Document: Part02_Retrieval_Evaluation
- Retrieved Rank: Not Found
- Failure Type: Document Miss
- Precision@5: 0.20
- Recall@5: 0.00

## Fix

- Header Keyword 보강
- FAQ 추가
- Retrieval Queries 추가
- Metadata domain 수정
- Reindex 완료

## Retest

- Retrieved Rank: 2
- Hit@3: Pass
- Precision@5: 0.60
- Recall@5: 0.80
- Result: Improved

## Side Effect Check

- Related Query regression: None
```

Retest 판단 기준:

| 결과                 | 판단               |
| -------------------- | ------------------ |
| Hit@K 개선           | 검색 성공 개선     |
| Precision 개선       | 노이즈 감소        |
| Recall 개선          | 누락 감소          |
| Ranking 개선         | 상위 배치 개선     |
| 다른 Query 성능 하락 | Regression 발생    |
| 변화 없음            | Target 재진단 필요 |

---

### [FAQ]

Q. Optimization Retest는 뭐야?

A. 개선 후 같은 Golden Query로 검색 결과가 실제로 좋아졌는지 확인하는 과정이다.

Q. 왜 같은 Query로 Retest해야 해?

A. 같은 조건에서 개선 전후를 비교해야 효과를 판단할 수 있기 때문이다.

Q. Retest에서 무엇을 비교해?

A. Hit@K, Precision, Recall, Ranking, Generation 품질을 비교한다.

Q. 개선 후 다른 Query가 나빠질 수 있어?

A. 가능하다. Regression Check가 필요하다.

Q. Retest 결과가 그대로면 어떻게 해?

A. 실패 원인을 다시 분류하고 Query, Chunk, Metadata, Index를 재점검한다.

---

## 6.2 Regression Check

### [개념]

Regression Check는 Retrieval Optimization 이후 기존에 잘 작동하던 Query의 검색 품질이 나빠지지 않았는지 확인하는 과정이다.

문서 구조나 Metadata를 수정하면 일부 Query는 개선되지만 다른 Query는 악화될 수 있다.

---

### [핵심]

- 개선 대상 Query만 확인하면 부족하다.
- 기존 통과 Query도 함께 Retest한다.
- Hit@K 하락 여부를 확인한다.
- Precision / Recall 하락 여부를 확인한다.
- Ranking 변화도 확인한다.
- Metadata Filter 수정 후 Regression이 자주 발생한다.
- Regression 발생 시 수정 범위를 재검토한다.

---

### [실무]

Regression Check 예시:

```md
# Regression Check

## Changed Document

RAG_Evaluation_Retrieval_Optimization_Part05_Query_Chunk_Metadata_Optimization.md

## Changed Area

- Header 수정
- Metadata tags 추가
- Retrieval Queries 보강

## Regression Query Set

| Query                        | Before Hit@3 | After Hit@3 | Status     |
| ---------------------------- | -----------: | ----------: | ---------- |
| Query Rewrite는 뭐야?        |            1 |           1 | Pass       |
| Chunk Optimization은 뭐야?   |            1 |           1 | Pass       |
| Metadata Filter는 왜 필요해? |            1 |           0 | Regression |
| 문서 수정 후 뭐 해야 해?     |            1 |           1 | Pass       |

## Action

- Metadata Filter 관련 Header와 tags 재검토
- Reindex 후 재평가
```

Regression Check 대상:

| 대상                          | 이유                |
| ----------------------------- | ------------------- |
| 같은 문서의 기존 Golden Query | 내부 검색성 유지    |
| 같은 Domain의 인접 Part Query | 문서 간 충돌 확인   |
| Metadata Filter Query         | 필터 부작용 확인    |
| Core 개념 Query               | 핵심 검색성 유지    |
| Failure-based Query           | 과거 실패 재발 방지 |

---

### [FAQ]

Q. Regression Check는 뭐야?

A. 개선 후 기존에 잘 되던 Query의 검색 품질이 나빠지지 않았는지 확인하는 과정이다.

Q. 왜 Regression Check가 필요해?

A. 한 Query를 개선하면서 다른 Query 검색성이 나빠질 수 있기 때문이다.

Q. Regression은 언제 자주 발생해?

A. Header, Metadata, Chunk Boundary를 크게 수정했을 때 자주 발생한다.

Q. Regression이 발생하면 어떻게 해?

A. 수정 범위를 재검토하고 영향받은 Query 기준으로 다시 Retest한다.

Q. Regression Check에는 어떤 Query를 넣어?

A. 기존 통과 Query, 같은 Domain Query, Metadata Filter Query, Failure-based Query를 넣는다.

---

# 7. Common Mistakes

## 7.1 Query / Chunk / Metadata Optimization 실수

### [개념]

Query / Chunk / Metadata Optimization에서 가장 흔한 실수는 검색 실패 원인을 확인하지 않고 키워드만 반복하거나 Top-K만 조정하는 것이다.

Retrieval Optimization은 실패 유형에 맞는 Target을 개선해야 한다.

---

### [핵심]

- 실패 원인을 분류하지 않는다.
- Query를 과도하게 확장한다.
- 사용자 의도를 바꾸는 Query Rewrite를 한다.
- Chunk에 여러 개념을 계속 섞는다.
- Header가 모호한데 FAQ만 추가한다.
- Metadata 값 표기를 통일하지 않는다.
- Filter를 너무 강하게 적용한다.
- 문서 수정 후 Reindex하지 않는다.
- Retest를 다른 Query로 수행한다.
- Regression Check를 생략한다.

---

### [실무]

잘못된 개선 예시:

```text
문제:
Expected Document가 Top-K에 없음

잘못된 조치:
Top-K를 무조건 크게 설정

문제점:
노이즈가 증가하고 Precision이 낮아질 수 있음

올바른 조치:
Query 표현, Header, FAQ, Retrieval Queries, Metadata, Reindex 여부를 먼저 확인
```

실수 방지 Checklist:

```md
### [Checklist]

- [ ] Failure Type을 먼저 분류했는가?
- [ ] Query Rewrite가 원래 의도를 유지하는가?
- [ ] Query Expansion이 과도하지 않은가?
- [ ] Header가 Chunk 핵심 개념을 포함하는가?
- [ ] Chunk가 Single Concept 원칙을 지키는가?
- [ ] FAQ에 실제 사용자 질문이 포함되었는가?
- [ ] Retrieval Queries가 문서 핵심 개념을 커버하는가?
- [ ] Metadata Domain / Level / Category 값이 통일되었는가?
- [ ] Filter가 과도하지 않은가?
- [ ] 문서 수정 후 Reindex했는가?
- [ ] 같은 Golden Query로 Retest했는가?
- [ ] Regression Check를 수행했는가?
```

---

### [FAQ]

Q. Retrieval Optimization에서 가장 흔한 실수는 뭐야?

A. 실패 원인을 분류하지 않고 키워드 반복이나 Top-K 조정만 하는 것이다.

Q. Query Expansion을 많이 하면 왜 문제야?

A. 검색 의도가 분산되어 관련 없는 문서가 많이 검색될 수 있다.

Q. Header가 약한데 FAQ만 추가하면 충분해?

A. 아니다. Header, Chunk 내용, FAQ, Retrieval Queries를 함께 보강해야 한다.

Q. Metadata Filter를 강하게 걸면 왜 위험해?

A. 필요한 문서가 제외되어 Recall이 낮아질 수 있다.

Q. 개선 후 가장 중요한 작업은 뭐야?

A. Reindex 후 같은 Golden Query로 Retest하고 Regression Check를 수행하는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Retrieval Optimization은 뭐야?
A. RAG가 사용자 Query에 맞는 문서와 Chunk를 더 정확하게 검색하도록 개선하는 과정이다.

Q. Retrieval Optimization은 어디부터 시작해?
A. 실패 Query와 Retrieved Chunks를 확인하고 실패 원인을 분류하는 것부터 시작한다.

Q. Optimization Target은 뭐야?
A. Retrieval 실패를 해결하기 위해 개선해야 하는 대상이다.

Q. 기대 문서가 검색되지 않으면 무엇을 고쳐?
A. Query, Header, FAQ, Retrieval Queries, Metadata, Reindex 여부를 우선 확인한다.

Q. 관련 없는 문서가 많이 나오면 무엇을 고쳐?
A. Metadata Filter, Similarity Threshold, Chunk 분리, Top-K를 확인한다.

Q. 문서는 검색되는데 Section이 다르면 뭐가 문제야?
A. Header가 모호하거나 Chunk 구조가 잘못되었을 가능성이 높다.

Q. Query Optimization은 뭐야?
A. 사용자 Query를 검색에 더 적합한 형태로 개선하는 과정이다.

Q. Query Optimization은 언제 필요해?
A. 질문이 짧거나 모호해서 필요한 문서가 검색되지 않을 때 필요하다.

Q. Intent Extraction은 뭐야?
A. 사용자 Query에서 실제 목적을 추출하는 과정이다.

Q. Intent가 왜 중요해?
A. 올바른 문서 검색, Agent Routing, 답변 관련도 평가에 필요하기 때문이다.

Q. Domain Keyword Injection은 뭐야?
A. Query에 기술 Domain의 핵심 용어를 추가해 검색 정확도를 높이는 방법이다.

Q. 한국어 Query에도 영어 키워드를 넣어야 해?
A. 기술 문서에서는 영어 용어 병기가 Retrieval 품질에 도움이 될 수 있다.

Q. Query Rewrite는 뭐야?
A. 사용자 Query의 의도를 유지하면서 검색에 더 적합한 표현으로 다시 쓰는 것이다.

Q. Query Rewrite는 언제 사용해?
A. Query가 짧거나 모호하거나 문제 상황만 표현할 때 사용한다.

Q. Query Rewrite에서 가장 중요한 것은 뭐야?
A. 원래 사용자 의도를 바꾸지 않는 것이다.

Q. Query Expansion은 뭐야?
A. 원래 Query에 관련 키워드나 동의어를 추가해 검색 범위를 넓히는 방법이다.

Q. Query Expansion은 언제 써?
A. 필요한 문서가 검색되지 않거나 Recall이 낮을 때 사용한다.

Q. Query Rewrite와 Query Expansion 차이는?
A. Rewrite는 Query를 다시 쓰는 것이고 Expansion은 관련 키워드를 추가하는 것이다.

Q. Query Expansion의 위험은 뭐야?
A. 관련 없는 문서가 섞여 Precision이 낮아질 수 있다.

Q. Chunk Optimization은 뭐야?
A. 문서의 Chunk 구조를 개선해 검색 품질을 높이는 작업이다.

Q. 좋은 Chunk는 어떤 Chunk야?
A. 하나의 개념만 담고 독립 검색되어도 의미가 유지되는 Chunk다.

Q. Chunk가 너무 길면 왜 문제야?
A. 여러 개념이 섞여 Query 의도와의 관련도가 흐려질 수 있다.

Q. Chunk가 너무 짧으면 왜 문제야?
A. 답변에 필요한 문맥이 부족할 수 있다.

Q. Header Clarity는 뭐야?
A. Section 제목이 Chunk의 핵심 개념과 검색 키워드를 명확히 드러내는 정도다.

Q. Header가 Retrieval에 영향을 줘?
A. 영향을 준다. Header가 명확하면 Query와 Chunk 연결성이 좋아진다.

Q. 나쁜 Header는 어떤 제목이야?
A. 개요, 문제, 기타처럼 검색 의도가 드러나지 않는 제목이다.

Q. Single Concept Chunk는 뭐야?
A. 하나의 Chunk가 하나의 핵심 개념만 설명하도록 구성하는 원칙이다.

Q. 여러 개념을 한 Chunk에 넣으면 왜 문제야?
A. Query 의도가 분산되어 관련 없는 검색 결과가 나올 수 있다.

Q. Chunk Size는 뭐야?
A. 하나의 검색 단위에 포함되는 토큰 양이다.

Q. 권장 Chunk Size는 어느 정도야?
A. RAG 문서에서는 300~1200 tokens 범위를 권장한다.

Q. Chunk Overlap은 뭐야?
A. 인접 Chunk 사이에 중복으로 포함되는 문맥이다.

Q. Overlap이 너무 크면 왜 문제야?
A. 중복 Chunk가 반복 검색되어 Context Budget을 낭비할 수 있다.

Q. FAQ Optimization은 뭐야?
A. 실제 사용자 질문 표현을 문서에 포함해 Query와 Chunk 연결성을 높이는 작업이다.

Q. FAQ가 Retrieval에 왜 중요해?
A. 사용자의 자연어 질문과 문서 내용을 직접 연결하기 때문이다.

Q. FAQ는 Q만 있어도 돼?
A. 안 된다. 반드시 Q와 A를 함께 작성해야 한다.

Q. Retrieval Queries Optimization은 뭐야?
A. 문서 마지막의 Retrieval Queries Block을 강화해 검색 표현 변형을 보강하는 작업이다.

Q. Retrieval Queries는 왜 필요해?
A. 실제 사용자 Query와 문서 내용을 더 잘 매칭하기 위해 필요하다.

Q. Metadata Optimization은 뭐야?
A. 문서와 Chunk에 검색 필터링과 Agent Routing용 정보를 부여하는 작업이다.

Q. Metadata는 왜 필요해?
A. 검색 범위를 제한하고 Agent가 필요한 Domain 문서를 찾도록 돕기 위해 필요하다.

Q. Metadata가 틀리면 어떤 문제가 생겨?
A. 필요한 문서가 검색에서 제외되거나 잘못된 Agent로 Routing될 수 있다.

Q. Domain Metadata는 뭐야?
A. 문서가 속한 기술 영역을 나타내는 값이다.

Q. Level Metadata는 뭐야?
A. 문서가 프로젝트 로드맵의 어느 단계에 속하는지 나타내는 값이다.

Q. Category Metadata는 뭐야?
A. AI, Backend, Frontend, DevOps 같은 큰 문서 분류다.

Q. Tags Metadata는 뭐야?
A. 문서나 Chunk의 핵심 검색 키워드를 Metadata로 표현한 값이다.

Q. Tags는 왜 필요해?
A. 유사 문서 구분, 검색 필터링, Agent Routing에 도움을 주기 때문이다.

Q. Version Metadata는 뭐야?
A. 문서의 변경 단위를 나타내는 값이다.

Q. UpdatedAt은 뭐야?
A. 문서가 마지막으로 수정된 날짜다.

Q. Version과 UpdatedAt은 왜 필요해?
A. 최신 문서 우선순위와 변경 이력을 판단하기 위해 필요하다.

Q. Filtered Retrieval은 뭐야?
A. Metadata 조건을 사용해 검색 범위를 제한하는 방식이다.

Q. Filtered Retrieval은 언제 유용해?
A. 특정 Domain이나 Agent가 참조할 문서 범위를 제한할 때 유용하다.

Q. Filter를 강하게 걸면 항상 좋아?
A. 아니다. 필요한 문서가 제외되어 Recall이 낮아질 수 있다.

Q. Metadata Filter Failure는 뭐야?
A. 필터 조건 때문에 필요한 문서가 검색 결과에서 제외되는 실패다.

Q. Filter Failure의 흔한 원인은 뭐야?
A. Domain, Level, Category 값 불일치와 과도한 필터 조건이다.

Q. Optimization Retest는 뭐야?
A. 개선 후 같은 Golden Query로 검색 결과가 실제로 좋아졌는지 확인하는 과정이다.

Q. 왜 같은 Query로 Retest해야 해?
A. 같은 조건에서 개선 전후를 비교해야 효과를 판단할 수 있기 때문이다.

Q. Retest에서 무엇을 비교해?
A. Hit@K, Precision, Recall, Ranking, Generation 품질을 비교한다.

Q. Regression Check는 뭐야?
A. 개선 후 기존에 잘 되던 Query의 검색 품질이 나빠지지 않았는지 확인하는 과정이다.

Q. Regression은 언제 자주 발생해?
A. Header, Metadata, Chunk Boundary를 크게 수정했을 때 자주 발생한다.

Q. Retrieval Optimization에서 가장 흔한 실수는?
A. 실패 원인을 분류하지 않고 키워드 반복이나 Top-K 조정만 하는 것이다.

Q. 개선 후 가장 중요한 작업은?
A. Reindex 후 같은 Golden Query로 Retest하고 Regression Check를 수행하는 것이다.
