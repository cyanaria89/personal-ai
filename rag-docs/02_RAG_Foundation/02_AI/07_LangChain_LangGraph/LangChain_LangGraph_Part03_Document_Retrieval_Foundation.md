# LangChain & LangGraph Part03 Document Retrieval Foundation

---

# 1. Document Retrieval Foundation

## 1.1 RAG 검색 기반 구조

### [개념]

Document Retrieval Foundation은 RAG Chain이 답변을 생성하기 전에 문서를 검색 가능한 구조로 만드는 기반 단계다.

RAG는 문서를 그대로 LLM에 넣는 구조가 아니다.

RAG는 원본 문서를 읽고, 의미 단위로 나누고, Vector로 변환하고, Vector Store에 저장한 뒤, 사용자 질문과 관련된 Chunk를 검색해 LLM Context로 전달하는 구조다.

기본 Flow:

```text
Raw Document
→ Document Loader
→ Document
→ Text Splitter
→ Chunk
→ Embedding Model
→ Vector Store
→ Retriever
→ Retrieved Documents
→ RAG Prompt Context
```

Part03은 Part04 RAG Chain의 검색 기반이다.

Part03의 목표는 문서 적재, Chunk 설계, Embedding, Vector Store, Retriever, Metadata, Golden Query Test 기준을 정리하는 것이다.

---

### [핵심]

- Document Loader는 원본 문서를 Document 객체로 변환한다.
- Text Splitter는 Document를 검색 가능한 Chunk로 나눈다.
- Chunk는 Retriever가 검색하는 기본 단위다.
- Embedding Model은 Chunk와 Query를 Vector로 변환한다.
- Vector Store는 Vector, page_content, Metadata를 저장한다.
- Retriever는 사용자 질문과 관련된 Chunk를 검색한다.
- Metadata는 Source 추적과 Domain Filter에 사용된다.
- RAG 답변 품질은 LLM보다 검색 품질에 크게 의존한다.
- 검색 품질은 Loader, Splitter, Chunk, Embedding, Metadata, Retriever 설정의 영향을 받는다.

---

### [실무]

2026 실무 기준 RAG 검색 품질은 다음 순서로 점검한다.

| 단계               | 품질 기준                            |
| ------------------ | ------------------------------------ |
| Document Loader    | 원본 구조 보존                       |
| Document Object    | page_content, metadata 정상 생성     |
| Text Splitter      | 의미 단위 Chunk 분리                 |
| Chunk Design       | 하나의 개념, 독립 검색 가능          |
| Metadata           | source, domain, part, section 유지   |
| Embedding Model    | 언어와 도메인에 맞는 모델            |
| Vector Store       | Dimension, Index, Metadata 저장 정상 |
| Retriever          | Golden Query 검색 성공               |
| Context Formatting | Source와 Section 구분 가능           |

RAG 검색 기반 실패 패턴:

```text
Raw Document
→ 문서 구조 훼손
→ 잘못된 Chunk 생성
→ Metadata 누락
→ 부정확한 Embedding
→ 관련 없는 Retrieval
→ LLM 답변 실패
```

RAG 검색 기반 개선 패턴:

```text
Markdown Header 유지
→ Chunk 의미 단위 분리
→ Metadata 보존
→ Embedding Dimension 확인
→ Golden Query Test
→ Retriever 튜닝
→ Grounded Answer 생성
```

---

### [FAQ]

Q. Document Retrieval Foundation이 뭐야?

A.
RAG에서 문서를 읽고, Chunk로 나누고, Embedding하고, 검색 가능하게 만드는 기반 구조다.

Q. RAG에서 LLM보다 검색 기반이 중요한 이유는?

A.
Retriever가 잘못된 문서를 가져오면 LLM은 잘못된 Context를 기반으로 답변하기 때문이다.

Q. RAG 검색 기반의 핵심 구성 요소는?

A.
Document Loader, Text Splitter, Chunk, Embedding Model, Vector Store, Retriever, Metadata다.

Q. RAG 검색 품질은 어디서 결정돼?

A.
문서 구조 보존, Chunk 품질, Metadata, Embedding 모델, Retriever 설정에서 결정된다.

Q. Part03은 Part04와 어떻게 연결돼?

A.
Part03은 문서를 검색 가능한 형태로 만들고, Part04는 그 검색 결과를 RAG Chain에서 답변 생성에 사용한다.

---

# 2. Document Loader

## 2.1 Document Loader 기본 개념

### [개념]

Document Loader는 외부 원본 문서를 LangChain에서 사용할 수 있는 Document 객체로 변환하는 구성 요소다.

Document Loader는 파일, 폴더, 웹페이지, PDF, Markdown, HTML, CSV, JSON 같은 Source를 읽어온다.

기본 Flow:

```text
File / Directory / Web / PDF / Markdown
→ Document Loader
→ Document
→ Text Splitter
```

Document 객체는 일반적으로 `page_content`와 `metadata`를 가진다.

```text
Document
├ page_content
└ metadata
```

Loader의 핵심 목표는 원본 문서 내용을 검색 가능한 Document로 변환하면서 구조와 출처 정보를 최대한 보존하는 것이다.

---

### [핵심]

- Loader는 원본 Source를 Document 객체로 변환한다.
- `page_content`에는 실제 문서 내용이 들어간다.
- `metadata`에는 source, title, section 같은 추적 정보가 들어간다.
- Markdown Loader는 Header 구조 보존이 중요하다.
- PDF Loader는 텍스트 추출 품질 확인이 필요하다.
- Directory Loader는 여러 파일을 일괄 적재할 때 사용한다.
- Web Loader는 웹 문서 적재에 사용한다.
- Encoding 문제를 확인해야 한다.
- Loader 결과는 Splitter 적용 전 샘플 검증이 필요하다.

---

### [실무]

Document Loader 종류:

| Loader           | 사용 대상      |
| ---------------- | -------------- |
| Text Loader      | `.txt` 문서    |
| Markdown Loader  | `.md` RAG 문서 |
| PDF Loader       | PDF 문서       |
| Directory Loader | 폴더 단위 문서 |
| Web Loader       | 웹페이지       |
| CSV Loader       | CSV 기반 문서  |
| JSON Loader      | JSON 문서      |
| HTML Loader      | HTML 문서      |

RAG 문서 Loader 기준:

```text
Markdown File
→ Markdown Loader
→ Header / Code Block / Table 구조 확인
→ Metadata 추가
→ Text Splitter 전달
```

Loader 검증 항목:

| 항목       | 확인                                  |
| ---------- | ------------------------------------- |
| Content    | 본문 누락 여부                        |
| Header     | 제목 구조 유지 여부                   |
| Code Block | 코드블록 깨짐 여부                    |
| Table      | 표 구조 유지 여부                     |
| Encoding   | 한글 깨짐 여부                        |
| Metadata   | source, title, domain, part 존재 여부 |

Metadata 권장 필드:

| Metadata   | 목적                     |
| ---------- | ------------------------ |
| source     | 원본 파일명 또는 경로    |
| title      | 문서 제목                |
| domain     | Backend, AI, Frontend 등 |
| document   | 문서 묶음 이름           |
| part       | Part 번호                |
| section    | Header 기준 Section      |
| version    | 문서 버전                |
| updated_at | 수정 시점                |

---

### [FAQ]

Q. Document Loader가 뭐야?

A.
원본 파일이나 웹 문서를 LangChain Document 객체로 변환하는 구성 요소다.

Q. Document 객체에는 뭐가 들어가?

A.
일반적으로 `page_content`와 `metadata`가 들어간다.

Q. Markdown 문서 Loader에서 중요한 것은?

A.
Header, Code Block, Table 구조가 훼손되지 않는지 확인하는 것이다.

Q. PDF Loader는 왜 주의해야 해?

A.
PDF는 줄바꿈, 표, 코드, 문단 구조가 깨질 수 있어 추출 품질 확인이 필요하다.

Q. Loader 결과는 언제 검증해?

A.
Text Splitter를 적용하기 전에 샘플 Document의 page_content와 metadata를 확인해야 한다.

---

# 3. Markdown Document Loading

## 3.1 Markdown RAG 문서 적재

### [개념]

Markdown 문서는 RAG 문서에 적합한 형식이다.

Markdown은 Header, Code Block, Table, List, FAQ를 통해 문서 구조를 명확히 표현할 수 있다.

RAG Agent는 Header와 Metadata를 기준으로 검색 결과의 의미와 위치를 파악할 수 있다.

Markdown 적재 Flow:

```text
Markdown File
→ Markdown Loader
→ Header Structure Check
→ Metadata Attach
→ Text Splitter
→ Chunk
```

Markdown RAG 문서는 사람용 긴 설명보다 검색 가능한 구조를 우선한다.

---

### [핵심]

- Markdown은 RAG 문서 제작에 적합하다.
- Header는 Chunk 경계와 Metadata로 활용할 수 있다.
- Code Block은 중간에 잘리지 않도록 주의한다.
- Table은 Loader와 Splitter에서 깨질 수 있다.
- FAQ는 검색 Query Matching에 유리하다.
- Retrieval Queries Block은 검색 최적화에 중요하다.
- Markdown 문서 수정 후 Re-embedding이 필요하다.
- Markdown 문서는 Header, FAQ, Retrieval Queries 구조를 일관되게 유지해야 한다.

---

### [실무]

Markdown RAG 문서 작성 기준:

| 요소              | 기준                               |
| ----------------- | ---------------------------------- |
| Header            | Section 구조 명확화                |
| Code Block        | 실행 예제 또는 Flow 표현           |
| Table             | 비교, 기준, 설정 정리              |
| FAQ               | 사용자 질문 패턴 대응              |
| Retrieval Queries | 검색어 매칭 강화                   |
| Metadata          | source, domain, part, section 유지 |

권장 Markdown 구조:

```md
# FileName

# Document Title

---

# 1. Main Section

## 1.1 Sub Section

### [개념]

### [핵심]

### [실무]

### [FAQ]

# Retrieval Queries
```

Markdown Loader 검증 항목:

- Header가 유지되는가?
- Code Block이 깨지지 않는가?
- Table이 읽을 수 있는 형태인가?
- FAQ Q/A가 분리되지 않는가?
- Retrieval Queries가 끝까지 포함되는가?
- Metadata에 source, domain, part, section이 포함되는가?

Markdown 적재 금지 패턴:

```text
긴 에세이형 문서
→ Header 없음
→ FAQ 없음
→ Metadata 없음
→ Chunk 의미 불명확
```

---

### [FAQ]

Q. Markdown이 RAG 문서에 적합한 이유는?

A.
Header, Code Block, Table, FAQ 구조를 통해 검색 가능한 Chunk를 만들기 쉽기 때문이다.

Q. Markdown Header는 왜 중요해?

A.
Header는 Chunk의 의미와 위치를 나타내고 Metadata로 활용할 수 있기 때문이다.

Q. Code Block은 어떻게 처리해야 해?

A.
중간에 잘리지 않도록 Chunk 경계를 조정하거나 Code Block Preservation 기준을 적용해야 한다.

Q. FAQ가 Retrieval에 좋은 이유는?

A.
사용자 질문 표현과 직접 매칭될 가능성이 높기 때문이다.

Q. Markdown 수정 후 무엇을 해야 해?

A.
수정된 문서를 다시 적재하고 Re-embedding해야 한다.

---

# 4. Text Splitter

## 4.1 Text Splitter 기본 개념

### [개념]

Text Splitter는 Document를 검색 가능한 Chunk로 나누는 구성 요소다.

Chunk는 Retriever가 검색하는 기본 단위다.

Chunk 품질이 낮으면 Embedding과 Retriever 품질도 낮아진다.

기본 Flow:

```text
Document
→ Text Splitter
→ Chunk
→ Metadata Attach
```

Text Splitter는 단순히 글자 수를 기준으로 자르는 도구가 아니다.

의미 단위, Header 구조, 문단 경계, Code Block, FAQ Q/A 단위를 고려해야 한다.

---

### [핵심]

- Text Splitter는 Document를 Chunk로 나눈다.
- Chunk는 Retrieval의 기본 검색 단위다.
- Markdown 문서는 Header 기반 Split이 유리하다.
- Recursive Character Splitter는 일반 텍스트에 자주 사용된다.
- Chunk Size와 Chunk Overlap은 문서 성격에 맞게 조정한다.
- Code Block 중간 분리를 피해야 한다.
- FAQ의 Q와 A는 같은 Chunk에 유지하는 것이 좋다.
- Split 후 샘플 검색 검증이 필요하다.

---

### [실무]

Text Splitter 종류:

| Splitter                     | 사용 대상           |
| ---------------------------- | ------------------- |
| Recursive Character Splitter | 일반 텍스트         |
| Markdown Header Splitter     | Markdown 문서       |
| Token Text Splitter          | Token 기준 분리     |
| Character Text Splitter      | 단순 문자 기준      |
| Semantic Splitter            | 의미 경계 기반 분리 |
| Code Splitter                | 코드 파일 분리      |

Chunk 설계 기준:

| 항목              | 기준                      |
| ----------------- | ------------------------- |
| Chunk Size        | 300~1200 tokens 권장      |
| Chunk Overlap     | 문맥 연결용 최소 중복     |
| Semantic Boundary | 하나의 개념 단위 유지     |
| Header Metadata   | Section 정보 유지         |
| Code Block        | 중간 분리 방지            |
| FAQ               | Q/A 함께 유지             |
| Table             | 가능한 한 한 Chunk에 유지 |

Splitter 적용 순서 예시:

```text
Markdown Document
→ Header 기준 1차 Split
→ 너무 긴 Section만 Size 기준 2차 Split
→ Metadata 보존
→ 샘플 Chunk 검증
```

---

### [FAQ]

Q. Text Splitter가 뭐야?

A.
Document를 검색 가능한 Chunk로 나누는 구성 요소다.

Q. Chunk가 중요한 이유는?

A.
Retriever가 Chunk 단위로 검색하므로 Chunk 품질이 RAG 검색 품질을 결정하기 때문이다.

Q. Markdown 문서는 어떻게 Split하는 게 좋아?

A.
Header 기반 Split을 우선 고려하고, 너무 긴 Section은 Size 기준 Split을 추가한다.

Q. Chunk Size는 얼마나 잡아야 해?

A.
문서 성격에 따라 다르지만 RAG 문서는 보통 300~1200 tokens 범위를 권장한다.

Q. FAQ의 Q와 A는 분리해도 돼?

A.
권장하지 않는다. Q/A가 함께 있어야 질문 매칭과 답변 생성에 유리하다.

---

# 5. Chunk Design

## 5.1 Chunk 품질 기준

### [개념]

Chunk는 독립 검색되어도 의미가 유지되어야 하는 검색 단위다.

좋은 Chunk는 하나의 개념을 설명하고 제목과 Metadata를 통해 문맥을 보존한다.

나쁜 Chunk는 여러 개념이 섞이거나, 문장 중간에서 잘리거나, Source를 추적할 수 없다.

좋은 Chunk 구조:

```text
Title / Section Metadata
→ Concept
→ Key Points
→ Example or Flow
→ FAQ
```

---

### [핵심]

- Chunk는 하나의 개념만 담는 것이 좋다.
- Chunk는 독립적으로 검색되어도 의미가 유지되어야 한다.
- Header와 Metadata가 Chunk 문맥을 보강한다.
- FAQ Q/A는 같은 Chunk에 유지한다.
- Code Block은 가능한 한 하나의 Chunk에 유지한다.
- 너무 작은 Chunk는 문맥 부족 문제가 발생한다.
- 너무 큰 Chunk는 검색 정밀도와 Context 효율이 낮아진다.
- Chunk는 Part04 RAG Chain의 Context 품질을 결정한다.

---

### [실무]

좋은 Chunk 조건:

| 조건             | 설명                                    |
| ---------------- | --------------------------------------- |
| Single Concept   | 하나의 개념 중심                        |
| Clear Title      | 검색 결과에서 의미 파악 가능            |
| Metadata         | source, domain, part, section 추적 가능 |
| Short Example    | 코드나 Flow 예제 포함                   |
| FAQ Included     | 질문 패턴 매칭 강화                     |
| Context Complete | 독립 검색 가능                          |
| No Noise         | 불필요한 서론 제거                      |

나쁜 Chunk 예시:

```text
LangChain 설명
+ LangGraph 설명
+ Prompt Template 설명
+ Tool Calling 설명
+ Multi-Agent 설명
```

문제:

- 여러 개념 혼합
- 검색 결과가 넓고 모호함
- LLM Context 품질 저하

좋은 Chunk 예시:

```text
Section: Output Parser
Concept: LLM 응답을 JSON 또는 Schema로 변환
Key Points:
- 형식 안정화
- Parse Error 처리
- Retry 필요
FAQ:
Q. Output Parser는 왜 필요해?
A. LLM 응답을 안정적인 구조로 사용하기 위해 필요하다.
```

Chunk 품질 점검:

```text
Chunk 하나만 읽어도
→ 무엇에 대한 내용인지 알 수 있는가?
→ 어떤 Source에서 왔는지 알 수 있는가?
→ 어떤 질문에 답할 수 있는가?
```

---

### [FAQ]

Q. 좋은 Chunk란 뭐야?

A.
하나의 개념을 담고 독립 검색되어도 의미가 유지되는 검색 단위다.

Q. Chunk가 너무 작으면 뭐가 문제야?

A.
문맥이 부족해 LLM이 답변에 필요한 정보를 충분히 얻지 못할 수 있다.

Q. Chunk가 너무 크면 뭐가 문제야?

A.
검색 정밀도가 낮아지고 관련 없는 내용이 Context에 섞일 수 있다.

Q. FAQ는 Chunk에 같이 넣어야 해?

A.
권장한다. Q/A가 함께 있어야 질문 매칭과 답변 생성에 유리하다.

Q. Chunk에 Metadata가 필요한 이유는?

A.
검색 결과의 출처와 Section을 추적하기 위해 필요하다.

---

# 6. Embedding Model

## 6.1 Embedding 기본 개념

### [개념]

Embedding Model은 텍스트를 Vector로 변환하는 모델이다.

RAG에서 Embedding Model은 문서 Chunk와 사용자 Query를 같은 Vector 공간에 배치해 유사도 검색을 가능하게 한다.

기본 Flow:

```text
Text
→ Embedding Model
→ Vector
```

RAG Embedding Flow:

```text
Document Chunk
→ Document Embedding
→ Vector Store

User Query
→ Query Embedding
→ Similarity Search
```

Embedding Model은 Chat Model과 역할이 다르다.

Chat Model은 답변을 생성하고, Embedding Model은 검색용 Vector를 생성한다.

---

### [핵심]

- Embedding Model은 검색용 Vector를 생성한다.
- Document Embedding은 문서 Chunk를 Vector로 변환한다.
- Query Embedding은 사용자 질문을 Vector로 변환한다.
- Vector 유사도를 기준으로 관련 Chunk를 검색한다.
- Chat Model과 Embedding Model은 역할이 다르다.
- Embedding Model 변경 시 기존 Vector는 재생성해야 한다.
- 한국어 문서는 Multilingual Embedding Model을 고려한다.
- Embedding 실패 Chunk는 기록해야 한다.

---

### [실무]

Embedding Model 선택 기준:

| 기준             | 설명                         |
| ---------------- | ---------------------------- |
| Language         | 한국어 / 영어 / 다국어 지원  |
| Domain           | 코드, 문서, 일반 지식 적합성 |
| Dimension        | Vector Store와 호환 필요     |
| Local Support    | 로컬 서버 실행 가능 여부     |
| Batch Processing | 대량 문서 처리 효율          |
| Performance      | 검색 품질                    |
| Cost             | API 비용 또는 로컬 리소스    |

Embedding 주의사항:

- 서로 다른 Embedding Model의 Vector를 섞지 않는다.
- Model 변경 시 전체 Re-embedding이 필요하다.
- Dimension 불일치가 발생하면 Vector Store 저장이 실패한다.
- 긴 Chunk는 Embedding 품질이 떨어질 수 있다.
- 너무 짧은 Chunk는 의미 정보가 부족할 수 있다.
- Embedding 실패 Chunk는 로그로 남긴다.
- Chat Model 교체와 Embedding Model 교체를 혼동하지 않는다.

개인 AI 서버 기준:

```text
Chat Model
→ 답변 생성

Embedding Model
→ 문서 검색용 Vector 생성

Vector Store
→ Embedding Vector 저장

Retriever
→ Query와 유사한 Chunk 검색
```

---

### [FAQ]

Q. Embedding Model이 뭐야?

A.
텍스트를 유사도 검색이 가능한 Vector로 변환하는 모델이다.

Q. Embedding Model과 Chat Model은 달라?

A.
다르다. Embedding Model은 검색용 Vector를 만들고, Chat Model은 답변을 생성한다.

Q. Document Embedding과 Query Embedding은 뭐야?

A.
Document Embedding은 문서 Chunk를 Vector로 바꾸는 것이고, Query Embedding은 사용자 질문을 Vector로 바꾸는 것이다.

Q. Embedding Model을 바꾸면 어떻게 해야 해?

A.
기존 Vector와 호환되지 않으므로 전체 문서를 Re-embedding해야 한다.

Q. Chat Model만 바꾸면 Re-embedding이 필요해?

A.
보통은 필요 없다. Re-embedding은 Embedding Model을 바꾸거나 문서 Chunk가 바뀔 때 필요하다.

---

# 7. Vector Store

## 7.1 Vector Store 기본 개념

### [개념]

Vector Store는 Embedding Vector와 Metadata를 저장하고 유사도 검색을 수행하는 저장소다.

Vector Store는 사용자 Query Vector와 문서 Chunk Vector 사이의 유사도를 계산해 관련 Chunk를 찾는다.

기본 Flow:

```text
Chunk
→ Embedding Vector
→ Vector Store
→ Similarity Search
→ Retrieved Documents
```

Vector Store는 RAG 검색 단계의 핵심 저장소다.

Vector Store는 Vector만 저장하는 공간이 아니라 page_content와 Metadata를 함께 보존해야 한다.

---

### [핵심]

- Vector Store는 Embedding Vector를 저장한다.
- Vector Store는 page_content와 Metadata를 함께 저장해야 한다.
- Similarity Search로 관련 Chunk를 찾는다.
- Vector Dimension은 Embedding Model과 일치해야 한다.
- Metadata Filter로 검색 범위를 제한할 수 있다.
- Index 설정은 검색 속도와 품질에 영향을 준다.
- 문서 수정 시 Vector Store 갱신이 필요하다.
- 삭제된 문서의 Vector도 제거해야 한다.

---

### [실무]

Vector Store 저장 데이터:

| 데이터            | 목적           |
| ----------------- | -------------- |
| vector            | 유사도 검색    |
| page_content      | LLM Context    |
| metadata.source   | 출처 추적      |
| metadata.domain   | Domain 필터    |
| metadata.document | 문서 묶음 식별 |
| metadata.part     | Part 필터      |
| metadata.section  | Section 추적   |
| metadata.version  | 문서 버전 관리 |

Vector Store 선택 기준:

| 기준            | 설명                         |
| --------------- | ---------------------------- |
| Local / Cloud   | 로컬 서버 또는 관리형 서비스 |
| Metadata Filter | Domain 검색 제한             |
| Persistence     | 재시작 후 데이터 유지        |
| Scale           | 문서 수와 Query 수           |
| Index Type      | 검색 속도                    |
| Hybrid Search   | Keyword + Vector 검색        |
| Backup          | Vector DB 복구 가능성        |

Vector Store 운영 주의:

- Embedding Dimension 불일치 금지
- 서로 다른 모델 Vector 혼합 금지
- Metadata 누락 금지
- 중복 문서 적재 확인
- 삭제 문서 Vector 제거
- 문서 수정 후 Re-embedding
- 백업과 복구 기준 마련

---

### [FAQ]

Q. Vector Store가 뭐야?

A.
Embedding Vector와 Metadata를 저장하고 유사도 검색을 수행하는 저장소다.

Q. Vector Store에는 Vector만 저장해도 돼?

A.
아니다. page_content와 source, section 같은 Metadata도 함께 저장해야 한다.

Q. Metadata Filter는 왜 필요해?

A.
Backend, AI, Frontend 같은 Domain 범위를 제한해 검색 정확도를 높이기 위해 필요하다.

Q. Embedding Dimension이 안 맞으면 어떻게 돼?

A.
Vector Store 저장 또는 검색이 실패할 수 있다.

Q. 문서 수정 후 Vector Store는 어떻게 해야 해?

A.
수정된 문서를 다시 적재하고 Re-embedding한 뒤 Vector Store를 갱신해야 한다.

---

# 8. Retriever

## 8.1 Retriever 기본 개념

### [개념]

Retriever는 사용자 Query와 관련된 문서 Chunk를 검색하는 구성 요소다.

Retriever는 Vector Store를 직접 노출하지 않고 검색 인터페이스를 제공한다.

기본 Flow:

```text
User Query
→ Retriever
→ Retrieved Documents
→ RAG Prompt Context
```

Retriever 결과는 LLM 답변의 근거가 된다.

Retriever가 부정확하면 RAG Chain은 부정확한 답변을 생성할 가능성이 높다.

---

### [핵심]

- Retriever는 RAG의 검색 단계다.
- Retriever는 사용자 Query와 관련된 Chunk를 반환한다.
- Top-K는 반환할 문서 수를 결정한다.
- Similarity Threshold는 낮은 관련도 문서를 차단한다.
- Metadata Filter는 검색 범위를 제한한다.
- Search Type은 검색 방식에 영향을 준다.
- Retrieved Documents는 LLM에 넣기 전 정리해야 한다.
- Retriever 품질은 Golden Query로 검증한다.

---

### [실무]

Retriever 설정 요소:

| 설정                 | 목적                         |
| -------------------- | ---------------------------- |
| top_k                | 검색 결과 개수               |
| similarity_threshold | 최소 유사도 기준             |
| metadata_filter      | Domain / Part / Section 제한 |
| search_type          | similarity, mmr 등           |
| score                | 검색 결과 관련도             |
| reranking            | 검색 결과 재정렬             |
| query_rewrite        | 검색 Query 개선              |

Top-K 기준:

| Top-K   | 특징                          |
| ------- | ----------------------------- |
| 작음    | 정밀도 높음, 누락 가능성 있음 |
| 큼      | 누락 감소, 노이즈 증가        |
| 너무 큼 | Context 오염 가능성 증가      |

Retriever 품질 검증:

```text
Golden Query
→ Retriever
→ Expected Document 포함 여부 확인
→ Rank 확인
→ Score 확인
→ Metadata 확인
```

Part04 연결:

```text
Retriever
→ Retrieved Documents
→ Context Formatting
→ RAG Prompt
→ Grounded Answer
```

---

### [FAQ]

Q. Retriever가 뭐야?

A.
사용자 질문과 관련된 문서 Chunk를 검색해 반환하는 구성 요소다.

Q. Retriever는 왜 중요해?

A.
Retriever 결과가 LLM 답변의 근거가 되기 때문이다.

Q. Top-K는 뭐야?

A.
검색 결과로 반환할 문서 Chunk 개수다.

Q. Similarity Threshold는 왜 필요해?

A.
관련도가 낮은 문서가 Context에 들어가는 것을 막기 위해 필요하다.

Q. Retriever 결과는 바로 LLM에 넣어도 돼?

A.
권장하지 않는다. Source, Section, Score를 정리하는 Context Formatting 후 사용하는 것이 좋다.

---

# 9. Metadata Filtering

## 9.1 Metadata 기반 검색 제한

### [개념]

Metadata Filtering은 Retriever가 모든 문서를 검색하지 않고 특정 조건에 맞는 문서만 검색하도록 제한하는 방식이다.

RAG 문서가 많아질수록 Metadata Filtering은 검색 정확도를 높이는 데 중요하다.

기본 Flow:

```text
User Query
→ Metadata Filter
→ Vector Search in Filtered Documents
→ Retrieved Documents
```

예시:

```text
domain = "AI"
document = "LangChain_LangGraph"
part = "Part03"
section = "Retriever"
```

---

### [핵심]

- Metadata Filter는 검색 범위를 줄인다.
- Domain별 Agent 검색 정확도를 높인다.
- 불필요한 문서 혼입을 줄인다.
- PM Agent가 task_type에 따라 Filter를 선택할 수 있다.
- Metadata가 부정확하면 검색 결과도 부정확해진다.
- Filter가 과도하면 필요한 문서가 누락될 수 있다.
- Metadata 필드명은 문서 전체에서 통일해야 한다.

---

### [실무]

Domain Agent별 Metadata Filter 예시:

| Agent          | Metadata Filter                                   |
| -------------- | ------------------------------------------------- |
| SQL Agent      | domain = "Backend", topic = "SQL"                 |
| Backend Agent  | domain = "Backend"                                |
| Frontend Agent | domain = "Frontend"                               |
| AI Agent       | domain = "AI"                                     |
| DevOps Agent   | domain = "DevOps"                                 |
| Review Agent   | domain in ["Backend", "AI", "Frontend", "DevOps"] |

LangChain & LangGraph 검색 예시:

```json
{
  "domain": "AI",
  "document": "LangChain_LangGraph",
  "part": "Part03",
  "section": "Retriever"
}
```

Metadata Filter 주의:

- Metadata 필드명을 문서 전체에서 통일한다.
- Domain 이름을 혼용하지 않는다.
- Part 번호를 일관되게 작성한다.
- Section명을 Header와 맞춘다.
- Filter 조건이 너무 좁으면 검색 실패가 발생한다.
- Filter 없는 검색과 Filter 있는 검색을 모두 테스트한다.

PM Agent Filter 선택 Flow:

```text
User Request
→ PM Agent task_type 판단
→ metadata_filter 생성
→ RAG Node / Retriever 사용
```

---

### [FAQ]

Q. Metadata Filtering이 뭐야?

A.
문서의 domain, document, part, section 같은 Metadata 조건으로 검색 범위를 제한하는 방식이다.

Q. Metadata Filter는 왜 필요해?

A.
관련 없는 Domain 문서가 검색되는 것을 줄이고 검색 정확도를 높이기 위해 필요하다.

Q. Metadata Filter를 너무 강하게 걸면 어떻게 돼?

A.
필요한 문서가 검색되지 않아 RAG 답변이 실패할 수 있다.

Q. PM Agent가 Metadata Filter를 선택할 수 있어?

A.
가능하다. PM Agent가 task_type을 분석해 적절한 Domain Filter를 선택할 수 있다.

Q. Metadata 이름은 자유롭게 써도 돼?

A.
권장하지 않는다. source, domain, document, part, section 같은 필드명을 일관되게 사용해야 한다.

---

# 10. Golden Query Test

## 10.1 Retriever 품질 테스트

### [개념]

Golden Query Test는 특정 질문에 대해 반드시 검색되어야 하는 문서나 Chunk가 Retriever 결과에 포함되는지 확인하는 테스트다.

Golden Query는 RAG 검색 품질을 검증하는 기준 질문이다.

기본 Flow:

```text
Golden Query
→ Retriever
→ Retrieved Documents
→ Expected Chunk Match
→ Pass / Fail
```

Golden Query Test는 RAG 구축 후 반드시 수행해야 한다.

문서 수정, Chunk 변경, Embedding Model 변경, Metadata 변경 후에도 다시 수행해야 한다.

---

### [핵심]

- Golden Query는 예상 답변 문서가 명확한 질문이다.
- Retriever 결과에 Expected Chunk가 포함되어야 한다.
- Top-K, Threshold, Metadata Filter를 검증할 수 있다.
- 문서 수정 후 재테스트가 필요하다.
- Embedding Model 변경 후 재테스트가 필요하다.
- 실패 Query는 FAQ와 Retrieval Queries에 반영할 수 있다.
- Golden Query는 Part08 Evaluation Set과 연결된다.

---

### [실무]

LangChain & LangGraph Golden Query 예시:

| Query                         | Expected Document                       |
| ----------------------------- | --------------------------------------- |
| LangChain과 LangGraph 차이는? | Part01 Core Overview                    |
| Runnable이 뭐야?              | Part02 Runnable Prompt Model Parser     |
| Prompt Template은 왜 필요해?  | Part02 Runnable Prompt Model Parser     |
| Document Loader가 뭐야?       | Part03 Document Retrieval Foundation    |
| Text Splitter는 왜 중요해?    | Part03 Document Retrieval Foundation    |
| Retriever Top-K는 뭐야?       | Part03 Document Retrieval Foundation    |
| RAG Chain은 어떻게 구성해?    | Part04 RAG Chain Retrieval Optimization |
| Tool Calling이 뭐야?          | Part05 Tool ToolCalling Agent           |
| State Schema는 어떻게 설계해? | Part06 State Node Edge Routing          |

Golden Query 평가 기준:

| 항목             | 기준                                    |
| ---------------- | --------------------------------------- |
| Hit Rate         | Expected Chunk 포함 여부                |
| Rank             | Expected Chunk가 상위 결과인지          |
| Score            | 유사도 점수                             |
| Noise            | 관련 없는 Chunk 포함 여부               |
| Metadata         | source, domain, part, section 정상 여부 |
| Answer Grounding | 답변이 검색 결과 기반인지               |

Golden Query 실패 처리:

```text
Golden Query Fail
→ Query 표현 확인
→ Expected Chunk 내용 확인
→ Chunk 제목 보강
→ FAQ 추가
→ Retrieval Queries 추가
→ Metadata Filter 조정
→ Top-K / Threshold 조정
→ Re-embedding
→ Retest
```

---

### [FAQ]

Q. Golden Query Test가 뭐야?

A.
정해진 질문에 대해 예상 문서나 Chunk가 Retriever 결과에 포함되는지 확인하는 테스트다.

Q. Golden Query는 왜 필요해?

A.
RAG 검색 품질을 객관적으로 확인하기 위해 필요하다.

Q. Golden Query 실패 시 무엇을 확인해?

A.
Query 표현, Chunk 제목, FAQ, Retrieval Queries, Metadata Filter, Top-K, Threshold를 확인한다.

Q. 문서 수정 후 Golden Query를 다시 해야 해?

A.
해야 한다. 문서 구조와 Embedding 결과가 바뀔 수 있기 때문이다.

Q. Golden Query는 Part08과 어떻게 연결돼?

A.
Part08의 Evaluation Set에서 Retriever 품질과 Agent Workflow 품질을 검증하는 기준으로 사용된다.

---

# 11. Retrieval Troubleshooting

## 11.1 Retriever가 관련 문서를 못 찾음

### [개념]

Retriever가 관련 문서를 못 찾는 문제는 RAG 실패의 대표 원인이다.

이 문제는 LLM 문제가 아니라 문서 구조, Chunk, Embedding, Metadata, Retriever 설정 문제일 가능성이 높다.

문제 해결은 검색 단계와 생성 단계를 분리해 확인해야 한다.

---

### [핵심]

문제:

- 질문과 관련된 문서가 검색되지 않음
- 엉뚱한 Chunk가 상위에 검색됨
- Source가 없는 답변이 생성됨
- 문서에 있는 내용인데 RAG가 없다고 답함
- Metadata Filter 적용 후 검색 결과가 사라짐

원인:

- Chunk가 너무 작거나 큼
- Header 제목이 모호함
- FAQ가 부족함
- Retrieval Queries가 부족함
- Query 표현과 문서 표현이 다름
- Metadata Filter가 과도함
- Top-K가 너무 작음
- Similarity Threshold가 너무 높음
- Embedding Model이 문서 언어에 부적합함
- Re-embedding이 누락됨

해결:

- Golden Query로 검색 결과 확인
- Chunk 제목과 Section명 보강
- FAQ와 Retrieval Queries 추가
- Metadata Filter 완화
- Top-K 조정
- Threshold 조정
- Query Rewrite 적용
- Re-embedding 수행
- Part04 RAG Evaluation으로 재검증

---

### [실무]

Troubleshooting Flow:

```text
Retrieval Failure
→ Golden Query Test
→ Retrieved Chunk 확인
→ Expected Chunk 확인
→ Metadata 확인
→ Chunk 내용 확인
→ Top-K / Threshold 조정
→ FAQ / Retrieval Queries 보강
→ Re-embedding
→ Retest
```

검색 실패 점검표:

| 점검 항목    | 확인 내용                                  |
| ------------ | ------------------------------------------ |
| 문서 적재    | Loader가 문서를 제대로 읽었는가            |
| Chunk        | 의미 단위로 나뉘었는가                     |
| Metadata     | source, domain, part, section이 존재하는가 |
| Embedding    | 모델과 Vector Dimension이 일치하는가       |
| Filter       | 너무 좁게 제한하지 않았는가                |
| Top-K        | 필요한 문서가 들어올 만큼 충분한가         |
| Threshold    | 관련 문서를 차단하지 않는가                |
| Query        | 문서 용어와 너무 다르지 않은가             |
| Re-embedding | 문서 수정 후 다시 Embedding했는가          |

증상별 대응:

| 증상                 | 우선 조치                         |
| -------------------- | --------------------------------- |
| 검색 결과 없음       | Threshold 완화, Filter 완화       |
| 관련 문서 누락       | Top-K 증가, Query Rewrite         |
| 엉뚱한 문서 검색     | Metadata Filter 강화, FAQ 보강    |
| Score 낮음           | Chunk 제목 보강, Embedding 재검토 |
| 문서 수정 반영 안 됨 | Re-embedding 수행                 |

---

### [FAQ]

Q. 문서에 있는 내용인데 RAG가 못 찾는 이유는?

A.
Chunk 품질, Metadata Filter, Top-K, Threshold, Embedding 모델, Query 표현 문제가 원인일 수 있다.

Q. Retriever가 엉뚱한 문서를 가져오면 어떻게 해?

A.
Chunk 제목, FAQ, Metadata Filter, Threshold, Reranking을 점검해야 한다.

Q. Top-K를 늘리면 항상 좋아?

A.
아니다. 누락은 줄지만 관련 없는 Context가 섞일 수 있다.

Q. Threshold를 높이면 항상 좋아?

A.
아니다. 관련 문서까지 차단해 검색 실패가 발생할 수 있다.

Q. 검색 실패는 LLM 문제야?

A.
대부분은 LLM 문제가 아니라 Retrieval Pipeline 문제다.

---

# 12. Part03 Checklist

## 12.1 Document Retrieval Checklist

### [Checklist]

- [ ] Document Loader가 원본 문서를 정상적으로 읽는가?
- [ ] Document 객체에 page_content와 metadata가 생성되는가?
- [ ] Markdown Header 구조가 유지되는가?
- [ ] Code Block과 Table이 깨지지 않는가?
- [ ] Metadata에 source, domain, document, part, section이 포함되는가?
- [ ] Text Splitter가 의미 단위로 Chunk를 나누는가?
- [ ] Chunk Size가 문서 성격에 적합한가?
- [ ] Chunk Overlap이 과도하거나 부족하지 않은가?
- [ ] FAQ Q/A가 같은 Chunk에 유지되는가?
- [ ] Code Block이 중간에 분리되지 않는가?
- [ ] Embedding Model이 문서 언어와 도메인에 적합한가?
- [ ] Embedding Dimension이 Vector Store와 일치하는가?
- [ ] 서로 다른 Embedding Model Vector를 섞지 않았는가?
- [ ] Vector Store에 vector, page_content, metadata가 함께 저장되는가?
- [ ] Retriever Top-K가 적절한가?
- [ ] Similarity Threshold가 과도하지 않은가?
- [ ] Metadata Filter가 검색 범위를 적절히 제한하는가?
- [ ] Golden Query Test를 수행했는가?
- [ ] 검색 실패 Query를 FAQ와 Retrieval Queries에 반영했는가?
- [ ] 문서 수정 후 Re-embedding 기준이 있는가?
- [ ] Part04 RAG Chain에서 사용할 Context Formatting 준비가 되었는가?

---

# Retrieval Queries

### [FAQ]

Q. Document Retrieval Foundation이 뭐야?
A. RAG에서 문서를 읽고, Chunk로 나누고, Embedding하고, 검색 가능하게 만드는 기반 구조다.

Q. RAG 검색 기반의 핵심 구성 요소는?
A. Document Loader, Text Splitter, Chunk, Embedding Model, Vector Store, Retriever, Metadata다.

Q. RAG에서 검색 품질이 중요한 이유는?
A. Retriever가 잘못된 문서를 가져오면 LLM은 잘못된 Context를 기반으로 답변하기 때문이다.

Q. Part03은 Part04와 어떻게 연결돼?
A. Part03은 문서를 검색 가능한 형태로 만들고, Part04는 그 검색 결과를 RAG Chain에서 답변 생성에 사용한다.

Q. Document Loader가 뭐야?
A. 원본 파일이나 웹 문서를 LangChain Document 객체로 변환하는 구성 요소다.

Q. Document 객체에는 뭐가 들어가?
A. 일반적으로 page_content와 metadata가 들어간다.

Q. Markdown Loader에서 중요한 것은?
A. Header, Code Block, Table 구조가 훼손되지 않는지 확인하는 것이다.

Q. PDF Loader는 왜 주의해야 해?
A. PDF는 줄바꿈, 표, 코드, 문단 구조가 깨질 수 있어 추출 품질 확인이 필요하다.

Q. Metadata는 왜 필요해?
A. 검색 결과의 출처, 문서 제목, Section을 추적하고 Source 기반 답변을 만들기 위해 필요하다.

Q. Loader 결과는 언제 검증해?
A. Text Splitter를 적용하기 전에 샘플 Document의 page_content와 metadata를 확인해야 한다.

Q. Markdown이 RAG 문서에 적합한 이유는?
A. Header, Code Block, Table, FAQ 구조를 통해 검색 가능한 Chunk를 만들기 쉽기 때문이다.

Q. Markdown Header는 왜 중요해?
A. Header는 Chunk의 의미와 위치를 나타내고 Metadata로 활용할 수 있기 때문이다.

Q. Code Block은 어떻게 처리해야 해?
A. 중간에 잘리지 않도록 Chunk 경계를 조정하거나 Code Block Preservation 기준을 적용해야 한다.

Q. FAQ가 Retrieval에 좋은 이유는?
A. 사용자 질문 표현과 직접 매칭될 가능성이 높기 때문이다.

Q. Markdown 수정 후 무엇을 해야 해?
A. 수정된 문서를 다시 적재하고 Re-embedding해야 한다.

Q. Text Splitter가 뭐야?
A. Document를 검색 가능한 Chunk로 나누는 구성 요소다.

Q. Chunk가 중요한 이유는?
A. Retriever가 Chunk 단위로 검색하므로 Chunk 품질이 RAG 검색 품질을 결정하기 때문이다.

Q. Markdown 문서는 어떻게 Split하는 게 좋아?
A. Header 기반 Split을 우선 고려하고, 너무 긴 Section은 Size 기준 Split을 추가한다.

Q. Chunk Size는 얼마나 잡아야 해?
A. 문서 성격에 따라 다르지만 RAG 문서는 보통 300~1200 tokens 범위를 권장한다.

Q. Chunk Overlap은 왜 필요해?
A. Chunk 경계에서 문맥이 끊기는 문제를 줄이기 위해 필요하다.

Q. FAQ의 Q와 A는 분리해도 돼?
A. 권장하지 않는다. Q/A가 함께 있어야 질문 매칭과 답변 생성에 유리하다.

Q. 좋은 Chunk란 뭐야?
A. 하나의 개념을 담고 독립 검색되어도 의미가 유지되는 검색 단위다.

Q. Chunk가 너무 작으면 뭐가 문제야?
A. 문맥이 부족해 LLM이 답변에 필요한 정보를 충분히 얻지 못할 수 있다.

Q. Chunk가 너무 크면 뭐가 문제야?
A. 검색 정밀도가 낮아지고 관련 없는 내용이 Context에 섞일 수 있다.

Q. Chunk에 Metadata가 필요한 이유는?
A. 검색 결과의 출처와 Section을 추적하기 위해 필요하다.

Q. Embedding Model이 뭐야?
A. 텍스트를 유사도 검색이 가능한 Vector로 변환하는 모델이다.

Q. Embedding Model과 Chat Model은 달라?
A. 다르다. Embedding Model은 검색용 Vector를 만들고, Chat Model은 답변을 생성한다.

Q. Document Embedding과 Query Embedding은 뭐야?
A. Document Embedding은 문서 Chunk를 Vector로 바꾸는 것이고, Query Embedding은 사용자 질문을 Vector로 바꾸는 것이다.

Q. Embedding Model을 바꾸면 어떻게 해야 해?
A. 기존 Vector와 호환되지 않으므로 전체 문서를 Re-embedding해야 한다.

Q. Chat Model만 바꾸면 Re-embedding이 필요해?
A. 보통은 필요 없다. Re-embedding은 Embedding Model을 바꾸거나 문서 Chunk가 바뀔 때 필요하다.

Q. 한국어 RAG에는 어떤 Embedding이 필요해?
A. 한국어 또는 다국어 검색 품질이 좋은 Multilingual Embedding Model을 고려해야 한다.

Q. Vector Store가 뭐야?
A. Embedding Vector와 Metadata를 저장하고 유사도 검색을 수행하는 저장소다.

Q. Vector Store에는 Vector만 저장해도 돼?
A. 아니다. page_content와 source, section 같은 Metadata도 함께 저장해야 한다.

Q. Metadata Filter는 왜 필요해?
A. Backend, AI, Frontend 같은 Domain 범위를 제한해 검색 정확도를 높이기 위해 필요하다.

Q. Embedding Dimension이 안 맞으면 어떻게 돼?
A. Vector Store 저장 또는 검색이 실패할 수 있다.

Q. 문서 수정 후 Vector Store는 어떻게 해야 해?
A. 수정된 문서를 다시 적재하고 Re-embedding한 뒤 Vector Store를 갱신해야 한다.

Q. Retriever가 뭐야?
A. 사용자 질문과 관련된 문서 Chunk를 검색해 반환하는 구성 요소다.

Q. Retriever는 왜 중요해?
A. Retriever 결과가 LLM 답변의 근거가 되기 때문이다.

Q. Top-K는 뭐야?
A. 검색 결과로 반환할 문서 Chunk 개수다.

Q. Similarity Threshold는 왜 필요해?
A. 관련도가 낮은 문서가 Context에 들어가는 것을 막기 위해 필요하다.

Q. Retriever 결과는 바로 LLM에 넣어도 돼?
A. 권장하지 않는다. Source, Section, Score를 정리하는 Context Formatting 후 사용하는 것이 좋다.

Q. Metadata Filtering이 뭐야?
A. 문서의 domain, document, part, section 같은 Metadata 조건으로 검색 범위를 제한하는 방식이다.

Q. Metadata Filter를 너무 강하게 걸면 어떻게 돼?
A. 필요한 문서가 검색되지 않아 RAG 답변이 실패할 수 있다.

Q. PM Agent가 Metadata Filter를 선택할 수 있어?
A. 가능하다. PM Agent가 task_type을 분석해 적절한 Domain Filter를 선택할 수 있다.

Q. Metadata 이름은 자유롭게 써도 돼?
A. 권장하지 않는다. source, domain, document, part, section 같은 필드명을 일관되게 사용해야 한다.

Q. Golden Query Test가 뭐야?
A. 정해진 질문에 대해 예상 문서나 Chunk가 Retriever 결과에 포함되는지 확인하는 테스트다.

Q. Golden Query는 왜 필요해?
A. RAG 검색 품질을 객관적으로 확인하기 위해 필요하다.

Q. Golden Query 실패 시 무엇을 확인해?
A. Query 표현, Chunk 제목, FAQ, Retrieval Queries, Metadata Filter, Top-K, Threshold를 확인한다.

Q. 문서 수정 후 Golden Query를 다시 해야 해?
A. 해야 한다. 문서 구조와 Embedding 결과가 바뀔 수 있기 때문이다.

Q. Golden Query는 Part08과 어떻게 연결돼?
A. Part08의 Evaluation Set에서 Retriever 품질과 Agent Workflow 품질을 검증하는 기준으로 사용된다.

Q. 문서에 있는 내용인데 RAG가 못 찾는 이유는?
A. Chunk 품질, Metadata Filter, Top-K, Threshold, Embedding 모델, Query 표현 문제가 원인일 수 있다.

Q. Retriever가 엉뚱한 문서를 가져오면 어떻게 해?
A. Chunk 제목, FAQ, Metadata Filter, Threshold, Reranking을 점검해야 한다.

Q. Top-K를 늘리면 항상 좋아?
A. 아니다. 누락은 줄지만 관련 없는 Context가 섞일 수 있다.

Q. Threshold를 높이면 항상 좋아?
A. 아니다. 관련 문서까지 차단해 검색 실패가 발생할 수 있다.

Q. 검색 실패는 LLM 문제야?
A. 대부분은 LLM 문제가 아니라 Retrieval Pipeline 문제다.
