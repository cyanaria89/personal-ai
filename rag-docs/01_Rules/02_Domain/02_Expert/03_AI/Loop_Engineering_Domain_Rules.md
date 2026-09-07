# Loop Engineering Domain Rules

---

# 1. Domain Purpose

## 1.1 Loop Engineering 문서 목적

### [개념]

Loop Engineering은 AI Agent가 한 번 답변하고 종료하는 방식이 아니라, 목표 달성까지 계획, 실행, 검증, 수정, 재실행을 반복하도록 설계하는 영역이다.

Loop Engineering Domain 문서는 PM Agent / Backend Agent / Frontend Agent / SQL Agent / Review Agent / DevOps Agent / AI Agent가 반복 작업을 안전하게 수행하고, 실패를 분석하며, 완료 조건을 만족할 때까지 진행할 수 있도록 만드는 RAG 문서 제작 규칙이다.

---

### [핵심]

- Loop Engineering은 Agent 반복 실행 구조 설계이다.
- Prompt Engineering은 지시 설계이다.
- Context Engineering은 문맥 설계이다.
- Harness Engineering은 실행 기반 설계이다.
- Loop Engineering은 계획, 실행, 검증, 수정, 재시도, 종료 조건을 설계한다.
- Loop는 Agent가 스스로 결과를 점검하고 개선하는 구조이다.
- Loop Engineering은 Level 4 AI Expert 문서에 속한다.

---

### [실무]

2026 실무 기준 Loop Engineering 문서는 단순 반복 처리 설명이 아니라 Agent가 실제 개발 업무에서 오류를 줄이고 완성도를 높이기 위한 반복 제어 규칙을 제공해야 한다.

실무 Loop는 다음을 포함한다.

- Goal Definition
- Planning Loop
- Execution Loop
- Verification Loop
- Review Loop
- Repair Loop
- Retry Loop
- Reflection Loop
- Stop Condition
- Failure Escalation
- Human Approval
- State Update
- Tool Result Feedback
- Test Feedback
- Guardrail Feedback
- Cost / Token Control
- Infinite Loop Prevention

---

### [FAQ]

Q. Loop Engineering은 뭐야?

A. AI Agent가 목표 달성까지 계획, 실행, 검증, 수정, 재실행을 반복하도록 설계하는 영역이다.

Q. Loop Engineering은 Agent Workflow와 같아?

A. 아니다. Agent Workflow는 흐름이고 Loop Engineering은 그 흐름을 반복, 검증, 수정, 종료 조건까지 포함해 제어하는 심화 구조이다.

Q. Loop Engineering은 Harness Engineering과 뭐가 달라?

A. Harness Engineering은 실행 기반이고 Loop Engineering은 그 실행을 반복하며 개선하는 제어 구조이다.

Q. Loop Engineering은 Level 2야 Level 4야?

A. Level 4가 적절하다. 기본 Agent Workflow를 넘어서 반복 실행, 실패 복구, 완료 조건, 비용 제어를 다루기 때문이다.

---

# 2. Scope

## 2.1 포함 범위

### [개념]

Loop Engineering 문서는 Agent가 목표를 달성하기 위해 반복적으로 생각하고, 도구를 실행하고, 결과를 검증하고, 실패를 수정하는 구조를 다룬다.

---

### [핵심]

포함 범위:

- Agent Loop
- Planning Loop
- Execution Loop
- Verification Loop
- Review Loop
- Repair Loop
- Retry Loop
- Reflection Loop
- ReAct Loop
- Plan-Execute-Verify Loop
- Test-Fix Loop
- Code Review Loop
- RAG Retrieval Loop
- Tool Feedback Loop
- Multi-Agent Loop
- Human-in-the-Loop
- Stop Condition
- Exit Criteria
- Retry Limit
- Iteration Limit
- Loop State
- Loop Memory
- Failure Classification
- Error Recovery
- Escalation Policy
- Infinite Loop Prevention
- Cost Control
- Token Budget Control
- Latency Control
- Quality Gate
- Final Verification

---

### [실무]

개인 AI 개발팀 구조에서 Loop는 Agent별로 다르게 설계한다.

예시:

- Backend Agent Loop: 코드 작성 → 컴파일 → 테스트 → 실패 분석 → 수정 → 재테스트
- Frontend Agent Loop: 컴포넌트 수정 → 빌드 → UI 오류 확인 → 수정 → 재빌드
- SQL Agent Loop: 쿼리 작성 → 안전성 검증 → 실행 계획 확인 → 결과 검증 → 쿼리 수정
- Review Agent Loop: 결과 검토 → 문제 발견 → 수정 요청 → 재검토
- PM Agent Loop: 작업 분해 → Agent 호출 → 결과 취합 → 누락 확인 → 재지시
- DevOps Agent Loop: 배포 계획 → 검증 → dry-run → 승인 → 실행 → 모니터링
- AI Agent Loop: RAG 검색 → 답변 생성 → 근거 검증 → 재검색 → 답변 개선

---

### [FAQ]

Q. Loop Engineering 문서는 어떤 Agent에게 중요해?

A. 구현, 테스트, 리뷰, 배포, 검색, 검증을 반복해야 하는 모든 Agent에게 중요하다.

Q. Loop Engineering은 단순 retry랑 같아?

A. 아니다. Retry는 실패한 작업을 다시 시도하는 것이고 Loop Engineering은 계획, 검증, 수정, 종료 조건까지 포함한다.

Q. Loop Engineering에 Human-in-the-Loop도 포함돼?

A. 포함된다. 위험하거나 불확실한 반복은 사람 승인 또는 검토로 전환해야 한다.

Q. Loop Engineering은 Multi-Agent와 연결돼?

A. 연결된다. 한 Agent의 실패 결과가 다른 Agent의 수정 작업으로 이어질 수 있기 때문이다.

---

# 3. Exclusion Scope

## 3.1 제외 범위

### [개념]

Loop Engineering 문서는 반복 실행 구조를 다루지만, 모델 학습, 도구 기본 사용법, 인프라 운영 전체를 깊게 다루지는 않는다.

---

### [핵심]

제외 범위:

- Prompt Engineering 기본 이론
- Context Engineering 기본 이론
- Tool Calling 기본 문법
- LangGraph 기본 튜토리얼
- Harness 전체 실행 정책 상세
- Fine-Tuning 학습 과정
- Model Quantization 알고리즘
- MLOps 전체 운영 체계
- Vector Database 기본 사용법
- Embedding 모델 구조 상세
- 프론트엔드 UI 구현 상세
- 백엔드 비즈니스 로직 상세
- Kubernetes 운영 심화

---

### [실무]

연계 기준:

- 도구 실행 권한은 `Harness Engineering`
- 반복 실행 구조는 `Loop Engineering`
- 다중 Agent 연결은 `Advanced Multi-Agent Orchestration`
- 장기 실패 패턴 저장은 `Long-Term Memory`
- 반복 실행 로그 분석은 `AI Observability`
- 반복 품질 평가는 `Agent Evaluation & Guardrails`
- RAG 재검색 품질은 `RAG Evaluation & Retrieval Optimization`

---

### [FAQ]

Q. Loop Engineering에서 Tool Permission을 자세히 다뤄?

A. 아니다. Tool Permission은 Harness Engineering에서 자세히 다루고 Loop Engineering은 반복 중 도구 사용 결과를 어떻게 반영할지 다룬다.

Q. Loop Engineering에서 LangGraph 사용법을 자세히 다뤄?

A. 아니다. Loop 구조와 설계 기준은 다루지만 LangGraph 상세 문법은 별도 문서에서 다룬다.

Q. Loop Engineering에서 Fine-Tuning을 다뤄?

A. 아니다. Fine-Tuning은 모델 학습 영역이고 Loop Engineering은 Agent 실행 흐름 영역이다.

Q. Loop Engineering에서 RAG 검색 알고리즘을 다뤄?

A. 검색 알고리즘 자체는 다루지 않는다. 다만 검색 실패 시 재검색 Loop는 다룬다.

---

# 4. Section Priority

## 4.1 Required Sections

### [개념]

Loop Engineering 문서는 반드시 반복 실행, 검증, 수정, 종료 조건 중심으로 작성한다.

---

### [핵심]

필수 Section:

- [개념]
- [핵심]
- [실무]
- [FAQ]

강력 권장 Section:

- [Flow]
- [예제]
- [주의]
- [Best Practice]
- [Checklist]
- [Troubleshooting]
- [Comparison]

선택 Section:

- [Loop Pattern]
- [Stop Condition]
- [Failure Case]
- [Quality Gate]
- [Escalation]
- [Cost Control]
- [Review Point]

---

### [실무]

Loop Engineering 문서는 RAG 검색에 강해야 한다.

각 Chunk는 다음 키워드 중 하나 이상을 포함하는 것이 좋다.

- Loop Engineering
- Agent Loop
- Planning Loop
- Execution Loop
- Verification Loop
- Review Loop
- Repair Loop
- Retry Loop
- Reflection Loop
- Stop Condition
- Exit Criteria
- Infinite Loop Prevention
- Quality Gate
- Human-in-the-Loop
- Tool Feedback Loop
- Test-Fix Loop

---

### [FAQ]

Q. Loop Engineering 문서에 [Flow]가 필요해?

A. 필요하다. Loop는 반복 흐름이 핵심이므로 Flow로 표현해야 검색과 적용에 유리하다.

Q. Loop Engineering 문서에 [주의]가 필요한 이유는?

A. 무한 반복, 비용 폭증, 잘못된 수정 반복 같은 위험이 있기 때문이다.

Q. Loop Engineering 문서에 [Checklist]가 필요해?

A. 권장한다. Stop Condition, Retry Limit, Quality Gate 누락 여부를 검수하기 좋다.

Q. Loop Engineering 문서에 [Troubleshooting]이 필요해?

A. 권장한다. 반복 실패, 무한 루프, 검증 누락, 상태 손실 문제를 빠르게 찾을 수 있어야 한다.

---

# 5. Core Concept Rules

## 5.1 Agent Loop

### [개념]

Agent Loop는 Agent가 목표를 달성하기 위해 하나 이상의 작업 단계를 반복하는 구조이다.

Agent Loop는 단순 반복이 아니라 현재 상태를 확인하고, 도구 결과를 반영하고, 다음 행동을 결정하고, 완료 조건을 검사하는 제어 흐름이다.

---

### [핵심]

Agent Loop 구성요소:

- Goal
- Plan
- Step
- Action
- Tool Call
- Observation
- Evaluation
- Feedback
- Repair
- State Update
- Stop Condition
- Final Answer

---

### [Flow]

```text
Goal
→ Plan
→ Execute
→ Observe
→ Evaluate
→ Repair if Needed
→ Stop or Continue
→ Final Answer
```

---

### [실무]

Agent Loop는 다음 조건을 반드시 가진다.

- 목표가 명확해야 한다.
- 현재 단계가 추적되어야 한다.
- 도구 실행 결과가 저장되어야 한다.
- 실패 원인이 분류되어야 한다.
- 반복 횟수 제한이 있어야 한다.
- 완료 조건이 있어야 한다.
- 중단 조건이 있어야 한다.
- 필요 시 사람에게 전환해야 한다.

---

### [FAQ]

Q. Agent Loop는 왜 필요해?

A. 한 번의 답변이나 실행으로 목표를 달성하지 못하는 작업이 많기 때문이다.

Q. Agent Loop에 Stop Condition이 꼭 필요해?

A. 필요하다. Stop Condition이 없으면 무한 반복이나 비용 폭증이 발생할 수 있다.

Q. Agent Loop는 항상 자동으로 돌아야 해?

A. 아니다. 위험하거나 불확실한 단계는 Human-in-the-Loop으로 전환해야 한다.

Q. Agent Loop와 State는 무슨 관계야?

A. Loop는 현재 단계와 실패 이력을 기억해야 하므로 State Management가 필요하다.

---

# 6. Planning Loop Rules

## 6.1 Planning Loop 설계

### [개념]

Planning Loop는 Agent가 목표를 작업 단계로 나누고, 실행 전 계획을 점검하고, 부족한 정보가 있으면 계획을 수정하는 반복 구조이다.

---

### [핵심]

Planning Loop 필수 요소:

- Goal Analysis
- Requirement Extraction
- Task Decomposition
- Dependency Check
- Tool Availability Check
- Risk Check
- Missing Information Check
- Plan Revision
- Approval Check

---

### [Flow]

```text
User Request
→ Analyze Goal
→ Extract Requirements
→ Create Plan
→ Check Dependencies
→ Check Risk
→ Revise Plan
→ Execute
```

---

### [실무]

PM Agent는 Planning Loop를 강하게 사용한다.

PM Agent Planning Loop 예시:

```text
User Request
→ 작업 범위 분석
→ Backend / Frontend / SQL / Review 작업 분리
→ 필요한 문서 검색
→ 누락 정보 확인
→ 위험도 판단
→ Agent별 작업 할당
```

---

### [주의]

- 계획만 반복하고 실행하지 않는 상태 금지
- 과도하게 긴 계획 생성 금지
- 불필요한 세부 계획 남발 금지
- 요구사항과 무관한 작업 추가 금지
- 승인 필요한 작업을 자동 실행 계획에 넣지 않기

---

### [FAQ]

Q. Planning Loop는 언제 필요해?

A. 작업이 여러 단계이거나 여러 Agent가 협업해야 할 때 필요하다.

Q. Planning Loop가 너무 길어지면 어떻게 해?

A. 최소 실행 가능한 계획으로 줄이고, 실행 후 검증 Loop에서 보완한다.

Q. PM Agent는 Planning Loop를 써야 해?

A. 써야 한다. PM Agent는 작업 분해와 Agent 할당을 담당하기 때문이다.

Q. Planning Loop에서 approval check가 필요한 이유는?

A. 위험 작업이 계획에 포함되어 있는지 실행 전에 확인해야 하기 때문이다.

---

# 7. Execution Loop Rules

## 7.1 Execution Loop 설계

### [개념]

Execution Loop는 Agent가 계획된 단계를 실행하고, 도구 결과를 관찰하고, 다음 실행 단계를 결정하는 반복 구조이다.

---

### [핵심]

Execution Loop 필수 요소:

- Step Selection
- Tool Selection
- Permission Check
- Tool Execution
- Tool Result Capture
- Error Classification
- State Update
- Next Step Decision

---

### [Flow]

```text
Plan
→ Select Step
→ Select Tool
→ Check Permission
→ Execute Tool
→ Capture Result
→ Update State
→ Continue
```

---

### [실무]

Execution Loop는 Harness Engineering과 강하게 연결된다.

실무 기준:

- Tool Registry 기반 도구 선택
- Tool Permission 검증
- Input Validation 적용
- Timeout 적용
- Output Validation 적용
- Tool Result 구조화
- 실패 시 Error Handling으로 전달
- 성공 시 다음 단계로 진행

---

### [FAQ]

Q. Execution Loop는 Harness 없이 가능해?

A. 가능은 하지만 안전하지 않다. Tool 권한, 검증, 로그를 위해 Harness가 필요하다.

Q. Execution Loop에서 가장 중요한 것은?

A. Tool 실행 결과를 구조화하고 State에 반영하는 것이다.

Q. 실행 실패 시 바로 재시도하면 돼?

A. 아니다. 실패 원인을 분류하고 retryable 여부를 판단해야 한다.

Q. Execution Loop는 모든 Agent에 필요해?

A. 도구를 사용하는 Agent라면 필요하다.

---

# 8. Verification Loop Rules

## 8.1 Verification Loop 설계

### [개념]

Verification Loop는 Agent 실행 결과가 목표, 요구사항, 테스트, 규칙, 안전 기준을 만족하는지 확인하고, 부족하면 수정 단계로 보내는 반복 구조이다.

---

### [핵심]

Verification 대상:

- Requirement Match
- Test Result
- Build Result
- Code Review Result
- RAG Rule Compliance
- Output Format
- Security Rule
- Changed Files
- Tool Result
- User Constraint
- Domain Rules

---

### [Flow]

```text
Agent Result
→ Check Requirements
→ Check Tests
→ Check Rules
→ Check Risk
→ Pass or Repair
```

---

### [실무]

Verification Loop는 Review Agent와 연결하는 것이 좋다.

예시:

```text
Backend Agent Output
→ Review Agent 검토
→ 테스트 결과 확인
→ Domain Rules 확인
→ 문제 발견
→ Backend Agent 수정 요청
→ 재검증
```

---

### [주의]

- Agent 자기평가만으로 종료 금지
- 테스트 실패 무시 금지
- 출력 형식 검증 누락 금지
- 변경 범위 초과 검증 필요
- 보안 위험 검증 필요
- RAG 문서 필수 섹션 검증 필요

---

### [FAQ]

Q. Verification Loop는 왜 필요해?

A. Agent가 완료했다고 말해도 실제 요구사항을 만족하지 않을 수 있기 때문이다.

Q. Verification Loop는 Review Agent가 담당해도 돼?

A. 가능하다. 개인 AI 개발팀 구조에서는 Review Agent가 담당하는 것이 적절하다.

Q. 테스트 통과만 하면 검증 완료야?

A. 아니다. 요구사항, 보안, 출력 형식, 변경 범위도 확인해야 한다.

Q. Verification 실패 시 어떻게 해?

A. Repair Loop 또는 Human Review로 전환한다.

---

# 9. Repair Loop Rules

## 9.1 Repair Loop 설계

### [개념]

Repair Loop는 검증 실패, 테스트 실패, 빌드 실패, 리뷰 실패가 발생했을 때 원인을 분석하고 수정한 뒤 다시 검증하는 반복 구조이다.

---

### [핵심]

Repair Loop 필수 요소:

- Failure Input
- Root Cause Analysis
- Fix Plan
- Minimal Change
- Apply Fix
- Re-Test
- Re-Review
- Stop or Continue

---

### [Flow]

```text
Failure
→ Analyze Cause
→ Create Fix Plan
→ Apply Minimal Fix
→ Re-Test
→ Re-Verify
→ Pass or Escalate
```

---

### [실무]

Backend Agent Repair Loop 예시:

```text
Compile Error
→ 오류 로그 분석
→ 관련 파일 확인
→ 최소 수정
→ ./gradlew test
→ 실패 시 재분석
→ 성공 시 Review Agent 전달
```

Frontend Agent Repair Loop 예시:

```text
Build Error
→ 에러 메시지 분석
→ import / type / route 확인
→ 최소 수정
→ npm run build
→ 성공 여부 확인
```

---

### [주의]

- 원인 분석 없이 무작정 수정 금지
- 한 번에 너무 많은 파일 수정 금지
- 같은 실패를 반복하면 escalation 필요
- 실패 로그를 무시하지 않기
- 테스트 없이 완료 처리 금지
- 수정 범위가 요구사항을 넘지 않도록 제한

---

### [FAQ]

Q. Repair Loop는 언제 필요해?

A. 테스트 실패, 빌드 실패, 리뷰 실패, 출력 형식 실패가 발생했을 때 필요하다.

Q. Repair Loop에서 가장 중요한 것은?

A. 원인 분석 후 최소 수정하고 다시 검증하는 것이다.

Q. 같은 오류가 계속 나면 어떻게 해?

A. 반복 횟수 제한 후 Human Review 또는 상위 Agent에게 escalation한다.

Q. Repair Loop는 자동으로 계속 돌아도 돼?

A. 아니다. retryLimit과 stop condition이 필요하다.

---

# 10. Retry Loop Rules

## 10.1 Retry Loop 설계

### [개념]

Retry Loop는 일시적 실패가 발생했을 때 제한된 조건과 횟수 안에서 같은 작업을 다시 시도하는 구조이다.

---

### [핵심]

Retry 가능 오류:

- Temporary Network Error
- API Timeout
- Rate Limit 일부
- Temporary File Lock
- Transient Service Failure
- Flaky Test 일부

Retry 금지 오류:

- PermissionError
- ValidationError
- SchemaMismatch
- Security Blocked
- Human Approval Rejected
- Destructive Command Blocked
- Repeated Logic Error
- Missing Required Information

---

### [Flow]

```text
Tool Failure
→ Classify Error
→ Check Retryable
→ Check Retry Count
→ Retry or Stop
```

---

### [실무]

Retry Loop 기준:

- retryLimit 필수
- retryDelay 필수
- exponential backoff 권장
- retryable 여부 명시
- retry 로그 저장
- 같은 실패 반복 시 중단
- 비용 발생 작업 retry 주의
- destructive 작업 retry 금지

---

### [FAQ]

Q. Retry Loop와 Repair Loop는 뭐가 달라?

A. Retry Loop는 같은 작업을 다시 시도하는 것이고 Repair Loop는 원인을 수정한 뒤 다시 검증하는 것이다.

Q. Retry는 몇 번까지 허용해?

A. 일반적으로 1~3회로 제한한다.

Q. PermissionError도 retry해도 돼?

A. 안 된다. 권한 오류는 재시도해도 해결되지 않는다.

Q. Flaky Test는 retry해도 돼?

A. 제한적으로 가능하지만 반복되면 테스트 안정성 문제로 분류해야 한다.

---

# 11. Reflection Loop Rules

## 11.1 Reflection Loop 설계

### [개념]

Reflection Loop는 Agent가 자신의 계획, 실행 결과, 실패 원인, 답변 품질을 점검하고 개선 방향을 도출하는 반복 구조이다.

---

### [핵심]

Reflection 대상:

- Plan Quality
- Requirement Coverage
- Tool Result Interpretation
- Error Cause
- Answer Completeness
- Hallucination Risk
- Rule Compliance
- Missing Context
- Next Action

---

### [Flow]

```text
Draft Result
→ Self Check
→ Identify Gaps
→ Retrieve More Context if Needed
→ Revise Result
→ Final Verification
```

---

### [실무]

Reflection Loop는 유용하지만 과신하면 안 된다.

실무 기준:

- 자기평가만으로 최종 검증하지 않음
- 외부 검증 도구와 함께 사용
- 테스트 결과와 충돌하면 테스트 결과 우선
- RAG 근거와 충돌하면 근거 재확인
- 반복 횟수 제한
- 불확실하면 human review 요청

---

### [주의]

- 자기합리화 위험
- Hallucination을 스스로 정당화할 수 있음
- 같은 답변을 표현만 바꾸며 반복할 수 있음
- 비용 증가 가능
- 검증 도구 없이 reflection만 사용 금지

---

### [FAQ]

Q. Reflection Loop는 좋은 거야?

A. 유용하지만 단독 검증 수단으로 쓰면 위험하다. 테스트, 리뷰, RAG 근거 확인과 함께 사용해야 한다.

Q. Agent 자기평가만 믿어도 돼?

A. 안 된다. 자기평가는 보조 수단이고 외부 검증이 필요하다.

Q. Reflection Loop는 언제 쓰면 좋아?

A. 답변 누락, 요구사항 불일치, RAG 근거 부족, 계획 오류를 점검할 때 유용하다.

Q. Reflection Loop도 반복 제한이 필요해?

A. 필요하다. 무한 자기검토나 비용 폭증을 막아야 한다.

---

# 12. RAG Retrieval Loop Rules

## 12.1 Retrieval Loop 설계

### [개념]

RAG Retrieval Loop는 Agent가 검색 결과가 부족하거나 부정확할 때 검색 쿼리를 수정하고, 추가 검색하고, 근거를 재검증하는 반복 구조이다.

---

### [핵심]

Retrieval Loop 단계:

- Initial Query
- Retrieve Documents
- Evaluate Relevance
- Detect Missing Context
- Rewrite Query
- Re-Retrieve
- Rerank
- Validate Evidence
- Generate Answer

---

### [Flow]

```text
Question
→ Initial Retrieval
→ Relevance Check
→ Query Rewrite
→ Re-Retrieval
→ Evidence Validation
→ Answer
```

---

### [실무]

RAG 문서 제작 Agent는 Retrieval Loop를 사용해야 한다.

사용 기준:

- 검색 결과가 질문과 맞지 않음
- 문서 근거가 부족함
- 용어가 혼재되어 있음
- 문서 간 충돌이 있음
- 필요한 Domain Rules를 찾지 못함
- 답변 근거가 약함

---

### [주의]

- 무한 재검색 금지
- 검색어만 바꾸며 반복 금지
- 관련 없는 문서 억지 사용 금지
- 낮은 관련도 문서로 확정 답변 금지
- 문서에 없는 내용을 있는 것처럼 답변 금지

---

### [FAQ]

Q. RAG Retrieval Loop는 언제 필요해?

A. 첫 검색 결과가 부족하거나 질문과 맞지 않을 때 필요하다.

Q. Query Rewrite는 왜 필요해?

A. 사용자의 표현과 문서의 표현이 다를 수 있기 때문이다.

Q. 검색 결과가 계속 부족하면 어떻게 해?

A. 검색을 중단하고 문서 부족 또는 근거 부족으로 보고해야 한다.

Q. Retrieval Loop도 제한이 필요해?

A. 필요하다. 보통 1~3회 재검색 후 중단하는 것이 안전하다.

---

# 13. Test-Fix Loop Rules

## 13.1 Test-Fix Loop 설계

### [개념]

Test-Fix Loop는 코드 수정 후 테스트를 실행하고, 실패 원인을 분석하고, 다시 수정하고, 테스트를 재실행하는 개발 Agent 반복 구조이다.

---

### [핵심]

Test-Fix Loop 단계:

- Code Change
- Run Test
- Parse Error
- Classify Failure
- Fix Code
- Re-Run Test
- Confirm Pass
- Report Result

---

### [Flow]

```text
Code Change
→ Run Tests
→ Test Failed?
→ Analyze Error
→ Fix Code
→ Re-Run Tests
→ Pass
```

---

### [실무]

Backend Agent 기준:

```text
Modify Java Code
→ ./gradlew test
→ Compile Error 확인
→ Unit Test Failure 확인
→ 최소 수정
→ ./gradlew test 재실행
→ 결과 보고
```

Frontend Agent 기준:

```text
Modify React Code
→ npm run build
→ Type / Import / Route Error 확인
→ 최소 수정
→ npm run build 재실행
→ 결과 보고
```

---

### [주의]

- 테스트 없이 완료 보고 금지
- 실패 로그 일부만 보고 추측 수정 금지
- 테스트 실패를 무시하고 통과 처리 금지
- 하나의 실패를 고치다가 관련 없는 리팩토링 금지
- 반복 실패 시 escalation 필요

---

### [FAQ]

Q. Test-Fix Loop는 왜 필요해?

A. 코드 생성 Agent가 만든 코드가 처음부터 항상 컴파일되거나 테스트를 통과하지는 않기 때문이다.

Q. 테스트가 없으면 어떻게 해?

A. 빌드, 린트, 타입 체크, 정적 분석 같은 대체 검증을 사용한다.

Q. 테스트 실패가 계속되면 어떻게 해?

A. 반복 횟수를 제한하고 실패 로그와 수정 이력을 보고해야 한다.

Q. Test-Fix Loop에서 핵심은 뭐야?

A. 최소 수정, 재테스트, 실패 원인 기록이다.

---

# 14. Review Loop Rules

## 14.1 Review Loop 설계

### [개념]

Review Loop는 Agent 작업 결과를 검토하고, 문제를 발견하면 수정 요청을 보내고, 수정 결과를 다시 검토하는 반복 구조이다.

---

### [핵심]

Review Loop 대상:

- Code Diff
- Test Result
- Build Result
- Security Risk
- Domain Rules
- Output Format
- RAG Structure
- User Requirement
- Regression Risk
- Performance Risk

---

### [Flow]

```text
Agent Output
→ Review
→ Issue Found?
→ Request Fix
→ Apply Fix
→ Re-Review
→ Approve
```

---

### [실무]

Review Agent는 다음 기준으로 검토한다.

- 요구사항 충족 여부
- 변경 범위 초과 여부
- 코드 품질
- 테스트 결과
- 보안 위험
- 파일 간 연계 문제
- RAG 문서 형식
- Retrieval Queries 포함 여부
- 치명적 문제 여부

---

### [주의]

- 리뷰 없이 최종 출력 금지
- 사소한 스타일 문제로 무한 반복 금지
- 치명적 문제와 개선 제안을 구분
- 변경 범위 외 수정 요구 금지
- Review 결과는 구조화해서 전달

---

### [FAQ]

Q. Review Loop는 왜 필요해?

A. Agent가 만든 결과를 별도 기준으로 검증하고 품질을 높이기 위해 필요하다.

Q. Review Agent가 수정도 해야 해?

A. 보통 Review Agent는 문제를 식별하고 수정은 담당 Agent에게 요청하는 구조가 좋다.

Q. Review Loop가 무한 반복되면 어떻게 해?

A. 반복 횟수를 제한하고 사소한 개선은 기록만 남기며 종료한다.

Q. Review Loop에서 가장 중요한 것은?

A. 치명적 문제와 단순 개선점을 구분하는 것이다.

---

# 15. Multi-Agent Loop Rules

## 15.1 Multi-Agent Loop 설계

### [개념]

Multi-Agent Loop는 여러 Agent가 각자의 역할을 수행하고, 결과를 주고받고, 검증과 수정을 반복하는 협업 구조이다.

---

### [핵심]

Multi-Agent Loop 구성:

- PM Agent
- Task Assignment
- Specialist Agent
- Tool Execution
- Review Agent
- Feedback
- Repair
- Final Integration
- Final Verification

---

### [Flow]

```text
User Request
→ PM Agent
→ Specialist Agent
→ Review Agent
→ Fix Request
→ Specialist Agent Repair
→ Review Again
→ PM Final Integration
```

---

### [실무]

개인 AI 개발팀 기본 Loop:

```text
User
→ PM Agent
→ SQL Agent
→ Backend Agent
→ Frontend Agent
→ Review Agent
→ Fix Loop
→ Final Output
```

적용 기준:

- PM Agent는 전체 State 관리
- Specialist Agent는 역할별 작업 수행
- Review Agent는 검증 수행
- 실패 시 원래 Agent로 반환
- 반복 횟수 제한
- 최종 결과는 PM Agent가 통합

---

### [주의]

- Agent 간 책임 불명확 금지
- 같은 작업을 여러 Agent가 중복 수행 금지
- Review 없이 최종 통합 금지
- PM Agent가 State를 잃지 않도록 관리
- Agent 간 출력 형식 통일
- 실패 원인을 명확히 전달

---

### [FAQ]

Q. Multi-Agent Loop는 언제 필요해?

A. 작업이 SQL, Backend, Frontend, Review처럼 역할별로 나뉠 때 필요하다.

Q. PM Agent의 역할은 뭐야?

A. 작업 분해, Agent 할당, State 관리, 결과 통합, 최종 검증이다.

Q. Review Agent는 왜 필요해?

A. Specialist Agent의 결과를 별도 기준으로 검증하기 위해 필요하다.

Q. Multi-Agent Loop의 가장 큰 위험은?

A. Agent 간 책임 불명확, 상태 손실, 무한 수정 반복이다.

---

# 16. Human-in-the-Loop Rules

## 16.1 Human-in-the-Loop 전환 기준

### [개념]

Human-in-the-Loop은 Agent Loop가 자동으로 해결하기 어렵거나 위험한 상황에서 사람의 판단을 요청하는 구조이다.

---

### [핵심]

Human Review 필요 조건:

- 요구사항이 모호함
- 반복 실패 발생
- 위험 작업 포함
- 비용 발생 작업 포함
- DB 변경 필요
- 배포 필요
- Secret 접근 필요
- 삭제 작업 필요
- 보안 위험 존재
- 충돌하는 규칙 존재
- 문서 근거 부족
- Agent 판단 신뢰도 낮음

---

### [Flow]

```text
Loop Running
→ Risk or Uncertainty Detected
→ Pause Loop
→ Request Human Decision
→ Continue or Abort
```

---

### [실무]

Human-in-the-Loop 요청에는 다음 정보를 포함한다.

- 현재 목표
- 진행 단계
- 발생 문제
- 선택 가능한 옵션
- 각 옵션의 영향
- 위험도
- 추천안
- 필요한 승인

---

### [주의]

- 불필요한 승인 요청 남발 금지
- 위험 작업 자동 진행 금지
- 사람의 결정을 무시하고 재실행 금지
- 승인 결과를 State에 기록
- 승인 범위를 초과하지 않기

---

### [FAQ]

Q. Loop 중 언제 사람에게 물어봐야 해?

A. 위험하거나 되돌리기 어렵거나 요구사항이 모호한 경우 사람에게 전환해야 한다.

Q. Human-in-the-Loop은 자동화를 방해하지 않아?

A. 방해가 아니라 위험한 자동화를 안전하게 만드는 제어 장치이다.

Q. 승인 후에도 검증이 필요해?

A. 필요하다. 승인받은 작업도 실행 후 결과 검증을 해야 한다.

Q. 사람이 거절하면 어떻게 해?

A. Loop를 중단하거나 안전한 대안으로 계획을 수정한다.

---

# 17. Stop Condition Rules

## 17.1 Stop Condition 설계

### [개념]

Stop Condition은 Loop가 언제 종료되어야 하는지 정의하는 조건이다.

Stop Condition이 없으면 Agent는 무한 반복하거나 불필요한 비용을 사용할 수 있다.

---

### [핵심]

종료 조건 예시:

- 목표 달성
- 테스트 통과
- Review 통과
- 요구사항 충족
- 출력 형식 검증 완료
- 최대 반복 횟수 도달
- 재시도 불가능 오류 발생
- Human Approval 거절
- 비용 한도 도달
- 시간 한도 도달
- 안전 정책 위반
- 필요한 정보 부족

---

### [Flow]

```text
Loop Step Complete
→ Check Success Condition
→ Check Failure Condition
→ Check Limit
→ Continue or Stop
```

---

### [실무]

Loop마다 Stop Condition을 명시한다.

예시:

Backend Test-Fix Loop Stop Condition:

- `./gradlew test` 성공
- 같은 실패 2회 반복
- 수정 범위 초과 필요
- 권한 없는 파일 수정 필요
- 최대 반복 횟수 도달

RAG Retrieval Loop Stop Condition:

- 충분한 관련 문서 확보
- 재검색 3회 초과
- 근거 부족 확정
- 충돌 문서 발견 후 human review 필요

---

### [FAQ]

Q. Stop Condition은 왜 필요해?

A. 무한 반복, 비용 폭증, 잘못된 수정 반복을 막기 위해 필요하다.

Q. 성공 조건만 있으면 돼?

A. 아니다. 실패 조건, 제한 조건, 사람 전환 조건도 필요하다.

Q. 최대 반복 횟수는 어느 정도가 좋아?

A. 작업 종류에 따라 다르지만 보통 2~5회 제한이 안전하다.

Q. Stop Condition에 비용 한도도 포함해야 해?

A. 포함하는 것이 좋다. LLM 호출과 도구 실행 비용을 통제해야 하기 때문이다.

---

# 18. Infinite Loop Prevention Rules

## 18.1 무한 루프 방지

### [개념]

Infinite Loop Prevention은 Agent가 같은 작업, 같은 실패, 같은 검색, 같은 수정을 끝없이 반복하지 않도록 막는 규칙이다.

---

### [핵심]

무한 루프 원인:

- Stop Condition 없음
- Retry Limit 없음
- State 저장 없음
- 실패 원인 분류 없음
- 같은 실패 반복 감지 없음
- 목표가 모호함
- 검증 기준 없음
- Agent 자기평가만 사용
- 도구 결과를 무시함
- Query Rewrite만 반복함

---

### [실무]

방지 기준:

- maxIterations 설정
- retryLimit 설정
- sameErrorLimit 설정
- State에 실패 이력 저장
- 반복 패턴 감지
- 실패 원인 분류
- 일정 횟수 후 escalation
- 비용 한도 설정
- 시간 한도 설정
- Human Review 전환

---

### [주의]

나쁜 Loop:

```text
Test Failed
→ Fix
→ Test Failed
→ Fix
→ Test Failed
→ Fix
→ 계속 반복
```

좋은 Loop:

```text
Test Failed
→ Analyze Error
→ Fix
→ Re-Test
→ Same Error Detected
→ Retry Limit Reached
→ Escalate
```

---

### [FAQ]

Q. Loop가 무한 반복되는 가장 흔한 이유는?

A. Stop Condition과 State Management가 없기 때문이다.

Q. 같은 오류가 반복되면 어떻게 해야 해?

A. 같은 오류 반복 횟수를 제한하고 human review 또는 상위 Agent에게 escalation해야 한다.

Q. 무한 재검색도 Loop 문제야?

A. 그렇다. Retrieval Loop에도 재검색 횟수 제한이 필요하다.

Q. Agent가 계속 다른 수정만 하면 괜찮아?

A. 아니다. 목표 달성 없이 변경만 늘어나면 중단하고 검토해야 한다.

---

# 19. Loop State Rules

## 19.1 Loop State Management

### [개념]

Loop State는 반복 실행 중 현재 목표, 단계, 시도 횟수, 실패 이력, 도구 결과, 변경 내용, 검증 결과를 저장하는 상태 정보이다.

---

### [핵심]

Loop State 필수 항목:

- loopId
- taskId
- goal
- currentStep
- iterationCount
- maxIterations
- toolCalls
- toolResults
- errors
- repeatedErrors
- changedFiles
- verificationResult
- approvalStatus
- stopReason
- finalStatus

---

### [예제]

```json
{
  "loopId": "loop-001",
  "taskId": "task-2026-001",
  "goal": "Fix backend test failure",
  "currentStep": "repair",
  "iterationCount": 2,
  "maxIterations": 3,
  "finalStatus": "running"
}
```

---

### [실무]

Loop State는 PM Agent와 Harness가 함께 관리한다.

실무 기준:

- 반복 횟수 저장
- 같은 오류 반복 감지
- 도구 결과 저장
- 변경 파일 저장
- 검증 결과 저장
- 중단 이유 저장
- Agent 간 전달 가능한 구조 사용

---

### [FAQ]

Q. Loop State는 왜 필요해?

A. Agent가 현재 반복 단계와 실패 이력을 추적해야 안전하게 다음 행동을 결정할 수 있기 때문이다.

Q. Loop State와 Harness State는 같아?

A. 겹치지만 Loop State는 반복 실행에 필요한 iteration, stopReason, repeatedErrors에 더 초점을 둔다.

Q. Loop State를 저장하지 않으면 어떻게 돼?

A. 같은 작업 반복, 실패 원인 손실, 무한 루프, 잘못된 완료 판단이 발생할 수 있다.

Q. Multi-Agent에서도 Loop State가 필요해?

A. 필요하다. PM Agent가 각 Agent의 반복 상태를 관리해야 한다.

---

# 20. Quality Gate Rules

## 20.1 Quality Gate 설계

### [개념]

Quality Gate는 Loop가 다음 단계로 넘어가거나 종료되기 전에 반드시 통과해야 하는 품질 기준이다.

---

### [핵심]

Quality Gate 예시:

- Requirement Gate
- Test Gate
- Build Gate
- Security Gate
- Review Gate
- Format Gate
- Retrieval Evidence Gate
- Performance Gate
- Cost Gate
- Human Approval Gate

---

### [Flow]

```text
Loop Result
→ Quality Gate Check
→ Pass
→ Continue or Finish

Loop Result
→ Quality Gate Check
→ Fail
→ Repair or Escalate
```

---

### [실무]

RAG 문서 제작 Quality Gate:

- 출력 형식 준수
- [개념], [핵심], [실무], [FAQ] 포함
- Retrieval Queries 포함
- 용어 통일
- 코드블록 id 제거
- 중복 설명 최소화
- FAQ 강화
- 문서 간 연계 확인
- 치명적 문제 확인

개발 Agent Quality Gate:

- 빌드 성공
- 테스트 성공
- lint 통과
- 변경 범위 적절
- 보안 위험 없음
- Review Agent 승인

---

### [FAQ]

Q. Quality Gate는 왜 필요해?

A. Loop가 낮은 품질의 결과를 완료로 처리하지 않도록 막기 위해 필요하다.

Q. Quality Gate를 너무 많이 두면 문제야?

A. 가능하다. 핵심 품질 기준 위주로 설정해야 Loop가 불필요하게 길어지지 않는다.

Q. RAG 문서 제작에도 Quality Gate가 필요해?

A. 필요하다. 출력 형식, 필수 섹션, Retrieval Queries, 용어 통일을 검증해야 한다.

Q. Quality Gate 실패 시 어떻게 해?

A. Repair Loop로 이동하거나 반복 제한 초과 시 escalation한다.

---

# 21. Cost and Token Control Rules

## 21.1 Cost / Token Control

### [개념]

Cost and Token Control은 Loop가 반복되면서 LLM 호출 비용, 토큰 사용량, 실행 시간을 과도하게 사용하지 않도록 제한하는 규칙이다.

---

### [핵심]

제어 대상:

- Max Iterations
- Max Tool Calls
- Max Retrieval Count
- Max Tokens
- Max Runtime
- API Cost Limit
- Rate Limit
- Context Size
- Log Size
- Reflection Count

---

### [실무]

Loop 비용 제어 기준:

- 반복 횟수 제한
- 재검색 횟수 제한
- Reflection 횟수 제한
- 불필요한 전체 파일 재읽기 금지
- 필요한 Chunk만 검색
- 긴 로그 전체 재주입 금지
- 실패 로그 요약 사용
- 비용 발생 API 호출 전 승인
- 대형 모델 호출 최소화
- 작은 작업은 작은 모델 사용 고려

---

### [주의]

- Loop가 길어질수록 비용과 지연 증가
- Reflection 반복은 비용 증가 원인
- RAG 재검색 반복은 latency 증가
- 긴 Context 재주입은 품질 저하 가능
- 불필요한 Multi-Agent 호출 금지

---

### [FAQ]

Q. Loop Engineering에서 비용 제어가 왜 중요해?

A. 반복 구조는 LLM 호출, 도구 실행, 검색 횟수를 늘려 비용과 시간이 커질 수 있기 때문이다.

Q. Token Budget은 어떻게 관리해?

A. 필요한 문서 Chunk만 사용하고, 이전 결과는 요약 State로 유지하며, 반복 횟수를 제한한다.

Q. Reflection Loop는 비용이 많이 들어?

A. 가능하다. Reflection 횟수를 제한하고 중요한 단계에서만 사용해야 한다.

Q. 재검색은 몇 번까지 하는 게 좋아?

A. 보통 1~3회로 제한하고 계속 부족하면 근거 부족으로 보고한다.

---

# 22. Escalation Rules

## 22.1 Escalation Policy

### [개념]

Escalation은 Agent Loop가 자동으로 해결할 수 없는 문제를 상위 Agent, Review Agent, 사람에게 넘기는 구조이다.

---

### [핵심]

Escalation 조건:

- 최대 반복 횟수 도달
- 같은 오류 반복
- 권한 부족
- 승인 필요 작업
- 보안 위험
- 요구사항 모호
- 문서 근거 부족
- 테스트 계속 실패
- 도구 계속 실패
- 비용 한도 초과
- 충돌하는 규칙 발견

---

### [Flow]

```text
Loop Failure
→ Check Escalation Condition
→ Prepare Summary
→ Send to PM / Review / Human
→ Wait Decision
```

---

### [실무]

Escalation Summary 필수 정보:

- 원래 목표
- 현재 상태
- 시도한 작업
- 실패 원인
- 반복 횟수
- 관련 로그
- 변경 파일
- 가능한 대안
- 추천 결정

---

### [FAQ]

Q. Escalation은 실패야?

A. 아니다. 자동 처리가 위험하거나 불확실할 때 안전하게 상위 판단으로 넘기는 정상 흐름이다.

Q. 같은 오류가 몇 번 반복되면 escalation해?

A. 보통 2~3회 반복되면 escalation하는 것이 안전하다.

Q. Escalation 대상은 누구야?

A. PM Agent, Review Agent, DevOps Agent, 또는 사람일 수 있다.

Q. Escalation Summary가 필요한 이유는?

A. 다음 판단자가 전체 반복 과정을 다시 추적하지 않아도 되게 하기 위해 필요하다.

---

# 23. Loop Pattern Rules

## 23.1 대표 Loop Pattern

### [개념]

Loop Pattern은 반복 실행 구조를 재사용 가능한 형태로 정리한 것이다.

---

### [핵심]

대표 Pattern:

- Plan-Execute-Verify
- ReAct Loop
- Test-Fix Loop
- Review-Fix Loop
- Retrieve-Validate-Retrieve
- Generate-Critique-Revise
- Tool-Observe-Repair
- PM-Delegate-Review-Integrate
- Human Approval Loop

---

### [실무]

Pattern 선택 기준:

| 상황             | 권장 Loop Pattern            |
| ---------------- | ---------------------------- |
| 개발 작업        | Plan-Execute-Verify          |
| 코드 오류 수정   | Test-Fix Loop                |
| 리뷰 기반 개선   | Review-Fix Loop              |
| RAG 근거 부족    | Retrieve-Validate-Retrieve   |
| 답변 품질 개선   | Generate-Critique-Revise     |
| 도구 실행 실패   | Tool-Observe-Repair          |
| Multi-Agent 협업 | PM-Delegate-Review-Integrate |
| 위험 작업        | Human Approval Loop          |

---

### [FAQ]

Q. 모든 작업에 같은 Loop Pattern을 써도 돼?

A. 아니다. 작업 성격에 따라 적절한 Loop Pattern을 선택해야 한다.

Q. 개발 작업에는 어떤 Loop가 좋아?

A. Plan-Execute-Verify와 Test-Fix Loop가 적합하다.

Q. RAG 답변에는 어떤 Loop가 좋아?

A. Retrieve-Validate-Retrieve와 Generate-Critique-Revise가 적합하다.

Q. 위험 작업에는 어떤 Loop가 좋아?

A. Human Approval Loop가 필요하다.

---

# 24. Comparison Rules

## 24.1 관련 개념 비교

### [개념]

Loop Engineering은 여러 AI Agent 개념과 연결되지만 동일하지 않다.

---

### [Comparison]

| 개념                      | 의미             | Loop와 관계                     |
| ------------------------- | ---------------- | ------------------------------- |
| Prompt Engineering        | 모델 지시문 설계 | Loop의 각 단계에 지시문 사용    |
| Context Engineering       | 문맥 구성 설계   | Loop 단계별 필요한 Context 제공 |
| Harness Engineering       | 실행 기반 설계   | Loop가 실행될 수 있는 기반 제공 |
| Tool Calling              | 도구 호출 방식   | Execution Loop에서 사용         |
| Agent Workflow            | Agent 작업 흐름  | Loop Engineering의 기초         |
| Retry Policy              | 실패 재시도 규칙 | Retry Loop의 일부               |
| Reflection                | 자기 점검        | Reflection Loop의 일부          |
| Multi-Agent Orchestration | 여러 Agent 협업  | Multi-Agent Loop를 구성         |
| Long-Term Memory          | 장기 기억        | 반복 실패와 결정 이력 저장      |
| AI Observability          | 관찰 가능성      | Loop 로그와 trace 분석          |
| Guardrails                | 안전 규칙        | Loop 중 위험 행동 차단          |

---

### [실무]

문서 작성 시 혼동 방지:

- Loop Engineering을 단순 Retry로 축소하지 않는다.
- Loop Engineering을 Agent Workflow 기본 흐름으로 축소하지 않는다.
- Loop Engineering을 Reflection만으로 설명하지 않는다.
- Loop Engineering은 반복 실행, 검증, 수정, 종료 조건 전체를 다룬다.
- Loop Engineering은 Harness Engineering과 함께 설계한다.

---

### [FAQ]

Q. Loop Engineering과 Retry Policy 차이는?

A. Retry Policy는 재시도 규칙이고 Loop Engineering은 계획, 실행, 검증, 수정, 종료 조건을 포함한 반복 구조이다.

Q. Loop Engineering과 Reflection 차이는?

A. Reflection은 자기 점검이고 Loop Engineering은 Reflection을 포함할 수 있는 전체 반복 설계이다.

Q. Loop Engineering과 Harness Engineering 차이는?

A. Harness는 실행 기반이고 Loop는 반복 제어 구조이다.

Q. Loop Engineering과 Multi-Agent Orchestration 차이는?

A. Loop는 반복 구조이고 Multi-Agent Orchestration은 여러 Agent를 연결하는 지휘 구조이다.

---

# 25. Best Practice Rules

## 25.1 Loop Engineering Best Practice

### [개념]

Best Practice는 Agent Loop를 안전하고, 효율적이고, 검증 가능하게 만들기 위한 기준이다.

---

### [Best Practice]

- 목표를 명확히 정의
- Loop State 저장
- maxIterations 설정
- retryLimit 설정
- Stop Condition 명시
- Exit Criteria 명시
- Quality Gate 적용
- Tool Result 구조화
- 실패 원인 분류
- 같은 오류 반복 감지
- Test-Fix Loop 적용
- Review Loop 적용
- Human-in-the-Loop 전환 기준 설정
- Cost / Token Budget 설정
- 로그와 trace 저장
- 무한 루프 방지
- Reflection은 보조 수단으로 사용
- 외부 검증 도구 우선
- 위험 작업은 자동 반복 금지
- 반복 실패 시 escalation
- 변경 범위 최소화
- 최종 검증 후 완료 처리

---

### [실무]

개인 AI 개발팀 기준 우선 적용 순서:

1. Goal Definition
2. Loop State
3. Stop Condition
4. maxIterations
5. Quality Gate
6. Tool Feedback
7. Verification Loop
8. Repair Loop
9. Review Loop
10. Escalation Policy
11. Cost Control
12. Human-in-the-Loop
13. Observability 연계
14. Long-Term Memory 연계

---

### [FAQ]

Q. Loop Engineering에서 가장 먼저 정해야 하는 것은?

A. 목표, 완료 조건, 최대 반복 횟수를 먼저 정해야 한다.

Q. Loop를 처음부터 복잡하게 만들어야 해?

A. 아니다. Plan → Execute → Verify → Repair 구조부터 시작하고 점진적으로 확장한다.

Q. Loop Best Practice의 핵심은 뭐야?

A. 목표 명확화, 상태 저장, 검증, 반복 제한, 중단 조건, escalation이다.

Q. Reflection을 많이 넣으면 품질이 좋아져?

A. 항상 그렇지 않다. Reflection은 비용을 늘릴 수 있으므로 중요한 단계에서 제한적으로 사용한다.

---

# 26. Common Mistakes

## 26.1 Loop Engineering 자주 발생하는 실수

### [개념]

Loop Engineering에서 가장 흔한 문제는 반복 조건과 종료 조건을 명확히 두지 않아 무한 반복하거나 잘못된 결과를 완료로 처리하는 것이다.

---

### [핵심]

자주 발생하는 실수:

- Stop Condition 없음
- maxIterations 없음
- retryLimit 없음
- Loop State 없음
- 같은 오류 반복 감지 없음
- 실패 원인 분류 없음
- 테스트 없이 완료 처리
- Review 없이 완료 처리
- Reflection만 믿고 완료 처리
- Tool Result 무시
- 검증 실패를 성공으로 처리
- 요구사항과 무관한 수정 반복
- 비용 한도 없음
- Token Budget 없음
- RAG 재검색 무한 반복
- Agent 간 책임 불명확
- Escalation 없음
- Human Approval 누락
- 위험 작업 자동 반복
- 로그 없음
- 변경 이력 없음

---

### [주의]

치명적 실수:

- 무한 Test-Fix Loop
- 무한 RAG Retrieval Loop
- 무한 Reflection Loop
- Production 작업 자동 재시도
- DB 변경 자동 반복
- 배포 실패 자동 반복
- 보안 차단 무시
- 같은 오류를 계속 다른 방식으로 수정
- 완료 조건 없이 "좋아질 때까지" 반복
- 실패 로그를 저장하지 않음

---

### [FAQ]

Q. Loop Engineering에서 가장 위험한 실수는?

A. Stop Condition 없이 Agent를 반복 실행시키는 것이다.

Q. Reflection Loop만 쓰면 안 돼?

A. 안 된다. 자기평가는 보조 수단이고 테스트, 리뷰, 도구 결과 같은 외부 검증이 필요하다.

Q. 실패 원인 분류가 없으면 왜 문제야?

A. 재시도할 문제와 중단할 문제를 구분하지 못해 무한 반복이 발생할 수 있다.

Q. 비용 한도가 없으면 어떤 문제가 생겨?

A. LLM 호출, API 호출, 검색, 도구 실행이 반복되어 비용과 시간이 급증할 수 있다.

---

# 27. Troubleshooting Rules

## 27.1 Infinite Loop

### [Troubleshooting]

문제:

- Agent가 같은 작업을 계속 반복함

원인:

- Stop Condition 없음
- maxIterations 없음
- State 저장 없음
- 같은 오류 반복 감지 없음
- 목표가 모호함
- 검증 기준 없음

해결:

- Stop Condition 추가
- maxIterations 설정
- Loop State 저장
- repeatedErrors 추적
- 목표와 완료 조건 재정의
- 반복 실패 시 escalation

---

## 27.2 Repeated Test Failure

### [Troubleshooting]

문제:

- Test-Fix Loop에서 같은 테스트가 계속 실패함

원인:

- 실패 원인 분석 오류
- 관련 파일 누락
- 잘못된 수정 반복
- 테스트 데이터 문제
- 환경 설정 문제
- 요구사항 오해

해결:

- 실패 로그 전체 확인
- 같은 오류 반복 여부 확인
- 최근 변경 diff 확인
- 테스트 환경 확인
- 수정 범위 최소화
- 2~3회 실패 후 Review Agent 또는 Human Review로 전환

---

## 27.3 Retrieval Loop Failure

### [Troubleshooting]

문제:

- RAG 검색을 반복해도 필요한 문서를 찾지 못함

원인:

- 검색어가 문서 용어와 다름
- 문서 자체가 없음
- Chunk 품질 낮음
- 유사 문서가 너무 많음
- Retrieval Queries 부족
- Domain Rules 미작성

해결:

- Query Rewrite 수행
- 핵심 용어로 재검색
- 문서명과 Domain 기준으로 검색
- 재검색 횟수 제한
- 근거 부족으로 보고
- 필요한 문서 제작 대상으로 등록

---

## 27.4 Reflection Loop Drift

### [Troubleshooting]

문제:

- Reflection을 반복할수록 답변이 요구사항에서 벗어남

원인:

- 자기평가만 사용
- 요구사항 State 누락
- 외부 검증 없음
- 불필요한 개선 반복
- 출력 형식 검증 없음

해결:

- 원래 요구사항을 State에 고정
- Quality Gate 적용
- 출력 형식 검증
- Review Agent 검토
- Reflection 횟수 제한

---

## 27.5 Cost Explosion

### [Troubleshooting]

문제:

- Loop 실행 중 토큰 사용량과 비용이 급증함

원인:

- 반복 횟수 제한 없음
- 전체 문서 반복 주입
- 긴 로그 전체 재사용
- RAG 재검색 반복
- Multi-Agent 호출 과다
- Reflection 반복

해결:

- maxIterations 설정
- Token Budget 설정
- Context 요약 사용
- 필요한 Chunk만 검색
- Reflection 횟수 제한
- Multi-Agent 호출 조건 제한

---

## 27.6 State Lost

### [Troubleshooting]

문제:

- Agent가 이전 반복 결과를 잃고 같은 작업을 다시 함

원인:

- Loop State 없음
- toolResult 저장 누락
- taskId 없음
- Agent 간 전달 누락
- 실패 후 State 초기화

해결:

- loopId와 taskId 사용
- iterationCount 저장
- toolResult 저장
- changedFiles 저장
- error history 저장
- PM Agent가 State 통합 관리

---

# 28. Checklist Rules

## 28.1 Loop Engineering Checklist

### [Checklist]

- [ ] Loop Engineering 목적을 설명했는가?
- [ ] Agent Loop 개념을 설명했는가?
- [ ] Planning Loop를 포함했는가?
- [ ] Execution Loop를 포함했는가?
- [ ] Verification Loop를 포함했는가?
- [ ] Repair Loop를 포함했는가?
- [ ] Retry Loop를 포함했는가?
- [ ] Reflection Loop를 포함했는가?
- [ ] RAG Retrieval Loop를 포함했는가?
- [ ] Test-Fix Loop를 포함했는가?
- [ ] Review Loop를 포함했는가?
- [ ] Multi-Agent Loop를 포함했는가?
- [ ] Human-in-the-Loop 기준을 포함했는가?
- [ ] Stop Condition을 포함했는가?
- [ ] Infinite Loop Prevention을 포함했는가?
- [ ] Loop State를 포함했는가?
- [ ] Quality Gate를 포함했는가?
- [ ] Cost / Token Control을 포함했는가?
- [ ] Escalation Policy를 포함했는가?
- [ ] Loop Pattern을 포함했는가?
- [ ] Harness Engineering과의 차이를 설명했는가?
- [ ] Agent Workflow와의 차이를 설명했는가?
- [ ] Multi-Agent Orchestration과의 관계를 설명했는가?
- [ ] Retrieval Queries를 포함했는가?

---

### [FAQ]

Q. Loop Engineering 문서 검수에서 가장 중요한 항목은?

A. Stop Condition, Loop State, Quality Gate, maxIterations, Escalation Policy이다.

Q. Checklist를 문서에 넣어도 돼?

A. 가능하다. Loop는 누락 항목이 무한 반복이나 품질 실패로 이어질 수 있어 Checklist가 유용하다.

Q. Test-Fix Loop는 필수야?

A. 개발 Agent를 목표로 한다면 강력 권장이다.

Q. Cost Control도 체크해야 해?

A. 해야 한다. 반복 구조는 토큰과 비용을 쉽게 증가시킨다.

---

# 29. Retrieval Optimization Rules

## 29.1 Retrieval Keyword Rules

### [개념]

Loop Engineering 문서는 Agent 반복 실행 구조 검색에 최적화되어야 한다.

---

### [핵심]

강조 키워드:

- Loop Engineering
- Agent Loop
- LLM Agent Loop
- Planning Loop
- Execution Loop
- Verification Loop
- Review Loop
- Repair Loop
- Retry Loop
- Reflection Loop
- RAG Retrieval Loop
- Test-Fix Loop
- Code Review Loop
- Tool Feedback Loop
- Multi-Agent Loop
- Human-in-the-Loop
- Stop Condition
- Exit Criteria
- Infinite Loop Prevention
- Loop State
- Loop Memory
- Quality Gate
- Error Recovery
- Failure Classification
- Escalation Policy
- Cost Control
- Token Budget
- Max Iterations
- Retry Limit
- Same Error Detection
- PM Agent Loop
- Backend Agent Loop
- SQL Agent Loop
- Frontend Agent Loop
- Review Agent Loop
- DevOps Agent Loop

---

### [실무]

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

포함할 질문 패턴:

- Loop Engineering이 뭐야?
- Agent Loop가 뭐야?
- Loop Engineering은 어디에 들어가?
- Loop Engineering과 Harness Engineering 차이는?
- Agent Workflow와 Loop Engineering 차이는?
- Stop Condition은 왜 필요해?
- Agent 무한 루프는 어떻게 막아?
- Test-Fix Loop는 어떻게 설계해?
- RAG 재검색 Loop는 어떻게 설계해?
- Review Loop는 어떻게 설계해?
- Multi-Agent Loop는 어떻게 설계해?
- Reflection Loop는 위험하지 않아?
- Retry Loop와 Repair Loop 차이는?
- Loop State는 왜 필요해?
- Quality Gate는 뭐야?
- Agent 반복 실패하면 어떻게 해?
- 비용 폭증은 어떻게 막아?

---

### [FAQ]

Q. Loop Engineering 문서는 검색 키워드를 반복해도 돼?

A. 가능하다. RAG 문서는 검색 최적화가 우선이므로 핵심 용어 반복이 허용된다.

Q. Retrieval Queries에는 어떤 질문을 넣어야 해?

A. 사용자가 실제로 물어볼 질문과 Agent가 검색할 가능성이 높은 질문을 넣어야 한다.

Q. Loop Engineering 문서는 사람용 학습 문서처럼 길게 써야 해?

A. 아니다. Agent 검색과 반복 실행 규칙 적용에 유리하도록 짧고 구조적으로 작성해야 한다.

Q. 용어는 영어와 한글을 섞어도 돼?

A. 가능하지만 핵심 개념명은 일관되게 유지해야 한다. 예: Loop Engineering, Agent Loop, Stop Condition.

---

# 30. Version Rules

## 30.1 기준 버전

### [개념]

Loop Engineering 문서는 2026년 기준 AI Agent 시스템과 Agentic Workflow 설계를 기준으로 작성한다.

---

### [핵심]

기준:

- 2026 AI Agent System
- LLM Agent
- Agentic Workflow
- Agent Loop
- Tool Feedback Loop
- Plan-Execute-Verify
- Test-Fix Loop
- Review-Fix Loop
- Human-in-the-Loop
- Structured Tool Output
- State Management
- Guardrails
- AI Observability
- Multi-Agent System

---

### [실무]

Legacy 제외:

- 단일 Prompt만으로 모든 작업 처리
- 검증 없는 자동 반복
- Stop Condition 없는 Agent
- maxIterations 없는 Loop
- 자연어 결과만 보고 다음 단계 결정
- 테스트 없는 코드 수정 반복
- 로그 없는 반복 실행
- Agent 자기평가만으로 완료 처리
- 모든 실패 무제한 retry
- 위험 작업 자동 반복
- 비용 제어 없는 Agent Loop

---

### [FAQ]

Q. Loop Engineering은 2026년 기준으로 중요한 개념이야?

A. 중요하다. Agent가 실제 작업을 수행할수록 반복 실행, 검증, 수정, 종료 조건 설계가 필요하다.

Q. Legacy Agent 방식은 뭐가 문제야?

A. 한 번 답변하고 끝나거나 검증 없는 반복을 수행해 품질과 안전성을 보장하기 어렵다.

Q. LangGraph를 쓰면 Loop Engineering이 자동 해결돼?

A. 아니다. LangGraph는 Loop를 구현할 수 있는 도구이고 Stop Condition, Quality Gate, Escalation은 별도로 설계해야 한다.

Q. Loop Engineering은 Agentic RAG와 연결돼?

A. 연결된다. Agentic RAG에서 검색, 재검색, 검증, 답변 수정을 반복할 수 있기 때문이다.

---

# 31. File Relationship Rules

## 31.1 연계 문서

### [개념]

Loop Engineering은 Level 4 AI Expert 문서이며, Level 2 Agent Workflow Design과 Level 4 Harness / Orchestration / Observability 문서를 연결한다.

---

### [핵심]

선행 문서:

- Prompt Engineering
- Context Engineering
- Tool Calling & Function Calling
- Agent Workflow Design
- Agent Memory & State Management
- Agent Evaluation & Guardrails
- LangChain & LangGraph
- Harness Engineering

연계 문서:

- Agentic RAG
- Graph RAG
- Advanced Multi-Agent Orchestration
- Long-Term Memory
- Tool Calling & Function Calling Reliability
- AI Guardrails & Security
- AI Observability
- MLOps
- RAG Evaluation & Retrieval Optimization

---

### [실무]

문서 간 역할:

- `Agent Workflow Design`은 기본 작업 흐름을 다룬다.
- `Harness Engineering`은 Loop 실행 기반과 도구 권한을 다룬다.
- `Loop Engineering`은 반복 실행, 검증, 수정, 종료 조건을 다룬다.
- `Advanced Multi-Agent Orchestration`은 여러 Agent 간 Loop를 연결한다.
- `AI Observability`는 Loop 로그와 실패 패턴을 분석한다.
- `Long-Term Memory`는 반복 실패와 결정 이력을 장기 저장한다.
- `RAG Evaluation & Retrieval Optimization`은 Retrieval Loop 품질 평가를 다룬다.

---

### [FAQ]

Q. Loop Engineering 전에 어떤 문서를 보면 좋아?

A. Agent Workflow Design, Tool Calling & Function Calling, Agent Memory & State Management, Harness Engineering을 먼저 보면 좋다.

Q. Loop Engineering 다음에는 어떤 문서가 자연스러워?

A. Advanced Multi-Agent Orchestration, AI Observability, Long-Term Memory가 자연스럽다.

Q. Loop Engineering과 Harness Engineering은 같이 봐야 해?

A. 그렇다. Harness가 실행 기반을 제공하고 Loop가 반복 제어를 담당한다.

Q. Loop Engineering과 AI Observability는 어떻게 연결돼?

A. Loop 실행 로그, 반복 횟수, 실패 원인, 품질 Gate 결과를 Observability에서 분석한다.

---

# 32. Final Goal

## 32.1 Loop Engineering RAG 문서 최종 목표

### [개념]

Loop Engineering RAG 문서는 Agent가 단발성 답변을 넘어 목표 달성까지 반복적으로 실행, 검증, 수정, 재실행할 수 있도록 만드는 기준 문서이다.

---

### [핵심]

최종적으로 Agent는 Loop Engineering 문서를 통해 아래를 수행할 수 있어야 한다.

- Agent Loop 개념 이해
- Planning Loop 설계
- Execution Loop 설계
- Verification Loop 설계
- Repair Loop 설계
- Retry Loop 설계
- Reflection Loop 설계
- RAG Retrieval Loop 설계
- Test-Fix Loop 설계
- Review Loop 설계
- Multi-Agent Loop 설계
- Human-in-the-Loop 전환 판단
- Stop Condition 정의
- Infinite Loop 방지
- Loop State 관리
- Quality Gate 적용
- Cost / Token Control 적용
- Escalation Policy 적용
- 반복 실패 원인 분류
- Harness Engineering과 연계
- AI Observability와 연계
- Long-Term Memory와 연계

---

### [실무]

개인 AI 개발팀에서 Loop Engineering의 최종 목표는 단순 반복이 아니다.

목표:

```text
Agent가 목표를 받는다
→ 계획을 만든다
→ 실행한다
→ 도구 결과를 관찰한다
→ 검증한다
→ 실패하면 원인을 분석한다
→ 최소 수정한다
→ 다시 검증한다
→ 완료 조건을 만족하면 종료한다
→ 반복 실패하면 escalation한다
```

---

### [FAQ]

Q. Loop Engineering 문서의 최종 목표는 뭐야?

A. Agent가 목표 달성까지 계획, 실행, 검증, 수정, 재실행을 안전하게 반복하도록 기준을 제공하는 것이다.

Q. Loop Engineering은 개인 AI 개발팀에서 꼭 필요해?

A. 필요하다. 개발, 테스트, 리뷰, RAG 검색, 배포는 한 번에 끝나지 않고 반복 검증이 필요하기 때문이다.

Q. Loop Engineering 문서는 Agent 성능에 영향을 줘?

A. 영향을 준다. Loop 품질이 낮으면 Agent가 무한 반복하거나 검증 없이 잘못된 결과를 완료로 처리한다.

Q. Loop Engineering의 핵심 한 줄 요약은?

A. Loop Engineering은 LLM Agent가 목표 달성까지 실행, 검증, 수정, 종료를 반복하도록 설계하는 영역이다.

---

# Retrieval Queries

### [FAQ]

Q. Loop Engineering이 뭐야?

A. AI Agent가 목표 달성까지 계획, 실행, 검증, 수정, 재실행을 반복하도록 설계하는 영역이다.

Q. Agent Loop가 뭐야?

A. Agent가 목표를 달성하기 위해 계획, 실행, 관찰, 평가, 수정, 종료 판단을 반복하는 구조이다.

Q. Loop Engineering은 Prompt Engineering과 뭐가 달라?

A. Prompt Engineering은 지시문 설계이고 Loop Engineering은 Agent가 반복적으로 실행하고 검증하는 흐름 설계이다.

Q. Loop Engineering은 Context Engineering과 뭐가 달라?

A. Context Engineering은 문맥 구성이고 Loop Engineering은 문맥과 도구 결과를 활용해 반복 실행을 제어한다.

Q. Loop Engineering은 Harness Engineering과 뭐가 달라?

A. Harness Engineering은 실행 기반이고 Loop Engineering은 실행, 검증, 수정, 재실행을 반복하는 제어 구조이다.

Q. Loop Engineering은 Tool Calling과 뭐가 달라?

A. Tool Calling은 도구 호출 방식이고 Loop Engineering은 도구 결과를 반영해 다음 행동을 반복 결정하는 구조이다.

Q. Loop Engineering은 Agent Workflow와 뭐가 달라?

A. Agent Workflow는 작업 흐름이고 Loop Engineering은 반복, 검증, 수정, 종료 조건까지 포함하는 심화 흐름이다.

Q. Loop Engineering은 Retry와 뭐가 달라?

A. Retry는 같은 작업을 다시 시도하는 것이고 Loop Engineering은 계획, 실행, 검증, 수정, 종료 조건을 포함한다.

Q. Loop Engineering은 Level 2야 Level 4야?

A. Level 4가 적절하다. 기본 Agent Workflow를 넘어 반복 실행, 실패 복구, 품질 Gate, 비용 제어를 다루기 때문이다.

Q. Loop Engineering 문서에는 무엇을 포함해야 해?

A. Planning Loop, Execution Loop, Verification Loop, Repair Loop, Retry Loop, Reflection Loop, Stop Condition, Quality Gate를 포함해야 한다.

Q. Planning Loop는 뭐야?

A. Agent가 목표를 분석하고 작업을 분해하고 위험과 누락 정보를 확인한 뒤 계획을 수정하는 반복 구조이다.

Q. Execution Loop는 뭐야?

A. Agent가 계획된 단계를 실행하고 도구 결과를 관찰하고 다음 단계를 결정하는 반복 구조이다.

Q. Verification Loop는 뭐야?

A. Agent 결과가 요구사항, 테스트, 규칙, 보안 기준을 만족하는지 확인하는 반복 구조이다.

Q. Repair Loop는 뭐야?

A. 실패 원인을 분석하고 최소 수정한 뒤 다시 테스트하거나 검증하는 반복 구조이다.

Q. Retry Loop는 뭐야?

A. 일시적 실패를 제한된 횟수와 조건 안에서 다시 시도하는 반복 구조이다.

Q. Reflection Loop는 뭐야?

A. Agent가 자신의 계획, 답변, 실행 결과를 점검하고 부족한 부분을 수정하는 반복 구조이다.

Q. RAG Retrieval Loop는 뭐야?

A. 검색 결과가 부족할 때 검색어를 수정하고 재검색하고 근거를 검증하는 반복 구조이다.

Q. Test-Fix Loop는 뭐야?

A. 코드 수정 후 테스트를 실행하고 실패하면 원인을 분석해 수정한 뒤 재테스트하는 구조이다.

Q. Review Loop는 뭐야?

A. Agent 결과를 검토하고 문제가 있으면 수정 요청 후 다시 검토하는 반복 구조이다.

Q. Multi-Agent Loop는 뭐야?

A. PM Agent, Specialist Agent, Review Agent가 역할별 작업과 검증을 반복하는 협업 구조이다.

Q. Human-in-the-Loop은 언제 필요해?

A. 위험 작업, 모호한 요구사항, 반복 실패, DB 변경, 배포, Secret 접근, 비용 발생 작업에서 필요하다.

Q. Stop Condition은 왜 필요해?

A. 무한 반복, 비용 폭증, 잘못된 수정 반복을 막기 위해 필요하다.

Q. Stop Condition에는 무엇이 들어가?

A. 목표 달성, 테스트 통과, Review 통과, 최대 반복 횟수, 실패 조건, 비용 한도, 승인 거절이 들어간다.

Q. Exit Criteria는 뭐야?

A. Loop가 성공적으로 종료되기 위해 반드시 만족해야 하는 조건이다.

Q. Infinite Loop는 어떻게 막아?

A. maxIterations, retryLimit, sameErrorLimit, Stop Condition, State 저장, escalation을 적용한다.

Q. maxIterations는 왜 필요해?

A. Agent가 같은 작업을 끝없이 반복하지 않게 제한하기 위해 필요하다.

Q. Retry Limit은 왜 필요해?

A. 해결 불가능한 오류를 계속 재시도하지 않도록 막기 위해 필요하다.

Q. Loop State는 왜 필요해?

A. 현재 단계, 반복 횟수, 실패 이력, 도구 결과, 변경 파일, 검증 결과를 추적하기 위해 필요하다.

Q. Loop State에는 무엇을 저장해?

A. loopId, taskId, goal, currentStep, iterationCount, toolResults, errors, changedFiles, stopReason을 저장한다.

Q. Quality Gate는 뭐야?

A. Loop가 다음 단계로 넘어가거나 종료되기 전에 통과해야 하는 품질 기준이다.

Q. RAG 문서 제작 Quality Gate는 뭐야?

A. 출력 형식 준수, 필수 섹션 포함, Retrieval Queries 포함, 용어 통일, 코드블록 id 제거, FAQ 강화이다.

Q. 개발 Agent Quality Gate는 뭐야?

A. 빌드 성공, 테스트 성공, lint 통과, 변경 범위 적절, 보안 위험 없음, Review 승인이다.

Q. Test-Fix Loop는 몇 번 반복해야 해?

A. 보통 2~3회 제한하고 같은 실패가 반복되면 escalation한다.

Q. RAG 재검색은 몇 번 반복해야 해?

A. 보통 1~3회 재검색 후에도 근거가 부족하면 근거 부족으로 보고한다.

Q. Reflection Loop는 많이 돌릴수록 좋아?

A. 아니다. 비용이 증가하고 자기합리화 위험이 있으므로 제한적으로 사용해야 한다.

Q. Agent 자기평가만 믿어도 돼?

A. 안 된다. 테스트, 리뷰, RAG 근거, 도구 결과 같은 외부 검증이 필요하다.

Q. Loop 중 같은 오류가 반복되면 어떻게 해?

A. repeatedErrors를 기록하고 반복 횟수 제한 후 Review Agent나 사람에게 escalation한다.

Q. Loop 중 비용이 너무 커지면 어떻게 해?

A. 반복 횟수, 재검색 횟수, Reflection 횟수, Context 크기, Tool 호출 수를 제한한다.

Q. Cost Control은 왜 필요해?

A. Loop는 LLM 호출, 검색, 도구 실행을 반복하므로 비용과 시간이 빠르게 증가할 수 있기 때문이다.

Q. Token Budget은 어떻게 관리해?

A. 필요한 Chunk만 사용하고, 이전 결과는 요약 State로 저장하며, 전체 로그 재주입을 피한다.

Q. Escalation은 실패야?

A. 아니다. 자동 처리가 위험하거나 불확실할 때 상위 판단으로 넘기는 정상적인 안전 흐름이다.

Q. Escalation Summary에는 무엇을 넣어야 해?

A. 목표, 현재 상태, 시도한 작업, 실패 원인, 반복 횟수, 관련 로그, 변경 파일, 가능한 대안을 포함한다.

Q. Backend Agent Loop는 어떻게 설계해?

A. 요구사항 분석, 코드 수정, 테스트 실행, 실패 분석, 최소 수정, 재테스트, Review 전달 구조로 설계한다.

Q. Frontend Agent Loop는 어떻게 설계해?

A. 컴포넌트 수정, 빌드, 타입 오류 확인, UI 흐름 검증, 수정, 재빌드 구조로 설계한다.

Q. SQL Agent Loop는 어떻게 설계해?

A. 스키마 확인, 쿼리 생성, 안전성 검증, 실행 계획 확인, 결과 검증, 쿼리 수정 구조로 설계한다.

Q. Review Agent Loop는 어떻게 설계해?

A. 결과 검토, 문제 분류, 수정 요청, 재검토, 승인 또는 escalation 구조로 설계한다.

Q. PM Agent Loop는 어떻게 설계해?

A. 작업 분해, Agent 할당, 결과 취합, 누락 확인, 재지시, 최종 통합 구조로 설계한다.

Q. Loop Engineering과 AI Observability는 어떻게 연결돼?

A. Loop 실행 로그, 반복 횟수, 실패 원인, 품질 Gate 결과를 Observability에서 분석한다.

Q. Loop Engineering과 Long-Term Memory는 어떻게 연결돼?

A. 반복 실패 패턴, 결정 이력, 성공한 해결 패턴을 Long-Term Memory에 저장해 다음 작업에 활용할 수 있다.

Q. Loop Engineering과 Advanced Multi-Agent Orchestration은 어떻게 연결돼?

A. Loop Engineering은 Agent별 반복 구조를 설계하고 Orchestration은 여러 Agent의 Loop를 연결하고 조율한다.

Q. Loop Engineering을 처음 도입할 때 무엇부터 만들면 돼?

A. Goal Definition, Loop State, Stop Condition, maxIterations, Quality Gate부터 만드는 것이 좋다.

Q. 개인 AI 서버에서도 Loop Engineering이 필요해?

A. 필요하다. 개인 AI 개발팀이 코드 작성, 테스트, 리뷰, RAG 검색을 반복 수행하려면 Loop 설계가 필요하다.

Q. Loop Engineering의 핵심 한 줄 요약은?

A. Loop Engineering은 LLM Agent가 목표 달성까지 실행, 검증, 수정, 종료를 반복하도록 설계하는 영역이다.
