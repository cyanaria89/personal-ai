# Authentication Frontend Flow Part06 - Protected Route / PublicOnlyRoute / Role Based Route / Role Based UI

---

# 1. Route Guard Overview

## 1.1 Frontend Route Guard Purpose

### [개념]

Route Guard는 Frontend에서 사용자의 인증 상태와 권한 상태에 따라 특정 화면 접근을 제어하는 UX 장치다.

Protected Route는 로그인하지 않은 사용자를 login 페이지로 redirect한다.

PublicOnlyRoute는 이미 로그인한 사용자가 login, signup 같은 인증 전용 페이지에 접근하지 못하게 한다.

Role Based Route는 사용자 role에 따라 접근 가능한 화면을 제한한다.

Route Guard는 보안의 최종 기준이 아니다.

실제 API 접근 제어와 권한 검증은 Backend Authorization이 수행해야 한다.

---

### [핵심]

핵심 키워드:

- Route Guard
- Protected Route
- Private Route
- PublicOnlyRoute
- Role Based Route
- Role Based UI
- authenticated
- initialized
- auth loading
- user
- role
- ROLE_USER
- ROLE_ADMIN
- Navigate
- Outlet
- redirect
- previous location
- forbidden page
- Backend Authorization
- Frontend UX Guard

Route Guard 종류:

```text
Protected Route
→ 비로그인 사용자 접근 차단
→ login redirect
```

```text
PublicOnlyRoute
→ 로그인 사용자 login / signup 접근 차단
→ main redirect
```

```text
Role Based Route
→ role 기준 접근 제한
→ forbidden page redirect
```

---

### [실무]

기본 Route Guard 흐름:

```text
Route Access
→ Check initialized
→ If not initialized: show loading
→ Check authenticated
→ If not authenticated: redirect login
→ Check role if needed
→ If role not allowed: redirect forbidden
→ Render Page
```

주의:

- initialized 전 redirect 금지
- auth loading 중 login redirect 금지
- Protected Route는 UX용
- Backend API 권한 검증 필수
- Role Based Route는 Backend Authorization을 대체하지 않음
- redirect loop 방지
- 이전 location 저장 가능
- role naming 통일
- 권한 없음은 403 처리와 연결

---

### [FAQ]

Q. Protected Route는 보안적으로 충분해?
A. 아니다. Frontend Route 보호는 UX용이고 실제 보안은 Backend 인증/인가가 담당해야 한다.

Q. Route Guard에서 가장 중요한 상태는 뭐야?
A. initialized, authenticated, user, role 상태를 구분하는 것이 중요하다.

Q. Frontend에서 페이지 접근을 막으면 API도 안전해져?
A. 아니다. 사용자는 API를 직접 호출할 수 있으므로 Backend에서 반드시 인증/인가를 검증해야 한다.

Q. auth loading 중에는 어떻게 해?
A. 로그인 페이지로 보내지 말고 loading UI를 보여주며 인증 상태 확인이 끝날 때까지 기다리는 것이 좋다.

---

# 2. Protected Route

## 2.1 Protected Route Basics

### [개념]

Protected Route는 로그인하지 않은 사용자가 인증이 필요한 페이지에 접근하면 login 페이지로 redirect하는 Frontend Route Guard다.

예를 들어 `/mypage`, `/favorites`, `/notifications`, `/settings` 같은 화면은 로그인 상태에서만 접근하도록 보호할 수 있다.

---

### [핵심]

필수 요소:

- Protected Route
- Private Route
- authenticated
- initialized
- auth loading
- Navigate
- previous location
- replace
- login redirect
- UX guard
- Backend security

기본 Flow:

```text
User Access Protected Page
→ Check initialized
→ If initialized false: Loading
→ If authenticated false: Navigate login
→ If authenticated true: Render Page
```

---

### [실무]

Component wrapper 예:

```tsx
function ProtectedRoute({ children }: { children: React.ReactNode }) {
  const { initialized, authenticated } = useAuth();
  const location = useLocation();

  if (!initialized) {
    return <p>인증 상태 확인 중...</p>;
  }

  if (!authenticated) {
    return <Navigate to="/login" replace state={{ from: location.pathname }} />;
  }

  return children;
}
```

적용 예:

```tsx
<Route
  path="/mypage"
  element={
    <ProtectedRoute>
      <MyPage />
    </ProtectedRoute>
  }
/>
```

권장:

- initialized 전 redirect 금지
- replace 옵션 사용으로 history 정리
- 이전 location을 login으로 전달
- 로그인 성공 후 원래 페이지로 이동 가능
- 인증 필요 API는 authApi 사용
- Backend Security와 함께 적용

주의:

- Protected Route만으로 API 보안 불가
- authenticated false 판단 전에 auth restore 완료 필요
- login page를 Protected Route로 감싸지 않음
- redirect target이 다시 Protected Route에 걸리는지 확인
- token 존재만으로 authenticated true 처리하지 않음

---

### [FAQ]

Q. Protected Route는 어떻게 만들어?
A. 인증 상태를 확인하고 비로그인 상태면 Navigate로 login 페이지에 redirect한다.

Q. Protected Route에서 initialized를 왜 확인해?
A. 새로고침 인증 복원 중 비로그인으로 오판해 login으로 잘못 보내는 것을 막기 위해서다.

Q. Protected Route로 감싸면 API 호출도 막혀?
A. 아니다. 화면 접근 UX만 막는 것이고 API 접근은 Backend Authorization으로 막아야 한다.

Q. Protected Route에서 이전 페이지를 어떻게 저장해?
A. `Navigate`의 `state={{ from: location.pathname }}` 또는 query string을 사용할 수 있다.

---

## 2.2 Protected Route with Outlet

### [개념]

Protected Route with Outlet은 React Router 중첩 라우팅에서 보호가 필요한 여러 Route를 한 번에 감싸는 방식이다.

여러 private page에 공통 인증 guard를 적용할 때 유용하다.

---

### [핵심]

사용 대상:

- nested routes
- private layout
- mypage routes
- admin routes
- settings routes
- Outlet
- route group
- shared guard

구조:

```text
ProtectedRoute
→ Outlet
→ Child Routes
```

---

### [실무]

Outlet 방식 예:

```tsx
function ProtectedRoute() {
  const { initialized, authenticated } = useAuth();
  const location = useLocation();

  if (!initialized) {
    return <p>인증 상태 확인 중...</p>;
  }

  if (!authenticated) {
    return <Navigate to="/login" replace state={{ from: location.pathname }} />;
  }

  return <Outlet />;
}
```

Route 설정 예:

```tsx
<Route element={<ProtectedRoute />}>
  <Route path="/mypage" element={<MyPage />} />
  <Route path="/favorites" element={<FavoritesPage />} />
  <Route path="/notifications" element={<NotificationPage />} />
</Route>
```

주의:

- Outlet 방식은 Route group 보호에 적합
- children wrapper 방식과 혼용 가능하지만 기준 통일 권장
- layout route와 auth guard 위치 확인
- nested route의 location 저장 기준 확인
- parent route redirect와 child route redirect 충돌 주의

---

### [FAQ]

Q. Protected Route를 모든 페이지마다 감싸야 해?
A. Outlet 기반 중첩 라우팅을 사용하면 여러 보호 페이지를 한 번에 감쌀 수 있다.

Q. children 방식과 Outlet 방식 중 뭐가 좋아?
A. 단일 페이지 보호는 children 방식도 가능하고 여러 route group 보호는 Outlet 방식이 편하다.

Q. nested route에서 redirect가 이상하게 동작해?
A. parent route guard와 child route 설정, location 저장값, index route 설정을 함께 확인해야 한다.

---

## 2.3 Protected Route Redirect After Login

### [개념]

Protected Route Redirect After Login은 보호 페이지 접근 후 login 페이지로 이동한 사용자를 로그인 성공 후 원래 페이지로 돌려보내는 흐름이다.

사용자가 원래 보려던 페이지를 잃지 않게 하는 UX 개선 패턴이다.

---

### [핵심]

Flow:

```text
Protected Page Access
→ Save Current Location
→ Redirect Login
→ Login Success
→ Navigate Saved Location
```

필수 요소:

- location state
- from path
- redirect target validation
- replace navigation
- login success redirect
- redirect loop prevention

---

### [실무]

Protected Route에서 저장:

```tsx
return <Navigate to="/login" replace state={{ from: location.pathname }} />;
```

Login Page에서 사용:

```tsx
const location = useLocation();
const navigate = useNavigate();

const from = getSafeRedirectPath(location.state?.from);

async function handleLogin(values: LoginFormValues) {
  const result = await login(toLoginRequest(values));

  applyLoginResult(result);

  navigate(from, { replace: true });
}
```

Safe Redirect 예:

```tsx
function getSafeRedirectPath(from: unknown) {
  if (typeof from !== "string") {
    return "/";
  }

  if (!from.startsWith("/") || from.startsWith("//")) {
    return "/";
  }

  if (from === "/login" || from === "/signup") {
    return "/";
  }

  return from;
}
```

주의:

- 외부 URL redirect 금지
- login / signup으로 다시 보내는 loop 방지
- OAuth2 callback redirect와 기준 분리 가능
- query string까지 보존할지 정책 결정
- replace 옵션으로 history 정리
- redirect target이 존재하지 않는 route인지 확인

---

### [FAQ]

Q. 로그인 후 원래 보려던 페이지로 돌아가려면?
A. Protected Route에서 location state나 query string에 이전 경로를 저장하고 로그인 성공 후 해당 경로로 navigate한다.

Q. redirect target 검증이 왜 필요해?
A. 외부 URL로 이동하는 open redirect 문제와 login 페이지 반복 이동 같은 redirect loop를 막기 위해 필요하다.

Q. 로그인 후 항상 `/`로 보내도 돼?
A. 가능하지만 보호 페이지 접근 후 로그인한 경우 사용자가 원래 보려던 페이지로 돌아가는 UX가 더 좋을 수 있다.

---

# 3. PublicOnlyRoute

## 3.1 PublicOnlyRoute Basics

### [개념]

PublicOnlyRoute는 이미 로그인한 사용자가 login, signup, find password 같은 인증 전용 페이지에 접근하지 못하도록 처리하는 Route Guard다.

로그인한 사용자가 login 페이지에 다시 접근했을 때 main page 또는 이전 페이지로 redirect하는 UX 정리 용도다.

---

### [핵심]

사용 대상:

- login page
- signup page
- find password page
- password reset request page
- already authenticated redirect
- auth initialized
- redirect loop prevention

기본 Flow:

```text
User Access Login Page
→ Check initialized
→ If initialized false: Loading
→ If authenticated true: Navigate main
→ If authenticated false: Render Login Page
```

---

### [실무]

PublicOnlyRoute 예:

```tsx
function PublicOnlyRoute({ children }: { children: React.ReactNode }) {
  const { initialized, authenticated } = useAuth();

  if (!initialized) {
    return <p>인증 상태 확인 중...</p>;
  }

  if (authenticated) {
    return <Navigate to="/" replace />;
  }

  return children;
}
```

적용 예:

```tsx
<Route
  path="/login"
  element={
    <PublicOnlyRoute>
      <LoginPage />
    </PublicOnlyRoute>
  }
/>

<Route
  path="/signup"
  element={
    <PublicOnlyRoute>
      <SignupPage />
    </PublicOnlyRoute>
  }
/>
```

주의:

- initialized 전 redirect 금지
- login / signup page 보호에 사용
- OAuth2 callback은 예외 처리 필요 가능
- redirect target 기준 명확화
- PublicOnlyRoute와 ProtectedRoute 조건 충돌 방지
- 로그인 상태에서 signup 접근 시 main으로 보낼지 profile setup으로 보낼지 정책 결정

---

### [FAQ]

Q. 로그인한 사용자가 login 페이지에 접근하면 어떻게 해?
A. 보통 메인 페이지나 이전 페이지로 redirect한다.

Q. PublicOnlyRoute도 꼭 필요해?
A. 필수는 아니지만 로그인/회원가입 페이지 UX를 정리하는 데 유용하다.

Q. login page도 Protected Route로 감싸야 해?
A. 아니다. login page는 비로그인 사용자가 접근해야 하므로 Protected Route로 감싸면 redirect loop가 생길 수 있다.

---

## 3.2 PublicOnlyRoute Exceptions

### [개념]

PublicOnlyRoute Exceptions는 인증 전용 페이지처럼 보이지만 로그인 상태에서도 접근이 필요할 수 있는 경로를 예외 처리하는 기준이다.

OAuth2 callback, email verification callback, password reset callback은 일반 login page와 다르게 처리될 수 있다.

---

### [핵심]

예외 후보:

- OAuth2 callback
- social login callback
- email verification callback
- password reset callback
- invitation accept page
- account linking page

예외 이유:

- callback 처리 전 authenticated 상태가 바뀔 수 있음
- token 저장 또는 code exchange가 필요함
- 로그인 상태에서도 계정 연결이 필요할 수 있음
- PublicOnlyRoute redirect가 callback 처리를 막을 수 있음

---

### [실무]

OAuth2 callback은 별도 route로 처리:

```tsx
<Route path="/oauth/callback" element={<OAuthCallbackPage />} />
```

PublicOnlyRoute 적용 대상 분리:

```tsx
<Route
  path="/login"
  element={
    <PublicOnlyRoute>
      <LoginPage />
    </PublicOnlyRoute>
  }
/>

<Route path="/oauth/callback" element={<OAuthCallbackPage />} />
```

주의:

- OAuth2 callback을 PublicOnlyRoute로 감싸면 처리 전에 redirect될 수 있음
- email verification은 로그인 상태에서도 접근 가능할 수 있음
- password reset token page는 인증 상태와 별개로 접근 필요 가능
- 예외 route는 보안 정책을 Backend와 맞춤
- callback 처리 후 최종 redirect를 명확히 설정

---

### [FAQ]

Q. OAuth2 callback도 PublicOnlyRoute로 감싸도 돼?
A. 주의해야 한다. callback 처리 전에 authenticated 상태가 바뀌거나 redirect가 발생하면 OAuth2 처리가 중단될 수 있다.

Q. 이메일 인증 callback은 로그인 사용자만 접근해야 해?
A. 프로젝트 정책에 따라 다르다. 이메일 인증 링크는 비로그인 상태에서도 접근 가능하게 설계하는 경우가 많다.

Q. password reset page는 PublicOnlyRoute로 감싸?
A. 로그인 사용자의 접근을 막을 수는 있지만 reset token 처리 흐름과 충돌하지 않는지 확인해야 한다.

---

# 4. Role Based Route

## 4.1 Role Based Route Basics

### [개념]

Role Based Route는 사용자 role에 따라 접근 가능한 Route를 제한하는 Frontend Route Guard다.

예를 들어 `ROLE_ADMIN` 사용자만 `/admin` 페이지에 접근하게 하고, 일반 사용자는 forbidden page로 이동시킬 수 있다.

Role Based Route는 UX용 접근 제어이며 Backend API 권한 검증을 대체하지 않는다.

---

### [핵심]

필수 요소:

- Role Based Route
- allowedRoles
- user.role
- ROLE_USER
- ROLE_ADMIN
- authenticated
- initialized
- forbidden page
- Navigate
- Backend Authorization
- role naming

기본 Flow:

```text
Route Access
→ Check initialized
→ Check authenticated
→ Check user.role
→ If allowed: render page
→ If not allowed: redirect forbidden
```

---

### [실무]

RoleRoute 예:

```tsx
type RoleRouteProps = {
  allowedRoles: Array<"ROLE_USER" | "ROLE_ADMIN">;
  children: React.ReactNode;
};

function RoleRoute({ allowedRoles, children }: RoleRouteProps) {
  const { user, initialized, authenticated } = useAuth();

  if (!initialized) {
    return <p>인증 상태 확인 중...</p>;
  }

  if (!authenticated) {
    return <Navigate to="/login" replace />;
  }

  if (!user || !allowedRoles.includes(user.role)) {
    return <Navigate to="/forbidden" replace />;
  }

  return children;
}
```

적용 예:

```tsx
<Route
  path="/admin"
  element={
    <RoleRoute allowedRoles={["ROLE_ADMIN"]}>
      <AdminPage />
    </RoleRoute>
  }
/>
```

주의:

- ROLE_ADMIN / ADMIN naming 혼용 금지
- Frontend role check는 UX용
- Backend API role check 필수
- user role이 없을 때 loading / error 처리
- 권한 없음은 403 UI와 연결 가능
- 관리자 API는 Backend Security에서 ROLE_ADMIN 검증
- role 정보가 오래되었으면 `/me` refetch 고려

---

### [FAQ]

Q. Role Based Route는 어떻게 만들어?
A. user.role이 allowedRoles에 포함되는지 확인하고 권한이 없으면 forbidden page로 redirect한다.

Q. Frontend에서 ROLE_ADMIN을 확인하면 관리자 API가 안전해져?
A. 아니다. Frontend role check는 화면 접근 UX용이고 관리자 API는 Backend에서 반드시 권한 검증해야 한다.

Q. 권한 없는 사용자는 어디로 보내?
A. 프로젝트 기준에 따라 `/forbidden`, `/`, `/login` 중 하나로 보낼 수 있다. 기준을 통일해야 한다.

Q. Role Based Route에서 user가 null이면?
A. 인증 복원 중인지 확인하고 initialized 이후에도 user가 없으면 login 또는 forbidden 처리 기준을 적용한다.

---

## 4.2 Role Based Route with Outlet

### [개념]

Role Based Route with Outlet은 관리자 영역처럼 여러 하위 Route에 동일한 role 조건을 적용할 때 사용하는 구조다.

Admin Layout, User Management, Dashboard, Settings 같은 하위 Route를 한 번에 보호할 수 있다.

---

### [핵심]

사용 대상:

- admin route group
- manager route group
- user-only route group
- role protected layout
- Outlet
- allowedRoles
- nested route

구조:

```text
RoleRoute allowedRoles=["ROLE_ADMIN"]
→ Outlet
→ Admin Child Routes
```

---

### [실무]

Outlet 기반 RoleRoute 예:

```tsx
function AdminRoute() {
  const { initialized, authenticated, user } = useAuth();

  if (!initialized) {
    return <p>인증 상태 확인 중...</p>;
  }

  if (!authenticated) {
    return <Navigate to="/login" replace />;
  }

  if (user?.role !== "ROLE_ADMIN") {
    return <Navigate to="/forbidden" replace />;
  }

  return <Outlet />;
}
```

Route 설정 예:

```tsx
<Route element={<AdminRoute />}>
  <Route path="/admin" element={<AdminDashboard />} />
  <Route path="/admin/users" element={<AdminUserPage />} />
  <Route path="/admin/settings" element={<AdminSettingsPage />} />
</Route>
```

주의:

- admin layout과 role guard 위치 구분
- 하위 route API도 Backend 권한 검증 필요
- forbidden page가 admin route 내부에 있으면 loop 가능
- user role 로딩 전 redirect 금지
- allowedRoles 배열 방식으로 확장 가능
- role route와 protected route 중복 여부 정리

---

### [FAQ]

Q. 관리자 하위 페이지마다 RoleRoute를 감싸야 해?
A. Outlet 기반 RoleRoute를 사용하면 관리자 하위 route를 한 번에 보호할 수 있다.

Q. AdminRoute 안에서 다시 ProtectedRoute를 써야 해?
A. RoleRoute가 authenticated 확인까지 포함하면 별도 ProtectedRoute가 필요 없을 수 있다. 역할을 중복하지 않도록 기준을 정한다.

Q. forbidden page가 계속 반복돼?
A. forbidden route 자체가 RoleRoute 내부에 있거나 redirect target이 다시 같은 guard에 걸릴 수 있다.

---

## 4.3 Owner Based Route Caution

### [개념]

Owner Based Route는 작성자나 소유자만 특정 화면에 접근하도록 제한하는 방식이다.

예를 들어 게시글 수정 페이지는 작성자만 접근해야 한다.

다만 소유자 판단은 Frontend Route Guard만으로 처리하면 안 되고 Backend가 최종 검증해야 한다.

---

### [핵심]

사용 예:

- edit post page
- delete page
- private resource page
- order detail page
- user owned resource
- owner-only action

주의:

- owner check
- Backend authorization
- resource fetch required
- userId comparison
- 403 handling
- loading state
- stale user risk

---

### [실무]

Frontend owner check 예:

```tsx
function PostEditPage({ post }: { post: PostDetail }) {
  const { user } = useAuth();

  if (user?.userId !== post.authorId) {
    return <Navigate to="/forbidden" replace />;
  }

  return <PostEditForm post={post} />;
}
```

Backend 검증 필수 Flow:

```text
User Access Edit Page
→ Frontend fetch post detail
→ Frontend compares userId and authorId for UX
→ User submits edit request
→ Backend verifies owner
→ If not owner: 403 Forbidden
```

주의:

- Frontend owner check는 UX용
- Backend에서 작성자 검증 필수
- resource fetch 전에는 owner 판단 불가
- post.authorId가 없으면 판단 불가
- userId와 authorId 타입 일치 확인
- 권한 없음은 403 처리
- stale user / stale resource 주의

---

### [FAQ]

Q. 수정 버튼을 작성자에게만 보여주면 충분해?
A. 아니다. 버튼 표시 제어는 UX용이고 실제 수정 API는 Backend에서 작성자 여부를 검증해야 한다.

Q. 게시글 수정 페이지를 Frontend에서 막으면 안전해?
A. 아니다. 사용자가 API를 직접 호출할 수 있으므로 Backend owner check가 필수다.

Q. owner check는 언제 가능해?
A. 현재 사용자 정보와 리소스 작성자 정보가 모두 로딩된 뒤 가능하다.

---

# 5. Role Based UI

## 5.1 Role Based UI Basics

### [개념]

Role Based UI는 사용자 권한에 따라 메뉴, 버튼, 링크, 페이지 일부를 다르게 보여주는 방식이다.

Role Based UI는 사용자 경험을 정리하는 용도이며 보안의 최종 기준이 아니다.

---

### [핵심]

사용 대상:

- admin menu
- mypage link
- edit button
- delete button
- owner-only action
- role badge
- forbidden message
- conditional rendering
- user menu
- notification link

기본 기준:

```text
authenticated false
→ login / signup button

authenticated true
→ mypage / logout button

user.role ROLE_ADMIN
→ admin menu

owner user
→ edit / delete button
```

---

### [실무]

Header 예:

```tsx
function Header() {
  const { initialized, authenticated, user } = useAuth();

  if (!initialized) {
    return <header />;
  }

  return (
    <header>
      <Link to="/">Home</Link>

      {authenticated && <Link to="/mypage">My Page</Link>}

      {user?.role === "ROLE_ADMIN" && <Link to="/admin">Admin</Link>}

      {!authenticated && <Link to="/login">Login</Link>}
    </header>
  );
}
```

Owner UI 예:

```tsx
function PostActions({ post }: { post: PostDetail }) {
  const { user } = useAuth();
  const isOwner = user?.userId === post.authorId;

  if (!isOwner) {
    return null;
  }

  return (
    <div>
      <button type="button">수정</button>
      <button type="button">삭제</button>
    </div>
  );
}
```

주의:

- 버튼 숨김은 보안이 아님
- API 호출 권한은 Backend가 검증
- owner check도 Backend에서 최종 검증
- role naming 통일
- user null 처리
- loading 중 flicker 방지
- role 정보가 없으면 fallback 처리
- UI 표시 기준과 API 권한 기준을 분리

---

### [FAQ]

Q. 관리자 메뉴는 어떻게 숨겨?
A. Auth State의 user.role을 확인해 ROLE_ADMIN일 때만 메뉴를 렌더링한다.

Q. 삭제 버튼을 작성자에게만 보여주면 충분해?
A. 아니다. 버튼 표시 제어는 UX용이고 실제 삭제 API는 Backend에서 작성자 여부를 검증해야 한다.

Q. role이 없을 때 UI가 깜빡여?
A. Auth loading이 끝나기 전 조건부 렌더링이 실행되면 flicker가 생길 수 있다. initialized 상태를 사용해 제어한다.

---

## 5.2 Permission Component Pattern

### [개념]

Permission Component Pattern은 role 또는 권한 조건을 재사용 가능한 컴포넌트로 분리하는 방식이다.

여러 화면에서 동일한 role 조건을 반복하지 않고 일관된 UI 제어를 할 수 있다.

---

### [핵심]

구성 요소:

- RequireAuth
- RequireRole
- RequireOwner
- Can
- PermissionGate
- allowedRoles
- fallback
- children
- user role
- condition

---

### [실무]

RequireRole 예:

```tsx
type RequireRoleProps = {
  allowedRoles: Array<"ROLE_USER" | "ROLE_ADMIN">;
  fallback?: React.ReactNode;
  children: React.ReactNode;
};

function RequireRole({
  allowedRoles,
  fallback = null,
  children,
}: RequireRoleProps) {
  const { initialized, user } = useAuth();

  if (!initialized) {
    return null;
  }

  if (!user || !allowedRoles.includes(user.role)) {
    return fallback;
  }

  return children;
}
```

사용 예:

```tsx
<RequireRole allowedRoles={["ROLE_ADMIN"]}>
  <Link to="/admin">Admin</Link>
</RequireRole>
```

Owner Gate 예:

```tsx
function RequireOwner({
  ownerId,
  children,
}: {
  ownerId: number;
  children: React.ReactNode;
}) {
  const { user } = useAuth();

  if (user?.userId !== ownerId) {
    return null;
  }

  return children;
}
```

주의:

- Permission Component는 UI 제어용
- Backend Authorization 대체 금지
- fallback 메시지 정책 결정
- initialized 전 null 또는 skeleton 처리
- role naming 통일
- ownerId 타입 일치 확인
- 권한 조건이 복잡하면 Permission Matrix 문서와 분리

---

### [FAQ]

Q. Role Based UI 조건문이 여러 곳에 반복돼?
A. RequireRole 또는 PermissionGate 컴포넌트로 분리하면 중복을 줄일 수 있다.

Q. PermissionGate를 쓰면 보안이 강화돼?
A. UI 일관성은 좋아지지만 보안의 최종 기준은 여전히 Backend Authorization이다.

Q. 권한 없는 경우 버튼을 숨길까 메시지를 보여줄까?
A. 기능 성격에 따라 다르다. 관리자 메뉴는 숨기고 접근 실패는 forbidden message를 보여주는 식으로 정책을 정한다.

---

# 6. Forbidden Page

## 6.1 Forbidden Page Design

### [개념]

Forbidden Page는 인증은 되었지만 접근 권한이 없는 사용자가 보는 권한 없음 화면이다.

403 Forbidden 응답이나 Role Based Route 실패와 연결된다.

---

### [핵심]

사용 상황:

- 403 response
- Role Based Route denied
- owner check failed
- admin page denied
- private resource denied
- forbidden fallback

표시 내용:

- 접근 권한 없음 메시지
- 메인으로 이동
- 이전 페이지로 이동
- 관리자 문의 안내
- 로그인 상태 유지

---

### [실무]

Forbidden Page 예:

```tsx
function ForbiddenPage() {
  const navigate = useNavigate();

  return (
    <main>
      <h1>접근 권한이 없습니다.</h1>
      <p>이 페이지를 볼 수 있는 권한이 없습니다.</p>
      <button type="button" onClick={() => navigate("/", { replace: true })}>
        메인으로 이동
      </button>
    </main>
  );
}
```

Route 설정:

```tsx
<Route path="/forbidden" element={<ForbiddenPage />} />
```

주의:

- forbidden page를 RoleRoute 내부에 두지 않음
- 403에서 logout하지 않음
- 사용자의 로그인 상태는 유지 가능
- 내부 권한 정책을 과도하게 노출하지 않음
- 이전 페이지로 이동 시 다시 forbidden이 반복될 수 있음
- 관리자 문의 문구는 프로젝트 정책에 따라 조정

---

### [FAQ]

Q. 403이면 로그아웃해야 해?
A. 대부분 아니다. 인증은 되었지만 권한이 없는 상태이므로 권한 없음 화면이나 메시지를 보여주는 것이 일반적이다.

Q. forbidden page는 어디에 둬야 해?
A. RoleRoute 보호 밖에 두어 권한 없는 사용자도 권한 없음 화면을 볼 수 있게 해야 한다.

Q. 권한 없음 메시지에 상세 사유를 보여줘도 돼?
A. 과도한 내부 권한 정책 노출은 피하고 사용자에게 필요한 수준만 안내하는 것이 좋다.

---

# 7. Route Guard Troubleshooting

## 7.1 Auth Redirect Loop

### [개념]

Auth Redirect Loop는 login page와 protected page 사이에서 redirect가 반복되는 문제다.

대부분 initialized 미사용, route guard 조건 충돌, PublicOnlyRoute와 ProtectedRoute 설정 오류로 발생한다.

---

### [핵심]

원인:

- auth loading 상태 미구분
- initialized 전 redirect
- login page도 protected 처리
- PublicOnlyRoute와 ProtectedRoute 조건 충돌
- authenticated 계산 오류
- token은 있지만 user 정보 없음
- `/me` 실패 처리 오류
- redirect target이 login 또는 signup

---

### [실무]

Debug Flow:

```text
Redirect Loop 발생
→ 현재 route 확인
→ initialized 값 확인
→ authenticated 값 확인
→ user 값 확인
→ ProtectedRoute 조건 확인
→ PublicOnlyRoute 조건 확인
→ Navigate target 확인
→ redirect target validation 확인
```

문제 예:

```text
문제: /mypage → /login → /mypage 반복
원인: login 성공 후 redirect target은 /mypage지만 auth state가 아직 false
해결: applyLoginResult 완료 후 navigate 실행
```

문제 예:

```text
문제: /login 접근 시 계속 /login으로 이동
원인: redirect target이 /login으로 저장됨
해결: getSafeRedirectPath에서 /login은 /로 보정
```

주의:

- 초기 인증 확인 전 redirect하지 않음
- login route는 ProtectedRoute로 감싸지 않음
- 이미 로그인한 사용자의 login 접근 처리 기준 명확화
- Navigate replace 사용 고려
- redirect target이 다시 guard에 걸리는지 확인

---

### [FAQ]

Q. login과 mypage 사이를 계속 왔다 갔다 해?
A. auth initialized 전에 redirect하거나 ProtectedRoute와 PublicOnlyRoute 조건이 충돌했을 가능성이 크다.

Q. token은 있는데 login으로 보내져?
A. user 정보 복원 전 authenticated를 false로 판단했거나 `/me` 확인 loading을 기다리지 않았을 수 있다.

Q. login page가 계속 다시 열려?
A. PublicOnlyRoute 조건, authenticated 상태, redirect target이 login으로 저장되었는지 확인해야 한다.

---

## 7.2 Role UI Not Updating

### [개념]

Role UI Not Updating은 사용자 권한 변경이나 로그인 상태 변화 후 메뉴, 버튼, Route 접근이 갱신되지 않는 문제다.

대부분 user role state, `/me` 응답, role naming, cache 갱신 문제로 발생한다.

---

### [핵심]

원인:

- user role state 미갱신
- `/me` API 미호출
- stale auth state
- cache 미무효화
- role naming 불일치
- ROLE_ADMIN / ADMIN 혼용
- conditional rendering 조건 오류
- initialized 전 렌더링
- mock user role 불일치

---

### [실무]

Debug Flow:

```text
Role UI 문제 발생
→ Auth User 확인
→ user.role 값 확인
→ Backend /me 응답 확인
→ ROLE_ADMIN naming 확인
→ Conditional Rendering 조건 확인
→ Store 업데이트 확인
→ Cache invalidate 확인
→ initialized 상태 확인
```

문제 예:

```text
문제: 관리자 계정인데 Admin 메뉴가 안 보임
원인: Backend는 ADMIN 반환, Frontend는 ROLE_ADMIN 비교
해결: role naming 통일
```

문제 예:

```text
문제: 권한 변경 후 메뉴가 안 바뀜
원인: Auth State가 stale 상태
해결: /me refetch 또는 auth store 갱신
```

주의:

- role 값은 Backend와 naming 통일
- 권한 변경 후 `/me` refetch 필요 가능
- UI 숨김과 API 권한 검증은 별개
- user null 상태 처리
- RoleRoute와 Role Based UI가 같은 role 기준 사용

---

### [FAQ]

Q. 관리자 계정인데 관리자 메뉴가 안 보여?
A. user.role 값, role naming, Auth State 업데이트, 조건부 렌더링 조건을 확인해야 한다.

Q. ROLE_ADMIN과 ADMIN은 같은 거야?
A. 프로젝트 기준에 따라 다르지만 문자열이 다르면 조건문에서 다르게 처리된다. naming을 통일해야 한다.

Q. role 변경 후 UI가 안 바뀌어?
A. `/me` refetch, auth store 갱신, cache invalidate가 필요할 수 있다.

---

## 7.3 Forbidden Loop Troubleshooting

### [개념]

Forbidden Loop는 권한 없음 처리 후 이동한 페이지가 다시 같은 RoleRoute 또는 ProtectedRoute에 걸려 반복 redirect되는 문제다.

Forbidden Page 위치나 redirect target 설정이 잘못되었을 때 발생한다.

---

### [핵심]

원인:

- forbidden route가 RoleRoute 내부에 있음
- forbidden route도 admin guard 적용
- 403 처리 후 다시 forbidden API 호출
- previous page 이동이 다시 forbidden page 접근
- RoleRoute fallback target 오류
- authenticated false와 forbidden 처리 혼동

---

### [실무]

잘못된 구조:

```tsx
<Route element={<AdminRoute />}>
  <Route path="/admin" element={<AdminPage />} />
  <Route path="/forbidden" element={<ForbiddenPage />} />
</Route>
```

올바른 구조:

```tsx
<Route path="/forbidden" element={<ForbiddenPage />} />

<Route element={<AdminRoute />}>
  <Route path="/admin" element={<AdminPage />} />
</Route>
```

Debug Flow:

```text
Forbidden Loop 발생
→ /forbidden route 위치 확인
→ RoleRoute 내부 여부 확인
→ Navigate target 확인
→ 401인지 403인지 확인
→ authenticated 상태 확인
→ previous page button 동작 확인
```

주의:

- forbidden page는 보호 route 밖에 둠
- 401은 login redirect, 403은 forbidden 처리
- 이전 페이지 이동 버튼은 loop 가능성 검토
- 권한 없음 상태에서 자동 retry 금지
- RoleRoute denied와 API 403 처리 기준 통일

---

### [FAQ]

Q. forbidden page가 계속 반복돼?
A. forbidden route가 RoleRoute 내부에 있거나 redirect target이 다시 같은 guard에 걸릴 수 있다.

Q. forbidden page도 로그인해야 볼 수 있게 해야 해?
A. 프로젝트 정책에 따라 가능하지만 RoleRoute 내부에는 두지 않는 것이 loop 방지에 좋다.

Q. 403인데 login으로 보내져?
A. 401과 403 처리 기준이 섞였을 가능성이 있다. 403은 권한 없음으로 처리하는 것이 일반적이다.

---

# 8. Part06 Review Checklist

## 8.1 Protected Route / Role Based Route Checklist

### [개념]

Part06 검수는 Protected Route, PublicOnlyRoute, Role Based Route, Role Based UI, Forbidden Page가 Auth State와 Backend Authorization 기준에 맞게 연결되는지 확인한다.

---

### [핵심]

Checklist:

```md
- [ ] Route Guard 목적이 명확한가?
- [ ] Protected Route 기준이 포함되었는가?
- [ ] initialized 전 redirect 금지가 포함되었는가?
- [ ] authenticated 기준이 포함되었는가?
- [ ] previous location 저장 기준이 포함되었는가?
- [ ] Redirect After Login 기준이 포함되었는가?
- [ ] Safe Redirect 기준이 포함되었는가?
- [ ] Outlet 기반 Protected Route 기준이 포함되었는가?
- [ ] PublicOnlyRoute 기준이 포함되었는가?
- [ ] PublicOnlyRoute 예외 기준이 포함되었는가?
- [ ] Role Based Route 기준이 포함되었는가?
- [ ] allowedRoles 기준이 포함되었는가?
- [ ] ROLE_USER / ROLE_ADMIN naming 통일 기준이 포함되었는가?
- [ ] Outlet 기반 RoleRoute 기준이 포함되었는가?
- [ ] Owner Based Route 주의가 포함되었는가?
- [ ] Role Based UI 기준이 포함되었는가?
- [ ] Permission Component Pattern이 포함되었는가?
- [ ] Forbidden Page 기준이 포함되었는가?
- [ ] Backend Authorization 필수 기준이 반복 명시되었는가?
- [ ] Auth Redirect Loop Troubleshooting이 포함되었는가?
- [ ] Role UI Not Updating Troubleshooting이 포함되었는가?
- [ ] Forbidden Loop Troubleshooting이 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

Part06 이후 권장 문서 순서:

```text
Part06 Protected Route / Role Based Route
→ Part07 Logout / User Profile Fetch
→ Part08 OAuth2 Frontend Flow
→ Part09 401 / 403 / Troubleshooting
→ Part10 Security / Checklist / Retrieval Optimization
```

검수 기준:

```text
Auth State
→ Protected Route
→ PublicOnlyRoute
→ Role Based Route
→ Role Based UI
→ Forbidden Page
→ Troubleshooting
```

---

### [FAQ]

Q. Part06의 핵심은 뭐야?
A. Protected Route, PublicOnlyRoute, Role Based Route, Role Based UI, Forbidden Page 기준을 Auth State와 연결하는 것이다.

Q. Part06에서 Backend 권한 검증도 구현해?
A. 아니다. Backend 권한 검증은 Security 문서에서 다루고 Part06은 Frontend UX Guard 기준을 다룬다.

Q. Part06 다음 문서는 뭐야?
A. Logout / User Profile Fetch 문서가 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. Protected Route는 어떻게 만들어?
A. 인증 상태를 확인하고 비로그인 상태면 Navigate로 login 페이지에 redirect한다.

Q. Protected Route는 보안적으로 충분해?
A. 아니다. Frontend Route 보호는 UX용이고 실제 보안은 Backend 인증/인가가 담당해야 한다.

Q. Route Guard에서 가장 중요한 상태는 뭐야?
A. initialized, authenticated, user, role 상태를 구분하는 것이 중요하다.

Q. Frontend에서 페이지 접근을 막으면 API도 안전해져?
A. 아니다. 사용자는 API를 직접 호출할 수 있으므로 Backend에서 반드시 인증/인가를 검증해야 한다.

Q. Protected Route에서 initialized를 왜 확인해?
A. 새로고침 인증 복원 중 비로그인으로 오판해 login으로 잘못 보내는 것을 막기 위해서다.

Q. Protected Route로 감싸면 API 호출도 막혀?
A. 아니다. 화면 접근 UX만 막는 것이고 API 접근은 Backend Authorization으로 막아야 한다.

Q. Protected Route에서 이전 페이지를 어떻게 저장해?
A. `Navigate`의 `state={{ from: location.pathname }}` 또는 query string을 사용할 수 있다.

Q. Protected Route를 모든 페이지마다 감싸야 해?
A. Outlet 기반 중첩 라우팅을 사용하면 여러 보호 페이지를 한 번에 감쌀 수 있다.

Q. children 방식과 Outlet 방식 중 뭐가 좋아?
A. 단일 페이지 보호는 children 방식도 가능하고 여러 route group 보호는 Outlet 방식이 편하다.

Q. 로그인 후 원래 보려던 페이지로 돌아가려면?
A. Protected Route에서 location state나 query string에 이전 경로를 저장하고 로그인 성공 후 해당 경로로 navigate한다.

Q. redirect target 검증이 왜 필요해?
A. 외부 URL로 이동하는 open redirect 문제와 login 페이지 반복 이동 같은 redirect loop를 막기 위해 필요하다.

Q. 로그인 후 항상 `/`로 보내도 돼?
A. 가능하지만 보호 페이지 접근 후 로그인한 경우 사용자가 원래 보려던 페이지로 돌아가는 UX가 더 좋을 수 있다.

Q. 로그인한 사용자가 login 페이지에 접근하면 어떻게 해?
A. 보통 메인 페이지나 이전 페이지로 redirect한다.

Q. PublicOnlyRoute도 꼭 필요해?
A. 필수는 아니지만 로그인/회원가입 페이지 UX를 정리하는 데 유용하다.

Q. login page도 Protected Route로 감싸야 해?
A. 아니다. login page는 비로그인 사용자가 접근해야 하므로 Protected Route로 감싸면 redirect loop가 생길 수 있다.

Q. OAuth2 callback도 PublicOnlyRoute로 감싸도 돼?
A. 주의해야 한다. callback 처리 전에 authenticated 상태가 바뀌거나 redirect가 발생하면 OAuth2 처리가 중단될 수 있다.

Q. 이메일 인증 callback은 로그인 사용자만 접근해야 해?
A. 프로젝트 정책에 따라 다르다. 이메일 인증 링크는 비로그인 상태에서도 접근 가능하게 설계하는 경우가 많다.

Q. Role Based Route는 어떻게 만들어?
A. user.role이 allowedRoles에 포함되는지 확인하고 권한이 없으면 forbidden page로 redirect한다.

Q. Frontend에서 ROLE_ADMIN을 확인하면 관리자 API가 안전해져?
A. 아니다. Frontend role check는 화면 접근 UX용이고 관리자 API는 Backend에서 반드시 권한 검증해야 한다.

Q. 권한 없는 사용자는 어디로 보내?
A. 프로젝트 기준에 따라 `/forbidden`, `/`, `/login` 중 하나로 보낼 수 있다. 기준을 통일해야 한다.

Q. Role Based Route에서 user가 null이면?
A. 인증 복원 중인지 확인하고 initialized 이후에도 user가 없으면 login 또는 forbidden 처리 기준을 적용한다.

Q. 관리자 하위 페이지마다 RoleRoute를 감싸야 해?
A. Outlet 기반 RoleRoute를 사용하면 관리자 하위 route를 한 번에 보호할 수 있다.

Q. AdminRoute 안에서 다시 ProtectedRoute를 써야 해?
A. RoleRoute가 authenticated 확인까지 포함하면 별도 ProtectedRoute가 필요 없을 수 있다. 역할을 중복하지 않도록 기준을 정한다.

Q. 수정 버튼을 작성자에게만 보여주면 충분해?
A. 아니다. 버튼 표시 제어는 UX용이고 실제 수정 API는 Backend에서 작성자 여부를 검증해야 한다.

Q. 게시글 수정 페이지를 Frontend에서 막으면 안전해?
A. 아니다. 사용자가 API를 직접 호출할 수 있으므로 Backend owner check가 필수다.

Q. owner check는 언제 가능해?
A. 현재 사용자 정보와 리소스 작성자 정보가 모두 로딩된 뒤 가능하다.

Q. 관리자 메뉴는 어떻게 숨겨?
A. Auth State의 user.role을 확인해 ROLE_ADMIN일 때만 메뉴를 렌더링한다.

Q. 삭제 버튼을 작성자에게만 보여주면 충분해?
A. 아니다. 버튼 표시 제어는 UX용이고 실제 삭제 API는 Backend에서 작성자 여부를 검증해야 한다.

Q. role이 없을 때 UI가 깜빡여?
A. Auth loading이 끝나기 전 조건부 렌더링이 실행되면 flicker가 생길 수 있다. initialized 상태를 사용해 제어한다.

Q. Role Based UI 조건문이 여러 곳에 반복돼?
A. RequireRole 또는 PermissionGate 컴포넌트로 분리하면 중복을 줄일 수 있다.

Q. PermissionGate를 쓰면 보안이 강화돼?
A. UI 일관성은 좋아지지만 보안의 최종 기준은 여전히 Backend Authorization이다.

Q. 권한 없는 경우 버튼을 숨길까 메시지를 보여줄까?
A. 기능 성격에 따라 다르다. 관리자 메뉴는 숨기고 접근 실패는 forbidden message를 보여주는 식으로 정책을 정한다.

Q. 403이면 로그아웃해야 해?
A. 대부분 아니다. 인증은 되었지만 권한이 없는 상태이므로 권한 없음 화면이나 메시지를 보여주는 것이 일반적이다.

Q. forbidden page는 어디에 둬야 해?
A. RoleRoute 보호 밖에 두어 권한 없는 사용자도 권한 없음 화면을 볼 수 있게 해야 한다.

Q. 권한 없음 메시지에 상세 사유를 보여줘도 돼?
A. 과도한 내부 권한 정책 노출은 피하고 사용자에게 필요한 수준만 안내하는 것이 좋다.

Q. login과 mypage 사이를 계속 왔다 갔다 해?
A. auth initialized 전에 redirect하거나 ProtectedRoute와 PublicOnlyRoute 조건이 충돌했을 가능성이 크다.

Q. token은 있는데 login으로 보내져?
A. user 정보 복원 전 authenticated를 false로 판단했거나 `/me` 확인 loading을 기다리지 않았을 수 있다.

Q. login page가 계속 다시 열려?
A. PublicOnlyRoute 조건, authenticated 상태, redirect target이 login으로 저장되었는지 확인해야 한다.

Q. 관리자 계정인데 관리자 메뉴가 안 보여?
A. user.role 값, role naming, Auth State 업데이트, 조건부 렌더링 조건을 확인해야 한다.

Q. ROLE_ADMIN과 ADMIN은 같은 거야?
A. 프로젝트 기준에 따라 다르지만 문자열이 다르면 조건문에서 다르게 처리된다. naming을 통일해야 한다.

Q. role 변경 후 UI가 안 바뀌어?
A. `/me` refetch, auth store 갱신, cache invalidate가 필요할 수 있다.

Q. forbidden page가 계속 반복돼?
A. forbidden route가 RoleRoute 내부에 있거나 redirect target이 다시 같은 guard에 걸릴 수 있다.

Q. 403인데 login으로 보내져?
A. 401과 403 처리 기준이 섞였을 가능성이 있다. 403은 권한 없음으로 처리하는 것이 일반적이다.

Q. Part06 다음 문서는 뭐야?
A. Logout / User Profile Fetch 문서가 이어지는 것이 좋다.
