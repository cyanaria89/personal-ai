# Multi-Agent System Part04 - Specialist Agent

---

# 1. Specialist Agent Core

## 1.1 Specialist Agent Definition

### [개념]

Specialist Agent는 Multi-Agent System에서 특정 Domain 작업을 전문적으로 수행하는 Agent이다.

Specialist Agent는 PM Agent가 전달한 Handoff를 기반으로 자신의 Responsibility, Scope, RAG Scope, Tool Permission 안에서 작업한다.

Specialist Agent의 핵심은 모든 작업을 처리하는 것이 아니라, 자기 Domain에서 명확한 Output을 생성하는 것이다.

기본 구조:

```text
PM Agent Handoff
→ Specialist Agent
→ Domain Rules Load
→ RAG Context Retrieval
→ Domain Task Execution
→ Structured Output
→ Review Agent
```

Specialist Agent 예시:

```text
SQL Agent
Backend Agent
Frontend Agent
DevOps Agent
AI Agent
Security Agent
Testing Agent
Documentation Agent
```

---

### [핵심]

- Specialist Agent는 특정 Domain 작업을 담당한다.
- PM Agent가 전달한 Handoff를 기준으로 작업한다.
- 자기 Domain Rules를 우선 적용한다.
- 필요한 RAG Scope 안에서 Context를 검색한다.
- Tool Permission 범위 안에서만 Tool을 사용한다.
- Output은 다음 Agent가 사용할 수 있도록 구조화한다.
- 불확실한 내용은 Assumption 또는 Open Question으로 표시한다.
- Scope 밖 작업은 PM Agent에게 반환한다.
- Specialist Agent는 PM Agent 역할을 대체하지 않는다.
- Specialist Agent는 Review Agent 역할을 대체하지 않는다.

---

### [실무]

2026 실무 기준에서 Specialist Agent는 Domain Expert 역할로 설계한다.

Specialist Agent는 아래 기준을 반드시 가져야 한다.

```text
Name
→ Role
→ Responsibility
→ Scope
→ Out of Scope
→ Input
→ Output
→ RAG Scope
→ Tool Permission
→ Done Criteria
→ Failure Handling
```

나쁜 Specialist Agent 예시:

```md
## Backend Expert

백엔드를 잘 만들어준다.
```

문제:

- Role 불명확
- Responsibility 없음
- Scope 없음
- Input / Output 없음
- RAG Scope 없음
- Tool Permission 없음
- Done Criteria 없음
- PM Agent와 책임 충돌 가능

좋은 Specialist Agent 예시:

```md
## Backend Agent

### Role

Spring Boot Backend API 설계 및 구현 방향 제시

### Responsibility

- API Contract 설계
- DTO 설계
- Service 책임 설계
- Exception Case 정리
- Transaction 기준 검토

### Scope

- Controller
- Service
- DTO
- JPA 연동 기준
- Security 적용 지점

### Out of Scope

- React Component 구현
- DB 직접 변경
- 운영 서버 배포

### Output

- API Contract
- Backend Implementation Plan
- Risks
- Assumptions
- Open Questions
```

---

### [FAQ]

Q. Specialist Agent가 뭐야?
A. SQL, Backend, Frontend, DevOps, AI처럼 특정 Domain 작업을 전문적으로 수행하는 Agent다.

Q. Specialist Agent는 모든 작업을 처리해도 돼?
A. 아니다. 자기 Responsibility와 Scope 안의 작업만 처리해야 한다.

Q. Specialist Agent는 누구에게 작업을 받아?
A. 보통 PM Agent가 생성한 Handoff를 통해 작업을 받는다.

Q. Specialist Agent 결과는 누가 검토해?
A. Review Agent가 요구사항, Domain Rules, 일관성, 위험 기준으로 검토한다.

---

# 2. Specialist Agent Operating Rules

## 2.1 Specialist Agent Input Handling

### [개념]

Specialist Agent Input Handling은 Specialist Agent가 PM Agent Handoff를 해석하고 작업 준비를 수행하는 단계이다.

Specialist Agent는 사용자 요청 원문만 보고 작업하지 않고, PM Agent가 정리한 Task, Requirements, Constraints, Context, RAG Scope, Done Criteria를 기준으로 작업해야 한다.

Input 처리 구조:

```text
Receive Handoff
→ Validate Task
→ Check Requirements
→ Check Constraints
→ Check Scope
→ Load RAG Context
→ Execute Domain Task
```

---

### [핵심]

- Specialist Agent는 Handoff를 먼저 검토한다.
- Task가 자기 Scope에 속하는지 확인한다.
- Requirements와 Constraints를 분리해서 해석한다.
- Done Criteria를 작업 완료 기준으로 사용한다.
- RAG Scope가 적절한지 확인한다.
- Tool Permission 범위 안에서만 작업한다.
- Missing Context가 있으면 Assumption 또는 Open Question으로 표시한다.
- 치명적 Missing Context는 PM Agent에게 반환한다.
- Scope 밖 요청은 직접 처리하지 않는다.

---

### [실무]

Specialist Agent Input 검토 예시:

```json
{
  "from": "PM Agent",
  "to": "Backend Agent",
  "task": "Design review API",
  "requirements": [
    "Authenticated user can create review",
    "Review author can update own review",
    "Review list uses Slice"
  ],
  "constraints": [
    "Spring Boot",
    "JPA",
    "JWT Authentication",
    "ApiResponse format"
  ],
  "ragScope": [
    "Spring Boot",
    "JPA Advanced",
    "Security Advanced",
    "API Design"
  ],
  "doneCriteria": [
    "API Contract defined",
    "DTO design included",
    "Exception cases included"
  ]
}
```

Backend Agent Input Handling:

```text
1. Task가 Backend API 설계인지 확인
2. 인증 요구사항 확인
3. Slice 사용 제약 확인
4. ApiResponse 형식 확인
5. Spring Boot / JPA / Security RAG Scope 사용
6. API Contract / DTO / Exception 기준 Output 생성
```

치명적 Missing Context 예시:

```text
Task: 기존 코드 수정
Missing Context: 실제 기존 코드 없음
Action: PM Agent에게 Required Context 반환
```

일반 Missing Context 예시:

```text
Task: Review API 설계
Missing Context: 중복 리뷰 허용 여부 불명확
Action: Assumption 또는 Open Question으로 표시 후 진행
```

---

### [FAQ]

Q. Specialist Agent Input Handling이 뭐야?
A. Specialist Agent가 PM Agent Handoff를 검토하고 작업에 필요한 요구사항, 제약, Context를 정리하는 단계다.

Q. Specialist Agent는 사용자 요청 원문만 보고 작업해도 돼?
A. 아니다. PM Agent가 정리한 Handoff와 Shared State를 기준으로 작업해야 한다.

Q. Missing Context가 있으면 어떻게 해?
A. 치명적 누락은 PM Agent에게 반환하고, 일반적 누락은 Assumption 또는 Open Question으로 표시한다.

Q. Scope 밖 요청이 들어오면 어떻게 해?
A. 직접 처리하지 않고 PM Agent에게 반환해야 한다.

---

## 2.2 Specialist Agent Output Handling

### [개념]

Specialist Agent Output Handling은 Specialist Agent가 작업 결과를 다음 Agent가 사용할 수 있도록 구조화해 반환하는 단계이다.

Specialist Agent Output은 최종 답변이 아니라 PM Agent, Review Agent, Fix Agent가 사용할 수 있는 중간 산출물인 경우가 많다.

기본 Output 구조:

```text
Task Summary
→ Result
→ Decisions
→ Assumptions
→ Risks
→ Open Questions
→ Next Step
```

---

### [핵심]

- Specialist Agent Output은 구조화되어야 한다.
- Task Summary를 포함한다.
- 실제 Result를 명확히 제공한다.
- 작업 중 내린 Decisions를 기록한다.
- Assumptions를 표시한다.
- Risks를 표시한다.
- Open Questions를 남긴다.
- Next Step을 제안한다.
- Review Agent가 검토할 수 있어야 한다.
- 실패한 경우 실패 상태를 명확히 반환한다.

---

### [실무]

Specialist Agent Output Template:

```md
## Specialist Agent Output

### Source Agent

Backend Agent

### Task

Review API 설계

### Result

- POST /reviews
- GET /festivals/{festivalId}/reviews
- PATCH /reviews/{reviewId}
- DELETE /reviews/{reviewId}

### Decisions

- 목록 조회는 Slice 사용
- 작성자 본인만 수정 / 삭제 가능
- Rating은 0~5 범위 검증

### Assumptions

- 인증 사용자는 SecurityContext에서 조회
- Reviews Entity는 Users, Festivals와 연관됨

### Risks

- 중복 리뷰 허용 여부 불명확
- 삭제 정책 Soft Delete 여부 확인 필요

### Open Questions

- 한 사용자가 같은 축제에 여러 리뷰를 작성할 수 있는가?

### Next Step

Review Agent가 API Contract와 요구사항 일치 여부 검토
```

실패 Output Template:

```md
## Specialist Agent Output

### Source Agent

Backend Agent

### Status

Failed

### Task

기존 ReviewService 수정

### Failure Reason

기존 ReviewService 코드가 제공되지 않아 정확한 수정 불가

### Required Context

- ReviewService.java
- ReviewController.java
- ReviewReqDto.java
- ReviewResDto.java

### Safe Alternative

기존 코드 없이 일반 설계안만 제공 가능

### Next Step

PM Agent가 필요한 파일을 수집한 뒤 재요청
```

---

### [FAQ]

Q. Specialist Agent Output은 뭐야?
A. Specialist Agent가 작업 결과로 반환하는 구조화된 산출물이다.

Q. Specialist Agent Output에는 뭐가 들어가야 해?
A. Task Summary, Result, Decisions, Assumptions, Risks, Open Questions, Next Step이 들어가야 한다.

Q. 실패한 경우도 Output을 만들어야 해?
A. 만들어야 한다. Failure Reason, Required Context, Safe Alternative, Next Step을 기록해야 한다.

Q. Specialist Agent Output은 왜 구조화해야 해?
A. PM Agent가 통합하고 Review Agent가 검토할 수 있어야 하기 때문이다.

---

# 3. SQL Agent

## 3.1 SQL Agent Definition

### [개념]

SQL Agent는 Database Schema, SQL Query, Index, Data Consistency를 담당하는 Specialist Agent이다.

SQL Agent는 DB 구조와 데이터 접근 기준을 설계하며, Backend Agent가 사용할 수 있는 Schema / Query 기준을 제공한다.

SQL Agent 기본 Flow:

```text
PM Agent Handoff
→ SQL Agent
→ Schema Requirement Analysis
→ Table / Relationship Design
→ Query / Index Candidate
→ Risk / Assumption Output
→ Backend Agent
```

---

### [핵심]

- SQL Agent는 Database 관련 작업을 담당한다.
- Table, PK, FK, Index를 설계한다.
- Query 구조를 제안한다.
- Data Consistency 위험을 검토한다.
- JPA Entity 설계에 영향을 주는 기준을 제공한다.
- Backend Agent가 사용할 수 있는 Schema Decision을 출력한다.
- Controller / Service 구현은 Scope 밖이다.
- Frontend UI 구현은 Scope 밖이다.
- Production DB 직접 변경은 Tool Permission 밖이다.

---

### [실무]

SQL Agent Definition:

```md
## Agent Definition

### Name

SQL Agent

### Role

Database Schema, Query, Index 설계 담당 Specialist Agent

### Responsibility

- Table 설계
- PK / FK 설계
- Relationship 설계
- Index 후보 제안
- Query Pattern 제안
- Data Consistency Risk 검토
- JPA Entity 설계 기준 제공

### Scope

- Database Schema
- SQL Query
- Index
- Constraint
- Relationship
- Data Consistency

### Out of Scope

- Controller 구현
- Service 구현
- Frontend UI 구현
- 운영 DB 직접 변경
- 배포 실행

### Input

- PM Agent Task
- Requirements
- Existing Schema Context
- Domain Rules
- Relevant RAG Context

### Output

- Table Design
- Relationship
- Index Candidates
- Query Pattern
- Data Consistency Risks
- Assumptions
- Open Questions

### Tool Permission

- RAG Search
- Schema Read
- Query Read

### RAG Scope

- SQL
- JPA Advanced
- QueryDSL Practical
- API Design

### Done Criteria

- Table 구조가 명확함
- PK / FK 기준 포함
- Index 후보 포함
- Data Consistency Risk 포함
- Backend Agent가 사용할 수 있는 Output 생성
```

SQL Agent Output 예시:

```md
## SQL Agent Output

### Task

Festival Review Schema 설계

### Table Design

- reviews
- review_id PK
- user_id FK
- festival_id FK
- rating
- content
- created_at
- updated_at

### Index Candidates

- idx_reviews_festival_id_created_at
- idx_reviews_user_id

### Decisions

- reviews는 users, festivals와 N:1 관계
- 목록 조회는 festival_id + created_at 기준 정렬

### Risks

- 한 사용자의 동일 축제 중복 리뷰 허용 여부 확인 필요
- Soft Delete 필요 여부 확인 필요

### Next Step

Backend Agent가 Entity / DTO / API Contract 설계
```

---

### [FAQ]

Q. SQL Agent는 뭐 하는 Agent야?
A. Database Schema, SQL Query, Index, Data Consistency를 설계하는 Specialist Agent다.

Q. SQL Agent가 Backend Service도 구현해?
A. 아니다. Service 구현은 Backend Agent의 책임이다.

Q. SQL Agent Output에는 뭐가 있어야 해?
A. Table Design, Relationship, Index Candidates, Query Pattern, Data Consistency Risks가 있어야 한다.

Q. SQL Agent의 주요 RAG Scope는?
A. SQL, JPA Advanced, QueryDSL Practical, API Design이다.

---

# 4. Backend Agent

## 4.1 Backend Agent Definition

### [개념]

Backend Agent는 Spring Boot 기반 Backend API, Service, DTO, Transaction, Exception Handling, Security 적용 기준을 담당하는 Specialist Agent이다.

Backend Agent는 SQL Agent의 Schema 기준과 PM Agent의 요구사항을 바탕으로 Backend Application Layer를 설계한다.

Backend Agent 기본 Flow:

```text
PM Agent Handoff
→ Backend Agent
→ API Contract Design
→ DTO Design
→ Service Responsibility Design
→ Exception / Transaction Rule
→ Structured Backend Output
→ Review Agent
```

---

### [핵심]

- Backend Agent는 Spring Boot Backend 작업을 담당한다.
- API Contract를 설계한다.
- Request / Response DTO를 설계한다.
- Service Layer 책임을 정의한다.
- Transaction 기준을 검토한다.
- Exception Handling 기준을 포함한다.
- Security 적용 지점을 검토한다.
- SQL Agent의 Schema Decision을 반영한다.
- Frontend UI 구현은 Scope 밖이다.
- 운영 DB 변경과 배포 실행은 Scope 밖이다.

---

### [실무]

Backend Agent Definition:

```md
## Agent Definition

### Name

Backend Agent

### Role

Spring Boot Backend API 및 Application Layer 설계 담당 Specialist Agent

### Responsibility

- REST API Contract 설계
- Controller 구조 설계
- Request DTO 설계
- Response DTO 설계
- Service Method 설계
- Transaction 기준 검토
- Exception Handling 기준 설계
- Security 적용 지점 검토
- Test Case 후보 제안

### Scope

- Backend API
- Controller
- Service
- DTO
- JPA 연동 기준
- Security 적용 기준
- Error Response
- Transaction

### Out of Scope

- React Component 구현
- UI 디자인 결정
- DB 직접 변경
- 운영 서버 배포
- 모델 Fine-Tuning

### Input

- PM Agent Task
- Requirements
- API Requirement
- SQL Agent Output
- Entity Context
- Domain Rules
- Relevant RAG Context

### Output

- API Contract
- DTO Design
- Service Method Plan
- Exception Cases
- Security Rules
- Transaction Rules
- Risks
- Assumptions

### Tool Permission

- RAG Search
- File Read
- Code Search

### RAG Scope

- Java
- Spring Boot
- JPA Advanced
- Security Advanced
- API Design
- Testing

### Done Criteria

- API Contract 정의
- Request / Response 구조 정의
- Service 책임 정의
- Validation 기준 포함
- Exception Case 포함
- Security 적용 기준 포함
- Review 가능한 Output 생성
```

Backend Agent Output 예시:

```md
## Backend Agent Output

### Task

Festival Review API 설계

### API Contract

- POST /reviews
- GET /festivals/{festivalId}/reviews
- PATCH /reviews/{reviewId}
- DELETE /reviews/{reviewId}

### DTO Design

- ReviewCreateReqDto
- ReviewUpdateReqDto
- ReviewResDto

### Service Methods

- createReview()
- getFestivalReviews()
- updateReview()
- deleteReview()

### Security Rules

- 리뷰 작성은 인증 사용자만 가능
- 리뷰 수정 / 삭제는 작성자 본인만 가능

### Exception Cases

- Festival Not Found
- Review Not Found
- Unauthorized Review Access
- Invalid Rating

### Risks

- 중복 리뷰 정책 확인 필요
- 삭제 정책 확인 필요

### Next Step

Review Agent가 API Contract와 SQL Agent Output 일치 여부 검토
```

---

### [FAQ]

Q. Backend Agent는 뭐 하는 Agent야?
A. Spring Boot 기반 API, DTO, Service, Exception, Transaction, Security 기준을 설계하는 Specialist Agent다.

Q. Backend Agent가 DB Schema를 직접 확정해?
A. Schema는 SQL Agent가 주도하고 Backend Agent는 Entity / JPA 연동 관점에서 검토한다.

Q. Backend Agent Output에는 뭐가 있어야 해?
A. API Contract, DTO Design, Service Method Plan, Exception Cases, Security Rules, Risks가 있어야 한다.

Q. Backend Agent의 주요 RAG Scope는?
A. Java, Spring Boot, JPA Advanced, Security Advanced, API Design, Testing이다.

---

# 5. Frontend Agent

## 5.1 Frontend Agent Definition

### [개념]

Frontend Agent는 Frontend UI, Component, State, API Integration, Loading / Error UX를 담당하는 Specialist Agent이다.

Frontend Agent는 Backend Agent가 정의한 API Contract를 기준으로 화면 흐름과 API 연동 구조를 설계한다.

Frontend Agent 기본 Flow:

```text
PM Agent Handoff
→ Frontend Agent
→ API Contract Check
→ Component Design
→ State Design
→ API Call Flow
→ Loading / Error UX
→ Structured Frontend Output
```

---

### [핵심]

- Frontend Agent는 UI와 API 연동을 담당한다.
- Component 구조를 설계한다.
- State 관리 기준을 설계한다.
- Backend API Contract를 기준으로 API 호출 흐름을 만든다.
- Loading / Error / Empty 상태를 포함한다.
- Form Handling과 Validation 기준을 포함한다.
- Backend API 경로를 임의로 변경하지 않는다.
- DB Schema 변경은 Scope 밖이다.
- Backend Business Logic 구현은 Scope 밖이다.

---

### [실무]

Frontend Agent Definition:

```md
## Agent Definition

### Name

Frontend Agent

### Role

Frontend UI, Component, State, API Integration 설계 담당 Specialist Agent

### Responsibility

- 화면 Flow 설계
- Component 구조 설계
- State 관리 설계
- API Call Flow 설계
- Form Handling 설계
- Client Validation 기준 설계
- Loading / Error / Empty UX 설계
- Backend API Contract 반영

### Scope

- React Component
- Routing
- State
- API Integration
- Form
- Client Validation
- UI State UX

### Out of Scope

- DB Schema 변경
- Backend Service 구현
- Security Filter 수정
- 운영 서버 배포
- API Contract 임의 변경

### Input

- PM Agent Task
- Requirements
- Backend API Contract
- UI Requirement
- Domain Rules
- Relevant RAG Context

### Output

- Component Design
- State Design
- API Call Flow
- Form Handling Plan
- Loading / Error UX
- Risks
- Assumptions

### Tool Permission

- RAG Search
- File Read
- Code Search

### RAG Scope

- HTML CSS Foundation
- JavaScript Foundation
- TypeScript Foundation
- React Core
- React Component Design
- React Router
- State Management
- Data Fetching REST API Integration
- Error Handling Loading UX

### Done Criteria

- Component 구조 정의
- API 호출 흐름 정의
- State 구조 정의
- Loading / Error / Empty 상태 포함
- Backend API Contract와 일치
- Review 가능한 Output 생성
```

Frontend Agent Output 예시:

```md
## Frontend Agent Output

### Task

Festival Review UI 연동 설계

### Components

- ReviewList
- ReviewItem
- ReviewForm
- ReviewEditModal

### State

- reviews
- isLoading
- error
- formState
- hasNext

### API Call Flow

- GET /festivals/{festivalId}/reviews
- POST /reviews
- PATCH /reviews/{reviewId}
- DELETE /reviews/{reviewId}

### UX States

- Loading
- Empty Review
- Error Retry
- Submit Disabled
- Validation Error

### Risks

- Backend API Response Field 확인 필요
- 인증 만료 시 처리 정책 필요

### Next Step

Review Agent가 Backend API Contract와 Frontend API Call 일치 여부 검토
```

---

### [FAQ]

Q. Frontend Agent는 뭐 하는 Agent야?
A. Frontend UI, Component, State, API Integration, Loading / Error UX를 설계하는 Specialist Agent다.

Q. Frontend Agent가 API 경로를 마음대로 바꿔도 돼?
A. 안 된다. Backend API Contract를 기준으로 작업해야 한다.

Q. Frontend Agent Output에는 뭐가 있어야 해?
A. Component Design, State Design, API Call Flow, Form Handling, Loading / Error UX, Risks가 있어야 한다.

Q. Frontend Agent의 주요 RAG Scope는?
A. HTML, CSS, JavaScript, TypeScript, React, State Management, Data Fetching REST API Integration이다.

---

# 6. DevOps Agent

## 6.1 DevOps Agent Definition

### [개념]

DevOps Agent는 개발 환경, Docker, Linux, CI/CD, 배포 절차, 운영 위험 검토를 담당하는 Specialist Agent이다.

DevOps Agent는 실행 환경과 운영 절차를 설계하지만, 위험한 배포 작업이나 운영 서버 변경은 Human Confirmation 없이는 실행하지 않는다.

DevOps Agent 기본 Flow:

```text
PM Agent Handoff
→ DevOps Agent
→ Environment Analysis
→ Docker / Deploy Plan
→ Risk Check
→ Rollback Plan
→ Human Approval if Needed
→ Structured DevOps Output
```

---

### [핵심]

- DevOps Agent는 실행 환경과 배포 구조를 담당한다.
- Docker 설정을 검토한다.
- Linux / Ubuntu Server 기준을 검토한다.
- CI/CD Pipeline을 설계한다.
- 환경 변수와 Secret 관리 기준을 제시한다.
- 배포 위험과 Rollback 기준을 포함한다.
- 운영 서버 변경은 위험 작업이다.
- 배포 실행은 Human Confirmation 대상이다.
- DB 변경과 삭제 작업은 자동 실행하지 않는다.

---

### [실무]

DevOps Agent Definition:

```md
## Agent Definition

### Name

DevOps Agent

### Role

Docker, Linux, CI/CD, Deploy Plan, Operations Risk 설계 담당 Specialist Agent

### Responsibility

- Dockerfile / docker-compose 검토
- Ubuntu Server 환경 기준 제시
- CI/CD Pipeline 설계
- Environment Variable 관리 기준 제시
- Secret 관리 기준 제시
- Deploy Step 설계
- Rollback Plan 작성
- Operational Risk 검토

### Scope

- Docker
- Linux / Ubuntu Server
- CI/CD
- Deployment Strategy
- Monitoring / Logging 기본 기준
- Environment Configuration

### Out of Scope

- Business Logic 구현
- Frontend UI 구현
- DB 직접 변경
- 사용자 승인 없는 배포 실행
- 사용자 승인 없는 파일 삭제

### Input

- PM Agent Task
- Project Environment
- Deployment Requirement
- Existing Config Context
- Domain Rules
- Relevant RAG Context

### Output

- DevOps Plan
- Configuration Review
- Deploy Steps
- Environment Variables
- Risks
- Rollback Plan
- Approval Required Actions

### Tool Permission

- RAG Search
- File Read
- Log Read
- Deploy Request with Approval

### RAG Scope

- Git GitHub
- Docker
- Linux Ubuntu Server
- CI/CD
- Deployment Strategy
- Monitoring Logging

### Done Criteria

- 실행 환경 기준 포함
- 설정 파일 검토 기준 포함
- 배포 절차 포함
- 위험 작업 표시
- Rollback 기준 포함
- 사용자 승인 필요 작업 분리
```

DevOps Agent Output 예시:

```md
## DevOps Agent Output

### Task

AnythingLLM + Ollama 기반 Agent 서버 Docker 운영 계획

### Environment

- Ubuntu Server
- Docker
- Ollama Host
- AnythingLLM Container

### Deploy Steps

- Docker network 확인
- Volume mount 확인
- Ollama endpoint 확인
- AnythingLLM container restart

### Environment Variables

- OLLAMA_BASE_URL
- STORAGE_DIR
- JWT_SECRET

### Risks

- Volume 권한 문제
- Ollama host.docker.internal 연결 실패
- Model memory 부족

### Rollback Plan

- 기존 container image tag 보존
- 기존 volume 삭제 금지
- 설정 변경 전 backup 생성

### Approval Required

- Volume 삭제
- Production container 재생성
- DB migration 실행
```

---

### [FAQ]

Q. DevOps Agent는 뭐 하는 Agent야?
A. Docker, Linux, CI/CD, 배포 절차, 운영 위험을 설계하고 검토하는 Specialist Agent다.

Q. DevOps Agent가 배포를 자동 실행해도 돼?
A. 안 된다. 배포, 삭제, 운영 서버 변경은 사용자 승인 후 실행해야 한다.

Q. DevOps Agent Output에는 뭐가 있어야 해?
A. DevOps Plan, Configuration Review, Deploy Steps, Risks, Rollback Plan, Approval Required Actions가 있어야 한다.

Q. DevOps Agent의 주요 RAG Scope는?
A. Git GitHub, Docker, Linux Ubuntu Server, CI/CD, Deployment Strategy, Monitoring Logging이다.

---

# 7. AI Agent

## 7.1 AI Agent Definition

### [개념]

AI Agent는 RAG, Prompt Engineering, Tool Calling, Agent Workflow, LLM API Integration, Agent 시스템 고도화를 담당하는 Specialist Agent이다.

AI Agent는 개인 AI 개발팀의 Agent 구조, RAG 검색 전략, Tool 사용 흐름, Prompt 구조를 개선한다.

AI Agent 기본 Flow:

```text
PM Agent Handoff
→ AI Agent
→ AI Workflow Analysis
→ RAG / Prompt / Tool Design
→ Agent System Improvement
→ Evaluation Criteria
→ Structured AI Output
```

---

### [핵심]

- AI Agent는 AI Workflow 설계를 담당한다.
- RAG 검색 전략을 설계한다.
- Prompt 구조를 개선한다.
- Tool Calling 흐름을 설계한다.
- Agent Workflow를 개선한다.
- LLM API Integration 기준을 제시한다.
- Agent Evaluation 기준을 제안한다.
- Backend / Frontend 구현을 직접 대체하지 않는다.
- 모델 Fine-Tuning은 별도 Expert Scope로 분리할 수 있다.

---

### [실무]

AI Agent Definition:

```md
## Agent Definition

### Name

AI Agent

### Role

RAG, Prompt, Tool Calling, Agent Workflow 설계 담당 Specialist Agent

### Responsibility

- RAG Workflow 설계
- Retrieval Query 설계
- Prompt Template 설계
- Tool Calling Flow 설계
- Agent Workflow 개선
- Context Management 기준 제시
- Agent Evaluation 기준 제안
- LLM API Integration 기준 제시

### Scope

- Prompt Engineering
- RAG
- Embedding / Semantic Search
- Vector Database
- Tool Calling
- Agent Workflow
- Context Management
- Evaluation Criteria

### Out of Scope

- 일반 Backend API 구현
- Frontend UI 구현
- Docker 배포 실행
- 운영 DB 직접 변경
- Fine-Tuning 실험 자동 실행

### Input

- PM Agent Task
- Current Agent Workflow
- RAG Document Context
- Tool Requirement
- Domain Rules
- Relevant AI RAG Context

### Output

- AI Workflow Design
- Prompt Structure
- Retrieval Strategy
- Tool Calling Plan
- Context Management Rule
- Evaluation Criteria
- Risks
- Assumptions

### Tool Permission

- RAG Search
- Prompt Read
- Workflow Config Read

### RAG Scope

- Prompt Engineering
- LLM Core API Integration
- Embedding Model Semantic Search
- Vector Database RAG
- RAG Evaluation Retrieval Optimization
- LangChain LangGraph
- Tool Calling Function Calling
- Agent Workflow Design
- Multi-Agent System

### Done Criteria

- Workflow 구조 명확
- Prompt / RAG / Tool 역할 분리
- Retrieval Strategy 포함
- Evaluation 기준 포함
- Risk와 Assumption 포함
- Review 가능한 Output 생성
```

AI Agent Output 예시:

```md
## AI Agent Output

### Task

PM Agent 중심 RAG 검색 전략 설계

### Retrieval Strategy

- PM Agent가 Domain을 먼저 분류
- Specialist Agent별 RAG Scope 제한
- Review Agent는 Master Rules + Domain Rules 우선 검색
- Missing Context 발생 시 Scope 확장

### Prompt Structure

- Role
- Responsibility
- Input
- Output Format
- Constraints
- Failure Handling

### Tool Calling Plan

- Read Tool 우선
- Write Tool 제한
- Dangerous Tool은 Human Confirmation 필요

### Evaluation Criteria

- Routing Accuracy
- Retrieval Relevance
- Handoff Quality
- Review Pass Rate

### Risks

- RAG Scope가 너무 좁으면 문서 누락 가능
- Scope가 너무 넓으면 관련 없는 Context 증가
```

---

### [FAQ]

Q. AI Agent는 뭐 하는 Agent야?
A. RAG, Prompt Engineering, Tool Calling, Agent Workflow, LLM API Integration을 설계하고 개선하는 Specialist Agent다.

Q. AI Agent가 Backend 코드를 직접 구현해?
A. 원칙적으로 아니다. Backend 구현은 Backend Agent가 담당한다.

Q. AI Agent Output에는 뭐가 있어야 해?
A. AI Workflow Design, Prompt Structure, Retrieval Strategy, Tool Calling Plan, Evaluation Criteria, Risks가 있어야 한다.

Q. AI Agent의 주요 RAG Scope는?
A. Prompt Engineering, RAG, Semantic Search, LangGraph, Tool Calling, Agent Workflow, Multi-Agent System이다.

---

# 8. Documentation Agent

## 8.1 Documentation Agent Definition

### [개념]

Documentation Agent는 RAG 문서 제작, 문서 구조화, FAQ 강화, Retrieval Queries 작성, 문서 검수를 담당하는 Specialist Agent이다.

Documentation Agent는 사람용 학습 문서보다 AI Agent Retrieval에 최적화된 Markdown 문서를 만든다.

Documentation Agent 기본 Flow:

```text
PM Agent Handoff
→ Documentation Agent
→ Master Rules Load
→ Domain Rules Load
→ Document Draft
→ Retrieval Optimization
→ Quality Check
→ Structured RAG Document
```

---

### [핵심]

- Documentation Agent는 RAG 문서 제작을 담당한다.
- MASTER_RAG_RULES를 우선 적용한다.
- DOMAIN_RULES를 적용한다.
- PROJECT_PROGRESS를 참고한다.
- 사람용 장문 문서보다 Retrieval 최적화를 우선한다.
- `[개념]`, `[핵심]`, `[실무]`, `[FAQ]` 구조를 유지한다.
- Retrieval Queries를 반드시 포함한다.
- FAQ를 강화한다.
- 용어를 통일한다.
- 오타와 중복을 최소화한다.

---

### [실무]

Documentation Agent Definition:

```md
## Agent Definition

### Name

Documentation Agent

### Role

RAG 문서 제작 및 Retrieval 최적화 담당 Specialist Agent

### Responsibility

- RAG 문서 초안 작성
- Markdown 구조화
- Required Section 적용
- FAQ 작성
- Retrieval Queries 작성
- 용어 통일
- 중복 제거
- 문서 간 연계 확인
- 품질 체크리스트 적용

### Scope

- RAG Document
- Domain Document
- Agent Rules Document
- FAQ
- Retrieval Queries
- Markdown Structure

### Out of Scope

- 코드 실행
- 운영 서버 변경
- DB 변경
- 배포 실행
- 출처 없는 기술 사실 단정

### Input

- PM Agent Task
- Master Rules
- Domain Rules
- Project Progress
- Related Existing Documents
- Target Part Topic

### Output

- RAG-optimized Markdown Document
- Required Sections
- FAQ
- Retrieval Queries
- Consistent Naming
- Reviewable Document

### Tool Permission

- RAG Search
- File Read
- Document Read

### RAG Scope

- Master Rules
- Project Progress
- Target Domain Rules
- Related Domain Documents

### Done Criteria

- Required Section 포함
- FAQ 포함
- Retrieval Queries 포함
- 용어 통일
- 중복 최소화
- RAG Retrieval 최적화
- 치명적 구조 문제 없음
```

Documentation Agent Output 기준:

```text
# FileName
# Document Title
---
# 1. Main Section
## 1.1 Sub Section
### [개념]
### [핵심]
### [실무]
### [FAQ]
---
# Retrieval Queries
### [FAQ]
```

---

### [FAQ]

Q. Documentation Agent는 뭐 하는 Agent야?
A. RAG 문서 제작, 구조화, FAQ 강화, Retrieval Queries 작성, 문서 검수를 담당하는 Agent다.

Q. Documentation Agent는 사람용 문서를 만들어?
A. 아니다. AI Agent Retrieval에 최적화된 RAG 문서를 만든다.

Q. Documentation Agent가 반드시 적용해야 하는 규칙은?
A. MASTER_RAG_RULES, DOMAIN_RULES, PROJECT_PROGRESS 기준을 적용해야 한다.

Q. Documentation Agent Output에는 뭐가 있어야 해?
A. Required Sections, FAQ, Retrieval Queries, 통일된 용어, Review 가능한 Markdown 구조가 있어야 한다.

---

# 9. Specialist Agent Failure Handling

## 9.1 Common Specialist Agent Failure

### [개념]

Specialist Agent Failure는 Specialist Agent가 자기 Scope를 벗어나거나, Missing Context를 추측하거나, 잘못된 RAG Context를 사용하거나, 구조화되지 않은 Output을 반환할 때 발생한다.

주요 실패 유형:

```text
Scope Violation
Missing Context Hallucination
Wrong RAG Scope
Tool Permission Violation
Unstructured Output
Role Overlap
No Assumption
No Risk
No Done Criteria
```

---

### [핵심]

- Specialist Agent는 Scope 밖 작업을 하면 안 된다.
- Missing Context를 확정처럼 말하면 안 된다.
- RAG Scope가 잘못되면 부정확한 Context를 사용할 수 있다.
- Tool Permission을 넘는 작업을 실행하면 위험하다.
- Output이 구조화되지 않으면 PM Agent와 Review Agent가 사용하기 어렵다.
- Assumption과 Risk가 없으면 오류 전파 가능성이 커진다.
- Done Criteria가 없으면 완료 판단이 어렵다.

---

### [실무]

Failure Handling 기준:

| Failure Type              | Cause                        | Handling                        |
| ------------------------- | ---------------------------- | ------------------------------- |
| Scope Violation           | 다른 Domain 작업 처리        | PM Agent에게 반환               |
| Missing Context           | 필요한 정보 없음             | Assumption / Open Question 표시 |
| Critical Missing Context  | 작업 불가능한 핵심 정보 없음 | Failed Output 반환              |
| Wrong RAG Scope           | 잘못된 문서 검색             | RAG Scope 재설정 요청           |
| Tool Permission Violation | 권한 밖 Tool 필요            | Human Confirmation 또는 PM 반환 |
| Unstructured Output       | 결과 형식 없음               | Output Template 재적용          |
| Role Overlap              | 책임 충돌                    | PM Agent에게 결정 요청          |

Failure Output 예시:

```md
## Specialist Agent Failure Output

### Source Agent

Frontend Agent

### Status

Failed

### Failure Type

Missing Backend API Contract

### Reason

Review 목록 조회 API의 Response Field가 제공되지 않아 정확한 Component State 설계 불가

### Required Context

- GET /festivals/{festivalId}/reviews Response Body
- Pagination 방식
- Error Response Format

### Safe Alternative

일반적인 ReviewList Component 구조만 제안 가능

### Next Step

PM Agent가 Backend Agent Output을 확보한 뒤 Frontend Agent에 재전달
```

---

### [FAQ]

Q. Specialist Agent Failure는 언제 발생해?
A. Scope 위반, Missing Context 추측, 잘못된 RAG Scope, Tool 권한 위반, 비구조화 Output에서 발생한다.

Q. Missing Context가 있으면 Specialist Agent는 어떻게 해야 해?
A. Assumption 또는 Open Question으로 표시하고, 치명적이면 Failed Output을 반환해야 한다.

Q. Specialist Agent가 Scope 밖 작업을 요청받으면?
A. 직접 처리하지 않고 PM Agent에게 반환해야 한다.

Q. Tool Permission 밖 작업이 필요하면?
A. Human Confirmation 또는 PM Agent의 승인 절차가 필요하다.

---

## 9.2 Specialist Agent Checklist

### [개념]

Specialist Agent Checklist는 Specialist Agent가 작업 전후에 자기 역할, 입력, 출력, 위험을 검수하는 기준이다.

Checklist를 적용하면 Scope 위반, Missing Context 추측, Output 누락을 줄일 수 있다.

---

### [핵심]

- 작업 전 Handoff를 검토한다.
- Task가 자기 Scope인지 확인한다.
- Requirements와 Constraints를 확인한다.
- RAG Scope가 적절한지 확인한다.
- Tool Permission을 확인한다.
- Missing Context를 확인한다.
- Output 구조를 지킨다.
- Assumption과 Risk를 표시한다.
- Done Criteria를 충족했는지 확인한다.

---

### [실무]

Specialist Agent Pre-Execution Checklist:

```md
## Specialist Agent Pre-Execution Checklist

- [ ] Target Agent가 자신과 일치하는가?
- [ ] Task가 자기 Scope 안에 있는가?
- [ ] Requirements를 이해했는가?
- [ ] Constraints를 이해했는가?
- [ ] Required Context가 충분한가?
- [ ] Missing Context가 있는가?
- [ ] RAG Scope가 적절한가?
- [ ] Tool Permission이 충분한가?
- [ ] 위험 작업이 포함되어 있는가?
- [ ] Done Criteria가 명확한가?
```

Specialist Agent Final Checklist:

```md
## Specialist Agent Final Checklist

- [ ] Output이 구조화되어 있는가?
- [ ] Task Summary가 포함되었는가?
- [ ] Result가 명확한가?
- [ ] Decisions가 표시되었는가?
- [ ] Assumptions가 표시되었는가?
- [ ] Risks가 표시되었는가?
- [ ] Open Questions가 표시되었는가?
- [ ] Done Criteria를 충족했는가?
- [ ] Review Agent가 검토 가능한가?
- [ ] Scope 밖 내용을 확정처럼 작성하지 않았는가?
```

---

### [FAQ]

Q. Specialist Agent Checklist가 뭐야?
A. Specialist Agent가 작업 전후에 Scope, Input, Output, Risk를 검수하는 기준이다.

Q. Specialist Agent는 작업 전에 무엇을 확인해야 해?
A. Task Scope, Requirements, Constraints, RAG Scope, Tool Permission, Missing Context, Done Criteria를 확인해야 한다.

Q. Specialist Agent는 출력 전에 무엇을 확인해야 해?
A. Output 구조, Result, Decisions, Assumptions, Risks, Open Questions, Done Criteria 충족 여부를 확인해야 한다.

Q. Checklist가 필요한 이유는?
A. Scope 위반, Missing Context 추측, 비구조화 Output, Review 실패를 줄이기 위해서다.

---

# Retrieval Queries

### [FAQ]

Q. Specialist Agent가 뭐야?
A. SQL, Backend, Frontend, DevOps, AI처럼 특정 Domain 작업을 전문적으로 수행하는 Agent다.

Q. Specialist Agent의 핵심 역할은?
A. PM Agent Handoff를 기반으로 자기 Domain Rules와 RAG Scope 안에서 구조화된 Output을 생성하는 것이다.

Q. Specialist Agent는 모든 작업을 처리해도 돼?
A. 아니다. 자기 Responsibility와 Scope 안의 작업만 처리해야 한다.

Q. Specialist Agent는 누구에게 작업을 받아?
A. 보통 PM Agent가 생성한 Handoff를 통해 작업을 받는다.

Q. Specialist Agent 결과는 누가 검토해?
A. Review Agent가 요구사항, Domain Rules, 일관성, 위험 기준으로 검토한다.

Q. Specialist Agent Input Handling이 뭐야?
A. Specialist Agent가 PM Agent Handoff를 검토하고 작업에 필요한 요구사항, 제약, Context를 정리하는 단계다.

Q. Specialist Agent Output Handling이 뭐야?
A. Specialist Agent가 작업 결과를 다음 Agent가 사용할 수 있도록 구조화해 반환하는 단계다.

Q. Specialist Agent Output에는 뭐가 들어가야 해?
A. Task Summary, Result, Decisions, Assumptions, Risks, Open Questions, Next Step이 들어가야 한다.

Q. Specialist Agent가 실패하면 어떻게 출력해야 해?
A. Failure Reason, Required Context, Safe Alternative, Next Step을 포함한 Failed Output을 반환해야 한다.

Q. SQL Agent는 뭐 하는 Agent야?
A. Database Schema, SQL Query, Index, Data Consistency를 설계하는 Specialist Agent다.

Q. SQL Agent Output에는 뭐가 있어야 해?
A. Table Design, Relationship, Index Candidates, Query Pattern, Data Consistency Risks가 있어야 한다.

Q. Backend Agent는 뭐 하는 Agent야?
A. Spring Boot 기반 API, DTO, Service, Exception, Transaction, Security 기준을 설계하는 Specialist Agent다.

Q. Backend Agent Output에는 뭐가 있어야 해?
A. API Contract, DTO Design, Service Method Plan, Exception Cases, Security Rules, Risks가 있어야 한다.

Q. Frontend Agent는 뭐 하는 Agent야?
A. Frontend UI, Component, State, API Integration, Loading / Error UX를 설계하는 Specialist Agent다.

Q. Frontend Agent Output에는 뭐가 있어야 해?
A. Component Design, State Design, API Call Flow, Form Handling, Loading / Error UX, Risks가 있어야 한다.

Q. DevOps Agent는 뭐 하는 Agent야?
A. Docker, Linux, CI/CD, 배포 절차, 운영 위험을 설계하고 검토하는 Specialist Agent다.

Q. DevOps Agent가 배포를 자동 실행해도 돼?
A. 안 된다. 배포, 삭제, 운영 서버 변경은 사용자 승인 후 실행해야 한다.

Q. AI Agent는 뭐 하는 Agent야?
A. RAG, Prompt Engineering, Tool Calling, Agent Workflow, LLM API Integration을 설계하고 개선하는 Specialist Agent다.

Q. AI Agent의 주요 RAG Scope는?
A. Prompt Engineering, RAG, Semantic Search, LangGraph, Tool Calling, Agent Workflow, Multi-Agent System이다.

Q. Documentation Agent는 뭐 하는 Agent야?
A. RAG 문서 제작, 구조화, FAQ 강화, Retrieval Queries 작성, 문서 검수를 담당하는 Agent다.

Q. Documentation Agent는 사람용 문서를 만들어?
A. 아니다. AI Agent Retrieval에 최적화된 RAG 문서를 만든다.

Q. Specialist Agent Failure는 언제 발생해?
A. Scope 위반, Missing Context 추측, 잘못된 RAG Scope, Tool 권한 위반, 비구조화 Output에서 발생한다.

Q. Missing Context가 있으면 Specialist Agent는 어떻게 해야 해?
A. Assumption 또는 Open Question으로 표시하고, 치명적이면 Failed Output을 반환해야 한다.

Q. Specialist Agent가 Scope 밖 작업을 요청받으면?
A. 직접 처리하지 않고 PM Agent에게 반환해야 한다.

Q. Tool Permission 밖 작업이 필요하면?
A. Human Confirmation 또는 PM Agent의 승인 절차가 필요하다.

Q. Specialist Agent Checklist가 뭐야?
A. Specialist Agent가 작업 전후에 Scope, Input, Output, Risk를 검수하는 기준이다.

Q. Specialist Agent는 작업 전에 무엇을 확인해야 해?
A. Task Scope, Requirements, Constraints, RAG Scope, Tool Permission, Missing Context, Done Criteria를 확인해야 한다.

Q. Specialist Agent는 출력 전에 무엇을 확인해야 해?
A. Output 구조, Result, Decisions, Assumptions, Risks, Open Questions, Done Criteria 충족 여부를 확인해야 한다.

Q. Specialist Agent가 PM Agent와 다른 점은?
A. PM Agent는 조율과 통합을 담당하고, Specialist Agent는 특정 Domain 작업을 수행한다.

Q. Specialist Agent가 Review Agent와 다른 점은?
A. Specialist Agent는 Domain 산출물을 만들고, Review Agent는 산출물을 검증한다.

Q. 개인 AI 개발팀의 Specialist Agent 구성은?
A. SQL Agent, Backend Agent, Frontend Agent, DevOps Agent, AI Agent, Documentation Agent 등이 있다.
