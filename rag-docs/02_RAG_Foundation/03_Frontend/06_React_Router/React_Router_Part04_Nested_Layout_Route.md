# React Router Part04 Nested Layout Route

---

# 1. Nested Route and Layout Route

## 1.1 Purpose

### [개념]

Nested Route와 Layout Route는 React Router에서 공통 UI 구조와 하위 Page Component를 계층적으로 연결하는 Routing 구조다.

Nested Route는 부모 Route 안에 자식 Route를 배치하는 방식이다.

Layout Route는 Header, Footer, Sidebar, Tab Menu 같은 공통 화면 구조를 제공하고 자식 Route를 Outlet에 렌더링하는 방식이다.

이 문서는 Frontend Agent가 Page Route Structure, Nested Route, Outlet, Layout Route, Route File Structure를 안정적으로 설계하도록 지원한다.

---

### [핵심]

- Nested Route
- Layout Route
- Outlet
- Parent Route
- Child Route
- Index Route
- Relative Path
- Page Component
- Layout Component
- Route Hierarchy
- Common Layout
- Header / Footer
- Sidebar Layout
- MyPage Layout
- Admin Layout
- Detail Tab Route
- Route File Structure

기본 관계:

```text
Parent Route
→ Layout Component
→ Outlet
→ Child Route Component
```

---

### [실무]

2026 실무 기준에서 Nested Route와 Layout Route는 화면 중복 제거와 URL 구조 정합성을 위해 사용한다.

실무 사용 대상:

- 공통 Header / Footer가 있는 Main Layout
- 로그인 / 회원가입용 Auth Layout
- 마이페이지 Sidebar Layout
- 관리자 Dashboard Layout
- 상세 페이지 Tab Layout
- 설정 페이지 Nested Layout
- 권한별 Page Grouping
- Page Route Structure 정리

예상 구조:

```text
/
├ MainLayout
│ ├ /
│ ├ /festivals
│ ├ /festivals/:festivalId
│ └ /mypage
├ AuthLayout
│ ├ /login
│ └ /signup
└ AdminLayout
  └ /admin
```

Route 설계 Flow:

```text
Page Group 확인
→ 공통 UI 확인
→ Layout Component 생성
→ Parent Route 정의
→ Child Route 정의
→ Outlet 위치 지정
→ Index Route 필요 여부 확인
→ Not Found Route 확인
```

---

### [FAQ]

Q. Nested Route는 왜 필요해?
A. 공통 Layout 안에서 하위 화면을 URL에 따라 바꾸기 위해 필요하다.

Q. Layout Route는 왜 필요해?
A. Header, Footer, Sidebar 같은 공통 UI를 여러 Page에서 중복 작성하지 않기 위해 필요하다.

Q. Outlet은 왜 필요해?
A. 부모 Layout Component 안에서 자식 Route Component가 렌더링될 위치를 지정하기 위해 필요하다.

Q. Nested Route와 Layout Route의 핵심은 뭐야?
A. 부모 Route가 공통 구조를 담당하고 자식 Route가 실제 하위 Page를 렌더링하는 것이다.

---

# 2. Nested Route

## 2.1 Nested Route Concept

### [개념]

Nested Route는 부모 Route 아래에 자식 Route를 구성하는 방식이다.

부모 Route는 공통 UI 또는 상위 화면 구조를 담당하고, 자식 Route는 Outlet 위치에 렌더링된다.

---

### [핵심]

- Nested Route
- Parent Route
- Child Route
- Route Hierarchy
- Outlet
- Relative Path
- Index Route
- Layout Route
- Child Render Position

기본 예:

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
→ Outlet: MyPageHome

/mypage/profile
→ MyPageLayout
→ Outlet: ProfilePage

/mypage/favorites
→ MyPageLayout
→ Outlet: FavoritePage
```

---

### [실무]

Nested Route 사용 상황:

- MyPage 내부 메뉴
- Admin Dashboard
- Settings Page
- Festival Detail Tab
- 공통 Sidebar + Content 구조
- 공통 Header + 하위 Page 구조
- Page Group별 Layout 분리

예:

```jsx
<Route path="/admin" element={<AdminLayout />}>
  <Route index element={<AdminDashboardPage />} />
  <Route path="users" element={<AdminUserPage />} />
  <Route path="festivals" element={<AdminFestivalPage />} />
</Route>
```

실무 기준:

- 부모 Component에는 Outlet 필요
- 자식 Route path는 보통 slash 없이 상대 경로 사용
- 부모 경로 기본 화면은 index route 사용
- 중첩 깊이는 과도하게 늘리지 않음
- Layout Component는 공통 UI 책임만 담당
- Page별 데이터 로직은 Page Component나 Custom Hook으로 분리
- URL 구조와 화면 구조가 과도하게 어긋나지 않도록 설계

---

### [FAQ]

Q. Nested Route는 언제 써?
A. 공통 Layout 안에서 하위 화면이 바뀌는 구조가 필요할 때 사용한다.

Q. Nested Route 화면이 안 나와?
A. 부모 Component에 `<Outlet />`이 없을 가능성이 크다.

Q. 자식 Route path에 slash를 붙여야 해?
A. 상대 경로로 쓰려면 보통 slash 없이 작성한다. 절대 경로가 필요한 경우 의도를 명확히 해야 한다.

Q. Nested Route는 깊게 많이 중첩해도 돼?
A. 가능은 하지만 과도한 중첩은 구조 이해와 유지보수를 어렵게 하므로 필요한 수준으로 제한한다.

---

## 2.2 Relative Path Rules

### [개념]

Relative Path는 Nested Route에서 부모 Route 경로를 기준으로 자식 Route path를 작성하는 방식이다.

자식 Route의 path에 앞 slash를 붙이지 않으면 부모 Route에 상대적으로 연결된다.

---

### [핵심]

- Relative Path
- Child Route Path
- Parent Route Path
- Slash 없음
- Absolute Path
- Nested Route Matching
- Route Hierarchy

예:

```jsx
<Route path="/mypage" element={<MyPageLayout />}>
  <Route path="profile" element={<ProfilePage />} />
</Route>
```

결과:

```text
Parent path: /mypage
Child path: profile
Matched URL: /mypage/profile
```

---

### [실무]

권장 예:

```jsx
<Route path="/festivals/:festivalId" element={<FestivalDetailLayout />}>
  <Route index element={<FestivalOverviewPage />} />
  <Route path="reviews" element={<FestivalReviewPage />} />
  <Route path="map" element={<FestivalMapPage />} />
</Route>
```

결과:

```text
/festivals/123
→ Overview

/festivals/123/reviews
→ Reviews

/festivals/123/map
→ Map
```

주의:

- 자식 Route에 `/reviews`처럼 slash를 붙이면 의도와 다르게 절대 경로가 될 수 있음
- 중첩 Route에서는 상대 경로를 기본으로 사용
- Link / NavLink의 to 값도 상대 경로 또는 절대 경로 기준을 명확히 함
- Route path와 Navigation path 정합성 확인
- index route에는 path를 쓰지 않음

---

### [FAQ]

Q. 자식 Route path에 slash를 붙이면 어떻게 돼?
A. 절대 경로로 해석될 수 있어 부모 Route 기준 중첩 의도와 달라질 수 있다.

Q. Nested Route의 자식 path는 보통 어떻게 써?
A. 보통 `profile`, `reviews`, `settings`처럼 앞 slash 없이 상대 경로로 작성한다.

Q. 부모 path가 `/mypage`이고 자식 path가 `profile`이면 URL은 뭐야?
A. `/mypage/profile`이다.

Q. index route에도 path를 써?
A. 아니다. index route는 path 없이 `index` 속성을 사용한다.

---

# 3. Outlet

## 3.1 Outlet Concept

### [개념]

Outlet은 Nested Route의 자식 Component가 렌더링될 위치를 표시하는 React Router Component다.

부모 Layout Component 안에서 Outlet이 있는 자리에 현재 매칭된 자식 Route의 element가 렌더링된다.

---

### [핵심]

- Outlet
- Child Route Render Position
- Parent Layout
- Nested UI
- Route Hierarchy
- Layout Component
- Content Area
- Child Component Slot

기본 예:

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

동작:

```text
Parent Layout Render
→ Sidebar Render
→ Outlet Position
→ Matched Child Route Render
```

---

### [실무]

Outlet 사용 상황:

- Header + Main Content
- Sidebar + Content
- Admin Layout
- MyPage Layout
- Festival Detail Tab Layout
- Settings Layout
- Auth Layout 내부 form area

예:

```jsx
function AdminLayout() {
  return (
    <div className="admin-layout">
      <AdminSidebar />
      <main className="admin-content">
        <Outlet />
      </main>
    </div>
  );
}
```

실무 기준:

- 부모 Route element가 Layout이면 Outlet 필수
- Outlet이 없으면 자식 Route가 화면에 보이지 않음
- Outlet 위치가 실제 자식 Page 렌더링 위치
- Layout Component는 공통 구조만 담당
- 자식 Page의 데이터 로직을 Layout에 과도하게 넣지 않음
- 접근성을 위해 main, nav, section 구조 고려
- 하나의 Layout에서 여러 Outlet을 쓰는 구조는 일반적이지 않음

---

### [FAQ]

Q. Outlet은 뭐야?
A. 부모 Route Component 안에서 자식 Route Component가 표시될 위치를 지정하는 Component다.

Q. Outlet이 없으면 어떻게 돼?
A. 부모 Layout은 보일 수 있지만 자식 Route 화면이 렌더링되지 않는다.

Q. Outlet은 어디에 둬?
A. 자식 Page가 표시되어야 하는 위치에 둔다. 예: Sidebar 옆 content 영역.

Q. Outlet을 여러 개 둘 수 있어?
A. 일반적인 Nested Route에서는 하나의 Outlet로 자식 Route 렌더링 위치를 지정한다. 여러 영역이 필요하면 Layout 구조를 다시 설계한다.

---

## 3.2 Outlet Missing Problem

### [개념]

Outlet Missing Problem은 Nested Route를 정의했지만 부모 Component에 Outlet이 없어 자식 Route 화면이 렌더링되지 않는 문제다.

URL은 바뀌지만 화면 내용이 바뀌지 않거나 Layout만 보이는 증상으로 나타난다.

---

### [핵심]

문제:

- URL은 `/mypage/profile`로 바뀜
- Sidebar는 보임
- ProfilePage가 안 보임
- Layout만 렌더링됨
- 자식 Route element가 표시되지 않음

원인:

- 부모 Layout에 Outlet 없음
- Outlet 위치가 조건부 렌더링으로 숨겨짐
- 자식 Route 구조가 부모 Route 안에 없음
- 잘못된 Route path
- 잘못된 Layout Component import

---

### [실무]

문제 예:

```jsx
function MyPageLayout() {
  return (
    <main>
      <MyPageSidebar />
      <section>Content</section>
    </main>
  );
}
```

Route:

```jsx
<Route path="/mypage" element={<MyPageLayout />}>
  <Route path="profile" element={<ProfilePage />} />
</Route>
```

문제:

```text
MyPageLayout에 Outlet이 없어서 ProfilePage가 렌더링되지 않음
```

해결:

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

Debug Flow:

```text
Nested Route 화면 안 보임
→ Current URL 확인
→ Parent Route 확인
→ Child Route 확인
→ Parent Layout Outlet 확인
→ Outlet 위치 확인
→ Console Error 확인
```

---

### [FAQ]

Q. Nested Route에서 URL은 바뀌는데 자식 화면이 안 나와?
A. 부모 Layout Component에 `<Outlet />`이 없을 가능성이 크다.

Q. Layout은 보이는데 content가 안 바뀌어?
A. Outlet 위치와 자식 Route 구조를 확인해야 한다.

Q. Outlet을 추가했는데도 안 나와?
A. 자식 Route가 부모 Route 내부에 정의되었는지, path가 맞는지, Component import 오류가 없는지 확인한다.

Q. Outlet Missing Problem은 어떻게 디버깅해?
A. URL, 부모 Route, 자식 Route, 부모 Layout의 Outlet, Console Error를 순서대로 확인한다.

---

# 4. Layout Route

## 4.1 Layout Route Concept

### [개념]

Layout Route는 공통 UI 구조를 제공하고 자식 Route를 Outlet에 렌더링하는 Route다.

Layout Route는 여러 Page에서 반복되는 Header, Footer, Sidebar, Navigation 구조를 공통화한다.

---

### [핵심]

- Layout Route
- Layout Component
- Common UI
- Header
- Footer
- Sidebar
- Outlet
- Parent Route
- Child Page
- Route Group
- Pathless Layout Route
- Nested Layout

기본 예:

```jsx
<Route element={<MainLayout />}>
  <Route path="/" element={<MainPage />} />
  <Route path="/festivals" element={<FestivalListPage />} />
  <Route path="/festivals/:festivalId" element={<FestivalDetailPage />} />
</Route>
```

Layout Component:

```jsx
import { Outlet } from "react-router";

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

---

### [실무]

Layout Route 유형:

```text
MainLayout
→ Header / Footer 포함
→ 일반 서비스 페이지

AuthLayout
→ 로그인 / 회원가입 전용
→ 간소화된 화면

MyPageLayout
→ Sidebar / Profile Summary 포함
→ 마이페이지 하위 화면

AdminLayout
→ Admin Sidebar / Admin Header 포함
→ 관리자 하위 화면

DetailLayout
→ Detail Header / Tab Menu 포함
→ 상세 페이지 하위 탭
```

실무 기준:

- Layout은 공통 UI 구조 담당
- Page Component는 실제 화면 내용 담당
- Layout에 Page별 API 로직을 과도하게 넣지 않음
- 공통 인증 상태, 사용자 정보 표시 정도는 Layout에서 가능
- Layout Route는 path가 있을 수도 있고 없을 수도 있음
- path 없는 Layout Route는 자식 Route를 공통 Layout으로 감쌀 때 사용
- Auth Layout과 Main Layout을 분리하면 Header 노출 기준이 명확해짐

---

### [FAQ]

Q. Layout Route는 뭐야?
A. 공통 UI를 제공하고 자식 Route를 Outlet에 렌더링하는 Route다.

Q. Layout Route는 왜 써?
A. 여러 페이지에서 공통 Header, Footer, Sidebar 구조를 중복 작성하지 않기 위해 사용한다.

Q. Layout Route에 path가 없어도 돼?
A. 가능하다. path 없는 Layout Route는 자식 Route를 공통 Layout으로 감싸는 데 사용할 수 있다.

Q. Layout Component에는 어떤 로직을 넣어?
A. 공통 UI와 공통 상태 표시 정도를 넣고 Page별 데이터 로직은 Page Component나 Hook으로 분리하는 것이 좋다.

---

## 4.2 Pathless Layout Route

### [개념]

Pathless Layout Route는 path 없이 element만 가진 Layout Route다.

URL segment를 추가하지 않고 여러 자식 Route를 공통 Layout으로 감쌀 때 사용한다.

---

### [핵심]

- Pathless Layout Route
- No path
- Layout Wrapper
- Shared UI
- Child Route Group
- Outlet
- Route Grouping
- URL unchanged

예:

```jsx
<Route element={<MainLayout />}>
  <Route path="/" element={<MainPage />} />
  <Route path="/festivals" element={<FestivalListPage />} />
</Route>
```

동작:

```text
/
→ MainLayout
→ Outlet: MainPage

/festivals
→ MainLayout
→ Outlet: FestivalListPage
```

---

### [실무]

Main / Auth Layout 분리 예:

```jsx
<Routes>
  <Route element={<MainLayout />}>
    <Route path="/" element={<MainPage />} />
    <Route path="/festivals" element={<FestivalListPage />} />
    <Route path="/festivals/:festivalId" element={<FestivalDetailPage />} />
  </Route>

  <Route element={<AuthLayout />}>
    <Route path="/login" element={<LoginPage />} />
    <Route path="/signup" element={<SignupPage />} />
  </Route>

  <Route path="*" element={<NotFoundPage />} />
</Routes>
```

실무 장점:

- URL 구조를 바꾸지 않고 Layout만 그룹화
- Header / Footer 적용 범위 명확화
- Auth Page와 Main Page UI 분리
- Route 파일 가독성 향상
- Page Group 관리 쉬움

주의:

- pathless layout에도 Outlet 필요
- 자식 Route path는 명확하게 작성
- Layout 중첩이 과하면 구조 파악 어려움
- NotFound Route를 어느 Layout에 포함할지 기준 필요

---

### [FAQ]

Q. Pathless Layout Route는 뭐야?
A. path 없이 element만 가진 Route로, URL을 추가하지 않고 자식 Route를 공통 Layout으로 감싼다.

Q. path 없는 Route가 왜 필요해?
A. 여러 URL을 같은 Layout으로 묶되 URL 경로 자체는 바꾸고 싶지 않을 때 필요하다.

Q. Pathless Layout에도 Outlet이 필요해?
A. 필요하다. 자식 Route를 표시하려면 Layout Component 안에 Outlet이 있어야 한다.

Q. 404 페이지도 Layout 안에 넣어?
A. 프로젝트 기준에 따라 다르다. 서비스 Header를 보여줄지 독립 404 화면으로 둘지 결정해야 한다.

---

# 5. Page Route Structure

## 5.1 Page Component and Layout Component

### [개념]

Page Component는 Route에 직접 연결되는 화면 단위 Component다.

Layout Component는 여러 Page가 공유하는 공통 UI 구조를 담당하는 Component다.

역할을 분리하면 Routing 구조와 화면 구조를 더 명확하게 관리할 수 있다.

---

### [핵심]

- Page Component
- Layout Component
- Route Element
- Screen Unit
- Shared UI
- Page Logic
- Layout Responsibility
- Component Responsibility
- Container / Presentational Awareness

구분:

```text
Page Component
→ Route에 연결되는 화면 단위
→ 데이터 로딩 / 화면 조합 담당 가능

Layout Component
→ 공통 Header / Footer / Sidebar 구조
→ Outlet 제공
→ Page별 상세 내용은 자식 Route에 위임
```

---

### [실무]

예:

```text
pages
├ MainPage.jsx
├ LoginPage.jsx
├ FestivalListPage.jsx
├ FestivalDetailPage.jsx
├ MyPageHome.jsx
└ NotFoundPage.jsx

layouts
├ MainLayout.jsx
├ AuthLayout.jsx
├ MyPageLayout.jsx
└ AdminLayout.jsx
```

권장 기준:

- Page Component는 pages 폴더
- Layout Component는 layouts 폴더
- Route 정의는 routes 폴더
- 공통 UI는 components 폴더
- Page 이름은 URL 또는 화면 목적과 연결
- Layout 이름은 적용 범위를 드러내게 작성
- Page Component에 Header / Footer 중복 작성 금지
- Layout Component에 모든 페이지 로직 집중 금지

---

### [FAQ]

Q. Page Component는 뭐야?
A. Route에 직접 연결되는 화면 단위 Component다.

Q. Layout Component는 뭐야?
A. 여러 Page가 공유하는 Header, Footer, Sidebar 같은 공통 UI 구조를 담당하는 Component다.

Q. Page와 Layout을 왜 분리해?
A. 공통 UI 중복을 줄이고 Route 구조와 화면 책임을 명확하게 나누기 위해서다.

Q. Header는 Page마다 넣어야 해?
A. 보통 MainLayout 같은 Layout Component에 넣어 중복을 줄인다.

---

## 5.2 Route File Structure

### [개념]

Route File Structure는 Route 정의, Page Component, Layout Component, Route Constants, Protected Route를 역할별로 배치하는 구조다.

Routing 관련 파일을 분리하면 Frontend Agent와 Review Agent가 Route 구조를 쉽게 검토할 수 있다.

---

### [핵심]

- routes
- pages
- layouts
- components
- route constants
- AppRoutes
- ProtectedRoute
- NotFoundPage
- Feature Route Grouping
- File Responsibility

기본 구조:

```text
src
├ routes
│ ├ AppRoutes.jsx
│ ├ ProtectedRoute.jsx
│ └ routePaths.js
├ layouts
│ ├ MainLayout.jsx
│ ├ AuthLayout.jsx
│ ├ MyPageLayout.jsx
│ └ AdminLayout.jsx
├ pages
│ ├ MainPage.jsx
│ ├ LoginPage.jsx
│ ├ SignupPage.jsx
│ ├ FestivalListPage.jsx
│ ├ FestivalDetailPage.jsx
│ ├ MyPageHome.jsx
│ └ NotFoundPage.jsx
└ components
```

---

### [실무]

AppRoutes 예:

```jsx
import { Routes, Route } from "react-router";
import MainLayout from "../layouts/MainLayout";
import AuthLayout from "../layouts/AuthLayout";
import MainPage from "../pages/MainPage";
import LoginPage from "../pages/LoginPage";
import SignupPage from "../pages/SignupPage";
import FestivalListPage from "../pages/FestivalListPage";
import FestivalDetailPage from "../pages/FestivalDetailPage";
import NotFoundPage from "../pages/NotFoundPage";

function AppRoutes() {
  return (
    <Routes>
      <Route element={<MainLayout />}>
        <Route path="/" element={<MainPage />} />
        <Route path="/festivals" element={<FestivalListPage />} />
        <Route path="/festivals/:festivalId" element={<FestivalDetailPage />} />
      </Route>

      <Route element={<AuthLayout />}>
        <Route path="/login" element={<LoginPage />} />
        <Route path="/signup" element={<SignupPage />} />
      </Route>

      <Route path="*" element={<NotFoundPage />} />
    </Routes>
  );
}

export default AppRoutes;
```

실무 기준:

- Route 정의는 AppRoutes로 분리
- Route path 상수는 routePaths.js / routePaths.ts로 분리 가능
- Page Component는 pages 폴더
- Layout Component는 layouts 폴더
- ProtectedRoute는 routes 또는 auth feature에 배치
- 작은 프로젝트는 과도한 폴더 분리 금지
- Feature 단위 구조를 쓰는 경우에도 Route 책임은 명확히 유지

---

### [FAQ]

Q. Route 정의 파일은 어디에 두는 게 좋아?
A. 보통 routes 폴더에 AppRoutes.jsx 또는 AppRoutes.tsx로 분리한다.

Q. Page Component는 어디에 둬?
A. 화면 단위 Component는 pages 폴더에 두는 방식이 일반적이다.

Q. Layout Component는 어디에 둬?
A. 공통 화면 구조를 담당하므로 layouts 폴더에 두는 방식이 명확하다.

Q. 작은 프로젝트도 routes, pages, layouts를 다 나눠야 해?
A. 필수는 아니다. 다만 Route가 많아지면 역할별 분리가 유지보수에 유리하다.

---

# 6. MyPage Layout Example

## 6.1 MyPage Nested Layout

### [개념]

MyPage Layout은 마이페이지 공통 Sidebar와 하위 Page를 Nested Route로 구성하는 대표적인 Layout Route 예시다.

사용자 정보, 프로필, 찜 목록, 작성글, 설정 같은 하위 화면을 같은 Layout 안에서 전환할 수 있다.

---

### [핵심]

- MyPage Layout
- Sidebar
- Nested Route
- Outlet
- Index Route
- Profile Page
- Favorites Page
- Settings Page
- Relative Path
- NavLink Menu

Route 구조:

```text
/mypage
├ index
├ profile
├ favorites
└ settings
```

---

### [실무]

Route 예:

```jsx
<Route path="/mypage" element={<MyPageLayout />}>
  <Route index element={<MyPageHome />} />
  <Route path="profile" element={<ProfilePage />} />
  <Route path="favorites" element={<FavoritePage />} />
  <Route path="settings" element={<SettingsPage />} />
</Route>
```

Layout 예:

```jsx
import { NavLink, Outlet } from "react-router";

function MyPageLayout() {
  return (
    <main className="mypage-layout">
      <aside>
        <nav>
          <NavLink to="/mypage">Home</NavLink>
          <NavLink to="/mypage/profile">Profile</NavLink>
          <NavLink to="/mypage/favorites">Favorites</NavLink>
          <NavLink to="/mypage/settings">Settings</NavLink>
        </nav>
      </aside>

      <section>
        <Outlet />
      </section>
    </main>
  );
}
```

실무 기준:

- `/mypage` 기본 화면은 index route 사용
- Sidebar menu는 NavLink 사용 가능
- Outlet은 content 영역에 배치
- 인증 필요 시 MyPage Route 전체를 Protected Route로 감싸기
- 하위 Page는 각자 데이터 로딩 담당
- 사용자 공통 정보는 Layout에서 조회하거나 전역 상태 사용 가능

---

### [FAQ]

Q. 마이페이지처럼 Sidebar가 있는 화면은 어떻게 구성해?
A. MyPageLayout을 부모 Route로 두고 Sidebar와 Outlet을 배치한 뒤 하위 Page를 Nested Route로 구성한다.

Q. `/mypage` 기본 화면은 어떻게 보여줘?
A. 자식 Route로 `<Route index element={<MyPageHome />} />`를 추가한다.

Q. MyPage 하위 메뉴는 Link와 NavLink 중 뭐가 좋아?
A. 현재 선택된 메뉴 표시가 필요하므로 NavLink가 적합하다.

Q. MyPage 전체를 로그인 사용자만 접근하게 하려면?
A. MyPage Route 또는 MyPageLayout을 Protected Route로 감싸는 방식을 사용한다.

---

# 7. Admin Layout Example

## 7.1 Admin Nested Layout

### [개념]

Admin Layout은 관리자 화면의 공통 Header, Sidebar, Content 영역을 Nested Route로 구성하는 구조다.

관리자 Dashboard, 회원 관리, 축제 관리, 신고 관리 같은 하위 Page를 같은 Layout 안에서 전환할 수 있다.

---

### [핵심]

- Admin Layout
- Admin Dashboard
- Admin Sidebar
- Role Based Route
- Nested Route
- Outlet
- Admin Page Group
- Relative Path
- ROLE_ADMIN
- Forbidden Page

Route 구조:

```text
/admin
├ index
├ users
├ festivals
└ reports
```

---

### [실무]

Route 예:

```jsx
<Route path="/admin" element={<AdminLayout />}>
  <Route index element={<AdminDashboardPage />} />
  <Route path="users" element={<AdminUserPage />} />
  <Route path="festivals" element={<AdminFestivalPage />} />
  <Route path="reports" element={<AdminReportPage />} />
</Route>
```

권한 Route와 결합 예:

```jsx
<Route
  path="/admin"
  element={
    <RoleRoute role={user.role} allowedRoles={["ROLE_ADMIN"]}>
      <AdminLayout />
    </RoleRoute>
  }
>
  <Route index element={<AdminDashboardPage />} />
  <Route path="users" element={<AdminUserPage />} />
  <Route path="festivals" element={<AdminFestivalPage />} />
</Route>
```

Layout 예:

```jsx
import { Outlet } from "react-router";

function AdminLayout() {
  return (
    <div className="admin-layout">
      <AdminSidebar />
      <main>
        <Outlet />
      </main>
    </div>
  );
}
```

실무 기준:

- Admin Layout은 관리자 공통 UI 담당
- Admin 하위 Page는 기능별로 분리
- Frontend RoleRoute는 UX용
- 실제 관리자 API는 Backend에서 ROLE_ADMIN 검증 필수
- `/admin` 기본 화면은 index route 사용
- 권한 없음은 `/forbidden` 또는 프로젝트 기준 redirect
- 관리자 Route와 일반 User Route를 명확히 분리

---

### [FAQ]

Q. Admin 페이지는 Nested Route로 만드는 게 좋아?
A. Sidebar와 여러 하위 관리 화면이 있으면 Nested Route와 AdminLayout이 적합하다.

Q. AdminLayout에 권한 체크를 넣으면 보안이 돼?
A. 아니다. Frontend 권한 체크는 UX용이고 실제 API 보안은 Backend에서 검증해야 한다.

Q. `/admin` 기본 화면은 어떻게 만들지?
A. index route로 AdminDashboardPage를 렌더링한다.

Q. 관리자 하위 Route path는 어떻게 작성해?
A. `/admin` 부모 아래에서 `users`, `festivals`, `reports`처럼 상대 경로로 작성한다.

---

# 8. Detail Tab Layout Example

## 8.1 Detail Page Nested Tab Route

### [개념]

Detail Tab Layout은 상세 페이지 안에서 개요, 리뷰, 지도, 문의 같은 탭 화면을 Nested Route로 구성하는 방식이다.

상세 리소스 ID는 부모 Route의 Path Parameter로 받고, 하위 탭은 자식 Route로 관리한다.

---

### [핵심]

- Detail Layout
- Tab Route
- Nested Route
- Outlet
- Dynamic Route
- Path Parameter
- useParams
- NavLink Tab
- Index Route
- Detail Child Page

Route 구조:

```text
/festivals/:festivalId
├ index
├ reviews
├ map
└ photos
```

---

### [실무]

Route 예:

```jsx
<Route path="/festivals/:festivalId" element={<FestivalDetailLayout />}>
  <Route index element={<FestivalOverviewPage />} />
  <Route path="reviews" element={<FestivalReviewPage />} />
  <Route path="map" element={<FestivalMapPage />} />
  <Route path="photos" element={<FestivalPhotoPage />} />
</Route>
```

Layout 예:

```jsx
import { NavLink, Outlet, useParams } from "react-router";

function FestivalDetailLayout() {
  const { festivalId } = useParams();

  return (
    <main>
      <FestivalDetailHeader festivalId={festivalId} />

      <nav>
        <NavLink to={`/festivals/${festivalId}`}>Overview</NavLink>
        <NavLink to={`/festivals/${festivalId}/reviews`}>Reviews</NavLink>
        <NavLink to={`/festivals/${festivalId}/map`}>Map</NavLink>
        <NavLink to={`/festivals/${festivalId}/photos`}>Photos</NavLink>
      </nav>

      <Outlet />
    </main>
  );
}
```

실무 기준:

- 부모 Route에서 `:festivalId`를 받음
- 하위 탭 Route는 상대 path로 정의
- 탭 메뉴는 NavLink 사용 가능
- index route는 기본 탭으로 사용
- festivalId 검증 필요
- Layout에서 공통 상세 Header를 제공 가능
- 하위 Page에서 같은 param을 useParams로 다시 읽을 수 있음
- 상세 데이터 중복 요청을 줄이려면 상위 Layout 또는 공통 Hook 설계 검토

---

### [FAQ]

Q. 상세 페이지 탭은 Nested Route로 만들 수 있어?
A. 가능하다. `/festivals/:festivalId` 부모 Route 아래에 reviews, map 같은 자식 Route를 둔다.

Q. Detail Layout에서도 useParams를 쓸 수 있어?
A. 가능하다. 부모 Dynamic Route의 param을 Layout과 자식 Page에서 읽을 수 있다.

Q. 상세 기본 탭은 어떻게 만들지?
A. index route를 사용해 OverviewPage 같은 기본 탭을 렌더링한다.

Q. 탭 메뉴는 Link와 NavLink 중 뭐가 좋아?
A. 현재 선택된 탭 표시가 필요하므로 NavLink가 적합하다.

---

# 9. Nested Layout Troubleshooting

## 9.1 Blank Page After Nested Routing

### [개념]

Blank Page After Nested Routing은 Nested Route 이동 후 URL은 바뀌었지만 화면이 비어 있거나 자식 화면이 보이지 않는 문제다.

대부분 Outlet 누락, path 불일치, Component import 오류, Router 구조 오류에서 발생한다.

---

### [핵심]

문제:

- URL은 바뀌지만 화면이 비어 있음
- Layout만 보이고 자식 Page가 안 보임
- Sidebar는 보이는데 content가 없음
- Nested Route 하위 화면이 NotFoundPage로 이동
- 탭 클릭 후 아무 변화 없음

원인:

- 부모 Layout에 Outlet 없음
- 자식 Route path 오타
- Link / NavLink to 오타
- 자식 path에 slash 혼동
- index route 누락
- Component import 오류
- 부모 Route와 자식 Route 구조가 분리됨
- BrowserRouter 누락
- NotFound Route가 잘못 매칭됨

---

### [실무]

Debug Flow:

```text
Nested Route Problem
→ Current URL 확인
→ Parent Route path 확인
→ Child Route path 확인
→ Link / NavLink to 확인
→ Parent Layout Outlet 확인
→ Index Route 확인
→ Component import 확인
→ Console Error 확인
→ NotFound Route 매칭 확인
```

대표 문제:

```text
문제: /mypage/profile에서 ProfilePage가 안 보임
원인: MyPageLayout에 Outlet 없음
해결: MyPageLayout content 영역에 <Outlet /> 추가
```

대표 문제:

```text
문제: /admin/users가 NotFoundPage로 이동
원인: child route path와 Link to 불일치
해결: /admin 부모 아래 path="users" 정의와 /admin/users 이동 경로 확인
```

---

### [FAQ]

Q. Nested Route에서 빈 화면이 나와?
A. Outlet 누락, path 불일치, Component import 오류를 우선 확인한다.

Q. Layout만 보이고 자식 Page가 안 보여?
A. 부모 Layout에 Outlet이 있는지 확인해야 한다.

Q. 탭 클릭 후 URL은 바뀌는데 내용이 안 바뀌어?
A. Detail Layout에 Outlet이 있는지, 탭 Route path가 맞는지 확인한다.

Q. Nested Route 문제는 어떤 순서로 봐?
A. URL, 부모 Route, 자식 Route, Link to, Outlet, Component import, Console Error 순서로 확인한다.

---

## 9.2 Route Structure Collision

### [개념]

Route Structure Collision은 Route 구조가 중복되거나 충돌해 의도하지 않은 Page가 렌더링되는 문제다.

Flat Route와 Nested Route를 혼용하거나 유사한 path를 중복 정의할 때 발생할 수 있다.

---

### [핵심]

문제:

- 같은 URL을 여러 Route에서 정의
- Parent Route와 Flat Route 중복
- `/mypage/profile`이 두 곳에 정의됨
- Layout 적용이 예상과 다름
- NotFound Route가 의도보다 먼저 매칭되는 것처럼 보임
- Admin Route와 User Route 구조 혼선

원인:

- Route 정의 위치 분산
- path 상수 미사용
- Layout Route와 Page Route 역할 혼동
- 절대 경로와 상대 경로 혼용
- Route 파일이 너무 커져 구조 파악 어려움

---

### [실무]

나쁜 구조 예:

```jsx
<Route path="/mypage" element={<MyPageLayout />}>
  <Route path="profile" element={<ProfilePage />} />
</Route>

<Route path="/mypage/profile" element={<ProfilePage />} />
```

문제:

```text
동일 화면 Route가 중복 정의되어 Layout 적용 기준이 불명확해짐
```

권장:

```jsx
<Route path="/mypage" element={<MyPageLayout />}>
  <Route index element={<MyPageHome />} />
  <Route path="profile" element={<ProfilePage />} />
</Route>
```

검수 기준:

- 동일 path 중복 정의 제거
- Layout 적용 대상 명확화
- Route Constants 사용 검토
- Feature별 Route grouping 기준 명확화
- Flat Route와 Nested Route 혼용 최소화
- AppRoutes에서 전체 구조 검토 가능하게 유지

---

### [FAQ]

Q. 같은 path를 여러 Route에 정의해도 돼?
A. 권장하지 않는다. Layout 적용과 Route 관리가 혼란스러워질 수 있다.

Q. Flat Route와 Nested Route를 섞어도 돼?
A. 가능하지만 같은 화면을 중복 정의하지 않고 Layout 적용 기준을 명확히 해야 한다.

Q. Route 구조 충돌은 어떻게 찾을 수 있어?
A. AppRoutes 전체에서 동일 path, 유사 path, Layout 적용 범위를 확인한다.

Q. Route path 상수는 구조 충돌 방지에 도움이 돼?
A. 도움이 된다. path 오타와 중복을 줄일 수 있다.

---

# 10. Nested Layout Checklist

## 10.1 Part04 Checklist

### [개념]

Nested Layout Route 문서는 Route 계층 구조, Layout 책임, Outlet 적용 여부를 검수하기 위한 체크리스트를 포함한다.

---

### [핵심]

Checklist:

```md
- [ ] Nested Route 개념이 설명되었는가?
- [ ] Parent Route와 Child Route 관계가 포함되었는가?
- [ ] Relative Path 규칙이 포함되었는가?
- [ ] 자식 Route path slash 주의가 포함되었는가?
- [ ] Outlet 개념이 설명되었는가?
- [ ] Outlet Missing Problem이 포함되었는가?
- [ ] Layout Route 개념이 설명되었는가?
- [ ] Pathless Layout Route가 포함되었는가?
- [ ] Page Component와 Layout Component 책임이 구분되었는가?
- [ ] Route File Structure가 포함되었는가?
- [ ] MyPage Layout 예제가 포함되었는가?
- [ ] Admin Layout 예제가 포함되었는가?
- [ ] Detail Tab Layout 예제가 포함되었는가?
- [ ] Nested Route Troubleshooting이 포함되었는가?
- [ ] Route Structure Collision 주의가 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 Flow:

```text
Draft
→ Nested Route Check
→ Relative Path Check
→ Outlet Check
→ Layout Route Check
→ Pathless Layout Check
→ Page / Layout Responsibility Check
→ Route File Structure Check
→ Example Route Check
→ Troubleshooting Check
→ FAQ Check
→ Retrieval Queries Check
→ Final Review
```

---

### [FAQ]

Q. Part04 검수에서 가장 중요한 것은?
A. Nested Route 구조, Outlet 존재 여부, Layout 책임 분리, Relative Path 규칙이다.

Q. Part04에서 Protected Route를 깊게 다뤄?
A. 아니다. MyPage / Admin Layout에서 연결 가능성만 언급하고 Protected Route 심화는 별도 Part에서 다룬다.

Q. Part04에서 SPA Fallback을 다뤄?
A. 아니다. 배포 fallback 문제는 Deployment / Troubleshooting Part에서 깊게 다룬다.

---

# 11. Nested Layout Common Mistakes

## 11.1 Common Mistakes

### [개념]

Nested Layout Route에서 자주 발생하는 실수는 Outlet 누락, 자식 path slash 혼동, Layout과 Page 책임 혼합, Route 중복 정의다.

---

### [핵심]

자주 발생:

- 부모 Layout에 Outlet 누락
- 자식 Route path에 slash를 잘못 붙임
- index route에 path 사용
- Layout Route에 Outlet 없음
- Pathless Layout Route에 Outlet 없음
- Layout Component에 모든 Page 로직 집중
- Page마다 Header / Footer 중복 작성
- 같은 path를 Flat Route와 Nested Route에 중복 정의
- Link / NavLink to와 child route path 불일치
- Dynamic Route 하위 탭에서 param 검증 누락
- MyPage / Admin Route 권한 보호 누락
- Layout 적용 범위 불명확
- Route 파일 구조가 과도하게 복잡
- 작은 프로젝트에 과도한 폴더 분리
- NotFound Route 위치 기준 없음

---

### [실무]

대표 문제 1:

```text
문제: /mypage/profile에서 ProfilePage가 보이지 않음
원인: MyPageLayout에 Outlet 없음
해결: content 영역에 <Outlet /> 추가
```

대표 문제 2:

```text
문제: /admin/users가 예상 Layout 없이 렌더링됨
원인: /admin/users를 Flat Route로 따로 정의함
해결: /admin 부모 Route 아래 path="users"로 정의
```

대표 문제 3:

```text
문제: 상세 탭 메뉴 active가 이상함
원인: NavLink to와 Nested child path 기준 불일치
해결: 실제 URL과 child Route path를 일치시킴
```

대표 문제 4:

```text
문제: /mypage 접속 시 아무 content가 없음
원인: index route 누락
해결: <Route index element={<MyPageHome />} /> 추가
```

Debug Flow:

```text
Nested Layout Problem
→ Current URL 확인
→ AppRoutes 구조 확인
→ Parent Layout 확인
→ Outlet 확인
→ Child path 확인
→ Link / NavLink 확인
→ Index Route 확인
→ 중복 Route 확인
→ Console Error 확인
```

---

### [FAQ]

Q. Nested Layout 문제는 어떻게 찾는 게 좋아?
A. 현재 URL, AppRoutes 구조, 부모 Layout, Outlet, 자식 path, Link to, index route를 순서대로 확인한다.

Q. Layout에 Outlet이 있는데도 자식 화면이 안 나와?
A. 자식 Route가 부모 Route 내부에 정의되어 있는지, path가 맞는지 확인해야 한다.

Q. `/mypage` 접속 시 빈 content가 나와?
A. index route가 없을 수 있다. 기본 화면을 index route로 추가한다.

Q. Route 구조에서 가장 흔한 실수는?
A. Outlet 누락, 자식 path slash 혼동, Link to와 Route path 불일치, Route 중복 정의다.

---

# Retrieval Queries

### [FAQ]

Q. React Router Part04는 뭘 다뤄?
A. Nested Route, Outlet, Layout Route, Pathless Layout Route, Page Route Structure, Route File Structure를 다룬다.

Q. Nested Route는 뭐야?
A. 부모 Route 안에 자식 Route를 구성해 공통 Layout 안에서 하위 화면을 렌더링하는 방식이다.

Q. Nested Route는 언제 써?
A. 공통 Layout 안에서 하위 화면이 바뀌는 구조가 필요할 때 사용한다.

Q. Parent Route는 뭐야?
A. 자식 Route를 포함하고 공통 Layout 또는 상위 화면 구조를 담당하는 Route다.

Q. Child Route는 뭐야?
A. Parent Route 아래에서 Outlet 위치에 렌더링되는 하위 Route다.

Q. Nested Route 화면이 안 나와?
A. 부모 Component에 `<Outlet />`이 없을 가능성이 크다.

Q. 자식 Route path에 slash를 붙여야 해?
A. 상대 경로로 쓰려면 보통 slash 없이 작성한다. 절대 경로가 필요한 경우 의도를 명확히 해야 한다.

Q. 부모 path가 `/mypage`이고 자식 path가 `profile`이면 URL은 뭐야?
A. `/mypage/profile`이다.

Q. index route에도 path를 써?
A. 아니다. index route는 path 없이 `index` 속성을 사용한다.

Q. Outlet은 뭐야?
A. 부모 Route Component 안에서 자식 Route Component가 표시될 위치를 지정하는 Component다.

Q. Outlet은 왜 필요해?
A. Nested Route의 자식 Component가 부모 Layout 안에서 렌더링될 위치를 지정하기 위해 필요하다.

Q. Outlet이 없으면 어떻게 돼?
A. 부모 Layout은 보일 수 있지만 자식 Route 화면이 렌더링되지 않는다.

Q. Outlet은 어디에 둬?
A. 자식 Page가 표시되어야 하는 위치에 둔다. 예: Sidebar 옆 content 영역.

Q. Outlet을 여러 개 둘 수 있어?
A. 일반적인 Nested Route에서는 하나의 Outlet로 자식 Route 렌더링 위치를 지정한다. 여러 영역이 필요하면 Layout 구조를 다시 설계한다.

Q. Layout Route는 뭐야?
A. 공통 UI를 제공하고 자식 Route를 Outlet에 렌더링하는 Route다.

Q. Layout Route는 왜 써?
A. 여러 페이지에서 공통 Header, Footer, Sidebar 구조를 중복 작성하지 않기 위해 사용한다.

Q. Layout Route에 path가 없어도 돼?
A. 가능하다. path 없는 Layout Route는 자식 Route를 공통 Layout으로 감싸는 데 사용할 수 있다.

Q. Pathless Layout Route는 뭐야?
A. path 없이 element만 가진 Route로, URL을 추가하지 않고 자식 Route를 공통 Layout으로 감싼다.

Q. path 없는 Route가 왜 필요해?
A. 여러 URL을 같은 Layout으로 묶되 URL 경로 자체는 바꾸고 싶지 않을 때 필요하다.

Q. Pathless Layout에도 Outlet이 필요해?
A. 필요하다. 자식 Route를 표시하려면 Layout Component 안에 Outlet이 있어야 한다.

Q. MainLayout은 뭐야?
A. 일반 서비스 Page에서 공통 Header, Footer, Main 영역을 제공하는 Layout Component다.

Q. AuthLayout은 뭐야?
A. 로그인, 회원가입 같은 인증 Page에 적용하는 전용 Layout Component다.

Q. AdminLayout은 뭐야?
A. 관리자 화면의 Sidebar, Header, Content 영역을 제공하는 Layout Component다.

Q. MyPageLayout은 뭐야?
A. 마이페이지의 Sidebar와 하위 Page content 영역을 제공하는 Layout Component다.

Q. Detail Tab Layout은 뭐야?
A. 상세 페이지 안에서 개요, 리뷰, 지도 같은 탭 화면을 Nested Route로 구성하는 Layout이다.

Q. Page Component는 뭐야?
A. Route에 직접 연결되는 화면 단위 Component다.

Q. Layout Component는 뭐야?
A. 여러 Page가 공유하는 Header, Footer, Sidebar 같은 공통 UI 구조를 담당하는 Component다.

Q. Page와 Layout을 왜 분리해?
A. 공통 UI 중복을 줄이고 Route 구조와 화면 책임을 명확하게 나누기 위해서다.

Q. Header는 Page마다 넣어야 해?
A. 보통 MainLayout 같은 Layout Component에 넣어 중복을 줄인다.

Q. Route 정의 파일은 어디에 두는 게 좋아?
A. 보통 routes 폴더에 AppRoutes.jsx 또는 AppRoutes.tsx로 분리한다.

Q. Page Component는 어디에 둬?
A. 화면 단위 Component는 pages 폴더에 두는 방식이 일반적이다.

Q. Layout Component는 어디에 둬?
A. 공통 화면 구조를 담당하므로 layouts 폴더에 두는 방식이 명확하다.

Q. 작은 프로젝트도 routes, pages, layouts를 다 나눠야 해?
A. 필수는 아니다. 다만 Route가 많아지면 역할별 분리가 유지보수에 유리하다.

Q. 마이페이지처럼 Sidebar가 있는 화면은 어떻게 구성해?
A. MyPageLayout을 부모 Route로 두고 Sidebar와 Outlet을 배치한 뒤 하위 Page를 Nested Route로 구성한다.

Q. `/mypage` 기본 화면은 어떻게 보여줘?
A. 자식 Route로 `<Route index element={<MyPageHome />} />`를 추가한다.

Q. MyPage 하위 메뉴는 Link와 NavLink 중 뭐가 좋아?
A. 현재 선택된 메뉴 표시가 필요하므로 NavLink가 적합하다.

Q. MyPage 전체를 로그인 사용자만 접근하게 하려면?
A. MyPage Route 또는 MyPageLayout을 Protected Route로 감싸는 방식을 사용한다.

Q. Admin 페이지는 Nested Route로 만드는 게 좋아?
A. Sidebar와 여러 하위 관리 화면이 있으면 Nested Route와 AdminLayout이 적합하다.

Q. AdminLayout에 권한 체크를 넣으면 보안이 돼?
A. 아니다. Frontend 권한 체크는 UX용이고 실제 API 보안은 Backend에서 검증해야 한다.

Q. `/admin` 기본 화면은 어떻게 만들지?
A. index route로 AdminDashboardPage를 렌더링한다.

Q. 관리자 하위 Route path는 어떻게 작성해?
A. `/admin` 부모 아래에서 `users`, `festivals`, `reports`처럼 상대 경로로 작성한다.

Q. 상세 페이지 탭은 Nested Route로 만들 수 있어?
A. 가능하다. `/festivals/:festivalId` 부모 Route 아래에 reviews, map 같은 자식 Route를 둔다.

Q. Detail Layout에서도 useParams를 쓸 수 있어?
A. 가능하다. 부모 Dynamic Route의 param을 Layout과 자식 Page에서 읽을 수 있다.

Q. 상세 기본 탭은 어떻게 만들지?
A. index route를 사용해 OverviewPage 같은 기본 탭을 렌더링한다.

Q. 탭 메뉴는 Link와 NavLink 중 뭐가 좋아?
A. 현재 선택된 탭 표시가 필요하므로 NavLink가 적합하다.

Q. Nested Route에서 빈 화면이 나와?
A. Outlet 누락, path 불일치, Component import 오류를 우선 확인한다.

Q. Layout만 보이고 자식 Page가 안 보여?
A. 부모 Layout에 Outlet이 있는지 확인해야 한다.

Q. 탭 클릭 후 URL은 바뀌는데 내용이 안 바뀌어?
A. Detail Layout에 Outlet이 있는지, 탭 Route path가 맞는지 확인한다.

Q. 같은 path를 여러 Route에 정의해도 돼?
A. 권장하지 않는다. Layout 적용과 Route 관리가 혼란스러워질 수 있다.

Q. Flat Route와 Nested Route를 섞어도 돼?
A. 가능하지만 같은 화면을 중복 정의하지 않고 Layout 적용 기준을 명확히 해야 한다.

Q. Route 구조 충돌은 어떻게 찾을 수 있어?
A. AppRoutes 전체에서 동일 path, 유사 path, Layout 적용 범위를 확인한다.

Q. Nested Layout 문제는 어떻게 찾는 게 좋아?
A. 현재 URL, AppRoutes 구조, 부모 Layout, Outlet, 자식 path, Link to, index route를 순서대로 확인한다.

Q. Layout에 Outlet이 있는데도 자식 화면이 안 나와?
A. 자식 Route가 부모 Route 내부에 정의되어 있는지, path가 맞는지 확인해야 한다.

Q. `/mypage` 접속 시 빈 content가 나와?
A. index route가 없을 수 있다. 기본 화면을 index route로 추가한다.

Q. Route 구조에서 가장 흔한 실수는?
A. Outlet 누락, 자식 path slash 혼동, Link to와 Route path 불일치, Route 중복 정의다.

Q. Part04 다음에는 뭘 다뤄?
A. Part05 Protected Route Auth에서 Protected Route, Role Based Route, Auth Redirect, Frontend Route Guard를 다룬다.
