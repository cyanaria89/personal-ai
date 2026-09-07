# Frontend Code Review Part03 - State and Hooks Review

---

# 1. State Review Rules

## 1.1 State Location Review

### [개념]

State Location Review는 React 상태가 적절한 컴포넌트, Context, Store, URL, Server State 영역에 위치하는지 검토하는 과정이다.

상태 위치가 잘못되면 props drilling, 중복 state, 불필요한 렌더링, 데이터 동기화 오류가 발생한다.

Review Agent는 state가 “어디에 있어야 가장 단순하고 안전한지”를 기준으로 판단한다.

---

### [핵심]

State 위치 기준:

```text
한 컴포넌트에서만 사용
→ Local State

부모와 자식이 공유
→ 가장 가까운 공통 부모

여러 페이지에서 공유
→ Global State 또는 Context

서버에서 받아온 데이터
→ Server State Tool 또는 Custom Query Hook

URL에 남아야 하는 값
→ URL Query Params

브라우저에 유지해야 하는 값
→ Storage 연동 또는 Persist Store

전역 UI 상태
→ Global UI Store
```

상태 분류:

| State Type      | 예시                          | 권장 위치                 |
| --------------- | ----------------------------- | ------------------------- |
| UI State        | modal open, tab selected      | Local State               |
| Form State      | input value, validation error | Form Component            |
| Server State    | festival list, user detail    | React Query / Custom Hook |
| Auth State      | user, token, role             | Auth Context / Store      |
| URL State       | search keyword, page, filter  | Query String              |
| Global UI State | toast, theme, sidebar         | Global Store              |
| Persisted State | remember option, theme        | LocalStorage 연동         |

---

### [실무]

State Location Review Flow:

```text
State Identify
→ Usage Scope Check
→ Owner Component Check
→ URL Persistence Need Check
→ Server State Check
→ Global State Need Check
→ Duplication Risk Check
→ Review Decision
```

예시:

```text
검색어 keyword
→ 검색 결과 공유 필요
→ 새로고침 유지 필요
→ 뒤로가기 지원 필요
→ URL Query Params 권장
```

예시:

```text
리뷰 작성 modal open
→ 한 페이지에서만 사용
→ Local State 권장
```

예시:

```text
로그인 사용자 정보
→ 여러 페이지에서 사용
→ Auth Context 또는 Global Store 권장
```

리뷰 코멘트 예:

```text
[Medium] 검색 조건이 local state에만 저장되어 새로고침 시 초기화됩니다. 공유와 뒤로가기 지원이 필요하다면 URL query params로 관리하는 것이 좋습니다.
```

---

### [FAQ]

Q. State Location Review는 왜 필요해?
A. 상태 위치가 잘못되면 props drilling, 중복 저장, 불필요한 렌더링, 동기화 오류가 생기기 때문이다.

Q. 모든 상태를 전역 store에 넣어도 돼?
A. 권장하지 않는다. 컴포넌트 내부에서만 사용하는 상태는 local state가 더 단순하다.

Q. 검색어는 state에 둬야 해 URL에 둬야 해?
A. 공유, 새로고침 유지, 뒤로가기 지원이 필요하면 URL query params가 좋다.

Q. 서버에서 받아온 데이터는 local state에 저장하면 안 돼?
A. 가능하지만 캐싱, 재요청, loading, error 처리가 복잡하면 server state 도구나 custom query hook이 적합하다.

---

## 1.2 Local State Review

### [개념]

Local State Review는 컴포넌트 내부에서만 사용하는 상태가 적절하게 useState 또는 useReducer로 관리되는지 검토하는 과정이다.

Local State는 가장 단순한 상태 관리 방식이지만, 범위를 넘어 사용되면 구조 문제가 발생한다.

---

### [핵심]

Local State가 적합한 경우:

- modal open / close
- dropdown open / close
- tab selected
- input value
- checkbox checked
- temporary filter
- hover 또는 focus 관련 UI 상태
- 한 컴포넌트 내부에서만 사용하는 상태
- 부모 또는 전역에서 알 필요 없는 상태

Local State가 부적합한 경우:

- 여러 페이지에서 공유되는 사용자 정보
- 여러 컴포넌트가 동시에 참조하는 인증 상태
- URL에 남아야 하는 검색 조건
- 서버 데이터 캐싱이 필요한 목록
- 앱 전체 toast 상태
- 권한 정보
- 장바구니처럼 전역 공유가 필요한 상태

---

### [실무]

좋은 예:

```jsx
function ReviewModalButton() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <>
      <button type="button" onClick={() => setIsOpen(true)}>
        리뷰 작성
      </button>

      {isOpen && <ReviewModal onClose={() => setIsOpen(false)} />}
    </>
  );
}
```

문제 예:

```jsx
const [loginUser, setLoginUser] = useState(null);
```

문제 상황:

```text
loginUser를 여러 페이지에서 필요로 하지만 각 페이지가 local state로 따로 관리함
→ 인증 상태 불일치 가능
→ Auth Context 또는 Global Store 검토
```

리뷰 코멘트 예:

```text
[High] 인증 사용자 정보를 각 페이지 local state에서 개별 관리하고 있어 새로고침 또는 페이지 이동 시 인증 상태가 불일치할 수 있습니다. Auth Context 또는 전역 store로 관리하는 것이 좋습니다.
```

---

### [FAQ]

Q. Local State는 언제 사용해?
A. 한 컴포넌트 내부에서만 사용하는 UI 상태나 간단한 form 상태에 적합하다.

Q. Local State를 많이 쓰면 문제야?
A. 필요한 local state는 괜찮다. 하지만 여러 컴포넌트에서 같은 의미의 상태를 따로 관리하면 문제다.

Q. 인증 상태를 local state로 관리해도 돼?
A. 일반적으로 부적합하다. 여러 페이지에서 공유되므로 Auth Context 또는 Global Store가 적합하다.

Q. modal open 상태는 전역으로 관리해야 해?
A. 한 화면에서만 쓰는 modal이면 local state가 더 단순하다.

---

## 1.3 Global State Review

### [개념]

Global State Review는 여러 화면 또는 여러 컴포넌트에서 공유되는 상태가 Context, Zustand, Redux, Recoil 등 적절한 전역 상태 도구로 관리되는지 검토하는 과정이다.

Global State는 공유 상태에 유용하지만 남용하면 앱 구조가 복잡해진다.

---

### [핵심]

Global State가 적합한 경우:

- 로그인 사용자 정보
- 인증 여부
- 사용자 권한
- theme
- sidebar open 상태
- toast / notification UI 상태
- 다수 페이지에서 공유되는 client state
- 앱 전체 설정
- 장바구니 / 선택 항목처럼 여러 페이지에서 공유되는 상태

Global State 남용 예:

- modal 하나의 open 상태를 전역 store에 저장
- input value를 전역 store에 저장
- 한 페이지에서만 쓰는 tab 상태를 전역 store에 저장
- 서버 데이터를 cache 없이 전역 state로 직접 저장
- 파생 값을 전역 state로 중복 저장

---

### [실무]

Global State Review 기준:

```md
- [ ] 여러 페이지에서 실제로 공유되는 상태인가?
- [ ] local state로 충분한 상태가 아닌가?
- [ ] server state와 client state가 혼합되지 않았는가?
- [ ] 상태 변경 흐름이 추적 가능한가?
- [ ] persist가 필요한 상태인가?
- [ ] 불필요한 렌더링을 만들지 않는가?
- [ ] 전역 store가 도메인별로 분리되어 있는가?
```

리뷰 코멘트 예:

```text
[Medium] ReviewModal의 open 상태가 전역 store에 저장되어 있습니다. 한 페이지에서만 사용하는 UI 상태라면 local state로 관리하는 것이 더 단순합니다.
```

```text
[High] 인증 사용자 정보와 권한이 여러 컴포넌트에서 중복 local state로 관리되고 있습니다. Auth Context 또는 전역 store로 단일 출처를 만드는 것이 좋습니다.
```

---

### [FAQ]

Q. Global State는 언제 써야 해?
A. 여러 페이지나 멀리 떨어진 컴포넌트가 같은 client state를 공유할 때 사용한다.

Q. 모든 상태를 Global State로 관리하면 좋아?
A. 아니다. 상태 범위가 불필요하게 커지고 변경 추적이 어려워진다.

Q. 서버 데이터도 Global State에 넣어야 해?
A. 보통 React Query 같은 server state 도구가 더 적합하다. 직접 전역 state에 넣으면 캐싱과 동기화가 어려워질 수 있다.

Q. Auth State는 Global State로 관리해도 돼?
A. 가능하다. 로그인 여부, 사용자 정보, 권한은 전역으로 필요한 경우가 많다.

---

## 1.4 URL State Review

### [개념]

URL State Review는 검색어, 필터, 정렬, 페이지 번호처럼 URL에 남아야 하는 상태가 query string 또는 route param으로 관리되는지 검토하는 과정이다.

URL State는 새로고침, 공유, 뒤로가기, 북마크 가능성을 높인다.

---

### [핵심]

URL State가 적합한 값:

- 검색어 keyword
- 지역 filter
- 카테고리 filter
- 정렬 sort
- 페이지 page
- 탭 tab
- 상세 페이지 id
- 기간 조건 startDate / endDate
- 목록 view mode
- modal route가 필요한 경우의 modal id

URL State가 부적합한 값:

- password input
- token
- 민감 정보
- 임시 form 입력값
- 파일 객체
- 큰 객체 전체
- API 응답 전체
- Secret Key
- 개인정보

---

### [실무]

좋은 예:

```text
/festivals?keyword=music&region=seoul&page=2&sort=latest
```

Review 기준:

```md
- [ ] 새로고침 시 검색 조건이 유지되는가?
- [ ] 검색 결과 URL을 공유할 수 있는가?
- [ ] 뒤로가기 시 이전 검색 조건으로 돌아가는가?
- [ ] 민감 정보가 query string에 노출되지 않는가?
- [ ] URL 값과 화면 state가 불일치하지 않는가?
```

리뷰 코멘트 예:

```text
[Suggestion] 축제 검색 keyword와 region filter를 URL query params로 관리하면 새로고침 유지, 링크 공유, 뒤로가기 동작이 자연스러워집니다.
```

```text
[Critical] Access Token이 URL query string에 포함되어 있습니다. 브라우저 기록, 로그, 외부 referrer에 노출될 수 있으므로 즉시 제거해야 합니다.
```

---

### [FAQ]

Q. URL State는 언제 사용해?
A. 새로고침 유지, 공유, 북마크, 뒤로가기 지원이 필요한 상태에 사용한다.

Q. 검색 조건은 URL에 두는 게 좋아?
A. 검색 결과 공유와 새로고침 유지가 필요하면 URL query params가 좋다.

Q. 토큰을 URL에 넣어도 돼?
A. 안 된다. 브라우저 기록, 서버 로그, referrer에 노출될 수 있어 보안 위험이 크다.

Q. URL State와 local state가 동시에 있으면 문제야?
A. 동기화가 명확하면 가능하지만 같은 의미의 상태가 중복되면 불일치 위험이 있다.

---

# 2. State Duplication and Update Review Rules

## 2.1 State Duplication Review

### [개념]

State Duplication Review는 같은 의미의 데이터가 여러 state에 중복 저장되어 동기화 오류를 만들 가능성이 있는지 검토하는 과정이다.

기존 state에서 계산 가능한 값은 별도 state로 저장하지 않는 것이 원칙이다.

---

### [핵심]

중복 state 문제 예:

```jsx
const [users, setUsers] = useState([]);
const [userCount, setUserCount] = useState(0);
```

`userCount`가 항상 `users.length`라면 state가 아니라 파생 값으로 계산하는 것이 좋다.

좋은 예:

```jsx
const userCount = users.length;
```

중복 state 위험:

- 한쪽 state만 업데이트되어 불일치 발생
- useEffect로 동기화 코드 증가
- 불필요한 렌더링 증가
- 디버깅 난이도 증가
- 테스트 케이스 증가
- 데이터 출처가 불명확해짐

---

### [실무]

파생 값 처리 기준:

```text
기존 state에서 즉시 계산 가능
→ 변수로 계산

계산 비용이 큼
→ useMemo 검토

서버에서 내려주는 별도 의미 값
→ state 또는 response field 유지 가능

사용자 입력 원본과 가공 결과 모두 필요
→ 원본 state + 파생 값 계산 권장
```

좋은 예:

```jsx
const filteredFestivals = festivals.filter(
  (festival) => festival.region === selectedRegion,
);
```

비용이 큰 계산 예:

```jsx
const filteredFestivals = useMemo(() => {
  return festivals.filter((festival) => festival.region === selectedRegion);
}, [festivals, selectedRegion]);
```

리뷰 코멘트 예:

```text
[Medium] festivalCount가 festivals.length와 같은 의미로 별도 state에 저장되어 있습니다. 동기화 오류를 막기 위해 state 대신 파생 값으로 계산하는 것이 좋습니다.
```

---

### [FAQ]

Q. State Duplication은 왜 문제야?
A. 같은 의미의 데이터가 여러 곳에 있으면 업데이트 누락과 동기화 오류가 생기기 때문이다.

Q. 파생 값은 state로 저장해야 해?
A. 대부분 기존 state에서 계산하는 것이 좋다.

Q. useMemo는 항상 써야 해?
A. 아니다. 계산 비용이 크거나 참조 안정성이 필요한 경우에만 사용한다.

Q. 서버가 count를 따로 주면 state로 저장해도 돼?
A. 가능하다. 서버 기준 count가 별도 의미를 가지면 response data로 유지할 수 있다.

---

## 2.2 State Update Immutability Review

### [개념]

State Update Immutability Review는 React state를 직접 수정하지 않고 새 참조로 업데이트하는지 검토하는 과정이다.

React는 state 변경 감지를 참조 기반으로 수행하므로 배열이나 객체를 직접 수정하면 렌더링 문제가 발생할 수 있다.

---

### [핵심]

검토 항목:

- 기존 배열 직접 수정 금지
- 기존 객체 직접 수정 금지
- 배열 추가 시 새 배열 생성
- 배열 삭제 시 filter 사용
- 배열 수정 시 map 사용
- 객체 수정 시 spread 사용
- nested object 수정 시 필요한 깊이까지 복사
- 이전 state 기반 업데이트는 함수형 업데이트 사용
- optimistic update rollback 고려

나쁜 예:

```jsx
items.push(newItem);
setItems(items);
```

좋은 예:

```jsx
setItems((prevItems) => [...prevItems, newItem]);
```

객체 업데이트:

```jsx
setUser((prevUser) => ({
  ...prevUser,
  nickname: "newName",
}));
```

---

### [실무]

배열 업데이트 패턴:

```jsx
// add
setItems((prev) => [...prev, newItem]);

// remove
setItems((prev) => prev.filter((item) => item.id !== targetId));

// update
setItems((prev) =>
  prev.map((item) =>
    item.id === targetId ? { ...item, name: nextName } : item,
  ),
);
```

리뷰 코멘트 예:

```text
[High] items 배열을 push로 직접 수정한 뒤 같은 참조를 setState하고 있습니다. React가 변경을 감지하지 못할 수 있으므로 새 배열을 만들어 업데이트해야 합니다.
```

---

### [FAQ]

Q. 배열에 push하고 setState 하면 안 돼?
A. 권장하지 않는다. 기존 배열을 직접 수정하면 React가 변경을 안정적으로 감지하지 못할 수 있다.

Q. 객체 state는 어떻게 수정해야 해?
A. 기존 객체를 직접 수정하지 말고 spread 등으로 새 객체를 만들어 업데이트한다.

Q. nested object는 어떻게 수정해?
A. 변경되는 깊이까지 새 객체를 만들어 불변성을 유지해야 한다.

Q. 직접 수정이 항상 화면 오류로 이어져?
A. 항상은 아니지만 렌더링 누락, 예측 어려운 버그, memoization 오류를 만들 수 있다.

---

## 2.3 Functional Update Review

### [개념]

Functional Update Review는 이전 state 값을 기준으로 다음 state를 계산할 때 함수형 업데이트를 사용하는지 검토하는 과정이다.

React state update는 비동기적으로 처리될 수 있으므로 이전 값에 의존하는 업데이트는 `setState(prev => next)` 형태가 안전하다.

---

### [핵심]

함수형 업데이트가 필요한 경우:

- counter 증가 / 감소
- 배열에 항목 추가
- 배열에서 항목 삭제
- toggle 처리
- 연속 클릭 가능성 있음
- 비동기 처리 후 이전 state 참조
- optimistic update
- 이전 form value 기반 업데이트

위험 예:

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

### [실무]

toggle 예:

```jsx
setIsOpen((prevIsOpen) => !prevIsOpen);
```

배열 추가 예:

```jsx
setMessages((prevMessages) => [...prevMessages, newMessage]);
```

form object 업데이트 예:

```jsx
setFormValues((prevValues) => ({
  ...prevValues,
  email: nextEmail,
}));
```

리뷰 코멘트 예:

```text
[Medium] 이전 state를 기준으로 messages를 업데이트하고 있지만 현재 closure의 messages 값을 직접 참조하고 있습니다. 연속 이벤트에서 누락될 수 있으므로 함수형 업데이트를 사용하는 것이 안전합니다.
```

---

### [FAQ]

Q. 함수형 업데이트는 언제 필요해?
A. 이전 state 값을 기준으로 다음 state를 계산할 때 필요하다.

Q. setCount(count + 1)은 항상 문제야?
A. 단일 업데이트에서는 동작할 수 있지만 연속 업데이트나 비동기 상황에서는 누락될 수 있다.

Q. toggle 상태는 어떻게 업데이트해야 해?
A. `setIsOpen(prev => !prev)` 형태가 안전하다.

Q. 배열에 새 항목을 추가할 때 함수형 업데이트가 좋아?
A. 이전 배열에 의존하므로 `setItems(prev => [...prev, newItem])` 형태가 안전하다.

---

## 2.4 Derived State Review

### [개념]

Derived State Review는 기존 props 또는 state에서 계산 가능한 값을 별도 state로 저장하지 않고 안전하게 계산하는지 검토하는 과정이다.

Derived State를 잘못 관리하면 stale data와 불필요한 useEffect가 증가한다.

---

### [핵심]

Derived State로 계산 가능한 값:

- 배열 길이
- 필터링 결과
- 정렬 결과
- 합계
- 선택 여부
- 권한 기반 표시 여부
- form submit 가능 여부
- error 존재 여부
- 빈 결과 여부

나쁜 예:

```jsx
const [filteredItems, setFilteredItems] = useState([]);

useEffect(() => {
  setFilteredItems(items.filter((item) => item.active));
}, [items]);
```

좋은 예:

```jsx
const filteredItems = items.filter((item) => item.active);
```

비용이 큰 경우:

```jsx
const filteredItems = useMemo(() => {
  return items.filter((item) => item.active);
}, [items]);
```

---

### [실무]

Derived State Review 기준:

```md
- [ ] 기존 state에서 계산 가능한 값을 별도 state로 저장하지 않았는가?
- [ ] 단순 계산을 useEffect로 동기화하지 않았는가?
- [ ] submit 가능 여부를 state로 중복 저장하지 않았는가?
- [ ] 필터링 / 정렬 결과가 원본과 불일치하지 않는가?
- [ ] useMemo가 필요한 계산인지 판단했는가?
```

리뷰 코멘트 예:

```text
[Medium] canSubmit은 formValues와 validation result에서 계산 가능한 값인데 별도 state로 저장되어 있습니다. 동기화 오류를 막기 위해 파생 값으로 계산하는 것이 좋습니다.
```

---

### [FAQ]

Q. Derived State는 뭐야?
A. 기존 props나 state에서 계산 가능한 값이다.

Q. Derived State를 별도 state로 저장하면 왜 문제야?
A. 원본 값과 동기화되지 않으면 stale data 또는 UI 불일치가 발생할 수 있다.

Q. 단순 필터링 결과를 useEffect로 state에 저장해도 돼?
A. 대부분 불필요하다. 렌더링 중 계산하거나 비용이 크면 useMemo를 사용한다.

Q. submit 가능 여부는 state로 저장해야 해?
A. 대부분 form value와 validation 결과에서 계산하는 것이 좋다.

---

# 3. React Hooks Review Rules

## 3.1 Hook Rule Review

### [개념]

Hook Rule Review는 React Hook 사용 규칙을 지키는지 검토하는 과정이다.

Hook 호출 순서가 렌더링마다 달라지면 React가 state와 effect를 올바르게 연결할 수 없다.

---

### [핵심]

Hook 규칙:

- 컴포넌트 최상위에서만 호출
- Custom Hook 최상위에서만 호출
- 조건문 안에서 호출 금지
- 반복문 안에서 호출 금지
- 중첩 함수 안에서 호출 금지
- 일반 함수에서 호출 금지
- return 이후 호출 금지
- React Component 또는 Custom Hook에서만 호출
- Hook 호출 순서 유지

나쁜 예:

```jsx
if (isLoggedIn) {
  useEffect(() => {
    fetchUser();
  }, []);
}
```

좋은 예:

```jsx
useEffect(() => {
  if (!isLoggedIn) return;

  fetchUser();
}, [isLoggedIn]);
```

---

### [실무]

Hook Rule Review 체크리스트:

```md
- [ ] Hook이 component 최상위에서 호출되는가?
- [ ] 조건문 안에서 Hook을 호출하지 않는가?
- [ ] 반복문 안에서 Hook을 호출하지 않는가?
- [ ] 일반 함수에서 Hook을 호출하지 않는가?
- [ ] early return보다 Hook 호출이 먼저 위치하는가?
- [ ] Custom Hook 이름이 use로 시작하는가?
```

리뷰 코멘트 예:

```text
[Critical] useEffect가 조건문 내부에서 호출되고 있습니다. Hook 호출 순서가 렌더링마다 달라질 수 있으므로 Hook은 최상위에서 호출하고 내부에서 조건을 처리해야 합니다.
```

---

### [FAQ]

Q. 조건문 안에서 useEffect를 호출해도 돼?
A. 안 된다. Hook 호출 순서가 렌더링마다 달라질 수 있다.

Q. 조건이 있을 때는 어떻게 해?
A. Hook은 최상위에서 호출하고 Hook 내부에서 조건을 처리한다.

Q. 반복문 안에서 Hook을 호출해도 돼?
A. 안 된다. Hook 호출 개수가 렌더링마다 달라질 수 있다.

Q. Custom Hook 이름은 꼭 use로 시작해야 해?
A. 그렇다. React Hook 규칙과 lint 검사를 위해 `use` prefix가 필요하다.

---

## 3.2 useEffect Dependency Review

### [개념]

useEffect Dependency Review는 useEffect의 dependency array가 side effect에서 사용하는 값과 일치하는지 검토하는 과정이다.

의존성이 누락되면 stale closure가 발생하고, 불필요한 의존성이 있으면 무한 루프나 중복 요청이 발생할 수 있다.

---

### [핵심]

검토 항목:

- dependency array 누락 여부
- effect 내부에서 사용하는 값이 dependency에 포함되었는가?
- 불필요한 dependency가 포함되지 않았는가?
- 매 렌더링마다 새로 생성되는 객체 / 배열 / 함수가 dependency에 들어가지 않았는가?
- API 호출 중복 위험이 없는가?
- cleanup이 필요한 effect에 cleanup이 있는가?
- ESLint exhaustive-deps warning을 무시하지 않았는가?

위험 예:

```jsx
useEffect(() => {
  fetchFestival(festivalId);
}, []);
```

`festivalId`가 변경될 수 있으면 dependency에 포함해야 한다.

좋은 예:

```jsx
useEffect(() => {
  fetchFestival(festivalId);
}, [festivalId]);
```

---

### [실무]

dependency 문제 Flow:

```text
Effect Purpose Identify
→ Used Variables Check
→ Dependency Array Check
→ Function Reference Stability Check
→ Object / Array Dependency Check
→ Infinite Loop Risk Check
→ Duplicate Request Check
```

무한 루프 예:

```jsx
const params = { keyword };

useEffect(() => {
  fetchFestivals(params);
}, [params]);
```

문제:

```text
params 객체가 매 렌더링마다 새로 생성됨
→ dependency가 매번 변경됨
→ effect 반복 실행 가능
```

개선 예:

```jsx
useEffect(() => {
  fetchFestivals({ keyword });
}, [keyword]);
```

리뷰 코멘트 예:

```text
[High] useEffect dependency에 매 렌더링마다 새로 생성되는 params 객체가 포함되어 API 요청이 반복될 수 있습니다. primitive dependency로 분리하거나 useMemo를 검토해야 합니다.
```

---

### [FAQ]

Q. useEffect dependency warning은 무시해도 돼?
A. 권장하지 않는다. 의존성 누락은 stale closure와 예측 어려운 버그를 만들 수 있다.

Q. dependency array를 빈 배열로 두면 한 번만 실행돼?
A. mount 시 한 번 실행된다. 하지만 effect 내부에서 props나 state를 사용하면 stale 값 문제가 생길 수 있다.

Q. 객체를 dependency에 넣으면 왜 문제가 될 수 있어?
A. 객체가 매 렌더링마다 새로 생성되면 dependency가 계속 변경되어 effect가 반복 실행될 수 있다.

Q. 함수를 dependency에 넣어야 해?
A. effect 내부에서 사용하는 함수는 dependency 고려 대상이다. 필요하면 useCallback 또는 effect 내부 선언을 검토한다.

---

## 3.3 useEffect Responsibility Review

### [개념]

useEffect Responsibility Review는 useEffect가 side effect 처리에만 사용되고, 단순 계산이나 state 동기화에 남용되지 않는지 검토하는 과정이다.

useEffect는 렌더링 결과로 발생하는 외부 효과를 처리하는 도구이지 모든 로직을 넣는 장소가 아니다.

---

### [핵심]

useEffect가 적합한 경우:

- API 호출
- 구독 설정
- 이벤트 리스너 등록
- 타이머 설정
- 외부 라이브러리 연동
- document title 변경
- WebSocket 연결
- cleanup이 필요한 외부 자원 관리

useEffect가 부적합한 경우:

- 단순 값 계산
- props를 state에 복사
- 렌더링 중 계산 가능한 값 저장
- 이벤트 핸들러에서 처리 가능한 로직
- validation result 중복 저장
- filter result 중복 저장
- derived state 동기화

---

### [실무]

나쁜 예:

```jsx
useEffect(() => {
  setFilteredItems(items.filter((item) => item.active));
}, [items]);
```

좋은 예:

```jsx
const filteredItems = items.filter((item) => item.active);
```

나쁜 예:

```jsx
useEffect(() => {
  setFullName(`${firstName} ${lastName}`);
}, [firstName, lastName]);
```

좋은 예:

```jsx
const fullName = `${firstName} ${lastName}`;
```

리뷰 코멘트 예:

```text
[Medium] useEffect로 filteredItems state를 동기화하고 있지만 items에서 계산 가능한 파생 값입니다. state와 effect를 제거하고 렌더링 중 계산하는 것이 더 단순합니다.
```

---

### [FAQ]

Q. useEffect는 언제 사용해야 해?
A. API 호출, 이벤트 리스너, 구독, 타이머, 외부 라이브러리 연동 같은 side effect 처리에 사용한다.

Q. 단순 계산에 useEffect를 써도 돼?
A. 권장하지 않는다. 렌더링 중 계산하거나 비용이 크면 useMemo를 사용한다.

Q. props를 state로 복사하려고 useEffect를 써도 돼?
A. 대부분 불필요하다. 특별한 초기화 목적이 아니라면 props를 직접 사용하거나 파생 값으로 계산한다.

Q. useEffect를 많이 쓰면 문제야?
A. 필요한 effect는 괜찮지만 단순 계산과 state 동기화에 남용하면 복잡도와 버그 위험이 커진다.

---

## 3.4 useEffect Cleanup Review

### [개념]

useEffect Cleanup Review는 effect에서 등록한 외부 자원, 이벤트, 타이머, 구독, 비동기 작업이 적절히 정리되는지 검토하는 과정이다.

cleanup이 누락되면 memory leak, 중복 이벤트, unmounted component update 문제가 발생할 수 있다.

---

### [핵심]

cleanup이 필요한 경우:

- window event listener
- document event listener
- setInterval
- setTimeout
- WebSocket 연결
- subscription
- external library instance
- AbortController가 필요한 fetch
- observer
- scroll listener
- resize listener

나쁜 예:

```jsx
useEffect(() => {
  window.addEventListener("resize", handleResize);
}, []);
```

좋은 예:

```jsx
useEffect(() => {
  window.addEventListener("resize", handleResize);

  return () => {
    window.removeEventListener("resize", handleResize);
  };
}, []);
```

---

### [실무]

Timer cleanup 예:

```jsx
useEffect(() => {
  const timerId = setInterval(() => {
    refetch();
  }, 5000);

  return () => {
    clearInterval(timerId);
  };
}, [refetch]);
```

fetch abort 예:

```jsx
useEffect(() => {
  const controller = new AbortController();

  fetch("/api/festivals", { signal: controller.signal });

  return () => {
    controller.abort();
  };
}, []);
```

리뷰 코멘트 예:

```text
[High] useEffect에서 window resize 이벤트를 등록하지만 cleanup에서 제거하지 않습니다. 페이지 이동 후에도 listener가 남아 중복 실행과 memory leak이 발생할 수 있습니다.
```

---

### [FAQ]

Q. useEffect cleanup은 언제 필요해?
A. 이벤트 리스너, 타이머, 구독, WebSocket, 외부 리소스를 등록할 때 필요하다.

Q. API fetch에도 cleanup이 필요해?
A. 컴포넌트 unmount 후 응답이 올 수 있는 상황이면 AbortController를 검토하는 것이 좋다.

Q. cleanup이 없으면 어떤 문제가 생겨?
A. memory leak, 중복 이벤트 실행, unmounted component update 문제가 생길 수 있다.

Q. 모든 useEffect에 cleanup이 필요해?
A. 아니다. 외부 자원을 등록하거나 취소 가능한 작업을 시작한 경우에 필요하다.

---

# 4. Custom Hook Review Rules

## 4.1 Custom Hook Responsibility Review

### [개념]

Custom Hook Responsibility Review는 재사용 가능한 상태 로직, side effect, API 흐름이 적절히 custom hook으로 분리되었는지 검토하는 과정이다.

Custom Hook은 컴포넌트의 책임을 줄이고 로직 재사용성과 테스트 가능성을 높인다.

---

### [핵심]

Custom Hook 적합 상황:

- 여러 컴포넌트에서 반복되는 로직
- API 호출 로직
- Form 상태 로직
- Modal 제어 로직
- LocalStorage 연동
- 권한 체크
- Pagination 로직
- Infinite Scroll 로직
- WebSocket 연결
- debounce / throttle 로직
- file upload 상태 관리

Custom Hook 부적합 상황:

- 한 컴포넌트에서만 쓰는 단순 상태
- UI markup이 대부분인 로직
- 추상화 기준이 불명확한 로직
- 너무 많은 책임을 하나의 hook에 넣는 경우

---

### [실무]

좋은 예:

```jsx
function useModal() {
  const [isOpen, setIsOpen] = useState(false);

  const open = () => setIsOpen(true);
  const close = () => setIsOpen(false);

  return { isOpen, open, close };
}
```

API hook 예:

```jsx
function useFestivalDetail(festivalId) {
  const [festival, setFestival] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!festivalId) return;

    async function fetchFestival() {
      setIsLoading(true);
      setError(null);

      try {
        const response = await festivalApi.getFestivalDetail(festivalId);
        setFestival(response.data);
      } catch (error) {
        setError(error);
      } finally {
        setIsLoading(false);
      }
    }

    fetchFestival();
  }, [festivalId]);

  return { festival, isLoading, error };
}
```

리뷰 코멘트 예:

```text
[Suggestion] 여러 페이지에서 modal open / close 로직이 반복됩니다. useModal custom hook으로 분리하면 중복을 줄일 수 있습니다.
```

---

### [FAQ]

Q. Custom Hook은 언제 만들어?
A. 여러 컴포넌트에서 반복되는 상태 로직, API 호출, form 처리, modal 제어를 분리할 때 만든다.

Q. Custom Hook 이름은 꼭 use로 시작해야 해?
A. 그렇다. React Hook 규칙과 lint 검사를 위해 `use` prefix가 필요하다.

Q. 한 번만 쓰는 로직도 Custom Hook으로 분리해야 해?
A. 반드시 그럴 필요는 없다. 복잡도가 높거나 테스트 가능성을 높이고 싶을 때 검토한다.

Q. Custom Hook에 UI를 반환해도 돼?
A. 일반적으로 hook은 상태와 로직을 반환하고 UI는 component에서 렌더링하는 것이 좋다.

---

## 4.2 Custom Hook Return Review

### [개념]

Custom Hook Return Review는 custom hook이 반환하는 값과 함수가 명확하고 사용하기 쉬운 구조인지 검토하는 과정이다.

반환 구조가 불명확하면 hook 사용 컴포넌트의 가독성과 안정성이 떨어진다.

---

### [핵심]

Custom Hook 반환 기준:

- 반환 값 이름이 명확함
- loading / error / data 상태가 포함됨
- refetch 또는 action 함수가 필요 시 제공됨
- 배열 반환과 객체 반환을 상황에 맞게 사용
- 과도하게 많은 값을 반환하지 않음
- setter를 무분별하게 외부로 노출하지 않음
- 내부 구현 세부사항을 과하게 노출하지 않음

객체 반환이 적합한 경우:

```text
반환 값이 많음
→ 이름 기반 접근 필요
→ 순서 실수 방지
```

배열 반환이 적합한 경우:

```text
useState처럼 짧고 관례가 강함
→ [value, setValue]
```

---

### [실무]

좋은 예:

```jsx
const { festival, isLoading, error, refetch } = useFestivalDetail(festivalId);
```

나쁜 예:

```jsx
const result = useFestivalDetail(festivalId);
```

문제:

```text
result.data, result.value, result.item 등 의미가 불명확하면 사용처에서 혼란 발생
```

setter 과다 노출 예:

```jsx
return {
  festival,
  setFestival,
  isLoading,
  setIsLoading,
  error,
  setError,
};
```

개선 방향:

```jsx
return {
  festival,
  isLoading,
  error,
  refetch,
};
```

리뷰 코멘트 예:

```text
[Medium] useFestivalDetail hook이 내부 setState 함수를 모두 외부로 노출하고 있습니다. 외부에서 상태를 임의 변경할 수 있어 흐름 추적이 어려우므로 필요한 action 함수만 제공하는 것이 좋습니다.
```

---

### [FAQ]

Q. Custom Hook은 객체로 반환하는 게 좋아 배열로 반환하는 게 좋아?
A. 반환 값이 많거나 의미가 중요한 경우 객체 반환이 안전하다. useState처럼 관례가 명확하면 배열도 가능하다.

Q. Custom Hook에서 setter를 그대로 반환해도 돼?
A. 가능하지만 남용하면 상태 변경 흐름이 흩어진다. 필요한 action 함수로 감싸는 것이 좋다.

Q. loading과 error도 hook에서 반환해야 해?
A. API hook이라면 대부분 반환해야 한다. 컴포넌트가 UX 상태를 표시해야 하기 때문이다.

Q. refetch 함수는 언제 반환해?
A. 사용자가 재시도하거나 수동 갱신할 수 있어야 하는 데이터 조회 hook에서 유용하다.

---

## 4.3 Custom Hook Dependency Review

### [개념]

Custom Hook Dependency Review는 custom hook 내부의 useEffect, useCallback, useMemo dependency가 안전하게 관리되는지 검토하는 과정이다.

Custom Hook은 여러 컴포넌트에서 재사용되므로 dependency 오류가 전파될 위험이 크다.

---

### [핵심]

검토 항목:

- hook parameter가 dependency에 포함되는가?
- 내부 callback이 stale closure를 만들지 않는가?
- 외부에서 전달한 callback을 안전하게 처리하는가?
- API 요청 dependency가 명확한가?
- 반환 함수의 참조 안정성이 필요한가?
- cleanup이 필요한 effect가 정리되는가?
- hook이 조건부로 다른 Hook을 호출하지 않는가?

---

### [실무]

위험 예:

```jsx
function useFestivalDetail(festivalId) {
  useEffect(() => {
    fetchFestival(festivalId);
  }, []);
}
```

문제:

```text
festivalId가 바뀌어도 effect가 다시 실행되지 않음
```

개선 예:

```jsx
function useFestivalDetail(festivalId) {
  useEffect(() => {
    if (!festivalId) return;

    fetchFestival(festivalId);
  }, [festivalId]);
}
```

외부 callback 사용 예:

```jsx
function useOutsideClick(ref, onOutsideClick) {
  useEffect(() => {
    function handleClick(event) {
      if (ref.current && !ref.current.contains(event.target)) {
        onOutsideClick();
      }
    }

    document.addEventListener("mousedown", handleClick);

    return () => {
      document.removeEventListener("mousedown", handleClick);
    };
  }, [ref, onOutsideClick]);
}
```

리뷰 코멘트 예:

```text
[High] custom hook 내부 useEffect가 festivalId를 사용하지만 dependency array가 비어 있습니다. festivalId 변경 시 이전 데이터를 계속 보여줄 수 있으므로 dependency에 포함해야 합니다.
```

---

### [FAQ]

Q. Custom Hook 내부 dependency도 리뷰해야 해?
A. 해야 한다. Custom Hook은 재사용되므로 dependency 오류가 여러 화면에 전파될 수 있다.

Q. hook parameter는 dependency에 넣어야 해?
A. effect 내부에서 사용하고 변경 가능성이 있으면 dependency에 포함해야 한다.

Q. 외부 callback을 dependency에 넣으면 effect가 자주 실행되지 않아?
A. 가능하다. 필요하면 호출부에서 useCallback으로 안정화하거나 hook 설계를 조정한다.

Q. Custom Hook에서도 조건부 Hook 호출이 금지야?
A. 그렇다. Custom Hook 내부에서도 Hook 호출 순서는 항상 같아야 한다.

---

# 5. State and Hooks Performance Review Rules

## 5.1 useMemo Review

### [개념]

useMemo Review는 비용이 큰 계산이나 참조 안정성이 필요한 값을 적절히 memoization하는지 검토하는 과정이다.

useMemo는 성능 최적화 도구이지만 남용하면 코드 복잡도만 증가할 수 있다.

---

### [핵심]

useMemo가 적합한 경우:

- 큰 배열 필터링
- 큰 배열 정렬
- 비용이 큰 계산
- memoized child component에 전달하는 객체
- dependency가 바뀔 때만 계산해야 하는 값
- 복잡한 derived data

useMemo가 불필요한 경우:

- 단순 문자열 조합
- 단순 boolean 계산
- 작은 배열의 간단한 map / filter
- 매 렌더링 비용이 거의 없는 계산
- 성능 문제가 확인되지 않은 경우

---

### [실무]

적절한 예:

```jsx
const filteredFestivals = useMemo(() => {
  return festivals.filter((festival) => {
    return festival.region === selectedRegion;
  });
}, [festivals, selectedRegion]);
```

불필요한 예:

```jsx
const fullName = useMemo(() => {
  return `${firstName} ${lastName}`;
}, [firstName, lastName]);
```

리뷰 기준:

```md
- [ ] 실제 계산 비용이 있는가?
- [ ] dependency가 정확한가?
- [ ] memoization으로 얻는 이점이 있는가?
- [ ] useMemo 남용으로 코드가 복잡해지지 않았는가?
```

리뷰 코멘트 예:

```text
[Suggestion] 축제 목록이 커질 경우 filter와 sort 계산이 매 렌더링마다 반복될 수 있습니다. 목록 크기가 커지는 요구사항이라면 useMemo 적용을 검토할 수 있습니다.
```

---

### [FAQ]

Q. useMemo는 항상 써야 해?
A. 아니다. 계산 비용이 크거나 참조 안정성이 필요한 경우에만 사용한다.

Q. 단순 문자열 조합에도 useMemo가 필요해?
A. 필요하지 않다. 오히려 코드가 복잡해질 수 있다.

Q. useMemo를 쓰면 항상 성능이 좋아져?
A. 아니다. memoization 자체에도 비용이 있으므로 실제 이점이 있을 때 사용해야 한다.

Q. useMemo dependency도 리뷰해야 해?
A. 해야 한다. dependency가 틀리면 stale value 또는 불필요한 재계산이 발생한다.

---

## 5.2 useCallback Review

### [개념]

useCallback Review는 함수 참조 안정성이 필요한 상황에서 useCallback을 적절히 사용하는지 검토하는 과정이다.

useCallback은 모든 함수에 붙이는 것이 아니라 memoized child, dependency 안정성, event listener cleanup 등 참조 안정성이 필요할 때 사용한다.

---

### [핵심]

useCallback이 적합한 경우:

- React.memo child component에 handler 전달
- custom hook dependency로 callback 전달
- useEffect dependency 안정화 필요
- event listener 등록 / 제거에 같은 함수 참조 필요
- 큰 리스트의 item handler 최적화가 필요한 경우

useCallback이 불필요한 경우:

- 일반 button onClick에 단순 함수 전달
- child component가 memoized 되어 있지 않음
- 함수 생성 비용이 의미 없음
- dependency가 자주 바뀌어 효과가 없음
- 코드 복잡도만 증가하는 경우

---

### [실무]

적절한 예:

```jsx
const handleFavoriteClick = useCallback(
  (festivalId) => {
    toggleFavorite(festivalId);
  },
  [toggleFavorite],
);
```

주의 예:

```jsx
const handleClick = useCallback(() => {
  console.log("click");
}, []);
```

Review 기준:

```md
- [ ] useCallback이 필요한 이유가 있는가?
- [ ] dependency가 정확한가?
- [ ] stale closure 위험이 없는가?
- [ ] child memoization과 함께 의미 있게 사용되는가?
- [ ] 불필요하게 모든 handler를 감싸지 않았는가?
```

리뷰 코멘트 예:

```text
[Low] 모든 이벤트 핸들러에 useCallback이 적용되어 있지만 memoized child에 전달되지 않습니다. 성능 이점이 크지 않고 코드 복잡도만 증가할 수 있습니다.
```

---

### [FAQ]

Q. useCallback은 모든 함수에 써야 해?
A. 아니다. 참조 안정성이 필요한 경우에만 사용한다.

Q. React.memo를 쓰지 않으면 useCallback은 의미 없어?
A. 대체로 이점이 줄어든다. 다만 effect dependency나 custom hook dependency 안정화에는 의미가 있을 수 있다.

Q. useCallback dependency가 틀리면 어떻게 돼?
A. stale closure로 이전 값을 참조하거나 함수가 불필요하게 재생성될 수 있다.

Q. useCallback을 많이 쓰면 성능이 좋아져?
A. 항상 그렇지 않다. 불필요한 useCallback은 코드 복잡도와 메모리 비용을 늘릴 수 있다.

---

## 5.3 useReducer Review

### [개념]

useReducer Review는 복잡한 상태 전환 로직이 useState보다 useReducer로 관리되는 것이 적절한지 검토하는 과정이다.

여러 state가 서로 연관되어 있고 action 기반 전환이 명확한 경우 useReducer가 유지보수에 도움이 된다.

---

### [핵심]

useReducer가 적합한 경우:

- form 상태가 복잡함
- 여러 state가 함께 변경됨
- 상태 전환 종류가 명확함
- loading / success / error 상태 전환이 복잡함
- undo / redo 같은 action history가 필요함
- reducer를 테스트하고 싶음

useReducer가 부적합한 경우:

- 단순 boolean toggle
- 단순 input 하나
- action 종류가 거의 없음
- reducer가 오히려 boilerplate만 증가
- 상태 구조가 불필요하게 복잡해짐

---

### [실무]

예시:

```jsx
const initialState = {
  value: "",
  error: null,
  isSubmitting: false,
};

function reducer(state, action) {
  switch (action.type) {
    case "CHANGE_VALUE":
      return { ...state, value: action.payload };
    case "SUBMIT_START":
      return { ...state, isSubmitting: true, error: null };
    case "SUBMIT_ERROR":
      return { ...state, isSubmitting: false, error: action.payload };
    case "SUBMIT_SUCCESS":
      return { ...state, isSubmitting: false };
    default:
      return state;
  }
}
```

리뷰 코멘트 예:

```text
[Suggestion] 이 Form은 value, validation error, submit state가 함께 변경됩니다. 상태 전환이 더 복잡해지면 useReducer로 action 기반 관리하는 것을 검토할 수 있습니다.
```

---

### [FAQ]

Q. useReducer는 언제 써?
A. 여러 상태가 연관되어 있고 상태 전환이 action 단위로 명확할 때 사용한다.

Q. useState보다 useReducer가 항상 좋아?
A. 아니다. 단순 상태는 useState가 더 간단하다.

Q. reducer는 테스트하기 좋아?
A. 좋다. 입력 state와 action에 따른 output state를 pure function으로 검증할 수 있다.

Q. form은 무조건 useReducer로 관리해야 해?
A. 아니다. 작은 form은 useState로 충분하다.

---

# 6. State and Hooks Review Checklist

## 6.1 State Review Checklist

### [개념]

State Review Checklist는 Review Agent가 프론트엔드 state 구조를 검토할 때 사용하는 최종 점검 목록이다.

상태 위치, 중복, 업데이트 방식, 파생 값, URL 상태, 전역 상태 남용을 빠르게 검토한다.

---

### [핵심]

State Review Checklist:

```md
## State Location

- [ ] state 사용 범위가 명확한가?
- [ ] 한 컴포넌트에서만 쓰는 상태는 local state인가?
- [ ] 여러 페이지에서 공유되는 상태는 Context 또는 Global Store인가?
- [ ] 서버 데이터는 server state로 관리되는가?
- [ ] 검색 조건, 페이지 번호, 필터는 URL state가 필요한가?

## Duplication

- [ ] 같은 의미의 state가 중복 저장되지 않았는가?
- [ ] 기존 state에서 계산 가능한 값이 별도 state로 저장되지 않았는가?
- [ ] 파생 값이 useEffect로 불필요하게 동기화되지 않는가?

## Update

- [ ] 배열 / 객체 state를 직접 수정하지 않는가?
- [ ] 새 참조로 state를 업데이트하는가?
- [ ] 이전 state 기반 업데이트에 함수형 업데이트를 사용하는가?
- [ ] optimistic update rollback이 필요한가?

## Global State

- [ ] 전역 상태가 실제로 여러 화면에서 필요한가?
- [ ] local state로 충분한 상태가 전역 store에 있지 않은가?
- [ ] server state와 client state가 섞이지 않았는가?

## URL State

- [ ] 새로고침 유지가 필요한 값이 URL에 반영되는가?
- [ ] URL에 민감 정보가 노출되지 않는가?
- [ ] URL 값과 화면 state가 불일치하지 않는가?
```

---

### [실무]

State Review 우선순위:

```text
Auth State Safety
→ Server State Consistency
→ State Duplication
→ Immutability
→ URL State Need
→ Global State Overuse
→ Derived State Simplification
```

리뷰 코멘트 우선순위 판단:

```text
인증 상태 불일치
→ High

직접 state mutation으로 렌더링 오류 가능
→ High

파생 값 중복 저장
→ Medium

전역 상태 남용
→ Medium

URL state 개선
→ Suggestion 또는 Medium
```

---

### [FAQ]

Q. State Review에서 가장 먼저 볼 것은 뭐야?
A. 인증 상태, 서버 데이터, 중복 state, 직접 mutation 여부를 먼저 본다.

Q. 직접 state mutation은 어떤 우선순위야?
A. 렌더링 오류 가능성이 크면 High로 판단할 수 있다.

Q. 전역 상태 남용은 어떤 우선순위야?
A. 보통 Medium이다. 구조 복잡도와 유지보수성에 영향을 준다.

Q. URL State 개선은 어떤 우선순위야?
A. 요구사항이면 Medium 이상이고, 편의 개선이면 Suggestion이다.

---

## 6.2 Hooks Review Checklist

### [개념]

Hooks Review Checklist는 Review Agent가 React Hook 사용을 검토할 때 사용하는 최종 점검 목록이다.

Hook 규칙, dependency, useEffect 책임, cleanup, custom hook 설계, memoization 남용을 빠르게 검토한다.

---

### [핵심]

Hooks Review Checklist:

```md
## Hook Rules

- [ ] Hook이 컴포넌트 최상위에서 호출되는가?
- [ ] 조건문 안에서 Hook을 호출하지 않는가?
- [ ] 반복문 안에서 Hook을 호출하지 않는가?
- [ ] 일반 함수에서 Hook을 호출하지 않는가?
- [ ] Custom Hook 이름이 use로 시작하는가?

## useEffect

- [ ] dependency array가 정확한가?
- [ ] effect 내부에서 사용하는 값이 dependency에 포함되는가?
- [ ] 매 렌더링마다 새로 생성되는 객체 / 배열 / 함수 때문에 반복 실행되지 않는가?
- [ ] 단순 계산을 useEffect로 처리하지 않는가?
- [ ] props를 state로 불필요하게 복사하지 않는가?
- [ ] cleanup이 필요한 effect에 cleanup이 있는가?

## Custom Hook

- [ ] 재사용 가능한 로직이 적절히 custom hook으로 분리되었는가?
- [ ] custom hook이 너무 많은 책임을 갖지 않는가?
- [ ] 반환 값 이름이 명확한가?
- [ ] 내부 setter를 과도하게 노출하지 않는가?
- [ ] loading / error / data 상태가 필요한 경우 반환되는가?

## Memoization

- [ ] useMemo가 실제 계산 비용 또는 참조 안정성을 위해 사용되는가?
- [ ] useCallback이 실제 참조 안정성을 위해 사용되는가?
- [ ] memoization dependency가 정확한가?
- [ ] 불필요한 memoization 남용이 없는가?
```

---

### [실무]

Hooks Review 우선순위:

```text
Hook Rule Violation
→ Dependency Bug
→ Infinite Loop / Duplicate Request
→ Missing Cleanup
→ useEffect Misuse
→ Custom Hook Responsibility
→ Memoization Overuse
```

리뷰 코멘트 우선순위 판단:

```text
조건부 Hook 호출
→ Critical 또는 High

useEffect 무한 루프
→ High

API dependency 누락
→ High

cleanup 누락
→ Medium 또는 High

useEffect로 파생 값 동기화
→ Medium

불필요한 useMemo / useCallback
→ Low
```

---

### [FAQ]

Q. Hooks Review에서 가장 위험한 문제는 뭐야?
A. 조건부 Hook 호출, dependency 오류, 무한 루프, cleanup 누락이다.

Q. 조건부 Hook 호출은 어떤 우선순위야?
A. Hook 규칙 위반이므로 Critical 또는 High로 판단할 수 있다.

Q. useEffect dependency 누락은 어떤 우선순위야?
A. API 오동작이나 stale data를 만들면 High로 판단할 수 있다.

Q. 불필요한 useMemo는 큰 문제야?
A. 보통 Low다. 성능 이점 없이 코드 복잡도만 늘리는 경우 개선 권장이다.

---

# Retrieval Queries

### [FAQ]

Q. State Location Review는 뭐야?
A. React 상태가 local state, global state, URL state, server state 중 어디에 위치해야 하는지 검토하는 과정이다.

Q. state 위치는 어떻게 정해?
A. 한 컴포넌트에서만 쓰면 local state, 여러 페이지에서 공유되면 global state, 서버 데이터는 server state, URL에 남아야 하면 query params가 적합하다.

Q. 모든 상태를 전역 store에 넣어도 돼?
A. 권장하지 않는다. 컴포넌트 내부에서만 사용하는 상태는 local state가 더 단순하다.

Q. 검색어는 state에 둬야 해 URL에 둬야 해?
A. 공유, 새로고침 유지, 뒤로가기 지원이 필요하면 URL query params가 좋다.

Q. Local State는 언제 사용해?
A. modal open, tab selected, input value처럼 한 컴포넌트 내부에서만 사용하는 UI 상태에 적합하다.

Q. Global State는 언제 사용해?
A. 로그인 사용자 정보, 인증 여부, 권한, theme, toast처럼 여러 페이지에서 공유되는 client state에 적합하다.

Q. 서버 데이터도 Global State에 넣어야 해?
A. 보통 React Query 같은 server state 도구가 더 적합하다.

Q. URL State는 언제 사용해?
A. 검색어, 필터, 정렬, 페이지 번호처럼 새로고침 유지, 공유, 뒤로가기 지원이 필요한 값에 사용한다.

Q. 토큰을 URL에 넣어도 돼?
A. 안 된다. 브라우저 기록, 로그, referrer에 노출될 수 있어 보안 위험이 크다.

Q. State Duplication은 뭐야?
A. 같은 의미의 데이터가 여러 state에 중복 저장되어 동기화 오류를 만들 수 있는 상태 구조다.

Q. 파생 값은 state로 저장해야 해?
A. 대부분 기존 state에서 계산하는 것이 좋다.

Q. Derived State는 뭐야?
A. 기존 props나 state에서 계산 가능한 값이다.

Q. Derived State를 별도 state로 저장하면 왜 문제야?
A. 원본 값과 동기화되지 않으면 stale data 또는 UI 불일치가 발생할 수 있다.

Q. 배열 state를 push로 수정해도 돼?
A. 권장하지 않는다. 기존 배열을 직접 수정하면 React가 변경을 안정적으로 감지하지 못할 수 있다.

Q. state 불변성은 왜 중요해?
A. React가 참조 변경을 기준으로 렌더링을 판단하기 때문에 직접 수정은 렌더링 누락을 만들 수 있다.

Q. 함수형 업데이트는 언제 필요해?
A. 이전 state 값을 기준으로 다음 state를 계산할 때 필요하다.

Q. toggle 상태는 어떻게 업데이트해야 해?
A. `setIsOpen(prev => !prev)` 형태가 안전하다.

Q. Hook Rule Review는 뭐야?
A. React Hook이 최상위에서 같은 순서로 호출되는지 검토하는 과정이다.

Q. 조건문 안에서 Hook을 호출해도 돼?
A. 안 된다. Hook 호출 순서가 렌더링마다 달라질 수 있다.

Q. 조건이 있을 때 useEffect는 어떻게 써?
A. Hook은 최상위에서 호출하고 Hook 내부에서 조건을 처리한다.

Q. useEffect Dependency Review는 뭐야?
A. useEffect의 dependency array가 effect 내부에서 사용하는 값과 일치하는지 검토하는 과정이다.

Q. useEffect dependency warning은 무시해도 돼?
A. 권장하지 않는다. 의존성 누락은 stale closure와 예측 어려운 버그를 만들 수 있다.

Q. 객체를 dependency에 넣으면 왜 문제가 될 수 있어?
A. 객체가 매 렌더링마다 새로 생성되면 dependency가 계속 변경되어 effect가 반복 실행될 수 있다.

Q. useEffect는 언제 사용해야 해?
A. API 호출, 이벤트 리스너, 구독, 타이머, 외부 라이브러리 연동 같은 side effect 처리에 사용한다.

Q. 단순 계산에 useEffect를 써도 돼?
A. 권장하지 않는다. 렌더링 중 계산하거나 비용이 크면 useMemo를 사용한다.

Q. useEffect cleanup은 언제 필요해?
A. 이벤트 리스너, 타이머, 구독, WebSocket, 외부 리소스를 등록할 때 필요하다.

Q. Custom Hook은 언제 만들어?
A. 여러 컴포넌트에서 반복되는 상태 로직, API 호출, form 처리, modal 제어를 분리할 때 만든다.

Q. Custom Hook 이름은 꼭 use로 시작해야 해?
A. 그렇다. React Hook 규칙과 lint 검사를 위해 `use` prefix가 필요하다.

Q. Custom Hook은 객체로 반환하는 게 좋아 배열로 반환하는 게 좋아?
A. 반환 값이 많거나 의미가 중요한 경우 객체 반환이 안전하다. useState처럼 관례가 명확하면 배열도 가능하다.

Q. Custom Hook에서 setter를 그대로 반환해도 돼?
A. 가능하지만 남용하면 상태 변경 흐름이 흩어진다. 필요한 action 함수로 감싸는 것이 좋다.

Q. Custom Hook 내부 dependency도 리뷰해야 해?
A. 해야 한다. Custom Hook은 재사용되므로 dependency 오류가 여러 화면에 전파될 수 있다.

Q. useMemo는 항상 써야 해?
A. 아니다. 계산 비용이 크거나 참조 안정성이 필요한 경우에만 사용한다.

Q. useCallback은 모든 함수에 써야 해?
A. 아니다. 참조 안정성이 필요한 경우에만 사용한다.

Q. useReducer는 언제 써?
A. 여러 상태가 연관되어 있고 상태 전환이 action 단위로 명확할 때 사용한다.

Q. State Review에서 가장 먼저 볼 것은 뭐야?
A. 인증 상태, 서버 데이터, 중복 state, 직접 mutation 여부를 먼저 본다.

Q. Hooks Review에서 가장 위험한 문제는 뭐야?
A. 조건부 Hook 호출, dependency 오류, 무한 루프, cleanup 누락이다.

Q. State and Hooks Review의 최종 목적은 뭐야?
A. React 상태와 Hook 사용이 예측 가능하고 안전하며 유지보수 가능한 구조인지 판단하는 것이다.
