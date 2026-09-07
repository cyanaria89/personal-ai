# State Management Part06 - State Debugging and Anti Patterns

---

# 1. State Debugging Overview

## 1.1 State Debugging Purpose

### [개념]

State Debugging은 React Frontend에서 State 값, State Owner, 변경 경로, 렌더링 결과, Server State 동기화 여부를 추적하는 과정이다.

State 문제는 단순한 버그가 아니라 State Classification, Ownership, Tool Selection, Cache Invalidation이 잘못되어 발생하는 경우가 많다.

State Debugging의 목적은 문제가 되는 State의 Source of Truth를 찾고 중복 저장, stale data, 잘못된 owner, 불필요한 global state를 제거하는 것이다.

---

### [핵심]

State Debugging 핵심 대상:

- State Value
- State Owner
- State Writer
- State Reader
- Source of Truth
- Derived State
- Duplicate State
- Stale State
- Props Drilling
- Global Store Misuse
- Query Cache Mismatch
- Mutation Invalidation
- Logout Cleanup
- Re-render Issue

---

### [실무]

2026 실무 기준 State Debugging Flow:

```text
UI 문제 발생
→ 어떤 값이 잘못 보이는지 확인
→ 해당 값의 Source of Truth 확인
→ State Owner 확인
→ State Writer 확인
→ State Reader 확인
→ 중복 State 여부 확인
→ Derived State 여부 확인
→ Server State 여부 확인
→ Query Cache / Store / URL 동기화 확인
→ 수정 방향 결정
```

State Debugging 기본 원칙:

- 화면 증상보다 State Source of Truth를 먼저 찾는다.
- State가 몇 군데에 저장되어 있는지 확인한다.
- API 데이터는 Query Cache 기준으로 확인한다.
- URL State와 queryKey가 일치하는지 확인한다.
- Form 입력값은 Form 내부에서 관리되는지 확인한다.
- Auth 관련 값은 Store, Query Cache, Persistence를 함께 확인한다.
- 전역 Store 문제는 Store Boundary부터 확인한다.

---

### [FAQ]

Q. State Debugging은 뭐야?
A. 화면에 잘못 표시되는 값을 기준으로 State Owner, Source of Truth, 변경 경로, 중복 저장 여부를 추적하는 과정이다.

Q. State 문제가 생기면 어디부터 봐야 해?
A. 먼저 잘못된 값의 Source of Truth가 어디인지 확인해야 한다.

Q. State Debugging에서 가장 중요한 것은 뭐야?
A. 같은 의미의 값이 여러 State에 중복 저장되어 있는지 확인하는 것이다.

---

# 2. Source of Truth Debugging

## 2.1 Source of Truth Definition

### [개념]

Source of Truth는 특정 데이터의 기준이 되는 원본 위치다.

하나의 데이터는 하나의 기준 출처를 가져야 하며, 나머지 값은 그 원본에서 계산하거나 조회해야 한다.

---

### [핵심]

Source of Truth 후보:

- Component Local State
- Page Shared State
- URL Search Params
- Zustand Store
- Redux Store
- TanStack Query Cache
- Form Library State
- Backend Server
- Browser Storage
- Router State

---

### [실무]

Source of Truth 판단표:

| 데이터 예시                 | Source of Truth                |
| --------------------------- | ------------------------------ |
| input draft                 | Form Local State               |
| search keyword after submit | URL Search Params              |
| festival list               | TanStack Query Cache           |
| festival detail             | TanStack Query Cache           |
| selectedFestivalId          | Component State 또는 URL State |
| authenticated               | Auth Store                     |
| user profile detail         | TanStack Query Cache           |
| modal open                  | Local State 또는 UI Store      |
| theme                       | Context 또는 UI Store          |
| filteredItems               | Derived Value                  |
| totalPrice                  | Derived Value                  |
| token/session               | Security Storage Policy        |

Source of Truth Debug Flow:

```text
잘못된 값 발견
→ 이 값의 원본은 어디인가?
→ 같은 값이 다른 곳에도 저장되어 있는가?
→ 원본이 아닌 복사본을 화면에서 쓰고 있는가?
→ 원본 기준으로 읽도록 수정
```

---

### [FAQ]

Q. Source of Truth가 뭐야?
A. 특정 데이터의 기준이 되는 원본 State나 Cache 위치다.

Q. Source of Truth가 여러 개면 왜 문제야?
A. 한쪽만 갱신되면 화면마다 다른 값이 표시되는 데이터 불일치가 발생한다.

Q. API 데이터의 Source of Truth는 어디야?
A. Frontend에서는 TanStack Query Cache가 기준이 되고 실제 원본은 Backend Server다.

---

## 2.2 Source of Truth Violation

### [개념]

Source of Truth Violation은 하나의 데이터를 여러 State에 저장해 원본 기준이 깨지는 문제다.

Source of Truth가 깨지면 stale UI, 화면 불일치, reset 누락, mutation 후 미갱신 문제가 발생한다.

---

### [핵심]

위반 예:

- query data를 Zustand에 복사
- API list와 filteredList를 둘 다 State로 저장
- authenticated를 Store와 localStorage에 동시에 신뢰
- user profile을 Auth Store와 Query Cache에 중복 저장
- selectedId와 selectedItem을 둘 다 저장
- Form input을 Local State와 Global Store에 동시에 저장
- URL filter와 Store filter를 동시에 사용

---

### [실무]

위반 Debug Flow:

```text
같은 값이 여러 곳에 있음
→ 기준 Source of Truth 결정
→ 복사본 제거
→ Derived Value로 전환
→ Query Cache 기준으로 통일
→ URL State 기준으로 통일
→ Store reset 기준 작성
```

개선 예:

```text
문제:
festivalList가 Query Cache와 Zustand Store에 동시에 있음

해결:
festivalList는 Query Cache 기준
Zustand에는 UI State만 유지
mutation 후 Query invalidate
```

주의:

- 중복 저장이 반드시 금지는 아니지만 sync 기준이 없으면 위험하다.
- 인증 요약과 사용자 상세 정보처럼 의도적 분리는 가능하다.
- 의도적 중복에는 명확한 갱신 정책이 필요하다.
- Derived State는 저장하지 않는 것이 기본이다.

---

### [FAQ]

Q. Source of Truth Violation은 뭐야?
A. 하나의 데이터가 여러 State에 중복 저장되어 기준 원본이 불명확해지는 문제다.

Q. Query data를 Store에 복사하면 왜 위험해?
A. Query Cache와 Store가 서로 달라져 stale data와 화면 불일치가 생길 수 있다.

Q. 의도적으로 중복 저장해야 할 때는 어떻게 해?
A. 최소 필드만 중복하고 sync 기준, reset 기준, 갱신 기준을 명확히 해야 한다.

---

# 3. Duplicate State Problem

## 3.1 Duplicate State Definition

### [개념]

Duplicate State는 같은 의미의 값을 여러 State에 저장하는 문제다.

Duplicate State는 Source of Truth를 깨뜨리고 데이터 불일치를 만든다.

---

### [핵심]

Duplicate State 대표 사례:

- items + filteredItems
- selectedId + selectedItem
- firstName + lastName + fullName
- cartItems + totalPrice
- query data + store data
- URL keyword + store keyword
- auth user + profile query user
- form value + global store value

---

### [실무]

나쁜 예:

```tsx
const [items, setItems] = useState([]);
const [keyword, setKeyword] = useState("");
const [filteredItems, setFilteredItems] = useState([]);
```

좋은 예:

```tsx
const filteredItems = items.filter((item) => item.title.includes(keyword));
```

Duplicate State Debug Flow:

```text
잘못된 화면 값 발견
→ 원본 값과 복사 값 확인
→ 두 값의 업데이트 시점 비교
→ 계산 가능한 값인지 확인
→ 복사 State 제거
→ Derived Value로 변경
```

---

### [FAQ]

Q. Duplicate State가 뭐야?
A. 같은 의미의 값을 여러 State에 저장하는 문제다.

Q. Duplicate State가 왜 위험해?
A. 한쪽만 변경되면 다른 값과 불일치해 화면에 오래된 데이터가 표시될 수 있다.

Q. Duplicate State를 줄이는 방법은?
A. 하나의 Source of Truth만 남기고 계산 가능한 값은 Derived Value로 처리한다.

---

## 3.2 Duplicate State Review

### [개념]

Duplicate State Review는 코드 리뷰 시 중복 저장된 State를 찾아 제거하는 검수 과정이다.

Review Agent는 State 이름, 계산 가능 여부, Server State 복사 여부, URL State 중복 여부를 확인해야 한다.

---

### [핵심]

Review 대상:

- useState 중복
- Store field 중복
- Query data 복사
- URL Params와 Store 중복
- Form State와 Store 중복
- Derived State 저장
- Selector로 계산 가능한 값
- Mapping 결과 저장

---

### [실무]

Duplicate State Review Checklist:

```md
- [ ] 같은 의미의 값이 두 곳 이상에 저장되어 있지 않은가?
- [ ] 기존 State로 계산 가능한 값을 별도 State로 저장하지 않았는가?
- [ ] Query data를 Store에 복사하지 않았는가?
- [ ] URL Search Params와 Store filter가 중복되지 않는가?
- [ ] Form input을 Global Store에 중복 저장하지 않았는가?
- [ ] selectedId와 selectedItem을 동시에 저장하지 않았는가?
- [ ] Store field 중 Derived State가 없는가?
- [ ] selector 또는 useMemo로 대체 가능한가?
```

위험 신호:

```text
setFilteredItems
setTotalPrice
setFullName
setSelectedItem
setStoreFromQueryData
setKeywordFromUrlAndStore
```

---

### [FAQ]

Q. Duplicate State는 코드 리뷰에서 어떻게 찾아?
A. 같은 의미의 데이터가 useState, Store, Query Cache, URL에 반복 저장되어 있는지 확인한다.

Q. selectedItem을 State로 저장하면 안 돼?
A. selectedId와 원본 list로 계산 가능하면 selectedItem은 Derived Value로 처리하는 것이 좋다.

Q. filteredItems State가 보이면 무조건 문제야?
A. 원본 items와 filter 조건으로 계산 가능하면 대부분 Derived State이므로 저장하지 않는 것이 좋다.

---

# 4. Stale State Problem

## 4.1 Stale State Definition

### [개념]

Stale State는 현재 최신 상태가 아닌 오래된 값이 UI에 표시되는 문제다.

Stale State는 Server State cache, closure, mutation 후 invalidation 누락, Store 복사본, dependency 누락에서 자주 발생한다.

---

### [핵심]

Stale State 원인:

- Query invalidation 누락
- queryKey parameter 누락
- API data를 Store에 복사
- useEffect dependency 누락
- stale closure
- localStorage 오래된 값 복원
- Auth Store와 Query Cache 불일치
- mutation 후 list/detail 일부만 갱신

---

### [실무]

Stale State Debug Flow:

```text
화면에 오래된 값 표시
→ Network 응답 최신 여부 확인
→ Query Cache 최신 여부 확인
→ queryKey parameter 확인
→ Store 복사본 여부 확인
→ mutation invalidation 확인
→ useEffect dependency 확인
→ Persistence 값 확인
```

문제별 판단:

```text
mutation 후 이전 목록 표시
→ invalidateQueries 누락

검색 조건 변경 후 결과 그대로
→ queryKey parameter 누락

Profile 수정 후 Header 그대로
→ Auth Store와 Query Cache sync 누락

logout 후 이전 사용자 데이터 표시
→ Store reset 또는 Query Cache cleanup 누락
```

---

### [FAQ]

Q. Stale State가 뭐야?
A. 최신 상태가 아닌 오래된 값이 UI에 남아 표시되는 문제다.

Q. mutation 후 데이터가 안 바뀌면 뭘 확인해?
A. 관련 queryKey를 invalidate했는지, Query Cache를 직접 업데이트했는지 확인한다.

Q. 검색 조건이 바뀌었는데 결과가 그대로면?
A. queryKey에 keyword, filter, page 같은 조건이 포함되어 있는지 확인한다.

---

## 4.2 Stale Closure

### [개념]

Stale Closure는 함수가 생성될 당시의 오래된 State나 Props 값을 참조하는 문제다.

React Hook, event handler, timer, async callback에서 자주 발생한다.

---

### [핵심]

발생 위치:

- setInterval
- setTimeout
- async function
- event listener
- useEffect
- useCallback
- subscription
- WebSocket handler
- mutation callback

---

### [실무]

나쁜 예:

```tsx
const [count, setCount] = useState(0);

function increaseLater() {
  setTimeout(() => {
    setCount(count + 1);
  }, 1000);
}
```

개선 예:

```tsx
function increaseLater() {
  setTimeout(() => {
    setCount((prev) => prev + 1);
  }, 1000);
}
```

Debug Flow:

```text
Callback에서 오래된 값 사용
→ 함수 생성 시점 확인
→ dependency array 확인
→ functional update 검토
→ ref 사용 필요 여부 확인
```

주의:

- 이전 State 기반 업데이트는 functional update를 우선 검토한다.
- useEffect dependency를 임의로 제거하지 않는다.
- WebSocket handler는 최신 상태 참조 전략이 필요할 수 있다.
- async callback은 실행 시점과 State 변경 시점이 다를 수 있다.

---

### [FAQ]

Q. Stale Closure가 뭐야?
A. 함수가 생성될 당시의 오래된 State나 Props 값을 계속 참조하는 문제다.

Q. 이전 State 기반 setState는 어떻게 해야 해?
A. setState((prev) => nextValue) 형태의 functional update를 사용하는 것이 안전하다.

Q. useEffect dependency를 빼면 stale closure가 생길 수 있어?
A. 맞다. dependency를 누락하면 effect 내부에서 오래된 값을 참조할 수 있다.

---

# 5. Wrong State Owner

## 5.1 Wrong State Owner Definition

### [개념]

Wrong State Owner는 State를 실제로 읽고 변경하는 위치와 맞지 않는 Component 또는 Store가 State를 소유하는 문제다.

State Owner가 잘못되면 Props Drilling, 중복 State, 불필요한 Global Store, Re-render 증가가 발생한다.

---

### [핵심]

Wrong Owner 증상:

- 특정 Component만 쓰는 State가 App에 있음
- Form input이 Global Store에 있음
- Page 내부 filter가 전역 Store에 있음
- Server State가 Zustand Store에 있음
- URL에 있어야 할 검색 조건이 Local State에만 있음
- 형제 Component 공유가 필요한데 자식 Component에만 State가 있음
- Derived State가 별도 State로 저장됨

---

### [실무]

Wrong Owner Debug Flow:

```text
문제 State 식별
→ State Reader 확인
→ State Writer 확인
→ 가장 가까운 공통 부모 확인
→ Server State 여부 확인
→ URL State 여부 확인
→ Derived State 여부 확인
→ Owner 재배치
```

재배치 기준:

```text
단일 Component만 사용
→ Local State

형제 Component 공유
→ Closest Common Parent

여러 Page 공유
→ Global Store 검토

API 데이터
→ TanStack Query

검색 조건 공유/복원
→ URL State

계산 가능 값
→ Derived Value
```

---

### [FAQ]

Q. Wrong State Owner가 뭐야?
A. State를 실제 사용 범위와 맞지 않는 위치가 소유하는 문제다.

Q. State가 너무 위에 있으면 어떤 문제가 생겨?
A. Props 전달과 Re-render 범위가 늘고 Component 재사용성이 낮아질 수 있다.

Q. State가 너무 아래에 있으면 어떤 문제가 생겨?
A. 형제 Component와 공유하기 어려워 중복 State나 callback 복잡도가 생길 수 있다.

---

## 5.2 State Relocation Rules

### [개념]

State Relocation은 잘못된 위치에 있는 State를 적절한 Owner로 이동하는 리팩토링이다.

State를 이동할 때는 Local, Shared, Global, URL, Server, Derived 기준을 다시 적용해야 한다.

---

### [핵심]

Relocation 방향:

- Global → Local
- Global → URL
- Global → Query Cache
- Local → Shared Parent
- Local → URL
- Store → Derived Value
- Store → Form Local State
- Component State → Query Cache

---

### [실무]

Relocation 예:

```text
문제:
searchKeyword가 Zustand Store에 있음

판단:
검색 결과 공유와 새로고침 복원이 필요함

이동:
Zustand Store → URL Search Params

queryKey:
["festivals", { keyword, page }]
```

Relocation Checklist:

```md
- [ ] 이동 후 Source of Truth가 하나인가?
- [ ] 기존 복사 State를 제거했는가?
- [ ] Props 전달 구조가 명확한가?
- [ ] queryKey와 URL State가 일치하는가?
- [ ] Store reset 기준이 단순해졌는가?
- [ ] Derived State를 제거했는가?
- [ ] 테스트나 UI 동작이 유지되는가?
```

---

### [FAQ]

Q. State Relocation은 언제 해?
A. State Owner가 잘못되어 중복 State, Props Drilling, stale data, Store 비대화가 생길 때 한다.

Q. Global State를 Local State로 내려도 돼?
A. 사용 범위가 특정 Component로 제한된다면 Local State로 내리는 것이 좋다.

Q. Store에 있던 검색 조건은 어디로 옮겨?
A. 공유와 새로고침 복원이 필요하면 URL State로 옮기는 것이 적합하다.

---

# 6. Overused Global State

## 6.1 Overused Global State Definition

### [개념]

Overused Global State는 Local State, Shared State, URL State, Server State로 충분한 값을 전역 Store에 과도하게 저장하는 문제다.

Global Store는 편의 저장소가 아니라 앱 단위 Client State를 위한 제한적 도구다.

---

### [핵심]

남용 사례:

- 모든 input 값을 Store에 저장
- 모든 modal open 상태를 Store에 저장
- API list cache를 Store에 저장
- Page filter를 Store에 저장
- Derived State를 Store에 저장
- 단일 Component selected tab을 Store에 저장
- Form validation error를 Store에 저장

---

### [실무]

나쁜 Store 예:

```text
useAppStore
- user
- authenticated
- festivalList
- searchKeyword
- reviewFormContent
- filteredFestivalList
- modalOpen
- selectedTab
- totalPrice
```

개선 예:

```text
Auth Store
- user summary
- authenticated

TanStack Query
- festivalList

URL State
- searchKeyword

Form Local State
- reviewFormContent

Derived Value
- filteredFestivalList
- totalPrice

Local State
- modalOpen
- selectedTab
```

---

### [FAQ]

Q. Overused Global State가 뭐야?
A. 필요 범위가 좁은 상태까지 전역 Store에 넣는 문제다.

Q. 모든 State를 Store에 넣으면 왜 안 좋아?
A. Store가 비대해지고 reset, persistence, re-render, 데이터 흐름 추적 비용이 증가한다.

Q. Overused Global State를 줄이는 방법은?
A. State Classification을 다시 수행하고 Local, Shared, URL, Server, Derived State로 분리한다.

---

## 6.2 Global Store Slim Down

### [개념]

Global Store Slim Down은 비대해진 Store에서 불필요한 State를 제거하고 책임별 Store로 정리하는 작업이다.

Store를 줄이면 State Flow가 단순해지고 reset과 debugging이 쉬워진다.

---

### [핵심]

Slim Down 대상:

- Local UI State
- Form State
- Server State
- Derived State
- URL State
- Temporary Draft
- Sensitive Input
- One-page Filter
- Single Component State

---

### [실무]

Store Slim Down Flow:

```text
Store Field 목록화
→ 각 Field State Type 분류
→ Store에 남길 값 표시
→ Local State로 내릴 값 표시
→ Query Cache로 이동할 값 표시
→ URL State로 이동할 값 표시
→ Derived Value로 제거할 값 표시
→ reset / persist 재정리
```

분류 결과 예:

```text
남김:
authenticated
user summary
global toast
theme

제거:
festivalList → TanStack Query
searchKeyword → URL State
reviewFormContent → Form Local State
filteredFestivalList → Derived Value
modalOpen → Local State
```

주의:

- Store 제거 후 Component가 어디서 값을 읽는지 명확히 한다.
- Store action 제거 후 UI event handler를 정리한다.
- persist schema 변경을 고려한다.
- logout reset 대상이 줄어드는지 확인한다.

---

### [FAQ]

Q. Store Slim Down은 어떻게 시작해?
A. Store field를 전부 목록화하고 각 field의 State Type을 다시 분류한다.

Q. Store에서 제거한 값은 어디로 가?
A. Local State, URL State, Query Cache, Derived Value, Form Library 등 적절한 위치로 이동한다.

Q. Store를 줄이면 뭐가 좋아?
A. 데이터 흐름이 단순해지고 reset, persistence, debugging이 쉬워진다.

---

# 7. Props Drilling Troubleshooting

## 7.1 Props Drilling Definition

### [개념]

Props Drilling은 중간 Component가 직접 사용하지 않는 props를 하위 Component에 전달하기 위해 계속 넘기는 상황이다.

Props Drilling은 항상 문제는 아니며, 깊이와 반복성, Component 결합도를 기준으로 판단해야 한다.

---

### [핵심]

정상 범위:

- 1~2단계 Props 전달
- 명확한 부모-자식 관계
- Feature 내부 단순 전달
- 일회성 callback 전달

문제 신호:

- 4단계 이상 반복 전달
- 중간 Component가 props를 전혀 사용하지 않음
- 여러 branch로 같은 props 전달
- props 변경 시 많은 Component 수정
- Component 재사용성 저하
- callback chain이 복잡함

---

### [실무]

Props Drilling 판단 Flow:

```text
Props 전달 발생
→ 전달 깊이 확인
→ 중간 Component 사용 여부 확인
→ 같은 props 반복 전달 여부 확인
→ State Owner가 올바른지 확인
→ Component Composition 검토
→ Context / Store / URL State 검토
```

해결 후보:

```text
State Owner 조정
Component Composition
Context API
Zustand Store
Redux Toolkit
URL State
Custom Hook
```

주의:

- Props 전달 자체를 무조건 문제로 보지 않는다.
- Context나 Store 도입 전에 Component 구조를 먼저 검토한다.
- 전역 Store는 Props Drilling 해결의 기본값이 아니다.
- Server State라면 TanStack Query로 각 Component에서 조회할 수 있다.

---

### [FAQ]

Q. Props Drilling은 무조건 나쁜 거야?
A. 아니다. 1~2단계 명확한 Props 전달은 정상적인 React 패턴이다.

Q. Props Drilling이 문제인지 어떻게 판단해?
A. 전달 깊이, 반복성, 중간 Component의 미사용 여부, 변경 비용을 기준으로 판단한다.

Q. Props Drilling이 있으면 바로 Zustand를 써야 해?
A. 아니다. State Owner, Composition, Context, URL State를 먼저 검토한다.

---

## 7.2 Props Drilling Resolution

### [개념]

Props Drilling Resolution은 깊은 props 전달 문제를 적절한 구조로 해결하는 과정이다.

해결책은 항상 Global Store가 아니며, 문제 State의 종류에 따라 달라진다.

---

### [핵심]

해결 기준:

- 단순 하위 Tree 공유 → Context
- 여러 Page 전역 공유 → Global Store
- 검색 조건 공유 → URL State
- API Data → TanStack Query
- Component 구조 문제 → Composition
- 같은 로직 반복 → Custom Hook
- Form 입력 공유 → Form Shared State

---

### [실무]

해결 Flow:

```text
Props Drilling 확인
→ 전달되는 값의 State Type 확인
→ Server State인가?
→ URL State인가?
→ Tree 내부 공유인가?
→ 여러 Page 공유인가?
→ 가장 단순한 해결책 선택
```

예시:

```text
theme이 깊게 전달됨
→ Context 또는 UI Store

festivalDetail이 깊게 전달됨
→ TanStack Query detail query

searchKeyword가 깊게 전달됨
→ URL State

reviewFormValue가 깊게 전달됨
→ Form Owner 조정

global toast action이 깊게 전달됨
→ UI Store
```

---

### [FAQ]

Q. Props Drilling 해결책은 뭐가 있어?
A. Composition, Context, Global Store, URL State, TanStack Query, Custom Hook 등이 있다.

Q. API 데이터를 props로 깊게 넘기면 어떻게 해?
A. Server State라면 TanStack Query로 필요한 Component에서 query data를 사용할 수 있는지 검토한다.

Q. 검색 조건 props drilling은 어떻게 해결해?
A. 공유와 새로고침 복원이 필요하면 URL State로 관리하는 것이 적합하다.

---

# 8. Re-render Troubleshooting

## 8.1 Re-render Problem

### [개념]

Re-render Problem은 State 변경으로 인해 필요 이상으로 많은 Component가 다시 렌더링되는 문제다.

Re-render 자체는 React의 정상 동작이며, 문제가 되는 것은 불필요하고 비용이 큰 렌더링이다.

---

### [핵심]

Re-render 원인:

- State Owner가 너무 위에 있음
- Context value가 자주 변경됨
- Store 전체 구독
- 객체/배열 props 매번 새로 생성
- memoization 부재
- Derived 계산 비용 큼
- Parent Component에서 모든 State 관리
- Global Store 남용

---

### [실무]

Re-render Debug Flow:

```text
느린 UI 확인
→ 어떤 State 변경 시 느린지 확인
→ Re-render 범위 확인
→ State Owner 위치 확인
→ Context value 변경 확인
→ Store selector 사용 확인
→ Derived 계산 비용 확인
→ Memoization 필요 여부 확인
```

개선 후보:

```text
State를 더 낮은 Component로 이동
Context 분리
Zustand selector 사용
Redux selector 사용
React.memo 검토
useMemo 검토
useCallback 검토
Query select 검토
Component 분리
```

주의:

- 성능 최적화는 측정 후 적용한다.
- useMemo/useCallback을 무조건 적용하지 않는다.
- State 위치를 조정하는 것이 memoization보다 우선일 수 있다.
- Store 전체 구독을 피한다.

---

### [FAQ]

Q. Re-render는 무조건 나쁜 거야?
A. 아니다. React의 정상 동작이며, 문제가 되는 것은 불필요하고 비용이 큰 Re-render다.

Q. Re-render가 많으면 먼저 뭘 봐야 해?
A. State Owner가 너무 위에 있는지, Context value가 과도하게 큰지, Store 전체를 구독하는지 확인한다.

Q. useMemo를 무조건 쓰면 해결돼?
A. 아니다. State 구조와 구독 범위가 잘못되면 useMemo보다 구조 개선이 먼저다.

---

## 8.2 Store Subscription Re-render

### [개념]

Store Subscription Re-render는 Zustand나 Redux Store에서 Component가 필요 이상의 State를 구독해 불필요하게 렌더링되는 문제다.

Selector를 사용해 필요한 값만 구독하는 것이 중요하다.

---

### [핵심]

문제 원인:

- Zustand Store 전체 구독
- Redux selector가 너무 넓음
- 객체 selector가 매번 새 객체 반환
- Context value에 여러 State 혼합
- action만 필요한 Component가 state도 구독
- Derived selector가 매번 새 배열 반환

---

### [실무]

Zustand 나쁜 예:

```tsx
const authStore = useAuthStore();
```

Zustand 좋은 예:

```tsx
const authenticated = useAuthStore((state) => state.authenticated);
const logout = useAuthStore((state) => state.logout);
```

Redux 좋은 예:

```tsx
const authenticated = useAppSelector(selectAuthenticated);
```

Debug Flow:

```text
Store 변경 시 불필요한 렌더링 발생
→ Component 구독 값 확인
→ 전체 Store 구독 여부 확인
→ selector 범위 축소
→ 객체 selector 비교 전략 확인
→ Derived selector memoization 검토
```

---

### [FAQ]

Q. Store 구독 때문에 Re-render가 많으면 어떻게 해?
A. 필요한 값만 selector로 구독하고 Store 전체 구독을 피한다.

Q. Zustand에서 useStore() 전체 호출은 왜 주의해야 해?
A. Store의 다른 값이 바뀌어도 Component가 다시 렌더링될 수 있기 때문이다.

Q. Redux selector도 Re-render에 영향을 줘?
A. 맞다. selector가 매번 새 객체나 배열을 반환하면 불필요한 렌더링이 발생할 수 있다.

---

# 9. useEffect State Sync Anti Patterns

## 9.1 useEffect Sync Problem

### [개념]

useEffect Sync Problem은 props, query data, store data를 useEffect로 다른 State에 복사해 동기화하려는 문제다.

이 방식은 Duplicate State와 Stale State를 만들기 쉽다.

---

### [핵심]

문제 예:

- props를 local state에 복사
- query data를 local state에 복사
- query data를 store에 복사
- URL params를 store에 복사
- derived value를 effect로 setState
- form default value와 edit state 혼동

---

### [실무]

나쁜 예:

```tsx
const { data } = useQuery({
  queryKey: ["festival", festivalId],
  queryFn: () => getFestivalDetail(festivalId),
});

const [festival, setFestival] = useState(null);

useEffect(() => {
  setFestival(data);
}, [data]);
```

좋은 예:

```tsx
const { data: festival } = useQuery({
  queryKey: ["festival", festivalId],
  queryFn: () => getFestivalDetail(festivalId),
});
```

판단 기준:

```text
복사 목적이 화면 표시뿐인가?
→ 복사 금지, 원본 data 직접 사용

수정 Form draft가 필요한가?
→ 명확한 edit draft State로 분리

Derived 계산인가?
→ 렌더링 중 계산 또는 useMemo

Store 공유가 필요한가?
→ Source of Truth와 sync 기준 명확화
```

---

### [FAQ]

Q. useEffect로 query data를 local state에 복사해도 돼?
A. 화면 표시 목적이라면 권장하지 않는다. Query data를 직접 사용하는 것이 좋다.

Q. props를 State에 복사하면 왜 문제야?
A. props 변경과 local state 변경이 어긋나 중복 Source of Truth가 생길 수 있다.

Q. 수정 Form에서는 서버 데이터를 State로 복사해도 돼?
A. edit draft가 필요한 경우 가능하지만 원본 data와 draft state를 명확히 구분해야 한다.

---

## 9.2 Derived State useEffect Problem

### [개념]

Derived State useEffect Problem은 계산 가능한 값을 useEffect와 setState로 동기화하는 문제다.

Derived Value는 가능한 렌더링 중 계산하거나 selector/useMemo로 처리한다.

---

### [핵심]

문제 예:

- useEffect로 filteredItems 설정
- useEffect로 totalPrice 설정
- useEffect로 canSubmit 설정
- useEffect로 selectedItem 설정
- useEffect로 fullName 설정

---

### [실무]

나쁜 예:

```tsx
const [canSubmit, setCanSubmit] = useState(false);

useEffect(() => {
  setCanSubmit(email.length > 0 && password.length >= 8);
}, [email, password]);
```

좋은 예:

```tsx
const canSubmit =
  email.length > 0 && password.length >= 8 && !mutation.isPending;
```

판단 Flow:

```text
useEffect 내부에서 setState 발견
→ 기존 State로 계산 가능한가?
→ 가능하면 Derived Value로 변경
→ 계산 비용이 크면 useMemo 검토
```

주의:

- Derived State를 effect로 동기화하면 한 렌더링 늦게 반영될 수 있다.
- dependency 누락 시 stale value가 발생한다.
- 불필요한 effect는 코드 복잡도를 높인다.

---

### [FAQ]

Q. 계산 가능한 값을 useEffect로 setState하면 안 돼?
A. 대부분 권장하지 않는다. 렌더링 중 계산하거나 useMemo로 처리하는 것이 더 단순하다.

Q. canSubmit은 useEffect로 관리해야 해?
A. 아니다. email, password, error, mutation 상태로 계산 가능하면 Derived Value로 두는 것이 좋다.

Q. Derived State를 useEffect로 만들면 어떤 문제가 생겨?
A. dependency 누락, 한 박자 늦은 반영, 원본과 파생 값 불일치가 발생할 수 있다.

---

# 10. URL State Troubleshooting

## 10.1 URL State Mismatch

### [개념]

URL State Mismatch는 URL Search Params, Component State, Store State, queryKey가 서로 다른 값을 가지는 문제다.

검색, 필터, 페이지네이션 화면에서 자주 발생한다.

---

### [핵심]

문제 예:

- URL page와 Store page 불일치
- queryKey에 URL filter 누락
- Form draft와 applied query 혼동
- 뒤로가기 시 화면 값 미복원
- 새로고침 후 filter 초기화
- URL에는 keyword가 있지만 input은 빈 값
- Store filter가 URL보다 우선 적용됨

---

### [실무]

Debug Flow:

```text
검색/필터 화면 문제 발생
→ URL Search Params 확인
→ Component draft state 확인
→ queryKey params 확인
→ queryFn params 확인
→ Store filter 중복 여부 확인
→ 뒤로가기 동작 확인
```

권장 구조:

```text
Form Draft State
→ 입력 중 임시값

URL Search Params
→ 적용된 검색 조건

queryKey
→ URL Search Params 기반

Query Data
→ Server State 결과
```

주의:

- URL State와 Store State를 동시에 Source of Truth로 두지 않는다.
- URL 값은 문자열이므로 타입 변환이 필요하다.
- page 값은 숫자로 변환한다.
- 검색 조건 변경 시 page reset을 검토한다.

---

### [FAQ]

Q. URL에는 keyword가 있는데 input이 비어 있으면 뭘 확인해?
A. URL Search Params에서 Form 초기값을 세팅하는 기준이 있는지 확인한다.

Q. 검색 결과가 URL 조건과 다르면 뭘 확인해?
A. queryKey와 queryFn parameter가 URL Search Params를 기준으로 만들어지는지 확인한다.

Q. 검색 조건을 URL과 Store에 둘 다 저장해도 돼?
A. 권장하지 않는다. URL State를 Source of Truth로 두는 것이 더 단순하다.

---

## 10.2 Page Reset Problem

### [개념]

Page Reset Problem은 검색 조건이나 필터가 변경되었는데 page 번호가 이전 값으로 남아 잘못된 결과를 조회하는 문제다.

검색 조건 변경 시 page를 1로 초기화하는 것이 일반적이다.

---

### [핵심]

발생 상황:

- keyword 변경
- filter 변경
- sort 변경
- category 변경
- date range 변경
- page query 유지
- server page out of range

---

### [실무]

문제 예:

```text
현재 URL:
/festivals?keyword=old&page=5

새 검색어 submit:
keyword=new

잘못된 결과:
/festivals?keyword=new&page=5

권장:
/festivals?keyword=new&page=1
```

Page Reset Flow:

```text
검색 조건 변경
→ page=1로 설정
→ URL Search Params 업데이트
→ queryKey 변경
→ Server State refetch
```

주의:

- page 이동만 하는 경우 page를 유지한다.
- 검색 조건 변경과 page 변경을 구분한다.
- sort 변경 시 page reset 여부를 정책으로 정한다.
- 서버 응답이 빈 결과면 page out of range도 의심한다.

---

### [FAQ]

Q. 검색 조건이 바뀌면 page를 왜 1로 돌려?
A. 이전 조건의 page 번호가 새 조건에서는 유효하지 않을 수 있기 때문이다.

Q. sort만 바뀌어도 page reset이 필요해?
A. 보통 reset을 검토하지만 프로젝트 UX 정책에 따라 결정한다.

Q. page out of range는 어떻게 처리해?
A. 빈 결과와 현재 page를 확인하고 필요하면 page를 1로 되돌리거나 마지막 page로 조정한다.

---

# 11. TanStack Query Troubleshooting

## 11.1 Query Key Troubleshooting

### [개념]

Query Key Troubleshooting은 queryKey가 API 요청 조건을 정확히 반영하는지 확인하는 과정이다.

queryKey가 잘못되면 캐시 재사용, refetch, invalidation이 모두 잘못 동작할 수 있다.

---

### [핵심]

확인 대상:

- queryKey domain
- id parameter
- filter parameter
- page parameter
- sort parameter
- userId parameter
- locale parameter
- enabled condition
- queryFn parameter consistency

---

### [실무]

Debug Flow:

```text
데이터가 예상과 다름
→ queryFn이 사용하는 parameter 확인
→ queryKey에 같은 parameter 포함 여부 확인
→ queryKey domain naming 확인
→ Query Devtools에서 key 확인
→ invalidation key와 일치 확인
```

나쁜 예:

```tsx
useQuery({
  queryKey: ["reviews"],
  queryFn: () => getReviews(festivalId),
});
```

좋은 예:

```tsx
useQuery({
  queryKey: ["reviews", festivalId],
  queryFn: () => getReviews(festivalId),
});
```

---

### [FAQ]

Q. queryKey 문제는 어떤 증상으로 나타나?
A. 검색 조건이 바뀌어도 데이터가 그대로이거나 다른 상세 데이터가 섞여 보일 수 있다.

Q. queryFn에서 사용하는 값은 queryKey에도 넣어야 해?
A. 맞다. queryFn 결과를 바꾸는 값은 queryKey에도 포함해야 한다.

Q. queryKey 디버깅은 어떻게 해?
A. Query Devtools에서 실제 생성된 queryKey와 Cache 상태를 확인한다.

---

## 11.2 Mutation Invalidation Troubleshooting

### [개념]

Mutation Invalidation Troubleshooting은 서버 상태 변경 후 관련 Query Cache가 올바르게 갱신되는지 확인하는 과정이다.

mutation 성공 후 화면이 바뀌지 않으면 invalidation 누락을 우선 의심한다.

---

### [핵심]

확인 대상:

- mutationFn 성공 여부
- onSuccess 실행 여부
- invalidateQueries 대상
- list queryKey
- detail queryKey
- summary queryKey
- count queryKey
- user-specific query
- Query Devtools stale status

---

### [실무]

Debug Flow:

```text
mutation 성공
→ Network 응답 확인
→ onSuccess 실행 확인
→ invalidateQueries queryKey 확인
→ Query Devtools에서 stale/refetch 확인
→ list/detail/summary cache 확인
→ UI가 query data를 쓰는지 확인
```

예:

```text
리뷰 작성 후 리뷰 목록 그대로
→ ["reviews", festivalId] invalidate 확인

리뷰 작성 후 평점 요약 그대로
→ ["festival", festivalId] invalidate 확인

좋아요 후 목록 카드 count 그대로
→ ["festivals", params] invalidate 확인
```

주의:

- mutation은 성공했지만 UI가 Store 복사본을 보고 있을 수 있다.
- invalidate key가 queryKey와 정확히 맞는지 확인한다.
- 너무 넓은 invalidate는 불필요한 refetch를 만든다.
- 너무 좁은 invalidate는 stale UI를 남긴다.

---

### [FAQ]

Q. mutation 후 화면이 안 바뀌면 뭘 확인해?
A. onSuccess에서 관련 queryKey를 invalidate했는지 확인한다.

Q. invalidateQueries를 했는데도 안 바뀌면?
A. UI가 Query data가 아니라 Store 복사본을 사용하고 있는지 확인한다.

Q. mutation 후 list와 detail을 둘 다 갱신해야 해?
A. 변경 영향이 list와 detail 모두에 있으면 둘 다 invalidate해야 할 수 있다.

---

# 12. Form State Troubleshooting

## 12.1 Form Reset Problem

### [개념]

Form Reset Problem은 제출 성공, modal close, page 이동, logout 이후 Form 입력값이 예상대로 초기화되지 않는 문제다.

Form Reset 기준은 Form 종류와 UX 정책에 따라 다르다.

---

### [핵심]

Reset 필요 상황:

- submit success
- modal close
- cancel edit
- logout
- account switch
- route leave
- wizard restart
- draft discard
- server data reload

---

### [실무]

Debug Flow:

```text
Form 값이 남아 있음
→ Form State 위치 확인
→ Local State인지 Store인지 확인
→ submit success reset 여부 확인
→ modal close reset 여부 확인
→ Form Library reset 호출 여부 확인
→ persisted draft cleanup 확인
```

Reset 기준 예:

```text
리뷰 작성 성공
→ Form reset

프로필 수정 성공
→ 최신 서버 데이터 반영

검색 Form submit
→ draft 유지 가능

로그아웃
→ 민감 Form draft cleanup

modal close
→ 작성 취소면 reset
```

주의:

- 실패 시 입력값을 임의로 reset하지 않는다.
- 수정 Form은 서버 최신값과 draft 초기값을 구분한다.
- persisted draft는 cleanup 정책이 필요하다.
- Form State가 Store에 있으면 reset 누락 위험이 커진다.

---

### [FAQ]

Q. submit 실패 시 Form을 reset해야 해?
A. 보통 아니다. 사용자가 수정 후 재시도할 수 있도록 입력값을 유지하는 것이 좋다.

Q. submit 성공 후 Form을 reset해야 해?
A. 작성 Form은 reset하는 경우가 많고 수정 Form은 최신 서버 데이터 반영 정책을 따른다.

Q. Form 값이 계속 남아 있으면 뭘 확인해?
A. Form State 위치, reset 호출, Form Library reset, Store reset, persisted draft cleanup을 확인한다.

---

## 12.2 Form Error State Problem

### [개념]

Form Error State Problem은 client validation error, server validation error, network error, auth error를 구분하지 않아 잘못된 메시지를 표시하는 문제다.

Error Type을 분류해야 사용자에게 적절한 UI를 제공할 수 있다.

---

### [핵심]

Error State 유형:

- Field Error
- Form-level Error
- Client Validation Error
- Server Validation Error
- Network Error
- Auth Error
- Permission Error
- Unknown Error

---

### [실무]

Debug Flow:

```text
Form Error 표시 문제
→ Client Validation인지 확인
→ Server Validation인지 확인
→ Field Error인지 확인
→ Form-level Error인지 확인
→ Auth Error인지 확인
→ Network Error인지 확인
→ Error Message Mapping 확인
```

처리 기준:

```text
Field validation error
→ input 근처 표시

Form-level submit error
→ Form 상단 표시

Network error
→ 재시도 안내

Auth error
→ Auth Flow 연결

Permission error
→ 권한 부족 안내
```

주의:

- 모든 오류를 toast로만 처리하지 않는다.
- 서버 원문 오류를 그대로 노출하지 않는다.
- Field Error는 field name mapping 기준이 필요하다.
- Error State는 submit 재시도 시 정리해야 한다.

---

### [FAQ]

Q. Form Error가 이상하게 표시되면 뭘 확인해?
A. Error Type, fieldErrors 구조, message mapping, Form-level Error와 Field Error 구분을 확인한다.

Q. 모든 Form Error를 한 곳에 표시해도 돼?
A. 가능하지만 Field Error는 해당 input 근처에 표시하는 것이 더 적합하다.

Q. 서버 validation error와 network error는 같아?
A. 아니다. 서버 validation error는 입력값 수정이 필요하고 network error는 재시도 안내가 필요하다.

---

# 13. Auth State Troubleshooting

## 13.1 Auth Initialization Problem

### [개념]

Auth Initialization Problem은 App 시작 시 인증 확인이 끝나기 전에 잘못된 Route redirect나 UI 깜빡임이 발생하는 문제다.

initialized, loading, authenticated 상태를 분리해야 안정적인 Auth UX를 만들 수 있다.

---

### [핵심]

문제 증상:

- 새로고침 시 login page로 순간 이동
- Protected Page가 잠깐 보였다가 사라짐
- authenticated false로 먼저 판단
- token 검증 전 redirect
- Current User Query 실패 처리 누락
- initialized 상태 없음

---

### [실무]

Debug Flow:

```text
새로고침 Auth 문제 발생
→ initialized 상태 존재 여부 확인
→ auth loading 처리 확인
→ Current User Query 확인
→ Protected Route 조건 확인
→ token 검증 전 redirect 여부 확인
→ 실패 시 clearAuth 기준 확인
```

권장 Route 판단:

```text
initialized === false
→ Loading UI

initialized === true && authenticated === false
→ Login Redirect

initialized === true && authenticated === true
→ Protected Content
```

주의:

- token 존재만으로 authenticated를 확정하지 않는다.
- initialized 전 redirect를 실행하지 않는다.
- Current User Query retry 정책을 확인한다.
- Auth Error와 일반 Error를 구분한다.

---

### [FAQ]

Q. 새로고침 때 로그인 페이지로 깜빡이면 뭘 확인해?
A. Auth initialized 상태와 Protected Route가 인증 확인 전 redirect하지 않는지 확인한다.

Q. initialized가 왜 필요해?
A. 인증 확인이 끝났는지 구분해 잘못된 redirect와 화면 깜빡임을 막기 위해 필요하다.

Q. token이 있으면 바로 authenticated true로 해도 돼?
A. UX상 임시 처리는 가능하지만 서버 검증이나 Current User Query로 확정하는 것이 안전하다.

---

## 13.2 Logout Cleanup Problem

### [개념]

Logout Cleanup Problem은 logout 후 Auth Store만 초기화하고 사용자별 Store, Query Cache, Persistence, WebSocket을 정리하지 않는 문제다.

이전 사용자 데이터가 남으면 보안과 UX 문제가 발생한다.

---

### [핵심]

Cleanup 대상:

- Auth Store
- Notification Store
- User-Specific Store
- Query Cache
- Persisted Storage
- Form Draft
- WebSocket Connection
- Subscription
- Private Route State

---

### [실무]

Debug Flow:

```text
logout 후 이전 데이터 표시
→ Auth Store reset 확인
→ user-specific Store reset 확인
→ Query Cache cleanup 확인
→ persisted storage 확인
→ WebSocket disconnect 확인
→ account switch 시 재현 확인
```

Logout Cleanup Flow:

```text
Logout
→ token cleanup
→ Auth Store reset
→ User-Specific Store reset
→ Query Cache remove/clear
→ persisted sensitive data cleanup
→ WebSocket disconnect
→ redirect
```

주의:

- Auth Store만 reset하면 부족할 수 있다.
- public query cache는 유지할지 제거할지 정책을 정한다.
- userId가 queryKey에 포함되면 사용자별 cache 분리에 도움이 된다.
- account switch는 logout보다 더 엄격히 검수한다.

---

### [FAQ]

Q. logout 후 이전 사용자 정보가 보이면 뭘 확인해?
A. Auth Store reset, user-specific Store reset, Query Cache cleanup, persisted storage를 확인한다.

Q. logout 때 queryClient.clear를 써도 돼?
A. 가능하지만 public cache도 제거되므로 프로젝트 정책에 따라 removeQueries와 비교해 선택한다.

Q. WebSocket도 logout 때 정리해야 해?
A. 사용자별 실시간 연결이면 disconnect 또는 unsubscribe가 필요하다.

---

# 14. Persistence Troubleshooting

## 14.1 Persisted State Problem

### [개념]

Persisted State Problem은 localStorage, sessionStorage, persisted Store에 오래된 값이나 민감정보가 남아 UI와 보안 문제가 발생하는 상황이다.

Persistence는 편의 기능이지만 cleanup과 scope 관리가 필요하다.

---

### [핵심]

문제 예:

- 이전 theme 아닌 오래된 layout 복원
- logout 후 user data 남음
- auth flag만 보고 로그인 처리
- 오래된 filter가 계속 적용됨
- toast 상태가 새로고침 후 표시됨
- 민감 Form Draft 저장
- token cleanup 누락

---

### [실무]

Persist Debug Flow:

```text
새로고침 후 이상한 상태 표시
→ localStorage 확인
→ sessionStorage 확인
→ Zustand persist 확인
→ Redux persist 확인
→ partialize 대상 확인
→ version/migration 확인
→ logout cleanup 확인
```

Persist Review 기준:

```text
비민감 설정인가?
→ persist 가능

URL State가 더 적합한가?
→ URL로 이동

Server State인가?
→ Query Cache 기준

임시 UI State인가?
→ persist 금지

민감정보인가?
→ persist 금지
```

---

### [FAQ]

Q. 새로고침 후 이상한 값이 계속 남으면 뭘 확인해?
A. localStorage, sessionStorage, persisted Store, persist partialize 대상을 확인한다.

Q. toast나 loading도 persist해야 해?
A. 보통 아니다. 임시 UI State는 새로고침 후 유지할 필요가 없다.

Q. persist된 auth flag를 믿어도 돼?
A. 안 된다. 저장된 값은 검증 전 임시 정보일 뿐이며 서버 검증이 필요하다.

---

## 14.2 Persist Cleanup Rules

### [개념]

Persist Cleanup은 logout, account switch, schema change, feature 종료 시 persisted 값을 제거하거나 갱신하는 규칙이다.

Persisted State는 메모리 State보다 오래 남기 때문에 cleanup 기준이 더 중요하다.

---

### [핵심]

Cleanup 트리거:

- logout
- account switch
- token expired
- refresh failed
- user deleted
- role changed
- app version changed
- schema version changed
- sensitive flow ended

---

### [실무]

Cleanup Flow:

```text
Cleanup Event 발생
→ 사용자별 persisted data 확인
→ 민감 persisted data 확인
→ remove 또는 reset
→ Store memory state reset
→ Query Cache cleanup
→ redirect 또는 reload 정책 적용
```

주의:

- persist key naming을 명확히 한다.
- 사용자별 persist data는 namespace를 검토한다.
- version migration 전략을 둔다.
- 민감정보는 persist 대상에서 제외한다.
- cleanup 누락은 account switch에서 특히 위험하다.

---

### [FAQ]

Q. Persist cleanup은 언제 해?
A. logout, account switch, token expired, schema 변경, 민감 flow 종료 시 검토한다.

Q. persisted Store reset과 메모리 Store reset은 달라?
A. 다를 수 있다. 메모리 State만 reset해도 storage에 값이 남아 다시 복원될 수 있다.

Q. 사용자별 persist data는 어떻게 관리해?
A. userId namespace를 쓰거나 logout/account switch 시 제거하는 정책을 둔다.

---

# 15. State Tool Mismatch

## 15.1 Wrong Tool Selection

### [개념]

Wrong Tool Selection은 State Type과 맞지 않는 도구를 선택하는 문제다.

도구 선택은 State Classification 이후에 해야 하며, 도구를 먼저 정하면 과도한 구조나 stale data가 생길 수 있다.

---

### [핵심]

Mismatch 예:

- API Data → Zustand
- API Data → Redux Slice
- modal open → TanStack Query
- input value → Global Store
- search params → Local State only
- derived total → Store
- auth detail profile → Auth Store
- server validation error → Global Error Store
- page filter → App Global Store

---

### [실무]

Tool Correction Table:

| 잘못된 선택                     | 올바른 후보      |
| ------------------------------- | ---------------- |
| API list in Zustand             | TanStack Query   |
| Search keyword in Store         | URL State        |
| Review content in Redux         | Form Local State |
| filteredItems in State          | Derived Value    |
| modal open in Query             | Local UI State   |
| auth user detail in Store       | Query Cache      |
| page number in Store            | URL State        |
| global toast in Local deep prop | UI Store         |

Tool Selection Flow:

```text
State 발견
→ State Type 분류
→ Owner 결정
→ Scope 결정
→ Tool 후보 선택
→ Anti Pattern 검토
```

---

### [FAQ]

Q. Wrong Tool Selection은 뭐야?
A. State 성격과 맞지 않는 상태관리 도구를 선택하는 문제다.

Q. API 데이터는 어떤 도구가 적합해?
A. 대부분 TanStack Query 같은 Server State 도구가 적합하다.

Q. 검색 조건은 어떤 도구가 적합해?
A. 공유와 새로고침 복원이 필요하면 URL State가 적합하다.

---

## 15.2 Tool Selection Review

### [개념]

Tool Selection Review는 구현된 State가 적절한 도구를 사용하고 있는지 검수하는 과정이다.

Review Agent는 도구보다 State Type을 먼저 확인해야 한다.

---

### [핵심]

Review 기준:

- State Type
- State Owner
- State Scope
- Server Ownership
- URL Restore
- Form Scope
- Auth Scope
- Derived 여부
- Persistence 필요성
- Reset 필요성

---

### [실무]

Review Checklist:

```md
- [ ] API Data를 Server State 도구로 관리하는가?
- [ ] Local UI State를 전역화하지 않았는가?
- [ ] 검색 조건을 URL State로 관리해야 하지 않는가?
- [ ] Form input을 Global Store에 넣지 않았는가?
- [ ] Derived State를 저장하지 않았는가?
- [ ] Auth Summary와 User Profile을 분리했는가?
- [ ] Global Store가 필요한 범위인가?
- [ ] Context value가 너무 크지 않은가?
- [ ] queryKey가 조건을 포함하는가?
- [ ] Persist 대상이 안전한가?
```

결과 예:

```text
festivalList in Redux
→ Server State
→ TanStack Query로 이동 권장

keyword in Zustand
→ URL 복원 필요
→ URL Search Params 권장

password in authStore
→ 민감 Form State
→ LoginForm Local State 권장
```

---

### [FAQ]

Q. Tool Selection Review에서 가장 먼저 볼 것은?
A. 어떤 도구를 썼는지가 아니라 해당 값의 State Type이 무엇인지 먼저 봐야 한다.

Q. Global Store를 썼다고 무조건 문제야?
A. 아니다. 여러 Page에서 필요한 Client State라면 적합할 수 있다.

Q. TanStack Query를 썼다고 모든 API 문제가 해결돼?
A. 아니다. queryKey, invalidation, loading/error/empty 처리가 올바른지 검토해야 한다.

---

# 16. State Debugging Tools

## 16.1 React DevTools

### [개념]

React DevTools는 Component Tree, props, hooks state, render 관계를 확인하는 도구다.

Local State, Props Drilling, Component Re-render, Context Provider 위치 확인에 유용하다.

---

### [핵심]

확인 대상:

- Component Tree
- Props
- Hooks State
- Context Provider
- Context Consumer
- Component Re-render
- State Owner
- Component Boundary

---

### [실무]

React DevTools 활용 Flow:

```text
UI 값 문제 발생
→ 해당 Component 선택
→ props 확인
→ hooks state 확인
→ 부모 Component 확인
→ Context Provider 확인
→ State Owner 위치 확인
```

활용 상황:

```text
Local State 값 확인
Props Drilling 확인
Context value 확인
State Owner 위치 확인
Re-render Component 확인
```

주의:

- React DevTools는 Server State Cache 자체를 모두 보여주지는 않는다.
- Query 문제는 TanStack Query Devtools와 함께 확인한다.
- Store 문제는 Redux DevTools 또는 Zustand Devtools를 함께 확인한다.

---

### [FAQ]

Q. React DevTools는 언제 써?
A. Component props, local state, hooks state, Context Provider, Re-render를 확인할 때 사용한다.

Q. React DevTools로 queryKey도 볼 수 있어?
A. 직접적인 Query Cache 확인은 TanStack Query Devtools가 더 적합하다.

Q. Props Drilling 확인에도 도움이 돼?
A. 맞다. Component Tree와 props 전달 흐름을 확인할 수 있다.

---

## 16.2 TanStack Query Devtools

### [개념]

TanStack Query Devtools는 Query Cache, queryKey, query status, stale/fresh 상태, refetch 여부를 확인하는 도구다.

Server State 문제를 디버깅할 때 핵심 도구다.

---

### [핵심]

확인 대상:

- queryKey
- cached data
- query status
- stale status
- observers
- last updated
- refetch
- inactive query
- mutation result
- error state

---

### [실무]

Query Devtools 활용 Flow:

```text
Server State 문제 발생
→ queryKey 확인
→ cached data 확인
→ stale/fresh 상태 확인
→ refetch 발생 여부 확인
→ invalidation 후 상태 확인
→ inactive cache 확인
```

활용 상황:

```text
검색 조건 변경 시 queryKey 변경 확인
mutation 후 invalidation 확인
logout 후 user-specific cache 제거 확인
staleTime 동작 확인
cache data와 화면 data 비교
```

주의:

- Devtools data와 화면 data가 다르면 Store 복사본 사용을 의심한다.
- Network 탭과 함께 확인한다.
- 운영 환경 노출 여부를 관리한다.

---

### [FAQ]

Q. TanStack Query Devtools는 언제 써?
A. queryKey, cache data, stale 상태, invalidation 동작을 확인할 때 사용한다.

Q. Devtools cache는 최신인데 화면은 오래된 값이면?
A. 화면이 Query data가 아니라 Store 복사본이나 Local State를 보고 있을 수 있다.

Q. mutation 후 Devtools에서 뭘 봐야 해?
A. 관련 query가 stale 처리되었는지, refetch되었는지, cache data가 갱신되었는지 확인한다.

---

## 16.3 Redux and Zustand Devtools

### [개념]

Redux and Zustand Devtools는 Global Store의 State 값, action 호출, 변경 흐름을 확인하는 도구다.

Global Store 문제는 Store 값과 action 흐름을 함께 확인해야 한다.

---

### [핵심]

확인 대상:

- current store value
- dispatched action
- action payload
- state diff
- reset action
- persist state
- selector result
- store boundary
- user-specific cleanup

---

### [실무]

Debug Flow:

```text
Global Store 문제 발생
→ Store 값 확인
→ Action 호출 여부 확인
→ Action payload 확인
→ State 변경 결과 확인
→ reset action 여부 확인
→ persist 값 확인
→ Query Cache와 중복 여부 확인
```

활용 상황:

```text
logout 후 authStore 값 확인
toast action 호출 확인
notification unread count reset 확인
Redux action history 확인
Zustand persist 값 확인
```

주의:

- Store 값이 맞는데 화면이 틀리면 selector와 props를 확인한다.
- Store 값이 틀리면 action 호출 위치를 확인한다.
- API 데이터가 Store에 있으면 Server State 분리 여부를 검토한다.

---

### [FAQ]

Q. Redux DevTools는 무엇을 확인할 때 좋아?
A. dispatch된 action, payload, state diff, action history를 확인할 때 좋다.

Q. Zustand 상태 문제는 어떻게 확인해?
A. Store 값, action 호출 위치, selector 사용, persist 값을 확인한다.

Q. Store 값은 맞는데 화면이 틀리면?
A. selector, Component props, Derived 계산, Local State 복사본을 확인해야 한다.

---

# 17. State Anti Pattern Catalog

## 17.1 Common State Anti Patterns

### [개념]

State Anti Pattern Catalog는 React 상태관리에서 자주 발생하는 문제 패턴을 정리한 목록이다.

Frontend Agent와 Review Agent는 코드 생성과 검수 시 이 Catalog를 기준으로 위험 신호를 탐지해야 한다.

---

### [핵심]

주요 Anti Pattern:

- Overused Global State
- Duplicate State
- Derived State Stored
- Server State in Store
- Query Data Copy to Store
- Missing Query Key Parameter
- Under Invalidation
- Over Invalidation
- Wrong State Owner
- Form State in Global Store
- Auth State Overtrust
- Props Drilling Overreaction
- useEffect Sync Misuse
- Stale Closure
- Persist Sensitive Data
- Logout Cleanup Missing

---

### [실무]

Anti Pattern Detection Flow:

```text
State Code Review
→ State Type 확인
→ Owner 확인
→ Tool 확인
→ 중복 저장 확인
→ Server State 복사 확인
→ Derived 저장 확인
→ reset / cleanup 확인
→ Query invalidation 확인
→ Persistence 보안 확인
```

위험 신호 키워드:

```text
setFiltered
setTotal
setFullName
setStoreFromQuery
useEffect setState from props
useEffect setState from query data
localStorage token
password in store
festivalList in store
queryKey ["list"]
auth flag persisted
```

---

### [FAQ]

Q. State Anti Pattern은 뭐야?
A. 유지보수성, 동기화, 성능, 보안 문제를 만드는 잘못된 State 관리 패턴이다.

Q. 가장 흔한 Anti Pattern은 뭐야?
A. 전역 상태 남용, 중복 State, Server State를 Store에 저장하는 문제가 흔하다.

Q. Anti Pattern은 어떻게 탐지해?
A. State Type, Owner, Source of Truth, Tool Selection, reset/invalidation 기준을 순서대로 확인한다.

---

## 17.2 Anti Pattern Fix Strategy

### [개념]

Anti Pattern Fix Strategy는 발견된 State 문제를 안전하게 수정하는 절차다.

수정은 도구 교체보다 Source of Truth 정리와 State 위치 재배치를 우선해야 한다.

---

### [핵심]

Fix 우선순위:

- Source of Truth 결정
- Duplicate State 제거
- Derived Value 전환
- Server State Query Cache 이동
- URL State 이동
- Form State Local 이동
- Store Boundary 정리
- Invalidation 추가
- Reset Cleanup 추가
- Persistence 제거

---

### [실무]

Fix Flow:

```text
Anti Pattern 발견
→ 영향 범위 확인
→ Source of Truth 결정
→ 중복 State 제거
→ 필요한 위치로 State 이동
→ UI 읽기 경로 수정
→ mutation/invalidation 수정
→ reset/cleanup 수정
→ 회귀 검수
```

수정 예:

```text
문제:
reviewFormContent가 Redux Store에 있음

수정:
ReviewForm Local State로 이동
submit 시 mutation payload로 전달
submit success 시 reset
Redux field 제거
```

주의:

- State 이동 후 기존 action과 selector를 정리한다.
- Query data를 Store에서 제거하면 UI가 Query data를 직접 사용하도록 변경한다.
- URL State 이동 시 뒤로가기/새로고침 동작을 확인한다.
- Auth cleanup 수정 시 account switch도 검수한다.

---

### [FAQ]

Q. State Anti Pattern을 고칠 때 가장 먼저 할 일은?
A. 해당 데이터의 Source of Truth를 하나로 정하는 것이다.

Q. 도구를 바꾸면 Anti Pattern이 해결돼?
A. 도구만 바꿔서는 부족하다. State Type, Owner, Source of Truth가 올바르게 정리되어야 한다.

Q. 수정 후 무엇을 확인해야 해?
A. 화면 값, reset, invalidation, persistence, account switch, URL 복원 동작을 확인해야 한다.

---

# 18. State Review Checklist

## 18.1 State Debugging Checklist

### [개념]

State Debugging Checklist는 UI 상태 문제가 발생했을 때 원인을 추적하기 위한 공통 점검 목록이다.

Agent는 문제 증상만 보고 답을 만들지 말고 State Source와 변경 흐름을 확인해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] 잘못 표시되는 값이 무엇인가?
- [ ] 해당 값의 Source of Truth는 어디인가?
- [ ] 같은 값이 여러 State에 중복 저장되어 있지 않은가?
- [ ] State Owner가 실제 사용 범위와 맞는가?
- [ ] Derived State를 저장하고 있지 않은가?
- [ ] Server State를 Store에 복사하지 않았는가?
- [ ] queryKey에 필요한 parameter가 포함되었는가?
- [ ] mutation 후 invalidation이 수행되는가?
- [ ] URL State와 queryKey가 일치하는가?
- [ ] useEffect로 불필요한 State sync를 하지 않는가?
- [ ] stale closure 가능성이 없는가?
- [ ] Form State가 Global Store에 있지 않은가?
- [ ] Auth State와 Query Cache sync 기준이 있는가?
- [ ] logout/account switch cleanup이 있는가?
- [ ] persist된 오래된 값이 문제를 만들지 않는가?
```

---

### [실무]

Debugging Output Template:

```md
## 문제 State

- name:
- current value:
- expected value:

## Source of Truth

- current:
- recommended:

## 원인 후보

- Duplicate State:
- Wrong Owner:
- Server State Copy:
- Missing Invalidation:
- Missing Query Key Parameter:
- Persistence Issue:

## 수정 방향

- relocate state:
- remove duplicate:
- update queryKey:
- add invalidation:
- add cleanup:
```

---

### [FAQ]

Q. State Debugging Checklist는 언제 써?
A. 화면 값이 이상하거나 상태가 갱신되지 않거나 logout 후 이전 데이터가 남을 때 사용한다.

Q. Checklist에서 가장 중요한 항목은 뭐야?
A. Source of Truth와 중복 State 여부 확인이다.

Q. Agent가 State 문제를 분석할 때 어떤 형식이 좋아?
A. 문제 State, Source of Truth, 원인 후보, 수정 방향을 분리해 출력하는 것이 좋다.

---

## 18.2 State Code Review Checklist

### [개념]

State Code Review Checklist는 React 상태관리 코드가 Domain Rules에 맞게 작성되었는지 검수하는 기준이다.

Review Agent는 State 생성, Store 설계, Query 사용, Form/Auth 처리, Persistence, Cleanup을 함께 검토해야 한다.

---

### [핵심]

Checklist:

```md
- [ ] State Classification이 명확한가?
- [ ] Local / Shared / Global 기준이 적절한가?
- [ ] Client State와 Server State가 분리되었는가?
- [ ] State Owner가 가장 가까운 적절한 위치인가?
- [ ] Global Store가 필요한 State만 포함하는가?
- [ ] Context value가 비대하지 않은가?
- [ ] Zustand/Redux selector를 적절히 사용하는가?
- [ ] TanStack Query queryKey가 정확한가?
- [ ] API data를 Store에 중복 저장하지 않는가?
- [ ] Derived State를 저장하지 않는가?
- [ ] Form State가 전역화되지 않았는가?
- [ ] Auth State를 보안 기준으로 과신하지 않는가?
- [ ] logout cleanup이 충분한가?
- [ ] Persistence에 민감정보가 없는가?
- [ ] Error / Loading / Empty 상태가 분리되었는가?
```

---

### [실무]

Review Output Template:

```md
## State Review Result

### 문제 없음

- item:

### 개선 필요

- issue:
- reason:
- recommended fix:

### 치명적 문제

- issue:
- impact:
- required fix:

### 확인 필요

- question:
- related file:
```

치명적 문제 후보:

```text
password in Store
access token unsafe persist
API data duplicated in Store without sync
logout cleanup missing
queryKey missing id/filter/page
Backend 권한 없이 Frontend role만 신뢰
```

---

### [FAQ]

Q. State Code Review에서 가장 먼저 볼 것은?
A. State Classification과 Source of Truth가 명확한지 확인해야 한다.

Q. 치명적 문제로 봐야 하는 것은?
A. 민감정보 Store 저장, Server State 중복 저장, logout cleanup 누락, queryKey parameter 누락, Frontend 권한 과신이다.

Q. Review 결과는 어떻게 출력하는 것이 좋아?
A. 문제 없음, 개선 필요, 치명적 문제, 확인 필요를 분리해 출력하는 것이 좋다.

---

# 19. Troubleshooting Decision Table

## 19.1 Symptom Based Debugging

### [개념]

Symptom Based Debugging은 화면 증상별로 어떤 State 문제를 의심해야 하는지 정리하는 방식이다.

증상에서 바로 결론을 내리지 말고 관련 State 흐름을 확인해야 한다.

---

### [핵심]

증상별 원인 후보:

| 증상                              | 원인 후보                              |
| --------------------------------- | -------------------------------------- |
| mutation 후 화면이 안 바뀜        | invalidation 누락, Store 복사본 사용   |
| 검색 조건 변경 후 결과 그대로     | queryKey parameter 누락                |
| 새로고침 후 필터 초기화           | URL State 미사용                       |
| 뒤로가기 시 검색 조건 복원 안 됨  | URL State 미사용                       |
| logout 후 이전 사용자 데이터 표시 | Store reset / Query Cache cleanup 누락 |
| Header nickname만 안 바뀜         | Auth Store와 Query Cache sync 누락     |
| Form 제출 후 값이 남음            | reset 누락, Store Form State           |
| 입력값이 갑자기 초기화됨          | 잘못된 key, remount, reset 과다        |
| 화면마다 다른 값 표시             | Duplicate State                        |
| 렌더링이 너무 많음                | State Owner 과상위, Store 전체 구독    |
| modal 상태가 꼬임                 | Local/Global Owner 혼동                |
| totalPrice가 틀림                 | Derived State 중복 저장                |

---

### [실무]

Symptom Debug Flow:

```text
증상 식별
→ 관련 State 후보 목록화
→ Source of Truth 확인
→ Tool Selection 확인
→ Sync / Invalidation / Reset 확인
→ 수정 방향 도출
```

예:

```text
증상:
좋아요 클릭 후 버튼은 바뀌지만 목록 count는 그대로

원인 후보:
- detail cache만 update
- list query invalidation 누락
- list가 Store 복사본 사용

수정:
- list queryKey invalidate
- Store 복사본 제거
```

---

### [FAQ]

Q. 화면 증상만 보고 원인을 확정해도 돼?
A. 아니다. 증상은 후보를 좁히는 용도이고 Source of Truth와 State 흐름을 확인해야 한다.

Q. mutation 후 화면이 안 바뀌면 가장 먼저 뭘 봐?
A. invalidation 누락과 UI가 Query data가 아닌 Store 복사본을 보고 있는지 확인한다.

Q. 화면마다 값이 다르면 무엇을 의심해?
A. Duplicate State 또는 Source of Truth Violation을 의심한다.

---

## 19.2 State Fix Decision Table

### [개념]

State Fix Decision Table은 발견된 문제 State를 어디로 이동하거나 어떻게 수정할지 결정하는 기준표다.

수정 방향은 State Type에 따라 달라진다.

---

### [핵심]

Fix Decision Table:

| 문제 State                       | 수정 방향                                 |
| -------------------------------- | ----------------------------------------- |
| 단일 Component UI State in Store | Local State로 이동                        |
| Form input in Store              | Form Local State 또는 Form Library로 이동 |
| API data in Store                | TanStack Query로 이동                     |
| search/filter in Store           | URL State로 이동                          |
| filtered list in State           | Derived Value로 변경                      |
| selected item object in State    | selectedId만 저장                         |
| auth detail in Store             | User Profile Query로 이동                 |
| persisted sensitive data         | persist 제거                              |
| missing invalidation             | 관련 queryKey invalidate                  |
| missing queryKey param           | queryKey에 parameter 추가                 |
| too wide Context                 | Context 분리 또는 Store 검토              |
| Store 전체 구독                  | selector 사용                             |

---

### [실무]

Fix Flow:

```text
문제 State Type 확인
→ Decision Table 매칭
→ Source of Truth 결정
→ State 이동 또는 제거
→ 읽기 경로 수정
→ reset / invalidation / persistence 검수
```

예:

```text
문제:
festivalList in Redux Slice

Fix:
festivalList는 Server State
→ Redux에서 제거
→ useQuery로 조회
→ mutation 후 invalidate
→ Component는 query data 사용
```

---

### [FAQ]

Q. 문제 State는 어떻게 고칠 방향을 정해?
A. State Type을 먼저 분류하고 Decision Table에 따라 적절한 위치로 이동한다.

Q. API data in Store는 어떻게 고쳐?
A. TanStack Query로 이동하고 Store 복사본을 제거한 뒤 queryKey와 invalidation을 설계한다.

Q. search filter in Store는 어떻게 고쳐?
A. 공유와 새로고침 복원이 필요하면 URL Search Params로 이동한다.

---

# 20. Part06 Final Review

## 20.1 Part06 Scope Summary

### [개념]

Part06은 State Debugging, Source of Truth, Duplicate State, Stale State, Wrong Owner, Overused Global State, Props Drilling, Re-render, Query/Form/Auth/Persistence Troubleshooting, Anti Pattern Review를 다룬다.

이 문서는 State Management 문서 전체의 검수 기준으로 사용된다.

---

### [핵심]

Part06 포함 범위:

- State Debugging Purpose
- Source of Truth Debugging
- Duplicate State Problem
- Stale State Problem
- Stale Closure
- Wrong State Owner
- State Relocation
- Overused Global State
- Global Store Slim Down
- Props Drilling Troubleshooting
- Re-render Troubleshooting
- useEffect Sync Anti Pattern
- URL State Troubleshooting
- TanStack Query Troubleshooting
- Form State Troubleshooting
- Auth State Troubleshooting
- Persistence Troubleshooting
- Wrong Tool Selection
- State Debugging Tools
- State Anti Pattern Catalog
- State Review Checklist
- Troubleshooting Decision Table

---

### [실무]

Part06 문서 연결:

```text
Part01 State Classification and Ownership
→ State Type / Owner 기준

Part02 Context API and useReducer
→ Context / useReducer 문제 검수

Part03 Zustand and Redux Toolkit
→ Global Store 문제 검수

Part04 TanStack Query and Server State
→ Server State / Query Cache 문제 검수

Part05 Form State and Auth State
→ Form / Auth 문제 검수

Part06 State Debugging and Anti Patterns
→ 전체 상태관리 문제 분석 및 리뷰 기준
```

Agent 사용 기준:

```text
User State Bug Report
→ Part06으로 증상 기반 원인 후보 도출
→ Part01로 State Type 재확인
→ 관련 Part02~05로 도구별 수정안 연결
→ 치명적 문제 여부 검토
→ 수정 방향 출력
```

---

### [FAQ]

Q. Part06의 핵심 목적은 뭐야?
A. React State 문제가 발생했을 때 Source of Truth, State Owner, 중복 저장, stale data, 잘못된 도구 선택을 기준으로 원인을 찾게 하는 것이다.

Q. Part06은 구현 문서야 검수 문서야?
A. 주로 Debugging과 Review 기준 문서다. 구현보다 문제 분석과 Anti Pattern 탐지에 집중한다.

Q. Part06 이후 State Management 문서 세트는 어떻게 사용해?
A. Part01로 분류하고, Part02~05로 도구별 구현 기준을 확인하며, Part06으로 문제 분석과 코드 리뷰를 수행한다.

---

# Retrieval Queries

### [FAQ]

Q. State Debugging은 뭐야?
A. 화면에 잘못 표시되는 값을 기준으로 State Owner, Source of Truth, 변경 경로, 중복 저장 여부를 추적하는 과정이다.

Q. State 문제가 생기면 어디부터 봐야 해?
A. 먼저 잘못된 값의 Source of Truth가 어디인지 확인해야 한다.

Q. State Debugging에서 가장 중요한 것은 뭐야?
A. 같은 의미의 값이 여러 State에 중복 저장되어 있는지 확인하는 것이다.

Q. Source of Truth가 뭐야?
A. 특정 데이터의 기준이 되는 원본 State나 Cache 위치다.

Q. Source of Truth가 여러 개면 왜 문제야?
A. 한쪽만 갱신되면 화면마다 다른 값이 표시되는 데이터 불일치가 발생한다.

Q. API 데이터의 Source of Truth는 어디야?
A. Frontend에서는 TanStack Query Cache가 기준이 되고 실제 원본은 Backend Server다.

Q. Source of Truth Violation은 뭐야?
A. 하나의 데이터가 여러 State에 중복 저장되어 기준 원본이 불명확해지는 문제다.

Q. Query data를 Store에 복사하면 왜 위험해?
A. Query Cache와 Store가 서로 달라져 stale data와 화면 불일치가 생길 수 있다.

Q. 의도적으로 중복 저장해야 할 때는 어떻게 해?
A. 최소 필드만 중복하고 sync 기준, reset 기준, 갱신 기준을 명확히 해야 한다.

Q. Duplicate State가 뭐야?
A. 같은 의미의 값을 여러 State에 저장하는 문제다.

Q. Duplicate State가 왜 위험해?
A. 한쪽만 변경되면 다른 값과 불일치해 화면에 오래된 데이터가 표시될 수 있다.

Q. Duplicate State를 줄이는 방법은?
A. 하나의 Source of Truth만 남기고 계산 가능한 값은 Derived Value로 처리한다.

Q. Duplicate State는 코드 리뷰에서 어떻게 찾아?
A. 같은 의미의 데이터가 useState, Store, Query Cache, URL에 반복 저장되어 있는지 확인한다.

Q. selectedItem을 State로 저장하면 안 돼?
A. selectedId와 원본 list로 계산 가능하면 selectedItem은 Derived Value로 처리하는 것이 좋다.

Q. filteredItems State가 보이면 무조건 문제야?
A. 원본 items와 filter 조건으로 계산 가능하면 대부분 Derived State이므로 저장하지 않는 것이 좋다.

Q. Stale State가 뭐야?
A. 최신 상태가 아닌 오래된 값이 UI에 남아 표시되는 문제다.

Q. mutation 후 데이터가 안 바뀌면 뭘 확인해?
A. 관련 queryKey를 invalidate했는지, Query Cache를 직접 업데이트했는지 확인한다.

Q. 검색 조건이 바뀌었는데 결과가 그대로면?
A. queryKey에 keyword, filter, page 같은 조건이 포함되어 있는지 확인한다.

Q. Stale Closure가 뭐야?
A. 함수가 생성될 당시의 오래된 State나 Props 값을 계속 참조하는 문제다.

Q. 이전 State 기반 setState는 어떻게 해야 해?
A. setState((prev) => nextValue) 형태의 functional update를 사용하는 것이 안전하다.

Q. useEffect dependency를 빼면 stale closure가 생길 수 있어?
A. 맞다. dependency를 누락하면 effect 내부에서 오래된 값을 참조할 수 있다.

Q. Wrong State Owner가 뭐야?
A. State를 실제 사용 범위와 맞지 않는 위치가 소유하는 문제다.

Q. State가 너무 위에 있으면 어떤 문제가 생겨?
A. Props 전달과 Re-render 범위가 늘고 Component 재사용성이 낮아질 수 있다.

Q. State가 너무 아래에 있으면 어떤 문제가 생겨?
A. 형제 Component와 공유하기 어려워 중복 State나 callback 복잡도가 생길 수 있다.

Q. State Relocation은 언제 해?
A. State Owner가 잘못되어 중복 State, Props Drilling, stale data, Store 비대화가 생길 때 한다.

Q. Global State를 Local State로 내려도 돼?
A. 사용 범위가 특정 Component로 제한된다면 Local State로 내리는 것이 좋다.

Q. Store에 있던 검색 조건은 어디로 옮겨?
A. 공유와 새로고침 복원이 필요하면 URL State로 옮기는 것이 적합하다.

Q. Overused Global State가 뭐야?
A. 필요 범위가 좁은 상태까지 전역 Store에 넣는 문제다.

Q. 모든 State를 Store에 넣으면 왜 안 좋아?
A. Store가 비대해지고 reset, persistence, re-render, 데이터 흐름 추적 비용이 증가한다.

Q. Overused Global State를 줄이는 방법은?
A. State Classification을 다시 수행하고 Local, Shared, URL, Server, Derived State로 분리한다.

Q. Store Slim Down은 어떻게 시작해?
A. Store field를 전부 목록화하고 각 field의 State Type을 다시 분류한다.

Q. Store에서 제거한 값은 어디로 가?
A. Local State, URL State, Query Cache, Derived Value, Form Library 등 적절한 위치로 이동한다.

Q. Store를 줄이면 뭐가 좋아?
A. 데이터 흐름이 단순해지고 reset, persistence, debugging이 쉬워진다.

Q. Props Drilling은 무조건 나쁜 거야?
A. 아니다. 1~2단계 명확한 Props 전달은 정상적인 React 패턴이다.

Q. Props Drilling이 문제인지 어떻게 판단해?
A. 전달 깊이, 반복성, 중간 Component의 미사용 여부, 변경 비용을 기준으로 판단한다.

Q. Props Drilling이 있으면 바로 Zustand를 써야 해?
A. 아니다. State Owner, Composition, Context, URL State를 먼저 검토한다.

Q. Props Drilling 해결책은 뭐가 있어?
A. Composition, Context, Global Store, URL State, TanStack Query, Custom Hook 등이 있다.

Q. API 데이터를 props로 깊게 넘기면 어떻게 해?
A. Server State라면 TanStack Query로 필요한 Component에서 query data를 사용할 수 있는지 검토한다.

Q. 검색 조건 props drilling은 어떻게 해결해?
A. 공유와 새로고침 복원이 필요하면 URL State로 관리하는 것이 적합하다.

Q. Re-render는 무조건 나쁜 거야?
A. 아니다. React의 정상 동작이며, 문제가 되는 것은 불필요하고 비용이 큰 Re-render다.

Q. Re-render가 많으면 먼저 뭘 봐야 해?
A. State Owner가 너무 위에 있는지, Context value가 과도하게 큰지, Store 전체를 구독하는지 확인한다.

Q. useMemo를 무조건 쓰면 해결돼?
A. 아니다. State 구조와 구독 범위가 잘못되면 useMemo보다 구조 개선이 먼저다.

Q. Store 구독 때문에 Re-render가 많으면 어떻게 해?
A. 필요한 값만 selector로 구독하고 Store 전체 구독을 피한다.

Q. Zustand에서 useStore() 전체 호출은 왜 주의해야 해?
A. Store의 다른 값이 바뀌어도 Component가 다시 렌더링될 수 있기 때문이다.

Q. Redux selector도 Re-render에 영향을 줘?
A. 맞다. selector가 매번 새 객체나 배열을 반환하면 불필요한 렌더링이 발생할 수 있다.

Q. useEffect로 query data를 local state에 복사해도 돼?
A. 화면 표시 목적이라면 권장하지 않는다. Query data를 직접 사용하는 것이 좋다.

Q. props를 State에 복사하면 왜 문제야?
A. props 변경과 local state 변경이 어긋나 중복 Source of Truth가 생길 수 있다.

Q. 수정 Form에서는 서버 데이터를 State로 복사해도 돼?
A. edit draft가 필요한 경우 가능하지만 원본 data와 draft state를 명확히 구분해야 한다.

Q. 계산 가능한 값을 useEffect로 setState하면 안 돼?
A. 대부분 권장하지 않는다. 렌더링 중 계산하거나 useMemo로 처리하는 것이 더 단순하다.

Q. canSubmit은 useEffect로 관리해야 해?
A. 아니다. email, password, error, mutation 상태로 계산 가능하면 Derived Value로 두는 것이 좋다.

Q. Derived State를 useEffect로 만들면 어떤 문제가 생겨?
A. dependency 누락, 한 박자 늦은 반영, 원본과 파생 값 불일치가 발생할 수 있다.

Q. URL에는 keyword가 있는데 input이 비어 있으면 뭘 확인해?
A. URL Search Params에서 Form 초기값을 세팅하는 기준이 있는지 확인한다.

Q. 검색 결과가 URL 조건과 다르면 뭘 확인해?
A. queryKey와 queryFn parameter가 URL Search Params를 기준으로 만들어지는지 확인한다.

Q. 검색 조건을 URL과 Store에 둘 다 저장해도 돼?
A. 권장하지 않는다. URL State를 Source of Truth로 두는 것이 더 단순하다.

Q. 검색 조건이 바뀌면 page를 왜 1로 돌려?
A. 이전 조건의 page 번호가 새 조건에서는 유효하지 않을 수 있기 때문이다.

Q. sort만 바뀌어도 page reset이 필요해?
A. 보통 reset을 검토하지만 프로젝트 UX 정책에 따라 결정한다.

Q. page out of range는 어떻게 처리해?
A. 빈 결과와 현재 page를 확인하고 필요하면 page를 1로 되돌리거나 마지막 page로 조정한다.

Q. queryKey 문제는 어떤 증상으로 나타나?
A. 검색 조건이 바뀌어도 데이터가 그대로이거나 다른 상세 데이터가 섞여 보일 수 있다.

Q. queryFn에서 사용하는 값은 queryKey에도 넣어야 해?
A. 맞다. queryFn 결과를 바꾸는 값은 queryKey에도 포함해야 한다.

Q. queryKey 디버깅은 어떻게 해?
A. Query Devtools에서 실제 생성된 queryKey와 Cache 상태를 확인한다.

Q. mutation 후 화면이 안 바뀌면 뭘 확인해?
A. onSuccess에서 관련 queryKey를 invalidate했는지 확인한다.

Q. invalidateQueries를 했는데도 안 바뀌면?
A. UI가 Query data가 아니라 Store 복사본을 사용하고 있는지 확인한다.

Q. mutation 후 list와 detail을 둘 다 갱신해야 해?
A. 변경 영향이 list와 detail 모두에 있으면 둘 다 invalidate해야 할 수 있다.

Q. submit 실패 시 Form을 reset해야 해?
A. 보통 아니다. 사용자가 수정 후 재시도할 수 있도록 입력값을 유지하는 것이 좋다.

Q. submit 성공 후 Form을 reset해야 해?
A. 작성 Form은 reset하는 경우가 많고 수정 Form은 최신 서버 데이터 반영 정책을 따른다.

Q. Form 값이 계속 남아 있으면 뭘 확인해?
A. Form State 위치, reset 호출, Form Library reset, Store reset, persisted draft cleanup을 확인한다.

Q. Form Error가 이상하게 표시되면 뭘 확인해?
A. Error Type, fieldErrors 구조, message mapping, Form-level Error와 Field Error 구분을 확인한다.

Q. 모든 Form Error를 한 곳에 표시해도 돼?
A. 가능하지만 Field Error는 해당 input 근처에 표시하는 것이 더 적합하다.

Q. 서버 validation error와 network error는 같아?
A. 아니다. 서버 validation error는 입력값 수정이 필요하고 network error는 재시도 안내가 필요하다.

Q. 새로고침 때 로그인 페이지로 깜빡이면 뭘 확인해?
A. Auth initialized 상태와 Protected Route가 인증 확인 전 redirect하지 않는지 확인한다.

Q. initialized가 왜 필요해?
A. 인증 확인이 끝났는지 구분해 잘못된 redirect와 화면 깜빡임을 막기 위해 필요하다.

Q. token이 있으면 바로 authenticated true로 해도 돼?
A. UX상 임시 처리는 가능하지만 서버 검증이나 Current User Query로 확정하는 것이 안전하다.

Q. logout 후 이전 사용자 정보가 보이면 뭘 확인해?
A. Auth Store reset, user-specific Store reset, Query Cache cleanup, persisted storage를 확인한다.

Q. logout 때 queryClient.clear를 써도 돼?
A. 가능하지만 public cache도 제거되므로 프로젝트 정책에 따라 removeQueries와 비교해 선택한다.

Q. WebSocket도 logout 때 정리해야 해?
A. 사용자별 실시간 연결이면 disconnect 또는 unsubscribe가 필요하다.

Q. 새로고침 후 이상한 값이 계속 남으면 뭘 확인해?
A. localStorage, sessionStorage, persisted Store, persist partialize 대상을 확인한다.

Q. toast나 loading도 persist해야 해?
A. 보통 아니다. 임시 UI State는 새로고침 후 유지할 필요가 없다.

Q. persist된 auth flag를 믿어도 돼?
A. 안 된다. 저장된 값은 검증 전 임시 정보일 뿐이며 서버 검증이 필요하다.

Q. Persist cleanup은 언제 해?
A. logout, account switch, token expired, schema 변경, 민감 flow 종료 시 검토한다.

Q. persisted Store reset과 메모리 Store reset은 달라?
A. 다를 수 있다. 메모리 State만 reset해도 storage에 값이 남아 다시 복원될 수 있다.

Q. 사용자별 persist data는 어떻게 관리해?
A. userId namespace를 쓰거나 logout/account switch 시 제거하는 정책을 둔다.

Q. Wrong Tool Selection은 뭐야?
A. State 성격과 맞지 않는 상태관리 도구를 선택하는 문제다.

Q. API 데이터는 어떤 도구가 적합해?
A. 대부분 TanStack Query 같은 Server State 도구가 적합하다.

Q. 검색 조건은 어떤 도구가 적합해?
A. 공유와 새로고침 복원이 필요하면 URL State가 적합하다.

Q. Tool Selection Review에서 가장 먼저 볼 것은?
A. 어떤 도구를 썼는지가 아니라 해당 값의 State Type이 무엇인지 먼저 봐야 한다.

Q. Global Store를 썼다고 무조건 문제야?
A. 아니다. 여러 Page에서 필요한 Client State라면 적합할 수 있다.

Q. TanStack Query를 썼다고 모든 API 문제가 해결돼?
A. 아니다. queryKey, invalidation, loading/error/empty 처리가 올바른지 검토해야 한다.

Q. React DevTools는 언제 써?
A. Component props, local state, hooks state, Context Provider, Re-render를 확인할 때 사용한다.

Q. React DevTools로 queryKey도 볼 수 있어?
A. 직접적인 Query Cache 확인은 TanStack Query Devtools가 더 적합하다.

Q. Props Drilling 확인에도 도움이 돼?
A. 맞다. Component Tree와 props 전달 흐름을 확인할 수 있다.

Q. TanStack Query Devtools는 언제 써?
A. queryKey, cache data, stale 상태, invalidation 동작을 확인할 때 사용한다.

Q. Devtools cache는 최신인데 화면은 오래된 값이면?
A. 화면이 Query data가 아니라 Store 복사본이나 Local State를 보고 있을 수 있다.

Q. mutation 후 Devtools에서 뭘 봐야 해?
A. 관련 query가 stale 처리되었는지, refetch되었는지, cache data가 갱신되었는지 확인한다.

Q. Redux DevTools는 무엇을 확인할 때 좋아?
A. dispatch된 action, payload, state diff, action history를 확인할 때 좋다.

Q. Zustand 상태 문제는 어떻게 확인해?
A. Store 값, action 호출 위치, selector 사용, persist 값을 확인한다.

Q. Store 값은 맞는데 화면이 틀리면?
A. selector, Component props, Derived 계산, Local State 복사본을 확인해야 한다.

Q. State Anti Pattern은 뭐야?
A. 유지보수성, 동기화, 성능, 보안 문제를 만드는 잘못된 State 관리 패턴이다.

Q. 가장 흔한 Anti Pattern은 뭐야?
A. 전역 상태 남용, 중복 State, Server State를 Store에 저장하는 문제가 흔하다.

Q. Anti Pattern은 어떻게 탐지해?
A. State Type, Owner, Source of Truth, Tool Selection, reset/invalidation 기준을 순서대로 확인한다.

Q. State Anti Pattern을 고칠 때 가장 먼저 할 일은?
A. 해당 데이터의 Source of Truth를 하나로 정하는 것이다.

Q. 도구를 바꾸면 Anti Pattern이 해결돼?
A. 도구만 바꿔서는 부족하다. State Type, Owner, Source of Truth가 올바르게 정리되어야 한다.

Q. 수정 후 무엇을 확인해야 해?
A. 화면 값, reset, invalidation, persistence, account switch, URL 복원 동작을 확인해야 한다.

Q. State Debugging Checklist는 언제 써?
A. 화면 값이 이상하거나 상태가 갱신되지 않거나 logout 후 이전 데이터가 남을 때 사용한다.

Q. Checklist에서 가장 중요한 항목은 뭐야?
A. Source of Truth와 중복 State 여부 확인이다.

Q. Agent가 State 문제를 분석할 때 어떤 형식이 좋아?
A. 문제 State, Source of Truth, 원인 후보, 수정 방향을 분리해 출력하는 것이 좋다.

Q. State Code Review에서 가장 먼저 볼 것은?
A. State Classification과 Source of Truth가 명확한지 확인해야 한다.

Q. 치명적 문제로 봐야 하는 것은?
A. 민감정보 Store 저장, Server State 중복 저장, logout cleanup 누락, queryKey parameter 누락, Frontend 권한 과신이다.

Q. Review 결과는 어떻게 출력하는 것이 좋아?
A. 문제 없음, 개선 필요, 치명적 문제, 확인 필요를 분리해 출력하는 것이 좋다.

Q. 화면 증상만 보고 원인을 확정해도 돼?
A. 아니다. 증상은 후보를 좁히는 용도이고 Source of Truth와 State 흐름을 확인해야 한다.

Q. mutation 후 화면이 안 바뀌면 가장 먼저 뭘 봐?
A. invalidation 누락과 UI가 Query data가 아닌 Store 복사본을 보고 있는지 확인한다.

Q. 화면마다 값이 다르면 무엇을 의심해?
A. Duplicate State 또는 Source of Truth Violation을 의심한다.

Q. 문제 State는 어떻게 고칠 방향을 정해?
A. State Type을 먼저 분류하고 Decision Table에 따라 적절한 위치로 이동한다.

Q. API data in Store는 어떻게 고쳐?
A. TanStack Query로 이동하고 Store 복사본을 제거한 뒤 queryKey와 invalidation을 설계한다.

Q. search filter in Store는 어떻게 고쳐?
A. 공유와 새로고침 복원이 필요하면 URL Search Params로 이동한다.

Q. Part06의 핵심 목적은 뭐야?
A. React State 문제가 발생했을 때 Source of Truth, State Owner, 중복 저장, stale data, 잘못된 도구 선택을 기준으로 원인을 찾게 하는 것이다.

Q. Part06은 구현 문서야 검수 문서야?
A. 주로 Debugging과 Review 기준 문서다. 구현보다 문제 분석과 Anti Pattern 탐지에 집중한다.

Q. Part06 이후 State Management 문서 세트는 어떻게 사용해?
A. Part01로 분류하고, Part02~05로 도구별 구현 기준을 확인하며, Part06으로 문제 분석과 코드 리뷰를 수행한다.
