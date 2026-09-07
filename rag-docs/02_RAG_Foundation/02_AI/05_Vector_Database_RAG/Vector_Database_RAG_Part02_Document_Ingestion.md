# Vector Database & RAG Part02 Document Ingestion

---

# 1. Document Ingestion Core

## 1.1 Document Ingestion Definition

### [개념]

Document Ingestion은 원본 문서를 RAG 시스템이 검색할 수 있는 형태로 변환하여 Vector Database에 적재하는 과정이다.

Document Ingestion은 단순 파일 업로드가 아니다.

Document Ingestion은 문서 로딩, 전처리, Chunking, Metadata 부여, Embedding 생성, Vector Store 저장, Retrieval 검증까지 포함한다.

기본 흐름은 다음과 같다.

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

RAG 품질은 Document Ingestion 품질에서 시작된다.

문서가 잘못 적재되면 좋은 Embedding Model과 좋은 LLM을 사용해도 관련 문서가 검색되지 않거나 잘못된 답변이 생성될 수 있다.

---

### [핵심]

- Document Ingestion은 RAG 품질의 시작점
- 단순 파일 업로드가 아니라 검색 가능 구조로 변환하는 과정
- Loader, Preprocessing, Chunking, Metadata, Embedding, Vector Store 저장 포함
- 문서 원문과 Vector는 반드시 연결되어야 함
- Metadata는 출처 추적과 검색 필터링에 필요
- Ingestion 후 반드시 Retrieval Validation 수행
- 문서 수정 후 Reindex 누락 주의

---

### [실무]

2026 실무 기준 Document Ingestion은 RAG 시스템의 데이터 파이프라인으로 다룬다.

개인 AI 서버에서 RAG 문서를 업로드할 때도 다음 기준을 적용해야 한다.

- Markdown Header 구조 확인
- Chunk 단위 의미 독립성 확인
- Code Block 중간 분리 방지
- Table 의미 보존
- FAQ와 Retrieval Queries 포함
- 파일명, 도메인, 레벨, 섹션 Metadata 부여
- Embedding Model 이름 기록
- Vector Store Collection 기준 통일
- 업로드 후 Golden Query로 검색 검증

Agent용 RAG에서는 문서가 사람이 읽기 좋은 순서보다 검색과 재사용에 적합한 구조를 가져야 한다.

---

### [FAQ]

Q. Document Ingestion이 뭐야?

A.
원본 문서를 읽고 정리한 뒤 Chunking, Metadata, Embedding을 거쳐 Vector Database에 저장하는 과정이다.

Q. Document Ingestion은 파일 업로드랑 같아?

A.
아니다. 파일 업로드는 시작 단계일 뿐이고, 검색 가능한 구조로 변환하고 검증하는 과정까지 포함한다.

Q. Document Ingestion이 왜 중요해?

A.
문서 적재 품질이 낮으면 관련 내용이 있어도 Retrieval에 실패할 수 있기 때문이다.

Q. Ingestion 후 바로 사용하면 돼?

A.
바로 사용할 수는 있지만 Golden Query로 검색 검증을 해야 한다.

Q. 문서를 수정하면 다시 Ingestion해야 해?

A.
해야 한다. 문서 내용이 바뀌면 Embedding Vector와 Metadata도 최신 상태로 갱신해야 한다.

---

# 2. Document Source

## 2.1 Source Document Type

### [개념]

Document Source는 RAG에 적재할 원본 문서를 의미한다.

Document Source는 Markdown, PDF, HTML, 코드 파일, API 문서, 운영 문서, 프로젝트 규칙 문서, 회의 기록 등 다양한 형태가 될 수 있다.

RAG 문서 제작 기준에서는 Markdown 문서가 가장 적합하다.

Markdown은 Header, Code Block, Table, FAQ, Retrieval Queries를 구조적으로 표현할 수 있기 때문이다.

---

### [핵심]

- Document Source는 RAG 적재 대상 원본 문서
- Markdown은 RAG 문서 제작에 적합
- PDF는 구조 손실 가능성 주의
- HTML은 광고, 메뉴, 불필요한 Navigation 제거 필요
- 코드 파일은 설명과 함께 적재해야 검색 품질이 좋음
- 프로젝트 규칙 문서는 최신성 관리 필요
- 출처와 버전 Metadata 기록 필수

---

### [실무]

개인 AI 프로젝트에서는 다음 Source 유형을 구분해서 관리한다.

| Source Type      | 예시                                | Ingestion 주의점                      |
| ---------------- | ----------------------------------- | ------------------------------------- |
| Master Rules     | Master_RAG_Rules.md                 | 전체 문서 공통 규칙으로 우선순위 높음 |
| Domain Rules     | Vector_Database_RAG_Domain_Rules.md | 도메인별 문서 생성 기준으로 사용      |
| Project Progress | Project_Progress.md                 | 완료/계획 상태 최신성 관리 필요       |
| RAG Document     | Part01 ~ PartXX                     | Agent 검색용 본문 문서                |
| Code Snippet     | Java, Python, JavaScript 코드       | 설명과 함께 Chunk 유지                |
| API Document     | Endpoint, Request, Response         | Path, Method, DTO 키워드 유지         |
| Troubleshooting  | 오류, 원인, 해결                    | 에러 메시지 원문 보존                 |

Document Source는 파일명만으로 판단하지 말고 문서의 역할을 Metadata로 명확히 기록해야 한다.

---

### [FAQ]

Q. RAG에 어떤 문서를 넣을 수 있어?

A.
Markdown, PDF, HTML, 코드, API 문서, 운영 문서, 프로젝트 규칙 문서 등을 넣을 수 있다.

Q. RAG 문서에는 어떤 형식이 좋아?

A.
Markdown이 가장 적합하다. Header, Code Block, Table, FAQ 구조를 보존하기 좋기 때문이다.

Q. PDF는 RAG에 안 좋아?

A.
사용할 수 있지만 구조 손실, 표 깨짐, Header 인식 오류가 생길 수 있어 전처리가 필요하다.

Q. 코드 파일만 넣으면 검색이 잘 돼?

A.
항상 그렇지 않다. 코드의 목적, 사용 상황, 주의점을 함께 문서화하는 것이 좋다.

Q. Source Metadata는 왜 필요해?

A.
검색 결과의 출처, 버전, 도메인, 섹션을 추적하기 위해 필요하다.

---

# 3. Document Loader

## 3.1 Loader Role

### [개념]

Document Loader는 원본 문서를 읽어 RAG Pipeline에서 처리 가능한 Text 또는 Structured Document로 변환하는 구성 요소다.

Loader는 파일 형식에 따라 달라진다.

예를 들어 Markdown Loader는 Header와 Code Block을 보존해야 하고, PDF Loader는 페이지 구조와 표를 최대한 유지해야 한다.

Loader 단계에서 문서 구조가 깨지면 이후 Chunking과 Retrieval 품질도 낮아진다.

---

### [핵심]

- Loader는 원본 문서를 읽는 단계
- 파일 형식별 Loader 전략 필요
- Markdown은 Header와 Code Block 보존 중요
- PDF는 페이지, 문단, 표 구조 손실 주의
- HTML은 불필요한 메뉴, 광고, 스크립트 제거 필요
- Loader 결과는 Chunking 가능한 구조여야 함
- Loader 실패는 Retrieval 실패로 이어질 수 있음

---

### [실무]

Loader 선택 시 다음 기준을 확인한다.

| 문서 형식 | Loader 기준                    | 주의점                                 |
| --------- | ------------------------------ | -------------------------------------- |
| Markdown  | Header, Code Block, Table 보존 | 코드블록 중간 깨짐 금지                |
| PDF       | 페이지, 문단, 표 추출          | 표, 목차, 각주 왜곡 주의               |
| HTML      | 본문 추출                      | 광고, 메뉴, Footer 제거                |
| CSV       | Row 구조 보존                  | RAG보다 분석 Pipeline이 적합할 수 있음 |
| Code      | 파일명, 함수명, 클래스명 유지  | 설명 없는 코드 단독 적재 주의          |
| JSON      | Key 구조 보존                  | 중첩 구조 Flatten 기준 필요            |

개인 AI RAG 문서는 Markdown 기반으로 정리한 뒤 업로드하는 것이 가장 안정적이다.

---

### [FAQ]

Q. Document Loader가 뭐야?

A.
원본 문서를 읽어 RAG Pipeline이 처리할 수 있는 Text 또는 구조화 문서로 변환하는 단계다.

Q. Loader가 왜 중요해?

A.
Loader에서 문서 구조가 깨지면 Chunking과 Retrieval 품질이 함께 떨어지기 때문이다.

Q. Markdown Loader에서 중요한 건 뭐야?

A.
Header, Code Block, Table, FAQ 구조를 보존하는 것이다.

Q. PDF Loader에서 주의할 점은 뭐야?

A.
표, 페이지 순서, 문단 구분, Header 구조가 깨지지 않는지 확인해야 한다.

Q. HTML 문서는 어떻게 처리해야 해?

A.
본문만 남기고 메뉴, 광고, Footer, Script 같은 노이즈를 제거해야 한다.

---

# 4. Document Preprocessing

## 4.1 Preprocessing Purpose

### [개념]

Document Preprocessing은 검색 가능한 형태로 문서를 정리하는 과정이다.

Preprocessing은 문서의 의미를 유지하면서 검색 품질을 떨어뜨리는 노이즈를 제거한다.

Preprocessing 대상에는 불필요한 목차 반복, 광고성 문구, 깨진 문자, 중복 문장, 불필요한 Navigation, 잘못된 Header, 손상된 Code Block 등이 포함된다.

Preprocessing은 의미를 삭제하는 과정이 아니라 Retrieval 품질을 높이기 위해 문서 구조를 정리하는 과정이다.

---

### [핵심]

- Preprocessing은 문서를 검색 친화적으로 정리하는 과정
- Text Cleaning, Header Normalization, Duplicate Removal 포함
- Code Block Preservation 중요
- Table Handling 중요
- Link Handling 기준 필요
- Encoding 문제 확인 필요
- 과한 정제는 의미 손실을 유발할 수 있음

---

### [실무]

RAG 문서 전처리 시 다음 항목을 점검한다.

```text
Text Cleaning
→ Header Normalization
→ Code Block Preservation
→ Table Handling
→ Link Handling
→ Duplicate Removal
→ Noise Removal
→ Encoding Check
```

Markdown 문서에서는 Header Level을 일관되게 유지한다.

예시는 다음과 같다.

```md
# FileName

# Document Title

---

# 1. Main Section

## 1.1 Sub Section

### [개념]
```

Header가 불명확하면 Chunk 제목이 약해지고, Chunk 제목이 약하면 Retrieval Hit가 떨어질 수 있다.

---

### [FAQ]

Q. Document Preprocessing이 뭐야?

A.
검색 품질을 높이기 위해 문서 구조를 정리하고 노이즈를 제거하는 과정이다.

Q. 전처리에서 가장 중요한 건 뭐야?

A.
핵심 문맥을 삭제하지 않으면서 Header, Code Block, Table 구조를 보존하는 것이다.

Q. 노이즈는 어떤 걸 말해?

A.
반복 목차, 광고, 메뉴, 깨진 문자, 불필요한 Footer, 중복 문장 등이 노이즈다.

Q. 전처리를 많이 하면 좋은 거 아니야?

A.
아니다. 과한 정제는 핵심 의미를 손실시켜 Retrieval 품질을 떨어뜨릴 수 있다.

Q. 한글 문서에서 전처리 주의점은 뭐야?

A.
Encoding 깨짐, 띄어쓰기 훼손, 기술 용어 오타를 확인해야 한다.

---

## 4.2 Header Normalization

### [개념]

Header Normalization은 문서 제목과 섹션 구조를 일관되게 정리하는 작업이다.

RAG에서 Header는 Chunk Boundary와 Retrieval Signal로 사용된다.

명확한 Header는 사용자 Query와 문서 Chunk를 연결하는 역할을 한다.

예를 들어 `# 3. Document Ingestion` 같은 Header는 문서 적재 관련 Query와 매칭되기 쉽다.

반대로 `# 기타`, `# 설명`, `# 내용` 같은 Header는 검색 의미가 약하다.

---

### [핵심]

- Header는 Chunk Boundary로 사용 가능
- Header는 Retrieval Signal 역할
- Header에는 핵심 키워드 포함 필요
- 모호한 Header 사용 금지
- Header Level 일관성 유지
- 한글과 영어 핵심 용어 병기 가능
- Section 제목은 Agent가 문맥을 판단하는 기준

---

### [실무]

좋은 Header 예시는 다음과 같다.

```md
# 3. Document Ingestion Pipeline

## 3.1 Loader and Preprocessing

## 3.2 Chunking and Metadata

## 3.3 Embedding and Vector Store Upsert
```

나쁜 Header 예시는 다음과 같다.

```md
# 설명

## 기타

## 내용

## 참고
```

기술 RAG 문서에서는 Header에 핵심 용어를 직접 포함한다.

예를 들어 `Chunking`, `Embedding`, `Metadata`, `Vector Store`, `Retrieval`, `Reindex` 같은 용어는 Header와 FAQ에 반복해서 포함해도 된다.

---

### [FAQ]

Q. Header Normalization이 뭐야?

A.
문서 제목과 섹션 구조를 일관되게 정리하는 작업이다.

Q. Header가 Retrieval에 영향을 줘?

A.
그렇다. Header는 Chunk 의미와 검색 키워드를 강화하는 역할을 한다.

Q. 좋은 Header는 어떤 형태야?

A.
핵심 용어가 포함되고, 해당 Chunk의 주제를 명확히 설명하는 Header다.

Q. 나쁜 Header는 어떤 형태야?

A.
`기타`, `내용`, `설명`처럼 검색 의미가 약한 Header다.

Q. Header에 영어 용어를 넣어도 돼?

A.
가능하다. 기술 문서에서는 한글과 영어 핵심 용어를 함께 쓰면 검색 매칭에 도움이 된다.

---

# 5. Code Block Preservation

## 5.1 Code Block Handling

### [개념]

Code Block Preservation은 문서 전처리와 Chunking 과정에서 코드 예제가 깨지지 않도록 보존하는 규칙이다.

RAG에서 코드 예제는 Code Generation과 Review에 직접 사용된다.

Code Block이 중간에 잘리거나 설명과 분리되면 Agent가 잘못된 코드를 생성할 수 있다.

Code Block은 가능한 한 관련 설명과 같은 Chunk에 유지해야 한다.

---

### [핵심]

- Code Block은 중간 분리 금지
- Code Example과 설명은 같은 Chunk에 유지 권장
- 불필요한 긴 전체 코드는 피함
- 핵심 로직 중심 Snippet 권장
- 코드 언어 표시 권장
- 코드블록 id="" 제거
- 코드 문법 훼손 금지

---

### [실무]

RAG 문서용 Code Block은 짧고 직접적이어야 한다.

좋은 예시는 다음과 같다.

```java
public ApiResponse<UserResDto> getUser(Long userId) {
    User user = userRepository.findById(userId)
        .orElseThrow(() -> new EntityNotFoundException("User not found"));

    return ApiResponse.success(UserResDto.from(user));
}
```

코드 예제는 다음 정보와 함께 배치하면 Retrieval 품질이 좋아진다.

- 사용 상황
- 핵심 메서드명
- 주의점
- 반환 타입
- 예외 처리 기준

나쁜 예시는 설명 없이 긴 전체 클래스를 그대로 넣는 방식이다.

RAG Agent는 긴 코드보다 검색 가능한 핵심 Snippet과 명확한 설명을 더 잘 활용한다.

---

### [FAQ]

Q. Code Block Preservation이 뭐야?

A.
문서 처리 과정에서 코드블록이 깨지거나 중간에 잘리지 않도록 보존하는 규칙이다.

Q. 코드블록은 왜 설명과 같이 있어야 해?

A.
Agent가 코드의 목적과 사용 조건을 함께 검색하고 이해해야 하기 때문이다.

Q. 긴 전체 클래스 코드를 넣어도 돼?

A.
가능은 하지만 RAG 문서에서는 핵심 로직 중심의 짧은 Snippet이 더 적합하다.

Q. 코드블록 id=""는 제거해야 해?

A.
해야 한다. 불필요한 속성은 문서 노이즈가 될 수 있다.

Q. 코드 예제가 Retrieval에 도움이 돼?

A.
그렇다. 메서드명, 클래스명, API 패턴 검색에 도움이 된다.

---

# 6. Table Handling

## 6.1 Table Preservation

### [개념]

Table Handling은 표 데이터를 RAG 검색에 적합한 형태로 보존하는 규칙이다.

표는 비교, 설정값, 옵션, 정책, 체크리스트를 표현할 때 유용하다.

하지만 PDF나 HTML에서 추출한 표는 구조가 깨질 수 있다.

RAG 문서에서는 Markdown Table 또는 구조화된 Bullet로 표의 의미를 유지해야 한다.

---

### [핵심]

- Table은 비교와 정책 정리에 유용
- Markdown Table 권장
- 표 구조 깨짐 주의
- 너무 큰 표는 분리 권장
- 표 제목과 설명 필요
- 각 행이 독립적으로 의미를 가져야 함
- 복잡한 표는 Bullet 구조로 변환 가능

---

### [실무]

좋은 Markdown Table 예시는 다음과 같다.

```md
| 단계      | 목적           | 주의점                    |
| --------- | -------------- | ------------------------- |
| Load      | 원본 문서 읽기 | 구조 손실 주의            |
| Clean     | 노이즈 제거    | 핵심 문맥 삭제 금지       |
| Chunking  | 검색 단위 분리 | Code Block 중간 분리 금지 |
| Embedding | Vector 생성    | Model 일관성 필요         |
| Upsert    | Vector DB 저장 | Metadata 누락 주의        |
```

표가 너무 크면 Retrieval 단위가 넓어져 검색 정밀도가 떨어질 수 있다.

큰 표는 다음 기준으로 분리한다.

- 기능별 분리
- 설정 범위별 분리
- Agent 역할별 분리
- Error / Cause / Solution 구조로 분리

---

### [FAQ]

Q. Table Handling이 뭐야?

A.
표 데이터를 검색 가능한 Markdown Table 또는 구조화 텍스트로 보존하는 규칙이다.

Q. 표는 RAG에 좋아?

A.
비교, 설정, 정책, 체크리스트에는 좋지만 너무 큰 표는 검색 정밀도를 떨어뜨릴 수 있다.

Q. PDF 표가 깨지면 어떻게 해?

A.
Markdown Table로 다시 정리하거나 Bullet 구조로 변환해야 한다.

Q. 표에도 제목이 필요해?

A.
필요하다. 표 제목과 설명이 있어야 검색 결과의 의미가 명확해진다.

Q. 큰 표는 어떻게 처리해?

A.
주제별로 분리하거나 Bullet 구조로 바꿔 Chunk 의미를 명확히 한다.

---

# 7. Metadata Attach

## 7.1 Metadata Purpose

### [개념]

Metadata는 문서 Chunk의 출처, 역할, 도메인, 레벨, 섹션, 버전 정보를 설명하는 부가 정보다.

RAG에서 Metadata는 검색 결과의 출처 추적, Agent Routing, Filtered Search, 최신성 판단에 사용된다.

Vector만 저장하고 Metadata를 생략하면 검색 결과가 어디에서 왔는지 추적하기 어렵다.

Metadata는 RAG 답변의 신뢰도와 검증 가능성을 높인다.

---

### [핵심]

- Metadata는 Chunk 출처 추적에 필요
- Domain / Level / Section은 Agent Routing에 도움
- Version / updatedAt은 최신성 판단에 필요
- source / fileName / documentId / chunkId 필수 권장
- tags는 검색 확장에 도움
- Metadata 필드명 통일 필요
- 잘못된 Metadata는 잘못된 검색 결과를 유발

---

### [실무]

RAG 문서 Chunk Metadata 예시는 다음과 같다.

```json
{
  "source": "Vector_Database_RAG_Part02_Document_Ingestion.md",
  "fileName": "Vector_Database_RAG_Part02_Document_Ingestion.md",
  "documentId": "vector-database-rag-part02",
  "chunkId": "vector-database-rag-part02-007",
  "domain": "AI",
  "level": "Foundation",
  "category": "Vector Database & RAG",
  "section": "Metadata Attach",
  "title": "Metadata Purpose",
  "tags": ["rag", "metadata", "document-ingestion", "vector-database"],
  "version": "2026-06",
  "updatedAt": "2026-06-30"
}
```

개인 AI Agent 구조에서는 Metadata를 통해 Agent가 어떤 문서를 우선 참조해야 하는지 판단할 수 있다.

예를 들어 Backend Agent는 Backend Domain 문서를 우선 검색하고, AI Agent는 AI Foundation 문서를 우선 검색할 수 있다.

---

### [FAQ]

Q. Metadata가 뭐야?

A.
문서 Chunk의 출처, 도메인, 레벨, 섹션, 버전 등을 설명하는 부가 정보다.

Q. Metadata는 왜 필요해?

A.
검색 결과의 출처 추적, 필터링, Agent Routing, 최신성 판단에 필요하다.

Q. Metadata 없이 Vector만 저장하면 안 돼?

A.
권장하지 않는다. 출처와 문맥을 추적하기 어려워 답변 검증이 약해진다.

Q. 필수 Metadata에는 뭐가 있어?

A.
source, fileName, documentId, chunkId, domain, level, section, tags, version, updatedAt을 권장한다.

Q. Metadata가 잘못되면 어떻게 돼?

A.
잘못된 문서가 검색되거나 Agent가 잘못된 도메인 기준으로 답변할 수 있다.

---

# 8. Embedding and Vector Store Upsert

## 8.1 Embedding Generation

### [개념]

Embedding Generation은 전처리와 Chunking이 완료된 Text Chunk를 Embedding Vector로 변환하는 단계다.

RAG에서는 Document Chunk와 User Query를 같은 Embedding Model로 Vector화한다.

Embedding Vector는 Vector Database에 저장되어 Similarity Search에 사용된다.

Embedding Model과 Vector Dimension이 일치하지 않으면 검색이 실패하거나 Vector Store에 저장할 수 없다.

---

### [핵심]

- Embedding은 Text Chunk를 Vector로 변환
- Chunk와 Query는 같은 Embedding Model 사용
- Embedding Model 이름과 버전 기록 권장
- Vector Dimension 일치 필요
- 한 Collection에는 같은 Embedding Model 사용 권장
- Embedding Model 변경 시 Reindex 필요
- Embedding 전 Chunk 품질 확인 필요

---

### [실무]

Embedding 생성 전 다음을 확인한다.

```text
Chunk Meaning Check
→ Metadata Check
→ Embedding Model Check
→ Vector Dimension Check
→ Collection Policy Check
→ Generate Embedding
```

개인 AI 서버에서는 BGE-M3 같은 다국어 Embedding Model을 사용할 수 있다.

하지만 Embedding Model이 좋아도 Chunk가 잘못 나뉘면 검색 품질은 낮아진다.

Embedding은 문서 품질을 보완하는 도구가 아니라 문서 의미를 Vector로 표현하는 도구다.

---

### [FAQ]

Q. Embedding Generation이 뭐야?

A.
Text Chunk를 의미 검색에 사용할 수 있는 Embedding Vector로 변환하는 단계다.

Q. Embedding 전에 무엇을 확인해야 해?

A.
Chunk 의미, Metadata, Embedding Model, Vector Dimension, Collection 기준을 확인해야 한다.

Q. 같은 Collection에 여러 Embedding Model을 섞어도 돼?

A.
권장하지 않는다. Vector 공간이 달라져 Similarity Search 품질이 깨질 수 있다.

Q. Embedding Model을 바꾸면 어떻게 해야 해?

A.
기존 Vector를 삭제하거나 분리하고 전체 문서를 다시 Embedding해야 한다.

Q. Embedding은 문서 품질 문제를 해결해줘?

A.
아니다. Chunk와 문서 구조가 나쁘면 좋은 Embedding Model을 써도 검색 품질이 낮다.

---

## 8.2 Vector Store Upsert

### [개념]

Vector Store Upsert는 생성된 Embedding Vector, Original Text, Metadata를 Vector Database에 저장하거나 갱신하는 단계다.

Upsert는 Insert와 Update를 합친 개념이다.

같은 documentId 또는 chunkId가 이미 존재하면 기존 값을 갱신하고, 없으면 새로 저장한다.

Upsert 정책이 없으면 중복 Chunk가 쌓이거나 오래된 문서가 검색될 수 있다.

---

### [핵심]

- Upsert는 Vector 저장 또는 갱신
- Vector + Original Text + Metadata 함께 저장
- documentId / chunkId 기준 필요
- 중복 저장 방지 필요
- 문서 수정 시 기존 Chunk 갱신 필요
- 삭제된 문서의 Vector 제거 필요
- Upsert 후 Retrieval Validation 수행

---

### [실무]

Vector Store Upsert 기본 구조는 다음과 같다.

```text
Chunk Text
+ Embedding Vector
+ Metadata
+ Document ID
+ Chunk ID
→ Vector Store Upsert
```

Upsert 정책 예시는 다음과 같다.

| 상황                 | 처리                                 |
| -------------------- | ------------------------------------ |
| 신규 문서            | 새 documentId로 Insert               |
| 기존 문서 수정       | 동일 documentId 기준 기존 Chunk 갱신 |
| 문서 삭제            | 해당 documentId Chunk 전체 Delete    |
| Embedding Model 변경 | Collection 분리 또는 전체 Reindex    |
| Metadata 변경        | Metadata 갱신 후 Retrieval 검증      |
| Chunk 구조 변경      | 기존 Chunk 삭제 후 재적재            |

RAG 문서 운영에서는 오래된 Vector가 남지 않도록 Delete / Reindex 정책을 반드시 정해야 한다.

---

### [FAQ]

Q. Vector Store Upsert가 뭐야?

A.
Embedding Vector, Original Text, Metadata를 Vector Database에 저장하거나 갱신하는 단계다.

Q. Upsert와 Insert 차이는 뭐야?

A.
Insert는 새로 저장만 하고, Upsert는 기존 값이 있으면 갱신하고 없으면 새로 저장한다.

Q. Upsert 기준은 뭐로 잡아야 해?

A.
documentId와 chunkId를 기준으로 잡는 것이 좋다.

Q. 중복 Chunk가 쌓이면 어떻게 돼?

A.
검색 결과가 중복되고 오래된 내용이 답변에 섞일 수 있다.

Q. 문서 삭제 시 Vector도 삭제해야 해?

A.
해야 한다. 원본 문서가 삭제되었는데 Vector가 남아 있으면 오래된 정보가 검색될 수 있다.

---

# 9. Ingestion Validation

## 9.1 Retrieval Validation

### [개념]

Retrieval Validation은 Document Ingestion 이후 문서가 실제로 검색되는지 확인하는 검증 단계다.

RAG에서는 문서가 Vector Database에 저장되었다고 해서 검색 품질이 보장되지 않는다.

Golden Query를 사용해 기대 Chunk가 Top-K 결과에 포함되는지 확인해야 한다.

기본 흐름은 다음과 같다.

```text
Golden Query
→ Query Embedding
→ Vector Search
→ Check Expected Chunk
→ Check Context Quality
→ Record Result
```

---

### [핵심]

- Ingestion 후 Retrieval Validation 필수
- Golden Query 사용 권장
- 기대 Chunk가 Top-K에 포함되는지 확인
- 검색 결과의 Chunk 품질 확인
- Metadata Filter 결과 확인
- 낮은 Score 또는 누락 Chunk 기록
- 실패 사례를 문서 개선에 반영

---

### [실무]

Retrieval Validation 테스트 예시는 다음과 같다.

```text
Golden Query:
Document Ingestion이 뭐야?

Expected File:
Vector_Database_RAG_Part02_Document_Ingestion.md

Expected Section:
Document Ingestion Core

Pass Criteria:
Expected Chunk appears in Top-K.
Chunk contains definition, core flow, and practical ingestion rules.
```

검증 실패 시 다음 순서로 수정한다.

1. Header 보강
2. FAQ 질문 표현 추가
3. Retrieval Queries 추가
4. 핵심 키워드 반복
5. Chunk 분리 조정
6. Metadata 확인
7. Reindex 수행
8. Top-K / Threshold 조정

---

### [FAQ]

Q. Retrieval Validation이 뭐야?

A.
문서 적재 후 기대 문서가 실제 검색 결과에 나오는지 확인하는 과정이다.

Q. Ingestion 후 검증이 꼭 필요해?

A.
필요하다. 저장은 되었지만 검색되지 않는 문서가 생길 수 있기 때문이다.

Q. Golden Query는 어떻게 만들어?

A.
실제 사용자가 물어볼 질문을 기준으로 만들고 기대 파일과 기대 섹션을 지정한다.

Q. 검증 실패하면 어떻게 해?

A.
Header, FAQ, Retrieval Queries, Chunk 구조, Metadata, Reindex 여부를 점검한다.

Q. Top-K에 기대 문서가 없으면 무슨 문제야?

A.
Chunk 구조, 키워드, Metadata Filter, Embedding, Top-K 설정 문제일 수 있다.

---

# 10. Reindex Policy

## 10.1 Reindex Definition

### [개념]

Reindex는 기존 문서의 Vector를 삭제하거나 갱신한 뒤 다시 Embedding하여 Vector Database에 저장하는 과정이다.

RAG 문서가 수정되면 기존 Embedding Vector는 오래된 문서 내용을 가리킬 수 있다.

Embedding Model이 변경되거나 Metadata 구조가 변경된 경우에도 Reindex가 필요하다.

Reindex 정책이 없으면 오래된 문서, 중복 Chunk, 잘못된 Metadata가 검색 결과에 남을 수 있다.

---

### [핵심]

- Reindex는 Vector 재생성 및 재저장 과정
- 문서 수정 시 Reindex 필요
- Embedding Model 변경 시 Reindex 필수
- Chunk 구조 변경 시 기존 Vector 삭제 후 재적재 권장
- Metadata 변경 시 갱신 필요
- 오래된 Vector 삭제 필요
- Reindex 후 Retrieval Validation 수행

---

### [실무]

Reindex가 필요한 상황은 다음과 같다.

| 상황                   | Reindex 필요 여부 | 이유                           |
| ---------------------- | ----------------: | ------------------------------ |
| 문서 내용 수정         |              필요 | 기존 Vector가 이전 내용을 반영 |
| Header 수정            |              필요 | Chunk 의미와 검색 Signal 변경  |
| FAQ 추가               |              필요 | 검색 매칭 문장 추가            |
| Retrieval Queries 추가 |              필요 | Query Matching 강화            |
| Metadata 수정          |              필요 | Filter와 출처 추적 기준 변경   |
| Embedding Model 변경   |              필수 | Vector 공간 변경               |
| Chunk Size 변경        |              필수 | Chunk ID와 의미 단위 변경      |
| 문서 삭제              |       Delete 필요 | 오래된 검색 결과 제거          |

Reindex 후에는 반드시 Golden Query로 검색 결과를 확인한다.

---

### [FAQ]

Q. Reindex가 뭐야?

A.
문서를 다시 Embedding하고 Vector Database에 갱신 저장하는 과정이다.

Q. 문서를 조금만 수정해도 Reindex해야 해?

A.
검색에 영향을 줄 수 있는 수정이라면 해야 한다.

Q. FAQ 추가해도 Reindex해야 해?

A.
해야 한다. FAQ는 Retrieval Matching에 직접 영향을 준다.

Q. Embedding Model을 바꾸면 Reindex가 필수야?

A.
필수다. Vector 공간이 달라지기 때문에 기존 Vector를 재사용하면 안 된다.

Q. Reindex 후 뭘 확인해야 해?

A.
Golden Query로 기대 Chunk가 Top-K에 들어오는지 확인해야 한다.

---

# 11. Common Ingestion Failures

## 11.1 Document Exists But Not Retrieved

### [개념]

문서가 Vector Database에 존재하지만 검색되지 않는 문제는 대표적인 Ingestion Failure다.

이 문제는 문서 저장 실패보다 더 위험하다.

시스템상 문서는 존재하지만 Agent가 검색하지 못하기 때문에 답변에서는 없는 문서처럼 취급된다.

---

### [핵심]

- 문서가 있어도 검색되지 않을 수 있음
- Header가 약하면 검색 Signal 부족
- Chunk가 너무 크면 핵심 주제가 흐려짐
- Chunk가 너무 작으면 문맥 부족
- FAQ가 없으면 사용자 질문 표현과 매칭 약화
- Metadata Filter가 잘못되면 검색에서 제외
- Reindex 누락 시 오래된 Vector 검색 가능

---

### [실무]

문제 해결 형식은 다음과 같다.

```text
문제:
문서에 있는 내용이 검색되지 않음

원인:
Header 불명확
Chunk 구조 부적절
핵심 키워드 누락
FAQ 부족
Retrieval Queries 부족
Metadata 오류
Embedding 재생성 누락

해결:
Header 보강
Chunk 재분리
핵심 키워드 추가
FAQ 질문 추가
Retrieval Queries 보강
Metadata 수정
Reindex 수행
Golden Query 재검증
```

이 문제는 LLM 성능 문제가 아니라 Ingestion과 Retrieval 문제일 가능성이 높다.

---

### [FAQ]

Q. 문서가 있는데 왜 검색되지 않아?

A.
Header, Chunk, FAQ, Metadata, Embedding, Top-K, Threshold 문제일 수 있다.

Q. 이 문제는 LLM 문제야?

A.
대부분 LLM 문제가 아니라 Ingestion 또는 Retrieval 문제다.

Q. 검색 안 되는 문서는 어떻게 고쳐?

A.
Header, FAQ, Retrieval Queries, Metadata를 보강하고 Reindex해야 한다.

Q. Chunk가 너무 크면 왜 문제야?

A.
여러 주제가 섞여 Similarity Search 정밀도가 떨어질 수 있다.

Q. Chunk가 너무 작으면 왜 문제야?

A.
검색은 되더라도 답변에 필요한 문맥이 부족할 수 있다.

---

## 11.2 Outdated Document Retrieved

### [개념]

Outdated Document Retrieved는 최신 문서가 아니라 오래된 문서가 검색되는 문제다.

문서 수정 후 기존 Vector를 삭제하지 않았거나, version Metadata가 없거나, 중복 문서가 존재할 때 발생한다.

이 문제는 Agent가 과거 기준으로 답변하게 만드는 위험한 RAG 장애다.

---

### [핵심]

- 오래된 문서 검색은 RAG 신뢰도 저하 원인
- Reindex 누락이 주요 원인
- Delete Policy 부재 시 이전 Vector 잔존
- Version Metadata 없으면 최신성 판단 어려움
- 중복 문서가 있으면 충돌 Context 발생
- 최신 문서 우선순위 기준 필요
- Project Progress와 문서 Registry 최신화 필요

---

### [실무]

문제 해결 형식은 다음과 같다.

```text
문제:
최신 문서가 아니라 오래된 문서가 검색됨

원인:
Reindex 누락
오래된 Vector 삭제 안 됨
version Metadata 없음
updatedAt Metadata 없음
중복 문서 존재
Collection 정리 안 됨

해결:
기존 Vector 삭제
최신 문서 재적재
version / updatedAt Metadata 추가
중복 문서 제거
최신 문서 우선순위 적용
Golden Query 재검증
```

개인 AI 프로젝트에서는 Project Progress와 Domain Rules를 최신 상태로 유지해야 Agent가 완료 문서와 예정 문서를 혼동하지 않는다.

---

### [FAQ]

Q. 오래된 문서가 검색되면 왜 위험해?

A.
Agent가 과거 규칙이나 이전 진행 상황을 기준으로 답변할 수 있기 때문이다.

Q. 오래된 문서가 검색되는 원인은 뭐야?

A.
Reindex 누락, 오래된 Vector 잔존, version Metadata 누락, 중복 문서 때문이다.

Q. version Metadata가 왜 필요해?

A.
최신 문서와 이전 문서를 구분하기 위해 필요하다.

Q. 문서 수정 후 이전 Vector는 삭제해야 해?

A.
해야 한다. 삭제하지 않으면 오래된 내용이 검색될 수 있다.

Q. Project Progress도 Reindex 대상이야?

A.
그렇다. 진행 상황이 바뀌면 최신 상태로 Reindex해야 한다.

---

# 12. Ingestion Checklist

## 12.1 Final Checklist

### [개념]

Ingestion Checklist는 문서를 Vector Database에 적재하기 전후로 확인해야 하는 검수 기준이다.

Checklist는 Document Quality, Chunk Quality, Metadata Quality, Embedding Quality, Retrieval Quality를 나눠 점검한다.

Ingestion Checklist를 사용하면 문서 업로드 후 검색 실패, 중복 검색, 오래된 문서 검색, 출처 누락 문제를 줄일 수 있다.

---

### [핵심]

- Ingestion 전 문서 구조 점검
- Chunk 의미 독립성 확인
- Code Block 깨짐 확인
- Metadata 필드 확인
- Embedding Model 확인
- Collection 기준 확인
- Upsert / Delete 정책 확인
- Golden Query 검증 수행

---

### [실무]

최종 Ingestion Checklist는 다음과 같다.

```md
### [Checklist]

- [ ] Document Source가 명확한가?
- [ ] FileName이 규칙에 맞는가?
- [ ] Document Title이 명확한가?
- [ ] Header 구조가 일관적인가?
- [ ] Chunk가 하나의 개념만 다루는가?
- [ ] Chunk가 독립 검색되어도 의미가 유지되는가?
- [ ] Code Block이 중간에 잘리지 않았는가?
- [ ] 코드블록 id=""가 제거되었는가?
- [ ] Table 구조가 깨지지 않았는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되어 있는가?
- [ ] 핵심 키워드가 Header / FAQ / 본문에 포함되어 있는가?
- [ ] Metadata 필드가 통일되었는가?
- [ ] source / fileName / documentId / chunkId가 있는가?
- [ ] domain / level / section / version이 있는가?
- [ ] Embedding Model 이름을 기록했는가?
- [ ] Vector Dimension이 일치하는가?
- [ ] Collection 기준이 명확한가?
- [ ] Upsert 정책이 있는가?
- [ ] Delete / Reindex 정책이 있는가?
- [ ] Golden Query로 Retrieval 검증을 했는가?
```

Checklist는 문서 제작 완료 후, Vector Store 적재 전, Reindex 후에 반복해서 사용한다.

---

### [FAQ]

Q. Ingestion Checklist는 왜 필요해?

A.
문서 적재 후 검색 실패와 오래된 문서 검색 문제를 줄이기 위해 필요하다.

Q. Checklist는 언제 사용해?

A.
문서 제작 완료 후, Vector Store 적재 전, Reindex 후에 사용한다.

Q. 가장 중요한 Checklist 항목은 뭐야?

A.
Chunk 의미 독립성, Metadata, Code Block 보존, Retrieval Queries, Golden Query 검증이다.

Q. Checklist를 생략하면 어떻게 돼?

A.
문서는 업로드되어도 검색되지 않거나 잘못된 Context가 답변에 사용될 수 있다.

Q. Agent용 RAG 문서에서도 Checklist가 필요해?

A.
필요하다. Agent는 검색 결과를 기준으로 작업하므로 문서 품질 검수가 중요하다.

---

# Retrieval Queries

### [FAQ]

Q. Document Ingestion이 뭐야?
A. 원본 문서를 읽고 정리한 뒤 Chunking, Metadata, Embedding을 거쳐 Vector Database에 저장하는 과정이다.

Q. Document Ingestion은 파일 업로드랑 같아?
A. 아니다. 파일 업로드는 시작 단계이고, RAG 검색을 위한 전처리, Chunking, Embedding, 검증까지 포함한다.

Q. RAG에서 Document Ingestion이 중요한 이유는 뭐야?
A. 문서 적재 품질이 낮으면 관련 내용이 있어도 Retrieval에 실패할 수 있기 때문이다.

Q. Document Ingestion Flow는 어떻게 돼?
A. Raw Document를 Load, Clean, Chunking, Metadata 부여, Embedding 생성, Vector DB 저장, Retrieval 검증 순서로 처리한다.

Q. Document Source가 뭐야?
A. RAG에 적재할 원본 문서다.

Q. RAG 문서 Source로 어떤 형식이 좋아?
A. Markdown이 가장 적합하다. Header, Code Block, Table, FAQ 구조를 보존하기 좋기 때문이다.

Q. PDF를 RAG에 넣을 때 주의할 점은 뭐야?
A. 표, 문단, Header, 페이지 순서가 깨지지 않는지 확인해야 한다.

Q. HTML을 RAG에 넣을 때 주의할 점은 뭐야?
A. 메뉴, 광고, Footer, Script 같은 노이즈를 제거하고 본문만 추출해야 한다.

Q. 코드 파일을 RAG에 넣어도 돼?
A. 가능하지만 코드 목적, 사용 상황, 주의점 설명과 함께 적재하는 것이 좋다.

Q. Document Loader가 뭐야?
A. 원본 문서를 읽어 RAG Pipeline이 처리할 수 있는 Text 또는 구조화 문서로 변환하는 단계다.

Q. Loader가 중요한 이유는 뭐야?
A. Loader 단계에서 문서 구조가 깨지면 Chunking과 Retrieval 품질도 떨어지기 때문이다.

Q. Markdown Loader에서 중요한 건 뭐야?
A. Header, Code Block, Table, FAQ 구조를 보존하는 것이다.

Q. Document Preprocessing이 뭐야?
A. 검색 품질을 높이기 위해 문서 구조를 정리하고 노이즈를 제거하는 과정이다.

Q. RAG 문서 전처리에서 제거할 노이즈는 뭐야?
A. 반복 목차, 광고, 메뉴, 깨진 문자, 불필요한 Footer, 중복 문장 등이다.

Q. 전처리를 많이 하면 좋아?
A. 아니다. 과한 전처리는 핵심 의미를 손실시켜 Retrieval 품질을 떨어뜨릴 수 있다.

Q. Header Normalization이 뭐야?
A. 문서 제목과 섹션 구조를 일관되게 정리하는 작업이다.

Q. Header가 Retrieval에 왜 중요해?
A. Header는 Chunk Boundary와 Retrieval Signal 역할을 하기 때문이다.

Q. 좋은 Header는 뭐야?
A. 핵심 용어가 포함되고 해당 Chunk의 주제를 명확히 설명하는 Header다.

Q. 나쁜 Header는 뭐야?
A. `기타`, `설명`, `내용`처럼 검색 의미가 약한 Header다.

Q. Code Block Preservation이 뭐야?
A. 문서 처리 과정에서 코드블록이 깨지거나 중간에 잘리지 않도록 보존하는 규칙이다.

Q. 코드블록은 설명과 같이 있어야 해?
A. 가능하면 같이 있어야 한다. Agent가 코드 목적과 조건을 함께 검색해야 하기 때문이다.

Q. 코드블록 id=""는 제거해야 해?
A. 제거해야 한다. 불필요한 속성은 RAG 문서 노이즈가 될 수 있다.

Q. Table Handling이 뭐야?
A. 표 데이터를 Markdown Table 또는 구조화 텍스트로 보존하는 규칙이다.

Q. 큰 표는 RAG에 안 좋아?
A. 너무 큰 표는 검색 정밀도를 떨어뜨릴 수 있으므로 주제별로 분리하는 것이 좋다.

Q. Metadata Attach가 뭐야?
A. Chunk에 source, fileName, documentId, chunkId, domain, level, section, version 같은 정보를 붙이는 과정이다.

Q. Metadata는 왜 필요해?
A. 출처 추적, 검색 필터링, Agent Routing, 최신성 판단에 필요하다.

Q. 필수 Metadata는 뭐야?
A. source, fileName, documentId, chunkId, domain, level, category, section, title, tags, version, updatedAt을 권장한다.

Q. Metadata 없이 Vector만 저장해도 돼?
A. 권장하지 않는다. 출처와 문맥을 추적하기 어려워 답변 검증이 약해진다.

Q. Embedding Generation이 뭐야?
A. Text Chunk를 의미 검색에 사용할 수 있는 Embedding Vector로 변환하는 단계다.

Q. Embedding 전에 확인할 것은 뭐야?
A. Chunk 의미, Metadata, Embedding Model, Vector Dimension, Collection 기준을 확인해야 한다.

Q. 같은 Collection에 여러 Embedding Model을 섞어도 돼?
A. 권장하지 않는다. Vector 공간이 달라져 Similarity Search 품질이 깨질 수 있다.

Q. Vector Store Upsert가 뭐야?
A. Embedding Vector, Original Text, Metadata를 Vector Database에 저장하거나 갱신하는 단계다.

Q. Upsert 기준은 뭐로 잡아야 해?
A. documentId와 chunkId를 기준으로 잡는 것이 좋다.

Q. 중복 Chunk가 쌓이면 어떻게 돼?
A. 검색 결과가 중복되고 오래된 내용이 답변에 섞일 수 있다.

Q. Retrieval Validation이 뭐야?
A. 문서 적재 후 기대 문서가 실제 검색 결과에 나오는지 확인하는 과정이다.

Q. Golden Query는 뭐야?
A. RAG 검색 품질을 검증하기 위해 미리 정한 테스트 질문이다.

Q. Ingestion 후 검증 실패하면 어떻게 해?
A. Header, FAQ, Retrieval Queries, Chunk 구조, Metadata, Reindex 여부를 점검한다.

Q. Reindex가 뭐야?
A. 문서를 다시 Embedding하고 Vector Database에 갱신 저장하는 과정이다.

Q. Reindex는 언제 해야 해?
A. 문서 수정, Header 수정, FAQ 추가, Metadata 변경, Embedding Model 변경, Chunk 구조 변경 시 해야 한다.

Q. 오래된 문서가 검색되면 어떻게 해?
A. 기존 Vector를 삭제하고 최신 문서를 재적재하며 version과 updatedAt Metadata를 추가해야 한다.

Q. 문서가 있는데 검색되지 않으면 어떻게 해?
A. Header, Chunk 구조, FAQ, Retrieval Queries, Metadata, Embedding, Top-K, Threshold를 확인해야 한다.

Q. Ingestion Checklist는 왜 필요해?
A. 문서 적재 후 검색 실패와 오래된 문서 검색 문제를 줄이기 위해 필요하다.

Q. Ingestion Checklist에서 가장 중요한 항목은 뭐야?
A. Chunk 의미 독립성, Metadata, Code Block 보존, Retrieval Queries, Golden Query 검증이다.

Q. Agent용 RAG 문서에서 Ingestion이 중요한 이유는 뭐야?
A. Agent는 검색된 문서를 기준으로 작업하므로 문서 적재 품질이 Agent 답변 품질을 결정하기 때문이다.
