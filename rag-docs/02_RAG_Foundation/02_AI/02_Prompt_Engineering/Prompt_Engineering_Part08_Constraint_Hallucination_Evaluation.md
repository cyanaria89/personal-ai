# Prompt Engineering Part08 Constraint, Hallucination Prevention, Prompt Evaluation

---

# 1. Constraint Prompt

## 1.1 Constraint Prompt Definition

### [개념]

Constraint Prompt는 LLM이 반드시 지켜야 할 조건, 금지사항, 우선순위, 출력 제한을 정의하는 Prompt다.

Constraint는 모델의 자유도를 조절한다.

Constraint가 없으면 LLM은 일반 지식, 추정, 선호 방식으로 답변할 수 있다.

기본 구조:

```text
Must
→ Must Not
→ Prefer
→ Avoid
→ Version
→ Scope
→ Output Limit
→ Assumption Limit
```

Constraint Prompt의 목적은 프로젝트 규칙, 출력 형식, 보안 조건, RAG 근거 규칙을 안정적으로 지키게 만드는 것이다.

---

### [핵심]

- Constraint는 Prompt 품질을 결정한다.
- Must는 반드시 지켜야 하는 조건이다.
- Must Not은 금지 조건이다.
- Prefer는 선호 조건이다.
- Avoid는 피해야 할 방식이다.
- Version은 기술 버전 제약이다.
- Scope는 작업 범위 제약이다.
- Output Limit은 출력 길이와 형식 제약이다.
- Assumption Limit은 추정 허용 범위 제약이다.
- Constraint가 충돌하면 우선순위를 명시해야 한다.

---

### [실무]

2026 실무 기준 Constraint Prompt는 코드 생성, 코드 리뷰, RAG 답변, Agent Workflow에서 필수다.

예시:

```text
Constraints:

Must:
- Use retrieved documents first.
- Follow project architecture.
- Return Korean Markdown.
- Mark missing information clearly.

Must Not:
- Do not invent project-specific facts.
- Do not create missing class names as confirmed code.
- Do not expose secrets.
- Do not change existing API contracts unless requested.

Prefer:
- Use short code snippets.
- Use checklist format for review output.

Avoid:
- Avoid essay-style explanations.
- Avoid mixing assumptions with confirmed facts.
```

Constraint는 많을수록 좋은 것이 아니다.

핵심 조건은 Must로 고정하고, 선택 조건은 Prefer로 분리하는 것이 안정적이다.

---

### [FAQ]

Q. Constraint Prompt가 뭐야?

A. LLM이 반드시 지켜야 할 조건, 금지사항, 우선순위, 출력 제한을 정의하는 Prompt다.

Q. Constraint는 왜 필요해?

A. 모델이 프로젝트 규칙, 출력 형식, 보안 조건, 문서 근거 규칙을 지키도록 제어하기 위해 필요하다.

Q. Must와 Prefer는 어떻게 달라?

A. Must는 반드시 지켜야 하는 조건이고, Prefer는 가능하면 따르는 선호 조건이다.

Q. Constraint가 없으면 어떻게 돼?

A. 모델이 일반 지식이나 추정으로 답변해 프로젝트와 맞지 않는 결과를 만들 수 있다.

---

# 2. Constraint Types

## 2.1 Must Rule

### [개념]

Must Rule은 LLM이 반드시 지켜야 하는 필수 조건이다.

Must Rule은 프로젝트 규칙, 기술 버전, 출력 형식, 근거 사용 규칙처럼 절대적으로 필요한 조건에 사용한다.

---

### [핵심]

- Must Rule은 필수 조건이다.
- 핵심 프로젝트 규칙을 포함한다.
- 기술 버전 조건을 포함한다.
- 출력 형식 조건을 포함한다.
- RAG 문서 근거 우선 규칙을 포함한다.
- 보안 규칙을 포함할 수 있다.
- Must Rule은 Prefer보다 우선한다.

---

### [실무]

Must Rule 예시:

```text
Must:
- Use Java 21.
- Use Spring Boot 3.x.
- Follow Controller → Service → Repository architecture.
- Use retrieved documents first.
- Include Missing Information when context is insufficient.
- Return output in the requested Markdown format.
```

RAG 문서 제작 Must Rule 예시:

```text
Must:
- Apply MASTER_RAG_RULES.
- Apply DOMAIN_RULES.
- Include [개념], [핵심], [실무], [FAQ].
- Include Retrieval Queries.
- Optimize for retrieval.
```

Must Rule은 반드시 지켜야 하므로 너무 많이 넣지 않고 핵심 조건 중심으로 작성한다.

---

### [FAQ]

Q. Must Rule이 뭐야?

A. LLM이 반드시 지켜야 하는 필수 조건이다.

Q. Must Rule에는 무엇을 넣어야 해?

A. 프로젝트 규칙, 기술 버전, 출력 형식, RAG 근거 우선 규칙, 보안 규칙을 넣는다.

Q. Must Rule이 너무 많으면 문제야?

A. 그렇다. 너무 많으면 모델이 핵심 조건을 놓칠 수 있으므로 필수 조건 중심으로 작성해야 한다.

---

## 2.2 Must Not Rule

### [개념]

Must Not Rule은 LLM이 절대 하지 말아야 할 행동을 정의하는 금지 조건이다.

Must Not Rule은 Hallucination, 보안 문제, 형식 오류, 범위 초과를 줄이는 데 중요하다.

---

### [핵심]

- Must Not Rule은 금지 조건이다.
- 프로젝트 고유 정보 임의 생성을 막는다.
- 보안정보 노출을 막는다.
- API 계약 변경을 막는다.
- 출력 형식 위반을 막는다.
- 보이지 않는 코드 단정을 막는다.
- 범위 밖 작업을 막는다.

---

### [실무]

Must Not Rule 예시:

```text
Must Not:
- Do not invent missing classes.
- Do not invent API paths.
- Do not invent database columns.
- Do not expose secrets.
- Do not change existing method signatures unless requested.
- Do not claim unseen files are correct.
- Do not include extra text outside JSON when JSON is requested.
```

RAG Prompt Must Not Rule 예시:

```text
Must Not:
- Do not answer with unsupported project-specific facts.
- Do not override retrieved context with general knowledge.
- Do not treat assumptions as confirmed facts.
```

Must Not Rule은 Do Rule과 함께 사용해야 한다.

금지사항만 있으면 원하는 결과가 불명확해질 수 있다.

---

### [FAQ]

Q. Must Not Rule이 뭐야?

A. LLM이 절대 하지 말아야 할 행동을 정의하는 금지 조건이다.

Q. Must Not Rule은 언제 중요해?

A. 없는 정보 생성, 보안정보 노출, API 계약 변경, JSON 형식 오류, 범위 초과를 막을 때 중요하다.

Q. Must Not Rule만 있으면 충분해?

A. 아니다. 원하는 행동을 알려주는 Must Rule이나 Do Rule과 함께 사용해야 한다.

---

## 2.3 Prefer Rule

### [개념]

Prefer Rule은 가능하면 따르는 선호 조건이다.

Prefer Rule은 필수는 아니지만 출력 품질과 일관성을 높이는 데 사용한다.

---

### [핵심]

- Prefer Rule은 선택적 선호 조건이다.
- Must보다 우선순위가 낮다.
- 코드 스타일, 설명 길이, 출력 방식 선호를 표현한다.
- 충돌 시 Must Rule을 우선한다.
- Prefer를 Must처럼 쓰면 Constraint가 과도해질 수 있다.

---

### [실무]

Prefer Rule 예시:

```text
Prefer:
- Use short code snippets.
- Use bullet points.
- Use Markdown checklist for validation.
- Keep explanations concise.
- Prefer existing project conventions.
```

코드 리뷰 Prefer Rule 예시:

```text
Prefer:
- Focus on runtime risk first.
- Separate defects and style preferences.
- Provide fix direction with minimal code changes.
```

Prefer Rule은 결과 품질을 다듬는 보조 제약이다.

핵심 조건은 Must로 작성한다.

---

### [FAQ]

Q. Prefer Rule이 뭐야?

A. 반드시 지켜야 하는 조건은 아니지만 가능하면 따르는 선호 조건이다.

Q. Prefer와 Must가 충돌하면 뭘 따라야 해?

A. Must를 따라야 한다.

Q. Prefer Rule은 어디에 좋아?

A. 출력 스타일, 설명 길이, 코드 snippet 길이, 리뷰 우선순위 같은 선호사항에 좋다.

---

## 2.4 Avoid Rule

### [개념]

Avoid Rule은 가능하면 피해야 하는 방식이나 패턴을 정의하는 제약이다.

Avoid는 Must Not보다 약한 금지 조건이다.

---

### [핵심]

- Avoid는 피해야 할 경향을 제어한다.
- Must Not보다 강도가 낮다.
- 장문 설명, 과도한 추상화, 불필요한 코드 생성을 줄인다.
- RAG 문서에서는 에세이형 설명을 피하게 한다.
- 코드 생성에서는 불필요한 전체 파일 생성을 피하게 한다.

---

### [실무]

Avoid Rule 예시:

```text
Avoid:
- Avoid essay-style explanations.
- Avoid unnecessary boilerplate.
- Avoid changing unrelated files.
- Avoid broad refactoring unless requested.
- Avoid mixing multiple concepts in one section.
```

RAG 문서 Avoid Rule 예시:

```text
Avoid:
- Avoid long paragraphs.
- Avoid generic explanations without retrieval keywords.
- Avoid mixing Prompt Engineering and unrelated AI topics.
```

Avoid Rule은 출력 품질을 다듬는 데 유용하지만, 절대 금지는 Must Not으로 작성한다.

---

### [FAQ]

Q. Avoid Rule이 뭐야?

A. 가능하면 피해야 하는 방식이나 패턴을 정의하는 제약이다.

Q. Avoid와 Must Not은 어떻게 달라?

A. Must Not은 절대 금지이고, Avoid는 가능하면 피하라는 약한 제약이다.

Q. RAG 문서에서 Avoid Rule은 왜 필요해?

A. 장문 에세이, 일반론, 개념 혼합을 줄여 Retrieval 품질을 높이기 위해 필요하다.

---

# 3. Scope Constraint

## 3.1 Scope Constraint Definition

### [개념]

Scope Constraint는 LLM이 작업할 수 있는 범위와 작업하면 안 되는 범위를 정의하는 제약이다.

Scope Constraint는 범위 초과, 불필요한 코드 생성, Agent 책임 중복을 방지한다.

---

### [핵심]

- 작업 범위를 명확히 한다.
- 포함 범위와 제외 범위를 함께 작성한다.
- 변경 가능한 파일과 변경 금지 파일을 구분한다.
- Agent 역할 범위를 제한한다.
- Refactoring에서는 Scope Constraint가 필수다.
- Multi-Agent Workflow에서는 Agent 간 Scope가 겹치지 않아야 한다.

---

### [실무]

Scope Constraint 예시:

```text
Scope:
Included:
- Service layer
- Transaction boundary
- Exception handling
- DTO conversion

Excluded:
- Frontend code
- Database migration
- Deployment configuration
- External API policy
```

Refactoring Scope 예시:

```text
Scope:
- Refactor Service code only.
- Preserve Controller signature.
- Preserve Repository signature.
- Preserve API response structure.
- Do not add new business rules.
```

Scope Constraint는 LLM이 요청 범위를 넘어 전체 구조를 임의로 수정하는 것을 막는다.

---

### [FAQ]

Q. Scope Constraint가 뭐야?

A. LLM이 작업할 수 있는 범위와 작업하면 안 되는 범위를 정의하는 제약이다.

Q. Scope Constraint가 없으면 어떻게 돼?

A. 모델이 요청 범위를 넘어 불필요한 코드, 정책, 구조 변경을 만들 수 있다.

Q. Refactoring에서 Scope Constraint가 중요한 이유는 뭐야?

A. 기능 유지와 변경 범위를 명확히 해야 외부 동작이 바뀌지 않기 때문이다.

---

# 4. Version Constraint

## 4.1 Version Constraint Definition

### [개념]

Version Constraint는 LLM이 특정 기술 버전 기준으로 답변하도록 제한하는 제약이다.

기술 스택은 버전에 따라 API, 설정 방식, 권장 패턴이 달라질 수 있다.

---

### [핵심]

- 언어 버전을 명시한다.
- 프레임워크 버전을 명시한다.
- 라이브러리 버전을 명시한다.
- DB 버전을 명시할 수 있다.
- 런타임 환경을 명시할 수 있다.
- 버전이 없으면 오래된 방식이 생성될 수 있다.
- 최신 기술은 버전 차이가 크므로 중요하다.

---

### [실무]

Version Constraint 예시:

```text
Version:
- Java 21
- Spring Boot 3.x
- Spring Security 6.x
- Spring Data JPA
- MySQL 8.x
```

Frontend Version Constraint 예시:

```text
Version:
- React 19
- TypeScript
- Vite
- React Router
```

AI Agent Version Constraint 예시:

```text
Version:
- Modern LLM
- RAG-based Prompt
- Agent Workflow
- Structured Output
- Tool Calling compatible
```

Version Constraint는 코드 생성, 설정, 디버깅, 라이브러리 사용법 답변에 중요하다.

---

### [FAQ]

Q. Version Constraint가 뭐야?

A. LLM이 특정 언어, 프레임워크, 라이브러리 버전 기준으로 답변하도록 제한하는 제약이다.

Q. 버전을 꼭 적어야 해?

A. 코드 생성, 설정, 디버깅에서는 적는 것이 좋다.

Q. 버전이 없으면 어떤 문제가 생겨?

A. 오래된 API, 다른 설정 방식, 프로젝트와 맞지 않는 코드가 생성될 수 있다.

---

# 5. Output Constraint

## 5.1 Output Constraint Definition

### [개념]

Output Constraint는 LLM의 최종 출력 형식, 길이, 포함 항목, 제외 항목을 제한하는 제약이다.

Output Constraint는 Structured Output과 연결된다.

---

### [핵심]

- 출력 형식을 지정한다.
- 필수 섹션을 지정한다.
- 출력 길이를 제한한다.
- JSON 출력 시 부가 설명을 금지한다.
- Markdown Header 계층을 고정한다.
- Code Block 사용 기준을 정한다.
- 후속 Agent가 처리 가능한 구조로 제한한다.

---

### [실무]

Markdown Output Constraint 예시:

```text
Output Constraint:
- Return Markdown.
- Use exactly these sections:
  - Summary
  - Findings
  - Missing Information
  - Fix Direction
  - Checklist
- Do not add unrelated sections.
```

JSON Output Constraint 예시:

```text
Output Constraint:
- Return only valid JSON.
- Do not include Markdown.
- Do not include explanation outside JSON.
- Use double quotes.
- Do not use trailing commas.
```

RAG 문서 Output Constraint 예시:

```text
Output Constraint:
- Use [개념], [핵심], [실무], [FAQ].
- Include Retrieval Queries.
- Do not use essay-style long paragraphs.
- Keep chunks independently searchable.
```

Output Constraint가 명확할수록 후속 Agent 처리 안정성이 높아진다.

---

### [FAQ]

Q. Output Constraint가 뭐야?

A. LLM의 최종 출력 형식, 길이, 포함 항목, 제외 항목을 제한하는 제약이다.

Q. Output Constraint는 왜 중요해?

A. 결과 형식이 안정되어 사람이 읽거나 후속 Agent가 처리하기 쉬워지기 때문이다.

Q. JSON Output Constraint에서 중요한 것은 뭐야?

A. 유효한 JSON만 출력하고 Markdown이나 부가 설명을 섞지 않도록 제한하는 것이다.

---

# 6. Assumption Constraint

## 6.1 Assumption Constraint Definition

### [개념]

Assumption Constraint는 LLM이 어떤 상황에서 가정을 허용하고, 어떤 방식으로 표시해야 하는지 제한하는 제약이다.

Assumption은 확정 사실이 아니다.

Assumption Constraint는 Hallucination 방지에 중요하다.

---

### [핵심]

- Assumption은 명확히 표시한다.
- 확정 사실과 Assumption을 분리한다.
- 프로젝트 고유 정보는 임의로 가정하지 않는다.
- 클래스명, API 경로, DB 컬럼은 확정하지 않는다.
- 필요한 경우 Assumptions 섹션을 따로 둔다.
- Assumption이 많으면 Missing Information을 표시한다.

---

### [실무]

Assumption Constraint 예시:

```text
Assumption Constraint:
- Mark all assumptions clearly.
- Do not present assumptions as confirmed facts.
- Do not invent project-specific class names, API paths, database columns, or policies.
- If assumptions are required, place them under Assumptions.
```

RAG Answer Output 예시:

```md
## Confirmed by Context

## Assumptions

## Missing Information

## Final Answer
```

Assumption Constraint는 RAG 답변, 코드 생성, 코드 리뷰, Agent Handoff에서 필수다.

---

### [FAQ]

Q. Assumption Constraint가 뭐야?

A. LLM이 어떤 상황에서 가정을 허용하고 어떻게 표시해야 하는지 제한하는 제약이다.

Q. Assumption은 확정 사실이야?

A. 아니다. Assumption은 작업 진행을 위한 임시 전제이며 확정 사실과 분리해야 한다.

Q. 프로젝트 고유 정보를 Assumption으로 만들어도 돼?

A. 확정하면 안 된다. 필요하면 예시 또는 가정으로 분리하고 Missing Information을 표시해야 한다.

---

# 7. Hallucination Prevention

## 7.1 Hallucination Prevention Definition

### [개념]

Hallucination Prevention은 LLM이 근거 없는 정보, 존재하지 않는 프로젝트 구조, 잘못된 코드, 없는 정책을 만들어내지 않도록 제어하는 Prompt 설계 방식이다.

Hallucination은 RAG, 코드 생성, 코드 리뷰, Agent Workflow에서 치명적이다.

기본 구조:

```text
Grounding
→ Source Context
→ Missing Information
→ Assumption
→ Verification
→ Safe Output
```

---

### [핵심]

- 문서에 없는 내용을 확정하지 않는다.
- 프로젝트 고유 정보를 임의 생성하지 않는다.
- 검색 문서를 일반 지식보다 우선한다.
- 확정 사실과 추정을 분리한다.
- 부족한 정보는 Missing Information으로 표시한다.
- 보이지 않는 코드는 단정하지 않는다.
- 검증 가능한 항목은 Verification Step으로 확인한다.
- Tool 결과를 임의로 확장하지 않는다.

---

### [실무]

Hallucination Prevention Prompt 예시:

```text
Hallucination Prevention:
- Use provided context first.
- Do not invent project-specific facts.
- If context does not contain the answer, say the context is insufficient.
- Clearly separate confirmed facts, assumptions, and missing information.
- Do not claim unseen files are correct.
```

Code Generation 방지 규칙:

```text
Do not create class names, method names, API paths, database columns, or business rules that are not provided.
If needed, propose them as assumptions, not confirmed project code.
```

Hallucination Prevention은 답변을 줄이는 것이 아니라, 근거 없는 확정을 막는 것이다.

---

### [FAQ]

Q. Hallucination Prevention이 뭐야?

A. LLM이 근거 없는 정보나 존재하지 않는 프로젝트 구조를 만들어내지 않도록 제어하는 Prompt 설계 방식이다.

Q. Hallucination은 왜 위험해?

A. 실제 프로젝트에 없는 클래스, API, DB 필드, 정책을 사실처럼 만들어 잘못된 구현을 유도할 수 있기 때문이다.

Q. Hallucination을 줄이는 핵심 규칙은 뭐야?

A. 문서 근거 우선, Missing Information 표시, Assumption 분리, 보이지 않는 코드 단정 금지다.

---

# 8. Grounding Rule

## 8.1 Grounding Rule Definition

### [개념]

Grounding Rule은 LLM 답변이 제공된 Context, RAG 문서, 코드, Tool 결과에 근거하도록 만드는 규칙이다.

Grounding은 RAG 답변의 핵심이다.

---

### [핵심]

- 제공된 Context를 우선 사용한다.
- RAG 문서를 우선 사용한다.
- Tool 결과를 확인된 사실로 사용한다.
- 일반 지식과 근거 기반 답변을 구분한다.
- 근거 없는 확정 표현을 피한다.
- 출처가 불충분하면 Missing Information을 표시한다.

---

### [실무]

Grounding Rule 예시:

```text
Grounding Rule:
- Answer based on provided context.
- Use retrieved documents as primary evidence.
- Do not override retrieved context with general knowledge.
- If evidence is insufficient, state what is missing.
```

Grounded Output 구조:

```md
## Confirmed by Context

## Evidence

## Assumptions

## Missing Information

## Final Answer
```

Grounding Rule은 RAG Agent, Review Agent, Code Generation Agent 모두에 적용 가능하다.

---

### [FAQ]

Q. Grounding Rule이 뭐야?

A. LLM 답변이 제공된 Context, RAG 문서, 코드, Tool 결과에 근거하도록 만드는 규칙이다.

Q. Grounding이 중요한 이유는 뭐야?

A. 근거 없는 답변과 Hallucination을 줄이기 위해 중요하다.

Q. 일반 지식은 사용하면 안 돼?

A. 사용할 수 있지만, 프로젝트 문서 근거와 일반 추론을 구분해야 한다.

---

# 9. Missing Information Rule

## 9.1 Missing Information Rule Definition

### [개념]

Missing Information Rule은 필요한 정보가 부족할 때 LLM이 지어내지 않고 부족한 정보를 표시하도록 하는 규칙이다.

Missing Information Rule은 RAG Prompt, Code Generation Prompt, Code Review Prompt, Agent Prompt에서 필수다.

---

### [핵심]

- 필요한 정보가 없으면 부족하다고 표시한다.
- 없는 클래스명, API 경로, DB 컬럼을 만들지 않는다.
- 보이지 않는 코드는 단정하지 않는다.
- 검색 문서에 답이 없으면 없다고 말한다.
- 안전한 범위에서는 부분 답변을 제공할 수 있다.
- Missing Information은 별도 섹션으로 분리한다.

---

### [실무]

Missing Information Rule 예시:

```text
If required information is missing:
- State what is missing.
- Do not invent missing details.
- Provide partial output only if safe.
- Mark assumptions clearly.
```

Code Review 예시:

```text
If only partial code is provided:
- Review only visible code.
- Do not make claims about unseen layers.
- List additional files needed for full review.
```

RAG 문서 답변 예시:

```md
## Missing Information

- Repository method signatures are not provided.
- Entity fields are not provided.
- SecurityConfig is not provided.
```

Missing Information Rule은 “모르는 것을 모른다고 말하게 하는 규칙”이다.

---

### [FAQ]

Q. Missing Information Rule이 뭐야?

A. 필요한 정보가 부족할 때 지어내지 않고 부족한 정보를 명확히 표시하도록 하는 규칙이다.

Q. Missing Information Rule은 왜 중요해?

A. 모델이 없는 정보를 만들어내는 Hallucination을 줄이기 위해 중요하다.

Q. 정보가 부족하면 답변을 멈춰야 해?

A. 안전한 범위에서는 부분 답변을 제공하고 한계를 명확히 표시할 수 있다.

---

# 10. Assumption Rule

## 10.1 Assumption Rule Definition

### [개념]

Assumption Rule은 작업을 진행하기 위해 필요한 가정을 어떻게 표시할지 정의하는 규칙이다.

Assumption은 확정된 사실이 아니다.

Assumption Rule은 확정 정보와 추정을 분리해 잘못된 결론을 줄인다.

---

### [핵심]

- Assumption은 별도 섹션으로 표시한다.
- Confirmed Fact와 섞지 않는다.
- 프로젝트 고유 정보는 임의 가정하지 않는다.
- 필요한 경우 예시로만 제안한다.
- Assumption이 많으면 추가 Context가 필요하다.
- Review Agent는 Assumption을 검증 대상에 포함해야 한다.

---

### [실무]

Assumption Rule 예시:

```text
Assumption Rule:
- If a detail is not confirmed by context, mark it as Assumption.
- Do not present assumptions as confirmed facts.
- Do not implement assumptions as final project code unless confirmed.
```

Output 예시:

```md
## Confirmed Facts

- Controller returns ApiResponse<T>.

## Assumptions

- UserRepository method names are examples and must be adjusted to actual code.

## Missing Information

- Actual UserRepository interface is not provided.
```

Assumption Rule은 Code Generation과 Agent Handoff에서 특히 중요하다.

---

### [FAQ]

Q. Assumption Rule이 뭐야?

A. 작업 진행을 위해 필요한 가정을 어떻게 표시할지 정의하는 규칙이다.

Q. Assumption과 Missing Information은 어떻게 달라?

A. Missing Information은 부족한 정보이고, Assumption은 그 부족한 정보를 임시로 전제한 것이다.

Q. Assumption을 최종 코드처럼 사용해도 돼?

A. 확정 정보가 아니므로 최종 코드처럼 사용하면 안 된다.

---

# 11. Verification Rule

## 11.1 Verification Rule Definition

### [개념]

Verification Rule은 LLM이 최종 출력 전에 답변이 근거, 형식, 제약을 만족하는지 확인하도록 하는 규칙이다.

Verification은 Hallucination Prevention의 마지막 단계다.

---

### [핵심]

- 최종 출력 전 근거를 확인한다.
- Missing Information이 필요한지 확인한다.
- Assumption이 명확히 표시되었는지 확인한다.
- Output Format을 확인한다.
- Constraint 위반이 없는지 확인한다.
- JSON은 유효한지 확인한다.
- RAG 문서는 필수 섹션과 Retrieval Queries를 확인한다.

---

### [실무]

Verification Rule 예시:

```text
Before final output, verify:
- Claims are grounded in provided context.
- Assumptions are clearly marked.
- Missing information is stated.
- Constraints are followed.
- Output format is valid.
```

RAG Document Verification 예시:

```text
Verify:
- [개념], [핵심], [실무], [FAQ] exist.
- Retrieval Queries exist.
- FAQ uses Q + A.
- Terms are consistent.
- Content is retrieval-friendly.
```

Verification Rule은 내부 검수에 사용하고, 사용자가 요청하지 않으면 검수 과정 자체는 출력하지 않는다.

---

### [FAQ]

Q. Verification Rule이 뭐야?

A. 최종 출력 전에 답변이 근거, 형식, 제약을 만족하는지 확인하도록 하는 규칙이다.

Q. Verification은 왜 필요해?

A. 형식 누락, 제약 위반, 근거 없는 확정, Missing Information 누락을 줄이기 위해 필요하다.

Q. Verification 과정을 항상 출력해야 해?

A. 아니다. 사용자가 요청하지 않으면 내부 검수만 수행하고 최종 결과만 출력하는 것이 좋다.

---

# 12. Prompt Evaluation

## 12.1 Prompt Evaluation Definition

### [개념]

Prompt Evaluation은 Prompt가 원하는 품질의 결과를 안정적으로 생성하는지 평가하는 과정이다.

Prompt는 한 번 작성하면 끝나는 것이 아니다.

출력 결과를 기준으로 평가하고 개선해야 한다.

기본 Flow:

```text
Prompt
→ Output
→ Accuracy Check
→ Format Check
→ Groundedness Check
→ Missing Information Check
→ Revision
→ Retest
```

---

### [핵심]

- Prompt Evaluation은 Prompt 품질 개선에 필요하다.
- Accuracy를 평가한다.
- Completeness를 평가한다.
- Format Compliance를 평가한다.
- Groundedness를 평가한다.
- Consistency를 평가한다.
- Reusability를 평가한다.
- Failure Handling을 평가한다.
- 평가 결과를 Prompt Iteration에 반영한다.

---

### [실무]

Prompt Evaluation Checklist:

```md
### [Checklist]

- [ ] 답변이 Task를 해결했는가?
- [ ] 필요한 Context를 사용했는가?
- [ ] 문서 근거와 추정을 구분했는가?
- [ ] Missing Information을 표시했는가?
- [ ] 출력 형식을 지켰는가?
- [ ] 불필요한 정보가 없는가?
- [ ] 후속 Agent가 처리 가능한 구조인가?
- [ ] 반복 실행해도 형식이 안정적인가?
```

Prompt Evaluation은 Prompt 자체가 아니라 Prompt가 만든 Output을 기준으로 수행한다.

---

### [FAQ]

Q. Prompt Evaluation이 뭐야?

A. Prompt가 원하는 품질의 결과를 안정적으로 생성하는지 평가하는 과정이다.

Q. Prompt는 한 번 만들면 끝이야?

A. 아니다. 출력 결과를 평가하고 실패 유형을 반영해 반복 개선해야 한다.

Q. Prompt Evaluation은 무엇을 기준으로 해?

A. Accuracy, Completeness, Format Compliance, Groundedness, Consistency, Reusability, Failure Handling을 기준으로 한다.

---

# 13. Prompt Evaluation Criteria

## 13.1 Accuracy

### [개념]

Accuracy는 Prompt 결과가 사실과 요구사항에 맞는지 평가하는 기준이다.

Accuracy는 답변의 정확성, 코드 정합성, 문서 근거 일치 여부를 확인한다.

---

### [핵심]

- 사용자 Task를 정확히 해결했는지 확인한다.
- 제공된 Context와 일치하는지 확인한다.
- 프로젝트 규칙과 맞는지 확인한다.
- 코드가 기술 스택과 맞는지 확인한다.
- 잘못된 사실이 없는지 확인한다.
- 일반 지식으로 문서 근거를 덮어쓰지 않았는지 확인한다.

---

### [실무]

Accuracy Evaluation 예시:

```md
### [Accuracy Checklist]

- [ ] 사용자 요청을 정확히 반영했는가?
- [ ] 프로젝트 Context와 충돌하지 않는가?
- [ ] 기술 버전 기준이 맞는가?
- [ ] 문서에 없는 내용을 확정하지 않았는가?
- [ ] 코드 예시가 기존 구조와 맞는가?
```

Accuracy가 낮으면 Context, Constraint, Grounding Rule을 강화해야 한다.

---

### [FAQ]

Q. Accuracy는 뭐야?

A. Prompt 결과가 사실, 요구사항, 프로젝트 규칙에 맞는지 평가하는 기준이다.

Q. Accuracy가 낮으면 어떻게 개선해?

A. Context를 보강하고 Constraint, Grounding Rule, Missing Information Rule을 강화해야 한다.

---

## 13.2 Completeness

### [개념]

Completeness는 Prompt 결과가 필요한 내용을 빠짐없이 포함했는지 평가하는 기준이다.

Completeness는 필수 섹션, 필수 필드, 필수 검토 항목 포함 여부를 확인한다.

---

### [핵심]

- Task의 모든 요구사항을 포함했는지 확인한다.
- 필수 섹션이 누락되지 않았는지 확인한다.
- Required Field가 포함되었는지 확인한다.
- Review Criteria가 모두 적용되었는지 확인한다.
- Retrieval Queries가 포함되었는지 확인한다.
- Missing Information이 필요한 경우 표시되었는지 확인한다.

---

### [실무]

Completeness Evaluation 예시:

```md
### [Completeness Checklist]

- [ ] Task의 모든 요구사항이 반영되었는가?
- [ ] 필수 섹션이 모두 포함되었는가?
- [ ] 필수 검토 기준이 모두 적용되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
- [ ] Missing Information이 필요한 경우 누락되지 않았는가?
```

Completeness가 낮으면 Output Format과 Checklist를 강화한다.

---

### [FAQ]

Q. Completeness는 뭐야?

A. Prompt 결과가 필요한 내용을 빠짐없이 포함했는지 평가하는 기준이다.

Q. Completeness가 낮으면 어떻게 개선해?

A. 필수 섹션, 필수 필드, Review Criteria, Checklist를 Prompt에 명확히 추가해야 한다.

---

## 13.3 Format Compliance

### [개념]

Format Compliance는 Prompt 결과가 요청한 출력 형식과 Schema를 지켰는지 평가하는 기준이다.

Structured Output에서는 Format Compliance가 핵심이다.

---

### [핵심]

- Markdown Header 구조를 확인한다.
- JSON 유효성을 확인한다.
- 필드명이 일관적인지 확인한다.
- 필수 섹션이 있는지 확인한다.
- FAQ가 Q + A 구조인지 확인한다.
- 코드블록 형식이 맞는지 확인한다.
- 불필요한 부가 설명이 없는지 확인한다.

---

### [실무]

Format Compliance Evaluation 예시:

```md
### [Format Compliance Checklist]

- [ ] 요청한 Output Format을 지켰는가?
- [ ] 필수 섹션이 누락되지 않았는가?
- [ ] Header 계층이 일관적인가?
- [ ] JSON이 유효한가?
- [ ] 필드명이 고정 Schema와 일치하는가?
- [ ] 불필요한 설명이 섞이지 않았는가?
```

Format Compliance가 낮으면 Fixed Schema, Few-Shot Example, Output Constraint를 강화한다.

---

### [FAQ]

Q. Format Compliance는 뭐야?

A. Prompt 결과가 요청한 출력 형식과 Schema를 지켰는지 평가하는 기준이다.

Q. Format Compliance가 낮으면 어떻게 개선해?

A. Fixed Schema, 예시 출력, Output Constraint를 추가해야 한다.

---

## 13.4 Groundedness

### [개념]

Groundedness는 Prompt 결과가 제공된 Context, RAG 문서, Tool 결과에 근거하고 있는지 평가하는 기준이다.

Groundedness는 RAG 답변과 Agent Workflow에서 중요하다.

---

### [핵심]

- 제공된 Context를 사용했는지 확인한다.
- RAG 문서 근거와 일치하는지 확인한다.
- Tool 결과를 왜곡하지 않았는지 확인한다.
- 일반 지식과 문서 근거를 구분했는지 확인한다.
- 근거 없는 확정 표현이 없는지 확인한다.
- Assumption이 명확히 표시되었는지 확인한다.

---

### [실무]

Groundedness Evaluation 예시:

```md
### [Groundedness Checklist]

- [ ] Retrieved Context를 우선 사용했는가?
- [ ] 문서에 없는 내용을 확정하지 않았는가?
- [ ] Assumption을 분리했는가?
- [ ] Missing Information을 표시했는가?
- [ ] 일반 지식과 문서 근거를 구분했는가?
```

Groundedness가 낮으면 RAG Use Rule, Missing Information Rule, Assumption Rule을 강화해야 한다.

---

### [FAQ]

Q. Groundedness는 뭐야?

A. Prompt 결과가 제공된 Context, RAG 문서, Tool 결과에 근거하고 있는지 평가하는 기준이다.

Q. Groundedness가 낮으면 어떤 문제가 생겨?

A. Hallucination, 프로젝트와 맞지 않는 답변, 없는 정보 확정 문제가 발생할 수 있다.

Q. Groundedness를 높이려면 어떻게 해?

A. RAG Use Rule, Missing Information Rule, Assumption Rule, Source Priority를 Prompt에 포함해야 한다.

---

## 13.5 Consistency

### [개념]

Consistency는 Prompt 결과가 반복 실행 시 같은 구조와 유사한 품질로 생성되는지 평가하는 기준이다.

Consistency는 반복 작업과 Agent Workflow에서 중요하다.

---

### [핵심]

- 출력 구조가 반복적으로 유지되는지 확인한다.
- 필드명이 일관적인지 확인한다.
- 용어가 통일되었는지 확인한다.
- 판단 기준이 흔들리지 않는지 확인한다.
- Agent Handoff 구조가 유지되는지 확인한다.
- FAQ와 Retrieval Queries 표현이 일관적인지 확인한다.

---

### [실무]

Consistency Evaluation 예시:

```md
### [Consistency Checklist]

- [ ] 같은 Prompt에서 출력 구조가 유지되는가?
- [ ] 필드명이 반복 실행마다 동일한가?
- [ ] 용어가 문서 전체에서 통일되었는가?
- [ ] Review Severity 기준이 일관적인가?
- [ ] Handoff Schema가 유지되는가?
```

Consistency가 낮으면 Output Format, Fixed Schema, Few-Shot Prompt를 강화한다.

---

### [FAQ]

Q. Consistency는 뭐야?

A. Prompt 결과가 반복 실행 시 같은 구조와 유사한 품질로 생성되는지 평가하는 기준이다.

Q. Consistency가 낮으면 어떻게 개선해?

A. Fixed Schema, Few-Shot Example, 용어 규칙, Output Constraint를 추가해야 한다.

---

## 13.6 Reusability

### [개념]

Reusability는 Prompt가 반복 작업이나 유사 작업에 재사용 가능한지 평가하는 기준이다.

재사용 가능한 Prompt는 Template으로 관리할 수 있다.

---

### [핵심]

- Placeholder를 사용할 수 있는지 확인한다.
- 고정 규칙과 동적 Context가 분리되었는지 확인한다.
- 특정 사례에 과도하게 묶이지 않았는지 확인한다.
- Agent별로 재사용 가능한지 확인한다.
- Output Schema가 안정적인지 확인한다.
- 유지보수가 쉬운지 확인한다.

---

### [실무]

Reusable Prompt 구조:

```text
Role:
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
{failure_rule}
```

Reusability가 낮으면 Prompt Template으로 분리하고 Placeholder를 명확히 정의한다.

---

### [FAQ]

Q. Reusability는 뭐야?

A. Prompt가 반복 작업이나 유사 작업에 재사용 가능한지 평가하는 기준이다.

Q. Reusability를 높이려면 어떻게 해?

A. Placeholder를 사용하고 고정 규칙과 동적 Context를 분리해야 한다.

---

## 13.7 Failure Handling

### [개념]

Failure Handling은 Prompt 결과가 정보 부족, 도구 실패, Context 부족, 형식 불가능 상황에 적절히 대응하는지 평가하는 기준이다.

---

### [핵심]

- 정보 부족 시 Missing Information을 표시했는지 확인한다.
- Tool 실패 시 결과를 지어내지 않았는지 확인한다.
- Context 부족 시 한계를 표시했는지 확인한다.
- 안전한 부분 답변을 제공했는지 확인한다.
- 불가능한 작업을 가능하다고 말하지 않았는지 확인한다.
- Failure Rule이 출력에 반영되었는지 확인한다.

---

### [실무]

Failure Handling Evaluation 예시:

```md
### [Failure Handling Checklist]

- [ ] 정보 부족을 표시했는가?
- [ ] Tool 결과를 지어내지 않았는가?
- [ ] 보이지 않는 코드를 단정하지 않았는가?
- [ ] 안전한 범위에서 부분 답변을 제공했는가?
- [ ] 추가로 필요한 정보를 명확히 표시했는가?
```

Failure Handling이 낮으면 Failure Rule과 Missing Information Rule을 강화한다.

---

### [FAQ]

Q. Failure Handling은 뭐야?

A. 정보 부족, 도구 실패, Context 부족, 형식 불가능 상황에 적절히 대응하는지 평가하는 기준이다.

Q. Failure Handling이 낮으면 어떻게 개선해?

A. Failure Rule, Missing Information Rule, Assumption Rule을 Prompt에 명확히 추가해야 한다.

---

# 14. Prompt Evaluation Pattern

## 14.1 Prompt Evaluation Checklist Pattern

### [개념]

Prompt Evaluation Checklist Pattern은 Prompt 결과를 반복 검수하기 위한 고정 Checklist 패턴이다.

Review Agent가 Prompt 또는 Output을 평가할 때 사용할 수 있다.

---

### [핵심]

평가 항목:

- Accuracy
- Completeness
- Format Compliance
- Groundedness
- Consistency
- Reusability
- Failure Handling
- Constraint Compliance
- Output Stability

---

### [실무]

Prompt Evaluation Output 예시:

```md
## Evaluation Summary

## Scores

| Criteria          | Score | Notes |
| ----------------- | ----: | ----- |
| Accuracy          |   0-5 |       |
| Completeness      |   0-5 |       |
| Format Compliance |   0-5 |       |
| Groundedness      |   0-5 |       |
| Consistency       |   0-5 |       |
| Failure Handling  |   0-5 |       |

## Findings

### 1. Issue

- Criteria:
- Severity:
- Cause:
- Fix Direction:

## Revised Prompt Direction
```

Evaluation 결과는 Prompt Iteration의 입력으로 사용한다.

---

### [FAQ]

Q. Prompt Evaluation Checklist Pattern이 뭐야?

A. Prompt 결과를 Accuracy, Completeness, Format Compliance, Groundedness 등 기준으로 반복 검수하는 패턴이다.

Q. Prompt Evaluation 결과는 어디에 사용해?

A. Prompt Iteration에서 실패 유형을 반영해 Prompt를 개선하는 데 사용한다.

---

# 15. Common Mistakes

## 15.1 Constraint Mistakes

### [개념]

Constraint Mistake는 제약이 없거나, 너무 많거나, 서로 충돌해 LLM 출력이 불안정해지는 문제다.

---

### [핵심]

자주 발생하는 실수:

- Must와 Prefer를 구분하지 않음
- Must Not만 나열하고 원하는 결과를 쓰지 않음
- 충돌하는 제약 작성
- 기술 버전 미작성
- Scope 미작성
- Output Constraint 없음
- Assumption Constraint 없음
- 제약이 너무 많아 핵심이 흐려짐

---

### [실무]

나쁜 Constraint:

```text
잘 만들고, 짧게 쓰고, 자세히 설명하고, 필요한 건 알아서 추가해줘.
```

개선 Constraint:

```text
Must:
- Follow provided project context.
- Return Markdown with required sections.
- State missing information.

Must Not:
- Do not invent project-specific facts.
- Do not change API contract.

Prefer:
- Keep explanations concise.
```

Constraint는 명확하고 충돌이 없어야 한다.

---

### [FAQ]

Q. Constraint에서 가장 흔한 실수는 뭐야?

A. Must와 Prefer를 구분하지 않거나 서로 충돌하는 제약을 작성하는 것이다.

Q. Must Not만 많이 쓰면 왜 문제야?

A. 금지사항은 많지만 원하는 출력이 불명확해질 수 있기 때문이다.

---

## 15.2 Hallucination Prevention Mistakes

### [개념]

Hallucination Prevention Mistake는 근거 우선 규칙, Missing Information Rule, Assumption Rule이 없어 모델이 없는 정보를 확정하는 문제다.

---

### [핵심]

자주 발생하는 실수:

- RAG 문서 우선 규칙 없음
- Missing Information Rule 없음
- Assumption Rule 없음
- 일반 지식으로 프로젝트 문서 덮어쓰기
- 보이지 않는 코드 단정
- Tool 결과를 임의 확장
- 프로젝트 고유 정보 임의 생성
- 검증 단계 없음

---

### [실무]

나쁜 Prompt:

```text
문서 참고해서 알아서 답해줘.
```

개선 Prompt:

```text
Use retrieved documents first.
If the retrieved context is insufficient, state missing information.
Do not invent project-specific facts.
Separate confirmed facts, assumptions, and missing information.
```

Hallucination Prevention은 RAG Agent와 Code Generation Agent의 핵심 안전장치다.

---

### [FAQ]

Q. Hallucination Prevention에서 가장 흔한 실수는 뭐야?

A. 문서 근거 우선 규칙과 Missing Information Rule 없이 답변을 요구하는 것이다.

Q. 일반 지식으로 보완하면 안 돼?

A. 가능하지만 프로젝트 고유 정보는 문서 근거와 일반 추론을 반드시 구분해야 한다.

---

## 15.3 Prompt Evaluation Mistakes

### [개념]

Prompt Evaluation Mistake는 출력 결과를 평가하지 않고 Prompt를 반복 사용해 실패 패턴이 누적되는 문제다.

---

### [핵심]

자주 발생하는 실수:

- Prompt를 한 번 작성하고 고정함
- 출력 형식 실패를 검토하지 않음
- Hallucination 여부를 확인하지 않음
- Missing Information 누락을 확인하지 않음
- 평가 기준이 없음
- 실패 원인을 Prompt에 반영하지 않음
- 재사용성을 검토하지 않음

---

### [실무]

나쁜 운영 방식:

```text
Prompt 작성
→ 출력 확인 안 함
→ 반복 사용
→ 같은 오류 반복
```

개선 운영 방식:

```text
Prompt 작성
→ Output 평가
→ 실패 유형 분류
→ Constraint / Example / Format 수정
→ Retest
→ Template화
```

Prompt Evaluation은 Prompt 품질을 지속적으로 높이는 운영 과정이다.

---

### [FAQ]

Q. Prompt Evaluation에서 가장 흔한 실수는 뭐야?

A. 출력 결과를 평가하지 않고 Prompt를 그대로 반복 사용하는 것이다.

Q. Prompt 실패를 어떻게 개선해?

A. 실패 유형을 분석하고 Constraint, Context, Output Format, Few-Shot Example을 보강해야 한다.

---

# 16. Best Practice

## 16.1 Constraint Best Practice

### [개념]

Constraint Best Practice는 LLM이 반드시 지켜야 할 조건과 선호 조건을 명확히 분리해 안정적인 출력을 유도하는 원칙이다.

---

### [핵심]

- Must, Must Not, Prefer, Avoid를 분리한다.
- 기술 버전과 프로젝트 규칙을 명시한다.
- Scope를 제한한다.
- Output Format을 고정한다.
- Assumption 허용 범위를 제한한다.
- 충돌하는 제약을 제거한다.
- 제약은 핵심 조건 중심으로 작성한다.
- 제약이 많으면 우선순위를 지정한다.

---

### [실무]

Constraint Template:

```text
Constraints:

Must:
- [Required rule]

Must Not:
- [Forbidden rule]

Prefer:
- [Preferred style or approach]

Avoid:
- [Pattern to avoid]

Scope:
- [Included scope]
- [Excluded scope]

Output:
- [Required output format]

Assumption:
- Mark assumptions clearly.
- Do not present assumptions as confirmed facts.
```

이 Template은 Code Generation, Code Review, RAG Answer, Agent Prompt에 공통 적용 가능하다.

---

### [FAQ]

Q. Constraint Best Practice는 뭐야?

A. Must, Must Not, Prefer, Avoid, Scope, Output, Assumption 제약을 분리해 명확히 작성하는 것이다.

Q. Constraint에서 가장 중요한 것은 뭐야?

A. 필수 조건과 선호 조건을 구분하고, 충돌하지 않게 작성하는 것이다.

---

## 16.2 Hallucination Prevention Best Practice

### [개념]

Hallucination Prevention Best Practice는 LLM이 근거 없는 프로젝트 정보를 확정하지 않도록 Grounding, Missing Information, Assumption, Verification을 함께 사용하는 원칙이다.

---

### [핵심]

- Retrieved Context를 우선 사용한다.
- 제공된 코드와 문서를 근거로 답변한다.
- 문서에 없는 내용은 Missing Information으로 표시한다.
- Assumption은 별도 섹션으로 분리한다.
- 프로젝트 고유 정보는 임의 생성하지 않는다.
- 보이지 않는 코드는 단정하지 않는다.
- Tool 결과를 지어내지 않는다.
- 최종 출력 전 Verification을 수행한다.

---

### [실무]

Hallucination Prevention Template:

```text
Grounding:
- Use provided context and retrieved documents first.

Missing Information:
- If required information is missing, state it clearly.

Assumption:
- Mark assumptions separately.
- Do not present assumptions as facts.

Do Not:
- Do not invent project-specific facts.
- Do not claim unseen files are correct.
- Do not create missing API paths or DB columns.

Verification:
- Check groundedness before final output.
```

이 Template은 RAG 기반 Agent의 기본 안전 규칙으로 사용할 수 있다.

---

### [FAQ]

Q. Hallucination Prevention Best Practice는 뭐야?

A. Grounding, Missing Information, Assumption, Verification을 함께 사용해 근거 없는 확정을 막는 것이다.

Q. Hallucination을 줄이는 가장 중요한 방법은 뭐야?

A. 문서 근거 우선 규칙과 Missing Information Rule을 Prompt에 명확히 넣는 것이다.

---

## 16.3 Prompt Evaluation Best Practice

### [개념]

Prompt Evaluation Best Practice는 Prompt 결과를 기준에 따라 평가하고 실패 유형을 Prompt 개선에 반영하는 원칙이다.

---

### [핵심]

- 출력 결과를 기준으로 평가한다.
- Accuracy를 확인한다.
- Completeness를 확인한다.
- Format Compliance를 확인한다.
- Groundedness를 확인한다.
- Consistency를 확인한다.
- Failure Handling을 확인한다.
- 실패 유형을 기록한다.
- Prompt를 수정하고 다시 테스트한다.
- 안정화된 Prompt는 Template화한다.

---

### [실무]

Prompt Evaluation Template:

```md
## Prompt Evaluation

### Target Prompt

### Output Sample

### Evaluation

- Accuracy:
- Completeness:
- Format Compliance:
- Groundedness:
- Consistency:
- Failure Handling:

### Failure Types

### Revision Direction

### Retest Checklist
```

Prompt Evaluation은 Prompt Template 품질을 유지하는 핵심 운영 절차다.

---

### [FAQ]

Q. Prompt Evaluation Best Practice는 뭐야?

A. Prompt 결과를 Accuracy, Completeness, Format Compliance, Groundedness 등 기준으로 평가하고 개선하는 것이다.

Q. Prompt Evaluation 후에는 뭘 해야 해?

A. 실패 유형을 반영해 Prompt를 수정하고 다시 테스트한 뒤 Template으로 관리해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Constraint Prompt가 뭐야?
A. LLM이 반드시 지켜야 할 조건, 금지사항, 우선순위, 출력 제한을 정의하는 Prompt다.

Q. Constraint는 왜 필요해?
A. 모델이 프로젝트 규칙, 출력 형식, 보안 조건, 문서 근거 규칙을 지키도록 제어하기 위해 필요하다.

Q. Must Rule이 뭐야?
A. LLM이 반드시 지켜야 하는 필수 조건이다.

Q. Must Not Rule이 뭐야?
A. LLM이 절대 하지 말아야 할 행동을 정의하는 금지 조건이다.

Q. Prefer Rule이 뭐야?
A. 반드시 지켜야 하는 조건은 아니지만 가능하면 따르는 선호 조건이다.

Q. Avoid Rule이 뭐야?
A. 가능하면 피해야 하는 방식이나 패턴을 정의하는 제약이다.

Q. Scope Constraint가 뭐야?
A. LLM이 작업할 수 있는 범위와 작업하면 안 되는 범위를 정의하는 제약이다.

Q. Version Constraint가 뭐야?
A. LLM이 특정 언어, 프레임워크, 라이브러리 버전 기준으로 답변하도록 제한하는 제약이다.

Q. Output Constraint가 뭐야?
A. LLM의 최종 출력 형식, 길이, 포함 항목, 제외 항목을 제한하는 제약이다.

Q. Assumption Constraint가 뭐야?
A. LLM이 어떤 상황에서 가정을 허용하고 어떻게 표시해야 하는지 제한하는 제약이다.

Q. Hallucination Prevention이 뭐야?
A. LLM이 근거 없는 정보나 존재하지 않는 프로젝트 구조를 만들어내지 않도록 제어하는 Prompt 설계 방식이다.

Q. Hallucination은 왜 위험해?
A. 실제 프로젝트에 없는 클래스, API, DB 필드, 정책을 사실처럼 만들어 잘못된 구현을 유도할 수 있기 때문이다.

Q. Hallucination을 줄이는 핵심 규칙은 뭐야?
A. 문서 근거 우선, Missing Information 표시, Assumption 분리, 보이지 않는 코드 단정 금지다.

Q. Grounding Rule이 뭐야?
A. LLM 답변이 제공된 Context, RAG 문서, 코드, Tool 결과에 근거하도록 만드는 규칙이다.

Q. Grounding이 중요한 이유는 뭐야?
A. 근거 없는 답변과 Hallucination을 줄이기 위해 중요하다.

Q. Missing Information Rule이 뭐야?
A. 필요한 정보가 부족할 때 지어내지 않고 부족한 정보를 명확히 표시하도록 하는 규칙이다.

Q. Assumption Rule이 뭐야?
A. 작업 진행을 위해 필요한 가정을 어떻게 표시할지 정의하는 규칙이다.

Q. Assumption과 Missing Information은 어떻게 달라?
A. Missing Information은 부족한 정보이고, Assumption은 그 부족한 정보를 임시로 전제한 것이다.

Q. Verification Rule이 뭐야?
A. 최종 출력 전에 답변이 근거, 형식, 제약을 만족하는지 확인하도록 하는 규칙이다.

Q. Prompt Evaluation이 뭐야?
A. Prompt가 원하는 품질의 결과를 안정적으로 생성하는지 평가하는 과정이다.

Q. Prompt는 한 번 만들면 끝이야?
A. 아니다. 출력 결과를 평가하고 실패 유형을 반영해 반복 개선해야 한다.

Q. Prompt Evaluation은 무엇을 기준으로 해?
A. Accuracy, Completeness, Format Compliance, Groundedness, Consistency, Reusability, Failure Handling을 기준으로 한다.

Q. Accuracy는 뭐야?
A. Prompt 결과가 사실, 요구사항, 프로젝트 규칙에 맞는지 평가하는 기준이다.

Q. Completeness는 뭐야?
A. Prompt 결과가 필요한 내용을 빠짐없이 포함했는지 평가하는 기준이다.

Q. Format Compliance는 뭐야?
A. Prompt 결과가 요청한 출력 형식과 Schema를 지켰는지 평가하는 기준이다.

Q. Groundedness는 뭐야?
A. Prompt 결과가 제공된 Context, RAG 문서, Tool 결과에 근거하고 있는지 평가하는 기준이다.

Q. Consistency는 뭐야?
A. Prompt 결과가 반복 실행 시 같은 구조와 유사한 품질로 생성되는지 평가하는 기준이다.

Q. Reusability는 뭐야?
A. Prompt가 반복 작업이나 유사 작업에 재사용 가능한지 평가하는 기준이다.

Q. Failure Handling은 뭐야?
A. 정보 부족, 도구 실패, Context 부족, 형식 불가능 상황에 적절히 대응하는지 평가하는 기준이다.

Q. Prompt Evaluation Checklist Pattern이 뭐야?
A. Prompt 결과를 Accuracy, Completeness, Format Compliance, Groundedness 등 기준으로 반복 검수하는 패턴이다.

Q. Constraint에서 가장 흔한 실수는 뭐야?
A. Must와 Prefer를 구분하지 않거나 서로 충돌하는 제약을 작성하는 것이다.

Q. Hallucination Prevention에서 가장 흔한 실수는 뭐야?
A. 문서 근거 우선 규칙과 Missing Information Rule 없이 답변을 요구하는 것이다.

Q. Prompt Evaluation에서 가장 흔한 실수는 뭐야?
A. 출력 결과를 평가하지 않고 Prompt를 그대로 반복 사용하는 것이다.

Q. Constraint Best Practice는 뭐야?
A. Must, Must Not, Prefer, Avoid, Scope, Output, Assumption 제약을 분리해 명확히 작성하는 것이다.

Q. Hallucination Prevention Best Practice는 뭐야?
A. Grounding, Missing Information, Assumption, Verification을 함께 사용해 근거 없는 확정을 막는 것이다.

Q. Prompt Evaluation Best Practice는 뭐야?
A. Prompt 결과를 Accuracy, Completeness, Format Compliance, Groundedness 등 기준으로 평가하고 개선하는 것이다.
