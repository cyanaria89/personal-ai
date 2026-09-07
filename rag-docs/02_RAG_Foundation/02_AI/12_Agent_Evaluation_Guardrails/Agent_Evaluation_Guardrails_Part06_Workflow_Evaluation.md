# Agent Evaluation & Guardrails Part06 - Workflow Evaluation

---

# 1. Workflow Evaluation

## 1.1 Workflow Evaluation Core

### [개념]

Workflow Evaluation은 Multi-Agent System에서 Agent 실행 흐름 전체가 사용자 요구사항을 올바르게 처리했는지 평가하는 기준이다.

Workflow Evaluation은 최종 Output만 평가하지 않는다.

평가 대상:

- Routing Accuracy
- Handoff Quality
- State Consistency
- Context Preservation
- Agent Role Compliance
- Intermediate Output Quality
- Review Effectiveness
- Fix Effectiveness
- Stop Condition
- Failure Handling
- Final Output Quality

Workflow Evaluation은 Agent 수가 많아질수록 중요해진다.

Agent가 많아도 Routing, Handoff, Review, Fix가 부정확하면 최종 Output 품질은 낮아진다.

---

### [핵심]

Workflow Evaluation 기본 Flow:

```text
Workflow Run
→ Check User Requirement
→ Check Routing
→ Check Agent Outputs
→ Check Handoff
→ Check Review
→ Check Fix
→ Check Stop Condition
→ Check Final Output
→ Pass / Fix / Stop
```

핵심 평가 항목:

| 항목                     | 검증 내용                                     |
| ------------------------ | --------------------------------------------- |
| Routing Accuracy         | 적절한 Agent에게 작업이 배정되었는가          |
| Handoff Quality          | 다음 Agent에게 필요한 Context가 전달되었는가  |
| State Consistency        | Agent 간 상태가 일관되는가                    |
| Requirement Preservation | 사용자 요구사항이 흐름 전체에서 유지되었는가  |
| Role Compliance          | 각 Agent가 자신의 역할 범위 안에서 작업했는가 |
| Review Effectiveness     | Review Agent가 실제 결함을 찾았는가           |
| Fix Effectiveness        | Fix가 Review Finding을 해결했는가             |
| Stop Condition           | 중단 조건이 올바르게 적용되었는가             |
| Final Output Quality     | 최종 결과가 요구사항을 충족하는가             |

Workflow Evaluation 결과:

```text
Pass:
- Routing 적절
- Handoff 충분
- State 일관
- Review / Fix 유효
- Final Output 요구사항 충족

Fix:
- 일부 Handoff 누락
- Review Finding 반영 부족
- 상태 불일치 일부 존재
- 최종 Output 보완 필요

Stop:
- 잘못된 Agent Routing
- 핵심 Context 손실
- 위험 작업 승인 누락
- Tool 실패 후 진행 불가
- Low Confidence 상태
```

---

### [실무]

2026 실무 기준 Workflow Evaluation은 개인 AI 개발팀 구조의 핵심 품질 관리 단계다.

개인 AI 개발팀 예시:

```text
User Request
→ PM Agent
→ Backend Agent
→ Frontend Agent
→ Review Agent
→ Fix Agent
→ Final Output
```

확장 Workflow 예시:

```text
User Request
→ PM Agent
→ Backend Agent
→ Frontend Agent
→ DevOps Agent
→ AI/ML Agent
→ Review Agent
→ Safety Agent
→ Fix Agent
→ Final Output
```

실무 평가 순서:

```text
1. User Requirement가 PM Agent에서 정확히 분해되었는지 확인
2. PM Agent가 적절한 Specialist Agent를 선택했는지 확인
3. Specialist Agent에게 필요한 Context가 전달되었는지 확인
4. 각 Agent Output이 Domain Rules와 일치하는지 확인
5. Review Agent가 실제 결함을 찾았는지 확인
6. Fix Agent가 Review Finding을 반영했는지 확인
7. Stop Condition과 Human Confirmation이 적용되었는지 확인
8. Final Output이 원래 사용자 요청과 일치하는지 확인
```

Workflow Evaluation Report 예시:

```md
### Workflow Evaluation Report

| Step           | Result | Issue                               | Fix                       |
| -------------- | ------ | ----------------------------------- | ------------------------- |
| PM Routing     | Pass   | Backend 작업을 Backend Agent로 전달 | 없음                      |
| Handoff        | Fix    | API 응답 규칙 누락                  | ApiResponse<T> 규칙 추가  |
| Backend Output | Fix    | Repository 메서드 근거 부족         | 실제 Repository 기준 수정 |
| Review         | Pass   | Unsupported Claim 탐지              | 없음                      |
| Fix            | Pass   | Review Finding 반영                 | 없음                      |
| Final Output   | Pass   | 요구사항 충족                       | 없음                      |
```

---

### [주의]

Workflow Evaluation 주의사항:

- Agent 수가 많다고 Workflow 품질이 좋은 것은 아니다.
- 최종 Output만 보면 중간 오류를 놓칠 수 있다.
- Handoff에서 요구사항이 누락되면 다음 Agent가 잘못된 결과를 만든다.
- Review Agent가 형식적으로만 동작하면 결함이 남는다.
- Fix Agent가 Review Finding을 반영하지 않으면 Review가 무의미하다.
- State 불일치는 최종 Output 오류로 이어질 수 있다.
- Tool Failure를 무시하고 Workflow를 계속 진행하면 안 된다.

---

### [Best Practice]

Workflow Evaluation Best Practice:

- User Requirement를 Workflow 전체의 기준으로 유지한다.
- Routing 결과를 기록한다.
- Handoff에는 목적, Context, 제약, Output Format을 포함한다.
- Agent별 Output을 개별 평가한다.
- Review Finding과 Fix Result를 매핑한다.
- Stop Condition을 명시한다.
- Human Confirmation 필요 작업은 Workflow를 중단한다.
- 반복 실패는 Failure Classification 후 Fallback으로 전환한다.
- Final Output은 원래 사용자 요청과 다시 대조한다.

---

### [FAQ]

Q. Workflow Evaluation이 뭐야?
A. Multi-Agent System에서 Agent 실행 흐름 전체가 사용자 요구사항을 올바르게 처리했는지 평가하는 기준이다.

Q. Workflow Evaluation은 최종 답변만 보면 돼?
A. 아니다. Routing, Handoff, Intermediate Output, Review, Fix, Stop Condition도 평가해야 한다.

Q. Agent 수가 많으면 Workflow 품질도 좋아져?
A. 아니다. Agent가 많아도 Routing과 Handoff가 부정확하면 품질이 낮아진다.

Q. Workflow Evaluation에서 가장 중요한 것은 뭐야?
A. 사용자 요구사항이 흐름 전체에서 유지되고, 적절한 Agent가 적절한 Context로 작업했는지 확인하는 것이다.

Q. Tool Failure가 있어도 Workflow를 계속해도 돼?
A. 실패가 해결되었거나 Fallback이 있을 때만 가능하다. 실패를 무시하고 진행하면 안 된다.

---

# 2. Routing Evaluation

## 2.1 Routing Accuracy

### [개념]

Routing Accuracy는 PM Agent 또는 Orchestrator가 사용자 요청을 적절한 Agent에게 배정했는지 평가하는 기준이다.

Routing이 잘못되면 전문 Agent가 아닌 Agent가 작업을 수행하게 되고, Output 품질이 낮아진다.

Routing Evaluation은 Agent Workflow의 첫 번째 품질 게이트다.

---

### [핵심]

Routing Evaluation 기준:

| 기준                 | 검증 내용                                              |
| -------------------- | ------------------------------------------------------ |
| Task Classification  | 요청 유형을 정확히 분류했는가                          |
| Agent Selection      | 적절한 Agent를 선택했는가                              |
| Domain Match         | 작업 Domain과 Agent 전문성이 맞는가                    |
| Complexity Match     | 작업 복잡도에 맞는 Agent를 선택했는가                  |
| Risk Match           | 위험 작업에 Safety / Review Agent를 포함했는가         |
| Dependency Awareness | 선행 Agent가 필요한 작업인지 확인했는가                |
| Multi-Agent Need     | 단일 Agent로 충분한지 다중 Agent가 필요한지 판단했는가 |

Routing Flow:

```text
User Request
→ Task Classification
→ Domain Identification
→ Risk Classification
→ Agent Selection
→ Handoff Preparation
```

Routing 결과:

```text
Correct:
- 작업 Domain과 Agent 역할 일치

Suboptimal:
- 가능하지만 더 적절한 Agent가 있음

Incorrect:
- Domain 불일치
- 필요한 Agent 누락

Unsafe:
- 위험 작업인데 Safety / Human Confirmation 누락
```

---

### [실무]

실무에서는 요청 유형별로 Agent를 분기한다.

Agent Routing 예시:

| User Request        | Primary Agent  | Support Agent        |
| ------------------- | -------------- | -------------------- |
| 요구사항 정리       | PM Agent       | Review Agent         |
| API 설계            | Backend Agent  | Review Agent         |
| React 화면 구현     | Frontend Agent | Review Agent         |
| 배포 스크립트 작성  | DevOps Agent   | Safety Agent         |
| RAG 답변 평가       | Review Agent   | RAG Evaluation Agent |
| Tool 실행 포함 작업 | Tool Agent     | Safety Agent         |
| 위험 작업           | Safety Agent   | Human Confirmation   |

Routing 예시:

```text
User Request:
Spring Boot Service 코드 검토해줘.

Correct Routing:
- Backend Agent
- Review Agent

Incorrect Routing:
- Frontend Agent 단독
```

위험 작업 Routing 예시:

```text
User Request:
운영 DB에서 테스트 데이터 삭제해줘.

Required Routing:
- PM Agent
- Safety Agent
- DB / DevOps Agent
- Human Confirmation

Evaluation:
- High Risk 작업
- 승인 전 실행 금지
```

Routing Report 예시:

```md
| Task             | Routed Agent  | Result | Issue                   | Fix                |
| ---------------- | ------------- | ------ | ----------------------- | ------------------ |
| Backend API 검토 | Backend Agent | Pass   | 없음                    | 없음               |
| 배포 실행        | DevOps Agent  | Fix    | Safety Agent 누락       | Safety Review 추가 |
| 이메일 발송      | Tool Agent    | Stop   | Human Confirmation 없음 | 승인 필요          |
```

---

### [주의]

Routing Evaluation 주의사항:

- PM Agent가 모든 작업을 직접 처리하면 전문성이 떨어질 수 있다.
- 단순 작업에 과도한 Multi-Agent Routing을 하면 비효율적이다.
- 위험 작업은 Specialist Agent만으로 충분하지 않다.
- Safety Agent 또는 Human Confirmation이 필요한 작업을 놓치면 Safety Failure다.
- Routing 단계에서 사용자 요구사항을 잘못 분류하면 전체 Workflow가 흔들린다.
- 최신 프로젝트 상태를 확인하지 않고 Routing하면 오래된 Agent 구성이 사용될 수 있다.

---

### [Best Practice]

Routing Evaluation Best Practice:

- User Request를 Domain, Risk, Output Type으로 분류한다.
- 단일 Agent와 Multi-Agent 필요성을 구분한다.
- 위험 작업은 Safety Agent 또는 Human Confirmation을 포함한다.
- Agent 역할 경계를 명확히 한다.
- PM Agent는 Routing 근거를 Handoff에 포함한다.
- 반복적으로 잘못 Routing되는 요청은 Routing Rule을 보강한다.
- Routing 결과를 Workflow Evaluation Report에 기록한다.

---

### [FAQ]

Q. Routing Accuracy가 뭐야?
A. 사용자 요청을 적절한 Agent에게 배정했는지 평가하는 기준이다.

Q. Routing이 틀리면 어떤 문제가 생겨?
A. 전문성이 맞지 않는 Agent가 작업해 Output 품질이 낮아지고 요구사항 누락이 발생할 수 있다.

Q. PM Agent가 모든 작업을 직접 처리하면 안 돼?
A. 간단한 작업은 가능하지만 전문 코드, 배포, 안전 작업은 Specialist Agent 또는 Safety Agent가 필요하다.

Q. 위험 작업 Routing에는 무엇이 필요해?
A. Safety Agent와 Human Confirmation이 필요할 수 있다.

Q. Routing은 어떤 기준으로 해?
A. Domain, Risk Level, Output Type, 작업 복잡도, Tool 필요성을 기준으로 한다.

---

# 3. Handoff Evaluation

## 3.1 Handoff Quality

### [개념]

Handoff Quality는 한 Agent가 다음 Agent에게 작업을 전달할 때 필요한 Context, 요구사항, 제약, 근거, 출력 형식을 충분히 전달했는지 평가하는 기준이다.

Handoff가 부실하면 다음 Agent는 잘못된 가정으로 작업하게 된다.

Handoff Evaluation은 Multi-Agent Workflow에서 Context 손실을 방지한다.

---

### [핵심]

Handoff 필수 요소:

| 요소                | 의미                         |
| ------------------- | ---------------------------- |
| Task Goal           | 다음 Agent가 수행할 목표     |
| User Requirement    | 원래 사용자 요구사항         |
| Constraints         | 기술, 형식, 범위 제약        |
| Context             | 필요한 코드, 문서, 검색 결과 |
| Evidence            | 근거 자료                    |
| Assumption          | 명시된 가정                  |
| Missing Information | 부족한 정보                  |
| Risk Level          | 작업 위험도                  |
| Output Format       | 요구 출력 형식               |
| Stop Condition      | 중단 기준                    |

Handoff Evaluation Flow:

```text
Previous Agent Output
→ Extract Handoff Context
→ Check Required Fields
→ Check Requirement Preservation
→ Check Missing / Distorted Context
→ Pass / Fix
```

Handoff 결과:

```text
Good Handoff:
- 목표 명확
- 요구사항 보존
- 필요한 Context 포함
- 제약과 형식 포함
- Missing Information 표시

Bad Handoff:
- 목표 모호
- 사용자 요구사항 누락
- Context 손실
- Assumption 숨김
- 출력 형식 누락
```

---

### [실무]

실무에서는 Handoff를 구조화된 형식으로 작성한다.

Handoff Template:

```md
# Agent Handoff

## Target Agent

- Backend Agent

## Task Goal

- Notification Service 코드 검토

## User Requirement

- 프로젝트 규칙 준수
- ApiResponse<T> 직접 반환
- 예외는 GlobalExceptionHandler 처리

## Context

- NotificationRepository 메서드 목록
- Notification Entity 주요 필드
- Controller 응답 규칙

## Constraints

- Java 21
- Spring Boot 3.x
- 존재하지 않는 메서드 생성 금지

## Missing Information

- 실제 Service 코드 일부 없음

## Output Format

- Findings Table
- Severity
- Fix Recommendation

## Stop Condition

- Repository 메서드 검증 불가 시 Assumption 표시
```

Handoff Evaluation Report 예시:

```md
| Handoff Item        | Result | Issue                  | Fix                 |
| ------------------- | ------ | ---------------------- | ------------------- |
| Task Goal           | Pass   | 명확함                 | 없음                |
| User Requirement    | Fix    | 출력 형식 누락         | Format 추가         |
| Context             | Fix    | Repository 메서드 없음 | 메서드 목록 포함    |
| Risk Level          | Pass   | Low                    | 없음                |
| Missing Information | Fail   | 누락됨                 | 검증 불가 항목 표시 |
```

---

### [주의]

Handoff Evaluation 주의사항:

- 요약 과정에서 요구사항을 삭제하지 않는다.
- Assumption을 사실처럼 전달하지 않는다.
- Missing Information을 숨기지 않는다.
- 이전 Agent의 오류를 다음 Agent에게 그대로 전달하면 오류가 증폭된다.
- 출력 형식이 빠지면 다음 Agent Output이 형식 위반될 수 있다.
- 위험도 정보가 빠지면 Tool 실행 안전성이 낮아진다.
- Context가 너무 많아도 핵심 정보가 묻힐 수 있다.

---

### [Best Practice]

Handoff Evaluation Best Practice:

- Handoff는 구조화된 Template을 사용한다.
- 원래 사용자 요구사항을 그대로 보존한다.
- Constraints와 Must Not을 명시한다.
- Evidence와 Assumption을 분리한다.
- Missing Information을 포함한다.
- 다음 Agent의 역할에 필요한 Context만 제공한다.
- Output Format과 Acceptance Criteria를 명시한다.
- 위험 작업은 Stop Condition과 Human Confirmation 요구를 포함한다.

---

### [FAQ]

Q. Handoff Quality가 뭐야?
A. Agent 간 작업 전달 시 필요한 Context, 요구사항, 제약, 근거, 출력 형식이 충분히 전달되었는지 평가하는 기준이다.

Q. Handoff가 부실하면 어떤 문제가 생겨?
A. 다음 Agent가 잘못된 가정으로 작업하고 요구사항 누락이나 Hallucination이 발생할 수 있다.

Q. 좋은 Handoff에는 뭐가 들어가야 해?
A. Task Goal, User Requirement, Constraints, Context, Evidence, Assumption, Missing Information, Output Format이 필요하다.

Q. Assumption도 Handoff에 포함해야 해?
A. 포함해야 한다. 단, 사실과 구분해서 명시해야 한다.

Q. Missing Information은 숨겨도 돼?
A. 안 된다. 검증 불가 영역을 숨기면 다음 Agent가 근거 없는 결론을 만들 수 있다.

---

# 4. State Consistency Evaluation

## 4.1 State Consistency

### [개념]

State Consistency는 Workflow 진행 중 Agent 간에 공유되는 상태, 요구사항, 작업 결과, 파일 상태, Tool 결과, Memory가 서로 일관되는지 평가하는 기준이다.

State가 불일치하면 Agent는 오래된 정보나 잘못된 Context를 기준으로 작업하게 된다.

State Consistency는 Multi-Agent System의 안정성을 결정한다.

---

### [핵심]

State Consistency 검증 대상:

| 상태                   | 검증 내용                              |
| ---------------------- | -------------------------------------- |
| User Requirement State | 요구사항이 변경되지 않았는가           |
| Project State          | 현재 프로젝트 상태가 정확한가          |
| File State             | 파일 생성 / 수정 상태가 일관되는가     |
| Tool Result State      | Tool 실행 결과가 반영되었는가          |
| Memory State           | 오래된 Memory와 충돌하지 않는가        |
| Agent Decision State   | 이전 Agent 결정이 유지되는가           |
| Review / Fix State     | Review Finding과 Fix 결과가 매핑되는가 |
| Progress State         | 완료 / 진행 중 / 대기 상태가 정확한가  |

State Consistency Flow:

```text
Workflow State
→ Compare Agent Outputs
→ Check Tool Result
→ Check Memory Conflict
→ Check Progress Status
→ Consistent / Conflict / Unknown
```

State 결과:

```text
Consistent:
- Agent 간 상태가 일치
- 최신 Tool Result 반영
- 요구사항 유지

Conflict:
- Agent 간 상태 충돌
- 오래된 Memory 사용
- 완료 / 대기 상태 혼동

Unknown:
- 상태 확인 근거 부족
- Tool Result 없음
```

---

### [실무]

실무에서는 상태를 명시적으로 관리해야 한다.

프로젝트 진행 상태 예시:

```text
Project Progress:
- Level 1 Backend Foundation 완료
- Level 2 AI 문서 대부분 완료
- Agent Evaluation & Guardrails Planned
- Frontend Foundation Planned
```

잘못된 State 사용 예시:

```text
Agent Output:
Frontend Foundation은 완료됨.

Evaluation:
- Project Progress와 충돌
- State Consistency Failure
- Fix: Frontend Foundation은 Planned 상태로 수정
```

Review / Fix State 예시:

```md
| Review Finding         | Fix Result | State      |
| ---------------------- | ---------- | ---------- |
| FAQ 누락               | FAQ 추가   | Consistent |
| Retrieval Queries 누락 | 수정 안 됨 | Conflict   |
| Unsupported Claim 있음 | 제거됨     | Consistent |
```

Tool Result State 예시:

```text
Tool Result:
Build failed

Wrong State:
- Build passed로 처리

Correct State:
- Build Failure 상태 유지
- 오류 원인 분석 또는 Stop
```

---

### [주의]

State Consistency 주의사항:

- Memory는 최신 상태가 아닐 수 있다.
- 현재 사용자 요청은 오래된 Memory보다 우선한다.
- Tool Result가 실패했는데 상태를 Success로 바꾸면 안 된다.
- Planned와 Completed를 혼동하면 Progress State 오류다.
- Review Finding이 Fix되지 않았는데 해결된 것으로 표시하면 안 된다.
- Agent별로 다른 Context를 보면 상태 충돌이 발생할 수 있다.
- 상태 확인 근거가 없으면 Unknown으로 표시한다.

---

### [Best Practice]

State Consistency Best Practice:

- Workflow State를 명시적으로 기록한다.
- 최신 사용자 요청을 우선한다.
- Tool Result를 상태 변경의 Evidence로 사용한다.
- Completed / In Progress / Planned를 구분한다.
- Review Finding과 Fix Result를 매핑한다.
- Memory 사용 전 Recency와 Conflict를 확인한다.
- 상태 충돌이 있으면 Source Priority를 적용한다.
- 상태가 불확실하면 Unknown 또는 Missing Information으로 표시한다.

---

### [FAQ]

Q. State Consistency가 뭐야?
A. Workflow 진행 중 Agent 간 공유 상태와 Tool 결과, Memory, 진행 상태가 서로 일관되는지 평가하는 기준이다.

Q. State가 불일치하면 어떤 문제가 생겨?
A. Agent가 오래된 정보나 잘못된 Context를 기준으로 작업해 오류가 발생한다.

Q. Memory와 현재 요청이 충돌하면 무엇을 우선해?
A. 현재 사용자 요청을 우선해야 한다.

Q. Tool Result가 실패했는데 성공으로 처리하면 어떤 문제야?
A. State Consistency Failure이며 Tool Failure를 성공으로 포장하는 문제다.

Q. Planned와 Completed를 혼동하면 어떤 문제야?
A. 프로젝트 진행 상태를 왜곡하는 State Consistency Failure다.

---

# 5. Review Effectiveness Evaluation

## 5.1 Review Effectiveness

### [개념]

Review Effectiveness는 Review Agent가 Agent Output의 실제 결함을 정확히 찾아내고, 적절한 Severity와 Fix 방향을 제시했는지 평가하는 기준이다.

Review Agent도 평가 대상이다.

Review가 형식적으로만 수행되면 Workflow 품질은 개선되지 않는다.

---

### [핵심]

Review Effectiveness 검증 항목:

| 항목                  | 의미                                  |
| --------------------- | ------------------------------------- |
| Finding Quality       | 실제 문제를 찾았는가                  |
| False Positive        | 문제가 아닌 것을 문제로 지적했는가    |
| False Negative        | 중요한 문제를 놓쳤는가                |
| Severity Accuracy     | 심각도 판단이 적절한가                |
| Evidence Quality      | 지적에 근거가 있는가                  |
| Fix Direction Quality | 수정 방향이 구체적인가                |
| Requirement Awareness | 사용자 요구사항을 기준으로 검토했는가 |
| Domain Rule Awareness | Domain Rules를 반영했는가             |

Review Evaluation Flow:

```text
Agent Output
→ Review Findings
→ Check Findings against Requirements / Evidence
→ Check Severity
→ Check Fix Recommendation
→ Review Pass / Review Fix
```

Review 결과:

```text
Effective Review:
- 실제 결함 탐지
- Evidence 제공
- Severity 적절
- Fix 구체적

Weak Review:
- 피상적 지적
- Evidence 부족
- Severity 부정확
- Fix 추상적

Bad Review:
- 핵심 결함 누락
- False Positive 다수
- 사용자 요구사항 무시
- 근거 없는 지적
```

---

### [실무]

실무에서는 Review Agent 자체를 다음 기준으로 평가한다.

좋은 Review 예시:

```md
| Severity | Issue                                | Evidence                        | Fix                    |
| -------- | ------------------------------------ | ------------------------------- | ---------------------- |
| Major    | Retrieval Queries 누락               | 문서 마지막에 해당 섹션 없음    | Retrieval Queries 추가 |
| Critical | 존재하지 않는 Repository 메서드 사용 | 제공된 Repository에 메서드 없음 | 실제 메서드명으로 수정 |
```

나쁜 Review 예시:

```text
- 문서가 좀 더 좋아지면 좋겠습니다.
- 코드 스타일을 조금 개선하세요.
```

문제:

- Issue 불명확
- Evidence 없음
- Severity 없음
- Fix 불명확

Review Agent 평가 Report:

```md
| Review Item     | Result | Issue                | Fix           |
| --------------- | ------ | -------------------- | ------------- |
| Finding Quality | Pass   | 실제 누락 탐지       | 없음          |
| Evidence        | Fix    | 일부 지적 근거 부족  | Evidence 추가 |
| Severity        | Fix    | Minor를 Major로 과장 | Severity 수정 |
| Fix Direction   | Pass   | 구체적 수정안 제시   | 없음          |
```

False Positive 예시:

```text
Review Finding:
FAQ가 너무 많으므로 줄여야 한다.

Context:
User Requirement = FAQ 강화
Domain Rules = FAQ와 Retrieval Queries 강화

Evaluation:
- False Positive
- 사용자 요구사항과 Domain Rules를 무시한 지적
```

False Negative 예시:

```text
Output:
Retrieval Queries 없음

Review:
문제 없음

Evaluation:
- False Negative
- Required Section 누락을 놓침
```

---

### [주의]

Review Effectiveness 주의사항:

- Review Agent도 Hallucination을 만들 수 있다.
- Review Agent가 취향을 결함처럼 지적할 수 있다.
- 너무 엄격한 Review는 Workflow 속도를 낮춘다.
- 너무 느슨한 Review는 결함을 남긴다.
- Evidence 없는 Finding은 신뢰도가 낮다.
- Severity가 부정확하면 Fix 우선순위가 흐려진다.
- Domain Rules와 사용자 요구사항을 기준으로 Review해야 한다.

---

### [Best Practice]

Review Effectiveness Best Practice:

- Review Criteria를 명확히 둔다.
- Finding마다 Evidence를 포함한다.
- Severity를 Critical / Major / Minor / Info로 나눈다.
- 취향, 개선, 결함을 구분한다.
- 사용자 요구사항과 Domain Rules를 우선 기준으로 삼는다.
- False Positive와 False Negative를 추적한다.
- Review Agent Output도 다시 평가한다.
- Fix Direction은 실행 가능하게 작성한다.

---

### [FAQ]

Q. Review Effectiveness가 뭐야?
A. Review Agent가 실제 결함을 정확히 찾고 적절한 Severity와 Fix 방향을 제시했는지 평가하는 기준이다.

Q. Review Agent도 평가해야 해?
A. 해야 한다. Review Agent가 쓸데없는 지적을 하거나 중요한 문제를 놓칠 수 있기 때문이다.

Q. False Positive는 뭐야?
A. 실제 문제가 아닌 것을 문제로 지적하는 것이다.

Q. False Negative는 뭐야?
A. 실제 중요한 문제를 놓치는 것이다.

Q. 좋은 Review Finding 조건은 뭐야?
A. Issue, Evidence, Severity, Fix Recommendation이 명확해야 한다.

Q. 취향과 결함은 어떻게 구분해?
A. 결함은 요구사항, 안전, 근거, 형식, 코드 정확성을 위반하는 것이고 취향은 대안 가능한 스타일 차이다.

---

# 6. Fix Effectiveness Evaluation

## 6.1 Fix Effectiveness

### [개념]

Fix Effectiveness는 Fix Agent 또는 수정 단계가 Review Finding을 실제로 해결했는지 평가하는 기준이다.

Fix가 적용되었다고 해서 문제가 해결된 것은 아니다.

Fix Effectiveness는 Review Finding과 수정 결과를 매핑해 검증한다.

---

### [핵심]

Fix Effectiveness 검증 항목:

| 항목                     | 의미                                   |
| ------------------------ | -------------------------------------- |
| Finding Coverage         | Review Finding을 모두 다뤘는가         |
| Correct Fix              | 수정이 문제를 실제로 해결했는가        |
| Regression Risk          | 수정으로 새로운 문제가 생기지 않았는가 |
| Requirement Preservation | 기존 요구사항을 유지했는가             |
| Format Preservation      | 출력 형식이 유지되었는가               |
| Evidence Update          | 수정 후 근거가 갱신되었는가            |
| Re-evaluation            | 수정 후 재검토했는가                   |

Fix Evaluation Flow:

```text
Review Findings
→ Fix Output
→ Map Finding to Fix
→ Check Resolution
→ Check Regression
→ Re-evaluate
→ Pass / Fix Again / Stop
```

Fix 결과:

```text
Resolved:
- Review Finding 해결
- 새로운 문제 없음

Partially Resolved:
- 일부 문제만 해결
- 추가 Fix 필요

Unresolved:
- Finding 미반영
- 문제 그대로 남음

Regression:
- 기존 문제 해결 중 새로운 문제 발생
```

---

### [실무]

실무에서는 Fix Mapping Table을 사용한다.

Fix Mapping 예시:

```md
| Review Finding         | Fix Applied      | Result             | Regression |
| ---------------------- | ---------------- | ------------------ | ---------- |
| [FAQ] 누락             | FAQ 추가         | Resolved           | 없음       |
| Retrieval Queries 누락 | 문서 마지막 추가 | Resolved           | 없음       |
| Header 계층 오류       | H2/H3 정리       | Resolved           | 없음       |
| Unsupported Claim 존재 | 일부만 제거      | Partially Resolved | 없음       |
```

Backend Fix 예시:

```text
Review Finding:
존재하지 않는 findUnreadByUserId() 사용

Fix:
countByUsers_UserIdAndReadStatusFalse(userId)로 수정

Evaluation:
- 실제 Repository 메서드와 일치
- Resolved
```

Format Regression 예시:

```text
Review Finding:
FAQ 답변이 너무 김

Fix:
FAQ 답변을 줄임

Regression:
Retrieval Queries 섹션이 삭제됨

Evaluation:
- 기존 문제 일부 해결
- 새로운 Format Failure 발생
```

---

### [주의]

Fix Effectiveness 주의사항:

- Fix가 Review Finding을 직접 해결했는지 확인해야 한다.
- 일부 수정만 하고 전체 해결로 표시하면 안 된다.
- Fix 과정에서 기존 요구사항을 삭제하면 Regression이다.
- Format Fix 중 Content Quality가 낮아질 수 있다.
- Code Fix 중 새로운 Compile Error가 생길 수 있다.
- Fix 후 재검토 없이 Pass 처리하면 위험하다.
- Review Finding이 잘못된 경우 Fix하지 말고 False Positive로 표시한다.

---

### [Best Practice]

Fix Effectiveness Best Practice:

- Review Finding과 Fix를 1:1로 매핑한다.
- Resolved / Partially Resolved / Unresolved / Regression으로 표시한다.
- Fix 후 Requirement Compliance를 다시 확인한다.
- Fix 후 Format Compliance를 다시 확인한다.
- 코드 수정은 컴파일 가능성과 Symbol을 재검증한다.
- 새로운 문제가 생기면 Regression으로 기록한다.
- Review Finding 자체가 틀렸으면 False Positive로 분류한다.
- 반복 Fix가 실패하면 Stop Condition을 적용한다.

---

### [FAQ]

Q. Fix Effectiveness가 뭐야?
A. Fix 단계가 Review Finding을 실제로 해결했는지 평가하는 기준이다.

Q. Fix가 적용되면 문제는 해결된 거야?
A. 아니다. Review Finding과 수정 결과를 매핑해 해결 여부를 확인해야 한다.

Q. Partially Resolved는 뭐야?
A. 일부 문제만 해결되고 일부는 남아 있는 상태다.

Q. Regression은 뭐야?
A. 기존 문제를 고치는 과정에서 새로운 문제가 생긴 상태다.

Q. Fix 후 다시 평가해야 해?
A. 해야 한다. Requirement, Format, Grounding, Code 기준을 다시 확인해야 한다.

Q. Review Finding이 틀렸으면 어떻게 해?
A. Fix하지 않고 False Positive로 표시해야 한다.

---

# 7. Workflow Stop Condition

## 7.1 Workflow Stop Condition

### [개념]

Workflow Stop Condition은 Multi-Agent Workflow가 언제 멈춰야 하는지 정의하는 기준이다.

Stop Condition은 무한 Review-Fix Loop, 위험 Tool 실행, 정보 부족 상태의 억지 완료를 막는다.

Workflow Stop은 실패만 의미하지 않는다.

사용자 확인 필요, 권한 부족, 안전 차단, Low Confidence 상태일 수도 있다.

---

### [핵심]

Workflow Stop Condition:

```text
Stop if:
- Required information is missing
- Handoff Context is insufficient
- Tool call failed and no fallback exists
- High Risk action requires Human Confirmation
- Unsafe action is detected
- Max review-fix iteration is reached
- State conflict cannot be resolved
- Critical Requirement Failure remains
- Grounding Failure remains
- Low Confidence remains
```

Stop 상태:

| 상태                    | 의미                     |
| ----------------------- | ------------------------ |
| Completed               | 정상 완료                |
| Needs User Confirmation | 사용자 승인 필요         |
| Blocked                 | 안전 / 권한 문제로 차단  |
| Failed                  | Tool 실패 또는 정보 부족 |
| Max Iteration Reached   | 반복 한계 도달           |
| Low Confidence          | 신뢰도 부족으로 중단     |
| Conflict                | 상태 충돌로 진행 불가    |

Stop Flow:

```text
Workflow Step
→ Check Failure / Risk / Missing Info
→ Retry or Fix Possible?
→ Yes: Continue with Limit
→ No: Stop
```

---

### [실무]

실무에서는 Review-Fix Loop에 Max Iteration을 둔다.

Review-Fix Stop 예시:

```text
Draft
→ Review
→ Fix
→ Review
→ Fix
→ Review
→ Max Iteration Reached
→ Stop and Report Remaining Issues
```

Tool Failure Stop 예시:

```text
Build Tool Failed
→ Retry 1회
→ 동일 실패
→ Fallback 없음
→ Stop
```

Human Confirmation Stop 예시:

```text
Deploy Request
→ High Risk
→ Action Preview
→ Human Confirmation Required
→ Stop until approval
```

State Conflict Stop 예시:

```text
Agent A:
Docker 문서 완료

Agent B:
Docker 문서 미완료

Project Progress:
Docker Completed

Evaluation:
- Agent B state conflict
- Fix 가능
- Project Progress 기준으로 수정
```

Stop Report 예시:

```md
### Workflow Stop Report

| Stop Reason                 | Evidence                 | Required Action  |
| --------------------------- | ------------------------ | ---------------- |
| Human Confirmation Required | DB DELETE 작업           | 사용자 승인 필요 |
| Missing Information         | Repository 코드 없음     | 코드 제공 필요   |
| Max Iteration Reached       | 같은 Format Failure 반복 | Schema 단순화    |
| Tool Failure                | Build timeout 반복       | 수동 확인 필요   |
```

---

### [주의]

Workflow Stop Condition 주의사항:

- 실패를 성공으로 처리하지 않는다.
- 사용자 승인 필요 상태에서 작업을 계속하지 않는다.
- Max Iteration 없이 Review-Fix를 반복하지 않는다.
- Low Confidence 상태에서 확정 Output을 만들지 않는다.
- Tool Failure 후 Fallback이 없으면 Stop해야 한다.
- Stop 사유와 필요한 다음 행동을 명확히 표시해야 한다.
- 안전 차단은 우회하지 않는다.

---

### [Best Practice]

Workflow Stop Condition Best Practice:

- Workflow 시작 전에 Stop Condition을 정의한다.
- Review-Fix Loop에는 Max Iteration을 둔다.
- High Risk 작업은 승인 전 Stop한다.
- Tool Failure는 Retry Limit 후 Stop 또는 Fallback 처리한다.
- Stop Report에는 사유, Evidence, 필요한 조치를 포함한다.
- Stop과 Fail을 구분한다.
- 사용자가 추가 정보를 주면 Workflow를 재개할 수 있게 Missing Information을 명확히 한다.

---

### [FAQ]

Q. Workflow Stop Condition은 뭐야?
A. Multi-Agent Workflow가 언제 멈춰야 하는지 정의하는 기준이다.

Q. Stop은 항상 실패야?
A. 아니다. 사용자 승인 필요, 정보 부족, 안전 차단처럼 안전하게 중단한 상태일 수 있다.

Q. Review-Fix Loop는 계속 반복해도 돼?
A. 안 된다. Max Iteration을 정하고 반복 실패 시 Stop해야 한다.

Q. High Risk 작업은 언제 Stop해?
A. 사용자 승인 전에는 Stop해야 한다.

Q. Tool Failure 후에는 어떻게 해?
A. Retry 가능 여부를 확인하고, Retry Limit 후 Fallback이 없으면 Stop해야 한다.

---

# 8. Workflow Evaluation Checklist

## 8.1 Checklist

### [개념]

Workflow Evaluation Checklist는 Multi-Agent Workflow 전체의 Routing, Handoff, State, Review, Fix, Stop Condition을 검증하기 위한 최소 평가 목록이다.

이 Checklist는 PM Agent, Review Agent, Safety Agent, Orchestrator가 공통으로 사용할 수 있다.

---

### [핵심]

Workflow Evaluation Checklist:

```md
### [Checklist]

- [ ] 사용자 요구사항이 정확히 추출되었는가?
- [ ] 작업 Domain이 올바르게 분류되었는가?
- [ ] 적절한 Agent로 Routing 되었는가?
- [ ] 위험 작업에 Safety Agent 또는 Human Confirmation이 포함되었는가?
- [ ] Handoff에 Task Goal이 포함되었는가?
- [ ] Handoff에 User Requirement가 보존되었는가?
- [ ] Handoff에 Constraints와 Output Format이 포함되었는가?
- [ ] Handoff에 Evidence와 Missing Information이 포함되었는가?
- [ ] Agent 간 State가 일관되는가?
- [ ] Tool Result가 Workflow State에 반영되었는가?
- [ ] Review Agent가 실제 결함을 찾았는가?
- [ ] Review Finding에 Evidence와 Severity가 있는가?
- [ ] Fix가 Review Finding을 해결했는가?
- [ ] Fix로 인한 Regression이 없는가?
- [ ] Stop Condition이 정의되었는가?
- [ ] Max Iteration이 적용되었는가?
- [ ] Final Output이 원래 사용자 요청과 일치하는가?
```

최소 Pass 기준:

```text
- Routing 정확
- Handoff 충분
- State 일관
- Review / Fix 유효
- 위험 작업 통제
- Stop Condition 적용
- Final Output 요구사항 충족
```

---

### [실무]

실무에서는 Workflow Evaluation Checklist를 최종 Output 전 적용한다.

적용 Flow:

```text
User Request
→ PM Routing
→ Agent Execution
→ Handoff Check
→ Review Check
→ Fix Check
→ Stop Condition Check
→ Final Output Check
```

Checklist Result 예시:

```md
### Workflow Evaluation Result

| Category | Item                                | Result | Fix              |
| -------- | ----------------------------------- | ------ | ---------------- |
| Routing  | Backend 작업을 Backend Agent로 전달 | Pass   | 없음             |
| Handoff  | Output Format 누락                  | Fix    | Format 추가      |
| State    | Progress 상태 일치                  | Pass   | 없음             |
| Review   | Evidence 없는 Finding 존재          | Fix    | Evidence 추가    |
| Fix      | 일부 Finding 미반영                 | Fix    | 재수정           |
| Stop     | High Risk 승인 없음                 | Stop   | 사용자 승인 필요 |
```

---

### [주의]

Workflow Evaluation Checklist 주의사항:

- Checklist는 최소 기준이며 세부 Domain Evaluation을 대체하지 않는다.
- 단일 Agent 작업에도 Routing과 Requirement Preservation은 확인할 수 있다.
- Handoff가 없더라도 Context Preservation은 확인해야 한다.
- Review가 없는 Workflow는 품질 게이트가 약하다.
- Fix가 없는 Review는 실제 개선으로 이어지지 않는다.
- Final Output만 보고 Pass 처리하지 않는다.
- 안전 관련 항목은 다른 항목보다 우선한다.

---

### [Best Practice]

Workflow Evaluation Checklist Best Practice:

- Workflow 단계별로 Evaluation Log를 남긴다.
- Routing, Handoff, State, Review, Fix를 분리해서 본다.
- Critical Issue는 즉시 Stop 또는 Fix 처리한다.
- Evidence 없는 Review Finding은 보완한다.
- Fix 결과는 Review Finding과 매핑한다.
- Final Output 전 원래 사용자 요구사항과 다시 비교한다.
- 반복 실패는 Workflow Rule 개선 대상으로 기록한다.

---

### [FAQ]

Q. Workflow Evaluation Checklist는 뭐야?
A. Multi-Agent Workflow 전체의 Routing, Handoff, State, Review, Fix, Stop Condition을 검증하는 최소 평가 목록이다.

Q. Workflow Checklist는 언제 써?
A. Final Output 전이나 Workflow Review 단계에서 사용한다.

Q. Workflow Checklist에서 가장 중요한 항목은 뭐야?
A. Routing 정확성, Handoff 품질, State 일관성, Review / Fix 유효성, Stop Condition이다.

Q. Final Output만 좋으면 Workflow Pass야?
A. 아니다. 중간에 위험 작업이나 근거 없는 상태 변경이 있으면 Workflow Failure일 수 있다.

Q. Review가 없으면 Workflow가 불완전해?
A. 고위험 또는 복잡한 작업에서는 Review가 없으면 품질 게이트가 약하다.

---

# Retrieval Queries

### [FAQ]

Q. Workflow Evaluation이 뭐야?
A. Multi-Agent System에서 Agent 실행 흐름 전체가 사용자 요구사항을 올바르게 처리했는지 평가하는 기준이다.

Q. Workflow Evaluation은 무엇을 평가해?
A. Routing Accuracy, Handoff Quality, State Consistency, Review Effectiveness, Fix Effectiveness, Stop Condition, Final Output Quality를 평가한다.

Q. Workflow Evaluation은 최종 답변만 보면 돼?
A. 아니다. Routing, Handoff, Intermediate Output, Review, Fix, Tool Result, Stop Condition도 평가해야 한다.

Q. Agent 수가 많으면 Workflow 품질도 좋아져?
A. 아니다. Agent가 많아도 Routing과 Handoff가 부정확하면 품질이 낮아진다.

Q. Routing Accuracy가 뭐야?
A. 사용자 요청을 적절한 Agent에게 배정했는지 평가하는 기준이다.

Q. Routing은 어떤 기준으로 해?
A. Domain, Risk Level, Output Type, 작업 복잡도, Tool 필요성을 기준으로 한다.

Q. Routing이 틀리면 어떤 문제가 생겨?
A. 전문성이 맞지 않는 Agent가 작업해 Output 품질이 낮아지고 요구사항 누락이 발생할 수 있다.

Q. 위험 작업 Routing에는 무엇이 필요해?
A. Safety Agent, Human Confirmation, Risk Classification이 필요할 수 있다.

Q. Handoff Quality가 뭐야?
A. Agent 간 작업 전달 시 필요한 Context, 요구사항, 제약, 근거, 출력 형식이 충분히 전달되었는지 평가하는 기준이다.

Q. 좋은 Handoff에는 뭐가 들어가?
A. Task Goal, User Requirement, Constraints, Context, Evidence, Assumption, Missing Information, Risk Level, Output Format이 들어간다.

Q. Handoff가 부실하면 어떤 문제가 생겨?
A. 다음 Agent가 잘못된 가정으로 작업하고 요구사항 누락이나 Hallucination이 발생할 수 있다.

Q. Assumption도 Handoff에 포함해야 해?
A. 포함해야 한다. 단, 사실과 구분해서 명시해야 한다.

Q. Missing Information은 Handoff에서 숨겨도 돼?
A. 안 된다. 검증 불가 영역을 숨기면 다음 Agent가 근거 없는 결론을 만들 수 있다.

Q. State Consistency가 뭐야?
A. Workflow 진행 중 Agent 간 공유 상태와 Tool 결과, Memory, 진행 상태가 서로 일관되는지 평가하는 기준이다.

Q. State가 불일치하면 어떤 문제가 생겨?
A. Agent가 오래된 정보나 잘못된 Context를 기준으로 작업해 오류가 발생한다.

Q. Memory와 현재 요청이 충돌하면 무엇을 우선해?
A. 현재 사용자 요청을 우선해야 한다.

Q. Planned와 Completed를 혼동하면 어떤 문제야?
A. 프로젝트 진행 상태를 왜곡하는 State Consistency Failure다.

Q. Review Effectiveness가 뭐야?
A. Review Agent가 실제 결함을 정확히 찾고 적절한 Severity와 Fix 방향을 제시했는지 평가하는 기준이다.

Q. Review Agent도 평가해야 해?
A. 해야 한다. Review Agent가 쓸데없는 지적을 하거나 중요한 문제를 놓칠 수 있기 때문이다.

Q. False Positive는 뭐야?
A. 실제 문제가 아닌 것을 문제로 지적하는 것이다.

Q. False Negative는 뭐야?
A. 실제 중요한 문제를 놓치는 것이다.

Q. 좋은 Review Finding 조건은 뭐야?
A. Issue, Evidence, Severity, Fix Recommendation이 명확해야 한다.

Q. Fix Effectiveness가 뭐야?
A. Fix 단계가 Review Finding을 실제로 해결했는지 평가하는 기준이다.

Q. Fix가 적용되면 문제는 해결된 거야?
A. 아니다. Review Finding과 수정 결과를 매핑해 해결 여부를 확인해야 한다.

Q. Partially Resolved는 뭐야?
A. 일부 문제만 해결되고 일부는 남아 있는 상태다.

Q. Regression은 뭐야?
A. 기존 문제를 고치는 과정에서 새로운 문제가 생긴 상태다.

Q. Workflow Stop Condition은 뭐야?
A. Multi-Agent Workflow가 언제 멈춰야 하는지 정의하는 기준이다.

Q. Stop은 항상 실패야?
A. 아니다. 사용자 승인 필요, 정보 부족, 안전 차단처럼 안전하게 중단한 상태일 수 있다.

Q. Review-Fix Loop는 계속 반복해도 돼?
A. 안 된다. Max Iteration을 정하고 반복 실패 시 Stop해야 한다.

Q. High Risk 작업은 언제 Stop해?
A. 사용자 승인 전에는 Stop해야 한다.

Q. Tool Failure 후에는 어떻게 해?
A. Retry 가능 여부를 확인하고 Retry Limit 후 Fallback이 없으면 Stop해야 한다.

Q. Workflow Evaluation Checklist는 언제 써?
A. Final Output 전이나 Workflow Review 단계에서 사용한다.

Q. Final Output만 좋으면 Workflow Pass야?
A. 아니다. 중간에 위험 작업이나 근거 없는 상태 변경이 있으면 Workflow Failure일 수 있다.

Q. Workflow Evaluation의 최종 목표는 뭐야?
A. Agent Workflow가 요구사항을 유지하고, 적절히 Routing하며, 안전하게 Review / Fix를 거쳐 신뢰 가능한 Final Output을 만들도록 검증하는 것이다.
