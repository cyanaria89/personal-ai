# Vector_Database_RAG_Part06_Evaluation_Troubleshooting.md

# Vector Database & RAG Part06 Evaluation and Troubleshooting

---

# 1. RAG Evaluation Core

## 1.1 RAG Evaluation Definition

### [개념]

RAG Evaluation은 RAG 시스템의 검색 품질과 답변 품질을 분리해서 평가하는 과정이다.

RAG 시스템은 두 단계로 동작한다.

```text
Retrieval
→ Generation
```

따라서 평가는 반드시 Retrieval Evaluation과 Generation Evaluation으로 나눠야 한다.

Retrieval Evaluation은 기대 문서와 기대 Chunk가 검색되는지 확인한다.

Generation Evaluation은 생성된 답변이 Retrieved Context와 일치하는지 확인한다.

RAG 답변만 보고 시스템 품질을 판단하면 문제 원인을 잘못 볼 수 있다.

---

### [핵심]

- RAG Evaluation은 Retrieval과 Generation을 분리 평가
- Retrieval Evaluation은 기대 Chunk 검색 여부 확인
- Generation Evaluation은 답변의 문서 근거 일치 여부 확인
- 답변만 보고 Retrieval 품질을 판단하지 않음
- 검색 결과가 좋아도 Prompt가 나쁘면 답변 실패 가능
- 검색 결과가 나쁘면 Generation 단계에서 좋은 답변이 어려움
- 실패 사례는 문서 개선과 검색 설정 개선에 반영

---

### [실무]

2026 실무 기준 RAG Evaluation은 문서 제작, Vector Store 적재, Reindex, 검색 설정 변경, Prompt 변경 이후 반복 수행한다.

개인 AI Agent용 RAG에서는 다음 평가 흐름을 사용한다.

```text
Golden Query
→ Retrieve Documents
→ Check Expected Chunk
→ Build Context
→ Generate Answer
→ Check Groundedness
→ Record Failure
→ Improve Document / Retrieval / Prompt
```

RAG Evaluation은 다음 질문에 답해야 한다.

- 기대 문서가 Top-K에 들어오는가
- 기대 Chunk가 질문에 직접 답할 수 있는가
- 검색 결과에 무관한 Chunk가 섞이는가
- 답변이 Retrieved Context와 일치하는가
- 문서에 없는 내용을 생성했는가
- 부족한 정보가 명확히 표시되었는가
- Source Metadata가 유지되는가

---

### [FAQ]

Q. RAG Evaluation이 뭐야?

A.
RAG 시스템의 검색 품질과 답변 품질을 분리해서 평가하는 과정이다.

Q. RAG 평가는 왜 Retrieval과 Generation을 나눠야 해?

A.
검색 실패와 답변 생성 실패는 원인과 해결 방법이 다르기 때문이다.

Q. 답변만 보고 RAG 품질을 판단하면 안 돼?

A.
안 된다. 답변이 틀렸을 때 검색 실패인지 Prompt 실패인지 구분할 수 없기 때문이다.

Q. RAG Evaluation은 언제 해야 해?

A.
문서 제작 후, Vector Store 적재 후, Reindex 후, 검색 설정 변경 후, Prompt 변경 후 해야 한다.

Q. RAG Evaluation의 핵심은 뭐야?

A.
기대 Chunk가 검색되는지와 답변이 Retrieved Context에 Grounded되어 있는지 확인하는 것이다.

---

# 2. Retrieval Evaluation

## 2.1 Retrieval Evaluation Definition

### [개념]

Retrieval Evaluation은 사용자 Query에 대해 기대 문서와 기대 Chunk가 검색되는지 평가하는 과정이다.

Retrieval Evaluation은 답변 생성 이전에 수행한다.

RAG에서는 관련 Chunk가 검색되지 않으면 LLM이 해당 문서를 근거로 답변할 수 없다.

따라서 Retrieval Evaluation은 RAG Evaluation의 첫 번째 단계다.

---

### [핵심]

- Retrieval Evaluation은 검색 품질 평가
- Expected Document 포함 여부 확인
- Expected Section 포함 여부 확인
- Expected Chunk 포함 여부 확인
- Top-K Hit 확인
- Rank 확인
- Context Quality 확인
- Metadata Filter 적절성 확인
- 실패 원인을 문서 구조와 검색 설정으로 분리

---

### [실무]

Retrieval Evaluation 기록 형식은 다음과 같다.

| 항목              | 설명                                    |
| ----------------- | --------------------------------------- |
| Query             | 평가 질문                               |
| Expected Document | 기대 파일                               |
| Expected Section  | 기대 섹션                               |
| Expected Chunk    | 기대 Chunk                              |
| Top-K             | 검색 결과 개수                          |
| Hit               | 기대 Chunk 포함 여부                    |
| Rank              | 기대 Chunk 순위                         |
| Context Quality   | Good / Weak / Bad                       |
| Failure Cause     | Header, FAQ, Metadata, Top-K, Threshold |
| Action            | 문서 보강, Reindex, 설정 조정           |

예시는 다음과 같다.

```text
Query:
Chunking은 왜 중요해?

Expected Document:
Vector_Database_RAG_Part03_Chunking_Metadata.md

Expected Section:
Chunking Core

Pass Criteria:
Expected Chunk appears in Top-K and explains Chunking, Retrieval minimum unit, Chunk quality impact.
```

Retrieval Evaluation은 LLM 답변을 보기 전에 검색 결과만 먼저 확인한다.

---

### [FAQ]

Q. Retrieval Evaluation이 뭐야?

A.
사용자 Query에 대해 기대 문서와 기대 Chunk가 검색되는지 평가하는 과정이다.

Q. Retrieval Evaluation은 언제 해?

A.
답변 생성 이전에 수행한다.

Q. Top-K Hit가 뭐야?

A.
기대 Chunk가 Top-K 검색 결과 안에 포함되었는지 여부다.

Q. Rank는 왜 기록해?

A.
기대 Chunk가 검색 결과에서 몇 번째로 나오는지 확인해 검색 품질을 판단하기 위해서다.

Q. Retrieval Evaluation 실패 시 무엇을 고쳐야 해?

A.
Header, FAQ, Retrieval Queries, Metadata, Chunk 구조, Top-K, Threshold, Reindex 상태를 확인해야 한다.

---

## 2.2 Golden Query

### [개념]

Golden Query는 RAG 검색 품질을 검증하기 위해 미리 정한 기준 질문이다.

Golden Query는 실제 사용자가 물어볼 가능성이 높은 표현으로 작성한다.

각 Golden Query에는 Expected Document, Expected Section, Expected Chunk, Pass Criteria가 연결되어야 한다.

Golden Query는 문서가 실제로 검색 가능한지 확인하는 기준이다.

---

### [핵심]

- Golden Query는 검색 품질 검증 질문
- 실제 사용자 질문 표현 기반
- Expected Document 필요
- Expected Section 필요
- Expected Chunk 지정 권장
- Pass Criteria 필요
- 문서 제작 후 반복 검증에 사용
- 실패 사례는 문서 개선에 반영

---

### [실무]

Golden Query 작성 예시는 다음과 같다.

```text
Golden Query:
문서에 있는데 왜 검색이 안 돼?

Expected Document:
Vector_Database_RAG_Part04_Retrieval_Search.md

Expected Section:
Retrieval Failure

Expected Chunk:
Expected Chunk Missing

Pass Criteria:
Chunk explains Header, FAQ, Retrieval Queries, Metadata Filter, Top-K, Threshold, Reindex causes.
```

Golden Query Set은 문서별로 최소 다음 유형을 포함한다.

- 개념 질문
- 실무 판단 질문
- 오류 원인 질문
- 설정 기준 질문
- Agent 작업 질문
- 문서 검수 질문

Golden Query는 문서 마지막 Retrieval Queries와 연결되어야 한다.

---

### [FAQ]

Q. Golden Query가 뭐야?

A.
RAG 검색 품질을 검증하기 위해 미리 정한 기준 질문이다.

Q. Golden Query는 어떻게 만들어?

A.
실제 사용자가 물어볼 가능성이 높은 표현으로 만들고 기대 문서와 기대 Chunk를 연결한다.

Q. Golden Query에는 무엇이 필요해?

A.
Query, Expected Document, Expected Section, Expected Chunk, Pass Criteria가 필요하다.

Q. Golden Query는 Retrieval Queries와 관련 있어?

A.
관련 있다. Retrieval Queries는 Golden Query 후보와 사용자 질문 표현을 문서에 포함하는 역할을 한다.

Q. Golden Query 실패는 어떻게 활용해?

A.
문서 Header, FAQ, Retrieval Queries, Metadata, Chunk 구조 개선에 반영한다.

---

# 3. Generation Evaluation

## 3.1 Generation Evaluation Definition

### [개념]

Generation Evaluation은 LLM이 생성한 답변이 Retrieved Context와 일치하는지 평가하는 과정이다.

검색 결과가 좋아도 답변이 문서와 다르면 RAG 시스템은 실패한 것이다.

Generation Evaluation은 Answer Correctness, Groundedness, Faithfulness, Relevance, Completeness를 기준으로 수행한다.

Generation Evaluation은 Review Agent가 수행하기 적합하다.

---

### [핵심]

- Generation Evaluation은 답변 품질 평가
- Retrieved Context와 답변 일치 여부 확인
- 문서에 없는 내용 생성 여부 확인
- Groundedness 확인
- Faithfulness 확인
- Relevance 확인
- Completeness 확인
- Missing Information Rule 적용 여부 확인
- Citation / Source Reference 확인

---

### [실무]

Generation Evaluation 기록 형식은 다음과 같다.

| 항목                  | 설명                                          |
| --------------------- | --------------------------------------------- |
| User Question         | 사용자 질문                                   |
| Retrieved Context     | 검색된 Context 요약                           |
| Answer                | 생성된 답변                                   |
| Correctness           | 정답성                                        |
| Groundedness          | 문서 근거 일치성                              |
| Faithfulness          | 문서 왜곡 여부                                |
| Relevance             | 질문 관련성                                   |
| Completeness          | 답변 완성도                                   |
| Missing Info Handling | 부족 정보 처리                                |
| Source Reference      | 출처 표시                                     |
| Failure Cause         | Prompt, Context, Conflict, Missing Rule       |
| Action                | Prompt 수정, Context Assembly 개선, 문서 보강 |

Generation Evaluation에서 가장 먼저 확인할 것은 답변이 Retrieved Context에 없는 프로젝트 특화 사실을 만들었는지 여부다.

---

### [FAQ]

Q. Generation Evaluation이 뭐야?

A.
LLM이 생성한 답변이 Retrieved Context와 일치하는지 평가하는 과정이다.

Q. 검색 결과가 좋으면 답변도 항상 좋아?

A.
아니다. Prompt, Context Assembly, Grounding Rule이 약하면 답변이 틀릴 수 있다.

Q. Generation Evaluation의 핵심 지표는 뭐야?

A.
Correctness, Groundedness, Faithfulness, Relevance, Completeness다.

Q. Review Agent가 Generation Evaluation을 해도 돼?

A.
적합하다. Review Agent는 답변이 문서 근거와 일치하는지 검증해야 한다.

Q. Generation 실패 시 무엇을 고쳐야 해?

A.
Prompt, Context Assembly, Grounding Rule, Missing Information Rule, 충돌 문서 처리를 확인해야 한다.

---

# 4. Evaluation Metrics

## 4.1 Retrieval Metrics

### [개념]

Retrieval Metrics는 검색 단계의 품질을 측정하는 기준이다.

RAG에서는 단순히 검색 결과가 있는지보다 기대 Chunk가 상위 검색 결과에 포함되는지가 중요하다.

Retrieval Metrics는 문서 구조, Embedding, Top-K, Threshold, Metadata Filter, Reranking 조정에 사용한다.

---

### [핵심]

- Hit Rate는 기대 Chunk 검색 여부
- Recall@K는 Top-K 안에 기대 Chunk가 포함되는 비율
- Precision@K는 Top-K 결과 중 관련 Chunk 비율
- MRR은 기대 Chunk가 얼마나 상위에 있는지 측정
- nDCG는 Ranking 품질 평가에 사용 가능
- Context Relevance는 검색 Context의 질문 관련성
- Duplicate Rate는 중복 Chunk 비율
- Stale Context Rate는 오래된 문서 검색 비율

---

### [실무]

Retrieval Metrics 기준은 다음과 같다.

| Metric             | 의미                                  | 사용 목적                |
| ------------------ | ------------------------------------- | ------------------------ |
| Hit Rate           | 기대 Chunk 검색 여부                  | 기본 검색 성공 판단      |
| Recall@K           | 기대 Chunk가 Top-K 안에 포함되는 비율 | 누락 방지                |
| Precision@K        | Top-K 중 관련 Chunk 비율              | 노이즈 확인              |
| MRR                | 기대 Chunk의 평균 역순위              | 상위 노출 평가           |
| Context Relevance  | 검색 Context 관련도                   | 답변 근거 품질 확인      |
| Duplicate Rate     | 중복 Chunk 비율                       | Context Budget 낭비 확인 |
| Stale Context Rate | 오래된 문서 비율                      | 최신성 문제 확인         |

개인 AI RAG 초기 단계에서는 복잡한 자동 지표보다 Golden Query 기반 수동 평가가 더 실용적이다.

---

### [FAQ]

Q. Retrieval Metrics가 뭐야?

A.
검색 단계의 품질을 측정하는 기준이다.

Q. Hit Rate가 뭐야?

A.
기대 Chunk가 검색 결과에 포함되었는지 측정하는 지표다.

Q. Recall@K가 뭐야?

A.
기대 Chunk가 Top-K 검색 결과 안에 포함되는 비율이다.

Q. Precision@K가 뭐야?

A.
Top-K 검색 결과 중 실제 관련 있는 Chunk의 비율이다.

Q. 개인 AI RAG에서도 복잡한 지표가 필요해?

A.
초기에는 Golden Query 기반 수동 평가가 더 실용적이고, 이후 자동 지표를 추가할 수 있다.

---

## 4.2 Generation Metrics

### [개념]

Generation Metrics는 생성된 답변의 품질을 평가하는 기준이다.

RAG 답변은 일반 자연어 품질보다 문서 근거 일치성이 중요하다.

Generation Metrics는 답변이 정확한지, Retrieved Context에 기반하는지, 질문에 맞는지, 필요한 정보를 충분히 포함하는지 평가한다.

---

### [핵심]

- Answer Correctness는 답변의 정답성
- Groundedness는 문서 근거 기반 여부
- Faithfulness는 문서 내용 왜곡 여부
- Relevance는 질문 관련성
- Completeness는 답변 완성도
- Citation Accuracy는 출처 일치성
- Missing Info Handling은 부족 정보 처리 여부
- Hallucination Rate는 근거 없는 생성 비율

---

### [실무]

Generation Metrics 기준은 다음과 같다.

| Metric                | 의미                     | 실패 예시                      |
| --------------------- | ------------------------ | ------------------------------ |
| Correctness           | 답변이 맞는가            | 잘못된 설정값 제시             |
| Groundedness          | 문서 근거가 있는가       | 문서에 없는 프로젝트 사실 생성 |
| Faithfulness          | 문서를 왜곡하지 않았는가 | 규칙 의미를 반대로 설명        |
| Relevance             | 질문에 답하는가          | 다른 주제 설명                 |
| Completeness          | 필요한 조건을 포함하는가 | 예외 조건 누락                 |
| Citation Accuracy     | 출처가 맞는가            | 다른 문서 Citation             |
| Missing Info Handling | 부족 정보를 표시했는가   | 없는 내용을 추정               |
| Hallucination Rate    | 근거 없는 내용 비율      | 임의 코드 생성                 |

Agent 답변 평가에서는 Groundedness와 Missing Info Handling을 가장 중요하게 본다.

---

### [FAQ]

Q. Generation Metrics가 뭐야?

A.
생성된 답변의 품질을 평가하는 기준이다.

Q. RAG 답변에서 가장 중요한 Generation Metric은 뭐야?

A.
Groundedness와 Faithfulness가 중요하다.

Q. Correctness와 Groundedness는 달라?

A.
다르다. Correctness는 답이 맞는지이고, Groundedness는 문서 근거가 있는지다.

Q. Citation Accuracy는 왜 필요해?

A.
답변에 표시한 출처가 실제 근거와 일치하는지 확인하기 위해 필요하다.

Q. Missing Info Handling은 왜 평가해?

A.
문서에 없는 내용을 임의로 생성하지 않았는지 확인하기 위해 필요하다.

---

# 5. Troubleshooting Core

## 5.1 Troubleshooting Format

### [개념]

RAG Troubleshooting은 RAG 시스템에서 발생하는 검색 실패, 답변 오류, 오래된 문서 검색, Context 과다 문제를 원인별로 분석하고 해결하는 과정이다.

Troubleshooting은 문제, 원인, 해결 형식으로 작성한다.

기본 형식은 다음과 같다.

```text
문제:

원인:

해결:
```

이 형식은 Agent가 오류 상황을 검색하고 바로 조치 방향을 제안하기에 적합하다.

---

### [핵심]

- Troubleshooting은 문제 / 원인 / 해결 형식 사용
- Retrieval 문제와 Generation 문제를 분리
- 문서 구조 문제와 검색 설정 문제를 분리
- 오래된 문서와 중복 문서 문제 확인
- Metadata와 Reindex 상태 확인
- Prompt와 Grounding Rule 확인
- 실패 사례를 문서 개선에 반영
- Review Agent 검증 기준으로 사용 가능

---

### [실무]

RAG Troubleshooting 작성 예시는 다음과 같다.

```text
문제:
문서에 있는 내용이 검색되지 않음

원인:
Header가 불명확함
FAQ가 부족함
Retrieval Queries가 없음
Metadata Filter가 과도함
Embedding 재생성 누락

해결:
Header에 핵심 키워드 추가
FAQ와 Retrieval Queries 보강
Metadata Filter 완화
Reindex 수행
Golden Query 재검증
```

Troubleshooting 문서는 RAG Evaluation 결과와 연결되어야 한다.

평가에서 실패한 Query는 Troubleshooting 항목으로 누적하고, 문서 개선 후 다시 검증한다.

---

### [FAQ]

Q. RAG Troubleshooting이 뭐야?

A.
RAG 검색 실패와 답변 오류를 문제, 원인, 해결 형식으로 분석하는 과정이다.

Q. Troubleshooting 형식은 어떻게 써?

A.
문제, 원인, 해결 순서로 작성한다.

Q. Troubleshooting에서 가장 먼저 나눌 것은 뭐야?

A.
Retrieval 문제인지 Generation 문제인지 먼저 구분해야 한다.

Q. Troubleshooting 결과는 어디에 반영해?

A.
Header, FAQ, Retrieval Queries, Metadata, Prompt, 검색 설정 개선에 반영한다.

Q. Agent용 문서에서 Troubleshooting이 중요한 이유는 뭐야?

A.
Agent가 오류 상황을 검색하고 바로 조치 방향을 찾을 수 있기 때문이다.

---

# 6. Retrieval Troubleshooting

## 6.1 Document Exists But Not Retrieved

### [개념]

Document Exists But Not Retrieved는 문서에 관련 내용이 있지만 Retrieval 결과에 나오지 않는 문제다.

이 문제는 RAG에서 가장 흔한 검색 실패 유형이다.

문서가 Vector Database에 저장되어 있어도 Chunk 구조, Header, FAQ, Metadata, Top-K, Threshold, Reindex 문제가 있으면 검색되지 않을 수 있다.

---

### [핵심]

- 문서에 있어도 검색되지 않을 수 있음
- Header 키워드 부족 가능
- Chunk 의미 단위 불명확 가능
- FAQ 부족 가능
- Retrieval Queries 부족 가능
- Metadata Filter 오류 가능
- Top-K가 낮을 수 있음
- Threshold가 높을 수 있음
- Reindex 누락 가능

---

### [실무]

```text
문제:
관련 내용이 문서에 있지만 Retrieval 결과에 나오지 않음

원인:
Chunk 제목이 불명확함
핵심 키워드 누락
Query와 문서 표현 불일치
FAQ 부족
Retrieval Queries 부족
Metadata 누락 또는 오류
Top-K가 너무 낮음
Threshold가 너무 높음
Embedding 재생성 누락

해결:
Header / FAQ / Retrieval Queries 보강
한글 + 영어 핵심 용어 병기
Chunk를 단일 개념으로 재분리
Metadata Filter 확인
Top-K 증가 테스트
Threshold 완화 테스트
문서 수정 후 Reindex
Golden Query 재검증
```

이 문제를 LLM 성능 문제로 먼저 판단하지 않는다.

검색 결과에 기대 Chunk가 들어왔는지 먼저 확인한다.

---

### [FAQ]

Q. 문서에 있는데 왜 검색이 안 돼?

A.
Header, Chunk 구조, FAQ, Retrieval Queries, Metadata, Top-K, Threshold, Reindex 문제일 수 있다.

Q. 이 문제는 LLM 문제야?

A.
대부분 Retrieval 문제다. 먼저 기대 Chunk가 Top-K에 있는지 확인해야 한다.

Q. Header를 바꾸면 검색이 좋아질 수 있어?

A.
그렇다. Header는 Chunk의 검색 신호로 작동한다.

Q. FAQ를 추가하면 검색에 도움이 돼?

A.
도움이 된다. 실제 사용자 질문 표현을 문서에 포함하기 때문이다.

Q. 수정 후에는 무엇을 해야 해?

A.
Reindex를 수행하고 Golden Query로 다시 검증해야 한다.

---

## 6.2 Irrelevant Documents Retrieved

### [개념]

Irrelevant Documents Retrieved는 사용자 Query와 관련 없는 문서 또는 Chunk가 검색 결과에 포함되는 문제다.

관련 없는 Context가 Prompt에 들어가면 LLM이 잘못된 답변을 생성할 가능성이 높아진다.

이 문제는 Chunk가 너무 크거나, Top-K가 너무 높거나, Threshold가 낮거나, Metadata Filter가 없을 때 발생할 수 있다.

---

### [핵심]

- 무관 Chunk 검색 문제
- Chunk가 너무 클 수 있음
- 여러 주제가 한 Chunk에 섞였을 수 있음
- Top-K가 너무 높을 수 있음
- Threshold가 너무 낮을 수 있음
- Metadata Filter가 부족할 수 있음
- Query가 모호할 수 있음
- Reranking이 필요할 수 있음

---

### [실무]

```text
문제:
Top-K에 무관한 Chunk가 포함됨

원인:
Chunk가 너무 큼
여러 주제가 한 Chunk에 섞임
Top-K가 너무 큼
Threshold가 낮음
Metadata Filter가 없음
Query가 모호함
Reranking 없음

해결:
Chunk를 주제별로 분리
Top-K / Threshold 조정
Metadata Filter 사용
Query Rewrite 적용
Reranking 적용 검토
Context Assembly에서 무관 Context 제거
Golden Query 재검증
```

무관 Chunk가 반복적으로 검색되면 문서 구조와 검색 설정을 함께 점검한다.

---

### [FAQ]

Q. 관련 없는 문서가 검색되는 이유는 뭐야?

A.
Chunk 과대, Top-K 과다, Threshold 과소, Metadata Filter 부족, Query 모호성 때문일 수 있다.

Q. 관련 없는 Chunk가 답변에 영향을 줘?

A.
그렇다. LLM이 무관한 Context를 근거처럼 사용할 수 있다.

Q. 무관 Chunk는 어떻게 줄여?

A.
Chunk를 주제별로 분리하고 Top-K, Threshold, Metadata Filter를 조정한다.

Q. Reranking이 도움이 돼?

A.
도움이 될 수 있다. 1차 검색 결과의 관련도 순서를 개선할 수 있다.

Q. Context Assembly에서도 제거해야 해?

A.
해야 한다. 검색 결과를 그대로 모두 Prompt에 넣으면 답변 품질이 떨어질 수 있다.

---

## 6.3 Low Score But Important Chunk

### [개념]

Low Score But Important Chunk는 Similarity Score는 낮지만 답변에 중요한 Chunk가 존재하는 상황이다.

Score만 기준으로 Chunk를 제거하면 필요한 근거가 빠질 수 있다.

이 문제는 Query 표현과 문서 표현이 다르거나, 정확한 키워드가 중요한 문서에서 자주 발생한다.

---

### [핵심]

- 낮은 Score라도 중요한 Chunk일 수 있음
- Score만으로 Context 제외 금지
- Query 표현과 문서 표현 차이 가능
- Keyword Search 필요 가능
- Hybrid Search 필요 가능
- FAQ와 Retrieval Queries 보강 필요
- Threshold 과도 설정 주의
- Golden Query로 실제 필요 여부 판단

---

### [실무]

```text
문제:
Similarity Score는 낮지만 답변에 필요한 Chunk가 있음

원인:
Query 표현과 문서 표현이 다름
정확한 키워드가 부족함
Embedding Model이 기술 용어를 약하게 처리함
Threshold가 너무 높음
Keyword Search가 없음
Hybrid Search가 없음

해결:
Threshold 완화 테스트
FAQ와 Retrieval Queries 보강
정확한 키워드 추가
한글/영어 용어 병기
Keyword Search 추가
Hybrid Search 적용 검토
Golden Query로 Pass Criteria 재확인
```

기술 문서에서는 클래스명, 메서드명, Endpoint, 에러 메시지가 포함된 Chunk가 낮은 의미 유사도 Score를 받을 수 있다.

이 경우 Keyword Search와 Hybrid Search를 함께 고려한다.

---

### [FAQ]

Q. 낮은 Score Chunk는 무조건 버려도 돼?

A.
아니다. 낮은 Score라도 답변에 중요한 Chunk일 수 있다.

Q. Low Score But Important Chunk는 왜 발생해?

A.
Query와 문서 표현이 다르거나 정확한 키워드 검색이 필요한 경우 발생할 수 있다.

Q. 해결하려면 어떻게 해?

A.
Threshold를 완화하고 FAQ, Retrieval Queries, Keyword Search, Hybrid Search를 보강한다.

Q. 기술 문서에서 특히 중요한 이유는 뭐야?

A.
클래스명, 메서드명, API Endpoint, 에러 메시지는 의미 검색보다 정확한 키워드 검색이 중요할 수 있기 때문이다.

Q. Score 기준은 어떻게 정해야 해?

A.
Golden Query 평가를 기준으로 Threshold와 Top-K를 조정해야 한다.

---

# 7. Generation Troubleshooting

## 7.1 Answer Differs From Documents

### [개념]

Answer Differs From Documents는 검색된 문서와 다른 답변이 생성되는 문제다.

Retrieval 결과가 있어도 LLM이 Retrieved Context를 충분히 따르지 않으면 답변이 문서와 달라질 수 있다.

이 문제는 Grounding Rule 부족, Context 과다, 충돌 문서 포함, Missing Information Rule 부재로 발생한다.

---

### [핵심]

- 검색된 문서와 다른 답변 생성
- Generation Failure 유형
- Grounding Rule 부족 가능
- Missing Information Rule 부재 가능
- Context 과다 가능
- 충돌 문서 포함 가능
- Source Metadata 부족 가능
- Grounding Check 필요

---

### [실무]

```text
문제:
검색된 문서와 다른 답변을 생성함

원인:
Grounding Rule 부족
LLM이 일반 지식으로 보완
Context가 불충분함
Context가 너무 많음
충돌하는 문서가 포함됨
Missing Information Rule 없음
Source Metadata 없음

해결:
RAG Prompt에 문서 근거 우선 규칙 추가
Missing Information Rule 추가
Context Deduplication 수행
Conflict Handling 적용
Source Metadata 포함
답변 검증 단계 추가
Review Agent Grounding Check 수행
```

답변이 자연스럽고 그럴듯해도 Retrieved Context와 다르면 RAG 답변으로는 실패다.

---

### [FAQ]

Q. 검색된 문서와 답변이 다르면 왜 그래?

A.
Grounding Rule 부족, Context Assembly 문제, 충돌 문서, Missing Information Rule 부재 때문일 수 있다.

Q. 답변이 그럴듯하면 괜찮아?

A.
아니다. RAG 답변은 Retrieved Context와 일치해야 한다.

Q. Grounding Rule은 왜 필요해?

A.
LLM이 검색 문서를 우선 근거로 사용하도록 제어하기 위해 필요하다.

Q. Missing Information Rule이 없으면 어떻게 돼?

A.
문서에 없는 내용을 LLM이 임의로 생성할 수 있다.

Q. 해결하려면 무엇을 해야 해?

A.
Prompt를 강화하고 Context를 정리하며 Grounding Check를 수행해야 한다.

---

## 7.2 Hallucinated Project Fact

### [개념]

Hallucinated Project Fact는 LLM이 프로젝트 문서에 없는 구체적 사실을 만들어내는 문제다.

예를 들어 실제 문서에 없는 API Endpoint, 클래스명, 설정값, 배포 환경, Agent 구성, Vector DB 설정을 확정적으로 말하는 경우다.

Agent 시스템에서는 Hallucinated Project Fact가 실제 코드 오류나 운영 오류로 이어질 수 있다.

---

### [핵심]

- 프로젝트 문서에 없는 사실 생성
- API Endpoint 임의 생성 위험
- 클래스명 / 메서드명 임의 생성 위험
- 운영 설정값 임의 생성 위험
- Vector DB Collection 이름 임의 생성 위험
- 배포 환경 임의 생성 위험
- Missing Information Rule 필요
- Source Reference 필요
- Review Agent 검증 필요

---

### [실무]

```text
문제:
문서에 없는 프로젝트 특화 사실을 확정적으로 답변함

원인:
Grounding Rule 부족
Missing Information Rule 없음
LLM 일반 지식 사용
Retrieved Context 부족
Source Reference 없음
Review 단계 없음

해결:
프로젝트 특화 사실 임의 생성 금지 규칙 추가
문서에 없는 내용은 없다고 표시
부족한 문서 목록 출력
Source Metadata 유지
Review Agent로 Grounding Check 수행
필요 시 Project Progress 또는 코드 문서 추가 적재
```

안전한 답변 예시는 다음과 같다.

```text
검색된 문서만으로는 실제 운영 Vector DB 제품을 확정할 수 없음.

부족한 정보:
- 운영 Vector DB 종류
- Collection 이름
- Embedding Model 버전
- 실제 Top-K / Threshold 설정값
```

---

### [FAQ]

Q. Hallucinated Project Fact가 뭐야?

A.
LLM이 프로젝트 문서에 없는 구체적 사실을 만들어내는 문제다.

Q. 어떤 예시가 있어?

A.
문서에 없는 API Endpoint, 클래스명, 설정값, 배포 환경, Vector DB 설정을 확정하는 경우다.

Q. 왜 위험해?

A.
Agent가 실제 프로젝트와 다른 코드나 운영 절차를 만들 수 있기 때문이다.

Q. 어떻게 막아?

A.
Missing Information Rule, Source Reference, Grounding Check를 적용해야 한다.

Q. 문서에 없으면 어떻게 답해야 해?

A.
확정하지 말고 부족한 정보와 필요한 문서를 표시해야 한다.

---

## 7.3 Context Overload

### [개념]

Context Overload는 Prompt에 너무 많은 Retrieved Context가 포함되어 답변 품질이 떨어지는 문제다.

많은 Context가 항상 좋은 것은 아니다.

무관한 Chunk, 중복 Chunk, 오래된 문서, 충돌 문서가 많으면 LLM이 핵심 근거를 놓치거나 서로 다른 기준을 섞을 수 있다.

---

### [핵심]

- Context 과다 문제
- Top-K 과다 가능
- 중복 Context 가능
- 무관 Context 포함 가능
- 오래된 문서 포함 가능
- 충돌 문서 포함 가능
- Context Compression 필요
- Context Deduplication 필요
- Conflict Handling 필요

---

### [실무]

```text
문제:
Context가 너무 길고 답변이 흔들림

원인:
Top-K 과다
Threshold 낮음
중복 Chunk 많음
무관 Context 포함
오래된 문서 포함
충돌 문서 포함
Context Compression 없음
Context Ordering 없음

해결:
Top-K 조정
Threshold 조정
Deduplication 수행
Metadata Filter 적용
최신 Version 우선
Conflict Handling 적용
Context Compression 수행
Context Ordering 적용
Grounding Check 수행
```

Context Window가 큰 모델을 사용해도 Context Assembly 품질이 낮으면 답변 품질은 떨어진다.

---

### [FAQ]

Q. Context Overload가 뭐야?

A.
Prompt에 너무 많은 Context가 들어가 답변 품질이 떨어지는 문제다.

Q. Context를 많이 넣으면 좋은 거 아니야?

A.
아니다. 무관하거나 중복되거나 충돌하는 Context는 답변 품질을 떨어뜨린다.

Q. Context Overload는 어떻게 해결해?

A.
Top-K 조정, Deduplication, Metadata Filter, Compression, Conflict Handling을 적용한다.

Q. Context Window가 크면 해결돼?

A.
항상 그렇지 않다. Context 품질과 구성 순서가 더 중요할 수 있다.

Q. 오래된 문서가 Context에 들어가면 어떻게 돼?

A.
Agent가 이전 기준으로 답변할 수 있다.

---

# 8. Index and Reindex Troubleshooting

## 8.1 Outdated Document Retrieved

### [개념]

Outdated Document Retrieved는 최신 문서가 아니라 오래된 문서가 검색되는 문제다.

문서를 수정했지만 Reindex하지 않았거나, 기존 Vector가 삭제되지 않았거나, version Metadata가 없을 때 발생한다.

이 문제는 Agent가 이전 규칙이나 과거 진행 상황을 기준으로 답변하게 만든다.

---

### [핵심]

- 오래된 문서 검색 문제
- Reindex 누락 가능
- 오래된 Vector 삭제 누락 가능
- 중복 문서 적재 가능
- version Metadata 누락 가능
- updatedAt Metadata 누락 가능
- Project Progress 최신화 필요
- 최신 문서 우선순위 필요

---

### [실무]

```text
문제:
최신 문서가 아닌 이전 문서 기준으로 답변함

원인:
Reindex 누락
오래된 Vector 삭제 안 됨
Version Metadata 없음
updatedAt Metadata 없음
중복 문서 존재
Project Progress 미갱신
Collection 정리 안 됨

해결:
기존 Vector 삭제 후 재색인
version / updatedAt Metadata 추가
중복 문서 제거
최신 문서 우선순위 적용
Project Progress 최신화
Golden Query 재검증
```

Project Progress 문서는 Agent 작업 순서와 완료 상태에 영향을 주므로 업데이트 후 반드시 Reindex 대상이다.

---

### [FAQ]

Q. 오래된 문서가 검색되는 이유는 뭐야?

A.
Reindex 누락, 오래된 Vector 잔존, version Metadata 누락, 중복 문서 때문이다.

Q. 오래된 문서가 검색되면 왜 위험해?

A.
Agent가 과거 규칙이나 이전 진행 상태를 기준으로 답변할 수 있기 때문이다.

Q. 문서를 수정하면 Reindex해야 해?

A.
해야 한다. 문서 내용이 바뀌면 기존 Embedding Vector는 이전 내용을 반영한다.

Q. version Metadata가 왜 필요해?

A.
최신 문서와 오래된 문서를 구분하기 위해 필요하다.

Q. Project Progress도 Reindex해야 해?

A.
해야 한다. 진행 상황 문서는 Agent 판단에 직접 영향을 준다.

---

## 8.2 Embedding Model Changed

### [개념]

Embedding Model Changed는 문서 Embedding에 사용한 모델이 변경된 상황이다.

Embedding Model이 바뀌면 Vector 공간과 Vector Dimension이 달라질 수 있다.

기존 Vector를 그대로 재사용하면 Similarity Search 품질이 깨지거나 검색 오류가 발생할 수 있다.

---

### [핵심]

- Embedding Model 변경 시 기존 Vector 재사용 금지
- Vector Dimension 불일치 가능
- Vector 공간 변경 가능
- Collection 분리 필요 가능
- 전체 Reindex 필요
- Embedding Model 이름과 버전 Metadata 기록 권장
- Query와 Document는 같은 Embedding Model 사용
- Golden Query 재검증 필요

---

### [실무]

```text
문제:
Embedding Model 변경 후 검색 품질이 급격히 나빠짐

원인:
기존 Vector를 재사용함
Query와 Document Embedding Model이 다름
Vector Dimension 불일치
Collection에 서로 다른 Model Vector가 섞임
Embedding Model 버전 기록 없음

해결:
기존 Vector 삭제
Embedding Model 기준 Collection 분리
전체 문서 재Embedding
Embedding Model 이름과 버전 Metadata 기록
Query Embedding 설정 확인
Golden Query 전체 재검증
```

같은 Collection에는 같은 Embedding Model과 같은 Vector Dimension을 사용하는 것이 원칙이다.

---

### [FAQ]

Q. Embedding Model을 바꾸면 기존 Vector를 써도 돼?

A.
권장하지 않는다. 전체 문서를 다시 Embedding하고 Reindex해야 한다.

Q. Vector Dimension이 왜 중요해?

A.
Embedding Model의 출력 차원과 Vector Database Collection 차원이 일치해야 하기 때문이다.

Q. 같은 Collection에 여러 Embedding Model을 섞어도 돼?

A.
권장하지 않는다. Similarity Search 품질이 깨질 수 있다.

Q. Embedding Model 버전을 기록해야 해?

A.
기록하는 것이 좋다. 검색 품질 문제를 추적하기 쉽기 때문이다.

Q. Model 변경 후 무엇을 검증해야 해?

A.
Golden Query Set 전체를 다시 실행해 기대 Chunk 검색 여부를 확인해야 한다.

---

# 9. Metadata Troubleshooting

## 9.1 Missing Metadata

### [개념]

Missing Metadata는 Chunk에 필요한 Metadata가 누락된 상태다.

Metadata가 없으면 Source Tracking, Filtered Search, Agent Routing, Version Control, Review Validation이 어려워진다.

RAG 시스템에서 Metadata 누락은 검색 품질뿐 아니라 답변 검증 품질도 떨어뜨린다.

---

### [핵심]

- Metadata 누락 문제
- Source Tracking 실패
- Filtered Search 실패 가능
- Agent Routing 불안정
- Version Control 어려움
- Citation 불가능
- Review Validation 약화
- Metadata 보강 후 Reindex 필요

---

### [실무]

```text
문제:
검색 결과의 출처와 도메인을 추적할 수 없음

원인:
source 누락
fileName 누락
documentId 누락
chunkId 누락
domain 누락
level 누락
section 누락
version 누락
updatedAt 누락

해결:
Metadata Schema 정의
필수 필드 보강
필드명 통일
기존 Vector Metadata 갱신
필요 시 전체 Reindex
Golden Query 재검증
```

필수 권장 Metadata는 다음과 같다.

```json
{
  "source": "Vector_Database_RAG_Part06_Evaluation_Troubleshooting.md",
  "fileName": "Vector_Database_RAG_Part06_Evaluation_Troubleshooting.md",
  "documentId": "vector-database-rag-part06",
  "chunkId": "vector-database-rag-part06-009",
  "domain": "AI",
  "level": "Foundation",
  "category": "Vector Database & RAG",
  "section": "Metadata Troubleshooting",
  "title": "Missing Metadata",
  "tags": ["rag", "metadata", "troubleshooting", "evaluation"],
  "version": "2026-06",
  "updatedAt": "2026-06-30"
}
```

---

### [FAQ]

Q. Missing Metadata가 뭐야?

A.
Chunk에 필요한 Metadata가 누락된 상태다.

Q. Metadata가 없으면 뭐가 문제야?

A.
출처 추적, 검색 필터링, Agent Routing, 최신성 판단, 답변 검증이 어려워진다.

Q. 필수 Metadata는 뭐야?

A.
source, fileName, documentId, chunkId, domain, level, category, section, title, tags, version, updatedAt을 권장한다.

Q. Metadata를 추가하면 Reindex해야 해?

A.
해야 한다. Vector Store에 저장된 Metadata도 갱신되어야 한다.

Q. Metadata 누락은 답변 품질에도 영향을 줘?

A.
영향을 준다. 올바른 문서 검색과 Source 검증이 어려워진다.

---

## 9.2 Wrong Metadata

### [개념]

Wrong Metadata는 Chunk에 잘못된 Metadata가 붙은 상태다.

Wrong Metadata는 Missing Metadata보다 더 위험할 수 있다.

잘못된 Metadata는 잘못된 문서를 정상 검색 결과처럼 보이게 만들고, Agent가 잘못된 Domain 기준으로 답변하게 할 수 있다.

---

### [핵심]

- 잘못된 Metadata 문제
- Domain 오분류 위험
- Level 오분류 위험
- Category 오분류 위험
- Source 오류 위험
- Version 오류 위험
- Agent Routing 실패 가능
- Filtered Search 오류 가능
- Metadata 검수 후 Reindex 필요

---

### [실무]

```text
문제:
Agent가 역할과 맞지 않는 문서를 검색함

원인:
domain Metadata 오입력
category Metadata 오입력
level Metadata 불일치
tags 과다 또는 부정확
version 오류
source 파일명 오류
Metadata Filter 기준 불일치

해결:
Metadata Schema 재검수
domain / level / category 값 통일
source / fileName 검증
잘못된 Chunk 검색 결과 기록
Metadata 수정
Reindex 수행
Agent별 Golden Query 재검증
```

예시는 다음과 같다.

```text
문제:
Backend Agent가 AI RAG 문서를 Backend 구현 규칙처럼 사용함

원인:
AI 문서에 domain: Backend Metadata가 잘못 부여됨

해결:
domain: AI로 수정
기존 Vector Metadata 갱신
Backend Agent Golden Query 재검증
```

---

### [FAQ]

Q. Wrong Metadata가 뭐야?

A.
Chunk에 잘못된 Metadata가 붙은 상태다.

Q. Wrong Metadata가 위험한 이유는 뭐야?

A.
잘못된 문서가 정상 검색 결과처럼 사용될 수 있기 때문이다.

Q. domain Metadata가 틀리면 어떻게 돼?

A.
Agent가 자기 역할과 맞지 않는 문서를 검색할 수 있다.

Q. source Metadata가 틀리면 어떻게 돼?

A.
Citation과 답변 검증 신뢰도가 떨어진다.

Q. Wrong Metadata는 어떻게 고쳐?

A.
Metadata를 수정하고 기존 Vector를 갱신하거나 Reindex해야 한다.

---

# 10. Prompt Troubleshooting

## 10.1 Weak Grounding Prompt

### [개념]

Weak Grounding Prompt는 RAG Prompt가 LLM에게 Retrieved Context를 우선 사용하도록 충분히 지시하지 못하는 상태다.

Prompt가 약하면 검색된 문서가 있어도 LLM이 일반 지식, 추론, 이전 대화 맥락을 기준으로 답할 수 있다.

RAG 시스템에서는 Prompt에 Grounding Rule, Missing Information Rule, Citation Rule, Output Format Rule을 명확히 포함해야 한다.

---

### [핵심]

- Grounding Prompt 부족 문제
- Retrieved Context 우선 규칙 필요
- 문서에 없는 내용 생성 금지 필요
- 부족 정보 표시 규칙 필요
- 추정과 근거 분리 필요
- Source Reference 유지 필요
- Output Format 명확화 필요
- Agent 역할별 Prompt 필요

---

### [실무]

```text
문제:
검색된 문서가 있는데도 LLM이 일반 지식으로 답변함

원인:
Grounding Rule 부족
Missing Information Rule 없음
Citation Rule 없음
Output Format 불명확
Agent Role 불명확
Context와 User Question 구분 부족

해결:
Retrieved Context 우선 사용 규칙 추가
문서에 없는 내용 생성 금지 규칙 추가
부족한 정보 표시 규칙 추가
추정과 근거 분리 규칙 추가
Source Reference 유지 규칙 추가
Output Format 명확화
Agent 역할별 Prompt 분리
```

권장 Prompt Rule은 다음과 같다.

```text
Rules:
- Use retrieved context first.
- Do not invent project-specific facts.
- If context is insufficient, say what is missing.
- Separate evidence-based answers from assumptions.
- Keep source references when available.
- Follow the required output format.
```

---

### [FAQ]

Q. Weak Grounding Prompt가 뭐야?

A.
LLM이 Retrieved Context를 우선 사용하도록 충분히 지시하지 못하는 Prompt 상태다.

Q. Prompt가 약하면 어떻게 돼?

A.
검색 문서보다 일반 지식이나 추론을 우선해 답변할 수 있다.

Q. RAG Prompt에 꼭 필요한 규칙은 뭐야?

A.
Grounding Rule, Missing Information Rule, Citation Rule, Output Format Rule이다.

Q. Agent별 Prompt가 필요해?

A.
필요하다. Agent 역할에 따라 우선 참조 문서와 검증 기준이 다르기 때문이다.

Q. Prompt 수정 후 무엇을 검증해야 해?

A.
Generation Evaluation과 Grounding Check를 다시 수행해야 한다.

---

# 11. Agent RAG Evaluation

## 11.1 Agent-Specific Evaluation

### [개념]

Agent RAG Evaluation은 Agent 역할별로 RAG 검색과 답변 품질을 평가하는 과정이다.

Multi-Agent System에서는 모든 Agent가 같은 방식으로 문서를 검색하지 않는다.

PM Agent, Backend Agent, Frontend Agent, Review Agent, DevOps Agent, AI Agent는 서로 다른 Domain, Level, Category 문서를 우선 검색해야 한다.

따라서 Agent별 Golden Query와 Agent별 Metadata Filter 평가가 필요하다.

---

### [핵심]

- Agent별 RAG Evaluation 필요
- PM Agent는 요구사항과 Project Progress 중심
- Backend Agent는 Backend Domain 문서 중심
- Frontend Agent는 Frontend Domain 문서 중심
- Review Agent는 Rules, Checklist, Troubleshooting 중심
- DevOps Agent는 DevOps 문서 중심
- AI Agent는 AI / RAG / Agent 문서 중심
- Agent별 Metadata Filter 검증 필요
- Agent별 Grounding Rule 검증 필요

---

### [실무]

Agent별 평가 기준은 다음과 같다.

| Agent          | 평가 기준                                                   |
| -------------- | ----------------------------------------------------------- |
| PM Agent       | 요구사항 분해, Project Progress 반영, 작업 위임 기준        |
| Backend Agent  | Backend 문서 검색, 코드 규칙 준수, API / DB / Security 기준 |
| Frontend Agent | Frontend 문서 검색, Component / State / API 연동 기준       |
| Review Agent   | Master Rules, Domain Rules, Checklist, Troubleshooting 검증 |
| DevOps Agent   | 배포, 운영, Docker, CI/CD, Monitoring 기준                  |
| AI Agent       | RAG, Agent Workflow, Evaluation, Guardrails 기준            |

Agent별 Golden Query 예시는 다음과 같다.

```text
AI Agent Golden Query:
RAG 답변이 문서와 다를 때 어디를 확인해야 해?

Expected Document:
Vector_Database_RAG_Part06_Evaluation_Troubleshooting.md

Expected Section:
Generation Troubleshooting
```

```text
Review Agent Golden Query:
RAG 문서 최종 검수 Checklist는 뭐야?

Expected Document:
Master_RAG_Rules.md
Vector_Database_RAG_Part06_Evaluation_Troubleshooting.md

Expected Section:
Quality Checklist
Evaluation Checklist
```

---

### [FAQ]

Q. Agent RAG Evaluation이 뭐야?

A.
Agent 역할별로 RAG 검색과 답변 품질을 평가하는 과정이다.

Q. 모든 Agent가 같은 문서를 검색하면 안 돼?

A.
안 된다. Agent 역할에 따라 우선 참조해야 할 Domain과 문서가 다르다.

Q. Review Agent는 무엇을 우선 검색해야 해?

A.
Master Rules, Domain Rules, Checklist, Troubleshooting 문서를 우선 검색해야 한다.

Q. AI Agent는 무엇을 우선 검색해야 해?

A.
RAG, Agent Workflow, Evaluation, Guardrails 관련 AI Domain 문서를 우선 검색해야 한다.

Q. Agent별 Golden Query가 필요한 이유는 뭐야?

A.
각 Agent가 자기 역할에 맞는 문서를 검색하고 Grounded Answer를 생성하는지 확인하기 위해서다.

---

# 12. Evaluation Checklist

## 12.1 Final Evaluation Checklist

### [개념]

Evaluation Checklist는 RAG 문서와 RAG 시스템의 검색, 답변, 검증 품질을 최종 확인하는 기준이다.

이 Checklist는 Retrieval Evaluation, Generation Evaluation, Metadata Evaluation, Prompt Evaluation, Agent Evaluation을 통합한다.

문서 제작 완료 후, Vector Store 적재 후, Reindex 후, Agent Workflow 변경 후 반복 사용한다.

---

### [핵심]

- Retrieval Evaluation 확인
- Generation Evaluation 확인
- Golden Query Set 확인
- Metadata 품질 확인
- Reindex 상태 확인
- Prompt Grounding Rule 확인
- Missing Information Rule 확인
- Citation Rule 확인
- Agent별 검색 품질 확인
- 실패 사례 기록 확인

---

### [실무]

최종 Evaluation Checklist는 다음과 같다.

```md
### [Checklist]

- [ ] Golden Query Set이 문서별로 준비되어 있는가?
- [ ] Golden Query가 실제 사용자 질문 표현을 포함하는가?
- [ ] 각 Golden Query에 Expected Document가 지정되어 있는가?
- [ ] 각 Golden Query에 Expected Section 또는 Expected Chunk가 지정되어 있는가?
- [ ] Expected Chunk가 Top-K에 포함되는가?
- [ ] 기대 Chunk의 Rank를 기록했는가?
- [ ] Top-K 결과에 무관 Chunk가 과도하게 포함되지 않는가?
- [ ] Similarity Threshold가 검색 실패를 만들지 않는가?
- [ ] Keyword Search가 필요한 Query 유형을 식별했는가?
- [ ] Hybrid Search가 필요한 Query 유형을 식별했는가?
- [ ] Reranking이 필요한 검색 실패 사례를 기록했는가?
- [ ] 중복 Chunk가 Context Budget을 낭비하지 않는가?
- [ ] Metadata Filter가 필요한 문서를 제외하지 않는가?
- [ ] source / fileName / documentId / chunkId가 있는가?
- [ ] domain / level / category / section이 정확한가?
- [ ] version / updatedAt이 최신성 판단에 충분한가?
- [ ] 문서 수정 후 Reindex를 수행했는가?
- [ ] Embedding Model 변경 후 전체 Reindex를 수행했는가?
- [ ] Prompt에 Grounding Rule이 포함되어 있는가?
- [ ] Prompt에 Missing Information Rule이 포함되어 있는가?
- [ ] Prompt에 Citation / Source Rule이 포함되어 있는가?
- [ ] 답변이 Retrieved Context와 일치하는가?
- [ ] 문서에 없는 프로젝트 특화 사실을 생성하지 않았는가?
- [ ] 부족한 정보가 명확히 표시되었는가?
- [ ] Source Reference가 답변 근거와 일치하는가?
- [ ] Review Agent가 Grounding Check를 수행하는가?
- [ ] Agent별 Golden Query가 준비되어 있는가?
- [ ] Agent별 Metadata Filter가 올바른 문서를 검색하는가?
- [ ] 실패 사례가 문서 개선과 검색 설정 개선에 반영되었는가?
```

이 Checklist는 Vector Database & RAG 문서 Set 전체의 최종 검수 기준으로 사용할 수 있다.

---

### [FAQ]

Q. Evaluation Checklist는 왜 필요해?

A.
RAG 검색, 답변, Metadata, Prompt, Agent 품질을 통합 검수하기 위해 필요하다.

Q. Evaluation Checklist는 언제 사용해?

A.
문서 제작 완료 후, Vector Store 적재 후, Reindex 후, Agent Workflow 변경 후 사용한다.

Q. 가장 중요한 검수 항목은 뭐야?

A.
Expected Chunk가 Top-K에 포함되는지와 답변이 Retrieved Context와 일치하는지 확인하는 것이다.

Q. Agent별 Evaluation도 해야 해?

A.
해야 한다. Agent마다 우선 검색해야 하는 문서와 검증 기준이 다르기 때문이다.

Q. 실패 사례는 어떻게 처리해?

A.
문서 Header, FAQ, Retrieval Queries, Metadata, Prompt, 검색 설정 개선에 반영한다.

---

# 13. Final Operation Rules

## 13.1 RAG Evaluation Operation

### [개념]

RAG Evaluation Operation은 RAG 문서와 Vector Database를 지속적으로 운영하면서 검색 품질을 유지하는 규칙이다.

RAG 시스템은 한 번 문서를 업로드하면 끝나는 구조가 아니다.

문서 수정, 추가, 삭제, Agent 변경, Embedding Model 변경, 검색 설정 변경이 발생할 때마다 평가와 Reindex가 필요하다.

---

### [핵심]

- RAG 문서 운영은 지속 관리 필요
- 문서 변경 시 Reindex 필요
- Agent 변경 시 Agent별 Golden Query 재검증
- Embedding Model 변경 시 전체 Reindex 필요
- Metadata Schema 변경 시 Reindex 필요
- 검색 설정 변경 시 Retrieval Evaluation 필요
- Prompt 변경 시 Generation Evaluation 필요
- 실패 로그를 문서 개선에 반영
- Project Progress 최신화 필요

---

### [실무]

운영 주기 기준은 다음과 같다.

| 상황                         | 필요한 작업                                       |
| ---------------------------- | ------------------------------------------------- |
| 새 Part 문서 추가            | Ingestion, Metadata Attach, Reindex, Golden Query |
| 기존 문서 수정               | Reindex, Retrieval Evaluation                     |
| FAQ / Retrieval Queries 추가 | Reindex, Golden Query 재검증                      |
| Metadata Schema 변경         | Metadata 갱신, Reindex                            |
| Embedding Model 변경         | 전체 Reindex, 전체 Golden Query 재검증            |
| Top-K / Threshold 변경       | Retrieval Evaluation                              |
| Prompt 변경                  | Generation Evaluation                             |
| Agent Role 변경              | Agent별 Golden Query 재검증                       |
| Project Progress 변경        | Project Progress Reindex                          |

운영 목표는 단순 업로드 완료가 아니라 Agent가 안정적으로 검색하고 근거 기반 답변을 생성하는 상태다.

---

### [FAQ]

Q. RAG 문서는 한 번 업로드하면 끝이야?

A.
아니다. 문서 수정, 설정 변경, Agent 변경 시 계속 평가하고 Reindex해야 한다.

Q. FAQ를 추가해도 Reindex해야 해?

A.
해야 한다. FAQ는 Retrieval Matching에 직접 영향을 준다.

Q. Prompt 변경 후에도 평가가 필요해?

A.
필요하다. Generation Evaluation과 Grounding Check를 다시 수행해야 한다.

Q. Agent Role을 바꾸면 무엇을 해야 해?

A.
Agent별 Golden Query와 Metadata Filter를 다시 검증해야 한다.

Q. RAG 운영의 최종 목표는 뭐야?

A.
Agent가 필요한 문서를 안정적으로 검색하고 문서 근거 기반 답변을 생성하는 상태를 유지하는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. RAG Evaluation이 뭐야?
A. RAG 시스템의 검색 품질과 답변 품질을 분리해서 평가하는 과정이다.

Q. RAG 평가는 왜 Retrieval과 Generation을 나눠야 해?
A. 검색 실패와 답변 생성 실패는 원인과 해결 방법이 다르기 때문이다.

Q. Retrieval Evaluation이 뭐야?
A. 사용자 Query에 대해 기대 문서와 기대 Chunk가 검색되는지 평가하는 과정이다.

Q. Generation Evaluation이 뭐야?
A. LLM이 생성한 답변이 Retrieved Context와 일치하는지 평가하는 과정이다.

Q. Golden Query가 뭐야?
A. RAG 검색 품질을 검증하기 위해 미리 정한 기준 질문이다.

Q. Golden Query에는 무엇이 필요해?
A. Query, Expected Document, Expected Section, Expected Chunk, Pass Criteria가 필요하다.

Q. Top-K Hit가 뭐야?
A. 기대 Chunk가 Top-K 검색 결과 안에 포함되었는지 여부다.

Q. Retrieval Metrics에는 뭐가 있어?
A. Hit Rate, Recall@K, Precision@K, MRR, Context Relevance, Duplicate Rate, Stale Context Rate가 있다.

Q. Generation Metrics에는 뭐가 있어?
A. Correctness, Groundedness, Faithfulness, Relevance, Completeness, Citation Accuracy, Missing Info Handling이 있다.

Q. Groundedness가 뭐야?
A. 답변이 Retrieved Context를 근거로 생성되었는지 평가하는 기준이다.

Q. Faithfulness가 뭐야?
A. 답변이 문서 내용을 왜곡하지 않았는지 평가하는 기준이다.

Q. RAG Troubleshooting 형식은 어떻게 써?
A. 문제, 원인, 해결 순서로 작성한다.

Q. 문서에 있는데 왜 검색이 안 돼?
A. Header, Chunk 구조, FAQ, Retrieval Queries, Metadata, Top-K, Threshold, Reindex 문제일 수 있다.

Q. 문서에 있는 내용이 검색되지 않으면 먼저 뭘 봐?
A. 기대 Chunk가 Top-K에 들어오는지 확인해야 한다.

Q. 관련 없는 문서가 검색되는 이유는 뭐야?
A. Chunk 과대, Top-K 과다, Threshold 과소, Metadata Filter 부족, Query 모호성 때문일 수 있다.

Q. 무관 Chunk는 어떻게 줄여?
A. Chunk를 주제별로 분리하고 Top-K, Threshold, Metadata Filter를 조정한다.

Q. 낮은 Score Chunk는 무조건 버려도 돼?
A. 아니다. 낮은 Score라도 답변에 중요한 Chunk일 수 있다.

Q. Low Score But Important Chunk는 어떻게 해결해?
A. Threshold를 완화하고 FAQ, Retrieval Queries, Keyword Search, Hybrid Search를 보강한다.

Q. 검색된 문서와 답변이 다르면 왜 그래?
A. Grounding Rule 부족, Context Assembly 문제, 충돌 문서, Missing Information Rule 부재 때문일 수 있다.

Q. Answer Differs From Documents는 어떻게 고쳐?
A. Prompt를 강화하고 Context를 정리하며 Grounding Check를 수행해야 한다.

Q. Hallucinated Project Fact가 뭐야?
A. LLM이 프로젝트 문서에 없는 구체적 사실을 만들어내는 문제다.

Q. 프로젝트 문서에 없는 사실을 만들면 왜 위험해?
A. Agent가 실제 프로젝트와 다른 코드나 운영 절차를 만들 수 있기 때문이다.

Q. 문서에 없는 내용은 어떻게 답해야 해?
A. 확정하지 말고 부족한 정보와 필요한 문서를 표시해야 한다.

Q. Context Overload가 뭐야?
A. Prompt에 너무 많은 Context가 들어가 답변 품질이 떨어지는 문제다.

Q. Context Overload는 어떻게 해결해?
A. Top-K 조정, Deduplication, Metadata Filter, Compression, Conflict Handling을 적용한다.

Q. 오래된 문서가 검색되는 이유는 뭐야?
A. Reindex 누락, 오래된 Vector 잔존, version Metadata 누락, 중복 문서 때문이다.

Q. Outdated Document Retrieved는 어떻게 해결해?
A. 기존 Vector를 삭제하고 최신 문서를 Reindex하며 version과 updatedAt Metadata를 추가한다.

Q. Embedding Model을 바꾸면 기존 Vector를 써도 돼?
A. 권장하지 않는다. 전체 문서를 다시 Embedding하고 Reindex해야 한다.

Q. 같은 Collection에 여러 Embedding Model을 섞어도 돼?
A. 권장하지 않는다. Similarity Search 품질이 깨질 수 있다.

Q. Missing Metadata가 뭐야?
A. Chunk에 필요한 Metadata가 누락된 상태다.

Q. Metadata가 없으면 뭐가 문제야?
A. 출처 추적, 검색 필터링, Agent Routing, 최신성 판단, 답변 검증이 어려워진다.

Q. Wrong Metadata가 뭐야?
A. Chunk에 잘못된 Metadata가 붙은 상태다.

Q. Wrong Metadata가 위험한 이유는 뭐야?
A. 잘못된 문서가 정상 검색 결과처럼 사용될 수 있기 때문이다.

Q. Weak Grounding Prompt가 뭐야?
A. LLM이 Retrieved Context를 우선 사용하도록 충분히 지시하지 못하는 Prompt 상태다.

Q. RAG Prompt에 꼭 필요한 규칙은 뭐야?
A. Grounding Rule, Missing Information Rule, Citation Rule, Output Format Rule이다.

Q. Agent RAG Evaluation이 뭐야?
A. Agent 역할별로 RAG 검색과 답변 품질을 평가하는 과정이다.

Q. Agent별 Golden Query가 필요한 이유는 뭐야?
A. 각 Agent가 자기 역할에 맞는 문서를 검색하고 Grounded Answer를 생성하는지 확인하기 위해서다.

Q. Review Agent는 무엇을 우선 검색해야 해?
A. Master Rules, Domain Rules, Checklist, Troubleshooting 문서를 우선 검색해야 한다.

Q. AI Agent는 무엇을 우선 검색해야 해?
A. RAG, Agent Workflow, Evaluation, Guardrails 관련 AI Domain 문서를 우선 검색해야 한다.

Q. Evaluation Checklist는 왜 필요해?
A. RAG 검색, 답변, Metadata, Prompt, Agent 품질을 통합 검수하기 위해 필요하다.

Q. Evaluation Checklist는 언제 사용해?
A. 문서 제작 완료 후, Vector Store 적재 후, Reindex 후, Agent Workflow 변경 후 사용한다.

Q. RAG 문서는 한 번 업로드하면 끝이야?
A. 아니다. 문서 수정, 설정 변경, Agent 변경 시 계속 평가하고 Reindex해야 한다.

Q. FAQ를 추가해도 Reindex해야 해?
A. 해야 한다. FAQ는 Retrieval Matching에 직접 영향을 준다.

Q. Prompt 변경 후에도 평가가 필요해?
A. 필요하다. Generation Evaluation과 Grounding Check를 다시 수행해야 한다.

Q. Agent Role을 바꾸면 무엇을 해야 해?
A. Agent별 Golden Query와 Metadata Filter를 다시 검증해야 한다.

Q. RAG 운영의 최종 목표는 뭐야?
A. Agent가 필요한 문서를 안정적으로 검색하고 문서 근거 기반 답변을 생성하는 상태를 유지하는 것이다.
