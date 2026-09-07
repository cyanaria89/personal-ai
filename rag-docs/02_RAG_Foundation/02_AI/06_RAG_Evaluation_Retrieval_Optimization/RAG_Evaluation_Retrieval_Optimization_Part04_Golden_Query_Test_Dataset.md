# RAG Evaluation & Retrieval Optimization Part04 Golden Query & Test Dataset

---

# 1. Golden Query Core

## 1.1 Golden Query 기본 개념

### [개념]

Golden Query는 RAG 검색 품질과 답변 품질을 평가하기 위해 미리 정의한 기준 질문이다.

Golden Query는 실제 사용자가 물어볼 법한 표현으로 작성하며, Expected Document, Expected Section, Expected Chunk, Expected Answer Keyword와 연결한다.

```text
User-like Query
→ Expected Document
→ Expected Section
→ Expected Chunk
→ Expected Answer Keyword
→ Retrieval Test
→ Generation Test
```

---

### [핵심]

- Golden Query는 RAG 평가용 기준 질문이다.
- 실제 사용자 질문 형태로 작성한다.
- 문서 제목 그대로만 묻는 Query는 평가 품질이 낮다.
- Expected Document를 반드시 연결한다.
- Expected Section과 Expected Chunk를 가능하면 지정한다.
- Expected Answer Keyword를 포함한다.
- Retrieval Evaluation과 Generation Evaluation에 모두 사용한다.
- 실패 Query는 문서 개선과 재평가에 사용한다.

---

### [실무]

2026 실무 기준 Golden Query는 단순 검색 테스트가 아니라 RAG 품질 관리의 기준 데이터다.

Golden Query 기본 구조:

```json
{
  "query": "RAG 품질은 어떻게 평가해?",
  "expectedDocument": "RAG_Evaluation_Retrieval_Optimization_Part01_Core.md",
  "expectedSection": "RAG Evaluation Core",
  "expectedChunks": [
    "Retrieval Evaluation과 Generation Evaluation을 분리한다",
    "Groundedness와 Faithfulness를 검증한다"
  ],
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

Golden Query는 문서 제작 완료 후 반드시 같은 Query로 재평가한다.

---

### [FAQ]

Q. Golden Query가 뭐야?

A. RAG 검색 품질과 답변 품질을 평가하기 위해 미리 정의한 기준 질문이다.

Q. Golden Query는 왜 필요해?

A. RAG 품질을 감이 아니라 고정된 기준 질문으로 반복 평가하기 위해 필요하다.

Q. Golden Query는 문서 제목 그대로 만들면 돼?

A. 아니다. 실제 사용자가 물어볼 법한 표현으로 만들어야 한다.

Q. Golden Query는 Retrieval만 평가해?

A. 아니다. Retrieval Evaluation과 Generation Evaluation 모두에 사용할 수 있다.

Q. 실패한 Golden Query는 어떻게 해?

A. 실패 원인을 기록하고 문서 개선 후 같은 Query로 재평가한다.

---

## 1.2 Golden Query 필수 필드

### [개념]

Golden Query는 Query만 있으면 부족하다.

RAG 평가에 사용하려면 Expected Document, Expected Section, Expected Chunk, Expected Answer Keyword, Difficulty, Domain, Intent를 함께 정의해야 한다.

---

### [핵심]

- query는 실제 사용자 질문이다.
- expectedDocument는 검색되어야 하는 기준 문서다.
- expectedSection은 기준 문서 내부의 목표 Section이다.
- expectedChunk는 답변 근거가 되는 최소 Chunk다.
- expectedAnswerKeywords는 답변에 포함되어야 할 핵심 키워드다.
- difficulty는 질문 난이도다.
- domain은 질문이 속한 기술 영역이다.
- intent는 사용자 질문 의도다.
- failureType은 평가 실패 후 기록한다.

---

### [실무]

Golden Query 필드 정의:

| 필드                   | 의미                            | 필수 여부 |
| ---------------------- | ------------------------------- | --------- |
| query                  | 실제 사용자형 질문              | 필수      |
| expectedDocument       | 검색되어야 하는 문서            | 필수      |
| expectedSection        | 검색되어야 하는 Section         | 권장      |
| expectedChunk          | 검색되어야 하는 최소 근거       | 권장      |
| expectedAnswerKeywords | 답변 핵심 키워드                | 필수      |
| difficulty             | basic / intermediate / advanced | 권장      |
| domain                 | RAG Evaluation 등 Domain        | 필수      |
| intent                 | 질문 의도                       | 필수      |
| expectedFailureMode    | 예상 실패 유형                  | 선택      |
| notes                  | 평가 메모                       | 선택      |

Golden Query Dataset 예시:

```json
[
  {
    "query": "문서에 있는데 검색이 안 되면 뭐부터 봐?",
    "expectedDocument": "RAG_Evaluation_Retrieval_Optimization_Part02_Retrieval_Evaluation.md",
    "expectedSection": "Retrieval Failure Analysis",
    "expectedAnswerKeywords": [
      "Expected Document",
      "Chunk Header",
      "FAQ",
      "Retrieval Queries",
      "Metadata",
      "Reindex"
    ],
    "difficulty": "intermediate",
    "domain": "RAG Evaluation",
    "intent": "retrieval_failure_diagnosis"
  }
]
```

---

### [FAQ]

Q. Golden Query에는 어떤 필드가 필요해?

A. Query, Expected Document, Expected Section, Expected Chunk, Expected Answer Keyword, Difficulty, Domain, Intent가 필요하다.

Q. Expected Document는 필수야?

A. 필수다. 기대 문서가 없으면 Retrieval 성공 여부를 판단하기 어렵다.

Q. Expected Answer Keyword는 왜 필요해?

A. Generation Evaluation에서 답변이 필요한 핵심 내용을 포함했는지 확인하기 위해 필요하다.

Q. Difficulty는 왜 적어?

A. 쉬운 질문, 모호한 질문, 복합 질문을 균형 있게 평가하기 위해 사용한다.

Q. Intent는 왜 필요해?

A. Query Rewrite, Agent Routing, Answer Relevance 평가에 사용하기 위해 필요하다.

---

# 2. Golden Query Design

## 2.1 User-like Query

### [개념]

User-like Query는 실제 사용자가 입력할 법한 자연스러운 질문이다.

RAG 문서 제목이나 Section 제목을 그대로 묻는 Query만으로는 실제 검색 품질을 충분히 평가할 수 없다.

---

### [핵심]

- 실제 사용자 표현을 사용한다.
- 짧은 질문, 구어체 질문, 모호한 질문을 포함한다.
- 문서 제목 그대로만 쓰지 않는다.
- 한국어 질문과 영어 기술 용어를 함께 고려한다.
- 실무 문제 상황형 Query를 포함한다.
- Agent가 받을 실제 요청과 유사하게 만든다.
- 동일 의도의 표현 변형을 여러 개 만든다.

---

### [실무]

좋은 User-like Query와 나쁜 Query 비교:

| 유형 | Query                                    | 평가                    |
| ---- | ---------------------------------------- | ----------------------- |
| 나쁨 | RAG Evaluation Core                      | 문서 제목 검색에 가까움 |
| 좋음 | RAG 품질은 어떻게 평가해?                | 실제 사용자형 질문      |
| 좋음 | 검색은 됐는데 답변이 이상하면 어디를 봐? | 문제 상황형             |
| 좋음 | Hit@K가 높으면 끝이야?                   | 검증형                  |
| 좋음 | 문서에 있는데 왜 검색이 안 돼?           | 실패 분석형             |
| 좋음 | Top-K는 무조건 키우면 돼?                | 오해 교정형             |

User-like Query 생성 패턴:

```text
개념 질문:
- RAG 품질은 어떻게 평가해?
- Groundedness가 뭐야?

문제 상황:
- 문서에 있는데 검색이 안 돼
- 검색 결과는 맞는데 답변이 틀려

비교 질문:
- Precision과 Recall 차이는?
- Groundedness와 Faithfulness 차이는?

오해 교정:
- Top-K는 무조건 크게 하면 좋아?
- 답변이 맞으면 RAG 평가 통과야?
```

---

### [FAQ]

Q. User-like Query는 뭐야?

A. 실제 사용자가 입력할 법한 자연스러운 질문이다.

Q. 문서 제목 그대로 Query를 만들면 왜 부족해?

A. 실제 사용자는 문서 제목이 아니라 문제 상황이나 자연어로 질문하기 때문이다.

Q. 구어체 질문도 Golden Query에 넣어도 돼?

A. 넣는 것이 좋다. 실제 사용 환경에 가까운 평가가 가능하다.

Q. 같은 의도의 Query를 여러 개 만들어야 해?

A. 권장한다. 표현 변형에 대한 Retrieval 안정성을 확인할 수 있다.

Q. User-like Query는 어떤 형태가 좋아?

A. 개념 질문, 문제 상황, 비교 질문, 오해 교정 질문을 섞는 것이 좋다.

---

## 2.2 Difficulty Design

### [개념]

Difficulty Design은 Golden Query를 난이도별로 구성하는 기준이다.

RAG 평가는 쉬운 질문만으로는 부족하며, 모호한 질문과 복합 질문도 포함해야 한다.

---

### [핵심]

- basic Query는 단일 개념 질문이다.
- intermediate Query는 문제 해결 또는 비교 질문이다.
- advanced Query는 여러 문서가 필요한 복합 질문이다.
- ambiguous Query는 의도가 짧거나 불명확한 질문이다.
- failure-based Query는 과거 실패 사례를 기반으로 만든 질문이다.
- 난이도별 Query를 섞어야 실제 운영 품질을 평가할 수 있다.

---

### [실무]

Difficulty 기준:

| Difficulty    | 설명             | 예시                                                     |
| ------------- | ---------------- | -------------------------------------------------------- |
| basic         | 단일 개념 정의   | Hit@K가 뭐야?                                            |
| intermediate  | 비교 / 문제 해결 | Precision과 Recall 차이는?                               |
| advanced      | 여러 개념 결합   | Retrieval은 성공했는데 Hallucination이 나면 어디를 고쳐? |
| ambiguous     | 짧고 모호한 질문 | 검색이 이상해                                            |
| failure-based | 실제 실패 기반   | 문서 수정했는데 검색 결과가 그대로야                     |

난이도별 권장 비율:

| Dataset 규모 | basic | intermediate | advanced | ambiguous | failure-based |
| ------------ | ----: | -----------: | -------: | --------: | ------------: |
| 20개         |     6 |            6 |        4 |         2 |             2 |
| 50개         |    12 |           15 |       10 |         6 |             7 |
| 100개        |    20 |           30 |       20 |        15 |            15 |

---

### [FAQ]

Q. Golden Query 난이도는 왜 나눠?

A. 쉬운 질문만 평가하면 실제 사용자 질문에 대한 검색 품질을 알기 어렵기 때문이다.

Q. Basic Query는 뭐야?

A. 단일 개념을 묻는 쉬운 질문이다.

Q. Advanced Query는 뭐야?

A. 여러 개념이나 여러 문서를 함께 참조해야 하는 복합 질문이다.

Q. Ambiguous Query도 넣어야 해?

A. 넣는 것이 좋다. 실제 사용자는 짧고 모호하게 질문하는 경우가 많다.

Q. Failure-based Query는 뭐야?

A. 실제 검색 실패나 답변 실패 사례를 기준으로 만든 Golden Query다.

---

## 2.3 Intent Design

### [개념]

Intent Design은 Golden Query가 어떤 사용자 의도를 평가하는지 명확히 정의하는 과정이다.

Intent가 명확해야 Query Rewrite, Agent Routing, Retrieval Evaluation, Answer Relevance 평가가 가능하다.

---

### [핵심]

- Intent는 Query의 목적이다.
- 같은 문서라도 Intent에 따라 기대 Section이 다를 수 있다.
- Intent는 짧고 일관된 값으로 정의한다.
- Agent Routing에 사용할 수 있게 Domain과 함께 관리한다.
- Intent는 Answer Relevance 평가 기준이 된다.
- 모호한 Query는 Intent 후보를 여러 개 가질 수 있다.

---

### [실무]

Intent 예시:

| Intent                       | 의미                    | Query 예시                     |
| ---------------------------- | ----------------------- | ------------------------------ |
| evaluation_core              | RAG 평가 기본 구조 질문 | RAG 품질은 어떻게 평가해?      |
| retrieval_failure_diagnosis  | 검색 실패 원인 분석     | 문서에 있는데 검색이 안 돼     |
| generation_failure_diagnosis | 생성 실패 원인 분석     | 검색 결과는 맞는데 답변이 틀려 |
| metric_definition            | 평가 지표 정의          | Hit@K가 뭐야?                  |
| metric_comparison            | 평가 지표 비교          | Precision과 Recall 차이는?     |
| grounding_check              | 문서 근거 검증          | 답변 근거는 어떻게 확인해?     |
| optimization_decision        | 개선 조치 판단          | Top-K는 언제 늘려?             |
| report_creation              | 리포트 작성             | RAG 품질 리포트는 어떻게 써?   |

Intent 기록 예시:

```json
{
  "query": "검색은 됐는데 답변이 이상해",
  "intent": "generation_failure_diagnosis",
  "domain": "RAG Evaluation",
  "expectedDocument": "RAG_Evaluation_Retrieval_Optimization_Part03_Generation_Evaluation.md"
}
```

---

### [FAQ]

Q. Intent는 뭐야?

A. 사용자 Query의 목적이나 의도다.

Q. Golden Query에 Intent가 왜 필요해?

A. 검색 평가, 답변 관련도 평가, Agent Routing, Query Rewrite에 사용되기 때문이다.

Q. 같은 Query가 여러 Intent를 가질 수 있어?

A. 모호한 Query는 여러 Intent 후보를 가질 수 있다.

Q. Intent 값은 길게 써도 돼?

A. 짧고 일관된 키워드 형태가 좋다.

Q. Intent가 틀리면 어떤 문제가 생겨?

A. 잘못된 문서를 검색하거나 질문과 맞지 않는 답변을 생성할 수 있다.

---

# 3. Expected Answer Design

## 3.1 Expected Answer Keyword

### [개념]

Expected Answer Keyword는 Generated Answer에 포함되어야 하는 핵심 키워드 목록이다.

Generation Evaluation에서 Answer Completeness와 Answer Relevance를 확인하는 기준으로 사용한다.

---

### [핵심]

- Expected Answer Keyword는 정답 방향을 나타낸다.
- 답변에 반드시 포함되어야 할 핵심 개념을 지정한다.
- 단어 하나보다 의미 단위 키워드가 좋다.
- 너무 많은 키워드를 넣으면 평가가 경직된다.
- 필수 키워드와 선택 키워드를 구분할 수 있다.
- Retrieval Evaluation보다 Generation Evaluation에 더 중요하다.

---

### [실무]

Expected Answer Keyword 예시:

```json
{
  "query": "RAG 품질은 어떻게 평가해?",
  "expectedAnswerKeywords": {
    "required": [
      "Retrieval Evaluation",
      "Generation Evaluation",
      "Groundedness",
      "Faithfulness"
    ],
    "optional": ["Hit@K", "Precision", "Recall", "Hallucination Check"]
  }
}
```

평가 기준:

| 상태                       | 판단              |
| -------------------------- | ----------------- |
| 필수 키워드 모두 포함      | Completeness 높음 |
| 필수 키워드 일부 누락      | Partial           |
| 필수 키워드 대부분 누락    | Fail              |
| 선택 키워드 포함           | 답변 보강         |
| 관련 없는 키워드 과다 포함 | Relevance 낮음    |

---

### [FAQ]

Q. Expected Answer Keyword는 뭐야?

A. Generated Answer에 포함되어야 하는 핵심 키워드 목록이다.

Q. Expected Answer Keyword는 왜 필요해?

A. 답변이 필요한 핵심 내용을 포함했는지 평가하기 위해 필요하다.

Q. 키워드는 많을수록 좋아?

A. 아니다. 너무 많으면 평가가 경직되고 핵심 판단이 어려워진다.

Q. 필수 키워드와 선택 키워드를 나눠도 돼?

A. 가능하다. 필수 내용과 보조 내용을 구분할 수 있다.

Q. 키워드가 없으면 Generation Evaluation이 어려워져?

A. 어렵다. Answer Completeness를 객관적으로 판단하기 힘들다.

---

## 3.2 Expected Answer Pattern

### [개념]

Expected Answer Pattern은 Query 유형별로 답변이 가져야 하는 구조다.

RAG 답변은 키워드만 포함하면 충분하지 않으며, 질문 유형에 맞는 답변 구조를 가져야 한다.

---

### [핵심]

- 정의 질문은 짧은 정의와 핵심 특징을 포함한다.
- 비교 질문은 비교 기준을 포함한다.
- 절차 질문은 순서를 포함한다.
- 문제 해결 질문은 원인과 해결을 포함한다.
- 평가 질문은 지표와 판단 기준을 포함한다.
- 정보 부족 질문은 부족함을 명확히 표시한다.
- 답변 구조는 Answer Completeness 평가 기준이 된다.

---

### [실무]

Query 유형별 Expected Answer Pattern:

| Query 유형     | Expected Answer Pattern                  |
| -------------- | ---------------------------------------- |
| 정의 질문      | 정의 → 핵심 특징                         |
| 비교 질문      | A 정의 → B 정의 → 차이                   |
| 절차 질문      | Step 1 → Step 2 → Step 3                 |
| 문제 해결 질문 | 증상 → 원인 → 해결                       |
| 평가 질문      | 평가 대상 → 지표 → 판단                  |
| 오해 교정 질문 | 오해 부정 → 조건부 설명                  |
| 정보 부족 질문 | 확인 불가 → 근거 있는 범위 → 필요한 정보 |

Expected Answer Pattern 예시:

```json
{
  "query": "Top-K는 무조건 크게 하면 좋아?",
  "expectedAnswerPattern": {
    "type": "misconception_correction",
    "structure": [
      "무조건 크게 하는 것은 아님",
      "필요 문서 누락 시 증가",
      "노이즈 많으면 감소 또는 Reranking",
      "Precision / Recall 균형 고려"
    ]
  }
}
```

---

### [FAQ]

Q. Expected Answer Pattern은 뭐야?

A. Query 유형별로 답변이 가져야 하는 구조다.

Q. 키워드만 맞으면 답변 평가 통과야?

A. 아니다. 질문 유형에 맞는 구조와 판단 기준도 필요하다.

Q. 문제 해결 질문은 어떤 구조가 좋아?

A. 증상, 원인, 해결 순서가 좋다.

Q. 비교 질문은 어떤 구조가 좋아?

A. 비교 대상의 정의와 차이점을 함께 제시해야 한다.

Q. 오해 교정 질문은 어떻게 답해야 해?

A. 잘못된 전제를 먼저 부정하고 조건부 기준을 설명해야 한다.

---

# 4. Test Dataset Design

## 4.1 RAG Test Dataset 기본 개념

### [개념]

RAG Test Dataset은 여러 Golden Query를 모아 RAG 품질을 반복 평가할 수 있도록 만든 기준 데이터셋이다.

Test Dataset은 Retrieval Evaluation, Generation Evaluation, Optimization Retest에 사용한다.

---

### [핵심]

- Test Dataset은 Golden Query 묶음이다.
- Domain별로 분리한다.
- Level별로 분리할 수 있다.
- 난이도별 Query를 포함한다.
- Intent별 Query를 포함한다.
- 실패 사례 기반 Query를 포함한다.
- 평가 결과와 함께 버전 관리한다.
- 문서 개선 후 같은 Dataset으로 재평가한다.

---

### [실무]

RAG Test Dataset 기본 구조:

```json
{
  "datasetName": "RAG_Evaluation_Golden_Query_Set_v1",
  "domain": "RAG Evaluation & Retrieval Optimization",
  "version": "v1.0",
  "createdAt": "2026-06-30",
  "queryCount": 20,
  "queries": [
    {
      "id": "rag-eval-001",
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
      "intent": "evaluation_core"
    }
  ]
}
```

Dataset 운영 기준:

| 기준             | 설명                             |
| ---------------- | -------------------------------- |
| Domain 분리      | Agent Routing과 평가 범위 명확화 |
| Version 관리     | 개선 전후 비교                   |
| Query Count 기록 | 평가 규모 확인                   |
| 실패 사례 반영   | 실제 운영 품질 개선              |
| Retest 고정      | 같은 조건으로 재평가             |

---

### [FAQ]

Q. RAG Test Dataset은 뭐야?

A. 여러 Golden Query를 모아 RAG 품질을 반복 평가할 수 있도록 만든 기준 데이터셋이다.

Q. Test Dataset은 왜 필요해?

A. 개선 전후 검색 품질과 답변 품질을 같은 기준으로 비교하기 위해 필요하다.

Q. Dataset은 Domain별로 나눠야 해?

A. 권장한다. Domain별 검색 품질과 Agent Routing 품질을 따로 평가할 수 있다.

Q. Dataset 버전은 왜 관리해?

A. 문서 개선 전후 평가 결과를 비교하기 위해 필요하다.

Q. 실패 Query도 Dataset에 넣어야 해?

A. 넣는 것이 좋다. 실제 취약점을 반복 평가할 수 있다.

---

## 4.2 Dataset Size

### [개념]

Dataset Size는 RAG 품질 평가에 사용하는 Golden Query 개수다.

너무 적으면 평가 신뢰도가 낮고, 너무 많으면 운영 비용이 커진다.

---

### [핵심]

- 초기 문서 검수는 20개 내외로 시작할 수 있다.
- Domain 안정화에는 50개 이상이 좋다.
- 핵심 운영 Domain은 100개 이상으로 확장할 수 있다.
- Query 수보다 Intent와 Difficulty 균형이 중요하다.
- 실패 Query를 누적하면 Dataset 품질이 높아진다.
- 너무 큰 Dataset은 Retest 비용을 고려해야 한다.

---

### [실무]

Dataset Size 기준:

| 단계               | Query Count | 용도                  |
| ------------------ | ----------: | --------------------- |
| Smoke Test         |      5 ~ 10 | 기본 검색 확인        |
| Initial Evaluation |     20 ~ 30 | 문서 초도 검수        |
| Domain Evaluation  |    50 ~ 100 | Domain 품질 평가      |
| Regression Test    |        100+ | 운영 품질 회귀 테스트 |

RAG Evaluation Domain 권장 시작 구성:

| Query 유형                 | 개수 |
| -------------------------- | ---: |
| Core 개념 질문             |    5 |
| Retrieval Evaluation 질문  |    5 |
| Generation Evaluation 질문 |    5 |
| Optimization 질문          |    5 |
| Failure Analysis 질문      |    5 |
| Report 작성 질문           |    5 |

총 30개로 시작 후 실패 Query를 누적한다.

---

### [FAQ]

Q. Golden Query는 몇 개가 적당해?

A. 초기 검수는 20~30개, Domain 평가는 50개 이상이 좋다.

Q. Query 수가 많으면 무조건 좋아?

A. 아니다. Intent와 Difficulty 균형이 더 중요하다.

Q. Smoke Test는 뭐야?

A. 5~10개 Query로 기본 검색 동작을 빠르게 확인하는 테스트다.

Q. Regression Test는 뭐야?

A. 문서 수정 후 기존 품질이 깨지지 않았는지 확인하는 회귀 테스트다.

Q. 실패 Query는 계속 추가해야 해?

A. 추가하는 것이 좋다. 실제 취약점을 지속적으로 검증할 수 있다.

---

## 4.3 Dataset Versioning

### [개념]

Dataset Versioning은 RAG Test Dataset의 변경 이력을 관리하는 방식이다.

Dataset이 바뀌면 평가 결과도 달라지므로 Version, 변경 이유, Query Count를 기록해야 한다.

---

### [핵심]

- Dataset에는 Version을 부여한다.
- Query 추가, 수정, 삭제를 기록한다.
- Query Count 변화를 기록한다.
- 평가 결과는 Dataset Version과 함께 저장한다.
- 문서 개선 전후 비교는 같은 Dataset Version으로 수행한다.
- Dataset 자체가 바뀌면 이전 평가 결과와 직접 비교하기 어렵다.

---

### [실무]

Dataset Version 기록 예시:

```md
# Dataset Version Log

| Version | Date       | Query Count | Change              | Reason               |
| ------- | ---------- | ----------: | ------------------- | -------------------- |
| v1.0    | 2026-06-30 |          30 | Initial Dataset     | 초도 평가            |
| v1.1    | 2026-07-05 |          36 | 실패 Query 6개 추가 | 운영 실패 반영       |
| v1.2    | 2026-07-10 |          40 | 모호한 Query 추가   | Ambiguous Query 보강 |
```

평가 결과 기록 시 Version 연결:

```md
# Evaluation Result

- Dataset: RAG_Evaluation_Golden_Query_Set
- Dataset Version: v1.1
- Query Count: 36
- Evaluation Date: 2026-07-05
- Hit@3: 0.86
```

---

### [FAQ]

Q. Dataset Versioning은 뭐야?

A. RAG Test Dataset의 변경 이력을 관리하는 방식이다.

Q. Dataset Version을 왜 기록해?

A. Dataset이 바뀌면 평가 결과도 달라지기 때문이다.

Q. Query를 추가하면 Version을 올려야 해?

A. 올리는 것이 좋다. 평가 기준이 바뀌었기 때문이다.

Q. 서로 다른 Dataset Version 결과를 직접 비교해도 돼?

A. 주의해야 한다. Query 구성이 다르면 결과가 달라질 수 있다.

Q. 문서 개선 전후 비교는 어떤 Dataset으로 해야 해?

A. 같은 Dataset Version으로 해야 정확하다.

---

# 5. Golden Query Set for RAG Evaluation Domain

## 5.1 Core Evaluation Query Set

### [개념]

Core Evaluation Query Set은 RAG Evaluation의 기본 개념, Retrieval / Generation 분리, Groundedness, Faithfulness를 평가하는 Query 묶음이다.

---

### [핵심]

- Part01 Core 문서 검색성을 평가한다.
- RAG Evaluation 기본 구조를 검증한다.
- Retrieval과 Generation 분리 개념을 검증한다.
- Groundedness와 Faithfulness 기본 개념을 검증한다.
- RAG 실패 분류 기본 이해를 확인한다.

---

### [실무]

Core Evaluation Query Set 예시:

| ID       | Query                                    | Expected Document | Intent                 | Difficulty   |
| -------- | ---------------------------------------- | ----------------- | ---------------------- | ------------ |
| core-001 | RAG 품질은 어떻게 평가해?                | Part01_Core       | evaluation_core        | basic        |
| core-002 | 답변이 맞으면 RAG 평가 통과야?           | Part01_Core       | grounded_answer_check  | basic        |
| core-003 | 검색 실패랑 생성 실패는 어떻게 나눠?     | Part01_Core       | failure_classification | intermediate |
| core-004 | RAG 답변이 문서 근거에 맞는지 어떻게 봐? | Part01_Core       | grounding_check        | intermediate |
| core-005 | RAG 개선은 어떤 순서로 해야 해?          | Part01_Core       | evaluation_loop        | intermediate |

Expected Answer Keywords:

| Query ID | Required Keywords                                                       |
| -------- | ----------------------------------------------------------------------- |
| core-001 | Retrieval Evaluation, Generation Evaluation, Groundedness, Faithfulness |
| core-002 | 검색 문서 근거, Groundedness, Unsupported Claim                         |
| core-003 | Retrieval Failure, Generation Failure                                   |
| core-004 | Claim, Evidence Match, Groundedness                                     |
| core-005 | Golden Query, Failure Analysis, Reindex, Retest                         |

---

### [FAQ]

Q. Core Evaluation Query Set은 뭐야?

A. RAG Evaluation의 기본 개념과 실패 분류를 평가하는 Query 묶음이다.

Q. Core Query는 어떤 문서를 대상으로 해?

A. 주로 Part01 Core 문서를 대상으로 한다.

Q. Core Query에서 꼭 확인할 개념은 뭐야?

A. Retrieval Evaluation, Generation Evaluation, Groundedness, Faithfulness, Evaluation Loop다.

Q. Core Query가 실패하면 무엇을 고쳐야 해?

A. Part01의 Header, FAQ, Retrieval Queries, 핵심 키워드를 보강한다.

Q. Core Query는 몇 개로 시작해?

A. 최소 5개 이상으로 시작하는 것이 좋다.

---

## 5.2 Retrieval Evaluation Query Set

### [개념]

Retrieval Evaluation Query Set은 Expected Document, Expected Chunk, Hit@K, Precision, Recall, Ranking Quality 검색성을 평가하는 Query 묶음이다.

---

### [핵심]

- Part02 Retrieval Evaluation 문서 검색성을 평가한다.
- Expected Document / Section / Chunk 개념 검색을 확인한다.
- Hit@K와 Retrieval Hit Rate 검색성을 확인한다.
- Precision / Recall 비교 검색성을 확인한다.
- Ranking Quality, MRR, NDCG 검색성을 확인한다.
- Retrieval Failure 진단 검색성을 확인한다.

---

### [실무]

Retrieval Evaluation Query Set 예시:

| ID      | Query                               | Expected Document           | Intent                      | Difficulty   |
| ------- | ----------------------------------- | --------------------------- | --------------------------- | ------------ |
| ret-001 | Retrieval Evaluation은 뭐야?        | Part02_Retrieval_Evaluation | retrieval_definition        | basic        |
| ret-002 | Expected Chunk가 왜 중요해?         | Part02_Retrieval_Evaluation | expected_chunk              | basic        |
| ret-003 | Hit@K가 높으면 검색 품질 좋은 거야? | Part02_Retrieval_Evaluation | hit_at_k_interpretation     | intermediate |
| ret-004 | Precision과 Recall 차이는?          | Part02_Retrieval_Evaluation | metric_comparison           | basic        |
| ret-005 | 문서에 있는데 검색이 안 돼          | Part02_Retrieval_Evaluation | retrieval_failure_diagnosis | intermediate |
| ret-006 | 검색 결과에 엉뚱한 문서가 많이 섞여 | Part02_Retrieval_Evaluation | low_precision               | intermediate |
| ret-007 | 관련 문서가 뒤쪽에 나와             | Part02_Retrieval_Evaluation | low_ranking                 | intermediate |

Expected Answer Keywords:

| Query ID | Required Keywords                                   |
| -------- | --------------------------------------------------- |
| ret-001  | Expected Document, Expected Chunk, Retrieved Chunks |
| ret-002  | 최소 근거, Grounded Answer, Chunk                   |
| ret-003  | Hit@K, Precision, Ranking Quality                   |
| ret-004  | Precision, Recall, Top-K                            |
| ret-005  | Header, FAQ, Retrieval Queries, Metadata, Reindex   |
| ret-006  | Precision, Top-K, Threshold, Metadata Filter        |
| ret-007  | Ranking Quality, MRR, Reranking                     |

---

### [FAQ]

Q. Retrieval Evaluation Query Set은 뭐야?

A. 검색 품질 지표와 Retrieval 실패 진단을 평가하는 Query 묶음이다.

Q. Retrieval Query는 어떤 문서를 대상으로 해?

A. 주로 Part02 Retrieval Evaluation 문서를 대상으로 한다.

Q. Retrieval Query에서 꼭 확인할 지표는 뭐야?

A. Hit@K, Precision, Recall, Ranking Quality, MRR이다.

Q. 검색 실패 Query는 포함해야 해?

A. 포함해야 한다. 실제 Retrieval Failure 진단 능력을 평가할 수 있다.

Q. Retrieval Query가 실패하면 무엇을 고쳐?

A. Expected Document, Header, FAQ, Retrieval Queries, Metadata를 보강한다.

---

## 5.3 Generation Evaluation Query Set

### [개념]

Generation Evaluation Query Set은 Groundedness, Faithfulness, Claim Extraction, Hallucination Check, Missing Information Handling 검색성과 답변 품질을 평가하는 Query 묶음이다.

---

### [핵심]

- Part03 Generation Evaluation 문서 검색성을 평가한다.
- Claim Extraction 개념을 확인한다.
- Supported Claim / Unsupported Claim 구분을 확인한다.
- Groundedness와 Faithfulness 차이를 확인한다.
- Hallucination Check 기준을 확인한다.
- Missing Information Handling을 확인한다.
- Generation Failure 진단을 확인한다.

---

### [실무]

Generation Evaluation Query Set 예시:

| ID      | Query                                    | Expected Document            | Intent                       | Difficulty   |
| ------- | ---------------------------------------- | ---------------------------- | ---------------------------- | ------------ |
| gen-001 | Generation Evaluation은 뭐야?            | Part03_Generation_Evaluation | generation_definition        | basic        |
| gen-002 | 답변 근거는 어떻게 확인해?               | Part03_Generation_Evaluation | groundedness_check           | basic        |
| gen-003 | Groundedness와 Faithfulness 차이는?      | Part03_Generation_Evaluation | metric_comparison            | intermediate |
| gen-004 | 문서에 없는 내용을 말하면 어떻게 평가해? | Part03_Generation_Evaluation | unsupported_claim            | intermediate |
| gen-005 | Hallucination은 어떻게 확인해?           | Part03_Generation_Evaluation | hallucination_check          | intermediate |
| gen-006 | 검색 결과는 맞는데 답변이 틀려           | Part03_Generation_Evaluation | generation_failure_diagnosis | intermediate |
| gen-007 | 문서에 정보가 없으면 어떻게 답해야 해?   | Part03_Generation_Evaluation | missing_information_handling | basic        |

Expected Answer Keywords:

| Query ID | Required Keywords                                           |
| -------- | ----------------------------------------------------------- |
| gen-001  | Retrieved Context, Generated Answer, Claim, Evidence        |
| gen-002  | Claim Extraction, Evidence Match, Supported Claim           |
| gen-003  | Groundedness, Faithfulness, 근거, 왜곡                      |
| gen-004  | Unsupported Claim, Hallucination, Assumption                |
| gen-005  | Claim, Retrieved Context, Fabricated Detail, Wrong Citation |
| gen-006  | Prompt, Context Assembly, Grounding Rule, Faithfulness      |
| gen-007  | 정보 부족, 확인 불가, 확정 답변 회피                        |

---

### [FAQ]

Q. Generation Evaluation Query Set은 뭐야?

A. 생성 답변의 근거성, 충실성, Hallucination 검증을 평가하는 Query 묶음이다.

Q. Generation Query는 어떤 문서를 대상으로 해?

A. 주로 Part03 Generation Evaluation 문서를 대상으로 한다.

Q. Generation Query에서 꼭 확인할 개념은 뭐야?

A. Claim Extraction, Groundedness, Faithfulness, Hallucination Check다.

Q. Missing Information Query는 왜 필요해?

A. 문서에 정보가 없을 때 확정 답변을 피하는지 평가하기 위해 필요하다.

Q. Generation Query가 실패하면 무엇을 고쳐?

A. Grounding Rule, Claim 검증, FAQ, Retrieval Queries, 답변 패턴을 보강한다.

---

# 6. Failure-based Golden Query

## 6.1 Failure-based Query 기본 개념

### [개념]

Failure-based Golden Query는 실제 Retrieval Failure 또는 Generation Failure 사례를 기준으로 만든 평가 Query다.

실패 사례를 Golden Query로 전환하면 동일한 문제가 다시 발생하는지 회귀 테스트할 수 있다.

---

### [핵심]

- 실패 Query는 버리지 않는다.
- 실패 Query는 Golden Query Dataset에 추가한다.
- 실패 원인과 기대 문서를 함께 기록한다.
- 수정 후 같은 Query로 재평가한다.
- 반복 실패 Query는 우선 개선 대상이다.
- Failure-based Query는 실제 운영 품질 개선에 가장 직접적이다.

---

### [실무]

Failure-based Query 전환 예시:

```md
# Failure Case

User Query:
검색은 됐는데 답변이 이상해

Observed Failure:
Part02 Retrieval 문서는 검색됐지만 Part03 Generation 문서가 누락됨

Expected:

- Expected Document: RAG_Evaluation_Retrieval_Optimization_Part03_Generation_Evaluation.md
- Expected Section: Generation Failure Analysis
- Expected Keywords: Generation Failure, Grounding Rule, Faithfulness, Hallucination Check

Action:

- Part03 Retrieval Queries에 "검색 결과는 맞는데 답변이 틀려" 추가
- Reindex
- Retest
```

Failure-based Query 기록 필드:

| 필드             | 의미                   |
| ---------------- | ---------------------- |
| originalQuery    | 실제 실패 Query        |
| observedFailure  | 관찰된 실패            |
| expectedDocument | 기대 문서              |
| expectedSection  | 기대 Section           |
| failureType      | Retrieval / Generation |
| fixAction        | 수정 조치              |
| retestResult     | 재평가 결과            |

---

### [FAQ]

Q. Failure-based Golden Query는 뭐야?

A. 실제 실패 사례를 기준으로 만든 평가 Query다.

Q. 실패 Query를 왜 Dataset에 추가해?

A. 같은 문제가 다시 발생하는지 회귀 테스트하기 위해서다.

Q. 실패 Query는 언제 추가해?

A. Retrieval Failure나 Generation Failure가 확인된 후 추가한다.

Q. 반복 실패 Query는 어떻게 처리해?

A. 우선 개선 대상으로 보고 Header, FAQ, Retrieval Queries, Prompt를 보강한다.

Q. Failure-based Query는 어떤 장점이 있어?

A. 실제 운영 취약점을 직접 개선하는 데 효과적이다.

---

## 6.2 Failure Query Retest

### [개념]

Failure Query Retest는 실패 Query를 기준으로 문서 수정, Reindex, 재평가를 수행하는 과정이다.

개선 조치가 실제로 효과가 있었는지 확인하는 필수 단계다.

---

### [핵심]

- 실패 Query를 고정한다.
- 실패 유형을 기록한다.
- 문서 수정 전 결과를 저장한다.
- Header, FAQ, Retrieval Queries, Metadata, Prompt를 개선한다.
- Reindex를 수행한다.
- 같은 Query로 재평가한다.
- 개선 전후 Hit@K, Precision, Recall, Groundedness를 비교한다.

---

### [실무]

Failure Query Retest Flow:

```text
Failure Query
→ Record Baseline Result
→ Analyze Failure Type
→ Apply Fix
→ Reindex
→ Retest Same Query
→ Compare Result
→ Update Report
```

Retest 기록 예시:

```md
# Failure Query Retest

## Query

문서에 있는데 검색이 안 돼

## Before

- Expected Document: Part02_Retrieval_Evaluation
- Retrieved Rank: Not Found
- Failure Type: Document Miss

## Fix

- FAQ 추가
- Retrieval Queries 보강
- Header Keyword 추가
- Reindex 완료

## After

- Retrieved Rank: 2
- Hit@3: Pass
- Result: Improved
```

---

### [FAQ]

Q. Failure Query Retest는 뭐야?

A. 실패 Query를 기준으로 수정 전후 검색 품질을 다시 평가하는 과정이다.

Q. Retest는 왜 같은 Query로 해야 해?

A. 같은 조건에서 개선 효과를 비교해야 하기 때문이다.

Q. 문서 수정 후 Retest 전에 무엇을 해야 해?

A. Reindex를 수행해야 한다.

Q. Retest에서 어떤 지표를 비교해?

A. Hit@K, Precision, Recall, Ranking Quality, Groundedness를 비교한다.

Q. Retest 후에도 실패하면 어떻게 해?

A. 실패 원인을 다시 분류하고 Chunk, Metadata, Query Rewrite, Reranking까지 검토한다.

---

# 7. Golden Query Quality Checklist

## 7.1 Golden Query Checklist

### [개념]

Golden Query Quality Checklist는 Golden Query가 실제 RAG 평가에 적합한지 검수하는 기준이다.

좋은 Golden Query는 검색 가능한 문서, 기대 답변, 사용자 의도, 실패 분석 기준을 함께 가진다.

---

### [핵심]

- 실제 사용자 질문 형태인가?
- Expected Document가 명확한가?
- Expected Section이 지정되었는가?
- Expected Answer Keyword가 있는가?
- Intent가 명확한가?
- Difficulty가 지정되었는가?
- 너무 인위적인 문서 제목 Query가 아닌가?
- 표현 변형 Query가 포함되었는가?
- 실패 사례 기반 Query가 포함되었는가?
- 재평가에 사용할 수 있는가?

---

### [실무]

Golden Query Checklist:

```md
### [Checklist]

- [ ] Query가 실제 사용자 질문 형태인가?
- [ ] Query가 문서 제목 그대로만 작성되지 않았는가?
- [ ] Expected Document가 파일명 기준으로 명확한가?
- [ ] Expected Section이 지정되었는가?
- [ ] Expected Chunk 또는 핵심 근거가 정의되었는가?
- [ ] Expected Answer Keyword가 정의되었는가?
- [ ] Intent가 명확한가?
- [ ] Difficulty가 지정되었는가?
- [ ] 같은 의도의 표현 변형이 있는가?
- [ ] Retrieval Evaluation에 사용할 수 있는가?
- [ ] Generation Evaluation에 사용할 수 있는가?
- [ ] 실패 시 Failure Type을 기록할 수 있는가?
- [ ] 개선 후 같은 Query로 Retest할 수 있는가?
```

Golden Query 품질이 낮으면 RAG 평가 결과도 신뢰하기 어렵다.

---

### [FAQ]

Q. Golden Query 품질은 어떻게 검수해?

A. 사용자형 질문인지, Expected Document와 Expected Answer가 명확한지 확인한다.

Q. 나쁜 Golden Query는 어떤 Query야?

A. 문서 제목만 반복하거나 기대 문서와 답변 기준이 없는 Query다.

Q. Expected Answer Keyword가 없으면 문제야?

A. Generation Evaluation에서 Completeness 판단이 어려워진다.

Q. Intent가 없는 Query는 왜 문제야?

A. Query Rewrite, Agent Routing, Answer Relevance 평가가 어려워진다.

Q. Golden Query Checklist는 언제 사용해?

A. Dataset 생성 전과 문서 개선 후 Query를 추가할 때 사용한다.

---

## 7.2 Test Dataset Checklist

### [개념]

Test Dataset Checklist는 RAG Test Dataset이 Domain 평가에 적절한 균형과 추적성을 가지는지 검수하는 기준이다.

Dataset은 Query 수보다 구성 품질이 중요하다.

---

### [핵심]

- Domain이 명확한가?
- Dataset Version이 있는가?
- Query Count가 기록되었는가?
- 난이도 분포가 균형적인가?
- Intent 분포가 균형적인가?
- Retrieval Query와 Generation Query가 모두 포함되었는가?
- Failure-based Query가 포함되었는가?
- 평가 결과와 연결 가능한가?
- 개선 전후 같은 Version으로 비교 가능한가?

---

### [실무]

Test Dataset Checklist:

```md
### [Checklist]

- [ ] Dataset Name이 명확한가?
- [ ] Domain이 명확한가?
- [ ] Version이 기록되었는가?
- [ ] Query Count가 기록되었는가?
- [ ] basic / intermediate / advanced Query가 포함되었는가?
- [ ] ambiguous Query가 포함되었는가?
- [ ] failure-based Query가 포함되었는가?
- [ ] Retrieval Evaluation용 Query가 포함되었는가?
- [ ] Generation Evaluation용 Query가 포함되었는가?
- [ ] Expected Document가 모든 Query에 있는가?
- [ ] Expected Answer Keyword가 모든 Query에 있는가?
- [ ] Dataset 변경 이력이 기록되는가?
- [ ] Evaluation Report와 연결되는가?
- [ ] Retest에 사용할 수 있는가?
```

Dataset Version과 Evaluation Report는 함께 관리한다.

---

### [FAQ]

Q. Test Dataset 품질은 어떻게 검수해?

A. Domain, Version, Query Count, 난이도, Intent, Expected Document, Expected Answer Keyword를 확인한다.

Q. Query 수만 많으면 좋은 Dataset이야?

A. 아니다. 난이도와 Intent 균형이 중요하다.

Q. Failure-based Query는 꼭 필요해?

A. 권장한다. 실제 실패를 회귀 테스트할 수 있기 때문이다.

Q. Dataset Version과 Evaluation Report는 연결해야 해?

A. 연결해야 한다. 평가 결과 해석에 Dataset Version이 필요하다.

Q. Dataset을 수정하면 무엇을 해야 해?

A. Version을 갱신하고 변경 이력을 기록한다.

---

# 8. Common Mistakes

## 8.1 Golden Query 자주 발생하는 실수

### [개념]

Golden Query 작성에서 가장 흔한 실수는 문서 제목을 그대로 Query로 사용하고 Expected Document만 확인하는 것이다.

실제 사용자형 Query, Expected Answer, Intent, Failure Type이 없으면 RAG 평가 품질이 낮아진다.

---

### [핵심]

- 문서 제목 그대로 Query를 만든다.
- Expected Document를 지정하지 않는다.
- Expected Answer Keyword가 없다.
- Intent가 없다.
- Difficulty가 모두 basic이다.
- 표현 변형 Query가 없다.
- 실패 Query를 Dataset에 반영하지 않는다.
- Dataset Version을 관리하지 않는다.
- 평가 결과를 Dataset Version과 연결하지 않는다.
- Retest를 다른 Query로 수행한다.

---

### [실무]

잘못된 Golden Query 예시:

```json
{
  "query": "Retrieval Evaluation",
  "expectedDocument": "Part02.md"
}
```

개선된 Golden Query 예시:

```json
{
  "query": "문서에 있는데 검색이 안 되면 뭐부터 봐?",
  "expectedDocument": "RAG_Evaluation_Retrieval_Optimization_Part02_Retrieval_Evaluation.md",
  "expectedSection": "Retrieval Failure Analysis",
  "expectedAnswerKeywords": [
    "Expected Document",
    "Header",
    "FAQ",
    "Retrieval Queries",
    "Metadata",
    "Reindex"
  ],
  "difficulty": "intermediate",
  "domain": "RAG Evaluation",
  "intent": "retrieval_failure_diagnosis"
}
```

---

### [FAQ]

Q. Golden Query 작성에서 가장 흔한 실수는 뭐야?

A. 문서 제목을 그대로 Query로 사용하는 것이다.

Q. Expected Document만 있으면 충분해?

A. 아니다. Expected Section, Expected Answer Keyword, Intent도 필요하다.

Q. Basic Query만 있으면 왜 부족해?

A. 실제 사용자의 모호한 질문과 복합 질문을 평가하지 못하기 때문이다.

Q. 실패 Query를 버리면 왜 문제야?

A. 같은 실패가 반복되는지 확인할 수 없다.

Q. Retest를 다른 Query로 해도 돼?

A. 안 된다. 같은 Query로 비교해야 개선 효과를 정확히 확인할 수 있다.

---

# Retrieval Queries

### [FAQ]

Q. Golden Query가 뭐야?
A. RAG 검색 품질과 답변 품질을 평가하기 위해 미리 정의한 기준 질문이다.

Q. Golden Query는 왜 필요해?
A. RAG 품질을 감이 아니라 고정된 기준 질문으로 반복 평가하기 위해 필요하다.

Q. Golden Query는 어떻게 만들어?
A. 실제 사용자 질문 형태로 만들고 Expected Document, Expected Section, Expected Answer Keyword, Intent를 연결한다.

Q. Golden Query에 필요한 필드는 뭐야?
A. Query, Expected Document, Expected Section, Expected Chunk, Expected Answer Keyword, Difficulty, Domain, Intent가 필요하다.

Q. Expected Document는 뭐야?
A. 특정 Query에 대해 검색되어야 하는 기준 문서다.

Q. Expected Section은 뭐야?
A. 기대 문서 내부에서 검색되어야 하는 구체적인 Section이다.

Q. Expected Chunk는 뭐야?
A. 답변 근거가 되는 최소 Chunk다.

Q. Expected Answer Keyword는 뭐야?
A. Generated Answer에 포함되어야 하는 핵심 키워드 목록이다.

Q. Expected Answer Pattern은 뭐야?
A. Query 유형별로 답변이 가져야 하는 구조다.

Q. User-like Query는 뭐야?
A. 실제 사용자가 입력할 법한 자연스러운 질문이다.

Q. 문서 제목 그대로 Query를 만들면 왜 부족해?
A. 실제 사용자는 문서 제목이 아니라 문제 상황이나 자연어로 질문하기 때문이다.

Q. 구어체 질문도 Golden Query에 넣어?
A. 넣는 것이 좋다. 실제 사용 환경에 가까운 평가가 가능하다.

Q. 같은 의도의 Query를 여러 개 만들어야 해?
A. 권장한다. 표현 변형에 대한 Retrieval 안정성을 확인할 수 있다.

Q. Golden Query 난이도는 왜 나눠?
A. 쉬운 질문만 평가하면 실제 사용자 질문에 대한 검색 품질을 알기 어렵기 때문이다.

Q. Basic Query는 뭐야?
A. 단일 개념을 묻는 쉬운 질문이다.

Q. Intermediate Query는 뭐야?
A. 비교나 문제 해결이 필요한 중간 난이도 질문이다.

Q. Advanced Query는 뭐야?
A. 여러 개념이나 여러 문서를 함께 참조해야 하는 복합 질문이다.

Q. Ambiguous Query는 뭐야?
A. 짧고 의도가 불명확한 모호한 질문이다.

Q. Failure-based Query는 뭐야?
A. 실제 검색 실패나 답변 실패 사례를 기준으로 만든 Golden Query다.

Q. Intent는 뭐야?
A. 사용자 Query의 목적이나 의도다.

Q. Intent가 왜 필요해?
A. 검색 평가, 답변 관련도 평가, Agent Routing, Query Rewrite에 사용되기 때문이다.

Q. Intent가 틀리면 어떤 문제가 생겨?
A. 잘못된 문서를 검색하거나 질문과 맞지 않는 답변을 생성할 수 있다.

Q. Expected Answer Keyword는 왜 필요해?
A. 답변이 필요한 핵심 내용을 포함했는지 평가하기 위해 필요하다.

Q. Expected Answer Pattern은 왜 필요해?
A. 답변이 질문 유형에 맞는 구조를 갖는지 평가하기 위해 필요하다.

Q. 문제 해결 질문은 어떤 답변 구조가 좋아?
A. 증상, 원인, 해결 순서가 좋다.

Q. 비교 질문은 어떤 답변 구조가 좋아?
A. 비교 대상의 정의와 차이점을 함께 제시해야 한다.

Q. 오해 교정 질문은 어떻게 답해야 해?
A. 잘못된 전제를 먼저 부정하고 조건부 기준을 설명해야 한다.

Q. RAG Test Dataset은 뭐야?
A. 여러 Golden Query를 모아 RAG 품질을 반복 평가할 수 있도록 만든 기준 데이터셋이다.

Q. Test Dataset은 왜 필요해?
A. 개선 전후 검색 품질과 답변 품질을 같은 기준으로 비교하기 위해 필요하다.

Q. Dataset은 Domain별로 나눠야 해?
A. 권장한다. Domain별 검색 품질과 Agent Routing 품질을 따로 평가할 수 있다.

Q. Golden Query는 몇 개가 적당해?
A. 초기 검수는 20~30개, Domain 평가는 50개 이상이 좋다.

Q. Query 수가 많으면 무조건 좋아?
A. 아니다. Intent와 Difficulty 균형이 더 중요하다.

Q. Smoke Test는 뭐야?
A. 5~10개 Query로 기본 검색 동작을 빠르게 확인하는 테스트다.

Q. Regression Test는 뭐야?
A. 문서 수정 후 기존 품질이 깨지지 않았는지 확인하는 회귀 테스트다.

Q. Dataset Versioning은 뭐야?
A. RAG Test Dataset의 변경 이력을 관리하는 방식이다.

Q. Dataset Version을 왜 기록해?
A. Dataset이 바뀌면 평가 결과도 달라지기 때문이다.

Q. Query를 추가하면 Version을 올려야 해?
A. 올리는 것이 좋다. 평가 기준이 바뀌었기 때문이다.

Q. 서로 다른 Dataset Version 결과를 직접 비교해도 돼?
A. 주의해야 한다. Query 구성이 다르면 결과가 달라질 수 있다.

Q. Failure-based Golden Query는 뭐야?
A. 실제 실패 사례를 기준으로 만든 평가 Query다.

Q. 실패 Query를 왜 Dataset에 추가해?
A. 같은 문제가 다시 발생하는지 회귀 테스트하기 위해서다.

Q. Failure Query Retest는 뭐야?
A. 실패 Query를 기준으로 수정 전후 검색 품질을 다시 평가하는 과정이다.

Q. Retest는 왜 같은 Query로 해야 해?
A. 같은 조건에서 개선 효과를 비교해야 하기 때문이다.

Q. 문서 수정 후 Retest 전에 무엇을 해야 해?
A. Reindex를 수행해야 한다.

Q. Golden Query 품질은 어떻게 검수해?
A. 사용자형 질문인지, Expected Document와 Expected Answer가 명확한지 확인한다.

Q. 나쁜 Golden Query는 어떤 Query야?
A. 문서 제목만 반복하거나 기대 문서와 답변 기준이 없는 Query다.

Q. Test Dataset 품질은 어떻게 검수해?
A. Domain, Version, Query Count, 난이도, Intent, Expected Document, Expected Answer Keyword를 확인한다.

Q. Golden Query 작성에서 가장 흔한 실수는?
A. 문서 제목을 그대로 Query로 사용하는 것이다.

Q. 실패 Query를 버리면 왜 문제야?
A. 같은 실패가 반복되는지 확인할 수 없다.

Q. Golden Query 개선 후 무엇을 해야 해?
A. Dataset Version을 갱신하고 같은 Query로 평가 결과를 다시 기록한다.
