# Tool Calling & Function Calling Part06 - Agent Tool Routing & Multi-Agent Tool Use

---

# 1. Agent Tool Routing

## 1.1 Agent Tool Routing Concept

### [개념]

Agent Tool Routing은 사용자 요청을 분석한 뒤 어떤 Agent가 어떤 Tool을 사용할지 결정하는 절차이다.

Multi-Agent System에서는 모든 Agent가 모든 Tool을 직접 사용하지 않는다.

PM Agent가 요청을 분석하고, Domain Agent가 역할에 맞는 Tool을 사용하며, Review Agent가 Tool Result와 산출물을 검증하는 구조가 안전하다.

Agent Tool Routing은 Tool Choice뿐 아니라 Agent Choice까지 포함한다.

---

### [핵심]

- Agent Tool Routing은 Agent 선택과 Tool 선택을 함께 다룬다.
- PM Agent는 요청 분석과 작업 분배를 담당한다.
- Backend Agent는 Backend 관련 Tool을 사용한다.
- Frontend Agent는 Frontend 관련 Tool을 사용한다.
- Review Agent는 검증 중심 Tool을 사용한다.
- DevOps Agent는 Infra, Log, Deploy 관련 Tool을 제한적으로 사용한다.
- AI/ML Agent는 RAG, Vector Search, Evaluation 관련 Tool을 사용한다.
- Agent별 allowedTools와 deniedTools를 분리한다.
- 위험 Tool은 Agent 권한과 Human Confirmation을 모두 통과해야 한다.
- Tool Result는 Agent Handoff 형식으로 전달한다.

---

### [실무]

기본 Agent Tool Routing Flow:

```text
User Request
→ PM Agent Request Analysis
→ Select Responsible Agent
→ Select Allowed Tool
→ Generate Tool Arguments
→ Validate Arguments
→ Execute Tool
→ Return Tool Result
→ Agent Handoff
→ Review Agent Validation
→ Final Output
```

Agent별 기본 역할:

| Agent          | 역할                                     | Tool 사용 방향       |
| -------------- | ---------------------------------------- | -------------------- |
| PM Agent       | 요청 분석 / 작업 분배 / 우선순위 판단    | 검색 / 라우팅 중심   |
| Backend Agent  | Backend 코드 / API / DB / 테스트 작업    | Backend Tool 중심    |
| Frontend Agent | UI / Component / Routing / API 연결 작업 | Frontend Tool 중심   |
| Review Agent   | 결과 검증 / 오류 탐지 / 품질 검수        | Read / Validate 중심 |
| DevOps Agent   | Infra / Log / Deploy / Runtime 상태      | 제한적 실행 중심     |
| AI/ML Agent    | RAG / Vector / Evaluation / Prompt 개선  | 검색 / 평가 중심     |

Routing 판단 기준:

```text
요청이 전체 기획 / 분배 → PM Agent
요청이 Backend 구현 / API / DB → Backend Agent
요청이 Frontend UI / React / Routing → Frontend Agent
요청이 검수 / 테스트 / 품질 확인 → Review Agent
요청이 배포 / 로그 / 인프라 → DevOps Agent
요청이 RAG / Embedding / Vector DB / Prompt / 평가 → AI/ML Agent
```

---

### [FAQ]

Q. Agent Tool Routing이 뭐야?
A. 사용자 요청을 어떤 Agent가 처리하고 어떤 Tool을 사용할지 결정하는 절차다.

Q. PM Agent가 모든 Tool을 직접 실행해도 돼?
A. 권장하지 않는다. PM Agent는 요청 분석과 작업 분배 중심으로 동작하는 것이 안전하다.

Q. Domain Agent는 뭐야?
A. Backend Agent, Frontend Agent, DevOps Agent, AI/ML Agent처럼 특정 영역 작업을 담당하는 Agent다.

Q. Review Agent는 어떤 Tool을 써?
A. Read Tool, Static Analysis Tool, Test Result Tool, RAG Search Tool처럼 검증 중심 Tool을 사용한다.

Q. Agent Tool Routing에서 가장 중요한 기준은?
A. Agent 역할, Tool 권한, Risk Level, Side Effect, Human Confirmation 필요 여부다.

---

# 2. Agent Tool Permission

## 2.1 Agent Permission Concept

### [개념]

Agent Tool Permission은 Agent별로 사용할 수 있는 Tool과 사용할 수 없는 Tool을 정의하는 권한 기준이다.

Multi-Agent System에서는 Agent별 최소 권한 원칙을 적용해야 한다.

Agent가 자신의 역할과 무관한 Tool을 사용할 수 있으면 오작동, 보안 문제, 데이터 손실이 발생할 수 있다.

---

### [핵심]

- Agent별 Tool Permission을 정의한다.
- allowedTools와 deniedTools를 구분한다.
- read, validate, write, execute, admin 권한을 분리한다.
- 위험 Tool은 제한된 Agent만 사용할 수 있다.
- High Risk Tool은 Agent 권한이 있어도 Human Confirmation이 필요하다.
- PM Agent는 위험 Tool 직접 실행을 제한한다.
- Review Agent는 수정 Tool보다 검증 Tool 중심으로 제한한다.
- DevOps Agent의 Production Deploy는 별도 승인 정책이 필요하다.
- Permission Check는 Agent Runtime에서 강제한다.

---

### [실무]

Agent Permission 예시:

```json
{
  "agents": {
    "pm-agent": {
      "allowedTools": ["search_rag_documents", "route_task"],
      "deniedTools": [
        "write_project_file",
        "execute_database_write",
        "deploy_application"
      ]
    },
    "backend-agent": {
      "allowedTools": [
        "search_rag_documents",
        "read_project_file",
        "write_project_file",
        "execute_test_suite"
      ],
      "deniedTools": ["deploy_application", "send_email_message"]
    },
    "frontend-agent": {
      "allowedTools": [
        "search_rag_documents",
        "read_project_file",
        "write_project_file",
        "execute_frontend_test"
      ],
      "deniedTools": ["execute_database_write", "deploy_application"]
    },
    "review-agent": {
      "allowedTools": [
        "search_rag_documents",
        "read_project_file",
        "run_static_analysis",
        "read_test_result"
      ],
      "deniedTools": [
        "write_project_file",
        "execute_database_write",
        "send_email_message"
      ]
    },
    "devops-agent": {
      "allowedTools": [
        "read_log",
        "check_infra_status",
        "read_deploy_status",
        "deploy_application"
      ],
      "deniedTools": ["execute_database_write", "send_email_message"]
    },
    "ai-ml-agent": {
      "allowedTools": [
        "search_rag_documents",
        "vector_search",
        "evaluate_retrieval",
        "rewrite_query"
      ],
      "deniedTools": [
        "delete_project_file",
        "execute_database_write",
        "deploy_application"
      ]
    }
  }
}
```

권한 확인 Flow:

```text
Agent Requests Tool
→ Check allowedTools
→ Check deniedTools
→ Check permissionLevel
→ Check riskLevel
→ Check confirmation requirement
→ Execute or Block
```

권한 부족 Result:

```json
{
  "status": "error",
  "error": {
    "type": "PermissionError",
    "code": "AGENT_TOOL_PERMISSION_DENIED",
    "message": "Review Agent does not have permission to write project files.",
    "retryable": false
  },
  "metadata": {
    "agent": "review-agent",
    "toolName": "write_project_file"
  }
}
```

---

### [FAQ]

Q. Agent Tool Permission이 뭐야?
A. Agent별로 사용할 수 있는 Tool과 사용할 수 없는 Tool을 정의하는 권한 기준이다.

Q. Agent별 권한을 왜 나눠야 해?
A. 최소 권한 원칙을 적용해 오작동, 보안 문제, 데이터 손실을 줄이기 위해서다.

Q. allowedTools와 deniedTools를 모두 둬야 해?
A. 둘 다 두는 것이 좋다. 허용 목록과 명시적 금지 목록을 함께 관리하면 안전하다.

Q. Agent 권한이 있으면 High Risk Tool을 바로 실행해도 돼?
A. 안 된다. Agent 권한이 있어도 High Risk Tool은 Human Confirmation을 통과해야 한다.

Q. Permission Check는 어디서 해야 해?
A. LLM Prompt가 아니라 Agent Runtime 또는 Backend System에서 강제해야 한다.

---

# 3. PM Agent Tool Use

## 3.1 PM Agent Role

### [개념]

PM Agent는 사용자 요청을 분석하고 작업을 분해하며 적절한 Domain Agent로 라우팅하는 Agent이다.

PM Agent는 전체 Workflow를 조율하지만 위험 Tool을 직접 실행하는 역할은 아니다.

PM Agent는 Tool Calling에서 검색, 계획, 작업 분배, Handoff 생성 중심으로 동작한다.

---

### [핵심]

- PM Agent는 사용자 요청을 분석한다.
- PM Agent는 작업을 작은 단위로 나눈다.
- PM Agent는 적절한 Domain Agent를 선택한다.
- PM Agent는 직접 위험 Tool을 실행하지 않는다.
- PM Agent는 RAG Search Tool을 사용할 수 있다.
- PM Agent는 Task Routing Tool을 사용할 수 있다.
- PM Agent는 Agent Handoff를 생성한다.
- PM Agent는 작업 우선순위와 의존성을 관리한다.
- PM Agent는 Final Output 흐름을 조율한다.

---

### [실무]

PM Agent 권장 Tool:

| Tool                   | 목적                      | Risk |
| ---------------------- | ------------------------- | ---- |
| search_rag_documents   | 관련 규칙 / 요구사항 검색 | Low  |
| route_task             | 적절한 Agent 선택         | Low  |
| create_task_plan       | 작업 분해                 | Low  |
| read_project_progress  | 진행 상황 확인            | Low  |
| summarize_agent_result | Agent 결과 요약           | Low  |

PM Agent 제한 Tool:

| Tool                   | 제한 이유           |
| ---------------------- | ------------------- |
| write_project_file     | 직접 수정 권한 제한 |
| execute_database_write | 데이터 변경 위험    |
| deploy_application     | 운영 환경 변경 위험 |
| send_email_message     | 외부 발송 위험      |
| request_payment        | 비용 발생 위험      |

PM Agent Routing 예시:

```json
{
  "fromAgent": "pm-agent",
  "toAgent": "backend-agent",
  "task": "Implement API response validation based on RAG rules.",
  "requiredTools": ["search_rag_documents", "read_project_file"],
  "riskLevel": "low",
  "requiresReview": true
}
```

---

### [FAQ]

Q. PM Agent는 어떤 역할이야?
A. 사용자 요청을 분석하고 작업을 분해한 뒤 적절한 Agent로 라우팅하는 역할이다.

Q. PM Agent가 파일을 직접 수정해도 돼?
A. 기본적으로 권장하지 않는다. 파일 수정은 Backend Agent나 Frontend Agent 같은 Domain Agent가 담당하는 것이 안전하다.

Q. PM Agent가 사용할 수 있는 Tool은?
A. RAG Search, Task Routing, Progress Read, Result Summary 같은 낮은 위험 Tool이 적절하다.

Q. PM Agent가 배포 Tool을 실행해도 돼?
A. 안 된다. 배포는 DevOps Agent와 Human Confirmation을 통해 처리하는 것이 안전하다.

Q. PM Agent의 핵심 산출물은?
A. Task Plan, Agent Routing, Agent Handoff, Final Output 조율이다.

---

# 4. Domain Agent Tool Use

## 4.1 Domain Agent Concept

### [개념]

Domain Agent는 특정 기술 영역의 작업을 담당하는 Agent이다.

이 문서의 기본 Domain Agent는 Backend Agent, Frontend Agent, DevOps Agent, AI/ML Agent이다.

Domain Agent는 자신의 영역에 필요한 Tool만 사용해야 한다.

---

### [핵심]

- Domain Agent는 특정 영역 작업을 담당한다.
- Backend Agent는 Backend 코드, API, DB, 테스트를 담당한다.
- Frontend Agent는 UI, Component, Routing, API 연결을 담당한다.
- DevOps Agent는 Infra, Log, Deploy 상태를 담당한다.
- AI/ML Agent는 RAG, Vector DB, Embedding, Evaluation을 담당한다.
- Domain Agent는 자신의 allowedTools 안에서만 Tool을 호출한다.
- Domain Agent의 결과는 Review Agent 검증을 거친다.
- Domain Agent가 고위험 Tool을 사용할 때는 Human Confirmation이 필요하다.

---

### [실무]

Backend Agent Tool 예시:

| Tool                 | 목적                  |
| -------------------- | --------------------- |
| search_rag_documents | Backend 규칙 검색     |
| read_project_file    | 코드 / 설정 파일 읽기 |
| write_project_file   | 코드 수정             |
| query_database_read  | DB 조회               |
| execute_test_suite   | 테스트 실행           |
| read_test_result     | 테스트 결과 확인      |

Frontend Agent Tool 예시:

| Tool                  | 목적                         |
| --------------------- | ---------------------------- |
| search_rag_documents  | Frontend 규칙 검색           |
| read_project_file     | Component / Router 파일 읽기 |
| write_project_file    | Component 수정               |
| execute_frontend_test | Frontend 테스트 실행         |
| read_browser_log      | 브라우저 로그 확인           |

DevOps Agent Tool 예시:

| Tool                | 목적                      |
| ------------------- | ------------------------- |
| read_log            | 서버 / 컨테이너 로그 확인 |
| check_infra_status  | 인프라 상태 확인          |
| read_deploy_status  | 배포 상태 확인            |
| deploy_application  | 배포 실행                 |
| rollback_deployment | 롤백 실행                 |

AI/ML Agent Tool 예시:

| Tool                     | 목적                |
| ------------------------ | ------------------- |
| search_rag_documents     | RAG 문서 검색       |
| vector_search            | Vector DB 검색      |
| evaluate_retrieval       | Retrieval 평가      |
| rewrite_query            | Query Rewrite       |
| inspect_embedding_config | Embedding 설정 확인 |

---

### [FAQ]

Q. Domain Agent가 뭐야?
A. Backend, Frontend, DevOps, AI/ML처럼 특정 기술 영역 작업을 담당하는 Agent다.

Q. Backend Agent는 어떤 Tool을 써?
A. Backend RAG Search, File Read, File Write, DB Read, Test Tool을 사용할 수 있다.

Q. Frontend Agent는 어떤 Tool을 써?
A. Frontend RAG Search, File Read, File Write, Component Search, Frontend Test Tool을 사용할 수 있다.

Q. DevOps Agent는 어떤 Tool을 써?
A. Log Search, Infra Status, Deploy Status, Deploy Tool을 제한적으로 사용할 수 있다.

Q. AI/ML Agent는 어떤 Tool을 써?
A. RAG Search, Vector Search, Retrieval Evaluation, Query Rewrite, Embedding Config Tool을 사용할 수 있다.

---

# 5. Review Agent Tool Use

## 5.1 Review Agent Role

### [개념]

Review Agent는 Domain Agent가 생성한 결과, Tool Result, 코드 변경, 테스트 결과, 안전 정책 준수 여부를 검증하는 Agent이다.

Review Agent는 기본적으로 직접 수정보다 검증과 피드백에 집중한다.

Review Agent는 Tool Calling 결과가 신뢰 가능한지 확인하고, 문제가 있으면 원 담당 Domain Agent에게 수정 요청을 전달한다.

---

### [핵심]

- Review Agent는 검증 중심 Agent이다.
- Review Agent는 Tool Result status를 확인한다.
- Review Agent는 source와 metadata를 확인한다.
- Review Agent는 success / error / blocked / partial을 구분한다.
- Review Agent는 테스트 결과를 확인한다.
- Review Agent는 Safe Execution Policy 준수 여부를 검토한다.
- Review Agent는 위험 Tool 자동 실행 여부를 확인한다.
- Review Agent는 직접 write 권한을 제한하는 것이 안전하다.
- 수정이 필요하면 원 담당 Domain Agent에게 재작업을 요청한다.

---

### [실무]

Review Agent 권장 Tool:

| Tool                 | 목적                  |
| -------------------- | --------------------- |
| search_rag_documents | 검수 기준 검색        |
| read_project_file    | 변경 파일 읽기        |
| run_static_analysis  | 정적 분석             |
| read_test_result     | 테스트 결과 확인      |
| compare_diff         | 변경 전후 비교        |
| validate_tool_result | Tool Result 구조 검증 |
| inspect_audit_log    | 위험 작업 로그 확인   |

Review Agent 검증 기준:

```text
Tool Result status 확인
→ source / metadata 확인
→ Error Handling 확인
→ Safe Execution Policy 확인
→ Test Result 확인
→ Domain Rule 위반 확인
→ Issue 생성 or Approve
```

Review Agent가 생성하는 검수 결과 예시:

```json
{
  "fromAgent": "review-agent",
  "toAgent": "backend-agent",
  "status": "changes_requested",
  "issues": [
    {
      "type": "ValidationMissing",
      "message": "Tool Arguments validation is not implemented before execution.",
      "severity": "high"
    }
  ],
  "requiresRework": true
}
```

Fix 작업 기준:

```text
Review Agent detects issue
→ Send rework request to original Domain Agent
→ Domain Agent fixes
→ Review Agent validates again
```

별도 Fix Agent는 기본 구조가 아니다.

필요한 경우 확장 옵션으로 둘 수 있지만, 기본 구조에서는 원 담당 Domain Agent가 재작업한다.

---

### [FAQ]

Q. Review Agent는 어떤 역할이야?
A. Tool Result, 코드 변경, 테스트 결과, 안전 정책 준수 여부를 검증하는 역할이다.

Q. Review Agent가 직접 파일을 수정해도 돼?
A. 기본적으로 권장하지 않는다. Review Agent는 검증하고, 수정은 원 담당 Domain Agent가 수행하는 것이 안전하다.

Q. Review Agent는 무엇을 확인해야 해?
A. Tool Result status, source, metadata, error handling, test result, Safe Execution Policy 준수 여부를 확인해야 한다.

Q. 문제가 발견되면 누가 수정해?
A. 기본 구조에서는 원 담당 Domain Agent가 수정하고 Review Agent가 다시 검증한다.

Q. Fix Agent는 필수야?
A. 아니다. Fix Agent는 확장 옵션이고, 기본 구조에서는 Backend Agent나 Frontend Agent 같은 원 담당 Agent가 재작업한다.

---

# 6. Multi-Agent Tool Use

## 6.1 Multi-Agent Tool Use Concept

### [개념]

Multi-Agent Tool Use는 여러 Agent가 하나의 사용자 요청을 처리하면서 각자의 역할에 맞는 Tool을 사용하는 구조이다.

Multi-Agent Tool Use에서는 Tool Result, Agent Handoff, Shared State, Review Loop가 중요하다.

Agent가 독립적으로 Tool을 호출하더라도 전체 Workflow는 PM Agent와 Review Agent 기준으로 조율되어야 한다.

---

### [핵심]

- Multi-Agent Tool Use는 역할 분리 기반이다.
- PM Agent가 작업을 분배한다.
- Domain Agent가 Tool을 사용해 작업을 수행한다.
- Review Agent가 결과를 검증한다.
- DevOps Agent는 배포와 운영 상태를 제한적으로 담당한다.
- AI/ML Agent는 RAG / Vector / Evaluation 작업을 담당한다.
- Tool Result는 구조화해서 전달한다.
- Shared State에는 작업 상태와 Tool Result를 저장할 수 있다.
- Review Loop를 통해 품질을 개선한다.
- 위험 작업은 어느 Agent가 호출해도 Safe Execution Policy를 따른다.

---

### [실무]

Multi-Agent Workflow:

```text
User
→ PM Agent
→ Backend Agent
→ Frontend Agent
→ Review Agent
→ DevOps Agent if needed
→ AI/ML Agent if needed
→ Review Agent
→ Final Output
```

Tool Result 전달 구조:

```json
{
  "workflowId": "wf_001",
  "taskId": "task_backend_001",
  "agent": "backend-agent",
  "toolResults": [
    {
      "toolName": "search_rag_documents",
      "status": "success",
      "source": "Backend_Domain_Rules.md"
    },
    {
      "toolName": "execute_test_suite",
      "status": "partial",
      "data": {
        "passed": 12,
        "failed": 1
      }
    }
  ],
  "nextAgent": "review-agent"
}
```

Multi-Agent Tool Use 원칙:

- Agent는 자신의 역할과 권한 안에서만 Tool을 사용한다.
- Tool Result는 status를 명확히 유지한다.
- failed / blocked / partial 상태를 숨기지 않는다.
- Review Agent는 최종 승인 전 결과를 검증한다.
- 위험 Tool은 Agent 종류와 무관하게 Human Confirmation을 요구한다.

---

### [FAQ]

Q. Multi-Agent Tool Use가 뭐야?
A. 여러 Agent가 각자의 역할에 맞는 Tool을 사용해 하나의 요청을 처리하는 구조다.

Q. Multi-Agent에서 가장 중요한 것은?
A. 역할 분리, Tool 권한 분리, Tool Result 구조화, Agent Handoff, Review Loop다.

Q. Tool Result는 왜 구조화해야 해?
A. 다음 Agent가 성공, 실패, 차단, 일부 성공 상태를 정확히 이해해야 하기 때문이다.

Q. 위험 Tool은 Domain Agent가 호출하면 자동 실행해도 돼?
A. 안 된다. 위험 Tool은 Agent 종류와 관계없이 Human Confirmation이 필요하다.

Q. Multi-Agent Workflow에서 Review Agent는 필수야?
A. 품질과 안전성을 위해 최종 검증 단계로 두는 것이 좋다.

---

# 7. Agent Handoff Format

## 7.1 Agent Handoff Concept

### [개념]

Agent Handoff는 한 Agent가 수행한 작업 결과를 다음 Agent에게 전달하는 구조이다.

Agent Handoff에는 작업 상태, Tool Result, 변경 사항, 문제점, 다음 작업 요청이 포함되어야 한다.

Agent Handoff가 불명확하면 다음 Agent가 이전 작업 결과를 잘못 해석할 수 있다.

---

### [핵심]

- Agent Handoff는 Agent 간 전달 형식이다.
- fromAgent와 toAgent를 명시한다.
- task와 status를 명시한다.
- Tool Result를 포함한다.
- changedFiles를 포함할 수 있다.
- knownIssues를 포함한다.
- requiredReview 여부를 표시한다.
- blocked / partial 상태를 숨기지 않는다.
- Review Agent가 검증할 수 있는 정보가 포함되어야 한다.

---

### [실무]

Agent Handoff 기본 구조:

```json
{
  "handoffId": "handoff_001",
  "workflowId": "wf_001",
  "fromAgent": "backend-agent",
  "toAgent": "review-agent",
  "task": "Implement Tool Arguments validation before execution.",
  "status": "completed",
  "toolResults": [
    {
      "toolName": "read_project_file",
      "status": "success",
      "metadata": {
        "source": "src/main/java/ToolService.java"
      }
    },
    {
      "toolName": "execute_test_suite",
      "status": "success",
      "data": {
        "passed": 18,
        "failed": 0
      }
    }
  ],
  "changedFiles": [
    "src/main/java/ToolService.java",
    "src/test/java/ToolServiceTest.java"
  ],
  "knownIssues": [],
  "requiresReview": true
}
```

문제 포함 Handoff 예시:

```json
{
  "fromAgent": "frontend-agent",
  "toAgent": "review-agent",
  "task": "Connect Tool Result UI state.",
  "status": "partial",
  "toolResults": [
    {
      "toolName": "execute_frontend_test",
      "status": "partial",
      "data": {
        "passed": 24,
        "failed": 2
      }
    }
  ],
  "knownIssues": [
    {
      "type": "TestFailure",
      "message": "Tool blocked state UI test failed."
    }
  ],
  "requiresReview": true
}
```

---

### [FAQ]

Q. Agent Handoff가 뭐야?
A. 한 Agent가 수행한 작업 결과를 다음 Agent에게 전달하는 구조다.

Q. Agent Handoff에는 무엇이 들어가야 해?
A. fromAgent, toAgent, task, status, toolResults, changedFiles, knownIssues, requiresReview가 들어가면 좋다.

Q. blocked나 partial 상태도 Handoff에 넣어야 해?
A. 반드시 넣어야 한다. 다음 Agent가 누락이나 차단 상태를 알아야 한다.

Q. Review Agent에게 Handoff할 때 중요한 것은?
A. Tool Result, 변경 파일, 테스트 결과, 알려진 문제, 검토 필요 여부다.

Q. Handoff가 부실하면 어떤 문제가 생겨?
A. 다음 Agent가 잘못된 전제로 작업하거나 실패 상태를 성공으로 오해할 수 있다.

---

# 8. Shared State

## 8.1 Shared State Concept

### [개념]

Shared State는 Multi-Agent Workflow에서 여러 Agent가 공유하는 작업 상태와 중간 결과이다.

Shared State에는 사용자 요청, 작업 계획, Agent Handoff, Tool Result, Review 결과, 승인 상태가 포함될 수 있다.

Shared State는 Agent 간 Context 손실을 줄이는 역할을 한다.

---

### [핵심]

- Shared State는 Workflow 공통 상태이다.
- workflowId와 taskId를 포함한다.
- 사용자 요청 원문을 보관할 수 있다.
- 작업 계획과 Agent 배정을 저장한다.
- Tool Result를 저장한다.
- Human Confirmation 상태를 저장한다.
- Review 결과를 저장한다.
- knownIssues를 저장한다.
- 민감정보는 Shared State에 저장하지 않는다.
- Shared State는 최신 상태와 이력을 구분할 수 있어야 한다.

---

### [실무]

Shared State 예시:

```json
{
  "workflowId": "wf_001",
  "userRequest": "Tool Calling 문서 세트를 검수하고 수정해줘.",
  "taskPlan": [
    {
      "taskId": "task_001",
      "assignedAgent": "ai-ml-agent",
      "status": "completed"
    },
    {
      "taskId": "task_002",
      "assignedAgent": "review-agent",
      "status": "in_review"
    }
  ],
  "toolResults": [],
  "approvals": [],
  "knownIssues": [],
  "finalStatus": "in_progress"
}
```

Shared State에 저장 가능한 항목:

| 항목                 | 저장 여부 |
| -------------------- | --------- |
| workflowId           | 저장      |
| taskId               | 저장      |
| Agent Handoff        | 저장      |
| Tool Result metadata | 저장      |
| Review Result        | 저장      |
| Approval Scope       | 저장      |
| API Key              | 저장 금지 |
| Password             | 저장 금지 |
| Raw Secret File      | 저장 금지 |
| 민감 개인정보        | 저장 금지 |

Shared State 관리 원칙:

```text
Store workflow context
→ Store structured Tool Result
→ Store approval status
→ Store review status
→ Mask sensitive data
```

---

### [FAQ]

Q. Shared State가 뭐야?
A. 여러 Agent가 공유하는 작업 상태, Tool Result, Review 결과, 승인 상태 같은 공통 Context다.

Q. Shared State에는 무엇을 저장해?
A. workflowId, taskId, Agent Handoff, Tool Result metadata, Review Result, Approval Scope를 저장할 수 있다.

Q. Shared State에 Secret을 저장해도 돼?
A. 안 된다. API Key, Password, Token, Raw Secret File은 저장하지 않는다.

Q. Shared State는 왜 필요해?
A. Agent 간 Context 손실을 줄이고 이전 Tool Result와 Review 결과를 추적하기 위해 필요하다.

Q. Approval Scope도 Shared State에 저장해?
A. 저장할 수 있다. 단, 승인 범위와 만료 조건을 명확히 해야 한다.

---

# 9. Review Loop

## 9.1 Review Loop Concept

### [개념]

Review Loop는 Domain Agent가 수행한 작업을 Review Agent가 검증하고, 문제가 있으면 원 담당 Domain Agent가 재작업한 뒤 다시 검증하는 반복 구조이다.

Review Loop는 Multi-Agent System의 품질 보증 절차이다.

Review Loop는 Tool Result, 테스트 결과, 코드 변경, 안전 정책 준수 여부를 기준으로 진행한다.

---

### [핵심]

- Review Loop는 품질 검증 반복 구조이다.
- Review Agent가 작업 결과를 검증한다.
- 문제가 없으면 approve한다.
- 문제가 있으면 changes_requested를 반환한다.
- 수정은 기본적으로 원 담당 Domain Agent가 수행한다.
- Fix Agent는 기본 필수 구조가 아니라 확장 옵션이다.
- Tool Result와 Test Result를 검증한다.
- blocked / partial 상태를 검토한다.
- Review Loop가 무한 반복되지 않도록 최대 반복 횟수를 둘 수 있다.

---

### [실무]

Review Loop Flow:

```text
Domain Agent Output
→ Review Agent Validation
→ Approve or Changes Requested
→ Domain Agent Rework
→ Review Agent Re-Validation
→ Final Approval
```

Review 결과 예시:

```json
{
  "fromAgent": "review-agent",
  "toAgent": "backend-agent",
  "reviewStatus": "changes_requested",
  "issues": [
    {
      "severity": "high",
      "type": "MissingPermissionCheck",
      "message": "Tool Execution occurs before Permission Check."
    },
    {
      "severity": "medium",
      "type": "MissingTest",
      "message": "No test covers blocked result handling."
    }
  ],
  "requiredActions": [
    "Move Permission Check before Tool Execution.",
    "Add test case for blocked result."
  ]
}
```

Review Loop 제한:

```text
maxReviewIterations = 3
```

반복 초과 시 PM Agent가 범위를 재조정하거나 사용자에게 현재 상태를 보고한다.

---

### [FAQ]

Q. Review Loop가 뭐야?
A. Domain Agent 작업을 Review Agent가 검증하고, 문제가 있으면 원 담당 Agent가 수정한 뒤 다시 검증하는 반복 구조다.

Q. Review Agent가 직접 수정하지 않는 이유는?
A. 역할 분리와 권한 제한을 유지하기 위해서다. 기본 구조에서는 원 담당 Domain Agent가 수정한다.

Q. Fix Agent가 꼭 필요해?
A. 아니다. Fix Agent는 확장 옵션이며 기본 구조에서는 원 담당 Domain Agent가 재작업한다.

Q. Review Loop는 언제 끝나?
A. Review Agent가 approve하거나 최대 반복 횟수에 도달하면 종료한다.

Q. Review Loop에서 무엇을 검증해?
A. Tool Result, Test Result, 코드 변경, Error Handling, Safe Execution Policy 준수 여부를 검증한다.

---

# 10. Failure Handling in Multi-Agent Workflow

## 10.1 Multi-Agent Failure Handling Concept

### [개념]

Multi-Agent Failure Handling은 Agent 작업 중 Tool 실패, 권한 실패, 차단, 일부 성공, Review 실패가 발생했을 때 Workflow를 안전하게 복구하는 기준이다.

Multi-Agent Workflow에서는 실패를 숨기지 않고 구조화해서 전달해야 한다.

실패 상태가 명확해야 PM Agent와 Review Agent가 재계획할 수 있다.

---

### [핵심]

- 실패 상태를 숨기지 않는다.
- Tool Result status를 유지한다.
- error, blocked, partial을 구분한다.
- PermissionError는 권한 재검토 또는 Agent 재배정이 필요하다.
- ValidationError는 Arguments 재생성이 필요하다.
- TimeoutError는 Retry / Idempotency 확인이 필요하다.
- blocked는 사용자 승인 또는 정책 재검토가 필요하다.
- partial은 성공 항목과 실패 항목을 분리한다.
- PM Agent는 실패 상태를 보고 재계획할 수 있다.
- Review Agent는 실패 처리의 적절성을 검증한다.

---

### [실무]

Failure Handling Flow:

```text
Tool Failure
→ Create Structured Tool Result
→ Agent Handoff with Failure
→ Review Agent Validation
→ PM Agent Replan if Needed
→ Retry / Reassign / Ask Confirmation / Stop
```

Failure 대응 기준:

| 상태                      | 의미                     | 대응                          |
| ------------------------- | ------------------------ | ----------------------------- |
| error                     | 검증 실패 또는 실행 실패 | Error Type 확인               |
| blocked                   | 정책 / 승인 필요         | Confirmation 또는 정책 재검토 |
| partial                   | 일부 성공                | 실패 항목만 보완              |
| PermissionError           | 권한 부족                | Agent 재배정 또는 권한 재검토 |
| ValidationError           | 입력값 문제              | Arguments 재생성              |
| TimeoutError              | 시간 초과                | Idempotency 확인 후 Retry     |
| RateLimitError            | 호출 제한                | Backoff 또는 fallback         |
| DangerousOperationBlocked | 위험 작업 차단           | 실행 중단 또는 수동 검토      |

실패 Handoff 예시:

```json
{
  "fromAgent": "devops-agent",
  "toAgent": "pm-agent",
  "task": "Deploy application to production.",
  "status": "blocked",
  "toolResults": [
    {
      "toolName": "deploy_application",
      "status": "blocked",
      "reason": "HumanConfirmationRequired",
      "message": "Production deployment requires user confirmation."
    }
  ],
  "requiresUserConfirmation": true
}
```

---

### [FAQ]

Q. Multi-Agent Workflow에서 실패가 발생하면 어떻게 해?
A. 실패를 숨기지 않고 Tool Result와 Agent Handoff에 error, blocked, partial 상태로 구조화해서 전달한다.

Q. blocked 상태는 실패야?
A. 아니다. 정책이나 승인 필요로 실행되지 않은 상태이며, 사용자 승인 또는 재계획이 필요하다.

Q. partial 상태는 어떻게 처리해?
A. 성공 항목과 실패 항목을 분리하고 실패 항목만 재시도하거나 보완한다.

Q. PermissionError가 발생하면 어떻게 해?
A. Agent 권한을 재검토하거나 적절한 Agent로 재배정한다.

Q. 실패가 반복되면 어떻게 해?
A. PM Agent가 범위를 줄이거나 Workflow를 재계획하고, 필요한 경우 사용자에게 현재 상태를 보고한다.

---

# 11. Tool Observability

## 11.1 Tool Observability Concept

### [개념]

Tool Observability는 Agent가 어떤 Tool을 언제, 왜, 어떤 Arguments로 호출했고 어떤 결과를 받았는지 추적하는 기준이다.

Tool Observability는 디버깅, 보안 감사, 성능 분석, Agent 품질 개선에 필요하다.

Tool Observability는 Audit Log보다 넓은 개념이며, Tool Calling 전체 흐름을 관측한다.

---

### [핵심]

- Tool Observability는 Tool 호출 추적이다.
- toolName, agentId, workflowId, taskId를 기록한다.
- status, errorType, executionTimeMs를 기록한다.
- retryCount와 timeout 여부를 기록한다.
- riskLevel과 confirmation 여부를 기록한다.
- blocked / partial 상태를 기록한다.
- Secret과 개인정보는 마스킹한다.
- Observability 데이터는 Troubleshooting과 Evaluation에 사용한다.
- Tool Observability는 Agent 성능 개선에 중요하다.

---

### [실무]

Tool Observability Log 예시:

```json
{
  "timestamp": "2026-07-01T12:00:00+09:00",
  "workflowId": "wf_001",
  "taskId": "task_backend_001",
  "agentId": "backend-agent",
  "toolName": "execute_test_suite",
  "status": "success",
  "executionTimeMs": 8420,
  "retryCount": 0,
  "riskLevel": "medium",
  "traceId": "trace_001"
}
```

Error Observability Log 예시:

```json
{
  "workflowId": "wf_001",
  "taskId": "task_frontend_001",
  "agentId": "frontend-agent",
  "toolName": "execute_frontend_test",
  "status": "partial",
  "errorType": "ExecutionError",
  "executionTimeMs": 22000,
  "retryCount": 1,
  "traceId": "trace_002"
}
```

Observability 지표:

| 지표             | 목적                    |
| ---------------- | ----------------------- |
| toolCallCount    | Tool 호출 수            |
| successRate      | 성공률                  |
| errorRate        | 실패율                  |
| blockedRate      | 차단 비율               |
| partialRate      | 일부 성공 비율          |
| averageLatency   | 평균 실행 시간          |
| timeoutRate      | Timeout 비율            |
| retryRate        | Retry 비율              |
| confirmationRate | Human Confirmation 비율 |

---

### [FAQ]

Q. Tool Observability가 뭐야?
A. Agent가 어떤 Tool을 호출했고 어떤 결과를 받았는지 추적하는 관측 기준이다.

Q. Observability에는 무엇을 기록해?
A. workflowId, taskId, agentId, toolName, status, errorType, executionTimeMs, retryCount, traceId를 기록한다.

Q. Audit Log와 Observability는 같아?
A. 다르다. Audit Log는 보안과 변경 이력 중심이고, Observability는 전체 Tool 호출 흐름 관측 중심이다.

Q. Tool Observability는 왜 필요해?
A. 디버깅, 성능 분석, 실패 원인 파악, Agent 품질 개선에 필요하다.

Q. Observability Log에 Secret을 넣어도 돼?
A. 안 된다. Secret, Token, Password, 개인정보는 마스킹해야 한다.

---

# 12. Agent Tool Routing Checklist

## 12.1 Routing Checklist

### [개념]

Agent Tool Routing Checklist는 Multi-Agent System에서 Agent와 Tool이 올바르게 연결되었는지 검수하는 기준이다.

이 Checklist는 PM Agent, Review Agent, Agent Runtime이 사용할 수 있다.

Routing Checklist는 Agent 권한, Tool 권한, Handoff, Shared State, Review Loop 누락을 방지한다.

---

### [핵심]

- 요청을 담당할 Agent가 명확한가?
- Agent 역할과 Tool이 일치하는가?
- Agent별 allowedTools가 정의되어 있는가?
- deniedTools가 정의되어 있는가?
- Permission Check가 Runtime에서 강제되는가?
- Risk Level이 Tool Definition에 있는가?
- High Risk Tool에 Human Confirmation이 있는가?
- Tool Result가 Handoff에 포함되는가?
- Shared State에 필요한 상태가 저장되는가?
- Review Agent가 결과를 검증하는가?
- 실패 상태가 숨겨지지 않는가?
- Fix 작업은 원 담당 Domain Agent로 돌아가는가?

---

### [실무]

Agent Tool Routing Checklist:

```md
### [Checklist]

- [ ] 사용자 요청을 분석했는가?
- [ ] 요청을 담당할 Agent를 선택했는가?
- [ ] Agent 역할과 요청이 일치하는가?
- [ ] Agent가 사용할 Tool이 allowedTools에 포함되어 있는가?
- [ ] Tool이 deniedTools에 포함되어 있지 않은가?
- [ ] Tool Definition에 permissionLevel이 있는가?
- [ ] Tool Definition에 riskLevel이 있는가?
- [ ] Tool Definition에 sideEffect 여부가 있는가?
- [ ] Permission Check가 Runtime에서 강제되는가?
- [ ] High Risk Tool에 Human Confirmation이 적용되는가?
- [ ] Tool Result가 success / error / blocked / partial을 구분하는가?
- [ ] Tool Result가 Agent Handoff에 포함되는가?
- [ ] blocked / partial 상태를 숨기지 않았는가?
- [ ] Shared State에 workflowId와 taskId가 유지되는가?
- [ ] Review Agent가 결과를 검증하는가?
- [ ] 수정이 필요한 경우 원 담당 Domain Agent에게 재작업을 요청하는가?
- [ ] Fix Agent를 기본 전제로 두지 않았는가?
- [ ] Final Output 전에 Review 결과를 반영했는가?
```

Checklist 실패 시 Routing Rule 또는 Agent Permission을 수정한다.

---

### [FAQ]

Q. Agent Tool Routing Checklist는 왜 필요해?
A. Multi-Agent System에서 Agent 역할, Tool 권한, Handoff, Review Loop 누락을 막기 위해 필요하다.

Q. 가장 중요한 Checklist 항목은?
A. Agent 역할 일치, allowedTools 확인, Permission Check, Risk Level, Human Confirmation, Review 검증이다.

Q. Fix Agent를 기본 구조로 둬야 해?
A. 아니다. 기본 구조에서는 원 담당 Domain Agent가 재작업하고, Fix Agent는 확장 옵션으로만 둔다.

Q. Routing 실패 시 어떻게 해?
A. PM Agent가 Agent를 재배정하거나 Tool Permission을 재검토해야 한다.

Q. Final Output 전에 무엇을 확인해야 해?
A. Tool Result, Review 결과, blocked / partial 상태, knownIssues를 확인해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Agent Tool Routing이 뭐야?
A. 사용자 요청을 어떤 Agent가 처리하고 어떤 Tool을 사용할지 결정하는 절차다.

Q. Multi-Agent System에서 Tool Calling은 어떻게 동작해?
A. PM Agent가 요청을 분석하고 Domain Agent가 Tool을 사용해 작업하며 Review Agent가 결과를 검증하는 방식으로 동작한다.

Q. Agent별 Tool 권한은 왜 필요해?
A. 최소 권한 원칙을 적용해 오작동, 보안 사고, 데이터 손실을 줄이기 위해 필요하다.

Q. allowedTools와 deniedTools는 뭐야?
A. allowedTools는 Agent가 사용할 수 있는 Tool 목록이고 deniedTools는 명시적으로 금지된 Tool 목록이다.

Q. PM Agent는 어떤 Tool을 사용해야 해?
A. RAG Search, Task Routing, Progress Read, Result Summary 같은 낮은 위험 Tool을 사용하는 것이 적절하다.

Q. PM Agent가 위험 Tool을 직접 실행해도 돼?
A. 권장하지 않는다. 위험 Tool은 Domain Agent와 Safe Execution Policy를 통해 처리해야 한다.

Q. Backend Agent는 어떤 Tool을 사용해?
A. Backend RAG Search, File Read, File Write, DB Read, Test Tool을 사용할 수 있다.

Q. Frontend Agent는 어떤 Tool을 사용해?
A. Frontend RAG Search, File Read, File Write, Component Search, Frontend Test Tool을 사용할 수 있다.

Q. DevOps Agent는 어떤 Tool을 사용해?
A. Log Search, Infra Status, Deploy Status, Deploy Tool을 제한적으로 사용할 수 있다.

Q. AI/ML Agent는 어떤 Tool을 사용해?
A. RAG Search, Vector Search, Retrieval Evaluation, Query Rewrite, Embedding Config Tool을 사용할 수 있다.

Q. Review Agent는 어떤 Tool을 사용해?
A. RAG Search, File Read, Static Analysis, Test Result Read, Diff Compare, Audit Log Inspect Tool을 사용할 수 있다.

Q. Review Agent가 직접 수정해도 돼?
A. 기본적으로 권장하지 않는다. Review Agent는 검증하고 수정은 원 담당 Domain Agent가 수행하는 것이 좋다.

Q. Fix Agent는 필수야?
A. 아니다. Fix Agent는 확장 옵션이고 기본 구조에서는 원 담당 Domain Agent가 재작업한다.

Q. Agent Handoff가 뭐야?
A. 한 Agent가 수행한 작업 결과를 다음 Agent에게 전달하는 구조다.

Q. Agent Handoff에는 무엇이 들어가야 해?
A. fromAgent, toAgent, task, status, toolResults, changedFiles, knownIssues, requiresReview가 들어가면 좋다.

Q. Tool Result를 Handoff에 포함해야 해?
A. 포함해야 한다. 다음 Agent가 결과와 실패 상태를 검증하기 위해 필요하다.

Q. blocked 상태도 Handoff에 넣어야 해?
A. 반드시 넣어야 한다. 사용자 승인이나 정책 재검토가 필요할 수 있기 때문이다.

Q. partial 상태도 Handoff에 넣어야 해?
A. 반드시 넣어야 한다. 성공 항목과 실패 항목을 구분해 후속 처리를 해야 한다.

Q. Shared State가 뭐야?
A. 여러 Agent가 공유하는 workflowId, taskId, Tool Result, Review Result, Approval Scope 같은 공통 상태다.

Q. Shared State에 Secret을 저장해도 돼?
A. 안 된다. API Key, Password, Token, Raw Secret File은 저장하지 않는다.

Q. Review Loop가 뭐야?
A. Domain Agent 작업을 Review Agent가 검증하고 문제가 있으면 원 담당 Agent가 수정한 뒤 다시 검증하는 구조다.

Q. Review Loop는 언제 끝나?
A. Review Agent가 approve하거나 최대 반복 횟수에 도달하면 종료한다.

Q. Multi-Agent Workflow에서 실패가 발생하면 어떻게 해?
A. error, blocked, partial 상태를 Tool Result와 Agent Handoff에 구조화해서 전달하고 PM Agent가 재계획한다.

Q. PermissionError가 발생하면 어떻게 해?
A. Agent 권한을 재검토하거나 적절한 Agent로 재배정한다.

Q. DangerousOperationBlocked가 발생하면 어떻게 해?
A. 위험 작업을 실행하지 않고 사용자 확인 또는 수동 검토로 넘긴다.

Q. Tool Observability가 뭐야?
A. Agent가 어떤 Tool을 언제, 왜 호출했고 어떤 결과를 받았는지 추적하는 기준이다.

Q. Tool Observability에는 무엇을 기록해?
A. workflowId, taskId, agentId, toolName, status, errorType, executionTimeMs, retryCount, riskLevel, traceId를 기록한다.

Q. Audit Log와 Observability는 달라?
A. 다르다. Audit Log는 보안과 변경 이력 중심이고 Observability는 Tool 호출 흐름과 성능 관측 중심이다.

Q. Agent Tool Routing Checklist에는 무엇이 들어가야 해?
A. Agent 역할 일치, allowedTools, deniedTools, permissionLevel, riskLevel, Human Confirmation, Tool Result Handoff, Review 검증을 확인해야 한다.

Q. Agent Tool Routing의 최종 목표는 뭐야?
A. Multi-Agent System에서 각 Agent가 자신의 역할과 권한 안에서 Tool을 안전하게 사용하고 검증 가능한 결과를 전달하게 만드는 것이다.
