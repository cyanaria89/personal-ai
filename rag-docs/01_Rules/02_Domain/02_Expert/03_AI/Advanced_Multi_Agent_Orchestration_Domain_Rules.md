# Advanced Multi-Agent Orchestration Domain Rules

---

# 1. Domain Purpose

## 1.1 Advanced Multi-Agent Orchestration 문서 목적

### [개념]

Advanced Multi-Agent Orchestration Domain 문서는 PM Agent / Backend Agent / Frontend Agent / DevOps Agent / AI/ML Agent / Review Agent / Architecture Review Agent가 복수 Agent 기반 시스템을 설계, 실행, 검토, 개선할 때 참조하는 RAG 제작 규칙 문서이다.

Advanced Multi-Agent Orchestration은 여러 Agent가 독립적으로 동작하는 구조가 아니라, 목표 분석, 작업 분해, 역할 분배, 상태 공유, 결과 통합, 검증, 재시도, 오류 복구를 조율하는 구조이다.

Multi-Agent System의 품질은 개별 Agent 성능보다 Orchestration 품질에 크게 의존한다.

---

### [핵심]

- Advanced Multi-Agent Orchestration = Task Planning + Agent Routing + State Management + Coordination + Validation
- PM Agent 중심 Workflow 설계 필요
- Specialist Agent 역할 분리 필요
- Review Agent 검증 단계 필요
- Agent 간 Input / Output Contract 필요
- Shared State와 Private State 구분 필요
- Agent Routing 기준 필요
- Failure Handling 기준 필요
- Human-in-the-Loop 기준 필요
- Agentic RAG / Graph RAG / Tool Calling과 연결 가능
- 최종 출력은 통합 결과 중심

---

### [실무]

2026 실무 기준 Advanced Multi-Agent Orchestration 문서는 다음 목적을 우선한다.

- Multi-Agent Workflow 설계
- PM Agent Routing 기준 제공
- Specialist Agent 역할 정의
- Agent 간 데이터 전달 규칙 제공
- Shared State 관리 기준 제공
- Agent Output Contract 정의
- Review / Validation Flow 제공
- Retry / Fallback 기준 제공
- Human Review 기준 제공
- Agent Evaluation 기준 제공
- Orchestration Troubleshooting 제공

이 문서는 사람이 Multi-Agent 개념을 공부하기 위한 문서가 아니라, Agent가 복합 작업을 안정적으로 분배하고 수행하기 위한 운영 기준 문서로 작성한다.

---

### [FAQ]

Q. Advanced Multi-Agent Orchestration 문서는 무엇을 위한 문서인가?

A. 여러 Agent가 역할을 나누어 작업하고, 결과를 통합하고, 검증할 수 있도록 Workflow와 실행 기준을 제공하는 문서이다.

Q. Multi-Agent Orchestration은 단순히 Agent를 여러 개 만드는 것인가?

A. 아니다. 작업 분해, Agent Routing, State 공유, 검증, 오류 복구, 결과 통합을 포함하는 조율 구조이다.

Q. Advanced Multi-Agent Orchestration의 핵심 Agent는?

A. PM Agent, Specialist Agent, Review Agent, Architecture Review Agent가 핵심이다.

---

# 2. Scope

## 2.1 포함 범위

### [개념]

Advanced Multi-Agent Orchestration Domain 문서는 복수 Agent가 협력하여 복잡한 작업을 수행하기 위한 구조, 역할, 상태, 메시지, 검증, 오류 처리 기준을 포함한다.

---

### [핵심]

포함 범위:

- Multi-Agent System
- Agent Orchestration
- PM Agent
- Specialist Agent
- Review Agent
- Agent Routing
- Task Decomposition
- Workflow Planning
- Role Definition
- Agent Input Contract
- Agent Output Contract
- Shared State
- Private State
- Message Passing
- Tool Coordination
- RAG Coordination
- Parallel Execution
- Sequential Execution
- Consensus Pattern
- Critic Pattern
- Retry / Fallback
- Human-in-the-Loop
- Evaluation
- Observability
- Troubleshooting

제외 범위:

- LLM 내부 구조 상세
- 단일 Agent Prompt 작성법 전체
- LangGraph 전체 API 문서 복붙
- AutoGen 전체 API 문서 복붙
- CrewAI 전체 API 문서 복붙
- 특정 프레임워크 종속 구현만 작성
- Kubernetes 운영 상세
- Vector DB 상세 튜닝
- 일반 조직론식 역할 설명

---

### [실무]

Advanced Multi-Agent Orchestration 문서는 아래 질문에 답할 수 있어야 한다.

- 어떤 요청을 Multi-Agent로 처리해야 하는가?
- PM Agent는 작업을 어떻게 분해해야 하는가?
- 어떤 Specialist Agent에게 작업을 보내야 하는가?
- Agent 간 전달 데이터는 어떤 형식이어야 하는가?
- Shared State에는 무엇을 저장해야 하는가?
- Agent 결과를 어떻게 통합해야 하는가?
- Review Agent는 무엇을 검증해야 하는가?
- Agent 실패 시 어떻게 재시도하거나 대체해야 하는가?
- Human Review가 필요한 상황은 언제인가?
- Orchestration 품질은 어떻게 평가해야 하는가?

---

### [FAQ]

Q. Multi-Agent 문서에 프레임워크 코드를 많이 넣어야 하는가?

A. 아니다. Domain Rules에서는 프레임워크보다 Workflow, Role, State, Contract, Validation 기준을 우선한다.

Q. 모든 요청을 Multi-Agent로 처리해야 하는가?

A. 아니다. 단순 질문은 단일 Agent로 충분하며, 복합 작업이나 검증이 필요한 작업에서 Multi-Agent를 사용한다.

Q. Orchestration 문서는 Agentic RAG와 중복되는가?

A. 일부 연결되지만, Agentic RAG는 검색과 도구 사용 중심이고 Orchestration은 Agent 간 작업 조율 중심이다.

---

# 3. Section Priority

## 3.1 필수 섹션 규칙

### [개념]

Advanced Multi-Agent Orchestration 문서는 모든 주요 Chunk에 `[개념]`, `[핵심]`, `[실무]`, `[FAQ]`를 우선 적용한다.

복잡한 Agent 흐름은 `[Flow]`를 추가한다.

역할 비교가 필요한 주제는 `[Comparison]`을 추가한다.

검증이 필요한 주제는 `[Checklist]`, `[Review Point]`, `[Evaluation]`을 추가한다.

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

- [Agent Contract]
- [State Schema]
- [Routing Rule]
- [Review Point]
- [Evaluation]
- [Anti-Pattern]

---

### [실무]

Advanced Multi-Agent Orchestration 문서는 단순 설명보다 실행 규칙을 우선한다.

각 문서는 아래 정보 중 최소 2개 이상을 포함한다.

- Agent Role 정의
- Workflow Flow
- Input / Output Contract
- Shared State 기준
- Routing Rule
- Validation Checklist
- Retry / Fallback 기준
- Human Review 기준
- Evaluation 기준

---

### [FAQ]

Q. Multi-Agent Orchestration 문서에 Flow는 필수인가?

A. PM Agent Routing, Agent Collaboration, Review Workflow, Retry Workflow 주제에서는 필수이다.

Q. Agent Contract 섹션은 왜 필요한가?

A. Agent 간 전달 데이터가 불명확하면 결과 통합과 검증이 실패하기 때문이다.

Q. Checklist는 어떤 Agent가 사용하는가?

A. Review Agent, PM Agent, Architecture Review Agent가 검증 기준으로 사용한다.

---

# 4. Core Concept Rules

## 4.1 Multi-Agent Orchestration 핵심 개념 작성 규칙

### [개념]

Advanced Multi-Agent Orchestration 핵심 개념은 단순한 다중 Agent 호출과 구분되도록 작성한다.

Multi-Agent Orchestration은 복수 Agent의 역할, 실행 순서, 데이터 전달, 검증, 실패 처리, 결과 통합을 설계하는 구조이다.

---

### [핵심]

반드시 포함할 개념:

- Multi-Agent System
- Agent Orchestration
- PM Agent
- Specialist Agent
- Review Agent
- Architecture Review Agent
- Task Decomposition
- Agent Routing
- Workflow Planning
- Shared State
- Private State
- Agent Contract
- Message Passing
- Sequential Execution
- Parallel Execution
- Consensus
- Critic
- Retry
- Fallback
- Human-in-the-Loop
- Evaluation
- Observability

용어 통일:

- Multi-Agent Orchestration
- PM Agent
- Specialist Agent
- Review Agent
- Agent Routing
- Task Decomposition
- Shared State
- Private State
- Agent Contract
- Final Output
- Human-in-the-Loop

---

### [실무]

Multi-Agent Orchestration 설명은 아래 구조를 기준으로 작성한다.

```text
User Request
→ PM Agent
→ Goal Analysis
→ Task Decomposition
→ Agent Routing
→ Specialist Agent Execution
→ Result Aggregation
→ Review Agent Validation
→ Fix Request
→ Final Output
```

Orchestration 문서는 “여러 Agent가 협력한다” 수준에서 멈추면 안 된다.

Agent가 어떤 기준으로 작업을 나누고, 어떤 Agent에게 보내고, 어떤 상태를 공유하고, 어떻게 검증하는지 작성해야 한다.

---

### [FAQ]

Q. Multi-Agent Orchestration의 핵심은 무엇인가?

A. 여러 Agent의 역할, 실행 순서, 상태 공유, 결과 통합, 검증, 실패 처리를 조율하는 것이다.

Q. PM Agent는 왜 필요한가?

A. 사용자 요청을 분석하고 작업을 분해한 뒤 적절한 Specialist Agent에게 전달하기 위해 필요하다.

Q. Review Agent는 왜 필요한가?

A. Specialist Agent 결과의 근거, 품질, 누락, 형식, 위험 요소를 검증하기 위해 필요하다.

---

# 5. Agent Role Rules

## 5.1 Agent Role 작성 규칙

### [개념]

Agent Role은 각 Agent가 담당하는 책임과 금지 영역을 정의하는 규칙이다.

역할이 불명확하면 Agent 간 중복 작업, 책임 누락, 충돌이 발생한다.

---

### [핵심]

대표 Agent 역할:

- PM Agent: 요청 분석, 작업 분해, Agent Routing, 최종 통합
- Backend Agent: Backend 설계, API, DB, Service, Security 구현
- Frontend Agent: UI, Component, State, API 연동, UX 구현
- DevOps Agent: Linux, Docker, CI/CD, 배포, Monitoring, 장애 대응
- AI/ML Agent: RAG, Agent, LLM, Evaluation, Prompt, Retrieval 설계
- Review Agent: 결과 검증, 누락 확인, 근거 확인, 형식 검토
- Architecture Review Agent: 구조, 확장성, 의존성, 모듈 경계 검토

역할 작성 기준:

- 책임 범위 명확화
- 입력값 명확화
- 출력값 명확화
- 금지 작업 명확화
- 다른 Agent와의 경계 명확화

---

### [실무]

Agent Role 문서는 아래 형식을 권장한다.

```md
### [Agent Role]

Agent:

- Backend Agent

Responsibilities:

- API 설계
- Entity / DTO / Repository / Service / Controller 구현
- Security 적용
- DB 연동

Inputs:

- taskGoal
- domainRules
- retrievedContext
- constraints

Outputs:

- implementationPlan
- codeDraft
- riskNotes
- testPoints

Do Not:

- Frontend UI 구현
- 배포 환경 변경
- 최종 승인 없이 전체 구조 변경
```

Agent Role은 문서마다 반복되어도 된다.

Retrieval 정확도를 위해 Role 키워드 반복을 허용한다.

---

### [FAQ]

Q. Agent Role은 왜 명확해야 하는가?

A. 역할이 모호하면 Agent 간 중복 작업과 책임 누락이 발생하기 때문이다.

Q. PM Agent가 모든 작업을 직접 수행해도 되는가?

A. 권장하지 않는다. PM Agent는 작업 분해, Routing, 통합에 집중하고 구현은 Specialist Agent에게 위임한다.

Q. Review Agent가 코드를 직접 수정해야 하는가?

A. 기본적으로 검증과 수정 요청을 담당하고, 직접 수정은 정책에 따라 제한한다.

---

# 6. Task Decomposition Rules

## 6.1 Task Decomposition 작성 규칙

### [개념]

Task Decomposition은 사용자 요청을 Agent가 수행 가능한 작은 작업 단위로 분해하는 과정이다.

Multi-Agent Orchestration에서 Task Decomposition 품질은 전체 Workflow 품질을 결정한다.

---

### [핵심]

Task Decomposition 기준:

- Domain 기준 분리
- Layer 기준 분리
- 기능 기준 분리
- 위험도 기준 분리
- 검증 가능 단위로 분리
- Agent Role 기준으로 분리
- 순차 / 병렬 가능성 구분
- 의존성 명시

Task 유형:

- Planning Task
- Research Task
- Design Task
- Implementation Task
- Review Task
- Test Task
- Fix Task
- Deployment Task

---

### [실무]

Task Decomposition 예시:

```text
User Request:
JWT 로그인 기능 구현해줘

Task Decomposition:
1. PM Agent: 요구사항 분석
2. Backend Agent: Auth API 설계
3. Backend Agent: JWT 발급 / 검증 로직 구현
4. Backend Agent: SecurityFilterChain 적용
5. Review Agent: 인증 Flow 검증
6. Test Agent: 로그인 성공 / 실패 / 만료 Token 테스트
7. PM Agent: 최종 결과 통합
```

작업은 Agent가 검증 가능한 단위로 나눈다.

너무 큰 Task는 Specialist Agent의 출력 품질을 낮춘다.

---

### [FAQ]

Q. Task Decomposition은 왜 필요한가?

A. 복합 요청을 Agent별로 수행 가능한 작은 작업 단위로 분해해야 안정적인 실행과 검증이 가능하기 때문이다.

Q. 작업을 얼마나 작게 나누어야 하는가?

A. 하나의 Agent가 명확한 입력과 출력으로 수행하고 검증할 수 있는 단위가 적절하다.

Q. 병렬 작업은 언제 가능한가?

A. 서로 의존성이 낮고 Shared State 충돌 가능성이 낮은 작업에서 가능하다.

---

# 7. Agent Routing Rules

## 7.1 Agent Routing 작성 규칙

### [개념]

Agent Routing은 분해된 Task를 어떤 Agent에게 전달할지 결정하는 과정이다.

Agent Routing 기준이 없으면 PM Agent가 잘못된 Agent에게 작업을 보내거나, 불필요하게 많은 Agent를 호출할 수 있다.

---

### [핵심]

Routing 기준:

- Domain
- Task Type
- Required Tool
- Required RAG Document
- Risk Level
- Dependency
- Required Validation
- User Output Type

Routing 예시:

- API / DB / Security → Backend Agent
- Component / UI / State → Frontend Agent
- Docker / Linux / CI/CD → DevOps Agent
- RAG / LLM / Agent / Evaluation → AI/ML Agent
- 품질 검증 / 누락 확인 → Review Agent
- 구조 검토 / 확장성 검토 → Architecture Review Agent

---

### [실무]

Agent Routing Flow:

```text
Task
→ Domain Classification
→ Risk Classification
→ Required Context Search
→ Agent Candidate Selection
→ Routing Decision
→ Specialist Agent Execution
```

Routing Rule 예시:

```text
if task.domain == "Backend" and task.type == "Implementation":
    routeTo = "Backend Agent"

if task.requiresValidation == true:
    routeToReview = "Review Agent"

if task.affectsArchitecture == true:
    routeToArchitectureReview = "Architecture Review Agent"
```

Agent Routing은 최소 Agent 호출을 기본값으로 한다.

불필요한 Agent 호출은 비용, 지연, 충돌을 증가시킨다.

---

### [FAQ]

Q. Agent Routing은 왜 중요한가?

A. 적절한 Agent에게 작업을 보내야 품질이 높고 불필요한 Agent 호출을 줄일 수 있기 때문이다.

Q. 모든 작업을 Review Agent에게 보내야 하는가?

A. 중요한 구현, 구조 변경, 보안, 배포, 최종 출력은 Review Agent 검토를 권장한다.

Q. Routing 실패 시 어떻게 해야 하는가?

A. PM Agent가 Task를 재분류하고 적절한 Agent에게 다시 전달한다.

---

# 8. Agent Contract Rules

## 8.1 Agent Input / Output Contract 작성 규칙

### [개념]

Agent Contract는 Agent 간 전달되는 입력과 출력의 구조를 정의하는 규칙이다.

Agent Contract가 명확해야 결과 통합, 검증, 재시도, 추적이 가능하다.

---

### [핵심]

Agent Input Contract 포함 요소:

- taskId
- taskGoal
- agentRole
- domain
- constraints
- requiredContext
- retrievedContext
- previousOutput
- acceptanceCriteria
- outputFormat

Agent Output Contract 포함 요소:

- taskId
- agentRole
- resultSummary
- output
- assumptions
- risks
- missingInfo
- validationPoints
- nextActions
- confidence

---

### [실무]

Agent Contract 예시:

```text
AgentInput:
- taskId: AUTH-001
- taskGoal: JWT 로그인 API 설계
- agentRole: Backend Agent
- domain: Spring Security
- constraints: Spring Boot 3.x, JWT, ApiResponse 사용
- retrievedContext: Security Domain Rules
- acceptanceCriteria: 로그인 성공 / 실패 응답 구조 포함
- outputFormat: implementationPlan + codeDraft + testPoints

AgentOutput:
- taskId: AUTH-001
- agentRole: Backend Agent
- resultSummary: JWT 로그인 API 설계 완료
- output: AuthController / AuthService 설계안
- assumptions: User Entity 존재
- risks: Refresh Token 저장 정책 필요
- validationPoints: Token 만료, 위조 Token 검증
- confidence: medium
```

Agent Contract는 너무 복잡하게 시작하지 않는다.

필수 필드부터 고정하고 필요에 따라 확장한다.

---

### [FAQ]

Q. Agent Contract는 왜 필요한가?

A. Agent 간 전달 데이터가 일관되어야 결과 통합, 검증, 재시도, 추적이 가능하기 때문이다.

Q. Agent Output에 assumptions를 넣어야 하는가?

A. 넣어야 한다. 가정이 명확해야 Review Agent가 위험 요소를 검토할 수 있다.

Q. confidence는 왜 필요한가?

A. Agent 출력의 확신도를 표시해 Review 또는 Human-in-the-Loop 필요 여부를 판단하기 위해 사용한다.

---

# 9. State Management Rules

## 9.1 Shared State / Private State 작성 규칙

### [개념]

State Management는 Multi-Agent Workflow에서 작업 상태, 검색 결과, Agent 출력, 검증 결과를 관리하는 규칙이다.

Shared State는 여러 Agent가 참조하는 공통 상태이고, Private State는 특정 Agent 내부 작업 상태이다.

---

### [핵심]

Shared State 포함 가능 정보:

- userRequest
- projectGoal
- taskList
- routingPlan
- globalConstraints
- domainRules
- retrievedContext
- agentOutputs
- validationResults
- finalDecision
- finalOutput

Private State 포함 가능 정보:

- agentLocalPlan
- temporaryReasoning
- toolCallHistory
- localRetrievedContext
- draftOutput
- retryCount
- localError

State 작성 기준:

- Shared State는 최소화
- Private State는 Agent 내부에 제한
- 최종 판단에 필요한 정보만 공유
- 민감정보 저장 금지
- 오래된 State 갱신 기준 필요
- State 충돌 시 PM Agent가 조정

---

### [실무]

State Flow 예시:

```text
User Request
→ sharedState.userRequest 저장
→ PM Agent taskList 생성
→ sharedState.routingPlan 저장
→ Specialist Agent privateState 생성
→ Specialist Agent output 생성
→ sharedState.agentOutputs 저장
→ Review Agent validationResults 저장
→ PM Agent finalOutput 생성
```

Shared State가 비대해지면 Context Noise가 증가한다.

State에는 “필요한 정보”만 저장하고, 장문 원문은 RAG 문서나 Source Reference로 연결한다.

---

### [FAQ]

Q. Shared State와 Private State의 차이는?

A. Shared State는 여러 Agent가 참조하는 공통 상태이고, Private State는 특정 Agent 내부 작업 상태이다.

Q. 모든 Agent 출력을 Shared State에 저장해야 하는가?

A. 최종 통합과 검증에 필요한 요약, 결과, 위험, 검증 포인트만 저장하는 것이 좋다.

Q. State 충돌이 발생하면 누가 조정하는가?

A. PM Agent가 충돌을 조정하고 필요한 경우 Review Agent 또는 Human Review로 넘긴다.

---

# 10. Message Passing Rules

## 10.1 Agent 간 메시지 전달 작성 규칙

### [개념]

Message Passing은 Agent 간 작업 요청, 결과 전달, 수정 요청, 검증 결과를 주고받는 방식이다.

메시지 구조가 불명확하면 Agent Workflow가 끊기거나 결과가 잘못 통합된다.

---

### [핵심]

메시지 유형:

- TaskRequest
- ContextRequest
- ToolRequest
- ResultResponse
- ReviewRequest
- FixRequest
- ApprovalRequest
- ErrorReport
- FinalOutputRequest

메시지 필수 요소:

- messageId
- fromAgent
- toAgent
- taskId
- messageType
- payload
- requiredAction
- deadlinePolicy
- priority
- status

---

### [실무]

Message Passing 예시:

```text
MessageType:
- ReviewRequest

From:
- PM Agent

To:
- Review Agent

Payload:
- Backend Agent output
- Acceptance Criteria
- Retrieved Context
- Risk Notes

RequiredAction:
- Validate groundedness, missing requirements, security risks, output format
```

메시지는 짧고 구조적으로 작성한다.

장문 설명보다 Agent가 실행할 Action과 검증 기준을 명확히 작성한다.

---

### [FAQ]

Q. Message Passing 규칙은 왜 필요한가?

A. Agent 간 요청과 응답 구조가 일관되어야 Workflow 추적과 오류 복구가 가능하기 때문이다.

Q. FixRequest에는 무엇을 넣어야 하는가?

A. 수정 대상, 문제 원인, 요구 수정 사항, 검증 기준을 포함해야 한다.

Q. 메시지에 전체 원문을 넣어야 하는가?

A. 아니다. 필요한 요약과 Source Reference를 넣고, 원문은 RAG 검색으로 연결하는 것이 좋다.

---

# 11. Execution Pattern Rules

## 11.1 Sequential / Parallel / Consensus Pattern 작성 규칙

### [개념]

Execution Pattern은 Agent들을 어떤 순서와 구조로 실행할지 정의하는 규칙이다.

Multi-Agent Orchestration은 요청 특성에 따라 Sequential, Parallel, Consensus, Critic, Supervisor Pattern을 선택해야 한다.

---

### [핵심]

주요 Pattern:

- Sequential Pattern
- Parallel Pattern
- Supervisor Pattern
- Router Pattern
- Critic Pattern
- Consensus Pattern
- Debate Pattern
- Planner-Executor Pattern
- Reflection Pattern

선택 기준:

- 순차 의존성 있음 → Sequential Pattern
- 독립 작업 병렬 처리 → Parallel Pattern
- 중앙 조율 필요 → Supervisor Pattern
- Domain 분기 필요 → Router Pattern
- 검증 필요 → Critic Pattern
- 복수 의견 비교 필요 → Consensus Pattern
- 계획과 실행 분리 필요 → Planner-Executor Pattern

---

### [실무]

Pattern 예시:

```text
Sequential Pattern:
PM Agent
→ Backend Agent
→ Review Agent
→ Fix
→ Final Output

Parallel Pattern:
PM Agent
→ Backend Agent
→ Frontend Agent
→ DevOps Agent
→ PM Agent Aggregation
→ Review Agent

Critic Pattern:
Specialist Agent Output
→ Review Agent
→ Issue List
→ Specialist Agent Fix
→ Final Review
```

Pattern은 요청마다 선택한다.

모든 Workflow에 복잡한 Pattern을 적용하지 않는다.

---

### [FAQ]

Q. Sequential Pattern은 언제 사용하는가?

A. 이전 단계 결과가 다음 단계 입력이 되는 작업에서 사용한다.

Q. Parallel Pattern은 언제 사용하는가?

A. 작업 간 의존성이 낮고 동시에 수행해도 충돌이 적은 경우 사용한다.

Q. Critic Pattern은 왜 필요한가?

A. Specialist Agent의 출력 오류, 누락, 형식 위반, 근거 부족을 검출하기 위해 필요하다.

---

# 12. RAG Coordination Rules

## 12.1 Multi-Agent RAG Coordination 작성 규칙

### [개념]

RAG Coordination은 여러 Agent가 RAG 문서를 검색하고 사용할 때 검색 범위, Context 우선순위, 중복 제거, 충돌 해결을 관리하는 규칙이다.

Multi-Agent 환경에서는 Agent마다 다른 문서를 검색하므로 Context 충돌과 중복이 발생할 수 있다.

---

### [핵심]

RAG Coordination 기준:

- Domain Rules 우선 적용
- Project Progress 참고
- Agent Role별 검색 범위 제한
- Shared Context와 Local Context 구분
- 중복 Chunk 제거
- 충돌 Context 감지
- 최신 규칙 우선
- Source Priority 명시
- Review Agent가 근거 검증

검색 우선순위:

```text
MASTER_RAG_RULES
→ PROJECT_PROGRESS
→ DOMAIN_RULES
→ PART DOCUMENTS
→ Agent Local Context
→ Memory
```

---

### [실무]

Agent별 RAG 검색 범위 예시:

```text
PM Agent:
- Project Progress
- Domain Rules
- Workflow Rules
- Agent Routing Rules

Backend Agent:
- Backend Domain Rules
- Security Rules
- API Design Rules
- Database Rules

AI/ML Agent:
- Agentic RAG Rules
- Graph RAG Rules
- Multi-Agent Orchestration Rules
- Evaluation Rules

Review Agent:
- Domain Rules
- Checklist
- Common Mistakes
- Troubleshooting
```

여러 Agent가 서로 다른 Context를 사용한 경우 PM Agent가 결과 통합 시 충돌 여부를 확인한다.

---

### [FAQ]

Q. Multi-Agent에서 RAG Coordination이 왜 필요한가?

A. Agent마다 다른 Context를 검색하면 중복, 충돌, 오래된 정보 사용 문제가 발생할 수 있기 때문이다.

Q. Domain Rules와 Agent Local Context가 충돌하면 무엇을 우선하는가?

A. Domain Rules와 Project Progress를 우선한다.

Q. Review Agent는 RAG Coordination에서 무엇을 확인하는가?

A. 출력이 검색 근거와 일치하는지, 오래된 Context를 사용하지 않았는지, 누락된 문서가 없는지 확인한다.

---

# 13. Tool Coordination Rules

## 13.1 Multi-Agent Tool Coordination 작성 규칙

### [개념]

Tool Coordination은 여러 Agent가 도구를 호출할 때 권한, 순서, 입력값, 결과 공유, 실패 처리를 조율하는 규칙이다.

Multi-Agent 환경에서는 도구 호출 중복, 충돌, 비용 증가, 잘못된 상태 변경을 방지해야 한다.

---

### [핵심]

Tool Coordination 기준:

- Tool 사용 권한 정의
- Tool 호출 전 목적 확인
- Tool 입력값 검증
- Tool 결과 저장 위치 정의
- Tool 결과 공유 범위 정의
- 중복 호출 방지
- 상태 변경 Tool은 승인 기준 필요
- 실패 시 Retry / Fallback 기준 필요
- Tool Result 검증 필요

Tool 유형:

- Search Tool
- File Search Tool
- Code Execution Tool
- Database Tool
- API Tool
- Calendar Tool
- Email Tool
- Deployment Tool
- Evaluation Tool

---

### [실무]

Tool Coordination Flow:

```text
Agent Tool Need
→ Tool Permission Check
→ Input Validation
→ Tool Call
→ Tool Result Validation
→ Shared State Update
→ Next Agent Notification
```

상태 변경 Tool 예시:

```text
주의 필요:
- Email Send
- Calendar Event Create
- File Delete
- Deployment Execute
- Database Migration
- Production Config Change
```

상태 변경 Tool은 PM Agent 승인 또는 Human-in-the-Loop 기준을 둔다.

---

### [FAQ]

Q. Tool Coordination은 왜 필요한가?

A. 여러 Agent가 중복으로 도구를 호출하거나 상태를 잘못 변경하는 문제를 방지하기 위해 필요하다.

Q. Tool Result는 바로 최종 답변에 사용해도 되는가?

A. 아니다. Tool 결과를 검증하고 필요한 경우 Review Agent가 확인해야 한다.

Q. 상태 변경 Tool은 어떻게 관리해야 하는가?

A. 권한, 승인, 입력 검증, 실행 로그, 복구 계획을 명확히 해야 한다.

---

# 14. Review and Validation Rules

## 14.1 Review Agent 검증 작성 규칙

### [개념]

Review and Validation은 Specialist Agent 결과가 사용자 요청, Domain Rules, 검색 근거, 출력 형식, 품질 기준을 만족하는지 확인하는 단계이다.

Multi-Agent Orchestration에서는 Review Agent가 품질 안정화의 핵심이다.

---

### [핵심]

Review 항목:

- 사용자 요청 충족 여부
- Agent Role 준수 여부
- Domain Rules 준수 여부
- 검색 근거 일치 여부
- Hallucination 여부
- 누락된 요구사항 여부
- 출력 형식 준수 여부
- 위험한 작업 여부
- 테스트 가능 여부
- 보안 문제 여부
- 충돌 Context 여부
- 최종 통합 가능 여부

---

### [실무]

Review Checklist 예시:

```md
### [Checklist]

- 사용자 요청을 직접 해결했는가?
- PM Agent가 Task를 적절히 분해했는가?
- 올바른 Specialist Agent에게 Routing 되었는가?
- Agent Output Contract를 지켰는가?
- 검색 근거와 결과가 일치하는가?
- 누락된 요구사항이 없는가?
- 위험하거나 확정할 수 없는 내용을 단정하지 않았는가?
- 최종 출력 형식을 지켰는가?
```

Review 결과는 Pass / Fix Required / Human Review Required로 구분한다.

---

### [FAQ]

Q. Review Agent는 왜 필요한가?

A. Specialist Agent 출력의 오류, 누락, 근거 부족, 형식 위반, 위험 요소를 검증하기 위해 필요하다.

Q. Review 결과가 Fix Required이면 어떻게 하는가?

A. PM Agent가 FixRequest를 생성해 해당 Specialist Agent에게 다시 전달한다.

Q. 모든 작업에 Review Agent가 필요한가?

A. 단순 작업은 생략 가능하지만, 구현, 보안, 배포, 아키텍처, 최종 산출물은 Review를 권장한다.

---

# 15. Retry and Fallback Rules

## 15.1 Retry / Fallback 작성 규칙

### [개념]

Retry와 Fallback은 Agent 실행 실패, 검색 실패, 도구 호출 실패, 검증 실패 발생 시 Workflow를 복구하는 규칙이다.

Advanced Multi-Agent Orchestration은 실패를 전제로 설계해야 한다.

---

### [핵심]

Retry 조건:

- 검색 결과 부족
- Tool Calling 일시 실패
- Agent Output Contract 위반
- Review Agent 검증 실패
- Context 누락
- 출력 형식 오류
- 낮은 confidence

Fallback 조건:

- 동일 Agent 반복 실패
- Tool 사용 불가
- 필요한 문서 부재
- Context 충돌 해결 불가
- 권한 부족
- 위험 작업 감지
- Human 판단 필요

---

### [실무]

Retry / Fallback Flow:

```text
Agent Execution
→ Validation
→ Fail
→ Retry Decision
→ Retry with Modified Input
→ Validation
→ Fallback Decision
→ Alternative Agent or Human Review
```

Retry 작성 규칙:

- 동일 입력으로 반복 금지
- 실패 원인 기록
- 수정된 입력으로 재시도
- retryCount 제한
- 반복 실패 시 Fallback 전환

Fallback 예시:

```text
Backend Agent가 2회 실패
→ PM Agent가 Task 재분해
→ Architecture Review Agent 검토
→ 필요한 경우 Human Review 요청
```

---

### [FAQ]

Q. Retry는 언제 수행하는가?

A. 검색 부족, 출력 형식 오류, Tool 일시 실패, 검증 실패처럼 수정 가능성이 있는 경우 수행한다.

Q. 동일 요청을 그대로 반복해도 되는가?

A. 권장하지 않는다. 실패 원인을 반영해 입력, Query, Agent, Context를 수정해야 한다.

Q. Fallback은 언제 필요한가?

A. 반복 실패, 권한 부족, 위험 작업, Context 충돌, Human 판단이 필요한 경우 필요하다.

---

# 16. Human-in-the-Loop Rules

## 16.1 Human Review 작성 규칙

### [개념]

Human-in-the-Loop은 Agent가 단독으로 결정하기 어렵거나 위험한 작업에서 사람의 확인을 받는 구조이다.

Multi-Agent Orchestration에서는 자동화와 안전성 사이의 경계를 명확히 해야 한다.

---

### [핵심]

Human Review 필요 상황:

- Production 변경
- 데이터 삭제
- 결제 / 메일 / 캘린더 등 상태 변경
- 보안 정책 변경
- 개인정보 처리
- 불확실한 요구사항
- 높은 비용의 작업
- 비가역 작업
- 법률 / 의료 / 금융 고위험 판단
- Agent 간 결론 충돌
- confidence 낮음
- Review Agent가 위험 표시

Human Review 요청 포함 요소:

- 결정해야 할 항목
- Agent 추천안
- 근거
- 위험
- 대안
- 되돌릴 수 있는지 여부
- 승인 후 실행 내용

---

### [실무]

Human Review 요청 예시:

```text
Human Review Required

결정 항목:
- Production DB Migration 실행 여부

Agent 추천:
- Migration 전 Backup 필요

근거:
- Schema 변경으로 기존 데이터 영향 가능

위험:
- Rollback 어려움
- 서비스 중단 가능

대안:
- Staging 환경에서 먼저 검증
```

Human Review는 불필요하게 남발하지 않는다.

단, 위험 작업에서는 자동 실행보다 Human Review를 우선한다.

---

### [FAQ]

Q. Human-in-the-Loop은 왜 필요한가?

A. Agent가 단독으로 결정하기 어려운 위험 작업이나 불확실한 상황에서 안전성을 확보하기 위해 필요하다.

Q. 모든 작업에 Human Review가 필요한가?

A. 아니다. 비가역 작업, 상태 변경, 보안, 배포, 불확실성이 큰 작업에 필요하다.

Q. Human Review 요청에는 무엇을 포함해야 하는가?

A. 결정 항목, 추천안, 근거, 위험, 대안, 승인 후 실행 내용을 포함해야 한다.

---

# 17. Observability Rules

## 17.1 Multi-Agent Observability 작성 규칙

### [개념]

Observability는 Multi-Agent Workflow의 실행 상태, Agent 호출, Tool 호출, RAG 검색, 오류, 검증 결과를 추적하는 구조이다.

Multi-Agent System은 실행 흐름이 복잡하므로 관측 가능성이 없으면 문제 원인을 찾기 어렵다.

---

### [핵심]

관측 대상:

- userRequest
- taskId
- workflowId
- agentName
- agentRole
- routingDecision
- retrievedContext
- toolCall
- toolResult
- agentOutput
- validationResult
- retryCount
- errorType
- latency
- cost
- finalOutput

로그 기준:

- Workflow 단위 추적
- Agent 단위 추적
- Tool Call 단위 추적
- RAG Retrieval 단위 추적
- Validation 결과 추적
- Error / Retry 추적

---

### [실무]

Observability Log 예시:

```text
workflowId: WF-2026-001
taskId: AUTH-001
agent: Backend Agent
action: Generate Auth API Plan
retrieval: Security_Advanced_Part04_JWT.md
toolCall: none
validation: Fix Required
errorType: Missing Refresh Token Policy
retryCount: 1
```

운영 환경에서는 Agent Trace, Tool Trace, Retrieval Trace를 분리해서 확인할 수 있어야 한다.

---

### [FAQ]

Q. Multi-Agent Observability는 왜 필요한가?

A. 여러 Agent와 Tool이 관여하므로 실패 원인, 비용, 지연, 품질 문제를 추적하기 위해 필요하다.

Q. 무엇을 반드시 로깅해야 하는가?

A. workflowId, taskId, agentName, routingDecision, toolCall, retrieval, validationResult, errorType, retryCount를 기록해야 한다.

Q. Agent 내부 추론 전체를 저장해야 하는가?

A. 아니다. 최종 판단에 필요한 요약, 결정, 근거, 오류 정보 중심으로 저장한다.

---

# 18. Evaluation Rules

## 18.1 Multi-Agent Orchestration Evaluation 작성 규칙

### [개념]

Multi-Agent Orchestration Evaluation은 여러 Agent가 작업을 제대로 분해, 실행, 검증, 통합했는지 평가하는 기준이다.

단일 Agent 답변 품질만 평가하지 않는다.

---

### [핵심]

평가 항목:

- Task Decomposition Quality
- Agent Routing Accuracy
- Agent Role Compliance
- Contract Compliance
- Shared State Consistency
- RAG Context Relevance
- Tool Coordination Accuracy
- Review Coverage
- Fix Loop Quality
- Final Output Integration
- User Goal Completion
- Latency
- Cost
- Error Recovery
- Human Review Appropriateness

---

### [실무]

Evaluation Checklist:

```md
### [Checklist]

- 사용자 요청이 올바르게 Task로 분해되었는가?
- 각 Task가 적절한 Agent에게 Routing 되었는가?
- Agent가 자신의 Role을 벗어나지 않았는가?
- Agent Output Contract를 지켰는가?
- Shared State가 일관되게 유지되었는가?
- Review Agent가 핵심 위험을 검토했는가?
- Fix Loop가 실제 문제를 해결했는가?
- 최종 출력이 통합되어 일관적인가?
- 불필요한 Agent 호출이 없었는가?
- Human Review가 필요한 상황을 놓치지 않았는가?
```

평가는 Workflow 단위와 Agent 단위로 나누어 수행한다.

---

### [FAQ]

Q. Multi-Agent Orchestration 평가는 무엇이 다른가?

A. 개별 답변 정확도뿐 아니라 Task 분해, Routing, State, Contract, Review, 통합 품질을 평가한다.

Q. Agent Routing Accuracy는 무엇인가?

A. Task가 가장 적절한 Agent에게 전달되었는지 평가하는 항목이다.

Q. 불필요한 Agent 호출도 평가 대상인가?

A. 그렇다. 불필요한 호출은 비용, 지연, 충돌 가능성을 증가시킨다.

---

# 19. Troubleshooting Rules

## 19.1 Multi-Agent Orchestration 장애 대응 작성 규칙

### [개념]

Troubleshooting 문서는 Multi-Agent Workflow에서 발생하는 Routing 실패, Agent 충돌, State 불일치, Tool 충돌, Review 누락, 결과 통합 실패를 해결하기 위한 규칙이다.

---

### [핵심]

자주 발생하는 문제:

- Task Decomposition 실패
- Agent Routing 오류
- Agent Role 중복
- Agent Role 누락
- Agent Contract 위반
- Shared State 오염
- Context 충돌
- Tool Calling 중복
- Tool 권한 오류
- Specialist Agent 결과 불일치
- Review Agent 누락
- Fix Loop 무한 반복
- Human Review 누락
- Final Output 통합 실패

---

### [실무]

Troubleshooting 형식:

```md
문제:
Backend Agent와 Frontend Agent 출력이 API Response 구조에서 충돌함

원인:

- Shared State에 API Contract가 고정되지 않음
- PM Agent가 공통 DTO 기준을 전달하지 않음
- Review Agent가 통합 검증을 수행하지 않음

해결:

- PM Agent가 API Contract를 Shared State에 등록
- Backend Agent와 Frontend Agent에 동일 Contract 전달
- Review Agent가 Response Schema 일치 여부 검증
```

장애 대응 문서는 문제 / 원인 / 해결 형식을 기본으로 한다.

---

### [FAQ]

Q. Multi-Agent Orchestration에서 가장 흔한 실패는?

A. Task 분해 실패, 잘못된 Agent Routing, Shared State 충돌, Review 누락, 결과 통합 실패이다.

Q. Agent 간 결과가 충돌하면 어떻게 해야 하는가?

A. PM Agent가 충돌 지점을 정리하고 Review Agent 또는 Architecture Review Agent 검토 후 기준을 확정한다.

Q. Fix Loop가 반복되면 어떻게 해야 하는가?

A. retryCount를 제한하고 실패 원인을 재분류한 뒤 Fallback 또는 Human Review로 전환한다.

---

# 20. Common Mistakes

## 20.1 자주 발생하는 작성 오류

### [개념]

Advanced Multi-Agent Orchestration 문서는 Agent를 여러 개 나열하는 문서가 아니다.

역할, Routing, State, Contract, Review, Retry, Fallback, Evaluation 기준을 제공해야 한다.

---

### [핵심]

금지 또는 주의:

- Agent 목록만 작성
- PM Agent 역할 누락
- Review Agent 역할 누락
- Agent Routing 기준 누락
- Task Decomposition 기준 누락
- Agent Contract 누락
- Shared State / Private State 구분 누락
- Message Passing 기준 누락
- Tool Coordination 기준 누락
- Retry / Fallback 기준 누락
- Human-in-the-Loop 기준 누락
- Evaluation Checklist 누락
- Troubleshooting 누락
- 프레임워크 코드 복붙 중심 작성
- 장문 개념 설명 중심 작성
- Retrieval Queries 누락

---

### [실무]

나쁜 문서 예시:

```text
Multi-Agent는 여러 AI Agent가 협력해서 작업하는 구조이다.
PM Agent, Backend Agent, Frontend Agent, Review Agent를 만들면 된다.
```

좋은 문서 예시:

```text
Multi-Agent Orchestration은 PM Agent가 요청을 분석하고 Task를 분해한 뒤 Specialist Agent에게 Routing하고, Review Agent가 결과를 검증하며, PM Agent가 최종 출력으로 통합하는 구조이다.

Flow:
User Request
→ PM Agent
→ Task Decomposition
→ Agent Routing
→ Specialist Agent Execution
→ Review Agent Validation
→ Fix Loop
→ Final Output
```

---

### [FAQ]

Q. Multi-Agent Orchestration 문서에서 가장 피해야 할 것은?

A. Agent 이름만 나열하고 Routing, State, Contract, Review 기준을 작성하지 않는 것이다.

Q. 프레임워크 예제 코드를 많이 넣으면 좋은가?

A. 아니다. Domain Rules에서는 프레임워크보다 역할, 흐름, 검증 기준이 더 중요하다.

Q. Review Agent는 선택 사항인가?

A. 단순 작업에서는 생략 가능하지만, 복잡한 작업과 최종 산출물 품질 검증에서는 핵심 역할이다.

---

# 21. Document Split Rules

## 21.1 Advanced Multi-Agent Orchestration 문서 분할 기준

### [개념]

Advanced Multi-Agent Orchestration은 Role, Routing, State, Contract, Tool Coordination, Review, Evaluation 범위가 넓기 때문에 Part 단위로 분리한다.

각 Part는 독립 검색 가능해야 하며, 하나의 Part는 하나의 핵심 주제를 다룬다.

---

### [핵심]

권장 문서 분할:

```text
Advanced_Multi_Agent_Orchestration_Part01_Core.md
Advanced_Multi_Agent_Orchestration_Part02_Agent_Role_Task_Decomposition.md
Advanced_Multi_Agent_Orchestration_Part03_Agent_Routing_Contract.md
Advanced_Multi_Agent_Orchestration_Part04_State_Message_Passing.md
Advanced_Multi_Agent_Orchestration_Part05_Execution_Patterns.md
Advanced_Multi_Agent_Orchestration_Part06_RAG_Tool_Coordination.md
Advanced_Multi_Agent_Orchestration_Part07_Review_Retry_Human_Loop.md
Advanced_Multi_Agent_Orchestration_Part08_Evaluation_Troubleshooting.md
```

분할 기준:

- 하나의 Part는 하나의 핵심 주제
- Role과 Task Decomposition은 함께 작성 가능
- Routing과 Contract는 함께 작성 권장
- State와 Message Passing은 함께 작성 권장
- Review / Retry / Human-in-the-Loop은 연결 문서로 작성
- Evaluation은 Checklist 중심
- Troubleshooting은 문제 / 원인 / 해결 형식
- 각 Part는 FAQ 포함
- 각 Part는 Retrieval Queries 포함

---

### [실무]

Advanced Multi-Agent Orchestration 문서 Set은 AI Expert Level에서 사용한다.

단, PM Agent와 Review Agent가 핵심 사용자이므로 프레임워크 종속 코드보다 Workflow와 판단 기준을 우선한다.

특정 프레임워크 구현은 별도 문서로 분리한다.

예:

```text
Advanced_Multi_Agent_Orchestration_Domain_Rules.md
LangGraph_Domain_Rules.md
AutoGen_Domain_Rules.md
CrewAI_Domain_Rules.md
Agent_Evaluation_Domain_Rules.md
```

---

### [FAQ]

Q. Advanced Multi-Agent Orchestration 문서는 몇 개 Part로 나누는 것이 좋은가?

A. 7~8개 Part를 권장한다. Core, Role, Routing, State, Pattern, Coordination, Review, Evaluation/Troubleshooting으로 분리한다.

Q. LangGraph 문서와 합쳐도 되는가?

A. 권장하지 않는다. Orchestration Domain Rules는 프레임워크 중립으로 작성하고 LangGraph 구현은 별도 문서로 분리한다.

Q. 각 Part에도 Retrieval Queries가 필요한가?

A. 필요하다. 각 문서가 독립 검색될 수 있어야 한다.

---

# 22. Agent Usage Rules

## 22.1 Agent별 사용 기준

### [개념]

Advanced Multi-Agent Orchestration Domain Rules는 여러 Agent가 동일한 기준으로 협업하고, 작업을 분해하고, 상태를 공유하고, 결과를 검증하도록 돕는다.

각 Agent는 자신의 역할에 맞는 Orchestration Chunk를 우선 검색한다.

---

### [핵심]

PM Agent:

- User Request 분석
- Task Decomposition
- Agent Routing
- Shared State 관리
- 결과 통합
- Human Review 판단

Backend Agent:

- Backend Task 수행
- Agent Contract 준수
- 구현 결과와 위험 포인트 출력
- Test Point 제공

Frontend Agent:

- Frontend Task 수행
- API Contract 준수
- UI / State / Error Handling 결과 출력
- UX Risk 제공

DevOps Agent:

- 배포 / 운영 Task 수행
- Tool Coordination 준수
- 위험 작업 Human Review 요청
- 운영 리스크 출력

AI/ML Agent:

- Agentic RAG / Graph RAG / Evaluation 설계
- Multi-Agent Workflow 개선
- Retrieval / Tool Coordination 설계

Review Agent:

- Contract 준수 검토
- Groundedness 검토
- 누락 검토
- Format 검토
- Risk 검토
- FixRequest 생성

Architecture Review Agent:

- 구조 검토
- Agent 경계 검토
- 의존성 검토
- 확장성 검토
- 장기 유지보수성 검토

---

### [실무]

Agent별 검색 우선순위:

```text
PM Agent
→ Task Decomposition / Agent Routing / Shared State / Final Output Integration

Specialist Agent
→ Agent Contract / Role Rules / Domain Rules / Output Format

Review Agent
→ Review Checklist / Common Mistakes / Troubleshooting / Evaluation

AI/ML Agent
→ Execution Pattern / RAG Coordination / Tool Coordination / Evaluation

Architecture Review Agent
→ Role Boundary / State Management / Dependency / Scalability
```

---

### [FAQ]

Q. Advanced Multi-Agent Orchestration Domain Rules는 어떤 Agent가 사용하는가?

A. PM Agent, Specialist Agent, Review Agent, AI/ML Agent, Architecture Review Agent가 역할별로 사용한다.

Q. PM Agent는 어떤 Chunk를 우선 검색해야 하는가?

A. Task Decomposition, Agent Routing, Shared State, Final Output Integration 관련 Chunk를 우선 검색한다.

Q. Review Agent는 어떤 Chunk를 우선 검색해야 하는가?

A. Review Checklist, Agent Contract, Common Mistakes, Troubleshooting, Evaluation 관련 Chunk를 우선 검색한다.

---

# 23. Final Goal

## 23.1 최종 목표

### [개념]

Advanced Multi-Agent Orchestration Domain Rules의 최종 목표는 Agent가 복합 요청을 안정적으로 분해하고, 적절한 Agent에게 분배하고, 상태를 관리하고, 결과를 검증하고, 최종 산출물로 통합할 수 있도록 문서 제작 기준을 제공하는 것이다.

---

### [핵심]

최종 목표:

- Multi-Agent Orchestration 개념 검색 가능
- Agent Role 정의 가능
- Task Decomposition 가능
- Agent Routing 가능
- Agent Contract 설계 가능
- Shared State / Private State 구분 가능
- Message Passing 설계 가능
- Execution Pattern 선택 가능
- RAG Coordination 가능
- Tool Coordination 가능
- Review Workflow 설계 가능
- Retry / Fallback 가능
- Human-in-the-Loop 판단 가능
- Observability 설계 가능
- Evaluation 가능
- Troubleshooting 가능

---

### [실무]

Advanced Multi-Agent Orchestration RAG Doc Set은 다음 작업을 지원해야 한다.

```text
User Request
→ PM Agent Goal Analysis
→ Task Decomposition
→ Agent Routing
→ Specialist Agent Execution
→ Shared State Update
→ Review Agent Validation
→ Fix Loop
→ Final Output Integration
→ Human Review if needed
```

문서 품질은 Agent 간 협업 안정성, 결과 통합 품질, 검증 정확도, 실패 복구 가능성으로 결정된다.

---

### [FAQ]

Q. Advanced Multi-Agent Orchestration Domain Rules의 최종 목적은?

A. Agent가 복합 작업을 분해, 분배, 실행, 검증, 통합할 수 있도록 문서 제작 기준을 제공하는 것이다.

Q. 이 문서는 사람 학습용인가?

A. 아니다. Multi-Agent Workflow 실행과 Agent Retrieval 품질을 높이기 위한 문서이다.

Q. Multi-Agent Orchestration 문서 품질은 무엇으로 판단하는가?

A. Agent가 역할에 맞게 작업하고, 상태를 일관되게 공유하고, 결과를 검증해 최종 산출물로 통합할 수 있는지로 판단한다.

---

# Retrieval Queries

### [FAQ]

Q. Advanced Multi-Agent Orchestration이란?
A. 여러 Agent의 작업 분해, Routing, 상태 공유, 결과 통합, 검증, 실패 복구를 조율하는 구조이다.

Q. Multi-Agent Orchestration과 단순 Multi-Agent의 차이는?
A. 단순 Multi-Agent는 Agent를 여러 개 사용하는 것이고, Orchestration은 역할, 순서, State, Contract, Review를 조율하는 것이다.

Q. PM Agent의 역할은?
A. 사용자 요청 분석, Task Decomposition, Agent Routing, Shared State 관리, 최종 결과 통합이다.

Q. Specialist Agent란?
A. Backend, Frontend, DevOps, AI/ML처럼 특정 Domain 작업을 수행하는 Agent이다.

Q. Review Agent의 역할은?
A. Specialist Agent 결과의 근거, 누락, 품질, 형식, 위험 요소를 검증하는 것이다.

Q. Task Decomposition이란?
A. 사용자 요청을 Agent가 수행 가능한 작은 작업 단위로 분해하는 과정이다.

Q. Agent Routing이란?
A. 분해된 Task를 가장 적절한 Agent에게 전달하는 과정이다.

Q. Agent Contract란?
A. Agent 간 전달되는 입력과 출력 구조를 정의하는 규칙이다.

Q. Agent Output Contract에는 무엇이 포함되는가?
A. taskId, agentRole, resultSummary, output, assumptions, risks, missingInfo, validationPoints, confidence가 포함된다.

Q. Shared State란?
A. 여러 Agent가 참조하는 공통 작업 상태이다.

Q. Private State란?
A. 특정 Agent 내부에서만 사용하는 작업 상태이다.

Q. Message Passing이란?
A. Agent 간 작업 요청, 결과 전달, 수정 요청, 검증 결과를 주고받는 방식이다.

Q. Sequential Pattern은 언제 사용하는가?
A. 이전 단계 결과가 다음 단계 입력이 되는 작업에서 사용한다.

Q. Parallel Pattern은 언제 사용하는가?
A. 서로 의존성이 낮은 작업을 동시에 처리할 때 사용한다.

Q. Critic Pattern은 무엇인가?
A. Specialist Agent Output을 Review Agent가 검토하고 수정 요청하는 검증 패턴이다.

Q. RAG Coordination이란?
A. 여러 Agent가 검색한 Context의 우선순위, 중복, 충돌, 최신성을 관리하는 규칙이다.

Q. Tool Coordination이란?
A. 여러 Agent의 도구 호출 권한, 순서, 입력값, 결과 공유, 실패 처리를 조율하는 규칙이다.

Q. Retry는 언제 수행하는가?
A. 검색 부족, 출력 형식 오류, Tool 일시 실패, 검증 실패처럼 수정 가능한 오류에서 수행한다.

Q. Fallback은 언제 필요한가?
A. 반복 실패, 권한 부족, 위험 작업, Context 충돌, Human 판단이 필요한 경우 필요하다.

Q. Human-in-the-Loop은 언제 필요한가?
A. Production 변경, 데이터 삭제, 보안 변경, 비가역 작업, 낮은 confidence, Agent 간 결론 충돌 상황에서 필요하다.

Q. Multi-Agent Observability는 무엇인가?
A. Agent 호출, Tool 호출, RAG 검색, 검증 결과, 오류, 비용, 지연을 추적하는 구조이다.

Q. Multi-Agent Orchestration Evaluation 항목은?
A. Task Decomposition Quality, Agent Routing Accuracy, Contract Compliance, Shared State Consistency, Review Coverage, Final Output Integration이다.

Q. Multi-Agent Orchestration에서 흔한 실패는?
A. Task 분해 실패, Agent Routing 오류, Shared State 충돌, Review 누락, 결과 통합 실패이다.

Q. Advanced Multi-Agent Orchestration 문서 분할은 어떻게 하는가?
A. Core, Role, Routing, State, Pattern, Coordination, Review, Evaluation/Troubleshooting으로 분리한다.

Q. Advanced Multi-Agent Orchestration 문서에서 피해야 할 것은?
A. Agent 이름만 나열하고 Routing, State, Contract, Review, Retry 기준을 작성하지 않는 것이다.

Q. Advanced Multi-Agent Orchestration Domain Rules는 어떤 Agent가 사용하는가?
A. PM Agent, Specialist Agent, Review Agent, AI/ML Agent, Architecture Review Agent가 역할별로 사용한다.
