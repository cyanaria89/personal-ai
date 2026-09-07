# React Component Design Part01 - Component Responsibility and Boundary

---

# 1. Component Responsibility

## 1.1 Component Responsibility Definition

### [개념]

Component Responsibility는 하나의 React Component가 담당해야 하는 역할과 책임 범위를 의미한다.

React Component는 화면을 구성하는 단순 JSX 조각이 아니라, UI 책임, 데이터 표시 책임, 이벤트 전달 책임, 상태 관리 책임 중 어떤 역할을 담당하는지 명확해야 한다.

Component Responsibility가 명확하면 Frontend Agent는 화면 요구사항을 Component 단위로 분해하고, 유지보수 가능한 React 구조를 생성할 수 있다.

---

### [핵심]

- Component Responsibility는 Component의 존재 이유다.
- Component는 하나의 명확한 주요 책임을 가져야 한다.
- 책임이 불명확한 Component는 유지보수성이 낮다.
- 하나의 Component에 API 호출, Form 처리, Modal 처리, List 렌더링, Card 렌더링이 모두 섞이면 Overgrown Component가 된다.
- Component 이름은 책임을 드러내야 한다.
- Component Responsibility는 Component Boundary 결정의 출발점이다.
- Page Component, Feature Component, UI Component는 책임 기준이 다르다.
- Component Responsibility가 명확해야 Props Contract도 명확해진다.
- Component Responsibility가 명확해야 State Ownership도 결정할 수 있다.

---

### [실무]

2026 실무 기준에서 React Component는 단순히 작게 나누는 것이 목표가 아니다.

중요한 기준은 "이 Component가 어떤 책임을 갖는가?"이다.

나쁜 구조:

```jsx
function FestivalPage() {
  // API 요청
  // 검색 Form 상태
  // 필터 상태
  // 축제 목록 렌더링
  // 축제 Card JSX
  // Modal 상태
  // Pagination 처리
  // Error 처리
  return null;
}
```

문제:

- FestivalPage가 너무 많은 책임을 가진다.
- 화면 변경 시 수정 범위가 커진다.
- 테스트 단위가 불명확하다.
- Props Contract를 설계하기 어렵다.
- Custom Hook 추출 기준이 흐려진다.
- UI Component 재사용이 어렵다.

개선 구조:

```text
FestivalPage
→ FestivalSearchForm
→ FestivalFilterPanel
→ FestivalList
→ FestivalCard
→ FestivalPagination
→ FestivalDetailModal
```

책임 분리 예:

```text
FestivalPage
- 화면 조립
- 주요 State 소유
- API 데이터 흐름 관리

FestivalSearchForm
- 검색어 입력
- 검색 submit 이벤트 발생

FestivalFilterPanel
- 지역 / 테마 / 기간 필터 UI 제공

FestivalList
- 축제 목록 렌더링

FestivalCard
- 축제 요약 정보 표시

FestivalPagination
- 페이지 이동 이벤트 전달

FestivalDetailModal
- 상세 정보 Modal 표시
```

---

### [FAQ]

Q. Component Responsibility가 뭐야?
A. 하나의 Component가 담당하는 역할과 책임 범위다. Component가 무엇을 표시하고 어떤 이벤트를 전달하며 어떤 상태를 소유하는지 정하는 기준이다.

Q. Component 책임은 왜 중요해?
A. 책임이 명확해야 Component 분리, Props 설계, State 위치 결정, Custom Hook 추출을 일관되게 할 수 있다.

Q. Component는 작게 나누면 무조건 좋아?
A. 아니다. 책임이 명확하거나 재사용 가능하거나 복잡도를 줄일 때 분리한다. 책임 없는 과분리는 피한다.

Q. Component 이름은 어떻게 지어야 해?
A. 역할이 드러나야 한다. FestivalCard, FestivalSearchForm, FilterPanel처럼 Component 책임을 이름에서 알 수 있어야 한다.

---

## 1.2 Single Responsibility Component

### [개념]

Single Responsibility Component는 하나의 Component가 하나의 주요 책임을 가지도록 설계하는 원칙이다.

React Component에서 Single Responsibility는 "파일 하나에 코드가 적어야 한다"가 아니라 "Component가 담당하는 역할이 명확해야 한다"는 의미다.

---

### [핵심]

- Component는 하나의 주요 책임을 가져야 한다.
- UI 표시와 데이터 요청은 분리할 수 있다.
- Form 입력 처리와 목록 렌더링은 분리할 수 있다.
- Modal 상태와 Page 데이터 로딩은 분리할 수 있다.
- Component가 커지는 원인은 책임 혼합이다.
- Single Responsibility는 재사용성보다 유지보수성 기준으로 먼저 판단한다.
- 책임이 다른 로직이 섞이면 Component 분리를 검토한다.

---

### [실무]

Component 분리 판단 기준:

```text
Component Analyze
→ Check JSX Length
→ Check State Count
→ Check Event Handler Count
→ Check API Logic
→ Check UI Section Independence
→ Check Reusability
→ Split Component if Responsibility Is Mixed
```

분리가 필요한 신호:

- JSX가 길어져 한눈에 구조가 보이지 않는다.
- useState가 많아진다.
- useEffect가 여러 목적을 가진다.
- Event Handler가 많아진다.
- API 요청과 UI 표시가 강하게 섞인다.
- 조건부 렌더링이 복잡하다.
- 특정 UI 영역을 독립적으로 설명할 수 있다.
- 같은 UI가 다른 화면에서도 반복된다.

예:

```jsx
function ReviewSection({ reviews, onSubmitReview }) {
  return (
    <section>
      <ReviewForm onSubmit={onSubmitReview} />
      <ReviewList reviews={reviews} />
    </section>
  );
}
```

책임:

```text
ReviewSection
- ReviewForm과 ReviewList 조립

ReviewForm
- 리뷰 입력
- submit 이벤트 전달

ReviewList
- 리뷰 목록 표시
```

주의:

- 무조건 작은 Component를 많이 만드는 것이 좋은 설계는 아니다.
- 1회성 JSX 조각을 과도하게 분리하면 파일 이동과 Props 전달만 늘어난다.
- 분리 목적이 명확해야 한다.

---

### [FAQ]

Q. Single Responsibility Component는 무슨 뜻이야?
A. 하나의 Component가 하나의 주요 역할을 담당하도록 설계하는 것이다.

Q. Component가 커졌을 때 어디부터 나눠?
A. 먼저 UI 영역 기준으로 Form, List, Card, Modal, Pagination 같은 독립 영역을 분리한다.

Q. useEffect가 많으면 Component를 나눠야 해?
A. useEffect 목적이 여러 개라면 API 요청, 이벤트 리스너, 타이머, 동기화 로직을 Custom Hook으로 분리할 수 있는지 검토한다.

Q. JSX가 길면 무조건 분리해야 해?
A. 아니다. JSX가 길어도 책임이 하나라면 유지할 수 있다. 하지만 독립 가능한 영역이 있으면 분리한다.

---

# 2. Component Boundary

## 2.1 Component Boundary Definition

### [개념]

Component Boundary는 Component를 어디에서 나누고 어떤 책임을 맡길지 결정하는 경계다.

Component Boundary는 UI 영역, State Ownership, 데이터 의존성, 이벤트 발생 위치, 재사용 가능성, 변경 가능성을 기준으로 결정한다.

---

### [핵심]

Component Boundary 판단 기준:

- UI Section Boundary
- State Ownership Boundary
- Data Dependency Boundary
- Event Source Boundary
- Reusability Boundary
- Domain Feature Boundary
- Change Boundary
- Test Boundary

Component Boundary가 명확하면:

- Props Contract가 단순해진다.
- State 위치가 명확해진다.
- Page / Feature / UI Component 역할이 구분된다.
- API Logic과 UI Logic을 분리하기 쉽다.
- Component Review가 쉬워진다.

---

### [실무]

Component Boundary Flow:

```text
Screen Requirement
→ Identify UI Sections
→ Identify Data Dependencies
→ Identify State Owner
→ Identify Event Sources
→ Identify Repeated UI
→ Split Component
→ Define Props Contract
→ Review Boundary
```

예:

```text
FestivalPage
- API 요청
- 검색 조건 State
- 축제 목록 State
- loading / error / empty 상태 처리

FestivalSearchForm
- keyword 입력
- submit 이벤트 발생

FestivalFilterPanel
- filter 선택
- filter change 이벤트 발생

FestivalList
- festivals 배열 표시

FestivalCard
- festival 단일 항목 표시
```

Boundary 판단:

```text
검색 입력 영역이 독립적이다
→ FestivalSearchForm 분리

필터 선택 영역이 독립적이다
→ FestivalFilterPanel 분리

목록 표시가 반복 구조다
→ FestivalList 분리

각 항목 카드가 반복된다
→ FestivalCard 분리
```

---

### [FAQ]

Q. Component Boundary가 뭐야?
A. Component를 어디서 나누고 어떤 책임을 맡길지 결정하는 경계다.

Q. Component Boundary는 뭘 기준으로 잡아?
A. UI 영역, State Owner, 데이터 의존성, 이벤트 발생 위치, 재사용 가능성, 변경 가능성을 기준으로 잡는다.

Q. Component Boundary가 잘못되면 어떤 문제가 생겨?
A. Props가 복잡해지고 State 위치가 애매해지며 Component가 너무 커지거나 과도하게 쪼개질 수 있다.

Q. Component Boundary와 Component Responsibility 차이는?
A. Responsibility는 Component의 역할이고 Boundary는 그 역할을 기준으로 Component를 어디서 나눌지 정하는 경계다.

---

## 2.2 UI Section Boundary

### [개념]

UI Section Boundary는 화면에서 의미 있는 UI 영역을 기준으로 Component를 나누는 방식이다.

사용자가 화면을 볼 때 독립적으로 인식할 수 있는 구역은 Component 분리 후보가 된다.

---

### [핵심]

UI Section Boundary 기준:

- Header 영역
- Search 영역
- Filter 영역
- List 영역
- Card 영역
- Form 영역
- Modal 영역
- Pagination 영역
- Empty State 영역
- Error State 영역

분리 후보:

- 독립적인 제목과 내용이 있는 영역
- 반복되는 UI 영역
- 독립적인 이벤트를 가진 영역
- 독립적인 상태를 가진 영역
- 다른 화면에서도 재사용될 수 있는 영역

---

### [실무]

화면 요구사항:

```text
축제 검색 페이지에는 검색창, 지역 필터, 테마 필터, 축제 목록, 페이지네이션이 있다.
```

Component 분해:

```text
FestivalSearchPage
→ FestivalSearchForm
→ FestivalRegionFilter
→ FestivalThemeFilter
→ FestivalList
→ FestivalPagination
```

예:

```jsx
function FestivalSearchPage() {
  return (
    <main>
      <FestivalSearchForm />
      <FestivalFilterSection />
      <FestivalList />
      <FestivalPagination />
    </main>
  );
}
```

주의:

- UI 영역이 독립적으로 보인다고 무조건 분리하지 않는다.
- 분리 후 Props가 더 복잡해지면 구조를 재검토한다.
- 작은 텍스트나 단순 wrapper는 분리하지 않아도 된다.
- 반복 구조는 Component 분리 우선순위가 높다.

---

### [FAQ]

Q. UI 영역 기준으로 Component를 나눠도 돼?
A. 가능하다. Search, Filter, List, Card, Modal처럼 의미 있는 UI 영역은 Component 분리 기준이 된다.

Q. 화면에 보이는 박스마다 Component로 나눠야 해?
A. 아니다. 책임이 명확하거나 반복되거나 독립적인 상태와 이벤트가 있을 때 분리한다.

Q. 반복되는 Card는 분리하는 게 좋아?
A. 일반적으로 좋다. List는 배열 렌더링을 담당하고 Card는 단일 항목 표시를 담당하게 만들 수 있다.

---

## 2.3 State Ownership Boundary

### [개념]

State Ownership Boundary는 State를 어떤 Component가 소유해야 하는지에 따라 Component 경계를 결정하는 방식이다.

State는 기본적으로 그 State를 사용하는 Component들의 가장 가까운 공통 부모에 위치한다.

---

### [핵심]

State Ownership 판단 기준:

- State를 읽는 Component
- State를 변경하는 Component
- State를 공유하는 Component
- 가장 가까운 공통 부모
- URL과 동기화 여부
- 서버 데이터 상태 여부
- 전역 상태 필요 여부

State Ownership 규칙:

- Local State는 사용하는 Component 내부에 둔다.
- Shared State는 가장 가까운 공통 부모에 둔다.
- Page State는 Page Component가 소유할 수 있다.
- Form 내부 임시값은 Form Component가 소유할 수 있다.
- 서버 데이터 상태는 Page, Container, Custom Hook에서 소유할 수 있다.
- UI Component는 필요한 값을 Props로 받는 것이 기본이다.

---

### [실무]

State Ownership Flow:

```text
Identify State
→ Find Components That Read State
→ Find Components That Change State
→ Find Closest Common Parent
→ Place State There
→ Pass Data Down
→ Pass Callback Down
```

예:

```text
FestivalPage owns keyword
→ FestivalSearchForm receives onSearch
→ FestivalList receives keyword or filtered festivals
```

구조:

```jsx
function FestivalPage() {
  const [keyword, setKeyword] = useState("");

  return (
    <>
      <FestivalSearchForm onSearch={setKeyword} />
      <FestivalList keyword={keyword} />
    </>
  );
}
```

판단:

```text
keyword는 FestivalSearchForm에서 변경된다.
keyword는 FestivalList 데이터 조회에 영향을 준다.
두 Component의 공통 부모는 FestivalPage다.
따라서 keyword State는 FestivalPage가 소유한다.
```

주의:

- 모든 State를 App에 올리지 않는다.
- 모든 State를 전역 상태로 만들지 않는다.
- 너무 아래에 두면 형제 Component가 공유하기 어렵다.
- 너무 위에 두면 Props 전달이 증가한다.

---

### [FAQ]

Q. State는 어디에 둬야 해?
A. 그 State를 사용하는 Component들의 가장 가까운 공통 부모에 두는 것이 기본이다.

Q. Form 입력값은 어디에 둬야 해?
A. Form 내부에서만 사용하면 Form Component에 둔다. 검색 결과나 목록 조회에 필요하면 Page 또는 공통 부모로 올린다.

Q. 모든 State를 Page에 두면 안 돼?
A. 권장하지 않는다. Page가 너무 많은 책임을 가지면 Overgrown Component가 된다.

Q. 모든 State를 전역 상태로 만들면 편하지 않아?
A. 초기에는 편해 보이지만 변경 추적이 어려워지고 불필요한 의존성이 생긴다. 전역 상태는 반복 공유가 명확할 때 검토한다.

---

# 3. Page, Feature, UI Component Boundary

## 3.1 Page Component Boundary

### [개념]

Page Component는 라우트나 화면 단위를 대표하는 Component다.

Page Component는 화면 조립, 주요 State 관리, API 호출 시작점, loading / error / empty 상태 분기를 담당할 수 있다.

---

### [핵심]

Page Component 역할:

- 화면 단위 구성
- Feature Component 조립
- 주요 State 소유
- API 호출 시작점 가능
- URL parameter 사용 가능
- loading 상태 처리 가능
- error 상태 처리 가능
- empty 상태 처리 가능
- Layout 연결 가능

Page Component 주의:

- 모든 UI JSX를 Page에 몰아넣지 않는다.
- 모든 Event Handler를 Page에 몰아넣지 않는다.
- API 함수가 길어지면 api 파일로 분리한다.
- API 상태 로직이 반복되면 Custom Hook으로 분리한다.
- 세부 UI는 Feature Component 또는 UI Component로 분리한다.

---

### [실무]

예:

```jsx
function FestivalPage() {
  const { festivals, loading, error } = useFestivals();

  if (loading) {
    return <LoadingView />;
  }

  if (error) {
    return <ErrorMessage message="축제 목록을 불러오지 못했습니다." />;
  }

  return (
    <main>
      <FestivalSearchSection />
      <FestivalList festivals={festivals} />
    </main>
  );
}
```

권장 구조:

```text
pages/FestivalPage/FestivalPage.tsx
features/festival/components/FestivalSearchSection.tsx
features/festival/components/FestivalList.tsx
features/festival/components/FestivalCard.tsx
features/festival/hooks/useFestivals.ts
features/festival/api/festivalApi.ts
components/LoadingView/LoadingView.tsx
components/ErrorMessage/ErrorMessage.tsx
```

---

### [FAQ]

Q. Page Component는 뭘 담당해?
A. 라우트나 화면 단위를 대표하며 화면 조립, 주요 State, 데이터 흐름, loading/error/empty 상태 분기를 담당할 수 있다.

Q. Page Component에서 API 호출해도 돼?
A. 간단한 화면에서는 가능하다. 하지만 API 로직이 길거나 반복되면 api 함수나 Custom Hook으로 분리한다.

Q. Page Component에 모든 JSX를 넣으면 안 돼?
A. 권장하지 않는다. Page가 너무 커지면 Component Responsibility가 흐려지고 유지보수가 어려워진다.

---

## 3.2 Feature Component Boundary

### [개념]

Feature Component는 특정 도메인 기능 단위를 담당하는 Component다.

Feature Component는 Page보다 작고 UI Component보다 도메인 의존성이 높다.

---

### [핵심]

Feature Component 역할:

- 특정 도메인 기능 UI 담당
- 내부 Local State 보유 가능
- Event Handler 보유 가능
- 도메인 데이터 사용 가능
- UI Component 조립 가능
- Page로 이벤트 전달 가능
- API 호출은 상황에 따라 가능하지만 분리 권장

Feature Component 예:

- FestivalSearchForm
- FestivalFilterPanel
- FestivalList
- ReviewForm
- NotificationList
- ChatRoomPanel
- LoginForm
- UserProfileEditor

---

### [실무]

예:

```jsx
function FestivalSearchForm({ onSearch }) {
  const [keyword, setKeyword] = useState("");

  function handleSubmit(event) {
    event.preventDefault();
    onSearch(keyword.trim());
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={keyword}
        onChange={(event) => setKeyword(event.target.value)}
      />
      <Button type="submit">검색</Button>
    </form>
  );
}
```

책임:

```text
FestivalSearchForm
- keyword Local State 관리
- submit 이벤트 처리
- 검색어를 부모에게 전달
- 실제 API 호출 여부는 부모 또는 Hook이 결정
```

주의:

- Feature Component는 도메인 이름을 가질 수 있다.
- Feature Component가 너무 커지면 내부 UI Component를 분리한다.
- Feature Component가 API, Form, Modal, List를 모두 가지면 다시 분리한다.

---

### [FAQ]

Q. Feature Component는 뭐야?
A. 특정 도메인 기능 단위를 담당하는 Component다. 예를 들어 FestivalSearchForm, ReviewForm, NotificationList가 있다.

Q. Feature Component는 State를 가져도 돼?
A. 가능하다. 해당 기능 내부에서만 필요한 Local State는 Feature Component가 소유할 수 있다.

Q. Feature Component와 UI Component 차이는?
A. Feature Component는 도메인 기능에 의존하고 UI Component는 도메인과 무관하게 재사용 가능해야 한다.

---

## 3.3 UI Component Boundary

### [개념]

UI Component는 도메인과 무관하게 재사용 가능한 표시 중심 Component다.

UI Component는 API 호출이나 특정 비즈니스 흐름을 몰라야 하며 Props 기반으로 표시와 상호작용을 처리한다.

---

### [핵심]

UI Component 역할:

- 재사용 가능한 UI 제공
- Props 기반 렌더링
- 도메인 로직 최소화
- API 호출 금지
- 접근성 기본 포함
- variant 지원 가능
- children 지원 가능
- className 확장 가능

UI Component 예:

- Button
- Input
- Select
- Modal
- Card
- Badge
- Spinner
- EmptyState
- ErrorMessage
- Pagination

---

### [실무]

예:

```tsx
type ButtonProps = {
  type?: "button" | "submit" | "reset";
  variant?: "primary" | "secondary" | "danger";
  disabled?: boolean;
  children: React.ReactNode;
  onClick?: () => void;
};

function Button({
  type = "button",
  variant = "primary",
  disabled = false,
  children,
  onClick,
}: ButtonProps) {
  return (
    <button
      type={type}
      className={`button button-${variant}`}
      disabled={disabled}
      onClick={onClick}
    >
      {children}
    </button>
  );
}
```

금지:

```text
Button 내부에서 특정 축제 API 호출
Card 내부에서 특정 게시글 fetch
Modal 내부에서 특정 페이지 이동 강제
Input 내부에서 전역 검색 상태 직접 변경
```

권장:

```text
UI Component
→ Props로 값 받기
→ Callback Props로 이벤트 알림
→ 접근성 속성 고려
→ 도메인 의존성 제거
```

---

### [FAQ]

Q. UI Component는 뭐야?
A. Button, Input, Modal처럼 도메인과 무관하게 재사용 가능한 표시 중심 Component다.

Q. UI Component에서 API 호출을 해도 돼?
A. 권장하지 않는다. UI Component는 표시와 상호작용만 담당하고 데이터 요청은 Page, Feature, Hook, API 계층에서 처리한다.

Q. UI Component 이름에 도메인 이름을 넣어도 돼?
A. 도메인 전용이면 Feature Component에 가깝다. 공통 UI Component는 Button, Card, Modal처럼 범용 이름이 좋다.

---

# 4. Component Boundary Decision Flow

## 4.1 Component Split Decision Flow

### [개념]

Component Split Decision Flow는 React 화면을 Component 단위로 분리할지 판단하는 절차다.

Frontend Agent는 화면 요구사항을 받으면 UI 영역, 책임, State, Props, 재사용성 순서로 Component 분리를 판단해야 한다.

---

### [핵심]

분리 판단 순서:

1. 화면의 주요 UI 영역을 식별한다.
2. 각 영역의 책임을 정의한다.
3. State를 누가 소유해야 하는지 확인한다.
4. 이벤트가 어디서 발생하는지 확인한다.
5. 데이터가 어디에서 필요한지 확인한다.
6. 반복되는 UI가 있는지 확인한다.
7. 재사용 가능성이 실제로 있는지 확인한다.
8. Props Contract가 단순해지는지 확인한다.
9. 분리 후 구조가 더 명확한지 검토한다.

---

### [실무]

Component Split Flow:

```text
Screen Requirement
→ UI Section Analysis
→ Responsibility Definition
→ State Ownership Check
→ Event Flow Check
→ Data Dependency Check
→ Reusability Check
→ Props Contract Design
→ Split or Keep Decision
```

분리 권장:

```text
- 책임이 2개 이상 섞임
- JSX 영역이 독립적으로 이해 가능
- 반복 렌더링 대상
- Local State가 독립적
- 이벤트 흐름이 독립적
- 다른 화면에서도 사용 가능
- 테스트 단위가 될 수 있음
```

분리 보류:

```text
- 단순한 1회성 markup
- 분리 후 Props가 과도하게 늘어남
- Component 이름이 애매함
- 책임을 설명하기 어려움
- 실제 재사용 가능성이 낮음
- 파일만 늘어나고 구조가 더 복잡해짐
```

---

### [FAQ]

Q. Component를 분리할지 말지 어떻게 판단해?
A. 책임, UI 영역, State Ownership, 이벤트 흐름, 데이터 의존성, 재사용성, Props 복잡도를 기준으로 판단한다.

Q. Component 분리 후 Props가 많아지면 좋은 분리야?
A. 아닐 수 있다. Props가 과도하게 많아지면 Boundary가 잘못되었거나 State 위치가 부적절할 수 있다.

Q. 작은 프로젝트도 Component를 많이 나눠야 해?
A. 아니다. 작은 프로젝트는 Page, components, api, hooks 정도로 단순하게 시작하고 복잡해질 때 분리한다.

---

## 4.2 Component Boundary Review Checklist

### [개념]

Component Boundary Review Checklist는 Component 분리가 적절한지 검수하기 위한 기준이다.

RAG 문서 기반 Frontend Agent와 Review Agent는 이 Checklist로 React Component 설계를 검토한다.

---

### [핵심]

Checklist:

```md
- [ ] Component 책임이 한 문장으로 설명되는가?
- [ ] Component 이름이 책임을 드러내는가?
- [ ] Page / Feature / UI Component 역할이 구분되는가?
- [ ] Component Boundary가 UI 영역과 일치하는가?
- [ ] State Owner가 적절한가?
- [ ] State를 너무 위로 올리지 않았는가?
- [ ] State를 너무 아래에 두지 않았는가?
- [ ] Props Contract가 명확한가?
- [ ] Props 전달 단계가 과도하지 않은가?
- [ ] Callback Props가 이벤트 의도를 드러내는가?
- [ ] UI Component가 API 호출을 하지 않는가?
- [ ] Feature Component가 과도하게 커지지 않았는가?
- [ ] Page Component에 모든 로직이 몰려 있지 않은가?
- [ ] 반복 UI는 Component로 분리되었는가?
- [ ] 분리 후 구조가 더 읽기 쉬운가?
- [ ] 과도한 추상화가 아닌가?
```

---

### [실무]

Review Flow:

```text
Component Tree Review
→ Responsibility Check
→ Boundary Check
→ State Ownership Check
→ Props Contract Check
→ API Logic Separation Check
→ Reusability Check
→ Anti Pattern Check
```

치명적 문제:

```text
- Page Component가 전체 기능을 모두 담당
- UI Component가 API 호출 수행
- State Owner가 불명확함
- Props 이름이 data, item, flag처럼 모호함
- 여러 boolean props로 불가능한 상태 발생
- Component 분리 목적이 없음
- 공통 Component가 도메인 로직에 강하게 의존
```

---

### [FAQ]

Q. Component Boundary 검수에서 가장 중요한 것은?
A. Component 책임, State Ownership, Props Contract, Page / Feature / UI Component 역할 구분이다.

Q. Review Agent는 Component 설계에서 뭘 먼저 봐야 해?
A. Component가 어떤 책임을 갖는지, 그 책임에 맞는 Boundary로 분리되었는지 먼저 확인해야 한다.

Q. 치명적인 Component 설계 문제는 뭐야?
A. Page에 모든 로직이 몰리거나 UI Component가 API를 호출하거나 State Owner가 불명확한 경우다.

---

# 5. Common Mistakes

## 5.1 Overgrown Component

### [개념]

Overgrown Component는 하나의 Component가 너무 많은 책임과 코드를 가지는 문제다.

React Component Design에서 가장 흔한 Anti Pattern이다.

---

### [핵심]

문제:

- JSX가 너무 길다.
- State가 너무 많다.
- useEffect가 너무 많다.
- Event Handler가 너무 많다.
- API Logic과 UI Logic이 섞인다.
- Form, List, Modal, Pagination이 한 Component에 섞인다.
- 조건부 렌더링이 복잡하다.
- 수정 시 영향 범위가 크다.

원인:

- Component Responsibility 미정의
- Component Boundary 미정의
- Page Component에 모든 코드 작성
- Custom Hook 분리 지연
- UI Component 추출 지연
- API 함수 분리 지연

---

### [실무]

해결 Flow:

```text
Find Overgrown Component
→ Identify UI Sections
→ Extract Presentational Components
→ Extract Feature Components
→ Extract API Functions
→ Extract Custom Hook
→ Review State Ownership
→ Define Props Contract
```

개선 예:

```text
Before:
FestivalPage

After:
FestivalPage
→ useFestivals
→ FestivalSearchForm
→ FestivalFilterPanel
→ FestivalList
→ FestivalCard
→ Pagination
→ ErrorMessage
→ EmptyState
```

---

### [FAQ]

Q. Overgrown Component가 뭐야?
A. 하나의 Component가 API 요청, 상태 관리, 이벤트 처리, 여러 UI 영역 렌더링을 모두 담당해 너무 커진 Component다.

Q. Overgrown Component는 어떻게 해결해?
A. UI 영역별 Component 분리, API 함수 분리, Custom Hook 분리, State Ownership 재검토 순서로 해결한다.

Q. Page Component가 커지는 건 자연스러운 거 아니야?
A. 어느 정도는 자연스럽지만 모든 세부 UI와 로직이 Page에 몰리면 유지보수성이 떨어진다.

---

## 5.2 Under-Splitting and Over-Splitting

### [개념]

Under-Splitting은 Component를 충분히 분리하지 않아 하나의 Component가 커지는 문제다.

Over-Splitting은 필요 이상으로 Component를 나누어 Props 전달과 파일 수만 늘어나는 문제다.

---

### [핵심]

Under-Splitting 문제:

- Component가 너무 커진다.
- 책임이 섞인다.
- 테스트가 어렵다.
- 재사용이 어렵다.
- 수정 영향 범위가 크다.

Over-Splitting 문제:

- 파일이 과도하게 많아진다.
- Props 전달이 증가한다.
- Component 이름이 애매해진다.
- 흐름 추적이 어렵다.
- 실제 책임이 없는 Component가 생긴다.

균형 기준:

- 책임이 명확하면 분리한다.
- 반복되면 분리한다.
- 복잡도를 줄이면 분리한다.
- Props만 전달하는 중간 Component가 많으면 재검토한다.
- 단순한 1회성 JSX는 유지할 수 있다.

---

### [실무]

판단 Flow:

```text
Is responsibility clear?
→ Is UI section independent?
→ Is state local or shared?
→ Is it reused?
→ Does split reduce complexity?
→ Does split increase props drilling?
→ Decide split or keep
```

분리 적합:

```text
FestivalCard
ReviewForm
NotificationList
ChatMessageItem
LoginForm
Modal
Button
EmptyState
```

분리 부적합 가능성:

```text
TitleTextOnlyWrapper
OneLineDescription
SingleUseDivBox
NoResponsibilityContainer
```

---

### [FAQ]

Q. Component를 너무 안 나누면 뭐가 문제야?
A. Component가 커지고 책임이 섞여 유지보수와 테스트가 어려워진다.

Q. Component를 너무 많이 나누면 뭐가 문제야?
A. Props 전달과 파일 이동이 늘어나고 오히려 구조 이해가 어려워질 수 있다.

Q. 적절한 Component 분리 기준은 뭐야?
A. 책임이 명확하고 독립적인 UI 영역이거나 반복되거나 복잡도를 줄일 때 분리한다.

---

# 6. Agent Output Rules

## 6.1 Frontend Agent Component Design Output

### [개념]

Frontend Agent는 사용자 화면 요구사항을 받으면 Component Responsibility와 Component Boundary를 먼저 설계한 후 코드를 생성해야 한다.

---

### [핵심]

Frontend Agent 출력 우선순위:

1. 화면 요구사항 분석
2. Component Responsibility 정의
3. Component Boundary 결정
4. Page / Feature / UI Component 구분
5. State Ownership 결정
6. Props Contract 설계
7. Component Tree 생성
8. Code Skeleton 생성
9. Anti Pattern 검토

---

### [실무]

Frontend Agent Component 설계 출력 예:

```text
Component Tree:

FestivalPage
- responsibility: 화면 조립, 축제 목록 데이터 흐름 관리
- state: keyword, filters, festivals, loading, error

FestivalSearchForm
- responsibility: 검색어 입력과 submit 이벤트 전달
- props: onSearch

FestivalFilterPanel
- responsibility: 필터 선택 UI와 변경 이벤트 전달
- props: filters, onChangeFilters

FestivalList
- responsibility: 축제 목록 표시
- props: festivals, onSelectFestival

FestivalCard
- responsibility: 축제 단일 항목 표시
- props: festival, onSelect
```

Code 생성 전 검토:

```text
- UI Component에서 API 호출 없음
- Props 이름 명확
- State Owner 명확
- Page가 과도하게 커지지 않음
- 반복 UI Component 분리
```

---

### [FAQ]

Q. Frontend Agent는 코드를 바로 생성하면 안 돼?
A. 바로 생성할 수 있지만 좋은 결과를 위해 Component Responsibility, Boundary, State Ownership, Props Contract를 먼저 설계해야 한다.

Q. Component Tree에는 무엇이 포함돼야 해?
A. Component 이름, 책임, Props, State Owner, 하위 Component 관계가 포함되어야 한다.

Q. Review Agent는 Component Tree에서 뭘 검토해야 해?
A. 책임 분리, Boundary 적절성, State Ownership, Props Contract, API Logic 분리 여부를 검토해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. React Component Responsibility가 뭐야?
A. 하나의 React Component가 담당해야 하는 역할과 책임 범위다.

Q. Component Responsibility는 왜 중요해?
A. 책임이 명확해야 Component 분리, Props 설계, State 위치 결정, Custom Hook 추출을 일관되게 할 수 있다.

Q. Component Boundary가 뭐야?
A. Component를 어디서 나누고 어떤 책임을 맡길지 결정하는 경계다.

Q. Component Boundary는 뭘 기준으로 잡아?
A. UI 영역, State Owner, 데이터 의존성, 이벤트 발생 위치, 재사용 가능성, 변경 가능성을 기준으로 잡는다.

Q. React Component는 언제 분리해?
A. 책임이 많아지거나 JSX가 길어지거나 반복되거나 재사용 가능하거나 특정 UI 영역을 독립적으로 이해할 수 있을 때 분리한다.

Q. Component를 작게 많이 나누면 무조건 좋아?
A. 아니다. 책임 없는 과분리는 Props 전달과 파일 이동만 늘려 복잡도를 높일 수 있다.

Q. Single Responsibility Component가 뭐야?
A. 하나의 Component가 하나의 주요 역할을 담당하도록 설계하는 것이다.

Q. JSX가 길면 무조건 Component를 분리해야 해?
A. 아니다. JSX가 길어도 책임이 하나라면 유지할 수 있다. 하지만 독립 가능한 영역이 있으면 분리한다.

Q. Page Component는 뭘 담당해?
A. 라우트나 화면 단위를 대표하며 화면 조립, 주요 State, 데이터 흐름, loading/error/empty 상태 분기를 담당할 수 있다.

Q. Feature Component는 뭐야?
A. 특정 도메인 기능 단위를 담당하는 Component다. Page보다 작고 UI Component보다 도메인 의존성이 높다.

Q. UI Component는 뭐야?
A. Button, Input, Modal처럼 도메인과 무관하게 재사용 가능한 표시 중심 Component다.

Q. Page Component와 Feature Component 차이는?
A. Page Component는 화면 전체 조립과 데이터 흐름을 담당하고 Feature Component는 특정 도메인 기능 UI를 담당한다.

Q. Feature Component와 UI Component 차이는?
A. Feature Component는 도메인 기능에 의존하고 UI Component는 도메인과 무관하게 재사용 가능해야 한다.

Q. UI Component에서 API 호출해도 돼?
A. 권장하지 않는다. UI Component는 표시와 상호작용만 담당하고 데이터 요청은 Page, Feature, Hook, API 계층에서 처리한다.

Q. State Ownership Boundary가 뭐야?
A. State를 어떤 Component가 소유해야 하는지에 따라 Component 경계를 결정하는 기준이다.

Q. State는 어디에 둬야 해?
A. 그 State를 사용하는 Component들의 가장 가까운 공통 부모에 두는 것이 기본이다.

Q. 모든 State를 Page에 둬도 돼?
A. 권장하지 않는다. Page가 너무 많은 책임을 가지면 Overgrown Component가 될 수 있다.

Q. 모든 State를 전역 상태로 만들면 안 돼?
A. 반복 공유가 명확하지 않다면 권장하지 않는다. 전역 상태는 변경 추적과 의존성을 복잡하게 만들 수 있다.

Q. UI Section Boundary가 뭐야?
A. 화면에서 의미 있는 UI 영역을 기준으로 Component를 나누는 방식이다.

Q. Search, Filter, List는 Component로 나누는 게 좋아?
A. 각 영역이 독립적인 책임과 이벤트를 가지면 Component로 나누는 것이 좋다.

Q. 반복되는 Card는 분리하는 게 좋아?
A. 일반적으로 좋다. List는 배열 렌더링을 담당하고 Card는 단일 항목 표시를 담당하게 만들 수 있다.

Q. Component 분리 후 Props가 많아지면 좋은 설계야?
A. 아닐 수 있다. Props가 과도하게 많아지면 Boundary나 State 위치를 재검토해야 한다.

Q. Overgrown Component가 뭐야?
A. 하나의 Component가 API 요청, 상태 관리, 이벤트 처리, 여러 UI 영역 렌더링을 모두 담당해 너무 커진 Component다.

Q. Overgrown Component는 어떻게 해결해?
A. UI 영역별 Component 분리, API 함수 분리, Custom Hook 분리, State Ownership 재검토 순서로 해결한다.

Q. Under-Splitting이 뭐야?
A. Component를 충분히 분리하지 않아 하나의 Component가 너무 많은 책임을 갖는 문제다.

Q. Over-Splitting이 뭐야?
A. 필요 이상으로 Component를 나누어 Props 전달과 파일 수만 늘어나는 문제다.

Q. 적절한 Component 분리 기준은 뭐야?
A. 책임이 명확하고 독립적인 UI 영역이거나 반복되거나 복잡도를 줄일 때 분리한다.

Q. Frontend Agent는 Component 설계 시 뭘 먼저 해야 해?
A. 화면 요구사항 분석 후 Component Responsibility, Boundary, State Ownership, Props Contract를 먼저 설계해야 한다.

Q. Component Tree에는 무엇이 포함돼야 해?
A. Component 이름, 책임, Props, State Owner, 하위 Component 관계가 포함되어야 한다.

Q. Review Agent는 React Component 설계에서 뭘 검토해야 해?
A. 책임 분리, Boundary 적절성, State Ownership, Props Contract, API Logic 분리 여부를 검토해야 한다.

Q. Component Boundary 검수 Checklist는 뭐야?
A. 책임 명확성, 이름 적절성, 역할 구분, State Owner, Props Contract, API Logic 분리, 과도한 분리 여부를 확인한다.

Q. React Component Design Part01의 핵심은 뭐야?
A. Component Responsibility와 Component Boundary를 기준으로 화면을 유지보수 가능한 Component 구조로 분해하는 것이다.
