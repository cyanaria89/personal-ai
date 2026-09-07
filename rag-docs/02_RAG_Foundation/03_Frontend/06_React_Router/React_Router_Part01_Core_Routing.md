# React Router Part01 Core Routing

---

# 1. React Router Core Routing

## 1.1 React Router Purpose

### [개념]

React Router는 React SPA에서 URL path와 Page Component를 연결하는 Client Side Router다.

React Router는 서버가 HTML 페이지를 매번 새로 내려주는 방식이 아니라, 브라우저 안에서 현재 URL에 맞는 React Component를 렌더링한다.

React Router 문서는 Frontend Agent가 화면 URL 구조를 설계하고 Page Component를 안정적으로 연결하도록 지원한다.

---

### [핵심]

- React Router
- React Routing
- SPA Routing
- Client Side Routing
- URL path
- Page Component
- Route Matching
- BrowserRouter
- Routes
- Route
- React Element
- Not Found Route
- SPA Fallback Awareness

React Router 핵심 역할:

- URL과 Component 연결
- 페이지 전환 시 전체 reload 방지
- SPA 화면 흐름 구성
- 상세 페이지 Dynamic Route 구성
- 중첩 Route와 Layout Route 기반 제공
- 인증 Route와 Not Found Route 기반 제공

---

### [실무]

2026 실무 기준에서 React Router는 단순 페이지 이동 도구가 아니다.

React Router는 Frontend 화면 구조의 기본 골격이다.

실무 사용 대상:

- 메인 페이지
- 로그인 페이지
- 회원가입 페이지
- 목록 페이지
- 상세 페이지
- 마이페이지
- 관리자 페이지
- 404 페이지
- 인증 필요 페이지
- Layout 포함 페이지

예상 URL 구조:

```text
/
├ /login
├ /signup
├ /festivals
├ /festivals/:festivalId
├ /mypage
├ /admin
└ *
```

React Router 설계 Flow:

```text
User Page Flow
→ Define URL Path
→ Create Page Component
→ Connect Route path and element
→ Add Navigation
→ Add Not Found Route
→ Check Refresh / Fallback
```

---

### [FAQ]

Q. React Router는 뭐야?
A. React SPA에서 URL path에 따라 어떤 Component를 렌더링할지 결정하는 Client Side Router다.

Q. React Router는 Backend Router야?
A. 아니다. React Router는 브라우저에서 동작하고 Backend Router는 서버 요청 URL을 처리한다.

Q. React Router 문서는 왜 필요해?
A. Frontend Agent가 URL과 Page Component를 연결하고 SPA 화면 흐름을 설계해야 하기 때문이다.

Q. React Router의 핵심은 뭐야?
A. BrowserRouter, Routes, Route, Link, useNavigate, useParams, useSearchParams, Outlet, Protected Route, Not Found Route다.

---

# 2. SPA Routing

## 2.1 SPA Routing Concept

### [개념]

SPA Routing은 Single Page Application에서 페이지 전체를 다시 로드하지 않고 URL에 맞는 React Component를 브라우저 안에서 바꾸는 방식이다.

React Router는 SPA Routing을 구현하기 위한 대표적인 React Routing 라이브러리다.

기본 Flow:

```text
User Navigation
→ URL Change
→ React Router Route Matching
→ Page Component Render
→ UI Update
```

---

### [핵심]

- SPA는 Single Page Application
- React Router는 Client Side Routing 담당
- URL 변경 시 서버 HTML 재요청 없이 화면 전환
- Browser History API 사용 가능
- 내부 이동은 Link / NavLink / useNavigate 사용
- 서버는 최초 entry file을 제공
- 직접 URL 접근과 새로고침은 SPA Fallback 설정 필요 가능

Client Side Routing 특징:

- 빠른 화면 전환
- Component 기반 Page 관리
- URL 공유 가능
- 뒤로가기 / 앞으로가기 가능
- 서버 Route와 역할 분리 필요

---

### [실무]

React SPA에서 Router는 Page 단위 화면을 연결한다.

예:

```text
URL: /
→ MainPage

URL: /login
→ LoginPage

URL: /festivals
→ FestivalListPage

URL: /festivals/1
→ FestivalDetailPage

URL: /unknown
→ NotFoundPage
```

실무 주의:

- React Router는 브라우저 내부 화면 전환 담당
- Backend API 요청과 React Route 이동을 혼동하지 않음
- 배포 환경에서는 `/festivals/1` 직접 접근 시 서버 fallback 필요
- API path와 Frontend Route path를 분리하는 것이 안전
- BrowserRouter 사용 시 clean URL 가능
- HashRouter는 fallback 문제를 줄일 수 있지만 URL 품질이 낮음

---

### [FAQ]

Q. SPA Routing이 뭐야?
A. 페이지 전체를 다시 로드하지 않고 URL에 맞는 React Component를 브라우저 안에서 렌더링하는 방식이다.

Q. SPA Routing은 서버가 처리해?
A. 아니다. React Router가 브라우저에서 URL과 Component를 매칭한다.

Q. React Router를 쓰면 새로고침해도 항상 정상 동작해?
A. 아니다. 배포 서버가 SPA 경로를 index.html로 fallback하도록 설정해야 할 수 있다.

Q. Client Side Routing의 장점은 뭐야?
A. 전체 페이지 reload 없이 빠르게 화면을 전환하고 React Component 중심으로 Page를 관리할 수 있다.

---

## 2.2 Client Side Routing vs Server Side Routing

### [개념]

Client Side Routing은 브라우저가 URL에 맞는 Component를 렌더링하는 방식이다.

Server Side Routing은 서버가 URL 요청을 받아 HTML, JSON, 파일 등을 응답하는 방식이다.

React Router는 Client Side Routing에 속한다.

---

### [핵심]

| 비교                    | Client Side Routing             | Server Side Routing     |
| ----------------------- | ------------------------------- | ----------------------- |
| 처리 위치               | Browser                         | Server                  |
| React Router 역할       | URL과 Component 매칭            | 해당 없음               |
| Backend Controller 역할 | 해당 없음                       | URL 요청 처리           |
| 화면 전환               | Component 교체                  | 서버 응답 기반          |
| 새로고침                | fallback 필요 가능              | 서버 Route 필요         |
| 예                      | `/festivals` → FestivalListPage | `/api/festivals` → JSON |

핵심 구분:

```text
Frontend Route
→ 화면 URL
→ React Component 렌더링

Backend API Route
→ 서버 URL
→ JSON / 데이터 응답
```

---

### [실무]

권장 구조:

```text
Frontend Route
/
 /login
 /festivals
 /festivals/:festivalId
 /mypage

Backend API
/api/auth/login
/api/festivals
/api/festivals/{festivalId}
/api/users/me
```

실무 기준:

- Frontend 화면 경로와 Backend API 경로를 분리
- Backend API는 `/api` prefix 사용 권장
- React Route와 Spring Controller 경로 충돌 주의
- SPA Fallback이 API 요청을 가로채지 않도록 설계
- Axios URL과 React Router path를 혼동하지 않음

문제 예:

```text
GET /festival
→ React Page Route인지 Backend API인지 모호함
```

권장 예:

```text
GET /festivals
→ Frontend Page Route

GET /api/festivals
→ Backend API Endpoint
```

---

### [FAQ]

Q. Client Side Routing과 Server Side Routing 차이는?
A. Client Side Routing은 브라우저에서 Component를 바꾸고 Server Side Routing은 서버가 URL 요청을 처리한다.

Q. React Router Route와 API Endpoint는 같은 거야?
A. 아니다. React Router Route는 화면 URL이고 API Endpoint는 서버 데이터 요청 URL이다.

Q. Backend API에 `/api` prefix를 붙이는 이유는?
A. Frontend Route와 충돌을 줄이고 SPA Fallback에서 API 요청을 제외하기 쉽기 때문이다.

Q. API 요청했는데 index.html이 오면 왜 그래?
A. SPA Fallback이 API 요청까지 forward했거나 API path와 Frontend Route가 충돌했을 가능성이 있다.

---

# 3. BrowserRouter

## 3.1 BrowserRouter Purpose

### [개념]

BrowserRouter는 브라우저 History API를 사용해 React Router가 URL을 관리하도록 하는 Router Provider다.

React 앱에서 Router 기능을 사용할 수 있도록 App 또는 AppRoutes 상위에서 감싼다.

---

### [핵심]

- BrowserRouter
- History API
- Router Provider
- App root wrapping
- Client Side Navigation
- Clean URL
- Router Hook 사용 가능 범위 제공
- SPA Fallback 필요 가능

BrowserRouter 역할:

```text
BrowserRouter
→ Provide Router Context
→ Track URL
→ Enable Route Matching
→ Enable Link / useNavigate / useParams
→ Render Matched Route
```

---

### [실무]

React entry point 예:

```jsx
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router";
import App from "./App";

ReactDOM.createRoot(document.getElementById("root")).render(
  <BrowserRouter>
    <App />
  </BrowserRouter>,
);
```

기존 React Router v6 프로젝트 예:

```jsx
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";
import App from "./App";

ReactDOM.createRoot(document.getElementById("root")).render(
  <BrowserRouter>
    <App />
  </BrowserRouter>,
);
```

실무 기준:

- BrowserRouter는 보통 main.jsx / main.tsx / index.jsx에 배치
- 앱 전체를 한 번만 감싸는 구조 권장
- Router Hook은 BrowserRouter 내부 Component에서만 사용
- BrowserRouter 외부에서 useNavigate / useParams / useLocation 사용 금지
- 배포 환경에서는 새로고침 404 방지를 위한 서버 fallback 검토

---

### [FAQ]

Q. BrowserRouter는 어디에 둬?
A. 보통 main.jsx, main.tsx, index.jsx 같은 React entry point에서 App을 감싼다.

Q. BrowserRouter를 여러 번 감싸도 돼?
A. 일반적으로 앱 전체를 한 번만 감싼다. 중첩 Router는 라우팅 혼란을 만들 수 있다.

Q. BrowserRouter 없이 Routes를 써도 돼?
A. 안 된다. Routes, Route, Link, Router Hook이 동작하려면 Router Context가 필요하다.

Q. BrowserRouter를 쓰면 서버 설정이 필요해?
A. 배포 환경에서 직접 URL 접근과 새로고침을 지원하려면 SPA Fallback 설정이 필요할 수 있다.

---

## 3.2 BrowserRouter Common Mistakes

### [개념]

BrowserRouter 관련 오류는 Router Context 누락, 중복 Router, 배포 fallback 누락에서 자주 발생한다.

---

### [핵심]

자주 발생하는 실수:

- BrowserRouter로 App을 감싸지 않음
- BrowserRouter를 여러 곳에서 중복 사용
- Router Hook을 Router 밖에서 사용
- BrowserRouter와 RouterProvider를 혼용
- React Router import 경로 혼용
- 배포 후 직접 URL 접근 404 발생
- basename 설정 누락
- HashRouter와 BrowserRouter 기준 혼동

---

### [실무]

문제 예:

```jsx
function LoginButton() {
  const navigate = useNavigate();

  return <button onClick={() => navigate("/login")}>Login</button>;
}

function Root() {
  return <LoginButton />;
}
```

문제:

```text
LoginButton이 BrowserRouter 내부에 없으면 useNavigate 사용 불가
```

해결 예:

```jsx
function Root() {
  return (
    <BrowserRouter>
      <LoginButton />
    </BrowserRouter>
  );
}
```

Debug Flow:

```text
Router Error 발생
→ BrowserRouter Wrapping 확인
→ Router Hook 위치 확인
→ 중복 Router 확인
→ import 경로 확인
→ 배포 fallback 확인
```

---

### [FAQ]

Q. useNavigate를 썼는데 Router 관련 에러가 나?
A. 해당 Component가 BrowserRouter 내부에서 렌더링되는지 확인해야 한다.

Q. BrowserRouter를 App 안에 둬도 돼?
A. 가능하지만 보통 entry point에서 App 전체를 감싸는 방식이 명확하다.

Q. BrowserRouter와 RouterProvider를 같이 써도 돼?
A. 일반적으로 같이 쓰지 않는다. BrowserRouter 방식과 createBrowserRouter 방식을 하나 선택한다.

Q. 배포 후 새로고침 404는 BrowserRouter 문제야?
A. BrowserRouter 자체 문제라기보다 서버가 SPA 경로를 index.html로 fallback하지 않는 문제일 가능성이 크다.

---

# 4. Routes and Route

## 4.1 Routes and Route Concept

### [개념]

Routes는 여러 Route를 감싸고 현재 URL에 맞는 Route를 선택하는 매칭 영역이다.

Route는 URL path와 렌더링할 React Element를 연결한다.

---

### [핵심]

- Routes
- Route
- path
- element
- React Element
- Route Matching
- Page Component
- Dynamic Route
- Catch All Route
- Not Found Route

기본 구조:

```jsx
<Routes>
  <Route path="/" element={<MainPage />} />
  <Route path="/login" element={<LoginPage />} />
  <Route path="/festivals" element={<FestivalListPage />} />
  <Route path="/festivals/:festivalId" element={<FestivalDetailPage />} />
  <Route path="*" element={<NotFoundPage />} />
</Routes>
```

핵심 규칙:

- `Routes`는 Route 매칭 영역
- `Route`는 path와 element 연결
- `path`는 URL pattern
- `element`는 렌더링할 JSX Element
- `:paramName`은 Dynamic Route
- `*`는 catch-all route

---

### [실무]

Route 정의는 보통 AppRoutes 파일로 분리한다.

예:

```jsx
import { Routes, Route } from "react-router";
import MainPage from "../pages/MainPage";
import LoginPage from "../pages/LoginPage";
import FestivalListPage from "../pages/FestivalListPage";
import FestivalDetailPage from "../pages/FestivalDetailPage";
import NotFoundPage from "../pages/NotFoundPage";

function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<MainPage />} />
      <Route path="/login" element={<LoginPage />} />
      <Route path="/festivals" element={<FestivalListPage />} />
      <Route path="/festivals/:festivalId" element={<FestivalDetailPage />} />
      <Route path="*" element={<NotFoundPage />} />
    </Routes>
  );
}

export default AppRoutes;
```

실무 권장:

- Route 정의는 한 곳에 모아 관리
- Page Component와 Route 연결 명확화
- NotFoundPage route 포함
- path 문자열 오타 방지
- Link to 값과 Route path 정합성 확인
- 인증 필요 Route는 Protected Route로 감싸기
- 공통 Layout은 Layout Route로 분리

---

### [FAQ]

Q. Routes와 Route는 어떻게 써?
A. Routes 안에 Route를 두고 path와 element를 연결한다.

Q. Route의 element에는 뭘 넣어?
A. 렌더링할 React Element를 넣는다. 예: `element={<LoginPage />}`.

Q. Route element에 Component 함수 자체를 넣어도 돼?
A. React Router v6+ 기준으로 `element={<LoginPage />}`처럼 JSX Element를 넣는다.

Q. Route path와 Link to가 다르면 어떻게 돼?
A. 사용자가 이동해도 원하는 Route가 매칭되지 않아 빈 화면이나 NotFoundPage가 나올 수 있다.

---

## 4.2 Route Path Design

### [개념]

Route Path Design은 서비스의 화면 URL을 일관성 있게 설계하는 기준이다.

React Router의 path는 사용자에게 보이는 화면 경로이며 Page Component 구조와 연결된다.

---

### [핵심]

Route path 설계 기준:

- 명확한 리소스 이름 사용
- 복수형 경로 사용 가능
- 상세 페이지는 Dynamic Route 사용
- 검색 조건은 Query String 사용
- 인증 페이지와 서비스 페이지 구분
- 관리자 페이지는 별도 prefix 사용 가능
- Catch All Route 포함

예:

```text
/
 /login
 /signup
 /festivals
 /festivals/:festivalId
 /mypage
 /admin
 /*
```

---

### [실무]

축제 서비스 예:

```text
Route Path
/                         → MainPage
/login                    → LoginPage
/signup                   → SignupPage
/festivals                → FestivalListPage
/festivals/:festivalId    → FestivalDetailPage
/festivals?keyword=꽃      → FestivalSearchPage or FestivalListPage
/mypage                   → MyPage
/admin                    → AdminPage
*                         → NotFoundPage
```

권장 기준:

```text
Resource List → /resources
Resource Detail → /resources/:resourceId
Filter / Search → /resources?keyword=value
User Area → /mypage
Admin Area → /admin
Unknown Route → *
```

주의:

- `/festival`과 `/festivals` 혼용 금지
- `/festival/:id`와 `/festivals/:festivalId` 혼용 금지
- Route path와 API endpoint를 동일하게 설계하지 않음
- URL 의미가 예측 가능해야 함
- 실제 Link 생성과 Route pattern 정합성 유지

---

### [FAQ]

Q. 목록 페이지 Route는 어떻게 잡아?
A. 보통 `/resources` 형태를 사용한다. 예: `/festivals`.

Q. 상세 페이지 Route는 어떻게 잡아?
A. 보통 `/resources/:resourceId` 형태를 사용한다. 예: `/festivals/:festivalId`.

Q. 검색 조건은 Route path에 넣어?
A. 검색, 필터, 정렬, 페이지 조건은 Query String으로 관리하는 것이 일반적이다.

Q. `/festival`과 `/festivals` 중 뭘 써야 해?
A. 프로젝트 기준으로 하나만 정해 통일한다. 목록/상세 리소스 구조에서는 복수형 `/festivals`가 자주 사용된다.

---

# 5. Route Constants

## 5.1 Route Constants Concept

### [개념]

Route Constants는 Route path 문자열을 상수로 관리하는 방식이다.

경로 오타, 중복 문자열, Link와 Route 불일치를 줄이기 위해 사용한다.

---

### [핵심]

- Route Constants
- path constants
- route map
- path builder
- Dynamic Route pattern
- Link URL generation
- Navigation consistency
- Redirect path consistency

Route Constants 사용 대상:

- Route 정의
- Navigation Menu
- Link to
- useNavigate target
- Protected Route redirect
- 상세 페이지 URL 생성
- 테스트 기준 path

---

### [실무]

기본 예:

```javascript
export const ROUTES = {
  HOME: "/",
  LOGIN: "/login",
  SIGNUP: "/signup",
  FESTIVALS: "/festivals",
  FESTIVAL_DETAIL: "/festivals/:festivalId",
  MYPAGE: "/mypage",
  ADMIN: "/admin",
  NOT_FOUND: "*",
};
```

상세 URL 생성 함수:

```javascript
export function createFestivalDetailPath(festivalId) {
  return `/festivals/${festivalId}`;
}
```

Route 정의 사용:

```jsx
<Route path={ROUTES.FESTIVALS} element={<FestivalListPage />} />
<Route path={ROUTES.FESTIVAL_DETAIL} element={<FestivalDetailPage />} />
```

Link 사용:

```jsx
<Link to={createFestivalDetailPath(festival.festivalId)}>{festival.title}</Link>
```

실무 장점:

- path 오타 감소
- 경로 변경 시 수정 범위 감소
- Route와 Navigation 정합성 유지
- Dynamic Route 생성 실수 감소
- Frontend Agent가 URL 기준을 일관되게 사용 가능

---

### [FAQ]

Q. Route path를 상수로 꼭 관리해야 해?
A. 작은 프로젝트는 직접 문자열도 가능하지만 경로가 많아지면 상수 관리가 오타를 줄인다.

Q. 동적 path도 상수로 관리해?
A. Route pattern은 상수로 두고 실제 이동 URL은 path builder 함수로 만드는 것이 좋다.

Q. Route Constants를 쓰면 뭐가 좋아?
A. Route 정의, Link, navigate, redirect 경로를 일관되게 관리할 수 있다.

Q. path builder 함수는 왜 필요해?
A. `/festivals/:festivalId`는 Route pattern이고 실제 이동 URL은 `/festivals/1`처럼 만들어야 하기 때문이다.

---

## 5.2 Route Constants Common Mistakes

### [개념]

Route Constants를 사용해도 pattern과 실제 URL을 혼동하면 잘못된 이동이나 params undefined 문제가 발생할 수 있다.

---

### [핵심]

자주 발생하는 실수:

- Dynamic Route pattern을 Link to에 그대로 사용
- path builder 없이 문자열 직접 조합 반복
- Route path와 constants 값 불일치
- Navigation 메뉴에서 오래된 path 사용
- redirect path와 실제 Route 불일치
- `/festival`과 `/festivals` 혼용
- `:id`와 `:festivalId` param 이름 혼용

---

### [실무]

나쁜 예:

```jsx
<Link to={ROUTES.FESTIVAL_DETAIL}>Detail</Link>
```

문제:

```text
ROUTES.FESTIVAL_DETAIL = "/festivals/:festivalId"
실제 이동 URL이 "/festivals/:festivalId"가 됨
```

좋은 예:

```jsx
<Link to={createFestivalDetailPath(festival.festivalId)}>Detail</Link>
```

Debug Flow:

```text
Link Click
→ URL Check
→ Route Pattern Check
→ Path Builder Check
→ useParams Key Check
→ Page Render Check
```

---

### [FAQ]

Q. `/festivals/:festivalId`를 Link to에 그대로 넣어도 돼?
A. 안 된다. Link에는 `/festivals/1`처럼 실제 값이 들어간 URL을 넣어야 한다.

Q. Route Constants를 썼는데도 params가 undefined야?
A. Dynamic Route pattern과 실제 URL 생성, useParams key 이름이 일치하는지 확인해야 한다.

Q. Route Constants 파일은 어디에 둬?
A. 보통 `src/routes/routePaths.js` 또는 `src/routes/routePaths.ts`처럼 routes 폴더에 둔다.

---

# 6. Index Route

## 6.1 Index Route Concept

### [개념]

Index Route는 부모 Route 경로에 정확히 매칭될 때 기본으로 렌더링되는 자식 Route다.

Nested Route 구조에서 부모 path의 기본 화면을 지정할 때 사용한다.

---

### [핵심]

- Index Route
- parent route
- default child route
- nested route
- Outlet
- path 없음
- index 속성 사용

예:

```jsx
<Route path="/mypage" element={<MyPageLayout />}>
  <Route index element={<MyPageHome />} />
  <Route path="profile" element={<ProfilePage />} />
  <Route path="favorites" element={<FavoritePage />} />
</Route>
```

동작:

```text
/mypage
→ MyPageLayout
→ MyPageHome rendered in Outlet

/mypage/profile
→ MyPageLayout
→ ProfilePage rendered in Outlet
```

---

### [실무]

Index Route 사용 상황:

- `/mypage` 기본 화면
- `/admin` dashboard 기본 화면
- `/settings` 기본 설정 화면
- `/festivals/:festivalId` 상세 기본 탭
- Layout 안의 기본 content

주의:

- index route에는 path를 쓰지 않음
- 부모 Component에는 Outlet 필요
- index route와 child path route 구분
- 중첩 Route 구조에서 사용
- Flat Route에서는 필수 아님

---

### [FAQ]

Q. Index Route는 언제 써?
A. 부모 경로에 들어왔을 때 기본으로 보여줄 자식 화면이 필요할 때 사용한다.

Q. Index Route에 path를 써도 돼?
A. 아니다. index route는 path 없이 `index` 속성을 사용한다.

Q. Index Route가 안 보여?
A. 부모 Layout Component에 `<Outlet />`이 없거나 부모 Route 구조가 잘못되었을 수 있다.

Q. `/mypage` 기본 화면은 어떻게 만들면 돼?
A. `/mypage` 부모 Route 아래에 `<Route index element={<MyPageHome />} />`를 둔다.

---

# 7. Not Found Route Basics

## 7.1 Catch All Route

### [개념]

Catch All Route는 어떤 Route와도 매칭되지 않은 URL에 대해 NotFoundPage를 렌더링하는 Route다.

React Router에서는 `path="*"`를 사용한다.

---

### [핵심]

- Not Found Route
- Catch All Route
- `path="*"`
- NotFoundPage
- invalid URL
- unknown route
- fallback UI
- home link
- navigation back

예:

```jsx
<Route path="*" element={<NotFoundPage />} />
```

---

### [실무]

NotFoundPage 예:

```jsx
import { Link } from "react-router";

function NotFoundPage() {
  return (
    <main>
      <h1>페이지를 찾을 수 없습니다.</h1>
      <p>요청한 주소가 존재하지 않습니다.</p>
      <Link to="/">메인으로 이동</Link>
    </main>
  );
}

export default NotFoundPage;
```

실무 기준:

- 전체 Route 마지막에 catch-all route 포함
- 잘못된 URL에서 빈 화면 방지
- 메인 이동 링크 제공
- 이전 페이지 이동 버튼 제공 가능
- Layout 포함 여부 결정
- SPA 404와 서버 404 차이 인지

주의:

- `path="*"`는 React Router 내부 매칭 실패 처리
- 서버 404와 동일하지 않음
- 배포 환경 직접 접근 404는 서버 fallback 문제일 수 있음
- 중첩 Route에서는 local 404와 global 404 구분 가능

---

### [FAQ]

Q. React Router에서 404 페이지는 어떻게 만들어?
A. `path="*"` Route를 추가하고 NotFoundPage를 렌더링한다.

Q. NotFound Route가 없으면 어떻게 돼?
A. 매칭되지 않는 URL에서 빈 화면처럼 보일 수 있다.

Q. SPA 404와 서버 404는 달라?
A. 다르다. SPA 404는 React Router가 매칭 실패를 처리하는 화면이고 서버 404는 서버가 경로나 파일을 찾지 못한 응답이다.

Q. 배포 후 `/festivals/1` 새로고침 404는 NotFoundPage 문제야?
A. 대부분 NotFoundPage보다 서버 fallback 설정 문제일 가능성이 크다.

---

# 8. React Router Version Awareness

## 8.1 React Router v6 and v7 Awareness

### [개념]

React Router는 버전에 따라 import 경로, Router 구성 방식, Data Router 기능, Framework Mode 기능이 달라질 수 있다.

Foundation 문서는 Modern React Router 기준으로 작성한다.

---

### [핵심]

기준:

- React Router v6+
- React Router v7 Awareness
- React 18+
- React 19 Compatibility Awareness
- Declarative Routing
- BrowserRouter
- Routes
- Route
- Link
- useNavigate
- useParams
- useSearchParams
- Nested Route
- Outlet
- Protected Route
- Data Router Basics Mention

Legacy 제외:

- Switch 중심 설명
- exact 중심 설명
- component prop 중심 설명
- useHistory 중심 설명
- withRouter 중심 설명
- class component routing 중심 설명
- v5 route order 중심 설명

---

### [실무]

React Router v7 공식 문서 스타일 예:

```jsx
import { BrowserRouter, Routes, Route } from "react-router";
```

React Router v6 프로젝트에서 흔한 예:

```jsx
import { BrowserRouter, Routes, Route } from "react-router-dom";
```

실무 기준:

- 프로젝트에 설치된 React Router 버전 확인
- 기존 코드 컨벤션 우선
- 한 프로젝트에서 import 경로 혼용 금지
- v5 문법과 v6+ 문법 혼용 금지
- BrowserRouter 방식과 RouterProvider 방식 혼용 금지
- Foundation 단계에서는 BrowserRouter + Routes + Route 중심

---

### [FAQ]

Q. React Router import는 react-router야 react-router-dom이야?
A. 프로젝트 버전에 따라 다를 수 있다. v6 프로젝트는 react-router-dom이 흔하고 v7 공식 문서는 react-router 예제를 제공할 수 있다. 프로젝트 기준으로 통일한다.

Q. Switch를 써야 해?
A. 아니다. React Router v6+에서는 Routes를 사용한다.

Q. useHistory를 써야 해?
A. 아니다. React Router v6+에서는 useNavigate를 사용한다.

Q. exact를 써야 해?
A. 아니다. React Router v6+의 Route 매칭 방식에서는 v5처럼 exact를 쓰지 않는다.

---

# 9. Core Routing Checklist

## 9.1 Part01 Checklist

### [개념]

Core Routing 문서는 React Router의 기본 골격을 검수하기 위한 기준을 포함한다.

---

### [핵심]

Checklist:

```md
- [ ] React Router 목적이 설명되었는가?
- [ ] SPA Routing 개념이 포함되었는가?
- [ ] Client Side Routing과 Server Side Routing 차이가 포함되었는가?
- [ ] BrowserRouter 위치가 설명되었는가?
- [ ] BrowserRouter 주의사항이 포함되었는가?
- [ ] Routes / Route 기본 예제가 포함되었는가?
- [ ] Route path와 element 개념이 설명되었는가?
- [ ] Route path 설계 기준이 포함되었는가?
- [ ] Route Constants 기준이 포함되었는가?
- [ ] Dynamic Route pattern과 실제 URL 차이가 언급되었는가?
- [ ] Index Route 기본 개념이 포함되었는가?
- [ ] Not Found Route 기본이 포함되었는가?
- [ ] React Router v6 / v7 차이 주의가 포함되었는가?
- [ ] Common Mistakes가 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 Flow:

```text
Draft
→ React Router Purpose Check
→ SPA Routing Check
→ BrowserRouter Check
→ Routes / Route Check
→ Route Path Design Check
→ Route Constants Check
→ Index Route Check
→ Not Found Route Check
→ Version Awareness Check
→ FAQ Check
→ Retrieval Queries Check
→ Final Review
```

---

### [FAQ]

Q. React Router Part01 검수에서 가장 중요한 것은?
A. React Router 목적, SPA Routing, BrowserRouter, Routes / Route, Route path 설계, Not Found Route 포함 여부다.

Q. Part01에서 Protected Route까지 깊게 다뤄?
A. 아니다. Part01은 Core Routing이고 Protected Route는 별도 Part에서 다룬다.

Q. Part01에서 SPA Fallback을 깊게 다뤄?
A. 아니다. Part01은 awareness만 포함하고 상세 해결은 Deployment / Troubleshooting Part에서 다룬다.

---

# 10. Core Routing Common Mistakes

## 10.1 Common Mistakes

### [개념]

Core Routing에서 자주 발생하는 실수는 Route 매칭 실패, Router Context 누락, path 불일치, version 문법 혼용이다.

---

### [핵심]

자주 발생:

- BrowserRouter로 App을 감싸지 않음
- Router Hook을 BrowserRouter 밖에서 사용
- BrowserRouter를 중복 사용
- BrowserRouter와 RouterProvider를 혼용
- Route element에 JSX Element가 아닌 Component 참조를 잘못 전달
- Route path와 Link to 불일치
- NotFound Route 누락
- Route Constants와 실제 path 불일치
- Dynamic Route pattern을 실제 이동 URL로 사용
- `/festival`과 `/festivals` 혼용
- `react-router`와 `react-router-dom` import 혼용
- React Router v5 문법과 v6+ 문법 혼용
- 새로고침 404를 React 코드 문제로만 판단
- API path와 Frontend Route path 충돌

---

### [실무]

Debug Flow:

```text
Routing Problem
→ URL 확인
→ BrowserRouter 확인
→ Routes / Route path 확인
→ element 확인
→ Link to 확인
→ Route Constants 확인
→ NotFound Route 확인
→ Console Error 확인
→ Network Response 확인
→ Server Fallback 확인
```

잘못된 예:

```jsx
<Route path="/login" element={LoginPage} />
```

권장 예:

```jsx
<Route path="/login" element={<LoginPage />} />
```

잘못된 예:

```jsx
<Link to="/festival/1">Detail</Link>
<Route path="/festivals/:festivalId" element={<FestivalDetailPage />} />
```

문제:

```text
Link to와 Route path가 불일치
```

권장 예:

```jsx
<Link to="/festivals/1">Detail</Link>
<Route path="/festivals/:festivalId" element={<FestivalDetailPage />} />
```

---

### [FAQ]

Q. URL은 바뀌는데 화면이 안 나와?
A. Route path와 Link to가 맞는지, element가 JSX인지, BrowserRouter로 감쌌는지 확인한다.

Q. React Router 초보가 가장 많이 하는 실수는?
A. BrowserRouter 누락, path 오타, element 작성 오류, NotFound Route 누락, import 경로 혼용이다.

Q. v5 문법과 v6+ 문법을 섞으면 어떻게 돼?
A. Switch, exact, component prop, useHistory 같은 v5 문법은 v6+ 기준 코드와 맞지 않아 오류나 혼란을 만든다.

Q. 새로고침 404는 어디부터 확인해?
A. 먼저 서버 응답이 index.html인지 확인하고 SPA Fallback 설정 여부를 점검한다.

---

# Retrieval Queries

### [FAQ]

Q. React Router Part01은 뭘 다뤄?
A. React Router 목적, SPA Routing, BrowserRouter, Routes / Route, Route path 설계, Route Constants, Index Route, Not Found Route 기본을 다룬다.

Q. React Router는 뭐야?
A. React SPA에서 URL path에 따라 어떤 Component를 렌더링할지 결정하는 Client Side Router다.

Q. React Router는 왜 필요해?
A. URL과 Page Component를 연결하고 SPA 화면 이동 구조를 만들기 위해 필요하다.

Q. SPA Routing이 뭐야?
A. 페이지 전체를 다시 로드하지 않고 URL에 맞는 React Component를 브라우저 안에서 렌더링하는 방식이다.

Q. Client Side Routing이 뭐야?
A. 서버가 아니라 브라우저에서 URL에 맞는 Component를 선택해 화면을 바꾸는 방식이다.

Q. Server Side Routing과 Client Side Routing 차이는?
A. Server Side Routing은 서버가 URL 요청을 처리하고 Client Side Routing은 브라우저가 Component를 렌더링한다.

Q. React Router는 서버 요청을 처리해?
A. 아니다. React Router는 브라우저에서 동작하는 Client Side Router다.

Q. Frontend Route와 Backend API Route 차이는?
A. Frontend Route는 화면 URL이고 Backend API Route는 서버 데이터 요청 URL이다.

Q. API path에 /api prefix를 붙이는 이유는?
A. Frontend Route와 Backend API Route 충돌을 줄이고 SPA Fallback에서 API 요청을 제외하기 쉽기 때문이다.

Q. BrowserRouter는 뭐야?
A. BrowserRouter는 브라우저 History API를 사용해 React Router가 URL을 관리하도록 하는 Router Provider다.

Q. BrowserRouter는 어디에 둬?
A. 보통 main.jsx, main.tsx, index.jsx 같은 React entry point에서 App을 감싼다.

Q. BrowserRouter를 여러 번 감싸도 돼?
A. 일반적으로 앱 전체를 한 번만 감싼다. 중첩 Router는 라우팅 혼란을 만들 수 있다.

Q. BrowserRouter 없이 useNavigate를 쓸 수 있어?
A. 안 된다. useNavigate 같은 Router Hook은 BrowserRouter 내부 Component에서만 사용할 수 있다.

Q. BrowserRouter를 쓰면 새로고침 404가 없어져?
A. 아니다. 배포 서버가 SPA 경로를 index.html로 fallback하도록 설정해야 할 수 있다.

Q. Routes는 뭐야?
A. Routes는 여러 Route 중 현재 URL과 매칭되는 Route를 선택하는 영역이다.

Q. Route는 뭐야?
A. Route는 URL path와 렌더링할 React Element를 연결하는 설정이다.

Q. Routes와 Route는 어떻게 써?
A. Routes 안에 Route를 두고 path와 element를 연결한다.

Q. Route의 element에는 뭘 넣어?
A. 렌더링할 React Element를 넣는다. 예: `element={<LoginPage />}`.

Q. Route element에 Component 함수만 넣어도 돼?
A. React Router v6+ 기준으로 `element={<LoginPage />}`처럼 JSX Element를 넣는다.

Q. Route path는 어떻게 설계해?
A. 목록은 `/resources`, 상세는 `/resources/:resourceId`, 검색 조건은 Query String으로 설계하는 것이 일반적이다.

Q. 축제 목록 Route는 어떻게 잡아?
A. 보통 `/festivals`처럼 복수형 리소스 경로를 사용한다.

Q. 축제 상세 Route는 어떻게 잡아?
A. 보통 `/festivals/:festivalId`처럼 Dynamic Route를 사용한다.

Q. 검색 조건은 Route path에 넣어?
A. 검색, 필터, 정렬, 페이지 조건은 Query String으로 관리하는 것이 좋다.

Q. Route Constants는 뭐야?
A. Route path 문자열을 상수로 관리해 오타와 불일치를 줄이는 방식이다.

Q. Route path를 상수로 관리해야 해?
A. 작은 프로젝트는 직접 문자열도 가능하지만 경로가 많아지면 상수 관리가 오타를 줄인다.

Q. Dynamic Route pattern은 Link to에 그대로 써도 돼?
A. 안 된다. `/festivals/:festivalId`는 Route pattern이고 Link에는 `/festivals/1` 같은 실제 URL을 넣어야 한다.

Q. path builder 함수는 왜 필요해?
A. Dynamic Route에 실제 ID 값을 넣어 이동 URL을 안전하게 만들기 위해 필요하다.

Q. Index Route는 뭐야?
A. 부모 Route 경로에 정확히 매칭될 때 기본으로 렌더링되는 자식 Route다.

Q. Index Route는 언제 써?
A. `/mypage`나 `/admin`처럼 부모 경로의 기본 화면이 필요할 때 사용한다.

Q. Index Route에 path를 써도 돼?
A. 아니다. index route는 path 없이 `index` 속성을 사용한다.

Q. Not Found Route는 뭐야?
A. 어떤 Route와도 매칭되지 않은 URL에 대해 404 화면을 보여주는 Route다.

Q. React Router에서 404 페이지는 어떻게 만들어?
A. `path="*"` Route를 추가하고 NotFoundPage를 렌더링한다.

Q. NotFound Route가 없으면 어떻게 돼?
A. 매칭되지 않는 URL에서 빈 화면처럼 보일 수 있다.

Q. SPA 404와 서버 404는 달라?
A. 다르다. SPA 404는 React Router 매칭 실패 화면이고 서버 404는 서버가 파일이나 경로를 찾지 못한 응답이다.

Q. React Router import는 react-router야 react-router-dom이야?
A. 프로젝트 버전에 따라 다르다. v6 프로젝트는 react-router-dom이 흔하고 v7 공식 문서는 react-router 예제를 제공할 수 있다. 프로젝트 기준으로 통일한다.

Q. Switch를 써야 해?
A. 아니다. React Router v6+에서는 Routes를 사용한다.

Q. useHistory를 써야 해?
A. 아니다. React Router v6+에서는 useNavigate를 사용한다.

Q. exact를 써야 해?
A. 아니다. React Router v6+의 Route 매칭 방식에서는 v5처럼 exact를 쓰지 않는다.

Q. URL은 바뀌는데 화면이 안 나와?
A. BrowserRouter, Route path, element, Link to, NotFound Route, Console Error를 순서대로 확인한다.

Q. React Router 문제는 어떻게 디버깅해?
A. URL, BrowserRouter, Routes / Route path, element, Link to, Route Constants, Console, Network, Server Fallback 순서로 확인한다.

Q. 새로고침 404는 React 코드 문제야?
A. 대부분 React 코드보다 배포 서버가 SPA 경로를 index.html로 fallback하지 않는 문제다.

Q. Part01 다음에는 뭘 다뤄?
A. Part02 Navigation에서 Link, NavLink, useNavigate, Navigate, useLocation, Navigation State를 다룬다.
