# Frontend Code Review Part01 - Overview and Review Priority

---

# 1. Frontend Code Review Overview

## 1.1 Frontend Code Review Purpose

### [개념]

Frontend Code Review는 React 기반 프론트엔드 코드가 요구사항, 사용자 흐름, 유지보수성, 안정성, 접근성, 보안, 성능, 빌드 가능성을 만족하는지 검토하는 과정이다.

이 문서는 사람 학습용 문서가 아니다.

목적은 Frontend Agent, Review Agent, PM Agent가 프론트엔드 코드의 품질과 배포 가능성을 판단할 수 있도록 Retrieval 기준을 제공하는 것이다.

---

### [핵심]

Frontend Code Review의 목적:

- 요구사항 충족 여부 검토
- UI 사용자 흐름 검토
- Component 구조 검토
- Props / State 설계 검토
- React Hooks 사용 검토
- API Integration 안정성 검토
- Error / Loading / Empty State 검토
- Form Validation 검토
- Authentication Flow 검토
- Routing 검토
- Accessibility 검토
- Frontend Security 검토
- Performance 위험 검토
- Testability 검토
- Build / Deploy 위험 검토
- Final Decision 판단

---

### [실무]

Frontend Code Review는 단순 문법 검사가 아니다.

2026 실무 기준에서 프론트엔드 리뷰는 다음 순서로 수행한다.

```text
User Requirement
→ UI Behavior Check
→ Component Structure Review
→ State / Props Review
→ API Integration Review
→ UX State Review
→ Authentication Review
→ Accessibility Review
→ Security Review
→ Performance Review
→ Testability Review
→ Build Deploy Risk Review
→ Final Review Result
```

Review Agent는 코드가 “동작하는 것처럼 보이는지”가 아니라 “사용자가 실제로 안정적으로 사용할 수 있는지”를 기준으로 판단한다.

---

### [FAQ]

Q. Frontend Code Review 문서는 사람 공부용이야?
A. 아니다. Frontend Agent / Review Agent / PM Agent가 코드 품질과 배포 가능성을 판단하기 위한 RAG 문서다.

Q. 프론트엔드 코드 리뷰에서 문법만 확인하면 돼?
A. 아니다. 요구사항, 사용자 흐름, API 실패, 인증, 접근성, 보안, 빌드 위험까지 함께 검토해야 한다.

Q. Review Agent는 어떤 기준으로 프론트엔드 코드를 봐야 해?
A. 요구사항 충족, 주요 사용자 흐름, Critical / High 위험, 유지보수성, 배포 가능성을 우선 검토한다.

Q. PM Agent도 Frontend Code Review 결과를 사용해?
A. 사용한다. PM Agent는 리뷰 결과를 기반으로 기능 완료 여부, 위험도, 배포 가능 여부를 판단한다.

---

## 1.2 Frontend Review Scope

### [개념]

Frontend Review Scope는 Review Agent가 프론트엔드 코드 리뷰에서 반드시 검토해야 하는 범위이다.

리뷰 범위는 코드 스타일만이 아니라 기능 요구사항, 사용자 경험, 운영 위험, 배포 가능성을 포함한다.

---

### [핵심]

포함 범위:

- Requirement Review
- UI Behavior Review
- Component Responsibility Review
- Component Naming Review
- Props Review
- State Location Review
- State Duplication Review
- State Update Review
- useEffect Review
- Custom Hook Review
- Hook Rule Review
- API Module Review
- API Error Review
- Request Duplication Review
- Loading State Review
- Error State Review
- Empty State Review
- Form Structure Review
- Validation Review
- Form Submit Review
- Auth Flow Review
- Token Storage Review
- Protected Route Review
- Route Structure Review
- Navigation Review
- Accessibility Review
- Styling Consistency Review
- Responsive Review
- TypeScript Review
- Performance Review
- Security Review
- Testability Review
- Build Deploy Review
- PR Review Checklist

---

### [실무]

Frontend Code Review는 다음 Domain Rules와 연결된다.

```text
React Core
→ React Component Design
→ React Router
→ State Management
→ Data Fetching REST API Integration
→ Form Handling Validation
→ Authentication Frontend Flow
→ Error Handling Loading UX
→ UI Component Pattern
→ Frontend Testing
→ Frontend Accessibility
→ Frontend Build Deploy
→ Frontend Code Review
```

Review Agent는 변경 범위에 따라 모든 항목을 동일하게 검토하지 않는다.

우선순위는 다음 기준으로 정한다.

```text
Critical Risk
→ User Flow Blocking
→ API / Auth Failure
→ Build Deploy Risk
→ Maintainability
→ Accessibility
→ Performance
→ Suggestion
```

---

### [FAQ]

Q. Frontend Code Review는 다른 Frontend 문서와 겹치지 않아?
A. 겹치는 개념을 다시 학습하는 문서가 아니라 기존 Frontend Domain Rules를 기준으로 리뷰 관점을 제공하는 문서다.

Q. 리뷰할 때 모든 항목을 매번 전부 봐야 해?
A. 변경 범위에 따라 선택 적용할 수 있지만 Critical / High 위험 항목은 항상 확인해야 한다.

Q. Frontend Review Scope에서 가장 중요한 범위는 뭐야?
A. 요구사항 충족, 사용자 흐름, API 실패 처리, 인증, 보안, 빌드 가능성이다.

Q. 사소한 스타일 문제도 리뷰해야 해?
A. 가능하지만 Critical / High 문제보다 우선하지 않는다. 취향성 의견은 Suggestion으로 분리한다.

---

# 2. Review Priority Rules

## 2.1 Review Priority Classification

### [개념]

Review Priority Classification은 코드 리뷰 문제를 영향도와 위험도에 따라 분류하는 규칙이다.

모든 리뷰 이슈를 같은 중요도로 다루면 수정 우선순위가 흐려진다.

Review Agent는 반드시 문제에 우선순위를 붙여야 한다.

---

### [핵심]

Frontend Code Review 우선순위:

| Priority   | 의미                                            | 예시                                              |
| ---------- | ----------------------------------------------- | ------------------------------------------------- |
| Critical   | 즉시 수정 필요, 서비스 장애 또는 보안 사고 가능 | 빌드 실패, 로그인 불가, Secret Key 노출           |
| High       | 주요 기능 오류 또는 운영 위험                   | API 에러 미처리, 인증 체크 누락, 사용자 흐름 중단 |
| Medium     | 유지보수성 또는 UX 문제                         | Empty State 누락, 컴포넌트 책임 과다              |
| Low        | 개선 권장                                       | naming 애매함, 작은 스타일 불일치                 |
| Suggestion | 선택 개선                                       | Custom Hook 분리 제안, 성능 최적화 여지           |

---

### [실무]

Review Agent는 아래 형식으로 문제를 분류한다.

```text
[Critical] npm run build 실패 가능성이 있음
[High] API 실패 시 사용자에게 에러 메시지가 표시되지 않음
[Medium] Page Component가 API 호출, Form 상태, Modal 상태를 모두 관리함
[Low] 변수명이 역할을 명확히 드러내지 않음
[Suggestion] 반복되는 Modal 제어 로직을 useModal custom hook으로 분리 가능
```

Critical / High 문제는 병합 또는 배포 전에 반드시 수정해야 한다.

Medium 이하 문제는 일정, 변경 범위, 영향도에 따라 처리한다.

---

### [FAQ]

Q. 코드 리뷰에서 우선순위를 왜 붙여야 해?
A. 개발자와 PM Agent가 어떤 문제를 먼저 수정해야 하는지 판단하기 위해 필요하다.

Q. Critical Issue는 무조건 수정해야 해?
A. 그렇다. 빌드 실패, 보안 키 노출, 핵심 기능 미동작은 진행을 막는 문제다.

Q. High Issue도 반드시 수정해야 해?
A. 대부분 수정해야 한다. 주요 기능 오류, 인증 누락, API 실패 미처리는 운영 위험이 크다.

Q. Medium Issue는 배포를 막아야 해?
A. 일반적으로 배포를 막지는 않지만 유지보수성, UX, 변경 안정성에 영향을 줄 수 있다.

Q. Suggestion은 필수 수정이야?
A. 아니다. 선택 개선 사항이며 필수 수정과 명확히 구분해야 한다.

---

## 2.2 Critical Issue Rules

### [개념]

Critical Issue는 프론트엔드 기능 사용, 보안, 빌드, 배포를 즉시 막는 문제이다.

Critical Issue가 존재하면 Review Agent는 Final Decision을 `BLOCKED` 또는 `CHANGES REQUESTED`로 판단해야 한다.

---

### [핵심]

Critical Issue 예시:

- `npm run build` 실패
- 주요 페이지 흰 화면
- 로그인 불가
- 회원가입 불가
- 결제 Secret Key 노출
- JWT_SECRET 노출
- DB_PASSWORD 노출
- OPENAI_API_KEY 노출
- AWS_SECRET_ACCESS_KEY 노출
- 핵심 API endpoint 오연결
- 인증 필요한 페이지 전체 접근 불가
- 운영 API URL이 완전히 잘못됨
- import path 대소문자 오류로 Linux 배포 실패 가능
- 필수 환경 변수 누락으로 앱 실행 불가

---

### [실무]

Critical Issue 검토 Flow:

```text
Build Check
→ Runtime Blocking Error Check
→ Secret Exposure Check
→ Auth Blocking Check
→ Main User Flow Blocking Check
→ Deployment Blocking Check
→ Final Decision
```

Critical Issue 발견 시 리뷰 코멘트 예:

```text
[Critical] 프론트엔드 환경 변수에 TOSS_SECRET_KEY가 포함되어 있습니다. 브라우저 빌드 결과물에 노출될 수 있으므로 즉시 제거하고 백엔드 환경 변수로 이동해야 합니다.
```

```text
[Critical] import 경로의 파일명 대소문자가 실제 파일명과 다릅니다. Windows에서는 동작할 수 있지만 Linux 배포 환경에서 빌드 실패가 발생할 수 있습니다.
```

---

### [FAQ]

Q. Critical Issue가 있으면 APPROVED 가능해?
A. 불가능하다. Critical Issue가 있으면 BLOCKED 또는 CHANGES REQUESTED로 판단해야 한다.

Q. Secret Key 노출은 왜 Critical이야?
A. 브라우저 코드와 빌드 결과물은 사용자에게 노출될 수 있기 때문에 즉시 보안 사고로 이어질 수 있다.

Q. 개발 환경에서만 빌드 실패하면 Critical이야?
A. 운영 빌드 또는 팀 공통 환경에서 재현 가능하면 Critical로 볼 수 있다.

Q. 로그인 불가는 Critical이야?
A. 인증이 핵심 기능인 서비스라면 Critical이다. 사용자가 주요 기능에 접근할 수 없기 때문이다.

---

## 2.3 High Priority Issue Rules

### [개념]

High Priority Issue는 즉시 서비스 전체를 막지는 않지만 주요 사용자 흐름, 운영 안정성, 인증, API 연동에 큰 위험을 만드는 문제이다.

High Issue는 배포 전 수정이 권장된다.

---

### [핵심]

High Issue 예시:

- API 실패 시 catch 처리 없음
- Loading이 종료되지 않음
- 401 처리 누락
- Protected Route 누락
- 인증 header 누락
- Form 중복 제출 가능
- 서버 validation error 미표시
- 주요 사용자 흐름 중간 단계 누락
- 권한 없는 사용자의 수정 / 삭제 버튼 노출
- API baseURL localhost 하드코딩
- 토큰 console 출력
- 사용자 입력 HTML sanitize 없음
- 파일 업로드 확장자 / 크기 검증 없음
- 새로고침 후 인증 상태 복원 불가
- 필수 Empty State 누락으로 사용자 혼란 발생

---

### [실무]

High Issue 검토 Flow:

```text
User Flow Check
→ API Failure Check
→ Auth Failure Check
→ Form Submit Check
→ Security Risk Check
→ UX Recovery Check
→ Required Fix Decision
```

High Issue 리뷰 코멘트 예:

```text
[High] API 요청 실패 시 catch 처리가 없어 사용자가 빈 화면을 보게 됩니다. Error State를 추가하고 가능한 경우 재시도 버튼을 제공해야 합니다.
```

```text
[High] 제출 중 버튼 disabled 처리가 없어 사용자가 저장 버튼을 여러 번 클릭하면 중복 요청이 발생할 수 있습니다.
```

```text
[High] 인증이 필요한 페이지에 Protected Route가 없어 비로그인 사용자가 화면에 접근할 수 있습니다. 프론트엔드 보호는 UX 목적이며 백엔드 권한 검증도 함께 필요합니다.
```

---

### [FAQ]

Q. High Issue가 있으면 배포하면 안 돼?
A. 일반적으로 배포 전 수정이 권장된다. 주요 사용자 흐름이나 운영 안정성에 영향을 주기 때문이다.

Q. API 에러 미처리는 왜 High야?
A. 실패 상황에서 사용자가 원인을 알 수 없고 복구할 수 없어 운영 장애처럼 보일 수 있기 때문이다.

Q. localhost 하드코딩은 왜 High야?
A. 운영 사용자의 브라우저에서 localhost는 사용자 자신의 컴퓨터를 의미하므로 API 연결이 실패할 수 있다.

Q. 토큰 console 출력은 Critical이야 High야?
A. 노출 범위와 민감도에 따라 다르지만 일반적으로 High 이상으로 본다. 운영 코드에 남으면 보안 위험이다.

---

## 2.4 Medium Low Suggestion Rules

### [개념]

Medium, Low, Suggestion은 즉시 서비스 장애를 만들 가능성은 낮지만 유지보수성, 코드 품질, UX, 확장성에 영향을 주는 문제이다.

Review Agent는 필수 수정과 선택 개선을 구분해야 한다.

---

### [핵심]

Medium Issue 예시:

- 컴포넌트 책임 과다
- 중복 API 호출 코드
- 중복 validation 로직
- Empty State 일부 누락
- props 개수 과다
- state 중복 저장
- useEffect 남용
- list key에 index 사용
- inline style 반복
- 반응형 일부 깨짐
- 테스트하기 어려운 구조

Low Issue 예시:

- 변수명 의미 부족
- className naming 불일치
- 작은 spacing 불일치
- 사용하지 않는 주석 일부 잔존
- 파일 구조 개선 여지

Suggestion 예시:

- Custom Hook 분리 제안
- React Query 도입 검토
- route-based lazy loading 검토
- Design Token 도입 검토
- 공통 Button Component 추출 제안
- 테스트 커버리지 확대 제안

---

### [실무]

Medium / Low / Suggestion 리뷰 코멘트 예:

```text
[Medium] FestivalDetailPage가 API 호출, Modal 상태, Form 제출을 모두 처리하고 있습니다. 데이터 조회 로직은 custom hook으로 분리하면 유지보수성이 좋아집니다.
```

```text
[Low] isData와 같은 boolean 변수명은 의미가 모호합니다. hasFestivalData처럼 true / false 의미가 드러나는 이름이 좋습니다.
```

```text
[Suggestion] 검색 조건이 URL에 반영되면 새로고침 유지와 공유가 쉬워집니다. search params 사용을 검토할 수 있습니다.
```

Suggestion은 필수 수정처럼 표현하지 않는다.

---

### [FAQ]

Q. Medium Issue는 반드시 수정해야 해?
A. 반드시 즉시 수정해야 하는 것은 아니지만 유지보수성과 UX에 영향을 주므로 일정에 따라 처리한다.

Q. Low Issue는 리뷰하지 않아도 돼?
A. 리뷰할 수 있지만 Critical / High 문제보다 우선하지 않는다.

Q. Suggestion을 필수 수정처럼 말해도 돼?
A. 안 된다. 선택 개선 사항은 Suggestion으로 표시하고 필수 수정과 구분해야 한다.

Q. 컴포넌트가 큰 것은 항상 Critical이야?
A. 아니다. 기능을 막지 않는다면 보통 Medium이다. 다만 버그와 장애 위험을 만들면 High로 올라갈 수 있다.

---

# 3. Review Result Format

## 3.1 Standard Review Result Format

### [개념]

Standard Review Result Format은 Review Agent가 코드 리뷰 결과를 일관되게 출력하기 위한 구조이다.

일관된 출력 형식은 PM Agent와 개발자가 다음 작업을 빠르게 판단하도록 돕는다.

---

### [핵심]

권장 출력 구조:

```md
# Frontend Code Review Result

## Summary

## Critical Issues

## High Priority Issues

## Medium Priority Issues

## Low Priority Issues

## Suggestions

## Checklist

## Final Decision
```

각 섹션 역할:

| Section                | 역할               |
| ---------------------- | ------------------ |
| Summary                | 전체 리뷰 요약     |
| Critical Issues        | 즉시 차단 문제     |
| High Priority Issues   | 주요 운영 위험     |
| Medium Priority Issues | 유지보수 / UX 문제 |
| Low Priority Issues    | 작은 개선 사항     |
| Suggestions            | 선택 개선          |
| Checklist              | 주요 검토 항목     |
| Final Decision         | 승인 여부          |

---

### [실무]

Review Agent는 문제가 없는 섹션도 명시할 수 있다.

예:

```md
## Critical Issues

None

## High Priority Issues

None
```

문제가 없는 경우에도 Final Decision은 반드시 작성한다.

Final Decision 예:

```text
APPROVED
APPROVED WITH COMMENTS
CHANGES REQUESTED
BLOCKED
```

---

### [FAQ]

Q. Review Result Format이 왜 필요해?
A. 리뷰 결과를 매번 같은 구조로 출력해야 PM Agent와 개발자가 빠르게 판단할 수 있기 때문이다.

Q. 이슈가 없으면 섹션을 생략해도 돼?
A. 가능하지만 RAG Agent 출력 일관성을 위해 `None`으로 명시하는 것이 좋다.

Q. Final Decision은 반드시 필요해?
A. 필요하다. PM Agent가 병합, 수정, 배포 여부를 판단하는 기준이 된다.

Q. Checklist는 모든 항목을 포함해야 해?
A. 변경 범위에 맞게 선택할 수 있지만 Critical / High 관련 체크는 포함하는 것이 좋다.

---

## 3.2 Final Decision Rules

### [개념]

Final Decision은 프론트엔드 코드가 병합, 배포, 재작업, 차단 중 어디에 해당하는지 판단하는 최종 리뷰 결과이다.

Review Agent는 이슈 우선순위를 기반으로 Final Decision을 결정한다.

---

### [핵심]

Final Decision 기준:

| Decision               | 의미                | 기준                                 |
| ---------------------- | ------------------- | ------------------------------------ |
| APPROVED               | 병합 / 배포 가능    | Critical / High 없음, 주요 흐름 정상 |
| APPROVED WITH COMMENTS | 경미한 개선 권장    | Low / Suggestion 중심                |
| CHANGES REQUESTED      | 수정 후 재검토 필요 | High 또는 중요한 Medium 존재         |
| BLOCKED                | 진행 차단           | Critical 존재                        |

---

### [실무]

Final Decision 판단 Flow:

```text
Critical Issue Exists?
→ Yes
→ BLOCKED

High Issue Exists?
→ Yes
→ CHANGES REQUESTED

Only Medium / Low / Suggestion?
→ APPROVED WITH COMMENTS

No Meaningful Issue?
→ APPROVED
```

Final Decision 예:

```md
## Final Decision

CHANGES REQUESTED

## Reason

- [High] API 실패 시 Error State가 없습니다.
- [High] 로그인 만료 시 401 처리 흐름이 없습니다.

## Required Fixes

1. API 실패 catch 처리 및 사용자 메시지 추가
2. 401 발생 시 로그인 이동 또는 refresh flow 처리
```

---

### [FAQ]

Q. Critical Issue가 있으면 Final Decision은 뭐야?
A. BLOCKED로 판단한다. 빌드 실패, 보안 키 노출, 핵심 기능 미동작은 진행을 막아야 한다.

Q. High Issue가 있으면 Final Decision은 뭐야?
A. 일반적으로 CHANGES REQUESTED다. 수정 후 재검토가 필요하다.

Q. Low와 Suggestion만 있으면 승인 가능해?
A. 가능하다. 이 경우 APPROVED WITH COMMENTS가 적절하다.

Q. 아무 문제도 없으면 어떻게 판단해?
A. APPROVED로 판단한다.

---

# 4. Review Agent Operating Rules

## 4.1 Review Agent Review Flow

### [개념]

Review Agent Review Flow는 프론트엔드 코드 리뷰를 수행할 때 따라야 하는 표준 작업 순서이다.

Review Agent는 사소한 스타일보다 Critical Risk와 User Flow를 먼저 확인해야 한다.

---

### [핵심]

Review Agent 기본 순서:

```text
Diff Overview
→ Requirement Match
→ Critical Risk Scan
→ User Flow Review
→ Component Structure Review
→ State / Props Review
→ Hook Review
→ API Integration Review
→ UX State Review
→ Auth Review
→ Routing Review
→ Accessibility Review
→ Security Review
→ Performance Review
→ Testability Review
→ Build Deploy Risk Review
→ Final Decision
```

우선 확인할 항목:

- 요구사항 충족 여부
- 핵심 사용자 흐름
- 빌드 실패 가능성
- Secret Key 노출
- API 실패 처리
- 인증 누락
- Error / Loading / Empty State
- 운영 URL / 환경 변수 문제

---

### [실무]

Review Agent는 아래 순서로 판단한다.

```text
1. 변경 목적 파악
2. 주요 사용자 흐름 파악
3. Critical / High 위험 먼저 탐지
4. 구조와 유지보수성 검토
5. 접근성, 성능, 테스트 가능성 검토
6. 수정 필수 항목과 선택 개선 분리
7. Final Decision 출력
```

잘못된 리뷰 방식:

```text
취향 위주 리뷰
→ naming만 과도하게 지적
→ 요구사항 확인 없이 코드 스타일만 검토
→ API 실패 상황 미검토
→ 접근성 / 보안 / 빌드 위험 무시
→ 모든 문제를 같은 우선순위로 표시
```

---

### [FAQ]

Q. Review Agent는 파일을 위에서 아래로만 보면 돼?
A. 아니다. 먼저 변경 목적과 사용자 흐름을 파악한 뒤 위험도가 높은 부분부터 검토해야 한다.

Q. 리뷰에서 가장 먼저 찾아야 할 문제는 뭐야?
A. 빌드 실패, 보안 키 노출, 로그인 불가, API 실패 미처리, 핵심 사용자 흐름 중단이다.

Q. naming 문제부터 지적해도 돼?
A. 가능하지만 Critical / High 문제가 먼저다. naming은 보통 Low 또는 Suggestion으로 분리한다.

Q. Review Agent는 코드를 직접 수정해야 해?
A. 핵심 역할은 독립 검토와 승인 판단이다. 필요하면 수정 방향이나 패치 예시를 제공할 수 있다.

---

## 4.2 Review Comment Rules

### [개념]

Review Comment Rules는 Review Agent가 코드 리뷰 코멘트를 명확하고 실행 가능하게 작성하기 위한 규칙이다.

좋은 리뷰 코멘트는 문제, 이유, 수정 방향, 우선순위가 명확하다.

---

### [핵심]

좋은 리뷰 코멘트 조건:

- 우선순위 표시
- 문제 위치 명확
- 문제 이유 설명
- 수정 방향 제안
- 필수 수정과 선택 개선 구분
- 비난 없는 표현
- 실행 가능한 문장
- 과도한 리팩토링 요구 금지

나쁜 리뷰 코멘트:

```text
이거 별로임.
```

좋은 리뷰 코멘트:

```text
[High] API 실패 시 catch 처리가 없어 사용자가 빈 화면을 보게 됩니다. Error State를 추가하고 재시도 버튼을 제공하는 것이 좋습니다.
```

---

### [실무]

리뷰 코멘트 템플릿:

```text
[Priority] 문제 설명. 왜 문제인지 설명. 수정 방향 제안.
```

예:

```text
[Critical] 프론트엔드 코드에 OPENAI_API_KEY가 포함되어 있습니다. 브라우저 빌드 결과물에 노출될 수 있으므로 즉시 제거하고 백엔드 API를 통해 호출하도록 변경해야 합니다.
```

```text
[High] 로그인 API 실패 시 에러 메시지가 표시되지 않습니다. 사용자가 실패 원인을 알 수 있도록 Error State와 사용자 친화 메시지를 추가해야 합니다.
```

```text
[Medium] FestivalSearchPage가 검색 상태, API 호출, 결과 렌더링을 모두 처리하고 있습니다. 검색 로직은 custom hook으로 분리하면 테스트 가능성과 유지보수성이 좋아집니다.
```

```text
[Suggestion] 검색 조건을 URL query params로 관리하면 새로고침 유지와 공유가 쉬워집니다.
```

---

### [FAQ]

Q. 좋은 리뷰 코멘트는 어떻게 써야 해?
A. 우선순위, 문제, 이유, 수정 방향을 명확히 작성해야 한다.

Q. 비난하는 표현을 써도 돼?
A. 안 된다. 리뷰는 코드 품질 개선을 위한 것이며 사람을 비난하면 안 된다.

Q. 선택 개선 사항은 어떻게 표현해?
A. Suggestion으로 표시하고 필수 수정처럼 말하지 않는다.

Q. 리뷰 코멘트에 수정 방향이 꼭 있어야 해?
A. 권장된다. 문제만 지적하면 개발자가 다음 행동을 결정하기 어렵다.

---

# 5. PM Agent Collaboration Rules

## 5.1 PM Agent Review Usage

### [개념]

PM Agent는 Frontend Code Review 결과를 기능 완료 여부, 일정 판단, 배포 가능 여부 판단에 사용한다.

PM Agent는 코드 세부 구현보다 요구사항 충족, 사용자 흐름, 위험도, 수정 우선순위를 중점적으로 본다.

---

### [핵심]

PM Agent 판단 기준:

- 요구사항 충족 여부
- 주요 사용자 흐름 정상 여부
- Critical Issue 존재 여부
- High Issue 존재 여부
- 배포 가능 여부
- 일정 내 수정 가능성
- 사용자 시나리오 통과 여부
- Backend API 연동 상태
- 인증 / 권한 흐름 안정성
- Build / Deploy 위험도

PM Agent Output 예:

```text
Feature Status: Complete / Partial / Blocked
Risk Level: Low / Medium / High
Required Fixes: Critical / High 중심
Release Decision: Go / No-Go
```

---

### [실무]

PM Agent 판단 Flow:

```text
Review Result Read
→ Requirement Match Check
→ Critical / High Issue Check
→ User Scenario Check
→ Required Fix Scope Estimate
→ Release Decision
```

PM Agent는 다음 기준으로 판단한다.

```text
Critical Issue 있음
→ Feature Status: Blocked
→ Release Decision: No-Go

High Issue 있음
→ Feature Status: Partial
→ Release Decision: No-Go or Conditional Go

Medium 이하만 있음
→ Feature Status: Complete 또는 Partial
→ Release Decision: Go with Comments

Issue 없음
→ Feature Status: Complete
→ Release Decision: Go
```

---

### [FAQ]

Q. PM Agent는 코드 세부 구현까지 봐야 해?
A. 세부 구현 전체보다 요구사항 충족, 사용자 흐름, 위험도, 배포 가능성을 봐야 한다.

Q. Critical Issue가 있으면 PM Agent는 완료로 판단해도 돼?
A. 안 된다. Critical Issue가 있으면 Blocked 또는 No-Go로 판단해야 한다.

Q. High Issue가 있으면 무조건 배포 불가야?
A. 대부분 배포 전 수정이 필요하다. 단, 영향 범위가 제한적이면 조건부 판단이 가능하다.

Q. PM Agent는 Review Agent 결과를 그대로 따라야 해?
A. Review Agent 결과를 기반으로 일정, 범위, 사용자 영향도를 함께 고려해 최종 판단한다.

---

# 6. Frontend Agent Self Review Rules

## 6.1 Frontend Agent Self Review

### [개념]

Frontend Agent Self Review는 Frontend Agent가 코드 생성 후 스스로 1차 점검을 수행하는 규칙이다.

Frontend Agent가 생성한 코드는 반드시 Review Agent가 다시 독립 검토해야 한다.

---

### [핵심]

Frontend Agent Self Review Checklist:

```md
- [ ] 요구사항을 만족하는가?
- [ ] 주요 사용자 흐름이 동작하는가?
- [ ] 컴포넌트 책임이 과도하지 않은가?
- [ ] props / state 구조가 적절한가?
- [ ] Hook 규칙을 지키는가?
- [ ] API 요청이 중복되지 않는가?
- [ ] API 실패 처리가 있는가?
- [ ] loading / error / empty state가 있는가?
- [ ] form validation이 있는가?
- [ ] 인증 / 권한 흐름이 맞는가?
- [ ] 접근성 기본을 지켰는가?
- [ ] 반응형을 고려했는가?
- [ ] secret key가 노출되지 않는가?
- [ ] localhost 하드코딩이 없는가?
- [ ] build를 깨뜨리지 않는가?
```

---

### [실무]

Frontend Agent는 코드 생성 후 다음 정보를 함께 제공한다.

```text
Implemented Files
Review Notes
Known Limitations
Test Checklist
Build Check
```

Frontend Agent Output 예:

```md
## Implemented Files

- src/pages/FestivalSearchPage.jsx
- src/api/festivalApi.js

## Review Notes

- 검색 API 호출 분리 완료
- Loading / Error / Empty State 추가
- 검색 제출 중 disabled 처리 완료

## Known Limitations

- 서버 validation message 구조 확정 후 error mapping 보완 필요

## Test Checklist

- 검색어 입력 후 결과 표시
- 검색 결과 없음 표시
- API 실패 시 error 표시
- 제출 중 버튼 disabled 확인

## Build Check

- npm run build 확인 필요
```

---

### [FAQ]

Q. Frontend Agent가 self review를 하면 Review Agent가 필요 없어?
A. 아니다. Self Review는 1차 점검이고 Review Agent는 독립 검증 역할이다.

Q. Frontend Agent는 코드 생성 후 무엇을 함께 제공해야 해?
A. 구현 파일, 리뷰 메모, 알려진 제한사항, 테스트 체크리스트, 빌드 확인 여부를 제공하는 것이 좋다.

Q. Self Review에서 가장 중요한 항목은 뭐야?
A. 요구사항 충족, API 실패 처리, Loading / Error / Empty State, 인증, 빌드 가능성이다.

Q. Frontend Agent가 build 확인을 못 하면 어떻게 해야 해?
A. 확인하지 못한 사실을 명시하고 Review Agent 또는 사용자에게 build check를 요청해야 한다.

---

# 7. Common Review Mistakes

## 7.1 Reviewer Mistakes

### [개념]

Reviewer Mistakes는 Review Agent가 프론트엔드 코드 리뷰 중 자주 범하는 잘못된 판단이다.

이 문서는 Review Agent가 사소한 취향보다 사용자 흐름과 운영 위험을 우선하도록 제어한다.

---

### [핵심]

피해야 할 리뷰 방식:

- 취향 위주 리뷰
- 사소한 naming만 지적
- 요구사항 확인 없이 코드만 봄
- UI 동작 흐름 미검토
- API 실패 상황 미검토
- Loading / Error / Empty State 미검토
- 접근성 무시
- 보안 키 노출 무시
- 빌드 가능성 미확인
- 테스트 가능성 미검토
- 모든 문제를 같은 우선순위로 표시
- 수정 방향 없는 지적
- 과도한 리팩토링 요구
- 선택 개선을 필수 수정처럼 표현

---

### [실무]

좋은 리뷰 기준:

```text
Requirement First
→ Critical Risk First
→ User Flow
→ API / Auth Stability
→ UX State
→ Maintainability
→ Accessibility
→ Security
→ Build Risk
→ Suggestions Last
```

리뷰 금지 예:

```text
[Critical] 변수명이 마음에 들지 않습니다.
```

올바른 예:

```text
[Low] 변수명 data는 의미가 모호합니다. festivalList처럼 데이터 의미가 드러나는 이름을 사용하는 것이 좋습니다.
```

---

### [FAQ]

Q. 코드 리뷰에서 개인 취향을 말해도 돼?
A. 가능하지만 필수 수정처럼 말하면 안 된다. 취향성 의견은 Suggestion으로 분리해야 한다.

Q. 리팩토링을 많이 요구해도 돼?
A. 일정과 영향도를 고려해야 한다. Critical 기능 수정과 High 운영 위험이 우선이다.

Q. 모든 문제를 Critical로 표시해도 돼?
A. 안 된다. 우선순위가 무너지면 실제로 먼저 수정해야 할 문제가 흐려진다.

Q. 리뷰에서 가장 흔한 실수는 뭐야?
A. 요구사항과 사용자 흐름을 보지 않고 코드 스타일이나 naming만 지적하는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Frontend Code Review 문서는 왜 필요해?
A. Frontend Agent / Review Agent / PM Agent가 프론트엔드 코드 품질, 안정성, 유지보수성, 배포 가능성을 판단하기 위해 필요하다.

Q. 프론트엔드 코드 리뷰에서 가장 중요한 기준은 뭐야?
A. 요구사항 충족, 사용자 흐름, API 안정성, Error / Loading / Empty 처리, 인증, 접근성, 빌드 가능성이다.

Q. Frontend Code Review는 문법 검사야?
A. 아니다. 구조, 상태, API, UX, 인증, 접근성, 보안, 성능, 테스트 가능성을 함께 보는 리뷰다.

Q. Review Agent는 어떤 순서로 리뷰해야 해?
A. 요구사항 확인, Critical 위험 확인, 사용자 흐름, 컴포넌트 구조, 상태, API, UX 상태, 인증, 접근성, 보안, 빌드 검토 순서가 좋다.

Q. 코드 리뷰 우선순위는 어떻게 나눠?
A. Critical, High, Medium, Low, Suggestion으로 나눈다.

Q. Critical Issue는 뭐야?
A. 빌드 실패, 로그인 불가, 핵심 기능 미동작, Secret Key 노출처럼 즉시 수정이 필요한 문제다.

Q. High Issue는 뭐야?
A. API 실패 미처리, 인증 체크 누락, 주요 사용자 흐름 오류처럼 운영 위험이 큰 문제다.

Q. Medium Issue는 뭐야?
A. 컴포넌트 책임 과다, 중복 코드, Empty State 일부 누락처럼 유지보수성과 UX에 영향을 주는 문제다.

Q. Low Issue는 뭐야?
A. naming 애매함, 작은 스타일 불일치처럼 개선하면 좋지만 기능을 막지는 않는 문제다.

Q. Suggestion은 뭐야?
A. Custom Hook 분리, lazy loading 검토, Design Token 도입처럼 선택 개선 사항이다.

Q. Critical Issue가 있으면 Final Decision은 뭐야?
A. BLOCKED로 판단한다.

Q. High Issue가 있으면 Final Decision은 뭐야?
A. 일반적으로 CHANGES REQUESTED로 판단한다.

Q. Low와 Suggestion만 있으면 Final Decision은 뭐야?
A. APPROVED WITH COMMENTS로 판단할 수 있다.

Q. 문제가 없으면 Final Decision은 뭐야?
A. APPROVED로 판단한다.

Q. Review Result Format은 어떻게 구성해?
A. Summary, Critical Issues, High Priority Issues, Medium Priority Issues, Low Priority Issues, Suggestions, Checklist, Final Decision 구조가 좋다.

Q. Review Agent가 가장 먼저 찾아야 할 문제는 뭐야?
A. 빌드 실패, 보안 키 노출, 로그인 불가, API 실패 미처리, 핵심 사용자 흐름 중단이다.

Q. 좋은 리뷰 코멘트는 어떻게 작성해?
A. 우선순위, 문제, 이유, 수정 방향을 명확히 작성한다.

Q. 선택 개선 사항은 어떻게 표시해?
A. Suggestion으로 표시하고 필수 수정과 구분한다.

Q. PM Agent는 Frontend Code Review 결과를 어떻게 사용해?
A. 기능 완료 여부, 위험도, 배포 가능성, 수정 우선순위를 판단하는 데 사용한다.

Q. Frontend Agent Self Review는 왜 필요해?
A. 코드 생성 후 요구사항, API, UX 상태, 인증, 빌드 위험을 1차 점검하기 위해 필요하다.

Q. Self Review를 하면 Review Agent가 필요 없어?
A. 아니다. Self Review는 1차 점검이고 Review Agent는 독립 검증 역할이다.

Q. Reviewer Mistake는 뭐야?
A. 요구사항과 사용자 흐름을 보지 않고 취향, naming, 스타일만 지적하는 잘못된 리뷰 방식이다.

Q. 코드 리뷰에서 모든 문제를 Critical로 표시해도 돼?
A. 안 된다. 우선순위가 무너지면 실제 수정 순서를 판단하기 어렵다.

Q. Frontend Code Review의 최종 목적은 뭐야?
A. 프론트엔드 코드가 요구사항을 만족하고 안정적으로 배포 가능한지 Agent가 일관되게 판단하도록 하는 것이다.
