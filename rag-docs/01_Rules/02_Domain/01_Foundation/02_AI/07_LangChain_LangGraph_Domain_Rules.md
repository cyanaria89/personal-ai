# LangChain & LangGraph Domain Rules

---

# 1. Domain Purpose

LangChain & LangGraph Domain 문서는 AI Agent / RAG Agent / PM Agent / Review Agent용 RAG 문서 제작 규칙이다.

목적:

- LangChain 기본 개념 이해
- LangGraph 기본 개념 이해
- LLM Application 구성 요소 이해
- Prompt / Model / Parser / Retriever / Tool 연결 구조 설명
- Chain 기반 흐름과 Graph 기반 Workflow 차이 설명
- Agent State / Node / Edge / Conditional Routing 설계 지원
- RAG Pipeline 구현 기준 제공
- Tool Calling Agent 구현 기준 제공
- Multi-Agent Workflow 구현 기초 제공
- 개인 AI 개발팀 구현 기반 제공

우선순위:

1. Concept Clarity
2. Runnable Pipeline
3. State-based Workflow
4. RAG Integration
5. Tool Integration
6. Multi-Agent Foundation
7. Reliability / Debuggability

---

# 2. Scope

포함 범위:

- LangChain Core
- LangGraph Core
- LLM Application
- Prompt Template
- Chat Model
- Output Parser
- Runnable
- Chain
- Retriever
- Vector Store Retriever
- Document Loader
- Text Splitter
- Embedding Model
- RAG Chain
- Tool
- Tool Calling
- Agent
- State
- Node
- Edge
- Conditional Edge
- StateGraph
- Checkpoint
- Memory
- Router
- Human-in-the-loop
- Multi-Agent Workflow
- Review / Fix Loop
- Debugging / Tracing 기초

제외 범위:

- LangChain 내부 소스코드 분석
- LangGraph 고급 분산 실행
- LangSmith 운영 심화
- Production Agent Platform 운영
- MCP Protocol 심화
- Graph RAG 심화
- Agentic RAG 심화
- Fine-Tuning
- MLOps 상세

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

# 4. LangChain Core Rules

LangChain 문서는 LLM Application의 구성 요소를 연결하는 Framework로 설명한다.

반드시 포함:

- LangChain은 LLM, Prompt, Retriever, Tool, Parser를 연결하는 도구
- 단순 LLM 호출보다 재사용 가능한 Pipeline 구성이 목적
- Prompt Template으로 입력을 구조화
- Output Parser로 결과 형식을 안정화
- Retriever를 연결해 RAG 구성 가능
- Tool Calling과 Agent 구현에 활용 가능

기본 Flow:

```text
Input
→ Prompt Template
→ LLM
→ Output Parser
→ Output
```

RAG Flow:

```text
User Query
→ Retriever
→ Retrieved Documents
→ Prompt Template
→ LLM
→ Answer
```

금지:

- LangChain을 LLM 자체로 설명
- Chain만 만들면 Agent가 완성된다는 설명
- Prompt / Retriever / Parser 책임을 섞어 설명
- RAG 품질 문제를 LangChain 설정 문제로만 단정
- 최신 API 변화 가능성을 무시하고 특정 코드만 절대 규칙처럼 설명

---

# 5. LangGraph Core Rules

LangGraph 문서는 State 기반 Agent Workflow를 구성하는 도구로 설명한다.

반드시 포함:

- LangGraph는 Graph 구조로 Agent Workflow를 설계하는 도구
- Node는 작업 단위 또는 Agent
- Edge는 다음 단계 연결
- State는 Node 간 공유되는 데이터
- Conditional Edge는 상태에 따라 다음 Node를 선택
- Checkpoint는 중단/재개와 상태 추적에 사용
- Multi-Agent Workflow 구현에 적합

기본 Flow:

```text
State
→ Node Execution
→ State Update
→ Edge
→ Next Node
→ Final State
```

Multi-Agent Flow:

```text
User Request
→ PM Node
→ Domain Agent Node
→ Review Node
→ Fix Node
→ Final Node
```

금지:

- LangGraph를 단순 Chain 실행 도구로만 설명
- State 없이 Node만 나열하는 설명
- 종료 조건 없는 Graph 설계
- Conditional Routing 없이 모든 요청을 같은 흐름으로 보내는 설계
- Checkpoint / Error Handling을 생략하는 긴 Workflow 설계

---

# 6. LangChain vs LangGraph Rules

LangChain과 LangGraph의 차이를 반드시 설명한다.

비교:

| 구분      | LangChain                            | LangGraph                                |
| --------- | ------------------------------------ | ---------------------------------------- |
| 핵심 목적 | LLM 구성 요소 연결                   | State 기반 Workflow 구성                 |
| 구조      | Chain / Runnable 중심                | Graph / Node / Edge 중심                 |
| 적합      | RAG Chain, Tool Chain, 단순 Pipeline | Agent Workflow, Multi-Agent, Review Loop |
| 상태 관리 | 상대적으로 단순                      | State 중심                               |
| 흐름 제어 | 순차 흐름에 적합                     | 조건 분기 / 반복 / 중단에 적합           |

반드시 설명:

- LangChain은 LLM App 구성 요소를 만들기 좋음
- LangGraph는 Agent Workflow를 제어하기 좋음
- 둘은 경쟁 관계라기보다 함께 사용할 수 있음
- LangGraph Node 내부에서 LangChain Runnable이나 Chain을 사용할 수 있음

주의:

- 단순 RAG는 LangChain만으로 가능
- Review / Fix Loop, Multi-Agent, Human Approval이 있으면 LangGraph가 적합
- 프로젝트 복잡도에 맞게 선택

---

# 7. Runnable Rules

Runnable은 LangChain의 실행 가능한 구성 단위로 설명한다.

필수 포함:

- Runnable
- RunnableSequence
- invoke
- batch
- stream
- pipe
- input
- output

기본 Flow:

```text
Runnable A
→ Runnable B
→ Runnable C
→ Result
```

반드시 설명:

- Runnable은 입력을 받아 출력하는 실행 단위
- Prompt, Model, Parser 등을 Runnable로 연결 가능
- `invoke`는 단일 입력 실행
- `batch`는 여러 입력 처리
- `stream`은 Streaming 처리에 사용 가능

주의:

- Runnable의 입력/출력 타입을 명확히 해야 함
- 중간 결과 형식이 맞지 않으면 Chain이 깨짐
- 복잡한 Runnable 조합은 디버깅이 어려울 수 있음

---

# 8. Prompt Template Rules

Prompt Template은 입력 변수를 Prompt로 변환하는 구성 요소이다.

필수 포함:

- Prompt Template
- Chat Prompt Template
- System Message
- User Message
- Placeholder
- Variable
- Partial Variable
- Template Validation

예시 구조:

```text
System:
You are a Backend Agent.

Context:
{context}

User Question:
{question}
```

반드시 설명:

- Prompt Template은 반복되는 Prompt를 안정화
- 변수를 통해 동적 입력 주입
- System / User Message를 분리
- RAG에서는 retrieved context와 user question을 분리
- 누락 변수 검증 필요

주의:

- Context와 Question을 섞어 넣지 않기
- Placeholder 이름 불명확 금지
- 너무 많은 변수를 가진 Template은 유지보수 어려움
- 사용자 입력을 그대로 System Prompt로 넣지 않기

---

# 9. Chat Model Rules

Chat Model은 실제 LLM 호출 부분으로 설명한다.

필수 포함:

- Chat Model
- Model Provider
- Local LLM
- API LLM
- Temperature
- Max Tokens
- Streaming
- Timeout
- Retry

반드시 설명:

- Chat Model은 Prompt를 받아 답변을 생성
- Provider별 설정과 응답 구조가 다를 수 있음
- Local LLM과 API LLM을 구분
- 개발/리뷰/RAG 작업은 낮은 Temperature 권장
- Timeout과 Retry 정책 필요

주의:

- 모델명을 문서에 고정 절대 규칙으로 쓰지 않기
- Provider API 변경 가능성 고려
- 로컬 모델은 하드웨어 제약 고려
- 모델 응답은 검증 필요

---

# 10. Output Parser Rules

Output Parser는 LLM 응답을 원하는 형식으로 변환하거나 검증한다.

필수 포함:

- String Parser
- JSON Parser
- Pydantic Parser
- Structured Output
- Schema Validation
- Parse Error
- Retry on Parse Failure

기본 Flow:

```text
LLM Response
→ Output Parser
→ Structured Result
→ Validation
```

반드시 설명:

- Parser는 출력 형식을 안정화하는 데 사용
- JSON / Schema 기반 Workflow에 중요
- Agent 간 Handoff 결과를 구조화할 수 있음
- Parse 실패 처리 필요

주의:

- Parser가 내용 정확성을 보장하지는 않음
- LLM이 잘못된 JSON을 낼 수 있음
- Schema가 너무 복잡하면 실패 가능성 증가
- Parse 실패 시 재요청 또는 fallback 필요

---

# 11. Chain Rules

Chain은 여러 구성 요소를 순서대로 연결한 Pipeline이다.

필수 포함:

- Chain
- Sequential Chain
- Runnable Chain
- Input Mapping
- Output Mapping
- Reusable Pipeline

기본 Flow:

```text
Input
→ Prompt
→ Model
→ Parser
→ Output
```

반드시 설명:

- Chain은 정해진 순서의 작업에 적합
- 요약, 분류, RAG 답변 생성 같은 작업에 유용
- 입력과 출력 형식이 명확해야 재사용 가능
- 복잡한 조건 분기나 반복은 Graph가 더 적합

주의:

- Chain이 길어질수록 디버깅 어려움
- 각 단계의 입출력 형식 확인
- 오류 처리와 재시도 기준 필요

---

# 12. Document Loader Rules

Document Loader는 외부 문서를 읽어오는 구성 요소이다.

필수 포함:

- Document Loader
- File Loader
- Directory Loader
- Web Loader
- PDF Loader
- Markdown Loader
- Metadata
- Encoding

기본 Flow:

```text
File / Source
→ Loader
→ Document
→ Splitter
```

반드시 설명:

- Loader는 원본 문서를 Document 객체로 변환
- 파일명, 경로, source 같은 Metadata 유지가 중요
- Markdown 기반 RAG 문서는 Header 구조 보존 필요
- Encoding 문제 주의

주의:

- Loader가 문서 구조를 훼손할 수 있음
- PDF는 텍스트 추출 품질 확인 필요
- 코드블록과 표가 깨지는지 확인
- 민감 파일 적재 주의

---

# 13. Text Splitter Rules

Text Splitter는 문서를 Chunk로 나누는 구성 요소이다.

필수 포함:

- Text Splitter
- Recursive Character Splitter
- Markdown Header Splitter
- Chunk Size
- Chunk Overlap
- Semantic Boundary
- Code Block Preservation

기본 Flow:

```text
Document
→ Split by Header / Size
→ Chunk
→ Metadata Attach
```

반드시 설명:

- Splitter는 Retrieval 품질에 큰 영향
- Markdown 문서는 Header 기반 Split이 유용
- Chunk Size와 Overlap은 문서 성격에 맞게 조정
- Code Block 중간 분리 주의

주의:

- 무조건 문자 수 기준으로 자르면 의미가 깨질 수 있음
- 너무 작은 Chunk는 문맥 부족
- 너무 큰 Chunk는 검색 정밀도 저하
- Split 후 샘플 검색 검증 필요

---

# 14. Embedding Integration Rules

Embedding Integration은 문서를 Vector로 변환해 검색 가능하게 하는 단계이다.

필수 포함:

- Embedding Model
- Query Embedding
- Document Embedding
- Vector Dimension
- Local Embedding
- API Embedding
- Batch Embedding
- Re-embedding

기본 Flow:

```text
Chunks
→ Embedding Model
→ Vectors
→ Vector Store
```

반드시 설명:

- Embedding Model은 검색용 Vector 생성에 사용
- Chat Model과 역할이 다름
- Model 변경 시 기존 Vector 재생성 필요
- Batch 처리와 Rate Limit 고려
- 한국어 문서는 Multilingual Embedding 고려

주의:

- 서로 다른 Embedding Model Vector를 섞지 않기
- Dimension 불일치 주의
- 문서 수정 후 Re-embedding 필요
- Embedding 실패 Chunk 기록 필요

---

# 15. Vector Store Retriever Rules

Vector Store Retriever는 Vector DB에서 관련 문서를 검색하는 구성 요소이다.

필수 포함:

- Vector Store
- Retriever
- Similarity Search
- Top-K
- Similarity Threshold
- Metadata Filter
- Search Type
- Retrieved Documents

기본 Flow:

```text
User Query
→ Retriever
→ Relevant Documents
→ RAG Prompt
```

반드시 설명:

- Retriever는 RAG의 검색 단계
- Top-K와 Threshold는 Context 품질에 영향
- Metadata Filter로 Domain 범위 제한 가능
- 검색 결과는 LLM에 넣기 전 정리 필요

주의:

- Retriever 결과가 항상 정답은 아님
- 관련 없는 문서가 섞일 수 있음
- 검색 결과가 없을 때 fallback 필요
- RAG 답변은 Retrieved Context 기반이어야 함

---

# 16. RAG Chain Rules

RAG Chain은 Retriever와 LLM을 연결해 문서 기반 답변을 생성한다.

필수 포함:

- User Query
- Retriever
- Retrieved Context
- Prompt Template
- LLM
- Output Parser
- Grounded Answer
- Source

기본 Flow:

```text
Question
→ Retrieve Documents
→ Format Context
→ Prompt
→ LLM
→ Parse Answer
→ Return Answer with Source
```

반드시 설명:

- RAG Chain은 검색과 생성을 연결
- Context Formatting이 중요
- 문서에 없는 내용은 없다고 답해야 함
- Source를 함께 반환하면 검증 가능
- 검색 실패와 생성 실패를 구분

주의:

- Retrieved Context를 과도하게 넣지 말 것
- Source 없는 답변은 검증 어려움
- LLM이 문서에 없는 내용을 보완하지 않도록 Prompt 필요
- Chunk 품질이 낮으면 Chain 구조가 좋아도 실패 가능

---

# 17. Tool Rules

Tool은 Agent가 외부 기능을 사용할 수 있게 하는 구성 요소이다.

필수 포함:

- Tool
- Tool Name
- Description
- Args Schema
- Tool Result
- Tool Error
- Tool Permission

예시 Tool:

```text
search_rag_documents(query, top_k)
read_file(path)
run_test(command)
call_api(endpoint, payload)
```

반드시 설명:

- Tool은 검색, 파일 처리, API 호출, 테스트 실행 등에 사용
- Tool 설명은 모델이 언제 사용할지 알 수 있게 작성
- Args Schema를 명확히 정의
- Tool 실행 전 입력값 검증 필요
- 위험 Tool은 승인 필요

주의:

- LLM이 생성한 Tool Arguments를 신뢰하지 않기
- Tool 결과가 실패일 수 있음
- Tool이 너무 많으면 선택 품질 저하
- Side Effect가 큰 Tool은 Human Confirmation 필요

---

# 18. Agent Rules

LangChain/LangGraph 문서에서 Agent는 LLM이 Tool과 상태를 활용해 목표를 수행하는 구성으로 설명한다.

필수 포함:

- Agent
- Tool Use
- Reasoning
- State
- Memory
- Prompt
- Stop Condition
- Error Handling

Agent Flow:

```text
User Task
→ Agent Prompt
→ Tool Selection
→ Tool Execution
→ Observation
→ Final Answer
```

반드시 설명:

- Agent는 LLM 호출 + Tool 사용 + 상태 관리의 조합
- Agent가 모든 일을 자동으로 해도 되는 것은 아님
- Tool 권한과 Stop Condition 필요
- RAG 기반 Agent는 검색 문서를 우선 사용해야 함

주의:

- 무한 Tool Loop 방지
- 위험 Tool 자동 실행 금지
- Agent Output 검증 필요
- Tool 실패 시 fallback 필요

---

# 19. LangGraph State Rules

LangGraph State는 Node 간 공유되는 데이터 구조이다.

필수 포함:

- State
- State Schema
- TypedDict / Pydantic
- Current Step
- Messages
- Requirements
- Retrieved Context
- Agent Output
- Review Findings
- Status

예시:

```python
from typing import TypedDict

class AgentState(TypedDict):
    user_request: str
    current_step: str
    requirements: list[str]
    agent_outputs: dict
    review_findings: list[str]
    status: str
```

반드시 설명:

- State Schema를 정의하면 Workflow 안정성이 높아짐
- 각 Node는 State를 읽고 일부를 업데이트
- 중간 결과와 결정 사항을 State에 저장
- Review / Fix Loop에서 State가 핵심

주의:

- State가 너무 커지면 Context 관리 어려움
- 모든 임시 정보를 State에 저장하지 않기
- State Update 규칙 필요
- 최신 사용자 요청이 오래된 State보다 우선

---

# 20. Node Rules

Node는 LangGraph에서 하나의 작업 단위이다.

필수 포함:

- Node
- Function Node
- Agent Node
- Tool Node
- Review Node
- Input State
- Output State Update

기본 Flow:

```text
State Input
→ Node Function
→ State Update
```

Node 예시:

```text
PM Node
Backend Agent Node
RAG Search Node
Review Node
Fix Node
Final Node
```

반드시 설명:

- Node는 State를 입력받아 작업을 수행
- Node는 전체 State가 아니라 변경할 부분만 반환할 수 있음
- Agent 하나를 Node로 만들 수 있음
- Tool 실행도 Node로 구성 가능

주의:

- Node 책임을 너무 크게 만들지 않기
- Node 간 입출력 형식 불일치 주의
- 실패 시 State에 error를 기록
- Side Effect 있는 Node는 승인/검증 필요

---

# 21. Edge Rules

Edge는 Node 간 실행 순서를 정의한다.

필수 포함:

- Edge
- Start
- End
- Normal Edge
- Conditional Edge
- Loop
- Stop Condition

기본 Flow:

```text
START
→ PM Node
→ Backend Node
→ Review Node
→ END
```

반드시 설명:

- Edge는 다음에 실행할 Node를 결정
- 단순 Edge는 항상 같은 다음 Node로 이동
- Conditional Edge는 State에 따라 다음 Node 선택
- Loop는 Review / Fix 같은 반복에 사용 가능
- 종료 조건이 반드시 필요

주의:

- 종료 조건 없는 Loop 금지
- Conditional Edge 조건이 모호하면 잘못 라우팅됨
- 실패 상태를 처리하는 Edge 필요

---

# 22. Conditional Routing Rules

Conditional Routing은 State를 기준으로 다음 Node를 선택한다.

필수 포함:

- Router Function
- Condition
- State Field
- Next Node
- Fallback
- Confidence

예시:

```text
if task_type == "backend":
    → Backend Agent
elif task_type == "frontend":
    → Frontend Agent
else:
    → PM Clarification
```

반드시 설명:

- PM Agent / Router Node가 Routing을 담당할 수 있음
- task_type, status, review_result 같은 State 값으로 분기
- 불확실하면 clarification 또는 fallback으로 이동
- 복합 작업은 여러 Node 순서로 분해 가능

주의:

- 문자열 비교만으로 복잡한 의도 판단 주의
- Routing 기준을 명확히 정의
- fallback이 없으면 Workflow가 중단될 수 있음

---

# 23. Checkpoint Rules

Checkpoint는 Workflow 중간 상태 저장에 사용한다.

필수 포함:

- Checkpoint
- Thread ID
- State Snapshot
- Resume
- Interrupt
- Human-in-the-loop
- Persistence

기본 Flow:

```text
Node Execution
→ State Update
→ Save Checkpoint
→ Resume Later if Needed
```

반드시 설명:

- Checkpoint는 긴 Agent Workflow에서 중요
- 중단 후 재개 가능
- Human Approval 대기 상태 저장 가능
- 실패 복구에 도움

주의:

- 민감정보가 Checkpoint에 저장되지 않도록 주의
- 오래된 Checkpoint 재개 전 최신성 확인
- Checkpoint 저장소 관리 필요

---

# 24. Memory Rules

LangChain / LangGraph 문서에서 Memory는 State와 구분해서 설명한다.

필수 포함:

- Conversation Memory
- Long-term Memory
- State
- Checkpoint
- Summary Memory
- Retrieval Memory

반드시 설명:

- State는 현재 Workflow의 실행 상태
- Memory는 과거 정보를 재사용하기 위한 구조
- 대화 전체를 무조건 Memory에 넣지 않음
- Summary와 Retrieval을 조합해 Context 관리 가능

주의:

- 오래된 Memory 검증 필요
- 민감정보 저장 금지
- 현재 요청과 Memory 충돌 시 현재 요청 우선
- State와 Memory를 혼동하지 않기

---

# 25. Human-in-the-loop Rules

Human-in-the-loop는 LangGraph Workflow에서 중요한 패턴이다.

필수 포함:

- Interrupt
- Approval
- Clarification
- Review
- Resume
- Dangerous Action
- User Decision

Flow:

```text
Agent Proposes Action
→ Interrupt
→ User Approval
→ Resume Workflow
```

반드시 설명:

- 위험 작업 전 사용자 확인 필요
- 정보가 부족하면 사용자에게 질문
- 승인 대기 상태는 Checkpoint와 연결 가능
- 사용자의 결정이 State에 반영되어야 함

주의:

- 사용자 승인 없이 파일 삭제 / DB 변경 / 배포 실행 금지
- 승인 범위를 넘어서는 작업 금지
- 대기 상태에서 State 손실 주의

---

# 26. Review / Fix Graph Rules

Review / Fix Loop는 LangGraph에 적합한 패턴이다.

필수 포함:

- Draft Node
- Review Node
- Fix Node
- Re-review
- Pass / Fail
- Max Iteration
- Stop Condition

Flow:

```text
Draft Node
→ Review Node
→ if pass: Final Node
→ if fail: Fix Node
→ Review Node
```

반드시 설명:

- Review 결과에 따라 Final 또는 Fix로 분기
- Fix 후 재검토 가능
- 반복 횟수 제한 필요
- Minor Issue와 Critical Issue 구분 가능

주의:

- 무한 반복 방지
- Review 기준 고정
- Fix가 새 문제를 만들 수 있으므로 재검토 필요
- Max Iteration 도달 시 사용자에게 상태 보고

---

# 27. Multi-Agent Graph Rules

Multi-Agent Workflow는 Node별 Agent로 구성할 수 있다.

필수 포함:

- PM Node
- SQL Node
- Backend Node
- Frontend Node
- DevOps Node
- AI Node
- Review Node
- Final Node

기본 구조:

```text
START
→ PM Node
→ SQL Node
→ Backend Node
→ Frontend Node
→ Review Node
→ Final Node
→ END
```

조건부 구조:

```text
PM Node
→ route by task type
→ Domain Agent Node
→ Review Node
→ Final Node
```

반드시 설명:

- Agent 하나를 Node로 표현 가능
- PM Node가 Routing과 Task Decomposition 담당
- Domain Node는 전문 작업 담당
- Review Node는 검증 담당
- Final Node는 사용자용 응답 정리

주의:

- 모든 요청을 모든 Agent에 보내지 않기
- Agent 결과 통합 기준 필요
- Cross-domain Consistency 검토 필요
- 초기에는 순차 실행 권장

---

# 28. Error Handling Rules

LangChain / LangGraph Workflow는 오류 처리를 포함해야 한다.

필수 포함:

- LLM Error
- Parser Error
- Tool Error
- Retrieval Error
- Timeout
- Invalid State
- Retry
- Fallback
- Error Node

기본 Flow:

```text
Node Error
→ Record Error in State
→ Retry if Possible
→ Fallback Node
→ Human Clarification or Stop
```

반드시 설명:

- Node 실패는 State에 기록
- 재시도 가능한 오류와 불가능한 오류 구분
- Parser Error는 재생성 가능
- Tool Error는 실패 결과를 다음 Node에 전달 가능
- 복구 불가 상태는 사용자에게 보고

주의:

- 예외를 숨기지 않기
- 실패한 Node 결과를 성공처럼 전달 금지
- 무제한 Retry 금지
- Error Handling 없는 Graph는 운영 불안정

---

# 29. Streaming Rules

Streaming은 사용자 경험 개선에 사용할 수 있다.

필수 포함:

- Streaming
- Token Stream
- Runnable Stream
- Partial Output
- Final Output
- UI Integration

반드시 설명:

- Streaming은 긴 답변의 체감 속도를 개선
- 중간 출력은 불완전할 수 있음
- 최종 결과 조립이 필요
- Agent Workflow에서는 중간 단계와 최종 답변을 구분

주의:

- JSON Structured Output은 Streaming 파싱이 어려울 수 있음
- 중간 출력이 최종 결정처럼 보이지 않게 주의
- Error 발생 시 부분 출력 처리 필요

---

# 30. Debugging / Tracing Rules

LangChain / LangGraph 문서에는 디버깅 기준을 포함한다.

필수 포함:

- Intermediate Step
- State Snapshot
- Node Input
- Node Output
- Tool Call Log
- Retrieved Context
- Prompt Log
- Parser Error
- Trace

반드시 설명:

- Agent Workflow는 중간 단계 확인이 중요
- 어느 Node에서 실패했는지 추적
- Prompt와 Retrieved Context를 확인
- Tool Call Arguments와 Result 확인
- State 변화 추적

주의:

- API Key / Secret 로그 출력 금지
- Prompt 전체 저장은 보안 고려
- 개인정보 포함 가능성 확인
- 로그가 너무 많으면 분석 어려움

---

# 31. Testing Rules

LangChain / LangGraph 문서에는 테스트 기준을 포함한다.

필수 포함:

- Prompt Test
- Chain Test
- Retriever Test
- Parser Test
- Tool Test
- Node Test
- Graph Test
- Golden Query Test

테스트 대상:

```text
Prompt Template
Retriever
Output Parser
Tool Function
Node Function
Conditional Router
Review-Fix Loop
```

반드시 설명:

- LLM 호출 없이 테스트 가능한 부분을 분리
- Retriever는 Golden Query로 테스트
- Parser는 잘못된 JSON 케이스 테스트
- Tool은 Mocking 가능
- Graph는 State 전이를 테스트

주의:

- 테스트마다 실제 LLM API 호출 금지
- 비결정적 출력에 대한 테스트 기준 설계
- 위험 Tool은 dry-run 또는 mock 사용
- 비용 발생 테스트 제한

---

# 32. Personal AI Project Rules

개인 AI 프로젝트 기준을 포함할 수 있다.

현재 목표 구조:

```text
User
→ PM Agent
→ SQL Agent
→ Backend Agent
→ Frontend Agent
→ Review Agent
→ Fix Agent
→ Final Output
```

LangGraph 표현:

```text
START
→ PM Node
→ SQL Node
→ Backend Node
→ Frontend Node
→ Review Node
→ Fix Node if needed
→ Final Node
→ END
```

반드시 설명:

- 초기에는 순차 실행 Graph 권장
- PM Node가 요청 분석과 라우팅 담당
- Domain Agent Node는 RAG 문서를 참조
- Review Node가 품질 검증
- Fix Node는 Review 결과 반영
- 로컬 LLM 환경에서는 병렬보다 순차가 현실적

주의:

- 처음부터 모든 Agent를 구현하지 않기
- 단일 Node가 너무 많은 책임을 갖지 않기
- State Schema를 단순하게 시작
- Tool 권한을 최소화

---

# 33. Troubleshooting Rules

반드시 포함 추천.

형식:

```md
문제:

원인:

해결:
```

---

## Chain 입력 형식이 맞지 않음

문제:

- Prompt / Model / Parser 연결 중 오류 발생

원인:

- 이전 Runnable 출력과 다음 Runnable 입력 불일치
- Template 변수 누락
- Parser가 예상한 형식과 실제 출력 불일치

해결:

- 각 Runnable의 input / output 확인
- Prompt Template 변수 검증
- Parser Schema 단순화
- 중간 출력 로그 확인

---

## Retriever가 관련 문서를 못 찾음

문제:

- RAG Chain이 엉뚱한 Context로 답변함

원인:

- Chunk 품질 낮음
- Query 표현과 문서 표현 불일치
- Top-K / Threshold 부적절
- Metadata Filter 과도함

해결:

- Golden Query로 Retriever 테스트
- Chunk 제목 / FAQ / Retrieval Queries 보강
- Query Rewrite 적용
- Metadata Filter 조정

---

## Graph가 무한 반복됨

문제:

- Review / Fix Loop가 끝나지 않음

원인:

- Stop Condition 없음
- Max Iteration 없음
- Review 기준이 계속 바뀜
- Conditional Edge 조건 오류

해결:

- Max Iteration 추가
- pass / fail 조건 명확화
- Severity 기준 설정
- Router 조건 테스트

---

## State가 너무 커짐

문제:

- Node 실행마다 Context가 길어지고 응답 품질이 저하됨

원인:

- 모든 중간 결과를 State에 저장
- Retrieved Context를 계속 누적
- Tool Result 전체 저장

해결:

- State Compression 적용
- 필요한 필드만 유지
- 완료된 단계 요약
- Tool Result는 요약 또는 참조만 저장

---

## Tool 호출이 실패함

문제:

- Agent가 Tool을 호출했지만 실행 실패

원인:

- Arguments Schema 불일치
- Permission 부족
- Timeout
- 외부 API 오류
- Tool Result 처리 누락

해결:

- Tool Arguments 검증
- Error Result 구조화
- Retry 가능 여부 구분
- 실패 시 fallback Node로 이동

---

## Checkpoint 재개 후 결과가 이상함

문제:

- Resume 후 오래된 상태 기준으로 진행됨

원인:

- Checkpoint가 오래됨
- 현재 사용자 요구와 State 충돌
- 완료된 단계와 pending 단계 구분 실패

해결:

- Resume 전 State Validation
- 현재 요청과 충돌 확인
- 완료/남은 작업 구분
- 필요 시 사용자 확인

---

# 34. Best Practice Rules

Best Practice:

- 단순 Pipeline은 LangChain Chain으로 시작
- 복잡한 Agent Workflow는 LangGraph로 설계
- Prompt / Model / Parser 책임을 분리
- RAG Chain은 Retriever 품질을 먼저 검증
- State Schema를 단순하게 정의
- Node는 하나의 책임만 갖게 설계
- Conditional Edge에는 fallback을 둠
- Review / Fix Loop에는 Max Iteration 설정
- Tool Arguments는 실행 전 검증
- Checkpoint로 긴 Workflow 복구 가능하게 설계
- Human Approval이 필요한 Node를 분리
- Debugging을 위해 Node input/output을 추적
- 민감정보는 로그와 State에 저장하지 않음

---

# 35. Comparison Rules

LangChain & LangGraph 문서는 비교 기준을 포함한다.

필수 비교 대상:

- LangChain vs LangGraph
- Chain vs Graph
- Runnable vs Node
- Prompt Template vs System Prompt
- Output Parser vs Structured Output Prompt
- Retriever vs Vector Store
- State vs Memory
- Edge vs Conditional Edge
- Single Agent Graph vs Multi-Agent Graph
- Sequential Graph vs Conditional Graph

예시:

| 비교 | Chain                 | Graph                                    |
| ---- | --------------------- | ---------------------------------------- |
| 구조 | 순차 Pipeline         | Node / Edge Workflow                     |
| 상태 | 단순 입력/출력 중심   | State 중심                               |
| 분기 | 제한적                | 조건 분기 가능                           |
| 적합 | RAG Chain, 요약, 변환 | Agent Workflow, Multi-Agent, Review Loop |

---

# 36. Checklist Rules

LangChain & LangGraph 문서에는 Checklist를 포함할 수 있다.

예시:

```md
### [Checklist]

- [ ] Prompt Template의 입력 변수가 명확한가?
- [ ] Model 설정 기준이 있는가?
- [ ] Output Parser가 필요한가?
- [ ] Retriever 품질을 테스트했는가?
- [ ] RAG Chain에 Grounding Rule이 있는가?
- [ ] State Schema가 정의되어 있는가?
- [ ] Node 책임이 분리되어 있는가?
- [ ] Conditional Edge에 fallback이 있는가?
- [ ] Review / Fix Loop에 Max Iteration이 있는가?
- [ ] Tool Arguments를 검증하는가?
- [ ] Checkpoint / Resume 기준이 있는가?
- [ ] 민감정보가 로그나 State에 저장되지 않는가?
```

---

# 37. Retrieval Optimization Rules

강조 대상 키워드:

- LangChain
- LangGraph
- LLM Application
- Runnable
- Chain
- Prompt Template
- Chat Prompt Template
- Chat Model
- Output Parser
- Structured Output
- Document Loader
- Text Splitter
- Embedding
- Vector Store Retriever
- RAG Chain
- Tool
- Tool Calling
- Agent
- StateGraph
- State
- Node
- Edge
- Conditional Edge
- Checkpoint
- Memory
- Human-in-the-loop
- Review-Fix Loop
- Multi-Agent Graph
- Workflow Debugging
- Graph Testing

키워드 반복 허용.

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

예:

- LangChain이 뭐야?
- LangGraph가 뭐야?
- LangChain과 LangGraph 차이는?
- Runnable이 뭐야?
- Chain은 언제 써?
- Graph는 언제 써?
- State는 어떻게 설계해?
- Node와 Edge는 뭐야?
- Conditional Edge는 언제 써?
- LangGraph로 Multi-Agent를 어떻게 만들어?
- RAG Chain은 어떻게 구성해?
- Review-Fix Loop는 어떻게 만들어?
- Checkpoint는 왜 필요해?

---

# 38. Version Rules

기준:

- Modern LangChain
- Modern LangGraph
- Runnable 기반 LangChain 구조
- StateGraph 기반 LangGraph 구조
- RAG Chain
- Tool Calling Agent
- Multi-Agent Workflow
- Checkpoint / Human-in-the-loop 가능 구조
- Python 3.11+
- Local LLM / API LLM 연동 가능 구조
- 개인 AI 서버 Agent 구현 기준

Legacy 제외:

- 오래된 Chain API만 중심으로 설명
- State 없는 Agent Loop
- Tool Arguments 검증 없는 Agent
- 종료 조건 없는 Graph
- Memory와 State를 혼동하는 구조
- RAG 검색 품질 평가 없는 Chain

---

# 39. Common Mistakes

자주 발생:

- LangChain과 LangGraph 역할을 혼동
- 단순 Chain으로 복잡한 Agent Workflow를 억지 구현
- State Schema 없이 Graph 작성
- Node 책임이 너무 큼
- Conditional Edge에 fallback 없음
- Review-Fix Loop에 종료 조건 없음
- Retriever 품질 확인 없이 RAG Chain 구성
- Parser 실패 처리 없음
- Tool Arguments 검증 없음
- Checkpoint 없이 긴 Workflow 실행
- State에 모든 중간 결과를 저장해 비대해짐
- 민감정보를 로그에 남김
- 최신 API 변화 가능성을 고려하지 않고 코드만 외움

---

# 40. Final Goal

LangChain & LangGraph RAG 문서는 Agent가 아래를 수행 가능해야 한다.

- LangChain 기본 개념 설명
- LangGraph 기본 개념 설명
- LangChain과 LangGraph 역할 구분
- Prompt / Model / Parser / Retriever 연결 구조 설명
- RAG Chain 설계
- Tool Calling Agent 설계
- StateGraph 구조 설계
- State Schema 제안
- Node / Edge / Conditional Edge 설계
- Checkpoint / Resume 기준 설명
- Human-in-the-loop 적용 여부 판단
- Review / Fix Loop 설계
- Multi-Agent Graph 설계
- Workflow Debugging 기준 제안
- LangChain / LangGraph 문제 Troubleshooting
- 개인 AI 개발팀 구현 방향 제안

문서 품질이 Agent Workflow 구현 가능성과 유지보수성을 결정한다.

---

# Retrieval Queries

### [FAQ]

Q. LangChain이 뭐야?

A.
LLM, Prompt, Retriever, Tool, Output Parser 같은 구성 요소를 연결해 LLM Application을 만들기 쉽게 해주는 Framework다.

Q. LangGraph가 뭐야?

A.
State, Node, Edge 기반으로 Agent Workflow와 Multi-Agent Workflow를 설계하는 Framework다.

Q. LangChain과 LangGraph 차이는?

A.
LangChain은 LLM 구성 요소를 연결하는 Chain / Runnable 중심이고, LangGraph는 State 기반 Workflow와 조건 분기, 반복, Checkpoint에 강하다.

Q. LangChain과 LangGraph는 같이 써?

A.
같이 쓸 수 있다. LangGraph Node 내부에서 LangChain Runnable, RAG Chain, Tool Chain을 실행할 수 있다.

Q. Runnable이 뭐야?

A.
입력을 받아 출력을 만드는 LangChain의 실행 가능한 구성 단위다.

Q. Chain은 언제 써?

A.
요약, 분류, RAG 답변 생성처럼 순차적인 Pipeline이 필요한 작업에 사용한다.

Q. Graph는 언제 써?

A.
조건 분기, Review-Fix Loop, Multi-Agent, Human Approval, Checkpoint가 필요한 복잡한 Workflow에 사용한다.

Q. Prompt Template은 왜 필요해?

A.
반복되는 Prompt 구조를 안정화하고 입력 변수를 명확히 주입하기 위해 필요하다.

Q. Output Parser는 왜 필요해?

A.
LLM 응답을 JSON, 문자열, Schema 기반 결과로 변환하고 검증하기 위해 필요하다.

Q. RAG Chain은 어떻게 구성해?

A.
User Query를 Retriever로 검색하고, Retrieved Context를 Prompt에 넣어 LLM이 답변하도록 구성한다.

Q. Retriever가 중요한 이유는?

A.
Retriever가 잘못된 문서를 가져오면 LLM 답변도 부정확해지기 때문이다.

Q. LangGraph State는 뭐야?

A.
Graph의 Node들이 읽고 업데이트하는 공유 데이터 구조다.

Q. State Schema는 왜 필요해?

A.
Node 간 입력과 출력 형식을 안정화하고 Agent 간 상태 충돌을 줄이기 위해 필요하다.

Q. Node는 뭐야?

A.
LangGraph에서 하나의 작업 단위다. Agent, Tool 실행, Review, Fix 같은 작업을 Node로 표현할 수 있다.

Q. Edge는 뭐야?

A.
Node 다음에 어떤 Node를 실행할지 연결하는 흐름이다.

Q. Conditional Edge는 언제 써?

A.
State 값에 따라 Backend Agent, Frontend Agent, Review Agent처럼 다음 단계를 다르게 선택할 때 사용한다.

Q. Checkpoint는 왜 필요해?

A.
긴 Workflow를 중간 저장하고 실패나 사용자 승인 대기 후 이어서 실행하기 위해 필요하다.

Q. Human-in-the-loop는 어떻게 연결해?

A.
위험 작업이나 정보 부족 상황에서 Workflow를 중단하고 사용자 승인 또는 답변을 받은 뒤 Checkpoint에서 재개한다.

Q. Review-Fix Loop는 어떻게 만들어?

A.
Draft Node 이후 Review Node가 pass/fail을 판단하고, fail이면 Fix Node로 보내고 다시 Review Node로 돌아오게 만든다.

Q. LangGraph로 개인 AI 개발팀을 만들 수 있어?

A.
가능하다. PM Node, SQL Node, Backend Node, Frontend Node, Review Node, Fix Node, Final Node를 StateGraph로 구성할 수 있다.

Q. 처음부터 LangGraph를 써야 해?

A.
단순 RAG나 요약은 LangChain만으로도 충분하다. Multi-Agent나 Review-Fix Loop가 필요해질 때 LangGraph를 쓰는 것이 자연스럽다.

Q. LangChain & LangGraph 문서의 최종 목표는 뭐야?

A.
Agent가 LLM 구성 요소와 State 기반 Workflow를 이해하고, RAG / Tool / Multi-Agent 시스템을 구현할 수 있게 만드는 것이다.
