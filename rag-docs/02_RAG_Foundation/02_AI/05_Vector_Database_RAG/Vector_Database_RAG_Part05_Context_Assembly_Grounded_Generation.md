# Vector Database & RAG Part05 Context Assembly and Grounded Generation

---

# 1. Context Assembly Core

## 1.1 Context Assembly Definition

### [개념]

Context Assembly는 Retrieval 단계에서 검색된 Chunk를 LLM Prompt에 넣을 Context로 구성하는 과정이다.

RAG에서 검색된 Chunk를 그대로 모두 LLM에 넣는 것은 권장되지 않는다.

Retrieved Chunks는 중복 제거, 관련도 정렬, 최신성 확인, Source Metadata 부여, Token Budget 조정을 거쳐야 한다.

기본 흐름은 다음과 같다.

```text
Retrieved Chunks
→ Remove Duplicates
→ Sort by Relevance / Priority
→ Resolve Conflicts
→ Trim to Token Budget
→ Add Source Metadata
→ Build Prompt Context
```

Context Assembly 품질이 낮으면 Retrieval이 성공해도 Generation 단계에서 잘못된 답변이 생성될 수 있다.

---

### [핵심]

- Context Assembly는 Retrieved Chunks를 Prompt Context로 구성하는 과정
- 검색 결과를 그대로 모두 넣지 않음
- 중복 Chunk 제거 필요
- 관련도와 문서 우선순위 기준으로 정렬
- Source / Section / Version Metadata 포함 권장
- Token Budget 안에서 핵심 문맥 유지
- 충돌 문서가 있으면 최신성 / 우선순위 기준 필요
- Context Assembly 실패는 Generation Failure로 이어질 수 있음

---

### [실무]

2026 실무 기준 RAG 시스템에서는 Context Assembly를 독립 단계로 다룬다.

개인 AI Agent 구조에서는 Context Assembly가 Agent 답변 품질을 크게 좌우한다.

예를 들어 Review Agent가 검증 작업을 수행할 때 다음 문서를 함께 검색할 수 있다.

- Master RAG Rules
- Domain Rules
- Part Document
- Checklist
- Troubleshooting
- Project Progress

이때 모든 문서를 그대로 넣으면 Context가 과도해지고 답변이 흔들릴 수 있다.

Context Assembly에서는 다음 기준을 적용한다.

- 현재 질문에 직접 답하는 Chunk 우선
- 현재 작업 요청의 출력 형식과 제약 조건 우선
- Master RAG Rules는 전체 문서 제작 규칙으로 우선
- Domain Rules는 도메인별 세부 기준으로 우선
- Project Progress는 진행 상태 판단에 사용
- 오래된 문서는 version / updatedAt 기준으로 후순위
- 중복 FAQ Chunk는 Deduplication
- Code Block은 필요한 부분만 포함
- Low Confidence 상황에서는 부족한 Context를 명시

---

### [FAQ]

Q. Context Assembly가 뭐야?

A.
검색된 Chunk를 정리해 LLM Prompt에 넣을 Context로 구성하는 과정이다.

Q. 검색된 Chunk를 전부 넣으면 안 돼?

A.
권장하지 않는다. 중복, 무관 정보, 충돌 문서가 답변 품질을 떨어뜨릴 수 있다.

Q. Context Assembly에서 가장 중요한 건 뭐야?

A.
관련 있는 Chunk만 남기고, 중복을 제거하며, Source와 Version을 유지하는 것이다.

Q. Context Assembly가 실패하면 어떻게 돼?

A.
검색은 성공했는데도 LLM이 잘못된 답변을 생성할 수 있다.

Q. Agent RAG에서 Context Assembly가 중요한 이유는 뭐야?

A.
Agent가 검색된 문서를 기준으로 판단하므로 Context 구성 품질이 작업 결과에 직접 영향을 주기 때문이다.

---

# 2. Retrieved Context

## 2.1 Retrieved Context Definition

### [개념]

Retrieved Context는 Retrieval 단계에서 검색되어 LLM Prompt에 포함되는 문서 Chunk다.

Retrieved Context는 RAG 답변의 근거다.

LLM은 Retrieved Context를 우선 사용해 답변해야 하며, Context에 없는 프로젝트 특화 사실을 임의로 생성하면 안 된다.

Retrieved Context에는 원문 Text뿐 아니라 Source Metadata도 함께 포함되는 것이 좋다.

---

### [핵심]

- Retrieved Context는 검색된 근거 Chunk
- RAG 답변의 핵심 근거
- Original Text와 Source Metadata 포함 권장
- Context에 없는 내용은 확정 답변 금지
- Context가 부족하면 Missing Information Rule 적용
- Context 품질은 Grounded Answer 품질에 영향
- 무관 Context는 Hallucination 위험 증가

---

### [실무]

Retrieved Context는 다음 구조로 관리하는 것이 좋다.

```text
[Source]
fileName: Vector_Database_RAG_Part05_Context_Assembly_Grounded_Generation.md
section: Grounded Generation
version: 2026-06

[Content]
Grounded Generation은 검색 문서를 근거로 답변하는 규칙이다.
문서에 없는 내용은 없다고 말해야 한다.
```

Agent가 Retrieved Context를 사용할 때 확인해야 할 항목은 다음과 같다.

- 이 Context가 질문에 직접 관련 있는가
- Source가 명확한가
- Version이 최신인가
- Domain이 Agent 역할과 맞는가
- 문서 간 충돌이 없는가
- 답변에 필요한 조건이 누락되지 않았는가

---

### [FAQ]

Q. Retrieved Context가 뭐야?

A.
Retrieval 단계에서 검색되어 LLM Prompt에 포함되는 문서 Chunk다.

Q. Retrieved Context에는 무엇이 들어가야 해?

A.
원문 Text, Source File, Section, Chunk ID, Version 같은 Metadata가 함께 들어가는 것이 좋다.

Q. Retrieved Context가 부족하면 어떻게 해?

A.
문서 근거가 부족하다고 말하고 필요한 정보를 명확히 표시해야 한다.

Q. 무관한 Context가 들어가면 어떻게 돼?

A.
LLM이 잘못된 근거를 사용해 부정확한 답변을 생성할 수 있다.

Q. Retrieved Context는 답변에 반드시 반영해야 해?

A.
RAG 답변에서는 Retrieved Context를 우선 근거로 사용해야 한다.

---

# 3. Context Ordering

## 3.1 Context Order Rule

### [개념]

Context Ordering은 여러 Retrieved Chunks를 어떤 순서로 LLM Prompt에 배치할지 결정하는 규칙이다.

LLM은 Prompt 앞쪽이나 명확히 구조화된 Context를 더 잘 사용할 수 있다.

따라서 가장 관련도가 높고, 최신이며, 규칙 우선순위가 높은 Chunk를 먼저 배치하는 것이 좋다.

Context Order가 잘못되면 오래된 문서나 낮은 우선순위 문서가 답변에 더 강하게 반영될 수 있다.

---

### [핵심]

- Context Ordering은 Prompt 내 Chunk 배치 순서 결정
- 관련도 높은 Chunk 우선
- 최신 문서 우선
- 현재 작업 요청의 출력 형식 우선
- Master Rules / Domain Rules 우선순위 고려
- 사용자 질문에 직접 답하는 Chunk 우선
- 보조 설명 Chunk는 후순위
- 충돌 가능 문서는 Conflict Handling 필요

---

### [실무]

개인 AI RAG 문서의 Context Ordering 기준은 다음과 같다.

| 우선순위 | Context 유형             | 사용 기준                                          |
| -------: | ------------------------ | -------------------------------------------------- |
|        1 | Current Task Constraints | 현재 작업의 출력 형식, 금지 규칙, 사용자 지정 조건 |
|        2 | User Task Direct Chunk   | 질문에 직접 답하는 Chunk                           |
|        3 | Master RAG Rules         | 전체 문서 제작 공통 규칙                           |
|        4 | Domain Rules             | 도메인별 세부 규칙                                 |
|        5 | Project Progress         | 현재 진행 상태 판단                                |
|        6 | Part Document            | 세부 개념과 실무 기준                              |
|        7 | Checklist                | 검수 기준                                          |
|        8 | Troubleshooting          | 오류 원인 분석                                     |
|        9 | FAQ / Retrieval Queries  | Query Matching 보조                                |

Context Order 예시는 다음과 같다.

```text
1. Current Task Output Format
2. Direct Answer Chunk
3. Master Rule Chunk
4. Domain Rule Chunk
5. Project Progress Chunk
6. Checklist Chunk
7. Troubleshooting Chunk
```

규칙 문서와 본문 문서가 충돌하면 규칙 문서의 우선순위를 먼저 확인한다.

현재 작업 요청이 Master Rules 또는 Domain Rules와 충돌하지 않는다면 현재 작업 요청의 출력 형식과 세부 제약을 우선 반영한다.

---

### [FAQ]

Q. Context Ordering이 뭐야?

A.
여러 Retrieved Chunks를 LLM Prompt에 어떤 순서로 배치할지 결정하는 규칙이다.

Q. Context 순서가 답변에 영향을 줘?

A.
영향을 줄 수 있다. 중요한 Context가 뒤에 있거나 묻히면 답변에 덜 반영될 수 있다.

Q. 어떤 Context를 먼저 배치해야 해?

A.
현재 작업 제약, 질문에 직접 답하는 최신 Chunk, 우선순위 높은 규칙 Chunk를 먼저 배치한다.

Q. Master Rules와 Domain Rules가 있으면 어느 쪽이 먼저야?

A.
기본 우선순위는 Master Rules → Domain Rules → Part Rules 순서다.

Q. FAQ Chunk는 어디에 배치해?

A.
직접 답변 근거라면 포함하고, 단순 보조 매칭용이면 후순위로 둔다.

---

# 4. Source Metadata in Context

## 4.1 Source Reference

### [개념]

Source Metadata는 Retrieved Context의 출처를 표시하는 정보다.

RAG 답변은 검색 문서를 근거로 하므로, 어떤 문서의 어떤 섹션을 사용했는지 추적 가능해야 한다.

Source Metadata는 Citation, Review Validation, Version Control, Conflict Handling에 사용된다.

Source Metadata가 없으면 답변 근거를 검증하기 어렵다.

---

### [핵심]

- Source Metadata는 Context 출처 정보
- Source File 표시 필요
- Section 표시 필요
- Chunk ID 표시 권장
- Document Title 표시 권장
- Version / updatedAt 표시 권장
- Citation과 Review Validation에 필요
- Source 없는 Context는 신뢰도 낮음

---

### [실무]

Context에 포함할 Source Metadata 예시는 다음과 같다.

```text
[source]
fileName: Vector_Database_RAG_Part05_Context_Assembly_Grounded_Generation.md
documentId: vector-database-rag-part05
chunkId: vector-database-rag-part05-004
section: Source Metadata in Context
title: Source Reference
version: 2026-06
updatedAt: 2026-06-30
```

Agent 답변에서 Source Metadata는 다음 용도로 사용된다.

- 답변 근거 추적
- 문서 버전 확인
- 오래된 문서 제외
- 충돌 문서 비교
- Review Agent 검증
- RAG Evaluation 기록

내부 RAG에서는 외부 논문식 Citation보다 파일명, 섹션, Chunk ID 기준 Citation이 실용적이다.

---

### [FAQ]

Q. Source Metadata가 뭐야?

A.
Retrieved Context가 어떤 문서와 섹션에서 왔는지 표시하는 출처 정보다.

Q. Source Metadata는 왜 필요해?

A.
답변 근거 추적, 검증, 최신성 확인, 충돌 처리에 필요하다.

Q. Source 없이 Context만 있으면 안 돼?

A.
권장하지 않는다. 답변 근거를 검증하기 어렵다.

Q. 내부 RAG Citation은 어떻게 해?

A.
파일명, Section, Chunk ID, Version 기준으로 표시하면 충분하다.

Q. Source Metadata는 Review Agent에도 필요해?

A.
필요하다. Review Agent가 답변 근거와 문서 일치 여부를 검증해야 하기 때문이다.

---

# 5. Context Deduplication

## 5.1 Deduplication Rule

### [개념]

Context Deduplication은 Retrieved Chunks 중 중복되거나 거의 동일한 내용을 제거하는 과정이다.

Chunk Overlap, 중복 문서 적재, FAQ 반복, Retrieval Queries 반복 때문에 유사한 Context가 여러 개 검색될 수 있다.

중복 Context가 많으면 Token Budget을 낭비하고, LLM이 같은 근거를 과도하게 중요하게 판단할 수 있다.

Context Deduplication은 Prompt Assembly 이전에 수행하는 것이 좋다.

---

### [핵심]

- Deduplication은 중복 Context 제거 과정
- 같은 chunkId 중복 제거
- 유사 본문 중복 제거
- 오래된 version 제거
- 중복 FAQ 과다 포함 주의
- Context Budget 절약
- 답변 왜곡 방지
- Deduplication 후 핵심 근거 유지 필요

---

### [실무]

Context Deduplication 기준은 다음과 같다.

| 기준                      | 처리                             |
| ------------------------- | -------------------------------- |
| 같은 chunkId              | 하나만 유지                      |
| 같은 documentId + section | 더 관련도 높은 Chunk 유지        |
| 거의 동일한 Text          | 하나만 유지                      |
| 같은 내용의 다른 version  | 최신 version 유지                |
| FAQ 반복                  | 질문과 직접 관련 있는 FAQ만 유지 |
| Retrieval Queries 반복    | 직접 근거가 아니면 후순위        |

Deduplication 흐름은 다음과 같다.

```text
Retrieved Chunks
→ Remove Same chunkId
→ Remove Similar Text
→ Keep Latest Version
→ Keep Higher Priority Source
→ Final Context Candidates
```

중복 제거 과정에서 필요한 근거까지 삭제하지 않도록 주의해야 한다.

---

### [FAQ]

Q. Context Deduplication이 뭐야?

A.
검색된 Context 중 중복되거나 거의 동일한 내용을 제거하는 과정이다.

Q. 중복 Context가 왜 문제야?

A.
Token Budget을 낭비하고 LLM이 같은 근거를 과도하게 중요하게 볼 수 있기 때문이다.

Q. FAQ 중복도 제거해야 해?

A.
질문과 직접 관련 없는 반복 FAQ는 제거하거나 후순위로 두는 것이 좋다.

Q. 오래된 버전과 최신 버전이 같이 검색되면 어떻게 해?

A.
version 또는 updatedAt 기준으로 최신 문서를 우선 사용한다.

Q. Deduplication 중 필요한 근거를 삭제하면 어떻게 돼?

A.
답변에 필요한 문맥이 부족해질 수 있으므로 핵심 조건은 유지해야 한다.

---

# 6. Context Compression

## 6.1 Context Compression Definition

### [개념]

Context Compression은 Retrieved Context를 Token Budget 안에 들어가도록 압축하거나 요약하는 과정이다.

Context Compression은 무작정 짧게 줄이는 것이 아니다.

답변에 필요한 핵심 조건, Source, 제약, 예외, Code Block 의미를 유지하면서 불필요한 부분을 줄이는 과정이다.

Compression 과정에서 핵심 정보가 삭제되면 Grounded Answer 품질이 낮아질 수 있다.

---

### [핵심]

- Context Compression은 Prompt Context 압축 과정
- Token Budget 관리 목적
- 핵심 조건 유지 필요
- Source Metadata 유지 필요
- Code Block 의미 훼손 금지
- 예외 조건 삭제 주의
- 과도한 압축은 답변 오류 유발
- Compression 후 Grounding 가능성 확인 필요

---

### [실무]

Context Compression 기준은 다음과 같다.

| Context 유형    | Compression 기준                  |
| --------------- | --------------------------------- |
| 개념 설명       | 정의와 핵심 조건 유지             |
| 실무 규칙       | 금지 / 권장 / 우선순위 유지       |
| Code Block      | 필요한 핵심 Snippet만 유지        |
| Checklist       | 관련 항목만 추출                  |
| Troubleshooting | 문제 / 원인 / 해결 구조 유지      |
| FAQ             | 질문과 직접 관련 있는 항목만 유지 |
| Metadata        | Source, Section, Version 유지     |

좋은 Compression 예시는 다음과 같다.

```text
원본:
RAG 답변은 검색 문서를 근거로 해야 하며, 문서에 없는 내용은 없다고 표현해야 한다.
일반 지식으로 보완할 경우 추정임을 표시하고, 답변에 사용한 근거 Chunk를 추적 가능해야 한다.

압축:
RAG 답변은 Retrieved Context를 근거로 해야 한다.
문서에 없는 내용은 확정하지 말고, 추정은 분리한다.
Source Chunk 추적이 가능해야 한다.
```

나쁜 Compression은 다음과 같다.

```text
RAG는 문서를 보고 답한다.
```

두 번째 예시는 Grounding Rule과 Missing Information Rule이 사라져 근거 제어가 약해진다.

---

### [FAQ]

Q. Context Compression이 뭐야?

A.
Retrieved Context를 Token Budget 안에 넣기 위해 핵심 정보를 유지하며 압축하는 과정이다.

Q. Context Compression은 그냥 요약이야?

A.
아니다. 답변에 필요한 조건, 제약, Source를 유지해야 한다.

Q. Compression에서 삭제하면 안 되는 건 뭐야?

A.
핵심 조건, 금지 규칙, 예외, Source Metadata, Code Block 의미는 삭제하면 안 된다.

Q. Compression을 많이 하면 좋은 거 아니야?

A.
아니다. 과도한 압축은 Grounded Answer 품질을 떨어뜨릴 수 있다.

Q. Code Block도 압축해도 돼?

A.
가능하지만 문법과 핵심 로직이 훼손되지 않아야 한다.

---

# 7. Conflict Handling

## 7.1 Conflicting Context

### [개념]

Conflict Handling은 Retrieved Context 간 내용이 서로 충돌할 때 어떤 문서를 우선할지 결정하는 과정이다.

RAG 시스템에서는 오래된 문서와 최신 문서, Master Rules와 Part 문서, Domain Rules와 일반 문서가 함께 검색될 수 있다.

충돌 Context를 그대로 넣으면 LLM이 혼합된 답변을 만들 수 있다.

따라서 충돌 기준을 명확히 정해야 한다.

---

### [핵심]

- Conflict Handling은 충돌 문서 처리 과정
- 현재 작업 출력 조건 확인
- 최신 version 우선
- Master Rules 우선
- Domain Rules 우선
- Project Progress 최신 상태 우선
- Source Metadata로 충돌 확인
- 충돌이 해결되지 않으면 불확실성 표시
- 충돌 Context를 그대로 섞지 않음

---

### [실무]

문서 우선순위 기준은 다음과 같다.

```text
1. System / Project Output Constraints
2. Current User Task Instruction
3. Master RAG Rules
4. Domain Rules
5. Project Progress
6. Part Document
7. FAQ / Retrieval Queries
8. General Knowledge
```

우선순위 해석 기준:

- System / Project Output Constraints는 대화 또는 프로젝트의 최상위 출력 형식과 금지 규칙이다.
- Current User Task Instruction은 현재 작업에서 사용자가 지정한 세부 요청이다.
- Current User Task Instruction은 Master RAG Rules와 Domain Rules를 깨뜨리는 방식으로 해석하지 않는다.
- Master RAG Rules는 전체 RAG 문서 제작 공통 기준이다.
- Domain Rules는 특정 기술 도메인 문서의 세부 기준이다.
- Project Progress는 현재 완료 / 예정 상태를 판단할 때 사용한다.
- Part Document는 세부 개념 설명과 실무 기준으로 사용한다.
- General Knowledge는 문서 근거가 부족할 때만 보조로 사용하고 추정으로 분리한다.

Conflict Handling 예시는 다음과 같다.

```text
문제:
Part 문서에는 오래된 파일명이 있고 Project Progress에는 최신 파일명이 있음.

처리:
Project Progress의 updatedAt 또는 최신 version을 우선 확인한다.
충돌이 해결되지 않으면 확정하지 않고 추가 확인 필요로 표시한다.
```

다른 예시는 다음과 같다.

```text
문제:
현재 작업 요청은 보고서 형식을 원하지 않지만, 이전 답변에는 보고서형 검수 결과가 생성됨.

처리:
현재 작업 요청의 출력 형식을 우선 적용한다.
최종 출력은 사용자가 요청한 파일명 목록 또는 재작업 문서 형식으로 제한한다.
```

충돌을 해결할 수 없는 경우 답변에 다음을 포함한다.

- 충돌하는 문서
- 충돌 내용
- 우선 적용한 기준
- 추가 확인이 필요한 정보

---

### [FAQ]

Q. Conflict Handling이 뭐야?

A.
검색된 Context끼리 내용이 충돌할 때 어떤 기준을 우선할지 결정하는 과정이다.

Q. 오래된 문서와 최신 문서가 충돌하면 어떻게 해?

A.
version 또는 updatedAt 기준으로 최신 문서를 우선한다.

Q. Master Rules와 Part 문서가 충돌하면 어떻게 해?

A.
Master Rules를 우선하고, 그다음 Domain Rules와 Part 문서를 적용한다.

Q. 현재 사용자 요청은 어디에 들어가?

A.
현재 작업의 구체적 출력 형식과 세부 조건으로 반영하되 Master Rules와 Domain Rules를 깨뜨리지 않는 범위에서 우선한다.

Q. 충돌을 해결할 수 없으면 어떻게 해?

A.
확정 답변을 피하고 충돌 내용과 추가 확인 필요 정보를 표시해야 한다.

---

# 8. Prompt Assembly

## 8.1 RAG Prompt Structure

### [개념]

Prompt Assembly는 System Instruction, Retrieved Context, User Question, Output Format, Grounding Rule을 하나의 LLM Prompt로 구성하는 과정이다.

RAG Prompt는 일반 Prompt와 다르다.

RAG Prompt는 LLM이 검색된 문서를 우선 사용하도록 명확히 지시해야 한다.

Context와 User Question은 분리되어야 하며, 문서에 없는 내용 처리 규칙이 포함되어야 한다.

---

### [핵심]

- Prompt Assembly는 최종 LLM Prompt 구성 과정
- System Instruction 포함
- Retrieved Context 포함
- User Question 포함
- Grounding Rule 포함
- Missing Information Rule 포함
- Output Format 포함
- Citation / Source Rule 포함 권장
- Context와 User Question 분리 필요

---

### [실무]

RAG Prompt 기본 구조는 다음과 같다.

```text
System:
You answer based on retrieved documents.
Use retrieved context first.
Do not invent project-specific facts.

Retrieved Context:
{retrieved_context}

User Question:
{question}

Rules:
- Use context first.
- If context is insufficient, say what is missing.
- Separate evidence from assumptions.
- Follow the requested output format.
- Include source references when available.

Output Format:
{output_format}
```

개인 AI Agent용 Prompt Assembly에서는 Agent 역할도 함께 포함할 수 있다.

```text
Agent Role:
Review Agent

Task:
Validate whether the generated RAG document follows Master Rules and Domain Rules.

Context:
{retrieved_context}

Validation Rules:
- Check required sections.
- Check FAQ quality.
- Check Retrieval Queries.
- Check code block id="" removal.
- Check terminology consistency.
```

---

### [FAQ]

Q. Prompt Assembly가 뭐야?

A.
System Instruction, Retrieved Context, User Question, Rules, Output Format을 하나의 Prompt로 구성하는 과정이다.

Q. RAG Prompt는 일반 Prompt와 뭐가 달라?

A.
RAG Prompt는 Retrieved Context를 우선 근거로 사용하도록 Grounding Rule을 포함한다.

Q. Context와 User Question은 분리해야 해?

A.
분리해야 한다. LLM이 문서 근거와 사용자 요청을 구분해야 하기 때문이다.

Q. RAG Prompt에 꼭 들어가야 하는 규칙은 뭐야?

A.
Grounding Rule, Missing Information Rule, Output Format, Citation Rule이 필요하다.

Q. Agent Prompt에도 Context Assembly가 필요해?

A.
필요하다. Agent 역할에 맞는 Context와 검증 규칙을 명확히 넣어야 한다.

---

# 9. Grounded Generation

## 9.1 Grounded Answer

### [개념]

Grounded Generation은 검색된 문서를 근거로 답변을 생성하는 규칙이다.

Grounded Answer는 Retrieved Context와 일치해야 한다.

문서에 없는 프로젝트 특화 사실은 확정적으로 생성하지 않는다.

일반 지식으로 보완할 경우에는 근거 기반 답변과 추정을 분리해야 한다.

기본 규칙은 다음과 같다.

```text
Use retrieved context first.
If the context does not contain enough information, say what is missing.
Do not invent project-specific facts.
Separate evidence-based answer from assumptions.
```

---

### [핵심]

- Grounded Generation은 문서 근거 기반 답변 생성
- Retrieved Context 우선 사용
- 문서에 없는 내용 확정 금지
- 일반 지식 보완 시 추정 표시
- Evidence와 Assumption 분리
- Source Reference 유지
- Grounding Check 필요
- Hallucination을 줄이지만 완전히 제거하지는 못함

---

### [실무]

Agent 답변은 다음 기준을 따라야 한다.

- 문서에 있는 내용: 근거 기반으로 답변
- 문서에 없는 내용: 없다고 표시
- 문서가 부족한 내용: 필요한 문서 또는 정보 명시
- 충돌하는 내용: 우선순위 기준과 불확실성 표시
- 일반 지식 보완: 추정 또는 일반 원칙으로 분리
- 코드 생성: 프로젝트 문서 근거와 일반 코드 패턴 구분

Grounded Answer 예시는 다음과 같다.

```text
문서 근거 기준으로는 Vector Database & RAG 문서에는 Chunking, Metadata, Retrieval, Context Assembly 기준이 포함되어야 한다.

문서에서 확인되지 않은 부분:
- 실제 Vector DB 제품 선택
- 운영 서버 Collection 이름
- 현재 AnythingLLM 내부 설정값

따라서 제품 선택은 별도 운영 문서 확인이 필요하다.
```

---

### [FAQ]

Q. Grounded Generation이 뭐야?

A.
검색된 문서를 근거로 답변을 생성하는 규칙이다.

Q. Grounded Answer가 뭐야?

A.
Retrieved Context와 일치하고 문서 근거를 기반으로 한 답변이다.

Q. 문서에 없는 내용은 어떻게 답해야 해?

A.
문서에 없다고 말하고 필요한 정보가 무엇인지 표시해야 한다.

Q. 일반 지식으로 보완해도 돼?

A.
가능하지만 근거 기반 답변과 추정을 분리해야 한다.

Q. Grounded Generation이 Hallucination을 완전히 막아?

A.
완전히 막지는 못하지만 문서 근거 우선 규칙으로 줄일 수 있다.

---

# 10. Missing Information Rule

## 10.1 Missing Context

### [개념]

Missing Information Rule은 Retrieved Context에 답변에 필요한 정보가 없거나 부족할 때 적용하는 규칙이다.

RAG 시스템은 문서에 없는 내용을 임의로 채워 넣지 않아야 한다.

문서 근거가 부족하면 무엇이 부족한지, 어떤 문서가 필요한지, 어떤 확인이 필요한지를 명확히 표시해야 한다.

Missing Information Rule은 Hallucination을 줄이는 핵심 규칙이다.

---

### [핵심]

- 문서에 없는 내용은 없다고 말함
- Context 부족 시 확정 답변 금지
- 부족한 정보 목록 표시
- 필요한 문서 또는 Source 제시
- 추정과 근거 분리
- 프로젝트 특화 사실 임의 생성 금지
- Low Confidence 상황과 연결
- Review Agent 검증 대상

---

### [실무]

Missing Information Rule 출력 예시는 다음과 같다.

```text
검색된 문서만으로는 확정할 수 없음.

부족한 정보:
- 실제 운영 Vector Database 종류
- Collection 이름
- Embedding Model 버전
- Top-K 설정값
- Threshold 설정값

필요한 확인:
- 운영 설정 문서
- AnythingLLM Workspace 설정
- Embedding Model Registry
```

개인 AI 개발팀에서는 Missing Information Rule이 특히 중요하다.

Agent가 프로젝트에 존재하지 않는 코드, 설정, 배포 환경을 임의로 만들면 실제 작업 오류로 이어질 수 있기 때문이다.

---

### [FAQ]

Q. Missing Information Rule이 뭐야?

A.
문서에 답변에 필요한 정보가 없을 때 없다고 말하고 부족한 정보를 표시하는 규칙이다.

Q. 문서에 없는 내용을 추정해서 답해도 돼?

A.
프로젝트 특화 사실은 확정적으로 추정하면 안 된다. 추정은 분리해서 표시해야 한다.

Q. Missing Information Rule은 왜 필요해?

A.
문서에 없는 내용을 LLM이 임의로 생성하는 Hallucination을 줄이기 위해 필요하다.

Q. 부족한 정보는 어떻게 표시해?

A.
부족한 정보, 필요한 문서, 추가 확인 항목으로 나눠 표시한다.

Q. Review Agent도 Missing Information Rule을 확인해야 해?

A.
해야 한다. 답변이 문서 근거를 벗어났는지 검증해야 한다.

---

# 11. Citation and Source Rule

## 11.1 Citation Rule

### [개념]

Citation and Source Rule은 RAG 답변이 어떤 문서를 근거로 생성되었는지 표시하는 규칙이다.

Citation은 외부 논문이나 웹 문서 인용만 의미하지 않는다.

내부 RAG 시스템에서는 파일명, 섹션, Chunk ID, Version을 표시하는 것도 Citation이다.

Citation은 답변 검증, 문서 업데이트, 오류 추적에 필요하다.

---

### [핵심]

- Citation은 답변 근거 표시
- Source File 표시 권장
- Section 표시 권장
- Chunk ID 표시 권장
- Version / updatedAt 표시 권장
- 내부 RAG에서는 파일명 기반 Citation 가능
- Source 없는 답변과 RAG 근거 답변 구분
- 잘못된 Citation은 신뢰도 하락

---

### [실무]

내부 RAG Citation 예시는 다음과 같다.

```text
근거:
- Vector_Database_RAG_Part05_Context_Assembly_Grounded_Generation.md
  - section: Grounded Generation
  - chunkId: vector-database-rag-part05-009
  - version: 2026-06
```

Agent Review에서는 다음을 확인한다.

- Citation이 실제 답변 내용과 일치하는가
- Source가 최신 문서인가
- Section이 답변 근거로 적절한가
- Chunk ID가 추적 가능한가
- Citation 없는 확정 답변이 없는가

RAG 문서 제작 결과물 자체에서는 Citation보다 Retrieval Queries와 Metadata 설계가 더 중요할 수 있다.

하지만 Agent 답변에서는 Source Reference를 유지해야 한다.

---

### [FAQ]

Q. Citation Rule이 뭐야?

A.
RAG 답변이 어떤 문서를 근거로 생성되었는지 표시하는 규칙이다.

Q. 내부 RAG에서도 Citation이 필요해?

A.
필요하다. 파일명, 섹션, Chunk ID, Version 기준으로 표시할 수 있다.

Q. Citation은 왜 중요해?

A.
답변 검증, 오류 추적, 문서 업데이트 판단에 필요하기 때문이다.

Q. Source 없는 답변은 문제가 돼?

A.
RAG 근거 답변이라면 Source가 없을 때 검증이 어렵다.

Q. 잘못된 Citation은 어떻게 돼?

A.
답변 신뢰도가 떨어지고 Review Validation이 실패할 수 있다.

---

# 12. Grounding Check

## 12.1 Answer Validation

### [개념]

Grounding Check는 생성된 답변이 Retrieved Context와 일치하는지 검증하는 과정이다.

RAG 답변은 검색된 문서를 근거로 해야 하므로, 답변 생성 후에도 문서와의 일치 여부를 확인해야 한다.

Grounding Check는 Generation Failure를 줄이기 위한 Review 단계다.

Review Agent가 수행하기 적합하다.

---

### [핵심]

- Grounding Check는 답변과 Context 일치 검증
- 문서에 없는 내용 생성 여부 확인
- Source와 답변 내용 일치 확인
- 충돌 문서 반영 여부 확인
- 추정과 근거 분리 여부 확인
- Missing Information Rule 적용 여부 확인
- Code Generation 결과 검증에 중요
- Review Agent 역할과 연결

---

### [실무]

Grounding Check 기준은 다음과 같다.

```text
### [Checklist]

- [ ] 답변이 Retrieved Context와 일치하는가?
- [ ] 문서에 없는 프로젝트 특화 사실을 만들지 않았는가?
- [ ] Source Metadata가 유지되었는가?
- [ ] 충돌 Context를 우선순위 기준으로 처리했는가?
- [ ] 부족한 정보가 명확히 표시되었는가?
- [ ] 추정과 근거 기반 답변을 분리했는가?
- [ ] 코드 생성 결과가 검색된 규칙과 일치하는가?
- [ ] Output Format을 지켰는가?
```

코드 생성 RAG에서는 다음 항목도 확인한다.

- 사용한 클래스명과 메서드명이 문서에 있는가
- DTO / Entity / Repository 구조가 문서와 맞는가
- API Endpoint가 실제 문서와 맞는가
- 보안 규칙이 Domain Rules와 충돌하지 않는가

---

### [FAQ]

Q. Grounding Check가 뭐야?

A.
생성된 답변이 Retrieved Context와 일치하는지 검증하는 과정이다.

Q. Grounding Check는 왜 필요해?

A.
검색 문서와 다른 답변을 생성하는 Generation Failure를 줄이기 위해 필요하다.

Q. Grounding Check는 누가 수행해?

A.
Review Agent가 수행하기 적합하다.

Q. Grounding Check에서 가장 중요한 건 뭐야?

A.
문서에 없는 내용을 확정적으로 생성하지 않았는지 확인하는 것이다.

Q. 코드 생성에도 Grounding Check가 필요해?

A.
필요하다. 생성된 코드가 프로젝트 문서와 규칙에 맞는지 확인해야 한다.

---

# 13. Generation Failure

## 13.1 Ungrounded Answer

### [개념]

Ungrounded Answer는 Retrieved Context와 일치하지 않거나 문서에 없는 내용을 근거 없이 생성한 답변이다.

Retrieval이 성공했더라도 Prompt가 약하거나 Context가 과도하거나 Grounding Rule이 없으면 Ungrounded Answer가 발생할 수 있다.

Ungrounded Answer는 RAG 신뢰도를 크게 낮춘다.

---

### [핵심]

- Ungrounded Answer는 문서 근거 없는 답변
- Retrieved Context와 다른 내용 생성
- 문서에 없는 프로젝트 사실 생성
- 일반 지식을 근거처럼 사용
- Prompt Grounding Rule 부족 가능
- Context 과다 또는 충돌 가능
- Missing Information Rule 부재 가능
- Review Agent 검증 필요

---

### [실무]

문제 해결 형식은 다음과 같다.

```text
문제:
검색된 문서와 다른 답변을 생성함

원인:
Grounding Rule 부족
Missing Information Rule 없음
Context 과다
충돌 문서 포함
Source Metadata 없음
Prompt Output Format 불명확
LLM이 일반 지식으로 보완

해결:
Grounding Rule 강화
문서에 없는 내용 금지 규칙 추가
Context Deduplication
Conflict Handling 적용
Source Metadata 포함
Output Format 명확화
Grounding Check 수행
```

Ungrounded Answer는 RAG 시스템에서 가장 경계해야 할 Generation Failure다.

특히 Agent가 코드, 설정, 배포 절차를 임의로 생성하면 실제 프로젝트 오류로 이어질 수 있다.

---

### [FAQ]

Q. Ungrounded Answer가 뭐야?

A.
Retrieved Context와 일치하지 않거나 문서에 없는 내용을 근거 없이 생성한 답변이다.

Q. 검색은 됐는데 답변이 틀리는 이유는 뭐야?

A.
Grounding Rule 부족, Context Assembly 문제, 충돌 문서, Missing Information Rule 부재 때문일 수 있다.

Q. 일반 지식으로 답하면 안 돼?

A.
일반 지식은 보조로 사용할 수 있지만 프로젝트 특화 사실처럼 확정하면 안 된다.

Q. Ungrounded Answer는 어떻게 줄여?

A.
Grounding Rule 강화, Source 유지, Context 정리, Grounding Check를 적용한다.

Q. Agent가 임의로 코드를 만들면 왜 위험해?

A.
프로젝트 구조와 맞지 않는 코드가 생성되어 실제 구현 오류를 만들 수 있기 때문이다.

---

## 13.2 Context Overload

### [개념]

Context Overload는 LLM Prompt에 너무 많은 Retrieved Context가 포함되어 답변 품질이 떨어지는 문제다.

관련 없는 Chunk, 중복 Chunk, 오래된 문서, 충돌 문서가 너무 많이 포함되면 LLM이 핵심 근거를 놓칠 수 있다.

Context Window가 크더라도 무조건 많은 Context를 넣는 것은 좋은 RAG 설계가 아니다.

---

### [핵심]

- Context Overload는 Context 과다 문제
- 무관 Chunk 포함 시 답변 품질 저하
- 중복 Chunk 포함 시 Token Budget 낭비
- 충돌 문서 포함 시 답변 혼선
- 오래된 문서 포함 시 잘못된 기준 반영
- Context Compression 필요
- Deduplication 필요
- Top-K / Threshold 조정 필요

---

### [실무]

Context Overload 해결 형식은 다음과 같다.

```text
문제:
Prompt Context가 너무 길고 답변이 흔들림

원인:
Top-K 과다
Threshold 낮음
중복 Chunk 많음
무관 Context 포함
충돌 문서 포함
오래된 문서 포함
Context Compression 없음

해결:
Top-K 조정
Threshold 조정
Deduplication 수행
Metadata Filter 적용
최신 Version 우선
Conflict Handling 적용
Context Compression 적용
Grounding Check 수행
```

Context Overload는 단순히 LLM Context Window를 늘린다고 해결되지 않는다.

검색 품질과 Context Assembly 품질을 함께 개선해야 한다.

---

### [FAQ]

Q. Context Overload가 뭐야?

A.
LLM Prompt에 너무 많은 Context가 들어가 답변 품질이 떨어지는 문제다.

Q. Context Window가 크면 많이 넣어도 돼?

A.
항상 그렇지 않다. 무관하거나 중복된 Context는 답변 품질을 떨어뜨린다.

Q. Context Overload는 어떻게 줄여?

A.
Top-K 조정, Deduplication, Metadata Filter, Context Compression을 적용한다.

Q. 중복 Context도 문제야?

A.
그렇다. Token Budget을 낭비하고 특정 근거가 과도하게 강조될 수 있다.

Q. 오래된 문서가 Context에 들어가면 어떻게 돼?

A.
Agent가 이전 기준으로 답변할 수 있다.

---

# 14. RAG Prompt Rules

## 14.1 Grounding Prompt Rule

### [개념]

Grounding Prompt Rule은 LLM이 Retrieved Context를 우선 근거로 사용하도록 지시하는 Prompt 규칙이다.

RAG Prompt에 Grounding Rule이 없으면 LLM은 검색 문서보다 일반 지식이나 추론을 우선할 수 있다.

Grounding Prompt Rule은 Missing Information Rule, Citation Rule, Output Format Rule과 함께 사용해야 한다.

---

### [핵심]

- Retrieved Context 우선 사용 지시
- 문서에 없는 내용 생성 금지
- 부족한 정보 표시 지시
- 추정과 근거 분리 지시
- Source Reference 유지 지시
- Output Format 준수 지시
- 사용자 요청이 Context 무시를 요구해도 Grounding 유지
- Agent 역할별 Prompt에 포함 필요

---

### [실무]

권장 Grounding Prompt는 다음과 같다.

```text
Rules:
- Use the retrieved context first.
- Do not invent project-specific facts.
- If the context is insufficient, say what is missing.
- Separate evidence-based answers from assumptions.
- Keep source references when available.
- Follow the required output format.
- If retrieved documents conflict, apply document priority rules.
```

Agent별로 다음 규칙을 추가할 수 있다.

| Agent          | 추가 Grounding Rule                     |
| -------------- | --------------------------------------- |
| PM Agent       | Project Progress와 Domain Rules 우선    |
| Backend Agent  | 코드 생성 시 Backend 문서 근거 우선     |
| Frontend Agent | API 연동 문서와 UI 규칙 우선            |
| Review Agent   | Checklist와 Rules 기준 검증             |
| DevOps Agent   | 운영 문서와 배포 규칙 우선              |
| AI Agent       | RAG / Agent 문서와 Evaluation 기준 우선 |

---

### [FAQ]

Q. Grounding Prompt Rule이 뭐야?

A.
LLM이 Retrieved Context를 우선 근거로 사용하도록 지시하는 Prompt 규칙이다.

Q. Grounding Rule이 없으면 어떻게 돼?

A.
LLM이 일반 지식으로 문서에 없는 내용을 생성할 수 있다.

Q. Grounding Prompt에 꼭 들어가야 하는 내용은 뭐야?

A.
Context 우선, 문서에 없는 내용 금지, 부족 정보 표시, Source 유지, Output Format 준수다.

Q. 사용자 요청이 Context를 무시하라고 하면 어떻게 해?

A.
RAG 답변에서는 Grounding Rule을 유지해야 한다.

Q. Agent별 Grounding Rule도 필요해?

A.
필요하다. Agent 역할에 따라 우선 참조할 문서와 검증 기준이 다르기 때문이다.

---

# 15. Context Assembly and Generation Checklist

## 15.1 Final Checklist

### [개념]

Context Assembly and Grounded Generation Checklist는 검색된 Chunk를 답변 근거로 안전하게 사용하는지 검수하는 기준이다.

이 Checklist는 Retrieval 성공 이후 Generation 단계의 오류를 줄이기 위해 사용한다.

Review Agent는 이 Checklist를 사용해 답변이 문서 근거와 일치하는지 검증할 수 있다.

---

### [핵심]

- Retrieved Context 관련성 확인
- Source Metadata 유지 확인
- Deduplication 수행 확인
- Context Ordering 확인
- Conflict Handling 확인
- Token Budget 확인
- Grounding Rule 적용 확인
- Missing Information Rule 적용 확인
- Citation Rule 적용 확인
- Grounding Check 수행 확인

---

### [실무]

최종 Checklist는 다음과 같다.

```text
### [Checklist]

- [ ] Retrieved Context가 사용자 질문에 직접 관련 있는가?
- [ ] Source File이 표시되어 있는가?
- [ ] Section 정보가 유지되어 있는가?
- [ ] Chunk ID가 추적 가능한가?
- [ ] Version / updatedAt 정보가 있는가?
- [ ] 중복 Chunk를 제거했는가?
- [ ] 오래된 문서를 제거하거나 후순위로 두었는가?
- [ ] Context를 관련도와 우선순위 기준으로 정렬했는가?
- [ ] 현재 작업 요청의 출력 형식과 제약을 반영했는가?
- [ ] Master Rules / Domain Rules / Project Progress 우선순위를 고려했는가?
- [ ] 충돌 Context를 처리했는가?
- [ ] Token Budget 안에서 핵심 문맥을 유지했는가?
- [ ] Context Compression 중 핵심 조건을 삭제하지 않았는가?
- [ ] Prompt에 Grounding Rule이 포함되어 있는가?
- [ ] Prompt에 Missing Information Rule이 포함되어 있는가?
- [ ] Prompt에 Output Format이 포함되어 있는가?
- [ ] Prompt에 Citation / Source Rule이 포함되어 있는가?
- [ ] 답변이 Retrieved Context와 일치하는가?
- [ ] 문서에 없는 프로젝트 특화 사실을 생성하지 않았는가?
- [ ] 추정과 근거 기반 답변을 분리했는가?
- [ ] Low Confidence 상황에서 확정 답변을 피했는가?
- [ ] Review Agent가 Grounding Check를 수행했는가?
```

이 Checklist는 RAG 문서 답변, 코드 생성, 설계 제안, Review Agent 검증에 공통 적용할 수 있다.

---

### [FAQ]

Q. Context Assembly and Grounded Generation Checklist는 왜 필요해?

A.
Retrieval 성공 이후 Generation 단계에서 문서와 다른 답변이 생성되는 문제를 줄이기 위해 필요하다.

Q. 이 Checklist는 언제 사용해?

A.
Context Assembly 후, Prompt Assembly 후, 답변 생성 후 검증 단계에서 사용한다.

Q. 가장 중요한 검수 항목은 뭐야?

A.
답변이 Retrieved Context와 일치하는지, 문서에 없는 내용을 생성하지 않았는지 확인하는 것이다.

Q. Review Agent가 이 Checklist를 써도 돼?

A.
적합하다. Review Agent는 Grounding Check와 Output Format 검증에 사용할 수 있다.

Q. Context Assembly가 좋아도 답변이 틀릴 수 있어?

A.
가능하다. Prompt Grounding Rule과 Grounding Check가 함께 필요하다.

---

# Retrieval Queries

### [FAQ]

Q. Context Assembly가 뭐야?
A. 검색된 Chunk를 정리해 LLM Prompt에 넣을 Context로 구성하는 과정이다.

Q. Retrieved Context가 뭐야?
A. Retrieval 단계에서 검색되어 LLM Prompt에 포함되는 문서 Chunk다.

Q. 검색된 Chunk를 전부 Prompt에 넣어도 돼?
A. 권장하지 않는다. 중복, 무관 정보, 충돌 문서가 답변 품질을 떨어뜨릴 수 있다.

Q. Context Assembly가 중요한 이유는 뭐야?
A. 검색 결과를 어떻게 조립하느냐에 따라 Grounded Answer 품질이 달라지기 때문이다.

Q. Context Ordering이 뭐야?
A. 여러 Retrieved Chunks를 LLM Prompt에 어떤 순서로 배치할지 결정하는 규칙이다.

Q. Context 순서는 답변에 영향을 줘?
A. 영향을 줄 수 있다. 중요한 Context가 뒤에 있거나 묻히면 답변에 덜 반영될 수 있다.

Q. 어떤 Context를 먼저 배치해야 해?
A. 현재 작업 제약, 질문에 직접 답하는 최신 Chunk, 우선순위 높은 규칙 Chunk를 먼저 배치한다.

Q. Master Rules와 Domain Rules가 충돌하면 어떻게 해?
A. Master Rules를 우선하고, 그다음 Domain Rules와 Part 문서를 적용한다.

Q. 현재 사용자 요청과 문서 규칙이 충돌하면 어떻게 해?
A. 현재 사용자 요청은 출력 형식과 세부 작업 조건으로 반영하되 Master Rules와 Domain Rules를 깨뜨리지 않는 범위에서 적용한다.

Q. Source Metadata가 뭐야?
A. Retrieved Context가 어떤 문서와 섹션에서 왔는지 표시하는 출처 정보다.

Q. Source Metadata는 왜 필요해?
A. 답변 근거 추적, 검증, 최신성 확인, 충돌 처리에 필요하다.

Q. 내부 RAG Citation은 어떻게 해?
A. 파일명, Section, Chunk ID, Version 기준으로 표시하면 충분하다.

Q. Context Deduplication이 뭐야?
A. 검색된 Context 중 중복되거나 거의 동일한 내용을 제거하는 과정이다.

Q. 중복 Context가 왜 문제야?
A. Token Budget을 낭비하고 LLM이 같은 근거를 과도하게 중요하게 볼 수 있기 때문이다.

Q. 오래된 문서와 최신 문서가 같이 검색되면 어떻게 해?
A. version 또는 updatedAt 기준으로 최신 문서를 우선 사용한다.

Q. Context Compression이 뭐야?
A. Retrieved Context를 Token Budget 안에 넣기 위해 핵심 정보를 유지하며 압축하는 과정이다.

Q. Context Compression에서 삭제하면 안 되는 것은 뭐야?
A. 핵심 조건, 금지 규칙, 예외, Source Metadata, Code Block 의미는 삭제하면 안 된다.

Q. Conflict Handling이 뭐야?
A. 검색된 Context끼리 내용이 충돌할 때 어떤 기준을 우선할지 결정하는 과정이다.

Q. 충돌 Context를 그대로 넣으면 안 돼?
A. 그대로 넣으면 LLM이 서로 다른 기준을 섞어 잘못된 답변을 만들 수 있다.

Q. Prompt Assembly가 뭐야?
A. System Instruction, Retrieved Context, User Question, Rules, Output Format을 하나의 Prompt로 구성하는 과정이다.

Q. RAG Prompt는 일반 Prompt와 뭐가 달라?
A. RAG Prompt는 Retrieved Context를 우선 근거로 사용하도록 Grounding Rule을 포함한다.

Q. RAG Prompt에 꼭 들어가야 하는 규칙은 뭐야?
A. Grounding Rule, Missing Information Rule, Output Format, Citation Rule이 필요하다.

Q. Grounded Generation이 뭐야?
A. 검색된 문서를 근거로 답변을 생성하는 규칙이다.

Q. Grounded Answer가 뭐야?
A. Retrieved Context와 일치하고 문서 근거를 기반으로 한 답변이다.

Q. 문서에 없는 내용은 어떻게 답해야 해?
A. 문서에 없다고 말하고 필요한 정보가 무엇인지 표시해야 한다.

Q. 일반 지식으로 보완해도 돼?
A. 가능하지만 근거 기반 답변과 추정을 분리해야 한다.

Q. Missing Information Rule이 뭐야?
A. 문서에 답변에 필요한 정보가 없을 때 없다고 말하고 부족한 정보를 표시하는 규칙이다.

Q. Missing Information Rule은 왜 필요해?
A. 문서에 없는 내용을 LLM이 임의로 생성하는 Hallucination을 줄이기 위해 필요하다.

Q. Citation Rule이 뭐야?
A. RAG 답변이 어떤 문서를 근거로 생성되었는지 표시하는 규칙이다.

Q. Source 없는 답변은 문제가 돼?
A. RAG 근거 답변이라면 Source가 없을 때 검증이 어렵다.

Q. Grounding Check가 뭐야?
A. 생성된 답변이 Retrieved Context와 일치하는지 검증하는 과정이다.

Q. Grounding Check는 누가 수행해?
A. Review Agent가 수행하기 적합하다.

Q. Grounding Check에서 가장 중요한 것은 뭐야?
A. 문서에 없는 내용을 확정적으로 생성하지 않았는지 확인하는 것이다.

Q. Ungrounded Answer가 뭐야?
A. Retrieved Context와 일치하지 않거나 문서에 없는 내용을 근거 없이 생성한 답변이다.

Q. 검색은 됐는데 답변이 틀리는 이유는 뭐야?
A. Grounding Rule 부족, Context Assembly 문제, 충돌 문서, Missing Information Rule 부재 때문일 수 있다.

Q. Context Overload가 뭐야?
A. LLM Prompt에 너무 많은 Context가 들어가 답변 품질이 떨어지는 문제다.

Q. Context Overload는 어떻게 줄여?
A. Top-K 조정, Deduplication, Metadata Filter, Context Compression을 적용한다.

Q. Grounding Prompt Rule이 뭐야?
A. LLM이 Retrieved Context를 우선 근거로 사용하도록 지시하는 Prompt 규칙이다.

Q. Grounding Rule이 없으면 어떻게 돼?
A. LLM이 일반 지식으로 문서에 없는 내용을 생성할 수 있다.

Q. 사용자 요청이 Context를 무시하라고 하면 어떻게 해?
A. RAG 답변에서는 Grounding Rule을 유지해야 한다.

Q. Agent별 Grounding Rule도 필요해?
A. 필요하다. Agent 역할에 따라 우선 참조할 문서와 검증 기준이 다르기 때문이다.

Q. Context Assembly and Grounded Generation Checklist는 왜 필요해?
A. Retrieval 성공 이후 Generation 단계에서 문서와 다른 답변이 생성되는 문제를 줄이기 위해 필요하다.

Q. Review Agent가 이 Checklist를 써도 돼?
A. 적합하다. Review Agent는 Grounding Check와 Output Format 검증에 사용할 수 있다.

Q. RAG에서 Hallucination을 줄이려면 무엇을 해야 해?
A. Retrieved Context 우선 사용, Missing Information Rule, Citation Rule, Grounding Check를 적용해야 한다.

Q. Agent가 프로젝트 특화 사실을 임의로 생성하면 안 되는 이유는 뭐야?
A. 실제 프로젝트 구조와 다른 코드, 설정, 배포 절차를 만들 수 있기 때문이다.
