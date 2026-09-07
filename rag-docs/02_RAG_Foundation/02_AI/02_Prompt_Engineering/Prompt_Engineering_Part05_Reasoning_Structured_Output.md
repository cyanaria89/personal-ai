# Prompt Engineering Part05 Reasoning Guidance and Structured Output

---

# 1. Reasoning Guidance

## 1.1 Reasoning Guidance Definition

### [개념]

Reasoning Guidance는 LLM이 복잡한 문제를 단계적으로 분석하고 검증하도록 유도하는 Prompt 설계 방식이다.

Reasoning Guidance는 내부 사고 과정을 길게 노출하는 것이 목적이 아니다.

목적은 최종 답변의 정확도, 일관성, 검증 품질을 높이는 것이다.

기본 구조:

```text
Analyze
→ Compare
→ Decide
→ Validate
→ Final Answer
```

Reasoning Guidance는 코드 리뷰, 오류 분석, 아키텍처 판단, RAG 답변 검증, Agent Workflow에서 중요하다.

---

### [핵심]

- Reasoning Guidance는 복잡한 문제를 단계적으로 처리하게 한다.
- 최종 출력은 사용자가 읽기 쉬운 형태로 제공한다.
- 내부 검토는 Checklist로 수행할 수 있다.
- 결론 없이 과정만 나열하면 안 된다.
- RAG 답변에서는 문서 근거와 추정을 구분해야 한다.
- 코드 리뷰에서는 문제, 원인, 위험, 수정 방향을 분리해야 한다.
- Reasoning Guidance는 Validation Step과 함께 사용한다.

---

### [실무]

2026 실무 기준 Reasoning Guidance는 “생각 과정을 모두 보여줘”보다 “검토 기준을 적용하고 최종 결과만 구조화해서 출력해”에 가깝다.

권장 Prompt:

```text
Analyze the problem step by step.
Use the checklist internally.
Return only the final structured result.
```

Code Review Prompt 예시:

```text
Review the provided Service code.

Internally check:
- Transaction boundary
- N+1 query risk
- Exception handling
- DTO conversion responsibility
- Null safety

Return only:
- Summary
- Findings
- Fix Direction
- Checklist
```

Reasoning Guidance는 최종 답변 품질을 높이되, 사용자에게 불필요한 장문 사고 과정을 출력하지 않도록 설계한다.

---

### [FAQ]

Q. Reasoning Guidance가 뭐야?

A. LLM이 복잡한 문제를 단계적으로 분석하고 검증하도록 유도하는 Prompt 설계 방식이다.

Q. Reasoning Guidance는 Chain-of-Thought를 모두 출력하라는 뜻이야?

A. 아니다. 내부적으로 단계적 검토를 하되 최종 출력은 구조화된 결과 중심으로 제공하는 것이 좋다.

Q. Reasoning Guidance는 언제 필요해?

A. 코드 리뷰, 오류 분석, 아키텍처 판단, RAG 답변 검증, Agent Workflow처럼 판단 기준이 많은 작업에 필요하다.

Q. Reasoning Guidance의 핵심은 뭐야?

A. 단계적 분석, 기준 기반 판단, 검증 단계, 최종 결과 정리다.

---

# 2. Step-by-Step Reasoning Instruction

## 2.1 Step-by-Step Instruction

### [개념]

Step-by-Step Reasoning Instruction은 LLM이 문제를 한 번에 결론내지 않고 순서대로 분석하도록 유도하는 지시다.

복잡한 작업에서 누락, 비약, 잘못된 결론을 줄이는 데 사용한다.

기본 Flow:

```text
Understand Task
→ Identify Context
→ Apply Criteria
→ Find Issues
→ Validate
→ Return Final Output
```

---

### [핵심]

- 복잡한 작업은 단계별로 나눈다.
- 먼저 Task와 Context를 확인한다.
- 그 다음 Criteria를 적용한다.
- 문제와 근거를 분리한다.
- 마지막에 Validation을 수행한다.
- 최종 출력은 요청한 Output Format을 따른다.
- 단계 자체보다 최종 결과의 정확성이 중요하다.

---

### [실무]

Step-by-Step Prompt 예시:

```text
Analyze the request in this order:
1. Identify the task.
2. Identify relevant context.
3. Apply constraints.
4. Check missing information.
5. Produce the final answer in the requested format.
```

RAG Answer Prompt 예시:

```text
Analyze using this process:
1. Check retrieved context.
2. Identify confirmed facts.
3. Identify missing information.
4. Mark assumptions.
5. Return grounded answer.
```

Code Review Prompt 예시:

```text
Review using this process:
1. Identify visible code responsibility.
2. Check project rule compliance.
3. Find runtime or maintainability risks.
4. Separate confirmed issues from possible risks.
5. Return findings with severity.
```

Step-by-Step Instruction은 내부 검토 흐름을 안정화하는 데 사용한다.

---

### [FAQ]

Q. Step-by-Step Reasoning Instruction은 뭐야?

A. LLM이 문제를 순서대로 분석하고 검증하도록 유도하는 지시다.

Q. Step-by-Step을 항상 출력해야 해?

A. 아니다. 사용자가 요청하지 않으면 내부적으로 적용하고 최종 결과만 출력하는 것이 좋다.

Q. RAG에서 Step-by-Step은 어떻게 써?

A. 검색 문서 확인, 확정 정보 분리, 부족 정보 표시, 추정 분리, 최종 답변 순서로 사용한다.

Q. 코드 리뷰에서는 어떻게 써?

A. 코드 책임 확인, 프로젝트 규칙 적용, 위험 탐지, 확정 문제와 가능성 분리, Severity 부여 순서로 사용한다.

---

# 3. Checklist Reasoning

## 3.1 Checklist Reasoning Definition

### [개념]

Checklist Reasoning은 미리 정의한 검토 항목을 기준으로 LLM이 빠짐없이 점검하도록 하는 방식이다.

Checklist는 Reasoning Guidance를 안정화하는 가장 실용적인 형태다.

Checklist는 코드 리뷰, 문서 검수, JSON 검증, RAG 답변 검증, Agent Handoff 검증에 적합하다.

---

### [핵심]

- Checklist는 누락을 줄인다.
- 검토 기준을 명확히 한다.
- 반복 작업의 품질을 안정화한다.
- Review Agent에 적합하다.
- RAG 문서 검수에 필수적이다.
- Checklist는 너무 길지 않아야 한다.
- 중요한 항목은 우선순위를 둔다.

---

### [실무]

Prompt Engineering Checklist 예시:

```md
### [Checklist]

- [ ] Goal이 명확한가?
- [ ] Role이 정의되었는가?
- [ ] Context가 충분한가?
- [ ] Constraints가 명확한가?
- [ ] Output Format이 지정되었는가?
- [ ] Missing Information Rule이 있는가?
- [ ] Assumption Rule이 있는가?
- [ ] Validation 기준이 있는가?
```

RAG Document Checklist 예시:

```md
### [Checklist]

- [ ] [개념] 섹션이 있는가?
- [ ] [핵심] 섹션이 있는가?
- [ ] [실무] 섹션이 있는가?
- [ ] [FAQ] 섹션이 있는가?
- [ ] Retrieval Queries가 있는가?
- [ ] 용어가 통일되었는가?
- [ ] 코드블록에 불필요한 속성이 없는가?
- [ ] FAQ가 Q + A 구조인가?
```

Checklist Reasoning은 최종 출력 전에 내부 검수 단계로 사용하는 것이 좋다.

---

### [FAQ]

Q. Checklist Reasoning이 뭐야?

A. 미리 정의한 검토 항목을 기준으로 LLM이 빠짐없이 점검하도록 하는 방식이다.

Q. Checklist Reasoning은 어디에 좋아?

A. 코드 리뷰, RAG 문서 검수, JSON 검증, Agent Handoff 검증에 좋다.

Q. Checklist는 길수록 좋아?

A. 아니다. 핵심 검토 항목 중심으로 짧고 명확해야 한다.

Q. Checklist 결과를 항상 출력해야 해?

A. 작업 성격에 따라 다르다. 검수용이면 출력하고, 내부 품질 향상용이면 최종 결과만 출력해도 된다.

---

# 4. Decision Criteria

## 4.1 Decision Criteria Definition

### [개념]

Decision Criteria는 LLM이 판단할 때 사용할 기준이다.

Decision Criteria가 없으면 모델은 일반적인 선호나 추정으로 답변할 수 있다.

Decision Criteria는 선택, 비교, 리뷰, 우선순위 판단에 필수다.

---

### [핵심]

- 판단 기준을 명확히 제공한다.
- 기준 간 우선순위를 지정한다.
- 취향과 결함을 구분한다.
- 런타임 위험과 유지보수 위험을 구분한다.
- RAG에서는 문서 근거를 우선한다.
- 코드 리뷰에서는 프로젝트 규칙과 안정성을 우선한다.
- Agent Workflow에서는 후속 Agent 처리 가능성을 고려한다.

---

### [실무]

Code Review Decision Criteria 예시:

```text
Decision Criteria:
1. Runtime risk
2. Security risk
3. Data consistency
4. Transaction safety
5. Maintainability
6. Style preference
```

RAG Answer Decision Criteria 예시:

```text
Decision Criteria:
1. Retrieved context support
2. Project rule consistency
3. Missing information visibility
4. Assumption clarity
5. Output format compliance
```

RAG Document Decision Criteria 예시:

```text
Decision Criteria:
1. Retrieval Hit
2. Chunk Quality
3. Semantic Similarity
4. FAQ Coverage
5. Human Readability
```

Decision Criteria는 모델이 “좋아 보이는 답변”이 아니라 “기준에 맞는 답변”을 생성하도록 만든다.

---

### [FAQ]

Q. Decision Criteria가 뭐야?

A. LLM이 선택, 비교, 리뷰, 판단을 할 때 사용할 기준이다.

Q. Decision Criteria가 없으면 어떻게 돼?

A. 모델이 일반적인 선호나 추정으로 답변할 수 있다.

Q. 코드 리뷰에서 중요한 Decision Criteria는 뭐야?

A. 런타임 위험, 보안 위험, 데이터 정합성, 트랜잭션 안정성, 유지보수성이다.

Q. RAG 문서에서 중요한 Decision Criteria는 뭐야?

A. Retrieval Hit, Chunk Quality, Semantic Similarity, FAQ Coverage, Human Readability다.

---

# 5. Verification Step

## 5.1 Verification Step Definition

### [개념]

Verification Step은 LLM이 최종 출력 전에 답변이 조건을 만족하는지 확인하는 단계다.

Verification은 Reasoning Guidance의 마지막 품질 점검 단계다.

Verification은 정확성, 완전성, 형식 준수, 근거성, 누락 정보 표시를 확인한다.

---

### [핵심]

- 최종 출력 전에 형식을 점검한다.
- 요청된 필수 섹션이 있는지 확인한다.
- 문서 근거와 추정이 분리되었는지 확인한다.
- Missing Information이 필요한 경우 표시되었는지 확인한다.
- JSON은 유효한 형식인지 확인한다.
- 코드 예시는 프로젝트 규칙과 맞는지 확인한다.
- RAG 문서는 Retrieval Queries 포함 여부를 확인한다.

---

### [실무]

Verification Prompt 예시:

```text
Before final output, verify:
- The output follows the requested format.
- Required sections are included.
- Claims are grounded in provided context.
- Assumptions are clearly marked.
- Missing information is stated.
- Constraints are followed.
```

RAG Document Verification 예시:

```text
Before final output, verify:
- [개념], [핵심], [실무], [FAQ] exist.
- Retrieval Queries exist.
- Terminology is consistent.
- Code blocks do not contain unnecessary attributes.
- FAQ uses Q + A.
- Content is retrieval-friendly.
```

Verification Step은 최종 답변 품질을 높이지만, 사용자가 요청하지 않으면 검증 과정 자체를 출력하지 않는다.

---

### [FAQ]

Q. Verification Step이 뭐야?

A. 최종 출력 전에 답변이 형식, 근거, 제약, 누락 정보 기준을 만족하는지 확인하는 단계다.

Q. Verification Step은 왜 필요해?

A. 형식 누락, 근거 없는 주장, 제약 위반, Missing Information 누락을 줄이기 위해 필요하다.

Q. Verification 결과를 출력해야 해?

A. 사용자가 검수 결과를 요청하지 않았다면 최종 결과만 출력하는 것이 좋다.

Q. RAG 문서 Verification은 무엇을 확인해?

A. 필수 섹션, Retrieval Queries, 용어 통일, FAQ 구조, 코드블록 형식, Chunk 품질을 확인한다.

---

# 6. Structured Output

## 6.1 Structured Output Definition

### [개념]

Structured Output은 LLM 답변을 고정된 구조로 생성하게 하는 Prompt 설계 방식이다.

Structured Output은 Markdown, JSON, YAML, Table, Checklist, Fixed Schema를 포함한다.

Agent Workflow에서는 Structured Output이 후속 Agent 처리와 자동화 안정성을 결정한다.

기본 구조:

```text
Output Format
→ Schema
→ Required Fields
→ Field Meaning
→ Validation Rule
```

---

### [핵심]

- Structured Output은 답변 일관성을 높인다.
- 후속 Agent가 결과를 처리하기 쉬워진다.
- Markdown은 사람이 읽는 결과에 적합하다.
- JSON은 Tool Calling과 자동 처리에 적합하다.
- Checklist는 Review와 Validation에 적합하다.
- Table은 비교 정보에 적합하다.
- Fixed Schema는 반복 작업에 적합하다.
- Schema가 명확할수록 출력 안정성이 높아진다.

---

### [실무]

Markdown Structured Output 예시:

```md
## Review Summary

## Findings

### 1. Problem

- Cause:
- Risk:
- Fix Direction:
- Severity:

## Checklist
```

JSON Structured Output 예시:

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

Structured Output은 PM Agent → Domain Agent → Review Agent Handoff에서 특히 중요하다.

---

### [FAQ]

Q. Structured Output이 뭐야?

A. LLM 답변을 Markdown, JSON, Checklist, Table 같은 고정된 구조로 생성하게 하는 방식이다.

Q. Structured Output은 왜 중요해?

A. 답변 일관성을 높이고 후속 Agent나 자동화 시스템이 결과를 처리하기 쉽게 만들기 때문이다.

Q. Agent Workflow에서는 왜 중요해?

A. 한 Agent의 출력이 다음 Agent의 입력이 되므로 구조가 안정적이어야 Workflow가 흔들리지 않는다.

Q. Structured Output에는 어떤 형식이 있어?

A. Markdown, JSON, YAML, Table, Checklist, Fixed Schema가 있다.

---

# 7. Markdown Output

## 7.1 Markdown Output Definition

### [개념]

Markdown Output은 Header, Bullet, Code Block, Table, Checklist, FAQ를 사용해 답변을 구조화하는 출력 방식이다.

Markdown은 사람이 읽는 문서, 코드 리뷰, RAG 문서, 체크리스트에 적합하다.

RAG 문서에서는 Header 기반 구조가 Chunk 품질과 Retrieval 정확도에 영향을 준다.

---

### [핵심]

- Header는 Chunk 경계를 만든다.
- Bullet은 짧고 검색 친화적인 설명에 적합하다.
- Code Block은 코드 예시와 Prompt 예시에 적합하다.
- Checklist는 검수와 리뷰에 적합하다.
- FAQ는 사용자 질문 패턴과 Retrieval을 연결한다.
- Table은 비교 정보에 적합하다.
- RAG 문서에서는 `[개념]`, `[핵심]`, `[실무]`, `[FAQ]` 구조를 우선한다.

---

### [실무]

RAG 문서 Markdown 구조:

```md
# FileName

# Document Title

---

# 1. Main Section

## 1.1 Sub Section

### [개념]

### [핵심]

### [실무]

### [FAQ]

# Retrieval Queries
```

Code Review Markdown 구조:

```md
## Review Summary

## Findings

### 1. Problem

- Severity:
- Cause:
- Risk:
- Fix Direction:

## Missing Information

## Checklist
```

Markdown Output은 설명형 답변보다 구조형 답변에 적합하다.

---

### [FAQ]

Q. Markdown Output은 언제 좋아?

A. 사람이 읽는 문서, 코드 리뷰, RAG 문서, 체크리스트, 작업 계획에 적합하다.

Q. RAG 문서에서 Markdown Header가 왜 중요해?

A. Header가 Chunk 경계를 만들고 검색 시 문맥을 유지하는 데 도움을 주기 때문이다.

Q. RAG 문서에서 필수 섹션은 뭐야?

A. `[개념]`, `[핵심]`, `[실무]`, `[FAQ]`, Retrieval Queries가 중요하다.

Q. Markdown Output의 주의점은 뭐야?

A. Header 계층을 혼동하지 말고, 너무 긴 Bullet과 불필요한 장문 설명을 피해야 한다.

---

# 8. JSON Output

## 8.1 JSON Output Definition

### [개념]

JSON Output은 LLM 답변을 기계가 파싱 가능한 JSON 형식으로 생성하게 하는 출력 방식이다.

JSON은 Tool Calling, Function Calling, Multi-Agent Workflow, 자동 검증, 후속 처리에 적합하다.

JSON Output은 반드시 유효한 JSON이어야 한다.

---

### [핵심]

- JSON은 자동 처리에 적합하다.
- Field Name을 고정해야 한다.
- Required Field와 Optional Field를 구분한다.
- 문자열은 double quote를 사용한다.
- trailing comma를 금지한다.
- Markdown과 부가 설명을 섞지 않는다.
- Schema가 복잡하면 실패 가능성이 커진다.
- Error Field와 Confidence Field를 포함할 수 있다.

---

### [실무]

JSON Output Prompt 예시:

```text
Return only valid JSON.
Do not include Markdown.
Do not include explanation outside JSON.
Use double quotes.
Do not use trailing commas.
```

JSON Schema 예시:

```json
{
  "taskType": "backend_review",
  "status": "completed",
  "summary": "Review completed",
  "severity": "medium",
  "findings": [
    {
      "type": "transaction",
      "message": "Transaction boundary is unclear",
      "severity": "high",
      "fixDirection": "Add @Transactional at Service method level"
    }
  ],
  "requiresFollowUp": false
}
```

JSON Output은 자동 처리에 강하지만, 사람이 읽는 긴 설명에는 Markdown이 더 적합하다.

---

### [FAQ]

Q. JSON Output은 언제 좋아?

A. Tool Calling, Function Calling, Multi-Agent Workflow, 자동 검증, 후속 처리에 적합하다.

Q. JSON Output에서 가장 중요한 규칙은 뭐야?

A. 유효한 JSON만 출력하고 Markdown이나 부가 설명을 섞지 않는 것이다.

Q. JSON 출력이 깨지면 어떻게 해야 해?

A. Schema를 단순화하고 “Return only valid JSON”과 부가 설명 금지 조건을 추가해야 한다.

Q. JSON Schema가 복잡하면 문제야?

A. 그렇다. Schema가 복잡할수록 필드 누락이나 형식 오류 가능성이 높아진다.

---

# 9. YAML Output

## 9.1 YAML Output Definition

### [개념]

YAML Output은 계층형 데이터를 사람이 읽기 쉬운 형식으로 표현하는 출력 방식이다.

YAML은 설정 파일, Agent Config, 간단한 구조 정의에 적합하다.

JSON보다 읽기 쉽지만, 들여쓰기 오류에 민감하다.

---

### [핵심]

- YAML은 설정과 구조 정의에 적합하다.
- 사람이 읽기 쉽다.
- 들여쓰기 오류에 주의해야 한다.
- 자동 파싱 안정성은 JSON보다 낮을 수 있다.
- 복잡한 데이터 교환에는 JSON이 더 안정적이다.
- Agent Config나 Prompt Template 정의에 사용할 수 있다.

---

### [실무]

YAML Output 예시:

```yaml
agent:
  name: BackendAgent
  role: Spring Boot Backend Agent
  language: Korean
  rules:
    - Use retrieved context first
    - Do not invent project-specific facts
    - Mark assumptions clearly
  output:
    format: markdown
    sections:
      - Summary
      - Findings
      - Checklist
```

YAML은 사람이 직접 수정할 설정에는 좋다.

엄격한 자동 처리와 API 연계에는 JSON이 더 안정적이다.

---

### [FAQ]

Q. YAML Output은 언제 좋아?

A. Agent Config, 설정 파일, Prompt Template처럼 사람이 읽고 수정할 구조에 적합하다.

Q. YAML은 JSON보다 좋아?

A. 목적이 다르다. YAML은 읽기 쉽고, JSON은 자동 처리 안정성이 높다.

Q. YAML Output의 주의점은 뭐야?

A. 들여쓰기 오류와 파싱 실패에 주의해야 한다.

---

# 10. Table Output

## 10.1 Table Output Definition

### [개념]

Table Output은 비교 정보, 옵션 평가, 장단점, 우선순위, 체크 결과를 행과 열로 구조화하는 출력 방식이다.

Table은 짧은 비교에는 유용하지만 긴 설명에는 적합하지 않다.

---

### [핵심]

- Table은 비교 정보에 적합하다.
- 짧은 항목을 정리할 때 좋다.
- 긴 문장이나 코드에는 부적합하다.
- RAG 문서에서는 과도한 Table 사용을 피한다.
- 비교 대상이 명확할 때 사용한다.
- Review 결과 요약에도 사용할 수 있다.

---

### [실무]

Prompt 비교 Table 예시:

```md
| 비교 | Markdown Output  | JSON Output          |
| ---- | ---------------- | -------------------- |
| 목적 | 사람이 읽는 설명 | 자동 처리            |
| 장점 | 가독성 좋음      | 파싱 가능            |
| 단점 | 자동 처리 어려움 | 형식 오류 가능       |
| 적합 | 문서, 리뷰       | Tool, Agent Workflow |
```

Review Summary Table 예시:

```md
| 항목                 | 결과      | 위험도 |
| -------------------- | --------- | ------ |
| Transaction Boundary | 문제 있음 | High   |
| DTO Responsibility   | 일부 혼재 | Medium |
| Exception Handling   | 누락 가능 | Medium |
```

Table은 요약에 사용하고, 상세 설명은 별도 섹션으로 분리하는 것이 좋다.

---

### [FAQ]

Q. Table Output은 언제 좋아?

A. 비교, 요약, 옵션 평가, 우선순위 정리에 좋다.

Q. Table Output은 언제 피해야 해?

A. 설명이 길거나 코드가 포함되거나 항목별 상세 근거가 필요한 경우 피하는 것이 좋다.

Q. RAG 문서에서 Table을 많이 써도 돼?

A. 가능하지만 과도하면 Chunk 품질과 가독성이 떨어질 수 있으므로 필요한 비교에만 사용하는 것이 좋다.

---

# 11. Checklist Output

## 11.1 Checklist Output Definition

### [개념]

Checklist Output은 검토 항목을 체크 가능한 목록으로 구조화하는 출력 방식이다.

Checklist는 Review, Validation, QA, 문서 검수, Agent Handoff 검증에 적합하다.

---

### [핵심]

- Checklist는 누락 방지에 좋다.
- 검토 기준을 명확히 보여준다.
- Review Agent 출력에 적합하다.
- RAG 문서 검수에 적합하다.
- 각 항목은 짧고 명확해야 한다.
- 너무 많은 항목은 실무 사용성이 낮다.
- 우선순위가 필요한 경우 High / Medium / Low를 함께 사용한다.

---

### [실무]

Code Review Checklist 예시:

```md
### [Checklist]

- [ ] Transaction Boundary가 명확한가?
- [ ] N+1 Query 위험이 없는가?
- [ ] Exception Handling이 일관적인가?
- [ ] DTO 변환 책임이 적절한가?
- [ ] Null Safety가 고려되었는가?
- [ ] API Response 형식이 프로젝트 규칙과 일치하는가?
```

RAG Document Checklist 예시:

```md
### [Checklist]

- [ ] 필수 섹션이 모두 포함되었는가?
- [ ] FAQ가 Q + A 구조인가?
- [ ] Retrieval Queries가 포함되었는가?
- [ ] 용어가 통일되었는가?
- [ ] Chunk가 독립 검색 가능한가?
- [ ] 장문 에세이형 설명을 피했는가?
```

Checklist Output은 검수용으로 좋고, 최종 사용자 답변에는 필요한 경우에만 포함한다.

---

### [FAQ]

Q. Checklist Output은 언제 좋아?

A. 코드 리뷰, 문서 검수, QA, Validation, Agent Handoff 검증에 좋다.

Q. Checklist는 어떻게 작성해야 해?

A. 각 항목을 짧고 검증 가능한 형태로 작성해야 한다.

Q. Checklist 항목이 많으면 좋아?

A. 아니다. 핵심 검토 기준 중심으로 작성해야 실무 사용성이 좋다.

---

# 12. Fixed Schema

## 12.1 Fixed Schema Definition

### [개념]

Fixed Schema는 LLM 출력의 필드, 섹션, 순서, 의미를 고정하는 방식이다.

Fixed Schema는 반복 작업과 Multi-Agent Workflow에서 출력 안정성을 높인다.

---

### [핵심]

- 필드명을 고정한다.
- 섹션 순서를 고정한다.
- Required Field를 명시한다.
- Optional Field를 구분한다.
- 각 필드 의미를 정의한다.
- 후속 Agent가 파싱하기 쉽게 만든다.
- Schema 변경은 Workflow 전체에 영향을 줄 수 있다.

---

### [실무]

Markdown Fixed Schema 예시:

```md
## Task Summary

## Context

## Constraints

## Output

## Missing Information

## Validation Checklist
```

JSON Fixed Schema 예시:

```json
{
  "status": "completed",
  "taskType": "rag_document_review",
  "summary": "",
  "findings": [],
  "missingInformation": [],
  "requiresFollowUp": false
}
```

Agent Handoff Schema 예시:

```md
## Agent Handoff

### Task

### Input Context

### Constraints

### Expected Output

### Review Criteria

### Missing Information
```

Fixed Schema는 Agent 간 출력 계약에 가깝다.

---

### [FAQ]

Q. Fixed Schema가 뭐야?

A. LLM 출력의 필드, 섹션, 순서, 의미를 고정하는 방식이다.

Q. Fixed Schema는 왜 필요해?

A. 반복 작업과 Multi-Agent Workflow에서 출력 안정성과 후속 처리 가능성을 높이기 위해 필요하다.

Q. Schema를 자주 바꿔도 돼?

A. 권장하지 않는다. Schema 변경은 후속 Agent나 자동 처리 로직에 영향을 줄 수 있다.

---

# 13. Structured Output in Agent Workflow

## 13.1 Agent Handoff Output

### [개념]

Agent Handoff Output은 한 Agent가 다음 Agent에게 넘기는 구조화된 산출물이다.

PM Agent, Domain Agent, Review Agent, Fix Agent는 서로 다른 역할을 가지므로 Handoff Output이 안정적이어야 한다.

---

### [핵심]

- Handoff Output은 다음 Agent의 Input이다.
- 구조가 흔들리면 Workflow 전체가 흔들린다.
- Task, Context, Constraint, Output, Missing Information을 포함한다.
- Review Agent가 검증 가능한 구조여야 한다.
- Fix Agent가 수정 가능한 형태여야 한다.
- Handoff Schema는 고정하는 것이 좋다.

---

### [실무]

PM Agent → Backend Agent Handoff:

```md
## Task

## Project Context

## Requirements

## Constraints

## Expected Backend Output

## Missing Information
```

Backend Agent → Review Agent Handoff:

```md
## Implementation Summary

## API

## DTO

## Service

## Repository

## Assumptions

## Validation Checklist
```

Review Agent → Fix Agent Handoff:

```md
## Review Summary

## Findings

### 1. Issue

- Severity:
- Cause:
- Risk:
- Fix Direction:

## Required Fixes
```

Agent Handoff Output은 사람용 설명보다 후속 Agent 처리 가능성이 우선이다.

---

### [FAQ]

Q. Agent Handoff Output이 뭐야?

A. 한 Agent가 다음 Agent에게 넘기는 구조화된 산출물이다.

Q. Handoff Output은 왜 중요해?

A. 한 Agent의 출력이 다음 Agent의 입력이 되므로 구조가 흔들리면 전체 Workflow가 불안정해진다.

Q. Handoff Output에는 뭐가 들어가야 해?

A. Task, Context, Constraints, Expected Output, Missing Information, Review Criteria가 들어가면 좋다.

---

# 14. Structured Output Validation

## 14.1 Format Compliance

### [개념]

Format Compliance는 LLM 출력이 요청한 구조와 형식을 지켰는지 확인하는 기준이다.

Structured Output은 형식 준수가 핵심이다.

형식이 깨지면 후속 Agent, Tool, 자동 처리 시스템이 실패할 수 있다.

---

### [핵심]

- 필수 섹션이 누락되지 않았는지 확인한다.
- 필드명이 일관적인지 확인한다.
- JSON은 유효한 형식인지 확인한다.
- Markdown Header 계층이 맞는지 확인한다.
- Checklist가 체크 가능한 형태인지 확인한다.
- 불필요한 부가 설명이 섞이지 않았는지 확인한다.
- 요청한 Output Format을 우선한다.

---

### [실무]

Format Compliance Prompt 예시:

```text
Before final output, check:
- Required sections are present.
- Field names are consistent.
- JSON is valid if JSON is requested.
- Markdown headers follow the requested structure.
- No extra explanation is included outside the requested format.
```

RAG 문서 Format Compliance 예시:

```text
Check:
- FileName exists.
- Document Title exists.
- [개념], [핵심], [실무], [FAQ] exist.
- Retrieval Queries exists.
- FAQ uses Q and A.
- Code blocks have no unnecessary attributes.
```

Format Compliance는 Review Agent와 문서 검수 Agent의 핵심 검증 항목이다.

---

### [FAQ]

Q. Format Compliance가 뭐야?

A. LLM 출력이 요청한 구조와 형식을 정확히 지켰는지 확인하는 기준이다.

Q. Format Compliance가 왜 중요해?

A. 형식이 깨지면 후속 Agent, Tool, 자동 처리 시스템이 실패할 수 있기 때문이다.

Q. JSON에서 Format Compliance는 무엇을 확인해?

A. 유효한 JSON인지, 필드명이 맞는지, trailing comma가 없는지, 부가 설명이 섞이지 않았는지 확인한다.

Q. Markdown에서 Format Compliance는 무엇을 확인해?

A. Header 계층, 필수 섹션, Checklist 구조, FAQ 형식, Code Block 형식을 확인한다.

---

# 15. Common Mistakes

## 15.1 Reasoning Guidance Mistakes

### [개념]

Reasoning Guidance Mistake는 단계적 사고를 유도하면서도 최종 답변 구조를 지정하지 않아 장황하거나 결론 없는 답변이 나오는 문제다.

---

### [핵심]

자주 발생하는 실수:

- “생각 과정을 모두 보여줘”라고 요청
- 최종 Output Format 없음
- 검증 기준 없음
- 결론 없이 분석만 나열
- 문서 근거와 추정을 구분하지 않음
- 내부 검토와 사용자 출력 구분 없음
- 단계가 너무 많아 핵심이 흐려짐

---

### [실무]

나쁜 예:

```text
천천히 생각해서 자세히 설명해줘.
```

개선 예:

```text
Analyze internally step by step.
Use the checklist to verify correctness.
Return only the final result in Markdown with Summary, Findings, Fix Direction.
```

Reasoning Guidance는 최종 출력 구조와 함께 사용해야 한다.

---

### [FAQ]

Q. Reasoning Guidance에서 가장 흔한 실수는 뭐야?

A. 단계적 사고만 요구하고 최종 출력 구조와 검증 기준을 지정하지 않는 것이다.

Q. 왜 내부 검토와 최종 출력을 구분해야 해?

A. 불필요한 장문 과정을 줄이고 사용자가 바로 사용할 수 있는 결과를 제공하기 위해서다.

---

## 15.2 Structured Output Mistakes

### [개념]

Structured Output Mistake는 출력 구조가 모호하거나 Schema가 복잡해서 형식이 깨지는 문제다.

---

### [핵심]

자주 발생하는 실수:

- Output Format 없음
- 필드명 불일치
- Required Field 미지정
- JSON에 Markdown 설명 섞기
- Schema가 지나치게 복잡함
- Markdown Header 계층 혼동
- Checklist 항목이 너무 많음
- Table에 긴 설명을 넣음
- 후속 Agent가 처리하기 어려운 구조

---

### [실무]

나쁜 JSON 요청:

```text
JSON으로 적당히 정리해줘.
```

개선 JSON 요청:

```text
Return only valid JSON with fields:
- status
- summary
- findings
- requiresFollowUp

Do not include Markdown.
Do not include explanation outside JSON.
```

나쁜 Markdown 요청:

```text
마크다운으로 보기 좋게 해줘.
```

개선 Markdown 요청:

```text
Use exactly these sections:
## Summary
## Findings
## Fix Direction
## Checklist
```

Structured Output은 “보기 좋게”가 아니라 “고정된 구조로” 요청해야 안정적이다.

---

### [FAQ]

Q. Structured Output에서 가장 흔한 실수는 뭐야?

A. 출력 형식과 필드명을 명확히 지정하지 않는 것이다.

Q. JSON에 설명 문장을 같이 넣어도 돼?

A. 자동 처리가 목적이면 넣으면 안 된다. JSON만 출력하도록 제한해야 한다.

Q. Markdown Header가 흔들리면 왜 문제야?

A. RAG 문서에서는 Header가 Chunk 경계와 검색 문맥에 영향을 주기 때문이다.

---

# 16. Best Practice

## 16.1 Reasoning Guidance Best Practice

### [개념]

Reasoning Guidance Best Practice는 내부적으로 단계적 분석과 검증을 수행하게 하고, 최종 출력은 구조화된 결과만 제공하는 방식이다.

---

### [핵심]

- 복잡한 작업에는 단계적 분석을 지시한다.
- 내부 검토와 최종 출력을 구분한다.
- Checklist를 사용해 누락을 줄인다.
- Decision Criteria를 명확히 제공한다.
- Verification Step을 포함한다.
- 문서 근거와 추정을 구분한다.
- 최종 출력 형식을 반드시 지정한다.
- 장황한 사고 과정 출력은 피한다.

---

### [실무]

Reasoning Guidance Template:

```text
Analyze the task internally using this checklist:
- Identify task
- Identify context
- Apply constraints
- Check missing information
- Validate output format

Return only the final answer in the requested structure.
```

Code Review Template:

```text
Internally check:
- Runtime risk
- Security risk
- Transaction boundary
- N+1 risk
- Exception handling
- Maintainability

Return:
## Summary
## Findings
## Fix Direction
## Checklist
```

Reasoning Guidance는 Agent가 검토 품질을 높이도록 돕는 내부 절차로 설계한다.

---

### [FAQ]

Q. Reasoning Guidance Best Practice는 뭐야?

A. 내부적으로 단계적 분석과 검증을 수행하게 하고, 최종 출력은 구조화된 결과만 제공하는 방식이다.

Q. Reasoning Guidance에 꼭 필요한 요소는 뭐야?

A. Checklist, Decision Criteria, Verification Step, Output Format이 중요하다.

---

## 16.2 Structured Output Best Practice

### [개념]

Structured Output Best Practice는 출력 형식, 필드명, 필수 섹션, 검증 기준을 명확히 지정해 결과 안정성을 높이는 방식이다.

---

### [핵심]

- Output Format을 명확히 지정한다.
- 필수 섹션을 고정한다.
- Field Name을 통일한다.
- Required Field와 Optional Field를 구분한다.
- JSON은 유효성 제약을 추가한다.
- Markdown은 Header 계층을 고정한다.
- Checklist는 검증 가능한 항목으로 작성한다.
- Table은 짧은 비교에만 사용한다.
- Agent Handoff Schema는 고정한다.
- Format Compliance를 검증한다.

---

### [실무]

Structured Output Template:

```text
Output Format:
Use Markdown with exactly these sections:
## Summary
## Findings
## Missing Information
## Fix Direction
## Checklist

Rules:
- Do not add extra top-level sections.
- Keep field names consistent.
- Mark assumptions clearly.
- Include missing information when needed.
```

JSON Output Template:

```text
Return only valid JSON.

Schema:
{
  "status": "completed | failed | partial",
  "summary": "string",
  "findings": [],
  "missingInformation": [],
  "requiresFollowUp": true
}
```

Structured Output은 Prompt를 재사용 가능한 Agent 작업 단위로 만드는 핵심이다.

---

### [FAQ]

Q. Structured Output Best Practice는 뭐야?

A. 출력 형식, 필드명, 필수 섹션, 검증 기준을 명확히 지정해 결과 안정성을 높이는 방식이다.

Q. Structured Output에서 가장 중요한 것은 뭐야?

A. 고정된 Output Format과 Field Name, Format Compliance다.

Q. Agent Workflow에서는 어떤 구조가 좋아?

A. Task, Context, Constraints, Expected Output, Missing Information, Review Criteria가 포함된 Handoff Schema가 좋다.

---

# Retrieval Queries

### [FAQ]

Q. Reasoning Guidance가 뭐야?
A. LLM이 복잡한 문제를 단계적으로 분석하고 검증하도록 유도하는 Prompt 설계 방식이다.

Q. Reasoning Guidance는 Chain-of-Thought를 모두 출력하라는 뜻이야?
A. 아니다. 내부적으로 단계적 검토를 하되 최종 출력은 구조화된 결과 중심으로 제공하는 것이 좋다.

Q. Step-by-Step Reasoning Instruction은 뭐야?
A. LLM이 문제를 순서대로 분석하고 검증하도록 유도하는 지시다.

Q. Step-by-Step을 항상 출력해야 해?
A. 아니다. 사용자가 요청하지 않으면 내부적으로 적용하고 최종 결과만 출력하는 것이 좋다.

Q. Checklist Reasoning이 뭐야?
A. 미리 정의한 검토 항목을 기준으로 LLM이 빠짐없이 점검하도록 하는 방식이다.

Q. Checklist Reasoning은 어디에 좋아?
A. 코드 리뷰, RAG 문서 검수, JSON 검증, Agent Handoff 검증에 좋다.

Q. Decision Criteria가 뭐야?
A. LLM이 선택, 비교, 리뷰, 판단을 할 때 사용할 기준이다.

Q. Decision Criteria가 없으면 어떻게 돼?
A. 모델이 일반적인 선호나 추정으로 답변할 수 있다.

Q. Verification Step이 뭐야?
A. 최종 출력 전에 답변이 형식, 근거, 제약, 누락 정보 기준을 만족하는지 확인하는 단계다.

Q. Verification Step은 왜 필요해?
A. 형식 누락, 근거 없는 주장, 제약 위반, Missing Information 누락을 줄이기 위해 필요하다.

Q. Structured Output이 뭐야?
A. LLM 답변을 Markdown, JSON, Checklist, Table 같은 고정된 구조로 생성하게 하는 방식이다.

Q. Structured Output은 왜 중요해?
A. 답변 일관성을 높이고 후속 Agent나 자동화 시스템이 결과를 처리하기 쉽게 만들기 때문이다.

Q. Agent Workflow에서 Structured Output은 왜 중요해?
A. 한 Agent의 출력이 다음 Agent의 입력이 되므로 구조가 안정적이어야 Workflow가 흔들리지 않는다.

Q. Markdown Output은 언제 좋아?
A. 사람이 읽는 문서, 코드 리뷰, RAG 문서, 체크리스트, 작업 계획에 적합하다.

Q. RAG 문서에서 Markdown Header가 왜 중요해?
A. Header가 Chunk 경계를 만들고 검색 시 문맥을 유지하는 데 도움을 주기 때문이다.

Q. JSON Output은 언제 좋아?
A. Tool Calling, Function Calling, Multi-Agent Workflow, 자동 검증, 후속 처리에 적합하다.

Q. JSON Output에서 가장 중요한 규칙은 뭐야?
A. 유효한 JSON만 출력하고 Markdown이나 부가 설명을 섞지 않는 것이다.

Q. JSON 출력이 깨지면 어떻게 해야 해?
A. Schema를 단순화하고 “Return only valid JSON”과 부가 설명 금지 조건을 추가해야 한다.

Q. YAML Output은 언제 좋아?
A. Agent Config, 설정 파일, Prompt Template처럼 사람이 읽고 수정할 구조에 적합하다.

Q. YAML Output의 주의점은 뭐야?
A. 들여쓰기 오류와 파싱 실패에 주의해야 한다.

Q. Table Output은 언제 좋아?
A. 비교, 요약, 옵션 평가, 우선순위 정리에 좋다.

Q. Table Output은 언제 피해야 해?
A. 설명이 길거나 코드가 포함되거나 항목별 상세 근거가 필요한 경우 피하는 것이 좋다.

Q. Checklist Output은 언제 좋아?
A. 코드 리뷰, 문서 검수, QA, Validation, Agent Handoff 검증에 좋다.

Q. Fixed Schema가 뭐야?
A. LLM 출력의 필드, 섹션, 순서, 의미를 고정하는 방식이다.

Q. Fixed Schema는 왜 필요해?
A. 반복 작업과 Multi-Agent Workflow에서 출력 안정성과 후속 처리 가능성을 높이기 위해 필요하다.

Q. Agent Handoff Output이 뭐야?
A. 한 Agent가 다음 Agent에게 넘기는 구조화된 산출물이다.

Q. Handoff Output은 왜 중요해?
A. 한 Agent의 출력이 다음 Agent의 입력이 되므로 구조가 흔들리면 전체 Workflow가 불안정해진다.

Q. Format Compliance가 뭐야?
A. LLM 출력이 요청한 구조와 형식을 정확히 지켰는지 확인하는 기준이다.

Q. Format Compliance가 왜 중요해?
A. 형식이 깨지면 후속 Agent, Tool, 자동 처리 시스템이 실패할 수 있기 때문이다.

Q. Reasoning Guidance에서 가장 흔한 실수는 뭐야?
A. 단계적 사고만 요구하고 최종 출력 구조와 검증 기준을 지정하지 않는 것이다.

Q. Structured Output에서 가장 흔한 실수는 뭐야?
A. 출력 형식과 필드명을 명확히 지정하지 않는 것이다.

Q. JSON에 설명 문장을 같이 넣어도 돼?
A. 자동 처리가 목적이면 넣으면 안 된다. JSON만 출력하도록 제한해야 한다.

Q. Reasoning Guidance Best Practice는 뭐야?
A. 내부적으로 단계적 분석과 검증을 수행하게 하고, 최종 출력은 구조화된 결과만 제공하는 방식이다.

Q. Structured Output Best Practice는 뭐야?
A. 출력 형식, 필드명, 필수 섹션, 검증 기준을 명확히 지정해 결과 안정성을 높이는 방식이다.

Q. Agent Workflow에서는 어떤 Structured Output 구조가 좋아?
A. Task, Context, Constraints, Expected Output, Missing Information, Review Criteria가 포함된 Handoff Schema가 좋다.
