# Authentication Frontend Flow Part09 - 401 / 403 Handling / Auth Troubleshooting

---

# 1. 401 / 403 Overview

## 1.1 401 Unauthorized vs 403 Forbidden

### [개념]

401 Unauthorized는 사용자가 인증되지 않았거나 Access Token이 유효하지 않을 때 발생하는 응답이다.

403 Forbidden은 사용자가 인증은 되었지만 해당 리소스나 기능에 접근할 권한이 없을 때 발생하는 응답이다.

Frontend는 401과 403을 반드시 구분해서 처리해야 한다.

401은 인증 문제이고 403은 권한 문제다.

---

### [핵심]

비교:

| Status | 의미                    | 대표 원인                                                     | Frontend 처리                        |
| -----: | ----------------------- | ------------------------------------------------------------- | ------------------------------------ |
|    401 | 인증 실패 / 로그인 필요 | token 없음, token 만료, token 위조, Authorization Header 누락 | refresh 시도 또는 login redirect     |
|    403 | 권한 부족               | role 부족, 소유자 불일치, 관리자 권한 없음                    | forbidden page 또는 권한 없음 메시지 |

핵심 키워드:

- 401 Unauthorized
- 403 Forbidden
- Authentication Failure
- Authorization Failure
- Token Missing
- Token Expired
- Bearer Token
- Authorization Header
- Refresh Token
- Login Redirect
- Forbidden Page
- Permission Denied
- Role Based Route
- Backend Authorization
- Auth Troubleshooting

---

### [실무]

기본 분기:

```text
401 Unauthorized
→ 인증되지 않음
→ token 없음 / 만료 / 위조 가능
→ refresh token flow 시도
→ 실패 시 clearAuth
→ login redirect
```

```text
403 Forbidden
→ 인증은 되었음
→ 권한 부족
→ Auth State 유지
→ forbidden page 또는 권한 없음 메시지
```

주의:

- 401과 403을 같은 방식으로 처리하지 않음
- 403에서 기본 logout 처리 금지
- 401에서 refresh 가능 여부 확인
- Login API 실패 401과 Token Expired 401 구분
- Backend Security 로그와 Frontend Network 탭을 함께 확인
- Frontend Route Guard는 UX용이고 최종 권한 검증은 Backend 기준

---

### [FAQ]

Q. 401과 403 차이는?
A. 401은 인증 실패 또는 로그인 필요이고 403은 인증은 되었지만 권한이 부족한 경우다.

Q. 401과 403을 같은 방식으로 처리해도 돼?
A. 권장하지 않는다. 401은 인증 문제, 403은 권한 문제다.

Q. 403이면 로그아웃해야 해?
A. 대부분 아니다. 인증은 되었지만 권한이 없는 상태이므로 권한 없음 화면이나 메시지를 보여주는 것이 일반적이다.

Q. 401이면 무조건 login으로 보내?
A. refresh token flow가 있으면 먼저 재발급을 시도할 수 있다. 재발급 실패 시 login으로 이동한다.

---

# 2. 401 Handling

## 2.1 401 Handling Flow

### [개념]

401 Handling은 인증되지 않았거나 Access Token이 유효하지 않은 요청을 처리하는 흐름이다.

Frontend는 401 발생 시 Refresh Token Flow, Clear Auth, Login Redirect, 사용자 메시지를 상황에 맞게 적용해야 한다.

---

### [핵심]

401 원인:

- token 없음
- token 만료
- token 위조
- Authorization Header 누락
- Bearer prefix 누락
- Bearer 형식 오류
- refresh token 만료
- refresh 실패
- 로그인 필요 API 접근
- Backend Security 인증 실패

처리 후보:

- refresh token 시도
- original request retry
- clearAuth
- login redirect
- auth expired message
- user message
- Promise.reject

기본 Flow:

```text
Receive 401
→ Check Refresh Available
→ If Refresh Success Retry Original Request
→ If Refresh Fail Clear Auth
→ Redirect Login
```

---

### [실무]

Refresh 없는 단순 처리:

```tsx
authApi.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      clearAuth();
      emitAuthExpired();
    }

    return Promise.reject(error);
  },
);
```

Refresh 포함 처리:

```tsx
authApi.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;
    const status = error.response?.status;

    if (status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;

      try {
        const newAccessToken = await refreshAccessToken();

        originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;

        return authApi(originalRequest);
      } catch (refreshError) {
        clearAuth();
        emitAuthExpired();

        return Promise.reject(refreshError);
      }
    }

    return Promise.reject(error);
  },
);
```

주의:

- 모든 401을 즉시 login redirect하면 UX가 나쁠 수 있음
- refresh endpoint의 401은 재시도 금지
- login API 실패 401과 token 만료 401 구분
- 원래 요청 retry는 1회만 수행
- refresh 실패 시 clearAuth 필수
- interceptor에서 React Router hook 직접 사용 금지
- Promise.reject로 호출부에 에러 전달

---

### [FAQ]

Q. 401이 나오면 무조건 로그아웃해야 해?
A. refresh token flow가 있으면 먼저 재발급을 시도할 수 있다. 재발급 실패 시 로그아웃 처리한다.

Q. 로그인 실패도 401이야?
A. Backend 설계에 따라 그럴 수 있다. 로그인 실패 401과 기존 세션 만료 401을 처리 흐름에서 구분해야 한다.

Q. refresh endpoint가 401이면?
A. refresh 실패로 보고 clearAuth 후 login redirect 처리하는 것이 일반적이다.

Q. 401 처리 후 Component catch도 실행돼야 해?
A. 화면별 메시지 처리가 필요하면 interceptor에서 Promise.reject를 반환해야 한다.

---

## 2.2 Token Missing 401

### [개념]

Token Missing 401은 인증 API 요청에 Access Token이 포함되지 않아 발생하는 401이다.

대부분 authApi 미사용, Authorization Header 누락, Request Interceptor 미등록, token 저장 실패 때문에 발생한다.

---

### [핵심]

확인 대상:

- token storage
- getAccessToken return value
- Authorization Header
- Bearer prefix
- authApi usage
- publicApi misuse
- interceptor registration
- setup file import
- request timing
- login response mapping
- response.data.data unwrap

Debug Flow:

```text
401 발생
→ Network Request Headers 확인
→ Authorization Header 존재 확인
→ Bearer 형식 확인
→ authApi 사용 여부 확인
→ token 저장 여부 확인
→ getAccessToken 반환값 확인
→ interceptor 등록 여부 확인
→ login response mapping 확인
```

---

### [실무]

문제 예:

```text
문제: localStorage에 token은 있음
원인: 인증 API 함수가 publicApi 사용
해결: authApi로 변경
```

문제 예:

```text
문제: token 저장은 됐지만 Header 없음
원인: Request Interceptor 설정 파일 import 누락
해결: apiClient.ts에서 authApi interceptor 1회 등록
```

문제 예:

```text
문제: Header에 Bearer undefined
원인: token getter가 undefined를 반환했는데 Header를 무조건 추가
해결: token이 있을 때만 Authorization Header 추가
```

확인 코드:

```tsx
authApi.interceptors.request.use((config) => {
  const accessToken = getAccessToken();

  if (accessToken) {
    config.headers.Authorization = `Bearer ${accessToken}`;
  }

  return config;
});
```

주의:

- token 존재와 Header 포함은 다른 문제
- publicApi로 인증 API 호출 금지
- `Bearer undefined` 금지
- `Bearer Bearer token` 중복 금지
- token 저장 전 인증 API 호출 금지
- Network 탭에서 Request Headers 확인
- token 값을 console.log로 출력하지 않음

---

### [FAQ]

Q. localStorage에 token이 있는데 401이 나?
A. Network 탭에서 Authorization Header에 실제로 token이 포함되었는지 확인해야 한다.

Q. 인증 API에 publicApi를 쓰면 어떻게 돼?
A. Authorization Header가 누락되어 401이 발생할 수 있다.

Q. Header에 Bearer undefined가 들어가?
A. token getter가 undefined를 반환했는데 Header를 무조건 추가했을 가능성이 있다.

Q. 로그인 직후 API만 401이 나?
A. token 저장 또는 Auth State 갱신이 완료되기 전에 인증 API 요청이 먼저 실행되었을 수 있다.

---

## 2.3 Token Expired 401

### [개념]

Token Expired 401은 Access Token이 만료되어 Backend가 인증 실패로 응답하는 상황이다.

Frontend는 refresh token flow가 있으면 새 Access Token을 요청하고 원래 요청을 재시도할 수 있다.

---

### [핵심]

Flow:

```text
Authenticated API Request
→ Access Token Expired
→ 401 Unauthorized
→ Refresh Access Token
→ Save New Access Token
→ Retry Original Request
→ Success
```

실패 Flow:

```text
Authenticated API Request
→ Access Token Expired
→ Refresh Request
→ Refresh Failed
→ Clear Auth
→ Login Redirect
```

확인 대상:

- access token expiration
- refresh token presence
- refresh endpoint
- retry flag
- original request
- refresh failure
- clearAuth
- auth expired event

---

### [실무]

Token Expired 처리 예:

```tsx
if (status === 401 && !originalRequest._retry) {
  originalRequest._retry = true;

  try {
    const newAccessToken = await refreshAccessToken();

    originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;

    return authApi(originalRequest);
  } catch (refreshError) {
    clearAuth();
    emitAuthExpired();

    return Promise.reject(refreshError);
  }
}
```

주의:

- 원래 요청 retry는 한 번만
- refresh API 실패 시 다시 refresh 시도 금지
- refresh token 만료 시 clearAuth
- 여러 API 동시 401이면 concurrent refresh 처리 검토
- mutation 요청 retry는 중복 실행 위험 검토
- refresh 성공 후 새 token을 저장해야 다음 요청에 반영됨
- refresh 실패 후 private cache 정리 필요

---

### [FAQ]

Q. access token이 만료되면 어떻게 해?
A. refresh token이 있으면 새 access token을 요청하고 성공 시 원래 API 요청을 재시도할 수 있다.

Q. refresh 요청도 실패하면?
A. 인증 정보를 정리하고 login 페이지로 이동시키는 것이 일반적이다.

Q. refresh 성공했는데 다음 요청도 401이야?
A. 새 access token 저장이 누락되었거나 원래 요청 Header에 이전 token이 남아 있을 수 있다.

Q. POST 요청도 token 만료 후 자동 retry해도 돼?
A. 가능하지만 결제, 주문, 중복 생성 같은 요청은 idempotency와 중복 실행 위험을 검토해야 한다.

---

# 3. 403 Handling

## 3.1 403 Handling Flow

### [개념]

403 Handling은 인증된 사용자가 권한이 부족한 리소스나 기능에 접근했을 때 처리하는 흐름이다.

403은 인증 실패가 아니므로 기본적으로 Auth State를 clear하지 않는다.

---

### [핵심]

403 원인:

- role 부족
- 관리자 권한 없음
- 작성자 / 소유자 불일치
- 접근 금지 리소스
- account status restriction
- Backend Authorization 실패
- Permission Policy 실패

처리 기준:

- Do Not Clear Auth by Default
- Forbidden Page 표시
- 권한 없음 메시지 표시
- 이전 페이지 이동
- role refetch 가능
- Auth State 유지
- Promise.reject

기본 Flow:

```text
Receive 403
→ Keep Auth State
→ Show Forbidden Message
→ Navigate Forbidden Page or Previous Page
```

---

### [실무]

Interceptor 처리:

```tsx
authApi.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 403) {
      markForbiddenError(error);
    }

    return Promise.reject(error);
  },
);
```

화면 처리:

```tsx
try {
  await deletePost(postId);
} catch (error) {
  if (isForbiddenError(error)) {
    setErrorMessage("권한이 없습니다.");
    return;
  }

  setErrorMessage("요청 처리 중 오류가 발생했습니다.");
}
```

Forbidden Page 이동:

```tsx
if (isForbiddenError(error)) {
  navigate("/forbidden", { replace: true });
}
```

주의:

- 403에서 기본 logout 처리 금지
- 403을 login redirect로 처리하지 않음
- 인증 상태는 유지될 수 있음
- 사용자에게 내부 권한 정책 과다 노출 금지
- role 정보가 stale하면 `/me` refetch 가능
- Backend 권한 기준 확인 필요

---

### [FAQ]

Q. 403이면 로그아웃해야 해?
A. 대부분 아니다. 인증은 되었지만 권한이 없는 상태이므로 권한 없음 화면이나 메시지를 보여주는 것이 일반적이다.

Q. 403에서 login 페이지로 보내도 돼?
A. 권장하지 않는다. 이미 로그인된 사용자라면 forbidden page나 권한 없음 메시지가 더 적절하다.

Q. 403이 나면 role을 다시 조회해야 해?
A. role 변경 가능성이 있는 서비스라면 `/me` refetch로 최신 권한을 확인할 수 있다.

Q. 403 메시지는 어떻게 보여줘?
A. “접근 권한이 없습니다” 같은 권한 부족 메시지나 forbidden page로 처리할 수 있다.

---

## 3.2 Role Based 403

### [개념]

Role Based 403은 사용자 role이 특정 API나 화면 접근에 필요한 role을 만족하지 못할 때 발생하는 권한 오류다.

Frontend는 Role Based UI와 Role Based Route로 UX를 정리할 수 있지만 Backend Authorization이 최종 기준이다.

---

### [핵심]

발생 상황:

- ROLE_USER가 admin API 호출
- ROLE_ADMIN 전용 페이지 접근
- role naming 불일치
- stale role state
- Backend role policy mismatch
- mock user role mismatch

확인 대상:

- user.role
- ROLE_USER
- ROLE_ADMIN
- allowedRoles
- Backend Security role check
- `/me` response role
- Role Based Route
- Role Based UI

---

### [실무]

RoleRoute 예:

```tsx
function RoleRoute({ allowedRoles, children }: RoleRouteProps) {
  const { initialized, authenticated, user } = useAuth();

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

Debug Flow:

```text
403 발생
→ Backend required role 확인
→ /me 응답 role 확인
→ Frontend user.role 확인
→ ROLE_ADMIN / ADMIN naming 확인
→ allowedRoles 확인
→ Backend Security 설정 확인
```

주의:

- Frontend role check는 UX용
- Backend role check 필수
- ROLE_ADMIN / ADMIN 혼용 금지
- role 정보가 오래되면 `/me` refetch
- role 변경 후 cache invalidate 필요
- 403을 401처럼 처리하지 않음

---

### [FAQ]

Q. 관리자 계정인데 403이 나?
A. Backend required role, `/me` 응답 role, Frontend role naming, token의 권한 claim을 확인해야 한다.

Q. ROLE_ADMIN과 ADMIN은 같은 거야?
A. 프로젝트 기준에 따라 다르지만 문자열이 다르면 조건문에서 다르게 처리된다. naming을 통일해야 한다.

Q. Frontend에서 ROLE_ADMIN을 확인하면 관리자 API가 안전해져?
A. 아니다. Frontend role check는 화면 접근 UX용이고 관리자 API는 Backend에서 반드시 권한 검증해야 한다.

---

## 3.3 Owner Based 403

### [개념]

Owner Based 403은 사용자가 인증은 되었지만 특정 리소스의 소유자 또는 작성자가 아니어서 접근이 거부되는 상황이다.

게시글 수정, 댓글 삭제, 주문 상세, 개인 파일 조회 같은 기능에서 발생한다.

---

### [핵심]

발생 상황:

- 작성자 불일치
- 소유자 불일치
- userId mismatch
- authorId mismatch
- private resource access
- owner-only action
- Backend owner check failure

Frontend 역할:

- edit / delete button 숨김
- owner-only action UX 정리
- 권한 없음 메시지 표시
- forbidden page 이동

Backend 역할:

- owner check
- resource authorization
- 403 response
- audit log optional

---

### [실무]

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

Owner 403 처리:

```tsx
try {
  await updatePost(postId, requestBody);
} catch (error) {
  if (isForbiddenError(error)) {
    setErrorMessage("이 게시글을 수정할 권한이 없습니다.");
    return;
  }

  throw error;
}
```

주의:

- 버튼 숨김은 보안이 아님
- Backend owner check 필수
- resource fetch 전에는 owner 판단 불가
- userId와 authorId 타입 일치 확인
- stale resource 정보 주의
- 403은 권한 부족으로 처리
- 내부 소유권 정책 과다 노출 금지

---

### [FAQ]

Q. 삭제 버튼을 작성자에게만 보여주면 충분해?
A. 아니다. 버튼 표시 제어는 UX용이고 실제 삭제 API는 Backend에서 작성자 여부를 검증해야 한다.

Q. 게시글 수정 API가 403이야?
A. 로그인은 되었지만 작성자 또는 소유자가 아닐 가능성이 있다. Backend owner check 기준을 확인해야 한다.

Q. owner check는 Frontend에서 해도 돼?
A. UX 목적으로 가능하지만 최종 검증은 Backend에서 해야 한다.

---

# 4. Auth Troubleshooting Flow

## 4.1 Global Auth Debug Flow

### [개념]

Global Auth Debug Flow는 인증 문제가 발생했을 때 Frontend와 Backend 원인을 순서대로 분리해서 확인하는 절차다.

인증 문제는 token, Header, Auth State, Route Guard, Backend Security가 모두 연결되어 있으므로 단계적으로 확인해야 한다.

---

### [핵심]

Debug 순서:

```text
1. 현재 URL / Route 확인
2. Auth State 확인
3. token storage 확인
4. Network Request Headers 확인
5. HTTP Status 확인
6. Response Body 확인
7. Axios Instance 확인
8. Interceptor 확인
9. Route Guard 조건 확인
10. Backend Security 로그 확인
```

확인 대상:

- initialized
- authenticated
- user
- user.role
- accessToken
- refreshToken
- Authorization Header
- Bearer format
- publicApi / authApi
- 401 / 403
- response.data.data
- ProtectedRoute
- RoleRoute
- Backend Security config

---

### [실무]

인증 문제 분석 Flow:

```text
문제 발생
→ 화면 문제인지 API 문제인지 구분
→ API 문제면 Network 탭 확인
→ 401이면 Header / Token / Refresh 확인
→ 403이면 Role / Owner / Backend Authorization 확인
→ 화면 문제면 Auth State / Route Guard 확인
→ 새로고침 문제면 Auth Restore / initialized 확인
```

판단 기준:

```text
Network에 요청 자체가 없음
→ Route Guard / Conditional Rendering / Hook 실행 조건 확인

Request Header에 Authorization 없음
→ authApi / Request Interceptor / getAccessToken 확인

Authorization 있음 + 401
→ token 만료 / 위조 / Backend 검증 실패 확인

Authorization 있음 + 403
→ role / owner / Backend 권한 정책 확인
```

주의:

- token 값을 직접 공유하지 않음
- Network 탭에서 token 존재 여부와 Bearer 형식만 확인
- Backend 로그 없이 Frontend만으로 401 원인을 확정하지 않음
- 401과 403을 먼저 구분
- Auth State와 Backend 응답이 충돌할 수 있음
- Route Guard 통과와 API 권한은 별개

---

### [FAQ]

Q. Auth 문제는 어떻게 찾는 게 좋아?
A. Network Header, Status Code, Auth State, token 저장 여부, Route Guard 조건, Backend Security 로그를 순서대로 확인한다.

Q. 요청 자체가 안 나가면 뭐부터 봐?
A. Route Guard, 조건부 렌더링, useEffect 조건, 버튼 disabled 상태, API 호출 함수 실행 여부를 확인한다.

Q. Header는 있는데 401이면?
A. token 만료, token 위조, Bearer 형식 오류, Backend JWT 검증 실패를 확인해야 한다.

Q. Header는 있는데 403이면?
A. 인증은 되었지만 권한이 부족한 상황이므로 role, owner, Backend Authorization 설정을 확인해야 한다.

---

## 4.2 Network Tab Debug Checklist

### [개념]

Network Tab Debug Checklist는 브라우저 개발자 도구 Network 탭에서 인증 요청 문제를 확인하는 기준이다.

Frontend 인증 문제의 대부분은 Request Header, Response Status, Response Body에서 단서를 찾을 수 있다.

---

### [핵심]

확인 항목:

- Request URL
- HTTP Method
- Request Headers
- Authorization Header
- Bearer prefix
- Cookie included
- withCredentials
- Request Payload
- Response Status
- Response Body
- CORS error
- Preflight OPTIONS
- Redirect chain

---

### [실무]

401 확인:

```text
Network
→ Request Headers
→ Authorization 존재?
→ Bearer 형식 맞음?
→ token 값이 undefined 아님?
→ Response Status 401?
→ Response Body message / code 확인
```

403 확인:

```text
Network
→ Authorization 존재?
→ Response Status 403?
→ Response Body code 확인
→ user.role 확인
→ 요청한 리소스 owner 확인
→ Backend 권한 정책 확인
```

Cookie Auth 확인:

```text
Network
→ Request Headers Cookie 포함 여부 확인
→ withCredentials 확인
→ SameSite / Secure 정책 확인
→ CORS Allow-Credentials 확인
```

주의:

- token 전체 값을 복사하거나 공유하지 않음
- Authorization Header 존재 여부만 확인
- CORS error는 status code가 명확히 안 보일 수 있음
- OPTIONS preflight와 실제 요청을 구분
- redirect 응답이 callback 처리에 영향을 줄 수 있음
- API baseURL이 올바른지 확인

---

### [FAQ]

Q. Network 탭에서 뭘 봐야 해?
A. Request URL, Authorization Header, Cookie 포함 여부, Response Status, Response Body를 확인해야 한다.

Q. CORS 에러도 401이야?
A. 아니다. CORS 문제는 브라우저가 응답 접근을 막는 것이며 Backend 인증 실패와 구분해야 한다.

Q. OPTIONS 요청이 실패하면?
A. Preflight CORS 설정 문제일 수 있다. Authorization Header 허용과 credentials 설정을 확인해야 한다.

---

# 5. Route Guard Troubleshooting

## 5.1 Auth Redirect Loop

### [개념]

Auth Redirect Loop는 login page와 protected page 사이에서 redirect가 반복되는 문제다.

대부분 initialized 미사용, Auth State 복원 지연, PublicOnlyRoute와 ProtectedRoute 조건 충돌로 발생한다.

---

### [핵심]

원인:

- auth loading 상태 미구분
- initialized 전 redirect
- login page도 ProtectedRoute 처리
- PublicOnlyRoute와 ProtectedRoute 조건 충돌
- authenticated 계산 오류
- token은 있지만 user 정보 없음
- `/me` 실패 처리 오류
- redirect target이 login 또는 signup
- stale persisted auth state

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
→ persisted auth storage 확인
```

문제 예:

```text
문제: /mypage → /login → /mypage 반복
원인: login 성공 후 redirect target은 /mypage지만 Auth State가 아직 false
해결: applyLoginResult 완료 후 navigate 실행
```

문제 예:

```text
문제: 새로고침 후 login으로 튕김
원인: initialized 전 authenticated false로 판단
해결: initialized false 동안 loading UI 표시
```

주의:

- 초기 인증 확인 전 redirect하지 않음
- login route는 ProtectedRoute로 감싸지 않음
- callback route는 auth guard 예외 가능
- Navigate replace 사용 고려
- redirect target이 다시 guard에 걸리는지 확인
- login / signup / callback은 safe redirect에서 기본 경로로 보정

---

### [FAQ]

Q. login과 mypage 사이를 계속 왔다 갔다 해?
A. auth initialized 전에 redirect하거나 ProtectedRoute와 PublicOnlyRoute 조건이 충돌했을 가능성이 크다.

Q. 새로고침 후 바로 login으로 튕겨?
A. 인증 상태 확인 loading을 기다리지 않고 Protected Route가 먼저 redirect했을 가능성이 있다.

Q. token은 있는데 login으로 보내져?
A. user 정보 복원 전 authenticated를 false로 판단했거나 `/me` 확인 loading을 기다리지 않았을 수 있다.

Q. login page가 계속 다시 열려?
A. PublicOnlyRoute 조건, authenticated 상태, redirect target이 login으로 저장되었는지 확인해야 한다.

---

## 5.2 Forbidden Loop

### [개념]

Forbidden Loop는 권한 없음 처리 후 이동한 forbidden page가 다시 RoleRoute 또는 ProtectedRoute 조건에 걸려 반복 redirect되는 문제다.

Forbidden Page 위치와 redirect target을 잘못 설정했을 때 자주 발생한다.

---

### [핵심]

원인:

- forbidden route가 RoleRoute 내부에 있음
- forbidden route도 admin guard 적용
- 403 처리 후 다시 forbidden API 호출
- previous page 이동이 다시 forbidden page 접근
- RoleRoute fallback target 오류
- 401과 403 처리 혼동

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

- forbidden page는 RoleRoute 보호 밖에 둠
- 401은 login redirect
- 403은 forbidden 처리
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

# 6. Refresh Troubleshooting

## 6.1 Refresh Loop Troubleshooting

### [개념]

Refresh Loop는 Access Token 재발급 로직이 실패하거나 조건이 잘못되어 refresh 요청이 반복되는 문제다.

Refresh Loop는 사용자 경험을 망치고 서버 부하를 증가시킨다.

---

### [핵심]

원인:

- refresh API도 interceptor retry 대상
- `_retry` 플래그 없음
- refresh 실패 후 clearAuth 누락
- 동일 401 요청 무한 재시도
- refresh token 만료
- 여러 요청 동시 401 처리 미흡
- login API 401까지 refresh 처리
- Promise.reject 누락
- auth expired event 후 재요청 발생

---

### [실무]

Debug Flow:

```text
Network에서 refresh 반복 확인
→ refresh 요청도 401인지 확인
→ retry flag 확인
→ refresh endpoint interceptor 제외 확인
→ refresh 실패 시 clearAuth 확인
→ pending queue 처리 여부 확인
→ Promise.reject 반환 확인
→ auth state false 후 재요청 여부 확인
```

해결 기준:

```text
refresh endpoint 401
→ retry 금지
→ clearAuth
→ login redirect

original request 401
→ _retry false이면 refresh 1회
→ _retry true이면 retry 금지
→ Promise.reject
```

주의:

- refresh 요청은 재귀 refresh 대상에서 제외
- 원래 요청 retry는 1회 제한
- refresh 실패 시 즉시 auth 정리
- login 실패 401과 token 만료 401 구분
- interceptor에서 error를 삼키지 않음
- auth false 상태에서 private query 자동 refetch 방지

---

### [FAQ]

Q. refresh 요청이 계속 반복돼?
A. refresh API까지 401 interceptor가 재시도 대상으로 잡혔거나 retry 제한이 없을 가능성이 있다.

Q. refresh 실패 후에도 계속 API가 호출돼?
A. clearAuth와 redirect 처리가 누락되었거나 원래 요청 retry 제한이 없을 수 있다.

Q. refresh loop는 어떻게 막아?
A. `_retry` 플래그, refresh endpoint 제외, refresh 실패 시 clearAuth, Promise.reject 반환으로 막는다.

Q. login API 401도 refresh해서 loop가 생겨?
A. 가능하다. Login API는 refresh 대상에서 제외해야 한다.

---

## 6.2 Concurrent 401 Troubleshooting

### [개념]

Concurrent 401 문제는 여러 인증 API가 동시에 401을 받아 refresh 요청이 여러 번 발생하거나 서로 다른 token이 충돌하는 상황이다.

동시 요청이 많은 화면에서는 refresh queue 또는 isRefreshing flag를 검토해야 한다.

---

### [핵심]

증상:

- refresh API 여러 번 호출
- token이 갱신됐는데 일부 요청은 계속 401
- refresh token rotation 충돌
- 로그아웃과 재로그인이 동시에 발생
- user가 null로 바뀌었다가 다시 복원
- notification / profile / favorite 요청이 동시에 실패

원인:

- multiple API requests
- simultaneous 401
- duplicate refresh requests
- no isRefreshing flag
- no pending queue
- stale access token retry

---

### [실무]

Queue Flow:

```text
Request A / B / C
→ All receive 401
→ A starts refresh
→ B / C wait in queue
→ Refresh success
→ Save new access token
→ Retry A / B / C with new token
→ Refresh failure
→ Reject all
→ Clear Auth
```

Debug Flow:

```text
동시 401 발생
→ Network refresh 요청 개수 확인
→ refresh token rotation 정책 확인
→ isRefreshing flag 여부 확인
→ pending queue 여부 확인
→ retry request Header의 token 확인
```

주의:

- refresh는 동시에 하나만 실행
- 대기 중인 요청은 새 token으로 재시도
- refresh 실패 시 queue 전체 reject
- 단순 프로젝트에서는 retry once로 시작 가능
- 실서비스에서는 concurrent refresh 처리 검토
- refresh token rotation 사용 시 특히 중요

---

### [FAQ]

Q. 여러 API가 동시에 401이면 어떻게 해?
A. refresh 요청을 하나만 수행하고 나머지 요청은 대기시킨 뒤 새 token으로 재시도하는 queue 방식이 필요할 수 있다.

Q. refresh 요청이 여러 번 나가면 뭐가 문제야?
A. token race condition, refresh token rotation 충돌, 불필요한 서버 부하가 발생할 수 있다.

Q. concurrent refresh 처리는 꼭 필요해?
A. 모든 프로젝트에서 필수는 아니지만 동시에 많은 인증 API를 호출하는 앱에서는 안정성을 높인다.

---

# 7. Auth State Troubleshooting

## 7.1 Auth State Mismatch

### [개념]

Auth State Mismatch는 token, user, authenticated, initialized 상태가 서로 일치하지 않아 인증 UI와 API 요청 흐름이 꼬이는 문제다.

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
- persisted store stale state

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
→ persisted storage 확인
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

Q. authenticated true인데 user가 null이야?
A. Login Response 처리나 `/me` 복원 과정에서 user 설정이 누락되었을 가능성이 있다.

Q. token은 지워졌는데 로그인 상태로 보여?
A. authenticated state나 persisted auth store가 정리되지 않았을 가능성이 있다.

Q. 로그아웃했는데 화면에 닉네임이 남아?
A. user state나 query cache가 정리되지 않았을 가능성이 있다.

Q. role이 없어서 관리자 메뉴가 안 보여?
A. `/me` 응답에 role이 없거나 Auth State user.role 설정이 누락되었을 수 있다.

---

## 7.2 Initialized Never Ends

### [개념]

Initialized Never Ends는 앱 최초 인증 상태 확인이 끝나지 않아 loading 화면이 계속 유지되는 문제다.

대부분 restoreAuth의 finally 누락, `/me` 요청 pending, refresh loop, interceptor deadlock 때문에 발생한다.

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
- early return before setInitialized
- Promise chain break

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
- token이 없어도 initialized true 필요
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

Q. interceptor 에러 처리 때문에 loading이 안 끝날 수 있어?
A. 가능하다. Promise.reject 또는 throw가 누락되면 호출부 finally가 실행되지 않을 수 있다.

---

# 8. Axios Interceptor Troubleshooting

## 8.1 Interceptor Duplicate Registration

### [개념]

Interceptor Duplicate Registration은 interceptor 설정 코드가 여러 번 실행되어 같은 요청 처리 로직이 중복 등록되는 문제다.

중복 등록은 Header 중복, refresh 중복, error handling 반복, memory leak을 유발할 수 있다.

---

### [핵심]

원인:

- Component 내부 등록
- Hook 내부 등록
- AuthProvider remount
- Hot Reload
- StrictMode
- setup function repeated call
- eject 누락

증상:

- request interceptor 여러 번 실행
- refresh API 여러 번 호출
- logout event 여러 번 발생
- error message 중복 표시
- performance issue

---

### [실무]

잘못된 예:

```tsx
function SomeComponent() {
  authApi.interceptors.request.use((config) => {
    return config;
  });

  return null;
}
```

권장 구조:

```tsx
// apiClient.ts
export const authApi = axios.create({
  baseURL: API_BASE_URL,
});

authApi.interceptors.request.use(
  (config) => {
    const token = getAccessToken();

    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }

    return config;
  },
  (error) => Promise.reject(error),
);
```

Debug Flow:

```text
API 요청 1회
→ interceptor 실행 횟수 확인
→ interceptor 등록 위치 확인
→ Component 내부 등록 여부 확인
→ AuthProvider remount 여부 확인
→ setup function 호출 횟수 확인
→ eject 필요 여부 확인
```

주의:

- Component 내부 등록은 피함
- module scope 등록은 대부분 1회 실행
- setup 파일 import 중복 확인
- test 환경에서는 setup 초기화 격리 필요
- Hot Reload 중 개발환경에서만 중복처럼 보일 수 있음
- production build에서도 재현되는지 확인

---

### [FAQ]

Q. interceptor가 여러 번 실행돼?
A. interceptor가 중복 등록되었을 가능성이 있다. 등록 위치를 module scope로 옮기거나 eject 처리를 확인해야 한다.

Q. Component에서 interceptor를 등록하면 왜 문제야?
A. Component가 렌더링되거나 remount될 때마다 interceptor가 추가될 수 있다.

Q. refresh 요청이 여러 번 나가?
A. interceptor 중복 등록 또는 concurrent 401 처리가 없어서 발생할 수 있다.

---

## 8.2 Response Interceptor Swallow Error

### [개념]

Response Interceptor Swallow Error는 interceptor에서 에러를 처리한 뒤 `Promise.reject`를 반환하지 않아 호출부가 에러를 인식하지 못하는 문제다.

이 문제는 화면별 에러 메시지 표시, loading 종료, retry 처리 누락을 유발한다.

---

### [핵심]

원인:

- return 누락
- Promise.reject 누락
- catch에서 error 삼킴
- async interceptor 반환 누락
- refresh 실패 후 reject 누락
- normalize 후 throw 누락

증상:

- Component catch 실행 안 됨
- loading 계속 유지
- error message 표시 안 됨
- API 함수가 undefined 반환
- retry 흐름 중단
- finally 미실행처럼 보임

---

### [실무]

잘못된 예:

```tsx
authApi.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      clearAuth();
    }
  },
);
```

올바른 예:

```tsx
authApi.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      clearAuth();
    }

    return Promise.reject(error);
  },
);
```

refresh 실패 예:

```tsx
catch (refreshError) {
  clearAuth();

  return Promise.reject(refreshError);
}
```

주의:

- interceptor error handler는 항상 response 또는 Promise.reject 반환
- 에러를 처리해도 호출부에 전달할지 기준 필요
- 공통 auth cleanup과 화면별 message 처리는 분리
- Promise chain이 끊기면 loading이 끝나지 않을 수 있음
- async function에서는 `throw error`도 가능

---

### [FAQ]

Q. interceptor에서 Promise.reject를 왜 해?
A. 호출한 API 함수나 화면에서도 에러를 인식하고 적절한 UI를 보여줄 수 있게 하기 위해서다.

Q. Component catch가 실행되지 않아?
A. response interceptor에서 에러를 삼키고 Promise.reject를 반환하지 않았을 가능성이 있다.

Q. API 실패 후 loading이 계속 돌아?
A. 호출부 catch나 finally가 실행되지 않았을 수 있으며 interceptor 반환값을 확인해야 한다.

---

# 9. OAuth2 Auth Troubleshooting

## 9.1 OAuth2 Login Success but User Missing

### [개념]

OAuth2 Login Success but User Missing은 소셜 로그인은 성공했지만 Frontend Auth State에 user 정보가 없는 문제다.

대부분 callback에서 token만 저장하고 `/me` 호출 또는 user state 설정을 누락해 발생한다.

---

### [핵심]

원인:

- token only stored
- getMe not called
- user state not set
- response unwrap mismatch
- role missing
- `/me` 401
- cookie not sent
- withCredentials missing
- Auth State update order wrong

---

### [실무]

Debug Flow:

```text
OAuth2 로그인 성공
→ token 또는 cookie 존재 확인
→ /me 호출 여부 확인
→ /me 응답 확인
→ response.data.data unwrap 확인
→ setUser 호출 확인
→ setAuthenticated true 확인
→ role 포함 여부 확인
```

문제 예:

```text
문제: 로그인 성공 후 Header가 비로그인 상태
원인: token 저장 후 user state를 설정하지 않음
해결: callback에서 /me 호출 후 setUser + setAuthenticated 처리
```

Cookie 방식 문제 예:

```text
문제: Cookie 방식 OAuth2 후 /me 401
원인: withCredentials 누락 또는 Backend CORS credentials 설정 누락
해결: authApi withCredentials와 Backend CORS 설정 확인
```

주의:

- token 저장과 Auth State 갱신은 별도 작업
- `/me` 응답에 role 포함 필요
- callback 처리 완료 전 route 이동 금지
- HttpOnly Cookie 방식은 token 확인 대신 `/me` 확인
- response wrapper unwrap 기준 확인

---

### [FAQ]

Q. OAuth2 로그인 성공했는데 Header가 로그인 상태로 안 바뀌어?
A. callback에서 `/me` API 호출 또는 user state 설정이 누락되었을 가능성이 있다.

Q. OAuth2 후 token은 있는데 user가 null이야?
A. token 저장 후 Auth State user를 채우지 않았거나 `/me` 호출이 실패했을 수 있다.

Q. Cookie 방식 OAuth2 후 /me가 401이야?
A. cookie 전송 설정, withCredentials, SameSite, Secure, Backend CORS credentials 설정을 확인해야 한다.

---

## 9.2 OAuth2 Redirect Loop

### [개념]

OAuth2 Redirect Loop는 OAuth2 callback, login page, protected page 사이에서 redirect가 반복되는 문제다.

대부분 callback route가 PublicOnlyRoute로 감싸졌거나 Auth State 갱신 전에 navigate가 실행되거나 returnUrl이 callback / login으로 설정되어 발생한다.

---

### [핵심]

원인:

- callback route wrapped by PublicOnlyRoute
- callback route wrapped by ProtectedRoute
- navigate before setAuthenticated
- returnUrl is login
- returnUrl is callback
- auth restore not initialized
- `/me` fails then retry social login
- stale authenticated state

---

### [실무]

Debug Flow:

```text
OAuth2 Redirect Loop 발생
→ callback route guard 확인
→ PublicOnlyRoute 감싸짐 여부 확인
→ ProtectedRoute 감싸짐 여부 확인
→ Auth State update 순서 확인
→ returnUrl 값 확인
→ getSafeRedirectPath 확인
→ /me 성공 여부 확인
```

권장 route:

```tsx
<Route path="/oauth/callback" element={<OAuthCallbackPage />} />
```

Safe Redirect:

```tsx
function getSafeOAuthRedirectPath(path: unknown) {
  if (typeof path !== "string") {
    return "/";
  }

  if (!path.startsWith("/") || path.startsWith("//")) {
    return "/";
  }

  if (
    path === "/login" ||
    path === "/signup" ||
    path.startsWith("/oauth/callback")
  ) {
    return "/";
  }

  return path;
}
```

주의:

- callback route는 auth guard 예외로 두는 것이 안전
- Auth State 갱신 후 navigate
- returnUrl 검증 필수
- `/me` 실패 시 무한 재시도 금지
- login page에서 자동 소셜 로그인 재시도 금지
- OAuth2 실패 후 명확한 error message 표시

---

### [FAQ]

Q. OAuth2 callback과 login이 계속 반복돼?
A. callback route guard 설정, Auth State 갱신 순서, returnUrl이 login 또는 callback인지 확인해야 한다.

Q. OAuth2 callback route를 ProtectedRoute로 감싸도 돼?
A. 권장하지 않는다. 로그인 결과를 처리해야 하는 route이므로 인증 전에도 접근 가능해야 한다.

Q. returnUrl이 callback이면 어떻게 해?
A. callback loop를 막기 위해 기본 경로 `/`로 보정하는 것이 좋다.

---

# 10. Part09 Review Checklist

## 10.1 401 / 403 / Troubleshooting Checklist

### [개념]

Part09 검수는 401과 403 처리 기준, token 문제, route guard 문제, refresh 문제, Auth State 문제, interceptor 문제, OAuth2 문제를 구분해 해결할 수 있는지 확인한다.

---

### [핵심]

Checklist:

```md
- [ ] 401 Unauthorized와 403 Forbidden 차이가 명확한가?
- [ ] 401 Handling Flow가 포함되었는가?
- [ ] 403 Handling Flow가 포함되었는가?
- [ ] Login API 401과 Token Expired 401 구분이 포함되었는가?
- [ ] Token Missing 401 기준이 포함되었는가?
- [ ] Token Expired 401 기준이 포함되었는가?
- [ ] Authorization Header 확인 기준이 포함되었는가?
- [ ] Bearer Token 확인 기준이 포함되었는가?
- [ ] Role Based 403 기준이 포함되었는가?
- [ ] Owner Based 403 기준이 포함되었는가?
- [ ] Global Auth Debug Flow가 포함되었는가?
- [ ] Network Tab Debug Checklist가 포함되었는가?
- [ ] Auth Redirect Loop Troubleshooting이 포함되었는가?
- [ ] Forbidden Loop Troubleshooting이 포함되었는가?
- [ ] Refresh Loop Troubleshooting이 포함되었는가?
- [ ] Concurrent 401 Troubleshooting이 포함되었는가?
- [ ] Auth State Mismatch 기준이 포함되었는가?
- [ ] Initialized Never Ends 기준이 포함되었는가?
- [ ] Interceptor Duplicate Registration 기준이 포함되었는가?
- [ ] Response Interceptor Swallow Error 기준이 포함되었는가?
- [ ] OAuth2 Login Success but User Missing 기준이 포함되었는가?
- [ ] OAuth2 Redirect Loop 기준이 포함되었는가?
- [ ] Backend Authorization 최종 책임이 반복 명시되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

Part09 이후 권장 문서 순서:

```text
Part09 401 / 403 / Troubleshooting
→ Part10 Security / Checklist / Retrieval Optimization
```

검수 기준:

```text
Status Code 확인
→ 401 / 403 구분
→ Header 확인
→ Token 확인
→ Auth State 확인
→ Route Guard 확인
→ Interceptor 확인
→ Backend Authorization 확인
```

---

### [FAQ]

Q. Part09의 핵심은 뭐야?
A. 401과 403을 구분하고 token, Header, Auth State, Route Guard, Interceptor, Backend Authorization 문제를 단계적으로 찾는 것이다.

Q. Part09에서 보안 저장 전략까지 다뤄?
A. token 저장 보안은 Part04에서 다루고 Part09는 인증 오류와 troubleshooting에 집중한다.

Q. Part09 다음 문서는 뭐야?
A. Security / Checklist / Retrieval Optimization 문서가 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. 401과 403 차이는?
A. 401은 인증 실패 또는 로그인 필요이고 403은 인증은 되었지만 권한이 부족한 경우다.

Q. 401과 403을 같은 방식으로 처리해도 돼?
A. 권장하지 않는다. 401은 인증 문제, 403은 권한 문제다.

Q. 403이면 로그아웃해야 해?
A. 대부분 아니다. 인증은 되었지만 권한이 없는 상태이므로 권한 없음 화면이나 메시지를 보여주는 것이 일반적이다.

Q. 401이면 무조건 login으로 보내?
A. refresh token flow가 있으면 먼저 재발급을 시도할 수 있다. 재발급 실패 시 login으로 이동한다.

Q. 401이 나오면 무조건 로그아웃해야 해?
A. refresh token flow가 있으면 먼저 재발급을 시도할 수 있다. 재발급 실패 시 로그아웃 처리한다.

Q. 로그인 실패도 401이야?
A. Backend 설계에 따라 그럴 수 있다. 로그인 실패 401과 기존 세션 만료 401을 처리 흐름에서 구분해야 한다.

Q. refresh endpoint가 401이면?
A. refresh 실패로 보고 clearAuth 후 login redirect 처리하는 것이 일반적이다.

Q. localStorage에 token이 있는데 401이 나?
A. Network 탭에서 Authorization Header에 실제로 token이 포함되었는지 확인해야 한다.

Q. 인증 API에 publicApi를 쓰면 어떻게 돼?
A. Authorization Header가 누락되어 401이 발생할 수 있다.

Q. Header에 Bearer undefined가 들어가?
A. token getter가 undefined를 반환했는데 Header를 무조건 추가했을 가능성이 있다.

Q. 로그인 직후 API만 401이 나?
A. token 저장 또는 Auth State 갱신이 완료되기 전에 인증 API 요청이 먼저 실행되었을 수 있다.

Q. access token이 만료되면 어떻게 해?
A. refresh token이 있으면 새 access token을 요청하고 성공 시 원래 API 요청을 재시도할 수 있다.

Q. refresh 요청도 실패하면?
A. 인증 정보를 정리하고 login 페이지로 이동시키는 것이 일반적이다.

Q. refresh 성공했는데 다음 요청도 401이야?
A. 새 access token 저장이 누락되었거나 원래 요청 Header에 이전 token이 남아 있을 수 있다.

Q. 403에서 login 페이지로 보내도 돼?
A. 권장하지 않는다. 이미 로그인된 사용자라면 forbidden page나 권한 없음 메시지가 더 적절하다.

Q. 403이 나면 role을 다시 조회해야 해?
A. role 변경 가능성이 있는 서비스라면 `/me` refetch로 최신 권한을 확인할 수 있다.

Q. 관리자 계정인데 403이 나?
A. Backend required role, `/me` 응답 role, Frontend role naming, token의 권한 claim을 확인해야 한다.

Q. ROLE_ADMIN과 ADMIN은 같은 거야?
A. 프로젝트 기준에 따라 다르지만 문자열이 다르면 조건문에서 다르게 처리된다. naming을 통일해야 한다.

Q. 게시글 수정 API가 403이야?
A. 로그인은 되었지만 작성자 또는 소유자가 아닐 가능성이 있다. Backend owner check 기준을 확인해야 한다.

Q. owner check는 Frontend에서 해도 돼?
A. UX 목적으로 가능하지만 최종 검증은 Backend에서 해야 한다.

Q. Auth 문제는 어떻게 찾는 게 좋아?
A. Network Header, Status Code, Auth State, token 저장 여부, Route Guard 조건, Backend Security 로그를 순서대로 확인한다.

Q. 요청 자체가 안 나가면 뭐부터 봐?
A. Route Guard, 조건부 렌더링, useEffect 조건, 버튼 disabled 상태, API 호출 함수 실행 여부를 확인한다.

Q. Header는 있는데 401이면?
A. token 만료, token 위조, Bearer 형식 오류, Backend JWT 검증 실패를 확인해야 한다.

Q. Header는 있는데 403이면?
A. 인증은 되었지만 권한이 부족한 상황이므로 role, owner, Backend Authorization 설정을 확인해야 한다.

Q. Network 탭에서 뭘 봐야 해?
A. Request URL, Authorization Header, Cookie 포함 여부, Response Status, Response Body를 확인해야 한다.

Q. CORS 에러도 401이야?
A. 아니다. CORS 문제는 브라우저가 응답 접근을 막는 것이며 Backend 인증 실패와 구분해야 한다.

Q. OPTIONS 요청이 실패하면?
A. Preflight CORS 설정 문제일 수 있다. Authorization Header 허용과 credentials 설정을 확인해야 한다.

Q. login과 mypage 사이를 계속 왔다 갔다 해?
A. auth initialized 전에 redirect하거나 ProtectedRoute와 PublicOnlyRoute 조건이 충돌했을 가능성이 크다.

Q. 새로고침 후 바로 login으로 튕겨?
A. 인증 상태 확인 loading을 기다리지 않고 Protected Route가 먼저 redirect했을 가능성이 있다.

Q. token은 있는데 login으로 보내져?
A. user 정보 복원 전 authenticated를 false로 판단했거나 `/me` 확인 loading을 기다리지 않았을 수 있다.

Q. forbidden page가 계속 반복돼?
A. forbidden route가 RoleRoute 내부에 있거나 redirect target이 다시 같은 guard에 걸릴 수 있다.

Q. 403인데 login으로 보내져?
A. 401과 403 처리 기준이 섞였을 가능성이 있다. 403은 권한 없음으로 처리하는 것이 일반적이다.

Q. refresh 요청이 계속 반복돼?
A. refresh API까지 401 interceptor가 재시도 대상으로 잡혔거나 retry 제한이 없을 가능성이 있다.

Q. refresh 실패 후에도 계속 API가 호출돼?
A. clearAuth와 redirect 처리가 누락되었거나 원래 요청 retry 제한이 없을 수 있다.

Q. refresh loop는 어떻게 막아?
A. `_retry` 플래그, refresh endpoint 제외, refresh 실패 시 clearAuth, Promise.reject 반환으로 막는다.

Q. 여러 API가 동시에 401이면 어떻게 해?
A. refresh 요청을 하나만 수행하고 나머지 요청은 대기시킨 뒤 새 token으로 재시도하는 queue 방식이 필요할 수 있다.

Q. refresh 요청이 여러 번 나가면 뭐가 문제야?
A. token race condition, refresh token rotation 충돌, 불필요한 서버 부하가 발생할 수 있다.

Q. authenticated true인데 user가 null이야?
A. Login Response 처리나 `/me` 복원 과정에서 user 설정이 누락되었을 가능성이 있다.

Q. token은 지워졌는데 로그인 상태로 보여?
A. authenticated state나 persisted auth store가 정리되지 않았을 가능성이 있다.

Q. 로그아웃했는데 화면에 닉네임이 남아?
A. user state나 query cache가 정리되지 않았을 가능성이 있다.

Q. 앱이 계속 인증 확인 중으로 멈춰?
A. restoreAuth의 finally에서 initialized를 true로 설정하지 않았거나 `/me` 요청이 끝나지 않았을 가능성이 있다.

Q. token이 없을 때도 initialized를 true로 해야 해?
A. 해야 한다. token이 없으면 비로그인 상태로 정리한 뒤 initialized true로 라우팅을 시작해야 한다.

Q. interceptor가 여러 번 실행돼?
A. interceptor가 중복 등록되었을 가능성이 있다. 등록 위치를 module scope로 옮기거나 eject 처리를 확인해야 한다.

Q. Component catch가 실행되지 않아?
A. response interceptor에서 에러를 삼키고 Promise.reject를 반환하지 않았을 가능성이 있다.

Q. API 실패 후 loading이 계속 돌아?
A. 호출부 catch나 finally가 실행되지 않았을 수 있으며 interceptor 반환값을 확인해야 한다.

Q. OAuth2 로그인 성공했는데 Header가 로그인 상태로 안 바뀌어?
A. callback에서 `/me` API 호출 또는 user state 설정이 누락되었을 가능성이 있다.

Q. OAuth2 후 token은 있는데 user가 null이야?
A. token 저장 후 Auth State user를 채우지 않았거나 `/me` 호출이 실패했을 수 있다.

Q. Cookie 방식 OAuth2 후 /me가 401이야?
A. cookie 전송 설정, withCredentials, SameSite, Secure, Backend CORS credentials 설정을 확인해야 한다.

Q. OAuth2 callback과 login이 계속 반복돼?
A. callback route guard 설정, Auth State 갱신 순서, returnUrl이 login 또는 callback인지 확인해야 한다.

Q. Part09 다음 문서는 뭐야?
A. Security / Checklist / Retrieval Optimization 문서가 이어지는 것이 좋다.
