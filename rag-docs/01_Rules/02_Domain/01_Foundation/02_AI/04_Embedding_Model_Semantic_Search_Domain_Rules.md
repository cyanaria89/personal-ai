# Embedding Model & Semantic Search Domain Rules

---

# 1. Domain Purpose

Embedding Model & Semantic Search Domain 문서는 AI Agent / RAG Agent / Review Agent용 RAG 문서 제작 규칙이다.

목적:

- Embedding Model 기본 개념 이해
- Text를 Vector로 변환하는 구조 이해
- Semantic Search 원리 설명
- Query Embedding / Document Embedding 구조 설계
- Chunking 전략과 Embedding 품질 연결
- Vector Similarity Search 기준 제공
- RAG 검색 품질 개선 지원
- Retrieval 실패 원인 분석 지원
- BGE-M3 같은 Embedding Model 활용 기준 제공

우선순위:

1. Embedding Core Concept
2. Semantic Search Quality
3. Chunk Quality
4. Query / Document Embedding
5. Similarity Search
6. Retrieval Optimization
7. RAG Integration

---

# 2. Scope

포함 범위:

- Embedding Core
- Embedding Model
- Text Embedding
- Query Embedding
- Document Embedding
- Chunk Embedding
- Vector
- Vector Dimension
- Semantic Similarity
- Similarity Search
- Cosine Similarity
- Dot Product
- Euclidean Distance
- Chunking
- Chunk Size
- Chunk Overlap
- Metadata
- Top-K Retrieval
- Similarity Threshold
- Hybrid Search 기초
- Reranking 기초
- Multilingual Embedding
- BGE-M3
- RAG Retrieval Integration
- Retrieval Evaluation
- Retrieval Troubleshooting

제외 범위:

- Vector Database 내부 구현 심화
- ANN Index 상세 구현
- Graph RAG 심화
- Agentic RAG 심화
- Fine-Tuning 상세
- Embedding Model 학습 상세
- MLOps 운영 상세

---

# 3. Section Priority

## Required

- [개념]
- [핵심]
- [실무]
- [FAQ]

---

## Strongly Recommended

- [Flow]
- [예제]
- [주의]
- [Best Practice]
- [Troubleshooting]
- [Checklist]
- [Comparison]

---

# 4. Embedding Core Rules

Embedding 문서는 Text를 의미 기반 Vector로 변환하는 개념 중심으로 작성한다.

반드시 포함:

- Embedding은 Text를 Vector로 변환
- 의미가 비슷한 Text는 가까운 Vector로 표현
- Embedding Model은 답변 생성 모델이 아니라 검색용 모델
- Query와 Document를 같은 Embedding 공간에 배치
- Semantic Search는 키워드 일치가 아니라 의미 유사도 기반 검색
- RAG 품질은 Embedding 품질과 Chunk 품질에 크게 의존

기본 Flow:

```text
Text
→ Embedding Model
→ Vector
→ Similarity Search
→ Retrieved Documents
```

금지:

- Embedding을 LLM 답변 생성과 혼동
- Vector DB만 있으면 RAG가 잘 된다는 설명
- Chunk 품질을 무시한 Embedding 설명
- Similarity Score를 절대적 정답 점수처럼 설명

---

# 5. Embedding Model Rules

Embedding Model은 검색 목적에 맞게 선택해야 한다.

필수 포함:

- Embedding Model
- Dense Embedding
- Sparse Embedding
- Multi-vector Embedding
- Multilingual Embedding
- Domain Suitability
- Vector Dimension
- Context Length
- Performance
- Latency

반드시 설명:

- Embedding Model은 Text를 Vector로 변환하는 모델
- Chat Model과 Embedding Model은 역할이 다름
- 한국어 문서가 많으면 Multilingual 성능이 중요
- 코드 / 기술 문서 검색에는 기술 용어 이해가 중요
- Model 변경 시 기존 Vector를 재생성해야 할 수 있음

주의:

- Embedding Model을 변경하면 Vector Dimension이 달라질 수 있음
- 서로 다른 Model로 만든 Vector를 같은 Index에서 비교하면 안 됨
- Domain에 맞지 않는 Embedding Model은 검색 품질 저하
- Local Embedding Model은 속도와 자원 사용량 고려

---

# 6. BGE-M3 Rules

BGE-M3는 Multilingual / Multi-function Embedding Model 예시로 설명한다.

필수 포함:

- BGE-M3
- Multilingual Embedding
- Dense Retrieval
- Sparse Retrieval
- Multi-vector Retrieval
- Korean Retrieval
- RAG Document Search

반드시 설명:

- BGE-M3는 다국어 검색에 적합한 Embedding Model로 사용할 수 있음
- 한국어 RAG 문서 검색에 활용 가능
- Dense Retrieval 중심으로 사용 가능
- Hybrid Search / Reranking과 함께 품질 개선 가능
- Local 환경에서 사용할 경우 모델 로딩과 속도 고려

주의:

- BGE-M3를 사용해도 Chunk 구조가 나쁘면 검색 품질이 낮음
- 문서 도메인 용어가 잘 드러나도록 제목과 FAQ를 작성해야 함
- Embedding Model 성능만으로 Hallucination이 해결되지는 않음

---

# 7. Vector Rules

Vector는 Embedding 결과를 표현하는 숫자 배열이다.

필수 포함:

- Vector
- Vector Dimension
- Dense Vector
- Sparse Vector
- Normalization
- Similarity Score

예시:

```text
"Spring Transaction"
→ [0.12, -0.03, 0.87, ...]
```

반드시 설명:

- Vector는 텍스트 의미를 수치화한 표현
- Dimension은 Vector 길이
- 같은 Embedding Model의 Vector끼리 비교해야 함
- Vector는 사람이 직접 해석하기 어렵지만 유사도 계산에 사용

주의:

- Vector Dimension 불일치 주의
- Vector 자체를 수정하지 않음
- Vector 저장 전 원본 Text와 Metadata 연결 필요
- Vector만 저장하고 원문을 잃어버리면 답변 근거 제시가 어려움

---

# 8. Query Embedding Rules

Query Embedding은 사용자 질문을 Vector로 변환하는 과정이다.

필수 포함:

- User Query
- Query Embedding
- Query Rewrite
- Query Expansion
- Keyword 포함
- Intent
- Domain Term

기본 Flow:

```text
User Query
→ Query Normalization
→ Query Embedding
→ Vector Search
```

반드시 설명:

- 사용자 질문을 Embedding Model에 입력해 Query Vector 생성
- Query가 짧거나 모호하면 검색 품질이 낮아질 수 있음
- Query Rewrite로 검색 의도를 명확히 할 수 있음
- 핵심 Domain Keyword를 포함하면 Retrieval 품질이 좋아질 수 있음

주의:

- Query를 과도하게 바꾸면 원래 의도가 손상될 수 있음
- 사용자 질문이 여러 개념을 섞으면 검색 결과가 분산될 수 있음
- Query와 문서 용어가 너무 다르면 Retrieval 실패 가능

---

# 9. Document Embedding Rules

Document Embedding은 문서 Chunk를 Vector로 변환하는 과정이다.

필수 포함:

- Document
- Chunk
- Chunk Embedding
- Metadata
- Source
- Title
- Section
- Retrieval Queries

기본 Flow:

```text
Markdown Document
→ Split into Chunks
→ Add Metadata
→ Generate Embedding
→ Store Vector
```

반드시 설명:

- 긴 문서는 Chunk 단위로 Embedding
- Chunk는 독립 검색되어도 의미가 유지되어야 함
- 제목, 섹션, 도메인 정보를 Metadata로 연결
- Code Block과 설명이 분리되지 않도록 주의
- FAQ / Retrieval Queries는 검색 매칭 강화에 도움

주의:

- 문서 전체를 하나의 Vector로 만들면 세부 검색 품질 저하
- 너무 작은 Chunk는 문맥 부족
- 너무 큰 Chunk는 주제 혼합
- 문서 수정 후 Embedding 재생성 필요

---

# 10. Chunking Rules

Chunking은 RAG 검색 품질의 핵심이다.

필수 포함:

- Chunk Size
- Chunk Overlap
- Semantic Chunking
- Header Based Chunking
- Code Block Preservation
- FAQ Chunk
- Retrieval Queries Chunk

권장 Flow:

```text
Markdown Header
→ Section Split
→ Semantic Boundary Check
→ Code Block Preservation
→ Chunk Metadata Attach
```

반드시 설명:

- Chunk는 하나의 주제를 중심으로 구성
- Header는 Chunk 경계로 활용 가능
- Code Example과 설명은 가능하면 같은 Chunk에 유지
- FAQ는 Query Matching을 강화
- Chunk Overlap은 문맥 단절을 완화하지만 중복을 증가시킴

주의:

- Code Block 중간에서 Chunk 분리 금지
- 여러 개념을 한 Chunk에 과도하게 섞지 말 것
- 너무 많은 Overlap은 저장 공간과 검색 중복 증가
- 제목 없는 Chunk는 검색 품질이 낮아질 수 있음

---

# 11. Chunk Size Rules

Chunk Size는 검색 품질과 Context 효율에 영향을 준다.

필수 포함:

- Small Chunk
- Large Chunk
- Token Count
- Context Window
- Retrieval Precision
- Retrieval Recall

비교:

| Chunk Size | 장점           | 단점           | 적합               |
| ---------- | -------------- | -------------- | ------------------ |
| Small      | 정밀 검색 유리 | 문맥 부족      | FAQ, 단일 개념     |
| Medium     | 균형 좋음      | 설계 필요      | 일반 RAG 문서      |
| Large      | 문맥 풍부      | 주제 혼합 가능 | 긴 설명, 복합 예제 |

반드시 설명:

- Chunk Size는 문서 성격에 따라 조정
- 개념 설명은 중간 크기가 적합
- FAQ는 작은 Chunk도 효과적
- 코드 예제는 설명과 함께 유지하는 것이 중요

주의:

- 무조건 작은 Chunk가 좋은 것은 아님
- 무조건 큰 Chunk도 좋은 것은 아님
- 검색 결과가 자주 빗나가면 Chunk 구조 점검 필요

---

# 12. Metadata Rules

Metadata는 검색 결과 해석과 필터링에 중요하다.

필수 포함:

- source
- fileName
- domain
- level
- part
- section
- title
- tags
- version
- createdAt
- updatedAt

예시:

```json
{
  "domain": "AI",
  "level": "Foundation",
  "fileName": "Embedding_Model_Semantic_Search_Part01_Core.md",
  "section": "Chunking",
  "tags": ["embedding", "semantic-search", "rag"]
}
```

반드시 설명:

- Metadata는 검색 결과의 출처와 문맥을 보존
- Domain / Level / Part 정보는 Agent Routing에 유용
- Section 정보는 답변 근거 제시에 유용
- Filtered Retrieval에 활용 가능

주의:

- Metadata 필드명 통일
- 누락된 Metadata는 검색 결과 해석을 어렵게 함
- 잘못된 Metadata는 잘못된 Agent 참조를 유발

---

# 13. Semantic Similarity Rules

Semantic Similarity는 의미 기반 유사도를 계산하는 기준이다.

필수 포함:

- Semantic Similarity
- Cosine Similarity
- Dot Product
- Euclidean Distance
- Similarity Score
- Ranking

기본 Flow:

```text
Query Vector
+ Document Vector
→ Similarity Score
→ Rank Documents
```

반드시 설명:

- Similarity Score는 Query와 Document의 의미적 가까움을 나타냄
- 높은 Score가 항상 정답을 의미하지는 않음
- Score는 Model / Index / Normalization 방식에 따라 해석이 달라짐
- Ranking 결과는 후처리와 검증이 필요

주의:

- Similarity Score를 절대 점수처럼 사용 금지
- 낮은 Score라도 필요한 문서일 수 있음
- 높은 Score라도 질문 의도와 다를 수 있음
- 검색 결과는 LLM 답변 전 검토 필요

---

# 14. Top-K Retrieval Rules

Top-K Retrieval은 검색 결과 개수 선택 기준이다.

필수 포함:

- Top-K
- Precision
- Recall
- Context Budget
- RAG Context
- Ranking

기본 Flow:

```text
Query
→ Retrieve Top-K Documents
→ Filter / Rerank
→ Build Context
```

반드시 설명:

- Top-K는 검색 결과로 가져올 Chunk 개수
- Top-K가 작으면 필요한 문서 누락 가능
- Top-K가 크면 관련 없는 문서가 섞일 수 있음
- Context Window와 Token Budget을 함께 고려
- 검색 품질이 낮으면 Top-K 조정보다 Chunk / Query 개선이 먼저일 수 있음

주의:

- 무조건 Top-K를 크게 하지 말 것
- 관련 없는 Chunk가 많으면 LLM 답변 품질 저하
- 검색 결과 중복 제거 필요
- Domain별 Top-K 기준이 다를 수 있음

---

# 15. Similarity Threshold Rules

Similarity Threshold는 낮은 관련도 결과를 제외하는 기준이다.

필수 포함:

- Similarity Threshold
- Minimum Score
- No Result
- Low Confidence
- Fallback

반드시 설명:

- Threshold는 낮은 관련도 문서를 제거하는 데 사용
- 너무 높으면 필요한 문서가 누락됨
- 너무 낮으면 관련 없는 문서가 포함됨
- 검색 결과가 없을 때 fallback 규칙 필요

주의:

- Threshold 값은 모델과 데이터에 따라 다름
- 일괄 고정값보다 평가 기반 조정 권장
- Score 분포 확인 필요
- 검색 실패 시 사용자에게 부족한 정보를 알려야 함

---

# 16. Hybrid Search Rules

Hybrid Search는 Keyword Search와 Semantic Search를 조합한다.

필수 포함:

- Keyword Search
- Semantic Search
- BM25
- Dense Retrieval
- Sparse Retrieval
- Hybrid Retrieval
- Score Fusion

비교:

| 방식            | 장점                  | 단점                    |
| --------------- | --------------------- | ----------------------- |
| Keyword Search  | 정확한 용어 매칭 강함 | 표현이 다르면 약함      |
| Semantic Search | 의미 기반 검색 강함   | 정확한 키워드 누락 가능 |
| Hybrid Search   | 두 방식 보완          | 구성 복잡도 증가        |

반드시 설명:

- 기술 문서 검색은 정확한 용어와 의미 검색이 모두 중요
- 클래스명, 메서드명, 에러명은 Keyword Search가 유리
- 개념 질문은 Semantic Search가 유리
- Hybrid Search는 RAG 검색 품질 개선에 유용

주의:

- Score 결합 기준 필요
- Keyword와 Vector 결과 중복 제거 필요
- Hybrid Search가 항상 필요한 것은 아님
- 시스템 복잡도 증가 고려

---

# 17. Reranking Rules

Reranking은 1차 검색 결과를 다시 정렬하는 과정이다.

필수 포함:

- Reranker
- Cross Encoder
- Relevance Scoring
- Candidate Documents
- Top-K Rerank
- Final Context Selection

기본 Flow:

```text
Initial Retrieval
→ Candidate Chunks
→ Reranker
→ Reordered Results
→ Context Selection
```

반드시 설명:

- Reranking은 검색 품질을 높이는 후처리
- 1차 검색은 넓게 가져오고 Reranker가 정밀하게 정렬
- 비용과 Latency가 증가할 수 있음
- 중요한 RAG 시스템에서 품질 개선에 효과적

주의:

- Reranker를 쓰면 응답 시간이 늘어날 수 있음
- 후보 수가 너무 많으면 비용 증가
- Reranking이 잘못된 Chunk 구조를 완전히 해결하지는 못함

---

# 18. Multilingual Retrieval Rules

Multilingual Retrieval은 한국어 / 영어 혼합 문서에서 중요하다.

필수 포함:

- Korean Query
- English Keyword
- Mixed Language Document
- Multilingual Embedding
- Technical Term
- Query Expansion

반드시 설명:

- 개발 문서는 한국어 설명과 영어 기술 용어가 섞임
- Query에 영어 핵심 키워드를 함께 포함하면 검색 품질이 좋아질 수 있음
- Multilingual Embedding Model은 한국어/영어 혼합 검색에 유리
- FAQ에 한국어 질문과 영어 용어를 함께 넣는 것이 효과적

예시:

```text
트랜잭션 경계
Transaction Boundary
@Transactional
```

주의:

- 한국어 번역어만 사용하면 영어 기술 문서 검색이 약해질 수 있음
- 영어 용어만 사용하면 한국어 질문과 매칭이 약해질 수 있음
- 핵심 용어는 한글 + 영어 병기 권장

---

# 19. RAG Integration Rules

Embedding과 Semantic Search는 RAG의 Retrieval 단계로 설명한다.

필수 포함:

- User Query
- Query Embedding
- Vector Search
- Retrieved Context
- Prompt Assembly
- Grounded Answer
- Missing Information

기본 Flow:

```text
User Query
→ Query Embedding
→ Semantic Search
→ Retrieved Chunks
→ Prompt Context
→ LLM Answer
```

반드시 설명:

- Embedding은 답변 생성 전 검색 단계
- 검색된 Chunk가 답변 근거로 사용됨
- 검색 결과가 부정확하면 LLM 답변도 부정확해짐
- RAG는 Retrieval과 Generation 모두 관리해야 함

주의:

- LLM이 검색 실패를 일반 지식으로 덮어쓰지 않도록 Prompt 필요
- 검색 결과가 부족하면 “문서에 없음” 또는 추가 검색 필요
- Retrieved Context가 서로 충돌하면 우선순위 필요

---

# 20. Retrieval Evaluation Rules

Retrieval Evaluation은 검색 품질 개선에 필요하다.

필수 포함:

- Retrieval Hit Rate
- Precision
- Recall
- MRR
- NDCG 기초
- Golden Query
- Expected Document
- Failure Case

기본 Flow:

```text
Test Queries
→ Retrieve Documents
→ Compare Expected Results
→ Analyze Failure
→ Improve Chunk / Query / Metadata
```

반드시 설명:

- 검색 품질은 테스트 Query로 평가 가능
- 사용자가 자주 묻는 질문을 Golden Query로 만들 수 있음
- 기대 문서가 Top-K 안에 들어오는지 확인
- 실패 사례를 기반으로 문서를 개선

주의:

- 한두 개 질문으로 전체 품질 판단 금지
- 평가 Query가 실제 사용자 질문과 달라지지 않도록 주의
- Retrieval 성공과 답변 성공은 다름

---

# 21. Retrieval Troubleshooting Rules

반드시 포함 추천.

형식:

```md
문제:

원인:

해결:
```

---

## 검색 결과가 안 나옴

문제:

- 관련 문서가 있는데 Retrieval 결과에 나타나지 않음

원인:

- Query 표현과 문서 표현 불일치
- Chunk 제목이 불명확함
- Metadata 누락
- Chunk가 너무 큼
- Embedding 미생성 또는 오래됨

해결:

- FAQ / Retrieval Queries 추가
- 핵심 키워드 한글 + 영어 병기
- Chunk 제목 개선
- 문서 수정 후 Embedding 재생성
- Query Rewrite 적용

---

## 관련 없는 문서가 검색됨

문제:

- 질문과 무관한 Chunk가 Top-K에 포함됨

원인:

- Top-K가 너무 큼
- Chunk에 여러 개념 혼합
- Similarity Threshold가 낮음
- 공통 단어가 많음

해결:

- Chunk를 주제별로 분리
- Top-K 조정
- Threshold 조정
- Metadata Filter 적용
- Reranking 적용 검토

---

## 검색은 됐는데 답변이 틀림

문제:

- Retrieved Context는 있지만 LLM 답변이 부정확함

원인:

- Context가 불충분함
- Prompt Grounding 규칙 부족
- Chunk가 너무 단편적임
- 서로 충돌하는 Context 포함

해결:

- Prompt에 문서 근거 우선 규칙 추가
- 필요한 Chunk를 함께 검색되게 구조 개선
- 관련 없는 Context 제거
- 답변 검증 단계 추가

---

## 비슷한 문서가 너무 많이 검색됨

문제:

- 중복 Chunk가 Top-K를 차지함

원인:

- Chunk Overlap 과다
- 중복 설명이 많음
- Retrieval Queries가 여러 문서에 동일하게 반복

해결:

- 중복 Chunk 제거
- Overlap 줄이기
- Retrieval Queries를 Domain별로 차별화
- 결과 Deduplication 적용

---

## 한국어 질문 검색 품질이 낮음

문제:

- 한국어 Query가 영어 기술 용어 문서를 잘 찾지 못함

원인:

- 한글/영어 용어 병기 부족
- Multilingual Embedding 성능 한계
- Query가 너무 짧음

해결:

- 핵심 용어 한글 + 영어 병기
- FAQ에 실제 한국어 질문 추가
- Query Expansion 적용
- BGE-M3 같은 Multilingual Embedding 활용

---

# 22. Best Practice Rules

Best Practice:

- 문서는 Header 중심으로 작성
- Chunk는 하나의 개념만 담기
- Code Block과 설명은 가능하면 함께 유지
- 핵심 용어는 한글 + 영어 병기
- FAQ와 Retrieval Queries를 적극 활용
- Metadata에 domain / level / section 포함
- Top-K는 Context Window와 함께 조정
- 검색 실패 사례를 문서 개선에 반영
- Embedding Model 변경 시 재색인
- Reranking은 품질이 필요한 경우 적용
- Retrieval 결과는 LLM 답변 전 검증

---

# 23. Comparison Rules

Embedding / Semantic Search 문서는 비교 기준을 포함한다.

필수 비교 대상:

- Chat Model vs Embedding Model
- Keyword Search vs Semantic Search
- Semantic Search vs Hybrid Search
- Small Chunk vs Large Chunk
- Top-K 증가 vs Reranking
- Metadata Filter vs Similarity Threshold
- Dense Retrieval vs Sparse Retrieval

예시:

| 비교 | Keyword Search             | Semantic Search                 |
| ---- | -------------------------- | ------------------------------- |
| 기준 | 단어 일치                  | 의미 유사도                     |
| 장점 | 정확한 용어 검색 강함      | 표현이 달라도 검색 가능         |
| 단점 | 표현 차이에 약함           | 정확한 키워드 검색 약할 수 있음 |
| 적합 | 에러명, 클래스명, 메서드명 | 개념 질문, 유사 의미 검색       |

---

# 24. Checklist Rules

Embedding / Semantic Search 문서에는 Checklist를 포함할 수 있다.

예시:

```md
### [Checklist]

- [ ] Chunk 제목이 명확한가?
- [ ] Chunk가 하나의 개념만 다루는가?
- [ ] Code Block이 중간에 잘리지 않았는가?
- [ ] 핵심 용어를 한글 + 영어로 병기했는가?
- [ ] Metadata에 domain / level / section이 포함되었는가?
- [ ] FAQ가 실제 사용자 질문 형태인가?
- [ ] Retrieval Queries가 포함되었는가?
- [ ] Top-K 기준이 정의되어 있는가?
- [ ] 검색 실패 사례를 기록했는가?
- [ ] Embedding Model 변경 시 재색인 규칙이 있는가?
```

---

# 25. Retrieval Optimization Rules

강조 대상 키워드:

- Embedding
- Embedding Model
- Text Embedding
- Query Embedding
- Document Embedding
- Chunk Embedding
- Vector
- Vector Dimension
- Semantic Search
- Semantic Similarity
- Similarity Search
- Cosine Similarity
- Dot Product
- Chunking
- Chunk Size
- Chunk Overlap
- Metadata
- Top-K Retrieval
- Similarity Threshold
- Hybrid Search
- Keyword Search
- BM25
- Reranking
- Multilingual Embedding
- BGE-M3
- Korean Retrieval
- RAG Retrieval
- Retrieval Evaluation
- Retrieval Hit Rate

키워드 반복 허용.

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

예:

- Embedding이 뭐야?
- Embedding Model은 뭐에 써?
- Chat Model과 Embedding Model 차이는?
- Semantic Search가 뭐야?
- Vector Search는 어떻게 동작해?
- Chunk Size는 어떻게 정해?
- Top-K는 몇 개가 좋아?
- Similarity Score가 높으면 무조건 좋은 문서야?
- 한국어 RAG에는 어떤 Embedding이 좋아?
- BGE-M3는 어디에 써?
- 검색 결과가 안 나올 때 어떻게 해?
- RAG 검색 품질은 어떻게 개선해?

---

# 26. Version Rules

기준:

- Modern Embedding Model
- Multilingual Embedding
- BGE-M3 활용 가능 구조
- Vector Database 기반 RAG
- Markdown 기반 RAG Document
- Semantic Search 기반 Retrieval
- Hybrid Search / Reranking 확장 가능성 고려

Legacy 제외:

- 단순 Keyword Search만 기준으로 설명
- Embedding Model과 Chat Model을 혼동하는 설명
- Chunking 없이 전체 문서 Embedding만 사용하는 방식
- Metadata 없이 Vector만 저장하는 방식

---

# 27. Common Mistakes

자주 발생:

- Chat Model을 Embedding Model처럼 사용하려 함
- Embedding Model 변경 후 기존 Vector 재사용
- Vector Dimension 불일치
- 너무 큰 Chunk로 여러 개념 혼합
- 너무 작은 Chunk로 문맥 부족
- Code Block 중간에서 Chunk 분리
- Metadata 누락
- Top-K를 무조건 크게 설정
- Similarity Score를 절대 정답으로 해석
- 한국어/영어 용어 병기 부족
- 문서 수정 후 Embedding 재생성 누락
- Retrieval 실패를 LLM 문제로만 판단

---

# 28. Final Goal

Embedding Model & Semantic Search RAG 문서는 Agent가 아래를 수행 가능해야 한다.

- Embedding 개념 설명
- Chat Model과 Embedding Model 구분
- Query Embedding / Document Embedding 구조 이해
- Semantic Search 원리 설명
- Chunking 전략 제안
- Metadata 설계 기준 제안
- Top-K / Threshold 기준 설명
- Hybrid Search / Reranking 적용 여부 판단
- BGE-M3 활용 기준 설명
- 한국어 / 영어 혼합 RAG 검색 품질 개선
- Retrieval 실패 원인 분석
- RAG 검색 품질 개선 방향 제안

문서 품질이 Retrieval 품질과 RAG 답변 품질을 결정한다.

---

# Retrieval Queries

### [FAQ]

Q. Embedding이 뭐야?

A.
텍스트를 의미 기반 숫자 벡터로 변환하는 것이다. 의미가 비슷한 텍스트는 벡터 공간에서 가깝게 표현된다.

Q. Embedding Model은 뭐에 써?

A.
문서와 질문을 Vector로 변환해 Semantic Search와 RAG 검색에 사용한다.

Q. Chat Model과 Embedding Model 차이는?

A.
Chat Model은 답변을 생성하고, Embedding Model은 검색을 위한 Vector를 생성한다.

Q. Semantic Search가 뭐야?

A.
단어가 정확히 일치하지 않아도 의미가 비슷한 문서를 찾는 검색 방식이다.

Q. Vector Search는 어떻게 동작해?

A.
Query Vector와 Document Vector의 유사도를 계산해 가장 가까운 문서를 찾는다.

Q. Query Embedding은 뭐야?

A.
사용자 질문을 Embedding Model로 Vector로 변환하는 과정이다.

Q. Document Embedding은 뭐야?

A.
문서 Chunk를 Embedding Model로 Vector로 변환해 검색 가능하게 저장하는 과정이다.

Q. Chunking은 왜 중요해?

A.
Chunk가 검색 단위가 되기 때문에, Chunk 품질이 Retrieval 품질을 크게 좌우한다.

Q. Chunk Size는 어떻게 정해?

A.
하나의 개념이 독립적으로 이해될 정도로 유지하되, 여러 개념이 섞이지 않도록 조정한다.

Q. Chunk Overlap은 왜 써?

A.
Chunk 경계에서 문맥이 끊기는 문제를 줄이기 위해 사용한다. 다만 중복이 증가할 수 있다.

Q. Code Block은 어떻게 Chunking해야 해?

A.
Code Block 중간에서 자르지 말고, 가능하면 설명과 같은 Chunk에 유지한다.

Q. Metadata는 왜 필요해?

A.
검색 결과의 출처, 도메인, 레벨, 섹션을 파악하고 필터링하기 위해 필요하다.

Q. Top-K는 몇 개가 좋아?

A.
고정 정답은 없다. 필요한 문서가 누락되지 않으면서 관련 없는 문서가 과도하게 섞이지 않도록 조정한다.

Q. Similarity Score가 높으면 무조건 좋은 문서야?

A.
아니다. Score는 의미적 유사도일 뿐이고, 질문 의도와 맞는지 검토해야 한다.

Q. Similarity Threshold는 왜 필요해?

A.
관련도가 낮은 검색 결과를 제외해 RAG Context 품질을 높이기 위해 사용한다.

Q. Hybrid Search는 언제 써?

A.
기술 용어, 에러명, 클래스명처럼 정확한 키워드 검색과 의미 검색이 모두 필요할 때 사용한다.

Q. Reranking은 언제 필요해?

A.
1차 검색 결과는 나오지만 순서가 부정확하거나 관련 없는 문서가 섞일 때 품질 개선용으로 사용한다.

Q. 한국어 RAG에는 어떤 Embedding이 좋아?

A.
한국어와 영어 기술 용어가 섞인 문서라면 Multilingual Embedding Model이 유리하다.

Q. BGE-M3는 어디에 써?

A.
한국어/영어 혼합 문서 검색, Dense Retrieval, RAG 검색에 사용할 수 있는 Multilingual Embedding Model로 활용할 수 있다.

Q. 검색 결과가 안 나올 때 어떻게 해?

A.
Query 표현과 문서 표현을 맞추고, 핵심 용어 병기, FAQ 추가, Chunk 제목 개선, Embedding 재생성을 확인한다.

Q. 관련 없는 문서가 검색되면 어떻게 해?

A.
Chunk를 주제별로 나누고, Top-K와 Threshold를 조정하며, Metadata Filter나 Reranking을 검토한다.

Q. RAG 검색 품질은 어떻게 개선해?

A.
Chunk 구조 개선, Metadata 보강, Retrieval Queries 추가, Query Rewrite, Hybrid Search, Reranking을 단계적으로 검토한다.
