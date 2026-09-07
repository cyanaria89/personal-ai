# Agent Workflow Design Part04 Review Fix Evaluation

---

# 1. Review Agent Core

## 1.1 Review Agent Definition

### [개념]

Review Agent는 Domain Agent 또는 Fix Agent의 산출물을 요구사항, Domain Rules, Project Rules, Done Criteria 기준으로 검증하는 Agent이다.

Review Agent는 구현자가 아니다.
Review Agent의 핵심 역할은 산출물의 문제, 원인, 영향, 위험도, 수정 방향을 구조화해서 제시하는 것이다.

Review Agent는 다음을 검증한다.

- Requirement Satisfaction
- Domain Rules Compliance
- Project Rules Compliance
- Output Format
- Security Risk
- Data Integrity
- API Contract
- Failure Handling
- Stop Condition
- Done Criteria

---

### [핵심]

- Review Agent는 산출물 품질 검증 담당이다.
- Review Agent는 구현보다 검증에 집중한다.
- Review 기준은 명확해야 한다.
- 문제, 원인, 영향, 수정 방향을 분리한다.
- Severity를 통해 우선순위를 판단한다.
- Finding은 Fix Agent가 바로 사용할 수 있어야 한다.
- 취향과 결함을 구분한다.
- 일부 코드만 보고 전체 시스템을 단정하지 않는다.
- 근거 없는 지적은 금지한다.

---

### [실무]

2026 실무 기준 Review Agent는 Multi-Agent Workflow의 품질 게이트 역할을 수행한다.

기본 Flow:

```text
Agent Output
→ Check Against Requirements
→ Check Domain Rules
→ Check Project Rules
→ Find Issues
→ Assign Severity
→ Suggest Fix
→ Pass or Return to Fix
```

Review Agent 입력:

| Input                  | 설명                  |
| ---------------------- | --------------------- |
| Review Target          | 검토 대상 산출물      |
| Original Requirement   | 원본 사용자 요구사항  |
| Constraints            | 지켜야 할 제약 조건   |
| Domain Rules           | 해당 Domain 검토 기준 |
| Project Rules          | 프로젝트 공통 규칙    |
| Done Criteria          | 완료 판단 기준        |
| Severity Rule          | 위험도 분류 기준      |
| Expected Review Output | Review 결과 형식      |

Review Agent 출력:

| Output             | 설명                         |
| ------------------ | ---------------------------- |
| Summary            | 검토 요약                    |
| Pass / Fail        | 통과 여부                    |
| Findings           | 문제 목록                    |
| Severity           | Critical, Major, Minor, Info |
| Cause              | 문제 원인                    |
| Impact             | 영향                         |
| Fix Direction      | 수정 방향                    |
| Re-review Required | 재검토 필요 여부             |

---

### [FAQ]

Q. Review Agent는 뭐야?
A. Domain Agent 산출물을 요구사항, Domain Rules, Project Rules, Done Criteria 기준으로 검증하는 Agent이다.

Q. Review Agent는 구현도 해?
A. 아니다. Review Agent는 구현보다 검증, 문제 식별, 영향 분석, 수정 방향 제시에 집중한다.

Q. Review Agent가 중요한 이유는?
A. Domain Agent 결과를 독립적으로 검증해 누락, 오류, 위험, 규칙 위반을 발견하기 위해 필요하다.

Q. Review Agent 결과는 누가 사용해?
A. PM Agent와 Fix Agent가 사용한다.

---

# 2. Review Criteria

## 2.1 Review Criteria Definition

### [개념]

Review Criteria는 Review Agent가 산출물을 검증할 때 사용하는 기준이다.

Review Criteria가 없으면 Review Agent는 취향 기반 지적을 하거나 중요한 결함을 놓칠 수 있다.

Review Criteria는 다음과 연결되어야 한다.

- Original Requirement
- PM Agent Handoff
- Domain Rules
- Project Rules
- Done Criteria
- Security Rules
- API Contract
- Output Format

---

### [핵심]

- Review Criteria는 명확하고 검증 가능해야 한다.
- 요구사항 충족 여부를 우선 검토한다.
- Domain Rules 위반 여부를 확인한다.
- Project Rules와 충돌 여부를 확인한다.
- Done Criteria 충족 여부를 확인한다.
- 보안, 데이터 손실, 비용 발생 위험은 높은 우선순위로 검토한다.
- 취향과 결함을 구분한다.
- Review 기준은 Loop 중간에 임의로 바꾸지 않는다.

---

### [실무]

Review Criteria Template:

```md
## Review Criteria

### Requirement Check

### Domain Rule Check

### Project Rule Check

### Output Format Check

### Security Check

### Data Integrity Check

### API Contract Check

### Failure Handling Check

### Done Criteria Check

### Stop Condition Check
```

예시:

```md
## Review Criteria

### Requirement Check

- 회원가입 API 설계 요구사항 충족 여부
- DTO, Service Flow, Controller Endpoint 포함 여부

### Domain Rule Check

- Backend Domain Rules 준수 여부
- Security Domain Rules 준수 여부

### Project Rule Check

- ApiResponse<T> 직접 반환 기준 준수
- GlobalExceptionHandler 사용 기준 준수

### Security Check

- Password 평문 저장 금지
- BCrypt Encoding 포함 여부

### API Contract Check

- Endpoint, Request, Response 형식 명확성
- Frontend 연동 영향 명시 여부

### Done Criteria Check

- 중복 이메일 처리 포함
- Validation 포함
- Exception Cases 포함
```

주의:

- 기준 없는 Review 금지
- 단순 선호를 결함으로 분류 금지
- Review Criteria를 매 반복마다 변경 금지
- 근거 없는 위험 단정 금지
- Review 대상 밖의 기능까지 과도하게 지적 금지

---

### [FAQ]

Q. Review Criteria는 뭐야?
A. Review Agent가 산출물을 검증할 때 사용하는 명확한 기준이다.

Q. Review Criteria에는 무엇이 들어가?
A. Requirement Check, Domain Rule Check, Project Rule Check, Security Check, API Contract Check, Done Criteria Check가 들어간다.

Q. Review Criteria가 없으면 어떻게 돼?
A. Review Agent가 취향 기반 지적을 하거나 중요한 결함을 놓칠 수 있다.

Q. Review Criteria는 중간에 바꿔도 돼?
A. 원칙적으로 Review / Fix Loop 중간에 임의로 바꾸면 안 된다.

---

# 3. Review Finding

## 3.1 Review Finding Definition

### [개념]

Review Finding은 Review Agent가 발견한 문제를 구조화한 검토 결과이다.

Finding은 단순히 “문제가 있음”이라고 쓰지 않는다.
문제, 원인, 영향, 수정 방향, 위험도, 통과 여부를 분리해서 작성한다.

필수 요소:

- Issue
- Severity
- Evidence
- Cause
- Impact
- Fix Direction
- Owner Agent
- Pass / Fail
- Re-review Required

---

### [핵심]

- Finding은 Fix Agent가 바로 사용할 수 있어야 한다.
- Issue는 구체적으로 작성한다.
- Evidence는 산출물의 어떤 부분에서 발견했는지 표시한다.
- Cause는 왜 문제가 발생했는지 설명한다.
- Impact는 문제가 남을 때의 영향을 설명한다.
- Fix Direction은 수정 방법을 제시한다.
- Severity는 우선순위 판단에 사용한다.
- Owner Agent를 지정하면 Fix Routing이 쉬워진다.

---

### [실무]

Review Finding Template:

```md
## Review Finding

### Issue

### Severity

Critical / Major / Minor / Info

### Evidence

### Cause

### Impact

### Fix Direction

### Owner Agent

### Pass / Fail

### Re-review Required

Yes / No
```

예시:

```md
## Review Finding

### Issue

회원가입 Service Flow에 Password Encoding 단계가 명시되지 않음.

### Severity

Critical

### Evidence

Backend Agent Output의 Service Flow에 passwordEncoder.encode() 단계 없음.

### Cause

Security 요구사항이 Backend Flow에 반영되지 않음.

### Impact

Password가 평문 저장될 가능성이 있으며 심각한 보안 문제가 발생할 수 있음.

### Fix Direction

User 저장 전에 passwordEncoder.encode(rawPassword)를 적용하는 단계를 Service Flow에 추가한다.

### Owner Agent

Backend Agent / Security Agent

### Pass / Fail

Fail

### Re-review Required

Yes
```

좋은 Finding 조건:

- 문제 위치가 명확함
- 영향이 구체적임
- 수정 방향이 실행 가능함
- Severity가 적절함
- Fix Agent가 바로 작업 가능함

---

### [FAQ]

Q. Review Finding은 뭐야?
A. Review Agent가 발견한 문제를 Issue, Severity, Evidence, Cause, Impact, Fix Direction으로 구조화한 결과이다.

Q. 좋은 Finding 조건은?
A. 문제 위치, 원인, 영향, 수정 방향, 담당 Agent가 명확해야 한다.

Q. Finding에 Fix Direction이 꼭 필요해?
A. 필요하다. Fix Direction이 없으면 Fix Agent가 어떻게 수정해야 할지 판단하기 어렵다.

Q. Finding에 Evidence를 왜 넣어?
A. 근거 없는 지적을 막고 Fix Agent가 문제 위치를 빠르게 찾기 위해 필요하다.

---

# 4. Severity Rules

## 4.1 Severity Definition

### [개념]

Severity는 Review Finding의 위험도와 수정 우선순위를 나타내는 기준이다.

Severity는 감정적 표현이 아니라 작업 우선순위와 Stop Condition을 결정하는 구조적 기준이다.

기본 Severity:

- Critical
- Major
- Minor
- Info

---

### [핵심]

- Critical은 즉시 수정이 필요한 치명적 문제이다.
- Major는 핵심 요구사항 또는 주요 동작에 영향을 주는 문제이다.
- Minor는 품질 개선 또는 작은 누락이다.
- Info는 참고 의견이다.
- Critical 또는 Major가 있으면 일반적으로 Review Fail이다.
- Minor만 있으면 조건부 Pass 가능하다.
- Severity 기준은 Review 전에 정의해야 한다.

---

### [실무]

Severity Table:

| Severity | 기준                                                   | 처리                        |
| -------- | ------------------------------------------------------ | --------------------------- |
| Critical | 보안 위험, 데이터 손실, 실행 불가, 위험 작업 자동 실행 | 즉시 Fix, Final Output 금지 |
| Major    | 핵심 요구사항 누락, API 계약 불일치, 주요 흐름 오류    | Fix 필요, Re-review 권장    |
| Minor    | 문서 보강, 작은 예외 누락, 명명 개선                   | Fix 권장 또는 조건부 Pass   |
| Info     | 참고 의견, 선택 개선 사항                              | Pass 가능                   |

예시:

```md
## Severity Rule

### Critical

- Password 평문 저장
- DB 삭제 작업 승인 없이 실행
- Secret 노출
- 실행 불가능한 핵심 코드
- 데이터 손실 가능성

### Major

- 필수 요구사항 누락
- API Request / Response 불일치
- Validation 누락
- Exception Flow 누락
- 기존 프로젝트 규칙 위반

### Minor

- Naming Consistency 부족
- FAQ 보강 필요
- Error Message 개선 필요
- 작은 중복 설명

### Info

- 향후 개선 제안
- 선택 기능 제안
- 참고 링크 또는 참고 패턴
```

Pass 기준:

```text
Pass:
- Critical 없음
- Major 없음
- Minor만 존재하거나 Info만 존재

Fail:
- Critical 1개 이상
- Major 1개 이상
- Done Criteria 핵심 항목 미충족
```

---

### [FAQ]

Q. Severity는 뭐야?
A. Review Finding의 위험도와 수정 우선순위를 나타내는 기준이다.

Q. Critical은 어떤 문제야?
A. 보안 위험, 데이터 손실, 실행 불가, Secret 노출, 위험 작업 자동 실행 같은 치명적 문제이다.

Q. Major는 어떤 문제야?
A. 핵심 요구사항 누락, API 계약 불일치, Validation 누락, 주요 흐름 오류 같은 문제이다.

Q. Minor가 있으면 Fail이야?
A. 반드시 Fail은 아니다. Critical과 Major가 없고 Minor만 있으면 조건부 Pass가 가능하다.

---

# 5. Fix Agent Core

## 5.1 Fix Agent Definition

### [개념]

Fix Agent는 Review Agent가 발견한 Finding을 기준으로 산출물을 수정하는 Agent이다.

Fix Agent는 임의로 새로운 기능을 추가하는 Agent가 아니다.
Fix Agent는 Review Finding, Fix Scope, 기존 요구사항, 기존 동작 보존 기준을 따라 수정한다.

Fix Agent 핵심 역할:

- Review Findings 분석
- Fix Scope 결정
- Priority 기반 수정
- Existing Behavior 보존
- Updated Output 생성
- Change Summary 작성
- Re-review 요청

---

### [핵심]

- Fix Agent는 Review Finding을 기준으로 수정한다.
- Critical과 Major를 우선 수정한다.
- 기존 요구사항을 보존해야 한다.
- 기존 API / DTO / DB 계약 변경 시 영향 범위를 명시한다.
- Review 범위를 넘어 임의 수정하지 않는다.
- 수정 내역을 요약해야 한다.
- 수정 후 Re-review 요청을 포함한다.
- Fix 결과는 Review Agent가 재검토 가능한 구조여야 한다.

---

### [실무]

Fix Agent Flow:

```text
Review Findings
→ Prioritize Issues
→ Define Fix Scope
→ Apply Fix
→ Preserve Existing Requirements
→ Produce Updated Output
→ Write Change Summary
→ Request Re-review
```

Fix Agent Input:

| Input                | 설명                       |
| -------------------- | -------------------------- |
| Review Findings      | Review Agent가 발견한 문제 |
| Original Output      | 수정 전 산출물             |
| Original Requirement | 원본 요구사항              |
| Constraints          | 지켜야 할 제약 조건        |
| Fix Scope            | 수정 범위                  |
| Done Criteria        | 완료 기준                  |
| Preserve Rules       | 유지해야 할 기존 동작      |

Fix Agent Output:

| Output             | 설명          |
| ------------------ | ------------- |
| Applied Fix        | 적용한 수정   |
| Updated Output     | 수정된 산출물 |
| Change Summary     | 변경 요약     |
| Preserved Behavior | 유지한 동작   |
| Remaining Issues   | 남은 이슈     |
| Re-review Request  | 재검토 요청   |

---

### [FAQ]

Q. Fix Agent는 뭐야?
A. Review Agent가 발견한 문제를 기준으로 산출물을 수정하는 Agent이다.

Q. Fix Agent가 임의로 기능을 추가해도 돼?
A. 안 된다. Review Finding과 Fix Scope 범위 안에서 수정해야 한다.

Q. Fix Agent가 가장 먼저 수정해야 할 것은?
A. Critical과 Major Severity의 문제를 우선 수정해야 한다.

Q. Fix 후에는 무엇을 해야 해?
A. Change Summary를 작성하고 Review Agent에게 Re-review를 요청해야 한다.

---

# 6. Fix Scope

## 6.1 Fix Scope Definition

### [개념]

Fix Scope는 Fix Agent가 수정할 수 있는 범위를 정의한다.

Fix Scope가 없으면 Fix Agent가 Review 범위를 넘어 구조를 과도하게 바꾸거나 새로운 문제를 만들 수 있다.

Fix Scope는 다음을 포함한다.

- Target Findings
- Allowed Changes
- Not Allowed Changes
- Preserve Behavior
- Impact Area
- Re-review Target

---

### [핵심]

- Fix Scope는 Review Finding과 연결되어야 한다.
- 허용된 수정과 금지된 수정을 구분한다.
- 기존 동작 보존 기준을 명확히 한다.
- 영향 범위를 표시한다.
- API / DTO / DB 변경은 별도 영향 분석이 필요하다.
- Fix Scope 밖 작업은 Deferred Task로 분리한다.
- 위험 변경은 사용자 확인이 필요하다.

---

### [실무]

Fix Scope Template:

```md
## Fix Scope

### Target Findings

### Allowed Changes

### Not Allowed Changes

### Preserve Behavior

### Impact Area

### Deferred Tasks

### User Confirmation Required

### Re-review Target
```

예시:

```md
## Fix Scope

### Target Findings

- Password Encoding 누락
- 중복 이메일 예외 흐름 누락

### Allowed Changes

- Service Flow에 passwordEncoder.encode() 단계 추가
- existsByEmail() 기반 중복 이메일 검증 추가
- Exception Cases에 DuplicateEmailException 추가

### Not Allowed Changes

- users table 구조 임의 변경
- Frontend 회원가입 화면 추가
- 이메일 인증 기능 추가
- JWT 발급 정책 변경

### Preserve Behavior

- ApiResponse<T> 직접 반환 유지
- GlobalExceptionHandler 사용 유지

### Impact Area

- UserService
- AuthController
- Exception Flow

### Deferred Tasks

- 이메일 인증 정책 결정

### User Confirmation Required

No

### Re-review Target

- Security
- Exception Flow
- API Response Consistency
```

주의:

- Fix Scope 없이 전체 구조를 다시 설계하지 않는다.
- Review Finding과 무관한 수정 금지.
- 기능 변경과 결함 수정을 구분한다.
- 위험 작업은 승인 없이 수정하지 않는다.
- 수정 범위가 커지면 PM Agent에게 반환한다.

---

### [FAQ]

Q. Fix Scope는 뭐야?
A. Fix Agent가 수정할 수 있는 범위를 정의하는 기준이다.

Q. Fix Scope가 왜 필요해?
A. Fix Agent가 Review 범위를 넘어 과도하게 수정하거나 새로운 문제를 만드는 것을 막기 위해 필요하다.

Q. Fix Scope에는 무엇이 들어가?
A. Target Findings, Allowed Changes, Not Allowed Changes, Preserve Behavior, Impact Area, Re-review Target이 들어간다.

Q. Fix Scope 밖 문제가 보이면 어떻게 해?
A. 직접 수정하지 않고 Deferred Task 또는 PM Agent Handoff로 분리한다.

---

# 7. Fix Output

## 7.1 Fix Output Definition

### [개념]

Fix Output은 Fix Agent가 Review Finding을 반영한 뒤 반환하는 구조화된 수정 결과이다.

Fix Output은 단순히 수정된 산출물만 포함하지 않는다.
어떤 Finding을 어떻게 수정했는지, 기존 동작은 유지했는지, 남은 이슈는 무엇인지 명확히 표시해야 한다.

---

### [핵심]

- Fix Output은 Review Finding과 연결되어야 한다.
- Applied Fix를 명확히 작성한다.
- Updated Output을 포함한다.
- Change Summary를 작성한다.
- Preserved Behavior를 표시한다.
- Remaining Issues를 숨기지 않는다.
- Re-review Request를 포함한다.
- Evidence 없이 완료 선언하지 않는다.

---

### [실무]

Fix Output Template:

```md
## Fix Output

### Target Findings

### Applied Fix

### Updated Output

### Change Summary

### Preserved Behavior

### Remaining Issues

### Done Criteria Check

### Re-review Request
```

예시:

```md
## Fix Output

### Target Findings

- Password Encoding 누락
- 중복 이메일 예외 흐름 누락

### Applied Fix

- Service Flow에 passwordEncoder.encode() 단계 추가
- userRepository.existsByEmail(email) 검증 추가
- DuplicateEmailException 처리 추가

### Updated Output

1. SignUpReqDto validation
2. email 중복 확인
3. passwordEncoder.encode(rawPassword)
4. Users Entity 생성
5. userRepository.save()
6. UserResDto 반환

### Change Summary

- 보안상 필요한 Password Encoding 단계 보강
- 중복 이메일 예외 흐름 보강
- 기존 ApiResponse<T> 반환 방식 유지

### Preserved Behavior

- Controller 응답 형식 유지
- GlobalExceptionHandler 사용 유지
- 이메일 인증 기능은 범위 제외 유지

### Remaining Issues

- 이메일 인증 필수 여부 미확정

### Done Criteria Check

- Password Encoding 포함: Yes
- 중복 이메일 처리 포함: Yes
- Review 가능한 구조: Yes

### Re-review Request

Security, Exception Flow, API Response Consistency 재검토 필요
```

주의:

- 변경 요약 없이 수정본만 제공하지 않는다.
- 기존 동작 보존 여부를 누락하지 않는다.
- Review Finding과 무관한 변경을 섞지 않는다.
- Remaining Issue를 완료로 포장하지 않는다.
- Re-review 대상이 불명확하면 Review Loop가 흔들린다.

---

### [FAQ]

Q. Fix Output은 뭐야?
A. Fix Agent가 Review Finding을 반영한 뒤 반환하는 구조화된 수정 결과이다.

Q. Fix Output에는 무엇이 들어가?
A. Target Findings, Applied Fix, Updated Output, Change Summary, Preserved Behavior, Remaining Issues, Re-review Request가 들어간다.

Q. Change Summary가 왜 필요해?
A. PM Agent와 Review Agent가 무엇이 수정되었는지 빠르게 확인하기 위해 필요하다.

Q. Remaining Issues를 숨겨도 돼?
A. 안 된다. 남은 이슈는 Review와 Final Integration 단계에서 반드시 확인되어야 한다.

---

# 8. Re-review

## 8.1 Re-review Definition

### [개념]

Re-review는 Fix Agent가 수정한 산출물을 Review Agent가 다시 검증하는 과정이다.

Re-review는 새 Review가 아니라 기존 Review Finding이 해결되었는지 확인하는 재검토이다.
단, Fix 과정에서 새 문제가 생겼다면 신규 Finding으로 기록할 수 있다.

---

### [핵심]

- Re-review는 기존 Finding 해결 여부를 확인한다.
- Review Criteria는 기존 기준을 유지한다.
- Fix Scope 밖 새 문제는 신규 Finding으로 분리한다.
- Critical 또는 Major가 남아 있으면 Fail이다.
- Minor만 남으면 조건부 Pass 가능하다.
- Re-review 결과는 PM Agent에게 전달된다.
- Max Iteration을 초과하면 blocked 또는 failed로 종료한다.

---

### [실무]

Re-review Template:

```md
## Re-review Result

### Reviewed Fix Output

### Previous Findings Check

| Finding | Status | Evidence | Note |
| ------- | ------ | -------- | ---- |

### New Findings

### Severity Summary

### Pass / Fail

### Remaining Issues

### Next Step
```

예시:

```md
## Re-review Result

### Reviewed Fix Output

회원가입 Service Flow 수정본

### Previous Findings Check

| Finding                | Status   | Evidence                                       | Note |
| ---------------------- | -------- | ---------------------------------------------- | ---- |
| Password Encoding 누락 | Resolved | passwordEncoder.encode() 단계 추가             |      |
| 중복 이메일 예외 누락  | Resolved | existsByEmail() + DuplicateEmailException 추가 |      |

### New Findings

None

### Severity Summary

- Critical: 0
- Major: 0
- Minor: 0
- Info: 1

### Pass / Fail

Pass

### Remaining Issues

- 이메일 인증 필수 여부는 정책 미확정

### Next Step

PM Agent Final Integration 가능
```

주의:

- Re-review에서 기준을 임의로 바꾸지 않는다.
- 수정된 부분만 보되 새 Critical 문제는 기록한다.
- 해결된 Finding을 계속 반복 지적하지 않는다.
- Max Iteration 없이 반복하지 않는다.
- Minor Issue를 이유로 무한 Fix하지 않는다.

---

### [FAQ]

Q. Re-review는 뭐야?
A. Fix Agent가 수정한 결과를 Review Agent가 다시 검증하는 과정이다.

Q. Re-review는 새 Review와 달라?
A. 기본적으로 기존 Finding 해결 여부를 확인하는 재검토이며, 새 문제가 생기면 신규 Finding으로 기록할 수 있다.

Q. Re-review에서 기준을 바꿔도 돼?
A. 원칙적으로 안 된다. 기존 Review Criteria를 유지해야 Loop가 안정적이다.

Q. Re-review가 계속 Fail이면 어떻게 해?
A. Max Iteration 도달 시 blocked 또는 failed로 종료하고 PM Agent가 사용자 확인 또는 범위 재조정을 수행한다.

---

# 9. Review / Fix Loop

## 9.1 Review / Fix Loop Definition

### [개념]

Review / Fix Loop는 Domain Agent 산출물을 검토하고, 문제가 있으면 수정한 뒤 재검토하는 품질 개선 반복 구조이다.

Review / Fix Loop는 Agent Workflow의 안정성과 품질을 높이지만, 종료 조건 없이 반복하면 무한 Loop가 발생할 수 있다.

---

### [핵심]

- Domain Agent Output을 Review Agent가 검증한다.
- Finding이 있으면 Fix Agent가 수정한다.
- Fix 후 Re-review를 수행한다.
- Critical 또는 Major Issue가 없으면 Pass 가능하다.
- Max Iteration을 설정해야 한다.
- Stop Condition을 명확히 정의해야 한다.
- Review 기준은 Loop 중간에 바꾸지 않는다.
- Minor Issue는 사용자에게 전달하고 종료 가능하다.

---

### [실무]

Review / Fix Loop Flow:

```text
Domain Agent Output
→ Review Agent
→ Findings
→ Severity Check
→ Fix Agent
→ Fix Output
→ Re-review
→ Pass or Repeat
→ Final Integration
```

Loop Control Template:

```md
## Review / Fix Loop Control

### Review Criteria

### Max Iteration

### Current Iteration

### Pass Condition

### Fix Required Condition

### Stop Condition

### Escalation Condition
```

예시:

```md
## Review / Fix Loop Control

### Review Criteria

- Requirement 충족
- Domain Rules 준수
- Security 위험 없음
- Done Criteria 충족

### Max Iteration

2

### Current Iteration

1

### Pass Condition

- Critical 0
- Major 0
- Done Criteria 핵심 항목 충족

### Fix Required Condition

- Critical 또는 Major 1개 이상
- 핵심 Done Criteria 미충족

### Stop Condition

- Pass 조건 충족
- Max Iteration 도달
- 사용자 확인 필요
- Tool Failure 발생

### Escalation Condition

- 같은 Critical Issue 반복
- 요구사항 충돌
- Scope 재정의 필요
```

권장 Max Iteration:

| 작업 유형           | 권장 반복               |
| ------------------- | ----------------------- |
| 단순 문서           | 1                       |
| 코드 설계           | 1~2                     |
| 보안 포함 작업      | 2~3                     |
| 배포 / DB 변경 포함 | 2 + Human Confirmation  |
| 고위험 작업         | Human Confirmation 우선 |

---

### [FAQ]

Q. Review / Fix Loop는 뭐야?
A. 산출물을 검토하고 문제가 있으면 수정한 뒤 다시 검토하는 품질 개선 반복 구조이다.

Q. Review / Fix Loop가 필요한 이유는?
A. Domain Agent가 놓친 요구사항, 결함, 보안 위험, 규칙 위반을 수정해 품질을 높이기 위해 필요하다.

Q. Review / Fix Loop는 몇 번 반복해야 해?
A. 단순 작업은 1회, 개발 작업은 1~2회, 보안 포함 작업은 2~3회가 적절하다.

Q. 무한 반복은 어떻게 막아?
A. Max Iteration, Pass Condition, Stop Condition, Escalation Condition을 정의해야 한다.

---

# 10. Stop Condition

## 10.1 Stop Condition Definition

### [개념]

Stop Condition은 Agent Workflow 또는 Review / Fix Loop가 언제 종료되는지 정의하는 기준이다.

Stop Condition은 완료, 실패, 보류, 사용자 확인 필요 상태를 구분한다.

---

### [핵심]

- Stop Condition은 Workflow 시작 전에 정의한다.
- Review Passed이면 완료 가능하다.
- Max Iteration에 도달하면 반복을 중단한다.
- Missing Information이 치명적이면 사용자 확인으로 중단한다.
- Tool Failure가 복구 불가능하면 중단한다.
- Unsafe Action이 감지되면 즉시 중단한다.
- 실패 상태를 성공으로 표시하지 않는다.
- 불완전한 결과를 완료로 처리하지 않는다.

---

### [실무]

Stop Condition Template:

```md
## Stop Condition

### Completed

### Review Passed

### Blocked

### Failed

### User Confirmation Required

### Tool Failure

### Unsafe Action Detected

### Max Iteration Reached
```

상태 정의:

| Status                     | 의미                                    |
| -------------------------- | --------------------------------------- |
| completed                  | 요구사항 충족, Review Pass              |
| review_passed              | 검토 통과, Final Integration 가능       |
| fix_required               | Critical 또는 Major Issue 존재          |
| blocked                    | 정보 부족, Scope 충돌, 사용자 확인 필요 |
| failed                     | 반복 실패, 복구 불가 오류               |
| user_confirmation_required | 위험 작업 또는 필수 결정 필요           |
| unsafe_action_detected     | 안전 문제로 중단                        |
| tool_failure               | Tool 실패로 진행 불가                   |

예시:

```md
## Stop Condition

### Completed

- Required Output 생성
- Critical / Major Issue 없음
- Done Criteria 핵심 항목 충족

### Blocked

- 이메일 인증 정책이 필수 요구사항인데 미확정
- 기존 Entity 정보가 없어 설계 불가

### Failed

- 같은 Critical Issue가 Max Iteration 동안 반복
- Tool Result가 계속 실패

### User Confirmation Required

- DB Schema 변경 필요
- 실제 배포 또는 파일 삭제 필요
```

---

### [FAQ]

Q. Stop Condition은 뭐야?
A. Agent Workflow나 Review / Fix Loop가 언제 완료, 실패, 보류, 사용자 확인 필요 상태로 끝나는지 정하는 기준이다.

Q. Stop Condition이 왜 필요해?
A. Agent가 무한 반복하거나 불완전한 결과를 완료로 처리하는 것을 막기 위해 필요하다.

Q. Max Iteration에 도달하면 어떻게 해?
A. 반복을 중단하고 blocked 또는 failed로 표시한 뒤 PM Agent가 사용자 확인이나 범위 재조정을 수행한다.

Q. Unsafe Action이 감지되면 어떻게 해?
A. 즉시 중단하거나 Human Confirmation을 요구해야 한다.

---

# 11. Failure Handling

## 11.1 Failure Handling Definition

### [개념]

Failure Handling은 Agent Workflow에서 발생하는 실패를 분류하고 복구 방법을 선택하는 과정이다.

Agent Workflow는 실패를 숨기지 않고 정상적인 상태로 다뤄야 한다.

주요 실패 유형:

- Missing Context
- Invalid Routing
- Handoff Failure
- Retrieval Failure
- Tool Failure
- Invalid Output
- Review Failure
- Fix Failure
- Timeout
- Unsafe Action
- Human Escalation Required

---

### [핵심]

- 실패 유형을 분류한다.
- 재시도 가능한 실패와 중단해야 하는 실패를 구분한다.
- Retry, Fallback, Ask User, Stop 중 하나를 선택한다.
- 실패 원인과 영향을 기록한다.
- 실패한 결과를 성공처럼 사용하지 않는다.
- Tool 실패를 숨기지 않는다.
- Retrieval 실패를 일반 지식으로 덮지 않는다.
- 안전 문제는 즉시 중단한다.

---

### [실무]

Failure Handling Flow:

```text
Failure Detected
→ Classify Failure
→ Identify Cause
→ Assess Impact
→ Select Recovery Option
→ Update Shared State
→ Continue or Stop
```

Failure Handling Template:

```md
## Failure Handling

### Failure Type

### Detected At

### Cause

### Impact

### Recovery Option

Retry / Fallback / Ask User / Stop

### State Update

### Next Step
```

Failure 처리 기준:

| Failure Type      | 처리                            |
| ----------------- | ------------------------------- |
| Missing Context   | Assumption 또는 사용자 확인     |
| Invalid Routing   | PM Agent 재분석 후 재라우팅     |
| Handoff Failure   | Handoff 재작성                  |
| Retrieval Failure | 검색 실패 표시, 제한적 답변     |
| Tool Failure      | 원인 기록, 재시도 또는 중단     |
| Invalid Output    | Output Format 재요청            |
| Review Failure    | Fix Agent로 전달                |
| Fix Failure       | Scope 재정의 또는 PM Escalation |
| Unsafe Action     | Stop 또는 Human Confirmation    |

예시:

```md
## Failure Handling

### Failure Type

Handoff Failure

### Detected At

Backend Agent Execution

### Cause

Expected Output과 Done Criteria가 누락됨.

### Impact

Backend Agent가 Review 가능한 산출물을 만들기 어려움.

### Recovery Option

Retry

### State Update

status: handoff_rewrite_required

### Next Step

PM Agent가 Handoff를 재작성하고 Backend Agent에게 재전달
```

---

### [FAQ]

Q. Failure Handling은 뭐야?
A. Agent Workflow에서 발생하는 실패를 분류하고 Retry, Fallback, Ask User, Stop 중 하나로 처리하는 과정이다.

Q. Retrieval Failure는 어떻게 처리해?
A. 검색 실패를 표시하고, Assumption을 명시하거나 사용자에게 관련 문서를 요청한다.

Q. Tool Failure는 어떻게 처리해?
A. 실패 원인과 영향을 기록하고, 재시도 가능 여부를 판단한 뒤 중단 또는 대체 경로를 선택한다.

Q. 실패한 결과를 다음 Agent에게 넘겨도 돼?
A. 안 된다. 잘못된 결과를 기반으로 다음 Agent를 실행하면 오류가 연쇄적으로 확산된다.

---

# 12. Human-in-the-loop

## 12.1 Human-in-the-loop Definition

### [개념]

Human-in-the-loop는 Agent Workflow에서 사용자 확인, 승인, 선택이 필요한 지점이다.

Agent가 모든 결정을 자동으로 처리하면 위험할 수 있다.
특히 외부 변경, 비용 발생, 삭제, 배포, DB 변경, 보안 위험이 있는 작업은 Human-in-the-loop가 필요하다.

---

### [핵심]

- 요구사항이 치명적으로 불명확하면 사용자 확인이 필요하다.
- 파일 삭제, DB 변경, 배포는 사용자 승인 대상이다.
- 비용 발생 API 대량 호출은 승인 대상이다.
- 보안 위험이 있으면 중단 또는 확인이 필요하다.
- 확인 요청은 구체적이어야 한다.
- 승인 범위를 넘어 실행하면 안 된다.
- 너무 자주 질문하면 자동화 가치가 낮아진다.
- 경미한 불확실성은 Assumption으로 처리 가능하다.

---

### [실무]

Human Confirmation Trigger:

| 상황                     | 처리                  |
| ------------------------ | --------------------- |
| 파일 삭제                | 사용자 승인 필요      |
| DB 변경 / 초기화         | 사용자 승인 필요      |
| 서버 배포                | 사용자 승인 필요      |
| 비용 발생 API 호출       | 사용자 승인 필요      |
| Secret / Credential 처리 | 사용자 확인 또는 중단 |
| 요구사항 충돌            | 사용자 선택 필요      |
| 치명적 정보 부족         | 사용자 확인 필요      |
| 보안 위험 작업           | 중단 또는 사용자 승인 |

Human-in-the-loop Template:

```md
## Human-in-the-loop

### Trigger

### Risk

### Required Decision

### Options

### Recommended Option

### Approval Scope

### Stop Until Confirmed

Yes / No
```

예시:

```md
## Human-in-the-loop

### Trigger

DB Schema 변경 필요

### Risk

기존 데이터와 Backend Entity에 영향 가능

### Required Decision

users.email unique constraint 추가 여부

### Options

1. Unique Constraint 추가
2. Application Level 중복 검사만 유지
3. 현재 작업에서는 보류

### Recommended Option

1. Unique Constraint 추가

### Approval Scope

DB Schema 변경 설계 승인까지만 해당

### Stop Until Confirmed

Yes
```

주의:

- 승인 없이 위험 작업 실행 금지
- 승인 범위를 확대 해석하지 않는다.
- 선택지는 구체적으로 제시한다.
- 질문 남발을 피한다.
- 불확실성을 숨기지 않는다.

---

### [FAQ]

Q. Human-in-the-loop는 뭐야?
A. Agent Workflow에서 사용자 확인, 승인, 선택이 필요한 지점이다.

Q. 언제 Human-in-the-loop가 필요해?
A. 파일 삭제, DB 변경, 배포, 비용 발생, 위험 작업, 치명적 요구사항 불명확 상황에서 필요하다.

Q. 모든 불확실성마다 사용자에게 물어야 해?
A. 아니다. 경미한 불확실성은 Assumption으로 표시하고 진행할 수 있다.

Q. 사용자 승인 범위를 넘어 실행해도 돼?
A. 안 된다. 승인받은 범위 안에서만 실행해야 한다.

---

# 13. Workflow Evaluation

## 13.1 Workflow Evaluation Definition

### [개념]

Workflow Evaluation은 Agent Workflow의 품질을 평가하는 과정이다.

Agent Workflow는 최종 답변만 평가하지 않는다.
Task Decomposition, Routing, Handoff, Intermediate Output, Review Finding, Fix Output, Stop Condition까지 함께 평가해야 한다.

---

### [핵심]

- 최종 결과 품질을 평가한다.
- 중간 산출물 품질을 평가한다.
- Agent Routing이 적절했는지 확인한다.
- Handoff가 충분했는지 확인한다.
- Review / Fix Loop가 품질 개선에 기여했는지 평가한다.
- Failure Handling이 적절했는지 확인한다.
- Latency와 Cost도 평가한다.
- Agent 수가 많다고 품질이 항상 좋아지는 것은 아니다.

---

### [실무]

Workflow Evaluation Metrics:

| Metric            | 설명                            |
| ----------------- | ------------------------------- |
| Task Success      | 사용자 요청 충족 여부           |
| Output Quality    | 최종 산출물 품질                |
| Retrieval Quality | 관련 RAG 검색 품질              |
| Routing Accuracy  | 적절한 Agent 배정 여부          |
| Handoff Quality   | 다음 Agent가 바로 작업 가능한지 |
| Review Pass Rate  | Review 통과율                   |
| Fix Effectiveness | Fix가 실제 문제를 해결했는지    |
| Tool Success Rate | Tool 호출 성공률                |
| Failure Rate      | 실패 빈도                       |
| Latency           | 실행 시간                       |
| Cost              | 모델 / Tool 비용                |
| User Satisfaction | 사용자 만족도                   |

Evaluation Template:

```md
## Workflow Evaluation

### Task Success

### Output Quality

### Routing Accuracy

### Handoff Quality

### Review Quality

### Fix Effectiveness

### Failure Handling

### Latency / Cost

### Improvement Actions
```

예시:

```md
## Workflow Evaluation

### Task Success

회원가입 API 설계 요구사항 충족

### Output Quality

DTO, Service Flow, Exception Cases 포함

### Routing Accuracy

Backend Agent와 Security Agent 배정 적절

### Handoff Quality

Constraints와 Done Criteria 포함

### Review Quality

Password Encoding 누락을 Critical로 탐지

### Fix Effectiveness

Fix 후 Encoding 단계 추가 완료

### Failure Handling

이메일 인증 정책 미확정 사항을 Open Issue로 처리

### Latency / Cost

Sequential Workflow로 비용과 복잡도 낮음

### Improvement Actions

이메일 인증 정책 결정 후 Security Agent 재검토 필요
```

---

### [FAQ]

Q. Workflow Evaluation은 뭐야?
A. Agent Workflow의 최종 결과, 중간 산출물, Routing, Handoff, Review, Fix, Failure Handling 품질을 평가하는 과정이다.

Q. 최종 답변만 평가하면 안 돼?
A. 안 된다. Agent Workflow는 중간 단계 품질이 최종 품질을 결정하므로 전체 흐름을 평가해야 한다.

Q. 평가 지표에는 무엇이 있어?
A. Task Success, Output Quality, Routing Accuracy, Handoff Quality, Review Pass Rate, Fix Effectiveness, Tool Success Rate, Latency, Cost가 있다.

Q. Agent 수가 많으면 평가 점수가 좋아져?
A. 항상 그렇지 않다. Agent 수가 많으면 복잡도와 Latency가 증가할 수 있다.

---

# 14. Review Agent Evaluation

## 14.1 Review Quality Evaluation

### [개념]

Review Agent Evaluation은 Review Agent가 실제로 유효한 검증을 수행했는지 평가하는 과정이다.

Review Agent는 문제를 많이 찾는 것이 목표가 아니다.
중요한 문제를 정확히 찾고, Fix 가능한 형태로 Finding을 작성하는 것이 목표이다.

---

### [핵심]

- Review Finding이 요구사항과 연결되어야 한다.
- Severity가 적절해야 한다.
- Evidence가 있어야 한다.
- Fix Direction이 실행 가능해야 한다.
- 취향과 결함을 구분해야 한다.
- Critical / Major를 놓치지 않아야 한다.
- Minor Issue를 과도하게 부풀리지 않아야 한다.
- Review 결과가 Fix Agent에게 유용해야 한다.

---

### [실무]

Review Agent Evaluation Checklist:

```md
## Review Agent Evaluation Checklist

- [ ] Review Criteria가 명확한가?
- [ ] Finding이 Evidence를 포함하는가?
- [ ] Severity가 적절한가?
- [ ] Critical / Major Issue를 놓치지 않았는가?
- [ ] 취향과 결함을 구분했는가?
- [ ] Fix Direction이 실행 가능한가?
- [ ] Finding이 Fix Agent에게 바로 전달 가능한가?
- [ ] Review 범위를 과도하게 벗어나지 않았는가?
- [ ] Pass / Fail 판단이 기준과 일치하는가?
```

Bad Review 예시:

```md
문제:
코드가 별로 좋아 보이지 않음.

원인:
깔끔하지 않음.

해결:
더 좋게 수정.
```

Good Review 예시:

```md
### Issue

Controller 응답 형식이 프로젝트 규칙과 다름.

### Severity

Major

### Evidence

프로젝트 규칙은 ApiResponse<T> 직접 반환인데, 현재 산출물은 ResponseEntity<String> 반환을 제안함.

### Impact

API 응답 일관성이 깨지고 Frontend 연동 오류 가능성이 있음.

### Fix Direction

Controller 반환 형식을 ApiResponse<UserResDto>로 변경하고 예외는 GlobalExceptionHandler에서 처리하도록 수정.
```

---

### [FAQ]

Q. Review Agent Evaluation은 뭐야?
A. Review Agent가 유효한 기준으로 정확한 Finding을 만들었는지 평가하는 과정이다.

Q. 좋은 Review Finding은 어떤 형태야?
A. Issue, Severity, Evidence, Cause, Impact, Fix Direction이 명확해야 한다.

Q. Review Agent가 문제를 많이 찾으면 좋은 거야?
A. 아니다. 중요한 문제를 정확히 찾고 Fix 가능한 형태로 전달하는 것이 중요하다.

Q. 취향 기반 Review는 왜 문제야?
A. 실제 결함이 아닌 선호를 문제로 만들면 Fix Loop가 불필요하게 길어진다.

---

# 15. Fix Agent Evaluation

## 15.1 Fix Quality Evaluation

### [개념]

Fix Agent Evaluation은 Fix Agent가 Review Finding을 정확히 반영했는지 평가하는 과정이다.

Fix Agent의 목표는 많이 바꾸는 것이 아니라, 필요한 문제를 정확히 수정하고 기존 요구사항을 보존하는 것이다.

---

### [핵심]

- Fix가 Review Finding과 연결되어야 한다.
- Critical / Major Issue가 해결되어야 한다.
- 기존 요구사항을 보존해야 한다.
- Fix Scope 밖 변경을 하지 않아야 한다.
- Change Summary가 명확해야 한다.
- Remaining Issues를 숨기지 않아야 한다.
- Re-review가 가능해야 한다.
- 새 문제를 만들지 않아야 한다.

---

### [실무]

Fix Agent Evaluation Checklist:

```md
## Fix Agent Evaluation Checklist

- [ ] Target Finding을 정확히 반영했는가?
- [ ] Critical Issue가 해결되었는가?
- [ ] Major Issue가 해결되었는가?
- [ ] Fix Scope를 벗어나지 않았는가?
- [ ] 기존 요구사항과 동작을 보존했는가?
- [ ] 변경 사항을 요약했는가?
- [ ] Remaining Issue를 표시했는가?
- [ ] Re-review Target을 명시했는가?
- [ ] 새 문제가 생기지 않았는가?
```

Bad Fix 예시:

```md
수정 완료.
```

문제:

- 어떤 Finding을 수정했는지 알 수 없음
- 변경 내용 없음
- 기존 동작 보존 여부 없음
- Re-review 불가

Good Fix 예시:

```md
### Target Findings

- Password Encoding 누락

### Applied Fix

- Service Flow에 passwordEncoder.encode(rawPassword) 단계 추가

### Preserved Behavior

- ApiResponse<T> 직접 반환 유지
- 이메일 인증은 범위 제외 유지

### Remaining Issues

- 이메일 인증 필수 여부 미확정

### Re-review Request

Security Agent 재검토 필요
```

---

### [FAQ]

Q. Fix Agent Evaluation은 뭐야?
A. Fix Agent가 Review Finding을 정확히 반영하고 기존 요구사항을 보존했는지 평가하는 과정이다.

Q. 좋은 Fix는 어떤 Fix야?
A. Target Finding을 해결하고, Fix Scope를 지키며, 변경 요약과 Re-review 요청을 포함하는 Fix이다.

Q. Fix Agent가 많이 고치면 좋은 거야?
A. 아니다. 필요한 범위만 정확히 수정하고 새 문제를 만들지 않는 것이 중요하다.

Q. Fix Scope 밖 문제가 보이면 어떻게 해?
A. 직접 수정하지 않고 Deferred Task 또는 PM Agent Handoff로 분리해야 한다.

---

# 16. Troubleshooting

## 16.1 Workflow Troubleshooting

### [개념]

Troubleshooting은 Agent Workflow에서 발생하는 문제를 원인과 해결책으로 정리하는 과정이다.

Troubleshooting은 실패 사례를 숨기지 않고, 다음 Workflow 개선에 반영하기 위해 필요하다.

---

### [핵심]

- 문제를 명확히 정의한다.
- 원인을 Role, Handoff, State, Tool, Review 기준으로 분류한다.
- 해결책은 실행 가능해야 한다.
- 같은 문제가 반복되면 Workflow Rule을 수정한다.
- 실패 사례는 Evaluation에 반영한다.
- Troubleshooting 결과는 Domain Rules와 Project Rules 개선에 사용한다.

---

### [실무]

Troubleshooting Template:

```md
## Troubleshooting

### 문제

### 원인

### 영향

### 해결

### 예방
```

---

## 16.2 Agent가 엉뚱한 일을 함

### [개념]

Agent가 요청과 다른 작업을 수행하는 문제이다.

### [핵심]

원인:

- Role / Task가 불명확함
- Handoff에 Context 누락
- Output Format 미지정
- Agent 권한이 너무 넓음
- Scope Control 없음

해결:

- Role과 책임 범위 명확화
- Handoff Template 개선
- Expected Output 지정
- Agent별 Scope 제한
- Not Responsible 명시

### [실무]

```md
## Troubleshooting

### 문제

Backend Agent가 Frontend 화면과 Docker 배포까지 설계함.

### 원인

Backend Agent Role과 Not Responsible이 불명확함.

### 영향

Scope가 확장되고 Review 기준이 불명확해짐.

### 해결

Backend Agent는 DTO, Service, Controller, Exception Flow만 수행하도록 제한.
Frontend와 DevOps 이슈는 Handoff Request로 분리.

### 예방

Domain Agent Role Template에 Not Responsible 추가.
```

---

## 16.3 Workflow가 끝나지 않음

### [개념]

Agent가 Review / Fix를 계속 반복하며 완료되지 않는 문제이다.

### [핵심]

원인:

- Stop Condition 없음
- Max Iteration 없음
- Review 기준이 계속 바뀜
- Minor Issue까지 무한 수정
- Pass Condition 불명확

해결:

- Stop Condition 정의
- Max Iteration 설정
- Critical / Major / Minor 구분
- Minor Issue는 조건부 Pass 처리
- Review Criteria 고정

### [실무]

```md
## Troubleshooting

### 문제

Review Agent와 Fix Agent가 계속 반복됨.

### 원인

Max Iteration과 Pass Condition이 없음.

### 영향

Latency 증가, 비용 증가, 최종 결과 지연.

### 해결

Max Iteration 2회 설정.
Critical / Major가 없으면 Pass.
Minor는 Remaining Issue로 전달 후 종료.

### 예방

Review / Fix Loop Control Template 사용.
```

---

## 16.4 Agent 간 결과가 이어지지 않음

### [개념]

다음 Agent가 이전 Agent 결과를 제대로 활용하지 못하는 문제이다.

### [핵심]

원인:

- Intermediate Output 구조 불명확
- Shared State 누락
- Handoff Format 불일치
- Decision과 Assumption 구분 없음
- Open Issue 누락

해결:

- 공통 Output Schema 정의
- Shared State에 결정 사항 기록
- Handoff Template 통일
- Assumption / Open Issue 표시
- Context Passing 개선

### [실무]

```md
## Troubleshooting

### 문제

Security Agent가 Backend Agent의 Password 정책을 이어받지 못함.

### 원인

Backend Agent Output에 Decisions와 Review Target이 없음.

### 영향

Security Review 누락 가능성 증가.

### 해결

Domain Agent Output에 Decisions, Assumptions, Review Target 추가.

### 예방

Intermediate Output Template 강제.
```

---

## 16.5 Review Agent가 쓸데없는 지적을 많이 함

### [개념]

Review 결과가 실제 품질 개선과 무관한 취향성 지적으로 채워지는 문제이다.

### [핵심]

원인:

- Review Criteria 불명확
- Severity 기준 없음
- 취향과 결함 구분 없음
- Review 범위가 과도함
- Pass Condition 없음

해결:

- Review Checklist 정의
- Severity 기준 추가
- 문제 / 영향 / 수정 방향 구조화
- 프로젝트 규칙 기반 Review 수행
- Info와 Minor를 구분

### [실무]

```md
## Troubleshooting

### 문제

Review Agent가 기능 결함이 아닌 문장 스타일만 반복 지적함.

### 원인

Review Criteria와 Severity 기준이 없음.

### 영향

Fix Loop가 길어지고 핵심 결함 수정이 지연됨.

### 해결

Critical, Major, Minor, Info 기준 정의.
사용자 요구사항과 Domain Rules 위반만 Finding으로 기록.

### 예방

Review Request에 Severity Rule과 Pass Condition 포함.
```

---

## 16.6 PM Agent가 일을 너무 많이 함

### [개념]

PM Agent가 조율이 아니라 구현까지 전부 수행하는 문제이다.

### [핵심]

원인:

- PM Agent Role이 모호함
- Domain Agent Handoff가 없음
- Workflow가 Single Agent처럼 동작함
- Final Integration과 구현이 혼합됨

해결:

- PM Agent를 분석 / 분해 / 라우팅 / 통합 중심으로 제한
- Domain Agent에게 명확히 Handoff
- PM Agent Output을 Task Plan 중심으로 변경
- 구현 결과는 Domain Agent Output으로 분리

### [실무]

```md
## Troubleshooting

### 문제

PM Agent가 Backend 코드, Security 검토, 테스트 케이스까지 직접 작성함.

### 원인

PM Agent 책임 범위가 제한되지 않음.

### 영향

Multi-Agent 구조가 무너지고 Review 품질이 낮아짐.

### 해결

PM Agent는 Task Decomposition과 Handoff까지만 수행.
Backend, Security, Testing Agent에게 작업 분리.

### 예방

PM Agent Anti-Pattern 규칙 적용.
```

---

### [FAQ]

Q. Agent가 엉뚱한 일을 하면 어떻게 해?
A. Role과 책임 범위를 명확히 하고, Handoff Template과 Expected Output을 개선해야 한다.

Q. Workflow가 끝나지 않으면 어떻게 해?
A. Stop Condition, Max Iteration, Severity 기준, Pass Condition을 추가해야 한다.

Q. Agent 간 결과가 이어지지 않으면 어떻게 해?
A. Shared State를 사용하고 Intermediate Output과 Handoff 형식을 통일해야 한다.

Q. Review Agent가 쓸데없는 지적을 많이 하면 어떻게 해?
A. Review Criteria, Severity Rule, Pass Condition을 명확히 해야 한다.

---

# 17. Best Practice

## 17.1 Review / Fix Best Practice

### [개념]

Best Practice는 Review Agent, Fix Agent, Evaluation, Troubleshooting을 안정적으로 운영하기 위한 권장 규칙이다.

---

### [핵심]

- Review 기준을 먼저 정의한다.
- Severity 기준을 명확히 한다.
- Finding은 Evidence와 Fix Direction을 포함한다.
- Critical / Major를 우선 수정한다.
- Fix Scope를 제한한다.
- Existing Behavior를 보존한다.
- Re-review 기준을 고정한다.
- Max Iteration을 설정한다.
- Minor Issue는 무한 수정하지 않는다.
- Failure를 숨기지 않는다.
- Human Confirmation이 필요한 작업은 중단한다.
- Evaluation 결과를 Workflow 개선에 반영한다.

---

### [실무]

Review / Fix 운영 규칙:

```md
## Review / Fix Best Practice

### Review

- Review Criteria 먼저 정의
- Severity Rule 포함
- Evidence 기반 Finding 작성
- 취향과 결함 구분
- Fix Direction 필수

### Fix

- Review Finding 기준 수정
- Fix Scope 밖 수정 금지
- Change Summary 작성
- Preserved Behavior 표시
- Remaining Issues 표시

### Loop

- Max Iteration 설정
- Pass Condition 정의
- Stop Condition 정의
- Re-review 기준 고정

### Evaluation

- Task Success 평가
- Handoff Quality 평가
- Review Quality 평가
- Fix Effectiveness 평가
- Failure 사례 기록
```

권장 Pass 기준:

```text
Review Pass:
- Critical Issue 0
- Major Issue 0
- 핵심 Done Criteria 충족
- Remaining Issue가 Blocking이 아님
```

권장 Fail 기준:

```text
Review Fail:
- Critical Issue 1개 이상
- Major Issue 1개 이상
- 핵심 Done Criteria 미충족
- 안전 문제 존재
- 사용자 확인이 필요한 위험 작업 존재
```

---

### [FAQ]

Q. Review / Fix Best Practice는 뭐야?
A. Review 기준 정의, Severity 분류, Evidence 기반 Finding, 제한된 Fix Scope, Re-review, Stop Condition을 포함하는 운영 규칙이다.

Q. Review Finding에는 무엇이 꼭 들어가야 해?
A. Issue, Severity, Evidence, Cause, Impact, Fix Direction이 들어가야 한다.

Q. Fix Agent는 무엇을 가장 주의해야 해?
A. Fix Scope를 벗어나지 않고 기존 요구사항과 동작을 보존해야 한다.

Q. Review Pass 기준은?
A. Critical과 Major Issue가 없고 핵심 Done Criteria가 충족되면 Pass 가능하다.

---

# Retrieval Queries

### [FAQ]

Q. Review Agent는 뭐야?
A. Domain Agent 산출물을 요구사항, Domain Rules, Project Rules, Done Criteria 기준으로 검증하는 Agent이다.

Q. Review Agent는 구현도 해?
A. 아니다. Review Agent는 구현보다 검증, 문제 식별, 영향 분석, 수정 방향 제시에 집중한다.

Q. Review Criteria는 뭐야?
A. Review Agent가 산출물을 검증할 때 사용하는 명확한 기준이다.

Q. Review Criteria에는 무엇이 들어가?
A. Requirement Check, Domain Rule Check, Project Rule Check, Security Check, API Contract Check, Done Criteria Check가 들어간다.

Q. Review Finding은 뭐야?
A. Review Agent가 발견한 문제를 Issue, Severity, Evidence, Cause, Impact, Fix Direction으로 구조화한 결과이다.

Q. 좋은 Review Finding은 어떤 형태야?
A. 문제 위치, 원인, 영향, 수정 방향, 담당 Agent가 명확해야 한다.

Q. Severity는 뭐야?
A. Review Finding의 위험도와 수정 우선순위를 나타내는 기준이다.

Q. Critical은 어떤 문제야?
A. 보안 위험, 데이터 손실, 실행 불가, Secret 노출, 위험 작업 자동 실행 같은 치명적 문제이다.

Q. Major는 어떤 문제야?
A. 핵심 요구사항 누락, API 계약 불일치, Validation 누락, 주요 흐름 오류 같은 문제이다.

Q. Minor가 있으면 Fail이야?
A. 반드시 Fail은 아니다. Critical과 Major가 없고 Minor만 있으면 조건부 Pass가 가능하다.

Q. Fix Agent는 뭐야?
A. Review Agent가 발견한 문제를 기준으로 산출물을 수정하는 Agent이다.

Q. Fix Agent가 임의로 기능을 추가해도 돼?
A. 안 된다. Review Finding과 Fix Scope 범위 안에서 수정해야 한다.

Q. Fix Scope는 뭐야?
A. Fix Agent가 수정할 수 있는 범위를 정의하는 기준이다.

Q. Fix Scope에는 무엇이 들어가?
A. Target Findings, Allowed Changes, Not Allowed Changes, Preserve Behavior, Impact Area, Re-review Target이 들어간다.

Q. Fix Output은 뭐야?
A. Fix Agent가 Review Finding을 반영한 뒤 반환하는 구조화된 수정 결과이다.

Q. Fix Output에는 무엇이 들어가?
A. Target Findings, Applied Fix, Updated Output, Change Summary, Preserved Behavior, Remaining Issues, Re-review Request가 들어간다.

Q. Re-review는 뭐야?
A. Fix Agent가 수정한 결과를 Review Agent가 다시 검증하는 과정이다.

Q. Re-review에서 기준을 바꿔도 돼?
A. 원칙적으로 안 된다. 기존 Review Criteria를 유지해야 Loop가 안정적이다.

Q. Review / Fix Loop는 뭐야?
A. 산출물을 검토하고 문제가 있으면 수정한 뒤 다시 검토하는 품질 개선 반복 구조이다.

Q. Review / Fix Loop는 몇 번 반복해야 해?
A. 단순 작업은 1회, 개발 작업은 1~2회, 보안 포함 작업은 2~3회가 적절하다.

Q. 무한 반복은 어떻게 막아?
A. Max Iteration, Pass Condition, Stop Condition, Escalation Condition을 정의해야 한다.

Q. Stop Condition은 뭐야?
A. Agent Workflow나 Review / Fix Loop가 언제 완료, 실패, 보류, 사용자 확인 필요 상태로 끝나는지 정하는 기준이다.

Q. Stop Condition이 왜 필요해?
A. Agent가 무한 반복하거나 불완전한 결과를 완료로 처리하는 것을 막기 위해 필요하다.

Q. Failure Handling은 뭐야?
A. Agent Workflow에서 발생하는 실패를 분류하고 Retry, Fallback, Ask User, Stop 중 하나로 처리하는 과정이다.

Q. Retrieval Failure는 어떻게 처리해?
A. 검색 실패를 표시하고, Assumption을 명시하거나 사용자에게 관련 문서를 요청한다.

Q. Tool Failure는 어떻게 처리해?
A. 실패 원인과 영향을 기록하고, 재시도 가능 여부를 판단한 뒤 중단 또는 대체 경로를 선택한다.

Q. Human-in-the-loop는 뭐야?
A. Agent Workflow에서 사용자 확인, 승인, 선택이 필요한 지점이다.

Q. 언제 Human-in-the-loop가 필요해?
A. 파일 삭제, DB 변경, 배포, 비용 발생, 위험 작업, 치명적 요구사항 불명확 상황에서 필요하다.

Q. Workflow Evaluation은 뭐야?
A. Agent Workflow의 최종 결과, 중간 산출물, Routing, Handoff, Review, Fix, Failure Handling 품질을 평가하는 과정이다.

Q. Workflow Evaluation 지표에는 무엇이 있어?
A. Task Success, Output Quality, Routing Accuracy, Handoff Quality, Review Pass Rate, Fix Effectiveness, Tool Success Rate, Latency, Cost가 있다.

Q. Review Agent Evaluation은 뭐야?
A. Review Agent가 유효한 기준으로 정확한 Finding을 만들었는지 평가하는 과정이다.

Q. Fix Agent Evaluation은 뭐야?
A. Fix Agent가 Review Finding을 정확히 반영하고 기존 요구사항을 보존했는지 평가하는 과정이다.

Q. Agent가 엉뚱한 일을 하면 어떻게 해?
A. Role과 책임 범위를 명확히 하고, Handoff Template과 Expected Output을 개선해야 한다.

Q. Workflow가 끝나지 않으면 어떻게 해?
A. Stop Condition, Max Iteration, Severity 기준, Pass Condition을 추가해야 한다.

Q. Agent 간 결과가 이어지지 않으면 어떻게 해?
A. Shared State를 사용하고 Intermediate Output과 Handoff 형식을 통일해야 한다.

Q. Review Agent가 쓸데없는 지적을 많이 하면 어떻게 해?
A. Review Criteria, Severity Rule, Pass Condition을 명확히 해야 한다.

Q. PM Agent가 일을 너무 많이 하면 어떻게 해?
A. PM Agent를 분석, 분해, 라우팅, 통합 중심으로 제한하고 Domain Agent에게 명확히 Handoff해야 한다.

Q. Review / Fix Best Practice는 뭐야?
A. Review 기준 정의, Severity 분류, Evidence 기반 Finding, 제한된 Fix Scope, Re-review, Stop Condition을 포함하는 운영 규칙이다.

Q. Review Pass 기준은?
A. Critical과 Major Issue가 없고 핵심 Done Criteria가 충족되면 Pass 가능하다.

Q. Review Fail 기준은?
A. Critical 또는 Major Issue가 있거나 핵심 Done Criteria가 미충족이면 Fail로 처리한다.

Q. Minor Issue는 어떻게 처리해?
A. Critical과 Major가 없으면 Remaining Issue로 표시하고 조건부 Pass 처리할 수 있다.

Q. Fix 후 남은 이슈는 숨겨도 돼?
A. 안 된다. Remaining Issues로 명확히 표시해야 한다.
