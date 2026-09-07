# Prompt Engineering Domain Rules

---

# 1. Domain Purpose

Prompt Engineering Domain 문서는 AI Agent / PM Agent / Review Agent용 RAG 문서 제작 규칙이다.

목적:

- LLM Prompt 작성 기준 제공
- System Prompt / User Prompt / Developer Prompt 구조 이해
- Agent Role Prompt 설계 지원
- RAG 기반 답변 품질 개선
- Code Generation Prompt 최적화
- Review / Validation Prompt 설계
- Structured Output 유도
- Hallucination 감소
- Multi-Agent Workflow Prompt 설계 지원

우선순위:

1. Clear Instruction
2. Context Quality
3. Role Definition
4. Output Format Control
5. Constraint Definition
6. Reasoning Guidance
7. Verification / Review

---

# 2. Scope

포함 범위:

- Prompt Engineering Core
- Instruction Design
- Role Prompt
- System Prompt
- User Prompt
- Context Prompt
- RAG Prompt
- Few-Shot Prompt
- Chain-of-Thought Guidance
- Step-by-Step Reasoning Instruction
- Structured Output
- JSON Output
- Markdown Output
- Code Generation Prompt
- Code Review Prompt
- Agent Prompt
- Multi-Agent Prompt
- Prompt Evaluation
- Prompt Iteration
- Hallucination Prevention
- Safety / Guardrail Prompt

제외 범위:

- LLM 내부 학습 구조 상세
- Fine-Tuning 상세
- RLHF 상세
- Model Quantization
- Vector Database 구현 상세
- LangGraph 구현 상세
- Production MLOps 상세

---

# 3. Section Priority

## Required

- [개념]
- [핵심]
- [실무]
- [FAQ]

---

## Strongly Recommended

- [Flow]
- [예제]
- [주의]
- [Best Practice]
- [Troubleshooting]
- [Checklist]
- [Comparison]

---

# 4. Prompt Engineering Core Rules

Prompt Engineering 문서는 단순 문장 작성법이 아니라 LLM에게 작업을 정확히 지시하는 구조 중심으로 작성한다.

핵심 구조:

```text
Goal
→ Role
→ Context
→ Task
→ Constraints
→ Output Format
→ Validation
```

반드시 설명:

- Prompt는 LLM의 작업 지시서
- 좋은 Prompt는 목표, 맥락, 제약, 출력 형식이 명확함
- RAG Prompt는 검색된 문서를 근거로 답변하게 해야 함
- Agent Prompt는 역할과 책임 범위가 명확해야 함
- Review Prompt는 검증 기준이 명확해야 함

금지:

- 모호한 지시
- 출력 형식 없는 지시
- 역할만 있고 작업 기준 없는 Prompt
- 긴 배경 설명만 있고 실제 Task가 불명확한 Prompt
- “알아서 잘 해줘” 식의 지시
- 근거 없는 답변을 허용하는 Prompt

---

# 5. Instruction Design Rules

Instruction Design은 Prompt Engineering의 핵심이다.

필수 포함:

- Clear Task
- Explicit Constraint
- Expected Output
- Priority
- Do / Do Not
- Assumption Rule
- Failure Rule

좋은 구조:

```text
You are [Role].
Your task is [Task].
Use [Context].
Follow [Constraints].
Return [Output Format].
If information is missing, [Failure Rule].
```

예시:

```text
You are a Backend Review Agent.
Review the given Spring Boot Service code.
Focus on transaction boundary, N+1 risk, exception handling, and API response consistency.
Return findings as a Markdown checklist.
```

반드시 설명:

- 지시는 짧고 명확해야 함
- 중요한 조건은 명시적으로 작성
- 우선순위가 충돌하면 기준을 제공
- 실패 시 행동을 정의해야 함

주의:

- 한 Prompt에 너무 많은 목표를 넣지 말 것
- 불필요한 예의 문구보다 작업 기준 우선
- 부정 조건만 나열하지 말고 원하는 결과도 명시

---

# 6. Role Prompt Rules

Role Prompt는 LLM의 관점과 책임을 설정한다.

필수 포함:

- Role
- Responsibility
- Scope
- Expertise
- Output Standard
- Limitation

예시:

```text
You are a Senior Spring Boot Backend Architect.
You review backend architecture based on maintainability, transaction boundary, domain responsibility, and testability.
```

반드시 설명:

- Role은 전문성과 관점을 부여
- Role만으로 충분하지 않고 작업 기준이 함께 필요
- Agent Role은 책임 범위와 금지 범위를 포함해야 함

주의:

- “너는 전문가야”만 쓰고 기준을 생략하지 말 것
- Role이 너무 넓으면 답변이 흐려짐
- 여러 Role을 한 Prompt에 섞지 말 것

---

# 7. System Prompt Rules

System Prompt는 Agent의 기본 행동 규칙으로 설명한다.

필수 포함:

- Identity
- Role
- Core Rules
- Response Language
- Output Format
- Safety Rule
- Tool Use Rule
- RAG Use Rule

예시 구조:

```text
You are a Backend Agent.
Answer in Korean.
Use retrieved documents first.
If the document does not contain enough information, say what is missing.
Do not invent project-specific code.
Return code snippets only when necessary.
```

반드시 설명:

- System Prompt는 지속적인 상위 규칙
- Agent의 역할, 말투, 판단 기준을 정의
- Domain Rules / RAG Rules와 연결 가능
- 너무 긴 System Prompt는 유지보수 어려움

주의:

- System Prompt에 일회성 작업을 과도하게 넣지 말 것
- 프로젝트별 규칙과 일반 규칙을 분리
- Agent별 Prompt는 역할에 맞게 분리

---

# 8. User Prompt Rules

User Prompt는 실제 요청을 구체화하는 지시로 설명한다.

필수 포함:

- Task
- Input
- Target
- Constraint
- Output Request
- Priority

좋은 예:

```text
Spring Boot Service 코드를 리뷰해줘.
중점은 Transaction, N+1, 예외 처리, DTO 변환이야.
결과는 문제 / 원인 / 수정 방향으로 정리해줘.
```

나쁜 예:

```text
이 코드 괜찮아?
```

반드시 설명:

- User Prompt는 작업 대상을 명확히 해야 함
- 원하는 출력 형태를 지정하면 품질이 올라감
- 부족한 정보가 있으면 Agent가 확인하거나 가정해야 함

---

# 9. Context Prompt Rules

Context Prompt는 LLM이 참고할 배경 정보를 제공한다.

필수 포함:

- Project Context
- Domain Context
- Code Context
- Business Rule
- Environment
- Constraint
- Existing Decision

기본 Flow:

```text
User Task
→ Relevant Context
→ Constraint
→ Expected Output
```

반드시 설명:

- Context는 답변 정확도에 직접 영향
- 너무 많은 Context는 핵심을 흐릴 수 있음
- RAG 검색 결과는 Context로 주입됨
- Context와 Task가 분리되어야 함

주의:

- 오래된 Context와 최신 Context 충돌 주의
- 관련 없는 Context 과다 제공 금지
- 중요한 제약은 Context가 아니라 Constraint로 명시

---

# 10. RAG Prompt Rules

RAG Prompt는 검색된 문서를 기반으로 답변하도록 설계한다.

필수 포함:

- Retrieved Context
- Source Priority
- Grounded Answer
- Missing Information Rule
- Citation / Reference Rule
- No Hallucination Rule

기본 구조:

```text
Use the retrieved context to answer.
If the context is insufficient, say what is missing.
Do not invent facts not supported by the context.
Return the answer in the requested format.
```

반드시 설명:

- RAG Prompt는 검색 결과를 우선 사용
- 문서에 없는 내용은 명확히 구분
- 검색된 Chunk가 불충분하면 추가 정보 필요를 표시
- Agent는 RAG 근거와 일반 추론을 구분해야 함

주의:

- 검색 결과와 무관한 일반 지식으로 덮어쓰기 금지
- 문서가 애매할 때 확정적으로 말하지 않기
- Retrieval 실패와 지식 부재를 구분

---

# 11. Few-Shot Prompt Rules

Few-Shot Prompt는 예시를 통해 출력 패턴을 안정화한다.

필수 포함:

- Example Input
- Example Output
- Pattern
- Variation
- Anti-Example

예시:

```text
Input:
Controller에 비즈니스 로직이 있음

Output:
문제: Fat Controller
원인: Controller가 요청 처리 외의 비즈니스 판단을 수행함
해결: 비즈니스 흐름을 Application Service로 이동
```

반드시 설명:

- Few-Shot은 형식과 판단 기준을 학습시키는 데 유용
- 예시는 짧고 대표적이어야 함
- 잘못된 예시와 올바른 예시 비교 가능

주의:

- 예시가 너무 많으면 Prompt가 길어짐
- 예시와 실제 Task가 다르면 오히려 품질 저하
- 예시 형식과 최종 출력 형식 일치 필요

---

# 12. Chain-of-Thought Guidance Rules

Reasoning Prompt는 답변 품질 향상을 위해 단계적 사고를 유도하되, 최종 출력 중심으로 작성한다.

필수 포함:

- Step-by-Step Analysis
- Checklist Reasoning
- Decision Criteria
- Verification Step
- Final Answer

권장 표현:

```text
Analyze the problem step by step.
Use the checklist internally.
Return only the final result.
```

반드시 설명:

- 복잡한 문제는 단계별 분석 지시가 유용
- 최종 답변은 사용자가 읽기 쉬운 형태로 제공
- 내부 추론 전체를 장황하게 노출하기보다 결과와 근거를 정리

주의:

- 불필요하게 긴 사고 과정 출력 금지
- 결론 없이 과정만 나열 금지
- 검증 단계 없이 답변 확정 금지

---

# 13. Structured Output Rules

Structured Output은 Agent Workflow에서 매우 중요하다.

필수 포함:

- Markdown
- Table
- Checklist
- JSON
- YAML
- Fixed Schema
- Field Definition

Markdown 예시:

```md
## 문제

## 원인

## 해결

## 체크리스트
```

JSON 예시:

```json
{
  "status": "success",
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

반드시 설명:

- Structured Output은 후속 Agent 처리에 유리
- JSON은 Tool / Agent Workflow에 적합
- Markdown은 사람이 읽는 결과에 적합
- Schema를 명확히 지정해야 출력 안정성이 높아짐

주의:

- JSON 출력 요구 시 설명 문장을 섞지 않도록 지시
- 필드명 통일
- Optional / Required 필드 구분
- Markdown 표는 내용이 길면 가독성 저하 가능

---

# 14. JSON Output Rules

JSON Output은 Agent Tool과 Multi-Agent Workflow에서 중요하다.

필수 포함:

- Valid JSON
- Schema
- Required Field
- Enum
- Error Field
- Confidence Field
- Evidence Field

예시:

```json
{
  "taskType": "backend_review",
  "status": "completed",
  "severity": "medium",
  "findings": [],
  "requiresFollowUp": false
}
```

반드시 설명:

- JSON은 반드시 유효한 형식이어야 함
- 문자열은 double quote 사용
- trailing comma 금지
- 후속 자동 처리에서는 Schema 고정이 중요

주의:

- JSON 코드블록 밖에 부가 설명 금지 요구 가능
- 모델이 JSON을 깨뜨릴 수 있으므로 검증 필요
- 너무 복잡한 Schema는 실패 가능성 증가

---

# 15. Markdown Output Rules

Markdown Output은 RAG 문서와 사람이 읽는 답변에 적합하다.

필수 포함:

- Header
- Bullet
- Code Block
- Table
- Checklist
- FAQ

반드시 설명:

- Markdown은 구조화된 설명에 적합
- RAG 문서는 Header 중심으로 Chunk 품질 향상
- Code Block은 언어 지정 권장
- Checklist는 Review / Validation에 유용

주의:

- Header 계층 혼동 금지
- 너무 긴 Bullet List 금지
- Code Block 안팎 설명 구분
- RAG 문서에서는 `[개념]`, `[핵심]`, `[실무]`, `[FAQ]` 구조 고려

---

# 16. Code Generation Prompt Rules

Code Generation Prompt는 정확한 기술 스택과 제약을 포함해야 한다.

필수 포함:

- Language
- Framework
- Version
- Architecture
- Input / Output
- Existing Code Context
- Constraint
- Error Handling
- Test Requirement

좋은 예:

```text
Spring Boot 3.x, Java 21 기준으로 Service 코드를 작성해줘.
구조는 Controller → Service → Repository이고,
응답은 ApiResponse<T>를 직접 반환하는 프로젝트 규칙을 따른다.
예외는 GlobalExceptionHandler가 처리한다고 가정한다.
```

반드시 설명:

- 버전과 프로젝트 규칙을 명시
- 기존 코드와 맞는 스타일을 요구
- 불필요한 전체 코드보다 필요한 부분만 요청
- 테스트 또는 검증 기준 포함 가능

주의:

- “전체 만들어줘”는 범위가 커질 수 있음
- Entity / DTO / Repository 관계를 명확히 제공
- 존재하지 않는 클래스명 생성 주의
- 보안 관련 코드는 검토 기준 포함

---

# 17. Code Review Prompt Rules

Code Review Prompt는 검증 기준 중심으로 작성한다.

필수 포함:

- Review Target
- Review Criteria
- Severity
- Reason
- Fix Direction
- Risk
- Checklist

예시:

```text
다음 Service 코드를 리뷰해줘.
중점:
- Transaction Boundary
- N+1 가능성
- Null Safety
- Exception Handling
- DTO 변환 책임
결과는 문제 / 원인 / 수정 방향으로 작성해줘.
```

출력 구조:

```md
## Review Summary

## Findings

### 1. 문제

- 원인:
- 영향:
- 수정 방향:
```

반드시 설명:

- Review Prompt는 기준이 명확해야 함
- 단순 감상보다 검증 항목을 요구
- Severity를 포함하면 우선순위 판단 가능
- 수정 방향은 코드 변경 가능성까지 고려

주의:

- 코드 일부만 보고 전체 구조를 단정하지 말 것
- 컴파일 불가능성 / 런타임 위험 구분
- 취향과 결함을 구분

---

# 18. Refactoring Prompt Rules

Refactoring Prompt는 기능 유지와 구조 개선을 명확히 구분한다.

필수 포함:

- Preserve Behavior
- Refactoring Goal
- Target Scope
- Before / After
- Risk
- Test Check

예시:

```text
기능은 유지하고 Service 책임만 분리해줘.
Controller, DTO, Repository 시그니처는 변경하지 말아줘.
변경 이유와 테스트 체크리스트도 함께 작성해줘.
```

반드시 설명:

- Refactoring은 기능 변경이 아님
- 변경 범위와 금지 범위를 명시
- 기존 API 호환성 유지 여부를 지정
- 테스트 체크리스트 포함 권장

주의:

- 기능 개선과 리팩토링을 동시에 크게 진행하지 않기
- 구조 변경 이유 없는 추상화 금지
- 기존 호출부 영향 확인

---

# 19. Debugging Prompt Rules

Debugging Prompt는 증상, 로그, 환경, 재현 절차를 포함해야 한다.

필수 포함:

- Symptom
- Error Message
- Stack Trace
- Environment
- Recent Change
- Reproduction Step
- Expected Result
- Actual Result

기본 구조:

```text
증상:
로그:
환경:
최근 변경:
재현 방법:
기대한 결과:
실제 결과:
```

반드시 설명:

- 에러 메시지 원문이 중요
- 최근 변경 사항은 원인 추적에 도움
- 재현 가능한 단계가 있으면 해결 품질이 높아짐
- 추정과 확인된 사실을 구분해야 함

주의:

- 로그 없이 “안 됨”만 제공하면 품질 저하
- 스크린샷만 있고 텍스트 로그가 없으면 한계 있음
- 원인 후보와 확정 원인 구분

---

# 20. Agent Prompt Rules

Agent Prompt는 역할, 입력, 출력, 금지사항, 종료 조건을 포함해야 한다.

필수 포함:

- Agent Role
- Responsibility
- Input
- Output
- Tools
- Constraints
- Handoff Rule
- Stop Condition
- Failure Rule

예시:

```text
You are a Backend Agent.
Receive task requirements from PM Agent.
Generate backend implementation plan and code snippets.
Do not modify frontend code.
If database schema is missing, request clarification from PM Agent.
Return output in Markdown with API, DTO, Service, Repository sections.
```

반드시 설명:

- Agent는 역할 경계가 명확해야 함
- 다른 Agent와 책임이 겹치지 않게 설계
- Handoff 규칙이 필요
- 실패 시 행동이 명확해야 함

주의:

- 하나의 Agent에 모든 책임 부여 금지
- Agent 간 출력 형식 불일치 주의
- 종료 조건 없는 Agent Loop 금지

---

# 21. Multi-Agent Prompt Rules

Multi-Agent Prompt는 Agent 간 협업 흐름 중심으로 작성한다.

필수 포함:

- PM Agent
- Domain Agent
- Review Agent
- Handoff
- Shared Context
- Task Decomposition
- Review / Fix Loop
- Final Output

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

반드시 설명:

- PM Agent는 요청 분해와 라우팅 담당
- Domain Agent는 전문 작업 수행
- Review Agent는 품질 검증 담당
- 최종 결과는 사용자에게 필요한 형태로 요약

주의:

- Agent 간 중복 작업 방지
- 중간 산출물 형식 통일
- Review 결과를 Fix에 반영하는 루프 필요
- 무한 반복 방지 조건 필요

---

# 22. Constraint Rules

Constraint는 Prompt 품질을 결정한다.

필수 포함:

- Must
- Must Not
- Prefer
- Avoid
- Version
- Style
- Output Limit
- Assumption Limit

예시:

```text
Must:
- Use Java 21
- Use Spring Boot 3.x
- Return Korean explanation

Must Not:
- Do not invent missing project classes
- Do not expose secrets
```

반드시 설명:

- Constraint는 모델의 자유도를 조절
- 기술 버전, 스타일, 금지사항은 명시
- 우선순위가 있으면 순서로 표현

주의:

- 제약이 너무 많으면 모델이 실패할 수 있음
- 서로 충돌하는 제약 금지
- 핵심 제약과 선호사항 구분

---

# 23. Hallucination Prevention Rules

Hallucination 방지는 RAG / Agent Prompt에서 중요하다.

필수 포함:

- Grounding
- Source Context
- Missing Information
- Uncertainty
- Assumption
- Verification

기본 규칙:

```text
If the provided context does not contain the answer, say that the context is insufficient.
Do not invent project-specific facts.
Clearly mark assumptions.
```

반드시 설명:

- 문서에 없는 내용을 있는 것처럼 말하지 않음
- 일반 지식과 프로젝트 문맥을 구분
- 불확실하면 불확실하다고 표현
- 검증 가능한 항목은 검증 단계 제안

주의:

- 파일명 / 클래스명 / API 경로를 임의 생성하지 않기
- 사용자가 제공하지 않은 정책을 확정하지 않기
- 오래된 정보와 최신 정보 충돌 주의

---

# 24. Prompt Evaluation Rules

Prompt Evaluation은 Prompt 개선에 필요하다.

필수 포함:

- Accuracy
- Completeness
- Format Compliance
- Groundedness
- Consistency
- Reusability
- Failure Handling

평가 기준:

```text
Prompt
→ Output
→ Check Accuracy
→ Check Format
→ Check Missing Info
→ Revise Prompt
```

반드시 설명:

- Prompt는 한 번에 완성되지 않을 수 있음
- 출력 품질을 기준으로 반복 개선
- 재사용 가능한 Prompt는 Template화 가능
- 실패 사례를 Prompt에 반영

주의:

- 한 번 잘 된 Prompt가 모든 상황에 맞는 것은 아님
- 예외 케이스를 평가하지 않으면 운영에서 실패 가능
- Format Compliance를 반드시 확인

---

# 25. Prompt Template Rules

Prompt Template은 반복 작업 자동화에 적합하다.

필수 포함:

- Placeholder
- Variable
- Fixed Instruction
- Dynamic Context
- Output Format

예시:

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
```

반드시 설명:

- Template은 반복 작업의 일관성을 높임
- Placeholder 이름은 명확해야 함
- 고정 규칙과 동적 입력을 분리
- 누락 변수 검증 필요

주의:

- Placeholder 누락 주의
- 동적 Context가 너무 길어지는 것 주의
- Template이 복잡하면 유지보수 어려움

---

# 26. Prompt Iteration Rules

Prompt 개선은 반복 과정으로 설명한다.

기본 Flow:

```text
Draft Prompt
→ Test Output
→ Identify Failure
→ Add Constraint / Example
→ Retest
→ Final Template
```

반드시 설명:

- 출력 실패 유형을 보고 Prompt 수정
- 형식 실패는 Output Format 강화
- 내용 누락은 Context / Checklist 추가
- 허위 답변은 Grounding Rule 추가
- 장황한 답변은 Length / Structure 제한

---

# 27. Troubleshooting Rules

반드시 포함 추천.

형식:

```md
문제:

원인:

해결:
```

---

## 답변이 너무 일반적임

문제:

- 결과가 프로젝트 상황에 맞지 않고 일반론으로 나옴

원인:

- Context 부족
- Role / Task 불명확
- 출력 기준 없음

해결:

- 프로젝트 Context 추가
- 구체적 Review 기준 추가
- 원하는 출력 형식 지정

---

## 출력 형식이 계속 깨짐

문제:

- JSON / Markdown / Table 형식이 지켜지지 않음

원인:

- Output Format이 모호함
- Schema가 복잡함
- 부가 설명을 허용함

해결:

- Schema 단순화
- 예시 출력 추가
- “Return only valid JSON” 같은 제약 추가

---

## 없는 정보를 지어냄

문제:

- 제공하지 않은 클래스명, API 경로, 정책을 만들어냄

원인:

- Missing Information Rule 없음
- RAG Context 우선 규칙 없음
- 추정과 사실 구분 없음

해결:

- 문서에 없으면 없다고 말하게 지시
- Assumption을 명시하게 함
- 프로젝트 고유 정보는 제공된 Context만 사용하게 함

---

## 답변이 너무 김

문제:

- 불필요한 설명이 많아 사용하기 어려움

원인:

- 출력 길이 제한 없음
- 핵심 항목 우선순위 없음
- 서술형 지시

해결:

- Bullet / Checklist 형식 지정
- 핵심 3~5개만 요구
- 장문 배경 설명 금지

---

## 코드가 프로젝트와 맞지 않음

문제:

- 생성된 코드가 기존 구조, 버전, 규칙과 다름

원인:

- 기술 스택 / 버전 미제공
- 기존 코드 Context 부족
- 프로젝트 규칙 미명시

해결:

- Java / Spring Boot 버전 명시
- 기존 Entity / DTO / Repository 구조 제공
- 프로젝트 응답 / 예외 처리 규칙 추가

---

# 28. Best Practice Rules

Best Practice:

- Prompt는 Goal / Context / Task / Constraint / Output Format으로 구성
- 역할만 주지 말고 책임과 기준도 명시
- RAG Prompt는 문서 근거 우선 규칙 포함
- 출력 형식은 Markdown / JSON 등 명확히 지정
- 실패 시 행동을 정의
- 복잡한 작업은 단계별로 분해
- 반복 작업은 Prompt Template으로 관리
- Code Generation은 버전과 프로젝트 규칙 명시
- Review Prompt는 검증 기준과 Severity 포함
- Agent Prompt는 Handoff / Stop Condition 포함
- 불확실한 정보는 Assumption으로 표시
- Prompt 결과는 평가 후 개선

---

# 29. Comparison Rules

Prompt Engineering 문서는 비교 기준을 포함한다.

필수 비교 대상:

- System Prompt vs User Prompt
- Role Prompt vs Task Prompt
- Zero-Shot vs Few-Shot
- Markdown Output vs JSON Output
- RAG Prompt vs General Prompt
- Code Generation Prompt vs Code Review Prompt
- Single Agent Prompt vs Multi-Agent Prompt
- Constraint vs Preference

예시:

| 비교 | Zero-Shot        | Few-Shot                     |
| ---- | ---------------- | ---------------------------- |
| 방식 | 예시 없이 지시   | 예시와 함께 지시             |
| 장점 | 짧고 단순        | 출력 패턴 안정               |
| 단점 | 형식 흔들림 가능 | Prompt 길어짐                |
| 적합 | 단순 작업        | 형식/판단 기준이 중요한 작업 |

---

# 30. Checklist Rules

Prompt Engineering 문서에는 Checklist를 포함할 수 있다.

예시:

```md
### [Checklist]

- [ ] 목표가 명확한가?
- [ ] 역할이 정의되어 있는가?
- [ ] 필요한 Context가 포함되어 있는가?
- [ ] 제약 조건이 명확한가?
- [ ] 출력 형식이 지정되어 있는가?
- [ ] 문서에 없는 내용에 대한 처리 규칙이 있는가?
- [ ] 실패 시 행동이 정의되어 있는가?
- [ ] 예시가 필요한 경우 Few-Shot이 포함되어 있는가?
- [ ] Review 기준이 명확한가?
- [ ] 후속 Agent가 처리 가능한 구조인가?
```

---

# 31. Retrieval Optimization Rules

강조 대상 키워드:

- Prompt Engineering
- Prompt Design
- Instruction Design
- Role Prompt
- System Prompt
- User Prompt
- Context Prompt
- RAG Prompt
- Few-Shot Prompt
- Chain-of-Thought Guidance
- Structured Output
- JSON Output
- Markdown Output
- Code Generation Prompt
- Code Review Prompt
- Refactoring Prompt
- Debugging Prompt
- Agent Prompt
- Multi-Agent Prompt
- Constraint
- Hallucination Prevention
- Grounded Answer
- Missing Information Rule
- Prompt Evaluation
- Prompt Template
- Prompt Iteration

키워드 반복 허용.

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

예:

- Prompt Engineering이 뭐야?
- 좋은 Prompt는 어떻게 작성해?
- System Prompt와 User Prompt 차이는?
- RAG Prompt는 어떻게 작성해?
- JSON 출력은 어떻게 강제해?
- 코드 생성 Prompt는 어떻게 작성해?
- 코드 리뷰 Prompt는 어떻게 작성해?
- Agent Prompt에는 뭐가 들어가야 해?
- Hallucination을 줄이려면 어떻게 해?
- Prompt Template은 어떻게 만들어?
- 출력 형식이 깨질 때 어떻게 해?

---

# 32. Version Rules

기준:

- Modern LLM
- RAG 기반 Prompt
- Agent Workflow 기반 Prompt
- Multi-Agent System Prompt
- Structured Output
- Tool Calling 연계 가능 Prompt
- Markdown / JSON Output 기준

Legacy 제외:

- 단순 명령문만 나열하는 Prompt
- 근거 없는 답변을 허용하는 Prompt
- 출력 형식 없는 Prompt
- 실패 처리 없는 Prompt
- 장황한 역할극 중심 Prompt

---

# 33. Common Mistakes

자주 발생:

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

# 34. Final Goal

Prompt Engineering RAG 문서는 Agent가 아래를 수행 가능해야 한다.

- 명확한 Prompt 작성
- System Prompt / User Prompt 구분
- RAG 기반 Prompt 설계
- Role Prompt 작성
- Code Generation Prompt 작성
- Code Review Prompt 작성
- Structured Output Prompt 설계
- JSON Output 유도
- Hallucination 감소
- Agent Prompt 설계
- Multi-Agent Workflow Prompt 설계
- Prompt Template 제작
- Prompt 문제 진단
- Prompt 개선 방향 제안

문서 품질이 Agent 응답 품질과 Workflow 안정성을 결정한다.

---

# Retrieval Queries

### [FAQ]

Q. Prompt Engineering이 뭐야?

A.
LLM이 원하는 작업을 정확히 수행하도록 목표, 맥락, 제약, 출력 형식을 설계하는 작업이다.

Q. 좋은 Prompt는 어떻게 작성해?

A.
Goal, Role, Context, Task, Constraints, Output Format을 명확히 작성한다.

Q. System Prompt와 User Prompt 차이는?

A.
System Prompt는 Agent의 지속적인 상위 규칙이고, User Prompt는 현재 작업 요청이다.

Q. Role Prompt는 왜 필요해?

A.
LLM이 어떤 관점과 책임으로 답변할지 정해 답변 방향을 안정화하기 위해 필요하다.

Q. Context Prompt는 왜 중요해?

A.
LLM은 제공된 Context를 기준으로 답변하므로, 프로젝트 상황과 제약을 정확히 넣어야 한다.

Q. RAG Prompt는 어떻게 작성해?

A.
검색된 문서를 우선 사용하고, 문서에 없는 내용은 없다고 말하며, 추정은 명확히 표시하도록 작성한다.

Q. Few-Shot Prompt는 언제 써?

A.
출력 형식이나 판단 기준을 안정화해야 할 때 예시 입력과 예시 출력을 함께 제공한다.

Q. JSON 출력은 어떻게 유도해?

A.
필드명과 Schema를 명확히 지정하고, “valid JSON only”처럼 부가 설명을 금지하는 제약을 넣는다.

Q. Markdown 출력은 언제 좋아?

A.
사람이 읽는 설명, RAG 문서, 코드 리뷰 결과, 체크리스트를 작성할 때 적합하다.

Q. 코드 생성 Prompt에는 뭐가 필요해?

A.
언어, 프레임워크, 버전, 기존 코드 구조, 프로젝트 규칙, 출력 범위, 예외 처리 기준이 필요하다.

Q. 코드 리뷰 Prompt에는 뭐가 필요해?

A.
리뷰 대상, 검증 기준, Severity, 문제 원인, 수정 방향, 체크리스트가 필요하다.

Q. Debugging Prompt에는 뭐가 들어가야 해?

A.
증상, 에러 메시지, 로그, 환경, 최근 변경, 재현 방법, 기대 결과, 실제 결과가 필요하다.

Q. Agent Prompt에는 뭐가 들어가야 해?

A.
Agent Role, Responsibility, Input, Output, Tools, Constraints, Handoff Rule, Stop Condition이 필요하다.

Q. Multi-Agent Prompt는 어떻게 설계해?

A.
PM Agent가 작업을 분해하고 Domain Agent가 수행하며 Review Agent가 검증하는 흐름과 산출물 형식을 정한다.

Q. Hallucination을 줄이려면 어떻게 해?

A.
문서 근거 우선 규칙, Missing Information Rule, Assumption 표시, 검증 단계를 Prompt에 포함한다.

Q. 출력 형식이 자꾸 깨지면 어떻게 해?

A.
Schema를 단순화하고 예시 출력을 제공하며, 부가 설명을 금지하는 제약을 추가한다.

Q. 답변이 너무 일반적이면 어떻게 해?

A.
프로젝트 Context, 구체적인 제약 조건, 원하는 출력 형식을 추가한다.

Q. Prompt Template은 언제 써?

A.
반복되는 작업을 일정한 품질로 수행해야 할 때 Placeholder 기반 Template을 사용한다.

Q. Prompt는 한 번 만들면 끝이야?

A.
아니다. 출력 결과를 평가하고 실패 유형을 반영해 반복 개선해야 한다.

Q. Prompt Engineering 문서의 최종 목표는 뭐야?

A.
Agent가 정확하고 일관된 지시를 이해하고, 근거 기반으로 구조화된 결과를 생성하도록 돕는 것이다.
