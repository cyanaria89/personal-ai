# Advanced React Pattern Domain Rules

---

# 1. Domain Purpose

## 1.1 Advanced React Pattern Domain 목적

### [개념]

Advanced React Pattern Domain 문서는 Frontend Agent / Next.js Agent / Review Agent용 RAG 문서 제작 규칙이다.

Advanced React Pattern은 React 기반 애플리케이션에서 복잡한 UI 상태, 컴포넌트 합성, 성능 최적화, 비동기 처리, 에러 격리, 재사용 가능한 Hook / Component 설계를 다루는 고급 프론트엔드 패턴이다.

목적:

- React 고급 컴포넌트 설계 지원
- Custom Hook 설계 지원
- Composition Pattern 적용 지원
- State Management 판단 지원
- Async UI / Suspense / Transition 처리 지원
- Error Boundary 설계 지원
- Performance Optimization 지원
- Re-render 원인 분석 지원
- React 19 Actions / Optimistic UI 이해 지원
- Next.js App Router와 연계 가능한 React 설계 지원
- Frontend 코드 리뷰 지원

---

### [핵심]

우선순위:

1. Component Composition
2. Custom Hook
3. State Colocation
4. Controlled / Uncontrolled Component
5. Compound Component Pattern
6. Render Props / Children as Function
7. Context Optimization
8. Reducer Pattern
9. Async UI Pattern
10. Suspense / Error Boundary
11. Transition / Optimistic UI
12. Memoization / Re-render Optimization
13. React 19 Actions
14. TypeScript Component Pattern
15. Testing / Review / Troubleshooting

---

### [실무]

2026 실무 기준:

- React Function Component 기준
- TypeScript 기준 예제 우선
- Class Component 중심 설명 금지
- React Hooks 기반 설계 우선
- Composition over Inheritance 원칙 적용
- 상태는 필요한 위치에 최대한 가깝게 배치
- Context는 전역 저장소가 아니라 Dependency / Shared State 전달 도구로 설명
- Memoization은 무조건 적용하지 않고 병목 확인 후 적용
- React 19 기준 Actions, `useActionState`, `useOptimistic`, `useTransition` 문맥 포함
- Next.js App Router의 Server Component / Client Component 경계와 연계 가능하게 작성
- UI 재사용성보다 상태 흐름 명확성 우선
- Agent가 코드 생성과 코드 리뷰에 바로 사용할 수 있는 판단 기준 포함

React 19는 Actions, `useActionState`, `useOptimistic`, form Actions 같은 비동기 UI 패턴을 공식적으로 강화했다.

---

### [FAQ]

Q. Advanced React Pattern 문서는 무엇을 위한 문서인가?

A.
React 고급 컴포넌트 설계, Hook 분리, 상태 관리, 비동기 UI, 성능 최적화, 코드 리뷰를 Agent가 수행하도록 돕는 RAG 문서 제작 규칙이다.

Q. Advanced React Pattern은 React 기초 문서인가?

A.
아니다. JSX, props, state 같은 기초가 아니라 복잡한 UI 구조와 실무 패턴 판단을 위한 고급 문서이다.

Q. Next.js App Router와 연계해야 하나?

A.
연계해야 한다. Client Component 내부의 React Pattern과 Server Component 경계 판단에 직접 연결된다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

Advanced React Pattern Domain은 React 프로젝트에서 구조 복잡도를 줄이고 유지보수 가능한 UI를 만들기 위한 고급 패턴을 포함한다.

---

### [핵심]

포함 범위:

- React Function Component
- Component Composition
- Children Pattern
- Slot Pattern
- Compound Component Pattern
- Render Props
- Custom Hook
- Hook Composition
- Controlled Component
- Uncontrolled Component
- State Colocation
- State Lifting
- Reducer Pattern
- Context Pattern
- Context Performance
- Provider Pattern
- Container / Presentational Pattern
- Headless Component
- Polymorphic Component
- Higher Order Component
- Error Boundary
- Suspense
- Transition
- Optimistic UI
- React Actions
- `useActionState`
- `useOptimistic`
- `useTransition`
- `useDeferredValue`
- `memo`
- `useMemo`
- `useCallback`
- `useRef`
- Lazy Loading
- Code Splitting
- Re-render Optimization
- TypeScript Props Pattern
- Generic Component
- Discriminated Union Props
- Component API Design
- React Testing Pattern
- Accessibility Pattern
- Review Checklist

---

### [실무]

제외 범위:

- React 기초 문법 전체
- JavaScript 기초 문법 전체
- CSS 상세 구현
- Redux / Zustand / Jotai 심화
- Next.js App Router 상세
- React Native 전용 패턴
- Class Component 중심 패턴
- Legacy Lifecycle Method 중심 설명
- jQuery / DOM 직접 조작 중심 UI

단, 고급 패턴 판단에 필요한 React / TypeScript / Next.js 연계 지식은 포함 가능하다.

---

### [FAQ]

Q. Redux나 Zustand도 포함해야 하나?

A.
전역 상태 관리 도구 자체의 심화는 제외한다. 단, local state와 external store를 구분하는 판단 기준은 포함한다.

Q. Class Component 패턴도 다뤄야 하나?

A.
기본적으로 제외한다. Error Boundary처럼 class 기반 구현이 필요한 경우만 제한적으로 언급한다.

Q. Advanced React Pattern 문서에 TypeScript가 필요한가?

A.
필요하다. 실무 React 코드 리뷰와 컴포넌트 API 설계는 TypeScript Props 설계와 강하게 연결된다.

---

# 3. Required Section Rules

## 3.1 문서 Section 구조

### [개념]

모든 Advanced React Pattern RAG 문서는 MASTER_RAG_RULES의 기본 Section 구조를 따른다.

---

### [핵심]

필수 Section:

- `[개념]`
- `[핵심]`
- `[실무]`
- `[FAQ]`

강력 권장 Section:

- `[Flow]`
- `[예제]`
- `[주의]`
- `[Best Practice]`
- `[Troubleshooting]`
- `[Checklist]`
- `[Comparison]`

---

### [실무]

Advanced React Pattern 문서는 판단 기준이 중요하므로 아래 Section을 적극 사용한다.

- `[Flow]`: 이벤트 → 상태 변경 → 렌더링 → 부수효과
- `[Comparison]`: Controlled vs Uncontrolled, Context vs Props
- `[Best Practice]`: State Colocation, Composition
- `[Troubleshooting]`: Infinite Render, Stale Closure, Hydration Error
- `[Checklist]`: Re-render, Hook Dependency, Accessibility 점검

---

### [FAQ]

Q. Advanced React 문서에 Comparison이 필요한 이유는?

A.
React 고급 설계는 정답보다 상황별 선택이 중요하므로 비교 기준이 있어야 Agent가 올바른 패턴을 선택할 수 있다.

Q. `[FAQ]` 대신 `[면접]` 섹션을 써도 되나?

A.
안 된다. MASTER_RAG_RULES에 따라 반드시 `[FAQ]`를 사용한다.

---

# 4. Component Composition Rules

## 4.1 Composition 중심 설계

### [개념]

Component Composition은 컴포넌트를 상속하지 않고 조합해서 UI를 구성하는 React의 핵심 설계 방식이다.

---

### [핵심]

필수 포함:

- Composition over Inheritance
- Children Pattern
- Slot Pattern
- Component API
- Parent / Child Responsibility
- Layout Composition
- UI 재사용성
- Props Drilling 완화
- Explicit Composition
- Flexible Component Structure

예시:

```tsx
type CardProps = {
  header?: React.ReactNode;
  children: React.ReactNode;
  footer?: React.ReactNode;
};

export function Card({ header, children, footer }: CardProps) {
  return (
    <section>
      {header && <header>{header}</header>}
      <main>{children}</main>
      {footer && <footer>{footer}</footer>}
    </section>
  );
}
```

---

### [실무]

Composition 사용 기준:

- UI 구조가 다양하게 조합될 때 사용
- 공통 Layout / Card / Modal / Form Shell에 적합
- Boolean Props가 과도하게 늘어나면 Composition 검토
- Component 내부에서 모든 변형을 처리하지 않기
- `children`, `header`, `footer`, `actions` 같은 Slot Props 사용 가능
- 재사용성과 명시성의 균형 유지

주의:

- 너무 많은 Slot은 API를 복잡하게 만듦
- 암묵적 Magic Composition 지양
- 단순 컴포넌트에 과도한 추상화 금지
- 비즈니스 로직과 UI Layout 책임 분리

---

### [FAQ]

Q. Component Composition은 언제 사용하나?

A.
같은 UI Shell 안에서 header, content, action, footer처럼 다양한 조합이 필요한 경우 사용한다.

Q. Boolean Props가 많으면 왜 문제인가?

A.
컴포넌트 내부 조건 분기가 많아지고 조합 폭발이 발생해 유지보수가 어려워진다.

Q. Composition은 Props Drilling을 없애는 기술인가?

A.
완전히 없애는 기술은 아니지만 상위 컴포넌트가 UI 조합을 명확히 제어하게 만들어 구조 복잡도를 줄일 수 있다.

---

# 5. Children and Slot Pattern Rules

## 5.1 Children / Slot 설계

### [개념]

Children Pattern은 컴포넌트 내부에 외부 UI를 주입하는 방식이고, Slot Pattern은 특정 위치에 들어갈 UI를 명명된 props로 전달하는 방식이다.

---

### [핵심]

필수 포함:

- `children`
- Named Slot
- `React.ReactNode`
- Layout Component
- Flexible UI
- Header Slot
- Footer Slot
- Action Slot
- Empty State Slot
- Component Contract

예시:

```tsx
type PageLayoutProps = {
  title: string;
  children: React.ReactNode;
  actions?: React.ReactNode;
};

export function PageLayout({ title, actions, children }: PageLayoutProps) {
  return (
    <div>
      <header>
        <h1>{title}</h1>
        {actions}
      </header>
      {children}
    </div>
  );
}
```

---

### [실무]

사용 기준:

- `children`: 주요 콘텐츠 삽입
- `actions`: 버튼 영역 삽입
- `header`: 커스텀 헤더 삽입
- `footer`: 하단 액션 삽입
- `empty`: 빈 상태 UI 삽입
- `fallback`: 대체 UI 삽입

Best Practice:

- Slot 이름은 역할 중심으로 작성
- Slot Props는 `React.ReactNode` 사용
- Slot이 필수인지 선택인지 명확히 표시
- Slot 내부 상태는 가능한 외부에서 관리
- 과도한 Slot보다 Compound Component가 나은지 검토

---

### [FAQ]

Q. `children`과 Slot Props 차이는?

A.
`children`은 기본 콘텐츠 영역이고 Slot Props는 header, actions, footer처럼 특정 위치에 들어갈 UI를 명명해서 전달하는 방식이다.

Q. Slot Props 타입은 무엇을 쓰나?

A.
보통 `React.ReactNode`를 사용한다.

Q. Slot Pattern이 적합한 컴포넌트는?

A.
Card, Modal, PageLayout, Toolbar, FormLayout처럼 UI 영역이 나뉘는 컴포넌트에 적합하다.

---

# 6. Compound Component Rules

## 6.1 Compound Component Pattern

### [개념]

Compound Component Pattern은 여러 하위 컴포넌트가 하나의 부모 컴포넌트와 함께 동작하면서 공유 상태나 문맥을 사용하는 패턴이다.

---

### [핵심]

필수 포함:

- Parent Component
- Child Component
- Shared State
- Context
- Implicit State Sharing
- Explicit API
- Tabs
- Accordion
- Select
- Menu
- Modal
- Component Namespace

예시:

```tsx
type TabsContextValue = {
  value: string;
  setValue: (value: string) => void;
};

const TabsContext = React.createContext<TabsContextValue | null>(null);

function useTabsContext() {
  const context = React.useContext(TabsContext);

  if (!context) {
    throw new Error("Tabs components must be used inside Tabs");
  }

  return context;
}
```

---

### [실무]

적합한 UI:

- Tabs
- Accordion
- Dropdown
- Menu
- Select
- Dialog
- Stepper
- Toggle Group

작성 기준:

- 부모 컴포넌트가 상태 제공
- 하위 컴포넌트는 Context로 상태 접근
- 사용 순서와 계층 제약 명확히 문서화
- 잘못된 사용 시 명확한 에러 메시지 제공
- 복잡한 상태는 Reducer와 결합 가능
- 접근성 속성까지 함께 설계

주의:

- Context Re-render 범위 주의
- 하위 컴포넌트가 부모 없이 사용될 때 에러 처리
- 과도한 Compound 구조는 추적 어려움
- 단순 UI에는 Slot Pattern이 더 적합할 수 있음

---

### [FAQ]

Q. Compound Component는 언제 사용하나?

A.
Tabs, Accordion, Select처럼 여러 하위 컴포넌트가 하나의 상태를 공유하며 함께 동작할 때 사용한다.

Q. Compound Component는 Context가 필수인가?

A.
대부분 Context를 사용하지만, 단순한 경우 props 전달이나 children mapping으로도 구현할 수 있다.

Q. Compound Component의 단점은?

A.
구조가 암묵적으로 동작할 수 있고 Context Re-render나 계층 제약 때문에 디버깅이 어려워질 수 있다.

---

# 7. Render Props Rules

## 7.1 Render Props Pattern

### [개념]

Render Props Pattern은 컴포넌트가 UI를 직접 결정하지 않고, 렌더링 함수를 props로 받아 상태나 동작을 외부에 제공하는 패턴이다.

---

### [핵심]

필수 포함:

- Function as Child
- Render Function
- State Sharing
- Behavior Reuse
- Headless Logic
- Flexible Rendering
- Legacy Pattern
- Custom Hook 대체 가능성

예시:

```tsx
type ToggleProps = {
  children: (state: { open: boolean; toggle: () => void }) => React.ReactNode;
};

export function Toggle({ children }: ToggleProps) {
  const [open, setOpen] = React.useState(false);

  return children({
    open,
    toggle: () => setOpen((value) => !value),
  });
}
```

---

### [실무]

사용 기준:

- UI는 외부에서 결정하고 동작만 재사용할 때 사용
- Headless Component 설계에 사용 가능
- 기존 라이브러리 패턴 이해에 필요
- 새 코드에서는 Custom Hook이 더 단순한지 먼저 검토
- TypeScript 타입이 복잡해질 수 있음

주의:

- 중첩 Render Props는 가독성 저하
- 불필요한 함수 재생성으로 렌더링 비용 증가 가능
- 단순 상태 공유에는 Custom Hook 우선 고려

---

### [FAQ]

Q. Render Props는 아직 사용하나?

A.
사용 가능하지만 새 코드에서는 Custom Hook이나 Compound Component가 더 단순한 경우가 많다.

Q. Render Props의 장점은?

A.
동작 로직과 렌더링 UI를 분리해 유연하게 재사용할 수 있다.

Q. Render Props의 단점은?

A.
중첩 구조가 복잡해지고 TypeScript 타입이 길어질 수 있다.

---

# 8. Custom Hook Rules

## 8.1 Custom Hook 설계

### [개념]

Custom Hook은 React Hook을 조합해 상태 로직과 부수효과를 재사용 가능한 함수로 분리하는 패턴이다.

---

### [핵심]

필수 포함:

- `use` Prefix
- Hook Composition
- State Logic Reuse
- Effect Encapsulation
- Return Value Design
- Stable API
- Dependency Management
- Testability
- Single Responsibility
- Error Handling

예시:

```tsx
type UseDisclosureResult = {
  open: boolean;
  onOpen: () => void;
  onClose: () => void;
  onToggle: () => void;
};

export function useDisclosure(initialOpen = false): UseDisclosureResult {
  const [open, setOpen] = React.useState(initialOpen);

  return {
    open,
    onOpen: () => setOpen(true),
    onClose: () => setOpen(false),
    onToggle: () => setOpen((value) => !value),
  };
}
```

---

### [실무]

Custom Hook 작성 기준:

- 이름은 반드시 `use`로 시작
- 하나의 Hook은 하나의 책임
- 반환값은 object 또는 tuple 기준 명확화
- 재사용 가능한 상태 로직만 분리
- UI JSX 반환은 신중히 사용
- 외부 API 호출 Hook은 loading / error / data 상태 포함
- Effect Dependency를 명확히 관리
- 테스트 가능한 순수 로직은 Hook 밖으로 분리
- 서버 상태는 TanStack Query 같은 도구와 역할 구분

반환값 기준:

| 반환 형태 | 적합 상황                           |
| --------- | ----------------------------------- |
| Object    | 값이 많거나 이름이 중요한 경우      |
| Tuple     | `useState`처럼 순서가 관례화된 경우 |

---

### [FAQ]

Q. Custom Hook은 언제 만들면 되나?

A.
여러 컴포넌트에서 동일한 상태 로직, 이벤트 처리, Effect 로직이 반복될 때 만든다.

Q. Custom Hook이 JSX를 반환해도 되나?

A.
가능은 하지만 일반적으로 Hook은 상태와 동작을 반환하고 UI는 컴포넌트에서 렌더링하는 것이 좋다.

Q. Custom Hook 반환값은 object가 좋나 tuple이 좋나?

A.
반환값이 많거나 의미가 중요하면 object, 짧고 관례적인 값이면 tuple이 적합하다.

---

# 9. State Colocation Rules

## 9.1 상태 위치 결정

### [개념]

State Colocation은 상태를 사용하는 컴포넌트와 가장 가까운 위치에 상태를 두는 설계 원칙이다.

---

### [핵심]

필수 포함:

- Local State
- Lift State Up
- Shared State
- Derived State
- Server State
- URL State
- Form State
- Global State
- State Ownership
- State Scope

판단 Flow:

```text
상태를 한 컴포넌트만 사용하는가?
→ Local State

형제 컴포넌트가 공유하는가?
→ 공통 부모로 Lift State Up

페이지 URL과 동기화되어야 하는가?
→ URL Search Params

서버 데이터인가?
→ Server State 관리 도구 또는 Server Component

앱 전체에서 자주 필요한가?
→ Context 또는 External Store 검토
```

---

### [실무]

상태 분류:

| 상태 유형       | 예시          | 권장 위치                      |
| --------------- | ------------- | ------------------------------ |
| Local UI State  | Modal open    | 해당 컴포넌트                  |
| Form State      | input value   | Form 컴포넌트                  |
| Shared UI State | selected tab  | 공통 부모                      |
| Server State    | user list     | Query / Server Component       |
| URL State       | search, page  | URL Query                      |
| Auth State      | current user  | Server Session / Auth Provider |
| Global UI State | theme         | Context                        |
| Derived State   | filtered list | 계산값                         |

주의:

- 모든 상태를 전역으로 올리지 않기
- Derived State를 중복 저장하지 않기
- Props로 계산 가능한 값은 state로 만들지 않기
- 상태 소유자를 명확히 정하기

---

### [FAQ]

Q. 상태는 어디에 두는 게 좋은가?

A.
그 상태를 실제로 사용하는 컴포넌트와 가장 가까운 곳에 둔다.

Q. 상태를 무조건 전역 관리하면 안 되나?

A.
권장하지 않는다. 전역 상태가 많아지면 변경 범위와 디버깅 복잡도가 커진다.

Q. Derived State는 왜 조심해야 하나?

A.
원본 상태와 파생 상태가 불일치할 수 있어 버그가 생기기 쉽다.

---

# 10. Controlled and Uncontrolled Component Rules

## 10.1 입력 상태 제어 패턴

### [개념]

Controlled Component는 값이 React state로 제어되는 컴포넌트이고, Uncontrolled Component는 DOM 자체가 값을 관리하는 컴포넌트이다.

---

### [핵심]

필수 포함:

- Controlled Component
- Uncontrolled Component
- Form Input
- `value`
- `defaultValue`
- `onChange`
- `ref`
- Form Library
- Validation
- Reset
- Performance

예시:

```tsx
type SearchInputProps = {
  value: string;
  onChange: (value: string) => void;
};

export function SearchInput({ value, onChange }: SearchInputProps) {
  return (
    <input value={value} onChange={(event) => onChange(event.target.value)} />
  );
}
```

---

### [실무]

비교:

| 기준    | Controlled              | Uncontrolled         |
| ------- | ----------------------- | -------------------- |
| 값 관리 | React State             | DOM                  |
| 검증    | 즉시 가능               | Submit 시 적합       |
| 동기화  | 쉬움                    | 제한적               |
| 성능    | 입력마다 렌더링         | 상대적으로 가벼움    |
| 사용 예 | 검색, 필터, 실시간 검증 | 단순 Form, 파일 입력 |

선택 기준:

- 실시간 검증 / 조건부 UI 필요 → Controlled
- 단순 제출 중심 Form → Uncontrolled 가능
- 파일 입력 → Uncontrolled 사용
- 대규모 Form → Form Library 또는 Uncontrolled 기반 검토
- 외부에서 값을 제어해야 함 → Controlled

---

### [FAQ]

Q. Controlled Component는 언제 사용하나?

A.
입력값을 React state와 동기화해야 하거나 실시간 검증, 조건부 UI가 필요할 때 사용한다.

Q. Uncontrolled Component는 나쁜 패턴인가?

A.
아니다. 단순 Form 제출이나 파일 입력처럼 DOM이 값을 관리하는 편이 자연스러운 경우 적합하다.

Q. `value`와 `defaultValue` 차이는?

A.
`value`는 React state가 계속 제어하고, `defaultValue`는 초기값만 지정한다.

---

# 11. Reducer Pattern Rules

## 11.1 `useReducer` 상태 전이 패턴

### [개념]

Reducer Pattern은 복잡한 상태 변경을 action과 reducer 함수로 분리해 예측 가능한 상태 전이를 만드는 패턴이다.

---

### [핵심]

필수 포함:

- `useReducer`
- State Machine
- Action
- Reducer
- Dispatch
- Immutable Update
- Complex State
- Form State
- UI State
- Exhaustive Check

예시:

```tsx
type State = {
  count: number;
};

type Action = { type: "increment" } | { type: "decrement" } | { type: "reset" };

function counterReducer(state: State, action: Action): State {
  switch (action.type) {
    case "increment":
      return { count: state.count + 1 };
    case "decrement":
      return { count: state.count - 1 };
    case "reset":
      return { count: 0 };
  }
}
```

---

### [실무]

사용 기준:

- 상태 필드가 여러 개
- 상태 변경 규칙이 복잡함
- 이전 상태 기반 전이가 많음
- action 단위로 의미를 표현하고 싶음
- Form Wizard / Modal Flow / Complex Filter에 적합
- Context와 결합해 상태 관리 가능

주의:

- 단순 boolean state에 과도하게 사용하지 않기
- reducer 내부에서 side effect 실행 금지
- action 이름은 사용자 의도 중심으로 작성
- TypeScript union으로 action을 명확히 표현

---

### [FAQ]

Q. `useState`와 `useReducer` 중 무엇을 써야 하나?

A.
단순 상태는 `useState`, 상태 전이가 복잡하거나 action 의미가 중요한 경우 `useReducer`를 사용한다.

Q. reducer 안에서 API 호출해도 되나?

A.
안 된다. reducer는 순수 함수여야 하며 side effect는 외부에서 처리해야 한다.

Q. Reducer Pattern은 전역 상태 관리인가?

A.
아니다. local state에도 사용할 수 있고 Context와 결합하면 공유 상태로 확장할 수 있다.

---

# 12. Context Pattern Rules

## 12.1 Context 사용 기준

### [개념]

Context는 props를 여러 단계로 전달하지 않고 하위 컴포넌트에 값을 제공하는 React 기능이다.

---

### [핵심]

필수 포함:

- React Context
- Provider
- Consumer
- `useContext`
- Shared Dependency
- Theme
- Auth
- Locale
- Context Splitting
- Re-render
- Provider Scope
- Context Value Memoization

예시:

```tsx
type ThemeContextValue = {
  theme: "light" | "dark";
  setTheme: (theme: "light" | "dark") => void;
};

const ThemeContext = React.createContext<ThemeContextValue | null>(null);

export function useTheme() {
  const context = React.useContext(ThemeContext);

  if (!context) {
    throw new Error("useTheme must be used inside ThemeProvider");
  }

  return context;
}
```

---

### [실무]

Context 적합 상황:

- Theme
- Locale
- Auth User Summary
- Feature Flag
- Design System Config
- Compound Component 내부 상태
- Dependency Injection

Context 부적합 상황:

- 자주 바뀌는 대규모 리스트
- 입력 중인 모든 Form Field
- 서버 캐시 데이터 전체
- 고빈도 업데이트 상태
- 무분별한 전역 Store 대체

Best Practice:

- Provider 범위를 좁게 유지
- 자주 바뀌는 값과 거의 안 바뀌는 값 분리
- State Context와 Action Context 분리 검토
- Context Value는 필요 시 memoization
- Context 기본값으로 조용히 실패하지 않기
- Custom Hook으로 사용 강제

---

### [FAQ]

Q. Context는 전역 상태 관리 도구인가?

A.
전역 상태 관리처럼 사용할 수 있지만 본질은 하위 컴포넌트에 값을 전달하는 도구이다.

Q. Context를 많이 쓰면 왜 느려질 수 있나?

A.
Provider value가 바뀌면 해당 Context를 사용하는 컴포넌트들이 다시 렌더링될 수 있기 때문이다.

Q. Context에는 무엇을 넣는 게 좋은가?

A.
Theme, Locale, Auth Summary, Feature Flag, Compound Component 상태처럼 넓게 공유되지만 변경 빈도가 낮은 값이 적합하다.

---

# 13. Container and Presentational Pattern Rules

## 13.1 로직 / UI 분리 패턴

### [개념]

Container / Presentational Pattern은 데이터 조회와 상태 관리 로직을 Container에 두고, UI 표현을 Presentational Component에 분리하는 패턴이다.

---

### [핵심]

필수 포함:

- Container Component
- Presentational Component
- Smart Component
- Dumb Component
- Props Contract
- UI Reuse
- Testing
- Data Fetching Boundary
- Business Logic Separation

예시:

```tsx
type UserListViewProps = {
  users: Array<{ id: string; name: string }>;
  onSelect: (id: string) => void;
};

export function UserListView({ users, onSelect }: UserListViewProps) {
  return (
    <ul>
      {users.map((user) => (
        <li key={user.id}>
          <button onClick={() => onSelect(user.id)}>{user.name}</button>
        </li>
      ))}
    </ul>
  );
}
```

---

### [실무]

사용 기준:

- 데이터 조회와 UI 렌더링이 섞여 복잡할 때 사용
- 같은 UI를 다른 데이터 소스와 재사용할 때 적합
- 테스트에서 UI 컴포넌트를 쉽게 검증 가능
- Next.js App Router에서는 Server Component가 Container 역할을 할 수 있음
- Client Component 내부에서도 Hook Container와 View Component 분리 가능

주의:

- 모든 컴포넌트를 기계적으로 둘로 나누지 않기
- 너무 작은 컴포넌트에는 불필요
- Props가 과도하게 많아지면 Component API 재검토

---

### [FAQ]

Q. Container / Presentational Pattern은 아직 유효한가?

A.
유효하다. 다만 Hooks와 Server Component 등장 이후 더 유연하게 적용한다.

Q. Next.js App Router에서는 어떻게 적용하나?

A.
Server Component가 데이터를 조회하고 Presentational Client Component에 안전한 props를 전달하는 식으로 적용할 수 있다.

---

# 14. Headless Component Rules

## 14.1 Headless UI 설계

### [개념]

Headless Component는 스타일과 마크업을 강하게 고정하지 않고 상태와 동작, 접근성 로직을 제공하는 컴포넌트 패턴이다.

---

### [핵심]

필수 포함:

- Headless Component
- Logic without Style
- Accessibility Behavior
- Render Props
- Custom Hook
- Compound Component
- Component API
- Reusable Behavior
- Design System Integration

예시:

```tsx
export function useToggle(initialValue = false) {
  const [selected, setSelected] = React.useState(initialValue);

  return {
    selected,
    toggle: () => setSelected((value) => !value),
    setSelected,
  };
}
```

---

### [실무]

적합한 경우:

- Design System과 결합
- 여러 스타일 변형 필요
- 접근성 로직 재사용 필요
- Dropdown / Dialog / Tabs / Combobox
- UI Library 내부 구현

작성 기준:

- 상태와 동작을 Hook 또는 Context로 제공
- 스타일은 외부에서 결정
- ARIA 속성 / Keyboard Interaction 포함
- 제어 가능 Controlled API 제공 검토
- 기본 사용 예제 제공

주의:

- 사용자가 직접 연결해야 하는 API가 많아질 수 있음
- 접근성 책임을 누락하면 위험
- 단순 앱 컴포넌트에는 과도할 수 있음

---

### [FAQ]

Q. Headless Component는 무엇인가?

A.
스타일을 고정하지 않고 상태, 동작, 접근성 로직만 제공해 다양한 UI로 조합할 수 있게 하는 패턴이다.

Q. Headless Component는 언제 필요한가?

A.
같은 동작을 여러 디자인으로 재사용하거나 Design System과 결합할 때 필요하다.

---

# 15. Polymorphic Component Rules

## 15.1 Polymorphic Component 설계

### [개념]

Polymorphic Component는 `as` prop을 사용해 렌더링할 HTML 태그나 컴포넌트를 바꿀 수 있는 패턴이다.

---

### [핵심]

필수 포함:

- `as` Prop
- Element Type
- Generic Props
- Ref Forwarding
- Accessibility
- Button vs Link
- Design System
- Type Safety
- Prop Collision

예시:

```tsx
type TextProps<T extends React.ElementType> = {
  as?: T;
  children: React.ReactNode;
} & React.ComponentPropsWithoutRef<T>;

export function Text<T extends React.ElementType = "p">({
  as,
  children,
  ...props
}: TextProps<T>) {
  const Component = as ?? "p";

  return <Component {...props}>{children}</Component>;
}
```

---

### [실무]

사용 기준:

- Design System의 Text, Box, Button 컴포넌트
- 스타일은 같지만 HTML Semantic이 달라야 할 때
- Link와 Button 역할 구분이 필요한 UI
- 접근성을 유지하면서 렌더링 태그를 바꿀 때

주의:

- TypeScript 타입이 복잡해짐
- `as`로 의미 없는 태그를 선택하면 접근성 문제 발생
- Button과 Link 역할 혼동 금지
- Ref 타입 처리 주의
- 단순 컴포넌트에는 과도한 추상화

React 19에서는 여러 경우에 `ref`를 일반 prop처럼 전달할 수 있도록 개선되었지만, 라이브러리 호환성과 타입 설계는 프로젝트 기준에 맞춰 검토해야 한다.

---

### [FAQ]

Q. Polymorphic Component는 언제 사용하나?

A.
Design System에서 같은 스타일을 유지하면서 `button`, `a`, `span`, `div` 등 렌더링 요소를 바꿔야 할 때 사용한다.

Q. Polymorphic Component의 위험은?

A.
타입 복잡도, 접근성 문제, Button과 Link 역할 혼동이 발생할 수 있다.

---

# 16. Higher Order Component Rules

## 16.1 HOC 사용 기준

### [개념]

Higher Order Component는 컴포넌트를 입력받아 추가 기능이 적용된 새 컴포넌트를 반환하는 패턴이다.

---

### [핵심]

필수 포함:

- Higher Order Component
- Component Wrapping
- Cross-cutting Concern
- Auth Guard
- Logging
- Feature Flag
- Legacy Pattern
- Hook 대체 가능성
- Prop Forwarding
- Display Name

예시:

```tsx
function withFeatureFlag<P>(
  Component: React.ComponentType<P>,
  enabled: boolean,
) {
  return function FeatureFlaggedComponent(props: P) {
    if (!enabled) {
      return null;
    }

    return <Component {...props} />;
  };
}
```

---

### [실무]

사용 기준:

- 기존 코드베이스에 HOC 패턴이 많을 때 이해 필요
- 공통 기능을 컴포넌트에 주입할 때 사용 가능
- 새 코드에서는 Custom Hook이나 Composition이 더 단순한지 검토
- Auth Guard는 Router / Server Layer에서 처리 가능한지 먼저 검토
- prop 충돌과 ref 전달 문제 주의

주의:

- Wrapper Hell 발생 가능
- 디버깅 어려움
- TypeScript 타입 복잡도 증가
- 컴포넌트 이름 추적 어려움

---

### [FAQ]

Q. HOC는 아직 사용하나?

A.
기존 라이브러리와 레거시 코드에서 여전히 볼 수 있다. 새 코드에서는 Custom Hook이나 Composition을 우선 검토한다.

Q. HOC의 단점은?

A.
Wrapper 중첩, props 충돌, ref 전달 문제, 디버깅 어려움이 있다.

---

# 17. Async UI Pattern Rules

## 17.1 비동기 UI 상태 설계

### [개념]

Async UI Pattern은 비동기 작업의 loading, success, error, empty, pending 상태를 명확히 분리해 사용자 경험과 코드 안정성을 높이는 패턴이다.

---

### [핵심]

필수 포함:

- Loading State
- Pending State
- Success State
- Error State
- Empty State
- Retry
- Cancellation
- Race Condition
- Optimistic UI
- Transition
- Suspense
- Error Boundary

Flow:

```text
User Action
→ Pending State
→ Async Request
→ Success / Error
→ Revalidation or Rollback
```

---

### [실무]

상태 설계 기준:

- Loading: 초기 데이터 요청
- Pending: 사용자 액션 처리 중
- Error: 실패 상태
- Empty: 성공했지만 데이터 없음
- Optimistic: 성공을 가정한 즉시 UI
- Retry: 재시도 가능 오류
- Disabled: 중복 제출 방지

주의:

- Loading과 Empty State 혼동 금지
- Error를 console만 찍고 숨기지 않기
- 중복 요청 / Race Condition 처리
- 컴포넌트 unmount 후 state update 주의
- 비동기 작업 실패 시 rollback 고려

---

### [FAQ]

Q. Loading State와 Pending State 차이는?

A.
Loading은 초기 데이터 로딩에 가깝고 Pending은 사용자 액션 처리 중 상태에 가깝다.

Q. Empty State는 Error인가?

A.
아니다. 요청은 성공했지만 표시할 데이터가 없는 상태이다.

Q. Retry는 언제 제공하나?

A.
네트워크 오류나 일시적 서버 오류처럼 사용자가 다시 시도할 수 있는 경우 제공한다.

---

# 18. Suspense and Error Boundary Rules

## 18.1 Suspense / Error Boundary 설계

### [개념]

Suspense는 비동기 렌더링 대기 상태를 fallback UI로 처리하고, Error Boundary는 하위 컴포넌트 렌더링 중 발생한 오류를 격리하는 패턴이다. `use`로 Promise를 읽는 컴포넌트가 Suspense로 감싸져 있으면 Promise pending 동안 fallback이 표시되고, Promise reject 시 가장 가까운 Error Boundary fallback이 표시된다.

---

### [핵심]

필수 포함:

- Suspense Boundary
- Fallback UI
- Error Boundary
- Error Isolation
- Retry
- Streaming
- Async Rendering
- Segment-level Boundary
- Component-level Boundary
- Graceful Degradation

예시:

```tsx
function UserPanel() {
  return (
    <ErrorBoundary fallback={<p>Failed to load user.</p>}>
      <React.Suspense fallback={<p>Loading user...</p>}>
        <UserProfile />
      </React.Suspense>
    </ErrorBoundary>
  );
}
```

---

### [실무]

사용 기준:

- 느린 UI 영역을 독립적으로 로딩 처리
- 중요 영역과 덜 중요한 영역 분리
- Error Boundary를 너무 상위에만 두지 않기
- 재시도 가능한 UI 제공
- Next.js App Router에서는 `loading.tsx`, `error.tsx`와 연계
- 데이터 패칭 라이브러리의 Suspense 지원 여부 확인
- fallback UI는 실제 Layout Shift를 줄이도록 설계

Error Boundary는 하위 트리의 렌더링, lifecycle, constructor 중 발생한 JavaScript 에러를 잡고 fallback UI를 표시한다.

---

### [FAQ]

Q. Suspense는 언제 사용하나?

A.
비동기 데이터나 lazy component가 준비될 때까지 fallback UI를 보여주고 싶을 때 사용한다.

Q. Error Boundary는 모든 에러를 잡나?

A.
렌더링 중 발생한 하위 컴포넌트 오류를 잡지만 이벤트 핸들러나 비동기 callback의 모든 오류를 자동으로 잡지는 않는다.

Q. Suspense와 Error Boundary를 같이 써야 하나?

A.
비동기 UI에서는 로딩과 실패를 모두 다뤄야 하므로 함께 설계하는 것이 좋다.

---

# 19. Transition and Deferred Value Rules

## 19.1 Non-blocking UI Update

### [개념]

`useTransition`은 긴 렌더링이나 비긴급 상태 업데이트를 non-blocking update로 처리해 UI 응답성을 유지하는 Hook이다. React 공식 문서에서 `useTransition`은 Actions를 만들고 pending state에 접근하는 Hook으로 설명된다.

---

### [핵심]

필수 포함:

- `useTransition`
- `startTransition`
- `isPending`
- Non-blocking Update
- Urgent Update
- Non-urgent Update
- `useDeferredValue`
- Search UI
- Filter UI
- Slow List Rendering
- Pending Indicator

예시:

```tsx
export function SearchBox() {
  const [keyword, setKeyword] = React.useState("");
  const [query, setQuery] = React.useState("");
  const [isPending, startTransition] = React.useTransition();

  function handleChange(value: string) {
    setKeyword(value);

    startTransition(() => {
      setQuery(value);
    });
  }

  return (
    <>
      <input
        value={keyword}
        onChange={(event) => handleChange(event.target.value)}
      />
      {isPending && <span>Updating...</span>}
      <SearchResult query={query} />
    </>
  );
}
```

---

### [실무]

사용 기준:

- 입력값은 즉시 반영하고 무거운 결과 렌더링은 늦춰야 할 때
- 검색 / 필터 / 탭 전환 / 큰 목록 렌더링
- 사용자 입력이 버벅이는 문제 개선
- `isPending`으로 진행 상태 표시
- 서버 요청 속도 개선이 아니라 렌더링 우선순위 조정임을 명확히 설명

주의:

- 모든 상태 업데이트를 Transition으로 감싸지 않기
- 입력 자체는 urgent update로 유지
- 비동기 요청 취소 / Race Condition은 별도 처리
- 성능 병목 확인 후 적용

---

### [FAQ]

Q. `useTransition`은 언제 사용하나?

A.
사용자 입력은 즉시 반영하면서 무거운 렌더링 업데이트를 뒤로 미루고 싶을 때 사용한다.

Q. `useTransition`이 API 요청을 빠르게 만드나?

A.
아니다. 렌더링 우선순위를 조정해 UI 응답성을 높이는 도구이다.

Q. `useDeferredValue`와 차이는?

A.
`useTransition`은 업데이트를 감싸고, `useDeferredValue`는 특정 값의 반영을 지연시킨다.

---

# 20. Optimistic UI Rules

## 20.1 Optimistic Update Pattern

### [개념]

Optimistic UI는 서버 응답을 기다리지 않고 성공을 가정해 UI를 먼저 업데이트한 뒤 실패 시 rollback하는 패턴이다. React 19는 `useOptimistic` Hook으로 Optimistic UI 구현을 지원한다.

---

### [핵심]

필수 포함:

- Optimistic UI
- `useOptimistic`
- Pending Mutation
- Rollback
- Server Confirmation
- Error Recovery
- Like Button
- Comment Submit
- Todo Add
- Temporary ID
- Revalidation

예시:

```tsx
type Comment = {
  id: string;
  text: string;
};

export function CommentList({ comments }: { comments: Comment[] }) {
  const [optimisticComments, addOptimisticComment] = React.useOptimistic(
    comments,
    (currentComments, text: string) => [
      ...currentComments,
      { id: crypto.randomUUID(), text },
    ],
  );

  return (
    <ul>
      {optimisticComments.map((comment) => (
        <li key={comment.id}>{comment.text}</li>
      ))}
    </ul>
  );
}
```

---

### [실무]

적합한 작업:

- Like / Unlike
- Bookmark
- Comment Add
- Todo Add
- Reaction
- Follow / Unfollow
- Cart Add

주의:

- 실패 가능성이 큰 작업에는 신중히 적용
- 결제 / 권한 변경 / 삭제 같은 민감 작업은 즉시 확정 UI 지양
- 실패 시 사용자에게 복구 메시지 제공
- 임시 ID와 서버 ID 매핑 고려
- 중복 제출 방지
- Mutation 후 서버 데이터와 재동기화

---

### [FAQ]

Q. Optimistic UI는 언제 사용하나?

A.
성공 가능성이 높고 사용자가 즉시 피드백을 기대하는 Like, Comment, Bookmark 같은 작업에 사용한다.

Q. Optimistic UI는 위험하지 않나?

A.
실패 시 rollback과 에러 메시지가 없으면 위험하다. 민감한 작업에는 신중히 적용해야 한다.

Q. `useOptimistic`은 무엇을 돕나?

A.
서버 응답 전 임시 UI 상태를 관리하고 사용자에게 빠른 피드백을 제공하는 데 도움을 준다.

---

# 21. React Actions and Form State Rules

## 21.1 Actions / `useActionState`

### [개념]

React Actions는 비동기 mutation을 선언적으로 처리하기 위한 패턴이다. `useActionState`는 Action 실행 결과 state와 pending 상태를 함께 관리하는 Hook이다.

---

### [핵심]

필수 포함:

- React Actions
- Form Action
- `useActionState`
- Pending State
- Action Result
- Validation Error
- Progressive Enhancement
- Submit Button State
- Server Action 연계
- Optimistic UI 연계

예시:

```tsx
type FormState = {
  message: string;
};

async function submitAction(
  previousState: FormState,
  formData: FormData,
): Promise<FormState> {
  const title = String(formData.get("title") ?? "");

  if (!title) {
    return { message: "Title is required" };
  }

  return { message: "Saved" };
}
```

---

### [실무]

사용 기준:

- Form submit 결과를 상태로 관리
- pending 상태를 UI에 표시
- 서버 검증 메시지를 화면에 표시
- Next.js Server Action과 연계 가능
- Client Form UX 개선
- 기존 `isLoading`, `error`, `data` 상태 분산을 줄일 수 있음

주의:

- Client Validation만 믿지 않기
- 서버 Action 내부 권한 검증 필수
- Action 결과 타입 명확히 정의
- 민감한 에러 상세 노출 금지
- FormData 값은 항상 검증

---

### [FAQ]

Q. `useActionState`는 언제 사용하나?

A.
Form Action의 결과 상태와 pending 상태를 함께 관리해야 할 때 사용한다.

Q. React Actions는 Next.js Server Actions와 같은가?

A.
개념적으로 연결되지만 동일한 것은 아니다. React Actions는 React의 비동기 mutation 패턴이고, Next.js Server Actions는 서버 실행 mutation 기능이다.

---

# 22. Memoization Rules

## 22.1 `memo` / `useMemo` / `useCallback`

### [개념]

Memoization은 동일한 입력에 대해 계산값이나 함수 참조를 재사용해 불필요한 렌더링이나 계산을 줄이는 최적화 패턴이다.

---

### [핵심]

필수 포함:

- `React.memo`
- `useMemo`
- `useCallback`
- Referential Equality
- Expensive Calculation
- Stable Props
- Re-render Optimization
- Dependency Array
- Premature Optimization
- React Compiler 고려

예시:

```tsx
const filteredItems = React.useMemo(() => {
  return items.filter((item) => item.name.includes(keyword));
}, [items, keyword]);
```

예시:

```tsx
const handleSelect = React.useCallback((id: string) => {
  setSelectedId(id);
}, []);
```

---

### [실무]

사용 기준:

- 실제 성능 문제가 확인된 경우
- 계산 비용이 큰 derived value
- memoized child에 안정적인 props 전달 필요
- Context value 안정화 필요
- 큰 리스트 item 렌더링 최적화
- Hook Dependency 안정화 필요

주의:

- 무조건 `useMemo`, `useCallback` 적용 금지
- Dependency 누락 금지
- 잘못된 memoization은 stale value 버그 발생
- 작은 계산에는 오히려 복잡도 증가
- React Compiler 도입 여부에 따라 manual memoization 전략 재검토

React Compiler는 자동 memoization을 목표로 하지만, 수동 최적화 API의 의미와 적용 기준은 여전히 코드 리뷰에서 중요하다.

---

### [FAQ]

Q. `useMemo`는 항상 써야 하나?

A.
아니다. 계산 비용이 크거나 참조 안정성이 필요한 경우에만 사용한다.

Q. `useCallback`은 왜 사용하나?

A.
함수 참조를 안정화해 memoized child의 불필요한 렌더링을 줄이거나 Hook Dependency를 명확히 하기 위해 사용한다.

Q. Memoization이 버그를 만들 수 있나?

A.
그렇다. Dependency가 누락되면 stale value나 stale closure 문제가 생길 수 있다.

---

# 23. Re-render Optimization Rules

## 23.1 렌더링 최적화 판단

### [개념]

Re-render Optimization은 컴포넌트가 언제, 왜 다시 렌더링되는지 분석하고 필요한 범위만 최적화하는 작업이다.

---

### [핵심]

필수 포함:

- Re-render Cause
- Parent Re-render
- State Update
- Props Change
- Context Value Change
- Key Change
- Memoization
- Component Split
- State Colocation
- Profiler
- Bundle Size
- Virtualization

Flow:

```text
Re-render 발생
→ 원인 확인
→ State 위치 확인
→ Props 안정성 확인
→ Context 범위 확인
→ Memoization 필요 여부 판단
→ Profiler로 검증
```

---

### [실무]

최적화 우선순위:

1. State Colocation
2. Component Split
3. Context Split
4. Expensive Calculation 분리
5. `memo` / `useMemo` / `useCallback`
6. List Virtualization
7. Code Splitting
8. Bundle Analysis

주의:

- 렌더링 자체보다 느린 렌더링이 문제인지 확인
- 작은 컴포넌트의 re-render는 대부분 문제 아님
- Context Provider value 변경이 넓게 퍼지는지 확인
- 리스트 key가 불안정하면 렌더링 문제가 커짐
- 성능 최적화 전 측정 우선

---

### [FAQ]

Q. React에서 re-render는 무조건 나쁜가?

A.
아니다. React는 re-render를 전제로 동작한다. 문제는 비용이 큰 re-render가 자주 발생하는 경우이다.

Q. 성능 최적화는 무엇부터 해야 하나?

A.
State 위치와 컴포넌트 분리를 먼저 확인하고, 그 다음 memoization을 검토한다.

Q. Profiler는 왜 필요한가?

A.
추측이 아니라 실제 렌더링 비용과 빈도를 확인하기 위해 필요하다.

---

# 24. Ref Pattern Rules

## 24.1 `useRef` 사용 기준

### [개념]

`useRef`는 렌더링을 발생시키지 않는 mutable value를 저장하거나 DOM 요소에 접근할 때 사용하는 Hook이다.

---

### [핵심]

필수 포함:

- `useRef`
- DOM Ref
- Mutable Ref
- Previous Value
- Timer ID
- Imperative Handle
- Focus Management
- Avoid Re-render
- Ref Forwarding
- React 19 Ref Prop

예시:

```tsx
export function SearchInput() {
  const inputRef = React.useRef<HTMLInputElement | null>(null);

  function focusInput() {
    inputRef.current?.focus();
  }

  return (
    <>
      <input ref={inputRef} />
      <button onClick={focusInput}>Focus</button>
    </>
  );
}
```

---

### [실무]

사용 기준:

- DOM focus 제어
- Scroll 위치 제어
- Timer ID 저장
- 이전 값 저장
- 외부 라이브러리 instance 저장
- 렌더링과 무관한 mutable value 저장

주의:

- 화면에 표시되는 값은 state 사용
- ref 변경은 re-render를 발생시키지 않음
- DOM 직접 조작 남용 금지
- ref로 React 상태 흐름을 우회하지 않기
- 접근성 목적의 focus 제어는 허용

---

### [FAQ]

Q. `useRef`와 `useState` 차이는?

A.
`useState` 변경은 re-render를 발생시키고, `useRef` 변경은 re-render를 발생시키지 않는다.

Q. `useRef`는 언제 사용하나?

A.
DOM 접근, focus 제어, timer ID, 외부 인스턴스, 이전 값 저장처럼 렌더링과 직접 관련 없는 값을 저장할 때 사용한다.

---

# 25. TypeScript Component Pattern Rules

## 25.1 Props 타입 설계

### [개념]

TypeScript Component Pattern은 React 컴포넌트의 props, event, children, variant, ref, generic을 타입 안정성 있게 설계하는 규칙이다.

---

### [핵심]

필수 포함:

- Props Type
- `React.ReactNode`
- Event Type
- Discriminated Union
- Generic Component
- Optional Props
- Required Props
- Variant Props
- Callback Props
- Component Props
- Ref Type
- Polymorphic Type

예시:

```tsx
type ButtonProps =
  | {
      variant: "link";
      href: string;
      onClick?: never;
      children: React.ReactNode;
    }
  | {
      variant: "button";
      href?: never;
      onClick: () => void;
      children: React.ReactNode;
    };

export function Button(props: ButtonProps) {
  if (props.variant === "link") {
    return <a href={props.href}>{props.children}</a>;
  }

  return <button onClick={props.onClick}>{props.children}</button>;
}
```

---

### [실무]

작성 기준:

- `any` 지양
- `children`은 `React.ReactNode`
- Event 타입은 구체적으로 작성
- Variant에 따라 필요한 props가 다르면 Discriminated Union 사용
- Callback 이름은 `onSubmit`, `onChange`, `onSelect`처럼 이벤트 의도 표현
- Boolean Props가 많으면 Variant Union 검토
- 외부 HTML 속성을 받을 때 `ComponentPropsWithoutRef` 사용 가능
- 컴포넌트 API는 사용자가 잘못 쓰기 어렵게 설계

---

### [FAQ]

Q. `children` 타입은 무엇을 쓰나?

A.
일반적으로 `React.ReactNode`를 사용한다.

Q. Boolean Props가 많으면 어떻게 개선하나?

A.
`variant`, `size`, `status` 같은 명시적 prop이나 Discriminated Union으로 구조화한다.

Q. 컴포넌트 props에 `any`를 써도 되나?

A.
권장하지 않는다. Agent 코드 리뷰 기준에서는 타입 안정성을 해치는 문제로 본다.

---

# 26. Accessibility Pattern Rules

## 26.1 접근성 중심 React 패턴

### [개념]

Accessibility Pattern은 React 컴포넌트가 키보드, 스크린 리더, 포커스, ARIA 속성을 올바르게 지원하도록 설계하는 규칙이다.

---

### [핵심]

필수 포함:

- Semantic HTML
- ARIA
- Keyboard Navigation
- Focus Management
- Label
- Role
- Dialog Accessibility
- Menu Accessibility
- Form Error Message
- Screen Reader
- Focus Trap
- Escape Key
- Button vs Link

---

### [실무]

접근성 기준:

- 가능한 Semantic HTML 우선
- `div` 클릭 대신 `button` 사용
- 링크 이동은 `a` 또는 Link 사용
- Form input에는 label 연결
- 에러 메시지는 input과 연결
- Modal은 focus trap과 Escape 닫기 지원
- Dropdown / Menu는 키보드 이동 고려
- Toggle 상태는 `aria-expanded`, `aria-pressed` 등 명시
- 색상만으로 상태 전달 금지
- Loading / Error 상태를 스크린 리더가 인식 가능하게 구성

주의:

- ARIA는 Semantic HTML을 대체하는 만능 도구가 아님
- 잘못된 ARIA는 접근성을 더 해칠 수 있음
- Custom Component는 기본 HTML 동작을 잃기 쉬움

---

### [FAQ]

Q. React 컴포넌트에서 접근성은 왜 중요한가?

A.
Custom UI가 많아질수록 기본 HTML 동작을 잃기 쉬우므로 키보드와 스크린 리더 사용성을 명확히 보장해야 한다.

Q. Button과 Link는 어떻게 구분하나?

A.
동작 실행은 Button, 페이지 이동은 Link를 사용한다.

Q. ARIA만 붙이면 접근성이 해결되나?

A.
아니다. Semantic HTML, 키보드 동작, 포커스 관리가 함께 필요하다.

---

# 27. Testing Pattern Rules

## 27.1 React 고급 패턴 테스트

### [개념]

React Testing Pattern은 컴포넌트 구현 세부사항보다 사용자 행동과 화면 결과를 기준으로 검증하는 테스트 규칙이다.

---

### [핵심]

필수 포함:

- Component Test
- Hook Test
- User Event
- Accessibility Query
- Async Test
- Error State Test
- Loading State Test
- Form Test
- Context Provider Test
- Mocking
- Integration Test
- E2E Test

---

### [실무]

테스트 기준:

- 사용자 관점 쿼리 사용
- 구현 세부 state 직접 검증 지양
- Form 입력 / 제출 / 에러 메시지 검증
- Loading / Error / Empty State 검증
- Custom Hook은 상태 전이 중심 검증
- Context는 Provider 포함 테스트
- 비동기 UI는 await 처리
- 외부 API는 Mock 사용
- 접근성 속성 검증
- Snapshot 남용 금지

테스트 우선순위:

1. 핵심 사용자 Flow
2. Form Validation
3. Error / Loading State
4. Custom Hook State Transition
5. Compound Component Interaction
6. Accessibility Behavior

---

### [FAQ]

Q. React 컴포넌트 테스트는 무엇을 기준으로 해야 하나?

A.
구현 세부사항보다 사용자가 보고 클릭하고 입력하는 결과를 기준으로 테스트한다.

Q. Custom Hook도 테스트해야 하나?

A.
복잡한 상태 전이나 재사용 로직이 있다면 테스트하는 것이 좋다.

Q. Snapshot Test는 많이 써도 되나?

A.
남용하지 않는 것이 좋다. 의미 있는 사용자 행동과 결과 검증이 더 중요하다.

---

# 28. Troubleshooting Rules

## 28.1 자주 발생하는 문제

### [개념]

Troubleshooting 문서는 Agent가 React 코드 오류 원인과 해결책을 빠르게 검색할 수 있도록 문제 / 원인 / 해결 형식을 사용한다.

---

### [핵심]

필수 Troubleshooting 항목:

- Infinite Render
- Stale Closure
- Missing Hook Dependency
- Invalid Hook Call
- Context Re-render
- Controlled / Uncontrolled Warning
- Hydration Error
- Key Warning
- State Update on Unmounted Component
- Too Many Re-renders
- Memoization Bug
- Event Handler Immediate Execution
- Ref Null Error
- Error Boundary Not Catching Event Error
- Suspense Fallback Not Showing
- Optimistic UI Rollback Failure

---

### [실무]

형식:

```md
문제:

원인:

해결:
```

예시:

```md
문제:

- Too many re-renders 오류 발생

원인:

- 렌더링 중 state setter를 즉시 호출함
- 이벤트 핸들러에 함수 참조가 아니라 실행 결과를 전달함

해결:

- 렌더링 중 상태 변경 금지
- `onClick={() => setOpen(true)}`처럼 함수로 감싸기
```

예시:

```md
문제:

- Stale Closure로 오래된 state를 참조함

원인:

- callback이나 effect dependency가 누락됨
- 비동기 함수가 이전 렌더링의 값을 캡처함

해결:

- dependency array 점검
- functional update 사용
- 최신 값이 필요하면 ref 사용 검토
```

---

### [FAQ]

Q. Infinite Render는 왜 발생하나?

A.
렌더링 중 상태를 변경하거나 Effect Dependency가 잘못되어 렌더링과 상태 변경이 반복될 때 발생한다.

Q. Stale Closure는 무엇인가?

A.
함수가 생성된 시점의 오래된 state나 props를 계속 참조하는 문제이다.

Q. Context Re-render는 어떻게 줄이나?

A.
Provider 범위를 줄이고, value를 분리하거나 memoization하며, 자주 바뀌는 상태를 별도 Context로 분리한다.

---

# 29. Code Example Rules

## 29.1 코드 예제 작성 기준

### [개념]

Advanced React Pattern 문서의 Code Example은 Agent 코드 생성과 리뷰에 직접 사용될 수 있도록 짧고 목적이 명확해야 한다.

---

### [핵심]

코드 예제 필수 기준:

- TypeScript 우선
- Function Component 기준
- Hook Rules 준수
- 핵심 로직 중심
- 긴 전체 파일 금지
- 불필요한 import 최소화
- 상태 소유자 명확히 표시
- Controlled / Uncontrolled 구분 명확화
- 접근성 속성 포함 권장
- Error / Loading 상태 포함 권장

---

### [실무]

권장 예제 유형:

- Composition Component
- Slot Pattern
- Compound Component Context
- Custom Hook
- Reducer Pattern
- Controlled Input
- Context Provider
- Suspense / Error Boundary
- Transition
- Optimistic UI
- Memoization
- TypeScript Discriminated Union Props

금지 예제:

- Hook을 조건문 내부에서 호출
- 렌더링 중 state setter 호출
- `any` 남용
- 접근성 없는 clickable `div`
- Context에 모든 앱 상태 넣기
- 불필요한 `useMemo` / `useCallback` 남용
- Client Secret 노출
- Error를 무시하는 비동기 코드

---

### [FAQ]

Q. 코드 예제는 길어도 되나?

A.
길면 안 된다. RAG Retrieval과 코드 생성에 필요한 핵심 snippet 중심으로 작성한다.

Q. JavaScript 예제도 허용되나?

A.
가능하지만 TypeScript 예제를 우선한다.

---

# 30. Comparison Rules

## 30.1 필수 비교 대상

### [개념]

Advanced React Pattern 문서는 Agent의 구조 판단을 돕기 위해 비교 섹션을 적극 사용한다.

---

### [핵심]

필수 비교:

- Composition vs Inheritance
- Children Pattern vs Slot Pattern
- Slot Pattern vs Compound Component
- Render Props vs Custom Hook
- Custom Hook vs Utility Function
- Controlled vs Uncontrolled Component
- `useState` vs `useReducer`
- Props Drilling vs Context
- Context vs External Store
- Local State vs Global State
- Server State vs Client State
- `useMemo` vs `useCallback`
- `memo` vs Component Split
- `useTransition` vs `useDeferredValue`
- Loading State vs Pending State
- Error Boundary vs try/catch
- Optimistic UI vs Pessimistic UI
- Headless Component vs Styled Component
- HOC vs Hook
- Button vs Link

---

### [실무]

Comparison 작성 기준:

- 표 사용 권장
- 기준은 목적 / 장점 / 단점 / 사용 예시로 정리
- 결론을 명확히 작성
- “항상 A” 같은 절대 표현 금지
- 실무 판단 Flow 포함

---

### [FAQ]

Q. Render Props와 Custom Hook 중 무엇을 써야 하나?

A.
대부분의 새 코드에서는 Custom Hook이 단순하다. UI 렌더링 제어를 외부에 완전히 맡겨야 하면 Render Props를 고려한다.

Q. Context와 External Store는 어떻게 구분하나?

A.
낮은 빈도의 공유 값은 Context, 복잡하고 자주 바뀌는 앱 상태는 External Store를 고려한다.

---

# 31. Checklist Rules

## 31.1 문서 품질 체크리스트

### [개념]

Advanced React Pattern RAG 문서는 출력 전 구조, 용어, Retrieval Query, 코드 안전성을 검수해야 한다.

---

### [핵심]

Checklist:

- [ ] React Function Component 기준인가?
- [ ] TypeScript 예제를 우선했는가?
- [ ] Component Composition 기준을 포함했는가?
- [ ] Custom Hook 설계 기준을 포함했는가?
- [ ] State Colocation 판단 기준을 포함했는가?
- [ ] Controlled / Uncontrolled Component를 구분했는가?
- [ ] Compound Component 기준을 포함했는가?
- [ ] Context 사용 기준과 성능 주의를 포함했는가?
- [ ] Reducer Pattern 기준을 포함했는가?
- [ ] Async UI 상태를 분리했는가?
- [ ] Suspense / Error Boundary를 포함했는가?
- [ ] Transition / Optimistic UI를 포함했는가?
- [ ] Memoization 남용 주의를 포함했는가?
- [ ] Re-render 분석 기준을 포함했는가?
- [ ] TypeScript Props Pattern을 포함했는가?
- [ ] Accessibility Pattern을 포함했는가?
- [ ] Testing Pattern을 포함했는가?
- [ ] Troubleshooting을 포함했는가?
- [ ] FAQ를 충분히 포함했는가?
- [ ] Retrieval Queries를 포함했는가?
- [ ] 코드블록에 `id=""`가 없는가?
- [ ] 오타와 용어 혼용을 제거했는가?

---

### [실무]

검수 기준:

- Minimum Quality: 95/100
- Target Quality: 97+/100
- 문서 하나는 하나의 주제를 중심으로 작성
- Chunk 단위로 독립 검색 가능해야 함
- FAQ는 실제 사용자 질문 문장으로 작성
- Retrieval Queries는 Agent 검색 패턴 중심으로 작성
- Next.js App Router / Frontend Architecture 문서와 충돌하지 않아야 함

---

### [FAQ]

Q. Advanced React Pattern 문서 품질에서 가장 중요한 것은?

A.
상태 위치, 컴포넌트 합성, Hook 분리, 비동기 UI, 성능 최적화 판단 기준이 명확해야 한다.

---

# 32. Retrieval Optimization Rules

## 32.1 검색 최적화 키워드

### [개념]

Retrieval Optimization은 Agent가 사용자의 질문을 정확한 문서 Chunk로 연결하도록 키워드와 질문 패턴을 강화하는 규칙이다.

---

### [핵심]

강조 키워드:

- React
- Advanced React Pattern
- React Pattern
- Component Composition
- Children Pattern
- Slot Pattern
- Compound Component
- Render Props
- Custom Hook
- Hook Composition
- State Colocation
- State Lifting
- Controlled Component
- Uncontrolled Component
- Reducer Pattern
- `useReducer`
- Context Pattern
- Context Performance
- Provider Pattern
- Headless Component
- Polymorphic Component
- Higher Order Component
- Error Boundary
- Suspense
- Async UI
- Loading State
- Pending State
- Empty State
- Optimistic UI
- `useOptimistic`
- `useTransition`
- `useDeferredValue`
- `useActionState`
- Memoization
- `React.memo`
- `useMemo`
- `useCallback`
- Re-render Optimization
- Stale Closure
- Infinite Render
- TypeScript Props Pattern
- Discriminated Union Props
- Accessibility Pattern
- React Testing Pattern

---

### [실무]

FAQ와 Retrieval Queries에는 아래 표현을 포함한다.

- React 고급 패턴 뭐부터 봐야 해?
- Component Composition은 언제 써?
- Compound Component는 언제 써?
- Custom Hook은 언제 분리해?
- 상태는 어디에 둬야 해?
- Controlled Component와 Uncontrolled Component 차이는?
- useState와 useReducer 차이는?
- Context는 언제 써?
- Context 쓰면 왜 re-render 돼?
- Render Props와 Custom Hook 차이는?
- Headless Component는 뭐야?
- Polymorphic Component는 언제 써?
- useMemo와 useCallback은 언제 써?
- React memoization은 항상 해야 해?
- React re-render 왜 발생해?
- Stale Closure는 어떻게 해결해?
- Infinite Render는 왜 발생해?
- Suspense와 Error Boundary는 어떻게 써?
- useTransition은 언제 써?
- useOptimistic은 언제 써?
- React 19 Actions는 뭐야?
- React 컴포넌트 타입은 어떻게 설계해?

---

### [FAQ]

Q. Retrieval Queries는 왜 필요한가?

A.
사용자의 자연어 질문을 문서 Chunk와 매칭하기 위해 필요하다.

Q. 키워드 반복은 허용되나?

A.
허용된다. 단, 문서 품질을 해치지 않는 범위에서 검색 친화적으로 반복한다.

---

# 33. Version Rules

## 33.1 기준 버전

### [개념]

Advanced React Pattern 문서는 Modern React 기준으로 작성하며, React 버전 변화 가능성을 명확히 기록한다.

---

### [핵심]

기준:

- React 19+
- Modern React
- Function Component
- Hooks
- TypeScript
- Suspense
- Error Boundary
- React Actions
- `useActionState`
- `useOptimistic`
- `useTransition`
- `useDeferredValue`
- React Compiler 고려
- Next.js App Router 연계 가능

Legacy 제외:

- Class Component 중심 설계
- Lifecycle Method 중심 설명
- Mixins
- Legacy Context API
- String Ref
- jQuery 기반 DOM 제어
- 무분별한 HOC 중심 설계
- 무분별한 Render Props 중첩

---

### [실무]

문서 작성 시 주의:

- React 19 이후 Actions / Optimistic UI / Form 관련 패턴 포함
- React Compiler 도입 여부에 따라 memoization 전략이 달라질 수 있음
- Next.js App Router에서는 Server Component / Client Component 경계 고려
- 라이브러리별 Suspense 지원 여부 확인
- Experimental 기능은 명확히 표시
- 안정 기능과 실험 기능을 혼동하지 않기

---

### [FAQ]

Q. Advanced React Pattern 문서는 React 19 기준이어야 하나?

A.
그렇다. React 19 이후 Actions, `useActionState`, `useOptimistic`, Transition 관련 패턴을 포함해야 한다.

Q. Class Component 패턴은 제외해도 되나?

A.
대부분 제외한다. Error Boundary 구현처럼 필요한 경우만 제한적으로 다룬다.

---

# 34. Common Mistakes

## 34.1 자주 발생하는 실수

### [개념]

Common Mistakes는 Agent가 코드 리뷰와 오류 진단에서 자주 참조하는 검색 최적화 Chunk이다.

---

### [핵심]

자주 발생하는 실수:

- 모든 상태를 전역 상태로 올림
- Derived State를 중복 저장
- `useEffect`로 계산 가능한 값을 동기화
- Hook을 조건문 내부에서 호출
- Effect Dependency 누락
- 렌더링 중 state setter 호출
- Event Handler에 함수 실행 결과 전달
- Context에 자주 바뀌는 큰 객체 저장
- Provider value를 매 렌더링마다 새로 생성
- `useMemo` / `useCallback` 무분별 사용
- Memoization Dependency 누락
- List key에 index 남용
- Controlled / Uncontrolled Input 혼용
- 접근성 없는 clickable `div`
- Error State 없이 API 실패 무시
- Loading과 Empty State 혼동
- Optimistic UI 실패 rollback 누락
- Compound Component 사용 제약 문서화 누락
- TypeScript props에 `any` 남용
- Boolean Props 폭발 방치
- Custom Hook에 너무 많은 책임 부여

---

### [실무]

리뷰 기준:

- 상태 위치 확인
- Hook Dependency 확인
- Component API 단순성 확인
- Context 범위 확인
- Re-render 원인 확인
- Memoization 필요성 확인
- 비동기 상태 분리 확인
- Error / Loading / Empty State 확인
- 접근성 확인
- TypeScript Props 안정성 확인
- 테스트 가능성 확인

---

### [FAQ]

Q. Advanced React에서 가장 흔한 실수는?

A.
상태 위치를 잘못 잡거나 Hook Dependency를 누락하고, memoization을 무분별하게 적용하는 것이다.

Q. Boolean Props가 많으면 왜 위험한가?

A.
컴포넌트 조합 폭발과 조건 분기 증가로 API가 복잡해지고 테스트가 어려워진다.

Q. Hook Dependency를 무시해도 되나?

A.
안 된다. Stale Closure와 예측 불가능한 상태 버그가 발생할 수 있다.

---

# 35. Final Goal

## 35.1 최종 목표

### [개념]

Advanced React Pattern RAG 문서는 Agent가 React 기반 복잡한 UI를 설계, 생성, 검토, 수정할 수 있도록 만들어야 한다.

---

### [핵심]

Agent가 수행 가능해야 하는 작업:

- Component Composition 설계
- Children / Slot Pattern 적용
- Compound Component 구현
- Custom Hook 분리
- 상태 위치 결정
- Controlled / Uncontrolled Component 판단
- `useReducer` 적용 판단
- Context Provider 설계
- Context Re-render 문제 진단
- Async UI 상태 설계
- Suspense / Error Boundary 설계
- Transition 적용 판단
- Optimistic UI 구현
- Memoization 적용 여부 판단
- Re-render 원인 분석
- TypeScript Props API 설계
- Accessibility Review
- React Testing 전략 제안
- Advanced React 코드 리뷰
- Next.js App Router Client Component 설계와 연계

---

### [실무]

최종 품질 기준:

- 검색 가능한 Chunk 구조
- 명확한 용어 통일
- FAQ 강화
- 실무 판단 기준 포함
- 코드 예제는 짧고 안전하게 작성
- 상태 / Hook / 컴포넌트 경계 명확화
- 성능 / 접근성 / 테스트 위험 명시
- Retrieval Queries 포함

---

### [FAQ]

Q. Advanced React Pattern Domain Rules의 최종 목적은?

A.
Agent가 React 기반 프로젝트에서 고급 컴포넌트 설계, 상태 관리, Hook 분리, 성능 최적화, 접근성, 테스트, 코드 리뷰를 수행하도록 만드는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Advanced React Pattern 문서는 어떤 기준으로 작성해야 해?

A.
Component Composition, Custom Hook, State Colocation, Context, Reducer, Suspense, Error Boundary, Transition, Optimistic UI, Memoization 중심으로 작성해야 한다.

Q. React 고급 패턴 뭐부터 봐야 해?

A.
Component Composition, Custom Hook, State Colocation, Controlled Component, Context, Reducer Pattern, Suspense, Memoization 순서로 보는 것이 좋다.

Q. Component Composition은 언제 써?

A.
Card, Modal, Layout처럼 UI 조합이 다양하고 Boolean Props가 많아질 때 사용한다.

Q. Children Pattern과 Slot Pattern 차이는?

A.
`children`은 기본 콘텐츠 주입이고, Slot Pattern은 header, footer, actions처럼 특정 위치에 UI를 명명해서 전달하는 방식이다.

Q. Compound Component는 언제 써?

A.
Tabs, Accordion, Select, Menu처럼 여러 하위 컴포넌트가 하나의 상태를 공유해야 할 때 사용한다.

Q. Compound Component 단점은?

A.
Context Re-render, 암묵적 계층 제약, 디버깅 어려움이 생길 수 있다.

Q. Render Props는 언제 써?

A.
동작 로직은 재사용하되 렌더링 UI를 호출자가 완전히 제어해야 할 때 사용한다.

Q. Render Props와 Custom Hook 차이는?

A.
Render Props는 렌더링 함수를 전달하고, Custom Hook은 상태와 동작을 반환해 컴포넌트가 직접 UI를 렌더링한다.

Q. Custom Hook은 언제 분리해?

A.
여러 컴포넌트에서 같은 상태 로직, Effect 로직, 이벤트 로직이 반복될 때 분리한다.

Q. Custom Hook 이름은 꼭 use로 시작해야 해?

A.
그렇다. React Hook 규칙을 따르려면 Custom Hook 이름은 `use`로 시작해야 한다.

Q. 상태는 어디에 둬야 해?

A.
상태를 사용하는 컴포넌트와 가장 가까운 위치에 둔다. 여러 컴포넌트가 공유하면 공통 부모로 올린다.

Q. 모든 상태를 전역으로 올리면 안 돼?

A.
권장하지 않는다. 전역 상태가 많아지면 변경 범위와 디버깅 복잡도가 커진다.

Q. Derived State는 왜 조심해야 해?

A.
원본 상태와 파생 상태가 불일치할 수 있기 때문이다. 계산 가능한 값은 state로 중복 저장하지 않는 것이 좋다.

Q. Controlled Component와 Uncontrolled Component 차이는?

A.
Controlled Component는 React state가 값을 제어하고, Uncontrolled Component는 DOM이 값을 관리한다.

Q. Controlled Component는 언제 써?

A.
실시간 검증, 조건부 UI, 외부 제어가 필요한 입력 컴포넌트에 사용한다.

Q. Uncontrolled Component는 언제 써?

A.
단순 제출 Form, 파일 입력, 성능이 중요한 대규모 Form에서 사용할 수 있다.

Q. `useState`와 `useReducer` 차이는?

A.
단순 상태는 `useState`, 복잡한 상태 전이와 action 의미가 중요하면 `useReducer`를 사용한다.

Q. reducer 안에서 API 호출해도 돼?

A.
안 된다. reducer는 순수 함수여야 하며 API 호출 같은 side effect는 외부에서 처리해야 한다.

Q. Context는 언제 써?

A.
Theme, Locale, Auth Summary, Feature Flag처럼 여러 하위 컴포넌트가 공유해야 하고 변경 빈도가 낮은 값에 적합하다.

Q. Context 쓰면 왜 re-render 돼?

A.
Provider value가 변경되면 해당 Context를 사용하는 컴포넌트들이 다시 렌더링될 수 있기 때문이다.

Q. Context re-render는 어떻게 줄여?

A.
Provider 범위를 줄이고, value를 분리하거나 memoization하며, 자주 바뀌는 상태를 별도 Context로 분리한다.

Q. Context와 External Store는 어떻게 구분해?

A.
낮은 빈도의 공유 값은 Context, 복잡하고 자주 바뀌는 앱 상태는 External Store를 고려한다.

Q. Headless Component는 뭐야?

A.
스타일을 고정하지 않고 상태, 동작, 접근성 로직만 제공해 다양한 UI로 조합할 수 있게 하는 패턴이다.

Q. Polymorphic Component는 언제 써?

A.
Design System에서 같은 스타일을 유지하면서 렌더링 태그를 `button`, `a`, `span` 등으로 바꿔야 할 때 사용한다.

Q. HOC는 아직 써?

A.
기존 코드와 라이브러리에서 볼 수 있다. 새 코드에서는 Custom Hook이나 Composition을 우선 검토한다.

Q. Loading State와 Pending State 차이는?

A.
Loading은 초기 데이터 로딩, Pending은 사용자 액션 처리 중 상태에 가깝다.

Q. Empty State는 Error야?

A.
아니다. 요청은 성공했지만 표시할 데이터가 없는 상태이다.

Q. Suspense는 언제 써?

A.
비동기 데이터나 lazy component가 준비될 때까지 fallback UI를 보여주고 싶을 때 사용한다.

Q. Error Boundary는 무엇을 잡아?

A.
하위 컴포넌트 렌더링 중 발생한 오류를 잡아 fallback UI를 보여준다.

Q. `useTransition`은 언제 써?

A.
사용자 입력은 즉시 반영하면서 무거운 렌더링 업데이트를 뒤로 미루고 싶을 때 사용한다.

Q. `useTransition`이 API 요청을 빠르게 해?

A.
아니다. API 속도 개선이 아니라 렌더링 우선순위를 조정해 UI 응답성을 높이는 도구이다.

Q. `useDeferredValue`는 언제 써?

A.
검색어처럼 값은 즉시 바뀌지만 무거운 결과 렌더링은 늦게 반영하고 싶을 때 사용한다.

Q. Optimistic UI는 언제 써?

A.
Like, Bookmark, Comment처럼 성공 가능성이 높고 즉시 피드백이 중요한 작업에 사용한다.

Q. `useOptimistic`은 무엇을 돕나?

A.
서버 응답 전 임시 UI 상태를 관리하고 실패 시 rollback할 수 있는 구조를 만드는 데 도움을 준다.

Q. `useActionState`는 언제 써?

A.
Form Action의 결과 상태와 pending 상태를 함께 관리해야 할 때 사용한다.

Q. React Actions는 뭐야?

A.
비동기 mutation을 선언적으로 처리하기 위한 React 패턴이다.

Q. `useMemo`는 항상 써야 해?

A.
아니다. 계산 비용이 크거나 참조 안정성이 필요한 경우에만 사용한다.

Q. `useCallback`은 언제 써?

A.
함수 참조 안정성이 필요하거나 memoized child에 callback을 전달할 때 사용한다.

Q. `React.memo`는 언제 써?

A.
props가 자주 변하지 않는 비용 큰 컴포넌트의 불필요한 렌더링을 줄일 때 사용한다.

Q. Memoization이 버그를 만들 수 있어?

A.
그렇다. Dependency가 누락되면 stale value나 stale closure 문제가 생길 수 있다.

Q. React re-render는 왜 발생해?

A.
state 변경, props 변경, parent re-render, context value 변경, key 변경 때문에 발생한다.

Q. Re-render는 무조건 나쁜 거야?

A.
아니다. 문제는 비용이 큰 re-render가 자주 발생하는 경우이다.

Q. React 성능 최적화는 무엇부터 해야 해?

A.
State 위치와 컴포넌트 분리를 먼저 확인하고, 그 다음 memoization을 검토한다.

Q. Stale Closure는 어떻게 해결해?

A.
Dependency array를 점검하고, 필요하면 functional update나 ref를 사용한다.

Q. Infinite Render는 왜 발생해?

A.
렌더링 중 상태를 변경하거나 Effect Dependency가 잘못되어 렌더링과 상태 변경이 반복될 때 발생한다.

Q. `useRef`와 `useState` 차이는?

A.
`useState` 변경은 re-render를 발생시키고, `useRef` 변경은 re-render를 발생시키지 않는다.

Q. React 컴포넌트 타입은 어떻게 설계해?

A.
Props 타입을 명확히 정의하고, variant별 필수 props가 다르면 Discriminated Union을 사용한다.

Q. Boolean Props가 많으면 어떻게 개선해?

A.
`variant`, `size`, `status` 같은 명시적 prop이나 Compound Component / Composition으로 개선한다.

Q. Button과 Link는 어떻게 구분해?

A.
동작 실행은 Button, 페이지 이동은 Link를 사용한다.

Q. React 컴포넌트 테스트는 무엇을 기준으로 해?

A.
구현 세부사항보다 사용자가 보고 클릭하고 입력하는 결과를 기준으로 테스트한다.

Q. Advanced React 코드 리뷰에서 가장 중요한 것은?

A.
상태 위치, Hook Dependency, Component API, Context 범위, Re-render 원인, 접근성, 테스트 가능성을 확인하는 것이다.

Q. Advanced React Pattern RAG 문서 최종 목표는?

A.
Agent가 React 기반 프로젝트에서 고급 컴포넌트 설계, 상태 관리, Hook 분리, 비동기 UI, 성능 최적화, 접근성, 테스트, 코드 리뷰를 수행하게 만드는 것이다.
