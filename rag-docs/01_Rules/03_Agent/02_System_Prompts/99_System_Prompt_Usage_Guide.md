# Agent System Prompt Usage Guide v1

## 1. 구성

```text
Agent_System_Prompts_v1
├ 00_Common_System_Prompt.md
├ 01_PM_Agent_System_Prompt.md
├ 02_DB_Agent_System_Prompt.md
├ 03_Backend_Agent_System_Prompt.md
├ 04_Frontend_Agent_System_Prompt.md
├ 05_Review_Agent_System_Prompt.md
├ 99_System_Prompt_Usage_Guide.md
└ README.md
```

---

## 2. 적용 방식

각 Agent의 System Prompt에는 다음 두 문서를 함께 넣는 것을 권장한다.

```text
1. 00_Common_System_Prompt.md
2. 해당 Agent System Prompt
```

예:

```text
PM Agent = Common System Prompt + PM Agent System Prompt
DB Agent = Common System Prompt + DB Agent System Prompt
Backend Agent = Common System Prompt + Backend Agent System Prompt
Frontend Agent = Common System Prompt + Frontend Agent System Prompt
Review Agent = Common System Prompt + Review Agent System Prompt
```

---

## 3. RAG 연결 우선순위

공통 우선순위:

```text
1. Master_RAG_Rules.md
2. Project_Progress.md
3. RAG_Document_Operation_Rules_Addendum.md
4. Agent_Build_Context.md
5. Common Agent Rules
6. 해당 Agent Rules
7. 관련 Domain Rules
8. 사용자 입력
9. 일반 추론
```

---

## 4. Agent별 권장 RAG 연결

PM Agent:

```text
- Master_RAG_Rules.md
- Project_Progress.md
- RAG_Document_Operation_Rules_Addendum.md
- Agent_Build_Context.md
- Common Agent Rules
- PM Agent Rules
- Agent Future Split Roadmap
- Foundation Domain 목록 요약
```

DB Agent:

```text
- Common Agent Rules
- DB Agent Rules
- SQL Domain Rules
- JPA Advanced Domain Rules
- QueryDSL Practical Domain Rules
- API Design Domain Rules
- Design Pattern Domain Rules
- Security Advanced Domain Rules 조건부
- Redis Domain Rules 조건부
- Testing Domain Rules 조건부
```

Backend Agent:

```text
- Common Agent Rules
- Backend Agent Rules
- Java Domain Rules
- Spring Boot Domain Rules
- JPA Advanced Domain Rules
- API Design Domain Rules
- Security Advanced Domain Rules
- QueryDSL Practical Domain Rules
- Testing Domain Rules
- Redis Domain Rules
- Design Pattern Domain Rules
- Docker Domain Rules 조건부
- Git/GitHub Domain Rules 조건부
- SSR Thymeleaf Domain Rules 조건부
```

Frontend Agent:

```text
- Common Agent Rules
- Frontend Agent Rules
- HTML/CSS Domain Rules
- JavaScript Domain Rules
- TypeScript Domain Rules
- React Core Domain Rules
- React Component Design Domain Rules
- React Router Domain Rules
- REST API Integration Domain Rules
- State Management Domain Rules
- Form Validation Domain Rules
- Auth Frontend Flow Domain Rules
- Error/Loading UX Domain Rules
- UI Component Pattern Domain Rules
- Frontend Code Review Domain Rules
- Styling Architecture Domain Rules
- Design System Foundation Domain Rules
```

Review Agent:

```text
- Common Agent Rules
- PM/DB/Backend/Frontend/Review Agent Rules
- SQL Domain Rules
- Java Domain Rules
- Spring Boot Domain Rules
- JPA Advanced Domain Rules
- Security Advanced Domain Rules
- QueryDSL Practical Domain Rules
- Testing Domain Rules
- Redis Domain Rules
- API Design Domain Rules
- Design Pattern Domain Rules
- Frontend Code Review Domain Rules
- Frontend Testing Domain Rules
- Frontend Accessibility Domain Rules
- Frontend Build & Deploy Domain Rules
- Agent Evaluation & Guardrails Domain Rules
- RAG Evaluation & Retrieval Optimization Domain Rules
```

---

## 5. 초기 운영 권장 Workflow

기본은 순차 진행이다.

```text
User Request
↓
PM Agent
↓
필요 시 DB Agent
↓
필요 시 Backend Agent
↓
필요 시 Frontend Agent
↓
Review Agent
↓
Final Answer
```

DB 변경이 없는 경우 DB Agent를 생략할 수 있다.

```text
PM → Backend → Frontend → Review
PM → Frontend → Review
PM → Review
```

---

## 6. Expert Agent 분리 원칙

현재 5개 Agent 구조는 초기 운영용이다.

다음 Agent는 Expert 문서 제작 후 분리한다.

```text
- DevOps Agent
- Test Agent
- Security Agent
- Docs Agent
- AI Agent
- RAG Update Agent
- Performance Agent
- Design System Agent
```

분리 시에는 기존 Agent System Prompt의 Secondary Responsibility / Future Split 섹션을 새 Agent Prompt로 이동하면 된다.

---

## 7. 주의사항

- System Prompt는 실제 Agent에 넣는 운영 지시문이다.
- Agent Rules는 상세 기준 문서로 RAG에 넣어 참조시키는 것이 좋다.
- System Prompt가 너무 길어지면 Common Prompt는 공통 설정으로 두고, 각 Agent Prompt만 개별 적용한다.
- RAG 문서 자동 수정은 금지한다.
- RAG Update Candidate는 사용자 승인 전까지 제안 상태로만 유지한다.
