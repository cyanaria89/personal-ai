# React Router Domain Rules

---

# 1. Domain Purpose

## 1.1 Purpose

### [개념]

React Router Domain 문서는 Frontend Agent / Review Agent / PM Agent용 RAG 문서 제작 규칙이다.

목적:

- React SPA Routing 구조 이해
- Client Side Routing 구현 지원
- Route 정의 기준 제공
- Page Component와 Route 연결 지원
- Layout Route 구조 설계 지원
- Nested Route 구현 지원
- Dynamic Route Parameter 처리 지원
- Query String / Search Params 처리 지원
- Link / NavLink / Navigate 사용 기준 제공
- Protected Route 구현 기준 제공
- Not Found Route 처리 지원
- Backend 통합 배포 시 SPA Fallback 문제 검토 지원

---

### [핵심]

우선순위:

1. Client Side Routing
2. BrowserRouter
3. Routes / Route
4. Page Component
5. Link / NavLink
6. useNavigate
7. useParams
8. useSearchParams
9. Nested Route
10. Layout Route
11. Outlet
12. Protected Route
13. Not Found Route
14. SPA Fallback
15. React Router Version Awareness

---

### [실무]

2026 실무 기준에서 React Router 문서는 단순 URL 이동 문서가 아니다.

Frontend Agent가 아래 작업을 수행할 수 있도록 작성한다.

- SPA Route 구조 설계
- Page Component와 URL path 연결
- Layout Route 구성
- Nested Route 구성
- 동적 상세 페이지 구현
- 검색 조건을 Query String으로 관리
- 로그인 필요 페이지 보호
- 권한별 접근 제어
- 404 페이지 처리
- 새로고침 404 문제 원인 분석
- Spring Boot / Nginx / Static Hosting 배포 시 Fallback 검토
- React Router v6 / v7 스타일 차이 인지

---

### [FAQ]

Q. React Router 문서는 React Core와 뭐가 달라?

A.
React Core는 Component, Props, State, Hook 기본이고 React Router는 URL과 Page Component를 연결하는 Routing 구조에 집중한다.

Q. React Router에서 가장 중요한 기준은 뭐야?

A.
Route 구조, Page Component 연결, Link 이동, useNavigate 이동, useParams, useSearchParams, Nested Route, Protected Route다.

Q. React Router는 Backend Router랑 같은 거야?

A.
아니다. React Router는 브라우저 안에서 화면 Component를 바꾸는 Client Side Router이고 Backend Router는 서버 요청 URL을 처리한다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

React Router 문서는 React SPA Routing 구현에 필요한 범위를 포함한다.

포함 범위:

- SPA Routing
- Client Side Routing
- BrowserRouter
- Routes
- Route
- Link
- NavLink
- Navigate
- useNavigate
- useParams
- useSearchParams
- useLocation
- Outlet
- Layout Route
- Nested Route
- Index Route
- Dynamic Route
- Path Parameter
- Query String
- Search Params
- Not Found Route
- Protected Route
- Role Based Route
- Auth Redirect
- Route Config
- Route Constants
- Navigation State
- Scroll Restoration Basics
- Lazy Route Basics
- React Router v6 / v7 Awareness
- Data Router Basics Mention
- Framework Mode Basics Mention
- SPA Fallback Deployment
- Spring Boot Static Hosting Fallback
- Browser Refresh 404 Troubleshooting

---

### [핵심]

반드시 포함:

- React Router는 URL에 따라 React Component를 렌더링
- BrowserRouter는 브라우저 History API 기반 라우팅
- Routes / Route는 URL path와 element 연결
- Link / NavLink는 사용자 클릭 이동에 사용
- useNavigate는 코드 기반 이동에 사용
- useParams는 path parameter 읽기
- useSearchParams는 query string 읽기 / 수정
- Outlet은 Nested Route 자식 위치 표시
- Protected Route는 인증 상태에 따라 접근 제어
- SPA 새로고침 404는 서버 fallback 설정 문제일 수 있음

---

### [실무]

React Router는 React Component Design 이후 Page 연결 단계에서 사용한다.

실무 연결:

```text
React Core
→ React Component Design
→ React Router
→ Authentication Frontend Flow
→ State Management
→ Data Fetching & REST API Integration
→ Deployment / SPA Fallback
```

---

### [FAQ]

Q. React Router에서 Data Router도 포함해?

A.
기초 개념은 언급 가능하지만 이 Foundation 문서는 Declarative Routing과 일반 SPA Routing을 우선한다.

Q. React Router Framework Mode도 여기서 깊게 다뤄?

A.
아니다. Framework Mode, loader, action 심화는 Data Fetching 또는 Advanced React Router 문서에서 다룬다.

Q. React Router와 Next.js Routing을 같이 다뤄?

A.
아니다. Next.js App Router는 별도 Expert 문서에서 다룬다.

---

## 2.2 Excluded Scope

### [개념]

React Router 문서에서는 고급 Router Framework 기능과 SSR 심화를 제외한다.

제외 범위:

- React Router Framework Mode 심화
- Loader / Action 심화
- Server Rendering 심화
- Streaming / Hydration 심화
- Next.js App Router
- Remix 심화
- File-based Routing 심화
- Advanced Data Router
- Route Module 심화
- Router Adapter / Server Runtime 심화
- Micro Frontend Routing
- Complex Permission Matrix
- Full Auth Architecture
- SEO SSR 전략
- Performance Preloading 심화

---

### [핵심]

제외 이유:

- Foundation 범위 초과
- Data Fetching / Auth / Deployment / Advanced Router 문서와 분리 필요
- Agent Retrieval 혼선 방지
- Chunk 품질 유지
- SPA Router 기본 구현 능력에 집중

---

### [실무]

고급 기술은 별도 Domain Rules에서 관리한다.

예:

```text
React Router
→ Authentication Frontend Flow
→ Data Fetching & REST API Integration
→ Frontend Deployment
→ Advanced React Router / Next.js App Router
```

---

### [FAQ]

Q. Loader와 Action은 여기서 다뤄?

A.
기초 언급은 가능하지만 심화 사용 기준은 Data Router 또는 Data Fetching 문서에서 다룬다.

Q. SSR Routing은 여기서 다뤄?

A.
아니다. SSR / SSG / ISR은 Next.js 또는 Frontend Expert 문서에서 다룬다.

Q. 복잡한 권한 매트릭스도 여기서 다뤄?

A.
아니다. 기본 Protected Route와 Role Route만 다루고 복잡한 인증/인가 설계는 Authentication Frontend Flow 문서에서 다룬다.

---

# 3. Section Priority

## 3.1 Required Sections

### [개념]

React Router RAG 문서는 모든 주요 Chunk에 아래 Section을 우선 포함한다.

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
- [실무]: 실제 Router 적용 기준
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

Q. 모든 React Router 문서에 FAQ가 필요해?

A.
필요하다. FAQ는 사용자 질문과 RAG 검색 매칭을 강화한다.

Q. [면접] 섹션을 써도 돼?

A.
안 된다. 반드시 [FAQ] 섹션을 사용한다.

---

## 3.2 Recommended Sections

### [개념]

React Router 문서에는 라우팅 설계와 오류 검증을 위해 추가 Section을 포함할 수 있다.

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

- Route 구조 설명 → [Flow], [예제]
- Nested Route 설명 → [Flow], [예제]
- Protected Route 설명 → [Flow], [주의]
- Search Params 설명 → [예제], [Troubleshooting]
- SPA Fallback 설명 → [Troubleshooting]
- Link / useNavigate 차이 → [Comparison]

---

### [실무]

예시:

```md
### [Flow]

User Click Link
→ URL Change
→ React Router Match Route
→ Render Page Component
→ Nested Outlet Render
```

---

### [FAQ]

Q. React Router 문서에 Troubleshooting이 중요한 이유는?

A.
새로고침 404, params undefined, 중첩 라우트 미표시, 잘못된 redirect 같은 오류가 자주 발생하기 때문이다.

Q. Comparison은 언제 쓰면 좋아?

A.
Link vs useNavigate, path param vs query string, BrowserRouter vs HashRouter처럼 헷갈리는 개념을 비교할 때 사용한다.

---

# 4. React Router Overview Rules

## 4.1 SPA Routing

### [개념]

SPA Routing은 전체 페이지를 서버에서 다시 받지 않고 브라우저 안에서 URL에 맞는 React Component를 렌더링하는 방식이다.

React Router는 React SPA에서 URL과 Component를 연결한다.

기본 Flow:

```text
User Navigation
→ URL Change
→ Route Matching
→ Page Component Render
→ UI Update
```

---

### [핵심]

반드시 설명:

- SPA는 Single Page Application
- React Router는 Client Side Routing 담당
- URL path와 React Component를 연결
- Browser History API를 사용 가능
- 페이지 전체 reload 없이 화면 전환
- 서버는 SPA entry file을 제공해야 함
- 새로고침 시 서버 fallback 설정 필요 가능

---

### [실무]

React Router는 아래 상황에서 사용된다.

- `/` 메인 페이지
- `/login` 로그인 페이지
- `/signup` 회원가입 페이지
- `/festivals` 축제 목록 페이지
- `/festivals/:festivalId` 축제 상세 페이지
- `/mypage` 마이페이지
- `/admin` 관리자 페이지
- `*` 404 페이지

예상 Route 구조:

```text
/
├ /login
├ /signup
├ /festivals
│  └ /festivals/:festivalId
├ /mypage
└ *
```

---

### [FAQ]

Q. SPA Routing이 뭐야?

A.
페이지 전체를 다시 로드하지 않고 URL에 맞는 React Component를 브라우저 안에서 렌더링하는 방식이다.

Q. React Router는 서버 요청을 처리해?

A.
아니다. React Router는 브라우저에서 동작하는 Client Side Router다.

Q. React Router를 쓰면 새로고침해도 항상 되나?

A.
아니다. 배포 서버가 모든 SPA 경로를 index.html로 fallback하도록 설정해야 한다.

---

## 4.2 BrowserRouter Rules

### [개념]

BrowserRouter는 브라우저 History API를 사용해 URL을 관리하는 React Router 구성 요소다.

React 앱의 Router 최상위 Provider 역할을 한다.

---

### [핵심]

반드시 포함:

- BrowserRouter
- History API
- app root wrapping
- client side navigation
- clean URL
- server fallback requirement

예:

```jsx
import { BrowserRouter } from "react-router";

function Root() {
  return (
    <BrowserRouter>
      <App />
    </BrowserRouter>
  );
}
```

---

### [실무]

BrowserRouter는 보통 React entry point 또는 App 최상위에서 감싼다.

예:

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

주의:

- Router 관련 Hook은 Router 내부 Component에서만 사용
- BrowserRouter는 보통 앱 전체를 한 번만 감쌈
- 배포 서버 fallback이 없으면 직접 URL 접근 / 새로고침 404 발생 가능
- React Router v6 프로젝트는 `react-router-dom` import를 사용할 수 있음
- React Router v7 문서는 `react-router` import 예제를 제공할 수 있음

---

### [FAQ]

Q. BrowserRouter는 어디에 둬?

A.
보통 main.jsx, main.tsx, index.jsx 같은 React entry point에서 App을 감싼다.

Q. BrowserRouter를 여러 번 감싸도 돼?

A.
일반적으로 앱 전체를 한 번만 감싼다. 중첩 Router는 혼란을 만들 수 있다.

Q. BrowserRouter를 쓰면 서버 설정이 필요해?

A.
배포 환경에서 직접 URL 접근과 새로고침을 지원하려면 SPA fallback 설정이 필요하다.

---

## 4.3 React Router Version Rules

### [개념]

React Router는 버전에 따라 import 경로, Router 구성 방식, Data Router / Framework 기능이 달라질 수 있다.

문서 작성 시 버전 기준을 명확히 한다.

---

### [핵심]

반드시 포함:

- React Router v6
- React Router v7
- Declarative Mode
- Data Router
- Framework Mode
- BrowserRouter / Routes / Route
- createBrowserRouter basics mention
- loader / action basics mention
- import path awareness

---

### [실무]

Foundation 문서 기준:

- 기본 SPA Routing은 BrowserRouter + Routes + Route 중심
- React Router v6 프로젝트는 `react-router-dom` import가 흔함
- React Router v7 공식 문서에서는 `react-router` import 예제가 사용될 수 있음
- 기존 v6 프로젝트 유지보수 가능성 고려
- Data Router / Framework Mode는 심화 문서로 분리
- 문서 예제는 프로젝트 기준 import path를 통일

예:

```jsx
import { BrowserRouter, Routes, Route } from "react-router";
```

또는 기존 프로젝트:

```jsx
import { BrowserRouter, Routes, Route } from "react-router-dom";
```

주의:

- 한 프로젝트에서 import 경로 혼용 금지
- 설치된 React Router 버전 확인
- 기존 코드 컨벤션 우선
- 공식 문서 기준과 프로젝트 버전 차이 확인

---

### [FAQ]

Q. React Router import는 react-router야 react-router-dom이야?

A.
프로젝트 버전에 따라 다를 수 있다. v6 프로젝트는 react-router-dom이 흔하고 v7 공식 문서는 react-router 예제를 제공할 수 있다. 프로젝트 기준으로 통일한다.

Q. React Router v6와 v7은 완전히 달라?

A.
기본 Declarative Routing 개념은 유사하지만 v7은 Framework 기능과 타입 지원이 강화되었다. 프로젝트 버전을 확인해야 한다.

Q. createBrowserRouter를 꼭 써야 해?

A.
아니다. 기본 SPA Routing은 BrowserRouter + Routes + Route로도 충분하다. Data Router 기능이 필요하면 createBrowserRouter를 검토한다.

---

# 5. Route Definition Rules

## 5.1 Routes and Route Rules

### [개념]

Routes와 Route는 URL path와 렌더링할 React Component를 연결한다.

기본 예:

```jsx
import { Routes, Route } from "react-router";

function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<MainPage />} />
      <Route path="/login" element={<LoginPage />} />
      <Route path="/festivals" element={<FestivalListPage />} />
      <Route path="/festivals/:festivalId" element={<FestivalDetailPage />} />
    </Routes>
  );
}
```

---

### [핵심]

반드시 설명:

- `Routes`는 여러 Route를 감싸는 매칭 영역
- `Route`는 path와 element를 연결
- `path`는 URL pattern
- `element`는 렌더링할 React Element
- 동적 경로는 `:paramName`
- `*`는 catch-all route로 사용 가능
- Route 순서 의존성은 v5와 다름

---

### [실무]

권장:

- Route 정의는 AppRoutes 같은 파일로 분리
- Page Component와 Route를 연결
- path 문자열은 constants로 관리 가능
- NotFoundPage route 포함
- 인증 필요 route는 Protected Route로 감쌈
- 중첩 구조는 Layout Route + Outlet 사용

예:

```jsx
<Route path="*" element={<NotFoundPage />} />
```

주의:

- element에 Component 함수가 아니라 JSX Element 전달
- 잘못된 path 앞뒤 slash 확인
- 중첩 route path 규칙 확인
- route path와 Link to 값 일치

---

### [FAQ]

Q. Route의 element에는 뭘 넣어?

A.
렌더링할 React Element를 넣는다. 예: `element={<LoginPage />}`.

Q. 404 페이지는 어떻게 만들어?

A.
`<Route path="*" element={<NotFoundPage />} />`처럼 catch-all route를 추가한다.

Q. Route path와 Link to가 다르면 어떻게 돼?

A.
사용자가 이동해도 원하는 Route가 매칭되지 않아 빈 화면이나 NotFoundPage가 나올 수 있다.

---

## 5.2 Route Constants Rules

### [개념]

Route Constants는 URL path 문자열을 상수로 관리하는 방식이다.

경로 오타와 중복을 줄이기 위해 사용한다.

---

### [핵심]

사용 대상:

- path constants
- route map
- navigation menu
- redirect path
- protected route redirect
- detail path builder

---

### [실무]

예:

```javascript
export const ROUTES = {
  HOME: "/",
  LOGIN: "/login",
  FESTIVALS: "/festivals",
  FESTIVAL_DETAIL: "/festivals/:festivalId",
};
```

상세 경로 생성:

```javascript
export function createFestivalDetailPath(festivalId) {
  return `/festivals/${festivalId}`;
}
```

사용:

```jsx
<Link to={createFestivalDetailPath(festival.festivalId)}>Detail</Link>
```

장점:

- path 오타 감소
- 경로 변경 시 수정 범위 감소
- Navigation과 Route 정의 정합성 유지
- Detail URL 생성 일관성 확보

---

### [FAQ]

Q. Route path를 상수로 꼭 관리해야 해?

A.
작은 프로젝트는 직접 문자열도 가능하지만 경로가 많아지면 상수 관리가 오타를 줄인다.

Q. 동적 path도 상수로 관리해?

A.
Route pattern은 상수로 두고 실제 이동 URL은 path builder 함수로 만드는 것이 좋다.

---

## 5.3 Index Route Rules

### [개념]

Index Route는 부모 Route 경로에 정확히 매칭될 때 기본으로 렌더링되는 자식 Route다.

---

### [핵심]

필수 포함:

- index route
- parent route
- default child
- nested route
- Outlet

예:

```jsx
<Route path="/mypage" element={<MyPageLayout />}>
  <Route index element={<MyPageHome />} />
  <Route path="profile" element={<ProfilePage />} />
</Route>
```

---

### [실무]

사용 상황:

- `/mypage` 기본 화면
- `/admin` 기본 dashboard
- `/festivals` 기본 목록
- layout 안의 기본 content

주의:

- index route에는 path를 쓰지 않음
- 부모 Component에 Outlet 필요
- index와 path child route 구분

---

### [FAQ]

Q. Index Route는 언제 써?

A.
부모 경로에 들어왔을 때 기본으로 보여줄 자식 화면이 필요할 때 사용한다.

Q. Index Route에 path를 써도 돼?

A.
아니다. index route는 path 없이 `index` 속성을 사용한다.

---

# 6. Navigation Rules

## 6.1 Link Rules

### [개념]

Link는 React Router에서 페이지 reload 없이 다른 Route로 이동하기 위한 Component다.

예:

```jsx
import { Link } from "react-router";

function Header() {
  return <Link to="/festivals">Festivals</Link>;
}
```

---

### [핵심]

반드시 설명:

- Link는 client side navigation
- `to`는 이동할 path
- a 태그 대신 사용
- 페이지 reload 방지
- 접근성 / 브라우저 기본 동작 유지
- 내부 Route 이동에 적합

---

### [실무]

권장:

```jsx
<Link to={`/festivals/${festival.festivalId}`}>{festival.title}</Link>
```

내부 이동:

- Link 사용
- NavLink 사용
- useNavigate 사용

외부 이동:

```jsx
<a href="https://example.com" target="_blank" rel="noreferrer">
  External Site
</a>
```

주의:

- 내부 라우트 이동에 일반 a href를 쓰면 전체 reload 발생 가능
- 외부 링크는 a 태그 사용
- button 클릭으로 단순 페이지 이동을 남용하지 않음

---

### [FAQ]

Q. React Router에서 a 태그 대신 Link를 쓰는 이유는?

A.
내부 Route 이동 시 페이지 전체 reload 없이 React Router가 URL과 화면을 갱신하기 위해서다.

Q. 외부 사이트 이동도 Link를 써?

A.
아니다. 외부 URL 이동은 일반 a 태그를 사용한다.

Q. Link의 to에는 뭘 넣어?

A.
이동할 내부 Route path를 넣는다. 예: `/login`, `/festivals/1`.

---

## 6.2 NavLink Rules

### [개념]

NavLink는 현재 URL과 일치하는 링크에 active 상태를 적용할 수 있는 Link다.

Navigation Menu에 적합하다.

---

### [핵심]

필수 포함:

- NavLink
- active state
- className callback
- navigation menu
- aria-current
- current route indication

예:

```jsx
<NavLink
  to="/festivals"
  className={({ isActive }) => (isActive ? "active" : "")}
>
  Festivals
</NavLink>
```

---

### [실무]

사용 상황:

- Header Navigation
- Sidebar Menu
- Tab-like Route Menu
- MyPage Menu
- Admin Menu

권장:

- 현재 페이지 표시
- active class 제공
- 접근성 고려
- 메뉴 route path와 실제 Route 정합성 유지

---

### [FAQ]

Q. Link와 NavLink 차이는?

A.
Link는 단순 이동이고 NavLink는 현재 URL과 일치할 때 active 상태를 알 수 있다.

Q. NavLink는 언제 써?

A.
Header, Sidebar, Tab Menu처럼 현재 선택된 메뉴 표시가 필요할 때 사용한다.

---

## 6.3 useNavigate Rules

### [개념]

useNavigate는 코드에서 명령형으로 Route 이동을 수행하는 Hook이다.

예:

```jsx
import { useNavigate } from "react-router";

function LoginPage() {
  const navigate = useNavigate();

  function handleLoginSuccess() {
    navigate("/");
  }

  return null;
}
```

---

### [핵심]

반드시 설명:

- programmatic navigation
- event after navigation
- auth redirect
- form submit success
- replace option
- history back / forward
- Router 내부에서만 사용 가능

---

### [실무]

사용 상황:

- 로그인 성공 후 메인 이동
- 회원가입 성공 후 로그인 이동
- 저장 성공 후 상세 페이지 이동
- 삭제 성공 후 목록 이동
- 권한 없음 redirect
- 뒤로가기 처리

예:

```jsx
navigate("/login", { replace: true });
```

뒤로가기:

```jsx
navigate(-1);
```

주의:

- 일반 클릭 링크 이동은 Link / NavLink 우선
- useNavigate는 Event Handler나 Effect 안에서 사용
- 렌더링 중 navigate 호출 금지
- 인증 redirect는 replace 옵션 고려

---

### [FAQ]

Q. Link와 useNavigate 중 뭐를 써?

A.
사용자가 클릭해서 이동하는 일반 링크는 Link를 우선하고, 로그인 성공 후 이동처럼 코드 흐름에 따른 이동은 useNavigate를 사용한다.

Q. navigate replace는 언제 써?

A.
로그인 페이지 redirect처럼 사용자가 뒤로가기로 다시 돌아오면 안 되는 경우에 사용한다.

Q. useNavigate를 Router 밖에서 쓸 수 있어?

A.
안 된다. Router 내부 Component에서만 사용할 수 있다.

---

## 6.4 Navigate Component Rules

### [개념]

Navigate Component는 렌더링 결과로 redirect를 수행하는 React Router Component다.

조건부 접근 제어에서 사용할 수 있다.

---

### [핵심]

필수 포함:

- Navigate
- redirect
- replace
- conditional render
- protected route
- auth guard

예:

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

사용 상황:

- 로그인 안 된 사용자 redirect
- 이미 로그인한 사용자의 login 페이지 접근 제한
- 권한 없는 관리자 페이지 redirect
- 조건부 route guard

주의:

- 무한 redirect 구조 주의
- 로그인 상태 로딩 중에는 redirect 보류
- 이전 위치 저장이 필요한 경우 location state 활용
- replace 옵션으로 history 정리 가능

---

### [FAQ]

Q. Navigate와 useNavigate 차이는?

A.
Navigate는 렌더링 결과로 redirect하고 useNavigate는 함수 호출로 이동한다.

Q. Protected Route에는 Navigate를 써도 돼?

A.
가능하다. 인증 상태에 따라 login 페이지로 redirect할 때 자주 사용한다.

---

# 7. Route Parameter Rules

## 7.1 Dynamic Route and useParams

### [개념]

Dynamic Route는 URL 일부를 변수처럼 받는 Route다.

useParams는 현재 Route의 path parameter를 읽는 Hook이다.

예:

```jsx
<Route path="/festivals/:festivalId" element={<FestivalDetailPage />} />
```

```jsx
import { useParams } from "react-router";

function FestivalDetailPage() {
  const { festivalId } = useParams();

  return <p>{festivalId}</p>;
}
```

---

### [핵심]

반드시 설명:

- Dynamic Route
- Path Parameter
- `:paramName`
- useParams
- string value
- undefined 가능성
- type conversion
- detail page

---

### [실무]

상세 페이지 예:

```jsx
function FestivalDetailPage() {
  const { festivalId } = useParams();

  if (!festivalId) {
    return <p>Invalid festival id.</p>;
  }

  return <FestivalDetail festivalId={Number(festivalId)} />;
}
```

주의:

- useParams 값은 문자열
- 숫자 ID가 필요하면 Number 변환
- param이 없을 수 있으므로 방어
- Route path와 Link URL 정합성 확인
- param 이름 통일

---

### [FAQ]

Q. useParams 값은 number야 string이야?

A.
문자열이다. 숫자 ID로 쓰려면 Number로 변환해야 한다.

Q. useParams가 undefined인 이유는?

A.
Route path에 해당 param이 없거나 param 이름이 맞지 않을 수 있다.

Q. 상세 페이지 path는 어떻게 잡아?

A.
일반적으로 `/resources/:resourceId` 형태를 사용한다. 예: `/festivals/:festivalId`.

---

## 7.2 Query String and useSearchParams

### [개념]

Query String은 URL에서 `?key=value` 형태로 검색 조건이나 필터 상태를 표현하는 방식이다.

useSearchParams는 Query String을 읽고 수정하는 Hook이다.

예:

```text
/festivals?keyword=spring&region=seoul
```

---

### [핵심]

필수 포함:

- query string
- search params
- useSearchParams
- URLSearchParams
- get
- set
- delete
- filter state
- pagination state
- bookmarkable URL

---

### [실무]

읽기 예:

```jsx
import { useSearchParams } from "react-router";

function FestivalSearchPage() {
  const [searchParams, setSearchParams] = useSearchParams();

  const keyword = searchParams.get("keyword") ?? "";
  const page = Number(searchParams.get("page") ?? "1");

  return null;
}
```

수정 예:

```jsx
setSearchParams({
  keyword: "spring",
  page: "1",
});
```

사용 상황:

- 검색어
- 필터 조건
- 정렬 조건
- 페이지 번호
- 탭 상태
- 목록 화면 상태 공유

주의:

- search param 값은 문자열
- 숫자 / boolean 변환 필요
- 빈 값은 제거 여부 결정
- URL 상태와 Component State 중복 주의
- Query String은 공유 가능한 상태에 적합

---

### [FAQ]

Q. 검색 조건은 State로 둬야 해 Query String으로 둬야 해?

A.
URL 공유, 새로고침 유지, 뒤로가기 복원이 필요하면 Query String으로 관리하는 것이 좋다.

Q. useSearchParams 값은 number로 바로 받아?

A.
아니다. 문자열로 읽히므로 Number 변환이 필요하다.

Q. setSearchParams를 호출하면 페이지 이동이야?

A.
URL search params가 바뀌므로 navigation이 발생한다.

---

## 7.3 Path Param vs Query String Rules

### [개념]

Path Parameter는 특정 리소스를 식별하는 URL 일부다.

Query String은 검색, 필터, 정렬, 페이지 같은 옵션을 표현한다.

---

### [핵심]

비교:

| 비교   | Path Parameter     | Query String                |
| ------ | ------------------ | --------------------------- |
| 형태   | `/festivals/1`     | `/festivals?keyword=spring` |
| 목적   | 리소스 식별        | 조건 / 옵션                 |
| 예     | festivalId, userId | keyword, page, sort         |
| 필수성 | 대체로 필수        | 선택적                      |
| Hook   | useParams          | useSearchParams             |

---

### [실무]

권장 기준:

```text
Resource Identity → Path Parameter
Filter / Search / Sort / Page → Query String
```

예:

- 축제 상세: `/festivals/123`
- 축제 검색: `/festivals?keyword=꽃&region=seoul`
- 리뷰 목록: `/festivals/123/reviews?page=2`

주의:

- 검색 조건을 path segment로 과도하게 만들지 않음
- 상세 ID를 query string으로 숨기지 않음
- URL 의미가 REST API와 비슷하게 읽히도록 설계

---

### [FAQ]

Q. ID는 path param이 좋아 query string이 좋아?

A.
특정 리소스 식별 ID는 path parameter가 일반적으로 적합하다.

Q. 검색어는 path param으로 넣어도 돼?

A.
가능은 하지만 필터와 검색 조건은 Query String이 더 적합한 경우가 많다.

---

# 8. Nested Route and Layout Rules

## 8.1 Nested Route Rules

### [개념]

Nested Route는 부모 Route 안에 자식 Route를 구성하는 방식이다.

공통 Layout과 하위 화면을 함께 구성할 때 사용한다.

---

### [핵심]

필수 포함:

- nested route
- parent route
- child route
- Outlet
- relative path
- index route
- layout route

예:

```jsx
<Route path="/mypage" element={<MyPageLayout />}>
  <Route index element={<MyPageHome />} />
  <Route path="profile" element={<ProfilePage />} />
  <Route path="favorites" element={<FavoritePage />} />
</Route>
```

---

### [실무]

사용 상황:

- MyPage 내부 메뉴
- Admin dashboard
- Festival Detail 하위 탭
- 공통 Header / Sidebar Layout
- Settings page
- Nested tab route

주의:

- 부모 element에 Outlet 필요
- 자식 path에는 보통 앞 slash 생략
- index route와 child path 구분
- 중첩 깊이가 과도하면 구조 복잡
- Layout Component 책임 명확화

---

### [FAQ]

Q. Nested Route 화면이 안 나와?

A.
부모 Component에 `<Outlet />`이 없을 가능성이 크다.

Q. 자식 Route path에 slash를 붙여야 해?

A.
상대 경로로 쓰려면 보통 slash 없이 작성한다. 절대 경로가 필요한 경우 의도를 명확히 해야 한다.

Q. Nested Route는 언제 써?

A.
공통 Layout 안에서 하위 화면이 바뀌는 구조가 필요할 때 사용한다.

---

## 8.2 Outlet Rules

### [개념]

Outlet은 Nested Route의 자식 Component가 렌더링될 위치를 표시하는 React Router Component다.

---

### [핵심]

반드시 설명:

- Outlet
- child route render position
- layout component
- nested UI
- route hierarchy
- parent route

예:

```jsx
import { Outlet } from "react-router";

function MyPageLayout() {
  return (
    <main>
      <MyPageSidebar />
      <section>
        <Outlet />
      </section>
    </main>
  );
}
```

---

### [실무]

Outlet 사용 상황:

- Sidebar + Content 구조
- Header + Main Content 구조
- Admin Layout
- MyPage Layout
- Detail Page Tab Layout

주의:

- Outlet이 없으면 자식 Route가 렌더링되지 않음
- Layout Component는 공통 구조만 담당
- Outlet 위치가 실제 자식 화면 위치
- 접근성 landmark 구조 고려

---

### [FAQ]

Q. Outlet은 왜 필요해?

A.
부모 Route Component 안에서 자식 Route Component가 표시될 위치를 지정하기 위해 필요하다.

Q. Outlet을 여러 개 둘 수 있어?

A.
일반적인 Nested Route에서는 하나의 Outlet로 자식 Route 렌더링 위치를 지정한다. 여러 영역이 필요하면 Layout 구조를 다시 설계한다.

---

## 8.3 Layout Route Rules

### [개념]

Layout Route는 공통 UI 구조를 제공하고 자식 Route를 Outlet에 렌더링하는 Route다.

---

### [핵심]

사용 대상:

- Public Layout
- Auth Layout
- Main Layout
- Admin Layout
- MyPage Layout
- Header / Footer
- Sidebar
- Outlet

---

### [실무]

예:

```jsx
<Route element={<MainLayout />}>
  <Route path="/" element={<MainPage />} />
  <Route path="/festivals" element={<FestivalListPage />} />
  <Route path="/festivals/:festivalId" element={<FestivalDetailPage />} />
</Route>
```

Layout Component:

```jsx
function MainLayout() {
  return (
    <>
      <Header />
      <main>
        <Outlet />
      </main>
      <Footer />
    </>
  );
}
```

권장:

- Layout은 공통 구조 담당
- Page별 데이터 로직은 Page Component 또는 Hook으로 분리
- Auth Layout / Admin Layout 분리 가능
- Header / Footer 중복 제거

---

### [FAQ]

Q. Layout Route는 왜 써?

A.
여러 페이지에서 공통 Header, Footer, Sidebar 구조를 중복 작성하지 않기 위해 사용한다.

Q. Layout Route에 path가 없어도 돼?

A.
가능하다. path 없는 Layout Route는 자식 Route를 공통 Layout으로 감싸는 데 사용할 수 있다.

---

# 9. Protected Route Rules

## 9.1 Protected Route Basics

### [개념]

Protected Route는 인증되지 않은 사용자나 권한이 없는 사용자의 Route 접근을 제한하는 구조다.

---

### [핵심]

필수 포함:

- authenticated
- authorization
- protected route
- private route
- auth guard
- Navigate
- redirect
- replace
- loading auth state
- role based route

---

### [실무]

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

Route 적용:

```jsx
<Route
  path="/mypage"
  element={
    <ProtectedRoute authenticated={authenticated}>
      <MyPage />
    </ProtectedRoute>
  }
/>
```

주의:

- 인증 상태 로딩 중에는 redirect하지 않음
- 로그인 후 돌아갈 위치 저장 고려
- replace 사용으로 history 정리 가능
- Frontend Route 보호는 UX용이며 Backend 인증/인가 필수
- JWT 존재만으로 권한을 완전히 신뢰하지 않음

---

### [FAQ]

Q. Protected Route는 보안적으로 충분해?

A.
아니다. Frontend Route 보호는 UX용이다. 실제 보안은 Backend 인증/인가가 반드시 필요하다.

Q. 인증 상태 확인 전 바로 login으로 보내도 돼?

A.
권장하지 않는다. 인증 상태 loading 중에는 임시 로딩 UI를 보여주고 확인 후 redirect해야 한다.

Q. 로그인 후 원래 페이지로 돌아가려면?

A.
location state나 query string에 redirect target을 저장해 로그인 성공 후 이동할 수 있다.

---

## 9.2 Role Based Route Rules

### [개념]

Role Based Route는 사용자 권한에 따라 접근 가능한 Route를 제한하는 구조다.

예:

- ROLE_USER
- ROLE_ADMIN

---

### [핵심]

필수 포함:

- user role
- allowed roles
- admin route
- authorization guard
- forbidden page
- redirect
- backend validation

---

### [실무]

예:

```jsx
function RoleRoute({ role, allowedRoles, children }) {
  if (!allowedRoles.includes(role)) {
    return <Navigate to="/forbidden" replace />;
  }

  return children;
}
```

Route 적용:

```jsx
<Route
  path="/admin"
  element={
    <RoleRoute role={user.role} allowedRoles={["ROLE_ADMIN"]}>
      <AdminPage />
    </RoleRoute>
  }
/>
```

주의:

- role 값 naming 통일
- ROLE_ADMIN / ADMIN 혼용 금지
- Frontend role check는 UX용
- Backend API 권한 검증 필수
- 권한 없음 페이지 또는 main redirect 기준 명확화

---

### [FAQ]

Q. Frontend에서 ROLE_ADMIN 체크하면 보안이 되는 거야?

A.
아니다. Frontend 권한 체크는 화면 접근 UX용이고 실제 API 보안은 Backend에서 검증해야 한다.

Q. 권한 없는 사용자는 어디로 보내?

A.
프로젝트 기준에 따라 `/forbidden`, `/login`, `/` 중 하나로 보낼 수 있다. 기준을 통일해야 한다.

---

## 9.3 Auth Redirect Rules

### [개념]

Auth Redirect는 로그인 상태에 따라 사용자를 적절한 Route로 이동시키는 흐름이다.

---

### [핵심]

사용 상황:

- 비로그인 사용자의 보호 페이지 접근
- 로그인 성공 후 원래 페이지 이동
- 로그인 사용자의 login page 접근 제한
- logout 후 main page 이동
- token 만료 후 login 이동

---

### [실무]

Redirect Flow:

```text
Protected Page Access
→ Check Auth Loading
→ If Not Authenticated
→ Save Current Location
→ Redirect Login
→ Login Success
→ Navigate Previous Location
```

예:

```jsx
<Navigate to="/login" replace state={{ from: location.pathname }} />
```

주의:

- redirect loop 방지
- login page에서 다시 login으로 redirect 금지
- token refresh 중 loading 처리
- 인증 실패와 권한 부족 구분
- redirect target validation 고려

---

### [FAQ]

Q. 로그인 페이지에서 이미 로그인된 사용자는 어떻게 해?

A.
메인 페이지나 이전 페이지로 redirect하는 기준을 둘 수 있다.

Q. redirect loop는 왜 생겨?

A.
인증 상태 판단 조건이 잘못되어 login과 protected page 사이를 계속 오갈 때 발생한다.

---

# 10. Route State and Location Rules

## 10.1 useLocation Rules

### [개념]

useLocation은 현재 URL location 정보를 읽는 Hook이다.

현재 path, search, hash, state를 확인할 수 있다.

---

### [핵심]

필수 포함:

- pathname
- search
- hash
- state
- navigation state
- previous location
- auth redirect
- current route check

예:

```jsx
import { useLocation } from "react-router";

function CurrentPath() {
  const location = useLocation();

  return <p>{location.pathname}</p>;
}
```

---

### [실무]

사용 상황:

- 현재 path 확인
- 로그인 redirect 이전 위치 저장
- 조건부 Layout
- route 변경 감지
- analytics tracking basics
- scroll 처리 basics

주의:

- location.state는 새로고침 시 사라질 수 있음
- 영구 유지가 필요한 값은 query string 또는 storage 고려
- path 비교 문자열 오타 주의
- 복잡한 active 판단은 NavLink 우선

---

### [FAQ]

Q. useLocation은 언제 써?

A.
현재 URL path, search, state 정보가 필요할 때 사용한다.

Q. location.state는 새로고침해도 남아?

A.
보장되지 않는다. 영구적으로 유지해야 하는 정보는 query string이나 storage를 고려한다.

---

## 10.2 Navigation State Rules

### [개념]

Navigation State는 navigate 또는 Link 이동 시 URL에 보이지 않는 임시 데이터를 함께 전달하는 방식이다.

---

### [핵심]

필수 포함:

- state option
- Link state
- navigate state
- temporary data
- previous location
- refresh caution

---

### [실무]

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

주의:

- URL에 보이지 않음
- 새로고침 / 직접 접근 시 state 없음
- 중요한 데이터 저장 용도 아님
- redirect target 정도에 적합
- 민감정보 전달 금지

---

### [FAQ]

Q. Navigation State는 언제 써?

A.
로그인 후 돌아갈 경로처럼 임시 이동 정보를 전달할 때 사용한다.

Q. Navigation State에 중요한 데이터를 넣어도 돼?

A.
권장하지 않는다. 새로고침이나 직접 접근 시 사라질 수 있고 URL 공유에도 포함되지 않는다.

---

# 11. Not Found and Error Route Rules

## 11.1 Not Found Route Rules

### [개념]

Not Found Route는 어떤 Route와도 매칭되지 않은 URL에 대해 보여주는 404 화면이다.

---

### [핵심]

필수 포함:

- catch-all route
- path="\*"
- NotFoundPage
- invalid URL
- navigation back
- home link

예:

```jsx
<Route path="*" element={<NotFoundPage />} />
```

---

### [실무]

NotFoundPage 기준:

- 잘못된 주소 안내
- 메인 이동 Link 제공
- 이전 페이지 이동 버튼 제공 가능
- 서비스 톤에 맞는 문구
- Layout 포함 여부 결정
- SEO / status code는 SPA 한계 고려

예:

```jsx
function NotFoundPage() {
  return (
    <main>
      <h1>페이지를 찾을 수 없습니다.</h1>
      <Link to="/">메인으로 이동</Link>
    </main>
  );
}
```

주의:

- catch-all route 누락 시 빈 화면 가능
- 중첩 route에서 local 404와 global 404 구분 가능
- 서버 404와 SPA 404 차이 이해

---

### [FAQ]

Q. React Router에서 404 페이지는 어떻게 만들어?

A.
`path="*"` Route를 추가하고 NotFoundPage를 렌더링한다.

Q. SPA 404와 서버 404는 달라?

A.
다르다. SPA 404는 React Router가 매칭 실패를 처리하는 화면이고 서버 404는 서버가 파일이나 경로를 찾지 못한 응답이다.

---

## 11.2 Route Error Handling Basics

### [개념]

Route Error Handling은 Route 매칭, 데이터 로딩, 권한 확인, 잘못된 parameter 등에서 발생하는 오류를 화면으로 처리하는 기준이다.

---

### [핵심]

처리 대상:

- invalid path
- invalid param
- missing resource
- forbidden
- unauthenticated
- network error
- route element error basics

---

### [실무]

상세 페이지 ID 오류 예:

```jsx
function FestivalDetailPage() {
  const { festivalId } = useParams();
  const parsedFestivalId = Number(festivalId);

  if (!festivalId || Number.isNaN(parsedFestivalId)) {
    return <NotFoundPage />;
  }

  return <FestivalDetail festivalId={parsedFestivalId} />;
}
```

권장:

- invalid param은 NotFound 또는 Error UI
- API 404는 resource not found UI
- 401은 login redirect
- 403은 forbidden page
- 500은 error message
- 사용자 메시지와 개발자 로그 구분

---

### [FAQ]

Q. 잘못된 URL parameter는 어떻게 처리해?

A.
Number 변환 실패나 필수 param 누락을 확인하고 NotFoundPage나 Error UI를 보여준다.

Q. API 404와 Route 404는 어떻게 달라?

A.
Route 404는 URL이 Route와 매칭되지 않는 경우이고 API 404는 서버 리소스를 찾지 못한 경우다.

---

# 12. Data Router Awareness Rules

## 12.1 Data Router Basics Mention

### [개념]

Data Router는 Route 단위에서 데이터 로딩, 제출, 에러 처리를 더 구조적으로 다룰 수 있는 React Router 방식이다.

Foundation 문서에서는 개념만 언급하고 심화는 별도 문서로 분리한다.

---

### [핵심]

키워드:

- createBrowserRouter
- RouterProvider
- loader
- action
- errorElement
- route object
- data loading
- form submission
- framework feature

---

### [실무]

기초 예:

```jsx
import { createBrowserRouter, RouterProvider } from "react-router";

const router = createBrowserRouter([
  {
    path: "/",
    element: <MainPage />,
  },
]);

function App() {
  return <RouterProvider router={router} />;
}
```

주의:

- BrowserRouter 방식과 RouterProvider 방식을 혼용하지 않음
- Data Router 도입 시 loader / action 설계 필요
- 기존 SPA useEffect fetch 구조와 역할 구분
- 프로젝트 요구사항에 따라 선택
- Foundation 단계에서는 Declarative Routing 우선

---

### [FAQ]

Q. BrowserRouter와 RouterProvider를 같이 써?

A.
일반적으로 같이 쓰지 않는다. BrowserRouter 방식과 createBrowserRouter / RouterProvider 방식 중 하나를 선택한다.

Q. loader와 action은 뭐야?

A.
Route 단위 데이터 로딩과 제출 처리를 담당하는 Data Router 기능이다. Foundation 문서에서는 개념만 다룬다.

---

# 13. SPA Fallback and Deployment Rules

## 13.1 SPA Refresh 404 Rules

### [개념]

SPA Refresh 404는 React Router 경로에서 새로고침하거나 직접 URL로 접근했을 때 서버가 해당 경로 파일을 찾지 못해 404를 반환하는 문제다.

---

### [핵심]

문제:

- `/festivals/1` 직접 접근 시 404
- 새로고침 시 Not Found
- 배포 후 Route 이동은 되는데 refresh 실패
- Spring Boot 통합 배포에서 index.html fallback 누락
- Nginx try_files 설정 누락

원인:

- React Router는 client side route
- 서버는 `/festivals/1` 파일을 찾음
- 서버 fallback이 index.html로 연결되지 않음
- API path와 SPA path 충돌
- 정적 리소스 경로 설정 문제

---

### [실무]

해결 원칙:

```text
Browser Request /festivals/1
→ Server checks static file
→ If not API and not static resource
→ Return index.html
→ React Router matches /festivals/1
→ Render Detail Page
```

Spring Boot Fallback 예:

```java
@Controller
public class SpaForwardController {
  @GetMapping(value = {
      "/",
      "/login",
      "/signup",
      "/festivals",
      "/festivals/{id}",
      "/mypage/**"
  })
  public String forward() {
    return "forward:/index.html";
  }
}
```

주의:

- `/api/**` 같은 Backend API 경로는 forward하면 안 됨
- 정적 파일 경로도 forward 대상에서 제외
- Backend Controller 경로와 Frontend Route 충돌 주의
- 배포 환경별 fallback 방식 다름
- BrowserRouter 사용 시 필요
- HashRouter는 fallback 문제를 줄일 수 있지만 URL 품질이 낮아질 수 있음

---

### [FAQ]

Q. React Router는 로컬에서 되는데 배포 후 새로고침하면 404가 나?

A.
서버가 SPA 경로를 index.html로 fallback하지 않아서 발생하는 경우가 많다.

Q. Spring Boot에 React build를 넣으면 새로고침 404는 어떻게 해결해?

A.
API와 정적 리소스를 제외한 Frontend Route를 `forward:/index.html`로 보내는 fallback Controller를 구성한다.

Q. 모든 요청을 index.html로 보내도 돼?

A.
안 된다. `/api/**`, 정적 리소스, 실제 Backend Controller 경로는 제외해야 한다.

---

## 13.2 API Path Collision Rules

### [개념]

API Path Collision은 Frontend Route path와 Backend API path가 겹쳐서 요청이 잘못 처리되는 문제다.

---

### [핵심]

문제:

- React Route로 이동하려는데 Backend API Controller가 잡음
- API 요청이 index.html을 반환함
- JSON을 기대했는데 HTML 응답
- 새로고침 시 잘못된 Controller 매칭
- 404 또는 MIME type 오류

원인:

- Frontend Route와 Backend API path prefix 혼용
- fallback Controller 범위 과다
- `/festival`과 `/festivals` 경로 혼동
- public API / auth API 경로 구분 부족

해결:

- Backend API는 `/api` prefix 권장
- Frontend Route와 API Route 분리
- fallback 대상에서 API 제외
- Axios baseURL과 Route path 구분
- Network response content-type 확인

---

### [실무]

권장 구조:

```text
Frontend Route
/festivals
/festivals/1
/calendar
/mypage

Backend API
/api/festivals
/api/festivals/1
/api/calendar/monthly
/api/users/me
```

주의:

- Route path와 API endpoint를 같은 이름으로 써도 prefix로 구분
- Axios 요청 URL과 React Router path 혼동 금지
- fallback이 API를 가로채면 JSON 대신 HTML 반환 가능

---

### [FAQ]

Q. API 요청했는데 index.html이 응답돼?

A.
SPA fallback Controller가 API 요청까지 forward하고 있을 가능성이 있다. API path를 fallback에서 제외해야 한다.

Q. Frontend Route와 Backend API 경로는 어떻게 구분해?

A.
Backend API는 `/api` prefix를 두고 Frontend Route는 화면 URL로 분리하는 것이 안전하다.

---

# 14. Route Structure and File Rules

## 14.1 Route File Structure

### [개념]

Route File Structure는 Route 정의, Page Component, Layout Component, route constants를 역할별로 배치하는 구조다.

---

### [핵심]

포함 대상:

- routes
- pages
- layouts
- components
- route constants
- protected route
- not found page
- feature route grouping

---

### [실무]

기본 구조:

```text
src
├ routes
│  ├ AppRoutes.jsx
│  ├ ProtectedRoute.jsx
│  └ routePaths.js
├ layouts
│  ├ MainLayout.jsx
│  └ AuthLayout.jsx
├ pages
│  ├ MainPage.jsx
│  ├ LoginPage.jsx
│  ├ FestivalListPage.jsx
│  ├ FestivalDetailPage.jsx
│  └ NotFoundPage.jsx
└ components
```

권장:

- Route 정의는 AppRoutes로 분리
- Route path 상수 분리 가능
- Page Component는 pages 폴더
- Layout Component는 layouts 폴더
- ProtectedRoute는 routes 또는 auth feature에 배치
- 프로젝트 규모에 따라 단순화

주의:

- 작은 프로젝트에 과도한 구조 금지
- Route 정의와 Navigation path 정합성 유지
- pages와 components 역할 구분
- auth 관련 route guard 위치 통일

---

### [FAQ]

Q. Route 정의 파일은 어디에 두는 게 좋아?

A.
보통 routes 폴더에 AppRoutes.jsx 또는 AppRoutes.tsx로 분리한다.

Q. Page Component는 어디에 둬?

A.
화면 단위 Component는 pages 폴더에 두는 방식이 일반적이다.

---

# 15. Troubleshooting Rules

## 15.1 Blank Page After Routing

### [개념]

Blank Page After Routing은 URL은 바뀌었지만 화면이 비어 보이는 문제다.

---

### [핵심]

문제:

- Link 클릭 후 빈 화면
- Route가 매칭되지 않음
- Nested Route 자식이 안 보임
- Layout은 보이는데 content 없음

원인:

- Route path 오타
- Link to 오타
- element 누락
- Component import 오류
- Outlet 누락
- BrowserRouter 누락
- 잘못된 basename
- NotFoundRoute 누락

해결:

- Console Error 확인
- Route path와 Link to 비교
- BrowserRouter 감싸기 확인
- Nested 부모에 Outlet 확인
- Component import 확인
- NotFoundPage 추가
- React DevTools 확인

---

### [실무]

Debug Flow:

```text
URL Check
→ Route Definition Check
→ Link to Check
→ BrowserRouter Check
→ Outlet Check
→ Console Error Check
→ Component Import Check
```

---

### [FAQ]

Q. URL은 바뀌는데 화면이 안 나와?

A.
Route path와 Link to가 맞는지, element가 있는지, BrowserRouter와 Outlet이 있는지 확인한다.

Q. Nested Route 자식 화면이 안 나와?

A.
부모 Layout Component에 Outlet이 없을 가능성이 크다.

---

## 15.2 Params Undefined Problem

### [개념]

Params Undefined Problem은 useParams에서 기대한 parameter 값이 undefined로 나오는 문제다.

---

### [핵심]

문제:

- festivalId가 undefined
- userId가 undefined
- 상세 API 호출 URL에 undefined 포함
- Number(undefined)로 NaN 발생

원인:

- Route path에 param 없음
- param 이름 불일치
- Link URL 생성 오류
- 중첩 route 위치 오류
- optional param 처리 누락

해결:

- Route path 확인
- useParams key 이름 확인
- Link URL 확인
- path builder 사용
- param 존재 여부 guard
- Number 변환 전 검증

---

### [실무]

나쁜 예:

```jsx
<Route path="/festivals/:id" element={<FestivalDetailPage />} />;

function FestivalDetailPage() {
  const { festivalId } = useParams();
}
```

문제:

- Route param 이름은 `id`
- useParams key는 `festivalId`
- 이름 불일치

좋은 예:

```jsx
<Route path="/festivals/:festivalId" element={<FestivalDetailPage />} />;

function FestivalDetailPage() {
  const { festivalId } = useParams();
}
```

---

### [FAQ]

Q. useParams가 undefined인 이유는?

A.
Route path의 param 이름과 useParams에서 꺼내는 key 이름이 다를 수 있다.

Q. param을 숫자로 변환할 때 주의할 점은?

A.
undefined나 잘못된 값이면 NaN이 되므로 변환 전 존재 여부와 Number.isNaN을 확인한다.

---

## 15.3 Search Params Sync Problem

### [개념]

Search Params Sync Problem은 URL Query String과 Component State가 서로 불일치하는 문제다.

---

### [핵심]

문제:

- URL에는 keyword가 있는데 input은 비어 있음
- 뒤로가기 시 화면 상태가 맞지 않음
- 검색 후 새로고침하면 조건이 사라짐
- page 값이 문자열이라 계산 오류 발생
- setSearchParams 후 기존 params가 사라짐

원인:

- URL과 State를 중복 관리
- 초기값 동기화 누락
- setSearchParams에서 기존 param 미보존
- 타입 변환 누락
- 빈 값 처리 기준 없음

해결:

- URL을 source of truth로 사용
- State 초기값을 searchParams에서 설정
- 필요한 기존 param 유지
- Number / boolean 변환
- 빈 값은 delete 기준 정의
- 검색 submit 시 page reset

---

### [실무]

Debug Flow:

```text
URL Search Check
→ searchParams.get Check
→ State Initial Value Check
→ setSearchParams Logic Check
→ Type Conversion Check
→ Back Button Behavior Check
```

---

### [FAQ]

Q. URL query와 input 값이 달라?

A.
URL search params와 input state를 중복 관리하면서 동기화가 누락되었을 수 있다.

Q. 검색할 때 page는 어떻게 처리해?

A.
검색 조건이 바뀌면 일반적으로 page를 1로 reset하는 것이 좋다.

---

## 15.4 Refresh 404 Problem

### [개념]

Refresh 404 Problem은 React Router 내부 이동은 되지만 새로고침하거나 직접 URL 접근 시 서버 404가 발생하는 문제다.

---

### [핵심]

문제:

- `/mypage` 새로고침 404
- `/festivals/1` 직접 접근 404
- 배포 환경에서만 발생
- 로컬 dev server에서는 정상

원인:

- SPA fallback 설정 없음
- 서버가 해당 path 파일을 찾음
- BrowserRouter 사용
- API / static / frontend route 구분 부족

해결:

- 서버 fallback 설정
- Spring Boot forward controller 작성
- Nginx try_files 설정
- Static hosting rewrite 설정
- API path 제외
- 정적 resource 제외

---

### [실무]

Debug Flow:

```text
Direct URL Access
→ Server Response Status Check
→ Response Body Check
→ index.html Returned?
→ API Path Excluded?
→ Fallback Rule Fix
```

---

### [FAQ]

Q. React Router 새로고침 404는 React 코드 문제야?

A.
대부분 React 코드보다 배포 서버 fallback 설정 문제다.

Q. BrowserRouter 대신 HashRouter를 쓰면 해결돼?

A.
일부 배포 환경에서는 해결될 수 있지만 URL에 #이 들어간다. 가능하면 서버 fallback을 설정하는 것이 좋다.

---

# 16. Comparison Rules

## 16.1 Required Comparisons

### [개념]

React Router 문서는 헷갈리는 Routing 개념을 비교해서 작성한다.

---

### [핵심]

필수 비교 대상:

- Client Side Routing vs Server Side Routing
- BrowserRouter vs HashRouter
- Link vs NavLink
- Link vs useNavigate
- Navigate vs useNavigate
- Path Parameter vs Query String
- Route path vs API endpoint
- Layout Route vs Page Route
- Nested Route vs Flat Route
- Protected Route vs Backend Authorization
- BrowserRouter vs RouterProvider
- location.state vs Query String
- SPA 404 vs Server 404

---

### [실무]

예시:

| 비교      | Link                       | useNavigate                    |
| --------- | -------------------------- | ------------------------------ |
| 방식      | Component 기반 이동        | 함수 호출 이동                 |
| 사용 상황 | 사용자가 클릭하는 링크     | 로그인 성공, 저장 성공 후 이동 |
| UX        | 브라우저 링크 기본 UX 유지 | 코드 흐름 기반 이동            |
| 위치      | JSX                        | Event Handler / Effect         |
| 권장      | 일반 이동 우선             | 조건부 / 처리 후 이동          |

---

### [FAQ]

Q. 비교 표는 왜 필요해?

A.
사용자가 자주 헷갈리는 Routing 질문에서 Retrieval Hit와 답변 정확도를 높이기 위해 필요하다.

Q. React Router 비교 문서에서 가장 중요한 것은?

A.
실무 선택 기준과 잘못 선택했을 때 발생하는 문제를 함께 설명하는 것이다.

---

# 17. Checklist Rules

## 17.1 React Router Checklist

### [개념]

React Router 문서 검수 시 Routing 설계 체크리스트를 사용한다.

---

### [핵심]

Checklist:

```md
- [ ] React Router 목적이 설명되었는가?
- [ ] Client Side Routing과 Server Routing 차이가 포함되었는가?
- [ ] BrowserRouter 위치가 설명되었는가?
- [ ] Routes / Route 예제가 포함되었는가?
- [ ] Link / NavLink / useNavigate 차이가 포함되었는가?
- [ ] Dynamic Route와 useParams가 포함되었는가?
- [ ] Query String과 useSearchParams가 포함되었는가?
- [ ] Nested Route와 Outlet이 포함되었는가?
- [ ] Layout Route 기준이 포함되었는가?
- [ ] Protected Route 기준이 포함되었는가?
- [ ] Role Based Route 기준이 포함되었는가?
- [ ] Not Found Route가 포함되었는가?
- [ ] SPA Refresh 404와 fallback 설명이 포함되었는가?
- [ ] API Path Collision 주의가 포함되었는가?
- [ ] Version 차이 주의가 포함되었는가?
- [ ] Troubleshooting이 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 기준:

```text
Draft
→ Route Concept Check
→ Navigation Check
→ Params Check
→ Nested Route Check
→ Protected Route Check
→ SPA Fallback Check
→ Troubleshooting Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

---

### [FAQ]

Q. React Router 문서 검수에서 가장 중요한 것은?

A.
Route 정의, Navigation, Params, Search Params, Nested Route, Protected Route, SPA Fallback, Troubleshooting 포함 여부다.

---

# 18. Retrieval Optimization Rules

## 18.1 Keyword Rules

### [개념]

React Router 문서는 검색 매칭을 위해 핵심 키워드를 반복 허용한다.

---

### [핵심]

강조 키워드:

- React Router
- React Routing
- SPA Routing
- Client Side Routing
- BrowserRouter
- HashRouter
- Routes
- Route
- Link
- NavLink
- Navigate
- useNavigate
- useParams
- useSearchParams
- useLocation
- Outlet
- Nested Route
- Layout Route
- Index Route
- Dynamic Route
- Path Parameter
- Query String
- Search Params
- Protected Route
- Private Route
- Role Based Route
- Auth Redirect
- Not Found Route
- Catch All Route
- Route Constants
- RouterProvider
- createBrowserRouter
- Data Router
- Browser Refresh 404
- SPA Fallback
- Spring Boot React Router Refresh
- API Path Collision
- Route Troubleshooting

---

### [실무]

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

예:

- React Router는 뭐야?
- BrowserRouter는 어디에 둬?
- Routes Route는 어떻게 써?
- Link와 useNavigate 차이는?
- NavLink는 언제 써?
- useParams가 undefined인 이유는?
- URL query string은 어떻게 읽어?
- useSearchParams는 어떻게 써?
- Nested Route에서 Outlet은 왜 필요해?
- Protected Route는 어떻게 만들어?
- React Router 새로고침 404는 왜 나?
- Spring Boot에 React build 넣었는데 새로고침 404 해결법은?
- API 요청했는데 index.html이 응답되는 이유는?
- path param과 query string 차이는?
- React Router v6 v7 import 차이는?

---

### [FAQ]

Q. 키워드 반복은 중복이야?

A.
불필요한 장문 중복은 금지지만 Retrieval 최적화를 위한 핵심 키워드 반복은 허용된다.

Q. FAQ 질문은 어떤 스타일이 좋아?

A.
실제 사용자가 검색하거나 질문할 법한 문장형 질문이 좋다.

---

# 19. Version Rules

## 19.1 Modern React Router 기준

### [개념]

React Router 문서는 Modern React Router 기준으로 작성한다.

---

### [핵심]

기준:

- React Router v6+
- React Router v7 인지
- React 18+
- React 19 호환 고려
- Declarative Routing
- BrowserRouter / Routes / Route
- Link / NavLink
- useNavigate
- useParams
- useSearchParams
- Nested Route / Outlet
- Protected Route
- Data Router Basics Mention
- Framework Mode Basics Mention
- TypeScript Ready

Legacy 제외:

- Switch 중심 설명
- component prop 중심 Route 설명
- exact 중심 설명
- withRouter 중심 설명
- useHistory 중심 설명
- v5 route order 중심 설명
- class component routing 중심 설명
- HashRouter 기본 권장
- jQuery location 변경 중심 설명

---

### [실무]

실무 기준:

```text
Modern React Router
→ BrowserRouter
→ Routes / Route
→ Link / NavLink
→ Params / Search Params
→ Nested Route / Outlet
→ Protected Route
→ SPA Fallback
```

---

### [FAQ]

Q. Switch를 써야 해?

A.
아니다. React Router v6+에서는 Routes를 사용한다.

Q. useHistory를 써야 해?

A.
아니다. React Router v6+에서는 useNavigate를 사용한다.

Q. exact를 써야 해?

A.
아니다. React Router v6+의 Route 매칭 방식에서는 v5처럼 exact를 쓰지 않는다.

---

# 20. Common Mistakes

## 20.1 React Router Common Mistakes

### [개념]

React Router 문서는 자주 발생하는 Routing 실수를 명확히 포함해야 한다.

---

### [핵심]

자주 발생:

- BrowserRouter로 App을 감싸지 않음
- Router Hook을 Router 밖에서 사용
- Route element에 Component 함수 자체를 넣음
- Link to와 Route path 불일치
- useParams param 이름 불일치
- useParams 문자열을 숫자로 변환하지 않음
- Nested Route 부모에 Outlet 누락
- 자식 Route path에 slash 혼동
- Index Route에 path 사용
- NotFound Route 누락
- Protected Route에서 auth loading 처리 누락
- 무한 redirect 발생
- Frontend Route 보호를 보안으로 착각
- Query String과 State 중복 관리
- setSearchParams에서 기존 param 삭제
- BrowserRouter 배포 fallback 누락
- API path와 Frontend path 충돌
- API 요청이 index.html을 응답
- React Router v5 문법과 v6+ 문법 혼용
- `react-router` / `react-router-dom` import 혼용

---

### [실무]

문서 작성 시 Common Mistakes는 Troubleshooting과 연결한다.

예:

```text
문제: /festivals/1 새로고침 404
원인: 서버가 /festivals/1 파일을 찾고 index.html fallback을 하지 않음
해결: API와 정적 리소스를 제외한 SPA 경로를 index.html로 forward
```

---

### [FAQ]

Q. React Router 초보가 가장 많이 하는 실수는?

A.
BrowserRouter 누락, path 오타, Outlet 누락, useParams 이름 불일치, 새로고침 404를 많이 겪는다.

Q. React Router 문제는 어떻게 찾는 게 좋아?

A.
URL, Route path, Link to, Router 감싸기, Outlet, Params 이름, Network 응답, 서버 fallback을 순서대로 확인한다.

---

# 21. Final Goal

## 21.1 Domain Final Goal

### [개념]

React Router RAG 문서는 Frontend Agent가 SPA Route 구조를 안정적으로 설계하고 구현하며 배포 오류까지 검토하도록 지원해야 한다.

---

### [핵심]

최종 목표:

- Client Side Routing 이해
- BrowserRouter 구성
- Routes / Route 작성
- Page Component 연결
- Link / NavLink 작성
- useNavigate 이동 구현
- Dynamic Route 작성
- useParams 처리
- Query String 처리
- useSearchParams 처리
- Nested Route 작성
- Outlet 적용
- Layout Route 설계
- Index Route 작성
- Protected Route 작성
- Role Based Route 작성
- Auth Redirect 구현
- Not Found Route 작성
- Route File Structure 설계
- SPA Refresh 404 원인 분석
- Spring Boot / Nginx / Static Hosting Fallback 검토
- API Path Collision 검토
- React Router Troubleshooting 수행

---

### [실무]

Agent 수행 가능 작업:

```text
User Page Flow Request
→ Define Route Paths
→ Connect Page Components
→ Add Layout Route
→ Add Params / Search Params
→ Add Protected Route
→ Add Not Found Route
→ Check SPA Fallback
→ Review Route Troubleshooting
→ React Router Output
```

---

### [FAQ]

Q. React Router 문서의 최종 목적은 뭐야?

A.
Frontend Agent가 URL과 Page Component를 연결하고, Nested Route, Protected Route, Query String, SPA Fallback까지 안정적으로 설계하게 만드는 것이다.

Q. 이 문서 다음에는 어떤 Domain Rules가 이어져야 해?

A.
State Management, Data Fetching & REST API Integration, Authentication Frontend Flow, Error Handling & Loading UX 순서로 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. React Router 문서는 왜 필요해?
A. Frontend Agent가 SPA에서 URL과 Page Component를 연결하고 화면 이동 구조를 설계해야 하기 때문이다.

Q. React Router는 뭐야?
A. React SPA에서 URL path에 따라 어떤 Component를 렌더링할지 결정하는 Client Side Router다.

Q. SPA Routing이 뭐야?
A. 페이지 전체를 다시 로드하지 않고 URL에 맞는 React Component를 브라우저 안에서 렌더링하는 방식이다.

Q. React Router는 서버 요청을 처리해?
A. 아니다. React Router는 브라우저에서 동작하는 Client Side Router다.

Q. Client Side Routing과 Server Side Routing 차이는?
A. Client Side Routing은 브라우저에서 Component를 바꾸고 Server Side Routing은 서버가 URL 요청을 처리해 응답을 반환한다.

Q. BrowserRouter는 어디에 둬?
A. 보통 main.jsx, main.tsx, index.jsx 같은 React entry point에서 App을 감싼다.

Q. BrowserRouter를 여러 번 감싸도 돼?
A. 일반적으로 앱 전체를 한 번만 감싼다. 중첩 Router는 혼란을 만들 수 있다.

Q. Routes와 Route는 어떻게 써?
A. Routes 안에 Route를 두고 path와 element를 연결한다.

Q. Route의 element에는 뭘 넣어?
A. 렌더링할 React Element를 넣는다. 예: `element={<LoginPage />}`.

Q. React Router에서 404 페이지는 어떻게 만들어?
A. `path="*"` Route를 추가하고 NotFoundPage를 렌더링한다.

Q. Route path를 상수로 관리해야 해?
A. 작은 프로젝트는 직접 문자열도 가능하지만 경로가 많아지면 상수 관리가 오타를 줄인다.

Q. 동적 path는 어떻게 만들어?
A. Route pattern은 `/festivals/:festivalId`처럼 정의하고 실제 이동 URL은 `/festivals/1`처럼 만든다.

Q. Index Route는 언제 써?
A. 부모 경로에 들어왔을 때 기본으로 보여줄 자식 화면이 필요할 때 사용한다.

Q. Index Route에 path를 써도 돼?
A. 아니다. index route는 path 없이 `index` 속성을 사용한다.

Q. React Router에서 a 태그 대신 Link를 쓰는 이유는?
A. 내부 Route 이동 시 페이지 전체 reload 없이 React Router가 URL과 화면을 갱신하기 위해서다.

Q. 외부 사이트 이동도 Link를 써?
A. 아니다. 외부 URL 이동은 일반 a 태그를 사용한다.

Q. Link의 to에는 뭘 넣어?
A. 이동할 내부 Route path를 넣는다. 예: `/login`, `/festivals/1`.

Q. Link와 NavLink 차이는?
A. Link는 단순 이동이고 NavLink는 현재 URL과 일치할 때 active 상태를 알 수 있다.

Q. NavLink는 언제 써?
A. Header, Sidebar, Tab Menu처럼 현재 선택된 메뉴 표시가 필요할 때 사용한다.

Q. Link와 useNavigate 중 뭐를 써?
A. 사용자가 클릭해서 이동하는 일반 링크는 Link를 우선하고, 로그인 성공 후 이동처럼 코드 흐름에 따른 이동은 useNavigate를 사용한다.

Q. useNavigate는 언제 써?
A. 로그인 성공, 저장 완료, 삭제 완료, 권한 없음 redirect처럼 코드 흐름에 따라 이동할 때 사용한다.

Q. navigate replace는 언제 써?
A. 로그인 페이지 redirect처럼 사용자가 뒤로가기로 다시 돌아오면 안 되는 경우에 사용한다.

Q. useNavigate를 Router 밖에서 쓸 수 있어?
A. 안 된다. Router 내부 Component에서만 사용할 수 있다.

Q. Navigate와 useNavigate 차이는?
A. Navigate는 렌더링 결과로 redirect하고 useNavigate는 함수 호출로 이동한다.

Q. Protected Route에는 Navigate를 써도 돼?
A. 가능하다. 인증 상태에 따라 login 페이지로 redirect할 때 자주 사용한다.

Q. Dynamic Route는 뭐야?
A. URL 일부를 변수처럼 받는 Route다. 예: `/festivals/:festivalId`.

Q. useParams 값은 number야 string이야?
A. 문자열이다. 숫자 ID로 쓰려면 Number로 변환해야 한다.

Q. useParams가 undefined인 이유는?
A. Route path에 해당 param이 없거나 param 이름이 맞지 않을 수 있다.

Q. 상세 페이지 path는 어떻게 잡아?
A. 일반적으로 `/resources/:resourceId` 형태를 사용한다. 예: `/festivals/:festivalId`.

Q. Query String은 뭐야?
A. URL에서 `?keyword=spring&page=1`처럼 검색 조건이나 옵션을 표현하는 부분이다.

Q. useSearchParams는 어떻게 써?
A. searchParams.get으로 값을 읽고 setSearchParams로 query string을 수정한다.

Q. 검색 조건은 State로 둬야 해 Query String으로 둬야 해?
A. URL 공유, 새로고침 유지, 뒤로가기 복원이 필요하면 Query String으로 관리하는 것이 좋다.

Q. useSearchParams 값은 number로 바로 받아?
A. 아니다. 문자열로 읽히므로 Number 변환이 필요하다.

Q. setSearchParams를 호출하면 페이지 이동이야?
A. URL search params가 바뀌므로 navigation이 발생한다.

Q. Path Parameter와 Query String 차이는?
A. Path Parameter는 리소스 식별에 사용하고 Query String은 검색, 필터, 정렬, 페이지 같은 옵션에 사용한다.

Q. ID는 path param이 좋아 query string이 좋아?
A. 특정 리소스 식별 ID는 path parameter가 일반적으로 적합하다.

Q. 검색어는 path param으로 넣어도 돼?
A. 가능은 하지만 필터와 검색 조건은 Query String이 더 적합한 경우가 많다.

Q. Nested Route는 언제 써?
A. 공통 Layout 안에서 하위 화면이 바뀌는 구조가 필요할 때 사용한다.

Q. Nested Route 화면이 안 나와?
A. 부모 Component에 `<Outlet />`이 없을 가능성이 크다.

Q. Outlet은 왜 필요해?
A. 부모 Route Component 안에서 자식 Route Component가 표시될 위치를 지정하기 위해 필요하다.

Q. 자식 Route path에 slash를 붙여야 해?
A. 상대 경로로 쓰려면 보통 slash 없이 작성한다. 절대 경로가 필요한 경우 의도를 명확히 해야 한다.

Q. Layout Route는 왜 써?
A. 여러 페이지에서 공통 Header, Footer, Sidebar 구조를 중복 작성하지 않기 위해 사용한다.

Q. Layout Route에 path가 없어도 돼?
A. 가능하다. path 없는 Layout Route는 자식 Route를 공통 Layout으로 감싸는 데 사용할 수 있다.

Q. Protected Route는 어떻게 만들어?
A. 인증 상태를 확인하고 비로그인 상태면 Navigate로 login 페이지에 redirect한다.

Q. Protected Route는 보안적으로 충분해?
A. 아니다. Frontend Route 보호는 UX용이다. 실제 보안은 Backend 인증/인가가 반드시 필요하다.

Q. 인증 상태 확인 전 바로 login으로 보내도 돼?
A. 권장하지 않는다. 인증 상태 loading 중에는 임시 로딩 UI를 보여주고 확인 후 redirect해야 한다.

Q. 로그인 후 원래 페이지로 돌아가려면?
A. location state나 query string에 redirect target을 저장해 로그인 성공 후 이동할 수 있다.

Q. Role Based Route는 뭐야?
A. 사용자 권한에 따라 접근 가능한 Route를 제한하는 구조다.

Q. Frontend에서 ROLE_ADMIN 체크하면 보안이 되는 거야?
A. 아니다. Frontend 권한 체크는 화면 접근 UX용이고 실제 API 보안은 Backend에서 검증해야 한다.

Q. 권한 없는 사용자는 어디로 보내?
A. 프로젝트 기준에 따라 `/forbidden`, `/login`, `/` 중 하나로 보낼 수 있다. 기준을 통일해야 한다.

Q. useLocation은 언제 써?
A. 현재 URL path, search, state 정보가 필요할 때 사용한다.

Q. location.state는 새로고침해도 남아?
A. 보장되지 않는다. 영구적으로 유지해야 하는 정보는 query string이나 storage를 고려한다.

Q. Navigation State는 언제 써?
A. 로그인 후 돌아갈 경로처럼 임시 이동 정보를 전달할 때 사용한다.

Q. Navigation State에 중요한 데이터를 넣어도 돼?
A. 권장하지 않는다. 새로고침이나 직접 접근 시 사라질 수 있고 URL 공유에도 포함되지 않는다.

Q. SPA 404와 서버 404는 달라?
A. 다르다. SPA 404는 React Router가 매칭 실패를 처리하는 화면이고 서버 404는 서버가 파일이나 경로를 찾지 못한 응답이다.

Q. 잘못된 URL parameter는 어떻게 처리해?
A. Number 변환 실패나 필수 param 누락을 확인하고 NotFoundPage나 Error UI를 보여준다.

Q. API 404와 Route 404는 어떻게 달라?
A. Route 404는 URL이 Route와 매칭되지 않는 경우이고 API 404는 서버 리소스를 찾지 못한 경우다.

Q. BrowserRouter와 RouterProvider를 같이 써?
A. 일반적으로 같이 쓰지 않는다. BrowserRouter 방식과 createBrowserRouter / RouterProvider 방식 중 하나를 선택한다.

Q. loader와 action은 뭐야?
A. Route 단위 데이터 로딩과 제출 처리를 담당하는 Data Router 기능이다. Foundation 문서에서는 개념만 다룬다.

Q. React Router 새로고침 404는 왜 나?
A. 서버가 SPA 경로를 index.html로 fallback하지 않아서 발생하는 경우가 많다.

Q. React Router는 로컬에서 되는데 배포 후 새로고침하면 404가 나?
A. 서버가 `/festivals/1` 같은 SPA 경로를 실제 파일로 찾고 index.html로 fallback하지 않아서 발생할 수 있다.

Q. Spring Boot에 React build를 넣으면 새로고침 404는 어떻게 해결해?
A. API와 정적 리소스를 제외한 Frontend Route를 `forward:/index.html`로 보내는 fallback Controller를 구성한다.

Q. 모든 요청을 index.html로 보내도 돼?
A. 안 된다. `/api/**`, 정적 리소스, 실제 Backend Controller 경로는 제외해야 한다.

Q. API 요청했는데 index.html이 응답돼?
A. SPA fallback Controller가 API 요청까지 forward하고 있을 가능성이 있다. API path를 fallback에서 제외해야 한다.

Q. Frontend Route와 Backend API 경로는 어떻게 구분해?
A. Backend API는 `/api` prefix를 두고 Frontend Route는 화면 URL로 분리하는 것이 안전하다.

Q. URL은 바뀌는데 화면이 안 나와?
A. Route path와 Link to가 맞는지, element가 있는지, BrowserRouter와 Outlet이 있는지 확인한다.

Q. URL query와 input 값이 달라?
A. URL search params와 input state를 중복 관리하면서 동기화가 누락되었을 수 있다.

Q. 검색할 때 page는 어떻게 처리해?
A. 검색 조건이 바뀌면 일반적으로 page를 1로 reset하는 것이 좋다.

Q. React Router import는 react-router야 react-router-dom이야?
A. 프로젝트 버전에 따라 다를 수 있다. v6 프로젝트는 react-router-dom이 흔하고 v7 공식 문서는 react-router 예제를 제공할 수 있다. 프로젝트 기준으로 통일한다.

Q. Switch를 써야 해?
A. 아니다. React Router v6+에서는 Routes를 사용한다.

Q. useHistory를 써야 해?
A. 아니다. React Router v6+에서는 useNavigate를 사용한다.

Q. exact를 써야 해?
A. 아니다. React Router v6+의 Route 매칭 방식에서는 v5처럼 exact를 쓰지 않는다.

Q. React Router 문제는 어떻게 찾는 게 좋아?
A. URL, Route path, Link to, Router 감싸기, Outlet, Params 이름, Network 응답, 서버 fallback을 순서대로 확인한다.

Q. React Router 다음 문서는 뭐가 좋아?
A. State Management, Data Fetching & REST API Integration, Authentication Frontend Flow, Error Handling & Loading UX 순서가 좋다.
