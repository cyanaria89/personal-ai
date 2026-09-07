# LangChain & LangGraph Part04 RAG Chain Retrieval Optimization

---

# 1. RAG Chain Core

## 1.1 RAG Chain 기본 개념

### [개념]

RAG Chain은 Retriever와 LLM을 연결해 문서 기반 답변을 생성하는 Pipeline이다.

RAG Chain은 LLM이 가진 일반 지식만 사용하는 구조가 아니다.

RAG Chain은 사용자 질문으로 관련 문서를 검색하고, 검색된 Context를 Prompt에 넣어 Grounded Answer를 생성한다.

기본 Flow:

```text
User Query
→ Query Preprocessing
→ Retriever
→ Retrieved Documents
→ Context Formatting
→ Prompt Template
→ Chat Model
→ Output Parser
→ Answer with Source
```

Part04는 Part03에서 만든 Retrieval Foundation을 실제 RAG Chain으로 연결하는 단계다.

Part03이 문서를 검색 가능한 상태로 만드는 과정이라면, Part04는 검색된 문서를 LLM 답변 생성에 안전하게 사용하는 과정이다.

---

### [핵심]

- RAG Chain은 검색 단계와 생성 단계를 연결한다.
- Retriever는 사용자 질문과 관련된 문서를 검색한다.
- Retrieved Documents는 Prompt Context로 사용된다.
- Context Formatting은 Source와 Section을 정리한다.
- Prompt Template은 Grounding Rule을 포함해야 한다.
- Chat Model은 Context 기반 답변을 생성한다.
- Output Parser는 답변 형식을 안정화한다.
- 문서에 없는 내용은 없다고 답해야 한다.
- Source를 함께 반환하면 검증 가능성이 높아진다.
- 검색 실패와 생성 실패를 구분해야 한다.

---

### [실무]

2026 실무 기준 RAG Chain은 단순히 `question → answer` 구조로 만들지 않는다.

권장 구조:

```text
Question
→ Query Rewrite
→ Metadata Filter
→ Retriever
→ Retrieved Documents
→ Context Filtering
→ Context Formatting
→ Grounded Prompt
→ Chat Model
→ Output Parser
→ Answer with Source
→ Evaluation
```

RAG Chain 구성 요소:

| 구성 요소           | 역할                    |
| ------------------- | ----------------------- |
| User Query          | 사용자 질문             |
| Query Rewrite       | 검색 Query 개선         |
| Metadata Filter     | 검색 범위 제한          |
| Retriever           | 관련 Chunk 검색         |
| Retrieved Documents | 검색된 문서             |
| Context Filtering   | 낮은 품질 Context 제거  |
| Context Formatting  | LLM 입력용 Context 정리 |
| Prompt Template     | 답변 규칙 주입          |
| Chat Model          | 답변 생성               |
| Output Parser       | 출력 형식 안정화        |
| Source              | 근거 문서 추적          |
| Evaluation          | 답변 품질 검증          |

RAG Chain 실패 패턴:

```text
Question
→ Retriever가 관련 없는 Chunk 검색
→ Prompt에 노이즈 Context 삽입
→ LLM이 부정확한 답변 생성
→ Source 검증 불가
```

RAG Chain 개선 패턴:

```text
Question
→ Query Rewrite
→ Metadata Filter
→ Retriever
→ Context Ranking
→ Grounded Prompt
→ Answer with Source
→ Review Agent 검증
```

---

### [FAQ]

Q. RAG Chain이 뭐야?

A.
사용자 질문으로 관련 문서를 검색하고, 검색된 Context를 LLM에 넣어 문서 기반 답변을 생성하는 Pipeline이다.

Q. RAG Chain에서 가장 중요한 단계는?

A.
Retriever와 Retrieved Context 품질이다. 잘못된 Context가 들어가면 답변도 부정확해진다.

Q. Grounded Answer가 뭐야?

A.
검색된 문서 Context에 근거해 생성된 답변이다.

Q. RAG Chain에 Source가 필요한 이유는?

A.
답변이 어떤 문서 근거에서 나왔는지 검증하기 위해 필요하다.

Q. Part04는 Part03과 어떻게 연결돼?

A.
Part03에서 검색 가능한 문서를 만들고, Part04에서 그 검색 결과를 Prompt Context로 사용해 답변을 생성한다.

---

# 2. RAG Chain Pipeline

## 2.1 단계별 Pipeline 설계

### [개념]

RAG Chain Pipeline은 검색과 생성을 순서대로 연결하는 구조다.

각 단계는 입력과 출력이 명확해야 한다.

기본 Pipeline:

```text
Input Question
→ Retrieve
→ Format Context
→ Generate Answer
→ Parse Output
→ Return Answer
```

각 단계의 출력은 다음 단계의 입력으로 사용된다.

RAG Chain은 LangChain Runnable로 구성할 수 있고, LangGraph에서는 RAG Node 내부에서 실행할 수 있다.

---

### [핵심]

- Query 입력 형식을 명확히 한다.
- Retriever 결과 형식을 명확히 한다.
- Context Formatting 기준을 정한다.
- Prompt Template에 Grounding Rule을 포함한다.
- Output Parser로 답변 형식을 안정화한다.
- Source와 Answer를 함께 반환한다.
- 각 단계별 실패 처리를 분리한다.
- LangGraph RAG Node에서 State를 읽고 결과를 State에 저장할 수 있다.

---

### [실무]

RAG Chain 단계별 입출력:

| 단계              | 입력                   | 출력                |
| ----------------- | ---------------------- | ------------------- |
| Query Input       | user_question          | normalized_query    |
| Query Rewrite     | normalized_query       | rewritten_query     |
| Retriever         | rewritten_query        | retrieved_documents |
| Context Filter    | retrieved_documents    | selected_documents  |
| Context Formatter | selected_documents     | formatted_context   |
| Prompt Template   | question + context     | prompt              |
| Chat Model        | prompt                 | llm_response        |
| Output Parser     | llm_response           | parsed_answer       |
| Final Response    | parsed_answer + source | answer_with_source  |

RAG Chain Output Schema 예시:

```json
{
  "answer": "LangGraph는 State, Node, Edge 기반으로 Agent Workflow를 설계하는 Framework다.",
  "sources": [
    {
      "source": "07_LangChain_LangGraph_Part01_Core_Overview.md",
      "section": "3. LangGraph Core"
    }
  ],
  "confidence": "medium",
  "missing_context": false
}
```

검색 실패 Output Schema 예시:

```json
{
  "answer": "문서에서 확인되지 않음.",
  "sources": [],
  "confidence": "low",
  "missing_context": true
}
```

LangGraph State 저장 예시:

```json
{
  "rewritten_query": "LangGraph State Node Edge Conditional Edge",
  "retrieved_context": [],
  "rag_answer": "문서에서 확인되지 않음.",
  "sources": [],
  "missing_context": true
}
```

---

### [FAQ]

Q. RAG Chain Pipeline은 어떻게 구성해?

A.
질문 입력, Query Rewrite, 문서 검색, Context Formatting, Prompt 생성, LLM 답변, Parser, Source 반환 순서로 구성한다.

Q. RAG Chain 단계별 입출력이 중요한 이유는?

A.
입출력이 명확해야 Chain 오류를 찾고 LangGraph Node와 연결하기 쉽기 때문이다.

Q. 검색 실패도 Output Schema로 반환해야 해?

A.
권장한다. 검색 실패와 생성 실패를 구분하고 Review Agent가 판단할 수 있기 때문이다.

Q. RAG Chain 결과에 confidence를 넣어도 돼?

A.
가능하다. 단, LLM의 주관적 확신이 아니라 검색 결과 품질과 근거 존재 여부를 기준으로 판단해야 한다.

Q. missing_context는 언제 true야?

A.
검색 결과가 없거나 질문에 답할 근거 문서가 부족할 때 true로 설정한다.

---

# 3. Context Formatting

## 3.1 Retrieved Context 정리

### [개념]

Context Formatting은 Retriever가 반환한 문서를 LLM이 읽기 쉬운 Prompt Context로 정리하는 단계다.

검색 결과를 그대로 Prompt에 넣으면 Source, Section, Content가 섞여 답변 품질이 낮아질 수 있다.

Context Formatting은 문서 근거를 구분 가능하게 만드는 작업이다.

기본 Flow:

```text
Retrieved Documents
→ Sort / Filter
→ Source Attach
→ Section Attach
→ Content Normalize
→ Formatted Context
```

Context Formatting은 RAG Grounding과 Source 검증의 기반이다.

---

### [핵심]

- Retrieved Documents는 LLM 입력 전에 정리해야 한다.
- Source와 Section을 함께 표시한다.
- 중복 Chunk를 제거한다.
- 관련도 낮은 Chunk를 제외한다.
- 너무 긴 Context는 제한하거나 요약한다.
- Code Block과 Table 구조를 가능한 유지한다.
- Context와 Question을 섞지 않는다.
- Context 순서는 관련도 또는 문서 Section 순서를 기준으로 정한다.

---

### [실무]

권장 Context Format:

```text
[Document 1]
Source: 07_LangChain_LangGraph_Part03_Document_Retrieval_Foundation.md
Section: 8. Retriever
Score: 0.82

Content:
Retriever는 사용자 Query와 관련된 문서 Chunk를 검색하는 구성 요소다.

[Document 2]
Source: 07_LangChain_LangGraph_Part03_Document_Retrieval_Foundation.md
Section: 9. Metadata Filtering
Score: 0.76

Content:
Metadata Filtering은 domain, part, section 조건으로 검색 범위를 제한한다.
```

Context Formatting 기준:

| 항목        | 기준                     |
| ----------- | ------------------------ |
| Source      | 파일명 또는 문서 ID 포함 |
| Section     | Header 기준 위치 포함    |
| Score       | 검색 관련도 표시         |
| Content     | 필요한 내용만 포함       |
| Order       | 관련도 또는 Section 순서 |
| Duplication | 중복 Chunk 제거          |
| Length      | Context Window 고려      |
| Separation  | Question과 Context 분리  |

금지 패턴:

```text
질문: Retriever가 뭐야?
문서내용: 이것저것 검색된 내용 전체...
```

문제:

- Source 구분 불가
- Section 구분 불가
- 질문과 문서 혼합
- LLM Grounding 약화
- Review Agent 검증 어려움

---

### [FAQ]

Q. Context Formatting이 뭐야?

A.
검색된 문서를 LLM이 근거로 사용하기 쉽도록 Source, Section, Content 형태로 정리하는 단계다.

Q. 검색 결과를 그대로 Prompt에 넣으면 안 돼?

A.
권장하지 않는다. Source와 내용이 섞이면 답변 근거를 구분하기 어렵다.

Q. Context에 Source를 넣어야 해?

A.
권장한다. Source가 있어야 답변 검증과 Review가 가능하다.

Q. 관련도 Score를 Context에 넣어도 돼?

A.
가능하다. 단, LLM이 Score를 절대적 사실로 오해하지 않도록 보조 정보로 사용해야 한다.

Q. Context와 Question은 왜 분리해야 해?

A.
문서 근거와 사용자 질문을 명확히 구분해야 Grounded Answer를 만들기 쉽기 때문이다.

---

# 4. Grounding Rule

## 4.1 문서 기반 답변 규칙

### [개념]

Grounding Rule은 LLM이 검색된 Context에 근거해서만 답변하도록 제한하는 규칙이다.

RAG Chain에서 LLM은 일반 지식을 자유롭게 보완하는 것이 아니라 제공된 문서를 기준으로 답변해야 한다.

기본 규칙:

```text
Use only the provided Context.
If the answer is not in the Context, say it is not found in the document.
Do not guess.
Return sources.
```

Grounding Rule은 Hallucination을 줄이고 Review Agent가 답변을 검증할 수 있게 한다.

---

### [핵심]

- RAG 답변은 Retrieved Context 기반이어야 한다.
- 문서에 없는 내용은 없다고 답한다.
- 추측으로 보완하지 않는다.
- Source 없는 답변은 신뢰도가 낮다.
- 여러 Source가 충돌하면 충돌을 명시한다.
- Context가 부족하면 missing_context로 처리한다.
- Review Agent는 Grounding 여부를 검증해야 한다.
- Prompt에 Grounding Rule을 명시적으로 포함한다.

---

### [실무]

RAG Prompt Grounding Rule 예시:

```text
System:
너는 문서 기반 RAG Agent다.

규칙:
- 반드시 제공된 Context에 근거해 답변하라.
- Context에 없는 내용은 "문서에서 확인되지 않음"이라고 답하라.
- 일반 지식으로 보완하지 마라.
- 답변에는 사용한 Source를 포함하라.
- Source 간 내용이 충돌하면 충돌을 명시하라.

Context:
{context}

Question:
{question}
```

Grounding 검증 기준:

| 항목              | 기준                                 |
| ----------------- | ------------------------------------ |
| Context Match     | 답변 내용이 Context에 존재하는가     |
| Source Match      | 답변 Source가 실제 검색 결과인가     |
| No Hallucination  | 문서에 없는 내용을 추가하지 않았는가 |
| Missing Context   | 근거 부족 시 없다고 답했는가         |
| Conflict Handling | 충돌 Source를 명시했는가             |
| Format Match      | Output Schema를 지켰는가             |

Review Agent Grounding Check:

```json
{
  "grounded": true,
  "unsupported_claims": [],
  "source_required": true,
  "missing_context": false
}
```

Unsupported Claim 예시:

```json
{
  "grounded": false,
  "unsupported_claims": ["Context에 없는 운영 배포 방식 설명 포함"],
  "source_required": true,
  "missing_context": false
}
```

---

### [FAQ]

Q. Grounding Rule이 뭐야?

A.
LLM이 제공된 Context에 근거해서만 답변하도록 제한하는 규칙이다.

Q. RAG 답변에서 추측하면 안 되는 이유는?

A.
RAG의 목적은 문서 기반 답변이므로 문서에 없는 내용을 보완하면 신뢰성이 떨어지기 때문이다.

Q. 문서에 없는 내용은 어떻게 처리해?

A.
문서에서 확인되지 않는다고 답하고 missing_context 상태로 처리한다.

Q. Source 간 내용이 충돌하면 어떻게 해?

A.
어느 Source가 충돌하는지 명시하고 단정하지 않는다.

Q. Grounding 여부는 누가 검증해?

A.
Review Agent 또는 RAG Evaluation 단계에서 답변과 Retrieved Context를 비교해 검증한다.

---

# 5. Query Rewrite

## 5.1 검색 Query 개선

### [개념]

Query Rewrite는 사용자 질문을 Retriever가 더 잘 검색할 수 있는 형태로 변환하는 단계다.

사용자 질문은 짧거나 모호할 수 있다.

문서 표현과 사용자 표현이 다르면 관련 문서가 검색되지 않을 수 있다.

기본 Flow:

```text
User Question
→ Query Rewrite
→ Retriever Query
→ Retrieved Documents
```

예시:

```text
사용자 질문:
"Graph는 언제 써?"

Rewrite Query:
"LangGraph Graph State Node Edge Conditional Edge Review Fix Loop Multi-Agent Workflow 사용 기준"
```

Query Rewrite는 Retrieval Recall을 높이는 데 유용하지만 사용자 의도를 바꾸면 안 된다.

---

### [핵심]

- Query Rewrite는 Retrieval Recall을 높인다.
- 사용자 표현을 문서 용어로 확장한다.
- 핵심 키워드를 추가한다.
- Domain과 task_type을 반영한다.
- Metadata Filter와 함께 사용하면 검색 정확도가 높아진다.
- 너무 과도한 Rewrite는 Query 의도를 흐릴 수 있다.
- Rewrite 전후 검색 결과를 비교해야 한다.
- Golden Query 실패 시 Query Rewrite를 고려한다.

---

### [실무]

Query Rewrite 적용 대상:

| 상황                           | Rewrite 필요성 |
| ------------------------------ | -------------- |
| 질문이 너무 짧음               | 높음           |
| 용어가 모호함                  | 높음           |
| 문서 용어와 사용자 표현이 다름 | 높음           |
| Domain이 불명확함              | 중간           |
| 이미 명확한 기술 용어          | 낮음           |
| Golden Query 실패              | 높음           |

Query Rewrite 예시:

| User Query         | Rewrite Query                                                                             |
| ------------------ | ----------------------------------------------------------------------------------------- |
| LangGraph 언제 써? | LangGraph State Node Edge Conditional Edge Review Fix Loop Multi-Agent Workflow 사용 기준 |
| 검색이 안돼        | Retriever 검색 실패 Chunk Metadata Top-K Threshold Golden Query Troubleshooting           |
| 도구 호출은?       | Tool Calling Tool Args Schema Tool Result Tool Error Agent Tool Use                       |
| 상태 저장은?       | LangGraph State Schema Checkpoint Memory State Update                                     |
| 검토 루프는?       | Review Fix Loop Review Node Fix Node Conditional Edge Max Iteration                       |

Rewrite Output Schema:

```json
{
  "original_query": "Graph는 언제 써?",
  "rewritten_query": "LangGraph Graph State Node Edge Conditional Edge Review Fix Loop Multi-Agent Workflow 사용 기준",
  "keywords": ["LangGraph", "State", "Node", "Edge", "Review Fix Loop"],
  "domain": "AI",
  "intent_preserved": true
}
```

Rewrite 금지:

- 사용자 의도 변경
- 존재하지 않는 요구사항 추가
- 특정 답변을 유도하는 편향된 Query 생성
- Metadata Filter와 충돌하는 Domain 추가
- 너무 긴 Query로 검색 노이즈 증가

---

### [FAQ]

Q. Query Rewrite가 뭐야?

A.
사용자 질문을 Retriever가 더 잘 검색할 수 있도록 문서 용어와 핵심 키워드 중심으로 바꾸는 단계다.

Q. Query Rewrite는 왜 필요해?

A.
사용자 표현과 문서 표현이 다르면 관련 Chunk가 검색되지 않을 수 있기 때문이다.

Q. Query Rewrite를 항상 해야 해?

A.
항상 필요하지는 않다. 질문이 짧거나 모호하거나 검색 실패가 잦을 때 우선 적용한다.

Q. Query Rewrite가 나쁘게 작동할 수도 있어?

A.
가능하다. 원래 질문 의도를 바꾸면 잘못된 문서가 검색될 수 있다.

Q. Query Rewrite 품질은 어떻게 확인해?

A.
Rewrite 전후 Retriever 결과를 Golden Query 기준으로 비교한다.

---

# 6. Metadata Filter in RAG Chain

## 6.1 Domain 기반 검색 범위 제한

### [개념]

Metadata Filter는 RAG Chain에서 Retriever가 검색할 문서 범위를 제한하는 조건이다.

Part03에서 Metadata를 설계하고 저장했다면, Part04에서는 그 Metadata를 사용해 RAG Chain 검색 범위를 제어한다.

기본 Flow:

```text
User Query
→ PM Agent task_type 분석
→ metadata_filter 생성
→ Retriever 검색 범위 제한
→ Retrieved Documents
```

Metadata Filter는 Multi-Agent 환경에서 특히 중요하다.

SQL Agent, Backend Agent, AI Agent가 같은 Vector Store를 사용하더라도 각 Agent는 자신의 Domain 문서를 우선 검색해야 한다.

---

### [핵심]

- Metadata Filter는 검색 범위를 제한한다.
- Domain Agent별 검색 정확도를 높인다.
- PM Agent가 task_type 기준으로 Filter를 생성할 수 있다.
- Filter가 없으면 관련 없는 Domain 문서가 섞일 수 있다.
- Filter가 너무 강하면 필요한 문서가 누락될 수 있다.
- Filter 필드명은 Part03 Metadata 설계와 일치해야 한다.
- Filter 적용 결과는 Golden Query로 검증해야 한다.

---

### [실무]

Metadata Filter 예시:

```json
{
  "domain": "AI",
  "document": "LangChain_LangGraph",
  "part": "Part04"
}
```

Agent별 Filter 예시:

| Agent          | Filter                            |
| -------------- | --------------------------------- |
| SQL Agent      | domain = "Backend", topic = "SQL" |
| Backend Agent  | domain = "Backend"                |
| Frontend Agent | domain = "Frontend"               |
| DevOps Agent   | domain = "DevOps"                 |
| AI Agent       | domain = "AI"                     |
| Review Agent   | domain in relevant_domains        |

Filter 적용 실패 예시:

```json
{
  "query": "State Schema는 어떻게 설계해?",
  "metadata_filter": {
    "domain": "Backend"
  },
  "result": "missing_context"
}
```

문제:

- 질문은 AI / LangGraph 관련
- Filter가 Backend로 제한됨
- Expected Source인 Part06 검색 실패

Filter 점검 기준:

- task_type과 domain이 일치하는가?
- document 필드명이 실제 Metadata와 일치하는가?
- part 조건이 과도하게 좁지 않은가?
- Review Agent는 필요한 여러 Domain을 검색할 수 있는가?
- Filter 없는 검색과 Filter 있는 검색 결과를 비교했는가?

---

### [FAQ]

Q. RAG Chain에서 Metadata Filter는 왜 필요해?

A.
관련 없는 Domain 문서가 Context에 섞이는 것을 줄이고 Agent별 검색 정확도를 높이기 위해 필요하다.

Q. Metadata Filter는 누가 정해?

A.
PM Agent, Router Node, RAG Node가 task_type과 required_agents를 기준으로 정할 수 있다.

Q. Metadata Filter가 너무 좁으면 어떻게 돼?

A.
필요한 문서가 검색되지 않아 missing_context가 발생할 수 있다.

Q. Metadata Filter는 Part03과 어떻게 연결돼?

A.
Part03에서 저장한 source, domain, document, part, section Metadata를 Part04 Retriever 검색 조건으로 사용한다.

Q. Review Agent도 Metadata Filter를 써?

A.
쓴다. 다만 Review Agent는 여러 Domain 결과를 검토해야 하므로 필요한 Domain 범위를 넓게 설정할 수 있다.

---

# 7. Hybrid Search

## 7.1 Vector Search와 Keyword Search 조합

### [개념]

Hybrid Search는 Vector Search와 Keyword Search를 함께 사용하는 검색 방식이다.

Vector Search는 의미 유사도에 강하고, Keyword Search는 정확한 용어 매칭에 강하다.

RAG 문서에서는 기술 용어, 클래스명, 메서드명, 설정값이 중요하므로 Hybrid Search가 유용할 수 있다.

기본 Flow:

```text
User Query
→ Vector Search
→ Keyword Search
→ Merge Results
→ Reranking
→ Retrieved Documents
```

---

### [핵심]

- Vector Search는 의미 유사도 검색에 강하다.
- Keyword Search는 정확한 용어 검색에 강하다.
- Hybrid Search는 두 결과를 합쳐 검색 품질을 높인다.
- 코드, 설정, API 이름 검색에는 Keyword Search가 유리할 수 있다.
- 개념 질문에는 Vector Search가 유리할 수 있다.
- 중복 결과 제거와 Reranking이 필요하다.
- Hybrid Search 결과도 Grounding 검증이 필요하다.

---

### [실무]

검색 방식 비교:

| 검색 방식      | 장점               | 단점                    |
| -------------- | ------------------ | ----------------------- |
| Vector Search  | 의미 유사도 검색   | 정확한 키워드 누락 가능 |
| Keyword Search | 정확한 용어 검색   | 표현이 다르면 검색 실패 |
| Hybrid Search  | 의미 + 키워드 보완 | Merge / Rank 설계 필요  |

Hybrid Search 적용 대상:

| Query 유형           | 권장 검색                     |
| -------------------- | ----------------------------- |
| 개념 질문            | Vector Search                 |
| 클래스명 / 메서드명  | Keyword Search                |
| 설정값 / 에러 메시지 | Keyword Search                |
| 모호한 질문          | Vector Search + Query Rewrite |
| 기술 문서 검색       | Hybrid Search                 |
| 코드 생성 근거 검색  | Hybrid Search                 |
| RAG 문서 검수        | Hybrid Search                 |

Hybrid Search 예시:

```text
Query:
"RunnableSequence invoke batch stream 차이"

Vector Search:
Runnable 실행 방식 관련 Chunk 검색

Keyword Search:
invoke, batch, stream 정확 매칭 Chunk 검색

Merge:
중복 제거 후 관련도 기준 재정렬
```

Hybrid Search 주의:

- Keyword Search 결과가 항상 정답은 아니다.
- Vector Search 결과와 Keyword Search 결과를 중복 제거해야 한다.
- 기술 용어가 많은 문서는 keyword score를 높게 볼 수 있다.
- 자연어 개념 질문은 vector score를 높게 볼 수 있다.
- 최종 Context는 Grounding Rule로 검증해야 한다.

---

### [FAQ]

Q. Hybrid Search가 뭐야?

A.
Vector Search와 Keyword Search를 함께 사용해 검색 결과를 보완하는 방식이다.

Q. Vector Search만 쓰면 안 돼?

A.
가능하지만 클래스명, 메서드명, 설정값 같은 정확한 용어 검색에서는 Keyword Search가 더 유리할 수 있다.

Q. Keyword Search만 쓰면 안 돼?

A.
가능하지만 사용자 표현과 문서 표현이 다르면 의미상 관련 문서를 놓칠 수 있다.

Q. Hybrid Search는 언제 좋아?

A.
기술 문서, 코드 문서, 설정값, API 이름, 개념 설명이 섞인 RAG 문서에서 유용하다.

Q. Hybrid Search 결과는 어떻게 정리해?

A.
Vector 결과와 Keyword 결과를 합치고 중복 제거 후 Reranking한다.

---

# 8. Reranking

## 8.1 검색 결과 재정렬

### [개념]

Reranking은 Retriever가 가져온 검색 결과를 다시 평가해 더 관련 있는 문서를 상위로 올리는 단계다.

Retriever의 1차 검색 결과에는 관련도가 낮은 Chunk가 섞일 수 있다.

Reranking은 Context 품질을 높이기 위해 사용된다.

기본 Flow:

```text
User Query
→ Retriever Top-K
→ Candidate Documents
→ Reranker
→ Ranked Documents
→ Context Formatting
```

Reranking은 검색 결과를 보완하는 단계이지, 나쁜 Chunk 설계를 완전히 해결하는 단계가 아니다.

---

### [핵심]

- Reranking은 검색 결과 순서를 재정렬한다.
- 1차 Retriever 결과의 노이즈를 줄인다.
- Context에 들어갈 최종 문서를 선택하는 데 유용하다.
- Cross-Encoder 기반 Reranker를 사용할 수 있다.
- LLM 기반 Reranking도 가능하지만 비용과 지연이 증가한다.
- Reranking 후에도 Source와 Metadata를 유지해야 한다.
- Reranker 품질은 Golden Query로 검증한다.
- Chunk 품질이 낮으면 Reranking 효과도 제한된다.

---

### [실무]

Reranking 적용 기준:

| 상황                        | Reranking 필요성 |
| --------------------------- | ---------------- |
| Top-K를 크게 가져오는 경우  | 높음             |
| 관련 없는 Chunk가 자주 섞임 | 높음             |
| 문서가 많음                 | 높음             |
| 답변 정확도가 중요함        | 높음             |
| 단순 FAQ 검색               | 낮음             |
| 소규모 문서셋               | 중간             |

Reranking Pipeline:

```text
Query
→ Retriever top_k = 20
→ Reranker
→ Top 5 Context
→ RAG Prompt
→ Answer
```

Reranking 주의:

- Reranking이 검색 실패를 완전히 해결하지는 않는다.
- 원본 Chunk 품질이 낮으면 Reranking 효과도 제한된다.
- Reranker가 Source Metadata를 제거하지 않도록 한다.
- 비용, 속도, 품질 균형을 고려한다.
- Reranking 전후 결과를 비교한다.
- Reranking 결과도 Review Agent가 Grounding 기준으로 검증할 수 있어야 한다.

---

### [FAQ]

Q. Reranking이 뭐야?

A.
검색된 Candidate Documents를 다시 평가해 더 관련 있는 문서를 상위로 재정렬하는 단계다.

Q. Reranking은 왜 필요해?

A.
Retriever 결과에 섞인 관련 없는 Chunk를 줄이고 Context 품질을 높이기 위해 필요하다.

Q. Reranking을 하면 검색 문제가 모두 해결돼?

A.
아니다. Chunk 품질, Metadata, Query Rewrite, Retriever 설정도 함께 개선해야 한다.

Q. Reranking은 언제 적용해?

A.
문서가 많거나 Top-K를 크게 가져오거나 관련 없는 Chunk가 자주 섞일 때 적용한다.

Q. Reranking 후에도 Metadata가 필요해?

A.
필요하다. Source와 Section을 유지해야 답변 근거를 추적할 수 있다.

---

# 9. Retrieval Optimization

## 9.1 검색 품질 최적화 기준

### [개념]

Retrieval Optimization은 RAG Chain에서 관련 문서를 더 정확히 찾기 위한 개선 작업이다.

RAG 실패는 LLM보다 Retrieval Pipeline에서 발생하는 경우가 많다.

Retrieval Optimization은 Chunk, Metadata, Embedding, Query, Retriever 설정, Reranking을 함께 조정한다.

기본 Flow:

```text
Retrieval Failure
→ Analyze Query
→ Check Chunk
→ Check Metadata
→ Tune Retriever
→ Add FAQ / Retrieval Queries
→ Re-embedding
→ Golden Query Test
```

---

### [핵심]

- Chunk 제목을 명확히 한다.
- FAQ와 Retrieval Queries를 강화한다.
- Metadata를 일관되게 유지한다.
- Query Rewrite를 적용한다.
- Top-K와 Threshold를 조정한다.
- Metadata Filter를 적절히 사용한다.
- 필요 시 Hybrid Search와 Reranking을 적용한다.
- 최적화 후 Golden Query Test를 수행한다.
- 검색 최적화 결과는 Part08 Evaluation Set에 반영한다.

---

### [실무]

Retrieval Optimization 대상:

| 대상              | 개선 방법                            |
| ----------------- | ------------------------------------ |
| Chunk             | 하나의 개념 단위로 분리              |
| Header            | 검색 키워드 포함                     |
| FAQ               | 사용자 질문 표현 추가                |
| Retrieval Queries | 실제 검색 질문 추가                  |
| Metadata          | domain, document, part, section 통일 |
| Query             | Rewrite / Expansion                  |
| Retriever         | Top-K / Threshold 조정               |
| Search Type       | similarity, mmr, hybrid 선택         |
| Reranking         | Candidate 재정렬                     |
| Evaluation        | Golden Query Test                    |

검색 실패 개선 순서:

```text
1. Golden Query로 실패 확인
2. 검색된 Chunk와 Expected Chunk 비교
3. Expected Chunk 제목과 FAQ 보강
4. Retrieval Queries 추가
5. Metadata Filter 조정
6. Top-K / Threshold 조정
7. Re-embedding
8. 재테스트
```

Optimization 결과 기록 예시:

```json
{
  "query": "Graph는 언제 써?",
  "failure_type": "expected_chunk_missing",
  "fixes": [
    "Part01 Retrieval Queries에 Graph 사용 기준 FAQ 추가",
    "Part06 Conditional Routing FAQ 보강",
    "metadata_filter AI domain으로 수정"
  ],
  "retest_result": "pass"
}
```

---

### [FAQ]

Q. Retrieval Optimization이 뭐야?

A.
RAG에서 관련 문서를 더 정확히 검색하기 위해 Chunk, Metadata, Query, Retriever 설정을 개선하는 작업이다.

Q. RAG 실패는 LLM 문제야?

A.
항상 그렇지 않다. 많은 경우 검색 실패, Chunk 품질, Metadata 문제에서 발생한다.

Q. 검색 품질을 가장 먼저 어떻게 개선해?

A.
Golden Query로 실패를 확인하고 Expected Chunk의 제목, FAQ, Retrieval Queries를 보강한다.

Q. Retrieval Queries는 왜 중요해?

A.
실제 사용자 질문 표현과 문서 Chunk를 직접 연결해 검색 매칭을 강화하기 때문이다.

Q. 최적화 후 무엇을 해야 해?

A.
Re-embedding 후 Golden Query Test로 검색 결과가 개선됐는지 확인한다.

---

# 10. RAG Evaluation

## 10.1 RAG 품질 평가

### [개념]

RAG Evaluation은 RAG Chain이 올바른 문서를 검색하고, 검색된 문서에 근거해 정확한 답변을 생성하는지 평가하는 과정이다.

RAG Evaluation은 검색 평가와 답변 평가를 분리해야 한다.

기본 Flow:

```text
Question
→ Retriever Evaluation
→ Context Evaluation
→ Answer Evaluation
→ Source Evaluation
```

검색이 실패하면 답변 생성이 좋아도 RAG 전체는 실패할 수 있다.

Part08의 Testing Strategy와 Evaluation Set은 Part04의 RAG Evaluation 기준을 확장한다.

---

### [핵심]

- Retriever 평가와 Answer 평가를 분리한다.
- Expected Document가 검색되는지 확인한다.
- Context가 질문에 충분한지 확인한다.
- 답변이 Context에 근거하는지 확인한다.
- Source가 정확한지 확인한다.
- 문서에 없는 내용을 생성하지 않는지 확인한다.
- Evaluation 결과는 개선 작업에 반영한다.
- Review Agent는 Evaluation 결과를 사용해 pass/fail을 판단할 수 있다.

---

### [실무]

RAG Evaluation 기준:

| 평가 항목                | 설명                          |
| ------------------------ | ----------------------------- |
| Retrieval Hit            | Expected Chunk 검색 여부      |
| Retrieval Rank           | Expected Chunk 상위 노출 여부 |
| Context Precision        | 검색 결과 중 관련 문서 비율   |
| Context Recall           | 필요한 근거가 포함됐는지      |
| Faithfulness             | 답변이 Context에 충실한지     |
| Answer Relevance         | 질문에 직접 답하는지          |
| Source Accuracy          | Source가 실제 근거인지        |
| Missing Context Handling | 근거 부족 시 없다고 답하는지  |
| Format Compliance        | Output Schema 준수 여부       |

Evaluation Output Schema:

```json
{
  "retrieval_hit": true,
  "expected_source_found": true,
  "context_precision": "high",
  "answer_grounded": true,
  "unsupported_claims": [],
  "source_accuracy": "valid",
  "result": "pass"
}
```

Evaluation 실패 Schema:

```json
{
  "retrieval_hit": false,
  "expected_source_found": false,
  "context_precision": "low",
  "answer_grounded": false,
  "unsupported_claims": ["문서에 없는 LangSmith 운영 심화 설명 포함"],
  "source_accuracy": "invalid",
  "result": "fail"
}
```

---

### [FAQ]

Q. RAG Evaluation이 뭐야?

A.
RAG Chain이 올바른 문서를 검색하고 문서에 근거해 정확히 답변하는지 평가하는 과정이다.

Q. Retriever 평가와 Answer 평가는 왜 분리해?

A.
검색이 실패했는지, 검색은 됐지만 답변 생성이 실패했는지 구분하기 위해 필요하다.

Q. Faithfulness가 뭐야?

A.
답변이 제공된 Context에 충실한지 평가하는 기준이다.

Q. Source Accuracy는 뭐야?

A.
답변에 표시된 Source가 실제 근거 문서와 일치하는지 확인하는 기준이다.

Q. RAG Evaluation 결과는 어디에 써?

A.
Chunk 보강, Query Rewrite, Retriever 튜닝, Prompt 개선, Review Agent 검증에 사용한다.

---

# 11. LangGraph RAG Node

## 11.1 RAG Chain을 LangGraph Node로 사용

### [개념]

LangGraph에서 RAG Chain은 하나의 Node로 구성할 수 있다.

RAG Node는 State에서 사용자 질문이나 작업 요구사항을 읽고, Retriever를 실행한 뒤, 검색 결과와 답변을 State에 저장한다.

기본 Flow:

```text
State
→ RAG Node
→ Query Rewrite
→ Retriever
→ RAG Chain
→ State Update
```

RAG Node는 PM Node, Domain Agent Node, Review Node와 연결할 수 있다.

RAG Node 내부에서는 LangChain Retriever, Prompt Template, Chat Model, Output Parser를 사용할 수 있다.

---

### [핵심]

- RAG Chain은 LangGraph Node 내부에서 실행할 수 있다.
- RAG Node는 State를 입력받는다.
- RAG Node는 rewritten_query를 State에 저장할 수 있다.
- RAG Node는 retrieved_context를 State에 저장한다.
- RAG Node는 rag_answer 또는 agent_output을 State에 저장한다.
- Metadata Filter는 State의 task_type을 기준으로 선택할 수 있다.
- 검색 실패는 State의 missing_context 또는 error에 기록한다.
- Review Node는 RAG Node 결과를 검증한다.

---

### [실무]

RAG Node State 예시:

```python
from typing import TypedDict

class AgentState(TypedDict):
    user_request: str
    task_type: str
    rewritten_query: str
    metadata_filter: dict
    retrieved_context: list[dict]
    rag_answer: str
    sources: list[dict]
    missing_context: bool
    error: str | None
```

RAG Node 실행 Flow:

```text
AgentState.user_request
→ Query Rewrite
→ Metadata Filter Selection
→ Retriever
→ Context Formatting
→ RAG Prompt
→ Chat Model
→ Parser
→ State Update
```

Domain별 RAG Node 예시:

| Node              | Metadata Filter            |
| ----------------- | -------------------------- |
| Backend RAG Node  | domain = "Backend"         |
| Frontend RAG Node | domain = "Frontend"        |
| AI RAG Node       | domain = "AI"              |
| DevOps RAG Node   | domain = "DevOps"          |
| Review RAG Node   | domain in relevant_domains |

RAG Node 오류 처리:

```text
Retriever Error
→ State.error = "retrieval_error"
→ Error Node or Fallback

No Context
→ State.missing_context = true
→ Final Node with "문서에서 확인되지 않음"

Parser Error
→ Retry
→ Error Node if failed
```

RAG Node Contract:

| Reads           | Writes            |
| --------------- | ----------------- |
| user_request    | rewritten_query   |
| task_type       | retrieved_context |
| metadata_filter | sources           |
| requirements    | rag_answer        |
|                 | missing_context   |
|                 | error             |

---

### [FAQ]

Q. RAG Chain을 LangGraph Node로 만들 수 있어?

A.
가능하다. Node 내부에서 Retriever, Prompt, Model, Parser를 실행하고 결과를 State에 저장할 수 있다.

Q. RAG Node는 State에서 무엇을 읽어?

A.
user_request, task_type, rewritten_query, metadata_filter 같은 값을 읽는다.

Q. RAG Node는 State에 무엇을 저장해?

A.
retrieved_context, rag_answer, sources, missing_context, error 같은 값을 저장한다.

Q. Metadata Filter는 어디서 결정해?

A.
PM Node나 Router Node가 task_type을 분석해 결정하거나 RAG Node 내부에서 선택할 수 있다.

Q. Review Node는 RAG Node 결과를 어떻게 검증해?

A.
rag_answer가 retrieved_context에 근거하는지, source가 정확한지, unsupported claim이 있는지 확인한다.

---

# 12. RAG Troubleshooting

## 12.1 RAG Chain 실패 처리

### [개념]

RAG Chain 실패는 검색 실패, Context Formatting 실패, Prompt 실패, LLM 생성 실패, Parser 실패, Source 검증 실패로 나눌 수 있다.

오류 유형을 구분해야 정확히 수정할 수 있다.

기본 Flow:

```text
RAG Failure
→ Identify Stage
→ Fix Retrieval or Generation
→ Re-evaluate
```

검색 실패와 생성 실패를 구분하는 것이 가장 중요하다.

---

### [핵심]

문제:

- 문서에 있는 내용인데 답변하지 못함
- 관련 없는 문서 기반 답변 생성
- Source가 틀림
- 문서에 없는 내용을 생성함
- JSON 출력 형식이 깨짐
- 검색 결과는 맞는데 답변이 부정확함

원인:

- Retriever 검색 실패
- Top-K 부족
- Threshold 과도
- Metadata Filter 오류
- Context Formatting 불량
- Prompt Grounding Rule 약함
- Parser 형식 지시 부족
- Source Mapping 오류
- Re-embedding 누락

해결:

- Golden Query Test 수행
- Retrieved Documents 직접 확인
- Metadata Filter 완화 또는 강화
- Top-K / Threshold 조정
- Query Rewrite 적용
- Context Formatting 개선
- Grounding Rule 강화
- Parser Retry 추가
- Source 검증 추가
- RAG Evaluation 재수행

---

### [실무]

Troubleshooting Matrix:

| 증상                  | 원인                 | 해결                       |
| --------------------- | -------------------- | -------------------------- |
| 문서가 있는데 못 찾음 | Retriever 실패       | Golden Query, FAQ 보강     |
| 엉뚱한 문서 검색      | Metadata Filter 부족 | Filter 강화                |
| 검색 결과 없음        | Threshold 과도       | Threshold 완화             |
| 관련 문서 누락        | Top-K 부족           | Top-K 증가                 |
| 답변이 추측 포함      | Grounding 약함       | Prompt Rule 강화           |
| Source가 틀림         | Source Mapping 오류  | Metadata 유지              |
| JSON 깨짐             | Parser 지시 부족     | Format Instruction + Retry |
| 답변이 너무 장황      | Context 노이즈       | Reranking / Context 제한   |

RAG 실패 처리 Flow:

```text
1. User Query 저장
2. Rewritten Query 확인
3. Metadata Filter 확인
4. Retriever 결과 확인
5. Expected Chunk 포함 여부 확인
6. Context Formatting 확인
7. Prompt Grounding Rule 확인
8. LLM Answer와 Context 비교
9. Source Mapping 확인
10. Evaluation 결과 기록
11. 문서 또는 Retriever 설정 개선
```

검색 실패 vs 생성 실패 구분:

| 구분           | 판단 기준                                    |
| -------------- | -------------------------------------------- |
| 검색 실패      | Expected Source가 Retrieved Documents에 없음 |
| 생성 실패      | Expected Source는 있는데 답변이 틀림         |
| Source 실패    | 답변 Source가 실제 근거와 불일치             |
| Parser 실패    | 내용은 있으나 Output Schema 불일치           |
| Grounding 실패 | Context에 없는 주장을 생성                   |

---

### [FAQ]

Q. RAG가 문서에 있는 내용을 못 찾는 이유는?

A.
Chunk 품질, Query 표현, Metadata Filter, Top-K, Threshold, Embedding 문제일 수 있다.

Q. 검색 결과는 맞는데 답변이 틀리는 이유는?

A.
Context Formatting이 나쁘거나 Prompt Grounding Rule이 약하거나 LLM이 문서 밖 내용을 보완했을 수 있다.

Q. Source가 틀리면 무엇을 확인해야 해?

A.
Metadata가 유지되는지, Context Formatting에서 Source가 잘 매핑되는지 확인해야 한다.

Q. RAG 답변이 JSON 형식을 자주 깨면 어떻게 해?

A.
Output Parser를 적용하고 Format Instruction을 강화하며 Parse 실패 시 Retry를 추가한다.

Q. RAG Troubleshooting의 첫 단계는?

A.
검색된 Retrieved Documents를 직접 확인해 검색 실패인지 생성 실패인지 구분하는 것이다.

---

# 13. Part04 Checklist

## 13.1 RAG Chain Checklist

### [Checklist]

- [ ] Part03 Retrieval Foundation과 연결되는가?
- [ ] RAG Chain의 검색 단계와 생성 단계를 분리했는가?
- [ ] Query Rewrite 기준이 있는가?
- [ ] Metadata Filter 기준이 있는가?
- [ ] Retriever 결과를 Context Formatting하는가?
- [ ] Context에 Source와 Section이 포함되는가?
- [ ] Context와 Question을 분리했는가?
- [ ] Prompt에 Grounding Rule이 포함되었는가?
- [ ] 문서에 없는 내용은 없다고 답하도록 했는가?
- [ ] Source를 함께 반환하는가?
- [ ] 검색 실패와 생성 실패를 구분하는가?
- [ ] Top-K와 Threshold 조정 기준이 있는가?
- [ ] Hybrid Search 적용 여부를 판단하는가?
- [ ] Reranking 적용 기준이 있는가?
- [ ] Golden Query Test를 수행하는가?
- [ ] RAG Evaluation 기준이 있는가?
- [ ] RAG Chain Output Schema가 있는가?
- [ ] RAG Node가 State를 읽고 업데이트하는가?
- [ ] RAG Node 오류를 State에 기록하는가?
- [ ] Review Node가 Grounding을 검증하는가?
- [ ] Part08 Evaluation Set과 연결되는가?
- [ ] 문서 수정 후 Re-embedding과 재평가를 수행하는가?

---

# Retrieval Queries

### [FAQ]

Q. RAG Chain이 뭐야?
A. 사용자 질문으로 관련 문서를 검색하고, 검색된 Context를 LLM에 넣어 문서 기반 답변을 생성하는 Pipeline이다.

Q. RAG Chain에서 가장 중요한 단계는?
A. Retriever와 Retrieved Context 품질이다. 잘못된 Context가 들어가면 답변도 부정확해진다.

Q. Grounded Answer가 뭐야?
A. 검색된 문서 Context에 근거해 생성된 답변이다.

Q. RAG Chain에 Source가 필요한 이유는?
A. 답변이 어떤 문서 근거에서 나왔는지 검증하기 위해 필요하다.

Q. Part04는 Part03과 어떻게 연결돼?
A. Part03에서 검색 가능한 문서를 만들고, Part04에서 그 검색 결과를 Prompt Context로 사용해 답변을 생성한다.

Q. RAG Chain Pipeline은 어떻게 구성해?
A. 질문 입력, Query Rewrite, 문서 검색, Context Formatting, Prompt 생성, LLM 답변, Parser, Source 반환 순서로 구성한다.

Q. RAG Chain 단계별 입출력이 중요한 이유는?
A. 입출력이 명확해야 Chain 오류를 찾고 LangGraph Node와 연결하기 쉽기 때문이다.

Q. 검색 실패도 Output Schema로 반환해야 해?
A. 권장한다. 검색 실패와 생성 실패를 구분하고 Review Agent가 판단할 수 있기 때문이다.

Q. missing_context는 언제 true야?
A. 검색 결과가 없거나 질문에 답할 근거 문서가 부족할 때 true로 설정한다.

Q. Context Formatting이 뭐야?
A. 검색된 문서를 LLM이 근거로 사용하기 쉽도록 Source, Section, Content 형태로 정리하는 단계다.

Q. 검색 결과를 그대로 Prompt에 넣으면 안 돼?
A. 권장하지 않는다. Source와 내용이 섞이면 답변 근거를 구분하기 어렵다.

Q. Context에 Source를 넣어야 해?
A. 권장한다. Source가 있어야 답변 검증과 Review가 가능하다.

Q. Context와 Question은 왜 분리해야 해?
A. 문서 근거와 사용자 질문을 명확히 구분해야 Grounded Answer를 만들기 쉽기 때문이다.

Q. Grounding Rule이 뭐야?
A. LLM이 제공된 Context에 근거해서만 답변하도록 제한하는 규칙이다.

Q. RAG 답변에서 추측하면 안 되는 이유는?
A. RAG의 목적은 문서 기반 답변이므로 문서에 없는 내용을 보완하면 신뢰성이 떨어지기 때문이다.

Q. Source 간 내용이 충돌하면 어떻게 해?
A. 어느 Source가 충돌하는지 명시하고 단정하지 않는다.

Q. Grounding 여부는 누가 검증해?
A. Review Agent 또는 RAG Evaluation 단계에서 답변과 Retrieved Context를 비교해 검증한다.

Q. Query Rewrite가 뭐야?
A. 사용자 질문을 Retriever가 더 잘 검색할 수 있도록 문서 용어와 핵심 키워드 중심으로 바꾸는 단계다.

Q. Query Rewrite는 왜 필요해?
A. 사용자 표현과 문서 표현이 다르면 관련 Chunk가 검색되지 않을 수 있기 때문이다.

Q. Query Rewrite를 항상 해야 해?
A. 항상 필요하지는 않다. 질문이 짧거나 모호하거나 검색 실패가 잦을 때 우선 적용한다.

Q. Query Rewrite 품질은 어떻게 확인해?
A. Rewrite 전후 Retriever 결과를 Golden Query 기준으로 비교한다.

Q. RAG Chain에서 Metadata Filter는 왜 필요해?
A. 관련 없는 Domain 문서가 Context에 섞이는 것을 줄이고 Agent별 검색 정확도를 높이기 위해 필요하다.

Q. Metadata Filter는 누가 정해?
A. PM Agent, Router Node, RAG Node가 task_type과 required_agents를 기준으로 정할 수 있다.

Q. Metadata Filter가 너무 좁으면 어떻게 돼?
A. 필요한 문서가 검색되지 않아 missing_context가 발생할 수 있다.

Q. Metadata Filter는 Part03과 어떻게 연결돼?
A. Part03에서 저장한 source, domain, document, part, section Metadata를 Part04 Retriever 검색 조건으로 사용한다.

Q. Hybrid Search가 뭐야?
A. Vector Search와 Keyword Search를 함께 사용해 검색 결과를 보완하는 방식이다.

Q. Vector Search만 쓰면 안 돼?
A. 가능하지만 클래스명, 메서드명, 설정값 같은 정확한 용어 검색에서는 Keyword Search가 더 유리할 수 있다.

Q. Keyword Search만 쓰면 안 돼?
A. 가능하지만 사용자 표현과 문서 표현이 다르면 의미상 관련 문서를 놓칠 수 있다.

Q. Hybrid Search는 언제 좋아?
A. 기술 문서, 코드 문서, 설정값, API 이름, 개념 설명이 섞인 RAG 문서에서 유용하다.

Q. Reranking이 뭐야?
A. 검색된 Candidate Documents를 다시 평가해 더 관련 있는 문서를 상위로 재정렬하는 단계다.

Q. Reranking은 왜 필요해?
A. Retriever 결과에 섞인 관련 없는 Chunk를 줄이고 Context 품질을 높이기 위해 필요하다.

Q. Reranking은 언제 적용해?
A. 문서가 많거나 Top-K를 크게 가져오거나 관련 없는 Chunk가 자주 섞일 때 적용한다.

Q. Retrieval Optimization이 뭐야?
A. RAG에서 관련 문서를 더 정확히 검색하기 위해 Chunk, Metadata, Query, Retriever 설정을 개선하는 작업이다.

Q. 검색 품질을 가장 먼저 어떻게 개선해?
A. Golden Query로 실패를 확인하고 Expected Chunk의 제목, FAQ, Retrieval Queries를 보강한다.

Q. Retrieval Queries는 왜 중요해?
A. 실제 사용자 질문 표현과 문서 Chunk를 직접 연결해 검색 매칭을 강화하기 때문이다.

Q. RAG Evaluation이 뭐야?
A. RAG Chain이 올바른 문서를 검색하고 문서에 근거해 정확히 답변하는지 평가하는 과정이다.

Q. Retriever 평가와 Answer 평가는 왜 분리해?
A. 검색이 실패했는지, 검색은 됐지만 답변 생성이 실패했는지 구분하기 위해 필요하다.

Q. Faithfulness가 뭐야?
A. 답변이 제공된 Context에 충실한지 평가하는 기준이다.

Q. Source Accuracy는 뭐야?
A. 답변에 표시된 Source가 실제 근거 문서와 일치하는지 확인하는 기준이다.

Q. RAG Chain을 LangGraph Node로 만들 수 있어?
A. 가능하다. Node 내부에서 Retriever, Prompt, Model, Parser를 실행하고 결과를 State에 저장할 수 있다.

Q. RAG Node는 State에서 무엇을 읽어?
A. user_request, task_type, rewritten_query, metadata_filter 같은 값을 읽는다.

Q. RAG Node는 State에 무엇을 저장해?
A. retrieved_context, rag_answer, sources, missing_context, error 같은 값을 저장한다.

Q. Metadata Filter는 어디서 결정해?
A. PM Node나 Router Node가 task_type을 분석해 결정하거나 RAG Node 내부에서 선택할 수 있다.

Q. Review Node는 RAG Node 결과를 어떻게 검증해?
A. rag_answer가 retrieved_context에 근거하는지, source가 정확한지, unsupported claim이 있는지 확인한다.

Q. RAG가 문서에 있는 내용을 못 찾는 이유는?
A. Chunk 품질, Query 표현, Metadata Filter, Top-K, Threshold, Embedding 문제일 수 있다.

Q. 검색 결과는 맞는데 답변이 틀리는 이유는?
A. Context Formatting이 나쁘거나 Prompt Grounding Rule이 약하거나 LLM이 문서 밖 내용을 보완했을 수 있다.

Q. Source가 틀리면 무엇을 확인해야 해?
A. Metadata가 유지되는지, Context Formatting에서 Source가 잘 매핑되는지 확인해야 한다.

Q. RAG Troubleshooting의 첫 단계는?
A. 검색된 Retrieved Documents를 직접 확인해 검색 실패인지 생성 실패인지 구분하는 것이다.
