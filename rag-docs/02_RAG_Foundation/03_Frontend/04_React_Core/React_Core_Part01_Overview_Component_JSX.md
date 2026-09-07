# React Core Part01 - Overview, Component, JSX

---

# 1. React Overview

## 1.1 React Core Purpose

### [개념]

React Core는 Component 기반으로 사용자 인터페이스를 작성하기 위한 Frontend Foundation 지식이다.

React Core 문서는 사람용 입문서가 아니라 Frontend Agent / Review Agent / PM Agent가 React 화면 구조를 생성하고 검토하기 위한 RAG 문서다.

React Core의 핵심 목적은 아래 작업을 안정적으로 수행하는 것이다.

- React Component 작성
- JSX 구조 작성
- Props / State 기반 UI 흐름 이해
- Event Handling 기반 사용자 행동 처리
- Conditional Rendering 구현
- List Rendering 구현
- useState / useEffect 기초 적용
- API 연동 전 기본 화면 구조 설계

---

### [핵심]

React Core 핵심 키워드:

- React
- React Core
- UI Library
- Component
- Functional Component
- JSX
- Props
- State
- Event Handling
- Conditional Rendering
- List Rendering
- Hook
- useState
- useEffect
- Re-render
- Declarative UI
- State-driven UI

React Core 우선순위:

1. Component
2. JSX
3. Props
4. State
5. Event Handling
6. Conditional Rendering
7. List Rendering
8. Hook Basics
9. useState
10. useEffect

---

### [실무]

2026 실무 기준 React Core는 React API 암기용 문서가 아니다.

React Core는 Frontend Agent가 아래 작업을 수행할 수 있도록 작성한다.

- 기본 화면 Component 생성
- JSX 기반 UI 구조 생성
- Props 전달 구조 설계
- State 기반 UI 갱신 설계
- Event Handler 작성
- loading / error / empty / success UI 분리
- React Component Design 문서로 이어지는 기본 구조 생성

React Core 문서는 아래 흐름의 기반이다.

```text
HTML CSS Foundation
→ JavaScript Foundation
→ TypeScript Foundation
→ React Core
→ React Component Design
→ React Router
→ State Management
→ Data Fetching REST API Integration
```

권장 기준:

- Functional Component 기준
- Hook 기준
- JSX 기준
- State-driven UI 기준
- Component Composition 기준
- TypeScript Ready 구조 고려

금지 기준:

- Class Component 중심 설명
- jQuery DOM 조작 중심 설명
- 긴 전체 프로젝트 코드
- 불필요한 boilerplate
- 사람용 장문 서론

---

### [FAQ]

Q. React Core 문서는 사람 공부용 문서야?
A. 아니다. Frontend Agent가 React 화면과 기본 Component 로직을 생성하고 검토하기 위한 RAG 문서다.

Q. React Core에서 가장 중요한 기준은 뭐야?
A. Component, JSX, Props, State, Event Handling, Conditional Rendering, List Rendering, useState, useEffect다.

Q. React Core는 어떤 문서와 연결돼?
A. HTML/CSS, JavaScript, TypeScript Foundation 이후 React Component Design, React Router, State Management, Data Fetching 문서로 연결된다.

---

## 1.2 React Definition

### [개념]

React는 Component 기반으로 사용자 인터페이스를 만들기 위한 JavaScript UI Library다.

React는 화면을 작은 Component 단위로 나누고, 데이터 변화에 따라 UI를 다시 렌더링한다.

기본 Flow:

```text
State / Props Change
→ Component Render
→ JSX Result
→ DOM Update
→ User sees UI
```

---

### [핵심]

React 핵심 개념:

- React는 UI Library
- React는 Component 기반
- React는 Declarative UI 방식
- React는 JSX 사용
- React는 Props로 데이터 전달
- React는 State로 UI 상태 관리
- State 변경 시 Re-render 발생
- Props 변경 시 Child Component Re-render 가능
- 직접 DOM 조작보다 State 기반 Rendering 우선
- 화면 구조와 로직을 Component로 묶음

---

### [실무]

React는 아래 상황에서 사용한다.

- 재사용 가능한 UI Component 작성
- API 데이터 기반 화면 작성
- 사용자 입력 Form 처리
- 조건부 UI 처리
- 목록 UI 처리
- SPA 화면 구성
- Frontend 팀 협업 프로젝트
- Backend API와 연결되는 화면 구현

React 실무 작성 기준:

```text
Data
→ Props / State
→ Component Render
→ UI Output
```

권장:

- 화면은 Component로 분리
- 데이터는 Props 또는 State로 전달
- UI 변화는 State 변경으로 처리
- DOM 직접 조작은 최소화
- API 응답 상태는 loading / error / empty / success로 분리

---

### [FAQ]

Q. React는 Framework야 Library야?
A. React 자체는 UI Library다. Router, 상태관리, 데이터 패칭 등을 함께 사용하면 Framework처럼 구성할 수 있다.

Q. React는 DOM을 직접 조작해?
A. 일반적으로 직접 조작하지 않는다. State와 Props 변화에 따라 React가 UI를 갱신한다.

Q. React에서 화면이 바뀌는 기준은 뭐야?
A. 주로 State 또는 Props가 변경되면 Component가 다시 렌더링되고 화면이 갱신된다.

---

# 2. Declarative UI

## 2.1 Declarative UI Basics

### [개념]

Declarative UI는 DOM을 어떻게 바꿀지 직접 명령하지 않고 현재 상태에 따라 어떤 UI가 보여야 하는지 선언하는 방식이다.

React는 Declarative UI를 사용한다.

명령형 UI는 DOM 변경 절차를 직접 작성한다.

```javascript
button.disabled = true;
button.textContent = "Loading";
```

선언형 UI는 상태에 따른 UI 결과를 작성한다.

```jsx
<button disabled={loading}>{loading ? "Loading" : "Submit"}</button>
```

---

### [핵심]

Declarative UI 핵심:

- UI 결과를 상태 기준으로 선언
- DOM 변경 절차를 직접 작성하지 않음
- React는 State 변경을 기준으로 UI를 다시 계산
- State가 UI의 기준
- Component는 현재 State / Props에 따른 JSX를 반환
- 유지보수와 디버깅에 유리

비교:

| 구분         | Imperative UI   | Declarative UI      |
| ------------ | --------------- | ------------------- |
| 기준         | DOM 변경 절차   | 상태에 따른 UI 결과 |
| 방식         | 직접 조작       | 상태 선언           |
| React 적합성 | 낮음            | 높음                |
| 유지보수     | 복잡해지기 쉬움 | 상태 흐름 추적 쉬움 |

---

### [실무]

React에서는 UI를 직접 바꾸지 않고 State를 변경한다.

권장 Flow:

```text
User Action
→ Event Handler
→ State Change
→ React Render
→ UI Result
```

금지:

- document.querySelector로 React UI 직접 변경 남용
- innerHTML로 React 화면 변경
- DOM 상태와 React State 불일치 발생
- React 외부에서 Component UI 강제 변경

좋은 예:

```jsx
function SubmitButton({ loading }) {
  return (
    <button type="submit" disabled={loading}>
      {loading ? "Loading" : "Submit"}
    </button>
  );
}
```

---

### [FAQ]

Q. Declarative UI가 뭐야?
A. 현재 상태에 따라 어떤 UI가 보여야 하는지 선언하는 방식이다.

Q. React에서 document.querySelector를 쓰면 안 돼?
A. 대부분의 UI 변경에는 쓰지 않는다. React에서는 State와 Props로 UI를 제어하는 것이 기본이다.

Q. Declarative UI가 왜 좋아?
A. 상태와 UI 관계가 명확해져 유지보수와 디버깅이 쉬워진다.

---

# 3. Component

## 3.1 Component Basics

### [개념]

Component는 React UI를 구성하는 재사용 가능한 단위다.

Component는 화면의 일부를 독립적인 함수처럼 작성하고, 필요한 데이터를 Props로 받아 JSX를 반환한다.

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

Component 핵심 키워드:

- React Component
- Functional Component
- Reusable UI Unit
- Component Name PascalCase
- Return JSX
- Props Input
- State Internal Data
- Component Composition
- Component File Separation

Component 작성 규칙:

- Component 이름은 PascalCase
- Component는 JSX 반환
- Component는 하나의 주요 책임을 가짐
- Props로 외부 데이터 전달
- State로 내부 UI 상태 관리
- UI가 커지면 하위 Component로 분리
- 재사용 가능한 단위로 설계

---

### [실무]

좋은 Component 예:

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

Component 분리 기준:

- 화면 구조가 길어질 때
- 같은 UI를 여러 곳에서 재사용할 때
- Props / State 책임이 명확히 나뉠 때
- Page Component와 UI Component 역할을 분리할 때
- Event Handler 또는 조건부 렌더링이 복잡해질 때

권장 구조:

```text
Page Component
→ Section Component
→ List Component
→ Card Component
→ Button / Input Component
```

주의:

- 모든 코드를 App.jsx에 몰아넣지 않음
- Component 이름을 소문자로 시작하지 않음
- 하나의 Component에 여러 책임을 과도하게 넣지 않음
- Component 내부에 불필요한 중첩 Component를 남용하지 않음

---

### [FAQ]

Q. React Component가 뭐야?
A. Component는 React UI를 구성하는 재사용 가능한 단위다.

Q. Component 이름은 왜 대문자로 시작해?
A. React가 소문자는 HTML 태그로 보고 대문자로 시작하는 이름을 Component로 인식하기 때문이다.

Q. Component는 얼마나 작게 나눠야 해?
A. 역할이 명확하고 재사용 가능하거나 복잡도를 줄일 수 있을 때 분리한다.

Q. Component 안에 Component를 계속 만들면 돼?
A. 간단한 경우는 가능하지만 매 렌더링마다 새 함수가 만들어질 수 있어 일반적으로 파일 또는 외부 함수로 분리한다.

---

## 3.2 Functional Component

### [개념]

Functional Component는 함수로 작성하는 React Component다.

현대 React에서는 Functional Component와 Hook을 기본으로 사용한다.

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

### [핵심]

Functional Component 핵심:

- function component
- arrow function component
- props parameter
- return JSX
- hook usage
- Functional Component + Hook 기준
- Class Component 중심 설명 제외

작성 방식:

```jsx
function FestivalTitle({ title }) {
  return <h1>{title}</h1>;
}
```

또는

```jsx
const FestivalTitle = ({ title }) => {
  return <h1>{title}</h1>;
};
```

---

### [실무]

Functional Component 작성 기준:

- Function Declaration 또는 Arrow Function 중 프로젝트 컨벤션 유지
- Component 이름 명확화
- Props 구조 명확화
- JSX return 명확화
- Hook은 Component 최상위에서 호출
- 조건문 내부에서 Hook 호출 금지
- 반복문 내부에서 Hook 호출 금지
- 일반 함수 내부에서 Hook 호출 금지

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

---

### [FAQ]

Q. Functional Component가 뭐야?
A. 함수로 작성하는 React Component다. 현대 React에서는 Functional Component와 Hook을 기본으로 사용한다.

Q. React에서 class component를 써야 해?
A. 신규 코드에서는 Functional Component와 Hook을 기준으로 작성한다. 기존 코드 유지보수에서 class component를 볼 수는 있다.

Q. Functional Component에서도 상태를 쓸 수 있어?
A. 가능하다. useState 같은 Hook을 사용한다.

---

## 3.3 Component Composition

### [개념]

Component Composition은 작은 Component를 조합해 큰 UI를 만드는 방식이다.

React는 상속보다 Component Composition을 우선한다.

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

---

### [핵심]

Component Composition 핵심:

- Parent Component
- Child Component
- Props Passing
- Children
- Reusable Component
- Layout Component
- Page Component
- UI Component
- Composition over Inheritance

Composition Flow:

```text
Page
→ Layout
→ Section
→ List
→ Card
→ Button / Input
```

---

### [실무]

Component 역할 분리:

| 구분              | 역할                        | 예시                   |
| ----------------- | --------------------------- | ---------------------- |
| Page Component    | 화면 단위, 데이터 흐름 관리 | FestivalPage           |
| Section Component | 화면 영역 구성              | PopularFestivalSection |
| List Component    | 배열 데이터 렌더링          | FestivalList           |
| Card Component    | 단일 데이터 표시            | FestivalCard           |
| Common Component  | 재사용 UI                   | Button, Modal, Input   |

주의:

- 너무 깊은 Props 전달은 복잡도 증가
- 공통 UI는 재사용 Component로 분리
- Page Component와 UI Component 역할 구분
- Composition은 상속보다 우선
- 데이터 흐름이 복잡하면 State Management 문서로 연결

---

### [FAQ]

Q. React에서 상속을 많이 써?
A. 아니다. React에서는 상속보다 Component Composition을 우선한다.

Q. Page Component와 UI Component 차이는?
A. Page Component는 화면 단위이며 데이터와 흐름을 가질 수 있고, UI Component는 재사용 가능한 표시 단위다.

Q. Component Composition은 왜 필요해?
A. 작은 Component를 조합해 복잡한 화면을 유지보수하기 쉽게 만들기 위해 필요하다.

---

# 4. JSX

## 4.1 JSX Basics

### [개념]

JSX는 JavaScript 안에서 HTML과 비슷한 UI 구조를 작성하는 문법이다.

JSX는 HTML이 아니라 JavaScript 표현식으로 변환되는 React 문법이다.

예:

```jsx
const element = <h1>Hello React</h1>;
```

Component에서 JSX 반환:

```jsx
function FestivalTitle({ title }) {
  return <h1 className="page-title">{title}</h1>;
}
```

---

### [핵심]

JSX 핵심 규칙:

- JSX는 HTML이 아님
- JavaScript 표현식 사용 가능
- 하나의 부모 요소 필요
- class 대신 className 사용
- for 대신 htmlFor 사용
- self-closing tag 필요
- 중괄호 `{}`로 JavaScript expression 사용
- statement는 JSX 내부에 직접 작성 불가
- 여러 요소 반환 시 Fragment 사용

JSX 사용 가능:

- string
- number
- variable
- function call
- ternary expression
- logical expression
- array map result
- null

JSX 사용 주의:

- if statement 직접 사용 불가
- for statement 직접 사용 불가
- while statement 직접 사용 불가
- object 직접 렌더링 불가

---

### [실무]

좋은 JSX 예:

```jsx
function FestivalInfo({ festival }) {
  return (
    <article className="festival-info">
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

문제:

- 객체 자체는 React child로 렌더링할 수 없음

개선:

```jsx
<div>{festival.title}</div>
```

JSX 작성 기준:

- className 사용
- 중괄호 내부에는 expression 사용
- 복잡한 조건은 JSX 밖에서 분리
- map 사용 시 key 필요
- 불필요한 div 대신 Fragment 사용 가능

---

### [FAQ]

Q. JSX는 HTML이야?
A. 아니다. JSX는 JavaScript 안에서 UI 구조를 표현하는 문법이며 React가 처리한다.

Q. JSX에서 class 대신 className을 쓰는 이유는?
A. class는 JavaScript 예약어와 충돌 가능성이 있어 React JSX에서는 className을 사용한다.

Q. JSX에서 if문을 바로 쓸 수 있어?
A. JSX 내부에는 statement를 직접 쓸 수 없다. 조건부 렌더링은 삼항 연산자, &&, early return 등을 사용한다.

Q. JSX 중괄호 안에는 뭘 넣을 수 있어?
A. 변수, 함수 호출, 삼항 연산자, 논리식, map 결과 같은 JavaScript expression을 넣을 수 있다.

---

## 4.2 JSX Expression

### [개념]

JSX Expression은 JSX 내부에서 중괄호 `{}`를 사용해 JavaScript 값을 표현하는 방식이다.

예:

```jsx
<p>{festival.title}</p>
<p>{festival.averageRating ?? "평점 없음"}</p>
```

---

### [핵심]

JSX Expression 사용 가능:

- variable
- function call
- ternary expression
- logical expression
- array map result
- null
- string
- number

JSX Expression 사용 불가:

- if statement
- for statement
- while statement
- object 직접 렌더링

예:

```jsx
<h2>{title}</h2>
<p>{isOpen ? "Open" : "Closed"}</p>
{imageUrl && <img src={imageUrl} alt={title} />}
```

---

### [실무]

권장:

```jsx
function FestivalStatus({ active }) {
  return <p>{active ? "진행 중" : "종료"}</p>;
}
```

복잡한 조건 분리:

```jsx
function FestivalBadge({ status }) {
  const label = status === "ACTIVE" ? "진행 중" : "종료";

  return <span>{label}</span>;
}
```

주의:

- JSX 안에 복잡한 조건식을 과도하게 넣지 않음
- 무거운 함수 호출은 렌더링마다 실행될 수 있음
- 객체를 직접 출력하지 않음
- 배열 map 결과는 key와 함께 렌더링

---

### [FAQ]

Q. JSX 중괄호 안에 객체를 넣어도 돼?
A. 객체 자체는 React child로 렌더링할 수 없다. 객체의 문자열 property 등을 렌더링해야 한다.

Q. JSX에서 함수 호출해도 돼?
A. 가능하지만 렌더링마다 실행되므로 무거운 연산은 분리하거나 최적화를 고려한다.

Q. JSX 안에서 for문을 바로 쓸 수 있어?
A. 직접 쓸 수 없다. 배열 렌더링은 map을 사용한다.

---

## 4.3 Fragment

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

Fragment 핵심:

- Fragment
- Empty Tag Syntax
- One Parent Rule
- No Extra DOM
- key with Fragment list

Fragment 사용 이유:

- 하나의 JSX 반환값 필요
- 불필요한 div 추가 방지
- table 구조 유지
- 여러 형제 요소 반환
- list에서 여러 요소 그룹 반환

---

### [실무]

일반 Fragment:

```jsx
function FestivalHeader({ title, description }) {
  return (
    <>
      <h1>{title}</h1>
      <p>{description}</p>
    </>
  );
}
```

key가 필요한 Fragment:

```jsx
function FestivalDescriptionList({ festivals }) {
  return (
    <dl>
      {festivals.map((festival) => (
        <React.Fragment key={festival.festivalId}>
          <dt>{festival.title}</dt>
          <dd>{festival.region}</dd>
        </React.Fragment>
      ))}
    </dl>
  );
}
```

주의:

- 빈 태그 `<>`에는 key를 줄 수 없음
- key가 필요하면 `React.Fragment` 사용
- 의미 없는 div 남용 방지
- Fragment는 DOM에 실제 노드를 추가하지 않음

---

### [FAQ]

Q. JSX에서 왜 하나의 부모 요소가 필요해?
A. Component는 하나의 JSX 값만 반환해야 하기 때문이다. 여러 요소는 Fragment로 묶을 수 있다.

Q. Fragment는 왜 써?
A. 불필요한 DOM 요소를 추가하지 않고 여러 JSX 요소를 묶기 위해 사용한다.

Q. 빈 태그 `<>`와 React.Fragment 차이는?
A. 둘 다 Fragment지만 key가 필요한 경우에는 `React.Fragment`를 사용한다.

---

# 5. React Element and Component Comparison

## 5.1 Component vs Element

### [개념]

Component는 UI를 만드는 함수 또는 재사용 단위다.

Element는 Component 또는 HTML 태그가 JSX로 표현된 UI 설명 객체다.

예:

```jsx
function FestivalCard() {
  return <article>Festival</article>;
}

const element = <FestivalCard />;
```

`FestivalCard`는 Component이고 `<FestivalCard />`는 Element다.

---

### [핵심]

비교:

| 비교   | Component               | Element               |
| ------ | ----------------------- | --------------------- |
| 의미   | UI를 만드는 재사용 단위 | 화면에 그릴 UI 설명   |
| 형태   | 함수 또는 클래스        | JSX 결과              |
| 예     | FestivalCard            | `<FestivalCard />`    |
| 역할   | Props를 받아 JSX 반환   | React가 렌더링할 대상 |
| 재사용 | 가능                    | 특정 렌더링 결과      |

---

### [실무]

Agent가 React 코드를 생성할 때 아래 구분을 유지한다.

- Component 이름은 PascalCase
- Component 사용은 JSX Element 형태
- Props는 Element에 속성으로 전달
- Component는 JSX를 반환

예:

```jsx
function FestivalCard({ title }) {
  return <article>{title}</article>;
}

function FestivalPage() {
  return <FestivalCard title="Spring Festival" />;
}
```

주의:

- 소문자 JSX는 HTML 태그로 인식
- 대문자 JSX는 Component로 인식
- Component와 Element 용어 혼용 주의

---

### [FAQ]

Q. Component와 Element 차이는 뭐야?
A. Component는 UI를 만드는 재사용 단위이고 Element는 React가 렌더링할 UI 설명이다.

Q. `<FestivalCard />`는 Component야 Element야?
A. JSX로 작성된 React Element다. FestivalCard 함수 자체가 Component다.

Q. Component 이름은 왜 PascalCase로 써?
A. React가 대문자로 시작하는 JSX를 사용자 정의 Component로 인식하기 때문이다.

---

# 6. Common Mistakes

## 6.1 React Overview and Component Mistakes

### [개념]

React Core 초기 단계에서 발생하는 주요 실수는 Component 이름, JSX 규칙, 직접 DOM 조작, Component 책임 혼합에서 자주 발생한다.

---

### [핵심]

자주 발생하는 실수:

- Component 이름 소문자로 작성
- JSX에서 class 사용
- JSX 내부에 if statement 직접 작성
- 객체를 React child로 직접 렌더링
- 불필요한 div 남용
- Component에 여러 책임 과도하게 포함
- 모든 코드를 App.jsx에 작성
- document.querySelector로 UI 직접 변경
- innerHTML로 React UI 변경
- Component와 Element 용어 혼동

---

### [실무]

문제 예:

```jsx
function festivalCard() {
  return <div class="card">Festival</div>;
}
```

문제:

- Component 이름이 소문자로 시작
- JSX에서 class 사용

개선:

```jsx
function FestivalCard() {
  return <div className="card">Festival</div>;
}
```

Debug Flow:

```text
Console Error Check
→ Component Name Check
→ JSX Syntax Check
→ Props / State Check
→ Render Result Check
→ DOM Direct Manipulation Check
```

---

### [FAQ]

Q. React 초보가 Component에서 가장 많이 하는 실수는?
A. Component 이름 소문자 작성, JSX에서 class 사용, 모든 코드를 App.jsx에 넣는 실수가 많다.

Q. JSX 오류는 어디서 먼저 확인해?
A. Browser Console과 개발 서버 컴파일 오류를 먼저 확인한다.

Q. React 화면이 이상하면 document.querySelector로 고치면 돼?
A. 아니다. React에서는 State와 Props 기준으로 UI를 수정하는 것이 기본이다.

---

# 7. Checklist

## 7.1 Part01 Quality Checklist

### [개념]

React Core Part01 검수는 Overview, Declarative UI, Component, JSX, Fragment, Component vs Element를 기준으로 수행한다.

---

### [핵심]

Checklist:

```md
- [ ] React가 UI Library로 설명되었는가?
- [ ] React Core 목적이 Agent Retrieval 기준으로 설명되었는가?
- [ ] Declarative UI가 포함되었는가?
- [ ] State / Props Change → Render Flow가 포함되었는가?
- [ ] Component 기본 개념이 포함되었는가?
- [ ] Functional Component 기준이 포함되었는가?
- [ ] Component 이름 PascalCase 규칙이 포함되었는가?
- [ ] Component Composition이 포함되었는가?
- [ ] JSX가 HTML이 아니라는 설명이 포함되었는가?
- [ ] className / htmlFor 규칙이 포함되었는가?
- [ ] JSX Expression 규칙이 포함되었는가?
- [ ] Fragment 사용 기준이 포함되었는가?
- [ ] Component vs Element 비교가 포함되었는가?
- [ ] Common Mistakes가 포함되었는가?
- [ ] FAQ가 포함되었는가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 Flow:

```text
Draft
→ MASTER_RAG_RULES Section Check
→ React Core Domain Scope Check
→ Overview Keyword Check
→ Component Rule Check
→ JSX Rule Check
→ FAQ Check
→ Retrieval Queries Check
→ Final Review
```

치명적 문제 기준:

- React Core 범위 초과
- Router / State Management 심화 포함
- Class Component 중심 설명
- 긴 에세이형 설명
- FAQ 누락
- Retrieval Queries 누락
- Component / JSX 핵심 키워드 누락

---

### [FAQ]

Q. Part01에서 가장 중요한 검수 기준은?
A. React Overview, Declarative UI, Component, Functional Component, JSX, Fragment, FAQ, Retrieval Queries 포함 여부다.

Q. Part01에서 다루면 안 되는 내용은?
A. React Router, 전역 상태관리, TanStack Query, 고급 Hook, Next.js, 테스트 심화는 제외한다.

---

# Retrieval Queries

### [FAQ]

Q. React Core 문서는 왜 필요해?
A. Frontend Agent가 React 화면을 만들기 전에 Component, JSX, Props, State, Event, Hook 기본 구조를 이해해야 하기 때문이다.

Q. React는 뭐야?
A. React는 Component 기반으로 사용자 인터페이스를 만들기 위한 JavaScript UI Library다.

Q. React는 Framework야 Library야?
A. React 자체는 UI Library다. Router, 상태관리, 데이터 패칭 등을 함께 사용하면 Framework처럼 구성할 수 있다.

Q. React는 DOM을 직접 조작해?
A. 일반적으로 직접 조작하지 않는다. State와 Props 변화에 따라 React가 UI를 갱신한다.

Q. React에서 화면이 바뀌는 기준은 뭐야?
A. 주로 State 또는 Props가 변경되면 Component가 다시 렌더링되고 화면이 갱신된다.

Q. Declarative UI가 뭐야?
A. 현재 상태에 따라 어떤 UI가 보여야 하는지 선언하는 방식이다.

Q. React에서 document.querySelector를 쓰면 안 돼?
A. 대부분의 UI 변경에는 쓰지 않는다. React에서는 State와 Props로 UI를 제어하는 것이 기본이다.

Q. Declarative UI가 왜 좋아?
A. 상태와 UI 관계가 명확해져 유지보수와 디버깅이 쉬워진다.

Q. React Component가 뭐야?
A. Component는 React UI를 구성하는 재사용 가능한 단위다.

Q. Component 이름은 왜 대문자로 시작해?
A. React가 소문자는 HTML 태그로 보고 대문자로 시작하는 이름을 Component로 인식하기 때문이다.

Q. Component는 얼마나 작게 나눠야 해?
A. 역할이 명확하고 재사용 가능하거나 복잡도를 줄일 수 있을 때 분리한다.

Q. Functional Component가 뭐야?
A. 함수로 작성하는 React Component다. 현대 React에서는 Functional Component와 Hook을 기본으로 사용한다.

Q. React에서 class component를 써야 해?
A. 신규 코드에서는 Functional Component와 Hook을 기준으로 작성한다.

Q. Functional Component에서도 상태를 쓸 수 있어?
A. 가능하다. useState 같은 Hook을 사용한다.

Q. React에서 상속을 많이 써?
A. 아니다. React에서는 상속보다 Component Composition을 우선한다.

Q. Page Component와 UI Component 차이는?
A. Page Component는 화면 단위이며 데이터와 흐름을 가질 수 있고, UI Component는 재사용 가능한 표시 단위다.

Q. Component Composition은 왜 필요해?
A. 작은 Component를 조합해 복잡한 화면을 유지보수하기 쉽게 만들기 위해 필요하다.

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

Q. JSX에서 함수 호출해도 돼?
A. 가능하지만 렌더링마다 실행되므로 무거운 연산은 분리하거나 최적화를 고려한다.

Q. JSX 안에서 for문을 바로 쓸 수 있어?
A. 직접 쓸 수 없다. 배열 렌더링은 map을 사용한다.

Q. Fragment는 왜 써?
A. 불필요한 DOM 요소를 추가하지 않고 여러 JSX 요소를 묶기 위해 사용한다.

Q. JSX에서 왜 하나의 부모 요소가 필요해?
A. Component는 하나의 JSX 값만 반환해야 하기 때문이다. 여러 요소는 Fragment로 묶을 수 있다.

Q. 빈 태그 `<>`와 React.Fragment 차이는?
A. 둘 다 Fragment지만 key가 필요한 경우에는 `React.Fragment`를 사용한다.

Q. Component와 Element 차이는 뭐야?
A. Component는 UI를 만드는 재사용 단위이고 Element는 React가 렌더링할 UI 설명이다.

Q. `<FestivalCard />`는 Component야 Element야?
A. JSX로 작성된 React Element다. FestivalCard 함수 자체가 Component다.

Q. React 초보가 Component에서 가장 많이 하는 실수는?
A. Component 이름 소문자 작성, JSX에서 class 사용, 모든 코드를 App.jsx에 넣는 실수가 많다.

Q. JSX 오류는 어디서 먼저 확인해?
A. Browser Console과 개발 서버 컴파일 오류를 먼저 확인한다.

Q. React 화면이 이상하면 document.querySelector로 고치면 돼?
A. 아니다. React에서는 State와 Props 기준으로 UI를 수정하는 것이 기본이다.

Q. React Core Part01 다음 문서는 뭐가 좋아?
A. Props, State, useState를 다루는 React Core Part02로 이어지는 것이 좋다.
