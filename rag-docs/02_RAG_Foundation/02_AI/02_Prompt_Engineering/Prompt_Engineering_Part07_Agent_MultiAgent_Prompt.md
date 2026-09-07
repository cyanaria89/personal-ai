# Prompt Engineering Part07 Agent Prompt and Multi-Agent Prompt

---

# 1. Agent Prompt

## 1.1 Agent Prompt Definition

### [개념]

Agent Prompt는 AI Agent의 역할, 책임, 입력, 출력, 도구 사용, 제약, Handoff, 종료 조건을 정의하는 Prompt다.

Agent Prompt는 단순 역할 지정이 아니다.

Agent Prompt는 Agent가 어떤 범위에서 판단하고, 어떤 결과를 만들고, 언제 작업을 종료해야 하는지 정의하는 실행 규칙이다.

기본 구조:

```text
Agent Role
→ Responsibility
→ Input
→ Output
→ Tools
→ Constraints
→ Handoff Rule
→ Stop Condition
→ Failure Rule
→ Validation
```

Agent Prompt의 목적은 Agent가 반복 가능하고 검증 가능한 방식으로 작업을 수행하도록 만드는 것이다.

---

### [핵심]

- Agent Prompt는 Agent의 행동 규칙이다.
- Role만 지정하면 불충분하다.
- Responsibility와 Scope를 반드시 포함한다.
- Input과 Output을 고정해야 한다.
- Tool 사용 기준을 정의해야 한다.
- Handoff Rule을 포함해야 한다.
- Stop Condition을 포함해야 한다.
- Failure Rule을 포함해야 한다.
- Agent 간 책임 중복을 피해야 한다.
- Agent Prompt는 Multi-Agent Workflow 안정성에 직접 영향을 준다.

---

### [실무]

2026 실무 기준 Agent Prompt는 단일 Prompt보다 “역할 계약서”에 가깝다.

Backend Agent Prompt 예시:

```text
You are a Backend Agent.

Responsibility:
- Receive task requirements from PM Agent.
- Generate backend implementation plan and code snippets.
- Follow Spring Boot project architecture.
- Use retrieved backend RAG documents.

Input:
- PM Agent task brief
- Project context
- Retrieved backend documents
- Existing code snippets

Output:
Markdown with:
- API
- DTO
- Service
- Repository
- Validation Checklist

Constraints:
- Do not modify frontend code.
- Do not invent missing project classes.
- Mark assumptions clearly.
- State missing information.

Handoff Rule:
Return output in a structure that Review Agent can validate.

Stop Condition:
Stop after producing implementation plan and required snippets.
```

Agent Prompt는 역할을 넓게 잡기보다 책임을 좁게 고정하는 것이 안정적이다.

---

### [FAQ]

Q. Agent Prompt가 뭐야?

A. AI Agent의 역할, 책임, 입력, 출력, 도구 사용, 제약, Handoff, 종료 조건을 정의하는 Prompt다.

Q. Agent Prompt는 Role Prompt와 같아?

A. 아니다. Role Prompt는 관점과 책임을 정의하고, Agent Prompt는 입력, 출력, 도구, Handoff, 종료 조건까지 포함한다.

Q. Agent Prompt에서 가장 중요한 것은 뭐야?

A. Responsibility, Input, Output, Constraints, Handoff Rule, Stop Condition이다.

Q. Agent Prompt에 Stop Condition이 왜 필요해?

A. Agent가 무한 반복하거나 작업 범위를 넘어가지 않도록 하기 위해 필요하다.

---

# 2. Agent Prompt Components

## 2.1 Agent Role

### [개념]

Agent Role은 Agent가 어떤 전문 역할을 수행하는지 정의하는 요소다.

Agent Role은 단순 직함이 아니라 작업 관점과 책임 범위를 함께 가져야 한다.

예시:

```text
PM Agent
Backend Agent
Frontend Agent
Review Agent
DevOps Agent
AI/ML Agent
```

---

### [핵심]

- Agent Role은 책임 분리의 시작점이다.
- Role은 도메인과 연결되어야 한다.
- Role은 Scope와 함께 작성해야 한다.
- 하나의 Agent에 너무 많은 Role을 넣으면 안 된다.
- Role은 Domain Rules와 연결되어야 한다.
- Agent Role은 Handoff 구조와 연결된다.

---

### [실무]

Agent Role 예시:

```text
You are a PM Agent.
You decompose user requests and route tasks to Domain Agents.
```

```text
You are a Backend Agent.
You generate backend plans and code snippets based on PM Agent task briefs.
```

```text
You are a Review Agent.
You validate outputs from Domain Agents based on project rules and quality criteria.
```

좋지 않은 Agent Role:

```text
You are an AI developer who does everything.
```

좋은 Agent Role:

```text
You are a Backend Review Agent.
You review Spring Boot backend outputs for transaction boundary, exception handling, DTO responsibility, API consistency, and maintainability.
```

Agent Role은 좁고 명확해야 한다.

---

### [FAQ]

Q. Agent Role은 뭐야?

A. Agent가 어떤 전문 역할과 관점으로 작업할지 정의하는 요소다.

Q. 하나의 Agent가 모든 역할을 하면 안 돼?

A. 권장하지 않는다. 역할이 넓으면 책임이 흐려지고 출력 품질이 낮아질 수 있다.

Q. Agent Role은 Domain Rules와 연결해야 해?

A. 그렇다. Backend Agent는 Backend Rules, Prompt Engineering Agent는 Prompt Engineering Rules처럼 도메인 기준과 연결해야 한다.

---

## 2.2 Responsibility

### [개념]

Responsibility는 Agent가 반드시 수행해야 하는 책임이다.

Agent Role이 “누구인가”를 정의한다면 Responsibility는 “무엇을 책임지는가”를 정의한다.

---

### [핵심]

- Responsibility는 Agent 작업 범위를 정한다.
- Agent 간 Responsibility는 겹치지 않게 설계한다.
- Responsibility는 Output과 연결되어야 한다.
- Responsibility가 모호하면 Handoff 품질이 낮아진다.
- Review Agent는 검증 책임을 가진다.
- PM Agent는 작업 분해와 라우팅 책임을 가진다.
- Domain Agent는 전문 산출물 생성 책임을 가진다.

---

### [실무]

PM Agent Responsibility:

```text
Responsibility:
- Analyze user request.
- Identify required domain.
- Decompose task.
- Prepare structured task brief.
- Route task to appropriate Domain Agent.
- Track missing information.
```

Backend Agent Responsibility:

```text
Responsibility:
- Generate backend implementation plan.
- Design API, DTO, Service, Repository flow.
- Follow retrieved backend RAG documents.
- Mark missing information.
```

Review Agent Responsibility:

```text
Responsibility:
- Validate Domain Agent output.
- Check rule compliance.
- Identify defects, risks, and missing information.
- Return findings with severity and fix direction.
```

Responsibility는 Agent Workflow의 품질 기준이다.

---

### [FAQ]

Q. Responsibility는 뭐야?

A. Agent가 반드시 수행해야 하는 책임과 담당 작업이다.

Q. Agent 간 Responsibility가 겹치면 어떻게 돼?

A. 중복 작업, 충돌 판단, 불안정한 Handoff가 발생할 수 있다.

Q. PM Agent의 핵심 Responsibility는 뭐야?

A. 사용자 요청 분석, 작업 분해, Agent 라우팅, 구조화된 Task Brief 생성이다.

---

## 2.3 Input

### [개념]

Input은 Agent가 작업을 수행할 때 받는 자료와 지시다.

Agent Input은 후속 Agent의 품질을 결정한다.

Input이 불명확하면 Agent는 일반론이나 추정을 생성할 수 있다.

---

### [핵심]

- Input은 구조화되어야 한다.
- Task Brief를 포함해야 한다.
- Project Context를 포함해야 한다.
- Retrieved Context를 포함할 수 있다.
- Existing Code Context를 포함할 수 있다.
- Constraints를 포함해야 한다.
- Missing Information을 포함할 수 있다.
- Input과 Output Schema는 연결되어야 한다.

---

### [실무]

Agent Input Schema 예시:

```md
## Task

## Project Context

## Domain Context

## Retrieved Context

## Existing Code Context

## Constraints

## Expected Output

## Missing Information
```

Backend Agent Input 예시:

```md
## Task

Login Service 구현 계획 작성

## Project Context

- Java 21
- Spring Boot 3.x
- Controller → Service → Repository
- GlobalExceptionHandler 사용

## Existing Code Context

- AuthController 제공됨
- LoginReqDto 제공됨
- UserRepository 제공되지 않음

## Constraints

- 없는 클래스명 생성 금지
- Controller 시그니처 변경 금지
```

Agent Input은 자연어 한 문장보다 구조화된 Markdown이 안정적이다.

---

### [FAQ]

Q. Agent Input은 뭐야?

A. Agent가 작업을 수행하기 위해 받는 Task, Context, Code, Constraints, Retrieved Context 같은 입력 자료다.

Q. Agent Input은 왜 구조화해야 해?

A. Agent가 작업 범위와 판단 근거를 명확히 이해하고 후속 Output을 안정적으로 만들기 위해 필요하다.

Q. Agent Input에 Missing Information을 넣어도 돼?

A. 가능하다. 부족한 정보가 명시되면 Agent가 무리하게 지어내는 것을 줄일 수 있다.

---

## 2.4 Output

### [개념]

Output은 Agent가 작업 후 반환해야 하는 산출물 구조다.

Agent Output은 다음 Agent의 Input이 되므로 고정된 형식이 중요하다.

---

### [핵심]

- Output Format을 고정한다.
- Markdown 또는 JSON Schema를 지정한다.
- 필수 섹션을 명시한다.
- 후속 Agent가 검증 가능한 구조여야 한다.
- Missing Information을 포함해야 한다.
- Assumptions를 포함해야 한다.
- Validation Checklist를 포함할 수 있다.
- Output이 흔들리면 Workflow 전체가 흔들린다.

---

### [실무]

Backend Agent Output Schema:

```md
## Implementation Summary

## API

## DTO

## Service

## Repository

## Assumptions

## Missing Information

## Validation Checklist
```

Review Agent Output Schema:

```md
## Review Summary

## Findings

### 1. Issue

- Severity:
- Cause:
- Risk:
- Fix Direction:

## Missing Information

## Required Fixes

## Final Decision
```

PM Agent Output Schema:

```md
## Task Brief

## Target Agent

## Requirements

## Context

## Constraints

## Expected Output

## Review Criteria
```

Agent Output은 자유 형식보다 Fixed Schema가 좋다.

---

### [FAQ]

Q. Agent Output은 뭐야?

A. Agent가 작업 후 반환하는 구조화된 산출물이다.

Q. Agent Output이 중요한 이유는 뭐야?

A. 한 Agent의 Output이 다음 Agent의 Input이 되므로 구조가 흔들리면 전체 Workflow가 불안정해진다.

Q. Agent Output에는 Missing Information이 필요해?

A. 필요하다. 부족한 정보를 명확히 표시해야 후속 Agent가 잘못된 확정을 하지 않는다.

---

## 2.5 Tool Use Rule

### [개념]

Tool Use Rule은 Agent가 도구를 언제, 어떤 기준으로 사용할지 정의하는 규칙이다.

Agent는 검색, 파일 조회, 코드 실행, API 호출, DB 조회, 웹 검색 같은 도구를 사용할 수 있다.

---

### [핵심]

- Tool 사용 조건을 명확히 한다.
- Tool 결과와 모델 추론을 구분한다.
- Tool 실패 시 Failure Rule을 따른다.
- 최신 정보가 필요하면 검색 도구를 사용한다.
- 파일 기반 작업은 제공된 파일을 우선 사용한다.
- 코드 실행 결과는 확인된 사실로 분리한다.
- Tool 결과를 임의로 확장하지 않는다.

---

### [실무]

Tool Use Rule 예시:

```text
Tool Use Rule:
- Use uploaded documents as primary context for RAG document tasks.
- Use retrieved documents before general knowledge.
- Use code execution only for validation when needed.
- If tool result is insufficient, state missing information.
- Do not invent tool outputs.
```

Code Review Agent Tool Rule:

```text
Tool Use Rule:
- Inspect provided files first.
- Do not assume unseen files.
- If required files are missing, list them under Missing Information.
```

RAG Agent Tool Rule:

```text
Tool Use Rule:
- Use retrieved chunks as primary evidence.
- If retrieval fails, report retrieval insufficiency.
- Do not replace missing retrieved context with unsupported facts.
```

Tool Use Rule은 Agent의 근거 품질을 높인다.

---

### [FAQ]

Q. Tool Use Rule이 뭐야?

A. Agent가 도구를 언제, 어떤 기준으로 사용할지 정의하는 규칙이다.

Q. Tool 결과와 추론은 왜 구분해야 해?

A. 도구로 확인한 사실과 모델의 추정을 구분해야 Hallucination을 줄일 수 있다.

Q. Tool 결과가 부족하면 어떻게 해야 해?

A. 부족한 정보를 Missing Information으로 표시하고 확정적으로 말하지 않아야 한다.

---

## 2.6 Handoff Rule

### [개념]

Handoff Rule은 한 Agent가 다른 Agent에게 작업을 넘길 때 사용하는 전달 규칙이다.

Handoff는 Multi-Agent Workflow의 핵심이다.

Handoff가 불안정하면 후속 Agent가 잘못된 입력을 받아 전체 결과 품질이 낮아진다.

---

### [핵심]

- Handoff Output은 다음 Agent의 Input이다.
- Handoff 구조를 고정해야 한다.
- Task, Context, Constraints, Expected Output을 포함한다.
- Missing Information을 포함한다.
- Assumption을 명확히 표시한다.
- Review Criteria를 포함하면 검증이 쉬워진다.
- Handoff는 장문 설명보다 구조화가 중요하다.

---

### [실무]

Handoff Schema 예시:

```md
## Agent Handoff

### Source Agent

### Target Agent

### Task

### Context

### Constraints

### Expected Output

### Assumptions

### Missing Information

### Review Criteria
```

PM Agent → Backend Agent Handoff:

```md
## Agent Handoff

### Source Agent

PM Agent

### Target Agent

Backend Agent

### Task

Login Service 구현 계획 작성

### Context

- Java 21
- Spring Boot 3.x
- JWT 인증 사용

### Constraints

- Controller 시그니처 변경 금지
- 없는 클래스명 생성 금지

### Expected Output

API, DTO, Service, Repository, Validation Checklist

### Missing Information

- UserRepository 메서드 시그니처 미제공
```

Handoff Rule은 Agent 간 출력 계약이다.

---

### [FAQ]

Q. Handoff Rule이 뭐야?

A. 한 Agent가 다른 Agent에게 작업을 넘길 때 사용하는 구조화된 전달 규칙이다.

Q. Handoff에는 뭐가 들어가야 해?

A. Source Agent, Target Agent, Task, Context, Constraints, Expected Output, Missing Information, Review Criteria가 들어가면 좋다.

Q. Handoff가 불안정하면 어떻게 돼?

A. 후속 Agent가 잘못된 입력을 받아 결과 품질이 낮아지고 Workflow가 흔들릴 수 있다.

---

## 2.7 Stop Condition

### [개념]

Stop Condition은 Agent가 언제 작업을 종료해야 하는지 정의하는 규칙이다.

Stop Condition은 무한 반복, 과도한 작업 확장, 범위 초과를 방지한다.

---

### [핵심]

- Agent 종료 조건을 명확히 한다.
- 작업 완료 기준을 정의한다.
- Review Loop 종료 조건을 정의한다.
- 반복 횟수 제한을 둘 수 있다.
- 추가 정보가 없으면 중단하고 Missing Information을 표시한다.
- Stop Condition이 없으면 Agent가 불필요하게 확장될 수 있다.

---

### [실무]

Stop Condition 예시:

```text
Stop Condition:
- Stop after producing the requested implementation plan.
- Stop after returning review findings and required fixes.
- Stop if required context is missing and cannot be safely assumed.
- Stop after one review-fix cycle unless further iteration is requested.
```

Review Loop Stop Condition:

```text
Review Loop Stop Condition:
- Stop when no Critical or High severity issues remain.
- Stop after maximum 2 review-fix iterations.
- Stop if missing information blocks further validation.
```

Stop Condition은 Agent Workflow 안정성에 필수다.

---

### [FAQ]

Q. Stop Condition이 뭐야?

A. Agent가 언제 작업을 종료해야 하는지 정의하는 규칙이다.

Q. Stop Condition이 없으면 어떤 문제가 생겨?

A. Agent가 무한 반복하거나 요청 범위를 넘어 불필요한 작업을 할 수 있다.

Q. Review Loop에도 Stop Condition이 필요해?

A. 필요하다. 반복 검토가 끝나는 기준이 없으면 무한 루프가 발생할 수 있다.

---

## 2.8 Failure Rule

### [개념]

Failure Rule은 Agent가 작업을 정상 수행할 수 없을 때 어떻게 행동해야 하는지 정의하는 규칙이다.

Failure Rule은 정보 부족, Tool 실패, Context 부족, 범위 초과, 충돌 조건에 대응한다.

---

### [핵심]

- 정보가 부족하면 Missing Information을 표시한다.
- Tool 실패 시 결과를 지어내지 않는다.
- Context가 불충분하면 부분 답변 한계를 표시한다.
- 보이지 않는 코드는 단정하지 않는다.
- 범위 밖 요청은 범위 밖이라고 표시한다.
- 충돌하는 규칙이 있으면 충돌 내용을 표시한다.
- 안전한 범위에서 부분 결과를 제공할 수 있다.

---

### [실무]

Agent Failure Rule 예시:

```text
Failure Rule:
If required information is missing:
- State what is missing.
- Do not invent missing details.
- Provide partial output only if safe.
- Mark assumptions clearly.
```

Code Agent Failure Rule:

```text
Failure Rule:
If Entity, DTO, or Repository code is missing:
- Do not generate final implementation as confirmed code.
- Provide implementation direction.
- List required missing files.
```

RAG Agent Failure Rule:

```text
Failure Rule:
If retrieved context is insufficient:
- Say the retrieved context is insufficient.
- List missing information.
- Do not answer with unsupported project-specific facts.
```

Failure Rule은 Agent가 모르는 내용을 확정하지 않도록 만든다.

---

### [FAQ]

Q. Failure Rule이 뭐야?

A. Agent가 정보 부족, Tool 실패, Context 부족, 범위 초과 상황에서 어떻게 행동할지 정의하는 규칙이다.

Q. Agent가 필요한 정보를 못 받으면 어떻게 해야 해?

A. Missing Information으로 표시하고, 안전한 범위에서만 부분 결과를 제공해야 한다.

Q. Tool 실패 시 결과를 추정해도 돼?

A. 확정하면 안 된다. Tool 실패와 부족한 정보를 명확히 표시해야 한다.

---

# 3. Agent Types

## 3.1 PM Agent

### [개념]

PM Agent는 사용자 요청을 분석하고 작업을 분해하며 적절한 Domain Agent에게 전달하는 Agent다.

PM Agent는 직접 모든 구현을 수행하지 않는다.

PM Agent의 핵심 역할은 Task Decomposition과 Routing이다.

---

### [핵심]

PM Agent 책임:

- User Request 분석
- 요구사항 추출
- 작업 분해
- Target Agent 결정
- Context 정리
- Constraint 정리
- Expected Output 정의
- Missing Information 식별
- Review Criteria 설정
- Handoff 생성

---

### [실무]

PM Agent Prompt 예시:

```text
You are a PM Agent.

Responsibility:
- Analyze user request.
- Decompose the task.
- Identify target Domain Agent.
- Prepare structured task brief.
- Do not implement domain-specific code directly.

Output:
## Task Brief
## Target Agent
## Requirements
## Context
## Constraints
## Expected Output
## Missing Information
## Review Criteria
```

PM Agent는 Domain Agent에게 넘길 입력 품질을 높이는 역할이다.

PM Agent가 불명확한 Handoff를 만들면 전체 Workflow가 흔들린다.

---

### [FAQ]

Q. PM Agent가 뭐야?

A. 사용자 요청을 분석하고 작업을 분해해 적절한 Domain Agent에게 전달하는 Agent다.

Q. PM Agent가 직접 구현해도 돼?

A. 기본적으로 구현보다 작업 분해, 라우팅, Handoff 생성에 집중하는 것이 좋다.

Q. PM Agent의 핵심 산출물은 뭐야?

A. Task Brief, Target Agent, Requirements, Context, Constraints, Expected Output, Review Criteria다.

---

## 3.2 Domain Agent

### [개념]

Domain Agent는 특정 기술 도메인의 작업을 수행하는 Agent다.

Backend Agent, Frontend Agent, DevOps Agent, AI/ML Agent, Prompt Engineering Agent가 Domain Agent에 해당한다.

---

### [핵심]

Domain Agent 책임:

- PM Agent Task Brief 수신
- Domain Rules 적용
- RAG 문서 활용
- 도메인 산출물 생성
- Assumption 표시
- Missing Information 표시
- Review Agent가 검토 가능한 Output 생성

Domain Agent 예시:

- Backend Agent
- Frontend Agent
- DevOps Agent
- AI/ML Agent
- Prompt Engineering Agent
- Security Agent
- Database Agent

---

### [실무]

Backend Agent Prompt 예시:

```text
You are a Backend Agent.

Responsibility:
- Generate backend implementation plan.
- Follow Spring Boot, JPA, Security, API rules.
- Use retrieved backend RAG documents.
- Return structured Markdown for Review Agent.

Input:
- PM Agent Task Brief
- Project Context
- Existing Code Context
- Retrieved Documents

Output:
## Implementation Summary
## API
## DTO
## Service
## Repository
## Assumptions
## Missing Information
## Validation Checklist
```

Domain Agent는 작업 수행 담당이고 Review Agent는 검증 담당이다.

---

### [FAQ]

Q. Domain Agent가 뭐야?

A. Backend, Frontend, DevOps, AI 같은 특정 기술 도메인의 작업을 수행하는 Agent다.

Q. Domain Agent는 어떤 문서를 사용해?

A. 해당 도메인의 RAG 문서와 Domain Rules를 우선 사용한다.

Q. Domain Agent Output은 어떤 구조가 좋아?

A. Review Agent가 검증할 수 있도록 Summary, 산출물, Assumptions, Missing Information, Checklist를 포함하는 구조가 좋다.

---

## 3.3 Review Agent

### [개념]

Review Agent는 Domain Agent의 산출물을 검증하는 Agent다.

Review Agent는 코드, 문서, 설계, Prompt, Agent Output이 규칙과 품질 기준을 만족하는지 확인한다.

---

### [핵심]

Review Agent 책임:

- Domain Agent Output 검토
- Rule Compliance 확인
- Format Compliance 확인
- Missing Information 확인
- Hallucination 확인
- Severity 부여
- Fix Direction 제시
- 최종 통과 여부 판단

Review Agent는 직접 대규모 구현을 수행하지 않는다.

---

### [실무]

Review Agent Prompt 예시:

```text
You are a Review Agent.

Responsibility:
- Review Domain Agent output.
- Check rule compliance.
- Check format compliance.
- Identify risks, missing information, and unsupported claims.
- Return findings with severity and fix direction.

Review Criteria:
- Accuracy
- Completeness
- Groundedness
- Format Compliance
- Project Rule Compliance
- Missing Information Handling

Output:
## Review Summary
## Findings
### 1. Issue
- Severity:
- Cause:
- Risk:
- Fix Direction:
## Required Fixes
## Final Decision
```

Review Agent는 결함과 취향을 구분해야 한다.

---

### [FAQ]

Q. Review Agent가 뭐야?

A. Domain Agent의 산출물이 규칙과 품질 기준을 만족하는지 검증하는 Agent다.

Q. Review Agent는 무엇을 검토해?

A. 정확성, 완전성, 근거성, 형식 준수, 프로젝트 규칙 준수, Missing Information 처리를 검토한다.

Q. Review Agent가 직접 구현도 해야 해?

A. 기본적으로 검증과 수정 방향 제시에 집중하고, 실제 수정은 Fix Agent나 Domain Agent가 수행하는 구조가 안정적이다.

---

## 3.4 Fix Agent

### [개념]

Fix Agent는 Review Agent의 Findings를 반영해 산출물을 수정하는 Agent다.

Fix Agent는 새로운 기능을 추가하는 Agent가 아니라 검토 결과를 반영하는 Agent다.

---

### [핵심]

Fix Agent 책임:

- Review Findings 수신
- Required Fixes 반영
- 기존 Scope 유지
- 새 요구사항 임의 추가 금지
- 수정 전후 차이 정리
- 남은 Risk 표시
- 재검토 가능한 Output 생성

---

### [실무]

Fix Agent Prompt 예시:

```text
You are a Fix Agent.

Responsibility:
- Apply Review Agent findings.
- Preserve original task scope.
- Do not introduce new requirements.
- Return corrected output for final review.

Input:
- Original Domain Agent output
- Review Agent findings
- Required fixes

Output:
## Fix Summary
## Applied Fixes
## Updated Output
## Remaining Risks
## Validation Checklist
```

Fix Agent는 Review Agent의 지적을 반영하되 범위를 확장하면 안 된다.

---

### [FAQ]

Q. Fix Agent가 뭐야?

A. Review Agent의 Findings를 반영해 산출물을 수정하는 Agent다.

Q. Fix Agent가 새 기능을 추가해도 돼?

A. 안 된다. 원래 Scope와 Review Findings 범위 안에서 수정해야 한다.

Q. Fix Agent Output에는 뭐가 있어야 해?

A. Fix Summary, Applied Fixes, Updated Output, Remaining Risks, Validation Checklist가 있으면 좋다.

---

# 4. Multi-Agent Prompt

## 4.1 Multi-Agent Prompt Definition

### [개념]

Multi-Agent Prompt는 여러 Agent가 협업하는 Workflow를 정의하는 Prompt다.

Multi-Agent Prompt는 Agent Role, Handoff, Shared Context, Review Loop, Stop Condition을 포함한다.

기본 Flow:

```text
User Request
→ PM Agent
→ Task Decomposition
→ Domain Agent
→ Review Agent
→ Fix Agent
→ Final Response
```

Multi-Agent Prompt의 목적은 복잡한 작업을 역할별로 분해하고 검증 가능한 Workflow로 처리하는 것이다.

---

### [핵심]

- PM Agent는 요청을 분해한다.
- Domain Agent는 전문 작업을 수행한다.
- Review Agent는 품질을 검증한다.
- Fix Agent는 리뷰 결과를 반영한다.
- Shared Context를 관리해야 한다.
- Agent 간 Handoff Schema를 고정해야 한다.
- Review / Fix Loop를 설계해야 한다.
- Stop Condition이 필요하다.
- Final Output은 사용자에게 필요한 형태로 정리한다.

---

### [실무]

Multi-Agent Prompt 예시:

```text
Workflow:
1. PM Agent analyzes user request.
2. PM Agent creates structured task brief.
3. Domain Agent performs the task using RAG documents.
4. Review Agent validates the output.
5. Fix Agent applies required fixes.
6. Final Response Agent returns concise final output.

Rules:
- Each Agent must stay within its responsibility.
- Each Handoff must follow the fixed schema.
- Missing information must be preserved across handoffs.
- Review loop stops when no High severity issues remain.
```

Multi-Agent Prompt는 Agent별 Prompt보다 Workflow 규칙이 중요하다.

---

### [FAQ]

Q. Multi-Agent Prompt가 뭐야?

A. 여러 Agent가 역할별로 협업하도록 Agent Role, Handoff, Shared Context, Review Loop, Stop Condition을 정의하는 Prompt다.

Q. Multi-Agent Workflow 기본 흐름은 뭐야?

A. User Request → PM Agent → Domain Agent → Review Agent → Fix Agent → Final Response 흐름이 기본이다.

Q. Multi-Agent Prompt에서 가장 중요한 것은 뭐야?

A. 역할 분리, Handoff Schema, Shared Context, Review Loop, Stop Condition이다.

---

# 5. Multi-Agent Workflow

## 5.1 Task Decomposition

### [개념]

Task Decomposition은 사용자 요청을 작은 작업 단위로 분해하는 과정이다.

PM Agent의 핵심 역할이다.

작업을 잘게 나누면 Domain Agent가 명확한 산출물을 만들 수 있다.

---

### [핵심]

- 사용자 요청을 분석한다.
- 기능 단위로 나눈다.
- 도메인별로 분리한다.
- 필요한 Context를 식별한다.
- Target Agent를 결정한다.
- Output 기준을 정한다.
- Review Criteria를 정의한다.
- Missing Information을 표시한다.

---

### [실무]

Task Decomposition 예시:

```md
## User Request

로그인 기능 구현해줘.

## Decomposed Tasks

1. Backend Agent
   - Auth API 구조 확인
   - Login Service 흐름 작성
   - JWT 발급 흐름 작성

2. Security Agent
   - Authentication Filter 검토
   - Token validation rule 검토

3. Review Agent
   - Transaction, Exception, Security Risk 검토

## Missing Information

- User Entity 미제공
- JWT Utility 코드 미제공
- SecurityConfig 미제공
```

Task Decomposition은 작업 범위와 누락 정보를 분명히 해야 한다.

---

### [FAQ]

Q. Task Decomposition이 뭐야?

A. 사용자 요청을 Agent가 처리 가능한 작은 작업 단위로 분해하는 과정이다.

Q. Task Decomposition은 누가 담당해?

A. 일반적으로 PM Agent가 담당한다.

Q. Task Decomposition이 왜 중요해?

A. 작업 범위가 명확해야 Domain Agent와 Review Agent가 안정적으로 작업할 수 있기 때문이다.

---

## 5.2 Routing

### [개념]

Routing은 분해된 작업을 적절한 Agent에게 전달하는 과정이다.

Routing은 작업 도메인, 필요한 전문성, 입력 Context를 기준으로 결정한다.

---

### [핵심]

- Backend 작업은 Backend Agent로 보낸다.
- Frontend 작업은 Frontend Agent로 보낸다.
- 인프라 작업은 DevOps Agent로 보낸다.
- Prompt 문서 작업은 Prompt Engineering Agent로 보낸다.
- 검증 작업은 Review Agent로 보낸다.
- 여러 도메인이 필요하면 순차 또는 병렬로 분리한다.
- Routing 기준이 없으면 Agent 책임이 겹친다.

---

### [실무]

Routing Rule 예시:

```text
Routing Rule:
- API, Service, Repository → Backend Agent
- Component, State, Routing, UI → Frontend Agent
- Docker, CI/CD, Server → DevOps Agent
- RAG, Prompt, Agent Design → AI Agent
- Validation, Review, Quality Check → Review Agent
```

Routing Output 예시:

```md
## Target Agent

Backend Agent

## Reason

The task requires Spring Boot Service design and Repository integration.

## Required Context

- Entity
- DTO
- Repository
- API rule
```

Routing은 PM Agent가 수행하고, Domain Agent는 받은 Task 범위 안에서 작업한다.

---

### [FAQ]

Q. Routing이 뭐야?

A. 분해된 작업을 적절한 Agent에게 전달하는 과정이다.

Q. Routing 기준은 뭐야?

A. 작업 도메인, 필요한 전문성, 입력 Context, 산출물 종류를 기준으로 결정한다.

Q. Routing이 잘못되면 어떻게 돼?

A. Agent가 자신의 전문 범위 밖 작업을 수행해 결과 품질이 낮아질 수 있다.

---

## 5.3 Shared Context

### [개념]

Shared Context는 여러 Agent가 공통으로 참고해야 하는 프로젝트 정보와 작업 상태다.

Shared Context는 Agent 간 일관성을 유지하는 데 필요하다.

---

### [핵심]

- 프로젝트 기술 스택을 포함한다.
- 아키텍처 규칙을 포함한다.
- 사용자 요구사항을 포함한다.
- 기존 결정사항을 포함한다.
- Missing Information을 포함한다.
- Assumptions를 포함한다.
- Review Findings를 포함할 수 있다.
- 오래된 Context와 최신 Context를 구분해야 한다.

---

### [실무]

Shared Context Schema:

```md
## Shared Context

### Project Stack

### Architecture Rules

### User Requirements

### Existing Decisions

### Retrieved Documents

### Assumptions

### Missing Information

### Review Findings
```

Shared Context 예시:

```md
## Shared Context

### Project Stack

- Java 21
- Spring Boot 3.x
- React
- MySQL

### Architecture Rules

- Controller → Service → Repository
- GlobalExceptionHandler handles exceptions
- API response uses ApiResponse<T>

### Missing Information

- UserRepository method signatures not provided
```

Shared Context가 없으면 Agent별 결과가 서로 충돌할 수 있다.

---

### [FAQ]

Q. Shared Context가 뭐야?

A. 여러 Agent가 공통으로 참고해야 하는 프로젝트 정보와 작업 상태다.

Q. Shared Context에는 뭐가 들어가야 해?

A. Project Stack, Architecture Rules, User Requirements, Existing Decisions, Assumptions, Missing Information이 들어가면 좋다.

Q. Shared Context가 없으면 어떤 문제가 생겨?

A. Agent마다 다른 전제를 사용해 결과가 충돌하거나 일관성이 깨질 수 있다.

---

## 5.4 Review / Fix Loop

### [개념]

Review / Fix Loop는 Domain Agent 산출물을 Review Agent가 검토하고 Fix Agent가 수정하는 반복 구조다.

Review / Fix Loop는 품질을 높이지만 무한 반복 방지 조건이 필요하다.

---

### [핵심]

- Domain Agent가 산출물을 만든다.
- Review Agent가 Findings를 생성한다.
- Fix Agent가 Required Fixes를 반영한다.
- 필요하면 Review Agent가 재검토한다.
- Severity 기준으로 반복 여부를 정한다.
- 반복 횟수를 제한한다.
- Missing Information이 있으면 루프를 중단할 수 있다.

---

### [실무]

Review / Fix Loop 예시:

```text
Domain Agent Output
→ Review Agent
→ Findings with Severity
→ Fix Agent
→ Updated Output
→ Review Agent Recheck
→ Final Output
```

Loop Rule 예시:

```text
Review / Fix Loop Rule:
- Fix all Critical and High severity issues.
- Medium issues may be documented if not fixed.
- Stop after maximum 2 iterations.
- Stop if missing information blocks validation.
```

Review / Fix Loop는 품질 향상용이며, 무한 반복 구조가 되면 안 된다.

---

### [FAQ]

Q. Review / Fix Loop가 뭐야?

A. Domain Agent 산출물을 Review Agent가 검토하고 Fix Agent가 수정하는 반복 구조다.

Q. Review / Fix Loop는 왜 필요해?

A. 산출물 품질을 높이고 오류, 누락, 형식 문제를 줄이기 위해 필요하다.

Q. Review / Fix Loop가 무한 반복되지 않게 하려면?

A. Severity 기준, 최대 반복 횟수, Missing Information 중단 조건을 둬야 한다.

---

## 5.5 Final Output

### [개념]

Final Output은 Multi-Agent Workflow의 최종 결과다.

Final Output은 내부 Handoff와 달리 사용자가 바로 사용할 수 있는 형태여야 한다.

---

### [핵심]

- 내부 Agent 로그를 모두 노출하지 않는다.
- 사용자에게 필요한 결과만 제공한다.
- 확정 정보와 추정을 구분한다.
- 남은 Missing Information을 표시한다.
- 코드, 문서, 계획, 리뷰 결과를 요청 형식에 맞게 정리한다.
- Final Output은 Workflow의 최종 산출물이다.

---

### [실무]

Final Output 구조 예시:

```md
## Final Result

## Key Decisions

## Output

## Remaining Assumptions

## Missing Information

## Next Validation
```

RAG 문서 제작 Final Output은 문서 자체만 제공하는 것이 좋다.

Code Review Final Output은 문제 / 원인 / 위험 / 수정 방향 중심이 좋다.

Code Generation Final Output은 구현 계획 / 코드 snippet / 검증 Checklist 중심이 좋다.

---

### [FAQ]

Q. Final Output은 뭐야?

A. Multi-Agent Workflow의 최종 결과로, 사용자가 바로 사용할 수 있는 형태의 산출물이다.

Q. Final Output에 모든 Agent 로그를 넣어야 해?

A. 아니다. 사용자가 필요한 결과 중심으로 정리하고 내부 Handoff는 불필요하면 제외한다.

Q. Final Output에도 Missing Information을 넣어야 해?

A. 남은 불확실성이 있으면 표시해야 한다.

---

# 6. Multi-Agent Prompt Patterns

## 6.1 PM to Backend Agent Pattern

### [개념]

PM to Backend Agent Pattern은 PM Agent가 Backend Agent에게 작업을 전달할 때 사용하는 Handoff 패턴이다.

---

### [핵심]

필수 포함:

- Task
- Backend Scope
- Project Context
- API Requirement
- DTO Requirement
- Service Requirement
- Repository Requirement
- Constraints
- Missing Information
- Expected Output
- Review Criteria

---

### [실무]

PM to Backend Agent Handoff:

```md
## Agent Handoff

### Source Agent

PM Agent

### Target Agent

Backend Agent

### Task

[Backend task]

### Backend Scope

- API
- DTO
- Service
- Repository

### Project Context

- Java 21
- Spring Boot 3.x
- Controller → Service → Repository

### Constraints

- Do not modify frontend code.
- Do not invent missing classes.
- Do not change existing API contract.

### Missing Information

- [Missing file or rule]

### Expected Output

- Implementation Summary
- API
- DTO
- Service
- Repository
- Validation Checklist

### Review Criteria

- Transaction Boundary
- Exception Handling
- DTO Responsibility
- API Response Consistency
```

이 패턴은 Backend Agent가 구현 범위를 명확히 이해하도록 만든다.

---

### [FAQ]

Q. PM to Backend Agent Pattern은 뭐야?

A. PM Agent가 Backend Agent에게 Backend 작업을 구조화해서 전달하는 Handoff 패턴이다.

Q. Backend Agent에게 넘길 때 필요한 정보는 뭐야?

A. Task, Backend Scope, Project Context, Constraints, Missing Information, Expected Output, Review Criteria가 필요하다.

---

## 6.2 Backend to Review Agent Pattern

### [개념]

Backend to Review Agent Pattern은 Backend Agent 산출물을 Review Agent에게 검증 요청할 때 사용하는 Handoff 패턴이다.

---

### [핵심]

필수 포함:

- Implementation Summary
- API
- DTO
- Service
- Repository
- Assumptions
- Missing Information
- Validation Checklist
- Review Request
- Review Criteria

---

### [실무]

Backend to Review Agent Handoff:

```md
## Agent Handoff

### Source Agent

Backend Agent

### Target Agent

Review Agent

### Implementation Summary

[Summary]

### Generated Output

#### API

#### DTO

#### Service

#### Repository

### Assumptions

[Assumptions]

### Missing Information

[Missing information]

### Review Criteria

- Architecture Consistency
- Transaction Boundary
- Exception Handling
- N+1 Query Risk
- DTO Responsibility
- API Response Consistency
```

Review Agent는 이 구조를 기준으로 문제, 위험, 수정 방향을 반환한다.

---

### [FAQ]

Q. Backend to Review Agent Pattern은 뭐야?

A. Backend Agent 산출물을 Review Agent가 검증할 수 있도록 구조화해 전달하는 Handoff 패턴이다.

Q. Review Agent에게 넘길 때 Assumptions가 필요한 이유는 뭐야?

A. 확정 정보와 가정을 구분해 잘못된 확정을 방지하기 위해 필요하다.

---

## 6.3 Review to Fix Agent Pattern

### [개념]

Review to Fix Agent Pattern은 Review Agent가 발견한 문제를 Fix Agent에게 전달하는 Handoff 패턴이다.

---

### [핵심]

필수 포함:

- Review Summary
- Findings
- Severity
- Required Fixes
- Preserve Scope
- Do Not Change
- Missing Information
- Recheck Criteria

---

### [실무]

Review to Fix Agent Handoff:

```md
## Agent Handoff

### Source Agent

Review Agent

### Target Agent

Fix Agent

### Review Summary

[Summary]

### Findings

#### 1. Issue

- Severity:
- Cause:
- Risk:
- Fix Direction:

### Required Fixes

[Fix list]

### Preserve Scope

- Original task scope
- Existing API contract
- Existing response structure

### Do Not Change

- Do not add new business rules.
- Do not modify unrelated layers.

### Recheck Criteria

- Critical / High issues resolved
- Output format preserved
- Missing Information preserved
```

Fix Agent는 Review Findings를 반영하되 범위를 확장하지 않는다.

---

### [FAQ]

Q. Review to Fix Agent Pattern은 뭐야?

A. Review Agent가 발견한 문제와 수정 요구사항을 Fix Agent에게 전달하는 Handoff 패턴이다.

Q. Fix Agent에게 Preserve Scope를 전달하는 이유는 뭐야?

A. 수정 중 원래 범위를 벗어나거나 새 요구사항을 임의 추가하는 것을 막기 위해 필요하다.

---

# 7. Agent Prompt Validation

## 7.1 Agent Prompt Checklist

### [개념]

Agent Prompt Checklist는 Agent Prompt가 실행 가능한 규칙을 충분히 포함하는지 검수하는 기준이다.

---

### [핵심]

검수 항목:

- Agent Role이 명확한가?
- Responsibility가 정의되었는가?
- Scope가 정의되었는가?
- Input Schema가 있는가?
- Output Schema가 있는가?
- Tool Use Rule이 있는가?
- Handoff Rule이 있는가?
- Stop Condition이 있는가?
- Failure Rule이 있는가?
- Missing Information Rule이 있는가?
- Assumption Rule이 있는가?
- Validation 기준이 있는가?
- Agent 간 책임이 중복되지 않는가?

---

### [실무]

Agent Prompt Checklist:

```md
### [Checklist]

- [ ] Agent Role이 명확한가?
- [ ] Responsibility가 구체적인가?
- [ ] Scope가 포함되었는가?
- [ ] Input이 구조화되었는가?
- [ ] Output이 고정 Schema를 따르는가?
- [ ] Tool 사용 기준이 있는가?
- [ ] Handoff 구조가 정의되었는가?
- [ ] Stop Condition이 있는가?
- [ ] Failure Rule이 있는가?
- [ ] Missing Information 처리 규칙이 있는가?
- [ ] Assumption 표시 규칙이 있는가?
- [ ] Review Agent가 검증 가능한가?
```

Agent Prompt는 생성 후 Review Agent 기준으로 검수해야 한다.

---

### [FAQ]

Q. Agent Prompt Checklist는 뭐야?

A. Agent Prompt가 역할, 책임, 입력, 출력, 도구, Handoff, 종료 조건을 충분히 포함하는지 검수하는 기준이다.

Q. Agent Prompt 검수에서 가장 중요한 항목은 뭐야?

A. Responsibility, Input, Output, Handoff Rule, Stop Condition, Failure Rule이다.

---

## 7.2 Multi-Agent Workflow Checklist

### [개념]

Multi-Agent Workflow Checklist는 여러 Agent가 협업하는 구조가 안정적인지 검수하는 기준이다.

---

### [핵심]

검수 항목:

- Agent Role이 분리되었는가?
- PM Agent가 Task Decomposition을 담당하는가?
- Domain Agent가 전문 작업을 담당하는가?
- Review Agent가 검증을 담당하는가?
- Fix Agent가 수정 반영을 담당하는가?
- Handoff Schema가 고정되었는가?
- Shared Context가 유지되는가?
- Missing Information이 전달되는가?
- Review / Fix Loop Stop Condition이 있는가?
- Final Output 구조가 명확한가?

---

### [실무]

Multi-Agent Workflow Checklist:

```md
### [Checklist]

- [ ] User Request가 PM Agent로 들어가는가?
- [ ] PM Agent가 작업을 분해하는가?
- [ ] 적절한 Domain Agent로 Routing되는가?
- [ ] Domain Agent Output이 구조화되어 있는가?
- [ ] Review Agent가 검증 가능한가?
- [ ] Fix Agent가 Review Findings만 반영하는가?
- [ ] Shared Context가 Agent 간 유지되는가?
- [ ] Missing Information이 손실되지 않는가?
- [ ] Review Loop 종료 조건이 있는가?
- [ ] Final Output이 사용자 요청 형식과 일치하는가?
```

Multi-Agent Workflow는 Agent 수보다 역할 분리와 Handoff 품질이 중요하다.

---

### [FAQ]

Q. Multi-Agent Workflow Checklist는 뭐야?

A. 여러 Agent가 역할별로 안정적으로 협업하는지 검수하는 기준이다.

Q. Multi-Agent Workflow에서 가장 중요한 것은 뭐야?

A. 역할 분리, Handoff Schema, Shared Context, Stop Condition이다.

---

# 8. Common Mistakes

## 8.1 Agent Prompt Mistakes

### [개념]

Agent Prompt Mistake는 Agent의 역할과 책임, 입력, 출력, 종료 조건이 불명확해 발생하는 문제다.

---

### [핵심]

자주 발생하는 실수:

- Role만 있고 Responsibility 없음
- Scope 없음
- Input Schema 없음
- Output Schema 없음
- Tool Use Rule 없음
- Handoff Rule 없음
- Stop Condition 없음
- Failure Rule 없음
- 여러 역할을 하나의 Agent에 혼합
- Missing Information 처리 없음
- Assumption 표시 없음

---

### [실무]

나쁜 Agent Prompt:

```text
You are a developer agent.
Do the task well.
```

개선 Agent Prompt:

```text
You are a Backend Agent.

Responsibility:
- Generate backend implementation plan.
- Follow PM Agent task brief.
- Use retrieved backend RAG documents.

Input:
- Task Brief
- Project Context
- Existing Code Context

Output:
## Implementation Summary
## API
## DTO
## Service
## Repository
## Missing Information
## Validation Checklist

Constraints:
- Do not modify frontend code.
- Do not invent missing project classes.

Stop Condition:
Stop after producing the requested backend output.
```

Agent Prompt는 명확한 실행 규칙이어야 한다.

---

### [FAQ]

Q. Agent Prompt에서 가장 흔한 실수는 뭐야?

A. Role만 지정하고 Responsibility, Input, Output, Stop Condition을 생략하는 것이다.

Q. Agent Prompt에 Output Schema가 없으면 어떻게 돼?

A. 후속 Agent가 처리하기 어려운 불안정한 출력이 생성될 수 있다.

---

## 8.2 Multi-Agent Prompt Mistakes

### [개념]

Multi-Agent Prompt Mistake는 Agent 간 책임과 Handoff가 불명확해 Workflow가 흔들리는 문제다.

---

### [핵심]

자주 발생하는 실수:

- PM Agent 없이 바로 모든 Agent 호출
- Agent 간 책임 중복
- Handoff Schema 없음
- Shared Context 없음
- Review Agent 없음
- Fix Loop 없음
- Stop Condition 없음
- Missing Information이 다음 Agent로 전달되지 않음
- Review Findings가 Fix에 반영되지 않음
- Final Output 기준 없음

---

### [실무]

나쁜 Multi-Agent Prompt:

```text
여러 Agent가 알아서 개발하고 검토해줘.
```

개선 Multi-Agent Prompt:

```text
Workflow:
1. PM Agent decomposes the user request.
2. Backend Agent generates backend output.
3. Review Agent validates backend output.
4. Fix Agent applies required fixes.
5. Final Response returns the corrected output.

Rules:
- Each Agent must stay within responsibility.
- Use fixed Handoff Schema.
- Preserve Missing Information.
- Stop after one review-fix cycle unless Critical issue remains.
```

Multi-Agent Workflow는 “여러 Agent를 많이 쓰는 것”이 아니라 “역할과 전달 구조를 명확히 하는 것”이 핵심이다.

---

### [FAQ]

Q. Multi-Agent Prompt에서 가장 흔한 실수는 뭐야?

A. Agent 간 책임 분리와 Handoff Schema 없이 여러 Agent를 동시에 사용하는 것이다.

Q. Review Agent 없이 Multi-Agent Workflow를 구성해도 돼?

A. 가능하지만 품질 검증이 약해진다. 실무에서는 Review Agent가 있는 구조가 안정적이다.

Q. Shared Context가 전달되지 않으면 어떻게 돼?

A. Agent마다 다른 전제를 사용해 결과가 충돌할 수 있다.

---

## 8.3 Handoff Mistakes

### [개념]

Handoff Mistake는 한 Agent가 다음 Agent에게 불완전하거나 불명확한 정보를 전달하는 문제다.

---

### [핵심]

자주 발생하는 실수:

- Task만 전달하고 Context 없음
- Constraints 누락
- Expected Output 누락
- Missing Information 누락
- Assumptions 누락
- Review Criteria 누락
- Source Agent / Target Agent 불명확
- 장문 설명만 있고 구조 없음

---

### [실무]

나쁜 Handoff:

```text
로그인 구현해줘.
```

개선 Handoff:

```md
## Agent Handoff

### Source Agent

PM Agent

### Target Agent

Backend Agent

### Task

Login Service 구현 계획 작성

### Context

- Spring Boot 3.x
- JWT 인증
- ApiResponse<T> 사용

### Constraints

- Controller 시그니처 변경 금지
- 없는 클래스명 생성 금지

### Expected Output

Service Flow, Code Snippet, Validation Checklist

### Missing Information

- UserRepository 시그니처 미제공
```

Handoff는 후속 Agent가 그대로 실행 가능한 수준이어야 한다.

---

### [FAQ]

Q. Handoff에서 가장 흔한 실수는 뭐야?

A. Task만 전달하고 Context, Constraints, Expected Output, Missing Information을 빼는 것이다.

Q. 좋은 Handoff의 기준은 뭐야?

A. 후속 Agent가 추가 추정 없이 바로 작업할 수 있는 구조화된 입력이어야 한다.

---

# 9. Best Practice

## 9.1 Agent Prompt Best Practice

### [개념]

Agent Prompt Best Practice는 Agent가 역할과 책임 범위 안에서 일관된 산출물을 생성하도록 설계하는 원칙이다.

---

### [핵심]

- Agent Role을 명확히 정의한다.
- Responsibility를 구체화한다.
- Scope를 제한한다.
- Input Schema를 제공한다.
- Output Schema를 고정한다.
- Tool Use Rule을 정의한다.
- Handoff Rule을 포함한다.
- Stop Condition을 포함한다.
- Failure Rule을 포함한다.
- Missing Information Rule을 포함한다.
- Assumption 표시 규칙을 포함한다.
- Review Agent가 검증 가능한 구조로 출력한다.

---

### [실무]

Agent Prompt Best Practice Template:

```text
You are a [Agent Role].

Responsibility:
- [Responsibility 1]
- [Responsibility 2]

Scope:
Included:
- [Allowed scope]

Excluded:
- [Forbidden scope]

Input:
- [Input 1]
- [Input 2]

Output:
[Fixed output schema]

Tool Use Rule:
- [Tool usage rule]

Constraints:
- [Must]
- [Must Not]

Handoff Rule:
- Return output in a structure that [Target Agent] can process.

Stop Condition:
- Stop when [completion condition].

Failure Rule:
- If information is missing, state what is missing and do not invent facts.
```

이 Template은 PM Agent, Backend Agent, Frontend Agent, Review Agent, DevOps Agent, AI/ML Agent에 적용 가능하다.

---

### [FAQ]

Q. Agent Prompt Best Practice는 뭐야?

A. Agent Role, Responsibility, Scope, Input, Output, Tool Use, Handoff, Stop Condition, Failure Rule을 명확히 정의하는 것이다.

Q. Agent Prompt에서 Output Schema를 고정해야 하는 이유는 뭐야?

A. 후속 Agent가 안정적으로 처리할 수 있도록 출력 구조를 일관되게 유지하기 위해서다.

---

## 9.2 Multi-Agent Prompt Best Practice

### [개념]

Multi-Agent Prompt Best Practice는 여러 Agent가 역할별로 협업하고 검증 가능한 Workflow를 수행하도록 설계하는 원칙이다.

---

### [핵심]

- User Request는 PM Agent가 먼저 분석한다.
- PM Agent는 Task Decomposition을 수행한다.
- Domain Agent는 전문 작업을 수행한다.
- Review Agent는 결과를 검증한다.
- Fix Agent는 Review Findings를 반영한다.
- Shared Context를 유지한다.
- Handoff Schema를 고정한다.
- Missing Information을 전달한다.
- Review / Fix Loop에 Stop Condition을 둔다.
- Final Output은 사용자 요청 형식에 맞춘다.

---

### [실무]

Multi-Agent Prompt Best Practice Template:

```text
Workflow:
1. PM Agent analyzes user request and creates Task Brief.
2. PM Agent routes the task to the correct Domain Agent.
3. Domain Agent generates structured output using RAG documents.
4. Review Agent validates the output.
5. Fix Agent applies required fixes.
6. Final Response returns the corrected result.

Global Rules:
- Use fixed Handoff Schema.
- Preserve Shared Context.
- Preserve Missing Information.
- Do not invent project-specific facts.
- Stop after defined review-fix iterations.
```

Multi-Agent 설계는 Agent 수보다 역할 분리, Context 유지, Handoff 품질이 중요하다.

---

### [FAQ]

Q. Multi-Agent Prompt Best Practice는 뭐야?

A. PM Agent, Domain Agent, Review Agent, Fix Agent의 역할을 분리하고 Handoff Schema와 Stop Condition을 명확히 하는 것이다.

Q. Multi-Agent Workflow에서 Agent 수가 많을수록 좋아?

A. 아니다. Agent 수보다 역할 분리와 Handoff 품질이 더 중요하다.

Q. Multi-Agent Workflow의 최종 목표는 뭐야?

A. 복잡한 작업을 역할별로 분해하고 검증된 최종 결과를 안정적으로 생성하는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Agent Prompt가 뭐야?
A. AI Agent의 역할, 책임, 입력, 출력, 도구 사용, 제약, Handoff, 종료 조건을 정의하는 Prompt다.

Q. Agent Prompt는 Role Prompt와 같아?
A. 아니다. Role Prompt는 관점과 책임을 정의하고, Agent Prompt는 입력, 출력, 도구, Handoff, 종료 조건까지 포함한다.

Q. Agent Prompt에서 가장 중요한 것은 뭐야?
A. Responsibility, Input, Output, Constraints, Handoff Rule, Stop Condition이다.

Q. Agent Prompt에 Stop Condition이 왜 필요해?
A. Agent가 무한 반복하거나 작업 범위를 넘어가지 않도록 하기 위해 필요하다.

Q. Agent Role은 뭐야?
A. Agent가 어떤 전문 역할과 관점으로 작업할지 정의하는 요소다.

Q. 하나의 Agent가 모든 역할을 하면 안 돼?
A. 권장하지 않는다. 역할이 넓으면 책임이 흐려지고 출력 품질이 낮아질 수 있다.

Q. Responsibility는 뭐야?
A. Agent가 반드시 수행해야 하는 책임과 담당 작업이다.

Q. Agent Input은 뭐야?
A. Agent가 작업을 수행하기 위해 받는 Task, Context, Code, Constraints, Retrieved Context 같은 입력 자료다.

Q. Agent Output은 뭐야?
A. Agent가 작업 후 반환하는 구조화된 산출물이다.

Q. Tool Use Rule이 뭐야?
A. Agent가 도구를 언제, 어떤 기준으로 사용할지 정의하는 규칙이다.

Q. Handoff Rule이 뭐야?
A. 한 Agent가 다른 Agent에게 작업을 넘길 때 사용하는 구조화된 전달 규칙이다.

Q. Handoff에는 뭐가 들어가야 해?
A. Source Agent, Target Agent, Task, Context, Constraints, Expected Output, Missing Information, Review Criteria가 들어가면 좋다.

Q. Stop Condition이 뭐야?
A. Agent가 언제 작업을 종료해야 하는지 정의하는 규칙이다.

Q. Failure Rule이 뭐야?
A. Agent가 정보 부족, Tool 실패, Context 부족, 범위 초과 상황에서 어떻게 행동할지 정의하는 규칙이다.

Q. PM Agent가 뭐야?
A. 사용자 요청을 분석하고 작업을 분해해 적절한 Domain Agent에게 전달하는 Agent다.

Q. PM Agent의 핵심 산출물은 뭐야?
A. Task Brief, Target Agent, Requirements, Context, Constraints, Expected Output, Review Criteria다.

Q. Domain Agent가 뭐야?
A. Backend, Frontend, DevOps, AI 같은 특정 기술 도메인의 작업을 수행하는 Agent다.

Q. Review Agent가 뭐야?
A. Domain Agent의 산출물이 규칙과 품질 기준을 만족하는지 검증하는 Agent다.

Q. Fix Agent가 뭐야?
A. Review Agent의 Findings를 반영해 산출물을 수정하는 Agent다.

Q. Multi-Agent Prompt가 뭐야?
A. 여러 Agent가 역할별로 협업하도록 Agent Role, Handoff, Shared Context, Review Loop, Stop Condition을 정의하는 Prompt다.

Q. Multi-Agent Workflow 기본 흐름은 뭐야?
A. User Request → PM Agent → Domain Agent → Review Agent → Fix Agent → Final Response 흐름이 기본이다.

Q. Task Decomposition이 뭐야?
A. 사용자 요청을 Agent가 처리 가능한 작은 작업 단위로 분해하는 과정이다.

Q. Routing이 뭐야?
A. 분해된 작업을 적절한 Agent에게 전달하는 과정이다.

Q. Shared Context가 뭐야?
A. 여러 Agent가 공통으로 참고해야 하는 프로젝트 정보와 작업 상태다.

Q. Review / Fix Loop가 뭐야?
A. Domain Agent 산출물을 Review Agent가 검토하고 Fix Agent가 수정하는 반복 구조다.

Q. Final Output은 뭐야?
A. Multi-Agent Workflow의 최종 결과로, 사용자가 바로 사용할 수 있는 형태의 산출물이다.

Q. PM to Backend Agent Pattern은 뭐야?
A. PM Agent가 Backend Agent에게 Backend 작업을 구조화해서 전달하는 Handoff 패턴이다.

Q. Backend to Review Agent Pattern은 뭐야?
A. Backend Agent 산출물을 Review Agent가 검증할 수 있도록 구조화해 전달하는 Handoff 패턴이다.

Q. Review to Fix Agent Pattern은 뭐야?
A. Review Agent가 발견한 문제와 수정 요구사항을 Fix Agent에게 전달하는 Handoff 패턴이다.

Q. Agent Prompt Checklist는 뭐야?
A. Agent Prompt가 역할, 책임, 입력, 출력, 도구, Handoff, 종료 조건을 충분히 포함하는지 검수하는 기준이다.

Q. Multi-Agent Workflow Checklist는 뭐야?
A. 여러 Agent가 역할별로 안정적으로 협업하는지 검수하는 기준이다.

Q. Agent Prompt에서 가장 흔한 실수는 뭐야?
A. Role만 지정하고 Responsibility, Input, Output, Stop Condition을 생략하는 것이다.

Q. Multi-Agent Prompt에서 가장 흔한 실수는 뭐야?
A. Agent 간 책임 분리와 Handoff Schema 없이 여러 Agent를 동시에 사용하는 것이다.

Q. Handoff에서 가장 흔한 실수는 뭐야?
A. Task만 전달하고 Context, Constraints, Expected Output, Missing Information을 빼는 것이다.

Q. Agent Prompt Best Practice는 뭐야?
A. Agent Role, Responsibility, Scope, Input, Output, Tool Use, Handoff, Stop Condition, Failure Rule을 명확히 정의하는 것이다.

Q. Multi-Agent Prompt Best Practice는 뭐야?
A. PM Agent, Domain Agent, Review Agent, Fix Agent의 역할을 분리하고 Handoff Schema와 Stop Condition을 명확히 하는 것이다.
