# Prompt Engineering Part09 Prompt Template, Prompt Iteration, Troubleshooting

---

# 1. Prompt Template

## 1.1 Prompt Template Definition

### [개념]

Prompt Template은 반복 작업을 일정한 품질과 형식으로 수행하기 위해 고정 구조와 동적 입력을 분리한 Prompt 형식이다.

Prompt Template은 매번 새 Prompt를 작성하는 방식이 아니다.

고정 규칙은 유지하고, 작업마다 바뀌는 값은 Placeholder로 주입한다.

기본 구조:

```text
Role
→ Task
→ Context
→ Constraints
→ Output Format
→ Failure Rule
→ Validation
```

Prompt Template의 목적은 반복 작업의 품질, 출력 형식, Agent Handoff, 검수 기준을 안정화하는 것이다.

---

### [핵심]

- Prompt Template은 반복 작업을 표준화한다.
- 고정 Instruction과 동적 Context를 분리한다.
- Placeholder를 명확히 정의한다.
- Output Format을 고정한다.
- Missing Information Rule을 포함한다.
- Agent Workflow에서는 Handoff Schema와 연결된다.
- Template은 재사용 가능해야 한다.
- Template이 너무 복잡하면 유지보수가 어려워진다.

---

### [실무]

2026 실무 기준 Prompt Template은 RAG Answer, Code Review, Code Generation, Agent Handoff, Document Generation에 사용한다.

기본 Prompt Template:

```text
You are a {agent_role}.

Task:
{task}

Context:
{context}

Constraints:
{constraints}

Output Format:
{output_format}

Failure Rule:
If required information is missing, state what is missing and do not invent facts.

Validation:
Before final output, check accuracy, format compliance, groundedness, and missing information.
```

Prompt Template은 `{agent_role}`, `{task}`, `{context}` 같은 Placeholder를 사용해 반복 작업에 재사용한다.

---

### [FAQ]

Q. Prompt Template이 뭐야?

A. 반복 작업을 일정한 품질과 형식으로 수행하기 위해 고정 구조와 동적 입력을 분리한 Prompt 형식이다.

Q. Prompt Template은 왜 필요해?

A. 반복 작업의 출력 품질, 형식, 검수 기준을 안정화하기 위해 필요하다.

Q. Prompt Template에는 뭐가 들어가야 해?

A. Role, Task, Context, Constraints, Output Format, Failure Rule, Validation이 들어가면 좋다.

Q. Prompt Template과 일반 Prompt는 뭐가 달라?

A. 일반 Prompt는 일회성 지시이고, Prompt Template은 반복 작업에 재사용 가능한 구조다.

---

# 2. Prompt Template Components

## 2.1 Placeholder

### [개념]

Placeholder는 Prompt Template에서 작업마다 바뀌는 값을 넣는 자리다.

Placeholder는 `{task}`, `{context}`, `{output_format}`처럼 명확한 이름으로 작성한다.

Placeholder가 모호하면 Template 재사용성이 낮아진다.

---

### [핵심]

- Placeholder는 동적 입력 위치다.
- 이름은 명확해야 한다.
- 역할과 의미를 구분해야 한다.
- 누락 여부를 검증해야 한다.
- 너무 많은 Placeholder는 Template을 복잡하게 만든다.
- Placeholder 값이 길어질 경우 Context Overload를 주의한다.

---

### [실무]

좋은 Placeholder 예시:

```text
{agent_role}
{task}
{project_context}
{retrieved_context}
{existing_code_context}
{constraints}
{output_format}
{failure_rule}
```

나쁜 Placeholder 예시:

```text
{data}
{thing}
{info}
{내용}
```

Prompt Template 예시:

```text
You are a {agent_role}.

Task:
{task}

Project Context:
{project_context}

Retrieved Context:
{retrieved_context}

Constraints:
{constraints}

Output Format:
{output_format}
```

Placeholder 이름은 후속 Agent나 자동화 시스템이 이해할 수 있어야 한다.

---

### [FAQ]

Q. Placeholder가 뭐야?

A. Prompt Template에서 작업마다 바뀌는 값을 넣는 자리다.

Q. Placeholder 이름은 어떻게 정해야 해?

A. `{task}`, `{project_context}`, `{output_format}`처럼 의미가 명확한 이름으로 정해야 한다.

Q. Placeholder가 많으면 좋아?

A. 아니다. 너무 많으면 Template이 복잡해지고 누락 가능성이 커진다.

---

## 2.2 Fixed Instruction

### [개념]

Fixed Instruction은 Prompt Template에서 항상 유지되는 고정 지시다.

Fixed Instruction은 Agent Role, 품질 기준, 금지사항, 출력 규칙, Failure Rule처럼 반복 적용되는 규칙을 포함한다.

---

### [핵심]

- Fixed Instruction은 반복 적용 규칙이다.
- 자주 바뀌지 않는 규칙만 넣는다.
- System Prompt와 중복되지 않게 관리한다.
- RAG Agent는 Grounding Rule을 포함한다.
- Code Agent는 Missing Information Rule을 포함한다.
- Output Format 고정 규칙을 포함할 수 있다.

---

### [실무]

Fixed Instruction 예시:

```text
Rules:
- Use provided context first.
- Do not invent project-specific facts.
- Mark assumptions clearly.
- State missing information when context is insufficient.
- Follow the requested output format.
```

RAG Document Fixed Instruction 예시:

```text
Rules:
- Apply MASTER_RAG_RULES.
- Apply DOMAIN_RULES.
- Optimize for retrieval.
- Include [개념], [핵심], [실무], [FAQ].
- Include Retrieval Queries.
```

Fixed Instruction에는 반복되는 핵심 규칙만 포함한다.

일회성 작업 조건은 Placeholder로 분리한다.

---

### [FAQ]

Q. Fixed Instruction이 뭐야?

A. Prompt Template에서 항상 유지되는 고정 지시다.

Q. Fixed Instruction에는 무엇을 넣어야 해?

A. 반복 적용되는 품질 기준, 금지사항, 출력 규칙, Failure Rule을 넣는다.

Q. 일회성 작업도 Fixed Instruction에 넣어야 해?

A. 아니다. 일회성 작업은 Placeholder나 User Prompt에 넣는 것이 좋다.

---

## 2.3 Dynamic Context

### [개념]

Dynamic Context는 작업마다 바뀌는 Context다.

Dynamic Context에는 사용자 요청, 코드, 검색 문서, 프로젝트 상황, 에러 로그, 요구사항이 들어갈 수 있다.

---

### [핵심]

- Dynamic Context는 작업별 입력이다.
- Task와 직접 관련된 Context만 넣는다.
- RAG 검색 결과는 Dynamic Context가 될 수 있다.
- 코드 리뷰에서는 제공된 코드가 Dynamic Context다.
- 디버깅에서는 로그와 재현 절차가 Dynamic Context다.
- Dynamic Context가 길어지면 핵심 정보가 흐려질 수 있다.

---

### [실무]

Dynamic Context 예시:

```text
Dynamic Context:
- User request
- Retrieved Context
- Existing Code Context
- Error Message
- Stack Trace
- Business Rule
- Recent Change
```

Template 내 Dynamic Context 사용 예시:

```text
Task:
{task}

Retrieved Context:
{retrieved_context}

Existing Code Context:
{existing_code_context}

Error Log:
{error_log}
```

Dynamic Context는 관련성 기준으로 선별해야 한다.

모든 정보를 넣는 것보다 작업에 필요한 정보를 넣는 것이 중요하다.

---

### [FAQ]

Q. Dynamic Context가 뭐야?

A. 작업마다 바뀌는 사용자 요청, 코드, 검색 문서, 로그, 요구사항 같은 입력 정보다.

Q. Dynamic Context는 많을수록 좋아?

A. 아니다. 작업과 직접 관련 있는 정확한 Context가 중요하다.

Q. RAG 검색 결과도 Dynamic Context야?

A. 그렇다. 검색된 Chunk는 작업마다 달라지는 Retrieved Context다.

---

## 2.4 Output Schema

### [개념]

Output Schema는 Prompt Template이 생성할 결과의 구조다.

Output Schema는 Markdown 섹션, JSON 필드, Checklist 항목, Handoff Schema로 정의할 수 있다.

---

### [핵심]

- Output Schema는 출력 안정성을 높인다.
- 필수 섹션을 고정한다.
- 필드명을 통일한다.
- 후속 Agent가 처리 가능한 구조로 작성한다.
- JSON은 Required Field를 명확히 한다.
- Markdown은 Header 계층을 고정한다.
- Output Schema가 흔들리면 Workflow가 불안정해진다.

---

### [실무]

Markdown Output Schema 예시:

```md
## Summary

## Findings

## Missing Information

## Fix Direction

## Validation Checklist
```

Agent Handoff Schema 예시:

```md
## Agent Handoff

### Source Agent

### Target Agent

### Task

### Context

### Constraints

### Expected Output

### Missing Information

### Review Criteria
```

JSON Output Schema 예시:

```json
{
  "status": "completed",
  "summary": "",
  "findings": [],
  "missingInformation": [],
  "requiresFollowUp": false
}
```

Output Schema는 반복 작업에서 가장 중요한 안정화 장치다.

---

### [FAQ]

Q. Output Schema가 뭐야?

A. Prompt Template이 생성할 결과의 고정 구조다.

Q. Output Schema는 왜 중요해?

A. 출력 형식을 안정화하고 후속 Agent나 자동화 시스템이 처리하기 쉽게 만들기 때문이다.

Q. Markdown과 JSON 중 뭐가 좋아?

A. 사람이 읽는 결과는 Markdown이 좋고, 자동 처리와 Tool 연계는 JSON이 좋다.

---

# 3. Prompt Template Types

## 3.1 RAG Answer Template

### [개념]

RAG Answer Template은 검색된 문서를 근거로 답변하는 반복 작업용 Template이다.

핵심은 Retrieved Context 우선, Missing Information 표시, Assumption 분리다.

---

### [핵심]

- Retrieved Context를 우선 사용한다.
- 문서에 없는 내용은 지어내지 않는다.
- Confirmed Facts를 분리한다.
- Assumptions를 분리한다.
- Missing Information을 표시한다.
- 출력 형식을 고정한다.
- Source Priority를 포함한다.

---

### [실무]

RAG Answer Template:

```text
You are a RAG Answer Agent.

Task:
{user_question}

Retrieved Context:
{retrieved_context}

Source Priority:
1. Retrieved Context
2. User-provided Context
3. General technical knowledge

Rules:
- Use retrieved context first.
- Do not invent project-specific facts.
- If context is insufficient, state missing information.
- Mark assumptions clearly.

Output Format:
## Answer
## Confirmed by Context
## Assumptions
## Missing Information
```

이 Template은 RAG QA, 문서 기반 코드 리뷰, 프로젝트 문서 질의에 사용할 수 있다.

---

### [FAQ]

Q. RAG Answer Template은 뭐야?

A. 검색된 문서를 근거로 답변하도록 고정한 반복 작업용 Prompt Template이다.

Q. RAG Answer Template에서 가장 중요한 규칙은 뭐야?

A. Retrieved Context를 우선 사용하고 문서에 없는 내용은 지어내지 않는 것이다.

Q. RAG Answer Template에는 Missing Information이 필요해?

A. 필요하다. 검색 문서가 부족한 경우 이를 명확히 표시해야 한다.

---

## 3.2 Code Review Template

### [개념]

Code Review Template은 코드 리뷰 결과를 일정한 기준과 형식으로 생성하기 위한 Prompt Template이다.

Code Review Template은 검토 기준과 Finding 구조를 고정한다.

---

### [핵심]

- Review Target을 명확히 한다.
- Review Criteria를 고정한다.
- Severity를 포함한다.
- Problem, Cause, Risk, Fix Direction을 분리한다.
- 보이는 코드만 확정적으로 리뷰한다.
- Missing Information을 표시한다.
- 취향과 결함을 구분한다.

---

### [실무]

Code Review Template:

```text
You are a {domain} Review Agent.

Task:
Review {review_target}.

Context:
{project_context}

Code:
{code_context}

Review Criteria:
{review_criteria}

Rules:
- Review only visible code.
- Do not claim unseen files are correct or incorrect.
- Separate confirmed issues and possible risks.
- Separate defects and style preferences.

Output Format:
## Review Summary

## Findings

### 1. Problem

- Severity:
- Cause:
- Risk:
- Fix Direction:
- Evidence:

## Missing Information

## Checklist
```

이 Template은 Backend Review, Frontend Review, Prompt Review, RAG Document Review에 변형 적용할 수 있다.

---

### [FAQ]

Q. Code Review Template은 뭐야?

A. 코드 리뷰 결과를 일정한 기준과 형식으로 생성하기 위한 Prompt Template이다.

Q. Code Review Template에서 가장 중요한 출력 구조는 뭐야?

A. Problem, Severity, Cause, Risk, Fix Direction, Evidence 구조다.

Q. Code Review Template에 Missing Information이 필요한 이유는 뭐야?

A. 보이지 않는 코드나 부족한 Context를 확정하지 않도록 하기 위해 필요하다.

---

## 3.3 Code Generation Template

### [개념]

Code Generation Template은 프로젝트 규칙과 기존 코드에 맞는 코드를 생성하기 위한 Prompt Template이다.

Code Generation Template은 Stack, Architecture, Existing Code Context, Constraints를 포함해야 한다.

---

### [핵심]

- 기술 스택과 버전을 명시한다.
- Architecture Context를 제공한다.
- Existing Code Context를 제공한다.
- Error Handling Rule을 포함한다.
- Transaction Rule을 포함한다.
- 없는 클래스명, API 경로, DB 컬럼 생성을 금지한다.
- 코드 snippet 범위를 제한한다.
- Validation Checklist를 포함한다.

---

### [실무]

Code Generation Template:

```text
You are a {domain} Code Generation Agent.

Task:
{generation_task}

Stack:
{stack}

Architecture:
{architecture_context}

Existing Code Context:
{existing_code_context}

Constraints:
- Do not invent missing classes.
- Do not invent API paths.
- Do not change existing signatures unless requested.
- Follow project rules.
- Mark missing information.

Output Format:
## Missing Information
## Assumptions
## Implementation Plan
## Code Snippet
## Validation Checklist
```

이 Template은 Service, Controller, Repository, Frontend Component, Agent Workflow 코드 생성에 사용할 수 있다.

---

### [FAQ]

Q. Code Generation Template은 뭐야?

A. 프로젝트 규칙과 기존 코드에 맞는 코드를 생성하기 위한 Prompt Template이다.

Q. Code Generation Template에서 가장 중요한 Context는 뭐야?

A. 기술 스택, 아키텍처, 기존 Entity / DTO / Repository / Controller 정보다.

Q. Code Generation Template에서 반드시 금지해야 하는 것은 뭐야?

A. 없는 클래스명, API 경로, DB 컬럼, 비즈니스 규칙을 확정 코드처럼 생성하는 것이다.

---

## 3.4 Debugging Template

### [개념]

Debugging Template은 오류 분석을 위해 증상, 로그, 환경, 최근 변경, 재현 절차를 구조화하는 Prompt Template이다.

Debugging Template은 원인 후보와 확정 사실을 구분하도록 설계해야 한다.

---

### [핵심]

- Symptom을 포함한다.
- Error Message를 포함한다.
- Stack Trace를 포함한다.
- Environment를 포함한다.
- Recent Change를 포함한다.
- Reproduction Steps를 포함한다.
- Expected Result와 Actual Result를 구분한다.
- Likely Causes와 Confirmed Facts를 분리한다.
- Verification Steps를 포함한다.

---

### [실무]

Debugging Template:

```text
Task:
Debug {issue}.

Symptom:
{symptom}

Error Message:
{error_message}

Stack Trace:
{stack_trace}

Environment:
{environment}

Recent Change:
{recent_change}

Reproduction Steps:
{reproduction_steps}

Expected Result:
{expected_result}

Actual Result:
{actual_result}

Output Format:
## Confirmed Facts
## Likely Causes
## Most Probable Cause
## Fix Direction
## Verification Steps
## Missing Information
```

Debugging Template은 Backend, Frontend, RAG, DevOps 디버깅에 모두 적용 가능하다.

---

### [FAQ]

Q. Debugging Template은 뭐야?

A. 오류 분석에 필요한 증상, 로그, 환경, 최근 변경, 재현 절차를 구조화하는 Prompt Template이다.

Q. Debugging Template에서 가장 중요한 정보는 뭐야?

A. Error Message와 Stack Trace다.

Q. Debugging Template에서 원인 후보와 확정 사실을 왜 구분해?

A. 근거가 부족한 원인을 확정하지 않기 위해서다.

---

## 3.5 Agent Handoff Template

### [개념]

Agent Handoff Template은 한 Agent가 다른 Agent에게 작업을 전달할 때 사용하는 구조다.

Handoff Template은 Multi-Agent Workflow의 입력 품질을 안정화한다.

---

### [핵심]

- Source Agent를 명시한다.
- Target Agent를 명시한다.
- Task를 명시한다.
- Context를 포함한다.
- Constraints를 포함한다.
- Expected Output을 포함한다.
- Assumptions를 포함한다.
- Missing Information을 포함한다.
- Review Criteria를 포함한다.

---

### [실무]

Agent Handoff Template:

```md
## Agent Handoff

### Source Agent

{source_agent}

### Target Agent

{target_agent}

### Task

{task}

### Context

{context}

### Constraints

{constraints}

### Expected Output

{expected_output}

### Assumptions

{assumptions}

### Missing Information

{missing_information}

### Review Criteria

{review_criteria}
```

Agent Handoff Template은 PM Agent, Backend Agent, Review Agent, Fix Agent 사이에서 사용할 수 있다.

---

### [FAQ]

Q. Agent Handoff Template은 뭐야?

A. 한 Agent가 다른 Agent에게 작업을 전달할 때 사용하는 구조화된 Prompt Template이다.

Q. Handoff Template이 왜 필요해?

A. 후속 Agent가 추가 추정 없이 바로 작업할 수 있도록 입력 품질을 안정화하기 위해 필요하다.

Q. Handoff Template에는 뭐가 들어가야 해?

A. Source Agent, Target Agent, Task, Context, Constraints, Expected Output, Assumptions, Missing Information, Review Criteria가 들어가면 좋다.

---

# 4. Prompt Iteration

## 4.1 Prompt Iteration Definition

### [개념]

Prompt Iteration은 Prompt 출력 결과를 평가하고 실패 유형을 반영해 Prompt를 반복 개선하는 과정이다.

Prompt는 한 번 작성하면 끝나는 고정 산출물이 아니다.

출력 실패를 확인하고 Constraint, Context, Output Format, Example을 보강해야 한다.

기본 Flow:

```text
Draft Prompt
→ Test Output
→ Identify Failure
→ Add Constraint / Example / Context
→ Retest
→ Final Template
```

---

### [핵심]

- Prompt Iteration은 Prompt 품질 개선 과정이다.
- 출력 결과를 기준으로 개선한다.
- 실패 유형을 분류한다.
- Format 실패는 Output Format을 강화한다.
- 내용 누락은 Context와 Checklist를 강화한다.
- Hallucination은 Grounding Rule과 Missing Information Rule을 강화한다.
- 반복 성공 후 Template으로 저장한다.

---

### [실무]

Prompt Iteration 예시:

```text
1. Draft Prompt 작성
2. Output 생성
3. Output Evaluation 수행
4. Failure Type 식별
5. Prompt 수정
6. 재실행
7. 반복 결과가 안정되면 Template화
```

Prompt Iteration은 특히 아래 작업에 중요하다.

- RAG Answer Prompt
- Code Review Prompt
- Code Generation Prompt
- JSON Output Prompt
- Agent Handoff Prompt
- RAG Document Generation Prompt

---

### [FAQ]

Q. Prompt Iteration이 뭐야?

A. Prompt 출력 결과를 평가하고 실패 유형을 반영해 Prompt를 반복 개선하는 과정이다.

Q. Prompt는 한 번 만들면 끝이야?

A. 아니다. 출력 결과를 평가하고 실패 유형을 반영해 반복 개선해야 한다.

Q. Prompt Iteration은 언제 필요해?

A. 출력 형식이 흔들리거나, 내용이 누락되거나, 없는 정보를 지어내거나, 반복 품질이 낮을 때 필요하다.

---

# 5. Prompt Iteration Process

## 5.1 Draft Prompt

### [개념]

Draft Prompt는 처음 작성한 초기 Prompt다.

Draft Prompt는 완성본이 아니라 테스트와 개선을 위한 시작점이다.

---

### [핵심]

- Draft Prompt는 빠르게 작성한다.
- 핵심 Task와 Output Format은 포함한다.
- 초기부터 모든 조건을 넣으려 하지 않는다.
- 테스트 가능한 수준으로 작성한다.
- 첫 출력 결과를 기준으로 개선한다.

---

### [실무]

Draft Prompt 예시:

```text
You are a Backend Review Agent.

Review the provided Service code.

Focus:
- Transaction boundary
- Exception handling
- DTO responsibility

Return:
- Problem
- Cause
- Risk
- Fix Direction
```

Draft Prompt는 단순하지만 검토 기준과 출력 구조를 포함해야 한다.

초기 출력 결과를 보고 부족한 Constraint와 Context를 추가한다.

---

### [FAQ]

Q. Draft Prompt가 뭐야?

A. 테스트와 개선을 위해 처음 작성하는 초기 Prompt다.

Q. Draft Prompt부터 완벽해야 해?

A. 아니다. 테스트 가능한 수준으로 작성하고 출력 결과를 기준으로 개선하면 된다.

Q. Draft Prompt에 꼭 들어가야 하는 것은 뭐야?

A. Task, 주요 기준, Output Format은 들어가야 한다.

---

## 5.2 Test Output

### [개념]

Test Output은 Draft Prompt로 생성한 실제 출력 결과다.

Prompt 개선은 Prompt 자체가 아니라 Test Output을 기준으로 수행한다.

---

### [핵심]

- Test Output을 기준으로 평가한다.
- 기대 형식과 비교한다.
- 내용 누락 여부를 확인한다.
- Hallucination 여부를 확인한다.
- Missing Information 표시 여부를 확인한다.
- 반복 실행 시 일관성을 확인할 수 있다.

---

### [실무]

Test Output 점검 항목:

```md
### [Checklist]

- [ ] 요청한 Task를 해결했는가?
- [ ] Output Format을 지켰는가?
- [ ] 필수 항목이 누락되지 않았는가?
- [ ] 문서 근거와 추정이 분리되었는가?
- [ ] Missing Information을 표시했는가?
- [ ] 불필요한 장문 설명이 없는가?
```

Test Output은 Prompt Evaluation과 연결된다.

실패 유형을 찾고 수정 방향을 결정하는 근거가 된다.

---

### [FAQ]

Q. Test Output이 뭐야?

A. Draft Prompt로 생성한 실제 출력 결과다.

Q. Prompt 개선은 무엇을 기준으로 해야 해?

A. Prompt 자체보다 Test Output의 실패 유형을 기준으로 해야 한다.

Q. Test Output은 한 번만 보면 돼?

A. 반복 품질이 중요한 Prompt는 여러 번 확인해 출력 안정성을 봐야 한다.

---

## 5.3 Failure Type Identification

### [개념]

Failure Type Identification은 Test Output에서 어떤 실패가 발생했는지 분류하는 과정이다.

실패 유형을 알아야 Prompt를 정확히 수정할 수 있다.

---

### [핵심]

대표 실패 유형:

- Task Misunderstanding
- Context Missing
- Constraint Violation
- Format Failure
- Hallucination
- Missing Information Omission
- Output Too Long
- Output Too Generic
- Inconsistent Field Name
- Unsafe Assumption
- Agent Scope Creep

---

### [실무]

Failure Type 분류 예시:

```md
## Failure Types

### Format Failure

- 요청한 Markdown 섹션이 누락됨

### Hallucination

- 제공하지 않은 Repository 메서드명을 확정적으로 생성함

### Output Too Generic

- 프로젝트 Context를 반영하지 못하고 일반론으로 답변함

### Missing Information Omission

- 필요한 코드가 없는데 부족 정보를 표시하지 않음
```

실패 유형별 수정 방향:

```text
Format Failure → Output Schema 강화
Hallucination → Grounding Rule / Must Not Rule 강화
Output Too Generic → Project Context 추가
Missing Information Omission → Failure Rule 강화
```

Failure Type을 정확히 분류하면 Prompt 수정이 쉬워진다.

---

### [FAQ]

Q. Failure Type Identification이 뭐야?

A. Test Output에서 어떤 실패가 발생했는지 분류하는 과정이다.

Q. 실패 유형을 왜 분류해야 해?

A. 실패 원인에 따라 Prompt 수정 방향이 달라지기 때문이다.

Q. 출력 형식 실패는 어떻게 고쳐?

A. Output Schema, Fixed Section, Few-Shot Example을 강화해야 한다.

---

## 5.4 Prompt Revision

### [개념]

Prompt Revision은 실패 유형을 반영해 Prompt를 수정하는 단계다.

Prompt Revision은 무작정 지시를 늘리는 것이 아니라 실패 원인에 맞게 수정해야 한다.

---

### [핵심]

- Format 실패는 Output Format을 강화한다.
- 내용 누락은 Context와 Checklist를 강화한다.
- Hallucination은 Must Not Rule을 강화한다.
- 일반론은 Project Context를 추가한다.
- 출력이 길면 Output Limit을 추가한다.
- Agent 범위 초과는 Scope Constraint를 추가한다.
- 반복 실패는 Few-Shot Example을 추가한다.

---

### [실무]

Prompt Revision 예시:

실패:

```text
모델이 없는 Repository 메서드를 확정적으로 생성함
```

수정:

```text
Must Not:
- Do not invent Repository method names.
- If Repository code is not provided, list required methods as candidates, not confirmed project code.

Output:
## Missing Information
## Repository Method Candidates
```

실패:

```text
출력 형식이 매번 바뀜
```

수정:

```text
Use exactly these sections:
## Summary
## Findings
## Missing Information
## Fix Direction
## Checklist
```

Prompt Revision은 실패 원인을 직접 겨냥해야 한다.

---

### [FAQ]

Q. Prompt Revision이 뭐야?

A. 실패 유형을 반영해 Prompt의 Context, Constraint, Output Format, Example을 수정하는 단계다.

Q. Prompt가 실패하면 지시를 많이 추가하면 돼?

A. 아니다. 실패 원인에 맞는 규칙만 추가해야 한다.

Q. 반복적으로 형식이 깨지면 어떻게 수정해?

A. Fixed Output Schema와 Few-Shot Example을 추가해야 한다.

---

## 5.5 Retest

### [개념]

Retest는 수정한 Prompt를 다시 실행해 실패가 해결되었는지 확인하는 단계다.

Retest는 Prompt Iteration의 검증 단계다.

---

### [핵심]

- 수정 후 다시 출력한다.
- 이전 실패가 해결되었는지 확인한다.
- 새로운 실패가 생겼는지 확인한다.
- 반복 실행 시 안정성을 확인한다.
- 품질이 안정되면 Template으로 저장한다.
- 실패가 남으면 다시 Revision한다.

---

### [실무]

Retest Checklist:

```md
### [Checklist]

- [ ] 이전 Format Failure가 해결되었는가?
- [ ] Hallucination이 줄었는가?
- [ ] Missing Information이 표시되는가?
- [ ] 출력 길이가 적절한가?
- [ ] Field Name이 일관적인가?
- [ ] 후속 Agent가 처리 가능한가?
```

Retest는 Prompt가 실제 작업에서 안정적으로 동작하는지 확인하는 단계다.

---

### [FAQ]

Q. Retest가 뭐야?

A. 수정한 Prompt를 다시 실행해 실패가 해결되었는지 확인하는 단계다.

Q. Retest에서 무엇을 확인해?

A. 이전 실패 해결 여부, 새로운 실패 발생 여부, 반복 출력 안정성을 확인한다.

Q. Retest 후 문제가 없으면 어떻게 해?

A. 안정화된 Prompt를 Template으로 저장해 재사용한다.

---

# 6. Prompt Troubleshooting

## 6.1 답변이 너무 일반적임

### [개념]

답변이 너무 일반적인 문제는 Prompt에 Project Context, Domain Context, 구체적 Task, Review Criteria, Output Format이 부족할 때 발생한다.

---

### [핵심]

문제:

- 프로젝트 상황에 맞지 않음
- 일반적인 개념 설명만 나옴
- 실무 적용 방향이 부족함
- 구체적인 수정 방향이 없음

원인:

- Context 부족
- Task 불명확
- Role만 있고 기준 없음
- Output Format 없음
- Domain Rules 미적용

해결:

- Project Context 추가
- Domain Context 추가
- Review Criteria 추가
- Output Format 지정
- 예시 출력 추가

---

### [실무]

나쁜 Prompt:

```text
이 코드 괜찮아?
```

개선 Prompt:

```text
Spring Boot 3.x Service 코드를 리뷰해줘.

Project Context:
- Java 21
- Controller → Service → Repository
- GlobalExceptionHandler 사용

Review Criteria:
- Transaction Boundary
- N+1 Query Risk
- Exception Handling
- DTO Responsibility

Output:
문제 / 원인 / 위험 / 수정 방향 / Severity
```

답변이 일반적이면 Context와 판단 기준을 강화해야 한다.

---

### [FAQ]

Q. 답변이 너무 일반적이면 어떻게 해?

A. Project Context, Domain Context, Review Criteria, Output Format을 추가해야 한다.

Q. 왜 모델이 일반론으로 답해?

A. 프로젝트 상황과 구체적 판단 기준이 부족하기 때문이다.

Q. Role을 전문가로 지정하면 해결돼?

A. 일부 도움은 되지만, Context와 Task 기준이 없으면 여전히 일반론이 나올 수 있다.

---

## 6.2 출력 형식이 계속 깨짐

### [개념]

출력 형식이 깨지는 문제는 Output Format이 모호하거나 Schema가 복잡하거나 예시가 부족할 때 발생한다.

---

### [핵심]

문제:

- Markdown 섹션 누락
- JSON 형식 오류
- Field Name 불일치
- 불필요한 설명 섞임
- Checklist 구조 불안정

원인:

- Output Format 불명확
- Fixed Schema 없음
- Schema가 너무 복잡함
- Few-Shot Example 없음
- 부가 설명 금지 조건 없음

해결:

- Output Schema 단순화
- 필수 섹션 고정
- Few-Shot Example 추가
- “Return only valid JSON” 추가
- Field Name 통일

---

### [실무]

Markdown 형식 안정화 Prompt:

```text
Use exactly these sections:
## Summary
## Findings
## Missing Information
## Fix Direction
## Checklist

Do not add extra top-level sections.
```

JSON 형식 안정화 Prompt:

```text
Return only valid JSON.
Do not include Markdown.
Do not include explanation outside JSON.
Use double quotes.
Do not use trailing commas.
```

출력 형식이 흔들릴 때는 자유도를 줄여야 한다.

---

### [FAQ]

Q. 출력 형식이 계속 깨지면 어떻게 해?

A. Fixed Output Schema, Few-Shot Example, 부가 설명 금지 조건을 추가해야 한다.

Q. JSON 출력이 깨지면 어떻게 해?

A. Schema를 단순화하고 “Return only valid JSON” 제약을 추가해야 한다.

Q. Markdown 섹션이 누락되면 어떻게 해?

A. 필수 섹션을 정확히 지정하고 추가 섹션 금지 조건을 넣어야 한다.

---

## 6.3 없는 정보를 지어냄

### [개념]

없는 정보를 지어내는 문제는 Grounding Rule, Missing Information Rule, Assumption Rule, Must Not Rule이 부족할 때 발생한다.

---

### [핵심]

문제:

- 제공하지 않은 클래스명 생성
- 없는 API 경로 생성
- DB 컬럼 임의 생성
- 프로젝트 정책 확정
- 보이지 않는 코드 단정

원인:

- Missing Information Rule 없음
- Must Not Rule 없음
- Assumption 표시 없음
- RAG Context 우선 규칙 없음
- 프로젝트 고유 정보 제한 없음

해결:

- Grounding Rule 추가
- Missing Information Rule 추가
- Assumption Rule 추가
- Must Not Rule 추가
- 보이지 않는 코드 단정 금지

---

### [실무]

Hallucination 방지 Prompt:

```text
Use provided context first.
Do not invent project-specific facts.
If class, method, API path, database column, or policy is not provided, mark it as Missing Information.
If an assumption is necessary, place it under Assumptions.
Do not present assumptions as confirmed facts.
```

코드 생성에서는 특히 클래스명, 필드명, API 경로 생성을 제한해야 한다.

---

### [FAQ]

Q. 모델이 없는 정보를 지어내면 어떻게 해?

A. Grounding Rule, Missing Information Rule, Assumption Rule, Must Not Rule을 추가해야 한다.

Q. 클래스명이나 API 경로를 임의로 만들면 왜 문제야?

A. 실제 프로젝트와 맞지 않는 코드를 생성해 구현 오류를 유도할 수 있기 때문이다.

Q. 필요한 정보가 없으면 어떻게 답하게 해야 해?

A. Missing Information으로 표시하고, 필요한 경우 Assumption으로 분리하게 해야 한다.

---

## 6.4 답변이 너무 김

### [개념]

답변이 너무 긴 문제는 Output Limit, Priority, Format Constraint가 없을 때 발생한다.

LLM은 기준이 없으면 배경 설명과 일반론을 과도하게 포함할 수 있다.

---

### [핵심]

문제:

- 불필요한 배경 설명이 많음
- 핵심 결론이 늦게 나옴
- 코드보다 설명이 과도함
- Review 결과가 장황함
- RAG 문서 Chunk가 길어짐

원인:

- Output Limit 없음
- 핵심 우선순위 없음
- 장문 설명 금지 조건 없음
- Bullet / Checklist 형식 미지정
- 에세이형 답변 허용

해결:

- Output Limit 지정
- Bullet 형식 지정
- 핵심 항목 수 제한
- 장문 배경 설명 금지
- Summary → Details 구조 사용

---

### [실무]

출력 길이 제어 Prompt:

```text
Keep the answer concise.
Use bullet points.
Focus on the top 3 issues.
Avoid long background explanations.
Return only the final structured result.
```

RAG 문서 길이 제어 Prompt:

```text
Optimize for retrieval.
Avoid essay-style paragraphs.
Keep each chunk focused on one concept.
Use short explanations and strong FAQ coverage.
```

답변이 길면 출력 형식과 우선순위를 명확히 제한한다.

---

### [FAQ]

Q. 답변이 너무 길면 어떻게 해?

A. Output Limit, Bullet 형식, 핵심 항목 수 제한, 장문 설명 금지 조건을 추가해야 한다.

Q. RAG 문서에서 긴 설명은 왜 문제야?

A. Chunk 품질이 떨어지고 검색 결과가 불필요한 문맥을 포함할 수 있기 때문이다.

Q. 짧게 쓰면 정보가 부족해지지 않아?

A. 핵심 정보와 FAQ를 강화하면 짧아도 Retrieval 품질을 유지할 수 있다.

---

## 6.5 코드가 프로젝트와 맞지 않음

### [개념]

코드가 프로젝트와 맞지 않는 문제는 기술 스택, 버전, 기존 코드 Context, 프로젝트 규칙이 부족할 때 발생한다.

---

### [핵심]

문제:

- 다른 버전 코드 생성
- 없는 Entity 필드 사용
- 없는 Repository 메서드 사용
- 프로젝트 응답 규칙 미반영
- 예외 처리 구조 불일치
- Controller에 비즈니스 로직 생성

원인:

- Version Constraint 없음
- Existing Code Context 없음
- Architecture Context 없음
- Error Handling Rule 없음
- Transaction Rule 없음
- Missing Information Rule 없음

해결:

- 기술 스택과 버전 명시
- 기존 코드 제공
- Architecture Rule 추가
- 변경 금지 범위 지정
- Missing Information Rule 추가
- 코드 snippet 범위 제한

---

### [실무]

프로젝트 정합성 강화 Prompt:

```text
Stack:
- Java 21
- Spring Boot 3.x
- Spring Data JPA

Architecture:
- Controller → Service → Repository
- Controller returns ApiResponse<T>
- GlobalExceptionHandler handles exceptions

Constraints:
- Do not invent missing classes.
- Do not use fields not present in Entity.
- Do not change existing method signatures.
- Keep business logic in Service.
```

코드 생성은 기존 코드와 프로젝트 규칙을 제공해야 안정적이다.

---

### [FAQ]

Q. 코드가 프로젝트와 맞지 않으면 어떻게 해?

A. 기술 스택, 버전, 기존 코드 Context, Architecture Rule, Missing Information Rule을 추가해야 한다.

Q. 모델이 없는 Repository 메서드를 쓰면 어떻게 해?

A. Repository 코드가 없으면 확정 메서드로 쓰지 말고 Missing Information이나 후보로 표시하게 해야 한다.

Q. 프로젝트 응답 규칙은 어디에 넣어야 해?

A. Project Context와 Constraint에 모두 명시하는 것이 좋다.

---

# 7. Prompt Template Validation

## 7.1 Template Validation Checklist

### [개념]

Template Validation Checklist는 Prompt Template이 반복 작업에 사용할 수 있을 만큼 안정적인지 검수하는 기준이다.

---

### [핵심]

검수 항목:

- Placeholder가 명확한가?
- Fixed Instruction이 과도하지 않은가?
- Dynamic Context 위치가 분리되었는가?
- Output Schema가 고정되어 있는가?
- Failure Rule이 포함되었는가?
- Missing Information Rule이 포함되었는가?
- Assumption Rule이 포함되었는가?
- Format Compliance를 확인하는가?
- 후속 Agent가 처리 가능한 구조인가?
- 재사용 가능한가?

---

### [실무]

Template Validation Checklist:

```md
### [Checklist]

- [ ] Placeholder 이름이 명확한가?
- [ ] Placeholder 누락 시 실패 처리가 가능한가?
- [ ] 고정 규칙과 동적 입력이 분리되었는가?
- [ ] Output Schema가 명확한가?
- [ ] Missing Information Rule이 있는가?
- [ ] Assumption Rule이 있는가?
- [ ] Must Not Rule이 있는가?
- [ ] 형식 실패를 줄이는 예시가 있는가?
- [ ] 반복 실행 시 구조가 안정적인가?
- [ ] Agent Handoff에 사용할 수 있는가?
```

Template 검수 후 안정화된 Prompt만 반복 작업에 사용한다.

---

### [FAQ]

Q. Template Validation Checklist는 뭐야?

A. Prompt Template이 반복 작업에 사용할 수 있을 만큼 안정적인지 검수하는 기준이다.

Q. Template 검수에서 가장 중요한 항목은 뭐야?

A. Placeholder 명확성, Output Schema, Missing Information Rule, 재사용성이다.

Q. Template이 복잡하면 어떻게 해야 해?

A. Placeholder를 줄이고 고정 규칙과 동적 Context를 분리해야 한다.

---

## 7.2 Iteration Validation Checklist

### [개념]

Iteration Validation Checklist는 Prompt Iteration 이후 문제가 해결되었는지 확인하는 기준이다.

Prompt 수정 후에는 반드시 이전 실패가 해결되었는지 확인해야 한다.

---

### [핵심]

검수 항목:

- 이전 실패 유형이 해결되었는가?
- 새로운 실패가 생기지 않았는가?
- 출력 형식이 안정적인가?
- Hallucination이 줄었는가?
- Missing Information이 표시되는가?
- Assumption이 분리되는가?
- Field Name이 일관적인가?
- 후속 Agent가 처리 가능한가?

---

### [실무]

Iteration Validation Checklist:

```md
### [Checklist]

- [ ] Format Failure가 해결되었는가?
- [ ] Hallucination이 줄었는가?
- [ ] Missing Information이 표시되는가?
- [ ] Output이 너무 길거나 짧지 않은가?
- [ ] Field Name이 고정되었는가?
- [ ] Required Section이 모두 포함되었는가?
- [ ] 반복 실행 시 구조가 유지되는가?
- [ ] Review Agent가 검증 가능한가?
```

Iteration Validation은 Prompt Template 저장 전 마지막 검수 단계다.

---

### [FAQ]

Q. Iteration Validation Checklist는 뭐야?

A. Prompt 수정 후 이전 실패가 해결되었는지 확인하는 검수 기준이다.

Q. Prompt 수정 후 바로 Template으로 저장해도 돼?

A. 아니다. Retest와 Iteration Validation 후 안정화되면 저장하는 것이 좋다.

Q. 새로운 실패가 생기면 어떻게 해?

A. 실패 유형을 다시 분류하고 Prompt Revision을 반복해야 한다.

---

# 8. Common Mistakes

## 8.1 Prompt Template Mistakes

### [개념]

Prompt Template Mistake는 Template이 재사용 가능하지 않거나 Placeholder, Output Schema, Failure Rule이 불명확한 문제다.

---

### [핵심]

자주 발생하는 실수:

- Placeholder 이름이 모호함
- Placeholder가 너무 많음
- 고정 규칙과 동적 입력이 섞임
- Output Schema 없음
- Missing Information Rule 없음
- Assumption Rule 없음
- 특정 사례에 과도하게 묶임
- Template이 너무 길고 복잡함
- 후속 Agent가 처리하기 어려운 구조

---

### [실무]

나쁜 Template:

```text
너는 전문가야.
{내용}을 보고 잘 답해줘.
필요한 건 알아서 해.
```

개선 Template:

```text
You are a {agent_role}.

Task:
{task}

Context:
{context}

Constraints:
{constraints}

Output Format:
{output_format}

Failure Rule:
If information is missing, state what is missing and do not invent facts.
```

Template은 재사용 가능한 구조와 명확한 Placeholder를 가져야 한다.

---

### [FAQ]

Q. Prompt Template에서 가장 흔한 실수는 뭐야?

A. Placeholder가 모호하고 Output Schema와 Failure Rule이 없는 것이다.

Q. Template이 특정 사례에 너무 묶이면 왜 문제야?

A. 다른 작업에 재사용하기 어렵고 유지보수가 어려워진다.

Q. Template을 단순하게 만들어도 돼?

A. 가능하다. 단순하더라도 Task, Context, Constraints, Output Format, Failure Rule은 포함하는 것이 좋다.

---

## 8.2 Prompt Iteration Mistakes

### [개념]

Prompt Iteration Mistake는 출력 실패를 분석하지 않고 임의로 Prompt를 수정하는 문제다.

---

### [핵심]

자주 발생하는 실수:

- 실패 유형 분류 없이 수정
- 제약만 계속 추가
- Output Format 실패를 Context 추가로 해결하려 함
- Hallucination을 예시만으로 해결하려 함
- Retest 없이 Template 저장
- 반복 출력 안정성 확인 안 함
- 새로운 실패 발생 여부 확인 안 함

---

### [실무]

나쁜 Iteration:

```text
출력이 이상함
→ 지시를 더 많이 추가
→ 더 복잡해짐
→ 또 실패
```

개선 Iteration:

```text
출력이 이상함
→ Failure Type 분류
→ Format Failure 확인
→ Output Schema 강화
→ Retest
→ Template 저장
```

Prompt Iteration은 실패 원인에 맞는 수정이 핵심이다.

---

### [FAQ]

Q. Prompt Iteration에서 가장 흔한 실수는 뭐야?

A. 실패 유형을 분류하지 않고 제약을 무작정 추가하는 것이다.

Q. Prompt가 실패하면 어떻게 해야 해?

A. Test Output을 보고 Failure Type을 분류한 뒤 원인에 맞게 수정해야 한다.

Q. Retest 없이 Prompt를 저장해도 돼?

A. 권장하지 않는다. 수정 후 출력 안정성을 확인해야 한다.

---

## 8.3 Troubleshooting Mistakes

### [개념]

Troubleshooting Mistake는 문제 증상만 보고 원인을 확정하거나, 실패 원인을 Prompt 구조가 아닌 모델 문제로만 판단하는 실수다.

---

### [핵심]

자주 발생하는 실수:

- 증상만 보고 원인 확정
- Prompt Context 부족을 모델 문제로 오해
- Output Format 부재를 모델 문제로 오해
- RAG 검색 실패와 Prompt 실패를 구분하지 않음
- Missing Information Rule 누락을 간과
- 같은 실패를 반복하면서 Template 수정 안 함
- 검수 없이 결과를 그대로 사용

---

### [실무]

나쁜 Troubleshooting:

```text
모델이 멍청해서 답을 못함
```

개선 Troubleshooting:

```text
문제:
답변이 일반론으로 나옴

원인 후보:
- Project Context 부족
- Review Criteria 없음
- Output Format 없음

해결:
- Project Context 추가
- Review Criteria 추가
- Output Schema 지정
```

Prompt Troubleshooting은 증상, 원인, 해결을 분리해야 한다.

---

### [FAQ]

Q. Prompt Troubleshooting에서 가장 흔한 실수는 뭐야?

A. Prompt 구조 문제를 분석하지 않고 모델 문제로만 판단하는 것이다.

Q. RAG 검색 실패와 Prompt 실패는 어떻게 구분해?

A. 검색된 Chunk가 부적절하면 Retrieval 문제이고, Chunk는 있는데 답변이 지어내면 Prompt Grounding 문제다.

Q. 같은 실패가 반복되면 어떻게 해?

A. 실패 유형을 Template에 반영하고 Retest해야 한다.

---

# 9. Best Practice

## 9.1 Prompt Template Best Practice

### [개념]

Prompt Template Best Practice는 반복 가능한 작업을 안정적으로 수행하기 위해 고정 규칙, 동적 입력, 출력 Schema를 분리하는 원칙이다.

---

### [핵심]

- Placeholder 이름을 명확히 한다.
- Fixed Instruction과 Dynamic Context를 분리한다.
- Output Schema를 고정한다.
- Missing Information Rule을 포함한다.
- Assumption Rule을 포함한다.
- Must Not Rule을 포함한다.
- Template은 너무 길지 않게 유지한다.
- Few-Shot Example은 필요한 경우에만 넣는다.
- 후속 Agent가 처리 가능한 구조로 만든다.
- 안정화된 Template만 재사용한다.

---

### [실무]

Prompt Template Best Practice Template:

```text
You are a {agent_role}.

Task:
{task}

Context:
{context}

Constraints:
Must:
- {must_rule}

Must Not:
- {must_not_rule}

Output Format:
{output_schema}

Failure Rule:
If information is missing, state what is missing and do not invent facts.

Validation:
Check accuracy, completeness, format compliance, groundedness, and missing information before final output.
```

이 Template은 RAG Answer, Code Review, Code Generation, Agent Handoff에 공통 적용 가능하다.

---

### [FAQ]

Q. Prompt Template Best Practice는 뭐야?

A. Placeholder, Fixed Instruction, Dynamic Context, Output Schema, Failure Rule을 명확히 분리하는 것이다.

Q. Prompt Template에서 가장 중요한 것은 뭐야?

A. 명확한 Placeholder, 고정 Output Schema, Missing Information Rule이다.

Q. Template은 언제 저장해야 해?

A. Retest를 거쳐 반복 출력이 안정된 후 저장하는 것이 좋다.

---

## 9.2 Prompt Iteration Best Practice

### [개념]

Prompt Iteration Best Practice는 출력 실패를 유형별로 분석하고 원인에 맞게 Prompt를 수정하는 원칙이다.

---

### [핵심]

- Draft Prompt를 작성한다.
- Test Output을 생성한다.
- 실패 유형을 분류한다.
- 원인에 맞게 Prompt를 수정한다.
- Retest를 수행한다.
- 반복 출력 안정성을 확인한다.
- 안정화되면 Template으로 저장한다.
- 실패 기록을 남긴다.

---

### [실무]

Prompt Iteration Best Practice Flow:

```text
Draft Prompt
→ Test Output
→ Failure Type Classification
→ Prompt Revision
→ Retest
→ Stability Check
→ Template Save
```

실패 유형별 수정:

```text
Format Failure → Output Schema 강화
Hallucination → Grounding Rule 강화
Missing Information Omission → Failure Rule 강화
Output Too Generic → Context 강화
Output Too Long → Output Limit 강화
Scope Creep → Scope Constraint 강화
```

Prompt Iteration은 Prompt 품질을 운영 가능한 수준으로 끌어올리는 과정이다.

---

### [FAQ]

Q. Prompt Iteration Best Practice는 뭐야?

A. 출력 실패를 유형별로 분석하고 원인에 맞게 Prompt를 수정한 뒤 Retest하는 것이다.

Q. Prompt Iteration에서 가장 중요한 단계는 뭐야?

A. Failure Type Classification과 Retest다.

Q. Prompt Iteration 결과는 어떻게 관리해?

A. 안정화된 Prompt는 Template으로 저장하고 실패 유형은 개선 기록으로 남기는 것이 좋다.

---

## 9.3 Prompt Troubleshooting Best Practice

### [개념]

Prompt Troubleshooting Best Practice는 Prompt 실패를 증상, 원인, 해결로 분리해 개선하는 원칙이다.

---

### [핵심]

- 문제 증상을 명확히 기록한다.
- 가능한 원인을 분류한다.
- RAG 문제와 Prompt 문제를 구분한다.
- Format 문제와 Context 문제를 구분한다.
- Hallucination 문제는 Grounding 기준으로 본다.
- 해결책은 실패 원인에 맞게 적용한다.
- Retest로 해결 여부를 확인한다.

---

### [실무]

Prompt Troubleshooting Template:

```md
## Problem

[Observed issue]

## Possible Causes

- [Cause 1]
- [Cause 2]

## Fix Direction

- [Prompt change]
- [Context change]
- [Output schema change]

## Retest Checklist

- [ ] Previous failure resolved
- [ ] No new failure introduced
- [ ] Output format stable
```

Troubleshooting은 Prompt를 더 길게 만드는 작업이 아니라 실패 원인을 정확히 제거하는 작업이다.

---

### [FAQ]

Q. Prompt Troubleshooting Best Practice는 뭐야?

A. Prompt 실패를 증상, 원인, 해결로 분리하고 Retest로 개선 여부를 확인하는 것이다.

Q. Prompt 문제와 RAG 검색 문제는 어떻게 구분해?

A. 검색된 Chunk 자체가 부적절하면 Retrieval 문제이고, Chunk는 적절한데 답변이 틀리면 Prompt 문제일 가능성이 높다.

Q. Troubleshooting 후에는 뭘 해야 해?

A. 수정한 Prompt를 Retest하고 안정화되면 Template에 반영해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Prompt Template이 뭐야?
A. 반복 작업을 일정한 품질과 형식으로 수행하기 위해 고정 구조와 동적 입력을 분리한 Prompt 형식이다.

Q. Prompt Template은 왜 필요해?
A. 반복 작업의 출력 품질, 형식, 검수 기준을 안정화하기 위해 필요하다.

Q. Prompt Template에는 뭐가 들어가야 해?
A. Role, Task, Context, Constraints, Output Format, Failure Rule, Validation이 들어가면 좋다.

Q. Placeholder가 뭐야?
A. Prompt Template에서 작업마다 바뀌는 값을 넣는 자리다.

Q. Placeholder 이름은 어떻게 정해야 해?
A. `{task}`, `{project_context}`, `{output_format}`처럼 의미가 명확한 이름으로 정해야 한다.

Q. Fixed Instruction이 뭐야?
A. Prompt Template에서 항상 유지되는 고정 지시다.

Q. Dynamic Context가 뭐야?
A. 작업마다 바뀌는 사용자 요청, 코드, 검색 문서, 로그, 요구사항 같은 입력 정보다.

Q. Output Schema가 뭐야?
A. Prompt Template이 생성할 결과의 고정 구조다.

Q. RAG Answer Template은 뭐야?
A. 검색된 문서를 근거로 답변하도록 고정한 반복 작업용 Prompt Template이다.

Q. Code Review Template은 뭐야?
A. 코드 리뷰 결과를 일정한 기준과 형식으로 생성하기 위한 Prompt Template이다.

Q. Code Generation Template은 뭐야?
A. 프로젝트 규칙과 기존 코드에 맞는 코드를 생성하기 위한 Prompt Template이다.

Q. Debugging Template은 뭐야?
A. 오류 분석에 필요한 증상, 로그, 환경, 최근 변경, 재현 절차를 구조화하는 Prompt Template이다.

Q. Agent Handoff Template은 뭐야?
A. 한 Agent가 다른 Agent에게 작업을 전달할 때 사용하는 구조화된 Prompt Template이다.

Q. Prompt Iteration이 뭐야?
A. Prompt 출력 결과를 평가하고 실패 유형을 반영해 Prompt를 반복 개선하는 과정이다.

Q. Prompt는 한 번 만들면 끝이야?
A. 아니다. 출력 결과를 평가하고 실패 유형을 반영해 반복 개선해야 한다.

Q. Draft Prompt가 뭐야?
A. 테스트와 개선을 위해 처음 작성하는 초기 Prompt다.

Q. Test Output이 뭐야?
A. Draft Prompt로 생성한 실제 출력 결과다.

Q. Failure Type Identification이 뭐야?
A. Test Output에서 어떤 실패가 발생했는지 분류하는 과정이다.

Q. Prompt Revision이 뭐야?
A. 실패 유형을 반영해 Prompt의 Context, Constraint, Output Format, Example을 수정하는 단계다.

Q. Retest가 뭐야?
A. 수정한 Prompt를 다시 실행해 실패가 해결되었는지 확인하는 단계다.

Q. 답변이 너무 일반적이면 어떻게 해?
A. Project Context, Domain Context, Review Criteria, Output Format을 추가해야 한다.

Q. 출력 형식이 계속 깨지면 어떻게 해?
A. Fixed Output Schema, Few-Shot Example, 부가 설명 금지 조건을 추가해야 한다.

Q. 모델이 없는 정보를 지어내면 어떻게 해?
A. Grounding Rule, Missing Information Rule, Assumption Rule, Must Not Rule을 추가해야 한다.

Q. 답변이 너무 길면 어떻게 해?
A. Output Limit, Bullet 형식, 핵심 항목 수 제한, 장문 설명 금지 조건을 추가해야 한다.

Q. 코드가 프로젝트와 맞지 않으면 어떻게 해?
A. 기술 스택, 버전, 기존 코드 Context, Architecture Rule, Missing Information Rule을 추가해야 한다.

Q. Template Validation Checklist는 뭐야?
A. Prompt Template이 반복 작업에 사용할 수 있을 만큼 안정적인지 검수하는 기준이다.

Q. Iteration Validation Checklist는 뭐야?
A. Prompt 수정 후 이전 실패가 해결되었는지 확인하는 검수 기준이다.

Q. Prompt Template에서 가장 흔한 실수는 뭐야?
A. Placeholder가 모호하고 Output Schema와 Failure Rule이 없는 것이다.

Q. Prompt Iteration에서 가장 흔한 실수는 뭐야?
A. 실패 유형을 분류하지 않고 제약을 무작정 추가하는 것이다.

Q. Prompt Troubleshooting에서 가장 흔한 실수는 뭐야?
A. Prompt 구조 문제를 분석하지 않고 모델 문제로만 판단하는 것이다.

Q. Prompt Template Best Practice는 뭐야?
A. Placeholder, Fixed Instruction, Dynamic Context, Output Schema, Failure Rule을 명확히 분리하는 것이다.

Q. Prompt Iteration Best Practice는 뭐야?
A. 출력 실패를 유형별로 분석하고 원인에 맞게 Prompt를 수정한 뒤 Retest하는 것이다.

Q. Prompt Troubleshooting Best Practice는 뭐야?
A. Prompt 실패를 증상, 원인, 해결로 분리하고 Retest로 개선 여부를 확인하는 것이다.
