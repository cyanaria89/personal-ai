# Multi-Agent System Part11 - RAG Scope and Context Management

---

# 1. RAG Scope Core

## 1.1 RAG Scope Definition

### [개념]

RAG Scope는 Multi-Agent System에서 각 Agent가 검색하고 참조할 수 있는 RAG 문서 범위이다.

RAG Scope는 Agent가 필요한 Domain 지식만 검색하도록 제한하여 Retrieval 품질을 높이고, 관련 없는 Context가 섞이는 것을 줄인다.

RAG Scope의 핵심은 Agent Role, Task Type, Domain Rules, Tool Permission과 일치하는 검색 범위를 설정하는 것이다.

기본 구조:

```text
Agent Role
→ Task Type
→ Domain
→ RAG Scope
→ Retrieved Context
→ Agent Output
```

개인 AI 개발팀 기준:

```text
PM Agent
→ Master Rules / Project Progress / Agent Rules

SQL Agent
→ SQL / JPA / QueryDSL

Backend Agent
→ Java / Spring Boot / JPA / Security / API Design

Frontend Agent
→ JavaScript / TypeScript / React / Data Fetching

DevOps Agent
→ Git / Docker / Linux / CI/CD

AI Agent
→ Prompt / RAG / Tool Calling / Agent Workflow

Review Agent
→ Master Rules / Domain Rules / Related Output
```

---

### [핵심]

- RAG Scope는 Agent별 검색 문서 범위이다.
- Agent Role과 RAG Scope는 일치해야 한다.
- Task Type에 따라 RAG Scope를 조정한다.
- Scope가 너무 넓으면 관련 없는 Context가 섞인다.
- Scope가 너무 좁으면 필요한 문서가 누락된다.
- PM Agent가 작업별 RAG Scope를 지정할 수 있다.
- Review Agent는 Master Rules와 Domain Rules를 우선 검색한다.
- Fix Agent는 Review Findings와 관련 Domain RAG를 검색한다.
- RAG Scope는 Tool Permission과 함께 제한해야 한다.
- RAG Scope 변경은 Shared State에 기록할 수 있다.

---

### [실무]

2026 실무 기준에서 RAG Scope는 Agent별 기본 Scope와 작업별 추가 Scope로 나누어 관리한다.

기본 Scope:

```json
{
  "agent": "Backend Agent",
  "defaultRagScope": ["Java", "Spring Boot", "JPA Advanced", "API Design"]
}
```

작업별 추가 Scope:

```json
{
  "task": "JWT 기반 회원 인증 API 설계",
  "agent": "Backend Agent",
  "defaultRagScope": ["Java", "Spring Boot", "JPA Advanced", "API Design"],
  "additionalRagScope": ["Security Advanced", "Testing"]
}
```

RAG Scope 선택 Flow:

```text
User Request
→ PM Agent Domain Detection
→ Target Agent Selection
→ Default RAG Scope Load
→ Task-specific RAG Scope Add
→ Retrieval Query Generation
→ Context Packaging
```

RAG Scope 검수 질문:

```text
이 Agent의 Role과 Scope가 일치하는가?
이 Task에 필요한 Domain 문서가 포함되었는가?
불필요한 Domain 문서가 포함되지 않았는가?
Master Rules 또는 Domain Rules가 필요한가?
Review Agent가 검토할 수 있는 기준 문서가 포함되었는가?
```

---

### [FAQ]

Q. RAG Scope가 뭐야?
A. 각 Agent가 검색하고 참조할 수 있는 RAG 문서 범위다.

Q. RAG Scope를 제한하는 이유는?
A. 관련 없는 Context를 줄이고 Retrieval 정확도를 높이기 위해서다.

Q. RAG Scope가 너무 넓으면 어떻게 돼?
A. 관련 없는 문서가 검색되어 Agent Output이 흔들릴 수 있다.

Q. RAG Scope가 너무 좁으면 어떻게 돼?
A. 필요한 문서가 검색되지 않아 Agent가 추측으로 작업할 수 있다.

---

# 2. Agent-Specific RAG Scope

## 2.1 PM Agent RAG Scope

### [개념]

PM Agent RAG Scope는 PM Agent가 요구사항 분석, 작업 분해, Agent Routing, Handoff 생성, 결과 통합을 수행할 때 참조하는 문서 범위이다.

PM Agent는 특정 Domain 구현 지식보다 Master Rules, Project Progress, Agent Rules, Domain Rules Index를 우선 참조한다.

PM Agent RAG Scope의 핵심은 전체 Workflow 기준을 유지하고 필요한 Specialist Agent에게 적절한 Context를 연결하는 것이다.

---

### [핵심]

- PM Agent는 전체 Workflow 기준 문서를 참조한다.
- Master Rules를 우선 적용한다.
- Project Progress를 참고한다.
- Domain Rules Index를 사용해 Target Agent를 선택한다.
- Agent Role 문서를 참조한다.
- Specialist Domain 문서는 필요한 범위만 검색한다.
- PM Agent는 모든 Domain 문서를 무조건 검색하지 않는다.
- Handoff 생성에 필요한 RAG Scope를 지정한다.
- 최종 결과 통합 시 Review Rules를 참조할 수 있다.

---

### [실무]

PM Agent 권장 RAG Scope:

```json
{
  "agent": "PM Agent",
  "defaultRagScope": [
    "Master RAG Rules",
    "Project Progress",
    "Multi-Agent System Domain Rules",
    "Agent Role Design",
    "Agent Communication and Handoff",
    "Shared State and Memory"
  ],
  "conditionalRagScope": [
    "Target Domain Rules",
    "Review Agent Rules",
    "Tool Permission Rules"
  ]
}
```

PM Agent Retrieval 예시:

```text
User Request:
"리뷰 기능 DB부터 화면까지 설계해줘"

PM Agent Retrieval:
- Master RAG Rules
- Multi-Agent System Domain Rules
- Agent Role Design
- SQL Agent Scope
- Backend Agent Scope
- Frontend Agent Scope
- Review Agent Scope
```

PM Agent가 검색하지 않아도 되는 경우:

```text
단순 Routing만 필요한 경우
→ 전체 Backend 세부 문서까지 검색하지 않음

RAG 문서 제작 요청인 경우
→ Target Domain Rules와 Master Rules 우선
→ 무관한 FestaPick 코드 문서 검색하지 않음
```

---

### [FAQ]

Q. PM Agent RAG Scope는 뭐야?
A. PM Agent가 요구사항 분석, 작업 분해, Routing, Handoff, 결과 통합을 위해 참조하는 문서 범위다.

Q. PM Agent는 모든 Domain 문서를 검색해야 해?
A. 아니다. 전체 기준 문서를 우선하고 필요한 Domain 문서만 추가로 검색해야 한다.

Q. PM Agent가 우선 검색할 문서는?
A. Master Rules, Project Progress, Multi-Agent System Domain Rules, Agent Role, Handoff, Shared State 관련 문서다.

Q. PM Agent가 Specialist Domain 문서를 검색하는 경우는?
A. Task 분해와 Handoff 생성을 위해 특정 Domain 제약을 확인해야 할 때다.

---

## 2.2 Specialist Agent RAG Scope

### [개념]

Specialist Agent RAG Scope는 SQL Agent, Backend Agent, Frontend Agent, DevOps Agent, AI Agent, Documentation Agent가 자기 Domain 작업을 수행할 때 참조하는 문서 범위이다.

Specialist Agent는 자기 Domain Rules와 관련 기술 문서를 우선 검색하고, Scope 밖 문서는 PM Agent가 명시적으로 추가한 경우에만 참조한다.

---

### [핵심]

- Specialist Agent는 자기 Domain 문서를 우선 검색한다.
- Domain Rules를 우선 적용한다.
- Task와 직접 관련된 문서만 검색한다.
- Scope 밖 문서는 기본 검색 대상이 아니다.
- 필요한 경우 PM Agent가 추가 RAG Scope를 지정한다.
- Specialist Agent는 검색 결과의 출처 Domain을 확인해야 한다.
- 불충분한 검색 결과는 Missing Context로 표시한다.
- 관련 없는 RAG Context는 Output 근거로 사용하지 않는다.

---

### [실무]

Specialist Agent RAG Scope Matrix:

| Agent               | Default RAG Scope                         | Conditional RAG Scope       |
| ------------------- | ----------------------------------------- | --------------------------- |
| SQL Agent           | SQL, JPA Advanced, QueryDSL               | API Design, Testing         |
| Backend Agent       | Java, Spring Boot, JPA, API Design        | Security, Testing, QueryDSL |
| Frontend Agent      | HTML, CSS, JavaScript, TypeScript, React  | API Design, Error Handling  |
| DevOps Agent        | Git, Docker, Linux, CI/CD                 | Monitoring, Security        |
| AI Agent            | Prompt, RAG, Tool Calling, Agent Workflow | LangGraph, Evaluation       |
| Documentation Agent | Master Rules, Target Domain Rules         | Related Domain Documents    |
| Review Agent        | Master Rules, Domain Rules, Project Rules | Target Domain RAG           |
| Fix Agent           | Review Finding Related Domain             | Original Agent RAG Scope    |

Backend Agent Scope 예시:

```json
{
  "agent": "Backend Agent",
  "task": "Review API 설계",
  "ragScope": [
    "Java",
    "Spring Boot",
    "JPA Advanced",
    "API Design",
    "Security Advanced"
  ],
  "excludedScope": [
    "React Component Design",
    "Docker Deployment",
    "Prompt Engineering"
  ]
}
```

---

### [FAQ]

Q. Specialist Agent RAG Scope는 뭐야?
A. 특정 Domain Agent가 자기 작업을 수행할 때 참조하는 Domain 문서 범위다.

Q. Specialist Agent가 Scope 밖 문서를 검색해도 돼?
A. 기본적으로 하지 않는다. PM Agent가 작업상 필요하다고 지정한 경우에만 추가한다.

Q. Backend Agent의 기본 RAG Scope는?
A. Java, Spring Boot, JPA, API Design이며 작업에 따라 Security, Testing을 추가한다.

Q. Documentation Agent의 기본 RAG Scope는?
A. Master Rules, Target Domain Rules, Project Progress, 관련 기존 문서다.

---

## 2.3 Review and Fix RAG Scope

### [개념]

Review Agent와 Fix Agent의 RAG Scope는 일반 Specialist Agent와 다르다.

Review Agent는 산출물을 검토하기 위해 Master Rules, Domain Rules, Target Output, Shared State, Related Domain RAG를 함께 참조한다.

Fix Agent는 Review Findings를 반영하기 위해 Review Target의 Domain RAG와 Fix Scope 관련 문서를 참조한다.

---

### [핵심]

- Review Agent는 검토 기준 문서를 우선 검색한다.
- Review Agent는 Master Rules와 Domain Rules를 우선 적용한다.
- Review Agent는 Target Output과 Handoff를 함께 참조한다.
- Fix Agent는 Review Findings와 Target Output을 우선 참조한다.
- Fix Agent는 수정 대상 Domain RAG를 검색한다.
- Fix Agent는 Review 범위 밖 RAG를 과도하게 검색하지 않는다.
- Review-Fix Loop에서 RAG Scope가 계속 바뀌면 안 된다.
- RAG Scope 변경이 필요하면 PM Agent가 결정한다.

---

### [실무]

Review Agent RAG Scope:

```json
{
  "agent": "Review Agent",
  "task": "RAG document review",
  "ragScope": [
    "Master RAG Rules",
    "Target Domain Rules",
    "Project Progress",
    "Target Document",
    "Related Part Documents"
  ],
  "reviewCriteria": [
    "Required Sections",
    "FAQ Quality",
    "Retrieval Queries",
    "Terminology Consistency",
    "Output Format Compliance"
  ]
}
```

Fix Agent RAG Scope:

```json
{
  "agent": "Fix Agent",
  "task": "Apply Review Findings to RAG document",
  "ragScope": [
    "Review Report",
    "Target Document",
    "Master RAG Rules",
    "Target Domain Rules"
  ],
  "fixScope": [
    "Findings only",
    "Preserve original requirements",
    "No new requirement creation"
  ]
}
```

Review-Fix RAG Scope 주의:

```text
Review Agent가 새로운 기준 문서를 계속 추가
→ Review 기준 변경
→ Fix Agent 수정 범위 증가
→ Review-Fix Loop 반복 가능

해결:
→ Review Criteria 고정
→ Max Iteration 설정
→ PM Agent Decision 필요
```

---

### [FAQ]

Q. Review Agent RAG Scope는 뭐야?
A. 산출물을 검토하기 위해 Master Rules, Domain Rules, Target Output, Shared State, Related Domain RAG를 포함하는 검색 범위다.

Q. Fix Agent RAG Scope는 뭐야?
A. Review Findings를 반영하기 위해 Target Output, Review Report, 수정 대상 Domain RAG를 포함하는 검색 범위다.

Q. Review-Fix 중 RAG Scope를 계속 바꿔도 돼?
A. 안 된다. 기준이 계속 바뀌면 Review-Fix Loop가 반복될 수 있다.

Q. Review 기준 문서는 누가 정해?
A. PM Agent가 Handoff와 Shared State 기준으로 정하고 Review Agent가 적용한다.

---

# 3. Retrieval Query Design

## 3.1 Retrieval Query Definition

### [개념]

Retrieval Query는 RAG 시스템에서 필요한 문서를 검색하기 위해 사용하는 질문 또는 검색 문장이다.

Retrieval Query는 사용자 질문을 그대로 사용하는 방식보다 Agent Role, Task Type, Domain, Expected Output에 맞게 재작성하는 것이 좋다.

Retrieval Query의 핵심은 검색 대상 문서의 표현과 사용자 요청 표현을 연결하는 것이다.

기본 구조:

```text
User Request
→ Task Intent
→ Domain Keywords
→ Rule Keywords
→ Retrieval Query
→ Retrieved Context
```

---

### [핵심]

- Retrieval Query는 RAG 검색 품질에 직접 영향을 준다.
- 사용자 질문을 그대로 쓰면 검색 품질이 낮을 수 있다.
- Agent Role에 맞게 Query를 재작성한다.
- Domain 용어를 포함한다.
- Required Section 이름을 포함할 수 있다.
- FAQ 표현을 포함하면 검색 매칭이 좋아진다.
- 너무 긴 Query는 핵심 키워드가 희석될 수 있다.
- 너무 짧은 Query는 문서 범위가 넓어질 수 있다.
- Query는 여러 개로 분해할 수 있다.

---

### [실무]

Retrieval Query Template:

```json
{
  "userRequest": "PM Agent 역할 문서 찾아줘",
  "agent": "PM Agent",
  "taskType": "RAG Retrieval",
  "queries": [
    "PM Agent 역할 요구사항 분석 작업 분해 Handoff",
    "PM Agent Agent Routing Shared State 결과 통합",
    "Multi-Agent System PM Agent FAQ"
  ]
}
```

Backend Agent Retrieval Query 예시:

```text
Spring Boot Review API Contract DTO Service Exception Security
JPA Review Entity Relationship Transaction Validation
API Design ApiResponse Slice Pagination Error Response
```

RAG 문서 제작 Retrieval Query 예시:

```text
MASTER_RAG_RULES Required Sections FAQ Retrieval Queries
Multi-Agent System Domain Rules Handoff Shared State Agent Role
RAG 문서 제작 출력 형식 writing block FAQ 강화
```

나쁜 Query 예시:

```text
이거 해줘
```

문제:

- Domain 없음
- Task Type 없음
- 검색 키워드 없음
- Target Document 매칭 어려움

---

### [FAQ]

Q. Retrieval Query가 뭐야?
A. RAG 시스템에서 필요한 문서를 검색하기 위해 사용하는 질문 또는 검색 문장이다.

Q. 사용자 질문을 그대로 검색하면 안 돼?
A. 가능하지만 검색 품질이 낮을 수 있으므로 Agent Role과 Domain에 맞게 재작성하는 것이 좋다.

Q. 좋은 Retrieval Query 조건은?
A. Domain 용어, Task Type, 필요한 Output, Rule 키워드가 포함되어야 한다.

Q. Retrieval Query는 여러 개 만들어도 돼?
A. 가능하다. 복합 요청은 여러 Query로 분해하는 것이 좋다.

---

## 3.2 Query Expansion

### [개념]

Query Expansion은 초기 Retrieval Query에 관련 용어, 동의어, Domain 키워드, FAQ 표현을 추가해 검색 범위를 보강하는 작업이다.

Query Expansion은 필요한 문서가 검색되지 않을 때 유용하지만, 과도하게 확장하면 관련 없는 문서가 섞일 수 있다.

기본 구조:

```text
Base Query
→ Domain Terms
→ Synonyms
→ FAQ Phrases
→ Related Rule Names
→ Expanded Queries
```

---

### [핵심]

- Query Expansion은 검색 범위 보강이다.
- Domain 용어를 추가한다.
- 관련 Agent 이름을 추가한다.
- Section 이름을 추가할 수 있다.
- FAQ 질문 표현을 추가할 수 있다.
- 약어와 풀네임을 함께 사용할 수 있다.
- 과도한 확장은 Precision을 낮출 수 있다.
- Expansion은 PM Agent 또는 AI Agent가 수행할 수 있다.

---

### [실무]

Query Expansion 예시:

```json
{
  "baseQuery": "Handoff",
  "expandedQueries": [
    "Agent Handoff Task Context Requirements Constraints",
    "Handoff Quality Checklist Expected Output Done Criteria",
    "Poor Handoff Missing Requirement Missing Constraint",
    "Agent Communication Handoff Message Type"
  ]
}
```

용어 확장 예시:

| Base Term | Expanded Terms                                     |
| --------- | -------------------------------------------------- |
| Handoff   | Agent Communication, Message, Task Transfer        |
| State     | Shared State, Workflow State, Decision State       |
| Memory    | Long-term Memory, Project Memory, User Preference  |
| Review    | Review Finding, Review Report, Severity, Pass Fail |
| Fix       | Fix Scope, Applied Fix, Regression Risk            |
| Tool      | Tool Permission, Human Approval, Dangerous Tool    |

확장 실패 예시:

```text
Base Query:
Backend API

Over-expanded Query:
Backend API React Docker Linux Prompt RAG Security SQL Frontend Payment Email Deploy

문제:
- 너무 많은 Domain 포함
- 검색 Precision 저하
- Context 혼합 가능성 증가
```

---

### [FAQ]

Q. Query Expansion이 뭐야?
A. 초기 검색 Query에 관련 용어와 FAQ 표현을 추가해 검색 범위를 보강하는 작업이다.

Q. Query Expansion은 언제 사용해?
A. 필요한 문서가 검색되지 않거나 검색 결과가 부족할 때 사용한다.

Q. Query Expansion을 많이 하면 좋아?
A. 아니다. 과도하게 확장하면 관련 없는 문서가 섞일 수 있다.

Q. Query Expansion은 누가 수행해?
A. PM Agent, AI Agent, Documentation Agent가 수행할 수 있다.

---

## 3.3 Query Narrowing

### [개념]

Query Narrowing은 검색 결과가 너무 넓거나 관련 없는 문서가 많이 나올 때 Query를 좁히는 작업이다.

Query Narrowing은 Domain, Agent Role, Section, FileName, Output Type을 기준으로 검색 범위를 제한한다.

기본 구조:

```text
Broad Query
→ Add Domain
→ Add Agent Role
→ Add Section
→ Add Output Type
→ Narrowed Query
```

---

### [핵심]

- Query Narrowing은 검색 범위 축소이다.
- Domain을 명확히 추가한다.
- Agent 이름을 추가한다.
- 문서 Part 이름을 추가한다.
- Section 이름을 추가한다.
- Output Type을 추가한다.
- 불필요한 Domain 키워드는 제거한다.
- Narrowing은 Precision을 높인다.
- 너무 좁히면 Recall이 낮아질 수 있다.

---

### [실무]

Query Narrowing 예시:

```text
Broad Query:
Agent

Narrowed Query:
Multi-Agent System PM Agent Requirement Analysis Handoff

More Narrowed Query:
Multi-Agent System Part03 PM Agent Handoff Generation Done Criteria FAQ
```

RAG 문서 검수 Query Narrowing:

```text
Broad Query:
RAG 문서 검수

Narrowed Query:
MASTER_RAG_RULES Required Section FAQ Retrieval Queries Output Format

More Narrowed Query:
Multi-Agent System Domain Rules Documentation Agent RAG Document Review FAQ Retrieval Queries
```

Backend Query Narrowing:

```text
Broad Query:
Review

Narrowed Query:
Spring Boot Review API DTO Service Exception Security

More Narrowed Query:
Review API author check rating validation ApiResponse Slice JPA
```

---

### [FAQ]

Q. Query Narrowing이 뭐야?
A. 검색 결과가 너무 넓을 때 Domain, Agent Role, Section 등을 추가해 검색 범위를 좁히는 작업이다.

Q. Query Narrowing은 언제 필요해?
A. 관련 없는 문서가 많이 검색되거나 Context가 너무 넓어질 때 필요하다.

Q. Query Narrowing 기준은?
A. Domain, Agent Role, FileName, Section, Output Type, Task Type이다.

Q. 너무 좁히면 어떻게 돼?
A. 필요한 문서가 검색되지 않을 수 있다.

---

# 4. Context Management Core

## 4.1 Context Management Definition

### [개념]

Context Management는 Multi-Agent System에서 Agent가 사용할 Context를 선택, 압축, 정리, 우선순위화하는 작업이다.

Context Management는 RAG Scope, Retrieved Context, Shared State, Memory, User Request, Agent Output을 적절히 조합해 Agent가 정확히 작업할 수 있게 만든다.

기본 구조:

```text
User Request
→ Shared State
→ RAG Context
→ Memory
→ Tool Result
→ Context Packaging
→ Agent Input
```

---

### [핵심]

- Context Management는 Agent Input 품질을 결정한다.
- 모든 Context를 넣으면 안 된다.
- 현재 User Request를 최우선으로 한다.
- Shared State의 최신 Decision을 포함한다.
- RAG Context는 Task와 직접 관련된 것만 포함한다.
- Memory는 관련 있을 때만 포함한다.
- Tool Result는 요약해서 포함한다.
- 오래된 Context는 최신 요청보다 후순위다.
- 충돌 Context는 명시적으로 처리한다.
- Context가 부족하면 Missing Context로 표시한다.

---

### [실무]

Context Management Flow:

```text
1. Current User Request 확인
2. Task Type 확인
3. Target Agent 확인
4. Shared State Decision 추출
5. RAG Scope 선택
6. Retrieval Query 생성
7. Retrieved Context 필터링
8. Memory 관련성 확인
9. Context Conflict 확인
10. Agent Input으로 Packaging
```

Agent Input Context Package 예시:

```json
{
  "targetAgent": "Backend Agent",
  "currentUserRequest": "축제 리뷰 API 설계",
  "requirements": ["리뷰 작성", "리뷰 목록 조회", "리뷰 수정", "리뷰 삭제"],
  "decisions": ["Review list uses Slice", "Rating range is 0 to 5"],
  "ragContext": [
    "Spring Boot API Design Rules",
    "JPA Relationship Rules",
    "Security Authorization Rules"
  ],
  "excludedContext": ["Frontend UI styling rules", "Docker deploy rules"],
  "openQuestions": ["중복 리뷰 허용 여부"]
}
```

---

### [FAQ]

Q. Context Management가 뭐야?
A. Agent가 사용할 User Request, Shared State, RAG Context, Memory, Tool Result를 선택하고 정리하는 작업이다.

Q. 모든 Context를 넣으면 안 되는 이유는?
A. Token 낭비와 지시 혼선이 생기고 관련 없는 정보가 Agent 판단을 흐릴 수 있기 때문이다.

Q. Context Management에서 가장 중요한 기준은?
A. 현재 User Request와 최신 Shared State Decision이다.

Q. Context가 부족하면 어떻게 해?
A. Missing Context, Assumption, Open Question으로 표시해야 한다.

---

## 4.2 Context Priority

### [개념]

Context Priority는 여러 Context가 동시에 존재하거나 충돌할 때 어떤 정보를 우선할지 정하는 기준이다.

Context Priority가 없으면 Agent가 오래된 Memory나 관련 없는 RAG Context를 현재 요청보다 우선할 수 있다.

권장 우선순위:

```text
Current User Request
→ Explicit PM Agent Decision
→ Master Rules
→ Domain Rules
→ Current Shared State
→ Current Handoff
→ Retrieved RAG Context
→ Tool Result
→ Long-term Memory
→ Older Conversation
```

---

### [핵심]

- 현재 User Request가 최우선이다.
- PM Agent Decision은 Workflow 기준이다.
- Master Rules는 공통 규칙이다.
- Domain Rules는 Domain별 기준이다.
- Shared State는 현재 작업 상태이다.
- Handoff는 Target Agent의 직접 작업 지시이다.
- RAG Context는 근거 지식이다.
- Tool Result는 실행 결과이다.
- Memory는 보조 Context이다.
- 오래된 대화는 후순위이다.
- 충돌 시 우선순위를 명시한다.

---

### [실무]

Context Priority 적용 예시:

```text
Current User Request:
- 중간 응답 금지
- 최종 결과만 출력

General Operation Rule:
- 장기 작업 시 중간 업데이트 제공

Decision:
- Current User Request 우선
- 중간 업데이트 없이 최종 writing block만 출력
```

RAG 문서 제작 기준:

```text
Current User Output Format
→ Master RAG Rules
→ Multi-Agent System Domain Rules
→ Project Progress
→ Previous Part Documents
→ General Writing Preference
```

Backend 작업 기준:

```text
Current User Request
→ PM Agent Handoff
→ Project Code / File Context
→ Backend Domain Rules
→ Spring Boot RAG Context
→ Older Project Memory
```

Context Conflict Record:

```md
## Context Conflict

### Conflict

Retrieved RAG Context suggests Page pagination, but PM Decision specifies Slice

### Priority

PM Agent Decision > Retrieved RAG Context

### Decision

Use Slice

### Impact

Backend and Frontend Output must follow Slice response structure
```

---

### [FAQ]

Q. Context Priority가 뭐야?
A. 여러 Context가 존재하거나 충돌할 때 어떤 정보를 우선할지 정하는 기준이다.

Q. 가장 우선하는 Context는?
A. 현재 User Request다.

Q. RAG Context와 PM Decision이 충돌하면?
A. 명시된 PM Agent Decision이 우선이다.

Q. Memory와 현재 요청이 충돌하면?
A. 현재 요청이 우선이다.

---

# 5. Context Packaging

## 5.1 Context Packaging Definition

### [개념]

Context Packaging은 Agent에게 전달할 Context를 선택, 요약, 구조화해 Agent Input으로 만드는 작업이다.

Context Packaging은 Context Management의 실행 단계이며, Handoff 품질과 Agent Output 품질에 직접 영향을 준다.

기본 구조:

```text
Raw Context
→ Filter
→ Summarize
→ Prioritize
→ Structure
→ Attach to Handoff
```

---

### [핵심]

- Context Packaging은 Agent Input 구성 작업이다.
- 필요한 Context만 포함한다.
- 관련 없는 Context는 제외한다.
- 요구사항과 제약사항을 분리한다.
- Decision과 Assumption을 분리한다.
- Retrieved RAG Context를 요약한다.
- Tool Result는 핵심 결과만 포함한다.
- Open Questions를 포함한다.
- Context 출처를 표시할 수 있다.
- Target Agent가 바로 작업할 수 있어야 한다.

---

### [실무]

Context Package Template:

```json
{
  "contextPackageId": "CTX-001",
  "targetAgent": "Frontend Agent",
  "priority": [
    "Current User Request",
    "Backend API Contract",
    "Shared State Decision",
    "React RAG Context"
  ],
  "requirements": [
    "Review list UI",
    "Review create form",
    "Review edit/delete action"
  ],
  "constraints": [
    "Use existing Backend API Contract",
    "Handle Loading / Error / Empty State"
  ],
  "decisions": ["Review list uses Slice", "Rating range is 0 to 5"],
  "ragContextSummary": [
    "React component should separate container and presentational responsibility",
    "Data fetching should handle loading, error, success states"
  ],
  "toolResultSummary": [
    "Backend API Contract includes GET, POST, PATCH, DELETE endpoints"
  ],
  "assumptions": ["ReviewResDto field names may require confirmation"],
  "openQuestions": ["Pagination response field names are not confirmed"],
  "excludedContext": [
    "Docker deployment notes",
    "SQL index details not needed for Frontend Agent"
  ]
}
```

Packaging 품질 기준:

```text
필요한 정보는 빠지지 않았는가?
불필요한 정보는 제거되었는가?
요구사항과 제약이 분리되었는가?
Decision과 Assumption이 구분되었는가?
Target Agent Scope에 맞는가?
```

---

### [FAQ]

Q. Context Packaging이 뭐야?
A. Agent에게 전달할 Context를 선택, 요약, 구조화해 Agent Input으로 만드는 작업이다.

Q. Context Packaging이 중요한 이유는?
A. Agent가 필요한 정보만 받아야 정확한 Output을 만들 수 있기 때문이다.

Q. Context Package에는 뭐가 들어가야 해?
A. Requirements, Constraints, Decisions, RAG Context Summary, Tool Result Summary, Assumptions, Open Questions가 들어가야 한다.

Q. Context Packaging에서 제외할 정보는?
A. Target Agent 작업과 무관한 Domain 정보, 오래된 정보, 중복 정보, 민감정보다.

---

## 5.2 Context Compression

### [개념]

Context Compression은 긴 Context를 핵심 정보 중심으로 압축하는 작업이다.

Context Compression은 Token 사용량을 줄이고 Agent가 핵심 요구사항에 집중하도록 돕는다.

단, Compression 과정에서 중요한 제약사항, 결정사항, Open Question이 삭제되면 안 된다.

기본 구조:

```text
Long Context
→ Extract Requirements
→ Extract Decisions
→ Extract Risks
→ Remove Noise
→ Compressed Context
```

---

### [핵심]

- Context Compression은 긴 Context를 줄이는 작업이다.
- 요구사항은 보존한다.
- 제약사항은 보존한다.
- 결정사항은 보존한다.
- Open Questions는 보존한다.
- 불필요한 대화와 중복 설명은 제거한다.
- Agent 내부 추론 과정은 포함하지 않는다.
- 너무 과도하게 압축하면 의미가 손상된다.
- 압축 결과는 Agent가 바로 사용할 수 있어야 한다.

---

### [실무]

Compression 전:

```text
사용자가 리뷰 기능을 만들어달라고 했고, 예전에 Slice를 쓰자고 했고,
ApiResponse 형식을 써야 하고, JWT 인증이 들어가야 하고,
중복 리뷰는 아직 정하지 않았고, 프론트는 React고,
예전에 Docker 배포 얘기도 했고, 카카오맵도 있었고...
```

Compression 후:

```json
{
  "requirements": ["Festival review create/list/update/delete"],
  "constraints": [
    "JWT Authentication",
    "ApiResponse format",
    "Use Slice for list response",
    "React frontend"
  ],
  "decisions": ["Rating range is 0 to 5"],
  "openQuestions": ["Duplicate review policy not confirmed"],
  "excludedContext": ["Docker deployment notes", "Kakao Map notes"]
}
```

Compression Checklist:

```md
## Context Compression Checklist

- [ ] 핵심 User Request가 유지되었는가?
- [ ] Requirements가 유지되었는가?
- [ ] Constraints가 유지되었는가?
- [ ] Decisions가 유지되었는가?
- [ ] Open Questions가 유지되었는가?
- [ ] Risks가 유지되었는가?
- [ ] 관련 없는 Context가 제거되었는가?
- [ ] 의미가 왜곡되지 않았는가?
```

---

### [FAQ]

Q. Context Compression이 뭐야?
A. 긴 Context를 요구사항, 결정사항, 위험, 미확정 사항 중심으로 압축하는 작업이다.

Q. Context Compression에서 삭제하면 안 되는 것은?
A. 핵심 요구사항, 제약사항, 결정사항, Open Questions, 위험 요소다.

Q. Context Compression이 필요한 이유는?
A. Token 사용량을 줄이고 Agent가 핵심 정보에 집중하도록 하기 위해서다.

Q. 너무 압축하면 어떻게 돼?
A. 중요한 의미가 손상되어 Agent가 잘못된 결과를 만들 수 있다.

---

# 6. Retrieval Quality Control

## 6.1 Retrieval Quality Definition

### [개념]

Retrieval Quality는 RAG 검색 결과가 현재 Agent Task에 얼마나 관련 있고 충분하며 정확한지를 나타내는 기준이다.

Retrieval Quality가 낮으면 Agent는 관련 없는 문서를 근거로 사용하거나 필요한 문서 없이 추측할 수 있다.

기본 구조:

```text
Retrieval Query
→ Retrieved Context
→ Relevance Check
→ Sufficiency Check
→ Conflict Check
→ Context Use Decision
```

---

### [핵심]

- Retrieval Quality는 검색 결과 품질이다.
- 검색 결과가 Task와 관련 있어야 한다.
- 검색 결과가 충분해야 한다.
- 검색 결과가 최신 Decision과 충돌하지 않아야 한다.
- 검색 결과의 Domain이 Target Agent와 맞아야 한다.
- 관련 없는 Context는 제외해야 한다.
- 검색 결과가 부족하면 Query Expansion 또는 Scope 확장이 필요하다.
- 검색 결과가 너무 넓으면 Query Narrowing이 필요하다.
- 충돌 Context는 우선순위 기준으로 처리한다.

---

### [실무]

Retrieval Quality Checklist:

```md
## Retrieval Quality Checklist

- [ ] Retrieved Context가 Task와 직접 관련 있는가?
- [ ] Target Agent Domain과 일치하는가?
- [ ] Requirements 해결에 필요한 정보가 포함되어 있는가?
- [ ] Constraints 확인에 필요한 정보가 포함되어 있는가?
- [ ] Domain Rules와 충돌하지 않는가?
- [ ] Shared State Decision과 충돌하지 않는가?
- [ ] 너무 오래된 정보가 아닌가?
- [ ] 중복 Context가 과도하지 않은가?
- [ ] 불필요한 Domain Context가 섞이지 않았는가?
- [ ] 결과가 부족하면 Query Expansion이 필요한가?
- [ ] 결과가 너무 넓으면 Query Narrowing이 필요한가?
```

Retrieval Quality Decision 예시:

```json
{
  "retrievalStatus": "partial",
  "relevance": "medium",
  "sufficiency": "insufficient",
  "issue": "Backend API Design context found, but Security authorization rule missing",
  "action": "Expand RAG Scope to Security Advanced"
}
```

---

### [FAQ]

Q. Retrieval Quality가 뭐야?
A. RAG 검색 결과가 현재 Agent Task에 얼마나 관련 있고 충분하며 정확한지를 나타내는 기준이다.

Q. Retrieval Quality가 낮으면 어떻게 돼?
A. Agent가 관련 없는 문서를 근거로 사용하거나 필요한 문서 없이 추측할 수 있다.

Q. 검색 결과가 부족하면 어떻게 해?
A. Query Expansion 또는 RAG Scope 확장을 수행한다.

Q. 검색 결과가 너무 넓으면 어떻게 해?
A. Query Narrowing으로 Domain과 Task 범위를 좁힌다.

---

## 6.2 Context Conflict in Retrieval

### [개념]

Context Conflict in Retrieval은 검색된 RAG Context가 현재 User Request, Shared State Decision, Domain Rules, Agent Output과 충돌하는 상태이다.

검색 결과가 RAG에서 나왔다고 해서 항상 우선되는 것은 아니다.

기본 구조:

```text
Retrieved Context
→ Compare with Current User Request
→ Compare with Shared State Decision
→ Compare with Domain Rules
→ Resolve Conflict
```

---

### [핵심]

- RAG Context도 충돌할 수 있다.
- 현재 User Request가 RAG Context보다 우선이다.
- Shared State Decision이 일반 RAG Context보다 우선이다.
- Master Rules와 Domain Rules가 일반 설명보다 우선이다.
- 검색 결과가 오래된 문서일 수 있다.
- 충돌은 무시하지 않고 기록한다.
- 충돌 해결 기준을 Handoff나 Review Report에 포함할 수 있다.

---

### [실무]

Retrieval Conflict 예시:

```md
## Retrieval Context Conflict

### Conflict

Retrieved Context recommends `Page` pagination, but Shared State Decision specifies `Slice`

### Priority

Shared State Decision > Retrieved RAG Context

### Decision

Use Slice

### Impact

Backend DTO and Frontend State must follow Slice-based response

### Action

Exclude Page-based context from current Agent Input
```

RAG 문서 제작 충돌 예시:

```md
## Retrieval Context Conflict

### Conflict

Retrieved writing guide suggests narrative explanation, but Master RAG Rules require Retrieval optimized structure

### Priority

Master RAG Rules > General Writing Guide

### Decision

Use structured RAG format with Required Sections and Retrieval Queries

### Action

Exclude narrative writing guide from final document generation
```

---

### [FAQ]

Q. Retrieval Context Conflict가 뭐야?
A. 검색된 RAG Context가 현재 요청, Shared State Decision, Domain Rules와 충돌하는 상태다.

Q. RAG에서 검색된 내용은 항상 맞아?
A. 아니다. 현재 요청, PM Decision, Master Rules, Domain Rules와 충돌하면 후순위다.

Q. Retrieval Context Conflict는 어떻게 처리해?
A. 우선순위 기준으로 결정하고 충돌 내용을 기록한 뒤 관련 없는 Context를 제외한다.

Q. RAG Context와 현재 요청이 충돌하면?
A. 현재 요청이 우선이다.

---

# 7. RAG Scope Failure Handling

## 7.1 RAG Scope Failure Cases

### [개념]

RAG Scope Failure는 Agent가 잘못된 문서 범위를 검색하거나, 필요한 문서를 누락하거나, 관련 없는 Context를 사용해 Output 품질이 떨어지는 문제이다.

RAG Scope Failure는 Agent Hallucination, Domain Rule 위반, Output 충돌의 원인이 된다.

주요 실패 유형:

```text
Scope Too Broad
Scope Too Narrow
Wrong Domain Scope
Missing Master Rules
Missing Domain Rules
Stale RAG Context
Unfiltered Retrieved Context
RAG Context Overtrust
```

---

### [핵심]

- Scope가 너무 넓으면 관련 없는 Context가 섞인다.
- Scope가 너무 좁으면 필요한 문서가 누락된다.
- 잘못된 Domain Scope는 잘못된 Agent Output을 만든다.
- Master Rules 누락은 문서 구조 위반으로 이어진다.
- Domain Rules 누락은 도메인 품질 저하로 이어진다.
- 오래된 RAG Context는 현재 Decision과 충돌할 수 있다.
- 검색 결과 필터링이 없으면 Context 혼합이 발생한다.
- RAG Context를 과신하면 현재 User Request를 무시할 수 있다.

---

### [실무]

RAG Scope Failure 대응 기준:

| Failure Type         | Cause                    | Handling                     |
| -------------------- | ------------------------ | ---------------------------- |
| Scope Too Broad      | 너무 많은 Domain 포함    | Query Narrowing              |
| Scope Too Narrow     | 필요한 문서 누락         | Query Expansion / Scope 확장 |
| Wrong Domain Scope   | Agent Role 오판          | PM Agent Routing 재검토      |
| Missing Master Rules | 공통 규칙 미검색         | Master Rules 추가            |
| Missing Domain Rules | Target Domain 규칙 누락  | Domain Rules 추가            |
| Stale RAG Context    | 오래된 문서 사용         | Current Decision 우선        |
| Unfiltered Context   | 검색 결과 그대로 사용    | Context Packaging 적용       |
| RAG Overtrust        | RAG를 절대 기준으로 사용 | Context Priority 적용        |

RAG Scope Failure Output 예시:

```md
## RAG Scope Failure

### Failure Type

Missing Domain Rules

### Issue

Documentation Agent가 Multi-Agent System Domain Rules를 참조하지 않고 Part 문서를 작성함

### Impact

Domain 용어와 Required Scope가 문서에 반영되지 않을 수 있음

### Fix Direction

Target Domain Rules를 RAG Scope에 추가하고 문서 구조를 재검토

### Re-review Required

Yes
```

---

### [FAQ]

Q. RAG Scope Failure는 언제 발생해?
A. Agent가 잘못된 문서 범위를 검색하거나 필요한 문서를 누락하거나 관련 없는 Context를 사용할 때 발생한다.

Q. Scope Too Broad는 뭐야?
A. RAG Scope가 너무 넓어 관련 없는 Domain 문서가 검색되는 상태다.

Q. Scope Too Narrow는 뭐야?
A. RAG Scope가 너무 좁아 필요한 문서가 검색되지 않는 상태다.

Q. RAG Scope Failure는 어떻게 줄여?
A. Agent Role 기반 Scope 설정, Query Expansion, Query Narrowing, Context Packaging을 적용한다.

---

## 7.2 Context Management Failure

### [개념]

Context Management Failure는 Agent Input에 필요한 Context가 누락되거나, 관련 없는 Context가 과도하게 포함되거나, 오래된 Context가 최신 요청을 덮는 문제이다.

Context Management Failure는 Multi-Agent System에서 Output 품질 저하의 주요 원인이다.

주요 실패 유형:

```text
Missing Context
Context Overload
Stale Context
Context Conflict
Uncompressed Context
Lost Constraint
Lost Decision
Memory Overuse
Tool Result Missing
```

---

### [핵심]

- Missing Context는 Agent 추측을 만든다.
- Context Overload는 핵심 지시를 묻히게 한다.
- Stale Context는 최신 요청과 충돌한다.
- Context Conflict는 명시적으로 해결해야 한다.
- Uncompressed Context는 Token 낭비를 만든다.
- Lost Constraint는 규칙 위반을 만든다.
- Lost Decision은 Agent 간 충돌을 만든다.
- Memory Overuse는 관련 없는 과거 정보를 섞는다.
- Tool Result Missing은 실행 결과 추적을 어렵게 한다.

---

### [실무]

Context Management Failure 대응 기준:

| Failure Type        | Cause                 | Handling                  |
| ------------------- | --------------------- | ------------------------- |
| Missing Context     | 필요한 정보 누락      | Required Context 요청     |
| Context Overload    | 전체 대화 전달        | Context Packaging         |
| Stale Context       | 오래된 정보 사용      | Current User Request 우선 |
| Context Conflict    | 정보 충돌             | Context Priority 적용     |
| Lost Constraint     | 압축 중 제약 삭제     | Constraint 복구           |
| Lost Decision       | 결정사항 누락         | Shared State 확인         |
| Memory Overuse      | 관련 없는 Memory 사용 | Memory Filtering          |
| Tool Result Missing | 결과 기록 누락        | Tool Result State 추가    |

Context Failure Output 예시:

```md
## Context Management Failure

### Failure Type

Lost Constraint

### Issue

Context Compression 과정에서 "Use Slice for list response" 제약이 누락됨

### Impact

Backend Agent가 Page 기반 API를 설계할 수 있음

### Fix Direction

Compressed Context의 Constraints에 Slice 사용 기준을 복구

### Re-review Required

Yes
```

---

### [FAQ]

Q. Context Management Failure는 언제 발생해?
A. 필요한 Context가 누락되거나 관련 없는 Context가 과도하게 포함되거나 오래된 Context가 최신 요청을 덮을 때 발생한다.

Q. Missing Context는 왜 위험해?
A. Agent가 추측으로 작업해 Hallucination이나 잘못된 Output을 만들 수 있기 때문이다.

Q. Context Overload는 왜 문제야?
A. 너무 많은 정보가 핵심 지시를 묻히게 하고 Token 낭비를 만든다.

Q. Lost Constraint는 어떻게 막아?
A. Context Compression 후 Requirements, Constraints, Decisions, Open Questions가 보존되었는지 확인한다.

---

# 8. RAG Scope and Context Checklist

## 8.1 RAG Scope Checklist

### [개념]

RAG Scope Checklist는 Agent별 RAG Scope가 현재 Task와 Agent Role에 맞는지 검수하는 기준이다.

Checklist를 적용하면 잘못된 문서 검색, Domain Rules 누락, 관련 없는 Context 혼합을 줄일 수 있다.

---

### [핵심]

- Agent Role을 확인한다.
- Task Type을 확인한다.
- Primary Domain을 확인한다.
- Required Domain Rules를 확인한다.
- Master Rules 필요 여부를 확인한다.
- Default RAG Scope를 확인한다.
- Additional RAG Scope를 확인한다.
- Excluded Scope를 확인한다.
- Scope가 너무 넓거나 좁지 않은지 확인한다.
- 검색 결과가 Task와 관련 있는지 확인한다.

---

### [실무]

RAG Scope Checklist:

```md
## RAG Scope Checklist

- [ ] Target Agent가 명확한가?
- [ ] Task Type이 명확한가?
- [ ] Primary Domain이 명확한가?
- [ ] Secondary Domain이 필요한가?
- [ ] Master Rules가 필요한가?
- [ ] Target Domain Rules가 포함되었는가?
- [ ] Default RAG Scope가 Agent Role과 일치하는가?
- [ ] Additional RAG Scope가 필요한가?
- [ ] Excluded Scope가 정의되었는가?
- [ ] Scope가 너무 넓지 않은가?
- [ ] Scope가 너무 좁지 않은가?
- [ ] Retrieval Query가 Scope와 일치하는가?
- [ ] Retrieved Context가 Task와 관련 있는가?
- [ ] Context Conflict가 없는가?
```

---

### [FAQ]

Q. RAG Scope Checklist가 뭐야?
A. Agent별 RAG Scope가 현재 Task와 Agent Role에 맞는지 검수하는 기준이다.

Q. RAG Scope Checklist에서 중요한 항목은?
A. Target Agent, Task Type, Domain, Master Rules, Domain Rules, Default Scope, Additional Scope다.

Q. Excluded Scope는 왜 필요해?
A. 관련 없는 Domain 문서가 검색되는 것을 막기 위해 필요하다.

Q. RAG Scope 검수는 누가 해?
A. PM Agent가 Handoff 전 수행하고 Review Agent가 산출물 검토 시 확인할 수 있다.

---

## 8.2 Context Management Checklist

### [개념]

Context Management Checklist는 Agent Input에 포함되는 Context가 적절히 선택, 압축, 우선순위화되었는지 검수하는 기준이다.

Checklist를 적용하면 Context 누락, 과다, 충돌, 오래된 정보 사용을 줄일 수 있다.

---

### [핵심]

- Current User Request가 포함되었는지 확인한다.
- Requirements가 포함되었는지 확인한다.
- Constraints가 포함되었는지 확인한다.
- Decisions가 포함되었는지 확인한다.
- Relevant RAG Context가 포함되었는지 확인한다.
- Tool Result가 필요한 경우 포함되었는지 확인한다.
- 관련 없는 Memory가 제외되었는지 확인한다.
- 오래된 Context가 최신 요청을 덮지 않았는지 확인한다.
- Context Conflict가 해결되었는지 확인한다.
- Open Questions가 보존되었는지 확인한다.

---

### [실무]

Context Management Checklist:

```md
## Context Management Checklist

- [ ] Current User Request가 유지되었는가?
- [ ] Requirements가 유지되었는가?
- [ ] Constraints가 유지되었는가?
- [ ] PM Agent Decisions가 유지되었는가?
- [ ] Shared State의 최신 정보가 반영되었는가?
- [ ] Relevant RAG Context만 포함되었는가?
- [ ] Tool Result Summary가 필요한 경우 포함되었는가?
- [ ] Assumptions가 표시되었는가?
- [ ] Open Questions가 유지되었는가?
- [ ] 관련 없는 Context가 제거되었는가?
- [ ] 오래된 Memory가 최신 요청을 덮지 않았는가?
- [ ] Context Conflict가 해결되었는가?
- [ ] Target Agent가 바로 작업할 수 있는 구조인가?
```

---

### [FAQ]

Q. Context Management Checklist가 뭐야?
A. Agent Input에 포함되는 Context가 적절히 선택, 압축, 우선순위화되었는지 검수하는 기준이다.

Q. Context Management Checklist에서 가장 중요한 항목은?
A. Current User Request, Requirements, Constraints, Decisions, Relevant RAG Context, Open Questions다.

Q. 관련 없는 Memory는 어떻게 처리해?
A. Context Package에서 제외해야 한다.

Q. Context Conflict는 어떻게 처리해?
A. Context Priority 기준으로 결정하고 Conflict Record를 남긴다.

---

# Retrieval Queries

### [FAQ]

Q. RAG Scope가 뭐야?
A. 각 Agent가 검색하고 참조할 수 있는 RAG 문서 범위다.

Q. RAG Scope를 제한하는 이유는?
A. 관련 없는 Context를 줄이고 Retrieval 정확도를 높이기 위해서다.

Q. RAG Scope가 너무 넓으면 어떻게 돼?
A. 관련 없는 문서가 검색되어 Agent Output이 흔들릴 수 있다.

Q. RAG Scope가 너무 좁으면 어떻게 돼?
A. 필요한 문서가 검색되지 않아 Agent가 추측으로 작업할 수 있다.

Q. PM Agent RAG Scope는 뭐야?
A. PM Agent가 요구사항 분석, 작업 분해, Routing, Handoff, 결과 통합을 위해 참조하는 문서 범위다.

Q. PM Agent는 모든 Domain 문서를 검색해야 해?
A. 아니다. 전체 기준 문서를 우선하고 필요한 Domain 문서만 추가로 검색해야 한다.

Q. Specialist Agent RAG Scope는 뭐야?
A. 특정 Domain Agent가 자기 작업을 수행할 때 참조하는 Domain 문서 범위다.

Q. Specialist Agent가 Scope 밖 문서를 검색해도 돼?
A. 기본적으로 하지 않는다. PM Agent가 작업상 필요하다고 지정한 경우에만 추가한다.

Q. Review Agent RAG Scope는 뭐야?
A. 산출물을 검토하기 위해 Master Rules, Domain Rules, Target Output, Shared State, Related Domain RAG를 포함하는 검색 범위다.

Q. Fix Agent RAG Scope는 뭐야?
A. Review Findings를 반영하기 위해 Target Output, Review Report, 수정 대상 Domain RAG를 포함하는 검색 범위다.

Q. Retrieval Query가 뭐야?
A. RAG 시스템에서 필요한 문서를 검색하기 위해 사용하는 질문 또는 검색 문장이다.

Q. 좋은 Retrieval Query 조건은?
A. Domain 용어, Task Type, 필요한 Output, Rule 키워드가 포함되어야 한다.

Q. Query Expansion이 뭐야?
A. 초기 검색 Query에 관련 용어와 FAQ 표현을 추가해 검색 범위를 보강하는 작업이다.

Q. Query Expansion은 언제 사용해?
A. 필요한 문서가 검색되지 않거나 검색 결과가 부족할 때 사용한다.

Q. Query Narrowing이 뭐야?
A. 검색 결과가 너무 넓을 때 Domain, Agent Role, Section 등을 추가해 검색 범위를 좁히는 작업이다.

Q. Query Narrowing은 언제 필요해?
A. 관련 없는 문서가 많이 검색되거나 Context가 너무 넓어질 때 필요하다.

Q. Context Management가 뭐야?
A. Agent가 사용할 User Request, Shared State, RAG Context, Memory, Tool Result를 선택하고 정리하는 작업이다.

Q. 모든 Context를 넣으면 안 되는 이유는?
A. Token 낭비와 지시 혼선이 생기고 관련 없는 정보가 Agent 판단을 흐릴 수 있기 때문이다.

Q. Context Priority가 뭐야?
A. 여러 Context가 존재하거나 충돌할 때 어떤 정보를 우선할지 정하는 기준이다.

Q. 가장 우선하는 Context는?
A. 현재 User Request다.

Q. RAG Context와 PM Decision이 충돌하면?
A. 명시된 PM Agent Decision이 우선이다.

Q. Context Packaging이 뭐야?
A. Agent에게 전달할 Context를 선택, 요약, 구조화해 Agent Input으로 만드는 작업이다.

Q. Context Package에는 뭐가 들어가야 해?
A. Requirements, Constraints, Decisions, RAG Context Summary, Tool Result Summary, Assumptions, Open Questions가 들어가야 한다.

Q. Context Compression이 뭐야?
A. 긴 Context를 요구사항, 결정사항, 위험, 미확정 사항 중심으로 압축하는 작업이다.

Q. Context Compression에서 삭제하면 안 되는 것은?
A. 핵심 요구사항, 제약사항, 결정사항, Open Questions, 위험 요소다.

Q. Retrieval Quality가 뭐야?
A. RAG 검색 결과가 현재 Agent Task에 얼마나 관련 있고 충분하며 정확한지를 나타내는 기준이다.

Q. Retrieval Quality가 낮으면 어떻게 돼?
A. Agent가 관련 없는 문서를 근거로 사용하거나 필요한 문서 없이 추측할 수 있다.

Q. Retrieval Context Conflict가 뭐야?
A. 검색된 RAG Context가 현재 요청, Shared State Decision, Domain Rules와 충돌하는 상태다.

Q. RAG에서 검색된 내용은 항상 맞아?
A. 아니다. 현재 요청, PM Decision, Master Rules, Domain Rules와 충돌하면 후순위다.

Q. RAG Scope Failure는 언제 발생해?
A. Agent가 잘못된 문서 범위를 검색하거나 필요한 문서를 누락하거나 관련 없는 Context를 사용할 때 발생한다.

Q. Scope Too Broad는 뭐야?
A. RAG Scope가 너무 넓어 관련 없는 Domain 문서가 검색되는 상태다.

Q. Scope Too Narrow는 뭐야?
A. RAG Scope가 너무 좁아 필요한 문서가 검색되지 않는 상태다.

Q. Context Management Failure는 언제 발생해?
A. 필요한 Context가 누락되거나 관련 없는 Context가 과도하게 포함되거나 오래된 Context가 최신 요청을 덮을 때 발생한다.

Q. Missing Context는 왜 위험해?
A. Agent가 추측으로 작업해 Hallucination이나 잘못된 Output을 만들 수 있기 때문이다.

Q. Lost Constraint는 어떻게 막아?
A. Context Compression 후 Requirements, Constraints, Decisions, Open Questions가 보존되었는지 확인한다.

Q. RAG Scope Checklist가 뭐야?
A. Agent별 RAG Scope가 현재 Task와 Agent Role에 맞는지 검수하는 기준이다.

Q. Context Management Checklist가 뭐야?
A. Agent Input에 포함되는 Context가 적절히 선택, 압축, 우선순위화되었는지 검수하는 기준이다.

Q. 개인 AI 개발팀에서 RAG Scope는 어디에 쓰여?
A. PM Agent가 Handoff를 만들 때 Agent별 검색 문서 범위를 지정하고 Specialist Agent가 관련 Domain 문서만 검색하는 데 사용한다.

Q. 개인 AI 개발팀에서 Context Management는 어디에 쓰여?
A. User Request, Shared State, RAG Context, Memory, Tool Result를 Agent별 Input으로 정리하는 데 사용한다.
