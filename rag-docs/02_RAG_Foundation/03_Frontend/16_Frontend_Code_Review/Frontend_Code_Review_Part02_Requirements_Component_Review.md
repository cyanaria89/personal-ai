# Frontend Code Review Part02 - Requirements and Component Review

---

# 1. Requirements Review Rules

## 1.1 Requirement Match Review

### [개념]

Requirement Match Review는 프론트엔드 구현 코드가 사용자의 요구사항과 실제 기능 목적을 만족하는지 검토하는 과정이다.

Frontend Code Review에서 요구사항 검토는 가장 먼저 수행해야 한다.

코드 품질이 좋아도 요구사항을 만족하지 못하면 기능 완료로 판단할 수 없다.

---

### [핵심]

Requirement Match Review 확인 항목:

- 요구된 화면이 구현되었는가?
- 요구된 사용자 행동이 동작하는가?
- 필수 UI 요소가 존재하는가?
- 필수 API가 연결되었는가?
- 성공 상태가 표시되는가?
- 실패 상태가 표시되는가?
- 빈 결과 상태가 표시되는가?
- 권한별 접근이 반영되었는가?
- 반응형 요구사항이 반영되었는가?
- 제출 / 저장 / 수정 / 삭제 흐름이 완성되었는가?
- 요구사항과 다른 임의 기능이 추가되지 않았는가?
- 요구사항에서 빠진 기능이 없는가?

---

### [실무]

Requirement Match Review Flow:

```text
User Requirement
→ Feature Checklist
→ UI Element Check
→ User Action Check
→ API Flow Check
→ State Feedback Check
→ Edge Case Check
→ Review Decision
```

예시 요구사항:

```text
축제 검색 기능 구현
```

검토 항목:

```md
- [ ] 검색 input이 있는가?
- [ ] 검색 버튼이 있는가?
- [ ] Enter 제출이 가능한가?
- [ ] 검색 API 요청이 정상인가?
- [ ] 검색 결과가 표시되는가?
- [ ] 검색 결과 없음 상태가 있는가?
- [ ] API 실패 상태가 있는가?
- [ ] 검색어 초기화가 가능한가?
- [ ] loading 상태가 표시되는가?
- [ ] 중복 제출이 방지되는가?
```

Review Agent는 코드가 존재하는지만 보지 않는다.

사용자가 실제로 기능을 사용할 수 있는지 확인해야 한다.

---

### [FAQ]

Q. Requirement Match Review는 왜 가장 먼저 해?
A. 요구사항을 만족하지 못하면 코드 구조가 좋아도 기능 완료로 판단할 수 없기 때문이다.

Q. UI만 있으면 요구사항을 만족한 거야?
A. 아니다. 사용자 행동, API 연동, 성공 / 실패 / 빈 상태, 권한 처리까지 확인해야 한다.

Q. 요구사항이 애매하면 어떻게 해?
A. 현재 코드 기준으로 가능한 가정을 명시하고 누락 가능성을 Issue로 남긴다.

Q. 요구사항에 없는 기능이 추가되면 문제야?
A. 상황에 따라 문제다. 불필요한 복잡도, 일정 지연, 버그 위험을 만들면 리뷰 이슈로 남긴다.

---

## 1.2 User Flow Review

### [개념]

User Flow Review는 사용자가 화면에 진입해서 목적을 달성하기까지의 흐름이 끊기지 않는지 검토하는 과정이다.

프론트엔드 기능은 단일 컴포넌트가 아니라 사용자 행동 흐름 단위로 검토해야 한다.

---

### [핵심]

User Flow Review 대상:

- 페이지 진입
- 초기 데이터 로딩
- 사용자 입력
- 버튼 클릭
- Form 제출
- API 요청
- 결과 표시
- 오류 처리
- 빈 결과 안내
- 페이지 이동
- 뒤로가기
- 인증 만료
- 로그아웃
- 권한 없음
- 새로고침
- 모바일 화면 사용

---

### [실무]

로그인 User Flow 예:

```text
Login Page 진입
→ 이메일 / 비밀번호 입력
→ 제출 버튼 클릭 또는 Enter 제출
→ Loading 표시
→ 로그인 API 요청
→ 성공 시 토큰 저장
→ 사용자 상태 갱신
→ 메인 페이지 이동
→ 실패 시 에러 메시지 표시
→ 사용자가 입력값 수정 후 재시도
```

리뷰 체크리스트:

```md
- [ ] 사용자가 다음 행동을 알 수 있는가?
- [ ] Loading 중 중복 행동이 방지되는가?
- [ ] 실패했을 때 원인을 알 수 있는가?
- [ ] 실패 후 복구할 수 있는가?
- [ ] 완료 후 적절한 피드백이 있는가?
- [ ] 인증 만료 시 흐름이 끊기지 않는가?
- [ ] 뒤로가기 동작이 자연스러운가?
```

User Flow가 끊기는 예:

```text
API 요청 실패
→ console.log만 출력
→ 화면은 계속 빈 상태
→ 사용자는 오류인지 데이터 없음인지 알 수 없음
```

이 경우 High Issue로 판단할 수 있다.

---

### [FAQ]

Q. User Flow Review는 왜 필요해?
A. 코드가 맞아 보여도 실제 사용자가 목적을 달성하지 못하면 기능이 완성된 것이 아니기 때문이다.

Q. API 성공만 확인하면 돼?
A. 아니다. 실패, 지연, 빈 결과, 인증 만료, 권한 없음도 함께 확인해야 한다.

Q. 사용자 흐름이 중간에 끊기면 어떤 우선순위야?
A. 핵심 기능 흐름이면 High 또는 Critical로 판단할 수 있다.

Q. User Flow Review에서 가장 중요한 것은 뭐야?
A. 사용자가 다음 행동을 이해하고 실패 상황에서 복구할 수 있는지 확인하는 것이다.

---

## 1.3 Edge Case Review

### [개념]

Edge Case Review는 일반적인 성공 흐름 외에 데이터 없음, 잘못된 입력, 네트워크 실패, 인증 만료 같은 예외 상황을 검토하는 과정이다.

프론트엔드 코드는 정상 데이터만 기준으로 작성하면 운영 중 쉽게 깨진다.

---

### [핵심]

자주 발생하는 Edge Case:

- API 응답 지연
- API 실패
- 네트워크 실패
- 빈 배열 응답
- null 데이터 응답
- undefined 접근
- 잘못된 route param
- 존재하지 않는 id
- 인증 만료
- 권한 없음
- 중복 제출
- 빠른 연속 클릭
- 새로고침 후 상태 초기화
- 모바일 작은 화면
- 긴 텍스트
- 이미지 로딩 실패
- 파일 크기 초과
- 서버 validation error

---

### [실무]

Edge Case Review 예:

```text
Festival Detail Page
→ festivalId가 잘못됨
→ API 404 응답
→ Not Found UI 표시
→ 목록으로 돌아가기 버튼 제공
```

잘못된 구현:

```jsx
return <h1>{festival.title}</h1>;
```

문제:

```text
festival이 null이면 Cannot read properties of null 오류 발생
```

개선 방향:

```jsx
if (isLoading) {
  return <p>불러오는 중...</p>;
}

if (error) {
  return <p>축제 정보를 불러오지 못했습니다.</p>;
}

if (!festival) {
  return <p>축제 정보를 찾을 수 없습니다.</p>;
}

return <h1>{festival.title}</h1>;
```

---

### [FAQ]

Q. Edge Case Review는 필수야?
A. 필수다. 운영 중 문제는 대부분 정상 흐름보다 예외 상황에서 발생한다.

Q. null 데이터 접근 오류는 왜 자주 발생해?
A. 데이터가 로딩되기 전에 화면이 먼저 렌더링되거나 API 응답이 예상과 다르기 때문이다.

Q. 빈 배열은 에러야?
A. 아니다. 요청은 성공했지만 표시할 데이터가 없는 Empty State로 처리해야 한다.

Q. 404 응답은 어떻게 처리해야 해?
A. 상황에 따라 Not Found UI 또는 사용자 안내 화면으로 처리해야 한다.

---

# 2. Component Review Rules

## 2.1 Component Responsibility Review

### [개념]

Component Responsibility Review는 React Component가 하나의 명확한 책임을 갖고 있는지 검토하는 과정이다.

컴포넌트가 너무 많은 역할을 담당하면 유지보수성, 테스트 가능성, 변경 안정성이 떨어진다.

---

### [핵심]

좋은 Component 기준:

- 역할이 명확함
- 파일명과 컴포넌트명이 일치함
- props가 과도하지 않음
- 내부 state가 필요한 만큼만 있음
- UI와 비즈니스 로직이 과하게 섞이지 않음
- API 호출이 과도하게 흩어지지 않음
- 불필요한 side effect가 없음
- 재사용 가능성이 있음
- 테스트하기 쉬움
- 도메인 의미가 드러남

나쁜 Component 징후:

- 한 컴포넌트가 API 호출, Form 검증, Modal 상태, Table 렌더링, Pagination, Toast, Auth 체크, Routing 이동을 모두 처리
- Page Component가 500줄 이상으로 커짐
- props가 10개 이상 전달됨
- useEffect가 여러 책임을 동시에 처리
- 조건부 렌더링이 지나치게 복잡함
- 상태와 파생 값이 중복 저장됨

---

### [실무]

권장 분리 기준:

```text
Page Component
→ route param 처리
→ 페이지 단위 데이터 조회
→ 화면 조립

Container Component
→ 상태 관리
→ 사용자 행동 흐름
→ 비즈니스 흐름 연결

Presentational Component
→ props 기반 UI 표시
→ 복잡한 side effect 없음

Custom Hook
→ 재사용 가능한 로직
→ API 호출
→ Form 상태
→ Modal 제어

API Module
→ endpoint 호출
→ axios / fetch wrapper 사용
```

컴포넌트 책임 과다 리뷰 코멘트 예:

```text
[Medium] FestivalDetailPage가 API 호출, 리뷰 작성 Form, Modal 상태, 좋아요 처리, 라우팅 이동을 모두 담당하고 있습니다. 데이터 조회는 custom hook으로 분리하고 리뷰 Form은 별도 Component로 분리하는 것이 좋습니다.
```

기능 오류를 유발하는 책임 과다는 High로 올라갈 수 있다.

---

### [FAQ]

Q. 컴포넌트가 몇 줄 이상이면 분리해야 해?
A. 줄 수만으로 판단하지 않는다. API, Form, Modal, 상태, 라우팅 등 여러 책임이 섞였는지가 더 중요하다.

Q. Page Component에 API 호출이 있어도 돼?
A. 가능하다. 다만 복잡하거나 여러 곳에서 재사용되면 Custom Hook 또는 Query Hook으로 분리하는 것이 좋다.

Q. Presentational Component는 뭐야?
A. 주로 props를 받아 UI를 표시하는 컴포넌트이며 복잡한 데이터 조회나 비즈니스 로직을 갖지 않는 것이 좋다.

Q. 컴포넌트 책임 과다는 어떤 우선순위야?
A. 보통 Medium이다. 하지만 주요 버그나 사용자 흐름 중단을 만들면 High로 판단할 수 있다.

---

## 2.2 Page Component Review

### [개념]

Page Component Review는 route에 연결된 페이지 컴포넌트가 페이지 조립 역할에 집중하고 있는지 검토하는 과정이다.

Page Component는 여러 UI 조각을 연결할 수 있지만 모든 로직을 직접 소유하면 유지보수성이 떨어진다.

---

### [핵심]

Page Component의 적절한 역할:

- route param 읽기
- query string 읽기
- 페이지 단위 데이터 요청 연결
- 레이아웃 조립
- 주요 사용자 흐름 연결
- 하위 컴포넌트에 필요한 props 전달
- 페이지 단위 Loading / Error / Empty 처리
- 페이지 이동 처리

Page Component에 과도한 역할:

- 복잡한 Form validation 전체 구현
- 여러 API 호출 로직 직접 구현
- Modal 내부 상세 로직 직접 구현
- 데이터 가공 로직 과다
- 긴 조건부 렌더링 중첩
- auth 로직 직접 반복
- 스타일 세부 구현 과다

---

### [실무]

권장 구조:

```text
FestivalDetailPage
→ useFestivalDetail(festivalId)
→ FestivalDetailHeader
→ FestivalInfoSection
→ FestivalMapSection
→ ReviewList
→ ReviewFormModal
```

나쁜 구조:

```text
FestivalDetailPage
→ route param 처리
→ API 호출
→ 좋아요 API 호출
→ 찜 API 호출
→ 리뷰 Form 상태
→ 리뷰 validation
→ Modal 상태
→ 지도 렌더링
→ 댓글 목록 렌더링
→ 모든 CSS class 직접 제어
```

리뷰 코멘트 예:

```text
[Medium] Page Component가 상세 조회, 좋아요 처리, 리뷰 작성, Modal 제어를 모두 포함하고 있어 변경 영향도가 큽니다. 데이터 조회와 액션 로직을 custom hook으로 분리하는 것이 좋습니다.
```

---

### [FAQ]

Q. Page Component는 무조건 얇아야 해?
A. 무조건은 아니다. 하지만 페이지 조립 역할을 넘어 복잡한 비즈니스 로직과 UI 세부 구현이 모두 들어가면 분리를 검토해야 한다.

Q. Page Component에서 route param을 읽어도 돼?
A. 가능하다. route param 처리와 페이지 단위 데이터 연결은 Page Component의 자연스러운 역할이다.

Q. Page Component에서 Form 상태를 관리해도 돼?
A. 작은 Form은 가능하지만 복잡한 validation이나 재사용 가능성이 있으면 Form Component 또는 Custom Hook으로 분리하는 것이 좋다.

Q. Page Component가 너무 크면 항상 배포 차단이야?
A. 아니다. 보통 Medium 이슈지만 버그를 만들거나 핵심 흐름을 막으면 High로 판단할 수 있다.

---

## 2.3 Container Presentational Component Review

### [개념]

Container Presentational Component Review는 상태와 로직을 담당하는 컴포넌트와 UI 표시를 담당하는 컴포넌트가 적절히 분리되어 있는지 검토하는 과정이다.

이 분리는 필수 패턴은 아니지만 복잡한 화면에서 유지보수성과 테스트 가능성을 높인다.

---

### [핵심]

Container Component 역할:

- state 관리
- API 호출 연결
- 사용자 이벤트 처리
- 비즈니스 흐름 처리
- 하위 UI 컴포넌트에 props 전달

Presentational Component 역할:

- props 기반 UI 표시
- semantic HTML 사용
- 스타일 적용
- 최소한의 이벤트 위임
- API 호출 없음
- 복잡한 side effect 없음

---

### [실무]

예시 구조:

```text
FestivalSearchContainer
→ 검색 상태 관리
→ 검색 API 호출
→ loading / error / empty 판단
→ FestivalSearchForm에 props 전달
→ FestivalSearchResultList에 props 전달
```

```text
FestivalSearchForm
→ input 렌더링
→ submit button 렌더링
→ onSubmit 호출
```

```text
FestivalSearchResultList
→ festival list 렌더링
→ FestivalCard 렌더링
```

리뷰 기준:

```md
- [ ] UI Component가 API를 직접 호출하지 않는가?
- [ ] Presentational Component가 불필요한 state를 갖지 않는가?
- [ ] Container가 너무 많은 UI 세부사항을 직접 처리하지 않는가?
- [ ] props 이름이 명확한가?
- [ ] 테스트하기 쉬운 구조인가?
```

---

### [FAQ]

Q. Container / Presentational 분리는 항상 필요해?
A. 아니다. 화면이 단순하면 하나의 컴포넌트로 충분하다. 복잡도가 올라가면 분리하는 것이 좋다.

Q. Presentational Component에서 이벤트 핸들러를 받을 수 있어?
A. 가능하다. 다만 직접 API 호출보다 onSubmit, onClick 같은 props로 상위에 위임하는 것이 좋다.

Q. Container Component가 UI를 전혀 가지면 안 돼?
A. 아니다. 기본 레이아웃 조립은 가능하다. 다만 세부 UI와 비즈니스 로직이 과하게 섞이지 않게 한다.

Q. 이 구조는 필수 리뷰 기준이야?
A. 필수는 아니지만 복잡한 화면의 유지보수성, 테스트 가능성 판단에 유용한 기준이다.

---

## 2.4 Component Naming Review

### [개념]

Component Naming Review는 컴포넌트 이름이 역할과 의미를 명확히 표현하는지 검토하는 과정이다.

이름은 Retrieval, 유지보수, 협업, 테스트 이해도에 영향을 준다.

---

### [핵심]

권장 Naming:

- PascalCase 사용
- 도메인 의미 포함
- 역할 중심 이름 사용
- Page / Form / List / Card / Item / Modal / Section 구분
- 파일명과 컴포넌트명 일치
- 너무 추상적인 이름 지양
- 임시 이름 금지

좋은 예:

```text
FestivalCard
FestivalList
FestivalSearchForm
FestivalDetailPage
ReviewModal
ReviewItem
NotificationList
LoginForm
ProtectedRoute
```

나쁜 예:

```text
Box
Component1
DataView
Custom
TestPage
Temp
Sample
ItemBox
```

---

### [실무]

파일명과 컴포넌트명 일치 권장:

```text
FestivalCard.jsx
→ function FestivalCard()
```

```text
LoginForm.tsx
→ function LoginForm()
```

역할별 Naming 기준:

| 역할        | 권장 suffix | 예시                |
| ----------- | ----------- | ------------------- |
| 페이지      | Page        | FestivalDetailPage  |
| 폼          | Form        | LoginForm           |
| 목록        | List        | ReviewList          |
| 항목        | Item        | NotificationItem    |
| 카드        | Card        | FestivalCard        |
| 모달        | Modal       | ReviewModal         |
| 섹션        | Section     | FestivalInfoSection |
| 라우트 보호 | Route       | ProtectedRoute      |

---

### [FAQ]

Q. 컴포넌트 이름은 왜 중요해?
A. 역할을 빠르게 이해하고 검색, 수정, 리뷰할 수 있게 하기 때문이다.

Q. Page suffix는 꼭 붙여야 해?
A. 페이지 단위 컴포넌트라면 붙이는 것이 좋다. route 연결 컴포넌트와 일반 UI 컴포넌트를 구분하기 쉽다.

Q. 이름이 길어도 돼?
A. 역할이 명확하다면 어느 정도 길어도 괜찮다. 모호한 짧은 이름보다 낫다.

Q. Component1 같은 이름은 왜 나빠?
A. 역할을 알 수 없어 검색, 유지보수, 리뷰가 어려워지기 때문이다.

---

# 3. Props Review Rules

## 3.1 Props Naming Review

### [개념]

Props Naming Review는 부모 컴포넌트가 자식 컴포넌트에 전달하는 데이터와 이벤트 이름이 명확한지 검토하는 과정이다.

props 이름이 모호하면 컴포넌트 책임과 데이터 흐름을 이해하기 어렵다.

---

### [핵심]

좋은 props 기준:

- 도메인 의미가 드러남
- boolean props는 true / false 의미가 명확함
- event handler props는 `on` prefix 사용
- 내부 handler는 `handle` prefix 사용
- data, item, value 같은 모호한 이름 남용 금지
- 함수 props 이름이 동작을 설명함
- optional props 기본값 고려
- props 이름과 실제 역할이 일치함

좋은 예:

```jsx
<FestivalCard
  festival={festival}
  isFavorite={isFavorite}
  onFavoriteClick={handleFavoriteClick}
/>
```

나쁜 예:

```jsx
<FestivalCard data={data} flag={true} fn={fn} />
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
onReviewCreate
```

내부 handler naming:

```text
handleClick
handleSubmit
handleChange
handleClose
handleSelect
handleFavoriteClick
handleSearchSubmit
handleReviewCreate
```

Boolean props naming:

```text
isOpen
isLoading
isSubmitting
hasError
hasNextPage
canSubmit
shouldShowModal
```

리뷰 코멘트 예:

```text
[Low] flag prop은 의미가 모호합니다. isFavorite 또는 isSelected처럼 true / false 의미가 드러나는 이름으로 변경하는 것이 좋습니다.
```

---

### [FAQ]

Q. props 이름이 왜 중요해?
A. 데이터 흐름과 컴포넌트 역할을 빠르게 이해할 수 있게 하기 때문이다.

Q. data, item 같은 props 이름은 항상 나빠?
A. 항상 나쁘지는 않지만 도메인 의미가 명확한 festival, review, user 같은 이름이 더 좋다.

Q. boolean props는 어떻게 지어야 해?
A. isOpen, hasError, canSubmit처럼 true / false 의미가 드러나게 작성한다.

Q. event handler props는 어떻게 지어야 해?
A. onSubmit, onClose, onFavoriteClick처럼 `on`으로 시작하는 이름을 권장한다.

---

## 3.2 Props Size and Drilling Review

### [개념]

Props Size and Drilling Review는 props 개수가 과도하거나 여러 계층을 지나 전달되는 문제가 있는지 검토하는 과정이다.

props가 많거나 깊게 전달되면 컴포넌트 책임이 커졌거나 상태 위치가 부적절할 수 있다.

---

### [핵심]

검토 항목:

- props 개수가 과도하지 않은가?
- 관련 props를 객체로 묶을 수 있는가?
- 불필요한 전체 객체 전달이 없는가?
- props drilling이 깊지 않은가?
- state 위치가 너무 상위에 있지 않은가?
- Context 또는 store가 필요한 상황인가?
- children composition으로 단순화 가능한가?
- 컴포넌트 분리가 필요한가?

props drilling 문제 예:

```text
App
→ Layout
→ Sidebar
→ UserMenu
→ ProfileButton
→ user 전달
```

---

### [실무]

props가 많은 경우 판단:

```text
필요한 데이터가 많음
→ 객체 props 검토

서로 관련 없는 props가 많음
→ 컴포넌트 책임 분리 검토

여러 단계로 전달만 함
→ Context / composition 검토

전역으로 필요한 상태
→ Global State 검토
```

나쁜 예:

```jsx
<UserProfile
  userId={userId}
  username={username}
  email={email}
  profileImage={profileImage}
  role={role}
  createdAt={createdAt}
  updatedAt={updatedAt}
/>
```

개선 예:

```jsx
<UserProfile user={user} />
```

주의:

```text
전체 객체 전달이 항상 좋은 것은 아니다.
컴포넌트가 필요하지 않은 필드까지 알게 되면 결합도가 높아질 수 있다.
```

---

### [FAQ]

Q. props가 많으면 무조건 나쁜 코드야?
A. 무조건은 아니지만 컴포넌트 책임이 커졌거나 구조 분리가 필요할 수 있다.

Q. props drilling은 언제 문제야?
A. 중간 컴포넌트가 사용하지 않는 props를 여러 단계로 전달만 할 때 문제다.

Q. props가 많으면 모두 객체로 묶어야 해?
A. 아니다. 관련 있는 데이터만 객체로 묶고, 무관한 props는 책임 분리를 검토해야 한다.

Q. props drilling 해결은 무조건 전역 상태야?
A. 아니다. Context, composition, 상태 위치 조정, 컴포넌트 분리도 해결 방법이다.

---

## 3.3 Optional Props Default Review

### [개념]

Optional Props Default Review는 선택 props가 전달되지 않았을 때 컴포넌트가 안전하게 동작하는지 검토하는 과정이다.

optional props 처리가 없으면 undefined 접근 오류나 의도치 않은 UI가 발생할 수 있다.

---

### [핵심]

검토 항목:

- optional props 기본값이 있는가?
- optional callback 호출 전 존재 여부를 확인하는가?
- optional array 기본값이 빈 배열인가?
- optional object 접근 시 null / undefined 처리가 있는가?
- default UI가 적절한가?
- TypeScript optional field가 안전하게 처리되는가?

---

### [실무]

좋은 예:

```jsx
function FestivalList({ festivals = [] }) {
  if (festivals.length === 0) {
    return <p>표시할 축제가 없습니다.</p>;
  }

  return (
    <ul>
      {festivals.map((festival) => (
        <li key={festival.id}>{festival.title}</li>
      ))}
    </ul>
  );
}
```

optional callback 예:

```jsx
function Modal({ isOpen, onClose }) {
  if (!isOpen) return null;

  return (
    <button type="button" onClick={() => onClose?.()}>
      닫기
    </button>
  );
}
```

리뷰 코멘트 예:

```text
[Medium] festivals prop이 undefined일 때 festivals.length 접근으로 런타임 오류가 발생할 수 있습니다. 기본값을 빈 배열로 설정하거나 fallback UI를 추가해야 합니다.
```

---

### [FAQ]

Q. optional props는 왜 기본값이 필요해?
A. 전달되지 않았을 때 undefined 접근 오류를 막고 컴포넌트 동작을 예측 가능하게 만들기 위해 필요하다.

Q. optional callback은 어떻게 호출해야 해?
A. onClose?.()처럼 존재 여부를 확인하거나 기본 no-op 함수를 제공하는 방식이 안전하다.

Q. optional array는 어떤 기본값이 좋아?
A. 대부분 빈 배열 `[]`이 적절하다.

Q. optional props 처리는 TypeScript만 있으면 충분해?
A. 아니다. TypeScript는 개발 시점 도움이고 런타임 데이터는 여전히 방어적으로 처리해야 한다.

---

# 4. Component Composition Review Rules

## 4.1 Children Composition Review

### [개념]

Children Composition Review는 props 전달이 복잡한 컴포넌트를 children 또는 composition 구조로 단순화할 수 있는지 검토하는 과정이다.

Composition은 props drilling을 줄이고 컴포넌트 결합도를 낮추는 데 도움이 된다.

---

### [핵심]

Composition이 적합한 경우:

- wrapper component가 내부 내용을 몰라도 되는 경우
- layout component가 children만 배치하면 되는 경우
- modal / card / panel처럼 공통 껍데기가 있는 경우
- props drilling을 줄일 수 있는 경우
- UI 조합을 호출부에서 명확히 표현하고 싶은 경우

---

### [실무]

나쁜 예:

```jsx
<Modal title="리뷰 작성" content={<ReviewForm />} footer={<SubmitButton />} />
```

개선 예:

```jsx
<Modal>
  <Modal.Header>리뷰 작성</Modal.Header>
  <Modal.Body>
    <ReviewForm />
  </Modal.Body>
  <Modal.Footer>
    <SubmitButton />
  </Modal.Footer>
</Modal>
```

Layout 예:

```jsx
<PageLayout>
  <FestivalSearchForm />
  <FestivalList />
</PageLayout>
```

리뷰 코멘트 예:

```text
[Suggestion] Card 컴포넌트가 title, content, footer props를 모두 받기보다 children composition 구조로 바꾸면 다양한 UI 조합에 대응하기 쉽습니다.
```

---

### [FAQ]

Q. children composition은 언제 사용해?
A. wrapper component가 내부 UI 내용을 직접 알 필요 없고 배치 역할만 할 때 적합하다.

Q. composition은 필수야?
A. 아니다. 단순 props 구조가 더 명확한 경우도 있다.

Q. composition을 쓰면 장점이 뭐야?
A. props drilling을 줄이고 UI 조합을 호출부에서 명확하게 표현할 수 있다.

Q. composition이 과하면 문제야?
A. 그렇다. 너무 복잡한 compound component 구조는 오히려 이해를 어렵게 만들 수 있다.

---

## 4.2 Conditional Rendering Review

### [개념]

Conditional Rendering Review는 조건부 렌더링이 명확하고 안전하게 작성되었는지 검토하는 과정이다.

프론트엔드 UI는 loading, error, empty, success, auth 상태에 따라 다른 화면을 보여주므로 조건 분기 품질이 중요하다.

---

### [핵심]

검토 항목:

- Loading / Error / Empty / Success 분기가 명확한가?
- 조건 순서가 안전한가?
- null 데이터 접근 전에 방어 코드가 있는가?
- 중첩 ternary가 과도하지 않은가?
- 조건식이 읽기 쉬운가?
- false, 0, empty string 처리가 의도와 맞는가?
- 권한 조건이 UI와 API 양쪽에서 고려되는가?
- 조건부 hook 호출이 없는가?

---

### [실무]

좋은 조건 순서:

```jsx
if (isLoading) {
  return <Loading />;
}

if (error) {
  return <ErrorMessage message="데이터를 불러오지 못했습니다." />;
}

if (!festival) {
  return <EmptyState message="축제 정보를 찾을 수 없습니다." />;
}

return <FestivalDetail festival={festival} />;
```

나쁜 예:

```jsx
return <div>{festival.title}</div>;
```

문제:

```text
festival이 null 또는 undefined일 때 런타임 오류 발생
```

중첩 ternary 과다 예:

```jsx
{
  isLoading ? <Loading /> : error ? <Error /> : data ? <List /> : <Empty />;
}
```

복잡한 경우 early return 또는 별도 함수 분리를 검토한다.

---

### [FAQ]

Q. 조건부 렌더링에서 가장 중요한 것은 뭐야?
A. null 데이터 접근 전에 loading, error, empty 상태를 먼저 처리하는 것이다.

Q. 중첩 ternary는 쓰면 안 돼?
A. 간단한 경우는 가능하지만 조건이 많아지면 가독성과 유지보수성이 떨어진다.

Q. 조건부 hook 호출은 가능해?
A. 안 된다. Hook은 항상 컴포넌트 최상위에서 같은 순서로 호출되어야 한다.

Q. Empty State와 Error State는 달라?
A. 다르다. Empty State는 요청 성공 후 데이터가 없는 상태이고 Error State는 요청 실패 상태다.

---

# 5. Component Review Checklist

## 5.1 Component Review Checklist

### [개념]

Component Review Checklist는 Review Agent가 컴포넌트 구조를 검토할 때 사용하는 최종 점검 목록이다.

이 체크리스트는 컴포넌트 책임, 이름, props, composition, 조건부 렌더링을 빠르게 검토하기 위한 Retrieval 기준이다.

---

### [핵심]

Component Review Checklist:

```md
## Requirement

- [ ] 컴포넌트가 요구사항에 필요한 UI를 제공하는가?
- [ ] 사용자 행동 흐름이 끊기지 않는가?

## Responsibility

- [ ] 컴포넌트 책임이 명확한가?
- [ ] API 호출, Form, Modal, Routing이 과하게 섞이지 않았는가?
- [ ] Page Component가 페이지 조립 역할에 집중하는가?
- [ ] 재사용 가능한 로직이 Custom Hook으로 분리 가능한가?

## Naming

- [ ] 컴포넌트 이름이 역할을 표현하는가?
- [ ] 파일명과 컴포넌트명이 일치하는가?
- [ ] Page / Form / List / Card / Item / Modal 구분이 명확한가?

## Props

- [ ] props 이름이 명확한가?
- [ ] boolean props 의미가 명확한가?
- [ ] event handler props가 on prefix를 사용하는가?
- [ ] props 개수가 과도하지 않은가?
- [ ] props drilling이 과하지 않은가?
- [ ] optional props 기본값이 있는가?

## Rendering

- [ ] Loading / Error / Empty / Success 분기가 명확한가?
- [ ] null / undefined 접근 위험이 없는가?
- [ ] 중첩 조건부 렌더링이 과하지 않은가?
- [ ] 조건부 Hook 호출이 없는가?

## Maintainability

- [ ] 테스트하기 쉬운 구조인가?
- [ ] UI와 비즈니스 로직이 과하게 섞이지 않았는가?
- [ ] 변경 영향 범위가 과도하지 않은가?
```

---

### [실무]

Component Review 우선순위:

```text
Requirement Match
→ User Flow
→ Responsibility
→ Props / State Boundary
→ Conditional Rendering Safety
→ Naming
→ Composition
→ Testability
```

Review Agent는 사소한 naming보다 책임 과다, null 접근, 사용자 흐름 중단을 먼저 검토한다.

---

### [FAQ]

Q. Component Review에서 가장 먼저 볼 것은 뭐야?
A. 요구사항을 만족하는지와 사용자 흐름이 끊기지 않는지 먼저 확인한다.

Q. 컴포넌트 이름 문제는 어떤 우선순위야?
A. 보통 Low다. 다만 이름 혼동이 큰 유지보수 문제를 만들면 Medium으로 볼 수 있다.

Q. 조건부 렌더링 문제는 어떤 우선순위야?
A. null 접근으로 흰 화면이 발생하면 High 또는 Critical이 될 수 있다.

Q. props drilling은 항상 문제야?
A. 아니다. 깊고 반복적인 전달로 유지보수성이 떨어질 때 문제다.

---

# Retrieval Queries

### [FAQ]

Q. Requirement Match Review는 뭐야?
A. 프론트엔드 구현 코드가 사용자의 요구사항과 실제 기능 목적을 만족하는지 검토하는 과정이다.

Q. 요구사항 리뷰는 왜 가장 먼저 해?
A. 요구사항을 만족하지 못하면 코드 구조가 좋아도 기능 완료로 판단할 수 없기 때문이다.

Q. UI만 구현되면 요구사항 완료야?
A. 아니다. 사용자 행동, API 연동, 성공 / 실패 / 빈 상태, 권한 처리까지 확인해야 한다.

Q. User Flow Review는 뭐야?
A. 사용자가 화면에 진입해서 목적을 달성하기까지 흐름이 끊기지 않는지 검토하는 과정이다.

Q. 사용자 흐름이 끊기면 어떤 문제야?
A. 핵심 기능 흐름이면 High 또는 Critical Issue로 판단할 수 있다.

Q. Edge Case Review는 뭐야?
A. API 실패, 빈 데이터, null 응답, 인증 만료, 중복 제출 같은 예외 상황을 검토하는 과정이다.

Q. 빈 배열 응답은 에러야?
A. 아니다. 요청은 성공했지만 표시할 데이터가 없는 Empty State로 처리해야 한다.

Q. null 데이터 접근 오류는 왜 발생해?
A. 데이터가 로딩되기 전에 화면이 먼저 렌더링되거나 API 응답이 예상과 다르기 때문이다.

Q. Component Responsibility Review는 뭐야?
A. React Component가 하나의 명확한 책임을 갖고 있는지 검토하는 과정이다.

Q. 컴포넌트가 너무 크면 무조건 문제야?
A. 줄 수만으로 판단하지 않는다. 여러 책임이 섞였는지가 더 중요하다.

Q. Page Component 역할은 뭐야?
A. route param 처리, 페이지 단위 데이터 조회 연결, 레이아웃 조립, 주요 사용자 흐름 연결이다.

Q. Page Component에 API 호출이 있어도 돼?
A. 가능하다. 다만 복잡하거나 재사용되면 Custom Hook 또는 Query Hook으로 분리하는 것이 좋다.

Q. Presentational Component는 뭐야?
A. props를 받아 UI를 표시하는 컴포넌트이며 복잡한 데이터 조회나 비즈니스 로직을 갖지 않는 것이 좋다.

Q. Container Component는 뭐야?
A. state 관리, API 호출 연결, 사용자 이벤트 처리, 비즈니스 흐름 처리를 담당하는 컴포넌트다.

Q. Component Naming Review는 뭐야?
A. 컴포넌트 이름이 역할과 의미를 명확히 표현하는지 검토하는 과정이다.

Q. 좋은 컴포넌트 이름은 뭐야?
A. FestivalCard, FestivalList, LoginForm, ReviewModal처럼 도메인과 역할이 드러나는 이름이다.

Q. 나쁜 컴포넌트 이름은 뭐야?
A. Box, Component1, DataView, Custom, Temp처럼 역할을 알 수 없는 이름이다.

Q. Props Naming Review는 뭐야?
A. 부모 컴포넌트가 자식 컴포넌트에 전달하는 데이터와 이벤트 이름이 명확한지 검토하는 과정이다.

Q. boolean props 이름은 어떻게 지어야 해?
A. isOpen, isLoading, hasError, canSubmit처럼 true / false 의미가 드러나게 작성한다.

Q. event handler props 이름은 어떻게 지어야 해?
A. onSubmit, onClose, onFavoriteClick처럼 `on`으로 시작하는 이름을 권장한다.

Q. 내부 handler 이름은 어떻게 지어야 해?
A. handleSubmit, handleClose, handleFavoriteClick처럼 `handle`로 시작하는 이름을 권장한다.

Q. props drilling은 뭐야?
A. 중간 컴포넌트가 사용하지 않는 props를 여러 계층 아래로 전달하는 문제다.

Q. props drilling 해결은 무조건 전역 상태야?
A. 아니다. Context, composition, 상태 위치 조정, 컴포넌트 분리도 해결 방법이다.

Q. optional props는 왜 기본값이 필요해?
A. 전달되지 않았을 때 undefined 접근 오류를 막고 컴포넌트 동작을 예측 가능하게 만들기 위해 필요하다.

Q. optional callback은 어떻게 호출해야 해?
A. onClose?.()처럼 존재 여부를 확인하거나 기본 no-op 함수를 제공하는 방식이 안전하다.

Q. children composition은 언제 사용해?
A. wrapper component가 내부 UI 내용을 직접 알 필요 없고 배치 역할만 할 때 적합하다.

Q. Conditional Rendering Review는 뭐야?
A. loading, error, empty, success, auth 상태에 따른 조건부 렌더링이 안전하고 명확한지 검토하는 과정이다.

Q. 조건부 렌더링에서 가장 중요한 것은 뭐야?
A. null 데이터 접근 전에 loading, error, empty 상태를 먼저 처리하는 것이다.

Q. 중첩 ternary는 사용하면 안 돼?
A. 간단한 경우는 가능하지만 조건이 많아지면 early return 또는 별도 함수 분리를 검토한다.

Q. 조건부 Hook 호출은 가능해?
A. 안 된다. Hook은 항상 컴포넌트 최상위에서 같은 순서로 호출되어야 한다.

Q. Component Review에서 가장 먼저 볼 것은 뭐야?
A. 요구사항 만족 여부와 사용자 흐름이 끊기지 않는지 먼저 확인한다.

Q. Component Review의 최종 목적은 뭐야?
A. 컴포넌트가 요구사항을 만족하면서 책임이 명확하고 유지보수 가능한 구조인지 판단하는 것이다.
