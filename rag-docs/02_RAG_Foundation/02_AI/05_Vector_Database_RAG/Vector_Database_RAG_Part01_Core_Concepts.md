# Vector Database & RAG Part01 Core Concepts

---

# 1. RAG Core Concept

## 1.1 RAG Definition

### [개념]

RAG는 Retrieval-Augmented Generation의 약자다.

RAG는 LLM이 자체 지식만으로 답변하지 않고, 외부 문서를 검색한 뒤 검색된 문서를 Context로 사용하여 답변을 생성하는 구조다.

RAG의 핵심은 두 단계로 분리된다.

```text
Retrieval
→ Generation
```

Retrieval은 사용자 질문과 관련 있는 문서 Chunk를 찾는 단계다.

Generation은 Retrieved Context를 기반으로 LLM이 답변을 생성하는 단계다.

RAG는 문서를 업로드하는 기능이 아니라, 검색된 문서를 근거로 답변을 생성하는 아키텍처다.

---

### [핵심]

- RAG = Retrieval-Augmented Generation
- RAG는 외부 문서를 검색해 LLM Context로 넣는 구조
- Retrieval 품질이 답변 품질을 결정
- Generation은 Retrieved Context 기반으로 수행
- 문서에 없는 내용은 없다고 말해야 함
- RAG는 Hallucination을 줄일 수 있지만 완전히 제거하지는 못함
- Retrieval 실패와 Generation 실패는 분리해서 분석해야 함

---

### [실무]

2026 실무 기준 RAG 시스템은 단순 Q&A 챗봇이 아니라, Agent가 문서를 검색하고 근거 기반으로 판단하는 Knowledge Retrieval Layer로 사용된다.

개인 AI 서버에서 RAG는 Backend Agent, Frontend Agent, Review Agent, DevOps Agent, AI Agent가 공통으로 참조하는 지식 기반이 된다.

RAG 문서는 사람이 읽기 좋은 학습 문서보다 검색이 잘 되는 구조가 중요하다.

실무 RAG 설계에서는 다음 기준을 우선한다.

- Chunk가 독립적으로 검색 가능한가
- 질문 표현과 문서 표현이 매칭되는가
- Metadata로 Domain / Level / Section을 필터링할 수 있는가
- 검색된 Context가 답변 근거로 충분한가
- 문서에 없는 내용을 LLM이 생성하지 않도록 제어하는가

---

### [FAQ]

Q. RAG가 뭐야?

A.
외부 문서를 검색한 뒤 검색된 문서를 LLM Context로 넣어 답변을 생성하는 구조다.

Q. RAG는 파일 업로드 기능이야?

A.
아니다. 파일 업로드는 Ingestion의 일부일 뿐이고, RAG의 핵심은 Retrieval과 Grounded Generation이다.

Q. RAG를 쓰면 Hallucination이 없어져?

A.
완전히 없어지지는 않는다. 다만 검색된 문서 근거를 사용하면 Hallucination을 줄일 수 있다.

Q. RAG 답변 품질은 무엇이 결정해?

A.
Document Quality, Chunk Quality, Metadata, Embedding, Retrieval, Prompt가 함께 결정한다.

Q. RAG에서 가장 먼저 봐야 할 문제는 뭐야?

A.
Retrieval 결과다. 관련 문서가 검색되지 않으면 Generation 단계에서 좋은 답변이 나오기 어렵다.

---

# 2. Retrieval and Generation

## 2.1 Retrieval

### [개념]

Retrieval은 사용자 Query와 관련 있는 문서 Chunk를 찾는 단계다.

RAG에서 Retrieval은 답변 생성 이전에 수행된다.

사용자 Query는 Embedding Vector로 변환되고, Vector Database는 Query Vector와 유사한 Chunk Vector를 검색한다.

기본 흐름은 다음과 같다.

```text
User Query
→ Query Embedding
→ Vector Search
→ Metadata Filter
→ Top-K Selection
→ Retrieved Context
```

Retrieval의 결과는 LLM이 답변할 때 사용할 근거 Context가 된다.

---

### [핵심]

- Retrieval은 관련 문서 Chunk 검색 단계
- Query Embedding과 Chunk Embedding의 Similarity를 비교
- Vector Search는 의미 기반 검색에 강함
- Metadata Filter는 검색 범위를 좁힘
- Top-K는 가져올 후보 Chunk 개수
- Threshold는 최소 관련도 기준
- Retrieval 결과가 부정확하면 답변도 부정확해질 가능성이 높음

---

### [실무]

실무에서는 Retrieval 성능을 단순 유사도 Score만으로 판단하지 않는다.

다음 항목을 함께 확인한다.

- 기대 문서가 Top-K 안에 들어오는가
- 검색된 Chunk가 질문에 직접 답할 수 있는가
- Chunk 제목과 본문이 Query와 의미적으로 연결되는가
- Metadata Filter가 너무 좁거나 넓지 않은가
- 유사한 Chunk가 중복으로 검색되지 않는가
- 오래된 문서가 최신 문서보다 우선 검색되지 않는가

기술 문서 RAG에서는 Vector Search만으로 부족할 수 있다.

클래스명, 메서드명, API Endpoint, 에러 메시지처럼 정확한 키워드가 중요한 경우 Hybrid Search 또는 Keyword Search가 필요할 수 있다.

---

### [FAQ]

Q. Retrieval이 뭐야?

A.
사용자 질문과 관련 있는 문서 Chunk를 검색하는 단계다.

Q. Retrieval 결과가 나쁘면 어떻게 돼?

A.
LLM이 잘못된 Context를 기반으로 답변하거나, 문서에 있는 내용도 없다고 답할 수 있다.

Q. Top-K는 뭐야?

A.
검색 결과로 가져올 Chunk 개수다.

Q. Similarity Threshold는 뭐야?

A.
검색 결과로 사용할 최소 유사도 기준이다.

Q. Metadata Filter는 왜 써?

A.
Domain, Level, Section, Version 기준으로 검색 범위를 줄이기 위해 사용한다.

---

## 2.2 Generation

### [개념]

Generation은 Retrieved Context를 바탕으로 LLM이 답변을 생성하는 단계다.

RAG에서 Generation은 일반 LLM 답변과 다르다.

RAG Generation은 반드시 검색된 문서를 우선 근거로 사용해야 한다.

기본 흐름은 다음과 같다.

```text
Retrieved Context
→ Prompt Assembly
→ LLM Generation
→ Grounding Check
→ Final Answer
```

Generation 단계에서는 Prompt가 중요하다.

Prompt는 LLM에게 문서 근거 우선 규칙, Missing Information Rule, Citation Rule, Output Format을 명확히 전달해야 한다.

---

### [핵심]

- Generation은 검색된 Context 기반 답변 생성 단계
- Retrieved Context를 우선 근거로 사용
- 문서에 없는 내용은 없다고 표현
- 일반 지식으로 보완할 경우 추정임을 분리
- Prompt에 Grounding Rule이 필요
- Context가 불충분하면 확정 답변 금지
- Generation 실패는 Prompt, Context Assembly, Grounding Rule 문제일 수 있음

---

### [실무]

실무 RAG에서는 LLM이 검색 문서를 무시하고 일반 지식으로 답변하지 않도록 제어해야 한다.

Prompt에는 다음 규칙을 포함하는 것이 좋다.

```text
Use retrieved context first.
If the context is insufficient, say what is missing.
Do not invent project-specific facts.
Separate evidence-based answers from assumptions.
```

개인 AI Agent 구조에서는 Generation 단계가 Agent 역할에 따라 달라질 수 있다.

- PM Agent: 요구사항 정리, 작업 분해
- Backend Agent: 코드 생성, 아키텍처 제안
- Frontend Agent: 컴포넌트 설계, API 연동
- Review Agent: 검증, 오류 탐지
- DevOps Agent: 배포, 운영 기준 제안
- AI Agent: RAG, Agent Workflow, Evaluation 설계

하지만 모든 Agent는 Retrieved Context를 근거로 답변해야 한다.

---

### [FAQ]

Q. Generation이 뭐야?

A.
검색된 문서를 바탕으로 LLM이 답변을 생성하는 단계다.

Q. RAG Generation과 일반 LLM 답변은 뭐가 달라?

A.
RAG Generation은 Retrieved Context를 우선 근거로 사용한다.

Q. 문서에 없는 내용은 어떻게 답해야 해?

A.
문서에 없다고 말하고, 필요한 정보가 무엇인지 분리해서 설명해야 한다.

Q. Grounding Rule은 왜 필요해?

A.
LLM이 검색 문서에 없는 내용을 확정적으로 생성하지 않도록 제어하기 위해 필요하다.

Q. Generation 실패 원인은 뭐야?

A.
Context 부족, Prompt 부족, Grounding Rule 부족, 충돌 문서 포함 등이 원인일 수 있다.

---

# 3. RAG Basic Flow

## 3.1 End-to-End RAG Flow

### [개념]

RAG의 전체 흐름은 문서 적재와 사용자 질문 처리로 나눌 수 있다.

문서 적재 흐름은 다음과 같다.

```text
Raw Document
→ Load
→ Clean
→ Split into Chunks
→ Add Metadata
→ Generate Embedding
→ Store in Vector Database
→ Validate Retrieval
```

사용자 질문 처리 흐름은 다음과 같다.

```text
User Query
→ Query Embedding
→ Retrieve Relevant Chunks
→ Build Context
→ Generate Grounded Answer
→ Validate Answer
```

이 두 흐름은 분리해서 설계해야 한다.

문서를 잘 적재하지 않으면 검색 품질이 떨어지고, 검색 품질이 떨어지면 답변 품질도 떨어진다.

---

### [핵심]

- RAG Flow는 Ingestion Flow와 Query Flow로 분리
- Ingestion Flow는 문서를 검색 가능한 형태로 저장
- Query Flow는 사용자 질문에 맞는 문서를 검색
- Retrieved Context는 LLM Prompt에 조립됨
- 답변은 Grounded Answer여야 함
- 검색 검증 없이 문서 업로드만 하면 RAG 품질을 보장할 수 없음

---

### [실무]

실무에서는 문서를 업로드한 뒤 반드시 Retrieval Validation을 수행한다.

검증용 Golden Query를 만들고, 기대 Chunk가 Top-K 안에 검색되는지 확인한다.

예시는 다음과 같다.

```text
Golden Query:
RAG에서 Chunking은 왜 중요해?

Expected Document:
Vector_Database_RAG_Part01_Core_Concepts.md

Expected Section:
Chunking 또는 Retrieval 관련 Section
```

검색 검증에서 실패하면 모델을 바꾸기 전에 문서 구조를 먼저 확인한다.

점검 순서는 다음과 같다.

1. Header가 명확한가
2. Chunk가 하나의 개념만 다루는가
3. FAQ가 실제 질문 표현과 가까운가
4. Retrieval Queries가 충분한가
5. Metadata가 누락되지 않았는가
6. Embedding 재생성이 되었는가
7. Top-K / Threshold가 적절한가

---

### [FAQ]

Q. RAG 전체 흐름은 어떻게 돼?

A.
문서를 Chunk로 나누고 Embedding하여 Vector DB에 저장한 뒤, 질문이 들어오면 관련 Chunk를 검색해 LLM Context로 넣는다.

Q. Ingestion Flow와 Query Flow는 왜 나눠?

A.
문서 적재 문제와 질문 검색 문제를 분리해서 분석하기 위해서다.

Q. 문서 업로드 후 바로 쓰면 안 돼?

A.
가능은 하지만 검색 검증을 생략하면 문서가 있어도 검색되지 않는 문제가 생길 수 있다.

Q. Golden Query는 뭐야?

A.
RAG 검색 품질을 검증하기 위해 미리 정한 테스트 질문이다.

Q. 검색 검증 실패 시 모델부터 바꿔야 해?

A.
아니다. 먼저 Chunk 구조, Header, FAQ, Metadata, Reindex 여부를 확인해야 한다.

---

# 4. Vector Database Core Concept

## 4.1 Vector Database

### [개념]

Vector Database는 Embedding Vector를 저장하고 검색하는 저장소다.

일반 Database가 정확한 값, 조건, 관계 검색에 강하다면 Vector Database는 의미 유사도 기반 검색에 강하다.

문서 Chunk는 Embedding Model을 통해 숫자 배열인 Vector로 변환된다.

Vector Database는 사용자 Query Vector와 저장된 Chunk Vector를 비교하여 의미적으로 가까운 문서를 찾는다.

기본 흐름은 다음과 같다.

```text
Document Chunk
→ Embedding
→ Vector + Original Text + Metadata
→ Vector Database
→ Similarity Search
```

---

### [핵심]

- Vector Database는 의미 기반 검색 저장소
- Embedding Vector를 저장하고 검색
- Original Text와 Metadata 연결이 중요
- Vector Dimension은 Embedding Model과 일치해야 함
- 같은 Collection에는 같은 Embedding Model 사용 권장
- 문서 변경 시 Reindex 필요
- Metadata는 필터링과 출처 추적에 사용

---

### [실무]

실무 Vector Database 설계에서는 Vector만 저장하지 않는다.

반드시 다음 정보를 함께 관리해야 한다.

```json
{
  "originalText": "RAG는 외부 문서를 검색해 LLM Context로 넣는 구조다.",
  "embeddingModel": "bge-m3",
  "collectionName": "ai-foundation-vector-database-rag",
  "metadata": {
    "source": "Vector_Database_RAG_Part01_Core_Concepts.md",
    "domain": "AI",
    "level": "Foundation",
    "section": "RAG Core Concept",
    "version": "2026-06"
  }
}
```

Vector와 원문 Text가 분리되면 검색 결과를 LLM Context로 사용할 수 없다.

Metadata가 없으면 Agent가 검색 결과의 출처, Domain, Level, Section을 판단하기 어렵다.

---

### [FAQ]

Q. Vector Database가 뭐야?

A.
Embedding Vector를 저장하고 의미적으로 유사한 문서 Chunk를 검색하는 저장소다.

Q. Vector DB에는 Vector만 저장하면 돼?

A.
아니다. Original Text와 Metadata도 함께 연결되어야 한다.

Q. Vector Dimension은 왜 중요해?

A.
Embedding Model이 생성한 Vector 차원과 Vector DB Collection의 차원이 맞아야 검색이 가능하다.

Q. Embedding Model을 바꾸면 기존 Vector를 재사용해도 돼?

A.
권장하지 않는다. Embedding Model이 바뀌면 기존 문서를 다시 Embedding하고 Reindex해야 한다.

Q. Vector DB와 일반 DB 차이는 뭐야?

A.
일반 DB는 정확한 값 검색에 강하고, Vector DB는 의미 유사도 검색에 강하다.

---

## 4.2 Vector Index

### [개념]

Vector Index는 Vector Database가 유사한 Vector를 빠르게 찾기 위해 사용하는 검색 구조다.

문서가 적을 때는 단순 비교도 가능하지만, 문서 Chunk가 많아지면 모든 Vector를 비교하는 방식은 비효율적이다.

Vector Index는 Similarity Search 성능을 높이는 역할을 한다.

RAG 문서 기준에서는 Vector Index의 내부 알고리즘보다 다음 기준이 더 중요하다.

- Embedding Model 일관성
- Collection 분리 기준
- Metadata 연결
- Reindex 정책
- Retrieval 검증

---

### [핵심]

- Vector Index는 Similarity Search 성능을 높임
- 대량 Chunk 검색에서 중요
- Index는 Vector Dimension과 Embedding Model에 의존
- 문서 변경, 삭제, 모델 변경 시 Index 상태를 관리해야 함
- RAG 문서에서는 ANN 알고리즘 심화보다 운영 기준이 중요

---

### [실무]

개인 AI 서버나 Local RAG 환경에서는 ChromaDB, FAISS, Qdrant 같은 Vector Store를 사용할 수 있다.

관리형 서비스에서는 Pinecone, Milvus, Qdrant Cloud 같은 선택지가 있다.

실무 선택 기준은 다음과 같다.

| 기준                | Local Vector DB | Managed Vector DB |
| ------------------- | --------------- | ----------------- |
| 운영 난이도         | 직접 관리 필요  | 관리 부담 낮음    |
| 비용                | 낮음            | 사용량 기반 비용  |
| 데이터 통제         | 높음            | 서비스 정책 의존  |
| 확장성              | 직접 설계 필요  | 확장 기능 제공    |
| 개인 AI 서버 적합성 | 높음            | 필요 시 선택      |

개인 AI 프로젝트에서는 Local LLM / Local Embedding / Local Vector DB 조합이 우선 적합하다.

---

### [FAQ]

Q. Vector Index는 뭐야?

A.
Vector Database가 유사한 Vector를 빠르게 찾기 위한 검색 구조다.

Q. RAG 문서에서 Index 알고리즘을 깊게 알아야 해?

A.
초기 RAG 문서에서는 깊은 ANN 알고리즘보다 Embedding, Metadata, Reindex 기준이 더 중요하다.

Q. Local Vector DB는 언제 좋아?

A.
개인 AI 서버처럼 데이터 통제와 로컬 운영이 중요한 경우 적합하다.

Q. Managed Vector DB는 언제 좋아?

A.
대규모 운영, 확장성, 관리 편의성이 중요한 경우 적합하다.

Q. Vector Index도 재생성이 필요해?

A.
문서 변경, Embedding Model 변경, Collection 재구성 시 Reindex가 필요할 수 있다.

---

# 5. Embedding Core Concept

## 5.1 Embedding

### [개념]

Embedding은 Text를 의미를 가진 숫자 배열인 Vector로 변환하는 과정이다.

RAG에서는 문서 Chunk와 사용자 Query를 같은 Embedding Model로 Vector화한다.

Vector Database는 두 Vector 간 Similarity를 계산해 의미적으로 가까운 Chunk를 찾는다.

기본 흐름은 다음과 같다.

```text
Text
→ Embedding Model
→ Embedding Vector
→ Vector Database
```

Embedding Model은 RAG 검색 품질에 큰 영향을 준다.

한글 문서, 코드 문서, 기술 용어 문서에서는 해당 언어와 도메인에 맞는 Embedding Model을 선택해야 한다.

---

### [핵심]

- Embedding은 Text를 Vector로 변환하는 과정
- Query와 Document Chunk는 같은 Embedding Model로 변환
- Embedding Vector는 의미 유사도 검색에 사용
- Embedding Model 변경 시 기존 Vector 재생성 필요
- Vector Dimension 불일치 주의
- 한글 RAG는 한글 검색 품질이 좋은 Embedding Model이 필요
- 기술 문서는 키워드 검색과 병행할 수 있음

---

### [실무]

개인 AI 서버에서 BGE-M3 같은 Embedding Model은 다국어 검색과 Semantic Search에 사용할 수 있다.

하지만 Embedding Model만 좋다고 RAG 품질이 보장되지는 않는다.

다음 요소가 함께 맞아야 한다.

- Chunk Size
- Chunk Boundary
- Header 품질
- FAQ 문장
- Retrieval Queries
- Metadata
- Top-K
- Threshold
- Reranking
- Prompt Grounding Rule

Embedding Model을 변경한 경우 기존 Vector를 그대로 재사용하지 말고 전체 Reindex를 수행해야 한다.

---

### [FAQ]

Q. Embedding이 뭐야?

A.
Text를 의미 기반 검색에 사용할 수 있는 숫자 Vector로 변환하는 과정이다.

Q. Query와 문서는 같은 Embedding Model을 써야 해?

A.
그렇다. 같은 Vector 공간에서 비교해야 Similarity Search가 가능하다.

Q. Embedding Model을 바꾸면 왜 Reindex해야 해?

A.
Model이 바뀌면 Vector 공간과 차원이 달라질 수 있기 때문에 기존 Vector를 재사용하면 검색 품질이 깨질 수 있다.

Q. Embedding만 좋으면 RAG가 좋아져?

A.
아니다. Chunk, Metadata, Retrieval 설정, Prompt도 함께 좋아야 한다.

Q. 한글 RAG에서 Embedding Model은 중요해?

A.
중요하다. 한글 표현과 기술 용어를 잘 처리하는 Embedding Model이 검색 품질에 영향을 준다.

---

# 6. RAG vs General LLM

## 6.1 Difference Between RAG and General LLM

### [개념]

일반 LLM 답변은 모델이 학습한 내부 지식과 현재 Prompt를 바탕으로 생성된다.

RAG 답변은 외부 문서를 검색한 뒤, 검색된 문서를 Context로 추가하여 생성된다.

차이는 근거의 위치다.

```text
General LLM
→ Internal Knowledge + User Prompt
→ Answer
```

```text
RAG
→ Retrieved External Documents + User Prompt
→ Grounded Answer
```

RAG는 프로젝트 문서, 내부 규칙, 최신 운영 문서, 코드 규칙처럼 LLM이 기본적으로 알 수 없는 정보를 답변에 사용할 수 있다.

---

### [핵심]

- 일반 LLM은 내부 지식 중심
- RAG는 외부 문서 검색 중심
- RAG는 프로젝트 특화 지식에 적합
- RAG는 최신 문서 반영이 가능
- RAG는 문서 근거 기반 답변에 적합
- 문서 품질이 낮으면 RAG 답변 품질도 낮음
- RAG는 LLM 자체 성능 문제와 문서 검색 문제를 분리해서 봐야 함

---

### [실무]

개인 AI 개발팀 구조에서는 일반 LLM보다 RAG 기반 Agent가 중요하다.

예를 들어 Backend Agent가 Spring Boot 코드를 생성할 때, 일반 지식만 사용하면 프로젝트 규칙과 맞지 않는 코드를 만들 수 있다.

RAG 기반 Backend Agent는 다음 문서를 검색해 프로젝트 기준에 맞는 코드를 생성할 수 있다.

- Master RAG Rules
- Backend Domain Rules
- Spring Boot RAG Documents
- API Design RAG Documents
- Security RAG Documents
- Project Progress
- Agent Operation Rules

RAG는 Agent의 답변을 프로젝트 기준에 맞추기 위한 핵심 구조다.

---

### [FAQ]

Q. 일반 LLM과 RAG 차이는 뭐야?

A.
일반 LLM은 내부 지식 중심이고, RAG는 외부 문서를 검색해 근거로 사용하는 구조다.

Q. RAG가 프로젝트 문서에 좋은 이유는 뭐야?

A.
LLM이 모르는 프로젝트 규칙, 코드 기준, 진행 상황을 검색해서 답변에 반영할 수 있기 때문이다.

Q. RAG가 항상 일반 LLM보다 좋아?

A.
아니다. 문서 품질과 검색 품질이 낮으면 오히려 답변 품질이 떨어질 수 있다.

Q. RAG는 최신 정보를 반영할 수 있어?

A.
문서를 최신화하고 Reindex하면 최신 정보를 반영할 수 있다.

Q. RAG가 필요한 대표 상황은 뭐야?

A.
프로젝트 규칙, 내부 문서, 코드 컨벤션, 운영 절차, Agent 지식 기반이 필요한 경우다.

---

# 7. RAG Failure Types

## 7.1 Retrieval Failure

### [개념]

Retrieval Failure는 관련 문서가 존재하지만 검색 결과에 나타나지 않는 문제다.

문서가 Vector DB에 있어도 Chunk 구조, 키워드, Metadata, Embedding, Top-K 설정이 부적절하면 검색되지 않을 수 있다.

대표 흐름은 다음과 같다.

```text
User Query
→ Vector Search
→ Expected Chunk Missing
→ Insufficient Context
→ Poor Answer
```

---

### [핵심]

- 관련 문서가 있어도 검색되지 않을 수 있음
- Chunk 제목이 불명확하면 검색 실패 가능
- 핵심 키워드 누락 시 Query Matching 약화
- Metadata Filter가 잘못되면 문서 제외 가능
- Embedding 재생성 누락 시 오래된 내용 검색 가능
- Top-K가 낮으면 기대 문서가 누락될 수 있음

---

### [실무]

Retrieval Failure가 발생하면 다음 순서로 점검한다.

```text
문제:
문서에 있는 내용이 검색되지 않음

원인:
Chunk 제목 불명확
FAQ 부족
Retrieval Queries 부족
Metadata 누락
Embedding 재생성 누락
Top-K 부족

해결:
Header 보강
FAQ 보강
핵심 키워드 반복
Metadata 확인
Reindex 수행
Top-K / Threshold 조정
```

모델 답변이 틀렸다고 바로 LLM을 교체하지 않는다.

먼저 검색 결과에 기대 Chunk가 포함되었는지 확인해야 한다.

---

### [FAQ]

Q. 문서에 있는데 왜 못 찾아?

A.
Chunk 구조, Header, FAQ, Metadata, Embedding, Top-K 설정 문제일 수 있다.

Q. Retrieval Failure는 LLM 문제야?

A.
항상 그렇지 않다. 대부분 문서 구조나 검색 설정 문제일 수 있다.

Q. 문서 검색이 안 되면 먼저 뭘 봐야 해?

A.
기대 Chunk가 Top-K에 들어오는지 확인해야 한다.

Q. FAQ가 Retrieval에 도움이 돼?

A.
그렇다. 실제 사용자 질문 표현과 문서 표현을 연결하는 데 도움이 된다.

Q. Reindex는 언제 필요해?

A.
문서 수정, Embedding Model 변경, Metadata 변경, Collection 재구성 시 필요하다.

---

## 7.2 Generation Failure

### [개념]

Generation Failure는 검색 결과가 있음에도 LLM 답변이 문서와 다르게 생성되는 문제다.

검색된 Context가 불충분하거나, Prompt의 Grounding Rule이 약하거나, 충돌 문서가 포함되면 Generation Failure가 발생할 수 있다.

대표 흐름은 다음과 같다.

```text
Retrieved Context
→ Weak Prompt
→ LLM Uses General Knowledge
→ Ungrounded Answer
```

---

### [핵심]

- 검색 결과가 있어도 답변이 틀릴 수 있음
- Grounding Rule 부족 시 일반 지식으로 보완 가능
- Context가 길고 복잡하면 핵심 조건이 무시될 수 있음
- 충돌 문서가 포함되면 답변이 흔들릴 수 있음
- Missing Information Rule이 없으면 없는 내용을 생성할 수 있음
- 답변 검증 단계가 필요함

---

### [실무]

Generation Failure가 발생하면 다음 순서로 점검한다.

```text
문제:
검색된 문서와 다른 답변 생성

원인:
Grounding Rule 부족
Missing Information Rule 없음
Context 과다
충돌 문서 포함
Prompt Output Format 불명확

해결:
문서 근거 우선 규칙 추가
문서에 없는 내용 금지 규칙 추가
Context Deduplication
최신 문서 우선순위 적용
답변 검증 단계 추가
```

Review Agent는 Generation 결과를 검증할 때 다음을 확인해야 한다.

- 답변이 Retrieved Context와 일치하는가
- 문서에 없는 프로젝트 사실을 만들지 않았는가
- 추정과 근거 기반 답변을 분리했는가
- 누락 정보가 명확히 표시되었는가

---

### [FAQ]

Q. 검색은 됐는데 답변이 틀리는 이유는 뭐야?

A.
Prompt, Grounding Rule, Context Assembly, 충돌 문서 문제일 수 있다.

Q. Grounding Rule이 약하면 어떻게 돼?

A.
LLM이 검색 문서보다 일반 지식을 우선 사용해 잘못된 답변을 만들 수 있다.

Q. Missing Information Rule은 왜 필요해?

A.
문서에 없는 내용을 LLM이 임의로 생성하지 않도록 하기 위해 필요하다.

Q. Context가 많으면 좋은 거 아니야?

A.
아니다. 관련 없는 Context가 많으면 답변 품질이 떨어질 수 있다.

Q. Generation Failure는 어떻게 줄여?

A.
Grounding Rule 강화, Context 정리, 충돌 제거, 답변 검증을 적용한다.

---

# 8. RAG Document Role in Multi-Agent System

## 8.1 Agent Knowledge Base

### [개념]

RAG 문서는 Multi-Agent System에서 Agent의 Knowledge Base 역할을 한다.

Agent는 사용자 요청을 처리할 때 RAG 문서를 검색하여 작업 기준, 코드 규칙, 설계 원칙, 검증 기준을 확인한다.

개인 AI 개발팀 구조에서 RAG 문서는 Agent 행동의 기준이 된다.

```text
User Request
→ PM Agent
→ Retrieve Project / Domain Rules
→ Delegate Task
→ Specialist Agent
→ Retrieve Domain Documents
→ Generate Output
→ Review Agent Validation
```

RAG 문서 품질이 낮으면 Agent의 작업 품질도 낮아진다.

---

### [핵심]

- RAG 문서는 Agent의 Knowledge Base
- Agent는 Domain Rules와 Project Progress를 검색
- PM Agent는 작업 분해 기준으로 사용
- Backend Agent는 코드 생성 기준으로 사용
- Frontend Agent는 UI / API 연동 기준으로 사용
- Review Agent는 검증 기준으로 사용
- Agent 답변은 Retrieved Context 기반이어야 함

---

### [실무]

개인 AI 프로젝트의 목표는 단순 RAG 챗봇이 아니라 개인 AI 개발팀이다.

RAG 문서는 다음 Agent 흐름을 지원해야 한다.

```text
User
→ PM Agent
→ Backend Agent
→ Frontend Agent
→ Review Agent
→ DevOps Agent
→ AI/ML Agent
→ Final Output
```

각 Agent가 제대로 동작하려면 문서는 다음 조건을 만족해야 한다.

- Domain별로 분리
- Level별로 분리
- Section 제목 명확화
- FAQ 강화
- Retrieval Queries 포함
- Metadata 기준 통일
- 문서 간 중복 최소화
- 최신 문서 우선순위 관리

---

### [FAQ]

Q. RAG 문서는 Agent에게 어떤 역할이야?

A.
Agent가 작업 기준과 도메인 지식을 검색하는 Knowledge Base 역할이다.

Q. PM Agent는 RAG 문서를 어떻게 써?

A.
요구사항을 분석하고 어떤 Agent에게 작업을 넘길지 판단하는 기준으로 사용한다.

Q. Backend Agent는 RAG 문서를 어떻게 써?

A.
Backend Domain Rules와 코드 문서를 검색해 프로젝트 기준에 맞는 코드를 생성한다.

Q. Review Agent는 RAG 문서를 어떻게 써?

A.
생성된 결과가 규칙과 문서 근거에 맞는지 검증한다.

Q. Multi-Agent에서 RAG 문서 품질이 중요한 이유는 뭐야?

A.
Agent의 검색 결과와 판단 기준이 RAG 문서 품질에 직접 의존하기 때문이다.

---

# Retrieval Queries

### [FAQ]

Q. RAG가 뭐야?
A. RAG는 외부 문서를 검색한 뒤 검색된 문서를 LLM Context로 넣어 답변을 생성하는 구조다.

Q. Retrieval-Augmented Generation이 뭐야?
A. Retrieval로 관련 문서를 찾고, Generation으로 검색 문서를 근거 삼아 답변을 생성하는 방식이다.

Q. RAG는 파일 업로드 기능이야?
A. 아니다. 파일 업로드는 문서 적재 과정의 일부이고, RAG의 핵심은 Retrieval과 Grounded Generation이다.

Q. RAG에서 Retrieval이 뭐야?
A. 사용자 Query와 관련 있는 문서 Chunk를 검색하는 단계다.

Q. RAG에서 Generation이 뭐야?
A. Retrieved Context를 기반으로 LLM이 답변을 생성하는 단계다.

Q. Retrieval과 Generation 차이는 뭐야?
A. Retrieval은 관련 문서를 찾는 단계이고, Generation은 검색된 문서를 바탕으로 답변을 만드는 단계다.

Q. RAG 전체 흐름은 어떻게 돼?
A. 문서를 Chunk로 나누고 Embedding해 Vector DB에 저장한 뒤, 질문이 들어오면 관련 Chunk를 검색해 답변에 사용한다.

Q. Vector Database가 뭐야?
A. Embedding Vector를 저장하고 의미적으로 유사한 문서 Chunk를 검색하는 저장소다.

Q. Vector DB와 일반 DB 차이는 뭐야?
A. 일반 DB는 정확한 값 검색에 강하고, Vector DB는 의미 유사도 검색에 강하다.

Q. Vector Index는 뭐야?
A. Vector Database가 유사한 Vector를 빠르게 찾기 위해 사용하는 검색 구조다.

Q. Embedding이 뭐야?
A. Text를 의미 기반 검색에 사용할 수 있는 숫자 Vector로 변환하는 과정이다.

Q. Query Embedding은 뭐야?
A. 사용자 질문을 Embedding Model로 Vector화한 결과다.

Q. Document Embedding은 뭐야?
A. 문서 Chunk를 Embedding Model로 Vector화한 결과다.

Q. Query와 Document는 같은 Embedding Model을 써야 해?
A. 그렇다. 같은 Vector 공간에서 비교해야 Similarity Search가 가능하다.

Q. Embedding Model을 바꾸면 기존 Vector를 재사용해도 돼?
A. 권장하지 않는다. Embedding Model을 바꾸면 전체 문서를 다시 Embedding하고 Reindex해야 한다.

Q. Vector Dimension은 왜 중요해?
A. Embedding Model의 Vector 차원과 Vector DB Collection 차원이 일치해야 검색할 수 있기 때문이다.

Q. Top-K는 뭐야?
A. 검색 결과로 가져올 Chunk 개수다.

Q. Similarity Threshold는 뭐야?
A. 검색 결과로 사용할 최소 유사도 기준이다.

Q. Metadata Filter는 왜 필요해?
A. Domain, Level, Section, Version 기준으로 검색 범위를 줄이기 위해 필요하다.

Q. Retrieved Context는 뭐야?
A. Retrieval 단계에서 검색되어 LLM Prompt에 들어가는 문서 Chunk다.

Q. Context Assembly는 뭐야?
A. 검색된 Chunk를 정렬, 중복 제거, 압축하여 LLM Prompt에 넣을 Context로 구성하는 과정이다.

Q. Grounded Answer는 뭐야?
A. 검색된 문서를 근거로 생성한 답변이다.

Q. Missing Information Rule은 뭐야?
A. 문서에 없는 내용은 없다고 말하고 필요한 정보를 분리해서 표시하는 규칙이다.

Q. RAG 답변이 틀리면 어디부터 봐야 해?
A. 먼저 기대 문서가 Retrieval 결과 Top-K에 들어오는지 확인해야 한다.

Q. 문서에 있는데 검색이 안 되면 어떻게 해?
A. Header, Chunk 구조, FAQ, Retrieval Queries, Metadata, Embedding 재생성 여부를 확인한다.

Q. 검색은 됐는데 답변이 틀리면 어떻게 해?
A. Grounding Rule, Prompt, Context Assembly, 충돌 문서 포함 여부를 확인한다.

Q. RAG에서 FAQ가 왜 중요해?
A. 실제 사용자 질문 표현과 문서 표현을 연결해 Retrieval Hit를 높이기 때문이다.

Q. Retrieval Queries는 왜 필요해?
A. Agent와 사용자의 다양한 질문 표현을 문서에 포함해 Semantic Retrieval을 강화하기 위해 필요하다.

Q. Golden Query는 뭐야?
A. RAG 검색 품질을 검증하기 위해 미리 정한 테스트 질문이다.

Q. Reindex는 언제 해야 해?
A. 문서 수정, Embedding Model 변경, Metadata 변경, Collection 재구성 시 필요하다.

Q. RAG가 Multi-Agent System에서 왜 중요해?
A. Agent가 프로젝트 규칙과 도메인 지식을 검색해 근거 기반으로 작업할 수 있게 해주기 때문이다.

Q. Agent Knowledge Base는 뭐야?
A. Agent가 작업 기준, 코드 규칙, 설계 원칙, 검증 기준을 검색하는 지식 기반이다.

Q. 개인 AI 개발팀에서 RAG 문서는 어떤 역할이야?
A. PM Agent, Backend Agent, Frontend Agent, Review Agent, DevOps Agent, AI Agent가 공통으로 참조하는 기준 문서 역할이다.
