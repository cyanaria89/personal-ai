# React Core Part05 - Hook Basics, useEffect, Dependency Array, Cleanup Function

---

# 1. Hook Basics

## 1.1 Hook Definition

### [개념]

Hook은 Functional Component에서 React 기능을 사용할 수 있게 해주는 함수다.

Hook은 State, Effect, Ref, Context 같은 React 기능을 Class Component 없이 사용할 수 있게 한다.

React Core에서는 Hook 중 `useState`와 `useEffect`를 중심으로 다룬다.

대표 Hook:

- useState
- useEffect
- useRef
- useMemo
- useCallback
- useContext

---

### [핵심]

Hook 핵심 키워드:

- Hook
- Functional Component
- useState
- useEffect
- useRef
- useMemo
- useCallback
- useContext
- Custom Hook
- Rules of Hooks
- Hook Call Order

React Core 기준:

- useState는 State 관리
- useEffect는 외부 시스템 동기화
- useRef는 DOM 참조 또는 렌더링과 무관한 값 보관
- useMemo / useCallback은 성능 최적화 심화에서 다룸
- useContext는 Context API / State Management 문서에서 다룸
- Custom Hook 심화는 React Component Design 또는 Advanced React Pattern 문서에서 다룸

---

### [실무]

Modern React 실무 기준:

```text
Functional Component
→ Hook
→ State-driven UI
→ Effect Synchronization
→ Component Composition
```

Hook 사용 목적:

- Component 내부 State 관리
- 렌더링 이후 외부 시스템과 동기화
- DOM 참조
- 공통 로직 분리
- Context 값 사용
- 성능 최적화

주의:

- Hook은 React Component 최상위에서 호출
- Hook은 조건문 내부에서 호출하지 않음
- Hook은 반복문 내부에서 호출하지 않음
- Hook은 일반 함수 내부에서 호출하지 않음
- Custom Hook 이름은 `use`로 시작
- Hook 호출 순서는 렌더링마다 같아야 함

---

### [FAQ]

Q. Hook이 뭐야?
A. Functional Component에서 React 기능을 사용할 수 있게 해주는 함수다.

Q. React Core에서 가장 중요한 Hook은 뭐야?
A. useState와 useEffect다.

Q. Hook은 왜 필요해?
A. Functional Component에서 State, Effect, Ref 같은 React 기능을 사용하기 위해 필요하다.

---

## 1.2 Rules of Hooks

### [개념]

Rules of Hooks는 Hook을 안전하게 사용하기 위한 React 규칙이다.

React는 Hook 호출 순서를 기준으로 Component의 State와 Effect를 연결한다.

따라서 Hook 호출 순서는 렌더링마다 동일해야 한다.

---

### [핵심]

Rules of Hooks 핵심:

- Hook은 Component 최상위에서 호출
- 조건문 내부에서 Hook 호출 금지
- 반복문 내부에서 Hook 호출 금지
- 중첩 함수 내부에서 Hook 호출 금지
- 일반 JavaScript 함수에서 Hook 호출 금지
- React Component 또는 Custom Hook 내부에서만 호출
- Custom Hook 이름은 `use`로 시작
- Hook 호출 순서 유지

금지:

```text
if
for
while
switch 내부 조건 분기
nested function
event handler 내부
일반 util 함수 내부
```

---

### [실무]

나쁜 예:

```jsx
function FestivalPanel({ enabled }) {
  if (enabled) {
    const [open, setOpen] = useState(false);
  }

  return null;
}
```

문제:

- enabled 값에 따라 Hook 호출 여부가 달라짐
- Hook 호출 순서가 렌더링마다 달라질 수 있음

좋은 예:

```jsx
function FestivalPanel({ enabled }) {
  const [open, setOpen] = useState(false);

  if (!enabled) {
    return null;
  }

  return (
    <button type="button" onClick={() => setOpen((prev) => !prev)}>
      {open ? "Close" : "Open"}
    </button>
  );
}
```

Event Handler 내부 Hook 호출 금지:

```jsx
function BadComponent() {
  function handleClick() {
    const [count, setCount] = useState(0);
  }

  return (
    <button type="button" onClick={handleClick}>
      Click
    </button>
  );
}
```

개선:

```jsx
function GoodComponent() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount((prev) => prev + 1);
  }

  return (
    <button type="button" onClick={handleClick}>
      {count}
    </button>
  );
}
```

---

### [FAQ]

Q. Hook은 왜 조건문 안에서 호출하면 안 돼?
A. React는 Hook 호출 순서로 상태를 관리한다. 조건에 따라 호출 순서가 바뀌면 상태 연결이 깨질 수 있다.

Q. Hook은 일반 함수에서 호출해도 돼?
A. 안 된다. React Component 또는 Custom Hook 내부에서 호출해야 한다.

Q. Custom Hook 이름은 왜 use로 시작해야 해?
A. React와 lint 도구가 Hook 규칙을 검사할 수 있게 하기 위해서다.

---

## 1.3 Hook Scope in React Core

### [개념]

React Core 문서에서 Hook은 기본 화면 구현에 필요한 수준만 다룬다.

useState와 useEffect는 필수 범위다.

useRef는 기초 언급 가능하다.

useMemo, useCallback, useContext, Custom Hook은 심화 문서로 분리한다.

---

### [핵심]

React Core 포함:

- useState 기본
- useEffect 기본
- Dependency Array 기본
- Cleanup Function 기본
- API Call Basic Pattern
- Timer Cleanup
- Event Listener Cleanup
- StrictMode Double Effect 주의

React Core 제외 또는 기초 언급만:

- useMemo 심화
- useCallback 심화
- React.memo
- useContext 심화
- Custom Hook 설계 심화
- useReducer 심화
- Suspense
- Concurrent Rendering 심화
- Server Components
- Advanced React Pattern

---

### [실무]

React Core Hook 학습 흐름:

```text
useState
→ Event Handler
→ Conditional Rendering
→ List Rendering
→ Rendering Flow
→ useEffect
→ Dependency Array
→ Cleanup Function
→ API Call Basic
```

문서 연결:

```text
React Core
→ React Component Design
→ State Management
→ Data Fetching REST API Integration
→ Advanced React Pattern
→ Frontend Performance Tuning
```

주의:

- Hook을 API 암기식으로 나열하지 않음
- Component 화면 구현과 연결해 설명
- useEffect를 모든 로직 처리 장소로 설명하지 않음
- Side Effect와 Rendering 계산을 구분
- 고급 최적화는 React Core에 과도하게 포함하지 않음

---

### [FAQ]

Q. React Core에서 모든 Hook을 깊게 다뤄?
A. 아니다. useState와 useEffect를 중심으로 다루고 고급 Hook은 별도 문서에서 다룬다.

Q. useMemo와 useCallback은 React Core에서 다뤄?
A. 기본 언급은 가능하지만 성능 최적화 심화는 React Performance 또는 Advanced React Pattern 문서에서 다룬다.

Q. useContext는 React Core 범위야?
A. 기초 소개는 가능하지만 전역 상태 설계는 State Management 문서에서 다룬다.

---

# 2. useEffect

## 2.1 useEffect Definition

### [개념]

useEffect는 Component가 렌더링된 후 외부 시스템과 동기화할 때 사용하는 Hook이다.

외부 시스템은 React 렌더링만으로 처리할 수 없는 브라우저 API, 서버 API, Timer, Event Listener, Subscription 등을 의미한다.

외부 시스템 예:

- API Request
- Browser Event
- Timer
- Interval
- Subscription
- WebSocket
- localStorage
- document title
- Third-party library

---

### [핵심]

useEffect 핵심 키워드:

- useEffect
- Effect
- Side Effect
- External System
- Synchronization
- Dependency Array
- Cleanup Function
- Component Mount
- Component Update
- Component Unmount
- StrictMode

useEffect 기본 구조:

```jsx
useEffect(() => {
  // effect logic
}, []);
```

핵심 규칙:

- useEffect는 렌더링 후 실행
- 외부 시스템 동기화 목적
- 모든 로직을 useEffect에 넣지 않음
- Event로 처리 가능한 로직은 Event Handler에서 처리
- dependency array로 실행 조건 제어
- 정리가 필요한 Effect는 Cleanup Function 반환
- Render Phase에서 Side Effect 실행 금지

---

### [실무]

document title 동기화 예:

```jsx
function FestivalPage() {
  useEffect(() => {
    document.title = "Festival List";
  }, []);

  return <h1>Festival List</h1>;
}
```

API 요청 기초 예:

```jsx
function FestivalPage() {
  const [festivals, setFestivals] = useState([]);

  useEffect(() => {
    async function loadFestivals() {
      const response = await fetch("/api/festivals");
      const data = await response.json();
      setFestivals(data);
    }

    loadFestivals();
  }, []);

  return <FestivalList festivals={festivals} />;
}
```

주의:

- Component 본문에서 API 요청 실행 금지
- useEffect 안에서 State를 변경할 수 있지만 dependency loop 주의
- Event Handler에서 가능한 로직을 useEffect로 우회하지 않음
- API 호출 심화는 Data Fetching 문서에서 다룸
- StrictMode 개발 환경에서 Effect가 두 번 실행되는 것처럼 보일 수 있음

---

### [FAQ]

Q. useEffect는 언제 써?
A. Component가 렌더링된 후 외부 시스템과 동기화해야 할 때 사용한다.

Q. useEffect는 렌더링 전에 실행돼?
A. 아니다. 보통 렌더링 결과가 DOM에 반영된 후 실행된다.

Q. 모든 로직을 useEffect에 넣으면 돼?
A. 아니다. 사용자 이벤트로 처리할 수 있는 로직은 Event Handler에서 처리한다.

Q. API 요청은 Component 본문에서 바로 하면 안 돼?
A. 렌더링마다 요청이 실행될 수 있어 useEffect 또는 Event Handler에서 처리해야 한다.

---

## 2.2 Side Effect

### [개념]

Side Effect는 Component 렌더링 결과 계산 외부에 영향을 주는 작업이다.

React Component의 Render Phase는 가능한 순수 계산이어야 한다.

Side Effect는 useEffect 또는 Event Handler에서 처리한다.

---

### [핵심]

Side Effect 예:

- API Request
- DOM 직접 조작
- document title 변경
- localStorage 읽기 / 쓰기
- Timer 등록
- Event Listener 등록
- WebSocket 연결
- Subscription 등록
- 외부 Library 초기화

Side Effect가 아닌 것:

- JSX 반환
- Props / State 기반 계산
- Derived Value 계산
- Conditional Rendering
- List Rendering
- 문자열 포맷팅
- 배열 filter / map 계산

핵심 구분:

```text
UI 결과 계산
→ Render Phase

외부 시스템 영향
→ useEffect or Event Handler
```

---

### [실무]

Render Phase에 적합한 예:

```jsx
function FestivalCount({ festivals }) {
  const count = festivals.length;

  return <p>{count}</p>;
}
```

Render Phase에 부적합한 예:

```jsx
function BadPage() {
  localStorage.setItem("visited", "true");

  return <h1>Page</h1>;
}
```

개선:

```jsx
function GoodPage() {
  useEffect(() => {
    localStorage.setItem("visited", "true");
  }, []);

  return <h1>Page</h1>;
}
```

Event Handler에 적합한 예:

```jsx
function SaveButton({ data }) {
  function handleSave() {
    localStorage.setItem("draft", JSON.stringify(data));
  }

  return (
    <button type="button" onClick={handleSave}>
      Save
    </button>
  );
}
```

주의:

- 사용자 행동에 대한 직접 반응은 Event Handler 우선
- 렌더링 때문에 외부 시스템과 동기화해야 하면 useEffect 사용
- Render Phase에서 외부 시스템 변경 금지
- Side Effect 위치가 잘못되면 무한 렌더링 / 중복 실행 가능

---

### [FAQ]

Q. Side Effect가 뭐야?
A. Component 렌더링 결과 계산 외부에 영향을 주는 작업이다.

Q. Side Effect는 어디서 처리해?
A. 외부 시스템 동기화는 useEffect에서, 사용자 이벤트에 대한 직접 반응은 Event Handler에서 처리한다.

Q. localStorage 작업은 무조건 useEffect에서 해?
A. 렌더링 후 동기화 목적이면 useEffect, 버튼 클릭 저장처럼 사용자 이벤트라면 Event Handler에서 처리한다.

---

## 2.3 useEffect vs Event Handler

### [개념]

useEffect와 Event Handler는 모두 로직을 실행할 수 있지만 실행 원인이 다르다.

useEffect는 렌더링 결과와 외부 시스템을 동기화할 때 사용한다.

Event Handler는 사용자 행동에 직접 반응할 때 사용한다.

---

### [핵심]

useEffect vs Event Handler 비교:

| 비교        | useEffect                 | Event Handler    |
| ----------- | ------------------------- | ---------------- |
| 실행 원인   | 렌더링 후 dependency 변화 | 사용자 이벤트    |
| 목적        | 외부 시스템 동기화        | 사용자 행동 처리 |
| 예          | 초기 API 호출, title 변경 | 클릭, 입력, 제출 |
| State 변경  | 가능하나 loop 주의        | 일반적           |
| Cleanup     | 가능                      | 보통 불필요      |
| 대표 키워드 | synchronization           | user action      |

선택 기준:

```text
사용자가 직접 발생시킨 동작인가?
→ Event Handler

렌더링 결과를 외부 시스템과 맞춰야 하는가?
→ useEffect
```

---

### [실무]

Event Handler에 적합:

```jsx
function SearchForm({ onSearch }) {
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
      <button type="submit">Search</button>
    </form>
  );
}
```

useEffect에 적합:

```jsx
function FestivalPage() {
  const [festivals, setFestivals] = useState([]);

  useEffect(() => {
    async function loadFestivals() {
      const response = await fetch("/api/festivals");
      const data = await response.json();
      setFestivals(data);
    }

    loadFestivals();
  }, []);

  return <FestivalList festivals={festivals} />;
}
```

나쁜 패턴:

```jsx
function BadSearch({ submitted, keyword, onSearch }) {
  useEffect(() => {
    if (submitted) {
      onSearch(keyword);
    }
  }, [submitted, keyword, onSearch]);

  return null;
}
```

문제:

- 사용자 submit 로직을 Effect로 우회
- dependency 복잡도 증가
- 실행 시점 추적 어려움

개선:

```text
Submit Event
→ handleSubmit
→ onSearch(keyword)
```

---

### [FAQ]

Q. useEffect와 Event Handler 차이는 뭐야?
A. useEffect는 렌더링 후 외부 시스템 동기화에 사용하고 Event Handler는 사용자 행동에 직접 반응할 때 사용한다.

Q. 버튼 클릭 로직을 useEffect에 넣어도 돼?
A. 보통 넣지 않는다. 버튼 클릭은 Event Handler에서 처리하는 것이 명확하다.

Q. 초기 데이터 로딩은 어디서 해?
A. Component mount 후 필요한 초기 데이터 로딩은 보통 useEffect에서 처리한다.

---

# 3. Dependency Array

## 3.1 Dependency Array Basics

### [개념]

Dependency Array는 useEffect가 언제 다시 실행될지 결정하는 배열이다.

Effect 내부에서 참조하는 값 중 렌더링마다 바뀔 수 있는 값은 dependency로 고려해야 한다.

기본 구조:

```jsx
useEffect(() => {
  // effect logic
}, [dependency]);
```

---

### [핵심]

Dependency Array 핵심 키워드:

- dependency array
- effect dependency
- empty dependency array
- no dependency array
- dependency change
- stale value
- infinite loop
- lint warning

실행 패턴:

| 형태                  | 실행 시점                          |
| --------------------- | ---------------------------------- |
| dependency array 없음 | 렌더링 후마다 실행                 |
| `[]`                  | mount 후 실행                      |
| `[value]`             | mount 후 실행 + value 변경 시 실행 |

핵심 규칙:

- Effect가 사용하는 외부 값을 dependency로 검토
- dependency 누락 시 오래된 값 사용 가능
- dependency 과다 또는 불안정 값은 반복 실행 가능
- dependency 경고를 무조건 무시하지 않음
- Effect 목적을 먼저 정의한 뒤 dependency를 정함

---

### [실무]

빈 배열 예:

```jsx
useEffect(() => {
  document.title = "Festival List";
}, []);
```

값 변경 시 실행 예:

```jsx
function FestivalDetail({ festivalId }) {
  useEffect(() => {
    document.title = `Festival ${festivalId}`;
  }, [festivalId]);

  return <h1>Festival Detail</h1>;
}
```

dependency array 없음 예:

```jsx
useEffect(() => {
  console.log("rendered");
});
```

주의:

- dependency array가 없으면 매 렌더링 후 실행
- `[]`는 mount 후 한 번 실행 패턴으로 사용
- Props / State를 Effect에서 사용하면 dependency 확인
- 객체 / 함수 dependency는 매 렌더링마다 바뀔 수 있음
- lint 경고를 숨기기보다 Effect 구조를 재검토

---

### [FAQ]

Q. useEffect dependency array가 뭐야?
A. useEffect가 언제 다시 실행될지 결정하는 배열이다.

Q. useEffect dependency array가 비어 있으면?
A. Component mount 후 한 번 실행되는 패턴으로 사용된다.

Q. useEffect에 dependency array를 안 쓰면?
A. 렌더링될 때마다 effect가 실행된다.

Q. dependency 경고는 무시해도 돼?
A. 대부분 무시하지 않는 것이 좋다. effect가 참조하는 값과 실행 조건을 다시 검토해야 한다.

---

## 3.2 Empty Dependency Array

### [개념]

Empty Dependency Array는 `[]` 형태의 dependency array다.

`[]`는 Effect가 Component mount 후 실행되는 패턴으로 사용된다.

---

### [핵심]

Empty Dependency Array 핵심:

- `[]`
- mount effect
- initial load
- initial synchronization
- one-time setup pattern
- StrictMode caution

사용 상황:

- 초기 API 요청
- document title 초기 설정
- 초기 Event Listener 등록
- Timer 등록
- 외부 Library 초기화
- Component mount 시 1회 동기화

주의:

- 개발 StrictMode에서 두 번처럼 보일 수 있음
- Effect 내부에서 사용하는 Props / State가 있다면 dependency 누락 주의
- 정말 mount 시점만 필요한지 검토
- Cleanup 필요한 작업은 return 함수 작성

---

### [실무]

초기 API 요청 예:

```jsx
function FestivalPage() {
  const [festivals, setFestivals] = useState([]);

  useEffect(() => {
    async function loadFestivals() {
      const response = await fetch("/api/festivals");
      const data = await response.json();
      setFestivals(data);
    }

    loadFestivals();
  }, []);

  return <FestivalList festivals={festivals} />;
}
```

초기 Event Listener 등록 예:

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

- `[]`를 dependency 경고 회피 용도로 남용하지 않음
- Effect 내부에서 props 값을 사용하면 최신 값 문제가 생길 수 있음
- API 요청에 query나 id가 필요하면 dependency로 포함 검토
- mount 후 1회 실행 패턴인지 명확히 판단

---

### [FAQ]

Q. dependency array `[]`는 무슨 뜻이야?
A. Component mount 후 실행되는 Effect 패턴으로 사용된다.

Q. `[]`를 쓰면 무조건 한 번만 실행돼?
A. 운영 기준으로 mount 후 실행 패턴이지만 개발 StrictMode에서는 추가 실행처럼 보일 수 있다.

Q. `[]` 안에 값을 안 넣으면 최신 Props를 못 볼 수 있어?
A. Effect 내부에서 Props나 State를 참조한다면 dependency 누락으로 오래된 값을 사용할 수 있다.

---

## 3.3 Dependency Change

### [개념]

Dependency Change는 dependency array에 포함된 값이 이전 렌더링과 달라지는 상황이다.

Dependency가 변경되면 useEffect는 다시 실행된다.

---

### [핵심]

Dependency Change 핵심:

- dependency value
- props dependency
- state dependency
- effect re-run
- cleanup before re-run
- latest value
- synchronization

실행 Flow:

```text
Initial Render
→ Effect Run
→ Dependency Value Change
→ Cleanup Previous Effect
→ Effect Re-run
```

사용 상황:

- id 변경 시 상세 데이터 재요청
- keyword 변경 시 document title 변경
- open 상태 변경 시 event listener 처리
- selected item 변경 시 외부 동기화
- route parameter 변경 시 데이터 갱신

---

### [실무]

festivalId 변경 시 Effect 실행:

```jsx
function FestivalDetail({ festivalId }) {
  const [festival, setFestival] = useState(null);

  useEffect(() => {
    async function loadFestival() {
      const response = await fetch(`/api/festivals/${festivalId}`);
      const data = await response.json();
      setFestival(data);
    }

    loadFestival();
  }, [festivalId]);

  if (!festival) {
    return <p>Loading...</p>;
  }

  return <h1>{festival.title}</h1>;
}
```

keyword 변경 시 title 동기화:

```jsx
function SearchPage({ keyword }) {
  useEffect(() => {
    document.title = keyword ? `Search: ${keyword}` : "Search";
  }, [keyword]);

  return <h1>Search</h1>;
}
```

주의:

- dependency가 변경되면 이전 Effect cleanup 후 새 Effect 실행 가능
- Effect 내부에서 dependency State를 계속 변경하면 loop 가능
- 객체 / 함수 dependency는 참조 변경으로 자주 바뀔 수 있음
- dependency가 자주 바뀌면 Effect 목적 재검토

---

### [FAQ]

Q. dependency 값이 바뀌면 useEffect는 어떻게 돼?
A. 이전 Effect를 정리한 뒤 새 dependency 기준으로 다시 실행될 수 있다.

Q. props 값을 useEffect에서 쓰면 dependency에 넣어야 해?
A. 일반적으로 넣어야 한다. 그래야 Props 변경 시 최신 값으로 동기화된다.

Q. dependency에 State를 넣고 Effect 안에서 그 State를 바꾸면?
A. 조건 없이 반복하면 무한 실행이 발생할 수 있다.

---

## 3.4 Dependency Problem

### [개념]

Dependency Problem은 dependency array가 잘못되어 Effect가 너무 자주 실행되거나 필요한 시점에 실행되지 않는 문제다.

React useEffect 오류 중 가장 자주 발생하는 문제다.

---

### [핵심]

Dependency Problem 키워드:

- dependency missing
- dependency over-added
- infinite effect loop
- stale closure
- repeated API call
- unstable object dependency
- unstable function dependency
- eslint exhaustive deps

문제 유형:

- dependency 누락
- dependency 과다 추가
- Effect 내부 State 변경과 dependency 연결
- 매 렌더링마다 새 객체 생성
- 매 렌더링마다 새 함수 생성
- Event 로직을 Effect에 넣음
- Derived Value를 Effect로 동기화

해결 방향:

- Effect 목적 재검토
- 필요한 dependency 명시
- Event 로직은 Event Handler로 이동
- Derived Value는 렌더링 중 계산
- State 변경 조건 추가
- 객체 / 함수 dependency 구조 단순화
- Cleanup 추가

---

### [실무]

반복 API 호출 문제:

```jsx
function BadPage({ keyword }) {
  const options = { keyword };

  useEffect(() => {
    fetchFestivals(options);
  }, [options]);

  return null;
}
```

문제:

- options 객체가 렌더링마다 새로 생성
- dependency가 매번 바뀐 것으로 인식 가능

개선:

```jsx
function GoodPage({ keyword }) {
  useEffect(() => {
    fetchFestivals({ keyword });
  }, [keyword]);

  return null;
}
```

Derived State 동기화 문제:

```jsx
function BadComponent({ firstName, lastName }) {
  const [fullName, setFullName] = useState("");

  useEffect(() => {
    setFullName(`${firstName} ${lastName}`);
  }, [firstName, lastName]);

  return <p>{fullName}</p>;
}
```

개선:

```jsx
function GoodComponent({ firstName, lastName }) {
  const fullName = `${firstName} ${lastName}`;

  return <p>{fullName}</p>;
}
```

Debug Flow:

```text
Effect Problem
→ Effect 목적 확인
→ dependency array 확인
→ Effect 내부 State 변경 확인
→ 객체 / 함수 dependency 확인
→ Event Handler로 이동 가능 여부 확인
→ Derived Value 제거 가능 여부 확인
```

---

### [FAQ]

Q. useEffect에서 API가 계속 호출되는 이유는?
A. dependency가 매 렌더링마다 바뀌거나 effect 내부 State 변경이 dependency와 연결되어 있을 수 있다.

Q. dependency에 객체를 넣으면 왜 문제가 될 수 있어?
A. 객체는 렌더링마다 새 참조가 만들어질 수 있어 Effect가 반복 실행될 수 있다.

Q. Derived Value를 useEffect로 State에 저장해도 돼?
A. 대부분 피하는 것이 좋다. Props나 State로 계산 가능하면 렌더링 중 계산한다.

---

# 4. Cleanup Function

## 4.1 Cleanup Function Definition

### [개념]

Cleanup Function은 useEffect에서 등록한 외부 작업을 정리하는 함수다.

useEffect callback에서 함수를 반환하면 React는 필요 시 그 함수를 실행해 이전 Effect를 정리한다.

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

Cleanup Function 핵심 키워드:

- cleanup function
- effect cleanup
- component unmount
- dependency change cleanup
- timer cleanup
- event listener cleanup
- subscription cleanup
- websocket cleanup
- abort controller
- memory leak prevention

Cleanup 필요 상황:

- setInterval
- setTimeout
- Event Listener
- Subscription
- WebSocket Connection
- External Library Instance
- Abortable API Request
- Observer
- External Resource

---

### [실무]

Cleanup 실행 시점:

```text
Component Unmount
→ Cleanup 실행

Dependency Change
→ Previous Cleanup 실행
→ New Effect 실행
```

Timer Cleanup 예:

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
- Event Listener 제거 시 같은 handler reference 필요
- dependency 변경 전 이전 Effect가 정리됨
- StrictMode 개발 환경에서 cleanup 동작 확인 가능
- Cleanup Function에서 불필요한 State 변경 지양

---

### [FAQ]

Q. useEffect cleanup은 왜 필요해?
A. Timer, Event Listener, Subscription 같은 외부 작업이 남아 memory leak이나 중복 실행을 만들 수 있기 때문이다.

Q. cleanup은 언제 실행돼?
A. Component unmount 시 또는 dependency 변경으로 effect가 다시 실행되기 전에 실행된다.

Q. cleanup function은 어디에 작성해?
A. useEffect callback 안에서 함수를 return하는 방식으로 작성한다.

---

## 4.2 Timer Cleanup

### [개념]

Timer Cleanup은 setTimeout 또는 setInterval로 등록한 Timer를 Component unmount 또는 Effect 재실행 전에 정리하는 작업이다.

Timer를 정리하지 않으면 Component가 사라진 후에도 Timer가 계속 실행될 수 있다.

---

### [핵심]

Timer Cleanup 핵심 키워드:

- setTimeout
- setInterval
- clearTimeout
- clearInterval
- timer id
- interval cleanup
- memory leak
- duplicate timer

Timer 규칙:

- setTimeout은 clearTimeout으로 정리
- setInterval은 clearInterval로 정리
- Timer ID를 변수에 저장
- Effect cleanup에서 Timer 제거
- dependency 변경으로 Timer가 중복 등록되지 않도록 주의

---

### [실무]

setTimeout Cleanup:

```jsx
useEffect(() => {
  const timeoutId = setTimeout(() => {
    console.log("timeout");
  }, 1000);

  return () => {
    clearTimeout(timeoutId);
  };
}, []);
```

setInterval Cleanup:

```jsx
function Clock() {
  const [now, setNow] = useState(new Date());

  useEffect(() => {
    const intervalId = setInterval(() => {
      setNow(new Date());
    }, 1000);

    return () => {
      clearInterval(intervalId);
    };
  }, []);

  return <p>{now.toLocaleTimeString()}</p>;
}
```

주의:

- interval cleanup 누락 시 중복 실행 가능
- dependency 변경마다 새 Timer가 등록될 수 있음
- Timer callback에서 State 사용 시 stale value 주의
- 복잡한 Timer 로직은 Custom Hook 또는 별도 문서로 분리 가능

---

### [FAQ]

Q. setInterval은 왜 cleanup 해야 해?
A. Component가 사라진 후에도 interval이 계속 실행될 수 있기 때문이다.

Q. setTimeout도 cleanup 해야 해?
A. Component unmount 전에 timeout이 남아 있을 수 있으면 clearTimeout으로 정리하는 것이 좋다.

Q. Timer가 중복 실행되는 이유는?
A. Effect가 여러 번 실행되면서 이전 Timer를 정리하지 않았을 수 있다.

---

## 4.3 Event Listener Cleanup

### [개념]

Event Listener Cleanup은 addEventListener로 등록한 Browser Event Listener를 removeEventListener로 제거하는 작업이다.

Event Listener를 정리하지 않으면 Component가 사라진 후에도 Handler가 남아 중복 실행 또는 memory leak이 발생할 수 있다.

---

### [핵심]

Event Listener Cleanup 핵심 키워드:

- addEventListener
- removeEventListener
- same handler reference
- window event
- document event
- resize
- scroll
- keydown
- cleanup function

핵심 규칙:

- addEventListener와 removeEventListener는 같은 handler reference 사용
- Effect cleanup에서 removeEventListener 호출
- dependency 변경 시 이전 listener 정리
- 익명 함수를 직접 넣으면 제거 어려움
- 이벤트 대상 window / document / element 명확화

---

### [실무]

resize listener 예:

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

keydown listener 예:

```jsx
function EscapeClosePanel({ onClose }) {
  useEffect(() => {
    function handleKeyDown(event) {
      if (event.key === "Escape") {
        onClose();
      }
    }

    window.addEventListener("keydown", handleKeyDown);

    return () => {
      window.removeEventListener("keydown", handleKeyDown);
    };
  }, [onClose]);

  return <section>Panel</section>;
}
```

나쁜 예:

```jsx
useEffect(() => {
  window.addEventListener("resize", () => {
    console.log(window.innerWidth);
  });

  return () => {
    window.removeEventListener("resize", () => {
      console.log(window.innerWidth);
    });
  };
}, []);
```

문제:

- add와 remove에 서로 다른 함수 reference 전달
- listener가 제거되지 않음

---

### [FAQ]

Q. Event Listener는 왜 cleanup 해야 해?
A. Component가 사라진 후에도 listener가 남아 중복 실행이나 memory leak을 만들 수 있기 때문이다.

Q. removeEventListener가 안 되는 이유는?
A. addEventListener에 전달한 함수와 removeEventListener에 전달한 함수 reference가 다를 수 있다.

Q. keydown listener는 어디에 등록해?
A. 목적에 따라 window, document, 특정 element에 등록할 수 있으며 cleanup으로 제거해야 한다.

---

## 4.4 Abort API Request Basics

### [개념]

Abort API Request는 Component unmount 또는 dependency 변경 시 이전 API 요청을 취소하는 기본 패턴이다.

React Core에서는 AbortController를 기초 수준으로만 다룬다.

API 요청 심화, 캐싱, 재시도, 중복 요청 방지는 Data Fetching REST API Integration 문서에서 다룬다.

---

### [핵심]

Abort API Request 핵심 키워드:

- AbortController
- signal
- abort
- fetch cancel
- cleanup
- stale request
- race condition basics
- component unmount

사용 상황:

- Component unmount 전 요청 취소
- dependency 변경으로 이전 요청 취소
- 빠르게 변경되는 검색어 요청
- 상세 ID 변경 시 이전 요청 취소
- 느린 API 응답이 늦게 도착하는 상황 방지

---

### [실무]

AbortController 기본 예:

```jsx
function FestivalDetail({ festivalId }) {
  const [festival, setFestival] = useState(null);

  useEffect(() => {
    const controller = new AbortController();

    async function loadFestival() {
      try {
        const response = await fetch(`/api/festivals/${festivalId}`, {
          signal: controller.signal,
        });

        const data = await response.json();
        setFestival(data);
      } catch (error) {
        if (error.name === "AbortError") {
          return;
        }

        console.error(error);
      }
    }

    loadFestival();

    return () => {
      controller.abort();
    };
  }, [festivalId]);

  if (!festival) {
    return <p>Loading...</p>;
  }

  return <h1>{festival.title}</h1>;
}
```

Flow:

```text
festivalId 변경
→ Previous Effect Cleanup
→ Previous Request Abort
→ New Effect Run
→ New Request Start
```

주의:

- AbortError는 일반 오류와 분리 처리
- fetch는 HTTP 오류를 자동 throw하지 않음
- response.ok 확인은 API Call Basic 문서에서 함께 다룸
- Core 문서에서는 AbortController 기초만 포함
- 실무 데이터 요청은 Data Fetching 문서에서 심화

---

### [FAQ]

Q. API 요청도 cleanup 할 수 있어?
A. fetch 요청은 AbortController를 사용해 취소할 수 있다.

Q. dependency가 바뀔 때 이전 API 요청은 어떻게 해?
A. Cleanup Function에서 controller.abort()를 호출해 이전 요청을 취소할 수 있다.

Q. AbortError는 실패로 보여줘야 해?
A. 보통 사용자가 볼 오류로 처리하지 않고 조용히 return하는 경우가 많다.

---

# 5. useEffect Troubleshooting

## 5.1 Infinite Effect Loop

### [개념]

Infinite Effect Loop는 useEffect가 반복 실행되며 State 변경과 Re-render가 계속 이어지는 문제다.

주로 Effect dependency와 Effect 내부 State 변경이 순환 구조를 만들 때 발생한다.

---

### [핵심]

Infinite Effect Loop 핵심 키워드:

- infinite loop
- repeated effect
- repeated API call
- dependency loop
- setState inside effect
- effect dependency
- unstable dependency
- Too many re-renders

주요 원인:

- Effect가 dependency State를 변경
- dependency에 매번 새 객체 포함
- dependency에 매번 새 함수 포함
- dependency array 누락
- Derived Value를 Effect로 동기화
- Event 로직을 Effect로 처리

해결:

- Effect 목적 재검토
- State 변경 조건 추가
- Derived Value는 렌더링 중 계산
- Event 로직은 Handler로 이동
- dependency를 primitive 값 중심으로 단순화
- 불필요한 Effect 제거

---

### [실무]

나쁜 예:

```jsx
function BadCounter() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    setCount(count + 1);
  }, [count]);

  return <p>{count}</p>;
}
```

문제:

```text
count 변경
→ effect 실행
→ setCount
→ count 변경
→ effect 재실행
```

개선 방향:

```jsx
function GoodCounter() {
  const [count, setCount] = useState(0);

  return (
    <button type="button" onClick={() => setCount((prev) => prev + 1)}>
      {count}
    </button>
  );
}
```

조건부 State 변경 예:

```jsx
useEffect(() => {
  if (!loaded) {
    setLoaded(true);
  }
}, [loaded]);
```

주의:

- 조건 없는 State 변경은 loop 가능성 높음
- Effect가 꼭 필요한지 먼저 확인
- 클릭 / 제출 / 입력 로직은 Event Handler로 이동
- Derived Value 계산은 useEffect보다 렌더링 중 계산

---

### [FAQ]

Q. useEffect에서 무한 루프가 나는 이유는?
A. effect가 State를 변경하고 그 State가 dependency에 있어 다시 effect가 실행되는 구조일 수 있다.

Q. useEffect 안에서 setState를 쓰면 안 돼?
A. 사용할 수 있지만 dependency와 순환 구조를 만들지 않도록 조건과 목적을 명확히 해야 한다.

Q. useEffect가 계속 실행될 때 먼저 볼 것은?
A. dependency array, Effect 내부 setState, 객체 / 함수 dependency, Event Handler로 이동 가능성을 확인한다.

---

## 5.2 Stale Value Problem

### [개념]

Stale Value Problem은 Effect 또는 callback이 최신 Props / State가 아닌 오래된 값을 참조하는 문제다.

dependency 누락이나 비동기 callback에서 자주 발생한다.

---

### [핵심]

Stale Value 핵심 키워드:

- stale value
- stale closure
- missing dependency
- latest state
- latest props
- async callback
- interval callback
- functional update

주요 원인:

- dependency 누락
- `[]` 내부에서 변경 가능한 값을 참조
- setInterval callback이 오래된 State 참조
- 비동기 응답 시점의 값 혼동
- Event Listener가 오래된 Props 참조

해결:

- dependency array에 필요한 값 포함
- 이전 State 기반 변경은 functional update 사용
- 최신 값이 필요한 구조 재검토
- Effect 목적과 lifecycle 재정의
- 필요 시 ref 사용 검토

---

### [실무]

나쁜 예:

```jsx
function BadTimer() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const intervalId = setInterval(() => {
      setCount(count + 1);
    }, 1000);

    return () => clearInterval(intervalId);
  }, []);

  return <p>{count}</p>;
}
```

문제:

- interval callback이 초기 count를 참조
- count가 기대대로 증가하지 않을 수 있음

개선:

```jsx
function GoodTimer() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    const intervalId = setInterval(() => {
      setCount((prevCount) => prevCount + 1);
    }, 1000);

    return () => clearInterval(intervalId);
  }, []);

  return <p>{count}</p>;
}
```

Props stale 예:

```jsx
useEffect(() => {
  console.log(festivalId);
}, []);
```

개선:

```jsx
useEffect(() => {
  console.log(festivalId);
}, [festivalId]);
```

주의:

- lint dependency 경고를 무시하지 않음
- functional update는 최신 이전 State 기준 변경에 유용
- 모든 stale 문제를 ref로 해결하려 하지 않음
- ref 심화는 별도 문서에서 다룸

---

### [FAQ]

Q. Stale Value가 뭐야?
A. Effect나 callback이 최신 값이 아니라 이전 렌더링의 오래된 값을 참조하는 문제다.

Q. interval에서 State가 안 오르는 이유는?
A. interval callback이 오래된 State를 참조할 수 있다. functional update를 사용하면 안전하다.

Q. dependency를 빼면 왜 오래된 값을 볼 수 있어?
A. Effect가 다시 실행되지 않아 이전 렌더링 시점의 값을 계속 사용할 수 있기 때문이다.

---

## 5.3 Missing Cleanup Problem

### [개념]

Missing Cleanup Problem은 useEffect에서 등록한 외부 작업을 정리하지 않아 중복 실행, memory leak, stale listener가 발생하는 문제다.

Timer, Event Listener, Subscription에서 자주 발생한다.

---

### [핵심]

Missing Cleanup 핵심 키워드:

- missing cleanup
- memory leak
- duplicate interval
- duplicate event listener
- stale subscription
- unmount cleanup
- dependency change cleanup

주요 증상:

- interval이 여러 번 실행됨
- event handler가 중복 호출됨
- Component unmount 후에도 작업 실행
- 오래된 Props / State로 listener 실행
- 개발 StrictMode에서 문제가 더 빨리 드러남

해결:

- Effect에서 cleanup function 반환
- Timer는 clearTimeout / clearInterval
- Event Listener는 removeEventListener
- Subscription은 unsubscribe
- WebSocket은 close
- API 요청은 필요 시 abort

---

### [실무]

나쁜 예:

```jsx
useEffect(() => {
  setInterval(() => {
    console.log("tick");
  }, 1000);
}, []);
```

개선:

```jsx
useEffect(() => {
  const intervalId = setInterval(() => {
    console.log("tick");
  }, 1000);

  return () => {
    clearInterval(intervalId);
  };
}, []);
```

Event Listener 누락:

```jsx
useEffect(() => {
  function handleScroll() {
    console.log(window.scrollY);
  }

  window.addEventListener("scroll", handleScroll);
}, []);
```

개선:

```jsx
useEffect(() => {
  function handleScroll() {
    console.log(window.scrollY);
  }

  window.addEventListener("scroll", handleScroll);

  return () => {
    window.removeEventListener("scroll", handleScroll);
  };
}, []);
```

Debug Flow:

```text
중복 실행 발생
→ Effect 실행 횟수 확인
→ Timer / Listener 등록 확인
→ Cleanup Function 유무 확인
→ Dependency 변경 시 정리 여부 확인
→ StrictMode 영향 확인
```

---

### [FAQ]

Q. cleanup이 없으면 어떤 문제가 생겨?
A. Timer나 Event Listener가 남아 중복 실행, memory leak, 오래된 값 참조 문제가 생길 수 있다.

Q. 이벤트가 두 번씩 실행되는 이유는?
A. Event Listener가 중복 등록되고 cleanup이 누락되었을 수 있다.

Q. StrictMode에서 cleanup 문제가 더 잘 보이는 이유는?
A. 개발 중 Effect와 cleanup 동작을 추가로 확인해 부작용 문제를 드러내기 때문이다.

---

# 6. Comparison

## 6.1 Required Comparisons

### [개념]

React Core Part05는 Hook, useEffect, dependency, cleanup에서 헷갈리는 개념을 비교해서 작성한다.

비교는 Retrieval Hit와 Agent 판단 정확도를 높인다.

---

### [핵심]

필수 비교 대상:

- useState vs useEffect
- useEffect vs Event Handler
- Render Phase vs Effect
- Dependency Array 없음 vs Empty Dependency Array
- Dependency Change vs Re-render
- Cleanup Function vs 일반 return
- Timer Cleanup vs Event Listener Cleanup
- Missing Dependency vs Infinite Loop
- Stale Value vs Latest State
- Side Effect vs Derived Value

---

### [실무]

useState vs useEffect:

| 비교      | useState                | useEffect             |
| --------- | ----------------------- | --------------------- |
| 목적      | UI State 관리           | 외부 시스템 동기화    |
| 실행      | 렌더링 중 State 값 제공 | 렌더링 후 Effect 실행 |
| 대표 작업 | input, toggle, loading  | API, timer, listener  |
| 변경 방식 | setter function         | dependency 기준 실행  |
| 주의      | 직접 mutation 금지      | dependency loop 주의  |

useEffect vs Event Handler:

| 비교      | useEffect                 | Event Handler           |
| --------- | ------------------------- | ----------------------- |
| 실행 원인 | 렌더링 후 dependency 변화 | 사용자 이벤트           |
| 목적      | 외부 시스템 동기화        | 클릭 / 입력 / 제출 처리 |
| 예시      | 초기 API 호출             | 검색 버튼 클릭          |
| cleanup   | 가능                      | 일반적으로 없음         |
| 실무 기준 | synchronization           | user action             |

Dependency Array 없음 vs Empty Dependency Array:

| 비교        | dependency array 없음 | `[]`               |
| ----------- | --------------------- | ------------------ |
| 실행 시점   | 렌더링 후마다 실행    | mount 후 실행 패턴 |
| 반복 가능성 | 높음                  | 낮음               |
| 사용 예     | 렌더링마다 로그       | 초기 설정          |
| 주의        | 반복 실행             | stale value 가능   |

---

### [FAQ]

Q. useState와 useEffect 차이는?
A. useState는 UI State 관리용이고 useEffect는 외부 시스템 동기화용이다.

Q. Dependency Array 없음과 [] 차이는?
A. dependency array가 없으면 렌더링 후마다 실행되고 `[]`는 mount 후 실행 패턴으로 사용된다.

Q. Side Effect와 Derived Value 차이는?
A. Side Effect는 외부 시스템에 영향을 주는 작업이고 Derived Value는 Props나 State로 계산 가능한 값이다.

---

# 7. Checklist

## 7.1 Part05 Quality Checklist

### [개념]

React Core Part05 검수는 Hook Basics, useEffect, Dependency Array, Cleanup Function, Troubleshooting을 기준으로 수행한다.

---

### [핵심]

Checklist:

```md
- [ ] Hook 기본 개념이 포함되었는가?
- [ ] Rules of Hooks가 포함되었는가?
- [ ] Hook을 조건문 / 반복문 / 일반 함수에서 호출 금지하는 규칙이 포함되었는가?
- [ ] useEffect 기본 개념이 포함되었는가?
- [ ] useEffect가 외부 시스템 동기화용임을 설명했는가?
- [ ] Side Effect 개념이 포함되었는가?
- [ ] useEffect vs Event Handler 비교가 포함되었는가?
- [ ] Dependency Array 기본 개념이 포함되었는가?
- [ ] Empty Dependency Array 설명이 포함되었는가?
- [ ] Dependency Change 설명이 포함되었는가?
- [ ] Dependency Problem이 포함되었는가?
- [ ] Cleanup Function 기본 개념이 포함되었는가?
- [ ] Timer Cleanup이 포함되었는가?
- [ ] Event Listener Cleanup이 포함되었는가?
- [ ] Abort API Request 기초가 포함되었는가?
- [ ] Infinite Effect Loop가 포함되었는가?
- [ ] Stale Value Problem이 포함되었는가?
- [ ] Missing Cleanup Problem이 포함되었는가?
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
→ Hook Rule Check
→ useEffect Purpose Check
→ Dependency Array Check
→ Cleanup Function Check
→ Troubleshooting Check
→ FAQ Check
→ Retrieval Queries Check
→ Final Review
```

치명적 문제 기준:

- Hook을 조건문 내부에서 호출하는 예제를 정상 예제로 제공
- useEffect를 모든 로직 처리 장소처럼 설명
- Event Handler로 처리할 일을 useEffect로 우회
- dependency warning 무시를 일반 권장처럼 설명
- cleanup 없는 timer / listener 예제를 정상 예제로 제공
- Render Phase에서 Side Effect 실행을 정상 예제로 제공
- FAQ 누락
- Retrieval Queries 누락

---

### [FAQ]

Q. Part05에서 가장 중요한 검수 기준은?
A. Rules of Hooks, useEffect 목적, dependency array, cleanup function, infinite loop, stale value 포함 여부다.

Q. Part05에서 다루면 안 되는 내용은?
A. useMemo, useCallback, React.memo, Custom Hook 설계, Suspense, Concurrent Rendering 심화는 제외한다.

---

# Retrieval Queries

### [FAQ]

Q. Hook이 뭐야?
A. Functional Component에서 React 기능을 사용할 수 있게 해주는 함수다.

Q. React Core에서 가장 중요한 Hook은 뭐야?
A. useState와 useEffect다.

Q. Hook은 왜 필요해?
A. Functional Component에서 State, Effect, Ref 같은 React 기능을 사용하기 위해 필요하다.

Q. Hook은 왜 조건문 안에서 호출하면 안 돼?
A. React는 Hook 호출 순서로 상태를 관리한다. 조건에 따라 호출 순서가 바뀌면 상태 연결이 깨질 수 있다.

Q. Hook은 일반 함수에서 호출해도 돼?
A. 안 된다. React Component 또는 Custom Hook 내부에서 호출해야 한다.

Q. Custom Hook 이름은 왜 use로 시작해야 해?
A. React와 lint 도구가 Hook 규칙을 검사할 수 있게 하기 위해서다.

Q. React Core에서 모든 Hook을 깊게 다뤄?
A. 아니다. useState와 useEffect를 중심으로 다루고 고급 Hook은 별도 문서에서 다룬다.

Q. useMemo와 useCallback은 React Core에서 다뤄?
A. 기본 언급은 가능하지만 성능 최적화 심화는 React Performance 또는 Advanced React Pattern 문서에서 다룬다.

Q. useContext는 React Core 범위야?
A. 기초 소개는 가능하지만 전역 상태 설계는 State Management 문서에서 다룬다.

Q. useEffect는 언제 써?
A. Component가 렌더링된 후 외부 시스템과 동기화해야 할 때 사용한다.

Q. useEffect는 렌더링 전에 실행돼?
A. 아니다. 보통 렌더링 결과가 DOM에 반영된 후 실행된다.

Q. 모든 로직을 useEffect에 넣으면 돼?
A. 아니다. 사용자 이벤트로 처리할 수 있는 로직은 Event Handler에서 처리한다.

Q. API 요청은 Component 본문에서 바로 하면 안 돼?
A. 렌더링마다 요청이 실행될 수 있어 useEffect 또는 Event Handler에서 처리해야 한다.

Q. Side Effect가 뭐야?
A. Component 렌더링 결과 계산 외부에 영향을 주는 작업이다.

Q. Side Effect는 어디서 처리해?
A. 외부 시스템 동기화는 useEffect에서, 사용자 이벤트에 대한 직접 반응은 Event Handler에서 처리한다.

Q. localStorage 작업은 무조건 useEffect에서 해?
A. 렌더링 후 동기화 목적이면 useEffect, 버튼 클릭 저장처럼 사용자 이벤트라면 Event Handler에서 처리한다.

Q. useEffect와 Event Handler 차이는 뭐야?
A. useEffect는 렌더링 후 외부 시스템 동기화에 사용하고 Event Handler는 사용자 행동에 직접 반응할 때 사용한다.

Q. 버튼 클릭 로직을 useEffect에 넣어도 돼?
A. 보통 넣지 않는다. 버튼 클릭은 Event Handler에서 처리하는 것이 명확하다.

Q. 초기 데이터 로딩은 어디서 해?
A. Component mount 후 필요한 초기 데이터 로딩은 보통 useEffect에서 처리한다.

Q. useEffect dependency array가 뭐야?
A. useEffect가 언제 다시 실행될지 결정하는 배열이다.

Q. useEffect dependency array가 비어 있으면?
A. Component mount 후 한 번 실행되는 패턴으로 사용된다.

Q. useEffect에 dependency array를 안 쓰면?
A. 렌더링될 때마다 effect가 실행된다.

Q. dependency 경고는 무시해도 돼?
A. 대부분 무시하지 않는 것이 좋다. effect가 참조하는 값과 실행 조건을 다시 검토해야 한다.

Q. dependency array []는 무슨 뜻이야?
A. Component mount 후 실행되는 Effect 패턴으로 사용된다.

Q. []를 쓰면 무조건 한 번만 실행돼?
A. 운영 기준으로 mount 후 실행 패턴이지만 개발 StrictMode에서는 추가 실행처럼 보일 수 있다.

Q. [] 안에 값을 안 넣으면 최신 Props를 못 볼 수 있어?
A. Effect 내부에서 Props나 State를 참조한다면 dependency 누락으로 오래된 값을 사용할 수 있다.

Q. dependency 값이 바뀌면 useEffect는 어떻게 돼?
A. 이전 Effect를 정리한 뒤 새 dependency 기준으로 다시 실행될 수 있다.

Q. props 값을 useEffect에서 쓰면 dependency에 넣어야 해?
A. 일반적으로 넣어야 한다. 그래야 Props 변경 시 최신 값으로 동기화된다.

Q. dependency에 State를 넣고 Effect 안에서 그 State를 바꾸면?
A. 조건 없이 반복하면 무한 실행이 발생할 수 있다.

Q. useEffect에서 API가 계속 호출되는 이유는?
A. dependency가 매 렌더링마다 바뀌거나 effect 내부 State 변경이 dependency와 연결되어 있을 수 있다.

Q. dependency에 객체를 넣으면 왜 문제가 될 수 있어?
A. 객체는 렌더링마다 새 참조가 만들어질 수 있어 Effect가 반복 실행될 수 있다.

Q. Derived Value를 useEffect로 State에 저장해도 돼?
A. 대부분 피하는 것이 좋다. Props나 State로 계산 가능하면 렌더링 중 계산한다.

Q. useEffect cleanup은 왜 필요해?
A. Timer, Event Listener, Subscription 같은 외부 작업이 남아 memory leak이나 중복 실행을 만들 수 있기 때문이다.

Q. cleanup은 언제 실행돼?
A. Component unmount 시 또는 dependency 변경으로 effect가 다시 실행되기 전에 실행된다.

Q. cleanup function은 어디에 작성해?
A. useEffect callback 안에서 함수를 return하는 방식으로 작성한다.

Q. setInterval은 왜 cleanup 해야 해?
A. Component가 사라진 후에도 interval이 계속 실행될 수 있기 때문이다.

Q. setTimeout도 cleanup 해야 해?
A. Component unmount 전에 timeout이 남아 있을 수 있으면 clearTimeout으로 정리하는 것이 좋다.

Q. Timer가 중복 실행되는 이유는?
A. Effect가 여러 번 실행되면서 이전 Timer를 정리하지 않았을 수 있다.

Q. Event Listener는 왜 cleanup 해야 해?
A. Component가 사라진 후에도 listener가 남아 중복 실행이나 memory leak을 만들 수 있기 때문이다.

Q. removeEventListener가 안 되는 이유는?
A. addEventListener에 전달한 함수와 removeEventListener에 전달한 함수 reference가 다를 수 있다.

Q. keydown listener는 어디에 등록해?
A. 목적에 따라 window, document, 특정 element에 등록할 수 있으며 cleanup으로 제거해야 한다.

Q. API 요청도 cleanup 할 수 있어?
A. fetch 요청은 AbortController를 사용해 취소할 수 있다.

Q. dependency가 바뀔 때 이전 API 요청은 어떻게 해?
A. Cleanup Function에서 controller.abort()를 호출해 이전 요청을 취소할 수 있다.

Q. AbortError는 실패로 보여줘야 해?
A. 보통 사용자가 볼 오류로 처리하지 않고 조용히 return하는 경우가 많다.

Q. useEffect에서 무한 루프가 나는 이유는?
A. effect가 State를 변경하고 그 State가 dependency에 있어 다시 effect가 실행되는 구조일 수 있다.

Q. useEffect 안에서 setState를 쓰면 안 돼?
A. 사용할 수 있지만 dependency와 순환 구조를 만들지 않도록 조건과 목적을 명확히 해야 한다.

Q. useEffect가 계속 실행될 때 먼저 볼 것은?
A. dependency array, Effect 내부 setState, 객체 / 함수 dependency, Event Handler로 이동 가능성을 확인한다.

Q. Stale Value가 뭐야?
A. Effect나 callback이 최신 값이 아니라 이전 렌더링의 오래된 값을 참조하는 문제다.

Q. interval에서 State가 안 오르는 이유는?
A. interval callback이 오래된 State를 참조할 수 있다. functional update를 사용하면 안전하다.

Q. dependency를 빼면 왜 오래된 값을 볼 수 있어?
A. Effect가 다시 실행되지 않아 이전 렌더링 시점의 값을 계속 사용할 수 있기 때문이다.

Q. cleanup이 없으면 어떤 문제가 생겨?
A. Timer나 Event Listener가 남아 중복 실행, memory leak, 오래된 값 참조 문제가 생길 수 있다.

Q. 이벤트가 두 번씩 실행되는 이유는?
A. Event Listener가 중복 등록되고 cleanup이 누락되었을 수 있다.

Q. StrictMode에서 cleanup 문제가 더 잘 보이는 이유는?
A. 개발 중 Effect와 cleanup 동작을 추가로 확인해 부작용 문제를 드러내기 때문이다.

Q. useState와 useEffect 차이는?
A. useState는 UI State 관리용이고 useEffect는 외부 시스템 동기화용이다.

Q. Dependency Array 없음과 [] 차이는?
A. dependency array가 없으면 렌더링 후마다 실행되고 `[]`는 mount 후 실행 패턴으로 사용된다.

Q. Side Effect와 Derived Value 차이는?
A. Side Effect는 외부 시스템에 영향을 주는 작업이고 Derived Value는 Props나 State로 계산 가능한 값이다.

Q. React Core Part05 다음 문서는 뭐가 좋아?
A. API Call Basic, React TypeScript Basics, File Structure, Debugging, Common Mistakes, Final Checklist를 다루는 React Core Part06으로 이어지는 것이 좋다.
