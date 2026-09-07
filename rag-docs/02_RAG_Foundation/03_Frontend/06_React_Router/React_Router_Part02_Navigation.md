# React Router Part02 Navigation

---

# 1. React Router Navigation

## 1.1 Navigation Purpose

### [개념]

React Router Navigation은 SPA 내부에서 URL을 변경하고 해당 Route의 Page Component를 렌더링하는 이동 구조다.

React Router Navigation은 전체 페이지 reload 없이 화면을 전환한다.

Navigation 문서는 Frontend Agent가 Link, NavLink, useNavigate, Navigate, useLocation, Navigation State를 상황에 맞게 선택하도록 지원한다.

---

### [핵심]

- React Router Navigation
- Client Side Navigation
- Link
- NavLink
- useNavigate
- Navigate
- useLocation
- Navigation State
- Browser History
- Internal Route
- External Link
- Redirect
- Auth Redirect
- replace option
- current location

Navigation 선택 기준:

```text
User Click Link
→ Link / NavLink

Code Flow Navigation
→ useNavigate

Render Redirect
→ Navigate

Current URL Read
→ useLocation

Temporary Data Transfer
→ Navigation State
```

---

### [실무]

2026 실무 기준에서 Navigation은 단순 URL 이동이 아니다.

실무 Navigation은 아래 흐름을 포함한다.

- Header Menu 이동
- Sidebar Menu 이동
- Tab Menu 이동
- 로그인 성공 후 이동
- 회원가입 성공 후 이동
- 저장 / 수정 / 삭제 완료 후 이동
- 권한 없음 redirect
- token 만료 후 login 이동
- Not Found Page에서 main 이동
- 이전 위치 저장 후 로그인 redirect
- 현재 URL 기반 Layout 제어

Navigation 설계 Flow:

```text
User Action
→ Choose Navigation Type
→ Change URL
→ React Router Match Route
→ Render Page Component
→ Preserve or Replace History
```

---

### [FAQ]

Q. React Router Navigation은 뭐야?
A. SPA 내부에서 URL을 변경하고 해당 Route의 Component를 렌더링하는 이동 구조다.

Q. 내부 페이지 이동은 뭘 써?
A. 사용자가 클릭하는 일반 내부 이동은 Link 또는 NavLink를 사용한다.

Q. 코드에서 이동하려면 뭘 써?
A. 로그인 성공, 저장 완료처럼 코드 흐름에 따라 이동할 때는 useNavigate를 사용한다.

Q. 조건에 따라 redirect하려면 뭘 써?
A. 렌더링 결과로 redirect할 때는 Navigate Component를 사용할 수 있다.

---

# 2. Link

## 2.1 Link Concept

### [개념]

Link는 React Router에서 페이지 전체 reload 없이 내부 Route로 이동하기 위한 Component다.

HTML a 태그와 유사하지만, React Router가 브라우저 History와 Route Matching을 처리한다.

---

### [핵심]

- Link
- Internal Route Navigation
- Client Side Navigation
- `to`
- Browser History
- Page reload 방지
- React Router Route Matching
- Accessibility
- Anchor-like UX

기본 예:

```jsx
import { Link } from "react-router";

function Header() {
  return <Link to="/festivals">Festivals</Link>;
}
```

핵심 규칙:

- 내부 Route 이동은 Link 사용
- `to`에는 실제 이동할 path 전달
- 페이지 전체 reload 없이 URL 변경
- Route path와 Link to 정합성 필요
- 외부 URL 이동에는 a 태그 사용

---

### [실무]

일반 내부 이동:

```jsx
<Link to="/">Home</Link>
<Link to="/login">Login</Link>
<Link to="/festivals">Festivals</Link>
```

상세 페이지 이동:

```jsx
<Link to={`/festivals/${festival.festivalId}`}>{festival.title}</Link>
```

path builder 사용:

```jsx
<Link to={createFestivalDetailPath(festival.festivalId)}>{festival.title}</Link>
```

외부 링크:

```jsx
<a href="https://example.com" target="_blank" rel="noreferrer">
  External Site
</a>
```

실무 기준:

- Header, Card, List Item 내부 이동은 Link 우선
- 단순 페이지 이동을 button + useNavigate로 남용하지 않음
- 외부 사이트는 Link가 아니라 a 태그 사용
- Link to는 Route path와 일치해야 함
- Dynamic Route pattern을 Link to에 그대로 넣지 않음
- 클릭 가능한 텍스트는 접근성 있는 이름 제공

---

### [FAQ]

Q. React Router에서 a 태그 대신 Link를 쓰는 이유는?
A. 내부 Route 이동 시 페이지 전체 reload 없이 React Router가 URL과 화면을 갱신하기 위해서다.

Q. 외부 사이트 이동도 Link를 써?
A. 아니다. 외부 URL 이동은 일반 a 태그를 사용한다.

Q. Link의 to에는 뭘 넣어?
A. 이동할 내부 Route path를 넣는다. 예: `/login`, `/festivals/1`.

Q. Link를 쓰면 API 요청이 발생해?
A. Link 자체는 Route 이동을 수행한다. 데이터 요청은 해당 Page Component나 Hook에서 별도로 수행한다.

---

## 2.2 Link Common Mistakes

### [개념]

Link 오류는 Route path 불일치, Dynamic Route pattern 오용, 외부 링크 처리 실수에서 자주 발생한다.

---

### [핵심]

자주 발생:

- Link to와 Route path 불일치
- Dynamic Route pattern을 Link to에 그대로 사용
- 내부 이동에 a href 사용
- 외부 이동에 Link 사용
- 잘못된 상대 경로 사용
- Route Constants와 실제 path 불일치
- id 값 undefined 상태로 URL 생성
- button으로 단순 링크 이동 남용

---

### [실무]

나쁜 예:

```jsx
<Link to="/festival/1">Detail</Link>

<Route path="/festivals/:festivalId" element={<FestivalDetailPage />} />
```

문제:

```text
Link to는 /festival/1
Route path는 /festivals/:festivalId
경로 불일치로 Route 매칭 실패 가능
```

좋은 예:

```jsx
<Link to="/festivals/1">Detail</Link>

<Route path="/festivals/:festivalId" element={<FestivalDetailPage />} />
```

나쁜 예:

```jsx
<Link to="/festivals/:festivalId">Detail</Link>
```

좋은 예:

```jsx
<Link to={`/festivals/${festival.festivalId}`}>Detail</Link>
```

Debug Flow:

```text
Click Link
→ URL 확인
→ Route path 확인
→ Link to 확인
→ Dynamic Value 확인
→ Route Match 확인
→ Page Render 확인
```

---

### [FAQ]

Q. Link 클릭 후 NotFoundPage가 나와?
A. Link to와 Route path가 일치하는지 확인해야 한다.

Q. `/festivals/:festivalId`를 Link to에 넣어도 돼?
A. 안 된다. Link에는 `/festivals/1`처럼 실제 값이 들어간 URL을 넣어야 한다.

Q. 내부 이동에 a href를 쓰면 안 돼?
A. 가능은 하지만 전체 reload가 발생할 수 있어 SPA 내부 이동에는 Link를 권장한다.

Q. Link URL에 undefined가 들어가?
A. URL 생성 전에 id 값이 존재하는지 확인하고 path builder 사용을 검토한다.

---

# 3. NavLink

## 3.1 NavLink Concept

### [개념]

NavLink는 현재 URL과 일치하는 링크에 active 상태를 적용할 수 있는 Link 확장 Component다.

Header, Sidebar, Tab Menu처럼 현재 선택된 메뉴 표시가 필요한 Navigation UI에 적합하다.

---

### [핵심]

- NavLink
- active state
- current route
- className callback
- style callback
- aria-current
- Navigation Menu
- Sidebar
- Tab Route
- Current Page Indication

기본 예:

```jsx
import { NavLink } from "react-router";

function Header() {
  return (
    <NavLink
      to="/festivals"
      className={({ isActive }) => (isActive ? "active" : "")}
    >
      Festivals
    </NavLink>
  );
}
```

---

### [실무]

Header Navigation 예:

```jsx
<nav>
  <NavLink to="/">Home</NavLink>
  <NavLink to="/festivals">Festivals</NavLink>
  <NavLink to="/mypage">MyPage</NavLink>
</nav>
```

active class 적용:

```jsx
<NavLink
  to="/festivals"
  className={({ isActive }) => (isActive ? "nav-link active" : "nav-link")}
>
  Festivals
</NavLink>
```

실무 사용 상황:

- Header menu
- Sidebar menu
- Admin menu
- MyPage menu
- Route 기반 tab
- 현재 위치 강조 UI

권장:

- 단순 이동은 Link
- 메뉴 active 표시가 필요하면 NavLink
- active class naming 통일
- 현재 Route 기준과 메뉴 URL 정합성 유지
- 접근성을 위해 의미 있는 nav 구조 사용

---

### [FAQ]

Q. Link와 NavLink 차이는?
A. Link는 단순 이동이고 NavLink는 현재 URL과 일치할 때 active 상태를 알 수 있다.

Q. NavLink는 언제 써?
A. Header, Sidebar, Tab Menu처럼 현재 선택된 메뉴 표시가 필요할 때 사용한다.

Q. NavLink active class는 어떻게 줘?
A. className callback에서 isActive 값을 확인해 active class를 반환한다.

Q. NavLink도 페이지 reload 없이 이동해?
A. 그렇다. NavLink도 React Router의 Client Side Navigation을 사용한다.

---

## 3.2 NavLink Common Mistakes

### [개념]

NavLink 오류는 active 기준 오해, path 불일치, 메뉴 구조와 Route 구조 불일치에서 자주 발생한다.

---

### [핵심]

자주 발생:

- Link가 필요한 곳에 NavLink 남용
- active className callback 작성 오류
- Route path와 NavLink to 불일치
- 상위 경로 active 포함 여부 오해
- 메뉴 path와 실제 Page Route 불일치
- CSS active class 미정의
- 현재 path 직접 비교 로직 중복 작성

---

### [실무]

나쁜 예:

```jsx
<NavLink to="/festivals" className={isActive ? "active" : ""}>
  Festivals
</NavLink>
```

문제:

```text
isActive는 className callback 인자로 받아야 함
```

좋은 예:

```jsx
<NavLink
  to="/festivals"
  className={({ isActive }) => (isActive ? "active" : "")}
>
  Festivals
</NavLink>
```

Debug Flow:

```text
Menu Active 문제
→ Current URL 확인
→ NavLink to 확인
→ className callback 확인
→ CSS active class 확인
→ Route path 확인
```

---

### [FAQ]

Q. NavLink active가 안 먹어?
A. NavLink to와 현재 URL이 일치하는지, className callback과 CSS active class가 맞는지 확인한다.

Q. 모든 Link를 NavLink로 바꿔도 돼?
A. 권장하지 않는다. 현재 메뉴 표시가 필요한 Navigation UI에만 NavLink를 쓰는 것이 좋다.

Q. 현재 path 비교는 useLocation으로 직접 해야 해?
A. 메뉴 active 표시 목적이면 NavLink를 우선 사용한다.

---

# 4. useNavigate

## 4.1 useNavigate Concept

### [개념]

useNavigate는 코드에서 명령형으로 Route 이동을 수행하는 React Router Hook이다.

사용자 클릭 링크가 아니라 로그인 성공, 저장 완료, 삭제 완료, 권한 없음 처리처럼 코드 흐름에 따라 이동할 때 사용한다.

---

### [핵심]

- useNavigate
- programmatic navigation
- imperative navigation
- event after navigation
- form submit success
- login success redirect
- save success redirect
- delete success redirect
- auth redirect
- replace option
- history back
- Router 내부 Hook

기본 예:

```jsx
import { useNavigate } from "react-router";

function LoginPage() {
  const navigate = useNavigate();

  function handleLoginSuccess() {
    navigate("/");
  }

  return <button onClick={handleLoginSuccess}>Login</button>;
}
```

---

### [실무]

로그인 성공 후 이동:

```jsx
function LoginPage() {
  const navigate = useNavigate();

  async function handleSubmit() {
    await login();
    navigate("/", { replace: true });
  }

  return <button onClick={handleSubmit}>Login</button>;
}
```

저장 성공 후 상세 페이지 이동:

```jsx
async function handleSave() {
  const savedFestival = await saveFestival(formData);
  navigate(`/festivals/${savedFestival.festivalId}`);
}
```

뒤로가기:

```jsx
navigate(-1);
```

실무 기준:

- 일반 클릭 이동은 Link / NavLink 우선
- 처리 완료 후 이동은 useNavigate 사용
- 로그인 redirect에는 replace 옵션 고려
- Event Handler 또는 Effect 내부에서 호출
- 렌더링 중 직접 navigate 호출 금지
- Router 내부 Component에서만 사용
- 이동 전 필요한 데이터 검증

---

### [FAQ]

Q. Link와 useNavigate 중 뭐를 써?
A. 사용자가 클릭해서 이동하는 일반 링크는 Link를 우선하고, 로그인 성공 후 이동처럼 코드 흐름에 따른 이동은 useNavigate를 사용한다.

Q. useNavigate는 언제 써?
A. 로그인 성공, 저장 완료, 삭제 완료, 권한 없음 redirect처럼 코드 흐름에 따라 이동할 때 사용한다.

Q. navigate replace는 언제 써?
A. 로그인 페이지 redirect처럼 사용자가 뒤로가기로 다시 돌아오면 안 되는 경우에 사용한다.

Q. useNavigate를 Router 밖에서 쓸 수 있어?
A. 안 된다. Router 내부 Component에서만 사용할 수 있다.

---

## 4.2 useNavigate Common Mistakes

### [개념]

useNavigate 오류는 Router Context 밖 사용, 렌더링 중 호출, 일반 링크 이동 남용에서 자주 발생한다.

---

### [핵심]

자주 발생:

- BrowserRouter 밖에서 useNavigate 사용
- Component render 중 navigate 직접 호출
- 일반 링크 이동에 useNavigate 남용
- replace 옵션 누락
- async 처리 완료 전 navigate 호출
- 이동할 URL 생성 값 undefined
- 권한 redirect loop 발생
- navigate(-1) 사용 시 fallback 경로 없음

---

### [실무]

나쁜 예:

```jsx
function ProtectedPage({ authenticated }) {
  const navigate = useNavigate();

  if (!authenticated) {
    navigate("/login");
  }

  return <div>Protected</div>;
}
```

문제:

```text
렌더링 중 navigate 호출
조건부 redirect에는 Navigate Component 또는 Effect 사용 검토
```

권장 예:

```jsx
import { Navigate } from "react-router";

function ProtectedPage({ authenticated }) {
  if (!authenticated) {
    return <Navigate to="/login" replace />;
  }

  return <div>Protected</div>;
}
```

async 처리 예:

```jsx
async function handleSubmit() {
  const result = await submitForm(formData);

  if (result.success) {
    navigate("/complete", { replace: true });
  }
}
```

Debug Flow:

```text
Navigation Error
→ BrowserRouter 내부 여부 확인
→ navigate 호출 위치 확인
→ async 완료 시점 확인
→ target path 확인
→ replace 필요 여부 확인
→ redirect loop 확인
```

---

### [FAQ]

Q. useNavigate 에러가 나면 뭘 확인해?
A. 해당 Component가 BrowserRouter 내부인지, navigate 호출 위치가 Event Handler나 Effect 내부인지 확인한다.

Q. 렌더링 중 navigate를 호출해도 돼?
A. 권장하지 않는다. 조건부 redirect는 Navigate Component를 사용하는 것이 명확하다.

Q. button 클릭 이동은 항상 useNavigate야?
A. 폼 제출이나 처리 후 이동이면 useNavigate가 적합하고, 단순 링크라면 Link가 더 적합하다.

Q. navigate(-1)은 언제 조심해야 해?
A. 이전 히스토리가 없을 수 있으므로 필요한 경우 fallback 경로를 제공하는 UI를 고려한다.

---

# 5. Navigate Component

## 5.1 Navigate Concept

### [개념]

Navigate Component는 렌더링 결과로 redirect를 수행하는 React Router Component다.

조건부 접근 제어, 인증 상태에 따른 redirect, 권한 부족 redirect에서 자주 사용한다.

---

### [핵심]

- Navigate
- redirect
- declarative redirect
- conditional render
- protected route
- auth guard
- role guard
- replace
- redirect target
- render result navigation

기본 예:

```jsx
import { Navigate } from "react-router";

function ProtectedRoute({ authenticated, children }) {
  if (!authenticated) {
    return <Navigate to="/login" replace />;
  }

  return children;
}
```

---

### [실무]

로그인 사용자 접근 제한:

```jsx
function GuestOnlyRoute({ authenticated, children }) {
  if (authenticated) {
    return <Navigate to="/" replace />;
  }

  return children;
}
```

권한 부족 redirect:

```jsx
function AdminRoute({ role, children }) {
  if (role !== "ROLE_ADMIN") {
    return <Navigate to="/forbidden" replace />;
  }

  return children;
}
```

실무 기준:

- 조건부 redirect는 Navigate 사용 가능
- Protected Route에서 자주 사용
- 로그인 상태 loading 중에는 redirect 보류
- replace 옵션으로 history 정리 가능
- redirect loop 방지
- 이전 위치 저장이 필요하면 location state 사용
- 실제 보안은 Backend 인증/인가에서 처리

---

### [FAQ]

Q. Navigate와 useNavigate 차이는?
A. Navigate는 렌더링 결과로 redirect하고 useNavigate는 함수 호출로 이동한다.

Q. Protected Route에는 Navigate를 써도 돼?
A. 가능하다. 인증 상태에 따라 login 페이지로 redirect할 때 자주 사용한다.

Q. Navigate의 replace는 왜 써?
A. 뒤로가기로 redirect 이전 페이지에 다시 돌아가는 것을 방지하기 위해 사용한다.

Q. Navigate는 보안 기능이야?
A. 아니다. Frontend redirect는 UX용이고 실제 보안은 Backend에서 검증해야 한다.

---

## 5.2 Navigate Common Mistakes

### [개념]

Navigate 오류는 인증 loading 처리 누락, redirect loop, 잘못된 target 경로에서 자주 발생한다.

---

### [핵심]

자주 발생:

- 인증 상태 확인 전 login으로 redirect
- login 페이지와 protected 페이지 간 redirect loop
- replace 옵션 누락
- 권한 없음과 비로그인 상태 구분 실패
- target path 오타
- 이전 위치 저장 누락
- Backend Authorization 없이 Frontend만 보호

---

### [실무]

나쁜 예:

```jsx
function ProtectedRoute({ authenticated, children }) {
  if (!authenticated) {
    return <Navigate to="/login" replace />;
  }

  return children;
}
```

문제 가능성:

```text
authenticated 초기값이 false이고 auth loading 중이면 즉시 login redirect 발생
```

권장 예:

```jsx
function ProtectedRoute({ loading, authenticated, children }) {
  if (loading) {
    return <div>Loading...</div>;
  }

  if (!authenticated) {
    return <Navigate to="/login" replace />;
  }

  return children;
}
```

Redirect Loop Debug Flow:

```text
Current Route 확인
→ Auth State 확인
→ Loading State 확인
→ Navigate target 확인
→ GuestOnlyRoute / ProtectedRoute 조건 확인
→ replace 여부 확인
```

---

### [FAQ]

Q. 인증 상태 확인 전 바로 login으로 보내도 돼?
A. 권장하지 않는다. 인증 상태 loading 중에는 임시 로딩 UI를 보여주고 확인 후 redirect해야 한다.

Q. redirect loop는 왜 생겨?
A. 인증 조건이나 redirect target이 잘못되어 login과 protected page 사이를 계속 오갈 때 발생한다.

Q. 권한 없는 사용자는 어디로 보내?
A. 프로젝트 기준에 따라 `/forbidden`, `/login`, `/` 중 하나로 보낼 수 있다. 기준을 통일해야 한다.

Q. Frontend Navigate만 있으면 API도 보호돼?
A. 아니다. API 보호는 Backend 인증/인가가 반드시 처리해야 한다.

---

# 6. useLocation

## 6.1 useLocation Concept

### [개념]

useLocation은 현재 URL location 정보를 읽는 React Router Hook이다.

현재 pathname, search, hash, state를 확인할 수 있다.

---

### [핵심]

- useLocation
- location
- pathname
- search
- hash
- state
- current route
- previous location
- auth redirect
- route change detection
- conditional layout
- analytics basics

기본 예:

```jsx
import { useLocation } from "react-router";

function CurrentPath() {
  const location = useLocation();

  return <p>{location.pathname}</p>;
}
```

location 주요 값:

```text
location.pathname
→ 현재 path

location.search
→ query string

location.hash
→ hash

location.state
→ navigation state
```

---

### [실무]

로그인 redirect 이전 위치 저장:

```jsx
import { Navigate, useLocation } from "react-router";

function ProtectedRoute({ authenticated, children }) {
  const location = useLocation();

  if (!authenticated) {
    return <Navigate to="/login" replace state={{ from: location.pathname }} />;
  }

  return children;
}
```

조건부 Layout 예:

```jsx
const location = useLocation();
const isAuthPage =
  location.pathname === "/login" || location.pathname === "/signup";
```

실무 사용 상황:

- 현재 path 확인
- 로그인 redirect 이전 위치 저장
- 조건부 Header / Footer 표시
- route 변경 감지
- analytics tracking basics
- scroll restoration basics
- query string 원문 확인

주의:

- 메뉴 active 표시는 NavLink 우선
- location.state는 새로고침 시 사라질 수 있음
- 영구 유지가 필요한 값은 query string 또는 storage 사용
- path 문자열 직접 비교는 상수 사용 권장
- 민감정보를 state에 넣지 않음

---

### [FAQ]

Q. useLocation은 언제 써?
A. 현재 URL path, search, state 정보가 필요할 때 사용한다.

Q. location.pathname은 뭐야?
A. 현재 URL의 path 부분이다. 예: `/festivals/1`.

Q. location.search는 뭐야?
A. 현재 URL의 query string 부분이다. 예: `?keyword=flower&page=1`.

Q. 메뉴 active 표시를 useLocation으로 해야 해?
A. 단순 메뉴 active 표시는 NavLink를 우선 사용한다.

---

## 6.2 useLocation Common Mistakes

### [개념]

useLocation 오류는 location.state 영구 저장 오해, path 직접 비교 남용, Router 밖 Hook 사용에서 자주 발생한다.

---

### [핵심]

자주 발생:

- location.state가 새로고침 후 유지된다고 착각
- 중요한 데이터를 location.state에 저장
- 민감정보를 location.state로 전달
- 메뉴 active 표시를 useLocation으로 복잡하게 구현
- path 문자열 오타
- query string 파싱을 수동으로 과도하게 처리
- Router 밖에서 useLocation 사용

---

### [실무]

나쁜 예:

```jsx
navigate("/payment", {
  state: {
    cardNumber: "1234-5678-1234-5678",
  },
});
```

문제:

```text
민감정보를 Navigation State로 전달
```

권장:

```text
민감정보는 Navigation State로 전달하지 않음
필요한 데이터는 서버 상태, 안전한 API, 임시 식별자 기준으로 처리
```

새로고침 주의:

```jsx
const location = useLocation();
const from = location.state?.from ?? "/";
```

Debug Flow:

```text
location 관련 문제
→ BrowserRouter 내부 여부 확인
→ pathname 확인
→ search 확인
→ state 존재 여부 확인
→ 새로고침 여부 확인
→ 영구 상태 필요 여부 확인
```

---

### [FAQ]

Q. location.state는 새로고침해도 남아?
A. 보장되지 않는다. 영구적으로 유지해야 하는 정보는 query string이나 storage를 고려한다.

Q. location.state에 중요한 데이터를 넣어도 돼?
A. 권장하지 않는다. 새로고침이나 직접 접근 시 사라질 수 있고 민감정보 전달에 부적합하다.

Q. useLocation으로 query string을 직접 파싱해야 해?
A. query string을 읽고 수정해야 한다면 useSearchParams를 우선 고려한다.

---

# 7. Navigation State

## 7.1 Navigation State Concept

### [개념]

Navigation State는 Link 또는 navigate 이동 시 URL에 보이지 않는 임시 데이터를 함께 전달하는 방식이다.

React Router의 location.state로 읽을 수 있다.

---

### [핵심]

- Navigation State
- location.state
- Link state
- navigate state
- temporary data
- previous location
- auth redirect
- invisible URL data
- refresh caution
- direct access caution

Link state 예:

```jsx
<Link to="/login" state={{ from: "/mypage" }}>
  Login
</Link>
```

navigate state 예:

```jsx
navigate("/login", {
  state: { from: location.pathname },
  replace: true,
});
```

읽기 예:

```jsx
const location = useLocation();
const from = location.state?.from ?? "/";
```

---

### [실무]

로그인 후 원래 페이지로 돌아가기:

```jsx
function LoginPage() {
  const navigate = useNavigate();
  const location = useLocation();

  const from = location.state?.from ?? "/";

  async function handleLogin() {
    await login();
    navigate(from, { replace: true });
  }

  return <button onClick={handleLogin}>Login</button>;
}
```

실무 사용 상황:

- 로그인 후 돌아갈 경로 저장
- 목록에서 상세로 이동 시 간단한 UI 힌트 전달
- 이전 페이지 정보 전달
- modal background location 패턴 기초
- 임시 redirect target 전달

주의:

- URL에 보이지 않음
- 새로고침 / 직접 접근 시 state 없음
- 중요한 데이터 저장 용도 아님
- 민감정보 전달 금지
- 공유 가능한 상태는 Query String 사용
- 서버 검증이 필요한 데이터는 API 기준으로 처리

---

### [FAQ]

Q. Navigation State는 뭐야?
A. Route 이동 시 URL에 보이지 않는 임시 데이터를 함께 전달하는 방식이다.

Q. Navigation State는 언제 써?
A. 로그인 후 돌아갈 경로처럼 임시 이동 정보를 전달할 때 사용한다.

Q. Navigation State는 URL에 보여?
A. 아니다. URL에는 보이지 않고 location.state로 읽는다.

Q. Navigation State는 새로고침해도 유지돼?
A. 보장되지 않는다. 직접 접근이나 새로고침 시 없을 수 있다.

---

## 7.2 Navigation State Common Mistakes

### [개념]

Navigation State 오류는 영구 데이터 저장 오해, 직접 접근 미대응, 민감정보 전달에서 자주 발생한다.

---

### [핵심]

자주 발생:

- 새로고침 후 state가 사라지는 문제 미처리
- 직접 URL 접근 시 state 없음 미처리
- 중요한 데이터를 state에만 저장
- 민감정보를 state에 전달
- 공유 가능한 검색 조건을 state로 처리
- redirect target 검증 누락
- fallback path 누락

---

### [실무]

나쁜 예:

```jsx
const location = useLocation();
const from = location.state.from;
```

문제:

```text
location.state가 undefined면 런타임 오류 발생
```

좋은 예:

```jsx
const location = useLocation();
const from = location.state?.from ?? "/";
```

검색 조건에 부적합한 예:

```jsx
navigate("/festivals", {
  state: { keyword: "꽃", region: "seoul" },
});
```

권장:

```text
/festivals?keyword=꽃&region=seoul
```

이유:

- 검색 조건은 공유 가능해야 함
- 새로고침 유지 필요
- 뒤로가기 복원 필요
- Query String이 더 적합

---

### [FAQ]

Q. location.state가 undefined야?
A. 직접 접근, 새로고침, state 없이 이동한 경우일 수 있으므로 optional chaining과 fallback 값을 사용한다.

Q. 검색 조건을 Navigation State로 넘겨도 돼?
A. 권장하지 않는다. 검색, 필터, 정렬, 페이지 조건은 Query String이 더 적합하다.

Q. redirect target은 state로 저장해도 돼?
A. 가능하다. 다만 없을 경우 기본 이동 경로를 준비해야 한다.

Q. Navigation State에 민감정보를 넣어도 돼?
A. 안 된다. 민감정보는 Navigation State로 전달하지 않는다.

---

# 8. Navigation Selection Guide

## 8.1 Link vs NavLink

### [개념]

Link와 NavLink는 모두 내부 Route 이동에 사용되지만 active 상태 필요 여부가 다르다.

Link는 단순 이동에 적합하고 NavLink는 현재 메뉴 표시가 필요한 Navigation UI에 적합하다.

---

### [핵심]

| 비교               | Link                         | NavLink                       |
| ------------------ | ---------------------------- | ----------------------------- |
| 목적               | 내부 Route 이동              | 내부 Route 이동 + active 상태 |
| active 여부        | 없음                         | 있음                          |
| 사용 위치          | 카드, 버튼형 링크, 일반 링크 | Header, Sidebar, Tab Menu     |
| className callback | 일반 className               | isActive 기반 가능            |
| 접근성             | 내부 링크 UX                 | 현재 route 표시 가능          |

선택 기준:

```text
Simple Internal Navigation
→ Link

Navigation Menu Active State
→ NavLink
```

---

### [실무]

Link 적합:

```jsx
<Link to={`/festivals/${festival.festivalId}`}>Detail</Link>
```

NavLink 적합:

```jsx
<NavLink
  to="/festivals"
  className={({ isActive }) => (isActive ? "active" : "")}
>
  Festivals
</NavLink>
```

실무 기준:

- 목록 카드 상세 이동은 Link
- 상단 메뉴는 NavLink
- 사이드바 메뉴는 NavLink
- 탭 메뉴는 NavLink 가능
- active 표시가 필요 없으면 Link로 충분

---

### [FAQ]

Q. Link와 NavLink 중 뭘 써야 해?
A. 단순 내부 이동은 Link, 현재 선택된 메뉴 표시가 필요하면 NavLink를 사용한다.

Q. Header Menu는 Link와 NavLink 중 뭐가 좋아?
A. 현재 페이지 표시가 필요하므로 NavLink가 적합하다.

Q. 카드 상세 이동은 NavLink가 좋아?
A. 보통 active 표시가 필요 없으므로 Link가 적합하다.

---

## 8.2 Link vs useNavigate

### [개념]

Link는 사용자가 클릭하는 선언형 내부 이동이고 useNavigate는 코드 흐름에 따른 명령형 이동이다.

---

### [핵심]

| 비교      | Link                   | useNavigate              |
| --------- | ---------------------- | ------------------------ |
| 방식      | Component 기반 이동    | 함수 호출 이동           |
| 사용 상황 | 사용자가 클릭하는 링크 | 처리 성공 / 실패 후 이동 |
| 위치      | JSX                    | Event Handler / Effect   |
| 예        | 상세 페이지 링크       | 로그인 성공 후 메인 이동 |
| 권장      | 일반 이동 우선         | 조건부 / 처리 후 이동    |

선택 기준:

```text
User sees a link and clicks
→ Link

Code decides where to go after logic
→ useNavigate
```

---

### [실무]

Link 사용:

```jsx
<Link to="/signup">Sign Up</Link>
```

useNavigate 사용:

```jsx
async function handleLogin() {
  await login();
  navigate("/", { replace: true });
}
```

실무 기준:

- 의미 있는 링크 UI는 Link
- 폼 제출 후 이동은 useNavigate
- 삭제 후 목록 이동은 useNavigate
- 권한 조건 처리 후 이동은 useNavigate 또는 Navigate
- 단순 메뉴 이동은 useNavigate보다 Link / NavLink 우선

---

### [FAQ]

Q. button onClick으로 navigate하면 안 돼?
A. 처리 후 이동이면 괜찮지만 단순 페이지 이동은 Link가 더 적합하다.

Q. 로그인 성공 후 이동은 Link야 useNavigate야?
A. 로그인 처리 성공 후 코드 흐름에 따라 이동하므로 useNavigate가 적합하다.

Q. 상세 페이지 이동은 Link야 useNavigate야?
A. 사용자가 목록에서 상세를 클릭하는 구조라면 Link가 적합하다.

---

## 8.3 Navigate vs useNavigate

### [개념]

Navigate는 렌더링 결과로 redirect하는 Component이고 useNavigate는 함수 호출로 이동하는 Hook이다.

조건부 렌더링 기반 redirect는 Navigate, 이벤트 처리 후 이동은 useNavigate가 적합하다.

---

### [핵심]

| 비교      | Navigate             | useNavigate            |
| --------- | -------------------- | ---------------------- |
| 형태      | Component            | Hook                   |
| 방식      | 렌더링 결과 redirect | 함수 호출 이동         |
| 사용 위치 | JSX return           | Event Handler / Effect |
| 예        | Protected Route      | 로그인 성공 후 이동    |
| replace   | prop                 | option                 |
| 위험      | redirect loop        | render 중 호출         |

선택 기준:

```text
If render condition says redirect
→ Navigate

If event or async logic completes
→ useNavigate
```

---

### [실무]

Navigate 사용:

```jsx
function ProtectedRoute({ authenticated, children }) {
  if (!authenticated) {
    return <Navigate to="/login" replace />;
  }

  return children;
}
```

useNavigate 사용:

```jsx
async function handleSave() {
  await save();
  navigate("/complete");
}
```

실무 기준:

- Protected Route는 Navigate가 명확함
- 로그인 성공 후 이동은 useNavigate가 명확함
- render 중 navigate 호출은 피함
- loading 상태 확인 후 redirect
- redirect loop 방지

---

### [FAQ]

Q. Navigate와 useNavigate 중 뭘 써야 해?
A. 렌더링 조건에 따른 redirect는 Navigate, 이벤트나 비동기 처리 후 이동은 useNavigate를 사용한다.

Q. Protected Route는 Navigate가 좋아?
A. 일반적으로 인증 조건에 따른 렌더링 redirect이므로 Navigate가 적합하다.

Q. useNavigate로 Protected Route를 만들 수 있어?
A. 가능은 하지만 렌더링 중 호출을 피해야 하므로 Navigate가 더 단순한 경우가 많다.

---

# 9. Navigation Checklist

## 9.1 Part02 Checklist

### [개념]

Navigation 문서는 React Router 이동 방식과 선택 기준을 검수하기 위한 체크리스트를 포함한다.

---

### [핵심]

Checklist:

```md
- [ ] React Router Navigation 목적이 설명되었는가?
- [ ] Link 개념과 사용 기준이 포함되었는가?
- [ ] 외부 링크는 a 태그 사용 기준이 포함되었는가?
- [ ] NavLink active 상태가 설명되었는가?
- [ ] Link와 NavLink 비교가 포함되었는가?
- [ ] useNavigate 사용 기준이 포함되었는가?
- [ ] navigate replace 옵션이 설명되었는가?
- [ ] Navigate Component 기준이 포함되었는가?
- [ ] Navigate와 useNavigate 비교가 포함되었는가?
- [ ] useLocation의 pathname / search / state가 포함되었는가?
- [ ] Navigation State 개념이 포함되었는가?
- [ ] location.state 새로고침 주의가 포함되었는가?
- [ ] 검색 조건은 Query String이 적합하다는 기준이 포함되었는가?
- [ ] Auth Redirect와 이전 위치 저장 예제가 포함되었는가?
- [ ] Common Mistakes가 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 Flow:

```text
Draft
→ Navigation Purpose Check
→ Link Check
→ NavLink Check
→ useNavigate Check
→ Navigate Check
→ useLocation Check
→ Navigation State Check
→ Comparison Check
→ Common Mistakes Check
→ FAQ Check
→ Retrieval Queries Check
→ Final Review
```

---

### [FAQ]

Q. Navigation 문서 검수에서 가장 중요한 것은?
A. Link, NavLink, useNavigate, Navigate, useLocation, Navigation State의 선택 기준과 실수 방지 기준이다.

Q. Part02에서 useParams도 다뤄?
A. 아니다. useParams와 useSearchParams는 Params / Search Params Part에서 다룬다.

Q. Part02에서 Protected Route를 깊게 다뤄?
A. 아니다. Navigate 사용 예로 언급하고 Protected Route 심화는 별도 Part에서 다룬다.

---

# 10. Navigation Common Mistakes

## 10.1 Common Mistakes

### [개념]

React Router Navigation에서 자주 발생하는 문제는 잘못된 이동 도구 선택, Route path 불일치, state 유지 오해, redirect loop다.

---

### [핵심]

자주 발생:

- 내부 Route 이동에 a href 사용
- 외부 URL 이동에 Link 사용
- 단순 링크 이동에 useNavigate 남용
- NavLink active callback 작성 오류
- useNavigate를 BrowserRouter 밖에서 사용
- 렌더링 중 navigate 직접 호출
- Navigate에서 auth loading 처리 누락
- redirect loop 발생
- replace 옵션 누락
- location.state 새로고침 유지 오해
- Navigation State에 중요한 데이터 저장
- Navigation State에 민감정보 전달
- 검색 조건을 Navigation State로 전달
- Link to와 Route path 불일치
- Dynamic Route pattern을 Link to에 그대로 사용
- id undefined로 URL 생성

---

### [실무]

Navigation Debug Flow:

```text
Navigation Problem
→ User Action 확인
→ 사용 도구 확인
→ Link / NavLink / useNavigate / Navigate 선택 적절성 확인
→ target path 확인
→ Route path 확인
→ BrowserRouter 내부 여부 확인
→ location.state 존재 여부 확인
→ auth loading 확인
→ redirect loop 확인
```

대표 문제 1:

```text
문제: Link 클릭 후 NotFoundPage
원인: Link to와 Route path 불일치
해결: Route Constants 또는 path builder 사용
```

대표 문제 2:

```text
문제: 로그인 후 뒤로가면 login 페이지로 돌아감
원인: replace 옵션 누락
해결: navigate("/", { replace: true }) 또는 <Navigate replace />
```

대표 문제 3:

```text
문제: 새로고침 후 location.state 없음
원인: Navigation State는 임시 데이터
해결: fallback path 사용 또는 Query String / Storage 검토
```

---

### [FAQ]

Q. React Router Navigation 문제는 어떻게 찾는 게 좋아?
A. 사용한 이동 도구, target path, Route path, BrowserRouter 내부 여부, location.state, redirect 조건을 순서대로 확인한다.

Q. 로그인 후 뒤로가면 login으로 돌아와?
A. 로그인 성공 이동이나 redirect에 replace 옵션을 적용하는 것을 검토한다.

Q. URL은 바뀌는데 원하는 화면이 안 나와?
A. target path와 Route path가 일치하는지, NotFoundRoute로 빠지는지 확인한다.

Q. Navigation State가 사라졌어?
A. Navigation State는 임시 데이터이므로 새로고침이나 직접 접근 시 없을 수 있다.

---

# Retrieval Queries

### [FAQ]

Q. React Router Part02는 뭘 다뤄?
A. Link, NavLink, useNavigate, Navigate, useLocation, Navigation State와 Navigation 선택 기준을 다룬다.

Q. React Router Navigation은 뭐야?
A. SPA 내부에서 URL을 변경하고 해당 Route의 Component를 렌더링하는 이동 구조다.

Q. Client Side Navigation이 뭐야?
A. 서버에서 새 HTML을 받지 않고 브라우저 안에서 URL과 Component를 바꾸는 이동 방식이다.

Q. 내부 페이지 이동은 뭘 써?
A. 사용자가 클릭하는 일반 내부 이동은 Link 또는 NavLink를 사용한다.

Q. 외부 사이트 이동은 뭘 써?
A. 외부 URL 이동은 일반 a 태그를 사용한다.

Q. React Router에서 a 태그 대신 Link를 쓰는 이유는?
A. 내부 Route 이동 시 페이지 전체 reload 없이 React Router가 URL과 화면을 갱신하기 위해서다.

Q. Link는 뭐야?
A. Link는 React Router에서 페이지 전체 reload 없이 내부 Route로 이동하기 위한 Component다.

Q. Link의 to에는 뭘 넣어?
A. 이동할 내부 Route path를 넣는다. 예: `/login`, `/festivals/1`.

Q. Link 클릭 후 NotFoundPage가 나와?
A. Link to와 Route path가 일치하는지 확인해야 한다.

Q. `/festivals/:festivalId`를 Link to에 넣어도 돼?
A. 안 된다. Link에는 `/festivals/1`처럼 실제 값이 들어간 URL을 넣어야 한다.

Q. 내부 이동에 a href를 쓰면 안 돼?
A. 가능은 하지만 전체 reload가 발생할 수 있어 SPA 내부 이동에는 Link를 권장한다.

Q. NavLink는 뭐야?
A. NavLink는 현재 URL과 일치하는 링크에 active 상태를 적용할 수 있는 Link 확장 Component다.

Q. Link와 NavLink 차이는?
A. Link는 단순 이동이고 NavLink는 현재 URL과 일치할 때 active 상태를 알 수 있다.

Q. NavLink는 언제 써?
A. Header, Sidebar, Tab Menu처럼 현재 선택된 메뉴 표시가 필요할 때 사용한다.

Q. NavLink active class는 어떻게 줘?
A. className callback에서 isActive 값을 확인해 active class를 반환한다.

Q. NavLink active가 안 먹어?
A. NavLink to와 현재 URL이 일치하는지, className callback과 CSS active class가 맞는지 확인한다.

Q. 모든 Link를 NavLink로 바꿔도 돼?
A. 권장하지 않는다. 현재 메뉴 표시가 필요한 Navigation UI에만 NavLink를 쓰는 것이 좋다.

Q. 현재 path 비교는 useLocation으로 직접 해야 해?
A. 메뉴 active 표시 목적이면 NavLink를 우선 사용한다.

Q. useNavigate는 뭐야?
A. useNavigate는 코드에서 명령형으로 Route 이동을 수행하는 React Router Hook이다.

Q. useNavigate는 언제 써?
A. 로그인 성공, 저장 완료, 삭제 완료, 권한 없음 redirect처럼 코드 흐름에 따라 이동할 때 사용한다.

Q. Link와 useNavigate 중 뭐를 써?
A. 사용자가 클릭해서 이동하는 일반 링크는 Link를 우선하고, 로그인 성공 후 이동처럼 코드 흐름에 따른 이동은 useNavigate를 사용한다.

Q. 로그인 성공 후 이동은 Link야 useNavigate야?
A. 로그인 처리 성공 후 코드 흐름에 따라 이동하므로 useNavigate가 적합하다.

Q. 상세 페이지 이동은 Link야 useNavigate야?
A. 사용자가 목록에서 상세를 클릭하는 구조라면 Link가 적합하다.

Q. navigate replace는 언제 써?
A. 로그인 페이지 redirect처럼 사용자가 뒤로가기로 다시 돌아오면 안 되는 경우에 사용한다.

Q. useNavigate를 Router 밖에서 쓸 수 있어?
A. 안 된다. Router 내부 Component에서만 사용할 수 있다.

Q. useNavigate 에러가 나면 뭘 확인해?
A. 해당 Component가 BrowserRouter 내부인지, navigate 호출 위치가 Event Handler나 Effect 내부인지 확인한다.

Q. 렌더링 중 navigate를 호출해도 돼?
A. 권장하지 않는다. 조건부 redirect는 Navigate Component를 사용하는 것이 명확하다.

Q. Navigate는 뭐야?
A. Navigate는 렌더링 결과로 redirect를 수행하는 React Router Component다.

Q. Navigate와 useNavigate 차이는?
A. Navigate는 렌더링 결과로 redirect하고 useNavigate는 함수 호출로 이동한다.

Q. Protected Route에는 Navigate를 써도 돼?
A. 가능하다. 인증 상태에 따라 login 페이지로 redirect할 때 자주 사용한다.

Q. Navigate의 replace는 왜 써?
A. 뒤로가기로 redirect 이전 페이지에 다시 돌아가는 것을 방지하기 위해 사용한다.

Q. 인증 상태 확인 전 바로 login으로 보내도 돼?
A. 권장하지 않는다. 인증 상태 loading 중에는 임시 로딩 UI를 보여주고 확인 후 redirect해야 한다.

Q. redirect loop는 왜 생겨?
A. 인증 조건이나 redirect target이 잘못되어 login과 protected page 사이를 계속 오갈 때 발생한다.

Q. Frontend Navigate만 있으면 API도 보호돼?
A. 아니다. API 보호는 Backend 인증/인가가 반드시 처리해야 한다.

Q. useLocation은 뭐야?
A. useLocation은 현재 URL location 정보를 읽는 React Router Hook이다.

Q. useLocation은 언제 써?
A. 현재 URL path, search, state 정보가 필요할 때 사용한다.

Q. location.pathname은 뭐야?
A. 현재 URL의 path 부분이다. 예: `/festivals/1`.

Q. location.search는 뭐야?
A. 현재 URL의 query string 부분이다. 예: `?keyword=flower&page=1`.

Q. location.state는 뭐야?
A. Navigation 시 URL에 보이지 않게 전달한 임시 데이터다.

Q. location.state는 새로고침해도 남아?
A. 보장되지 않는다. 영구적으로 유지해야 하는 정보는 query string이나 storage를 고려한다.

Q. Navigation State는 뭐야?
A. Route 이동 시 URL에 보이지 않는 임시 데이터를 함께 전달하는 방식이다.

Q. Navigation State는 언제 써?
A. 로그인 후 돌아갈 경로처럼 임시 이동 정보를 전달할 때 사용한다.

Q. Navigation State는 URL에 보여?
A. 아니다. URL에는 보이지 않고 location.state로 읽는다.

Q. Navigation State에 중요한 데이터를 넣어도 돼?
A. 권장하지 않는다. 새로고침이나 직접 접근 시 사라질 수 있고 민감정보 전달에 부적합하다.

Q. location.state가 undefined야?
A. 직접 접근, 새로고침, state 없이 이동한 경우일 수 있으므로 optional chaining과 fallback 값을 사용한다.

Q. 검색 조건을 Navigation State로 넘겨도 돼?
A. 권장하지 않는다. 검색, 필터, 정렬, 페이지 조건은 Query String이 더 적합하다.

Q. 로그인 후 원래 페이지로 돌아가려면?
A. location.state나 query string에 redirect target을 저장해 로그인 성공 후 이동할 수 있다.

Q. Link와 NavLink 중 뭘 써야 해?
A. 단순 내부 이동은 Link, 현재 선택된 메뉴 표시가 필요하면 NavLink를 사용한다.

Q. Navigate와 useNavigate 중 뭘 써야 해?
A. 렌더링 조건에 따른 redirect는 Navigate, 이벤트나 비동기 처리 후 이동은 useNavigate를 사용한다.

Q. React Router Navigation 문제는 어떻게 찾는 게 좋아?
A. 사용한 이동 도구, target path, Route path, BrowserRouter 내부 여부, location.state, redirect 조건을 순서대로 확인한다.

Q. 로그인 후 뒤로가면 login으로 돌아와?
A. 로그인 성공 이동이나 redirect에 replace 옵션을 적용하는 것을 검토한다.

Q. URL은 바뀌는데 원하는 화면이 안 나와?
A. target path와 Route path가 일치하는지, NotFoundRoute로 빠지는지 확인한다.

Q. Part02 다음에는 뭘 다뤄?
A. Part03 Params SearchParams에서 Dynamic Route, useParams, Path Parameter, Query String, useSearchParams를 다룬다.
