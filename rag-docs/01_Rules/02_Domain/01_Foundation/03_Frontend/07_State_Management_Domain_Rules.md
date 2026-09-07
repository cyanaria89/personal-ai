# State Management Domain Rules

---

# 1. Domain Purpose

## 1.1 Purpose

### [개념]

State Management Domain 문서는 Frontend Agent / Review Agent / PM Agent용 RAG 문서 제작 규칙이다.

목적:

- Frontend State 종류 구분 지원
- Local State / Shared State / Global State 판단 기준 제공
- Server State와 Client State 구분 지원
- React useState / useReducer / Context 사용 기준 제공
- Zustand / Redux Toolkit / TanStack Query 같은 도구 선택 기준 제공
- State Ownership 설계 지원
- Props Drilling 문제 분석 지원
- Form State / UI State / Auth State / Cache State 분리 기준 제공
- 유지보수 가능한 상태 구조 설계 지원
- State Management Anti Pattern 검출 지원

---

### [핵심]

우선순위:

1. State Classification
2. Local State
3. Shared State
4. Global State
5. Server State
6. State Ownership
7. Lifting State Up
8. Props Drilling
9. Context API
10. useReducer
11. Zustand
12. Redux Toolkit
13. TanStack Query
14. Auth State
15. Form State
16. Cache State
17. State Anti Pattern

---

### [실무]

2026 실무 기준에서 State Management 문서는 단순 전역 상태 라이브러리 사용법 문서가 아니다.

Frontend Agent가 아래 작업을 수행할 수 있도록 작성한다.

- 상태 종류 분류
- 상태 위치 결정
- Local State 유지 여부 판단
- Props Drilling 개선 여부 판단
- Context 적용 여부 판단
- 전역 상태 라이브러리 도입 여부 판단
- Server State와 Client State 분리
- API 데이터 캐싱 전략 판단
- 인증 상태 흐름 설계
- Form 상태 관리 기준 제공
- 불필요한 전역 상태화 감지
- 상태 중복 저장 문제 감지
- 유지보수 가능한 상태 흐름 설계

---

### [FAQ]

Q. State Management 문서는 React Core와 뭐가 달라?

A.
React Core는 useState와 기본 상태 사용법이고 State Management는 상태를 어디에 두고 어떤 도구로 관리할지 설계하는 문서다.

Q. State Management에서 가장 중요한 기준은 뭐야?

A.
State 종류 분류, State Ownership, Local / Shared / Global / Server State 구분, Props Drilling 판단, 도구 선택 기준이다.

Q. 상태는 전부 전역 상태로 관리하면 편하지 않아?

A.
아니다. 불필요한 전역 상태는 데이터 흐름을 복잡하게 만들고 Re-render 범위와 유지보수 비용을 키울 수 있다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

State Management 문서는 Frontend 상태 설계와 관리에 필요한 범위를 포함한다.

포함 범위:

- State Classification
- Local State
- Shared State
- Global State
- Server State
- Client State
- UI State
- Form State
- Auth State
- URL State
- Cache State
- Derived State
- State Ownership
- Lifting State Up
- Props Drilling
- Context API
- useReducer
- Custom Hook State
- Zustand Basics
- Redux Toolkit Basics
- TanStack Query Basics
- State Persistence
- localStorage / sessionStorage
- Optimistic Update Basics
- Loading / Error / Empty State
- State Normalization Basics
- State Debugging
- State Anti Patterns
- State Management Tool Selection

---

### [핵심]

반드시 포함:

- 모든 상태를 같은 방식으로 관리하지 않음
- Local State는 가장 가까운 Component에 둠
- Shared State는 가장 가까운 공통 부모에 둠
- Global State는 여러 영역에서 반복적으로 필요한 경우에만 사용
- Server State는 API 데이터와 캐시 중심
- URL State는 공유 / 새로고침 / 뒤로가기 복원이 필요한 상태
- Form State는 입력과 검증 흐름 중심
- Auth State는 인증 확인 / 토큰 / 사용자 정보 흐름 중심
- Derived State 중복 저장 금지
- 전역 상태 도구 도입 전 상태 종류를 먼저 분류

---

### [실무]

State Management는 React Component Design 이후 상태 흐름을 정리하는 단계에서 사용한다.

실무 연결:

```text
React Component Design
→ State Classification
→ State Ownership
→ Local / Shared / Global Decision
→ Server State Decision
→ Tool Selection
→ State Flow Review
```

---

### [FAQ]

Q. State Management 문서에서 Redux를 깊게 다뤄?

A.
아니다. Redux Toolkit의 도입 기준과 기본 개념만 다루고 심화 패턴은 별도 문서에서 다룬다.

Q. TanStack Query도 여기서 다뤄?

A.
Server State 관리 도구로 기초 기준은 포함한다. 상세 query key, mutation, invalidation 심화는 Data Fetching 문서에서 다룬다.

Q. Form Library도 여기서 다뤄?

A.
Form State 기준은 포함하지만 React Hook Form 심화는 Form Handling & Validation 문서에서 다룬다.

---

## 2.2 Excluded Scope

### [개념]

State Management 문서에서는 고급 상태관리 라이브러리 심화와 서버 데이터 패칭 심화를 제외한다.

제외 범위:

- Redux Middleware 심화
- Redux Saga
- Redux Observable
- Zustand Middleware 심화
- TanStack Query 심화
- React Hook Form 심화
- XState 심화
- State Machine 심화
- Apollo Client 심화
- GraphQL Cache 심화
- Relay 심화
- Offline Sync 심화
- CRDT
- Real-time Collaboration State
- Micro Frontend State Sharing
- Complex Permission Matrix
- Full Authentication Architecture

---

### [핵심]

제외 이유:

- Foundation 범위 초과
- Data Fetching / Authentication / Form / Frontend Architecture 문서와 분리 필요
- Agent Retrieval 혼선 방지
- Chunk 품질 유지
- 상태 분류와 도구 선택 기준에 집중

---

### [실무]

고급 기술은 별도 Domain Rules에서 관리한다.

예:

```text
State Management
→ Data Fetching & REST API Integration
→ Authentication Frontend Flow
→ Form Handling & Validation
→ Frontend Architecture
→ Advanced State Management
```

---

### [FAQ]

Q. Redux Saga는 여기서 다뤄?

A.
아니다. Redux Saga는 고급 비동기 흐름 도구이므로 Advanced State Management 문서에서 다룬다.

Q. XState는 여기서 다뤄?

A.
기초 언급은 가능하지만 상태 머신 심화는 별도 문서가 적합하다.

Q. 서버 캐시 전략을 깊게 다뤄?

A.
아니다. Server State와 Cache State 구분만 다루고 상세 캐싱 전략은 Data Fetching 문서에서 다룬다.

---

# 3. Section Priority

## 3.1 Required Sections

### [개념]

State Management RAG 문서는 모든 주요 Chunk에 아래 Section을 우선 포함한다.

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
- [실무]: 실제 상태 설계 기준
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

Q. 모든 State Management 문서에 FAQ가 필요해?

A.
필요하다. FAQ는 사용자 질문과 RAG 검색 매칭을 강화한다.

Q. [면접] 섹션을 써도 돼?

A.
안 된다. 반드시 [FAQ] 섹션을 사용한다.

---

## 3.2 Recommended Sections

### [개념]

State Management 문서에는 상태 판단과 오류 검증을 위해 추가 Section을 포함할 수 있다.

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

- State Classification 설명 → [Flow], [Comparison]
- State Ownership 설명 → [Flow], [Checklist]
- Context / Zustand / Redux 비교 → [Comparison]
- Server State 설명 → [Comparison], [주의]
- Props Drilling 설명 → [Troubleshooting]
- Anti Pattern 설명 → [Troubleshooting], [Checklist]

---

### [실무]

예시:

```md
### [Flow]

Identify State
→ Classify State Type
→ Decide Owner
→ Decide Scope
→ Choose Tool
→ Review Anti Pattern
```

---

### [FAQ]

Q. State Management 문서에 Comparison이 중요한 이유는?

A.
Local State, Context, Zustand, Redux, TanStack Query 선택 기준을 정확히 구분해야 하기 때문이다.

Q. State Management 문서에 Troubleshooting이 필요한 이유는?

A.
전역 상태 남용, 상태 중복 저장, stale data, Props Drilling, 불필요한 Re-render 문제가 자주 발생하기 때문이다.

---

# 4. State Classification Rules

## 4.1 State Classification

### [개념]

State Classification은 상태를 성격과 소유 범위에 따라 분류하는 작업이다.

상태는 모두 같은 방식으로 관리하지 않는다.

---

### [핵심]

필수 분류:

- Local State
- Shared State
- Global State
- Server State
- Client State
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
→ URL에 남아야 하는가?
→ 여러 Component가 공유하는가?
→ 여러 페이지에서 필요한가?
→ 입력 Form 상태인가?
→ 계산 가능한 값인가?
→ 관리 위치 결정
```

판단 기준:

```text
Component 내부만 사용 → Local State
형제 Component 공유 → Shared State
여러 페이지 공유 → Global State
API 응답 데이터 → Server State
검색 조건 / 페이지 번호 → URL State
입력값 / 검증값 → Form State
기존 값으로 계산 가능 → Derived Value
```

---

### [FAQ]

Q. State Classification은 왜 먼저 해?

A.
상태 종류를 구분해야 useState, Context, Zustand, Redux, TanStack Query 중 적절한 관리 방법을 선택할 수 있기 때문이다.

Q. 모든 상태를 Zustand나 Redux에 넣으면 안 돼?

A.
권장하지 않는다. Local State나 Form State까지 전역화하면 데이터 흐름이 복잡해지고 유지보수가 어려워질 수 있다.

Q. API 응답 데이터는 Client State야 Server State야?

A.
대부분 Server State다. 서버가 원본 소유자이고 Frontend는 캐시하거나 화면에 표시한다.

---

## 4.2 Client State vs Server State

### [개념]

Client State는 브라우저 UI와 사용자 상호작용을 위해 클라이언트가 소유하는 상태다.

Server State는 서버가 원본을 소유하고 Frontend가 가져와 표시하거나 캐싱하는 상태다.

---

### [핵심]

Client State 예:

- modal open 여부
- selected tab
- input value
- local filter toggle
- theme
- sidebar open 여부

Server State 예:

- user profile
- festival list
- festival detail
- review list
- notification list
- server pagination result
- API cache data

---

### [실무]

비교:

| 비교        | Client State                  | Server State              |
| ----------- | ----------------------------- | ------------------------- |
| 원본 소유자 | Frontend                      | Backend / Server          |
| 예          | modal open, selected tab      | festival list, user info  |
| 관리 도구   | useState, useReducer, Zustand | TanStack Query, API Hook  |
| 주요 문제   | 상태 위치, Props Drilling     | 캐시, stale data, refetch |
| 새로고침    | 사라질 수 있음                | 서버에서 다시 조회        |

권장:

- Server State를 전역 Client State에 무분별하게 복사 금지
- API 데이터 캐싱은 Server State 도구 고려
- UI State와 Server State를 분리
- 서버 원본 변경 후 refetch / invalidate 고려

---

### [FAQ]

Q. Server State를 Redux나 Zustand에 넣어도 돼?

A.
가능은 하지만 캐시, stale data, refetch, pagination 관리가 필요하면 TanStack Query 같은 Server State 도구가 더 적합할 수 있다.

Q. Client State와 Server State를 왜 나눠?

A.
소유자와 갱신 방식이 다르기 때문이다. Server State는 서버 동기화와 캐시 전략이 중요하다.

---

## 4.3 UI State Rules

### [개념]

UI State는 화면 표시와 상호작용을 제어하는 상태다.

예:

- modal open
- dropdown open
- selected tab
- sidebar collapsed
- accordion open
- loading 표시 여부
- toast 표시 여부

---

### [핵심]

반드시 포함:

- modal state
- dropdown state
- tab state
- toggle state
- open / close
- selected item
- UI visibility
- local interaction

---

### [실무]

UI State는 가능한 가까운 Component에 둔다.

예:

```jsx
function ModalButton() {
  const [open, setOpen] = useState(false);

  return (
    <>
      <button type="button" onClick={() => setOpen(true)}>
        Open
      </button>
      {open && <Modal onClose={() => setOpen(false)} />}
    </>
  );
}
```

전역화 검토 상황:

- 여러 페이지에서 같은 Modal 제어
- Global Toast
- App-wide Theme
- Auth-dependent Layout
- 전역 Sidebar 상태

주의:

- 단일 Component 내부 UI State를 전역화하지 않음
- boolean이 많아지면 상태 모델링 재검토
- 상호 배타 상태는 union 사용

---

### [FAQ]

Q. Modal open 상태는 전역으로 둬야 해?

A.
해당 화면에서만 쓰면 Local State가 적합하다. 여러 영역에서 공통으로 열어야 하면 전역 상태를 검토한다.

Q. UI State는 보통 어디에 둬?

A.
해당 상태를 사용하는 가장 가까운 Component에 둔다.

---

## 4.4 URL State Rules

### [개념]

URL State는 URL path나 query string에 저장되는 상태다.

검색 조건, 필터, 페이지 번호처럼 공유와 복원이 필요한 값에 적합하다.

---

### [핵심]

사용 대상:

- search keyword
- filter
- sort
- page
- tab
- selected category
- date range
- map position basics
- path parameter
- query string

---

### [실무]

URL State 적합 조건:

- URL 공유 필요
- 새로고침 후 유지 필요
- 뒤로가기 / 앞으로가기 복원 필요
- 검색 결과 페이지
- 목록 필터 페이지
- 페이지네이션
- 탭 화면

예:

```text
/festivals?keyword=flower&region=seoul&page=1
```

주의:

- URL 값은 문자열
- 숫자 / boolean 변환 필요
- 민감정보 저장 금지
- 너무 복잡한 객체 저장 금지
- Form 입력 중 임시값과 제출된 URL State 구분 가능

---

### [FAQ]

Q. 검색 조건은 State로 둬야 해 URL로 둬야 해?

A.
검색 결과를 공유하거나 새로고침 후 유지해야 하면 URL State가 적합하다.

Q. URL State에 민감정보를 넣어도 돼?

A.
안 된다. URL은 브라우저 기록, 공유 링크, 서버 로그에 남을 수 있다.

---

# 5. State Ownership Rules

## 5.1 State Ownership

### [개념]

State Ownership은 어떤 Component 또는 Store가 State를 소유하고 변경할 책임을 가지는지 결정하는 기준이다.

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
→ Place State
```

예:

```text
SearchForm 입력값만 필요 → SearchForm Local State
SearchForm 입력 결과가 FestivalList에 필요 → FestivalPage Shared State
검색 조건을 URL로 공유해야 함 → URL State
축제 목록은 서버 원본 → Server State
```

주의:

- State를 너무 위로 올리면 Props 전달 증가
- State를 너무 아래에 두면 공유 어려움
- 전역 Store는 마지막 선택지로 검토
- Server State를 Client State처럼 직접 소유하지 않음

---

### [FAQ]

Q. State는 어디에 둬야 해?

A.
그 State를 읽고 변경하는 Component들의 가장 가까운 공통 부모에 두는 것이 기본이다.

Q. State Owner가 잘못되면 어떤 문제가 생겨?

A.
Props Drilling, 중복 상태, 불필요한 Re-render, 데이터 불일치 문제가 생길 수 있다.

---

## 5.2 Lifting State Up

### [개념]

Lifting State Up은 여러 Component가 같은 상태를 공유해야 할 때 State를 공통 부모로 올리는 패턴이다.

---

### [핵심]

사용 상황:

- 형제 Component가 같은 상태 필요
- 검색 Form 상태가 목록에 영향
- 선택된 item이 상세 영역에 영향
- Form 입력이 Preview에 영향
- 부모가 자식 이벤트 결과를 알아야 함

---

### [실무]

예:

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

권장:

- 공유 필요가 생긴 시점에 올림
- 너무 일찍 App까지 올리지 않음
- callback props로 변경 요청 전달
- State Owner를 명확히 표현
- 깊은 Props 전달이 되면 구조 개선 검토

---

### [FAQ]

Q. Lifting State Up은 언제 해?

A.
여러 Component가 같은 State를 읽거나 변경 결과를 공유해야 할 때 한다.

Q. State를 올리면 무조건 좋은 거야?

A.
아니다. 필요한 범위보다 높게 올리면 Props 전달과 Re-render 범위가 커질 수 있다.

---

## 5.3 Derived State Rules

### [개념]

Derived State는 기존 Props, State, Server Data로부터 계산 가능한 값이다.

계산 가능한 값은 별도 State로 저장하지 않는 것이 좋다.

---

### [핵심]

예:

- fullName
- filteredItems
- sortedItems
- totalPrice
- selectedItem
- isValid
- canSubmit
- visibleItems

---

### [실무]

나쁜 예:

```jsx
const [items, setItems] = useState([]);
const [filteredItems, setFilteredItems] = useState([]);
```

좋은 예:

```jsx
const filteredItems = items.filter((item) => item.title.includes(keyword));
```

주의:

- 원본 State와 Derived State 불일치 가능
- 계산 비용이 큰 경우 memoization 고려
- 서버 응답을 화면용으로 변환하는 mapping 함수 분리 가능
- Derived 값을 전역 Store에 저장하지 않음

---

### [FAQ]

Q. 계산 가능한 값도 State로 저장해야 해?

A.
대부분 아니다. 기존 State나 Props로 계산 가능하면 렌더링 중 계산하는 것이 좋다.

Q. Derived State가 위험한 이유는?

A.
원본 상태가 바뀌었는데 파생 상태가 갱신되지 않아 데이터 불일치가 생길 수 있다.

---

# 6. Local and Shared State Rules

## 6.1 Local State Rules

### [개념]

Local State는 특정 Component 내부에서만 필요한 상태다.

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

---

### [실무]

예:

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
    </form>
  );
}
```

권장:

- 가장 가까운 Component에 둠
- 외부 공유가 필요해질 때만 올림
- 전역 Store에 넣지 않음
- Component 제거 시 함께 사라져도 되는 값에 적합

---

### [FAQ]

Q. Local State는 언제 써?

A.
특정 Component 내부에서만 필요하고 다른 Component와 공유하지 않는 상태에 사용한다.

Q. input 값은 무조건 전역 상태로 둬야 해?

A.
아니다. 해당 Form 내부에서만 필요하면 Local State가 적합하다.

---

## 6.2 Shared State Rules

### [개념]

Shared State는 여러 Component가 함께 읽거나 변경해야 하는 상태다.

---

### [핵심]

Shared State 예:

- 검색 조건
- 선택된 item
- 현재 tab
- 부모와 자식이 공유하는 form 결과
- 형제 Component가 함께 쓰는 filter
- 특정 페이지 내부 공통 상태

---

### [실무]

Shared State는 가장 가까운 공통 부모에 둔다.

예:

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

주의:

- Shared State라고 무조건 Global State 아님
- 페이지 내부 공유는 Page Component State로 충분할 수 있음
- Props 전달이 깊어지면 구조 개선 검토
- URL State가 더 적합한지 검토

---

### [FAQ]

Q. Shared State는 전역 상태야?

A.
항상 전역 상태는 아니다. 특정 페이지 내부에서만 공유되면 공통 부모 State로 충분할 수 있다.

Q. 형제 Component가 같은 값을 써야 하면 어떻게 해?

A.
가장 가까운 공통 부모로 State를 올리고 Props와 callback으로 전달한다.

---

# 7. Global State Rules

## 7.1 Global State Criteria

### [개념]

Global State는 여러 페이지 또는 앱 전체에서 공유해야 하는 상태다.

전역 상태는 편의 기능이 아니라 공유 범위가 넓은 상태를 관리하기 위한 도구다.

---

### [핵심]

Global State 적합 예:

- authenticated user summary
- auth status
- theme
- global modal
- global toast
- app layout state
- cart
- user preference
- notification unread count
- language setting

Global State 부적합 예:

- 단일 input value
- 단일 modal open
- 특정 페이지의 임시 filter
- 특정 Component 내부 selected tab
- Derived State
- 단순 API list data 전체

---

### [실무]

Global State 판단 Flow:

```text
여러 페이지에서 필요한가?
→ 깊은 Component 트리에서 반복 전달되는가?
→ URL State로 표현 가능한가?
→ Server State 도구가 더 적합한가?
→ 전역 Store 도입
```

주의:

- 전역 상태는 관리 비용이 있음
- 상태 변경 영향 범위가 커짐
- Store 구조 설계 필요
- 초기화 / 지속 저장 / 동기화 기준 필요
- Server State와 혼합 주의

---

### [FAQ]

Q. Global State는 언제 써?

A.
여러 페이지나 깊은 Component 트리에서 반복적으로 필요한 상태일 때 사용한다.

Q. 모든 페이지에서 쓰지 않는 값도 Global State로 둬도 돼?

A.
가능은 하지만 권장하지 않는다. 필요한 범위가 좁으면 Local 또는 Shared State가 더 적합하다.

---

## 7.2 Global Store Design Rules

### [개념]

Global Store Design은 전역 상태를 어떤 단위와 구조로 나눌지 결정하는 작업이다.

---

### [핵심]

설계 대상:

- store domain
- state field
- action function
- selector
- initial state
- persistence
- reset
- auth lifecycle
- side effect boundary

---

### [실무]

Store 분리 예:

```text
authStore
- user
- authenticated
- login
- logout

uiStore
- theme
- sidebarOpen
- toast

notificationStore
- unreadCount
- setUnreadCount
```

권장:

- 도메인 기준 분리
- action 이름 명확화
- Store에 Derived State 과다 저장 금지
- API 호출 위치 기준 명확화
- logout 시 reset 대상 명확화
- persist 대상 최소화

주의:

- 모든 상태를 하나의 거대한 store에 넣지 않음
- Store 간 순환 의존 주의
- 서버 응답 원본 전체 저장 주의
- 민감정보 persist 금지

---

### [FAQ]

Q. 전역 Store는 하나로 만드는 게 좋아?

A.
작은 프로젝트는 하나로 가능하지만 규모가 커지면 auth, ui, notification처럼 도메인별로 분리하는 것이 좋다.

Q. Store에 API 응답을 전부 저장해도 돼?

A.
무조건 권장하지 않는다. 서버 데이터는 TanStack Query 같은 Server State 도구가 더 적합할 수 있다.

---

# 8. Props Drilling Rules

## 8.1 Props Drilling Problem

### [개념]

Props Drilling은 중간 Component들이 직접 사용하지 않는 Props를 깊은 자식에게 전달하기만 하는 문제다.

---

### [핵심]

문제:

- 중간 Component가 사용하지 않는 Props 전달
- Props 변경 시 여러 파일 수정
- Component 재사용성 저하
- 데이터 흐름 추적 어려움
- Component 계층 의존 증가

---

### [실무]

Props Drilling 판단 Flow:

```text
Prop 전달 경로 추적
→ 중간 Component가 실제 사용하는가?
→ 전달 깊이가 깊은가?
→ 여러 branch로 퍼지는가?
→ State Owner가 적절한가?
→ Context / Store / Composition 검토
```

해결 후보:

- Component Composition
- State 위치 조정
- Context API
- Zustand / Redux Store
- URL State
- Custom Hook
- Feature 구조 개선

주의:

- 1~2단계 Props 전달은 정상
- 모든 Props 전달을 문제로 보지 않음
- Context나 Store도 남용하면 복잡도 증가

---

### [FAQ]

Q. Props Drilling은 무조건 나쁜 거야?

A.
아니다. 짧은 Props 전달은 자연스럽다. 깊고 반복되어 유지보수가 어려워질 때 문제가 된다.

Q. Props Drilling 해결은 무조건 Context야?

A.
아니다. State 위치 조정, Component Composition, URL State, 전역 Store 등 여러 선택지를 검토해야 한다.

---

## 8.2 Props Drilling Solution Rules

### [개념]

Props Drilling Solution은 깊은 Props 전달 문제를 줄이기 위한 설계 선택이다.

---

### [핵심]

해결 순서:

1. Props 전달이 정말 문제인지 확인
2. State Owner 재검토
3. Component 구조 단순화
4. children / composition 활용
5. Context API 검토
6. 전역 Store 검토
7. Server State 도구 검토

---

### [실무]

Composition 개선 예:

```jsx
function Page() {
  return <Layout header={<Header user={user} />} content={<Content />} />;
}
```

Context 검토 상황:

- theme
- auth user
- language
- layout preference
- deeply shared UI state

전역 Store 검토 상황:

- 여러 페이지 공유
- 여러 feature에서 변경
- Context만으로 action 관리가 복잡
- 상태 변화 추적 필요

---

### [FAQ]

Q. Context와 Zustand 중 뭐가 좋아?

A.
Theme처럼 비교적 단순하고 변경 빈도가 낮은 값은 Context가 적합할 수 있고, 변경 함수와 상태가 많아지면 Zustand 같은 Store가 편할 수 있다.

Q. Props Drilling이 생기면 바로 Redux를 써야 해?

A.
아니다. Redux는 복잡한 전역 상태에 적합하다. 먼저 구조 조정과 Context, Zustand를 검토한다.

---

# 9. Context API Rules

## 9.1 Context API Basics

### [개념]

Context API는 Component Tree 아래로 값을 직접 전달하지 않고 하위 Component들이 공유 값을 읽을 수 있게 하는 React 기능이다.

---

### [핵심]

사용 대상:

- theme
- auth summary
- language
- layout preference
- app config
- low-frequency shared state

부적합 대상:

- 빠르게 자주 바뀌는 대량 데이터
- API list cache 전체
- Form 입력값 전체
- 복잡한 action이 많은 상태
- 자주 변경되는 pagination data

---

### [실무]

Context 기본 구조:

```jsx
const ThemeContext = createContext(null);

function ThemeProvider({ children }) {
  const [theme, setTheme] = useState("light");

  return (
    <ThemeContext.Provider value={{ theme, setTheme }}>
      {children}
    </ThemeContext.Provider>
  );
}
```

주의:

- Provider value가 바뀌면 구독 Component Re-render 가능
- Context를 너무 큰 객체로 만들지 않음
- Context 분리 고려
- Custom Hook으로 사용 API 감싸기
- Provider 위치 명확화

---

### [FAQ]

Q. Context API는 전역 상태관리야?

A.
전역처럼 값을 공유할 수 있지만 상태관리 라이브러리라기보다 Component Tree에 값을 공급하는 React 기능에 가깝다.

Q. Context는 언제 써?

A.
Theme, Auth Summary, Language처럼 여러 하위 Component에서 필요한 값을 전달할 때 사용한다.

Q. 모든 상태를 Context에 넣어도 돼?

A.
권장하지 않는다. 자주 바뀌는 값이나 복잡한 상태는 전용 상태관리 도구가 더 적합할 수 있다.

---

## 9.2 Context Custom Hook Rules

### [개념]

Context Custom Hook은 Context 사용 코드를 안전하고 일관되게 감싸는 Custom Hook이다.

---

### [핵심]

목적:

- useContext 직접 사용 숨김
- Provider 누락 감지
- Context 사용 API 통일
- 타입 안정성 강화
- 재사용성 향상

---

### [실무]

예:

```tsx
const AuthContext = createContext<AuthContextValue | null>(null);

export function useAuth() {
  const context = useContext(AuthContext);

  if (!context) {
    throw new Error("useAuth must be used within AuthProvider");
  }

  return context;
}
```

권장:

- Context마다 전용 Hook 제공
- Provider 외부 사용 오류 명확화
- null check 처리
- Hook 이름은 use로 시작
- Context Value Type 명확화

---

### [FAQ]

Q. useContext를 직접 쓰면 안 돼?

A.
가능하지만 Custom Hook으로 감싸면 Provider 누락 검증과 사용 API 통일이 쉬워진다.

Q. Context 기본값은 null로 둬도 돼?

A.
가능하다. 대신 Custom Hook에서 null을 검사해 Provider 누락 오류를 명확히 처리한다.

---

## 9.3 Context Performance Caution

### [개념]

Context Performance Caution은 Context value 변경 시 하위 구독 Component들이 Re-render될 수 있다는 주의사항이다.

---

### [핵심]

문제:

- Provider value 객체가 매 렌더링마다 새로 생성됨
- 자주 바뀌는 상태를 큰 Context에 넣음
- 많은 Component가 같은 Context를 구독
- 불필요한 Re-render 증가

---

### [실무]

주의 예:

```jsx
<AuthContext.Provider value={{ user, login, logout }}>
  {children}
</AuthContext.Provider>
```

개선 후보:

- Context 분리
- value memoization 고려
- 자주 바뀌는 상태는 별도 Store 검토
- 단순 config와 dynamic state 분리
- selector 기반 Store 검토

주의:

- memoization을 무조건 먼저 적용하지 않음
- 실제 성능 문제가 있을 때 측정 후 개선
- Context 자체보다 value 설계가 중요

---

### [FAQ]

Q. Context를 쓰면 무조건 성능 문제가 생겨?

A.
아니다. 하지만 큰 value나 자주 바뀌는 상태를 많은 Component가 구독하면 Re-render 문제가 생길 수 있다.

Q. Context 성능 문제는 어떻게 줄여?

A.
Context를 역할별로 분리하고 자주 바뀌는 상태는 전용 Store를 검토한다.

---

# 10. useReducer Rules

## 10.1 useReducer Basics

### [개념]

useReducer는 여러 상태 전환을 action 기반으로 관리하는 React Hook이다.

복잡한 Local State나 Form State에 사용할 수 있다.

---

### [핵심]

사용 대상:

- 복잡한 상태 전환
- 여러 action type
- 상태 변경 규칙 명확화
- Form State
- Step State
- Local UI State Machine Basics
- useState가 많아진 Component

---

### [실무]

예:

```jsx
const initialState = {
  keyword: "",
  region: "",
};

function reducer(state, action) {
  switch (action.type) {
    case "SET_KEYWORD":
      return { ...state, keyword: action.payload };
    case "SET_REGION":
      return { ...state, region: action.payload };
    case "RESET":
      return initialState;
    default:
      return state;
  }
}
```

사용:

```jsx
const [state, dispatch] = useReducer(reducer, initialState);
```

주의:

- 단순 boolean / string 상태에는 useState가 더 간단
- reducer는 순수 함수로 작성
- action type naming 통일
- 상태 변경은 immutable update
- 복잡한 전역 상태는 별도 Store 검토

---

### [FAQ]

Q. useReducer는 언제 써?

A.
상태 필드가 많고 변경 규칙이 action 단위로 명확할 때 사용한다.

Q. useState와 useReducer 중 뭐가 좋아?

A.
단순 상태는 useState가 좋고, 상태 전환이 복잡하면 useReducer가 적합하다.

Q. reducer 안에서 API 호출해도 돼?

A.
권장하지 않는다. reducer는 순수 함수로 유지하고 API 호출은 외부에서 처리한다.

---

## 10.2 useReducer Action Rules

### [개념]

useReducer Action은 상태 변경 의도를 표현하는 객체다.

Action은 상태가 어떻게 바뀌어야 하는지 reducer에 전달한다.

---

### [핵심]

Action 구성:

- type
- payload
- action naming
- discriminated union
- reducer switch
- default case
- immutable update

---

### [실무]

TypeScript 예:

```tsx
type SearchState = {
  keyword: string;
  region: string;
};

type SearchAction =
  | { type: "SET_KEYWORD"; payload: string }
  | { type: "SET_REGION"; payload: string }
  | { type: "RESET" };

function searchReducer(state: SearchState, action: SearchAction): SearchState {
  switch (action.type) {
    case "SET_KEYWORD":
      return { ...state, keyword: action.payload };
    case "SET_REGION":
      return { ...state, region: action.payload };
    case "RESET":
      return { keyword: "", region: "" };
  }
}
```

주의:

- action type 문자열 오타 방지
- payload 타입 명확화
- default 처리 기준 통일
- 상태 필드 직접 변경 금지

---

### [FAQ]

Q. useReducer action type은 어떻게 지어?

A.
SET_KEYWORD, RESET_FORM처럼 상태 변경 의도를 드러내는 이름이 좋다.

Q. TypeScript에서 useReducer action은 어떻게 정의해?

A.
Discriminated Union으로 action type별 payload를 명확히 정의하는 방식이 좋다.

---

# 11. Zustand Rules

## 11.1 Zustand Basics

### [개념]

Zustand는 간단한 API로 전역 상태 Store를 만들 수 있는 React 상태관리 라이브러리다.

작고 직관적인 Global State 관리에 적합하다.

---

### [핵심]

사용 대상:

- auth summary
- theme
- global UI state
- sidebar state
- toast state
- selected global option
- notification unread count
- medium complexity global state

---

### [실무]

기본 구조 예:

```typescript
import { create } from "zustand";

type UiStore = {
  sidebarOpen: boolean;
  toggleSidebar: () => void;
};

export const useUiStore = create<UiStore>((set) => ({
  sidebarOpen: false,
  toggleSidebar: () => set((state) => ({ sidebarOpen: !state.sidebarOpen })),
}));
```

사용:

```tsx
const sidebarOpen = useUiStore((state) => state.sidebarOpen);
const toggleSidebar = useUiStore((state) => state.toggleSidebar);
```

권장:

- selector로 필요한 값만 구독
- store를 도메인별로 분리
- action 함수 포함
- persist는 필요한 값만 적용
- Server State 전체 저장 지양

---

### [FAQ]

Q. Zustand는 언제 써?

A.
Context보다 action과 상태가 많고 Redux보다 가벼운 전역 상태가 필요할 때 적합하다.

Q. Zustand에 API 데이터를 전부 넣어도 돼?

A.
권장하지 않는다. 서버 데이터 캐싱은 TanStack Query 같은 Server State 도구가 더 적합할 수 있다.

Q. Zustand selector는 왜 써?

A.
필요한 상태만 구독해 불필요한 Re-render를 줄이기 위해 사용한다.

---

## 11.2 Zustand Store Design Rules

### [개념]

Zustand Store Design은 상태 필드와 action을 도메인별로 구성하는 기준이다.

---

### [핵심]

설계 요소:

- store name
- state fields
- actions
- selectors
- initial values
- reset action
- persistence
- domain separation

---

### [실무]

Auth Store 예:

```typescript
type AuthUser = {
  userId: number;
  nickname: string;
  role: "ROLE_USER" | "ROLE_ADMIN";
};

type AuthStore = {
  user: AuthUser | null;
  authenticated: boolean;
  setUser: (user: AuthUser) => void;
  clearAuth: () => void;
};

export const useAuthStore = create<AuthStore>((set) => ({
  user: null,
  authenticated: false,
  setUser: (user) => set({ user, authenticated: true }),
  clearAuth: () => set({ user: null, authenticated: false }),
}));
```

권장:

- authStore / uiStore / notificationStore 등 분리
- action 이름 명확화
- logout 시 reset action 제공
- persist 대상 최소화
- 민감정보 저장 주의

---

### [FAQ]

Q. Zustand Store는 어떻게 나누는 게 좋아?

A.
auth, ui, notification처럼 도메인 또는 책임 기준으로 나누는 것이 좋다.

Q. Store에 action 함수를 같이 넣어도 돼?

A.
가능하다. Zustand에서는 상태와 상태 변경 함수를 함께 정의하는 방식이 일반적이다.

---

# 12. Redux Toolkit Rules

## 12.1 Redux Toolkit Basics

### [개념]

Redux Toolkit은 Redux를 현대적인 방식으로 사용하기 위한 공식 도구 모음이다.

복잡한 전역 상태와 명확한 action / reducer 흐름이 필요한 경우에 적합하다.

---

### [핵심]

사용 대상:

- large scale global state
- complex state transition
- predictable update flow
- action history
- devtools
- team convention
- complex domain state
- centralized state architecture

---

### [실무]

Redux Toolkit 고려 상황:

- 상태 변경 흐름 추적이 중요
- 전역 상태 도메인이 많음
- 여러 팀원이 같은 상태 규칙을 공유
- 복잡한 action과 reducer가 필요
- 기존 프로젝트가 Redux 기반
- DevTools 기반 디버깅 필요

주의:

- 작은 프로젝트에는 과할 수 있음
- boilerplate가 Zustand보다 많을 수 있음
- Server State 캐시는 RTK Query 또는 TanStack Query 고려
- 단순 UI State만을 위해 Redux 도입 지양

---

### [FAQ]

Q. Redux Toolkit은 언제 써?

A.
복잡한 전역 상태와 예측 가능한 상태 변경 흐름, DevTools 기반 추적이 필요한 큰 프로젝트에 적합하다.

Q. 작은 프로젝트에도 Redux Toolkit을 써야 해?

A.
필수는 아니다. 작은 프로젝트는 useState, Context, Zustand만으로 충분할 수 있다.

Q. Redux와 Redux Toolkit은 달라?

A.
Redux Toolkit은 Redux를 더 쉽게 사용하기 위한 공식 권장 도구다.

---

## 12.2 Redux Slice Rules

### [개념]

Slice는 Redux Toolkit에서 특정 도메인의 state, reducer, action을 함께 정의하는 단위다.

---

### [핵심]

포함 요소:

- slice name
- initialState
- reducers
- actions
- reducer export
- typed selector
- dispatch

---

### [실무]

기본 예:

```typescript
import { createSlice, PayloadAction } from "@reduxjs/toolkit";

type UiState = {
  sidebarOpen: boolean;
};

const initialState: UiState = {
  sidebarOpen: false,
};

const uiSlice = createSlice({
  name: "ui",
  initialState,
  reducers: {
    toggleSidebar(state) {
      state.sidebarOpen = !state.sidebarOpen;
    },
    setSidebarOpen(state, action: PayloadAction<boolean>) {
      state.sidebarOpen = action.payload;
    },
  },
});

export const { toggleSidebar, setSidebarOpen } = uiSlice.actions;
export default uiSlice.reducer;
```

주의:

- Redux Toolkit은 내부적으로 Immer를 사용해 mutation처럼 작성 가능
- 실제 불변성 처리는 Immer가 담당
- slice는 도메인 기준으로 분리
- action payload 타입 명확화

---

### [FAQ]

Q. Redux Toolkit에서 state를 직접 바꿔도 돼?

A.
createSlice 내부 reducer에서는 Immer가 불변 업데이트로 변환하므로 mutation처럼 작성할 수 있다.

Q. Slice는 어떻게 나눠?

A.
auth, ui, notification, cart처럼 도메인 책임 기준으로 나눈다.

---

# 13. TanStack Query and Server State Rules

## 13.1 Server State Management Rules

### [개념]

Server State Management는 서버가 원본으로 소유하는 데이터를 Frontend에서 조회, 캐싱, 갱신, 동기화하는 방식이다.

TanStack Query 같은 도구는 Server State 관리에 적합하다.

---

### [핵심]

Server State 특징:

- server owns data
- async loading
- cache
- stale data
- refetch
- mutation
- invalidation
- pagination
- background update
- error state

---

### [실무]

Server State 예:

- festival list
- festival detail
- review list
- user profile
- notification list
- chat room list
- favorite list
- donation history

관리 기준:

```text
API Data
→ Server State 여부 확인
→ Cache 필요 여부 확인
→ Refetch 필요 여부 확인
→ TanStack Query 고려
→ UI State와 분리
```

주의:

- Server State를 전역 Client Store에 복사하지 않음
- API mutation 후 cache invalidation 필요
- stale data 처리 기준 필요
- loading / error 상태 분리
- optimistic update는 신중하게 적용

---

### [FAQ]

Q. Server State는 왜 별도로 관리해?

A.
서버 데이터는 캐시, stale data, refetch, mutation 같은 동기화 문제가 있어서 일반 Client State와 관리 방식이 다르다.

Q. API 데이터는 Zustand에 넣으면 안 돼?

A.
가능은 하지만 캐싱과 동기화가 복잡해질 수 있다. Server State 도구가 더 적합한 경우가 많다.

---

## 13.2 TanStack Query Basics

### [개념]

TanStack Query는 API 데이터 같은 Server State를 조회, 캐싱, 갱신, 동기화하는 도구다.

---

### [핵심]

필수 키워드:

- QueryClient
- QueryClientProvider
- useQuery
- useMutation
- queryKey
- queryFn
- invalidateQueries
- staleTime
- cacheTime / gcTime
- loading
- error
- data
- refetch

---

### [실무]

기초 예:

```tsx
function FestivalListPage() {
  const { data, isLoading, error } = useQuery({
    queryKey: ["festivals"],
    queryFn: getFestivals,
  });

  if (isLoading) {
    return <p>Loading...</p>;
  }

  if (error) {
    return <p>Failed to load festivals.</p>;
  }

  return <FestivalList festivals={data ?? []} />;
}
```

권장:

- queryKey는 데이터 식별 기준
- queryFn은 API 요청 함수
- mutation 후 invalidateQueries 고려
- 서버 데이터는 query cache에 맡김
- UI State와 query state 분리
- 상세 심화는 Data Fetching 문서에서 다룸

---

### [FAQ]

Q. TanStack Query는 전역 상태관리야?

A.
일반적인 Client State 전역 관리 도구라기보다 Server State와 API 캐시 관리 도구에 가깝다.

Q. queryKey는 왜 중요해?

A.
캐시에서 데이터를 식별하고 refetch / invalidation 대상을 결정하기 때문이다.

Q. mutation 후 목록을 갱신하려면?

A.
관련 queryKey를 invalidate해서 다시 조회하도록 처리할 수 있다.

---

# 14. Form State Rules

## 14.1 Form State Management

### [개념]

Form State는 사용자의 입력값, 검증 상태, 제출 상태를 관리하는 상태다.

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

간단한 Form은 useState로 충분하다.

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

복잡한 Form은 전용 Form 도구 검토:

- 입력 필드가 많음
- 검증 규칙이 많음
- 에러 메시지가 복잡함
- touched / dirty 관리 필요
- 서버 검증 오류 반영 필요
- 성능 최적화 필요

주의:

- Form 입력값을 무조건 전역 상태로 두지 않음
- 제출 후 서버 응답 상태와 입력 상태 구분
- URL State와 Form 임시값 구분
- 민감정보 persist 금지

---

### [FAQ]

Q. Form State는 전역으로 둬야 해?

A.
대부분 아니다. Form 내부에서만 필요한 입력값은 Local State나 Form Library로 관리하는 것이 좋다.

Q. React Hook Form은 언제 써?

A.
입력 필드와 검증 규칙이 많고 touched, dirty, error 상태 관리가 복잡할 때 검토한다.

---

# 15. Auth State Rules

## 15.1 Auth State Management

### [개념]

Auth State는 사용자의 인증 여부와 사용자 요약 정보를 표현하는 상태다.

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

권장:

- 인증 확인 중 loading 상태 분리
- 로그인 / 로그아웃 action 명확화
- 권한 role naming 통일
- Protected Route와 연결
- Backend 인증/인가를 최종 보안 기준으로 둠
- Token 저장 위치 보안 검토
- 민감정보 Store 저장 최소화

주의:

- Frontend Auth State는 UX용
- JWT 존재만으로 신뢰하지 않음
- role check는 Backend에서도 필수
- logout 시 관련 Store reset 필요
- 만료 처리 기준 필요

---

### [FAQ]

Q. Auth State는 전역 상태가 좋아?

A.
대부분 여러 페이지와 Component에서 필요하므로 전역 상태나 Context로 관리하는 경우가 많다.

Q. Frontend에서 로그인 상태만 확인하면 보안이 돼?

A.
아니다. Frontend 인증 상태는 UX용이고 실제 보안은 Backend 인증/인가가 반드시 필요하다.

Q. logout 시 어떤 상태를 초기화해야 해?

A.
user, authenticated, notification, user-specific cache, 민감한 화면 상태 등을 초기화해야 한다.

---

# 16. Persistence Rules

## 16.1 State Persistence

### [개념]

State Persistence는 상태를 새로고침 후에도 유지하기 위해 localStorage, sessionStorage, IndexedDB 등에 저장하는 방식이다.

---

### [핵심]

저장 후보:

- theme
- language
- simple user preference
- sidebar preference
- non-sensitive UI setting
- recent search basics

저장 주의 대상:

- access token
- refresh token
- password
- personal sensitive data
- payment data
- server cache 전체
- form sensitive input

---

### [실무]

Persistence 판단 Flow:

```text
새로고침 후 유지가 필요한가?
→ URL State가 더 적합한가?
→ 서버 저장이 더 적합한가?
→ 민감정보인가?
→ localStorage / sessionStorage 검토
```

주의:

- localStorage는 JavaScript에서 접근 가능
- XSS 발생 시 노출 위험
- 민감정보 저장 주의
- 저장한 상태의 version migration 고려
- logout 시 사용자별 저장 값 제거 검토

---

### [FAQ]

Q. 모든 전역 상태를 localStorage에 저장하면 좋아?

A.
아니다. 새로고침 후 유지가 필요한 비민감 설정만 저장하는 것이 좋다.

Q. localStorage에 token을 저장해도 돼?

A.
보안 위험이 있다. 프로젝트 인증 구조와 보안 요구사항에 따라 신중히 결정해야 한다.

Q. 검색 조건은 localStorage에 저장해?

A.
공유와 뒤로가기 복원이 필요하면 localStorage보다 URL Query String이 더 적합한 경우가 많다.

---

# 17. State Debugging Rules

## 17.1 State Debugging

### [개념]

State Debugging은 상태 값, 변경 위치, 데이터 흐름, Re-render 원인을 추적하는 과정이다.

---

### [핵심]

확인 대상:

- current state value
- state owner
- setter call location
- props flow
- store action
- query cache
- derived value
- stale closure
- re-render source
- async update timing

---

### [실무]

Debug Flow:

```text
UI Problem
→ State Value Check
→ State Owner Check
→ Setter / Action Check
→ Props Flow Check
→ Derived State Check
→ Server State Cache Check
→ Re-render Check
```

도구:

- React DevTools
- Browser Console
- Network Tab
- Redux DevTools
- TanStack Query DevTools
- Zustand selector logging basics

주의:

- setState 직후 값이 즉시 바뀌었다고 가정 금지
- stale closure 확인
- derived state 중복 저장 확인
- server data와 local copy 불일치 확인
- StrictMode 개발 동작 확인

---

### [FAQ]

Q. React State 값은 어디서 확인해?

A.
React DevTools에서 Component의 Props와 State를 확인할 수 있다.

Q. 전역 상태 변경은 어떻게 추적해?

A.
Redux DevTools, Zustand 로그, Store action, React DevTools를 함께 확인한다.

Q. API 데이터가 화면과 안 맞으면?

A.
Network 응답, query cache, local copy, mapping 함수, State 업데이트 위치를 확인한다.

---

# 18. Troubleshooting Rules

## 18.1 Overused Global State

### [개념]

Overused Global State는 Local 또는 Shared State로 충분한 값을 전역 Store에 과도하게 넣는 문제다.

---

### [핵심]

문제:

- Store가 너무 커짐
- 상태 변경 영향 범위 증가
- 데이터 흐름 추적 어려움
- Component 재사용성 저하
- 불필요한 persistence 증가
- 서버 데이터와 중복 저장

원인:

- 전역 상태 도구를 기본 선택지로 사용
- State Classification 생략
- Props 전달을 모두 문제로 판단
- Server State와 Client State 혼동
- Derived State 저장

해결:

- 상태 종류 재분류
- Local State로 내리기
- Page State로 이동
- URL State로 이동
- TanStack Query로 Server State 분리
- Derived State 제거

---

### [실무]

Debug Flow:

```text
Store Field Review
→ Usage Scope Check
→ Local / Shared 가능 여부 확인
→ Server State 여부 확인
→ Derived State 여부 확인
→ Store Slim Down
```

---

### [FAQ]

Q. 전역 Store가 너무 커졌으면 어떻게 해?

A.
각 상태의 사용 범위와 소유자를 다시 확인하고 Local State, URL State, Server State로 분리한다.

Q. 전역 상태가 많으면 왜 안 좋아?

A.
변경 영향 범위가 커지고 데이터 흐름을 추적하기 어려워지며 유지보수 비용이 증가한다.

---

## 18.2 Duplicate State Problem

### [개념]

Duplicate State Problem은 같은 의미의 데이터를 여러 State에 중복 저장해 불일치가 발생하는 문제다.

---

### [핵심]

문제:

- 목록 데이터와 필터 결과가 불일치
- user 정보가 authStore와 component state에서 다름
- API cache와 global store 값이 다름
- 수정 후 일부 화면만 갱신
- 선택 상태와 URL 값 불일치

원인:

- Derived State 저장
- Server State local copy
- Store와 Component State 중복
- URL State와 Local State 중복
- Mapping 기준 불명확

해결:

- Single Source of Truth 결정
- Derived State 계산으로 변경
- Server State는 Query Cache 기준
- URL State는 URL 기준
- 중복 저장 제거
- mapping 함수 일관화

---

### [실무]

예:

```text
문제: festivals와 filteredFestivals를 둘 다 State로 저장
해결: filteredFestivals는 festivals + keyword로 계산
```

Debug Flow:

```text
Find Duplicated Values
→ Decide Source of Truth
→ Remove Derived State
→ Use Mapping Function
→ Sync URL or Query Cache
```

---

### [FAQ]

Q. 같은 값을 여러 State에 저장하면 왜 문제야?

A.
한쪽만 갱신되면 화면마다 다른 값이 표시되는 데이터 불일치가 생길 수 있다.

Q. Single Source of Truth가 뭐야?

A.
하나의 데이터는 하나의 기준 출처에서 관리하고 나머지는 그 값을 기반으로 계산하는 원칙이다.

---

## 18.3 Stale State Problem

### [개념]

Stale State Problem은 오래된 State 값을 기준으로 로직이 실행되는 문제다.

React Closure, 비동기 로직, Server State 캐시에서 자주 발생한다.

---

### [핵심]

문제:

- setState 후 이전 값 출력
- Event Handler가 오래된 값 사용
- interval에서 이전 state 사용
- API 응답 순서 꼬임
- Cache data가 오래됨

원인:

- setState 비동기 업데이트 오해
- closure가 이전 값 캡처
- dependency array 누락
- functional update 미사용
- stale cache 정책 미설정
- race condition

해결:

- functional update 사용
- dependency array 점검
- ref 사용 검토
- request cancellation 검토
- query invalidation / refetch
- 최신 응답만 반영

---

### [실무]

나쁜 예:

```jsx
setCount(count + 1);
setCount(count + 1);
```

좋은 예:

```jsx
setCount((prevCount) => prevCount + 1);
setCount((prevCount) => prevCount + 1);
```

---

### [FAQ]

Q. setState 후 값이 바로 안 바뀌는 이유는?

A.
React State 업데이트는 비동기적으로 처리될 수 있고 렌더링 이후 새 값이 반영되기 때문이다.

Q. 이전 State를 기준으로 업데이트할 때는 어떻게 해?

A.
functional update를 사용한다. 예: `setCount((prev) => prev + 1)`.

---

## 18.4 Props Drilling Troubleshooting

### [개념]

Props Drilling Troubleshooting은 깊은 Props 전달로 인한 구조 문제를 분석하는 과정이다.

---

### [핵심]

문제:

- 중간 Component가 props를 사용하지 않음
- props 이름 변경 시 여러 파일 수정
- 깊은 자식에서만 필요한 값이 최상위에서 내려옴
- Component 재사용 어려움
- 상태 위치 판단 어려움

해결:

- 전달 경로 추적
- State Owner 재검토
- Component Composition 적용
- Context 적용
- Global Store 적용
- URL State 전환
- Feature 구조 분리

---

### [실무]

Debug Flow:

```text
Prop Source 확인
→ Prop Destination 확인
→ Intermediate Usage 확인
→ State Owner 확인
→ Scope 확인
→ Context / Store / Composition 선택
```

주의:

- 1~2단계 전달은 정상
- 해결 도구보다 상태 범위 판단이 먼저
- Context도 남용하면 복잡해짐

---

### [FAQ]

Q. Props Drilling 문제는 어떻게 판단해?

A.
중간 Component가 사용하지 않는 props를 여러 단계로 전달하고 수정 비용이 커질 때 문제로 판단한다.

Q. Props Drilling을 해결하려고 무조건 Zustand를 써도 돼?

A.
아니다. State Owner 조정, Composition, Context를 먼저 검토한다.

---

# 19. Tool Selection Rules

## 19.1 State Management Tool Selection

### [개념]

State Management Tool Selection은 상태 종류와 복잡도에 따라 적절한 도구를 선택하는 기준이다.

---

### [핵심]

선택 기준:

- useState
- useReducer
- Context API
- Zustand
- Redux Toolkit
- TanStack Query
- URL Search Params
- localStorage
- Form Library

---

### [실무]

선택 Flow:

```text
단일 Component 내부 상태인가?
→ useState

상태 전환 규칙이 복잡한가?
→ useReducer

여러 하위 Component에 값 공급이 필요한가?
→ Context

여러 페이지에서 가벼운 전역 상태가 필요한가?
→ Zustand

복잡하고 추적 가능한 전역 상태가 필요한가?
→ Redux Toolkit

API 서버 데이터인가?
→ TanStack Query

공유 가능한 검색 조건인가?
→ URL Search Params

복잡한 Form인가?
→ Form Library
```

---

### [FAQ]

Q. 상태관리 도구는 뭘 먼저 써야 해?

A.
먼저 상태 종류와 범위를 분류한 뒤 가장 단순한 도구부터 선택한다.

Q. Zustand와 Redux Toolkit 중 뭐가 좋아?

A.
가볍고 단순한 전역 상태는 Zustand가 편하고, 복잡한 상태 변경 추적과 팀 컨벤션이 필요하면 Redux Toolkit이 적합할 수 있다.

Q. API 데이터는 Zustand와 TanStack Query 중 뭐가 좋아?

A.
캐시, refetch, stale data 관리가 필요하면 TanStack Query가 더 적합한 경우가 많다.

---

# 20. Comparison Rules

## 20.1 Required Comparisons

### [개념]

State Management 문서는 헷갈리는 상태 개념과 도구를 비교해서 작성한다.

---

### [핵심]

필수 비교 대상:

- Local State vs Shared State
- Client State vs Server State
- UI State vs Server State
- URL State vs Component State
- Form State vs Global State
- Derived State vs Stored State
- Props Drilling vs Context
- Context vs Zustand
- Zustand vs Redux Toolkit
- Redux Toolkit vs TanStack Query
- useState vs useReducer
- Context API vs Global Store
- localStorage vs sessionStorage
- Server Cache vs Global Store
- Optimistic Update vs Refetch

---

### [실무]

예시:

| 비교     | Zustand             | Redux Toolkit          |
| -------- | ------------------- | ---------------------- |
| 성격     | 가벼운 전역 Store   | 구조화된 전역 상태관리 |
| 코드량   | 적음                | 비교적 많음            |
| 적합     | 중소 규모 전역 상태 | 복잡한 상태 흐름       |
| DevTools | 가능                | 강력함                 |
| 팀 규칙  | 유연함              | 명확한 패턴            |

---

### [FAQ]

Q. 비교 표는 왜 필요해?

A.
사용자가 자주 헷갈리는 상태관리 선택 질문에서 Retrieval Hit와 답변 정확도를 높이기 위해 필요하다.

Q. State Management 비교 문서에서 가장 중요한 것은?

A.
상태 종류, 상태 범위, 소유자, 도구 선택 기준, 잘못 선택했을 때 발생하는 문제를 함께 설명하는 것이다.

---

# 21. Checklist Rules

## 21.1 State Management Checklist

### [개념]

State Management 문서 검수 시 상태 설계 체크리스트를 사용한다.

---

### [핵심]

Checklist:

```md
- [ ] State Classification이 포함되었는가?
- [ ] Local State / Shared State / Global State 차이가 포함되었는가?
- [ ] Client State / Server State 차이가 포함되었는가?
- [ ] UI State / Form State / Auth State / URL State 기준이 포함되었는가?
- [ ] State Ownership 기준이 포함되었는가?
- [ ] Lifting State Up 기준이 포함되었는가?
- [ ] Derived State 저장 금지 기준이 포함되었는가?
- [ ] Props Drilling 판단 기준이 포함되었는가?
- [ ] Context API 사용 기준이 포함되었는가?
- [ ] useReducer 사용 기준이 포함되었는가?
- [ ] Zustand 사용 기준이 포함되었는가?
- [ ] Redux Toolkit 사용 기준이 포함되었는가?
- [ ] TanStack Query / Server State 기준이 포함되었는가?
- [ ] Persistence 주의사항이 포함되었는가?
- [ ] Auth State 주의사항이 포함되었는가?
- [ ] State Debugging Flow가 포함되었는가?
- [ ] Common Mistakes가 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 기준:

```text
Draft
→ State Classification Check
→ Ownership Check
→ Scope Check
→ Tool Selection Check
→ Anti Pattern Check
→ Troubleshooting Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

---

### [FAQ]

Q. State Management 문서 검수에서 가장 중요한 것은?

A.
상태 종류 분류, State Ownership, Server State 분리, 전역 상태 도구 선택 기준, Anti Pattern 포함 여부다.

---

# 22. Retrieval Optimization Rules

## 22.1 Keyword Rules

### [개념]

State Management 문서는 검색 매칭을 위해 핵심 키워드를 반복 허용한다.

---

### [핵심]

강조 키워드:

- State Management
- React State Management
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
- State Ownership
- Lifting State Up
- Props Drilling
- Context API
- useContext
- useReducer
- Zustand
- Redux Toolkit
- Redux Slice
- TanStack Query
- Query Cache
- queryKey
- useQuery
- useMutation
- invalidateQueries
- localStorage
- sessionStorage
- Persistence
- State Debugging
- Stale State
- Duplicate State
- Global Store
- State Anti Pattern
- Single Source of Truth

---

### [실무]

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

예:

- React 상태관리는 언제 필요해?
- State는 어디에 둬야 해?
- Local State와 Global State 차이는?
- Server State가 뭐야?
- API 데이터는 어디에 저장해?
- Props Drilling은 어떻게 해결해?
- Context는 언제 써?
- Zustand는 언제 써?
- Redux Toolkit은 언제 써?
- TanStack Query는 언제 써?
- 검색 조건은 URL에 둬야 해?
- Form State는 전역으로 둬야 해?
- Auth State는 어떻게 관리해?
- Derived State는 왜 위험해?
- 전역 Store가 너무 커졌을 때 어떻게 해?
- setState 후 값이 바로 안 바뀌는 이유는?

---

### [FAQ]

Q. 키워드 반복은 중복이야?

A.
불필요한 장문 중복은 금지지만 Retrieval 최적화를 위한 핵심 키워드 반복은 허용된다.

Q. FAQ 질문은 어떤 스타일이 좋아?

A.
실제 사용자가 검색하거나 질문할 법한 문장형 질문이 좋다.

---

# 23. Version Rules

## 23.1 Modern State Management 기준

### [개념]

State Management 문서는 Modern React 상태관리 기준으로 작성한다.

---

### [핵심]

기준:

- React 18+
- React 19 호환 고려
- Functional Component
- Hook 기반 상태관리
- useState / useReducer
- Context API
- Zustand
- Redux Toolkit
- TanStack Query
- Server State 분리
- TypeScript Ready Store
- URL State 고려
- State Classification 우선

Legacy 제외:

- Class Component setState 중심 설명
- Legacy Context API
- Redux connect 중심 설명
- mapStateToProps 중심 설명
- Redux Saga 중심 Foundation
- MobX 중심 Foundation
- 모든 API 데이터를 Redux에 저장하는 방식
- 전역 상태 만능주의
- jQuery DOM 상태 관리

---

### [실무]

실무 기준:

```text
Modern React State
→ Classify State
→ Decide Owner
→ Keep Local if Possible
→ Use URL for Shareable State
→ Use Query for Server State
→ Use Store for App-wide Client State
```

---

### [FAQ]

Q. Redux connect를 써야 해?

A.
신규 문서에서는 Redux Toolkit과 Hook 기반 사용을 우선한다. 기존 코드 유지보수에서 connect를 볼 수는 있다.

Q. 모든 API 데이터를 Redux에 저장하는 방식은 좋아?

A.
현대 React에서는 Server State 도구를 고려하는 것이 좋다. API 캐시를 Redux에 직접 모두 저장하면 관리 비용이 커질 수 있다.

---

# 24. Common Mistakes

## 24.1 State Management Common Mistakes

### [개념]

State Management 문서는 자주 발생하는 상태 설계 실수를 명확히 포함해야 한다.

---

### [핵심]

자주 발생:

- 모든 State를 App에 둠
- 모든 State를 전역 Store에 둠
- Local State를 Global State로 올림
- Server State와 Client State 혼동
- API 응답을 여러 Store에 중복 저장
- Derived State를 State로 저장
- Props Drilling을 무조건 나쁜 것으로 판단
- Context에 모든 상태를 넣음
- 자주 바뀌는 값을 큰 Context에 넣음
- Form 입력값을 전역 상태로 저장
- URL에 있어야 할 검색 조건을 Component State에만 둠
- 민감정보를 localStorage에 저장
- logout 시 Store reset 누락
- setState 직후 값이 즉시 변경된다고 오해
- stale closure 문제 무시
- query cache와 local state가 불일치
- Zustand Store를 거대하게 만듦
- Redux Toolkit을 작은 UI 상태에 과도하게 도입
- TanStack Query를 Client UI State 관리에 사용하려 함

---

### [실무]

문서 작성 시 Common Mistakes는 Troubleshooting과 연결한다.

예:

```text
문제: 화면마다 user 정보가 다르게 보임
원인: authStore, component state, query cache에 user 정보를 중복 저장
해결: user 정보의 Source of Truth를 정하고 중복 저장 제거
```

---

### [FAQ]

Q. State Management 초보가 가장 많이 하는 실수는?

A.
상태 종류를 분류하지 않고 모든 값을 전역 상태로 올리거나 API 데이터를 중복 저장하는 실수가 많다.

Q. State Management 문제는 어떻게 찾는 게 좋아?

A.
State 종류, State Owner, 사용 범위, Source of Truth, 중복 저장, Server State 여부를 순서대로 확인한다.

---

# 25. Final Goal

## 25.1 Domain Final Goal

### [개념]

State Management RAG 문서는 Frontend Agent가 상태 종류를 분류하고 적절한 위치와 도구를 선택해 유지보수 가능한 상태 흐름을 설계하도록 지원해야 한다.

---

### [핵심]

최종 목표:

- State Classification 수행
- Client State / Server State 구분
- Local State / Shared State / Global State 구분
- UI State / Form State / Auth State / URL State 구분
- State Ownership 결정
- Lifting State Up 판단
- Derived State 제거 판단
- Props Drilling 문제 분석
- Context API 적용 판단
- useReducer 적용 판단
- Zustand 적용 판단
- Redux Toolkit 적용 판단
- TanStack Query 적용 판단
- Form State 관리 기준 제공
- Auth State 관리 기준 제공
- Persistence 기준 제공
- State Debugging 수행
- State Anti Pattern 탐지
- Tool Selection 기준 제공

---

### [실무]

Agent 수행 가능 작업:

```text
User Frontend State Request
→ Identify State
→ Classify State Type
→ Decide State Owner
→ Decide State Scope
→ Choose useState / Context / Store / Query
→ Check Duplicate State
→ Check Props Drilling
→ Review Anti Patterns
→ State Management Output
```

---

### [FAQ]

Q. State Management 문서의 최종 목적은 뭐야?

A.
Frontend Agent가 상태를 무작정 전역화하지 않고 상태 종류, 소유자, 범위, 도구를 기준으로 안정적인 상태 흐름을 설계하게 만드는 것이다.

Q. 이 문서 다음에는 어떤 Domain Rules가 이어져야 해?

A.
Data Fetching & REST API Integration, Authentication Frontend Flow, Form Handling & Validation, Error Handling & Loading UX 순서로 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. State Management 문서는 왜 필요해?
A. Frontend Agent가 React 상태를 어디에 두고 어떤 도구로 관리할지 판단해야 하기 때문이다.

Q. React 상태관리는 언제 필요해?
A. Component 내부 상태를 넘어서 여러 Component나 여러 페이지가 같은 상태를 공유하거나 서버 데이터와 동기화해야 할 때 필요하다.

Q. State Classification이 뭐야?
A. 상태를 Local, Shared, Global, Server, Form, Auth, URL State처럼 성격에 따라 분류하는 작업이다.

Q. State Classification은 왜 먼저 해?
A. 상태 종류를 구분해야 useState, Context, Zustand, Redux, TanStack Query 중 적절한 관리 방법을 선택할 수 있기 때문이다.

Q. Client State와 Server State 차이는?
A. Client State는 Frontend가 소유하는 UI 상태이고 Server State는 서버가 원본을 소유하는 API 데이터다.

Q. Server State가 뭐야?
A. 서버가 원본으로 소유하고 Frontend가 조회, 캐싱, 갱신하는 데이터다.

Q. API 응답 데이터는 Client State야 Server State야?
A. 대부분 Server State다. 서버가 원본 소유자이고 Frontend는 캐시하거나 화면에 표시한다.

Q. UI State는 뭐야?
A. modal open, dropdown open, selected tab처럼 화면 표시와 상호작용을 제어하는 상태다.

Q. URL State는 뭐야?
A. 검색 조건, 필터, 페이지 번호처럼 URL path나 query string에 저장되는 상태다.

Q. 검색 조건은 State로 둬야 해 URL로 둬야 해?
A. 검색 결과를 공유하거나 새로고침 후 유지해야 하면 URL State가 적합하다.

Q. URL State에 민감정보를 넣어도 돼?
A. 안 된다. URL은 브라우저 기록, 공유 링크, 서버 로그에 남을 수 있다.

Q. State는 어디에 둬야 해?
A. 그 State를 읽고 변경하는 Component들의 가장 가까운 공통 부모에 두는 것이 기본이다.

Q. State Owner가 뭐야?
A. State를 소유하고 변경할 책임을 가지는 Component 또는 Store다.

Q. State Owner가 잘못되면 어떤 문제가 생겨?
A. Props Drilling, 중복 상태, 불필요한 Re-render, 데이터 불일치 문제가 생길 수 있다.

Q. Lifting State Up은 언제 해?
A. 여러 Component가 같은 State를 읽거나 변경 결과를 공유해야 할 때 한다.

Q. State를 올리면 무조건 좋은 거야?
A. 아니다. 필요한 범위보다 높게 올리면 Props 전달과 Re-render 범위가 커질 수 있다.

Q. Derived State가 뭐야?
A. 기존 Props, State, Server Data로부터 계산 가능한 값이다.

Q. 계산 가능한 값도 State로 저장해야 해?
A. 대부분 아니다. 기존 State나 Props로 계산 가능하면 렌더링 중 계산하는 것이 좋다.

Q. Derived State가 위험한 이유는?
A. 원본 상태가 바뀌었는데 파생 상태가 갱신되지 않아 데이터 불일치가 생길 수 있다.

Q. Local State는 언제 써?
A. 특정 Component 내부에서만 필요하고 다른 Component와 공유하지 않는 상태에 사용한다.

Q. input 값은 무조건 전역 상태로 둬야 해?
A. 아니다. 해당 Form 내부에서만 필요하면 Local State가 적합하다.

Q. Shared State는 전역 상태야?
A. 항상 전역 상태는 아니다. 특정 페이지 내부에서만 공유되면 공통 부모 State로 충분할 수 있다.

Q. 형제 Component가 같은 값을 써야 하면 어떻게 해?
A. 가장 가까운 공통 부모로 State를 올리고 Props와 callback으로 전달한다.

Q. Global State는 언제 써?
A. 여러 페이지나 깊은 Component 트리에서 반복적으로 필요한 상태일 때 사용한다.

Q. 모든 페이지에서 쓰지 않는 값도 Global State로 둬도 돼?
A. 가능은 하지만 권장하지 않는다. 필요한 범위가 좁으면 Local 또는 Shared State가 더 적합하다.

Q. 전역 Store는 어떻게 나누는 게 좋아?
A. auth, ui, notification처럼 도메인 또는 책임 기준으로 나누는 것이 좋다.

Q. Store에 API 응답을 전부 저장해도 돼?
A. 무조건 권장하지 않는다. 서버 데이터는 TanStack Query 같은 Server State 도구가 더 적합할 수 있다.

Q. Props Drilling은 무조건 나쁜 거야?
A. 아니다. 짧은 Props 전달은 자연스럽다. 깊고 반복되어 유지보수가 어려워질 때 문제가 된다.

Q. Props Drilling은 어떻게 해결해?
A. State 위치 조정, Component Composition, Context, 전역 Store, URL State를 순서대로 검토한다.

Q. Props Drilling 해결은 무조건 Context야?
A. 아니다. State 위치 조정, Component Composition, URL State, 전역 Store 등 여러 선택지를 검토해야 한다.

Q. Context API는 전역 상태관리야?
A. 전역처럼 값을 공유할 수 있지만 상태관리 라이브러리라기보다 Component Tree에 값을 공급하는 React 기능에 가깝다.

Q. Context는 언제 써?
A. Theme, Auth Summary, Language처럼 여러 하위 Component에서 필요한 값을 전달할 때 사용한다.

Q. 모든 상태를 Context에 넣어도 돼?
A. 권장하지 않는다. 자주 바뀌는 값이나 복잡한 상태는 전용 상태관리 도구가 더 적합할 수 있다.

Q. useContext를 직접 쓰면 안 돼?
A. 가능하지만 Custom Hook으로 감싸면 Provider 누락 검증과 사용 API 통일이 쉬워진다.

Q. Context를 쓰면 무조건 성능 문제가 생겨?
A. 아니다. 하지만 큰 value나 자주 바뀌는 상태를 많은 Component가 구독하면 Re-render 문제가 생길 수 있다.

Q. Context 성능 문제는 어떻게 줄여?
A. Context를 역할별로 분리하고 자주 바뀌는 상태는 전용 Store를 검토한다.

Q. useReducer는 언제 써?
A. 상태 필드가 많고 변경 규칙이 action 단위로 명확할 때 사용한다.

Q. useState와 useReducer 중 뭐가 좋아?
A. 단순 상태는 useState가 좋고, 상태 전환이 복잡하면 useReducer가 적합하다.

Q. reducer 안에서 API 호출해도 돼?
A. 권장하지 않는다. reducer는 순수 함수로 유지하고 API 호출은 외부에서 처리한다.

Q. useReducer action type은 어떻게 지어?
A. SET_KEYWORD, RESET_FORM처럼 상태 변경 의도를 드러내는 이름이 좋다.

Q. Zustand는 언제 써?
A. Context보다 action과 상태가 많고 Redux보다 가벼운 전역 상태가 필요할 때 적합하다.

Q. Zustand에 API 데이터를 전부 넣어도 돼?
A. 권장하지 않는다. 서버 데이터 캐싱은 TanStack Query 같은 Server State 도구가 더 적합할 수 있다.

Q. Zustand selector는 왜 써?
A. 필요한 상태만 구독해 불필요한 Re-render를 줄이기 위해 사용한다.

Q. Zustand Store는 어떻게 나누는 게 좋아?
A. auth, ui, notification처럼 도메인 또는 책임 기준으로 나누는 것이 좋다.

Q. Redux Toolkit은 언제 써?
A. 복잡한 전역 상태와 예측 가능한 상태 변경 흐름, DevTools 기반 추적이 필요한 큰 프로젝트에 적합하다.

Q. 작은 프로젝트에도 Redux Toolkit을 써야 해?
A. 필수는 아니다. 작은 프로젝트는 useState, Context, Zustand만으로 충분할 수 있다.

Q. Redux Toolkit에서 state를 직접 바꿔도 돼?
A. createSlice 내부 reducer에서는 Immer가 불변 업데이트로 변환하므로 mutation처럼 작성할 수 있다.

Q. Slice는 어떻게 나눠?
A. auth, ui, notification, cart처럼 도메인 책임 기준으로 나눈다.

Q. TanStack Query는 전역 상태관리야?
A. 일반적인 Client State 전역 관리 도구라기보다 Server State와 API 캐시 관리 도구에 가깝다.

Q. TanStack Query는 언제 써?
A. API 데이터 조회, 캐싱, refetch, mutation, stale data 관리가 필요할 때 사용한다.

Q. queryKey는 왜 중요해?
A. 캐시에서 데이터를 식별하고 refetch / invalidation 대상을 결정하기 때문이다.

Q. mutation 후 목록을 갱신하려면?
A. 관련 queryKey를 invalidate해서 다시 조회하도록 처리할 수 있다.

Q. Form State는 전역으로 둬야 해?
A. 대부분 아니다. Form 내부에서만 필요한 입력값은 Local State나 Form Library로 관리하는 것이 좋다.

Q. React Hook Form은 언제 써?
A. 입력 필드와 검증 규칙이 많고 touched, dirty, error 상태 관리가 복잡할 때 검토한다.

Q. Auth State는 전역 상태가 좋아?
A. 대부분 여러 페이지와 Component에서 필요하므로 전역 상태나 Context로 관리하는 경우가 많다.

Q. Frontend에서 로그인 상태만 확인하면 보안이 돼?
A. 아니다. Frontend 인증 상태는 UX용이고 실제 보안은 Backend 인증/인가가 반드시 필요하다.

Q. logout 시 어떤 상태를 초기화해야 해?
A. user, authenticated, notification, user-specific cache, 민감한 화면 상태 등을 초기화해야 한다.

Q. 모든 전역 상태를 localStorage에 저장하면 좋아?
A. 아니다. 새로고침 후 유지가 필요한 비민감 설정만 저장하는 것이 좋다.

Q. localStorage에 token을 저장해도 돼?
A. 보안 위험이 있다. 프로젝트 인증 구조와 보안 요구사항에 따라 신중히 결정해야 한다.

Q. 검색 조건은 localStorage에 저장해?
A. 공유와 뒤로가기 복원이 필요하면 localStorage보다 URL Query String이 더 적합한 경우가 많다.

Q. React State 값은 어디서 확인해?
A. React DevTools에서 Component의 Props와 State를 확인할 수 있다.

Q. 전역 상태 변경은 어떻게 추적해?
A. Redux DevTools, Zustand 로그, Store action, React DevTools를 함께 확인한다.

Q. API 데이터가 화면과 안 맞으면?
A. Network 응답, query cache, local copy, mapping 함수, State 업데이트 위치를 확인한다.

Q. 전역 Store가 너무 커졌으면 어떻게 해?
A. 각 상태의 사용 범위와 소유자를 다시 확인하고 Local State, URL State, Server State로 분리한다.

Q. 전역 상태가 많으면 왜 안 좋아?
A. 변경 영향 범위가 커지고 데이터 흐름을 추적하기 어려워지며 유지보수 비용이 증가한다.

Q. 같은 값을 여러 State에 저장하면 왜 문제야?
A. 한쪽만 갱신되면 화면마다 다른 값이 표시되는 데이터 불일치가 생길 수 있다.

Q. Single Source of Truth가 뭐야?
A. 하나의 데이터는 하나의 기준 출처에서 관리하고 나머지는 그 값을 기반으로 계산하는 원칙이다.

Q. setState 후 값이 바로 안 바뀌는 이유는?
A. React State 업데이트는 비동기적으로 처리될 수 있고 렌더링 이후 새 값이 반영되기 때문이다.

Q. 이전 State를 기준으로 업데이트할 때는 어떻게 해?
A. functional update를 사용한다. 예: `setCount((prev) => prev + 1)`.

Q. 상태관리 도구는 뭘 먼저 써야 해?
A. 먼저 상태 종류와 범위를 분류한 뒤 가장 단순한 도구부터 선택한다.

Q. Zustand와 Redux Toolkit 중 뭐가 좋아?
A. 가볍고 단순한 전역 상태는 Zustand가 편하고, 복잡한 상태 변경 추적과 팀 컨벤션이 필요하면 Redux Toolkit이 적합할 수 있다.

Q. API 데이터는 Zustand와 TanStack Query 중 뭐가 좋아?
A. 캐시, refetch, stale data 관리가 필요하면 TanStack Query가 더 적합한 경우가 많다.

Q. Redux connect를 써야 해?
A. 신규 문서에서는 Redux Toolkit과 Hook 기반 사용을 우선한다. 기존 코드 유지보수에서 connect를 볼 수는 있다.

Q. State Management 문제는 어떻게 찾는 게 좋아?
A. State 종류, State Owner, 사용 범위, Source of Truth, 중복 저장, Server State 여부를 순서대로 확인한다.

Q. State Management 다음 문서는 뭐가 좋아?
A. Data Fetching & REST API Integration, Authentication Frontend Flow, Form Handling & Validation, Error Handling & Loading UX 순서가 좋다.
