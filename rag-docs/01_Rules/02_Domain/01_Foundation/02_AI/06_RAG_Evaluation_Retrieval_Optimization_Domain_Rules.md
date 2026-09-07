# RAG Evaluation & Retrieval Optimization Domain Rules

---

# 1. Domain Purpose

RAG Evaluation & Retrieval Optimization Domain 문서는 AI Agent / RAG Agent / Review Agent용 RAG 문서 제작 규칙이다.

목적:

- RAG 검색 품질 평가 기준 제공
- Retrieval 실패 원인 분석 지원
- Chunk / Metadata / Query / Top-K 개선 기준 제공
- RAG 답변 품질 평가 기준 제공
- Hallucination / Grounding 문제 분석 지원
- Golden Query 기반 테스트 설계 지원
- RAG 문서 품질 개선 방향 제안
- Agent가 RAG 시스템을 검토하고 개선할 수 있도록 지원

우선순위:

1. Retrieval Quality
2. Grounded Answer
3. Failure Analysis
4. Query Optimization
5. Chunk Optimization
6. Context Optimization
7. Evaluation Loop

---

# 2. Scope

포함 범위:

- RAG Evaluation Core
- Retrieval Evaluation
- Generation Evaluation
- Golden Query
- Expected Document
- Retrieval Hit Rate
- Precision
- Recall
- MRR
- NDCG 기초
- Groundedness
- Faithfulness
- Answer Relevance
- Answer Completeness
- Hallucination Check
- Query Rewrite
- Query Expansion
- Chunk Optimization
- Metadata Optimization
- Top-K Optimization
- Similarity Threshold
- Reranking
- Context Optimization
- Failure Case Analysis
- RAG Test Dataset
- RAG Quality Report

제외 범위:

- Vector Database 내부 알고리즘 심화
- Embedding Model 학습
- Fine-Tuning
- Graph RAG 심화
- Agentic RAG 심화
- MLOps 평가 파이프라인 심화
- 대규모 Benchmark 구축 심화

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

# 4. RAG Evaluation Core Rules

RAG Evaluation 문서는 Retrieval과 Generation을 반드시 분리해서 평가한다.

핵심 구조:

```text
User Query
→ Retrieval Evaluation
→ Context Evaluation
→ Generation Evaluation
→ Grounding Check
→ Improvement
```

반드시 설명:

- RAG 실패는 검색 실패와 생성 실패로 나눠 분석
- Retrieval이 실패하면 좋은 LLM도 정확히 답하기 어렵다
- Retrieval이 성공해도 Prompt가 나쁘면 답변이 틀릴 수 있다
- 답변이 맞아 보여도 문서 근거가 없으면 RAG 품질은 낮다
- 평가 결과는 문서 구조 개선에 반영해야 한다

금지:

- 최종 답변만 보고 RAG 품질을 판단
- 검색 결과를 확인하지 않고 모델 문제로 단정
- 정량 평가 없이 감으로 Top-K 조정
- Hallucination을 LLM 문제로만 설명
- 문서 품질과 Chunk 품질을 평가에서 제외

---

# 5. Retrieval Evaluation Rules

Retrieval Evaluation은 사용자의 질문에 맞는 문서가 검색되는지 평가한다.

필수 포함:

- Query
- Retrieved Chunks
- Expected Document
- Expected Chunk
- Top-K Hit
- Retrieval Hit Rate
- Precision
- Recall
- Ranking Quality

기본 Flow:

```text
Golden Query
→ Retrieve Top-K Chunks
→ Check Expected Chunk
→ Score Retrieval
→ Record Failure
```

반드시 설명:

- 기대 문서가 Top-K 안에 포함되는지 확인
- Top-1, Top-3, Top-5 기준 평가 가능
- 검색된 Chunk가 질문 의도와 맞는지 확인
- 관련 없는 Chunk가 많이 섞이면 Precision이 낮음
- 필요한 Chunk가 빠지면 Recall이 낮음

주의:

- 관련 문서가 Top-K에 있어도 순위가 너무 낮으면 품질이 낮을 수 있음
- 문서가 너무 큰 Chunk로 되어 있으면 평가가 애매해짐
- Golden Query가 실제 사용자 질문과 달라지면 평가 의미가 낮아짐

---

# 6. Generation Evaluation Rules

Generation Evaluation은 LLM 답변이 검색 문서를 근거로 올바르게 생성되었는지 평가한다.

필수 포함:

- Answer Correctness
- Groundedness
- Faithfulness
- Relevance
- Completeness
- Citation / Source Match
- Missing Information Handling

기본 Flow:

```text
Retrieved Context
→ Generated Answer
→ Check Evidence
→ Check Hallucination
→ Check Completeness
```

반드시 설명:

- 답변이 문서 근거와 일치하는지 확인
- 문서에 없는 내용을 확정적으로 말하면 Hallucination으로 본다
- 질문에 필요한 핵심 내용을 빠뜨리면 Completeness가 낮다
- 관련 없는 내용을 많이 포함하면 Relevance가 낮다
- 문서에 정보가 없을 때 “부족하다”고 말하는 것도 올바른 답변일 수 있다

주의:

- 정답처럼 보이는 일반 지식 답변도 RAG 근거가 없으면 낮게 평가
- 긴 답변이 항상 좋은 답변은 아님
- Citation이 있어도 실제 내용과 맞는지 확인 필요

---

# 7. Golden Query Rules

Golden Query는 RAG 평가용 기준 질문이다.

필수 포함:

- User-like Query
- Expected Document
- Expected Section
- Expected Answer
- Difficulty
- Domain
- Intent

예시:

```json
{
  "query": "JPA N+1 문제는 어떻게 해결해?",
  "expectedDocument": "Performance_Tuning_Part.md",
  "expectedSection": "N+1 Problem",
  "expectedAnswerKeywords": [
    "Fetch Join",
    "EntityGraph",
    "Batch Size",
    "DTO Projection"
  ]
}
```

반드시 설명:

- Golden Query는 실제 사용자가 물어볼 법한 질문이어야 함
- 각 Query에는 기대 문서와 기대 답변 키워드를 연결
- 쉬운 질문, 모호한 질문, 복합 질문을 모두 포함 가능
- 실패 사례를 Golden Query로 추가하면 품질 개선에 도움

주의:

- 문서 제목 그대로만 묻는 Query는 실제 평가로 부족
- 너무 인위적인 질문만 넣지 말 것
- 기대 문서가 여러 개인 경우 우선순위 정의

---

# 8. Retrieval Hit Rate Rules

Retrieval Hit Rate는 기대 문서가 검색 결과에 포함되는 비율이다.

필수 포함:

- Hit@1
- Hit@3
- Hit@5
- Hit@K
- Expected Chunk
- Retrieval Success

계산 개념:

```text
Hit@K = Expected Document가 Top-K 안에 있으면 성공
```

반드시 설명:

- Hit@K는 RAG 검색의 기본 품질 지표
- Hit@1은 가장 관련 있는 문서가 첫 번째인지 확인
- Hit@5는 필요한 문서가 검색 후보에 포함되는지 확인
- Hit Rate가 낮으면 Query / Chunk / Embedding / Metadata를 점검

주의:

- Hit Rate가 높아도 관련 없는 문서가 많으면 답변 품질이 낮을 수 있음
- Expected Document 정의가 애매하면 평가도 부정확
- 같은 질문의 표현 변형도 테스트 필요

---

# 9. Precision / Recall Rules

Precision과 Recall은 Retrieval 품질을 균형 있게 평가한다.

필수 포함:

- Precision
- Recall
- Relevant Chunk
- Retrieved Chunk
- False Positive
- False Negative

설명:

```text
Precision: 검색된 결과 중 관련 문서 비율
Recall: 필요한 관련 문서 중 검색된 문서 비율
```

반드시 설명:

- Precision이 낮으면 관련 없는 문서가 많이 검색됨
- Recall이 낮으면 필요한 문서가 누락됨
- Top-K를 높이면 Recall은 올라갈 수 있지만 Precision은 낮아질 수 있음
- Chunk 구조와 Query 표현이 Precision / Recall에 영향

주의:

- Precision만 높이면 필요한 문서를 놓칠 수 있음
- Recall만 높이면 Context에 노이즈가 많아질 수 있음
- RAG는 Context Budget 안에서 균형이 중요

---

# 10. Ranking Quality Rules

Ranking Quality는 관련 문서가 얼마나 상위에 배치되는지 평가한다.

필수 포함:

- Ranking
- MRR
- NDCG
- Relevance Score
- Top Rank
- Reranking

기본 개념:

```text
좋은 Retrieval은 관련 문서를 Top-K 안에 넣는 것뿐 아니라 상위에 배치해야 한다.
```

반드시 설명:

- 관련 문서가 Top-1에 가까울수록 좋음
- MRR은 첫 번째 관련 문서의 순위를 평가
- NDCG는 여러 관련 문서의 순위 품질을 평가
- 순위가 불안정하면 Reranking을 고려

주의:

- MRR / NDCG는 기초 개념 중심으로 설명
- 너무 복잡한 수식보다 실무 해석 중심
- 평가 데이터가 충분하지 않으면 수치 해석 주의

---

# 11. Groundedness Rules

Groundedness는 답변이 검색 문서에 근거하는지 평가한다.

필수 포함:

- Grounded Answer
- Evidence Match
- Citation Match
- Unsupported Claim
- Assumption
- Missing Information

기본 Flow:

```text
Answer Claim
→ Check Retrieved Context
→ Supported / Unsupported
→ Mark Groundedness
```

반드시 설명:

- 답변의 주요 주장마다 근거가 있는지 확인
- 문서에 없는 주장은 Unsupported Claim
- 추정은 Assumption으로 표시해야 함
- 문서에 정보가 부족하면 부족하다고 답해야 함

주의:

- 답변이 사실이어도 검색 문서 근거가 없으면 RAG Groundedness는 낮음
- Citation만 붙어 있고 실제 근거가 없으면 잘못된 Citation
- 일반 지식과 문서 근거를 구분

---

# 12. Faithfulness Rules

Faithfulness는 답변이 제공된 Context를 왜곡하지 않는지 평가한다.

필수 포함:

- Faithfulness
- Context Consistency
- Contradiction
- Fabrication
- Misinterpretation

반드시 설명:

- Faithfulness는 답변이 Context와 일치하는 정도
- Context 내용을 과장하거나 바꾸면 Faithfulness가 낮음
- 서로 충돌하는 Context가 있으면 우선순위 기준 필요
- 답변이 Context에 없는 세부사항을 추가하면 문제

주의:

- 요약 과정에서 의미가 바뀌지 않도록 주의
- 코드 설명에서 조건이나 예외를 누락하면 왜곡 가능
- 여러 문서를 합칠 때 충돌 확인 필요

---

# 13. Query Optimization Rules

Query Optimization은 검색 입력을 개선하는 과정이다.

필수 포함:

- Query Rewrite
- Query Expansion
- Keyword Injection
- Domain Term
- Synonym
- Korean / English Term
- Intent Extraction

기본 Flow:

```text
Raw User Query
→ Extract Intent
→ Add Domain Keywords
→ Rewrite Query
→ Retrieve
```

예시:

```text
원본 Query:
"서비스가 너무 커졌어"

개선 Query:
"God Service Application Service Domain Service Facade 책임 분리 Spring Architecture"
```

반드시 설명:

- 짧고 모호한 Query는 검색 실패 가능성이 높음
- Domain Keyword를 보강하면 Retrieval 품질이 좋아질 수 있음
- 한국어 질문에는 영어 기술 용어 병기가 효과적
- Query Rewrite는 원래 의도를 유지해야 함

주의:

- Query를 과도하게 바꾸면 사용자 의도 손상
- 하나의 Query에 너무 많은 개념을 넣으면 검색이 분산됨
- Query Expansion 결과도 평가 필요

---

# 14. Chunk Optimization Rules

Chunk Optimization은 문서 구조를 개선해 Retrieval 품질을 높이는 작업이다.

필수 포함:

- Header Clarity
- Single Concept Chunk
- Chunk Size
- Chunk Overlap
- Code Block Preservation
- FAQ
- Retrieval Queries
- Keyword Placement

기본 Flow:

```text
Failure Query
→ Check Retrieved Chunks
→ Check Missing Chunk
→ Improve Header / FAQ / Keywords
→ Re-embed
→ Re-test
```

반드시 설명:

- 검색 실패는 Chunk 제목과 내용이 불명확해서 발생할 수 있음
- 하나의 Chunk에 여러 개념이 섞이면 검색 의도가 흐려짐
- FAQ는 실제 사용자 질문과 문서를 연결
- Retrieval Queries는 검색 질의 매칭을 강화
- 문서 수정 후 Reindex 필요

주의:

- 키워드 반복만으로 문서 품질을 해결하려 하지 말 것
- Chunk를 너무 잘게 쪼개면 문맥이 부족해짐
- Overlap을 과도하게 늘리면 중복 검색 증가

---

# 15. Metadata Optimization Rules

Metadata Optimization은 필터링과 Agent Routing을 개선한다.

필수 포함:

- Domain
- Level
- Category
- Section
- Source
- Version
- Tags
- UpdatedAt
- Filtered Retrieval

반드시 설명:

- Metadata는 검색 범위 제한에 유용
- Agent별로 필요한 Domain / Level을 필터링할 수 있음
- Version과 UpdatedAt은 최신 문서 우선순위에 도움
- Tags는 유사 문서 구분에 도움

주의:

- Metadata가 틀리면 관련 문서를 제외할 수 있음
- 필터가 너무 강하면 필요한 문서가 누락됨
- 필드명과 값 규칙을 통일

---

# 16. Top-K Optimization Rules

Top-K Optimization은 Context 품질과 Recall의 균형을 맞춘다.

필수 포함:

- Top-K
- Context Budget
- Recall
- Precision
- Noise
- Deduplication
- Reranking

판단 기준:

```text
필요 문서가 누락됨 → Top-K 증가 검토
관련 없는 문서가 많음 → Top-K 감소 / Threshold / Reranking 검토
중복 문서가 많음 → Deduplication 검토
```

반드시 설명:

- Top-K는 평가 결과를 보고 조정
- Top-K가 높으면 필요한 문서가 포함될 가능성은 커짐
- Top-K가 높으면 관련 없는 문서도 섞일 가능성이 커짐
- Context Window와 함께 고려

주의:

- 무조건 Top-K를 크게 하는 것은 좋지 않음
- Chunk 품질이 낮으면 Top-K 조정만으로 해결 어려움
- 검색 결과 정렬 품질도 함께 확인

---

# 17. Context Optimization Rules

Context Optimization은 LLM에 전달할 검색 결과를 정리하는 과정이다.

필수 포함:

- Context Assembly
- Deduplication
- Relevance Ordering
- Source Priority
- Token Budget
- Context Compression
- Conflict Resolution

기본 Flow:

```text
Retrieved Chunks
→ Remove Duplicates
→ Remove Low Relevance
→ Sort by Priority
→ Compress if Needed
→ Build Prompt
```

반드시 설명:

- 검색된 결과를 모두 넣는 것이 항상 좋지 않음
- 중복 Context는 Token 낭비
- 관련도가 낮은 Context는 오답을 유발
- 충돌하는 문서가 있으면 최신성 또는 우선순위 기준 필요
- Context 압축 시 핵심 조건을 유지

주의:

- 핵심 근거를 압축 과정에서 제거하지 말 것
- Context 순서가 답변에 영향을 줄 수 있음
- 오래된 문서가 최신 문서보다 앞서지 않도록 주의

---

# 18. Hallucination Check Rules

Hallucination Check는 RAG 답변 검증에 중요하다.

필수 포함:

- Unsupported Claim
- Fabricated Detail
- Wrong Citation
- Missing Evidence
- Assumption Marking
- Confidence

기본 Flow:

```text
Generated Answer
→ Extract Claims
→ Match Claims with Context
→ Mark Unsupported Claims
→ Revise Answer
```

반드시 설명:

- 답변의 주요 주장마다 근거 확인
- 문서에 없는 클래스명 / 파일명 / 설정값 생성 주의
- 확실하지 않은 내용은 Assumption으로 표시
- 근거가 부족하면 답변을 제한해야 함

주의:

- 문서에 없는 내용을 일반 지식으로 확정하지 말 것
- Citation이 있어도 내용 불일치 확인
- 코드 생성 시 존재하지 않는 프로젝트 구조를 만들지 않도록 주의

---

# 19. RAG Quality Report Rules

RAG Evaluation 문서는 품질 리포트 형식을 포함할 수 있다.

필수 포함:

- Evaluation Date
- Dataset
- Query Count
- Hit@K
- Common Failures
- Improvement Actions
- Retest Result

예시:

```md
# RAG Quality Report

## Summary

- Query Count:
- Hit@3:
- Main Failure:
- Next Action:

## Failure Cases

| Query | Expected | Retrieved | Cause | Fix |
| ----- | -------- | --------- | ----- | --- |
```

반드시 설명:

- 품질 리포트는 개선 전후 비교에 사용
- 실패 원인과 수정 액션을 함께 기록
- 수정 후 반드시 재평가
- Agent가 품질 개선 우선순위를 판단할 수 있게 작성

---

# 20. Troubleshooting Rules

반드시 포함 추천.

형식:

```md
문제:

원인:

해결:
```

---

## Hit Rate가 낮음

문제:

- 기대 문서가 Top-K 안에 들어오지 않음

원인:

- Query와 문서 표현 불일치
- Chunk 제목 불명확
- 핵심 키워드 부족
- Embedding 품질 한계
- Metadata 필터 오류

해결:

- Query Rewrite 적용
- Header / FAQ / Retrieval Queries 보강
- 한글 + 영어 용어 병기
- Metadata 검토
- Reindex 수행

---

## Precision이 낮음

문제:

- 검색 결과에 관련 없는 문서가 많음

원인:

- Top-K 과다
- Chunk에 여러 개념 혼합
- Threshold 낮음
- Metadata Filter 없음

해결:

- Chunk 분리
- Top-K 감소
- Threshold 조정
- Metadata Filter 적용
- Reranking 검토

---

## 답변은 그럴듯한데 근거가 없음

문제:

- 답변이 문서에 근거하지 않음

원인:

- Grounding Rule 부족
- LLM 일반 지식 사용
- Citation 검증 없음

해결:

- 문서 근거 우선 Prompt 추가
- Unsupported Claim 검사
- Citation / Source 확인
- 답변 검증 단계 추가

---

## Query Rewrite 후 검색이 더 나빠짐

문제:

- 원래 질문 의도와 다른 문서가 검색됨

원인:

- Query를 과도하게 확장
- 핵심 의도 손상
- 불필요한 키워드 추가

해결:

- 원본 Query와 Rewrite Query 비교
- 핵심 Intent 유지
- Domain Keyword만 제한적으로 추가
- 여러 Rewrite 후보 테스트

---

## 평가 결과가 매번 달라짐

문제:

- 동일 Query 평가 결과가 불안정함

원인:

- 검색 Index 변경
- 문서 중복
- Reranking 불안정
- 평가 기준 모호

해결:

- 평가 Dataset 고정
- Index 상태 기록
- 중복 문서 제거
- Expected Document 기준 명확화

---

# 21. Best Practice Rules

Best Practice:

- Retrieval과 Generation을 분리 평가
- Golden Query를 실제 사용자 질문 형태로 작성
- Expected Document / Expected Section을 명확히 지정
- Hit@K로 검색 성공 여부 확인
- Precision / Recall 균형 고려
- 답변은 Groundedness와 Faithfulness로 검증
- 실패 Query를 문서 개선에 반영
- Query Rewrite는 원래 의도를 유지
- Chunk 제목과 FAQ를 적극 개선
- Metadata Filter는 과도하게 쓰지 않음
- Top-K는 평가 결과 기반으로 조정
- 수정 후 Reindex와 재평가 수행
- RAG Quality Report로 개선 이력 관리

---

# 22. Comparison Rules

RAG Evaluation 문서는 비교 기준을 포함한다.

필수 비교 대상:

- Retrieval Evaluation vs Generation Evaluation
- Precision vs Recall
- Hit@K vs MRR
- Groundedness vs Faithfulness
- Query Rewrite vs Query Expansion
- Top-K Increase vs Reranking
- Metadata Filter vs Similarity Threshold
- Answer Correctness vs Evidence Support

예시:

| 비교      | Retrieval Evaluation     | Generation Evaluation       |
| --------- | ------------------------ | --------------------------- |
| 평가 대상 | 검색 결과                | 생성 답변                   |
| 핵심 질문 | 필요한 문서를 찾았는가?  | 문서에 근거해 답했는가?     |
| 주요 지표 | Hit@K, Precision, Recall | Groundedness, Faithfulness  |
| 개선 대상 | Chunk, Query, Metadata   | Prompt, Context, Validation |

---

# 23. Checklist Rules

RAG Evaluation 문서에는 Checklist를 포함할 수 있다.

예시:

```md
### [Checklist]

- [ ] Golden Query가 실제 사용자 질문 형태인가?
- [ ] Expected Document가 정의되어 있는가?
- [ ] Hit@K를 확인했는가?
- [ ] Precision / Recall을 구분했는가?
- [ ] 검색 실패 Query를 기록했는가?
- [ ] Chunk 제목을 점검했는가?
- [ ] FAQ / Retrieval Queries를 보강했는가?
- [ ] Metadata Filter가 과도하지 않은가?
- [ ] 답변이 Retrieved Context에 근거하는가?
- [ ] Unsupported Claim을 확인했는가?
- [ ] 수정 후 Reindex 했는가?
- [ ] 재평가 결과를 기록했는가?
```

---

# 24. Retrieval Optimization Rules

강조 대상 키워드:

- RAG Evaluation
- Retrieval Evaluation
- Generation Evaluation
- Golden Query
- Expected Document
- Expected Chunk
- Hit@K
- Retrieval Hit Rate
- Precision
- Recall
- MRR
- NDCG
- Groundedness
- Faithfulness
- Answer Relevance
- Answer Completeness
- Hallucination Check
- Unsupported Claim
- Query Rewrite
- Query Expansion
- Chunk Optimization
- Metadata Optimization
- Top-K Optimization
- Similarity Threshold
- Context Optimization
- Reranking
- RAG Quality Report
- Failure Case Analysis

키워드 반복 허용.

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

예:

- RAG 품질은 어떻게 평가해?
- Retrieval이 실패했는지 어떻게 알아?
- Hit@K가 뭐야?
- Precision과 Recall 차이는?
- Groundedness가 뭐야?
- Faithfulness가 뭐야?
- Query Rewrite는 언제 해?
- Top-K는 어떻게 조정해?
- 검색 결과는 나오는데 답변이 틀리면 어디를 봐?
- Hallucination은 어떻게 확인해?
- RAG 품질 리포트는 어떻게 작성해?

---

# 25. Version Rules

기준:

- Modern RAG Evaluation
- Vector Search 기반 Retrieval
- Markdown RAG Document 기반 평가
- Golden Query 기반 테스트
- Grounded Answer 평가
- Retrieval / Generation 분리 평가
- Query Rewrite / Reranking 확장 가능 구조
- 개인 AI Agent RAG 품질 개선 기준

Legacy 제외:

- 최종 답변만 보고 RAG 품질 판단
- 검색 결과 확인 없는 모델 평가
- 감으로 Top-K 조정
- Grounding 검증 없는 답변 평가
- 실패 사례 기록 없는 RAG 운영

---

# 26. Common Mistakes

자주 발생:

- Retrieval과 Generation 실패를 구분하지 않음
- Golden Query 없이 감으로 평가
- 문서가 검색됐는지 확인하지 않음
- Hit@K만 보고 Precision을 무시
- 답변이 맞아 보이면 근거 검증을 생략
- Query Rewrite가 사용자 의도를 바꿈
- Top-K를 무조건 크게 설정
- Chunk 구조 문제를 모델 문제로 오해
- Metadata Filter를 너무 강하게 적용
- 문서 수정 후 Reindex를 하지 않음
- 실패 사례를 기록하지 않음
- 개선 후 재평가하지 않음

---

# 27. Final Goal

RAG Evaluation & Retrieval Optimization RAG 문서는 Agent가 아래를 수행 가능해야 한다.

- RAG 품질 평가 기준 설명
- Retrieval / Generation 실패 구분
- Golden Query 설계
- Hit@K / Precision / Recall 해석
- Groundedness / Faithfulness 검증
- Hallucination 원인 분석
- Query Rewrite 적용 여부 판단
- Chunk / Metadata 개선 방향 제안
- Top-K / Threshold 조정 기준 제안
- Context Optimization 방향 제안
- RAG Quality Report 작성
- 실패 사례 기반 문서 개선
- Reindex / Retest 필요 여부 판단

문서 품질이 RAG 시스템 개선 속도와 Agent 답변 신뢰도를 결정한다.

---

# Retrieval Queries

### [FAQ]

Q. RAG 품질은 어떻게 평가해?

A.
Retrieval이 필요한 문서를 찾았는지와 Generation이 문서 근거에 맞게 답했는지를 분리해서 평가한다.

Q. Retrieval Evaluation은 뭐야?

A.
사용자 Query에 대해 기대 문서나 기대 Chunk가 검색 결과에 포함되는지 평가하는 것이다.

Q. Generation Evaluation은 뭐야?

A.
LLM 답변이 Retrieved Context에 근거하고 질문에 맞게 생성되었는지 평가하는 것이다.

Q. Golden Query가 뭐야?

A.
RAG 검색 품질을 테스트하기 위해 미리 정의한 기준 질문이다.

Q. Expected Document는 뭐야?

A.
특정 Golden Query가 검색해야 하는 기대 문서 또는 기대 Section이다.

Q. Hit@K가 뭐야?

A.
기대 문서가 Top-K 검색 결과 안에 포함되는지 확인하는 지표다.

Q. Precision과 Recall 차이는?

A.
Precision은 검색된 결과 중 관련 문서 비율이고, Recall은 필요한 관련 문서 중 검색된 비율이다.

Q. MRR은 뭐야?

A.
첫 번째 관련 문서가 검색 결과에서 얼마나 상위에 있는지 평가하는 지표다.

Q. Groundedness가 뭐야?

A.
답변의 주요 내용이 검색된 문서에 근거하고 있는지 평가하는 기준이다.

Q. Faithfulness가 뭐야?

A.
답변이 제공된 Context를 왜곡하지 않고 충실하게 반영하는지 평가하는 기준이다.

Q. 답변이 맞아 보이면 평가 통과야?

A.
아니다. RAG에서는 답변이 검색 문서에 근거하는지도 확인해야 한다.

Q. 검색 결과는 맞는데 답변이 틀리면 어디를 봐야 해?

A.
RAG Prompt, Context Assembly, Grounding Rule, 답변 검증 과정을 확인한다.

Q. 문서에 있는데 검색이 안 되면 어떻게 해?

A.
Chunk 제목, FAQ, Retrieval Queries, 핵심 키워드, Metadata, Reindex 여부를 확인한다.

Q. Query Rewrite는 언제 해?

A.
사용자 질문이 짧거나 모호해서 검색 의도가 잘 드러나지 않을 때 사용한다.

Q. Query Expansion은 뭐야?

A.
원래 질문에 관련 Domain Keyword나 동의어를 추가해 검색 품질을 높이는 방법이다.

Q. Top-K는 어떻게 조정해?

A.
필요 문서가 누락되면 늘리고, 관련 없는 문서가 많으면 줄이거나 Threshold / Reranking을 적용한다.

Q. Similarity Threshold는 언제 조정해?

A.
관련 없는 문서가 많이 검색되거나 검색 결과가 너무 자주 비어 있을 때 조정한다.

Q. Hallucination은 어떻게 확인해?

A.
답변의 주요 주장을 Retrieved Context와 대조해 근거 없는 내용을 찾는다.

Q. RAG Quality Report는 왜 필요해?

A.
검색 실패 원인, 개선 조치, 재평가 결과를 기록해 RAG 품질 개선 이력을 관리하기 위해 필요하다.

Q. RAG 개선 후 무엇을 해야 해?

A.
문서를 수정했다면 Reindex하고, 같은 Golden Query로 재평가해 개선 여부를 확인해야 한다.
