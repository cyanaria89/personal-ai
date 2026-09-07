# React Router Part05 Protected Route Auth

---

# 1. Protected Route and Auth Routing

## 1.1 Purpose

### [개념]

Protected Route는 인증되지 않은 사용자나 권한이 없는 사용자가 특정 Route에 접근하지 못하도록 제한하는 Frontend Routing 구조다.

React Router에서 Protected Route는 Navigate, useLocation, 인증 상태, 권한 정보, loading 상태를 조합해 구현한다.

이 문서는 Frontend Agent가 인증 기반 Route Guard, Role Based Route, Auth Redirect, Guest Only Route, Backend Authorization 주의사항을 안정적으로 설계하도록 지원한다.

---

### [핵심]

- Protected Route
- Private Route
- Auth Route
- Route Guard
- Frontend Route Guard
- Authentication
- Authorization
- authenticated
- auth loading
- Navigate
- useLocation
- Auth Redirect
- Role Based Route
- Guest Only Route
- ROLE_USER
- ROLE_ADMIN
- Forbidden Page
- Backend Authorization
- JWT
- Access Token
- Refresh Token
- Security Boundary

기본 원칙:

```text
Frontend Protected Route
→ UX 접근 제어

Backend Authorization
→ 실제 보안 검증
```

---

### [실무]

2026 실무 기준에서 Protected Route는 보안의 전부가 아니다.

Frontend Protected Route는 사용자가 접근하면 안 되는 화면을 숨기거나 login page로 redirect하는 UX 장치다.

실제 보안은 반드시 Backend API에서 인증/인가로 검증해야 한다.

실무 사용 대상:

- 마이페이지
- 회원 정보 수정
- 찜 목록
- 결제 내역
- 관리자 페이지
- 게시글 작성 페이지
- 인증 사용자 전용 기능
- ROLE_ADMIN 전용 화면
- 로그인 사용자의 login page 접근 제한
- token 만료 후 login redirect

Auth Route 설계 Flow:

```text
Route Access
→ Check Auth Loading
→ Check Authentication
→ Check Role / Permission
→ Allow Render or Redirect
→ Backend API Authorization Still Required
```

---

### [FAQ]

Q. Protected Route는 뭐야?
A. 인증되지 않은 사용자나 권한 없는 사용자가 특정 화면 Route에 접근하지 못하도록 제한하는 Frontend Routing 구조다.

Q. Protected Route는 보안적으로 충분해?
A. 아니다. Frontend Route 보호는 UX용이고 실제 보안은 Backend 인증/인가가 반드시 처리해야 한다.

Q. Protected Route의 핵심은 뭐야?
A. 인증 loading 처리, authenticated 확인, 권한 확인, Navigate redirect, Backend Authorization 필수 인식이다.

Q. 로그인하지 않은 사용자는 어디로 보내?
A. 보통 `/login`으로 redirect하고 필요하면 원래 접근하려던 경로를 저장한다.

---

# 2. Protected Route Basics

## 2.1 Protected Route Concept

### [개념]

Protected Route는 인증 상태를 확인한 뒤 접근 가능하면 children을 렌더링하고, 접근 불가능하면 login page나 forbidden page로 redirect하는 Component다.

React Router에서는 Navigate Component를 사용해 조건부 redirect를 수행할 수 있다.

---

### [핵심]

- Protected Route
- authenticated
- children
- Navigate
- redirect
- replace
- auth loading
- private page
- login redirect
- route guard

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

---

### [실무]

loading 포함 예:

```jsx
import { Navigate } from "react-router";

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

Nested Route 보호 예:

```jsx
<Route
  path="/mypage"
  element={
    <ProtectedRoute loading={authLoading} authenticated={authenticated}>
      <MyPageLayout />
    </ProtectedRoute>
  }
>
  <Route index element={<MyPageHome />} />
  <Route path="profile" element={<ProfilePage />} />
  <Route path="favorites" element={<FavoritePage />} />
</Route>
```

실무 기준:

- 인증 상태 loading 중에는 redirect하지 않음
- authenticated 확인 후 children 렌더링
- 비로그인 사용자는 `/login` redirect
- redirect에는 replace 옵션 고려
- MyPage 같은 그룹 Route는 부모 Route에서 보호 가능
- Frontend Route 보호는 UX용
- Backend API 인증/인가 필수
- JWT 존재 여부만으로 권한을 완전히 신뢰하지 않음

---

### [FAQ]

Q. Protected Route는 어떻게 만들어?
A. 인증 상태를 확인하고 비로그인 상태면 Navigate로 login 페이지에 redirect한다.

Q. 인증 상태 확인 전 바로 login으로 보내도 돼?
A. 권장하지 않는다. 인증 상태 loading 중에는 임시 Loading UI를 보여주고 확인 후 redirect해야 한다.

Q. Protected Route는 어디에 적용해?
A. 마이페이지, 회원 정보, 관리자 페이지, 작성 페이지처럼 인증이 필요한 Route에 적용한다.

Q. Nested Route 전체를 보호할 수 있어?
A. 가능하다. 부모 Layout Route를 Protected Route로 감싸면 하위 Route 전체를 보호할 수 있다.

---

## 2.2 Protected Route with useLocation

### [개념]

useLocation을 사용하면 비로그인 사용자가 접근하려던 기존 경로를 저장하고 login 성공 후 원래 위치로 되돌릴 수 있다.

이전 위치는 Navigate의 state로 전달할 수 있다.

---

### [핵심]

- useLocation
- location.pathname
- location.search
- previous location
- redirect target
- login redirect
- Navigate state
- return after login
- from path

예:

```jsx
import { Navigate, useLocation } from "react-router";

function ProtectedRoute({ loading, authenticated, children }) {
  const location = useLocation();

  if (loading) {
    return <div>Loading...</div>;
  }

  if (!authenticated) {
    return (
      <Navigate
        to="/login"
        replace
        state={{ from: location.pathname + location.search }}
      />
    );
  }

  return children;
}
```

---

### [실무]

LoginPage에서 복귀 처리:

```jsx
import { useLocation, useNavigate } from "react-router";

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

실무 기준:

- 기존 path와 query string을 함께 저장 가능
- `location.pathname + location.search` 사용 가능
- login 성공 후 `navigate(from, { replace: true })`
- location.state가 없을 때 fallback path 필요
- redirect target validation 고려
- 민감정보를 location.state에 넣지 않음
- 새로고침 시 location.state가 사라질 수 있음
- 영구 redirect target이 필요하면 query string 방식 검토

---

### [FAQ]

Q. 로그인 후 원래 페이지로 돌아가려면?
A. Protected Route에서 useLocation으로 현재 경로를 state에 저장하고 로그인 성공 후 navigate로 복귀한다.

Q. location.pathname만 저장하면 충분해?
A. 검색 조건까지 복원해야 하면 location.search도 함께 저장하는 것이 좋다.

Q. location.state가 없으면 어떻게 해?
A. 기본 경로 `/` 같은 fallback path를 사용한다.

Q. redirect target을 state로 저장해도 돼?
A. 가능하다. 다만 새로고침 시 사라질 수 있으므로 fallback 처리가 필요하다.

---

# 3. Auth Loading State

## 3.1 Auth Loading Concept

### [개념]

Auth Loading State는 사용자의 인증 상태를 확인하는 동안 아직 로그인 여부를 확정할 수 없는 상태다.

Protected Route는 auth loading 중에 바로 redirect하면 안 된다.

---

### [핵심]

- auth loading
- authentication check
- token validation
- refresh token check
- user profile loading
- loading UI
- redirect delay
- false negative prevention
- flicker prevention

문제 Flow:

```text
Initial Render
→ authenticated default false
→ Protected Route redirects login
→ Auth check later succeeds
→ Wrong redirect already happened
```

권장 Flow:

```text
Initial Render
→ authLoading true
→ Show Loading
→ Auth Check Complete
→ authenticated true or false
→ Render or Redirect
```

---

### [실무]

Auth 상태 예:

```jsx
const authState = {
  loading: true,
  authenticated: false,
  user: null,
};
```

Protected Route 예:

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

실무 기준:

- App 초기 진입 시 token 확인 필요
- Access Token 만료 여부 확인 가능
- Refresh Token 재발급 중 loading 유지 가능
- 사용자 정보 `/api/users/me` 조회 중 loading 유지 가능
- loading 중 redirect 금지
- loading UI 또는 skeleton 표시 가능
- loading이 무한 지속되지 않도록 error 처리 필요
- 인증 실패와 서버 오류를 구분

---

### [FAQ]

Q. Auth Loading State는 왜 필요해?
A. 인증 상태 확인 전 비로그인으로 오판해 잘못 redirect하는 문제를 막기 위해 필요하다.

Q. authenticated 초기값을 false로 두면 안 돼?
A. 가능하지만 loading 상태 없이 false만 사용하면 초기 인증 확인 전에 login으로 redirect될 수 있다.

Q. token 확인 중에는 어떤 화면을 보여줘?
A. Loading UI, skeleton, blank guard 화면 등을 사용할 수 있다.

Q. auth loading이 끝나지 않으면?
A. token validation, refresh 요청, user profile 요청의 실패 처리를 확인해야 한다.

---

# 4. Guest Only Route

## 4.1 Guest Only Route Concept

### [개념]

Guest Only Route는 로그인하지 않은 사용자만 접근할 수 있는 Route다.

이미 로그인한 사용자가 login page나 signup page에 접근하면 main page 또는 이전 page로 redirect한다.

---

### [핵심]

- Guest Only Route
- Public Only Route
- Login Page Guard
- Signup Page Guard
- authenticated user redirect
- Navigate
- replace
- auth loading
- redirect loop prevention

기본 예:

```jsx
import { Navigate } from "react-router";

function GuestOnlyRoute({ loading, authenticated, children }) {
  if (loading) {
    return <div>Loading...</div>;
  }

  if (authenticated) {
    return <Navigate to="/" replace />;
  }

  return children;
}
```

---

### [실무]

Route 적용:

```jsx
<Route
  path="/login"
  element={
    <GuestOnlyRoute loading={authLoading} authenticated={authenticated}>
      <LoginPage />
    </GuestOnlyRoute>
  }
/>

<Route
  path="/signup"
  element={
    <GuestOnlyRoute loading={authLoading} authenticated={authenticated}>
      <SignupPage />
    </GuestOnlyRoute>
  }
/>
```

실무 기준:

- login page
- signup page
- find password page는 정책에 따라 guest only 또는 public 가능
- 이미 로그인한 사용자는 `/` 또는 `/mypage`로 redirect
- loading 중에는 redirect하지 않음
- Protected Route와 Guest Only Route 조건이 충돌하지 않게 설계
- login 성공 후 redirect target 처리 기준과 충돌 방지
- redirect loop 주의

---

### [FAQ]

Q. Guest Only Route는 뭐야?
A. 로그인하지 않은 사용자만 접근할 수 있는 Route다.

Q. 로그인한 사용자가 login page에 접근하면 어떻게 해?
A. 보통 main page나 mypage로 redirect한다.

Q. signup page도 Guest Only Route로 감싸?
A. 일반적으로 이미 로그인한 사용자가 회원가입 페이지에 갈 필요가 없으므로 감쌀 수 있다.

Q. Guest Only Route에서도 loading 처리가 필요해?
A. 필요하다. 인증 상태 확인 전 잘못 redirect하는 것을 막기 위해 필요하다.

---

# 5. Role Based Route

## 5.1 Role Based Route Concept

### [개념]

Role Based Route는 사용자 권한에 따라 접근 가능한 Route를 제한하는 구조다.

예를 들어 ROLE_ADMIN 사용자만 `/admin` Route에 접근하도록 제한할 수 있다.

---

### [핵심]

- Role Based Route
- Role Route
- Authorization Guard
- user role
- allowed roles
- ROLE_USER
- ROLE_ADMIN
- forbidden redirect
- admin route
- Backend Authorization
- Frontend UX Guard

기본 예:

```jsx
import { Navigate } from "react-router";

function RoleRoute({ loading, authenticated, role, allowedRoles, children }) {
  if (loading) {
    return <div>Loading...</div>;
  }

  if (!authenticated) {
    return <Navigate to="/login" replace />;
  }

  if (!allowedRoles.includes(role)) {
    return <Navigate to="/forbidden" replace />;
  }

  return children;
}
```

---

### [실무]

Admin Route 적용:

```jsx
<Route
  path="/admin"
  element={
    <RoleRoute
      loading={authLoading}
      authenticated={authenticated}
      role={user?.role}
      allowedRoles={["ROLE_ADMIN"]}
    >
      <AdminLayout />
    </RoleRoute>
  }
>
  <Route index element={<AdminDashboardPage />} />
  <Route path="users" element={<AdminUserPage />} />
  <Route path="festivals" element={<AdminFestivalPage />} />
</Route>
```

실무 기준:

- role naming 통일
- `ROLE_ADMIN` / `ADMIN` 혼용 금지
- allowedRoles 배열 사용 가능
- 비로그인과 권한 부족을 구분
- 비로그인은 `/login`
- 권한 부족은 `/forbidden` 또는 프로젝트 기준 redirect
- Frontend role check는 UX용
- Backend API에서 `ROLE_ADMIN` 검증 필수
- JWT payload role만 맹신하지 않음
- 사용자 role은 서버 검증된 user profile 기준 사용 권장

---

### [FAQ]

Q. Role Based Route는 뭐야?
A. 사용자 권한에 따라 접근 가능한 Route를 제한하는 구조다.

Q. Admin Route는 어떻게 보호해?
A. RoleRoute에서 authenticated와 role을 확인하고 ROLE_ADMIN이 아니면 forbidden page로 redirect한다.

Q. Frontend에서 ROLE_ADMIN 체크하면 보안이 되는 거야?
A. 아니다. Frontend 권한 체크는 화면 접근 UX용이고 실제 API 보안은 Backend에서 검증해야 한다.

Q. 권한 없는 사용자는 어디로 보내?
A. 프로젝트 기준에 따라 `/forbidden`, `/login`, `/` 중 하나로 보낼 수 있다. 기준을 통일해야 한다.

---

## 5.2 Role Naming Consistency

### [개념]

Role Naming Consistency는 Frontend와 Backend에서 사용하는 권한 이름을 통일하는 규칙이다.

권한 이름이 혼용되면 Route Guard, API Authorization, UI 조건부 렌더링에서 오류가 발생할 수 있다.

---

### [핵심]

권장:

- ROLE_USER
- ROLE_ADMIN

금지:

- ROLE_ADMIN / ADMIN 혼용
- ROLE_USER / USER 혼용
- admin / ROLE_ADMIN 혼용
- 대소문자 혼용
- role / authority / permission 의미 혼동

사용 위치:

- JWT payload
- user profile response
- RoleRoute
- Admin Menu conditional render
- Backend SecurityConfig
- API Authorization

---

### [실무]

좋은 예:

```javascript
export const USER_ROLES = {
  USER: "ROLE_USER",
  ADMIN: "ROLE_ADMIN",
};
```

사용:

```jsx
<RoleRoute role={user?.role} allowedRoles={[USER_ROLES.ADMIN]}>
  <AdminLayout />
</RoleRoute>
```

나쁜 예:

```jsx
<RoleRoute role={user?.role} allowedRoles={["ADMIN"]}>
  <AdminLayout />
</RoleRoute>
```

문제:

```text
Backend user role이 ROLE_ADMIN이면 "ADMIN"과 일치하지 않음
```

실무 기준:

- Backend 응답 role 값과 Frontend 상수 일치
- 권한 문자열은 상수화
- 대소문자 통일
- ROLE prefix 사용 여부 통일
- 문서 전체에서 ROLE_ADMIN / ROLE_USER 기준 유지
- Permission 세분화는 별도 Auth Architecture 문서에서 다룸

---

### [FAQ]

Q. ROLE_ADMIN과 ADMIN 중 뭘 써야 해?
A. 프로젝트 기준으로 하나만 써야 한다. Spring Security 기준과 맞추려면 ROLE_ADMIN 형태가 자주 사용된다.

Q. role 이름이 안 맞으면 어떻게 돼?
A. 실제 관리자인데도 forbidden으로 redirect되거나 권한 UI가 잘못 표시될 수 있다.

Q. role 문자열은 직접 써도 돼?
A. 가능하지만 상수로 관리하면 오타와 혼용을 줄일 수 있다.

Q. Frontend와 Backend role 이름을 맞춰야 해?
A. 맞춰야 한다. API 응답, JWT, Route Guard, Backend Authorization 기준이 일관되어야 한다.

---

# 6. Auth Redirect Flow

## 6.1 Auth Redirect Concept

### [개념]

Auth Redirect는 로그인 상태, 권한 상태, token 상태에 따라 사용자를 적절한 Route로 이동시키는 흐름이다.

Auth Redirect는 Protected Route, Guest Only Route, Role Based Route, token 만료 처리에서 사용된다.

---

### [핵심]

사용 상황:

- 비로그인 사용자의 보호 페이지 접근
- 로그인 성공 후 원래 페이지 이동
- 이미 로그인한 사용자의 login page 접근
- 권한 없는 사용자의 admin page 접근
- logout 후 main page 이동
- token 만료 후 login 이동
- refresh token 실패 후 login 이동

기본 Flow:

```text
Protected Page Access
→ Check Auth Loading
→ If Not Authenticated
→ Save Current Location
→ Redirect Login
→ Login Success
→ Navigate Previous Location
```

---

### [실무]

Protected Route redirect:

```jsx
<Navigate
  to="/login"
  replace
  state={{ from: location.pathname + location.search }}
/>
```

Login success redirect:

```jsx
const from = location.state?.from ?? "/";

await login();
navigate(from, { replace: true });
```

Logout redirect:

```jsx
async function handleLogout() {
  await logout();
  navigate("/", { replace: true });
}
```

Token expired redirect:

```text
API 401
→ Clear Auth State
→ Try Refresh Token if policy allows
→ If Refresh Fails
→ Redirect /login
```

실무 기준:

- redirect target 저장 기준 통일
- login 성공 후 복귀 기준 통일
- logout 후 이동 기준 통일
- token 만료 시 처리 기준 통일
- 401과 403 구분
- redirect loop 방지
- replace 옵션 적극 검토
- redirect target validation 고려

---

### [FAQ]

Q. Auth Redirect는 뭐야?
A. 로그인 상태나 권한 상태에 따라 사용자를 login, forbidden, main 같은 Route로 이동시키는 흐름이다.

Q. 로그인 후 원래 페이지로 돌아가려면?
A. Protected Route에서 현재 위치를 저장하고 login 성공 후 해당 위치로 navigate한다.

Q. logout 후에는 어디로 보내?
A. 보통 main page `/` 또는 login page로 보내며 프로젝트 기준을 통일한다.

Q. token 만료 시 어디로 보내?
A. refresh token 재발급 정책에 따라 처리하고 실패하면 보통 `/login`으로 redirect한다.

---

## 6.2 Redirect Loop Prevention

### [개념]

Redirect Loop는 Route Guard 조건이 충돌해 사용자가 두 Route 사이를 계속 이동하거나 화면이 정상 렌더링되지 않는 문제다.

Protected Route, Guest Only Route, Auth Loading 처리에서 자주 발생한다.

---

### [핵심]

원인:

- auth loading 처리 누락
- authenticated 초기값 오판
- login page도 Protected Route로 감쌈
- Protected Route와 Guest Only Route 조건 충돌
- redirect target이 현재 Route와 동일
- role check와 auth check 순서 오류
- token refresh 실패 반복
- useEffect navigate dependency 오류

---

### [실무]

잘못된 구조 예:

```jsx
<Route
  path="/login"
  element={
    <ProtectedRoute authenticated={authenticated}>
      <LoginPage />
    </ProtectedRoute>
  }
/>
```

문제:

```text
login page는 비로그인 사용자가 접근해야 하는데 Protected Route로 막음
```

권장:

```jsx
<Route
  path="/login"
  element={
    <GuestOnlyRoute loading={authLoading} authenticated={authenticated}>
      <LoginPage />
    </GuestOnlyRoute>
  }
/>
```

Redirect Loop Debug Flow:

```text
Redirect Loop
→ Current Route 확인
→ Route Guard 종류 확인
→ loading 처리 확인
→ authenticated 값 확인
→ role 값 확인
→ Navigate target 확인
→ replace 여부 확인
→ useEffect navigate dependency 확인
```

실무 기준:

- login route는 Guest Only 또는 Public 기준
- protected route는 인증 필요 화면에만 적용
- loading 중 redirect 금지
- 현재 path와 target path 동일 여부 확인
- token refresh retry 제한
- 401 처리와 route redirect 중복 확인

---

### [FAQ]

Q. redirect loop는 왜 생겨?
A. 인증 조건이나 redirect target이 잘못되어 login과 protected page 사이를 계속 오갈 때 발생한다.

Q. login page를 Protected Route로 감싸도 돼?
A. 일반적으로 안 된다. login page는 Guest Only Route 또는 Public Route로 처리한다.

Q. redirect loop는 어떻게 디버깅해?
A. 현재 Route, Guard 조건, loading 상태, authenticated 값, Navigate target을 확인한다.

Q. token 만료 후 redirect가 반복돼?
A. refresh token 실패 처리, auth state 초기화, 401 interceptor 반복 요청 여부를 확인해야 한다.

---

# 7. Frontend Guard vs Backend Authorization

## 7.1 Security Boundary

### [개념]

Frontend Guard는 화면 접근 UX를 제어하는 구조이고 Backend Authorization은 실제 데이터와 기능 접근을 보호하는 보안 경계다.

React Router Protected Route는 보안 경계가 아니다.

---

### [핵심]

Frontend Guard 역할:

- 화면 접근 제한
- 메뉴 숨김
- login redirect
- forbidden page 표시
- 사용자 UX 개선

Backend Authorization 역할:

- API 인증 검증
- API 권한 검증
- 데이터 접근 제어
- 관리자 기능 보호
- 서버 리소스 보호
- Security Boundary

핵심 원칙:

```text
Frontend Route Guard can be bypassed.
Backend Authorization must protect API.
```

---

### [실무]

위험한 착각:

```text
Admin Route를 Frontend에서 숨겼으니 안전하다
```

문제:

```text
사용자가 직접 API를 호출할 수 있음
Frontend 코드는 브라우저에서 노출됨
Route Guard는 우회 가능
```

필수 Backend 검증:

```text
GET /api/admin/users
→ Backend checks Authentication
→ Backend checks ROLE_ADMIN
→ Return data or 403
```

실무 기준:

- Frontend Protected Route는 UX용
- Backend SecurityConfig / Method Security / Controller Authorization 필요
- Admin API는 ROLE_ADMIN 검증 필수
- User API는 본인 리소스 접근 검증 필요
- JWT payload는 서버에서 검증 필요
- Frontend에 민감한 권한 로직만 의존하지 않음
- 401 / 403 응답 처리 기준 필요

---

### [FAQ]

Q. Frontend Route Guard만 있으면 보안이 돼?
A. 아니다. Frontend Guard는 우회 가능하므로 Backend Authorization이 실제 보안을 담당해야 한다.

Q. 관리자 메뉴를 숨기면 관리자 API도 안전해?
A. 아니다. 메뉴 숨김은 UX일 뿐이고 관리자 API는 Backend에서 ROLE_ADMIN을 검증해야 한다.

Q. Protected Route를 왜 쓰는 거야?
A. 비로그인 사용자의 화면 접근을 자연스럽게 login으로 유도하고 UX를 개선하기 위해 사용한다.

Q. 실제 보안 경계는 어디야?
A. Backend API 인증/인가가 실제 보안 경계다.

---

## 7.2 401 and 403 Handling

### [개념]

401 Unauthorized는 인증되지 않은 상태이고 403 Forbidden은 인증은 되었지만 권한이 부족한 상태다.

Frontend Route Guard와 API Error Handling은 401과 403을 구분해야 한다.

---

### [핵심]

- 401 Unauthorized
- 403 Forbidden
- unauthenticated
- unauthorized naming caution
- forbidden
- login redirect
- forbidden page
- token expired
- insufficient role
- API error handling

구분:

| Status | 의미                       | Frontend 처리                        |
| ------ | -------------------------- | ------------------------------------ |
| 401    | 인증 안 됨 / token invalid | login redirect 또는 refresh token    |
| 403    | 인증됨 / 권한 부족         | forbidden page 또는 접근 불가 메시지 |
| 404    | 리소스 없음                | Not Found UI                         |
| 500    | 서버 오류                  | Error UI                             |

---

### [실무]

401 처리 Flow:

```text
API 401
→ Access Token 만료 확인
→ Refresh Token 시도
→ 성공 시 원래 요청 재시도
→ 실패 시 auth state clear
→ /login redirect
```

403 처리 Flow:

```text
API 403
→ User authenticated
→ Permission insufficient
→ /forbidden route or Forbidden UI
```

Route Guard 기준:

```text
Not Authenticated
→ /login

Authenticated but Not Allowed
→ /forbidden
```

실무 기준:

- 401과 403을 같은 login redirect로 처리하지 않음
- token 만료와 권한 부족 구분
- forbidden page 제공 가능
- API 응답 status 기반 UI 처리
- Frontend role guard와 Backend API 403 처리 둘 다 필요
- 사용자 메시지와 개발자 로그 구분

---

### [FAQ]

Q. 401과 403 차이는 뭐야?
A. 401은 인증이 안 된 상태이고 403은 인증은 됐지만 권한이 부족한 상태다.

Q. 401이면 어디로 보내?
A. refresh token 정책을 적용한 뒤 실패하면 보통 `/login`으로 보낸다.

Q. 403이면 어디로 보내?
A. 보통 `/forbidden` 페이지나 접근 권한 없음 UI를 보여준다.

Q. 권한 부족도 login으로 보내면 안 돼?
A. 로그인된 사용자의 권한 부족은 forbidden 처리하는 것이 의미상 더 명확하다.

---

# 8. Protected Route Structure

## 8.1 Route File Structure

### [개념]

Protected Route Structure는 인증 관련 Route Guard, 권한 상수, 인증 상태 Hook, Page Route를 역할별로 배치하는 구조다.

Routing 파일이 커질수록 ProtectedRoute, GuestOnlyRoute, RoleRoute를 분리하는 것이 좋다.

---

### [핵심]

- ProtectedRoute.jsx
- GuestOnlyRoute.jsx
- RoleRoute.jsx
- routePaths.js
- userRoles.js
- useAuth
- auth store
- AppRoutes
- Auth Layout
- Admin Layout
- MyPage Layout

기본 구조:

```text
src
├ routes
│ ├ AppRoutes.jsx
│ ├ ProtectedRoute.jsx
│ ├ GuestOnlyRoute.jsx
│ ├ RoleRoute.jsx
│ └ routePaths.js
├ constants
│ └ userRoles.js
├ hooks
│ └ useAuth.js
├ layouts
│ ├ MainLayout.jsx
│ ├ AuthLayout.jsx
│ ├ MyPageLayout.jsx
│ └ AdminLayout.jsx
└ pages
```

---

### [실무]

ProtectedRoute 파일 예:

```jsx
import { Navigate, useLocation } from "react-router";
import { ROUTES } from "./routePaths";

function ProtectedRoute({ loading, authenticated, children }) {
  const location = useLocation();

  if (loading) {
    return <div>Loading...</div>;
  }

  if (!authenticated) {
    return (
      <Navigate
        to={ROUTES.LOGIN}
        replace
        state={{ from: location.pathname + location.search }}
      />
    );
  }

  return children;
}

export default ProtectedRoute;
```

Role constants:

```javascript
export const USER_ROLES = {
  USER: "ROLE_USER",
  ADMIN: "ROLE_ADMIN",
};
```

실무 기준:

- Guard Component는 routes 폴더 또는 auth feature에 배치
- role 문자열은 constants로 관리
- route path는 routePaths로 관리
- auth state는 useAuth 또는 store에서 제공
- AppRoutes는 Route 연결에 집중
- Guard 내부에서 복잡한 API 호출을 직접 수행하지 않음
- Auth Provider / Store / Hook 책임 분리

---

### [FAQ]

Q. ProtectedRoute 파일은 어디에 둬?
A. 보통 routes 폴더나 auth feature 폴더에 둔다.

Q. role 상수는 어디에 둬?
A. constants/userRoles.js 같은 파일에 두면 오타와 혼용을 줄일 수 있다.

Q. AppRoutes 안에 Guard 로직을 다 써도 돼?
A. 작은 프로젝트는 가능하지만 Route가 많아지면 ProtectedRoute, RoleRoute로 분리하는 것이 좋다.

Q. Guard Component에서 API를 직접 호출해도 돼?
A. 인증 상태 조회는 useAuth나 store에서 받고 Guard는 판단과 redirect에 집중하는 것이 좋다.

---

## 8.2 AppRoutes Auth Example

### [개념]

AppRoutes Auth Example은 MainLayout, AuthLayout, MyPageLayout, AdminLayout을 Protected Route와 Role Based Route로 연결하는 구성 예시다.

---

### [핵심]

구성 대상:

- Public Route
- Guest Only Route
- Protected Route
- Role Based Route
- MainLayout
- AuthLayout
- MyPageLayout
- AdminLayout
- NotFoundPage
- ForbiddenPage

---

### [실무]

예:

```jsx
import { Routes, Route } from "react-router";
import MainLayout from "../layouts/MainLayout";
import AuthLayout from "../layouts/AuthLayout";
import MyPageLayout from "../layouts/MyPageLayout";
import AdminLayout from "../layouts/AdminLayout";
import ProtectedRoute from "./ProtectedRoute";
import GuestOnlyRoute from "./GuestOnlyRoute";
import RoleRoute from "./RoleRoute";
import { USER_ROLES } from "../constants/userRoles";

function AppRoutes({ authLoading, authenticated, user }) {
  return (
    <Routes>
      <Route element={<MainLayout />}>
        <Route path="/" element={<MainPage />} />
        <Route path="/festivals" element={<FestivalListPage />} />
        <Route path="/festivals/:festivalId" element={<FestivalDetailPage />} />
      </Route>

      <Route element={<AuthLayout />}>
        <Route
          path="/login"
          element={
            <GuestOnlyRoute loading={authLoading} authenticated={authenticated}>
              <LoginPage />
            </GuestOnlyRoute>
          }
        />
        <Route
          path="/signup"
          element={
            <GuestOnlyRoute loading={authLoading} authenticated={authenticated}>
              <SignupPage />
            </GuestOnlyRoute>
          }
        />
      </Route>

      <Route
        path="/mypage"
        element={
          <ProtectedRoute loading={authLoading} authenticated={authenticated}>
            <MyPageLayout />
          </ProtectedRoute>
        }
      >
        <Route index element={<MyPageHome />} />
        <Route path="profile" element={<ProfilePage />} />
        <Route path="favorites" element={<FavoritePage />} />
      </Route>

      <Route
        path="/admin"
        element={
          <RoleRoute
            loading={authLoading}
            authenticated={authenticated}
            role={user?.role}
            allowedRoles={[USER_ROLES.ADMIN]}
          >
            <AdminLayout />
          </RoleRoute>
        }
      >
        <Route index element={<AdminDashboardPage />} />
        <Route path="users" element={<AdminUserPage />} />
      </Route>

      <Route path="/forbidden" element={<ForbiddenPage />} />
      <Route path="*" element={<NotFoundPage />} />
    </Routes>
  );
}
```

실무 기준:

- public route와 protected route 구분
- auth page는 GuestOnlyRoute 적용 가능
- mypage 그룹은 ProtectedRoute로 보호
- admin 그룹은 RoleRoute로 보호
- forbidden route 제공
- NotFound route 제공
- loading, authenticated, user role 전달 기준 통일
- 실제 API 보안은 Backend에서 처리

---

### [FAQ]

Q. MyPage 전체를 보호하려면 어떻게 해?
A. `/mypage` 부모 Route element를 ProtectedRoute로 감싸면 하위 Route 전체를 보호할 수 있다.

Q. Admin 전체를 보호하려면 어떻게 해?
A. `/admin` 부모 Route element를 RoleRoute로 감싸고 allowedRoles에 ROLE_ADMIN을 지정한다.

Q. `/forbidden` Route도 만들어야 해?
A. 권한 부족을 명확히 안내하려면 ForbiddenPage를 두는 것이 좋다.

Q. Public Route와 Protected Route를 AppRoutes에서 같이 관리해도 돼?
A. 가능하다. 다만 Guard Component를 분리해 AppRoutes 가독성을 유지하는 것이 좋다.

---

# 9. Auth Route Troubleshooting

## 9.1 Protected Route Troubleshooting

### [개념]

Protected Route Troubleshooting은 인증 Route 접근 실패, 잘못된 redirect, loading 오작동, 권한 판단 오류를 찾는 과정이다.

---

### [핵심]

문제:

- 로그인했는데 login page로 이동
- 비로그인인데 보호 Page가 보임
- 관리자 계정인데 forbidden 표시
- 일반 사용자가 admin page 접근 가능
- 새로고침 후 auth 상태 초기화
- token 만료 후 무한 redirect
- login 성공 후 원래 page로 돌아가지 않음
- 뒤로가기로 login page 복귀
- location.state가 undefined
- role 값이 undefined

원인:

- auth loading 처리 누락
- authenticated state 초기화 문제
- token 저장 / 복원 문제
- user profile 조회 실패
- role naming 불일치
- ROLE_ADMIN / ADMIN 혼용
- replace 옵션 누락
- location.state fallback 누락
- Backend 401 / 403 처리 혼동
- Route Guard 적용 위치 오류

---

### [실무]

Debug Flow:

```text
Auth Route Problem
→ Current URL 확인
→ authLoading 값 확인
→ authenticated 값 확인
→ user 값 확인
→ user.role 값 확인
→ Route Guard 종류 확인
→ Navigate target 확인
→ location.state 확인
→ token 저장 상태 확인
→ API 401 / 403 응답 확인
```

대표 문제 1:

```text
문제: 로그인했는데 /login으로 이동
원인: auth loading 중 authenticated false로 판단
해결: loading 중 redirect 금지
```

대표 문제 2:

```text
문제: 관리자 계정인데 /forbidden
원인: user.role은 ROLE_ADMIN인데 allowedRoles는 ADMIN
해결: role naming 통일
```

대표 문제 3:

```text
문제: login 성공 후 원래 page로 안 돌아감
원인: location.state.from 저장 또는 읽기 누락
해결: ProtectedRoute에서 state 저장, LoginPage에서 fallback 포함 처리
```

대표 문제 4:

```text
문제: 뒤로가면 login page로 돌아감
원인: replace 옵션 누락
해결: Navigate replace 또는 navigate(..., { replace: true }) 적용
```

---

### [FAQ]

Q. 로그인했는데도 login으로 보내져?
A. auth loading 처리, authenticated state 복원, token validation 결과를 확인해야 한다.

Q. 관리자 계정인데 forbidden이 나와?
A. user.role 값과 allowedRoles 값이 정확히 일치하는지 확인한다.

Q. login 성공 후 원래 페이지로 안 돌아가?
A. ProtectedRoute에서 location.state.from을 저장하고 LoginPage에서 읽는지 확인한다.

Q. 뒤로가기로 login page에 돌아와?
A. login 성공 navigate 또는 Protected Route redirect에 replace 옵션을 적용하는 것을 검토한다.

---

## 9.2 Auth State Refresh Problem

### [개념]

Auth State Refresh Problem은 새로고침 후 메모리의 인증 상태가 초기화되어 로그인 상태를 잃거나 잘못 redirect되는 문제다.

SPA는 새로고침 시 JavaScript 메모리 상태가 초기화되므로 token 복원과 user profile 재조회 기준이 필요하다.

---

### [핵심]

문제:

- 새로고침 후 로그아웃된 것처럼 보임
- 새로고침 후 Protected Route에서 login redirect
- token은 있는데 user가 null
- user.role이 undefined
- admin page 새로고침 시 forbidden
- auth loading이 너무 빨리 false가 됨

원인:

- token 저장소에서 복원 누락
- user profile 재조회 누락
- auth loading 상태 부재
- refresh token 처리 실패
- role 정보 로딩 전 RoleRoute 판단
- localStorage / cookie 정책 혼동

---

### [실무]

권장 초기화 Flow:

```text
App Start
→ authLoading true
→ Check Access Token / Cookie
→ Validate Token or Request /api/users/me
→ Set authenticated and user
→ authLoading false
→ Route Guard 판단
```

RoleRoute 주의:

```jsx
function RoleRoute({ loading, authenticated, role, allowedRoles, children }) {
  if (loading) {
    return <div>Loading...</div>;
  }

  if (!authenticated) {
    return <Navigate to="/login" replace />;
  }

  if (!role || !allowedRoles.includes(role)) {
    return <Navigate to="/forbidden" replace />;
  }

  return children;
}
```

실무 기준:

- 새로고침 후 auth state 복원 필요
- user role 로딩 전 RoleRoute 판단 금지
- token 저장 방식에 따른 복원 전략 필요
- cookie 기반이면 `/api/users/me` 확인 가능
- localStorage 기반이면 token 존재 확인 후 검증 필요
- 보안 정책은 Authentication Frontend Flow 문서에서 심화
- Guard는 loading 완료 후 판단

---

### [FAQ]

Q. 새로고침하면 로그인 상태가 풀려?
A. 메모리 상태가 초기화되므로 token 복원과 user profile 재조회가 필요하다.

Q. token은 있는데 user가 null이야?
A. token만 복원하고 사용자 정보 `/api/users/me` 조회를 하지 않았을 수 있다.

Q. admin page 새로고침 시 forbidden이 나와?
A. role 로딩 전 RoleRoute가 판단했을 가능성이 있다. auth loading 처리를 확인한다.

Q. auth state 복원은 어디서 해?
A. 보통 AuthProvider, 전역 store 초기화, App 초기 effect에서 처리한다.

---

# 10. Protected Route Checklist

## 10.1 Part05 Checklist

### [개념]

Protected Route Auth 문서는 인증 기반 Route Guard와 권한 기반 Route Guard를 검수하기 위한 체크리스트를 포함한다.

---

### [핵심]

Checklist:

```md
- [ ] Protected Route 개념이 설명되었는가?
- [ ] Frontend Route Guard는 UX용이라는 설명이 포함되었는가?
- [ ] Backend Authorization 필수 설명이 포함되었는가?
- [ ] auth loading 처리 기준이 포함되었는가?
- [ ] Navigate redirect 예제가 포함되었는가?
- [ ] useLocation으로 이전 위치 저장 예제가 포함되었는가?
- [ ] login 성공 후 원래 경로 복귀 기준이 포함되었는가?
- [ ] Guest Only Route가 포함되었는가?
- [ ] Role Based Route가 포함되었는가?
- [ ] ROLE_USER / ROLE_ADMIN naming 통일 기준이 포함되었는가?
- [ ] 401과 403 차이가 포함되었는가?
- [ ] Forbidden Page 기준이 포함되었는가?
- [ ] Redirect Loop Prevention이 포함되었는가?
- [ ] Auth State Refresh Problem이 포함되었는가?
- [ ] Route File Structure가 포함되었는가?
- [ ] Common Mistakes가 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 Flow:

```text
Draft
→ Protected Route Check
→ Auth Loading Check
→ useLocation Redirect Check
→ Guest Only Route Check
→ Role Based Route Check
→ Role Naming Check
→ Frontend vs Backend Security Check
→ 401 / 403 Check
→ Redirect Loop Check
→ Auth Refresh Check
→ Troubleshooting Check
→ FAQ Check
→ Retrieval Queries Check
→ Final Review
```

---

### [FAQ]

Q. Part05 검수에서 가장 중요한 것은?
A. auth loading 처리, redirect 기준, role naming 통일, Backend Authorization 필수 인식이다.

Q. Part05에서 JWT 저장 전략을 깊게 다뤄?
A. 아니다. JWT 저장과 refresh flow 심화는 Authentication Frontend Flow 문서에서 다룬다.

Q. Part05에서 Backend SecurityConfig를 다뤄?
A. 아니다. Backend Authorization 필요성만 명확히 언급하고 구현은 Security Domain Rules에서 다룬다.

---

# 11. Protected Route Common Mistakes

## 11.1 Common Mistakes

### [개념]

Protected Route에서 자주 발생하는 실수는 auth loading 누락, Frontend Guard를 보안으로 착각, role 이름 불일치, redirect loop, 401/403 혼동이다.

---

### [핵심]

자주 발생:

- 인증 상태 확인 전 login redirect
- auth loading 상태 없음
- authenticated 초기값 false만 사용
- login page를 Protected Route로 감쌈
- Guest Only Route와 Protected Route 조건 충돌
- Navigate target이 현재 path와 같음
- login 성공 후 replace 옵션 누락
- location.state fallback 누락
- location.state가 새로고침 후 유지된다고 착각
- ROLE_ADMIN / ADMIN 혼용
- role 로딩 전 forbidden redirect
- Frontend RoleRoute만으로 보안이 된다고 착각
- Backend API 권한 검증 누락
- 401과 403을 모두 login redirect로 처리
- token 만료 refresh 실패 반복
- 새로고침 후 auth state 복원 누락
- Admin menu 숨김을 보안으로 착각
- JWT payload role을 무조건 신뢰
- user profile 조회 실패 처리 누락

---

### [실무]

대표 문제 1:

```text
문제: 새로고침하면 login으로 튕김
원인: auth state 복원 전 Protected Route 판단
해결: authLoading true 상태에서 검증 완료 후 판단
```

대표 문제 2:

```text
문제: 일반 사용자가 admin API 호출 가능
원인: Frontend Route만 막고 Backend API 권한 검증 누락
해결: Backend에서 ROLE_ADMIN 검증 필수
```

대표 문제 3:

```text
문제: 관리자도 forbidden
원인: ROLE_ADMIN / ADMIN naming 불일치
해결: role 상수화와 Backend 응답 기준 통일
```

대표 문제 4:

```text
문제: login과 mypage 사이 redirect loop
원인: loading 처리 누락 또는 Guard 조건 충돌
해결: loading, authenticated, GuestOnlyRoute 조건 확인
```

Debug Flow:

```text
Protected Route Problem
→ authLoading 확인
→ authenticated 확인
→ user 확인
→ role 확인
→ Route Guard 확인
→ Navigate target 확인
→ location.state 확인
→ token validation 확인
→ API 401 / 403 확인
→ Backend Authorization 확인
```

---

### [FAQ]

Q. Protected Route에서 가장 흔한 실수는?
A. auth loading 없이 바로 redirect하거나 Frontend Guard만으로 보안이 된다고 착각하는 것이다.

Q. role 관련 문제는 어떻게 줄여?
A. ROLE_USER, ROLE_ADMIN 같은 권한 문자열을 상수화하고 Backend 응답과 통일한다.

Q. 새로고침 후 로그인 상태가 사라지는 문제는 어떻게 봐?
A. token 복원, user profile 재조회, auth loading 처리 순서를 확인한다.

Q. 권한 문제는 Frontend와 Backend 중 어디를 먼저 봐?
A. UX 문제는 Frontend Guard를 보고 실제 보안 문제는 Backend Authorization을 확인해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. React Router Part05는 뭘 다뤄?
A. Protected Route, Guest Only Route, Role Based Route, Auth Redirect, Frontend Guard와 Backend Authorization 차이를 다룬다.

Q. Protected Route는 뭐야?
A. 인증되지 않은 사용자나 권한 없는 사용자가 특정 화면 Route에 접근하지 못하도록 제한하는 Frontend Routing 구조다.

Q. Private Route는 뭐야?
A. Protected Route와 유사하게 인증된 사용자만 접근 가능한 Route를 의미한다.

Q. Route Guard는 뭐야?
A. Route 접근 전에 인증 상태나 권한을 확인해 렌더링 또는 redirect를 결정하는 구조다.

Q. Frontend Route Guard는 보안 기능이야?
A. 아니다. Frontend Route Guard는 UX용이고 실제 보안은 Backend Authorization이 담당해야 한다.

Q. Protected Route는 보안적으로 충분해?
A. 아니다. Frontend Route 보호는 UX용이고 실제 보안은 Backend 인증/인가가 반드시 처리해야 한다.

Q. Protected Route는 어떻게 만들어?
A. 인증 상태를 확인하고 비로그인 상태면 Navigate로 login 페이지에 redirect한다.

Q. Protected Route에는 Navigate를 써도 돼?
A. 가능하다. 인증 상태에 따라 login 페이지로 redirect할 때 자주 사용한다.

Q. 인증 상태 확인 전 바로 login으로 보내도 돼?
A. 권장하지 않는다. 인증 상태 loading 중에는 Loading UI를 보여주고 확인 후 redirect해야 한다.

Q. Auth Loading State는 왜 필요해?
A. 인증 상태 확인 전 비로그인으로 오판해 잘못 redirect하는 문제를 막기 위해 필요하다.

Q. authenticated 초기값을 false로 두면 안 돼?
A. 가능하지만 loading 상태 없이 false만 사용하면 초기 인증 확인 전에 login으로 redirect될 수 있다.

Q. token 확인 중에는 어떤 화면을 보여줘?
A. Loading UI, skeleton, blank guard 화면 등을 사용할 수 있다.

Q. Protected Route는 어디에 적용해?
A. 마이페이지, 회원 정보, 관리자 페이지, 작성 페이지처럼 인증이 필요한 Route에 적용한다.

Q. Nested Route 전체를 보호할 수 있어?
A. 가능하다. 부모 Layout Route를 Protected Route로 감싸면 하위 Route 전체를 보호할 수 있다.

Q. MyPage 전체를 보호하려면 어떻게 해?
A. `/mypage` 부모 Route element를 ProtectedRoute로 감싸면 하위 Route 전체를 보호할 수 있다.

Q. 로그인하지 않은 사용자는 어디로 보내?
A. 보통 `/login`으로 redirect하고 필요하면 원래 접근하려던 경로를 저장한다.

Q. 로그인 후 원래 페이지로 돌아가려면?
A. Protected Route에서 현재 위치를 저장하고 login 성공 후 해당 위치로 navigate한다.

Q. useLocation으로 이전 위치를 저장하는 이유는?
A. 로그인 성공 후 사용자가 원래 접근하려던 페이지로 돌아가게 하기 위해서다.

Q. location.pathname만 저장하면 충분해?
A. 검색 조건까지 복원해야 하면 location.search도 함께 저장하는 것이 좋다.

Q. location.state가 없으면 어떻게 해?
A. 기본 경로 `/` 같은 fallback path를 사용한다.

Q. redirect target을 state로 저장해도 돼?
A. 가능하다. 다만 새로고침 시 사라질 수 있으므로 fallback 처리가 필요하다.

Q. Guest Only Route는 뭐야?
A. 로그인하지 않은 사용자만 접근할 수 있는 Route다.

Q. 로그인한 사용자가 login page에 접근하면 어떻게 해?
A. 보통 main page나 mypage로 redirect한다.

Q. signup page도 Guest Only Route로 감싸?
A. 일반적으로 이미 로그인한 사용자가 회원가입 페이지에 갈 필요가 없으므로 감쌀 수 있다.

Q. Guest Only Route에서도 loading 처리가 필요해?
A. 필요하다. 인증 상태 확인 전 잘못 redirect하는 것을 막기 위해 필요하다.

Q. Role Based Route는 뭐야?
A. 사용자 권한에 따라 접근 가능한 Route를 제한하는 구조다.

Q. Admin Route는 어떻게 보호해?
A. RoleRoute에서 authenticated와 role을 확인하고 ROLE_ADMIN이 아니면 forbidden page로 redirect한다.

Q. Admin 전체를 보호하려면 어떻게 해?
A. `/admin` 부모 Route element를 RoleRoute로 감싸고 allowedRoles에 ROLE_ADMIN을 지정한다.

Q. Frontend에서 ROLE_ADMIN 체크하면 보안이 되는 거야?
A. 아니다. Frontend 권한 체크는 화면 접근 UX용이고 실제 API 보안은 Backend에서 검증해야 한다.

Q. 권한 없는 사용자는 어디로 보내?
A. 프로젝트 기준에 따라 `/forbidden`, `/login`, `/` 중 하나로 보낼 수 있다. 기준을 통일해야 한다.

Q. ROLE_ADMIN과 ADMIN 중 뭘 써야 해?
A. 프로젝트 기준으로 하나만 써야 한다. Spring Security 기준과 맞추려면 ROLE_ADMIN 형태가 자주 사용된다.

Q. role 이름이 안 맞으면 어떻게 돼?
A. 실제 관리자인데도 forbidden으로 redirect되거나 권한 UI가 잘못 표시될 수 있다.

Q. role 문자열은 직접 써도 돼?
A. 가능하지만 상수로 관리하면 오타와 혼용을 줄일 수 있다.

Q. Frontend와 Backend role 이름을 맞춰야 해?
A. 맞춰야 한다. API 응답, JWT, Route Guard, Backend Authorization 기준이 일관되어야 한다.

Q. Auth Redirect는 뭐야?
A. 로그인 상태나 권한 상태에 따라 사용자를 login, forbidden, main 같은 Route로 이동시키는 흐름이다.

Q. logout 후에는 어디로 보내?
A. 보통 main page `/` 또는 login page로 보내며 프로젝트 기준을 통일한다.

Q. token 만료 시 어디로 보내?
A. refresh token 재발급 정책에 따라 처리하고 실패하면 보통 `/login`으로 redirect한다.

Q. redirect loop는 왜 생겨?
A. 인증 조건이나 redirect target이 잘못되어 login과 protected page 사이를 계속 오갈 때 발생한다.

Q. login page를 Protected Route로 감싸도 돼?
A. 일반적으로 안 된다. login page는 Guest Only Route 또는 Public Route로 처리한다.

Q. redirect loop는 어떻게 디버깅해?
A. 현재 Route, Guard 조건, loading 상태, authenticated 값, Navigate target을 확인한다.

Q. token 만료 후 redirect가 반복돼?
A. refresh token 실패 처리, auth state 초기화, 401 interceptor 반복 요청 여부를 확인해야 한다.

Q. Frontend Route Guard만 있으면 보안이 돼?
A. 아니다. Frontend Guard는 우회 가능하므로 Backend Authorization이 실제 보안을 담당해야 한다.

Q. 관리자 메뉴를 숨기면 관리자 API도 안전해?
A. 아니다. 메뉴 숨김은 UX일 뿐이고 관리자 API는 Backend에서 ROLE_ADMIN을 검증해야 한다.

Q. 실제 보안 경계는 어디야?
A. Backend API 인증/인가가 실제 보안 경계다.

Q. 401과 403 차이는 뭐야?
A. 401은 인증이 안 된 상태이고 403은 인증은 됐지만 권한이 부족한 상태다.

Q. 401이면 어디로 보내?
A. refresh token 정책을 적용한 뒤 실패하면 보통 `/login`으로 보낸다.

Q. 403이면 어디로 보내?
A. 보통 `/forbidden` 페이지나 접근 권한 없음 UI를 보여준다.

Q. 권한 부족도 login으로 보내면 안 돼?
A. 로그인된 사용자의 권한 부족은 forbidden 처리하는 것이 의미상 더 명확하다.

Q. `/forbidden` Route도 만들어야 해?
A. 권한 부족을 명확히 안내하려면 ForbiddenPage를 두는 것이 좋다.

Q. ProtectedRoute 파일은 어디에 둬?
A. 보통 routes 폴더나 auth feature 폴더에 둔다.

Q. role 상수는 어디에 둬?
A. constants/userRoles.js 같은 파일에 두면 오타와 혼용을 줄일 수 있다.

Q. AppRoutes 안에 Guard 로직을 다 써도 돼?
A. 작은 프로젝트는 가능하지만 Route가 많아지면 ProtectedRoute, RoleRoute로 분리하는 것이 좋다.

Q. Guard Component에서 API를 직접 호출해도 돼?
A. 인증 상태 조회는 useAuth나 store에서 받고 Guard는 판단과 redirect에 집중하는 것이 좋다.

Q. 로그인했는데도 login으로 보내져?
A. auth loading 처리, authenticated state 복원, token validation 결과를 확인해야 한다.

Q. 관리자 계정인데 forbidden이 나와?
A. user.role 값과 allowedRoles 값이 정확히 일치하는지 확인한다.

Q. login 성공 후 원래 페이지로 안 돌아가?
A. ProtectedRoute에서 location.state.from을 저장하고 LoginPage에서 읽는지 확인한다.

Q. 뒤로가기로 login page에 돌아와?
A. login 성공 navigate 또는 Protected Route redirect에 replace 옵션을 적용하는 것을 검토한다.

Q. 새로고침하면 로그인 상태가 풀려?
A. 메모리 상태가 초기화되므로 token 복원과 user profile 재조회가 필요하다.

Q. token은 있는데 user가 null이야?
A. token만 복원하고 사용자 정보 `/api/users/me` 조회를 하지 않았을 수 있다.

Q. admin page 새로고침 시 forbidden이 나와?
A. role 로딩 전 RoleRoute가 판단했을 가능성이 있다. auth loading 처리를 확인한다.

Q. auth state 복원은 어디서 해?
A. 보통 AuthProvider, 전역 store 초기화, App 초기 effect에서 처리한다.

Q. Protected Route에서 가장 흔한 실수는?
A. auth loading 없이 바로 redirect하거나 Frontend Guard만으로 보안이 된다고 착각하는 것이다.

Q. role 관련 문제는 어떻게 줄여?
A. ROLE_USER, ROLE_ADMIN 같은 권한 문자열을 상수화하고 Backend 응답과 통일한다.

Q. 새로고침 후 로그인 상태가 사라지는 문제는 어떻게 봐?
A. token 복원, user profile 재조회, auth loading 처리 순서를 확인한다.

Q. 권한 문제는 Frontend와 Backend 중 어디를 먼저 봐?
A. UX 문제는 Frontend Guard를 보고 실제 보안 문제는 Backend Authorization을 확인해야 한다.

Q. Part05 다음에는 뭘 다뤄?
A. Part06 Error Deployment Troubleshooting에서 Not Found Route, Route Error Handling, SPA Refresh 404, API Path Collision을 다룬다.
