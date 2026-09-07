# React Core Part04 - List Rendering, key, Rendering Flow, Re-render

---

# 1. List Rendering

## 1.1 List Rendering Basics

### [개념]

List Rendering은 배열 데이터를 JSX 목록으로 변환해 렌더링하는 방식이다.

React에서는 배열의 `map` 메서드를 사용해 데이터 목록을 Component 또는 JSX Element 목록으로 만든다.

예:

```jsx
function FestivalList({ festivals }) {
  return (
    <ul>
      {festivals.map((festival) => (
        <li key={festival.festivalId}>{festival.title}</li>
      ))}
    </ul>
  );
}
```

List Rendering은 API 응답 목록, 검색 결과, 카드 목록, 테이블 행, 메뉴 목록, 댓글 목록을 화면에 표시할 때 사용한다.

---

### [핵심]

List Rendering 핵심 키워드:

- List Rendering
- Array map
- JSX List
- key
- stable id
- list item component
- empty list
- filter before map
- sort copy before map
- Component extraction

핵심 규칙:

- 배열은 `map`으로 JSX 목록으로 변환
- 반복되는 최상위 JSX에는 key 필요
- key는 안정적인 고유 ID 사용
- index key는 정렬 / 삭제 / 추가가 있는 목록에서 지양
- 빈 목록 UI 제공
- filter / sort / map 흐름 분리 가능
- List Item UI가 커지면 Component로 분리

---

### [실무]

기본 목록 예:

```jsx
function FestivalList({ festivals }) {
  if (festivals.length === 0) {
    return <p>No festivals found.</p>;
  }

  return (
    <section className="festival-list">
      {festivals.map((festival) => (
        <article key={festival.festivalId} className="festival-card">
          <h2>{festival.title}</h2>
          <p>{festival.region}</p>
        </article>
      ))}
    </section>
  );
}
```

Component 분리 예:

```jsx
function FestivalList({ festivals, onSelect }) {
  if (festivals.length === 0) {
    return <p>No festivals found.</p>;
  }

  return (
    <section className="festival-list">
      {festivals.map((festival) => (
        <FestivalCard
          key={festival.festivalId}
          festival={festival}
          onSelect={onSelect}
        />
      ))}
    </section>
  );
}

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

주의:

- key는 반복되는 최상위 요소에 부여
- key는 Component 내부 props로 자동 전달되지 않음
- `key={Math.random()}` 금지
- map callback에서 `{}` block body를 쓰면 return 필요
- 빈 배열 상태를 고려
- 목록 정렬은 원본 배열을 직접 변경하지 않음

---

### [FAQ]

Q. React List Rendering은 어떻게 해?
A. 배열의 map 메서드로 데이터를 JSX 목록으로 변환한다.

Q. React list에서 key는 왜 필요해?
A. React가 목록 item의 추가, 삭제, 변경을 효율적으로 추적하기 위해 필요하다.

Q. map 안에서 Component를 써도 돼?
A. 가능하다. 반복 UI가 커지면 List Item Component로 분리하는 것이 좋다.

Q. 빈 목록은 어떻게 처리해?
A. 배열 길이가 0이면 empty UI를 먼저 반환하거나 조건부 렌더링한다.

---

## 1.2 map Rendering Rules

### [개념]

map Rendering은 배열의 각 item을 JSX Element로 변환하는 패턴이다.

React에서는 수동 반복보다 `map`을 사용해 데이터 기반 UI를 선언적으로 작성한다.

---

### [핵심]

map Rendering 핵심 키워드:

- array map
- item parameter
- JSX return
- implicit return
- explicit return
- key prop
- list item
- data driven UI

map 사용 방식:

```jsx
items.map((item) => <Component key={item.id} item={item} />);
```

또는

```jsx
items.map((item) => {
  return <Component key={item.id} item={item} />;
});
```

주의:

- `()`는 implicit return 가능
- `{}`는 explicit return 필요
- key 누락 금지
- map 결과는 JSX 내부에서 렌더링 가능
- 복잡한 로직은 map 밖으로 분리

---

### [실무]

좋은 예:

```jsx
function RegionFilter({ regions, selectedRegion, onSelect }) {
  return (
    <div className="region-filter">
      {regions.map((region) => (
        <button
          key={region.code}
          type="button"
          className={region.code === selectedRegion ? "active" : ""}
          onClick={() => onSelect(region.code)}
        >
          {region.name}
        </button>
      ))}
    </div>
  );
}
```

명시적 return 예:

```jsx
function FestivalList({ festivals }) {
  return (
    <section>
      {festivals.map((festival) => {
        const label = festival.active ? "진행 중" : "종료";

        return (
          <article key={festival.festivalId}>
            <h2>{festival.title}</h2>
            <p>{label}</p>
          </article>
        );
      })}
    </section>
  );
}
```

주의:

- map 내부 계산이 길어지면 함수 분리
- 조건이 복잡하면 filter 후 map 또는 Component 분리
- map 안에서 State setter 호출 금지
- map 안에서 key를 안정적으로 부여
- index key는 마지막 선택지로만 사용

---

### [FAQ]

Q. map 안에서 중괄호를 쓰면 return이 필요한 이유는?
A. 화살표 함수에서 `{}`를 사용하면 block body가 되므로 명시적으로 return해야 한다.

Q. map 안에서 조건문을 많이 써도 돼?
A. 가능하지만 복잡해지면 filter, 변수, 함수, Component로 분리하는 것이 좋다.

Q. map 안에서 setState를 호출해도 돼?
A. 렌더링 중 State 변경이 되어 무한 렌더링이 발생할 수 있으므로 금지한다.

---

## 1.3 filter, sort, map Pattern

### [개념]

filter, sort, map Pattern은 목록 데이터를 필터링하고 정렬한 뒤 JSX로 렌더링하는 흐름이다.

React에서는 원본 State 배열을 직접 변경하지 않고 계산된 배열을 렌더링한다.

---

### [핵심]

filter / sort / map 핵심 키워드:

- filter before map
- sort copy before map
- derived list
- immutable array
- no direct mutation
- search result
- sorted result
- rendered list

권장 Flow:

```text
Original State Array
→ filter
→ copy + sort
→ map
→ JSX List
```

핵심 규칙:

- filter는 새 배열 반환
- sort는 원본 배열 변경 주의
- sort 전 배열 복사 필요
- 렌더링 가능한 목록은 Derived Value로 계산
- 계산 결과를 불필요하게 State로 중복 저장하지 않음

---

### [실무]

검색 필터 예:

```jsx
function FestivalSearchResult({ festivals, keyword }) {
  const filteredFestivals = festivals.filter((festival) =>
    festival.title.toLowerCase().includes(keyword.toLowerCase()),
  );

  if (filteredFestivals.length === 0) {
    return <p>No festivals found.</p>;
  }

  return (
    <section>
      {filteredFestivals.map((festival) => (
        <FestivalCard key={festival.festivalId} festival={festival} />
      ))}
    </section>
  );
}
```

정렬 예:

```jsx
function FestivalList({ festivals }) {
  const sortedFestivals = [...festivals].sort((a, b) =>
    a.title.localeCompare(b.title),
  );

  return (
    <section>
      {sortedFestivals.map((festival) => (
        <FestivalCard key={festival.festivalId} festival={festival} />
      ))}
    </section>
  );
}
```

필터 + 정렬 + 렌더링 예:

```jsx
function ActiveFestivalList({ festivals }) {
  const activeFestivals = festivals
    .filter((festival) => festival.active)
    .toSorted((a, b) => a.title.localeCompare(b.title));

  return (
    <section>
      {activeFestivals.map((festival) => (
        <FestivalCard key={festival.festivalId} festival={festival} />
      ))}
    </section>
  );
}
```

주의:

- `festivals.sort()`는 원본 배열을 변경함
- 브라우저 지원 범위를 고려해 `toSorted` 또는 `[...array].sort()` 선택
- filter 결과가 빈 배열이면 empty UI 필요
- 검색어 비교 시 대소문자 정책 결정
- 복잡한 검색 / 정렬은 Data Fetching 또는 State Management 문서로 연결 가능

---

### [FAQ]

Q. filter와 map은 어떤 순서로 써?
A. 보통 먼저 filter로 보여줄 데이터를 고른 뒤 map으로 JSX 목록을 만든다.

Q. sort를 바로 써도 돼?
A. State 배열에 직접 sort를 쓰면 원본이 변경될 수 있으므로 복사 후 정렬해야 한다.

Q. 필터링된 목록을 State로 따로 저장해야 해?
A. 대부분 아니다. 원본 State와 검색 조건으로 계산 가능한 Derived Value로 처리하는 것이 좋다.

---

# 2. key

## 2.1 key Basics

### [개념]

key는 React가 목록 item을 식별하기 위해 사용하는 특수한 값이다.

React는 key를 기준으로 어떤 item이 추가, 삭제, 이동, 변경되었는지 추적한다.

예:

```jsx
{
  festivals.map((festival) => (
    <FestivalCard key={festival.festivalId} festival={festival} />
  ));
}
```

---

### [핵심]

key 핵심 키워드:

- key
- stable key
- unique key
- item identity
- list reconciliation
- server id
- no random key
- avoid index key

key 규칙:

- 반복되는 형제 요소 사이에서 unique해야 함
- 안정적인 값이어야 함
- 서버 ID 사용 권장
- index key는 정렬 / 삭제 / 추가가 있는 목록에서 지양
- Math.random key 금지
- key는 Component 내부 props로 전달되지 않음
- key는 반복문의 최상위 Element에 부여

---

### [실무]

좋은 예:

```jsx
function FestivalList({ festivals }) {
  return (
    <section>
      {festivals.map((festival) => (
        <FestivalCard key={festival.festivalId} festival={festival} />
      ))}
    </section>
  );
}
```

나쁜 예:

```jsx
{
  festivals.map((festival) => <FestivalCard festival={festival} />);
}
```

나쁜 예:

```jsx
{
  festivals.map((festival) => (
    <FestivalCard key={Math.random()} festival={festival} />
  ));
}
```

주의:

- key는 데이터의 identity를 표현해야 함
- key가 바뀌면 React는 다른 item으로 인식할 수 있음
- key는 전역 unique가 아니라 같은 list 형제 사이에서 unique하면 됨
- Component 내부에서 key 값이 필요하면 별도 prop으로 전달

```jsx
<FestivalCard
  key={festival.festivalId}
  festivalId={festival.festivalId}
  festival={festival}
/>
```

---

### [FAQ]

Q. React list에서 key는 왜 필요해?
A. React가 목록 item의 추가, 삭제, 변경을 효율적으로 추적하기 위해 필요하다.

Q. key는 어떤 값을 쓰는 게 좋아?
A. 서버에서 받은 고유 ID처럼 안정적이고 unique한 값을 쓰는 것이 좋다.

Q. key는 Component 안에서 props로 받을 수 있어?
A. 아니다. key는 React 내부에서 사용하는 특수 값이다. 필요하면 별도 prop으로 전달해야 한다.

---

## 2.2 index key Problem

### [개념]

index key는 배열 index를 key로 사용하는 방식이다.

정적인 목록에서는 가능하지만 추가, 삭제, 정렬이 있는 목록에서는 item identity가 깨질 수 있다.

예:

```jsx
{
  festivals.map((festival, index) => (
    <FestivalCard key={index} festival={festival} />
  ));
}
```

---

### [핵심]

index key 문제 키워드:

- index key
- unstable identity
- reordered list
- inserted item
- deleted item
- input state mismatch
- wrong item state
- avoid index key

index key가 위험한 상황:

- 목록 정렬 가능
- item 삭제 가능
- item 추가 가능
- 필터링 가능
- input이 포함된 목록
- item 내부 State가 있는 목록
- drag and drop 목록

index key가 비교적 허용되는 상황:

- 정적 목록
- 순서 변경 없음
- 추가 / 삭제 없음
- item 내부 State 없음
- 단순 텍스트 목록

---

### [실무]

나쁜 예:

```jsx
function TodoList({ todos }) {
  return (
    <ul>
      {todos.map((todo, index) => (
        <li key={index}>
          <input defaultValue={todo.title} />
        </li>
      ))}
    </ul>
  );
}
```

문제:

- item 삭제 / 정렬 시 input 값이 다른 item에 남을 수 있음
- React가 같은 index 위치의 item을 같은 것으로 오해할 수 있음

개선:

```jsx
function TodoList({ todos }) {
  return (
    <ul>
      {todos.map((todo) => (
        <li key={todo.todoId}>
          <input defaultValue={todo.title} />
        </li>
      ))}
    </ul>
  );
}
```

주의:

- index key는 편하지만 안정성이 낮음
- 서버 ID가 없으면 클라이언트에서 생성한 stable id 검토
- random key는 index key보다 더 나쁜 경우가 많음
- key 선택은 목록 UI 버그와 직접 연결됨

---

### [FAQ]

Q. index를 key로 써도 돼?
A. 정적인 목록은 가능하지만 추가, 삭제, 정렬이 있는 목록에서는 안정적인 ID를 사용하는 것이 좋다.

Q. index key를 쓰면 어떤 문제가 생겨?
A. 목록 순서가 바뀔 때 React가 item을 잘못 매칭해 UI 상태가 다른 item에 남을 수 있다.

Q. 서버 ID가 없으면 어떻게 해?
A. 데이터 생성 시 stable id를 만들거나 목록이 정적인지 확인한 뒤 index key 사용 여부를 신중히 결정한다.

---

## 2.3 Fragment key

### [개념]

Fragment key는 반복 렌더링에서 여러 형제 JSX를 하나의 그룹으로 반환해야 할 때 사용하는 key다.

빈 Fragment 문법 `<>...</>`에는 key를 줄 수 없으므로 `React.Fragment`를 사용한다.

---

### [핵심]

Fragment key 핵심 키워드:

- React.Fragment
- Fragment key
- empty fragment
- grouped siblings
- list rendering
- no extra DOM
- key required

규칙:

- `<>...</>`는 key 설정 불가
- key가 필요하면 `<React.Fragment key={id}>` 사용
- Fragment는 실제 DOM을 추가하지 않음
- 반복되는 최상위 그룹에 key 부여
- 여러 형제 요소를 반환할 때 사용

---

### [실무]

좋은 예:

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

나쁜 예:

```jsx
{
  festivals.map((festival) => (
    <>
      <h2>{festival.title}</h2>
      <p>{festival.region}</p>
    </>
  ));
}
```

개선:

```jsx
{
  festivals.map((festival) => (
    <React.Fragment key={festival.festivalId}>
      <h2>{festival.title}</h2>
      <p>{festival.region}</p>
    </React.Fragment>
  ));
}
```

주의:

- 의미 없는 div 추가를 피할 때 Fragment key 사용
- table / dl 구조에서 DOM 구조를 유지할 때 유용
- key는 Fragment에 직접 부여
- Fragment 내부 첫 요소에 key를 주는 것과 다름

---

### [FAQ]

Q. Fragment에도 key가 필요해?
A. Fragment가 list의 반복 최상위 요소라면 key가 필요하다.

Q. 빈 Fragment `<>`에 key를 줄 수 있어?
A. 줄 수 없다. key가 필요하면 `React.Fragment`를 사용한다.

Q. Fragment key는 언제 써?
A. list에서 여러 형제 요소를 DOM 추가 없이 그룹으로 반환해야 할 때 사용한다.

---

# 3. Rendering Flow

## 3.1 React Rendering Flow

### [개념]

React Rendering Flow는 State 또는 Props 변화에 따라 Component 함수가 다시 실행되고 JSX 결과가 갱신되는 흐름이다.

Rendering은 화면을 직접 바꾸는 과정이 아니라 현재 State / Props를 기준으로 UI 결과를 계산하는 과정이다.

기본 Flow:

```text
Initial Render
→ User Event
→ State Update
→ Re-render
→ JSX Recalculation
→ DOM Update
```

---

### [핵심]

Rendering Flow 핵심 키워드:

- Initial Render
- Re-render
- State Change
- Props Change
- Component Function Execution
- JSX Recalculation
- DOM Update
- Render Phase
- Commit Phase
- State-driven UI

핵심 규칙:

- Component 함수는 렌더링마다 다시 실행
- State 변경은 Re-render를 유발
- Props 변경도 Child Component Re-render 가능
- Rendering은 UI 결과 계산 과정
- Rendering 중 State 변경 금지
- Side Effect는 useEffect에서 처리
- DOM 직접 조작보다 State 기반 Rendering 우선

---

### [실무]

좋은 Flow:

```text
User Click
→ handleClick
→ setCount
→ Counter Re-render
→ JSX Recalculation
→ Updated Button Text
```

예:

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

주의 예:

```jsx
function BadComponent() {
  const [count, setCount] = useState(0);

  setCount(count + 1);

  return <p>{count}</p>;
}
```

문제:

- 렌더링 중 State 변경
- State 변경이 다시 렌더링 유발
- 무한 렌더링 발생 가능

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

---

### [FAQ]

Q. React Rendering Flow가 뭐야?
A. State나 Props 변화에 따라 Component 함수가 다시 실행되고 JSX 결과가 갱신되는 흐름이다.

Q. Component 함수는 언제 실행돼?
A. 초기 렌더링과 State 또는 Props 변경으로 다시 렌더링될 때 실행된다.

Q. 렌더링 중 setState를 호출하면 왜 문제야?
A. State 변경이 다시 렌더링을 유발해 무한 렌더링이 발생할 수 있다.

Q. Rendering은 DOM을 바로 바꾸는 거야?
A. Rendering은 UI 결과를 계산하는 과정이고 실제 DOM 반영은 이후 React가 처리한다.

---

## 3.2 Initial Render and Re-render

### [개념]

Initial Render는 Component가 처음 화면에 나타날 때 실행되는 렌더링이다.

Re-render는 State 또는 Props 변화로 Component가 다시 실행되는 렌더링이다.

---

### [핵심]

Initial Render 핵심:

- Component first render
- initial State
- initial Props
- JSX first calculation
- mount

Re-render 핵심:

- State update
- Props change
- Parent re-render
- Context change mention
- JSX recalculation
- UI update

Re-render 발생 가능 상황:

- 현재 Component의 State 변경
- Parent Component가 다시 렌더링됨
- Child에 전달된 Props 변경
- Context 값 변경
- external store 구독 값 변경

---

### [실무]

Initial Render 예:

```jsx
function FestivalPage() {
  const [festivals, setFestivals] = useState([]);

  return <FestivalList festivals={festivals} />;
}
```

초기 상태:

- `festivals`는 `[]`
- `FestivalList`는 빈 배열 기준으로 렌더링
- API 데이터 로딩 전 empty 또는 loading UI 필요

Re-render 예:

```jsx
function FestivalPage() {
  const [keyword, setKeyword] = useState("");

  return (
    <>
      <input
        value={keyword}
        onChange={(event) => setKeyword(event.target.value)}
      />
      <p>{keyword}</p>
    </>
  );
}
```

Flow:

```text
Initial Render
→ keyword = ""
→ User Input
→ setKeyword
→ Re-render
→ p text update
```

주의:

- Re-render는 오류가 아니라 React의 정상 동작
- Re-render마다 Component 함수 내부 계산이 다시 실행됨
- 무거운 계산은 필요 시 최적화 문서에서 다룸
- React Core에서는 useMemo / useCallback 심화 제외
- 불필요한 Re-render 최적화보다 정확한 State 구조가 우선

---

### [FAQ]

Q. Initial Render는 뭐야?
A. Component가 처음 화면에 렌더링되는 과정이다.

Q. Re-render는 언제 발생해?
A. State 변경, Props 변경, Parent Re-render, Context 변경 등으로 발생할 수 있다.

Q. Re-render가 발생하면 무조건 나쁜 거야?
A. 아니다. React에서 UI를 최신 상태로 갱신하기 위한 정상 동작이다.

Q. Re-render마다 함수 내부 코드가 다시 실행돼?
A. Component 함수 내부의 렌더링 로직은 다시 실행된다.

---

## 3.3 Render Phase and Commit Phase

### [개념]

Render Phase는 React가 새로운 UI 결과를 계산하는 단계다.

Commit Phase는 계산된 변경 사항을 실제 DOM에 반영하는 단계다.

React Core에서는 Render Phase와 Commit Phase를 깊게 다루지 않고 렌더링 흐름 이해용으로만 사용한다.

---

### [핵심]

Render Phase 핵심:

- Component function execution
- JSX calculation
- pure calculation
- no side effect
- no state update during render

Commit Phase 핵심:

- DOM update
- ref update
- effect after commit
- user sees update

기본 Flow:

```text
State / Props Change
→ Render Phase: UI 계산
→ Commit Phase: DOM 반영
→ Browser Paint
→ useEffect 실행
```

핵심 규칙:

- Render Phase에서는 순수 계산 중심
- Render Phase에서 State 변경 금지
- Side Effect는 useEffect에서 처리
- DOM 반영 이후 Effect 실행

---

### [실무]

Render Phase에 적합한 작업:

- JSX 반환
- Props / State 기반 값 계산
- Derived Value 계산
- 조건부 렌더링
- List Rendering

Render Phase에 부적합한 작업:

- setState 직접 호출
- API Request 직접 실행
- Timer 등록
- Event Listener 등록
- localStorage 쓰기 남용
- DOM 직접 조작

나쁜 예:

```jsx
function FestivalPage() {
  const [festivals, setFestivals] = useState([]);

  fetch("/api/festivals")
    .then((response) => response.json())
    .then((data) => setFestivals(data));

  return <FestivalList festivals={festivals} />;
}
```

문제:

- 렌더링 중 API Request 실행
- State 변경으로 다시 렌더링
- 다시 API Request 실행 가능
- 무한 요청 가능

개선 방향:

```text
API Request
→ useEffect 또는 Event Handler에서 처리
```

---

### [FAQ]

Q. Render Phase는 뭐야?
A. React가 Component를 실행해 새로운 UI 결과를 계산하는 단계다.

Q. Commit Phase는 뭐야?
A. 계산된 변경 사항을 실제 DOM에 반영하는 단계다.

Q. API 요청을 Component 본문에서 바로 하면 안 돼?
A. 렌더링마다 요청이 실행될 수 있어 useEffect 또는 Event Handler에서 처리해야 한다.

Q. Side Effect는 어디서 처리해?
A. 외부 시스템과 동기화가 필요한 작업은 useEffect에서 처리한다.

---

# 4. Re-render

## 4.1 Re-render Basics

### [개념]

Re-render는 React Component가 다시 실행되어 새로운 JSX 결과를 계산하는 과정이다.

Re-render는 State 변경, Props 변경, Parent Re-render 등으로 발생한다.

---

### [핵심]

Re-render 핵심 키워드:

- Re-render
- State Update
- Props Change
- Parent Render
- JSX Recalculation
- UI Update
- Render Count
- React DevTools
- StrictMode

Re-render 핵심 이해:

- Re-render는 정상 동작
- State 변경은 Re-render 유발
- Parent가 Re-render되면 Child도 Re-render될 수 있음
- Re-render는 DOM 전체 교체를 의미하지 않음
- React는 필요한 DOM 변경만 반영
- 개발 모드 StrictMode에서 렌더링이 더 많이 보일 수 있음

---

### [실무]

Parent Re-render 예:

```jsx
function Parent() {
  const [count, setCount] = useState(0);

  return (
    <>
      <button type="button" onClick={() => setCount((prev) => prev + 1)}>
        Count
      </button>
      <Child />
    </>
  );
}

function Child() {
  console.log("Child render");

  return <p>Child</p>;
}
```

특징:

- Parent State가 변경되면 Parent가 Re-render
- Child도 함께 다시 실행될 수 있음
- 이것은 일반적으로 정상 동작

주의:

- 무조건 memoization부터 적용하지 않음
- 먼저 State 위치와 Props 구조를 검토
- 불필요한 State를 제거
- Derived Value는 State로 중복 저장하지 않음
- 성능 최적화 심화는 React Performance 문서로 연결

---

### [FAQ]

Q. Re-render가 뭐야?
A. Component가 다시 실행되어 새로운 JSX 결과를 계산하는 과정이다.

Q. Parent가 Re-render되면 Child도 Re-render돼?
A. 일반적으로 Child도 다시 렌더링될 수 있다.

Q. Re-render는 DOM 전체를 다시 만드는 거야?
A. 아니다. React는 새로운 UI 결과를 계산한 뒤 필요한 DOM 변경만 반영한다.

Q. Re-render가 많으면 무조건 useMemo를 써야 해?
A. 아니다. 먼저 State 위치, Props 구조, 불필요한 State를 검토해야 한다.

---

## 4.2 State Update and Re-render

### [개념]

State Update는 Component의 State를 변경하는 작업이다.

State Update가 발생하면 React는 해당 Component를 다시 렌더링할 수 있다.

---

### [핵심]

State Update 핵심 키워드:

- setState
- setter function
- scheduled update
- batching
- functional update
- Re-render
- stale state caution

핵심 규칙:

- setter 호출은 State 변경을 예약
- React는 여러 State 업데이트를 묶어 처리할 수 있음
- setter 호출 직후 값이 즉시 바뀐 것처럼 읽히지 않을 수 있음
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
- State update는 즉시 변수 대입이 아님

Functional Update 예:

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

연속 업데이트 예:

```jsx
setCount((prevCount) => prevCount + 1);
setCount((prevCount) => prevCount + 1);
setCount((prevCount) => prevCount + 1);
```

주의:

- 이전 값 기반이면 functional update 사용
- `setCount(count + 1)` 반복은 기대와 다를 수 있음
- 상태 변경 직후 결과 확인은 렌더링 결과 또는 effect로 검토
- React Core에서는 batching 심화 제외

---

### [FAQ]

Q. setState 호출하면 바로 Re-render돼?
A. React가 State 변경을 예약하고 적절한 시점에 Re-render를 수행한다.

Q. setState 직후 console.log 값이 이전 값인 이유는?
A. State 업데이트가 즉시 변수에 반영되는 단순 대입이 아니기 때문이다.

Q. 여러 번 State를 증가시키려면 어떻게 해?
A. 이전 State 기반 업데이트이므로 functional update를 사용한다.

---

## 4.3 StrictMode Double Render Caution

### [개념]

StrictMode는 개발 중 React Component의 잠재적 문제를 찾기 위한 개발 모드 도구다.

개발 환경에서는 StrictMode 때문에 Component 렌더링이나 effect 실행이 두 번처럼 보일 수 있다.

---

### [핵심]

StrictMode 핵심 키워드:

- React StrictMode
- development mode
- double render caution
- side effect detection
- useEffect double run
- no production double render
- debugging caution

핵심 이해:

- StrictMode는 개발 모드에서만 추가 검사 수행
- Component render가 두 번처럼 보일 수 있음
- useEffect가 추가 실행되는 것처럼 보일 수 있음
- Side Effect 문제를 찾기 위한 목적
- 운영 환경 동작과 다를 수 있음
- StrictMode 때문에 발생한 현상인지 확인 필요

---

### [실무]

StrictMode 예:

```jsx
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <App />
  </StrictMode>,
);
```

Debug 기준:

```text
Effect가 두 번 실행되는 것처럼 보임
→ 개발 모드인지 확인
→ StrictMode 사용 여부 확인
→ cleanup 함수 정상 동작 확인
→ API 중복 호출 방지 구조 확인
```

주의:

- StrictMode를 무작정 제거하지 않음
- Effect cleanup을 올바르게 작성
- API 요청 중복 방지 구조는 Data Fetching 문서에서 심화
- Console log만 보고 운영 버그로 단정하지 않음
- Side Effect를 Render Phase에 두지 않음

---

### [FAQ]

Q. 개발 중 useEffect가 두 번 실행되는 것처럼 보여?
A. React StrictMode에서 개발 중 부작용 검사를 위해 effect가 추가 실행될 수 있다.

Q. StrictMode는 운영 환경에도 영향을 줘?
A. StrictMode의 추가 검사는 개발 환경 중심이며 운영 환경 동작과 다를 수 있다.

Q. StrictMode를 꺼야 해?
A. 보통 끄기보다 effect cleanup과 side effect 위치를 올바르게 수정하는 것이 좋다.

---

# 5. Rendering Troubleshooting

## 5.1 Infinite Render Problem

### [개념]

Infinite Render Problem은 Component가 계속 다시 렌더링되는 문제다.

대표적으로 렌더링 중 State를 변경하거나, Event Handler를 잘못 전달하거나, Effect dependency가 잘못된 경우 발생한다.

---

### [핵심]

Infinite Render 핵심 키워드:

- Too many re-renders
- infinite render
- render loop
- setState during render
- immediate handler execution
- useEffect dependency loop
- State Update Condition

주요 원인:

- 렌더링 중 setState 호출
- onClick에 함수 실행 결과 전달
- useEffect dependency 문제
- effect 안에서 dependency state 계속 변경
- props 변경과 state 변경 순환
- Derived State 동기화 로직 오류

해결:

- setState를 Event Handler 또는 useEffect 내부 조건부 로직으로 이동
- onClick에는 함수 참조 전달
- dependency array 확인
- 상태 변경 조건 추가
- Derived State 제거 검토

---

### [실무]

렌더링 중 setState 문제:

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

Event Handler 즉시 실행 문제:

```jsx
<button onClick={setCount(count + 1)}>Count</button>
```

개선:

```jsx
<button type="button" onClick={() => setCount((prev) => prev + 1)}>
  Count
</button>
```

Debug Flow:

```text
Too many re-renders
→ setState 위치 확인
→ Event Handler 전달 방식 확인
→ useEffect dependency 확인
→ Derived State 동기화 제거 검토
→ 조건부 State Update 확인
```

---

### [FAQ]

Q. Too many re-renders 오류는 왜 나?
A. 렌더링 중 State를 변경하거나 Event Handler를 잘못 전달해 렌더링마다 setState가 호출될 때 발생한다.

Q. onClick에서 setState를 바로 쓰면 안 돼?
A. `onClick={setCount(count + 1)}`는 렌더링 중 실행된다. `onClick={() => setCount(count + 1)}`처럼 함수로 감싸야 한다.

Q. 무한 렌더링은 어디서 먼저 확인해?
A. setState가 Component 본문에서 실행되는지와 Event Handler가 즉시 실행되는지 먼저 확인한다.

---

## 5.2 List UI Update Problem

### [개념]

List UI Update Problem은 목록 렌더링에서 item 추가, 삭제, 정렬, 수정 시 화면이 예상과 다르게 갱신되는 문제다.

주요 원인은 key 누락, index key, 배열 State 직접 mutation이다.

---

### [핵심]

List UI 문제 키워드:

- key warning
- index key problem
- state mutation
- array push
- array sort mutation
- wrong item update
- stale list UI
- stable key

주요 원인:

- key 누락
- 중복 key 사용
- index key 사용
- random key 사용
- 배열 State 직접 수정
- 원본 배열 sort 직접 실행
- item identity 불안정

해결:

- stable id key 사용
- key 중복 제거
- index key 지양
- random key 금지
- immutable update 사용
- sort 전 배열 복사
- item 수정은 map 사용

---

### [실무]

State mutation 문제:

```jsx
festivals.push(newFestival);
setFestivals(festivals);
```

개선:

```jsx
setFestivals((prevFestivals) => [...prevFestivals, newFestival]);
```

sort mutation 문제:

```jsx
const sortedFestivals = festivals.sort((a, b) =>
  a.title.localeCompare(b.title),
);
```

개선:

```jsx
const sortedFestivals = [...festivals].sort((a, b) =>
  a.title.localeCompare(b.title),
);
```

item 수정 예:

```jsx
setFestivals((prevFestivals) =>
  prevFestivals.map((festival) =>
    festival.festivalId === targetId
      ? { ...festival, title: "Updated Title" }
      : festival,
  ),
);
```

Debug Flow:

```text
List UI 이상
→ Console key warning 확인
→ key 값 안정성 확인
→ index key 사용 여부 확인
→ 배열 mutation 여부 확인
→ sort 원본 변경 여부 확인
```

---

### [FAQ]

Q. 목록 UI가 이상하게 바뀌는 이유는?
A. key가 불안정하거나 배열 State를 직접 수정했을 가능성이 높다.

Q. item 삭제 후 다른 item 값이 남는 이유는?
A. index key 때문에 React가 item identity를 잘못 매칭했을 수 있다.

Q. 목록 정렬 후 화면이 이상하면 뭘 확인해?
A. 원본 State 배열을 직접 sort했는지와 key가 안정적인지 확인한다.

---

## 5.3 Key Warning

### [개념]

Key Warning은 React 목록 렌더링에서 각 item을 구분할 key가 없거나 부적절할 때 발생하는 경고다.

대표 메시지는 `Each child in a list should have a unique key prop` 형태다.

---

### [핵심]

Key Warning 핵심 키워드:

- Each child in a list should have a unique key prop
- missing key
- duplicate key
- unstable key
- random key
- index key
- list reconciliation

원인:

- key 누락
- 중복 key 사용
- 반복 최상위 요소가 아닌 내부 요소에 key 부여
- index key 남용
- Math.random key 사용
- Fragment key 누락

해결:

- 서버 ID 사용
- 고유한 stable key 사용
- key는 반복 최상위 요소에 부여
- Fragment 반복 시 React.Fragment key 사용
- index key 지양
- random key 금지

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

반복 최상위 요소 key 예:

```jsx
{
  festivals.map((festival) => (
    <div key={festival.festivalId}>
      <FestivalCard festival={festival} />
    </div>
  ));
}
```

Fragment key 예:

```jsx
{
  festivals.map((festival) => (
    <React.Fragment key={festival.festivalId}>
      <h2>{festival.title}</h2>
      <p>{festival.region}</p>
    </React.Fragment>
  ));
}
```

주의:

- key는 props로 자동 전달되지 않음
- key는 화면 표시용 값이 아니라 React 추적용 값
- list item 내부 가장 바깥에 key 부여
- key warning은 무시하지 않음

---

### [FAQ]

Q. React key warning은 왜 나?
A. 목록 item을 구분할 고유 key가 없거나 중복되었기 때문이다.

Q. key에 Math.random을 쓰면 안 돼?
A. 안 된다. 매 렌더링마다 key가 바뀌어 React가 item을 안정적으로 추적할 수 없다.

Q. key warning을 무시해도 돼?
A. 무시하지 않는 것이 좋다. 목록 UI 갱신 버그로 이어질 수 있다.

---

# 6. Comparison

## 6.1 Required Comparisons

### [개념]

React Core Part04는 목록 렌더링과 렌더링 흐름에서 헷갈리는 개념을 비교해서 작성한다.

비교는 Retrieval Hit와 Agent 판단 정확도를 높인다.

---

### [핵심]

필수 비교 대상:

- map Rendering vs Manual Repetition
- key id vs index key
- State Array vs Derived List
- filter vs map
- sort vs toSorted
- Initial Render vs Re-render
- Render Phase vs Commit Phase
- Re-render vs DOM Update
- Conditional Rendering vs List Empty UI
- Stable key vs Random key

---

### [실무]

map Rendering vs Manual Repetition:

| 비교        | map Rendering | Manual Repetition |
| ----------- | ------------- | ----------------- |
| 기준        | 데이터 배열   | 수동 JSX 작성     |
| 확장성      | 높음          | 낮음              |
| 유지보수    | 쉬움          | 어려움            |
| 동적 데이터 | 적합          | 부적합            |
| React 목록  | 권장          | 비권장            |

key id vs index key:

| 비교      | Stable ID Key | Index Key |
| --------- | ------------- | --------- |
| 안정성    | 높음          | 낮음      |
| 정렬 대응 | 안전          | 위험      |
| 삭제 대응 | 안전          | 위험      |
| 추가 대응 | 안전          | 위험      |
| 권장도    | 높음          | 제한적    |

Render Phase vs Commit Phase:

| 비교           | Render Phase | Commit Phase            |
| -------------- | ------------ | ----------------------- |
| 역할           | UI 결과 계산 | DOM 반영                |
| Component 실행 | 발생         | 발생하지 않음           |
| Side Effect    | 금지         | 이후 Effect 실행        |
| State 변경     | 금지         | Event / Effect에서 가능 |
| 목적           | JSX 계산     | 화면 반영               |

---

### [FAQ]

Q. 비교 표는 왜 필요해?
A. 사용자가 자주 헷갈리는 질문에서 Retrieval Hit와 답변 정확도를 높이기 위해 필요하다.

Q. Part04에서 가장 중요한 비교는?
A. key id vs index key, Initial Render vs Re-render, Render Phase vs Commit Phase 비교가 중요하다.

Q. Re-render와 DOM Update는 같은 말이야?
A. 아니다. Re-render는 UI 결과 계산이고 DOM Update는 React가 필요한 변경을 실제 DOM에 반영하는 과정이다.

---

# 7. Checklist

## 7.1 Part04 Quality Checklist

### [개념]

React Core Part04 검수는 List Rendering, key, Rendering Flow, Re-render, Troubleshooting을 기준으로 수행한다.

---

### [핵심]

Checklist:

```md
- [ ] List Rendering 기본 개념이 포함되었는가?
- [ ] map Rendering 규칙이 포함되었는가?
- [ ] map callback return 주의가 포함되었는가?
- [ ] filter before map 패턴이 포함되었는가?
- [ ] sort copy before map 패턴이 포함되었는가?
- [ ] key 기본 개념이 포함되었는가?
- [ ] stable key 규칙이 포함되었는가?
- [ ] index key 문제점이 포함되었는가?
- [ ] Fragment key 설명이 포함되었는가?
- [ ] Rendering Flow가 포함되었는가?
- [ ] Initial Render와 Re-render 설명이 포함되었는가?
- [ ] Render Phase와 Commit Phase 기초가 포함되었는가?
- [ ] 렌더링 중 setState 금지가 포함되었는가?
- [ ] Re-render 정상 동작 설명이 포함되었는가?
- [ ] StrictMode double render 주의가 포함되었는가?
- [ ] Infinite Render Problem이 포함되었는가?
- [ ] List UI Update Problem이 포함되었는가?
- [ ] Key Warning이 포함되었는가?
- [ ] Comparison이 포함되었는가?
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
→ List Rendering Rule Check
→ key Rule Check
→ Rendering Flow Check
→ Re-render Check
→ Troubleshooting Check
→ FAQ Check
→ Retrieval Queries Check
→ Final Review
```

치명적 문제 기준:

- key 없는 list 예제를 정상 예제로 제공
- index key를 일반 권장처럼 설명
- Math.random key를 허용처럼 설명
- 배열 State 직접 sort / push를 정상 예제로 제공
- 렌더링 중 setState를 허용처럼 설명
- Component 본문 API 요청을 정상 예제로 제공
- Re-render를 무조건 오류처럼 설명
- FAQ 누락
- Retrieval Queries 누락

---

### [FAQ]

Q. Part04에서 가장 중요한 검수 기준은?
A. List Rendering, stable key, index key 문제, Rendering Flow, Re-render, Infinite Render Problem 포함 여부다.

Q. Part04에서 다루면 안 되는 내용은?
A. useMemo, React.memo, useCallback, Virtualization, 고급 성능 최적화, TanStack Query 심화는 제외한다.

---

# Retrieval Queries

### [FAQ]

Q. React List Rendering은 어떻게 해?
A. 배열의 map 메서드로 데이터를 JSX 목록으로 변환한다.

Q. React list에서 key는 왜 필요해?
A. React가 목록 item의 추가, 삭제, 변경을 효율적으로 추적하기 위해 필요하다.

Q. map 안에서 Component를 써도 돼?
A. 가능하다. 반복 UI가 커지면 List Item Component로 분리하는 것이 좋다.

Q. 빈 목록은 어떻게 처리해?
A. 배열 길이가 0이면 empty UI를 먼저 반환하거나 조건부 렌더링한다.

Q. map 안에서 중괄호를 쓰면 return이 필요한 이유는?
A. 화살표 함수에서 `{}`를 사용하면 block body가 되므로 명시적으로 return해야 한다.

Q. map 안에서 조건문을 많이 써도 돼?
A. 가능하지만 복잡해지면 filter, 변수, 함수, Component로 분리하는 것이 좋다.

Q. map 안에서 setState를 호출해도 돼?
A. 렌더링 중 State 변경이 되어 무한 렌더링이 발생할 수 있으므로 금지한다.

Q. filter와 map은 어떤 순서로 써?
A. 보통 먼저 filter로 보여줄 데이터를 고른 뒤 map으로 JSX 목록을 만든다.

Q. sort를 바로 써도 돼?
A. State 배열에 직접 sort를 쓰면 원본이 변경될 수 있으므로 복사 후 정렬해야 한다.

Q. 필터링된 목록을 State로 따로 저장해야 해?
A. 대부분 아니다. 원본 State와 검색 조건으로 계산 가능한 Derived Value로 처리하는 것이 좋다.

Q. key는 어떤 값을 쓰는 게 좋아?
A. 서버에서 받은 고유 ID처럼 안정적이고 unique한 값을 쓰는 것이 좋다.

Q. key는 Component 안에서 props로 받을 수 있어?
A. 아니다. key는 React 내부에서 사용하는 특수 값이다. 필요하면 별도 prop으로 전달해야 한다.

Q. index를 key로 써도 돼?
A. 정적인 목록은 가능하지만 추가, 삭제, 정렬이 있는 목록에서는 안정적인 ID를 사용하는 것이 좋다.

Q. index key를 쓰면 어떤 문제가 생겨?
A. 목록 순서가 바뀔 때 React가 item을 잘못 매칭해 UI 상태가 다른 item에 남을 수 있다.

Q. 서버 ID가 없으면 어떻게 해?
A. 데이터 생성 시 stable id를 만들거나 목록이 정적인지 확인한 뒤 index key 사용 여부를 신중히 결정한다.

Q. Fragment에도 key가 필요해?
A. Fragment가 list의 반복 최상위 요소라면 key가 필요하다.

Q. 빈 Fragment `<>`에 key를 줄 수 있어?
A. 줄 수 없다. key가 필요하면 `React.Fragment`를 사용한다.

Q. Fragment key는 언제 써?
A. list에서 여러 형제 요소를 DOM 추가 없이 그룹으로 반환해야 할 때 사용한다.

Q. React Rendering Flow가 뭐야?
A. State나 Props 변화에 따라 Component 함수가 다시 실행되고 JSX 결과가 갱신되는 흐름이다.

Q. Component 함수는 언제 실행돼?
A. 초기 렌더링과 State 또는 Props 변경으로 다시 렌더링될 때 실행된다.

Q. 렌더링 중 setState를 호출하면 왜 문제야?
A. State 변경이 다시 렌더링을 유발해 무한 렌더링이 발생할 수 있다.

Q. Rendering은 DOM을 바로 바꾸는 거야?
A. Rendering은 UI 결과를 계산하는 과정이고 실제 DOM 반영은 이후 React가 처리한다.

Q. Initial Render는 뭐야?
A. Component가 처음 화면에 렌더링되는 과정이다.

Q. Re-render는 언제 발생해?
A. State 변경, Props 변경, Parent Re-render, Context 변경 등으로 발생할 수 있다.

Q. Re-render가 발생하면 무조건 나쁜 거야?
A. 아니다. React에서 UI를 최신 상태로 갱신하기 위한 정상 동작이다.

Q. Re-render마다 함수 내부 코드가 다시 실행돼?
A. Component 함수 내부의 렌더링 로직은 다시 실행된다.

Q. Render Phase는 뭐야?
A. React가 Component를 실행해 새로운 UI 결과를 계산하는 단계다.

Q. Commit Phase는 뭐야?
A. 계산된 변경 사항을 실제 DOM에 반영하는 단계다.

Q. API 요청을 Component 본문에서 바로 하면 안 돼?
A. 렌더링마다 요청이 실행될 수 있어 useEffect 또는 Event Handler에서 처리해야 한다.

Q. Side Effect는 어디서 처리해?
A. 외부 시스템과 동기화가 필요한 작업은 useEffect에서 처리한다.

Q. Re-render가 뭐야?
A. Component가 다시 실행되어 새로운 JSX 결과를 계산하는 과정이다.

Q. Parent가 Re-render되면 Child도 Re-render돼?
A. 일반적으로 Child도 다시 렌더링될 수 있다.

Q. Re-render는 DOM 전체를 다시 만드는 거야?
A. 아니다. React는 새로운 UI 결과를 계산한 뒤 필요한 DOM 변경만 반영한다.

Q. Re-render가 많으면 무조건 useMemo를 써야 해?
A. 아니다. 먼저 State 위치, Props 구조, 불필요한 State를 검토해야 한다.

Q. setState 호출하면 바로 Re-render돼?
A. React가 State 변경을 예약하고 적절한 시점에 Re-render를 수행한다.

Q. setState 직후 console.log 값이 이전 값인 이유는?
A. State 업데이트가 즉시 변수에 반영되는 단순 대입이 아니기 때문이다.

Q. 여러 번 State를 증가시키려면 어떻게 해?
A. 이전 State 기반 업데이트이므로 functional update를 사용한다.

Q. 개발 중 useEffect가 두 번 실행되는 것처럼 보여?
A. React StrictMode에서 개발 중 부작용 검사를 위해 effect가 추가 실행될 수 있다.

Q. StrictMode는 운영 환경에도 영향을 줘?
A. StrictMode의 추가 검사는 개발 환경 중심이며 운영 환경 동작과 다를 수 있다.

Q. StrictMode를 꺼야 해?
A. 보통 끄기보다 effect cleanup과 side effect 위치를 올바르게 수정하는 것이 좋다.

Q. Too many re-renders 오류는 왜 나?
A. 렌더링 중 State를 변경하거나 Event Handler를 잘못 전달해 렌더링마다 setState가 호출될 때 발생한다.

Q. onClick에서 setState를 바로 쓰면 안 돼?
A. `onClick={setCount(count + 1)}`는 렌더링 중 실행된다. `onClick={() => setCount(count + 1)}`처럼 함수로 감싸야 한다.

Q. 무한 렌더링은 어디서 먼저 확인해?
A. setState가 Component 본문에서 실행되는지와 Event Handler가 즉시 실행되는지 먼저 확인한다.

Q. 목록 UI가 이상하게 바뀌는 이유는?
A. key가 불안정하거나 배열 State를 직접 수정했을 가능성이 높다.

Q. item 삭제 후 다른 item 값이 남는 이유는?
A. index key 때문에 React가 item identity를 잘못 매칭했을 수 있다.

Q. 목록 정렬 후 화면이 이상하면 뭘 확인해?
A. 원본 State 배열을 직접 sort했는지와 key가 안정적인지 확인한다.

Q. React key warning은 왜 나?
A. 목록 item을 구분할 고유 key가 없거나 중복되었기 때문이다.

Q. key에 Math.random을 쓰면 안 돼?
A. 안 된다. 매 렌더링마다 key가 바뀌어 React가 item을 안정적으로 추적할 수 없다.

Q. key warning을 무시해도 돼?
A. 무시하지 않는 것이 좋다. 목록 UI 갱신 버그로 이어질 수 있다.

Q. Re-render와 DOM Update는 같은 말이야?
A. 아니다. Re-render는 UI 결과 계산이고 DOM Update는 React가 필요한 변경을 실제 DOM에 반영하는 과정이다.

Q. React Core Part04 다음 문서는 뭐가 좋아?
A. Hook Basics, useEffect, Dependency Array, Cleanup Function을 다루는 React Core Part05로 이어지는 것이 좋다.
