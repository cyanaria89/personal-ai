# Authentication Frontend Flow Part07 - Logout Flow / User Profile Fetch / Cache Cleanup

---

# 1. Logout Flow

## 1.1 Logout Flow Overview

### [개념]

Logout Flow는 사용자의 인증 상태를 종료하고 token, user state, authenticated state, user-specific cache, private page state를 정리하는 흐름이다.

Logout은 단순히 Access Token만 삭제하는 작업이 아니다.

Frontend Logout Flow는 Backend Logout API 호출 여부와 관계없이 local auth state cleanup을 안정적으로 수행해야 한다.

---

### [핵심]

기본 Flow:

```text
User Click Logout
→ Optional Logout API
→ Clear Access Token
→ Clear Refresh Token
→ Clear Auth State
→ Clear User State
→ Clear User-specific Cache
→ Clear Private Page State
→ Redirect Main or Login
```

핵심 키워드:

- Logout Flow
- Logout API
- Clear Token
- Clear Auth
- Clear User
- Auth State Reset
- Query Cache Cleanup
- Persisted Store Cleanup
- Notification State Cleanup
- Redirect After Logout
- Cross Tab Logout
- Refresh Token Invalidation
- Backend Logout
- Local Logout

---

### [실무]

2026 실무 기준 Logout Flow는 API 호출, 상태 정리, cache 정리, route 이동을 함께 처리한다.

예:

```tsx
async function handleLogout() {
  try {
    await logoutApi();
  } finally {
    clearTokens();
    clearAuthState();
    queryClient.clear();

    navigate("/login", { replace: true });
  }
}
```

권장 기준:

- logout API 실패 여부와 관계없이 local cleanup 수행 검토
- Access Token 제거
- Refresh Token 제거
- user state null 처리
- authenticated false 처리
- authError 초기화
- user-specific query cache 정리
- persisted auth store 정리
- notification / message / private data state 정리
- logout 후 private page history 접근 방지
- replace navigation 사용 고려
- 다른 탭 logout 동기화 검토

주의:

```text
token만 삭제
→ Header UI에 user 정보 남음
→ cache에 이전 사용자 데이터 남음
→ private page stale data 노출 가능
```

---

### [FAQ]

Q. 로그아웃할 때 token만 지우면 돼?
A. 아니다. user state, authenticated 상태, 사용자별 cache, persisted store도 함께 정리해야 한다.

Q. logout API가 실패하면 local token을 유지해야 해?
A. 프로젝트 정책에 따라 다르지만 사용자 입장에서는 로그아웃을 요청했으므로 local 인증 정보를 정리하는 경우가 많다.

Q. 로그아웃 후 어디로 이동해?
A. 프로젝트 기준에 따라 `/login`, `/`, 또는 public main page로 이동할 수 있다.

Q. logout 후 뒤로가기로 mypage가 보여?
A. replace navigation과 Protected Route, cache cleanup을 함께 확인해야 한다.

---

## 1.2 Local Logout and Backend Logout

### [개념]

Local Logout은 Frontend 저장소와 Auth State를 정리하는 작업이다.

Backend Logout은 서버에 저장된 Refresh Token, session, device token, push token 등을 무효화하는 작업이다.

JWT Access Token만 사용하는 구조에서는 Backend Logout API가 없을 수도 있다.

Refresh Token을 서버에서 관리한다면 Backend Logout API가 필요할 수 있다.

---

### [핵심]

Local Logout:

- Access Token 제거
- Refresh Token 제거
- Auth State 초기화
- User State 초기화
- Cache 정리
- Redirect 처리

Backend Logout:

- Refresh Token 무효화
- Refresh Token Rotation 상태 정리
- Server Session 만료
- Device Token 제거
- Remember Me Token 제거
- Logout Audit 기록

구분:

```text
Local Logout
→ Frontend 상태 정리

Backend Logout
→ 서버 인증 자원 무효화
```

---

### [실무]

Backend Logout API 사용 예:

```tsx
export async function logoutApi() {
  return authApi.post("/auth/logout");
}
```

Logout 처리 예:

```tsx
async function logout() {
  try {
    await logoutApi();
  } catch {
    // 서버 로그아웃 실패 여부는 정책에 따라 사용자에게 표시 가능
  } finally {
    clearAuth();
    clearUserCache();
  }
}
```

Backend Logout API가 없는 경우:

```tsx
function logoutLocalOnly() {
  clearAuth();
  clearUserCache();
  navigate("/login", { replace: true });
}
```

주의:

- Refresh Token이 서버 DB에 저장되면 logout API로 무효화 권장
- HttpOnly Cookie 기반이면 Backend에서 cookie 만료 응답 필요
- 서버 logout 실패 시 local cleanup 여부 정책 결정
- Access Token은 이미 발급된 경우 만료 전까지 유효할 수 있음
- 고보안 서비스는 token blacklist 또는 short-lived access token 검토
- Frontend는 token 검증과 무효화의 최종 책임자가 아님

---

### [FAQ]

Q. Logout API는 꼭 필요해?
A. Refresh Token이나 session을 서버에서 관리하면 필요할 수 있다. 단순 local token 제거만으로 충분한 구조도 있다.

Q. JWT는 로그아웃이 어려워?
A. 이미 발급된 Access Token은 만료 전까지 유효할 수 있으므로 짧은 만료 시간, refresh token 무효화, blacklist 같은 정책을 검토한다.

Q. HttpOnly Cookie 방식에서는 logout을 어떻게 해?
A. Backend Logout API가 cookie를 만료시키고 Frontend는 Auth State와 cache를 정리한다.

---

## 1.3 Logout Redirect

### [개념]

Logout Redirect는 logout 처리 후 사용자를 어느 화면으로 이동시킬지 결정하는 기준이다.

인증이 필요한 페이지에 남아 있으면 다시 Protected Route에 의해 login으로 이동할 수 있으므로 명확한 redirect 정책이 필요하다.

---

### [핵심]

Redirect 후보:

- `/login`
- `/`
- public main page
- logout complete page
- previous public page

권장 기준:

- replace navigation
- protected page history cleanup
- user-specific page 접근 방지
- redirect loop prevention
- logout message optional

---

### [실무]

Login Page 이동 예:

```tsx
navigate("/login", {
  replace: true,
  state: { message: "로그아웃되었습니다." },
});
```

Main Page 이동 예:

```tsx
navigate("/", { replace: true });
```

Protected Route와 연결:

```text
Logout
→ clearAuth
→ navigate("/login", replace)
→ user clicks back
→ ProtectedRoute checks authenticated false
→ login redirect 유지
```

주의:

- logout 후 mypage에 머물지 않음
- replace 옵션으로 history 정리
- logout message는 state 또는 toast로 전달 가능
- login page가 PublicOnlyRoute로 감싸져 있으면 authenticated false 상태 확인
- logout 직후 Auth State 정리보다 navigate가 먼저 실행되지 않도록 순서 주의

---

### [FAQ]

Q. 로그아웃 후 main으로 보내도 돼?
A. 가능하다. 다만 인증 필요 페이지에서 로그아웃했다면 public page 또는 login page로 보내는 것이 일반적이다.

Q. logout 후 뒤로가기를 누르면 이전 private page가 보여?
A. replace navigation, Protected Route, user cache cleanup이 제대로 동작하는지 확인해야 한다.

Q. 로그아웃 메시지는 어디서 보여줘?
A. login page state, toast, global notification 등 프로젝트 UX 기준에 맞춰 처리할 수 있다.

---

# 2. Logout Cleanup

## 2.1 Clear Auth State

### [개념]

Clear Auth State는 인증 관련 상태를 초기값으로 되돌리는 작업이다.

Clear Auth State는 token 제거뿐 아니라 user, authenticated, authError, loading, tokenExpired 상태를 함께 정리해야 한다.

---

### [핵심]

정리 대상:

- accessToken
- refreshToken
- user
- authenticated
- authError
- tokenExpired
- role
- initialized 유지 여부
- loading false
- persisted auth storage

Auth State 초기화 예:

```text
authenticated false
user null
authError null
tokenExpired false
loading false
initialized true
```

---

### [실무]

clearAuth 예:

```tsx
function clearAuth() {
  clearTokens();

  setAuthState({
    initialized: true,
    authenticated: false,
    loading: false,
    user: null,
    authError: null,
  });
}
```

Zustand 예:

```tsx
const useAuthStore = create<AuthStore>((set) => ({
  initialized: false,
  authenticated: false,
  user: null,

  clearAuth: () =>
    set({
      initialized: true,
      authenticated: false,
      user: null,
    }),
}));
```

주의:

- logout 시 initialized를 false로 되돌릴 필요는 보통 없음
- restoreAuth 중 실패 시 initialized true 처리 필요
- user null 처리 필수
- authenticated false 처리 필수
- role state가 별도라면 함께 초기화
- persisted auth store가 있으면 persist storage 정리
- clearAuth 후 인증 API 자동 호출이 다시 발생하지 않도록 의존성 확인

---

### [FAQ]

Q. clearAuth에서 initialized도 false로 바꿔?
A. 보통 logout이나 인증 실패 후에는 initialized true 상태에서 비로그인으로 처리한다.

Q. authenticated만 false로 바꾸면 돼?
A. 아니다. user, role, token, authError, user-specific cache도 함께 정리해야 한다.

Q. clearAuth 후 다시 /me API가 호출돼?
A. useEffect 의존성이나 AuthProvider 초기화 로직이 잘못되었을 수 있다.

---

## 2.2 Query Cache Cleanup

### [개념]

Query Cache Cleanup은 로그아웃 시 이전 사용자와 관련된 서버 상태 cache를 제거하는 작업이다.

TanStack Query, RTK Query, SWR 같은 server state cache에 사용자 데이터가 남아 있으면 로그아웃 후에도 이전 사용자 정보가 보일 수 있다.

---

### [핵심]

정리 대상:

- me query
- my profile query
- my favorites query
- notifications query
- private messages query
- my orders query
- user dashboard query
- role-specific query
- admin query
- owner-only resource cache

Cache 종류:

- TanStack Query cache
- RTK Query cache
- SWR cache
- custom memory cache
- persisted query cache

---

### [실무]

TanStack Query 전체 정리:

```tsx
queryClient.clear();
```

선택 정리:

```tsx
queryClient.removeQueries({ queryKey: ["me"] });
queryClient.removeQueries({ queryKey: ["myFavorites"] });
queryClient.removeQueries({ queryKey: ["notifications"] });
```

Logout 예:

```tsx
async function handleLogout() {
  try {
    await logoutApi();
  } finally {
    clearAuth();
    queryClient.clear();
    navigate("/login", { replace: true });
  }
}
```

주의:

- 전체 clear는 단순하지만 public cache도 제거됨
- 선택 remove는 정교하지만 누락 위험 있음
- 사용자별 query key 설계 필요
- cache persist 사용 시 persisted cache도 정리
- logout 후 이전 사용자 데이터 flicker 방지
- admin cache와 private cache 정리 필수
- mutation in-flight 상태 처리 검토

---

### [FAQ]

Q. 로그아웃할 때 query cache도 지워야 해?
A. 사용자별 데이터가 cache에 남을 수 있으므로 me, favorites, notifications 같은 private cache는 정리하는 것이 좋다.

Q. queryClient.clear()를 써도 돼?
A. 가능하다. 단순하지만 public cache까지 제거될 수 있으므로 프로젝트 규모에 따라 선택한다.

Q. 로그아웃했는데 이전 사용자 알림이 보여?
A. notification query cache나 notification state가 정리되지 않았을 가능성이 있다.

---

## 2.3 Persisted Store Cleanup

### [개념]

Persisted Store Cleanup은 Zustand Persist, Redux Persist, localStorage, sessionStorage 등에 남아 있는 인증 관련 상태를 제거하는 작업이다.

Persisted Store가 정리되지 않으면 새로고침 후 이전 사용자 인증 상태가 복원되는 문제가 발생할 수 있다.

---

### [핵심]

정리 대상:

- access token storage
- refresh token storage
- auth persist store
- user persist store
- role persist store
- query cache persist
- notification persist
- private page draft
- local user settings with sensitive data

---

### [실무]

Web Storage 정리:

```tsx
function clearTokens() {
  localStorage.removeItem("accessToken");
  localStorage.removeItem("refreshToken");
  sessionStorage.removeItem("accessToken");
  sessionStorage.removeItem("refreshToken");
}
```

Zustand persist 정리 예:

```tsx
function clearPersistedAuth() {
  localStorage.removeItem("auth-storage");
}
```

Redux Persist 정리 예:

```tsx
persistor.purge();
```

주의:

- persist key 이름 통일
- token과 user summary 저장 위치 확인
- query cache persist 사용 여부 확인
- logout 시 private draft 저장소 정리 여부 검토
- 공개 UI preference는 유지 가능
- 민감정보와 편의 설정을 구분
- storage cleanup 후 Auth State도 함께 정리

---

### [FAQ]

Q. Zustand persist를 쓰면 logout 때 뭘 지워야 해?
A. auth store의 persisted key, token storage, user summary, private cache를 정리해야 한다.

Q. localStorage만 지우면 store도 지워져?
A. 현재 메모리 store 상태는 남을 수 있으므로 store state도 함께 초기화해야 한다.

Q. public UI 설정도 logout 때 지워야 해?
A. 꼭 그렇지는 않다. 테마 같은 공개 설정은 유지하고 인증 관련 민감 상태만 지우는 방식도 가능하다.

---

# 3. User Profile Fetch

## 3.1 User Profile Fetch Overview

### [개념]

User Profile Fetch는 현재 로그인한 사용자의 정보를 Backend에서 조회하는 흐름이다.

Auth State에 저장하는 user summary와 profile page에서 사용하는 user detail은 분리하는 것이 좋다.

`/me` API는 인증 상태 복원과 기본 사용자 정보 확인에 사용하고, profile detail API는 마이페이지나 설정 화면에서 사용한다.

---

### [핵심]

구분:

```text
Me API
→ 인증 상태 복원
→ user summary
→ role
→ header / route guard용
```

```text
Profile API
→ 사용자 상세 정보
→ mypage
→ account settings
→ profile edit form
```

핵심 키워드:

- User Profile Fetch
- Me API
- Auth User
- User Summary
- User Detail
- My Profile
- Profile Page
- Auth Restore
- Role Based UI
- authApi
- response unwrap

---

### [실무]

Me API 예:

```tsx
export async function getMe() {
  const response = await authApi.get<ApiResponse<AuthUser>>("/users/me");

  return response.data.data;
}
```

Profile API 예:

```tsx
export async function getMyProfile() {
  const response =
    await authApi.get<ApiResponse<UserProfile>>("/users/me/profile");

  return response.data.data;
}
```

사용 기준:

```text
App Start
→ getMe
→ Auth State 복원

MyPage Mount
→ getMyProfile
→ Profile Detail 표시
```

주의:

- Auth State에는 최소 user summary만 저장
- profile detail은 필요한 화면에서 별도 조회
- role은 `/me` 응답에 포함 권장
- profile API는 authApi 사용
- response.data.data unwrap 기준 통일
- profile cache는 logout 시 정리
- 민감정보는 Frontend에 불필요하게 내려보내지 않음

---

### [FAQ]

Q. /me API와 profile API는 뭐가 달라?
A. /me API는 인증 상태 복원과 user summary용이고 profile API는 마이페이지 상세 정보 조회용이다.

Q. profile 정보를 전부 Auth State에 넣어도 돼?
A. 권장하지 않는다. Auth State에는 최소 정보만 넣고 profile page에서 상세 정보를 별도 조회하는 것이 좋다.

Q. profile API도 authApi를 써야 해?
A. 현재 로그인한 사용자 정보를 조회하므로 인증이 필요하며 authApi를 사용하는 것이 일반적이다.

---

## 3.2 Me API for Auth Restore

### [개념]

Me API for Auth Restore는 앱 시작 또는 새로고침 시 현재 사용자의 인증 상태를 확인하고 Auth State를 복원하는 흐름이다.

Frontend는 token 또는 cookie 존재만으로 로그인 상태를 확정하지 않고 `/me` API 응답으로 인증 상태를 확정할 수 있다.

---

### [핵심]

사용 상황:

- app initialization
- page refresh
- login response lacks user
- role refetch
- auth verification
- stale user update

기본 Flow:

```text
App Start
→ Check Token or Cookie
→ Call /me
→ Success: setUser + authenticated true
→ 401: clearAuth or refresh
→ finally: initialized true
```

---

### [실무]

restoreAuth 예:

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

refresh와 연결:

```text
App Start
→ Access Token expired
→ /me returns 401
→ Refresh Access Token
→ Retry /me
→ Success: restore auth
→ Failure: clearAuth
```

주의:

- `/me` API는 authApi 사용
- 401이면 refresh flow 또는 clearAuth
- 403은 일반적으로 권한 문제지만 `/me`에서는 정책 확인 필요
- initialized는 finally에서 true 처리
- role 누락 시 Role Based UI 불가
- user summary 응답은 최소화
- Auth Restore 중 loading UI 표시

---

### [FAQ]

Q. /me API는 언제 써?
A. 새로고침 후 인증 상태 복원, 로그인 응답에 사용자 정보가 부족한 경우, 최신 user profile 확인에 사용한다.

Q. 로그인 응답에 user가 있는데 /me API도 필요해?
A. 항상 필요하지는 않다. 하지만 새로고침 후 인증 상태 복원이나 최신 사용자 정보 확인에는 유용하다.

Q. /me API가 401이면 어떻게 해?
A. token이 유효하지 않은 상태로 보고 인증 정보를 정리하거나 refresh flow를 시도한다.

---

## 3.3 Profile Detail Fetch

### [개념]

Profile Detail Fetch는 마이페이지, 계정 설정, 프로필 수정 화면에서 필요한 상세 사용자 정보를 조회하는 흐름이다.

Profile Detail은 Auth State와 분리해 화면 단위 query로 관리하는 것이 좋다.

---

### [핵심]

Profile Detail 후보:

- userId
- email
- nickname
- profileImageUrl
- phone
- provider
- createdAt
- verified
- marketingAgreed
- notificationSettings
- public profile fields

제외 대상:

- password
- password hash
- refresh token
- internal security flags
- sensitive personal data
- unnecessary admin-only data

---

### [실무]

Profile 타입 예:

```tsx
type UserProfile = {
  userId: number;
  email: string;
  nickname: string;
  profileImageUrl?: string;
  provider?: "LOCAL" | "KAKAO" | "GOOGLE";
  verified: boolean;
};
```

Profile 조회 예:

```tsx
function MyProfilePage() {
  const { data, isLoading, error } = useQuery({
    queryKey: ["myProfile"],
    queryFn: getMyProfile,
  });

  if (isLoading) {
    return <p>프로필을 불러오는 중...</p>;
  }

  if (error) {
    return <p>프로필을 불러오지 못했습니다.</p>;
  }

  return <ProfileView profile={data} />;
}
```

주의:

- profile detail은 필요한 화면에서만 조회
- Auth State에 상세 profile을 과도하게 저장하지 않음
- profile query는 logout 시 정리
- profile update 후 `/me`와 profile cache 동기화 필요
- email / phone 같은 개인정보 표시 기준 확인
- Backend DTO에서 민감정보 제외
- provider별 수정 가능 필드가 다를 수 있음

---

### [FAQ]

Q. 마이페이지 정보는 /me로 충분해?
A. 간단한 정보는 가능하지만 상세 정보와 수정 화면은 별도 profile API를 두는 것이 관리하기 좋다.

Q. profile update 후 Header 닉네임이 안 바뀌어?
A. profile cache만 갱신하고 Auth State 또는 /me cache를 갱신하지 않았을 가능성이 있다.

Q. profile API 응답에 password hash가 있으면?
A. 심각한 보안 문제다. Backend 응답 DTO에서 제거해야 한다.

---

# 4. Profile Update and Auth State Sync

## 4.1 Profile Update Sync

### [개념]

Profile Update Sync는 사용자가 닉네임, 프로필 이미지 등 정보를 수정한 뒤 Auth State와 profile cache를 일관되게 갱신하는 기준이다.

Header, MyPage, Role Based UI가 서로 다른 사용자 정보를 보여주지 않도록 동기화가 필요하다.

---

### [핵심]

동기화 대상:

- Auth State user summary
- `/me` query cache
- myProfile query cache
- header user area
- profile page
- local persisted user
- notification user info

수정 후보:

- nickname
- profileImageUrl
- email
- password
- notification settings
- provider-linked info

---

### [실무]

Profile Update API 예:

```tsx
export async function updateMyProfile(requestBody: UpdateProfileRequest) {
  const response = await authApi.patch<ApiResponse<UserProfile>>(
    "/users/me/profile",
    requestBody,
  );

  return response.data.data;
}
```

업데이트 후 cache invalidation 예:

```tsx
async function handleProfileUpdate(values: UpdateProfileFormValues) {
  await updateMyProfile(toUpdateProfileRequest(values));

  await queryClient.invalidateQueries({ queryKey: ["myProfile"] });
  await queryClient.invalidateQueries({ queryKey: ["me"] });

  const me = await getMe();
  setUser(me);
}
```

직접 Auth State 갱신 예:

```tsx
setUser({
  ...user,
  nickname: updatedProfile.nickname,
  profileImageUrl: updatedProfile.profileImageUrl,
});
```

주의:

- Auth State와 profile cache 불일치 주의
- `/me` 응답과 profile 응답 필드 차이 확인
- nickname 변경 후 Header 즉시 갱신 필요
- profile image 변경 후 캐시 이미지 갱신 고려
- email 변경은 재인증 또는 인증 메일 필요 가능
- password 변경 후 logout 정책 검토
- provider login 사용자는 일부 필드 수정 제한 가능

---

### [FAQ]

Q. 프로필 수정 후 Header 닉네임이 그대로야?
A. Auth State user summary를 갱신하지 않았거나 `/me` cache를 invalidate하지 않았을 가능성이 있다.

Q. profile cache만 invalidate하면 충분해?
A. Header가 Auth State를 사용한다면 Auth State 또는 `/me` query도 함께 갱신해야 한다.

Q. 비밀번호 변경 후 자동 로그아웃해야 해?
A. 프로젝트 보안 정책에 따라 다르다. 보안 요구가 높으면 모든 token을 무효화하고 재로그인시키는 방식을 검토한다.

---

## 4.2 Account Status and Auth State

### [개념]

Account Status는 사용자의 계정 상태를 나타내는 값이다.

Frontend는 계정 상태에 따라 접근 제한, 안내 메시지, logout 처리, email verification flow를 구분할 수 있다.

---

### [핵심]

상태 후보:

- ACTIVE
- PENDING_EMAIL_VERIFICATION
- LOCKED
- DISABLED
- DELETED
- DORMANT
- SUSPENDED

처리 기준:

```text
ACTIVE
→ 정상 사용

PENDING_EMAIL_VERIFICATION
→ 인증 안내

LOCKED / DISABLED / SUSPENDED
→ 접근 제한

DELETED
→ logout / account unavailable
```

---

### [실무]

AuthUser 상태 포함 예:

```tsx
type AuthUser = {
  userId: number;
  nickname: string;
  role: "ROLE_USER" | "ROLE_ADMIN";
  status: "ACTIVE" | "PENDING_EMAIL_VERIFICATION" | "LOCKED" | "DISABLED";
};
```

Route 처리 예:

```tsx
function ActiveAccountRoute({ children }: { children: React.ReactNode }) {
  const { user } = useAuth();

  if (user?.status === "PENDING_EMAIL_VERIFICATION") {
    return <Navigate to="/verify-email" replace />;
  }

  if (user?.status === "LOCKED" || user?.status === "DISABLED") {
    return <Navigate to="/account-unavailable" replace />;
  }

  return children;
}
```

주의:

- 계정 상태의 최종 판단은 Backend 기준
- Frontend는 UX 안내와 route 분기만 담당
- 계정 잠김 / 비활성은 login response 또는 `/me`에서 명확히 전달
- status naming Backend와 통일
- 민감한 제한 사유를 과도하게 노출하지 않음
- 계정 상태 변경 후 Auth State 갱신 필요

---

### [FAQ]

Q. 이메일 인증 전 사용자는 authenticated true야?
A. 프로젝트 정책에 따라 다르다. 인증 전에도 로그인은 허용하되 특정 기능만 제한하거나, 로그인 자체를 제한할 수 있다.

Q. 계정이 잠긴 사용자는 어떻게 처리해?
A. Backend 응답 기준으로 접근 제한 안내를 보여주고 필요하면 logout 또는 account unavailable page로 이동시킨다.

Q. 계정 상태도 Frontend에서 최종 판단해?
A. 아니다. Frontend는 UX 분기용으로 사용하고 최종 접근 제어는 Backend가 수행해야 한다.

---

# 5. Private Data State Cleanup

## 5.1 Private Page State Cleanup

### [개념]

Private Page State Cleanup은 로그아웃 또는 인증 만료 시 private page에 남아 있는 사용자별 화면 상태를 정리하는 기준이다.

사용자별 draft, form, selected item, notification count, private message state가 남으면 다른 사용자에게 이전 정보가 보일 수 있다.

---

### [핵심]

정리 대상:

- private form draft
- profile edit draft
- notification count
- unread message count
- selected private tab
- admin filter state
- user dashboard state
- private modal state
- uploaded temp file state
- websocket subscription state

---

### [실무]

Private State Store 예:

```tsx
type PrivateUiStore = {
  notificationCount: number;
  selectedPrivateTab: string | null;
  resetPrivateUi: () => void;
};

const usePrivateUiStore = create<PrivateUiStore>((set) => ({
  notificationCount: 0,
  selectedPrivateTab: null,

  resetPrivateUi: () =>
    set({
      notificationCount: 0,
      selectedPrivateTab: null,
    }),
}));
```

Logout 시 호출:

```tsx
function clearPrivateState() {
  usePrivateUiStore.getState().resetPrivateUi();
  queryClient.clear();
}
```

주의:

- Auth State만 정리하면 private UI state가 남을 수 있음
- 알림 / 채팅 / 대시보드 상태 정리 필요
- WebSocket 연결 종료 필요 가능
- Form draft는 민감정보 포함 여부 확인
- admin page filter도 사용자별 상태일 수 있음
- 다른 사용자 로그인 시 이전 state 재사용 방지

---

### [FAQ]

Q. 로그아웃 후 이전 사용자 알림 숫자가 보여?
A. notification state나 query cache가 정리되지 않았을 가능성이 있다.

Q. private form draft도 logout 때 지워야 해?
A. 민감정보가 포함될 수 있으므로 logout 시 정리하는 것이 안전하다.

Q. WebSocket 연결도 logout 때 끊어야 해?
A. 인증 사용자 전용 구독이면 logout 시 연결 해제 또는 재구독 정리가 필요하다.

---

## 5.2 WebSocket and Subscription Cleanup

### [개념]

WebSocket and Subscription Cleanup은 로그아웃 또는 인증 만료 시 인증 사용자 전용 실시간 연결과 구독을 정리하는 기준이다.

인증이 필요한 채팅, 알림, 실시간 업데이트 구독은 logout 후 유지되면 안 된다.

---

### [핵심]

정리 대상:

- WebSocket connection
- STOMP subscription
- notification subscription
- private chat subscription
- SSE connection
- polling interval
- background refetch
- authenticated room subscription

---

### [실무]

WebSocket cleanup 예:

```tsx
function cleanupRealtimeConnections() {
  notificationSubscription?.unsubscribe();
  chatSubscription?.unsubscribe();
  stompClient?.disconnect();
}
```

Logout 연결:

```tsx
async function handleLogout() {
  try {
    await logoutApi();
  } finally {
    cleanupRealtimeConnections();
    clearAuth();
    queryClient.clear();
    navigate("/login", { replace: true });
  }
}
```

Polling cleanup 예:

```tsx
useEffect(() => {
  if (!authenticated) {
    return;
  }

  const timerId = window.setInterval(fetchNotifications, 30000);

  return () => {
    window.clearInterval(timerId);
  };
}, [authenticated]);
```

주의:

- logout 후 인증 WebSocket 유지 금지
- notification subscription 정리
- private chat room subscription 정리
- polling interval 정리
- token 만료 시 재연결 loop 주의
- 다른 사용자 로그인 시 이전 구독 재사용 금지
- reconnect 로직이 logout 후 실행되지 않도록 조건 확인

---

### [FAQ]

Q. 로그아웃했는데 알림 WebSocket이 계속 연결돼?
A. logout cleanup에서 subscription unsubscribe와 client disconnect가 누락되었을 가능성이 있다.

Q. token 만료 후 WebSocket이 계속 재연결돼?
A. reconnect 조건에서 authenticated 상태를 확인하지 않았을 수 있다.

Q. 다른 사용자로 로그인했는데 이전 채팅 알림이 와?
A. 이전 WebSocket subscription이나 private cache가 정리되지 않았을 가능성이 있다.

---

# 6. Cross Tab Logout

## 6.1 Cross Tab Logout Sync

### [개념]

Cross Tab Logout Sync는 여러 브라우저 탭이 열려 있을 때 한 탭에서 로그아웃하면 다른 탭도 비로그인 상태로 동기화하는 흐름이다.

localStorage storage event 또는 BroadcastChannel을 사용해 logout 이벤트를 전달할 수 있다.

---

### [핵심]

사용 상황:

- multiple tabs
- logout in one tab
- token removed
- other tab still authenticated
- storage event
- BroadcastChannel
- auth state sync
- clearAuth sync
- private cache cleanup

---

### [실무]

storage event 예:

```tsx
const LOGOUT_EVENT_KEY = "auth:logout";

function broadcastLogout() {
  localStorage.setItem(LOGOUT_EVENT_KEY, String(Date.now()));
}

useEffect(() => {
  function handleStorageChange(event: StorageEvent) {
    if (event.key === LOGOUT_EVENT_KEY) {
      clearAuth();
      queryClient.clear();
    }
  }

  window.addEventListener("storage", handleStorageChange);

  return () => {
    window.removeEventListener("storage", handleStorageChange);
  };
}, []);
```

BroadcastChannel 예:

```tsx
const authChannel = new BroadcastChannel("auth");

function broadcastLogout() {
  authChannel.postMessage({ type: "LOGOUT" });
}

authChannel.onmessage = (event) => {
  if (event.data?.type === "LOGOUT") {
    clearAuth();
    queryClient.clear();
  }
};
```

주의:

- localStorage storage event는 같은 탭에서는 발생하지 않음
- sessionStorage는 탭 간 공유되지 않음
- BroadcastChannel 지원 범위 확인
- 같은 탭 logout은 직접 clearAuth 수행
- 다른 탭에서는 route redirect도 필요 가능
- private cache도 함께 정리
- 단순 프로젝트에서는 우선순위를 낮출 수 있음

---

### [FAQ]

Q. 한 탭에서 로그아웃했는데 다른 탭은 로그인 상태야?
A. 탭 간 인증 상태 동기화가 없으면 발생할 수 있다. storage event나 BroadcastChannel을 사용할 수 있다.

Q. sessionStorage를 쓰면 탭 간 로그아웃 동기화가 돼?
A. 기본적으로 어렵다. sessionStorage는 탭 단위 저장소이므로 별도 broadcast가 필요하다.

Q. Cross Tab Logout은 필수야?
A. 실서비스 UX에서는 유용하지만 단순 학습 프로젝트에서는 우선순위를 낮출 수 있다.

---

## 6.2 Cross Tab Token Expired Sync

### [개념]

Cross Tab Token Expired Sync는 한 탭에서 refresh 실패나 인증 만료가 발생했을 때 다른 탭에도 인증 만료 상태를 전달하는 흐름이다.

Logout Sync와 유사하지만 사용자가 직접 logout하지 않은 인증 만료 상황도 포함한다.

---

### [핵심]

사용 상황:

- refresh failure
- token expired
- auth expired event
- multiple tabs
- clearAuth all tabs
- login redirect all tabs
- stale auth prevention

Flow:

```text
Tab A API Request
→ Refresh Failed
→ clearAuth in Tab A
→ Broadcast AUTH_EXPIRED
→ Tab B receives event
→ clearAuth in Tab B
→ redirect login if needed
```

---

### [실무]

Auth Expired Broadcast 예:

```tsx
const AUTH_EXPIRED_EVENT_KEY = "auth:expired";

function broadcastAuthExpired() {
  localStorage.setItem(AUTH_EXPIRED_EVENT_KEY, String(Date.now()));
}

function handleAuthExpiredAcrossTabs(event: StorageEvent) {
  if (event.key !== AUTH_EXPIRED_EVENT_KEY) {
    return;
  }

  clearAuth();
  queryClient.clear();
}
```

Interceptor 연결:

```tsx
catch (refreshError) {
  clearAuth();
  broadcastAuthExpired();

  return Promise.reject(refreshError);
}
```

주의:

- refresh 실패 시 모든 탭 인증 상태 정리
- 현재 탭은 storage event를 받지 않으므로 직접 clearAuth
- 다른 탭 redirect는 Router 계층과 연결
- 반복 broadcast 방지
- auth expired와 manual logout 메시지 구분 가능
- login page에 이미 있으면 중복 redirect 방지

---

### [FAQ]

Q. 한 탭에서 refresh 실패했는데 다른 탭은 계속 로그인 상태야?
A. Cross Tab Auth Expired Sync가 없으면 발생할 수 있다. storage event나 BroadcastChannel로 인증 만료를 전파할 수 있다.

Q. auth expired와 logout을 같은 이벤트로 처리해도 돼?
A. 가능하지만 사용자 메시지가 다를 수 있으므로 구분하면 UX가 더 명확하다.

Q. 다른 탭도 login으로 보내야 해?
A. 인증이 만료되었다면 private page에 남지 않도록 login redirect 또는 public page 이동을 처리하는 것이 좋다.

---

# 7. Logout / Profile Troubleshooting

## 7.1 Logout State Remains

### [개념]

Logout State Remains는 로그아웃 후에도 이전 사용자 정보, 메뉴, 알림, private data가 화면에 남아 있는 문제다.

대부분 Auth State, query cache, persisted store, private UI state 중 일부가 정리되지 않아 발생한다.

---

### [핵심]

원인:

- user state 정리 누락
- authenticated false 누락
- query cache cleanup 누락
- persisted store cleanup 누락
- notification state cleanup 누락
- WebSocket subscription 유지
- Header가 stale user 사용
- profile cache 유지
- cross tab sync 없음

---

### [실무]

Debug Flow:

```text
Logout 후 사용자 정보 남음
→ Auth State 확인
→ user null 확인
→ authenticated false 확인
→ token storage 확인
→ query cache 확인
→ persisted store 확인
→ notification state 확인
→ WebSocket subscription 확인
→ Header rendering source 확인
```

문제 예:

```text
문제: logout 후 Header 닉네임이 남음
원인: user state 정리 누락
해결: clearAuth에서 user null 처리
```

문제 예:

```text
문제: logout 후 알림 개수가 남음
원인: notification query cache 또는 store 정리 누락
해결: queryClient.clear 또는 notification state reset
```

주의:

- token 제거만 확인하지 말고 UI state 확인
- Header가 Auth State와 query cache 중 무엇을 참조하는지 확인
- logout cleanup 순서 확인
- private cache가 persist 되는지 확인
- 다른 탭 상태도 확인

---

### [FAQ]

Q. 로그아웃했는데 화면에 닉네임이 남아?
A. user state나 query cache가 정리되지 않았을 가능성이 있다.

Q. 로그아웃했는데 이전 사용자 알림이 보여?
A. notification state나 query cache가 정리되지 않았을 가능성이 있다.

Q. token은 지워졌는데 로그인 상태로 보여?
A. authenticated state나 persisted auth store가 정리되지 않았을 가능성이 있다.

---

## 7.2 Profile Data Stale

### [개념]

Profile Data Stale은 프로필 수정 후 Header, MyPage, Auth State, `/me` cache가 서로 다른 사용자 정보를 보여주는 문제다.

profile update 후 관련 cache와 Auth State를 함께 갱신하지 않으면 발생한다.

---

### [핵심]

원인:

- myProfile cache만 갱신
- `/me` cache 미갱신
- Auth State user summary 미갱신
- Header가 stale user 참조
- profile image cache 문제
- Backend 응답 필드 누락
- update response와 AuthUser 타입 불일치

---

### [실무]

Debug Flow:

```text
Profile 수정 후 UI 불일치
→ update API 응답 확인
→ myProfile query 확인
→ /me query 확인
→ Auth State user 확인
→ Header source 확인
→ query invalidate 확인
→ setUser 호출 확인
```

해결 예:

```tsx
await updateMyProfile(requestBody);

const me = await getMe();

setUser(me);
queryClient.invalidateQueries({ queryKey: ["myProfile"] });
queryClient.invalidateQueries({ queryKey: ["me"] });
```

주의:

- update response가 profile detail이면 AuthUser로 직접 쓰기 어려울 수 있음
- Header가 Auth State를 사용하면 setUser 필요
- Header가 `/me` query를 사용하면 `/me` invalidate 필요
- 이미지 URL이 같으면 브라우저 cache로 갱신이 안 보일 수 있음
- role 변경은 별도 권한 갱신 정책 필요

---

### [FAQ]

Q. 프로필 수정 후 Header 닉네임이 그대로야?
A. Auth State user summary를 갱신하지 않았거나 `/me` cache를 invalidate하지 않았을 가능성이 있다.

Q. MyPage는 바뀌었는데 Header는 안 바뀌어?
A. MyPage는 profile query를 사용하고 Header는 Auth State를 사용하기 때문에 둘을 함께 갱신해야 한다.

Q. 프로필 이미지가 바뀌지 않아?
A. 이미지 URL이 같아서 브라우저 cache가 유지되었거나 Auth State/profile cache가 갱신되지 않았을 수 있다.

---

## 7.3 Logout Redirect Loop

### [개념]

Logout Redirect Loop는 로그아웃 후 login, main, protected page 사이에서 redirect가 반복되는 문제다.

대부분 clearAuth 순서, PublicOnlyRoute 조건, ProtectedRoute 조건, redirect target 설정이 충돌해 발생한다.

---

### [핵심]

원인:

- navigate가 clearAuth보다 먼저 실행
- authenticated false 처리 지연
- login page가 ProtectedRoute 내부
- redirect target이 private page로 고정
- PublicOnlyRoute가 stale authenticated true 사용
- persisted auth store 미정리
- initialized false 유지

---

### [실무]

Debug Flow:

```text
Logout redirect loop 발생
→ clearAuth 호출 순서 확인
→ authenticated false 확인
→ initialized true 확인
→ navigate target 확인
→ login route guard 확인
→ protected route guard 확인
→ persisted auth storage 확인
```

권장 순서:

```text
Logout Click
→ logout API optional
→ clearAuth
→ clear cache
→ broadcast logout
→ navigate public route
```

주의:

- clearAuth 전에 private route로 navigate하지 않음
- logout 후 redirect target을 login 또는 public route로 명확화
- login page를 ProtectedRoute로 감싸지 않음
- PublicOnlyRoute는 initialized 이후 판단
- stale persisted auth가 다시 authenticated true로 복원되지 않도록 정리

---

### [FAQ]

Q. 로그아웃 후 login과 main을 왔다 갔다 해?
A. clearAuth 순서, PublicOnlyRoute 조건, persisted auth store 정리 여부를 확인해야 한다.

Q. 로그아웃 후 다시 로그인 상태로 복원돼?
A. localStorage, Zustand persist, query persist 등 저장소에 이전 auth 정보가 남아 있을 수 있다.

Q. logout 후 private page로 다시 이동해?
A. redirect target이나 history가 private page를 가리키고 있을 수 있다. replace navigation과 Protected Route를 확인해야 한다.

---

# 8. Part07 Review Checklist

## 8.1 Logout / User Profile Checklist

### [개념]

Part07 검수는 Logout Flow, Auth State Cleanup, Query Cache Cleanup, Persisted Store Cleanup, User Profile Fetch, Profile Update Sync, Cross Tab Logout이 일관되게 연결되는지 확인한다.

---

### [핵심]

Checklist:

```md
- [ ] Logout Flow 목적이 명확한가?
- [ ] token만 삭제하면 부족하다는 기준이 포함되었는가?
- [ ] Local Logout과 Backend Logout 차이가 포함되었는가?
- [ ] Logout Redirect 기준이 포함되었는가?
- [ ] Clear Auth State 기준이 포함되었는가?
- [ ] Query Cache Cleanup 기준이 포함되었는가?
- [ ] Persisted Store Cleanup 기준이 포함되었는가?
- [ ] Private Page State Cleanup 기준이 포함되었는가?
- [ ] WebSocket / Subscription Cleanup 기준이 포함되었는가?
- [ ] Cross Tab Logout Sync 기준이 포함되었는가?
- [ ] Cross Tab Token Expired Sync 기준이 포함되었는가?
- [ ] Me API와 Profile API 차이가 포함되었는가?
- [ ] User Summary와 User Detail 차이가 포함되었는가?
- [ ] Profile Detail Fetch 기준이 포함되었는가?
- [ ] Profile Update 후 Auth State Sync 기준이 포함되었는가?
- [ ] Account Status 처리 기준이 포함되었는가?
- [ ] Logout State Remains Troubleshooting이 포함되었는가?
- [ ] Profile Data Stale Troubleshooting이 포함되었는가?
- [ ] Logout Redirect Loop Troubleshooting이 포함되었는가?
- [ ] Backend Authorization / Backend Logout 책임 구분이 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

Part07 이후 권장 문서 순서:

```text
Part07 Logout / User Profile Fetch
→ Part08 OAuth2 Frontend Flow
→ Part09 401 / 403 / Troubleshooting
→ Part10 Security / Checklist / Retrieval Optimization
```

검수 기준:

```text
Logout
→ Clear Auth
→ Clear Cache
→ Clear Private State
→ Redirect
→ Profile Fetch
→ Profile Sync
→ Troubleshooting
```

---

### [FAQ]

Q. Part07의 핵심은 뭐야?
A. logout 시 token, user state, cache, persisted store, private state를 정리하고 profile fetch와 Auth State sync 기준을 정리하는 것이다.

Q. Part07에서 OAuth2 Logout까지 다뤄?
A. 일반 logout 기준은 포함하지만 OAuth2 provider logout이나 social account unlink는 OAuth2 문서에서 별도로 다루는 것이 좋다.

Q. Part07 다음 문서는 뭐야?
A. OAuth2 Frontend Flow 문서가 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. 로그아웃할 때 token만 지우면 돼?
A. 아니다. user state, authenticated 상태, 사용자별 cache, persisted store도 함께 정리해야 한다.

Q. logout API가 실패하면 local token을 유지해야 해?
A. 프로젝트 정책에 따라 다르지만 사용자 입장에서는 로그아웃을 요청했으므로 local 인증 정보를 정리하는 경우가 많다.

Q. 로그아웃 후 어디로 이동해?
A. 프로젝트 기준에 따라 `/login`, `/`, 또는 public main page로 이동할 수 있다.

Q. logout 후 뒤로가기로 mypage가 보여?
A. replace navigation과 Protected Route, cache cleanup을 함께 확인해야 한다.

Q. Logout API는 꼭 필요해?
A. Refresh Token이나 session을 서버에서 관리하면 필요할 수 있다. 단순 local token 제거만으로 충분한 구조도 있다.

Q. JWT는 로그아웃이 어려워?
A. 이미 발급된 Access Token은 만료 전까지 유효할 수 있으므로 짧은 만료 시간, refresh token 무효화, blacklist 같은 정책을 검토한다.

Q. HttpOnly Cookie 방식에서는 logout을 어떻게 해?
A. Backend Logout API가 cookie를 만료시키고 Frontend는 Auth State와 cache를 정리한다.

Q. 로그아웃 후 main으로 보내도 돼?
A. 가능하다. 다만 인증 필요 페이지에서 로그아웃했다면 public page 또는 login page로 보내는 것이 일반적이다.

Q. clearAuth에서 initialized도 false로 바꿔?
A. 보통 logout이나 인증 실패 후에는 initialized true 상태에서 비로그인으로 처리한다.

Q. authenticated만 false로 바꾸면 돼?
A. 아니다. user, role, token, authError, user-specific cache도 함께 정리해야 한다.

Q. clearAuth 후 다시 /me API가 호출돼?
A. useEffect 의존성이나 AuthProvider 초기화 로직이 잘못되었을 수 있다.

Q. 로그아웃할 때 query cache도 지워야 해?
A. 사용자별 데이터가 cache에 남을 수 있으므로 me, favorites, notifications 같은 private cache는 정리하는 것이 좋다.

Q. queryClient.clear()를 써도 돼?
A. 가능하다. 단순하지만 public cache까지 제거될 수 있으므로 프로젝트 규모에 따라 선택한다.

Q. 로그아웃했는데 이전 사용자 알림이 보여?
A. notification query cache나 notification state가 정리되지 않았을 가능성이 있다.

Q. Zustand persist를 쓰면 logout 때 뭘 지워야 해?
A. auth store의 persisted key, token storage, user summary, private cache를 정리해야 한다.

Q. localStorage만 지우면 store도 지워져?
A. 현재 메모리 store 상태는 남을 수 있으므로 store state도 함께 초기화해야 한다.

Q. public UI 설정도 logout 때 지워야 해?
A. 꼭 그렇지는 않다. 테마 같은 공개 설정은 유지하고 인증 관련 민감 상태만 지우는 방식도 가능하다.

Q. /me API와 profile API는 뭐가 달라?
A. /me API는 인증 상태 복원과 user summary용이고 profile API는 마이페이지 상세 정보 조회용이다.

Q. profile 정보를 전부 Auth State에 넣어도 돼?
A. 권장하지 않는다. Auth State에는 최소 정보만 넣고 profile page에서 상세 정보를 별도 조회하는 것이 좋다.

Q. profile API도 authApi를 써야 해?
A. 현재 로그인한 사용자 정보를 조회하므로 인증이 필요하며 authApi를 사용하는 것이 일반적이다.

Q. /me API는 언제 써?
A. 새로고침 후 인증 상태 복원, 로그인 응답에 사용자 정보가 부족한 경우, 최신 user profile 확인에 사용한다.

Q. 로그인 응답에 user가 있는데 /me API도 필요해?
A. 항상 필요하지는 않다. 하지만 새로고침 후 인증 상태 복원이나 최신 사용자 정보 확인에는 유용하다.

Q. /me API가 401이면 어떻게 해?
A. token이 유효하지 않은 상태로 보고 인증 정보를 정리하거나 refresh flow를 시도한다.

Q. 마이페이지 정보는 /me로 충분해?
A. 간단한 정보는 가능하지만 상세 정보와 수정 화면은 별도 profile API를 두는 것이 관리하기 좋다.

Q. profile update 후 Header 닉네임이 안 바뀌어?
A. profile cache만 갱신하고 Auth State 또는 /me cache를 갱신하지 않았을 가능성이 있다.

Q. profile API 응답에 password hash가 있으면?
A. 심각한 보안 문제다. Backend 응답 DTO에서 제거해야 한다.

Q. 프로필 수정 후 Header 닉네임이 그대로야?
A. Auth State user summary를 갱신하지 않았거나 `/me` cache를 invalidate하지 않았을 가능성이 있다.

Q. profile cache만 invalidate하면 충분해?
A. Header가 Auth State를 사용한다면 Auth State 또는 `/me` query도 함께 갱신해야 한다.

Q. 비밀번호 변경 후 자동 로그아웃해야 해?
A. 프로젝트 보안 정책에 따라 다르다. 보안 요구가 높으면 모든 token을 무효화하고 재로그인시키는 방식을 검토한다.

Q. 이메일 인증 전 사용자는 authenticated true야?
A. 프로젝트 정책에 따라 다르다. 인증 전에도 로그인은 허용하되 특정 기능만 제한하거나, 로그인 자체를 제한할 수 있다.

Q. 계정이 잠긴 사용자는 어떻게 처리해?
A. Backend 응답 기준으로 접근 제한 안내를 보여주고 필요하면 logout 또는 account unavailable page로 이동시킨다.

Q. private form draft도 logout 때 지워야 해?
A. 민감정보가 포함될 수 있으므로 logout 시 정리하는 것이 안전하다.

Q. WebSocket 연결도 logout 때 끊어야 해?
A. 인증 사용자 전용 구독이면 logout 시 연결 해제 또는 재구독 정리가 필요하다.

Q. 로그아웃했는데 알림 WebSocket이 계속 연결돼?
A. logout cleanup에서 subscription unsubscribe와 client disconnect가 누락되었을 가능성이 있다.

Q. token 만료 후 WebSocket이 계속 재연결돼?
A. reconnect 조건에서 authenticated 상태를 확인하지 않았을 수 있다.

Q. 다른 사용자로 로그인했는데 이전 채팅 알림이 와?
A. 이전 WebSocket subscription이나 private cache가 정리되지 않았을 가능성이 있다.

Q. 한 탭에서 로그아웃했는데 다른 탭은 로그인 상태야?
A. 탭 간 인증 상태 동기화가 없으면 발생할 수 있다. storage event나 BroadcastChannel을 사용할 수 있다.

Q. sessionStorage를 쓰면 탭 간 로그아웃 동기화가 돼?
A. 기본적으로 어렵다. sessionStorage는 탭 단위 저장소이므로 별도 broadcast가 필요하다.

Q. 한 탭에서 refresh 실패했는데 다른 탭은 계속 로그인 상태야?
A. Cross Tab Auth Expired Sync가 없으면 발생할 수 있다. storage event나 BroadcastChannel로 인증 만료를 전파할 수 있다.

Q. auth expired와 logout을 같은 이벤트로 처리해도 돼?
A. 가능하지만 사용자 메시지가 다를 수 있으므로 구분하면 UX가 더 명확하다.

Q. 로그아웃했는데 화면에 닉네임이 남아?
A. user state나 query cache가 정리되지 않았을 가능성이 있다.

Q. token은 지워졌는데 로그인 상태로 보여?
A. authenticated state나 persisted auth store가 정리되지 않았을 가능성이 있다.

Q. MyPage는 바뀌었는데 Header는 안 바뀌어?
A. MyPage는 profile query를 사용하고 Header는 Auth State를 사용하기 때문에 둘을 함께 갱신해야 한다.

Q. 프로필 이미지가 바뀌지 않아?
A. 이미지 URL이 같아서 브라우저 cache가 유지되었거나 Auth State/profile cache가 갱신되지 않았을 수 있다.

Q. 로그아웃 후 login과 main을 왔다 갔다 해?
A. clearAuth 순서, PublicOnlyRoute 조건, persisted auth store 정리 여부를 확인해야 한다.

Q. 로그아웃 후 다시 로그인 상태로 복원돼?
A. localStorage, Zustand persist, query persist 등 저장소에 이전 auth 정보가 남아 있을 수 있다.

Q. Part07 다음 문서는 뭐야?
A. OAuth2 Frontend Flow 문서가 이어지는 것이 좋다.
