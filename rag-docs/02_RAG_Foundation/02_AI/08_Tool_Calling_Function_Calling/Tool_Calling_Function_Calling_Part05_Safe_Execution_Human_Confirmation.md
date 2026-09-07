# Tool Calling & Function Calling Part05 - Safe Execution & Human Confirmation

---

# 1. Safe Tool Execution

## 1.1 Safe Tool Execution Concept

### [개념]

Safe Tool Execution은 LLM이 생성한 Tool Call을 그대로 실행하지 않고, 검증, 권한 확인, 위험도 판단, 사용자 승인 절차를 거쳐 안전하게 실행하는 구조이다.

Tool Calling은 외부 시스템에 실제 영향을 줄 수 있다.

따라서 Tool Execution은 항상 안전 실행 기준을 포함해야 한다.

LLM Output은 실행 명령이 아니라 검증 대상이다.

---

### [핵심]

- Safe Tool Execution은 Tool 실행 전 안전성을 확인하는 구조이다.
- LLM이 생성한 Tool Arguments는 신뢰하지 않는다.
- Tool Arguments는 Schema Validation을 통과해야 한다.
- Tool Arguments는 Business Validation을 통과해야 한다.
- Agent 권한과 User 권한을 확인한다.
- Side Effect 여부를 확인한다.
- Risk Level에 따라 자동 실행, 로그, 사용자 확인을 결정한다.
- 위험 작업은 Human Confirmation 없이 실행하지 않는다.
- Tool Result는 success, error, blocked, partial로 구조화한다.
- Safe Tool Execution은 Agent Runtime에서 강제한다.

---

### [실무]

2026 실무 기준 Safe Tool Execution 기본 Flow:

```text
LLM Tool Call
→ Validate Arguments
→ Check Permission
→ Check Risk Level
→ Check Side Effect
→ Require Human Confirmation if Needed
→ Execute Tool
→ Capture Result
→ Return Structured Tool Result
```

위험도 기준:

```text
Low Risk
→ Auto Execute

Medium Risk
→ Validate + Log

High Risk
→ Human Confirmation Required
```

Safe Tool Execution에서 금지되는 방식:

- LLM이 생성한 Shell Command 즉시 실행
- LLM이 생성한 SQL 즉시 실행
- LLM이 생성한 파일 경로 그대로 삭제
- 사용자 확인 없이 이메일 발송
- 사용자 확인 없이 결제 요청
- 사용자 확인 없이 배포 실행
- Tool 실패를 성공처럼 반환
- Raw Exception 또는 Secret 노출
- blocked 상태를 success로 처리

---

### [FAQ]

Q. Safe Tool Execution이 뭐야?
A. LLM이 만든 Tool Call을 검증, 권한 확인, 위험도 판단 후 안전하게 실행하는 구조다.

Q. LLM이 생성한 Tool Arguments를 그대로 실행해도 돼?
A. 안 된다. LLM Output은 실행 명령이 아니라 검증 대상이다.

Q. Safe Tool Execution에서 가장 중요한 기준은?
A. 입력값 검증, 권한 확인, 위험도 판단, Human Confirmation이다.

Q. 위험 작업은 언제 실행해?
A. 사용자에게 변경 내용과 위험을 보여주고 명시적 승인을 받은 뒤 실행한다.

Q. Safe Tool Execution 실패 시 어떻게 해?
A. Tool을 실행하지 않고 error 또는 blocked 상태의 Tool Result를 반환한다.

---

# 2. Risk Level

## 2.1 Risk Level Classification

### [개념]

Risk Level은 Tool Execution이 시스템, 데이터, 비용, 사용자 계정, 외부 서비스에 미치는 영향을 기준으로 위험도를 분류하는 기준이다.

Risk Level은 Tool 실행 방식과 Human Confirmation 필요 여부를 결정한다.

Risk Level은 Tool Definition, Safe Execution Policy, Agent Tool Permission과 연결된다.

---

### [핵심]

- Risk Level은 low, medium, high로 분류할 수 있다.
- Low Risk Tool은 읽기, 검색, 검증 중심이다.
- Medium Risk Tool은 파일 쓰기, 설정 변경, 제한된 수정 작업이다.
- High Risk Tool은 삭제, 결제, 발송, 배포, DB 변경, 계정 변경 작업이다.
- Side Effect가 큰 작업은 High Risk로 분류한다.
- Non-Idempotent 작업은 High Risk로 분류하는 것이 안전하다.
- Risk Level은 Tool Definition에 포함한다.
- Risk Level에 따라 실행 전 승인 정책이 달라진다.
- Risk Level은 Agent Runtime에서 강제해야 한다.

---

### [실무]

Risk Level 예시:

| Risk Level | 설명                                           | 처리               |
| ---------- | ---------------------------------------------- | ------------------ |
| low        | 읽기 / 검색 / 계산 / 검증                      | Auto Execute       |
| medium     | 제한된 쓰기 / Append / 임시 파일 생성          | Validate + Log     |
| high       | 삭제 / 덮어쓰기 / 발송 / 결제 / 배포 / DB 변경 | Human Confirmation |

Tool별 Risk Level:

| Tool                   | Risk Level    | 이유                         |
| ---------------------- | ------------- | ---------------------------- |
| search_rag_documents   | low           | 검색만 수행                  |
| read_project_file      | low           | 읽기 중심                    |
| calculate_expression   | low           | 계산만 수행                  |
| append_project_file    | medium        | 기존 파일에 내용 추가        |
| write_project_file     | medium ~ high | 파일 생성 또는 덮어쓰기 가능 |
| delete_project_file    | high          | 데이터 손실 가능             |
| execute_database_write | high          | DB 상태 변경                 |
| send_email_message     | high          | 외부 발송                    |
| request_payment        | high          | 비용 발생                    |
| deploy_application     | high          | 운영 환경 변경               |

Risk Level 판단 Flow:

```text
Tool Call
→ Has Side Effect?
→ Changes External State?
→ Can Be Undone?
→ Is Non-Idempotent?
→ Has Cost or Account Impact?
→ Decide Risk Level
```

---

### [FAQ]

Q. Risk Level이 뭐야?
A. Tool 실행이 시스템, 데이터, 비용, 외부 서비스에 미치는 영향을 기준으로 나눈 위험도다.

Q. Low Risk Tool은 자동 실행해도 돼?
A. 일반적으로 가능하지만 입력값 검증과 권한 확인은 필요하다.

Q. High Risk Tool에는 뭐가 있어?
A. 파일 삭제, 파일 덮어쓰기, DB 변경, 이메일 발송, 결제 요청, 배포, 계정 변경 작업이 있다.

Q. Medium Risk Tool은 어떻게 처리해?
A. 입력값 검증, 권한 확인, 로그 기록을 적용하고 상황에 따라 사용자 확인을 요구한다.

Q. Risk Level은 어디에 정의해?
A. Tool Definition과 Agent Runtime의 Tool Policy에 정의하는 것이 좋다.

---

# 3. Side Effect Control

## 3.1 Side Effect Control Concept

### [개념]

Side Effect Control은 Tool 실행이 외부 시스템이나 데이터 상태를 변경하는 경우, 변경 범위와 실행 조건을 통제하는 기준이다.

Side Effect가 있는 Tool은 실행 전 영향 범위를 확인해야 한다.

Side Effect가 큰 작업은 Human Confirmation이 필요하다.

---

### [핵심]

- Side Effect는 외부 상태 변경이다.
- 파일 생성, 수정, 삭제는 Side Effect다.
- DB INSERT, UPDATE, DELETE는 Side Effect다.
- 이메일 발송, 결제 요청, 배포 실행은 Side Effect다.
- Side Effect Tool은 Preview를 제공하는 것이 좋다.
- Side Effect Tool은 Audit Log를 남긴다.
- Side Effect Tool은 Retry 시 중복 실행 위험이 있다.
- Side Effect Tool은 Undo 가능 여부를 확인한다.
- Side Effect Tool은 Approval Scope를 벗어나면 실행하지 않는다.

---

### [실무]

Side Effect 분류:

| 작업           | Side Effect | 처리                   |
| -------------- | ----------- | ---------------------- |
| 파일 읽기      | 없음        | Auto Execute           |
| 파일 Append    | 있음        | Validate + Log         |
| 파일 Overwrite | 있음        | Confirmation           |
| 파일 Delete    | 있음        | Confirmation           |
| DB SELECT      | 없음        | Validate + Limit       |
| DB INSERT      | 있음        | Confirmation           |
| DB UPDATE      | 있음        | Confirmation           |
| DB DELETE      | 있음        | Confirmation           |
| Email Send     | 있음        | Preview + Confirmation |
| Deployment     | 있음        | Approval + Audit Log   |

Side Effect Control Flow:

```text
Tool Call
→ Detect Side Effect
→ Identify Target
→ Estimate Impact
→ Check Undo Option
→ Preview Change
→ Human Confirmation
→ Execute
→ Audit Log
```

Side Effect Tool Result에는 다음 metadata를 포함할 수 있다.

```json
{
  "metadata": {
    "sideEffect": true,
    "target": "docs/tool-calling.md",
    "operation": "overwrite",
    "requiresConfirmation": true,
    "undoAvailable": true
  }
}
```

---

### [FAQ]

Q. Side Effect가 뭐야?
A. Tool 실행이 파일, DB, 이메일, 결제, 배포처럼 외부 상태를 변경하는 효과다.

Q. Side Effect Tool은 왜 조심해야 해?
A. 데이터 손실, 중복 발송, 중복 결제, 운영 장애 같은 문제가 발생할 수 있기 때문이다.

Q. Side Effect Tool 실행 전 무엇을 확인해야 해?
A. 대상, 변경 내용, 영향 범위, Undo 가능 여부, 사용자 승인 여부를 확인해야 한다.

Q. DB UPDATE는 Side Effect야?
A. 맞다. DB 상태를 변경하므로 Side Effect가 있는 High Risk 작업이다.

Q. Side Effect Tool은 Retry해도 돼?
A. 신중해야 한다. Idempotency Key나 상태 확인 없이 Retry하면 중복 실행 위험이 있다.

---

# 4. Human Confirmation

## 4.1 Human Confirmation Concept

### [개념]

Human Confirmation은 위험 Tool 실행 전에 사용자에게 작업 내용, 대상, 영향 범위, 위험, Preview를 보여주고 명시적 승인을 받는 절차이다.

Human Confirmation은 High Risk Tool을 자동 실행하지 않기 위한 안전 장치이다.

Human Confirmation이 필요한 작업은 승인 전 status: blocked로 처리한다.

---

### [핵심]

- Human Confirmation은 위험 작업 전 사용자 승인 절차이다.
- 파일 삭제, 파일 덮어쓰기, DB 변경은 Human Confirmation 대상이다.
- 이메일 발송, 결제, 배포는 Human Confirmation 대상이다.
- Confirmation에는 Action Summary가 필요하다.
- Confirmation에는 Target과 Impact가 필요하다.
- Confirmation에는 Preview가 필요하다.
- Confirmation에는 Confirm / Cancel 선택이 필요하다.
- 승인 전에는 Tool을 실행하지 않는다.
- 승인 범위를 넘어서는 추가 작업은 실행하지 않는다.
- 승인 결과는 Audit Log와 Agent Handoff에 남길 수 있다.

---

### [실무]

Human Confirmation이 필요한 작업:

| 작업                 | 이유                    |
| -------------------- | ----------------------- |
| File Delete          | 복구 어려움             |
| File Overwrite       | 기존 내용 손실 가능     |
| Database Write       | 데이터 상태 변경        |
| Email Send           | 외부 발송               |
| Payment Request      | 비용 발생               |
| Deployment           | 운영 환경 변경          |
| Account Modification | 권한 / 사용자 정보 변경 |
| Shell Command        | 시스템 영향 가능        |

Human Confirmation Prompt 예시:

```text
다음 작업은 파일을 덮어씁니다.

대상:
- docs/tool-calling.md

변경:
- 기존 파일 내용을 새 내용으로 교체

위험:
- 기존 내용이 사라질 수 있음

Preview:
- 변경 전/후 diff 확인 필요

실행할까요?
```

Human Confirmation Required Result 예시:

```json
{
  "status": "blocked",
  "reason": "HumanConfirmationRequired",
  "message": "File overwrite requires user confirmation.",
  "requiredAction": {
    "type": "confirm",
    "target": "docs/tool-calling.md",
    "operation": "overwrite"
  }
}
```

---

### [FAQ]

Q. Human Confirmation이 뭐야?
A. 위험 Tool 실행 전에 사용자에게 작업 내용과 위험을 보여주고 명시적 승인을 받는 절차다.

Q. Human Confirmation은 언제 필요해?
A. 삭제, 덮어쓰기, DB 변경, 이메일 발송, 결제, 배포처럼 되돌리기 어렵거나 외부 영향을 주는 작업 전에 필요하다.

Q. 사용자 승인이 없으면 어떻게 해?
A. Tool을 실행하지 않고 blocked 상태를 반환한다.

Q. 승인 후 다른 작업까지 실행해도 돼?
A. 안 된다. 사용자가 승인한 범위 안의 작업만 실행해야 한다.

Q. Human Confirmation에는 무엇을 보여줘야 해?
A. 대상, 작업 내용, 영향 범위, 위험, Preview, Undo 가능 여부를 보여줘야 한다.

---

# 5. Preview and Dry Run

## 5.1 Preview and Dry Run Concept

### [개념]

Preview는 실제 실행 전에 변경 대상과 변경 내용을 사용자에게 보여주는 절차이다.

Dry Run은 실제 변경 없이 실행될 작업을 시뮬레이션하는 절차이다.

Preview와 Dry Run은 Human Confirmation의 품질을 높인다.

---

### [핵심]

- Preview는 실행 전 변경 내용을 보여준다.
- Dry Run은 실제 변경 없이 결과를 예측한다.
- 파일 수정은 diff preview가 유용하다.
- DB 변경은 affected rows preview가 필요하다.
- 이메일 발송은 수신자, 제목, 본문 preview가 필요하다.
- 배포는 대상 환경과 변경 버전 preview가 필요하다.
- Dry Run 결과는 실제 실행 결과와 다를 수 있음을 표시한다.
- Preview 없이 High Risk Tool을 실행하지 않는다.
- Preview는 승인 범위와 함께 저장할 수 있다.

---

### [실무]

File Write Preview:

```text
Target:
- docs/tool-calling.md

Operation:
- overwrite

Diff Preview:
- removed: old section
- added: new section
```

Database Write Dry Run:

```json
{
  "status": "success",
  "data": {
    "operation": "UPDATE",
    "table": "users",
    "estimatedAffectedRows": 3,
    "whereClause": "user_id IN (1, 2, 3)"
  },
  "metadata": {
    "dryRun": true
  }
}
```

Email Preview:

```text
To:
- user@example.com

Subject:
- Project Update

Body Preview:
- 안녕하세요. 프로젝트 진행 상황 공유드립니다...
```

Preview / Dry Run Flow:

```text
High Risk Tool Call
→ Validate Arguments
→ Generate Preview or Dry Run
→ Show Action Summary
→ Human Confirmation
→ Execute Actual Tool
```

---

### [FAQ]

Q. Preview가 뭐야?
A. 실제 실행 전에 변경 대상과 변경 내용을 사용자에게 보여주는 절차다.

Q. Dry Run이 뭐야?
A. 실제 변경 없이 어떤 작업이 실행될지 시뮬레이션하는 절차다.

Q. 파일 수정에는 어떤 Preview가 좋아?
A. 변경 전/후 diff preview가 좋다.

Q. DB 변경에는 어떤 Dry Run이 필요해?
A. 대상 테이블, 조건, 예상 affected rows를 보여주는 Dry Run이 필요하다.

Q. Preview 없이 위험 작업을 실행해도 돼?
A. 안 된다. High Risk Tool은 Preview와 Human Confirmation 후 실행하는 것이 안전하다.

---

# 6. Approval Scope

## 6.1 Approval Scope Concept

### [개념]

Approval Scope는 사용자가 승인한 작업의 범위이다.

Human Confirmation을 받은 뒤에도 Tool은 승인된 대상, 작업, 조건 안에서만 실행해야 한다.

승인 범위를 넘어서는 추가 작업은 새 확인을 받아야 한다.

---

### [핵심]

- Approval Scope는 승인된 작업 범위이다.
- 승인 대상 파일, DB, API, 이메일 수신자를 명확히 한다.
- 승인된 operation만 실행한다.
- 승인된 횟수만 실행한다.
- 승인된 시간 또는 세션 범위를 제한할 수 있다.
- 추가 작업이 필요하면 새 Confirmation을 받는다.
- 모호한 동의는 승인으로 처리하지 않는다.
- 승인 기록은 Audit Log에 남긴다.
- Approval Scope는 Agent Handoff와 Shared State에 포함할 수 있다.

---

### [실무]

Approval Scope 예시:

```json
{
  "approvalScope": {
    "toolName": "write_project_file",
    "operation": "overwrite",
    "target": "docs/tool-calling.md",
    "allowedOnce": true,
    "expiresAt": "2026-07-01T12:00:00+09:00"
  }
}
```

승인 범위 위반 예시:

| 승인된 작업        | 실행하려는 작업    | 처리         |
| ------------------ | ------------------ | ------------ |
| file A overwrite   | file B overwrite   | 새 승인 필요 |
| email draft create | email send         | 새 승인 필요 |
| DB SELECT          | DB UPDATE          | 새 승인 필요 |
| staging deploy     | production deploy  | 새 승인 필요 |
| one-time execution | repeated execution | 새 승인 필요 |

Approval Scope Check Flow:

```text
User Approval
→ Store Approval Scope
→ Before Execution Check Scope
→ Execute Only Approved Action
→ Reject Out-of-Scope Action
```

---

### [FAQ]

Q. Approval Scope가 뭐야?
A. 사용자가 승인한 Tool 실행의 대상, 작업, 조건 범위다.

Q. 사용자가 파일 A 수정을 승인했으면 파일 B도 수정해도 돼?
A. 안 된다. 승인 범위를 벗어나므로 새 확인이 필요하다.

Q. “ㅇㅋ” 같은 짧은 답변도 승인으로 봐도 돼?
A. 직전 Confirmation 내용이 명확하면 가능하지만, 대상이나 작업이 모호하면 다시 확인해야 한다.

Q. 이메일 초안 생성을 승인했으면 발송도 해도 돼?
A. 안 된다. 초안 생성과 발송은 위험도가 다르므로 발송은 별도 승인이 필요하다.

Q. Approval Scope는 로그에 남겨야 해?
A. 위험 작업은 승인 범위와 실행 결과를 Audit Log에 남기는 것이 좋다.

---

# 7. Audit Log

## 7.1 Audit Log Concept

### [개념]

Audit Log는 Tool Execution의 중요한 실행 내역을 추적하기 위해 남기는 기록이다.

Audit Log는 위험 작업, Side Effect 작업, 권한 관련 작업, 실패 및 차단 이벤트를 추적하는 데 사용한다.

Audit Log는 디버깅, 보안 감사, 사고 분석에 필요하다.

---

### [핵심]

- Audit Log는 Tool 실행 추적 기록이다.
- High Risk Tool은 Audit Log를 남긴다.
- Side Effect Tool은 Audit Log를 남긴다.
- PermissionError와 Blocked Result도 기록한다.
- Audit Log에는 Tool Name, Agent ID, User ID, Target, Action, Status를 포함할 수 있다.
- Secret, Token, 개인정보는 마스킹한다.
- 전체 파일 내용이나 민감 데이터는 로그에 남기지 않는다.
- Audit Log는 변경 전후 추적에 유용하다.
- Audit Log는 Tool Observability와 연결된다.

---

### [실무]

Audit Log 예시:

```json
{
  "traceId": "trace_20260701_001",
  "toolName": "write_project_file",
  "agentId": "backend-agent",
  "userId": "user_001",
  "action": "overwrite",
  "target": "docs/tool-calling.md",
  "riskLevel": "high",
  "approvalRequired": true,
  "approvalReceived": true,
  "status": "success",
  "executionTimeMs": 31
}
```

Audit Log 금지 예시:

```json
{
  "apiKey": "sk-secret-key",
  "password": "plain-password",
  "fullFileContent": "..."
}
```

Audit Log 대상:

| 이벤트                    | 로그 필요 |
| ------------------------- | --------- |
| High Risk Tool 실행       | 필요      |
| DB Write 실행             | 필요      |
| Email Send 실행           | 필요      |
| Deployment 실행           | 필요      |
| PermissionError           | 필요      |
| DangerousOperationBlocked | 필요      |
| Human Confirmation        | 필요      |
| Low Risk 검색             | 선택      |

---

### [FAQ]

Q. Audit Log가 뭐야?
A. Tool 실행 내역을 추적하기 위해 남기는 기록이다.

Q. 어떤 Tool에 Audit Log가 필요해?
A. 삭제, DB 변경, 이메일 발송, 결제, 배포 같은 High Risk Tool에 필요하다.

Q. Audit Log에는 무엇을 남겨야 해?
A. Tool Name, Agent ID, User ID, Target, Action, Risk Level, Approval 여부, Status, Trace ID를 남길 수 있다.

Q. Audit Log에 Secret을 남겨도 돼?
A. 안 된다. API Key, Token, Password, 개인정보는 마스킹해야 한다.

Q. Blocked Result도 로그에 남겨야 해?
A. 위험 작업 차단이나 권한 위반은 보안 감사에 필요하므로 남기는 것이 좋다.

---

# 8. Dangerous Operation

## 8.1 Dangerous Operation Control

### [개념]

Dangerous Operation은 Tool 실행 시 데이터 손실, 보안 사고, 비용 발생, 운영 장애, 외부 발송, 권한 변경을 일으킬 수 있는 작업이다.

Dangerous Operation은 기본적으로 자동 실행하지 않는다.

Dangerous Operation은 차단, Preview, Human Confirmation, Audit Log를 적용한다.

---

### [핵심]

- Dangerous Operation은 High Risk 작업이다.
- 파일 삭제와 덮어쓰기는 Dangerous Operation이다.
- DELETE / UPDATE without WHERE는 Dangerous Operation이다.
- Shell Command 실행은 Dangerous Operation이다.
- 이메일 발송, 결제, 배포는 Dangerous Operation이다.
- 계정 권한 변경은 Dangerous Operation이다.
- Dangerous Operation은 Human Confirmation이 필요하다.
- 일부 작업은 Human Confirmation이 있어도 정책상 차단할 수 있다.
- Dangerous Operation 차단 결과는 status: blocked로 반환한다.

---

### [실무]

Dangerous Operation 예시:

| 작업                          | 위험             |
| ----------------------------- | ---------------- |
| rm -rf 실행                   | 파일 시스템 손상 |
| DELETE FROM users             | 전체 데이터 삭제 |
| UPDATE users SET role='ADMIN' | 권한 상승        |
| 결제 API 호출                 | 비용 발생        |
| 이메일 대량 발송              | 스팸 / 오발송    |
| Production Deploy             | 서비스 장애      |
| Secret 파일 읽기              | 보안 사고        |

Dangerous Operation 차단 예시:

```json
{
  "status": "blocked",
  "reason": "DangerousOperationBlocked",
  "message": "DELETE without WHERE is not allowed.",
  "metadata": {
    "toolName": "execute_database_write",
    "riskLevel": "high"
  }
}
```

Dangerous Operation Check Flow:

```text
Tool Call
→ Detect Dangerous Pattern
→ Block or Require Confirmation
→ Generate Preview
→ Audit Log
```

위험 패턴 예시:

```text
rm -rf /
DELETE FROM table
UPDATE table SET value
DROP TABLE
chmod 777
curl | sh
```

---

### [FAQ]

Q. Dangerous Operation이 뭐야?
A. 데이터 손실, 보안 사고, 비용 발생, 운영 장애, 외부 발송을 일으킬 수 있는 위험 작업이다.

Q. DELETE without WHERE는 왜 위험해?
A. 조건 없이 전체 데이터를 삭제할 수 있기 때문이다.

Q. Shell Command Tool은 왜 위험해?
A. 파일 시스템, 네트워크, Secret, 권한에 직접 영향을 줄 수 있기 때문이다.

Q. Dangerous Operation은 승인만 받으면 항상 실행해도 돼?
A. 아니다. 정책상 금지된 작업은 승인 여부와 관계없이 차단해야 한다.

Q. Dangerous Operation은 어떻게 감지해?
A. 명령 패턴, SQL 패턴, Tool Risk Level, Side Effect, 대상 리소스를 기준으로 감지한다.

---

# 9. Safe Execution Policy

## 9.1 Safe Execution Policy Design

### [개념]

Safe Execution Policy는 Tool 실행 전후에 적용되는 보안, 권한, 위험도, 승인, 로그 기준을 문서화한 정책이다.

Safe Execution Policy는 Agent Runtime이 일관되게 Tool을 통제하기 위한 기준이다.

Prompt만으로는 Safe Execution을 보장할 수 없으므로 Runtime Policy가 필요하다.

---

### [핵심]

- Safe Execution Policy는 Runtime에서 강제한다.
- Prompt만으로 안전 실행을 보장하지 않는다.
- Tool별 Risk Level을 정의한다.
- Agent별 Permission을 정의한다.
- Side Effect Tool의 승인 기준을 정의한다.
- Dangerous Operation 차단 기준을 정의한다.
- Retry 가능 여부와 Idempotency 기준을 정의한다.
- Audit Log 기준을 정의한다.
- Error Result와 Blocked Result 형식을 정의한다.
- 정책이 없는 Tool은 기본 차단하는 것이 안전하다.

---

### [실무]

Safe Execution Policy 예시:

```json
{
  "toolPolicy": {
    "read_project_file": {
      "riskLevel": "low",
      "requiresConfirmation": false,
      "allowedAgents": ["backend-agent", "review-agent", "pm-agent"]
    },
    "write_project_file": {
      "riskLevel": "high",
      "requiresConfirmation": true,
      "allowedAgents": ["backend-agent", "frontend-agent"],
      "requiresPreview": true,
      "auditLog": true
    },
    "deploy_application": {
      "riskLevel": "high",
      "requiresConfirmation": true,
      "allowedAgents": ["devops-agent"],
      "requiresApprovalScope": true,
      "auditLog": true
    }
  }
}
```

Policy Evaluation Flow:

```text
Tool Call
→ Match Tool Policy
→ Check Agent Permission
→ Check Risk Level
→ Check Confirmation Requirement
→ Execute / Block
```

Policy가 없으면 안전한 기본값은 차단이다.

```text
Unknown Tool Policy
→ Block Execution
```

---

### [FAQ]

Q. Safe Execution Policy가 뭐야?
A. Tool 실행을 통제하기 위한 권한, 위험도, 승인, 로그, 차단 기준이다.

Q. Safe Execution Policy는 어디서 적용해?
A. Agent Runtime 또는 Backend System에서 강제해야 한다.

Q. Prompt만으로 Safe Execution을 보장할 수 있어?
A. 아니다. Prompt는 보조 수단이고 실제 통제는 Runtime Policy가 담당해야 한다.

Q. Tool Policy가 없는 Tool은 어떻게 처리해?
A. 안전한 기본값으로 실행을 차단하는 것이 좋다.

Q. Safe Execution Policy의 핵심 항목은?
A. allowedAgents, riskLevel, requiresConfirmation, requiresPreview, auditLog, blockedPatterns다.

---

# 10. Safe Execution Checklist

## 10.1 Safety Checklist

### [개념]

Safe Execution Checklist는 Tool을 실행하기 전 안전 기준을 빠짐없이 확인하기 위한 검수 목록이다.

Checklist는 Tool 연결 전, Tool 실행 전, Review Agent 검토 단계에서 사용할 수 있다.

Safe Execution Checklist는 Final Integration Checklist와 연결된다.

---

### [핵심]

- Tool Risk Level이 정의되었는가?
- Side Effect 여부가 정의되었는가?
- Agent Permission이 정의되었는가?
- Tool Arguments Validation이 있는가?
- Dangerous Operation 감지가 있는가?
- Human Confirmation 필요 여부가 정의되었는가?
- Preview 또는 Dry Run이 가능한가?
- Approval Scope가 제한되어 있는가?
- Timeout이 설정되어 있는가?
- Retry와 Idempotency 기준이 있는가?
- Audit Log 기준이 있는가?
- Error / Blocked Result 구조가 정의되었는가?

---

### [실무]

Safe Execution Checklist:

```md
### [Checklist]

- [ ] Tool Definition에 riskLevel이 있는가?
- [ ] Tool Definition에 sideEffect 여부가 있는가?
- [ ] Tool Definition에 permissionLevel이 있는가?
- [ ] Agent별 allowedTools가 정의되어 있는가?
- [ ] Tool Arguments Schema Validation이 있는가?
- [ ] Business Validation이 있는가?
- [ ] Path Traversal 방지가 있는가?
- [ ] SQL Injection 방지가 있는가?
- [ ] Command Injection 방지가 있는가?
- [ ] Dangerous Operation 감지 규칙이 있는가?
- [ ] High Risk Tool에 Human Confirmation이 적용되는가?
- [ ] Preview 또는 Dry Run을 제공하는가?
- [ ] Approval Scope를 저장하고 검증하는가?
- [ ] Timeout이 설정되어 있는가?
- [ ] Retry 정책이 Idempotency 기준과 연결되어 있는가?
- [ ] Side Effect Tool에 Audit Log가 있는가?
- [ ] Secret / Token / 개인정보가 로그에 남지 않는가?
- [ ] Tool Result가 success / error / blocked / partial을 구분하는가?
- [ ] Blocked Result에 reason과 requiredAction이 있는가?
- [ ] User Facing Error Message가 안전한가?
```

Checklist 실패 시 Tool Execution을 허용하지 않는다.

---

### [FAQ]

Q. Safe Execution Checklist는 왜 필요해?
A. Tool 실행 전 보안, 권한, 위험도, 승인 기준 누락을 막기 위해 필요하다.

Q. Checklist에서 가장 중요한 항목은?
A. Risk Level, Side Effect, Permission, Human Confirmation, Audit Log다.

Q. Checklist 실패 시 어떻게 해?
A. Tool을 실행하지 않고 정책을 보완한 뒤 다시 검수한다.

Q. Review Agent도 Checklist를 사용해?
A. 사용할 수 있다. Tool Result와 Tool Policy 검증에 유용하다.

Q. Safe Execution Checklist의 최종 목표는?
A. Agent가 위험 Tool을 자동 실행하지 않고 안전한 Runtime 기준에 따라 실행하게 만드는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Safe Tool Execution이 뭐야?
A. LLM이 만든 Tool Call을 검증, 권한 확인, 위험도 판단, 사용자 승인 후 안전하게 실행하는 구조다.

Q. LLM Tool Call을 그대로 실행하면 안 되는 이유는?
A. LLM이 잘못된 파일 경로, SQL, Shell Command, 이메일 수신자, 결제 금액 같은 위험한 입력을 생성할 수 있기 때문이다.

Q. Safe Tool Execution 기본 Flow는?
A. Tool Call → Validate Arguments → Check Permission → Check Risk Level → Human Confirmation → Execute Tool → Return Tool Result 순서다.

Q. Risk Level이 뭐야?
A. Tool 실행이 시스템, 데이터, 비용, 외부 서비스에 미치는 영향을 기준으로 나눈 위험도다.

Q. Tool Risk Level은 어떻게 나눠?
A. low, medium, high로 나누고 high는 Human Confirmation을 요구한다.

Q. High Risk Tool 예시는?
A. 파일 삭제, 파일 덮어쓰기, DB 변경, 이메일 발송, 결제 요청, 배포, 계정 변경 작업이다.

Q. Side Effect가 뭐야?
A. Tool 실행이 파일, DB, 이메일, 결제, 배포처럼 외부 상태를 변경하는 효과다.

Q. Side Effect Tool은 어떻게 처리해?
A. 대상, 변경 내용, 영향 범위, Undo 가능 여부를 확인하고 Human Confirmation과 Audit Log를 적용한다.

Q. Human Confirmation이 뭐야?
A. 위험 Tool 실행 전에 사용자에게 작업 내용과 위험을 보여주고 명시적 승인을 받는 절차다.

Q. Human Confirmation은 언제 필요해?
A. 삭제, 덮어쓰기, DB 변경, 이메일 발송, 결제, 배포처럼 되돌리기 어렵거나 외부 영향이 있는 작업 전에 필요하다.

Q. 사용자 승인 전 Tool을 실행해도 돼?
A. 안 된다. 승인 전에는 blocked 상태를 반환해야 한다.

Q. Preview가 뭐야?
A. 실제 실행 전에 변경 대상과 변경 내용을 사용자에게 보여주는 절차다.

Q. Dry Run이 뭐야?
A. 실제 변경 없이 실행될 작업을 시뮬레이션하는 절차다.

Q. DB 변경 Dry Run에는 무엇이 필요해?
A. 대상 테이블, WHERE 조건, 예상 affected rows, 실행될 operation을 보여주는 것이 좋다.

Q. Approval Scope가 뭐야?
A. 사용자가 승인한 Tool 실행의 대상, 작업, 조건 범위다.

Q. 승인 범위를 넘어서는 작업을 해도 돼?
A. 안 된다. 새 대상이나 새 작업은 별도 Confirmation이 필요하다.

Q. Audit Log가 뭐야?
A. Tool 실행 내역을 추적하기 위해 남기는 기록이다.

Q. 어떤 Tool에 Audit Log가 필요해?
A. High Risk Tool, Side Effect Tool, PermissionError, DangerousOperationBlocked 이벤트에 필요하다.

Q. Audit Log에 Secret을 남겨도 돼?
A. 안 된다. API Key, Token, Password, 개인정보는 마스킹해야 한다.

Q. Dangerous Operation이 뭐야?
A. 데이터 손실, 보안 사고, 비용 발생, 운영 장애, 외부 발송을 일으킬 수 있는 위험 작업이다.

Q. DELETE without WHERE는 어떻게 처리해?
A. DangerousOperationBlocked로 차단해야 한다.

Q. Shell Command Tool은 왜 위험해?
A. 파일 시스템, 네트워크, Secret, 권한에 직접 영향을 줄 수 있기 때문이다.

Q. Safe Execution Policy가 뭐야?
A. Tool 실행을 통제하기 위한 권한, 위험도, 승인, 로그, 차단 기준이다.

Q. Safe Execution Policy는 어디서 강제해?
A. Prompt가 아니라 Agent Runtime 또는 Backend System에서 강제해야 한다.

Q. Tool Policy가 없는 Tool은 어떻게 처리해?
A. 안전한 기본값으로 실행을 차단하는 것이 좋다.

Q. Safe Execution Checklist에는 무엇이 들어가야 해?
A. riskLevel, sideEffect, permissionLevel, validation, Dangerous Operation 감지, Human Confirmation, Preview, Audit Log, blocked result 확인이 들어가야 한다.

Q. Safe Execution의 최종 목표는 뭐야?
A. Agent가 외부 도구를 사용할 때 위험 작업을 통제하고 검증된 Tool만 안전하게 실행하게 만드는 것이다.
