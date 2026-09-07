# Prompt Engineering Part02 Instruction Design

---

# 1. Instruction Design Core

## 1.1 Instruction Design Definition

### [개념]

Instruction Design은 LLM에게 수행할 작업을 명확하게 지시하는 Prompt 설계 방식이다.

Instruction은 단순 명령문이 아니라 아래 요소를 포함하는 작업 기준이다.

```text
Clear Task
→ Explicit Constraint
→ Expected Output
→ Priority
→ Do / Do Not
→ Assumption Rule
→ Failure Rule
```

Instruction Design의 목적은 LLM이 사용자의 의도를 추정하지 않고, 제공된 기준에 따라 일관된 결과를 생성하도록 만드는 것이다.

---

### [핵심]

- Instruction Design은 Prompt Engineering의 핵심이다.
- Instruction은 작업 대상, 작업 내용, 제약, 출력 형식을 포함해야 한다.
- 좋은 Instruction은 짧고 명확하다.
- 중요한 조건은 명시적으로 작성해야 한다.
- 모호한 Instruction은 일반론, 누락, 형식 실패를 만든다.
- RAG 환경에서는 검색 문서 우선 규칙을 Instruction에 포함해야 한다.
- Agent 환경에서는 역할 경계와 Handoff 기준을 Instruction에 포함해야 한다.

---

### [실무]

2026 실무 기준 Instruction은 아래 구조로 작성하는 것이 안정적이다.

```text
You are [Role].
Your task is [Task].
Use [Context].
Follow [Constraints].
Return [Output Format].
If information is missing, [Failure Rule].
Before final output, check [Validation Criteria].
```

예시:

```text
You are a Backend Review Agent.
Review the given Spring Boot Service code.
Focus on transaction boundary, N+1 risk, exception handling, and API response consistency.
Use only the provided project context.
Return findings as a Markdown checklist.
If required code context is missing, state what is missing.
```

Instruction은 LLM에게 자유롭게 판단하라고 맡기는 것이 아니라, 판단 기준과 결과 형식을 함께 제공하는 방식으로 작성한다.

---

### [FAQ]

Q. Instruction Design이 뭐야?

A. LLM이 수행할 작업, 제약, 출력 형식, 실패 시 행동을 명확히 따르도록 지시를 설계하는 방식이다.

Q. Instruction과 Prompt는 같은 말이야?

A. Prompt는 전체 입력이고, Instruction은 그 안에서 실제 작업 지시와 규칙을 담당하는 핵심 부분이다.

Q. 좋은 Instruction의 핵심은 뭐야?

A. 작업 대상, 작업 내용, 제약 조건, 출력 형식, 실패 처리 기준이 명확해야 한다.

Q. Instruction이 모호하면 어떻게 돼?

A. 모델이 사용자의 의도를 추정하게 되어 일반론, 누락, Hallucination, 형식 오류가 발생할 수 있다.

---

# 2. Clear Task

## 2.1 Clear Task Rule

### [개념]

Clear Task는 LLM이 수행해야 할 작업을 명확히 정의하는 규칙이다.

Task는 “무엇을 할지”뿐 아니라 “무엇을 기준으로 어떤 결과를 만들지”까지 포함해야 한다.

나쁜 Task:

```text
이 코드 봐줘.
```

좋은 Task:

```text
Review this Spring Boot Service code for transaction boundary, N+1 query risk, exception handling, and DTO conversion responsibility.
Return problems, causes, risks, and fix directions.
```

---

### [핵심]

- Task는 작업 대상이 명확해야 한다.
- Task는 수행 기준이 있어야 한다.
- Task는 기대 결과를 포함해야 한다.
- Task가 여러 개면 우선순위를 지정해야 한다.
- Task는 Context와 분리해서 작성한다.
- Task가 불명확하면 모델이 일반적인 답변을 생성한다.

---

### [실무]

실무 Task 작성 예시:

```text
Task:
Create a RAG-optimized Markdown document for Prompt Engineering.

Target:
Instruction Design.

Focus:
- Clear Task
- Explicit Constraint
- Output Format
- Failure Rule
- Validation

Output:
Use [개념], [핵심], [실무], [FAQ], Retrieval Queries.
```

Code Review Prompt 예시:

```text
Task:
Review the provided Controller code.

Focus:
- Business logic inside Controller
- Request validation
- Response consistency
- Exception handling

Return:
- Problem
- Cause
- Risk
- Fix Direction
```

Task는 짧게 작성하되, 판단 기준과 산출물 기준은 반드시 포함한다.

---

### [FAQ]

Q. Clear Task가 뭐야?

A. LLM이 수행해야 할 작업 대상, 기준, 결과물을 명확히 정의하는 것이다.

Q. “검토해줘”는 왜 부족해?

A. 어떤 기준으로 검토할지 없기 때문에 답변이 감상이나 일반론으로 흐를 수 있다.

Q. Task에 출력 형식도 포함해야 해?

A. Task 자체에 간단히 포함할 수 있고, 복잡한 경우 Output Format 섹션으로 분리하는 것이 좋다.

Q. Task가 여러 개면 어떻게 해?

A. 우선순위를 지정하고, 순서대로 처리하도록 Instruction을 작성해야 한다.

---

# 3. Explicit Constraint

## 3.1 Constraint Design Rule

### [개념]

Explicit Constraint는 LLM이 반드시 지켜야 하는 조건을 명시하는 규칙이다.

Constraint는 모델의 자유도를 줄이고 프로젝트 규칙, 기술 버전, 금지사항, 출력 제한을 고정한다.

Constraint는 보통 아래처럼 구분한다.

```text
Must
Must Not
Prefer
Avoid
Version
Style
Output Limit
Assumption Limit
```

---

### [핵심]

- Constraint는 모델의 답변 범위를 제한한다.
- 기술 버전은 명확히 작성한다.
- 프로젝트 규칙은 반드시 명시한다.
- 금지사항은 Must Not으로 분리한다.
- 선호사항은 Prefer로 분리한다.
- 충돌하는 Constraint는 금지한다.
- Constraint가 너무 많으면 모델이 핵심을 놓칠 수 있다.

---

### [실무]

Backend Code Generation Constraint 예시:

```text
Must:
- Use Java 21.
- Use Spring Boot 3.x.
- Follow Controller → Service → Repository structure.
- Return Korean explanation.

Must Not:
- Do not invent missing classes.
- Do not expose secrets.
- Do not change existing API paths unless requested.
- Do not put business logic in Controller.

Prefer:
- Use short code snippets.
- Explain only important decisions.
```

RAG Answer Constraint 예시:

```text
Must:
- Use retrieved documents first.
- Separate confirmed facts from assumptions.
- Include missing information if context is insufficient.

Must Not:
- Do not invent project-specific facts.
- Do not override retrieved context with general knowledge.
```

Constraint는 Prompt 품질을 높이지만, 핵심 조건과 선호 조건을 구분해야 한다.

---

### [FAQ]

Q. Explicit Constraint가 뭐야?

A. LLM이 반드시 지켜야 하는 조건과 금지사항을 명확히 작성하는 규칙이다.

Q. Must와 Prefer는 어떻게 달라?

A. Must는 반드시 지켜야 하는 조건이고, Prefer는 가능하면 따르는 선호 조건이다.

Q. Must Not은 언제 써?

A. 모델이 하면 안 되는 행동, 예를 들어 클래스명 임의 생성, 보안정보 노출, API 경로 변경을 막을 때 사용한다.

Q. Constraint를 많이 넣으면 좋아?

A. 아니다. 너무 많거나 서로 충돌하면 모델이 실패하거나 중요한 조건을 놓칠 수 있다.

---

# 4. Expected Output

## 4.1 Expected Output Rule

### [개념]

Expected Output은 LLM이 최종적으로 어떤 형태의 결과를 반환해야 하는지 지정하는 규칙이다.

Expected Output은 결과의 구조, 길이, 포맷, 포함 항목을 정의한다.

Output Format이 없으면 모델은 임의의 형식으로 답변할 가능성이 높다.

---

### [핵심]

- Expected Output은 결과 형태를 고정한다.
- Markdown은 문서, 리뷰, 설명에 적합하다.
- JSON은 Tool Calling, Agent Workflow, 자동 처리에 적합하다.
- Checklist는 검증 작업에 적합하다.
- Table은 비교 정보에 적합하다.
- Code Block은 코드 예시에 적합하다.
- 출력 형식은 후속 Agent 처리 안정성에 직접 영향을 준다.

---

### [실무]

Markdown Output 예시:

```md
## Review Summary

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
  ],
  "requiresFollowUp": false
}
```

Expected Output Instruction 예시:

```text
Return the result in Markdown.
Use the following sections:
- Summary
- Findings
- Fix Direction
- Checklist
```

JSON 출력이 필요한 경우 아래 제약을 함께 사용한다.

```text
Return only valid JSON.
Do not include Markdown.
Do not include extra explanation outside JSON.
```

---

### [FAQ]

Q. Expected Output이 뭐야?

A. LLM이 반환해야 하는 결과의 구조, 형식, 포함 항목을 지정하는 규칙이다.

Q. Output Format을 지정하지 않으면 어떻게 돼?

A. 모델이 임의의 형식으로 답변하여 후속 처리나 검수가 어려워질 수 있다.

Q. Markdown은 언제 좋아?

A. 사람이 읽는 문서, 코드 리뷰, 설명, 체크리스트에 적합하다.

Q. JSON은 언제 좋아?

A. Tool Calling, 자동 처리, Multi-Agent Workflow에서 결과를 파싱해야 할 때 적합하다.

---

# 5. Priority Rule

## 5.1 Priority Design Rule

### [개념]

Priority Rule은 여러 지시가 있을 때 어떤 기준을 먼저 따라야 하는지 정하는 규칙이다.

Prompt에는 Role, Task, Context, Constraint, Output Format 등 여러 지시가 함께 들어간다.

이 지시들이 충돌할 경우 우선순위가 없으면 모델이 임의로 판단할 수 있다.

---

### [핵심]

- 중요한 규칙은 우선순위를 명시한다.
- Must는 Prefer보다 우선한다.
- 프로젝트 규칙은 일반 지식보다 우선한다.
- RAG 검색 문서는 일반 추론보다 우선한다.
- 보안 규칙은 편의성보다 우선한다.
- Output Format은 최종 출력 안정성을 위해 우선 관리한다.
- 충돌 조건이 있으면 어떤 조건을 따를지 명시한다.

---

### [실무]

Priority Rule 예시:

```text
Priority:
1. Follow safety and security rules.
2. Follow retrieved project documents.
3. Follow domain rules.
4. Follow user task.
5. Follow preferred style.
```

RAG Prompt Priority 예시:

```text
When retrieved context conflicts with general knowledge, prioritize retrieved context.
When retrieved context is insufficient, state missing information instead of guessing.
```

Code Generation Priority 예시:

```text
Priority:
1. Existing project structure
2. Existing API contract
3. Java 21 / Spring Boot 3.x compatibility
4. Clean code preference
```

Priority Rule은 복잡한 Prompt와 Multi-Agent Workflow에서 중요하다.

---

### [FAQ]

Q. Priority Rule이 뭐야?

A. 여러 지시나 조건이 충돌할 때 어떤 기준을 먼저 따를지 정하는 규칙이다.

Q. 왜 우선순위가 필요해?

A. 우선순위가 없으면 모델이 중요한 제약보다 덜 중요한 선호사항을 따를 수 있기 때문이다.

Q. RAG에서는 어떤 우선순위가 중요해?

A. 검색 문서와 프로젝트 Context를 일반 지식보다 우선하도록 지정하는 것이 중요하다.

Q. Must와 Prefer가 충돌하면 뭘 따라야 해?

A. Must가 Prefer보다 우선한다.

---

# 6. Do / Do Not Rule

## 6.1 Do Rule

### [개념]

Do Rule은 LLM이 반드시 수행해야 하는 행동을 명확히 지정하는 규칙이다.

Do Rule은 원하는 결과를 직접적으로 유도한다.

---

### [핵심]

- Do Rule은 원하는 행동을 명확히 작성한다.
- 긍정 지시는 모델이 따라가기 쉽다.
- 핵심 작업 기준은 Do Rule로 작성한다.
- Review 기준, 출력 항목, 검증 항목을 Do Rule로 지정한다.
- Do Rule은 Must와 함께 사용할 수 있다.

---

### [실무]

Do Rule 예시:

```text
Do:
- Use retrieved documents first.
- Mark assumptions clearly.
- Return the result in Markdown.
- Include problem, cause, risk, and fix direction.
- Keep code snippets short.
- Include Retrieval Queries.
```

Review Agent Do Rule 예시:

```text
Do:
- Check transaction boundary.
- Check N+1 query risk.
- Check exception handling.
- Check DTO conversion responsibility.
- Assign severity to each finding.
```

Do Rule은 “무엇을 하지 말라”보다 “무엇을 해야 하는지”를 먼저 알려주는 것이 좋다.

---

### [FAQ]

Q. Do Rule이 뭐야?

A. LLM이 반드시 수행해야 하는 행동과 포함해야 할 항목을 명확히 지정하는 규칙이다.

Q. Do Rule은 왜 필요해?

A. 원하는 결과를 직접 유도하고 누락을 줄이기 위해 필요하다.

Q. Do Rule에는 어떤 내용을 넣어?

A. 사용할 근거, 출력 구조, 검증 항목, 포함해야 할 내용, 처리 기준을 넣는다.

---

## 6.2 Do Not Rule

### [개념]

Do Not Rule은 LLM이 하지 말아야 할 행동을 명확히 금지하는 규칙이다.

Do Not Rule은 Hallucination, 형식 오류, 범위 초과, 보안 문제를 줄인다.

---

### [핵심]

- Do Not Rule은 금지사항을 명확히 작성한다.
- 프로젝트 고유 정보 임의 생성 금지는 중요하다.
- 보안정보 노출 금지는 필수다.
- Output Format을 깨는 부가 설명을 금지할 수 있다.
- 범위 밖 작업을 금지할 수 있다.
- Do Not Rule만 나열하지 말고 Do Rule도 함께 작성한다.

---

### [실무]

Do Not Rule 예시:

```text
Do Not:
- Do not invent missing classes.
- Do not invent API paths.
- Do not expose secrets.
- Do not change existing method signatures unless requested.
- Do not include extra explanation outside JSON.
- Do not mix frontend responsibility into backend output.
```

RAG Do Not Rule 예시:

```text
Do Not:
- Do not answer with unsupported project-specific facts.
- Do not treat assumptions as confirmed facts.
- Do not ignore missing information.
```

Do Not Rule은 방어 장치지만, 원하는 결과를 알려주는 Do Rule과 함께 작성해야 안정적이다.

---

### [FAQ]

Q. Do Not Rule이 뭐야?

A. LLM이 하지 말아야 할 행동을 명확히 금지하는 규칙이다.

Q. Do Not Rule은 언제 중요해?

A. 프로젝트 고유 정보 생성, 보안정보 노출, JSON 형식 오류, 범위 초과를 막을 때 중요하다.

Q. Do Not Rule만 있으면 충분해?

A. 아니다. 금지사항만 있으면 원하는 결과가 불명확하므로 Do Rule도 함께 작성해야 한다.

---

# 7. Assumption Rule

## 7.1 Assumption Design Rule

### [개념]

Assumption Rule은 정보가 부족할 때 LLM이 어떤 가정을 허용하고 어떻게 표시해야 하는지 정하는 규칙이다.

Assumption은 확정 사실이 아니다.

Assumption은 작업 진행을 위한 임시 전제다.

---

### [핵심]

- Assumption은 명확히 표시해야 한다.
- 확정 사실과 Assumption을 섞지 않는다.
- 프로젝트 고유 정보는 함부로 Assumption 처리하지 않는다.
- API 경로, 클래스명, DB 컬럼은 임의 생성하지 않는다.
- 필요한 경우 Assumption 목록을 별도 섹션으로 분리한다.
- Assumption이 많으면 추가 Context가 필요하다는 신호다.

---

### [실무]

Assumption Rule 예시:

```text
If information is missing but the task can continue, mark it as Assumption.
Do not present assumptions as confirmed facts.
Do not invent project-specific class names, API paths, or database columns.
```

Output 예시:

```md
## Assumptions

- The project uses Java 21.
- Exception handling is managed by GlobalExceptionHandler.
- ApiResponse<T> is the standard response wrapper.
```

Code Generation에서 Assumption이 필요한 경우:

```md
## Missing Information

- Entity field list is not provided.
- Repository method signatures are not provided.

## Assumptions

- Service method names are examples and should be adjusted to the existing project.
```

---

### [FAQ]

Q. Assumption Rule이 뭐야?

A. 정보가 부족할 때 사용할 가정과 그 표시 방식을 정하는 규칙이다.

Q. Assumption은 확정 사실이야?

A. 아니다. Assumption은 작업 진행을 위한 임시 전제이며 확정 사실과 구분해야 한다.

Q. 어떤 정보는 Assumption으로 처리하면 안 돼?

A. 프로젝트 고유 클래스명, API 경로, DB 컬럼, 보안 정책은 임의로 가정하면 안 된다.

Q. Assumption이 너무 많으면 어떻게 해야 해?

A. 추가 Context가 필요하다고 표시하고 Missing Information을 분리해야 한다.

---

# 8. Failure Rule

## 8.1 Failure Rule Definition

### [개념]

Failure Rule은 LLM이 정상적으로 답변하기 어려운 상황에서 어떻게 행동해야 하는지 정의하는 규칙이다.

Failure Rule은 정보 부족, 문서 부재, 형식 불가능, 범위 초과, 충돌 조건에 대응한다.

---

### [핵심]

- 정보가 부족하면 부족한 정보를 표시한다.
- 문서에 없으면 문서에 없다고 말한다.
- 추정 가능한 부분과 불가능한 부분을 구분한다.
- 출력 형식을 지킬 수 없으면 이유를 표시한다.
- 범위 밖 요청은 범위 밖이라고 표시한다.
- 실패 시에도 사용 가능한 부분 결과를 제공할 수 있다.

---

### [실무]

Failure Rule 예시:

```text
If required information is missing:
- State what is missing.
- Do not invent missing details.
- Provide a partial answer only if it is safe.
- Mark assumptions clearly.
```

RAG Failure Rule 예시:

```text
If the retrieved context does not contain the answer:
- Say the context is insufficient.
- List missing information.
- Do not answer with unsupported facts.
```

Code Review Failure Rule 예시:

```text
If only partial code is provided:
- Review only the visible code.
- Do not make claims about unseen layers.
- State what additional files are needed for full review.
```

Failure Rule은 “모르면 모른다고 말하기”를 구조화한 규칙이다.

---

### [FAQ]

Q. Failure Rule이 뭐야?

A. 정보 부족, 문서 부재, 범위 초과처럼 정상 답변이 어려운 상황에서 어떻게 행동할지 정하는 규칙이다.

Q. RAG에서 Failure Rule은 왜 중요해?

A. 검색 문서에 없는 내용을 모델이 지어내지 않도록 막기 위해 중요하다.

Q. 코드 일부만 제공됐을 때는 어떻게 해야 해?

A. 보이는 코드만 리뷰하고, 전체 판단에 필요한 추가 파일을 Missing Information으로 표시해야 한다.

Q. 실패하면 답변을 아예 안 해야 해?

A. 아니다. 안전한 범위에서 부분 답변을 제공하고 한계를 명확히 표시할 수 있다.

---

# 9. Validation Instruction

## 9.1 Validation Rule

### [개념]

Validation Instruction은 LLM이 최종 출력 전에 결과를 점검하도록 하는 규칙이다.

Validation은 정확성, 완전성, 형식 준수, 근거성, 제약 준수를 확인한다.

---

### [핵심]

- 최종 출력 전에 형식을 점검한다.
- 요청한 섹션이 모두 있는지 확인한다.
- 문서 근거와 추정을 구분했는지 확인한다.
- Missing Information을 표시했는지 확인한다.
- 코드 예시가 프로젝트 규칙에 맞는지 확인한다.
- JSON 출력은 유효한 JSON인지 확인한다.
- RAG 문서는 Retrieval Queries 포함 여부를 확인한다.

---

### [실무]

Validation Instruction 예시:

```text
Before final output, check:
- Does the answer follow the requested output format?
- Are all required sections included?
- Are claims grounded in the provided context?
- Are assumptions clearly marked?
- Is missing information clearly stated?
- Are constraints followed?
```

RAG Document Validation 예시:

```text
Before final output, verify:
- [개념], [핵심], [실무], [FAQ] sections exist.
- Retrieval Queries exist.
- Terms are consistent.
- Code blocks do not include unnecessary attributes.
- Explanations are retrieval-friendly.
```

Validation은 내부 점검용으로 사용하고, 최종 답변에는 검수 과정이 아니라 결과만 출력하는 것이 좋다.

---

### [FAQ]

Q. Validation Instruction이 뭐야?

A. LLM이 최종 출력 전에 정확성, 형식, 근거, 제약 준수를 점검하도록 하는 지시다.

Q. Validation 결과를 전부 출력해야 해?

A. 아니다. 사용자가 요청하지 않으면 검수 과정은 내부에서 처리하고 최종 결과만 출력하는 것이 좋다.

Q. RAG 문서에서 Validation은 무엇을 확인해?

A. 필수 섹션, Retrieval Queries, 용어 통일, Chunk 품질, FAQ 품질, 코드블록 형식을 확인한다.

---

# 10. Instruction Pattern

## 10.1 Standard Instruction Pattern

### [개념]

Standard Instruction Pattern은 대부분의 Prompt에 적용 가능한 기본 Instruction 구조다.

기본 패턴:

```text
Role
→ Task
→ Context
→ Constraints
→ Output Format
→ Failure Rule
→ Validation
```

이 구조는 Code Generation, Code Review, RAG Answer, Agent Workflow에 공통 적용 가능하다.

---

### [핵심]

- Role은 관점을 정한다.
- Task는 작업을 정한다.
- Context는 판단 근거를 제공한다.
- Constraints는 제한을 정한다.
- Output Format은 결과 구조를 고정한다.
- Failure Rule은 정보 부족 대응을 정한다.
- Validation은 최종 점검을 유도한다.

---

### [실무]

표준 Instruction Template:

```text
You are a [Role].

Task:
[Specific task]

Context:
[Relevant context]

Constraints:
- [Must rule]
- [Must not rule]
- [Version rule]
- [Scope rule]

Output Format:
[Expected structure]

Failure Rule:
If information is missing, state what is missing and do not invent facts.

Validation:
Before final output, check accuracy, format compliance, and missing information.
```

이 Template은 반복 작업에서 Placeholder만 바꿔 재사용할 수 있다.

---

### [FAQ]

Q. Standard Instruction Pattern은 뭐야?

A. Role, Task, Context, Constraints, Output Format, Failure Rule, Validation으로 구성된 기본 지시 구조다.

Q. 모든 Prompt에 이 구조를 써도 돼?

A. 대부분의 실무 Prompt에 적용 가능하지만, 단순 질문에는 일부 요소를 생략할 수 있다.

Q. 왜 Template으로 관리해야 해?

A. 반복 작업의 품질과 출력 형식을 안정화하기 위해서다.

---

## 10.2 Code Generation Instruction Pattern

### [개념]

Code Generation Instruction Pattern은 코드 생성을 위한 Instruction 구조다.

코드 생성 Prompt는 기술 스택, 버전, 기존 코드 구조, 제약, 예외 처리 기준을 명확히 포함해야 한다.

---

### [핵심]

- Language와 Framework를 명시한다.
- Version을 명시한다.
- Architecture를 명시한다.
- 기존 Entity, DTO, Repository 정보를 제공한다.
- 변경 금지 범위를 명시한다.
- Error Handling 기준을 명시한다.
- Test Requirement를 포함할 수 있다.
- 존재하지 않는 클래스 생성을 금지한다.

---

### [실무]

Code Generation Instruction 예시:

```text
You are a Spring Boot Backend Agent.

Task:
Generate a Service implementation plan and code snippets.

Stack:
- Java 21
- Spring Boot 3.x
- Spring Data JPA

Context:
- Controller returns ApiResponse<T> directly.
- GlobalExceptionHandler handles exceptions.
- Entity, DTO, Repository structures are provided below.

Constraints:
- Do not invent missing classes.
- Do not change Controller method signatures.
- Keep business logic in Service.
- Use @Transactional where needed.

Output Format:
Return Markdown with:
- Service Responsibility
- Method Plan
- Code Snippet
- Validation Checklist

Failure Rule:
If Entity or Repository information is insufficient, list missing information.
```

Code Generation Instruction은 “전체 만들어줘”보다 “대상과 범위를 제한한 생성”이 안정적이다.

---

### [FAQ]

Q. Code Generation Instruction에는 뭐가 필요해?

A. 언어, 프레임워크, 버전, 아키텍처, 기존 코드 구조, 제약, 예외 처리 기준이 필요하다.

Q. 코드 생성에서 가장 위험한 실수는 뭐야?

A. 존재하지 않는 클래스명, API 경로, 필드명, 비즈니스 규칙을 임의로 만드는 것이다.

Q. 전체 코드를 한 번에 요청해도 돼?

A. 가능하지만 범위가 커져 오류가 늘 수 있으므로 필요한 계층이나 기능 단위로 제한하는 것이 좋다.

---

## 10.3 Code Review Instruction Pattern

### [개념]

Code Review Instruction Pattern은 코드 검토를 위한 Instruction 구조다.

Code Review Prompt는 검토 대상, 검토 기준, Severity, Reason, Fix Direction, Risk를 포함해야 한다.

---

### [핵심]

- Review Target을 명확히 한다.
- Review Criteria를 명시한다.
- Severity를 포함한다.
- 문제와 취향을 구분한다.
- 원인과 영향을 설명한다.
- 수정 방향을 제공한다.
- 보이는 코드와 보이지 않는 코드를 구분한다.

---

### [실무]

Code Review Instruction 예시:

```text
You are a Backend Review Agent.

Task:
Review the given Spring Boot Service code.

Review Criteria:
- Transaction boundary
- N+1 query risk
- Null safety
- Exception handling
- DTO conversion responsibility
- API response consistency

Output Format:
Return Markdown:
## Review Summary
## Findings
### 1. Problem
- Severity:
- Cause:
- Risk:
- Fix Direction:
## Checklist

Failure Rule:
Review only the provided code.
Do not make claims about unseen layers.
State missing files needed for full review.
```

Code Review Instruction은 단순히 “괜찮아?”가 아니라 “어떤 기준으로 검토할지”를 명확히 해야 한다.

---

### [FAQ]

Q. Code Review Instruction에는 뭐가 필요해?

A. 리뷰 대상, 검증 기준, Severity, 문제 원인, 영향, 수정 방향, 한계 표시가 필요하다.

Q. 코드 일부만 보고 전체 구조를 단정해도 돼?

A. 아니다. 보이는 코드만 검토하고 보이지 않는 계층은 Missing Information으로 표시해야 한다.

Q. 취향과 결함은 어떻게 구분해?

A. 런타임 위험, 유지보수 위험, 보안 위험은 결함이고, 스타일 선호는 개선 제안으로 구분해야 한다.

---

## 10.4 RAG Answer Instruction Pattern

### [개념]

RAG Answer Instruction Pattern은 검색된 문서를 기반으로 답변하도록 만드는 Instruction 구조다.

핵심은 문서 근거 우선, Missing Information 표시, Hallucination 방지다.

---

### [핵심]

- Retrieved Context를 우선 사용한다.
- 문서에 없는 내용은 지어내지 않는다.
- 검색 실패와 지식 부재를 구분한다.
- 일반 지식과 문서 근거를 구분한다.
- Assumption을 명확히 표시한다.
- 출력 형식을 지정한다.
- 필요한 경우 추가 Context를 요청한다.

---

### [실무]

RAG Answer Instruction 예시:

```text
You are a RAG Answer Agent.

Task:
Answer the user question using retrieved documents.

Rules:
- Use retrieved context first.
- Do not invent project-specific facts.
- If the context is insufficient, state what is missing.
- Separate confirmed facts and assumptions.
- Return the answer in Korean Markdown.

Output Format:
## Answer
## Evidence from Context
## Assumptions
## Missing Information
## Next Step
```

RAG Answer Instruction은 모델이 일반 지식으로 문서를 덮어쓰지 않도록 제어해야 한다.

---

### [FAQ]

Q. RAG Answer Instruction의 핵심은 뭐야?

A. 검색 문서를 우선 사용하고 문서에 없는 내용은 지어내지 않는 것이다.

Q. 문서에 없는 내용은 어떻게 해야 해?

A. Missing Information으로 표시하고, 필요한 추가 Context를 명확히 적어야 한다.

Q. 일반 지식은 사용하면 안 돼?

A. 사용할 수 있지만 문서 근거와 일반 추론을 구분해야 한다.

---

## 10.5 Agent Instruction Pattern

### [개념]

Agent Instruction Pattern은 AI Agent의 역할, 책임, 입력, 출력, 도구 사용, Handoff, 종료 조건을 정의하는 구조다.

Agent Instruction은 일반 Prompt보다 책임 경계와 상태 흐름이 더 중요하다.

---

### [핵심]

- Agent Role을 정의한다.
- Responsibility를 정의한다.
- Input을 고정한다.
- Output을 고정한다.
- Tool 사용 기준을 정의한다.
- Handoff Rule을 포함한다.
- Stop Condition을 포함한다.
- Failure Rule을 포함한다.

---

### [실무]

Agent Instruction 예시:

```text
You are a Backend Agent.

Responsibility:
- Generate backend implementation plan.
- Follow PM Agent task brief.
- Use retrieved backend RAG documents.

Input:
- Task brief
- Project context
- Retrieved documents
- Existing code snippets

Output:
Markdown with:
- API
- DTO
- Service
- Repository
- Validation

Constraints:
- Do not modify frontend code.
- Do not invent missing project classes.
- Mark assumptions clearly.

Handoff Rule:
Return output in a structure that Review Agent can validate.

Stop Condition:
Stop after producing implementation plan and required snippets.
```

Agent Instruction은 단일 Agent의 품질뿐 아니라 전체 Multi-Agent Workflow 안정성에 영향을 준다.

---

### [FAQ]

Q. Agent Instruction에는 뭐가 들어가야 해?

A. Agent Role, Responsibility, Input, Output, Tools, Constraints, Handoff Rule, Stop Condition, Failure Rule이 필요하다.

Q. Handoff Rule은 왜 필요해?

A. 한 Agent의 출력이 다음 Agent의 입력이 되므로 형식과 책임 범위를 안정화하기 위해 필요하다.

Q. Stop Condition은 왜 필요해?

A. Agent가 불필요하게 반복하거나 작업 범위를 벗어나지 않도록 하기 위해 필요하다.

---

# 11. Instruction Troubleshooting

## 11.1 답변이 너무 일반적임

### [개념]

답변이 너무 일반적인 문제는 Instruction에 구체적인 Task, Context, Constraint, Output Format이 부족할 때 발생한다.

---

### [핵심]

문제:

- 답변이 프로젝트 상황에 맞지 않음
- 일반적인 개념 설명만 나옴
- 실무 적용 방향이 부족함

원인:

- Context 부족
- Role / Task 불명확
- 출력 기준 없음
- 프로젝트 규칙 미제공

해결:

- 프로젝트 Context 추가
- 구체적 Review 기준 추가
- 기술 스택과 버전 명시
- 원하는 출력 형식 지정

---

### [실무]

문제 있는 Prompt:

```text
이 코드 괜찮아?
```

개선 Prompt:

```text
Spring Boot 3.x Service 코드를 리뷰해줘.
중점은 Transaction Boundary, N+1 위험, 예외 처리, DTO 변환 책임이야.
결과는 문제 / 원인 / 위험 / 수정 방향으로 정리해줘.
```

---

### [FAQ]

Q. 답변이 너무 일반적이면 어떻게 해?

A. 프로젝트 Context, 구체적인 Task, 검증 기준, 출력 형식을 추가해야 한다.

Q. 기술 스택도 적어야 해?

A. 코드 생성이나 리뷰에서는 Java 버전, Spring Boot 버전, DB, 프로젝트 규칙을 적는 것이 좋다.

---

## 11.2 출력 형식이 깨짐

### [개념]

출력 형식이 깨지는 문제는 Output Format이 모호하거나 Schema가 복잡하거나 부가 설명을 허용할 때 발생한다.

---

### [핵심]

문제:

- JSON 형식이 깨짐
- Markdown 섹션이 누락됨
- 표 구조가 흔들림
- 불필요한 설명이 섞임

원인:

- Output Format 불명확
- Schema 과도하게 복잡함
- 예시 출력 없음
- 부가 설명 금지 조건 없음

해결:

- Schema 단순화
- 예시 출력 추가
- “Return only valid JSON” 제약 추가
- 필수 섹션 목록 명시

---

### [실무]

JSON 출력 안정화 Instruction:

```text
Return only valid JSON.
Use double quotes.
Do not include trailing commas.
Do not include Markdown.
Do not include explanation outside JSON.
```

Markdown 출력 안정화 Instruction:

```text
Use exactly these sections:
## Summary
## Findings
## Fix Direction
## Checklist
```

---

### [FAQ]

Q. 출력 형식이 계속 깨지면 어떻게 해?

A. Output Format을 단순화하고 예시를 제공하며 부가 설명 금지 조건을 추가해야 한다.

Q. JSON 출력이 깨질 때 가장 중요한 제약은 뭐야?

A. “Return only valid JSON”과 “Do not include extra explanation outside JSON”이다.

---

## 11.3 없는 정보를 지어냄

### [개념]

없는 정보를 지어내는 문제는 Missing Information Rule, RAG Context 우선 규칙, Assumption Rule이 부족할 때 발생한다.

---

### [핵심]

문제:

- 제공하지 않은 클래스명이 생김
- 없는 API 경로를 만듦
- DB 컬럼을 임의 생성함
- 프로젝트 정책을 확정적으로 말함

원인:

- Missing Information Rule 없음
- RAG Context 우선 규칙 없음
- Assumption 표시 규칙 없음
- 프로젝트 고유 정보와 일반 지식을 구분하지 않음

해결:

- 문서에 없으면 없다고 말하게 지시
- Assumption을 명시하게 함
- 프로젝트 고유 정보는 제공된 Context만 사용하게 함
- Missing Information 섹션 추가

---

### [실무]

Hallucination 방지 Instruction:

```text
Do not invent project-specific facts.
If a class, method, API path, database column, or policy is not provided, mark it as Missing Information.
If an assumption is necessary, place it under Assumptions and do not present it as confirmed.
```

---

### [FAQ]

Q. 모델이 없는 정보를 지어내면 어떻게 해?

A. Missing Information Rule, Assumption Rule, RAG Context 우선 규칙을 Prompt에 추가해야 한다.

Q. 클래스명이나 API 경로를 가정해도 돼?

A. 프로젝트 고유 정보이므로 임의로 확정하면 안 되고, 필요하면 Assumption으로 분리해야 한다.

---

# 12. Instruction Best Practice

## 12.1 Instruction Design Checklist

### [개념]

Instruction Design Checklist는 Prompt가 실행 가능한 작업 지시로 충분한지 검수하는 기준이다.

Checklist는 Prompt 작성, Prompt 검수, Agent Prompt 개선에 사용할 수 있다.

---

### [핵심]

- Task가 명확한가?
- Context가 충분한가?
- Constraint가 명확한가?
- Output Format이 지정되었는가?
- Priority가 필요한 경우 지정되었는가?
- Do / Do Not이 균형 있게 작성되었는가?
- Assumption Rule이 있는가?
- Failure Rule이 있는가?
- Validation Instruction이 있는가?
- 후속 Agent가 처리 가능한 구조인가?

---

### [실무]

Instruction Design Checklist:

```md
### [Checklist]

- [ ] Role이 필요한 경우 정의했는가?
- [ ] Task가 구체적인가?
- [ ] Input / Target이 명확한가?
- [ ] Context가 관련성 있는 정보로 구성되었는가?
- [ ] Must / Must Not이 분리되었는가?
- [ ] Prefer와 Must를 혼동하지 않았는가?
- [ ] Output Format이 명확한가?
- [ ] Missing Information Rule이 있는가?
- [ ] Assumption 표시 규칙이 있는가?
- [ ] Failure Rule이 있는가?
- [ ] Validation 기준이 있는가?
- [ ] 불필요하게 장황하지 않은가?
```

이 Checklist는 Prompt Engineering RAG 문서, PM Agent 지시서, Backend Review Prompt, RAG Answer Prompt에 공통 적용 가능하다.

---

### [FAQ]

Q. Instruction Design Checklist는 왜 필요해?

A. Prompt가 실행 가능한 지시인지 검수하고 반복 작업 품질을 안정화하기 위해 필요하다.

Q. 가장 먼저 확인할 항목은 뭐야?

A. Task, Context, Constraints, Output Format이 명확한지 먼저 확인해야 한다.

Q. Agent Workflow에서는 어떤 항목이 중요해?

A. Input, Output, Handoff Rule, Stop Condition, Failure Rule이 중요하다.

---

## 12.2 Instruction Design Best Practice

### [개념]

Instruction Design Best Practice는 LLM에게 명확하고 안정적인 작업 지시를 제공하기 위한 원칙이다.

Instruction은 짧고 명확해야 하지만, 필수 기준은 빠지면 안 된다.

---

### [핵심]

- 작업 대상과 작업 내용을 명확히 작성한다.
- Context와 Task를 분리한다.
- Must와 Prefer를 구분한다.
- Do Rule과 Do Not Rule을 함께 사용한다.
- 출력 형식을 구체적으로 지정한다.
- 부족한 정보 처리 규칙을 포함한다.
- 추정과 확정 사실을 구분하게 한다.
- 복잡한 작업은 단계별로 나눈다.
- 반복 작업은 Template으로 관리한다.
- 검수 기준을 Instruction에 포함한다.

---

### [실무]

권장 Instruction Template:

```text
You are a [Role].

Task:
[What to do]

Context:
[What to use]

Constraints:
Must:
- [Required rule]

Must Not:
- [Forbidden rule]

Output Format:
[Required output structure]

Failure Rule:
If information is missing, state what is missing and do not invent facts.

Validation:
Check format, constraints, missing information, and groundedness before final output.
```

이 Template은 Prompt Engineering, RAG Prompt, Code Review Prompt, Agent Prompt 설계의 기본형으로 사용할 수 있다.

---

### [FAQ]

Q. Instruction Design Best Practice는 뭐야?

A. 작업 대상, Context, 제약, 출력 형식, 실패 처리, 검증 기준을 명확히 작성하는 것이다.

Q. Instruction은 짧을수록 좋아?

A. 짧고 명확한 것이 좋지만, 필요한 제약과 출력 형식은 반드시 포함해야 한다.

Q. 반복 작업에는 어떤 방식이 좋아?

A. Placeholder 기반 Instruction Template으로 관리하는 방식이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. Instruction Design이 뭐야?
A. LLM이 수행할 작업, 제약, 출력 형식, 실패 시 행동을 명확히 따르도록 지시를 설계하는 방식이다.

Q. Instruction과 Prompt는 같은 말이야?
A. Prompt는 전체 입력이고, Instruction은 그 안에서 실제 작업 지시와 규칙을 담당하는 핵심 부분이다.

Q. 좋은 Instruction의 핵심은 뭐야?
A. 작업 대상, 작업 내용, 제약 조건, 출력 형식, 실패 처리 기준이 명확해야 한다.

Q. Clear Task가 뭐야?
A. LLM이 수행해야 할 작업 대상, 기준, 결과물을 명확히 정의하는 것이다.

Q. “검토해줘”만 쓰면 왜 부족해?
A. 어떤 기준으로 검토할지 없기 때문에 답변이 감상이나 일반론으로 흐를 수 있다.

Q. Explicit Constraint가 뭐야?
A. LLM이 반드시 지켜야 하는 조건과 금지사항을 명확히 작성하는 규칙이다.

Q. Must와 Prefer는 어떻게 달라?
A. Must는 반드시 지켜야 하는 조건이고, Prefer는 가능하면 따르는 선호 조건이다.

Q. Do Not Rule은 언제 써?
A. 모델이 하면 안 되는 행동, 예를 들어 클래스명 임의 생성, 보안정보 노출, API 경로 변경을 막을 때 사용한다.

Q. Expected Output이 뭐야?
A. LLM이 반환해야 하는 결과의 구조, 형식, 포함 항목을 지정하는 규칙이다.

Q. Output Format을 지정하지 않으면 어떻게 돼?
A. 모델이 임의의 형식으로 답변하여 후속 처리나 검수가 어려워질 수 있다.

Q. Priority Rule이 뭐야?
A. 여러 지시나 조건이 충돌할 때 어떤 기준을 먼저 따를지 정하는 규칙이다.

Q. RAG에서는 어떤 우선순위가 중요해?
A. 검색 문서와 프로젝트 Context를 일반 지식보다 우선하도록 지정하는 것이 중요하다.

Q. Do Rule이 뭐야?
A. LLM이 반드시 수행해야 하는 행동과 포함해야 할 항목을 명확히 지정하는 규칙이다.

Q. Do Not Rule이 뭐야?
A. LLM이 하지 말아야 할 행동을 명확히 금지하는 규칙이다.

Q. Do Not Rule만 있으면 충분해?
A. 아니다. 금지사항만 있으면 원하는 결과가 불명확하므로 Do Rule도 함께 작성해야 한다.

Q. Assumption Rule이 뭐야?
A. 정보가 부족할 때 사용할 가정과 그 표시 방식을 정하는 규칙이다.

Q. Assumption은 확정 사실이야?
A. 아니다. Assumption은 작업 진행을 위한 임시 전제이며 확정 사실과 구분해야 한다.

Q. 어떤 정보는 Assumption으로 처리하면 안 돼?
A. 프로젝트 고유 클래스명, API 경로, DB 컬럼, 보안 정책은 임의로 가정하면 안 된다.

Q. Failure Rule이 뭐야?
A. 정보 부족, 문서 부재, 범위 초과처럼 정상 답변이 어려운 상황에서 어떻게 행동할지 정하는 규칙이다.

Q. RAG에서 Failure Rule은 왜 중요해?
A. 검색 문서에 없는 내용을 모델이 지어내지 않도록 막기 위해 중요하다.

Q. 코드 일부만 제공됐을 때는 어떻게 해야 해?
A. 보이는 코드만 리뷰하고, 전체 판단에 필요한 추가 파일을 Missing Information으로 표시해야 한다.

Q. Validation Instruction이 뭐야?
A. LLM이 최종 출력 전에 정확성, 형식, 근거, 제약 준수를 점검하도록 하는 지시다.

Q. RAG 문서에서 Validation은 무엇을 확인해?
A. 필수 섹션, Retrieval Queries, 용어 통일, Chunk 품질, FAQ 품질, 코드블록 형식을 확인한다.

Q. Standard Instruction Pattern은 뭐야?
A. Role, Task, Context, Constraints, Output Format, Failure Rule, Validation으로 구성된 기본 지시 구조다.

Q. Code Generation Instruction에는 뭐가 필요해?
A. 언어, 프레임워크, 버전, 아키텍처, 기존 코드 구조, 제약, 예외 처리 기준이 필요하다.

Q. Code Review Instruction에는 뭐가 필요해?
A. 리뷰 대상, 검증 기준, Severity, 문제 원인, 영향, 수정 방향, 한계 표시가 필요하다.

Q. RAG Answer Instruction의 핵심은 뭐야?
A. 검색 문서를 우선 사용하고 문서에 없는 내용은 지어내지 않는 것이다.

Q. Agent Instruction에는 뭐가 들어가야 해?
A. Agent Role, Responsibility, Input, Output, Tools, Constraints, Handoff Rule, Stop Condition, Failure Rule이 필요하다.

Q. 답변이 너무 일반적이면 어떻게 해?
A. 프로젝트 Context, 구체적인 Task, 검증 기준, 출력 형식을 추가해야 한다.

Q. 출력 형식이 계속 깨지면 어떻게 해?
A. Output Format을 단순화하고 예시를 제공하며 부가 설명 금지 조건을 추가해야 한다.

Q. 모델이 없는 정보를 지어내면 어떻게 해?
A. Missing Information Rule, Assumption Rule, RAG Context 우선 규칙을 Prompt에 추가해야 한다.

Q. Instruction Design Checklist는 왜 필요해?
A. Prompt가 실행 가능한 지시인지 검수하고 반복 작업 품질을 안정화하기 위해 필요하다.

Q. Instruction Design Best Practice는 뭐야?
A. 작업 대상, Context, 제약, 출력 형식, 실패 처리, 검증 기준을 명확히 작성하는 것이다.

Q. 반복 작업에는 어떤 방식이 좋아?
A. Placeholder 기반 Instruction Template으로 관리하는 방식이 좋다.
