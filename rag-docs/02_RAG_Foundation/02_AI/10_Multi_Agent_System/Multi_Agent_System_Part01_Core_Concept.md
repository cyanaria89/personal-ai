# Multi-Agent System Part01 - Core Concept

---

# 1. Multi-Agent System Core

## 1.1 Multi-Agent System Definition

### [개념]

Multi-Agent System은 여러 AI Agent가 역할을 나누어 하나의 목표를 수행하는 AI Workflow 구조이다.

단일 Agent가 모든 작업을 처리하는 방식이 아니라, PM Agent, Specialist Agent, Review Agent, Fix Agent처럼 책임을 분리한다.

Multi-Agent System의 핵심은 Agent 개수가 아니라 역할 분리, 책임 경계, Handoff 품질, Review-Fix Loop 안정성이다.

기본 구조:

```text
User Request
→ PM Agent
→ Specialist Agent
→ Review Agent
→ Fix Agent
→ Final Output
```

개인 AI 개발팀 기준 구조:

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

- Multi-Agent System은 여러 Agent가 협업하는 구조이다.
- 각 Agent는 명확한 Role, Responsibility, Input, Output을 가져야 한다.
- PM Agent는 전체 Workflow를 조율한다.
- Specialist Agent는 특정 Domain 작업을 수행한다.
- Review Agent는 산출물을 독립적으로 검증한다.
- Fix Agent는 Review 결과를 반영해 수정한다.
- Agent 간 정보 전달은 Handoff 형식으로 구조화해야 한다.
- Shared State는 요구사항, 결정사항, 중간 결과, Review 결과를 보존한다.
- 초기 로컬 LLM 환경에서는 Sequential Multi-Agent 구조가 가장 현실적이다.

---

### [실무]

2026년 실무 기준에서 Multi-Agent System은 복잡한 작업을 안정적으로 처리하기 위한 Workflow 설계 방식으로 사용된다.

실무 적용 목적:

- 요구사항 분석
- 작업 분해
- Domain별 전문 처리
- 코드 생성
- 코드 검토
- 오류 수정
- 문서 생성
- 운영 자동화
- RAG 기반 개발 보조
- Tool Calling 기반 작업 실행

개인 AI 서버에서는 처음부터 복잡한 병렬 Agent 구조보다 PM Agent 중심의 순차 실행 구조가 적합하다.

권장 시작 구조:

```text
User Request
→ PM Agent
→ Backend Agent
→ Review Agent
→ Final Output
```

확장 구조:

```text
User Request
→ PM Agent
→ SQL Agent
→ Backend Agent
→ Frontend Agent
→ DevOps Agent
→ AI Agent
→ Review Agent
→ Fix Agent
→ Final Output
```

---

### [FAQ]

Q. Multi-Agent System이 뭐야?
A. 여러 Agent가 역할을 나누어 하나의 목표를 수행하는 AI 시스템 구조다.

Q. Multi-Agent System의 핵심은 Agent 개수야?
A. 아니다. 핵심은 역할 분리, 책임 경계, Handoff 품질, Review-Fix 안정성이다.

Q. 개인 AI 개발팀에 Multi-Agent System이 필요한 이유는?
A. PM, Backend, Frontend, Review처럼 역할을 나누면 복잡한 개발 작업을 더 안정적으로 처리할 수 있기 때문이다.

Q. 로컬 LLM 환경에서도 Multi-Agent System이 가능해?
A. 가능하다. 다만 병렬 실행보다 순차 실행 구조가 현실적이다.

---

# 2. Single Agent vs Multi-Agent

## 2.1 Single Agent Limitation

### [개념]

Single Agent는 하나의 Agent가 모든 작업을 처리하는 구조이다.

단순 질문, 짧은 코드 생성, 간단한 문서 요약에는 적합하지만 복잡한 개발 Workflow에서는 한계가 있다.

Single Agent 구조:

```text
User Request
→ Single Agent
→ Final Output
```

한계:

- 요구사항 분석과 구현이 섞임
- Review 없이 결과가 바로 출력됨
- Domain별 전문성이 약해짐
- 긴 Context에서 핵심 제약이 누락될 수 있음
- 복잡한 작업의 중간 상태 관리가 어려움
- 실패 원인 추적이 어려움

---

### [핵심]

- Single Agent는 단순 작업에 적합하다.
- Single Agent는 빠르고 구조가 단순하다.
- 복잡한 개발 작업에서는 책임이 과도하게 집중된다.
- 설계, 구현, 검토, 수정이 한 Agent 안에서 섞인다.
- Review Agent가 없으면 품질 검증이 약하다.
- Shared State가 없으면 작업 흐름 추적이 어렵다.
- Tool 권한이 넓으면 위험 작업 통제가 어렵다.

---

### [실무]

실무에서 Single Agent는 아래 작업에 적합하다.

적합한 작업:

- 개념 설명
- 짧은 코드 예제 생성
- 단일 함수 수정
- 간단한 오류 원인 분석
- 짧은 문서 요약
- 단순 질의응답

부적합한 작업:

- 전체 기능 설계
- DB / Backend / Frontend 연동 개발
- 배포 Workflow 설계
- 보안 검토
- 다단계 코드 수정
- Review-Fix Loop가 필요한 작업
- Tool Calling이 포함된 위험 작업
- 장기 프로젝트 상태 관리

---

### [FAQ]

Q. Single Agent는 언제 쓰면 좋아?
A. 단순 질문, 짧은 코드 생성, 간단한 오류 분석처럼 범위가 작은 작업에 적합하다.

Q. Single Agent의 가장 큰 한계는?
A. 설계, 구현, 검토, 수정이 한 Agent 안에 섞여 품질과 추적성이 떨어질 수 있다는 점이다.

Q. Single Agent로도 개발 보조가 가능해?
A. 가능하다. 다만 복잡한 개발 Workflow에서는 Multi-Agent 구조가 더 안정적이다.

Q. Single Agent가 항상 나쁜 구조야?
A. 아니다. 작업이 작고 단순하면 Single Agent가 더 빠르고 효율적이다.

---

## 2.2 Multi-Agent Advantage

### [개념]

Multi-Agent는 작업을 여러 Agent에게 분배하여 처리하는 구조이다.

각 Agent는 자기 책임 범위 안에서 작업하고, PM Agent가 전체 흐름을 조율한다.

Multi-Agent 구조:

```text
User Request
→ PM Agent
→ Specialist Agent
→ Review Agent
→ Fix Agent
→ Final Output
```

장점:

- 작업 분해 가능
- Domain별 전문성 강화
- Review-Fix Loop 구성 가능
- Agent별 RAG Scope 제한 가능
- Agent별 Tool Permission 제한 가능
- Shared State 기반 진행 상황 관리 가능
- 실패 지점 추적 가능

---

### [핵심]

- Multi-Agent는 복잡한 작업을 분해한다.
- PM Agent가 작업을 분석하고 라우팅한다.
- Specialist Agent가 Domain 작업을 수행한다.
- Review Agent가 요구사항과 품질 기준을 검증한다.
- Fix Agent가 Review 결과를 반영한다.
- Agent별 RAG Scope를 제한하면 검색 정확도가 올라간다.
- Agent별 Tool Permission을 제한하면 위험이 줄어든다.
- Shared State를 사용하면 Agent 간 일관성이 유지된다.

---

### [실무]

실무형 Multi-Agent는 역할별 Output이 다음 Agent의 Input으로 이어져야 한다.

예시 Workflow:

```text
User Request
→ PM Agent: 요구사항 분석, 작업 분해
→ SQL Agent: Schema / Query 설계
→ Backend Agent: API / Service / DTO 설계
→ Frontend Agent: UI / State / API 연동 설계
→ Review Agent: 요구사항 / 일관성 / 위험 검토
→ Fix Agent: Review 결과 반영
→ PM Agent: 최종 통합
→ Final Output
```

실무 적용 시 주의:

- Agent가 많다고 항상 품질이 좋아지는 것은 아니다.
- Agent 수가 늘어나면 Latency, 비용, 복잡도가 증가한다.
- Handoff가 부정확하면 다음 Agent 결과도 부정확해진다.
- Review 기준이 없으면 Review Agent가 취향 기반 지적을 할 수 있다.
- Stop Condition이 없으면 Review-Fix Loop가 무한 반복될 수 있다.

---

### [FAQ]

Q. Multi-Agent의 장점은 뭐야?
A. 작업 분해, 전문성 강화, Review-Fix Loop, RAG Scope 제한, Tool Permission 제한이 가능하다는 점이다.

Q. Agent를 많이 만들면 무조건 좋아져?
A. 아니다. Agent가 많아질수록 복잡도, 비용, Latency가 증가한다.

Q. Multi-Agent에서 가장 중요한 Agent는 뭐야?
A. PM Agent다. PM Agent가 요구사항 분석, 작업 분해, 라우팅, 결과 통합을 담당하기 때문이다.

Q. Multi-Agent가 실패하는 주된 이유는?
A. 역할 경계 부족, Handoff 누락, Shared State 부재, Review 기준 부재, Stop Condition 부재 때문이다.

---

# 3. Core Agent Types

## 3.1 PM Agent

### [개념]

PM Agent는 Multi-Agent System의 중심 조율자이다.

PM Agent는 직접 구현보다 User Request를 분석하고 작업을 분해하며 적절한 Agent에게 전달하는 역할을 수행한다.

PM Agent Flow:

```text
User Request
→ Requirement Analysis
→ Task Decomposition
→ Agent Selection
→ Handoff
→ Result Integration
→ Final Output
```

---

### [핵심]

- PM Agent는 User Request를 분석한다.
- PM Agent는 요구사항과 제약을 정리한다.
- PM Agent는 작업을 작은 단위로 분해한다.
- PM Agent는 필요한 Specialist Agent를 선택한다.
- PM Agent는 Handoff를 생성한다.
- PM Agent는 Agent 결과를 통합한다.
- PM Agent는 최종 출력 품질에 책임을 가진다.
- PM Agent는 모든 구현을 직접 처리하지 않는다.

---

### [실무]

PM Agent는 개인 AI 개발팀에서 사용자가 직접 대화하는 대표 Agent로 사용한다.

권장 역할:

- 요구사항 분석
- 모호한 요구사항 정리
- 작업 우선순위 판단
- 필요한 Agent 선택
- RAG Scope 지정
- Handoff 생성
- 결과 통합
- 누락 사항 확인
- 최종 답변 생성

금지 역할:

- 모든 Domain 구현 직접 처리
- Specialist Agent 결과 검증 없이 합치기
- 불확실한 프로젝트 구조를 단정하기
- 사용자 승인 없이 위험 작업 실행하기

---

### [FAQ]

Q. PM Agent는 뭐 하는 Agent야?
A. 사용자 요청을 분석하고 작업을 분해하며, 적절한 Agent에게 전달하고 최종 결과를 통합하는 조율자다.

Q. PM Agent가 직접 코드를 작성해도 돼?
A. 간단한 작업은 가능하지만, Multi-Agent 구조에서는 구현보다 분석, 분해, 라우팅, 통합에 집중하는 것이 좋다.

Q. PM Agent가 중요한 이유는?
A. PM Agent의 작업 분해와 Handoff 품질이 전체 Agent 결과 품질을 결정하기 때문이다.

Q. 사용자는 어떤 Agent에게 요청해야 해?
A. 개인 AI 개발팀 구조에서는 사용자가 PM Agent에게만 요청하는 방식이 가장 단순하고 안정적이다.

---

## 3.2 Specialist Agent

### [개념]

Specialist Agent는 특정 Domain 작업을 전문적으로 수행하는 Agent이다.

예시:

- SQL Agent
- Backend Agent
- Frontend Agent
- DevOps Agent
- AI Agent
- Security Agent
- Testing Agent
- Documentation Agent

Specialist Agent Flow:

```text
Receive Handoff
→ Load Domain Rules
→ Retrieve RAG Context
→ Execute Domain Task
→ Return Structured Output
```

---

### [핵심]

- Specialist Agent는 자기 Domain 작업만 수행한다.
- Domain Rules와 RAG Context를 우선 적용한다.
- PM Agent가 전달한 요구사항과 제약을 따른다.
- Output은 다음 Agent가 사용할 수 있도록 구조화한다.
- 다른 Domain 변경이 필요하면 PM Agent에게 전달한다.
- 존재하지 않는 프로젝트 구조를 만들어내면 안 된다.
- 불확실한 부분은 Assumption 또는 Open Question으로 표시한다.

---

### [실무]

Specialist Agent는 RAG Scope를 제한해서 사용하는 것이 좋다.

예시:

| Agent          | RAG Scope                                             |
| -------------- | ----------------------------------------------------- |
| SQL Agent      | SQL, QueryDSL, JPA                                    |
| Backend Agent  | Java, Spring Boot, JPA, Security, API Design          |
| Frontend Agent | HTML, CSS, JavaScript, TypeScript, React              |
| DevOps Agent   | Git, Docker, Linux, CI/CD, Kubernetes                 |
| AI Agent       | Prompt Engineering, RAG, Tool Calling, Agent Workflow |
| Review Agent   | Master Rules, Domain Rules, Project Rules             |

Specialist Agent Output 예시:

```md
## Backend Agent Output

### Task

회원가입 API 설계

### Result

- Controller
- Service
- DTO
- Validation
- Exception

### Assumption

- User Entity가 존재한다고 가정

### Risk

- Email 중복 검증 방식 확인 필요
```

---

### [FAQ]

Q. Specialist Agent는 뭐야?
A. SQL, Backend, Frontend, DevOps, AI처럼 특정 Domain 작업을 전문적으로 수행하는 Agent다.

Q. Specialist Agent가 다른 Domain 작업도 해도 돼?
A. 원칙적으로 하지 않는 것이 좋다. 다른 Domain 변경이 필요하면 PM Agent에게 전달해야 한다.

Q. Specialist Agent에 RAG Scope 제한이 필요한 이유는?
A. 관련 없는 문서 검색을 줄이고 Domain 정확도를 높이기 위해서다.

Q. Specialist Agent 결과에는 뭐가 포함돼야 해?
A. 작업 결과, 근거, Assumption, Risk, 다음 Agent가 사용할 수 있는 구조화된 Output이 포함되어야 한다.

---

## 3.3 Review Agent

### [개념]

Review Agent는 다른 Agent가 만든 산출물을 독립적으로 검증하는 Agent이다.

Review Agent는 단순히 비판하는 Agent가 아니라 요구사항, Domain Rules, 일관성, 위험 요소를 기준으로 결과 품질을 확인한다.

Review Agent Flow:

```text
Specialist Output
→ Requirement Check
→ Domain Rules Check
→ Consistency Check
→ Risk Check
→ Findings
→ Pass / Fail
```

---

### [핵심]

- Review Agent는 독립적인 검증 담당이다.
- 요구사항 충족 여부를 확인한다.
- Domain Rules 위반 여부를 확인한다.
- Agent 결과 간 충돌을 확인한다.
- 위험 요소와 누락 사항을 찾는다.
- Severity 기준으로 문제 우선순위를 분류한다.
- Fix Agent가 바로 사용할 수 있는 수정 방향을 제공한다.
- 근거 없는 취향성 지적은 피해야 한다.

---

### [실무]

Review Agent는 Review Criteria가 명확해야 한다.

Review Criteria 예시:

```md
## Review Criteria

- Requirement Match
- Domain Rules Compliance
- API Contract Consistency
- Security Risk
- Data Consistency
- Error Handling
- Testability
- Maintainability
```

Review Output 예시:

```md
## Review Findings

### Critical

- 인증이 필요한 API에 Security 조건이 누락됨

### Major

- DTO Validation 기준이 불명확함

### Minor

- Method Naming Consistency 개선 가능

### Fix Direction

- SecurityConfig 접근 권한 추가
- Request DTO에 Validation Annotation 추가
```

---

### [FAQ]

Q. Review Agent는 왜 필요해?
A. 다른 Agent의 결과를 요구사항, Domain Rules, 일관성, 위험 기준으로 검증하기 위해 필요하다.

Q. Review Agent는 코드 스타일만 보는 Agent야?
A. 아니다. 요구사항 충족, 보안, API 계약, 데이터 일관성, 오류 처리까지 검토한다.

Q. Review Agent가 주의해야 할 점은?
A. 근거 없는 지적, 취향 기반 비판, 수정 방향 없는 비판을 피해야 한다.

Q. Review Agent 결과는 누가 사용해?
A. Fix Agent 또는 PM Agent가 Review 결과를 사용해 산출물을 수정하거나 최종 통합한다.

---

## 3.4 Fix Agent

### [개념]

Fix Agent는 Review Agent가 발견한 문제를 반영해 산출물을 수정하는 Agent이다.

Fix Agent는 새로운 요구사항을 만드는 Agent가 아니라 Review Findings 범위 안에서 기존 요구사항을 유지하며 수정한다.

Fix Agent Flow:

```text
Review Findings
→ Select Fix Scope
→ Apply Fix
→ Preserve Original Requirement
→ Return Updated Output
→ Re-review Request
```

---

### [핵심]

- Fix Agent는 Review 결과를 반영한다.
- 기존 요구사항을 유지해야 한다.
- Review 범위 밖의 큰 구조 변경은 피한다.
- 변경 내용과 변경 이유를 요약한다.
- Regression Risk를 표시한다.
- 수정 후 Re-review가 가능해야 한다.
- 기존 API 계약 변경 시 영향 범위를 표시한다.

---

### [실무]

Fix Agent는 수정 범위를 명확히 제한해야 한다.

Fix Output 예시:

```md
## Fix Result

### Applied Fix

- SecurityConfig에 인증 필요 경로 추가
- SignUpReqDto에 Validation Annotation 추가

### Preserved Requirement

- 기존 회원가입 Flow 유지
- 기존 Response Format 유지

### Regression Risk

- 기존 테스트에서 인증 없는 요청 실패 가능성 확인 필요

### Re-review Request

- Security Rule 적용 여부 재검토 필요
```

주의:

- Review에 없는 대규모 리팩터링 금지
- 기존 기능 삭제 금지
- 요구사항 임의 변경 금지
- API 계약 변경 시 PM Agent에게 보고

---

### [FAQ]

Q. Fix Agent는 뭐야?
A. Review Agent가 발견한 문제를 반영해 산출물을 수정하는 Agent다.

Q. Fix Agent가 새 요구사항을 추가해도 돼?
A. 안 된다. Fix Agent는 기존 요구사항과 Review Findings 범위 안에서 수정해야 한다.

Q. Fix Agent가 주의해야 할 점은?
A. Review 범위 밖의 큰 구조 변경, 기존 기능 삭제, API 계약 임의 변경을 피해야 한다.

Q. Fix 결과에는 뭐가 있어야 해?
A. Applied Fix, Preserved Requirement, Change Summary, Regression Risk, Re-review Request가 있어야 한다.

---

# 4. Multi-Agent Workflow Basics

## 4.1 Sequential Multi-Agent

### [개념]

Sequential Multi-Agent는 Agent를 순서대로 실행하는 구조이다.

각 Agent의 Output이 다음 Agent의 Input이 되며, 작업 의존성이 있는 개발 Workflow에 적합하다.

Sequential Flow:

```text
User Request
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

- 순차 실행은 구조가 단순하다.
- 각 단계의 결과를 다음 단계에서 사용할 수 있다.
- 작업 의존성이 있는 경우 안정적이다.
- 로컬 LLM 환경에서 현실적이다.
- 병렬 실행보다 충돌 관리가 쉽다.
- 단점은 Latency가 증가할 수 있다는 점이다.
- Agent 수가 많아지면 전체 처리 시간이 길어진다.

---

### [실무]

개인 AI 서버에서는 Sequential Multi-Agent 구조를 우선 사용한다.

적합한 이유:

- 로컬 LLM 리소스 제한
- RAM / VRAM 제약
- 모델 동시 실행 부담
- Agent 결과 통합 복잡도 감소
- 단계별 Review 가능
- 실패 지점 추적 용이

권장 초기 구조:

```text
User
→ PM Agent
→ Backend Agent
→ Review Agent
→ Final Output
```

권장 확장 구조:

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

### [FAQ]

Q. Sequential Multi-Agent가 뭐야?
A. Agent를 순서대로 실행하고 이전 Agent 결과를 다음 Agent가 사용하는 구조다.

Q. 로컬 LLM 환경에서는 왜 순차 실행이 좋아?
A. 모델 동시 실행 부담이 적고, 결과 충돌 관리가 쉬우며, 작업 흐름 추적이 쉽기 때문이다.

Q. 순차 실행의 단점은?
A. Agent가 많아질수록 전체 처리 시간이 길어진다.

Q. 개인 AI 개발팀 초기 구조로 적합해?
A. 적합하다. 처음에는 PM Agent, Specialist Agent, Review Agent 중심의 순차 구조가 안정적이다.

---

## 4.2 Parallel Multi-Agent

### [개념]

Parallel Multi-Agent는 여러 Agent를 동시에 실행하는 구조이다.

독립적인 작업을 빠르게 처리할 수 있지만 결과 통합과 충돌 관리가 필요하다.

Parallel Flow:

```text
User Request
→ PM Agent
→ SQL Agent + Backend Agent + Frontend Agent
→ Integration Agent
→ Review Agent
→ Final Output
```

---

### [핵심]

- 병렬 실행은 속도 개선이 가능하다.
- 독립 작업에 적합하다.
- 결과 통합 Agent가 필요하다.
- API 계약 충돌 가능성이 있다.
- Shared State 관리가 중요하다.
- 리소스 사용량이 증가한다.
- 로컬 LLM 환경에서는 부담이 클 수 있다.

---

### [실무]

Parallel Multi-Agent는 아래 조건에서 고려한다.

적합한 경우:

- 작업 간 의존성이 낮음
- Agent 결과가 독립적임
- 충분한 RAM / VRAM 확보
- 결과 통합 기준이 명확함
- Shared State가 안정적으로 관리됨
- Conflict Resolution 규칙이 있음

부적합한 경우:

- DB Schema가 먼저 정해져야 하는 Backend 작업
- API Contract가 먼저 필요한 Frontend 작업
- 인증 / 보안 정책이 여러 Domain에 영향을 주는 작업
- 로컬 LLM 리소스가 부족한 환경
- Integration Agent가 없는 구조

---

### [FAQ]

Q. Parallel Multi-Agent가 뭐야?
A. 여러 Agent를 동시에 실행해 독립 작업을 병렬 처리하는 구조다.

Q. 병렬 실행은 언제 좋아?
A. 작업 간 의존성이 낮고 결과 통합 기준이 명확할 때 좋다.

Q. 병렬 실행의 위험은?
A. Agent 결과 충돌, API 계약 불일치, 리소스 사용량 증가, 통합 복잡도 증가가 있다.

Q. 개인 로컬 LLM 서버에서 병렬 실행이 적합해?
A. 초기에는 적합하지 않다. 순차 실행으로 안정화한 뒤 확장하는 것이 좋다.

---

# 5. Handoff and Shared State Overview

## 5.1 Agent Handoff

### [개념]

Agent Handoff는 한 Agent가 다음 Agent에게 작업 정보를 전달하는 구조화된 메시지이다.

Handoff는 자연어 장문이 아니라 Task, Context, Constraints, Expected Output, Assumptions, Open Questions를 분리해서 전달해야 한다.

Handoff Template:

```json
{
  "from": "PM Agent",
  "to": "Backend Agent",
  "task": "Design signup API",
  "context": [],
  "constraints": [],
  "expectedOutput": "Markdown",
  "assumptions": [],
  "openQuestions": []
}
```

---

### [핵심]

- Handoff는 Agent 간 작업 전달 형식이다.
- Task와 Context를 분리해야 한다.
- Constraints를 명확히 전달해야 한다.
- Expected Output을 지정해야 한다.
- Assumption과 Open Question을 포함해야 한다.
- 다음 Agent가 바로 작업할 수 있어야 한다.
- Handoff가 부정확하면 다음 Agent 결과도 부정확해진다.

---

### [실무]

실무형 Handoff에는 최소한 아래 항목이 필요하다.

필수 항목:

- Source Agent
- Target Agent
- Task
- Background Context
- Requirements
- Constraints
- RAG Scope
- Tool Permission
- Expected Output
- Assumptions
- Open Questions
- Done Criteria

예시:

```json
{
  "from": "PM Agent",
  "to": "SQL Agent",
  "task": "Design tables for festival review feature",
  "requirements": [
    "User can write review for festival",
    "Rating range is 0 to 5",
    "One user can write multiple reviews"
  ],
  "constraints": ["Use MySQL", "Follow existing JPA naming convention"],
  "ragScope": ["SQL", "JPA Advanced", "API Design"],
  "expectedOutput": "Table design and risks",
  "doneCriteria": [
    "PK/FK defined",
    "Index candidates included",
    "Review risks included"
  ]
}
```

---

### [FAQ]

Q. Agent Handoff가 뭐야?
A. 한 Agent가 다음 Agent에게 작업, Context, 제약, 기대 출력 등을 구조화해서 전달하는 방식이다.

Q. Handoff가 중요한 이유는?
A. 다음 Agent가 필요한 정보를 정확히 받아야 결과 품질이 유지되기 때문이다.

Q. Handoff에 뭐가 들어가야 해?
A. Task, Context, Requirements, Constraints, RAG Scope, Expected Output, Assumptions, Open Questions, Done Criteria가 들어가야 한다.

Q. 자연어로 길게 전달하면 안 돼?
A. 장문 자연어만 사용하면 요구사항 누락과 해석 오류가 발생하기 쉽다.

---

## 5.2 Shared State

### [개념]

Shared State는 Multi-Agent Workflow에서 Agent들이 공통으로 참조하는 작업 상태이다.

Shared State는 현재 요청, 요구사항, 제약, 결정사항, Agent Output, Tool Result, Review Findings, Status를 관리한다.

Shared State Example:

```json
{
  "status": "in_progress",
  "currentStep": "backend_design",
  "userRequest": "",
  "requirements": [],
  "constraints": [],
  "decisions": [],
  "agentOutputs": {},
  "reviewFindings": [],
  "finalResult": null
}
```

---

### [핵심]

- Shared State는 현재 Workflow의 작업 상태이다.
- 요구사항과 결정사항을 보존한다.
- Agent 결과를 누적한다.
- Review-Fix Loop에서 기준점 역할을 한다.
- Agent 간 일관성을 유지한다.
- 오래된 State가 최신 요청을 덮어쓰면 안 된다.
- 모든 대화를 저장하면 Token 낭비가 커진다.
- 중요한 정보만 선별해 저장해야 한다.

---

### [실무]

Shared State는 Multi-Agent 개발 Workflow에서 API Contract, Schema Decision, Review Findings 관리에 유용하다.

예시:

```json
{
  "requirements": [
    "Festival review feature",
    "Authenticated user only",
    "Rating 0 to 5"
  ],
  "decisions": [
    "Use reviews table",
    "Use festival_id and user_id as FK",
    "Use Slice for review list"
  ],
  "agentOutputs": {
    "SQL Agent": "reviews table design",
    "Backend Agent": "Review API design"
  },
  "reviewFindings": ["Need duplicate review policy", "Need rating validation"],
  "status": "review_required"
}
```

주의:

- 현재 요청이 Memory보다 우선한다.
- 오래된 프로젝트 정보는 검증 후 사용한다.
- 민감정보 저장은 제한한다.
- Review 결과 반영 후 State를 갱신한다.

---

### [FAQ]

Q. Shared State가 뭐야?
A. Multi-Agent Workflow에서 요구사항, 결정사항, Agent 결과, Review 결과를 공통으로 관리하는 작업 상태다.

Q. Shared State와 Memory는 달라?
A. 다르다. Shared State는 현재 Workflow 상태이고, Memory는 장기 프로젝트 정보나 사용자 선호를 저장하는 구조다.

Q. Shared State가 필요한 이유는?
A. Agent 간 요구사항과 결정사항을 일관되게 유지하기 위해 필요하다.

Q. Shared State에 모든 대화를 저장해야 해?
A. 아니다. 중요한 요구사항, 결정사항, 결과, Review Findings만 선별해 저장해야 한다.

---

# 6. RAG Scope and Tool Permission Overview

## 6.1 Agent RAG Scope

### [개념]

Agent RAG Scope는 각 Agent가 검색할 수 있는 RAG 문서 범위이다.

Agent별로 필요한 Domain 문서만 검색하게 하면 관련 없는 Context를 줄이고 Retrieval 정확도를 높일 수 있다.

RAG Scope Example:

| Agent          | RAG Scope                                             |
| -------------- | ----------------------------------------------------- |
| PM Agent       | Master Rules, Project Progress, Agent Rules           |
| SQL Agent      | SQL, QueryDSL, JPA                                    |
| Backend Agent  | Java, Spring Boot, JPA, Security, API Design          |
| Frontend Agent | JavaScript, TypeScript, React, Data Fetching          |
| DevOps Agent   | Git, Docker, Linux, CI/CD                             |
| AI Agent       | Prompt Engineering, RAG, Tool Calling, Agent Workflow |
| Review Agent   | Master Rules, Domain Rules, Project Rules             |

---

### [핵심]

- RAG Scope는 Agent별 검색 범위이다.
- 필요한 문서만 검색하면 Retrieval 품질이 좋아진다.
- Scope가 너무 넓으면 관련 없는 Context가 섞인다.
- Scope가 너무 좁으면 필요한 문서가 누락된다.
- PM Agent가 작업별 RAG Scope를 지정할 수 있다.
- Review Agent는 Domain Rules와 산출물을 비교해야 한다.
- Metadata 품질이 RAG Scope 정확도에 영향을 준다.

---

### [실무]

실무에서는 Agent별 기본 RAG Scope와 작업별 추가 RAG Scope를 분리한다.

예시:

```json
{
  "agent": "Backend Agent",
  "defaultRagScope": ["Java", "Spring Boot", "JPA", "API Design"],
  "taskRagScope": ["Security Advanced", "Testing"]
}
```

검색 전략:

- PM Agent가 Domain을 판단한다.
- 기본 RAG Scope를 선택한다.
- 작업 특성에 따라 추가 Scope를 붙인다.
- 검색 결과가 부족하면 Scope를 확장한다.
- Review Agent가 Rule 위반 여부를 검토한다.

---

### [FAQ]

Q. Agent RAG Scope가 뭐야?
A. 각 Agent가 검색할 수 있는 RAG 문서 범위다.

Q. RAG Scope를 제한하는 이유는?
A. 관련 없는 Context를 줄이고 검색 정확도를 높이기 위해서다.

Q. RAG Scope가 너무 좁으면 어떻게 돼?
A. 필요한 문서가 검색되지 않아 Agent가 잘못된 결론을 낼 수 있다.

Q. RAG Scope는 누가 정해?
A. 기본 Scope는 Agent 설정에서 정하고, 작업별 Scope는 PM Agent가 조정할 수 있다.

---

## 6.2 Agent Tool Permission

### [개념]

Agent Tool Permission은 각 Agent가 사용할 수 있는 Tool 권한 범위이다.

Multi-Agent System에서는 모든 Agent에게 모든 Tool을 허용하면 위험하다.

Tool Permission은 Least Privilege 원칙에 따라 최소 권한으로 설계한다.

Tool Permission Example:

| Agent         | Tool Permission                        |
| ------------- | -------------------------------------- |
| PM Agent      | RAG Search, Routing                    |
| SQL Agent     | RAG Search, Schema Read                |
| Backend Agent | RAG Search, File Read, Code Search     |
| Review Agent  | RAG Search, Test Result Read           |
| Fix Agent     | File Write with Approval               |
| DevOps Agent  | Log Read, Deploy Request with Approval |

---

### [핵심]

- Agent별 Tool 권한은 제한해야 한다.
- 최소 권한 원칙을 적용한다.
- 읽기 Tool과 쓰기 Tool을 구분한다.
- 위험 Tool은 사용자 승인이 필요하다.
- 삭제, 배포, DB 변경은 자동 실행하면 위험하다.
- Tool 사용 결과는 기록 가능해야 한다.
- 권한이 넓을수록 사고 위험이 증가한다.

---

### [실무]

위험 작업은 Human-in-the-loop를 적용한다.

사용자 승인 필요 작업:

- 파일 삭제
- DB 변경
- 배포 실행
- 결제 처리
- 이메일 발송
- 외부 API 대량 호출
- 보안 설정 변경
- 운영 서버 변경
- 민감정보 접근

권장 정책:

```text
Read Tool → 자동 허용 가능
Write Tool → 제한적 허용
Dangerous Tool → 사용자 승인 필수
External Side Effect Tool → 사용자 승인 필수
Production Tool → Dry-run 우선
```

---

### [FAQ]

Q. Agent Tool Permission이 뭐야?
A. 각 Agent가 사용할 수 있는 Tool 권한 범위다.

Q. 모든 Agent에게 모든 Tool을 주면 안 돼?
A. 안 된다. 파일 삭제, DB 변경, 배포 같은 위험 작업을 잘못 실행할 수 있다.

Q. Tool Permission 설계 원칙은?
A. Least Privilege, 읽기/쓰기 구분, 위험 작업 승인, Tool 사용 기록이다.

Q. 사용자 승인이 필요한 Tool은 뭐야?
A. 삭제, 배포, DB 변경, 결제, 이메일 발송, 운영 서버 변경처럼 외부 영향이 있는 Tool이다.

---

# 7. Common Failure Cases

## 7.1 Role Overlap

### [개념]

Role Overlap은 여러 Agent의 책임이 겹쳐 같은 작업을 반복하거나 서로 다른 결론을 내는 문제이다.

예시:

```text
Backend Agent가 API Contract를 정함
Frontend Agent도 다른 API Contract를 정함
→ API 경로와 Request/Response 불일치 발생
```

---

### [핵심]

- Agent 책임이 모호하면 Role Overlap이 발생한다.
- Responsibility와 Scope를 분리해야 한다.
- PM Agent가 API Contract와 결정사항을 먼저 확정해야 한다.
- Shared State에 결정사항을 기록해야 한다.
- Review Agent가 Cross-domain Consistency를 확인해야 한다.

---

### [실무]

해결 방법:

```text
Agent Definition 작성
→ Responsibility / Scope 분리
→ PM Agent Routing 기준 작성
→ Shared State에 결정사항 기록
→ Review Agent가 충돌 검토
```

예시 기준:

| 작업              | 담당 Agent               |
| ----------------- | ------------------------ |
| API Contract 확정 | PM Agent + Backend Agent |
| DB Schema 설계    | SQL Agent                |
| Backend 구현      | Backend Agent            |
| Frontend 연동     | Frontend Agent           |
| 품질 검토         | Review Agent             |
| 수정 반영         | Fix Agent                |

---

### [FAQ]

Q. Agent 역할이 겹치면 어떤 문제가 생겨?
A. 같은 작업을 반복하거나 서로 다른 결론을 내서 결과 충돌이 발생할 수 있다.

Q. Role Overlap은 어떻게 줄여?
A. Agent별 Role, Responsibility, Scope, Input, Output, Done Criteria를 명확히 정의해야 한다.

Q. API Contract 충돌은 누가 막아야 해?
A. PM Agent가 계약을 확정하고 Review Agent가 Cross-domain Consistency를 검토해야 한다.

Q. Role Overlap이 생기면 Agent를 줄여야 해?
A. 필요하면 줄여야 한다. Agent 수보다 책임 경계가 더 중요하다.

---

## 7.2 Poor Handoff

### [개념]

Poor Handoff는 Agent 간 전달 정보가 부족하거나 모호해서 다음 Agent가 잘못된 결과를 생성하는 문제이다.

예시:

```text
PM Agent: 회원가입 만들어줘
Backend Agent: 어떤 인증 방식인지 모름
Review Agent: 요구사항 기준을 모름
→ 결과 품질 저하
```

---

### [핵심]

- Handoff가 모호하면 결과 품질이 낮아진다.
- Task, Context, Constraints를 분리해야 한다.
- Expected Output을 지정해야 한다.
- Assumption과 Open Question을 포함해야 한다.
- Done Criteria가 없으면 완료 기준이 흔들린다.
- 출처 없는 결정 사항 전달은 피해야 한다.

---

### [실무]

Poor Handoff 해결 Template:

```json
{
  "task": "Implement signup API",
  "requirements": [
    "Email signup",
    "Password validation",
    "Duplicate email check"
  ],
  "constraints": ["Spring Boot", "JPA", "ApiResponse format"],
  "expectedOutput": ["Controller", "Service", "DTO", "Exception cases"],
  "doneCriteria": [
    "Validation included",
    "Duplicate check included",
    "Error response included"
  ]
}
```

---

### [FAQ]

Q. Poor Handoff가 뭐야?
A. Agent 간 전달 정보가 부족하거나 모호해서 다음 Agent가 잘못된 결과를 내는 문제다.

Q. Handoff 품질을 높이려면?
A. Task, Context, Requirements, Constraints, Expected Output, Done Criteria를 분리해서 전달해야 한다.

Q. Done Criteria가 왜 필요해?
A. Agent가 작업 완료 기준을 명확히 알고 결과를 만들 수 있기 때문이다.

Q. Handoff에 Open Question이 필요한 이유는?
A. 불확실한 사항을 숨기지 않고 다음 Agent나 사용자에게 확인하기 위해서다.

---

## 7.3 Infinite Review-Fix Loop

### [개념]

Infinite Review-Fix Loop는 Review Agent와 Fix Agent가 끝없이 수정과 검토를 반복하는 문제이다.

원인:

- Stop Condition 없음
- Max Iteration 없음
- Severity 기준 없음
- Minor Issue를 계속 수정
- Review 기준이 반복마다 바뀜

---

### [핵심]

- Review-Fix Loop에는 종료 조건이 필요하다.
- Max Iteration을 설정해야 한다.
- Critical, Major, Minor를 구분해야 한다.
- Minor Issue는 보고 후 종료할 수 있다.
- Review 기준은 중간에 바뀌면 안 된다.
- Pass Criteria를 명확히 정의해야 한다.

---

### [실무]

권장 Review-Fix 정책:

```text
Max Iteration: 2
Critical: 반드시 수정
Major: 가능하면 수정
Minor: 보고 후 종료 가능
Pass Criteria: Critical 0개, Major 허용 기준 이하
```

Severity 기준:

| Severity | 의미                                | 처리              |
| -------- | ----------------------------------- | ----------------- |
| Critical | 요구사항 실패, 보안 위험, 실행 불가 | 반드시 수정       |
| Major    | 기능 품질 저하, 일관성 문제         | 수정 권장         |
| Minor    | 네이밍, 표현, 작은 개선             | 보고 후 종료 가능 |

---

### [FAQ]

Q. Review-Fix Loop가 무한 반복되는 이유는?
A. Stop Condition, Max Iteration, Severity 기준이 없기 때문이다.

Q. 무한 반복을 막으려면?
A. Max Iteration, Pass Criteria, Severity 기준을 설정해야 한다.

Q. Minor Issue도 계속 수정해야 해?
A. 아니다. Minor Issue는 보고 후 종료할 수 있다.

Q. Review 기준은 매번 바꿔도 돼?
A. 안 된다. 기준이 계속 바뀌면 Review-Fix Loop가 끝나지 않는다.

---

# 8. Best Practice

## 8.1 Initial Design Rules

### [개념]

Multi-Agent System은 처음부터 많은 Agent를 만드는 것보다 최소 구조로 시작해 점진적으로 확장하는 것이 안정적이다.

권장 초기 구조:

```text
User
→ PM Agent
→ Backend Agent
→ Review Agent
→ Final Output
```

권장 확장 구조:

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

- 처음부터 모든 Agent를 만들지 않는다.
- PM Agent 중심 구조로 시작한다.
- Specialist Agent는 필요한 Domain부터 추가한다.
- Review Agent는 초기에 포함하는 것이 좋다.
- Handoff Template을 먼저 만든다.
- Shared State 구조를 먼저 만든다.
- Tool Permission은 최소 권한으로 시작한다.
- RAG Scope는 Agent별로 제한한다.
- Review-Fix Loop에는 Max Iteration을 둔다.

---

### [실무]

개인 AI 개발팀 구축 순서:

```text
1. Master Rules 정리
2. Domain Rules 정리
3. PM Agent 정의
4. Backend Agent 정의
5. Review Agent 정의
6. Handoff Template 정의
7. Shared State Schema 정의
8. RAG Scope 설정
9. Tool Permission 설정
10. Sequential Workflow 테스트
11. SQL / Frontend / DevOps / AI Agent 확장
```

초기 성공 기준:

- PM Agent가 요구사항을 분해할 수 있음
- Specialist Agent가 Domain Rules를 참조함
- Review Agent가 요구사항과 Rules를 검토함
- Handoff 누락이 줄어듦
- Final Output이 사용자 관점에서 정리됨

---

### [FAQ]

Q. Multi-Agent System은 어떻게 시작하는 게 좋아?
A. PM Agent, Specialist Agent, Review Agent 중심의 최소 순차 구조로 시작하는 것이 좋다.

Q. 처음부터 SQL, Backend, Frontend, DevOps, AI Agent를 다 만들어야 해?
A. 아니다. 필요한 Agent부터 추가하는 것이 안정적이다.

Q. Review Agent는 초기에 필요해?
A. 가능하면 초기에 포함하는 것이 좋다. 품질 안정성과 오류 추적에 도움이 된다.

Q. Multi-Agent 구축에서 가장 먼저 정해야 할 것은?
A. Agent Role, Responsibility, Handoff Template, Shared State, RAG Scope다.

---

# Retrieval Queries

### [FAQ]

Q. Multi-Agent System이 뭐야?
A. 여러 Agent가 역할을 나누어 하나의 목표를 수행하는 AI Workflow 구조다.

Q. Multi-Agent System 핵심은 뭐야?
A. Agent 개수가 아니라 역할 분리, 책임 경계, Handoff 품질, Shared State, Review-Fix 안정성이다.

Q. Single Agent와 Multi-Agent 차이는?
A. Single Agent는 하나의 Agent가 모든 작업을 처리하고, Multi-Agent는 PM, Specialist, Review, Fix Agent가 역할을 나눠 처리한다.

Q. Single Agent는 언제 적합해?
A. 단순 질문, 짧은 코드 생성, 간단한 오류 분석처럼 범위가 작은 작업에 적합하다.

Q. Single Agent 한계는 뭐야?
A. 설계, 구현, 검토, 수정이 한 Agent 안에 섞여 품질과 추적성이 떨어질 수 있다.

Q. Multi-Agent 장점은 뭐야?
A. 작업 분해, Domain 전문성 강화, Review-Fix Loop, RAG Scope 제한, Tool Permission 제한이 가능하다.

Q. PM Agent는 뭐 하는 Agent야?
A. 사용자 요청을 분석하고 작업을 분해하며, 적절한 Agent에게 전달하고 최종 결과를 통합하는 조율자다.

Q. Specialist Agent는 뭐야?
A. SQL, Backend, Frontend, DevOps, AI처럼 특정 Domain 작업을 전문적으로 수행하는 Agent다.

Q. Review Agent는 왜 필요해?
A. Agent 산출물을 요구사항, Domain Rules, 일관성, 위험 기준으로 검증하기 위해 필요하다.

Q. Fix Agent는 뭐야?
A. Review Agent가 발견한 문제를 기존 요구사항 범위 안에서 수정하는 Agent다.

Q. Sequential Multi-Agent가 뭐야?
A. Agent를 순서대로 실행하고 이전 Agent 결과를 다음 Agent가 사용하는 구조다.

Q. 로컬 LLM 환경에서는 어떤 Multi-Agent 구조가 좋아?
A. 초기에는 순차 실행 구조가 현실적이다. 병렬 실행은 리소스와 결과 통합 부담이 크다.

Q. Parallel Multi-Agent가 뭐야?
A. 여러 Agent를 동시에 실행해 독립 작업을 병렬 처리하는 구조다.

Q. 병렬 Multi-Agent는 언제 적합해?
A. 작업 간 의존성이 낮고 결과 통합 기준이 명확하며 리소스가 충분할 때 적합하다.

Q. Agent Handoff가 뭐야?
A. 한 Agent가 다음 Agent에게 Task, Context, Constraints, Expected Output, Assumptions, Open Questions를 구조화해서 전달하는 방식이다.

Q. Handoff가 중요한 이유는?
A. 다음 Agent가 필요한 정보를 정확히 받아야 결과 품질이 유지되기 때문이다.

Q. Shared State가 뭐야?
A. Multi-Agent Workflow에서 요구사항, 결정사항, Agent 결과, Review 결과를 공통으로 관리하는 작업 상태다.

Q. Shared State와 Memory 차이는?
A. Shared State는 현재 Workflow 상태이고, Memory는 장기 프로젝트 정보나 사용자 선호를 저장하는 구조다.

Q. Agent RAG Scope가 뭐야?
A. 각 Agent가 검색할 수 있는 RAG 문서 범위다.

Q. Agent별 RAG Scope를 제한하는 이유는?
A. 관련 없는 Context를 줄이고 검색 정확도를 높이기 위해서다.

Q. Agent Tool Permission이 뭐야?
A. 각 Agent가 사용할 수 있는 Tool 권한 범위다.

Q. 모든 Agent에게 모든 Tool을 주면 안 되는 이유는?
A. 파일 삭제, DB 변경, 배포 같은 위험 작업을 잘못 실행할 수 있기 때문이다.

Q. Multi-Agent 실패 원인은 뭐야?
A. 역할 겹침, Poor Handoff, Shared State 부재, Review 기준 부재, Stop Condition 부재가 주요 원인이다.

Q. Role Overlap은 뭐야?
A. 여러 Agent의 책임이 겹쳐 같은 작업을 반복하거나 서로 다른 결론을 내는 문제다.

Q. Poor Handoff는 뭐야?
A. Agent 간 전달 정보가 부족하거나 모호해서 다음 Agent가 잘못된 결과를 내는 문제다.

Q. Review-Fix Loop가 무한 반복되면 어떻게 해?
A. Max Iteration, Stop Condition, Severity 기준, Pass Criteria를 설정해야 한다.

Q. 개인 AI 개발팀은 어떻게 시작해?
A. PM Agent, Specialist Agent, Review Agent 중심의 최소 순차 구조로 시작하고 필요한 Agent를 점진적으로 추가한다.

Q. 개인 AI 개발팀 기본 구조는?
A. User → PM Agent → SQL Agent → Backend Agent → Frontend Agent → Review Agent → Fix Agent → Final Output 구조다.

Q. Multi-Agent System에서 Review Agent를 초기에 넣어야 해?
A. 가능하면 초기에 넣는 것이 좋다. 산출물 품질 안정성과 오류 추적에 도움이 된다.

Q. Multi-Agent System에서 가장 먼저 정할 것은?
A. Agent Role, Responsibility, Handoff Template, Shared State, RAG Scope, Tool Permission이다.
