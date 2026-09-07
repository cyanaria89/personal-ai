# Vector Database & RAG Domain Rules

---

# 1. Domain Purpose

Vector Database & RAG Domain 문서는 AI Agent / RAG Agent / Backend Agent / Review Agent용 RAG 문서 제작 규칙이다.

목적:

- Vector Database 기본 개념 이해
- RAG 구조 설계 지원
- Document Ingestion Pipeline 기준 제공
- Chunk / Embedding / Index / Retrieval 흐름 설명
- Vector Search 기반 Context Retrieval 지원
- RAG Prompt Assembly 기준 제공
- Retrieval 실패 / Hallucination 문제 분석 지원
- RAG System Review 기준 제공

우선순위:

1. RAG Core Concept
2. Document Ingestion Quality
3. Chunk / Embedding / Metadata Quality
4. Retrieval Accuracy
5. Context Assembly
6. Grounded Answer
7. Evaluation / Troubleshooting

---

# 2. Scope

포함 범위:

- RAG Core
- Vector Database
- Document Ingestion
- Document Loader
- Text Splitter
- Chunking
- Embedding
- Vector Index
- Metadata
- Vector Search
- Similarity Search
- Hybrid Search 기초
- Reranking 기초
- Top-K Retrieval
- Context Assembly
- Grounded Generation
- Citation / Source Reference
- Missing Information Rule
- RAG Evaluation
- RAG Troubleshooting
- ChromaDB
- FAISS
- Qdrant
- Milvus
- Pinecone
- AnythingLLM / Ollama 연동 개념

제외 범위:

- Vector Database 내부 ANN 알고리즘 심화
- HNSW 상세 튜닝 심화
- Graph RAG 심화
- Agentic RAG 심화
- Fine-Tuning
- Embedding Model 학습
- Production MLOps 상세
- 대규모 검색 엔진 운영 상세

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

# 4. RAG Core Rules

RAG 문서는 Retrieval과 Generation을 분리해서 설명한다.

반드시 포함:

- RAG는 Retrieval-Augmented Generation
- 외부 문서를 검색해 LLM Context로 넣는 구조
- LLM 자체 지식이 아니라 Retrieved Context를 근거로 답변
- Retrieval 품질이 답변 품질을 결정
- 문서에 없는 내용은 없다고 말해야 함
- RAG는 Hallucination을 줄일 수 있지만 완전히 제거하지는 못함

기본 Flow:

```text
User Query
→ Retrieve Relevant Documents
→ Build Context
→ LLM Generate Answer
→ Validate Grounding
```

금지:

- RAG를 단순 파일 업로드 기능으로 설명
- Vector DB만 있으면 정확한 답변이 나온다는 설명
- LLM이 문서에 없는 내용을 보완해도 된다는 설명
- Retrieval 실패를 항상 LLM 문제로 판단

---

# 5. Vector Database Rules

Vector Database는 Embedding Vector를 저장하고 검색하는 저장소로 설명한다.

필수 포함:

- Vector Database
- Vector Index
- Embedding Vector
- Similarity Search
- Metadata
- Collection
- Upsert
- Delete
- Reindex
- Query

기본 Flow:

```text
Document Chunk
→ Embedding
→ Vector + Metadata
→ Vector Database
→ Similarity Search
```

반드시 설명:

- Vector Database는 의미 기반 검색을 위한 저장소
- 원문 Text, Vector, Metadata 연결이 중요
- Embedding Model과 Vector Dimension이 일치해야 함
- 문서 변경 시 Vector 재생성 / Reindex 필요
- Metadata는 필터링과 출처 추적에 사용

주의:

- Vector만 저장하고 원문을 잃지 말 것
- 서로 다른 Embedding Model Vector를 같은 Collection에서 혼합 금지
- Metadata 누락은 답변 근거 추적을 어렵게 함
- Delete / Update 정책이 없으면 오래된 문서가 검색될 수 있음

---

# 6. Document Ingestion Rules

Document Ingestion은 RAG 품질의 시작점이다.

필수 포함:

- Document Source
- Loader
- Preprocessing
- Chunking
- Embedding
- Metadata Attach
- Vector Store Upsert
- Validation

기본 Flow:

```text
Raw Document
→ Load
→ Clean
→ Split into Chunks
→ Add Metadata
→ Generate Embedding
→ Store in Vector DB
→ Validate Retrieval
```

반드시 설명:

- 문서 적재 전 구조와 품질을 확인
- Markdown Header는 Chunk 경계로 활용 가능
- Code Block은 깨지지 않도록 처리
- 문서 출처와 버전 정보를 Metadata로 저장
- Ingestion 후 샘플 Query로 검색 검증

주의:

- 문서만 업로드하고 검색 품질 검증을 생략하지 말 것
- 중복 문서 적재 주의
- 오래된 문서와 최신 문서 충돌 관리
- 문서 수정 후 재색인 누락 주의

---

# 7. Document Preprocessing Rules

Document Preprocessing은 검색 가능한 형태로 문서를 정리하는 과정이다.

필수 포함:

- Text Cleaning
- Header Normalization
- Code Block Preservation
- Table Handling
- Link Handling
- Duplicate Removal
- Noise Removal
- Encoding

반드시 설명:

- 불필요한 서론, 목차 반복, 광고성 문구는 검색 품질을 떨어뜨릴 수 있음
- Header는 검색과 Chunking에 중요
- Code Block과 설명의 연결 유지 필요
- 표는 의미가 유지되도록 Markdown Table 또는 구조화 텍스트로 보존
- 한글 문서는 Encoding 문제를 확인

주의:

- 전처리 중 핵심 문맥 삭제 금지
- Code Block 내부 문법 훼손 금지
- 너무 과한 정제는 의미 손실 가능
- 원본 파일 백업 권장

---

# 8. Chunking Rules

Chunking은 Vector Database & RAG 문서의 핵심이다.

필수 포함:

- Chunk
- Chunk Size
- Chunk Overlap
- Semantic Chunking
- Header Based Chunking
- Code Block Preservation
- FAQ Chunk
- Retrieval Queries Chunk

기본 Flow:

```text
Markdown Document
→ Header Split
→ Semantic Boundary Check
→ Chunk Size Check
→ Add Overlap if Needed
→ Save Chunk
```

반드시 설명:

- Chunk는 검색의 최소 단위
- Chunk는 독립적으로 검색되어도 의미를 가져야 함
- 하나의 Chunk에는 하나의 핵심 개념만 포함
- Code Example과 설명은 가능하면 같은 Chunk에 유지
- FAQ와 Retrieval Queries는 실제 질문 매칭에 유리

주의:

- Code Block 중간 분리 금지
- 여러 주제를 하나의 Chunk에 섞지 말 것
- 너무 작은 Chunk는 문맥 부족
- 너무 큰 Chunk는 검색 정밀도 저하
- Overlap 과다는 중복 검색 유발

---

# 9. Metadata Rules

Metadata는 RAG 검색과 Agent Routing에 중요하다.

필수 포함:

- source
- fileName
- documentId
- chunkId
- domain
- level
- category
- section
- title
- tags
- version
- updatedAt

예시:

```json
{
  "documentId": "springboot-part01",
  "chunkId": "springboot-part01-003",
  "domain": "Backend",
  "level": "Foundation",
  "section": "Service Layer",
  "tags": ["spring-boot", "service", "transaction"]
}
```

반드시 설명:

- Metadata는 검색 결과의 출처를 보존
- Domain / Level / Section은 Agent가 문서를 해석하는 데 도움
- Chunk ID는 추적과 업데이트에 필요
- Filtered Search에 Metadata 사용 가능

주의:

- Metadata 필드명 통일
- 잘못된 Metadata는 잘못된 문서 검색을 유발
- 문서 업데이트 시 Metadata도 함께 갱신
- Source 없는 Chunk는 근거 제시가 어려움

---

# 10. Embedding Storage Rules

Embedding Storage는 Vector와 원문 연결 기준을 포함한다.

필수 포함:

- Embedding Vector
- Original Text
- Metadata
- Vector Dimension
- Embedding Model Name
- Collection Name
- Upsert Policy
- Reindex Policy

반드시 설명:

- Vector는 반드시 원문 Text와 연결되어야 함
- Embedding Model 이름과 버전 기록 권장
- Collection은 Domain / Project / Version 기준으로 나눌 수 있음
- 같은 Collection에는 같은 Embedding Model 사용 권장

주의:

- Embedding Model 변경 시 기존 Vector 재사용 금지
- Vector Dimension 불일치 주의
- 오래된 Chunk가 남지 않도록 Delete / Reindex 정책 필요
- 중복 Upsert 방지 필요

---

# 11. Retrieval Rules

Retrieval은 사용자 Query와 관련 있는 Chunk를 찾는 과정이다.

필수 포함:

- Query
- Query Embedding
- Similarity Search
- Top-K
- Similarity Threshold
- Metadata Filter
- Reranking
- Retrieved Context

기본 Flow:

```text
User Query
→ Query Embedding
→ Vector Search
→ Metadata Filter
→ Rerank
→ Select Context
```

반드시 설명:

- Retrieval은 RAG 답변 품질의 핵심
- Top-K와 Threshold는 Context 품질에 영향
- Metadata Filter는 검색 범위를 줄이는 데 유용
- Reranking은 최종 관련도 개선에 도움
- 검색 결과는 LLM에 넣기 전 정리 필요

주의:

- 관련 없는 Chunk를 많이 넣으면 답변 품질 저하
- 검색 결과가 없을 때 fallback 규칙 필요
- 검색 결과 중복 제거 필요
- Score만 보고 무조건 채택하지 말 것

---

# 12. Top-K / Threshold Rules

Top-K와 Threshold는 Retrieval 범위 제어 기준이다.

필수 포함:

- Top-K
- Similarity Threshold
- Precision
- Recall
- Context Budget
- Low Confidence

비교:

| 설정           | 장점           | 단점                     |
| -------------- | -------------- | ------------------------ |
| Top-K 낮음     | 정밀도 증가    | 필요한 문서 누락 가능    |
| Top-K 높음     | 재현율 증가    | 관련 없는 문서 포함 가능 |
| Threshold 높음 | 무관 문서 제거 | 검색 실패 가능           |
| Threshold 낮음 | 검색 결과 확보 | 노이즈 증가              |

반드시 설명:

- Top-K는 가져올 Chunk 수
- Threshold는 최소 관련도 기준
- 둘 다 문서 품질과 Query 특성에 따라 조정
- Context Window와 함께 고려해야 함

주의:

- 고정값이 항상 정답은 아님
- Top-K를 키우기 전에 Chunk 구조 점검
- Threshold가 높으면 “문서에 없음”이 자주 발생 가능
- 낮은 Score라도 중요한 문서일 수 있음

---

# 13. Hybrid Search Rules

Hybrid Search는 Keyword Search와 Vector Search를 조합한다.

필수 포함:

- Keyword Search
- BM25
- Semantic Search
- Dense Retrieval
- Sparse Retrieval
- Score Fusion
- Exact Term Matching

적합한 경우:

- 에러 메시지 검색
- 클래스명 / 메서드명 검색
- API Endpoint 검색
- 기술 용어 검색
- 개념 질문 검색

반드시 설명:

- Vector Search는 의미 검색에 강함
- Keyword Search는 정확한 용어 검색에 강함
- 기술 문서는 둘을 함께 쓰면 품질이 좋아질 수 있음
- Score 결합과 중복 제거 기준 필요

주의:

- Hybrid Search는 시스템 복잡도 증가
- 두 검색 결과가 충돌할 수 있음
- Keyword 검색 품질도 문서 용어 통일에 의존

---

# 14. Reranking Rules

Reranking은 1차 검색 결과를 재정렬하는 단계이다.

필수 포함:

- Reranker
- Cross Encoder
- Candidate Chunk
- Relevance Score
- Final Ranking
- Latency Cost

기본 Flow:

```text
Vector Search Top-20
→ Reranker
→ Final Top-5
→ Context Assembly
```

반드시 설명:

- Reranking은 검색 결과 순서를 개선
- 1차 검색에서 넓게 가져오고 Reranker가 정밀하게 판단
- 품질은 좋아질 수 있지만 Latency 증가
- 중요한 답변 품질이 필요한 RAG에 적합

주의:

- Reranker가 Chunk 품질 문제를 완전히 해결하지는 못함
- 후보 수가 많으면 비용 증가
- 실시간 응답에서는 Latency 고려

---

# 15. Context Assembly Rules

Context Assembly는 검색 결과를 LLM Prompt에 넣는 과정이다.

필수 포함:

- Retrieved Chunks
- Context Order
- Source
- Deduplication
- Compression
- Conflict Handling
- Token Budget
- Prompt Template

기본 Flow:

```text
Retrieved Chunks
→ Remove Duplicates
→ Sort by Relevance / Priority
→ Trim to Token Budget
→ Add Source Metadata
→ Build Prompt Context
```

반드시 설명:

- 검색된 Chunk를 그대로 모두 넣지 않을 수 있음
- 중복과 관련 없는 내용을 제거
- Source / Section 정보 포함 권장
- Token Budget 안에서 핵심 문맥을 유지
- 충돌하는 문서가 있으면 최신성 / 우선순위 기준 필요

주의:

- 관련 없는 Context가 많으면 LLM이 오답 생성 가능
- 출처 없는 Context는 검증 어려움
- Context 압축 과정에서 핵심 조건 삭제 주의
- 긴 Code Block은 필요한 부분만 넣을 수 있음

---

# 16. Grounded Generation Rules

Grounded Generation은 검색 문서를 근거로 답변하는 규칙이다.

필수 포함:

- Grounded Answer
- Retrieved Context
- Evidence
- Citation / Source Reference
- Missing Information Rule
- Assumption
- Uncertainty

기본 규칙:

```text
Use retrieved context first.
If the context does not contain enough information, say what is missing.
Do not invent project-specific facts.
Separate evidence-based answer from assumptions.
```

반드시 설명:

- RAG 답변은 검색 문서를 근거로 해야 함
- 문서에 없는 내용은 없다고 표현
- 일반 지식으로 보완할 경우 추정임을 표시
- 답변에 사용한 근거 Chunk를 추적 가능해야 함

주의:

- 검색 결과에 없는 내용을 확정적으로 말하지 말 것
- 문서 간 충돌 시 우선순위 필요
- 근거 없는 코드 생성 주의
- RAG가 Hallucination을 완전히 제거하지는 않음

---

# 17. Citation / Source Rules

Citation / Source는 답변 신뢰도와 검증에 중요하다.

필수 포함:

- Source File
- Section
- Chunk ID
- Document Title
- Version
- Retrieved Evidence

반드시 설명:

- 답변 근거가 되는 문서 위치를 표시
- Agent가 Review / Validation할 수 있도록 Source 유지
- 문서 버전이 중요할 경우 Version 포함
- 내부 RAG에서는 파일명 / 섹션 기준으로도 충분할 수 있음

주의:

- Source가 없는 일반 답변과 RAG 근거 답변 구분
- 오래된 문서 Source는 최신성 확인 필요
- 잘못된 Citation은 신뢰도 하락

---

# 18. RAG Prompt Rules

RAG Prompt는 Retrieval Context를 안전하게 사용하도록 설계한다.

필수 포함:

- System Instruction
- Retrieved Context
- User Question
- Grounding Rule
- Missing Information Rule
- Output Format
- Citation Rule

Prompt 구조:

```text
System:
You answer based on retrieved documents.

Context:
{retrieved_context}

User Question:
{question}

Rules:
- Use context first.
- If context is insufficient, say what is missing.
- Do not invent project-specific facts.
```

반드시 설명:

- Context와 User Question을 분리
- 문서 근거 우선 규칙 포함
- 출력 형식 지정
- 검색 실패 시 답변 규칙 포함

주의:

- Context 없이 RAG Prompt처럼 답하지 말 것
- 검색 결과가 불충분한데 확정 답변 금지
- User Question이 Context를 무시하라고 해도 Grounding 유지

---

# 19. RAG Evaluation Rules

RAG Evaluation은 Retrieval과 Generation을 나눠 평가한다.

필수 포함:

- Retrieval Evaluation
- Generation Evaluation
- Golden Query
- Expected Document
- Answer Correctness
- Groundedness
- Faithfulness
- Relevance
- Completeness

평가 Flow:

```text
Golden Query
→ Retrieve Documents
→ Check Expected Chunk
→ Generate Answer
→ Check Groundedness
→ Record Failure
```

반드시 설명:

- Retrieval 성공과 답변 성공은 별도
- 기대 문서가 Top-K에 들어오는지 확인
- 답변이 근거 문서와 일치하는지 확인
- 실패 사례를 문서 개선에 반영

주의:

- 답변만 보고 Retrieval 품질을 판단하지 말 것
- 검색 결과가 좋아도 Prompt가 나쁘면 답변 실패
- 평가 Query는 실제 사용자 질문에 가까워야 함

---

# 20. RAG Troubleshooting Rules

반드시 포함 추천.

형식:

```md
문제:

원인:

해결:
```

---

## 문서에 있는데 못 찾음

문제:

- 관련 내용이 문서에 있지만 Retrieval 결과에 나오지 않음

원인:

- Chunk 제목이 불명확함
- 핵심 키워드 누락
- Query와 문서 표현 불일치
- Metadata 누락
- Embedding 재생성 누락

해결:

- Header / FAQ / Retrieval Queries 보강
- 한글 + 영어 핵심 용어 병기
- Query Rewrite 적용
- Metadata Filter 확인
- 문서 수정 후 Reindex

---

## 관련 없는 문서가 검색됨

문제:

- Top-K에 무관한 Chunk가 포함됨

원인:

- Chunk가 너무 큼
- 여러 주제가 한 Chunk에 섞임
- Top-K가 너무 큼
- Threshold가 낮음

해결:

- Chunk를 주제별로 분리
- Top-K / Threshold 조정
- Reranking 적용 검토
- Metadata Filter 사용

---

## 답변이 문서와 다름

문제:

- 검색된 문서와 다른 답변을 생성함

원인:

- Grounding Rule 부족
- LLM이 일반 지식으로 보완
- Context가 불충분함
- 충돌하는 문서가 포함됨

해결:

- RAG Prompt에 문서 근거 우선 규칙 추가
- Missing Information Rule 추가
- Context 충돌 제거
- 답변 검증 단계 추가

---

## 오래된 문서가 검색됨

문제:

- 최신 문서가 아닌 이전 문서 기준으로 답변함

원인:

- Reindex 누락
- 오래된 Vector 삭제 안 됨
- Version Metadata 없음
- 중복 문서 존재

해결:

- 기존 Vector 삭제 후 재색인
- version / updatedAt Metadata 추가
- 중복 문서 제거
- 최신 문서 우선순위 적용

---

## Context가 너무 길어짐

문제:

- 검색 결과를 Prompt에 넣을 때 Token 초과 또는 답변 품질 저하 발생

원인:

- Top-K 과다
- Chunk가 너무 큼
- 중복 Context 많음
- 관련 없는 문서 포함

해결:

- Top-K 조정
- Deduplication
- Context Compression
- Reranking
- 핵심 Section만 포함

---

# 21. Best Practice Rules

Best Practice:

- RAG는 Retrieval과 Generation을 분리해서 설계
- Markdown Header 기반 Chunking 권장
- Chunk는 하나의 개념 중심으로 작성
- Metadata에 domain / level / section / source 포함
- Embedding Model 이름과 버전 기록
- 문서 수정 후 Reindex
- Top-K는 평가 기반으로 조정
- Context는 중복 제거 후 조립
- RAG Prompt에는 Grounding Rule 포함
- 문서에 없는 내용은 없다고 답변
- Golden Query로 검색 품질 테스트
- 실패 사례를 문서 개선에 반영

---

# 22. Comparison Rules

Vector Database & RAG 문서는 비교 기준을 포함한다.

필수 비교 대상:

- Keyword Search vs Vector Search
- Vector Search vs Hybrid Search
- Retrieval vs Generation
- Embedding Model vs Chat Model
- Chunk Size Small vs Large
- Top-K vs Threshold
- Reranking vs No Reranking
- Local Vector DB vs Managed Vector DB

예시:

| 비교      | Retrieval             | Generation                 |
| --------- | --------------------- | -------------------------- |
| 역할      | 관련 문서 검색        | 답변 생성                  |
| 입력      | User Query            | Retrieved Context + Prompt |
| 출력      | Document Chunks       | Natural Language Answer    |
| 실패 원인 | 검색 품질, Chunk 문제 | Prompt 문제, Hallucination |

---

# 23. Checklist Rules

Vector Database & RAG 문서에는 Checklist를 포함할 수 있다.

예시:

```md
### [Checklist]

- [ ] 문서 Source가 명확한가?
- [ ] Chunk가 하나의 개념만 다루는가?
- [ ] Code Block이 깨지지 않았는가?
- [ ] Metadata가 포함되어 있는가?
- [ ] Embedding Model 이름을 기록했는가?
- [ ] Vector Dimension이 일치하는가?
- [ ] Top-K 기준이 있는가?
- [ ] Context 중복 제거를 수행하는가?
- [ ] Grounding Rule이 Prompt에 있는가?
- [ ] 문서에 없는 내용 처리 규칙이 있는가?
- [ ] Reindex 기준이 정의되어 있는가?
```

---

# 24. Retrieval Optimization Rules

강조 대상 키워드:

- RAG
- Retrieval-Augmented Generation
- Vector Database
- Vector Store
- Vector Search
- Similarity Search
- Document Ingestion
- Document Loader
- Text Splitter
- Chunking
- Chunk Size
- Chunk Overlap
- Embedding
- Metadata
- Vector Index
- Collection
- Top-K Retrieval
- Similarity Threshold
- Hybrid Search
- Reranking
- Context Assembly
- Grounded Generation
- Citation
- Source Reference
- Missing Information Rule
- RAG Evaluation
- Golden Query
- Reindex
- ChromaDB
- FAISS
- Qdrant
- Milvus
- Pinecone

키워드 반복 허용.

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

예:

- RAG가 뭐야?
- Vector Database는 뭐에 써?
- Vector DB랑 일반 DB 차이는?
- RAG 문서는 어떻게 적재해?
- Chunking은 왜 중요해?
- Metadata는 왜 필요해?
- Top-K는 어떻게 정해?
- RAG 답변이 틀릴 때 어디를 봐야 해?
- 문서 수정 후 재색인해야 해?
- 검색 결과가 이상하면 어떻게 해?
- RAG Prompt는 어떻게 만들어?

---

# 25. Version Rules

기준:

- Modern RAG
- Vector Database 기반 Retrieval
- Markdown 기반 RAG Document
- Embedding Model 기반 Semantic Search
- Metadata Filter 활용 가능 구조
- Hybrid Search / Reranking 확장 가능성 고려
- Local LLM / Local Embedding 연동 가능성 고려
- AnythingLLM / Ollama 기반 개인 AI 서버 구조 고려

Legacy 제외:

- 문서 전체를 하나의 Context로 넣는 방식
- Chunking 없이 전체 문서 Embedding
- Metadata 없이 Vector만 저장
- 문서 근거 없이 LLM 일반 지식으로 답변하는 방식
- Reindex 정책 없는 문서 운영

---

# 26. Common Mistakes

자주 발생:

- 문서 업로드 후 검색 검증을 하지 않음
- Chunk가 너무 크거나 작음
- Code Block이 중간에 잘림
- Metadata 누락
- Embedding Model 변경 후 기존 Vector 재사용
- 문서 수정 후 Reindex 누락
- 오래된 문서 Vector 삭제 안 함
- Top-K를 무조건 크게 설정
- 관련 없는 Context를 너무 많이 넣음
- RAG Prompt에 Grounding Rule 없음
- 문서에 없는 내용을 LLM이 일반 지식으로 답변
- Retrieval 실패를 문서 품질 문제가 아니라 모델 문제로만 판단

---

# 27. Final Goal

Vector Database & RAG RAG 문서는 Agent가 아래를 수행 가능해야 한다.

- RAG 구조 설명
- Vector Database 역할 설명
- Document Ingestion Pipeline 설계
- Chunking 기준 제안
- Metadata 설계 기준 제안
- Embedding 저장 기준 설명
- Retrieval / Top-K / Threshold 기준 설명
- Context Assembly 방식 제안
- Grounded Generation Prompt 설계
- RAG 답변 오류 원인 분석
- Reindex 필요 여부 판단
- RAG Evaluation 기준 제안
- RAG 시스템 Review
- Troubleshooting Direction 제안

문서 품질이 RAG 검색 품질과 Agent 답변 품질을 결정한다.

---

# Retrieval Queries

### [FAQ]

Q. RAG가 뭐야?

A.
RAG는 외부 문서를 검색한 뒤 그 문서를 LLM Context로 넣어 답변을 생성하는 구조다.

Q. Vector Database는 뭐에 써?

A.
Embedding Vector를 저장하고 사용자 질문과 의미적으로 가까운 문서 Chunk를 검색하는 데 사용한다.

Q. Vector DB랑 일반 DB 차이는?

A.
일반 DB는 주로 정확한 값과 조건 검색에 강하고, Vector DB는 의미 유사도 기반 검색에 강하다.

Q. RAG에서 Retrieval과 Generation 차이는?

A.
Retrieval은 관련 문서를 찾는 단계이고, Generation은 찾은 문서를 바탕으로 답변을 생성하는 단계다.

Q. Document Ingestion은 뭐야?

A.
원본 문서를 읽고 정리한 뒤 Chunking, Embedding, Metadata 저장을 거쳐 Vector DB에 적재하는 과정이다.

Q. Chunking은 왜 중요해?

A.
Chunk가 검색 단위가 되기 때문에 Chunk가 나쁘면 관련 문서가 있어도 검색되지 않을 수 있다.

Q. Metadata는 왜 필요해?

A.
문서 출처, 도메인, 섹션, 버전을 추적하고 검색 필터링에 사용하기 위해 필요하다.

Q. Top-K는 어떻게 정해?

A.
필요한 문서가 누락되지 않으면서 관련 없는 문서가 과도하게 섞이지 않도록 평가 기반으로 조정한다.

Q. Similarity Threshold는 왜 써?

A.
관련도가 낮은 문서가 Context에 들어가는 것을 줄이기 위해 사용한다.

Q. Hybrid Search는 언제 필요해?

A.
에러명, 클래스명, API 경로 같은 정확한 키워드와 개념 검색이 모두 중요할 때 사용한다.

Q. Reranking은 언제 써?

A.
1차 검색 결과는 나오지만 관련도 순서가 부정확하거나 무관한 문서가 섞일 때 사용한다.

Q. Context Assembly는 뭐야?

A.
검색된 Chunk를 중복 제거, 정렬, 압축한 뒤 LLM Prompt에 넣을 Context로 구성하는 과정이다.

Q. Grounded Answer는 뭐야?

A.
검색된 문서를 근거로 답변하고, 문서에 없는 내용은 추정하거나 없다고 표시하는 답변이다.

Q. RAG Prompt에는 뭐가 들어가야 해?

A.
Retrieved Context, User Question, Grounding Rule, Missing Information Rule, Output Format이 들어가야 한다.

Q. 문서에 있는데 못 찾으면 어떻게 해?

A.
Chunk 제목, 핵심 키워드, FAQ, Retrieval Queries, Metadata, Embedding 재생성 여부를 확인한다.

Q. RAG 답변이 문서와 다르면 어떻게 해?

A.
Grounding Rule을 강화하고, 검색 Context를 정리하며, 답변 검증 단계를 추가한다.

Q. 문서를 수정하면 재색인해야 해?

A.
해야 한다. 문서 내용이 바뀌면 기존 Embedding Vector가 오래된 내용을 가리킬 수 있다.

Q. 오래된 문서가 검색되면 어떻게 해?

A.
이전 Vector를 삭제하고 재색인하며, version 또는 updatedAt Metadata를 추가한다.

Q. RAG Evaluation은 어떻게 해?

A.
Golden Query를 만들고 기대 문서가 Top-K에 들어오는지, 답변이 문서 근거와 일치하는지 확인한다.

Q. RAG 품질을 높이려면 뭐부터 봐야 해?

A.
Chunk 구조, Metadata, Embedding Model, Top-K, RAG Prompt, Grounding Rule을 순서대로 확인한다.
