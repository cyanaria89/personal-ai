# Agent Evaluation & Guardrails Part07 - Safety Guardrails

---

# 1. Safety Guardrails

## 1.1 Safety Guardrails Core

### [개념]

Safety Guardrails는 Agent가 위험하거나 되돌리기 어려운 행동을 하지 않도록 제한하는 안전 규칙이다.

Safety Guardrails는 Tool Calling 자체를 설명하는 문서가 아니다.

Safety Guardrails의 초점은 **위험 판단, 승인 필요 여부, 차단 조건, 안전한 중단 기준**이다.

Safety Guardrails 적용 대상:

- 위험 작업 실행
- 데이터 삭제 / 변경
- 외부 시스템 영향
- 비용 발생 작업
- Secret / 민감정보 노출
- 승인 없는 자동 실행
- 요청 범위 밖 작업
- 안전하지 않은 Tool 사용 제안
- 위험한 Fix Recommendation

Safety Guardrails는 Agent의 행동을 다음 세 가지로 분류한다.

```text
Allow
Ask
Block
```

---

### [핵심]

Safety Guardrails 핵심 원칙:

- 사용자 요청 범위 안에서만 작업한다.
- 위험도는 실행 전 분류한다.
- 되돌리기 어려운 작업은 자동 실행하지 않는다.
- Secret은 출력, 저장, 로그 기록하지 않는다.
- High Risk 작업은 Human Confirmation 전 Stop한다.
- Block 대상은 사용자 요청이 있어도 실행하지 않는다.
- Tool 실패나 위험을 성공처럼 포장하지 않는다.
- Safety Finding은 다른 개선사항보다 우선한다.

Safety Decision Flow:

```text
Agent Action
→ Scope Check
→ Risk Check
→ Side Effect Check
→ Secret Check
→ Confirmation Check
→ Allow / Ask / Block / Stop
```

Safety Decision 기준:

| Decision | 의미                      | 처리                  |
| -------- | ------------------------- | --------------------- |
| Allow    | 안전하고 변경 영향이 낮음 | 진행 가능             |
| Ask      | 위험하거나 범위 확인 필요 | 사용자 확인 필요      |
| Stop     | 현재 조건에서 진행 불가   | 사유와 필요 조치 표시 |
| Block    | 안전상 허용 불가          | 차단                  |

---

### [실무]

개인 AI 개발팀 구조에서는 PM Agent, Backend Agent, Frontend Agent, DevOps Agent, AI/ML Agent, Review Agent, Safety Agent가 모두 Safety Guardrails의 영향을 받는다.

Agent별 Safety 초점:

| Agent          | Safety 초점                                     |
| -------------- | ----------------------------------------------- |
| PM Agent       | 위험 작업 Routing, 승인 필요 여부 판단          |
| Backend Agent  | DB 변경, 인증/권한, Secret 노출 방지            |
| Frontend Agent | 사용자 입력, Token 노출, 외부 API Key 노출 방지 |
| DevOps Agent   | 배포, 서버 재시작, 환경 변수, 인프라 변경 통제  |
| AI/ML Agent    | RAG 근거 부족, Memory 충돌, 민감정보 사용 방지  |
| Review Agent   | Safety Finding 탐지                             |
| Safety Agent   | Risk Level, Scope, Confirmation 최종 판단       |

실무 적용 예시:

```text
Action:
프로젝트 파일 읽기

Safety Decision:
Allow

Reason:
- 읽기 작업
- Side Effect 없음
- Low Risk
```

```text
Action:
application.properties 수정 제안

Safety Decision:
Ask 또는 Preview

Reason:
- 설정 변경
- 애플리케이션 동작 영향 가능
- Medium Risk
```

```text
Action:
운영 DB DELETE 실행

Safety Decision:
Stop

Reason:
- 데이터 삭제
- High Risk
- Human Confirmation 필요
```

```text
Action:
API Key 전체 출력

Safety Decision:
Block

Reason:
- Secret 노출
- 안전상 허용 불가
```

---

### [주의]

Safety Guardrails 주의사항:

- 사용자 요청이 있다고 항상 실행 가능한 것은 아니다.
- 모호한 요청으로 High Risk 작업을 실행하지 않는다.
- 위험도가 불명확하면 Allow가 아니라 Ask로 처리한다.
- 안전 차단 대상은 우회하지 않는다.
- 승인된 작업 범위를 넘는 추가 행동은 금지한다.
- 파일 읽기와 파일 수정은 위험도가 다르다.
- 초안 작성과 실제 발송은 위험도가 다르다.
- 테스트 환경과 운영 환경은 위험도가 다르다.

---

### [Best Practice]

Safety Guardrails Best Practice:

- 모든 Agent Action에 Safety Decision을 적용한다.
- Low / Medium / High / Block 기준을 고정한다.
- High Risk 작업은 Preview 후 사용자 확인을 요구한다.
- Block 작업은 실행하지 않는다.
- Secret은 항상 마스킹한다.
- 요청 범위와 승인 범위를 분리해 판단한다.
- Stop 사유는 명확히 기록한다.
- Safety Finding은 Critical 또는 Major로 우선 처리한다.
- Review Agent가 Safety Checklist를 반드시 확인하게 한다.

---

### [FAQ]

Q. Safety Guardrails가 뭐야?
A. Agent가 위험하거나 되돌리기 어려운 행동을 하지 않도록 제한하는 안전 규칙이다.

Q. Safety Guardrails의 핵심 판단은 뭐야?
A. Agent Action을 Allow, Ask, Stop, Block 중 하나로 분류하는 것이다.

Q. Safety Guardrails는 Tool Calling Evaluation과 같아?
A. 아니다. Tool Calling Evaluation은 Tool 선택과 실행 검증이고, Safety Guardrails는 위험도와 승인 조건 판단에 초점을 둔다.

Q. 위험도가 애매하면 어떻게 해?
A. Allow로 처리하지 말고 Ask 또는 Stop으로 처리해야 한다.

Q. Safety Finding은 왜 우선순위가 높아?
A. 데이터 손실, Secret 노출, 외부 시스템 영향처럼 치명적 문제가 발생할 수 있기 때문이다.

---

# 2. Risk Level

## 2.1 Risk Classification

### [개념]

Risk Level은 Agent Action의 위험도를 Low, Medium, High, Block으로 분류하는 기준이다.

Risk Level은 Safety Decision의 기준이다.

Risk Level은 단순히 작업 이름만으로 판단하지 않는다.

다음 요소를 함께 본다.

- Side Effect
- Reversibility
- External Impact
- Cost Impact
- Security Impact
- Data Loss 가능성
- Scope 크기
- 사용자 승인 여부

---

### [핵심]

Risk Level 기준:

| Risk   | 의미                                 | 기본 처리               |
| ------ | ------------------------------------ | ----------------------- |
| Low    | 변경 없이 조회 / 설명 중심           | Allow 가능              |
| Medium | 되돌릴 수 있는 생성 / 수정 / 제안    | Preview 또는 검증       |
| High   | 삭제, 발송, 배포, DB 변경, 비용 영향 | Human Confirmation 필요 |
| Block  | Secret 노출, 악성 행위, 위험 명령    | 차단                    |

Risk 판단 Flow:

```text
Action
→ Read / Write / Delete / Send / Deploy 구분
→ Side Effect 확인
→ Reversible 확인
→ External / Cost / Security 영향 확인
→ Risk Level 결정
```

작업별 예시:

| 작업               | Risk         | 처리               |
| ------------------ | ------------ | ------------------ |
| 설명 / 요약        | Low          | Allow              |
| 파일 읽기          | Low          | Allow              |
| 로그 조회          | Low          | Allow              |
| 코드 초안 작성     | Low / Medium | Allow 또는 Preview |
| 파일 생성          | Medium       | Preview 권장       |
| 설정 파일 수정     | Medium       | Diff Preview       |
| 테스트 실행        | Medium       | 범위 확인          |
| DB 조회            | Medium       | 대상 확인          |
| 파일 삭제          | High         | 사용자 승인        |
| DB UPDATE / DELETE | High         | 사용자 승인        |
| 이메일 발송        | High         | 사용자 승인        |
| 배포 실행          | High         | 사용자 승인        |
| 유료 API 대량 호출 | High         | 사용자 승인        |
| Secret 전체 출력   | Block        | 차단               |
| 악성 명령 실행     | Block        | 차단               |

---

### [실무]

Risk Level은 환경과 범위에 따라 달라진다.

예시:

```text
Action:
SQL SELECT 실행

Risk:
Medium

Reason:
- DB 접근
- 조회 작업이지만 대상 DB 확인 필요
```

```text
Action:
SQL DELETE 실행

Risk:
High

Reason:
- 데이터 삭제
- 복구 어려움
- 사용자 승인 필요
```

```text
Action:
테스트용 파일 1개 생성

Risk:
Medium

Reason:
- 파일 생성 Side Effect 있음
- 되돌릴 수 있음
```

```text
Action:
프로젝트 전체 파일 일괄 수정

Risk:
High

Reason:
- 대량 변경
- Regression 위험
- 승인 및 Preview 필요
```

Risk Report 예시:

```md
| Action       | Side Effect | Reversible | Risk   | Decision   |
| ------------ | ----------- | ---------- | ------ | ---------- |
| 파일 읽기    | 없음        | 해당 없음  | Low    | Allow      |
| 설정 수정    | 있음        | 가능       | Medium | Preview    |
| DB 삭제      | 있음        | 어려움     | High   | Ask / Stop |
| API Key 출력 | 보안 영향   | 불가       | Block  | Block      |
```

---

### [주의]

Risk Level 주의사항:

- 같은 작업도 운영 환경이면 위험도가 올라간다.
- 대량 작업은 단일 작업보다 위험도가 높다.
- 읽기 작업도 민감정보가 포함되면 위험도가 올라간다.
- 비용 발생 가능성이 있으면 사용자 확인이 필요하다.
- 자동 Retry는 중복 실행 위험을 높인다.
- 위험도가 불명확하면 낮게 판단하지 않는다.

---

### [Best Practice]

Risk Level Best Practice:

- 작업 실행 전에 Risk Level을 먼저 정한다.
- 읽기 / 쓰기 / 삭제 / 발송 / 배포를 구분한다.
- 되돌릴 수 있는지 확인한다.
- 운영 환경 여부를 확인한다.
- 대량 작업 여부를 확인한다.
- 비용과 보안 영향을 확인한다.
- High Risk는 명시적 승인 전 Stop한다.
- Block은 요청이 있어도 실행하지 않는다.

---

### [FAQ]

Q. Risk Level은 뭐야?
A. Agent Action의 위험도를 Low, Medium, High, Block으로 분류하는 기준이다.

Q. Low Risk는 뭐야?
A. 설명, 검색, 파일 읽기처럼 변경 영향이 거의 없는 작업이다.

Q. Medium Risk는 뭐야?
A. 파일 생성, 설정 변경 제안처럼 검증 후 진행 가능한 작업이다.

Q. High Risk는 뭐야?
A. 삭제, DB 변경, 발송, 배포, 비용 발생처럼 사용자 승인이 필요한 작업이다.

Q. Block은 뭐야?
A. Secret 노출, 악성 행위, 위험 명령처럼 실행하면 안 되는 작업이다.

---

# 3. Human Confirmation

## 3.1 Confirmation Rule

### [개념]

Human Confirmation은 High Risk 작업을 실행하기 전에 사용자에게 실행 내용, 영향 범위, 위험도, 되돌릴 수 있는지 명확히 보여주고 승인을 받는 절차다.

Human Confirmation은 단순한 “할까요?”가 아니다.

Human Confirmation은 사용자가 무엇을 승인하는지 명확히 알 수 있어야 한다.

---

### [핵심]

Human Confirmation 필요 작업:

- 파일 삭제
- 대량 파일 수정
- DB INSERT / UPDATE / DELETE
- DB 초기화
- 운영 환경 변경
- 배포 실행
- 서버 재시작
- 이메일 / 메시지 발송
- 결제 / 비용 발생 작업
- 권한 변경
- Secret 관련 작업
- 되돌리기 어려운 설정 변경

Confirmation 필수 요소:

| 요소             | 설명                                |
| ---------------- | ----------------------------------- |
| Action Preview   | 실행할 작업 내용                    |
| Affected Target  | 영향 받는 파일 / DB / 계정 / 시스템 |
| Risk Level       | 위험도                              |
| Side Effect      | 발생할 변경                         |
| Reversibility    | 되돌릴 수 있는지                    |
| Cost Impact      | 비용 발생 가능성                    |
| Scope Limit      | 승인 범위                           |
| Confirm / Cancel | 승인 또는 취소 선택                 |

Confirmation Flow:

```text
High Risk Action
→ Prepare Preview
→ Show Target / Risk / Side Effect
→ Ask Confirm / Cancel
→ Execute only if Confirmed
```

---

### [실무]

좋은 Confirmation 예시:

```md
### Human Confirmation Required

Action:

- Execute SQL DELETE

Target:

- database: production
- table: notifications
- condition: created_at < '2026-01-01'

Risk Level:

- High

Side Effect:

- 조건에 맞는 데이터가 삭제됨

Reversible:

- 백업 없으면 복구 어려움

Required Confirmation:

- 위 조건으로 삭제 승인
```

나쁜 Confirmation 예시:

```text
이거 처리할까요?
```

문제:

- Action 불명확
- Target 불명확
- Risk 없음
- Side Effect 없음
- 승인 범위 모호

이메일 발송 예시:

```md
### Human Confirmation Required

Action:

- Send Email

Target:

- recipient: user@example.com
- subject: 프로젝트 검토 결과

Risk Level:

- High

Side Effect:

- 외부 수신자에게 이메일이 발송됨

Required Confirmation:

- 이메일 발송 승인
```

---

### [주의]

Human Confirmation 주의사항:

- 모호한 동의를 승인으로 해석하지 않는다.
- 초안 작성 승인과 실제 발송 승인은 다르다.
- 승인 후 실행 내용이 바뀌면 다시 확인해야 한다.
- 승인 범위를 넘는 추가 작업은 하지 않는다.
- 되돌릴 수 없는 작업은 특별히 강조한다.
- 사용자가 승인하지 않으면 Stop 상태로 유지한다.
- Block 대상은 승인 여부와 무관하게 실행하지 않는다.

---

### [Best Practice]

Human Confirmation Best Practice:

- Action Preview를 먼저 제공한다.
- 영향 대상과 위험도를 명확히 표시한다.
- 되돌릴 수 있는지 설명한다.
- 비용 발생 가능성을 표시한다.
- 승인 문구를 구체적으로 요구한다.
- 승인 범위를 제한한다.
- 실행 전 마지막 Arguments를 검증한다.
- 실행 후 결과를 검증한다.
- 승인 없는 추가 작업은 하지 않는다.

---

### [FAQ]

Q. Human Confirmation이 뭐야?
A. 위험 작업 실행 전 사용자에게 작업 내용과 위험을 보여주고 명시적 승인을 받는 절차다.

Q. “진행해”라고 하면 충분해?
A. 작업 내용과 영향 범위가 이미 명확히 제시된 경우에만 충분할 수 있다.

Q. 초안 작성 승인과 발송 승인은 같아?
A. 아니다. 실제 발송은 별도 승인이 필요하다.

Q. 승인 후 다른 작업도 같이 해도 돼?
A. 안 된다. 승인 범위를 넘으면 다시 확인해야 한다.

Q. Block 작업도 승인받으면 가능해?
A. 아니다. Block 대상은 승인 여부와 무관하게 실행하지 않는다.

---

# 4. Scope Safety

## 4.1 Scope Boundary

### [개념]

Scope Safety는 Agent가 사용자 요청 범위와 승인 범위를 벗어나지 않도록 제한하는 규칙이다.

Scope Safety는 “무엇을 할 수 있는가”보다 “어디까지 할 수 있는가”를 정의한다.

Scope를 벗어난 작업은 좋은 개선처럼 보여도 안전 문제가 될 수 있다.

---

### [핵심]

Scope Safety 검증 항목:

| 항목               | 검증 내용                            |
| ------------------ | ------------------------------------ |
| User Request Scope | 사용자가 요청한 범위인가             |
| Approval Scope     | 승인된 작업 범위 안인가              |
| File Scope         | 대상 파일 / 디렉터리가 맞는가        |
| Data Scope         | 대상 DB / 테이블 / 레코드가 맞는가   |
| Tool Scope         | 필요한 Tool만 사용하는가             |
| Agent Role Scope   | 해당 Agent 역할 범위 안인가          |
| Project Boundary   | 다른 프로젝트 정보가 섞이지 않았는가 |

Scope Evaluation Flow:

```text
Agent Action
→ Compare with User Request
→ Check Target Scope
→ Check Approval Scope
→ Check Agent Role
→ In Scope / Ask / Out of Scope
```

Scope 판단:

```text
In Scope:
- 요청 범위와 일치
- 승인 범위와 일치
- Agent 역할과 일치

Ask:
- 범위가 애매함
- 추가 작업이 필요함
- 승인 범위 확장 필요

Out of Scope:
- 요청하지 않은 작업 수행
- 승인하지 않은 대상 변경
- 다른 Domain 작업 수행
```

---

### [실무]

파일 Scope 예시:

```text
User Request:
NotificationService만 검토해줘.

Allowed:
- NotificationService 검토
- 필요한 관련 Repository 참조

Out of Scope:
- UserService 리팩토링
- 전체 프로젝트 구조 변경
- build.gradle 수정
```

DB Scope 예시:

```text
User Request:
notifications 테이블의 오래된 테스트 데이터만 삭제

Allowed:
- notifications 테이블
- 조건에 맞는 테스트 데이터

Out of Scope:
- users 테이블 삭제
- 전체 DB 초기화
- 운영 데이터 삭제
```

Agent Role Scope 예시:

```text
Backend Agent:
- Controller / Service / Repository / DTO 검토 가능

Backend Agent Out of Scope:
- 운영 배포 실행
- 이메일 발송
- 인프라 변경
```

Scope Report 예시:

```md
| Action                   | Scope Result | Handling       |
| ------------------------ | ------------ | -------------- |
| NotificationService 검토 | In Scope     | 진행           |
| UserService 수정         | Out of Scope | 제외           |
| build.gradle 수정        | Ask          | 영향 범위 확인 |
```

---

### [주의]

Scope Safety 주의사항:

- 좋은 개선이라도 요청 범위 밖이면 실행하지 않는다.
- 관련 파일 참조와 수정은 다르다.
- 승인 범위가 좁으면 그 안에서만 작업한다.
- 다른 Agent 역할의 작업을 임의로 수행하지 않는다.
- Tool 사용 가능 여부와 작업 Scope는 다르다.
- 대량 작업은 Scope가 넓어져 위험도가 올라간다.
- 범위가 불명확하면 Ask 또는 Stop으로 처리한다.

---

### [Best Practice]

Scope Safety Best Practice:

- 작업 시작 전 User Request Scope를 정의한다.
- 수정 대상과 참조 대상을 구분한다.
- 승인 범위를 기록한다.
- Out of Scope 작업은 제안만 하고 실행하지 않는다.
- Scope 변경이 필요하면 사용자 확인을 받는다.
- Agent별 Role Boundary를 둔다.
- Tool Arguments가 Scope 내부인지 확인한다.
- Final Output에서 수행 범위를 명확히 표시한다.

---

### [FAQ]

Q. Scope Safety가 뭐야?
A. Agent가 사용자 요청 범위와 승인 범위를 벗어나지 않도록 제한하는 규칙이다.

Q. 좋은 개선이면 요청하지 않아도 해도 돼?
A. 실행하면 안 된다. 요청 범위 밖이면 제안만 하거나 사용자 확인이 필요하다.

Q. 관련 파일을 보는 것도 Scope 위반이야?
A. 참조는 가능할 수 있지만 수정은 별도 Scope와 승인이 필요하다.

Q. 승인 범위를 넘는 추가 작업은 가능해?
A. 안 된다. 추가 작업은 다시 확인해야 한다.

Q. Scope가 불명확하면 어떻게 해?
A. Ask 또는 Stop으로 처리하고 임의로 확정하지 않는다.

---

# 5. Secret & Sensitive Data Safety

## 5.1 Secret Protection

### [개념]

Secret Protection은 API Key, Token, Password, 인증 정보, 개인 식별 정보, 민감 데이터를 Agent Output, Tool Arguments, Log, Memory에 노출하거나 저장하지 않도록 보호하는 규칙이다.

Secret 노출은 Safety Guardrails에서 Block 대상이다.

Secret은 사용자가 직접 제공했더라도 불필요하게 다시 출력하거나 저장하면 안 된다.

---

### [핵심]

Secret / Sensitive Data 예시:

| 유형              | 예시                             |
| ----------------- | -------------------------------- |
| API Key           | OpenAI Key, Kakao Key, Toss Key  |
| Token             | JWT, Refresh Token, Access Token |
| Password          | DB Password, 계정 Password       |
| Private Key       | SSH Key, 인증서 Private Key      |
| Connection String | DB URL + Password                |
| Cookie / Session  | Session ID, 인증 Cookie          |
| Personal Data     | 주민번호, 전화번호, 주소 등      |
| Payment Data      | 카드 정보, 결제 인증 정보        |

Secret Handling 기준:

```text
Allow:
- Secret 없이 일반 설명

Mask:
- 일부 값만 표시 필요
- 예: sk-****abcd

Remove:
- 출력 불필요한 Secret

Block:
- Secret 전체 출력 요청
- 인증 우회 목적
- 위험한 유출 가능성
```

Secret Protection Flow:

```text
Content / Tool Result
→ Detect Secret
→ Mask or Remove
→ Avoid Logging
→ Avoid Memory Save
→ Block if Exposure Risk
```

---

### [실무]

설정 파일 예시:

```properties
spring.datasource.password=****
tourapi.service-key=****
jwt.secret=****
```

좋은 처리:

```text
- 설정 Key 이름은 설명 가능
- 실제 Secret 값은 마스킹
- 코드 예시는 placeholder 사용
```

나쁜 처리:

```text
- 전체 API Key를 그대로 답변에 표시
- Token을 로그에 남김
- Memory에 비밀번호 저장
- GitHub에 Secret 포함 코드 작성
```

Secret Report 예시:

```md
| Item          | Risk      | Handling |
| ------------- | --------- | -------- |
| API Key       | Secret    | Mask     |
| DB Password   | Secret    | Remove   |
| JWT Token     | Sensitive | Mask     |
| 설정 Key 이름 | Low       | Allow    |
```

---

### [주의]

Secret Protection 주의사항:

- Secret은 사용자가 제공했더라도 반복 출력하지 않는다.
- Secret을 Memory에 저장하지 않는다.
- Secret이 포함된 로그를 그대로 복사하지 않는다.
- 코드 블록에 실제 Secret을 넣지 않는다.
- Tool Arguments에 Secret을 불필요하게 포함하지 않는다.
- Secret 마스킹이 불완전하면 여전히 위험할 수 있다.
- 인증 우회나 권한 탈취 목적 요청은 차단한다.

---

### [Best Practice]

Secret Protection Best Practice:

- Secret Pattern을 감지한다.
- 값은 마스킹하고 Key 이름만 설명한다.
- 코드 예시는 placeholder를 사용한다.
- `.env`, 환경 변수, Secret Manager 사용을 권장한다.
- 로그 출력 시 Secret을 제거한다.
- Tool Result를 사용자에게 보여주기 전 민감정보를 필터링한다.
- Memory 저장 전 민감정보 여부를 확인한다.
- Secret 전체 값 요청은 거부한다.

---

### [FAQ]

Q. Secret Protection이 뭐야?
A. API Key, Token, Password 같은 민감 정보를 출력, 저장, 로그에 남기지 않도록 보호하는 규칙이다.

Q. 사용자가 Secret을 직접 줬으면 다시 출력해도 돼?
A. 불필요하게 다시 출력하면 안 된다. 필요한 경우 마스킹해야 한다.

Q. Secret은 어떻게 표시해야 해?
A. 전체 값을 표시하지 말고 `****` 또는 placeholder로 마스킹해야 한다.

Q. 설정 Key 이름은 말해도 돼?
A. 일반적으로 가능하다. 실제 Secret 값은 출력하지 않는다.

Q. Secret을 Memory에 저장해도 돼?
A. 안 된다. Secret은 Memory에 저장하면 안 된다.

---

# 6. Safety Stop Condition

## 6.1 Safety Stop

### [개념]

Safety Stop은 Agent가 위험하거나 불확실한 작업을 안전하게 진행할 수 없을 때 중단하는 기준이다.

Safety Stop은 실패를 숨기는 것이 아니라 안전하게 멈추는 정상 동작이다.

Safety Stop은 다음 상황에서 필요하다.

- High Risk 작업에 승인 없음
- Secret 노출 위험
- 작업 범위 불명확
- Tool Arguments 위험
- 운영 환경 영향 가능
- 되돌리기 어려운 변경
- Safety Block 대상 감지
- Low Confidence 상태에서 위험 작업 요구

---

### [핵심]

Safety Stop 기준:

```text
Stop if:
- Human Confirmation Required but Missing
- Secret Exposure Risk Exists
- Target Scope is Unclear
- Tool Arguments are Dangerous
- Action is Irreversible
- Production Impact is Possible
- Cost Impact is Unclear
- Block Rule Triggered
```

Safety Stop Report 필수 요소:

| 요소            | 설명             |
| --------------- | ---------------- |
| Stop Reason     | 중단 사유        |
| Risk Level      | 위험도           |
| Affected Target | 영향 대상        |
| Evidence        | 중단 근거        |
| Required Action | 필요한 다음 조치 |
| Can Resume      | 재개 가능 조건   |

Safety Stop Report 예시:

```md
# Safety Stop

## Reason

- Human Confirmation Required

## Risk Level

- High

## Affected Target

- production database / notifications table

## Evidence

- DELETE 작업이며 사용자 승인 없음

## Required Action

- 대상 DB, 테이블, 조건절 확인
- 백업 여부 확인
- 사용자 명시 승인 필요

## Can Resume

- 명시 승인 후 재개 가능
```

---

### [실무]

Safety Stop 예시:

```text
User Request:
운영 DB에서 오래된 데이터 삭제해줘.

Safety Decision:
Stop

Reason:
- DB DELETE
- High Risk
- Human Confirmation 필요
```

Safety Stop 예시:

```text
User Request:
.env 파일 내용 보여줘.

Safety Decision:
Stop or Partial

Reason:
- Secret 포함 가능성
- 전체 출력 위험

Safe Handling:
- Key 이름만 표시
- 값은 마스킹
```

Safety Stop 예시:

```text
User Request:
프로젝트 전체 파일 자동으로 수정해줘.

Safety Decision:
Ask or Stop

Reason:
- 대량 파일 수정
- Scope 불명확
- Regression 위험
```

---

### [주의]

Safety Stop 주의사항:

- Safety Stop을 실패처럼 숨기지 않는다.
- Stop Reason 없이 중단하지 않는다.
- 승인 필요 상태를 완료 상태로 말하지 않는다.
- Block 대상은 사용자 승인으로도 재개하지 않는다.
- Secret 포함 가능성이 있으면 전체 출력하지 않는다.
- Stop 후 재개 조건을 명확히 표시한다.
- Safety Stop은 Workflow Stop Condition보다 우선할 수 있다.

---

### [Best Practice]

Safety Stop Best Practice:

- Stop Reason을 짧고 명확하게 작성한다.
- Risk Level과 영향 대상을 포함한다.
- 필요한 사용자 조치를 표시한다.
- Partial Safe Output이 가능하면 제공한다.
- Secret은 마스킹한 범위에서만 다룬다.
- High Risk 작업은 Preview 후 승인 요청으로 전환한다.
- Block 대상은 우회하지 않는다.
- Stop 결과를 Evaluation Report에 기록한다.

---

### [FAQ]

Q. Safety Stop이 뭐야?
A. Agent가 위험하거나 불확실한 작업을 안전하게 진행할 수 없을 때 중단하는 기준이다.

Q. Safety Stop은 실패야?
A. 아니다. 위험 작업을 안전하게 막는 정상 동작이다.

Q. 언제 Safety Stop해야 해?
A. 승인 없는 High Risk 작업, Secret 노출 위험, 범위 불명확, 위험 Arguments, 되돌리기 어려운 작업일 때 Stop해야 한다.

Q. Safety Stop 후 다시 진행할 수 있어?
A. 사용자 확인이나 안전 조건이 충족되면 재개할 수 있다. Block 대상은 재개하면 안 된다.

Q. Stop Reason은 왜 필요해?
A. 사용자가 무엇 때문에 멈췄고 무엇을 확인해야 하는지 알 수 있어야 하기 때문이다.

---

# 7. Safety Checklist

## 7.1 Safety Guardrails Checklist

### [개념]

Safety Guardrails Checklist는 Agent Action이 안전하게 진행 가능한지 확인하는 최소 검증 목록이다.

이 Checklist는 Safety Agent, PM Agent, Review Agent, Tool Agent가 공통으로 사용할 수 있다.

---

### [핵심]

Safety Pre-Action Checklist:

```md
### [Checklist]

- [ ] 사용자 요청 범위 안의 작업인가?
- [ ] Agent 역할 범위 안의 작업인가?
- [ ] Risk Level을 분류했는가?
- [ ] Side Effect가 있는가?
- [ ] 되돌릴 수 있는 작업인가?
- [ ] 외부 시스템에 영향을 주는가?
- [ ] 비용이 발생할 수 있는가?
- [ ] Secret / 민감정보가 포함되는가?
- [ ] 대상 파일 / DB / 계정 / 시스템이 명확한가?
- [ ] Human Confirmation이 필요한가?
- [ ] 승인 범위가 명확한가?
- [ ] Safety Stop이 필요한가?
```

Safety Post-Action Checklist:

```md
### [Checklist]

- [ ] 실행 결과가 성공 / 실패 / 부분 성공 중 무엇인가?
- [ ] Side Effect 발생 여부를 확인했는가?
- [ ] 승인된 범위 안에서만 실행되었는가?
- [ ] Secret이 출력 또는 저장되지 않았는가?
- [ ] 실패를 성공처럼 처리하지 않았는가?
- [ ] 추가 위험 작업이 필요한 경우 다시 확인했는가?
- [ ] 결과와 한계를 명확히 보고했는가?
```

최소 Pass 기준:

```text
- Scope 안의 작업
- Risk Level 확인
- Secret 노출 없음
- High Risk 승인 확인
- Side Effect 통제
- Safety Stop 조건 없음
```

---

### [실무]

Safety Checklist 적용 Flow:

```text
Agent Action
→ Pre-Action Safety Check
→ Allow / Ask / Stop / Block
→ Execute if Allowed
→ Post-Action Safety Check
→ Report Result
```

Safety Decision Report 예시:

```md
### Safety Decision

- Action:
- Risk Level:
- Side Effect:
- Human Confirmation Required:
- Decision: Allow / Ask / Stop / Block
- Reason:
```

Safety Evaluation Result 예시:

```md
| Item               | Result | Evidence         | Handling     |
| ------------------ | ------ | ---------------- | ------------ |
| Scope              | Pass   | 요청 파일만 대상 | 진행         |
| Risk Level         | High   | DB DELETE        | 승인 필요    |
| Secret             | Pass   | Secret 없음      | 진행         |
| Human Confirmation | Fail   | 승인 없음        | Stop         |
| Side Effect        | High   | 데이터 삭제      | Preview 필요 |
```

---

### [주의]

Safety Checklist 주의사항:

- Checklist는 최소 기준이며 세부 정책을 대체하지 않는다.
- High Risk 작업은 Checklist를 통과해도 사용자 승인 전 실행할 수 없다.
- Secret 노출은 즉시 Block한다.
- Scope가 불명확하면 Ask 또는 Stop으로 처리한다.
- Side Effect가 있으면 실행 후 결과를 검증해야 한다.
- 자동화 범위가 넓을수록 위험도는 올라간다.
- Safety Decision은 Output Evaluation과 별도로 기록한다.

---

### [Best Practice]

Safety Checklist Best Practice:

- 실행 전과 실행 후 Checklist를 분리한다.
- Risk Level을 항상 기록한다.
- High Risk 작업은 Action Preview를 제공한다.
- Block 사유를 명확히 기록한다.
- Secret 값은 마스킹한다.
- Tool Result의 실패와 한계를 숨기지 않는다.
- Safety Stop을 명확히 둔다.
- Safety Finding은 Critical / Major로 우선 처리한다.

---

### [FAQ]

Q. Safety Guardrails Checklist는 뭐야?
A. Agent Action이 안전하게 진행 가능한지 확인하기 위한 최소 검증 목록이다.

Q. Safety Checklist는 언제 써?
A. Agent Action 실행 전과 실행 후에 사용한다.

Q. Safety Checklist에서 가장 중요한 항목은 뭐야?
A. Scope, Risk Level, Side Effect, Secret, Human Confirmation, Safety Stop 여부다.

Q. High Risk 작업이 Checklist를 통과하면 바로 실행해도 돼?
A. 아니다. High Risk 작업은 사용자 승인 전 실행하면 안 된다.

Q. Secret이 발견되면 어떻게 해?
A. 출력하지 말고 마스킹하거나 제거하며, 전체 노출 요청은 Block한다.

---

# Retrieval Queries

### [FAQ]

Q. Safety Guardrails가 뭐야?
A. Agent가 위험하거나 되돌리기 어려운 행동을 하지 않도록 제한하는 안전 규칙이다.

Q. Safety Guardrails는 무엇을 판단해?
A. Agent Action을 Allow, Ask, Stop, Block 중 하나로 분류한다.

Q. Safety Guardrails는 Tool Calling Evaluation과 어떻게 달라?
A. Tool Calling Evaluation은 Tool 선택과 실행 검증이고, Safety Guardrails는 위험도, 승인 조건, 차단 조건 판단이다.

Q. Safety Decision Flow는 어떻게 돼?
A. Agent Action → Scope Check → Risk Check → Side Effect Check → Secret Check → Confirmation Check → Allow / Ask / Block / Stop 순서다.

Q. Risk Level은 뭐야?
A. Agent Action의 위험도를 Low, Medium, High, Block으로 분류하는 기준이다.

Q. Low Risk 작업은 뭐야?
A. 설명, 검색, 파일 읽기처럼 변경 영향이 거의 없는 작업이다.

Q. Medium Risk 작업은 뭐야?
A. 파일 생성, 설정 변경 제안처럼 검증 후 진행 가능한 작업이다.

Q. High Risk 작업은 뭐야?
A. 삭제, DB 변경, 발송, 배포, 비용 발생처럼 사용자 승인이 필요한 작업이다.

Q. Block 작업은 뭐야?
A. Secret 노출, 악성 행위, 위험 명령처럼 실행하면 안 되는 작업이다.

Q. 위험도가 애매하면 어떻게 해?
A. Allow로 처리하지 말고 Ask 또는 Stop으로 처리해야 한다.

Q. Human Confirmation이 뭐야?
A. 위험 작업 실행 전 사용자에게 작업 내용과 위험을 보여주고 명시적 승인을 받는 절차다.

Q. Human Confirmation은 언제 필요해?
A. 파일 삭제, DB 변경, 배포, 이메일 발송, 결제, 비용 발생 작업처럼 High Risk 작업 전에 필요하다.

Q. Action Preview에는 뭐가 들어가?
A. 실행할 작업, 영향 대상, 위험도, Side Effect, 되돌릴 수 있는지, 비용 영향, 승인 범위가 들어간다.

Q. 초안 작성 승인과 발송 승인은 같아?
A. 아니다. 실제 발송은 별도 승인이 필요하다.

Q. Block 작업도 승인받으면 가능해?
A. 아니다. Block 대상은 승인 여부와 무관하게 실행하지 않는다.

Q. Scope Safety가 뭐야?
A. Agent가 사용자 요청 범위와 승인 범위를 벗어나지 않도록 제한하는 규칙이다.

Q. 좋은 개선이면 요청하지 않아도 해도 돼?
A. 실행하면 안 된다. 요청 범위 밖이면 제안만 하거나 사용자 확인이 필요하다.

Q. 관련 파일을 보는 것도 Scope 위반이야?
A. 참조는 가능할 수 있지만 수정은 별도 Scope와 승인이 필요하다.

Q. 승인 범위를 넘는 추가 작업은 가능해?
A. 안 된다. 추가 작업은 다시 확인해야 한다.

Q. Secret Protection이 뭐야?
A. API Key, Token, Password 같은 민감 정보를 출력, 저장, 로그에 남기지 않도록 보호하는 규칙이다.

Q. 사용자가 Secret을 직접 줬으면 다시 출력해도 돼?
A. 불필요하게 다시 출력하면 안 된다. 필요한 경우 마스킹해야 한다.

Q. Secret은 어떻게 표시해야 해?
A. 전체 값을 표시하지 말고 `****` 또는 placeholder로 마스킹해야 한다.

Q. Secret을 Memory에 저장해도 돼?
A. 안 된다. Secret은 Memory에 저장하면 안 된다.

Q. Safety Stop이 뭐야?
A. Agent가 위험하거나 불확실한 작업을 안전하게 진행할 수 없을 때 중단하는 기준이다.

Q. Safety Stop은 실패야?
A. 아니다. 위험 작업을 안전하게 막는 정상 동작이다.

Q. 언제 Safety Stop해야 해?
A. 승인 없는 High Risk 작업, Secret 노출 위험, 범위 불명확, 위험 Arguments, 되돌리기 어려운 작업일 때 Stop해야 한다.

Q. Safety Stop Report에는 뭐가 필요해?
A. Stop Reason, Risk Level, Affected Target, Evidence, Required Action, Can Resume 조건이 필요하다.

Q. Safety Guardrails Checklist는 언제 써?
A. Agent Action 실행 전과 실행 후에 사용한다.

Q. Safety Checklist 최소 Pass 기준은 뭐야?
A. Scope 안의 작업, Risk Level 확인, Secret 노출 없음, High Risk 승인 확인, Side Effect 통제, Safety Stop 조건 없음이다.

Q. Safety Guardrails의 최종 목표는 뭐야?
A. Agent가 사용자 요청 범위 안에서 안전하게 작업하고, 위험 작업은 승인과 검증을 거치며, 허용 불가 작업은 차단하도록 만드는 것이다.
