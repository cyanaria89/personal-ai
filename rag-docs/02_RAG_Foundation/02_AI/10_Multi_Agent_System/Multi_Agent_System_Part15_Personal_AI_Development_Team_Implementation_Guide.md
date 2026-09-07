# Multi-Agent System Part15 - Personal AI Development Team Implementation Guide

---

# 1. Personal AI Development Team Core

## 1.1 Personal AI Development Team Definition

### [개념]

Personal AI Development Team은 개인 AI 서버를 단순 RAG 챗봇이 아니라 PM Agent 중심의 개발 보조 Multi-Agent System으로 운영하는 구조이다.

사용자는 여러 Agent에게 직접 요청하지 않고 PM Agent에게만 요청한다. PM Agent는 사용자 요청을 분석하고 필요한 Agent를 선택하며, Handoff와 Review-Fix를 거쳐 최종 결과를 통합한다.

Personal AI Development Team의 목적은 개인 개발자가 혼자 처리하는 분석, 설계, 검토, 수정, 문서화 작업을 역할별 Agent에게 분배하여 안정적인 결과를 얻는 것이다.

기본 구조:

```text
User
→ PM Agent
→ Specialist Agent
→ Review Agent
→ Fix Agent
→ PM Agent
→ Final Output
```

기능 개발 중심 구조:

```text
User
→ PM Agent
→ SQL Agent
→ Backend Agent
→ Frontend Agent
→ Review Agent
→ Fix Agent
→ Final Output
```

---

### [핵심]

- 사용자는 PM Agent에게만 요청한다.
- PM Agent는 전체 작업을 조율한다.
- Specialist Agent는 자기 Domain 작업만 수행한다.
- SQL Agent는 DB와 Query를 담당한다.
- Backend Agent는 Java, Spring Boot, JPA, API를 담당한다.
- Frontend Agent는 React, UI, API 연동을 담당한다.
- DevOps Agent는 Docker, Linux, 배포, 운영 계획을 담당한다.
- AI Agent는 RAG, Prompt, Agent Workflow를 담당한다.
- Documentation Agent는 RAG 문서 작성과 정리를 담당한다.
- Review Agent는 산출물을 검토한다.
- Fix Agent는 Review Findings를 반영한다.
- 최종 결과는 PM Agent가 통합한다.

---

### [실무]

개인 AI 개발팀 1차 목표:

```text
단순 RAG 챗봇
→ PM Agent 중심 구조
→ Specialist Agent 분리
→ Review-Fix Loop 적용
→ 개인 개발팀 Workflow 구성
```

개인 AI 개발팀 운영 원칙:

```text
User는 PM Agent에게만 요청
PM Agent는 직접 구현보다 조율
Specialist Agent는 Domain 작업 수행
Review Agent는 품질 검수
Fix Agent는 수정 반영
PM Agent는 최종 결과 통합
```

개인 AI 개발팀이 처리할 작업:

```text
RAG 문서 제작
RAG 문서 검수
SQL Schema 설계
Backend API 설계
Frontend Component 설계
코드 리뷰
테스트 전략 설계
배포 계획 수립
Agent Workflow 설계
프로젝트 구조 분석
학습 자료 정리
기술 의사결정 보조
```

---

### [FAQ]

Q. Personal AI Development Team이 뭐야?
A. 개인 AI 서버를 PM Agent 중심의 Multi-Agent System으로 운영해 SQL, Backend, Frontend, Review, Fix 작업을 역할별로 처리하는 구조다.

Q. 사용자가 모든 Agent에게 직접 요청해야 해?
A. 아니다. 사용자는 PM Agent에게만 요청하고 PM Agent가 필요한 Agent에게 작업을 분배한다.

Q. 개인 AI 개발팀의 핵심 Agent는?
A. PM Agent, Specialist Agent, Review Agent, Fix Agent다.

Q. 개인 AI 개발팀의 장점은?
A. 역할 분리, RAG Scope 제한, Review-Fix 품질 개선, 최종 결과 통합이 가능하다는 점이다.

---

# 2. Initial Implementation Scope

## 2.1 Minimum Viable Agent Set

### [개념]

Minimum Viable Agent Set은 개인 AI 개발팀을 처음 구축할 때 필요한 최소 Agent 구성이다.

처음부터 많은 Agent를 만들면 Handoff, Shared State, RAG Scope, Tool Permission 관리가 복잡해진다. 초기에는 PM Agent, Documentation Agent, Review Agent, Fix Agent를 중심으로 시작하고, 기능 개발이 필요할 때 SQL Agent, Backend Agent, Frontend Agent를 추가하는 것이 안정적이다.

기본 초기 구성:

```text
PM Agent
Documentation Agent
Review Agent
Fix Agent
```

기능 개발 최소 구성:

```text
PM Agent
SQL Agent
Backend Agent
Frontend Agent
Review Agent
Fix Agent
```

---

### [핵심]

- 초기에는 Agent 수를 과도하게 늘리지 않는다.
- PM Agent는 필수이다.
- Review Agent는 초기부터 포함하는 것이 좋다.
- Fix Agent는 Review-Fix Loop에 필요하다.
- Documentation Agent는 RAG 문서 제작에 유용하다.
- Backend Agent는 개인 개발 보조의 핵심이다.
- SQL Agent와 Frontend Agent는 기능 개발 시 추가한다.
- DevOps Agent와 AI Agent는 안정화 후 추가한다.
- Router Agent와 Planner Agent는 초기에는 PM Agent 내부 기능으로 운영한다.
- Executor Agent는 Tool 자동화가 필요해진 뒤 분리한다.

---

### [실무]

추천 Agent 추가 순서:

```text
Step 1
PM Agent

Step 2
Documentation Agent
Review Agent
Fix Agent

Step 3
SQL Agent
Backend Agent

Step 4
Frontend Agent

Step 5
DevOps Agent
AI Agent

Step 6
Router Agent
Planner Agent
Executor Agent
```

초기 Agent 구성 예시:

```json
{
  "initialAgents": [
    {
      "name": "PM Agent",
      "role": "Requirement analysis, routing, handoff, state management, final integration"
    },
    {
      "name": "Documentation Agent",
      "role": "RAG document creation"
    },
    {
      "name": "Review Agent",
      "role": "Output review and quality gate"
    },
    {
      "name": "Fix Agent",
      "role": "Apply review findings within scope"
    }
  ],
  "nextAgents": ["SQL Agent", "Backend Agent", "Frontend Agent"]
}
```

초기 적용 예시:

```text
RAG 문서 제작 요청
→ PM Agent
→ Documentation Agent
→ Review Agent
→ Fix Agent
→ Final Document
```

---

### [FAQ]

Q. 처음부터 모든 Agent를 만들어야 해?
A. 아니다. PM Agent, Documentation Agent, Review Agent, Fix Agent부터 시작하는 것이 안정적이다.

Q. Backend Agent와 SQL Agent는 언제 추가해?
A. RAG 문서 제작 Workflow가 안정화된 뒤 실제 기능 개발 보조를 시작할 때 추가한다.

Q. Router Agent는 처음부터 필요해?
A. 아니다. 초기에는 PM Agent가 Routing을 겸하고 Agent 수가 늘면 Router Agent 분리를 검토한다.

Q. Review Agent는 왜 초기부터 필요해?
A. Agent Output 품질을 검수하고 RAG 문서 구조 위반, 요구사항 누락, Handoff 문제를 줄이기 위해 필요하다.

---

## 2.2 Local AI Server Baseline

### [개념]

Local AI Server Baseline은 개인 AI 개발팀을 운영하기 위한 기본 실행 환경이다.

개인 AI 개발팀은 LLM, Embedding Model, RAG 플랫폼, 문서 저장 구조, Agent Prompt, Workflow 규칙이 필요하다.

현재 기준 예시:

```text
Ubuntu
→ Ollama
→ Qwen2.5 14B
→ BGE-M3
→ AnythingLLM
→ Markdown RAG Documents
→ Agent Workflow
```

---

### [핵심]

- Ubuntu 기반 서버에서 운영할 수 있다.
- Ollama를 LLM 실행 환경으로 사용할 수 있다.
- Qwen2.5 14B를 Text LLM으로 사용할 수 있다.
- BGE-M3를 Embedding Model로 사용할 수 있다.
- AnythingLLM을 RAG 플랫폼으로 사용할 수 있다.
- RAG 문서는 Markdown 중심으로 관리한다.
- 초기 Agent Workflow는 순차 실행 방식이 안정적이다.
- 모델 성능보다 RAG 문서 품질과 Handoff 품질이 중요하다.
- 자동화보다 검증 가능한 운영 구조가 먼저이다.

---

### [실무]

권장 Baseline:

```json
{
  "os": "Ubuntu",
  "llmRuntime": "Ollama",
  "textModel": "Qwen2.5 14B",
  "embeddingModel": "BGE-M3",
  "ragPlatform": "AnythingLLM",
  "documentFormat": "Markdown",
  "initialWorkflow": "PM-centered sequential workflow",
  "initialToolPolicy": "read-first, approval-required for dangerous tools"
}
```

초기 실행 전략:

```text
1. RAG 문서 구조 정리
2. Master Rules / Domain Rules 업로드
3. PM Agent Prompt 구성
4. Documentation Agent Prompt 구성
5. Review Agent Prompt 구성
6. Fix Agent Prompt 구성
7. RAG 문서 제작 Workflow 테스트
8. Backend / SQL Agent 추가
```

운영 주의:

```text
처음부터 완전 자동 Multi-Agent를 목표로 하지 않는다.
먼저 PM 중심 Handoff 구조를 안정화한다.
Agent별 System Prompt와 RAG Scope를 분리한다.
Review-Fix 품질이 안정된 후 Tool Permission을 확장한다.
Dangerous Tool은 Human Approval 대상으로 유지한다.
```

---

### [FAQ]

Q. 개인 AI 개발팀을 운영하려면 어떤 서버 구성이 필요해?
A. Ubuntu, Ollama, Text LLM, Embedding Model, RAG 플랫폼, Markdown 문서 구조가 필요하다.

Q. AnythingLLM을 사용할 수 있어?
A. 가능하다. 초기 개인 RAG 기반 Agent 운영에 사용할 수 있다.

Q. Qwen2.5 14B와 BGE-M3 조합은 어떤 역할이야?
A. Qwen2.5 14B는 Text LLM, BGE-M3는 Embedding Model 역할이다.

Q. 처음부터 완전 자동 Agent Workflow를 만들어야 해?
A. 아니다. 처음에는 PM 중심 수동 또는 반자동 Workflow로 시작하고 점진적으로 확장하는 것이 좋다.

---

# 3. Agent Definition Implementation

## 3.1 PM Agent Implementation

### [개념]

PM Agent Implementation은 개인 AI 개발팀의 단일 진입점이 되는 Agent를 정의하는 작업이다.

PM Agent는 요구사항 분석, 작업 분해, Agent Routing, Handoff 생성, Shared State 관리, 결과 통합을 담당한다.

PM Agent는 Specialist Agent를 대체하지 않고 조율자 역할을 수행해야 한다.

---

### [핵심]

- PM Agent는 사용자 요청의 단일 진입점이다.
- PM Agent는 요구사항을 분석한다.
- PM Agent는 작업을 분해한다.
- PM Agent는 Target Agent를 선택한다.
- PM Agent는 Handoff를 생성한다.
- PM Agent는 Shared State를 관리한다.
- PM Agent는 Agent 결과를 통합한다.
- PM Agent는 Review-Fix Loop를 조율한다.
- PM Agent는 위험 작업을 승인 요청으로 전환한다.
- PM Agent는 상세 구현을 과도하게 직접 수행하지 않는다.

---

### [실무]

PM Agent Definition Template:

```md
# PM Agent Definition

## Role

You are the PM Agent for a personal AI development team.

## Responsibilities

- Analyze user request
- Extract requirements and constraints
- Decompose task into agent-level tasks
- Select target agents
- Generate structured handoff
- Manage shared state
- Integrate agent outputs
- Request review when needed
- Request human approval for risky actions
- Produce final output for user

## Forbidden Scope

- Do not directly perform detailed implementation when Specialist Agent is required
- Do not execute dangerous tools
- Do not ignore Review Findings
- Do not hide Open Questions
- Do not overwrite current user request with old memory

## Output Requirements

- Structured plan when needed
- Handoff for Specialist Agent
- Final integrated result
- Risks and Open Questions if unresolved
```

PM Agent Handoff Template:

```json
{
  "from": "PM Agent",
  "to": "Target Agent",
  "task": "<specific task>",
  "requirements": [],
  "constraints": [],
  "ragScope": [],
  "toolPermission": [],
  "expectedOutput": [],
  "doneCriteria": [],
  "assumptions": [],
  "openQuestions": []
}
```

PM Agent Quality Gate:

```md
## PM Agent Quality Gate

- [ ] Current User Request를 반영했는가?
- [ ] Requirements와 Constraints를 분리했는가?
- [ ] Target Agent가 적절한가?
- [ ] Handoff가 충분한가?
- [ ] RAG Scope가 지정되었는가?
- [ ] Tool Permission이 확인되었는가?
- [ ] Review 필요 여부를 판단했는가?
- [ ] Final Output 형식을 확인했는가?
```

---

### [FAQ]

Q. PM Agent는 무엇을 구현해야 해?
A. 요구사항 분석, 작업 분해, Routing, Handoff, Shared State, 결과 통합을 구현해야 한다.

Q. PM Agent가 직접 코드나 문서를 작성해도 돼?
A. 간단한 작업은 가능하지만, 전문 Domain 작업은 Specialist Agent에게 위임하는 것이 원칙이다.

Q. PM Agent의 가장 중요한 Output은?
A. 구조화된 Handoff와 최종 통합 결과다.

Q. PM Agent의 실패를 줄이려면?
A. Role Boundary, Handoff Template, Shared State, Workflow Pattern Selection 기준을 명확히 해야 한다.

---

## 3.2 Specialist Agent Implementation

### [개념]

Specialist Agent Implementation은 각 Domain별 Agent의 역할, 입력, 출력, RAG Scope, Tool Permission을 정의하는 작업이다.

Specialist Agent는 자기 Domain 작업만 수행하고, Scope 밖 작업은 PM Agent에게 반환해야 한다.

---

### [핵심]

- Specialist Agent는 Domain별 전문가 역할이다.
- Agent별 Role을 명확히 한다.
- Agent별 Scope를 명확히 한다.
- Agent별 Forbidden Scope를 정의한다.
- Agent별 RAG Scope를 지정한다.
- Agent별 Tool Permission을 지정한다.
- Agent별 Expected Output을 구조화한다.
- Assumptions와 Open Questions를 표시한다.
- Scope 밖 작업은 PM Agent에게 반환한다.
- 다음 Agent가 사용할 수 있는 Output을 만든다.

---

### [실무]

Backend Agent Definition Template:

```md
# Backend Agent Definition

## Role

You are the Backend Agent for Java, Spring Boot, JPA, Security, and API Design.

## Responsibilities

- Design API Contract
- Design DTO
- Design Service method flow
- Define validation
- Define exception cases
- Define security and authorization rules
- Identify transaction boundaries
- Identify backend risks

## RAG Scope

- Java Domain Rules
- Spring Boot Domain Rules
- JPA Advanced Domain Rules
- Security Advanced Domain Rules
- API Design Domain Rules
- Testing Domain Rules when needed

## Tool Permission

- Allowed: RAG Search, File Read, Code Search
- Approval Required: Code Modify, Config Write
- Forbidden: Production Deploy, DB Migration without approval

## Forbidden Scope

- Do not define React component structure
- Do not execute deployment
- Do not modify DB schema without SQL Agent / PM decision
- Do not ignore Security constraints

## Expected Output

- API Contract
- DTO Design
- Service Method Plan
- Validation Rules
- Exception Cases
- Security Rules
- Risks
- Open Questions
```

SQL Agent Definition 요약:

```md
# SQL Agent Definition

## Role

DB Schema, Query, Index, Constraint specialist

## Expected Output

- Table Design
- PK / FK
- Constraints
- Index Candidates
- Query Examples
- Data Consistency Risks
```

Frontend Agent Definition 요약:

```md
# Frontend Agent Definition

## Role

React UI, Component, State, API Integration specialist

## Expected Output

- Component Structure
- State Design
- API Call Flow
- Loading / Error / Empty State
- Form Validation
- UI Risks
```

---

### [FAQ]

Q. Specialist Agent는 무엇을 구현해야 해?
A. 자기 Domain의 설계, 분석, 검토, 출력 구조를 담당해야 한다.

Q. Specialist Agent가 Scope 밖 작업을 받으면?
A. PM Agent에게 Scope 밖이라고 반환하거나 필요한 Target Agent를 제안해야 한다.

Q. Backend Agent의 기본 RAG Scope는?
A. Java, Spring Boot, JPA, Security, API Design이다.

Q. Specialist Agent Output에는 무엇이 있어야 해?
A. Domain Output, Decisions, Assumptions, Risks, Open Questions가 있어야 한다.

---

## 3.3 Review and Fix Agent Implementation

### [개념]

Review Agent와 Fix Agent는 개인 AI 개발팀의 품질 관리 핵심이다.

Review Agent는 산출물을 검토하고 Review Findings를 작성한다. Fix Agent는 Review Findings를 반영해 산출물을 수정한다.

Review와 Fix를 분리하면 역할 경계가 명확해지고, 수정 추적과 Regression 관리가 쉬워진다.

---

### [핵심]

- Review Agent는 검토 담당이다.
- Review Agent는 직접 수정하지 않는다.
- Review Agent는 Severity, Evidence, Impact, Fix Direction을 작성한다.
- Fix Agent는 Review Findings를 반영한다.
- Fix Agent는 Fix Scope를 지킨다.
- Fix Agent는 기존 요구사항을 보존한다.
- Fix Agent는 Change Summary를 작성한다.
- Fix Agent는 Regression Risk를 표시한다.
- Review-Fix Loop에는 Max Iteration이 필요하다.
- Minor Issue만 남으면 Pass with Notes로 종료할 수 있다.

---

### [실무]

Review Agent Definition Template:

```md
# Review Agent Definition

## Role

You are the Review Agent for quality control.

## Responsibilities

- Review output against user request
- Review output against PM handoff
- Review output against Master Rules and Domain Rules
- Identify missing requirements
- Identify scope violations
- Identify consistency issues
- Identify risk and regression
- Produce Review Findings

## Forbidden Scope

- Do not directly fix output
- Do not create new requirements
- Do not change review criteria during loop
- Do not mark preference as defect without criteria

## Expected Output

- Review Summary
- Findings by Severity
- Evidence
- Impact
- Fix Direction
- Pass / Fail Decision
```

Fix Agent Definition Template:

```md
# Fix Agent Definition

## Role

You are the Fix Agent for applying Review Findings.

## Responsibilities

- Analyze Review Findings
- Define Fix Scope
- Apply minimal required changes
- Preserve original requirements
- Preserve PM decisions
- Produce Updated Output
- Produce Change Summary
- Identify Regression Risk
- Request Re-review when needed

## Forbidden Scope

- Do not create new requirements
- Do not over-fix
- Do not delete existing requirements
- Do not change API contract without PM decision
- Do not execute dangerous tools without approval

## Expected Output

- Applied Fix
- Updated Output
- Preserved Requirements
- Change Summary
- Regression Risk
- Re-review Required
```

Review-Fix 설정:

```json
{
  "maxIteration": 2,
  "criticalPolicy": "must_fix",
  "majorPolicy": "fix_or_pm_decision",
  "minorPolicy": "pass_with_notes",
  "stopCondition": [
    "critical_0",
    "major_resolved_or_decided",
    "minor_only",
    "max_iteration_reached"
  ]
}
```

---

### [FAQ]

Q. Review Agent와 Fix Agent를 왜 분리해?
A. 검토와 수정을 분리해야 책임 경계, 수정 추적, Regression 관리가 쉬워진다.

Q. Review Agent는 직접 수정해도 돼?
A. 원칙적으로 안 된다. Review Agent는 Finding을 작성하고 Fix Agent가 수정한다.

Q. Fix Agent의 핵심 원칙은?
A. Review Findings 범위 안에서 최소 수정하고 기존 요구사항을 보존하는 것이다.

Q. Review-Fix Loop는 몇 번 반복해?
A. 기본 Max Iteration 2회를 권장하고, Critical 0개와 Major 해결 상태를 종료 기준으로 삼는다.

---

# 4. RAG Document Implementation

## 4.1 RAG Document Set Implementation

### [개념]

RAG Document Set Implementation은 개인 AI 개발팀이 사용할 Markdown 기반 RAG 문서 세트를 구성하는 작업이다.

RAG 문서는 Agent가 검색하고 사용할 수 있는 구조여야 하며, 사람용 장문 설명보다 Retrieval 최적화와 FAQ 검색 매칭을 우선한다.

기본 구조:

```text
Master Rules
→ Domain Rules
→ Part Documents
→ Retrieval Queries
→ Agent RAG Scope
```

---

### [핵심]

- RAG 문서는 Markdown으로 관리한다.
- Master Rules는 전체 문서 제작 기준이다.
- Domain Rules는 Domain별 문서 기준이다.
- Project Progress는 진행 상태와 중복 방지 기준이다.
- Part Documents는 세부 주제별 문서이다.
- 각 문서는 Required Section을 포함한다.
- `[개념]`, `[핵심]`, `[실무]`, `[FAQ]` 구조를 사용한다.
- 문서 마지막에 Retrieval Queries를 포함한다.
- FAQ는 실제 사용자 질문 표현을 포함한다.
- 파일명과 제목은 검색 가능하게 작성한다.
- Agent별 RAG Scope와 연결한다.

---

### [실무]

권장 RAG 문서 구조:

```text
RAG Doc
├ Rules
│ ├ Master
│ │ ├ Master RAG Rules.md
│ │ ├ Project Progress.md
│ │ └ RAG Document Operation Rules Addendum.md
│ ├ Domain
│ │ ├ Backend
│ │ ├ Frontend
│ │ ├ AI
│ │ ├ DevOps
│ │ └ Multi Agent System
│ └ Agent
│   ├ PM Agent Rules.md
│   ├ Review Agent Rules.md
│   └ Fix Agent Rules.md
├ SQL
├ Java
├ Spring Boot
├ JPA
├ Security
├ React
├ Docker
└ Multi Agent System
```

RAG 문서 파일명 규칙:

```text
<Domain>_Part<Number>_<Topic>.md

예:
Multi_Agent_System_Part15_Personal_AI_Development_Team_Implementation_Guide.md
Spring_Boot_Part03_Controller_Service_API.md
JPA_Advanced_Part04_Relationship_Mapping.md
```

RAG 문서 기본 Template:

```md
# FileName

# Document Title

---

# 1. Main Section

## 1.1 Sub Section

### [개념]

...

---

### [핵심]

- ...

---

### [실무]

...

---

### [FAQ]

Q. ...
A. ...

---

# Retrieval Queries

### [FAQ]

Q. ...
A. ...
```

---

### [FAQ]

Q. RAG Document Set Implementation이 뭐야?
A. 개인 AI 개발팀이 사용할 Markdown 기반 RAG 문서 세트를 구성하는 작업이다.

Q. RAG 문서는 사람용 설명 위주로 만들면 돼?
A. 아니다. Agent Retrieval을 위해 구조화, FAQ, Retrieval Queries를 우선해야 한다.

Q. RAG 문서에 Retrieval Queries가 필요한 이유는?
A. 사용자 질문 표현과 문서 Chunk 매칭을 강화하기 위해 필요하다.

Q. RAG 문서 파일명은 어떻게 정해?
A. Domain, Part Number, Topic이 드러나도록 작성한다.

---

## 4.2 Agent RAG Scope Mapping

### [개념]

Agent RAG Scope Mapping은 각 Agent가 어떤 RAG 문서 범위를 검색할지 연결하는 작업이다.

Agent별 RAG Scope가 명확하지 않으면 관련 없는 문서가 검색되거나 필요한 Domain Rules가 누락된다.

기본 구조:

```text
Agent
→ Default RAG Scope
→ Conditional RAG Scope
→ Excluded Scope
```

---

### [핵심]

- Agent별 Default RAG Scope를 지정한다.
- Task별 Conditional RAG Scope를 추가한다.
- 관련 없는 Excluded Scope를 지정할 수 있다.
- PM Agent는 Master Rules와 Project Progress를 우선 검색한다.
- Specialist Agent는 자기 Domain 문서를 우선 검색한다.
- Review Agent는 Master Rules와 Target Domain Rules를 우선 검색한다.
- Fix Agent는 Review Findings 관련 문서를 검색한다.
- RAG Scope 변경은 PM Agent가 결정한다.
- RAG Scope는 Tool Permission과 함께 관리한다.

---

### [실무]

Agent RAG Scope Mapping 예시:

```json
{
  "PM Agent": {
    "default": [
      "Master RAG Rules",
      "Project Progress",
      "Multi-Agent System Domain Rules",
      "Agent Role Design"
    ],
    "conditional": ["Target Domain Rules"],
    "excluded": ["Unrelated Project Notes"]
  },
  "Backend Agent": {
    "default": [
      "Java Domain Rules",
      "Spring Boot Domain Rules",
      "JPA Advanced Domain Rules",
      "API Design Domain Rules"
    ],
    "conditional": [
      "Security Advanced Domain Rules",
      "Testing Domain Rules",
      "QueryDSL Domain Rules"
    ],
    "excluded": ["React UI Design", "Docker Deployment"]
  },
  "Review Agent": {
    "default": [
      "Master RAG Rules",
      "Target Domain Rules",
      "Review Agent Rules"
    ],
    "conditional": ["Related Specialist Output", "Project Progress"],
    "excluded": ["Unrelated Past Conversation"]
  }
}
```

RAG Scope 적용 Flow:

```text
User Request
→ PM Agent Domain Detection
→ Target Agent 선택
→ Default Scope 로드
→ Conditional Scope 추가
→ Excluded Scope 제거
→ Retrieval Query 생성
```

---

### [FAQ]

Q. Agent RAG Scope Mapping이 뭐야?
A. 각 Agent가 어떤 RAG 문서 범위를 검색할지 연결하는 작업이다.

Q. Agent별 RAG Scope가 필요한 이유는?
A. 관련 없는 문서 검색을 줄이고 필요한 Domain Rules를 누락하지 않기 위해서다.

Q. Backend Agent의 기본 RAG Scope는?
A. Java, Spring Boot, JPA Advanced, API Design이며 작업에 따라 Security와 Testing을 추가한다.

Q. Review Agent의 기본 RAG Scope는?
A. Master Rules, Target Domain Rules, Review Agent Rules, Target Output이다.

---

# 5. Workflow Implementation

## 5.1 Initial Workflow Implementation

### [개념]

Initial Workflow Implementation은 개인 AI 개발팀을 처음 운영할 때 사용할 최소 Workflow를 구현하는 단계이다.

초기에는 완전 자동화보다 PM Agent 중심의 명확한 수동 또는 반자동 Workflow가 안정적이다.

기본 초기 Workflow:

```text
User Request
→ PM Agent
→ Target Agent
→ Review Agent
→ Fix Agent
→ Final Output
```

RAG 문서 제작 초기 Workflow:

```text
User Request
→ PM Agent
→ Documentation Agent
→ Review Agent
→ Fix Agent
→ Final Writing Block
```

---

### [핵심]

- 초기에는 단순 Workflow로 시작한다.
- PM Agent를 중심으로 운영한다.
- Agent 수를 제한한다.
- Handoff Template을 먼저 안정화한다.
- Shared State는 간단한 구조로 시작한다.
- Review-Fix Loop를 기본 적용한다.
- Tool Permission은 읽기 중심으로 시작한다.
- 위험 Tool은 처음부터 승인 대상으로 분리한다.
- 자동 실행보다 품질 안정화가 우선이다.

---

### [실무]

초기 Workflow 단계:

```text
1. User Request 수신
2. PM Agent가 요구사항 분석
3. PM Agent가 Target Agent 선택
4. PM Agent가 Handoff 작성
5. Target Agent가 Output 작성
6. Review Agent가 검토
7. Fix Agent가 필요 시 수정
8. PM Agent가 Final Output 통합
```

초기 Shared State 최소 구조:

```json
{
  "currentUserRequest": "",
  "workflowPattern": "",
  "targetAgent": "",
  "requirements": [],
  "constraints": [],
  "decisions": [],
  "agentOutputs": {},
  "reviewFindings": [],
  "fixResults": [],
  "openQuestions": [],
  "status": "initialized"
}
```

초기 Quality Gate:

```md
## Initial Quality Gate

- [ ] Current User Request 반영
- [ ] Requirements 정리
- [ ] Constraints 정리
- [ ] Target Agent 적절성 확인
- [ ] Handoff 작성
- [ ] Review 수행
- [ ] Critical Issue 0개
- [ ] Final Output Format 준수
```

---

### [FAQ]

Q. 초기 Workflow는 어떻게 시작해?
A. User → PM Agent → Target Agent → Review Agent → Fix Agent → Final Output 구조로 시작한다.

Q. 처음부터 자동화해야 해?
A. 아니다. 처음에는 수동 또는 반자동 Handoff로 품질을 안정화하는 것이 좋다.

Q. 초기 Shared State는 복잡해야 해?
A. 아니다. currentUserRequest, requirements, constraints, decisions, outputs, reviewFindings 정도로 시작하면 된다.

Q. 초기 Tool Permission은 어떻게 설정해?
A. 읽기 중심으로 제한하고 쓰기와 위험 Tool은 승인 대상으로 분리한다.

---

## 5.2 Feature Development Workflow Implementation

### [개념]

Feature Development Workflow Implementation은 개인 AI 개발팀이 실제 웹 기능 개발을 보조하기 위한 Workflow를 구현하는 단계이다.

기능 개발은 DB, Backend, Frontend 의존성이 있으므로 PM Agent가 Sequential Workflow를 선택하고 각 Specialist Agent에게 작업을 전달한다.

---

### [핵심]

- 기능 개발은 Sequential Workflow가 적합하다.
- SQL Agent가 DB 구조를 먼저 설계한다.
- Backend Agent가 API Contract를 설계한다.
- Frontend Agent가 API 연동과 UI 구조를 설계한다.
- Review Agent가 Cross-Domain Consistency를 검토한다.
- Fix Agent가 Review Findings를 반영한다.
- Shared State에 각 Agent Output을 기록한다.
- API Contract와 DTO Field는 Frontend Agent의 핵심 Input이다.
- 미확정 정책은 Open Questions로 분리한다.

---

### [실무]

기능 개발 Workflow Template:

```md
## Feature Development Workflow

### Step 1. PM Agent

- Requirement Analysis
- Domain Detection
- Workflow Pattern Selection
- Task Decomposition

### Step 2. SQL Agent

- Table Design
- PK / FK
- Constraints
- Index Candidates
- Data Consistency Risks

### Step 3. Backend Agent

- API Contract
- DTO Design
- Service Method Plan
- Validation
- Exception Cases
- Security Rules

### Step 4. Frontend Agent

- Component Structure
- State Design
- API Call Flow
- Loading / Error / Empty State
- Form Validation

### Step 5. Review Agent

- SQL / Backend / Frontend Consistency
- Requirement Coverage
- Security Risk
- API Contract Consistency

### Step 6. Fix Agent

- Apply Review Findings
- Preserve Requirements
- Regression Risk

### Step 7. PM Agent

- Final Integration
```

기능 개발 Output 기준:

```json
{
  "finalOutput": {
    "requirements": [],
    "dbDesign": {},
    "apiContract": {},
    "frontendDesign": {},
    "crossDomainConsistency": [],
    "risks": [],
    "openQuestions": [],
    "implementationOrder": []
  }
}
```

---

### [FAQ]

Q. 기능 개발 Workflow는 어떤 구조가 좋아?
A. PM Agent → SQL Agent → Backend Agent → Frontend Agent → Review Agent → Fix Agent 구조가 적합하다.

Q. 왜 SQL Agent가 먼저야?
A. DB Schema와 관계가 Backend Entity, Repository, API 설계의 기반이 되기 때문이다.

Q. 왜 Backend Agent가 Frontend Agent보다 먼저야?
A. Frontend는 API Contract와 DTO Field를 기준으로 State와 API 연동을 설계해야 하기 때문이다.

Q. 기능 개발 Workflow에서 Review Agent는 무엇을 봐?
A. DB, API, UI 간 일관성, 요구사항 충족, 보안, 예외, 위험 요소를 검토한다.

---

# 6. Prompt and Output Implementation

## 6.1 Agent System Prompt Structure

### [개념]

Agent System Prompt Structure는 각 Agent의 역할, 책임, 금지 범위, RAG Scope, Tool Permission, Output Format을 정의하는 Prompt 구조이다.

Agent 품질은 System Prompt의 명확성에 크게 좌우된다.

기본 구조:

```text
Role
→ Responsibilities
→ Forbidden Scope
→ RAG Scope
→ Tool Permission
→ Input Handling
→ Output Format
→ Quality Criteria
→ Failure Handling
```

---

### [핵심]

- Agent System Prompt에는 Role이 명확해야 한다.
- Responsibilities를 명확히 작성한다.
- Forbidden Scope를 작성한다.
- RAG Scope를 지정한다.
- Tool Permission을 지정한다.
- Output Format을 구조화한다.
- Quality Criteria를 포함한다.
- Failure Handling 기준을 포함한다.
- Assumption과 Open Question 처리 기준을 포함한다.
- 현재 User Request를 최우선으로 둔다.

---

### [실무]

Agent System Prompt Template:

```md
# Agent System Prompt

## Role

You are <Agent Name>.

## Responsibilities

- <Responsibility 1>
- <Responsibility 2>

## Forbidden Scope

- Do not <forbidden action>
- Do not perform tasks outside your domain

## RAG Scope

- <Default RAG Scope>
- <Conditional RAG Scope>

## Tool Permission

- Allowed: <tools>
- Approval Required: <tools>
- Forbidden: <tools>

## Input Handling

- Use current user request first
- Use PM Agent Handoff as task source
- Use Shared State Decisions as workflow criteria
- Mark missing context as Open Question or Blocked

## Output Format

- Status
- Result
- Decisions
- Assumptions
- Risks
- Open Questions
- Next Step

## Quality Criteria

- Requirement coverage
- Scope compliance
- Constraint compliance
- Structured output
- Review-ready result

## Failure Handling

- If required context is missing, return Blocked
- If task is outside scope, return to PM Agent
- If dangerous tool is needed, request Human Approval
```

Prompt 작성 기준:

```text
짧고 명확한 Role
구체적인 Responsibility
명시적인 Forbidden Scope
검색 범위 제한
출력 구조 고정
실패 상태 처리 포함
```

---

### [FAQ]

Q. Agent System Prompt에는 무엇이 들어가야 해?
A. Role, Responsibilities, Forbidden Scope, RAG Scope, Tool Permission, Output Format, Quality Criteria, Failure Handling이 들어가야 한다.

Q. Forbidden Scope가 왜 필요해?
A. Agent가 자기 역할 밖 작업을 수행하는 Role Overlap을 막기 위해 필요하다.

Q. Output Format을 고정해야 해?
A. 고정하는 것이 좋다. PM Agent와 Review Agent가 결과를 안정적으로 처리할 수 있기 때문이다.

Q. Missing Context는 어떻게 처리하도록 Prompt에 넣어야 해?
A. 추측하지 말고 Assumption, Open Question, Partial, Blocked로 표시하도록 해야 한다.

---

## 6.2 Final Output Policy

### [개념]

Final Output Policy는 PM Agent가 사용자에게 최종 결과를 전달할 때 따르는 출력 규칙이다.

Final Output은 Agent 내부 작업 과정 전체를 노출하는 것이 아니라, 사용자 요청에 맞는 최종 산출물을 제공해야 한다.

기본 구조:

```text
Agent Outputs
→ PM Agent Integration
→ User Output Format Check
→ Final Output
```

---

### [핵심]

- Final Output은 사용자 요청 형식을 따른다.
- 사용자가 결과만 요청하면 결과만 제공한다.
- 내부 Agent 과정은 필요할 때만 요약한다.
- 미해결 Open Question은 숨기지 않는다.
- 위험 사항은 명확히 표시한다.
- RAG 문서 제작에서는 writing block 형식을 지킨다.
- 코드 / 문서 / 설계 결과는 재사용 가능한 형태로 제공한다.
- Review Findings가 남아 있으면 상태를 표시한다.
- Final Output은 PM Agent가 통합한다.

---

### [실무]

Final Output Policy 예시:

| 요청 유형     | Final Output                            |
| ------------- | --------------------------------------- |
| 단순 질문     | 직접 답변                               |
| RAG 문서 작성 | Writing Block 안의 최종 문서            |
| 코드 리뷰     | Findings + Fix Direction                |
| 기능 설계     | DB / API / UI / Risk 통합 결과          |
| 배포 계획     | 단계별 계획 + Risk + Approval 필요 항목 |
| 문서 검수     | Pass / Fail + Findings                  |
| 수정 요청     | Updated Output + Change Summary         |

RAG 문서 Final Output 기준:

```text
사용자가 final result only 요청
→ Writing Block만 출력
→ 외부 설명 없음
→ 중간 과정 없음
→ Retrieval Queries 포함
```

기능 개발 Final Output 기준:

```md
## Final Output

### Requirement Summary

...

### DB Design

...

### Backend API Design

...

### Frontend Integration Design

...

### Risks

...

### Open Questions

...

### Recommended Implementation Order

...
```

---

### [FAQ]

Q. Final Output Policy가 뭐야?
A. PM Agent가 사용자에게 최종 결과를 전달할 때 따르는 출력 규칙이다.

Q. Agent 내부 과정을 모두 보여줘야 해?
A. 아니다. 사용자가 원하지 않으면 최종 결과 중심으로 제공해야 한다.

Q. RAG 문서 제작 Final Output은 어떻게 해야 해?
A. 사용자가 요구한 writing block 형식과 문서 구조를 그대로 지켜야 한다.

Q. Open Question은 숨겨도 돼?
A. 아니다. 미확정 사항은 명확히 표시해야 한다.

---

# 7. Implementation Roadmap

## 7.1 Build Order

### [개념]

Build Order는 개인 AI 개발팀을 단계적으로 구축하는 실행 순서이다.

처음부터 완전한 Multi-Agent 자동화를 목표로 하면 복잡도가 높아 실패하기 쉽다.

권장 순서는 RAG 문서 → PM Agent → Documentation Workflow → Review-Fix → Specialist Agent → Workflow Automation이다.

---

### [핵심]

- RAG 문서 구조를 먼저 안정화한다.
- Master Rules와 Domain Rules를 먼저 만든다.
- PM Agent를 먼저 만든다.
- Documentation Workflow로 검증한다.
- Review-Fix Loop를 적용한다.
- SQL / Backend Agent를 추가한다.
- Frontend Agent를 추가한다.
- DevOps / AI Agent는 나중에 추가한다.
- Tool Permission은 천천히 확장한다.
- 자동화보다 품질 안정화가 우선이다.

---

### [실무]

권장 Roadmap:

```text
Phase 1. RAG Foundation
- Master Rules 정리
- Domain Rules 정리
- Project Progress 정리
- Part Documents 제작

Phase 2. PM Agent
- PM Agent Role Definition
- Handoff Template
- Shared State 최소 구조
- Workflow Pattern Selection

Phase 3. Documentation Workflow
- Documentation Agent
- Review Agent
- Fix Agent
- RAG Document Quality Gate

Phase 4. Backend Development Workflow
- SQL Agent
- Backend Agent
- Review-Fix Loop
- API / DB 설계 검증

Phase 5. Frontend Integration Workflow
- Frontend Agent
- API Contract 기반 연동 설계
- Cross-Domain Review

Phase 6. DevOps / AI Agent Extension
- DevOps Agent
- AI Agent
- Tool Permission 강화
- Human Approval Workflow

Phase 7. Automation
- Router Agent 분리
- Planner / Executor 분리
- Workflow 자동 실행
- Evaluation Metrics 적용
```

우선순위:

```text
1. RAG 문서 품질
2. PM Agent Handoff 품질
3. Review-Fix 품질
4. Specialist Agent 정확도
5. Workflow 자동화
6. Tool 실행 자동화
```

---

### [FAQ]

Q. 개인 AI 개발팀 구축은 어떤 순서로 해?
A. RAG 문서 → PM Agent → Documentation Workflow → Review-Fix → SQL / Backend → Frontend → DevOps / AI → 자동화 순서가 좋다.

Q. 왜 RAG 문서를 먼저 만들어야 해?
A. Agent가 참조할 기준 지식과 Rules가 있어야 안정적인 Output을 만들 수 있기 때문이다.

Q. 왜 자동화를 나중에 해야 해?
A. Handoff, RAG Scope, Review-Fix 품질이 안정되기 전에 자동화하면 오류가 빠르게 전파되기 때문이다.

Q. 가장 먼저 안정화할 것은?
A. RAG 문서 품질과 PM Agent Handoff 품질이다.

---

## 7.2 Scaling Criteria

### [개념]

Scaling Criteria는 초기 개인 AI 개발팀을 더 많은 Agent, 더 복잡한 Workflow, 더 높은 자동화 수준으로 확장해도 되는지 판단하는 기준이다.

Scaling은 Agent 수를 늘리는 것만 의미하지 않는다. RAG Scope, Shared State, Tool Permission, Evaluation, Failure Handling도 함께 강화해야 한다.

---

### [핵심]

- Agent 수 증가는 복잡도 증가를 만든다.
- Router Agent는 Agent 수가 많아진 뒤 분리한다.
- Planner Agent는 복잡한 작업이 많아질 때 분리한다.
- Executor Agent는 자동 실행이 필요할 때 분리한다.
- Shared State 구조를 강화해야 한다.
- Tool Permission Matrix를 강화해야 한다.
- Evaluation Metrics를 도입해야 한다.
- Failure Troubleshooting 기록을 쌓아야 한다.
- DevOps Agent는 Human Approval과 함께 확장한다.

---

### [실무]

확장 기준:

| 확장 대상      | 추가 시점                                      |
| -------------- | ---------------------------------------------- |
| Router Agent   | Agent 수가 많고 Routing 실패가 늘 때           |
| Planner Agent  | 복잡한 다단계 작업이 많을 때                   |
| Executor Agent | Plan 기반 자동 실행이 필요할 때                |
| DevOps Agent   | 배포 / 운영 보조가 필요할 때                   |
| AI Agent       | RAG / Prompt / Agent Workflow 개선이 필요할 때 |
| Testing Agent  | 테스트 케이스와 품질 검증 자동화가 필요할 때   |
| Security Agent | 인증 / 인가 / 보안 검토가 많아질 때            |
| Memory Manager | 장기 Memory 충돌이 늘어날 때                   |

확장 전 Checklist:

```md
## Scaling Readiness Checklist

- [ ] PM Agent Handoff 품질이 안정적인가?
- [ ] Shared State가 최신 상태를 유지하는가?
- [ ] Review-Fix Loop가 무한 반복되지 않는가?
- [ ] RAG Scope가 Agent별로 분리되었는가?
- [ ] Tool Permission Matrix가 정의되었는가?
- [ ] Human Approval Workflow가 정의되었는가?
- [ ] Failure Troubleshooting 기준이 있는가?
- [ ] Evaluation Metrics가 최소한으로 적용되는가?
```

---

### [FAQ]

Q. Scaling Criteria가 뭐야?
A. 초기 개인 AI 개발팀을 더 많은 Agent와 자동화 수준으로 확장해도 되는지 판단하는 기준이다.

Q. Agent 수를 늘리면 무조건 좋아?
A. 아니다. Agent 수가 늘면 Handoff, Shared State, RAG Scope, Tool Permission 관리 복잡도도 증가한다.

Q. Router Agent는 언제 분리해?
A. Agent 수가 많아지고 Routing 실패가 늘 때 분리한다.

Q. Executor Agent는 언제 필요해?
A. Plan 기반 자동 실행과 Step별 결과 관리가 필요할 때 필요하다.

---

# 8. Operation and Maintenance

## 8.1 Daily Operation

### [개념]

Daily Operation은 개인 AI 개발팀을 실제로 사용할 때 반복적으로 수행하는 운영 방식이다.

개인 AI 개발팀은 한 번 구축하고 끝나는 시스템이 아니라, RAG 문서 업데이트, Agent Prompt 개선, Failure 기록, Evaluation 결과 반영을 통해 점진적으로 개선해야 한다.

---

### [핵심]

- PM Agent를 단일 진입점으로 사용한다.
- RAG 문서를 지속적으로 업데이트한다.
- Agent Output 실패를 기록한다.
- Handoff 문제를 개선한다.
- Review Findings를 누적 분석한다.
- Fix 과정의 Regression을 확인한다.
- Tool Permission을 주기적으로 점검한다.
- 오래된 Memory와 State를 정리한다.
- 새로운 Domain은 Domain Rules부터 만든다.

---

### [실무]

일상 운영 Flow:

```text
1. User가 PM Agent에게 요청
2. PM Agent가 Workflow Pattern 선택
3. 필요한 Agent에게 Handoff
4. Agent Output 수신
5. Review Agent 검토
6. Fix Agent 수정
7. PM Agent Final Output 제공
8. Failure 또는 개선점 기록
9. 필요한 RAG 문서 보강
```

운영 기록 Template:

```md
## Operation Log

### Date

YYYY-MM-DD

### Request Type

RAG Document / Backend / Frontend / DevOps / Review

### Workflow Pattern

<Pattern>

### Agents Used

- PM Agent
- ...

### Result

Completed / Partial / Failed

### Failure

<Failure Type or None>

### Improvement Candidate

<Prompt / RAG / Handoff / Review / Tool Permission>
```

---

### [FAQ]

Q. 개인 AI 개발팀은 어떻게 일상 운영해?
A. PM Agent를 단일 진입점으로 사용하고, Agent Output을 Review-Fix 후 최종 통합하는 방식으로 운영한다.

Q. 운영 중 가장 자주 개선할 것은?
A. Handoff Template, RAG Scope, Review Checklist, Agent Prompt다.

Q. 새로운 Domain을 추가할 때 먼저 할 일은?
A. 해당 Domain Rules와 기본 RAG 문서를 먼저 작성해야 한다.

Q. Failure 기록은 왜 필요해?
A. 반복 실패를 줄이고 Agent Definition과 Workflow를 개선하기 위해 필요하다.

---

## 8.2 Maintenance Checklist

### [개념]

Maintenance Checklist는 개인 AI 개발팀의 RAG 문서, Agent Definition, Workflow, Tool Permission, Memory를 주기적으로 점검하는 기준이다.

Maintenance를 하지 않으면 문서가 오래되고, Agent Prompt가 현재 프로젝트와 맞지 않으며, Memory와 Shared State 충돌이 증가한다.

---

### [핵심]

- RAG 문서 최신성을 확인한다.
- Domain Rules 누락을 확인한다.
- Agent Definition을 점검한다.
- Handoff Template을 점검한다.
- Review Criteria를 점검한다.
- Tool Permission Matrix를 점검한다.
- Memory 충돌을 점검한다.
- Failure Log를 기반으로 개선한다.
- Evaluation Metrics를 확인한다.

---

### [실무]

Maintenance Checklist:

```md
## Maintenance Checklist

### RAG Documents

- [ ] Master Rules가 최신인가?
- [ ] Domain Rules가 최신인가?
- [ ] Project Progress가 최신인가?
- [ ] Part Documents에 Retrieval Queries가 있는가?
- [ ] FAQ가 실제 검색 질문과 맞는가?
- [ ] 중복 / 오타 / 용어 불일치가 과도하지 않은가?

### Agent Definitions

- [ ] Role이 명확한가?
- [ ] Responsibilities가 최신인가?
- [ ] Forbidden Scope가 명확한가?
- [ ] RAG Scope가 적절한가?
- [ ] Output Format이 안정적인가?

### Workflow

- [ ] Workflow Pattern Selection 기준이 명확한가?
- [ ] Handoff Template이 누락 없이 작동하는가?
- [ ] Review-Fix Loop가 종료되는가?
- [ ] Final Integration 기준이 있는가?

### Tool Permission

- [ ] Agent별 Tool Permission이 제한되어 있는가?
- [ ] Dangerous Tool이 Approval 대상인가?
- [ ] Tool Result 기록 기준이 있는가?

### Memory / State

- [ ] 오래된 Memory가 현재 프로젝트와 충돌하지 않는가?
- [ ] Shared State가 Workflow마다 초기화되는가?
- [ ] Open Questions가 Decision으로 잘못 저장되지 않았는가?
```

---

### [FAQ]

Q. Maintenance Checklist가 뭐야?
A. 개인 AI 개발팀의 RAG 문서, Agent Definition, Workflow, Tool Permission, Memory를 주기적으로 점검하는 기준이다.

Q. Maintenance를 하지 않으면 어떻게 돼?
A. 오래된 문서와 Prompt가 현재 프로젝트와 충돌하고 Agent Output 품질이 떨어질 수 있다.

Q. 가장 중요한 Maintenance 대상은?
A. Master Rules, Domain Rules, Agent Definition, Handoff Template, Review Checklist다.

Q. Failure Log는 Maintenance에 어떻게 사용해?
A. 반복 실패 유형을 찾아 Agent Prompt, RAG Scope, Workflow 기준을 수정하는 데 사용한다.

---

# 9. Final Implementation Checklist

## 9.1 Minimum Viable Personal AI Development Team Checklist

### [개념]

Minimum Viable Personal AI Development Team Checklist는 개인 AI 개발팀 구축이 최소 운영 가능한 상태인지 확인하는 기준이다.

이 Checklist를 통과하면 RAG 문서 제작, 문서 검수, 간단한 Backend 설계, Review-Fix Workflow 테스트를 시작할 수 있다.

---

### [핵심]

- RAG 문서 구조가 준비되어야 한다.
- Master Rules가 있어야 한다.
- Domain Rules가 있어야 한다.
- PM Agent Definition이 있어야 한다.
- Handoff Template이 있어야 한다.
- Review Agent Definition이 있어야 한다.
- Fix Agent Definition이 있어야 한다.
- Shared State 최소 구조가 있어야 한다.
- RAG Scope Mapping이 있어야 한다.
- Tool Permission 기본 정책이 있어야 한다.
- Review-Fix Stop Condition이 있어야 한다.

---

### [실무]

Minimum Viable Personal AI Development Team Checklist:

```md
## Minimum Viable Personal AI Development Team Checklist

### RAG Foundation

- [ ] Master RAG Rules 작성 완료
- [ ] Project Progress 작성 완료
- [ ] Target Domain Rules 작성 완료
- [ ] Part Documents 작성 시작
- [ ] Retrieval Queries 포함 규칙 적용

### Agent Foundation

- [ ] PM Agent Definition 작성
- [ ] Documentation Agent Definition 작성
- [ ] Review Agent Definition 작성
- [ ] Fix Agent Definition 작성
- [ ] Backend Agent Definition 작성 예정
- [ ] SQL Agent Definition 작성 예정

### Workflow Foundation

- [ ] PM 중심 단일 진입점 설정
- [ ] Handoff Template 설정
- [ ] Shared State 최소 구조 설정
- [ ] Review-Fix Loop 설정
- [ ] Max Iteration 설정
- [ ] Quality Gate 설정

### Safety Foundation

- [ ] Tool Permission 기본 정책 설정
- [ ] Dangerous Tool Human Approval 설정
- [ ] File Delete / DB Write / Deploy 자동 실행 금지
- [ ] Tool Result 기록 기준 설정

### Operation Foundation

- [ ] Failure Log Template 준비
- [ ] Maintenance Checklist 준비
- [ ] RAG Scope Mapping 준비
- [ ] Final Output Policy 준비
```

---

### [FAQ]

Q. 개인 AI 개발팀 최소 구축 기준은?
A. Master Rules, Domain Rules, PM Agent, Handoff Template, Review Agent, Fix Agent, Shared State, RAG Scope, Tool Permission이 준비되어야 한다.

Q. 최소 구축 후 바로 가능한 작업은?
A. RAG 문서 제작, 문서 검수, 간단한 Backend 설계, Review-Fix Workflow 테스트가 가능하다.

Q. Tool 실행 자동화는 최소 구축에 포함돼?
A. 아니다. 초기에는 위험 Tool 자동 실행을 금지하고 승인 절차부터 만든다.

Q. 개인 AI 개발팀 구축에서 가장 중요한 것은?
A. PM Agent Handoff 품질, RAG 문서 품질, Review-Fix 품질이다.

---

# 10. Implementation Failure Control

## 10.1 Common Implementation Failures

### [개념]

Implementation Failure Control은 개인 AI 개발팀 구축 중 자주 발생하는 실패를 예방하고 수정하는 기준이다.

개인 AI 개발팀 구축 실패는 보통 모델 성능보다 RAG 문서 부족, Handoff 부실, Agent Scope 중복, Tool Permission 과다, Review-Fix 부재에서 발생한다.

---

### [핵심]

- Agent를 너무 많이 만들면 관리가 어려워진다.
- RAG 문서가 부족하면 Agent가 추측한다.
- Handoff가 부실하면 Specialist Output이 흔들린다.
- Agent Scope가 겹치면 Output 충돌이 생긴다.
- Review-Fix가 없으면 품질 문제가 누적된다.
- Tool Permission이 과도하면 위험 작업 가능성이 커진다.
- 자동화를 너무 빨리 적용하면 오류가 빠르게 전파된다.
- Failure Log 없이 운영하면 같은 문제가 반복된다.

---

### [실무]

Common Failure Matrix:

| Failure              | Symptom                      | Fix                        |
| -------------------- | ---------------------------- | -------------------------- |
| Agent Over-splitting | Agent는 많은데 결과가 불안정 | 초기 Agent 수 축소         |
| Poor Handoff         | Output 누락 / 추측 증가      | Handoff Template 보강      |
| Weak RAG Foundation  | Domain Rules 누락            | Master / Domain Rules 작성 |
| Role Overlap         | Agent Output 충돌            | Forbidden Scope 추가       |
| No Review-Fix        | 오류가 Final Output으로 전달 | Review Agent 추가          |
| Over-permission      | 위험 Tool 실행 가능          | Least Privilege 적용       |
| Early Automation     | 실패가 자동 확산             | 수동 / 반자동으로 되돌림   |
| No Maintenance       | 오래된 기준 사용             | Maintenance Checklist 적용 |

Implementation Failure Record:

```md
## Implementation Failure

### Failure Type

Poor Handoff

### Symptom

Backend Agent Output에서 Security Rule이 반복적으로 누락됨

### Root Cause

PM Agent Handoff의 Constraints에 Security Rule이 포함되지 않음

### Fix Direction

Backend Handoff Template에 Security / Authorization 항목을 필수 추가

### Prevention Rule

Backend 작업은 Security Advanced RAG Scope를 조건부 포함
```

---

### [FAQ]

Q. 개인 AI 개발팀 구축 중 가장 흔한 실패는?
A. Poor Handoff, Weak RAG Foundation, Role Overlap, No Review-Fix, Over-permission이다.

Q. Agent를 많이 만들면 더 좋아?
A. 아니다. Agent 수가 많아질수록 Handoff와 Shared State 관리가 어려워진다.

Q. 자동화는 언제 적용해야 해?
A. Handoff, RAG Scope, Review-Fix 품질이 안정된 뒤 적용하는 것이 좋다.

Q. 모델 성능만 올리면 해결돼?
A. 아니다. RAG 문서 품질, Agent Role, Handoff, Review-Fix 기준이 함께 필요하다.

---

# Retrieval Queries

### [FAQ]

Q. Personal AI Development Team이 뭐야?
A. 개인 AI 서버를 PM Agent 중심의 Multi-Agent System으로 운영해 SQL, Backend, Frontend, Review, Fix 작업을 역할별로 처리하는 구조다.

Q. 사용자가 모든 Agent에게 직접 요청해야 해?
A. 아니다. 사용자는 PM Agent에게만 요청하고 PM Agent가 필요한 Agent에게 작업을 분배한다.

Q. 개인 AI 개발팀의 핵심 Agent는?
A. PM Agent, Specialist Agent, Review Agent, Fix Agent다.

Q. 개인 AI 개발팀의 장점은?
A. 역할 분리, RAG Scope 제한, Review-Fix 품질 개선, 최종 결과 통합이 가능하다는 점이다.

Q. 처음부터 모든 Agent를 만들어야 해?
A. 아니다. PM Agent, Documentation Agent, Review Agent, Fix Agent부터 시작하는 것이 안정적이다.

Q. Backend Agent와 SQL Agent는 언제 추가해?
A. RAG 문서 제작 Workflow가 안정화된 뒤 실제 기능 개발 보조를 시작할 때 추가한다.

Q. Router Agent는 처음부터 필요해?
A. 아니다. 초기에는 PM Agent가 Routing을 겸하고 Agent 수가 늘면 Router Agent 분리를 검토한다.

Q. 개인 AI 개발팀을 운영하려면 어떤 서버 구성이 필요해?
A. Ubuntu, Ollama, Text LLM, Embedding Model, RAG 플랫폼, Markdown 문서 구조가 필요하다.

Q. AnythingLLM을 사용할 수 있어?
A. 가능하다. 초기 개인 RAG 기반 Agent 운영에 사용할 수 있다.

Q. Qwen2.5 14B와 BGE-M3 조합은 어떤 역할이야?
A. Qwen2.5 14B는 Text LLM, BGE-M3는 Embedding Model 역할이다.

Q. 처음부터 완전 자동 Agent Workflow를 만들어야 해?
A. 아니다. 처음에는 PM 중심 수동 또는 반자동 Workflow로 시작하고 점진적으로 확장하는 것이 좋다.

Q. PM Agent는 무엇을 구현해야 해?
A. 요구사항 분석, 작업 분해, Routing, Handoff, Shared State, 결과 통합을 구현해야 한다.

Q. PM Agent가 직접 코드나 문서를 작성해도 돼?
A. 간단한 작업은 가능하지만, 전문 Domain 작업은 Specialist Agent에게 위임하는 것이 원칙이다.

Q. PM Agent의 가장 중요한 Output은?
A. 구조화된 Handoff와 최종 통합 결과다.

Q. Specialist Agent는 무엇을 구현해야 해?
A. 자기 Domain의 설계, 분석, 검토, 출력 구조를 담당해야 한다.

Q. Specialist Agent가 Scope 밖 작업을 받으면?
A. PM Agent에게 Scope 밖이라고 반환하거나 필요한 Target Agent를 제안해야 한다.

Q. Backend Agent의 기본 RAG Scope는?
A. Java, Spring Boot, JPA, Security, API Design이다.

Q. Review Agent와 Fix Agent를 왜 분리해?
A. 검토와 수정을 분리해야 책임 경계, 수정 추적, Regression 관리가 쉬워진다.

Q. Review Agent는 직접 수정해도 돼?
A. 원칙적으로 안 된다. Review Agent는 Finding을 작성하고 Fix Agent가 수정한다.

Q. Fix Agent의 핵심 원칙은?
A. Review Findings 범위 안에서 최소 수정하고 기존 요구사항을 보존하는 것이다.

Q. RAG Document Set Implementation이 뭐야?
A. 개인 AI 개발팀이 사용할 Markdown 기반 RAG 문서 세트를 구성하는 작업이다.

Q. RAG 문서는 사람용 설명 위주로 만들면 돼?
A. 아니다. Agent Retrieval을 위해 구조화, FAQ, Retrieval Queries를 우선해야 한다.

Q. RAG 문서에 Retrieval Queries가 필요한 이유는?
A. 사용자 질문 표현과 문서 Chunk 매칭을 강화하기 위해 필요하다.

Q. Agent RAG Scope Mapping이 뭐야?
A. 각 Agent가 어떤 RAG 문서 범위를 검색할지 연결하는 작업이다.

Q. Agent별 RAG Scope가 필요한 이유는?
A. 관련 없는 문서 검색을 줄이고 필요한 Domain Rules를 누락하지 않기 위해서다.

Q. 초기 Workflow는 어떻게 시작해?
A. User → PM Agent → Target Agent → Review Agent → Fix Agent → Final Output 구조로 시작한다.

Q. 처음부터 자동화해야 해?
A. 아니다. 처음에는 수동 또는 반자동 Handoff로 품질을 안정화하는 것이 좋다.

Q. 기능 개발 Workflow는 어떤 구조가 좋아?
A. PM Agent → SQL Agent → Backend Agent → Frontend Agent → Review Agent → Fix Agent 구조가 적합하다.

Q. 왜 SQL Agent가 먼저야?
A. DB Schema와 관계가 Backend Entity, Repository, API 설계의 기반이 되기 때문이다.

Q. 왜 Backend Agent가 Frontend Agent보다 먼저야?
A. Frontend는 API Contract와 DTO Field를 기준으로 State와 API 연동을 설계해야 하기 때문이다.

Q. Agent System Prompt에는 무엇이 들어가야 해?
A. Role, Responsibilities, Forbidden Scope, RAG Scope, Tool Permission, Output Format, Quality Criteria, Failure Handling이 들어가야 한다.

Q. Forbidden Scope가 왜 필요해?
A. Agent가 자기 역할 밖 작업을 수행하는 Role Overlap을 막기 위해 필요하다.

Q. Final Output Policy가 뭐야?
A. PM Agent가 사용자에게 최종 결과를 전달할 때 따르는 출력 규칙이다.

Q. Agent 내부 과정을 모두 보여줘야 해?
A. 아니다. 사용자가 원하지 않으면 최종 결과 중심으로 제공해야 한다.

Q. 개인 AI 개발팀 구축은 어떤 순서로 해?
A. RAG 문서 → PM Agent → Documentation Workflow → Review-Fix → SQL / Backend → Frontend → DevOps / AI → 자동화 순서가 좋다.

Q. 왜 RAG 문서를 먼저 만들어야 해?
A. Agent가 참조할 기준 지식과 Rules가 있어야 안정적인 Output을 만들 수 있기 때문이다.

Q. 왜 자동화를 나중에 해야 해?
A. Handoff, RAG Scope, Review-Fix 품질이 안정되기 전에 자동화하면 오류가 빠르게 전파되기 때문이다.

Q. Scaling Criteria가 뭐야?
A. 초기 개인 AI 개발팀을 더 많은 Agent와 자동화 수준으로 확장해도 되는지 판단하는 기준이다.

Q. Agent 수를 늘리면 무조건 좋아?
A. 아니다. Agent 수가 늘면 Handoff, Shared State, RAG Scope, Tool Permission 관리 복잡도도 증가한다.

Q. 개인 AI 개발팀은 어떻게 일상 운영해?
A. PM Agent를 단일 진입점으로 사용하고, Agent Output을 Review-Fix 후 최종 통합하는 방식으로 운영한다.

Q. 운영 중 가장 자주 개선할 것은?
A. Handoff Template, RAG Scope, Review Checklist, Agent Prompt다.

Q. Maintenance Checklist가 뭐야?
A. 개인 AI 개발팀의 RAG 문서, Agent Definition, Workflow, Tool Permission, Memory를 주기적으로 점검하는 기준이다.

Q. Maintenance를 하지 않으면 어떻게 돼?
A. 오래된 문서와 Prompt가 현재 프로젝트와 충돌하고 Agent Output 품질이 떨어질 수 있다.

Q. 개인 AI 개발팀 최소 구축 기준은?
A. Master Rules, Domain Rules, PM Agent, Handoff Template, Review Agent, Fix Agent, Shared State, RAG Scope, Tool Permission이 준비되어야 한다.

Q. 최소 구축 후 바로 가능한 작업은?
A. RAG 문서 제작, 문서 검수, 간단한 Backend 설계, Review-Fix Workflow 테스트가 가능하다.

Q. Tool 실행 자동화는 최소 구축에 포함돼?
A. 아니다. 초기에는 위험 Tool 자동 실행을 금지하고 승인 절차부터 만든다.

Q. 개인 AI 개발팀 구축에서 가장 중요한 것은?
A. PM Agent Handoff 품질, RAG 문서 품질, Review-Fix 품질이다.

Q. 개인 AI 개발팀 구축 중 가장 흔한 실패는?
A. Poor Handoff, Weak RAG Foundation, Role Overlap, No Review-Fix, Over-permission이다.

Q. 자동화는 언제 적용해야 해?
A. Handoff, RAG Scope, Review-Fix 품질이 안정된 뒤 적용하는 것이 좋다.

Q. 모델 성능만 올리면 해결돼?
A. 아니다. RAG 문서 품질, Agent Role, Handoff, Review-Fix 기준이 함께 필요하다.
