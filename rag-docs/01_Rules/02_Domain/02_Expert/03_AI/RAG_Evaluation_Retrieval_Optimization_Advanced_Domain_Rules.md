# RAG Evaluation & Retrieval Optimization Advanced Domain Rules

---

# 1. Domain Purpose

## 1.1 RAG Evaluation & Retrieval Optimization Advanced 문서 목적

### [개념]

RAG Evaluation & Retrieval Optimization Advanced Domain 문서는 AI Agent / AI/ML Agent / PM Agent / Backend Agent / Review Agent / Architecture Review Agent가 RAG 시스템의 검색 품질, 답변 근거성, Retrieval Pipeline, Chunk 전략, Embedding 품질, Re-Ranking 품질, Evaluation Metric을 설계, 검토, 개선할 때 참조하는 RAG 제작 규칙 문서이다.

RAG Evaluation은 RAG 시스템이 “답변을 잘하는지”만 보는 것이 아니다.

RAG Evaluation은 Query가 적절히 해석되었는지, 필요한 문서가 검색되었는지, 검색된 Context가 답변에 사용되었는지, 답변이 근거에 충실한지, 검색 실패 원인이 무엇인지 평가하는 구조이다.

Retrieval Optimization은 단순히 Top-K를 늘리는 작업이 아니다.

Retrieval Optimization은 Chunking, Embedding, Query Rewrite, Hybrid Search, Metadata Filtering, Re-Ranking, Context Selection, Evaluation Feedback을 반복 개선하는 과정이다.

---

### [핵심]

- RAG Evaluation = Retrieval 평가 + Context 평가 + Answer 평가
- Retrieval Optimization = 검색 품질 개선 + Context 품질 개선
- 검색 결과와 최종 답변을 분리해서 평가
- Retrieval Precision / Recall 평가 필요
- Context Relevance 평가 필요
- Groundedness / Faithfulness 평가 필요
- Hallucination 감지 필요
- Query Rewrite / Query Expansion 기준 필요
- Hybrid Search 기준 필요
- Re-Ranking 기준 필요
- Chunking Strategy 평가 필요
- Embedding Model 평가 필요
- Retrieval Failure 분석 필요
- Evaluation Dataset 필요
- RAGOps / AI Observability와 연결 가능

---

### [실무]

2026 실무 기준 RAG Evaluation & Retrieval Optimization 문서는 다음 목적을 우선한다.

- RAG Evaluation Dataset 설계
- Retrieval Metric 정의
- Answer Quality Metric 정의
- Groundedness 평가 기준 제공
- Faithfulness 평가 기준 제공
- Hallucination 감지 기준 제공
- Chunking Strategy 평가 기준 제공
- Embedding Model 비교 기준 제공
- Query Rewrite / Query Expansion 기준 제공
- Hybrid Search 최적화 기준 제공
- Re-Ranking 최적화 기준 제공
- Context Selection 최적화 기준 제공
- Retrieval Failure 분석 기준 제공
- RAG 개선 Loop 설계 기준 제공

이 문서는 사람이 검색 이론을 공부하기 위한 문서가 아니라, Agent가 RAG 시스템의 검색 실패 원인을 찾고 개선할 수 있도록 돕는 운영 지식 문서로 작성한다.

---

### [FAQ]

Q. RAG Evaluation & Retrieval Optimization 문서는 무엇을 위한 문서인가?

A. Agent가 RAG 검색 품질, Context 품질, 답변 근거성, Hallucination, Retrieval 실패 원인을 평가하고 개선할 수 있도록 기준을 제공하는 문서이다.

Q. RAG Evaluation은 답변만 평가하면 되는가?

A. 아니다. Query, Retrieval, Context Selection, Answer Grounding, Citation, Failure 원인을 함께 평가해야 한다.

Q. Retrieval Optimization은 Top-K를 늘리는 것인가?

A. 아니다. Chunking, Embedding, Query Rewrite, Hybrid Search, Re-Ranking, Context Selection을 함께 개선하는 과정이다.

---

# 2. Scope

## 2.1 포함 범위

### [개념]

RAG Evaluation & Retrieval Optimization Domain 문서는 RAG Pipeline의 검색 품질과 답변 품질을 측정하고 개선하기 위한 Metric, Dataset, Pipeline, 최적화 전략, 장애 대응 기준을 포함한다.

---

### [핵심]

포함 범위:

- RAG Evaluation
- Retrieval Evaluation
- Answer Evaluation
- Evaluation Dataset
- Golden Dataset
- Query Set
- Expected Context
- Expected Answer
- Retrieval Precision
- Retrieval Recall
- Hit Rate
- MRR
- NDCG
- Context Relevance
- Groundedness
- Faithfulness
- Hallucination Rate
- Citation Accuracy
- Answer Completeness
- Chunking Evaluation
- Embedding Evaluation
- Query Rewrite
- Query Expansion
- Hybrid Search
- Metadata Filtering
- Re-Ranking
- Context Selection
- Context Compression
- Failure Analysis
- Feedback Loop
- RAGOps
- AI Observability

제외 범위:

- Vector Database 설치법 전체
- 특정 Embedding Model 논문 상세
- 검색 엔진 내부 수학 이론 상세
- LLM 내부 구조 상세
- 특정 SaaS Evaluation 도구 API 전체 복붙
- 단순 벤치마크 점수 나열
- 근거 없는 모델 순위 추천
- 일반 검색엔진 SEO 문서
- 사용자 질의와 무관한 통계 이론 장문 설명

---

### [실무]

RAG Evaluation & Retrieval Optimization 문서는 아래 질문에 답할 수 있어야 한다.

- RAG가 필요한 문서를 검색했는가?
- 검색된 Chunk가 질문과 관련 있는가?
- 검색 결과 중 실제 답변에 사용된 Context는 무엇인가?
- 답변이 검색 근거에 기반했는가?
- 문서에 없는 내용을 생성했는가?
- Chunk Size와 Overlap이 적절한가?
- Embedding Model 변경 후 검색 품질이 좋아졌는가?
- Hybrid Search가 필요한 상황인가?
- Re-Ranking이 검색 노이즈를 줄였는가?
- 검색 실패 원인이 Query 문제인가, Chunk 문제인가, Embedding 문제인가?
- RAG 개선 후 실제 답변 품질이 향상되었는가?

---

### [FAQ]

Q. RAG Evaluation 문서에 Metric만 나열하면 되는가?

A. 아니다. Metric 정의, 사용 상황, 실패 원인 분석, 개선 Action을 함께 작성해야 한다.

Q. Retrieval Optimization은 Vector DB 튜닝과 같은가?

A. 아니다. Vector DB 튜닝은 일부이고, Query, Chunk, Embedding, Re-Ranking, Context Selection까지 포함한다.

Q. RAG Evaluation은 AI Observability와 연결되는가?

A. 연결된다. Retrieval Trace, Context Trace, Groundedness Metric, Hallucination Trace가 필요하다.

---

# 3. Section Priority

## 3.1 필수 섹션 규칙

### [개념]

RAG Evaluation & Retrieval Optimization 문서는 모든 주요 Chunk에 `[개념]`, `[핵심]`, `[실무]`, `[FAQ]`를 우선 적용한다.

Metric이 필요한 주제는 `[Evaluation]`, `[Metric]`을 추가한다.

검색 개선이 필요한 주제는 `[Optimization]`, `[Checklist]`를 추가한다.

실패 분석이 필요한 주제는 `[Troubleshooting]`을 추가한다.

방식 비교가 필요한 주제는 `[Comparison]`을 추가한다.

---

### [핵심]

Required:

- [개념]
- [핵심]
- [실무]
- [FAQ]

Strongly Recommended:

- [Flow]
- [예제]
- [주의]
- [Best Practice]
- [Checklist]
- [Evaluation]
- [Metric]
- [Troubleshooting]
- [Comparison]

Optional:

- [Optimization]
- [Failure Analysis]
- [Evaluation Dataset]
- [Retrieval Trace]
- [Review Point]
- [Anti-Pattern]

---

### [실무]

RAG Evaluation & Retrieval Optimization 문서는 단순 개념 설명보다 평가 기준과 개선 기준을 우선한다.

각 문서는 아래 정보 중 최소 2개 이상을 포함한다.

- Evaluation Dataset 기준
- Retrieval Metric 기준
- Answer Metric 기준
- Chunking 평가 기준
- Embedding 평가 기준
- Query Rewrite 기준
- Hybrid Search 기준
- Re-Ranking 기준
- Failure Analysis 기준
- 개선 Loop 기준

---

### [FAQ]

Q. RAG Evaluation 문서에 Metric 섹션이 필요한가?

A. 필요하다. Retrieval, Context, Answer 품질을 수치 또는 기준으로 평가해야 개선 여부를 판단할 수 있다.

Q. Optimization 섹션은 왜 필요한가?

A. Evaluation 결과를 실제 Chunk, Query, Embedding, Re-Ranking 개선으로 연결해야 하기 때문이다.

Q. Troubleshooting 섹션이 필요한 이유는?

A. RAG 품질 저하는 검색 실패, Context 누락, 문서 구조 문제, Embedding 문제 등 원인이 다양하기 때문이다.

---

# 4. Core Concept Rules

## 4.1 RAG Evaluation 핵심 개념 작성 규칙

### [개념]

RAG Evaluation 핵심 개념은 일반 LLM Evaluation과 구분되도록 작성한다.

RAG Evaluation은 모델 답변만 평가하는 것이 아니라, Retrieval 단계와 Answer 단계의 연결 품질을 평가한다.

---

### [핵심]

반드시 포함할 개념:

- RAG Evaluation
- Retrieval Evaluation
- Answer Evaluation
- Evaluation Dataset
- Golden Dataset
- Query Set
- Expected Context
- Expected Answer
- Retrieval Precision
- Retrieval Recall
- Hit Rate
- MRR
- NDCG
- Context Relevance
- Groundedness
- Faithfulness
- Hallucination Rate
- Citation Accuracy
- Answer Completeness
- Retrieval Failure
- Optimization Loop

용어 통일:

- RAG Evaluation
- Retrieval Evaluation
- Answer Evaluation
- Evaluation Dataset
- Golden Dataset
- Expected Context
- Expected Answer
- Context Relevance
- Groundedness
- Faithfulness
- Hallucination Rate
- Retrieval Optimization

---

### [실무]

RAG Evaluation 설명은 아래 구조를 기준으로 작성한다.

```text
User Query
→ Query Processing
→ Retrieval
→ Re-Ranking
→ Context Selection
→ Answer Generation
→ Groundedness Evaluation
→ Failure Analysis
→ Retrieval Optimization
```

RAG Evaluation 문서는 “정답과 비슷한 답변인가” 수준에서 멈추면 안 된다.

Agent가 검색 단계에서 실패했는지, Context 선택에서 실패했는지, 답변 생성에서 실패했는지 분리해서 판단할 수 있어야 한다.

---

### [FAQ]

Q. RAG Evaluation의 핵심은 무엇인가?

A. 필요한 문서를 검색했는지, 검색 Context가 답변에 사용되었는지, 답변이 근거에 충실한지 평가하는 것이다.

Q. RAG Evaluation과 일반 LLM Evaluation의 차이는?

A. 일반 LLM Evaluation은 답변 품질 중심이고, RAG Evaluation은 Retrieval, Context, Grounding까지 평가한다.

Q. RAG 품질 문제는 항상 LLM 문제인가?

A. 아니다. Query, Chunking, Embedding, Re-Ranking, Context Selection 문제가 원인일 수 있다.

---

# 5. Evaluation Dataset Rules

## 5.1 RAG Evaluation Dataset 작성 규칙

### [개념]

Evaluation Dataset은 RAG 시스템의 검색 품질과 답변 품질을 일관되게 평가하기 위한 Query, Expected Context, Expected Answer, Metadata의 집합이다.

RAG Evaluation Dataset이 없으면 개선 전후 품질을 신뢰성 있게 비교하기 어렵다.

---

### [핵심]

Evaluation Dataset 구성 요소:

- queryId
- userQuery
- queryType
- domain
- expectedContext
- expectedSourceDocument
- expectedChunkId
- expectedAnswer
- difficulty
- requiredEvidence
- negativeContext
- metadata
- evaluationCriteria

Query 유형:

- Concept Query
- Practical Query
- Code Query
- Troubleshooting Query
- Comparison Query
- FAQ Query
- Multi-Hop Query
- No-Answer Query
- Latest-Version Query
- Format-Sensitive Query

---

### [실무]

Evaluation Dataset 예시:

```json
{
  "queryId": "RAG-EVAL-001",
  "userQuery": "JWT 인증 흐름은 어떻게 동작해?",
  "queryType": "Concept Query",
  "domain": "Security",
  "expectedSourceDocument": "Security_Advanced_Part04_JWT.md",
  "expectedContext": [
    "Access Token",
    "JwtAuthenticationFilter",
    "SecurityContext"
  ],
  "expectedAnswer": "JWT 인증은 Access Token 검증 후 SecurityContext에 Authentication을 저장하는 흐름이다.",
  "evaluationCriteria": ["retrievalHit", "groundedness", "answerCompleteness"]
}
```

Evaluation Dataset은 실제 사용자 Query와 Agent 내부 Query를 모두 반영한다.

문서 제작용 RAG에서는 FAQ Query와 Retrieval Queries 기반 Query를 반드시 포함한다.

---

### [FAQ]

Q. RAG Evaluation Dataset은 왜 필요한가?

A. RAG 개선 전후 검색 품질과 답변 품질을 일관되게 비교하기 위해 필요하다.

Q. Expected Context는 무엇인가?

A. 특정 Query에 답하기 위해 검색되어야 하는 핵심 Chunk, 문서, 개념, Evidence이다.

Q. No-Answer Query도 필요한가?

A. 필요하다. 문서에 없는 내용을 모델이 단정하지 않는지 평가하기 위해 사용한다.

---

# 6. Retrieval Metric Rules

## 6.1 Retrieval Metric 작성 규칙

### [개념]

Retrieval Metric은 RAG 시스템이 사용자 Query에 필요한 문서나 Chunk를 제대로 검색했는지 평가하는 기준이다.

Retrieval Metric은 답변 생성 전 검색 단계 품질을 평가한다.

---

### [핵심]

대표 Retrieval Metric:

- Hit Rate
- Recall@K
- Precision@K
- MRR
- NDCG
- MAP
- Context Relevance
- Missing Context Rate
- Duplicate Context Rate
- Noise Context Rate

Metric 의미:

- Hit Rate: 필요한 문서가 검색 결과에 포함되었는가
- Recall@K: 필요한 문서 중 Top-K에 포함된 비율
- Precision@K: Top-K 검색 결과 중 관련 문서 비율
- MRR: 정답 문서가 얼마나 상위에 등장하는가
- NDCG: 검색 순위 품질
- Missing Context Rate: 필요한 Context 누락 비율
- Noise Context Rate: 관련 없는 Context 비율

---

### [실무]

Retrieval Metric 선택 기준:

```text
단순 검색 성공 여부:
- Hit Rate

필요 문서 누락 확인:
- Recall@K

검색 결과 노이즈 확인:
- Precision@K

정답 Chunk 순위 확인:
- MRR
- NDCG

Context 품질 확인:
- Context Relevance
- Noise Context Rate
```

RAG 문서 검색에서는 Recall@K와 Context Relevance를 함께 본다.

정답 Chunk를 찾았지만 관련 없는 Chunk가 너무 많으면 Answer 품질이 낮아질 수 있다.

---

### [FAQ]

Q. Hit Rate는 무엇인가?

A. 필요한 문서나 Chunk가 검색 결과 안에 포함되었는지 평가하는 Metric이다.

Q. Recall@K와 Precision@K의 차이는?

A. Recall@K는 필요한 문서를 얼마나 찾았는지, Precision@K는 검색 결과 중 관련 문서 비율이 얼마나 높은지 평가한다.

Q. MRR은 왜 필요한가?

A. 정답 Chunk가 검색 결과 상위에 등장하는지 평가하기 위해 필요하다.

---

# 7. Answer Evaluation Rules

## 7.1 RAG Answer 평가 규칙

### [개념]

Answer Evaluation은 RAG 시스템의 최종 답변이 사용자 질문을 충족하고 검색된 Context에 근거하는지 평가하는 과정이다.

RAG 답변 평가는 답변 품질과 근거성을 함께 평가해야 한다.

---

### [핵심]

Answer Evaluation 항목:

- Groundedness
- Faithfulness
- Answer Completeness
- Answer Relevance
- Citation Accuracy
- Hallucination Rate
- Format Compliance
- Instruction Following
- Source Coverage
- No-Answer Handling
- Conciseness
- Practical Usefulness

평가 기준:

- 답변이 질문에 직접 답하는가
- 답변이 검색 Context와 일치하는가
- 필요한 Evidence가 포함되었는가
- 문서에 없는 내용을 생성하지 않았는가
- 출처가 실제 내용을 지지하는가
- 출력 형식을 지켰는가

---

### [실무]

Answer Evaluation Checklist:

```md
### [Checklist]

- 사용자 질문에 직접 답했는가?
- 검색된 Context를 실제로 사용했는가?
- 핵심 주장마다 근거가 있는가?
- 문서에 없는 내용을 단정하지 않았는가?
- 답변이 너무 일반적이지 않은가?
- 필요한 예제나 실무 기준이 포함되었는가?
- Citation 또는 Source가 답변을 지지하는가?
- 출력 형식을 지켰는가?
```

RAG 답변 평가는 LLM 응답만 보지 않는다.

검색된 Context와 최종 답변을 비교해야 한다.

---

### [FAQ]

Q. Answer Evaluation은 무엇을 평가하는가?

A. 최종 답변이 질문에 적절히 답하고, 검색된 Context에 근거하며, 문서에 없는 내용을 생성하지 않았는지 평가한다.

Q. Groundedness와 Faithfulness는 왜 중요한가?

A. RAG 답변은 검색된 근거에 기반해야 하므로 답변과 Context의 일치성이 중요하다.

Q. Format Compliance도 평가해야 하는가?

A. 해야 한다. RAG 문서 생성, 코드 생성, Agent Output에서는 출력 형식 준수가 품질의 일부이다.

---

# 8. Groundedness and Faithfulness Rules

## 8.1 Groundedness / Faithfulness 평가 규칙

### [개념]

Groundedness는 답변이 제공된 문서, Chunk, Tool Result, 사용자 입력 같은 근거에 기반하는 정도이다.

Faithfulness는 답변이 제공된 Context를 왜곡하지 않고 충실하게 반영하는 정도이다.

RAG Evaluation에서는 Groundedness와 Faithfulness를 핵심 Metric으로 다룬다.

---

### [핵심]

Groundedness 평가 대상:

- 핵심 주장
- 숫자 / 날짜 / 버전
- 코드 설명
- 기술 선택 기준
- 문제 원인
- 해결 방법
- Citation
- Source 연결

Faithfulness 실패 유형:

- Context에 없는 내용 생성
- Context 내용 왜곡
- 여러 Source 내용 잘못 결합
- 조건부 내용을 확정적으로 표현
- 오래된 Context를 최신 사실처럼 표현
- Tool Result와 다른 결론 생성

---

### [실무]

Groundedness Evaluation Flow:

```text
Answer
→ Claim Extraction
→ Evidence Matching
→ Source Verification
→ Conflict Detection
→ Groundedness Score
→ Pass / Fail
```

Faithfulness Checklist:

```md
### [Checklist]

- 답변의 핵심 주장마다 Evidence가 있는가?
- Evidence가 실제로 해당 주장을 지지하는가?
- Context 내용을 과장하거나 왜곡하지 않았는가?
- 여러 문서의 내용을 잘못 연결하지 않았는가?
- 불확실한 내용은 불확실하게 표현했는가?
```

Groundedness가 낮으면 Retrieval, Context Selection, Prompt, Answer Synthesis를 함께 점검한다.

---

### [FAQ]

Q. Groundedness란?

A. 답변이 검색된 문서나 Tool Result 같은 근거에 기반하는 정도이다.

Q. Faithfulness란?

A. 답변이 제공된 Context를 왜곡하지 않고 충실히 반영하는 정도이다.

Q. Groundedness가 낮으면 무엇을 확인해야 하는가?

A. Retrieval 결과, Context Selection, Prompt 지시, Answer Synthesis, Citation 연결을 확인해야 한다.

---

# 9. Hallucination Evaluation Rules

## 9.1 Hallucination 평가 규칙

### [개념]

Hallucination Evaluation은 RAG 답변이 문서에 없는 내용, 근거 없는 주장, 잘못된 코드, 존재하지 않는 API, 잘못된 출처를 생성했는지 평가하는 과정이다.

RAG 시스템은 문서 근거가 있어야 하므로 Hallucination 감지가 필수이다.

---

### [핵심]

Hallucination 유형:

- Source 없는 주장
- Context와 불일치
- 존재하지 않는 파일 / 클래스 / API 생성
- 문서에 없는 정책 생성
- 잘못된 숫자 / 날짜 / 버전 생성
- 검색 결과와 다른 결론
- Tool Result 왜곡
- No-Answer Query에 답변 생성
- Memory 기반 과잉 추론

감지 기준:

- Claim과 Evidence 비교
- Source Document 확인
- Tool Result 비교
- No-Answer Query 평가
- Review Agent 검증
- User Feedback 반영

---

### [실무]

Hallucination Checklist:

```md
### [Checklist]

- 답변에 문서 근거 없는 주장이 있는가?
- 존재하지 않는 코드나 API를 생성했는가?
- 검색 Context와 반대되는 내용을 말했는가?
- Tool Result와 다른 결론을 냈는가?
- 모르는 내용을 확정적으로 답했는가?
- No-Answer Query에서 답변을 만들어냈는가?
```

Hallucination이 발견되면 단순히 모델을 교체하지 않는다.

먼저 Retrieval 실패, Context 누락, Prompt 문제, Memory 충돌, Evaluation Dataset 부족을 확인한다.

---

### [FAQ]

Q. RAG에서 Hallucination은 무엇인가?

A. 검색 문서나 제공된 Context에 없는 내용을 사실처럼 생성하는 현상이다.

Q. No-Answer Query는 왜 필요한가?

A. 문서에 없는 질문에 대해 모델이 모른다고 답하는지 평가하기 위해 필요하다.

Q. Hallucination이 발생하면 바로 Fine-Tuning해야 하는가?

A. 아니다. Retrieval, Context, Prompt, Grounding, Evaluation 기준을 먼저 점검해야 한다.

---

# 10. Chunking Evaluation Rules

## 10.1 Chunking Strategy 평가 규칙

### [개념]

Chunking Evaluation은 문서를 어떤 단위로 나누었을 때 Retrieval 품질과 Answer 품질이 좋아지는지 평가하는 과정이다.

Chunk 품질은 RAG 성능의 핵심이다.

---

### [핵심]

Chunking 평가 대상:

- Chunk Size
- Chunk Overlap
- Heading Preservation
- Semantic Boundary
- Code Block Preservation
- Table Preservation
- FAQ Preservation
- Metadata Preservation
- Cross-Chunk Dependency
- Duplicate Chunk
- Too Small Chunk
- Too Large Chunk

좋은 Chunk 조건:

- 하나의 핵심 개념 포함
- 독립 검색 가능
- 제목과 Section 유지
- FAQ 포함 가능
- 코드 예제 잘림 없음
- Context로 넣었을 때 의미 유지
- Metadata로 Source 추적 가능

---

### [실무]

Chunking Evaluation Checklist:

```md
### [Checklist]

- Chunk 하나가 독립적으로 의미를 가지는가?
- 제목과 Section 정보가 유지되는가?
- 코드블록이 중간에 잘리지 않는가?
- FAQ의 Q와 A가 분리되지 않았는가?
- 하나의 Chunk에 너무 많은 개념이 섞이지 않았는가?
- Chunk가 너무 작아 의미가 부족하지 않은가?
- Metadata에 문서명, Section, Part 정보가 포함되었는가?
```

RAG 문서 제작에서는 Markdown Header 기반 Chunking이 유리하다.

Domain Rules 문서는 Section 구조와 FAQ 구조를 유지해야 한다.

---

### [FAQ]

Q. Chunking Evaluation은 왜 필요한가?

A. Chunk가 너무 크거나 작거나 의미 단위가 깨지면 Retrieval 품질과 답변 품질이 낮아지기 때문이다.

Q. 좋은 Chunk의 기준은?

A. 하나의 핵심 개념을 담고, 독립 검색 가능하며, 제목과 근거가 유지되는 Chunk이다.

Q. FAQ의 Q와 A가 분리되면 왜 문제인가?

A. Query Matching은 되지만 답변 근거가 누락되어 Retrieval 품질이 떨어질 수 있다.

---

# 11. Embedding Evaluation Rules

## 11.1 Embedding Model 평가 규칙

### [개념]

Embedding Evaluation은 Query와 Document Chunk를 Vector로 변환하는 Embedding Model이 실제 RAG 검색에 적합한지 평가하는 과정이다.

Embedding Model 품질은 Retrieval 품질에 직접 영향을 준다.

---

### [핵심]

Embedding Evaluation 대상:

- Semantic Similarity 품질
- Keyword Matching 보완 필요성
- 한국어 Query 품질
- 영어 / 한글 혼합 Query 품질
- 코드 검색 품질
- 명령어 검색 품질
- FAQ 검색 품질
- Domain 용어 검색 품질
- 긴 Chunk 검색 품질
- 짧은 Query 검색 품질
- Near-Duplicate 구분 능력
- Vector Dimension
- Index Compatibility

평가 Metric:

- Recall@K
- Precision@K
- MRR
- NDCG
- Context Relevance
- Retrieval Hit Rate

---

### [실무]

Embedding Evaluation Checklist:

```md
### [Checklist]

- 한국어 Query에서 핵심 문서가 검색되는가?
- Domain 용어가 포함된 Query에서 정확도가 높은가?
- 코드 / 명령어 Query를 잘 찾는가?
- FAQ Query와 Q/A Chunk가 잘 매칭되는가?
- 비슷하지만 다른 개념을 구분하는가?
- Vector Index와 Distance Metric이 적절한가?
- 기존 Embedding Model 대비 Recall@K가 개선되었는가?
```

Embedding Model은 벤치마크 점수보다 실제 RAG Dataset으로 평가한다.

RAG 문서가 한국어 중심이면 한국어 Query Evaluation Set이 반드시 필요하다.

---

### [FAQ]

Q. Embedding Evaluation은 왜 필요한가?

A. Embedding Model이 Query와 문서 Chunk를 잘 연결하지 못하면 RAG가 필요한 근거를 찾지 못하기 때문이다.

Q. Embedding Model은 벤치마크 점수만 보고 선택해도 되는가?

A. 아니다. 실제 문서, 실제 Query, 실제 Domain 용어로 평가해야 한다.

Q. 코드 검색에는 Semantic Search만으로 충분한가?

A. 부족할 수 있다. 코드, 명령어, 설정값은 Keyword Search나 Hybrid Search가 필요할 수 있다.

---

# 12. Query Optimization Rules

## 12.1 Query Rewrite / Query Expansion 규칙

### [개념]

Query Optimization은 사용자 질문을 Retrieval에 적합한 검색 Query로 변환하거나 확장하는 과정이다.

RAG 검색 실패는 사용자 질문이 문서 용어와 맞지 않아서 발생할 수 있다.

---

### [핵심]

Query Optimization 방식:

- Query Rewrite
- Query Expansion
- Keyword Extraction
- Domain Term Mapping
- Synonym Expansion
- HyDE
- Multi-Query Retrieval
- Metadata Query 생성
- Verification Query 생성
- No-Answer Check Query 생성

Query 유형:

- Precision Query
- Recall Query
- Semantic Query
- Keyword Query
- Metadata Query
- Troubleshooting Query
- Verification Query
- Follow-up Query

---

### [실무]

Query Optimization 예시:

```text
User Query:
로그인이 안 돼

Query Rewrite:
- Spring Security Login Failure
- JWT Authentication Error
- SecurityFilterChain 인증 실패
- Login API Troubleshooting
- AuthController Login Error

Search Strategy:
- Keyword Search: error message
- Semantic Search: authentication failure
- Troubleshooting Search: login failure checklist
```

복잡한 질문은 하나의 Query로 검색하지 않는다.

Agent는 Precision Query와 Recall Query를 함께 생성해야 한다.

---

### [FAQ]

Q. Query Rewrite는 언제 필요한가?

A. 사용자 질문이 모호하거나 문서 용어와 다르거나 첫 검색 결과가 부족할 때 필요하다.

Q. Query Expansion은 무엇인가?

A. 원래 Query에 관련 Domain 용어, 동의어, 하위 개념을 추가해 검색 범위를 넓히는 것이다.

Q. Multi-Query Retrieval은 왜 필요한가?

A. 복합 질문은 하나의 Query로 필요한 모든 Chunk를 찾기 어렵기 때문이다.

---

# 13. Hybrid Search Rules

## 13.1 Hybrid Search 최적화 규칙

### [개념]

Hybrid Search는 Semantic Search, Keyword Search, Metadata Filtering, Graph Search, Re-Ranking을 함께 사용하는 검색 전략이다.

RAG 시스템은 하나의 검색 방식만으로 모든 Query를 처리하기 어렵다.

---

### [핵심]

검색 방식별 사용 기준:

- Semantic Search: 개념, 설명, 유사 의미 검색
- Keyword Search: 코드, 명령어, 에러 메시지, 설정값 검색
- Metadata Search: Domain, Version, Part, 문서 유형 필터
- Graph Search: Entity, Relation, Multi-Hop 관계 검색
- Re-Ranking: 검색 결과 정렬과 노이즈 제거

Hybrid Search 적합 상황:

- 코드와 개념이 섞인 질문
- 에러 메시지 기반 Troubleshooting
- 특정 문서 Part 검색
- 최신 Version 필터 필요
- Entity 관계 검색 필요
- Semantic Search 결과가 너무 넓음
- Keyword Search 결과가 너무 좁음

---

### [실무]

Hybrid Search Flow:

```text
User Query
→ Query Classification
→ Semantic Search
→ Keyword Search
→ Metadata Filtering
→ Optional Graph Search
→ Result Merge
→ Re-Ranking
→ Context Selection
```

검색 전략 예시:

```text
질문:
Docker 컨테이너 권한 오류 해결 방법?

Hybrid Search:
1. Keyword Search: Permission Denied
2. Semantic Search: Docker volume permission troubleshooting
3. Metadata Filter: Docker Domain
4. Troubleshooting Chunk 우선
5. Re-Ranking
```

---

### [FAQ]

Q. Hybrid Search는 왜 필요한가?

A. 개념 질문, 코드 질문, 에러 질문, 설정 질문은 서로 다른 검색 방식이 강하기 때문이다.

Q. Keyword Search는 언제 중요한가?

A. 에러 메시지, 코드, 명령어, 설정값, 파일명, 클래스명처럼 정확한 문자열이 중요한 경우 필요하다.

Q. Metadata Filtering은 왜 사용하는가?

A. Domain, Version, 문서 유형을 제한해 관련 없는 검색 결과를 줄이기 위해 사용한다.

---

# 14. Re-Ranking Rules

## 14.1 Re-Ranking 최적화 규칙

### [개념]

Re-Ranking은 1차 검색 결과를 Query와의 관련성, 근거성, 품질 기준에 따라 다시 정렬하는 과정이다.

Re-Ranking은 Retrieval Noise를 줄이고 Context 품질을 높이기 위해 사용한다.

---

### [핵심]

Re-Ranking 대상:

- Semantic Search 결과
- Keyword Search 결과
- Hybrid Search 결과
- Graph Search 결과
- Multi-Query Retrieval 결과

Re-Ranking 기준:

- Query Relevance
- Context Relevance
- Source Priority
- Domain Match
- Metadata Match
- Freshness
- Section Priority
- FAQ Match
- Code Example Match
- Troubleshooting Match
- Duplicate Removal

---

### [실무]

Re-Ranking Flow:

```text
Initial Retrieval Results
→ Relevance Scoring
→ Source Priority Scoring
→ Duplicate Removal
→ Noise Filtering
→ Top Context Selection
```

Re-Ranking Checklist:

```md
### [Checklist]

- Query와 직접 관련 있는 Chunk가 상위에 있는가?
- Domain Rules가 일반 문서보다 우선되는가?
- FAQ Chunk가 질문과 매칭되는가?
- 중복 Chunk가 제거되었는가?
- 관련 없는 Chunk가 Context에 포함되지 않았는가?
- 최신 Project Progress가 우선되는가?
```

Re-Ranking은 Top-K를 크게 늘린 뒤 무조건 적용하는 방식이 아니다.

1차 검색 품질과 비용을 함께 고려한다.

---

### [FAQ]

Q. Re-Ranking은 왜 필요한가?

A. 1차 검색 결과에는 관련성이 낮은 Chunk가 섞일 수 있으므로 답변에 적합한 Context를 상위로 정렬하기 위해 필요하다.

Q. Re-Ranking은 언제 사용해야 하는가?

A. Top-K 결과에 노이즈가 많거나, Hybrid Search 결과를 통합하거나, Context 선택 품질이 낮을 때 사용한다.

Q. Re-Ranking도 비용이 드는가?

A. 든다. Re-Ranking 모델 호출이나 추가 계산 비용이 있으므로 품질 개선 효과와 비용을 함께 평가해야 한다.

---

# 15. Context Selection Rules

## 15.1 Context Selection / Compression 규칙

### [개념]

Context Selection은 검색된 Chunk 중 최종 LLM 입력에 넣을 Context를 선택하는 과정이다.

Context Compression은 선택된 Context를 의미를 유지한 채 Token Budget에 맞게 압축하는 과정이다.

---

### [핵심]

Context Selection 기준:

- Query와 직접 관련
- Expected Context 포함
- Domain Rules 우선
- Project Progress 우선
- 최신 문서 우선
- FAQ / Checklist / Troubleshooting 우선
- Code Example 보존
- 중복 제거
- 충돌 Context 감지
- Token Budget 고려

Context Compression 기준:

- 핵심 근거 유지
- Source 유지
- 조건과 예외 유지
- 숫자 / 버전 / 코드 보존
- 장문 설명 축소
- 중복 문장 제거
- 추론에 필요한 연결 관계 유지

---

### [실무]

Context Selection Flow:

```text
Retrieved Chunks
→ Re-Ranking
→ Duplicate Removal
→ Conflict Detection
→ Source Priority
→ Token Budget Check
→ Context Assembly
```

Context Selection Checklist:

```md
### [Checklist]

- 답변에 필요한 핵심 Chunk가 포함되었는가?
- 관련 없는 Chunk를 제거했는가?
- 중복 Chunk를 제거했는가?
- Domain Rules와 Project Progress가 우선되었는가?
- 코드 예제가 잘리지 않았는가?
- Context 충돌이 표시되었는가?
- Token Budget을 초과하지 않는가?
```

Context가 많다고 답변 품질이 항상 좋아지지 않는다.

관련 없는 Context는 Hallucination과 답변 혼란을 증가시킬 수 있다.

---

### [FAQ]

Q. Context Selection은 왜 중요한가?

A. 검색 결과가 좋아도 잘못된 Context를 넣으면 LLM 답변 품질이 낮아지기 때문이다.

Q. Context가 많을수록 좋은가?

A. 아니다. 관련 없는 Context가 많으면 노이즈가 증가하고 답변이 흔들릴 수 있다.

Q. Context Compression 시 무엇을 보존해야 하는가?

A. 핵심 근거, Source, 조건, 예외, 코드, 숫자, 버전을 보존해야 한다.

---

# 16. Metadata Optimization Rules

## 16.1 Metadata 기반 Retrieval 최적화 규칙

### [개념]

Metadata Optimization은 문서와 Chunk에 Domain, Part, Version, Section, Source, 작성일, 문서 유형 같은 Metadata를 부여해 Retrieval 품질을 높이는 과정이다.

Metadata가 없으면 Agent가 검색 결과의 우선순위를 판단하기 어렵다.

---

### [핵심]

권장 Metadata:

- fileName
- documentTitle
- domain
- level
- part
- section
- subsection
- documentType
- sourceType
- version
- createdAt
- updatedAt
- priority
- agentTarget
- tags
- language
- status

Metadata 사용 목적:

- Domain Filtering
- Version Filtering
- Section Filtering
- Agent별 검색 범위 제한
- 최신 문서 우선
- Domain Rules 우선
- Troubleshooting Chunk 우선
- FAQ Chunk 우선
- Deprecated 문서 제외

---

### [실무]

Metadata 예시:

```json
{
  "fileName": "Security_Advanced_Part04_JWT.md",
  "domain": "Security",
  "level": "Level1",
  "part": "Part04",
  "section": "JWT Authentication",
  "documentType": "RAG_DOC",
  "agentTarget": ["Backend Agent", "Review Agent"],
  "status": "active"
}
```

Metadata Filter 예시:

```text
질문:
JWT 인증 오류 해결

Filter:
- domain = Security
- section contains JWT
- documentType = RAG_DOC
- status = active
- sectionType = Troubleshooting
```

---

### [FAQ]

Q. Metadata Optimization은 왜 필요한가?

A. 검색 결과를 Domain, Version, Section, 문서 유형 기준으로 필터링하고 우선순위를 정하기 위해 필요하다.

Q. Metadata가 없으면 어떤 문제가 생기는가?

A. 오래된 문서, 관련 없는 Domain, 낮은 우선순위 Chunk가 검색 결과에 섞일 수 있다.

Q. Agent별 Metadata가 필요한가?

A. 필요하다. PM Agent, Backend Agent, Review Agent가 우선 검색해야 할 문서가 다르기 때문이다.

---

# 17. Retrieval Failure Analysis Rules

## 17.1 Retrieval Failure 분석 규칙

### [개념]

Retrieval Failure Analysis는 RAG가 필요한 Context를 검색하지 못했거나, 관련 없는 Context를 검색했거나, 검색 결과를 답변에 제대로 사용하지 못한 원인을 분석하는 과정이다.

RAG 최적화는 실패 원인 분류에서 시작한다.

---

### [핵심]

Failure 유형:

- No Retrieval
- Wrong Chunk Retrieved
- Relevant Chunk Missing
- Correct Chunk Ranked Low
- Too Much Noise
- Duplicate Context
- Stale Context Retrieved
- Metadata Filter Too Strict
- Metadata Filter Too Loose
- Query Rewrite Failure
- Embedding Mismatch
- Chunk Boundary Problem
- Context Selection Failure
- Answer Ignored Context

원인 분류:

- Query Problem
- Chunking Problem
- Embedding Problem
- Index Problem
- Metadata Problem
- Re-Ranking Problem
- Context Problem
- Prompt Problem
- Model Problem

---

### [실무]

Failure Analysis 형식:

```md
문제:
JWT 인증 질문에서 Security 문서가 검색되지 않음

원인:

- Query가 "로그인 안 됨"처럼 너무 모호함
- Security Domain Keyword가 Query에 없음
- Troubleshooting Chunk Metadata가 누락됨

해결:

- Query Rewrite 추가
- Security / JWT / Authentication Keyword Expansion
- Troubleshooting Metadata 보완
- Evaluation Query Set에 유사 질문 추가
```

Retrieval Failure는 “검색이 안 됨”으로만 기록하지 않는다.

원인 유형과 개선 Action을 반드시 연결한다.

---

### [FAQ]

Q. Retrieval Failure Analysis는 왜 필요한가?

A. 검색 실패 원인을 알아야 Query, Chunk, Embedding, Metadata, Re-Ranking 중 무엇을 개선할지 판단할 수 있기 때문이다.

Q. Correct Chunk Ranked Low는 무엇인가?

A. 필요한 Chunk가 검색되었지만 순위가 낮아 실제 Context에 포함되지 못하는 문제이다.

Q. Answer Ignored Context는 무엇인가?

A. 올바른 Context가 제공되었지만 LLM이 답변 생성에서 이를 사용하지 않는 문제이다.

---

# 18. Optimization Loop Rules

## 18.1 RAG Optimization Loop 작성 규칙

### [개념]

RAG Optimization Loop는 Evaluation 결과와 Failure Analysis를 기반으로 RAG Pipeline을 반복 개선하는 과정이다.

RAG 최적화는 한 번 설정하고 끝나는 작업이 아니다.

---

### [핵심]

Optimization Loop 단계:

```text
Evaluation Dataset 준비
→ Baseline 측정
→ Retrieval Trace 분석
→ Failure 유형 분류
→ 개선 대상 선택
→ Chunk / Query / Embedding / Re-Ranking 개선
→ 재평가
→ Regression Test
→ 배포
→ Monitoring
```

개선 대상:

- Chunk Size
- Chunk Overlap
- Markdown Structure
- FAQ 추가
- Retrieval Queries 추가
- Metadata 보완
- Embedding Model 변경
- Hybrid Search 적용
- Query Rewrite 적용
- Re-Ranking 적용
- Context Selection 개선
- Prompt 개선

---

### [실무]

Optimization 우선순위:

```text
1. 문서 구조와 Chunk 품질 개선
2. Evaluation Dataset 구축
3. Metadata 보완
4. Query Rewrite / Expansion 적용
5. Hybrid Search 적용
6. Re-Ranking 적용
7. Embedding Model 비교
8. Context Selection 개선
9. Answer Prompt 개선
10. 운영 Monitoring 연결
```

무작정 Embedding Model을 바꾸기 전에 문서 구조, Chunk, Query, Metadata를 먼저 점검한다.

RAG 문서 품질이 낮으면 모델 변경 효과가 제한된다.

---

### [FAQ]

Q. RAG Optimization은 무엇부터 해야 하는가?

A. Evaluation Dataset을 만들고 Baseline을 측정한 뒤 실패 원인을 분류해야 한다.

Q. Embedding Model을 바꾸면 RAG 문제가 해결되는가?

A. 항상 그렇지 않다. Chunking, Query, Metadata, Re-Ranking, Context Selection 문제가 원인일 수 있다.

Q. 최적화 후 무엇을 해야 하는가?

A. 기존 Evaluation Dataset으로 재평가하고 Regression Test를 수행해야 한다.

---

# 19. RAG Regression Rules

## 19.1 RAG Regression Test 규칙

### [개념]

RAG Regression Test는 RAG Pipeline 변경 후 기존에 잘 되던 Query와 답변 품질이 유지되는지 확인하는 테스트이다.

RAG 개선은 일부 Query 품질을 높이면서 다른 Query 품질을 떨어뜨릴 수 있다.

---

### [핵심]

Regression Test 대상:

- 기존 주요 Query
- FAQ Query
- Domain별 대표 Query
- Troubleshooting Query
- Code Query
- No-Answer Query
- Multi-Hop Query
- Format-Sensitive Query
- 이전 실패 후 수정된 Query
- 사용자 피드백 기반 Query

변경 대상:

- Chunking 변경
- Embedding Model 변경
- Vector Index 재생성
- Top-K 변경
- Re-Ranking 추가
- Metadata Filter 변경
- Query Rewrite 변경
- Prompt 변경
- Model 변경

---

### [실무]

Regression Checklist:

```md
### [Checklist]

- 기존 대표 Query의 Hit Rate가 유지되는가?
- 기존 FAQ Query가 여전히 올바른 Chunk를 찾는가?
- No-Answer Query에서 허위 답변이 증가하지 않았는가?
- Format Compliance가 유지되는가?
- Groundedness가 떨어지지 않았는가?
- 특정 Domain 검색 품질만 나빠지지 않았는가?
- Latency와 Cost가 허용 범위인가?
```

RAG Pipeline 변경은 항상 Regression Test와 함께 수행한다.

특히 Embedding Model 변경이나 Chunking 변경은 전체 Index와 검색 품질에 큰 영향을 준다.

---

### [FAQ]

Q. RAG Regression Test는 왜 필요한가?

A. RAG 최적화가 일부 Query에는 좋아도 기존 Query 품질을 떨어뜨릴 수 있기 때문이다.

Q. 어떤 변경 후 Regression Test가 필요한가?

A. Chunking, Embedding, Index, Top-K, Re-Ranking, Metadata Filter, Prompt, Model 변경 후 필요하다.

Q. Regression Test에서 가장 중요한 Query는?

A. 실제 사용자 질문, FAQ Query, Troubleshooting Query, 기존 실패 수정 Query가 중요하다.

---

# 20. RAG Observability Rules

## 20.1 RAG Evaluation 관측 규칙

### [개념]

RAG Observability는 RAG Evaluation과 Retrieval Optimization을 운영 중에도 추적하기 위한 Trace, Metric, Log 구조이다.

Evaluation은 오프라인 테스트뿐 아니라 운영 중 품질 추적과 연결되어야 한다.

---

### [핵심]

RAG Trace 대상:

- originalQuery
- rewrittenQuery
- queryType
- embeddingModel
- embeddingModelVersion
- vectorIndexVersion
- topK
- metadataFilter
- retrievedChunks
- selectedChunks
- rerankedChunks
- rejectedChunks
- contextSnapshot
- answer
- groundednessScore
- hallucinationFlag
- latency
- cost
- userFeedback

운영 Metric:

- retrievalHitRate
- contextRelevance
- missingContextRate
- groundedness
- citationAccuracy
- hallucinationRate
- noAnswerAccuracy
- retrievalLatency
- rerankingLatency
- answerLatency
- costPerQuery

---

### [실무]

RAG Trace 예시:

```text
traceId: RAG-TRACE-001
queryType: Troubleshooting Query
embeddingModel: bge-m3
vectorIndexVersion: rag-doc-v4
topK: 10
retrievedChunks: 10
selectedChunks: 4
groundednessScore: high
hallucinationFlag: false
```

RAG Observability는 Evaluation Dataset 개선에도 사용한다.

운영 실패 사례를 Evaluation Dataset에 추가해 반복 실패를 줄인다.

---

### [FAQ]

Q. RAG Observability는 왜 필요한가?

A. 운영 중 검색 품질, Context 품질, Groundedness, Hallucination, 비용, 지연을 추적하기 위해 필요하다.

Q. 운영 실패 Query는 어떻게 활용해야 하는가?

A. Failure Analysis 후 Evaluation Dataset에 추가하고 Regression Test에 포함한다.

Q. retrievedChunks와 selectedChunks를 모두 기록해야 하는가?

A. 기록해야 한다. 검색 결과와 실제 LLM 입력 Context를 분리해서 분석하기 위해 필요하다.

---

# 21. Common Mistakes

## 21.1 자주 발생하는 작성 오류

### [개념]

RAG Evaluation & Retrieval Optimization 문서는 “검색 성능을 높이는 방법”만 설명하는 문서가 아니다.

Agent가 Query, Chunk, Embedding, Retrieval, Context, Answer, Grounding, Failure 원인을 분리해서 평가하고 개선할 수 있도록 작성해야 한다.

---

### [핵심]

금지 또는 주의:

- 답변 품질만 평가
- Retrieval Metric 누락
- Evaluation Dataset 누락
- Expected Context 누락
- No-Answer Query 누락
- Chunking 평가 누락
- Embedding 평가 누락
- Metadata 기준 누락
- Query Rewrite 기준 누락
- Hybrid Search 기준 누락
- Re-Ranking 기준 누락
- Context Selection 기준 누락
- Groundedness 평가 누락
- Hallucination 평가 누락
- Failure Analysis 누락
- Regression Test 누락
- Observability 연결 누락
- Top-K만 늘리는 방식으로 최적화
- 모델 교체만으로 문제 해결 시도
- 장문 이론 설명 중심 작성
- Retrieval Queries 누락

---

### [실무]

나쁜 문서 예시:

```text
RAG 성능은 Top-K를 늘리거나 더 좋은 Embedding Model을 쓰면 좋아진다.
답변이 좋으면 검색도 잘 된 것이다.
```

좋은 문서 예시:

```text
RAG Evaluation은 Retrieval, Context Selection, Answer Grounding을 분리해 평가한다.

Flow:
Evaluation Dataset
→ Retrieval Metric 측정
→ Answer Groundedness 평가
→ Failure Analysis
→ Chunk / Query / Embedding / Re-Ranking 개선
→ Regression Test
```

---

### [FAQ]

Q. RAG Evaluation 문서에서 가장 피해야 할 것은?

A. 답변 품질만 보고 Retrieval, Context, Grounding, Failure 원인 분석을 누락하는 것이다.

Q. Top-K를 늘리면 RAG 성능이 좋아지는가?

A. 항상 그렇지 않다. 관련 없는 Chunk가 늘어나면 Context Noise가 증가할 수 있다.

Q. 더 좋은 모델을 쓰면 RAG 문제가 해결되는가?

A. 아니다. 문서 구조, Chunking, Query, Metadata, Embedding, Re-Ranking 문제가 먼저일 수 있다.

---

# 22. Document Split Rules

## 22.1 RAG Evaluation & Retrieval Optimization 문서 분할 기준

### [개념]

RAG Evaluation & Retrieval Optimization은 Evaluation Dataset, Retrieval Metric, Answer Evaluation, Chunking, Embedding, Query, Hybrid Search, Failure Analysis, Observability 범위가 넓기 때문에 Part 단위로 분리한다.

각 Part는 독립 검색 가능해야 하며, 하나의 Part는 하나의 핵심 주제를 다룬다.

---

### [핵심]

권장 문서 분할:

```text
RAG_Evaluation_Retrieval_Optimization_Part01_Core.md
RAG_Evaluation_Retrieval_Optimization_Part02_Evaluation_Dataset.md
RAG_Evaluation_Retrieval_Optimization_Part03_Retrieval_Metrics.md
RAG_Evaluation_Retrieval_Optimization_Part04_Answer_Groundedness_Evaluation.md
RAG_Evaluation_Retrieval_Optimization_Part05_Chunking_Embedding_Evaluation.md
RAG_Evaluation_Retrieval_Optimization_Part06_Query_Hybrid_Search_Optimization.md
RAG_Evaluation_Retrieval_Optimization_Part07_ReRanking_Context_Selection.md
RAG_Evaluation_Retrieval_Optimization_Part08_Failure_Analysis_Regression.md
RAG_Evaluation_Retrieval_Optimization_Part09_Observability_Troubleshooting.md
```

분할 기준:

- 하나의 Part는 하나의 핵심 주제
- Evaluation Dataset은 독립 문서 권장
- Retrieval Metric과 Answer Metric은 분리 권장
- Chunking과 Embedding은 함께 작성 가능
- Query와 Hybrid Search는 함께 작성 권장
- Re-Ranking과 Context Selection은 함께 작성 권장
- Failure Analysis와 Regression은 연결 문서로 작성
- Troubleshooting은 문제 / 원인 / 해결 형식
- 각 Part는 FAQ 포함
- 각 Part는 Retrieval Queries 포함

---

### [실무]

RAG Evaluation & Retrieval Optimization 문서 Set은 AI Expert Level과 RAGOps 문서에서 사용한다.

AI/ML Agent는 Evaluation과 Optimization 기준을 참조하고, Review Agent는 Groundedness와 Hallucination 검증 기준을 참조한다.

특정 도구는 별도 문서로 분리한다.

예:

```text
RAG_Evaluation_Retrieval_Optimization_Domain_Rules.md
RAGOps_Domain_Rules.md
Embedding_Evaluation_Part.md
ReRanking_Domain_Rules.md
LLM_Judge_Evaluation_Part.md
```

---

### [FAQ]

Q. RAG Evaluation & Retrieval Optimization 문서는 몇 개 Part로 나누는 것이 좋은가?

A. 8~9개 Part를 권장한다. Core, Dataset, Metrics, Answer Evaluation, Chunk/Embedding, Query/Hybrid, Re-Ranking/Context, Failure/Regression, Observability로 분리한다.

Q. RAGOps 문서와 합쳐도 되는가?

A. 기본 연결은 포함하되, RAG Evaluation은 검색 품질 평가와 최적화 기준 중심이므로 별도 문서로 분리하는 것이 좋다.

Q. 각 Part에도 Retrieval Queries가 필요한가?

A. 필요하다. 각 문서가 독립 검색될 수 있어야 한다.

---

# 23. Agent Usage Rules

## 23.1 Agent별 사용 기준

### [개념]

RAG Evaluation & Retrieval Optimization Domain Rules는 여러 Agent가 RAG 품질을 동일한 기준으로 평가하고 개선하도록 돕는다.

각 Agent는 자신의 역할에 맞는 Evaluation / Optimization Chunk를 우선 검색한다.

---

### [핵심]

PM Agent:

- RAG 품질 문제 범위 정의
- Evaluation 목표 설정
- 개선 우선순위 결정
- Human Review 필요 여부 판단
- 최종 개선 결과 승인

AI/ML Agent:

- Evaluation Dataset 설계
- Retrieval Metric 설계
- Embedding 평가
- Query Rewrite 설계
- Hybrid Search / Re-Ranking 최적화
- Failure Analysis 수행

Backend Agent:

- Retrieval Pipeline 구현
- Metadata Filter 구현
- Re-Ranking 연동
- Evaluation Log 저장
- RAG API 응답 구조 개선

DevOps Agent:

- Vector Index 운영
- Evaluation Pipeline 자동화
- RAG Observability 구성
- Latency / Cost 모니터링
- Index 재생성 관리

Review Agent:

- Groundedness 검토
- Hallucination 검토
- Citation Accuracy 검토
- Expected Context 누락 검토
- Regression Test 결과 검토

Architecture Review Agent:

- RAG Pipeline 구조 검토
- Evaluation / Observability 구조 검토
- 확장성 검토
- 비용 / 성능 Trade-off 검토

---

### [실무]

Agent별 검색 우선순위:

```text
PM Agent
→ Evaluation Goal / Failure Priority / Improvement Decision

AI/ML Agent
→ Evaluation Dataset / Retrieval Metrics / Query Optimization / Re-Ranking

Backend Agent
→ Retrieval Pipeline / Metadata / Context Selection / Logging

DevOps Agent
→ Vector Index / Evaluation Automation / Observability / Cost

Review Agent
→ Groundedness / Hallucination / Citation / Regression

Architecture Review Agent
→ RAG Architecture / Hybrid Search / Scalability / Trade-off
```

RAG Evaluation은 AI/ML Agent 단독 영역이 아니다.

Backend Agent, DevOps Agent, Review Agent가 함께 검색 Pipeline과 운영 품질을 검토해야 한다.

---

### [FAQ]

Q. RAG Evaluation & Retrieval Optimization Domain Rules는 어떤 Agent가 사용하는가?

A. PM Agent, AI/ML Agent, Backend Agent, DevOps Agent, Review Agent, Architecture Review Agent가 역할별로 사용한다.

Q. AI/ML Agent는 무엇을 우선 검색해야 하는가?

A. Evaluation Dataset, Retrieval Metric, Query Optimization, Hybrid Search, Re-Ranking, Failure Analysis를 우선 검색한다.

Q. Review Agent는 무엇을 검토해야 하는가?

A. Groundedness, Hallucination, Citation Accuracy, Expected Context 누락, Regression Test 결과를 검토해야 한다.

---

# 24. Final Goal

## 24.1 최종 목표

### [개념]

RAG Evaluation & Retrieval Optimization Domain Rules의 최종 목표는 Agent가 RAG 시스템의 검색 품질과 답변 품질을 분리 평가하고, 실패 원인을 분석하고, Retrieval Pipeline을 반복 개선할 수 있도록 문서 제작 기준을 제공하는 것이다.

---

### [핵심]

최종 목표:

- RAG Evaluation 개념 검색 가능
- Evaluation Dataset 설계 가능
- Retrieval Metric 선택 가능
- Answer Evaluation 가능
- Groundedness 평가 가능
- Faithfulness 평가 가능
- Hallucination 감지 가능
- Chunking Strategy 평가 가능
- Embedding Model 평가 가능
- Query Rewrite / Expansion 가능
- Hybrid Search 최적화 가능
- Re-Ranking 최적화 가능
- Context Selection 최적화 가능
- Metadata 기반 검색 개선 가능
- Retrieval Failure 분석 가능
- RAG Regression Test 가능
- RAG Observability 구성 가능
- Troubleshooting 가능

---

### [실무]

RAG Evaluation & Retrieval Optimization RAG Doc Set은 다음 작업을 지원해야 한다.

```text
User Request
→ Evaluation Goal 정의
→ Evaluation Dataset 준비
→ Baseline Retrieval 측정
→ Answer Groundedness 평가
→ Failure Analysis
→ Chunk / Query / Embedding / Re-Ranking 개선
→ Regression Test
→ Observability 연결
→ 운영 개선
```

문서 품질은 Agent가 RAG 실패 원인을 정확히 분리하고, 검색 품질과 답변 근거성을 반복 개선할 수 있는지로 결정된다.

---

### [FAQ]

Q. RAG Evaluation & Retrieval Optimization Domain Rules의 최종 목적은?

A. Agent가 RAG 검색 품질, Context 품질, 답변 근거성, 실패 원인을 평가하고 Retrieval Pipeline을 개선할 수 있도록 문서 제작 기준을 제공하는 것이다.

Q. 이 문서는 사람 학습용인가?

A. 아니다. AI Agent Retrieval과 RAG 운영 품질을 높이기 위한 문서이다.

Q. RAG Evaluation 문서 품질은 무엇으로 판단하는가?

A. Agent가 Retrieval, Context, Answer, Grounding, Failure 원인을 분리 평가하고 개선 Action으로 연결할 수 있는지로 판단한다.

---

# Retrieval Queries

### [FAQ]

Q. RAG Evaluation이란?
A. RAG 시스템의 Retrieval, Context Selection, Answer Grounding, Hallucination, Citation 품질을 평가하는 과정이다.

Q. Retrieval Optimization이란?
A. Chunking, Embedding, Query Rewrite, Hybrid Search, Re-Ranking, Context Selection을 개선해 검색 품질을 높이는 과정이다.

Q. RAG Evaluation과 일반 LLM Evaluation의 차이는?
A. 일반 LLM Evaluation은 답변 품질 중심이고, RAG Evaluation은 Retrieval, Context, Grounding까지 평가한다.

Q. RAG Evaluation Dataset은 무엇인가?
A. Query, Expected Context, Expected Answer, Source Document, Evaluation Criteria를 포함한 평가 데이터셋이다.

Q. Expected Context란?
A. 특정 Query에 답하기 위해 검색되어야 하는 핵심 Chunk, 문서, 개념, Evidence이다.

Q. No-Answer Query는 왜 필요한가?
A. 문서에 없는 질문에 대해 모델이 모른다고 답하는지 평가하기 위해 필요하다.

Q. Retrieval Metric에는 무엇이 있는가?
A. Hit Rate, Recall@K, Precision@K, MRR, NDCG, Context Relevance, Missing Context Rate가 있다.

Q. Hit Rate란?
A. 필요한 문서나 Chunk가 검색 결과 안에 포함되었는지 평가하는 Metric이다.

Q. Recall@K란?
A. 필요한 문서 중 Top-K 검색 결과에 포함된 비율을 평가하는 Metric이다.

Q. Precision@K란?
A. Top-K 검색 결과 중 실제 관련 문서 비율을 평가하는 Metric이다.

Q. MRR이란?
A. 정답 Chunk가 검색 결과에서 얼마나 상위에 등장하는지 평가하는 Metric이다.

Q. Answer Evaluation은 무엇을 평가하는가?
A. 최종 답변이 질문에 직접 답하고, 검색 Context에 근거하며, 문서에 없는 내용을 생성하지 않았는지 평가한다.

Q. Groundedness란?
A. 답변이 검색된 문서나 Tool Result 같은 근거에 기반하는 정도이다.

Q. Faithfulness란?
A. 답변이 제공된 Context를 왜곡하지 않고 충실히 반영하는 정도이다.

Q. Hallucination Evaluation이란?
A. 답변이 문서에 없는 내용, 근거 없는 주장, 존재하지 않는 코드나 API를 생성했는지 평가하는 과정이다.

Q. Chunking Evaluation은 왜 필요한가?
A. Chunk가 너무 크거나 작거나 의미 단위가 깨지면 Retrieval 품질과 답변 품질이 낮아지기 때문이다.

Q. Embedding Evaluation은 왜 필요한가?
A. Embedding Model이 Query와 문서 Chunk를 잘 연결하지 못하면 RAG가 필요한 근거를 찾지 못하기 때문이다.

Q. Query Rewrite는 언제 필요한가?
A. 사용자 질문이 모호하거나 문서 용어와 다르거나 첫 검색 결과가 부족할 때 필요하다.

Q. Query Expansion이란?
A. 원래 Query에 관련 Domain 용어, 동의어, 하위 개념을 추가해 검색 범위를 넓히는 것이다.

Q. Hybrid Search란?
A. Semantic Search, Keyword Search, Metadata Filtering, Graph Search, Re-Ranking을 함께 사용하는 검색 전략이다.

Q. Keyword Search는 언제 중요한가?
A. 에러 메시지, 코드, 명령어, 설정값, 파일명, 클래스명처럼 정확한 문자열이 중요한 경우 필요하다.

Q. Re-Ranking이란?
A. 1차 검색 결과를 Query와의 관련성, Source Priority, Metadata 기준으로 다시 정렬하는 과정이다.

Q. Context Selection이란?
A. 검색된 Chunk 중 최종 LLM 입력에 넣을 Context를 선택하는 과정이다.

Q. Metadata Optimization이란?
A. 문서와 Chunk에 Domain, Part, Version, Section, Source 같은 Metadata를 부여해 검색 품질을 높이는 과정이다.

Q. Retrieval Failure Analysis란?
A. 필요한 Context를 검색하지 못했거나 관련 없는 Context를 검색한 원인을 Query, Chunk, Embedding, Metadata, Re-Ranking 등으로 분류하는 과정이다.

Q. Correct Chunk Ranked Low란?
A. 필요한 Chunk가 검색되었지만 순위가 낮아 실제 Context에 포함되지 못하는 문제이다.

Q. Answer Ignored Context란?
A. 올바른 Context가 제공되었지만 LLM이 답변 생성에서 이를 사용하지 않는 문제이다.

Q. RAG Optimization Loop는 무엇인가?
A. Evaluation Dataset 준비, Baseline 측정, Failure Analysis, Pipeline 개선, 재평가, Regression Test를 반복하는 과정이다.

Q. RAG Regression Test는 왜 필요한가?
A. RAG 최적화가 일부 Query 품질은 높이지만 기존 Query 품질을 떨어뜨릴 수 있기 때문이다.

Q. RAG Observability란?
A. Query, Retrieval, Context, Answer, Groundedness, Hallucination, Latency, Cost를 운영 중 추적하는 구조이다.

Q. RAG Evaluation 문서 분할은 어떻게 하는가?
A. Core, Dataset, Metrics, Answer Evaluation, Chunk/Embedding, Query/Hybrid, Re-Ranking/Context, Failure/Regression, Observability로 분리한다.

Q. RAG Evaluation 문서에서 피해야 할 것은?
A. 답변 품질만 보고 Retrieval, Context, Grounding, Failure 원인 분석을 누락하는 것이다.

Q. RAG Evaluation & Retrieval Optimization Domain Rules는 어떤 Agent가 사용하는가?
A. PM Agent, AI/ML Agent, Backend Agent, DevOps Agent, Review Agent, Architecture Review Agent가 역할별로 사용한다.
