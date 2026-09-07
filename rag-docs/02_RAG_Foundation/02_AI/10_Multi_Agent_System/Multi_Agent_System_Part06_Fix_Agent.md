# Multi-Agent System Part06 - Fix Agent

---

# 1. Fix Agent Core

## 1.1 Fix Agent Definition

### [개념]

Fix Agent는 Review Agent가 발견한 Review Findings를 반영해 산출물을 수정하는 Agent이다.

Fix Agent는 새로운 요구사항을 만드는 Agent가 아니라, 기존 User Request, PM Agent Decision, Shared State, Review Findings 범위 안에서 산출물을 수정한다.

Fix Agent의 핵심은 기존 요구사항을 보존하면서 Review Finding을 정확히 반영하는 것이다.

기본 구조:

```text
Review Findings
→ Fix Agent
→ Fix Scope Selection
→ Apply Fix
→ Preserve Original Requirement
→ Updated Output
→ Re-review Request
```

Review-Fix Loop 구조:

```text
Draft Output
→ Review Agent
→ Review Findings
→ Fix Agent
→ Updated Output
→ Review Agent
→ Pass / Conditional Pass / Fail
```

---

### [핵심]

- Fix Agent는 Review Findings를 반영한다.
- Fix Agent는 기존 요구사항을 보존한다.
- Fix Agent는 PM Agent Decision을 따라야 한다.
- Fix Agent는 Shared State의 결정사항을 기준으로 수정한다.
- Fix Agent는 Review 범위 안에서 수정한다.
- Fix Agent는 새 요구사항을 임의로 추가하지 않는다.
- Fix Agent는 변경 내용과 변경 이유를 기록한다.
- Fix Agent는 Regression Risk를 표시한다.
- Fix Agent는 Re-review 필요 여부를 표시한다.
- Fix Agent는 Review-Fix Loop의 무한 반복을 만들면 안 된다.

---

### [실무]

2026 실무 기준에서 Fix Agent는 Review 결과를 산출물에 반영하는 Revision 담당 Agent로 사용한다.

Fix Agent 주요 책임:

```text
Review Findings 분석
→ Fix Scope 결정
→ Critical / Major 우선 수정
→ 기존 요구사항 보존
→ 변경 내용 요약
→ Regression Risk 표시
→ Updated Output 생성
→ Re-review 요청
```

Fix Agent가 수정할 수 있는 대상:

- PM Agent Plan
- Specialist Agent Output
- SQL Agent Schema Design
- Backend Agent API Contract
- Frontend Agent API Integration
- DevOps Agent Deploy Plan
- AI Agent Workflow Design
- Documentation Agent RAG Document
- Final Output Draft

Fix Agent가 임의로 하면 안 되는 일:

- 새로운 기능 요구사항 추가
- 기존 요구사항 삭제
- API Contract 무단 변경
- DB Schema 무단 변경
- 운영 서버 변경
- 파일 삭제
- 배포 실행
- Review 기준 변경
- Review Findings 범위 밖 대규모 리팩터링

---

### [FAQ]

Q. Fix Agent는 뭐 하는 Agent야?
A. Review Agent가 발견한 문제를 기존 요구사항과 Review Findings 범위 안에서 수정하는 Agent다.

Q. Fix Agent가 새 요구사항을 추가해도 돼?
A. 안 된다. 새 요구사항은 PM Agent에게 반환해야 한다.

Q. Fix Agent가 중요한 이유는?
A. Review Findings를 실제 산출물에 반영해 Multi-Agent 결과 품질을 높이기 때문이다.

Q. Fix Agent는 Review Agent와 뭐가 달라?
A. Review Agent는 문제를 찾고, Fix Agent는 Review Findings를 반영해 산출물을 수정한다.

---

# 2. Fix Input

## 2.1 Fix Input Definition

### [개념]

Fix Input은 Fix Agent가 수정 작업을 수행하기 위해 받는 정보이다.

Fix Agent는 Review Findings만 보고 수정하지 않는다. Original User Request, PM Agent Decision, Shared State, Review Report, Target Output, Domain Rules, Done Criteria를 함께 참조해야 한다.

Fix Input 기본 구조:

```text
Original User Request
→ PM Agent Decision
→ Shared State
→ Review Report
→ Review Findings
→ Target Output
→ Domain Rules
→ Done Criteria
```

Fix Input이 부족하면 Fix Agent는 기존 요구사항을 훼손하거나 Review 범위 밖의 수정을 할 수 있다.

---

### [핵심]

- Fix Agent는 Review Findings를 기준으로 수정한다.
- Original User Request를 확인해야 한다.
- PM Agent Decision을 확인해야 한다.
- Shared State의 결정사항을 확인해야 한다.
- Review Report를 확인해야 한다.
- 수정 대상 Output을 확인해야 한다.
- Domain Rules를 확인해야 한다.
- Done Criteria를 확인해야 한다.
- Missing Context가 있으면 단정하지 않고 Open Question으로 표시해야 한다.

---

### [실무]

Fix Input Template:

```json
{
  "fixTarget": "Backend Agent Output",
  "originalUserRequest": "축제 리뷰 API 설계",
  "pmDecision": [
    "Review list uses Slice",
    "Authenticated user can create review",
    "Review author can update/delete own review"
  ],
  "sharedState": {
    "decisions": ["Rating range is 0 to 5", "ApiResponse format required"],
    "openQuestions": [
      "Can one user write multiple reviews for the same festival?"
    ]
  },
  "reviewReport": {
    "status": "Fail",
    "critical": ["리뷰 수정 / 삭제 API에 작성자 본인 확인 조건 누락"],
    "major": ["ReviewCreateReqDto Validation 기준 부족"]
  },
  "targetOutput": "Backend Agent Output Draft",
  "domainRules": [
    "Multi-Agent System Domain Rules",
    "API Design Domain Rules",
    "Security Advanced Domain Rules"
  ],
  "doneCriteria": [
    "Critical Issue 0개",
    "Security Rule 포함",
    "Validation 기준 포함",
    "Re-review 가능한 Updated Output 생성"
  ]
}
```

Fix Input 부족 예시:

```text
Review Finding만 있음
→ 원래 요구사항 없음
→ 수정 대상 Output 없음
→ Shared State 없음
→ 정확한 Fix 불가
```

---

### [FAQ]

Q. Fix Input이 뭐야?
A. Fix Agent가 수정 작업을 수행하기 위해 받는 Review Findings, Target Output, Shared State, Domain Rules, Done Criteria 등의 정보다.

Q. Fix Agent는 Review Findings만 보고 수정해도 돼?
A. 아니다. 기존 요구사항, PM Decision, Shared State, Target Output을 함께 확인해야 한다.

Q. Fix Input이 부족하면 어떻게 해?
A. 단정하지 않고 Missing Context 또는 Open Question으로 표시해야 한다.

Q. Fix Agent가 가장 먼저 확인할 것은?
A. Review Findings와 Target Output, Original User Request, PM Agent Decision이다.

---

## 2.2 Fix Context Priority

### [개념]

Fix Context Priority는 Fix Agent가 수정 작업 중 여러 Context가 충돌할 때 어떤 기준을 우선할지 정하는 순서이다.

Fix Agent는 Review Findings를 반영하되, 현재 User Request와 PM Agent Decision을 훼손하면 안 된다.

권장 우선순위:

```text
Current User Request
→ Explicit PM Agent Decision
→ Review Findings
→ Master Rules
→ Domain Rules
→ Shared State
→ Target Output
→ Long-term Memory
```

---

### [핵심]

- 현재 사용자 요청이 가장 우선이다.
- PM Agent Decision은 Workflow의 결정 기준이다.
- Review Findings는 수정 대상이다.
- Master Rules와 Domain Rules는 수정 방식의 기준이다.
- Shared State는 현재 Workflow의 결정사항이다.
- Target Output은 수정 대상이며 절대 기준이 아니다.
- Long-term Memory는 보조 정보다.
- 충돌이 발생하면 PM Agent에게 반환하거나 Open Question으로 표시한다.

---

### [실무]

Context 충돌 예시:

```text
Current User Request:
- 중간 응답 금지
- 작업 완료 후 결과만 출력

Target Output:
- 작업 과정 설명 포함
- 검수 과정 설명 포함

Fix Decision:
- Current User Request 우선
- 작업 과정 설명 제거
- 최종 결과만 출력
```

Review Finding과 PM Decision 충돌 예시:

```text
PM Agent Decision:
- 목록 조회는 Slice 사용

Review Finding:
- Page 사용 권장

Fix Decision:
- PM Decision 우선
- Review Finding을 적용하지 않음
- Reason: 명시된 결정사항과 충돌
```

Fix Conflict Output 예시:

```md
## Fix Conflict

### Conflict

Review Finding이 PM Agent Decision과 충돌함

### Priority

PM Agent Decision > Review Finding

### Decision

해당 Finding은 적용하지 않음

### Reason

Shared State에 Slice 사용이 명시되어 있음

### Re-review Required

Yes
```

---

### [FAQ]

Q. Fix Context Priority가 뭐야?
A. Fix Agent가 여러 Context 중 무엇을 우선 기준으로 삼을지 정하는 순서다.

Q. Review Finding과 PM Decision이 충돌하면 뭐가 우선이야?
A. 일반적으로 PM Agent Decision이 우선이며, 충돌은 Fix Conflict로 기록해야 한다.

Q. Target Output과 Domain Rules가 충돌하면?
A. Domain Rules를 우선하고 Target Output을 수정해야 한다.

Q. 현재 사용자 요청과 과거 Memory가 충돌하면?
A. 현재 사용자 요청이 우선이다.

---

# 3. Fix Scope

## 3.1 Fix Scope Definition

### [개념]

Fix Scope는 Fix Agent가 수정할 수 있는 범위이다.

Fix Scope는 Review Findings, PM Agent Decision, Domain Rules, Done Criteria를 기준으로 결정한다.

Fix Agent는 Fix Scope 밖의 대규모 변경을 임의로 수행하면 안 된다.

Fix Scope 구조:

```text
Review Finding
→ Fix Scope
→ Allowed Changes
→ Forbidden Changes
→ Updated Output
```

---

### [핵심]

- Fix Scope는 수정 범위이다.
- Fix Scope는 Review Findings 기준으로 제한한다.
- Critical Issue는 우선 수정한다.
- Major Issue는 가능하면 수정한다.
- Minor Issue는 보고 후 종료 가능하다.
- Review 범위 밖 대규모 변경은 금지한다.
- 새 요구사항 생성은 금지한다.
- API Contract 변경은 영향 범위를 표시해야 한다.
- DB Schema 변경은 PM Agent Decision이 필요하다.

---

### [실무]

Fix Scope 예시:

```md
## Fix Scope

### Review Findings

- Critical: 작성자 본인 확인 조건 누락
- Major: Rating Validation 기준 부족

### Allowed Changes

- Security Rule 추가
- Service Layer 권한 검증 조건 추가
- DTO Validation 기준 추가
- Exception Case 추가

### Forbidden Changes

- API Path 변경
- Review Feature 요구사항 삭제
- DB Schema 임의 변경
- Frontend Flow 임의 변경
- 삭제 정책 임의 확정

### Expected Updated Output

- Backend Agent Output Revised Version
```

Fix Scope 검수 질문:

```text
이 수정은 Review Finding을 해결하는가?
이 수정은 기존 요구사항을 보존하는가?
이 수정은 PM Agent Decision과 충돌하지 않는가?
이 수정은 다른 Agent Output에 영향을 주는가?
이 수정은 사용자 승인이 필요한 위험 작업인가?
```

---

### [FAQ]

Q. Fix Scope가 뭐야?
A. Fix Agent가 Review Findings를 반영하기 위해 수정할 수 있는 범위다.

Q. Fix Agent가 Review 범위 밖도 고쳐도 돼?
A. 원칙적으로 안 된다. 범위 밖 변경은 PM Agent에게 반환해야 한다.

Q. Critical Issue는 반드시 고쳐야 해?
A. 그렇다. Critical Issue는 Pass 전에 반드시 수정해야 한다.

Q. API Contract를 바꾸는 Fix는 어떻게 처리해?
A. 영향 범위를 표시하고 PM Agent Decision 또는 Re-review를 요청해야 한다.

---

## 3.2 Fix Scope Control

### [개념]

Fix Scope Control은 Fix Agent가 수정 범위를 과도하게 확장하지 않도록 제어하는 규칙이다.

Fix Agent가 Review Findings를 넘어 구조를 크게 바꾸면 새로운 오류, Regression Risk, Agent 결과 충돌이 발생할 수 있다.

Fix Scope Control 구조:

```text
Review Finding
→ Minimal Required Change
→ Impact Check
→ Regression Risk Check
→ Apply Fix
```

---

### [핵심]

- 최소 수정 원칙을 적용한다.
- Review Findings와 직접 관련된 부분만 수정한다.
- 변경 전 영향 범위를 확인한다.
- 기존 요구사항을 삭제하지 않는다.
- 기존 API 계약을 무단 변경하지 않는다.
- 다른 Agent Output과 충돌하지 않게 한다.
- 위험 작업은 Human Confirmation 대상으로 분리한다.
- 새로 발견한 문제는 PM Agent 또는 Review Agent에게 반환한다.

---

### [실무]

잘못된 Fix 예시:

```text
Review Finding:
- DTO에 rating Validation 누락

Bad Fix:
- API Path 전체 변경
- Review Entity 구조 변경
- Frontend Flow까지 재설계
```

문제:

- Fix Scope 과도 확장
- 기존 API Contract 파괴
- Frontend Agent Output 충돌 가능
- Regression Risk 증가

좋은 Fix 예시:

```text
Review Finding:
- DTO에 rating Validation 누락

Good Fix:
- ReviewCreateReqDto에 rating 필드와 0~5 Validation 추가
- Invalid Rating Exception Case 추가
- 변경 내용과 영향 범위 표시
```

Fix Scope Control Checklist:

```md
## Fix Scope Control Checklist

- [ ] Review Finding과 직접 관련 있는 수정인가?
- [ ] 최소 수정으로 해결 가능한가?
- [ ] 기존 Requirement를 보존하는가?
- [ ] PM Decision과 충돌하지 않는가?
- [ ] API Contract 변경이 있는가?
- [ ] DB Schema 변경이 있는가?
- [ ] 다른 Agent Output에 영향이 있는가?
- [ ] Regression Risk를 표시했는가?
- [ ] 사용자 승인이 필요한 위험 작업인가?
```

---

### [FAQ]

Q. Fix Scope Control이 뭐야?
A. Fix Agent가 수정 범위를 과도하게 확장하지 않도록 제어하는 규칙이다.

Q. Fix는 크게 고치는 게 좋아?
A. 아니다. Review Findings를 해결하는 최소 수정이 원칙이다.

Q. Fix Scope가 커지면 어떤 문제가 생겨?
A. 기존 요구사항 훼손, API 충돌, Regression Risk 증가, Review-Fix Loop 반복이 발생할 수 있다.

Q. 새 문제를 발견하면 Fix Agent가 바로 고쳐도 돼?
A. Review 범위 밖이면 PM Agent 또는 Review Agent에게 반환해야 한다.

---

# 4. Fix Execution

## 4.1 Fix Execution Flow

### [개념]

Fix Execution은 Fix Agent가 Review Findings를 실제 산출물에 반영하는 단계이다.

Fix Execution은 Findings 분석, 수정 범위 결정, 변경 적용, 기존 요구사항 보존 확인, Regression Risk 표시, Updated Output 생성 순서로 진행한다.

기본 Flow:

```text
Receive Review Findings
→ Classify Severity
→ Select Fix Scope
→ Apply Changes
→ Preserve Requirement Check
→ Regression Risk Check
→ Updated Output
→ Re-review Request
```

---

### [핵심]

- Review Findings를 Severity별로 분류한다.
- Critical Issue를 먼저 수정한다.
- Major Issue를 다음으로 수정한다.
- Minor Issue는 필요 시 반영하거나 Notes로 남긴다.
- 변경 전 Fix Scope를 확정한다.
- 변경 후 기존 요구사항 보존 여부를 확인한다.
- Regression Risk를 기록한다.
- Updated Output은 Review 가능한 구조여야 한다.
- Re-review 필요 여부를 표시한다.

---

### [실무]

Fix Execution Template:

```md
## Fix Execution

### Review Findings

- Critical: 작성자 본인 확인 조건 누락
- Major: Rating Validation 기준 부족

### Selected Fixes

- 작성자 본인 확인 조건 추가
- Rating 0~5 Validation 기준 추가
- Invalid Rating Exception Case 추가

### Applied Changes

- updateReview()에 owner check 추가
- deleteReview()에 owner check 추가
- ReviewCreateReqDto에 rating validation 추가
- Exception Cases에 Invalid Rating 추가

### Preserved Requirements

- 기존 API Path 유지
- 기존 ApiResponse Format 유지
- Slice 목록 조회 유지

### Regression Risk

- 기존 테스트에서 인증 없는 수정 / 삭제 요청 실패 가능성 확인 필요
- Frontend에서 rating 입력값 검증 필요

### Re-review Required

Yes
```

Fix Execution 실패 예시:

```md
## Fix Execution

### Status

Blocked

### Reason

Review Finding은 "기존 코드의 owner check 누락"을 지적했지만 기존 Service 코드가 제공되지 않음

### Required Context

- ReviewService.java
- SecurityContext 사용자 조회 방식
- Review Entity의 작성자 필드명

### Safe Alternative

일반적인 owner check 설계 방향만 제공 가능

### Next Step

PM Agent가 필요한 코드 Context를 수집한 뒤 재요청
```

---

### [FAQ]

Q. Fix Execution이 뭐야?
A. Fix Agent가 Review Findings를 실제 산출물에 반영하는 단계다.

Q. Fix Execution 순서는?
A. Findings 분류, Fix Scope 결정, 변경 적용, 요구사항 보존 확인, Regression Risk 기록, Updated Output 생성 순서다.

Q. Critical과 Major 중 무엇을 먼저 고쳐?
A. Critical Issue를 먼저 수정한다.

Q. 수정할 Context가 부족하면 어떻게 해?
A. Blocked 상태로 표시하고 Required Context와 Safe Alternative를 제공해야 한다.

---

## 4.2 Preserve Requirement Check

### [개념]

Preserve Requirement Check는 Fix Agent가 수정 과정에서 기존 요구사항을 훼손하지 않았는지 확인하는 검토이다.

Fix Agent는 문제를 수정하면서 기존 기능, API Contract, Output Format, PM Agent Decision을 유지해야 한다.

검토 구조:

```text
Original Requirement
→ PM Decision
→ Target Output
→ Applied Fix
→ Requirement Preservation Check
```

---

### [핵심]

- Fix 후 기존 요구사항을 확인한다.
- 기존 API Contract를 유지했는지 확인한다.
- 기존 Response Format을 유지했는지 확인한다.
- 기존 Domain Rules를 유지했는지 확인한다.
- PM Agent Decision을 유지했는지 확인한다.
- Shared State Decisions를 위반하지 않았는지 확인한다.
- 기존 기능을 삭제하지 않았는지 확인한다.
- 수정으로 새 요구사항을 만들지 않았는지 확인한다.

---

### [실무]

Preserve Requirement Checklist:

```md
## Preserve Requirement Checklist

- [ ] Original User Request가 유지되었는가?
- [ ] Functional Requirements가 삭제되지 않았는가?
- [ ] Non-functional Requirements가 유지되었는가?
- [ ] Constraints가 유지되었는가?
- [ ] PM Agent Decision이 유지되었는가?
- [ ] Shared State Decisions와 충돌하지 않는가?
- [ ] API Contract가 무단 변경되지 않았는가?
- [ ] Response Format이 유지되었는가?
- [ ] Domain Rules가 유지되었는가?
- [ ] Fix가 새 요구사항을 만들지 않았는가?
```

Preserve Requirement Finding 예시:

```md
## Preserve Requirement Check

### Status

Failed

### Issue

Fix 과정에서 기존 DELETE /reviews/{reviewId} API가 제거됨

### Impact

Original Requirement의 리뷰 삭제 기능이 누락됨

### Required Action

DELETE API를 복구하고 작성자 본인 확인 조건을 추가하는 방식으로 수정
```

---

### [FAQ]

Q. Preserve Requirement Check가 뭐야?
A. Fix Agent가 수정 과정에서 기존 요구사항과 결정사항을 훼손하지 않았는지 확인하는 검토다.

Q. Fix하면서 기존 API를 바꿔도 돼?
A. PM Agent Decision이나 Review Finding에 명시되지 않았다면 무단 변경하면 안 된다.

Q. 기존 요구사항이 삭제되면 어떤 문제야?
A. Fix는 성공해도 전체 요구사항 충족에 실패할 수 있다.

Q. Preserve Requirement Check는 언제 해?
A. Fix 적용 후 Updated Output을 만들기 전에 수행한다.

---

# 5. Fix Output

## 5.1 Fix Output Structure

### [개념]

Fix Output은 Fix Agent가 Review Findings를 반영한 결과를 구조화해 반환하는 산출물이다.

Fix Output은 변경된 최종 산출물뿐 아니라 Applied Fix, Preserved Requirement, Change Summary, Regression Risk, Re-review Request를 포함해야 한다.

기본 구조:

```text
Fix Summary
→ Applied Fix
→ Updated Output
→ Preserved Requirement
→ Change Summary
→ Regression Risk
→ Open Questions
→ Re-review Request
```

---

### [핵심]

- Fix Output은 구조화되어야 한다.
- 어떤 Review Finding을 반영했는지 표시한다.
- Applied Fix를 명확히 작성한다.
- Updated Output을 제공한다.
- 보존된 요구사항을 표시한다.
- 변경 요약을 작성한다.
- Regression Risk를 표시한다.
- 남은 Open Question을 표시한다.
- Re-review 필요 여부를 명시한다.

---

### [실무]

Fix Output Template:

```md
## Fix Output

### Source Agent

Fix Agent

### Fix Target

Backend Agent Output - Festival Review API

### Review Findings Addressed

- Critical: 작성자 본인 확인 조건 누락
- Major: Rating Validation 기준 부족

### Applied Fix

- updateReview() 작성자 본인 확인 조건 추가
- deleteReview() 작성자 본인 확인 조건 추가
- rating 0~5 Validation 기준 추가
- Invalid Rating Exception Case 추가

### Updated Output

<수정된 Backend Agent Output>

### Preserved Requirements

- 기존 API Path 유지
- 기존 ApiResponse Format 유지
- Slice 목록 조회 유지
- 인증 사용자 기준 유지

### Change Summary

- 보안 권한 검증 추가
- 입력값 검증 강화
- 예외 케이스 보강

### Regression Risk

- 기존 테스트에서 수정 / 삭제 권한 검증 필요
- Frontend rating 입력값과 Backend Validation 일치 확인 필요

### Open Questions

- 동일 축제 중복 리뷰 허용 여부는 아직 미확정

### Re-review Required

Yes
```

간단한 Fix Output 예시:

```md
## Fix Output

### Status

Fixed

### Applied Fix

- Retrieval Queries Block 추가
- FAQ Q/A 형식 보강

### Preserved Requirements

- 기존 문서 제목 유지
- 기존 Section 구조 유지

### Regression Risk

- 없음

### Re-review Required

No
```

---

### [FAQ]

Q. Fix Output이 뭐야?
A. Fix Agent가 Review Findings를 반영한 결과를 구조화해 반환하는 산출물이다.

Q. Fix Output에는 뭐가 들어가야 해?
A. Applied Fix, Updated Output, Preserved Requirements, Change Summary, Regression Risk, Open Questions, Re-review Required가 들어가야 한다.

Q. Fix Output에 Regression Risk가 필요한 이유는?
A. 수정으로 인해 기존 기능이나 다른 Agent Output에 영향이 생길 수 있기 때문이다.

Q. Re-review Required는 반드시 표시해야 해?
A. 표시하는 것이 좋다. Review-Fix Loop 종료 여부를 판단하는 기준이 된다.

---

## 5.2 Change Summary

### [개념]

Change Summary는 Fix Agent가 무엇을 왜 변경했는지 요약한 기록이다.

Change Summary는 PM Agent, Review Agent, 사용자에게 수정 내역을 빠르게 이해시키는 역할을 한다.

Change Summary는 단순 변경 목록이 아니라 Review Finding과 연결되어야 한다.

기본 구조:

```text
Review Finding
→ Applied Change
→ Reason
→ Impact
```

---

### [핵심]

- Change Summary는 수정 내역 요약이다.
- Review Finding과 연결해야 한다.
- 변경 이유를 포함해야 한다.
- 변경 영향 범위를 표시해야 한다.
- API Contract 변경 여부를 표시해야 한다.
- DB Schema 변경 여부를 표시해야 한다.
- 다른 Agent Output 영향 여부를 표시해야 한다.
- PM Agent가 통합에 사용할 수 있어야 한다.

---

### [실무]

Change Summary Template:

```md
## Change Summary

| Review Finding             | Applied Change                 | Reason                | Impact                   |
| -------------------------- | ------------------------------ | --------------------- | ------------------------ |
| 작성자 본인 확인 조건 누락 | update/delete owner check 추가 | 권한 상승 방지        | Backend Security 강화    |
| Rating Validation 누락     | 0~5 Validation 추가            | 잘못된 평점 입력 방지 | DTO / Frontend Form 영향 |
| Retrieval Queries 누락     | Retrieval Queries Block 추가   | RAG 검색 최적화       | 문서 검색 매칭 개선      |
```

Change Impact 표시 예시:

```md
## Change Impact

### API Contract Changed

No

### DB Schema Changed

No

### Frontend Impact

Rating validation message 반영 필요

### Re-review Required

Yes
```

---

### [FAQ]

Q. Change Summary가 뭐야?
A. Fix Agent가 무엇을 왜 변경했는지 Review Finding과 연결해 요약한 기록이다.

Q. Change Summary가 필요한 이유는?
A. PM Agent와 Review Agent가 수정 내역과 영향 범위를 빠르게 파악하기 위해 필요하다.

Q. Change Summary에는 뭐가 있어야 해?
A. Review Finding, Applied Change, Reason, Impact가 있어야 한다.

Q. API Contract 변경 여부도 표시해야 해?
A. 표시해야 한다. Backend / Frontend / Review Agent의 일관성 검토에 필요하다.

---

# 6. Regression Risk

## 6.1 Regression Risk Definition

### [개념]

Regression Risk는 Fix Agent가 수정한 내용이 기존 요구사항, 기능, API Contract, Agent Output에 부정적 영향을 줄 가능성이다.

Fix Agent는 문제를 수정한 뒤에도 기존 동작이 깨질 수 있음을 표시해야 한다.

Regression Risk 구조:

```text
Applied Fix
→ Affected Area
→ Possible Regression
→ Verification Needed
```

---

### [핵심]

- Regression Risk는 수정으로 인한 부작용 가능성이다.
- Fix 후 기존 요구사항이 깨질 수 있다.
- API Contract 변경은 Frontend에 영향을 줄 수 있다.
- DB Schema 변경은 Backend와 데이터 마이그레이션에 영향을 줄 수 있다.
- Security Rule 변경은 기존 요청 흐름에 영향을 줄 수 있다.
- RAG 문서 구조 변경은 Retrieval 결과에 영향을 줄 수 있다.
- Regression Risk는 Re-review 기준으로 사용된다.

---

### [실무]

Regression Risk 예시:

```md
## Regression Risk

### Applied Fix

리뷰 수정 / 삭제 API에 작성자 본인 확인 조건 추가

### Affected Area

- Backend Service
- Security Rule
- Review API Test
- Frontend Error Handling

### Possible Regression

- 기존 테스트에서 인증 없는 수정 / 삭제 요청 실패
- Frontend에서 403 Error 처리 누락 가능
- 관리자 권한 예외 정책 필요 가능

### Verification Needed

- 작성자 본인 수정 성공 테스트
- 타 사용자 수정 실패 테스트
- 인증 없는 요청 실패 테스트
- Frontend 403 처리 확인
```

RAG 문서 Regression Risk 예시:

```md
## Regression Risk

### Applied Fix

FAQ 구조와 Retrieval Queries 보강

### Affected Area

- Chunk Boundary
- Query Matching
- 문서 길이

### Possible Regression

- FAQ 중복 증가 가능
- Chunk 크기 증가 가능

### Verification Needed

- 중복 FAQ 제거
- Retrieval Queries 사용자 질문 표현 확인
- Section별 독립 검색 가능 여부 확인
```

---

### [FAQ]

Q. Regression Risk가 뭐야?
A. Fix Agent가 수정한 내용이 기존 기능, 요구사항, API Contract, Agent Output에 부정적 영향을 줄 가능성이다.

Q. Fix가 성공해도 Regression Risk가 있어?
A. 있다. 문제를 고치면서 다른 부분이 깨질 수 있다.

Q. Regression Risk에는 뭐가 있어야 해?
A. Applied Fix, Affected Area, Possible Regression, Verification Needed가 있어야 한다.

Q. Regression Risk는 누가 검토해?
A. Review Agent가 Re-review 단계에서 검토한다.

---

# 7. Fix Agent Failure Handling

## 7.1 Fix Agent Failure Cases

### [개념]

Fix Agent Failure는 Fix Agent가 Review Findings를 잘못 해석하거나, 수정 범위를 벗어나거나, 기존 요구사항을 훼손하거나, Regression Risk를 숨길 때 발생한다.

주요 실패 유형:

```text
Review Finding Misread
Over-fixing
Requirement Damage
New Requirement Creation
No Change Summary
No Regression Risk
No Re-review Request
Tool Permission Violation
Context Missing
```

---

### [핵심]

- Review Finding을 잘못 해석하면 잘못된 수정이 발생한다.
- Over-fixing은 기존 구조를 불필요하게 바꾼다.
- 기존 요구사항을 훼손하면 Fix 실패이다.
- 새 요구사항을 만들면 PM Agent로 반환해야 한다.
- Change Summary가 없으면 수정 추적이 어렵다.
- Regression Risk를 숨기면 Re-review 품질이 떨어진다.
- 위험 Tool은 사용자 승인 없이 실행하면 안 된다.
- Context가 부족하면 Blocked 상태로 반환해야 한다.

---

### [실무]

Fix Agent Failure 예시:

```md
## Bad Fix

### Review Finding

Rating Validation 누락

### Applied Fix

Review API 전체 경로 변경
Review Entity 구조 변경
Frontend Form 구조 변경
```

문제:

- Fix Scope 과도 확장
- Review Finding과 직접 관련 없음
- API Contract 파괴
- Frontend Agent Output 충돌 가능
- Regression Risk 미표시

Good Fix:

```md
## Good Fix

### Review Finding

Rating Validation 누락

### Applied Fix

ReviewCreateReqDto와 ReviewUpdateReqDto에 rating 0~5 Validation 기준 추가

### Preserved Requirements

- 기존 API Path 유지
- 기존 Response Format 유지

### Regression Risk

- Frontend rating 입력 검증과 Backend Validation 일치 확인 필요

### Re-review Required

Yes
```

Context Missing 처리:

```md
## Fix Agent Output

### Status

Blocked

### Reason

기존 코드가 제공되지 않아 Review Finding을 실제 코드에 반영할 수 없음

### Required Context

- Target File
- Current Code
- Existing API Contract

### Safe Alternative

일반 수정 방향만 제공 가능

### Next Step

PM Agent가 Required Context를 확보한 뒤 재요청
```

---

### [FAQ]

Q. Fix Agent Failure는 언제 발생해?
A. Review Finding을 잘못 해석하거나, 수정 범위를 벗어나거나, 기존 요구사항을 훼손할 때 발생한다.

Q. Over-fixing이 뭐야?
A. Review Finding을 해결하는 데 필요한 범위를 넘어 불필요하게 구조를 크게 바꾸는 것이다.

Q. Fix Agent가 기존 요구사항을 삭제하면?
A. Fix 실패다. Preserve Requirement Check를 다시 수행해야 한다.

Q. Context가 부족하면 Fix Agent는 어떻게 해야 해?
A. Blocked 상태로 반환하고 Required Context와 Safe Alternative를 제공해야 한다.

---

## 7.2 Fix Agent Checklist

### [개념]

Fix Agent Checklist는 Fix Agent가 수정 전후에 Review Findings, Fix Scope, 기존 요구사항 보존, Regression Risk를 확인하는 기준이다.

Checklist를 적용하면 Over-fixing, 요구사항 훼손, 변경 추적 누락을 줄일 수 있다.

---

### [핵심]

- 수정 전 Review Findings를 확인한다.
- 수정 전 Original User Request를 확인한다.
- PM Agent Decision을 확인한다.
- Shared State Decisions를 확인한다.
- Fix Scope를 제한한다.
- 수정 후 기존 요구사항 보존 여부를 확인한다.
- Change Summary를 작성한다.
- Regression Risk를 표시한다.
- Re-review 필요 여부를 표시한다.
- 위험 작업은 Human Confirmation 대상으로 분리한다.

---

### [실무]

Fix Agent Pre-Fix Checklist:

```md
## Fix Agent Pre-Fix Checklist

- [ ] Review Findings를 확인했는가?
- [ ] Severity를 확인했는가?
- [ ] Original User Request를 확인했는가?
- [ ] PM Agent Decision을 확인했는가?
- [ ] Shared State Decisions를 확인했는가?
- [ ] Target Output을 확인했는가?
- [ ] Domain Rules를 확인했는가?
- [ ] Done Criteria를 확인했는가?
- [ ] Fix Scope를 정의했는가?
- [ ] Forbidden Changes를 정의했는가?
- [ ] Missing Context가 있는가?
- [ ] 위험 Tool 사용이 필요한가?
```

Fix Agent Final Checklist:

```md
## Fix Agent Final Checklist

- [ ] Critical Issue를 수정했는가?
- [ ] Major Issue를 처리했는가?
- [ ] Minor Issue 처리 방식을 표시했는가?
- [ ] 기존 Requirement를 보존했는가?
- [ ] PM Decision과 충돌하지 않는가?
- [ ] Shared State Decisions와 충돌하지 않는가?
- [ ] API Contract 변경 여부를 표시했는가?
- [ ] DB Schema 변경 여부를 표시했는가?
- [ ] Change Summary를 작성했는가?
- [ ] Regression Risk를 표시했는가?
- [ ] Open Question을 표시했는가?
- [ ] Re-review 필요 여부를 표시했는가?
```

---

### [FAQ]

Q. Fix Agent Checklist가 뭐야?
A. Fix Agent가 수정 전후에 Review Findings, Fix Scope, 요구사항 보존, Regression Risk를 확인하는 기준이다.

Q. Fix 전에 확인해야 할 것은?
A. Review Findings, Severity, Original User Request, PM Decision, Shared State, Target Output, Fix Scope다.

Q. Fix 후 확인해야 할 것은?
A. Critical / Major 처리 여부, 요구사항 보존, Change Summary, Regression Risk, Re-review 필요 여부다.

Q. Checklist가 필요한 이유는?
A. Over-fixing, 요구사항 훼손, Regression Risk 누락, Review-Fix Loop 반복을 줄이기 위해서다.

---

# 8. RAG Document Fix Agent

## 8.1 RAG Document Fix

### [개념]

RAG Document Fix는 Review Agent가 발견한 RAG 문서 문제를 MASTER_RAG_RULES와 Target DOMAIN_RULES 기준에 맞게 수정하는 작업이다.

RAG Document Fix는 사람용 문장 개선보다 Retrieval 최적화, FAQ 강화, Required Section 복구, Retrieval Queries 보강을 우선한다.

RAG Document Fix 구조:

```text
RAG Review Findings
→ Fix Agent
→ Required Section Fix
→ FAQ Fix
→ Retrieval Queries Fix
→ Naming Consistency Fix
→ Updated RAG Document
→ Re-review
```

---

### [핵심]

- RAG Document Fix는 Retrieval 최적화가 우선이다.
- MASTER_RAG_RULES를 보존해야 한다.
- Target DOMAIN_RULES를 보존해야 한다.
- Required Section을 복구해야 한다.
- FAQ는 Q + A 형식으로 보강한다.
- Retrieval Queries는 문서 마지막에 둔다.
- 용어 통일을 유지한다.
- Chunk 독립성을 유지한다.
- 중복 설명을 줄인다.
- 오타를 최소화한다.
- 무분별한 `---` 사용을 피한다.

---

### [실무]

RAG Document Fix 대상:

| Review Finding         | Fix Direction                              |
| ---------------------- | ------------------------------------------ |
| `[FAQ]` 누락           | 각 주요 Section에 Q/A 추가                 |
| Retrieval Queries 누락 | 문서 마지막에 Retrieval Queries Block 추가 |
| 장문 에세이형 설명     | Bullet / Short Chunk로 분리                |
| 용어 혼용              | 표준 용어로 통일                           |
| Section 구조 누락      | `[개념]`, `[핵심]`, `[실무]`, `[FAQ]` 복구 |
| 중복 설명 과다         | 중복 Chunk 제거                            |
| FAQ에 답변 없음        | Q + A 형식으로 수정                        |
| 파일명 불명확          | Domain + Part + Topic 기준으로 변경        |

RAG Document Fix Output 예시:

```md
## RAG Document Fix Output

### Fix Target

Multi_Agent_System_Part05_Review_Agent.md

### Review Findings Addressed

- Retrieval Queries 일부 부족
- FAQ 표현 중복
- Severity 관련 검색 질문 부족

### Applied Fix

- Retrieval Queries에 Severity / Pass Fail / Review Finding 질문 추가
- 중복 FAQ 표현 정리
- Review-Fix Loop 검색 질문 보강

### Preserved Requirements

- Required Section 유지
- 기존 Document Title 유지
- MASTER_RAG_RULES 구조 유지

### Regression Risk

- FAQ 증가로 문서 길이 증가 가능

### Re-review Required

No
```

---

### [FAQ]

Q. RAG Document Fix가 뭐야?
A. Review Agent가 발견한 RAG 문서 문제를 Master Rules와 Domain Rules 기준에 맞게 수정하는 작업이다.

Q. RAG Document Fix에서 가장 중요한 것은?
A. Retrieval 최적화, Required Section, FAQ, Retrieval Queries, 용어 통일이다.

Q. RAG 문서 Fix는 사람용 문장 개선이 우선이야?
A. 아니다. AI Agent Retrieval 성능을 높이는 구조 수정이 우선이다.

Q. RAG Document Fix 후 Re-review가 필요해?
A. Critical 또는 Major 수정이면 필요하고, Minor 보강이면 필요하지 않을 수 있다.

---

# Retrieval Queries

### [FAQ]

Q. Fix Agent는 뭐야?
A. Review Agent가 발견한 문제를 기존 요구사항과 Review Findings 범위 안에서 수정하는 Agent다.

Q. Fix Agent의 핵심 역할은?
A. Review Findings를 반영하고 기존 요구사항을 보존하며 Updated Output을 생성하는 것이다.

Q. Fix Agent가 새 요구사항을 추가해도 돼?
A. 안 된다. 새 요구사항은 PM Agent에게 반환해야 한다.

Q. Fix Agent와 Review Agent 차이는?
A. Review Agent는 문제를 찾고, Fix Agent는 Review Findings를 반영해 산출물을 수정한다.

Q. Fix Input이 뭐야?
A. Fix Agent가 수정 작업을 수행하기 위해 받는 Review Findings, Target Output, Shared State, Domain Rules, Done Criteria 등의 정보다.

Q. Fix Agent는 Review Findings만 보고 수정해도 돼?
A. 아니다. 기존 요구사항, PM Decision, Shared State, Target Output을 함께 확인해야 한다.

Q. Fix Context Priority가 뭐야?
A. Fix Agent가 여러 Context 중 무엇을 우선 기준으로 삼을지 정하는 순서다.

Q. Review Finding과 PM Decision이 충돌하면 뭐가 우선이야?
A. 일반적으로 PM Agent Decision이 우선이며, 충돌은 Fix Conflict로 기록해야 한다.

Q. Fix Scope가 뭐야?
A. Fix Agent가 Review Findings를 반영하기 위해 수정할 수 있는 범위다.

Q. Fix Agent가 Review 범위 밖도 고쳐도 돼?
A. 원칙적으로 안 된다. 범위 밖 변경은 PM Agent에게 반환해야 한다.

Q. Fix Scope Control이 뭐야?
A. Fix Agent가 수정 범위를 과도하게 확장하지 않도록 제어하는 규칙이다.

Q. Fix는 크게 고치는 게 좋아?
A. 아니다. Review Findings를 해결하는 최소 수정이 원칙이다.

Q. Over-fixing이 뭐야?
A. Review Finding을 해결하는 데 필요한 범위를 넘어 불필요하게 구조를 크게 바꾸는 것이다.

Q. Fix Execution이 뭐야?
A. Fix Agent가 Review Findings를 실제 산출물에 반영하는 단계다.

Q. Fix Execution 순서는?
A. Findings 분류, Fix Scope 결정, 변경 적용, 요구사항 보존 확인, Regression Risk 기록, Updated Output 생성 순서다.

Q. Critical과 Major 중 무엇을 먼저 고쳐?
A. Critical Issue를 먼저 수정한다.

Q. 수정할 Context가 부족하면 어떻게 해?
A. Blocked 상태로 표시하고 Required Context와 Safe Alternative를 제공해야 한다.

Q. Preserve Requirement Check가 뭐야?
A. Fix Agent가 수정 과정에서 기존 요구사항과 결정사항을 훼손하지 않았는지 확인하는 검토다.

Q. Fix하면서 기존 API를 바꿔도 돼?
A. PM Agent Decision이나 Review Finding에 명시되지 않았다면 무단 변경하면 안 된다.

Q. Fix Output이 뭐야?
A. Fix Agent가 Review Findings를 반영한 결과를 구조화해 반환하는 산출물이다.

Q. Fix Output에는 뭐가 들어가야 해?
A. Applied Fix, Updated Output, Preserved Requirements, Change Summary, Regression Risk, Open Questions, Re-review Required가 들어가야 한다.

Q. Change Summary가 뭐야?
A. Fix Agent가 무엇을 왜 변경했는지 Review Finding과 연결해 요약한 기록이다.

Q. Change Summary에는 뭐가 있어야 해?
A. Review Finding, Applied Change, Reason, Impact가 있어야 한다.

Q. Regression Risk가 뭐야?
A. Fix Agent가 수정한 내용이 기존 기능, 요구사항, API Contract, Agent Output에 부정적 영향을 줄 가능성이다.

Q. Fix가 성공해도 Regression Risk가 있어?
A. 있다. 문제를 고치면서 다른 부분이 깨질 수 있다.

Q. Regression Risk에는 뭐가 있어야 해?
A. Applied Fix, Affected Area, Possible Regression, Verification Needed가 있어야 한다.

Q. Fix Agent Failure는 언제 발생해?
A. Review Finding을 잘못 해석하거나, 수정 범위를 벗어나거나, 기존 요구사항을 훼손할 때 발생한다.

Q. Fix Agent가 기존 요구사항을 삭제하면?
A. Fix 실패다. Preserve Requirement Check를 다시 수행해야 한다.

Q. Context가 부족하면 Fix Agent는 어떻게 해야 해?
A. Blocked 상태로 반환하고 Required Context와 Safe Alternative를 제공해야 한다.

Q. Fix Agent Checklist가 뭐야?
A. Fix Agent가 수정 전후에 Review Findings, Fix Scope, 요구사항 보존, Regression Risk를 확인하는 기준이다.

Q. Fix 전에 확인해야 할 것은?
A. Review Findings, Severity, Original User Request, PM Decision, Shared State, Target Output, Fix Scope다.

Q. Fix 후 확인해야 할 것은?
A. Critical / Major 처리 여부, 요구사항 보존, Change Summary, Regression Risk, Re-review 필요 여부다.

Q. RAG Document Fix가 뭐야?
A. Review Agent가 발견한 RAG 문서 문제를 Master Rules와 Domain Rules 기준에 맞게 수정하는 작업이다.

Q. RAG Document Fix에서 가장 중요한 것은?
A. Retrieval 최적화, Required Section, FAQ, Retrieval Queries, 용어 통일이다.

Q. RAG 문서 Fix는 사람용 문장 개선이 우선이야?
A. 아니다. AI Agent Retrieval 성능을 높이는 구조 수정이 우선이다.

Q. 개인 AI 개발팀에서 Fix Agent는 언제 사용해?
A. Review Agent가 Critical 또는 Major Issue를 발견했을 때 사용한다.

Q. Review-Fix Loop에서 Fix Agent의 종료 기준은?
A. Review Findings 반영, 기존 요구사항 보존, Regression Risk 표시, Re-review 요청 완료다.
