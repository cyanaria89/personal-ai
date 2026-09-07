# React Core Part02 - Props, State, useState

---

# 1. Props

## 1.1 Props Basics

### [개념]

Props는 부모 Component가 자식 Component에 전달하는 읽기 전용 데이터다.

Props는 Parent Component에서 Child Component로 전달된다.

Props는 Component 재사용성과 데이터 전달 구조를 만드는 React Core 핵심 개념이다.

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

Props 핵심 키워드:

- Props
- Parent Component
- Child Component
- Props Passing
- Read-only Data
- Props Destructuring
- Callback Props
- children
- Reusable Component
- Child Re-render

Props 핵심 규칙:

- Props는 부모에서 자식으로 전달
- Props는 읽기 전용
- Props 직접 수정 금지
- Props 변경 시 Child Component Re-render 가능
- Props로 data 전달 가능
- Props로 callback function 전달 가능
- Props로 Component 설정값 전달 가능
- Props는 Component 재사용성을 높임

---

### [실무]

Props 사용 대상:

- UI 표시 데이터
- Component 설정값
- Event Callback
- children
- optional props 기본값
- API 응답 데이터를 하위 Component에 전달
- 재사용 UI Component에 필요한 값 전달

좋은 예:

```jsx
function FestivalCard({ title, imageUrl, region, onSelect }) {
  return (
    <article className="festival-card" onClick={onSelect}>
      {imageUrl && <img src={imageUrl} alt={title} />}
      <h2>{title}</h2>
      <p>{region}</p>
    </article>
  );
}
```

사용 예:

```jsx
function FestivalList({ festivals }) {
  return (
    <section className="festival-list">
      {festivals.map((festival) => (
        <FestivalCard
          key={festival.festivalId}
          title={festival.title}
          imageUrl={festival.imageUrl}
          region={festival.region}
          onSelect={() => console.log(festival.festivalId)}
        />
      ))}
    </section>
  );
}
```

주의:

- Child Component에서 Props 직접 수정 금지
- Props 이름은 의미 있게 작성
- Props 개수가 너무 많으면 Component 책임 분리 검토
- Event Callback Props는 `on` prefix 권장
- Component 내부 Handler는 `handle` prefix 권장

---

### [FAQ]

Q. Props가 뭐야?
A. Props는 부모 Component가 자식 Component에 전달하는 읽기 전용 데이터다.

Q. Props는 어느 방향으로 전달돼?
A. 부모 Component에서 자식 Component로 전달된다.

Q. Props는 수정해도 돼?
A. 안 된다. Props는 읽기 전용이다. 변경이 필요하면 부모 State를 변경하는 callback을 전달한다.

Q. Props로 함수도 전달할 수 있어?
A. 가능하다. 자식에서 발생한 이벤트를 부모에게 알릴 때 callback props를 자주 사용한다.

---

## 1.2 Props Destructuring

### [개념]

Props Destructuring은 Props 객체에서 필요한 값을 구조 분해로 꺼내는 방식이다.

Props Destructuring은 Component 내부에서 `props.title`처럼 반복 접근하지 않고 필요한 값을 명확하게 사용하게 한다.

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

Props Destructuring 핵심 키워드:

- props object
- destructuring
- default value
- rest props basics
- readability
- optional props
- TypeScript props type readiness

Props Destructuring 장점:

- Props 사용 위치 명확
- 코드 반복 감소
- Component 입력값 파악 쉬움
- 기본값 설정 가능
- TypeScript Props Type과 연결 쉬움

---

### [실무]

기본값 설정 예:

```jsx
function Button({ type = "button", disabled = false, children }) {
  return (
    <button type={type} disabled={disabled}>
      {children}
    </button>
  );
}
```

Rest Props 기초 예:

```jsx
function TextInput({ label, ...inputProps }) {
  return (
    <label>
      {label}
      <input {...inputProps} />
    </label>
  );
}
```

주의:

- Props 개수가 너무 많으면 Component 책임 검토
- 중첩 객체 Destructuring 과도 사용 금지
- 기본값 설정 위치 일관성 유지
- Rest Props 남용 금지
- TypeScript 사용 시 Props Type과 정합성 유지

---

### [FAQ]

Q. Props Destructuring은 왜 써?
A. `props.title`처럼 반복 접근하지 않고 필요한 값을 명확하게 사용할 수 있기 때문이다.

Q. Props 기본값은 어떻게 줘?
A. 구조 분해 할당에서 `type = "button"`처럼 기본값을 설정할 수 있다.

Q. Props가 너무 많으면 어떻게 해?
A. Component 책임을 분리하거나 관련 데이터를 객체로 묶을지 검토한다.

---

## 1.3 Callback Props

### [개념]

Callback Props는 부모 Component가 자식 Component에 함수 형태로 전달하는 Props다.

Callback Props는 자식 Component에서 발생한 이벤트를 부모 Component로 전달할 때 사용한다.

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

Callback Props 핵심 키워드:

- callback props
- parent state update
- child event
- onClick
- onChange
- onSubmit
- event lifting
- parent-child communication

Callback Props 규칙:

- Props Callback 이름은 `on` prefix 권장
- Child 내부 Handler 이름은 `handle` prefix 권장
- Child는 직접 부모 State를 수정하지 않음
- Child는 Callback 호출로 이벤트만 전달
- 실제 State 변경은 Parent에서 수행

---

### [실무]

Parent State를 Child Event로 변경하는 예:

```jsx
function FestivalPage() {
  const [selectedFestivalId, setSelectedFestivalId] = useState(null);

  function handleSelectFestival(festivalId) {
    setSelectedFestivalId(festivalId);
  }

  return (
    <FestivalCard
      festivalId={1}
      title="Spring Festival"
      onSelect={handleSelectFestival}
    />
  );
}

function FestivalCard({ festivalId, title, onSelect }) {
  return (
    <article>
      <h2>{title}</h2>
      <button type="button" onClick={() => onSelect(festivalId)}>
        Select
      </button>
    </article>
  );
}
```

Flow:

```text
User Click
→ Child Component Event Handler
→ Callback Props 호출
→ Parent State Update
→ Re-render
```

주의:

- `onClick={onSelect(festivalId)}`는 즉시 실행되므로 주의
- 인자가 필요하면 arrow function 사용
- Callback Props가 많아지면 Component 책임 분리 검토
- 너무 깊은 Callback 전달은 State Management 문서로 연결

---

### [FAQ]

Q. Callback Props가 뭐야?
A. 부모가 자식에게 전달하는 함수 Props이며 자식 이벤트를 부모에게 알릴 때 사용한다.

Q. 자식 Component가 부모 State를 직접 바꿀 수 있어?
A. 직접 바꾸지 않는다. 부모가 전달한 Callback Props를 호출해 부모가 State를 변경하게 한다.

Q. onClick에서 Callback에 인자를 넘기려면 어떻게 해?
A. `onClick={() => onSelect(id)}`처럼 함수로 감싸서 전달한다.

---

## 1.4 children

### [개념]

children은 Component 태그 사이에 전달되는 React Node다.

children은 Wrapper Component, Layout Component, Card Component처럼 내부 내용을 외부에서 자유롭게 조합할 때 사용한다.

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

children 핵심 키워드:

- children
- React Node
- Wrapper Component
- Layout Component
- Card Component
- Modal Component
- Component Composition
- Reusable Container

children 사용 대상:

- Card
- Modal
- Layout
- Section
- Button
- FormGroup
- 공통 wrapper UI

---

### [실무]

Layout Component 예:

```jsx
function PageLayout({ children }) {
  return <main className="page-layout">{children}</main>;
}
```

Card Component 예:

```jsx
function InfoCard({ children }) {
  return <article className="info-card">{children}</article>;
}
```

사용 예:

```jsx
function FestivalPage() {
  return (
    <PageLayout>
      <InfoCard>
        <h1>Festival</h1>
        <p>Festival information</p>
      </InfoCard>
    </PageLayout>
  );
}
```

주의:

- children 구조가 복잡하면 명시적 props 검토
- 너무 많은 암묵적 children 의존 금지
- 접근성 구조 유지
- Layout 역할과 데이터 역할을 혼합하지 않음

---

### [FAQ]

Q. children은 언제 써?
A. Component 내부 내용을 외부에서 자유롭게 조합해야 할 때 사용한다.

Q. children과 props 차이는?
A. children은 태그 사이에 전달되는 특별한 props이고, 일반 props는 속성 형태로 전달된다.

Q. children을 너무 많이 쓰면 문제야?
A. 구조가 불명확해질 수 있다. 필요한 경우 명시적 props나 Component 분리를 검토한다.

---

# 2. State

## 2.1 State Basics

### [개념]

State는 Component 내부에서 관리되는 변경 가능한 UI 데이터다.

State가 변경되면 React는 Component를 다시 렌더링한다.

State는 사용자 행동, API 응답, 화면 상태 변화에 따라 UI가 바뀌어야 할 때 사용한다.

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

State 핵심 키워드:

- State
- UI State
- useState
- setter function
- Re-render
- initial value
- functional update
- immutable update
- local component state

State 핵심 규칙:

- State는 Component 내부 변경 가능 데이터
- useState로 생성
- setter function으로 변경
- State 직접 변경 금지
- State 변경 시 Re-render 발생
- 초기값 타입 중요
- 이전 State 기반 업데이트는 functional update 권장
- 객체 / 배열 State는 immutable update 필요

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
- tab 선택 상태
- checkbox 선택 상태

State로 두지 않아도 되는 값:

- Props로 계산 가능한 값
- 기존 State로 계산 가능한 값
- 렌더링 중 계산 가능한 값
- 고정 상수
- DOM에서 직접 읽지 않아도 되는 값

State Flow:

```text
User Action
→ Event Handler
→ setState
→ Re-render
→ UI Update
```

주의:

- State를 직접 수정하지 않음
- setter 호출 직후 State 값이 즉시 바뀐 것처럼 읽히지 않을 수 있음
- 불필요한 State 생성 금지
- 파생 가능한 값은 Derived Value로 계산
- 여러 State가 강하게 연결되면 구조 재검토

---

### [FAQ]

Q. State가 뭐야?
A. State는 Component 내부에서 관리되는 변경 가능한 UI 데이터다.

Q. State는 언제 써?
A. 사용자 행동이나 API 응답에 따라 화면이 바뀌어야 하는 값을 State로 둔다.

Q. State를 직접 바꾸면 안 돼?
A. 안 된다. React가 변경을 감지하지 못할 수 있으므로 setter 함수를 사용해야 한다.

Q. State가 바뀌면 무슨 일이 일어나?
A. Component가 다시 렌더링되고 변경된 State 기준으로 UI가 갱신된다.

---

## 2.2 Props vs State

### [개념]

Props와 State는 React Component의 데이터를 다루는 핵심 개념이다.

Props는 부모가 자식에게 전달하는 읽기 전용 데이터다.

State는 Component 내부에서 관리되는 변경 가능한 UI 데이터다.

---

### [핵심]

Props vs State 비교:

| 비교      | Props                    | State                        |
| --------- | ------------------------ | ---------------------------- |
| 소유      | Parent Component         | Current Component            |
| 변경      | Child 직접 변경 금지     | setter로 변경                |
| 용도      | 외부 데이터 전달         | 내부 UI 상태                 |
| 방향      | Parent → Child           | Component 내부               |
| 변경 결과 | Child Re-render 가능     | Current Component Re-render  |
| 예시      | title, onClick, children | keyword, loading, selectedId |

핵심 구분:

- Props는 외부에서 들어오는 값
- State는 내부에서 바뀌는 값
- Props는 읽기 전용
- State는 setter로 변경
- Props와 State 모두 UI 렌더링에 사용 가능

---

### [실무]

Props 사용 예:

```jsx
function FestivalCard({ title }) {
  return <h2>{title}</h2>;
}
```

State 사용 예:

```jsx
function SearchBox() {
  const [keyword, setKeyword] = useState("");

  return (
    <input
      value={keyword}
      onChange={(event) => setKeyword(event.target.value)}
    />
  );
}
```

선택 기준:

```text
부모가 전달하는 값인가?
→ Props

Component 내부에서 바뀌는 값인가?
→ State

Props나 State로 계산 가능한 값인가?
→ Derived Value
```

주의:

- Props를 State로 복사하는 패턴은 신중히 사용
- 동일 데이터를 Props와 State에 중복 저장하면 불일치 가능
- Child가 Props를 변경해야 한다면 Parent Callback을 사용
- State 위치는 필요한 최소 공통 부모에 둠

---

### [FAQ]

Q. Props와 State 차이는 뭐야?
A. Props는 부모가 전달하는 읽기 전용 데이터이고 State는 Component 내부에서 변경 가능한 UI 데이터다.

Q. Props를 State에 복사해도 돼?
A. 대부분 피하는 것이 좋다. 원본 Props와 복사된 State가 불일치할 수 있다.

Q. Child에서 Parent 데이터를 바꾸려면 어떻게 해?
A. Parent가 State 변경 함수를 Callback Props로 전달하고 Child가 그 Callback을 호출한다.

---

## 2.3 State Location

### [개념]

State Location은 State를 어느 Component에 둘지 결정하는 기준이다.

State는 그 값을 실제로 사용하거나 변경해야 하는 가장 가까운 공통 부모 Component에 두는 것이 기본이다.

---

### [핵심]

State Location 핵심 키워드:

- state ownership
- nearest common parent
- lifting state up
- local state
- shared state
- props drilling
- source of truth

State 위치 기준:

- 한 Component만 사용하면 해당 Component에 둠
- 여러 Child가 공유하면 공통 Parent에 둠
- Child 이벤트로 Parent 데이터를 바꿔야 하면 Parent에 둠
- 전역 공유가 필요하면 State Management 문서로 연결
- 서버 데이터 캐싱은 Data Fetching 문서로 연결

---

### [실무]

Local State 예:

```jsx
function ToggleButton() {
  const [open, setOpen] = useState(false);

  return (
    <button type="button" onClick={() => setOpen((prev) => !prev)}>
      {open ? "Close" : "Open"}
    </button>
  );
}
```

Shared State 예:

```jsx
function FestivalPage() {
  const [selectedFestivalId, setSelectedFestivalId] = useState(null);

  return (
    <>
      <FestivalList onSelect={setSelectedFestivalId} />
      <FestivalDetail festivalId={selectedFestivalId} />
    </>
  );
}
```

Flow:

```text
Shared State Needed
→ Find Nearest Common Parent
→ Place State in Parent
→ Pass Value / Callback by Props
```

주의:

- State를 너무 위에 두면 불필요한 Re-render 증가
- State를 너무 아래에 두면 형제 Component 공유 어려움
- 중복 State는 source of truth 혼란 발생
- props drilling이 깊어지면 State Management 검토

---

### [FAQ]

Q. State는 어디에 두는 게 좋아?
A. 그 State를 사용하는 Component들의 가장 가까운 공통 부모에 두는 것이 기본이다.

Q. Lifting State Up이 뭐야?
A. 여러 Component가 공유해야 하는 State를 공통 부모 Component로 올리는 것이다.

Q. State를 무조건 최상위 App에 두면 좋아?
A. 아니다. 불필요한 Re-render와 복잡도가 증가할 수 있어 필요한 범위에만 둔다.

---

# 3. useState

## 3.1 useState Basics

### [개념]

useState는 Functional Component에서 State를 선언하고 변경하기 위한 React Hook이다.

useState는 State 값과 setter function을 배열 형태로 반환한다.

예:

```jsx
const [keyword, setKeyword] = useState("");
```

---

### [핵심]

useState 핵심 키워드:

- useState
- state value
- setter function
- initial value
- array destructuring
- functional update
- object state
- array state
- nullable state
- TypeScript generic basics

useState 기본 구조:

```jsx
const [state, setState] = useState(initialValue);
```

규칙:

- Hook은 Component 최상위에서 호출
- 조건문 내부에서 호출 금지
- 반복문 내부에서 호출 금지
- 일반 함수 내부에서 호출 금지
- setter function으로 State 변경
- setter 호출 시 Re-render 발생 가능

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

숫자 State:

```jsx
const [page, setPage] = useState(1);
```

배열 State:

```jsx
const [festivals, setFestivals] = useState([]);
```

객체 State:

```jsx
const [user, setUser] = useState({
  name: "",
  email: "",
});
```

Nullable State:

```jsx
const [selectedFestivalId, setSelectedFestivalId] = useState(null);
```

주의:

- 초기값 타입을 명확히 설정
- 빈 배열은 TypeScript에서 Generic 필요
- null 초기값은 TypeScript에서 Union Type 필요
- setter 호출 직후 기존 State가 보일 수 있음
- 이전 State 기반이면 functional update 사용

---

### [FAQ]

Q. useState는 뭐야?
A. Functional Component에서 State를 선언하고 변경하기 위한 React Hook이다.

Q. useState는 무엇을 반환해?
A. 현재 State 값과 그 값을 변경하는 setter function을 배열로 반환한다.

Q. useState는 어디서 호출해야 해?
A. React Component 최상위 또는 Custom Hook 내부에서 호출해야 한다.

Q. useState 초기값은 왜 중요해?
A. 초기값이 State 타입과 렌더링 조건에 영향을 주기 때문이다.

---

## 3.2 State Setter

### [개념]

State Setter는 useState가 반환하는 State 변경 함수다.

State Setter를 호출하면 React는 State 변경을 예약하고 Component를 다시 렌더링할 수 있다.

예:

```jsx
const [count, setCount] = useState(0);

setCount(count + 1);
```

---

### [핵심]

State Setter 핵심:

- setter function
- state update
- scheduled update
- Re-render
- asynchronous update
- functional update
- no direct mutation

State Setter 규칙:

- State는 setter로 변경
- State 직접 대입 금지
- setter 호출 직후 값이 즉시 변경된 것처럼 읽히지 않을 수 있음
- 이전 State 기반 업데이트는 functional update 사용
- 렌더링 중 setter 호출 금지

---

### [실무]

주의 예:

```jsx
function Counter() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
    console.log(count);
  }

  return <button onClick={handleClick}>{count}</button>;
}
```

주의:

- `console.log(count)`는 기존 값일 수 있음
- State 업데이트는 즉시 변수에 반영되는 단순 대입이 아님

권장:

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

금지:

```jsx
count = count + 1;
```

---

### [FAQ]

Q. setState 호출 직후 값이 바로 바뀌어?
A. React State 업데이트는 비동기적으로 처리될 수 있어 호출 직후 기존 값이 보일 수 있다.

Q. State 값을 직접 대입하면 안 돼?
A. 안 된다. React가 변경을 감지하고 렌더링할 수 있도록 setter function을 사용해야 한다.

Q. 렌더링 중 setter를 호출하면 어떻게 돼?
A. State 변경이 다시 렌더링을 유발해 무한 렌더링이 발생할 수 있다.

---

## 3.3 Functional Update

### [개념]

Functional Update는 이전 State 값을 기준으로 다음 State를 계산하는 방식이다.

이전 State에 의존하는 업데이트는 setter에 함수를 전달한다.

예:

```jsx
setCount((prevCount) => prevCount + 1);
```

---

### [핵심]

Functional Update 핵심 키워드:

- previous state
- updater function
- safe state update
- count increment
- toggle
- array update
- object update

Functional Update 사용 상황:

- 이전 count 기반 증가 / 감소
- boolean toggle
- 배열에 item 추가
- 배열에서 item 삭제
- 객체 일부 property 수정
- 연속 State 업데이트 가능성 있는 경우

---

### [실무]

숫자 증가:

```jsx
setCount((prevCount) => prevCount + 1);
```

불리언 Toggle:

```jsx
setOpen((prevOpen) => !prevOpen);
```

배열 추가:

```jsx
setFestivals((prevFestivals) => [...prevFestivals, newFestival]);
```

배열 삭제:

```jsx
setFestivals((prevFestivals) =>
  prevFestivals.filter((festival) => festival.festivalId !== targetId),
);
```

객체 업데이트:

```jsx
setUser((prevUser) => ({
  ...prevUser,
  name: "newName",
}));
```

주의:

- 이전 State를 기준으로 할 때는 functional update 우선
- 여러 번 연속 업데이트할 가능성이 있으면 functional update 권장
- 기존 배열 / 객체 직접 수정 금지
- updater function은 순수하게 작성

---

### [FAQ]

Q. 이전 State 기반 업데이트는 어떻게 해?
A. `setCount((prevCount) => prevCount + 1)`처럼 functional update를 사용한다.

Q. Toggle State는 어떻게 바꿔?
A. `setOpen((prevOpen) => !prevOpen)`처럼 이전 값을 반전한다.

Q. Functional Update는 언제 필요해?
A. 다음 State가 이전 State에 의존할 때 필요하다.

---

# 4. Array and Object State

## 4.1 Array State

### [개념]

Array State는 목록 데이터를 Component State로 관리하는 방식이다.

React에서 배열 State는 직접 수정하지 않고 새 배열을 만들어 setter에 전달해야 한다.

---

### [핵심]

Array State 핵심 키워드:

- array state
- immutable update
- spread
- map
- filter
- sort copy
- no push
- no splice
- List Rendering

배열 State 규칙:

- push 사용 금지
- splice 직접 사용 금지
- 원본 배열 sort 직접 변경 주의
- 새 배열 생성 후 setter 호출
- 추가는 spread 사용
- 삭제는 filter 사용
- 수정은 map 사용

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

삭제 예:

```jsx
setFestivals((prevFestivals) =>
  prevFestivals.filter((festival) => festival.festivalId !== targetId),
);
```

수정 예:

```jsx
setFestivals((prevFestivals) =>
  prevFestivals.map((festival) =>
    festival.festivalId === targetId
      ? { ...festival, title: "Updated Festival" }
      : festival,
  ),
);
```

정렬 예:

```jsx
const sortedFestivals = [...festivals].sort((a, b) =>
  a.title.localeCompare(b.title),
);
```

주의:

- 원본 배열 직접 mutation 금지
- sort는 원본 배열을 변경하므로 복사 후 사용
- State 배열 변경 후 key 안정성 유지
- 목록 렌더링은 List Rendering 문서와 연결

---

### [FAQ]

Q. 배열 State는 push로 바꾸면 돼?
A. 안 된다. 새 배열을 만들어 setter에 전달해야 한다.

Q. 배열 State에서 item 삭제는 어떻게 해?
A. `filter`로 새 배열을 만들어 setter에 전달한다.

Q. 배열 State에서 item 수정은 어떻게 해?
A. `map`으로 대상 item만 새 객체로 바꾸고 나머지는 유지한다.

Q. 배열 State를 sort해도 돼?
A. 원본 배열을 직접 sort하지 말고 복사한 배열을 sort해야 한다.

---

## 4.2 Object State

### [개념]

Object State는 여러 관련 값을 객체 형태로 Component State에서 관리하는 방식이다.

React에서 객체 State는 직접 수정하지 않고 새 객체를 만들어 setter에 전달해야 한다.

---

### [핵심]

Object State 핵심 키워드:

- object state
- immutable update
- spread
- property update
- nested object caution
- no direct mutation

객체 State 규칙:

- 객체 property 직접 수정 금지
- spread로 새 객체 생성
- 변경할 property만 덮어쓰기
- 중첩 객체 수정은 단계별 복사 필요
- 객체가 너무 커지면 State 분리 검토

---

### [실무]

나쁜 예:

```jsx
user.name = "newName";
setUser(user);
```

좋은 예:

```jsx
setUser((prevUser) => ({
  ...prevUser,
  name: "newName",
}));
```

Form 객체 State 예:

```jsx
const [form, setForm] = useState({
  title: "",
  region: "",
});

function handleChange(event) {
  const { name, value } = event.target;

  setForm((prevForm) => ({
    ...prevForm,
    [name]: value,
  }));
}
```

중첩 객체 주의:

```jsx
setUser((prevUser) => ({
  ...prevUser,
  profile: {
    ...prevUser.profile,
    nickname: "newNickname",
  },
}));
```

주의:

- 객체 State 직접 mutation 금지
- 중첩 객체가 깊어지면 구조 단순화 검토
- 관련 없는 값은 별도 State로 분리 가능
- 복잡한 Form은 Form Handling 문서로 연결

---

### [FAQ]

Q. 객체 State는 property만 바꾸면 돼?
A. 안 된다. 기존 객체를 직접 수정하지 말고 spread로 새 객체를 만들어야 한다.

Q. 객체 State에서 하나의 값만 바꾸려면?
A. 기존 객체를 spread로 복사하고 변경할 property만 덮어쓴다.

Q. 중첩 객체 State는 어떻게 수정해?
A. 변경 경로의 각 객체를 spread로 복사해 새 객체를 만들어야 한다.

---

# 5. Derived State

## 5.1 Derived Value

### [개념]

Derived Value는 기존 Props나 State로부터 계산 가능한 값이다.

계산 가능한 값은 별도 State로 두지 않고 렌더링 중 계산하는 것이 기본이다.

---

### [핵심]

Derived Value 핵심 키워드:

- derived value
- derived state
- avoid duplicate state
- props based calculation
- state based calculation
- render calculation
- source of truth
- memoization basics mention

핵심 규칙:

- Props로 계산 가능한 값은 State로 두지 않음
- State로 계산 가능한 값은 중복 State로 두지 않음
- 원본 데이터 하나를 source of truth로 유지
- 계산 비용이 큰 경우에만 memoization 고려
- React Core에서는 useMemo 심화 제외

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

개수 계산 예:

```jsx
const festivalCount = festivals.length;
```

주의:

- 원본 State와 파생 State 불일치 가능
- Derived Value를 State로 저장하면 동기화 코드 증가
- 계산 가능한 값은 렌더링 중 계산
- 비용이 큰 계산은 Performance 문서로 연결

---

### [FAQ]

Q. 계산 가능한 값도 State로 둬야 해?
A. 대부분 아니다. Props나 State로 계산 가능하면 렌더링 중 계산하는 것이 좋다.

Q. Derived State를 잘못 쓰면 어떤 문제가 생겨?
A. 원본 값과 파생 값이 서로 불일치하는 버그가 생길 수 있다.

Q. fullName 같은 값은 State로 둬야 해?
A. firstName과 lastName으로 계산 가능하면 별도 State로 두지 않는 것이 좋다.

---

## 5.2 Source of Truth

### [개념]

Source of Truth는 특정 데이터의 기준이 되는 원본 상태를 의미한다.

React에서는 동일한 값을 여러 State에 중복 저장하지 않고 하나의 원본 State에서 필요한 값을 계산하는 것이 좋다.

---

### [핵심]

Source of Truth 핵심 키워드:

- source of truth
- duplicate state
- derived value
- state synchronization
- single data owner
- predictable UI

규칙:

- 하나의 데이터는 하나의 원본에서 관리
- 중복 State 저장 최소화
- Props와 State 중복 복사 주의
- 원본 State 변경 시 파생 값은 계산으로 처리
- 데이터 소유 Component를 명확히 함

---

### [실무]

나쁜 예:

```jsx
const [festivals, setFestivals] = useState([]);
const [festivalCount, setFestivalCount] = useState(0);
```

좋은 예:

```jsx
const [festivals, setFestivals] = useState([]);
const festivalCount = festivals.length;
```

선택된 item 계산 예:

```jsx
const selectedFestival = festivals.find(
  (festival) => festival.festivalId === selectedFestivalId,
);
```

주의:

- 데이터 중복 저장은 동기화 버그를 만든다
- API 응답 원본과 화면용 파생 값을 분리할 때 기준 명확화
- 서버 데이터 캐싱은 Data Fetching 문서에서 다룸
- 전역 source of truth는 State Management 문서에서 다룸

---

### [FAQ]

Q. Source of Truth가 뭐야?
A. 특정 데이터의 기준이 되는 원본 상태를 의미한다.

Q. 같은 값을 여러 State에 저장하면 안 돼?
A. 동기화 불일치가 생길 수 있어 가능하면 하나의 원본 State에서 계산하는 것이 좋다.

Q. 선택된 객체를 State로 저장해야 해?
A. 보통 selectedId만 State로 두고 객체는 목록에서 계산하는 방식이 더 안전하다.

---

# 6. Common Mistakes

## 6.1 Props Mistakes

### [개념]

Props 실수는 Props 직접 수정, Props와 State 혼동, Callback Props 즉시 실행, Props 과다 전달에서 자주 발생한다.

---

### [핵심]

Props Common Mistakes:

- Props 직접 수정
- Props를 무조건 State로 복사
- Callback Props 즉시 실행
- Props 이름 불명확
- Props 개수 과다
- Child에서 Parent State 직접 변경 시도
- key를 Component 내부 Props로 받으려 함
- children과 일반 Props 역할 혼동

---

### [실무]

나쁜 예:

```jsx
function FestivalCard({ title }) {
  title = "Changed Title";

  return <h2>{title}</h2>;
}
```

개선:

```jsx
function FestivalCard({ title, onChangeTitle }) {
  return (
    <article>
      <h2>{title}</h2>
      <button type="button" onClick={onChangeTitle}>
        Change
      </button>
    </article>
  );
}
```

Callback 즉시 실행 문제:

```jsx
<button onClick={onSelect(festivalId)}>Select</button>
```

개선:

```jsx
<button type="button" onClick={() => onSelect(festivalId)}>
  Select
</button>
```

---

### [FAQ]

Q. Props를 직접 바꾸면 왜 안 돼?
A. Props는 부모가 소유한 읽기 전용 데이터라 Child에서 직접 변경하면 React 데이터 흐름이 깨진다.

Q. Callback Props가 바로 실행되는 이유는?
A. `onClick={onSelect(id)}`처럼 함수 호출 결과를 전달했기 때문이다. 클릭 시 실행하려면 함수로 감싸야 한다.

Q. key를 Props로 받을 수 있어?
A. key는 React 내부 특수 값이라 Component 내부에서 props로 받을 수 없다. 필요하면 별도 prop으로 전달해야 한다.

---

## 6.2 State Mistakes

### [개념]

State 실수는 State 직접 변경, 배열 / 객체 mutation, 불필요한 중복 State, 렌더링 중 setter 호출에서 자주 발생한다.

---

### [핵심]

State Common Mistakes:

- State 직접 변경
- 배열 State에 push 사용
- 객체 State property 직접 수정
- 원본 배열 sort 직접 실행
- setState 직후 값이 즉시 바뀐다고 오해
- 이전 State 기반 업데이트에 일반 setter 사용
- Derived Value를 State로 중복 저장
- 렌더링 중 setState 호출
- 모든 값을 State로 저장
- State를 너무 위 또는 너무 아래에 배치

---

### [실무]

State 직접 변경 문제:

```jsx
festivals.push(newFestival);
setFestivals(festivals);
```

개선:

```jsx
setFestivals((prevFestivals) => [...prevFestivals, newFestival]);
```

렌더링 중 setter 호출 문제:

```jsx
function BadComponent() {
  const [count, setCount] = useState(0);

  setCount(count + 1);

  return <p>{count}</p>;
}
```

개선:

```jsx
function GoodComponent() {
  const [count, setCount] = useState(0);

  return (
    <button type="button" onClick={() => setCount((prev) => prev + 1)}>
      {count}
    </button>
  );
}
```

Debug Flow:

```text
UI Update Problem
→ State Setter 사용 여부 확인
→ Direct Mutation 여부 확인
→ Functional Update 필요 여부 확인
→ Derived State 중복 여부 확인
→ State 위치 확인
```

---

### [FAQ]

Q. State 직접 변경하면 어떤 문제가 생겨?
A. React가 변경을 감지하지 못해 화면이 업데이트되지 않거나 예측하기 어려운 버그가 생길 수 있다.

Q. Too many re-renders 오류는 왜 나?
A. 렌더링 중 State를 변경하거나 Event Handler를 잘못 전달해 렌더링마다 setState가 호출될 때 발생한다.

Q. 모든 값을 State로 두면 안 돼?
A. 계산 가능한 값까지 State로 두면 중복과 동기화 문제가 생길 수 있다.

---

# 7. Checklist

## 7.1 Part02 Quality Checklist

### [개념]

React Core Part02 검수는 Props, State, useState, 배열 / 객체 State, Derived Value를 기준으로 수행한다.

---

### [핵심]

Checklist:

```md
- [ ] Props 기본 개념이 포함되었는가?
- [ ] Props가 Parent → Child 방향임을 설명했는가?
- [ ] Props 읽기 전용 규칙이 포함되었는가?
- [ ] Props Destructuring이 포함되었는가?
- [ ] Callback Props가 포함되었는가?
- [ ] children 설명이 포함되었는가?
- [ ] State 기본 개념이 포함되었는가?
- [ ] State 변경 시 Re-render 설명이 포함되었는가?
- [ ] Props vs State 비교가 포함되었는가?
- [ ] State Location 기준이 포함되었는가?
- [ ] useState 기본 구조가 포함되었는가?
- [ ] State Setter 설명이 포함되었는가?
- [ ] Functional Update가 포함되었는가?
- [ ] Array State immutable update가 포함되었는가?
- [ ] Object State immutable update가 포함되었는가?
- [ ] Derived Value와 Source of Truth가 포함되었는가?
- [ ] Common Mistakes가 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 Flow:

```text
Draft
→ MASTER_RAG_RULES Section Check
→ React Core Domain Scope Check
→ Props Rule Check
→ State Rule Check
→ useState Rule Check
→ Immutable Update Check
→ Derived State Check
→ Common Mistakes Check
→ FAQ Check
→ Retrieval Queries Check
→ Final Review
```

치명적 문제 기준:

- Props 직접 수정 허용처럼 설명
- State 직접 변경 허용처럼 설명
- useState를 조건문 내부에서 호출하는 예제
- 배열 State push 예제를 정상 예제로 제공
- 객체 State 직접 수정 예제를 정상 예제로 제공
- Derived Value를 무조건 State로 두라고 설명
- FAQ 누락
- Retrieval Queries 누락

---

### [FAQ]

Q. Part02에서 가장 중요한 검수 기준은?
A. Props 읽기 전용, State setter 변경, useState, functional update, immutable update, Derived Value 포함 여부다.

Q. Part02에서 다루면 안 되는 내용은?
A. 전역 상태관리, Redux, Zustand, TanStack Query, React Hook Form, useReducer 심화는 제외한다.

---

# Retrieval Queries

### [FAQ]

Q. Props가 뭐야?
A. Props는 부모 Component가 자식 Component에 전달하는 읽기 전용 데이터다.

Q. Props는 어느 방향으로 전달돼?
A. 부모 Component에서 자식 Component로 전달된다.

Q. Props는 수정해도 돼?
A. 안 된다. Props는 읽기 전용이다. 변경이 필요하면 부모 State를 변경하는 callback을 전달한다.

Q. Props로 함수도 전달할 수 있어?
A. 가능하다. 자식에서 발생한 이벤트를 부모에게 알릴 때 callback props를 자주 사용한다.

Q. Props Destructuring은 왜 써?
A. `props.title`처럼 반복 접근하지 않고 필요한 값을 명확하게 사용할 수 있기 때문이다.

Q. Props 기본값은 어떻게 줘?
A. 구조 분해 할당에서 `type = "button"`처럼 기본값을 설정할 수 있다.

Q. Props가 너무 많으면 어떻게 해?
A. Component 책임을 분리하거나 관련 데이터를 객체로 묶을지 검토한다.

Q. Callback Props가 뭐야?
A. 부모가 자식에게 전달하는 함수 Props이며 자식 이벤트를 부모에게 알릴 때 사용한다.

Q. 자식 Component가 부모 State를 직접 바꿀 수 있어?
A. 직접 바꾸지 않는다. 부모가 전달한 Callback Props를 호출해 부모가 State를 변경하게 한다.

Q. onClick에서 Callback에 인자를 넘기려면 어떻게 해?
A. `onClick={() => onSelect(id)}`처럼 함수로 감싸서 전달한다.

Q. children은 언제 써?
A. Component 내부 내용을 외부에서 자유롭게 조합해야 할 때 사용한다.

Q. children과 props 차이는?
A. children은 태그 사이에 전달되는 특별한 props이고, 일반 props는 속성 형태로 전달된다.

Q. State가 뭐야?
A. State는 Component 내부에서 관리되는 변경 가능한 UI 데이터다.

Q. State는 언제 써?
A. 사용자 행동이나 API 응답에 따라 화면이 바뀌어야 하는 값을 State로 둔다.

Q. State를 직접 바꾸면 안 돼?
A. 안 된다. React가 변경을 감지하지 못할 수 있으므로 setter 함수를 사용해야 한다.

Q. State가 바뀌면 무슨 일이 일어나?
A. Component가 다시 렌더링되고 변경된 State 기준으로 UI가 갱신된다.

Q. Props와 State 차이는 뭐야?
A. Props는 부모가 전달하는 읽기 전용 데이터이고 State는 Component 내부에서 변경 가능한 UI 데이터다.

Q. Props를 State에 복사해도 돼?
A. 대부분 피하는 것이 좋다. 원본 Props와 복사된 State가 불일치할 수 있다.

Q. Child에서 Parent 데이터를 바꾸려면 어떻게 해?
A. Parent가 State 변경 함수를 Callback Props로 전달하고 Child가 그 Callback을 호출한다.

Q. State는 어디에 두는 게 좋아?
A. 그 State를 사용하는 Component들의 가장 가까운 공통 부모에 두는 것이 기본이다.

Q. Lifting State Up이 뭐야?
A. 여러 Component가 공유해야 하는 State를 공통 부모 Component로 올리는 것이다.

Q. State를 무조건 최상위 App에 두면 좋아?
A. 아니다. 불필요한 Re-render와 복잡도가 증가할 수 있어 필요한 범위에만 둔다.

Q. useState는 뭐야?
A. Functional Component에서 State를 선언하고 변경하기 위한 React Hook이다.

Q. useState는 무엇을 반환해?
A. 현재 State 값과 그 값을 변경하는 setter function을 배열로 반환한다.

Q. useState는 어디서 호출해야 해?
A. React Component 최상위 또는 Custom Hook 내부에서 호출해야 한다.

Q. useState 초기값은 왜 중요해?
A. 초기값이 State 타입과 렌더링 조건에 영향을 주기 때문이다.

Q. setState 호출 직후 값이 바로 바뀌어?
A. React State 업데이트는 비동기적으로 처리될 수 있어 호출 직후 기존 값이 보일 수 있다.

Q. State 값을 직접 대입하면 안 돼?
A. 안 된다. React가 변경을 감지하고 렌더링할 수 있도록 setter function을 사용해야 한다.

Q. 렌더링 중 setter를 호출하면 어떻게 돼?
A. State 변경이 다시 렌더링을 유발해 무한 렌더링이 발생할 수 있다.

Q. 이전 State 기반 업데이트는 어떻게 해?
A. `setCount((prevCount) => prevCount + 1)`처럼 functional update를 사용한다.

Q. Toggle State는 어떻게 바꿔?
A. `setOpen((prevOpen) => !prevOpen)`처럼 이전 값을 반전한다.

Q. Functional Update는 언제 필요해?
A. 다음 State가 이전 State에 의존할 때 필요하다.

Q. 배열 State는 push로 바꾸면 돼?
A. 안 된다. 새 배열을 만들어 setter에 전달해야 한다.

Q. 배열 State에서 item 삭제는 어떻게 해?
A. `filter`로 새 배열을 만들어 setter에 전달한다.

Q. 배열 State에서 item 수정은 어떻게 해?
A. `map`으로 대상 item만 새 객체로 바꾸고 나머지는 유지한다.

Q. 배열 State를 sort해도 돼?
A. 원본 배열을 직접 sort하지 말고 복사한 배열을 sort해야 한다.

Q. 객체 State는 property만 바꾸면 돼?
A. 안 된다. 기존 객체를 직접 수정하지 말고 spread로 새 객체를 만들어야 한다.

Q. 객체 State에서 하나의 값만 바꾸려면?
A. 기존 객체를 spread로 복사하고 변경할 property만 덮어쓴다.

Q. 중첩 객체 State는 어떻게 수정해?
A. 변경 경로의 각 객체를 spread로 복사해 새 객체를 만들어야 한다.

Q. 계산 가능한 값도 State로 둬야 해?
A. 대부분 아니다. Props나 State로 계산 가능하면 렌더링 중 계산하는 것이 좋다.

Q. Derived State를 잘못 쓰면 어떤 문제가 생겨?
A. 원본 값과 파생 값이 서로 불일치하는 버그가 생길 수 있다.

Q. Source of Truth가 뭐야?
A. 특정 데이터의 기준이 되는 원본 상태를 의미한다.

Q. 같은 값을 여러 State에 저장하면 안 돼?
A. 동기화 불일치가 생길 수 있어 가능하면 하나의 원본 State에서 계산하는 것이 좋다.

Q. 선택된 객체를 State로 저장해야 해?
A. 보통 selectedId만 State로 두고 객체는 목록에서 계산하는 방식이 더 안전하다.

Q. Props를 직접 바꾸면 왜 안 돼?
A. Props는 부모가 소유한 읽기 전용 데이터라 Child에서 직접 변경하면 React 데이터 흐름이 깨진다.

Q. Callback Props가 바로 실행되는 이유는?
A. `onClick={onSelect(id)}`처럼 함수 호출 결과를 전달했기 때문이다. 클릭 시 실행하려면 함수로 감싸야 한다.

Q. key를 Props로 받을 수 있어?
A. key는 React 내부 특수 값이라 Component 내부에서 props로 받을 수 없다. 필요하면 별도 prop으로 전달해야 한다.

Q. State 직접 변경하면 어떤 문제가 생겨?
A. React가 변경을 감지하지 못해 화면이 업데이트되지 않거나 예측하기 어려운 버그가 생길 수 있다.

Q. Too many re-renders 오류는 왜 나?
A. 렌더링 중 State를 변경하거나 Event Handler를 잘못 전달해 렌더링마다 setState가 호출될 때 발생한다.

Q. 모든 값을 State로 두면 안 돼?
A. 계산 가능한 값까지 State로 두면 중복과 동기화 문제가 생길 수 있다.

Q. React Core Part02 다음 문서는 뭐가 좋아?
A. Event Handling, Controlled Input, Conditional Rendering을 다루는 React Core Part03으로 이어지는 것이 좋다.
