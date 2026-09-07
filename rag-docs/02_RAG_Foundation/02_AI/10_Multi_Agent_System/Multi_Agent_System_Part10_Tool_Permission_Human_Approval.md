# Multi-Agent System Part10 - Tool Permission and Human Approval

---

# 1. Tool Permission Core

## 1.1 Tool Permission Definition

### [개념]

Tool Permission은 Multi-Agent System에서 각 Agent가 사용할 수 있는 Tool의 권한 범위이다.

Tool Permission은 Agent가 어떤 Tool을 사용할 수 있는지, 어떤 Tool은 제한되는지, 어떤 Tool은 사용자 승인 후에만 가능한지 정의한다.

Tool Permission의 목적은 Agent가 자기 역할에 필요한 Tool만 사용하게 하고, 데이터 손상, 서비스 장애, 비용 발생, 보안 사고를 일으킬 수 있는 작업을 통제하는 것이다.

기본 구조:

```text
Agent Role
→ Allowed Tools
→ Restricted Tools
→ Approval Required Tools
→ Forbidden Tools
```

개인 AI 개발팀 기준:

```text
PM Agent
→ RAG Search / State Update / Routing

Specialist Agent
→ RAG Search / File Read / Code Search

Review Agent
→ RAG Search / File Read / Test Result Read

Fix Agent
→ File Write / Code Modify with Scope Control

DevOps Agent
→ Log Read / Config Read / Deploy Request with Approval
```

---

### [핵심]

- Tool Permission은 Agent별 Tool 사용 권한이다.
- 모든 Agent에게 모든 Tool을 허용하면 위험하다.
- 최소 권한 원칙을 적용한다.
- Agent Role과 Tool Permission은 일치해야 한다.
- Read Tool과 Write Tool을 분리한다.
- Dangerous Tool은 Human Approval 대상으로 분리한다.
- Tool 사용 전 Scope와 Permission을 확인한다.
- Tool 사용 후 Tool Result를 기록한다.
- Tool Failure를 숨기지 않는다.
- Tool Permission은 RAG Scope, Shared State, Workflow Pattern과 함께 관리한다.

---

### [실무]

2026 실무 기준에서 Tool Permission은 Agent Definition에 반드시 포함한다.

Tool Permission 기본 분류:

| 분류                   | 의미                                 | 예시                        |
| ---------------------- | ------------------------------------ | --------------------------- |
| Allowed Tool           | Agent가 바로 사용할 수 있는 Tool     | RAG Search, File Read       |
| Restricted Tool        | 조건부로 사용할 수 있는 Tool         | File Write, Code Modify     |
| Approval Required Tool | 사용자 승인 후 사용 가능한 Tool      | Deploy, DB Migration        |
| Forbidden Tool         | 해당 Agent가 사용하면 안 되는 Tool   | Review Agent의 직접 수정    |
| Dangerous Tool         | 외부 영향 또는 손상 위험이 있는 Tool | Delete, Payment, Email Send |

Agent별 권장 Tool Permission:

| Agent               | Allowed Tools                                         | Approval Required           |
| ------------------- | ----------------------------------------------------- | --------------------------- |
| PM Agent            | RAG Search, State Update, Routing, Handoff Generation | Dangerous Tool Request      |
| SQL Agent           | RAG Search, Schema Read, Query Read                   | DB Write, Migration         |
| Backend Agent       | RAG Search, File Read, Code Search                    | Code Modify, Config Write   |
| Frontend Agent      | RAG Search, File Read, Code Search                    | Code Modify                 |
| DevOps Agent        | RAG Search, Config Read, Log Read                     | Deploy, Restart, Delete     |
| AI Agent            | RAG Search, Prompt Read, Workflow Config Read         | Workflow Config Write       |
| Review Agent        | RAG Search, File Read, Test Result Read               | 직접 수정 금지              |
| Fix Agent           | RAG Search, File Read, Code Search                    | File Write, Code Modify     |
| Documentation Agent | RAG Search, Document Read, Document Write             | Existing Document Overwrite |

---

### [FAQ]

Q. Tool Permission이 뭐야?
A. Multi-Agent System에서 각 Agent가 사용할 수 있는 Tool의 권한 범위다.

Q. Tool Permission이 필요한 이유는?
A. Agent가 자기 역할에 맞는 Tool만 사용하게 하고 위험 작업을 통제하기 위해 필요하다.

Q. 모든 Agent에게 모든 Tool을 허용하면 안 돼?
A. 안 된다. 권한이 과도하면 삭제, 배포, DB 변경 같은 위험 작업을 잘못 실행할 수 있다.

Q. Tool Permission은 어디에 정의해?
A. Agent Definition의 Tool Permission 항목에 정의한다.

---

## 1.2 Least Privilege Principle

### [개념]

Least Privilege Principle은 Agent가 작업 수행에 필요한 최소 Tool 권한만 가져야 한다는 원칙이다.

Multi-Agent System에서 권한이 넓을수록 Agent가 Scope 밖 작업을 수행하거나 위험 Tool을 실행할 가능성이 커진다.

기본 구조:

```text
Task Requirement
→ Required Tool
→ Minimum Permission
→ Execute or Request Approval
```

---

### [핵심]

- 최소 권한 원칙은 Tool Permission의 기본이다.
- Agent는 자기 역할에 필요한 Tool만 사용한다.
- PM Agent는 위험 Tool을 직접 실행하지 않는다.
- Review Agent는 직접 수정하지 않는다.
- Fix Agent는 Review Findings 범위 안에서만 수정한다.
- DevOps Agent는 승인 없이 배포하지 않는다.
- SQL Agent는 승인 없이 DB Write를 하지 않는다.
- 권한이 넓으면 Role Overlap과 Tool Failure가 증가한다.
- 권한 부족은 Approval Request 또는 PM Agent 반환으로 처리한다.

---

### [실무]

최소 권한 적용 예시:

```json
{
  "agent": "Review Agent",
  "task": "Review backend API design",
  "requiredTools": ["RAG Search", "File Read", "Test Result Read"],
  "notRequiredTools": ["File Write", "Code Modify", "Deploy", "DB Write"],
  "permissionDecision": "read_only"
}
```

나쁜 권한 설정:

```json
{
  "agent": "Review Agent",
  "allowedTools": [
    "File Read",
    "File Write",
    "Code Modify",
    "Deploy",
    "DB Write"
  ]
}
```

문제:

- Review Agent가 Fix Agent 역할을 침범할 수 있다.
- 검토와 수정 추적이 분리되지 않는다.
- 승인 없는 위험 작업 가능성이 생긴다.
- Tool Result 추적이 어려워진다.

---

### [FAQ]

Q. 최소 권한 원칙이 뭐야?
A. Agent가 작업 수행에 필요한 최소 Tool 권한만 가져야 한다는 원칙이다.

Q. 최소 권한 원칙을 적용하는 이유는?
A. Role Overlap, 위험 Tool 실행, Tool Permission Failure를 줄이기 위해서다.

Q. Review Agent에게 Write 권한을 주면 안 돼?
A. 원칙적으로 주지 않는 것이 좋다. Review Agent는 검토하고 Fix Agent가 수정해야 한다.

Q. 권한이 부족하면 어떻게 해?
A. PM Agent에게 반환하거나 Human Approval이 필요한 작업으로 전환한다.

---

# 2. Tool Categories

## 2.1 Read Tool

### [개념]

Read Tool은 파일, 문서, 로그, DB Schema, Test Result, RAG Context처럼 정보를 조회하는 Tool이다.

Read Tool은 상대적으로 안전하지만, 민감정보나 운영 데이터가 포함될 수 있으므로 Scope 제한이 필요하다.

기본 구조:

```text
RAG Search
→ File Read
→ Code Search
→ Schema Read
→ Log Read
→ Test Result Read
```

---

### [핵심]

- Read Tool은 정보를 조회하는 Tool이다.
- 대부분의 Agent가 제한적으로 사용할 수 있다.
- Read Tool도 Scope 제한이 필요하다.
- 민감정보가 포함된 파일은 접근 제한이 필요하다.
- 운영 로그는 토큰, 이메일, IP, 에러 상세를 포함할 수 있다.
- `.env` 파일은 민감정보 가능성이 높다.
- DB Schema Read와 Data Read는 구분해야 한다.
- Read Tool 결과는 필요한 부분만 Context로 전달한다.
- Read Tool 결과도 Tool Result로 기록할 수 있다.

---

### [실무]

Read Tool 예시:

| Tool             | 설명               | 주요 Agent                     |
| ---------------- | ------------------ | ------------------------------ |
| RAG Search       | 문서 검색          | 모든 Agent                     |
| Document Read    | RAG 문서 읽기      | PM, Documentation, Review      |
| File Read        | 프로젝트 파일 읽기 | Backend, Frontend, Review, Fix |
| Code Search      | 코드 위치 검색     | Backend, Frontend, Review, Fix |
| Schema Read      | DB Schema 조회     | SQL, Backend, Review           |
| Log Read         | 로그 조회          | DevOps, Review                 |
| Test Result Read | 테스트 결과 조회   | Testing, Review, Fix           |
| Config Read      | 설정 조회          | DevOps, Backend, Review        |

Read Tool 사용 기준:

```text
필요 정보만 조회
→ 민감정보 포함 여부 확인
→ Target Agent Scope 확인
→ Context Packaging
→ Tool Result 기록
```

Read Tool 주의:

```text
.env 파일
→ 기본적으로 민감정보 가능

운영 로그
→ 사용자 정보와 토큰 포함 가능

DB Data Read
→ 실제 사용자 데이터 포함 가능

Config Read
→ Credential 또는 Secret 포함 가능
```

---

### [FAQ]

Q. Read Tool이 뭐야?
A. 파일, 문서, 로그, Schema, RAG Context처럼 정보를 조회하는 Tool이다.

Q. Read Tool은 항상 안전해?
A. 아니다. 민감정보나 운영 데이터가 포함될 수 있으므로 Scope 제한이 필요하다.

Q. RAG Search는 모든 Agent가 써도 돼?
A. 가능하지만 Agent별 RAG Scope를 제한해야 한다.

Q. Read Tool 결과는 어떻게 처리해?
A. 필요한 정보만 Context Packaging해서 Agent Input 또는 Shared State에 반영한다.

---

## 2.2 Write Tool

### [개념]

Write Tool은 파일, 코드, 문서, 설정, Shared State를 생성하거나 수정하는 Tool이다.

Write Tool은 시스템 상태를 변경하므로 Read Tool보다 엄격한 권한 관리가 필요하다.

기본 구조:

```text
File Write
→ Code Modify
→ Document Write
→ Config Write
→ State Update
```

---

### [핵심]

- Write Tool은 상태를 변경하는 Tool이다.
- Write Tool은 Agent별로 제한해야 한다.
- PM Agent는 State Update를 수행할 수 있다.
- Documentation Agent는 Document Write를 수행할 수 있다.
- Fix Agent는 Review Findings 범위 안에서 수정할 수 있다.
- Code Modify는 Fix Scope와 Approval 기준이 필요하다.
- Config Write는 위험도가 높다.
- Write 전 영향 범위를 확인해야 한다.
- Write 후 Review 또는 Test가 필요하다.

---

### [실무]

Write Tool 예시:

| Tool           | 설명              | 권장 Agent          | 주의                    |
| -------------- | ----------------- | ------------------- | ----------------------- |
| State Update   | Shared State 갱신 | PM Agent            | 최신 요청 우선          |
| Document Write | 문서 작성 / 수정  | Documentation Agent | 기존 문서 덮어쓰기 주의 |
| File Write     | 파일 생성 / 수정  | Fix, Documentation  | Scope 확인              |
| Code Modify    | 코드 수정         | Fix Agent           | Review Findings 기반    |
| Config Write   | 설정 파일 수정    | DevOps, Fix         | 승인 필요 가능          |
| Draft Create   | 초안 생성         | PM, Documentation   | 외부 발송 아님          |

Write Tool 사용 Flow:

```text
Write Request
→ Scope Check
→ Permission Check
→ Impact Check
→ Approval Check
→ Apply Write
→ Result Record
→ Review / Test
```

Write Tool Pre-check:

```md
## Write Tool Pre-check

- [ ] Target이 명확한가?
- [ ] 작업이 Agent Scope 안인가?
- [ ] 기존 요구사항을 훼손하지 않는가?
- [ ] Review Finding 또는 명확한 사용자 요청이 있는가?
- [ ] Approval이 필요한 작업인가?
- [ ] 변경 후 Review 또는 Test가 필요한가?
```

---

### [FAQ]

Q. Write Tool이 뭐야?
A. 파일, 코드, 문서, 설정, Shared State를 생성하거나 수정하는 Tool이다.

Q. Write Tool은 왜 제한해야 해?
A. 시스템 상태를 변경하므로 잘못 사용하면 데이터 손상, 코드 충돌, 설정 오류가 발생할 수 있기 때문이다.

Q. Code Modify는 언제 사용해?
A. 명확한 사용자 요청 또는 Review Findings를 반영할 때 사용한다.

Q. Write Tool 사용 후 필요한 것은?
A. Tool Result 기록, Change Summary, Review 또는 Test가 필요하다.

---

## 2.3 Dangerous Tool

### [개념]

Dangerous Tool은 잘못 실행하면 데이터 손상, 서비스 중단, 비용 발생, 보안 사고, 외부 영향이 발생할 수 있는 Tool이다.

Dangerous Tool은 기본적으로 자동 실행하지 않고 Human Approval 후 실행해야 한다.

기본 구조:

```text
Delete
→ DB Write
→ Migration
→ Deploy
→ Restart
→ Payment
→ Email Send
→ External Side Effect
```

---

### [핵심]

- Dangerous Tool은 자동 실행하면 안 된다.
- Human Approval이 필요하다.
- 실행 전 Action과 Target을 명확히 해야 한다.
- 영향 범위를 설명해야 한다.
- Risk를 설명해야 한다.
- Rollback Plan이 필요하다.
- Dry-run 또는 Preview를 우선한다.
- 승인 범위를 벗어난 작업을 실행하면 안 된다.
- 실행 후 Tool Result를 기록해야 한다.

---

### [실무]

Dangerous Tool 예시:

| Tool                     | 위험              | 승인 기준            |
| ------------------------ | ----------------- | -------------------- |
| File Delete              | 파일 손실         | 명시 승인            |
| Existing File Overwrite  | 기존 내용 손상    | 대상 확인            |
| DB Write                 | 데이터 변경       | 승인 + Backup 권장   |
| DB Migration             | Schema 변경       | 승인 + Rollback Plan |
| Deploy                   | 서비스 영향       | 승인 + Rollback Plan |
| Restart Service          | 서비스 중단       | 승인                 |
| Payment                  | 금전 영향         | 명시 승인            |
| Email Send               | 외부 발송         | 명시 승인            |
| Bulk External API Call   | 비용 / Rate Limit | 승인                 |
| Production Config Change | 운영 장애         | 승인 + Preview       |

Dangerous Tool Approval Template:

```md
## Approval Request

### Requested Action

Production backend deploy

### Target

backend production container

### Reason

New backend API change must be applied

### Expected Impact

Service may be temporarily unavailable

### Risks

- Running requests can fail
- Rollback may be required

### Rollback Plan

- Restore previous image tag
- Restart previous container

### Approval Required

Yes
```

---

### [FAQ]

Q. Dangerous Tool이 뭐야?
A. 잘못 실행하면 데이터 손상, 서비스 중단, 비용 발생, 보안 사고, 외부 영향이 발생할 수 있는 Tool이다.

Q. Dangerous Tool은 자동 실행해도 돼?
A. 안 된다. Human Approval 후 실행해야 한다.

Q. Dangerous Tool 사용 전 필요한 것은?
A. Action, Target, Impact, Risk, Rollback Plan, 사용자 승인이다.

Q. Dry-run은 왜 필요해?
A. 실제 변경 전에 예상 영향과 실행 결과를 확인해 사고를 줄이기 위해 필요하다.

---

# 3. Human Approval

## 3.1 Human Approval Definition

### [개념]

Human Approval은 Agent가 위험하거나 외부 영향이 있는 작업을 실행하기 전에 사용자 승인을 받는 절차이다.

Human Approval은 Tool Permission의 안전장치이다.

Human Approval은 Workflow Pattern 설명이 아니라 Tool 실행 통제 규칙이다.

기본 구조:

```text
Dangerous Action Detected
→ Approval Request
→ User Confirmation
→ Execute or Cancel
→ Tool Result Record
```

---

### [핵심]

- Human Approval은 위험 Tool 실행 전 승인 절차이다.
- 승인 없이 Dangerous Tool을 실행하면 안 된다.
- 파일 삭제는 승인 대상이다.
- 기존 파일 덮어쓰기는 승인 대상이 될 수 있다.
- DB Write와 Migration은 승인 대상이다.
- 운영 배포와 재시작은 승인 대상이다.
- 결제와 이메일 발송은 승인 대상이다.
- Approval Request에는 Action, Target, Impact, Risk, Rollback Plan이 포함되어야 한다.
- 승인 범위와 실행 범위가 일치해야 한다.

---

### [실무]

Human Approval Required Actions:

```text
File Delete
Existing File Overwrite
DB Write
DB Migration
Production Deploy
Service Restart
Payment Execution
Email Send
Bulk Message Send
External API Costly Call
Secret / Credential Change
Production Config Change
```

Approval Request Template:

```md
## Human Approval Request

### Action

DB Migration 실행

### Target

production database

### Reason

reviews table에 deleted_at column 추가 필요

### Expected Impact

Schema 변경 발생

### Risks

- Migration 실패 시 배포 중단 가능
- 기존 Query와 충돌 가능
- Rollback 필요 가능

### Rollback Plan

- Migration 전 Backup 생성
- 실패 시 이전 Schema로 Rollback

### Required Confirmation

사용자 승인 필요
```

Approval 처리 기준:

| User Response  | Action                      |
| -------------- | --------------------------- |
| 명확한 승인    | 승인 범위 안에서 실행       |
| 거절           | 실행 중단                   |
| 보류           | approval_required 상태 유지 |
| 조건부 승인    | 조건 반영 후 실행           |
| 모호한 응답    | 재확인                      |
| 승인 범위 초과 | 별도 승인 요청              |

---

### [FAQ]

Q. Human Approval이 뭐야?
A. 위험하거나 외부 영향이 있는 Tool을 실행하기 전에 사용자 승인을 받는 절차다.

Q. Human Approval은 Workflow Pattern이야?
A. 아니다. Tool 실행 통제를 위한 승인 규칙이다.

Q. Human Approval이 필요한 작업은?
A. 파일 삭제, DB 변경, 배포, 서비스 재시작, 결제, 이메일 발송, 운영 설정 변경이다.

Q. 승인 범위 밖 작업도 같이 실행해도 돼?
A. 안 된다. 승인된 Action과 Target 범위 안에서만 실행해야 한다.

---

## 3.2 Approval State

### [개념]

Approval State는 Human Approval이 필요한 작업의 승인 상태를 Shared State에 기록한 정보이다.

Approval State는 승인 대기, 승인 완료, 거절, 취소, 실행 완료, 실패를 구분한다.

기본 구조:

```text
approvalId
→ action
→ target
→ requestedBy
→ status
→ risk
→ decision
→ executionResult
```

---

### [핵심]

- Approval State는 승인 필요 작업의 상태이다.
- 승인 요청 대상 Action을 기록한다.
- Target을 기록한다.
- 요청 Agent를 기록한다.
- Risk와 Rollback Plan을 기록한다.
- 사용자 Decision을 기록한다.
- 실행 결과를 기록한다.
- 승인 없는 실행을 방지한다.
- 승인 상태는 최신이어야 한다.
- 오래된 승인을 새 작업에 재사용하면 안 된다.

---

### [실무]

Approval State Template:

```json
{
  "approvalId": "APP-001",
  "action": "Deploy backend service",
  "target": "production server",
  "requestedBy": "DevOps Agent",
  "status": "pending",
  "reason": "New backend API needs deployment",
  "risk": ["Temporary service interruption", "Rollback may be required"],
  "rollbackPlan": ["Restore previous image tag", "Restart previous container"],
  "userDecision": null,
  "executionResult": null
}
```

Approval Status:

| Status    | 의미              |
| --------- | ----------------- |
| pending   | 승인 대기         |
| approved  | 승인됨            |
| rejected  | 거절됨            |
| cancelled | 취소됨            |
| executed  | 실행 완료         |
| failed    | 승인 후 실행 실패 |
| expired   | 승인 만료         |

Approval State Update 예시:

```json
{
  "approvalId": "APP-001",
  "status": "approved",
  "userDecision": "approved",
  "approvedScope": {
    "action": "Deploy backend service",
    "target": "production server"
  },
  "nextStep": "execute_deploy"
}
```

---

### [FAQ]

Q. Approval State가 뭐야?
A. Human Approval이 필요한 작업의 승인 상태를 Shared State에 기록한 정보다.

Q. Approval State에는 뭐가 있어야 해?
A. approvalId, action, target, requestedBy, status, reason, risk, rollbackPlan, userDecision, executionResult가 있어야 한다.

Q. 승인 대기 상태에서는 실행해도 돼?
A. 안 된다. status가 approved가 되기 전에는 실행하지 않는다.

Q. 오래된 승인을 새 작업에 재사용해도 돼?
A. 안 된다. 승인은 특정 Action과 Target에 한정해야 한다.

---

# 4. Agent Tool Policy

## 4.1 PM Agent Tool Policy

### [개념]

PM Agent Tool Policy는 PM Agent가 사용할 수 있는 Tool과 제한 사항을 정의한 규칙이다.

PM Agent는 전체 조율자이므로 RAG Search, State Update, Routing, Handoff Generation, Result Integration 권한을 가진다.

PM Agent는 위험 Tool을 직접 실행하기보다 Approval Request를 생성하고 적절한 Agent에게 작업을 위임한다.

---

### [핵심]

- PM Agent는 RAG Search를 사용할 수 있다.
- PM Agent는 Shared State를 업데이트할 수 있다.
- PM Agent는 Routing과 Handoff를 수행한다.
- PM Agent는 Tool Permission을 판단한다.
- PM Agent는 Agent 결과를 통합한다.
- PM Agent는 위험 작업을 직접 실행하지 않는다.
- 위험 작업은 Approval Request로 전환한다.
- PM Agent는 Specialist Agent를 대체하지 않는다.
- PM Agent는 Tool Result를 최종 통합에 반영한다.

---

### [실무]

PM Agent Tool Permission:

```json
{
  "agent": "PM Agent",
  "allowedTools": [
    "RAG Search",
    "State Update",
    "Routing",
    "Handoff Generation",
    "Result Integration"
  ],
  "restrictedTools": ["File Write", "Code Modify", "DB Write", "Deploy"],
  "approvalRequiredTools": ["Dangerous Tool Request"],
  "forbiddenTools": ["Unauthorized Delete", "Unauthorized Production Change"]
}
```

PM Agent Tool 사용 기준:

```text
요청 분석
→ 필요한 Tool 판단
→ Agent별 Tool Permission 확인
→ 위험 작업이면 Approval Request
→ 안전 작업이면 Handoff
```

---

### [FAQ]

Q. PM Agent는 어떤 Tool을 사용할 수 있어?
A. RAG Search, State Update, Routing, Handoff Generation, Result Integration을 사용할 수 있다.

Q. PM Agent가 직접 배포를 실행해도 돼?
A. 안 된다. 배포는 DevOps Agent와 Human Approval을 통해 처리해야 한다.

Q. PM Agent가 Tool Permission을 판단해?
A. 그렇다. PM Agent는 작업에 필요한 Tool과 승인 필요 여부를 판단한다.

Q. PM Agent가 위험 작업을 발견하면?
A. Approval Request로 전환하고 사용자 승인 전에는 실행하지 않는다.

---

## 4.2 Specialist Agent Tool Policy

### [개념]

Specialist Agent Tool Policy는 SQL Agent, Backend Agent, Frontend Agent, DevOps Agent, AI Agent, Documentation Agent가 자기 Domain 작업을 수행할 때 사용할 Tool을 정의한 규칙이다.

Specialist Agent는 자기 Domain 작업에 필요한 Tool만 사용해야 하며, Scope 밖 Tool은 PM Agent 또는 Human Approval을 거쳐야 한다.

---

### [핵심]

- Specialist Agent는 자기 Domain에 필요한 Tool만 사용한다.
- SQL Agent는 Schema Read와 Query Read 중심이다.
- Backend Agent는 File Read, Code Search, RAG Search 중심이다.
- Frontend Agent는 File Read, Code Search, RAG Search 중심이다.
- DevOps Agent는 Config Read, Log Read 중심이다.
- AI Agent는 RAG Search, Prompt Read, Workflow Config Read 중심이다.
- Documentation Agent는 Document Read, Document Write 중심이다.
- DB Write, Deploy, Config Write는 승인 대상이다.
- Scope 밖 Tool 요청은 PM Agent에게 반환한다.

---

### [실무]

Specialist Agent Tool Permission Matrix:

| Agent               | Allowed Tools                                 | Approval Required                     |
| ------------------- | --------------------------------------------- | ------------------------------------- |
| SQL Agent           | RAG Search, Schema Read, Query Read           | DB Write, Migration                   |
| Backend Agent       | RAG Search, File Read, Code Search            | Code Modify, Config Write             |
| Frontend Agent      | RAG Search, File Read, Code Search            | Code Modify                           |
| DevOps Agent        | RAG Search, Config Read, Log Read             | Deploy, Restart, Delete, Config Write |
| AI Agent            | RAG Search, Prompt Read, Workflow Config Read | Workflow Config Write                 |
| Documentation Agent | RAG Search, Document Read, Document Write     | Existing Document Overwrite           |
| Testing Agent       | RAG Search, Test Read, Test Run               | Test Environment Reset                |
| Security Agent      | RAG Search, Config Read, Code Search          | Security Config Write                 |

Specialist Agent Permission Check:

```md
## Specialist Agent Permission Check

- [ ] Requested Tool이 Agent Scope 안인가?
- [ ] Tool이 Read Tool인가 Write Tool인가?
- [ ] Tool 사용이 외부 영향을 만드는가?
- [ ] Tool 사용이 기존 파일 / DB / 서비스 상태를 변경하는가?
- [ ] Approval이 필요한가?
- [ ] Tool Result를 기록할 수 있는가?
```

---

### [FAQ]

Q. Specialist Agent는 어떤 Tool을 사용할 수 있어?
A. 자기 Domain 작업에 필요한 RAG Search, File Read, Code Search, Schema Read 같은 Tool을 제한적으로 사용할 수 있다.

Q. Backend Agent가 Code Modify를 바로 해도 돼?
A. 명확한 사용자 요청이나 Review Finding이 있고 권한이 허용된 경우에만 가능하며 보통 Fix Agent가 담당한다.

Q. DevOps Agent가 배포를 바로 실행해도 돼?
A. 안 된다. 배포와 재시작은 Human Approval 대상이다.

Q. Documentation Agent는 Document Write를 사용할 수 있어?
A. 가능하다. 다만 기존 문서 덮어쓰기나 삭제는 승인 대상이 될 수 있다.

---

## 4.3 Review and Fix Tool Policy

### [개념]

Review Agent와 Fix Agent는 Tool Permission이 명확히 분리되어야 한다.

Review Agent는 검토와 읽기 중심 Tool을 사용한다.
Fix Agent는 Review Findings 범위 안에서 제한적 쓰기 Tool을 사용할 수 있다.

Review Agent가 직접 수정까지 수행하면 역할 경계가 흐려지고 수정 추적이 어려워진다.

---

### [핵심]

- Review Agent는 읽기 중심이다.
- Review Agent는 직접 수정하지 않는 것이 원칙이다.
- Review Agent는 RAG Search, File Read, Test Result Read를 사용할 수 있다.
- Fix Agent는 Review Findings 범위 안에서 수정한다.
- Fix Agent의 Write Tool은 Fix Scope로 제한한다.
- Fix Agent는 Minimal Fix 원칙을 따른다.
- Fix Agent는 Change Summary와 Regression Risk를 기록한다.
- Fix Agent가 위험 작업을 해야 하면 Human Approval이 필요하다.

---

### [실무]

Review Agent Tool Permission:

```json
{
  "agent": "Review Agent",
  "allowedTools": [
    "RAG Search",
    "File Read",
    "Code Search",
    "Test Result Read",
    "Log Read"
  ],
  "restrictedTools": [],
  "approvalRequiredTools": [],
  "forbiddenTools": [
    "File Write",
    "Code Modify",
    "Deploy",
    "DB Write",
    "Unauthorized Fix"
  ]
}
```

Fix Agent Tool Permission:

```json
{
  "agent": "Fix Agent",
  "allowedTools": ["RAG Search", "File Read", "Code Search"],
  "restrictedTools": ["File Write", "Code Modify", "Config Write"],
  "approvalRequiredTools": [
    "Existing File Overwrite",
    "Config Write",
    "DB Migration",
    "Deploy"
  ],
  "forbiddenTools": [
    "Unauthorized Delete",
    "Unapproved Production Change",
    "New Requirement Creation"
  ]
}
```

Review-Fix Tool Flow:

```text
Review Agent
→ Read / Analyze
→ Review Findings

Fix Agent
→ Read Target
→ Apply Fix within Scope
→ Change Summary
→ Regression Risk
→ Re-review Request
```

---

### [FAQ]

Q. Review Agent와 Fix Agent Tool Permission은 왜 분리해?
A. Review는 검토, Fix는 수정 역할이므로 권한을 분리해야 책임 경계와 안전성이 유지된다.

Q. Review Agent가 직접 파일을 수정해도 돼?
A. 원칙적으로 수정하지 않는다. 수정은 Fix Agent가 담당한다.

Q. Fix Agent가 Write Tool을 사용할 수 있어?
A. 가능하지만 Review Findings와 Fix Scope 안에서만 사용해야 하며 위험 작업은 승인 필요하다.

Q. Fix Agent가 수정 후 반드시 해야 할 것은?
A. Change Summary, Preserved Requirements, Regression Risk, Re-review Required를 기록해야 한다.

---

# 5. Permission Check

## 5.1 Permission Check Flow

### [개념]

Permission Check Flow는 Agent가 Tool을 사용하기 전에 Scope, 권한, 위험도, 승인 필요 여부를 확인하는 절차이다.

Permission Check Flow는 Tool 실행 전 안전 검문소 역할을 한다.

기본 구조:

```text
Tool Request
→ Agent Scope Check
→ Tool Permission Check
→ Risk Check
→ Approval Check
→ Execute or Block
```

---

### [핵심]

- Tool 사용 전 Permission Check를 수행한다.
- 요청 Tool이 Agent Scope 안인지 확인한다.
- Agent에게 해당 Tool 권한이 있는지 확인한다.
- Tool을 Read / Write / Dangerous로 분류한다.
- 외부 영향이 있는지 확인한다.
- 사용자 승인 필요 여부를 판단한다.
- 승인 전에는 Dangerous Tool을 실행하지 않는다.
- 권한이 없으면 PM Agent에게 반환한다.
- 실행 후 Tool Result를 기록한다.

---

### [실무]

Permission Check Template:

```json
{
  "agent": "DevOps Agent",
  "requestedTool": "Deploy",
  "task": "Deploy backend service",
  "scopeCheck": "in_scope",
  "permissionCheck": "approval_required",
  "riskLevel": "high",
  "externalImpact": true,
  "approvalRequired": true,
  "decision": "request_human_approval"
}
```

Permission Check Decision:

| Decision         | 의미               |
| ---------------- | ------------------ |
| allow            | 실행 가능          |
| allow_read_only  | 읽기만 허용        |
| require_approval | 사용자 승인 필요   |
| deny_scope       | Agent Scope 밖     |
| deny_permission  | Tool 권한 없음     |
| block_unsafe     | 위험 작업으로 차단 |
| return_to_pm     | PM Agent 판단 필요 |

Permission Check 예시:

```text
Backend Agent가 파일 읽기 요청
→ Scope 안
→ File Read 허용
→ allow

Backend Agent가 운영 DB Migration 요청
→ Scope 밖 또는 위험
→ require_approval / return_to_pm

DevOps Agent가 로그 읽기 요청
→ Scope 안
→ Log Read 허용
→ allow

DevOps Agent가 배포 요청
→ Scope 안
→ 위험 작업
→ require_approval
```

---

### [FAQ]

Q. Permission Check Flow가 뭐야?
A. Agent가 Tool 사용 전에 Scope, 권한, 위험도, 승인 필요 여부를 확인하는 절차다.

Q. Tool 사용 전 무엇을 확인해야 해?
A. Agent Scope, Tool Permission, Tool 위험도, 외부 영향, Human Approval 필요 여부를 확인해야 한다.

Q. 권한이 없으면 어떻게 해?
A. Tool 실행을 중단하고 PM Agent에게 반환하거나 Approval Request를 생성한다.

Q. 위험 Tool이면 어떻게 해?
A. 사용자 승인 전에는 실행하지 않는다.

---

## 5.2 Permission Decision Record

### [개념]

Permission Decision Record는 Tool 사용 허용, 차단, 승인 요청, PM Agent 반환 같은 결정을 기록하는 정보이다.

Permission Decision Record는 Tool Permission 판단의 추적성을 높이고 Review Agent가 권한 준수 여부를 검토할 수 있게 한다.

기본 구조:

```text
Requested Tool
→ Permission Check
→ Decision
→ Reason
→ Next Action
```

---

### [핵심]

- Tool 사용 결정은 기록할 수 있어야 한다.
- Decision과 Reason을 함께 저장한다.
- 위험 작업은 Approval State와 연결한다.
- 차단된 작업은 차단 이유를 기록한다.
- PM Agent 판단이 필요한 작업은 return_to_pm으로 표시한다.
- Permission Decision은 Tool Result와 다르다.
- Permission Decision은 실행 전 판단이다.
- Tool Result는 실행 후 결과이다.

---

### [실무]

Permission Decision Record Template:

```json
{
  "permissionDecisionId": "PERM-001",
  "agent": "Fix Agent",
  "requestedTool": "Code Modify",
  "target": "ReviewService.java",
  "task": "Apply Review Finding for owner check",
  "scopeCheck": "in_scope",
  "permissionCheck": "restricted_allowed",
  "riskLevel": "medium",
  "approvalRequired": false,
  "decision": "allow",
  "reason": "Code modification is within Review Finding and Fix Scope",
  "nextAction": "execute_code_modify"
}
```

Permission Block Record:

```json
{
  "permissionDecisionId": "PERM-002",
  "agent": "Review Agent",
  "requestedTool": "File Write",
  "target": "ReviewService.java",
  "task": "Directly fix reviewed code",
  "scopeCheck": "out_of_scope",
  "permissionCheck": "forbidden",
  "riskLevel": "medium",
  "approvalRequired": false,
  "decision": "deny_permission",
  "reason": "Review Agent cannot directly modify files",
  "nextAction": "create_review_finding_for_fix_agent"
}
```

---

### [FAQ]

Q. Permission Decision Record가 뭐야?
A. Tool 사용 허용, 차단, 승인 요청, PM Agent 반환 같은 결정을 기록하는 정보다.

Q. Permission Decision과 Tool Result는 같아?
A. 아니다. Permission Decision은 실행 전 판단이고 Tool Result는 실행 후 결과다.

Q. 차단된 Tool 요청도 기록해야 해?
A. 기록하는 것이 좋다. 반복 Permission Failure를 분석할 수 있기 때문이다.

Q. Review Agent가 File Write를 요청하면?
A. deny_permission으로 차단하고 Fix Agent에게 전달해야 한다.

---

# 6. Tool Result Management

## 6.1 Tool Result State

### [개념]

Tool Result State는 Agent가 Tool을 사용한 결과를 Shared State에 기록한 정보이다.

Tool Result State는 어떤 Tool이 어떤 입력으로 실행되었고, 어떤 결과를 반환했는지 추적하기 위해 사용한다.

기본 구조:

```text
toolCallId
→ agent
→ tool
→ inputSummary
→ status
→ resultSummary
→ risk
→ nextAction
```

---

### [핵심]

- Tool Result State는 Tool 사용 결과 기록이다.
- Tool Call ID를 기록한다.
- 사용 Agent를 기록한다.
- Tool 이름을 기록한다.
- 입력 요약을 기록한다.
- 실행 상태를 기록한다.
- 결과 요약을 기록한다.
- 위험 또는 실패를 기록한다.
- 다음 조치를 기록한다.
- 민감정보는 기록하지 않거나 마스킹한다.
- Tool Failure도 기록한다.

---

### [실무]

Tool Result State Template:

```json
{
  "toolCallId": "TOOL-001",
  "agent": "Backend Agent",
  "tool": "Code Search",
  "inputSummary": "Search ReviewController and ReviewService",
  "status": "completed",
  "resultSummary": [
    "ReviewController.java found",
    "ReviewService.java found",
    "ReviewReqDto.java found"
  ],
  "risk": [],
  "nextAction": "Read target files for API contract review"
}
```

Tool Failure Result:

```json
{
  "toolCallId": "TOOL-002",
  "agent": "DevOps Agent",
  "tool": "Log Read",
  "inputSummary": "Read backend container logs",
  "status": "failed",
  "failureReason": "Log file not accessible",
  "requiredPermission": "Log Read",
  "nextAction": "Request permission or ask user to provide logs"
}
```

Tool Result 기록 기준:

```text
중요 Tool 사용
→ 결과 요약 저장

위험 Tool 사용
→ 승인 상태 + 결과 저장

실패한 Tool 사용
→ Failure Reason 저장

민감정보 포함 Tool
→ 마스킹 또는 저장 제외
```

---

### [FAQ]

Q. Tool Result State가 뭐야?
A. Agent가 Tool을 사용한 결과를 Shared State에 기록한 정보다.

Q. Tool Result State에는 뭐가 있어야 해?
A. toolCallId, agent, tool, inputSummary, status, resultSummary, risk, nextAction이 있어야 한다.

Q. Tool 결과에 민감정보가 있으면?
A. 마스킹하거나 Shared State에 저장하지 않아야 한다.

Q. Tool Failure도 기록해야 해?
A. 해야 한다. 실패 원인과 필요한 권한 또는 다음 조치를 기록해야 한다.

---

## 6.2 Tool Failure Handling

### [개념]

Tool Failure Handling은 Tool 실행 실패, 권한 부족, 입력 오류, 외부 시스템 오류가 발생했을 때 Agent가 처리하는 방식이다.

Tool Failure를 숨기면 다음 Agent가 잘못된 결과를 기준으로 작업할 수 있다.

기본 구조:

```text
Tool Call
→ Failure
→ Classify Failure
→ Record Failure
→ Retry / Fallback / Ask Approval / Stop
```

---

### [핵심]

- Tool Failure는 숨기지 않는다.
- 실패 유형을 분류한다.
- Failure Reason을 기록한다.
- Required Permission을 표시한다.
- Retry 가능 여부를 판단한다.
- Fallback을 제안한다.
- 위험 작업이면 중단한다.
- PM Agent에게 Failure Message를 반환한다.
- Tool Failure가 있으면 결과를 확정처럼 말하지 않는다.

---

### [실무]

Tool Failure Type:

| Failure Type      | 원인             | 처리                    |
| ----------------- | ---------------- | ----------------------- |
| Permission Denied | 권한 부족        | Approval 또는 권한 요청 |
| Not Found         | 대상 없음        | Target 확인             |
| Invalid Input     | 입력 형식 오류   | Input 수정              |
| Timeout           | 시간 초과        | Retry 또는 범위 축소    |
| External Error    | 외부 시스템 문제 | 재시도 또는 중단        |
| Unsafe Action     | 위험 작업 감지   | Human Approval          |
| Partial Result    | 일부 결과만 획득 | Partial로 표시          |

Tool Failure Message:

```md
## Tool Failure Message

### Source Agent

DevOps Agent

### Tool

Log Read

### Status

Failed

### Failure Type

Permission Denied

### Reason

Container log path 접근 권한 없음

### Required Permission

Log Read permission

### Safe Alternative

사용자가 로그 일부를 제공하면 분석 가능

### Suggested Action

PM Agent가 사용자에게 로그 제공 또는 권한 승인을 요청
```

---

### [FAQ]

Q. Tool Failure Handling이 뭐야?
A. Tool 실행 실패, 권한 부족, 입력 오류, 외부 오류가 발생했을 때 처리하는 방식이다.

Q. Tool Failure를 숨기면 안 되는 이유는?
A. 다음 Agent가 잘못된 상태를 정상 결과로 오해할 수 있기 때문이다.

Q. Tool Failure에는 뭐가 있어야 해?
A. Tool, Status, Failure Type, Reason, Required Permission, Safe Alternative, Suggested Action이 있어야 한다.

Q. Tool Timeout이 발생하면?
A. 재시도하거나 작업 범위를 줄이고, 실패 상태를 기록해야 한다.

---

# 7. RAG Scope and Tool Permission

## 7.1 Relationship Between RAG Scope and Tool Permission

### [개념]

RAG Scope와 Tool Permission은 Agent가 어떤 정보를 조회하고 어떤 작업을 수행할 수 있는지를 함께 제한하는 안전 장치이다.

RAG Scope는 검색 가능한 문서 범위이다.
Tool Permission은 실행 가능한 Tool 범위이다.

기본 관계:

```text
RAG Scope
→ 어떤 지식을 참조할 수 있는가

Tool Permission
→ 어떤 행동을 실행할 수 있는가
```

---

### [핵심]

- RAG Scope는 지식 접근 범위이다.
- Tool Permission은 행동 권한 범위이다.
- 둘은 Agent Role과 일치해야 한다.
- RAG Scope가 넓으면 관련 없는 Context가 섞일 수 있다.
- Tool Permission이 넓으면 위험 작업 가능성이 커진다.
- Specialist Agent는 자기 Domain RAG와 Tool만 사용해야 한다.
- Review Agent는 기준 문서를 읽고 검토한다.
- Fix Agent는 수정 대상 Domain RAG와 Review Findings를 참조한다.
- RAG Scope와 Tool Permission이 불일치하면 Agent Output 품질이 떨어진다.

---

### [실무]

RAG Scope와 Tool Permission 매핑:

| Agent               | RAG Scope                                    | Tool Permission                   |
| ------------------- | -------------------------------------------- | --------------------------------- |
| SQL Agent           | SQL, JPA, QueryDSL                           | Schema Read, Query Read           |
| Backend Agent       | Java, Spring Boot, JPA, Security, API Design | File Read, Code Search            |
| Frontend Agent      | JavaScript, TypeScript, React, Data Fetching | File Read, Code Search            |
| DevOps Agent        | Git, Docker, Linux, CI/CD                    | Config Read, Log Read             |
| AI Agent            | Prompt, RAG, Tool Calling, Agent Workflow    | Prompt Read, Workflow Config Read |
| Review Agent        | Master Rules, Domain Rules, Related Output   | File Read, Test Result Read       |
| Fix Agent           | Review Finding Related Domain                | File Read, Code Modify with Scope |
| Documentation Agent | Master Rules, Target Domain Rules            | Document Read, Document Write     |

잘못된 매핑 예시:

```text
Frontend Agent
→ RAG Scope: Docker, SQL, Security, React 전체
→ Tool Permission: DB Write, Deploy

문제:
- Domain Scope 과도
- 위험 Tool 과다
- Agent Role과 불일치
```

---

### [FAQ]

Q. Tool Permission과 RAG Scope 차이는?
A. RAG Scope는 어떤 지식을 검색할 수 있는지이고, Tool Permission은 어떤 행동을 실행할 수 있는지이다.

Q. 둘 다 제한해야 하는 이유는?
A. 관련 없는 지식 사용과 위험한 행동 실행을 동시에 줄이기 위해서다.

Q. Specialist Agent는 어떤 RAG Scope와 Tool Permission을 가져야 해?
A. 자기 Domain에 필요한 RAG Scope와 Tool만 가져야 한다.

Q. Tool Permission과 RAG Scope가 Agent Role과 맞지 않으면?
A. Agent가 엉뚱한 Context를 사용하거나 위험 작업을 실행할 수 있다.

---

# 8. Permission Failure Handling

## 8.1 Permission Failure Cases

### [개념]

Permission Failure는 Agent가 허용되지 않은 Tool을 사용하려 하거나, 위험 작업을 승인 없이 실행하거나, Tool Permission과 Agent Scope가 불일치할 때 발생한다.

Permission Failure는 데이터 손상, 서비스 중단, 보안 사고로 이어질 수 있다.

주요 실패 유형:

```text
Unauthorized Tool Use
Scope Tool Mismatch
Dangerous Tool Without Approval
Hidden Tool Failure
Over-permissioned Agent
Missing Tool Result
Sensitive Data Exposure
```

---

### [핵심]

- 권한 없는 Tool 사용은 차단해야 한다.
- Agent Scope와 Tool Permission은 일치해야 한다.
- Dangerous Tool은 승인 없이 실행하면 안 된다.
- Tool Failure를 숨기면 안 된다.
- 과도한 권한은 사고 위험을 높인다.
- Tool Result 누락은 추적성을 떨어뜨린다.
- 민감정보 노출 위험을 확인해야 한다.
- Permission Failure는 PM Agent와 Review Agent가 검토해야 한다.

---

### [실무]

Permission Failure 대응 기준:

| Failure Type                    | Cause                    | Handling               |
| ------------------------------- | ------------------------ | ---------------------- |
| Unauthorized Tool Use           | 권한 없는 Tool 요청      | 실행 차단              |
| Scope Tool Mismatch             | Agent Role과 Tool 불일치 | PM Agent 반환          |
| Dangerous Tool Without Approval | 승인 없는 위험 작업      | 즉시 중단              |
| Hidden Tool Failure             | 실패 은폐                | Failure Message 작성   |
| Over-permissioned Agent         | 권한 과다                | Permission 축소        |
| Missing Tool Result             | 결과 기록 누락           | Tool Result State 추가 |
| Sensitive Data Exposure         | 민감정보 노출            | 마스킹 / 접근 제한     |

Permission Failure Output 예시:

```md
## Permission Failure

### Failure Type

Dangerous Tool Without Approval

### Issue

DevOps Agent가 사용자 승인 없이 Production Deploy를 실행하려 함

### Impact

서비스 중단 또는 장애가 발생할 수 있음

### Decision

Deploy 실행 차단

### Required Action

Human Approval Request 생성

### Re-review Required

Yes
```

---

### [FAQ]

Q. Permission Failure는 언제 발생해?
A. 권한 없는 Tool 사용, 승인 없는 위험 작업 실행, Agent Scope와 Tool Permission 불일치에서 발생한다.

Q. Dangerous Tool을 승인 없이 실행하려 하면?
A. 즉시 차단하고 Human Approval Request를 생성해야 한다.

Q. Over-permissioned Agent가 뭐야?
A. Agent 역할에 비해 너무 많은 Tool 권한을 가진 상태다.

Q. Permission Failure는 누가 검토해?
A. PM Agent와 Review Agent가 검토하고 Tool Permission을 수정해야 한다.

---

## 8.2 Approval Failure Cases

### [개념]

Approval Failure는 Human Approval이 필요한 작업을 승인 없이 실행하거나, 승인 범위와 다른 작업을 실행하거나, 승인 상태를 잘못 기록하는 문제이다.

Approval Failure는 Dangerous Tool Failure의 핵심 유형이다.

주요 실패 유형:

```text
No Approval
Ambiguous Approval
Approval Scope Mismatch
Stale Approval
Missing Impact Explanation
Missing Rollback Plan
Execution Result Missing
```

---

### [핵심]

- 승인 없이 위험 작업을 실행하면 안 된다.
- 모호한 승인은 실행 기준이 아니다.
- 승인 범위 밖 작업을 실행하면 안 된다.
- 오래된 승인을 새 작업에 재사용하면 안 된다.
- Impact와 Risk를 설명해야 한다.
- Rollback Plan을 제공해야 한다.
- 실행 결과를 기록해야 한다.
- 승인 실패는 PM Agent와 Review Agent가 검토해야 한다.

---

### [실무]

Approval Failure 예시:

```md
## Approval Failure

### Failure Type

Approval Scope Mismatch

### Issue

사용자는 backend container restart만 승인했지만 DevOps Agent가 DB Migration까지 실행하려 함

### Impact

승인 범위를 벗어난 DB 변경으로 데이터 손상 위험 발생

### Decision

DB Migration 실행 차단

### Fix Direction

별도 DB Migration Approval Request 생성

### Re-review Required

Yes
```

Approval Checklist:

```md
## Approval Checklist

- [ ] 승인 대상 Action이 명확한가?
- [ ] Target이 명확한가?
- [ ] Expected Impact가 설명되었는가?
- [ ] Risk가 설명되었는가?
- [ ] Rollback Plan이 있는가?
- [ ] 사용자가 명확히 승인했는가?
- [ ] Approval Scope 안의 작업만 실행하는가?
- [ ] Approval State가 최신인가?
- [ ] 실행 결과를 기록했는가?
```

---

### [FAQ]

Q. Approval Failure는 언제 발생해?
A. 승인 없이 위험 작업을 실행하거나 승인 범위와 다른 작업을 실행할 때 발생한다.

Q. 모호한 승인은 실행 기준이 될 수 있어?
A. 아니다. 대상, Action, 범위가 명확해야 한다.

Q. 오래된 승인을 재사용해도 돼?
A. 안 된다. Approval은 특정 Action과 Target에 한정해야 한다.

Q. 승인 후 실행 결과도 기록해야 해?
A. 해야 한다. Tool Result State와 Shared State에 기록해야 한다.

---

# 9. RAG Document Tool Permission

## 9.1 Documentation Tool Permission

### [개념]

Documentation Tool Permission은 RAG 문서 제작과 검수 과정에서 Documentation Agent, Review Agent, Fix Agent가 사용할 수 있는 문서 관련 Tool 권한이다.

RAG 문서 작업에서는 새 문서 작성, 기존 문서 수정, 기존 문서 덮어쓰기, 문서 삭제를 구분해야 한다.

기본 구조:

```text
Documentation Agent
→ Document Read / Document Write

Review Agent
→ Document Read / RAG Search

Fix Agent
→ Document Read / Document Modify within Findings

PM Agent
→ State Update / Final Integration
```

---

### [핵심]

- Documentation Agent는 문서 작성 중심이다.
- Review Agent는 문서 읽기와 검수 중심이다.
- Fix Agent는 Review Findings 범위 안에서 문서 수정 가능하다.
- 새 문서 초안 생성은 보통 승인 없이 가능하다.
- 기존 문서 덮어쓰기는 승인 대상이 될 수 있다.
- 문서 삭제는 Dangerous Tool이다.
- Master Rules와 Domain Rules 수정은 승인 대상이다.
- Output Format은 현재 User Request를 우선한다.

---

### [실무]

RAG 문서 Tool Permission:

| Agent               | Allowed Tools                             | Restricted / Approval    |
| ------------------- | ----------------------------------------- | ------------------------ |
| PM Agent            | RAG Search, State Update, Handoff         | 기존 문서 삭제           |
| Documentation Agent | Document Read, Document Write, RAG Search | 기존 문서 덮어쓰기       |
| Review Agent        | Document Read, RAG Search                 | Document Write 금지      |
| Fix Agent           | Document Read, Document Modify            | 기존 문서 덮어쓰기, 삭제 |
| File Manager Agent  | File Create                               | Delete, Overwrite        |

RAG 문서 위험 작업:

```text
기존 문서 삭제
기존 문서 덮어쓰기
파일명 변경
디렉터리 구조 변경
Master Rules 수정
Domain Rules 수정
Project Progress 수정
```

RAG Document Approval Matrix:

| Action                  | Approval         |
| ----------------------- | ---------------- |
| 새 Part 문서 작성       | 보통 불필요      |
| 새 초안 생성            | 보통 불필요      |
| 기존 Part 문서 수정     | 상황에 따라 필요 |
| 기존 Part 문서 덮어쓰기 | 필요             |
| Master Rules 수정       | 필요             |
| Domain Rules 수정       | 필요             |
| Project Progress 수정   | 필요             |
| 폴더 구조 변경          | 필요             |
| 문서 삭제               | 필요             |
| 파일명 변경             | 필요             |

---

### [FAQ]

Q. Documentation Tool Permission이 뭐야?
A. RAG 문서 제작, 검수, 수정 과정에서 Agent가 사용할 수 있는 문서 관련 Tool 권한이다.

Q. Documentation Agent는 어떤 Tool을 사용할 수 있어?
A. Document Read, Document Write, RAG Search를 사용할 수 있다.

Q. Review Agent가 문서를 직접 수정해도 돼?
A. 원칙적으로 수정하지 않는다. Review Agent는 검수하고 Fix Agent가 수정한다.

Q. RAG 문서 제작에서 위험 Tool은 뭐야?
A. 기존 문서 삭제, 덮어쓰기, 파일명 변경, Master Rules 수정, Domain Rules 수정이다.

---

# 10. Tool Permission Checklist

## 10.1 Pre-use Checklist

### [개념]

Pre-use Checklist는 Agent가 Tool을 사용하기 전에 권한, Scope, 위험, 승인 필요 여부를 검수하는 기준이다.

Pre-use Checklist는 승인 없는 위험 작업과 Role Scope 위반을 줄인다.

---

### [핵심]

- Agent Role을 확인한다.
- Requested Tool을 확인한다.
- Tool Category를 확인한다.
- Agent Scope를 확인한다.
- Tool Permission을 확인한다.
- 위험 작업 여부를 확인한다.
- 외부 영향 여부를 확인한다.
- Approval 필요 여부를 확인한다.
- Approval State를 확인한다.
- 민감정보 접근 여부를 확인한다.

---

### [실무]

Tool Permission Pre-use Checklist:

```md
## Tool Permission Pre-use Checklist

- [ ] Agent Role이 명확한가?
- [ ] Requested Tool이 Agent Scope 안인가?
- [ ] Requested Tool이 Agent Permission에 포함되는가?
- [ ] Tool Category가 Read / Write / Dangerous 중 무엇인가?
- [ ] 외부 영향이 있는가?
- [ ] 데이터 변경이 발생하는가?
- [ ] 파일 삭제 또는 덮어쓰기가 발생하는가?
- [ ] 운영 환경에 영향을 주는가?
- [ ] 비용이 발생하는가?
- [ ] Human Approval이 필요한가?
- [ ] Approval State가 approved인가?
- [ ] 민감정보 접근 위험이 있는가?
```

---

### [FAQ]

Q. Pre-use Checklist가 뭐야?
A. Agent가 Tool을 사용하기 전에 권한, Scope, 위험, 승인 필요 여부를 검수하는 기준이다.

Q. Tool 사용 전에 반드시 확인할 것은?
A. Agent Scope, Tool Permission, Tool Category, 외부 영향, Human Approval 필요 여부다.

Q. Approval State가 pending이면 실행해도 돼?
A. 안 된다. approved 상태가 되기 전에는 실행하지 않는다.

Q. 민감정보 접근 위험도 확인해야 해?
A. 해야 한다. Read Tool이라도 민감정보가 포함될 수 있기 때문이다.

---

## 10.2 Post-use Checklist

### [개념]

Post-use Checklist는 Agent가 Tool을 사용한 후 결과 기록, 실패 기록, 민감정보 마스킹, Shared State 반영 여부를 검수하는 기준이다.

Post-use Checklist는 Tool Result Missing과 Tool Failure 은폐를 줄인다.

---

### [핵심]

- Tool Result를 기록한다.
- Status를 기록한다.
- Failure가 있으면 숨기지 않는다.
- Partial Result를 표시한다.
- 민감정보를 마스킹한다.
- Shared State 업데이트 필요 여부를 확인한다.
- Review 또는 Test 필요 여부를 확인한다.
- Regression Risk를 확인한다.
- 다음 Action을 기록한다.

---

### [실무]

Tool Permission Post-use Checklist:

```md
## Tool Permission Post-use Checklist

- [ ] Tool Result가 기록되었는가?
- [ ] Status가 completed / failed / partial 중 하나로 표시되었는가?
- [ ] Failure가 숨겨지지 않았는가?
- [ ] Partial Result가 표시되었는가?
- [ ] 민감정보가 마스킹되었는가?
- [ ] Shared State 업데이트가 필요한가?
- [ ] Review 또는 Test가 필요한가?
- [ ] Regression Risk가 있는가?
- [ ] Next Action이 명확한가?
```

---

### [FAQ]

Q. Post-use Checklist가 뭐야?
A. Tool 사용 후 결과 기록, 실패 기록, 민감정보 마스킹, Shared State 반영 여부를 검수하는 기준이다.

Q. Tool 사용 후 가장 중요한 것은?
A. Tool Result와 Status를 기록하는 것이다.

Q. Tool Failure는 숨겨도 돼?
A. 안 된다. Failure Type, Reason, Suggested Action을 기록해야 한다.

Q. Tool Result에 민감정보가 있으면?
A. 마스킹하거나 필요한 요약만 기록해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Tool Permission이 뭐야?
A. Multi-Agent System에서 각 Agent가 사용할 수 있는 Tool의 권한 범위다.

Q. Tool Permission이 필요한 이유는?
A. Agent가 자기 역할에 맞는 Tool만 사용하게 하고 위험 작업을 통제하기 위해 필요하다.

Q. 모든 Agent에게 모든 Tool을 허용하면 안 되는 이유는?
A. 삭제, 배포, DB 변경 같은 위험 작업을 잘못 실행할 수 있기 때문이다.

Q. 최소 권한 원칙이 뭐야?
A. Agent가 작업 수행에 필요한 최소 Tool 권한만 가져야 한다는 원칙이다.

Q. 최소 권한 원칙을 적용하는 이유는?
A. Role Overlap, 위험 Tool 실행, Tool Permission Failure를 줄이기 위해서다.

Q. Read Tool이 뭐야?
A. 파일, 문서, 로그, Schema, RAG Context처럼 정보를 조회하는 Tool이다.

Q. Read Tool은 항상 안전해?
A. 아니다. 민감정보나 운영 데이터가 포함될 수 있으므로 Scope 제한이 필요하다.

Q. Write Tool이 뭐야?
A. 파일, 코드, 문서, 설정, Shared State를 생성하거나 수정하는 Tool이다.

Q. Write Tool은 왜 제한해야 해?
A. 시스템 상태를 변경하므로 잘못 사용하면 데이터 손상, 코드 충돌, 설정 오류가 발생할 수 있기 때문이다.

Q. Dangerous Tool이 뭐야?
A. 잘못 실행하면 데이터 손상, 서비스 중단, 비용 발생, 보안 사고, 외부 영향이 발생할 수 있는 Tool이다.

Q. Dangerous Tool은 자동 실행해도 돼?
A. 안 된다. Human Approval 후 실행해야 한다.

Q. Human Approval이 뭐야?
A. 위험하거나 외부 영향이 있는 Tool을 실행하기 전에 사용자 승인을 받는 절차다.

Q. Human Approval은 Workflow Pattern이야?
A. 아니다. Tool 실행 통제를 위한 승인 규칙이다.

Q. Human Approval이 필요한 작업은?
A. 파일 삭제, DB 변경, 배포, 서비스 재시작, 결제, 이메일 발송, 운영 설정 변경이다.

Q. Approval State가 뭐야?
A. Human Approval이 필요한 작업의 승인 상태를 Shared State에 기록한 정보다.

Q. 승인 대기 상태에서는 실행해도 돼?
A. 안 된다. status가 approved가 되기 전에는 실행하지 않는다.

Q. PM Agent는 어떤 Tool을 사용할 수 있어?
A. RAG Search, State Update, Routing, Handoff Generation, Result Integration을 사용할 수 있다.

Q. PM Agent가 직접 배포를 실행해도 돼?
A. 안 된다. 배포는 DevOps Agent와 Human Approval을 통해 처리해야 한다.

Q. Specialist Agent는 어떤 Tool을 사용할 수 있어?
A. 자기 Domain 작업에 필요한 RAG Search, File Read, Code Search, Schema Read 같은 Tool을 제한적으로 사용할 수 있다.

Q. DevOps Agent가 배포를 바로 실행해도 돼?
A. 안 된다. 배포와 재시작은 Human Approval 대상이다.

Q. Review Agent와 Fix Agent Tool Permission은 왜 분리해?
A. Review는 검토, Fix는 수정 역할이므로 권한을 분리해야 책임 경계와 안전성이 유지된다.

Q. Review Agent가 직접 파일을 수정해도 돼?
A. 원칙적으로 수정하지 않는다. 수정은 Fix Agent가 담당한다.

Q. Permission Check Flow가 뭐야?
A. Agent가 Tool 사용 전에 Scope, 권한, 위험도, 승인 필요 여부를 확인하는 절차다.

Q. 권한이 없으면 어떻게 해?
A. Tool 실행을 중단하고 PM Agent에게 반환하거나 Approval Request를 생성한다.

Q. Permission Decision Record가 뭐야?
A. Tool 사용 허용, 차단, 승인 요청, PM Agent 반환 같은 결정을 기록하는 정보다.

Q. Permission Decision과 Tool Result는 같아?
A. 아니다. Permission Decision은 실행 전 판단이고 Tool Result는 실행 후 결과다.

Q. Tool Result State가 뭐야?
A. Agent가 Tool을 사용한 결과를 Shared State에 기록한 정보다.

Q. Tool Failure Handling이 뭐야?
A. Tool 실행 실패, 권한 부족, 입력 오류, 외부 오류가 발생했을 때 처리하는 방식이다.

Q. Tool Permission과 RAG Scope 차이는?
A. RAG Scope는 어떤 지식을 검색할 수 있는지이고, Tool Permission은 어떤 행동을 실행할 수 있는지이다.

Q. Tool Permission과 RAG Scope를 둘 다 제한해야 하는 이유는?
A. 관련 없는 지식 사용과 위험한 행동 실행을 동시에 줄이기 위해서다.

Q. Permission Failure는 언제 발생해?
A. 권한 없는 Tool 사용, 승인 없는 위험 작업 실행, Agent Scope와 Tool Permission 불일치에서 발생한다.

Q. Dangerous Tool을 승인 없이 실행하려 하면?
A. 즉시 차단하고 Human Approval Request를 생성해야 한다.

Q. Approval Failure는 언제 발생해?
A. 승인 없이 위험 작업을 실행하거나 승인 범위와 다른 작업을 실행할 때 발생한다.

Q. 모호한 승인은 실행 기준이 될 수 있어?
A. 아니다. 대상, Action, 범위가 명확해야 한다.

Q. Documentation Tool Permission이 뭐야?
A. RAG 문서 제작, 검수, 수정 과정에서 Agent가 사용할 수 있는 문서 관련 Tool 권한이다.

Q. RAG 문서 제작에서 위험 Tool은 뭐야?
A. 기존 문서 삭제, 덮어쓰기, 파일명 변경, Master Rules 수정, Domain Rules 수정이다.

Q. Pre-use Checklist가 뭐야?
A. Agent가 Tool을 사용하기 전에 권한, Scope, 위험, 승인 필요 여부를 검수하는 기준이다.

Q. Post-use Checklist가 뭐야?
A. Tool 사용 후 결과 기록, 실패 기록, 민감정보 마스킹, Shared State 반영 여부를 검수하는 기준이다.

Q. 개인 AI 개발팀에서 Tool Permission은 왜 필요해?
A. Agent가 파일, 코드, DB, 배포, 문서 작업을 안전하게 수행하고 위험 작업을 승인 절차로 분리하기 위해 필요하다.

Q. Part10과 Part12의 차이는 뭐야?
A. Part10은 Tool 권한과 승인 규칙을 다루고, Part12는 Workflow Pattern 종류와 실행 흐름을 다룬다.
