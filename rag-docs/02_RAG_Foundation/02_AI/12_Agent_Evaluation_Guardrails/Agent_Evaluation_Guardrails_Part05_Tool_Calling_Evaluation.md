# Agent Evaluation & Guardrails Part05 - Tool Calling Evaluation

---

# 1. Tool Calling Evaluation

## 1.1 Tool Calling Evaluation Core

### [개념]

Tool Calling Evaluation은 Agent가 외부 Tool을 올바르게 선택하고, 안전한 인자로 실행하며, 실행 결과를 정확하게 해석했는지 평가하는 기준이다.

Tool Calling은 실제 시스템에 영향을 줄 수 있다.

따라서 Tool Calling Evaluation은 단순히 Tool이 호출되었는지 확인하는 것이 아니다.

평가 대상:

- Tool Choice
- Tool Arguments
- Permission
- Risk Level
- Execution Status
- Tool Result
- Side Effect
- Error Handling
- Audit Log
- Human Confirmation

Tool Calling Evaluation은 Agent Workflow의 안전성과 신뢰도를 높이기 위한 핵심 평가 기준이다.

---

### [핵심]

Tool Calling Evaluation 기본 Flow:

```text
Tool Call
→ Check Tool Choice
→ Validate Arguments
→ Check Permission
→ Check Risk Level
→ Execute or Stop
→ Validate Result
→ Continue / Retry / Fallback / Stop
```

핵심 검증 항목:

| 항목                    | 검증 내용                          |
| ----------------------- | ---------------------------------- |
| Tool Choice Correctness | 요청에 맞는 Tool을 선택했는가      |
| Argument Validation     | 인자가 Schema와 제약을 만족하는가  |
| Permission Check        | 실행 권한과 승인 조건을 만족하는가 |
| Risk Level              | 작업 위험도가 분류되었는가         |
| Execution Status        | Tool 실행 성공 / 실패를 확인했는가 |
| Result Validation       | Tool 결과를 정확히 해석했는가      |
| Side Effect Check       | 외부 시스템 변경 가능성이 있는가   |
| Error Handling          | 실패 시 적절히 처리했는가          |
| Audit Log               | 중요한 작업 기록이 남는가          |

Tool Calling 결과 판단:

```text
Pass:
- Tool 선택 적절
- Arguments 유효
- 권한과 위험도 확인
- 실행 결과 검증 완료
- Side Effect 안전

Fix:
- Arguments 일부 오류
- 결과 해석 부족
- Retry 가능 오류
- 추가 검증 필요

Stop:
- 위험 작업 승인 없음
- Tool 권한 없음
- Arguments 위험
- Tool 실패 후 Fallback 없음
- Safety 위반
```

---

### [실무]

2026 실무 기준 Tool Calling Agent는 검색, 파일 읽기, 파일 작성, 코드 실행, DB 변경, 이메일 발송, 배포, API 호출 등 다양한 작업을 수행할 수 있다.

개인 AI 개발팀 구조에서는 Tool Calling Evaluation이 PM Agent, DevOps Agent, Review Agent, Safety Agent의 핵심 검증 대상이다.

실무 평가 순서:

```text
1. 사용자 요청에서 Tool 필요성 판단
2. Tool Choice가 적절한지 확인
3. Tool Arguments Schema 검증
4. 작업 Risk Level 분류
5. Human Confirmation 필요 여부 확인
6. Tool 실행 결과 확인
7. 실패 / 오류 / Side Effect 검증
8. 다음 단계 결정
```

예시:

```text
User Request:
프로젝트 파일에서 Controller 목록 찾아줘.

Tool Choice:
- 파일 검색 Tool 사용

Risk Level:
- Low
- 파일 읽기만 수행

Evaluation:
- Tool 선택 적절
- Side Effect 없음
- 자동 실행 가능
```

위험 예시:

```text
User Request:
DB 테이블 초기화하고 다시 만들어줘.

Tool Choice:
- DB 실행 Tool

Risk Level:
- High
- 데이터 손실 가능
- 사용자 승인 필요

Evaluation:
- Human Confirmation 전 실행 금지
- Dry Run 또는 실행 SQL Preview 필요
```

Tool Calling Evaluation Report 예시:

```md
| Item             | Result | Evidence                        | Fix                 |
| ---------------- | ------ | ------------------------------- | ------------------- |
| Tool Choice      | Pass   | 파일 검색 요청에 검색 Tool 사용 | 없음                |
| Arguments        | Fix    | path 누락                       | 대상 경로 추가      |
| Risk Level       | High   | DB 변경 작업                    | 사용자 승인 필요    |
| Execution Status | Fail   | Tool timeout                    | Retry 또는 Fallback |
```

---

### [주의]

Tool Calling Evaluation 주의사항:

- LLM이 만든 Tool Arguments를 그대로 신뢰하지 않는다.
- Tool Result가 실패했는데 성공처럼 답변하면 안 된다.
- Side Effect가 있는 Tool은 실행 전 위험도 판단이 필요하다.
- 삭제, DB 변경, 배포, 이메일 발송은 High Risk로 본다.
- 비용이 발생하는 API 호출은 사용자 확인이 필요할 수 있다.
- Non-idempotent 작업은 재시도에 주의한다.
- 민감정보가 Tool Result에 포함될 수 있으므로 출력과 로그를 제한한다.

---

### [Best Practice]

Tool Calling Evaluation Best Practice:

- Tool 실행 전 Tool Choice와 Arguments를 검증한다.
- Tool Risk Level을 Low / Medium / High / Block으로 분류한다.
- High Risk Tool은 Human Confirmation을 요구한다.
- Medium Risk Tool은 Preview 또는 Dry Run을 우선한다.
- Tool Result는 성공 / 실패 / 부분 성공을 구분한다.
- 실패 시 Retry 가능 여부를 확인한다.
- Retry Limit을 설정한다.
- 실패가 반복되면 Fallback 또는 Stop으로 전환한다.
- Tool 실행 결과는 Evidence로 기록한다.
- 민감정보와 Secret은 로그에 남기지 않는다.

---

### [FAQ]

Q. Tool Calling Evaluation이 뭐야?
A. Agent가 외부 Tool을 올바르게 선택하고 안전하게 실행했으며 결과를 정확히 해석했는지 평가하는 기준이다.

Q. Tool Calling은 왜 별도로 평가해야 해?
A. Tool은 파일 수정, DB 변경, 이메일 발송, 배포처럼 실제 시스템에 영향을 줄 수 있기 때문이다.

Q. Tool Calling Evaluation에서 가장 먼저 볼 것은 뭐야?
A. Tool Choice가 사용자 요청에 맞는지 확인해야 한다.

Q. Tool Arguments는 왜 검증해야 해?
A. 잘못된 인자는 잘못된 파일 수정, 데이터 손실, 실행 실패, 보안 문제를 만들 수 있기 때문이다.

Q. Tool Result가 실패했는데 답변은 가능해?
A. 가능하지만 실패 사실을 명확히 표시하고 성공처럼 포장하면 안 된다.

Q. Tool Calling 결과는 어떻게 나눠?
A. Pass, Fix, Stop으로 나눌 수 있다.

---

# 2. Tool Choice Evaluation

## 2.1 Tool Choice Correctness

### [개념]

Tool Choice Correctness는 Agent가 사용자 요청을 수행하기 위해 적절한 Tool을 선택했는지 평가하는 기준이다.

Tool 선택이 틀리면 이후 Arguments, 실행 결과, 최종 Output도 모두 실패할 수 있다.

Tool Choice는 작업 목적, 위험도, 권한, 데이터 소스, Side Effect 여부를 기준으로 판단한다.

---

### [핵심]

Tool Choice 검증 기준:

| 기준            | 검증 내용                               |
| --------------- | --------------------------------------- |
| Task Fit        | 사용자 요청과 Tool 기능이 맞는가        |
| Data Source Fit | 필요한 데이터에 접근 가능한 Tool인가    |
| Safety Fit      | 더 안전한 Tool이 있는가                 |
| Permission Fit  | 실행 권한이 있는 Tool인가               |
| Side Effect Fit | 읽기 작업에 쓰기 Tool을 쓰지 않았는가   |
| Cost Fit        | 비용 발생 Tool 사용이 필요한가          |
| Freshness Fit   | 최신 정보가 필요한 경우 적절한 Tool인가 |

Tool Choice Evaluation Flow:

```text
User Intent
→ Required Capability
→ Available Tool Match
→ Risk Compare
→ Select Tool or Ask / Stop
```

Tool Choice 결과:

```text
Correct:
- 요청 수행에 적합한 Tool 선택

Suboptimal:
- 가능하지만 더 안전하거나 직접적인 Tool이 있음

Incorrect:
- 요청과 맞지 않는 Tool 선택
- 접근 불가 데이터 Tool 선택
- 읽기 요청에 변경 Tool 선택

Unsafe:
- 불필요하게 High Risk Tool 선택
- 승인 없이 위험 Tool 선택
```

---

### [실무]

실무에서는 Tool을 선택하기 전에 작업 유형을 분류한다.

작업 유형별 Tool 선택 기준:

| 작업 유형      | 적절한 Tool              | 위험도 |
| -------------- | ------------------------ | ------ |
| 문서 검색      | Search / Read Tool       | Low    |
| 파일 내용 확인 | File Read Tool           | Low    |
| 코드 검증      | Test / Build Tool        | Medium |
| 파일 생성      | File Write Tool          | Medium |
| 설정 변경      | File Write / Config Tool | Medium |
| DB 조회        | DB Read Tool             | Medium |
| DB 변경        | DB Write Tool            | High   |
| 이메일 발송    | Email Send Tool          | High   |
| 배포 실행      | Deploy Tool              | High   |
| 삭제           | Delete Tool              | High   |

잘못된 Tool Choice 예시:

```text
User Request:
현재 설정 파일 내용 확인해줘.

Wrong Tool:
- 파일 수정 Tool 사용

Issue:
- 읽기 요청에 쓰기 Tool 선택
- 불필요한 Side Effect 가능성
```

올바른 Tool Choice 예시:

```text
User Request:
최근 로그에서 에러만 찾아줘.

Correct Tool:
- 파일 읽기 / 로그 검색 Tool

Evaluation:
- 읽기 작업
- Low Risk
- 자동 실행 가능
```

Tool Choice Report 예시:

```md
| User Intent    | Selected Tool | Result                  | Issue       | Fix            |
| -------------- | ------------- | ----------------------- | ----------- | -------------- |
| 파일 확인      | File Read     | Correct                 | 없음        | 없음           |
| DB 삭제        | DB Write      | Unsafe without approval | High Risk   | 승인 요청      |
| 최신 문서 확인 | Stale Memory  | Incorrect               | 최신성 부족 | 검색 Tool 사용 |
```

---

### [주의]

Tool Choice 주의사항:

- Tool이 가능하다고 항상 적절한 것은 아니다.
- 읽기 작업에는 쓰기 Tool을 사용하지 않는다.
- 위험도가 낮은 대안이 있으면 먼저 사용한다.
- 최신 정보가 필요한데 Memory만 사용하면 부정확할 수 있다.
- 사용자 승인 없이 High Risk Tool을 선택하면 Safety Failure다.
- Tool 권한이 없으면 억지로 진행하지 않는다.

---

### [Best Practice]

Tool Choice Best Practice:

- 사용자 Intent를 먼저 파악한다.
- 가장 낮은 위험도의 Tool을 우선 선택한다.
- 읽기 / 쓰기 / 삭제 / 외부 전송 작업을 구분한다.
- Tool 권한과 접근 가능 데이터를 확인한다.
- 최신 정보 필요 여부를 판단한다.
- 불필요한 Tool 호출을 줄인다.
- High Risk Tool은 선택 단계에서 Human Confirmation 필요 여부를 표시한다.

---

### [FAQ]

Q. Tool Choice Correctness는 뭐야?
A. Agent가 사용자 요청을 수행하기 위해 적절한 Tool을 선택했는지 평가하는 기준이다.

Q. Tool 선택이 왜 중요해?
A. Tool 선택이 틀리면 실행 실패, 잘못된 결과, 데이터 손실, 보안 문제가 발생할 수 있기 때문이다.

Q. 읽기 요청에 파일 수정 Tool을 써도 돼?
A. 안 된다. 읽기 요청에는 읽기 Tool을 사용해야 Side Effect를 줄일 수 있다.

Q. 최신 정보가 필요한데 Memory만 쓰면 문제야?
A. 문제다. 최신 정보는 검색이나 외부 조회 Tool로 확인해야 한다.

Q. 더 안전한 Tool이 있으면 어떻게 해?
A. 더 낮은 위험도의 Tool을 우선 사용해야 한다.

---

# 3. Argument Validation

## 3.1 Tool Argument Validation

### [개념]

Tool Argument Validation은 Tool 실행 전에 Agent가 생성한 인자가 Schema, 타입, 범위, 대상, 권한, 안전 조건을 만족하는지 검증하는 과정이다.

Tool Arguments는 실제 실행 대상과 동작을 결정한다.

잘못된 Arguments는 잘못된 파일 수정, 데이터 손실, 비용 발생, 보안 문제, 실행 실패로 이어질 수 있다.

---

### [핵심]

Argument Validation 검증 항목:

| 항목              | 검증 내용                                   |
| ----------------- | ------------------------------------------- |
| Schema Match      | Tool Schema와 일치하는가                    |
| Required Argument | 필수 인자가 있는가                          |
| Type Correctness  | 타입이 맞는가                               |
| Value Range       | 값 범위가 안전한가                          |
| Target Validity   | 대상 파일 / DB / API가 맞는가               |
| Path Safety       | 경로가 안전한가                             |
| Permission        | 대상 접근 권한이 있는가                     |
| Injection Risk    | 명령 / SQL / Prompt Injection 위험이 있는가 |
| Secret Exposure   | Secret이 포함되지 않았는가                  |

Argument Validation Flow:

```text
Generated Arguments
→ Schema Check
→ Required Field Check
→ Type Check
→ Target Check
→ Safety Check
→ Valid / Fix / Stop
```

Argument Validation 결과:

```text
Valid:
- Schema 일치
- 필수값 존재
- 타입 정상
- 대상 명확
- 안전 문제 없음

Fix:
- 일부 누락
- 타입 오류
- 대상 불명확
- 수정 후 실행 가능

Stop:
- 위험 경로
- 삭제 대상 불명확
- Secret 포함
- Injection 위험
- 권한 없음
```

---

### [실무]

실무에서는 Arguments를 실행 전에 Preview해야 한다.

파일 작업 Arguments 예시:

```json
{
  "path": "/project/src/main/java/UserService.java",
  "operation": "read"
}
```

검증:

```text
- path 존재 여부 확인
- operation이 read인지 확인
- 쓰기 / 삭제 작업이 아닌지 확인
- 경로가 프로젝트 범위 내부인지 확인
```

DB 작업 Arguments 예시:

```json
{
  "query": "DELETE FROM users",
  "database": "prod"
}
```

검증 결과:

```text
- DELETE 문 포함
- prod DB 대상
- 데이터 손실 가능
- High Risk
- Human Confirmation 필요
- Dry Run 또는 Transaction Rollback 계획 필요
```

Argument Validation Report 예시:

```md
| Argument  | Result | Issue                | Fix                |
| --------- | ------ | -------------------- | ------------------ |
| path      | Pass   | 프로젝트 내부 경로   | 없음               |
| operation | Fail   | delete 작업          | 승인 필요          |
| query     | Stop   | DELETE without WHERE | 실행 금지          |
| recipient | Fix    | 이메일 주소 불명확   | 정확한 수신자 확인 |
```

---

### [주의]

Argument Validation 주의사항:

- Tool Schema만 맞아도 안전한 것은 아니다.
- path나 query는 내용 자체가 위험할 수 있다.
- DELETE, DROP, TRUNCATE는 High Risk다.
- 이메일 수신자, DB 이름, 파일 경로는 특히 검증해야 한다.
- wildcard 삭제는 위험하다.
- Secret이나 Token을 Arguments에 포함하면 안 된다.
- LLM이 추론한 대상 경로를 확정하지 않는다.

---

### [Best Practice]

Argument Validation Best Practice:

- 필수 인자와 타입을 먼저 검증한다.
- 실행 대상 파일, DB, API를 명확히 표시한다.
- 위험 명령어와 위험 SQL을 탐지한다.
- 파일 경로는 허용된 Scope 내부인지 확인한다.
- High Risk Arguments는 Human Confirmation을 요구한다.
- 실행 전 Preview 또는 Dry Run을 제공한다.
- Secret은 마스킹하거나 전달하지 않는다.
- Arguments 검증 실패 시 Tool을 실행하지 않는다.

---

### [FAQ]

Q. Tool Argument Validation이 뭐야?
A. Tool 실행 전에 인자가 Schema, 타입, 범위, 대상, 안전 조건을 만족하는지 검증하는 과정이다.

Q. Schema가 맞으면 실행해도 돼?
A. 아니다. Schema가 맞아도 대상, 위험도, 권한, Side Effect를 추가로 확인해야 한다.

Q. 어떤 Arguments가 위험해?
A. DELETE, DROP, TRUNCATE, 파일 삭제 경로, prod DB 대상, 이메일 수신자, Secret 포함 인자가 위험하다.

Q. Arguments 검증에 실패하면 어떻게 해?
A. Tool을 실행하지 말고 Fix, Human Confirmation, Stop 중 하나로 처리해야 한다.

Q. 파일 경로는 어떻게 검증해?
A. 실제 존재 여부, 프로젝트 Scope 내부 여부, 작업 종류, 삭제 여부를 확인한다.

---

# 4. Permission & Risk Evaluation

## 4.1 Permission Check

### [개념]

Permission Check는 Agent가 Tool을 실행할 권한이 있는지, 사용자 승인 범위 안에 있는지, 작업 위험도가 허용 가능한지 확인하는 과정이다.

Tool 실행은 권한과 승인 범위를 넘어가면 안 된다.

Permission Check는 Human Confirmation Rule과 연결된다.

---

### [핵심]

Permission Check 검증 항목:

| 항목               | 검증 내용                         |
| ------------------ | --------------------------------- |
| User Authorization | 사용자가 해당 작업을 요청했는가   |
| Tool Permission    | Agent에게 Tool 사용 권한이 있는가 |
| Scope Permission   | 실행 대상이 승인 범위 안인가      |
| Risk Level         | 작업 위험도가 분류되었는가        |
| Human Confirmation | 승인 필요 작업에 승인이 있는가    |
| Role Permission    | 해당 Agent 역할에 맞는 Tool인가   |
| Cost Permission    | 비용 발생 가능성에 동의가 있는가  |

Permission Check Flow:

```text
Tool Request
→ Check User Intent
→ Check Agent Tool Permission
→ Check Scope
→ Check Risk Level
→ Confirmation Required?
→ Allow / Ask / Block
```

Permission 결과:

```text
Allow:
- 사용자 요청 범위 내
- Tool 권한 있음
- Low Risk 또는 승인 완료

Ask:
- 승인 필요
- 대상 불명확
- 비용 가능성 있음
- 범위 확인 필요

Block:
- 권한 없음
- 승인 없는 High Risk
- 사용자 요청 범위 밖
- 보안 위험
```

---

### [실무]

실무에서는 Risk Level과 Permission을 함께 평가한다.

Risk Level 기준:

| Risk   | 작업 예시                              | 처리             |
| ------ | -------------------------------------- | ---------------- |
| Low    | 검색, 파일 읽기, 로그 조회             | 자동 허용 가능   |
| Medium | 파일 생성, 초안 작성, 설정 변경 제안   | 검증 후 진행     |
| High   | 파일 삭제, DB 변경, 배포, 이메일 발송  | 사용자 승인 필요 |
| Block  | Secret 노출, 위험 명령, 악성 코드 실행 | 차단             |

Permission Check 예시:

```text
User Request:
이메일 초안 작성해줘.

Tool:
Draft Email

Risk Level:
Medium

Permission:
- 초안 작성은 가능
- 실제 발송은 별도 승인 필요
```

High Risk 예시:

```text
User Request:
이메일 보내줘.

Tool:
Send Email

Risk Level:
High

Permission:
- 사용자가 명시적으로 발송 요청했는지 확인
- 수신자 / 제목 / 본문 확인
- 승인 범위 밖 추가 발송 금지
```

Permission Report 예시:

```md
| Action         | Risk   | Permission   | Result        | Handling    |
| -------------- | ------ | ------------ | ------------- | ----------- |
| 파일 읽기      | Low    | 요청 범위 내 | Allow         | 실행 가능   |
| 설정 파일 수정 | Medium | 요청 범위 내 | Ask / Preview | 변경안 제시 |
| DB 삭제        | High   | 승인 없음    | Stop          | 승인 필요   |
| Secret 출력    | Block  | 권한 없음    | Block         | 차단        |
```

---

### [주의]

Permission Check 주의사항:

- 사용자 요청이 모호하면 High Risk 작업을 실행하지 않는다.
- 한 작업 승인으로 다른 작업까지 확장하지 않는다.
- 초안 작성 승인과 발송 승인은 다르다.
- 테스트 DB와 운영 DB는 위험도가 다르다.
- 비용 발생 작업은 별도 확인이 필요할 수 있다.
- Agent 역할 밖 Tool 사용은 제한해야 한다.
- 승인 없이 위험 작업을 자동화하면 Safety Failure다.

---

### [Best Practice]

Permission Check Best Practice:

- 사용자 요청 범위를 명확히 추출한다.
- Tool 권한과 Agent 역할을 확인한다.
- 위험도에 따라 Allow / Ask / Block으로 처리한다.
- High Risk 작업은 Action Preview를 제공한다.
- 승인 요청에는 대상, 영향, 되돌릴 수 있는지 포함한다.
- 승인 범위 밖 추가 작업은 수행하지 않는다.
- 권한 없음 상태에서는 Fallback을 제안한다.

---

### [FAQ]

Q. Permission Check가 뭐야?
A. Agent가 Tool을 실행할 권한과 사용자 승인 범위 안에 있는지 확인하는 과정이다.

Q. 사용자 요청이 있으면 모든 Tool을 실행해도 돼?
A. 아니다. 위험도, 권한, 승인 범위, Side Effect를 확인해야 한다.

Q. 초안 작성과 발송은 같은 권한이야?
A. 아니다. 초안 작성은 Medium Risk이고 실제 발송은 High Risk로 별도 승인이 필요하다.

Q. High Risk 작업은 어떻게 처리해?
A. 사용자 승인 전에는 실행하지 않고 대상과 영향 범위를 Preview해야 한다.

Q. Block 작업은 뭐야?
A. Secret 노출, 위험 명령, 악성 코드 실행처럼 허용하면 안 되는 작업이다.

---

# 5. Tool Result Validation

## 5.1 Result Validation

### [개념]

Tool Result Validation은 Tool 실행 결과가 성공인지 실패인지, 결과가 사용자 요청을 해결하는지, 결과 해석이 정확한지 확인하는 과정이다.

Tool을 호출했다고 작업이 완료된 것은 아니다.

Tool Result를 검증하지 않으면 실패를 성공으로 착각하거나 잘못된 데이터를 기반으로 답변할 수 있다.

---

### [핵심]

Tool Result Validation 검증 항목:

| 항목                     | 검증 내용                    |
| ------------------------ | ---------------------------- |
| Execution Status         | 성공 / 실패 / 부분 성공 여부 |
| Error Message            | 오류 메시지 확인             |
| Result Completeness      | 결과가 충분한가              |
| Result Relevance         | 사용자 요청과 관련 있는가    |
| Data Freshness           | 최신성이 필요한 데이터인가   |
| Data Integrity           | 결과 데이터가 일관되는가     |
| Side Effect Confirmation | 실제 변경이 발생했는가       |
| Output Limitation        | 결과 한계가 있는가           |

Result Validation Flow:

```text
Tool Result
→ Check Status
→ Check Error
→ Check Completeness
→ Check Relevance
→ Interpret Result
→ Continue / Retry / Fallback / Stop
```

Tool Result 상태:

```text
Success:
- Tool 실행 성공
- 결과가 요청 해결에 충분

Partial Success:
- 일부 결과만 확보
- 한계 표시 필요

Failure:
- Tool 실행 실패
- Error Handling 필요

Unknown:
- 결과 해석 불가
- 추가 검증 필요
```

---

### [실무]

실무에서는 Tool Result를 Evidence로 사용하기 전에 검증한다.

성공 결과 예시:

```text
Tool Result:
3개 파일 검색됨.
Master_RAG_Rules.md, Project_Progress.md, Domain_Rules.md

Validation:
- 요청한 문서 확인에 충분
- Success
```

실패 결과 예시:

```text
Tool Result:
Permission denied

Validation:
- Tool 실행 실패
- 파일 내용 확인 불가
- Failure
- 성공 답변 금지
```

부분 성공 예시:

```text
Tool Result:
10개 중 6개 파일만 읽음.
4개 파일은 encoding error.

Validation:
- Partial Success
- 누락 파일 표시 필요
- 전체 검수 완료로 말하면 안 됨
```

Tool Result Validation Report:

```md
| Tool        | Status          | Result Quality | Issue            | Next Step            |
| ----------- | --------------- | -------------- | ---------------- | -------------------- |
| File Search | Success         | 충분           | 없음             | 답변 가능            |
| Build Test  | Failure         | 불충분         | compileJava 실패 | 오류 분석            |
| DB Query    | Partial Success | 일부 누락      | timeout          | Retry 또는 범위 축소 |
```

---

### [주의]

Tool Result Validation 주의사항:

- Tool Result가 비어 있으면 검색 실패일 수 있다.
- 결과 없음과 존재하지 않음은 다르다.
- Tool 실패를 성공처럼 말하면 안 된다.
- 부분 결과를 전체 결과처럼 일반화하면 안 된다.
- 오류 메시지는 원인 분석 Evidence로 사용할 수 있다.
- Tool이 반환한 데이터에도 한계와 최신성 문제가 있을 수 있다.
- 외부 API 결과는 변동 가능성을 고려해야 한다.

---

### [Best Practice]

Tool Result Validation Best Practice:

- Tool 실행 상태를 먼저 확인한다.
- 오류 메시지를 숨기지 않고 요약한다.
- 결과가 사용자 요청을 해결하기에 충분한지 확인한다.
- 부분 성공은 Partial로 표시한다.
- 결과 없음은 “제공된 범위에서 찾지 못함”으로 표현한다.
- Tool Result를 Evidence로 사용할 때 한계를 표시한다.
- 실패 시 Retry 가능 여부와 Fallback을 판단한다.

---

### [FAQ]

Q. Tool Result Validation이 뭐야?
A. Tool 실행 결과가 성공인지 실패인지, 결과가 충분하고 정확한지 확인하는 과정이다.

Q. Tool을 호출하면 작업 완료야?
A. 아니다. 실행 상태와 결과 품질을 검증해야 한다.

Q. Tool 결과가 없으면 존재하지 않는다는 뜻이야?
A. 아니다. 검색 실패, 권한 부족, 범위 부족일 수 있다.

Q. Partial Success는 어떻게 처리해?
A. 일부만 성공했다고 표시하고 누락 범위와 한계를 명확히 해야 한다.

Q. Tool 실패 시 어떻게 해야 해?
A. 실패를 보고하고 Retry 가능 여부, Fallback, Stop을 판단해야 한다.

---

# 6. Side Effect Evaluation

## 6.1 Side Effect Check

### [개념]

Side Effect Check는 Tool 실행이 외부 시스템, 파일, DB, 네트워크, 사용자 계정, 비용, 상태에 변경을 일으키는지 평가하는 과정이다.

Side Effect가 있는 작업은 위험도가 높아질 수 있다.

읽기 작업과 변경 작업은 반드시 구분해야 한다.

---

### [핵심]

Side Effect 유형:

| 유형                   | 예시                                |
| ---------------------- | ----------------------------------- |
| File System Change     | 파일 생성, 수정, 삭제               |
| Database Change        | INSERT, UPDATE, DELETE, DROP        |
| External Communication | 이메일 발송, 메시지 전송, API 호출  |
| Deployment Change      | 서버 배포, 재시작, 설정 반영        |
| Cost Impact            | 유료 API 호출, 클라우드 리소스 생성 |
| Account State Change   | 캘린더 생성, 라벨 변경, 권한 수정   |
| Security Impact        | Secret 출력, 권한 변경, 방화벽 변경 |

Side Effect Evaluation Flow:

```text
Planned Tool Action
→ Read or Write?
→ External Side Effect?
→ Reversible?
→ Cost / Security Impact?
→ Risk Level
→ Allow / Ask / Block
```

Side Effect 위험 판단:

```text
Low:
- 읽기만 수행
- 외부 변경 없음

Medium:
- 파일 생성
- 초안 작성
- 되돌릴 수 있는 설정 변경

High:
- 삭제
- DB 변경
- 배포
- 실제 발송
- 비용 발생 가능

Block:
- Secret 노출
- 위험 명령
- 악성 코드 실행
```

---

### [실무]

실무에서는 Side Effect가 있는 작업에 Preview / Dry Run / Confirmation을 적용한다.

파일 수정 예시:

```text
Action:
application.properties 수정

Side Effect:
- 파일 변경
- 애플리케이션 동작 영향 가능

Handling:
- 변경 전 diff preview
- 사용자 확인
- 백업 또는 rollback 안내
```

DB 변경 예시:

```text
Action:
DELETE FROM notifications

Side Effect:
- 데이터 삭제
- 복구 어려움

Handling:
- High Risk
- 실행 금지
- 조건절 확인
- 사용자 승인 필요
```

이메일 발송 예시:

```text
Action:
send_email

Side Effect:
- 외부 수신자에게 메시지 발송
- 회수 어려움

Handling:
- High Risk
- 수신자 / 제목 / 본문 확인
- 명시적 발송 승인 필요
```

Side Effect Report 예시:

```md
| Action      | Side Effect | Reversible | Risk   | Handling     |
| ----------- | ----------- | ---------- | ------ | ------------ |
| 파일 읽기   | 없음        | 해당 없음  | Low    | Allow        |
| 파일 생성   | 있음        | 가능       | Medium | Preview      |
| DB 삭제     | 있음        | 어려움     | High   | Confirmation |
| Secret 출력 | 보안 영향   | 불가       | Block  | 차단         |
```

---

### [주의]

Side Effect Check 주의사항:

- 읽기 작업과 쓰기 작업을 혼동하지 않는다.
- 삭제와 발송은 되돌리기 어렵다.
- 테스트 환경과 운영 환경을 구분해야 한다.
- 비용 발생 가능성이 있으면 사용자 확인이 필요하다.
- 외부 API 호출도 상태 변경이나 비용이 있을 수 있다.
- 자동 Retry가 중복 생성이나 중복 발송을 만들 수 있다.
- Non-idempotent 작업은 Retry를 제한해야 한다.

---

### [Best Practice]

Side Effect Check Best Practice:

- Tool 실행 전 읽기 / 쓰기 / 삭제 / 외부 전송을 구분한다.
- Reversible / Irreversible 여부를 판단한다.
- 외부 시스템 영향 여부를 확인한다.
- 비용과 보안 영향을 평가한다.
- High Risk 작업은 Human Confirmation을 요구한다.
- Medium Risk 작업은 Preview 또는 Dry Run을 제공한다.
- Non-idempotent 작업은 Retry를 피하거나 제한한다.
- 실제 실행 후에는 변경 결과를 검증한다.

---

### [FAQ]

Q. Side Effect Check가 뭐야?
A. Tool 실행이 파일, DB, 외부 시스템, 비용, 계정 상태에 변경을 일으키는지 평가하는 과정이다.

Q. 읽기 작업도 위험해?
A. 보통 Low Risk지만 민감정보를 읽는 경우 보안 주의가 필요하다.

Q. 어떤 Side Effect가 High Risk야?
A. 삭제, DB 변경, 배포, 실제 이메일 발송, 비용 발생 작업은 High Risk다.

Q. 외부 API 호출도 Side Effect가 있어?
A. 있을 수 있다. 상태 변경, 비용 발생, Rate Limit 사용이 발생할 수 있다.

Q. Non-idempotent 작업은 왜 주의해야 해?
A. 재시도 시 중복 생성, 중복 결제, 중복 발송 같은 문제가 생길 수 있기 때문이다.

---

# 7. Tool Error Handling

## 7.1 Tool Failure Handling

### [개념]

Tool Error Handling은 Tool 실행 실패, Timeout, 권한 오류, Rate Limit, 잘못된 Arguments, 부분 성공 상태를 안전하게 처리하는 기준이다.

Tool 실패는 Agent 실패로 이어질 수 있지만, 올바르게 처리하면 Retry, Fallback, Partial Answer, Stop으로 복구할 수 있다.

---

### [핵심]

Tool Failure 유형:

| Failure               | 의미                            |
| --------------------- | ------------------------------- |
| Argument Error        | 인자 누락, 타입 오류, 범위 오류 |
| Permission Error      | 권한 부족, 승인 없음            |
| Timeout               | 실행 시간 초과                  |
| Rate Limit            | 호출 제한 초과                  |
| Network Error         | 네트워크 오류                   |
| Not Found             | 대상 파일 / 리소스 없음         |
| Partial Failure       | 일부만 성공                     |
| Unsafe Action Blocked | 안전 규칙으로 차단              |
| Unknown Failure       | 원인 불명 실패                  |

Tool Error Handling Flow:

```text
Tool Failure
→ Identify Failure Type
→ Retryable?
→ Risk Level Check
→ Retry / Fallback / Ask / Stop
```

Retry 가능 여부:

| Failure          | Retry 가능성 | 처리                        |
| ---------------- | ------------ | --------------------------- |
| Timeout          | 가능         | 제한적 Retry                |
| Rate Limit       | 가능         | 대기 또는 빈도 조절         |
| Network Error    | 가능         | 제한적 Retry                |
| Argument Error   | 수정 후 가능 | Arguments Fix               |
| Permission Error | 불가         | 사용자 승인 또는 Stop       |
| Unsafe Action    | 불가         | Block                       |
| Not Found        | 제한적       | 경로 확인 또는 Missing      |
| Partial Failure  | 가능         | 범위 축소 또는 Partial 처리 |

---

### [실무]

실무에서는 Tool 실패를 성공으로 포장하지 않는다.

Timeout 예시:

```text
Tool Result:
Timeout

Handling:
- Tool Failure로 표시
- Retry 가능 여부 확인
- 동일 작업 무제한 반복 금지
- 필요 시 범위 축소
```

Permission Error 예시:

```text
Tool Result:
Permission denied

Handling:
- 권한 부족 표시
- 실행하지 못한 범위 명확화
- Fallback 가능 여부 확인
- 필요 시 사용자 확인
```

Unsafe Action 예시:

```text
Tool Action:
DROP TABLE users

Handling:
- Unsafe Action Blocked
- Block 처리
- 사용자 승인만으로도 정책 위반이면 실행 금지
```

Tool Failure Report 예시:

```md
| Tool       | Failure Type     | Retryable | Handling  |
| ---------- | ---------------- | --------- | --------- |
| File Read  | Not Found        | 제한적    | 경로 확인 |
| Build      | Timeout          | 가능      | 1회 Retry |
| DB Delete  | Unsafe Action    | 불가      | Block     |
| Email Send | Permission Error | 불가      | 승인 필요 |
```

---

### [주의]

Tool Error Handling 주의사항:

- 무제한 Retry는 금지한다.
- 같은 Arguments로 반복 실패하면 Arguments를 수정해야 한다.
- 위험 작업은 Retry가 특히 위험하다.
- Permission Error는 Retry로 해결되지 않을 수 있다.
- Partial Failure를 전체 성공으로 말하면 안 된다.
- Tool Error를 숨기면 Evaluation 신뢰도가 낮아진다.
- 안전상 차단된 작업은 우회하지 않는다.

---

### [Best Practice]

Tool Error Handling Best Practice:

- Failure Type을 먼저 분류한다.
- Retryable / Non-Retryable을 구분한다.
- Retry Limit을 명시한다.
- 같은 실패가 반복되면 Fallback으로 전환한다.
- Permission 문제는 사용자 확인 또는 Stop으로 처리한다.
- 안전 차단은 우회하지 않는다.
- Partial Failure는 한계와 누락 범위를 표시한다.
- 최종 답변에는 Tool 실패 여부를 정확히 반영한다.

---

### [FAQ]

Q. Tool Error Handling이 뭐야?
A. Tool 실행 실패, Timeout, 권한 오류, Rate Limit, 부분 성공 상태를 안전하게 처리하는 기준이다.

Q. Tool 실패하면 계속 Retry하면 돼?
A. 안 된다. Retry Limit을 두고 실패 유형에 따라 Fallback 또는 Stop으로 전환해야 한다.

Q. Permission Error는 Retry하면 해결돼?
A. 보통 해결되지 않는다. 사용자 승인이나 권한 변경이 필요하다.

Q. Partial Failure는 어떻게 답변해?
A. 일부만 성공했다고 표시하고 누락 범위와 한계를 명확히 해야 한다.

Q. Unsafe Action Blocked는 우회해도 돼?
A. 안 된다. 안전 규칙으로 차단된 작업은 우회하면 안 된다.

---

# 8. Tool Calling Checklist

## 8.1 Checklist

### [개념]

Tool Calling Checklist는 Agent가 Tool을 실행하기 전후에 확인해야 하는 최소 검증 목록이다.

이 Checklist는 Tool Agent, PM Agent, Review Agent, Safety Agent가 공통으로 사용할 수 있다.

---

### [핵심]

Tool Calling Pre-Execution Checklist:

```md
### [Checklist]

- [ ] 사용자 요청에 Tool 사용이 필요한가?
- [ ] 선택한 Tool이 작업 목적과 맞는가?
- [ ] 더 낮은 위험도의 Tool 대안은 없는가?
- [ ] Tool Arguments가 Schema와 일치하는가?
- [ ] 필수 인자가 누락되지 않았는가?
- [ ] 실행 대상 파일 / DB / API가 명확한가?
- [ ] Path / Query / Recipient가 안전한가?
- [ ] Tool 실행 권한이 있는가?
- [ ] Risk Level을 분류했는가?
- [ ] Side Effect가 있는가?
- [ ] Human Confirmation이 필요한가?
- [ ] Dry Run 또는 Preview가 필요한가?
```

Tool Calling Post-Execution Checklist:

```md
### [Checklist]

- [ ] Tool 실행 상태를 확인했는가?
- [ ] 성공 / 실패 / 부분 성공을 구분했는가?
- [ ] 오류 메시지를 확인했는가?
- [ ] 결과가 사용자 요청 해결에 충분한가?
- [ ] Tool Result를 과장하지 않았는가?
- [ ] Side Effect 발생 여부를 확인했는가?
- [ ] 실패 시 Retry 가능 여부를 판단했는가?
- [ ] Retry Limit을 적용했는가?
- [ ] Fallback 또는 Stop이 필요한가?
- [ ] 민감정보를 출력하지 않았는가?
```

최소 Pass 기준:

```text
- Tool Choice 적절
- Arguments 유효
- Risk Level 확인
- Human Confirmation 필요 여부 확인
- Tool Result 검증 완료
- 실패를 성공처럼 처리하지 않음
```

---

### [실무]

실무에서는 Tool Calling Checklist를 실행 전과 실행 후로 나누어 적용한다.

실행 전:

```text
User Request
→ Tool Need Check
→ Tool Choice
→ Arguments Validation
→ Risk Classification
→ Permission Check
→ Execute or Stop
```

실행 후:

```text
Tool Result
→ Status Check
→ Result Validation
→ Side Effect Confirmation
→ Error Handling
→ Continue / Retry / Fallback / Stop
```

Checklist Result 예시:

```md
### Tool Calling Evaluation Result

| Phase | Item              | Result | Fix         |
| ----- | ----------------- | ------ | ----------- |
| Pre   | Tool Choice       | Pass   | 없음        |
| Pre   | Arguments         | Fix    | path 명확화 |
| Pre   | Risk Level        | High   | 승인 필요   |
| Post  | Execution Status  | Fail   | Timeout     |
| Post  | Result Validation | Stop   | 결과 불충분 |
```

---

### [주의]

Tool Calling Checklist 주의사항:

- Checklist는 최소 기준이며 Safety Evaluation을 대체하지 않는다.
- 실행 전 검증 없이 Tool을 호출하지 않는다.
- 실행 후 결과 검증 없이 Final Output을 만들지 않는다.
- High Risk 작업은 Checklist 통과만으로 실행할 수 없다.
- 사용자 승인 범위를 넘는 추가 Tool 호출은 금지한다.
- 실패 결과를 숨기지 않는다.
- 민감정보가 포함된 Tool Result는 출력하지 않는다.

---

### [Best Practice]

Tool Calling Checklist Best Practice:

- Pre-Execution과 Post-Execution을 분리한다.
- 위험도 분류를 실행 전에 완료한다.
- Arguments를 Preview 가능한 형태로 정리한다.
- High Risk 작업은 명시적 승인 전 Stop한다.
- Tool Result는 Evidence로 기록한다.
- 실패 유형을 분류한다.
- Retry와 Fallback 기준을 둔다.
- 최종 Output에 Tool Result의 한계를 반영한다.

---

### [FAQ]

Q. Tool Calling Checklist는 뭐야?
A. Agent가 Tool을 실행하기 전후에 확인해야 하는 최소 검증 목록이다.

Q. Tool 실행 전에는 무엇을 확인해?
A. Tool 필요성, Tool Choice, Arguments, 권한, Risk Level, Side Effect, Human Confirmation 여부를 확인한다.

Q. Tool 실행 후에는 무엇을 확인해?
A. 실행 상태, 성공 / 실패 / 부분 성공, 오류 메시지, 결과 충분성, Side Effect 발생 여부를 확인한다.

Q. Checklist를 통과하면 High Risk Tool을 실행해도 돼?
A. 아니다. High Risk Tool은 사용자 승인 전 실행하면 안 된다.

Q. Tool Result가 실패했는데 Final Output을 만들어도 돼?
A. 가능하지만 실패 사실과 한계를 명확히 반영해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Tool Calling Evaluation이 뭐야?
A. Agent가 외부 Tool을 올바르게 선택하고 안전하게 실행했으며 결과를 정확히 해석했는지 평가하는 기준이다.

Q. Tool Calling은 왜 별도로 평가해야 해?
A. Tool은 파일 수정, DB 변경, 이메일 발송, 배포처럼 실제 시스템에 영향을 줄 수 있기 때문이다.

Q. Tool Calling Evaluation Flow는 어떻게 돼?
A. Tool Call → Check Tool Choice → Validate Arguments → Check Permission → Check Risk Level → Execute or Stop → Validate Result 순서다.

Q. Tool Choice Correctness는 뭐야?
A. Agent가 사용자 요청을 수행하기 위해 적절한 Tool을 선택했는지 평가하는 기준이다.

Q. Tool 선택은 어떻게 평가해?
A. Task Fit, Data Source Fit, Safety Fit, Permission Fit, Side Effect Fit, Cost Fit, Freshness Fit을 기준으로 평가한다.

Q. 읽기 요청에 쓰기 Tool을 써도 돼?
A. 안 된다. 읽기 요청에는 읽기 Tool을 사용해야 Side Effect를 줄일 수 있다.

Q. Tool Argument Validation이 뭐야?
A. Tool 실행 전에 인자가 Schema, 타입, 범위, 대상, 안전 조건을 만족하는지 검증하는 과정이다.

Q. Schema가 맞으면 Tool을 실행해도 돼?
A. 아니다. Schema가 맞아도 대상, 권한, 위험도, Side Effect를 추가로 확인해야 한다.

Q. 위험한 Tool Arguments는 뭐야?
A. DELETE, DROP, TRUNCATE, 파일 삭제 경로, prod DB 대상, 이메일 수신자, Secret 포함 인자가 위험하다.

Q. Arguments 검증 실패 시 어떻게 해?
A. Tool을 실행하지 말고 Fix, Human Confirmation, Stop 중 하나로 처리해야 한다.

Q. Permission Check는 뭐야?
A. Agent가 Tool을 실행할 권한과 사용자 승인 범위 안에 있는지 확인하는 과정이다.

Q. Tool Risk Level은 어떻게 나눠?
A. Low, Medium, High, Block으로 나눈다.

Q. Low Risk Tool 작업은 뭐야?
A. 검색, 파일 읽기, 로그 조회처럼 Side Effect가 없는 작업이다.

Q. Medium Risk Tool 작업은 뭐야?
A. 파일 생성, 초안 작성, 설정 변경 제안처럼 검증 후 진행 가능한 작업이다.

Q. High Risk Tool 작업은 뭐야?
A. 파일 삭제, DB 변경, 배포, 이메일 발송처럼 사용자 승인이 필요한 작업이다.

Q. Block Tool 작업은 뭐야?
A. Secret 노출, 위험 명령, 악성 코드 실행처럼 차단해야 하는 작업이다.

Q. Human Confirmation은 언제 필요해?
A. 삭제, DB 변경, 배포, 이메일 발송, 결제, 비용 발생 작업처럼 위험하거나 되돌리기 어려운 작업 전에 필요하다.

Q. Tool Result Validation이 뭐야?
A. Tool 실행 결과가 성공인지 실패인지, 결과가 충분하고 정확한지 확인하는 과정이다.

Q. Tool을 호출하면 작업 완료야?
A. 아니다. 실행 상태와 결과 품질을 검증해야 한다.

Q. Tool Result가 없으면 존재하지 않는다는 뜻이야?
A. 아니다. 검색 실패, 권한 부족, 범위 부족일 수 있다.

Q. Partial Success는 어떻게 처리해?
A. 일부만 성공했다고 표시하고 누락 범위와 한계를 명확히 해야 한다.

Q. Tool 실패 시 어떻게 해야 해?
A. 실패를 보고하고 Retry 가능 여부, Fallback, Stop을 판단해야 한다.

Q. Side Effect Check가 뭐야?
A. Tool 실행이 파일, DB, 외부 시스템, 비용, 계정 상태에 변경을 일으키는지 평가하는 과정이다.

Q. 어떤 Side Effect가 High Risk야?
A. 삭제, DB 변경, 배포, 실제 이메일 발송, 비용 발생 작업은 High Risk다.

Q. Non-idempotent 작업은 왜 주의해야 해?
A. 재시도 시 중복 생성, 중복 결제, 중복 발송 같은 문제가 생길 수 있기 때문이다.

Q. Tool Error Handling은 뭐야?
A. Tool 실행 실패, Timeout, 권한 오류, Rate Limit, 부분 성공 상태를 안전하게 처리하는 기준이다.

Q. Tool 실패하면 계속 Retry하면 돼?
A. 안 된다. Retry Limit을 두고 실패 유형에 따라 Fallback 또는 Stop으로 전환해야 한다.

Q. Permission Error는 Retry하면 해결돼?
A. 보통 해결되지 않는다. 사용자 승인이나 권한 변경이 필요하다.

Q. Unsafe Action Blocked는 우회해도 돼?
A. 안 된다. 안전 규칙으로 차단된 작업은 우회하면 안 된다.

Q. Tool Calling Checklist는 언제 써?
A. Agent가 Tool을 실행하기 전후에 사용한다.

Q. Tool 실행 전에는 무엇을 확인해?
A. Tool 필요성, Tool Choice, Arguments, 권한, Risk Level, Side Effect, Human Confirmation 여부를 확인한다.

Q. Tool 실행 후에는 무엇을 확인해?
A. 실행 상태, 성공 / 실패 / 부분 성공, 오류 메시지, 결과 충분성, Side Effect 발생 여부를 확인한다.

Q. Tool 실패를 성공처럼 답변하면 어떤 문제야?
A. Tool Failure를 숨기는 것이며 Evaluation 신뢰도와 Agent Workflow 신뢰도를 떨어뜨린다.
