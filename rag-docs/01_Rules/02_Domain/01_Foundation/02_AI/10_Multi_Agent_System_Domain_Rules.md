# Multi-Agent System Domain Rules

---

# 1. Domain Purpose

Multi-Agent System Domain 문서는 AI Agent / PM Agent / Review Agent / Architecture Agent용 RAG 문서 제작 규칙이다.

목적:

- Multi-Agent System 기본 개념 이해
- 여러 Agent의 역할 분리 기준 제공
- PM Agent 중심 협업 구조 설계 지원
- Agent 간 Handoff / State / Memory 관리 기준 제공
- Review / Fix / Final Output 흐름 설계 지원
- RAG / Tool Calling / Workflow와 Multi-Agent 구조 연결
- 개인 AI 개발팀 구조 확장 기준 제공
- Multi-Agent 실패 원인 분석과 개선 방향 제공

우선순위:

1. Agent Role Separation
2. Clear Responsibility
3. PM-based Coordination
4. Handoff Quality
5. Shared State Consistency
6. Review / Fix Reliability
7. System Stability

---

# 2. Scope

포함 범위:

- Multi-Agent System Core
- Agent Role
- Agent Responsibility
- PM Agent
- Backend Agent
- Frontend Agent
- SQL Agent
- DevOps Agent
- AI Agent
- Review Agent
- Fix Agent
- Router Agent
- Planner Agent
- Executor Agent
- Critic Agent
- Agent Communication
- Agent Handoff
- Shared State
- Agent Memory
- Agent Tool Permission
- Agent Collaboration Pattern
- Sequential Multi-Agent
- Router-based Multi-Agent
- Review-Fix Multi-Agent
- Human-in-the-loop
- Multi-Agent Evaluation
- Multi-Agent Troubleshooting

제외 범위:

- LangGraph 구현 상세
- LangChain Agent 내부 구현 상세
- AutoGen / CrewAI / Semantic Kernel 상세 사용법
- MCP Protocol 심화
- Agentic RAG 심화
- Graph RAG 심화
- 대규모 분산 Agent 운영
- Fine-Tuning 기반 Agent 학습

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

# 4. Multi-Agent Core Rules

Multi-Agent System 문서는 여러 Agent가 역할을 나누어 하나의 목표를 수행하는 구조 중심으로 작성한다.

핵심 구조:

```text
User Request
→ Coordinator / PM Agent
→ Specialist Agents
→ Review Agent
→ Fix Agent
→ Final Output
```

반드시 설명:

- Multi-Agent System은 여러 Agent가 역할별로 협업하는 구조
- Agent는 각자 명확한 책임과 입력/출력을 가져야 함
- PM Agent 또는 Coordinator가 전체 흐름을 조율
- Review Agent는 산출물 품질을 검증
- Agent가 많을수록 품질이 좋아질 수 있지만 복잡도, 비용, Latency도 증가
- 초기에는 순차 실행 구조가 가장 현실적

금지:

- Agent를 단순 Prompt 이름만 바꾼 구조로 설명
- 모든 Agent가 모든 Tool을 사용하는 구조
- 역할 경계 없는 Agent 구성
- Review / Stop Condition 없는 무한 협업 구조
- Agent 간 Handoff 형식 없는 구조

---

# 5. Agent Role Design Rules

Agent Role은 Multi-Agent 품질의 핵심이다.

필수 포함:

- Agent Name
- Role
- Responsibility
- Input
- Output
- Scope
- Tool Permission
- RAG Scope
- Done Criteria

Agent 정의 Template:

```md
## Agent Definition

### Name

Backend Agent

### Role

Spring Boot Backend 구현 담당

### Responsibility

- API 설계
- DTO / Service / Controller 작성
- Transaction / Exception 기준 반영

### Input

- PM Agent Task
- Domain Rules
- Relevant RAG Context

### Output

- Backend Implementation Plan
- Code Snippets
- Risks / Assumptions

### Done Criteria

- 요구사항 충족
- Review 가능한 구조
```

반드시 설명:

- Agent Role은 구체적이어야 함
- Responsibility와 Scope를 분리
- Agent가 하지 말아야 할 일도 정의
- Output은 다음 Agent가 사용할 수 있는 형태로 구조화

주의:

- “전문가 Agent”처럼 추상적인 역할만 두지 말 것
- 책임이 겹치는 Agent를 너무 많이 만들지 말 것
- Agent별 Tool 권한을 제한하지 않으면 위험 증가

---

# 6. PM Agent Rules

PM Agent는 Multi-Agent System의 중심 조율자이다.

필수 포함:

- User Request Understanding
- Requirement Analysis
- Task Decomposition
- Agent Routing
- Priority Control
- Context Selection
- Result Integration
- User-facing Final Output

PM Flow:

```text
User Request
→ Analyze Requirement
→ Split Tasks
→ Select Agents
→ Send Handoff
→ Collect Outputs
→ Request Review
→ Integrate Final Answer
```

반드시 설명:

- PM Agent는 직접 구현보다 작업 분해와 통합이 핵심
- 어떤 Agent가 필요한지 판단
- 각 Agent에게 명확한 Handoff 제공
- 중간 결과를 통합하고 누락된 부분을 확인
- 사용자에게는 최종 결과 중심으로 전달

주의:

- PM Agent가 모든 Domain 작업을 직접 처리하지 않기
- 요구사항이 불명확하면 확인 또는 Assumption 표시
- Agent 결과를 검증 없이 그대로 합치지 않기
- PM Agent가 최종 품질 책임을 가짐

---

# 7. Specialist Agent Rules

Specialist Agent는 특정 Domain 작업을 수행한다.

예시:

- SQL Agent
- Backend Agent
- Frontend Agent
- DevOps Agent
- AI Agent
- Security Agent
- Testing Agent
- Documentation Agent

필수 포함:

- Domain Expertise
- Domain Rules
- RAG Context
- Tool Access
- Output Schema
- Constraint
- Assumption

Specialist Flow:

```text
Receive Task
→ Load Domain Rules
→ Retrieve Relevant Documents
→ Execute Domain Work
→ Return Structured Result
```

반드시 설명:

- Specialist Agent는 자기 영역의 전문 작업만 수행
- PM Agent가 전달한 요구사항과 제약을 우선
- Domain Rules와 RAG 문서를 근거로 작업
- 다른 Domain 변경이 필요하면 PM Agent에게 전달

주의:

- 다른 Agent의 책임 영역을 임의로 수정하지 않기
- 모르는 프로젝트 구조를 만들어내지 않기
- 구현 결과에 Assumption과 Risk를 포함

---

# 8. Review Agent Rules

Review Agent는 Multi-Agent 산출물을 검증한다.

필수 포함:

- Review Criteria
- Domain Rules Check
- Requirement Check
- Consistency Check
- Risk Check
- Severity
- Fix Direction
- Pass / Fail

Review Flow:

```text
Specialist Output
→ Check Requirement
→ Check Domain Rules
→ Check Consistency
→ Identify Issues
→ Return Findings
```

반드시 설명:

- Review Agent는 독립적인 품질 검증 담당
- 문제 / 원인 / 영향 / 수정 방향을 분리
- Severity를 기준으로 수정 우선순위 판단
- Review 결과는 Fix Agent가 바로 사용할 수 있어야 함

주의:

- 단순 취향을 결함처럼 표현하지 않기
- 근거 없는 지적 금지
- 수정 방향 없는 비판 금지
- 전체 Context가 부족하면 단정하지 않기

---

# 9. Fix Agent Rules

Fix Agent는 Review 결과를 반영한다.

필수 포함:

- Review Findings
- Fix Scope
- Preserve Requirement
- Change Summary
- Updated Output
- Regression Risk
- Re-review Request

Fix Flow:

```text
Review Findings
→ Select Fixes
→ Apply Changes
→ Check Original Requirements
→ Return Updated Output
→ Re-review
```

반드시 설명:

- Fix Agent는 Review 범위 안에서 수정
- 기존 요구사항과 기능을 유지
- 수정 내용과 변경 이유를 요약
- 재검토가 필요한 항목을 표시

주의:

- Review에 없는 큰 구조 변경을 임의로 하지 않기
- 수정 과정에서 새 요구사항을 만들지 않기
- 기존 API 계약 변경 시 영향 범위 표시

---

# 10. Router Agent Rules

Router Agent는 요청을 적절한 Agent로 분기한다.

필수 포함:

- Intent Classification
- Domain Detection
- Task Type
- Agent Selection
- Fallback
- Confidence

Routing 기준:

```text
DB / Query / Schema → SQL Agent
Spring Boot / API / JPA → Backend Agent
React / UI / State → Frontend Agent
Docker / Deploy / Linux → DevOps Agent
LLM / RAG / Agent → AI Agent
Review / 검증 → Review Agent
```

반드시 설명:

- Router는 요청의 Domain과 작업 유형을 판단
- Confidence가 낮으면 PM Agent 또는 사용자에게 확인
- 복합 요청은 여러 Agent로 분해
- Routing 결과는 기록 가능

주의:

- 짧은 질문만으로 과도하게 단정하지 않기
- 여러 Domain이 섞인 작업을 하나의 Agent에게 몰아주지 않기
- Fallback 기준 필요

---

# 11. Planner / Executor Rules

Planner / Executor 패턴은 계획과 실행을 분리한다.

필수 포함:

- Planner Agent
- Executor Agent
- Plan
- Step
- Dependency
- Execution Result
- Plan Revision

Flow:

```text
Planner Agent
→ Create Plan
→ Executor Agent
→ Execute Step
→ Return Result
→ Revise Plan if Needed
```

반드시 설명:

- Planner는 작업 순서와 전략을 만든다
- Executor는 실제 실행을 담당한다
- 복잡한 작업은 계획과 실행을 분리하면 안정적
- 실행 결과에 따라 계획 수정 가능

주의:

- 계획만 길고 실행이 없는 구조 금지
- Executor가 계획 범위를 벗어나지 않도록 함
- Plan Revision 조건 필요

---

# 12. Critic / Reviewer Pattern Rules

Critic / Reviewer Pattern은 결과 검증에 사용한다.

필수 포함:

- Draft Agent
- Critic Agent
- Review Criteria
- Findings
- Revision
- Acceptance Criteria

Flow:

```text
Draft
→ Critic Review
→ Revision
→ Final Review
→ Accept
```

반드시 설명:

- Critic Agent는 오류, 누락, 위험을 찾음
- Critic 기준은 명확해야 함
- Revision Agent는 Critic 결과를 반영
- Acceptance Criteria가 있어야 종료 가능

주의:

- Critic이 과도하게 까다로우면 무한 수정 발생
- Review 기준이 계속 바뀌지 않도록 함
- Minor Issue와 Critical Issue 구분

---

# 13. Agent Communication Rules

Agent Communication은 Agent 간 정보 전달 방식이다.

필수 포함:

- Message
- Handoff
- Shared State
- Structured Output
- Source Agent
- Target Agent
- Context
- Open Question

Communication Template:

```json
{
  "from": "PM Agent",
  "to": "Backend Agent",
  "task": "Design signup API",
  "context": [],
  "constraints": [],
  "expectedOutput": "Markdown",
  "openQuestions": []
}
```

반드시 설명:

- Agent 간 메시지는 구조화되어야 함
- Context, Task, Expected Output을 분리
- Assumption과 Open Question을 포함
- 다음 Agent가 바로 사용할 수 있어야 함

주의:

- 자연어 장문만 넘기면 누락 가능
- 출처 없는 결정 사항 전달 금지
- 실패 상태를 성공 메시지처럼 전달 금지

---

# 14. Shared State Rules

Shared State는 Multi-Agent System의 공통 작업 상태이다.

필수 포함:

- User Request
- Requirements
- Constraints
- Decisions
- Current Step
- Agent Outputs
- Tool Results
- Review Findings
- Status
- Final Result

예시:

```json
{
  "status": "in_progress",
  "currentStep": "backend_design",
  "requirements": [],
  "constraints": [],
  "decisions": [],
  "agentOutputs": {},
  "reviewFindings": []
}
```

반드시 설명:

- Shared State는 Agent들이 공통으로 참조하는 작업 기록
- 요구사항, 결정, 중간 결과를 보존
- Review / Fix Loop에서 중요
- 상태는 최신 정보 기준으로 관리

주의:

- 오래된 State가 최신 요청을 덮어쓰지 않게 함
- 모든 대화를 저장하면 Token 낭비
- 민감정보 저장 주의
- State 업데이트 규칙 필요

---

# 15. Memory Rules

Memory는 Agent가 이전 정보와 사용자 선호를 활용하는 구조이다.

필수 포함:

- Short-term Memory
- Long-term Memory
- Working Memory
- Project Memory
- User Preference
- Memory Retrieval
- Memory Update

반드시 설명:

- Short-term Memory는 현재 작업 흐름에 사용
- Long-term Memory는 장기 프로젝트 정보와 사용자 선호에 사용
- Project Memory는 기술 스택, 규칙, 결정사항 저장에 유용
- Memory는 최신성, 정확성, 민감정보를 관리해야 함

주의:

- 오래된 Memory를 무조건 신뢰하지 않기
- 현재 요청과 충돌하면 현재 요청 우선
- 민감정보 저장 금지 또는 제한
- Memory Update 기준 필요

---

# 16. Context Management Rules

Context Management는 필요한 정보만 Agent에게 전달하는 기준이다.

필수 포함:

- Relevant Context
- Context Filtering
- Context Compression
- Source Priority
- Token Budget
- Conflict Resolution
- Missing Context

Flow:

```text
Full Context
→ Filter Relevant Information
→ Compress
→ Attach Source
→ Pass to Agent
```

반드시 설명:

- 모든 Context를 전달하면 품질이 떨어질 수 있음
- Agent 작업에 필요한 정보만 전달
- 중요한 제약은 생략하면 안 됨
- 출처와 최신성을 유지
- 충돌하는 정보는 우선순위를 정함

주의:

- Context 부족은 Hallucination을 유발
- Context 과다는 핵심 지시를 묻히게 함
- 압축 과정에서 중요한 제약 삭제 금지

---

# 17. Tool Permission Rules

Multi-Agent System에서는 Agent별 Tool 권한을 제한해야 한다.

필수 포함:

- Tool Permission
- Least Privilege
- Read Tool
- Write Tool
- Dangerous Tool
- Human Approval
- Audit Log

예시:

| Agent         | Tool Permission                        |
| ------------- | -------------------------------------- |
| PM Agent      | RAG Search, Routing                    |
| Backend Agent | RAG Search, File Read, Code Search     |
| Review Agent  | RAG Search, Test Result Read           |
| DevOps Agent  | Log Read, Infra Status, Deploy Request |
| Fix Agent     | File Write with Approval               |

반드시 설명:

- 모든 Agent가 모든 Tool을 쓰면 위험
- 역할별 최소 권한 적용
- 위험 Tool은 승인 필요
- Tool 사용 내역은 기록 가능해야 함

주의:

- 삭제 / 배포 / DB 변경은 자동 실행 금지 또는 제한
- Tool 권한이 넓으면 사고 위험 증가
- Agent별 권한 정책 문서화

---

# 18. RAG Scope Rules

Agent별로 참조할 RAG Scope를 제한할 수 있다.

필수 포함:

- Domain RAG
- Project Rules
- Agent Rules
- Foundation RAG
- Expert RAG
- Metadata Filter
- Domain Filter

예시:

| Agent          | RAG Scope                             |
| -------------- | ------------------------------------- |
| Backend Agent  | Backend Foundation + Backend Expert   |
| Frontend Agent | Frontend Foundation + Frontend Expert |
| DevOps Agent   | DevOps Expert                         |
| AI Agent       | AI Foundation + AI Expert             |
| Review Agent   | Domain Rules + Project Rules          |

반드시 설명:

- Agent가 필요한 문서 범위만 검색하면 정확도가 올라감
- PM Agent가 검색 Scope를 지정 가능
- Review Agent는 Domain Rules와 실제 산출물을 비교
- 공통 문서는 여러 Agent가 참조 가능

주의:

- Scope가 너무 좁으면 필요한 문서 누락
- Scope가 너무 넓으면 관련 없는 문서 검색
- Metadata 품질이 중요

---

# 19. Multi-Agent Workflow Patterns

Multi-Agent System 문서에는 주요 패턴을 포함한다.

필수 Pattern:

- Coordinator Pattern
- Router Pattern
- Planner-Executor Pattern
- Specialist Team Pattern
- Review-Fix Pattern
- Human Approval Pattern
- Tool-Using Agent Pattern

예시:

```text
Coordinator Pattern:
User → PM Agent → Specialist Agents → PM Agent → Final

Review-Fix Pattern:
Draft Agent → Review Agent → Fix Agent → Review Agent → Final
```

반드시 설명:

- Coordinator Pattern은 PM Agent 중심 구조
- Router Pattern은 요청 분기에 적합
- Specialist Team은 복합 개발 작업에 적합
- Review-Fix는 품질 검증에 적합
- Human Approval은 위험 작업에 필수

주의:

- 여러 Pattern을 조합할 수 있음
- 초기에는 단순한 Sequential / Coordinator 구조 권장
- 복잡도 증가에 따른 Latency 고려

---

# 20. Sequential vs Parallel Rules

순차 실행과 병렬 실행의 차이를 설명한다.

비교:

| 구분 | Sequential                 | Parallel                    |
| ---- | -------------------------- | --------------------------- |
| 구조 | Agent를 순서대로 실행      | 여러 Agent를 동시에 실행    |
| 장점 | 단순하고 안정적            | 속도 개선 가능              |
| 단점 | 느림                       | 충돌/통합 복잡              |
| 적합 | 로컬 LLM, 의존성 있는 작업 | 독립 작업, 강한 리소스 환경 |

반드시 설명:

- 로컬 LLM 환경에서는 순차 실행이 현실적
- 병렬 실행은 Agent 결과 통합이 필요
- 작업 의존성이 있으면 순차 실행이 안전
- 병렬 실행은 리소스와 충돌 관리 필요

주의:

- 의존성 있는 작업을 병렬로 실행하면 충돌 가능
- 병렬 Agent는 메모리 / 비용 / Rate Limit 증가
- 결과 통합 Agent 필요

---

# 21. Personal AI Development Team Rules

개인 AI 개발팀 구조는 이 Domain의 핵심 사용 사례이다.

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

확장 구조:

```text
User
→ PM Agent
→ SQL Agent
→ Backend Agent
→ Frontend Agent
→ DevOps Agent
→ AI Agent
→ Review Agent
→ Final Output
```

반드시 설명:

- 사용자는 PM Agent에게만 요청
- PM Agent가 요구사항을 분석하고 Agent를 선택
- 각 Agent는 자기 Domain Rules와 RAG 문서를 참조
- Review Agent가 전체 품질을 검증
- 최종 결과는 사용자가 이해하기 쉽게 정리

현실 기준:

- 초기에는 순차 실행
- Agent 수는 최소 구성부터 시작
- RAG 문서 품질이 Agent 품질을 결정
- 로컬 모델 환경에서는 속도와 메모리 고려
- Review Agent를 두면 품질이 안정됨

주의:

- 처음부터 모든 Agent를 만들지 말 것
- 하나의 Agent에 모든 책임을 주지 말 것
- Review 없이 자동 수정/완료하지 말 것

---

# 22. Human-in-the-loop Rules

Human-in-the-loop는 Multi-Agent System의 안전장치이다.

필수 포함:

- Clarification
- Approval
- Risky Action
- Costly Action
- External Side Effect
- Final Confirmation

사용자 확인이 필요한 경우:

```text
요구사항 불명확
파일 삭제
DB 변경
배포
결제 / 이메일 발송
대량 API 호출
보안상 위험한 작업
```

반드시 설명:

- Agent가 자동으로 결정하면 위험한 작업이 있음
- 사용자 확인은 구체적인 선택지로 제공
- 승인 범위를 넘어 실행하지 않음
- 위험 작업은 dry-run 제공 가능

주의:

- 사소한 일까지 모두 확인하면 자동화 가치 저하
- 위험한 일은 반드시 확인
- 사용자 승인 로그를 남길 수 있음

---

# 23. Multi-Agent Evaluation Rules

Multi-Agent System도 평가가 필요하다.

필수 포함:

- Task Success Rate
- Routing Accuracy
- Handoff Quality
- Review Pass Rate
- Fix Success Rate
- Tool Success Rate
- Latency
- Cost
- User Satisfaction
- Failure Case

평가 Flow:

```text
Workflow Run
→ Evaluate Routing
→ Evaluate Agent Output
→ Evaluate Review
→ Evaluate Final Output
→ Record Failure
→ Improve Workflow
```

반드시 설명:

- 최종 결과뿐 아니라 중간 단계도 평가
- Agent Routing이 적절했는지 확인
- Handoff가 충분했는지 확인
- Review가 실제 품질 개선에 기여했는지 확인
- 실패 사례를 Workflow 개선에 반영

주의:

- Agent 수가 많다고 성공률이 항상 오르지 않음
- 비용과 Latency도 품질 지표
- 사용자 만족도와 실제 정확도를 함께 봐야 함

---

# 24. Failure Handling Rules

Multi-Agent System은 실패 처리를 명확히 해야 한다.

필수 포함:

- Routing Failure
- Handoff Failure
- Retrieval Failure
- Tool Failure
- Invalid Output
- Review Failure
- Fix Failure
- Infinite Loop
- User Clarification

Failure Flow:

```text
Failure Detected
→ Classify
→ Retry / Reroute / Ask User / Stop
→ Update State
→ Continue or Finalize
```

반드시 설명:

- 실패는 상태로 기록해야 함
- 실패 유형에 따라 대응이 다름
- 재시도 가능한 실패와 중단해야 하는 실패 구분
- 사용자 확인이 필요한 실패도 있음

주의:

- 실패를 숨기고 성공처럼 답변 금지
- 같은 실패를 반복하지 않기
- 실패 후 State를 갱신하지 않으면 다음 Agent가 오판

---

# 25. Troubleshooting Rules

반드시 포함 추천.

형식:

```md
문제:

원인:

해결:
```

---

## Agent 역할이 겹침

문제:

- 여러 Agent가 같은 작업을 반복하거나 서로 다른 결론을 냄

원인:

- Responsibility 정의 부족
- Scope 구분 없음
- PM Agent Routing 기준 부족

해결:

- Agent Definition 작성
- 각 Agent의 Input / Output / Done Criteria 명확화
- PM Agent Routing Rule 추가

---

## Handoff가 부정확함

문제:

- 다음 Agent가 필요한 정보를 받지 못함

원인:

- Context 누락
- Expected Output 미지정
- Assumption / Open Question 누락

해결:

- Handoff Template 사용
- Task / Context / Constraint 분리
- 미확정 사항 표시

---

## Review-Fix가 무한 반복됨

문제:

- Review와 Fix가 끝나지 않음

원인:

- Stop Condition 없음
- Severity 기준 없음
- Minor Issue까지 계속 수정
- Review 기준이 반복마다 바뀜

해결:

- Max Iteration 설정
- Critical / Major / Minor 구분
- Pass 기준 정의
- Minor Issue는 보고 후 종료 가능

---

## PM Agent가 구현까지 다 함

문제:

- PM Agent가 라우팅이 아니라 직접 코드를 작성함

원인:

- PM Agent 역할이 넓음
- Specialist Agent 호출 규칙 없음
- Handoff 단계 생략

해결:

- PM Agent를 분석 / 분해 / 라우팅 / 통합으로 제한
- 구현은 Specialist Agent에게 위임
- PM Output을 Task Plan 중심으로 변경

---

## Agent 결과가 서로 충돌함

문제:

- Backend Agent와 Frontend Agent 결과가 API 계약 등에서 맞지 않음

원인:

- Shared State 부족
- API Contract 미정의
- Agent 간 중간 결과 공유 부족

해결:

- Shared State에 API Contract 기록
- PM Agent가 계약을 먼저 확정
- Review Agent가 Cross-domain Consistency 검토

---

## Agent가 존재하지 않는 정보를 만듦

문제:

- 실제 프로젝트에 없는 파일명, 클래스명, API 경로를 생성함

원인:

- RAG Context 부족
- Missing Information Rule 없음
- 프로젝트 구조 확인 없이 진행

해결:

- 프로젝트 구조 RAG 검색
- 불확실하면 Assumption 표시
- 필요한 경우 사용자 확인
- Review Agent가 존재 여부 검증

---

# 26. Best Practice Rules

Best Practice:

- Multi-Agent는 역할 분리부터 설계
- PM Agent는 조율자 역할로 제한
- Specialist Agent는 Domain별로 분리
- Review Agent는 독립적으로 유지
- Handoff Template을 통일
- Shared State에 요구사항, 결정, 산출물을 기록
- Agent별 Tool Permission을 제한
- Agent별 RAG Scope를 제한
- Review-Fix Loop에는 Max Iteration 설정
- 위험 작업에는 Human-in-the-loop 적용
- 초기에는 순차 실행 구조로 시작
- 실패 사례를 Workflow 개선에 반영
- Agent 수는 필요할 때만 늘림

---

# 27. Comparison Rules

Multi-Agent System 문서는 비교 기준을 포함한다.

필수 비교 대상:

- Single Agent vs Multi-Agent
- PM Agent vs Router Agent
- PM Agent vs Specialist Agent
- Specialist Agent vs Review Agent
- Sequential Execution vs Parallel Execution
- Shared State vs Memory
- Handoff vs Conversation History
- Review-Fix Loop vs Self-Check
- Human-in-the-loop vs Full Automation

예시:

| 비교 | Single Agent             | Multi-Agent            |
| ---- | ------------------------ | ---------------------- |
| 구조 | 하나의 Agent가 전체 처리 | 여러 Agent가 역할 분담 |
| 장점 | 단순하고 빠름            | 전문성, 검증, 확장성   |
| 단점 | 복잡 작업에 약함         | 느리고 설계 복잡       |
| 적합 | 단순 답변, 작은 작업     | 개발팀형 Workflow      |

---

# 28. Checklist Rules

Multi-Agent System 문서에는 Checklist를 포함할 수 있다.

예시:

```md
### [Checklist]

- [ ] Agent별 Role이 명확한가?
- [ ] Responsibility와 Scope가 분리되어 있는가?
- [ ] PM Agent가 구현이 아닌 조율을 담당하는가?
- [ ] Specialist Agent가 Domain Rules를 참조하는가?
- [ ] Handoff Template이 있는가?
- [ ] Shared State가 정의되어 있는가?
- [ ] Agent별 RAG Scope가 제한되어 있는가?
- [ ] Agent별 Tool Permission이 제한되어 있는가?
- [ ] Review Agent가 독립적으로 검증하는가?
- [ ] Review-Fix Loop에 Max Iteration이 있는가?
- [ ] Stop Condition이 있는가?
- [ ] 위험 작업에 Human Confirmation이 있는가?
```

---

# 29. Retrieval Optimization Rules

강조 대상 키워드:

- Multi-Agent System
- Multi-Agent Architecture
- Agent Role
- Agent Responsibility
- PM Agent
- Coordinator Agent
- Router Agent
- Specialist Agent
- Backend Agent
- Frontend Agent
- SQL Agent
- DevOps Agent
- AI Agent
- Review Agent
- Fix Agent
- Planner Agent
- Executor Agent
- Critic Agent
- Agent Communication
- Agent Handoff
- Shared State
- Agent Memory
- Agent Tool Permission
- Agent RAG Scope
- Sequential Multi-Agent
- Parallel Multi-Agent
- Review-Fix Loop
- Human-in-the-loop
- Personal AI Development Team

키워드 반복 허용.

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

예:

- Multi-Agent System이 뭐야?
- Agent 역할은 어떻게 나눠?
- PM Agent는 뭐 하는 Agent야?
- Specialist Agent는 뭐야?
- Review Agent는 왜 필요해?
- Agent Handoff는 어떻게 해?
- Shared State는 왜 필요해?
- Agent별 Tool 권한은 어떻게 나눠?
- 순차 실행과 병렬 실행 차이는?
- 개인 AI 개발팀은 어떻게 구성해?
- Multi-Agent가 실패하면 어디를 봐야 해?

---

# 30. Version Rules

기준:

- Modern LLM Agent
- Multi-Agent System Foundation
- PM Agent 중심 구조
- RAG 기반 Agent
- Tool Calling 기반 Agent
- Sequential Multi-Agent 우선
- Review-Fix Loop
- Human-in-the-loop
- Local LLM 기반 개인 AI 서버 고려
- LangGraph / LangChain 확장 가능성 고려

Legacy 제외:

- Agent 역할 구분 없는 Prompt 묶음
- Shared State 없는 Multi-Agent
- Handoff 형식 없는 Agent 협업
- Tool 권한 구분 없는 Agent
- Review 없는 자동 완료 구조
- 종료 조건 없는 무한 Agent Loop

---

# 31. Common Mistakes

자주 발생:

- Agent를 너무 많이 만듦
- Agent 역할이 겹침
- PM Agent가 구현까지 담당
- Handoff가 모호함
- Shared State가 없음
- Agent별 RAG Scope가 없음
- Agent별 Tool 권한이 없음
- Review Agent가 없음
- Review-Fix Loop가 무한 반복
- Stop Condition이 없음
- Agent 결과 간 충돌 검증 없음
- Human Confirmation 없이 위험 작업 실행
- 최종 결과 통합 품질이 낮음

---

# 32. Final Goal

Multi-Agent System RAG 문서는 Agent가 아래를 수행 가능해야 한다.

- Multi-Agent System 개념 설명
- Agent Role 설계
- PM Agent / Specialist Agent / Review Agent 역할 구분
- Router / Planner / Executor / Critic Pattern 이해
- Agent Handoff 구조 설계
- Shared State 구조 설계
- Agent Memory 기준 설명
- Agent별 Tool Permission 설계
- Agent별 RAG Scope 설계
- Sequential / Parallel 실행 기준 판단
- Review-Fix Loop 설계
- Human-in-the-loop 필요 여부 판단
- 개인 AI 개발팀 구조 제안
- Multi-Agent 실패 원인 분석
- Multi-Agent Workflow 개선 방향 제안

문서 품질이 개인 AI 개발팀의 협업 품질과 실행 안정성을 결정한다.

---

# Retrieval Queries

### [FAQ]

Q. Multi-Agent System이 뭐야?

A.
여러 Agent가 역할을 나누어 하나의 목표를 수행하는 AI 시스템 구조다.

Q. Single Agent와 Multi-Agent 차이는?

A.
Single Agent는 하나의 Agent가 모든 작업을 처리하고, Multi-Agent는 PM, Backend, Review처럼 역할을 나눠 처리한다.

Q. Multi-Agent는 언제 필요해?

A.
작업이 복잡하거나 설계, 구현, 검토, 수정처럼 역할 분리가 품질에 도움이 될 때 필요하다.

Q. PM Agent는 뭐 하는 Agent야?

A.
사용자 요청을 분석하고 작업을 분해하며, 적절한 Agent에게 라우팅하고 최종 결과를 통합하는 조율자다.

Q. Specialist Agent는 뭐야?

A.
Backend, Frontend, SQL, DevOps, AI처럼 특정 Domain 작업을 전문적으로 수행하는 Agent다.

Q. Review Agent는 왜 필요해?

A.
다른 Agent가 만든 결과를 요구사항, Domain Rules, 품질 기준에 맞게 검증하기 위해 필요하다.

Q. Fix Agent는 뭐야?

A.
Review Agent가 발견한 문제를 반영해 산출물을 수정하는 Agent다.

Q. Router Agent는 뭐야?

A.
요청의 Domain과 작업 유형을 판단해 적절한 Agent를 선택하는 Agent다.

Q. Planner Agent와 Executor Agent 차이는?

A.
Planner Agent는 계획을 만들고, Executor Agent는 계획에 따라 실제 작업을 수행한다.

Q. Critic Agent는 뭐야?

A.
산출물의 오류, 누락, 위험을 찾고 개선 방향을 제안하는 검토 Agent다.

Q. Agent Handoff는 어떻게 해?

A.
작업, Context, 제약, 기대 출력, Assumption, Open Question을 구조화해서 다음 Agent에게 전달한다.

Q. Shared State는 왜 필요해?

A.
요구사항, 결정 사항, Agent 결과, Review 결과를 공통으로 관리해 Agent 간 일관성을 유지하기 위해 필요하다.

Q. Agent Memory와 Shared State 차이는?

A.
Shared State는 현재 Workflow의 작업 상태이고, Memory는 장기 사용자 정보나 프로젝트 지식을 저장하는 구조다.

Q. Agent별 Tool 권한은 왜 나눠야 해?

A.
모든 Agent가 위험 Tool을 사용할 수 있으면 파일 수정, DB 변경, 배포 같은 사고 가능성이 커지기 때문이다.

Q. Agent별 RAG Scope는 왜 제한해?

A.
필요한 Domain 문서만 검색하게 해 관련 없는 Context를 줄이고 답변 정확도를 높이기 위해서다.

Q. 순차 실행과 병렬 실행 차이는?

A.
순차 실행은 Agent를 차례대로 실행해 안정적이고, 병렬 실행은 여러 Agent를 동시에 실행해 빠르지만 통합이 복잡하다.

Q. 로컬 LLM 환경에서는 어떤 방식이 좋아?

A.
처음에는 순차 실행 Multi-Agent 구조가 현실적이다. 병렬 실행은 RAM, 속도, 모델 동시 실행 제약을 고려해야 한다.

Q. Review-Fix Loop는 왜 필요해?

A.
생성 결과를 검토하고 수정해 최종 품질을 높이기 위해 필요하다.

Q. Multi-Agent가 무한 반복하면 어떻게 해?

A.
Max Iteration, Stop Condition, Severity 기준, Human Confirmation 조건을 설정한다.

Q. 개인 AI 개발팀은 어떻게 구성해?

A.
User가 PM Agent에게 요청하고, PM Agent가 SQL, Backend, Frontend, DevOps, AI, Review Agent로 작업을 분배한 뒤 최종 결과를 통합한다.
