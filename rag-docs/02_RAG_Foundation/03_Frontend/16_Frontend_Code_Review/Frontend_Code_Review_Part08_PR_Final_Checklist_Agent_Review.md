# Frontend Code Review Part08 - PR Review, Common Issues, Final Checklist, and Agent Review

---

# 1. Pull Request Review Rules

## 1.1 PR Review Overview

### [개념]

Pull Request Review는 변경된 프론트엔드 코드가 요구사항을 만족하고, 병합 가능한 품질과 운영 안정성을 갖추었는지 검토하는 과정이다.

PR Review는 전체 코드를 처음부터 다시 읽는 작업이 아니다.

Review Agent는 변경 목적, 사용자 흐름, Critical / High 위험, 빌드 가능성, 배포 영향도를 우선 검토해야 한다.

---

### [핵심]

PR Review 핵심 기준:

- 변경 목적이 명확한가?
- 요구사항을 만족하는가?
- 주요 사용자 흐름이 동작하는가?
- 변경 범위가 과도하지 않은가?
- Critical Issue가 없는가?
- High Issue가 없는가?
- API 연동이 정상인가?
- Error / Loading / Empty State가 있는가?
- 인증 / 권한 흐름이 안전한가?
- 접근성 기본을 만족하는가?
- 보안 위험이 없는가?
- build가 깨지지 않는가?
- 테스트 가능성이 있는가?
- 리뷰 코멘트가 실행 가능한가?

---

### [실무]

PR Review Flow:

```text
PR Title / Description Read
→ Changed Files Overview
→ Requirement Match Check
→ User Flow Check
→ Critical Risk Scan
→ API / Auth / Form Review
→ UX State Review
→ Accessibility / Security Review
→ Build Deploy Risk Review
→ Testability Review
→ Final Decision
```

PR에서 가장 먼저 볼 파일:

```text
Route / Page Component
→ API Module
→ Auth / Store / Context
→ Form Component
→ Shared Component
→ Env / Config
→ Package Dependency
```

리뷰 코멘트 예:

```text
[High] PR 설명에는 검색 결과 없음 처리가 포함되어 있지만 실제 FestivalSearchPage에는 Empty State가 없습니다. 요구사항 누락이므로 검색 결과가 빈 배열일 때 안내 UI를 추가해야 합니다.
```

---

### [FAQ]

Q. PR Review는 전체 파일을 처음부터 끝까지 보면 돼?
A. 가능하지만 비효율적이다. 변경 목적과 사용자 흐름을 먼저 파악하고 위험도가 높은 파일부터 검토하는 것이 좋다.

Q. PR Review에서 가장 먼저 확인할 것은 뭐야?
A. 요구사항 충족, 핵심 사용자 흐름, Critical / High 위험, build 가능성이다.

Q. PR 설명이 없으면 어떻게 해?
A. 변경 파일과 코드 흐름을 기준으로 가능한 목적을 추정하되, 요구사항 누락 가능성을 Issue로 남긴다.

Q. PR Review는 코드 스타일 리뷰야?
A. 아니다. 코드 스타일보다 기능 안정성, 사용자 흐름, API, 인증, 보안, 빌드 위험이 우선이다.

---

## 1.2 PR Diff Review

### [개념]

PR Diff Review는 변경된 코드의 차이점을 기준으로 영향 범위와 위험도를 파악하는 과정이다.

Diff만 보면 전체 맥락을 놓칠 수 있고, 전체 파일만 보면 변경 의도를 놓칠 수 있다.

Review Agent는 diff와 관련 파일 맥락을 함께 확인해야 한다.

---

### [핵심]

PR Diff Review 검토 항목:

- 변경된 파일이 요구사항과 일치하는가?
- 변경 범위가 과도하지 않은가?
- 핵심 사용자 흐름에 영향을 주는가?
- 공통 컴포넌트 변경이 다른 화면에 영향을 주는가?
- API module 변경이 여러 페이지에 영향을 주는가?
- auth context 변경이 전체 앱에 영향을 주는가?
- route 변경이 기존 링크를 깨뜨리지 않는가?
- env / config 변경이 배포에 영향을 주는가?
- package dependency 변경이 bundle과 build에 영향을 주는가?
- 삭제된 코드가 다른 파일에서 참조되지 않는가?

---

### [실무]

Diff 영향도 판단:

```text
Page Component 변경
→ 해당 페이지 사용자 흐름 검토

Shared Component 변경
→ 사용하는 모든 화면 영향 검토

API Module 변경
→ endpoint / response mapping / error handling 검토

Auth Store 변경
→ login / logout / protected route / 401 처리 검토

Route 변경
→ navigation / direct URL / NotFound / fallback 검토

Env 변경
→ build / deploy / secret exposure 검토

Package 변경
→ bundle size / breaking change / build 확인
```

리뷰 코멘트 예:

```text
[Medium] 공통 Button 컴포넌트의 disabled 스타일이 변경되었습니다. 저장, 로그인, 리뷰 작성 등 중복 제출 방지 버튼에 영향을 줄 수 있으므로 주요 form 화면에서 동작 확인이 필요합니다.
```

---

### [FAQ]

Q. Diff만 보면 충분해?
A. 아니다. diff는 변경 지점을 보여주지만 관련 사용자 흐름과 사용처 맥락도 함께 봐야 한다.

Q. 공통 컴포넌트 변경은 왜 위험해?
A. 여러 화면에 영향을 주므로 작은 변경도 예상보다 넓은 회귀 버그를 만들 수 있다.

Q. package.json 변경도 리뷰해야 해?
A. 해야 한다. dependency 추가는 bundle size, 보안, build 실패 가능성과 연결된다.

Q. 삭제된 코드는 어떻게 리뷰해?
A. 다른 파일에서 참조 중인지, route나 import가 깨지지 않는지 확인해야 한다.

---

## 1.3 PR Checklist Review

### [개념]

PR Checklist Review는 PR이 병합 가능한 상태인지 빠르게 판단하기 위한 표준 점검 목록이다.

Review Agent는 변경 범위에 따라 체크리스트를 선택 적용하되, Critical / High 위험 항목은 항상 확인해야 한다.

---

### [핵심]

PR Review Checklist:

```md
## Requirement

- [ ] 요구사항을 만족하는가?
- [ ] 주요 사용자 흐름이 동작하는가?
- [ ] 성공 / 실패 / 빈 상태가 모두 처리되는가?

## Component

- [ ] 컴포넌트 책임이 명확한가?
- [ ] 컴포넌트 이름이 역할을 표현하는가?
- [ ] props / state 구조가 적절한가?
- [ ] UI와 비즈니스 로직이 과하게 섞이지 않았는가?

## API

- [ ] API 호출이 module로 분리되어 있는가?
- [ ] endpoint가 backend 명세와 일치하는가?
- [ ] response mapping이 정확한가?
- [ ] API error handling이 있는가?
- [ ] 중복 요청 위험이 없는가?

## UX State

- [ ] Loading State가 있는가?
- [ ] Error State가 있는가?
- [ ] Empty State가 있는가?
- [ ] 중복 제출이 방지되는가?

## Form

- [ ] form 구조가 적절한가?
- [ ] label이 연결되어 있는가?
- [ ] validation이 있는가?
- [ ] 서버 validation error를 표시하는가?
- [ ] submit 중 disabled 처리가 있는가?

## Auth / Routing

- [ ] 로그인 / 로그아웃 흐름이 맞는가?
- [ ] token 노출 위험이 없는가?
- [ ] Protected Route가 있는가?
- [ ] 401 / 403 처리가 있는가?
- [ ] NotFound route가 있는가?
- [ ] route param 처리가 안전한가?

## Accessibility / Styling

- [ ] semantic HTML을 사용하는가?
- [ ] keyboard navigation이 가능한가?
- [ ] focus-visible이 있는가?
- [ ] image alt가 있는가?
- [ ] 반응형이 깨지지 않는가?

## Security

- [ ] secret key가 노출되지 않는가?
- [ ] token console 출력이 없는가?
- [ ] dangerouslySetInnerHTML 사용이 안전한가?
- [ ] 외부 링크 rel 설정이 있는가?
- [ ] UI 권한 제한만으로 보안을 대체하지 않는가?

## Build / Test

- [ ] npm run build 또는 yarn build가 성공하는가?
- [ ] localhost 하드코딩이 없는가?
- [ ] 환경 변수가 올바른가?
- [ ] 파일명 대소문자 문제가 없는가?
- [ ] 테스트 가능한 구조인가?
```

---

### [실무]

PR Checklist 적용 우선순위:

```text
Critical / High Risk
→ Requirement
→ User Flow
→ API / Auth / Form
→ UX State
→ Security
→ Build
→ Maintainability
→ Suggestions
```

PR이 작아도 반드시 확인할 항목:

```text
build 가능성
secret 노출
API URL localhost
token console 출력
사용자 흐름 차단
에러 처리 누락
```

---

### [FAQ]

Q. PR Checklist를 매번 전부 써야 해?
A. 변경 범위에 따라 선택 적용할 수 있다. 다만 Critical / High 위험 항목은 항상 확인해야 한다.

Q. 작은 PR도 build 위험을 봐야 해?
A. 봐야 한다. 작은 import 경로 변경도 Linux 배포에서 build 실패를 만들 수 있다.

Q. Checklist에서 가장 중요한 영역은 뭐야?
A. 요구사항, 사용자 흐름, API, 인증, 보안, 빌드 가능성이다.

Q. PR Checklist는 PM Agent도 사용해?
A. 사용할 수 있다. PM Agent는 기능 완료와 배포 가능성을 판단할 때 checklist 결과를 참고한다.

---

## 1.4 Review Comment Quality Rules

### [개념]

Review Comment Quality Rules는 코드 리뷰 코멘트가 명확하고 실행 가능하며 우선순위가 구분되도록 작성하는 규칙이다.

리뷰 코멘트는 개발자를 비난하는 문장이 아니라 문제와 수정 방향을 전달하는 작업 지시이다.

---

### [핵심]

좋은 리뷰 코멘트 조건:

- 우선순위가 있다.
- 문제 위치가 명확하다.
- 왜 문제인지 설명한다.
- 수정 방향을 제안한다.
- 필수 수정과 선택 개선을 구분한다.
- 사용자 영향 또는 운영 위험을 설명한다.
- 비난 표현을 사용하지 않는다.
- 과도한 리팩토링을 강요하지 않는다.

나쁜 코멘트:

```text
이거 이상함.
```

좋은 코멘트:

```text
[High] 로그인 실패 시 사용자에게 에러 메시지가 표시되지 않습니다. 사용자가 실패 원인을 알 수 있도록 Error State와 사용자 친화 메시지를 추가해야 합니다.
```

---

### [실무]

리뷰 코멘트 템플릿:

```text
[Priority] 문제 설명. 사용자 영향 또는 위험 설명. 수정 방향 제안.
```

예시:

```text
[Critical] 프론트엔드 환경 변수에 OPENAI_API_KEY가 포함되어 있습니다. 브라우저 번들에 노출될 수 있으므로 즉시 제거하고 백엔드 API를 통해 호출하도록 변경해야 합니다.
```

```text
[High] 저장 요청 실패 시 loading이 종료되지 않아 사용자가 무한 로딩 상태를 보게 됩니다. try / catch / finally 구조로 성공과 실패 모두 setIsSubmitting(false)가 실행되도록 수정해야 합니다.
```

```text
[Medium] FestivalDetailPage가 API 호출, Modal 상태, 리뷰 Form 제출을 모두 담당하고 있습니다. 데이터 조회와 리뷰 작성 로직을 custom hook 또는 하위 컴포넌트로 분리하면 유지보수성이 좋아집니다.
```

```text
[Suggestion] 검색 조건을 URL query params로 관리하면 새로고침 유지와 링크 공유가 쉬워집니다.
```

---

### [FAQ]

Q. 좋은 리뷰 코멘트는 어떻게 써?
A. 우선순위, 문제, 영향, 수정 방향을 명확히 작성한다.

Q. 선택 개선도 리뷰 코멘트로 남겨도 돼?
A. 가능하다. 다만 Suggestion으로 표시해 필수 수정과 구분해야 한다.

Q. 비난하는 표현을 써도 돼?
A. 안 된다. 리뷰는 코드 품질 개선을 위한 것이며 사람을 비난하면 안 된다.

Q. 수정 방향 없이 문제만 말해도 돼?
A. 가능은 하지만 권장하지 않는다. 실행 가능한 수정 방향이 있어야 개발자가 빠르게 대응할 수 있다.

---

# 2. Common Frontend Review Issues

## 2.1 Frequent Critical Issues

### [개념]

Frequent Critical Issues는 프론트엔드 코드 리뷰에서 즉시 병합 또는 배포를 차단해야 하는 반복 문제이다.

Critical Issue는 서비스 장애, 보안 사고, 핵심 기능 실패와 직접 연결된다.

---

### [핵심]

자주 발생하는 Critical Issue:

- `npm run build` 실패
- 핵심 페이지 흰 화면
- 로그인 불가
- 회원가입 불가
- Secret Key 프론트엔드 노출
- Access Token URL query string 노출
- 결제 Secret Key 노출
- 운영 API URL 완전 오연결
- 핵심 API response mapping 오류
- 조건부 Hook 호출로 앱 런타임 오류 발생
- import path 대소문자 오류로 Linux build 실패
- SPA fallback 누락으로 핵심 페이지 직접 접근 불가
- 필수 환경 변수 누락으로 앱 실행 불가

---

### [실무]

Critical Issue 판단 Flow:

```text
Does It Block Build?
→ Does It Break Main User Flow?
→ Does It Expose Secret?
→ Does It Cause Runtime White Screen?
→ Does It Break Production Access?
→ Critical
```

Critical 리뷰 코멘트 예:

```text
[Critical] VITE_OPENAI_API_KEY가 프론트엔드 환경 변수에 포함되어 있습니다. 브라우저 번들에 노출될 수 있으므로 즉시 제거하고 키 폐기 또는 재발급을 검토해야 합니다.
```

```text
[Critical] useEffect가 조건문 내부에서 호출되고 있어 Hook 호출 순서가 렌더링마다 달라질 수 있습니다. Hook은 최상위에서 호출하고 내부에서 조건을 처리해야 합니다.
```

---

### [FAQ]

Q. Critical Issue는 언제 붙여?
A. build 실패, secret 노출, 핵심 기능 미동작, 런타임 흰 화면, 운영 접근 불가에 붙인다.

Q. Critical Issue가 있으면 APPROVED 가능해?
A. 불가능하다. BLOCKED 또는 CHANGES REQUESTED로 판단해야 한다.

Q. Secret Key 노출은 왜 Critical이야?
A. 브라우저 코드와 빌드 결과물은 사용자에게 노출될 수 있기 때문이다.

Q. import path 대소문자 문제도 Critical이 될 수 있어?
A. Linux 배포에서 build 실패를 만들면 Critical로 판단할 수 있다.

---

## 2.2 Frequent High Issues

### [개념]

Frequent High Issues는 서비스 전체를 즉시 중단하지는 않지만 주요 사용자 흐름, 운영 안정성, 인증, API 연동에 큰 위험을 만드는 반복 문제이다.

High Issue는 일반적으로 배포 전 수정해야 한다.

---

### [핵심]

자주 발생하는 High Issue:

- API 실패 시 catch 처리 없음
- Error State 없음
- Loading 종료 누락
- Form 중복 제출 가능
- 인증 header 누락
- 401 처리 누락
- Protected Route 누락
- logout 시 token 미삭제
- token console 출력
- 서버 validation error 미표시
- API endpoint와 backend 명세 불일치
- response.data.data mapping 오류
- route param dependency 누락
- 삭제 / 저장 버튼 권한 제한 누락
- sanitize 없는 사용자 입력 HTML 렌더링
- 파일 업로드 확장자 / 크기 검증 없음
- 더보기 / 무한 스크롤 중복 요청 가능
- 운영 API baseURL localhost 잔존

---

### [실무]

High Issue 판단 Flow:

```text
Does It Break Key User Flow?
→ Does It Hide API Failure?
→ Does It Risk Duplicate Write?
→ Does It Break Auth / Permission?
→ Does It Create Security Risk?
→ High
```

High 리뷰 코멘트 예:

```text
[High] 회원가입 실패 시 서버 validation error가 표시되지 않아 사용자가 어떤 입력을 수정해야 하는지 알 수 없습니다. field별 error mapping을 추가해야 합니다.
```

```text
[High] 운영 API baseURL이 http://localhost:8080으로 남아 있습니다. 운영 사용자의 브라우저에서 localhost는 사용자 자신의 컴퓨터를 의미하므로 환경 변수로 분리해야 합니다.
```

---

### [FAQ]

Q. High Issue는 언제 붙여?
A. 주요 사용자 흐름 오류, API 실패 미처리, 인증 누락, 중복 저장 위험, 보안 위험에 붙인다.

Q. High Issue가 있으면 배포 가능해?
A. 일반적으로 배포 전 수정이 필요하다. 영향 범위가 제한적이면 조건부 판단이 가능하다.

Q. API 실패 처리 없음은 왜 High야?
A. 사용자가 실패 원인을 알 수 없고 복구할 수 없어 운영 장애처럼 보일 수 있기 때문이다.

Q. 운영 localhost 잔존은 왜 High야?
A. 운영 사용자의 브라우저에서 localhost는 사용자 자신의 컴퓨터를 의미해 API 연결이 실패하기 때문이다.

---

## 2.3 Frequent Medium Issues

### [개념]

Frequent Medium Issues는 즉시 장애를 만들 가능성은 낮지만 유지보수성, UX, 테스트 가능성, 접근성에 영향을 주는 반복 문제이다.

Medium Issue는 일정과 영향도에 따라 수정 우선순위를 정한다.

---

### [핵심]

자주 발생하는 Medium Issue:

- 컴포넌트 책임 과다
- Page Component 비대화
- props drilling 과다
- state 중복 저장
- derived state를 useEffect로 동기화
- Empty State 누락
- form label 누락
- modal focus 관리 누락
- image alt 부적절
- 모바일 layout 일부 깨짐
- index key 사용
- API module 미분리
- validation 로직 컴포넌트 내부 집중
- custom hook 반환 setter 과다 노출
- 타입 any 남용
- API response type 부정확
- 테스트 mock 어려운 구조
- error.response.status 직접 접근

---

### [실무]

Medium Issue 판단 Flow:

```text
Does It Hurt Maintainability?
→ Does It Reduce UX Clarity?
→ Does It Reduce Accessibility?
→ Does It Make Testing Hard?
→ Does It Increase Change Risk?
→ Medium
```

Medium 리뷰 코멘트 예:

```text
[Medium] FestivalSearchPage가 검색 상태, API 호출, 결과 렌더링, pagination을 모두 담당하고 있습니다. 검색 로직과 목록 렌더링을 분리하면 유지보수성과 테스트 가능성이 좋아집니다.
```

```text
[Medium] 검색 결과가 빈 배열일 때 아무 안내가 표시되지 않습니다. Empty State를 추가해 결과가 없음을 명확히 알려야 합니다.
```

---

### [FAQ]

Q. Medium Issue는 반드시 수정해야 해?
A. 반드시 즉시 수정해야 하는 것은 아니지만 유지보수성, UX, 테스트 가능성에 영향을 주므로 일정에 따라 처리한다.

Q. Empty State 누락은 왜 Medium이야?
A. 사용자가 오류인지 데이터 없음인지 구분할 수 없어 UX가 나빠지기 때문이다.

Q. 컴포넌트 책임 과다는 왜 Medium이야?
A. 변경 영향도와 테스트 난이도를 높여 유지보수 비용을 증가시키기 때문이다.

Q. any 남용은 항상 Medium이야?
A. 핵심 데이터 흐름에서 타입 오류를 숨기면 Medium 이상으로 판단할 수 있다.

---

## 2.4 Frequent Low and Suggestion Issues

### [개념]

Frequent Low and Suggestion Issues는 기능 안정성을 즉시 해치지는 않지만 코드 품질, 일관성, 향후 확장성 개선에 도움이 되는 반복 항목이다.

Review Agent는 Low와 Suggestion을 필수 수정처럼 표현하지 않아야 한다.

---

### [핵심]

자주 발생하는 Low Issue:

- 변수명 의미 부족
- className naming 불일치
- 작은 spacing 불일치
- 사용하지 않는 주석 일부 잔존
- 불필요한 useCallback
- event type any
- 중복 CSS 일부 존재
- import 정렬 불일치
- 작은 UI copy 불일치

자주 발생하는 Suggestion:

- Custom Hook 분리 제안
- React Query 도입 검토
- URL query params 적용 검토
- route-based lazy loading 검토
- Design Token 도입 검토
- 공통 Button Component 추출 제안
- Storybook 도입 검토
- 테스트 커버리지 확대 제안
- Error Boundary 도입 검토
- Skeleton UI 적용 검토

---

### [실무]

Low 리뷰 코멘트 예:

```text
[Low] isData 변수명은 의미가 모호합니다. hasFestivalData처럼 true / false 의미가 드러나는 이름이 더 명확합니다.
```

Suggestion 리뷰 코멘트 예:

```text
[Suggestion] 검색 조건을 URL query params로 관리하면 새로고침 유지, 뒤로가기, 링크 공유가 쉬워집니다.
```

주의:

```text
Suggestion을 Required Fixes에 넣지 않는다.
Low Issue를 Critical처럼 표현하지 않는다.
취향성 의견은 Suggestion으로 분리한다.
```

---

### [FAQ]

Q. Low Issue는 반드시 수정해야 해?
A. 아니다. 개선 권장 사항이며 Critical / High보다 우선하지 않는다.

Q. Suggestion은 필수 수정이야?
A. 아니다. 선택 개선 사항이다.

Q. 취향성 리뷰는 어떻게 남겨?
A. Suggestion으로 표시하고 필수 수정처럼 말하지 않는다.

Q. Low와 Suggestion을 왜 구분해?
A. Low는 작은 품질 문제이고 Suggestion은 선택적 구조 개선이나 확장 제안이기 때문이다.

---

# 3. Final Review Result Rules

## 3.1 Final Review Output Format

### [개념]

Final Review Output Format은 Review Agent가 프론트엔드 코드 리뷰 결과를 일관되게 출력하기 위한 최종 형식이다.

이 형식은 PM Agent가 기능 완료, 수정 필요, 배포 가능 여부를 빠르게 판단하도록 설계한다.

---

### [핵심]

표준 출력 구조:

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

섹션별 목적:

| Section                | Purpose                 |
| ---------------------- | ----------------------- |
| Summary                | 전체 리뷰 요약          |
| Critical Issues        | 즉시 차단 문제          |
| High Priority Issues   | 주요 운영 위험          |
| Medium Priority Issues | 유지보수 / UX 문제      |
| Low Priority Issues    | 작은 개선 사항          |
| Suggestions            | 선택 개선               |
| Checklist              | 검토 완료 항목          |
| Final Decision         | 승인 / 수정 / 차단 판단 |

---

### [실무]

문제가 없는 섹션 처리:

```md
## Critical Issues

None

## High Priority Issues

None
```

Final Decision 예:

```text
APPROVED
APPROVED WITH COMMENTS
CHANGES REQUESTED
BLOCKED
```

Final Decision은 반드시 포함한다.

리뷰 결과 예:

```md
## Final Decision

CHANGES REQUESTED

## Reason

- [High] API 실패 시 Error State가 없습니다.
- [High] Form 중복 제출이 가능합니다.

## Required Fixes

1. API catch 처리 및 사용자 에러 메시지 추가
2. isSubmitting guard와 submit button disabled 처리 추가
```

---

### [FAQ]

Q. Final Review Output Format은 왜 필요해?
A. 리뷰 결과를 일관되게 출력해야 PM Agent와 개발자가 빠르게 판단할 수 있기 때문이다.

Q. 문제가 없는 섹션은 생략해도 돼?
A. 가능하지만 Agent 출력 일관성을 위해 None으로 명시하는 것이 좋다.

Q. Final Decision은 반드시 필요해?
A. 필요하다. 병합, 수정, 배포 여부를 판단하는 핵심 결과다.

Q. Required Fixes에는 무엇을 넣어?
A. Critical / High 중심의 필수 수정 항목을 넣는다. Suggestion은 별도로 분리한다.

---

## 3.2 Final Decision Rules

### [개념]

Final Decision Rules는 Review Agent가 이슈 우선순위를 기반으로 승인, 코멘트 승인, 수정 요청, 차단을 판단하는 규칙이다.

Final Decision은 리뷰 코멘트의 단순 요약이 아니라 다음 작업 진행 여부를 결정하는 기준이다.

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

Final Decision Flow:

```text
Critical Issue Exists?
→ Yes
→ BLOCKED

High Issue Exists?
→ Yes
→ CHANGES REQUESTED

Medium Issue Blocks Requirement Or Main User Flow?
→ Yes
→ CHANGES REQUESTED

Only Medium Maintainability / UX Issues?
→ APPROVED WITH COMMENTS or CHANGES REQUESTED by impact

Only Low / Suggestion?
→ APPROVED WITH COMMENTS

No Meaningful Issue?
→ APPROVED
```

판단 예:

```text
build 실패
→ BLOCKED

Secret Key 노출
→ BLOCKED

API 실패 처리 없음
→ CHANGES REQUESTED

요구사항에 포함된 Empty State 누락
→ CHANGES REQUESTED

선택적 Empty State CTA 개선
→ APPROVED WITH COMMENTS

naming 개선만 있음
→ APPROVED WITH COMMENTS
```

---

### [FAQ]

Q. Critical Issue가 있으면 Final Decision은 뭐야?
A. BLOCKED다.

Q. High Issue가 있으면 Final Decision은 뭐야?
A. 일반적으로 CHANGES REQUESTED다.

Q. Medium Issue만 있으면 어떻게 판단해?
A. 사용자 흐름 영향이 크면 CHANGES REQUESTED, 경미하면 APPROVED WITH COMMENTS로 판단할 수 있다.

Q. Low와 Suggestion만 있으면 승인 가능해?
A. 가능하다. APPROVED WITH COMMENTS가 적절하다.

---

## 3.3 Required Fixes Rules

### [개념]

Required Fixes Rules는 리뷰 결과에서 반드시 수정해야 하는 항목을 명확히 구분하는 규칙이다.

Required Fixes는 Critical / High Issue 중심으로 구성한다.

Medium 이하 항목은 영향도에 따라 포함 여부를 결정한다.

---

### [핵심]

Required Fixes에 포함할 항목:

- Critical Issue
- High Issue
- 핵심 요구사항 누락
- 핵심 사용자 흐름 차단
- build 실패
- secret 노출
- 인증 / 권한 실패
- API 실패 처리 누락
- 중복 저장 / 중복 결제 위험
- 운영 배포 실패 위험

Required Fixes에 일반적으로 넣지 않는 항목:

- 단순 naming 개선
- 취향성 구조 변경
- 선택적 custom hook 분리
- route lazy loading 제안
- 디자인 토큰 도입 제안
- 테스트 커버리지 확대 제안
- 작은 spacing 불일치

---

### [실무]

Required Fixes 예:

```md
## Required Fixes

1. 프론트엔드 환경 변수에서 TOSS_SECRET_KEY 제거
2. 로그인 실패 시 Error State 추가
3. 회원가입 submit 중 중복 제출 방지
4. 운영 API baseURL을 환경 변수로 분리
```

Suggestions 예:

```md
## Suggestions

- 검색 조건을 URL query params로 관리하면 공유와 새로고침 유지가 쉬워집니다.
- FestivalDetailPage의 리뷰 작성 로직을 custom hook으로 분리하면 유지보수성이 좋아집니다.
```

리뷰 코멘트 예:

```text
[High] 필수 수정 항목과 선택 개선 항목이 섞여 있습니다. Required Fixes에는 배포 전 수정이 필요한 Critical / High 문제만 포함하고, 구조 개선 제안은 Suggestions로 분리하는 것이 좋습니다.
```

---

### [FAQ]

Q. Required Fixes에는 무엇을 넣어야 해?
A. Critical / High Issue와 핵심 요구사항 누락처럼 배포 전 반드시 수정해야 하는 항목을 넣는다.

Q. Suggestion도 Required Fixes에 넣어도 돼?
A. 권장하지 않는다. 선택 개선은 Suggestions로 분리해야 수정 우선순위가 명확해진다.

Q. Medium Issue는 Required Fixes에 넣을 수 있어?
A. 사용자 흐름이나 요구사항에 중요한 영향을 주면 넣을 수 있다.

Q. Required Fixes가 많으면 어떻게 해야 해?
A. Critical / High 우선으로 정렬하고, Medium 이하 항목은 영향도에 따라 분리한다.

---

# 4. Agent Collaboration Review Rules

## 4.1 Frontend Agent Self Review Output

### [개념]

Frontend Agent Self Review Output은 Frontend Agent가 코드 생성 후 스스로 1차 검토 결과를 제공하는 표준 형식이다.

Self Review는 Review Agent 검토를 대체하지 않는다.

Frontend Agent는 구현 파일, 변경 내용, 제한사항, 테스트 체크리스트, 빌드 확인 여부를 명시해야 한다.

---

### [핵심]

Frontend Agent Self Review Output:

```md
## Implemented Files

## Implementation Summary

## Self Review Notes

## Known Limitations

## Test Checklist

## Build Check
```

필수 포함:

- 구현 / 수정 파일
- 요구사항 충족 요약
- API 연동 여부
- Loading / Error / Empty 처리 여부
- 인증 / 권한 처리 여부
- 알려진 제한사항
- 수동 테스트 항목
- build 확인 여부

---

### [실무]

출력 예:

```md
## Implemented Files

- src/pages/FestivalSearchPage.jsx
- src/components/festival/FestivalSearchForm.jsx
- src/api/festivalApi.js

## Implementation Summary

- 축제 검색 input, submit, 결과 목록 구현
- 검색 API module 분리
- Loading / Error / Empty State 추가

## Self Review Notes

- 검색 submit 중 중복 요청 방지 적용
- API 실패 시 사용자 메시지 표시
- 검색 결과 없음 안내 추가

## Known Limitations

- 서버 validation error 구조 확정 후 field mapping 보완 필요

## Test Checklist

- 검색어 입력 후 결과 표시
- 검색 결과 없음 표시
- API 실패 시 error 표시
- submit 중 버튼 disabled 확인

## Build Check

- npm run build 확인 필요
```

---

### [FAQ]

Q. Frontend Agent Self Review는 왜 필요해?
A. 코드 생성 Agent가 1차 품질 점검을 수행하고 Review Agent가 빠르게 검토할 수 있도록 하기 위해 필요하다.

Q. Self Review가 있으면 Review Agent가 필요 없어?
A. 아니다. Self Review는 1차 점검이고 Review Agent는 독립 검증 역할이다.

Q. Build Check를 못 했으면 어떻게 써?
A. 확인하지 못했다고 명시해야 한다. 확인하지 않은 build 성공을 주장하면 안 된다.

Q. Known Limitations는 왜 필요해?
A. 미완성 영역과 후속 검토 필요 사항을 명확히 분리하기 위해 필요하다.

---

## 4.2 Review Agent Final Output

### [개념]

Review Agent Final Output은 Review Agent가 프론트엔드 코드 검토 후 PM Agent와 개발자가 사용할 수 있는 최종 판단을 제공하는 형식이다.

Review Agent는 문제를 찾는 것에서 끝나지 않고 우선순위, 필수 수정, 최종 결정을 제공해야 한다.

---

### [핵심]

Review Agent Final Output:

```md
# Frontend Code Review Result

## Summary

## Critical Issues

## High Priority Issues

## Medium Priority Issues

## Low Priority Issues

## Suggestions

## Required Fixes

## Checklist

## Final Decision
```

Final Output 필수 기준:

- Critical / High 문제 우선
- 필수 수정과 선택 개선 분리
- Final Decision 명시
- 불확실한 항목은 가정으로 표시
- 확인하지 못한 build / test는 확인하지 못했다고 명시
- 비난 없는 코멘트
- 수정 방향 제시

---

### [실무]

Review Agent Output 예:

```md
# Frontend Code Review Result

## Summary

검색 기능의 기본 UI와 API 호출은 구현되어 있으나 API 실패 처리와 중복 제출 방지가 누락되어 수정이 필요합니다.

## Critical Issues

None

## High Priority Issues

- [High] API 실패 시 Error State가 표시되지 않습니다.
- [High] 검색 submit 중 버튼 disabled 처리가 없어 중복 요청이 발생할 수 있습니다.

## Medium Priority Issues

- [Medium] 검색 결과가 빈 배열일 때 Empty State가 없습니다.

## Suggestions

- 검색 조건을 URL query params로 관리하면 새로고침 유지와 공유가 쉬워집니다.

## Required Fixes

1. API catch 처리와 사용자 에러 메시지 추가
2. isSubmitting guard와 submit button disabled 처리 추가

## Final Decision

CHANGES REQUESTED
```

---

### [FAQ]

Q. Review Agent Final Output에는 무엇이 꼭 있어야 해?
A. Summary, priority별 issues, Required Fixes, Final Decision이 필요하다.

Q. 확인하지 못한 build를 성공했다고 써도 돼?
A. 안 된다. 확인하지 못했으면 확인하지 못했다고 명시해야 한다.

Q. 불확실한 내용은 어떻게 써?
A. 가정을 명시하고 확인 필요 항목으로 분리해야 한다.

Q. Review Agent의 핵심 역할은 뭐야?
A. 코드 품질과 운영 위험을 독립적으로 검토하고 승인 여부를 결정하는 것이다.

---

## 4.3 PM Agent Review Decision Usage

### [개념]

PM Agent Review Decision Usage는 PM Agent가 Frontend Code Review 결과를 기능 완료, 일정 조정, 배포 가능 여부 판단에 사용하는 규칙이다.

PM Agent는 코드 세부 구현보다 요구사항 충족, 위험도, 필수 수정 범위, 배포 가능성을 판단한다.

---

### [핵심]

PM Agent 판단 기준:

- 요구사항 충족 여부
- 주요 사용자 시나리오 통과 여부
- Critical Issue 존재 여부
- High Issue 존재 여부
- Required Fixes 규모
- 일정 내 수정 가능성
- 배포 가능 여부
- Backend API 연동 상태
- 인증 / 권한 흐름 안정성
- build / deploy 위험도

PM Agent Output:

```text
Feature Status: Complete / Partial / Blocked
Risk Level: Low / Medium / High
Required Fixes: Critical / High 중심
Release Decision: Go / Conditional Go / No-Go
```

---

### [실무]

PM Agent 판단 Flow:

```text
Review Result Read
→ Requirement Match Check
→ Critical / High Issue Check
→ Required Fixes Scope Check
→ User Scenario Risk Check
→ Schedule Impact Check
→ Release Decision
```

판단 기준:

```text
Final Decision: BLOCKED
→ Feature Status: Blocked
→ Release Decision: No-Go

Final Decision: CHANGES REQUESTED
→ Feature Status: Partial
→ Release Decision: No-Go or Conditional Go

Final Decision: APPROVED WITH COMMENTS
→ Feature Status: Complete
→ Release Decision: Go with Comments

Final Decision: APPROVED
→ Feature Status: Complete
→ Release Decision: Go
```

---

### [FAQ]

Q. PM Agent는 코드 세부 구현을 봐야 해?
A. 세부 구현 전체보다 요구사항 충족, 위험도, 배포 가능성, 수정 우선순위를 봐야 한다.

Q. Critical Issue가 있으면 PM Agent는 어떻게 판단해?
A. Blocked 또는 No-Go로 판단해야 한다.

Q. High Issue가 있으면 완료로 볼 수 있어?
A. 일반적으로 Partial 또는 Changes Requested로 판단한다.

Q. PM Agent는 Review Agent 결과를 그대로 따르면 돼?
A. Review Agent 결과를 기반으로 일정, 범위, 사용자 영향도를 함께 고려해 최종 판단한다.

---

# 5. Final Frontend Code Review Checklist

## 5.1 Full Frontend Review Checklist

### [개념]

Full Frontend Review Checklist는 Frontend Code Review 전체 영역을 통합한 최종 점검 목록이다.

Review Agent는 변경 범위에 따라 선택 적용하되, Critical / High 위험 항목은 항상 확인해야 한다.

---

### [핵심]

Full Frontend Review Checklist:

```md
## Requirement

- [ ] 요구사항을 만족하는가?
- [ ] 주요 사용자 흐름이 끊기지 않는가?
- [ ] 성공 / 실패 / 빈 상태가 모두 처리되는가?
- [ ] 권한별 동작이 요구사항과 일치하는가?

## Component

- [ ] 컴포넌트 책임이 명확한가?
- [ ] 컴포넌트 이름이 역할을 표현하는가?
- [ ] Page Component가 과도하게 비대하지 않은가?
- [ ] props가 과도하지 않은가?
- [ ] props drilling이 과하지 않은가?
- [ ] optional props 기본값이 있는가?
- [ ] 조건부 렌더링이 안전한가?

## State

- [ ] state 위치가 적절한가?
- [ ] local / global / URL / server state 구분이 맞는가?
- [ ] 중복 state가 없는가?
- [ ] derived state를 불필요하게 저장하지 않는가?
- [ ] 배열 / 객체 state를 직접 수정하지 않는가?
- [ ] 이전 state 기반 업데이트에 함수형 업데이트를 사용하는가?

## Hooks

- [ ] Hook 호출 규칙을 지키는가?
- [ ] 조건문 / 반복문 안에서 Hook을 호출하지 않는가?
- [ ] useEffect dependency가 적절한가?
- [ ] useEffect가 단순 계산에 남용되지 않는가?
- [ ] cleanup이 필요한 effect에 cleanup이 있는가?
- [ ] custom hook 책임이 명확한가?
- [ ] memoization을 남용하지 않는가?

## API

- [ ] API module이 분리되어 있는가?
- [ ] Axios instance 또는 fetch wrapper가 있는가?
- [ ] baseURL이 환경 변수로 관리되는가?
- [ ] endpoint가 backend 명세와 일치하는가?
- [ ] response mapping이 정확한가?
- [ ] API 실패 처리가 있는가?
- [ ] status별 error handling이 있는가?
- [ ] 네트워크 실패와 timeout을 처리하는가?
- [ ] 중복 요청 위험이 없는가?

## UX State

- [ ] Loading State가 있는가?
- [ ] Error State가 있는가?
- [ ] Empty State가 있는가?
- [ ] Error Recovery가 있는가?
- [ ] 제출 중 disabled 처리가 있는가?
- [ ] Partial Loading이 필요한 곳에 적용되어 있는가?

## Form

- [ ] form 태그와 onSubmit을 사용하는가?
- [ ] input label이 연결되어 있는가?
- [ ] button type이 명시되어 있는가?
- [ ] controlled input이 안전한가?
- [ ] validation이 있는가?
- [ ] 서버 validation error를 표시하는가?
- [ ] 중복 제출이 방지되는가?
- [ ] 파일 업로드 검증이 있는가?

## Auth

- [ ] 로그인 흐름이 완성되어 있는가?
- [ ] 로그아웃 처리가 완전한가?
- [ ] token 저장 방식이 요구사항에 맞는가?
- [ ] token이 console 또는 URL에 노출되지 않는가?
- [ ] 401 refresh 또는 로그인 이동 흐름이 있는가?
- [ ] Protected Route가 있는가?
- [ ] 권한별 UI가 적절한가?
- [ ] 백엔드 권한 검증을 대체하지 않는가?

## Routing

- [ ] route path가 명확한가?
- [ ] NotFound route가 있는가?
- [ ] route param 처리가 안전한가?
- [ ] 내부 이동에 Link / navigate를 사용하는가?
- [ ] API path와 frontend route가 충돌하지 않는가?
- [ ] SPA refresh fallback이 배포 환경에 맞는가?

## Accessibility

- [ ] semantic HTML을 사용하는가?
- [ ] heading 구조가 자연스러운가?
- [ ] keyboard navigation이 가능한가?
- [ ] focus-visible 스타일이 있는가?
- [ ] input label이 있는가?
- [ ] image alt가 적절한가?
- [ ] modal focus trap과 focus 복원이 있는가?
- [ ] error message 접근성이 고려되어 있는가?

## Styling

- [ ] styling naming이 일관적인가?
- [ ] inline style 남용이 없는가?
- [ ] 모바일 반응형이 깨지지 않는가?
- [ ] hover / active / disabled / focus 상태가 있는가?
- [ ] 색상 / spacing이 일관적인가?
- [ ] 전역 CSS 충돌 위험이 없는가?

## TypeScript

- [ ] props type이 명확한가?
- [ ] API response type이 있는가?
- [ ] ApiResponse / Page / Slice 타입이 정확한가?
- [ ] any 남용이 없는가?
- [ ] null / undefined 처리가 안전한가?
- [ ] event type이 명확한가?
- [ ] type assertion을 남용하지 않는가?

## Performance

- [ ] list key가 안정적인가?
- [ ] 큰 리스트 최적화가 필요한가?
- [ ] 이미지 크기와 fallback이 적절한가?
- [ ] layout shift 위험이 없는가?
- [ ] 큰 라이브러리 import 위험이 없는가?
- [ ] lazy loading이 필요한 route가 있는가?

## Security

- [ ] secret key가 프론트엔드에 노출되지 않는가?
- [ ] dangerouslySetInnerHTML 사용이 안전한가?
- [ ] markdown / rich text sanitize가 있는가?
- [ ] 외부 링크 rel 설정이 있는가?
- [ ] 사용자 입력 URL protocol 검증이 있는가?
- [ ] token과 개인정보가 안전하게 처리되는가?

## Testability

- [ ] API mock이 가능한가?
- [ ] validation / mapper / formatter가 테스트 가능한가?
- [ ] role / label / text 기반 UI 테스트가 가능한가?
- [ ] loading / error / empty state 테스트가 가능한가?
- [ ] auth / router / storage mock이 가능한가?

## Build Deploy

- [ ] npm run build 또는 yarn build가 성공하는가?
- [ ] TypeScript / ESLint error가 없는가?
- [ ] import path 대소문자 문제가 없는가?
- [ ] .env에 secret이 없는가?
- [ ] 운영 API URL에 localhost가 없는가?
- [ ] asset path가 배포 환경과 맞는가?
- [ ] SPA fallback 설정이 있는가?
- [ ] source map 공개 여부가 정책과 맞는가?
```

---

### [실무]

Full Checklist 적용 우선순위:

```text
Critical Risk Scan
→ Requirement / User Flow
→ API / Auth / Form
→ UX State
→ Security / Build
→ Accessibility / Routing
→ State / Hooks / Component
→ Performance / Testability
→ Low / Suggestion
```

항상 먼저 확인할 항목:

```text
build failure
secret exposure
token exposure
login failure
API endpoint mismatch
response mapping error
missing error handling
duplicate submit
protected route missing
production localhost
SPA refresh 404
```

---

### [FAQ]

Q. Full Frontend Review Checklist는 매번 전부 적용해야 해?
A. 변경 범위에 따라 선택 적용한다. 다만 Critical / High 위험 항목은 항상 확인해야 한다.

Q. 전체 체크리스트에서 가장 먼저 볼 항목은 뭐야?
A. build failure, secret exposure, login failure, API mismatch, missing error handling, duplicate submit이다.

Q. 체크리스트가 길면 어떻게 사용해?
A. 변경 파일과 기능 범위에 맞춰 관련 섹션을 선택하고 Critical / High 항목부터 적용한다.

Q. 최종 승인 기준은 뭐야?
A. Critical / High 문제가 없고 주요 사용자 흐름과 build가 정상이어야 한다.

---

# 6. Final Goal

## 6.1 Frontend Code Review Final Goal

### [개념]

Frontend Code Review의 최종 목적은 Frontend Agent가 생성한 코드나 사용자가 작성한 프론트엔드 코드를 Review Agent가 안정적으로 검토하고, PM Agent가 기능 완료와 배포 가능 여부를 판단할 수 있도록 하는 것이다.

이 문서는 사람 학습용 문서가 아니라 Agent Retrieval, Code Review, Validation, Final Decision을 위한 기준 문서이다.

---

### [핵심]

Frontend Code Review 최종 수행 가능 작업:

- 요구사항 충족 여부 검토
- 사용자 흐름 검토
- React Component 구조 검토
- Props / State 설계 검토
- Hook 사용 검토
- API 연동 안정성 검토
- Error / Loading / Empty State 검토
- Form Validation 검토
- Authentication Flow 검토
- Routing 검토
- Accessibility 검토
- Styling 일관성 검토
- TypeScript 타입 안정성 검토
- Performance 위험 검토
- Frontend Security 검토
- Testability 검토
- Build Deploy 위험 검토
- PR Review 결과 생성
- Final Decision 판단
- PM Agent 기능 완료 판단 지원

---

### [실무]

최종 Agent Flow:

```text
Code Review Request
→ Requirement Match
→ Critical Risk Scan
→ User Flow Review
→ Component Review
→ State Review
→ Hooks Review
→ API Review
→ UX State Review
→ Form Review
→ Auth Review
→ Routing Review
→ Accessibility Review
→ Styling Review
→ TypeScript Review
→ Performance Review
→ Security Review
→ Testability Review
→ Build Deploy Review
→ Review Result
→ Final Decision
```

최종 Decision 기준:

```text
Critical Issue
→ BLOCKED

High Issue
→ CHANGES REQUESTED

Low / Suggestion Only
→ APPROVED WITH COMMENTS

No Issue
→ APPROVED
```

---

### [FAQ]

Q. Frontend Code Review의 최종 목적은 뭐야?
A. 프론트엔드 코드가 요구사항을 만족하고 안정적으로 배포 가능한지 Agent가 일관되게 판단하도록 하는 것이다.

Q. 이 문서는 사람 공부용이야?
A. 아니다. Agent Retrieval, Code Review, Validation, Final Decision을 위한 RAG 최적화 문서다.

Q. Review Agent의 최종 역할은 뭐야?
A. 코드 품질과 운영 위험을 독립적으로 검토하고 승인 여부를 결정하는 것이다.

Q. PM Agent는 이 문서를 어떻게 사용해?
A. 기능 완료 여부, 위험도, 필수 수정 범위, 배포 가능성을 판단하는 데 사용한다.

---

# Retrieval Queries

### [FAQ]

Q. PR Review는 뭐야?
A. 변경된 프론트엔드 코드가 요구사항을 만족하고 병합 가능한 품질과 운영 안정성을 갖추었는지 검토하는 과정이다.

Q. PR Review에서 가장 먼저 확인할 것은 뭐야?
A. 요구사항 충족, 핵심 사용자 흐름, Critical / High 위험, build 가능성이다.

Q. PR Diff Review는 뭐야?
A. 변경된 코드의 차이점을 기준으로 영향 범위와 위험도를 파악하는 과정이다.

Q. Diff만 보면 충분해?
A. 아니다. diff는 변경 지점을 보여주지만 관련 사용자 흐름과 사용처 맥락도 함께 봐야 한다.

Q. 공통 컴포넌트 변경은 왜 위험해?
A. 여러 화면에 영향을 주므로 작은 변경도 예상보다 넓은 회귀 버그를 만들 수 있다.

Q. PR Checklist에서 가장 중요한 영역은 뭐야?
A. 요구사항, 사용자 흐름, API, 인증, 보안, 빌드 가능성이다.

Q. 좋은 리뷰 코멘트는 어떻게 써?
A. 우선순위, 문제, 영향, 수정 방향을 명확히 작성한다.

Q. 선택 개선도 리뷰 코멘트로 남겨도 돼?
A. 가능하다. 다만 Suggestion으로 표시해 필수 수정과 구분해야 한다.

Q. Critical Issue는 언제 붙여?
A. build 실패, secret 노출, 핵심 기능 미동작, 런타임 흰 화면, 운영 접근 불가에 붙인다.

Q. Critical Issue가 있으면 APPROVED 가능해?
A. 불가능하다. BLOCKED 또는 CHANGES REQUESTED로 판단해야 한다.

Q. High Issue는 언제 붙여?
A. 주요 사용자 흐름 오류, API 실패 미처리, 인증 누락, 중복 저장 위험, 보안 위험에 붙인다.

Q. High Issue가 있으면 배포 가능해?
A. 일반적으로 배포 전 수정이 필요하다. 영향 범위가 제한적이면 조건부 판단이 가능하다.

Q. Medium Issue는 언제 붙여?
A. 유지보수성, UX, 테스트 가능성, 접근성에 영향을 주는 문제에 붙인다.

Q. Medium Issue는 반드시 수정해야 해?
A. 반드시 즉시 수정해야 하는 것은 아니지만 일정과 영향도에 따라 처리한다.

Q. Low Issue는 반드시 수정해야 해?
A. 아니다. 개선 권장 사항이며 Critical / High보다 우선하지 않는다.

Q. Suggestion은 필수 수정이야?
A. 아니다. 선택 개선 사항이다.

Q. Final Review Output Format은 뭐야?
A. Summary, Critical Issues, High Priority Issues, Medium Priority Issues, Low Priority Issues, Suggestions, Checklist, Final Decision 구조다.

Q. 문제가 없는 섹션은 생략해도 돼?
A. 가능하지만 Agent 출력 일관성을 위해 None으로 명시하는 것이 좋다.

Q. Final Decision은 반드시 필요해?
A. 필요하다. 병합, 수정, 배포 여부를 판단하는 핵심 결과다.

Q. Final Decision에는 뭐가 있어?
A. APPROVED, APPROVED WITH COMMENTS, CHANGES REQUESTED, BLOCKED가 있다.

Q. Critical Issue가 있으면 Final Decision은 뭐야?
A. BLOCKED다.

Q. High Issue가 있으면 Final Decision은 뭐야?
A. 일반적으로 CHANGES REQUESTED다.

Q. Low와 Suggestion만 있으면 승인 가능해?
A. 가능하다. APPROVED WITH COMMENTS가 적절하다.

Q. Required Fixes에는 무엇을 넣어야 해?
A. Critical / High Issue와 핵심 요구사항 누락처럼 배포 전 반드시 수정해야 하는 항목을 넣는다.

Q. Suggestion도 Required Fixes에 넣어도 돼?
A. 권장하지 않는다. 선택 개선은 Suggestions로 분리해야 수정 우선순위가 명확해진다.

Q. Frontend Agent Self Review는 왜 필요해?
A. 코드 생성 Agent가 1차 품질 점검을 수행하고 Review Agent가 빠르게 검토할 수 있도록 하기 위해 필요하다.

Q. Self Review가 있으면 Review Agent가 필요 없어?
A. 아니다. Self Review는 1차 점검이고 Review Agent는 독립 검증 역할이다.

Q. Build Check를 못 했으면 어떻게 써?
A. 확인하지 못했다고 명시해야 한다. 확인하지 않은 build 성공을 주장하면 안 된다.

Q. Review Agent Final Output에는 무엇이 꼭 있어야 해?
A. Summary, priority별 issues, Required Fixes, Final Decision이 필요하다.

Q. 확인하지 못한 build를 성공했다고 써도 돼?
A. 안 된다. 확인하지 못했으면 확인하지 못했다고 명시해야 한다.

Q. PM Agent는 코드 세부 구현을 봐야 해?
A. 세부 구현 전체보다 요구사항 충족, 위험도, 배포 가능성, 수정 우선순위를 봐야 한다.

Q. Critical Issue가 있으면 PM Agent는 어떻게 판단해?
A. Blocked 또는 No-Go로 판단해야 한다.

Q. Full Frontend Review Checklist는 매번 전부 적용해야 해?
A. 변경 범위에 따라 선택 적용한다. 다만 Critical / High 위험 항목은 항상 확인해야 한다.

Q. 전체 체크리스트에서 가장 먼저 볼 항목은 뭐야?
A. build failure, secret exposure, login failure, API mismatch, missing error handling, duplicate submit이다.

Q. 최종 승인 기준은 뭐야?
A. Critical / High 문제가 없고 주요 사용자 흐름과 build가 정상이어야 한다.

Q. Frontend Code Review의 최종 목적은 뭐야?
A. 프론트엔드 코드가 요구사항을 만족하고 안정적으로 배포 가능한지 Agent가 일관되게 판단하도록 하는 것이다.

Q. Review Agent의 최종 역할은 뭐야?
A. 코드 품질과 운영 위험을 독립적으로 검토하고 승인 여부를 결정하는 것이다.

Q. PM Agent는 Frontend Code Review 문서를 어떻게 사용해?
A. 기능 완료 여부, 위험도, 필수 수정 범위, 배포 가능성을 판단하는 데 사용한다.
