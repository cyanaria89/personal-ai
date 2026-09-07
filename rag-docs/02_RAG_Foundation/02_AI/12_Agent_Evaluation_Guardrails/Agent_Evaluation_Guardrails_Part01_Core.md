# Agent Evaluation & Guardrails Part01 - Core

---

# 1. Agent Evaluation & Guardrails Core

## 1.1 Agent Evaluation

### [개념]

Agent Evaluation은 AI Agent가 생성한 결과물이 사용자 요구사항, 제공된 Context, RAG 문서, 출력 형식, 안전 기준을 만족하는지 평가하는 과정이다.

Agent Evaluation은 최종 답변만 평가하지 않는다.

평가 대상:

- Agent Output
- Intermediate Output
- Tool Calling Result
- RAG Grounding
- Workflow Routing
- Review / Fix Result
- Final Output

Agent Evaluation의 목적은 Agent 결과를 무조건 신뢰하지 않고, 검증 가능한 기준으로 Pass / Fail / Fix를 판단하는 것이다.

---

### [핵심]

Agent Evaluation 핵심 기준:

- Correctness
- Completeness
- Groundedness
- Faithfulness
- Requirement Compliance
- Format Compliance
- Safety
- Consistency
- Actionability

Agent Evaluation 기본 Flow:

```text
Agent Output
→ Requirement Check
→ Grounding Check
→ Format Check
→ Safety Check
→ Tool / State Check
→ Pass or Fix
```

중요 원칙:

- Agent Output은 항상 검증 대상이다.
- RAG 기반 답변은 Retrieved Context와 일치해야 한다.
- Tool Calling 결과는 실행 상태와 결과 정확성을 검증해야 한다.
- Workflow 결과는 중간 Handoff와 Review 품질까지 확인해야 한다.
- 근거 없는 확정 답변은 Unsupported Claim으로 분류한다.

금지:

- Agent 답변을 무조건 신뢰
- 최종 답변만 보고 전체 Workflow 성공 판단
- 문서에 없는 프로젝트 사실 생성
- Tool 실패를 성공처럼 포장
- 요구사항 누락을 Minor Issue로만 처리

---

### [실무]

2026 실무 기준 Agent Evaluation은 Multi-Agent Workflow의 품질 게이트 역할을 한다.

개인 AI 개발팀 구조에서는 PM Agent, Backend Agent, Frontend Agent, Review Agent, DevOps Agent, AI/ML Agent가 각자 산출물을 만든다.

각 Agent 산출물은 다음 단계로 전달되기 전에 평가되어야 한다.

실무 평가 순서:

```text
User Request
→ PM Agent Output Evaluation
→ Specialist Agent Output Evaluation
→ Review Agent Evaluation
→ Fix Result Evaluation
→ Final Output Evaluation
```

예시:

```text
User Requirement:
- Java 21 기준
- Spring Boot 3.x 기준
- ApiResponse<T> 직접 반환
- 예외는 GlobalExceptionHandler 처리

Evaluation:
- Java 21 문법 사용 여부
- Spring Boot 3.x 호환 여부
- ResponseEntity 사용 여부
- 예외 처리 중복 여부
- 프로젝트 규칙 위반 여부
```

실무 판단 기준:

| Evaluation Target | 주요 평가 기준                                  |
| ----------------- | ----------------------------------------------- |
| PM Agent          | 요구사항 분해, Agent Routing, 누락 여부         |
| Backend Agent     | 코드 정확성, 프로젝트 규칙, 컴파일 가능성       |
| Frontend Agent    | API 연동, 상태 처리, UI 흐름                    |
| Review Agent      | 결함 탐지, Severity 정확도, False Positive      |
| DevOps Agent      | 실행 안전성, 배포 위험도, 설정 검증             |
| AI/ML Agent       | RAG Grounding, Tool Calling, Output Reliability |

Agent Evaluation 결과는 Pass / Fix / Stop 중 하나로 정리한다.

```text
Pass:
- 요구사항 충족
- 근거 충분
- 형식 정상
- 안전 문제 없음

Fix:
- 일부 요구사항 누락
- 형식 오류
- 근거 부족
- 코드 개선 필요

Stop:
- 정보 부족
- Tool 실패
- 위험 작업 승인 필요
- Low Confidence
```

---

### [주의]

Agent Evaluation 주의사항:

- 답변이 길다고 Completeness가 높은 것은 아니다.
- 코드가 그럴듯해도 존재하지 않는 클래스나 메서드를 사용할 수 있다.
- Citation이 있어도 실제 근거가 아닐 수 있다.
- 형식이 맞아도 내용이 틀릴 수 있다.
- Review Agent도 평가 대상이다.
- 오래된 Memory는 현재 요청보다 우선하지 않는다.
- Tool Calling은 실제 시스템 Side Effect를 만들 수 있다.

---

### [Best Practice]

Agent Evaluation Best Practice:

- Requirement Compliance를 가장 먼저 확인한다.
- RAG 답변은 Groundedness와 Faithfulness를 분리해서 평가한다.
- Unsupported Claim을 명시적으로 표시한다.
- Tool Calling은 Tool Choice, Arguments, Permission, Result를 모두 확인한다.
- 위험 작업은 Human Confirmation 상태로 중단한다.
- 평가 결과에는 Evidence와 Fix Recommendation을 포함한다.
- Review Agent의 False Positive / False Negative도 추적한다.
- 반복 실패는 Failure Classification 후 Fallback 처리한다.

---

### [FAQ]

Q. Agent Evaluation이 뭐야?
A. Agent가 만든 결과가 요구사항, 근거, 형식, 안전 기준을 만족하는지 평가하는 과정이다.

Q. Agent Output은 무조건 검증해야 해?
A. 해야 한다. Agent Output은 그럴듯해도 요구사항 누락, 근거 부족, Hallucination이 있을 수 있다.

Q. 최종 답변만 평가하면 안 돼?
A. 안 된다. Multi-Agent Workflow에서는 Routing, Handoff, Tool Calling, Review, Fix 과정도 평가해야 한다.

Q. Agent Evaluation에서 가장 먼저 볼 것은 뭐야?
A. Requirement Compliance다. 사용자 요구사항과 금지 조건을 먼저 확인해야 한다.

Q. RAG 기반 답변은 무엇을 평가해야 해?
A. Groundedness와 Faithfulness를 평가해야 한다. 답변이 Retrieved Context에 근거하고 Context를 왜곡하지 않아야 한다.

Q. Agent Evaluation 결과는 어떻게 나눠?
A. Pass, Fix, Stop으로 나눈다. 통과 가능하면 Pass, 수정 필요하면 Fix, 진행 불가하면 Stop이다.

Q. Review Agent도 평가 대상이야?
A. 맞다. Review Agent가 중요한 문제를 놓치거나 쓸데없는 지적을 많이 하면 Workflow 품질이 떨어진다.

---

# 2. Guardrails Core

## 2.1 Guardrails

### [개념]

Guardrails는 Agent가 위험하거나 부정확한 행동을 하지 않도록 제한하고 통제하는 규칙이다.

Guardrails는 Agent의 자유도를 완전히 막는 것이 아니다.

목적:

- 위험 행동 차단
- 근거 없는 답변 방지
- Tool Calling 안전성 확보
- Memory 오용 방지
- RAG Grounding 강제
- Human Confirmation 필요 여부 판단
- Stop Condition 적용

Guardrails는 Agent 실행 전, 실행 중, 실행 후 모두 적용될 수 있다.

---

### [핵심]

Guardrails 핵심 구성:

- Safety Rule
- Scope Limit
- Tool Permission
- Human Confirmation
- Grounding Rule
- Output Validation
- Retry Limit
- Stop Condition

Guardrail 기본 Flow:

```text
Agent Action
→ Check Policy / Scope
→ Check Tool Permission
→ Check Risk Level
→ Allow / Ask / Block
```

Guardrails 유형:

| 유형                | 목적                                           |
| ------------------- | ---------------------------------------------- |
| Prompt Guardrails   | 역할, 범위, 출력 형식, 금지 조건 제한          |
| Tool Guardrails     | Tool 선택, 인자 검증, 권한, 실행 위험 통제     |
| Memory Guardrails   | 오래된 Memory, 충돌 Memory, 민감정보 저장 방지 |
| RAG Guardrails      | Retrieved Context 우선, Unsupported Claim 방지 |
| Workflow Guardrails | Stop Condition, Retry Limit, Handoff 품질 통제 |

판단 결과:

```text
Allow:
- Low Risk
- 근거 충분
- 권한 문제 없음
- 사용자 승인 불필요

Ask:
- 정보 부족
- Medium / High Risk
- 외부 Side Effect 가능
- 사용자 확인 필요

Block:
- Secret 노출
- 위험 명령 실행
- 정책 위반
- 근거 없는 치명적 주장
```

---

### [실무]

2026 실무 기준 Guardrails는 Tool Calling Agent와 Multi-Agent Workflow에서 필수다.

특히 개인 AI 개발팀 구조에서는 Agent가 코드 작성, 파일 수정, 설정 변경, 배포, 이메일 발송, DB 변경 같은 작업을 제안하거나 실행할 수 있다.

위험도 기반 Guardrail이 필요하다.

Risk Classification:

| Risk   | 작업 예시                              | 처리             |
| ------ | -------------------------------------- | ---------------- |
| Low    | 설명, 요약, 검색, 파일 읽기            | 자동 허용 가능   |
| Medium | 파일 생성, 초안 작성, 설정 제안        | 검증 후 진행     |
| High   | 파일 삭제, DB 변경, 배포, 이메일 발송  | 사용자 승인 필요 |
| Block  | Secret 노출, 위험 명령, 악성 코드 실행 | 차단             |

Tool Guardrail 예시:

```text
Tool Call
→ Validate Tool Choice
→ Validate Arguments
→ Check Permission
→ Check Risk Level
→ Require Human Confirmation if High Risk
→ Execute or Stop
```

RAG Guardrail 예시:

```text
Retrieved Context 있음
→ Context 기반 답변
→ 주요 Claim 근거 확인
→ Unsupported Claim 제거
→ Missing Information 표시
```

Memory Guardrail 예시:

```text
Memory 사용 전
→ 최신성 확인
→ 현재 요청과 충돌 확인
→ 민감정보 여부 확인
→ 불확실하면 Assumption 표시
```

Human Confirmation이 필요한 작업:

- 파일 삭제
- DB 데이터 변경
- 배포 실행
- 이메일 발송
- 결제 요청
- 대량 API 호출
- 비용 발생 작업
- 되돌리기 어려운 설정 변경

---

### [주의]

Guardrails 주의사항:

- Prompt Guardrail만으로 안전을 보장할 수 없다.
- Tool Guardrail 없이 외부 Tool을 실행하면 위험하다.
- Guardrail이 너무 약하면 위험 행동을 막지 못한다.
- Guardrail이 너무 강하면 Agent Workflow가 진행되지 않는다.
- 위험 작업은 Preview와 실제 실행 내용이 일치해야 한다.
- 승인 범위를 넘는 추가 작업은 금지한다.
- 실패 상태를 성공처럼 출력하면 안 된다.

---

### [Best Practice]

Guardrails Best Practice:

- 작업 실행 전 Risk Classification을 수행한다.
- Low / Medium / High / Block 기준을 명확히 둔다.
- High Risk 작업은 Human Confirmation을 필수로 둔다.
- Tool Arguments는 Schema와 실제 대상 기준으로 검증한다.
- RAG 답변은 Retrieved Context 우선 규칙을 적용한다.
- 문서에 없는 프로젝트 고유 정보는 생성하지 않는다.
- Memory는 최신성, 충돌 여부, 민감정보 여부를 확인한다.
- Stop Condition과 Retry Limit을 명시한다.
- 실패 시 Failure Classification 후 Fallback으로 전환한다.

---

### [FAQ]

Q. Guardrails가 뭐야?
A. Agent가 위험하거나 부정확한 행동을 하지 않도록 제한하고 통제하는 규칙이다.

Q. Guardrails는 Agent 작업을 막는 기능이야?
A. 전부 막는 기능은 아니다. 위험 작업은 통제하고 안전한 작업은 진행하도록 돕는 기준이다.

Q. Guardrails는 언제 적용해?
A. 실행 전, 실행 중, 실행 후 모두 적용할 수 있다. 특히 Tool Calling 전에는 반드시 필요하다.

Q. Prompt Guardrails만 있으면 충분해?
A. 부족하다. Tool Guardrails, Memory Guardrails, RAG Guardrails, Workflow Guardrails가 함께 필요하다.

Q. Human Confirmation은 언제 필요해?
A. 삭제, DB 변경, 배포, 이메일 발송, 결제, 비용 발생 작업처럼 되돌리기 어렵거나 위험한 작업 전에 필요하다.

Q. Guardrails가 너무 강하면 어떻게 돼?
A. Agent가 필요한 작업도 진행하지 못한다. Risk Level 기준으로 Allow / Ask / Block을 나눠야 한다.

Q. Guardrails가 너무 약하면 어떻게 돼?
A. 근거 없는 답변, 위험 Tool 실행, 데이터 손실, 비용 발생, 보안 문제가 생길 수 있다.

---

# 3. Evaluation vs Guardrails

## 3.1 Evaluation과 Guardrails 차이

### [개념]

Evaluation은 Agent 결과를 평가하는 기준이다.

Guardrails는 Agent 행동을 제한하고 통제하는 기준이다.

둘은 목적과 적용 시점이 다르지만 함께 사용해야 Agent Workflow의 신뢰도가 높아진다.

---

### [핵심]

Evaluation vs Guardrails:

| 비교 | Evaluation                    | Guardrails                          |
| ---- | ----------------------------- | ----------------------------------- |
| 목적 | 결과 품질 평가                | 위험 행동 예방/통제                 |
| 시점 | 실행 후 또는 중간             | 실행 전/중/후                       |
| 대상 | Output, Workflow, Tool Result | Prompt, Tool, Memory, RAG, Workflow |
| 결과 | Pass / Fix / Fail             | Allow / Ask / Block                 |
| 예시 | 답변 근거 평가                | Tool 실행 전 승인 요구              |

핵심 관계:

```text
Guardrails
→ 위험 행동 예방

Evaluation
→ 생성 결과 검증

Guardrails + Evaluation
→ 안정적인 Agent Workflow
```

---

### [실무]

실무에서는 Guardrails가 먼저 위험 행동을 줄이고, Evaluation이 결과 품질을 검증한다.

예시 Flow:

```text
User Request
→ Guardrail Check
→ Agent Execution
→ Output Evaluation
→ Review / Fix
→ Final Guardrail Check
→ Final Output
```

예시 상황:

```text
User Request:
서버 설정 파일 수정하고 배포해줘.

Guardrail:
- 설정 파일 수정 = Medium Risk
- 배포 실행 = High Risk
- 사용자 승인 필요

Evaluation:
- 설정 변경 내용이 요구사항과 맞는지 확인
- 배포 명령이 안전한지 확인
- 실패 시 Rollback 계획이 있는지 확인
```

Evaluation만 있고 Guardrails가 없으면 위험한 작업이 실행된 뒤에야 문제를 발견한다.

Guardrails만 있고 Evaluation이 없으면 안전하게 실행했더라도 결과 품질이 낮을 수 있다.

---

### [주의]

Evaluation과 Guardrails 혼동 주의:

- Evaluation은 결과 평가다.
- Guardrails는 행동 통제다.
- Evaluation만으로 위험 실행을 사전에 막을 수 없다.
- Guardrails만으로 결과의 정확성을 보장할 수 없다.
- 둘 중 하나만 있으면 Multi-Agent Workflow 안정성이 낮다.

---

### [FAQ]

Q. Evaluation과 Guardrails 차이는 뭐야?
A. Evaluation은 결과를 평가하는 것이고, Guardrails는 위험 행동을 사전에 막거나 실행 중 통제하는 것이다.

Q. Evaluation만 있으면 안 돼?
A. 부족하다. 위험 Tool 실행은 결과 평가 전에 이미 Side Effect를 만들 수 있다.

Q. Guardrails만 있으면 안 돼?
A. 부족하다. 안전하게 실행했더라도 결과가 틀리거나 요구사항을 누락할 수 있다.

Q. 둘 중 뭐가 먼저야?
A. 위험 행동은 Guardrails가 먼저 막고, 생성된 결과는 Evaluation으로 검증한다.

Q. Multi-Agent에서는 왜 둘 다 필요해?
A. 여러 Agent가 Handoff와 Tool Calling을 수행하므로 행동 통제와 결과 검증이 모두 필요하다.

---

# 4. Core Evaluation Checklist

## 4.1 Agent Output Core Checklist

### [개념]

Core Evaluation Checklist는 Agent Output을 빠르게 검증하기 위한 최소 평가 목록이다.

이 Checklist는 Review Agent, PM Agent, Safety Agent가 공통으로 사용할 수 있다.

---

### [핵심]

Core Checklist:

```md
### [Checklist]

- [ ] 사용자 요구사항을 모두 반영했는가?
- [ ] 금지 조건을 위반하지 않았는가?
- [ ] 답변이 Retrieved Context에 근거하는가?
- [ ] Unsupported Claim이 없는가?
- [ ] 불확실한 내용은 Assumption으로 표시했는가?
- [ ] 출력 형식이 요구사항과 일치하는가?
- [ ] Tool Arguments를 검증했는가?
- [ ] 위험 Tool 실행에 사용자 승인이 있는가?
- [ ] Stop Condition이 정의되어 있는가?
- [ ] 반복 실패 시 Fallback이 있는가?
- [ ] 오래된 Memory를 검증했는가?
```

최소 Pass 기준:

```text
Requirement Compliance = Pass
Groundedness = Pass
Safety = Pass
Format Compliance = Pass
No Critical Unsupported Claim
No Unauthorized High Risk Tool Action
```

---

### [실무]

실무에서는 Checklist를 작업 유형별로 확장한다.

Backend Code Evaluation:

```text
- Java / Spring Boot 버전이 맞는가?
- 존재하는 Entity / DTO / Repository 기준인가?
- Transaction Boundary가 적절한가?
- 예외 처리 구조가 프로젝트 규칙과 맞는가?
- N+1 위험이 있는가?
- 테스트 가능한 구조인가?
```

RAG Answer Evaluation:

```text
- Retrieved Context가 사용되었는가?
- 주요 Claim이 문서 근거와 일치하는가?
- 문서에 없는 내용을 확정하지 않았는가?
- 부족한 정보는 부족하다고 표시했는가?
```

Tool Calling Evaluation:

```text
- Tool 선택이 적절한가?
- Arguments가 Schema와 맞는가?
- 대상 파일 / DB / API가 명확한가?
- Side Effect가 있는가?
- Human Confirmation이 필요한가?
- Tool Result가 성공인지 실패인지 확인했는가?
```

Workflow Evaluation:

```text
- PM Agent Routing이 적절한가?
- Handoff Context가 충분한가?
- Review Agent가 실제 문제를 찾았는가?
- Fix가 Review Finding을 반영했는가?
- 최종 Output이 사용자 요구사항과 일치하는가?
```

---

### [주의]

Checklist 사용 주의:

- Checklist는 최소 기준이며 전체 평가를 대체하지 않는다.
- 모든 항목이 동일한 중요도를 가지지 않는다.
- Safety와 Requirement 위반은 Critical로 볼 수 있다.
- 문서 근거가 없는 프로젝트 고유 정보는 Unsupported Claim이다.
- Tool 실패가 있으면 성공 응답으로 마무리하면 안 된다.

---

### [FAQ]

Q. Core Evaluation Checklist는 왜 필요해?
A. Agent Output을 일관되게 평가하고 요구사항, 근거, 형식, 안전 문제를 빠르게 찾기 위해 필요하다.

Q. Checklist만 통과하면 무조건 좋은 결과야?
A. 아니다. Checklist는 최소 기준이다. 작업 유형별 세부 평가가 추가로 필요할 수 있다.

Q. 가장 중요한 Checklist 항목은 뭐야?
A. Requirement Compliance, Groundedness, Safety, Format Compliance다.

Q. Tool Calling도 Checklist로 평가해야 해?
A. 해야 한다. Tool 선택, 인자 검증, 권한, 실행 결과, Side Effect를 확인해야 한다.

Q. RAG 답변에서 가장 중요한 검증은 뭐야?
A. Retrieved Context에 근거하는지 확인하는 Groundedness 검증이다.

---

# 5. Core Failure Types

## 5.1 Agent Failure Classification

### [개념]

Failure Classification은 Agent 실패를 유형별로 분류하는 기준이다.

실패 유형을 알아야 수정 방향을 명확하게 정할 수 있다.

---

### [핵심]

주요 실패 유형:

| Failure              | 의미                                     |
| -------------------- | ---------------------------------------- |
| Requirement Failure  | 사용자 요구사항 누락 또는 위반           |
| Retrieval Failure    | 필요한 문서 검색 실패                    |
| Grounding Failure    | 근거 없는 답변 생성                      |
| Faithfulness Failure | Context 왜곡 또는 과장                   |
| Format Failure       | 출력 형식 위반                           |
| Tool Failure         | Tool 선택, 실행, 결과 처리 실패          |
| Safety Failure       | 위험 행동 또는 승인 없는 실행            |
| Memory Failure       | 오래된 Memory 또는 충돌 Memory 사용      |
| Workflow Failure     | Routing, Handoff, State 문제             |
| Review Failure       | Review Agent가 문제를 놓치거나 잘못 지적 |

Failure Handling Flow:

```text
Failure Detected
→ Classify Failure Type
→ Check Severity
→ Fix / Retry / Fallback / Stop
```

---

### [실무]

실무에서는 실패 유형별 Fix 전략을 다르게 적용한다.

Failure Fix Strategy:

| Failure             | Fix Strategy                                         |
| ------------------- | ---------------------------------------------------- |
| Requirement Failure | 사용자 요구사항 재대조, 누락 항목 추가               |
| Retrieval Failure   | Query 변형, 문서 범위 확인, Missing Information 표시 |
| Grounding Failure   | Unsupported Claim 제거, Evidence 기반 재작성         |
| Format Failure      | Schema 단순화, 출력 예시 기준 재생성                 |
| Tool Failure        | Tool Result 확인, Arguments 수정, Retry 제한         |
| Safety Failure      | 작업 중단, Human Confirmation 요청                   |
| Memory Failure      | 최신 요청 우선, Memory 충돌 표시                     |
| Workflow Failure    | Routing 재설계, Handoff Context 보강                 |
| Review Failure      | Review Criteria 보강, Severity 기준 수정             |

예시:

```text
문제:
Agent가 문서에 없는 API 경로를 실제 프로젝트에 있는 것처럼 설명함

Failure Type:
Grounding Failure
Hallucination
Unsupported Claim

Fix:
- Retrieved Context와 대조
- 문서에 없는 API 경로 제거
- 필요한 경우 Assumption으로 표시
- 사용자에게 실제 API 코드 확인 요청
```

---

### [주의]

Failure Classification 주의:

- 실패를 성공처럼 포장하지 않는다.
- 단일 실패처럼 보여도 복합 실패일 수 있다.
- Retrieval Failure와 Grounding Failure를 구분한다.
- Tool Failure는 실행 실패와 결과 해석 실패를 구분한다.
- Safety Failure는 우선순위가 높다.
- 반복 실패는 Retry보다 Fallback 또는 Stop이 적절할 수 있다.

---

### [FAQ]

Q. Failure Classification이 왜 필요해?
A. 실패 유형을 알아야 올바른 수정 방향을 정할 수 있기 때문이다.

Q. Requirement Failure는 뭐야?
A. 사용자 요구사항을 누락하거나 금지 조건을 위반한 실패다.

Q. Retrieval Failure와 Grounding Failure 차이는?
A. Retrieval Failure는 필요한 문서를 찾지 못한 것이고, Grounding Failure는 근거 없이 답변한 것이다.

Q. Tool Failure는 어떤 경우야?
A. Tool 선택이 틀렸거나, 인자가 잘못됐거나, 실행 실패를 성공처럼 처리한 경우다.

Q. Safety Failure는 어떻게 처리해?
A. 즉시 중단하고 위험도와 필요한 Human Confirmation을 확인해야 한다.

Q. 반복 실패하면 계속 Retry하면 돼?
A. 안 된다. Retry Limit을 두고 실패가 반복되면 Fallback 또는 Stop으로 전환해야 한다.

---

# 6. Core Stop Condition

## 6.1 Stop Condition

### [개념]

Stop Condition은 Agent가 언제 작업을 멈춰야 하는지 정의하는 기준이다.

Stop Condition은 무한 반복, 위험 실행, 근거 없는 완료 처리를 막는다.

---

### [핵심]

Stop Condition 예시:

```text
Stop if:
- Required information is missing
- Retrieved Context is insufficient
- Tool call failed and no fallback exists
- Action requires user approval
- Unsafe action is detected
- Low confidence remains
- Max review-fix iteration is reached
- Output format repeatedly fails
```

Stop 판단 결과:

| 상태                    | 의미                                   |
| ----------------------- | -------------------------------------- |
| Completed               | 작업 완료                              |
| Needs Fix               | 수정 후 재검토 필요                    |
| Needs User Confirmation | 사용자 승인 필요                       |
| Blocked                 | 안전 또는 권한 문제로 진행 불가        |
| Failed                  | Tool 실패 또는 정보 부족으로 완료 불가 |

---

### [실무]

실무에서는 Stop Condition을 Review-Fix Loop와 Tool Calling Workflow에 반드시 적용한다.

Review-Fix Loop 예시:

```text
Draft Output
→ Review
→ Fix
→ Review
→ Pass or Stop
```

Max Iteration 예시:

```text
Max Review-Fix Iteration = 2 or 3
```

Tool Calling Stop 예시:

```text
Tool Call Failed
→ Retryable 확인
→ Retry Limit 확인
→ Fallback 가능 여부 확인
→ 불가능하면 Stop
```

Human Confirmation Stop 예시:

```text
Agent wants to deploy
→ High Risk
→ Human Confirmation Required
→ Stop until approval
```

RAG Stop 예시:

```text
Retrieved Context 없음
→ 프로젝트 고유 정보 답변 불가
→ Missing Information 표시
→ Stop or Ask
```

---

### [주의]

Stop Condition 주의:

- 완료와 실패를 명확히 구분한다.
- Low Confidence 상태에서 억지로 완료하지 않는다.
- Max Iteration 없이 Review-Fix를 반복하지 않는다.
- 사용자 승인이 필요한 작업은 승인 전 실행하지 않는다.
- Tool 실패를 무시하고 Final Output을 만들지 않는다.
- Missing Information을 임의 생성으로 채우지 않는다.

---

### [FAQ]

Q. Stop Condition은 왜 필요해?
A. Agent가 무한 반복하지 않고 완료, 실패, 사용자 확인 필요 상태를 명확히 판단하기 위해 필요하다.

Q. 언제 Agent를 멈춰야 해?
A. 정보 부족, Tool 실패, 위험 작업 승인 필요, Low Confidence, Max Iteration 도달 시 멈춰야 한다.

Q. Stop은 실패야?
A. 항상 실패는 아니다. 사용자 승인 필요나 정보 부족처럼 안전하게 중단한 상태일 수 있다.

Q. Review-Fix는 몇 번 반복해야 해?
A. 무제한 반복하면 안 된다. 보통 Max Iteration을 정하고 초과 시 Stop 또는 사용자 확인으로 전환한다.

Q. Retrieved Context가 없으면 어떻게 해?
A. 프로젝트 고유 정보는 확정하지 말고 Missing Information으로 표시해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Agent Evaluation이 뭐야?
A. Agent가 만든 결과가 요구사항, 근거, 형식, 안전 기준을 만족하는지 평가하는 과정이다.

Q. Agent Output은 어떻게 평가해?
A. Requirement Compliance, Groundedness, Faithfulness, Format Compliance, Safety, Actionability 기준으로 평가한다.

Q. Agent 결과를 왜 검증해야 해?
A. Agent 결과는 그럴듯해도 요구사항 누락, 근거 부족, Hallucination, Tool 실패가 있을 수 있기 때문이다.

Q. Guardrails가 뭐야?
A. Agent가 위험하거나 부정확한 행동을 하지 않도록 제한하고 통제하는 규칙이다.

Q. Guardrails는 어떤 종류가 있어?
A. Prompt Guardrails, Tool Guardrails, Memory Guardrails, RAG Guardrails, Workflow Guardrails가 있다.

Q. Evaluation과 Guardrails 차이는?
A. Evaluation은 결과를 평가하는 것이고, Guardrails는 위험 행동을 사전에 막거나 실행 중 통제하는 것이다.

Q. Agent Evaluation Flow는 어떻게 돼?
A. Agent Output → Requirement Check → Grounding Check → Format Check → Safety Check → Tool / State Check → Pass or Fix 순서다.

Q. Guardrail Flow는 어떻게 돼?
A. Agent Action → Check Policy / Scope → Check Tool Permission → Check Risk Level → Allow / Ask / Block 순서다.

Q. Agent Output 평가 기준은 뭐야?
A. Correctness, Completeness, Groundedness, Faithfulness, Requirement Compliance, Format Compliance, Safety를 기준으로 평가한다.

Q. Requirement Compliance는 뭐야?
A. 사용자 요구사항과 금지 조건을 Agent 결과가 지켰는지 확인하는 평가 기준이다.

Q. Groundedness는 뭐야?
A. 답변의 주요 주장이 Retrieved Context나 제공 문서에 근거하는지 확인하는 기준이다.

Q. Faithfulness는 뭐야?
A. 답변이 제공된 Context를 왜곡하거나 과장하지 않고 충실히 반영하는지 평가하는 기준이다.

Q. Unsupported Claim은 뭐야?
A. 문서나 Retrieved Context에 근거가 없는 주장이다.

Q. Hallucination은 어떻게 잡아?
A. 문서에 없는 파일명, 클래스명, API, 정책, 잘못된 Citation을 Unsupported Claim으로 표시한다.

Q. Tool Calling은 어떻게 평가해?
A. Tool 선택, Arguments, Permission, Risk Level, Execution Status, Result Validation, Side Effect를 확인한다.

Q. Human Confirmation은 언제 필요해?
A. 삭제, DB 변경, 배포, 이메일 발송, 결제, 대량 API 호출처럼 위험하거나 비용이 발생할 수 있는 작업 전에 필요하다.

Q. Risk Classification은 어떻게 해?
A. 작업의 되돌릴 수 있음, 외부 Side Effect, 비용 영향, 보안 영향을 기준으로 Low / Medium / High / Block으로 나눈다.

Q. Failure Classification은 왜 필요해?
A. Requirement Failure, Retrieval Failure, Grounding Failure, Tool Failure처럼 실패 유형을 알아야 수정 방향을 정할 수 있기 때문이다.

Q. Stop Condition은 왜 필요해?
A. Agent가 무한 반복하거나 위험 작업을 승인 없이 실행하지 않도록 멈춤 기준을 정의하기 위해 필요하다.

Q. Agent가 무한 반복하면 어떻게 해?
A. Max Iteration을 적용하고 반복 실패 시 Failure Classification 후 Fallback 또는 Stop으로 전환한다.

Q. RAG 문서에 근거가 없으면 어떻게 해?
A. 프로젝트 고유 정보는 확정하지 않고 Missing Information 또는 Assumption으로 표시해야 한다.

Q. Review Agent도 평가해야 해?
A. 해야 한다. Review Agent가 False Positive를 많이 내거나 중요한 문제를 놓치면 Workflow 품질이 떨어진다.

Q. Agent Evaluation & Guardrails의 핵심 목표는 뭐야?
A. Agent가 정확하고 근거 있는 결과를 만들고 위험한 작업은 통제하며 실패를 안전하게 처리하도록 만드는 것이다.
