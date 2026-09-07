# React Core Part03 - Event Handling, Controlled Input, Conditional Rendering

---

# 1. Event Handling

## 1.1 React Event Handling

### [개념]

React Event Handling은 사용자 행동에 반응해 함수를 실행하는 방식이다.

React에서는 HTML 이벤트 속성과 비슷한 이름을 사용하지만 camelCase로 작성한다.

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

React Event Handling은 State 변경, Callback Props 호출, Form 처리, UI 전환의 시작점이다.

---

### [핵심]

Event Handling 핵심 키워드:

- Event Handling
- onClick
- onChange
- onSubmit
- onKeyDown
- event object
- preventDefault
- handler function
- callback props
- React Synthetic Event
- State Update
- User Action

핵심 규칙:

- 이벤트 이름은 camelCase 사용
- 이벤트에는 함수 참조 전달
- `onClick={handleClick}` 권장
- `onClick={handleClick()}` 즉시 실행 주의
- Component 내부 Handler는 `handle` prefix 권장
- Props Callback은 `on` prefix 권장
- Form Submit에는 preventDefault 고려
- Event Handler에서 State 변경 가능
- Event Handler에서 Callback Props 호출 가능

---

### [실무]

Click Event 예:

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

인자가 필요한 Event Handler 예:

```jsx
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

Event Flow:

```text
User Action
→ Event Handler
→ State Update or Callback Props
→ Re-render
→ UI Update
```

주의:

- `onClick={handleClick()}`는 렌더링 중 즉시 실행
- 인자가 필요하면 arrow function 사용
- 이벤트 로직이 길어지면 별도 함수로 분리
- DOM 직접 조작보다 State 변경 우선
- 비동기 요청 심화는 Data Fetching 문서로 연결

---

### [FAQ]

Q. React Event Handling은 어떻게 해?
A. onClick, onChange, onSubmit 같은 props에 Event Handler 함수를 전달한다.

Q. onClick={handleClick()}가 왜 문제야?
A. 렌더링 중 함수가 즉시 실행된다. 클릭 시 실행하려면 `onClick={handleClick}`처럼 함수 참조를 전달해야 한다.

Q. onClick에서 인자를 넘기려면 어떻게 해?
A. `onClick={() => handleClick(id)}`처럼 함수로 감싸서 전달한다.

Q. handler 이름은 어떻게 짓는 게 좋아?
A. Component 내부 함수는 handleSubmit, handleClick처럼 짓고 props callback은 onSubmit, onClick처럼 짓는 방식이 흔하다.

---

## 1.2 Event Object

### [개념]

Event Object는 이벤트가 발생했을 때 React가 Handler에 전달하는 이벤트 정보 객체다.

Event Object를 사용하면 입력값, 키 입력, 기본 동작 제어, 이벤트 대상 등을 확인할 수 있다.

예:

```jsx
function SearchInput() {
  function handleChange(event) {
    console.log(event.target.value);
  }

  return <input onChange={handleChange} />;
}
```

---

### [핵심]

Event Object 핵심 키워드:

- event object
- event.target
- event.currentTarget
- event.target.value
- event.preventDefault
- event.stopPropagation
- React Synthetic Event
- input change event
- form submit event

핵심 사용:

- input 값 읽기
- form submit 기본 동작 막기
- key 값 확인
- checkbox checked 값 확인
- select value 확인
- 이벤트 전파 제어

---

### [실무]

Input Change 예:

```jsx
function SearchInput() {
  const [keyword, setKeyword] = useState("");

  function handleChange(event) {
    setKeyword(event.target.value);
  }

  return <input value={keyword} onChange={handleChange} />;
}
```

Checkbox Change 예:

```jsx
function AgreeCheckbox() {
  const [checked, setChecked] = useState(false);

  function handleChange(event) {
    setChecked(event.target.checked);
  }

  return <input type="checkbox" checked={checked} onChange={handleChange} />;
}
```

Key Event 예:

```jsx
function SearchBox({ onSearch }) {
  function handleKeyDown(event) {
    if (event.key === "Enter") {
      onSearch();
    }
  }

  return <input onKeyDown={handleKeyDown} />;
}
```

주의:

- input text 값은 `event.target.value`
- checkbox 값은 `event.target.checked`
- form submit 기본 동작은 preventDefault로 제어
- Event Object를 비동기 코드에서 오래 보관하는 패턴은 지양
- TypeScript에서는 Element Type에 맞는 Event Type 사용

---

### [FAQ]

Q. React event object는 뭐야?
A. 이벤트가 발생했을 때 React가 Handler에 전달하는 이벤트 정보 객체다.

Q. input 입력값은 어디서 읽어?
A. `event.target.value`에서 읽는다.

Q. checkbox 체크 여부는 어디서 읽어?
A. `event.target.checked`에서 읽는다.

Q. event.target과 event.currentTarget 차이는?
A. target은 실제 이벤트가 발생한 요소이고 currentTarget은 Handler가 연결된 요소다.

---

## 1.3 Form Submit Event

### [개념]

Form Submit Event는 사용자가 form을 제출했을 때 발생하는 이벤트다.

React에서는 form submit 시 브라우저 기본 새로고침을 막고 JavaScript 로직으로 제출 처리를 하는 경우가 많다.

예:

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

---

### [핵심]

Form Submit 핵심 키워드:

- onSubmit
- form event
- preventDefault
- submit button
- validation
- controlled input
- form state
- error state
- reset

핵심 규칙:

- form에는 onSubmit 사용
- submit button에는 `type="submit"` 사용
- 일반 button에는 `type="button"` 명시
- submit 기본 새로고침은 preventDefault로 차단
- 검증 후 submit 로직 실행
- 입력값은 State로 관리 가능
- 제출 후 필요 시 reset 처리

---

### [실무]

Search Form 예:

```jsx
function SearchForm({ onSearch }) {
  const [keyword, setKeyword] = useState("");

  function handleSubmit(event) {
    event.preventDefault();

    const trimmedKeyword = keyword.trim();

    if (!trimmedKeyword) {
      return;
    }

    onSearch(trimmedKeyword);
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

Reset 예:

```jsx
function handleSubmit(event) {
  event.preventDefault();

  onSearch(keyword.trim());
  setKeyword("");
}
```

주의:

- form 내부 일반 버튼은 `type="button"` 명시
- submit 로직과 validation 로직 분리 가능
- 빈 문자열 처리 필요
- API 요청은 Event Handler에서 직접 수행 가능
- 복잡한 Form은 Form Handling Validation 문서로 연결

---

### [FAQ]

Q. React에서 event.preventDefault는 언제 써?
A. form 제출 시 페이지 새로고침 같은 기본 동작을 막을 때 사용한다.

Q. form 제출은 button onClick으로 처리해도 돼?
A. 가능하지만 form 구조에서는 onSubmit을 사용하는 것이 Enter 입력과 접근성 측면에서 더 적절하다.

Q. form 안의 button type은 왜 명시해?
A. 기본 type이 submit일 수 있어 의도치 않은 form 제출을 막기 위해 일반 버튼은 `type="button"`을 명시한다.

---

# 2. Controlled Input

## 2.1 Controlled Input Basics

### [개념]

Controlled Input은 input value를 React State로 제어하는 방식이다.

Controlled Input에서는 화면의 입력값과 React State가 같은 값을 기준으로 움직인다.

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

Controlled Input 핵심 키워드:

- Controlled Input
- Controlled Component
- value
- onChange
- State
- input value
- form state
- validation
- reset
- single source of truth

핵심 규칙:

- input value는 State로 관리
- onChange에서 State 변경
- value와 onChange를 함께 사용
- 초기값은 빈 문자열 권장
- 입력값 검증 가능
- 제출 후 reset 가능
- State가 input의 Source of Truth

---

### [실무]

Controlled Input Flow:

```text
User Input
→ onChange
→ setState
→ Re-render
→ input value update
```

기본 예:

```jsx
function SearchForm() {
  const [keyword, setKeyword] = useState("");

  function handleChange(event) {
    setKeyword(event.target.value);
  }

  return (
    <input
      value={keyword}
      onChange={handleChange}
      placeholder="Search festival"
    />
  );
}
```

주의:

- value만 있고 onChange가 없으면 읽기 전용처럼 동작
- 초기값이 undefined 또는 null이면 controlled/uncontrolled warning 가능
- 문자열 input 초기값은 `""` 권장
- 숫자 입력도 event.target.value는 문자열로 들어옴
- 복잡한 Form 상태는 Form Handling 문서로 연결

---

### [FAQ]

Q. Controlled Input이 뭐야?
A. input 값을 DOM이 아니라 React State로 관리하는 방식이다.

Q. input에 value만 넣고 onChange를 안 넣으면?
A. 사용자가 값을 변경할 수 없는 읽기 전용 input처럼 동작할 수 있다.

Q. Controlled Input의 기준 데이터는 뭐야?
A. React State가 기준 데이터다.

Q. input 초기값은 어떻게 두는 게 좋아?
A. 문자열 input은 빈 문자열 `""`로 시작하는 것이 일반적이다.

---

## 2.2 Controlled Form State

### [개념]

Controlled Form State는 여러 입력값을 React State로 관리하는 방식이다.

간단한 Form은 각각의 State를 사용할 수 있고, 관련 입력값이 많으면 객체 State로 묶을 수 있다.

---

### [핵심]

Controlled Form State 핵심 키워드:

- form state
- input state
- object state
- name attribute
- computed property name
- validation
- submit
- reset

Form State 방식:

- 단일 input: 개별 State 사용
- 여러 input: 객체 State 사용 가능
- checkbox: checked 사용
- select: value 사용
- textarea: value 사용
- submit 시 State 값 사용

---

### [실무]

개별 State 예:

```jsx
function LoginForm() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  return (
    <form>
      <input value={email} onChange={(event) => setEmail(event.target.value)} />
      <input
        type="password"
        value={password}
        onChange={(event) => setPassword(event.target.value)}
      />
    </form>
  );
}
```

객체 State 예:

```jsx
function FestivalForm() {
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

  return (
    <form>
      <input name="title" value={form.title} onChange={handleChange} />
      <input name="region" value={form.region} onChange={handleChange} />
    </form>
  );
}
```

Reset 예:

```jsx
setForm({
  title: "",
  region: "",
});
```

주의:

- input name과 State property 이름 일치 필요
- 객체 State 직접 수정 금지
- checkbox는 value가 아니라 checked 사용
- Form 검증은 submit 전 수행
- 복잡한 검증은 Form Handling Validation 문서로 분리

---

### [FAQ]

Q. Form 입력값은 State 하나씩 만들어야 해?
A. 입력값이 적으면 개별 State를 사용하고, 관련 입력값이 많으면 객체 State로 묶을 수 있다.

Q. 객체 Form State에서 input 값을 어떻게 바꿔?
A. input name을 기준으로 `[name]: value` 형태로 새 객체를 만들어 setter에 전달한다.

Q. checkbox는 value로 제어해?
A. 아니다. checkbox는 checked와 onChange로 제어한다.

---

## 2.3 Controlled vs Uncontrolled Input

### [개념]

Controlled Input은 React State가 입력값을 제어하는 방식이다.

Uncontrolled Input은 DOM 자체가 입력값을 관리하고 필요할 때 ref 등으로 값을 읽는 방식이다.

React Core에서는 Controlled Input을 기본 패턴으로 다룬다.

---

### [핵심]

Controlled vs Uncontrolled 비교:

| 비교            | Controlled Input      | Uncontrolled Input                   |
| --------------- | --------------------- | ------------------------------------ |
| 값 관리         | React State           | DOM                                  |
| 접근 방식       | value + onChange      | ref                                  |
| 검증            | 실시간 검증 쉬움      | 제출 시 읽기 쉬움                    |
| UI 동기화       | React 기준            | DOM 기준                             |
| 권장 상황       | 일반 Form, 검색, 필터 | 단순 파일 입력, 간단한 외부 DOM 연동 |
| React Core 기준 | 기본 패턴             | 기초 언급만                          |

핵심 구분:

- Controlled Input은 State 기반
- Uncontrolled Input은 DOM 기반
- React Form 기본은 Controlled Input
- file input은 Uncontrolled 성격이 강함

---

### [실무]

Controlled Input 예:

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

Uncontrolled Input 기초 예:

```jsx
function SearchInput() {
  const inputRef = useRef(null);

  function handleSubmit() {
    console.log(inputRef.current.value);
  }

  return (
    <>
      <input ref={inputRef} />
      <button type="button" onClick={handleSubmit}>
        Submit
      </button>
    </>
  );
}
```

주의:

- React Core 문서는 Controlled Input 중심
- ref 기반 Form 관리는 심화하지 않음
- file input은 보통 DOM 값 직접 제어가 제한됨
- Form 라이브러리 심화는 Form Handling Validation 문서로 연결

---

### [FAQ]

Q. Controlled Input과 Uncontrolled Input 차이는?
A. Controlled Input은 React State가 값을 관리하고 Uncontrolled Input은 DOM이 값을 관리한다.

Q. React에서는 어떤 input 방식을 기본으로 써?
A. 일반적인 Form 입력은 Controlled Input을 기본으로 사용한다.

Q. file input도 Controlled로 관리해?
A. file input은 브라우저 보안 제약 때문에 보통 Uncontrolled 성격으로 다룬다.

---

# 3. Conditional Rendering

## 3.1 Conditional Rendering Basics

### [개념]

Conditional Rendering은 조건에 따라 다른 UI를 렌더링하는 방식이다.

React에서는 State, Props, API 응답 상태에 따라 loading, error, empty, success UI를 분리할 수 있다.

---

### [핵심]

Conditional Rendering 핵심 키워드:

- Conditional Rendering
- if outside JSX
- early return
- ternary operator
- logical AND
- null return
- loading state
- error state
- empty state
- success state

조건부 렌더링 방식:

- return 이전 if
- early return
- ternary operator
- logical AND
- null return
- 변수에 JSX 저장
- Component 분리

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
        <li key={festival.festivalId}>{festival.title}</li>
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

Logical AND 예:

```jsx
{
  imageUrl && <img src={imageUrl} alt={title} />;
}
```

null return 예:

```jsx
function AdminPanel({ isAdmin }) {
  if (!isAdmin) {
    return null;
  }

  return <section>Admin Panel</section>;
}
```

주의:

- 복잡한 조건은 JSX 밖에서 분리
- `0 && <Component />`는 0이 렌더링될 수 있음
- loading / error / empty / success 상태 분리
- 조건이 많으면 함수 또는 Component 분리
- CSS display none과 Conditional Rendering은 목적이 다름

---

### [FAQ]

Q. React 조건부 렌더링은 어떻게 해?
A. early return, 삼항 연산자, logical AND, null return 등을 사용한다.

Q. React에서 if문은 어디에 써?
A. JSX 내부에 직접 쓰지 않고 return 전에 early return하거나 변수로 계산해 사용한다.

Q. && 조건부 렌더링은 언제 조심해야 해?
A. 왼쪽 값이 0이면 0이 화면에 렌더링될 수 있어 주의해야 한다.

Q. 조건이 많아지면 어떻게 해?
A. 조건별 Component를 분리하거나 return 전에 명확한 변수로 계산한다.

---

## 3.2 Loading Error Empty Success UI

### [개념]

Loading / Error / Empty / Success UI는 비동기 데이터 화면에서 상태별로 다른 UI를 제공하는 조건부 렌더링 패턴이다.

API 기반 React 화면에서는 데이터가 없거나 로딩 중이거나 실패한 상태를 명확히 분리해야 한다.

---

### [핵심]

상태 키워드:

- loading state
- error state
- empty state
- success state
- data state
- API response
- conditional UI
- user feedback

상태 구분:

| 상태    | 의미         | UI 예            |
| ------- | ------------ | ---------------- |
| loading | 요청 진행 중 | Loading...       |
| error   | 요청 실패    | Failed to load   |
| empty   | 데이터 없음  | No data          |
| success | 데이터 있음  | List / Detail UI |

---

### [실무]

상태 분리 예:

```jsx
function FestivalSection({ loading, error, festivals }) {
  if (loading) {
    return <p>Loading festivals...</p>;
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

권장 Flow:

```text
API Request
→ loading true
→ success: data set
→ failure: error set
→ loading false
→ Conditional Rendering
```

주의:

- loading과 empty를 혼동하지 않음
- error가 있는데 empty UI를 보여주지 않음
- 초기 데이터 타입을 렌더링에 안전하게 설정
- 배열 데이터 초기값은 `[]` 권장
- null 데이터 접근 전 조건 확인

---

### [FAQ]

Q. loading, error, empty 상태를 분리해야 해?
A. 분리하는 것이 좋다. 비동기 UI 상태를 명확하게 관리할 수 있다.

Q. empty UI는 언제 보여줘?
A. 요청은 성공했지만 렌더링할 데이터가 없을 때 보여준다.

Q. error UI와 empty UI 차이는 뭐야?
A. error는 요청 실패 상태이고 empty는 요청 성공 후 데이터가 없는 상태다.

Q. 초기 배열 State는 왜 []로 두는 게 좋아?
A. map이나 length 같은 배열 메서드를 안전하게 사용할 수 있기 때문이다.

---

## 3.3 Conditional Rendering vs CSS Hide

### [개념]

Conditional Rendering은 조건에 따라 Component를 렌더링하지 않는 방식이다.

CSS Hide는 Component를 렌더링하지만 CSS로 화면에서 숨기는 방식이다.

---

### [핵심]

Conditional Rendering vs CSS Hide 비교:

| 비교       | Conditional Rendering                | CSS Hide                             |
| ---------- | ------------------------------------ | ------------------------------------ |
| DOM 존재   | 조건이 false면 없음                  | DOM에 존재                           |
| State 유지 | unmount 시 내부 State 사라질 수 있음 | 내부 State 유지 가능                 |
| 접근성     | 숨김 여부 명확히 설계 필요           | aria-hidden 등 고려 필요             |
| 성능       | 불필요한 렌더링 줄일 수 있음         | 렌더링은 유지                        |
| 용도       | 권한, 상태별 UI, 조건별 화면         | 애니메이션, 토글 표시, 레이아웃 유지 |

핵심 구분:

- 아예 필요 없는 UI는 Conditional Rendering
- 숨기지만 상태 유지가 필요하면 CSS Hide 고려
- 접근성 처리는 별도 고려
- Modal / Dropdown은 목적에 따라 선택

---

### [실무]

Conditional Rendering 예:

```jsx
{
  isOpen && <Modal />;
}
```

CSS Hide 예:

```jsx
<div className={isOpen ? "modal open" : "modal hidden"}>Modal Content</div>
```

선택 기준:

```text
조건이 false일 때 DOM에서 제거해야 하는가?
→ Conditional Rendering

DOM은 유지하고 표시만 바꿔야 하는가?
→ CSS Hide
```

주의:

- Conditional Rendering은 Component unmount 가능
- CSS Hide는 DOM과 내부 State가 유지될 수 있음
- 접근성 속성 aria-hidden, focus 관리 고려
- UI Component Pattern 문서와 연결 가능

---

### [FAQ]

Q. Conditional Rendering과 CSS Hide 차이는?
A. Conditional Rendering은 조건에 따라 DOM에 렌더링하지 않고 CSS Hide는 렌더링 후 화면에서 숨긴다.

Q. Modal은 조건부 렌더링이 좋아?
A. 단순 Modal은 조건부 렌더링이 흔하지만 애니메이션이나 상태 유지가 필요하면 CSS Hide도 고려한다.

Q. 숨긴 Component의 State를 유지하려면?
A. DOM에 남겨두는 CSS Hide 방식이나 상위 State 관리 방식을 검토한다.

---

# 4. Event and Conditional Rendering Integration

## 4.1 Event Driven UI Change

### [개념]

Event Driven UI Change는 사용자 이벤트로 State를 변경하고, 변경된 State에 따라 UI를 조건부 렌더링하는 흐름이다.

React의 기본 화면 변화는 Event → State Update → Conditional Rendering 구조로 처리한다.

---

### [핵심]

Event Driven UI 핵심 키워드:

- user event
- event handler
- state update
- conditional rendering
- toggle UI
- selected item
- modal open
- tab change
- filter condition

기본 Flow:

```text
User Event
→ Event Handler
→ setState
→ Re-render
→ Conditional UI
```

---

### [실무]

Toggle UI 예:

```jsx
function NoticeToggle() {
  const [open, setOpen] = useState(false);

  function handleToggle() {
    setOpen((prevOpen) => !prevOpen);
  }

  return (
    <section>
      <button type="button" onClick={handleToggle}>
        Toggle Notice
      </button>

      {open && <p>Notice Content</p>}
    </section>
  );
}
```

Selected Item 예:

```jsx
function FestivalSelector({ festivals }) {
  const [selectedFestivalId, setSelectedFestivalId] = useState(null);

  const selectedFestival = festivals.find(
    (festival) => festival.festivalId === selectedFestivalId,
  );

  return (
    <section>
      {festivals.map((festival) => (
        <button
          key={festival.festivalId}
          type="button"
          onClick={() => setSelectedFestivalId(festival.festivalId)}
        >
          {festival.title}
        </button>
      ))}

      {selectedFestival && <p>{selectedFestival.title}</p>}
    </section>
  );
}
```

주의:

- 이벤트에서 DOM을 직접 숨기지 않음
- State를 변경하고 UI는 State 기준으로 렌더링
- 선택된 객체 전체보다 selectedId 저장이 안전한 경우가 많음
- 계산 가능한 selected object는 Derived Value로 처리

---

### [FAQ]

Q. 버튼 클릭으로 화면을 바꾸려면 어떻게 해?
A. 클릭 Handler에서 State를 변경하고 그 State를 기준으로 조건부 렌더링한다.

Q. 토글 UI는 어떻게 만들어?
A. boolean State를 만들고 `setOpen((prev) => !prev)`로 값을 반전한 뒤 조건부 렌더링한다.

Q. 선택된 item은 객체로 저장해야 해?
A. 보통 selectedId만 State로 저장하고 객체는 목록에서 계산하는 방식이 안전하다.

---

## 4.2 Form Validation Basic

### [개념]

Form Validation Basic은 사용자가 입력한 값을 제출하기 전에 기본 조건을 검사하는 과정이다.

React Core에서는 submit handler 내부의 간단한 validation만 다룬다.

---

### [핵심]

Form Validation 핵심 키워드:

- validation
- required value
- trim
- error message
- submit handler
- form state
- controlled input
- early return

기본 검증 대상:

- 빈 문자열
- 최소 길이
- 선택 여부
- 숫자 범위
- 필수 체크박스
- 간단한 형식 확인

---

### [실무]

기본 검증 예:

```jsx
function SearchForm({ onSearch }) {
  const [keyword, setKeyword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  function handleSubmit(event) {
    event.preventDefault();

    const trimmedKeyword = keyword.trim();

    if (!trimmedKeyword) {
      setErrorMessage("검색어를 입력하세요.");
      return;
    }

    setErrorMessage("");
    onSearch(trimmedKeyword);
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={keyword}
        onChange={(event) => setKeyword(event.target.value)}
      />
      {errorMessage && <p>{errorMessage}</p>}
      <button type="submit">Search</button>
    </form>
  );
}
```

Flow:

```text
Submit Event
→ preventDefault
→ Input Trim
→ Validation
→ Error State or Submit Logic
→ Conditional Error UI
```

주의:

- validation 실패 시 early return
- error message도 State로 관리 가능
- 입력 중 error를 지울지 submit 후 지울지 정책 필요
- 복잡한 검증은 Form Handling Validation 문서로 연결

---

### [FAQ]

Q. Form 입력값 검증은 어디서 해?
A. 기본 검증은 submit handler 또는 별도 validation 함수에서 처리한다.

Q. validation 실패 시 어떻게 처리해?
A. error State를 설정하고 submit 로직을 실행하지 않도록 early return한다.

Q. 입력값 앞뒤 공백은 어떻게 처리해?
A. `trim()`으로 제거한 값을 검증하거나 제출한다.

---

# 5. Common Mistakes

## 5.1 Event Handling Mistakes

### [개념]

Event Handling 실수는 Handler 즉시 실행, button type 누락, preventDefault 누락, State 직접 변경에서 자주 발생한다.

---

### [핵심]

Event Handling Common Mistakes:

- `onClick={handleClick()}` 사용
- 인자가 필요한 Handler를 즉시 실행
- form submit에서 preventDefault 누락
- form 내부 button type 누락
- Event Handler에서 State 직접 변경
- DOM 직접 조작으로 UI 변경
- Handler 이름 불명확
- 너무 많은 로직을 JSX inline에 작성

---

### [실무]

즉시 실행 문제:

```jsx
<button onClick={handleClick()}>Click</button>
```

개선:

```jsx
<button type="button" onClick={handleClick}>
  Click
</button>
```

인자 전달 문제:

```jsx
<button onClick={onSelect(festivalId)}>Select</button>
```

개선:

```jsx
<button type="button" onClick={() => onSelect(festivalId)}>
  Select
</button>
```

Form 새로고침 문제:

```jsx
function handleSubmit(event) {
  event.preventDefault();
}
```

Debug Flow:

```text
Unexpected Execution
→ Handler Reference Check
→ Arrow Function 필요 여부 확인
→ Button Type Check
→ preventDefault Check
→ State Update 위치 확인
```

---

### [FAQ]

Q. 클릭하지 않았는데 함수가 실행돼?
A. `onClick={handleClick()}`처럼 렌더링 중 함수를 호출했을 가능성이 높다.

Q. form 제출하면 화면이 새로고침돼?
A. submit handler에서 `event.preventDefault()`를 호출했는지 확인한다.

Q. button을 눌렀는데 form이 제출돼?
A. form 내부 button의 기본 type이 submit일 수 있으므로 일반 버튼에는 `type="button"`을 명시한다.

---

## 5.2 Controlled Input Mistakes

### [개념]

Controlled Input 실수는 value와 onChange 불일치, 초기값 문제, checkbox 처리 오류, 객체 Form State 직접 변경에서 자주 발생한다.

---

### [핵심]

Controlled Input Common Mistakes:

- value만 있고 onChange 없음
- onChange만 있고 value 없음
- 초기값 undefined 또는 null
- checkbox를 value로 제어
- 객체 Form State 직접 수정
- input name과 State property 불일치
- 숫자 input value를 number로 착각
- validation 없이 submit 처리

---

### [실무]

읽기 전용 input 문제:

```jsx
<input value={keyword} />
```

개선:

```jsx
<input value={keyword} onChange={(event) => setKeyword(event.target.value)} />
```

checkbox 오류:

```jsx
<input
  type="checkbox"
  value={checked}
  onChange={(event) => setChecked(event.target.value)}
/>
```

개선:

```jsx
<input
  type="checkbox"
  checked={checked}
  onChange={(event) => setChecked(event.target.checked)}
/>
```

객체 State 직접 수정 문제:

```jsx
form.title = "New Title";
setForm(form);
```

개선:

```jsx
setForm((prevForm) => ({
  ...prevForm,
  title: "New Title",
}));
```

---

### [FAQ]

Q. input이 입력되지 않는 이유는?
A. value만 있고 onChange가 없거나 State가 제대로 업데이트되지 않을 수 있다.

Q. checkbox 값이 이상하게 들어와?
A. checkbox는 `event.target.value`가 아니라 `event.target.checked`를 사용해야 한다.

Q. controlled/uncontrolled warning은 왜 나?
A. input value가 undefined/null에서 문자열로 바뀌는 등 제어 방식이 중간에 바뀔 때 발생할 수 있다.

---

## 5.3 Conditional Rendering Mistakes

### [개념]

Conditional Rendering 실수는 JSX 내부 if문 사용, `0 && Component` 문제, loading/error/empty 상태 혼동에서 자주 발생한다.

---

### [핵심]

Conditional Rendering Common Mistakes:

- JSX 내부에 if statement 직접 작성
- `0 && <Component />`로 0 렌더링
- loading과 empty 상태 혼동
- error 상태 무시
- null 데이터 property 접근
- 조건식이 너무 복잡함
- CSS Hide와 Conditional Rendering 목적 혼동
- key 없는 조건부 list 렌더링

---

### [실무]

JSX 내부 if 문제:

```jsx
return (
  <div>
    {if (loading) {
      return <p>Loading...</p>;
    }}
  </div>
);
```

개선:

```jsx
if (loading) {
  return <p>Loading...</p>;
}

return <div>Content</div>;
```

`0 && Component` 문제:

```jsx
{
  count && <p>Count exists</p>;
}
```

개선:

```jsx
{
  count > 0 && <p>Count exists</p>;
}
```

null 접근 문제:

```jsx
<p>{festival.title}</p>
```

개선:

```jsx
if (!festival) {
  return <p>No festival selected.</p>;
}

return <p>{festival.title}</p>;
```

---

### [FAQ]

Q. JSX 안에서 if문을 쓰면 왜 안 돼?
A. JSX 내부에는 statement를 직접 쓸 수 없기 때문이다. return 전에 조건을 처리하거나 삼항 연산자 등을 사용한다.

Q. 화면에 0이 갑자기 보이는 이유는?
A. `0 && <Component />`에서 왼쪽 값 0이 그대로 렌더링될 수 있기 때문이다.

Q. null property 오류는 어떻게 막아?
A. 데이터가 없을 때 early return하거나 optional chaining, 조건부 렌더링을 사용한다.

---

# 6. Checklist

## 6.1 Part03 Quality Checklist

### [개념]

React Core Part03 검수는 Event Handling, Controlled Input, Conditional Rendering을 기준으로 수행한다.

---

### [핵심]

Checklist:

```md
- [ ] Event Handling 기본 개념이 포함되었는가?
- [ ] onClick / onChange / onSubmit 설명이 포함되었는가?
- [ ] 함수 참조와 즉시 실행 차이가 포함되었는가?
- [ ] Event Object 설명이 포함되었는가?
- [ ] preventDefault 설명이 포함되었는가?
- [ ] Form Submit Event가 포함되었는가?
- [ ] Controlled Input 기본 개념이 포함되었는가?
- [ ] value + onChange 패턴이 포함되었는가?
- [ ] Controlled Form State가 포함되었는가?
- [ ] checkbox checked 처리 설명이 포함되었는가?
- [ ] Controlled vs Uncontrolled 비교가 포함되었는가?
- [ ] Conditional Rendering 기본 개념이 포함되었는가?
- [ ] early return / ternary / logical AND / null return이 포함되었는가?
- [ ] loading / error / empty / success UI가 포함되었는가?
- [ ] Conditional Rendering vs CSS Hide 비교가 포함되었는가?
- [ ] Event Driven UI Change가 포함되었는가?
- [ ] Form Validation Basic이 포함되었는가?
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
→ Event Handler Rule Check
→ Controlled Input Rule Check
→ Conditional Rendering Rule Check
→ Common Mistakes Check
→ FAQ Check
→ Retrieval Queries Check
→ Final Review
```

치명적 문제 기준:

- `onClick={handler()}`를 정상 패턴처럼 설명
- form submit에서 preventDefault 누락
- Controlled Input에서 value만 제공
- checkbox를 value로 제어하는 예제를 정상 예제로 제공
- JSX 내부 if statement를 정상 예제로 제공
- loading / error / empty 상태 혼동
- FAQ 누락
- Retrieval Queries 누락

---

### [FAQ]

Q. Part03에서 가장 중요한 검수 기준은?
A. Event Handler 함수 참조, Controlled Input value/onChange, preventDefault, 조건부 렌더링 상태 분리 포함 여부다.

Q. Part03에서 다루면 안 되는 내용은?
A. React Hook Form, Formik, Zod, TanStack Query, 고급 접근성, 복잡한 Form Architecture는 제외한다.

---

# Retrieval Queries

### [FAQ]

Q. React Event Handling은 어떻게 해?
A. onClick, onChange, onSubmit 같은 props에 Event Handler 함수를 전달한다.

Q. onClick={handleClick()}가 왜 문제야?
A. 렌더링 중 함수가 즉시 실행된다. 클릭 시 실행하려면 `onClick={handleClick}`처럼 함수 참조를 전달해야 한다.

Q. onClick에서 인자를 넘기려면 어떻게 해?
A. `onClick={() => handleClick(id)}`처럼 함수로 감싸서 전달한다.

Q. handler 이름은 어떻게 짓는 게 좋아?
A. Component 내부 함수는 handleSubmit, handleClick처럼 짓고 props callback은 onSubmit, onClick처럼 짓는 방식이 흔하다.

Q. React event object는 뭐야?
A. 이벤트가 발생했을 때 React가 Handler에 전달하는 이벤트 정보 객체다.

Q. input 입력값은 어디서 읽어?
A. `event.target.value`에서 읽는다.

Q. checkbox 체크 여부는 어디서 읽어?
A. `event.target.checked`에서 읽는다.

Q. event.target과 event.currentTarget 차이는?
A. target은 실제 이벤트가 발생한 요소이고 currentTarget은 Handler가 연결된 요소다.

Q. React에서 event.preventDefault는 언제 써?
A. form 제출 시 페이지 새로고침 같은 기본 동작을 막을 때 사용한다.

Q. form 제출은 button onClick으로 처리해도 돼?
A. 가능하지만 form 구조에서는 onSubmit을 사용하는 것이 Enter 입력과 접근성 측면에서 더 적절하다.

Q. form 안의 button type은 왜 명시해?
A. 기본 type이 submit일 수 있어 의도치 않은 form 제출을 막기 위해 일반 버튼은 `type="button"`을 명시한다.

Q. Controlled Input이 뭐야?
A. input 값을 DOM이 아니라 React State로 관리하는 방식이다.

Q. input에 value만 넣고 onChange를 안 넣으면?
A. 사용자가 값을 변경할 수 없는 읽기 전용 input처럼 동작할 수 있다.

Q. Controlled Input의 기준 데이터는 뭐야?
A. React State가 기준 데이터다.

Q. input 초기값은 어떻게 두는 게 좋아?
A. 문자열 input은 빈 문자열 `""`로 시작하는 것이 일반적이다.

Q. Form 입력값은 State 하나씩 만들어야 해?
A. 입력값이 적으면 개별 State를 사용하고, 관련 입력값이 많으면 객체 State로 묶을 수 있다.

Q. 객체 Form State에서 input 값을 어떻게 바꿔?
A. input name을 기준으로 `[name]: value` 형태로 새 객체를 만들어 setter에 전달한다.

Q. checkbox는 value로 제어해?
A. 아니다. checkbox는 checked와 onChange로 제어한다.

Q. Controlled Input과 Uncontrolled Input 차이는?
A. Controlled Input은 React State가 값을 관리하고 Uncontrolled Input은 DOM이 값을 관리한다.

Q. React에서는 어떤 input 방식을 기본으로 써?
A. 일반적인 Form 입력은 Controlled Input을 기본으로 사용한다.

Q. file input도 Controlled로 관리해?
A. file input은 브라우저 보안 제약 때문에 보통 Uncontrolled 성격으로 다룬다.

Q. React 조건부 렌더링은 어떻게 해?
A. early return, 삼항 연산자, logical AND, null return 등을 사용한다.

Q. React에서 if문은 어디에 써?
A. JSX 내부에 직접 쓰지 않고 return 전에 early return하거나 변수로 계산해 사용한다.

Q. && 조건부 렌더링은 언제 조심해야 해?
A. 왼쪽 값이 0이면 0이 화면에 렌더링될 수 있어 주의해야 한다.

Q. 조건이 많아지면 어떻게 해?
A. 조건별 Component를 분리하거나 return 전에 명확한 변수로 계산한다.

Q. loading, error, empty 상태를 분리해야 해?
A. 분리하는 것이 좋다. 비동기 UI 상태를 명확하게 관리할 수 있다.

Q. empty UI는 언제 보여줘?
A. 요청은 성공했지만 렌더링할 데이터가 없을 때 보여준다.

Q. error UI와 empty UI 차이는 뭐야?
A. error는 요청 실패 상태이고 empty는 요청 성공 후 데이터가 없는 상태다.

Q. 초기 배열 State는 왜 []로 두는 게 좋아?
A. map이나 length 같은 배열 메서드를 안전하게 사용할 수 있기 때문이다.

Q. Conditional Rendering과 CSS Hide 차이는?
A. Conditional Rendering은 조건에 따라 DOM에 렌더링하지 않고 CSS Hide는 렌더링 후 화면에서 숨긴다.

Q. Modal은 조건부 렌더링이 좋아?
A. 단순 Modal은 조건부 렌더링이 흔하지만 애니메이션이나 상태 유지가 필요하면 CSS Hide도 고려한다.

Q. 숨긴 Component의 State를 유지하려면?
A. DOM에 남겨두는 CSS Hide 방식이나 상위 State 관리 방식을 검토한다.

Q. 버튼 클릭으로 화면을 바꾸려면 어떻게 해?
A. 클릭 Handler에서 State를 변경하고 그 State를 기준으로 조건부 렌더링한다.

Q. 토글 UI는 어떻게 만들어?
A. boolean State를 만들고 `setOpen((prev) => !prev)`로 값을 반전한 뒤 조건부 렌더링한다.

Q. 선택된 item은 객체로 저장해야 해?
A. 보통 selectedId만 State로 저장하고 객체는 목록에서 계산하는 방식이 안전하다.

Q. Form 입력값 검증은 어디서 해?
A. 기본 검증은 submit handler 또는 별도 validation 함수에서 처리한다.

Q. validation 실패 시 어떻게 처리해?
A. error State를 설정하고 submit 로직을 실행하지 않도록 early return한다.

Q. 입력값 앞뒤 공백은 어떻게 처리해?
A. `trim()`으로 제거한 값을 검증하거나 제출한다.

Q. 클릭하지 않았는데 함수가 실행돼?
A. `onClick={handleClick()}`처럼 렌더링 중 함수를 호출했을 가능성이 높다.

Q. form 제출하면 화면이 새로고침돼?
A. submit handler에서 `event.preventDefault()`를 호출했는지 확인한다.

Q. button을 눌렀는데 form이 제출돼?
A. form 내부 button의 기본 type이 submit일 수 있으므로 일반 버튼에는 `type="button"`을 명시한다.

Q. input이 입력되지 않는 이유는?
A. value만 있고 onChange가 없거나 State가 제대로 업데이트되지 않을 수 있다.

Q. checkbox 값이 이상하게 들어와?
A. checkbox는 `event.target.value`가 아니라 `event.target.checked`를 사용해야 한다.

Q. controlled/uncontrolled warning은 왜 나?
A. input value가 undefined/null에서 문자열로 바뀌는 등 제어 방식이 중간에 바뀔 때 발생할 수 있다.

Q. JSX 안에서 if문을 쓰면 왜 안 돼?
A. JSX 내부에는 statement를 직접 쓸 수 없기 때문이다. return 전에 조건을 처리하거나 삼항 연산자 등을 사용한다.

Q. 화면에 0이 갑자기 보이는 이유는?
A. `0 && <Component />`에서 왼쪽 값 0이 그대로 렌더링될 수 있기 때문이다.

Q. null property 오류는 어떻게 막아?
A. 데이터가 없을 때 early return하거나 optional chaining, 조건부 렌더링을 사용한다.

Q. React Core Part03 다음 문서는 뭐가 좋아?
A. List Rendering, key, Rendering Flow, Re-render를 다루는 React Core Part04로 이어지는 것이 좋다.
