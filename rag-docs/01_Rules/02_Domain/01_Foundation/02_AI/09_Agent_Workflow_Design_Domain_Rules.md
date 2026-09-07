# Agent Workflow Design Domain Rules

---

# 1. Domain Purpose

Agent Workflow Design Domain 문서는 AI Agent / PM Agent / Review Agent / Multi-Agent System용 RAG 문서 제작 규칙이다.

목적:

- Agent Workflow 기본 개념 이해
- 단일 Agent / Multi-Agent Workflow 설계 지원
- PM Agent 중심 Task Decomposition 기준 제공
- Agent Routing / Handoff / Review Loop 설계 지원
- Agent State / Context 전달 기준 제공
- Tool Calling / RAG / Memory 연계 기준 제공
- Agent 실패 / 반복 / 중단 조건 설계 지원
- 개인 AI 개발팀 구조 설계 지원

우선순위:

1. Clear Workflow
2. Agent Role Separation
3. Task Decomposition
4. Handoff Quality
5. State / Context Management
6. Review / Fix Loop
7. Failure Handling

---

# 2. Scope

포함 범위:

- Agent Workflow Core
- Single Agent Workflow
- Multi-Agent Workflow
- PM Agent
- Domain Agent
- Review Agent
- Fix Agent
- Agent Role
- Agent Responsibility
- Task Decomposition
- Task Routing
- Agent Handoff
- Shared State
- Context Passing
- Intermediate Output
- Review Loop
- Fix Loop
- Stop Condition
- Failure Handling
- Human-in-the-loop
- Tool Calling Integration
- RAG Integration
- Memory Integration
- Workflow Evaluation

제외 범위:

- LangGraph 상세 구현
- LangChain 상세 구현
- MCP Protocol 상세
- Agentic RAG 심화
- Graph RAG 심화
- Production Agent Platform 운영
- Fine-Tuning 기반 Agent 학습
- 대규모 분산 Agent 시스템 운영

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

# 4. Agent Workflow Core Rules

Agent Workflow 문서는 Agent가 작업을 어떻게 분해하고 순서대로 처리하는지 중심으로 작성한다.

핵심 구조:

```text
User Request
→ Task Analysis
→ Agent Routing
→ Agent Execution
→ Review
→ Fix
→ Final Output
```

반드시 설명:

- Agent Workflow는 LLM 호출을 순서와 책임에 따라 연결한 구조
- Agent는 역할과 책임이 명확해야 함
- Workflow는 입력, 출력, 상태, 종료 조건을 가져야 함
- Multi-Agent 구조는 협업 품질과 검증 품질을 높일 수 있음
- Agent가 많을수록 복잡도와 Latency도 증가함

금지:

- Agent를 단순 프롬프트 모음으로만 설명
- 모든 Agent가 모든 일을 하게 만드는 구조
- 종료 조건 없는 반복 구조
- Review 없이 자동 완료하는 구조
- Agent 실패 처리를 생략하는 구조

---

# 5. Single Agent Workflow Rules

Single Agent Workflow는 하나의 Agent가 요청 분석부터 답변까지 처리하는 구조이다.

필수 포함:

- User Request
- Prompt
- RAG Search
- Tool Use
- Response Generation
- Self-Check
- Final Answer

기본 Flow:

```text
User Request
→ Agent Analyze
→ Retrieve Context if Needed
→ Use Tool if Needed
→ Generate Answer
→ Self Check
→ Final Output
```

적합한 경우:

- 단순 질의응답
- 작은 코드 설명
- 짧은 문서 요약
- 간단한 자동화 작업
- Agent 간 분리가 불필요한 작업

주의:

- 복잡한 개발 작업에는 책임이 과도하게 집중될 수 있음
- Review 품질이 낮을 수 있음
- Self-Check는 독립 Review보다 약할 수 있음

---

# 6. Multi-Agent Workflow Rules

Multi-Agent Workflow는 여러 Agent가 역할을 나누어 작업하는 구조이다.

필수 포함:

- PM Agent
- Domain Agent
- Review Agent
- Fix Agent
- Final Response Agent
- Handoff
- Shared State
- Review Loop

기본 Flow:

```text
User Request
→ PM Agent
→ Task Decomposition
→ Backend / Frontend / AI / DevOps Agent
→ Review Agent
→ Fix Agent
→ Final Output
```

반드시 설명:

- PM Agent는 요청 분석과 라우팅 담당
- Domain Agent는 전문 작업 수행
- Review Agent는 결과 검증 담당
- Fix Agent는 Review 결과를 반영
- Final Output은 사용자에게 필요한 형태로 정리

주의:

- Agent가 많으면 실행 시간이 길어짐
- Agent 간 출력 형식이 다르면 Workflow가 깨짐
- 중간 결과 누락 시 Review 품질이 낮아짐
- 무한 Review / Fix Loop 방지 필요

---

# 7. PM Agent Rules

PM Agent는 전체 Workflow의 시작점이자 조율자이다.

필수 포함:

- User Request Analysis
- Requirement Clarification
- Task Decomposition
- Agent Routing
- Priority Decision
- Scope Control
- Final Integration

PM Agent Flow:

```text
User Request
→ Understand Goal
→ Identify Domain
→ Split Tasks
→ Assign Agents
→ Collect Results
→ Request Review
→ Finalize
```

반드시 설명:

- PM Agent는 직접 구현보다 작업 분해와 조율이 핵심
- 불명확한 요구사항은 확인하거나 가정 표시
- 작업 범위와 우선순위를 정리
- 각 Agent에게 명확한 입력과 기대 출력을 전달
- 최종 결과를 사용자 목적에 맞게 통합

주의:

- PM Agent가 모든 구현을 직접 처리하지 않도록 함
- 요구사항이 불명확한데 무리하게 진행 금지
- Agent별 책임 범위를 침범하지 않도록 함

---

# 8. Domain Agent Rules

Domain Agent는 특정 전문 영역의 작업을 수행한다.

예시:

- Backend Agent
- Frontend Agent
- SQL Agent
- DevOps Agent
- AI Agent
- Security Agent
- Testing Agent

필수 포함:

- Domain Role
- Input
- Output
- Required Context
- Domain Rules
- Tool Access
- Done Criteria

Domain Agent Flow:

```text
Task Input
→ Load Domain Rules
→ Retrieve Related RAG
→ Execute Domain Task
→ Return Structured Output
```

반드시 설명:

- Domain Agent는 자기 영역에 집중
- 필요한 RAG 문서와 Domain Rules를 우선 참조
- 결과는 Review Agent가 검증 가능한 형태로 작성
- 구현 코드뿐 아니라 판단 근거와 주의점 포함 가능

주의:

- 다른 Domain까지 임의로 수정하지 않기
- 존재하지 않는 프로젝트 구조를 만들지 않기
- 불확실한 정보는 Assumption으로 표시

---

# 9. Review Agent Rules

Review Agent는 산출물 품질을 검증한다.

필수 포함:

- Review Criteria
- Checklist
- Severity
- Finding
- Risk
- Fix Direction
- Pass / Fail
- Re-review

Review Flow:

```text
Agent Output
→ Check Against Requirements
→ Check Domain Rules
→ Find Issues
→ Assign Severity
→ Suggest Fix
→ Pass or Return to Fix
```

반드시 설명:

- Review Agent는 구현이 아니라 검증이 핵심
- Review 기준은 명확해야 함
- 문제, 원인, 영향, 수정 방향을 분리
- Severity를 통해 우선순위 판단
- Review 결과는 Fix Agent가 사용할 수 있어야 함

주의:

- 취향과 결함을 구분
- 일부 코드만 보고 전체 시스템을 단정하지 않기
- 근거 없는 지적 금지
- Fix 방향 없이 문제만 나열하지 않기

---

# 10. Fix Agent Rules

Fix Agent는 Review 결과를 반영해 산출물을 개선한다.

필수 포함:

- Review Findings
- Fix Scope
- Preserve Behavior
- Change Summary
- Updated Output
- Retest / Re-review Request

Fix Flow:

```text
Review Findings
→ Prioritize Issues
→ Apply Fix
→ Preserve Existing Requirements
→ Return Updated Output
→ Request Re-review
```

반드시 설명:

- Fix Agent는 Review 결과를 기준으로 수정
- 기능 변경과 결함 수정을 구분
- 기존 요구사항을 유지해야 함
- 수정 내역을 요약해야 함
- 필요하면 재검토 요청

주의:

- Review 범위를 넘어 임의 수정 금지
- 새로운 구조를 과도하게 추가하지 않기
- 기존 API / DTO / 계약 변경 시 영향 명시

---

# 11. Task Decomposition Rules

Task Decomposition은 복잡한 요청을 실행 가능한 단위로 나누는 과정이다.

필수 포함:

- Goal
- Subtask
- Dependency
- Priority
- Owner Agent
- Expected Output
- Done Criteria

예시:

```text
User Request:
회원가입 기능 만들어줘

Task Decomposition:
1. SQL Agent: users table 검토
2. Backend Agent: DTO / Service / Controller 설계
3. Security Agent: Password Encoding / Validation 검토
4. Testing Agent: 테스트 케이스 작성
5. Review Agent: 전체 검증
```

반드시 설명:

- 큰 요청은 작은 작업으로 나누어야 함
- 각 Subtask는 담당 Agent와 결과물이 명확해야 함
- 선행 작업과 후행 작업 의존성 고려
- Done Criteria가 있어야 완료 판단 가능

주의:

- 너무 작게 쪼개면 오버헤드 증가
- 너무 크게 유지하면 Agent가 놓치는 부분 증가
- 병렬 가능 작업과 순차 작업 구분

---

# 12. Agent Routing Rules

Agent Routing은 어떤 Agent가 어떤 작업을 맡을지 결정하는 과정이다.

필수 포함:

- Task Type
- Domain
- Required Expertise
- Required Tool
- Priority
- Routing Rule
- Fallback Agent

Routing 기준:

```text
SQL / DB Schema → SQL Agent
Spring Boot / API → Backend Agent
React / UI → Frontend Agent
Docker / Deploy → DevOps Agent
RAG / LLM / Agent → AI Agent
검증 / 품질 → Review Agent
```

반드시 설명:

- Routing은 PM Agent의 핵심 책임
- 작업 Domain이 여러 개면 순서를 정해야 함
- 모호한 요청은 우선 분석 Agent 또는 PM Agent가 정리
- 담당 Agent가 실패하면 fallback 또는 clarification 필요

주의:

- 하나의 요청을 무조건 하나의 Agent에게만 맡기지 말 것
- 역할이 겹치는 경우 책임 기준 필요
- Tool 권한과 Agent 역할을 함께 고려

---

# 13. Handoff Rules

Handoff는 Agent 간 작업 전달 형식이다.

필수 포함:

- Source Agent
- Target Agent
- Task
- Context
- Input
- Output Format
- Constraints
- Assumptions
- Open Questions

Handoff Template:

```md
## Handoff

From: PM Agent
To: Backend Agent

### Task

회원가입 API 설계

### Context

- Spring Boot 3.x
- Java 21
- ApiResponse<T> 직접 반환
- GlobalExceptionHandler 사용

### Expected Output

- DTO
- Service Flow
- Controller Endpoint
- Exception Cases
```

반드시 설명:

- Handoff는 다음 Agent가 바로 작업할 수 있을 만큼 명확해야 함
- Context와 Task를 분리
- Output Format 지정
- 가정과 미확정 사항 표시

주의:

- 모호한 Handoff는 Agent 품질 저하
- 이전 Agent의 추정을 사실처럼 넘기지 않기
- 누락된 제약 조건 확인

---

# 14. Shared State Rules

Shared State는 Workflow 전체에서 유지되는 정보이다.

필수 포함:

- User Request
- Requirements
- Decisions
- Constraints
- Current Task
- Agent Outputs
- Review Findings
- Final Result

기본 구조:

```json
{
  "userRequest": "",
  "requirements": [],
  "constraints": [],
  "decisions": [],
  "agentOutputs": {},
  "reviewFindings": [],
  "status": "in_progress"
}
```

반드시 설명:

- Shared State는 Agent 간 공통 기억 역할
- 변경 이력과 결정 사항을 유지
- Agent 출력은 구조화해서 저장
- Review와 Fix 결과도 상태에 반영

주의:

- 오래된 State가 최신 요구사항을 덮어쓰지 않도록 주의
- 불필요한 전체 대화 저장은 Token 낭비
- 민감정보 저장 주의

---

# 15. Context Passing Rules

Context Passing은 다음 Agent에게 필요한 정보만 전달하는 과정이다.

필수 포함:

- Relevant Context
- Minimal Context
- Source
- Constraint
- Decision
- Assumption
- Excluded Context

기본 Flow:

```text
Full State
→ Select Relevant Context
→ Compress
→ Attach Source / Decision
→ Send to Next Agent
```

반드시 설명:

- 모든 Context를 넘기는 것이 항상 좋지 않음
- 작업에 필요한 정보만 전달
- 중요한 제약과 결정은 반드시 포함
- 오래된 정보와 최신 정보 충돌 시 최신 정보 우선

주의:

- Context 누락 시 Agent가 임의 추정
- Context 과다 시 핵심 지시가 묻힘
- 출처 없는 정보는 신뢰도 낮음

---

# 16. Intermediate Output Rules

Intermediate Output은 다음 단계가 검증/사용할 수 있게 구조화한다.

필수 포함:

- Summary
- Details
- Decisions
- Assumptions
- Open Issues
- Artifacts
- Next Step

예시:

```md
## Backend Agent Output

### Summary

회원가입 API 설계 완료

### Decisions

- Password는 BCrypt로 Encoding
- 중복 이메일은 BusinessException 처리

### Open Issues

- 이메일 인증 필수 여부 확인 필요
```

반드시 설명:

- 중간 결과는 최종 답변과 다름
- 다음 Agent가 사용할 판단 근거 포함
- 미확정 사항을 명확히 표시
- Review 가능한 구조로 작성

주의:

- 중간 결과에 과도한 장문 설명 금지
- 결정과 추정을 구분
- 누락된 부분을 숨기지 않기

---

# 17. Review / Fix Loop Rules

Review / Fix Loop는 산출물 품질을 개선하는 반복 구조이다.

기본 Flow:

```text
Domain Agent Output
→ Review Agent
→ Findings
→ Fix Agent
→ Updated Output
→ Re-review
→ Pass
```

필수 포함:

- Review Criteria
- Finding
- Severity
- Fix Action
- Re-review
- Max Iteration
- Stop Condition

반드시 설명:

- Review 결과가 Fail이면 Fix 단계로 이동
- Fix 후 재검토 가능
- 반복 횟수 제한 필요
- Minor Issue는 사용자에게 전달하고 종료 가능

주의:

- 무한 반복 방지
- Review 기준이 바뀌면 안 됨
- Fix Agent가 새 문제를 만들 수 있으므로 재검토 필요

---

# 18. Stop Condition Rules

Stop Condition은 Workflow 종료 기준이다.

필수 포함:

- Task Completed
- Review Passed
- Max Iteration Reached
- Missing Information
- User Confirmation Required
- Tool Failure
- Unsafe Action Detected

예시:

```text
Stop when:
- Required output is generated
- Review Agent passes result
- No blocking issue remains
- Final answer is ready
```

반드시 설명:

- Agent Workflow에는 명확한 종료 조건이 필요
- 완료, 실패, 보류 상태를 구분
- 정보 부족 시 사용자 확인으로 종료 가능
- 위험 작업은 승인 대기로 중단

주의:

- 종료 조건 없는 Agent Loop 금지
- 불완전한 결과를 성공으로 표시 금지
- 실패 상태를 명확히 반환

---

# 19. Failure Handling Rules

Agent Workflow는 실패를 정상적인 상태로 다뤄야 한다.

필수 포함:

- Missing Context
- Tool Failure
- Retrieval Failure
- Invalid Output
- Review Failure
- Timeout
- Unsafe Action
- Human Escalation

Failure Flow:

```text
Failure Detected
→ Classify Failure
→ Retry / Fallback / Ask User
→ Update State
→ Continue or Stop
```

반드시 설명:

- 실패 유형을 구분해야 함
- 재시도 가능한 실패와 불가능한 실패를 나눔
- 정보 부족은 사용자 확인 필요
- Tool 실패는 구조화된 에러로 전달
- 안전 문제는 즉시 중단 가능

주의:

- 실패를 숨기지 않기
- 무제한 재시도 금지
- 잘못된 결과를 기반으로 다음 Agent 실행 금지

---

# 20. Human-in-the-loop Rules

Human-in-the-loop는 사용자 확인이 필요한 지점이다.

필수 포함:

- Clarification
- Approval
- Risky Action
- Ambiguous Requirement
- Costly Operation
- External Side Effect
- Final Confirmation

필요한 경우:

```text
요구사항 불명확
→ 사용자 확인

파일 삭제 / DB 변경 / 배포
→ 사용자 승인

비용 발생 API 대량 호출
→ 사용자 승인

정책상 위험한 작업
→ 중단 또는 확인
```

반드시 설명:

- Agent가 모든 결정을 자동으로 하면 위험할 수 있음
- 불명확하거나 위험한 작업은 사용자에게 확인
- 확인 요청은 구체적이고 선택 가능해야 함
- 사용자의 승인 범위를 넘어 실행하지 않음

주의:

- 너무 자주 물으면 자동화 가치가 낮아짐
- 반대로 위험 작업을 묻지 않으면 안전 문제가 생김
- 승인 내용과 실행 내용이 일치해야 함

---

# 21. RAG Integration Rules

Agent Workflow는 RAG와 연결될 수 있다.

필수 포함:

- Domain Rules Retrieval
- Project Rules Retrieval
- Code Context Retrieval
- Search Query Generation
- Retrieved Context
- Grounded Answer
- Source Tracking

RAG Flow:

```text
Agent Task
→ Generate Search Query
→ Retrieve Domain RAG
→ Use Retrieved Context
→ Produce Grounded Output
```

반드시 설명:

- Agent는 작업 전 관련 RAG 문서를 검색할 수 있음
- PM Agent는 Domain 선택을 통해 검색 범위 제한 가능
- Domain Agent는 자기 영역 RAG를 우선 사용
- Review Agent는 Domain Rules와 결과물을 비교

주의:

- 관련 없는 RAG Context 과다 주입 금지
- 검색 실패 시 일반 지식으로 확정하지 말 것
- 출처와 가정을 구분

---

# 22. Tool Calling Integration Rules

Agent Workflow는 Tool Calling과 연결된다.

필수 포함:

- Tool Need Detection
- Tool Choice
- Tool Permission
- Tool Execution
- Tool Result
- Tool Failure
- Human Confirmation

Tool Flow:

```text
Agent Needs External Action
→ Select Tool
→ Validate Arguments
→ Execute Tool
→ Use Tool Result
→ Continue Workflow
```

반드시 설명:

- Agent가 직접 할 수 없는 작업은 Tool로 수행
- Tool 권한은 Agent별로 제한
- 위험 Tool은 사용자 승인 필요
- Tool Result는 Shared State에 저장 가능

주의:

- Tool 결과 검증 없이 다음 단계 진행 금지
- 실패한 Tool을 성공처럼 처리 금지
- Tool 호출로 인한 Side Effect 관리

---

# 23. Memory Integration Rules

Agent Workflow는 Memory / State와 연결될 수 있다.

필수 포함:

- Short-term Memory
- Long-term Memory
- Working State
- User Preference
- Project Decision
- Conversation Summary
- Checkpoint

반드시 설명:

- Short-term Memory는 현재 작업 문맥
- Long-term Memory는 장기 사용자/프로젝트 정보
- Workflow State는 현재 실행 상태
- Checkpoint는 중간 복구에 유용
- Memory는 최신성과 정확성 관리가 필요

주의:

- 오래된 Memory를 무조건 신뢰하지 않기
- 민감정보 저장 주의
- 현재 사용자 요청과 충돌하면 현재 요청 우선
- 불확실한 Memory는 확인 필요

---

# 24. Workflow Evaluation Rules

Agent Workflow 품질도 평가해야 한다.

필수 포함:

- Task Success
- Output Quality
- Review Pass Rate
- Tool Success Rate
- Latency
- Cost
- User Satisfaction
- Failure Rate

평가 Flow:

```text
Workflow Run
→ Check Final Output
→ Check Intermediate Outputs
→ Check Review Findings
→ Record Failure
→ Improve Workflow
```

반드시 설명:

- 최종 답변뿐 아니라 중간 단계도 평가
- Agent Routing이 적절했는지 확인
- Review Loop가 실제 품질 개선에 기여했는지 확인
- 실패 사례를 Workflow 개선에 반영

주의:

- Agent 수가 많다고 품질이 항상 좋아지는 것은 아님
- Latency와 비용도 평가해야 함
- 자동 평가와 사람 검토를 함께 고려

---

# 25. Workflow Pattern Rules

Agent Workflow 문서에는 자주 쓰는 Pattern을 포함한다.

필수 Pattern:

- Sequential Workflow
- Router Workflow
- Review-Fix Workflow
- Planner-Executor Workflow
- Human Approval Workflow
- Tool-Using Workflow

예시:

```text
Sequential:
A → B → C → Final

Router:
PM → Backend or Frontend or DevOps

Review-Fix:
Draft → Review → Fix → Re-review → Final
```

반드시 설명:

- Sequential은 단순하고 안정적
- Router는 작업 종류별 Agent 분기에 적합
- Review-Fix는 품질 검증에 적합
- Human Approval은 위험 작업에 필요
- Tool-Using은 외부 시스템 작업에 필요

주의:

- 복잡한 Workflow를 처음부터 과도하게 설계하지 말 것
- Pattern은 작업 목적에 맞게 선택
- 여러 Pattern을 조합 가능

---

# 26. Personal AI Development Team Rules

개인 AI 개발팀 구조에 맞춘 설명을 포함할 수 있다.

기본 구조:

```text
User
→ PM Agent
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
→ Review Agent
→ Final Output
```

반드시 설명:

- 사용자는 PM Agent에게만 요청
- PM Agent가 필요한 Agent로 작업 분해
- 각 Agent는 Domain Rules와 RAG 문서를 참조
- Review Agent가 최종 품질 검증
- 사용자는 최종 결과만 확인 가능

주의:

- 초기에는 순차 실행이 현실적
- 병렬 Agent 실행은 복잡도 증가
- 로컬 모델 환경에서는 속도와 메모리 제약 고려
- Agent별 Model / Tool 권한 분리 가능

---

# 27. Troubleshooting Rules

반드시 포함 추천.

형식:

```md
문제:

원인:

해결:
```

---

## Agent가 엉뚱한 일을 함

문제:

- Agent가 요청과 다른 작업을 수행함

원인:

- Role / Task가 불명확함
- Handoff에 Context 누락
- Output Format 미지정
- Agent 권한이 너무 넓음

해결:

- Role과 책임 범위 명확화
- Handoff Template 개선
- Expected Output 지정
- Agent별 Scope 제한

---

## Workflow가 끝나지 않음

문제:

- Agent가 계속 Review / Fix를 반복함

원인:

- Stop Condition 없음
- Max Iteration 없음
- Review 기준이 계속 바뀜
- Minor Issue까지 무한 수정

해결:

- Stop Condition 정의
- Max Iteration 설정
- Critical / Minor Issue 구분
- 일정 기준 이하 이슈는 사용자에게 보고 후 종료

---

## Agent 간 결과가 이어지지 않음

문제:

- 다음 Agent가 이전 Agent 결과를 제대로 활용하지 못함

원인:

- Intermediate Output 구조 불명확
- Shared State 누락
- Handoff Format 불일치
- 결정 사항 누락

해결:

- 공통 Output Schema 정의
- Shared State에 결정 사항 기록
- Handoff Template 통일
- Assumption / Open Issue 표시

---

## Review Agent가 쓸데없는 지적을 많이 함

문제:

- Review 결과가 실제 품질 개선과 무관함

원인:

- Review Criteria 불명확
- Severity 기준 없음
- 취향과 결함 구분 없음

해결:

- Review Checklist 정의
- Severity 기준 추가
- 문제 / 영향 / 수정 방향 구조화
- 프로젝트 규칙 기반 Review 수행

---

## PM Agent가 일을 너무 많이 함

문제:

- PM Agent가 라우팅이 아니라 구현까지 수행함

원인:

- PM Agent Role이 모호함
- Domain Agent Handoff가 없음
- Workflow가 단일 Agent처럼 동작

해결:

- PM Agent를 분석/분해/라우팅 중심으로 제한
- Domain Agent에게 명확히 Handoff
- PM Agent 출력 형식을 Task Plan 중심으로 변경

---

# 28. Best Practice Rules

Best Practice:

- Agent Role을 명확히 분리
- PM Agent는 요청 분석과 라우팅 중심
- Domain Agent는 전문 작업 중심
- Review Agent는 검증 중심
- Handoff Template을 통일
- Shared State에 요구사항과 결정 사항 기록
- 중간 결과는 구조화
- Review / Fix Loop에는 최대 반복 횟수 설정
- Stop Condition을 명확히 정의
- Tool 권한은 Agent별로 제한
- RAG 검색 범위는 Domain 기준으로 제한
- 위험 작업은 Human Confirmation 적용
- Workflow 실패 사례를 기록하고 개선

---

# 29. Comparison Rules

Agent Workflow 문서는 비교 기준을 포함한다.

필수 비교 대상:

- Single Agent vs Multi-Agent
- PM Agent vs Domain Agent
- Domain Agent vs Review Agent
- Sequential Workflow vs Router Workflow
- Review-Fix Loop vs Self-Check
- Shared State vs Conversation History
- Human-in-the-loop vs Full Automation
- Tool-based Workflow vs Prompt-only Workflow

예시:

| 비교 | Single Agent             | Multi-Agent                    |
| ---- | ------------------------ | ------------------------------ |
| 구조 | 하나의 Agent가 전체 처리 | 여러 Agent가 역할 분담         |
| 장점 | 단순하고 빠름            | 전문성/검증 품질 향상          |
| 단점 | 복잡 작업에 약함         | 느리고 설계 복잡               |
| 적합 | 단순 질의/작은 작업      | 개발 워크플로우/검증 필요 작업 |

---

# 30. Checklist Rules

Agent Workflow 문서에는 Checklist를 포함할 수 있다.

예시:

```md
### [Checklist]

- [ ] User Request가 명확히 분석되었는가?
- [ ] Task가 실행 가능한 단위로 분해되었는가?
- [ ] 각 Task에 담당 Agent가 지정되었는가?
- [ ] Handoff에 Context와 Expected Output이 포함되었는가?
- [ ] Shared State에 요구사항과 결정 사항이 기록되었는가?
- [ ] Review 기준이 명확한가?
- [ ] Fix Loop에 Max Iteration이 있는가?
- [ ] Stop Condition이 정의되어 있는가?
- [ ] Tool 권한이 Agent별로 제한되었는가?
- [ ] 위험 작업에 Human Confirmation이 있는가?
```

---

# 31. Retrieval Optimization Rules

강조 대상 키워드:

- Agent Workflow
- Agent Workflow Design
- Single Agent Workflow
- Multi-Agent Workflow
- PM Agent
- Domain Agent
- Review Agent
- Fix Agent
- Task Decomposition
- Agent Routing
- Agent Handoff
- Shared State
- Context Passing
- Intermediate Output
- Review Loop
- Fix Loop
- Stop Condition
- Failure Handling
- Human-in-the-loop
- RAG Integration
- Tool Calling Integration
- Memory Integration
- Workflow Evaluation
- Personal AI Development Team

키워드 반복 허용.

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

예:

- Agent Workflow가 뭐야?
- Multi-Agent는 언제 써?
- PM Agent는 무슨 역할이야?
- Agent 역할은 어떻게 나눠?
- Handoff는 어떻게 작성해?
- Shared State는 뭐야?
- Review-Fix Loop는 어떻게 설계해?
- Stop Condition은 왜 필요해?
- Agent가 무한 반복하면 어떻게 해?
- 개인 AI 개발팀 Workflow는 어떻게 구성해?

---

# 32. Version Rules

기준:

- Modern LLM Agent
- RAG 기반 Agent Workflow
- Tool Calling 연동 Agent
- Multi-Agent System Foundation
- PM Agent 중심 Workflow
- Sequential Agent Execution
- Review / Fix Loop
- Local LLM 기반 개인 AI 서버 구조 고려
- LangGraph / LangChain 확장 가능성 고려

Legacy 제외:

- 단순 Prompt Chain만 나열하는 방식
- Agent 역할 구분 없는 Workflow
- 종료 조건 없는 Agent Loop
- Tool 권한 제한 없는 Agent
- Review 없이 자동 완료하는 Agent Workflow

---

# 33. Common Mistakes

자주 발생:

- Agent 역할이 겹침
- PM Agent가 구현까지 담당
- Handoff가 모호함
- Shared State가 없음
- 중간 결과가 비구조적임
- Stop Condition 없음
- Review / Fix Loop가 무한 반복
- Review 기준이 모호함
- Tool 권한이 너무 넓음
- RAG 검색 범위가 너무 넓음
- 실패 처리 없이 성공 가정
- 사용자 확인이 필요한 작업을 자동 실행
- Agent 수를 너무 많이 늘림

---

# 34. Final Goal

Agent Workflow Design RAG 문서는 Agent가 아래를 수행 가능해야 한다.

- Agent Workflow 개념 설명
- Single Agent / Multi-Agent 구조 구분
- PM Agent 역할 정의
- Domain Agent 역할 정의
- Review Agent 역할 정의
- Task Decomposition 수행
- Agent Routing 기준 제안
- Handoff Template 작성
- Shared State 구조 설계
- Context Passing 기준 제안
- Review / Fix Loop 설계
- Stop Condition 정의
- Failure Handling 설계
- RAG / Tool / Memory Integration 방향 제안
- 개인 AI 개발팀 Workflow 설계
- Agent Workflow 문제 Troubleshooting

문서 품질이 Multi-Agent System의 실행 안정성과 결과 품질을 결정한다.

---

# Retrieval Queries

### [FAQ]

Q. Agent Workflow가 뭐야?

A.
사용자 요청을 Agent가 분석하고, 필요한 작업을 순서대로 실행하며, 검토와 수정을 거쳐 최종 결과를 만드는 흐름이다.

Q. Single Agent와 Multi-Agent 차이는?

A.
Single Agent는 하나의 Agent가 전체 작업을 처리하고, Multi-Agent는 여러 Agent가 역할을 나눠 처리한다.

Q. Multi-Agent는 언제 써?

A.
작업이 복잡하거나 Backend, Frontend, DevOps, Review처럼 전문 영역을 나누는 것이 품질에 도움이 될 때 사용한다.

Q. PM Agent는 무슨 역할이야?

A.
사용자 요청을 분석하고 작업을 분해하며, 적절한 Agent에게 라우팅하고 최종 결과를 통합한다.

Q. Domain Agent는 무슨 역할이야?

A.
Backend, Frontend, SQL, AI, DevOps처럼 특정 전문 영역의 작업을 수행한다.

Q. Review Agent는 왜 필요해?

A.
Domain Agent의 결과를 기준에 맞게 검증하고 문제, 원인, 수정 방향을 제시하기 위해 필요하다.

Q. Fix Agent는 무슨 역할이야?

A.
Review Agent가 발견한 문제를 반영해 산출물을 수정한다.

Q. Task Decomposition은 뭐야?

A.
큰 사용자 요청을 실행 가능한 작은 작업으로 나누고 담당 Agent와 완료 기준을 정하는 과정이다.

Q. Agent Routing은 어떻게 해?

A.
작업 Domain, 필요한 전문성, 필요한 Tool, 우선순위를 기준으로 담당 Agent를 선택한다.

Q. Handoff는 뭐야?

A.
한 Agent가 다음 Agent에게 작업, Context, 제약, 기대 출력 형식을 전달하는 구조화된 작업 전달이다.

Q. 좋은 Handoff에는 뭐가 들어가야 해?

A.
Source Agent, Target Agent, Task, Context, Constraints, Expected Output, Assumptions, Open Questions가 들어가야 한다.

Q. Shared State는 뭐야?

A.
Workflow 전체에서 공유되는 요구사항, 결정 사항, 중간 결과, Review 결과, 현재 상태를 저장하는 구조다.

Q. Context Passing은 왜 중요해?

A.
다음 Agent가 필요한 정보만 정확히 받아야 작업 품질이 높아지고 Token 낭비를 줄일 수 있기 때문이다.

Q. Review-Fix Loop는 어떻게 설계해?

A.
Domain Agent 결과를 Review Agent가 검증하고, 문제가 있으면 Fix Agent가 수정한 뒤 재검토하는 흐름으로 설계한다.

Q. Stop Condition은 왜 필요해?

A.
Agent가 무한 반복하지 않고 완료, 실패, 사용자 확인 필요 상태를 명확히 판단하기 위해 필요하다.

Q. Agent가 무한 반복하면 어떻게 해?

A.
Max Iteration, Severity 기준, Pass 조건, 사용자 확인 조건을 추가한다.

Q. Workflow 실패는 어떻게 처리해?

A.
실패 유형을 Missing Context, Tool Failure, Retrieval Failure, Invalid Output 등으로 분류하고 Retry, Fallback, 사용자 확인 중 하나를 선택한다.

Q. Human-in-the-loop는 언제 필요해?

A.
요구사항이 불명확하거나 파일 삭제, DB 변경, 배포, 비용 발생 작업처럼 위험한 작업 전에 필요하다.

Q. 개인 AI 개발팀 Workflow는 어떻게 구성해?

A.
User는 PM Agent에게 요청하고, PM Agent가 SQL, Backend, Frontend, AI, DevOps, Review Agent로 작업을 나눈 뒤 최종 결과를 통합한다.

Q. 처음부터 복잡한 Multi-Agent를 만들어야 해?

A.
아니다. 초기에는 순차 실행 기반의 단순 Workflow로 시작하고, 필요할 때 Agent와 Review Loop를 확장하는 것이 좋다.
