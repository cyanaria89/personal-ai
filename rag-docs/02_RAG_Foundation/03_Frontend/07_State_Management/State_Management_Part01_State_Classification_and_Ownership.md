# State_Management_Part01_State_Classification_and_Ownership.md

# State Management Part01 - State Classification and Ownership

---

# 1. State Management Overview

## 1.1 State Management Purpose

### [개념]

State Management는 React Frontend에서 State를 어디에 두고 어떤 방식으로 관리할지 결정하는 설계 기준이다.

State Management는 단순히 Redux, Zustand 같은 전역 상태 라이브러리 사용법이 아니다.

핵심 목적은 State의 종류, 소유자, 사용 범위, 갱신 방식, 저장 위치를 판단하는 것이다.

---

### [핵심]

State Management 핵심 목적:

- State Classification
- State Ownership
- Local State 판단
- Shared State 판단
- Global State 판단
- Client State와 Server State 구분
- UI State / Form State / Auth State / URL State 구분
- Derived State 중복 저장 방지
- Props Drilling 문제 판단
- 상태관리 도구 선택 기준 제공

---

### [실무]

2026 실무 기준에서 State Management는 아래 순서로 판단한다.

```text
State 발견
→ State Type 분류
→ State Owner 결정
→ State Scope 결정
→ Local / Shared / Global 판단
→ Server State 여부 판단
→ URL State 여부 판단
→ Tool Selection
→ Anti Pattern 검토
```

State Management의 기본 원칙:

- State는 가능한 필요한 곳 가까이에 둔다.
- 여러 Component가 공유해야 할 때만 위로 올린다.
- 여러 페이지에서 반복적으로 필요할 때만 Global State를 검토한다.
- API 데이터는 대부분 Server State로 본다.
- 계산 가능한 값은 Derived State로 보고 별도 저장하지 않는다.
- 전역 Store는 기본 선택지가 아니라 필요한 경우에만 선택한다.

---

### [FAQ]

Q. State Management는 왜 필요해?
A. React 상태를 어디에 두고 어떤 도구로 관리할지 판단해야 유지보수 가능한 Frontend 구조를 만들 수 있기 때문이다.

Q. State Management는 Redux 사용법이야?
A. 아니다. Redux, Zustand, Context, TanStack Query 중 무엇을 선택할지 결정하기 전 State 종류와 소유자를 분류하는 설계 기준이다.

Q. State Management에서 가장 먼저 해야 할 일은 뭐야?
A. State Classification이다. 상태 종류를 먼저 분류해야 적절한 관리 위치와 도구를 선택할 수 있다.

---

# 2. State Classification

## 2.1 State Classification Definition

### [개념]

State Classification은 상태를 성격과 소유 범위에 따라 분류하는 작업이다.

모든 State를 같은 방식으로 관리하면 안 된다.

같은 값처럼 보여도 원본 소유자, 사용 범위, 저장 필요성, 공유 필요성에 따라 관리 방식이 달라진다.

---

### [핵심]

필수 State Classification:

- Local State
- Shared State
- Global State
- Client State
- Server State
- UI State
- Form State
- Auth State
- URL State
- Cache State
- Derived State

---

### [실무]

State Classification Flow:

```text
State 발견
→ 이 값은 서버 데이터인가?
→ 이 값은 URL에 남아야 하는가?
→ 이 값은 여러 Component가 공유하는가?
→ 이 값은 여러 페이지에서 필요한가?
→ 이 값은 Form 입력 상태인가?
→ 이 값은 UI 표시 상태인가?
→ 이 값은 인증 상태인가?
→ 이 값은 기존 값으로 계산 가능한가?
→ 관리 위치와 도구 결정
```

기본 판단 기준:

```text
Component 내부만 사용 → Local State
형제 Component 공유 → Shared State
여러 페이지에서 반복 사용 → Global State
API 응답 데이터 → Server State
검색 조건 / 페이지 번호 → URL State
입력값 / 검증값 → Form State
modal / dropdown / tab → UI State
로그인 여부 / 사용자 요약 → Auth State
기존 값으로 계산 가능 → Derived State
```

---

### [FAQ]

Q. State Classification이 뭐야?
A. State를 Local, Shared, Global, Server, Form, Auth, URL State처럼 성격과 범위에 따라 분류하는 작업이다.

Q. State Classification은 왜 먼저 해?
A. 상태 종류를 구분해야 useState, useReducer, Context, Zustand, Redux Toolkit, TanStack Query 중 적절한 도구를 선택할 수 있기 때문이다.

Q. 모든 State를 Zustand나 Redux에 넣으면 안 돼?
A. 권장하지 않는다. Local State나 Form State까지 전역화하면 데이터 흐름이 복잡해지고 유지보수 비용이 증가한다.

---

## 2.2 State Type Quick Decision

### [개념]

State Type Quick Decision은 발견된 State를 빠르게 분류하기 위한 판단표다.

Frontend Agent는 상태명을 보고 바로 도구를 선택하지 말고 먼저 State Type을 판단해야 한다.

---

### [핵심]

State Type 판단 키워드:

- input value
- modal open
- selected tab
- search keyword
- filter
- page number
- user profile
- authenticated
- access token
- festival list
- review list
- notification count
- total price
- filtered items
- cache data

---

### [실무]

State Type Decision Table:

| 상태 예시                 | State Type                       | 기본 위치                    |
| ------------------------- | -------------------------------- | ---------------------------- |
| input 임시값              | Form State / Local State         | Form Component               |
| modal open                | UI State / Local State           | Modal 사용 Component         |
| selected tab              | UI State                         | 해당 Page 또는 Component     |
| 검색 keyword              | URL State 또는 Shared State      | URL Query 또는 Page          |
| filter 조건               | URL State 또는 Shared State      | URL Query 또는 Page          |
| page number               | URL State                        | URL Query                    |
| user profile              | Server State / Auth State        | Query Cache 또는 Auth Store  |
| authenticated             | Auth State / Global State        | Auth Context 또는 Auth Store |
| festival list             | Server State                     | TanStack Query               |
| review list               | Server State                     | TanStack Query               |
| notification unread count | Global State 또는 Server State   | Store 또는 Query             |
| total price               | Derived State                    | 계산값                       |
| filtered items            | Derived State                    | 계산값                       |
| theme                     | Global State / Persistence State | UI Store 또는 Context        |

---

### [FAQ]

Q. 상태명을 보면 바로 도구를 정해도 돼?
A. 아니다. 먼저 State Type, 사용 범위, 원본 소유자, 공유 필요성을 판단해야 한다.

Q. API 응답 목록은 Global State야?
A. 대부분 Server State다. 캐시, refetch, stale data 관리가 필요하면 TanStack Query 같은 Server State 도구가 적합하다.

Q. 검색 조건은 Local State야?
A. 단순 입력 중 임시값은 Local State지만, 결과 공유와 새로고침 복원이 필요하면 URL State가 적합하다.

---

# 3. Client State and Server State

## 3.1 Client State

### [개념]

Client State는 Frontend가 원본을 소유하고 UI 상호작용을 위해 관리하는 상태다.

Client State는 브라우저 화면, 사용자 입력, UI 표시, 앱 설정과 관련된다.

---

### [핵심]

Client State 예:

- modal open
- dropdown open
- selected tab
- input value
- local filter toggle
- sidebar open
- theme
- language
- form validation message
- selected item
- UI visibility

---

### [실무]

Client State 관리 도구:

```text
단일 Component 내부 → useState
상태 전환 복잡 → useReducer
하위 Tree 공유 → Context API
여러 페이지 공유 → Zustand / Redux Toolkit
공유 가능한 검색 조건 → URL Search Params
새로고침 후 유지 설정 → localStorage / sessionStorage
```

Client State 설계 기준:

- 가능한 가까운 Component에 둔다.
- 외부 공유가 필요해질 때만 위로 올린다.
- 여러 페이지에서 필요할 때만 Global State를 검토한다.
- UI State와 Server State를 섞지 않는다.
- Client State에 API 응답 원본을 무분별하게 저장하지 않는다.

---

### [FAQ]

Q. Client State가 뭐야?
A. Frontend가 원본을 소유하고 화면 표시나 사용자 상호작용을 위해 관리하는 상태다.

Q. modal open은 Client State야?
A. 맞다. modal open 여부는 Frontend UI 표시 상태이므로 Client State다.

Q. Client State는 무조건 전역 Store에 둬야 해?
A. 아니다. 대부분은 useState나 useReducer로 충분하고, 여러 페이지에서 필요한 경우에만 전역 Store를 검토한다.

---

## 3.2 Server State

### [개념]

Server State는 서버가 원본을 소유하고 Frontend가 조회, 표시, 캐싱, 갱신하는 데이터다.

Server State는 일반 Client State와 달리 캐시, stale data, refetch, mutation, invalidation 문제가 있다.

---

### [핵심]

Server State 예:

- user profile
- festival list
- festival detail
- review list
- notification list
- favorite list
- donation history
- chat room list
- server pagination result
- API cache data

Server State 키워드:

- API Data
- Cache
- Stale Data
- Refetch
- Mutation
- Invalidation
- Pagination
- Background Update
- Loading State
- Error State

---

### [실무]

Server State 관리 Flow:

```text
API 응답 데이터 발견
→ 서버가 원본인지 확인
→ 캐시 필요 여부 확인
→ refetch 필요 여부 확인
→ mutation 여부 확인
→ pagination 여부 확인
→ TanStack Query 검토
→ Client State와 분리
```

Server State 관리 기준:

- 서버 데이터는 전역 Client Store에 무분별하게 복사하지 않는다.
- API mutation 후 invalidateQueries 또는 refetch를 고려한다.
- loading / error / empty 상태를 함께 설계한다.
- stale data 정책을 고려한다.
- 화면용 selected id는 Client State, 상세 데이터는 Server State로 분리할 수 있다.

---

### [FAQ]

Q. Server State가 뭐야?
A. 서버가 원본으로 소유하고 Frontend가 조회, 캐싱, 갱신하는 데이터다.

Q. API 응답 데이터는 Client State야 Server State야?
A. 대부분 Server State다. 서버가 원본 소유자이고 Frontend는 캐시하거나 화면에 표시한다.

Q. Server State를 Zustand에 넣으면 안 돼?
A. 가능은 하지만 캐시, stale data, refetch, mutation 관리가 복잡하면 TanStack Query 같은 Server State 도구가 더 적합하다.

---

## 3.3 Client State vs Server State

### [개념]

Client State와 Server State는 원본 소유자와 갱신 방식이 다르다.

State Management에서 가장 중요한 구분 중 하나다.

---

### [핵심]

비교 기준:

- 원본 소유자
- 갱신 주체
- 캐시 필요성
- 새로고침 처리
- 동기화 방식
- 적합한 도구
- 주요 오류 유형

---

### [실무]

Client State vs Server State:

| 비교        | Client State                  | Server State                |
| ----------- | ----------------------------- | --------------------------- |
| 원본 소유자 | Frontend                      | Backend / Server            |
| 예시        | modal open, selected tab      | festival list, user profile |
| 관리 도구   | useState, useReducer, Zustand | TanStack Query, API Hook    |
| 주요 문제   | State 위치, Props Drilling    | Cache, stale data, refetch  |
| 새로고침    | 사라질 수 있음                | 서버에서 다시 조회          |
| 갱신 방식   | setState / store action       | mutation / invalidation     |
| 저장 주의   | localStorage 민감정보 주의    | query cache 기준 필요       |

권장 판단:

```text
서버 DB 또는 API가 원본이다 → Server State
브라우저 UI가 원본이다 → Client State
서버 데이터의 선택 ID만 관리한다 → Client State
선택 ID로 조회한 상세 데이터 → Server State
```

---

### [FAQ]

Q. Client State와 Server State를 왜 나눠?
A. 소유자와 갱신 방식이 다르기 때문이다. Server State는 서버 동기화와 캐시 전략이 중요하다.

Q. user profile은 Auth State야 Server State야?
A. 서버에서 조회하는 원본 데이터는 Server State이고, 로그인 여부와 사용자 요약은 Auth State로 관리할 수 있다.

Q. 목록에서 선택된 item id는 Server State야?
A. 보통 selected item id는 Client State이고, 해당 id로 조회한 상세 데이터는 Server State다.

---

# 4. Local State

## 4.1 Local State Definition

### [개념]

Local State는 특정 Component 내부에서만 필요한 상태다.

Local State는 가장 좁은 범위에서 관리하는 상태이며, Component가 사라지면 함께 사라져도 되는 값에 적합하다.

---

### [핵심]

Local State 예:

- input 임시값
- dropdown open
- modal open
- hover-like UI state
- selected tab inside component
- local validation message
- accordion open
- local checkbox checked
- temporary preview state

---

### [실무]

Local State 예:

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

Local State 권장 기준:

- 해당 Component 내부에서만 사용한다.
- 다른 Component와 공유하지 않는다.
- URL에 남길 필요가 없다.
- 새로고침 후 유지할 필요가 없다.
- Component 제거 시 함께 초기화되어도 된다.

주의:

- Local State를 불필요하게 App까지 올리지 않는다.
- Local State를 Global Store에 넣지 않는다.
- Local State가 여러 형제 Component에 필요해지면 Shared State로 전환한다.

---

### [FAQ]

Q. Local State는 언제 써?
A. 특정 Component 내부에서만 필요하고 다른 Component와 공유하지 않는 상태에 사용한다.

Q. input 값은 무조건 전역 상태로 둬야 해?
A. 아니다. 해당 Form 내부에서만 필요한 입력값은 Local State가 적합하다.

Q. modal open 상태는 Local State로 둬도 돼?
A. 해당 화면이나 Component 안에서만 열고 닫는 modal이면 Local State가 적합하다.

---

## 4.2 Local State Decision Criteria

### [개념]

Local State Decision Criteria는 State를 Component 내부에 둘 수 있는지 판단하는 기준이다.

기본 원칙은 가능한 Local State로 유지하고, 공유 필요가 생길 때만 범위를 넓히는 것이다.

---

### [핵심]

Local State 적합 조건:

- 단일 Component에서만 읽음
- 단일 Component에서만 변경
- 다른 Component가 몰라도 됨
- URL 공유 필요 없음
- 새로고침 복원 필요 없음
- 서버 원본 아님
- 계산 가능한 Derived State 아님

---

### [실무]

Local State 판단 Flow:

```text
State 발견
→ 이 Component 안에서만 쓰는가?
→ 다른 Component가 읽지 않는가?
→ 다른 Component가 변경하지 않는가?
→ URL에 남길 필요가 없는가?
→ 여러 페이지에서 필요하지 않은가?
→ Local State 유지
```

Local State에서 벗어나는 신호:

- 형제 Component가 같은 값을 필요로 한다.
- 부모 Component가 변경 결과를 알아야 한다.
- 여러 페이지에서 같은 상태가 필요하다.
- 새로고침 후 유지해야 한다.
- 공유 URL로 복원해야 한다.
- Props 전달이 깊고 반복된다.

---

### [FAQ]

Q. State를 Local로 둘지 어떻게 판단해?
A. 해당 Component만 읽고 변경하며 외부 공유나 복원이 필요 없으면 Local State로 둔다.

Q. Local State를 나중에 Shared State로 바꿔도 돼?
A. 가능하다. 처음부터 너무 높게 올리지 말고 공유 필요가 생긴 시점에 올리는 것이 좋다.

Q. Local State가 많으면 무조건 문제야?
A. 아니다. 각 Component 내부에서만 필요한 상태라면 Local State가 많은 것은 자연스럽다.

---

# 5. Shared State

## 5.1 Shared State Definition

### [개념]

Shared State는 여러 Component가 함께 읽거나 변경해야 하는 상태다.

Shared State는 전역 상태가 아니라, 공유하는 Component들의 가장 가까운 공통 부모에서 관리하는 상태일 수 있다.

---

### [핵심]

Shared State 예:

- 검색 조건
- 선택된 item
- 현재 tab
- 부모와 자식이 공유하는 form 결과
- 형제 Component가 함께 쓰는 filter
- 특정 Page 내부 공통 상태
- Preview에 반영되는 Form 입력 결과

---

### [실무]

Shared State 예:

```jsx
function FestivalPage() {
  const [selectedFestivalId, setSelectedFestivalId] = useState(null);

  return (
    <>
      <FestivalList
        selectedFestivalId={selectedFestivalId}
        onSelect={setSelectedFestivalId}
      />
      <FestivalPreview festivalId={selectedFestivalId} />
    </>
  );
}
```

Shared State 관리 기준:

- 가장 가까운 공통 부모에 둔다.
- Page 내부에서만 공유되면 Page Component State로 충분하다.
- 여러 페이지에서 공유될 때만 Global State를 검토한다.
- URL State가 더 적합한지 확인한다.
- Server State와 혼동하지 않는다.

---

### [FAQ]

Q. Shared State는 전역 상태야?
A. 항상 전역 상태는 아니다. 특정 Page 내부에서만 공유되면 공통 부모 State로 충분할 수 있다.

Q. 형제 Component가 같은 값을 써야 하면 어떻게 해?
A. 가장 가까운 공통 부모로 State를 올리고 Props와 callback으로 전달한다.

Q. Shared State는 Context로 관리해야 해?
A. 필수는 아니다. 공유 범위가 좁으면 부모 State와 Props 전달이 더 단순하다.

---

## 5.2 Shared State Decision Criteria

### [개념]

Shared State Decision Criteria는 Local State를 공통 부모로 올려야 하는지 판단하는 기준이다.

State를 공유하는 Component들이 생기면 Lifting State Up을 검토한다.

---

### [핵심]

Shared State 적합 조건:

- 두 개 이상의 Component가 같은 값을 읽음
- 한 Component의 변경 결과가 다른 Component에 필요함
- 형제 Component 간 상태 공유 필요
- Form 입력이 Preview에 필요
- 선택한 item이 상세 영역에 필요
- Page 내부 공통 filter 필요

---

### [실무]

Shared State 판단 Flow:

```text
Local State 발견
→ 다른 Component도 읽는가?
→ 다른 Component 변경 결과가 필요한가?
→ 공통 부모가 존재하는가?
→ 가장 가까운 공통 부모로 이동
→ Props와 callback으로 전달
```

주의:

- Shared State라고 바로 Global Store로 보내지 않는다.
- 공통 부모가 너무 멀면 Component 구조를 먼저 검토한다.
- 1~2단계 Props 전달은 정상이다.
- Props Drilling이 심해질 때 Context나 Store를 검토한다.
- 검색 조건은 URL State가 더 적합할 수 있다.

---

### [FAQ]

Q. Shared State와 Global State 차이는?
A. Shared State는 특정 Component 집합에서 공유되는 상태이고, Global State는 여러 페이지나 앱 전체에서 공유되는 상태다.

Q. Page 내부 filter는 Global State로 둬야 해?
A. 보통 아니다. 해당 Page 내부에서만 필요하면 Page Component의 Shared State로 충분하다.

Q. Shared State가 많아지면 어떻게 해?
A. State Owner를 재검토하고, Props Drilling이 심하면 Context, Zustand, URL State 등을 검토한다.

---

# 6. Global State

## 6.1 Global State Definition

### [개념]

Global State는 여러 페이지 또는 앱 전체에서 반복적으로 공유해야 하는 상태다.

Global State는 편의 기능이 아니라 공유 범위가 넓은 Client State를 관리하기 위한 선택지다.

---

### [핵심]

Global State 적합 예:

- authenticated
- auth user summary
- theme
- language
- global toast
- global modal
- app layout state
- sidebar state
- cart
- user preference
- notification unread count

Global State 부적합 예:

- 단일 input value
- 단일 modal open
- 특정 Page의 임시 filter
- 특정 Component 내부 selected tab
- Derived State
- 단순 API list data 전체
- Form 입력값 전체

---

### [실무]

Global State 판단 Flow:

```text
State 발견
→ 여러 페이지에서 필요한가?
→ 깊은 Component Tree에서 반복 전달되는가?
→ URL State로 표현 가능한가?
→ Server State 도구가 더 적합한가?
→ Context 또는 Global Store 검토
```

Global State 관리 도구:

```text
단순 값 공급 / 낮은 변경 빈도 → Context API
가벼운 전역 Store → Zustand
복잡한 전역 상태 / DevTools / 팀 컨벤션 → Redux Toolkit
서버 데이터 캐시 → TanStack Query
```

주의:

- 전역 상태는 관리 비용이 있다.
- 상태 변경 영향 범위가 커질 수 있다.
- Store 구조 설계가 필요하다.
- logout 시 reset 기준이 필요하다.
- Server State와 혼합하지 않는다.
- 민감정보 persist를 피한다.

---

### [FAQ]

Q. Global State는 언제 써?
A. 여러 페이지나 깊은 Component Tree에서 반복적으로 필요한 상태일 때 사용한다.

Q. 모든 페이지에서 쓰지 않는 값도 Global State로 둬도 돼?
A. 가능은 하지만 권장하지 않는다. 필요한 범위가 좁으면 Local State나 Shared State가 더 적합하다.

Q. API 목록 데이터를 Global State에 저장해도 돼?
A. 무조건 권장하지 않는다. 서버 데이터는 TanStack Query 같은 Server State 도구가 더 적합할 수 있다.

---

## 6.2 Global State Decision Criteria

### [개념]

Global State Decision Criteria는 State를 전역 Store나 Context로 올려야 하는지 판단하는 기준이다.

전역 상태 도입 전에는 반드시 Local State, Shared State, URL State, Server State 가능성을 먼저 검토한다.

---

### [핵심]

Global State 검토 조건:

- 여러 Page에서 필요
- App Layout 전체에서 필요
- 인증 상태처럼 전역 접근 필요
- 여러 Feature에서 같은 값 변경
- Props Drilling이 깊고 반복됨
- Context만으로 action 관리가 복잡함
- 전역 UI 기능 필요
- 새로고침 후 일부 설정 유지 필요

---

### [실무]

Global State 도입 전 Checklist:

```md
- [ ] Local State로 충분하지 않은가?
- [ ] Shared State로 충분하지 않은가?
- [ ] URL State가 더 적합하지 않은가?
- [ ] Server State가 아닌가?
- [ ] Derived State가 아닌가?
- [ ] 여러 페이지에서 반복 사용되는가?
- [ ] logout/reset 기준이 있는가?
- [ ] persist가 필요한 값인가?
- [ ] 민감정보 저장 위험이 없는가?
```

Global State 설계 기준:

```text
authStore
- user
- authenticated
- login
- logout
- clearAuth

uiStore
- theme
- sidebarOpen
- toast

notificationStore
- unreadCount
- setUnreadCount
- resetNotification
```

---

### [FAQ]

Q. 전역 Store는 어떻게 나누는 게 좋아?
A. auth, ui, notification처럼 도메인 또는 책임 기준으로 나누는 것이 좋다.

Q. 전역 Store 하나에 모든 상태를 넣어도 돼?
A. 권장하지 않는다. Store가 거대해지면 데이터 흐름 추적과 유지보수가 어려워진다.

Q. Global State 도입 전에 무엇을 확인해야 해?
A. Local, Shared, URL, Server State로 충분한지 먼저 확인해야 한다.

---

# 7. State Ownership

## 7.1 State Ownership Definition

### [개념]

State Ownership은 어떤 Component 또는 Store가 State를 소유하고 변경할 책임을 가지는지 결정하는 기준이다.

State Owner는 State의 Source of Truth가 된다.

---

### [핵심]

State Owner 결정 기준:

- State를 읽는 Component
- State를 변경하는 Component
- State를 공유하는 Component들의 공통 부모
- 여러 페이지에서 필요한지 여부
- 서버가 원본인지 여부
- URL과 동기화할 필요 여부
- 지속 저장이 필요한지 여부
- logout/reset이 필요한지 여부

---

### [실무]

State Ownership Flow:

```text
Identify State
→ Find Readers
→ Find Writers
→ Find Closest Common Owner
→ Check Server Ownership
→ Check URL Persistence
→ Check Global Scope
→ Place State
```

예시 판단:

```text
SearchForm 입력값만 필요
→ SearchForm Local State

SearchForm 결과가 FestivalList에 필요
→ FestivalPage Shared State

검색 조건을 공유 URL로 복원해야 함
→ URL State

축제 목록은 서버 원본
→ Server State / TanStack Query

로그인 여부는 여러 페이지에서 필요
→ Auth State / Global Store 또는 Context
```

주의:

- State를 너무 위로 올리면 Props 전달과 Re-render 범위가 증가한다.
- State를 너무 아래에 두면 공유가 어렵다.
- 전역 Store는 마지막 선택지로 검토한다.
- Server State를 Client State처럼 직접 소유하지 않는다.
- Derived State를 별도 Owner에게 저장하지 않는다.

---

### [FAQ]

Q. State Owner가 뭐야?
A. State를 소유하고 변경할 책임을 가지는 Component 또는 Store다.

Q. State는 어디에 둬야 해?
A. 그 State를 읽고 변경하는 Component들의 가장 가까운 공통 부모에 두는 것이 기본이다.

Q. State Owner가 잘못되면 어떤 문제가 생겨?
A. Props Drilling, 중복 상태, 불필요한 Re-render, 데이터 불일치 문제가 생길 수 있다.

---

## 7.2 Closest Common Owner

### [개념]

Closest Common Owner는 같은 State를 사용하는 Component들의 가장 가까운 공통 부모다.

React State 배치의 기본 원칙은 State를 필요한 곳보다 더 높게 올리지 않는 것이다.

---

### [핵심]

Closest Common Owner 사용 상황:

- 형제 Component가 같은 State를 읽음
- 한 자식 Component의 이벤트 결과가 다른 자식 Component에 필요
- 부모가 자식 State를 기준으로 렌더링 결정
- Page 내부 여러 Section이 같은 filter 사용
- List와 Detail Preview가 같은 selected id 사용

---

### [실무]

Closest Common Owner 판단 예:

```jsx
function ProductPage() {
  const [selectedProductId, setSelectedProductId] = useState(null);

  return (
    <>
      <ProductList onSelect={setSelectedProductId} />
      <ProductPreview productId={selectedProductId} />
    </>
  );
}
```

판단 기준:

```text
ProductList만 selectedProductId 필요 → ProductList Local State
ProductPreview도 selectedProductId 필요 → ProductPage Shared State
여러 Page에서 selectedProductId 필요 → Global State 검토
URL로 공유해야 함 → URL State 검토
```

주의:

- 가장 가까운 공통 부모보다 더 높게 올리지 않는다.
- App 최상단 State는 정말 전역일 때만 사용한다.
- Page State로 충분하면 Global Store를 쓰지 않는다.
- Component 구조가 복잡하면 Composition도 함께 검토한다.

---

### [FAQ]

Q. 가장 가까운 공통 부모에 State를 둔다는 게 무슨 뜻이야?
A. 해당 State를 사용하는 Component들을 모두 포함하는 가장 낮은 부모 Component가 State를 소유한다는 뜻이다.

Q. 공통 부모가 너무 위에 있으면 어떻게 해?
A. Component 구조를 재검토하거나 Context, Store, URL State를 검토한다.

Q. 모든 Shared State를 App에 두면 편하지 않아?
A. 초반에는 편해 보이지만 Props 전달, Re-render 범위, 유지보수 비용이 커질 수 있다.

---

# 8. Lifting State Up

## 8.1 Lifting State Up Definition

### [개념]

Lifting State Up은 여러 Component가 같은 State를 공유해야 할 때 State를 공통 부모로 올리는 React 패턴이다.

Local State가 Shared State로 바뀌는 대표적인 과정이다.

---

### [핵심]

Lifting State Up 사용 상황:

- 형제 Component가 같은 상태 필요
- 검색 Form 상태가 목록에 영향
- 선택된 item이 상세 영역에 영향
- Form 입력이 Preview에 영향
- 부모가 자식 이벤트 결과를 알아야 함
- 자식 Component 간 데이터 동기화 필요

---

### [실무]

Lifting State Up 예:

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

권장 기준:

- 공유 필요가 생긴 시점에 올린다.
- 너무 일찍 App까지 올리지 않는다.
- callback props로 변경 요청을 전달한다.
- State Owner를 명확히 표현한다.
- Props 전달이 깊어지면 구조 개선을 검토한다.

주의:

- State를 올리면 하위 Component가 부모 State에 의존한다.
- 필요 이상으로 올리면 재사용성이 낮아질 수 있다.
- Lifting State Up은 Global State 도입과 다르다.
- URL State가 더 적합한 검색 조건인지 확인한다.

---

### [FAQ]

Q. Lifting State Up은 언제 해?
A. 여러 Component가 같은 State를 읽거나 변경 결과를 공유해야 할 때 한다.

Q. State를 올리면 무조건 좋은 거야?
A. 아니다. 필요한 범위보다 높게 올리면 Props 전달과 Re-render 범위가 커질 수 있다.

Q. Lifting State Up과 Global State는 같아?
A. 아니다. Lifting State Up은 공통 부모로 올리는 것이고, Global State는 앱 전체 공유 상태로 관리하는 것이다.

---

## 8.2 Lifting State Up Decision Flow

### [개념]

Lifting State Up Decision Flow는 Local State를 공통 부모로 이동해야 하는지 판단하는 절차다.

기본 원칙은 Local State를 유지하다가 공유 필요가 명확해지면 올리는 것이다.

---

### [핵심]

Decision Flow:

```text
Local State 존재
→ 다른 Component가 같은 값을 읽는가?
→ 다른 Component가 변경 결과를 알아야 하는가?
→ 공통 부모가 가까운가?
→ 공통 부모로 State 이동
→ Props와 callback 전달
→ Props Drilling 여부 점검
```

---

### [실무]

예시 시나리오:

```text
문제:
SearchInput이 keyword를 가지고 있고 FestivalList가 keyword로 필터링해야 함

판단:
SearchInput만 keyword 필요 → Local State
FestivalList도 keyword 필요 → FestivalPage로 Lifting State Up

결과:
FestivalPage가 keyword Owner
SearchInput은 onSearch 호출
FestivalList는 keyword props 수신
```

검토 기준:

- Lifting 후 Props 전달 깊이가 1~2단계면 정상이다.
- Lifting 후 전달 깊이가 깊고 반복되면 Props Drilling 검토가 필요하다.
- 검색 조건이 URL 공유 대상이면 URL Search Params를 검토한다.
- API 데이터 필터 조건이면 queryKey와 함께 관리할 수 있다.

---

### [FAQ]

Q. Local State를 언제 Shared State로 바꿔?
A. 다른 Component가 같은 값을 읽거나 변경 결과를 알아야 할 때 Shared State로 바꾼다.

Q. Lifting State Up 후 Props가 많아지면 어떻게 해?
A. State Owner, Component 구조, Composition, Context, Store, URL State를 순서대로 검토한다.

Q. 검색 keyword는 Lifting State Up만 하면 돼?
A. 검색 결과 공유나 새로고침 복원이 필요하면 URL State가 더 적합할 수 있다.

---

# 9. Derived State

## 9.1 Derived State Definition

### [개념]

Derived State는 기존 Props, State, Server Data로부터 계산 가능한 값이다.

계산 가능한 값은 별도 State로 저장하지 않는 것이 기본 원칙이다.

---

### [핵심]

Derived State 예:

- fullName
- filteredItems
- sortedItems
- totalPrice
- selectedItem
- isValid
- canSubmit
- visibleItems
- completedCount
- averageRating
- hasPermission

---

### [실무]

나쁜 예:

```jsx
const [items, setItems] = useState([]);
const [keyword, setKeyword] = useState("");
const [filteredItems, setFilteredItems] = useState([]);
```

좋은 예:

```jsx
const [items, setItems] = useState([]);
const [keyword, setKeyword] = useState("");

const filteredItems = items.filter((item) => item.title.includes(keyword));
```

Derived State 관리 기준:

- 원본 State에서 계산한다.
- 별도 State로 저장하지 않는다.
- 계산 비용이 큰 경우 useMemo를 검토한다.
- 서버 응답 변환은 mapping 함수로 분리할 수 있다.
- Store에 Derived State를 과도하게 저장하지 않는다.

주의:

- 원본 State와 Derived State가 불일치할 수 있다.
- setState 순서와 동기화 오류가 발생할 수 있다.
- Server State를 복사한 Derived State는 stale data 원인이 될 수 있다.

---

### [FAQ]

Q. Derived State가 뭐야?
A. 기존 Props, State, Server Data로부터 계산 가능한 값이다.

Q. 계산 가능한 값도 State로 저장해야 해?
A. 대부분 아니다. 기존 State나 Props로 계산 가능하면 렌더링 중 계산하는 것이 좋다.

Q. Derived State가 위험한 이유는?
A. 원본 상태가 바뀌었는데 파생 상태가 갱신되지 않아 데이터 불일치가 생길 수 있다.

---

## 9.2 Derived State Decision Criteria

### [개념]

Derived State Decision Criteria는 어떤 값이 저장 대상인지 계산 대상인지 판단하는 기준이다.

State로 저장하기 전에 기존 값으로 계산 가능한지 확인해야 한다.

---

### [핵심]

Derived State 판단 질문:

- 기존 State로 계산 가능한가?
- Props로 계산 가능한가?
- Server Data로 계산 가능한가?
- filter / sort 결과인가?
- count / sum / average 결과인가?
- boolean 조건 결과인가?
- selected id로 찾을 수 있는 item인가?

---

### [실무]

Derived State 판단 Flow:

```text
새 State 추가 필요
→ 기존 State / Props / Server Data로 계산 가능한가?
→ 계산 가능하면 State 저장 금지
→ 렌더링 중 계산
→ 비용이 크면 memoization 검토
```

예시:

```text
items + keyword → filteredItems
firstName + lastName → fullName
cartItems → totalPrice
user.role → isAdmin
selectedId + items → selectedItem
form values → canSubmit
```

주의:

- Derived State를 Global Store에 넣지 않는다.
- Derived State와 원본 State를 동시에 업데이트하지 않는다.
- query cache 데이터를 복사해 별도 State로 보관하지 않는다.
- 성능 문제는 먼저 측정하고 useMemo를 적용한다.

---

### [FAQ]

Q. filteredItems를 State로 저장하면 안 돼?
A. items와 keyword로 계산 가능하면 별도 State로 저장하지 않는 것이 좋다.

Q. selectedItem은 State로 저장해야 해?
A. selectedId와 items로 찾을 수 있으면 selectedId만 저장하고 selectedItem은 계산하는 것이 좋다.

Q. Derived State에 useMemo를 항상 써야 해?
A. 아니다. 계산 비용이 크거나 렌더링 비용 문제가 있을 때 검토한다.

---

# 10. URL State

## 10.1 URL State Definition

### [개념]

URL State는 URL path나 query string에 저장되는 상태다.

검색 조건, 필터, 정렬, 페이지 번호처럼 공유와 복원이 필요한 상태에 적합하다.

---

### [핵심]

URL State 사용 대상:

- search keyword
- filter
- sort
- page
- selected category
- selected tab
- date range
- path parameter
- query string
- map position basics

---

### [실무]

URL State 예:

```text
/festivals?keyword=flower&region=seoul&page=1
```

URL State 적합 조건:

- URL 공유 필요
- 새로고침 후 유지 필요
- 뒤로가기 / 앞으로가기 복원 필요
- 검색 결과 페이지
- 목록 필터 페이지
- 페이지네이션
- 탭 화면
- 상세 페이지 id

주의:

- URL 값은 문자열이다.
- 숫자와 boolean 변환이 필요하다.
- 민감정보를 저장하지 않는다.
- 너무 복잡한 객체를 저장하지 않는다.
- Form 입력 중 임시값과 제출된 URL State를 구분한다.

---

### [FAQ]

Q. URL State가 뭐야?
A. 검색 조건, 필터, 페이지 번호처럼 URL path나 query string에 저장되는 상태다.

Q. 검색 조건은 State로 둬야 해 URL로 둬야 해?
A. 검색 결과를 공유하거나 새로고침 후 유지해야 하면 URL State가 적합하다.

Q. URL State에 민감정보를 넣어도 돼?
A. 안 된다. URL은 브라우저 기록, 공유 링크, 서버 로그에 남을 수 있다.

---

## 10.2 URL State vs Component State

### [개념]

URL State와 Component State는 복원성과 공유 가능성에서 차이가 있다.

검색 조건, 필터, 페이지 번호는 Component State보다 URL State가 더 적합한 경우가 많다.

---

### [핵심]

URL State 적합:

- 공유 링크 필요
- 새로고침 복원 필요
- 뒤로가기 복원 필요
- 검색 조건
- 필터 조건
- 페이지 번호
- 정렬 조건

Component State 적합:

- 입력 중 임시값
- modal open
- dropdown open
- local tab
- hover state
- Form 내부 상태

---

### [실무]

비교:

| 비교          | URL State                  | Component State    |
| ------------- | -------------------------- | ------------------ |
| 저장 위치     | URL                        | React Memory       |
| 새로고침 유지 | 가능                       | 기본적으로 불가    |
| 공유 링크     | 가능                       | 불가               |
| 뒤로가기 복원 | 가능                       | 직접 구현 필요     |
| 적합 예       | keyword, page, sort        | modal, input draft |
| 주의          | 문자열 변환, 민감정보 금지 | 공유/복원 어려움   |

판단 기준:

```text
검색 Form 입력 중 keyword → Local State
검색 submit 후 keyword → URL State
URL keyword 변경 → queryKey 변경
queryKey 변경 → Server State refetch
```

---

### [FAQ]

Q. 검색 input 입력 중 값도 URL에 바로 넣어야 해?
A. 필수는 아니다. 입력 중 임시값은 Local State로 두고 submit 후 URL State로 반영할 수 있다.

Q. page number는 URL State가 좋아?
A. 목록 페이지에서 새로고침과 공유가 필요하면 URL State가 적합하다.

Q. modal open도 URL State로 둬야 해?
A. 일반 modal은 Component State가 적합하다. 단, 특정 modal 상태를 공유 링크로 열어야 하면 URL State를 검토할 수 있다.

---

# 11. Auth State

## 11.1 Auth State Definition

### [개념]

Auth State는 사용자의 인증 여부와 사용자 요약 정보를 표현하는 상태다.

Auth State는 여러 페이지와 Component에서 필요하므로 Global State 또는 Context로 관리하는 경우가 많다.

---

### [핵심]

Auth State 구성:

- authenticated
- auth loading
- user summary
- role
- access token handling
- refresh token handling
- login
- logout
- token expired
- protected route relation
- user-specific cache reset

---

### [실무]

Auth State 예:

```typescript
type AuthState = {
  authenticated: boolean;
  loading: boolean;
  user: {
    userId: number;
    nickname: string;
    role: "ROLE_USER" | "ROLE_ADMIN";
  } | null;
};
```

Auth State 관리 기준:

- 인증 확인 중 loading 상태를 분리한다.
- 로그인 / 로그아웃 action을 명확히 한다.
- 권한 role naming을 통일한다.
- Protected Route와 연결한다.
- Backend 인증/인가를 최종 보안 기준으로 둔다.
- Token 저장 위치는 보안 기준에 따라 신중히 결정한다.
- 민감정보 Store 저장을 최소화한다.
- logout 시 관련 Store와 Query Cache reset을 고려한다.

---

### [FAQ]

Q. Auth State는 전역 상태가 좋아?
A. 대부분 여러 페이지와 Component에서 필요하므로 전역 상태나 Context로 관리하는 경우가 많다.

Q. Frontend에서 로그인 상태만 확인하면 보안이 돼?
A. 아니다. Frontend 인증 상태는 UX용이고 실제 보안은 Backend 인증/인가가 반드시 필요하다.

Q. logout 시 어떤 상태를 초기화해야 해?
A. user, authenticated, notification, user-specific cache, 민감한 화면 상태 등을 초기화해야 한다.

---

## 11.2 Auth State Ownership

### [개념]

Auth State Ownership은 인증 상태의 Source of Truth를 어디에 둘지 결정하는 기준이다.

Frontend Auth State는 UX와 화면 제어를 위한 상태이며, 실제 보안 판단은 Backend가 담당해야 한다.

---

### [핵심]

Auth State Owner 후보:

- Auth Context
- Zustand authStore
- Redux authSlice
- TanStack Query user profile cache
- Protected Route
- API Interceptor
- Backend Session / Token Validation

---

### [실무]

Auth State 분리 예:

```text
authenticated / user summary
→ Auth Store 또는 Auth Context

user profile detail
→ Server State / TanStack Query

access token handling
→ 인증 구조 기준에 따라 관리

protected route visibility
→ Auth State 기반 UX 처리

role authorization
→ Frontend UX 처리 + Backend 최종 검증
```

주의:

- JWT 존재만으로 authenticated true를 신뢰하지 않는다.
- role check는 Backend에서도 반드시 수행한다.
- localStorage에 민감정보 저장을 신중히 검토한다.
- refresh 실패 시 Auth Store reset이 필요하다.
- logout 시 Query Cache와 사용자별 Store를 초기화한다.

---

### [FAQ]

Q. user profile은 Auth Store에 넣어야 해?
A. 사용자 요약 정보는 Auth Store에 둘 수 있지만 상세 프로필은 Server State로 관리하는 것이 적합할 수 있다.

Q. JWT가 있으면 로그인 상태로 봐도 돼?
A. UX상 임시 판단은 가능하지만 만료와 위조 가능성이 있으므로 서버 검증 또는 인증 확인 흐름이 필요하다.

Q. 권한 체크는 Frontend에서만 해도 돼?
A. 아니다. Frontend 권한 체크는 UX용이고 실제 접근 제어는 Backend에서 반드시 처리해야 한다.

---

# 12. Form State

## 12.1 Form State Definition

### [개념]

Form State는 사용자의 입력값, 검증 상태, 제출 상태를 관리하는 상태다.

Form State는 대부분 Form 내부에서 관리하며, 무조건 Global State로 올리지 않는다.

---

### [핵심]

Form State 구성:

- input value
- touched
- dirty
- validation error
- submit status
- disabled state
- server validation error
- reset
- controlled input

---

### [실무]

간단한 Form State 예:

```jsx
function ReviewForm({ onSubmit }) {
  const [content, setContent] = useState("");
  const [rating, setRating] = useState(5);

  function handleSubmit(event) {
    event.preventDefault();

    if (!content.trim()) {
      return;
    }

    onSubmit({ content: content.trim(), rating });
  }

  return null;
}
```

Form State 관리 기준:

- 단순 Form은 useState로 충분하다.
- 상태 전환이 복잡하면 useReducer를 검토한다.
- 입력 필드와 검증 규칙이 많으면 Form Library를 검토한다.
- 제출 후 서버 응답 상태와 입력 상태를 구분한다.
- Form 입력값을 무조건 Global State로 두지 않는다.
- 민감한 Form 입력값은 persist하지 않는다.

---

### [FAQ]

Q. Form State는 전역으로 둬야 해?
A. 대부분 아니다. Form 내부에서만 필요한 입력값은 Local State나 Form Library로 관리하는 것이 좋다.

Q. React Hook Form은 언제 써?
A. 입력 필드와 검증 규칙이 많고 touched, dirty, error 상태 관리가 복잡할 때 검토한다.

Q. Form 입력값을 localStorage에 저장해도 돼?
A. 민감정보가 포함될 수 있으므로 신중해야 한다. 비민감 임시저장 요구가 있을 때만 제한적으로 검토한다.

---

## 12.2 Form State Ownership

### [개념]

Form State Ownership은 입력값과 검증 상태를 Form 내부에 둘지, 부모로 올릴지, URL이나 Store와 연결할지 결정하는 기준이다.

---

### [핵심]

Form State Owner 판단:

- Form 내부에서만 사용 → Form Local State
- 부모가 제출 결과만 필요 → callback 전달
- 입력 중 Preview 필요 → 공통 부모 Shared State
- 검색 결과 복원 필요 → URL State
- 복잡한 검증 필요 → Form Library
- 여러 Step 공유 필요 → useReducer 또는 Store 검토

---

### [실무]

Form State 판단 Flow:

```text
Form 입력값 발견
→ Form 내부에서만 필요한가?
→ 제출 결과만 부모에 전달하면 되는가?
→ 입력 중 다른 Component가 필요한가?
→ URL 복원이 필요한 검색 조건인가?
→ 복잡한 검증과 dirty/touched가 필요한가?
→ 관리 방식 결정
```

예시:

```text
로그인 Form input → Form Local State
리뷰 작성 content/rating → Form Local State
검색 Form submit keyword → URL State
회원가입 복잡 검증 → Form Library
Wizard Step Form → useReducer 또는 Store 검토
```

---

### [FAQ]

Q. 부모가 Form 값을 알아야 하면 어떻게 해?
A. 제출 시 callback으로 결과만 전달하거나, 입력 중 공유가 필요하면 공통 부모로 State를 올린다.

Q. 검색 Form은 Form State야 URL State야?
A. 입력 중 값은 Form State이고, 제출되어 검색 결과를 결정하는 값은 URL State가 적합할 수 있다.

Q. Form State를 Zustand에 넣어도 돼?
A. Wizard처럼 여러 페이지나 Step에서 공유해야 하는 특수한 경우가 아니면 권장하지 않는다.

---

# 13. State Ownership Anti Patterns

## 13.1 Overused Global State

### [개념]

Overused Global State는 Local State나 Shared State로 충분한 값을 전역 Store에 과도하게 넣는 문제다.

전역 상태 남용은 State Management에서 가장 흔한 Anti Pattern이다.

---

### [핵심]

문제:

- Store가 너무 커짐
- 상태 변경 영향 범위 증가
- 데이터 흐름 추적 어려움
- Component 재사용성 저하
- 불필요한 persistence 증가
- 서버 데이터와 중복 저장
- logout/reset 누락 가능성 증가

원인:

- State Classification 생략
- Props 전달을 모두 문제로 판단
- 전역 상태 도구를 기본 선택지로 사용
- Server State와 Client State 혼동
- Derived State 저장

---

### [실무]

Overused Global State Debug Flow:

```text
Store Field Review
→ Usage Scope Check
→ Local State 가능 여부 확인
→ Shared State 가능 여부 확인
→ URL State 가능 여부 확인
→ Server State 여부 확인
→ Derived State 여부 확인
→ Store Slim Down
```

잘못된 예:

```text
authStore
- user
- authenticated
- loginModalOpen
- searchKeyword
- festivalList
- filteredFestivalList
- reviewFormContent
```

개선 예:

```text
authStore
- user
- authenticated

uiStore
- globalToast

URL State
- searchKeyword

TanStack Query
- festivalList

Local State
- reviewFormContent

Derived Value
- filteredFestivalList
```

---

### [FAQ]

Q. 전역 Store가 너무 커졌으면 어떻게 해?
A. 각 상태의 사용 범위와 소유자를 다시 확인하고 Local State, Shared State, URL State, Server State로 분리한다.

Q. 전역 상태가 많으면 왜 안 좋아?
A. 변경 영향 범위가 커지고 데이터 흐름을 추적하기 어려워지며 유지보수 비용이 증가한다.

Q. Props 전달이 싫어서 전부 Store에 넣어도 돼?
A. 권장하지 않는다. 먼저 Props 전달이 실제 문제인지 확인하고 State Owner와 Component 구조를 재검토해야 한다.

---

## 13.2 Duplicate State Problem

### [개념]

Duplicate State Problem은 같은 의미의 데이터를 여러 State에 중복 저장해 불일치가 발생하는 문제다.

Single Source of Truth가 깨지면 화면마다 다른 값이 표시될 수 있다.

---

### [핵심]

문제:

- 목록 데이터와 필터 결과가 불일치
- user 정보가 authStore와 component state에서 다름
- API cache와 global store 값이 다름
- 수정 후 일부 화면만 갱신
- 선택 상태와 URL 값 불일치
- Form 값과 Store 값 불일치

원인:

- Derived State 저장
- Server State local copy
- Store와 Component State 중복
- URL State와 Local State 중복
- Mapping 기준 불명확

---

### [실무]

Duplicate State Debug Flow:

```text
Find Duplicated Values
→ Decide Source of Truth
→ Remove Derived State
→ Use Mapping Function
→ Sync URL or Query Cache
→ Remove Local Copy
```

예시:

```text
문제:
festivals와 filteredFestivals를 둘 다 State로 저장

원인:
filteredFestivals는 festivals + keyword로 계산 가능한 Derived State

해결:
filteredFestivals State 제거
렌더링 시 festivals와 keyword로 계산
```

Source of Truth 기준:

```text
Server Data → Query Cache
검색 조건 → URL
Form 입력 중 값 → Form State
인증 요약 → Auth Store
계산 결과 → Derived Value
```

---

### [FAQ]

Q. 같은 값을 여러 State에 저장하면 왜 문제야?
A. 한쪽만 갱신되면 화면마다 다른 값이 표시되는 데이터 불일치가 생길 수 있다.

Q. Single Source of Truth가 뭐야?
A. 하나의 데이터는 하나의 기준 출처에서 관리하고 나머지는 그 값을 기반으로 계산하는 원칙이다.

Q. API cache 데이터를 Store에도 복사하면 안 돼?
A. 중복 저장으로 stale data가 발생할 수 있으므로 Query Cache를 기준으로 두는 것이 좋다.

---

## 13.3 Wrong State Owner

### [개념]

Wrong State Owner는 State를 읽고 변경하는 실제 위치와 다른 곳이 State를 소유하는 문제다.

State Owner가 잘못되면 Props Drilling, 중복 저장, 불필요한 Re-render가 발생할 수 있다.

---

### [핵심]

Wrong State Owner 증상:

- State가 너무 높은 Component에 있음
- State가 너무 낮아 형제 Component가 공유하지 못함
- Store에 있지만 특정 Component만 사용함
- URL에 있어야 할 값이 Component State에만 있음
- Server State가 Client Store에 저장됨
- Derived State가 별도 State로 저장됨

---

### [실무]

Wrong State Owner Debug Flow:

```text
문제 State 식별
→ Readers 확인
→ Writers 확인
→ 공통 부모 확인
→ Server Ownership 확인
→ URL Persistence 확인
→ Derived 여부 확인
→ Owner 재배치
```

재배치 예:

```text
단일 Component만 사용 → Local State로 내림
Page 내부 여러 Component 사용 → Page Shared State
여러 Page 사용 → Global State 검토
API 원본 데이터 → Server State로 이동
검색 조건 복원 필요 → URL State로 이동
계산 가능 값 → Derived Value로 제거
```

---

### [FAQ]

Q. State Owner가 잘못됐는지 어떻게 알아?
A. State를 읽고 변경하는 위치, 공유 범위, 서버 원본 여부, URL 복원 필요성을 확인하면 판단할 수 있다.

Q. State가 너무 위에 있으면 어떤 문제가 생겨?
A. Props 전달이 늘고 Re-render 범위가 커지며 Component 재사용성이 낮아질 수 있다.

Q. State가 너무 아래에 있으면 어떤 문제가 생겨?
A. 형제 Component나 부모 Component가 같은 값을 공유하기 어려워져 중복 State가 생길 수 있다.

---

# 14. State Classification Checklist

## 14.1 State Classification Checklist

### [개념]

State Classification Checklist는 새로운 State를 추가하기 전에 반드시 확인해야 하는 검수 기준이다.

Frontend Agent는 코드 생성 전에 이 Checklist로 상태 배치를 검토해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] 이 State는 Client State인가 Server State인가?
- [ ] 이 State는 Local State로 충분한가?
- [ ] 여러 Component가 공유해야 하는가?
- [ ] 여러 Page에서 필요한가?
- [ ] URL에 저장해야 하는가?
- [ ] Form 입력 상태인가?
- [ ] Auth State인가?
- [ ] UI 표시 상태인가?
- [ ] 기존 값으로 계산 가능한 Derived State인가?
- [ ] API 응답 데이터를 중복 저장하고 있지 않은가?
- [ ] 가장 가까운 공통 Owner에 위치하는가?
- [ ] Props Drilling이 실제 문제인가?
- [ ] Global Store 도입이 필요한가?
- [ ] logout/reset 대상인가?
- [ ] persist 대상인가?
- [ ] 민감정보 저장 위험이 있는가?
```

---

### [실무]

State 추가 전 검수 Flow:

```text
New State Request
→ Classification Check
→ Ownership Check
→ Scope Check
→ Derived Check
→ Server State Check
→ URL State Check
→ Tool Selection
→ Anti Pattern Review
```

판단 결과 예:

```text
reviewFormContent
→ Form State
→ Local State
→ ReviewForm Owner
→ Global Store 금지

festivalList
→ Server State
→ TanStack Query
→ Zustand 중복 저장 금지

searchKeyword
→ URL State
→ URL Search Params
→ queryKey 포함

filteredFestivalList
→ Derived State
→ State 저장 금지
```

---

### [FAQ]

Q. 새 State를 만들기 전에 무엇을 확인해야 해?
A. State Type, Owner, Scope, Server State 여부, URL State 여부, Derived State 여부를 먼저 확인해야 한다.

Q. State Classification Checklist가 왜 필요해?
A. 불필요한 전역 상태, 중복 상태, Server State 혼동, Derived State 저장 문제를 줄이기 위해 필요하다.

Q. Frontend Agent는 State를 만들 때 어떤 순서로 판단해야 해?
A. State Classification, State Ownership, Scope, Tool Selection, Anti Pattern 검토 순서로 판단해야 한다.

---

# 15. Part01 Final Review

## 15.1 Part01 Scope Summary

### [개념]

Part01은 State Management의 기초 판단 기준인 State Classification과 State Ownership을 다룬다.

이 문서는 상태관리 도구 사용법보다 상태를 어떻게 분류하고 어디에 둘지 판단하는 데 집중한다.

---

### [핵심]

Part01 포함 범위:

- State Management Purpose
- State Classification
- Client State
- Server State
- Local State
- Shared State
- Global State
- State Ownership
- Closest Common Owner
- Lifting State Up
- Derived State
- URL State
- Auth State
- Form State
- Ownership Anti Patterns
- State Classification Checklist

---

### [실무]

Part01 이후 문서 연결:

```text
Part01 State Classification and Ownership
→ Part02 Context API and useReducer
→ Part03 Zustand and Redux Toolkit
→ Part04 TanStack Query and Server State
→ Part05 Form State and Auth State
→ Part06 State Debugging and Anti Patterns
```

Agent 사용 기준:

```text
User Frontend State Request
→ Part01로 State Type과 Owner 판단
→ 이후 Part 문서로 Tool Selection 세부 구현
```

---

### [FAQ]

Q. Part01의 핵심 목적은 뭐야?
A. React State를 무작정 전역화하지 않고 State Type, Owner, Scope 기준으로 적절한 위치를 판단하게 하는 것이다.

Q. Part01에서 도구 사용법을 깊게 다뤄?
A. 아니다. useState, Context, Zustand, Redux Toolkit, TanStack Query 선택 전에 필요한 분류와 소유자 판단 기준을 다룬다.

Q. Part01 다음에는 무엇을 다뤄야 해?
A. Context API와 useReducer, Zustand와 Redux Toolkit, TanStack Query, Form/Auth State, Debugging과 Anti Pattern으로 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. State Management는 왜 필요해?
A. React 상태를 어디에 두고 어떤 도구로 관리할지 판단해야 유지보수 가능한 Frontend 구조를 만들 수 있기 때문이다.

Q. State Management는 Redux 사용법이야?
A. 아니다. Redux, Zustand, Context, TanStack Query 중 무엇을 선택할지 결정하기 전 State 종류와 소유자를 분류하는 설계 기준이다.

Q. State Management에서 가장 먼저 해야 할 일은 뭐야?
A. State Classification이다. 상태 종류를 먼저 분류해야 적절한 관리 위치와 도구를 선택할 수 있다.

Q. State Classification이 뭐야?
A. State를 Local, Shared, Global, Server, Form, Auth, URL State처럼 성격과 범위에 따라 분류하는 작업이다.

Q. State Classification은 왜 먼저 해?
A. 상태 종류를 구분해야 useState, useReducer, Context, Zustand, Redux Toolkit, TanStack Query 중 적절한 도구를 선택할 수 있기 때문이다.

Q. 모든 State를 Zustand나 Redux에 넣으면 안 돼?
A. 권장하지 않는다. Local State나 Form State까지 전역화하면 데이터 흐름이 복잡해지고 유지보수 비용이 증가한다.

Q. API 응답 목록은 Global State야?
A. 대부분 Server State다. 캐시, refetch, stale data 관리가 필요하면 TanStack Query 같은 Server State 도구가 적합하다.

Q. 검색 조건은 Local State야?
A. 단순 입력 중 임시값은 Local State지만, 결과 공유와 새로고침 복원이 필요하면 URL State가 적합하다.

Q. Client State가 뭐야?
A. Frontend가 원본을 소유하고 화면 표시나 사용자 상호작용을 위해 관리하는 상태다.

Q. modal open은 Client State야?
A. 맞다. modal open 여부는 Frontend UI 표시 상태이므로 Client State다.

Q. Client State는 무조건 전역 Store에 둬야 해?
A. 아니다. 대부분은 useState나 useReducer로 충분하고, 여러 페이지에서 필요한 경우에만 전역 Store를 검토한다.

Q. Server State가 뭐야?
A. 서버가 원본으로 소유하고 Frontend가 조회, 캐싱, 갱신하는 데이터다.

Q. API 응답 데이터는 Client State야 Server State야?
A. 대부분 Server State다. 서버가 원본 소유자이고 Frontend는 캐시하거나 화면에 표시한다.

Q. Server State를 Zustand에 넣으면 안 돼?
A. 가능은 하지만 캐시, stale data, refetch, mutation 관리가 복잡하면 TanStack Query 같은 Server State 도구가 더 적합하다.

Q. Client State와 Server State를 왜 나눠?
A. 소유자와 갱신 방식이 다르기 때문이다. Server State는 서버 동기화와 캐시 전략이 중요하다.

Q. user profile은 Auth State야 Server State야?
A. 서버에서 조회하는 원본 데이터는 Server State이고, 로그인 여부와 사용자 요약은 Auth State로 관리할 수 있다.

Q. 목록에서 선택된 item id는 Server State야?
A. 보통 selected item id는 Client State이고, 해당 id로 조회한 상세 데이터는 Server State다.

Q. Local State는 언제 써?
A. 특정 Component 내부에서만 필요하고 다른 Component와 공유하지 않는 상태에 사용한다.

Q. input 값은 무조건 전역 상태로 둬야 해?
A. 아니다. 해당 Form 내부에서만 필요한 입력값은 Local State가 적합하다.

Q. modal open 상태는 Local State로 둬도 돼?
A. 해당 화면이나 Component 안에서만 열고 닫는 modal이면 Local State가 적합하다.

Q. State를 Local로 둘지 어떻게 판단해?
A. 해당 Component만 읽고 변경하며 외부 공유나 복원이 필요 없으면 Local State로 둔다.

Q. Local State를 나중에 Shared State로 바꿔도 돼?
A. 가능하다. 처음부터 너무 높게 올리지 말고 공유 필요가 생긴 시점에 올리는 것이 좋다.

Q. Local State가 많으면 무조건 문제야?
A. 아니다. 각 Component 내부에서만 필요한 상태라면 Local State가 많은 것은 자연스럽다.

Q. Shared State는 전역 상태야?
A. 항상 전역 상태는 아니다. 특정 Page 내부에서만 공유되면 공통 부모 State로 충분할 수 있다.

Q. 형제 Component가 같은 값을 써야 하면 어떻게 해?
A. 가장 가까운 공통 부모로 State를 올리고 Props와 callback으로 전달한다.

Q. Shared State는 Context로 관리해야 해?
A. 필수는 아니다. 공유 범위가 좁으면 부모 State와 Props 전달이 더 단순하다.

Q. Shared State와 Global State 차이는?
A. Shared State는 특정 Component 집합에서 공유되는 상태이고, Global State는 여러 페이지나 앱 전체에서 공유되는 상태다.

Q. Page 내부 filter는 Global State로 둬야 해?
A. 보통 아니다. 해당 Page 내부에서만 필요하면 Page Component의 Shared State로 충분하다.

Q. Shared State가 많아지면 어떻게 해?
A. State Owner를 재검토하고, Props Drilling이 심하면 Context, Zustand, URL State 등을 검토한다.

Q. Global State는 언제 써?
A. 여러 페이지나 깊은 Component Tree에서 반복적으로 필요한 상태일 때 사용한다.

Q. 모든 페이지에서 쓰지 않는 값도 Global State로 둬도 돼?
A. 가능은 하지만 권장하지 않는다. 필요한 범위가 좁으면 Local State나 Shared State가 더 적합하다.

Q. API 목록 데이터를 Global State에 저장해도 돼?
A. 무조건 권장하지 않는다. 서버 데이터는 TanStack Query 같은 Server State 도구가 더 적합할 수 있다.

Q. 전역 Store는 어떻게 나누는 게 좋아?
A. auth, ui, notification처럼 도메인 또는 책임 기준으로 나누는 것이 좋다.

Q. 전역 Store 하나에 모든 상태를 넣어도 돼?
A. 권장하지 않는다. Store가 거대해지면 데이터 흐름 추적과 유지보수가 어려워진다.

Q. Global State 도입 전에 무엇을 확인해야 해?
A. Local, Shared, URL, Server State로 충분한지 먼저 확인해야 한다.

Q. State Owner가 뭐야?
A. State를 소유하고 변경할 책임을 가지는 Component 또는 Store다.

Q. State는 어디에 둬야 해?
A. 그 State를 읽고 변경하는 Component들의 가장 가까운 공통 부모에 두는 것이 기본이다.

Q. State Owner가 잘못되면 어떤 문제가 생겨?
A. Props Drilling, 중복 상태, 불필요한 Re-render, 데이터 불일치 문제가 생길 수 있다.

Q. 가장 가까운 공통 부모에 State를 둔다는 게 무슨 뜻이야?
A. 해당 State를 사용하는 Component들을 모두 포함하는 가장 낮은 부모 Component가 State를 소유한다는 뜻이다.

Q. 공통 부모가 너무 위에 있으면 어떻게 해?
A. Component 구조를 재검토하거나 Context, Store, URL State를 검토한다.

Q. 모든 Shared State를 App에 두면 편하지 않아?
A. 초반에는 편해 보이지만 Props 전달, Re-render 범위, 유지보수 비용이 커질 수 있다.

Q. Lifting State Up은 언제 해?
A. 여러 Component가 같은 State를 읽거나 변경 결과를 공유해야 할 때 한다.

Q. State를 올리면 무조건 좋은 거야?
A. 아니다. 필요한 범위보다 높게 올리면 Props 전달과 Re-render 범위가 커질 수 있다.

Q. Lifting State Up과 Global State는 같아?
A. 아니다. Lifting State Up은 공통 부모로 올리는 것이고, Global State는 앱 전체 공유 상태로 관리하는 것이다.

Q. Local State를 언제 Shared State로 바꿔?
A. 다른 Component가 같은 값을 읽거나 변경 결과를 알아야 할 때 Shared State로 바꾼다.

Q. Lifting State Up 후 Props가 많아지면 어떻게 해?
A. State Owner, Component 구조, Composition, Context, Store, URL State를 순서대로 검토한다.

Q. 검색 keyword는 Lifting State Up만 하면 돼?
A. 검색 결과 공유나 새로고침 복원이 필요하면 URL State가 더 적합할 수 있다.

Q. Derived State가 뭐야?
A. 기존 Props, State, Server Data로부터 계산 가능한 값이다.

Q. 계산 가능한 값도 State로 저장해야 해?
A. 대부분 아니다. 기존 State나 Props로 계산 가능하면 렌더링 중 계산하는 것이 좋다.

Q. Derived State가 위험한 이유는?
A. 원본 상태가 바뀌었는데 파생 상태가 갱신되지 않아 데이터 불일치가 생길 수 있다.

Q. filteredItems를 State로 저장하면 안 돼?
A. items와 keyword로 계산 가능하면 별도 State로 저장하지 않는 것이 좋다.

Q. selectedItem은 State로 저장해야 해?
A. selectedId와 items로 찾을 수 있으면 selectedId만 저장하고 selectedItem은 계산하는 것이 좋다.

Q. Derived State에 useMemo를 항상 써야 해?
A. 아니다. 계산 비용이 크거나 렌더링 비용 문제가 있을 때 검토한다.

Q. URL State가 뭐야?
A. 검색 조건, 필터, 페이지 번호처럼 URL path나 query string에 저장되는 상태다.

Q. 검색 조건은 State로 둬야 해 URL로 둬야 해?
A. 검색 결과를 공유하거나 새로고침 후 유지해야 하면 URL State가 적합하다.

Q. URL State에 민감정보를 넣어도 돼?
A. 안 된다. URL은 브라우저 기록, 공유 링크, 서버 로그에 남을 수 있다.

Q. 검색 input 입력 중 값도 URL에 바로 넣어야 해?
A. 필수는 아니다. 입력 중 임시값은 Local State로 두고 submit 후 URL State로 반영할 수 있다.

Q. page number는 URL State가 좋아?
A. 목록 페이지에서 새로고침과 공유가 필요하면 URL State가 적합하다.

Q. modal open도 URL State로 둬야 해?
A. 일반 modal은 Component State가 적합하다. 단, 특정 modal 상태를 공유 링크로 열어야 하면 URL State를 검토할 수 있다.

Q. Auth State는 전역 상태가 좋아?
A. 대부분 여러 페이지와 Component에서 필요하므로 전역 상태나 Context로 관리하는 경우가 많다.

Q. Frontend에서 로그인 상태만 확인하면 보안이 돼?
A. 아니다. Frontend 인증 상태는 UX용이고 실제 보안은 Backend 인증/인가가 반드시 필요하다.

Q. logout 시 어떤 상태를 초기화해야 해?
A. user, authenticated, notification, user-specific cache, 민감한 화면 상태 등을 초기화해야 한다.

Q. user profile은 Auth Store에 넣어야 해?
A. 사용자 요약 정보는 Auth Store에 둘 수 있지만 상세 프로필은 Server State로 관리하는 것이 적합할 수 있다.

Q. JWT가 있으면 로그인 상태로 봐도 돼?
A. UX상 임시 판단은 가능하지만 만료와 위조 가능성이 있으므로 서버 검증 또는 인증 확인 흐름이 필요하다.

Q. 권한 체크는 Frontend에서만 해도 돼?
A. 아니다. Frontend 권한 체크는 UX용이고 실제 접근 제어는 Backend에서 반드시 처리해야 한다.

Q. Form State는 전역으로 둬야 해?
A. 대부분 아니다. Form 내부에서만 필요한 입력값은 Local State나 Form Library로 관리하는 것이 좋다.

Q. React Hook Form은 언제 써?
A. 입력 필드와 검증 규칙이 많고 touched, dirty, error 상태 관리가 복잡할 때 검토한다.

Q. Form 입력값을 localStorage에 저장해도 돼?
A. 민감정보가 포함될 수 있으므로 신중해야 한다. 비민감 임시저장 요구가 있을 때만 제한적으로 검토한다.

Q. 부모가 Form 값을 알아야 하면 어떻게 해?
A. 제출 시 callback으로 결과만 전달하거나, 입력 중 공유가 필요하면 공통 부모로 State를 올린다.

Q. 검색 Form은 Form State야 URL State야?
A. 입력 중 값은 Form State이고, 제출되어 검색 결과를 결정하는 값은 URL State가 적합할 수 있다.

Q. Form State를 Zustand에 넣어도 돼?
A. Wizard처럼 여러 페이지나 Step에서 공유해야 하는 특수한 경우가 아니면 권장하지 않는다.

Q. 전역 Store가 너무 커졌으면 어떻게 해?
A. 각 상태의 사용 범위와 소유자를 다시 확인하고 Local State, Shared State, URL State, Server State로 분리한다.

Q. 전역 상태가 많으면 왜 안 좋아?
A. 변경 영향 범위가 커지고 데이터 흐름을 추적하기 어려워지며 유지보수 비용이 증가한다.

Q. Props 전달이 싫어서 전부 Store에 넣어도 돼?
A. 권장하지 않는다. 먼저 Props 전달이 실제 문제인지 확인하고 State Owner와 Component 구조를 재검토해야 한다.

Q. 같은 값을 여러 State에 저장하면 왜 문제야?
A. 한쪽만 갱신되면 화면마다 다른 값이 표시되는 데이터 불일치가 생길 수 있다.

Q. Single Source of Truth가 뭐야?
A. 하나의 데이터는 하나의 기준 출처에서 관리하고 나머지는 그 값을 기반으로 계산하는 원칙이다.

Q. API cache 데이터를 Store에도 복사하면 안 돼?
A. 중복 저장으로 stale data가 발생할 수 있으므로 Query Cache를 기준으로 두는 것이 좋다.

Q. State Owner가 잘못됐는지 어떻게 알아?
A. State를 읽고 변경하는 위치, 공유 범위, 서버 원본 여부, URL 복원 필요성을 확인하면 판단할 수 있다.

Q. State가 너무 위에 있으면 어떤 문제가 생겨?
A. Props 전달이 늘고 Re-render 범위가 커지며 Component 재사용성이 낮아질 수 있다.

Q. State가 너무 아래에 있으면 어떤 문제가 생겨?
A. 형제 Component나 부모 Component가 같은 값을 공유하기 어려워져 중복 State가 생길 수 있다.

Q. 새 State를 만들기 전에 무엇을 확인해야 해?
A. State Type, Owner, Scope, Server State 여부, URL State 여부, Derived State 여부를 먼저 확인해야 한다.

Q. State Classification Checklist가 왜 필요해?
A. 불필요한 전역 상태, 중복 상태, Server State 혼동, Derived State 저장 문제를 줄이기 위해 필요하다.

Q. Frontend Agent는 State를 만들 때 어떤 순서로 판단해야 해?
A. State Classification, State Ownership, Scope, Tool Selection, Anti Pattern 검토 순서로 판단해야 한다.

Q. Part01의 핵심 목적은 뭐야?
A. React State를 무작정 전역화하지 않고 State Type, Owner, Scope 기준으로 적절한 위치를 판단하게 하는 것이다.

Q. Part01에서 도구 사용법을 깊게 다뤄?
A. 아니다. useState, Context, Zustand, Redux Toolkit, TanStack Query 선택 전에 필요한 분류와 소유자 판단 기준을 다룬다.

Q. Part01 다음에는 무엇을 다뤄야 해?
A. Context API와 useReducer, Zustand와 Redux Toolkit, TanStack Query, Form/Auth State, Debugging과 Anti Pattern으로 이어지는 것이 좋다.
