# Frontend Code Review Domain Rules

---

# 1. Domain Purpose

## 1.1 Purpose

### [개념]

Frontend Code Review Domain Rules 문서는 Frontend Agent / Review Agent / PM Agent가 프론트엔드 코드의 품질, 안정성, 유지보수성, 성능, 접근성, 보안, API 연동, 상태 관리, 컴포넌트 설계, 테스트 가능성을 검토하기 위한 RAG Retrieval 최적화 문서이다.

이 문서는 사람 공부용 문서가 아니라 Agent가 실제 프론트엔드 코드 리뷰를 수행할 때 사용하는 판단 기준 문서이다.

목적:

- React 코드 리뷰 기준 제공
- JavaScript / TypeScript 코드 품질 검토
- Component 구조 검토
- Props / State 설계 검토
- API 연동 코드 검토
- Error / Loading / Empty State 검토
- Form / Validation 검토
- Authentication Flow 검토
- Accessibility 검토
- Styling 구조 검토
- Performance 문제 검토
- Test 가능성 검토
- Build / Deploy 위험 요소 검토
- PM Agent의 기능 완료 판단 지원
- Review Agent의 최종 승인 기준 제공

---

### [핵심]

Frontend Code Review의 핵심 기준:

1. 요구사항을 만족하는가?
2. 컴포넌트 책임이 명확한가?
3. 상태 관리가 과하지 않은가?
4. API 연동이 안정적인가?
5. Error / Loading / Empty 처리가 있는가?
6. Form Validation이 누락되지 않았는가?
7. 인증 흐름이 안전한가?
8. 접근성 기본 기준을 만족하는가?
9. 불필요한 렌더링과 성능 문제가 없는가?
10. 빌드와 배포에 문제 없는가?
11. 테스트 가능한 구조인가?
12. 유지보수 가능한 코드인가?

---

### [실무]

Frontend Code Review는 단순 문법 검사가 아니다.

Review Agent는 아래 흐름으로 판단해야 한다.

```text
User Requirement
→ UI Behavior Check
→ Component Structure Review
→ State / Props Review
→ API Integration Review
→ UX State Review
→ Accessibility Review
→ Security Review
→ Performance Review
→ Testability Review
→ Build Deploy Risk Review
→ Final Review Result
```

---

### [FAQ]

Q. Frontend Code Review 문서는 사람 공부용이야?

A.
아니다. Frontend Agent / Review Agent / PM Agent가 코드 품질을 판단하기 위한 RAG 문서다.

Q. 코드 리뷰에서 문법만 보면 돼?

A.
아니다. 요구사항, 구조, 상태, API, UX, 접근성, 보안, 성능, 테스트 가능성까지 함께 봐야 한다.

Q. 프론트엔드 리뷰에서 가장 중요한 것은 뭐야?

A.
사용자가 실제로 정상적으로 사용할 수 있는지, 코드가 유지보수 가능한지, 장애 상황을 처리하는지가 중요하다.

Q. Review Agent는 어떤 관점으로 봐야 해?

A.
기능 동작 여부뿐 아니라 운영 중 오류 가능성, 협업 가능성, 변경 용이성까지 봐야 한다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

Frontend Code Review 문서는 프론트엔드 구현 결과를 검토하는 데 필요한 실무 범위를 포함한다.

포함 범위:

- Requirements Review
- UI Behavior Review
- Component Review
- Props Review
- State Review
- Event Handler Review
- React Hooks Review
- API Integration Review
- Axios / Fetch Review
- Error Handling Review
- Loading UX Review
- Empty State Review
- Form Validation Review
- Authentication Flow Review
- Authorization UI Review
- Routing Review
- Accessibility Review
- Styling Review
- Responsive Review
- Performance Review
- TypeScript Review
- Security Review
- Testability Review
- Build / Deploy Risk Review
- Code Smell Review
- PR Review Checklist

---

### [핵심]

반드시 포함:

- 기능 요구사항 충족 여부
- 컴포넌트 책임 분리
- Props drilling 과다 여부
- State 위치 적절성
- useEffect 의존성 검토
- API 호출 중복 여부
- Error / Loading / Empty 처리
- Form submit 중복 방지
- 인증 토큰 처리
- 접근성 기본 검토
- 반응형 UI 검토
- 환경 변수와 localhost 하드코딩 검토
- 빌드 가능성 검토

---

### [실무]

Frontend Code Review는 다음 Domain Rules와 연결된다.

```text
React Core
→ React Component Design
→ State Management
→ Data Fetching
→ Form Handling
→ Authentication Flow
→ Error Handling Loading UX
→ UI Component Pattern
→ Frontend Accessibility
→ Frontend Build Deploy
→ Frontend Code Review
```

---

### [FAQ]

Q. Code Review 문서가 다른 Frontend 문서와 겹치지 않아?

A.
겹치는 개념을 다시 설명하는 것이 아니라, 기존 Domain Rules를 기준으로 검토 관점을 제공한다.

Q. Review Agent는 모든 코드를 완벽히 고쳐야 해?

A.
아니다. 문제를 분류하고 우선순위를 정해 수정 방향을 제시하는 것이 핵심이다.

Q. PM Agent도 이 문서를 써?

A.
쓴다. PM Agent는 기능 완료 여부와 배포 가능 여부를 판단할 때 Code Review 결과를 참고한다.

---

## 2.2 Excluded Scope

### [개념]

Frontend Code Review 문서는 코드 리뷰 기준에 집중한다.

제외 범위:

- React 문법 기초 전체 설명
- JavaScript 문법 기초 전체 설명
- TypeScript 문법 기초 전체 설명
- CSS Architecture 심화
- Design System 심화
- Next.js App Router 심화
- Advanced Performance Profiling
- Browser Rendering Engine 심화
- Security Penetration Testing
- DevOps CI/CD 심화
- Backend Code Review

---

### [핵심]

제외 이유:

- Domain별 책임 분리
- Retrieval 혼선 방지
- Review 기준 중심 유지
- Chunk 품질 유지

---

### [실무]

다른 문서로 위임하는 경우:

```text
문법 자체 설명 필요
→ JavaScript / TypeScript / React Core 문서 참조

스타일 구조 심화 필요
→ Styling Architecture 문서 참조

디자인 토큰 / 컴포넌트 규격 필요
→ Design System 문서 참조

배포 설정 심화 필요
→ Frontend Build Deploy 문서 참조
```

---

### [FAQ]

Q. Code Review 문서에서 React 문법을 자세히 설명해야 해?

A.
아니다. React 문법 자체는 React Core 문서에서 다루고, 여기서는 리뷰 기준 중심으로 다룬다.

Q. CSS 구조 리뷰도 포함해?

A.
기본적인 스타일 리뷰는 포함하지만 심화 구조는 Styling Architecture 문서에서 다룬다.

---

# 3. Review Priority Rules

## 3.1 Review Priority

### [개념]

Frontend Code Review는 모든 문제를 같은 중요도로 보지 않는다.

리뷰 문제는 우선순위를 나누어 판단해야 한다.

---

### [핵심]

우선순위:

1. Critical
2. High
3. Medium
4. Low
5. Suggestion

---

### [Comparison]

| Priority   | 의미                             | 예시                                     |
| ---------- | -------------------------------- | ---------------------------------------- |
| Critical   | 즉시 수정 필요, 서비스 장애 가능 | 로그인 불가, 빌드 실패, 결제 Secret 노출 |
| High       | 주요 기능 오류 또는 운영 위험    | API 에러 미처리, 인증 체크 누락          |
| Medium     | 유지보수 / UX 문제               | 중복 코드, Empty State 누락              |
| Low        | 개선 권장                        | naming 애매함, 작은 스타일 불일치        |
| Suggestion | 선택 개선                        | 구조 리팩토링 제안, 성능 최적화 여지     |

---

### [실무]

Review Agent는 아래 형식으로 문제를 분류한다.

```text
[Critical] 빌드 실패 가능성이 있음
[High] API 실패 시 사용자에게 에러 메시지가 표시되지 않음
[Medium] 컴포넌트 책임이 커서 분리 필요
[Low] 변수명이 역할을 명확히 드러내지 않음
[Suggestion] Custom Hook으로 분리하면 재사용성이 좋아짐
```

---

### [FAQ]

Q. 코드 리뷰에서 모든 지적을 반드시 수정해야 해?

A.
아니다. Critical과 High는 반드시 수정하고, Medium 이하 문제는 일정과 영향도를 고려한다.

Q. 사소한 naming도 리뷰해야 해?

A.
가능하지만 기능 안정성, 유지보수성, 오류 가능성보다 우선하지 않는다.

Q. Review Agent는 우선순위를 왜 붙여야 해?

A.
사용자나 개발자가 어떤 문제를 먼저 수정해야 하는지 판단하기 쉽기 때문이다.

---

## 3.2 Review Result Format

### [개념]

Review Result Format은 Code Review 결과를 일관되게 출력하기 위한 형식이다.

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

---

### [실무]

Final Decision 예:

```text
APPROVED
APPROVED WITH COMMENTS
CHANGES REQUESTED
BLOCKED
```

판단 기준:

| Decision               | 의미                                 |
| ---------------------- | ------------------------------------ |
| APPROVED               | 배포 또는 병합 가능                  |
| APPROVED WITH COMMENTS | 경미한 개선 권장                     |
| CHANGES REQUESTED      | 수정 후 재검토 필요                  |
| BLOCKED                | 빌드 실패, 보안 문제, 핵심 기능 실패 |

---

### [FAQ]

Q. 리뷰 결과에 Final Decision이 필요해?

A.
필요하다. PM Agent와 Review Agent가 다음 작업 진행 여부를 판단하기 위해 필요하다.

Q. BLOCKED는 언제 써?

A.
빌드 실패, 인증 실패, 보안 키 노출, 핵심 기능 미동작처럼 진행을 막아야 할 때 사용한다.

---

# 4. Requirements Review Rules

## 4.1 Requirement Match Review

### [개념]

Requirement Match Review는 구현 코드가 사용자의 요구사항과 실제 기능 목적을 만족하는지 검토하는 과정이다.

---

### [핵심]

확인 항목:

- 요구된 화면이 구현되었는가?
- 요구된 사용자 행동이 동작하는가?
- 필수 API가 연결되었는가?
- 성공 / 실패 / 빈 결과 상태가 있는가?
- 권한별 접근이 반영되었는가?
- 반응형 요구사항이 반영되었는가?
- 제출 / 저장 / 수정 / 삭제 흐름이 완성되었는가?

---

### [Flow]

```text
User Requirement
→ Feature Checklist
→ UI Element Check
→ User Action Check
→ API Flow Check
→ Edge Case Check
→ Review Decision
```

---

### [실무]

리뷰 시 단순히 코드가 존재하는지만 보면 안 된다.

예:

```text
요구사항: 축제 검색 기능
검토:
- 검색 input이 있는가?
- 검색 버튼 또는 enter 제출이 가능한가?
- API 요청이 정상인가?
- 검색 결과가 표시되는가?
- 결과 없음 상태가 있는가?
- API 실패 상태가 있는가?
- 검색어 초기화가 가능한가?
```

---

### [FAQ]

Q. 요구사항 리뷰는 PM Agent 역할 아니야?

A.
PM Agent도 담당하지만 Review Agent도 코드가 요구사항을 실제로 만족하는지 확인해야 한다.

Q. UI만 보이면 기능 완료로 봐도 돼?

A.
아니다. 사용자 행동, API 연동, 오류 처리, 권한 처리까지 확인해야 한다.

Q. 요구사항이 애매하면 어떻게 해?

A.
현재 코드 기준으로 가능한 가정을 명시하고 누락 가능성을 Issue로 남긴다.

---

## 4.2 User Flow Review

### [개념]

User Flow Review는 사용자가 실제 화면에서 수행하는 행동 흐름이 끊기지 않는지 검토하는 과정이다.

---

### [핵심]

검토 대상:

- 페이지 진입
- 데이터 로딩
- 사용자 입력
- 버튼 클릭
- API 요청
- 결과 표시
- 오류 처리
- 페이지 이동
- 뒤로가기
- 로그아웃 / 권한 만료

---

### [실무]

User Flow 예:

```text
로그인 페이지 진입
→ 이메일 / 비밀번호 입력
→ 제출
→ Loading 표시
→ 로그인 API 요청
→ 토큰 저장
→ 메인 페이지 이동
→ 실패 시 에러 메시지 표시
```

리뷰 기준:

```md
- [ ] 사용자가 다음 행동을 알 수 있는가?
- [ ] 실패했을 때 복구할 수 있는가?
- [ ] 중복 제출이 방지되는가?
- [ ] 완료 후 적절한 피드백이 있는가?
```

---

### [FAQ]

Q. User Flow 리뷰는 왜 필요해?

A.
코드는 맞아 보여도 실제 사용자 흐름이 끊기면 기능이 완성된 것이 아니기 때문이다.

Q. API 성공만 보면 안 돼?

A.
안 된다. 실패, 지연, 빈 결과, 인증 만료 같은 상황도 함께 봐야 한다.

---

# 5. Component Review Rules

## 5.1 Component Responsibility Review

### [개념]

Component Responsibility Review는 컴포넌트가 하나의 명확한 책임을 갖고 있는지 검토하는 과정이다.

---

### [핵심]

좋은 컴포넌트 기준:

- 역할이 명확함
- props가 과도하지 않음
- 내부 상태가 필요한 만큼만 있음
- UI와 비즈니스 로직이 과하게 섞이지 않음
- 재사용 가능성이 있음
- 파일명이 역할을 표현함
- 불필요한 사이드 이펙트가 없음

---

### [주의]

나쁜 컴포넌트 예:

```text
한 컴포넌트가 다음을 모두 처리:
- API 호출
- Form 검증
- Modal 상태
- Table 렌더링
- Pagination
- Toast
- Auth 체크
- Routing 이동
```

이런 경우 분리가 필요하다.

---

### [실무]

분리 기준:

```text
Page Component
→ 데이터 조회 / 페이지 조립

Container Component
→ 상태와 비즈니스 흐름

Presentational Component
→ UI 표시

Custom Hook
→ 재사용 가능한 로직

Service / API Module
→ API 호출
```

---

### [FAQ]

Q. 컴포넌트가 몇 줄 이상이면 분리해야 해?

A.
줄 수만으로 판단하지 않는다. 책임이 여러 개 섞였는지가 더 중요하다.

Q. Page 컴포넌트에 API 호출이 있어도 돼?

A.
가능하다. 다만 여러 곳에서 재사용되거나 복잡해지면 Custom Hook 또는 Query Hook으로 분리하는 것이 좋다.

Q. Presentational Component는 뭐야?

A.
주로 props를 받아 UI를 표시하는 컴포넌트다. 데이터 조회나 복잡한 상태 관리는 하지 않는 것이 좋다.

---

## 5.2 Component Naming Review

### [개념]

Component Naming Review는 컴포넌트 이름이 역할과 의미를 명확히 표현하는지 검토하는 과정이다.

---

### [핵심]

권장:

- PascalCase 사용
- 역할 중심 이름
- Page / Modal / Form / List / Card / Item 구분
- 너무 추상적인 이름 지양
- 도메인 의미 포함

좋은 예:

```text
FestivalCard
FestivalList
FestivalSearchForm
LoginForm
ReviewModal
NotificationItem
```

나쁜 예:

```text
Box
Component1
DataView
Custom
TestPage
Temp
```

---

### [실무]

파일명과 컴포넌트명 일치 권장:

```text
FestivalCard.jsx
→ function FestivalCard()

LoginForm.tsx
→ function LoginForm()
```

---

### [FAQ]

Q. 컴포넌트 이름에 Page를 붙여야 해?

A.
페이지 단위 컴포넌트라면 `LoginPage`, `FestivalDetailPage`처럼 붙이는 것이 구분에 좋다.

Q. 이름이 길어도 돼?

A.
역할이 명확하다면 어느 정도 길어도 괜찮다. 모호한 짧은 이름보다 낫다.

---

## 5.3 Props Review

### [개념]

Props Review는 부모 컴포넌트가 자식 컴포넌트에 전달하는 데이터와 이벤트가 적절한지 검토하는 과정이다.

---

### [핵심]

검토 항목:

- props 이름이 명확한가?
- props 개수가 과도하지 않은가?
- optional props 기본값이 있는가?
- event handler naming이 일관적인가?
- boolean props가 의미 명확한가?
- 불필요한 전체 객체 전달이 없는가?
- props drilling이 과하지 않은가?

---

### [예제]

좋은 예:

```jsx
<FestivalCard
  festival={festival}
  onFavoriteClick={handleFavoriteClick}
  isFavorite={isFavorite}
/>
```

나쁜 예:

```jsx
<FestivalCard data={data} fn={fn} flag={true} />
```

---

### [실무]

Event handler props naming:

```text
onClick
onSubmit
onChange
onClose
onSelect
onFavoriteClick
onSearchSubmit
```

내부 handler naming:

```text
handleClick
handleSubmit
handleChange
handleClose
handleSelect
```

---

### [FAQ]

Q. props가 많으면 무조건 나쁜 코드야?

A.
무조건은 아니지만 props가 너무 많으면 컴포넌트 책임이 커졌거나 객체화 / 분리가 필요할 수 있다.

Q. data, item 같은 props 이름은 안 좋아?

A.
문맥이 명확하면 가능하지만 `festival`, `review`, `user`처럼 도메인 이름을 쓰는 것이 더 명확하다.

Q. boolean props 이름은 어떻게 짓는 게 좋아?

A.
`isOpen`, `isLoading`, `hasError`, `canSubmit`처럼 true / false 의미가 드러나게 작성한다.

---

# 6. State Review Rules

## 6.1 State Location Review

### [개념]

State Location Review는 상태가 적절한 컴포넌트나 store에 위치하는지 검토하는 과정이다.

---

### [핵심]

상태 위치 기준:

```text
한 컴포넌트에서만 사용
→ Local State

부모와 자식이 공유
→ 가장 가까운 공통 부모

여러 페이지에서 공유
→ Global State

서버 데이터
→ Server State Tool 또는 Query Hook

URL에 남아야 하는 값
→ URL Query Params
```

---

### [실무]

상태 분류:

| 상태 종류       | 예시                     | 권장 위치                 |
| --------------- | ------------------------ | ------------------------- |
| UI State        | modal open, tab selected | local state               |
| Form State      | input value              | form component            |
| Server State    | festival list            | React Query / custom hook |
| Auth State      | user, token              | auth context / store      |
| URL State       | search keyword, page     | query string              |
| Global UI State | toast, theme             | global store              |

---

### [FAQ]

Q. 모든 상태를 Redux나 Zustand에 넣어도 돼?

A.
권장하지 않는다. 컴포넌트 내부에서만 쓰는 상태는 local state가 더 단순하다.

Q. 검색어는 state에 둬야 해 URL에 둬야 해?

A.
공유, 새로고침 유지, 뒤로가기 지원이 필요하면 URL query params가 좋다.

Q. 서버에서 받아온 데이터는 local state에 저장하면 안 돼?

A.
가능하지만 캐싱, 재요청, 로딩, 에러 처리가 복잡하면 React Query 같은 server state 도구가 적합하다.

---

## 6.2 State Duplication Review

### [개념]

State Duplication은 같은 의미의 데이터가 여러 state에 중복 저장되는 문제다.

---

### [핵심]

문제 예:

```jsx
const [users, setUsers] = useState([]);
const [userCount, setUserCount] = useState(0);
```

`userCount`가 항상 `users.length`라면 파생 값으로 계산하는 것이 낫다.

---

### [Best Practice]

파생 값은 state보다 계산으로 처리한다.

```jsx
const userCount = users.length;
```

복잡한 계산은 memoization을 고려한다.

```jsx
const filteredFestivals = useMemo(() => {
  return festivals.filter((festival) => festival.region === selectedRegion);
}, [festivals, selectedRegion]);
```

---

### [FAQ]

Q. state를 많이 만들면 안 돼?

A.
필요한 state는 만들어야 한다. 하지만 기존 state에서 계산 가능한 값은 중복 저장하지 않는 것이 좋다.

Q. useMemo는 항상 써야 해?

A.
아니다. 계산 비용이 크거나 참조 안정성이 필요한 경우에만 사용한다.

---

## 6.3 State Update Review

### [개념]

State Update Review는 상태 변경 방식이 React의 비동기 업데이트와 불변성 원칙에 맞는지 검토하는 과정이다.

---

### [핵심]

검토 항목:

- 기존 state 직접 수정 금지
- 이전 state 기반 업데이트 시 함수형 업데이트 사용
- 배열 / 객체는 새 참조로 업데이트
- 비동기 처리 후 unmounted component 업데이트 주의
- optimistic update rollback 고려

---

### [예제]

나쁜 예:

```jsx
items.push(newItem);
setItems(items);
```

좋은 예:

```jsx
setItems((prevItems) => [...prevItems, newItem]);
```

객체 업데이트:

```jsx
setUser((prevUser) => ({
  ...prevUser,
  nickname: "newName",
}));
```

---

### [FAQ]

Q. 배열에 push하고 setState 하면 안 돼?

A.
권장하지 않는다. 기존 배열을 직접 수정하면 React가 변경을 감지하지 못할 수 있다.

Q. 이전 state 값을 기준으로 업데이트할 때는 어떻게 해?

A.
`setState(prev => next)` 형태의 함수형 업데이트를 사용하는 것이 안전하다.

---

# 7. React Hooks Review Rules

## 7.1 useEffect Review

### [개념]

useEffect Review는 side effect 처리와 dependency array가 적절한지 검토하는 과정이다.

---

### [핵심]

검토 항목:

- dependency array 누락 여부
- 불필요한 effect 여부
- 무한 루프 가능성
- cleanup 필요 여부
- API 호출 중복 여부
- state 동기화 남용 여부
- effect 안에서 너무 많은 책임 처리 여부

---

### [주의]

나쁜 예:

```jsx
useEffect(() => {
  setFilteredItems(items.filter((item) => item.active));
}, [items]);
```

단순 파생 값이면 state + effect보다 계산 값이 낫다.

좋은 예:

```jsx
const filteredItems = items.filter((item) => item.active);
```

---

### [실무]

useEffect가 적합한 경우:

```text
API 호출
구독 설정
이벤트 리스너 등록
타이머 설정
외부 라이브러리 연동
document title 변경
```

useEffect가 부적합한 경우:

```text
단순 값 계산
props를 state에 복사
렌더링 중 계산 가능한 값
이벤트 핸들러에서 처리 가능한 로직
```

---

### [FAQ]

Q. useEffect dependency warning은 무시해도 돼?

A.
권장하지 않는다. 의존성 누락은 stale closure나 예상치 못한 버그를 만들 수 있다.

Q. props를 state로 복사하려고 useEffect를 써도 돼?

A.
대부분 불필요하다. 특별한 초기화 목적이 아니라면 props를 직접 사용하거나 파생 값으로 계산한다.

Q. useEffect가 계속 실행돼?

A.
dependency에 매 렌더링마다 새로 만들어지는 객체, 배열, 함수가 들어갔을 수 있다.

---

## 7.2 Custom Hook Review

### [개념]

Custom Hook Review는 재사용 가능한 로직이 적절히 hook으로 분리되었는지 검토하는 과정이다.

---

### [핵심]

Custom Hook 적합 상황:

- 여러 컴포넌트에서 반복되는 로직
- API 호출 로직
- Form 상태 로직
- Modal 제어 로직
- LocalStorage 연동
- 권한 체크
- Pagination 로직

---

### [예제]

좋은 예:

```jsx
function useModal() {
  const [isOpen, setIsOpen] = useState(false);

  const open = () => setIsOpen(true);
  const close = () => setIsOpen(false);

  return { isOpen, open, close };
}
```

---

### [실무]

Custom Hook 리뷰 기준:

```md
- [ ] 이름이 use로 시작하는가?
- [ ] hook 내부에서 조건부 hook 호출이 없는가?
- [ ] 반환 값이 명확한가?
- [ ] 너무 많은 책임을 갖지 않는가?
- [ ] 컴포넌트와 분리 가능한 로직인가?
```

---

### [FAQ]

Q. Custom Hook은 언제 만들어?

A.
동일한 상태 로직이나 side effect 로직이 여러 컴포넌트에서 반복될 때 만든다.

Q. Hook 이름은 꼭 use로 시작해야 해?

A.
그렇다. React Hook 규칙과 lint 검사를 위해 `use` prefix를 사용해야 한다.

---

## 7.3 Hook Rule Review

### [개념]

Hook Rule Review는 React Hook 사용 규칙을 지키는지 검토하는 과정이다.

---

### [핵심]

Hook 규칙:

- 컴포넌트 최상위에서만 호출
- 조건문 안에서 호출 금지
- 반복문 안에서 호출 금지
- 일반 함수에서 호출 금지
- React Component 또는 Custom Hook에서만 호출
- Hook 호출 순서 유지

---

### [예제]

나쁜 예:

```jsx
if (isLoggedIn) {
  useEffect(() => {
    fetchUser();
  }, []);
}
```

좋은 예:

```jsx
useEffect(() => {
  if (!isLoggedIn) return;

  fetchUser();
}, [isLoggedIn]);
```

---

### [FAQ]

Q. 조건문 안에서 useEffect를 호출하면 안 돼?

A.
안 된다. Hook 호출 순서가 렌더링마다 달라질 수 있기 때문이다.

Q. 조건이 있을 때는 어떻게 해?

A.
Hook은 최상위에서 호출하고, Hook 내부에서 조건을 처리한다.

---

# 8. API Integration Review Rules

## 8.1 API Module Review

### [개념]

API Module Review는 API 호출 코드가 일관된 구조로 분리되어 있는지 검토하는 과정이다.

---

### [핵심]

검토 항목:

- API 호출 코드가 컴포넌트에 과도하게 섞이지 않았는가?
- Axios instance 또는 fetch wrapper가 있는가?
- baseURL이 환경 변수로 분리되었는가?
- 인증 header 처리가 일관적인가?
- 공통 에러 처리가 있는가?
- endpoint naming이 명확한가?
- public API와 private API가 구분되는가?

---

### [예제]

권장 구조:

```text
src/
├─ api/
│  ├─ axiosInstance.js
│  ├─ festivalApi.js
│  ├─ authApi.js
│  └─ reviewApi.js
```

API 함수 예:

```js
export const festivalApi = {
  getFestivalDetail: (festivalId) => api.get(`/festivals/${festivalId}`),

  searchFestivals: (params) => api.get("/festivals/search", { params }),
};
```

---

### [FAQ]

Q. 컴포넌트 안에서 axios.get을 바로 써도 돼?

A.
작은 코드에서는 가능하지만 API가 늘어나면 api module로 분리하는 것이 유지보수에 좋다.

Q. API 함수 이름은 어떻게 짓는 게 좋아?

A.
`getFestivalDetail`, `createReview`, `deleteFavorite`처럼 동작과 도메인이 드러나야 한다.

---

## 8.2 API Error Review

### [개념]

API Error Review는 API 실패 상황을 사용자와 코드가 적절히 처리하는지 검토하는 과정이다.

---

### [핵심]

검토 항목:

- try / catch 또는 error boundary가 있는가?
- 사용자에게 에러 메시지가 표시되는가?
- 401 / 403 / 404 / 500 처리가 구분되는가?
- 네트워크 실패 처리가 있는가?
- 재시도 가능 여부가 있는가?
- Loading이 종료되는가?
- 에러 후 복구 행동이 있는가?

---

### [예제]

기본 예:

```js
try {
  const response = await festivalApi.getFestivalDetail(festivalId);
  setFestival(response.data);
} catch (error) {
  setError("축제 정보를 불러오지 못했습니다.");
} finally {
  setLoading(false);
}
```

---

### [실무]

Status별 처리:

| Status        | 의미        | UI 처리                    |
| ------------- | ----------- | -------------------------- |
| 400           | 잘못된 요청 | 입력값 확인 안내           |
| 401           | 인증 필요   | 로그인 이동 또는 토큰 갱신 |
| 403           | 권한 없음   | 접근 불가 메시지           |
| 404           | 데이터 없음 | Not Found 화면             |
| 500           | 서버 오류   | 잠시 후 재시도 안내        |
| Network Error | 연결 실패   | 네트워크 확인 안내         |

---

### [FAQ]

Q. API 에러는 console.log만 해도 돼?

A.
안 된다. 사용자가 알 수 있는 메시지와 복구 방법이 필요하다.

Q. 401 에러는 어떻게 처리해야 해?

A.
인증 만료로 보고 refresh token 처리 또는 로그인 페이지 이동을 고려한다.

Q. 404는 항상 에러야?

A.
상황에 따라 Not Found 상태로 정상적으로 안내해야 하는 경우도 있다.

---

## 8.3 Request Duplication Review

### [개념]

Request Duplication Review는 동일한 API 요청이 불필요하게 반복되는지 검토하는 과정이다.

---

### [핵심]

중복 요청 원인:

- useEffect dependency 오류
- React StrictMode 개발 중 이중 실행
- 이벤트 핸들러 중복 바인딩
- 페이지 진입 시 여러 컴포넌트에서 같은 요청
- cache 전략 없음
- submit 버튼 중복 클릭

---

### [실무]

검토 Flow:

```text
Network Tab 확인
→ 같은 API 반복 요청 확인
→ useEffect dependency 확인
→ component mount 위치 확인
→ cache / query key 확인
→ submit disabled 처리 확인
```

---

### [예제]

중복 제출 방지:

```jsx
<button type="submit" disabled={isSubmitting}>
  {isSubmitting ? "저장 중..." : "저장"}
</button>
```

---

### [FAQ]

Q. API가 두 번 호출돼?

A.
useEffect 의존성, StrictMode, 중복 컴포넌트 mount, submit 중복 클릭을 확인한다.

Q. React StrictMode 때문에 개발에서 두 번 호출될 수 있어?

A.
개발 환경에서는 side effect 검출을 위해 일부 로직이 두 번 실행될 수 있다. 운영 동작과 구분해야 한다.

---

# 9. Error Loading Empty Review Rules

## 9.1 Loading State Review

### [개념]

Loading State Review는 데이터 요청 중 사용자가 대기 상태를 이해할 수 있는지 검토하는 과정이다.

---

### [핵심]

검토 항목:

- 초기 로딩 표시
- 버튼 제출 중 disabled
- 중복 클릭 방지
- Skeleton / Spinner / Text loading 적절성
- 로딩 종료 보장
- 부분 로딩 구분
- 긴 로딩 시 사용자 피드백

---

### [예제]

```jsx
if (isLoading) {
  return <div>불러오는 중...</div>;
}
```

버튼 로딩:

```jsx
<button type="submit" disabled={isSubmitting}>
  {isSubmitting ? "제출 중..." : "제출"}
</button>
```

---

### [FAQ]

Q. Loading UI는 꼭 필요해?

A.
필요하다. API 요청 중 사용자가 화면이 멈췄다고 느끼지 않게 해야 한다.

Q. 버튼 제출 중 disabled는 왜 필요해?

A.
중복 제출과 중복 API 요청을 막기 위해 필요하다.

---

## 9.2 Error State Review

### [개념]

Error State Review는 실패 상황에서 사용자가 문제를 이해하고 다음 행동을 할 수 있는지 검토하는 과정이다.

---

### [핵심]

좋은 Error UI:

- 무엇이 실패했는지 알려줌
- 사용자가 이해할 수 있는 문장 사용
- 재시도 버튼 제공 가능
- 개발자용 raw error 노출 금지
- 인증 오류는 로그인 이동 제공
- 권한 오류는 접근 불가 안내

---

### [예제]

```jsx
if (error) {
  return (
    <div role="alert">
      <p>데이터를 불러오지 못했습니다.</p>
      <button type="button" onClick={refetch}>
        다시 시도
      </button>
    </div>
  );
}
```

---

### [FAQ]

Q. 에러 메시지에 서버 에러 내용을 그대로 보여줘도 돼?

A.
권장하지 않는다. 사용자 친화 메시지로 바꾸고 민감한 정보는 노출하지 않아야 한다.

Q. 에러 상태에는 재시도 버튼이 필요해?

A.
데이터 조회 실패처럼 복구 가능한 경우에는 재시도 버튼이 좋다.

---

## 9.3 Empty State Review

### [개념]

Empty State Review는 데이터가 없을 때 빈 화면 대신 적절한 안내를 제공하는지 검토하는 과정이다.

---

### [핵심]

Empty State가 필요한 상황:

- 검색 결과 없음
- 알림 없음
- 리뷰 없음
- 즐겨찾기 없음
- 채팅 메시지 없음
- 필터 결과 없음

---

### [예제]

```jsx
if (festivals.length === 0) {
  return <p>조건에 맞는 축제가 없습니다.</p>;
}
```

---

### [실무]

좋은 Empty State:

```text
상태 설명
→ 이유 또는 조건 안내
→ 다음 행동 제안
```

예:

```text
검색 결과가 없습니다.
다른 키워드나 지역으로 다시 검색해 보세요.
```

---

### [FAQ]

Q. 데이터가 없으면 그냥 빈 화면이면 안 돼?

A.
안 된다. 사용자는 오류인지 결과가 없는지 알 수 없다.

Q. Empty State는 Error State와 달라?

A.
다르다. Empty State는 요청은 성공했지만 표시할 데이터가 없는 상태다.

---

# 10. Form Review Rules

## 10.1 Form Structure Review

### [개념]

Form Structure Review는 입력 폼이 의미 있는 구조와 접근성을 갖추었는지 검토하는 과정이다.

---

### [핵심]

검토 항목:

- form 태그 사용 여부
- label 연결 여부
- input name 설정
- button type 명시
- submit 이벤트 처리
- Enter 제출 가능 여부
- placeholder를 label 대체로 사용하지 않는가?
- 에러 메시지가 입력 필드와 연결되어 있는가?

---

### [예제]

```jsx
<form onSubmit={handleSubmit}>
  <label htmlFor="email">이메일</label>
  <input id="email" name="email" type="email" />

  <button type="submit">로그인</button>
</form>
```

---

### [FAQ]

Q. form 태그 없이 div로 만들어도 돼?

A.
가능은 하지만 Enter 제출, 접근성, 브라우저 기본 동작을 고려하면 form 태그가 적합하다.

Q. button type은 꼭 써야 해?

A.
form 내부에서는 반드시 명시하는 것이 좋다. 기본 submit 동작 때문에 의도치 않은 제출이 발생할 수 있다.

---

## 10.2 Validation Review

### [개념]

Validation Review는 사용자 입력값이 프론트엔드에서 적절히 검증되는지 확인하는 과정이다.

---

### [핵심]

검토 항목:

- required 필드 검증
- email 형식 검증
- password 길이 검증
- 숫자 범위 검증
- 파일 크기 / 확장자 검증
- 서버 validation error 표시
- submit 전 validation
- validation message 명확성

---

### [예제]

```js
if (!email) {
  setError("이메일을 입력해 주세요.");
  return;
}

if (!email.includes("@")) {
  setError("올바른 이메일 형식이 아닙니다.");
  return;
}
```

---

### [실무]

Validation은 두 단계로 본다.

```text
Frontend Validation
→ 빠른 사용자 피드백

Backend Validation
→ 최종 데이터 검증
```

프론트엔드 검증만 믿으면 안 된다.

---

### [FAQ]

Q. 프론트엔드 validation이 있으면 백엔드 validation은 없어도 돼?

A.
안 된다. 프론트엔드 검증은 우회 가능하므로 백엔드 검증이 반드시 필요하다.

Q. 서버 validation error도 화면에 보여줘야 해?

A.
보여줘야 한다. 중복 이메일, 권한 없음, 비밀번호 불일치 같은 서버 판단 결과는 사용자에게 안내해야 한다.

---

## 10.3 Form Submit Review

### [개념]

Form Submit Review는 폼 제출 흐름이 안정적으로 처리되는지 검토하는 과정이다.

---

### [핵심]

검토 항목:

- preventDefault 처리
- 중복 제출 방지
- 제출 중 버튼 disabled
- 성공 후 이동 또는 초기화
- 실패 후 입력 유지
- 에러 메시지 표시
- Loading 종료 보장
- 파일 업로드 진행 상태

---

### [예제]

```jsx
async function handleSubmit(event) {
  event.preventDefault();

  if (isSubmitting) return;

  setIsSubmitting(true);

  try {
    await submitForm(formValues);
    navigate("/success");
  } catch (error) {
    setError("저장에 실패했습니다.");
  } finally {
    setIsSubmitting(false);
  }
}
```

---

### [FAQ]

Q. 제출 버튼을 여러 번 누르면 어떻게 돼?

A.
중복 API 요청이나 중복 저장이 발생할 수 있다. 제출 중에는 버튼을 disabled 처리해야 한다.

Q. 제출 실패 시 입력값을 지워도 돼?

A.
권장하지 않는다. 사용자가 다시 입력하지 않도록 기존 입력값을 유지하는 것이 좋다.

---

# 11. Authentication Review Rules

## 11.1 Auth Flow Review

### [개념]

Auth Flow Review는 로그인, 로그아웃, 토큰 저장, 인증 만료, 권한별 접근이 올바르게 처리되는지 검토하는 과정이다.

---

### [핵심]

검토 항목:

- 로그인 성공 후 토큰 저장
- 로그아웃 시 토큰 제거
- 인증 필요한 API에 Authorization header 포함
- 401 발생 시 refresh 또는 로그인 이동
- 인증 필요한 페이지 보호
- 로그인 사용자가 로그인 페이지 접근 시 redirect
- 권한 없는 사용자의 UI 접근 제한
- 새로고침 후 인증 상태 복원

---

### [Flow]

```text
Login Submit
→ Auth API Request
→ Token Save
→ User State Update
→ Redirect
→ Authenticated API Request
→ 401 Handling
→ Logout
```

---

### [FAQ]

Q. 로그인 성공 후 토큰만 저장하면 끝이야?

A.
아니다. 사용자 상태 갱신, 인증 API header 설정, redirect, 만료 처리까지 확인해야 한다.

Q. 새로고침하면 로그인이 풀려?

A.
토큰 저장 방식과 인증 상태 복원 로직이 없으면 풀릴 수 있다.

Q. 로그아웃 시 무엇을 해야 해?

A.
토큰 제거, 사용자 상태 초기화, 필요 시 서버 로그아웃 API 호출, 로그인 페이지 이동을 처리한다.

---

## 11.2 Token Storage Review

### [개념]

Token Storage Review는 Access Token / Refresh Token을 어디에 저장하고 어떻게 사용하는지 검토하는 과정이다.

---

### [핵심]

저장 방식 비교:

| 방식            | 장점            | 단점                  |
| --------------- | --------------- | --------------------- |
| localStorage    | 구현 쉬움       | XSS에 취약            |
| sessionStorage  | 탭 종료 시 제거 | XSS에 취약            |
| memory          | 노출 감소       | 새로고침 시 사라짐    |
| httpOnly Cookie | JS 접근 불가    | CSRF / CORS 설정 필요 |

---

### [실무]

리뷰 기준:

```md
- [ ] 토큰 저장 위치가 프로젝트 보안 요구사항에 맞는가?
- [ ] 로그아웃 시 토큰이 제거되는가?
- [ ] 만료 토큰 처리 흐름이 있는가?
- [ ] Authorization header가 중복 또는 누락되지 않는가?
- [ ] 민감 정보가 console에 출력되지 않는가?
```

---

### [FAQ]

Q. JWT를 localStorage에 저장해도 돼?

A.
가능은 하지만 XSS 위험이 있다. 보안 요구사항이 높다면 httpOnly Cookie 방식도 검토해야 한다.

Q. 토큰을 console.log로 찍어도 돼?

A.
개발 중에도 권장하지 않는다. 운영 코드에 남으면 보안 위험이다.

---

## 11.3 Protected Route Review

### [개념]

Protected Route Review는 인증이 필요한 페이지에 비로그인 사용자가 접근하지 못하도록 처리했는지 검토하는 과정이다.

---

### [예제]

```jsx
function ProtectedRoute({ children }) {
  const { isLoggedIn } = useAuth();

  if (!isLoggedIn) {
    return <Navigate to="/login" replace />;
  }

  return children;
}
```

---

### [핵심]

검토 항목:

- 인증 필요 페이지 보호
- 비로그인 접근 시 로그인 이동
- 로그인 후 원래 페이지 복귀
- 권한별 접근 제한
- Loading 중 redirect 오동작 방지
- 서버 권한 검증과 병행

---

### [FAQ]

Q. 프론트에서 Protected Route만 있으면 보안이 충분해?

A.
아니다. 프론트엔드 보호는 UX 목적이고 실제 권한 검증은 백엔드에서 반드시 해야 한다.

Q. 인증 상태 확인 중인데 로그인 페이지로 튕겨?

A.
auth loading 상태를 고려하지 않으면 새로고침 직후 잘못 redirect될 수 있다.

---

# 12. Routing Review Rules

## 12.1 Route Structure Review

### [개념]

Route Structure Review는 페이지 경로가 명확하고 유지보수 가능한지 검토하는 과정이다.

---

### [핵심]

검토 항목:

- route path가 명확한가?
- dynamic route가 적절한가?
- 중첩 route 구조가 과하지 않은가?
- Not Found route가 있는가?
- 인증 route와 공개 route가 구분되는가?
- backend API path와 충돌하지 않는가?
- basename이 필요한 배포 환경인가?

---

### [예제]

```jsx
<Routes>
  <Route path="/" element={<MainPage />} />
  <Route path="/festivals" element={<FestivalListPage />} />
  <Route path="/festivals/:festivalId" element={<FestivalDetailPage />} />
  <Route path="/login" element={<LoginPage />} />
  <Route path="*" element={<NotFoundPage />} />
</Routes>
```

---

### [FAQ]

Q. NotFoundPage가 꼭 필요해?

A.
권장된다. 잘못된 URL에 대해 사용자가 이해할 수 있는 화면을 제공해야 한다.

Q. API 경로와 프론트 route가 같아도 돼?

A.
권장하지 않는다. API는 `/api` prefix로 분리하는 것이 안전하다.

---

## 12.2 Navigation Review

### [개념]

Navigation Review는 페이지 이동 방식이 SPA 특성과 사용자 경험에 맞는지 검토하는 과정이다.

---

### [핵심]

검토 항목:

- 내부 이동에 Link 또는 navigate 사용
- 외부 이동에는 a 태그 사용
- button과 link 역할 구분
- 뒤로가기 동작 자연스러움
- redirect 후 history 처리
- 로그인 후 이동 경로 적절성
- replace 사용 필요 여부

---

### [예제]

내부 이동:

```jsx
<Link to="/festivals">축제 목록</Link>
```

프로그래밍 방식 이동:

```jsx
navigate("/login", { replace: true });
```

외부 이동:

```jsx
<a href="https://example.com" target="_blank" rel="noreferrer">
  외부 사이트
</a>
```

---

### [FAQ]

Q. 내부 페이지 이동에 a 태그를 써도 돼?

A.
가능하지만 SPA에서는 전체 새로고침이 발생할 수 있으므로 React Router의 Link를 권장한다.

Q. 로그인 후 replace는 언제 써?

A.
뒤로가기로 로그인 페이지에 다시 돌아가는 것을 막고 싶을 때 사용할 수 있다.

---

# 13. Accessibility Review Rules

## 13.1 Accessibility Review

### [개념]

Accessibility Review는 다양한 사용자가 프론트엔드 화면을 사용할 수 있는지 검토하는 과정이다.

---

### [핵심]

검토 항목:

- Semantic HTML 사용
- heading 구조
- button / a 역할 구분
- input label 연결
- img alt 제공
- keyboard navigation
- focus style
- color contrast
- aria 사용 적절성
- modal focus trap
- error message role
- loading 상태 안내

---

### [Checklist]

```md
- [ ] h1, h2, h3 구조가 자연스러운가?
- [ ] 클릭 요소가 button 또는 a로 작성되었는가?
- [ ] input에 label이 연결되었는가?
- [ ] 이미지에 적절한 alt가 있는가?
- [ ] 키보드만으로 조작 가능한가?
- [ ] focus outline이 보이는가?
- [ ] 색상만으로 상태를 전달하지 않는가?
- [ ] modal 닫기와 focus 이동이 가능한가?
- [ ] error message가 screen reader에 전달되는가?
```

---

### [FAQ]

Q. 접근성 리뷰는 꼭 해야 해?

A.
해야 한다. 접근성은 품질, 사용성, SEO, 법적 기준과도 연결될 수 있다.

Q. div에 onClick을 쓰면 안 돼?

A.
버튼 역할이면 button을 사용하는 것이 좋다. div 클릭은 키보드 접근성과 의미 전달에 문제가 생기기 쉽다.

Q. aria를 많이 넣으면 좋아?

A.
아니다. Semantic HTML을 우선 사용하고 부족한 의미를 보완할 때만 aria를 사용한다.

---

## 13.2 Modal Accessibility Review

### [개념]

Modal Accessibility Review는 모달 UI가 키보드와 스크린 리더 환경에서도 안전하게 동작하는지 검토하는 과정이다.

---

### [핵심]

검토 항목:

- `role="dialog"` 또는 적절한 dialog 구조
- modal title 제공
- 배경 스크롤 방지
- ESC 닫기
- 닫기 버튼 제공
- focus trap
- 닫힌 후 이전 focus 복원
- overlay 클릭 닫기 정책 명확화

---

### [예제]

```jsx
<div role="dialog" aria-modal="true" aria-labelledby="modal-title">
  <h2 id="modal-title">리뷰 작성</h2>
  <button type="button" onClick={onClose}>
    닫기
  </button>
</div>
```

---

### [FAQ]

Q. Modal은 div로만 만들면 안 돼?

A.
가능하지만 접근성을 위해 dialog 역할, 제목 연결, focus 관리가 필요하다.

Q. 모달이 열렸을 때 focus는 어디로 가야 해?

A.
모달 내부의 첫 번째 조작 가능한 요소나 제목으로 이동하는 것이 좋다.

---

# 14. Styling Review Rules

## 14.1 Styling Consistency Review

### [개념]

Styling Consistency Review는 스타일 코드가 일관된 규칙으로 작성되었는지 검토하는 과정이다.

---

### [핵심]

검토 항목:

- className naming 일관성
- inline style 남용 여부
- 중복 CSS 여부
- 색상 하드코딩 여부
- spacing 값 일관성
- 반응형 breakpoint 일관성
- hover / active / disabled 상태
- dark mode 필요 여부
- CSS module / styled-components / Tailwind 사용 규칙 일관성

---

### [실무]

Review Agent는 스타일 도구 자체보다 일관성을 우선 본다.

```text
CSS Module을 쓰는 프로젝트
→ className 구조와 scope 확인

Styled Components를 쓰는 프로젝트
→ props 기반 스타일 과다 여부 확인

Tailwind를 쓰는 프로젝트
→ className 과도한 중복과 component 추출 여부 확인

Plain CSS를 쓰는 프로젝트
→ 전역 class 충돌과 naming 확인
```

---

### [FAQ]

Q. inline style은 무조건 나빠?

A.
무조건은 아니지만 반복되는 스타일이나 상태 스타일은 class 또는 styling system으로 분리하는 것이 좋다.

Q. 색상값을 직접 써도 돼?

A.
가능하지만 반복되는 색상은 design token 또는 CSS variable로 관리하는 것이 좋다.

---

## 14.2 Responsive Review

### [개념]

Responsive Review는 화면이 다양한 기기 크기에서 깨지지 않는지 검토하는 과정이다.

---

### [핵심]

검토 항목:

- 모바일 화면에서 가로 스크롤 없음
- 카드 / 리스트 줄바꿈 정상
- 이미지 크기 반응형
- font size 가독성
- 터치 영역 충분
- breakpoint 과다 생성 없음
- layout shift 최소화
- header / modal / table 모바일 대응

---

### [실무]

반응형 확인 기준:

```text
Mobile 360px
→ Tablet 768px
→ Desktop 1024px
→ Wide 1280px
```

대표 문제:

```text
고정 width
이미지 max-width 누락
flex-wrap 누락
table overflow 처리 누락
modal width 고정
button touch area 부족
```

---

### [FAQ]

Q. 반응형 리뷰에서 가장 먼저 볼 것은?

A.
모바일 화면에서 가로 스크롤이 생기는지, 주요 버튼과 텍스트가 사용 가능한지 확인한다.

Q. 모든 기기 사이즈를 다 맞춰야 해?

A.
모든 기기를 개별 대응하기보다 콘텐츠가 깨지는 지점을 기준으로 breakpoint를 설정한다.

---

# 15. TypeScript Review Rules

## 15.1 Type Safety Review

### [개념]

Type Safety Review는 TypeScript 타입이 실제 데이터 구조와 맞고, `any` 남용이 없는지 검토하는 과정이다.

---

### [핵심]

검토 항목:

- API Response 타입 정의
- Props 타입 정의
- Event 타입 정의
- nullable 처리
- optional field 처리
- `any` 남용 여부
- type assertion 남용 여부
- enum / union type 적절성
- generic 과도한 복잡성 여부

---

### [예제]

Props 타입:

```tsx
type FestivalCardProps = {
  festival: Festival;
  isFavorite: boolean;
  onFavoriteClick: (festivalId: number) => void;
};

function FestivalCard({
  festival,
  isFavorite,
  onFavoriteClick,
}: FestivalCardProps) {
  return (
    <article>
      <h2>{festival.title}</h2>
      <button type="button" onClick={() => onFavoriteClick(festival.id)}>
        {isFavorite ? "찜 해제" : "찜하기"}
      </button>
    </article>
  );
}
```

---

### [FAQ]

Q. any를 써도 돼?

A.
임시로는 가능하지만 최종 코드에서는 구체적인 타입으로 대체하는 것이 좋다.

Q. API 응답 타입은 꼭 만들어야 해?

A.
권장된다. 응답 구조가 명확해야 화면 코드와 API 변경 영향도를 줄일 수 있다.

Q. 타입 단언 as를 많이 써도 돼?

A.
남용하면 TypeScript의 안전성이 떨어진다. 실제 타입을 좁히는 방식이 더 좋다.

---

## 15.2 Null Undefined Review

### [개념]

Null Undefined Review는 값이 없을 수 있는 상황을 안전하게 처리하는지 검토하는 과정이다.

---

### [핵심]

검토 항목:

- 초기 데이터 null 처리
- optional chaining 사용 여부
- loading 전 데이터 접근 방지
- fallback UI 제공
- non-null assertion 남용 금지
- API optional field 대응

---

### [예제]

나쁜 예:

```tsx
return <h1>{festival.title}</h1>;
```

`festival`이 null일 수 있으면 오류가 발생한다.

좋은 예:

```tsx
if (!festival) {
  return <p>축제 정보를 찾을 수 없습니다.</p>;
}

return <h1>{festival.title}</h1>;
```

---

### [FAQ]

Q. Cannot read properties of undefined 오류는 왜 나?

A.
데이터가 로딩되기 전 undefined 또는 null 값에 접근했기 때문이다.

Q. optional chaining만 쓰면 충분해?

A.
항상 충분하지 않다. 사용자에게 보여줄 fallback UI도 필요하다.

---

# 16. Performance Review Rules

## 16.1 Rendering Performance Review

### [개념]

Rendering Performance Review는 불필요한 렌더링과 무거운 계산으로 인해 UI 성능이 저하되는지 검토하는 과정이다.

---

### [핵심]

검토 항목:

- list key 안정성
- 불필요한 state update
- 무거운 계산 반복
- 큰 리스트 렌더링
- inline object / function으로 인한 memo 무효화
- memoization 과다 또는 부족
- 이미지 최적화
- lazy loading 적용 필요 여부

---

### [예제]

나쁜 key:

```jsx
items.map((item, index) => <Item key={index} item={item} />);
```

좋은 key:

```jsx
items.map((item) => <Item key={item.id} item={item} />);
```

---

### [실무]

성능 최적화 우선순위:

```text
실제 느린지 확인
→ 불필요한 렌더링 확인
→ list key 확인
→ 큰 리스트 가상화 검토
→ 이미지 최적화
→ code splitting
→ memoization
```

---

### [FAQ]

Q. React.memo를 모든 컴포넌트에 써야 해?

A.
아니다. 실제 성능 문제가 있거나 props 안정성이 있는 경우에 사용한다.

Q. map에서 index를 key로 쓰면 안 돼?

A.
리스트 순서가 바뀌거나 삭제 / 추가가 발생하면 렌더링 버그가 생길 수 있다. 고유 id가 좋다.

---

## 16.2 Bundle Review

### [개념]

Bundle Review는 빌드 결과물의 크기와 초기 로딩 성능을 검토하는 과정이다.

---

### [핵심]

검토 항목:

- 큰 라이브러리 전체 import
- 사용하지 않는 의존성
- route-based lazy loading
- 이미지 파일 크기
- source map 공개 여부
- 중복 dependency
- 번들 분석 필요 여부

---

### [예제]

나쁜 예:

```js
import _ from "lodash";
```

좋은 예:

```js
import debounce from "lodash/debounce";
```

---

### [FAQ]

Q. 번들 크기는 코드 리뷰에서 봐야 해?

A.
운영 성능에 영향을 주므로 주요 라이브러리 추가나 초기 로딩이 느릴 때 확인해야 한다.

Q. lazy loading은 언제 리뷰해야 해?

A.
페이지 단위 코드가 커지거나 초기 화면과 관련 없는 기능이 번들에 포함될 때 검토한다.

---

# 17. Security Review Rules

## 17.1 Frontend Security Review

### [개념]

Frontend Security Review는 브라우저에 노출되는 코드 특성을 고려해 보안 위험을 줄이는 과정이다.

---

### [핵심]

검토 항목:

- Secret Key 노출 여부
- API Key 도메인 제한 여부
- 토큰 console 출력 여부
- dangerouslySetInnerHTML 사용 여부
- XSS 위험 입력 처리
- localStorage token 저장 위험
- 외부 링크 rel 설정
- 파일 업로드 확장자 / 크기 제한
- 권한 UI만 믿지 않는지
- 민감 정보 URL query 노출 여부

---

### [주의]

프론트엔드에 저장하면 안 되는 값:

```text
JWT_SECRET
DB_PASSWORD
TOSS_SECRET_KEY
OPENAI_API_KEY
AWS_SECRET_ACCESS_KEY
ADMIN_PASSWORD
PRIVATE_KEY
```

---

### [예제]

외부 링크:

```jsx
<a href="https://example.com" target="_blank" rel="noreferrer">
  외부 링크
</a>
```

---

### [FAQ]

Q. 프론트엔드에 API Secret을 넣어도 돼?

A.
안 된다. 브라우저 코드와 빌드 결과물에서 노출될 수 있다.

Q. Kakao JavaScript Key는 프론트엔드에 있어도 돼?

A.
브라우저에서 사용해야 하는 public key는 가능하지만 도메인 제한을 반드시 설정해야 한다.

Q. 권한 버튼을 숨기면 보안이 되는 거야?

A.
아니다. 프론트엔드 UI 제한은 UX 목적이고 실제 권한 검증은 백엔드에서 해야 한다.

---

## 17.2 XSS Review

### [개념]

XSS Review는 사용자 입력이나 외부 데이터를 HTML로 렌더링할 때 스크립트 실행 위험이 있는지 검토하는 과정이다.

---

### [핵심]

검토 항목:

- `dangerouslySetInnerHTML` 사용 여부
- 사용자 입력 HTML 렌더링 여부
- markdown 렌더링 sanitize 여부
- URL 입력 검증
- rich text editor 결과 처리
- 외부 API 응답 신뢰 여부

---

### [예제]

위험한 예:

```jsx
<div dangerouslySetInnerHTML={{ __html: userInput }} />
```

---

### [실무]

허용이 필요한 경우:

```text
HTML 렌더링 필요
→ sanitize 적용
→ 허용 tag 제한
→ script / event handler 제거
→ link protocol 검증
```

---

### [FAQ]

Q. dangerouslySetInnerHTML은 절대 쓰면 안 돼?

A.
절대 금지는 아니지만 사용자 입력이나 외부 데이터를 넣을 때는 sanitize가 반드시 필요하다.

Q. React는 XSS를 자동으로 막아줘?

A.
일반 문자열 렌더링은 escape하지만, dangerouslySetInnerHTML을 사용하면 개발자가 직접 책임져야 한다.

---

# 18. Testability Review Rules

## 18.1 Testability Review

### [개념]

Testability Review는 코드가 테스트하기 쉬운 구조인지 검토하는 과정이다.

---

### [핵심]

테스트하기 좋은 코드:

- UI와 로직이 적절히 분리됨
- API 호출이 mock 가능함
- side effect가 분리됨
- 입력과 출력이 명확함
- selector가 안정적임
- 접근성 기반 query 사용 가능
- 복잡한 로직이 pure function으로 분리됨

---

### [실무]

테스트 어려운 코드:

```text
컴포넌트 내부에 모든 로직 집중
직접 window.location 변경
API 호출 하드코딩
시간 / 랜덤 값 직접 사용
DOM 구조에 강하게 의존
```

개선 방향:

```text
API module 분리
Custom Hook 분리
Pure Function 분리
Dependency Injection 일부 적용
Role / Label 기반 테스트 가능 구조
```

---

### [FAQ]

Q. 테스트 코드가 없어도 testability를 리뷰해야 해?

A.
해야 한다. 테스트하기 어려운 코드는 유지보수와 리팩토링 비용이 커진다.

Q. 테스트용 id를 많이 넣어야 해?

A.
접근성 role, label, text로 찾을 수 있으면 우선 사용하고, 어려운 경우에 test id를 고려한다.

---

## 18.2 Unit and UI Test Review

### [개념]

Unit and UI Test Review는 주요 로직과 사용자 인터랙션이 테스트로 검증 가능한지 확인하는 과정이다.

---

### [핵심]

검토 대상:

- form validation
- button click
- API success state
- API error state
- loading state
- empty state
- protected route
- custom hook
- utility function
- conditional rendering

---

### [예제]

테스트 관점 checklist:

```md
- [ ] 정상 데이터 표시 테스트가 가능한가?
- [ ] 로딩 상태 테스트가 가능한가?
- [ ] 에러 상태 테스트가 가능한가?
- [ ] 빈 결과 상태 테스트가 가능한가?
- [ ] 사용자 입력 테스트가 가능한가?
- [ ] 제출 이벤트 테스트가 가능한가?
```

---

### [FAQ]

Q. 모든 컴포넌트를 테스트해야 해?

A.
아니다. 핵심 사용자 흐름, form, API 상태, 인증 흐름, 복잡한 로직을 우선한다.

Q. 단순 UI 컴포넌트도 테스트해야 해?

A.
재사용성이 높거나 조건부 렌더링이 있다면 테스트 가치가 있다.

---

# 19. Build Deploy Review Rules

## 19.1 Build Risk Review

### [개념]

Build Risk Review는 코드가 운영 빌드에서 실패하거나 배포 후 문제를 일으킬 수 있는지 검토하는 과정이다.

---

### [핵심]

검토 항목:

- `npm run build` 성공 여부
- TypeScript error 여부
- ESLint error 여부
- 환경 변수 누락
- localhost 하드코딩
- 파일명 대소문자 문제
- unused import 과다
- dynamic import 오류
- asset path 오류
- build output 경로 확인

---

### [실무]

배포 전 필수:

```bash
npm run build
```

가능하면 함께 확인:

```bash
npm run lint
npm test
```

---

### [FAQ]

Q. 개발 서버에서 잘 되면 build 확인 안 해도 돼?

A.
안 된다. 운영 빌드에서만 발생하는 타입, 경로, 환경 변수 문제가 있을 수 있다.

Q. Windows에서 되는데 서버에서 안 되는 이유는?

A.
Linux 서버는 파일명 대소문자를 구분하므로 import 경로 대소문자 문제가 발생할 수 있다.

---

## 19.2 Environment Review

### [개념]

Environment Review는 환경 변수와 운영 설정이 안전하고 올바르게 분리되었는지 검토하는 과정이다.

---

### [핵심]

검토 항목:

- `.env`에 secret 없음
- `.env.example` 제공
- Vite / CRA prefix 일치
- API Base URL 환경별 분리
- 운영 빌드에 localhost 없음
- public key 도메인 제한
- source map 공개 여부 판단
- runtime config 필요 여부

---

### [FAQ]

Q. 코드 리뷰에서 .env도 봐야 해?

A.
봐야 한다. API URL, Secret Key 노출, 빌드 오류의 주요 원인이 환경 변수다.

Q. 운영 빌드에 localhost가 있으면 안 돼?

A.
안 된다. 운영 사용자의 브라우저에서 localhost는 사용자 자신의 컴퓨터를 의미한다.

---

# 20. Code Smell Review Rules

## 20.1 Common Code Smells

### [개념]

Code Smell은 즉시 오류는 아니지만 유지보수성, 안정성, 확장성을 해치는 코드 징후다.

---

### [핵심]

Frontend Common Code Smell:

- 너무 큰 컴포넌트
- 중복된 API 호출 코드
- 중복된 validation 로직
- props drilling 과다
- any 남용
- useEffect 남용
- state 중복 저장
- magic number / magic string
- console.log 잔존
- 주석 처리된 코드 방치
- 임시 변수명
- inline style 남용
- 하드코딩 URL
- 에러 처리 누락
- loading 처리 누락
- empty state 누락
- key에 index 사용
- 조건부 hook 호출
- secret key 노출
- 접근성 누락

---

### [실무]

리뷰 코멘트 예:

```text
[Medium] 이 컴포넌트는 API 호출, Form 상태, Modal 상태를 모두 관리하고 있어 책임이 과합니다. API 로직은 custom hook으로 분리하는 것이 좋습니다.

[High] API 요청 실패 시 catch 처리가 없어 사용자가 실패 상태를 알 수 없습니다. Error State와 재시도 UI를 추가해야 합니다.

[Critical] 프론트엔드 환경 변수에 Secret Key가 포함되어 있습니다. 즉시 제거하고 백엔드로 이동해야 합니다.
```

---

### [FAQ]

Q. Code Smell은 반드시 수정해야 해?

A.
Critical / High 위험으로 이어지는 smell은 수정해야 한다. 나머지는 일정과 영향도에 따라 결정한다.

Q. console.log는 남겨도 돼?

A.
운영 코드에는 남기지 않는 것이 좋다. 특히 토큰, 사용자 정보, API 응답 전체 출력은 위험하다.

---

# 21. Pull Request Review Rules

## 21.1 PR Review Checklist

### [개념]

Pull Request Review는 변경된 코드가 병합 가능한 상태인지 확인하는 과정이다.

---

### [Checklist]

PR 리뷰 기본 체크리스트:

```md
- [ ] 요구사항을 만족하는가?
- [ ] 주요 사용자 흐름이 동작하는가?
- [ ] 컴포넌트 책임이 명확한가?
- [ ] props / state 구조가 적절한가?
- [ ] API 호출이 모듈화되어 있는가?
- [ ] loading / error / empty state가 있는가?
- [ ] form validation이 있는가?
- [ ] 인증 / 권한 처리가 맞는가?
- [ ] 접근성 기본 기준을 만족하는가?
- [ ] 반응형 화면이 깨지지 않는가?
- [ ] TypeScript 타입이 적절한가?
- [ ] secret key가 노출되지 않는가?
- [ ] localhost 하드코딩이 없는가?
- [ ] 테스트 가능성이 있는가?
- [ ] build가 성공하는가?
```

---

### [실무]

PR 리뷰 순서:

```text
Diff Overview
→ Requirement Match
→ Critical Risk Check
→ Component Structure
→ State / API Flow
→ UX State
→ Accessibility
→ Security
→ Build Risk
→ Final Decision
```

---

### [FAQ]

Q. PR에서 모든 파일을 순서대로 보면 돼?

A.
가능하지만 먼저 변경 목적과 주요 흐름을 파악한 뒤 위험도가 높은 파일부터 보는 것이 좋다.

Q. PR 리뷰에서 가장 먼저 찾을 문제는?

A.
빌드 실패, 인증 오류, API 오류, secret 노출, 사용자 흐름 중단 같은 Critical / High 문제다.

---

## 21.2 Review Comment Rules

### [개념]

Review Comment Rules는 코드 리뷰 코멘트를 명확하고 실행 가능하게 작성하기 위한 기준이다.

---

### [핵심]

좋은 리뷰 코멘트:

- 문제 위치 명확
- 왜 문제인지 설명
- 수정 방향 제안
- 우선순위 표시
- 비난 없이 작성
- 선택 개선과 필수 수정 구분

---

### [예제]

나쁜 코멘트:

```text
이거 별로임.
```

좋은 코멘트:

```text
[High] API 실패 시 catch 처리가 없어 사용자가 빈 화면을 보게 됩니다. Error State를 추가하고 재시도 버튼을 제공하는 것이 좋습니다.
```

---

### [FAQ]

Q. 리뷰 코멘트는 짧게만 쓰면 돼?

A.
짧되 문제와 수정 방향이 명확해야 한다.

Q. 선택 사항도 리뷰 코멘트로 남겨도 돼?

A.
가능하다. 다만 Suggestion으로 표시해 필수 수정과 구분해야 한다.

---

# 22. Agent Collaboration Rules

## 22.1 PM Agent Review Role

### [개념]

PM Agent는 Code Review 결과를 기능 완료 여부와 일정 판단에 활용한다.

---

### [핵심]

PM Agent 판단 기준:

- 요구사항 충족 여부
- 주요 기능 동작 여부
- Critical / High Issue 존재 여부
- 배포 가능 여부
- 사용자 시나리오 통과 여부
- 일정 내 수정 가능성

---

### [실무]

PM Agent Output:

```text
Feature Status: Complete / Partial / Blocked
Risk Level: Low / Medium / High
Required Fixes: Critical / High 중심
Release Decision: Go / No-Go
```

---

### [FAQ]

Q. PM Agent는 코드 세부 구현을 봐야 해?

A.
세부 구현 전체보다 요구사항 충족, 위험도, 배포 가능성, 수정 우선순위를 봐야 한다.

Q. Critical Issue가 있으면 완료로 봐도 돼?

A.
안 된다. Critical Issue가 있으면 Blocked 또는 Changes Requested로 판단해야 한다.

---

## 22.2 Frontend Agent Review Role

### [개념]

Frontend Agent는 코드 생성뿐 아니라 자체 점검을 수행해야 한다.

---

### [핵심]

Frontend Agent Self Review:

```md
- [ ] 요구사항을 만족하는가?
- [ ] 컴포넌트가 과도하게 커지지 않았는가?
- [ ] API 요청이 중복되지 않는가?
- [ ] loading / error / empty state가 있는가?
- [ ] form validation이 있는가?
- [ ] 접근성 기본을 지켰는가?
- [ ] 반응형을 고려했는가?
- [ ] build를 깨뜨리지 않는가?
```

---

### [실무]

Frontend Agent는 코드 생성 후 다음을 함께 제공하면 좋다.

```text
Implemented Files
Review Notes
Known Limitations
Test Checklist
Build Check
```

---

### [FAQ]

Q. Frontend Agent가 만든 코드는 Review Agent가 다시 봐야 해?

A.
봐야 한다. 생성 Agent와 검토 Agent의 역할을 분리해야 품질이 높아진다.

Q. Frontend Agent가 self review를 하면 Review Agent가 필요 없어?

A.
아니다. Self Review는 1차 점검이고 Review Agent는 독립 검증 역할이다.

---

## 22.3 Review Agent Role

### [개념]

Review Agent는 코드 품질과 운영 위험을 독립적으로 검토하는 Agent다.

---

### [핵심]

Review Agent 주요 역할:

- 변경 코드 분석
- 요구사항 충족 여부 확인
- Critical / High Issue 탐지
- 코드 품질 평가
- UX 상태 검토
- 접근성 검토
- 보안 위험 검토
- 테스트 가능성 검토
- 배포 가능성 판단
- 최종 승인 여부 결정

---

### [실무]

Review Agent Final Output:

```md
## Final Decision

CHANGES REQUESTED

## Reason

- [High] 로그인 실패 시 에러 메시지가 표시되지 않음
- [High] API URL이 localhost로 하드코딩되어 있음
- [Medium] FestivalDetailPage가 너무 많은 책임을 가짐

## Required Fixes

1. 로그인 실패 Error State 추가
2. API Base URL 환경 변수화
3. 데이터 조회 로직을 custom hook으로 분리
```

---

### [FAQ]

Q. Review Agent는 코드 수정을 직접 해야 해?

A.
상황에 따라 수정안을 제시하거나 패치 방향을 줄 수 있지만, 핵심 역할은 독립 검토와 승인 판단이다.

Q. Review Agent는 사소한 스타일도 봐야 해?

A.
보되 Critical / High 문제를 우선해야 한다.

---

# 23. Common Review Mistakes

## 23.1 Reviewer Mistakes

### [개념]

Reviewer Mistakes는 코드 리뷰를 수행하는 Agent가 자주 범하는 잘못된 판단이다.

---

### [핵심]

피해야 할 리뷰 방식:

- 취향 위주 리뷰
- 사소한 naming만 지적
- 요구사항 확인 없이 코드만 봄
- UI 동작 흐름 미검토
- API 실패 상황 미검토
- 접근성 무시
- 보안 키 노출 무시
- 빌드 가능성 미확인
- 테스트 가능성 미검토
- 모든 문제를 같은 우선순위로 표시
- 수정 방향 없는 지적
- 과도한 리팩토링 요구

---

### [실무]

좋은 리뷰 기준:

```text
Requirement First
→ Critical Risk First
→ User Flow
→ Maintainability
→ Accessibility
→ Performance
→ Suggestions Last
```

---

### [FAQ]

Q. 코드 리뷰에서 개인 취향을 말해도 돼?

A.
가능하지만 필수 수정처럼 말하면 안 된다. 취향성 의견은 Suggestion으로 분리해야 한다.

Q. 리뷰에서 리팩토링을 많이 요구해도 돼?

A.
일정과 영향도를 고려해야 한다. Critical 기능 수정이 우선이다.

---

# 24. Common Frontend Issues

## 24.1 Frequent Issues

### [개념]

Frontend Code Review에서는 반복적으로 발생하는 실무 문제를 빠르게 탐지해야 한다.

---

### [핵심]

자주 발생하는 문제:

- API URL localhost 하드코딩
- loading 없는 API 호출
- catch 없는 API 호출
- 빈 배열 화면 처리 없음
- form 중복 제출 가능
- button type 누락
- label 없는 input
- div onClick 사용
- key index 사용
- useEffect dependency 누락
- 조건부 hook 호출
- props drilling 과다
- any 남용
- null 접근 오류
- token console 출력
- secret key 노출
- 반응형 깨짐
- image alt 누락
- NotFound route 없음
- Protected Route 누락
- build 실패 가능 import 경로

---

### [Troubleshooting]

문제별 빠른 판단:

```text
흰 화면
→ null 접근 / asset 404 / runtime error 확인

API 실패
→ baseURL / CORS / token / status code 확인

로그인 실패
→ token 저장 / header / cookie / 401 처리 확인

모바일 깨짐
→ fixed width / overflow / image size 확인

빌드 실패
→ TypeScript / import path / env / dependency 확인
```

---

### [FAQ]

Q. Review Agent가 가장 자주 찾아야 할 문제는?

A.
API 실패 처리 누락, loading / error / empty state 누락, 인증 처리 누락, 환경 변수 문제, 접근성 기본 누락이다.

Q. 프론트엔드 버그는 대부분 어디서 나?

A.
상태 동기화, 비동기 API 처리, 인증 만료, 라우팅, 환경 변수, null 데이터 접근에서 자주 발생한다.

---

# 25. Final Review Checklist

## 25.1 Full Checklist

### [Checklist]

최종 Frontend Code Review Checklist:

```md
## Requirement

- [ ] 요구사항을 만족하는가?
- [ ] 주요 사용자 흐름이 끊기지 않는가?
- [ ] 성공 / 실패 / 빈 상태가 모두 처리되는가?

## Component

- [ ] 컴포넌트 책임이 명확한가?
- [ ] 컴포넌트 이름이 역할을 표현하는가?
- [ ] props가 과도하지 않은가?
- [ ] UI와 비즈니스 로직이 과하게 섞이지 않았는가?

## State

- [ ] state 위치가 적절한가?
- [ ] 중복 state가 없는가?
- [ ] 불변성 원칙을 지키는가?
- [ ] 전역 상태 남용이 없는가?

## Hooks

- [ ] Hook 호출 규칙을 지키는가?
- [ ] useEffect dependency가 적절한가?
- [ ] 불필요한 useEffect가 없는가?
- [ ] cleanup이 필요한 effect에 cleanup이 있는가?

## API

- [ ] API module이 분리되어 있는가?
- [ ] baseURL이 환경 변수로 관리되는가?
- [ ] API 실패 처리가 있는가?
- [ ] 중복 요청 위험이 없는가?
- [ ] 인증 header 처리가 일관적인가?

## UX State

- [ ] Loading State가 있는가?
- [ ] Error State가 있는가?
- [ ] Empty State가 있는가?
- [ ] 중복 제출이 방지되는가?

## Form

- [ ] form 구조가 적절한가?
- [ ] label이 연결되어 있는가?
- [ ] button type이 명시되어 있는가?
- [ ] validation이 있는가?
- [ ] 서버 validation error를 표시하는가?

## Auth

- [ ] 로그인 흐름이 완성되어 있는가?
- [ ] 로그아웃 처리가 완전한가?
- [ ] Protected Route가 있는가?
- [ ] 401 처리 흐름이 있는가?
- [ ] 토큰 저장 방식이 적절한가?

## Routing

- [ ] route path가 명확한가?
- [ ] NotFound route가 있는가?
- [ ] 내부 이동에 Link / navigate를 사용하는가?
- [ ] API path와 route path가 충돌하지 않는가?

## Accessibility

- [ ] Semantic HTML을 사용하는가?
- [ ] heading 구조가 적절한가?
- [ ] input label이 있는가?
- [ ] image alt가 있는가?
- [ ] keyboard navigation이 가능한가?
- [ ] focus style이 보이는가?

## Styling

- [ ] 스타일 naming이 일관적인가?
- [ ] inline style 남용이 없는가?
- [ ] 반응형이 깨지지 않는가?
- [ ] 색상 / spacing이 일관적인가?

## TypeScript

- [ ] props type이 명확한가?
- [ ] API response type이 있는가?
- [ ] any 남용이 없는가?
- [ ] null / undefined 처리가 안전한가?

## Performance

- [ ] list key가 안정적인가?
- [ ] 불필요한 렌더링이 없는가?
- [ ] 큰 리스트 / 이미지 최적화가 필요한가?
- [ ] bundle size 위험이 없는가?

## Security

- [ ] secret key가 노출되지 않는가?
- [ ] token console 출력이 없는가?
- [ ] dangerouslySetInnerHTML 사용이 안전한가?
- [ ] 외부 링크 rel 설정이 있는가?

## Build Deploy

- [ ] npm run build가 성공하는가?
- [ ] localhost 하드코딩이 없는가?
- [ ] 환경 변수가 올바른가?
- [ ] 파일명 대소문자 문제가 없는가?
- [ ] 배포 후 API URL이 정상인가?

## Testability

- [ ] 주요 흐름 테스트가 가능한가?
- [ ] API mock이 가능한가?
- [ ] 복잡한 로직이 분리되어 있는가?
- [ ] loading / error / empty state 테스트가 가능한가?
```

---

### [FAQ]

Q. 이 체크리스트를 매번 전부 써야 해?

A.
변경 범위에 따라 선택 적용할 수 있다. 다만 Critical / High 위험 항목은 항상 확인해야 한다.

Q. 최종 승인 기준은 뭐야?

A.
Critical / High 문제가 없고, 주요 사용자 흐름과 build가 정상이어야 한다.

---

# 26. Final Goal

## 26.1 Domain Final Goal

### [개념]

Frontend Code Review Domain Rules의 최종 목적은 Frontend Agent가 생성한 코드나 사용자가 작성한 프론트엔드 코드를 Review Agent가 안정적으로 검토하고, PM Agent가 기능 완료와 배포 가능 여부를 판단할 수 있도록 하는 것이다.

---

### [핵심]

최종 수행 가능 작업:

- 요구사항 충족 여부 검토
- React Component 구조 검토
- Props / State 설계 검토
- useEffect / Hook 사용 검토
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

---

### [실무]

최종 Agent Flow:

```text
Code Review Request
→ Requirement Match
→ Critical Risk Scan
→ Component Review
→ State Review
→ API Review
→ UX State Review
→ Auth Review
→ Accessibility Review
→ Security Review
→ Build Review
→ Testability Review
→ Final Decision
```

---

### [FAQ]

Q. Frontend Code Review 문서의 최종 목적은 뭐야?

A.
Frontend Agent / Review Agent / PM Agent가 코드 품질과 배포 가능성을 일관되게 판단하도록 만드는 것이다.

Q. 이 문서 다음에는 어떤 Domain Rules가 이어져야 해?

A.
Styling Architecture Domain Rules와 Design System Domain Rules가 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. Frontend Code Review 문서는 왜 필요해?

A.
Frontend Agent / Review Agent / PM Agent가 프론트엔드 코드 품질, 안정성, 유지보수성, 배포 가능성을 판단하기 위해 필요하다.

Q. 프론트엔드 코드 리뷰에서 가장 중요한 기준은 뭐야?

A.
요구사항 충족, 사용자 흐름, API 안정성, Error / Loading / Empty 처리, 인증, 접근성, 빌드 가능성이다.

Q. 코드 리뷰에서 문법만 보면 돼?

A.
아니다. 구조, 상태, API, UX, 접근성, 보안, 성능, 테스트 가능성을 함께 봐야 한다.

Q. Review Agent는 어떤 순서로 리뷰해야 해?

A.
요구사항 확인 → Critical 위험 확인 → 컴포넌트 구조 → 상태 → API → UX 상태 → 인증 → 접근성 → 보안 → 빌드 검토 순서가 좋다.

Q. 코드 리뷰 우선순위는 어떻게 나눠?

A.
Critical, High, Medium, Low, Suggestion으로 나눈다.

Q. Critical Issue는 뭐야?

A.
빌드 실패, 로그인 불가, 핵심 기능 미동작, Secret Key 노출처럼 즉시 수정이 필요한 문제다.

Q. High Issue는 뭐야?

A.
API 실패 미처리, 인증 체크 누락, 주요 사용자 흐름 오류처럼 운영 위험이 큰 문제다.

Q. Review 결과는 어떤 형식이 좋아?

A.
Summary, Critical Issues, High Issues, Medium Issues, Low Issues, Suggestions, Checklist, Final Decision 형식이 좋다.

Q. Final Decision은 뭐가 있어?

A.
APPROVED, APPROVED WITH COMMENTS, CHANGES REQUESTED, BLOCKED를 사용할 수 있다.

Q. BLOCKED는 언제 사용해?

A.
빌드 실패, 보안 키 노출, 핵심 기능 실패처럼 진행을 막아야 할 때 사용한다.

Q. 요구사항 리뷰는 왜 필요해?

A.
코드가 존재해도 사용자의 실제 요구사항과 사용자 흐름을 만족하지 못하면 완료가 아니기 때문이다.

Q. UI만 보이면 기능 완료야?

A.
아니다. 사용자 행동, API 연동, 오류 처리, 권한 처리까지 확인해야 한다.

Q. User Flow Review는 뭐야?

A.
사용자가 페이지 진입부터 입력, 제출, 결과 확인, 오류 복구까지 자연스럽게 사용할 수 있는지 검토하는 것이다.

Q. 컴포넌트 책임 리뷰는 뭐야?

A.
컴포넌트가 하나의 명확한 역할을 갖고 있는지, 너무 많은 책임을 갖지 않는지 검토하는 것이다.

Q. 컴포넌트가 너무 크면 무조건 문제야?

A.
줄 수만으로 판단하지 않고 API, Form, Modal, 상태, 라우팅 등 여러 책임이 섞였는지 본다.

Q. Page Component 역할은 뭐야?

A.
페이지 단위 데이터 조회, 화면 조립, route params 처리 같은 역할을 담당한다.

Q. Presentational Component는 뭐야?

A.
props를 받아 UI를 표시하는 컴포넌트로, 복잡한 데이터 조회나 비즈니스 로직을 갖지 않는 것이 좋다.

Q. 컴포넌트 이름은 어떻게 지어야 해?

A.
FestivalCard, LoginForm, ReviewModal처럼 도메인과 역할이 드러나게 짓는다.

Q. props 리뷰에서 뭘 봐야 해?

A.
props 이름, 개수, optional 처리, event handler naming, boolean props 의미, props drilling을 확인한다.

Q. event handler props 이름은 어떻게 짓는 게 좋아?

A.
onClick, onSubmit, onClose, onFavoriteClick처럼 `on`으로 시작하는 이름이 좋다.

Q. 내부 handler 이름은 어떻게 짓는 게 좋아?

A.
handleClick, handleSubmit, handleClose처럼 `handle`로 시작하는 이름이 좋다.

Q. boolean props 이름은 어떻게 지어야 해?

A.
isOpen, isLoading, hasError, canSubmit처럼 true / false 의미가 드러나게 작성한다.

Q. state 위치는 어떻게 정해?

A.
한 컴포넌트에서만 쓰면 local state, 여러 페이지에서 공유하면 global state, 서버 데이터는 server state 도구를 고려한다.

Q. 모든 상태를 전역 store에 넣어도 돼?

A.
권장하지 않는다. 컴포넌트 내부에서만 쓰는 상태는 local state가 더 단순하다.

Q. 검색어는 state에 둬야 해 URL에 둬야 해?

A.
공유, 새로고침 유지, 뒤로가기 지원이 필요하면 URL query params가 좋다.

Q. 중복 state는 왜 문제야?

A.
같은 의미의 데이터가 여러 곳에 저장되면 동기화 오류가 생길 수 있다.

Q. 파생 값은 state로 저장해야 해?

A.
대부분 기존 state에서 계산하는 것이 좋다. 복잡한 계산은 useMemo를 고려한다.

Q. state 배열을 push로 수정해도 돼?

A.
권장하지 않는다. 새 배열을 만들어 setState해야 React가 변경을 안정적으로 감지한다.

Q. useEffect 리뷰에서 가장 중요한 것은?

A.
dependency array, 무한 루프 가능성, cleanup 필요 여부, 불필요한 effect 여부다.

Q. useEffect dependency warning은 무시해도 돼?

A.
권장하지 않는다. 의존성 누락은 stale closure와 예측 어려운 버그를 만들 수 있다.

Q. props를 state로 복사하려고 useEffect를 써도 돼?

A.
대부분 불필요하다. 특별한 초기화 목적이 아니라면 props를 직접 사용하거나 파생 값으로 계산한다.

Q. 조건문 안에서 Hook을 호출해도 돼?

A.
안 된다. Hook 호출 순서가 렌더링마다 달라질 수 있다.

Q. 조건이 있을 때 useEffect는 어떻게 써?

A.
Hook은 최상위에서 호출하고 Hook 내부에서 조건을 처리한다.

Q. Custom Hook은 언제 만들어?

A.
여러 컴포넌트에서 반복되는 상태 로직, API 호출, modal 제어, form 로직을 분리할 때 만든다.

Q. Custom Hook 이름은 꼭 use로 시작해야 해?

A.
그렇다. React Hook 규칙과 lint 검사를 위해 use prefix가 필요하다.

Q. API 호출 코드는 어디에 두는 게 좋아?

A.
컴포넌트에 직접 흩뿌리기보다 api module이나 custom hook으로 분리하는 것이 좋다.

Q. API 함수 이름은 어떻게 짓는 게 좋아?

A.
getFestivalDetail, createReview, deleteFavorite처럼 동작과 도메인이 드러나야 한다.

Q. API 에러는 console.log만 해도 돼?

A.
안 된다. 사용자에게 에러 메시지와 복구 방법을 제공해야 한다.

Q. 401 에러는 어떻게 처리해야 해?

A.
인증 만료로 보고 refresh token 처리 또는 로그인 페이지 이동을 고려한다.

Q. 404는 항상 에러야?

A.
상황에 따라 Not Found 상태로 사용자에게 안내해야 하는 정상 흐름일 수 있다.

Q. API가 두 번 호출되는 이유는?

A.
useEffect dependency 오류, React StrictMode, 중복 mount, submit 중복 클릭, cache 미사용이 원인일 수 있다.

Q. React StrictMode 때문에 API가 두 번 호출될 수 있어?

A.
개발 환경에서는 side effect 검출을 위해 일부 로직이 두 번 실행될 수 있다.

Q. Loading State는 왜 필요해?

A.
API 요청 중 사용자가 화면이 멈춘 것으로 오해하지 않게 하기 위해 필요하다.

Q. 제출 중 버튼 disabled는 왜 필요해?

A.
중복 제출과 중복 API 요청을 막기 위해 필요하다.

Q. Error State는 어떻게 만들어야 해?

A.
실패 이유를 사용자 친화적으로 설명하고, 가능하면 재시도나 복구 행동을 제공해야 한다.

Q. Empty State는 뭐야?

A.
요청은 성공했지만 표시할 데이터가 없는 상태를 사용자에게 안내하는 UI다.

Q. 빈 화면이면 안 돼?

A.
안 된다. 사용자는 오류인지 결과가 없는지 알 수 없다.

Q. Form 리뷰에서 뭘 봐야 해?

A.
form 태그, label 연결, input name, button type, validation, submit 처리, 에러 메시지를 확인한다.

Q. button type은 왜 명시해야 해?

A.
form 내부에서 기본 submit 동작 때문에 의도치 않은 제출이 발생할 수 있기 때문이다.

Q. 프론트엔드 validation만 있으면 충분해?

A.
아니다. 프론트엔드 검증은 우회 가능하므로 백엔드 validation이 반드시 필요하다.

Q. 서버 validation error도 화면에 보여줘야 해?

A.
보여줘야 한다. 중복 이메일, 권한 없음, 비밀번호 불일치 같은 서버 판단 결과는 사용자에게 필요하다.

Q. 폼 제출 실패 시 입력값을 지워도 돼?

A.
권장하지 않는다. 사용자가 다시 입력하지 않도록 기존 입력값을 유지하는 것이 좋다.

Q. 로그인 흐름 리뷰에서 뭘 봐야 해?

A.
로그인 API, 토큰 저장, 사용자 상태 갱신, 인증 header, redirect, 401 처리, 로그아웃 처리를 확인한다.

Q. 새로고침하면 로그인이 풀리는 이유는?

A.
토큰 저장 방식과 인증 상태 복원 로직이 없기 때문일 수 있다.

Q. 로그아웃 시 무엇을 해야 해?

A.
토큰 제거, 사용자 상태 초기화, 서버 로그아웃 API 호출, 로그인 페이지 이동을 처리한다.

Q. JWT를 localStorage에 저장해도 돼?

A.
가능은 하지만 XSS 위험이 있다. 보안 요구사항이 높다면 httpOnly Cookie 방식도 검토한다.

Q. 토큰을 console.log로 찍어도 돼?

A.
권장하지 않는다. 운영 코드에 남으면 보안 위험이다.

Q. Protected Route만 있으면 보안이 충분해?

A.
아니다. 프론트엔드 route 보호는 UX 목적이고 실제 권한 검증은 백엔드에서 해야 한다.

Q. 인증 확인 중 로그인 페이지로 튕기는 이유는?

A.
auth loading 상태를 고려하지 않으면 새로고침 직후 잘못 redirect될 수 있다.

Q. NotFoundPage는 꼭 필요해?

A.
권장된다. 잘못된 URL에 대해 사용자가 이해할 수 있는 화면을 제공해야 한다.

Q. 내부 이동에 a 태그를 써도 돼?

A.
SPA에서는 전체 새로고침이 발생할 수 있으므로 React Router의 Link를 권장한다.

Q. 외부 링크에는 무엇을 확인해야 해?

A.
target blank 사용 시 rel="noreferrer" 또는 rel="noopener noreferrer" 설정을 확인한다.

Q. 접근성 리뷰에서 가장 중요한 것은?

A.
Semantic HTML, heading 구조, label, alt, keyboard navigation, focus style이다.

Q. div에 onClick을 써도 돼?

A.
버튼 역할이면 button을 사용하는 것이 좋다. div 클릭은 키보드 접근성 문제가 생기기 쉽다.

Q. aria를 많이 넣으면 접근성이 좋아져?

A.
아니다. Semantic HTML을 우선 사용하고 부족한 의미를 보완할 때만 aria를 사용한다.

Q. Modal 접근성에서는 뭘 봐야 해?

A.
dialog 역할, 제목 연결, focus trap, ESC 닫기, 닫기 버튼, focus 복원을 확인한다.

Q. Styling 리뷰에서는 뭘 봐야 해?

A.
naming, 중복 CSS, inline style 남용, 색상 하드코딩, 반응형, hover / disabled 상태를 확인한다.

Q. inline style은 무조건 나빠?

A.
무조건은 아니지만 반복되는 스타일과 상태 스타일은 class나 styling system으로 분리하는 것이 좋다.

Q. 반응형 리뷰에서 가장 먼저 볼 것은?

A.
모바일 화면에서 가로 스크롤이 생기는지, 버튼과 텍스트가 사용 가능한지 확인한다.

Q. any를 써도 돼?

A.
임시로는 가능하지만 최종 코드에서는 구체적인 타입으로 대체하는 것이 좋다.

Q. API 응답 타입은 꼭 필요해?

A.
권장된다. 응답 구조가 명확해야 화면 코드와 API 변경 영향도를 줄일 수 있다.

Q. Cannot read properties of undefined 오류는 왜 나?

A.
데이터가 로딩되기 전 undefined 또는 null 값에 접근했기 때문이다.

Q. optional chaining만 쓰면 충분해?

A.
항상 충분하지 않다. 사용자에게 보여줄 fallback UI도 필요하다.

Q. React.memo를 모든 컴포넌트에 써야 해?

A.
아니다. 실제 성능 문제가 있거나 props 안정성이 있는 경우에 사용한다.

Q. map에서 index를 key로 써도 돼?

A.
리스트 순서가 바뀌거나 삭제 / 추가가 발생하면 렌더링 버그가 생길 수 있다. 고유 id가 좋다.

Q. 번들 크기도 코드 리뷰에서 봐야 해?

A.
운영 성능에 영향을 주므로 큰 라이브러리 추가나 초기 로딩 문제가 있을 때 확인해야 한다.

Q. Secret Key를 프론트엔드에 넣어도 돼?

A.
안 된다. 브라우저 코드와 빌드 결과물에서 노출될 수 있다.

Q. Kakao JavaScript Key는 프론트엔드에 있어도 돼?

A.
브라우저에서 사용해야 하는 public key는 가능하지만 도메인 제한을 반드시 설정해야 한다.

Q. 권한 버튼을 숨기면 보안이 되는 거야?

A.
아니다. UI 제한은 UX 목적이고 실제 권한 검증은 백엔드에서 해야 한다.

Q. dangerouslySetInnerHTML은 절대 쓰면 안 돼?

A.
절대 금지는 아니지만 사용자 입력이나 외부 데이터를 넣을 때 sanitize가 반드시 필요하다.

Q. 테스트 가능성은 왜 리뷰해야 해?

A.
테스트하기 어려운 코드는 유지보수와 리팩토링 비용이 커진다.

Q. 모든 컴포넌트를 테스트해야 해?

A.
아니다. 핵심 사용자 흐름, form, API 상태, 인증 흐름, 복잡한 로직을 우선한다.

Q. npm run build는 리뷰에서 꼭 확인해야 해?

A.
그렇다. 개발 서버에서 정상이어도 운영 빌드에서 실패할 수 있다.

Q. 운영 코드에 localhost가 있으면 왜 문제야?

A.
운영 사용자의 브라우저에서 localhost는 사용자 자신의 컴퓨터를 의미하기 때문이다.

Q. Windows에서는 되는데 Linux 배포에서 import 에러가 나는 이유는?

A.
Linux는 파일명 대소문자를 구분하므로 import 경로 대소문자 문제가 발생할 수 있다.

Q. Code Smell은 뭐야?

A.
즉시 오류는 아니지만 유지보수성, 안정성, 확장성을 해치는 코드 징후다.

Q. 프론트엔드에서 자주 나오는 Code Smell은 뭐야?

A.
큰 컴포넌트, useEffect 남용, any 남용, loading / error 누락, API 중복, props drilling, hardcoding이 많다.

Q. console.log는 남겨도 돼?

A.
운영 코드에는 남기지 않는 것이 좋다. 특히 토큰, 사용자 정보, API 응답 전체 출력은 위험하다.

Q. PR 리뷰에서 가장 먼저 볼 것은?

A.
요구사항 충족과 Critical / High 위험 요소를 먼저 확인한다.

Q. 좋은 리뷰 코멘트는 어떻게 써?

A.
문제 위치, 이유, 수정 방향, 우선순위를 명확하게 작성한다.

Q. 취향성 리뷰는 어떻게 남겨?

A.
필수 수정처럼 말하지 말고 Suggestion으로 구분한다.

Q. PM Agent는 코드 리뷰 결과를 어떻게 써?

A.
기능 완료 여부, 위험도, 배포 가능성, 수정 우선순위를 판단하는 데 사용한다.

Q. Frontend Agent도 self review를 해야 해?

A.
해야 한다. 코드 생성 후 요구사항, 상태, API, UX, 접근성, build 가능성을 1차 점검해야 한다.

Q. Review Agent의 최종 역할은 뭐야?

A.
코드 품질과 운영 위험을 독립적으로 검토하고 승인 여부를 결정하는 것이다.

Q. Frontend Code Review 문서 다음은 뭐야?

A.
Styling Architecture Domain Rules와 Design System Domain Rules로 이어지는 것이 좋다.
