# Authentication Frontend Flow Part03 - Auth State / Auth Loading / Auth Restore

---

# 1. Auth State Design

## 1.1 Auth State Overview

### [개념]

Auth State는 Frontend에서 사용자의 인증 여부, 인증 확인 진행 상태, 사용자 요약 정보, 인증 오류 상태를 표현하는 상태다.

Auth State는 단순히 token 존재 여부만 의미하지 않는다.

Auth State는 `initialized`, `loading`, `authenticated`, `user`, `role`, `authError`를 구분해 Route Guard, Role Based UI, 인증 API 요청 흐름을 안정화한다.

---

### [핵심]

Auth State 핵심 요소:

- initialized
- authenticated
- loading
- user
- role
- accessToken presence
- authError
- tokenExpired
- login action
- logout action
- restore action
- clearAuth action

상태 구분:

```text
initialized false
→ 앱 시작 후 인증 상태 확인 중

authenticated true
→ 로그인 상태

authenticated false
→ 비로그인 상태

loading true
→ login / logout / me / refresh 요청 처리 중

user null
→ 사용자 정보 없음
```

---

### [실무]

2026 실무 기준 Auth State는 token, user, route guard, API client와 연결된다.

TypeScript 예:

```tsx
type AuthRole = "ROLE_USER" | "ROLE_ADMIN";

type AuthUser = {
  userId: number;
  nickname: string;
  role: AuthRole;
};

type AuthState = {
  initialized: boolean;
  authenticated: boolean;
  loading: boolean;
  user: AuthUser | null;
  authError: string | null;
};
```

권장 기준:

- authenticated와 user를 함께 관리
- initialized로 앱 초기 인증 확인 완료 여부 구분
- loading으로 login / logout / restore 요청 상태 구분
- token 존재만으로 authenticated 확정하지 않음
- `/me` API로 사용자 상태 확인 가능
- role naming은 `ROLE_USER`, `ROLE_ADMIN`처럼 통일
- logout 시 user와 authenticated 초기화
- 인증 실패 시 user null, authenticated false로 정리

주의:

```text
token exists
→ authenticated true 즉시 확정 금지
→ /me 또는 refresh 확인
→ 성공 시 user 설정
→ authenticated true
```

---

### [FAQ]

Q. Auth State에는 무엇이 들어가?
A. authenticated, initialized, loading, user, role, authError 같은 인증 상태 정보가 들어갈 수 있다.

Q. token이 있으면 authenticated true로 해도 돼?
A. 가능은 하지만 token이 만료되었거나 위조되었을 수 있으므로 `/me` 같은 API로 확인하는 흐름이 더 안전하다.

Q. user가 null인데 authenticated true여도 돼?
A. 권장하지 않는다. Role Based UI와 Protected Route가 불안정해지므로 user 복원 후 authenticated true로 처리하는 것이 좋다.

Q. role은 어디에 저장해?
A. UI 분기와 Route Guard에 필요한 최소 user summary 안에 `role`로 저장하는 방식이 일반적이다.

---

## 1.2 Auth State Lifecycle

### [개념]

Auth State Lifecycle은 앱 시작, 로그인, 새로고침 복원, token 만료, 로그아웃 과정에서 인증 상태가 어떻게 변하는지 정의하는 흐름이다.

Auth State Lifecycle을 명확히 해야 redirect loop, UI flicker, 인증 API 401 문제를 줄일 수 있다.

---

### [핵심]

Lifecycle 단계:

- App Start
- Auth Restore
- Login Pending
- Login Success
- Login Failure
- Authenticated Request
- Token Expired
- Refresh Success
- Refresh Failure
- Logout
- Clear Auth

기본 흐름:

```text
App Start
→ initialized false
→ Restore Auth
→ Restore Success: authenticated true
→ Restore Failure: authenticated false
→ initialized true
```

---

### [실무]

상태 전이 예:

| 상황           | initialized | loading | authenticated | user     |
| -------------- | ----------: | ------: | ------------: | -------- |
| 앱 시작 직후   |       false |    true |         false | null     |
| 인증 복원 성공 |        true |   false |          true | AuthUser |
| 인증 복원 실패 |        true |   false |         false | null     |
| 로그인 요청 중 |        true |    true |         false | null     |
| 로그인 성공    |        true |   false |          true | AuthUser |
| 로그아웃 후    |        true |   false |         false | null     |

구현 흐름:

```text
App Mount
→ setInitialized(false)
→ restoreAuth()
→ success: setUser(user), setAuthenticated(true)
→ failure: clearAuth()
→ finally: setInitialized(true)
```

주의:

- initialized 전 Protected Route redirect 금지
- 로그인 성공 전 authenticated true 금지
- 로그인 실패 시 기존 user state 정리 여부 검토
- token refresh 성공 시 authenticated 유지
- refresh 실패 시 clearAuth
- logout 시 user-specific cache 정리 필요

---

### [FAQ]

Q. initialized와 loading은 뭐가 달라?
A. initialized는 앱 최초 인증 확인이 끝났는지 나타내고 loading은 login, logout, `/me` 같은 인증 요청 진행 상태를 나타낸다.

Q. auth loading은 왜 필요해?
A. 새로고침 후 인증 상태 확인 전에 Protected Route가 login으로 잘못 redirect하는 것을 막기 위해 필요하다.

Q. 로그인 중 loading과 앱 시작 loading은 같은 상태로 처리해도 돼?
A. 가능하지만 UX가 복잡하면 `initialized`와 `loading`을 분리하는 것이 안정적이다.

---

# 2. Auth Store Pattern

## 2.1 Context Based Auth Store

### [개념]

Context Based Auth Store는 React Context와 Hook을 사용해 Auth State와 인증 액션을 전역으로 제공하는 방식이다.

소규모 프로젝트나 인증 상태가 단순한 프로젝트에서 사용하기 쉽다.

---

### [핵심]

구성 요소:

- AuthProvider
- useAuth
- AuthState
- login
- logout
- restoreAuth
- clearAuth
- setUser
- setAuthenticated

장점:

- React 기본 기능 사용
- Provider 기반 공유 쉬움
- 인증 상태 전역 접근 가능
- 별도 상태관리 라이브러리 불필요

주의:

- Context value 변경 시 하위 컴포넌트 re-render 가능
- 상태 규모가 커지면 Zustand / Redux Toolkit 검토
- Provider 위치 통일 필요

---

### [실무]

Context 예:

```tsx
type AuthContextValue = {
  initialized: boolean;
  authenticated: boolean;
  loading: boolean;
  user: AuthUser | null;
  login: (values: LoginFormValues) => Promise<void>;
  logout: () => Promise<void>;
  restoreAuth: () => Promise<void>;
};

const AuthContext = createContext<AuthContextValue | null>(null);

export function useAuth() {
  const value = useContext(AuthContext);

  if (!value) {
    throw new Error("useAuth must be used within AuthProvider");
  }

  return value;
}
```

Provider 위치 예:

```tsx
root.render(
  <AuthProvider>
    <RouterProvider router={router} />
  </AuthProvider>,
);
```

주의:

- AuthProvider는 Route Guard보다 상위에 위치
- useAuth는 AuthProvider 내부에서만 사용
- login / logout / restoreAuth 함수는 책임 분리
- token storage 로직과 user state 로직 혼합 주의
- re-render가 많으면 state selector 패턴 검토

---

### [FAQ]

Q. Auth State는 Context로 관리해도 돼?
A. 가능하다. 프로젝트 규모가 작거나 인증 상태가 단순하면 Context 기반 AuthProvider가 충분할 수 있다.

Q. useAuth를 아무 곳에서나 호출해도 돼?
A. AuthProvider 하위 컴포넌트에서만 호출해야 한다.

Q. Context를 쓰면 성능 문제가 생겨?
A. 상태 변경 시 하위 컴포넌트가 re-render될 수 있으므로 규모가 커지면 Zustand나 Redux Toolkit을 검토할 수 있다.

---

## 2.2 Zustand / Redux Auth Store

### [개념]

Zustand 또는 Redux Toolkit Auth Store는 인증 상태와 인증 액션을 외부 상태관리 라이브러리로 관리하는 방식이다.

인증 상태가 여러 화면, API, cache, role UI와 복잡하게 연결될 때 적합하다.

---

### [핵심]

사용 후보:

- Zustand
- Zustand Persist
- Redux Toolkit
- RTK Query
- TanStack Query 조합
- Auth Slice
- Auth Store
- Token Store
- User Store

장점:

- 전역 상태 접근 쉬움
- selector 기반 re-render 제어 가능
- 상태 액션 분리 쉬움
- 대규모 앱에서 관리 용이

주의:

- persist 대상 최소화
- token persist 보안 주의
- user 정보 과다 저장 금지
- cache와 auth state 불일치 주의

---

### [실무]

Zustand 예:

```tsx
type AuthStore = {
  initialized: boolean;
  authenticated: boolean;
  user: AuthUser | null;
  setInitialized: (value: boolean) => void;
  setAuth: (user: AuthUser) => void;
  clearAuth: () => void;
};

export const useAuthStore = create<AuthStore>((set) => ({
  initialized: false,
  authenticated: false,
  user: null,

  setInitialized: (value) => set({ initialized: value }),

  setAuth: (user) =>
    set({
      authenticated: true,
      user,
    }),

  clearAuth: () =>
    set({
      authenticated: false,
      user: null,
    }),
}));
```

Persist 주의 예:

```text
Persist 가능 후보
→ user summary
→ UI preference
→ last login flag

Persist 신중 후보
→ accessToken
→ refreshToken
→ personal data
```

주의:

- Zustand persist에 민감정보 저장 최소화
- token 저장 위치는 Backend 인증 정책과 함께 결정
- logout 시 persist storage 정리 필요
- store와 localStorage token 불일치 방지
- role 변경 시 `/me` refetch 또는 store 갱신 필요

---

### [FAQ]

Q. React에서 인증은 무조건 Redux로 해야 해?
A. 아니다. 프로젝트 규모에 따라 Context, Zustand, Redux Toolkit, TanStack Query 조합 중 선택할 수 있다.

Q. Zustand persist에 token을 저장해도 돼?
A. 가능은 하지만 XSS 위험이 있으므로 보안 요구사항에 따라 신중히 결정해야 한다.

Q. user 정보를 전부 store에 저장해도 돼?
A. 권장하지 않는다. UI에 필요한 최소한의 user summary만 저장하는 것이 좋다.

---

# 3. Auth Restore on Refresh

## 3.1 Auth Restore Overview

### [개념]

Auth Restore on Refresh는 브라우저 새로고침 후에도 로그인 상태를 복원하는 흐름이다.

Memory State는 새로고침 시 사라질 수 있으므로 저장된 token, cookie, refresh token, `/me` API를 활용해 인증 상태를 다시 확인해야 한다.

---

### [핵심]

필수 요소:

- app initialization
- initialized state
- auth loading
- stored token check
- cookie auth check
- `/me` request
- refresh token
- token expired handling
- clearAuth fallback
- route rendering delay

기본 Flow:

```text
App Start
→ Check Stored Token or Cookie
→ If Exists Call /me
→ Success: Set User and Authenticated
→ Failure: Clear Auth
→ Set Initialized True
→ Render Routes
```

---

### [실무]

Auth Restore 예:

```tsx
useEffect(() => {
  async function initializeAuth() {
    try {
      setInitialized(false);

      const hasAuthCredential = hasStoredTokenOrCookie();

      if (!hasAuthCredential) {
        clearAuth();
        return;
      }

      const user = await getMe();

      setUser(user);
      setAuthenticated(true);
    } catch {
      clearAuth();
    } finally {
      setInitialized(true);
    }
  }

  initializeAuth();
}, []);
```

주의:

- 초기화 완료 전 Protected Route redirect 보류
- token 존재만으로 로그인 확정하지 않음
- `/me` 실패 시 token 정리
- refresh token flow가 있으면 재발급 후 `/me` 재시도 가능
- 앱 첫 렌더링 깜빡임 방지 고려
- AuthProvider mount 시 한 번만 실행되도록 위치 주의
- StrictMode에서 effect 중복 실행 가능성 고려

---

### [FAQ]

Q. 새로고침하면 로그인이 풀려?
A. Auth State가 memory에만 있거나 초기 인증 복원 로직이 없으면 새로고침 시 로그인이 풀릴 수 있다.

Q. 새로고침 후 바로 login으로 튕겨?
A. 인증 상태 확인 loading을 기다리지 않고 Protected Route가 먼저 redirect했을 가능성이 있다.

Q. token은 있는데 왜 `/me`를 호출해?
A. token이 만료되었거나 위조되었을 수 있으므로 Backend 확인을 통해 실제 인증 상태와 사용자 정보를 복원하기 위해서다.

---

## 3.2 Restore with Access Token

### [개념]

Restore with Access Token은 브라우저 저장소에 남아 있는 access token으로 `/me` API를 호출해 인증 상태를 복원하는 방식이다.

이 방식은 구현이 단순하지만 access token 저장 위치의 보안 위험을 함께 검토해야 한다.

---

### [핵심]

Flow:

```text
App Start
→ Read Access Token
→ If Missing: clearAuth
→ If Exists: Call /me with Authorization Header
→ Success: setUser + authenticated true
→ 401: clearAuth
```

확인 대상:

- localStorage
- sessionStorage
- memory fallback
- Authorization Header
- Bearer Token
- `/me` API
- token expired
- token invalid

---

### [실무]

예:

```tsx
async function restoreAuthWithAccessToken() {
  const accessToken = getAccessToken();

  if (!accessToken) {
    clearAuth();
    return;
  }

  try {
    const user = await getMe();
    setUser(user);
    setAuthenticated(true);
  } catch {
    clearTokens();
    clearAuth();
  } finally {
    setInitialized(true);
  }
}
```

주의:

- access token이 저장되어도 Header에 붙지 않으면 `/me`는 401 발생
- Bearer 형식 확인 필요
- access token 만료 시 refresh flow 여부 결정
- localStorage 저장은 XSS 위험 검토
- sessionStorage는 탭 종료 시 사라짐
- token을 console.log로 출력하지 않음

---

### [FAQ]

Q. localStorage에 token이 있는데 401이 나?
A. Network 탭에서 Authorization Header에 실제로 token이 포함되었는지 확인해야 한다.

Q. Bearer를 빼먹으면 어떻게 돼?
A. Backend가 token 형식을 인식하지 못해 401이 발생할 수 있다.

Q. access token만으로 새로고침 복원이 가능해?
A. 가능하지만 token이 만료되면 복원에 실패할 수 있으므로 refresh token flow를 함께 고려할 수 있다.

---

## 3.3 Restore with Cookie Auth

### [개념]

Restore with Cookie Auth는 HttpOnly Cookie 기반 인증에서 Frontend가 token을 직접 읽지 않고 `/me` API를 호출해 인증 상태를 복원하는 방식이다.

Frontend는 cookie 값을 직접 확인하지 않고 Backend 응답으로 인증 여부를 판단한다.

---

### [핵심]

Flow:

```text
App Start
→ Call /me with credentials
→ Backend Checks Cookie
→ Success: setUser + authenticated true
→ 401: clearAuth
```

핵심 키워드:

- HttpOnly Cookie
- credentials
- withCredentials
- SameSite
- CSRF
- Cookie Auth
- Me API
- Auth Restore

---

### [실무]

Axios 설정 예:

```tsx
export const authApi = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  withCredentials: true,
});
```

복원 예:

```tsx
async function restoreAuthWithCookie() {
  try {
    const user = await getMe();

    setUser(user);
    setAuthenticated(true);
  } catch {
    clearAuth();
  } finally {
    setInitialized(true);
  }
}
```

주의:

- HttpOnly Cookie는 JS에서 직접 읽을 수 없음
- Frontend는 `/me` 응답으로 인증 여부 확인
- `withCredentials` 설정 필요 가능
- CORS credentials 설정은 Backend와 맞춰야 함
- SameSite / Secure / CSRF 정책 확인 필요
- Cookie Auth에서도 Backend Authorization이 최종 기준

---

### [FAQ]

Q. HttpOnly Cookie를 쓰면 Frontend에서 token을 읽을 수 있어?
A. 아니다. HttpOnly Cookie는 JavaScript로 읽을 수 없고 Frontend는 `/me` API 응답으로 인증 상태를 확인한다.

Q. Cookie Auth에서도 `/me` API가 필요해?
A. 필요하다. Frontend가 로그인 상태와 사용자 정보를 복원하려면 Backend에 현재 사용자 정보를 요청해야 한다.

Q. withCredentials는 언제 필요해?
A. cross-origin 요청에서 cookie를 포함해야 할 때 필요할 수 있으며 Backend CORS 설정과 함께 맞춰야 한다.

---

# 4. User Summary State

## 4.1 User Summary Design

### [개념]

User Summary State는 Frontend 인증 상태와 UI 분기에 필요한 최소 사용자 정보다.

전체 사용자 상세 정보가 아니라 Route Guard, Header, MyPage 링크, Role Based UI에 필요한 값만 저장한다.

---

### [핵심]

저장 후보:

- userId
- nickname
- email
- role
- profileImageUrl
- status
- verified
- provider

저장 지양:

- password
- refresh token
- 주민번호
- 상세 개인정보
- 결제 정보
- 민감 설정
- 불필요한 전체 profile

---

### [실무]

권장 타입:

```tsx
type AuthUser = {
  userId: number;
  nickname: string;
  role: "ROLE_USER" | "ROLE_ADMIN";
  profileImageUrl?: string;
};
```

사용 예:

```tsx
function HeaderUserArea() {
  const { authenticated, user } = useAuth();

  if (!authenticated || !user) {
    return <Link to="/login">Login</Link>;
  }

  return <Link to="/mypage">{user.nickname}</Link>;
}
```

주의:

- user summary는 UI에 필요한 최소 정보만 포함
- 사용자 상세 정보는 profile page에서 별도 조회 가능
- role은 Backend와 naming 통일
- user null 처리 필수
- role 변경 가능성이 있으면 `/me` refetch 필요
- 개인 정보 과다 persist 금지

---

### [FAQ]

Q. user 정보를 전부 저장해도 돼?
A. 권장하지 않는다. UI에 필요한 최소한의 user summary만 저장하는 것이 좋다.

Q. user summary에 role은 꼭 필요해?
A. Role Based UI나 Role Based Route를 사용한다면 필요하다.

Q. profile page 정보도 Auth State에 다 넣어야 해?
A. 아니다. Auth State에는 최소 정보만 넣고 profile page에서 상세 정보를 별도 조회하는 것이 좋다.

---

## 4.2 Role Naming Consistency

### [개념]

Role Naming Consistency는 Frontend와 Backend에서 권한 문자열을 동일하게 사용하는 기준이다.

`ROLE_ADMIN`과 `ADMIN`을 혼용하면 Role Based UI와 Role Based Route가 정상 동작하지 않을 수 있다.

---

### [핵심]

권장 naming:

- ROLE_USER
- ROLE_ADMIN

혼용 금지:

- USER
- ADMIN
- ROLE_MEMBER
- member
- admin
- role_admin

사용 위치:

- Auth State
- Role Based UI
- Role Based Route
- API Response DTO
- Backend Security
- Test Mock User

---

### [실무]

권장 타입:

```tsx
type AuthRole = "ROLE_USER" | "ROLE_ADMIN";

type AuthUser = {
  userId: number;
  nickname: string;
  role: AuthRole;
};
```

조건부 렌더링 예:

```tsx
function AdminMenu() {
  const { user } = useAuth();

  if (user?.role !== "ROLE_ADMIN") {
    return null;
  }

  return <Link to="/admin">Admin</Link>;
}
```

주의:

- Backend 응답의 role 문자열 확인
- Mock 데이터도 동일 naming 사용
- 대소문자 불일치 주의
- role이 없는 동안 loading / fallback 처리
- role check는 UX용이며 Backend Authorization을 대체하지 않음

---

### [FAQ]

Q. ROLE_ADMIN과 ADMIN은 같은 거야?
A. 프로젝트 기준에 따라 다르지만 문자열이 다르면 조건문에서 다르게 처리된다. naming을 통일해야 한다.

Q. 관리자 계정인데 관리자 메뉴가 안 보여?
A. user.role 값, role naming, Auth State 업데이트, 조건부 렌더링 조건을 확인해야 한다.

Q. Frontend에서 role check하면 보안이 돼?
A. 아니다. Frontend role check는 UX용이고 실제 권한 검증은 Backend에서 수행해야 한다.

---

# 5. Auth Loading UX

## 5.1 Auth Loading and Initialized

### [개념]

Auth Loading은 인증 관련 요청이 진행 중임을 나타내는 상태다.

Initialized는 앱 최초 인증 상태 확인이 완료되었는지 나타내는 상태다.

이 둘을 구분하면 새로고침 후 잘못된 redirect와 UI flicker를 줄일 수 있다.

---

### [핵심]

필수 구분:

- initialized false
- initialized true
- loading true
- loading false
- auth restore loading
- login submit loading
- logout loading
- protected route pending
- public only route pending

---

### [실무]

Route Guard에서 initialized 사용:

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

UI 기준:

```text
initialized false
→ 앱 인증 상태 확인 화면

login loading true
→ 로그인 버튼 disabled

logout loading true
→ 로그아웃 처리 중

authenticated false + initialized true
→ 비로그인 UI
```

주의:

- initialized 전 login redirect 금지
- role 정보 로딩 전 admin menu 깜빡임 주의
- login submit loading과 app init loading 혼동 금지
- loading UI는 짧고 명확하게 표시
- Loading UX 상세는 Error Handling & Loading UX 문서와 연결

---

### [FAQ]

Q. auth loading 중에는 어떻게 해?
A. 로그인 페이지로 보내지 말고 loading UI를 보여주며 인증 상태 확인이 끝날 때까지 기다리는 것이 좋다.

Q. role이 없을 때 UI가 깜빡여?
A. Auth loading이 끝나기 전 조건부 렌더링이 실행되면 flicker가 생길 수 있다. initialized 상태를 사용해 제어한다.

Q. initialized 없이 authenticated만 써도 돼?
A. 가능은 하지만 새로고침 복원 중 잘못된 redirect가 발생할 수 있어 initialized를 분리하는 것이 좋다.

---

## 5.2 Auth Flicker Prevention

### [개념]

Auth Flicker는 인증 상태 확인이 끝나기 전에 비로그인 UI나 권한 없는 UI가 잠깐 보이는 현상이다.

Auth Flicker를 방지하려면 initialized와 loading 상태를 기준으로 렌더링을 지연해야 한다.

---

### [핵심]

발생 원인:

- initialized 미사용
- `/me` 응답 전 비로그인 UI 렌더링
- user null 상태에서 role UI 판단
- token restore 전 route guard 실행
- PublicOnlyRoute와 ProtectedRoute 조건 충돌
- auth state와 persisted storage 불일치

방지 기준:

- initialized 전 route 판단 보류
- user 복원 전 role UI 판단 보류
- loading skeleton 사용
- auth restore 완료 후 main render
- token만 보고 UI 확정 금지

---

### [실무]

App Shell 예:

```tsx
function AppShell() {
  const { initialized } = useAuth();

  if (!initialized) {
    return <p>앱을 준비하는 중...</p>;
  }

  return <RouterProvider router={router} />;
}
```

Role UI 예:

```tsx
function AdminLink() {
  const { initialized, user } = useAuth();

  if (!initialized) {
    return null;
  }

  if (user?.role !== "ROLE_ADMIN") {
    return null;
  }

  return <Link to="/admin">Admin</Link>;
}
```

주의:

- 인증 확인 전 Header 메뉴 렌더링 주의
- user null은 비로그인과 로딩 중을 구분해야 함
- role 기반 메뉴는 initialized 이후 렌더링
- loading UI가 너무 길게 유지되면 `/me` 실패 처리 확인
- StrictMode effect 중복으로 flicker가 생기는지 확인

---

### [FAQ]

Q. 새로고침하면 잠깐 로그아웃 상태로 보여?
A. 인증 복원 완료 전 비로그인 UI가 렌더링되어 발생한다. initialized 상태로 렌더링을 지연해야 한다.

Q. 관리자 메뉴가 잠깐 보였다 사라져?
A. role 정보 복원 전에 조건부 렌더링이 잘못 실행되었을 가능성이 있다.

Q. 앱 전체를 initialized 전까지 숨겨도 돼?
A. 가능하다. 다만 사용자에게 짧은 loading UI를 제공하는 것이 좋다.

---

# 6. Me API Flow

## 6.1 Me API Purpose

### [개념]

Me API는 현재 로그인한 사용자의 정보를 조회하는 API다.

Frontend는 access token 또는 cookie 인증을 기반으로 `/me` API를 호출해 Auth State를 복원하거나 최신 사용자 정보를 확인한다.

---

### [핵심]

사용 상황:

- app initialization
- refresh auth restore
- login response lacks user
- profile page
- role check
- auth verification
- user summary refresh
- role update sync

기본 Flow:

```text
Stored Token Exists
→ Call /me
→ Success: Set User / Authenticated
→ 401: Clear Auth or Refresh
→ 403: Show Forbidden or Clear Auth by Policy
```

---

### [실무]

API 함수 예:

```tsx
export async function getMe() {
  const response = await authApi.get("/users/me");
  return response.data.data;
}
```

Auth Restore 연결:

```tsx
async function restoreAuth() {
  try {
    const user = await getMe();

    setUser(user);
    setAuthenticated(true);
  } catch {
    clearAuth();
  } finally {
    setInitialized(true);
  }
}
```

주의:

- `/me` API는 authApi 사용
- 로그인 직후 user 정보가 부족하면 `/me` 호출
- 새로고침 복원에서 `/me` 활용 가능
- 401이면 token 만료 또는 인증 실패
- 사용자 정보 DTO는 최소화
- role 정보 포함 여부 확인
- `/me` 응답 wrapper 구조 확인
- `/me` 실패 시 token 정리 또는 refresh flow 시도

---

### [FAQ]

Q. /me API는 언제 써?
A. 새로고침 후 인증 상태 복원, 로그인 응답에 사용자 정보가 부족한 경우, 최신 user profile 확인에 사용한다.

Q. 로그인 응답에 user가 있는데 /me API도 필요해?
A. 항상 필요하지는 않다. 하지만 새로고침 후 인증 상태 복원이나 최신 사용자 정보 확인에는 유용하다.

Q. /me API가 401이면 어떻게 해?
A. token이 유효하지 않은 상태로 보고 인증 정보를 정리하거나 refresh flow를 시도한다.

---

## 6.2 Me API Response Design

### [개념]

Me API Response Design은 Frontend Auth State를 채우기 위한 현재 사용자 응답 구조를 정의하는 기준이다.

Me API 응답은 Frontend 인증 상태와 Role Based UI가 필요한 최소 정보를 제공해야 한다.

---

### [핵심]

응답 필드 후보:

- userId
- email
- nickname
- role
- profileImageUrl
- provider
- verified
- status

필수 후보:

- userId
- nickname
- role

주의 후보:

- password
- refreshToken
- sensitive personal data
- unnecessary profile detail

---

### [실무]

권장 응답 예:

```json
{
  "success": true,
  "message": "현재 사용자 조회 성공",
  "data": {
    "userId": 1,
    "nickname": "jun",
    "role": "ROLE_USER",
    "profileImageUrl": "/images/profile/default.png"
  }
}
```

Frontend 타입 예:

```tsx
type MeResponse = {
  userId: number;
  nickname: string;
  role: "ROLE_USER" | "ROLE_ADMIN";
  profileImageUrl?: string;
};
```

처리 예:

```tsx
async function fetchMeAndSetAuth() {
  const me = await getMe();

  setUser({
    userId: me.userId,
    nickname: me.nickname,
    role: me.role,
    profileImageUrl: me.profileImageUrl,
  });

  setAuthenticated(true);
}
```

주의:

- role 누락 시 Role Based UI 불가
- email 표시가 필요 없으면 Auth State에 저장하지 않아도 됨
- 민감정보 포함 금지
- Backend DTO와 Frontend type 일치
- response.data.data unwrap 통일

---

### [FAQ]

Q. /me 응답에 role이 꼭 있어야 해?
A. Role Based UI나 Role Based Route를 구현하려면 role이 포함되는 것이 좋다.

Q. /me 응답에 accessToken도 넣어야 해?
A. 일반적으로 /me는 현재 사용자 정보 조회용이다. token 재발급은 refresh endpoint에서 분리하는 것이 좋다.

Q. /me 응답에 password가 오면?
A. 보안상 잘못된 응답이다. 비밀번호나 민감정보는 Frontend로 내려보내지 않아야 한다.

---

# 7. Auth State Troubleshooting

## 7.1 Auth State Mismatch

### [개념]

Auth State Mismatch는 token, user, authenticated 상태가 서로 일치하지 않아 UI와 API 요청 흐름이 꼬이는 문제다.

예를 들어 token은 있는데 authenticated false이거나, authenticated true인데 user가 null인 상태가 발생할 수 있다.

---

### [핵심]

대표 문제:

- token exists + authenticated false
- authenticated true + user null
- user role missing
- initialized false 유지
- loading true 유지
- token removed + authenticated true
- logout 후 user cache 유지
- login 실패 후 이전 user 유지
- refresh 실패 후 Auth State 미정리

---

### [실무]

Debug Flow:

```text
Auth 문제 발생
→ token storage 확인
→ Auth Store 확인
→ initialized 확인
→ authenticated 확인
→ user 확인
→ role 확인
→ /me 응답 확인
→ clearAuth 실행 여부 확인
→ route guard 조건 확인
```

문제 예:

```text
문제: token은 있는데 login으로 이동
원인: auth restore 완료 전 authenticated false 판단
해결: initialized false 동안 redirect 보류
```

문제 예:

```text
문제: 로그아웃했는데 사용자 이름이 Header에 남음
원인: user state 또는 query cache 정리 누락
해결: clearAuth와 user-specific cache cleanup 수행
```

주의:

- token과 Auth State를 별도 관리하면 불일치 가능
- clearAuth는 token, user, authenticated를 함께 정리
- login failure catch에서 기존 상태 유지 여부 검토
- refresh failure 시 clearAuth 필수
- Header, Route Guard, API Client가 같은 Auth 기준을 사용해야 함

---

### [FAQ]

Q. token은 있는데 login으로 보내져?
A. user 정보 복원 전 authenticated를 false로 판단했거나 `/me` 확인 loading을 기다리지 않았을 수 있다.

Q. 로그아웃했는데 화면에 닉네임이 남아?
A. user state나 query cache가 정리되지 않았을 가능성이 있다.

Q. authenticated true인데 user가 null이야?
A. Login Response 처리나 `/me` 복원 과정에서 user 설정이 누락되었을 가능성이 있다.

---

## 7.2 Initialized Never Ends

### [개념]

Initialized Never Ends는 앱 최초 인증 상태 확인이 끝나지 않아 loading 화면이 계속 유지되는 문제다.

대부분 `finally`에서 initialized를 true로 설정하지 않거나 `/me` 요청이 무한 대기하는 경우 발생한다.

---

### [핵심]

원인:

- finally 누락
- `/me` 요청 pending
- restoreAuth 내부 throw 후 처리 누락
- refresh loop
- interceptor deadlock
- AuthProvider remount 반복
- StrictMode effect 중복 처리 미흡
- condition return before setInitialized

---

### [실무]

안전한 초기화 예:

```tsx
useEffect(() => {
  let mounted = true;

  async function initializeAuth() {
    try {
      await restoreAuth();
    } catch {
      clearAuth();
    } finally {
      if (mounted) {
        setInitialized(true);
      }
    }
  }

  initializeAuth();

  return () => {
    mounted = false;
  };
}, []);
```

Debug Flow:

```text
Loading 계속 유지
→ initialized 값 확인
→ restoreAuth finally 확인
→ /me Network 상태 확인
→ refresh loop 여부 확인
→ AuthProvider remount 확인
→ interceptor에서 Promise 반환 확인
```

주의:

- early return 전에 initialized true 처리 필요
- refresh loop가 있으면 initialized가 끝나지 않을 수 있음
- interceptor에서 Promise를 반환하지 않으면 흐름이 멈출 수 있음
- AuthProvider 위치가 route 변경마다 remount되는지 확인
- StrictMode 환경에서 effect 중복 호출 고려

---

### [FAQ]

Q. 앱이 계속 인증 확인 중으로 멈춰?
A. restoreAuth의 finally에서 initialized를 true로 설정하지 않았거나 `/me` 요청이 끝나지 않았을 가능성이 있다.

Q. token이 없을 때도 initialized를 true로 해야 해?
A. 해야 한다. token이 없으면 비로그인 상태로 정리한 뒤 initialized true로 라우팅을 시작해야 한다.

Q. refresh loop가 initialized 문제를 만들 수 있어?
A. 가능하다. refresh 요청이 무한 반복되면 인증 초기화가 끝나지 않을 수 있다.

---

# 8. Part03 Review Checklist

## 8.1 Auth State / Restore Checklist

### [개념]

Part03 검수는 Auth State 구조, 초기 인증 복원, Auth Loading, `/me` API, user summary, role naming이 일관되게 연결되는지 확인한다.

---

### [핵심]

Checklist:

```md
- [ ] Auth State 목적이 명확한가?
- [ ] initialized / loading / authenticated 구분이 있는가?
- [ ] user summary 구조가 포함되었는가?
- [ ] role naming 기준이 포함되었는가?
- [ ] token 존재만으로 authenticated true 처리하지 않는 기준이 있는가?
- [ ] Auth State Lifecycle이 포함되었는가?
- [ ] Context Auth Store 기준이 포함되었는가?
- [ ] Zustand / Redux Auth Store 기준이 포함되었는가?
- [ ] Auth Restore on Refresh 흐름이 포함되었는가?
- [ ] Access Token 기반 복원 기준이 포함되었는가?
- [ ] Cookie Auth 기반 복원 기준이 포함되었는가?
- [ ] Auth Loading UX 기준이 포함되었는가?
- [ ] Auth Flicker Prevention 기준이 포함되었는가?
- [ ] /me API 목적과 응답 기준이 포함되었는가?
- [ ] Auth State Mismatch Troubleshooting이 포함되었는가?
- [ ] initialized never ends 문제 해결 기준이 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

Part03 이후 권장 문서 순서:

```text
Part03 Auth State / Auth Restore
→ Part04 Token Handling / Token Storage
→ Part05 Axios Auth Integration
→ Part06 Protected Route / Role Based Route
→ Part07 Logout / User Profile Fetch
→ Part08 OAuth2 Frontend Flow
→ Part09 401 / 403 / Troubleshooting
→ Part10 Security / Checklist / Retrieval Optimization
```

검수 기준:

```text
Auth State
→ Auth Store
→ Auth Restore
→ Auth Loading
→ User Summary
→ Me API
→ Troubleshooting
```

---

### [FAQ]

Q. Part03의 핵심은 뭐야?
A. Auth State 구조, initialized / loading / authenticated 구분, 새로고침 인증 복원, `/me` API 흐름을 정리하는 것이다.

Q. Part03에서 token 저장 보안을 깊게 다뤄?
A. 아니다. token 저장 위치와 보안 비교는 Token Handling / Token Storage 문서에서 자세히 다룬다.

Q. Part03에서 Protected Route를 깊게 다뤄?
A. 아니다. initialized를 Route Guard에서 사용하는 기준은 다루지만 Protected Route 상세 구현은 별도 문서에서 다룬다.

---

# Retrieval Queries

### [FAQ]

Q. Auth State에는 무엇이 들어가?
A. authenticated, initialized, loading, user, role, authError 같은 인증 상태 정보가 들어갈 수 있다.

Q. token이 있으면 authenticated true로 해도 돼?
A. 가능은 하지만 token이 만료되었거나 위조되었을 수 있으므로 `/me` 같은 API로 확인하는 흐름이 더 안전하다.

Q. user가 null인데 authenticated true여도 돼?
A. 권장하지 않는다. Role Based UI와 Protected Route가 불안정해지므로 user 복원 후 authenticated true로 처리하는 것이 좋다.

Q. initialized와 loading은 뭐가 달라?
A. initialized는 앱 최초 인증 확인이 끝났는지 나타내고 loading은 login, logout, `/me` 같은 인증 요청 진행 상태를 나타낸다.

Q. auth loading은 왜 필요해?
A. 새로고침 후 인증 상태 확인 전에 Protected Route가 login으로 잘못 redirect하는 것을 막기 위해 필요하다.

Q. Auth State는 Context로 관리해도 돼?
A. 가능하다. 프로젝트 규모가 작거나 인증 상태가 단순하면 Context 기반 AuthProvider가 충분할 수 있다.

Q. React에서 인증은 무조건 Redux로 해야 해?
A. 아니다. 프로젝트 규모에 따라 Context, Zustand, Redux Toolkit, TanStack Query 조합 중 선택할 수 있다.

Q. Zustand persist에 token을 저장해도 돼?
A. 가능은 하지만 XSS 위험이 있으므로 보안 요구사항에 따라 신중히 결정해야 한다.

Q. 새로고침하면 로그인이 풀려?
A. Auth State가 memory에만 있거나 초기 인증 복원 로직이 없으면 새로고침 시 로그인이 풀릴 수 있다.

Q. 새로고침 후 바로 login으로 튕겨?
A. 인증 상태 확인 loading을 기다리지 않고 Protected Route가 먼저 redirect했을 가능성이 있다.

Q. token은 있는데 왜 /me를 호출해?
A. token이 만료되었거나 위조되었을 수 있으므로 Backend 확인을 통해 실제 인증 상태와 사용자 정보를 복원하기 위해서다.

Q. localStorage에 token이 있는데 401이 나?
A. Network 탭에서 Authorization Header에 실제로 token이 포함되었는지 확인해야 한다.

Q. Bearer를 빼먹으면 어떻게 돼?
A. Backend가 token 형식을 인식하지 못해 401이 발생할 수 있다.

Q. access token만으로 새로고침 복원이 가능해?
A. 가능하지만 token이 만료되면 복원에 실패할 수 있으므로 refresh token flow를 함께 고려할 수 있다.

Q. HttpOnly Cookie를 쓰면 Frontend에서 token을 읽을 수 있어?
A. 아니다. HttpOnly Cookie는 JavaScript로 읽을 수 없고 Frontend는 `/me` API 응답으로 인증 상태를 확인한다.

Q. Cookie Auth에서도 /me API가 필요해?
A. 필요하다. Frontend가 로그인 상태와 사용자 정보를 복원하려면 Backend에 현재 사용자 정보를 요청해야 한다.

Q. withCredentials는 언제 필요해?
A. cross-origin 요청에서 cookie를 포함해야 할 때 필요할 수 있으며 Backend CORS 설정과 함께 맞춰야 한다.

Q. user 정보를 전부 저장해도 돼?
A. 권장하지 않는다. UI에 필요한 최소한의 user summary만 저장하는 것이 좋다.

Q. user summary에 role은 꼭 필요해?
A. Role Based UI나 Role Based Route를 사용한다면 필요하다.

Q. ROLE_ADMIN과 ADMIN은 같은 거야?
A. 프로젝트 기준에 따라 다르지만 문자열이 다르면 조건문에서 다르게 처리된다. naming을 통일해야 한다.

Q. 관리자 계정인데 관리자 메뉴가 안 보여?
A. user.role 값, role naming, Auth State 업데이트, 조건부 렌더링 조건을 확인해야 한다.

Q. Frontend에서 role check하면 보안이 돼?
A. 아니다. Frontend role check는 UX용이고 실제 권한 검증은 Backend에서 수행해야 한다.

Q. role이 없을 때 UI가 깜빡여?
A. Auth loading이 끝나기 전 조건부 렌더링이 실행되면 flicker가 생길 수 있다. initialized 상태를 사용해 제어한다.

Q. 새로고침하면 잠깐 로그아웃 상태로 보여?
A. 인증 복원 완료 전 비로그인 UI가 렌더링되어 발생한다. initialized 상태로 렌더링을 지연해야 한다.

Q. /me API는 언제 써?
A. 새로고침 후 인증 상태 복원, 로그인 응답에 사용자 정보가 부족한 경우, 최신 user profile 확인에 사용한다.

Q. 로그인 응답에 user가 있는데 /me API도 필요해?
A. 항상 필요하지는 않다. 하지만 새로고침 후 인증 상태 복원이나 최신 사용자 정보 확인에는 유용하다.

Q. /me API가 401이면 어떻게 해?
A. token이 유효하지 않은 상태로 보고 인증 정보를 정리하거나 refresh flow를 시도한다.

Q. /me 응답에 role이 꼭 있어야 해?
A. Role Based UI나 Role Based Route를 구현하려면 role이 포함되는 것이 좋다.

Q. /me 응답에 password가 오면?
A. 보안상 잘못된 응답이다. 비밀번호나 민감정보는 Frontend로 내려보내지 않아야 한다.

Q. token은 있는데 login으로 보내져?
A. user 정보 복원 전 authenticated를 false로 판단했거나 `/me` 확인 loading을 기다리지 않았을 수 있다.

Q. 로그아웃했는데 화면에 닉네임이 남아?
A. user state나 query cache가 정리되지 않았을 가능성이 있다.

Q. authenticated true인데 user가 null이야?
A. Login Response 처리나 `/me` 복원 과정에서 user 설정이 누락되었을 가능성이 있다.

Q. 앱이 계속 인증 확인 중으로 멈춰?
A. restoreAuth의 finally에서 initialized를 true로 설정하지 않았거나 `/me` 요청이 끝나지 않았을 가능성이 있다.

Q. token이 없을 때도 initialized를 true로 해야 해?
A. 해야 한다. token이 없으면 비로그인 상태로 정리한 뒤 initialized true로 라우팅을 시작해야 한다.

Q. Part03 다음 문서는 뭐야?
A. Token Handling / Token Storage 문서가 이어지는 것이 좋다.
