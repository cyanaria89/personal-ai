# React Core Part06 - API Call Basic, React TypeScript Basics, File Structure, Debugging, Final Checklist

---

# 1. API Call Basic

## 1.1 API Call in React Core

### [개념]

React에서 API Call은 서버 데이터를 요청하고 응답 데이터를 State에 저장한 뒤 UI로 렌더링하는 흐름이다.

React Core에서는 Fetch API, useEffect, useState를 조합한 기본 API Call Pattern을 다룬다.

API Call은 Data Fetching REST API Integration 문서로 이어지는 기초 범위다.

---

### [핵심]

API Call 핵심 키워드:

- API Call
- Fetch API
- useEffect
- useState
- loading state
- error state
- data state
- empty state
- response.ok
- async function
- try catch finally
- AbortController basics
- API function separation

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

핵심 규칙:

- 초기 데이터 로딩은 보통 useEffect에서 처리
- 사용자 이벤트 요청은 Event Handler에서 처리
- API 응답 데이터는 State에 저장
- loading / error / empty / success UI 분리
- fetch는 HTTP 오류를 자동 throw하지 않음
- response.ok 확인 필요
- Component 본문에서 API 요청 직접 실행 금지

---

### [실무]

기본 API Call 예:

```jsx
function FestivalPage() {
  const [festivals, setFestivals] = useState([]);
  const [loading, setLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

  useEffect(() => {
    async function loadFestivals() {
      setLoading(true);
      setErrorMessage("");

      try {
        const response = await fetch("/api/festivals");

        if (!response.ok) {
          throw new Error("Failed to load festivals");
        }

        const data = await response.json();
        setFestivals(data);
      } catch (error) {
        setErrorMessage("축제 목록을 불러오지 못했습니다.");
      } finally {
        setLoading(false);
      }
    }

    loadFestivals();
  }, []);

  if (loading) {
    return <p>Loading...</p>;
  }

  if (errorMessage) {
    return <p>{errorMessage}</p>;
  }

  if (festivals.length === 0) {
    return <p>No festivals found.</p>;
  }

  return <FestivalList festivals={festivals} />;
}
```

주의:

- fetch는 네트워크 오류는 reject하지만 HTTP 400 / 500은 자동 throw하지 않음
- response.ok 확인 후 직접 Error 처리
- 배열 응답 State 초기값은 `[]` 권장
- 단일 객체 응답 State 초기값은 `null` 가능
- API 요청 중 unmount 가능성이 있으면 AbortController 검토
- API 요청 심화는 Data Fetching REST API Integration 문서에서 다룸

---

### [FAQ]

Q. React에서 API 호출은 어디서 해?
A. 초기 데이터 로딩은 보통 useEffect에서 처리하고 사용자 이벤트 요청은 Event Handler에서 처리한다.

Q. API 호출 상태는 어떤 State로 나눠?
A. data, loading, error, empty 상태를 분리하는 것이 좋다.

Q. fetch 실패 처리는 어떻게 해?
A. response.ok를 확인하고 실패 시 error state를 설정해 사용자에게 안내한다.

Q. Component 본문에서 fetch를 바로 실행하면 안 돼?
A. 렌더링마다 요청이 실행될 수 있어 useEffect 또는 Event Handler에서 처리해야 한다.

---

## 1.2 Loading Error Empty Success Pattern

### [개념]

Loading Error Empty Success Pattern은 API 기반 화면에서 상태별 UI를 명확히 분리하는 패턴이다.

비동기 화면은 요청 전, 요청 중, 요청 실패, 요청 성공 후 데이터 없음, 요청 성공 후 데이터 있음 상태를 구분해야 한다.

---

### [핵심]

상태 구분:

| 상태    | 의미                    | State 예              |
| ------- | ----------------------- | --------------------- |
| loading | 요청 진행 중            | `loading === true`    |
| error   | 요청 실패               | `errorMessage !== ""` |
| empty   | 요청 성공 + 데이터 없음 | `data.length === 0`   |
| success | 요청 성공 + 데이터 있음 | `data.length > 0`     |

핵심 키워드:

- loading state
- error state
- empty state
- success state
- data state
- conditional rendering
- user feedback
- API response state

핵심 규칙:

- loading과 empty를 혼동하지 않음
- error와 empty를 혼동하지 않음
- error 발생 시 사용자 안내 UI 제공
- empty 상태도 정상 상태로 처리
- success UI는 data 존재 기준으로 렌더링

---

### [실무]

상태별 렌더링 예:

```jsx
function FestivalContent({ loading, errorMessage, festivals }) {
  if (loading) {
    return <p>Loading festivals...</p>;
  }

  if (errorMessage) {
    return <p>{errorMessage}</p>;
  }

  if (festivals.length === 0) {
    return <p>No festivals found.</p>;
  }

  return <FestivalList festivals={festivals} />;
}
```

단일 상세 데이터 예:

```jsx
function FestivalDetailContent({ loading, errorMessage, festival }) {
  if (loading) {
    return <p>Loading festival...</p>;
  }

  if (errorMessage) {
    return <p>{errorMessage}</p>;
  }

  if (!festival) {
    return <p>No festival selected.</p>;
  }

  return (
    <article>
      <h1>{festival.title}</h1>
      <p>{festival.region}</p>
    </article>
  );
}
```

주의:

- 배열 데이터는 `length`로 empty 확인
- 객체 데이터는 null 여부 확인
- API 응답 구조가 `{ data: [...] }`인지 `[...]`인지 확인
- loading false 이후 empty 판단
- error가 있으면 empty UI보다 error UI 우선

---

### [FAQ]

Q. loading과 empty 차이는 뭐야?
A. loading은 요청 진행 중이고 empty는 요청 성공 후 표시할 데이터가 없는 상태다.

Q. error와 empty 차이는 뭐야?
A. error는 요청 실패 상태이고 empty는 요청 성공 후 데이터가 없는 정상 상태다.

Q. API 데이터가 null일 때 어떻게 렌더링해?
A. null 체크 후 fallback UI를 먼저 반환하고 데이터가 있을 때 상세 UI를 렌더링한다.

---

## 1.3 API Function Separation

### [개념]

API Function Separation은 Component 내부의 API 요청 로직을 별도 함수 또는 api 파일로 분리하는 방식이다.

간단한 예제는 Component 안에 API 요청을 작성할 수 있지만, 재사용되거나 복잡한 요청은 api 파일로 분리하는 것이 좋다.

---

### [핵심]

API Function Separation 핵심 키워드:

- api folder
- API function
- fetch wrapper
- reusable request
- component separation
- service function
- response handling
- error handling

분리 기준:

- 여러 Component에서 같은 API 사용
- 요청 URL이 복잡함
- 공통 header 필요
- 인증 token 필요
- error handling 공통화 필요
- Component 코드가 길어짐
- 테스트 / 검토가 필요함

---

### [실무]

api 파일 예:

```javascript
// api/festivalApi.js
export async function getFestivals() {
  const response = await fetch("/api/festivals");

  if (!response.ok) {
    throw new Error("Failed to load festivals");
  }

  return response.json();
}
```

Component 사용 예:

```jsx
import { getFestivals } from "../api/festivalApi";

function FestivalPage() {
  const [festivals, setFestivals] = useState([]);
  const [loading, setLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState("");

  useEffect(() => {
    async function loadFestivals() {
      setLoading(true);
      setErrorMessage("");

      try {
        const data = await getFestivals();
        setFestivals(data);
      } catch (error) {
        setErrorMessage("축제 목록을 불러오지 못했습니다.");
      } finally {
        setLoading(false);
      }
    }

    loadFestivals();
  }, []);

  return (
    <FestivalContent
      loading={loading}
      errorMessage={errorMessage}
      festivals={festivals}
    />
  );
}
```

주의:

- API 함수는 UI State를 직접 알지 않게 작성
- Component는 loading / error / data State 관리
- fetch wrapper 심화는 Data Fetching 문서에서 다룸
- Axios / TanStack Query 심화는 React Core 범위 제외
- 인증 header 처리는 Authentication Frontend Flow 문서와 연결

---

### [FAQ]

Q. API 호출 함수는 Component 안에 둬도 돼?
A. 간단한 예제는 가능하지만 재사용되거나 복잡하면 api 파일로 분리하는 것이 좋다.

Q. api 파일에는 무엇을 넣어?
A. 서버 요청 함수, URL 처리, response.ok 확인, response json 변환 같은 요청 관련 로직을 넣는다.

Q. loading State는 api 함수에 넣어?
A. 보통 loading, error, data State는 Component에서 관리하고 api 함수는 요청과 응답 처리에 집중한다.

---

# 2. React TypeScript Basics

## 2.1 Props Type

### [개념]

React TypeScript에서 Props Type은 Component가 받는 Props의 구조를 정의하는 타입이다.

Props Type은 Component 입력값을 명확하게 만들고 잘못된 Props 전달을 줄인다.

---

### [핵심]

Props Type 핵심 키워드:

- Props Type
- type
- interface
- string
- number
- boolean
- nullable prop
- optional prop
- callback prop
- children
- ReactNode

기본 규칙:

- Props 구조를 type 또는 interface로 정의
- required props와 optional props 구분
- nullable 값은 union type 사용
- callback props는 함수 타입으로 정의
- children은 ReactNode 사용 가능
- Component와 가까운 위치에 Props Type 작성 가능

---

### [실무]

Props Type 예:

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
    <article className="festival-card">
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

children Type 예:

```tsx
import type { ReactNode } from "react";

type CardProps = {
  children: ReactNode;
};

function Card({ children }: CardProps) {
  return <section className="card">{children}</section>;
}
```

주의:

- imageUrl처럼 없을 수 있는 값은 `string | null`
- 선택 Props는 `label?: string`
- callback props는 인자와 반환 타입 명확화
- 불필요한 any 사용 금지
- React.FC 사용은 필수가 아님

---

### [FAQ]

Q. React Props Type은 어떻게 정의해?
A. type 또는 interface로 Props 구조를 정의하고 Component parameter에 적용한다.

Q. optional prop은 어떻게 써?
A. `label?: string`처럼 property 이름 뒤에 `?`를 붙인다.

Q. nullable prop은 어떻게 써?
A. `imageUrl: string | null`처럼 union type을 사용한다.

Q. children Type은 뭐로 써?
A. 일반적으로 ReactNode를 사용할 수 있다.

---

## 2.2 State Type

### [개념]

React TypeScript에서 State Type은 useState가 관리하는 값의 타입을 명확히 지정하는 방식이다.

초기값만으로 타입 추론이 어려운 경우 useState Generic을 사용한다.

---

### [핵심]

State Type 핵심 키워드:

- useState generic
- string state
- boolean state
- number state
- array state
- object state
- nullable state
- union type

기본 규칙:

- 문자열 초기값은 `useState("")`
- boolean 초기값은 `useState(false)`
- number 초기값은 `useState(0)`
- 빈 배열은 Generic 명시 권장
- null 초기값은 union type 필요
- 객체 State는 type 정의 권장

---

### [실무]

배열 State Type 예:

```tsx
type Festival = {
  festivalId: number;
  title: string;
  region: string;
};

const [festivals, setFestivals] = useState<Festival[]>([]);
```

Nullable State Type 예:

```tsx
type Festival = {
  festivalId: number;
  title: string;
};

const [selectedFestival, setSelectedFestival] = useState<Festival | null>(null);
```

ID State 예:

```tsx
const [selectedFestivalId, setSelectedFestivalId] = useState<number | null>(
  null,
);
```

객체 State 예:

```tsx
type FestivalForm = {
  title: string;
  region: string;
};

const [form, setForm] = useState<FestivalForm>({
  title: "",
  region: "",
});
```

주의:

- `useState([])`는 never[]로 추론될 수 있음
- null 초기값은 TypeScript가 이후 객체 타입을 알 수 없음
- 가능한 한 any 사용 금지
- API 응답 타입과 State 타입 정합성 유지
- 복잡한 서버 타입은 shared types 파일로 분리 가능

---

### [FAQ]

Q. useState 빈 배열 타입은 어떻게 써?
A. TypeScript에서는 `useState<Festival[]>([])`처럼 Generic으로 요소 타입을 명시한다.

Q. null 초기값 State는 어떻게 타입 지정해?
A. `useState<Festival | null>(null)`처럼 union type을 사용한다.

Q. useState에 any를 써도 돼?
A. 가능은 하지만 타입 안정성이 떨어지므로 구체적인 타입을 정의하는 것이 좋다.

---

## 2.3 Event Type

### [개념]

React TypeScript에서 Event Type은 Event Handler가 받는 event object의 타입을 지정하는 방식이다.

Event Type은 input, form, button 등 이벤트 대상 Element에 따라 달라진다.

---

### [핵심]

Event Type 핵심 키워드:

- ChangeEvent
- FormEvent
- MouseEvent
- KeyboardEvent
- HTMLInputElement
- HTMLFormElement
- HTMLButtonElement
- event.target.value
- event.currentTarget

자주 쓰는 Event Type:

| 이벤트            | 타입 예                            |
| ----------------- | ---------------------------------- |
| input onChange    | `ChangeEvent<HTMLInputElement>`    |
| textarea onChange | `ChangeEvent<HTMLTextAreaElement>` |
| select onChange   | `ChangeEvent<HTMLSelectElement>`   |
| form onSubmit     | `FormEvent<HTMLFormElement>`       |
| button onClick    | `MouseEvent<HTMLButtonElement>`    |
| keydown           | `KeyboardEvent<HTMLInputElement>`  |

---

### [실무]

Input Change Event 예:

```tsx
import type { ChangeEvent } from "react";

function SearchInput() {
  const [keyword, setKeyword] = useState("");

  function handleChange(event: ChangeEvent<HTMLInputElement>): void {
    setKeyword(event.target.value);
  }

  return <input value={keyword} onChange={handleChange} />;
}
```

Form Submit Event 예:

```tsx
import type { FormEvent } from "react";

function SearchForm() {
  function handleSubmit(event: FormEvent<HTMLFormElement>): void {
    event.preventDefault();
  }

  return (
    <form onSubmit={handleSubmit}>
      <button type="submit">Search</button>
    </form>
  );
}
```

Button Click Event 예:

```tsx
import type { MouseEvent } from "react";

function handleClick(event: MouseEvent<HTMLButtonElement>): void {
  console.log(event.currentTarget.name);
}
```

주의:

- input 값은 `event.target.value`
- checkbox는 `event.target.checked`
- currentTarget은 Handler가 연결된 요소 기준
- Event Type은 대상 Element와 함께 작성
- inline handler는 타입 추론이 가능하지만 분리 함수는 명시 권장

---

### [FAQ]

Q. input onChange 타입은 뭐야?
A. TypeScript React에서는 일반적으로 `ChangeEvent<HTMLInputElement>`를 사용한다.

Q. form onSubmit 타입은 뭐야?
A. `FormEvent<HTMLFormElement>`를 사용한다.

Q. button onClick 타입은 뭐야?
A. `MouseEvent<HTMLButtonElement>`를 사용할 수 있다.

Q. Event Type은 꼭 써야 해?
A. 분리된 Handler 함수에서는 명시하는 것이 타입 안정성과 가독성에 좋다.

---

## 2.4 React TypeScript Common Rules

### [개념]

React TypeScript Common Rules는 Props, State, Event, API 응답 타입을 일관되게 작성하기 위한 기본 규칙이다.

React Core에서는 타입 안정성을 높이는 기초 패턴만 다룬다.

---

### [핵심]

TypeScript Common Rules:

- Props Type 정의
- State Type 명시
- Event Type 명시
- API Response Type 정의
- nullable 값 처리
- optional 값 처리
- callback props 타입 명확화
- any 사용 최소화
- React.FC 강제하지 않음
- shared type 분리 가능

---

### [실무]

API Response Type 예:

```tsx
type Festival = {
  festivalId: number;
  title: string;
  region: string;
  imageUrl: string | null;
};

async function getFestivals(): Promise<Festival[]> {
  const response = await fetch("/api/festivals");

  if (!response.ok) {
    throw new Error("Failed to load festivals");
  }

  return response.json();
}
```

Component 연결 예:

```tsx
function FestivalPage() {
  const [festivals, setFestivals] = useState<Festival[]>([]);

  useEffect(() => {
    async function loadFestivals(): Promise<void> {
      const data = await getFestivals();
      setFestivals(data);
    }

    loadFestivals();
  }, []);

  return <FestivalList festivals={festivals} />;
}
```

주의:

- 서버 응답 구조와 타입을 맞춤
- null 가능한 필드는 union type으로 표현
- optional과 nullable을 구분
- `any`보다 `unknown` 또는 구체 타입 검토
- TypeScript 심화는 TypeScript Foundation / Frontend Architecture 문서와 연결

---

### [FAQ]

Q. React.FC를 꼭 써야 해?
A. 필수는 아니다. 프로젝트 컨벤션에 따라 사용 여부를 결정한다.

Q. optional과 nullable 차이는?
A. optional은 property 자체가 없을 수 있고 nullable은 property는 있지만 값이 null일 수 있다.

Q. API 응답 타입은 어디에 둬?
A. 작으면 Component 근처에 두고 여러 곳에서 쓰면 types 폴더나 api 타입 파일로 분리한다.

---

# 3. File Structure

## 3.1 React Basic File Structure

### [개념]

React File Structure는 Component, Page, API, Utility, Type, Style 파일을 역할별로 분리하는 구조다.

React Core에서는 기본적인 역할 분리와 파일 위치 기준만 다룬다.

---

### [핵심]

File Structure 핵심 키워드:

- components
- pages
- api
- hooks
- utils
- types
- styles
- assets
- file naming
- index file caution

기본 구조:

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
├ styles
│  └ global.css
└ assets
   └ logo.svg
```

---

### [실무]

역할 기준:

| 폴더       | 역할                      |
| ---------- | ------------------------- |
| components | 재사용 UI Component       |
| pages      | 화면 단위 Component       |
| api        | 서버 요청 함수            |
| hooks      | Custom Hook               |
| utils      | 순수 유틸 함수            |
| types      | 공통 TypeScript Type      |
| styles     | 공통 스타일               |
| assets     | 이미지, 아이콘, 정적 자산 |

파일 분리 기준:

- Page Component는 pages
- 재사용 가능한 UI는 components
- API 요청 함수는 api
- 순수 계산 함수는 utils
- 공통 타입은 types
- 공통 스타일은 styles
- 이미지 / 아이콘은 assets

주의:

- 모든 코드를 App.jsx에 몰아넣지 않음
- Component가 커지면 분리
- API 요청 함수는 분리 가능
- 파일명은 Component 이름과 일치 권장
- 프로젝트 컨벤션 우선
- index 파일 남용은 import 추적을 어렵게 할 수 있음

---

### [FAQ]

Q. Component 파일은 어디에 둬?
A. 재사용 Component는 components 폴더, 화면 단위 Component는 pages 폴더에 두는 방식이 일반적이다.

Q. API 호출 함수는 어디에 둬?
A. 재사용되거나 복잡한 API 요청 함수는 api 폴더에 둔다.

Q. 모든 코드를 App.jsx에 넣어도 돼?
A. 작은 실습은 가능하지만 실무 프로젝트에서는 역할별 파일 분리가 필요하다.

---

## 3.2 Component File Separation

### [개념]

Component File Separation은 하나의 파일이 너무 커지거나 역할이 섞일 때 Component를 별도 파일로 분리하는 방식이다.

Component 분리는 재사용성, 가독성, 검토 가능성, RAG Retrieval 품질을 높인다.

---

### [핵심]

Component 분리 기준:

- UI 블록이 재사용됨
- JSX가 길어짐
- 조건부 렌더링이 복잡함
- List Item UI가 커짐
- Props / State 책임이 분리됨
- Page와 UI 역할이 섞임
- 테스트 / 검토 단위가 필요함

분리 대상:

- Card
- List
- Modal
- Form
- Button
- Input
- Section
- Header
- Filter
- Detail

---

### [실무]

분리 전:

```jsx
function FestivalPage({ festivals }) {
  return (
    <section>
      <h1>Festival</h1>
      {festivals.map((festival) => (
        <article key={festival.festivalId}>
          <h2>{festival.title}</h2>
          <p>{festival.region}</p>
        </article>
      ))}
    </section>
  );
}
```

분리 후:

```jsx
function FestivalPage({ festivals }) {
  return (
    <section>
      <h1>Festival</h1>
      <FestivalList festivals={festivals} />
    </section>
  );
}

function FestivalList({ festivals }) {
  return (
    <section>
      {festivals.map((festival) => (
        <FestivalCard key={festival.festivalId} festival={festival} />
      ))}
    </section>
  );
}

function FestivalCard({ festival }) {
  return (
    <article>
      <h2>{festival.title}</h2>
      <p>{festival.region}</p>
    </article>
  );
}
```

주의:

- 너무 작은 단위로 무조건 분리하지 않음
- 분리 기준은 역할, 재사용, 복잡도
- Props가 과도해지면 Component 책임 재검토
- Page Component는 데이터 흐름과 화면 조립 중심
- UI Component는 표시와 사용자 이벤트 중심

---

### [FAQ]

Q. Component는 언제 파일로 분리해?
A. 재사용되거나 JSX가 길어지거나 역할이 명확히 나뉠 때 분리한다.

Q. Component를 너무 많이 나누면 좋아?
A. 아니다. 역할이 불명확한 과도한 분리는 오히려 추적을 어렵게 만든다.

Q. Page Component와 UI Component는 왜 나눠?
A. Page는 화면 흐름과 데이터 조립을 담당하고 UI Component는 재사용 가능한 표시 단위를 담당하게 하기 위해서다.

---

## 3.3 Naming Convention

### [개념]

Naming Convention은 파일명, Component명, Props명, Event Handler명을 일관되게 작성하는 규칙이다.

이름 일관성은 RAG Retrieval, 코드 생성, 코드 리뷰 정확도를 높인다.

---

### [핵심]

Naming 핵심 규칙:

- Component 이름은 PascalCase
- Component 파일명은 PascalCase 권장
- 변수와 함수는 camelCase
- Props Callback은 `on` prefix
- Component 내부 Handler는 `handle` prefix
- boolean State는 is / has / can prefix 권장
- List Component는 List suffix 가능
- Card Component는 Card suffix 가능
- API 함수는 동사 + 대상 형태 권장

예:

| 대상          | 예                |
| ------------- | ----------------- |
| Component     | FestivalCard      |
| File          | FestivalCard.jsx  |
| Handler       | handleClick       |
| Callback Prop | onClick           |
| Boolean State | isOpen, hasError  |
| API Function  | getFestivals      |
| Type          | FestivalCardProps |

---

### [실무]

좋은 예:

```jsx
function FestivalSearchForm({ onSearch }) {
  const [keyword, setKeyword] = useState("");
  const [isSubmitting, setIsSubmitting] = useState(false);

  function handleSubmit(event) {
    event.preventDefault();
    onSearch(keyword);
  }

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={keyword}
        onChange={(event) => setKeyword(event.target.value)}
      />
      <button type="submit" disabled={isSubmitting}>
        Search
      </button>
    </form>
  );
}
```

주의:

- Component 이름 소문자 시작 금지
- Props 이름을 data, item으로만 남용하지 않음
- Handler와 Callback 이름 구분
- boolean 변수 이름은 조건 의미가 드러나게 작성
- 약어 남용 금지
- 프로젝트 컨벤션 우선

---

### [FAQ]

Q. Component 이름은 어떻게 지어?
A. PascalCase로 의미 있는 UI 역할을 드러내게 짓는다.

Q. Event Handler 이름은 어떻게 지어?
A. Component 내부 함수는 handleClick, handleSubmit처럼 handle prefix를 사용한다.

Q. Props Callback 이름은 어떻게 지어?
A. onClick, onSubmit, onSelect처럼 on prefix를 사용하는 방식이 흔하다.

---

# 4. Debugging

## 4.1 React Debugging Basics

### [개념]

React Debugging은 Component 렌더링, Props, State, Event, API 요청 흐름을 확인하는 과정이다.

React 문제는 Console, React DevTools, Network Tab, Component 구조를 순서대로 확인하면 원인을 찾기 쉽다.

---

### [핵심]

Debugging 핵심 키워드:

- React Debugging
- Browser Console
- React DevTools
- Network Tab
- Props Check
- State Check
- Component Tree
- Event Handler Check
- Rendering Condition Check
- API Response Check
- StrictMode caution

기본 Debug Flow:

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

---

### [실무]

확인 순서:

1. Console Error 확인
2. 컴파일 에러 확인
3. React DevTools에서 Component Tree 확인
4. Props 전달 확인
5. State 변경 확인
6. Event Handler 실행 확인
7. Network Tab에서 API 요청 확인
8. API 응답 body 확인
9. 조건부 렌더링 조건 확인
10. key warning 확인

주의:

- Console Error를 먼저 확인
- State가 setter로 변경되는지 확인
- Props가 실제로 전달되는지 확인
- Network 요청 URL과 응답 구조 확인
- loading / error / empty 조건 확인
- StrictMode에서 effect가 두 번처럼 보일 수 있음
- 렌더링 중 setState 여부 확인

---

### [FAQ]

Q. React State 값은 어디서 확인해?
A. React DevTools에서 Component를 선택해 State와 Props를 확인할 수 있다.

Q. React 화면이 안 바뀌면 뭘 확인해?
A. State가 setter로 변경되는지, Props가 전달되는지, 조건부 렌더링 조건이 맞는지 확인한다.

Q. API 데이터가 안 뜨면 뭘 확인해?
A. Network Tab에서 요청 URL, 응답 status, 응답 body, setState 여부, 렌더링 조건을 확인한다.

---

## 4.2 Common Error Debugging

### [개념]

Common Error Debugging은 React Core에서 자주 발생하는 오류를 원인별로 확인하는 과정이다.

React 오류는 JSX 문법, Props / State, Event Handler, List key, useEffect dependency, API 응답 구조에서 자주 발생한다.

---

### [핵심]

자주 발생하는 오류:

- Component 이름 소문자 작성
- JSX에서 class 사용
- JSX 내부 if statement 직접 작성
- 객체를 React child로 렌더링
- Props 직접 수정
- State 직접 변경
- onClick 즉시 실행
- key 누락
- index key 남용
- useEffect dependency 문제
- cleanup 누락
- input value만 있고 onChange 없음
- API response.ok 확인 누락
- null 데이터 property 접근

---

### [실무]

오류별 확인:

| 증상              | 확인 지점                               |
| ----------------- | --------------------------------------- |
| 화면이 안 바뀜    | State setter, Props 전달, 조건부 렌더링 |
| input 입력 안 됨  | value + onChange                        |
| 클릭 전 함수 실행 | onClick에 함수 호출 여부                |
| 목록 이상 갱신    | key, index key, State mutation          |
| API 반복 호출     | useEffect dependency                    |
| API 데이터 안 뜸  | Network, response body, setState        |
| null 오류         | 초기값, early return, optional chaining |
| 이벤트 중복 실행  | cleanup 누락, StrictMode                |

Debug 예:

```text
Input 입력 불가
→ value만 있는지 확인
→ onChange에서 setState 호출 확인
→ State 초기값 확인
→ disabled / readOnly 확인
```

```text
API 호출 반복
→ useEffect dependency 확인
→ Effect 내부 setState 확인
→ 객체 / 함수 dependency 확인
→ StrictMode 여부 확인
```

주의:

- 오류 메시지를 먼저 읽음
- 문제를 DOM에서 강제로 수정하지 않음
- React State / Props 흐름 기준으로 해결
- 에러를 숨기기보다 원인 제거
- eslint-disable 남용 금지

---

### [FAQ]

Q. input이 입력되지 않는 이유는?
A. value만 있고 onChange가 없거나 State가 제대로 업데이트되지 않을 수 있다.

Q. 클릭하지 않았는데 함수가 실행되는 이유는?
A. `onClick={handleClick()}`처럼 렌더링 중 함수를 호출했을 가능성이 높다.

Q. API가 계속 호출되는 이유는?
A. useEffect dependency가 매 렌더링마다 바뀌거나 Effect 내부 State 변경과 연결되어 있을 수 있다.

Q. 목록 UI가 이상하게 바뀌는 이유는?
A. key가 불안정하거나 배열 State를 직접 수정했을 가능성이 높다.

---

## 4.3 Review Agent Debug Checklist

### [개념]

Review Agent Debug Checklist는 React Core 코드 검토 시 반복적으로 확인해야 하는 항목이다.

Review Agent는 코드가 동작하는지만 보지 않고 React 데이터 흐름과 RAG 문서 규칙을 기준으로 검토해야 한다.

---

### [핵심]

Review Agent 확인 항목:

- Component 이름 PascalCase
- JSX className 사용
- Props 읽기 전용 유지
- State setter 사용
- 배열 / 객체 immutable update
- Event Handler 함수 참조 전달
- Controlled Input value + onChange
- Conditional Rendering 상태 분리
- List key 안정성
- useEffect 목적 적절성
- dependency array 적절성
- cleanup function 필요 여부
- API response.ok 확인
- loading / error / empty UI 존재
- TypeScript Props / State / Event Type 적절성
- 파일 역할 분리

---

### [실무]

Review Flow:

```text
React Code Review
→ Component Structure Check
→ Props / State Flow Check
→ Event Handler Check
→ Rendering Condition Check
→ List key Check
→ Hook / useEffect Check
→ API Call Check
→ TypeScript Type Check
→ File Structure Check
→ Common Mistake Check
```

치명적 문제:

- 렌더링 중 setState
- Component 본문 API 요청
- key 없는 list
- Math.random key
- State 직접 mutation
- Props 직접 수정
- useEffect 무한 loop
- cleanup 없는 timer / listener
- Controlled Input value만 제공
- null 데이터 무조건 접근

주의:

- 고급 최적화보다 Core 정확성 우선
- useMemo / useCallback 남용 지적보다 State 구조 확인 우선
- Data Fetching 심화는 별도 문서로 연결
- React Router / Global State 심화는 별도 문서로 연결

---

### [FAQ]

Q. Review Agent는 React 코드에서 뭘 먼저 봐야 해?
A. Component 구조, Props / State 흐름, Event Handler, List key, useEffect dependency를 먼저 확인한다.

Q. React Core 검토에서 치명적인 문제는 뭐야?
A. 렌더링 중 setState, State 직접 mutation, key 누락, useEffect loop, Component 본문 API 요청이 치명적이다.

Q. 성능 최적화부터 검토해야 해?
A. 아니다. React Core에서는 먼저 데이터 흐름, 렌더링 조건, State 구조가 올바른지 확인한다.

---

# 5. React Common Mistakes

## 5.1 JSX and Component Mistakes

### [개념]

JSX and Component Mistakes는 React 초기 코드에서 자주 발생하는 구조 오류다.

Component 이름, JSX 문법, Fragment, Element 렌더링 규칙을 확인해야 한다.

---

### [핵심]

자주 발생:

- Component 이름 소문자로 작성
- JSX에서 class 사용
- JSX에서 for 사용
- JSX 내부 if statement 직접 작성
- 하나의 부모 요소 없이 여러 JSX 반환
- 객체를 React child로 직접 렌더링
- 불필요한 div 남용
- Component와 Element 용어 혼동
- 모든 코드를 App.jsx에 작성

---

### [실무]

나쁜 예:

```jsx
function festivalCard({ festival }) {
  return <div class="card">{festival}</div>;
}
```

문제:

- Component 이름 소문자
- JSX에서 class 사용
- 객체를 직접 렌더링 가능성

개선:

```jsx
function FestivalCard({ festival }) {
  return (
    <article className="card">
      <h2>{festival.title}</h2>
    </article>
  );
}
```

주의:

- Component 이름은 PascalCase
- JSX에서는 className 사용
- 객체는 property를 렌더링
- 여러 JSX는 Fragment로 묶음
- 큰 Component는 역할별로 분리

---

### [FAQ]

Q. React 초보가 JSX에서 가장 많이 하는 실수는?
A. class 사용, if문 직접 작성, 객체 직접 렌더링, 부모 요소 없이 여러 요소 반환하는 실수가 많다.

Q. Component 이름을 소문자로 쓰면 왜 문제야?
A. React가 소문자로 시작하는 JSX를 HTML 태그로 인식하기 때문이다.

Q. 객체를 JSX에 바로 넣으면 왜 안 돼?
A. 객체 자체는 React child로 렌더링할 수 없으므로 문자열 property 등을 렌더링해야 한다.

---

## 5.2 Props State Event Mistakes

### [개념]

Props State Event Mistakes는 React 데이터 흐름과 사용자 이벤트 처리에서 자주 발생하는 오류다.

Props는 읽기 전용이고 State는 setter로 변경해야 하며 Event Handler는 함수 참조로 전달해야 한다.

---

### [핵심]

자주 발생:

- Props 직접 수정
- Props를 무조건 State로 복사
- State 직접 변경
- 배열 State에 push 사용
- 객체 State property 직접 수정
- setState 직후 값이 즉시 바뀐다고 오해
- onClick에 함수 실행 결과 전달
- form submit에서 preventDefault 누락
- button type 누락
- Controlled Input value만 있고 onChange 없음

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

Event Handler 즉시 실행 문제:

```jsx
<button onClick={onSelect(festivalId)}>Select</button>
```

개선:

```jsx
<button type="button" onClick={() => onSelect(festivalId)}>
  Select
</button>
```

Controlled Input 문제:

```jsx
<input value={keyword} />
```

개선:

```jsx
<input value={keyword} onChange={(event) => setKeyword(event.target.value)} />
```

주의:

- Props 직접 수정 금지
- State 직접 mutation 금지
- 이전 State 기반이면 functional update 사용
- Event Handler에는 함수 참조 전달
- Form 내부 일반 버튼은 `type="button"` 명시

---

### [FAQ]

Q. Props를 직접 바꾸면 왜 안 돼?
A. Props는 부모가 소유한 읽기 전용 데이터라 Child에서 직접 변경하면 React 데이터 흐름이 깨진다.

Q. State 직접 변경하면 어떤 문제가 생겨?
A. React가 변경을 감지하지 못해 화면이 업데이트되지 않거나 예측하기 어려운 버그가 생길 수 있다.

Q. 클릭하지 않았는데 함수가 실행되는 이유는?
A. `onClick={handler()}`처럼 렌더링 중 함수를 호출했기 때문이다.

---

## 5.3 Hook API Debug Mistakes

### [개념]

Hook API Debug Mistakes는 useEffect, dependency array, cleanup, API Call에서 자주 발생하는 오류다.

React Core에서 useEffect는 외부 시스템 동기화 도구이지 모든 로직을 넣는 장소가 아니다.

---

### [핵심]

자주 발생:

- Hook을 조건문 내부에서 호출
- Hook을 Event Handler 내부에서 호출
- Component 본문에서 API 요청
- useEffect dependency 누락
- useEffect dependency loop
- 객체 / 함수 dependency로 반복 실행
- cleanup 없는 Timer
- cleanup 없는 Event Listener
- response.ok 확인 누락
- AbortError를 일반 오류로 표시
- loading / error / empty 상태 누락

---

### [실무]

Component 본문 API 요청 문제:

```jsx
function BadPage() {
  const [festivals, setFestivals] = useState([]);

  fetch("/api/festivals")
    .then((response) => response.json())
    .then((data) => setFestivals(data));

  return <FestivalList festivals={festivals} />;
}
```

개선:

```jsx
function GoodPage() {
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

cleanup 누락 문제:

```jsx
useEffect(() => {
  window.addEventListener("resize", handleResize);
}, []);
```

개선:

```jsx
useEffect(() => {
  window.addEventListener("resize", handleResize);

  return () => {
    window.removeEventListener("resize", handleResize);
  };
}, []);
```

주의:

- Hook 규칙 위반은 치명적 문제
- useEffect loop는 dependency와 내부 setState 확인
- API 요청은 response.ok 확인
- cleanup 필요한 외부 작업은 return 함수 작성
- Data Fetching 심화는 별도 문서에서 다룸

---

### [FAQ]

Q. useEffect를 모든 로직 처리 장소로 쓰면 안 돼?
A. 안 된다. useEffect는 외부 시스템 동기화용이고 사용자 이벤트는 Event Handler에서 처리하는 것이 명확하다.

Q. API 호출이 반복되는 이유는?
A. useEffect dependency가 계속 바뀌거나 Effect 내부 State 변경과 dependency가 순환할 수 있다.

Q. cleanup이 없으면 어떤 문제가 생겨?
A. Timer나 Event Listener가 남아 중복 실행, memory leak, 오래된 값 참조 문제가 생길 수 있다.

---

# 6. Final Checklist

## 6.1 React Core Document Set Checklist

### [개념]

React Core Document Set Checklist는 React Core Part01부터 Part06까지 전체 문서가 Frontend Agent용 RAG 문서로 충분한지 검수하는 기준이다.

이 Checklist는 문서 제작 완료 전 최종 검수에 사용한다.

---

### [핵심]

전체 Part 구성:

```text
Part01 Overview / Component / JSX
Part02 Props / State / useState
Part03 Event Handling / Controlled Input / Conditional Rendering
Part04 List Rendering / key / Rendering Flow / Re-render
Part05 Hook Basics / useEffect / Dependency / Cleanup
Part06 API Call Basic / TypeScript / File Structure / Debugging / Final Checklist
```

최종 검수 항목:

```md
- [ ] React Overview가 포함되었는가?
- [ ] Component 개념과 Functional Component가 포함되었는가?
- [ ] JSX 규칙과 JSX Expression이 포함되었는가?
- [ ] Fragment가 포함되었는가?
- [ ] Props와 Props Destructuring이 포함되었는가?
- [ ] Callback Props와 children이 포함되었는가?
- [ ] State와 useState가 포함되었는가?
- [ ] Props vs State 비교가 포함되었는가?
- [ ] Array / Object State immutable update가 포함되었는가?
- [ ] Derived Value와 Source of Truth가 포함되었는가?
- [ ] Event Handling과 Event Object가 포함되었는가?
- [ ] Controlled Input과 Form Submit이 포함되었는가?
- [ ] Conditional Rendering이 포함되었는가?
- [ ] loading / error / empty / success UI가 포함되었는가?
- [ ] List Rendering과 key가 포함되었는가?
- [ ] index key 문제점이 포함되었는가?
- [ ] Rendering Flow와 Re-render가 포함되었는가?
- [ ] Rules of Hooks가 포함되었는가?
- [ ] useEffect 목적과 Side Effect 구분이 포함되었는가?
- [ ] Dependency Array와 Cleanup Function이 포함되었는가?
- [ ] API Call Basic Pattern이 포함되었는가?
- [ ] React TypeScript Props / State / Event Type이 포함되었는가?
- [ ] File Structure와 Naming Convention이 포함되었는가?
- [ ] Debugging Flow가 포함되었는가?
- [ ] Common Mistakes가 충분히 포함되었는가?
- [ ] 모든 Part에 FAQ가 포함되었는가?
- [ ] 모든 Part에 Retrieval Queries가 포함되었는가?
```

---

### [실무]

전체 검수 Flow:

```text
React Core Part01~06 Draft
→ MASTER_RAG_RULES Check
→ React_Core_Domain_Rules Check
→ Project Progress Scope Check
→ Part 간 중복 / 누락 확인
→ FAQ Coverage Check
→ Retrieval Queries Coverage Check
→ Common Mistakes Check
→ Final Quality Review
```

치명적 문제 기준:

- Part별 Retrieval Queries 누락
- [FAQ] 누락
- React Core 범위 초과 심화 내용 과다
- 잘못된 예제를 정상 예제로 제공
- State 직접 mutation 허용
- Props 직접 수정 허용
- key 없는 List 예제 제공
- Hook 규칙 위반 예제를 정상 예제로 제공
- useEffect를 모든 로직 처리 장소로 설명
- API 요청을 Component 본문에서 정상처럼 설명
- TypeScript any 남용 권장

---

### [FAQ]

Q. React Core 전체 문서의 최종 목적은 뭐야?
A. Frontend Agent가 React Component, Props, State, Event, Rendering, Hook, API 기본 화면을 안정적으로 생성하고 검토하게 만드는 것이다.

Q. React Core 문서에서 가장 중요한 품질 기준은?
A. Retrieval 가능한 Chunk 구조, FAQ, 실무 오류 방지, 핵심 코드 예제, 용어 통일이다.

Q. React Core 다음 문서는 뭐가 좋아?
A. React Component Design, React Router, State Management, Data Fetching REST API Integration 순서로 이어지는 것이 좋다.

---

## 6.2 Agent Output Checklist

### [개념]

Agent Output Checklist는 Frontend Agent가 React Core 기반 코드를 생성할 때 최종 출력 전에 검토해야 하는 기준이다.

Frontend Agent는 단순히 동작하는 코드가 아니라 React Core 규칙에 맞는 코드를 생성해야 한다.

---

### [핵심]

Frontend Agent 출력 기준:

- Functional Component 사용
- Component 이름 PascalCase
- JSX className 사용
- Props Type 또는 Props 구조 명확화
- State는 useState로 관리
- State 직접 mutation 금지
- Event Handler 함수 참조 전달
- Controlled Input은 value + onChange
- Conditional Rendering 명확화
- List Rendering은 stable key 사용
- useEffect는 외부 시스템 동기화용
- dependency array 검토
- cleanup 필요한 Effect는 cleanup 작성
- API Call은 loading / error / empty 처리
- TypeScript 사용 시 Props / State / Event Type 작성
- 파일 역할 분리 고려

---

### [실무]

Agent Self Review Flow:

```text
Generate React Code
→ Component Name Check
→ JSX Rule Check
→ Props / State Check
→ Event Handler Check
→ Rendering Condition Check
→ List key Check
→ Hook Rule Check
→ API State Check
→ TypeScript Type Check
→ Common Mistake Check
→ Final Output
```

출력 전 금지 확인:

```md
- [ ] Component 이름이 소문자인가?
- [ ] JSX에서 class를 사용했는가?
- [ ] Props를 직접 수정했는가?
- [ ] State를 직접 수정했는가?
- [ ] 배열 State에 push를 사용했는가?
- [ ] onClick에 함수 실행 결과를 전달했는가?
- [ ] key 없는 map 렌더링이 있는가?
- [ ] Math.random key를 사용했는가?
- [ ] Hook을 조건문 내부에서 호출했는가?
- [ ] Component 본문에서 API 요청했는가?
- [ ] cleanup 없는 timer/listener가 있는가?
- [ ] loading/error/empty 처리가 누락되었는가?
```

---

### [FAQ]

Q. Frontend Agent가 React 코드를 만들 때 가장 먼저 지켜야 할 것은?
A. Functional Component, JSX 규칙, Props / State 흐름, Event Handler, List key, Hook 규칙을 지켜야 한다.

Q. Agent가 React 코드 출력 전 반드시 확인할 것은?
A. State mutation, key 누락, Hook 규칙 위반, useEffect loop, API 상태 처리 누락 여부를 확인해야 한다.

Q. React Core 출력에서 고급 최적화를 먼저 해야 해?
A. 아니다. React Core에서는 정확한 데이터 흐름과 안정적인 렌더링 구조가 우선이다.

---

# Retrieval Queries

### [FAQ]

Q. React에서 API 호출은 어디서 해?
A. 초기 데이터 로딩은 보통 useEffect에서 처리하고 사용자 이벤트 요청은 Event Handler에서 처리한다.

Q. API 호출 상태는 어떤 State로 나눠?
A. data, loading, error, empty 상태를 분리하는 것이 좋다.

Q. fetch 실패 처리는 어떻게 해?
A. response.ok를 확인하고 실패 시 error state를 설정해 사용자에게 안내한다.

Q. Component 본문에서 fetch를 바로 실행하면 안 돼?
A. 렌더링마다 요청이 실행될 수 있어 useEffect 또는 Event Handler에서 처리해야 한다.

Q. loading과 empty 차이는 뭐야?
A. loading은 요청 진행 중이고 empty는 요청 성공 후 표시할 데이터가 없는 상태다.

Q. error와 empty 차이는 뭐야?
A. error는 요청 실패 상태이고 empty는 요청 성공 후 데이터가 없는 정상 상태다.

Q. API 데이터가 null일 때 어떻게 렌더링해?
A. null 체크 후 fallback UI를 먼저 반환하고 데이터가 있을 때 상세 UI를 렌더링한다.

Q. API 호출 함수는 Component 안에 둬도 돼?
A. 간단한 예제는 가능하지만 재사용되거나 복잡하면 api 파일로 분리하는 것이 좋다.

Q. api 파일에는 무엇을 넣어?
A. 서버 요청 함수, URL 처리, response.ok 확인, response json 변환 같은 요청 관련 로직을 넣는다.

Q. loading State는 api 함수에 넣어?
A. 보통 loading, error, data State는 Component에서 관리하고 api 함수는 요청과 응답 처리에 집중한다.

Q. React Props Type은 어떻게 정의해?
A. type 또는 interface로 Props 구조를 정의하고 Component parameter에 적용한다.

Q. optional prop은 어떻게 써?
A. `label?: string`처럼 property 이름 뒤에 `?`를 붙인다.

Q. nullable prop은 어떻게 써?
A. `imageUrl: string | null`처럼 union type을 사용한다.

Q. children Type은 뭐로 써?
A. 일반적으로 ReactNode를 사용할 수 있다.

Q. useState 빈 배열 타입은 어떻게 써?
A. TypeScript에서는 `useState<Festival[]>([])`처럼 Generic으로 요소 타입을 명시한다.

Q. null 초기값 State는 어떻게 타입 지정해?
A. `useState<Festival | null>(null)`처럼 union type을 사용한다.

Q. useState에 any를 써도 돼?
A. 가능은 하지만 타입 안정성이 떨어지므로 구체적인 타입을 정의하는 것이 좋다.

Q. input onChange 타입은 뭐야?
A. TypeScript React에서는 일반적으로 `ChangeEvent<HTMLInputElement>`를 사용한다.

Q. form onSubmit 타입은 뭐야?
A. `FormEvent<HTMLFormElement>`를 사용한다.

Q. button onClick 타입은 뭐야?
A. `MouseEvent<HTMLButtonElement>`를 사용할 수 있다.

Q. Event Type은 꼭 써야 해?
A. 분리된 Handler 함수에서는 명시하는 것이 타입 안정성과 가독성에 좋다.

Q. React.FC를 꼭 써야 해?
A. 필수는 아니다. 프로젝트 컨벤션에 따라 사용 여부를 결정한다.

Q. optional과 nullable 차이는?
A. optional은 property 자체가 없을 수 있고 nullable은 property는 있지만 값이 null일 수 있다.

Q. API 응답 타입은 어디에 둬?
A. 작으면 Component 근처에 두고 여러 곳에서 쓰면 types 폴더나 api 타입 파일로 분리한다.

Q. Component 파일은 어디에 둬?
A. 재사용 Component는 components 폴더, 화면 단위 Component는 pages 폴더에 두는 방식이 일반적이다.

Q. API 호출 함수는 어디에 둬?
A. 재사용되거나 복잡한 API 요청 함수는 api 폴더에 둔다.

Q. 모든 코드를 App.jsx에 넣어도 돼?
A. 작은 실습은 가능하지만 실무 프로젝트에서는 역할별 파일 분리가 필요하다.

Q. Component는 언제 파일로 분리해?
A. 재사용되거나 JSX가 길어지거나 역할이 명확히 나뉠 때 분리한다.

Q. Component를 너무 많이 나누면 좋아?
A. 아니다. 역할이 불명확한 과도한 분리는 오히려 추적을 어렵게 만든다.

Q. Page Component와 UI Component는 왜 나눠?
A. Page는 화면 흐름과 데이터 조립을 담당하고 UI Component는 재사용 가능한 표시 단위를 담당하게 하기 위해서다.

Q. Component 이름은 어떻게 지어?
A. PascalCase로 의미 있는 UI 역할을 드러내게 짓는다.

Q. Event Handler 이름은 어떻게 지어?
A. Component 내부 함수는 handleClick, handleSubmit처럼 handle prefix를 사용한다.

Q. Props Callback 이름은 어떻게 지어?
A. onClick, onSubmit, onSelect처럼 on prefix를 사용하는 방식이 흔하다.

Q. React State 값은 어디서 확인해?
A. React DevTools에서 Component를 선택해 State와 Props를 확인할 수 있다.

Q. React 화면이 안 바뀌면 뭘 확인해?
A. State가 setter로 변경되는지, Props가 전달되는지, 조건부 렌더링 조건이 맞는지 확인한다.

Q. API 데이터가 안 뜨면 뭘 확인해?
A. Network Tab에서 요청 URL, 응답 status, 응답 body, setState 여부, 렌더링 조건을 확인한다.

Q. input이 입력되지 않는 이유는?
A. value만 있고 onChange가 없거나 State가 제대로 업데이트되지 않을 수 있다.

Q. 클릭하지 않았는데 함수가 실행되는 이유는?
A. `onClick={handleClick()}`처럼 렌더링 중 함수를 호출했을 가능성이 높다.

Q. API가 계속 호출되는 이유는?
A. useEffect dependency가 매 렌더링마다 바뀌거나 Effect 내부 State 변경과 연결되어 있을 수 있다.

Q. 목록 UI가 이상하게 바뀌는 이유는?
A. key가 불안정하거나 배열 State를 직접 수정했을 가능성이 높다.

Q. Review Agent는 React 코드에서 뭘 먼저 봐야 해?
A. Component 구조, Props / State 흐름, Event Handler, List key, useEffect dependency를 먼저 확인한다.

Q. React Core 검토에서 치명적인 문제는 뭐야?
A. 렌더링 중 setState, State 직접 mutation, key 누락, useEffect loop, Component 본문 API 요청이 치명적이다.

Q. 성능 최적화부터 검토해야 해?
A. 아니다. React Core에서는 먼저 데이터 흐름, 렌더링 조건, State 구조가 올바른지 확인한다.

Q. React 초보가 JSX에서 가장 많이 하는 실수는?
A. class 사용, if문 직접 작성, 객체 직접 렌더링, 부모 요소 없이 여러 요소 반환하는 실수가 많다.

Q. Component 이름을 소문자로 쓰면 왜 문제야?
A. React가 소문자로 시작하는 JSX를 HTML 태그로 인식하기 때문이다.

Q. 객체를 JSX에 바로 넣으면 왜 안 돼?
A. 객체 자체는 React child로 렌더링할 수 없으므로 문자열 property 등을 렌더링해야 한다.

Q. Props를 직접 바꾸면 왜 안 돼?
A. Props는 부모가 소유한 읽기 전용 데이터라 Child에서 직접 변경하면 React 데이터 흐름이 깨진다.

Q. State 직접 변경하면 어떤 문제가 생겨?
A. React가 변경을 감지하지 못해 화면이 업데이트되지 않거나 예측하기 어려운 버그가 생길 수 있다.

Q. useEffect를 모든 로직 처리 장소로 쓰면 안 돼?
A. 안 된다. useEffect는 외부 시스템 동기화용이고 사용자 이벤트는 Event Handler에서 처리하는 것이 명확하다.

Q. cleanup이 없으면 어떤 문제가 생겨?
A. Timer나 Event Listener가 남아 중복 실행, memory leak, 오래된 값 참조 문제가 생길 수 있다.

Q. React Core 전체 문서의 최종 목적은 뭐야?
A. Frontend Agent가 React Component, Props, State, Event, Rendering, Hook, API 기본 화면을 안정적으로 생성하고 검토하게 만드는 것이다.

Q. React Core 문서에서 가장 중요한 품질 기준은?
A. Retrieval 가능한 Chunk 구조, FAQ, 실무 오류 방지, 핵심 코드 예제, 용어 통일이다.

Q. React Core 다음 문서는 뭐가 좋아?
A. React Component Design, React Router, State Management, Data Fetching REST API Integration 순서로 이어지는 것이 좋다.

Q. Frontend Agent가 React 코드를 만들 때 가장 먼저 지켜야 할 것은?
A. Functional Component, JSX 규칙, Props / State 흐름, Event Handler, List key, Hook 규칙을 지켜야 한다.

Q. Agent가 React 코드 출력 전 반드시 확인할 것은?
A. State mutation, key 누락, Hook 규칙 위반, useEffect loop, API 상태 처리 누락 여부를 확인해야 한다.

Q. React Core 출력에서 고급 최적화를 먼저 해야 해?
A. 아니다. React Core에서는 정확한 데이터 흐름과 안정적인 렌더링 구조가 우선이다.
