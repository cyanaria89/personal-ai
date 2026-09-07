# Prompt Engineering Part03 Role Prompt, System Prompt, User Prompt

---

# 1. Role Prompt

## 1.1 Role Prompt Definition

### [개념]

Role Prompt는 LLM이 어떤 관점, 책임, 전문성으로 답변할지 정의하는 Prompt다.

Role Prompt는 단순히 “너는 전문가야”라고 지정하는 것이 아니다.

Role Prompt는 아래 요소를 함께 포함해야 한다.

```text
Role
→ Responsibility
→ Scope
→ Expertise
→ Output Standard
→ Limitation
```

Role Prompt는 Agent의 정체성과 책임 경계를 결정한다.

---

### [핵심]

- Role Prompt는 LLM의 답변 관점을 안정화한다.
- Role은 전문성과 판단 기준을 부여한다.
- Role만 있고 Task가 없으면 결과가 불명확하다.
- Role에는 Responsibility와 Scope가 함께 있어야 한다.
- Agent Workflow에서는 Agent별 Role 분리가 중요하다.
- 하나의 Prompt에 여러 Role을 섞으면 책임 경계가 흐려진다.
- Role Prompt는 System Prompt 또는 Agent Prompt에 포함될 수 있다.

---

### [실무]

2026 실무 기준 Role Prompt는 Agent 단위로 분리한다.

예시:

```text
You are a Senior Spring Boot Backend Architect.

Responsibility:
- Review backend architecture.
- Check transaction boundary.
- Check domain responsibility.
- Check maintainability and testability.

Scope:
- Backend code only.
- Do not modify frontend code.
- Do not invent missing project classes.

Output Standard:
- Return findings with severity, cause, risk, and fix direction.
```

좋지 않은 Role Prompt:

```text
You are an expert.
```

좋은 Role Prompt:

```text
You are a Backend Review Agent.
You review Spring Boot backend code based on transaction boundary, N+1 query risk, exception handling, DTO responsibility, and API response consistency.
Return findings in Korean Markdown.
```

Role은 넓게 잡기보다 작업 기준과 책임 범위를 명확히 포함해야 한다.

---

### [FAQ]

Q. Role Prompt가 뭐야?

A. LLM이 어떤 관점, 책임, 전문성으로 답변할지 정의하는 Prompt다.

Q. “너는 전문가야”만 쓰면 충분해?

A. 아니다. 책임 범위, 검증 기준, 출력 형식이 함께 있어야 한다.

Q. Role Prompt는 왜 필요해?

A. LLM의 답변 관점을 안정화하고 Agent의 책임 범위를 명확히 하기 위해 필요하다.

Q. 하나의 Prompt에 여러 Role을 넣어도 돼?

A. 권장하지 않는다. 역할이 섞이면 답변 기준과 책임 경계가 흐려질 수 있다.

---

# 2. Role Prompt Components

## 2.1 Responsibility

### [개념]

Responsibility는 Role이 담당해야 하는 작업 책임이다.

Role이 “누구인지”를 정한다면 Responsibility는 “무엇을 책임지는지”를 정한다.

Responsibility가 없으면 Role Prompt는 역할극에 가까워진다.

---

### [핵심]

- Responsibility는 수행 책임을 명확히 한다.
- Agent별 Responsibility는 겹치지 않게 설계한다.
- Responsibility는 Task와 연결되어야 한다.
- Responsibility에는 검증 기준을 포함할 수 있다.
- Responsibility가 넓으면 Agent 출력이 불안정해진다.

---

### [실무]

Backend Agent Responsibility 예시:

```text
Responsibility:
- Analyze backend requirements.
- Design API, DTO, Service, Repository structure.
- Follow Spring Boot 3.x and Java 21 conventions.
- Keep business logic in Service.
- Mark missing information clearly.
```

Review Agent Responsibility 예시:

```text
Responsibility:
- Review generated backend output.
- Check correctness, maintainability, transaction boundary, exception handling, and RAG rule compliance.
- Return findings with severity and fix direction.
```

PM Agent Responsibility 예시:

```text
Responsibility:
- Analyze user request.
- Decompose the task.
- Route work to the appropriate Domain Agent.
- Provide structured task brief.
```

Agent 책임은 명확하게 분리해야 한다.

PM Agent는 작업 분해, Domain Agent는 작업 수행, Review Agent는 검증을 담당한다.

---

### [FAQ]

Q. Responsibility는 뭐야?

A. Role이 어떤 작업을 책임지는지 정의하는 요소다.

Q. Role과 Responsibility는 어떻게 달라?

A. Role은 관점과 정체성이고, Responsibility는 실제 담당 업무다.

Q. Agent별 Responsibility가 겹치면 어떻게 돼?

A. 중복 작업, 충돌 출력, 책임 불명확 문제가 발생할 수 있다.

---

## 2.2 Scope

### [개념]

Scope는 Role이 다룰 수 있는 범위와 다루면 안 되는 범위를 정의한다.

Scope는 Agent의 작업 경계를 제한한다.

Scope가 없으면 Agent가 요청 범위를 넘어 불필요한 작업을 수행할 수 있다.

---

### [핵심]

- Scope는 포함 범위와 제외 범위를 모두 정의한다.
- Scope는 Agent 책임 경계를 고정한다.
- Scope는 Hallucination과 범위 초과를 줄인다.
- Scope는 Handoff 기준과 연결된다.
- Code Generation에서는 변경 가능한 파일과 변경 금지 파일을 구분해야 한다.

---

### [실무]

Scope 예시:

```text
Scope:
Included:
- Spring Boot Service logic
- Repository usage
- Transaction boundary
- Exception handling
- DTO conversion

Excluded:
- Frontend component design
- Database schema migration
- Deployment configuration
- Unprovided external API policy
```

Backend Agent Scope 예시:

```text
Scope:
- Work only on backend implementation.
- Do not modify frontend code.
- Do not create database schema unless explicitly requested.
- Do not invent missing business rules.
```

Scope는 Agent가 “하지 말아야 할 일”을 명확히 하므로 작업 안정성에 중요하다.

---

### [FAQ]

Q. Scope는 뭐야?

A. Role이나 Agent가 다룰 수 있는 작업 범위와 제외 범위를 정의하는 요소다.

Q. Scope가 없으면 어떤 문제가 생겨?

A. Agent가 범위를 넘어 불필요한 코드나 정책을 생성할 수 있다.

Q. Scope에는 제외 범위도 적어야 해?

A. 그렇다. 포함 범위와 제외 범위를 함께 적어야 책임 경계가 명확해진다.

---

## 2.3 Expertise

### [개념]

Expertise는 Role이 어떤 전문 지식을 기준으로 판단해야 하는지 정의하는 요소다.

Expertise는 답변의 판단 기준과 품질 기준을 결정한다.

---

### [핵심]

- Expertise는 기술 도메인을 명확히 한다.
- Expertise는 버전과 프레임워크를 포함할 수 있다.
- Expertise는 검토 기준과 연결된다.
- Expertise가 모호하면 답변이 일반론이 된다.
- Agent별 Expertise는 Domain Rules와 연결되어야 한다.

---

### [실무]

Expertise 예시:

```text
Expertise:
- Java 21
- Spring Boot 3.x
- Spring Data JPA
- REST API Design
- Transaction Management
- Exception Handling
- Layered Architecture
```

Prompt Engineering Agent Expertise 예시:

```text
Expertise:
- Prompt Engineering
- Instruction Design
- RAG Prompt
- Agent Prompt
- Structured Output
- Hallucination Prevention
- Multi-Agent Workflow Prompt
```

Expertise는 “전문가”라는 단어보다 구체적인 도메인 키워드로 작성해야 Retrieval과 답변 품질이 좋아진다.

---

### [FAQ]

Q. Expertise는 뭐야?

A. Role이 어떤 전문 지식과 기준으로 판단해야 하는지 정의하는 요소다.

Q. Expertise에 버전을 넣어야 해?

A. 코드 생성이나 리뷰에서는 Java, Spring Boot, React 같은 기술 버전을 넣는 것이 좋다.

Q. Expertise가 모호하면 어떻게 돼?

A. 답변이 구체적인 실무 기준이 아니라 일반적인 설명으로 흐를 수 있다.

---

## 2.4 Limitation

### [개념]

Limitation은 Role이 할 수 없는 일, 확정할 수 없는 일, 피해야 할 일을 정의하는 요소다.

Limitation은 과도한 추정과 Hallucination을 줄이는 안전장치다.

---

### [핵심]

- Limitation은 Role의 한계를 명확히 한다.
- 제공되지 않은 정보는 확정하지 않는다.
- 프로젝트 고유 정보는 임의 생성하지 않는다.
- 보이지 않는 코드에 대해 단정하지 않는다.
- 외부 정책이나 최신 정보는 필요 시 확인해야 한다.
- Limitation은 Missing Information Rule과 연결된다.

---

### [실무]

Limitation 예시:

```text
Limitation:
- Do not invent missing classes, API paths, database columns, or business rules.
- Do not claim unseen code has no issue.
- If required context is missing, state what is missing.
- Mark assumptions clearly.
```

Review Agent Limitation 예시:

```text
Limitation:
- Review only the provided code.
- Do not make claims about unseen layers.
- Separate confirmed issues from possible risks.
```

Limitation은 Agent가 확실하지 않은 내용을 확정적으로 말하지 않도록 제어한다.

---

### [FAQ]

Q. Limitation은 뭐야?

A. Role이 할 수 없는 일과 확정하면 안 되는 일을 정의하는 요소다.

Q. Limitation은 왜 필요해?

A. 모델이 제공되지 않은 정보를 지어내거나 보이지 않는 코드까지 단정하는 것을 막기 위해 필요하다.

Q. Limitation과 Missing Information Rule은 관련 있어?

A. 관련 있다. Limitation은 모르는 내용을 확정하지 않게 하고, Missing Information Rule은 부족한 정보를 표시하게 한다.

---

# 3. System Prompt

## 3.1 System Prompt Definition

### [개념]

System Prompt는 Agent 또는 LLM의 기본 행동 규칙을 정의하는 상위 Prompt다.

System Prompt는 지속적으로 적용되는 기본 규칙이며, Role, 응답 언어, 출력 형식, Tool 사용 기준, RAG 사용 기준, 안전 규칙을 포함할 수 있다.

System Prompt는 일회성 요청보다 상위에 있는 행동 지침이다.

---

### [핵심]

- System Prompt는 지속적인 상위 규칙이다.
- Agent의 Identity와 Role을 정의한다.
- 응답 언어와 출력 형식을 고정할 수 있다.
- RAG 문서 사용 우선순위를 정의한다.
- Tool Use Rule을 정의할 수 있다.
- Safety Rule과 Hallucination Prevention Rule을 포함한다.
- 너무 긴 System Prompt는 유지보수가 어렵다.
- 프로젝트별 규칙과 일반 규칙은 분리하는 것이 좋다.

---

### [실무]

System Prompt 예시:

```text
You are a Backend Agent.
Answer in Korean.
Use retrieved documents first.
If the document does not contain enough information, say what is missing.
Do not invent project-specific code.
Return code snippets only when necessary.
Follow the project architecture and domain rules.
```

Prompt Engineering Agent System Prompt 예시:

```text
You are a Prompt Engineering Agent.
Your task is to create and review RAG-optimized Prompt Engineering documents.
Use MASTER_RAG_RULES and Prompt Engineering Domain Rules.
Return Markdown documents with [개념], [핵심], [실무], [FAQ], and Retrieval Queries.
Do not produce essay-style content.
Do not include unsupported project-specific facts.
```

System Prompt는 Agent의 기본 행동을 고정하는 데 사용하고, 개별 작업은 User Prompt에서 지정한다.

---

### [FAQ]

Q. System Prompt가 뭐야?

A. Agent나 LLM의 기본 행동 규칙을 정의하는 지속적인 상위 Prompt다.

Q. System Prompt에는 뭐가 들어가야 해?

A. Identity, Role, Core Rules, Response Language, Output Format, Safety Rule, Tool Use Rule, RAG Use Rule이 들어갈 수 있다.

Q. System Prompt에 모든 작업을 다 넣어도 돼?

A. 권장하지 않는다. 지속 규칙은 System Prompt에, 일회성 작업은 User Prompt에 넣는 것이 좋다.

Q. System Prompt가 너무 길면 문제야?

A. 유지보수가 어렵고 핵심 규칙이 흐려질 수 있다.

---

# 4. System Prompt Components

## 4.1 Identity

### [개념]

Identity는 System Prompt에서 Agent가 어떤 존재인지 정의하는 요소다.

Identity는 Role보다 더 상위의 정체성이다.

예를 들어 “Backend Agent”는 Identity이고, “Spring Boot Service Review 담당”은 Role 또는 Responsibility다.

---

### [핵심]

- Identity는 Agent의 기본 정체성을 정의한다.
- Identity는 지속적으로 유지된다.
- Identity는 Agent 이름이나 역할군으로 표현할 수 있다.
- Identity는 Responsibility와 함께 작성해야 한다.
- Identity만 있고 작업 기준이 없으면 불충분하다.

---

### [실무]

Identity 예시:

```text
You are a Backend Agent in a personal AI development team.
```

```text
You are a Prompt Engineering Agent for RAG document creation and review.
```

```text
You are a Review Agent responsible for validating outputs from Domain Agents.
```

Identity는 Agent 시스템의 전체 구조와 맞아야 한다.

예시 Agent 구조:

```text
User
→ PM Agent
→ Backend Agent
→ Frontend Agent
→ Review Agent
→ Final Output
```

Identity는 Agent 간 책임 분리에 사용된다.

---

### [FAQ]

Q. Identity는 뭐야?

A. System Prompt에서 Agent가 어떤 존재인지 정의하는 기본 정체성이다.

Q. Identity와 Role은 어떻게 달라?

A. Identity는 Agent의 큰 정체성이고, Role은 특정 작업에서의 관점과 책임이다.

Q. Identity만 있으면 충분해?

A. 아니다. Responsibility, Scope, Output Rule이 함께 있어야 한다.

---

## 4.2 Core Rules

### [개념]

Core Rules는 Agent가 항상 따라야 하는 기본 규칙이다.

Core Rules는 응답 방식, 근거 사용, 출력 형식, 금지사항, 검증 기준을 포함한다.

---

### [핵심]

- Core Rules는 지속 규칙이다.
- System Prompt에서 우선순위가 높다.
- RAG 기반 Agent는 검색 문서 우선 규칙을 포함해야 한다.
- 코드 생성 Agent는 프로젝트 구조 준수 규칙을 포함해야 한다.
- Review Agent는 검증 기준과 Severity 기준을 포함할 수 있다.
- Core Rules가 많으면 유지보수성과 준수율이 낮아질 수 있다.

---

### [실무]

Core Rules 예시:

```text
Core Rules:
- Answer in Korean.
- Use retrieved documents first.
- Do not invent project-specific facts.
- Mark assumptions clearly.
- State missing information when context is insufficient.
- Keep output structured and concise.
- Follow requested output format.
```

RAG Document Agent Core Rules 예시:

```text
Core Rules:
- Apply MASTER_RAG_RULES.
- Apply DOMAIN_RULES.
- Optimize for retrieval, not human reading.
- Include [개념], [핵심], [실무], [FAQ].
- Include Retrieval Queries.
- Keep chunks independently searchable.
- Avoid essay-style explanations.
```

Core Rules는 Agent가 매번 반복해서 지켜야 하는 기준만 넣는다.

---

### [FAQ]

Q. Core Rules는 뭐야?

A. Agent가 항상 따라야 하는 기본 행동 규칙이다.

Q. Core Rules에는 무엇을 넣어야 해?

A. 응답 언어, 근거 사용, 출력 형식, 금지사항, Missing Information Rule, 검증 기준을 넣을 수 있다.

Q. Core Rules가 너무 많으면 어떻게 돼?

A. 핵심 규칙이 흐려지고 유지보수와 준수가 어려워질 수 있다.

---

## 4.3 Response Language

### [개념]

Response Language는 Agent가 어떤 언어로 답변할지 정의하는 규칙이다.

다국어 입력이 있더라도 프로젝트 기준 언어를 고정해야 할 때 사용한다.

---

### [핵심]

- 응답 언어를 명확히 지정한다.
- 프로젝트 문서 언어와 답변 언어를 일치시키는 것이 좋다.
- 코드 키워드와 기술 용어는 원문 영어를 유지할 수 있다.
- 번역보다 용어 통일이 중요하다.
- RAG 문서에서는 검색 키워드 때문에 영어 기술 용어를 유지하는 것이 유리하다.

---

### [실무]

Response Language 예시:

```text
Answer in Korean.
Keep technical terms such as Prompt Engineering, System Prompt, RAG Prompt, Agent Prompt, Structured Output in English.
```

RAG 문서에서는 아래처럼 용어를 유지한다.

```text
Prompt Engineering
System Prompt
User Prompt
Role Prompt
RAG Prompt
Agent Prompt
Multi-Agent Prompt
Structured Output
Hallucination Prevention
```

한글 설명과 영어 기술 용어를 함께 사용하면 한국어 질의와 영어 키워드 검색 모두에 유리하다.

---

### [FAQ]

Q. Response Language는 뭐야?

A. Agent가 어떤 언어로 답변할지 지정하는 규칙이다.

Q. 한국어 문서에서 영어 기술 용어를 써도 돼?

A. 가능하다. Prompt Engineering, RAG Prompt 같은 핵심 용어는 영어로 유지하면 Retrieval에 유리하다.

Q. 응답 언어를 지정하지 않으면 어떻게 돼?

A. 입력 언어, 모델 성향, 검색 문서 언어에 따라 답변 언어가 흔들릴 수 있다.

---

## 4.4 Tool Use Rule

### [개념]

Tool Use Rule은 Agent가 도구를 언제, 어떻게 사용해야 하는지 정의하는 규칙이다.

Tool Use Rule은 검색, 파일 조회, 코드 실행, 캘린더, 메일, 웹 조회 같은 외부 도구 사용 기준을 정한다.

---

### [핵심]

- Tool 사용 조건을 명확히 한다.
- Tool 사용 결과와 모델 추론을 구분한다.
- 최신 정보가 필요한 경우 검색 도구 사용을 지정할 수 있다.
- 파일 기반 작업은 업로드 문서를 우선 사용한다.
- Tool 실패 시 Failure Rule을 적용한다.
- Tool 결과를 과도하게 일반화하지 않는다.

---

### [실무]

Tool Use Rule 예시:

```text
Tool Use Rule:
- Use uploaded documents as primary context for RAG document tasks.
- Use search only when current or external information is required.
- If tool result is insufficient, state missing information.
- Do not invent tool outputs.
```

Code Review Agent Tool Use Rule 예시:

```text
Tool Use Rule:
- If source code files are provided, inspect provided files first.
- Do not assume unseen files.
- If required files are missing, list them as Missing Information.
```

Tool Use Rule은 Agent가 외부 정보와 내부 추론을 섞지 않도록 제어한다.

---

### [FAQ]

Q. Tool Use Rule이 뭐야?

A. Agent가 도구를 언제, 어떻게 사용해야 하는지 정하는 규칙이다.

Q. Tool 결과와 추론은 구분해야 해?

A. 그렇다. 도구로 확인한 정보와 모델이 추론한 정보는 구분해야 한다.

Q. Tool 결과가 부족하면 어떻게 해야 해?

A. 부족한 정보를 Missing Information으로 표시하고 확정적으로 말하지 않아야 한다.

---

## 4.5 RAG Use Rule

### [개념]

RAG Use Rule은 Agent가 검색된 문서를 어떻게 사용할지 정의하는 규칙이다.

RAG Use Rule은 Grounded Answer와 Hallucination Prevention의 핵심이다.

---

### [핵심]

- 검색 문서를 우선 사용한다.
- 문서에 없는 내용은 지어내지 않는다.
- 검색 결과가 부족하면 부족한 정보를 표시한다.
- 문서 근거와 일반 추론을 구분한다.
- 문서 간 충돌이 있으면 우선순위를 따른다.
- Retrieval Queries와 FAQ를 활용해 검색 적중률을 높인다.

---

### [실무]

RAG Use Rule 예시:

```text
RAG Use Rule:
- Use retrieved documents first.
- If retrieved context is insufficient, state what is missing.
- Do not invent project-specific facts.
- Separate confirmed facts, assumptions, and missing information.
- Follow MASTER_RAG_RULES and DOMAIN_RULES when generating documents.
```

RAG Answer Agent 출력 예시:

```md
## Answer

## Confirmed by Retrieved Context

## Assumptions

## Missing Information
```

RAG Use Rule이 없으면 모델이 검색 문서를 무시하고 일반 지식으로 답변할 수 있다.

---

### [FAQ]

Q. RAG Use Rule이 뭐야?

A. Agent가 검색된 문서를 우선 사용하고 문서에 없는 내용을 지어내지 않도록 하는 규칙이다.

Q. RAG Use Rule이 없으면 어떻게 돼?

A. 모델이 검색 문서를 무시하고 일반 지식이나 추정으로 답할 수 있다.

Q. 문서에 없는 내용은 어떻게 처리해?

A. Missing Information으로 표시하고 필요한 추가 정보를 명확히 적어야 한다.

---

# 5. User Prompt

## 5.1 User Prompt Definition

### [개념]

User Prompt는 사용자가 현재 수행하고 싶은 작업을 구체화하는 Prompt다.

System Prompt가 지속 규칙이라면, User Prompt는 현재 요청이다.

User Prompt는 Task, Input, Target, Constraint, Output Request, Priority를 포함하는 것이 좋다.

---

### [핵심]

- User Prompt는 현재 작업을 정의한다.
- 작업 대상과 원하는 결과를 명확히 해야 한다.
- 필요한 Context를 함께 제공하면 품질이 높아진다.
- 출력 형식을 지정하면 결과가 안정된다.
- 부족한 정보가 있으면 Agent가 Missing Information으로 표시해야 한다.
- User Prompt는 System Prompt와 충돌하지 않아야 한다.

---

### [실무]

나쁜 User Prompt:

```text
이 코드 괜찮아?
```

좋은 User Prompt:

```text
Spring Boot Service 코드를 리뷰해줘.
중점은 Transaction Boundary, N+1 Query Risk, Exception Handling, DTO Conversion Responsibility야.
결과는 문제 / 원인 / 위험 / 수정 방향으로 정리해줘.
보이지 않는 코드는 단정하지 말고 Missing Information으로 표시해줘.
```

RAG 문서 제작 User Prompt 예시:

```text
Prompt Engineering Part03 문서를 만들어줘.
주제는 Role Prompt, System Prompt, User Prompt야.
MASTER_RAG_RULES와 Prompt Engineering Domain Rules를 적용해.
출력은 [개념], [핵심], [실무], [FAQ], Retrieval Queries 구조로 작성해.
```

User Prompt는 “원하는 결과를 말하는 요청”이 아니라 “Agent가 바로 실행 가능한 작업 지시”로 작성하는 것이 좋다.

---

### [FAQ]

Q. User Prompt가 뭐야?

A. 사용자가 현재 수행하고 싶은 작업을 구체화하는 Prompt다.

Q. User Prompt에는 뭐가 들어가야 해?

A. Task, Input, Target, Constraint, Output Request, Priority가 들어가면 좋다.

Q. System Prompt와 User Prompt는 어떻게 달라?

A. System Prompt는 지속적인 상위 규칙이고, User Prompt는 현재 작업 요청이다.

Q. User Prompt가 모호하면 어떻게 돼?

A. 모델이 의도를 추정하게 되어 결과가 일반적이거나 원하는 형식과 다를 수 있다.

---

# 6. User Prompt Components

## 6.1 Task

### [개념]

Task는 User Prompt에서 실제 수행할 작업을 정의하는 요소다.

Task는 명확하고 실행 가능해야 한다.

---

### [핵심]

- Task는 작업 내용을 명확히 한다.
- Task는 대상과 기준을 포함해야 한다.
- Task가 여러 개면 순서를 지정한다.
- Task는 Output Request와 연결되어야 한다.
- Task가 모호하면 모델이 추정한다.

---

### [실무]

Task 예시:

```text
Task:
Review the provided Backend Service code.
```

구체적인 Task 예시:

```text
Task:
Review the provided Spring Boot Service code for transaction boundary, N+1 query risk, exception handling, and DTO conversion responsibility.
```

RAG 문서 제작 Task 예시:

```text
Task:
Create a RAG-optimized Markdown document for Prompt Engineering Role Prompt, System Prompt, and User Prompt.
```

Task는 “무엇을 해줘”에서 끝나면 부족하다.

검토 기준, 생성 범위, 결과 구조와 함께 작성해야 한다.

---

### [FAQ]

Q. User Prompt에서 Task는 뭐야?

A. LLM이 실제로 수행해야 하는 작업 내용이다.

Q. Task는 짧게 써도 돼?

A. 가능하지만 작업 대상과 기준은 포함해야 한다.

Q. Task가 여러 개면 어떻게 해?

A. 순서와 우선순위를 지정해 모델이 처리 순서를 알 수 있게 해야 한다.

---

## 6.2 Input

### [개념]

Input은 User Prompt에서 LLM이 작업에 사용할 실제 자료다.

Input에는 코드, 문서, 요구사항, 에러 로그, 검색 결과, 프로젝트 규칙이 포함될 수 있다.

---

### [핵심]

- Input은 작업 대상 자료다.
- Input과 Task를 분리하면 Prompt가 명확해진다.
- 코드 리뷰는 코드 Input이 필요하다.
- 디버깅은 에러 로그와 재현 절차 Input이 필요하다.
- RAG 문서 제작은 Domain Rules와 작성 대상이 필요하다.
- Input이 부족하면 Missing Information으로 표시해야 한다.

---

### [실무]

Input 예시:

```text
Input:
- Service code
- Entity code
- DTO code
- Repository interface
- Error log
- Project rule
```

코드 리뷰 User Prompt 예시:

```text
Task:
Review the Service code.

Input:
[Paste Service code here]

Context:
Java 21, Spring Boot 3.x, Spring Data JPA.

Output:
Problems, causes, risks, fix directions.
```

Input이 길 경우에는 중요한 부분을 먼저 제공하고, 전체 판단이 필요한 경우 관련 파일을 함께 제공한다.

---

### [FAQ]

Q. Input은 뭐야?

A. LLM이 작업에 사용할 실제 자료나 코드, 문서, 요구사항이다.

Q. Input이 없으면 어떻게 돼?

A. 모델이 일반론으로 답하거나 필요한 정보를 Missing Information으로 표시해야 한다.

Q. 코드 리뷰에는 어떤 Input이 필요해?

A. 대상 코드, 관련 Entity, DTO, Repository, 에러 로그, 프로젝트 규칙이 있으면 좋다.

---

## 6.3 Target

### [개념]

Target은 작업 대상의 범위를 구체적으로 지정하는 요소다.

Target은 어떤 파일, 어떤 코드, 어떤 문서, 어떤 기능을 처리할지 정한다.

---

### [핵심]

- Target은 작업 대상을 명확히 한다.
- Target이 없으면 범위가 과도하게 넓어진다.
- Target은 파일명, 클래스명, 기능명, 문서 Part로 지정할 수 있다.
- Target은 Scope와 연결된다.
- Target 외 영역은 건드리지 않도록 제한할 수 있다.

---

### [실무]

Target 예시:

```text
Target:
- AuthService.java
- LoginReqDto.java
- AuthController login endpoint
```

RAG 문서 Target 예시:

```text
Target:
- Prompt Engineering Part03
- Role Prompt
- System Prompt
- User Prompt
```

Refactoring Target 예시:

```text
Target:
- Service layer only
- Preserve Controller, DTO, Repository signatures
```

Target을 명확히 하면 모델이 불필요한 전체 구조를 생성하지 않는다.

---

### [FAQ]

Q. Target은 뭐야?

A. 작업 대상 파일, 코드, 문서, 기능 범위를 구체적으로 지정하는 요소다.

Q. Target이 없으면 어떤 문제가 생겨?

A. 모델이 요청 범위를 넓게 해석해 불필요한 코드나 설명을 생성할 수 있다.

Q. Target은 파일명으로 지정해도 돼?

A. 가능하다. 파일명, 클래스명, 기능명, 문서 Part로 지정할 수 있다.

---

## 6.4 Constraint

### [개념]

User Prompt의 Constraint는 현재 작업에서 지켜야 할 조건이다.

System Prompt의 지속 규칙과 달리 User Prompt Constraint는 해당 요청에 특화된 조건이다.

---

### [핵심]

- 현재 작업의 제한사항을 명확히 한다.
- 변경 금지 범위를 지정한다.
- 출력 형식 제약을 포함할 수 있다.
- 기술 버전과 프로젝트 규칙을 포함한다.
- System Prompt와 충돌하면 안 된다.
- 핵심 조건은 Must로 작성한다.

---

### [실무]

User Prompt Constraint 예시:

```text
Constraints:
- Use Java 21 and Spring Boot 3.x.
- Do not change existing API paths.
- Do not modify Controller signatures.
- Do not invent missing classes.
- Return Korean Markdown.
```

RAG 문서 Constraint 예시:

```text
Constraints:
- Apply MASTER_RAG_RULES.
- Apply DOMAIN_RULES.
- Optimize for retrieval.
- Do not write essay-style explanations.
- Include Retrieval Queries.
```

Constraint는 요청마다 달라질 수 있으므로 User Prompt에서 명확히 지정하는 것이 좋다.

---

### [FAQ]

Q. User Prompt의 Constraint는 뭐야?

A. 현재 작업에서 지켜야 할 조건과 제한사항이다.

Q. System Prompt에도 규칙이 있는데 User Prompt Constraint가 필요해?

A. 필요하다. System Prompt는 지속 규칙이고 User Prompt Constraint는 현재 작업의 세부 조건이다.

Q. Constraint가 System Prompt와 충돌하면 어떻게 해야 해?

A. 충돌하지 않게 작성해야 하며, 일반적으로 상위 System Prompt 규칙을 우선한다.

---

## 6.5 Output Request

### [개념]

Output Request는 User Prompt에서 원하는 결과 형식을 지정하는 요소다.

Output Request는 Markdown, JSON, Checklist, Table, Code Snippet, RAG Document 구조를 정의한다.

---

### [핵심]

- Output Request는 결과 형식을 안정화한다.
- 후속 Agent 처리에 필요한 구조를 지정한다.
- 문서 작성은 필수 섹션을 지정한다.
- 코드 리뷰는 문제, 원인, 위험, 수정 방향을 지정한다.
- JSON은 Schema를 지정해야 한다.
- 출력 형식이 없으면 결과가 흔들린다.

---

### [실무]

Markdown Output Request 예시:

```text
Output Request:
Return Markdown with:
- Summary
- Findings
- Fix Direction
- Checklist
```

Code Review Output Request 예시:

```text
Output Request:
For each issue, include:
- Problem
- Cause
- Risk
- Fix Direction
- Severity
```

RAG Document Output Request 예시:

```text
Output Request:
Use:
- [개념]
- [핵심]
- [실무]
- [FAQ]
- Retrieval Queries
```

JSON Output Request 예시:

```text
Output Request:
Return only valid JSON with fields:
- status
- summary
- findings
- requiresFollowUp
```

Output Request는 가능하면 고정된 Schema나 Section으로 작성한다.

---

### [FAQ]

Q. Output Request는 뭐야?

A. User Prompt에서 원하는 결과 형식과 포함 항목을 지정하는 요소다.

Q. Output Request가 없으면 어떻게 돼?

A. 모델이 임의 형식으로 답변해 후속 처리와 검수가 어려워질 수 있다.

Q. JSON을 원하면 어떻게 요청해야 해?

A. 필드명과 Schema를 지정하고 “Return only valid JSON” 같은 제약을 함께 넣어야 한다.

---

## 6.6 Priority

### [개념]

Priority는 User Prompt 안의 여러 요구사항 중 무엇을 우선할지 정하는 요소다.

Priority는 조건 충돌, 작업 순서, 품질 기준을 정하는 데 사용한다.

---

### [핵심]

- 중요한 요구사항을 우선순위로 정한다.
- Must는 Prefer보다 우선한다.
- 프로젝트 규칙은 일반 선호보다 우선한다.
- RAG 문서는 Retrieval 최적화가 사람용 가독성보다 우선할 수 있다.
- 보안 규칙은 편의성보다 우선한다.
- 충돌 조건이 있으면 우선순위를 명시한다.

---

### [실무]

Priority 예시:

```text
Priority:
1. Apply MASTER_RAG_RULES.
2. Apply DOMAIN_RULES.
3. Optimize retrieval quality.
4. Keep human readability acceptable.
```

Code Review Priority 예시:

```text
Priority:
1. Runtime risk
2. Security risk
3. Data consistency
4. Maintainability
5. Style preference
```

Priority는 복잡한 요청에서 모델이 덜 중요한 조건을 먼저 따르는 문제를 줄인다.

---

### [FAQ]

Q. User Prompt에서 Priority는 왜 필요해?

A. 여러 요구사항이 있을 때 무엇을 먼저 따라야 하는지 명확히 하기 위해 필요하다.

Q. RAG 문서 제작에서는 무엇이 우선이야?

A. Retrieval Hit, Chunk Quality, Semantic Similarity, Human Readability 순서로 우선한다.

Q. 코드 리뷰에서는 무엇을 우선해야 해?

A. 런타임 위험, 보안 위험, 데이터 정합성, 유지보수성, 스타일 선호 순서가 안정적이다.

---

# 7. System Prompt vs User Prompt

## 7.1 Difference

### [개념]

System Prompt와 User Prompt는 역할이 다르다.

System Prompt는 지속적인 상위 규칙이다.

User Prompt는 현재 작업 요청이다.

두 Prompt는 서로 충돌하지 않아야 하며, System Prompt가 기본 행동 기준을 제공하고 User Prompt가 구체적인 작업을 제공한다.

---

### [핵심]

| 구분      | System Prompt                       | User Prompt                             |
| --------- | ----------------------------------- | --------------------------------------- |
| 목적      | 지속 규칙 정의                      | 현재 작업 요청                          |
| 범위      | Agent 전체 행동                     | 현재 요청                               |
| 내용      | Role, 언어, 금지사항, RAG 사용 규칙 | Task, Input, Target, Constraint, Output |
| 변경 빈도 | 낮음                                | 높음                                    |
| 예시      | 답변은 한국어, 문서 근거 우선       | 이 Service 코드를 리뷰해줘              |
| 위험      | 너무 길면 유지보수 어려움           | 모호하면 결과 불안정                    |

---

### [실무]

좋은 분리 예시:

System Prompt:

```text
You are a Backend Review Agent.
Answer in Korean.
Use provided context first.
Do not invent project-specific facts.
Return structured Markdown.
```

User Prompt:

```text
Review the provided AuthService code.
Focus on transaction boundary, exception handling, DTO conversion responsibility, and N+1 query risk.
Return findings with severity, cause, risk, and fix direction.
```

System Prompt에는 지속 규칙만 넣고, User Prompt에는 현재 작업만 넣는 것이 유지보수에 좋다.

---

### [FAQ]

Q. System Prompt와 User Prompt 차이는 뭐야?

A. System Prompt는 지속적인 상위 규칙이고, User Prompt는 현재 작업 요청이다.

Q. 프로젝트 규칙은 어디에 넣어야 해?

A. 반복 적용되는 프로젝트 규칙은 System Prompt에, 현재 작업에만 필요한 세부 조건은 User Prompt에 넣는다.

Q. System Prompt와 User Prompt가 충돌하면 어떻게 돼?

A. 충돌 조건 때문에 모델 출력이 불안정해질 수 있으므로 규칙을 분리하고 우선순위를 명확히 해야 한다.

---

# 8. Role Prompt vs Task Prompt

## 8.1 Difference

### [개념]

Role Prompt는 LLM의 관점과 책임을 정한다.

Task Prompt는 LLM이 실제로 수행할 작업을 정한다.

Role만 있으면 “누구로 답할지”는 정해지지만 “무엇을 할지”가 부족하다.

Task만 있으면 작업은 정해지지만 판단 관점과 전문성이 부족할 수 있다.

---

### [핵심]

| 구분           | Role Prompt                 | Task Prompt          |
| -------------- | --------------------------- | -------------------- |
| 목적           | 관점과 책임 설정            | 수행 작업 정의       |
| 질문           | 어떤 역할로 답할까?         | 무엇을 할까?         |
| 포함 요소      | Role, Responsibility, Scope | Task, Target, Output |
| 단독 사용 위험 | 작업 기준 부족              | 전문 관점 부족       |
| 실무 기준      | Role + Responsibility 필요  | Task + Criteria 필요 |

---

### [실무]

Role만 있는 나쁜 예:

```text
You are a backend expert.
```

Task만 있는 부족한 예:

```text
Review this code.
```

Role + Task 좋은 예:

```text
You are a Backend Review Agent.

Task:
Review the provided Spring Boot Service code.

Criteria:
- Transaction boundary
- N+1 query risk
- Exception handling
- DTO conversion responsibility

Output:
Return problem, cause, risk, fix direction, and severity.
```

Role Prompt와 Task Prompt는 함께 사용할 때 가장 안정적이다.

---

### [FAQ]

Q. Role Prompt와 Task Prompt 차이는 뭐야?

A. Role Prompt는 관점과 책임을 정하고, Task Prompt는 실제 수행할 작업을 정한다.

Q. Role만 있으면 왜 부족해?

A. 역할은 정해지지만 작업 기준과 출력 형식이 없어서 답변이 흔들릴 수 있다.

Q. Task만 있으면 왜 부족해?

A. 작업은 정해지지만 어떤 전문 관점으로 판단할지 부족할 수 있다.

---

# 9. Prompt Layering

## 9.1 Prompt Layering Definition

### [개념]

Prompt Layering은 여러 Prompt 계층을 역할에 맞게 분리하는 설계 방식이다.

System Prompt, Domain Rules, RAG Context, User Prompt, Output Format은 서로 다른 계층으로 관리할 수 있다.

기본 구조:

```text
System Prompt
→ Domain Rules
→ Retrieved Context
→ User Prompt
→ Output Format
→ Validation
```

---

### [핵심]

- Prompt 계층을 분리하면 유지보수가 쉬워진다.
- System Prompt는 지속 규칙을 담당한다.
- Domain Rules는 도메인별 작성 기준을 담당한다.
- Retrieved Context는 근거 자료를 제공한다.
- User Prompt는 현재 작업을 지정한다.
- Output Format은 산출물 구조를 고정한다.
- Validation은 최종 점검을 담당한다.

---

### [실무]

RAG 문서 제작 Prompt Layering 예시:

```text
System Prompt:
You are a RAG document generation agent.

Master Rules:
Apply MASTER_RAG_RULES.

Domain Rules:
Apply Prompt Engineering Domain Rules.

Retrieved Context:
Use uploaded rules and project progress.

User Prompt:
Create Part03 for Role Prompt, System Prompt, User Prompt.

Output Format:
Use writing block with document variant.

Validation:
Check required sections, FAQ, Retrieval Queries, terminology consistency.
```

Layer를 분리하면 어떤 규칙이 어디서 왔는지 추적하기 쉽고, Agent별 Prompt 재사용성이 좋아진다.

---

### [FAQ]

Q. Prompt Layering이 뭐야?

A. System Prompt, Domain Rules, Retrieved Context, User Prompt, Output Format, Validation을 계층별로 분리하는 설계 방식이다.

Q. Prompt Layering은 왜 필요해?

A. 규칙 충돌을 줄이고 유지보수성과 재사용성을 높이기 위해 필요하다.

Q. RAG에서는 어떤 계층이 중요해?

A. Retrieved Context, RAG Use Rule, Missing Information Rule, Output Format 계층이 중요하다.

---

# 10. Common Mistakes

## 10.1 Role Prompt Mistakes

### [개념]

Role Prompt Mistake는 역할만 지정하고 책임, 범위, 기준을 생략하는 실수다.

이 경우 모델은 전문적인 말투를 흉내 내지만 실제 작업 품질은 안정되지 않는다.

---

### [핵심]

자주 발생하는 실수:

- “너는 전문가야”만 작성
- Responsibility 없음
- Scope 없음
- Output Standard 없음
- Limitation 없음
- 여러 Role을 하나에 혼합
- Agent 간 Role 중복
- Role과 Task 불일치

---

### [실무]

나쁜 예:

```text
You are an expert developer.
```

개선 예:

```text
You are a Backend Review Agent.
You review Spring Boot Service code.
Focus on transaction boundary, N+1 query risk, exception handling, DTO conversion responsibility, and maintainability.
Return findings with severity, cause, risk, and fix direction.
Do not make claims about unseen files.
```

Role Prompt는 반드시 Responsibility, Scope, Output Standard와 연결한다.

---

### [FAQ]

Q. Role Prompt에서 가장 흔한 실수는 뭐야?

A. 역할만 지정하고 책임, 범위, 검증 기준, 출력 형식을 생략하는 것이다.

Q. 여러 Role을 한 Prompt에 넣으면 왜 문제야?

A. 책임 경계가 흐려지고 답변 기준이 충돌할 수 있다.

---

## 10.2 System Prompt Mistakes

### [개념]

System Prompt Mistake는 지속 규칙과 일회성 작업을 섞거나, 너무 많은 규칙을 넣어 유지보수가 어려워지는 문제다.

---

### [핵심]

자주 발생하는 실수:

- System Prompt에 일회성 작업 포함
- 너무 긴 규칙 나열
- 프로젝트 규칙과 일반 규칙 혼합
- RAG Use Rule 없음
- Missing Information Rule 없음
- Output Format 없음
- Tool Use Rule 불명확
- Safety Rule 없음

---

### [실무]

나쁜 System Prompt:

```text
You are an AI. Answer well. Create login service today. Also review frontend later.
```

개선 System Prompt:

```text
You are a Backend Agent.
Answer in Korean.
Use retrieved documents first.
Do not invent project-specific facts.
If required context is missing, state what is missing.
Return structured Markdown.
```

System Prompt는 지속적으로 적용될 규칙만 넣고, 현재 작업은 User Prompt로 분리한다.

---

### [FAQ]

Q. System Prompt에서 가장 흔한 실수는 뭐야?

A. 지속 규칙과 일회성 작업을 섞고, 너무 많은 규칙을 넣어 핵심이 흐려지는 것이다.

Q. System Prompt에는 현재 작업을 넣으면 안 돼?

A. 일반적으로 넣지 않는 것이 좋다. 현재 작업은 User Prompt에 넣는 것이 유지보수에 좋다.

---

## 10.3 User Prompt Mistakes

### [개념]

User Prompt Mistake는 현재 작업 요청이 모호하거나 입력, 대상, 제약, 출력 형식이 부족한 문제다.

---

### [핵심]

자주 발생하는 실수:

- “해줘”, “봐줘”, “만들어줘”만 작성
- Input 없음
- Target 없음
- Constraint 없음
- Output Request 없음
- Priority 없음
- 작업 범위가 너무 넓음
- 필요한 Context 없이 코드 생성 요청
- 보이지 않는 코드에 대한 단정 유도

---

### [실무]

나쁜 User Prompt:

```text
로그인 만들어줘.
```

개선 User Prompt:

```text
Spring Boot 3.x, Java 21 기준으로 로그인 Service 구현 계획을 작성해줘.

Context:
- Users Entity와 UserRepository는 존재한다고 가정하지 말고, 제공된 코드만 사용해.
- JWT 인증 구조를 사용한다.

Constraints:
- Controller 시그니처는 변경하지 않는다.
- 없는 클래스명은 만들지 않는다.
- 부족한 정보는 Missing Information으로 표시한다.

Output:
- Required Files
- Service Responsibility
- Method Flow
- Code Snippet
- Validation Checklist
```

User Prompt는 Agent가 바로 실행 가능한 작업 지시로 작성해야 한다.

---

### [FAQ]

Q. User Prompt에서 가장 흔한 실수는 뭐야?

A. 작업 대상, 입력, 제약, 출력 형식을 명확히 쓰지 않는 것이다.

Q. “만들어줘”만 쓰면 왜 문제야?

A. 범위와 기준이 없어 모델이 임의로 구조, 클래스명, 정책을 만들 수 있다.

---

# 11. Best Practice

## 11.1 Role Prompt Best Practice

### [개념]

Role Prompt Best Practice는 Role을 전문성, 책임, 범위, 출력 기준, 한계와 함께 정의하는 방식이다.

---

### [핵심]

- Role은 구체적인 도메인명으로 작성한다.
- Responsibility를 포함한다.
- Scope를 포함한다.
- Expertise를 구체적으로 작성한다.
- Output Standard를 지정한다.
- Limitation을 포함한다.
- Agent별 Role은 분리한다.
- Role과 Task를 함께 사용한다.

---

### [실무]

Role Prompt Template:

```text
You are a [Domain] Agent.

Responsibility:
- [Main responsibility]
- [Review or generation criteria]

Scope:
- Included: [Allowed work]
- Excluded: [Forbidden work]

Expertise:
- [Technology / domain keywords]

Output Standard:
- Return [format] with [required fields].

Limitation:
- Do not invent missing information.
- Mark assumptions clearly.
```

이 Template은 Backend Agent, Frontend Agent, Review Agent, Prompt Engineering Agent에 공통 적용 가능하다.

---

### [FAQ]

Q. Role Prompt Best Practice는 뭐야?

A. Role을 Responsibility, Scope, Expertise, Output Standard, Limitation과 함께 정의하는 것이다.

Q. Role Prompt는 Agent마다 따로 작성해야 해?

A. 그렇다. Agent마다 책임과 출력 기준이 다르므로 별도 작성하는 것이 좋다.

---

## 11.2 System Prompt Best Practice

### [개념]

System Prompt Best Practice는 지속 규칙만 간결하게 유지하고, 현재 작업은 User Prompt로 분리하는 방식이다.

---

### [핵심]

- Identity를 명확히 한다.
- Core Rules를 간결하게 유지한다.
- Response Language를 지정한다.
- RAG Use Rule을 포함한다.
- Tool Use Rule을 필요한 경우 포함한다.
- Missing Information Rule을 포함한다.
- Output Standard를 포함한다.
- 일회성 작업은 넣지 않는다.

---

### [실무]

System Prompt Template:

```text
You are a [Agent Identity].

Core Rules:
- Answer in [Language].
- Use retrieved context first.
- Follow [Master Rules / Domain Rules].
- Do not invent project-specific facts.
- Mark assumptions clearly.
- State missing information when context is insufficient.
- Return structured output in the requested format.

Tool Use Rule:
- Use tools only when needed.
- Do not invent tool results.
```

RAG 문서 제작 Agent는 System Prompt에서 MASTER_RAG_RULES와 DOMAIN_RULES 적용을 고정한다.

---

### [FAQ]

Q. System Prompt Best Practice는 뭐야?

A. 지속 규칙을 간결하게 유지하고, RAG Use Rule, Missing Information Rule, 출력 기준을 포함하는 것이다.

Q. System Prompt와 User Prompt를 왜 분리해?

A. 지속 규칙과 현재 작업을 분리해야 유지보수성과 재사용성이 좋아진다.

---

## 11.3 User Prompt Best Practice

### [개념]

User Prompt Best Practice는 현재 작업을 Agent가 바로 실행 가능한 형태로 작성하는 방식이다.

---

### [핵심]

- Task를 명확히 작성한다.
- Input을 제공한다.
- Target을 지정한다.
- Constraint를 명시한다.
- Output Request를 지정한다.
- Priority를 필요한 경우 작성한다.
- Missing Information 처리 기준을 포함한다.
- 작업 범위를 과도하게 넓히지 않는다.

---

### [실무]

User Prompt Template:

```text
Task:
[What to do]

Input:
[Code / document / requirement / log]

Target:
[File / class / feature / document part]

Context:
[Project context / stack / rules]

Constraints:
- [Must]
- [Must Not]

Output Request:
[Markdown / JSON / Checklist / Code Snippet]

Priority:
[Optional priority]

Failure Rule:
If information is missing, state what is missing and do not invent facts.
```

이 Template은 코드 생성, 코드 리뷰, RAG 문서 제작, 디버깅, 리팩토링 요청에 재사용할 수 있다.

---

### [FAQ]

Q. User Prompt Best Practice는 뭐야?

A. Task, Input, Target, Context, Constraints, Output Request, Failure Rule을 명확히 작성하는 것이다.

Q. User Prompt를 길게 써야 해?

A. 불필요하게 길 필요는 없지만, 작업에 필요한 기준과 입력은 포함해야 한다.

Q. Missing Information Rule은 User Prompt에도 넣어야 해?

A. 중요한 작업에서는 넣는 것이 좋다. 정보 부족 시 모델이 지어내지 않게 막을 수 있다.

---

# Retrieval Queries

### [FAQ]

Q. Role Prompt가 뭐야?
A. LLM이 어떤 관점, 책임, 전문성으로 답변할지 정의하는 Prompt다.

Q. Role Prompt는 왜 필요해?
A. LLM의 답변 관점을 안정화하고 Agent의 책임 범위를 명확히 하기 위해 필요하다.

Q. “너는 전문가야”만 쓰면 충분해?
A. 아니다. 책임 범위, 검증 기준, 출력 형식이 함께 있어야 한다.

Q. Role Prompt에는 뭐가 들어가야 해?
A. Role, Responsibility, Scope, Expertise, Output Standard, Limitation이 들어가야 한다.

Q. Responsibility는 뭐야?
A. Role이 어떤 작업을 책임지는지 정의하는 요소다.

Q. Scope는 뭐야?
A. Role이나 Agent가 다룰 수 있는 작업 범위와 제외 범위를 정의하는 요소다.

Q. Expertise는 뭐야?
A. Role이 어떤 전문 지식과 기준으로 판단해야 하는지 정의하는 요소다.

Q. Limitation은 뭐야?
A. Role이 할 수 없는 일과 확정하면 안 되는 일을 정의하는 요소다.

Q. System Prompt가 뭐야?
A. Agent나 LLM의 기본 행동 규칙을 정의하는 지속적인 상위 Prompt다.

Q. System Prompt에는 뭐가 들어가야 해?
A. Identity, Role, Core Rules, Response Language, Output Format, Safety Rule, Tool Use Rule, RAG Use Rule이 들어갈 수 있다.

Q. System Prompt에 모든 작업을 다 넣어도 돼?
A. 권장하지 않는다. 지속 규칙은 System Prompt에, 일회성 작업은 User Prompt에 넣는 것이 좋다.

Q. Identity는 뭐야?
A. System Prompt에서 Agent가 어떤 존재인지 정의하는 기본 정체성이다.

Q. Core Rules는 뭐야?
A. Agent가 항상 따라야 하는 기본 행동 규칙이다.

Q. Response Language는 뭐야?
A. Agent가 어떤 언어로 답변할지 지정하는 규칙이다.

Q. 한국어 문서에서 영어 기술 용어를 써도 돼?
A. 가능하다. Prompt Engineering, RAG Prompt 같은 핵심 용어는 영어로 유지하면 Retrieval에 유리하다.

Q. Tool Use Rule이 뭐야?
A. Agent가 도구를 언제, 어떻게 사용해야 하는지 정하는 규칙이다.

Q. RAG Use Rule이 뭐야?
A. Agent가 검색된 문서를 우선 사용하고 문서에 없는 내용을 지어내지 않도록 하는 규칙이다.

Q. User Prompt가 뭐야?
A. 사용자가 현재 수행하고 싶은 작업을 구체화하는 Prompt다.

Q. User Prompt에는 뭐가 들어가야 해?
A. Task, Input, Target, Constraint, Output Request, Priority가 들어가면 좋다.

Q. System Prompt와 User Prompt 차이는 뭐야?
A. System Prompt는 지속적인 상위 규칙이고, User Prompt는 현재 작업 요청이다.

Q. User Prompt가 모호하면 어떻게 돼?
A. 모델이 의도를 추정하게 되어 결과가 일반적이거나 원하는 형식과 다를 수 있다.

Q. User Prompt에서 Task는 뭐야?
A. LLM이 실제로 수행해야 하는 작업 내용이다.

Q. Input은 뭐야?
A. LLM이 작업에 사용할 실제 자료나 코드, 문서, 요구사항이다.

Q. Target은 뭐야?
A. 작업 대상 파일, 코드, 문서, 기능 범위를 구체적으로 지정하는 요소다.

Q. User Prompt의 Constraint는 뭐야?
A. 현재 작업에서 지켜야 할 조건과 제한사항이다.

Q. Output Request는 뭐야?
A. User Prompt에서 원하는 결과 형식과 포함 항목을 지정하는 요소다.

Q. User Prompt에서 Priority는 왜 필요해?
A. 여러 요구사항이 있을 때 무엇을 먼저 따라야 하는지 명확히 하기 위해 필요하다.

Q. Role Prompt와 Task Prompt 차이는 뭐야?
A. Role Prompt는 관점과 책임을 정하고, Task Prompt는 실제 수행할 작업을 정한다.

Q. Role만 있으면 왜 부족해?
A. 역할은 정해지지만 작업 기준과 출력 형식이 없어서 답변이 흔들릴 수 있다.

Q. Task만 있으면 왜 부족해?
A. 작업은 정해지지만 어떤 전문 관점으로 판단할지 부족할 수 있다.

Q. Prompt Layering이 뭐야?
A. System Prompt, Domain Rules, Retrieved Context, User Prompt, Output Format, Validation을 계층별로 분리하는 설계 방식이다.

Q. Prompt Layering은 왜 필요해?
A. 규칙 충돌을 줄이고 유지보수성과 재사용성을 높이기 위해 필요하다.

Q. Role Prompt에서 가장 흔한 실수는 뭐야?
A. 역할만 지정하고 책임, 범위, 검증 기준, 출력 형식을 생략하는 것이다.

Q. System Prompt에서 가장 흔한 실수는 뭐야?
A. 지속 규칙과 일회성 작업을 섞고, 너무 많은 규칙을 넣어 핵심이 흐려지는 것이다.

Q. User Prompt에서 가장 흔한 실수는 뭐야?
A. 작업 대상, 입력, 제약, 출력 형식을 명확히 쓰지 않는 것이다.

Q. Role Prompt Best Practice는 뭐야?
A. Role을 Responsibility, Scope, Expertise, Output Standard, Limitation과 함께 정의하는 것이다.

Q. System Prompt Best Practice는 뭐야?
A. 지속 규칙을 간결하게 유지하고, RAG Use Rule, Missing Information Rule, 출력 기준을 포함하는 것이다.

Q. User Prompt Best Practice는 뭐야?
A. Task, Input, Target, Context, Constraints, Output Request, Failure Rule을 명확히 작성하는 것이다.
