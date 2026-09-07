# React Component Design Domain Rules

---

# 1. Domain Purpose

## 1.1 Purpose

### [개념]

React Component Design Domain 문서는 Frontend Agent / Review Agent / PM Agent용 RAG 문서 제작 규칙이다.

목적:

- React Component 설계 기준 제공
- Component 분리 기준 제공
- Page Component / UI Component 역할 구분
- Props 설계 기준 제공
- State 위치 결정 기준 제공
- Reusable Component 작성 지원
- Presentational / Container 분리 기준 제공
- Component Composition 설계 지원
- Custom Hook 분리 기준 제공
- React TypeScript Component 설계 지원
- 유지보수 가능한 Frontend 구조 생성 지원

---

### [핵심]

우선순위:

1. Component Responsibility
2. Component Boundary
3. Props Design
4. State Ownership
5. Component Composition
6. Reusable UI Component
7. Page / Feature / UI Component Separation
8. Container / Presentational Pattern
9. Custom Hook Extraction
10. TypeScript Props Type
11. Accessibility in Component
12. Maintainability

---

### [실무]

2026 실무 기준에서 React Component Design 문서는 단순 Component 작성법 문서가 아니다.

Frontend Agent가 아래 작업을 수행할 수 있도록 작성한다.

- 화면을 Component 단위로 분해
- Component 책임과 경계 설정
- Props 구조 설계
- State 위치 결정
- 재사용 가능한 UI Component 작성
- Page / Feature / UI Component 분리
- API 호출 로직과 UI 로직 분리
- Custom Hook 분리 판단
- TypeScript Props Type 설계
- Component 유지보수성 검토
- 과도한 Props Drilling 감지
- Component Anti Pattern 검출

---

### [FAQ]

Q. React Component Design 문서는 React Core와 뭐가 달라?

A.
React Core는 Component, Props, State, Hook 기본 사용법이고 React Component Design은 Component를 어떻게 나누고 설계할지에 집중한다.

Q. Component Design에서 가장 중요한 기준은 뭐야?

A.
Component Responsibility, Component Boundary, Props Design, State Ownership, Reusability, Composition이다.

Q. Component는 작게 많이 나누면 무조건 좋아?

A.
아니다. 책임이 명확하거나 재사용 가능하거나 복잡도를 줄일 때 분리한다. 무의미한 과분리는 피한다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

React Component Design 문서는 React 화면 설계와 Component 구조화에 필요한 범위를 포함한다.

포함 범위:

- Component Responsibility
- Component Boundary
- Component Naming
- Component File Structure
- Page Component
- Feature Component
- UI Component
- Layout Component
- Container Component
- Presentational Component
- Component Composition
- Props Design
- Props Naming
- Callback Props
- Children Pattern
- Controlled Component
- Uncontrolled Component Basics
- State Ownership
- Lifting State Up
- Derived State Avoidance
- Custom Hook Extraction
- API Logic Separation
- UI Logic Separation
- Reusable Component
- Component TypeScript Props
- Compound Component Basics
- Slot-like Composition Basics
- Accessibility Component Rules
- Component Testing Readiness
- Component Review Checklist
- Common Component Anti Patterns

---

### [핵심]

반드시 포함:

- Component는 하나의 명확한 책임을 가져야 함
- Component 분리는 목적이 있어야 함
- Props는 Component 외부 계약
- State는 가장 가까운 공통 부모에 위치
- UI Component는 데이터 요청 로직을 몰라도 됨
- Page Component는 화면 조립과 데이터 흐름을 담당 가능
- 재사용 Component는 도메인 의존성을 줄임
- Custom Hook은 재사용 가능한 상태 로직 분리에 사용
- TypeScript Props Type은 Component Contract를 명확히 함

---

### [실무]

React Component Design은 React Core 이후에 적용되는 설계 문서다.

실무 연결:

```text
React Core
→ Component Responsibility
→ Component Boundary
→ Props Design
→ State Ownership
→ Component Composition
→ Custom Hook Extraction
→ Maintainable Frontend
```

---

### [FAQ]

Q. React Router도 여기서 다뤄?

A.
아니다. Page Component와 Layout Component 개념만 연결하고 Router 설정은 React Router 문서에서 다룬다.

Q. 전역 상태관리도 여기서 다뤄?

A.
아니다. State 위치 결정과 Props Drilling 감지는 다루지만 Redux, Zustand, Context 심화는 State Management 문서에서 다룬다.

Q. Design System도 여기서 다뤄?

A.
아니다. 재사용 UI Component 기초만 다루고 Design System 심화는 별도 문서에서 다룬다.

---

## 2.2 Excluded Scope

### [개념]

React Component Design 문서에서는 고급 Architecture와 외부 라이브러리 심화를 제외한다.

제외 범위:

- React Router 상세 설정
- Redux / Zustand / Recoil 심화
- TanStack Query 심화
- React Hook Form 심화
- Design System 심화
- Storybook 심화
- Advanced Compound Component
- Render Props Pattern 심화
- Headless UI Library 제작 심화
- Micro Frontend
- Next.js Server Component
- SSR / SSG / ISR
- Performance Optimization 심화
- React Testing Library 상세
- Visual Regression Testing

---

### [핵심]

제외 이유:

- Component Design Foundation 범위 초과
- Router / State / Data Fetching / Testing 문서와 분리 필요
- Agent Retrieval 혼선 방지
- Chunk 품질 유지
- Component 설계 원칙에 집중

---

### [실무]

고급 기술은 별도 Domain Rules에서 관리한다.

예:

```text
React Component Design
→ React Router
→ State Management
→ Data Fetching
→ UI Component Pattern
→ Frontend Architecture
```

---

### [FAQ]

Q. Compound Component Pattern은 여기서 다뤄?

A.
기초 개념과 사용 기준은 가능하지만 심화 구현은 UI Component Pattern 문서가 적합하다.

Q. Storybook은 여기서 다뤄?

A.
아니다. Component 문서화와 시각 테스트는 Frontend Testing 또는 Design System 문서에서 다룬다.

Q. TanStack Query는 여기서 다뤄?

A.
아니다. API 데이터 상태 관리는 Data Fetching & REST API Integration 문서에서 다룬다.

---

# 3. Section Priority

## 3.1 Required Sections

### [개념]

React Component Design RAG 문서는 모든 주요 Chunk에 아래 Section을 우선 포함한다.

Required:

- [개념]
- [핵심]
- [실무]
- [FAQ]

---

### [핵심]

필수 Section 목적:

- [개념]: 정의와 역할
- [핵심]: 검색 친화 키워드
- [실무]: 실제 Component 설계 기준
- [FAQ]: 사용자 질문 매칭 강화

---

### [실무]

각 문서는 아래 구조를 기본으로 한다.

```md
# Topic

## Sub Topic

### [개념]

### [핵심]

### [실무]

### [FAQ]
```

---

### [FAQ]

Q. 모든 Component Design 문서에 FAQ가 필요해?

A.
필요하다. FAQ는 사용자 질문과 RAG 검색 매칭을 강화한다.

Q. [면접] 섹션을 써도 돼?

A.
안 된다. 반드시 [FAQ] 섹션을 사용한다.

---

## 3.2 Recommended Sections

### [개념]

React Component Design 문서에는 설계 판단과 검증을 위해 추가 Section을 포함할 수 있다.

Strongly Recommended:

- [Flow]
- [예제]
- [주의]
- [Best Practice]
- [Troubleshooting]
- [Checklist]
- [Comparison]

---

### [핵심]

추천 Section 사용 기준:

- Component 분리 기준 → [Flow], [Checklist]
- Props Design → [예제], [주의], [Best Practice]
- State Ownership → [Flow], [Comparison]
- Custom Hook 분리 → [Flow], [예제]
- Anti Pattern → [Troubleshooting]
- Page / UI Component 차이 → [Comparison]

---

### [실무]

예시:

```md
### [Flow]

Screen Requirement
→ Identify UI Sections
→ Define Component Responsibility
→ Decide State Owner
→ Design Props Contract
→ Compose Components
```

---

### [FAQ]

Q. Component Design 문서에 Checklist가 중요한 이유는?

A.
Component 분리, Props 설계, State 위치 같은 설계 판단을 일관되게 검수하기 위해 필요하다.

Q. Comparison은 언제 쓰면 좋아?

A.
Page vs UI Component, Props vs State, Container vs Presentational처럼 헷갈리는 설계 기준을 비교할 때 사용한다.

---

# 4. Component Responsibility Rules

## 4.1 Single Responsibility Component

### [개념]

Single Responsibility Component는 하나의 Component가 하나의 명확한 역할을 가지도록 설계하는 원칙이다.

Component 책임 예:

- 데이터 로딩
- 화면 레이아웃
- 카드 표시
- 버튼 표시
- 입력 처리
- 목록 렌더링
- 상태별 UI 처리

---

### [핵심]

반드시 설명:

- Component는 하나의 주요 책임을 가져야 함
- UI 표시와 데이터 요청은 분리 가능
- Component가 너무 많은 역할을 가지면 분리 검토
- Component 이름은 책임을 드러내야 함
- 책임이 불명확한 Component는 유지보수 어려움

---

### [실무]

나쁜 예:

```jsx
function FestivalPage() {
  // API call
  // search form logic
  // filter logic
  // card markup
  // modal logic
  // pagination logic
  return null;
}
```

개선 방향:

```text
FestivalPage
→ FestivalSearchForm
→ FestivalFilterPanel
→ FestivalList
→ FestivalCard
→ FestivalPagination
```

분리 기준:

- JSX가 너무 길어짐
- State가 너무 많음
- Event Handler가 너무 많음
- 특정 UI 영역이 독립적으로 이해 가능
- 재사용 가능성이 있음
- 테스트 단위로 분리 가능

---

### [FAQ]

Q. Component는 언제 분리해야 해?

A.
책임이 많아지거나, JSX가 길어지거나, 재사용 가능하거나, 특정 영역을 독립적으로 이해할 수 있을 때 분리한다.

Q. Component를 너무 많이 나누면 안 좋아?

A.
그럴 수 있다. 책임 없는 과분리는 파일 이동과 Props 전달만 늘려 복잡도를 높인다.

Q. Component 이름은 어떻게 지어야 해?

A.
역할을 드러내는 이름을 사용한다. FestivalCard, SearchForm, FilterPanel처럼 의미가 명확해야 한다.

---

## 4.2 Component Boundary Rules

### [개념]

Component Boundary는 Component를 어디서 나누고 어떤 책임을 맡길지 결정하는 경계다.

---

### [핵심]

Boundary 판단 기준:

- UI 영역 기준
- 데이터 흐름 기준
- State 소유 기준
- 재사용 가능성 기준
- 도메인 기능 기준
- 변경 가능성 기준
- 테스트 가능성 기준

---

### [실무]

Component Boundary Flow:

```text
Screen Analyze
→ Identify Repeated UI
→ Identify State Owner
→ Identify Event Source
→ Identify Data Dependency
→ Split Component
→ Define Props Contract
```

예:

```text
FestivalPage
- 데이터 요청
- 검색 조건 State
- 목록 데이터 State

FestivalSearchForm
- keyword 입력
- submit 이벤트

FestivalList
- 목록 표시

FestivalCard
- 축제 카드 표시
```

주의:

- 데이터가 필요한 곳과 표시하는 곳을 구분
- 너무 깊은 Component 계층 주의
- Props 전달만 하는 중간 Component 증가 주의
- 재사용성을 과도하게 예측하지 않음

---

### [FAQ]

Q. Component Boundary는 뭘 기준으로 잡아?

A.
UI 영역, State 소유자, 데이터 의존성, 재사용 가능성, 변경 가능성을 기준으로 잡는다.

Q. 중간 Component가 Props만 전달하면 문제야?

A.
항상 문제는 아니지만 Props Drilling이 깊어지면 구조 개선을 검토해야 한다.

---

# 5. Component Category Rules

## 5.1 Page Component Rules

### [개념]

Page Component는 라우트나 화면 단위를 대표하는 Component다.

Page Component는 화면 조립, 데이터 흐름, 주요 State 관리를 담당할 수 있다.

---

### [핵심]

역할:

- 화면 단위 구성
- Feature Component 조립
- API 호출 시작점 가능
- URL parameter 사용 가능
- 주요 State 소유 가능
- loading / error / empty 상태 분기 가능
- Layout 연결 가능

---

### [실무]

예:

```jsx
function FestivalPage() {
  const [festivals, setFestivals] = useState([]);
  const [keyword, setKeyword] = useState("");

  return (
    <main>
      <FestivalSearchForm onSearch={setKeyword} />
      <FestivalList festivals={festivals} />
    </main>
  );
}
```

권장:

- Page는 화면 조립자 역할
- 세부 UI는 하위 Component로 분리
- Page에 모든 markup을 몰아넣지 않음
- API 호출 함수가 길면 api 파일 또는 custom hook으로 분리
- Route와 연결되는 Component는 pages 폴더에 배치

---

### [FAQ]

Q. Page Component는 뭘 담당해?

A.
화면 단위 조립, 주요 데이터 흐름, 주요 State, loading/error/empty 상태 분기를 담당할 수 있다.

Q. Page Component에 API 호출이 있어도 돼?

A.
기본 패턴에서는 가능하다. 복잡하거나 재사용되면 api 함수나 custom hook으로 분리한다.

---

## 5.2 Feature Component Rules

### [개념]

Feature Component는 특정 도메인 기능 단위를 담당하는 Component다.

예:

- FestivalSearchForm
- FestivalFilterPanel
- ReviewForm
- NotificationList
- ChatRoomPanel

---

### [핵심]

역할:

- 특정 기능 UI
- 도메인 데이터 사용 가능
- Event Handler 보유 가능
- 하위 UI Component 조립
- Page보다 작고 UI Component보다 도메인 의존적

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
      <Button type="submit">Search</Button>
    </form>
  );
}
```

권장:

- 도메인 기능 이름 사용
- 내부 State 보유 가능
- 외부에 필요한 결과는 callback props로 전달
- 공통 Button, Input, Card 같은 UI Component 조합
- Feature 폴더로 묶는 구조 가능

---

### [FAQ]

Q. Feature Component는 UI Component와 뭐가 달라?

A.
Feature Component는 특정 도메인 기능에 의존하고, UI Component는 도메인과 무관하게 재사용 가능해야 한다.

Q. Feature Component는 State를 가져도 돼?

A.
가능하다. 해당 기능 내부에서만 필요한 State는 Feature Component가 소유할 수 있다.

---

## 5.3 UI Component Rules

### [개념]

UI Component는 도메인과 무관하게 재사용 가능한 표시 중심 Component다.

예:

- Button
- Input
- Card
- Modal
- Badge
- Spinner
- EmptyState

---

### [핵심]

역할:

- 재사용 가능한 UI
- 도메인 로직 최소화
- API 호출 금지
- 외부 데이터 요청 몰라도 됨
- Props 기반 표시
- 접근성 기본 포함
- 스타일 일관성 제공

---

### [실무]

예:

```jsx
function Button({
  type = "button",
  variant = "primary",
  disabled = false,
  children,
  onClick,
}) {
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

권장:

- 도메인 이름 제거
- API 로직 제거
- 재사용 가능한 props 설계
- disabled, type, aria 속성 고려
- children 지원 고려
- 스타일 variant 명확화

금지:

- Button 내부에서 특정 API 호출
- Card 내부에서 특정 도메인 fetch
- Modal 내부에서 특정 페이지 이동 강제
- UI Component가 전역 상태에 직접 강하게 의존

---

### [FAQ]

Q. UI Component는 API 호출을 해도 돼?

A.
권장하지 않는다. UI Component는 표시와 상호작용만 담당하고 데이터 요청은 Page, Feature, Hook, API 계층에서 처리한다.

Q. UI Component 이름에 도메인 이름을 넣어도 돼?

A.
도메인 전용이면 Feature Component에 가깝다. 공통 UI Component는 Button, Card, Modal처럼 범용 이름이 좋다.

---

## 5.4 Layout Component Rules

### [개념]

Layout Component는 화면의 공통 구조를 담당하는 Component다.

예:

- AppLayout
- Header
- Sidebar
- Footer
- PageContainer
- SectionLayout

---

### [핵심]

역할:

- 공통 페이지 구조
- Header / Footer / Sidebar 배치
- children 렌더링
- 공통 여백 / 폭 / 영역 관리
- Router Outlet 연결 가능
- 도메인 로직 최소화

---

### [실무]

예:

```jsx
function PageLayout({ children }) {
  return (
    <div className="page-layout">
      <Header />
      <main className="page-main">{children}</main>
      <Footer />
    </div>
  );
}
```

권장:

- children 기반 조합
- 공통 레이아웃 책임만 유지
- 데이터 로직 최소화
- 접근성 landmark 고려
- main, nav, header, footer semantic tag 사용

---

### [FAQ]

Q. Layout Component는 언제 만들어?

A.
여러 페이지에서 공통으로 사용하는 Header, Footer, Sidebar, main 영역 구조가 있을 때 만든다.

Q. Layout Component에 페이지 데이터를 넣어도 돼?

A.
공통 레이아웃 목적이면 페이지별 도메인 데이터는 넣지 않는 것이 좋다.

---

# 6. Props Design Rules

## 6.1 Props Contract Rules

### [개념]

Props Contract는 부모 Component와 자식 Component 사이의 데이터 전달 계약이다.

Props는 Component가 외부에서 무엇을 받아야 하는지 정의한다.

---

### [핵심]

반드시 포함:

- required props
- optional props
- callback props
- children
- default value
- TypeScript Props Type
- readonly concept
- stable props shape

---

### [실무]

좋은 Props 예:

```tsx
type FestivalCardProps = {
  festivalId: number;
  title: string;
  imageUrl: string | null;
  region: string;
  onSelect: (festivalId: number) => void;
};

function FestivalCard({
  festivalId,
  title,
  imageUrl,
  region,
  onSelect,
}: FestivalCardProps) {
  return (
    <article>
      {imageUrl && <img src={imageUrl} alt={title} />}
      <h2>{title}</h2>
      <p>{region}</p>
      <button type="button" onClick={() => onSelect(festivalId)}>
        Detail
      </button>
    </article>
  );
}
```

권장:

- 필요한 값만 전달
- callback props는 명확한 parameter 사용
- boolean props는 의미 명확화
- optional props에는 기본값 고려
- props type은 Component 계약으로 관리

---

### [FAQ]

Q. Props는 객체 하나로 넘기는 게 좋아, 필요한 값만 넘기는 게 좋아?

A.
Component 성격에 따라 다르다. 도메인 Card는 객체를 받을 수 있고, 범용 UI Component는 필요한 값만 명확히 받는 편이 좋다.

Q. Props Type은 왜 중요해?

A.
Component가 외부에서 요구하는 데이터 구조를 명확히 해 잘못된 사용을 줄인다.

---

## 6.2 Props Naming Rules

### [개념]

Props Naming은 Component 사용 의도를 드러내는 이름을 붙이는 규칙이다.

---

### [핵심]

권장 Naming:

- Event callback: `onClick`, `onSubmit`, `onSelect`, `onChange`
- Internal handler: `handleClick`, `handleSubmit`
- Boolean props: `isOpen`, `isActive`, `disabled`, `loading`
- Data props: `title`, `items`, `value`, `festival`
- Render content: `children`, `header`, `footer`

---

### [실무]

좋은 예:

```tsx
type ModalProps = {
  isOpen: boolean;
  title: string;
  onClose: () => void;
  children: ReactNode;
};
```

나쁜 예:

```tsx
type ModalProps = {
  open: boolean;
  data: string;
  close: () => void;
};
```

주의:

- 모호한 props 이름 금지
- data, info, item 남용 금지
- boolean props는 true/false 의미가 명확해야 함
- callback props는 `on` prefix 권장

---

### [FAQ]

Q. callback props 이름은 어떻게 짓는 게 좋아?

A.
외부에서 전달받는 callback은 onSelect, onSubmit처럼 `on` prefix를 사용하고 내부 함수는 handleSelect처럼 짓는 것이 좋다.

Q. boolean props 이름은 어떻게 짓는 게 좋아?

A.
isOpen, isActive, loading, disabled처럼 true/false 의미가 명확해야 한다.

---

## 6.3 Callback Props Rules

### [개념]

Callback Props는 자식 Component에서 발생한 이벤트나 결과를 부모 Component에 전달하기 위한 함수 props다.

---

### [핵심]

필수 포함:

- onClick
- onChange
- onSubmit
- onSelect
- callback parameter
- parent state update
- child event notification
- inversion of control

---

### [실무]

예:

```jsx
function FestivalCard({ festivalId, title, onSelect }) {
  return (
    <button type="button" onClick={() => onSelect(festivalId)}>
      {title}
    </button>
  );
}

function FestivalPage() {
  function handleSelect(festivalId) {
    console.log(festivalId);
  }

  return (
    <FestivalCard
      festivalId={1}
      title="Spring Festival"
      onSelect={handleSelect}
    />
  );
}
```

권장:

- 자식은 이벤트 발생만 알림
- 부모가 실제 상태 변경이나 이동 처리
- callback parameter는 최소한으로 전달
- 함수 이름은 의도 중심
- UI Component는 동작 결과를 강제하지 않음

---

### [FAQ]

Q. 자식 Component가 부모 State를 직접 바꿀 수 있어?

A.
직접 바꿀 수 없다. 부모가 callback props를 전달하고 자식은 그 함수를 호출한다.

Q. callback props에는 어떤 값을 넘겨야 해?

A.
부모가 다음 작업을 수행하는 데 필요한 최소한의 값만 넘기는 것이 좋다.

---

## 6.4 Boolean Props Rules

### [개념]

Boolean Props는 true 또는 false로 Component 상태나 변형을 제어하는 props다.

예:

```tsx
type ButtonProps = {
  disabled?: boolean;
  loading?: boolean;
};
```

---

### [핵심]

주의 대상:

- isOpen
- isActive
- disabled
- loading
- selected
- checked
- multiple boolean props
- impossible state

---

### [실무]

나쁜 예:

```tsx
type AlertProps = {
  success?: boolean;
  warning?: boolean;
  error?: boolean;
};
```

문제:

- success와 error가 동시에 true일 수 있음
- 불가능한 상태 발생

개선:

```tsx
type AlertVariant = "success" | "warning" | "error";

type AlertProps = {
  variant: AlertVariant;
};
```

권장:

- 상호 배타 상태는 union 값 사용
- boolean props가 많아지면 variant 검토
- true/false 의미가 명확한 경우에만 사용

---

### [FAQ]

Q. Boolean Props가 많으면 왜 문제야?

A.
서로 동시에 true가 될 수 있어 불가능한 상태가 생기고 Component 동작을 예측하기 어려워진다.

Q. success, error 같은 상태는 boolean으로 둬도 돼?

A.
하나만 선택되어야 하는 상태라면 `variant: "success" | "error"` 같은 union 방식이 더 안전하다.

---

# 7. State Ownership Rules

## 7.1 State Ownership

### [개념]

State Ownership은 어떤 Component가 State를 소유하고 변경할 책임을 가지는지 결정하는 기준이다.

---

### [핵심]

State 위치 결정 기준:

- State를 사용하는 Component
- State를 변경하는 Component
- State를 공유하는 Component들의 가장 가까운 공통 부모
- API 데이터를 소유하는 화면 단위
- URL과 동기화할 필요 여부
- 전역 상태 필요 여부

---

### [실무]

State Ownership Flow:

```text
Identify State
→ Find Components That Need It
→ Find Closest Common Parent
→ Place State There
→ Pass Data Down
→ Pass Callback Down
```

예:

```text
FestivalPage owns selectedFestivalId
→ FestivalList receives selectedFestivalId
→ FestivalCard receives isSelected
→ FestivalCard calls onSelect
```

주의:

- 너무 아래에 두면 형제 Component가 공유하기 어려움
- 너무 위에 두면 불필요한 Props 전달 증가
- 전역 상태로 너무 빨리 올리지 않음
- URL 상태와 UI 상태 구분

---

### [FAQ]

Q. State는 어디에 둬야 해?

A.
그 State를 사용하는 Component들의 가장 가까운 공통 부모에 두는 것이 기본이다.

Q. 모든 State를 최상위 App에 두면 안 돼?

A.
권장하지 않는다. 불필요한 Props 전달과 Re-render 범위가 커질 수 있다.

---

## 7.2 Lifting State Up Rules

### [개념]

Lifting State Up은 여러 Component가 같은 State를 공유해야 할 때 State를 공통 부모로 올리는 패턴이다.

---

### [핵심]

사용 상황:

- 형제 Component가 같은 값 필요
- 한 Component 입력이 다른 Component에 영향
- 부모가 자식의 선택 결과를 알아야 함
- 검색 조건이 목록 데이터에 영향
- Form과 Preview가 같은 데이터 사용

---

### [실무]

예:

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

권장:

- 공유가 필요한 순간에만 올림
- 너무 일찍 전역 상태로 만들지 않음
- callback props로 자식 이벤트 전달
- State Owner를 명확히 함

---

### [FAQ]

Q. Lifting State Up은 언제 해?

A.
여러 Component가 같은 State를 읽거나 변경 결과를 공유해야 할 때 한다.

Q. State를 올리면 Props가 많아지지 않아?

A.
그럴 수 있다. 깊어지면 Component 구조, Context, 전역 상태를 검토한다.

---

## 7.3 Local State vs Shared State Rules

### [개념]

Local State는 특정 Component 내부에서만 필요한 State다.

Shared State는 여러 Component가 함께 사용하는 State다.

---

### [핵심]

Local State 예:

- input focus
- dropdown open
- modal 내부 step
- hover-like UI 상태
- 내부 form 임시값

Shared State 예:

- login user
- selected item
- search filter
- cart items
- API list data shared by multiple sections

---

### [실무]

비교:

| 비교 | Local State            | Shared State             |
| ---- | ---------------------- | ------------------------ |
| 범위 | 특정 Component 내부    | 여러 Component           |
| 위치 | 사용하는 Component     | 공통 부모 또는 전역      |
| 예   | input value, open 여부 | 로그인 사용자, 검색 조건 |
| 위험 | 외부 동기화 어려움     | Props 전달 증가          |

권장:

- 가능한 가까운 곳에 State 배치
- 공유 필요성이 생기면 위로 올림
- 전역 상태는 마지막에 검토
- 서버 데이터 상태와 UI 상태 구분

---

### [FAQ]

Q. Local State와 Shared State 차이는?

A.
Local State는 한 Component 내부에서만 필요하고 Shared State는 여러 Component가 함께 사용한다.

Q. 전역 상태는 언제 써?

A.
여러 페이지나 깊은 Component 트리에서 반복적으로 필요한 상태일 때 검토한다.

---

# 8. Component Composition Rules

## 8.1 Composition Basics

### [개념]

Component Composition은 작은 Component를 조합해 큰 화면을 만드는 설계 방식이다.

React에서는 상속보다 Composition을 우선한다.

---

### [핵심]

필수 포함:

- parent component
- child component
- children
- props composition
- layout composition
- feature composition
- reusable component

---

### [실무]

Composition Flow:

```text
Page
→ Feature Section
→ List
→ Card
→ Button / Badge / Image
```

예:

```jsx
function FestivalPage() {
  return (
    <PageLayout>
      <FestivalSearchSection />
      <FestivalRecommendationSection />
      <FestivalListSection />
    </PageLayout>
  );
}
```

권장:

- 큰 화면을 의미 있는 구역으로 나눔
- 공통 wrapper는 children 사용
- 도메인 Component와 범용 UI Component 구분
- 조합으로 변형을 처리하고 상속 사용 지양

---

### [FAQ]

Q. React에서 상속보다 Composition을 쓰는 이유는?

A.
Component를 조합하는 방식이 UI 재사용과 변경에 더 유연하기 때문이다.

Q. Composition은 언제 중요해?

A.
여러 UI 조각을 조합해 페이지를 만들거나 공통 Layout / Card / Modal을 재사용할 때 중요하다.

---

## 8.2 Children Composition Rules

### [개념]

Children Composition은 Component 내부 내용을 외부에서 전달해 유연하게 조합하는 패턴이다.

---

### [핵심]

적합 상황:

- Layout
- Card
- Modal
- Section
- Button
- FormGroup
- Tabs basics
- Wrapper Component

---

### [실무]

예:

```tsx
type CardProps = {
  title?: string;
  children: ReactNode;
};

function Card({ title, children }: CardProps) {
  return (
    <section className="card">
      {title && <h2>{title}</h2>}
      {children}
    </section>
  );
}
```

사용:

```tsx
<Card title="Festival Info">
  <p>Festival description</p>
  <Button>Detail</Button>
</Card>
```

주의:

- children 구조가 너무 암묵적이면 명시적 props 검토
- 접근성 구조를 깨지 않도록 설계
- children과 variant 조합이 복잡하면 Component 분리 검토

---

### [FAQ]

Q. children을 쓰면 뭐가 좋아?

A.
Component 내부 내용을 외부에서 자유롭게 구성할 수 있어 재사용성과 조합성이 좋아진다.

Q. children보다 props가 나은 경우도 있어?

A.
있다. 구조가 고정되어 있고 필요한 데이터가 명확하면 명시적 props가 더 읽기 쉽다.

---

## 8.3 Slot-like Props Rules

### [개념]

Slot-like Props는 header, footer, action처럼 특정 영역에 ReactNode를 전달해 Component를 조합하는 방식이다.

---

### [핵심]

사용 대상:

- modal header / footer
- card action
- page toolbar
- list empty view
- table action area
- layout aside

---

### [실무]

예:

```tsx
type PanelProps = {
  title: string;
  actions?: ReactNode;
  children: ReactNode;
};

function Panel({ title, actions, children }: PanelProps) {
  return (
    <section className="panel">
      <header className="panel-header">
        <h2>{title}</h2>
        {actions}
      </header>
      <div className="panel-content">{children}</div>
    </section>
  );
}
```

장점:

- 특정 영역만 외부에서 커스터마이징 가능
- children보다 구조가 명확함
- Compound Component보다 단순함

주의:

- slot props가 너무 많으면 복잡도 증가
- ReactNode props 이름 명확화
- 접근성 구조 유지

---

### [FAQ]

Q. Slot-like Props는 언제 써?

A.
Card, Modal, Panel처럼 특정 영역만 외부에서 커스터마이징하고 싶을 때 사용한다.

Q. children과 Slot-like Props 차이는?

A.
children은 전체 본문을 전달하고 Slot-like Props는 header, action, footer 같은 특정 영역을 전달한다.

---

# 9. Container and Presentational Rules

## 9.1 Container Component Rules

### [개념]

Container Component는 데이터 로딩, State 관리, 이벤트 흐름을 담당하는 Component다.

---

### [핵심]

역할:

- API 요청
- State 관리
- Event Handler 정의
- 데이터 변환
- UI Component에 props 전달
- loading / error / empty 상태 판단

---

### [실무]

예:

```jsx
function FestivalListContainer() {
  const [festivals, setFestivals] = useState([]);
  const [loading, setLoading] = useState(false);

  return <FestivalList festivals={festivals} loading={loading} />;
}
```

권장:

- 데이터와 흐름을 관리
- 표시 전용 Component와 분리 가능
- 너무 많은 Container 생성은 지양
- Page Component가 Container 역할을 할 수도 있음

---

### [FAQ]

Q. Container Component는 꼭 만들어야 해?

A.
아니다. 복잡한 데이터 흐름이 있을 때 유용하다. 단순 화면에서는 Page Component가 역할을 겸할 수 있다.

Q. Container Component는 UI를 렌더링하지 않아?

A.
일부 렌더링할 수 있지만 핵심 역할은 데이터와 흐름 관리다.

---

## 9.2 Presentational Component Rules

### [개념]

Presentational Component는 전달받은 Props를 기반으로 UI를 표시하는 Component다.

---

### [핵심]

역할:

- UI 표시
- Props 기반 렌더링
- 도메인 로직 최소화
- API 호출 없음
- 재사용성 높음
- 테스트 쉬움

---

### [실무]

예:

```tsx
type FestivalListProps = {
  festivals: Festival[];
  loading: boolean;
};

function FestivalList({ festivals, loading }: FestivalListProps) {
  if (loading) {
    return <p>Loading...</p>;
  }

  return (
    <section>
      {festivals.map((festival) => (
        <FestivalCard key={festival.festivalId} festival={festival} />
      ))}
    </section>
  );
}
```

권장:

- Props Contract 명확화
- 외부 API 구조 직접 의존 줄이기
- 표시 로직 중심
- callback props로 이벤트 알림

---

### [FAQ]

Q. Presentational Component는 State를 가지면 안 돼?

A.
항상 금지는 아니다. UI 내부 open 여부 같은 Local State는 가질 수 있다. 다만 데이터 흐름과 API 로직은 최소화한다.

Q. Presentational Component의 장점은 뭐야?

A.
재사용성과 테스트 가능성이 높고 UI 표시 책임이 명확하다.

---

## 9.3 Container vs Presentational Comparison

### [개념]

Container / Presentational 분리는 데이터 흐름과 UI 표시를 분리하는 설계 방식이다.

---

### [핵심]

비교:

| 비교     | Container Component       | Presentational Component |
| -------- | ------------------------- | ------------------------ |
| 역할     | 데이터 / 상태 / 흐름 관리 | UI 표시                  |
| API 호출 | 가능                      | 지양                     |
| State    | 주요 State 가능           | Local UI State 정도      |
| 재사용성 | 낮거나 중간               | 높음                     |
| 테스트   | 흐름 테스트               | 표시 테스트              |
| Props    | 하위 Component에 전달     | 외부에서 받음            |

---

### [실무]

사용 기준:

- 화면이 단순하면 분리하지 않아도 됨
- API / 상태 / UI가 섞여 복잡해지면 분리
- Page Component가 Container 역할을 할 수 있음
- UI Component는 Presentational 성격 유지

---

### [FAQ]

Q. Container / Presentational Pattern은 항상 써야 해?

A.
아니다. 복잡도를 줄일 때만 사용한다. 단순한 Component에는 오히려 과한 설계가 될 수 있다.

Q. Page Component는 Container야?

A.
많은 경우 Page Component가 Container 역할을 할 수 있다.

---

# 10. Custom Hook Design Rules

## 10.1 Custom Hook Extraction Rules

### [개념]

Custom Hook은 Component에서 재사용 가능한 상태 로직이나 Effect 로직을 분리한 함수다.

Custom Hook 이름은 `use`로 시작한다.

---

### [핵심]

분리 대상:

- 반복되는 State Logic
- API Fetch Logic
- Form Logic
- Browser Event Logic
- Timer Logic
- LocalStorage Logic
- Complex Effect Logic

---

### [실무]

분리 전:

```jsx
function FestivalPage() {
  const [festivals, setFestivals] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    // fetch logic
  }, []);

  return null;
}
```

분리 후:

```jsx
function useFestivals() {
  const [festivals, setFestivals] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  return { festivals, loading, error };
}

function FestivalPage() {
  const { festivals, loading, error } = useFestivals();

  return <FestivalList festivals={festivals} loading={loading} error={error} />;
}
```

분리 기준:

- 여러 Component에서 재사용
- Component 로직이 길어짐
- useEffect가 복잡함
- Form 상태 로직이 반복됨
- API 요청 상태 패턴이 반복됨

---

### [FAQ]

Q. Custom Hook은 언제 만들어?

A.
상태 로직이나 Effect 로직이 반복되거나 Component를 복잡하게 만들 때 만든다.

Q. Custom Hook 이름은 왜 use로 시작해야 해?

A.
React와 lint 도구가 Hook 규칙을 검사할 수 있게 하기 위해서다.

Q. Custom Hook은 UI를 반환해?

A.
일반적으로 UI가 아니라 상태, 함수, 계산값 같은 로직 결과를 반환한다.

---

## 10.2 Custom Hook Return Rules

### [개념]

Custom Hook Return은 Hook이 Component에 어떤 상태와 함수를 제공할지 정의하는 계약이다.

---

### [핵심]

반환 방식:

- Object Return
- Array Return
- State
- Action Function
- Loading
- Error
- Data
- Refetch Function

---

### [실무]

Object Return 권장 상황:

```tsx
function useFestivals() {
  return {
    festivals,
    loading,
    error,
    refetch,
  };
}
```

Array Return 적합 상황:

```tsx
function useToggle(initialValue = false) {
  return [value, toggle] as const;
}
```

기준:

- 반환 값이 여러 개이고 이름이 중요하면 Object
- useState처럼 짧고 순서가 명확하면 Array
- API Hook은 Object Return이 읽기 쉬움
- 반환 타입 명확화

---

### [FAQ]

Q. Custom Hook은 Object로 반환하는 게 좋아?

A.
반환 값이 여러 개이고 의미가 중요하면 Object Return이 좋다.

Q. Array Return은 언제 좋아?

A.
useState처럼 반환 값의 순서와 의미가 명확하고 짧을 때 적합하다.

---

# 11. Reusable Component Rules

## 11.1 Reusable Component Criteria

### [개념]

Reusable Component는 여러 곳에서 재사용할 수 있도록 도메인 의존성을 줄이고 Props로 동작을 제어하는 Component다.

---

### [핵심]

재사용 기준:

- 여러 화면에서 반복
- 도메인 로직 없음
- Props로 데이터 주입
- variant 지원 가능
- 접근성 기본 포함
- 스타일 일관성 제공
- 단일 책임

---

### [실무]

재사용 Component 후보:

- Button
- Input
- Select
- Checkbox
- Modal
- Card
- Badge
- Spinner
- EmptyState
- ErrorMessage
- Pagination

좋은 설계:

```tsx
type EmptyStateProps = {
  title: string;
  description?: string;
  action?: ReactNode;
};

function EmptyState({ title, description, action }: EmptyStateProps) {
  return (
    <section className="empty-state">
      <h2>{title}</h2>
      {description && <p>{description}</p>}
      {action}
    </section>
  );
}
```

주의:

- 모든 Component를 처음부터 재사용 가능하게 만들 필요 없음
- 실제 반복이 보이면 추출
- 도메인 의존성을 낮춤
- variant가 많아지면 설계 재검토

---

### [FAQ]

Q. 처음부터 공통 Component를 많이 만들면 좋아?

A.
아니다. 실제 반복과 필요가 확인된 후 추출하는 것이 안전하다.

Q. Reusable Component는 도메인 데이터를 알아도 돼?

A.
가능하면 몰라야 한다. 도메인 데이터는 부모가 가공해서 props로 전달하는 것이 좋다.

---

## 11.2 Variant Design Rules

### [개념]

Variant는 Component의 시각적 또는 의미적 변형을 제한된 값으로 표현하는 방식이다.

예:

```tsx
type ButtonVariant = "primary" | "secondary" | "danger";
```

---

### [핵심]

사용 대상:

- Button variant
- Badge status
- Alert type
- Card tone
- Size
- Color intent
- Semantic variant

---

### [실무]

예:

```tsx
type ButtonProps = {
  variant?: "primary" | "secondary" | "danger";
  size?: "sm" | "md" | "lg";
  children: ReactNode;
};

function Button({ variant = "primary", size = "md", children }: ButtonProps) {
  return (
    <button className={`button button-${variant} button-${size}`}>
      {children}
    </button>
  );
}
```

권장:

- variant 값 제한
- boolean 여러 개보다 union variant 사용
- 의미 기반 variant 우선
- className 생성 규칙 명확화
- size와 intent 분리

주의:

- variant가 너무 많으면 Component 책임 과다
- 조합이 복잡하면 하위 Component 분리
- 시각 이름보다 semantic 이름 권장

---

### [FAQ]

Q. variant는 왜 써?

A.
Component 변형을 제한된 값으로 관리해 오타와 불가능한 상태를 줄이기 위해 사용한다.

Q. primary, danger 같은 이름은 괜찮아?

A.
괜찮다. 의미 기반 variant는 스타일 변경에도 의도를 유지하기 쉽다.

---

# 12. API Logic Separation Rules

## 12.1 API Logic in Component Design

### [개념]

API Logic Separation은 Component 내부의 서버 요청 로직을 api 함수나 custom hook으로 분리하는 설계 기준이다.

---

### [핵심]

분리 대상:

- fetch / axios request
- request parameter mapping
- response mapping
- error handling
- loading / error state
- retry / refetch
- pagination data loading

---

### [실무]

나쁜 예:

```jsx
function FestivalCard() {
  useEffect(() => {
    fetch("/api/festivals/1")
      .then((res) => res.json())
      .then((data) => console.log(data));
  }, []);

  return null;
}
```

개선:

```jsx
async function getFestivalDetail(festivalId) {
  const response = await fetch(`/api/festivals/${festivalId}`);

  if (!response.ok) {
    throw new Error("Failed to load festival detail");
  }

  return await response.json();
}
```

Component:

```jsx
function FestivalDetailPage({ festivalId }) {
  const [festival, setFestival] = useState(null);

  useEffect(() => {
    getFestivalDetail(festivalId).then(setFestival);
  }, [festivalId]);

  return null;
}
```

권장:

- API 호출 함수는 api 폴더로 분리
- API 상태 로직은 custom hook으로 분리 가능
- UI Component는 API 직접 호출 지양
- API Response를 화면용 데이터로 mapping 가능

---

### [FAQ]

Q. API 호출을 Component 안에 쓰면 안 돼?

A.
간단한 화면에서는 가능하지만 재사용되거나 길어지면 api 함수나 custom hook으로 분리하는 것이 좋다.

Q. UI Component에서 fetch를 하면 왜 안 좋아?

A.
UI Component가 서버 구조에 의존하게 되어 재사용성과 테스트 가능성이 떨어진다.

---

# 13. TypeScript Component Rules

## 13.1 Props Type Design

### [개념]

Props Type Design은 Component가 외부에서 받는 데이터와 callback의 타입을 명확히 정의하는 작업이다.

---

### [핵심]

필수 포함:

- Props Type
- Required Props
- Optional Props
- Callback Props
- Children Type
- ReactNode
- Event Handler Type
- Generic Component Basics

---

### [실무]

Props Type 예:

```tsx
import type { ReactNode } from "react";

type ModalProps = {
  isOpen: boolean;
  title: string;
  onClose: () => void;
  children: ReactNode;
};

function Modal({ isOpen, title, onClose, children }: ModalProps) {
  if (!isOpen) {
    return null;
  }

  return (
    <section role="dialog" aria-modal="true">
      <h2>{title}</h2>
      <button type="button" onClick={onClose}>
        Close
      </button>
      {children}
    </section>
  );
}
```

권장:

- Props Type은 Component 가까이에 작성
- 공유 타입은 별도 types 파일로 분리
- callback parameter와 return type 명확화
- children은 ReactNode 사용
- 불필요한 React.FC 강제 금지

---

### [FAQ]

Q. Props Type은 어디에 두는 게 좋아?

A.
Component 전용이면 같은 파일에 두고 여러 곳에서 공유하면 types 파일로 분리한다.

Q. children 타입은 뭐로 써?

A.
일반적으로 ReactNode를 사용한다.

Q. React.FC를 꼭 써야 해?

A.
필수는 아니다. 프로젝트 컨벤션에 따라 사용 여부를 정한다.

---

## 13.2 Generic Component Basics

### [개념]

Generic Component는 여러 데이터 타입에 재사용 가능한 Component를 만들 때 사용하는 TypeScript 패턴이다.

---

### [핵심]

사용 대상:

- Select
- List
- Table
- Combobox
- Data Renderer
- Option Component

---

### [실무]

기초 예:

```tsx
type ListProps<T> = {
  items: T[];
  getKey: (item: T) => string | number;
  renderItem: (item: T) => ReactNode;
};

function List<T>({ items, getKey, renderItem }: ListProps<T>) {
  return (
    <ul>
      {items.map((item) => (
        <li key={getKey(item)}>{renderItem(item)}</li>
      ))}
    </ul>
  );
}
```

주의:

- Foundation 단계에서는 단순 Generic만 사용
- Generic이 Component 사용성을 해치면 명시적 Component가 나음
- 너무 추상적인 Generic Component 지양
- 실제 반복 패턴이 있을 때 도입

---

### [FAQ]

Q. Generic Component는 언제 써?

A.
List, Select, Table처럼 데이터 타입은 다르지만 렌더링 구조가 반복될 때 사용한다.

Q. Generic Component를 많이 만들면 좋아?

A.
아니다. 과도한 추상화는 사용성과 가독성을 떨어뜨릴 수 있다.

---

# 14. Accessibility Component Rules

## 14.1 Component Accessibility Basics

### [개념]

Component Accessibility는 Component 단위에서 접근성 기준을 유지하는 설계다.

---

### [핵심]

필수 포함:

- semantic element
- button vs div
- label
- alt
- aria basics
- focus management
- keyboard interaction
- role
- aria-expanded
- aria-controls
- aria-modal

---

### [실무]

Button 접근성:

```tsx
function IconButton({ label, onClick, children }) {
  return (
    <button type="button" aria-label={label} onClick={onClick}>
      {children}
    </button>
  );
}
```

Modal 접근성 기초:

```tsx
<section role="dialog" aria-modal="true" aria-labelledby="modal-title">
  <h2 id="modal-title">Modal Title</h2>
</section>
```

Checklist:

```md
- [ ] 클릭 가능한 요소가 button 또는 a인가?
- [ ] input에 label이 연결되었는가?
- [ ] 이미지 alt가 적절한가?
- [ ] Modal에 dialog role이 있는가?
- [ ] Toggle에 aria-expanded가 필요한가?
- [ ] Keyboard로 조작 가능한가?
- [ ] Focus 상태가 보이는가?
```

---

### [FAQ]

Q. div에 onClick을 달아서 버튼처럼 써도 돼?

A.
권장하지 않는다. 동작 버튼은 button 태그를 사용해야 키보드 접근성과 기본 동작을 얻을 수 있다.

Q. Icon Button에는 왜 aria-label이 필요해?

A.
아이콘만으로는 스크린 리더가 버튼 목적을 알 수 없기 때문이다.

Q. aria를 많이 붙이면 접근성이 좋아져?

A.
아니다. 먼저 Semantic HTML을 사용하고 부족한 의미를 보완할 때 aria를 사용한다.

---

# 15. Styling Component Rules

## 15.1 Styling Responsibility Rules

### [개념]

Styling Responsibility는 Component가 어떤 스타일 책임을 가질지 결정하는 기준이다.

---

### [핵심]

필수 포함:

- className
- variant class
- layout style
- component style
- global style
- scoped style
- responsive style
- style prop caution

---

### [실무]

권장:

```jsx
function FestivalCard({ title, className = "" }) {
  return (
    <article className={`festival-card ${className}`}>
      <h2>{title}</h2>
    </article>
  );
}
```

기준:

- Component 자체 스타일은 Component class
- 페이지 배치는 부모 Layout에서 제어
- margin 책임은 부모가 가지는 경우가 많음
- 공통 UI는 variant class 지원 가능
- inline style 남용 금지
- className 확장 가능성 고려

주의:

- 자식 Component가 부모 layout margin을 강제하지 않음
- style prop으로 모든 스타일을 주입하지 않음
- 도메인 Component와 UI Component 스타일 책임 구분

---

### [FAQ]

Q. Component margin은 내부에서 줘도 돼?

A.
상황에 따라 다르지만 재사용 UI Component는 외부 배치 margin을 부모가 관리하는 것이 유연하다.

Q. className prop을 받아야 해?

A.
재사용 Component라면 외부 스타일 확장이 필요할 수 있어 className prop을 고려한다.

---

# 16. File Structure Rules

## 16.1 Component File Structure

### [개념]

Component File Structure는 Component, style, test, type, hook을 어떻게 배치할지 정하는 구조다.

---

### [핵심]

구조 기준:

- feature-based
- component-based
- colocate
- shared components
- pages
- hooks
- api
- types
- styles

---

### [실무]

기본 구조:

```text
src
├ pages
│  └ FestivalPage
│     └ FestivalPage.tsx
├ features
│  └ festival
│     ├ components
│     │  ├ FestivalSearchForm.tsx
│     │  └ FestivalList.tsx
│     ├ hooks
│     │  └ useFestivals.ts
│     ├ api
│     │  └ festivalApi.ts
│     └ types
│        └ festivalTypes.ts
├ components
│  ├ Button
│  │  └ Button.tsx
│  └ Modal
│     └ Modal.tsx
└ utils
```

기준:

- shared components: 도메인 무관 공통 UI
- features: 도메인 기능 단위
- pages: 라우트 화면 단위
- hooks: 재사용 로직
- api: 서버 요청 함수
- types: 공유 타입

주의:

- 프로젝트 규모에 맞게 단순화
- 작은 프로젝트에서 과한 폴더 구조 금지
- 한 파일에 모든 Component 몰아넣지 않음
- Component 파일명과 Component 이름 일치 권장

---

### [FAQ]

Q. Feature 기반 폴더 구조는 언제 좋아?

A.
도메인 기능이 많고 Component, API, Hook, Type이 함께 움직일 때 좋다.

Q. 작은 프로젝트도 features 구조를 써야 해?

A.
필수는 아니다. 작은 프로젝트는 pages, components, api, hooks 정도로 단순하게 시작해도 된다.

---

# 17. Troubleshooting Rules

## 17.1 Overgrown Component

### [개념]

Overgrown Component는 하나의 Component가 너무 많은 책임과 코드를 가지는 문제다.

---

### [핵심]

문제:

- JSX가 너무 길다
- State가 많다
- useEffect가 많다
- Event Handler가 많다
- API 로직과 UI 로직이 섞임
- 조건부 렌더링이 복잡함
- 수정 시 영향 범위가 큼

원인:

- Component 분리 기준 부재
- Page에 모든 코드 작성
- Custom Hook 분리 지연
- UI Component 추출 지연
- 데이터 로직과 표시 로직 혼합

해결:

- UI 영역별 Component 분리
- API 로직 api 파일로 분리
- 반복 상태 로직 Custom Hook 분리
- List / Card / Form 분리
- State Ownership 재검토
- Props Contract 정의

---

### [실무]

Refactoring Flow:

```text
Find Long Component
→ Identify UI Sections
→ Extract Presentational Components
→ Extract API Functions
→ Extract Custom Hook
→ Define Props Types
→ Review State Ownership
```

---

### [FAQ]

Q. Component가 너무 커졌을 때 어디부터 나눠?

A.
먼저 UI 영역을 기준으로 List, Card, Form, Modal 같은 표시 Component를 분리한다.

Q. useEffect가 많은 Component는 어떻게 해?

A.
각 Effect 목적을 검토하고 API / Timer / Event Listener 로직을 custom hook으로 분리할 수 있는지 확인한다.

---

## 17.2 Props Drilling Problem

### [개념]

Props Drilling은 여러 중간 Component를 거쳐 깊은 자식에게 Props를 계속 전달하는 문제다.

---

### [핵심]

문제:

- 중간 Component가 사용하지 않는 Props 전달
- Props 변경 시 여러 파일 수정
- Component 재사용성 저하
- 데이터 흐름 추적 어려움

원인:

- State 위치가 너무 높거나 낮음
- Component 계층이 깊음
- 공통 상태 관리 부재
- Composition 구조 부적절

해결:

- State Owner 재검토
- Component 구조 단순화
- children / composition 활용
- Context 검토
- 전역 상태 검토
- Feature 단위 구조 검토

---

### [실무]

Debug Flow:

```text
Trace Prop Path
→ Check Intermediate Usage
→ Review State Owner
→ Reduce Component Depth
→ Use Composition
→ Consider Context or Global State
```

주의:

- Props Drilling이 항상 나쁜 것은 아님
- 1~2단계 전달은 자연스러움
- 깊고 반복적이면 개선 검토

---

### [FAQ]

Q. Props Drilling은 무조건 나빠?

A.
아니다. 짧은 전달은 자연스럽다. 깊고 반복되어 유지보수가 어려워질 때 문제가 된다.

Q. Props Drilling 해결은 무조건 전역 상태야?

A.
아니다. State 위치 조정, Component Composition, Context 등 여러 방법을 먼저 검토한다.

---

## 17.3 Unclear Props Problem

### [개념]

Unclear Props Problem은 Props 이름이나 구조가 모호해서 Component 사용 의도를 알기 어려운 문제다.

---

### [핵심]

문제:

- data, item, info 같은 모호한 이름
- boolean props 의미 불명확
- callback 이름이 동작을 설명하지 않음
- optional props가 너무 많음
- props 조합으로 불가능한 상태 발생

원인:

- Props Contract 미정의
- TypeScript Props Type 부실
- Component 책임 불명확
- variant 대신 boolean 남용
- 도메인 객체를 무분별하게 전달

해결:

- Props 이름 구체화
- Props Type 정의
- callback `on` prefix 사용
- boolean 대신 union variant 사용
- Component 책임 재정의
- 필요한 값만 전달

---

### [실무]

나쁜 예:

```tsx
type Props = {
  data: any;
  flag: boolean;
  action: () => void;
};
```

좋은 예:

```tsx
type FestivalCardProps = {
  festival: FestivalSummary;
  isSelected: boolean;
  onSelect: (festivalId: number) => void;
};
```

---

### [FAQ]

Q. data라는 Props 이름은 안 좋아?

A.
항상 나쁜 것은 아니지만 의미가 모호하다. festival, user, items처럼 구체적인 이름이 더 좋다.

Q. callback 이름은 어떻게 고쳐?

A.
onSelect, onClose, onSubmit처럼 Component 외부에서 발생하는 이벤트 의미를 드러내는 이름이 좋다.

---

## 17.4 Over-Abstraction Problem

### [개념]

Over-Abstraction은 실제 필요보다 과도하게 추상화해서 Component 사용성이 떨어지는 문제다.

---

### [핵심]

문제:

- 재사용하려고 만든 Component가 이해하기 어려움
- props가 너무 많음
- variant 조합이 복잡함
- Generic Component 사용이 어렵다
- 단순한 UI 수정도 복잡함
- 실제 재사용 빈도가 낮음

원인:

- 미래 재사용성 과도 예측
- Design System 없이 공통화 남발
- Component 책임 과다
- 도메인 차이를 무시한 통합
- Generic / slot / render props 남용

해결:

- 실제 중복이 확인된 후 추출
- 단순 Component 유지
- 도메인별 Component 분리 허용
- variant 수 줄이기
- 명시적 Component가 더 나은지 검토
- 사용 예제 기준으로 API 재설계

---

### [실무]

판단 기준:

```text
Is it reused now?
→ Does abstraction reduce duplication?
→ Is props API understandable?
→ Are variants limited?
→ Is explicit component simpler?
```

---

### [FAQ]

Q. 재사용 가능하게 만들수록 좋은 거 아니야?

A.
아니다. 실제 사용성이 떨어지는 추상화는 유지보수를 어렵게 만든다.

Q. 중복 코드가 조금 있으면 바로 공통화해야 해?

A.
아니다. 반복 패턴이 명확해지고 변경 방향이 보일 때 공통화하는 것이 안전하다.

---

# 18. Comparison Rules

## 18.1 Required Comparisons

### [개념]

React Component Design 문서는 헷갈리는 설계 개념을 비교해서 작성한다.

---

### [핵심]

필수 비교 대상:

- Page Component vs UI Component
- Feature Component vs UI Component
- Container Component vs Presentational Component
- Props vs State
- Local State vs Shared State
- children vs explicit props
- callback props vs direct state update
- boolean props vs variant
- Component Composition vs Inheritance
- Custom Hook vs Utility Function
- API Function vs Custom Hook
- Reusable Component vs Domain Component
- Props Drilling vs Context
- Under-Abstraction vs Over-Abstraction

---

### [실무]

예시:

| 비교     | UI Component        | Feature Component  |
| -------- | ------------------- | ------------------ |
| 의존성   | 도메인 의존 낮음    | 도메인 의존 높음   |
| 예       | Button, Modal, Card | FestivalSearchForm |
| API 호출 | 지양                | 필요 시 가능       |
| 재사용성 | 높음                | 특정 기능 중심     |
| Props    | 범용 Props          | 도메인 Props 가능  |

---

### [FAQ]

Q. 비교 표는 왜 필요해?

A.
사용자가 자주 헷갈리는 설계 질문에서 Retrieval Hit와 답변 정확도를 높이기 위해 필요하다.

Q. Component Design 비교 문서에서 가장 중요한 것은?

A.
실무 선택 기준과 잘못 설계했을 때 생기는 문제를 함께 설명하는 것이다.

---

# 19. Checklist Rules

## 19.1 Component Design Checklist

### [개념]

React Component Design 문서 검수 시 Component 설계 체크리스트를 사용한다.

---

### [핵심]

Checklist:

```md
- [ ] Component 책임이 명확한가?
- [ ] Component 이름이 역할을 드러내는가?
- [ ] Page / Feature / UI Component 역할이 구분되는가?
- [ ] Props Contract가 명확한가?
- [ ] Props 이름이 모호하지 않은가?
- [ ] Callback Props 이름이 on prefix 기준인가?
- [ ] Boolean Props가 불가능한 상태를 만들지 않는가?
- [ ] State Owner가 적절한가?
- [ ] State를 너무 위로 올리지 않았는가?
- [ ] State를 너무 아래에 두지 않았는가?
- [ ] Derived State를 불필요하게 만들지 않았는가?
- [ ] API Logic과 UI Logic이 과도하게 섞이지 않았는가?
- [ ] 반복 로직은 Custom Hook 분리 대상인가?
- [ ] 재사용 UI Component가 도메인에 강하게 의존하지 않는가?
- [ ] children / slot-like props 사용이 적절한가?
- [ ] 접근성 기본 기준이 반영되었는가?
- [ ] Props Drilling이 과도하지 않은가?
- [ ] Over-Abstraction이 아닌가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 기준:

```text
Draft
→ Responsibility Check
→ Boundary Check
→ Props Check
→ State Ownership Check
→ Composition Check
→ Custom Hook Check
→ Anti Pattern Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

---

### [FAQ]

Q. Component Design 검수에서 가장 중요한 것은?

A.
책임, 경계, Props Contract, State Ownership, 재사용성, 접근성, Anti Pattern 포함 여부다.

---

# 20. Retrieval Optimization Rules

## 20.1 Keyword Rules

### [개념]

React Component Design 문서는 검색 매칭을 위해 핵심 키워드를 반복 허용한다.

---

### [핵심]

강조 키워드:

- React Component Design
- Component Responsibility
- Component Boundary
- Component Naming
- Page Component
- Feature Component
- UI Component
- Layout Component
- Container Component
- Presentational Component
- Component Composition
- Props Design
- Props Contract
- Props Naming
- Callback Props
- Boolean Props
- Variant
- Children
- Slot-like Props
- State Ownership
- Lifting State Up
- Local State
- Shared State
- Props Drilling
- Custom Hook
- Reusable Component
- API Logic Separation
- React TypeScript Props
- Component Accessibility
- Overgrown Component
- Over-Abstraction
- Component Anti Pattern

---

### [실무]

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

예:

- React Component는 언제 분리해?
- Component 책임은 어떻게 정해?
- Page Component와 UI Component 차이는?
- Feature Component가 뭐야?
- Props 이름은 어떻게 지어?
- callback props는 어떻게 설계해?
- State는 어디에 둬야 해?
- Lifting State Up은 언제 해?
- Props Drilling은 어떻게 해결해?
- Custom Hook은 언제 만들어?
- API 로직은 Component에서 분리해야 해?
- Reusable Component는 언제 만들어?
- children은 언제 써?
- boolean props가 많으면 왜 문제야?
- Component가 너무 커졌을 때 어떻게 나눠?
- 과도한 추상화는 왜 문제야?

---

### [FAQ]

Q. 키워드 반복은 중복이야?

A.
불필요한 장문 중복은 금지지만 Retrieval 최적화를 위한 핵심 키워드 반복은 허용된다.

Q. FAQ 질문은 어떤 스타일이 좋아?

A.
실제 사용자가 검색하거나 질문할 법한 문장형 질문이 좋다.

---

# 21. Version Rules

## 21.1 Modern React Component Design 기준

### [개념]

React Component Design 문서는 Modern React 기준으로 작성한다.

---

### [핵심]

기준:

- React 18+
- React 19 호환 고려
- Functional Component
- Hook 기반 설계
- Component Composition
- TypeScript Ready
- Props Contract 중심
- State Ownership 중심
- Custom Hook 기반 로직 분리
- Accessibility 기본 포함
- Feature-based Structure 고려

Legacy 제외:

- Class Component 중심 설계
- Inheritance 중심 설계
- mixin
- legacy context 중심 설계
- jQuery DOM 조작 기반 Component
- 모든 로직을 HOC로 처리하는 구식 패턴 중심
- 불필요한 React.FC 강제
- 과도한 render props 중심 설계

---

### [실무]

실무 기준:

```text
Modern React Component
→ Clear Responsibility
→ Props Contract
→ State Ownership
→ Composition
→ Custom Hook Extraction
→ TypeScript Ready
→ Maintainable UI
```

---

### [FAQ]

Q. React Component Design에서 class component도 고려해야 해?

A.
기존 코드 유지보수에서는 볼 수 있지만 신규 설계 문서는 Functional Component와 Hook 중심으로 작성한다.

Q. HOC는 여기서 다뤄?

A.
기초 언급은 가능하지만 현대 React Foundation에서는 Custom Hook과 Composition을 우선한다.

---

# 22. Common Mistakes

## 22.1 Component Design Common Mistakes

### [개념]

React Component Design 문서는 자주 발생하는 설계 실수를 명확히 포함해야 한다.

---

### [핵심]

자주 발생:

- 모든 코드를 Page Component에 작성
- Component 책임이 불명확함
- Component 이름이 모호함
- UI Component에서 API 호출
- Props 이름이 data, info, item으로 모호함
- callback props 이름이 불명확함
- boolean props가 너무 많음
- Props 직접 수정
- State 위치가 너무 높음
- State 위치가 너무 낮음
- Derived State 중복 저장
- Props Drilling 방치
- 모든 상태를 전역 상태로 이동
- Custom Hook 분리 지연
- Custom Hook 과도 생성
- 재사용성 과도 예측
- Generic Component 과도 추상화
- 접근성 없는 Button / Modal 작성
- className 확장성 미고려
- 작은 프로젝트에 과도한 폴더 구조 적용

---

### [실무]

문서 작성 시 Common Mistakes는 Troubleshooting과 연결한다.

예:

```text
문제: Component가 너무 커짐
원인: API 로직, Form 로직, List 렌더링, Modal 로직이 한 Component에 섞임
해결: UI Component 분리, API 함수 분리, Custom Hook 분리, State Owner 재검토
```

---

### [FAQ]

Q. React Component Design 초보가 가장 많이 하는 실수는?

A.
Page Component에 모든 코드를 넣고, Props 이름을 모호하게 짓고, State 위치를 잘못 잡는 경우가 많다.

Q. Component 설계 문제는 어떻게 찾는 게 좋아?

A.
Component 책임, Props 흐름, State 위치, API 로직 위치, 재사용성, 접근성을 순서대로 확인한다.

---

# 23. Final Goal

## 23.1 Domain Final Goal

### [개념]

React Component Design RAG 문서는 Frontend Agent가 유지보수 가능한 React Component 구조를 설계하고 검토하도록 지원해야 한다.

---

### [핵심]

최종 목표:

- Component Responsibility 정의
- Component Boundary 설정
- Page / Feature / UI Component 구분
- Layout Component 설계
- Props Contract 설계
- Props Naming 적용
- Callback Props 설계
- Boolean Props 개선
- Variant 설계
- State Ownership 결정
- Lifting State Up 적용
- Local State / Shared State 구분
- Component Composition 적용
- children / Slot-like Props 사용
- Container / Presentational 분리 판단
- Custom Hook 추출 판단
- API Logic Separation 적용
- Reusable Component 설계
- React TypeScript Props Type 작성
- Component Accessibility 검토
- Component Anti Pattern 탐지

---

### [실무]

Agent 수행 가능 작업:

```text
User Frontend Screen Request
→ Analyze Screen Sections
→ Define Component Responsibility
→ Split Page / Feature / UI Components
→ Decide State Ownership
→ Design Props Contract
→ Compose Components
→ Extract Hook if Needed
→ Review Anti Patterns
→ Maintainable Component Output
```

---

### [FAQ]

Q. React Component Design 문서의 최종 목적은 뭐야?

A.
Frontend Agent가 React 화면을 책임, 경계, Props, State, Composition 기준으로 분해하고 유지보수 가능한 Component 구조를 설계하게 만드는 것이다.

Q. 이 문서 다음에는 어떤 Domain Rules가 이어져야 해?

A.
React Router, State Management, Data Fetching & REST API Integration, Form Handling & Validation 순서로 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. React Component Design 문서는 왜 필요해?
A. Frontend Agent가 React 화면을 단순히 작성하는 것을 넘어 유지보수 가능한 Component 구조로 설계해야 하기 때문이다.

Q. React Component는 언제 분리해?
A. 책임이 많아지거나 JSX가 길어지거나 재사용 가능하거나 특정 UI 영역을 독립적으로 이해할 수 있을 때 분리한다.

Q. Component를 작게 많이 나누면 무조건 좋아?
A. 아니다. 책임 없는 과분리는 Props 전달과 파일 이동만 늘려 복잡도를 높일 수 있다.

Q. Component 책임은 어떻게 정해?
A. UI 영역, 데이터 의존성, State 소유, 이벤트 발생 위치, 재사용 가능성을 기준으로 정한다.

Q. Component Boundary는 뭘 기준으로 잡아?
A. UI 영역, State Owner, 데이터 흐름, 변경 가능성, 재사용 가능성, 테스트 가능성을 기준으로 잡는다.

Q. Page Component는 뭐야?
A. 라우트나 화면 단위를 대표하고 화면 조립, 주요 State, 데이터 흐름을 담당할 수 있는 Component다.

Q. Feature Component는 뭐야?
A. 특정 도메인 기능 단위를 담당하는 Component다. 예를 들어 FestivalSearchForm, ReviewForm 같은 Component다.

Q. UI Component는 뭐야?
A. Button, Input, Modal처럼 도메인과 무관하게 재사용 가능한 표시 중심 Component다.

Q. Page Component와 UI Component 차이는?
A. Page Component는 화면 조립과 흐름을 담당하고 UI Component는 재사용 가능한 표시와 상호작용을 담당한다.

Q. Feature Component와 UI Component 차이는?
A. Feature Component는 도메인 기능에 의존하고 UI Component는 도메인 의존성을 최소화한다.

Q. Layout Component는 언제 만들어?
A. 여러 페이지에서 공통으로 사용하는 Header, Footer, Sidebar, main 영역 구조가 있을 때 만든다.

Q. UI Component에서 API 호출을 해도 돼?
A. 권장하지 않는다. UI Component는 표시와 상호작용만 담당하고 데이터 요청은 Page, Feature, Hook, API 계층에서 처리한다.

Q. Props Contract가 뭐야?
A. 부모 Component와 자식 Component 사이의 데이터 전달 계약이다.

Q. Props 이름은 어떻게 지어?
A. title, value, items처럼 의미가 명확하게 짓고 callback은 onSelect, onSubmit처럼 on prefix를 사용한다.

Q. data라는 Props 이름은 안 좋아?
A. 항상 나쁜 것은 아니지만 의미가 모호하다. festival, user, items처럼 구체적인 이름이 더 좋다.

Q. callback props는 어떻게 설계해?
A. 자식은 이벤트 발생을 알리고 부모가 실제 상태 변경이나 이동 처리를 하도록 설계한다.

Q. 자식 Component가 부모 State를 직접 바꿀 수 있어?
A. 직접 바꿀 수 없다. 부모가 callback props를 전달하고 자식은 그 함수를 호출한다.

Q. Boolean Props가 많으면 왜 문제야?
A. 서로 동시에 true가 될 수 있어 불가능한 상태가 생기고 Component 동작을 예측하기 어려워진다.

Q. Boolean Props 대신 뭘 써?
A. 상호 배타적인 상태라면 `variant: "success" | "error"` 같은 union variant를 사용한다.

Q. State는 어디에 둬야 해?
A. 그 State를 사용하는 Component들의 가장 가까운 공통 부모에 두는 것이 기본이다.

Q. 모든 State를 App에 두면 안 돼?
A. 권장하지 않는다. 불필요한 Props 전달과 Re-render 범위가 커질 수 있다.

Q. Lifting State Up은 언제 해?
A. 여러 Component가 같은 State를 읽거나 변경 결과를 공유해야 할 때 한다.

Q. Local State와 Shared State 차이는?
A. Local State는 한 Component 내부에서만 필요하고 Shared State는 여러 Component가 함께 사용한다.

Q. 전역 상태는 언제 써?
A. 여러 페이지나 깊은 Component 트리에서 반복적으로 필요한 상태일 때 검토한다.

Q. Props Drilling은 무조건 나빠?
A. 아니다. 짧은 전달은 자연스럽다. 깊고 반복되어 유지보수가 어려워질 때 문제가 된다.

Q. Props Drilling은 어떻게 해결해?
A. State 위치 조정, Component Composition, Context, 전역 상태를 순서대로 검토한다.

Q. Component Composition이 뭐야?
A. 작은 Component를 조합해 큰 화면을 만드는 설계 방식이다.

Q. React에서 상속보다 Composition을 쓰는 이유는?
A. Component를 조합하는 방식이 UI 재사용과 변경에 더 유연하기 때문이다.

Q. children은 언제 써?
A. Component 내부 내용을 외부에서 자유롭게 조합해야 할 때 사용한다.

Q. children과 explicit props 차이는?
A. children은 자유로운 내부 조합에 좋고 explicit props는 구조가 고정되고 데이터가 명확할 때 좋다.

Q. Slot-like Props는 언제 써?
A. Card, Modal, Panel처럼 header, action, footer 같은 특정 영역만 외부에서 커스터마이징하고 싶을 때 사용한다.

Q. Container Component는 뭐야?
A. 데이터 로딩, State 관리, 이벤트 흐름을 담당하는 Component다.

Q. Presentational Component는 뭐야?
A. 전달받은 Props를 기반으로 UI를 표시하는 Component다.

Q. Container와 Presentational은 항상 분리해야 해?
A. 아니다. 복잡도를 줄일 때만 사용한다. 단순한 Component에는 과한 설계가 될 수 있다.

Q. Custom Hook은 언제 만들어?
A. 상태 로직이나 Effect 로직이 반복되거나 Component를 복잡하게 만들 때 만든다.

Q. Custom Hook 이름은 왜 use로 시작해야 해?
A. React와 lint 도구가 Hook 규칙을 검사할 수 있게 하기 위해서다.

Q. Custom Hook은 UI를 반환해?
A. 일반적으로 UI가 아니라 상태, 함수, 계산값 같은 로직 결과를 반환한다.

Q. Custom Hook은 Object로 반환하는 게 좋아?
A. 반환 값이 여러 개이고 의미가 중요하면 Object Return이 좋다.

Q. Array Return은 언제 좋아?
A. useState처럼 반환 값의 순서와 의미가 명확하고 짧을 때 적합하다.

Q. Reusable Component는 언제 만들어?
A. 여러 화면에서 같은 UI가 반복되고 도메인 로직 없이 Props로 제어할 수 있을 때 만든다.

Q. 처음부터 공통 Component를 많이 만들면 좋아?
A. 아니다. 실제 반복과 필요가 확인된 후 추출하는 것이 안전하다.

Q. Reusable Component는 도메인 데이터를 알아도 돼?
A. 가능하면 몰라야 한다. 도메인 데이터는 부모가 가공해서 props로 전달하는 것이 좋다.

Q. variant는 왜 써?
A. Component 변형을 제한된 값으로 관리해 오타와 불가능한 상태를 줄이기 위해 사용한다.

Q. API 호출은 Component에서 분리해야 해?
A. 간단한 화면에서는 Component 안에 둘 수 있지만 재사용되거나 길어지면 api 함수나 custom hook으로 분리한다.

Q. API Logic과 UI Logic을 왜 분리해?
A. Component 재사용성과 테스트 가능성을 높이고 서버 구조 변경 영향을 줄이기 위해서다.

Q. Props Type은 어디에 두는 게 좋아?
A. Component 전용이면 같은 파일에 두고 여러 곳에서 공유하면 types 파일로 분리한다.

Q. children 타입은 뭐로 써?
A. TypeScript React에서는 일반적으로 ReactNode를 사용한다.

Q. React.FC를 꼭 써야 해?
A. 필수는 아니다. 프로젝트 컨벤션에 따라 사용 여부를 정한다.

Q. Generic Component는 언제 써?
A. List, Select, Table처럼 데이터 타입은 다르지만 렌더링 구조가 반복될 때 사용한다.

Q. Generic Component를 많이 만들면 좋아?
A. 아니다. 과도한 추상화는 사용성과 가독성을 떨어뜨릴 수 있다.

Q. div에 onClick을 달아서 버튼처럼 써도 돼?
A. 권장하지 않는다. 동작 버튼은 button 태그를 사용해야 키보드 접근성과 기본 동작을 얻을 수 있다.

Q. Icon Button에는 왜 aria-label이 필요해?
A. 아이콘만으로는 스크린 리더가 버튼 목적을 알 수 없기 때문이다.

Q. Component margin은 내부에서 줘도 돼?
A. 상황에 따라 다르지만 재사용 UI Component는 외부 배치 margin을 부모가 관리하는 것이 유연하다.

Q. className prop을 받아야 해?
A. 재사용 Component라면 외부 스타일 확장이 필요할 수 있어 className prop을 고려한다.

Q. Feature 기반 폴더 구조는 언제 좋아?
A. 도메인 기능이 많고 Component, API, Hook, Type이 함께 움직일 때 좋다.

Q. 작은 프로젝트도 features 구조를 써야 해?
A. 필수는 아니다. 작은 프로젝트는 pages, components, api, hooks 정도로 단순하게 시작해도 된다.

Q. Component가 너무 커졌을 때 어디부터 나눠?
A. 먼저 UI 영역을 기준으로 List, Card, Form, Modal 같은 표시 Component를 분리한다.

Q. useEffect가 많은 Component는 어떻게 해?
A. 각 Effect 목적을 검토하고 API, Timer, Event Listener 로직을 custom hook으로 분리할 수 있는지 확인한다.

Q. 과도한 추상화는 왜 문제야?
A. 실제 사용성이 떨어지는 추상화는 props를 복잡하게 만들고 유지보수를 어렵게 만든다.

Q. 중복 코드가 조금 있으면 바로 공통화해야 해?
A. 아니다. 반복 패턴이 명확해지고 변경 방향이 보일 때 공통화하는 것이 안전하다.

Q. Component 설계 문제는 어떻게 찾는 게 좋아?
A. Component 책임, Props 흐름, State 위치, API 로직 위치, 재사용성, 접근성을 순서대로 확인한다.

Q. React Component Design 다음 문서는 뭐가 좋아?
A. React Router, State Management, Data Fetching & REST API Integration, Form Handling & Validation 순서가 좋다.
