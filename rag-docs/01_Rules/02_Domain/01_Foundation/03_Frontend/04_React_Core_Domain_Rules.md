# React Core Domain Rules

---

# 1. Domain Purpose

## 1.1 Purpose

### [개념]

React Core Domain 문서는 Frontend Agent / Review Agent / PM Agent용 RAG 문서 제작 규칙이다.

목적:

- React 기본 개념 이해
- Component 기반 UI 작성 지원
- JSX 작성 지원
- Props / State 이해 지원
- Event Handling 구현 지원
- Conditional Rendering 구현 지원
- List Rendering 구현 지원
- React Hook 기초 이해 지원
- useState / useEffect 실무 사용 기준 제공
- Frontend 화면 구조 설계 지원
- Backend API 연동 전 React 기본 흐름 제공
- React Component Design 문서로 이어지는 기반 제공

---

### [핵심]

우선순위:

1. React Component
2. JSX
3. Props
4. State
5. Event Handling
6. Conditional Rendering
7. List Rendering
8. Hook Basics
9. useState
10. useEffect
11. Component Lifecycle Concept
12. React Rendering Flow
13. React TypeScript Readiness

---

### [실무]

2026 실무 기준에서 React Core 문서는 React API 암기용 문서가 아니다.

Frontend Agent가 아래 작업을 수행할 수 있도록 작성한다.

- 기본 React Component 작성
- JSX 구조 작성
- Props 전달 구조 설계
- State 기반 UI 갱신
- Event Handler 작성
- 조건부 화면 처리
- 목록 렌더링
- useState / useEffect 사용
- API 호출 위치 판단
- loading / error / empty / success UI 구성
- Component 분리 전 기본 구조 설계
- React Component Design 문서로 연결

---

### [FAQ]

Q. React Core 문서는 사람 공부용 문서야?

A.
아니다. Frontend Agent가 React 화면과 기본 Component 로직을 생성하고 검토하기 위한 RAG 문서다.

Q. React Core는 HTML/CSS/JavaScript와 어떤 관계야?

A.
React는 HTML 구조를 JSX로 작성하고 JavaScript로 UI 상태와 이벤트를 제어한다. HTML/CSS/JavaScript Foundation 위에 React Core가 올라간다.

Q. React Core에서 가장 중요한 기준은 뭐야?

A.
Component, JSX, Props, State, Event Handling, Conditional Rendering, List Rendering, useState, useEffect다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

React Core 문서는 React 기본 화면 구현에 필요한 범위를 포함한다.

포함 범위:

- React Overview
- Component
- Functional Component
- JSX
- JSX Expression
- Props
- Props Destructuring
- State
- useState
- Event Handling
- Controlled Input Basics
- Conditional Rendering
- List Rendering
- key
- Fragment
- Children Basics
- Hook Basics
- useEffect
- Effect Dependency
- Cleanup Function
- Rendering Flow
- Re-render
- Component Lifecycle Concept
- React DevTools Basics
- React TypeScript Basics
- API Call Basic Pattern
- Loading / Error / Empty State
- Component File Structure Basics
- Common React Errors
- React Debugging Basics

---

### [핵심]

반드시 포함:

- React는 Component 기반 UI Library
- Component는 UI를 재사용 가능한 단위로 분리
- JSX는 JavaScript 안에서 UI 구조를 표현
- Props는 부모에서 자식으로 전달되는 읽기 전용 데이터
- State는 Component 내부에서 변경 가능한 UI 데이터
- State 변경은 Re-render를 유발
- Hook은 Functional Component에서 React 기능을 사용하는 함수
- useEffect는 외부 시스템과 동기화할 때 사용
- List Rendering에는 안정적인 key 필요
- React는 직접 DOM 조작보다 State 기반 Rendering 우선

---

### [실무]

React Core는 React Component Design / React Router / State Management / Data Fetching 문서의 기반이다.

실무 연결:

```text
HTML CSS Foundation
→ JavaScript Foundation
→ TypeScript Foundation
→ React Core
→ React Component Design
→ React Router
→ State Management
→ Data Fetching & REST API Integration
```

---

### [FAQ]

Q. React Core에서 Router도 깊게 다뤄?

A.
아니다. React Router는 별도 Domain Rules에서 다룬다.

Q. React Core에서 상태관리 라이브러리도 다뤄?

A.
아니다. useState 중심의 기본 상태만 다루고 Zustand, Redux, TanStack Query는 별도 문서에서 다룬다.

Q. React Core에서 CSS 방법론도 깊게 다뤄?

A.
아니다. className 기반 스타일 연결 정도만 다루고 CSS Module, Styled Components, Tailwind는 별도 문서에서 다룬다.

---

## 2.2 Excluded Scope

### [개념]

React Core 문서에서는 고급 React Architecture와 외부 라이브러리 심화를 제외한다.

제외 범위:

- React Router 심화
- Global State Management 심화
- Redux / Zustand / Recoil
- TanStack Query 심화
- React Hook Form 심화
- Advanced Custom Hook
- Compound Component Pattern
- Render Props Pattern
- Context API 심화
- Suspense 심화
- Server Components
- Next.js App Router
- SSR / SSG / ISR
- Performance Optimization 심화
- Memoization 심화
- Testing Library 심화
- Design System 심화

---

### [핵심]

제외 이유:

- Core 범위 초과
- React Component Design / State Management / Data Fetching 문서와 분리 필요
- Agent Retrieval 혼선 방지
- Chunk 품질 유지
- React 기본 작성 능력에 집중

---

### [실무]

고급 기술은 별도 Domain Rules에서 관리한다.

예:

```text
React Core
→ React Component Design
→ React Router
→ State Management
→ Data Fetching
→ Frontend Architecture
```

---

### [FAQ]

Q. useMemo와 useCallback은 여기서 다뤄?

A.
기본 개념 언급은 가능하지만 심화 최적화는 React Performance 또는 Advanced React Pattern 문서에서 다룬다.

Q. Context API는 여기서 다뤄?

A.
기초 소개는 가능하지만 전역 상태 설계는 State Management 문서에서 다룬다.

Q. Next.js는 여기서 다뤄?

A.
아니다. Next.js는 Frontend Expert 또는 Next.js App Router 문서에서 다룬다.

---

# 3. Section Priority

## 3.1 Required Sections

### [개념]

React Core RAG 문서는 모든 주요 Chunk에 아래 Section을 우선 포함한다.

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
- [실무]: 실제 React 적용 기준
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

Q. 모든 React Core 문서에 FAQ가 필요해?

A.
필요하다. FAQ는 사용자 질문과 RAG 검색 매칭을 강화한다.

Q. [면접] 섹션을 써도 돼?

A.
안 된다. 반드시 [FAQ] 섹션을 사용한다.

---

## 3.2 Recommended Sections

### [개념]

React Core 문서에는 실무 적용과 검증을 위해 추가 Section을 포함할 수 있다.

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

- Rendering Flow 설명 → [Flow], [예제]
- Props / State 설명 → [Comparison], [주의]
- useEffect 설명 → [Flow], [Troubleshooting]
- List Rendering 설명 → [예제], [주의]
- React Error 설명 → [Troubleshooting]
- Component 기본 구조 설명 → [Best Practice], [Checklist]

---

### [실무]

예시:

```md
### [Flow]

User Event
→ Event Handler
→ State Update
→ Re-render
→ UI Update
```

---

### [FAQ]

Q. React Core 문서에 Troubleshooting이 필요한 이유는?

A.
무한 렌더링, key 오류, state 직접 변경, useEffect dependency 문제 같은 오류가 자주 발생하기 때문이다.

Q. Comparison은 언제 쓰면 좋아?

A.
Props vs State, Controlled vs Uncontrolled, useEffect vs Event Handler처럼 헷갈리는 개념을 비교할 때 사용한다.

---

# 4. React Overview Rules

## 4.1 React Overview

### [개념]

React는 Component 기반으로 사용자 인터페이스를 만들기 위한 JavaScript UI Library다.

React는 화면을 작은 Component 단위로 나누고, 데이터 변화에 따라 UI를 다시 렌더링한다.

기본 Flow:

```text
State / Props Change
→ Component Render
→ Virtual UI Description
→ DOM Update
→ User sees UI
```

---

### [핵심]

반드시 설명:

- React는 UI Library
- Component 기반 구조
- Declarative UI
- JSX 사용
- Props로 데이터 전달
- State로 UI 상태 관리
- State 변경 시 Re-render
- DOM 직접 조작보다 상태 기반 렌더링
- React는 화면 구조와 로직을 Component로 묶음

---

### [실무]

React는 아래 상황에서 사용된다.

- 재사용 가능한 UI Component 작성
- 화면 상태가 자주 바뀌는 서비스
- API 데이터 기반 화면
- Form 입력 처리
- 조건부 UI
- 목록 UI
- SPA 구조
- Frontend 팀 협업 프로젝트

React 문서는 JavaScript / TypeScript 기반으로 작성한다.

권장:

- Functional Component 기준
- Hook 기준
- class component 중심 설명 제외
- 명확한 Props / State 구조
- API 응답 상태 분리

---

### [FAQ]

Q. React는 Framework야 Library야?

A.
React 자체는 UI Library다. Router, 상태관리, 데이터 패칭 등을 함께 사용하면 Framework처럼 구성할 수 있다.

Q. React는 DOM을 직접 조작해?

A.
일반적으로 직접 조작하지 않는다. State와 Props 변화에 따라 React가 UI를 갱신한다.

Q. React에서 화면이 바뀌는 기준은 뭐야?

A.
주로 State 또는 Props가 변경되면 Component가 다시 렌더링되고 화면이 갱신된다.

---

## 4.2 Declarative UI Rules

### [개념]

Declarative UI는 DOM을 어떻게 바꿀지 직접 명령하기보다 현재 상태에 따라 어떤 UI가 보여야 하는지 선언하는 방식이다.

---

### [핵심]

명령형 방식:

```javascript
button.disabled = true;
button.textContent = "Loading";
```

선언형 방식:

```jsx
<button disabled={loading}>{loading ? "Loading" : "Submit"}</button>
```

핵심 차이:

- Imperative UI: DOM 변경 절차를 직접 작성
- Declarative UI: 상태에 따른 UI 결과를 작성
- React는 Declarative UI 방식
- State가 UI의 기준

---

### [실무]

React에서는 DOM 조작보다 상태를 변경한다.

권장 Flow:

```text
User Action
→ State Change
→ React Render
→ UI Result
```

금지:

- document.querySelector로 UI 직접 변경 남용
- innerHTML로 React UI 변경
- DOM 상태와 React State 불일치 발생
- React 외부에서 Component UI 강제 변경

---

### [FAQ]

Q. React에서 document.querySelector를 쓰면 안 돼?

A.
대부분의 UI 변경에는 쓰지 않는다. React에서는 State와 Props로 UI를 제어하는 것이 기본이다.

Q. Declarative UI가 왜 좋아?

A.
상태와 UI 관계가 명확해져 유지보수와 디버깅이 쉬워진다.

---

# 5. Component Rules

## 5.1 Component Basics

### [개념]

Component는 React UI를 구성하는 재사용 가능한 단위다.

예:

```jsx
function FestivalCard() {
  return (
    <section className="festival-card">
      <h2>Festival Title</h2>
      <p>Festival Description</p>
    </section>
  );
}
```

---

### [핵심]

반드시 포함:

- Functional Component
- Component Name PascalCase
- Return JSX
- Reusable UI Unit
- Props Input
- State Internal Data
- Component Composition
- Component File Separation

---

### [실무]

Component 작성 기준:

- 이름은 PascalCase
- 하나의 Component는 하나의 주요 책임
- UI 구조가 커지면 하위 Component로 분리
- Props로 외부 데이터 전달
- State는 필요한 Component에만 위치
- Component 내부 로직이 길어지면 함수 분리
- 재사용 가능한 단위로 설계

좋은 예:

```jsx
function FestivalCard({ title, region }) {
  return (
    <article className="festival-card">
      <h2>{title}</h2>
      <p>{region}</p>
    </article>
  );
}
```

---

### [FAQ]

Q. Component 이름은 왜 대문자로 시작해?

A.
React가 소문자는 HTML 태그로 보고 대문자로 시작하는 이름을 Component로 인식하기 때문이다.

Q. Component는 얼마나 작게 나눠야 해?

A.
역할이 명확하고 재사용 가능하거나 복잡도를 줄일 수 있을 때 분리한다.

Q. Component 안에 Component를 계속 만들면 돼?

A.
간단한 경우는 가능하지만 매 렌더링마다 새 함수가 만들어질 수 있어 일반적으로 파일 또는 외부 함수로 분리한다.

---

## 5.2 Functional Component Rules

### [개념]

Functional Component는 함수로 작성하는 React Component다.

현대 React에서는 Functional Component와 Hook을 기본으로 사용한다.

---

### [핵심]

반드시 포함:

- function component
- arrow function component
- props parameter
- return JSX
- hook usage
- no class component 중심 설명

예:

```jsx
function SearchButton({ onClick }) {
  return (
    <button type="button" onClick={onClick}>
      Search
    </button>
  );
}
```

---

### [실무]

권장:

- Function Declaration 또는 Arrow Function 중 프로젝트 컨벤션 유지
- Component 이름 명확화
- Props 구조 명확화
- JSX return 명확화
- Hook은 Component 최상위에서 호출
- 조건문 내부에서 Hook 호출 금지

---

### [FAQ]

Q. React에서 class component를 써야 해?

A.
신규 코드에서는 Functional Component와 Hook을 기준으로 작성한다. 기존 코드 유지보수에서 class component를 볼 수는 있다.

Q. Functional Component에서도 상태를 쓸 수 있어?

A.
가능하다. useState 같은 Hook을 사용한다.

---

## 5.3 Component Composition Rules

### [개념]

Component Composition은 작은 Component를 조합해 큰 UI를 만드는 방식이다.

---

### [핵심]

필수 포함:

- parent component
- child component
- props passing
- children
- reusable component
- layout component
- page component

---

### [실무]

예:

```jsx
function FestivalList({ festivals }) {
  return (
    <section>
      {festivals.map((festival) => (
        <FestivalCard
          key={festival.id}
          title={festival.title}
          region={festival.region}
        />
      ))}
    </section>
  );
}
```

설계 Flow:

```text
Page
→ Section
→ List
→ Card
→ Button / Input
```

주의:

- 너무 깊은 props 전달은 복잡도 증가
- 공통 UI는 재사용 Component로 분리
- Page Component와 UI Component 역할 구분
- Composition은 상속보다 우선

---

### [FAQ]

Q. React에서 상속을 많이 써?

A.
아니다. React에서는 상속보다 Component Composition을 우선한다.

Q. Page Component와 UI Component 차이는?

A.
Page Component는 화면 단위이며 데이터와 흐름을 가질 수 있고, UI Component는 재사용 가능한 표시 단위다.

---

# 6. JSX Rules

## 6.1 JSX Basics

### [개념]

JSX는 JavaScript 안에서 HTML과 비슷한 UI 구조를 작성하는 문법이다.

예:

```jsx
const element = <h1>Hello React</h1>;
```

JSX는 JavaScript 표현식으로 변환된다.

---

### [핵심]

반드시 설명:

- JSX는 HTML이 아님
- JavaScript 표현식 사용 가능
- 하나의 부모 요소 필요
- class 대신 className 사용
- for 대신 htmlFor 사용
- self-closing tag 필요
- 중괄호 `{}`로 JavaScript expression 사용
- statement는 JSX 내부에 직접 작성 불가

---

### [실무]

좋은 예:

```jsx
function FestivalTitle({ title }) {
  return <h1 className="page-title">{title}</h1>;
}
```

JSX expression 예:

```jsx
<p>{festival.title}</p>
<p>{festival.averageRating ?? "평점 없음"}</p>
```

주의:

- JSX 안에는 if문 statement 직접 작성 불가
- map 사용 시 key 필요
- className 오타 주의
- 중괄호 안에는 expression 사용
- 여러 요소 반환 시 Fragment 사용

---

### [FAQ]

Q. JSX는 HTML이야?

A.
아니다. JSX는 JavaScript 안에서 UI 구조를 표현하는 문법이며 React가 처리한다.

Q. JSX에서 class 대신 className을 쓰는 이유는?

A.
class는 JavaScript 예약어와 충돌 가능성이 있어 React JSX에서는 className을 사용한다.

Q. JSX에서 if문을 바로 쓸 수 있어?

A.
JSX 내부에는 statement를 직접 쓸 수 없다. 조건부 렌더링은 삼항 연산자, &&, 함수 분리 등을 사용한다.

---

## 6.2 JSX Expression Rules

### [개념]

JSX Expression은 JSX 내부에서 중괄호 `{}`를 사용해 JavaScript 값을 표현하는 방식이다.

---

### [핵심]

사용 가능:

- variable
- function call
- ternary expression
- logical expression
- array map result
- null
- string
- number

사용 불가:

- if statement
- for statement
- while statement
- object 직접 렌더링

---

### [실무]

예:

```jsx
function FestivalInfo({ festival }) {
  return (
    <article>
      <h2>{festival.title}</h2>
      <p>{festival.region}</p>
      <p>{festival.averageRating ?? "평점 없음"}</p>
    </article>
  );
}
```

주의:

```jsx
<div>{festival}</div>
```

객체를 직접 렌더링하면 오류가 발생할 수 있다.

개선:

```jsx
<div>{festival.title}</div>
```

---

### [FAQ]

Q. JSX 중괄호 안에 객체를 넣어도 돼?

A.
객체 자체는 React child로 렌더링할 수 없다. 객체의 문자열 property 등을 렌더링해야 한다.

Q. JSX에서 함수 호출해도 돼?

A.
가능하지만 렌더링마다 실행되므로 무거운 연산은 분리하거나 최적화를 고려한다.

---

## 6.3 Fragment Rules

### [개념]

Fragment는 불필요한 DOM 요소를 추가하지 않고 여러 JSX 요소를 묶는 기능이다.

예:

```jsx
function HeaderInfo() {
  return (
    <>
      <h1>Title</h1>
      <p>Description</p>
    </>
  );
}
```

---

### [핵심]

필수 포함:

- Fragment
- empty tag syntax
- one parent rule
- no extra DOM
- key with Fragment list

---

### [실무]

Fragment 사용 상황:

- 불필요한 div 추가 방지
- table 구조 유지
- 여러 요소 반환
- list에서 여러 형제 요소 반환

key가 필요한 경우:

```jsx
<React.Fragment key={item.id}>
  <dt>{item.title}</dt>
  <dd>{item.description}</dd>
</React.Fragment>
```

---

### [FAQ]

Q. JSX에서 왜 하나의 부모 요소가 필요해?

A.
Component는 하나의 JSX 값만 반환해야 하기 때문이다. 여러 요소는 Fragment로 묶을 수 있다.

Q. 빈 태그 `<>`와 React.Fragment 차이는?

A.
둘 다 Fragment지만 key가 필요한 경우에는 `React.Fragment`를 사용한다.

---

# 7. Props Rules

## 7.1 Props Basics

### [개념]

Props는 부모 Component가 자식 Component에 전달하는 읽기 전용 데이터다.

예:

```jsx
function FestivalCard({ title }) {
  return <h2>{title}</h2>;
}

function FestivalPage() {
  return <FestivalCard title="Spring Festival" />;
}
```

---

### [핵심]

반드시 설명:

- Props는 Parent → Child 방향 전달
- Props는 읽기 전용
- Props Destructuring 사용 가능
- Props로 data 전달
- Props로 callback 전달
- Props 변경 시 Child Re-render 가능
- Props 직접 수정 금지

---

### [실무]

Props 사용 기준:

- 외부에서 주입되는 데이터
- 재사용 Component 설정값
- Event Callback
- UI 표시 데이터
- children
- optional props 기본값

좋은 예:

```jsx
function FestivalCard({ title, imageUrl, onSelect }) {
  return (
    <article onClick={onSelect}>
      <img src={imageUrl} alt={title} />
      <h2>{title}</h2>
    </article>
  );
}
```

---

### [FAQ]

Q. Props는 수정해도 돼?

A.
안 된다. Props는 읽기 전용이다. 변경이 필요하면 부모 State를 변경하는 callback을 전달한다.

Q. Props는 어느 방향으로 전달돼?

A.
부모 Component에서 자식 Component로 전달된다.

Q. Props로 함수도 전달할 수 있어?

A.
가능하다. 자식에서 발생한 이벤트를 부모에게 알릴 때 callback props를 자주 사용한다.

---

## 7.2 Props Destructuring Rules

### [개념]

Props Destructuring은 Props 객체에서 필요한 값을 구조 분해로 꺼내는 방식이다.

예:

```jsx
function UserProfile({ name, email }) {
  return (
    <section>
      <h2>{name}</h2>
      <p>{email}</p>
    </section>
  );
}
```

---

### [핵심]

필수 포함:

- props object
- destructuring
- default value
- rest props basics
- readability
- TypeScript props type 연결

---

### [실무]

권장:

```jsx
function Button({ type = "button", disabled = false, children }) {
  return (
    <button type={type} disabled={disabled}>
      {children}
    </button>
  );
}
```

주의:

- Props 개수가 너무 많으면 Component 책임 검토
- 중첩 객체 Destructuring 과도 사용 금지
- 기본값 설정 위치 일관성 유지
- TypeScript Props Type과 정합성 유지

---

### [FAQ]

Q. Props Destructuring은 왜 써?

A.
props.title처럼 반복 접근하지 않고 필요한 값을 명확하게 사용할 수 있기 때문이다.

Q. Props가 너무 많으면 어떻게 해?

A.
Component 책임을 분리하거나 관련 데이터를 객체로 묶을지 검토한다.

---

## 7.3 Children Rules

### [개념]

children은 Component 태그 사이에 전달되는 React Node다.

예:

```jsx
function Card({ children }) {
  return <section className="card">{children}</section>;
}

function Page() {
  return (
    <Card>
      <h2>Title</h2>
      <p>Description</p>
    </Card>
  );
}
```

---

### [핵심]

필수 포함:

- children
- wrapper component
- layout component
- reusable container
- composition
- ReactNode TypeScript 연결

---

### [실무]

children 사용 적합 상황:

- Card
- Modal
- Layout
- Section
- Button
- FormGroup
- 공통 wrapper UI

주의:

- children 구조가 복잡하면 명시적 props 검토
- 너무 많은 암묵적 children 의존 금지
- 접근성 구조 유지

---

### [FAQ]

Q. children은 언제 써?

A.
Component 내부 내용을 외부에서 자유롭게 조합해야 할 때 사용한다.

Q. children과 props 차이는?

A.
children은 태그 사이에 전달되는 특별한 props이고, 일반 props는 속성 형태로 전달된다.

---

# 8. State Rules

## 8.1 State Basics

### [개념]

State는 Component 내부에서 관리되는 변경 가능한 데이터다.

State가 변경되면 React는 Component를 다시 렌더링한다.

예:

```jsx
import { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <button type="button" onClick={() => setCount(count + 1)}>
      {count}
    </button>
  );
}
```

---

### [핵심]

반드시 설명:

- State는 UI 상태 데이터
- useState로 생성
- setter로 변경
- 직접 변경 금지
- State 변경 시 Re-render
- 초기값 중요
- 이전 State 기반 업데이트는 functional update 권장

---

### [실무]

State 사용 대상:

- input value
- modal open 여부
- selected item
- loading 상태
- error 상태
- API response data
- pagination page
- filter 조건

State로 두지 않아도 되는 값:

- Props로 계산 가능한 값
- 렌더링 중 계산 가능한 값
- 고정 상수
- DOM에서 직접 읽지 않아도 되는 값

---

### [FAQ]

Q. State는 언제 써?

A.
사용자 행동이나 API 응답에 따라 화면이 바뀌어야 하는 값을 State로 둔다.

Q. State를 직접 바꾸면 안 돼?

A.
안 된다. React가 변경을 감지하지 못할 수 있으므로 setter 함수를 사용해야 한다.

Q. State가 바뀌면 무슨 일이 일어나?

A.
Component가 다시 렌더링되고 변경된 State 기준으로 UI가 갱신된다.

---

## 8.2 useState Rules

### [개념]

useState는 Functional Component에서 State를 선언하고 변경하기 위한 React Hook이다.

예:

```jsx
const [keyword, setKeyword] = useState("");
```

---

### [핵심]

필수 포함:

- state value
- setter function
- initial value
- functional update
- object state
- array state
- nullable state
- TypeScript generic basics

---

### [실무]

문자열 State:

```jsx
const [keyword, setKeyword] = useState("");
```

불리언 State:

```jsx
const [open, setOpen] = useState(false);
```

배열 State:

```jsx
const [festivals, setFestivals] = useState([]);
```

이전 State 기반 업데이트:

```jsx
setCount((prevCount) => prevCount + 1);
```

배열 업데이트:

```jsx
setFestivals((prevFestivals) => [...prevFestivals, newFestival]);
```

객체 업데이트:

```jsx
setUser((prevUser) => ({
  ...prevUser,
  name: "newName",
}));
```

주의:

- setter 호출 직후 State 값은 즉시 바뀐 것처럼 읽히지 않을 수 있음
- object / array 직접 mutation 금지
- 이전 State 기반이면 functional update 사용
- 초기값 타입 명확화
- 불필요한 State 생성 금지

---

### [FAQ]

Q. setState 호출 직후 값이 바로 바뀌어?

A.
React State 업데이트는 비동기적으로 처리될 수 있어 호출 직후 기존 값이 보일 수 있다.

Q. 배열 State는 push로 바꾸면 돼?

A.
안 된다. 새 배열을 만들어 setter에 전달해야 한다.

Q. 객체 State는 property만 바꾸면 돼?

A.
안 된다. 기존 객체를 직접 수정하지 말고 spread로 새 객체를 만들어야 한다.

---

## 8.3 Derived State Rules

### [개념]

Derived State는 기존 Props나 State로부터 계산 가능한 값이다.

계산 가능한 값은 별도 State로 두지 않는 것이 좋다.

---

### [핵심]

필수 포함:

- derived value
- avoid duplicate state
- props based calculation
- state based calculation
- render calculation
- memoization basics mention

---

### [실무]

나쁜 예:

```jsx
const [firstName, setFirstName] = useState("Jun");
const [lastName, setLastName] = useState("Kim");
const [fullName, setFullName] = useState("Jun Kim");
```

좋은 예:

```jsx
const fullName = `${firstName} ${lastName}`;
```

목록 필터 예:

```jsx
const filteredFestivals = festivals.filter((festival) =>
  festival.title.includes(keyword),
);
```

주의:

- 원본 State와 파생 State 불일치 가능
- 계산 비용이 큰 경우에만 memoization 고려
- Core 문서에서는 useMemo 심화 제외

---

### [FAQ]

Q. 계산 가능한 값도 State로 둬야 해?

A.
대부분 아니다. Props나 State로 계산 가능하면 렌더링 중 계산하는 것이 좋다.

Q. Derived State를 잘못 쓰면 어떤 문제가 생겨?

A.
원본 값과 파생 값이 서로 불일치하는 버그가 생길 수 있다.

---

# 9. Event Handling Rules

## 9.1 React Event Handling

### [개념]

React Event Handling은 사용자 행동에 반응해 함수를 실행하는 방식이다.

예:

```jsx
function SearchButton({ onSearch }) {
  return (
    <button type="button" onClick={onSearch}>
      Search
    </button>
  );
}
```

---

### [핵심]

필수 포함:

- onClick
- onChange
- onSubmit
- onKeyDown
- event object
- preventDefault
- handler function
- callback props
- React Synthetic Event basics

---

### [실무]

Click Event:

```jsx
function Counter() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount((prevCount) => prevCount + 1);
  }

  return (
    <button type="button" onClick={handleClick}>
      {count}
    </button>
  );
}
```

Form Submit:

```jsx
function SearchForm() {
  function handleSubmit(event) {
    event.preventDefault();
  }

  return (
    <form onSubmit={handleSubmit}>
      <button type="submit">Search</button>
    </form>
  );
}
```

주의:

- `onClick={handleClick}`처럼 함수 참조 전달
- `onClick={handleClick()}`는 즉시 실행되므로 주의
- form submit에는 preventDefault 고려
- handler 이름은 `handle` prefix 권장
- props callback은 `on` prefix 권장

---

### [FAQ]

Q. onClick={handleClick()}가 왜 문제야?

A.
렌더링 중 함수가 즉시 실행된다. 클릭 시 실행하려면 `onClick={handleClick}`처럼 함수 참조를 전달해야 한다.

Q. React에서 event.preventDefault는 언제 써?

A.
form 제출 시 페이지 새로고침 같은 기본 동작을 막을 때 사용한다.

Q. handler 이름은 어떻게 짓는 게 좋아?

A.
Component 내부 함수는 handleSubmit, handleClick처럼 짓고 props callback은 onSubmit, onClick처럼 짓는 방식이 흔하다.

---

## 9.2 Controlled Input Rules

### [개념]

Controlled Input은 input value를 React State로 제어하는 방식이다.

예:

```jsx
function SearchInput() {
  const [keyword, setKeyword] = useState("");

  return (
    <input
      value={keyword}
      onChange={(event) => setKeyword(event.target.value)}
    />
  );
}
```

---

### [핵심]

필수 포함:

- value
- onChange
- state
- controlled component
- input value
- form state
- validation
- reset

---

### [실무]

Form Flow:

```text
User Input
→ onChange
→ setState
→ Re-render
→ input value update
```

예:

```jsx
function SearchForm() {
  const [keyword, setKeyword] = useState("");

  function handleSubmit(event) {
    event.preventDefault();

    const trimmedKeyword = keyword.trim();
    if (!trimmedKeyword) {
      return;
    }

    console.log(trimmedKeyword);
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={keyword}
        onChange={(event) => setKeyword(event.target.value)}
      />
      <button type="submit">Search</button>
    </form>
  );
}
```

주의:

- value만 있고 onChange가 없으면 읽기 전용처럼 동작
- 초기값은 빈 문자열 권장
- validation과 submit 분리
- 복잡한 Form은 별도 Form Handling 문서에서 다룸

---

### [FAQ]

Q. Controlled Input이 뭐야?

A.
input 값을 DOM이 아니라 React State로 관리하는 방식이다.

Q. input에 value만 넣고 onChange를 안 넣으면?

A.
사용자가 값을 변경할 수 없는 읽기 전용 input처럼 동작할 수 있다.

Q. Form 입력값 검증은 어디서 해?

A.
기본 검증은 submit handler 또는 별도 validation 함수에서 처리한다.

---

# 10. Rendering Rules

## 10.1 Conditional Rendering Rules

### [개념]

Conditional Rendering은 조건에 따라 다른 UI를 렌더링하는 방식이다.

---

### [핵심]

필수 포함:

- if outside JSX
- ternary operator
- logical AND
- early return
- null return
- loading state
- error state
- empty state

---

### [실무]

Early Return 예:

```jsx
function FestivalList({ loading, error, festivals }) {
  if (loading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>Failed to load festivals.</p>;
  }

  if (festivals.length === 0) {
    return <p>No festivals found.</p>;
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

삼항 연산자 예:

```jsx
{
  isLoggedIn ? <Profile /> : <LoginButton />;
}
```

주의:

- 복잡한 조건은 JSX 밖에서 분리
- `0 && <Component />` 렌더링 주의
- loading / error / empty / success 상태 분리
- 조건이 많으면 함수 또는 Component 분리

---

### [FAQ]

Q. React에서 if문은 어디에 써?

A.
JSX 내부에 직접 쓰지 않고 return 전에 early return하거나 변수로 계산해 사용한다.

Q. && 조건부 렌더링은 언제 조심해야 해?

A.
왼쪽 값이 0이면 0이 화면에 렌더링될 수 있어 주의해야 한다.

Q. loading, error, empty 상태를 분리해야 해?

A.
분리하는 것이 좋다. 비동기 UI 상태를 명확하게 관리할 수 있다.

---

## 10.2 List Rendering Rules

### [개념]

List Rendering은 배열 데이터를 JSX 목록으로 변환해 렌더링하는 방식이다.

예:

```jsx
function FestivalList({ festivals }) {
  return (
    <ul>
      {festivals.map((festival) => (
        <li key={festival.id}>{festival.title}</li>
      ))}
    </ul>
  );
}
```

---

### [핵심]

필수 포함:

- Array map
- key
- stable id
- list item component
- empty list
- filter before map
- sort copy before map

---

### [실무]

권장:

```jsx
function FestivalList({ festivals }) {
  if (festivals.length === 0) {
    return <p>No festivals found.</p>;
  }

  return (
    <section className="festival-list">
      {festivals.map((festival) => (
        <FestivalCard
          key={festival.festivalId}
          title={festival.title}
          imageUrl={festival.imageUrl}
        />
      ))}
    </section>
  );
}
```

주의:

- key는 안정적인 고유 ID 사용
- index key는 목록 순서 변경 시 문제 가능
- map callback에는 JSX 반환 필요
- 빈 목록 UI 제공
- sort는 원본 배열 변경 주의
- filter / map 로직이 복잡하면 변수 분리

---

### [FAQ]

Q. React list에서 key는 왜 필요해?

A.
React가 목록 item의 추가, 삭제, 변경을 효율적으로 추적하기 위해 필요하다.

Q. index를 key로 써도 돼?

A.
정적인 목록은 가능하지만 추가, 삭제, 정렬이 있는 목록에서는 안정적인 ID를 사용하는 것이 좋다.

Q. map 안에서 중괄호를 쓰면 return이 필요한 이유는?

A.
화살표 함수에서 `{}`를 사용하면 block body가 되므로 명시적으로 return해야 한다.

---

## 10.3 Rendering Flow Rules

### [개념]

React Rendering Flow는 State 또는 Props 변화에 따라 Component 함수가 다시 실행되고 JSX 결과가 갱신되는 흐름이다.

---

### [핵심]

Flow:

```text
Initial Render
→ User Event
→ State Update
→ Re-render
→ JSX Recalculation
→ DOM Update
```

반드시 설명:

- Component 함수는 렌더링마다 다시 실행
- State 변경은 Re-render 유발
- Props 변경도 Child Re-render 가능
- 렌더링은 UI 결과 계산 과정
- 렌더링 중 State 변경 금지
- Side Effect는 useEffect에서 처리

---

### [실무]

주의:

```jsx
function BadComponent() {
  const [count, setCount] = useState(0);

  setCount(count + 1);

  return <p>{count}</p>;
}
```

문제:

- 렌더링 중 State 변경
- 무한 렌더링 발생 가능

개선:

```jsx
function GoodComponent() {
  const [count, setCount] = useState(0);

  return (
    <button type="button" onClick={() => setCount(count + 1)}>
      {count}
    </button>
  );
}
```

---

### [FAQ]

Q. Component 함수는 언제 실행돼?

A.
초기 렌더링과 State 또는 Props 변경으로 다시 렌더링될 때 실행된다.

Q. 렌더링 중 setState를 호출하면 왜 문제야?

A.
State 변경이 다시 렌더링을 유발해 무한 렌더링이 발생할 수 있다.

Q. Side Effect는 어디서 처리해?

A.
외부 시스템과 동기화가 필요한 작업은 useEffect에서 처리한다.

---

# 11. Hook Rules

## 11.1 Hook Basics

### [개념]

Hook은 Functional Component에서 React 기능을 사용할 수 있게 해주는 함수다.

대표 Hook:

- useState
- useEffect
- useRef
- useMemo
- useCallback
- useContext

React Core에서는 useState와 useEffect를 중심으로 다룬다.

---

### [핵심]

Hook 규칙:

- Component 최상위에서 호출
- 조건문 내부에서 호출 금지
- 반복문 내부에서 호출 금지
- 일반 함수에서 호출 금지
- Custom Hook은 이름이 use로 시작
- Hook 호출 순서가 렌더링마다 같아야 함

---

### [실무]

나쁜 예:

```jsx
function Component({ enabled }) {
  if (enabled) {
    const [count, setCount] = useState(0);
  }

  return null;
}
```

좋은 예:

```jsx
function Component({ enabled }) {
  const [count, setCount] = useState(0);

  if (!enabled) {
    return null;
  }

  return <p>{count}</p>;
}
```

---

### [FAQ]

Q. Hook은 왜 조건문 안에서 호출하면 안 돼?

A.
React는 Hook 호출 순서로 상태를 관리한다. 조건에 따라 호출 순서가 바뀌면 상태 연결이 깨질 수 있다.

Q. Hook은 일반 함수에서 호출해도 돼?

A.
안 된다. React Component 또는 Custom Hook 내부에서 호출해야 한다.

Q. Custom Hook 이름은 왜 use로 시작해야 해?

A.
React와 lint 도구가 Hook 규칙을 검사할 수 있게 하기 위해서다.

---

## 11.2 useEffect Rules

### [개념]

useEffect는 Component가 렌더링된 후 외부 시스템과 동기화할 때 사용하는 Hook이다.

외부 시스템 예:

- API Request
- Browser Event
- Timer
- Subscription
- localStorage
- document title

---

### [핵심]

필수 포함:

- effect callback
- dependency array
- cleanup function
- external system synchronization
- API call basics
- timer cleanup
- event listener cleanup
- infinite loop caution

예:

```jsx
useEffect(() => {
  document.title = "Festival List";
}, []);
```

---

### [실무]

API 호출 예:

```jsx
function FestivalPage() {
  const [festivals, setFestivals] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    async function loadFestivals() {
      setLoading(true);

      try {
        const response = await fetch("/api/festivals");
        const data = await response.json();
        setFestivals(data);
      } finally {
        setLoading(false);
      }
    }

    loadFestivals();
  }, []);

  return null;
}
```

주의:

- useEffect는 모든 로직을 넣는 곳이 아님
- Event Handler에서 처리할 수 있는 것은 Event Handler에서 처리
- dependency array 누락 시 매 렌더링 실행
- State를 dependency로 넣고 effect 안에서 같은 State를 변경하면 무한 루프 가능
- cleanup 필요한 effect는 cleanup return
- API 호출 심화는 Data Fetching 문서에서 다룸

---

### [FAQ]

Q. useEffect는 언제 써?

A.
Component가 렌더링된 후 외부 시스템과 동기화해야 할 때 사용한다.

Q. useEffect dependency array가 비어 있으면?

A.
Component mount 후 한 번 실행되는 패턴으로 사용된다.

Q. useEffect에 dependency array를 안 쓰면?

A.
렌더링될 때마다 effect가 실행된다.

Q. useEffect에서 무한 루프가 나는 이유는?

A.
effect가 State를 변경하고 그 State가 dependency에 있어 다시 effect가 실행되는 구조일 수 있다.

---

## 11.3 Cleanup Function Rules

### [개념]

Cleanup Function은 useEffect에서 등록한 외부 작업을 정리하는 함수다.

예:

```jsx
useEffect(() => {
  const timerId = setInterval(() => {
    console.log("tick");
  }, 1000);

  return () => {
    clearInterval(timerId);
  };
}, []);
```

---

### [핵심]

Cleanup 필요 상황:

- timer
- interval
- event listener
- subscription
- websocket connection
- abort controller
- external resource

---

### [실무]

Event Listener Cleanup 예:

```jsx
useEffect(() => {
  function handleResize() {
    console.log(window.innerWidth);
  }

  window.addEventListener("resize", handleResize);

  return () => {
    window.removeEventListener("resize", handleResize);
  };
}, []);
```

주의:

- cleanup 누락 시 memory leak 가능
- 같은 handler reference로 remove 필요
- Component unmount 시 정리
- dependency 변경 전 이전 effect 정리

---

### [FAQ]

Q. useEffect cleanup은 왜 필요해?

A.
Timer, Event Listener, Subscription 같은 외부 작업이 남아 memory leak이나 중복 실행을 만들 수 있기 때문이다.

Q. cleanup은 언제 실행돼?

A.
Component unmount 시 또는 dependency 변경으로 effect가 다시 실행되기 전에 실행된다.

---

# 12. API Call Basic Rules

## 12.1 API Call in React Core

### [개념]

React에서 API Call은 서버 데이터를 가져와 State에 저장하고 UI로 렌더링하는 흐름이다.

React Core에서는 Fetch API + useEffect + useState 기본 패턴을 다룬다.

---

### [핵심]

필수 포함:

- fetch
- useEffect
- useState
- loading state
- error state
- data state
- empty state
- response.ok
- cleanup / abort basics
- API function separation basics

---

### [실무]

기본 Flow:

```text
Component Mount
→ useEffect
→ API Request
→ Loading State
→ Success: setData
→ Error: setError
→ Finally: setLoading(false)
→ Render by State
```

예:

```jsx
function FestivalPage() {
  const [festivals, setFestivals] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function loadFestivals() {
      setLoading(true);
      setError(null);

      try {
        const response = await fetch("/api/festivals");

        if (!response.ok) {
          throw new Error("Failed to load festivals");
        }

        const data = await response.json();
        setFestivals(data);
      } catch (error) {
        setError(error);
      } finally {
        setLoading(false);
      }
    }

    loadFestivals();
  }, []);

  if (loading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>Failed to load festivals.</p>;
  }

  if (festivals.length === 0) {
    return <p>No festivals found.</p>;
  }

  return <FestivalList festivals={festivals} />;
}
```

주의:

- fetch는 HTTP 오류를 자동 throw하지 않음
- response.ok 확인
- loading / error / empty 상태 분리
- Component 내부 API 로직이 길면 api 파일로 분리
- Data Fetching 심화는 별도 문서에서 다룸

---

### [FAQ]

Q. React에서 API 호출은 어디서 해?

A.
초기 데이터 로딩은 보통 useEffect에서 처리한다. 사용자 이벤트로 발생하는 요청은 Event Handler에서 처리한다.

Q. API 호출 상태는 어떤 State로 나눠?

A.
data, loading, error, empty 상태를 분리하는 것이 좋다.

Q. fetch 실패 처리는 어떻게 해?

A.
response.ok를 확인하고 실패 시 error state를 설정해 사용자에게 안내한다.

---

# 13. React TypeScript Rules

## 13.1 React TypeScript Basics

### [개념]

React TypeScript는 React Component, Props, State, Event Handler에 TypeScript 타입을 적용하는 방식이다.

---

### [핵심]

필수 포함:

- Props Type
- State Type
- Event Type
- ReactNode
- ChangeEvent
- FormEvent
- MouseEvent
- nullable state
- array state
- callback props

---

### [실무]

Props Type 예:

```tsx
type FestivalCardProps = {
  title: string;
  imageUrl: string | null;
  onClick: () => void;
};

function FestivalCard({ title, imageUrl, onClick }: FestivalCardProps) {
  return (
    <article onClick={onClick}>
      <h2>{title}</h2>
      {imageUrl && <img src={imageUrl} alt={title} />}
    </article>
  );
}
```

Input Event 예:

```tsx
import type { ChangeEvent } from "react";

function handleChange(event: ChangeEvent<HTMLInputElement>): void {
  console.log(event.target.value);
}
```

State Type 예:

```tsx
type Festival = {
  festivalId: number;
  title: string;
};

const [festivals, setFestivals] = useState<Festival[]>([]);
```

주의:

- 빈 배열 State는 Generic으로 타입 명시
- null 초기값은 Union Type 사용
- Event Type은 target element와 함께 작성
- Props Type은 Component와 가까운 위치 또는 shared type 파일에 작성
- React TypeScript 심화는 별도 문서에서 다룸

---

### [FAQ]

Q. React Props Type은 어떻게 정의해?

A.
type 또는 interface로 Props 구조를 정의하고 Component parameter에 적용한다.

Q. useState 빈 배열 타입은 어떻게 써?

A.
`useState<Festival[]>([])`처럼 Generic으로 요소 타입을 명시한다.

Q. input onChange 타입은 뭐야?

A.
일반적으로 `ChangeEvent<HTMLInputElement>`를 사용한다.

---

# 14. File Structure Rules

## 14.1 React Basic File Structure

### [개념]

React File Structure는 Component, Page, API, Utility 파일을 역할별로 분리하는 구조다.

---

### [핵심]

필수 포함:

- components
- pages
- api
- hooks basics
- utils
- types
- styles
- assets
- index file caution

---

### [실무]

기본 구조 예:

```text
src
├ components
│  ├ FestivalCard.jsx
│  └ FestivalList.jsx
├ pages
│  └ FestivalPage.jsx
├ api
│  └ festivalApi.js
├ utils
│  └ dateUtils.js
├ types
│  └ festival.ts
└ styles
   └ global.css
```

역할 기준:

- components: 재사용 UI Component
- pages: 화면 단위 Component
- api: API 요청 함수
- utils: 순수 유틸 함수
- types: 공통 TypeScript Type
- styles: 공통 스타일

주의:

- 모든 코드를 App.jsx에 몰아넣지 않음
- Component가 커지면 분리
- API 요청 함수는 분리 가능
- 파일명은 Component 이름과 일치 권장
- 프로젝트 컨벤션 우선

---

### [FAQ]

Q. Component 파일은 어디에 둬?

A.
재사용 Component는 components 폴더, 화면 단위 Component는 pages 폴더에 두는 방식이 일반적이다.

Q. API 호출 함수는 Component 안에 둬도 돼?

A.
간단한 예제는 가능하지만 재사용되거나 복잡하면 api 파일로 분리하는 것이 좋다.

Q. App.jsx에 모든 코드를 넣어도 돼?

A.
작은 실습은 가능하지만 실무 프로젝트에서는 역할별 파일 분리가 필요하다.

---

# 15. Debugging Rules

## 15.1 React Debugging

### [개념]

React Debugging은 Component 렌더링, Props, State, Event, API 요청 흐름을 확인하는 과정이다.

---

### [핵심]

필수 포함:

- React DevTools
- Browser Console
- Network Tab
- Props Check
- State Check
- Component Tree
- Event Handler Check
- Rendering Count
- Error Boundary mention
- StrictMode double render caution

---

### [실무]

Debug Flow:

```text
UI Problem
→ Console Error Check
→ Component Tree Check
→ Props Check
→ State Check
→ Event Handler Check
→ Network Request Check
→ Render Condition Check
→ Fix Component Logic
```

API UI Debug Flow:

```text
Button Click or Mount
→ Event / useEffect Trigger
→ Network Request
→ Response Body
→ setState
→ Re-render
→ Conditional UI Check
```

주의:

- Console Error 먼저 확인
- React DevTools로 Props / State 확인
- Network 탭으로 API 응답 확인
- StrictMode에서 개발 중 effect가 두 번 실행될 수 있음
- 렌더링 중 State 변경 여부 확인

---

### [FAQ]

Q. React State 값은 어디서 확인해?

A.
React DevTools에서 Component를 선택해 State와 Props를 확인할 수 있다.

Q. React 화면이 안 바뀌면 뭘 확인해?

A.
State가 setter로 변경되는지, Props가 전달되는지, 조건부 렌더링 조건이 맞는지 확인한다.

Q. 개발 중 useEffect가 두 번 실행되는 것처럼 보여?

A.
React StrictMode에서 개발 중 부작용 검사를 위해 effect가 추가 실행될 수 있다.

---

# 16. Code Example Rules

## 16.1 Example Style

### [개념]

React Core 예제는 짧고 직접적이어야 한다.

목적:

- Retrieval
- Code Generation
- Review
- Debugging
- React Component 생성 지원

---

### [핵심]

권장:

- Functional Component 기준
- JSX 핵심 구조만 포함
- Props / State 명확화
- Event Handler 포함
- loading / error / empty 예제 포함
- key 포함
- useEffect dependency 포함
- TypeScript 예제는 필요한 경우만 포함

금지:

- Class Component 중심 예제
- 긴 전체 프로젝트 코드
- 불필요한 boilerplate
- jQuery / DOM 직접 조작 예제
- setState 직접 mutation 예제
- key 없는 list 예제
- dependency 없는 useEffect 남용 예제
- API Key 하드코딩 예제

---

### [실무]

좋은 예:

```jsx
function FestivalCard({ festival, onSelect }) {
  return (
    <article className="festival-card">
      <h2>{festival.title}</h2>
      <p>{festival.region}</p>
      <button type="button" onClick={() => onSelect(festival.festivalId)}>
        Detail
      </button>
    </article>
  );
}
```

좋은 목록 예:

```jsx
function FestivalList({ festivals }) {
  if (festivals.length === 0) {
    return <p>No festivals found.</p>;
  }

  return (
    <section>
      {festivals.map((festival) => (
        <FestivalCard
          key={festival.festivalId}
          festival={festival}
          onSelect={(festivalId) => console.log(festivalId)}
        />
      ))}
    </section>
  );
}
```

---

### [FAQ]

Q. React 예제 코드는 길수록 좋아?

A.
아니다. RAG 문서에서는 짧고 검색 가능한 실무 예제가 더 좋다.

Q. React 예제에 key를 꼭 넣어야 해?

A.
목록 렌더링 예제에는 반드시 안정적인 key를 포함한다.

---

# 17. Troubleshooting Rules

## 17.1 Infinite Render Problem

### [개념]

Infinite Render Problem은 Component가 계속 다시 렌더링되는 문제다.

---

### [핵심]

문제:

- Too many re-renders 오류
- 화면 멈춤
- Console 오류 반복
- useEffect 반복 실행

원인:

- 렌더링 중 setState 호출
- onClick에 함수 실행 결과 전달
- useEffect dependency 문제
- effect 안에서 dependency state 계속 변경
- props 변경과 state 변경 순환

해결:

- setState를 Event Handler 또는 useEffect 내부로 이동
- onClick에는 함수 참조 전달
- dependency array 확인
- 상태 변경 조건 추가
- derived state 제거 검토

---

### [실무]

나쁜 예:

```jsx
function BadButton() {
  const [count, setCount] = useState(0);

  return (
    <button type="button" onClick={setCount(count + 1)}>
      {count}
    </button>
  );
}
```

좋은 예:

```jsx
function GoodButton() {
  const [count, setCount] = useState(0);

  return (
    <button type="button" onClick={() => setCount(count + 1)}>
      {count}
    </button>
  );
}
```

Debug Flow:

```text
Error Message Check
→ setState Location Check
→ Event Handler Check
→ useEffect Dependency Check
→ State Update Condition Check
```

---

### [FAQ]

Q. Too many re-renders 오류는 왜 나?

A.
렌더링 중 State를 변경하거나 Event Handler를 잘못 전달해 렌더링마다 setState가 호출될 때 발생한다.

Q. onClick에서 setState를 바로 쓰면 안 돼?

A.
`onClick={setCount(count + 1)}`는 렌더링 중 실행된다. `onClick={() => setCount(count + 1)}`처럼 함수로 감싸야 한다.

---

## 17.2 State Mutation Problem

### [개념]

State Mutation Problem은 State 객체나 배열을 직접 수정해서 React가 변경을 올바르게 감지하지 못하는 문제다.

---

### [핵심]

문제:

- 화면이 업데이트되지 않음
- 값은 바뀐 것 같은데 Re-render 안 됨
- 이전 State가 예상과 다름
- 목록 추가 / 삭제 UI 오류

원인:

- 배열 push 사용
- 객체 property 직접 변경
- sort로 원본 배열 변경
- splice로 원본 배열 변경
- nested object 직접 수정

해결:

- 새 배열 생성
- 새 객체 생성
- spread 사용
- map / filter 사용
- 원본 복사 후 sort
- immutable update 적용

---

### [실무]

나쁜 예:

```jsx
festivals.push(newFestival);
setFestivals(festivals);
```

좋은 예:

```jsx
setFestivals((prevFestivals) => [...prevFestivals, newFestival]);
```

객체 업데이트:

```jsx
setUser((prevUser) => ({
  ...prevUser,
  name: "newName",
}));
```

---

### [FAQ]

Q. 배열 State에 push를 쓰면 안 돼?

A.
안 된다. 기존 배열을 직접 수정하지 말고 새 배열을 만들어 setter에 전달해야 한다.

Q. 객체 State는 어떻게 수정해?

A.
기존 객체를 직접 수정하지 말고 spread로 새 객체를 만들어 수정한다.

---

## 17.3 Key Warning

### [개념]

Key Warning은 React 목록 렌더링에서 각 item을 구분할 key가 없거나 부적절할 때 발생하는 경고다.

---

### [핵심]

문제:

- Each child in a list should have a unique key prop
- 목록 UI가 이상하게 갱신됨
- input 값이 다른 item에 남음
- item 순서 변경 시 오류

원인:

- key 누락
- 중복 key 사용
- index key 사용
- 불안정한 random key 사용

해결:

- 서버 ID 사용
- 고유한 stable key 사용
- index key 지양
- random key 금지
- key는 최상위 반복 요소에 부여

---

### [실무]

나쁜 예:

```jsx
{
  festivals.map((festival) => <FestivalCard festival={festival} />);
}
```

좋은 예:

```jsx
{
  festivals.map((festival) => (
    <FestivalCard key={festival.festivalId} festival={festival} />
  ));
}
```

주의:

- key는 props로 자동 전달되지 않음
- Component 내부에서 key 값을 쓰려면 별도 prop으로 전달
- `key={Math.random()}` 금지

---

### [FAQ]

Q. React key warning은 왜 나?

A.
목록 item을 구분할 고유 key가 없거나 중복되었기 때문이다.

Q. key에 Math.random을 쓰면 안 돼?

A.
안 된다. 매 렌더링마다 key가 바뀌어 React가 item을 안정적으로 추적할 수 없다.

Q. key는 Component 안에서 props로 받을 수 있어?

A.
아니다. key는 React 내부에서 사용하는 특수 값이다. 필요하면 별도 prop으로 전달해야 한다.

---

## 17.4 useEffect Dependency Problem

### [개념]

useEffect Dependency Problem은 dependency array가 잘못되어 effect가 너무 자주 실행되거나 필요한 시점에 실행되지 않는 문제다.

---

### [핵심]

문제:

- useEffect가 계속 실행됨
- API가 반복 호출됨
- 최신 State를 못 읽음
- dependency lint 경고 발생
- 화면 데이터가 갱신되지 않음

원인:

- dependency 누락
- dependency 과다 추가
- effect 안에서 dependency state 변경
- 매 렌더링마다 새 객체 / 함수 생성
- event 로직을 effect에 넣음

해결:

- effect 목적 재검토
- 필요한 dependency 명시
- event 로직은 handler로 이동
- derived value는 렌더링 중 계산
- API 호출 조건 분리
- cleanup 추가

---

### [실무]

Debug Flow:

```text
Effect Purpose Check
→ Dependency List Check
→ State Update Inside Effect Check
→ External System Sync 여부 확인
→ Event Handler로 이동 가능 여부 확인
```

주의:

- dependency 경고를 무조건 무시하지 않음
- eslint-disable 남용 금지
- useEffect는 데이터 흐름 우회 도구가 아님
- 외부 시스템 동기화 목적 중심으로 사용

---

### [FAQ]

Q. useEffect dependency 경고는 무시해도 돼?

A.
대부분 무시하지 않는 것이 좋다. effect가 참조하는 값과 실행 조건을 다시 검토해야 한다.

Q. useEffect에서 API가 계속 호출되는 이유는?

A.
dependency가 매 렌더링마다 바뀌거나 effect 내부 State 변경이 dependency와 연결되어 있을 수 있다.

---

# 18. Comparison Rules

## 18.1 Required Comparisons

### [개념]

React Core 문서는 헷갈리는 개념을 비교해서 작성한다.

---

### [핵심]

필수 비교 대상:

- Component vs Element
- Props vs State
- Controlled vs Uncontrolled Input
- useState vs useEffect
- Event Handler vs useEffect
- Conditional Rendering vs CSS Hide
- map Rendering vs Manual Repetition
- key id vs index key
- State vs Derived Value
- JSX vs HTML
- className vs class
- React Fragment vs div
- Parent Component vs Child Component
- Page Component vs UI Component

---

### [실무]

예시:

| 비교      | Props                 | State                       |
| --------- | --------------------- | --------------------------- |
| 소유      | 부모 Component        | 현재 Component              |
| 변경      | 자식이 직접 변경 금지 | setter로 변경               |
| 용도      | 외부 데이터 전달      | 내부 UI 상태                |
| 변경 결과 | Child Re-render 가능  | Current Component Re-render |

---

### [FAQ]

Q. 비교 표는 왜 필요해?

A.
사용자가 자주 헷갈리는 질문에서 Retrieval Hit와 답변 정확도를 높이기 위해 필요하다.

Q. React 비교 문서에서 가장 중요한 것은?

A.
실무 선택 기준과 오류 가능성을 함께 설명하는 것이다.

---

# 19. Checklist Rules

## 19.1 Document Quality Checklist

### [개념]

React Core 문서 검수 시 품질 체크리스트를 사용한다.

---

### [핵심]

Checklist:

```md
- [ ] React 기본 개념이 포함되었는가?
- [ ] Component 설명이 포함되었는가?
- [ ] JSX 규칙이 포함되었는가?
- [ ] Props / State 차이가 포함되었는가?
- [ ] Event Handling 예제가 포함되었는가?
- [ ] Controlled Input 기초가 포함되었는가?
- [ ] Conditional Rendering이 포함되었는가?
- [ ] List Rendering과 key 설명이 포함되었는가?
- [ ] Hook 규칙이 포함되었는가?
- [ ] useState 예제가 포함되었는가?
- [ ] useEffect와 dependency 설명이 포함되었는가?
- [ ] API Call 기본 패턴이 포함되었는가?
- [ ] React TypeScript 연결 기초가 포함되었는가?
- [ ] Troubleshooting이 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 기준:

```text
Draft
→ Required Section Check
→ Component Example Check
→ Props / State Check
→ Hook Rule Check
→ Rendering Flow Check
→ Troubleshooting Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

---

### [FAQ]

Q. React Core 문서 검수에서 가장 중요한 것은?

A.
Component, JSX, Props, State, Event, List Rendering, useState, useEffect, FAQ, Retrieval Queries 포함 여부다.

---

# 20. Retrieval Optimization Rules

## 20.1 Keyword Rules

### [개념]

React Core 문서는 검색 매칭을 위해 핵심 키워드를 반복 허용한다.

---

### [핵심]

강조 키워드:

- React
- React Core
- React Component
- Functional Component
- JSX
- JSX Expression
- className
- Fragment
- Props
- Props Destructuring
- children
- State
- useState
- setState
- Event Handling
- onClick
- onChange
- onSubmit
- Controlled Input
- Conditional Rendering
- List Rendering
- key
- Hook
- useEffect
- Dependency Array
- Cleanup Function
- Re-render
- Rendering Flow
- API Call
- Loading State
- Error State
- Empty State
- React TypeScript
- React DevTools
- React Debugging
- Infinite Render
- State Mutation
- Key Warning

---

### [실무]

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

예:

- React Component가 뭐야?
- JSX는 HTML이야?
- Props와 State 차이는?
- useState는 언제 써?
- setState 직후 값이 안 바뀌는 이유는?
- React에서 배열 State는 어떻게 수정해?
- React에서 이벤트 처리는 어떻게 해?
- onClick에서 함수가 바로 실행되는 이유는?
- Controlled Input이 뭐야?
- 조건부 렌더링 어떻게 해?
- map 렌더링에서 key는 왜 필요해?
- useEffect는 언제 써?
- useEffect 무한 실행 이유는?
- React에서 API 호출은 어디서 해?
- Too many re-renders 오류는 왜 나?
- React 화면이 안 바뀌는 이유는?

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

## 21.1 Modern React 기준

### [개념]

React Core 문서는 Modern React 기준으로 작성한다.

---

### [핵심]

기준:

- React 18+
- React 19 호환 기준 고려
- Functional Component
- Hook
- JSX Transform
- ES Module
- TypeScript Ready
- StrictMode 고려
- Component Composition
- State-driven UI
- Declarative UI

Legacy 제외:

- Class Component 중심 설명
- lifecycle method 중심 설명
- jQuery DOM 조작
- createClass
- mixin
- string ref
- legacy context 중심 설명
- componentWillMount 중심 설명
- 불필요한 React.FC 강제

---

### [실무]

실무 기준:

```text
Modern React
→ Functional Component
→ Props / State
→ Hook
→ State-driven Rendering
→ Component Composition
→ TypeScript Ready Component
```

---

### [FAQ]

Q. React class component도 배워야 해?

A.
기존 코드 유지보수에서는 볼 수 있지만 신규 문서는 Functional Component와 Hook 중심으로 작성한다.

Q. React.FC를 꼭 써야 해?

A.
필수는 아니다. 프로젝트 컨벤션에 따라 사용 여부를 결정한다.

---

# 22. Common Mistakes

## 22.1 React Common Mistakes

### [개념]

React Core 문서는 자주 발생하는 실수를 명확히 포함해야 한다.

---

### [핵심]

자주 발생:

- Component 이름 소문자로 작성
- JSX에서 class 사용
- JSX 내부에 if statement 직접 작성
- 객체를 React child로 직접 렌더링
- Props 직접 수정
- State 직접 변경
- 배열 State에 push 사용
- 객체 State property 직접 수정
- setState 직후 값이 즉시 바뀐다고 오해
- 렌더링 중 setState 호출
- onClick에 함수 실행 결과 전달
- key 누락
- index key 남용
- key에 Math.random 사용
- useEffect dependency 누락
- useEffect 무한 루프
- cleanup 누락
- input value만 있고 onChange 누락
- loading / error / empty 상태 누락
- API response.ok 확인 누락
- 모든 코드를 App.jsx에 작성

---

### [실무]

문서 작성 시 Common Mistakes는 Troubleshooting과 연결한다.

예:

```text
문제: Too many re-renders
원인: 렌더링 중 setState 호출
해결: setState를 Event Handler 또는 useEffect 내부 조건부 로직으로 이동
```

---

### [FAQ]

Q. React 초보가 가장 많이 하는 실수는?

A.
State 직접 변경, key 누락, onClick 즉시 실행, useEffect dependency 문제, Props와 State 혼동이 많다.

Q. React 오류는 어떻게 찾는 게 좋아?

A.
Console Error, React DevTools의 Props / State, Network 요청, 렌더링 조건, useEffect 실행 조건을 순서대로 확인한다.

---

# 23. Final Goal

## 23.1 Domain Final Goal

### [개념]

React Core RAG 문서는 Frontend Agent가 기본 React 화면과 Component 로직을 안정적으로 생성하고 검토하도록 지원해야 한다.

---

### [핵심]

최종 목표:

- React 기본 개념 이해
- Component 작성
- Functional Component 작성
- JSX 작성
- Props 전달 구조 작성
- children 사용
- State 정의
- useState 사용
- Event Handler 작성
- Controlled Input 작성
- Conditional Rendering 구현
- List Rendering 구현
- key 적용
- Hook 기본 규칙 이해
- useEffect 사용
- dependency array 이해
- cleanup function 작성
- API Call 기본 패턴 작성
- loading / error / empty UI 구성
- React TypeScript 기초 연결
- React Debugging 수행
- React Common Mistakes 검토

---

### [실무]

Agent 수행 가능 작업:

```text
User Frontend Request
→ React Component Structure
→ Props Definition
→ State Definition
→ Event Handling
→ Conditional Rendering
→ List Rendering
→ useEffect / API Basic Flow
→ Debugging Review
→ React Core Output
```

---

### [FAQ]

Q. React Core 문서의 최종 목적은 뭐야?

A.
Frontend Agent가 React Component, Props, State, Event, Rendering, useState, useEffect 기반의 기본 화면을 안정적으로 생성하고 검토하게 만드는 것이다.

Q. 이 문서 다음에는 어떤 Domain Rules가 이어져야 해?

A.
React Component Design, React Router, State Management, Data Fetching & REST API Integration 순서로 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. React Core 문서는 왜 필요해?
A. Frontend Agent가 React 화면을 만들기 전에 Component, JSX, Props, State, Event, Hook 기본 구조를 이해해야 하기 때문이다.

Q. React는 뭐야?
A. React는 Component 기반으로 사용자 인터페이스를 만들기 위한 JavaScript UI Library다.

Q. React는 Framework야 Library야?
A. React 자체는 UI Library다. Router, 상태관리, 데이터 패칭 등을 함께 사용하면 Framework처럼 구성할 수 있다.

Q. React Component가 뭐야?
A. Component는 React UI를 구성하는 재사용 가능한 단위다.

Q. Component 이름은 왜 대문자로 시작해?
A. React가 소문자는 HTML 태그로 보고 대문자로 시작하는 이름을 Component로 인식하기 때문이다.

Q. Functional Component가 뭐야?
A. 함수로 작성하는 React Component다. 현대 React에서는 Functional Component와 Hook을 기본으로 사용한다.

Q. React에서 class component를 써야 해?
A. 신규 코드에서는 Functional Component와 Hook을 기준으로 작성한다.

Q. JSX는 HTML이야?
A. 아니다. JSX는 JavaScript 안에서 UI 구조를 표현하는 문법이며 React가 처리한다.

Q. JSX에서 class 대신 className을 쓰는 이유는?
A. class는 JavaScript 예약어와 충돌 가능성이 있어 React JSX에서는 className을 사용한다.

Q. JSX에서 if문을 바로 쓸 수 있어?
A. JSX 내부에는 statement를 직접 쓸 수 없다. 조건부 렌더링은 삼항 연산자, &&, early return 등을 사용한다.

Q. JSX 중괄호 안에는 뭘 넣을 수 있어?
A. 변수, 함수 호출, 삼항 연산자, 논리식, map 결과 같은 JavaScript expression을 넣을 수 있다.

Q. JSX 중괄호 안에 객체를 넣어도 돼?
A. 객체 자체는 React child로 렌더링할 수 없다. 객체의 문자열 property 등을 렌더링해야 한다.

Q. Fragment는 왜 써?
A. 불필요한 DOM 요소를 추가하지 않고 여러 JSX 요소를 묶기 위해 사용한다.

Q. Props가 뭐야?
A. Props는 부모 Component가 자식 Component에 전달하는 읽기 전용 데이터다.

Q. Props는 수정해도 돼?
A. 안 된다. Props는 읽기 전용이다. 변경이 필요하면 부모 State를 변경하는 callback을 전달한다.

Q. Props는 어느 방향으로 전달돼?
A. 부모 Component에서 자식 Component로 전달된다.

Q. Props로 함수도 전달할 수 있어?
A. 가능하다. 자식에서 발생한 이벤트를 부모에게 알릴 때 callback props를 자주 사용한다.

Q. Props Destructuring은 왜 써?
A. props.title처럼 반복 접근하지 않고 필요한 값을 명확하게 사용할 수 있기 때문이다.

Q. children은 언제 써?
A. Component 내부 내용을 외부에서 자유롭게 조합해야 할 때 사용한다.

Q. State가 뭐야?
A. State는 Component 내부에서 관리되는 변경 가능한 UI 데이터다.

Q. State는 언제 써?
A. 사용자 행동이나 API 응답에 따라 화면이 바뀌어야 하는 값을 State로 둔다.

Q. State를 직접 바꾸면 안 돼?
A. 안 된다. React가 변경을 감지하지 못할 수 있으므로 setter 함수를 사용해야 한다.

Q. State가 바뀌면 무슨 일이 일어나?
A. Component가 다시 렌더링되고 변경된 State 기준으로 UI가 갱신된다.

Q. useState는 뭐야?
A. Functional Component에서 State를 선언하고 변경하기 위한 React Hook이다.

Q. setState 호출 직후 값이 바로 바뀌어?
A. React State 업데이트는 비동기적으로 처리될 수 있어 호출 직후 기존 값이 보일 수 있다.

Q. 배열 State는 push로 바꾸면 돼?
A. 안 된다. 새 배열을 만들어 setter에 전달해야 한다.

Q. 객체 State는 property만 바꾸면 돼?
A. 안 된다. 기존 객체를 직접 수정하지 말고 spread로 새 객체를 만들어야 한다.

Q. 이전 State 기반 업데이트는 어떻게 해?
A. `setCount((prevCount) => prevCount + 1)`처럼 functional update를 사용한다.

Q. 계산 가능한 값도 State로 둬야 해?
A. 대부분 아니다. Props나 State로 계산 가능하면 렌더링 중 계산하는 것이 좋다.

Q. Derived State를 잘못 쓰면 어떤 문제가 생겨?
A. 원본 값과 파생 값이 서로 불일치하는 버그가 생길 수 있다.

Q. React Event Handling은 어떻게 해?
A. onClick, onChange, onSubmit 같은 props에 Event Handler 함수를 전달한다.

Q. onClick={handleClick()}가 왜 문제야?
A. 렌더링 중 함수가 즉시 실행된다. 클릭 시 실행하려면 `onClick={handleClick}`처럼 함수 참조를 전달해야 한다.

Q. React에서 preventDefault는 언제 써?
A. form 제출 시 페이지 새로고침 같은 기본 동작을 막을 때 사용한다.

Q. Controlled Input이 뭐야?
A. input 값을 DOM이 아니라 React State로 관리하는 방식이다.

Q. input에 value만 넣고 onChange를 안 넣으면?
A. 사용자가 값을 변경할 수 없는 읽기 전용 input처럼 동작할 수 있다.

Q. Form 입력값 검증은 어디서 해?
A. 기본 검증은 submit handler 또는 별도 validation 함수에서 처리한다.

Q. React 조건부 렌더링은 어떻게 해?
A. early return, 삼항 연산자, logical AND, null return 등을 사용한다.

Q. && 조건부 렌더링은 언제 조심해야 해?
A. 왼쪽 값이 0이면 0이 화면에 렌더링될 수 있어 주의해야 한다.

Q. loading error empty 상태를 분리해야 해?
A. 분리하는 것이 좋다. 비동기 UI 상태를 명확하게 관리할 수 있다.

Q. React List Rendering은 어떻게 해?
A. 배열의 map 메서드로 데이터를 JSX 목록으로 변환한다.

Q. React list에서 key는 왜 필요해?
A. React가 목록 item의 추가, 삭제, 변경을 효율적으로 추적하기 위해 필요하다.

Q. index를 key로 써도 돼?
A. 정적인 목록은 가능하지만 추가, 삭제, 정렬이 있는 목록에서는 안정적인 ID를 사용하는 것이 좋다.

Q. key에 Math.random을 쓰면 안 돼?
A. 안 된다. 매 렌더링마다 key가 바뀌어 React가 item을 안정적으로 추적할 수 없다.

Q. key는 Component 안에서 props로 받을 수 있어?
A. 아니다. key는 React 내부에서 사용하는 특수 값이다. 필요하면 별도 prop으로 전달해야 한다.

Q. Hook이 뭐야?
A. Functional Component에서 React 기능을 사용할 수 있게 해주는 함수다.

Q. Hook은 왜 조건문 안에서 호출하면 안 돼?
A. React는 Hook 호출 순서로 상태를 관리한다. 조건에 따라 호출 순서가 바뀌면 상태 연결이 깨질 수 있다.

Q. Hook은 일반 함수에서 호출해도 돼?
A. 안 된다. React Component 또는 Custom Hook 내부에서 호출해야 한다.

Q. useEffect는 언제 써?
A. Component가 렌더링된 후 외부 시스템과 동기화해야 할 때 사용한다.

Q. useEffect dependency array가 비어 있으면?
A. Component mount 후 한 번 실행되는 패턴으로 사용된다.

Q. useEffect에 dependency array를 안 쓰면?
A. 렌더링될 때마다 effect가 실행된다.

Q. useEffect에서 무한 루프가 나는 이유는?
A. effect가 State를 변경하고 그 State가 dependency에 있어 다시 effect가 실행되는 구조일 수 있다.

Q. useEffect cleanup은 왜 필요해?
A. Timer, Event Listener, Subscription 같은 외부 작업이 남아 memory leak이나 중복 실행을 만들 수 있기 때문이다.

Q. cleanup은 언제 실행돼?
A. Component unmount 시 또는 dependency 변경으로 effect가 다시 실행되기 전에 실행된다.

Q. React에서 API 호출은 어디서 해?
A. 초기 데이터 로딩은 보통 useEffect에서 처리한다. 사용자 이벤트로 발생하는 요청은 Event Handler에서 처리한다.

Q. API 호출 상태는 어떤 State로 나눠?
A. data, loading, error, empty 상태를 분리하는 것이 좋다.

Q. fetch 실패 처리는 어떻게 해?
A. response.ok를 확인하고 실패 시 error state를 설정해 사용자에게 안내한다.

Q. React Props Type은 어떻게 정의해?
A. TypeScript에서 type 또는 interface로 Props 구조를 정의하고 Component parameter에 적용한다.

Q. useState 빈 배열 타입은 어떻게 써?
A. TypeScript에서는 `useState<Festival[]>([])`처럼 Generic으로 요소 타입을 명시한다.

Q. input onChange 타입은 뭐야?
A. TypeScript React에서는 일반적으로 `ChangeEvent<HTMLInputElement>`를 사용한다.

Q. React State 값은 어디서 확인해?
A. React DevTools에서 Component를 선택해 State와 Props를 확인할 수 있다.

Q. React 화면이 안 바뀌면 뭘 확인해?
A. State가 setter로 변경되는지, Props가 전달되는지, 조건부 렌더링 조건이 맞는지 확인한다.

Q. 개발 중 useEffect가 두 번 실행되는 것처럼 보여?
A. React StrictMode에서 개발 중 부작용 검사를 위해 effect가 추가 실행될 수 있다.

Q. Too many re-renders 오류는 왜 나?
A. 렌더링 중 State를 변경하거나 Event Handler를 잘못 전달해 렌더링마다 setState가 호출될 때 발생한다.

Q. React key warning은 왜 나?
A. 목록 item을 구분할 고유 key가 없거나 중복되었기 때문이다.

Q. useEffect dependency 경고는 무시해도 돼?
A. 대부분 무시하지 않는 것이 좋다. effect가 참조하는 값과 실행 조건을 다시 검토해야 한다.

Q. Component 파일은 어디에 둬?
A. 재사용 Component는 components 폴더, 화면 단위 Component는 pages 폴더에 두는 방식이 일반적이다.

Q. API 호출 함수는 Component 안에 둬도 돼?
A. 간단한 예제는 가능하지만 재사용되거나 복잡하면 api 파일로 분리하는 것이 좋다.

Q. React Core 다음 문서는 뭐가 좋아?
A. React Component Design, React Router, State Management, Data Fetching & REST API Integration 순서가 좋다.
