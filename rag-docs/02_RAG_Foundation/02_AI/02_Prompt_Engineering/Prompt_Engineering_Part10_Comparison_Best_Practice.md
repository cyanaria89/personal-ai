# Prompt Engineering Part10 Comparison and Best Practice

---

# 1. Prompt Comparison Core

## 1.1 Prompt Comparison Definition

### [개념]

Prompt Comparison은 Prompt 유형, 출력 형식, Agent 구조, RAG 방식의 차이를 비교해 상황에 맞는 Prompt 설계를 선택하는 기준이다.

Prompt Engineering에서는 하나의 방식이 항상 정답이 아니다.

작업 목적, 입력 Context, 출력 사용처, Agent Workflow 여부에 따라 적절한 Prompt 구조가 달라진다.

비교 기준:

```text
Purpose
→ Input Type
→ Output Type
→ Stability
→ Automation
→ Human Readability
→ Risk
→ Best Use Case
```

Prompt Comparison의 목적은 Prompt 선택 실수를 줄이고, RAG 문서와 Agent Workflow에서 일관된 판단 기준을 제공하는 것이다.

---

### [핵심]

- Prompt 유형은 작업 목적에 따라 선택한다.
- System Prompt는 지속 규칙에 적합하다.
- User Prompt는 현재 작업 요청에 적합하다.
- Role Prompt는 관점과 책임 설정에 적합하다.
- Task Prompt는 실제 작업 정의에 적합하다.
- RAG Prompt는 검색 문서 기반 답변에 적합하다.
- Agent Prompt는 역할, 입력, 출력, 도구, Handoff 정의에 적합하다.
- Structured Output은 후속 처리 안정성에 중요하다.
- 비교 기준 없이 Prompt를 선택하면 출력 품질이 흔들린다.

---

### [실무]

2026 실무 기준 Prompt 설계는 아래 순서로 판단한다.

```text
1. 이 Prompt가 지속 규칙인가?
   → System Prompt

2. 현재 작업 요청인가?
   → User Prompt

3. Agent 역할 정의인가?
   → Agent Prompt / Role Prompt

4. 검색 문서를 근거로 답해야 하는가?
   → RAG Prompt

5. 출력이 자동 처리되어야 하는가?
   → JSON / Fixed Schema

6. 사람이 읽고 검토해야 하는가?
   → Markdown / Checklist

7. 반복 작업인가?
   → Prompt Template
```

Prompt Comparison은 PM Agent가 작업을 분해하고 적절한 Prompt Pattern을 선택할 때 유용하다.

---

### [FAQ]

Q. Prompt Comparison이 뭐야?

A. Prompt 유형, 출력 형식, Agent 구조, RAG 방식을 비교해 상황에 맞는 Prompt 설계를 선택하는 기준이다.

Q. Prompt Comparison은 왜 필요해?

A. 작업 목적에 맞지 않는 Prompt 구조를 사용하면 출력 품질과 안정성이 떨어지기 때문이다.

Q. Prompt 유형은 어떻게 선택해?

A. 지속 규칙인지, 현재 작업인지, RAG 기반인지, Agent Workflow인지, 자동 처리 대상인지 기준으로 선택한다.

Q. 하나의 Prompt 구조만 계속 쓰면 안 돼?

A. 가능하지만 작업 유형이 달라지면 품질이 떨어질 수 있다. 목적에 맞는 Prompt Pattern을 선택하는 것이 좋다.

---

# 2. System Prompt vs User Prompt

## 2.1 Difference

### [개념]

System Prompt는 LLM 또는 Agent의 지속적인 상위 행동 규칙이다.

User Prompt는 사용자의 현재 작업 요청이다.

System Prompt는 기본 규칙을 고정하고, User Prompt는 매번 바뀌는 작업을 전달한다.

---

### [핵심]

| 비교      | System Prompt                            | User Prompt                                     |
| --------- | ---------------------------------------- | ----------------------------------------------- |
| 목적      | 지속 규칙 정의                           | 현재 작업 요청                                  |
| 적용 범위 | Agent 전체 행동                          | 단일 요청                                       |
| 변경 빈도 | 낮음                                     | 높음                                            |
| 포함 내용 | Identity, Role, Core Rules, RAG Use Rule | Task, Input, Target, Constraint, Output Request |
| 예시      | 답변은 한국어, 문서 근거 우선            | Part10 문서 작성                                |
| 위험      | 너무 길면 유지보수 어려움                | 모호하면 출력 불안정                            |

---

### [실무]

System Prompt 예시:

```text
You are a RAG document generation agent.
Answer in Korean.
Apply MASTER_RAG_RULES and DOMAIN_RULES.
Optimize documents for retrieval.
Do not invent project-specific facts.
```

User Prompt 예시:

```text
Create Prompt Engineering Part10 document.
Topic:
- Prompt Comparison
- Best Practice
- Prompt Selection Criteria

Output:
Use [개념], [핵심], [실무], [FAQ], Retrieval Queries.
```

System Prompt에는 반복되는 기본 규칙을 넣고, User Prompt에는 현재 작업의 목표와 산출물을 넣는다.

---

### [FAQ]

Q. System Prompt와 User Prompt 차이는 뭐야?

A. System Prompt는 지속적인 상위 규칙이고, User Prompt는 현재 작업 요청이다.

Q. 프로젝트 규칙은 어디에 넣어야 해?

A. 반복 적용되는 규칙은 System Prompt에 넣고, 현재 작업에만 필요한 조건은 User Prompt에 넣는다.

Q. User Prompt에 모든 규칙을 넣어도 돼?

A. 가능하지만 반복 규칙이 매번 중복되므로 유지보수가 어렵다.

Q. System Prompt에 일회성 작업을 넣어도 돼?

A. 권장하지 않는다. 일회성 작업은 User Prompt에 넣는 것이 좋다.

---

# 3. Role Prompt vs Task Prompt

## 3.1 Difference

### [개념]

Role Prompt는 LLM이 어떤 관점과 책임으로 답변할지 정의한다.

Task Prompt는 LLM이 실제로 수행해야 할 작업을 정의한다.

Role Prompt는 “누구로 답할지”를 정하고, Task Prompt는 “무엇을 할지”를 정한다.

---

### [핵심]

| 비교           | Role Prompt                            | Task Prompt                    |
| -------------- | -------------------------------------- | ------------------------------ |
| 목적           | 관점과 책임 설정                       | 수행 작업 정의                 |
| 핵심 질문      | 어떤 역할인가?                         | 무엇을 할 것인가?              |
| 포함 요소      | Role, Responsibility, Scope, Expertise | Task, Target, Criteria, Output |
| 단독 사용 위험 | 작업 기준 부족                         | 전문 관점 부족                 |
| 실무 기준      | Role + Responsibility 필요             | Task + Criteria 필요           |

---

### [실무]

Role만 있는 부족한 Prompt:

```text
You are a backend expert.
```

Task만 있는 부족한 Prompt:

```text
Review this code.
```

Role + Task 조합:

```text
You are a Backend Review Agent.

Task:
Review the provided Spring Boot Service code.

Criteria:
- Transaction Boundary
- N+1 Query Risk
- Exception Handling
- DTO Responsibility

Output:
Return Problem, Cause, Risk, Fix Direction, and Severity.
```

Role과 Task는 함께 사용할 때 가장 안정적이다.

---

### [FAQ]

Q. Role Prompt와 Task Prompt 차이는 뭐야?

A. Role Prompt는 관점과 책임을 정하고, Task Prompt는 실제 수행할 작업을 정한다.

Q. Role만 있으면 왜 부족해?

A. 역할은 정해지지만 작업 기준과 출력 형식이 없어서 답변이 흔들릴 수 있다.

Q. Task만 있으면 왜 부족해?

A. 작업은 정해지지만 어떤 전문 관점과 기준으로 판단할지 부족할 수 있다.

Q. Role과 Task는 항상 함께 써야 해?

A. 복잡한 작업, 코드 리뷰, Agent Workflow에서는 함께 쓰는 것이 좋다.

---

# 4. Zero-Shot vs Few-Shot

## 4.1 Difference

### [개념]

Zero-Shot Prompt는 예시 없이 지시만 제공하는 방식이다.

Few-Shot Prompt는 예시 입력과 예시 출력을 함께 제공해 출력 패턴을 안정화하는 방식이다.

---

### [핵심]

| 비교        | Zero-Shot              | Few-Shot                            |
| ----------- | ---------------------- | ----------------------------------- |
| 방식        | 예시 없이 지시         | 예시와 함께 지시                    |
| 장점        | 짧고 빠름              | 출력 형식 안정                      |
| 단점        | 결과가 흔들릴 수 있음  | Prompt가 길어짐                     |
| 적합 작업   | 단순 질의, 간단한 변환 | 코드 리뷰, JSON 출력, Agent Handoff |
| 안정화 방법 | 명확한 Instruction     | Example Input / Output              |

---

### [실무]

Zero-Shot이 적합한 경우:

- 단순 개념 설명
- 짧은 변환 작업
- 기준이 명확한 단일 질문
- 간단한 요약

Few-Shot이 적합한 경우:

- Code Review 결과 구조 고정
- JSON Output 안정화
- RAG Answer의 Confirmed / Assumption / Missing Information 분리
- Agent Handoff Schema 고정
- 반복 문서 생성

Few-Shot은 출력 구조가 중요할수록 효과적이다.

---

### [FAQ]

Q. Zero-Shot과 Few-Shot 차이는 뭐야?

A. Zero-Shot은 예시 없이 지시만 제공하고, Few-Shot은 예시 입력과 예시 출력을 함께 제공한다.

Q. Few-Shot은 언제 써야 해?

A. 출력 형식이나 판단 기준을 안정화해야 할 때 사용한다.

Q. Zero-Shot은 나쁜 방식이야?

A. 아니다. 단순 작업에는 Zero-Shot이 더 짧고 효율적이다.

Q. Few-Shot 예시는 많을수록 좋아?

A. 아니다. 실제 작업과 유사한 짧고 대표적인 예시가 좋다.

---

# 5. Markdown Output vs JSON Output

## 5.1 Difference

### [개념]

Markdown Output은 사람이 읽고 검토하기 좋은 구조화 출력이다.

JSON Output은 시스템, Tool, Agent가 파싱하기 좋은 기계 친화 출력이다.

출력 형식 선택은 결과를 누가 사용할지에 따라 달라진다.

---

### [핵심]

| 비교      | Markdown Output           | JSON Output                           |
| --------- | ------------------------- | ------------------------------------- |
| 목적      | 사람용 구조화 문서        | 기계 파싱 / 자동 처리                 |
| 장점      | 가독성 좋음               | 자동 처리 안정                        |
| 단점      | 엄격한 파싱 어려움        | 형식 오류 가능                        |
| 적합 작업 | RAG 문서, 코드 리뷰, 설명 | Tool Calling, Agent Handoff, API 연계 |
| 주요 제약 | Header 계층 유지          | Valid JSON only                       |
| 위험      | 장문 설명 과다            | Markdown 혼입, trailing comma         |

---

### [실무]

Markdown이 적합한 경우:

- RAG 문서 작성
- 코드 리뷰 결과
- 작업 계획
- Checklist
- 사용자에게 보여줄 최종 답변

JSON이 적합한 경우:

- Tool Calling
- Function Calling
- 자동 검증
- Agent 간 기계 처리
- 시스템 상태 전달

JSON Prompt에서는 아래 조건이 중요하다.

```text
Return only valid JSON.
Do not include Markdown.
Do not include explanation outside JSON.
Use double quotes.
Do not use trailing commas.
```

Markdown Prompt에서는 아래 조건이 중요하다.

```text
Use fixed section headers.
Do not add unrelated top-level sections.
Keep bullet points concise.
```

---

### [FAQ]

Q. Markdown Output과 JSON Output 차이는 뭐야?

A. Markdown은 사람이 읽기 좋고, JSON은 시스템이 파싱하기 좋다.

Q. RAG 문서는 Markdown이 좋아?

A. 그렇다. Header, FAQ, Checklist 구조가 Retrieval과 사람 검수에 모두 유리하다.

Q. Agent Workflow에서는 JSON이 좋아?

A. 자동 처리와 Tool 연계가 필요하면 JSON이 좋고, 사람이 검토해야 하면 Markdown이 좋다.

Q. JSON 출력에서 가장 중요한 조건은 뭐야?

A. 유효한 JSON만 출력하고 Markdown이나 부가 설명을 섞지 않는 것이다.

---

# 6. RAG Prompt vs General Prompt

## 6.1 Difference

### [개념]

General Prompt는 모델의 일반 지식과 제공된 입력을 기반으로 답변한다.

RAG Prompt는 검색된 문서인 Retrieved Context를 우선 근거로 답변한다.

RAG Prompt는 Grounded Answer와 Missing Information Rule이 핵심이다.

---

### [핵심]

| 비교               | General Prompt           | RAG Prompt                                              |
| ------------------ | ------------------------ | ------------------------------------------------------- |
| 근거               | 모델 일반 지식 + 입력    | Retrieved Context 우선                                  |
| 핵심 규칙          | 명확한 작업 지시         | 문서 근거 우선                                          |
| 위험               | 일반론, 최신성 부족      | 검색 실패, 근거 부족                                    |
| 필수 요소          | Task, Constraint, Output | Retrieved Context, Source Priority, Missing Information |
| 적합 작업          | 일반 설명, 아이디어 생성 | 프로젝트 문서 기반 답변, 코드 검토                      |
| Hallucination 방지 | Constraint 중심          | Grounding + Missing Information 중심                    |

---

### [실무]

General Prompt 예시:

```text
Explain what Prompt Engineering is.
```

RAG Prompt 예시:

```text
Answer using retrieved project documents first.
If the context is insufficient, state missing information.
Do not invent project-specific facts.
Separate confirmed facts, assumptions, and missing information.
```

RAG Prompt는 프로젝트 고유 정보가 중요한 작업에 적합하다.

예시:

- 개인 AI 프로젝트 RAG 문서 질의
- 업로드 문서 기반 코드 생성
- 프로젝트 규칙 기반 코드 리뷰
- Domain Rules 기반 문서 생성
- Agent Handoff 검증

---

### [FAQ]

Q. RAG Prompt와 General Prompt 차이는 뭐야?

A. General Prompt는 일반 지식 기반이고, RAG Prompt는 검색 문서를 우선 근거로 답변한다.

Q. RAG Prompt에서 가장 중요한 규칙은 뭐야?

A. Retrieved Context를 우선 사용하고 문서에 없는 내용은 지어내지 않는 것이다.

Q. 일반 지식을 RAG 답변에 사용하면 안 돼?

A. 사용할 수 있지만 프로젝트 문서 근거와 일반 추론을 구분해야 한다.

Q. 프로젝트 고유 정보에는 어떤 Prompt가 좋아?

A. RAG Prompt가 좋다. 문서 근거 기반으로 답변해야 하기 때문이다.

---

# 7. Code Generation Prompt vs Code Review Prompt

## 7.1 Difference

### [개념]

Code Generation Prompt는 새 코드나 구현 계획을 생성하도록 지시한다.

Code Review Prompt는 기존 코드나 산출물을 검토하도록 지시한다.

생성 Prompt와 리뷰 Prompt는 목적, 입력, 출력 기준이 다르다.

---

### [핵심]

| 비교      | Code Generation Prompt             | Code Review Prompt                  |
| --------- | ---------------------------------- | ----------------------------------- |
| 목적      | 코드 생성 / 구현 계획              | 코드 검증 / 위험 탐지               |
| 입력      | 요구사항, 기존 코드 Context        | 검토 대상 코드                      |
| 핵심 기준 | Stack, Architecture, Existing Code | Review Criteria, Severity           |
| 출력      | Plan, Code Snippet, Checklist      | Problem, Cause, Risk, Fix Direction |
| 위험      | 없는 코드 임의 생성                | 보이지 않는 코드 단정               |
| 필수 규칙 | Missing Information Rule           | Visible Code Only Rule              |

---

### [실무]

Code Generation Prompt 핵심:

```text
Generate implementation plan and code snippets.
Do not invent missing classes.
Follow existing architecture.
List missing information first.
```

Code Review Prompt 핵심:

```text
Review only provided code.
Do not make claims about unseen files.
Return problem, cause, risk, fix direction, and severity.
```

Code Generation은 “무엇을 만들지”가 중요하고, Code Review는 “무엇이 문제인지”가 중요하다.

---

### [FAQ]

Q. Code Generation Prompt와 Code Review Prompt 차이는 뭐야?

A. Code Generation은 코드를 만들고, Code Review는 기존 코드의 문제와 위험을 검토한다.

Q. 코드 생성에서 가장 중요한 규칙은 뭐야?

A. 없는 클래스명, API 경로, DB 필드, 비즈니스 규칙을 임의로 만들지 않는 것이다.

Q. 코드 리뷰에서 가장 중요한 규칙은 뭐야?

A. 보이는 코드만 확정적으로 리뷰하고 보이지 않는 코드는 단정하지 않는 것이다.

Q. Code Generation과 Review를 한 Prompt에서 같이 해도 돼?

A. 가능하지만 생성과 검증은 분리하는 것이 더 안정적이다.

---

# 8. Single Agent vs Multi-Agent

## 8.1 Difference

### [개념]

Single Agent는 하나의 Agent가 분석, 생성, 검토를 모두 수행하는 구조다.

Multi-Agent는 PM Agent, Domain Agent, Review Agent, Fix Agent처럼 역할을 나눠 협업하는 구조다.

작업 복잡도와 검증 필요성에 따라 선택한다.

---

### [핵심]

| 비교      | Single Agent              | Multi-Agent                             |
| --------- | ------------------------- | --------------------------------------- |
| 구조      | 하나의 Agent가 처리       | 여러 Agent 역할 분리                    |
| 장점      | 단순하고 빠름             | 검증과 역할 분리 가능                   |
| 단점      | 자체 검증 약함            | Handoff 관리 필요                       |
| 적합 작업 | 단순 질의, 짧은 코드 리뷰 | 복잡한 개발 작업, RAG 문서 제작         |
| 핵심 요소 | 좋은 Prompt 하나          | Handoff, Shared Context, Stop Condition |
| 위험      | 누락, 자기검증 한계       | 역할 중복, Context 손실                 |

---

### [실무]

Single Agent가 적합한 경우:

- 단순 개념 설명
- 작은 코드 snippet 생성
- 짧은 문서 수정
- 간단한 질의응답

Multi-Agent가 적합한 경우:

- 복잡한 기능 설계
- Backend + Frontend + Review 포함 작업
- RAG 문서 Set 제작
- 코드 생성 후 검수와 수정이 필요한 작업
- PM Agent가 작업 분해를 해야 하는 작업

Multi-Agent는 Agent 수보다 역할 분리와 Handoff 품질이 중요하다.

---

### [FAQ]

Q. Single Agent와 Multi-Agent 차이는 뭐야?

A. Single Agent는 하나의 Agent가 모두 처리하고, Multi-Agent는 역할별 Agent가 협업한다.

Q. Multi-Agent가 항상 더 좋아?

A. 아니다. 단순 작업에는 Single Agent가 더 빠르고 효율적이다.

Q. Multi-Agent가 필요한 경우는 언제야?

A. 작업이 복잡하고 역할 분리, 검증, 수정 루프가 필요한 경우다.

Q. Multi-Agent에서 가장 중요한 것은 뭐야?

A. 역할 분리, Handoff Schema, Shared Context, Stop Condition이다.

---

# 9. Constraint vs Preference

## 9.1 Difference

### [개념]

Constraint는 반드시 지켜야 하는 조건이다.

Preference는 가능하면 따르는 선호 조건이다.

Prompt에서 Constraint와 Preference를 구분하지 않으면 모델이 중요한 조건보다 덜 중요한 스타일을 우선할 수 있다.

---

### [핵심]

| 비교      | Constraint                     | Preference              |
| --------- | ------------------------------ | ----------------------- |
| 의미      | 반드시 지킬 조건               | 가능하면 따를 조건      |
| 표현      | Must, Must Not                 | Prefer, Avoid           |
| 우선순위  | 높음                           | 낮음                    |
| 예시      | API 경로 변경 금지             | 짧은 Bullet 선호        |
| 위반 영향 | 오류 / 정책 위반               | 품질 저하               |
| 사용 위치 | 보안, 프로젝트 규칙, 출력 형식 | 스타일, 길이, 표현 방식 |

---

### [실무]

Constraint 예시:

```text
Must:
- Use retrieved documents first.
- Do not invent project-specific facts.
- Preserve existing API contract.
```

Preference 예시:

```text
Prefer:
- Keep explanations concise.
- Use bullet points.
- Use short code snippets.
```

중요한 규칙은 Preference가 아니라 Constraint로 작성해야 한다.

---

### [FAQ]

Q. Constraint와 Preference 차이는 뭐야?

A. Constraint는 반드시 지켜야 하는 조건이고, Preference는 가능하면 따르는 선호 조건이다.

Q. 중요한 조건은 Prefer로 써도 돼?

A. 안 된다. 반드시 지켜야 하는 조건은 Must 또는 Must Not으로 작성해야 한다.

Q. Preference가 Constraint와 충돌하면 뭘 따라야 해?

A. Constraint를 따라야 한다.

Q. Prompt에서 둘을 왜 구분해야 해?

A. 중요한 규칙이 스타일 선호보다 우선 적용되도록 하기 위해 필요하다.

---

# 10. Prompt Selection Criteria

## 10.1 Selection Criteria Definition

### [개념]

Prompt Selection Criteria는 작업 상황에 맞는 Prompt 유형과 출력 형식을 선택하는 기준이다.

Prompt를 잘 선택하면 출력 품질, 검증 가능성, Agent Handoff 안정성이 높아진다.

---

### [핵심]

Prompt 선택 기준:

- 작업이 일회성인가 반복 작업인가?
- 일반 지식인가 RAG 문서 기반인가?
- 사람이 읽을 결과인가 시스템이 처리할 결과인가?
- 코드 생성인가 코드 리뷰인가?
- Agent 협업이 필요한가?
- 출력 형식 안정성이 중요한가?
- Hallucination 위험이 높은가?
- Missing Information 처리가 필요한가?

---

### [실무]

Prompt 선택 예시:

| 상황                | 권장 Prompt                |
| ------------------- | -------------------------- |
| 지속 규칙 정의      | System Prompt              |
| 현재 작업 요청      | User Prompt                |
| 역할과 책임 설정    | Role Prompt / Agent Prompt |
| 검색 문서 기반 답변 | RAG Prompt                 |
| 출력 형식 안정화    | Structured Output Prompt   |
| 반복 작업           | Prompt Template            |
| 코드 생성           | Code Generation Prompt     |
| 코드 검토           | Code Review Prompt         |
| 오류 분석           | Debugging Prompt           |
| Agent 협업          | Multi-Agent Prompt         |

실무에서는 Prompt를 하나만 선택하지 않고 조합한다.

예시:

```text
System Prompt
+ RAG Use Rule
+ User Prompt
+ Output Format
+ Validation Rule
```

---

### [FAQ]

Q. Prompt Selection Criteria가 뭐야?

A. 작업 상황에 맞는 Prompt 유형과 출력 형식을 선택하는 기준이다.

Q. Prompt는 하나만 선택해야 해?

A. 아니다. System Prompt, User Prompt, RAG Prompt, Output Format처럼 조합해서 사용하는 경우가 많다.

Q. RAG 문서 제작에는 어떤 Prompt가 필요해?

A. RAG Document Generation Prompt, Domain Rules, Output Constraint, Validation Rule이 필요하다.

Q. Agent Workflow에는 어떤 Prompt가 필요해?

A. Agent Prompt, Handoff Prompt, Review Prompt, Stop Condition, Shared Context 규칙이 필요하다.

---

# 11. Prompt Engineering Best Practice

## 11.1 General Best Practice

### [개념]

Prompt Engineering Best Practice는 LLM이 정확하고 일관된 결과를 생성하도록 Prompt를 설계하는 핵심 원칙이다.

Best Practice는 단일 Prompt, RAG Prompt, Code Prompt, Agent Prompt에 모두 적용된다.

---

### [핵심]

- Goal을 명확히 작성한다.
- Role을 책임과 함께 정의한다.
- Context와 Task를 분리한다.
- Constraint를 Must / Must Not / Prefer로 구분한다.
- Output Format을 고정한다.
- Missing Information Rule을 포함한다.
- Assumption Rule을 포함한다.
- RAG에서는 Retrieved Context를 우선한다.
- 코드 작업에서는 기존 코드 Context를 제공한다.
- Agent Workflow에서는 Handoff Schema를 고정한다.
- 최종 출력 전 Validation을 수행한다.
- 반복 작업은 Template으로 관리한다.

---

### [실무]

기본 Prompt 구조:

```text
You are a [Role].

Task:
[Specific task]

Context:
[Relevant context]

Constraints:
Must:
- [Required rule]

Must Not:
- [Forbidden rule]

Output Format:
[Fixed structure]

Failure Rule:
If information is missing, state what is missing and do not invent facts.

Validation:
Check accuracy, format compliance, groundedness, and missing information before final output.
```

이 구조는 대부분의 실무 Prompt에 적용 가능하다.

---

### [FAQ]

Q. Prompt Engineering Best Practice는 뭐야?

A. Goal, Role, Context, Task, Constraint, Output Format, Failure Rule, Validation을 명확히 설계하는 것이다.

Q. Prompt에서 가장 중요한 요소는 뭐야?

A. 작업 목적, Context, 제약, 출력 형식, Missing Information Rule이다.

Q. 반복 작업에는 어떤 방식이 좋아?

A. Prompt Template으로 관리하는 것이 좋다.

Q. RAG Prompt에는 어떤 규칙이 꼭 필요해?

A. Retrieved Context 우선, Missing Information 표시, Assumption 분리 규칙이 필요하다.

---

## 11.2 RAG Prompt Best Practice

### [개념]

RAG Prompt Best Practice는 검색 문서를 근거로 답변하고, 문서에 없는 내용을 지어내지 않도록 설계하는 원칙이다.

RAG Prompt는 Grounded Answer가 핵심이다.

---

### [핵심]

- Retrieved Context를 우선 사용한다.
- Source Priority를 명시한다.
- 문서에 없는 정보는 Missing Information으로 표시한다.
- Assumption을 분리한다.
- 일반 지식과 문서 근거를 구분한다.
- 프로젝트 고유 정보를 임의 생성하지 않는다.
- 답변 형식을 고정한다.
- 검색 실패와 정보 부재를 구분한다.
- FAQ와 Retrieval Queries를 강화한다.

---

### [실무]

RAG Prompt Template:

```text
You are a RAG Answer Agent.

Task:
[Answer the user question]

Retrieved Context:
[Retrieved documents]

Source Priority:
1. Retrieved Context
2. User-provided Context
3. General technical knowledge

Rules:
- Use retrieved context first.
- Do not invent project-specific facts.
- If context is insufficient, state missing information.
- Mark assumptions clearly.

Output:
## Answer
## Confirmed by Context
## Assumptions
## Missing Information
```

RAG 문서 제작에서는 사람용 설명보다 Retrieval Hit와 Chunk Quality가 우선이다.

---

### [FAQ]

Q. RAG Prompt Best Practice는 뭐야?

A. Retrieved Context 우선, Missing Information 표시, Assumption 분리, Grounded Answer 구조를 사용하는 것이다.

Q. RAG Prompt에서 가장 중요한 규칙은 뭐야?

A. 검색 문서를 우선 사용하고 문서에 없는 내용은 지어내지 않는 것이다.

Q. RAG 문서 제작에서 중요한 것은 뭐야?

A. Retrieval Hit, Chunk Quality, Semantic Similarity, FAQ Coverage, 용어 통일이다.

Q. RAG 답변에서 일반 지식은 어떻게 처리해?

A. 문서 근거와 일반 추론을 분리하고, 프로젝트 고유 정보는 문서 근거 없이 확정하지 않는다.

---

## 11.3 Code Prompt Best Practice

### [개념]

Code Prompt Best Practice는 LLM이 프로젝트 구조와 기존 코드에 맞는 코드를 생성하거나 검토하도록 설계하는 원칙이다.

Code Prompt는 기술 스택, 기존 코드 Context, 아키텍처 규칙, 검증 기준이 중요하다.

---

### [핵심]

- Language와 Framework를 명시한다.
- Version을 명시한다.
- Architecture Context를 제공한다.
- Existing Code Context를 제공한다.
- Error Handling Rule을 포함한다.
- Transaction Rule을 포함한다.
- 보이지 않는 코드는 단정하지 않는다.
- 없는 클래스명과 API 경로를 만들지 않는다.
- Review Criteria를 명확히 한다.
- Code Snippet은 필요한 범위로 제한한다.
- Validation Checklist를 포함한다.

---

### [실무]

Code Generation Prompt Template:

```text
Task:
Generate Service implementation plan and code snippet.

Stack:
- Java 21
- Spring Boot 3.x

Architecture:
- Controller → Service → Repository
- GlobalExceptionHandler handles exceptions

Existing Code Context:
[Entity / DTO / Repository / Controller]

Constraints:
- Do not invent missing classes.
- Do not change existing signatures.
- Use @Transactional for write operations.

Output:
## Missing Information
## Implementation Plan
## Code Snippet
## Validation Checklist
```

Code Review Prompt Template:

```text
Task:
Review the provided code.

Review Criteria:
- Transaction Boundary
- N+1 Query Risk
- Exception Handling
- DTO Responsibility

Rules:
- Review only visible code.
- Do not claim unseen files are correct.

Output:
Problem / Cause / Risk / Fix Direction / Severity
```

---

### [FAQ]

Q. Code Prompt Best Practice는 뭐야?

A. 기술 스택, 기존 코드 Context, 아키텍처 규칙, 예외 처리, 검증 기준을 명확히 제공하는 것이다.

Q. 코드 생성에서 가장 조심할 점은 뭐야?

A. 없는 클래스명, API 경로, DB 필드, 비즈니스 규칙을 임의로 만들지 않는 것이다.

Q. 코드 리뷰에서 가장 조심할 점은 뭐야?

A. 보이지 않는 코드를 단정하지 않고 보이는 코드만 기준으로 검토하는 것이다.

Q. Code Prompt에는 테스트 기준도 필요해?

A. 중요한 기능이면 Test Requirement 또는 Validation Checklist를 포함하는 것이 좋다.

---

## 11.4 Agent Prompt Best Practice

### [개념]

Agent Prompt Best Practice는 Agent가 자신의 역할과 책임 범위 안에서 안정적인 산출물을 생성하도록 설계하는 원칙이다.

Agent Prompt는 Role, Responsibility, Input, Output, Handoff, Stop Condition이 핵심이다.

---

### [핵심]

- Agent Role을 명확히 한다.
- Responsibility를 구체화한다.
- Scope를 제한한다.
- Input Schema를 구조화한다.
- Output Schema를 고정한다.
- Tool Use Rule을 정의한다.
- Handoff Rule을 포함한다.
- Stop Condition을 포함한다.
- Failure Rule을 포함한다.
- Missing Information과 Assumption을 보존한다.
- Review Agent가 검증 가능한 구조로 출력한다.

---

### [실무]

Agent Prompt Template:

```text
You are a [Agent Role].

Responsibility:
- [Responsibility]

Scope:
Included:
- [Allowed work]

Excluded:
- [Forbidden work]

Input:
- [Input schema]

Output:
[Fixed output schema]

Tool Use Rule:
- [Tool rules]

Handoff Rule:
Return output in a structure that [Target Agent] can validate.

Stop Condition:
Stop when [completion condition].

Failure Rule:
If information is missing, state what is missing and do not invent facts.
```

Agent Workflow에서는 Output Schema와 Handoff Schema를 고정해야 한다.

---

### [FAQ]

Q. Agent Prompt Best Practice는 뭐야?

A. Agent Role, Responsibility, Scope, Input, Output, Tool Use, Handoff, Stop Condition, Failure Rule을 명확히 정의하는 것이다.

Q. Agent Prompt에서 가장 중요한 것은 뭐야?

A. Responsibility, Input Schema, Output Schema, Handoff Rule, Stop Condition이다.

Q. Agent Output은 왜 고정해야 해?

A. 한 Agent의 Output이 다음 Agent의 Input이 되므로 구조가 안정적이어야 한다.

Q. Agent가 모르는 정보는 어떻게 처리해야 해?

A. Missing Information으로 표시하고 임의로 확정하지 않아야 한다.

---

# 12. Prompt Engineering Checklist

## 12.1 Final Checklist

### [개념]

Prompt Engineering Checklist는 Prompt가 실무 작업에 사용할 수 있을 만큼 명확하고 안정적인지 검수하는 기준이다.

Checklist는 Prompt 작성, Prompt 검수, Prompt Template 저장 전에 사용한다.

---

### [핵심]

검수 항목:

- Goal이 명확한가?
- Role이 필요한 경우 정의되었는가?
- Responsibility가 포함되었는가?
- Context와 Task가 분리되었는가?
- Constraint가 Must / Must Not / Prefer로 구분되었는가?
- Output Format이 고정되었는가?
- Missing Information Rule이 있는가?
- Assumption Rule이 있는가?
- RAG Use Rule이 필요한 경우 포함되었는가?
- Tool Use Rule이 필요한 경우 포함되었는가?
- Validation Rule이 있는가?
- 후속 Agent가 처리 가능한 구조인가?
- 반복 작업이면 Template화 가능한가?

---

### [실무]

Prompt Engineering Final Checklist:

```md
### [Checklist]

- [ ] Task가 명확한가?
- [ ] Target이 명확한가?
- [ ] Context가 충분한가?
- [ ] 기술 스택과 버전이 필요한 경우 포함되었는가?
- [ ] Must / Must Not이 구분되었는가?
- [ ] Output Format이 명확한가?
- [ ] Missing Information Rule이 있는가?
- [ ] Assumption Rule이 있는가?
- [ ] Hallucination 방지 규칙이 있는가?
- [ ] Format Compliance를 검증하는가?
- [ ] 반복 사용 가능한 구조인가?
```

Checklist는 Prompt가 길어지는 것을 막고 핵심 품질 기준을 유지하게 한다.

---

### [FAQ]

Q. Prompt Engineering Checklist는 뭐야?

A. Prompt가 실무 작업에 사용할 수 있을 만큼 명확하고 안정적인지 검수하는 기준이다.

Q. Checklist는 언제 사용해?

A. Prompt 작성 후, Prompt Template 저장 전, Agent Prompt 검수 시 사용한다.

Q. Checklist에서 가장 중요한 항목은 뭐야?

A. Task, Context, Constraints, Output Format, Missing Information Rule이다.

Q. 반복 작업 Prompt는 어떻게 관리해?

A. Checklist로 검수한 뒤 Template으로 저장해 재사용한다.

---

# Retrieval Queries

### [FAQ]

Q. Prompt Comparison이 뭐야?
A. Prompt 유형, 출력 형식, Agent 구조, RAG 방식을 비교해 상황에 맞는 Prompt 설계를 선택하는 기준이다.

Q. Prompt Comparison은 왜 필요해?
A. 작업 목적에 맞지 않는 Prompt 구조를 사용하면 출력 품질과 안정성이 떨어지기 때문이다.

Q. System Prompt와 User Prompt 차이는 뭐야?
A. System Prompt는 지속적인 상위 규칙이고, User Prompt는 현재 작업 요청이다.

Q. 프로젝트 규칙은 System Prompt와 User Prompt 중 어디에 넣어?
A. 반복 적용되는 규칙은 System Prompt에 넣고, 현재 작업에만 필요한 조건은 User Prompt에 넣는다.

Q. Role Prompt와 Task Prompt 차이는 뭐야?
A. Role Prompt는 관점과 책임을 정하고, Task Prompt는 실제 수행할 작업을 정한다.

Q. Role만 있으면 왜 부족해?
A. 역할은 정해지지만 작업 기준과 출력 형식이 없어서 답변이 흔들릴 수 있다.

Q. Zero-Shot과 Few-Shot 차이는 뭐야?
A. Zero-Shot은 예시 없이 지시만 제공하고, Few-Shot은 예시 입력과 예시 출력을 함께 제공한다.

Q. Few-Shot은 언제 써야 해?
A. 출력 형식이나 판단 기준을 안정화해야 할 때 사용한다.

Q. Markdown Output과 JSON Output 차이는 뭐야?
A. Markdown은 사람이 읽기 좋고, JSON은 시스템이 파싱하기 좋다.

Q. RAG 문서는 Markdown이 좋아?
A. 그렇다. Header, FAQ, Checklist 구조가 Retrieval과 사람 검수에 유리하다.

Q. JSON 출력에서 가장 중요한 조건은 뭐야?
A. 유효한 JSON만 출력하고 Markdown이나 부가 설명을 섞지 않는 것이다.

Q. RAG Prompt와 General Prompt 차이는 뭐야?
A. General Prompt는 일반 지식 기반이고, RAG Prompt는 검색 문서를 우선 근거로 답변한다.

Q. RAG Prompt에서 가장 중요한 규칙은 뭐야?
A. Retrieved Context를 우선 사용하고 문서에 없는 내용은 지어내지 않는 것이다.

Q. Code Generation Prompt와 Code Review Prompt 차이는 뭐야?
A. Code Generation은 코드를 만들고, Code Review는 기존 코드의 문제와 위험을 검토한다.

Q. 코드 생성에서 가장 중요한 규칙은 뭐야?
A. 없는 클래스명, API 경로, DB 필드, 비즈니스 규칙을 임의로 만들지 않는 것이다.

Q. 코드 리뷰에서 가장 중요한 규칙은 뭐야?
A. 보이는 코드만 확정적으로 리뷰하고 보이지 않는 코드는 단정하지 않는 것이다.

Q. Single Agent와 Multi-Agent 차이는 뭐야?
A. Single Agent는 하나의 Agent가 모두 처리하고, Multi-Agent는 역할별 Agent가 협업한다.

Q. Multi-Agent가 항상 더 좋아?
A. 아니다. 단순 작업에는 Single Agent가 더 빠르고 효율적이다.

Q. Multi-Agent에서 가장 중요한 것은 뭐야?
A. 역할 분리, Handoff Schema, Shared Context, Stop Condition이다.

Q. Constraint와 Preference 차이는 뭐야?
A. Constraint는 반드시 지켜야 하는 조건이고, Preference는 가능하면 따르는 선호 조건이다.

Q. 중요한 조건은 Prefer로 써도 돼?
A. 안 된다. 반드시 지켜야 하는 조건은 Must 또는 Must Not으로 작성해야 한다.

Q. Prompt Selection Criteria가 뭐야?
A. 작업 상황에 맞는 Prompt 유형과 출력 형식을 선택하는 기준이다.

Q. Prompt는 하나만 선택해야 해?
A. 아니다. System Prompt, User Prompt, RAG Prompt, Output Format처럼 조합해서 사용하는 경우가 많다.

Q. RAG 문서 제작에는 어떤 Prompt가 필요해?
A. RAG Document Generation Prompt, Domain Rules, Output Constraint, Validation Rule이 필요하다.

Q. Agent Workflow에는 어떤 Prompt가 필요해?
A. Agent Prompt, Handoff Prompt, Review Prompt, Stop Condition, Shared Context 규칙이 필요하다.

Q. Prompt Engineering Best Practice는 뭐야?
A. Goal, Role, Context, Task, Constraint, Output Format, Failure Rule, Validation을 명확히 설계하는 것이다.

Q. Prompt에서 가장 중요한 요소는 뭐야?
A. 작업 목적, Context, 제약, 출력 형식, Missing Information Rule이다.

Q. RAG Prompt Best Practice는 뭐야?
A. Retrieved Context 우선, Missing Information 표시, Assumption 분리, Grounded Answer 구조를 사용하는 것이다.

Q. RAG 문서 제작에서 중요한 것은 뭐야?
A. Retrieval Hit, Chunk Quality, Semantic Similarity, FAQ Coverage, 용어 통일이다.

Q. Code Prompt Best Practice는 뭐야?
A. 기술 스택, 기존 코드 Context, 아키텍처 규칙, 예외 처리, 검증 기준을 명확히 제공하는 것이다.

Q. Agent Prompt Best Practice는 뭐야?
A. Agent Role, Responsibility, Scope, Input, Output, Tool Use, Handoff, Stop Condition, Failure Rule을 명확히 정의하는 것이다.

Q. Prompt Engineering Checklist는 뭐야?
A. Prompt가 실무 작업에 사용할 수 있을 만큼 명확하고 안정적인지 검수하는 기준이다.

Q. Checklist에서 가장 중요한 항목은 뭐야?
A. Task, Context, Constraints, Output Format, Missing Information Rule이다.

Q. 반복 작업 Prompt는 어떻게 관리해?
A. Checklist로 검수한 뒤 Template으로 저장해 재사용한다.
