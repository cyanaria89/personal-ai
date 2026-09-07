# Agentic RAG Domain Rules

---

# 1. Domain Purpose

## 1.1 Agentic RAG 문서 목적

### [개념]

Agentic RAG Domain 문서는 AI Agent / PM Agent / Backend Agent / Review Agent / AI/ML Agent가 Agentic RAG 기반 시스템을 설계, 구현, 검토, 개선할 때 참조하는 RAG 제작 규칙 문서이다.

Agentic RAG는 단순히 문서를 검색한 뒤 답변하는 RAG가 아니다.

Agentic RAG는 LLM Agent가 목적을 이해하고, 필요한 정보를 검색하고, 도구를 호출하고, 중간 결과를 검증하고, 부족한 정보를 다시 검색하며, 최종 답변이나 작업 결과를 생성하는 구조이다.

---

### [핵심]

- Agentic RAG = Agent + Retrieval + Tool Use + Reasoning + Validation
- 단순 RAG보다 Workflow 중심
- 검색 결과를 그대로 답하지 않음
- Agent가 검색 전략을 선택
- Agent가 필요한 도구를 호출
- Agent가 결과를 검증
- Agent가 부족한 정보를 재검색
- Multi-Agent System과 연결 가능
- PM Agent / Backend Agent / Review Agent / AI Agent가 모두 참조 가능해야 함

---

### [실무]

2026 실무 기준 Agentic RAG 문서는 다음 목적을 우선한다.

- AI Agent Workflow 설계
- Query Planning 지원
- Retrieval Strategy 선택 지원
- Tool Calling 설계 지원
- Multi-Step Reasoning 지원
- Self-Review / Self-Validation 지원
- Agent State 관리 지원
- Failure Handling 지원
- RAG Evaluation 지원

Agentic RAG 문서는 사람이 공부하기 위한 설명서가 아니라, Agent가 작업 중 검색해서 판단 기준으로 사용하는 운영 지식 문서로 작성한다.

---

### [FAQ]

Q. Agentic RAG 문서는 무엇을 위한 문서인가?

A. Agent가 RAG 검색, 도구 호출, 추론, 검증, 재검색을 수행할 수 있도록 기준을 제공하는 문서이다.

Q. Agentic RAG는 일반 RAG와 무엇이 다른가?

A. 일반 RAG는 검색 후 답변이 중심이고, Agentic RAG는 목표 달성을 위한 검색 계획, 도구 사용, 검증, 반복 수행이 중심이다.

Q. Agentic RAG Domain Rules의 주요 사용 Agent는?

A. PM Agent, AI/ML Agent, Backend Agent, Review Agent, DevOps Agent가 사용할 수 있다.

---

# 2. Scope

## 2.1 포함 범위

### [개념]

Agentic RAG Domain 문서는 Agent가 RAG 기반 작업을 자율적으로 수행하기 위해 필요한 설계 규칙, 실행 흐름, 도구 사용 규칙, 검증 규칙을 포함한다.

---

### [핵심]

포함 범위:

- Agentic RAG 개념
- RAG Workflow
- Query Planning
- Retrieval Strategy
- Multi-Step Retrieval
- Tool Calling
- Function Calling
- Agent State
- Memory
- Reflection
- Self-Validation
- Re-Retrieval
- Context Engineering
- Citation Grounding
- Answer Synthesis
- Failure Handling
- Multi-Agent RAG
- RAG Evaluation
- Observability
- Guardrails

제외 범위:

- LLM 수학 이론 상세
- Transformer 내부 구조 상세
- Vector Database 제품별 설치 상세
- LangChain / LangGraph 전체 API 문서 복붙
- 특정 클라우드 벤더 종속 구현
- Prompt 예술론 중심 장문 설명

---

### [실무]

Agentic RAG 문서는 아래 질문에 답할 수 있어야 한다.

- Agent가 어떤 순서로 검색해야 하는가?
- 검색 결과가 부족하면 어떻게 해야 하는가?
- 도구 호출은 언제 해야 하는가?
- Memory는 언제 사용해야 하는가?
- 답변 생성 전 어떤 검증을 해야 하는가?
- Multi-Agent 구조에서 어떤 Agent가 어떤 역할을 맡아야 하는가?
- Hallucination을 줄이기 위한 기준은 무엇인가?
- Retrieval 품질을 어떻게 평가해야 하는가?

---

### [FAQ]

Q. Agentic RAG Domain 문서에 LangGraph 코드 전체를 넣어야 하는가?

A. 아니다. 전체 코드보다 Workflow, Node 역할, State 전파, Retrieval 기준을 짧고 검색 친화적으로 작성한다.

Q. Vector Database 설치법도 포함해야 하는가?

A. 제품별 설치법은 Vector Database Domain Rules나 DevOps 문서로 분리하고, Agentic RAG에서는 검색 전략과 사용 기준만 다룬다.

Q. Prompt Engineering과 중복되는가?

A. 일부 겹치지만 Agentic RAG는 Prompt 자체보다 Agent Workflow, Retrieval Decision, Tool Use, Validation에 초점을 둔다.

---

# 3. Section Priority

## 3.1 필수 섹션 규칙

### [개념]

Agentic RAG 문서는 모든 주요 Chunk에 `[개념]`, `[핵심]`, `[실무]`, `[FAQ]`를 우선 적용한다.

복잡한 실행 흐름은 `[Flow]`를 추가한다.

검증이나 장애 대응이 필요한 주제는 `[Troubleshooting]`, `[Checklist]`, `[Best Practice]`를 추가한다.

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
- [Troubleshooting]
- [Comparison]

Optional:

- [Anti-Pattern]
- [Review Point]
- [Evaluation]
- [Observability]

---

### [실무]

Agentic RAG는 구조와 흐름이 중요하므로 단순 개념 설명만 작성하지 않는다.

각 문서는 아래 정보 중 최소 2개 이상을 포함한다.

- Agent Workflow
- Retrieval Decision
- Tool Calling Decision
- State Update
- Validation Point
- Failure Handling
- Review Checklist

---

### [FAQ]

Q. Agentic RAG 문서에 Flow는 필수인가?

A. 복잡한 Agent Workflow, Multi-Step Retrieval, Tool Calling 주제에서는 사실상 필수이다.

Q. FAQ는 왜 강화해야 하는가?

A. 사용자의 자연어 질문과 Agent의 내부 검색 Query가 FAQ 형태와 잘 매칭되기 때문이다.

Q. Agentic RAG 문서에 Checklist가 필요한가?

A. 필요하다. Review Agent와 AI/ML Agent가 검증 기준으로 사용하기 좋다.

---

# 4. Core Concept Rules

## 4.1 Agentic RAG 핵심 개념 작성 규칙

### [개념]

Agentic RAG 핵심 개념은 일반 RAG와 구분되도록 작성한다.

단순히 Retrieval Augmented Generation의 확장이라고만 설명하지 않는다.

Agent가 검색, 판단, 도구 호출, 검증, 재시도를 수행한다는 점을 반드시 포함한다.

---

### [핵심]

반드시 포함할 개념:

- Agent
- RAG
- Retriever
- Query Planning
- Context
- Tool Calling
- Function Calling
- State
- Memory
- Reflection
- Self-Validation
- Re-Retrieval
- Grounding
- Citation
- Evaluation
- Guardrails

용어 통일:

- Agentic RAG
- Query Planning
- Retrieval Strategy
- Tool Calling
- Agent State
- Short-Term Memory
- Long-Term Memory
- Self-Validation
- Re-Retrieval
- Context Engineering
- Grounded Answer

---

### [실무]

Agentic RAG 개념 문서는 아래 차이를 명확히 작성한다.

```text
Naive RAG
→ User Query
→ Retrieve
→ Generate Answer

Agentic RAG
→ User Goal Analysis
→ Query Planning
→ Retrieve
→ Tool Calling
→ Validate
→ Re-Retrieve
→ Synthesize
→ Final Answer
```

Agentic RAG 설명에서는 “검색 결과를 넣고 답변한다” 수준에서 멈추면 안 된다.

Agent가 목표 달성을 위해 어떤 판단을 하는지 작성해야 한다.

---

### [FAQ]

Q. Agentic RAG의 핵심은 무엇인가?

A. Agent가 검색 계획, 검색 실행, 도구 호출, 검증, 재검색을 반복하며 목표를 달성하는 것이다.

Q. Agentic RAG에서 Agent는 무엇을 판단하는가?

A. 어떤 정보를 검색할지, 어떤 도구를 호출할지, 검색 결과가 충분한지, 다시 검색해야 하는지를 판단한다.

Q. Agentic RAG에서 Grounding이 중요한 이유는?

A. 답변이 검색된 근거에 기반하지 않으면 Hallucination 가능성이 커지기 때문이다.

---

# 5. Workflow Rules

## 5.1 Agentic RAG Workflow 작성 규칙

### [개념]

Agentic RAG 문서는 Workflow 중심으로 작성한다.

Workflow는 Agent가 사용자 요청을 처리하는 단계별 흐름이다.

Workflow가 명확해야 PM Agent, AI Agent, Review Agent가 동일한 기준으로 작업을 분해하고 검토할 수 있다.

---

### [핵심]

기본 Workflow:

```text
User Request
→ Goal Analysis
→ Query Planning
→ Retrieval
→ Context Selection
→ Tool Calling
→ Intermediate Reasoning
→ Self-Validation
→ Re-Retrieval
→ Answer Synthesis
→ Final Review
→ Final Output
```

필수 작성 요소:

- 단계 이름
- 단계 목적
- 입력 데이터
- 출력 데이터
- 실패 조건
- 다음 단계 이동 기준

---

### [실무]

Workflow 문서는 아래 형식을 권장한다.

```md
### [Flow]

User Request
→ Goal Analysis
→ Query Planning
→ Retrieval
→ Validation
→ Final Answer

입력:

- userRequest
- agentState
- retrievedContext

출력:

- groundedAnswer
- validationResult
```

Workflow가 복잡한 경우 단계별 Chunk로 분리한다.

하나의 Chunk에 전체 Agentic RAG 시스템을 모두 설명하지 않는다.

---

### [FAQ]

Q. Agentic RAG Workflow에서 가장 중요한 단계는?

A. Query Planning, Retrieval, Self-Validation, Re-Retrieval 단계가 중요하다.

Q. Workflow 문서에 입력과 출력을 써야 하는가?

A. 써야 한다. Agent가 각 단계에서 무엇을 받아 무엇을 반환해야 하는지 알아야 한다.

Q. Workflow가 길어지면 어떻게 작성하는가?

A. 전체 Flow를 먼저 제시하고, 각 단계를 별도 Chunk로 분리한다.

---

# 6. Query Planning Rules

## 6.1 Query Planning 작성 규칙

### [개념]

Query Planning은 Agent가 사용자 요청을 바로 검색하지 않고, 검색 가능한 Query로 분해하는 과정이다.

Agentic RAG에서 Query Planning은 Retrieval 품질을 결정하는 핵심 단계이다.

---

### [핵심]

Query Planning 문서에는 다음을 포함한다.

- User Intent 분석
- Task Decomposition
- Search Query 생성
- Keyword Query 생성
- Semantic Query 생성
- Metadata Filter 조건 생성
- Re-Retrieval 조건
- Query Expansion
- Query Rewrite

Query 유형:

- Precision Query
- Recall Query
- Semantic Query
- Keyword Query
- Metadata Query
- Follow-up Query
- Verification Query

---

### [실무]

Query Planning 문서는 아래 예시처럼 작성한다.

```text
User Request:
Spring Security JWT 인증 흐름 검토해줘

Query Planning:
1. JWT Authentication Flow 검색
2. Security Filter Chain 검색
3. Access Token 검증 검색
4. Refresh Token 재발급 검색
5. Common Mistakes 검색
6. Review Checklist 검색
```

Agent가 하나의 Query만 사용하는 것을 기본값으로 두지 않는다.

복잡한 요청은 여러 검색 Query로 분해하도록 작성한다.

---

### [FAQ]

Q. Query Planning은 왜 필요한가?

A. 사용자 요청은 모호하거나 복합적이므로 Agent가 검색 가능한 단위로 분해해야 Retrieval 품질이 좋아진다.

Q. Precision Query와 Recall Query의 차이는?

A. Precision Query는 정확한 개념을 찾기 위한 Query이고, Recall Query는 관련 후보를 넓게 찾기 위한 Query이다.

Q. Query Rewrite는 언제 사용하는가?

A. 첫 검색 결과가 부족하거나 사용자 표현이 문서 용어와 다를 때 사용한다.

---

# 7. Retrieval Strategy Rules

## 7.1 Retrieval Strategy 작성 규칙

### [개념]

Retrieval Strategy는 Agent가 어떤 방식으로 문서를 검색하고, 어떤 Context를 선택할지 결정하는 규칙이다.

Agentic RAG 문서는 검색 방식 자체보다 검색 선택 기준을 명확히 작성해야 한다.

---

### [핵심]

필수 포함:

- Top-K Retrieval
- Hybrid Search
- Semantic Search
- Keyword Search
- Metadata Filtering
- Re-Ranking
- Context Window Control
- Chunk Selection
- Source Prioritization
- Duplicate Context Removal
- Stale Context Detection

검색 전략 선택 기준:

- 개념 질문 → Semantic Search
- 명령어 / 코드 질문 → Keyword + Semantic Search
- 최신성 필요 → Metadata / Version Filter
- 검증 요청 → Checklist / Common Mistakes 검색
- 장애 대응 → Troubleshooting 검색
- 구현 요청 → 예제 / Best Practice 검색

---

### [실무]

Agentic RAG 문서에는 Retrieval Strategy를 상황별로 작성한다.

```text
상황:
사용자가 에러 해결 요청

Retrieval Strategy:
1. Error Message Keyword Search
2. Troubleshooting Chunk Search
3. Common Mistakes Search
4. Best Practice Search
5. Verification Query Search
```

검색 결과가 부족하면 Agent는 Re-Retrieval을 수행해야 한다.

---

### [FAQ]

Q. Agentic RAG에서 Hybrid Search가 중요한 이유는?

A. 코드, 명령어, 설정값은 Keyword Search가 강하고, 개념 설명은 Semantic Search가 강하기 때문이다.

Q. Top-K 값은 항상 크게 잡아야 하는가?

A. 아니다. 너무 큰 Top-K는 노이즈를 증가시킬 수 있으므로 Re-Ranking과 Context Selection이 필요하다.

Q. Retrieval 결과가 부족하면 어떻게 해야 하는가?

A. Query Rewrite, Query Expansion, Metadata Filter 변경, Re-Retrieval을 수행한다.

---

# 8. Tool Calling Rules

## 8.1 Tool Calling 작성 규칙

### [개념]

Tool Calling은 Agent가 답변 생성을 위해 외부 도구, 내부 함수, 검색 시스템, 코드 실행기, DB, API 등을 호출하는 과정이다.

Agentic RAG에서 Tool Calling은 검색만으로 부족한 작업을 수행하기 위한 핵심 기능이다.

---

### [핵심]

Tool Calling 문서에는 다음을 포함한다.

- Tool 사용 조건
- Tool 입력값
- Tool 출력값
- Tool 실패 조건
- Tool 결과 검증
- Tool 재시도 조건
- Tool 호출 전 Retrieval 필요 여부
- Tool 호출 후 Answer Synthesis 기준

대표 Tool 유형:

- Search Tool
- File Search Tool
- Code Execution Tool
- Database Query Tool
- API Tool
- Calendar Tool
- Email Tool
- Browser Tool
- Calculator Tool
- Evaluation Tool

---

### [실무]

Tool Calling은 무조건 호출하지 않는다.

아래 기준을 따른다.

```text
Tool Calling 필요:
- 현재 정보가 필요함
- 계산이 필요함
- 파일 분석이 필요함
- 코드 실행 검증이 필요함
- DB 조회가 필요함
- 외부 API 결과가 필요함

Tool Calling 불필요:
- 제공된 문서만으로 충분함
- 단순 개념 설명
- 이미 검색된 Context로 답변 가능
```

Tool 결과는 그대로 답변하지 않고 검증 후 사용한다.

---

### [FAQ]

Q. Agentic RAG에서 Tool Calling은 언제 필요한가?

A. 검색된 문서만으로 답변할 수 없거나, 실행, 계산, 조회, 검증이 필요한 경우 사용한다.

Q. Tool Calling 결과를 바로 최종 답변으로 사용해도 되는가?

A. 아니다. Tool 결과를 검증하고 Context와 비교한 뒤 사용해야 한다.

Q. Tool Calling 실패 시 어떻게 해야 하는가?

A. 실패 원인을 기록하고, 재시도 가능 여부를 판단하거나 대체 경로를 사용한다.

---

# 9. Agent State Rules

## 9.1 Agent State 작성 규칙

### [개념]

Agent State는 Agent가 작업 중 유지하는 현재 상태 정보이다.

Agentic RAG에서는 사용자 요청, 검색 Query, 검색 결과, 도구 호출 결과, 검증 상태, 최종 출력 후보를 State로 관리한다.

---

### [핵심]

Agent State에 포함 가능한 정보:

- userRequest
- goal
- taskList
- queryPlan
- retrievedContext
- selectedContext
- toolCallHistory
- intermediateResult
- validationResult
- retryCount
- errorState
- finalAnswer

State 작성 규칙:

- State 이름 통일
- 입력 / 출력 명확화
- 단계별 업데이트 기준 작성
- 불필요한 개인정보 저장 금지
- 장기 저장 여부 분리

---

### [실무]

Agentic RAG Workflow 문서에는 State 변화를 포함하는 것이 좋다.

```text
User Request
→ state.userRequest 저장
→ state.goal 생성
→ state.queryPlan 생성
→ state.retrievedContext 저장
→ state.validationResult 저장
→ state.finalAnswer 생성
```

State가 불명확하면 Multi-Agent Workflow에서 정보 전달 오류가 발생한다.

---

### [FAQ]

Q. Agent State는 Memory와 같은가?

A. 아니다. Agent State는 현재 작업 흐름의 상태이고, Memory는 재사용 가능한 저장 정보이다.

Q. Agent State를 왜 문서화해야 하는가?

A. Agent가 단계별로 어떤 정보를 유지하고 전달해야 하는지 명확히 하기 위해서이다.

Q. State에 모든 정보를 저장해야 하는가?

A. 아니다. 작업 수행에 필요한 최소 정보만 저장해야 한다.

---

# 10. Memory Rules

## 10.1 Memory 작성 규칙

### [개념]

Memory는 Agent가 과거 정보, 사용자 선호, 장기 프로젝트 지식, 반복 작업 규칙을 저장하고 재사용하는 구조이다.

Agentic RAG 문서에서는 Short-Term Memory와 Long-Term Memory를 구분한다.

---

### [핵심]

Memory 유형:

- Short-Term Memory
- Long-Term Memory
- Episodic Memory
- Semantic Memory
- Project Memory
- User Preference Memory
- Tool Result Memory

Memory 사용 기준:

- 현재 작업에 필요한가?
- 장기적으로 재사용 가능한가?
- 민감정보인가?
- 최신성이 중요한가?
- RAG 문서와 충돌하지 않는가?

---

### [실무]

Memory는 무조건 사용하지 않는다.

```text
사용 적합:
- 프로젝트 구조
- 사용자 선호 출력 형식
- 반복되는 개발 규칙
- Agent Workflow 설정
- 장기 RAG 제작 기준

사용 부적합:
- 일회성 임시 값
- 민감한 개인정보
- 검증되지 않은 추측
- 오래되어 바뀔 가능성이 큰 정보
```

Memory와 RAG 문서가 충돌하면 최신 Project Progress와 Domain Rules를 우선한다.

---

### [FAQ]

Q. Agentic RAG에서 Memory는 왜 필요한가?

A. 반복되는 프로젝트 규칙, 사용자 선호, 장기 작업 맥락을 유지하기 위해 필요하다.

Q. Memory와 RAG 문서 중 무엇을 우선해야 하는가?

A. 명시적인 최신 Domain Rules와 Project Progress를 우선한다.

Q. 모든 사용자 정보를 Memory에 저장해야 하는가?

A. 아니다. 장기적으로 유용하고 안전한 정보만 저장해야 한다.

---

# 11. Validation Rules

## 11.1 Self-Validation 작성 규칙

### [개념]

Self-Validation은 Agent가 최종 답변 전 자신의 검색 결과, 근거, 논리, 출력 형식을 검증하는 단계이다.

Agentic RAG 문서에서는 검증 기준을 반드시 포함해야 한다.

---

### [핵심]

검증 항목:

- 사용자 요청 충족 여부
- 검색 근거 충분성
- Context와 답변 일치 여부
- Hallucination 여부
- 최신성 필요 여부
- Tool 결과 검증 여부
- 출력 형식 준수 여부
- 누락된 단계 여부
- 위험한 권장 여부
- 재검색 필요 여부

---

### [실무]

Self-Validation 문서는 Checklist 형태가 적합하다.

```md
### [Checklist]

- 사용자 요청을 직접 해결했는가?
- 검색된 Context에 근거했는가?
- 근거 없는 내용을 생성하지 않았는가?
- 부족한 정보는 부족하다고 표시했는가?
- 필요한 경우 Re-Retrieval을 수행했는가?
- 출력 형식을 지켰는가?
```

Review Agent가 그대로 사용할 수 있도록 짧고 명확하게 작성한다.

---

### [FAQ]

Q. Self-Validation은 왜 필요한가?

A. Agent가 검색 결과와 무관한 답변을 생성하거나 누락된 정보를 확신하는 문제를 줄이기 위해 필요하다.

Q. 검증 실패 시 어떻게 해야 하는가?

A. Re-Retrieval, Tool Re-Call, 답변 축소, 불확실성 표시 중 하나를 수행한다.

Q. Self-Validation은 최종 답변 후에 하는가?

A. 아니다. 최종 답변 생성 전에 수행해야 한다.

---

# 12. Re-Retrieval Rules

## 12.1 Re-Retrieval 작성 규칙

### [개념]

Re-Retrieval은 초기 검색 결과가 부족하거나 불명확할 때 Agent가 검색 Query를 수정하여 다시 검색하는 과정이다.

Agentic RAG에서 Re-Retrieval은 답변 품질을 높이는 핵심 반복 단계이다.

---

### [핵심]

Re-Retrieval 조건:

- 검색 결과 부족
- 검색 결과 충돌
- Context가 오래됨
- 사용자 질문 일부만 해결됨
- 코드 예제가 없음
- Troubleshooting 근거 부족
- 검증 Checklist 누락
- Tool 결과와 문서 내용 불일치

Re-Retrieval 방식:

- Query Rewrite
- Query Expansion
- Keyword 추가
- Domain 용어 변경
- Metadata Filter 변경
- 관련 FAQ 검색
- Common Mistakes 검색
- Troubleshooting 검색

---

### [실무]

Re-Retrieval은 무한 반복하지 않는다.

```text
권장:
1차 Retrieval
→ Validation
→ Re-Retrieval
→ Final Validation
→ Answer

주의:
- 동일 Query 반복 금지
- 근거 없는 재시도 금지
- retryCount 관리
- 실패 시 불확실성 표시
```

---

### [FAQ]

Q. Re-Retrieval은 언제 해야 하는가?

A. 검색 결과가 부족하거나, 답변 근거가 약하거나, 사용자 요청의 일부만 해결된 경우 수행한다.

Q. 같은 Query로 다시 검색해도 되는가?

A. 권장하지 않는다. Query Rewrite나 Keyword 추가가 필요하다.

Q. Re-Retrieval은 몇 번까지 해야 하는가?

A. 시스템 정책에 따라 제한해야 하며, 무한 반복은 금지한다.

---

# 13. Context Engineering Rules

## 13.1 Context Engineering 작성 규칙

### [개념]

Context Engineering은 Agent가 검색된 Chunk, Tool 결과, Memory, 사용자 요청을 조합하여 LLM 입력 Context를 구성하는 과정이다.

Agentic RAG에서는 검색보다 Context 선택과 배치가 답변 품질에 큰 영향을 준다.

---

### [핵심]

Context Engineering 요소:

- Context Selection
- Context Compression
- Context Ordering
- Duplicate Removal
- Conflict Detection
- Source Priority
- Token Budget Control
- Instruction Priority
- Retrieved Evidence
- Final Prompt Assembly

우선순위:

```text
System / Master Rules
→ Domain Rules
→ Project Progress
→ User Request
→ Retrieved Context
→ Memory
→ Tool Result
```

---

### [실무]

Context 구성 시 아래 기준을 적용한다.

```text
포함:
- 사용자 요청과 직접 관련된 Chunk
- 최신 Project Progress
- 해당 Domain Rules
- 예제 코드 또는 명령어
- Checklist
- FAQ

제외:
- 중복 Chunk
- 관련성 낮은 일반 설명
- 오래된 규칙
- 충돌하는 이전 정보
- 근거 없는 Memory
```

---

### [FAQ]

Q. Context Engineering은 왜 중요한가?

A. 검색 결과가 좋아도 LLM 입력 Context가 어지럽거나 충돌하면 답변 품질이 낮아지기 때문이다.

Q. Context가 너무 많으면 어떻게 해야 하는가?

A. 중복 제거, 압축, 우선순위 정렬, 핵심 Chunk 선택을 수행한다.

Q. Domain Rules와 Memory가 충돌하면 무엇을 우선하는가?

A. 최신 Domain Rules와 Project Progress를 우선한다.

---

# 14. Multi-Agent RAG Rules

## 14.1 Multi-Agent 구조 작성 규칙

### [개념]

Multi-Agent RAG는 여러 Agent가 역할을 나누어 RAG 검색, 작업 수행, 검토, 수정, 최종 출력을 담당하는 구조이다.

Agentic RAG Domain 문서는 Multi-Agent Workflow와 역할 분리를 명확히 작성해야 한다.

---

### [핵심]

대표 Agent 역할:

- PM Agent: 요청 분석, 작업 분해, Agent Routing
- Backend Agent: Backend 설계, 코드 생성, 구현 판단
- Frontend Agent: UI 구현, API 연동, 상태 관리
- DevOps Agent: 배포, 서버, Docker, Linux, CI/CD 판단
- AI/ML Agent: RAG, Agent, LLM, Evaluation 설계
- Review Agent: 검증, 누락 확인, 품질 리뷰
- Architecture Review Agent: 구조 검토, 확장성 검토

---

### [실무]

Multi-Agent RAG Workflow 예시:

```text
User Request
→ PM Agent
→ Query Planning
→ Domain Routing
→ Specialist Agent Retrieval
→ Specialist Agent Output
→ Review Agent Validation
→ Fix Request
→ Final Output
```

Agent 간 전달 정보:

- taskGoal
- domain
- queryPlan
- retrievedContext
- outputDraft
- validationResult
- fixRequest
- finalOutput

---

### [FAQ]

Q. Multi-Agent RAG에서 PM Agent의 역할은?

A. 사용자 요청을 분석하고 작업을 분해한 뒤 적절한 Specialist Agent에게 전달하는 것이다.

Q. Review Agent는 왜 필요한가?

A. Specialist Agent의 출력이 근거, 형식, 품질, 누락 여부를 만족하는지 검증하기 위해 필요하다.

Q. 모든 요청에 모든 Agent를 사용해야 하는가?

A. 아니다. 요청 Domain에 따라 필요한 Agent만 사용해야 한다.

---

# 15. Evaluation Rules

## 15.1 Agentic RAG Evaluation 작성 규칙

### [개념]

Agentic RAG Evaluation은 Agent가 검색, 도구 사용, 추론, 검증, 최종 답변을 제대로 수행했는지 평가하는 기준이다.

단순 답변 정확도만 평가하지 않는다.

---

### [핵심]

평가 항목:

- Query Planning Quality
- Retrieval Precision
- Retrieval Recall
- Context Relevance
- Tool Calling Accuracy
- State Consistency
- Groundedness
- Faithfulness
- Answer Completeness
- Format Compliance
- Re-Retrieval Decision
- Hallucination Rate
- User Goal Completion

---

### [실무]

Agentic RAG 평가 문서는 Checklist와 Metric을 함께 작성한다.

```md
### [Checklist]

- Query가 사용자 요청을 충분히 분해했는가?
- 검색 결과가 답변에 실제 사용되었는가?
- Tool Calling이 필요한 상황에서 호출되었는가?
- Tool Calling이 불필요한 상황에서 남발되지 않았는가?
- 답변이 Context에 근거했는가?
- 검증 후 최종 출력했는가?
```

정량 평가와 정성 평가를 함께 사용한다.

---

### [FAQ]

Q. Agentic RAG 평가는 일반 RAG 평가와 무엇이 다른가?

A. 검색 품질뿐 아니라 Query Planning, Tool Calling, State 관리, 검증, 재검색 판단까지 평가한다.

Q. Groundedness는 무엇인가?

A. 답변이 검색된 근거와 실제로 연결되어 있는 정도이다.

Q. Tool Calling도 평가해야 하는가?

A. 해야 한다. 잘못된 도구 호출이나 불필요한 호출은 Agentic RAG 품질을 낮춘다.

---

# 16. Troubleshooting Rules

## 16.1 Agentic RAG 장애 대응 작성 규칙

### [개념]

Agentic RAG Troubleshooting 문서는 Agent Workflow에서 발생하는 검색 실패, 도구 호출 실패, State 오류, Hallucination, 무한 반복 문제를 해결하기 위한 규칙이다.

---

### [핵심]

자주 발생하는 문제:

- Query Planning 실패
- Retrieval 결과 부족
- 관련 없는 Chunk 검색
- Context 과다
- Context 충돌
- Tool Calling 실패
- Tool Calling 남발
- State 누락
- Memory 오염
- Re-Retrieval 무한 반복
- Hallucination
- 출력 형식 위반
- Review 누락

---

### [실무]

Troubleshooting 형식:

```md
문제:
Agent가 관련 없는 문서를 검색함

원인:
Query가 너무 포괄적이거나 Domain Keyword가 부족함

해결:

- Query Rewrite 수행
- Domain Keyword 추가
- Metadata Filter 적용
- FAQ Chunk 검색
- Common Mistakes Chunk 검색
```

장애 대응 문서는 “문제 / 원인 / 해결” 형식을 기본으로 한다.

---

### [FAQ]

Q. Agentic RAG에서 가장 흔한 실패는?

A. Query Planning 실패, Retrieval Noise, Context 충돌, Tool Calling 남발, 검증 누락이다.

Q. 관련 없는 문서가 계속 검색되면 어떻게 해야 하는가?

A. Query Rewrite, Metadata Filter, Domain Keyword 추가, Re-Ranking을 적용한다.

Q. Agent가 무한 반복하면 어떻게 해야 하는가?

A. retryCount를 제한하고 실패 시 불확실성을 표시하거나 Human Review로 넘긴다.

---

# 17. Common Mistakes

## 17.1 자주 발생하는 작성 오류

### [개념]

Agentic RAG 문서는 개념 설명이 아니라 Agent 실행 기준 문서이다.

따라서 일반 AI 설명문처럼 작성하면 Retrieval 품질과 Agent 실행 품질이 낮아진다.

---

### [핵심]

금지 또는 주의:

- Agentic RAG를 일반 RAG처럼 설명
- Workflow 없이 개념만 작성
- Tool Calling 기준 누락
- Query Planning 기준 누락
- Re-Retrieval 기준 누락
- Self-Validation 누락
- Memory와 State 혼용
- LangChain / LangGraph 코드 복붙
- 장문 서술형 설명
- FAQ 부족
- Retrieval Queries 누락
- 용어 혼용
- 최신성 기준 누락
- 실패 조건 누락

---

### [실무]

나쁜 문서 예시:

```text
Agentic RAG는 AI Agent가 RAG를 사용하는 방식이다.
LangChain을 사용하면 쉽게 구현할 수 있다.
```

좋은 문서 예시:

```text
Agentic RAG는 Agent가 Query Planning, Retrieval, Tool Calling, Self-Validation, Re-Retrieval을 수행하는 구조이다.

Flow:
User Request
→ Goal Analysis
→ Query Planning
→ Retrieval
→ Tool Calling
→ Validation
→ Final Output
```

---

### [FAQ]

Q. Agentic RAG 문서에서 가장 피해야 할 것은?

A. Workflow, Query Planning, Validation 없이 개념 설명만 길게 작성하는 것이다.

Q. 코드 예제는 많이 넣는 것이 좋은가?

A. 아니다. 핵심 Workflow나 State 구조를 보여주는 짧은 Snippet만 넣는 것이 좋다.

Q. Tool Calling 설명은 필수인가?

A. 필수에 가깝다. Agentic RAG는 단순 검색보다 도구 사용과 판단이 중요하기 때문이다.

---

# 18. Document Split Rules

## 18.1 Agentic RAG 문서 분할 기준

### [개념]

Agentic RAG는 범위가 넓기 때문에 하나의 문서에 모두 작성하지 않는다.

RAG Retrieval 품질을 위해 Part 단위로 분리한다.

---

### [핵심]

권장 문서 분할:

```text
Agentic_RAG_Part01_Core.md
Agentic_RAG_Part02_Query_Planning.md
Agentic_RAG_Part03_Retrieval_Strategy.md
Agentic_RAG_Part04_Tool_Calling.md
Agentic_RAG_Part05_Agent_State_Memory.md
Agentic_RAG_Part06_Workflow_Orchestration.md
Agentic_RAG_Part07_Validation_Evaluation.md
Agentic_RAG_Part08_Troubleshooting_Best_Practice.md
```

분할 기준:

- 하나의 Part는 하나의 핵심 주제
- 각 Part는 독립 검색 가능
- 각 Part는 FAQ 포함
- 각 Part는 Retrieval Queries 포함
- Workflow 관련 Part는 Flow 필수
- Evaluation 관련 Part는 Checklist 필수

---

### [실무]

Agentic RAG 문서 Set은 AI Expert Level에서 사용한다.

단, PM Agent와 Review Agent도 참조할 수 있으므로 너무 특정 프레임워크 중심으로 작성하지 않는다.

프레임워크보다 Workflow, Decision Rule, Validation Rule을 우선한다.

---

### [FAQ]

Q. Agentic RAG 문서는 몇 개 Part로 나누는 것이 좋은가?

A. 6~8개 Part를 권장한다. Core, Query Planning, Retrieval, Tool Calling, State/Memory, Workflow, Evaluation, Troubleshooting으로 분리한다.

Q. LangGraph 전용 문서로 작성해도 되는가?

A. Agentic RAG Domain Rules는 프레임워크 중립으로 작성하고, LangGraph 세부 구현은 별도 Domain Rules나 Part 문서에서 다룬다.

Q. 각 Part에도 Retrieval Queries가 필요한가?

A. 필요하다. 각 문서가 독립 검색될 수 있어야 한다.

---

# 19. Agent Usage Rules

## 19.1 Agent별 사용 기준

### [개념]

Agentic RAG Domain Rules는 여러 Agent가 동일한 기준으로 RAG 기반 작업을 수행하도록 돕는다.

각 Agent는 자신의 역할에 맞는 Chunk를 우선 검색한다.

---

### [핵심]

PM Agent:

- User Request 분석
- Task Decomposition
- Agent Routing
- Workflow 선택

AI/ML Agent:

- Agentic RAG 구조 설계
- Query Planning 설계
- Tool Calling 설계
- Evaluation 설계

Backend Agent:

- RAG API 구현
- Tool Calling Backend 구현
- Agent State 저장 구조 구현
- Vector DB 연동 구현

DevOps Agent:

- Agent 실행 환경 구성
- Vector DB 운영
- Observability 구성
- 배포 및 장애 대응

Review Agent:

- Groundedness 검증
- Hallucination 검토
- Workflow 누락 검토
- Output Format 검토
- Common Mistakes 검토

---

### [실무]

Agentic RAG 문서 검색 우선순위:

```text
PM Agent
→ Workflow / Query Planning / Agent Routing

AI/ML Agent
→ Retrieval Strategy / Tool Calling / Evaluation

Backend Agent
→ State / API / Tool Integration

DevOps Agent
→ Observability / Failure Handling / Deployment

Review Agent
→ Self-Validation / Checklist / Common Mistakes
```

---

### [FAQ]

Q. Agentic RAG Domain Rules는 AI Agent만 사용하는가?

A. 아니다. PM Agent, Backend Agent, DevOps Agent, Review Agent도 역할에 따라 사용한다.

Q. Review Agent는 어떤 부분을 우선 검색해야 하는가?

A. Self-Validation, Evaluation, Common Mistakes, Troubleshooting Chunk를 우선 검색한다.

Q. Backend Agent는 어떤 부분을 우선 검색해야 하는가?

A. Agent State, Tool Calling, API Integration, Vector DB 연동 기준을 우선 검색한다.

---

# 20. Final Goal

## 20.1 최종 목표

### [개념]

Agentic RAG Domain Rules의 최종 목표는 Agent가 RAG 문서를 단순 검색 자료가 아니라 작업 수행 기준으로 사용할 수 있게 만드는 것이다.

Agent는 이 문서를 통해 검색 계획을 세우고, 도구를 호출하고, 결과를 검증하고, 필요하면 재검색하며, 최종 결과를 생성해야 한다.

---

### [핵심]

최종 목표:

- Agentic RAG 개념 검색 가능
- Workflow 설계 가능
- Query Planning 가능
- Retrieval Strategy 선택 가능
- Tool Calling 기준 판단 가능
- Agent State 설계 가능
- Memory 사용 판단 가능
- Self-Validation 가능
- Re-Retrieval 가능
- Multi-Agent RAG 설계 가능
- Evaluation 가능
- Troubleshooting 가능

---

### [실무]

Agentic RAG RAG Doc Set은 다음 작업을 지원해야 한다.

```text
User Request
→ Agent가 목표 분석
→ 검색 Query 생성
→ 관련 문서 검색
→ Tool Calling 판단
→ 결과 검증
→ 부족하면 재검색
→ 최종 답변 생성
→ Review Agent 검토
```

문서 품질이 Agentic RAG 품질을 결정한다.

---

### [FAQ]

Q. Agentic RAG Domain Rules의 최종 목적은?

A. Agent가 검색, 도구 호출, 추론, 검증, 재검색을 수행할 수 있도록 문서 제작 기준을 제공하는 것이다.

Q. 이 문서는 사람 학습용인가?

A. 아니다. AI Agent Retrieval과 Agent Workflow 실행 품질을 높이기 위한 문서이다.

Q. Agentic RAG 문서 품질은 무엇으로 판단하는가?

A. Agent가 필요한 Chunk를 잘 검색하고, 작업 판단과 검증에 사용할 수 있는지로 판단한다.

---

# Retrieval Queries

### [FAQ]

Q. Agentic RAG란?
A. Agent가 Query Planning, Retrieval, Tool Calling, Self-Validation, Re-Retrieval을 수행하는 RAG 구조이다.

Q. Agentic RAG와 일반 RAG의 차이는?
A. 일반 RAG는 검색 후 답변이 중심이고, Agentic RAG는 목표 분석, 검색 계획, 도구 호출, 검증, 재검색이 중심이다.

Q. Agentic RAG Workflow는?
A. User Request → Goal Analysis → Query Planning → Retrieval → Tool Calling → Validation → Re-Retrieval → Final Output 흐름이다.

Q. Agentic RAG에서 Query Planning이 중요한 이유는?
A. 사용자 요청을 검색 가능한 단위로 분해해야 정확한 Retrieval이 가능하기 때문이다.

Q. Agentic RAG에서 Tool Calling은 언제 사용하는가?
A. 검색된 문서만으로 부족하고 계산, 실행, 조회, 외부 API, 파일 분석, 코드 검증이 필요한 경우 사용한다.

Q. Agentic RAG에서 Self-Validation은 무엇인가?
A. 최종 답변 전 검색 근거, 논리, 출력 형식, Tool 결과, 누락 여부를 검증하는 단계이다.

Q. Agentic RAG에서 Re-Retrieval은 언제 필요한가?
A. 검색 결과가 부족하거나 충돌하거나 사용자 요청 일부만 해결된 경우 필요하다.

Q. Agent State란?
A. Agent가 현재 작업 중 유지하는 userRequest, goal, queryPlan, retrievedContext, validationResult 같은 상태 정보이다.

Q. Agent State와 Memory의 차이는?
A. Agent State는 현재 작업 상태이고, Memory는 장기적으로 재사용 가능한 저장 정보이다.

Q. Multi-Agent RAG란?
A. PM Agent, Specialist Agent, Review Agent 등이 역할을 나누어 RAG 기반 작업을 수행하는 구조이다.

Q. Review Agent는 Agentic RAG에서 무엇을 검증하는가?
A. Groundedness, Hallucination, Workflow 누락, 출력 형식, Common Mistakes를 검증한다.

Q. Agentic RAG Evaluation 항목은?
A. Query Planning Quality, Retrieval Precision, Context Relevance, Tool Calling Accuracy, Groundedness, Answer Completeness, Format Compliance이다.

Q. Agentic RAG 문서 분할은 어떻게 하는가?
A. Core, Query Planning, Retrieval Strategy, Tool Calling, State/Memory, Workflow, Evaluation, Troubleshooting으로 분리한다.

Q. Agentic RAG 문서에서 피해야 할 것은?
A. Workflow 없이 개념만 길게 설명하거나, Tool Calling, Validation, Re-Retrieval 기준을 누락하는 것이다.

Q. Agentic RAG Domain Rules는 어떤 Agent가 사용하는가?
A. PM Agent, AI/ML Agent, Backend Agent, DevOps Agent, Review Agent가 역할별로 사용한다.
