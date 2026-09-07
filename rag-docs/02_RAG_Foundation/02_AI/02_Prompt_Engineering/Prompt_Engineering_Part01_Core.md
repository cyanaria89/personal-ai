# Prompt Engineering Part01 Core

---

# 1. Prompt Engineering Core

## 1.1 Prompt Engineering Definition

### [개념]

Prompt Engineering은 LLM이 원하는 작업을 정확하게 수행하도록 입력 지시를 설계하는 기술이다.

Prompt는 단순 질문이 아니라 LLM에게 전달되는 작업 지시서다.

Prompt Engineering은 아래 요소를 명확히 정의한다.

```text
Goal
→ Role
→ Context
→ Task
→ Constraints
→ Output Format
→ Validation
```

Prompt Engineering의 목적은 LLM 답변을 더 정확하고, 일관되고, 재사용 가능하게 만드는 것이다.

---

### [핵심]

- Prompt Engineering은 LLM 작업 지시 설계다.
- 좋은 Prompt는 목표, 맥락, 작업, 제약, 출력 형식이 명확하다.
- Prompt는 답변 품질, 코드 생성 품질, 리뷰 품질에 직접 영향을 준다.
- Agent Workflow에서는 Prompt가 Agent의 역할과 행동 규칙이 된다.
- RAG 환경에서는 Prompt가 검색 문서를 어떻게 사용할지 결정한다.
- Prompt Engineering은 Hallucination 감소와 Structured Output 안정화에 중요하다.

---

### [실무]

2026 실무 기준 Prompt Engineering은 단순히 “질문을 잘하는 기술”이 아니다.

AI Agent, RAG, Tool Calling, Multi-Agent Workflow에서 Prompt는 시스템 동작 규칙에 가깝다.

실무 Prompt는 보통 아래 구조를 가진다.

```text
Role:
You are a [Agent Role].

Task:
Perform [Specific Task].

Context:
Use [Provided Context / Retrieved Documents].

Constraints:
Follow [Rules / Limits / Project Standards].

Output Format:
Return [Markdown / JSON / Checklist / Code Snippet].

Validation:
Check [Accuracy / Missing Information / Format Compliance].
```

Backend Agent, Frontend Agent, Review Agent, PM Agent는 각자 다른 Prompt를 가져야 한다.

하나의 Prompt에 모든 역할을 넣으면 책임 경계가 흐려지고 결과 품질이 낮아진다.

---

### [FAQ]

Q. Prompt Engineering이 뭐야?

A. LLM이 원하는 작업을 정확히 수행하도록 목표, 맥락, 제약, 출력 형식을 설계하는 작업이다.

Q. Prompt는 그냥 질문이야?

A. 아니다. 실무에서는 Prompt가 LLM에게 전달하는 작업 지시서이자 행동 규칙이다.

Q. 좋은 Prompt의 핵심은 뭐야?

A. Goal, Role, Context, Task, Constraints, Output Format, Validation이 명확해야 한다.

Q. Prompt Engineering은 왜 중요해?

A. 답변 정확도, 코드 생성 품질, 리뷰 품질, Agent Workflow 안정성에 직접 영향을 주기 때문이다.

---

# 2. Prompt Structure

## 2.1 Core Prompt Structure

### [개념]

Prompt Structure는 LLM에게 작업을 전달하는 기본 구조다.

좋은 Prompt는 역할만 지정하지 않는다.

작업 목표, 참고 맥락, 제약 조건, 출력 형식, 실패 시 행동까지 포함한다.

기본 구조:

```text
Goal
→ Role
→ Context
→ Task
→ Constraints
→ Output Format
→ Failure Rule
→ Validation
```

---

### [핵심]

- Goal은 작업 목적이다.
- Role은 LLM의 관점과 책임이다.
- Context는 판단에 필요한 배경 정보다.
- Task는 실제 수행할 작업이다.
- Constraints는 반드시 지켜야 할 조건이다.
- Output Format은 결과 형태다.
- Failure Rule은 정보 부족 시 행동이다.
- Validation은 최종 점검 기준이다.

---

### [실무]

2026 실무 기준으로 Prompt는 재사용 가능한 Template 형태로 관리하는 것이 좋다.

예시:

```text
You are a Backend Review Agent.

Task:
Review the given Spring Boot Service code.

Context:
Use the provided project rules and code context.

Constraints:
- Do not invent missing classes.
- Separate confirmed facts from assumptions.
- Focus on transaction boundary, N+1 risk, exception handling, and DTO responsibility.

Output Format:
Return Markdown with Summary, Findings, Fix Direction, Checklist.

Failure Rule:
If the code context is insufficient, clearly state what is missing.
```

이 구조는 Backend Review Agent, Code Generation Agent, PM Agent, RAG Answer Agent에 공통 적용 가능하다.

---

### [FAQ]

Q. Prompt 구조는 어떻게 잡아야 해?

A. Goal, Role, Context, Task, Constraints, Output Format, Failure Rule, Validation 순서로 잡으면 안정적이다.

Q. Role만 주면 충분해?

A. 아니다. Role만 있으면 관점은 생기지만 작업 기준과 출력 형식이 부족해 결과가 흔들릴 수 있다.

Q. Output Format을 왜 지정해야 해?

A. Markdown, JSON, Checklist처럼 결과 형식을 지정해야 후속 처리와 검수가 쉬워진다.

Q. Failure Rule은 왜 필요해?

A. 정보가 부족할 때 모델이 지어내지 않고 부족한 정보를 명확히 표시하도록 하기 위해 필요하다.

---

# 3. Prompt Component

## 3.1 Goal

### [개념]

Goal은 Prompt의 최종 목적이다.

Goal은 LLM이 무엇을 달성해야 하는지 정의한다.

좋은 Goal은 짧고 명확해야 한다.

예시:

```text
Goal:
Generate a Spring Boot Service implementation plan.
```

```text
Goal:
Review the given code for maintainability and runtime risks.
```

---

### [핵심]

- Goal은 Prompt의 방향을 결정한다.
- Goal이 모호하면 답변이 일반론으로 흐른다.
- Goal은 하나의 주요 목적에 집중해야 한다.
- 여러 목표가 있으면 우선순위를 지정해야 한다.

---

### [실무]

실무에서는 Goal을 구체적인 산출물 기준으로 작성한다.

나쁜 Goal:

```text
이 코드 봐줘.
```

좋은 Goal:

```text
Review this Spring Boot Service code and identify transaction boundary, N+1 query risk, null safety, and exception handling issues.
```

Goal은 “무엇을 해줘”가 아니라 “어떤 기준으로 어떤 결과를 만들어줘”까지 포함하는 것이 좋다.

---

### [FAQ]

Q. Goal은 뭘 적는 부분이야?

A. LLM이 최종적으로 달성해야 할 작업 목적을 적는 부분이다.

Q. Goal이 모호하면 어떻게 돼?

A. 답변이 일반적이거나 사용자가 원하는 방향과 다르게 나올 가능성이 높다.

Q. Goal은 길게 써야 해?

A. 아니다. 짧고 명확하게 작성하되, 산출물 기준은 포함하는 것이 좋다.

---

## 3.2 Role

### [개념]

Role은 LLM이 어떤 관점과 책임으로 답변할지 정하는 요소다.

Role은 전문성, 판단 기준, 책임 범위를 부여한다.

예시:

```text
You are a Senior Spring Boot Backend Architect.
```

```text
You are a PM Agent for a Multi-Agent Development Workflow.
```

---

### [핵심]

- Role은 답변 관점을 안정화한다.
- Role은 책임 범위와 함께 정의해야 한다.
- Role만 있고 Task가 없으면 결과가 불명확하다.
- Agent 시스템에서는 Role 분리가 중요하다.
- PM Agent, Backend Agent, Frontend Agent, Review Agent는 서로 다른 Role을 가져야 한다.

---

### [실무]

실무 Role Prompt는 아래 요소를 포함한다.

```text
Role
→ Responsibility
→ Scope
→ Expertise
→ Output Standard
→ Limitation
```

예시:

```text
You are a Backend Agent.
You design Spring Boot backend implementation based on provided requirements.
You focus on API, DTO, Service, Repository, transaction boundary, and exception handling.
Do not modify frontend code.
```

Role은 넓게 잡기보다 담당 영역을 명확히 나누는 것이 좋다.

---

### [FAQ]

Q. Role Prompt는 왜 필요해?

A. LLM이 어떤 관점과 책임으로 답변할지 정해 답변 방향을 안정화하기 위해 필요하다.

Q. “너는 전문가야”라고만 쓰면 충분해?

A. 아니다. 책임 범위, 검증 기준, 출력 형식이 함께 있어야 한다.

Q. Agent마다 Role을 따로 둬야 해?

A. 그렇다. PM Agent, Backend Agent, Review Agent는 책임이 다르므로 Role Prompt도 달라야 한다.

---

## 3.3 Context

### [개념]

Context는 LLM이 답변할 때 참고해야 하는 배경 정보다.

Context에는 프로젝트 상황, 코드 구조, 비즈니스 규칙, 기술 스택, 기존 결정사항, RAG 검색 결과가 포함될 수 있다.

Context가 부족하면 답변은 일반론이 된다.

---

### [핵심]

- Context는 답변 정확도에 직접 영향을 준다.
- 프로젝트 고유 규칙은 Context로 제공해야 한다.
- RAG 검색 결과는 Context로 주입된다.
- Context와 Task는 분리해서 작성하는 것이 좋다.
- 오래된 Context와 최신 Context 충돌을 주의해야 한다.
- 관련 없는 Context를 과도하게 넣으면 핵심이 흐려진다.

---

### [실무]

실무 Context 작성 예시:

```text
Project Context:
- Java 21
- Spring Boot 3.x
- Response uses ApiResponse<T>
- GlobalExceptionHandler handles exceptions
- Controller should not contain business logic

Code Context:
- Entity, DTO, Repository are already defined
- Service should handle transaction boundary

Task:
Generate Service implementation plan.
```

Context는 “참고 정보”이고, Task는 “해야 할 일”이다.

둘을 섞으면 Prompt가 길어지고 모델이 핵심을 놓칠 수 있다.

---

### [FAQ]

Q. Context Prompt는 왜 중요해?

A. LLM은 제공된 Context를 기준으로 답변하므로 프로젝트 상황과 제약이 없으면 일반적인 답변을 하게 된다.

Q. Context를 많이 넣으면 무조건 좋아?

A. 아니다. 관련 없는 Context가 많으면 핵심이 흐려지고 답변 품질이 낮아질 수 있다.

Q. RAG 검색 결과도 Context야?

A. 그렇다. RAG에서 검색된 문서는 Prompt에 주입되는 핵심 Context다.

---

## 3.4 Task

### [개념]

Task는 LLM이 실제로 수행해야 하는 작업이다.

Task는 구체적이고 실행 가능해야 한다.

나쁜 Task:

```text
좋게 만들어줘.
```

좋은 Task:

```text
Refactor the Service logic while preserving the existing Controller, DTO, and Repository signatures.
```

---

### [핵심]

- Task는 명확해야 한다.
- Task는 입력과 대상이 있어야 한다.
- Task는 원하는 산출물을 포함해야 한다.
- Task가 여러 개면 순서와 우선순위를 지정해야 한다.
- Task와 Context는 분리해서 작성한다.

---

### [실무]

실무에서 Task는 아래처럼 작성한다.

```text
Task:
Review the provided Controller code.

Focus:
- Business logic inside Controller
- Request validation
- Response format consistency
- Exception handling

Return:
- Problem
- Cause
- Risk
- Fix Direction
```

Task가 명확할수록 Review Agent나 Code Generation Agent의 출력 품질이 좋아진다.

---

### [FAQ]

Q. Task는 어떻게 작성해야 해?

A. 수행 대상, 작업 내용, 검증 기준, 출력 형태를 명확히 작성해야 한다.

Q. “검토해줘”만 쓰면 안 좋아?

A. 기준이 없기 때문에 단순 감상이나 일반론으로 답변할 가능성이 높다.

Q. 여러 작업을 한 번에 시켜도 돼?

A. 가능하지만 우선순위와 출력 구조를 명확히 지정해야 한다.

---

## 3.5 Constraints

### [개념]

Constraints는 LLM이 반드시 지켜야 하는 조건이다.

Constraints는 모델의 자유도를 줄이고 프로젝트 규칙을 따르게 만든다.

Constraints는 Must, Must Not, Prefer, Avoid로 구분할 수 있다.

---

### [핵심]

- Constraints는 Prompt 품질을 결정한다.
- 기술 버전, 스타일, 금지사항은 명시해야 한다.
- 프로젝트 고유 규칙은 Constraints로 고정한다.
- 제약이 충돌하면 우선순위를 지정해야 한다.
- 제약이 너무 많으면 모델이 실패할 수 있다.

---

### [실무]

실무 Constraints 예시:

```text
Must:
- Use Java 21.
- Use Spring Boot 3.x.
- Return Korean explanation.
- Follow Controller → Service → Repository structure.

Must Not:
- Do not invent missing classes.
- Do not expose secrets.
- Do not change existing API paths unless requested.

Prefer:
- Use short code snippets.
- Explain only important decisions.
```

Constraints는 Agent의 출력 안정성과 프로젝트 일관성을 높인다.

---

### [FAQ]

Q. Constraints는 왜 필요해?

A. 모델이 프로젝트 규칙과 금지사항을 지키도록 제어하기 위해 필요하다.

Q. Must와 Prefer는 어떻게 달라?

A. Must는 반드시 지켜야 하는 조건이고, Prefer는 가능하면 따르는 선호 조건이다.

Q. 제약 조건이 많으면 좋아?

A. 아니다. 너무 많거나 충돌하면 모델이 실패하거나 중요한 조건을 놓칠 수 있다.

---

## 3.6 Output Format

### [개념]

Output Format은 LLM 결과의 형태를 지정하는 요소다.

Output Format은 Markdown, JSON, YAML, Table, Checklist, Code Block 등이 될 수 있다.

Agent Workflow에서는 Output Format이 후속 Agent 처리에 직접 영향을 준다.

---

### [핵심]

- Output Format은 답변 일관성을 높인다.
- Markdown은 사람이 읽는 문서와 리뷰에 적합하다.
- JSON은 Tool Calling과 자동 처리에 적합하다.
- Checklist는 검증 작업에 적합하다.
- Code Block은 코드 생성과 예시에 적합하다.
- Schema가 명확할수록 출력이 안정적이다.

---

### [실무]

Markdown Output 예시:

```md
## Summary

## Findings

### 1. Problem

- Cause:
- Risk:
- Fix Direction:

## Checklist
```

JSON Output 예시:

```json
{
  "status": "completed",
  "summary": "Review completed",
  "findings": [
    {
      "type": "transaction",
      "severity": "high",
      "message": "Transaction boundary is unclear"
    }
  ]
}
```

JSON을 요구할 때는 부가 설명을 금지하는 제약을 함께 넣는 것이 좋다.

```text
Return only valid JSON.
Do not include Markdown or extra explanation.
```

---

### [FAQ]

Q. Output Format은 왜 지정해야 해?

A. 결과 형식을 고정해야 사람이 읽거나 후속 Agent가 처리하기 쉽기 때문이다.

Q. Markdown은 언제 좋아?

A. 설명, 리뷰, RAG 문서, 체크리스트처럼 사람이 읽는 결과에 적합하다.

Q. JSON은 언제 좋아?

A. Tool Calling, 자동 처리, Multi-Agent Workflow에서 후속 시스템이 결과를 파싱해야 할 때 적합하다.

Q. JSON 출력이 자꾸 깨지면 어떻게 해?

A. Schema를 단순화하고 “Return only valid JSON” 같은 제약을 추가한다.

---

## 3.7 Validation

### [개념]

Validation은 LLM이 출력하기 전에 결과를 검토하도록 만드는 단계다.

Validation은 정확성, 완전성, 형식 준수, 근거성, 누락 정보 여부를 점검한다.

복잡한 Prompt에서는 Validation이 품질 안정화에 중요하다.

---

### [핵심]

- Validation은 최종 답변 품질을 높인다.
- Accuracy, Completeness, Format Compliance를 확인한다.
- RAG에서는 Groundedness를 확인해야 한다.
- 코드 생성에서는 컴파일 가능성, 프로젝트 규칙, 예외 처리를 확인한다.
- 리뷰에서는 Severity와 Fix Direction이 적절한지 확인한다.

---

### [실무]

실무 Validation Prompt 예시:

```text
Before final answer, check:
- Does the answer follow the requested output format?
- Are all claims grounded in the provided context?
- Are assumptions clearly marked?
- Is missing information clearly stated?
- Are code snippets aligned with the project stack?
```

Validation은 내부 점검용으로 두고 최종 출력은 간결하게 만드는 것이 좋다.

---

### [FAQ]

Q. Validation은 뭐야?

A. LLM이 답변 전 정확성, 누락, 형식 준수, 근거성을 점검하도록 하는 단계다.

Q. RAG에서 Validation은 왜 중요해?

A. 검색 문서에 없는 내용을 지어내지 않도록 Groundedness를 확인해야 하기 때문이다.

Q. Validation 결과를 전부 출력해야 해?

A. 아니다. 사용자가 요청하지 않으면 최종 결과 중심으로 정리하는 것이 좋다.

---

# 4. Prompt Quality Criteria

## 4.1 Clear Instruction

### [개념]

Clear Instruction은 Prompt가 명확한 지시를 제공하는지 평가하는 기준이다.

명확한 지시는 LLM의 답변 방향을 안정화한다.

모호한 지시는 답변 품질을 크게 떨어뜨린다.

---

### [핵심]

- 지시는 짧고 직접적이어야 한다.
- 작업 대상과 결과물이 명확해야 한다.
- 불필요한 배경 설명보다 작업 기준이 중요하다.
- 중요한 조건은 명시적으로 작성한다.
- 모호한 표현을 피한다.

---

### [실무]

나쁜 지시:

```text
이거 괜찮게 정리해줘.
```

좋은 지시:

```text
Rewrite this text as a RAG-optimized Markdown document.
Use [개념], [핵심], [실무], [FAQ] sections.
Keep explanations short and retrieval-friendly.
```

Clear Instruction은 RAG 문서 제작, 코드 생성, 코드 리뷰, Agent Prompt 설계 모두에 적용된다.

---

### [FAQ]

Q. Clear Instruction이 뭐야?

A. LLM이 해야 할 작업과 출력 기준을 명확히 지시하는 것이다.

Q. 모호한 지시는 왜 문제야?

A. 모델이 원하는 결과를 추정해야 하므로 답변이 흔들리거나 일반론으로 흐른다.

Q. 좋은 지시는 어떤 특징이 있어?

A. 작업 대상, 수행 기준, 제약 조건, 출력 형식이 명확하다.

---

## 4.2 Context Quality

### [개념]

Context Quality는 Prompt에 제공된 배경 정보의 품질이다.

Context가 정확하고 관련성이 높을수록 LLM 답변 품질이 올라간다.

Context가 부족하거나 오래되었거나 충돌하면 답변 품질이 낮아진다.

---

### [핵심]

- 관련 있는 Context만 제공한다.
- 최신 Context와 기존 Context 충돌을 확인한다.
- 프로젝트 고유 규칙은 명시한다.
- 코드 생성 시 Entity, DTO, Repository 구조를 제공한다.
- RAG에서는 검색된 Chunk의 품질이 Context Quality를 결정한다.

---

### [실무]

좋은 Context 예시:

```text
Environment:
- Java 21
- Spring Boot 3.x
- MySQL
- Spring Data JPA

Project Rule:
- Controller returns ApiResponse<T> directly.
- Exception handling is done by GlobalExceptionHandler.
- Business logic belongs to Service.

Target:
- Review the provided Service code.
```

Context Quality가 낮으면 Agent는 일반적인 Spring Boot 답변을 생성한다.

Context Quality가 높으면 Agent는 프로젝트에 맞는 답변을 생성한다.

---

### [FAQ]

Q. Context Quality가 뭐야?

A. LLM이 참고하는 배경 정보가 정확하고 관련성이 높은지를 의미한다.

Q. Context가 부족하면 어떻게 돼?

A. 모델이 일반 지식으로 답하거나 프로젝트와 맞지 않는 내용을 생성할 수 있다.

Q. RAG에서 Context Quality는 무엇에 달려 있어?

A. 검색된 Chunk의 정확도, 관련성, 독립성, 최신성에 달려 있다.

---

## 4.3 Output Stability

### [개념]

Output Stability는 LLM이 반복 실행해도 비슷한 구조와 품질의 결과를 생성하는 능력이다.

Output Stability는 Prompt Template, Output Format, Few-Shot Example, Constraints로 개선할 수 있다.

---

### [핵심]

- Output Format을 고정하면 안정성이 높아진다.
- Few-Shot Example은 출력 패턴을 안정화한다.
- JSON Schema는 자동 처리 안정성을 높인다.
- Markdown Header는 RAG 문서 구조를 안정화한다.
- 불필요한 자유도를 줄이면 결과가 일관된다.

---

### [실무]

Agent Workflow에서 Output Stability는 매우 중요하다.

PM Agent가 Backend Agent에게 넘기는 산출물 형식이 매번 달라지면 후속 Agent가 처리하기 어렵다.

예시:

```md
## Task Summary

## Requirements

## Constraints

## Output Expected

## Missing Information
```

이처럼 고정된 형식을 사용하면 Agent 간 Handoff 품질이 좋아진다.

---

### [FAQ]

Q. Output Stability는 왜 중요해?

A. 반복 작업과 Multi-Agent Workflow에서 결과 형식이 안정적이어야 후속 처리가 가능하기 때문이다.

Q. 출력이 매번 달라지면 어떻게 해야 해?

A. Output Format, Schema, Few-Shot Example, Constraints를 추가해야 한다.

Q. RAG 문서에서도 Output Stability가 필요해?

A. 필요하다. 문서 구조가 일정해야 검색 Chunk 품질과 Retrieval 정확도가 좋아진다.

---

# 5. Prompt Engineering in RAG

## 5.1 RAG Prompt Core

### [개념]

RAG Prompt는 검색된 문서를 기반으로 답변하도록 설계된 Prompt다.

RAG Prompt의 핵심은 Grounded Answer다.

Grounded Answer는 검색 문서에 근거한 답변이다.

문서에 없는 내용은 추정하거나 지어내지 않고 부족한 정보로 표시해야 한다.

---

### [핵심]

- 검색된 문서를 우선 사용한다.
- 문서에 없는 내용은 없다고 말한다.
- 일반 지식과 문서 근거를 구분한다.
- 추정은 Assumption으로 표시한다.
- 검색 실패와 지식 부재를 구분한다.
- RAG Prompt는 Hallucination Prevention Rule을 포함해야 한다.

---

### [실무]

RAG Prompt 기본 구조:

```text
Use the retrieved context to answer the user question.

Rules:
- Prioritize retrieved documents.
- Do not invent project-specific facts.
- If context is insufficient, say what is missing.
- Clearly separate confirmed facts and assumptions.
- Return the answer in the requested format.
```

RAG Agent가 코드 생성까지 수행할 경우 아래 규칙이 추가된다.

```text
Code Generation Rules:
- Use only provided project structure.
- Do not create missing class names unless marked as assumption.
- Keep snippets short.
- Follow project conventions.
```

---

### [FAQ]

Q. RAG Prompt는 뭐야?

A. 검색된 문서를 근거로 답변하도록 설계한 Prompt다.

Q. RAG Prompt에서 가장 중요한 규칙은 뭐야?

A. 검색 문서를 우선 사용하고 문서에 없는 내용은 지어내지 않는 것이다.

Q. 문서에 없는 내용은 어떻게 처리해야 해?

A. 정보가 부족하다고 말하고 필요한 추가 정보를 명확히 표시해야 한다.

Q. RAG Prompt가 없으면 어떻게 돼?

A. 모델이 검색 문서보다 일반 지식으로 답하거나 프로젝트에 없는 내용을 지어낼 수 있다.

---

## 5.2 Retrieval-Friendly Prompt

### [개념]

Retrieval-Friendly Prompt는 검색 결과를 잘 활용하도록 설계된 Prompt다.

질문이 문서 Chunk와 잘 매칭되도록 핵심 키워드, 도메인 용어, 출력 형식을 명확히 포함한다.

---

### [핵심]

- 도메인 키워드를 명확히 사용한다.
- 질문 의도를 구체화한다.
- 검색 대상 개념을 분명히 한다.
- 출력 형식을 지정한다.
- 불필요한 배경 설명을 줄인다.
- 문서 용어와 사용자 질문 용어를 연결한다.

---

### [실무]

나쁜 Prompt:

```text
이거 어떻게 해?
```

좋은 Prompt:

```text
Prompt Engineering 문서 기준으로 RAG Prompt 작성 방법을 설명해줘.
검색 문서에 없는 내용은 Assumption으로 표시하고,
결과는 [개념], [핵심], [실무], [FAQ] 구조로 작성해줘.
```

Retrieval-Friendly Prompt는 RAG 시스템에서 검색 정확도를 높인다.

사용자가 실제로 물어볼 표현을 Retrieval Queries에 포함하면 검색 품질이 좋아진다.

---

### [FAQ]

Q. Retrieval-Friendly Prompt가 뭐야?

A. RAG 검색 결과와 잘 매칭되도록 핵심 키워드와 질문 의도를 명확히 포함한 Prompt다.

Q. 검색이 잘 안 되면 Prompt를 어떻게 바꿔야 해?

A. 도메인 키워드, 문서 용어, 원하는 출력 형식, 구체적인 질문 의도를 추가한다.

Q. Retrieval Queries는 왜 필요해?

A. 사용자가 실제로 물어볼 질문 패턴을 문서에 포함해 검색 적중률을 높이기 위해 필요하다.

---

# 6. Prompt Engineering in Agent Workflow

## 6.1 Agent Prompt Core

### [개념]

Agent Prompt는 AI Agent의 역할, 입력, 출력, 도구 사용, 제약, 종료 조건을 정의하는 Prompt다.

Agent Prompt는 단순 역할극이 아니라 Agent의 책임 범위와 행동 규칙이다.

---

### [핵심]

- Agent Role을 명확히 정의한다.
- Responsibility를 구체화한다.
- Input과 Output을 고정한다.
- Tools 사용 기준을 정의한다.
- Handoff Rule을 포함한다.
- Stop Condition을 명확히 한다.
- Failure Rule을 포함한다.

---

### [실무]

Agent Prompt 기본 구조:

```text
You are a Backend Agent.

Responsibility:
- Design backend implementation.
- Generate API, DTO, Service, Repository plan.
- Follow project architecture.

Input:
- PM Agent task brief.
- Retrieved backend RAG documents.
- Existing project code context.

Output:
- Markdown with API, DTO, Service, Repository, Validation sections.

Constraints:
- Do not modify frontend code.
- Do not invent missing project classes.
- Mark assumptions clearly.

Stop Condition:
- Stop after producing implementation plan and required code snippets.
```

Agent Prompt는 역할 경계를 좁게 잡을수록 안정적이다.

---

### [FAQ]

Q. Agent Prompt는 뭐야?

A. AI Agent의 역할, 책임, 입력, 출력, 도구 사용, 제약, 종료 조건을 정의하는 Prompt다.

Q. Agent Prompt에 Stop Condition이 왜 필요해?

A. Agent가 불필요하게 반복하거나 범위를 벗어나지 않도록 하기 위해 필요하다.

Q. 하나의 Agent에 모든 역할을 넣어도 돼?

A. 권장하지 않는다. 역할이 넓으면 책임이 흐려지고 결과 품질이 낮아진다.

---

## 6.2 Multi-Agent Prompt Core

### [개념]

Multi-Agent Prompt는 여러 Agent가 협업할 때 필요한 역할 분리와 Handoff 구조를 정의한다.

PM Agent는 요청을 분해하고, Domain Agent는 작업을 수행하고, Review Agent는 결과를 검증한다.

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

---

### [핵심]

- PM Agent는 작업 분해와 라우팅을 담당한다.
- Domain Agent는 전문 작업을 수행한다.
- Review Agent는 품질 검증을 담당한다.
- Fix Agent는 리뷰 결과를 반영한다.
- 최종 결과는 사용자에게 필요한 형태로 요약한다.
- Agent 간 출력 형식을 통일해야 한다.
- 무한 반복 방지 조건이 필요하다.

---

### [실무]

Multi-Agent Workflow Prompt 예시:

```text
PM Agent:
- Analyze user request.
- Decompose task.
- Send structured task to Backend Agent.

Backend Agent:
- Generate backend implementation plan.
- Return structured Markdown output.

Review Agent:
- Review backend output using checklist.
- Return findings with severity.

Fix Agent:
- Apply review feedback.
- Return final corrected output.
```

Agent 간 Handoff 문서는 아래 구조를 권장한다.

```md
## Task

## Context

## Constraints

## Expected Output

## Missing Information

## Review Criteria
```

---

### [FAQ]

Q. Multi-Agent Prompt는 어떻게 설계해?

A. PM Agent가 작업을 분해하고 Domain Agent가 수행하며 Review Agent가 검증하는 흐름과 산출물 형식을 정한다.

Q. Agent 간 Handoff가 왜 중요해?

A. 한 Agent의 출력이 다음 Agent의 입력이 되므로 형식이 불안정하면 전체 Workflow가 흔들린다.

Q. Review Agent는 왜 필요해?

A. Domain Agent의 결과를 검증하고 오류, 누락, 형식 문제를 찾아 품질을 높이기 위해 필요하다.

---

# 7. Hallucination Prevention

## 7.1 Missing Information Rule

### [개념]

Missing Information Rule은 정보가 부족할 때 LLM이 지어내지 않고 부족한 정보를 표시하도록 하는 규칙이다.

RAG, Code Generation, Project Review, Agent Workflow에서 필수다.

---

### [핵심]

- 문서에 없는 내용을 확정하지 않는다.
- 프로젝트 고유 클래스명, API 경로, 정책을 임의 생성하지 않는다.
- 부족한 정보는 Missing Information으로 표시한다.
- 추정은 Assumption으로 분리한다.
- 확정 사실과 추정을 구분한다.

---

### [실무]

Missing Information Rule 예시:

```text
If the provided context does not contain the answer, say that the context is insufficient.
Do not invent project-specific facts.
Clearly mark assumptions.
```

코드 생성 Prompt에서는 아래 규칙을 추가한다.

```text
Do not create class names, API paths, database columns, or business rules that are not provided.
If needed, propose them as assumptions, not confirmed facts.
```

---

### [FAQ]

Q. Missing Information Rule이 뭐야?

A. 정보가 부족할 때 모델이 지어내지 않고 부족한 정보를 명확히 표시하도록 하는 규칙이다.

Q. 왜 프로젝트 고유 정보를 지어내면 안 돼?

A. 실제 코드, API, DB 구조와 맞지 않는 결과를 만들 수 있기 때문이다.

Q. Assumption은 언제 사용해?

A. 확정 정보는 없지만 작업 진행을 위해 가정이 필요한 경우 명확히 표시할 때 사용한다.

---

## 7.2 Grounded Answer

### [개념]

Grounded Answer는 제공된 Context나 RAG 문서를 근거로 작성된 답변이다.

Grounded Answer는 일반 지식, 추정, 문서 근거를 구분한다.

---

### [핵심]

- 검색 문서에 근거한 답변을 우선한다.
- 근거 없는 확정 표현을 피한다.
- 문서에 없는 정보는 Missing Information으로 표시한다.
- 추정은 Assumption으로 표시한다.
- 오래된 정보와 최신 정보 충돌을 주의한다.

---

### [실무]

Grounded Answer Prompt 예시:

```text
Answer based on the retrieved context.
If the retrieved context is insufficient, state what is missing.
Separate:
- Confirmed by context
- Assumption
- Missing information
```

Review Agent에서는 아래 형식을 사용할 수 있다.

```md
## Confirmed

## Assumptions

## Missing Information

## Final Recommendation
```

---

### [FAQ]

Q. Grounded Answer가 뭐야?

A. 제공된 Context나 RAG 문서에 근거해 작성한 답변이다.

Q. Grounded Answer가 왜 중요해?

A. Hallucination을 줄이고 프로젝트 문맥에 맞는 답변을 만들기 위해 중요하다.

Q. 일반 지식은 사용하면 안 돼?

A. 사용할 수 있지만, RAG 문서 근거와 일반 추론을 구분해야 한다.

---

# 8. Common Mistakes

## 8.1 Prompt Mistakes

### [개념]

Prompt Mistake는 LLM 답변 품질을 떨어뜨리는 잘못된 Prompt 작성 방식이다.

대부분의 실패는 목표, 맥락, 제약, 출력 형식 부족에서 발생한다.

---

### [핵심]

자주 발생하는 실수:

- 목표가 불명확함
- Context가 부족함
- 출력 형식이 없음
- 제약 조건이 모호함
- Role만 있고 Task가 없음
- 문서에 없는 내용을 지어냄
- JSON 출력이 깨짐
- Prompt가 너무 길어 핵심이 흐려짐
- Agent 간 책임이 겹침
- 실패 시 행동이 없음
- Code Generation에 버전 정보가 없음
- Review 기준 없이 “검토해줘”라고만 요청
- RAG Prompt에 근거 우선 규칙이 없음
- Prompt 결과 평가 없이 반복 사용

---

### [실무]

문제 있는 Prompt:

```text
너는 전문가야. 이거 잘 만들어줘.
```

개선된 Prompt:

```text
You are a Prompt Engineering Agent.

Task:
Create a RAG-optimized Markdown document about RAG Prompt.

Constraints:
- Use [개념], [핵심], [실무], [FAQ].
- Keep explanations short and retrieval-friendly.
- Do not invent project-specific facts.
- Include Retrieval Queries.

Output Format:
Return only the final Markdown document.
```

Prompt 실패는 대부분 Prompt Template 개선으로 줄일 수 있다.

---

### [FAQ]

Q. Prompt 작성에서 가장 흔한 실수는 뭐야?

A. 목표, Context, 제약, 출력 형식을 명확히 쓰지 않는 것이다.

Q. Role만 주면 왜 부족해?

A. Role은 관점만 정할 뿐 실제 작업 기준과 결과 형식을 보장하지 않기 때문이다.

Q. Prompt가 너무 길면 문제야?

A. 관련 없는 내용이 많으면 핵심이 흐려져 답변 품질이 낮아질 수 있다.

---

# 9. Best Practice

## 9.1 Prompt Engineering Best Practice

### [개념]

Prompt Engineering Best Practice는 LLM에게 안정적이고 재사용 가능한 결과를 얻기 위한 작성 원칙이다.

Best Practice는 RAG, Code Generation, Code Review, Agent Workflow 전반에 적용된다.

---

### [핵심]

- Prompt는 Goal / Context / Task / Constraint / Output Format으로 구성한다.
- Role만 주지 말고 책임과 기준도 명시한다.
- RAG Prompt는 문서 근거 우선 규칙을 포함한다.
- 출력 형식은 Markdown / JSON 등으로 명확히 지정한다.
- 실패 시 행동을 정의한다.
- 복잡한 작업은 단계별로 분해한다.
- 반복 작업은 Prompt Template으로 관리한다.
- Code Generation은 버전과 프로젝트 규칙을 명시한다.
- Code Review는 검증 기준과 Severity를 포함한다.
- Agent Prompt는 Handoff Rule과 Stop Condition을 포함한다.
- 불확실한 정보는 Assumption으로 표시한다.
- Prompt 결과는 평가 후 개선한다.

---

### [실무]

실무 Prompt 작성 Checklist:

```md
### [Checklist]

- [ ] Goal이 명확한가?
- [ ] Role이 정의되어 있는가?
- [ ] Task가 구체적인가?
- [ ] Context가 충분한가?
- [ ] Constraints가 명확한가?
- [ ] Output Format이 지정되어 있는가?
- [ ] Missing Information Rule이 있는가?
- [ ] Assumption 표시 규칙이 있는가?
- [ ] Validation 기준이 있는가?
- [ ] 후속 Agent가 처리 가능한 구조인가?
```

이 Checklist는 PM Agent, Backend Agent, Review Agent, RAG Agent Prompt 설계에 공통 적용 가능하다.

---

### [FAQ]

Q. Prompt Engineering Best Practice는 뭐야?

A. 목표, 맥락, 작업, 제약, 출력 형식, 실패 처리, 검증 기준을 명확히 설계하는 것이다.

Q. 반복 작업에는 어떤 방식이 좋아?

A. Prompt Template을 만들어 Placeholder 기반으로 재사용하는 방식이 좋다.

Q. Agent Prompt에서 가장 중요한 것은 뭐야?

A. 역할, 책임, 입력, 출력, Handoff Rule, Stop Condition을 명확히 하는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Prompt Engineering이 뭐야?
A. LLM이 원하는 작업을 정확히 수행하도록 목표, 맥락, 제약, 출력 형식을 설계하는 작업이다.

Q. Prompt는 그냥 질문이야?
A. 아니다. 실무에서 Prompt는 LLM에게 전달하는 작업 지시서이자 Agent 행동 규칙이다.

Q. 좋은 Prompt는 어떻게 작성해?
A. Goal, Role, Context, Task, Constraints, Output Format, Validation을 명확히 작성한다.

Q. Prompt 기본 구조는 뭐야?
A. Goal → Role → Context → Task → Constraints → Output Format → Failure Rule → Validation 구조가 안정적이다.

Q. Goal은 왜 중요해?
A. LLM이 달성해야 할 작업 목적을 정해 답변 방향을 결정하기 때문이다.

Q. Role Prompt는 왜 필요해?
A. LLM이 어떤 관점과 책임으로 답변할지 정해 답변 방향을 안정화하기 위해 필요하다.

Q. Context Prompt는 왜 중요해?
A. LLM은 제공된 Context를 기준으로 답변하므로 프로젝트 상황과 제약을 정확히 넣어야 한다.

Q. Task는 어떻게 작성해야 해?
A. 수행 대상, 작업 내용, 검증 기준, 출력 형태를 명확히 작성해야 한다.

Q. Constraints는 왜 필요해?
A. 모델이 프로젝트 규칙, 기술 버전, 금지사항을 지키도록 제어하기 위해 필요하다.

Q. Output Format은 왜 지정해야 해?
A. 결과 형식을 고정해야 사람이 읽거나 후속 Agent가 처리하기 쉽기 때문이다.

Q. Markdown 출력은 언제 좋아?
A. 설명, 리뷰, RAG 문서, 체크리스트처럼 사람이 읽는 결과에 적합하다.

Q. JSON 출력은 언제 좋아?
A. Tool Calling, 자동 처리, Multi-Agent Workflow에서 후속 시스템이 결과를 파싱해야 할 때 적합하다.

Q. JSON 출력이 자꾸 깨지면 어떻게 해?
A. Schema를 단순화하고 “Return only valid JSON” 같은 제약을 추가한다.

Q. Validation은 왜 필요해?
A. 답변 전 정확성, 누락, 형식 준수, 근거성을 점검해 출력 품질을 높이기 위해 필요하다.

Q. Clear Instruction이 뭐야?
A. LLM이 해야 할 작업과 출력 기준을 명확히 지시하는 것이다.

Q. Context Quality가 뭐야?
A. LLM이 참고하는 배경 정보가 정확하고 관련성이 높은지를 의미한다.

Q. Output Stability는 왜 중요해?
A. 반복 작업과 Multi-Agent Workflow에서 결과 형식이 안정적이어야 후속 처리가 가능하기 때문이다.

Q. RAG Prompt는 뭐야?
A. 검색된 문서를 근거로 답변하도록 설계한 Prompt다.

Q. RAG Prompt에서 가장 중요한 규칙은 뭐야?
A. 검색 문서를 우선 사용하고 문서에 없는 내용은 지어내지 않는 것이다.

Q. Retrieval-Friendly Prompt가 뭐야?
A. RAG 검색 결과와 잘 매칭되도록 핵심 키워드와 질문 의도를 명확히 포함한 Prompt다.

Q. Agent Prompt는 뭐야?
A. AI Agent의 역할, 책임, 입력, 출력, 도구 사용, 제약, 종료 조건을 정의하는 Prompt다.

Q. Multi-Agent Prompt는 어떻게 설계해?
A. PM Agent가 작업을 분해하고 Domain Agent가 수행하며 Review Agent가 검증하는 흐름과 산출물 형식을 정한다.

Q. Agent 간 Handoff가 왜 중요해?
A. 한 Agent의 출력이 다음 Agent의 입력이 되므로 형식이 불안정하면 전체 Workflow가 흔들린다.

Q. Missing Information Rule이 뭐야?
A. 정보가 부족할 때 모델이 지어내지 않고 부족한 정보를 명확히 표시하도록 하는 규칙이다.

Q. Grounded Answer가 뭐야?
A. 제공된 Context나 RAG 문서에 근거해 작성한 답변이다.

Q. Hallucination을 줄이려면 어떻게 해?
A. 문서 근거 우선 규칙, Missing Information Rule, Assumption 표시, 검증 단계를 Prompt에 포함한다.

Q. Prompt 작성에서 가장 흔한 실수는 뭐야?
A. 목표, Context, 제약, 출력 형식을 명확히 쓰지 않는 것이다.

Q. Role만 주면 왜 부족해?
A. Role은 관점만 정할 뿐 실제 작업 기준과 결과 형식을 보장하지 않기 때문이다.

Q. Prompt Engineering Best Practice는 뭐야?
A. 목표, 맥락, 작업, 제약, 출력 형식, 실패 처리, 검증 기준을 명확히 설계하는 것이다.

Q. Prompt Template은 언제 써?
A. 반복 작업을 일정한 품질과 형식으로 수행해야 할 때 사용한다.

Q. Prompt Engineering 문서의 최종 목표는 뭐야?
A. Agent가 정확하고 일관된 지시를 이해하고 근거 기반으로 구조화된 결과를 생성하도록 돕는 것이다.
