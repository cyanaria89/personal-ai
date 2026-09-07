# AI Observability Domain Rules

---

# 1. Domain Purpose

## 1.1 AI Observability 문서 목적

### [개념]

AI Observability Domain 문서는 AI Agent / AI/ML Agent / DevOps Agent / Backend Agent / Review Agent / Architecture Review Agent가 LLM, RAG, Agent, Tool Calling, Memory, Fine-Tuning, Model Serving 시스템의 동작을 관측, 추적, 분석, 개선할 때 참조하는 RAG 제작 규칙 문서이다.

AI Observability는 단순 로그 수집이 아니다.

AI Observability는 AI 시스템의 입력, Retrieval, Context, Prompt, Model Output, Tool Call, Agent State, Evaluation, 비용, 지연, 오류, 사용자 피드백을 연결하여 “왜 이런 답변이 나왔는가”를 추적하는 운영 체계이다.

---

### [핵심]

- AI Observability = Trace + Metrics + Logs + Evaluation + Feedback
- LLM 응답 원인 추적 필요
- RAG Retrieval 과정 추적 필요
- Prompt Version 추적 필요
- Context 구성 추적 필요
- Tool Calling 추적 필요
- Agent Workflow 추적 필요
- Memory 사용 추적 필요
- Hallucination 감지 필요
- Groundedness 평가 필요
- Latency / Cost 관측 필요
- 품질 저하 원인 분석 필요
- LLMOps / RAGOps / AgentOps / MLOps와 연결 필요

---

### [실무]

2026 실무 기준 AI Observability 문서는 다음 목적을 우선한다.

- LLM 호출 Trace 설계
- Prompt / Context / Output 추적 기준 제공
- RAG Retrieval Trace 기준 제공
- Agent Workflow Trace 기준 제공
- Tool Calling Trace 기준 제공
- Memory Usage Trace 기준 제공
- Evaluation Metric 기준 제공
- Hallucination / Groundedness 모니터링 기준 제공
- Latency / Cost / Token 사용량 관측 기준 제공
- Failure Analysis 기준 제공
- Feedback Loop 설계 기준 제공

AI Observability 문서는 사람이 로그 시스템을 공부하기 위한 문서가 아니라, Agent가 AI 시스템의 품질 문제를 추적하고 개선할 수 있도록 돕는 운영 지식 문서로 작성한다.

---

### [FAQ]

Q. AI Observability 문서는 무엇을 위한 문서인가?

A. Agent가 LLM, RAG, Tool Calling, Agent Workflow, Memory, Evaluation의 실행 흐름과 품질 문제를 추적할 수 있도록 기준을 제공하는 문서이다.

Q. AI Observability는 일반 서버 Monitoring과 같은가?

A. 아니다. 일반 Monitoring은 시스템 상태 중심이고, AI Observability는 Prompt, Context, Retrieval, Output, Tool Call, 품질 평가까지 포함한다.

Q. AI Observability의 핵심은 무엇인가?

A. AI 시스템이 어떤 입력과 Context를 기반으로 어떤 판단과 출력을 만들었는지 추적하는 것이다.

---

# 2. Scope

## 2.1 포함 범위

### [개념]

AI Observability Domain 문서는 AI 시스템의 실행 흐름, 품질, 비용, 지연, 오류, 평가 결과를 관측하고 분석하기 위한 Trace, Metric, Log, Evaluation, Feedback 기준을 포함한다.

---

### [핵심]

포함 범위:

- AI Observability 개념
- LLM Observability
- RAG Observability
- Agent Observability
- Tool Calling Observability
- Memory Observability
- Prompt Trace
- Context Trace
- Retrieval Trace
- Generation Trace
- Evaluation Trace
- Feedback Trace
- Token Usage
- Cost Tracking
- Latency Tracking
- Hallucination Detection
- Groundedness Evaluation
- Faithfulness Evaluation
- Format Compliance
- Safety Monitoring
- Drift Detection
- Failure Analysis
- Alerting
- Dashboard
- Feedback Loop

제외 범위:

- 일반 서버 Monitoring 전체 설명
- Kubernetes Observability 전체 매뉴얼
- 특정 SaaS Observability 도구 API 전체 복붙
- 단순 로그 수집만 설명
- LLM 평가 이론만 장문 설명
- 모델 학습 수학 상세
- Vector DB 운영 전체 상세
- 보안 감사 로그 전체 문서

---

### [실무]

AI Observability 문서는 아래 질문에 답할 수 있어야 한다.

- 이 답변은 어떤 Prompt와 Context로 생성되었는가?
- 어떤 문서 Chunk가 검색되었는가?
- 검색된 Context가 실제 답변에 사용되었는가?
- Tool Calling은 왜 호출되었는가?
- Tool Calling 결과는 검증되었는가?
- Agent Workflow는 어느 단계에서 실패했는가?
- Memory가 답변에 어떤 영향을 주었는가?
- Hallucination이 발생했는가?
- Groundedness가 낮아진 원인은 무엇인가?
- 비용과 지연이 증가한 원인은 무엇인가?
- 품질 저하를 어떻게 감지하고 개선할 것인가?

---

### [FAQ]

Q. AI Observability 문서에 일반 로그 수집 방법만 넣어도 되는가?

A. 아니다. LLM Prompt, Retrieval, Context, Tool Call, Agent State, Evaluation까지 함께 추적해야 한다.

Q. AI Observability는 MLOps와 중복되는가?

A. 일부 연결되지만, AI Observability는 LLM / RAG / Agent 실행 흐름과 품질 추적에 더 집중한다.

Q. AI Observability는 왜 필요한가?

A. AI 출력은 비결정성과 복잡한 Context에 영향을 받으므로 원인 추적 없이는 품질 개선이 어렵기 때문이다.

---

# 3. Section Priority

## 3.1 필수 섹션 규칙

### [개념]

AI Observability 문서는 모든 주요 Chunk에 `[개념]`, `[핵심]`, `[실무]`, `[FAQ]`를 우선 적용한다.

흐름 추적이 필요한 주제는 `[Flow]`를 추가한다.

품질 판단이 필요한 주제는 `[Evaluation]`, `[Metric]`, `[Checklist]`를 추가한다.

장애 대응이 필요한 주제는 `[Troubleshooting]`을 추가한다.

운영 비교가 필요한 주제는 `[Comparison]`을 추가한다.

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
- [Evaluation]
- [Troubleshooting]
- [Comparison]

Optional:

- [Trace Schema]
- [Metric]
- [Dashboard]
- [Alert Rule]
- [Review Point]
- [Anti-Pattern]

---

### [실무]

AI Observability 문서는 단순 개념 설명보다 추적 기준과 문제 분석 기준을 우선한다.

각 문서는 아래 정보 중 최소 2개 이상을 포함한다.

- Trace 대상
- Metric 기준
- Log 기준
- Evaluation 기준
- Alert 기준
- Failure Analysis 기준
- Dashboard 기준
- Feedback Loop 기준
- Troubleshooting 기준

---

### [FAQ]

Q. AI Observability 문서에 Trace Schema가 필요한가?

A. 필요하다. 어떤 입력, Context, Tool Call, Output, Metric을 연결해 추적할지 정의해야 하기 때문이다.

Q. Evaluation 섹션은 왜 필요한가?

A. AI Observability는 단순 실행 성공이 아니라 답변 품질과 근거성을 관측해야 하기 때문이다.

Q. Troubleshooting 섹션이 필요한 이유는?

A. AI 시스템에서는 Retrieval 실패, Context 누락, Tool Call 오류, Hallucination, 비용 증가가 자주 발생하기 때문이다.

---

# 4. Core Concept Rules

## 4.1 AI Observability 핵심 개념 작성 규칙

### [개념]

AI Observability 핵심 개념은 일반 Logging, Monitoring, APM, MLOps와 구분되도록 작성한다.

AI Observability는 AI 출력의 품질과 원인을 설명하기 위해 Prompt, Context, Retrieval, Model Output, Tool Call, Agent State, Evaluation Result를 연결해서 관측하는 구조이다.

---

### [핵심]

반드시 포함할 개념:

- AI Observability
- LLM Observability
- RAG Observability
- Agent Observability
- Trace
- Metrics
- Logs
- Span
- Prompt Trace
- Context Trace
- Retrieval Trace
- Tool Call Trace
- Agent Workflow Trace
- Memory Trace
- Evaluation Trace
- Feedback Loop
- Hallucination
- Groundedness
- Faithfulness
- Latency
- Cost
- Token Usage

용어 통일:

- AI Observability
- LLM Trace
- RAG Trace
- Agent Trace
- Tool Call Trace
- Memory Trace
- Prompt Version
- Context Snapshot
- Retrieval Result
- Evaluation Result
- Groundedness
- Hallucination Rate
- Token Usage
- Cost Tracking

---

### [실무]

AI Observability 설명은 아래 구분을 반드시 포함한다.

```text
Logging
→ 이벤트와 오류 기록

Monitoring
→ 시스템 상태와 Metric 관측

APM
→ 애플리케이션 성능 추적

MLOps
→ 모델 Lifecycle 운영

AI Observability
→ Prompt, Context, Retrieval, Tool Call, Agent Workflow, Output, Evaluation을 연결해 AI 품질 원인을 추적
```

AI Observability 문서는 “로그를 남긴다” 수준에서 멈추면 안 된다.

Agent가 어떤 Trace를 수집하고, 어떤 Metric을 보고, 어떤 원인 분석을 수행해야 하는지 판단할 수 있어야 한다.

---

### [FAQ]

Q. AI Observability란?

A. LLM, RAG, Agent 시스템의 Prompt, Context, Retrieval, Tool Call, Output, Evaluation을 추적해 품질과 오류 원인을 분석하는 운영 체계이다.

Q. AI Observability와 Monitoring의 차이는?

A. Monitoring은 상태와 Metric 중심이고, AI Observability는 AI 출력이 생성된 과정과 품질 근거를 추적한다.

Q. AI Observability에서 가장 중요한 Trace는?

A. Prompt Trace, Context Trace, Retrieval Trace, Tool Call Trace, Agent Workflow Trace, Evaluation Trace가 중요하다.

---

# 5. Trace Design Rules

## 5.1 AI Trace 설계 규칙

### [개념]

Trace Design은 AI 시스템의 요청이 어떤 단계를 거쳐 최종 출력으로 이어졌는지 추적 가능한 구조를 설계하는 과정이다.

AI Observability에서 Trace는 문제 원인 분석의 핵심이다.

---

### [핵심]

Trace 구성 요소:

- traceId
- sessionId
- userRequestId
- workflowId
- agentId
- spanId
- parentSpanId
- timestamp
- input
- output
- status
- latency
- errorType
- metadata

Trace 대상:

- User Request
- Prompt Assembly
- Retrieval
- Context Selection
- Model Inference
- Tool Call
- Agent Step
- Memory Retrieval
- Evaluation
- Final Output

---

### [실무]

Trace Flow 예시:

```text
User Request
→ Prompt Assembly Span
→ Retrieval Span
→ Context Selection Span
→ LLM Inference Span
→ Tool Call Span
→ Evaluation Span
→ Final Output Span
```

Trace Schema 예시:

```text
traceId: TRACE-001
workflowId: WF-001
agentName: PM Agent
spanType: retrieval
input: userQuery
output: retrievedChunks
latencyMs: 230
status: success
metadata: topK=10, domain=RAG
```

Trace는 너무 자세한 원문 저장보다 원인 분석에 필요한 구조화 정보를 우선한다.

---

### [FAQ]

Q. Trace Design은 왜 필요한가?

A. AI 응답이 어떤 단계와 Context를 거쳐 생성되었는지 추적해야 문제 원인을 분석할 수 있기 때문이다.

Q. 모든 원문을 Trace에 저장해야 하는가?

A. 아니다. 민감정보를 피하고 원인 분석에 필요한 요약, ID, Metadata 중심으로 저장한다.

Q. traceId와 workflowId는 왜 필요한가?

A. 하나의 사용자 요청이 여러 Agent, Tool, Retrieval 단계로 나뉘므로 전체 흐름을 연결하기 위해 필요하다.

---

# 6. LLM Observability Rules

## 6.1 LLM 호출 관측 규칙

### [개념]

LLM Observability는 모델 호출의 Prompt, System Instruction, Context, Output, Token 사용량, Latency, Error, Evaluation 결과를 추적하는 구조이다.

LLM 호출은 AI 시스템 품질과 비용의 핵심 관측 지점이다.

---

### [핵심]

LLM Trace 대상:

- modelName
- modelVersion
- provider
- runtime
- systemPromptVersion
- userPrompt
- promptTemplateVersion
- contextSnapshot
- output
- temperature
- maxTokens
- inputTokens
- outputTokens
- totalTokens
- latency
- cost
- finishReason
- errorType

품질 Metric:

- instructionFollowing
- formatCompliance
- answerCompleteness
- hallucinationRate
- groundedness
- safetyViolationRate
- userFeedbackScore

---

### [실무]

LLM Observability Checklist:

```md
### [Checklist]

- modelName과 modelVersion이 기록되었는가?
- Prompt Template Version이 기록되었는가?
- Context Snapshot 또는 Context ID가 기록되었는가?
- Token 사용량이 기록되었는가?
- Latency와 Cost가 기록되었는가?
- Output Format 준수 여부가 평가되었는가?
- Hallucination 또는 Groundedness 평가가 연결되었는가?
```

LLM 호출 결과만 저장하지 않는다.

입력 Prompt, Context, 모델 설정, Output, 평가 결과를 함께 연결해야 한다.

---

### [FAQ]

Q. LLM Observability에서 무엇을 기록해야 하는가?

A. 모델 버전, Prompt, Context, Output, Token 사용량, Latency, Cost, 오류, 평가 결과를 기록해야 한다.

Q. Prompt Version은 왜 필요한가?

A. Prompt 변경이 답변 품질 변화의 원인일 수 있으므로 버전 추적이 필요하다.

Q. LLM Output만 저장하면 충분한가?

A. 아니다. Output이 어떤 Prompt와 Context에서 나왔는지 함께 추적해야 한다.

---

# 7. Prompt Observability Rules

## 7.1 Prompt Trace 작성 규칙

### [개념]

Prompt Observability는 System Prompt, Developer Instruction, User Prompt, Prompt Template, Few-shot Example, Context Assembly 결과를 추적하는 구조이다.

Prompt 변경은 AI 시스템 품질에 직접 영향을 준다.

---

### [핵심]

Prompt Trace 대상:

- systemPromptVersion
- developerInstructionVersion
- promptTemplateVersion
- userPrompt
- rewrittenPrompt
- fewShotExamples
- insertedContext
- outputFormatInstruction
- safetyInstruction
- toolInstruction
- agentRoleInstruction

Prompt 변경 추적 항목:

- 변경일
- 변경자
- 변경 이유
- 영향 범위
- 평가 결과
- Rollback 가능 여부

---

### [실무]

Prompt Trace 예시:

```text
promptTemplateId: RAG-DOC-GEN-V3
systemPromptVersion: SYS-2026-06
outputFormatInstruction: writing block required
domainRulesApplied: true
evaluationResult: formatCompliance=0.98
```

Prompt Observability는 Prompt 자체만 기록하는 것이 아니라, Prompt 변경 후 품질 Metric 변화를 함께 추적한다.

---

### [FAQ]

Q. Prompt Observability는 왜 필요한가?

A. Prompt 변경이 답변 품질, 출력 형식, 안전성, 비용에 영향을 줄 수 있기 때문이다.

Q. Prompt Template Version을 관리해야 하는가?

A. 관리해야 한다. 같은 모델도 Prompt Version에 따라 출력이 달라질 수 있다.

Q. User Prompt를 그대로 저장해도 되는가?

A. 민감정보가 포함될 수 있으므로 마스킹, 요약, 접근 제한 기준이 필요하다.

---

# 8. RAG Observability Rules

## 8.1 RAG Retrieval 관측 규칙

### [개념]

RAG Observability는 Query 변환, 문서 검색, Chunk 선택, Context 구성, 답변 Grounding을 추적하는 구조이다.

RAG 품질 문제는 LLM 문제가 아니라 Retrieval 문제일 수 있다.

---

### [핵심]

RAG Trace 대상:

- originalQuery
- rewrittenQuery
- queryType
- embeddingModel
- embeddingModelVersion
- vectorIndexVersion
- topK
- retrievedChunks
- selectedChunks
- rejectedChunks
- rerankingScore
- sourceDocument
- chunkId
- retrievalLatency
- contextAssembly
- groundednessScore
- citationAccuracy

RAG 품질 Metric:

- retrievalHitRate
- retrievalPrecision
- retrievalRecall
- contextRelevance
- groundedness
- citationAccuracy
- answerFaithfulness
- missingContextRate

---

### [실무]

RAG Observability Flow:

```text
User Query
→ Query Rewrite
→ Embedding
→ Vector Search
→ Re-Ranking
→ Chunk Selection
→ Context Assembly
→ LLM Answer
→ Groundedness Evaluation
```

RAG Trace 예시:

```text
query: JWT 인증 흐름 설명
embeddingModel: bge-m3
topK: 10
retrievedChunks: Security_Advanced_Part04_JWT.md
selectedChunks: 4
groundednessScore: high
missingContext: false
```

RAG 답변 품질이 낮으면 먼저 검색된 Chunk와 선택된 Context를 확인한다.

---

### [FAQ]

Q. RAG Observability는 왜 필요한가?

A. 답변 오류가 검색 실패, 잘못된 Chunk 선택, Context 누락에서 발생할 수 있기 때문이다.

Q. retrievedChunks와 selectedChunks를 구분해야 하는가?

A. 구분해야 한다. 검색된 Chunk 중 실제 Context에 포함된 Chunk만 답변에 영향을 준다.

Q. Groundedness는 무엇인가?

A. 최종 답변이 검색된 문서 근거에 얼마나 충실한지 나타내는 품질 기준이다.

---

# 9. Agent Observability Rules

## 9.1 Agent Workflow 관측 규칙

### [개념]

Agent Observability는 Agent가 작업을 어떻게 분해하고, 어떤 도구를 호출하고, 어떤 상태를 업데이트하고, 어떤 검증을 거쳐 최종 결과를 생성했는지 추적하는 구조이다.

Agent 시스템은 단일 LLM 호출보다 실행 흐름이 복잡하므로 Agent Trace가 필수이다.

---

### [핵심]

Agent Trace 대상:

- workflowId
- agentName
- agentRole
- taskId
- taskGoal
- routingDecision
- agentInput
- agentOutput
- stateUpdate
- toolCall
- retrievalCall
- validationResult
- retryCount
- fallbackReason
- finalDecision

Agent Metric:

- workflowSuccessRate
- taskCompletionRate
- routingAccuracy
- toolCallSuccessRate
- retryCount
- validationFailureRate
- fixLoopCount
- finalOutputQuality
- humanReviewRate

---

### [실무]

Agent Workflow Trace 예시:

```text
workflowId: WF-RAG-001
agentName: PM Agent
task: Domain Rules 생성
routingDecision: AI/ML Agent
reviewAgentResult: pass
retryCount: 0
finalOutputStatus: completed
```

Agent Observability는 각 Agent의 출력만 보지 않는다.

작업 분해, Routing, Tool Calling, Review, Fix Loop까지 연결해서 본다.

---

### [FAQ]

Q. Agent Observability는 왜 필요한가?

A. Agent Workflow는 여러 단계와 도구 호출로 구성되므로 실패 원인을 찾으려면 단계별 Trace가 필요하다.

Q. Agent Routing도 관측해야 하는가?

A. 해야 한다. 잘못된 Agent에게 작업이 전달되면 전체 품질이 낮아진다.

Q. retryCount는 왜 중요한가?

A. 반복 재시도 증가는 Workflow 불안정, Retrieval 실패, Tool 오류, 출력 형식 문제의 신호일 수 있다.

---

# 10. Tool Calling Observability Rules

## 10.1 Tool Call Trace 작성 규칙

### [개념]

Tool Calling Observability는 Agent가 외부 도구, API, 코드 실행기, 검색 도구, 파일 도구, DB 도구를 호출한 과정을 추적하는 구조이다.

Tool Calling은 상태 변경이나 외부 결과에 영향을 주므로 입력, 출력, 오류, 검증 결과를 기록해야 한다.

---

### [핵심]

Tool Call Trace 대상:

- toolName
- toolVersion
- callerAgent
- toolInput
- toolOutput
- status
- latency
- errorType
- retryCount
- permissionCheck
- validationResult
- stateChange
- rollbackAvailable
- cost

Tool Call Metric:

- toolCallSuccessRate
- toolCallErrorRate
- toolLatency
- invalidInputRate
- invalidOutputRate
- retryRate
- stateChangeFailureRate

---

### [실무]

Tool Call Trace 예시:

```text
toolName: file_search
callerAgent: Review Agent
toolInput: Domain Rules query
toolOutput: retrieved file lines
status: success
latencyMs: 180
validationResult: usable
```

상태 변경 Tool은 더 강한 관측이 필요하다.

```text
상태 변경 Tool:
- Email Send
- Calendar Create
- Database Update
- File Delete
- Deployment Execute
```

상태 변경 Tool은 승인 여부, 실행 결과, Rollback 가능 여부를 함께 기록한다.

---

### [FAQ]

Q. Tool Calling Observability는 왜 필요한가?

A. Tool 호출 실패, 잘못된 입력, 잘못된 결과 사용, 상태 변경 오류를 추적하기 위해 필요하다.

Q. Tool Output을 바로 신뢰해도 되는가?

A. 아니다. Tool Output은 검증 결과와 함께 기록하고 필요한 경우 Review Agent가 확인해야 한다.

Q. 상태 변경 Tool은 무엇을 추가로 기록해야 하는가?

A. 승인 여부, 변경 대상, 실행 결과, 실패 원인, Rollback 가능 여부를 기록해야 한다.

---

# 11. Memory Observability Rules

## 11.1 Memory Usage Trace 작성 규칙

### [개념]

Memory Observability는 Long-Term Memory, Short-Term Memory, Agent State가 AI 출력에 어떤 영향을 주었는지 추적하는 구조이다.

Memory는 개인화와 프로젝트 맥락에 영향을 주므로 사용 근거와 최신성 확인이 필요하다.

---

### [핵심]

Memory Trace 대상:

- memoryId
- memoryType
- memoryQuery
- retrievedMemory
- selectedMemory
- rejectedMemory
- freshness
- confidence
- sensitivity
- usageReason
- conflictDetected
- appliedToOutput
- updateCandidate
- deletionCandidate

Memory 품질 Metric:

- memoryRetrievalPrecision
- staleMemoryRate
- memoryConflictRate
- memoryUsefulness
- privacyRiskRate
- memoryUpdateRate
- memoryDeletionCompliance

---

### [실무]

Memory Trace 예시:

```text
memoryType: User Preference Memory
memoryQuery: RAG document output format
freshness: current
confidence: high
appliedToOutput: writing block format applied
conflictDetected: false
```

Memory는 현재 사용자 요청보다 우선하지 않는다.

Memory 사용 Trace에는 현재 요청과 충돌 여부를 포함해야 한다.

---

### [FAQ]

Q. Memory Observability는 왜 필요한가?

A. 어떤 Memory가 답변에 영향을 주었는지 추적하고 오래되거나 잘못된 Memory 사용을 방지하기 위해 필요하다.

Q. Memory Freshness를 기록해야 하는가?

A. 기록해야 한다. 오래된 Memory가 현재 작업에 잘못 적용될 수 있기 때문이다.

Q. Memory Conflict는 무엇인가?

A. 현재 사용자 요청, Project Progress, Domain Rules, 기존 Memory가 서로 충돌하는 상황이다.

---

# 12. Evaluation Observability Rules

## 12.1 Evaluation Trace 작성 규칙

### [개념]

Evaluation Observability는 AI 출력이 품질 기준을 만족하는지 평가한 결과를 추적하는 구조이다.

AI Observability는 실행 Trace뿐 아니라 품질 평가 Trace까지 포함해야 한다.

---

### [핵심]

Evaluation 대상:

- Answer Quality
- Groundedness
- Faithfulness
- Hallucination
- Format Compliance
- Instruction Following
- Completeness
- Relevance
- Safety Compliance
- Tool Call Correctness
- RAG Context Usage
- Agent Workflow Success
- User Satisfaction

Evaluation Trace 대상:

- evaluationId
- evaluationType
- evaluator
- evaluationDataset
- metricName
- metricValue
- passFail
- failureReason
- improvementAction

---

### [실무]

Evaluation Trace 예시:

```text
evaluationId: EVAL-001
target: RAG answer
metric: groundedness
result: pass
failureReason: none
evaluator: Review Agent
```

Evaluation은 자동 평가와 Human Review를 함께 사용할 수 있다.

LLM Judge를 사용할 경우 Judge Prompt Version과 평가 기준도 추적해야 한다.

---

### [FAQ]

Q. Evaluation Observability는 왜 필요한가?

A. AI 시스템의 출력 품질이 실제 기준을 만족하는지 추적하고 개선하기 위해 필요하다.

Q. Groundedness와 Faithfulness는 같은가?

A. 비슷하지만 Groundedness는 검색 근거 기반 여부, Faithfulness는 제공된 Context와 답변의 일치성을 강조한다.

Q. LLM Judge도 추적해야 하는가?

A. 해야 한다. Judge Model, Judge Prompt, 평가 기준이 결과에 영향을 줄 수 있기 때문이다.

---

# 13. Metrics Rules

## 13.1 AI Observability Metric 작성 규칙

### [개념]

AI Observability Metric은 AI 시스템의 품질, 비용, 지연, 안정성, 검색 품질, Agent 성공률을 수치로 관측하는 기준이다.

Metric은 운영 판단과 Alert의 근거가 된다.

---

### [핵심]

LLM Metric:

- inputTokens
- outputTokens
- totalTokens
- latency
- cost
- errorRate
- formatCompliance
- hallucinationRate

RAG Metric:

- retrievalHitRate
- retrievalPrecision
- retrievalRecall
- contextRelevance
- groundedness
- citationAccuracy
- missingContextRate

Agent Metric:

- workflowSuccessRate
- toolCallSuccessRate
- retryCount
- fixLoopCount
- routingAccuracy
- humanReviewRate

System Metric:

- latency
- throughput
- memoryUsage
- cpuUsage
- gpuUsage
- queueLength
- timeoutRate

---

### [실무]

Metric 작성 기준:

```text
품질 Metric:
- groundedness
- faithfulness
- formatCompliance
- answerCompleteness

운영 Metric:
- latency
- cost
- tokenUsage
- errorRate

Agent Metric:
- workflowSuccessRate
- toolCallErrorRate
- retryCount
```

Metric은 단일 값만 보지 않는다.

품질, 비용, 지연, 안정성을 함께 본다.

---

### [FAQ]

Q. AI Observability에서 가장 중요한 Metric은?

A. 사용 목적에 따라 다르지만 Groundedness, Format Compliance, Hallucination Rate, Latency, Cost, Workflow Success Rate가 중요하다.

Q. Token Usage는 왜 추적해야 하는가?

A. 비용, 지연, Context Overflow, Prompt 비효율의 원인을 분석하기 위해 필요하다.

Q. Metric이 많을수록 좋은가?

A. 아니다. 운영 의사결정에 필요한 핵심 Metric을 우선해야 한다.

---

# 14. Hallucination Monitoring Rules

## 14.1 Hallucination 감지 규칙

### [개념]

Hallucination Monitoring은 AI가 근거 없는 내용, 검색 Context와 불일치하는 내용, 존재하지 않는 사실을 생성하는지 감지하는 구조이다.

RAG / Agent 시스템에서는 Hallucination 감지가 품질 관리의 핵심이다.

---

### [핵심]

Hallucination 유형:

- Source 없는 주장
- 검색 Context와 불일치
- 문서에 없는 내용 단정
- 존재하지 않는 API / 코드 / 파일 생성
- 잘못된 숫자 / 날짜 생성
- Tool 결과 왜곡
- Memory 기반 과잉 추론
- 불확실한 내용을 확정적으로 표현

감지 기준:

- 답변과 Context 비교
- Citation 존재 여부
- Tool Result와 Output 비교
- RAG 문서 내 근거 확인
- Review Agent 검증
- 사용자 피드백 반영

---

### [실무]

Hallucination Detection Checklist:

```md
### [Checklist]

- 답변의 핵심 주장에 근거가 있는가?
- 검색된 Context와 답변이 일치하는가?
- 문서에 없는 내용을 단정하지 않았는가?
- Tool 결과를 왜곡하지 않았는가?
- 불확실한 정보는 불확실하다고 표시했는가?
- 존재하지 않는 코드나 API를 생성하지 않았는가?
```

Hallucination은 모델 문제만이 아니다.

Retrieval 실패, Context 누락, Prompt 문제, Memory 오류, Tool Result 검증 실패가 원인일 수 있다.

---

### [FAQ]

Q. Hallucination이란?

A. AI가 근거 없는 내용이나 실제 Context와 일치하지 않는 내용을 사실처럼 생성하는 현상이다.

Q. Hallucination은 어떻게 감지하는가?

A. 답변을 검색 Context, Tool Result, Source Document, Review Checklist와 비교해 감지한다.

Q. Hallucination이 발생하면 무엇을 확인해야 하는가?

A. Retrieval 결과, Context 구성, Prompt, Memory 사용, Tool Result 검증, 모델 설정을 확인해야 한다.

---

# 15. Groundedness Rules

## 15.1 Groundedness 관측 규칙

### [개념]

Groundedness는 AI 답변이 제공된 근거, 검색 문서, Tool Result, 사용자 입력에 기반하고 있는 정도이다.

RAG 시스템에서는 Groundedness가 답변 신뢰도를 결정한다.

---

### [핵심]

Groundedness 확인 대상:

- 답변 핵심 주장
- 인용된 Source
- 검색된 Chunk
- Tool Result
- Memory 적용 내용
- 코드 예제
- 숫자 / 날짜 / 버전
- 최종 결론

Groundedness 저하 원인:

- 관련 없는 Chunk 검색
- 필요한 Chunk 누락
- Context 과다로 핵심 근거 희석
- LLM이 Context를 무시
- Citation 누락
- Tool Result 미검증
- Memory와 문서 충돌

---

### [실무]

Groundedness Evaluation Flow:

```text
Answer
→ Claim Extraction
→ Evidence Matching
→ Source Verification
→ Conflict Detection
→ Groundedness Score
→ Pass / Fail
```

Groundedness Checklist:

```md
### [Checklist]

- 핵심 주장마다 근거가 있는가?
- 근거 Chunk가 실제로 답변 내용과 연결되는가?
- 인용된 Source가 답변을 지원하는가?
- Tool Result와 답변이 일치하는가?
- 근거 없는 일반화를 하지 않았는가?
```

---

### [FAQ]

Q. Groundedness란?

A. AI 답변이 제공된 문서, Tool Result, 사용자 입력 같은 근거에 기반하는 정도이다.

Q. Groundedness와 Citation은 같은가?

A. 아니다. Citation은 출처 표시이고, Groundedness는 답변 내용이 실제 근거와 일치하는지 평가한다.

Q. Groundedness가 낮으면 어떻게 해야 하는가?

A. Retrieval, Context Selection, Prompt, Citation, Answer Synthesis 과정을 점검해야 한다.

---

# 16. Cost and Latency Rules

## 16.1 비용 / 지연 관측 규칙

### [개념]

Cost and Latency Observability는 AI 시스템의 Token 사용량, 모델 호출 비용, Tool 호출 비용, 응답 지연, 병목 구간을 추적하는 구조이다.

AI 시스템은 품질뿐 아니라 운영 비용과 응답 시간도 관리해야 한다.

---

### [핵심]

Cost 대상:

- inputTokens
- outputTokens
- totalTokens
- modelCallCost
- embeddingCost
- rerankingCost
- toolCallCost
- storageCost
- vectorDbCost
- fineTuningCost
- servingCost

Latency 대상:

- totalLatency
- retrievalLatency
- embeddingLatency
- rerankingLatency
- modelLatency
- toolCallLatency
- agentStepLatency
- queueLatency
- postprocessingLatency

---

### [실무]

Latency Trace 예시:

```text
totalLatencyMs: 4200
retrievalLatencyMs: 300
rerankingLatencyMs: 180
modelLatencyMs: 3200
toolCallLatencyMs: 400
postprocessingLatencyMs: 120
```

비용 최적화 판단 기준:

```text
비용 증가 원인:
- Prompt가 너무 김
- Context Chunk가 과다함
- Top-K가 너무 큼
- Re-Ranking 남발
- Tool Calling 중복
- Agent Step 과다
- Retry 과다
```

비용 최적화는 품질 저하 없이 수행해야 한다.

---

### [FAQ]

Q. AI 시스템에서 Cost Tracking이 중요한 이유는?

A. Token, Tool, Retrieval, Serving 비용이 누적되면 운영 비용이 빠르게 증가할 수 있기 때문이다.

Q. Latency 병목은 어떻게 찾는가?

A. Retrieval, Reranking, Model Inference, Tool Call, Agent Step별 Latency를 분리해 추적한다.

Q. 비용을 줄이려면 Context를 무조건 줄이면 되는가?

A. 아니다. Context를 줄이면 Groundedness가 떨어질 수 있으므로 품질 평가와 함께 조정해야 한다.

---

# 17. Drift and Regression Rules

## 17.1 AI 품질 Drift / Regression 관측 규칙

### [개념]

AI Drift와 Regression은 시간이 지나거나 Prompt, 모델, 문서, Index, Tool, Memory가 변경되면서 AI 시스템 품질이 저하되는 현상이다.

AI Observability는 품질 저하를 조기에 감지해야 한다.

---

### [핵심]

Drift 유형:

- Prompt Drift
- Retrieval Drift
- Embedding Drift
- Model Drift
- Tool Behavior Drift
- Memory Drift
- User Query Drift
- Evaluation Drift
- Cost Drift
- Latency Drift

Regression 유형:

- Format Compliance 저하
- Groundedness 저하
- Tool Calling 오류 증가
- Retrieval Hit Rate 저하
- Hallucination 증가
- Agent Workflow 실패 증가
- 한국어 응답 품질 저하
- 코드 생성 품질 저하

---

### [실무]

Drift Detection Flow:

```text
Baseline Metric
→ Current Metric
→ Difference Detection
→ Alert
→ Root Cause Analysis
→ Fix or Rollback
```

Regression Checklist:

```md
### [Checklist]

- Prompt 변경 후 품질이 떨어졌는가?
- Embedding Model 변경 후 검색 품질이 낮아졌는가?
- Vector Index 재생성 후 Top-K 결과가 바뀌었는가?
- 모델 변경 후 출력 형식이 깨지는가?
- Tool 업데이트 후 오류율이 증가했는가?
- Memory 변경 후 오래된 정보가 사용되는가?
```

---

### [FAQ]

Q. AI Drift란?

A. Prompt, Retrieval, Model, Tool, Memory, 사용자 Query 변화로 AI 시스템 품질이 시간이 지나며 변하는 현상이다.

Q. Regression은 무엇인가?

A. 이전에는 잘 되던 기능이나 품질이 변경 이후 나빠지는 현상이다.

Q. Drift가 감지되면 바로 모델을 바꿔야 하는가?

A. 아니다. Prompt, Retrieval, Index, Tool, Memory, Evaluation 기준을 먼저 확인해야 한다.

---

# 18. Alerting Rules

## 18.1 AI Alert 기준 작성 규칙

### [개념]

Alerting은 AI 시스템의 품질, 비용, 지연, 오류, 안전성 문제가 임계값을 넘었을 때 운영자나 Agent에게 알리는 구조이다.

AI Alert는 서버 장애뿐 아니라 품질 저하와 안전 문제도 포함해야 한다.

---

### [핵심]

Alert 대상:

- Error Rate 증가
- Latency 증가
- Cost 급증
- Hallucination Rate 증가
- Groundedness 저하
- Retrieval Hit Rate 저하
- Tool Call Error 증가
- Agent Workflow Failure 증가
- Format Compliance 저하
- Safety Violation 발생
- Memory Conflict 증가
- OOM / Runtime Crash
- 사용자 부정 피드백 증가

Alert 우선순위:

- P0: 보안 / 개인정보 / 위험 출력 / Production 장애
- P1: 대규모 품질 저하 / Tool 실패 / RAG 검색 실패
- P2: 비용 증가 / Latency 증가 / Format 오류 증가
- P3: 경미한 품질 변동 / 개선 필요 신호

---

### [실무]

Alert Rule 예시:

```text
Rule:
- groundednessScore가 기준 이하로 3회 연속 발생

Action:
- Review Agent 검토 요청
- Retrieval Trace 확인
- 최근 문서 / Index 변경 확인
```

Alert는 너무 민감하면 Noise가 증가하고, 너무 둔감하면 장애 감지가 늦어진다.

품질 Alert는 운영 Metric과 Evaluation Metric을 함께 사용한다.

---

### [FAQ]

Q. AI Alert는 일반 서버 Alert와 무엇이 다른가?

A. 서버 상태뿐 아니라 Hallucination, Groundedness, Retrieval 품질, Tool Call 오류, Agent 실패도 감지해야 한다.

Q. Groundedness 저하도 Alert 대상인가?

A. 그렇다. RAG 기반 시스템에서 Groundedness 저하는 신뢰도 저하로 이어진다.

Q. Alert가 너무 많으면 어떻게 해야 하는가?

A. 우선순위, 임계값, 집계 기준, 중복 제거를 조정해야 한다.

---

# 19. Dashboard Rules

## 19.1 AI Observability Dashboard 작성 규칙

### [개념]

AI Observability Dashboard는 AI 시스템의 품질, 비용, 지연, Retrieval, Tool Calling, Agent Workflow, Evaluation 상태를 한눈에 확인하는 화면이다.

Dashboard는 운영 판단과 장애 분석을 돕기 위한 구조로 설계한다.

---

### [핵심]

Dashboard 구성 요소:

- Request Volume
- Success Rate
- Error Rate
- Latency
- Token Usage
- Cost
- Model Usage
- Prompt Version
- Retrieval Hit Rate
- Groundedness Score
- Hallucination Rate
- Tool Call Success Rate
- Agent Workflow Success Rate
- Retry Count
- User Feedback
- Alert Status

Dashboard 유형:

- Executive Summary
- LLM Dashboard
- RAG Dashboard
- Agent Dashboard
- Tool Dashboard
- Cost Dashboard
- Quality Dashboard
- Failure Analysis Dashboard

---

### [실무]

Dashboard 구성 예시:

```text
AI Quality Dashboard:
- groundedness
- hallucinationRate
- formatCompliance
- userFeedbackScore

RAG Dashboard:
- retrievalHitRate
- topKQuality
- missingContextRate
- vectorIndexVersion

Agent Dashboard:
- workflowSuccessRate
- toolCallErrorRate
- retryCount
- reviewFailureRate

Cost Dashboard:
- tokenUsage
- modelCallCost
- toolCallCost
- costPerRequest
```

Dashboard는 보기 좋은 차트보다 운영 의사결정에 필요한 Metric을 우선한다.

---

### [FAQ]

Q. AI Observability Dashboard에는 무엇이 있어야 하는가?

A. 품질, 비용, 지연, Retrieval, Tool Calling, Agent Workflow, Evaluation, Alert 상태를 확인할 수 있어야 한다.

Q. Dashboard에서 가장 중요한 것은?

A. 문제를 빠르게 발견하고 원인을 추적할 수 있는 Metric과 Trace 연결이다.

Q. Dashboard에 모든 Metric을 넣어야 하는가?

A. 아니다. 역할별 Dashboard를 나누고 핵심 Metric을 우선 표시한다.

---

# 20. Feedback Loop Rules

## 20.1 Feedback Loop 작성 규칙

### [개념]

Feedback Loop는 사용자 피드백, Review Agent 결과, Evaluation 결과, 운영 Metric을 기반으로 Prompt, RAG, Tool, Memory, Model, Agent Workflow를 개선하는 구조이다.

AI Observability의 최종 목적은 관측이 아니라 개선이다.

---

### [핵심]

Feedback Source:

- User Feedback
- Review Agent Feedback
- Human Review
- Evaluation Result
- Alert
- Failure Case
- Tool Error
- Retrieval Failure
- Hallucination Report
- Cost Report

개선 대상:

- Prompt
- RAG Document
- Chunk Strategy
- Embedding Model
- Retrieval Strategy
- Tool Schema
- Agent Workflow
- Memory
- Model Selection
- Fine-Tuning Dataset
- Evaluation Dataset

---

### [실무]

Feedback Loop Flow:

```text
Observation
→ Failure Case Collection
→ Root Cause Analysis
→ Improvement Target Selection
→ Fix
→ Evaluation
→ Deployment
→ Monitoring
```

Feedback는 바로 모델 학습으로 연결하지 않는다.

먼저 Prompt, RAG, Tool, Memory, Workflow 중 어떤 부분이 원인인지 분석한다.

---

### [FAQ]

Q. Feedback Loop는 왜 필요한가?

A. 관측된 품질 문제를 실제 개선으로 연결해야 AI 시스템 품질이 지속적으로 좋아지기 때문이다.

Q. 사용자 피드백은 어떻게 사용해야 하는가?

A. 실패 사례로 분류하고 원인을 분석한 뒤 Prompt, RAG, Tool, Memory, Model 개선에 반영한다.

Q. 모든 문제를 Fine-Tuning으로 해결해야 하는가?

A. 아니다. Prompt, RAG, Tool Schema, Memory, Agent Workflow 개선이 먼저일 수 있다.

---

# 21. Privacy and Security Rules

## 21.1 AI Observability Privacy / Security 규칙

### [개념]

AI Observability는 Prompt, User Input, Context, Tool Result, Memory, Output을 추적하므로 개인정보와 민감정보 노출 위험이 있다.

관측 가능성과 개인정보 보호의 균형이 필요하다.

---

### [핵심]

주의 대상:

- 개인정보
- 민감정보
- API Key
- Access Token
- Refresh Token
- Password
- Secret
- 개인 문서
- 이메일 내용
- 결제 정보
- 상세 위치
- 내부 코드
- 기밀 문서
- 사용자 식별자

보안 기준:

- 민감정보 마스킹
- Trace 접근 권한 제한
- Log Retention 정책
- 암호화
- Audit Log
- 최소 수집
- 목적 기반 수집
- 삭제 요청 반영
- Production Trace 접근 통제

---

### [실무]

Privacy Checklist:

```md
### [Checklist]

- Prompt와 Output에 민감정보가 포함되지 않았는가?
- API Key와 Token이 마스킹되었는가?
- Tool Result에 개인정보가 포함되지 않았는가?
- Trace 접근 권한이 제한되었는가?
- Log Retention 기간이 정의되었는가?
- 삭제 요청을 반영할 수 있는가?
```

AI Observability는 모든 것을 저장하는 것이 아니다.

문제 분석에 필요한 최소 정보를 안전하게 저장하는 것이 원칙이다.

---

### [FAQ]

Q. AI Observability에서 Privacy가 중요한 이유는?

A. Prompt, Context, Tool Result, Memory에 민감정보가 포함될 수 있기 때문이다.

Q. API Key를 Trace에 저장해도 되는가?

A. 안 된다. API Key, Token, Password는 마스킹하거나 저장하지 않아야 한다.

Q. 모든 Prompt를 원문 그대로 저장해야 하는가?

A. 아니다. 민감정보 위험이 있으므로 요약, 마스킹, 접근 제한 기준이 필요하다.

---

# 22. Troubleshooting Rules

## 22.1 AI Observability 장애 대응 작성 규칙

### [개념]

AI Observability Troubleshooting 문서는 AI 시스템의 품질 저하, 오류 증가, 비용 증가, 지연 증가, Retrieval 실패, Agent 실패 원인을 추적하고 해결하기 위한 규칙이다.

---

### [핵심]

자주 발생하는 문제:

- Trace 누락
- Prompt Version 미기록
- Retrieval Result 미기록
- Context Snapshot 누락
- Tool Call Input / Output 미기록
- Memory 사용 근거 누락
- Evaluation Result 누락
- Groundedness 측정 없음
- Hallucination 감지 실패
- Token Cost 급증
- Latency 병목 미분리
- Agent Workflow 실패 원인 불명확
- Alert Noise 과다
- 민감정보 로그 노출
- Dashboard Metric 과다

---

### [실무]

Troubleshooting 형식:

```md
문제:
RAG 답변 품질이 갑자기 낮아짐

원인:

- Embedding Model 변경 후 Vector Index 재생성 누락
- Retrieval Trace가 없어 Top-K 결과 확인 불가
- Prompt 변경 후 Context 사용 지시 약화
- Evaluation Dataset이 최신 문서 구조를 반영하지 않음

해결:

- Retrieval Trace 확인
- Vector Index Version 확인
- Prompt Version 변경 이력 확인
- Groundedness Evaluation 수행
- 필요 시 Index 재생성 또는 Prompt Rollback
```

문제 / 원인 / 해결 형식을 기본으로 작성한다.

---

### [FAQ]

Q. AI Observability에서 가장 흔한 실패는?

A. Trace 누락, Prompt Version 미기록, Retrieval 결과 미기록, Evaluation 부재, 민감정보 로그 노출이다.

Q. 품질 저하 원인을 모르면 무엇부터 확인해야 하는가?

A. Prompt 변경, Model 변경, Retrieval 변경, Index 변경, Tool 변경, Memory 변경 이력을 확인한다.

Q. 비용이 갑자기 증가하면 무엇을 봐야 하는가?

A. Token 사용량, Context 크기, Top-K, Tool Call 중복, Retry Count, Agent Step 수를 확인해야 한다.

---

# 23. Common Mistakes

## 23.1 자주 발생하는 작성 오류

### [개념]

AI Observability 문서는 “로그를 남기는 방법”만 설명하는 문서가 아니다.

Agent가 AI 시스템의 품질, 비용, 지연, 오류, 근거성, Tool Call, Agent Workflow를 추적하고 개선할 수 있도록 작성해야 한다.

---

### [핵심]

금지 또는 주의:

- 일반 서버 로그 중심 작성
- Prompt Trace 누락
- Context Trace 누락
- Retrieval Trace 누락
- Tool Call Trace 누락
- Agent Workflow Trace 누락
- Memory Trace 누락
- Evaluation Trace 누락
- Groundedness Metric 누락
- Hallucination 감지 기준 누락
- Token / Cost 추적 누락
- Latency 단계 분리 누락
- Alert 기준 누락
- Feedback Loop 누락
- Privacy / Security 기준 누락
- Dashboard Metric 과다
- 특정 Observability 도구 사용법만 작성
- 장문 이론 설명 중심 작성
- Retrieval Queries 누락

---

### [실무]

나쁜 문서 예시:

```text
AI Observability는 AI 서비스 로그를 수집하고 대시보드로 확인하는 것이다.
```

좋은 문서 예시:

```text
AI Observability는 Prompt, Context, Retrieval, Tool Call, Agent Workflow, Memory, Output, Evaluation을 Trace로 연결하고 품질, 비용, 지연, 오류 원인을 분석하는 운영 체계이다.

Flow:
User Request
→ Prompt Trace
→ Retrieval Trace
→ Context Trace
→ LLM Trace
→ Tool Call Trace
→ Evaluation Trace
→ Feedback Loop
```

---

### [FAQ]

Q. AI Observability 문서에서 가장 피해야 할 것은?

A. 일반 로그 수집만 설명하고 Prompt, Retrieval, Context, Tool Call, Evaluation 추적을 누락하는 것이다.

Q. Metric을 많이 만들면 좋은가?

A. 아니다. 운영 판단과 품질 개선에 필요한 핵심 Metric을 우선해야 한다.

Q. Observability 도구 사용법만 작성해도 되는가?

A. 아니다. 도구보다 Trace 설계, Metric 기준, Evaluation, Failure Analysis 기준이 중요하다.

---

# 24. Document Split Rules

## 24.1 AI Observability 문서 분할 기준

### [개념]

AI Observability는 LLM, RAG, Agent, Tool, Memory, Evaluation, Cost, Security, Dashboard 범위가 넓기 때문에 Part 단위로 분리한다.

각 Part는 독립 검색 가능해야 하며, 하나의 Part는 하나의 핵심 주제를 다룬다.

---

### [핵심]

권장 문서 분할:

```text
AI_Observability_Part01_Core.md
AI_Observability_Part02_Trace_Design_LLM.md
AI_Observability_Part03_Prompt_Context_Observability.md
AI_Observability_Part04_RAG_Observability.md
AI_Observability_Part05_Agent_Tool_Memory_Observability.md
AI_Observability_Part06_Evaluation_Metrics.md
AI_Observability_Part07_Hallucination_Groundedness_Cost.md
AI_Observability_Part08_Drift_Alert_Dashboard.md
AI_Observability_Part09_Feedback_Privacy_Troubleshooting.md
```

분할 기준:

- 하나의 Part는 하나의 핵심 주제
- Trace Design과 LLM Observability는 함께 작성 가능
- Prompt와 Context는 함께 작성 권장
- RAG Observability는 독립 문서 권장
- Agent / Tool / Memory Observability는 연결 문서로 작성 가능
- Evaluation과 Metric은 함께 작성 권장
- Hallucination과 Groundedness는 함께 작성 권장
- Privacy와 Troubleshooting은 반드시 포함
- 각 Part는 FAQ 포함
- 각 Part는 Retrieval Queries 포함

---

### [실무]

AI Observability 문서 Set은 AI Expert Level과 DevOps Expert Level에서 함께 사용한다.

AI/ML Agent는 품질 평가와 Trace 구조를 참조하고, DevOps Agent는 운영 Metric, Alert, Dashboard를 참조한다.

특정 도구는 별도 문서로 분리한다.

예:

```text
AI_Observability_Domain_Rules.md
LangSmith_Domain_Rules.md
OpenTelemetry_AI_Trace_Part.md
RAGOps_Observability_Part.md
AgentOps_Observability_Part.md
LLM_Evaluation_Observability_Part.md
```

---

### [FAQ]

Q. AI Observability 문서는 몇 개 Part로 나누는 것이 좋은가?

A. 8~9개 Part를 권장한다. Core, Trace, Prompt, RAG, Agent/Tool/Memory, Evaluation, Groundedness/Cost, Drift/Dashboard, Privacy/Troubleshooting으로 분리한다.

Q. MLOps Observability 문서와 합쳐도 되는가?

A. 기본 연결은 포함하되, AI Observability는 LLM / RAG / Agent Trace 중심이므로 별도 문서로 분리하는 것이 좋다.

Q. 각 Part에도 Retrieval Queries가 필요한가?

A. 필요하다. 각 문서가 독립 검색될 수 있어야 한다.

---

# 25. Agent Usage Rules

## 25.1 Agent별 사용 기준

### [개념]

AI Observability Domain Rules는 여러 Agent가 AI 시스템 실행 흐름, 품질, 비용, 오류를 동일한 기준으로 추적하고 분석하도록 돕는다.

각 Agent는 자신의 역할에 맞는 Observability Chunk를 우선 검색한다.

---

### [핵심]

PM Agent:

- 품질 문제 원인 분류
- Trace 확인 요청
- 개선 우선순위 결정
- Human Review 필요 여부 판단
- Feedback Loop 관리

AI/ML Agent:

- LLM / RAG / Agent Evaluation 설계
- Groundedness / Hallucination Metric 설계
- Prompt / Context / Retrieval Trace 설계
- 품질 저하 원인 분석

Backend Agent:

- Trace ID 전파 구현
- LLM / Tool / RAG 호출 Logging 구현
- API 수준 Observability 구현
- Evaluation Result 저장 구조 구현

DevOps Agent:

- Metrics / Logs / Traces 수집
- Dashboard 구성
- Alert Rule 구성
- Cost / Latency 모니터링
- 운영 장애 대응

Review Agent:

- 답변 Groundedness 검토
- Hallucination 검토
- Format Compliance 검토
- Trace 누락 검토
- Privacy 로그 노출 검토

Architecture Review Agent:

- Observability Architecture 검토
- Trace Schema 검토
- AgentOps / RAGOps / LLMOps 연계 검토
- 장기 운영 확장성 검토

---

### [실무]

Agent별 검색 우선순위:

```text
PM Agent
→ Failure Analysis / Feedback Loop / Alert Priority

AI/ML Agent
→ Evaluation / Groundedness / Hallucination / RAG Trace

Backend Agent
→ Trace Schema / LLM Logging / Tool Call Logging / API Integration

DevOps Agent
→ Metrics / Dashboard / Alerting / Cost / Latency

Review Agent
→ Evaluation Trace / Groundedness / Common Mistakes / Privacy

Architecture Review Agent
→ Observability Architecture / LLMOps / RAGOps / AgentOps
```

AI Observability는 DevOps Agent만의 영역이 아니다.

AI/ML Agent, Backend Agent, Review Agent가 함께 품질과 원인 추적 기준을 설계해야 한다.

---

### [FAQ]

Q. AI Observability Domain Rules는 어떤 Agent가 사용하는가?

A. PM Agent, AI/ML Agent, Backend Agent, DevOps Agent, Review Agent, Architecture Review Agent가 역할별로 사용한다.

Q. DevOps Agent는 AI Observability에서 무엇을 담당하는가?

A. Metric, Log, Trace 수집, Dashboard, Alert, Cost / Latency 모니터링을 담당한다.

Q. Review Agent는 무엇을 검토해야 하는가?

A. Groundedness, Hallucination, Format Compliance, Trace 누락, Privacy 로그 노출을 검토해야 한다.

---

# 26. Final Goal

## 26.1 최종 목표

### [개념]

AI Observability Domain Rules의 최종 목표는 Agent가 AI 시스템의 입력부터 최종 출력까지 전체 실행 흐름과 품질 지표를 추적하고, 문제 원인을 분석하고, 개선으로 연결할 수 있도록 문서 제작 기준을 제공하는 것이다.

---

### [핵심]

최종 목표:

- AI Observability 개념 검색 가능
- LLM Trace 설계 가능
- Prompt Trace 설계 가능
- Context Trace 설계 가능
- RAG Trace 설계 가능
- Agent Workflow Trace 설계 가능
- Tool Call Trace 설계 가능
- Memory Trace 설계 가능
- Evaluation Trace 설계 가능
- Groundedness 평가 가능
- Hallucination 감지 가능
- Cost / Latency 분석 가능
- Drift / Regression 감지 가능
- Alert / Dashboard 설계 가능
- Feedback Loop 설계 가능
- Privacy / Security 검토 가능
- Troubleshooting 가능

---

### [실무]

AI Observability RAG Doc Set은 다음 작업을 지원해야 한다.

```text
User Request
→ Trace ID 생성
→ Prompt / Context 구성 추적
→ RAG Retrieval 추적
→ LLM 호출 추적
→ Tool Calling 추적
→ Agent Workflow 추적
→ Output Evaluation
→ Cost / Latency 기록
→ Feedback Loop
→ 개선 또는 Rollback
```

문서 품질은 Agent가 AI 시스템 품질 저하의 원인을 추적하고, 개선 대상을 정확히 찾고, 안전하게 운영할 수 있는지로 결정된다.

---

### [FAQ]

Q. AI Observability Domain Rules의 최종 목적은?

A. Agent가 AI 시스템의 실행 흐름, 품질, 비용, 오류, 근거성을 추적하고 개선할 수 있도록 문서 제작 기준을 제공하는 것이다.

Q. 이 문서는 사람 학습용인가?

A. 아니다. AI Agent Retrieval과 AI 시스템 운영 품질을 높이기 위한 문서이다.

Q. AI Observability 문서 품질은 무엇으로 판단하는가?

A. Agent가 Prompt, Retrieval, Context, Tool Call, Agent Workflow, Evaluation Trace를 활용해 문제 원인을 찾고 개선할 수 있는지로 판단한다.

---

# Retrieval Queries

### [FAQ]

Q. AI Observability란?
A. LLM, RAG, Agent 시스템의 Prompt, Context, Retrieval, Tool Call, Output, Evaluation을 추적해 품질과 오류 원인을 분석하는 운영 체계이다.

Q. AI Observability와 Monitoring의 차이는?
A. Monitoring은 상태와 Metric 중심이고, AI Observability는 AI 출력이 생성된 과정과 품질 근거를 추적한다.

Q. AI Observability에서 중요한 Trace는?
A. Prompt Trace, Context Trace, Retrieval Trace, Tool Call Trace, Agent Workflow Trace, Memory Trace, Evaluation Trace가 중요하다.

Q. Trace Design이란?
A. 사용자 요청이 어떤 단계와 Span을 거쳐 최종 출력으로 이어졌는지 추적 가능한 구조를 설계하는 것이다.

Q. LLM Observability에서 무엇을 기록해야 하는가?
A. 모델 버전, Prompt, Context, Output, Token 사용량, Latency, Cost, 오류, 평가 결과를 기록해야 한다.

Q. Prompt Observability는 왜 필요한가?
A. Prompt 변경이 답변 품질, 출력 형식, 안전성, 비용에 영향을 줄 수 있기 때문이다.

Q. RAG Observability란?
A. Query 변환, 문서 검색, Chunk 선택, Context 구성, 답변 Grounding을 추적하는 구조이다.

Q. retrievedChunks와 selectedChunks의 차이는?
A. retrievedChunks는 검색된 Chunk이고 selectedChunks는 실제 LLM Context에 포함된 Chunk이다.

Q. Agent Observability란?
A. Agent의 작업 분해, Routing, Tool Calling, State Update, Review, Final Output 흐름을 추적하는 구조이다.

Q. Tool Calling Observability란?
A. Tool 호출의 입력, 출력, 오류, 지연, 검증 결과, 상태 변경 여부를 추적하는 구조이다.

Q. Memory Observability란?
A. 어떤 Memory가 답변에 사용되었고 현재 요청과 충돌하지 않는지 추적하는 구조이다.

Q. Evaluation Observability란?
A. AI 출력이 Groundedness, Faithfulness, Format Compliance, Safety 같은 품질 기준을 만족하는지 추적하는 구조이다.

Q. Groundedness란?
A. AI 답변이 제공된 문서, Tool Result, 사용자 입력 같은 근거에 기반하는 정도이다.

Q. Hallucination이란?
A. AI가 근거 없는 내용이나 실제 Context와 일치하지 않는 내용을 사실처럼 생성하는 현상이다.

Q. Hallucination은 어떻게 감지하는가?
A. 답변을 검색 Context, Tool Result, Source Document, Review Checklist와 비교해 감지한다.

Q. Cost Tracking은 왜 필요한가?
A. Token, Tool, Retrieval, Serving 비용이 누적되면 운영 비용이 빠르게 증가할 수 있기 때문이다.

Q. Latency 병목은 어떻게 찾는가?
A. Retrieval, Reranking, Model Inference, Tool Call, Agent Step별 Latency를 분리해 추적한다.

Q. AI Drift란?
A. Prompt, Retrieval, Model, Tool, Memory, 사용자 Query 변화로 AI 시스템 품질이 시간이 지나며 변하는 현상이다.

Q. Regression이란?
A. 이전에는 잘 되던 기능이나 품질이 변경 이후 나빠지는 현상이다.

Q. AI Alert는 무엇을 감지해야 하는가?
A. 오류율, Latency, Cost, Hallucination, Groundedness 저하, Tool Call 실패, Agent Workflow 실패를 감지해야 한다.

Q. AI Observability Dashboard에는 무엇이 있어야 하는가?
A. 품질, 비용, 지연, Retrieval, Tool Calling, Agent Workflow, Evaluation, Alert 상태가 있어야 한다.

Q. Feedback Loop란?
A. 사용자 피드백, Evaluation, Alert, 실패 사례를 기반으로 Prompt, RAG, Tool, Memory, Model, Agent Workflow를 개선하는 구조이다.

Q. AI Observability에서 Privacy가 중요한 이유는?
A. Prompt, Context, Tool Result, Memory에 개인정보와 민감정보가 포함될 수 있기 때문이다.

Q. AI Observability에서 흔한 실패는?
A. Trace 누락, Prompt Version 미기록, Retrieval 결과 미기록, Evaluation 부재, 민감정보 로그 노출이다.

Q. AI Observability 문서 분할은 어떻게 하는가?
A. Core, Trace, Prompt, RAG, Agent/Tool/Memory, Evaluation, Groundedness/Cost, Drift/Dashboard, Privacy/Troubleshooting으로 분리한다.

Q. AI Observability 문서에서 피해야 할 것은?
A. 일반 로그 수집만 설명하고 Prompt, Retrieval, Context, Tool Call, Evaluation 추적을 누락하는 것이다.

Q. AI Observability Domain Rules는 어떤 Agent가 사용하는가?
A. PM Agent, AI/ML Agent, Backend Agent, DevOps Agent, Review Agent, Architecture Review Agent가 역할별로 사용한다.
