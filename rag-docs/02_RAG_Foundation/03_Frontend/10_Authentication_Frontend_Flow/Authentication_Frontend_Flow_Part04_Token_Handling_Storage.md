# Authentication Frontend Flow Part04 - Token Handling / Token Storage / Refresh Token Basics

---

# 1. Token Handling Overview

## 1.1 Access Token and Refresh Token

### [개념]

Token Handling은 Frontend가 Backend에서 발급받은 token을 인증 API 요청에 사용하고, 만료 또는 로그아웃 시 안전하게 정리하는 흐름이다.

Access Token은 인증된 API 요청에 사용되는 짧은 수명의 token이다.

Refresh Token은 Access Token이 만료되었을 때 새 Access Token을 발급받기 위한 token이다.

Frontend는 token을 생성하거나 검증하지 않는다.

Frontend는 발급받은 token을 저장, 전달, 제거, 재발급 요청 흐름에 맞게 사용한다.

---

### [핵심]

핵심 키워드:

- Token Handling
- Access Token
- Refresh Token
- Authorization Header
- Bearer Token
- Token Storage
- Token Expired
- Token Refresh
- Token Removal
- Auth State
- Auth Restore
- Axios Interceptor
- 401 Unauthorized
- Logout Cleanup
- Frontend Auth Security

Access Token:

- API 요청 인증에 사용
- Authorization Header에 포함
- 짧은 수명 권장
- 만료 시 401 발생 가능
- 노출 시 API 접근 위험

Refresh Token:

- Access Token 재발급에 사용
- Access Token보다 더 민감
- 저장 위치 신중히 결정
- 만료 또는 실패 시 logout 처리
- rotation 정책은 Backend와 맞춤

---

### [실무]

기본 Token Flow:

```text
Login Success
→ Receive Access Token / Refresh Token
→ Store Token by Project Policy
→ Set Auth State
→ Attach Access Token to Authorization Header
→ Authenticated API Request
→ Access Token Expired
→ Refresh Token Request
→ New Access Token
→ Retry Original Request
→ Refresh Failed
→ Clear Auth
```

Frontend 책임:

```text
Token 받기
→ 저장 또는 memory 관리
→ Header에 넣기
→ 만료 응답 처리
→ 재발급 요청
→ 실패 시 정리
```

Backend 책임:

```text
Token 발급
→ Token 서명
→ Token 검증
→ Token 만료 판단
→ 권한 검증
→ Refresh Token Rotation 정책 적용
```

주의:

- token을 console.log로 출력하지 않음
- token을 코드에 하드코딩하지 않음
- token 저장 위치는 보안 요구사항에 따라 결정
- token 존재만으로 authenticated true 확정하지 않음
- `/me` API로 사용자 상태 확인 가능
- logout 시 token과 auth state를 함께 정리
- refresh 실패 시 clearAuth 처리
- Authorization Header 형식 통일

---

### [FAQ]

Q. Access Token은 어디에 써?
A. 인증이 필요한 API 요청의 Authorization Header에 넣어 사용한다.

Q. Refresh Token은 어디에 써?
A. Access Token이 만료되었을 때 새 Access Token을 발급받는 데 사용한다.

Q. Frontend가 token을 검증해?
A. 아니다. Frontend는 token을 사용하고 실제 검증은 Backend가 수행한다.

Q. token이 있으면 로그인 상태로 봐도 돼?
A. 가능은 하지만 token이 만료되었거나 위조되었을 수 있으므로 `/me` API로 확인하는 흐름이 더 안전하다.

---

# 2. Access Token Rules

## 2.1 Authorization Header

### [개념]

Authorization Header는 인증이 필요한 API 요청에 Access Token을 전달하는 HTTP Header다.

JWT 기반 인증에서는 일반적으로 `Authorization: Bearer <accessToken>` 형식을 사용한다.

---

### [핵심]

Header 형식:

```text
Authorization: Bearer <accessToken>
```

필수 확인:

- Authorization spelling
- Bearer prefix
- Bearer 뒤 공백
- accessToken 존재 여부
- tokenType 중복 여부
- authApi 사용 여부
- request interceptor 적용 여부
- Network Request Headers 확인

---

### [실무]

Axios Request Interceptor 예:

```tsx
authApi.interceptors.request.use((config) => {
  const accessToken = getAccessToken();

  if (accessToken) {
    config.headers.Authorization = `Bearer ${accessToken}`;
  }

  return config;
});
```

tokenType 처리 예:

```tsx
function buildAuthorizationHeader(accessToken: string, tokenType?: string) {
  const normalizedType = tokenType ?? "Bearer";

  if (accessToken.startsWith("Bearer ")) {
    return accessToken;
  }

  return `${normalizedType} ${accessToken}`;
}
```

주의:

- Bearer와 token 사이 공백 필요
- access token이 없으면 header 생략
- tokenType이 `Bearer`로 오면 중복 주의
- `Bearer Bearer token` 금지
- 인증 필요 API는 authApi 사용
- 공개 API에 불필요한 token 전송 지양
- token을 console.log로 출력하지 않음
- Network 탭에서 Request Headers 확인 가능

---

### [FAQ]

Q. Authorization Header 형식은 뭐야?
A. 일반적으로 `Authorization: Bearer <accessToken>` 형식을 사용한다.

Q. Bearer를 빼먹으면 어떻게 돼?
A. Backend가 token 형식을 인식하지 못해 401이 발생할 수 있다.

Q. tokenType이 Bearer로 오면 어떻게 해?
A. Authorization Header 생성 시 `Bearer Bearer token`처럼 중복되지 않도록 처리 기준을 통일해야 한다.

Q. token은 있는데 401이 나?
A. Authorization Header에 실제로 포함되었는지, Bearer 형식이 맞는지, token이 만료되지 않았는지 확인해야 한다.

---

## 2.2 Access Token Lifecycle

### [개념]

Access Token Lifecycle은 Access Token이 발급, 저장, 사용, 만료, 갱신, 제거되는 흐름이다.

Access Token은 짧은 수명의 인증 수단이므로 만료와 재발급 처리를 고려해야 한다.

---

### [핵심]

Lifecycle:

- login success
- access token receive
- token storage
- attach header
- authenticated request
- token expired
- 401 response
- refresh request
- new access token
- retry request
- logout cleanup

---

### [실무]

Access Token 처리 흐름:

```text
Login API Success
→ accessToken receive
→ setAccessToken
→ authApi request interceptor reads accessToken
→ Authorization Header attach
→ API request success
```

만료 처리 흐름:

```text
Authenticated API Request
→ Access Token Expired
→ 401 Unauthorized
→ Try Refresh
→ Refresh Success: Save New Access Token
→ Retry Original Request
→ Refresh Failure: Clear Auth
```

간단 저장 예:

```tsx
function setAccessToken(token: string) {
  sessionStorage.setItem("accessToken", token);
}

function getAccessToken() {
  return sessionStorage.getItem("accessToken");
}

function removeAccessToken() {
  sessionStorage.removeItem("accessToken");
}
```

주의:

- 저장 위치는 프로젝트 정책에 따라 결정
- access token은 만료될 수 있음
- 만료 전 선제 갱신 여부는 선택
- token 만료 시간 `expiresIn`이 있으면 UX 개선 가능
- token 삭제와 Auth State 초기화는 함께 수행
- access token이 바뀌면 이후 요청에 새 token이 반영되어야 함

---

### [FAQ]

Q. access token이 만료되면 어떻게 해?
A. refresh token이 있으면 새 access token을 요청하고 성공 시 원래 API 요청을 재시도할 수 있다.

Q. access token은 항상 localStorage에 저장해?
A. 아니다. memory, sessionStorage, localStorage, cookie 등 프로젝트 보안 요구사항에 따라 선택한다.

Q. access token을 삭제하면 로그아웃이야?
A. token 삭제만으로는 부족하다. user state, authenticated 상태, cache도 함께 정리해야 한다.

---

# 3. Refresh Token Rules

## 3.1 Refresh Token Flow

### [개념]

Refresh Token Flow는 Access Token이 만료되었을 때 사용자에게 다시 로그인시키지 않고 새 Access Token을 발급받는 흐름이다.

Refresh Token은 Access Token보다 민감하므로 저장과 재발급 정책을 신중히 설계해야 한다.

---

### [핵심]

기본 Flow:

```text
API Request
→ Access Token Expired
→ 401 Response
→ Refresh Request
→ New Access Token
→ Retry Original Request
→ Refresh Failed
→ Logout / Login Redirect
```

필수 기준:

- refresh endpoint
- refresh token storage
- refresh request
- new access token save
- original request retry
- retry once
- refresh failed clearAuth
- refresh loop prevention
- concurrent 401 handling

---

### [실무]

간단 Refresh Flow:

```tsx
async function refreshAccessToken() {
  const refreshToken = getRefreshToken();

  if (!refreshToken) {
    throw new Error("Refresh token missing");
  }

  const response = await publicApi.post("/auth/refresh", {
    refreshToken,
  });

  const newAccessToken = response.data.data.accessToken;
  setAccessToken(newAccessToken);

  return newAccessToken;
}
```

Cookie 기반 Refresh Flow:

```tsx
async function refreshAccessTokenWithCookie() {
  const response = await publicApi.post(
    "/auth/refresh",
    {},
    { withCredentials: true },
  );

  const newAccessToken = response.data.data.accessToken;
  setAccessToken(newAccessToken);

  return newAccessToken;
}
```

주의:

- refresh 요청 중 중복 refresh 방지
- 원래 요청 retry는 한 번만 수행
- refresh 실패 시 clearAuth 후 login redirect
- refresh token rotation 정책은 Backend와 맞춤
- refresh token 저장 위치는 보안 요구사항에 따라 결정
- refresh API에는 무한 retry를 걸지 않음
- refresh endpoint가 auth interceptor 대상인지 확인
- refresh 요청 실패와 일반 API 401 처리 구분

---

### [FAQ]

Q. refresh token은 어떻게 처리해?
A. access token 만료로 401이 발생하면 refresh token으로 새 access token을 요청하고 성공 시 원래 요청을 재시도한다.

Q. refresh 요청도 실패하면?
A. 인증 정보를 정리하고 login 페이지로 이동시키는 것이 일반적이다.

Q. refresh 요청이 무한 반복될 수 있어?
A. 잘못 구현하면 가능하다. refresh 요청 자체에는 retry를 걸지 않거나 `_retry` 같은 플래그로 반복을 막아야 한다.

Q. refresh token은 access token보다 더 중요해?
A. 그렇다. refresh token은 새 access token을 발급받을 수 있으므로 더 민감하게 다뤄야 한다.

---

## 3.2 Refresh Retry Guard

### [개념]

Refresh Retry Guard는 Access Token 만료 후 원래 요청을 재시도할 때 무한 반복을 막는 기준이다.

API 요청이 401을 받을 때마다 refresh와 retry를 반복하면 refresh loop가 발생할 수 있다.

---

### [핵심]

필수 요소:

- `_retry` flag
- retry once
- exclude refresh endpoint
- exclude login endpoint
- clearAuth on refresh failure
- Promise.reject on failure
- avoid infinite loop

---

### [실무]

Response Interceptor 예:

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
        return Promise.reject(refreshError);
      }
    }

    return Promise.reject(error);
  },
);
```

Refresh 제외 기준:

```text
401 발생
→ originalRequest가 refresh request인지 확인
→ refresh request면 retry 금지
→ login request면 global refresh 금지
→ 일반 인증 API면 refresh 1회 시도
```

주의:

- `_retry` 플래그로 원래 요청 1회만 재시도
- refresh endpoint 자체는 refresh retry 대상에서 제외
- login API 실패 401과 token expired 401 구분
- refresh 실패 후 clearAuth 필수
- clearAuth 후 login redirect는 Router 계층과 연결
- interceptor에서 error를 삼키지 말고 Promise.reject 반환

---

### [FAQ]

Q. `_retry` 플래그는 왜 필요해?
A. 같은 요청이 401을 계속 받을 때 refresh와 retry가 무한 반복되는 것을 막기 위해 필요하다.

Q. refresh API도 401이면 다시 refresh를 시도해?
A. 아니다. refresh API 실패는 인증 복원 실패로 보고 clearAuth 또는 login redirect 처리해야 한다.

Q. Login API 401도 refresh를 시도해야 해?
A. 아니다. Login API 401은 로그인 실패로 처리해야 하며 token 만료 401과 구분해야 한다.

---

## 3.3 Concurrent Refresh Handling

### [개념]

Concurrent Refresh Handling은 여러 API 요청이 동시에 401을 받았을 때 refresh 요청을 하나만 보내고 나머지 요청을 대기시키는 기준이다.

동시 401 처리가 없으면 refresh 요청이 여러 번 발생하고 token race condition이 생길 수 있다.

---

### [핵심]

문제 상황:

- multiple API requests
- simultaneous 401
- duplicate refresh requests
- token race condition
- stale access token
- retry queue

처리 기준:

- isRefreshing flag
- pending request queue
- resolve after refresh
- reject after refresh failure
- single refresh request
- retry original requests

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

간단 구조 예:

```tsx
let isRefreshing = false;
let refreshWaitQueue: Array<(token: string) => void> = [];

function addRefreshWaiter(callback: (token: string) => void) {
  refreshWaitQueue.push(callback);
}

function resolveRefreshWaiters(token: string) {
  refreshWaitQueue.forEach((callback) => callback(token));
  refreshWaitQueue = [];
}
```

주의:

- refresh는 동시에 하나만 실행
- 대기 중인 요청은 새 token을 받은 뒤 재시도
- refresh 실패 시 queue 전체 reject 필요
- 구현 복잡도가 높으므로 프로젝트 규모에 따라 적용
- 단순 학습 프로젝트에서는 retry once만으로 시작 가능
- 실서비스에서는 동시 401 처리 검토

---

### [FAQ]

Q. 여러 API가 동시에 401이면 어떻게 해?
A. refresh 요청을 하나만 수행하고 나머지 요청은 대기시킨 뒤 새 token으로 재시도하는 queue 방식이 필요할 수 있다.

Q. concurrent refresh 처리는 꼭 필요해?
A. 모든 프로젝트에서 필수는 아니지만 동시에 많은 인증 API를 호출하는 앱에서는 안정성을 높인다.

Q. refresh 요청이 여러 번 나가면 뭐가 문제야?
A. token race condition, refresh token rotation 충돌, 불필요한 서버 부하가 발생할 수 있다.

---

# 4. Token Storage Criteria

## 4.1 Token Storage Options

### [개념]

Token Storage는 token을 브라우저 또는 memory 어디에 보관할지 결정하는 기준이다.

저장 위치는 보안, UX, 새로고침 복원, 구현 난이도에 영향을 준다.

어떤 저장 방식도 완전한 정답은 아니며 프로젝트 보안 요구사항과 Backend 정책에 맞춰 선택한다.

---

### [핵심]

저장 후보:

- Memory State
- localStorage
- sessionStorage
- HttpOnly Cookie
- Zustand Persist
- Redux Persist
- IndexedDB

비교:

| 저장 위치       | 장점                | 주의                     |
| --------------- | ------------------- | ------------------------ |
| Memory State    | XSS 노출 감소       | 새로고침 시 사라짐       |
| localStorage    | 새로고침 유지 쉬움  | XSS 노출 위험            |
| sessionStorage  | 탭 단위 유지        | XSS 노출 위험            |
| HttpOnly Cookie | JS 접근 불가        | CSRF / Backend 설정 고려 |
| Zustand Persist | 구현 편리           | 저장 대상 최소화 필요    |
| Redux Persist   | 전역 상태 유지 쉬움 | 민감정보 persist 주의    |

---

### [실무]

선택 기준:

```text
보안 우선
→ HttpOnly Cookie 또는 Memory State 검토

구현 단순성 우선
→ sessionStorage 또는 localStorage 검토

새로고침 유지 필요
→ sessionStorage / localStorage / Cookie 검토

Refresh Token 보호 우선
→ HttpOnly Cookie 검토

학습 프로젝트
→ sessionStorage 또는 localStorage 사용 가능
→ 위험성 문서화 필수
```

주의:

- localStorage token은 XSS에 취약할 수 있음
- sessionStorage도 XSS에는 취약
- HttpOnly Cookie는 JS 접근 불가
- Cookie Auth는 CSRF / SameSite / Secure 설정 필요
- refresh token은 access token보다 더 민감
- 민감정보를 persist store에 과도하게 저장하지 않음
- logout 시 모든 저장소 정리 필수
- 저장 위치와 Auth Restore Flow를 함께 설계

---

### [FAQ]

Q. token은 localStorage에 저장하면 돼?
A. 가능은 하지만 XSS 위험이 있다. 프로젝트 보안 요구사항에 따라 memory, sessionStorage, HttpOnly Cookie 등을 검토해야 한다.

Q. HttpOnly Cookie가 무조건 정답이야?
A. 항상 정답은 아니다. JS 접근 차단 장점이 있지만 CSRF, SameSite, Backend 설정 등 함께 고려해야 한다.

Q. sessionStorage는 안전해?
A. localStorage보다 유지 범위는 좁지만 XSS에 노출될 수 있으므로 완전히 안전하다고 볼 수 없다.

Q. token 저장 방식은 Frontend 혼자 정해도 돼?
A. 아니다. Backend 인증 방식, refresh token 정책, CORS, cookie 설정과 함께 결정해야 한다.

---

## 4.2 Memory State Token Storage

### [개념]

Memory State Token Storage는 token을 브라우저 영구 저장소에 저장하지 않고 JavaScript memory 상태에만 보관하는 방식이다.

XSS로 인한 persistent token 탈취 위험을 줄일 수 있지만 새로고침 시 token이 사라진다.

---

### [핵심]

장점:

- persistent storage 노출 감소
- logout cleanup 단순
- 저장소에 token 흔적 감소

주의:

- 새로고침 시 token 사라짐
- 앱 재시작 시 로그인 풀림
- refresh token cookie 조합 필요 가능
- 페이지 reload UX 고려 필요

---

### [실무]

Memory 저장 예:

```tsx
let accessTokenMemory: string | null = null;

export function setAccessToken(token: string) {
  accessTokenMemory = token;
}

export function getAccessToken() {
  return accessTokenMemory;
}

export function clearAccessToken() {
  accessTokenMemory = null;
}
```

Cookie Refresh 조합 Flow:

```text
App Start
→ accessToken memory empty
→ refresh token cookie exists
→ refresh access token
→ set access token in memory
→ call /me
→ set authenticated true
```

주의:

- 단독 memory 방식은 새로고침 유지가 어려움
- refresh token을 HttpOnly Cookie로 두고 access token만 memory에 둘 수 있음
- 여러 탭 간 인증 상태 동기화가 어려움
- SPA runtime 중에는 XSS로 memory 접근 가능성도 완전히 배제할 수 없음
- 보안 요구사항과 UX 요구사항 균형 필요

---

### [FAQ]

Q. token을 memory에만 저장하면 안전해?
A. persistent storage 노출은 줄지만 XSS 위험이 완전히 사라지는 것은 아니다. 새로고침 시 사라지는 UX 문제도 있다.

Q. memory 방식이면 새로고침 후 로그인이 풀려?
A. access token만 memory에 있으면 풀릴 수 있다. refresh token cookie와 조합하면 복원할 수 있다.

Q. 여러 탭에서 로그인 상태가 공유돼?
A. memory 방식만 사용하면 탭 간 공유가 어렵다.

---

## 4.3 localStorage / sessionStorage Token Storage

### [개념]

localStorage와 sessionStorage는 Frontend에서 token을 쉽게 저장하고 새로고침 후 복원할 수 있는 Web Storage다.

구현은 쉽지만 JavaScript로 접근 가능하므로 XSS에 취약할 수 있다.

---

### [핵심]

localStorage:

- 브라우저에 지속 저장
- 새로고침 / 브라우저 재시작 후 유지
- XSS 노출 위험
- logout 시 removeItem 필요

sessionStorage:

- 탭 단위 저장
- 탭 종료 시 제거
- XSS 노출 위험
- 탭 간 공유 어려움

---

### [실무]

Storage 유틸 예:

```tsx
const ACCESS_TOKEN_KEY = "accessToken";
const REFRESH_TOKEN_KEY = "refreshToken";

export function setTokens(accessToken: string, refreshToken?: string) {
  sessionStorage.setItem(ACCESS_TOKEN_KEY, accessToken);

  if (refreshToken) {
    sessionStorage.setItem(REFRESH_TOKEN_KEY, refreshToken);
  }
}

export function getAccessToken() {
  return sessionStorage.getItem(ACCESS_TOKEN_KEY);
}

export function getRefreshToken() {
  return sessionStorage.getItem(REFRESH_TOKEN_KEY);
}

export function clearTokens() {
  sessionStorage.removeItem(ACCESS_TOKEN_KEY);
  sessionStorage.removeItem(REFRESH_TOKEN_KEY);
}
```

주의:

- token key 이름 통일
- storage에 user personal data 과다 저장 금지
- access token / refresh token console.log 금지
- logout 시 clearTokens 필수
- refresh token을 Web Storage에 저장하는 것은 더 큰 위험
- XSS 방어가 약한 프로젝트에서는 신중히 사용
- storage event로 다른 탭 logout 동기화 가능

---

### [FAQ]

Q. localStorage에 token을 저장하면 무조건 안 돼?
A. 무조건 금지는 아니지만 XSS에 노출될 수 있어 보안 요구사항에 따라 신중히 결정해야 한다.

Q. sessionStorage는 localStorage보다 나아?
A. 탭 종료 시 사라지는 장점은 있지만 JavaScript 접근이 가능하므로 XSS 위험은 여전히 있다.

Q. refresh token도 localStorage에 저장해도 돼?
A. 가능은 하지만 refresh token은 더 민감하므로 HttpOnly Cookie 같은 대안을 우선 검토하는 것이 좋다.

Q. logout할 때 storage만 지우면 돼?
A. 아니다. Auth State와 user-specific cache도 함께 정리해야 한다.

---

## 4.4 HttpOnly Cookie Token Storage

### [개념]

HttpOnly Cookie Token Storage는 token을 JavaScript에서 직접 접근할 수 없는 cookie에 저장하는 방식이다.

Frontend는 token 값을 읽지 않고, API 요청 시 cookie가 자동 포함되거나 `withCredentials` 설정을 통해 전달된다.

---

### [핵심]

장점:

- JavaScript에서 token 직접 접근 불가
- token console.log 위험 감소
- refresh token 보호에 유리

주의:

- CSRF 대응 필요
- SameSite 설정 필요
- Secure 설정 필요
- CORS credentials 설정 필요
- Backend cookie 발급 설정 필요
- Frontend에서 token 값 확인 불가

---

### [실무]

Axios 설정 예:

```tsx
export const authApi = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  withCredentials: true,
});
```

Cookie Auth Restore Flow:

```text
App Start
→ Call /me with credentials
→ Backend reads HttpOnly Cookie
→ Success: return user summary
→ Frontend set authenticated true
→ Failure: clearAuth
```

주의:

- Frontend는 cookie 내부 token을 읽지 않음
- `/me` API로 인증 상태 복원
- CSRF token 전략이 필요할 수 있음
- SameSite=Lax / Strict / None 정책 확인
- SameSite=None이면 Secure 필요
- CORS `Access-Control-Allow-Credentials` 필요 가능
- cookie domain / path 설정 확인
- local 개발환경과 배포환경 cookie 정책 차이 주의

---

### [FAQ]

Q. HttpOnly Cookie를 쓰면 Frontend에서 token을 읽을 수 있어?
A. 아니다. HttpOnly Cookie는 JavaScript로 읽을 수 없고 Frontend는 `/me` API 응답으로 인증 상태를 확인한다.

Q. HttpOnly Cookie를 쓰면 Authorization Header가 필요 없어?
A. Cookie 기반 인증이면 필요 없을 수 있다. Backend 인증 방식에 따라 Header Auth와 Cookie Auth 중 기준을 통일해야 한다.

Q. Cookie Auth에서도 CSRF를 고려해야 해?
A. 해야 한다. Cookie는 자동 전송될 수 있으므로 SameSite, CSRF token, Backend 방어 정책을 함께 고려해야 한다.

Q. withCredentials는 언제 필요해?
A. cross-origin 요청에서 cookie를 포함해야 할 때 필요할 수 있으며 Backend CORS 설정과 함께 맞춰야 한다.

---

# 5. Token Security Rules

## 5.1 Token Logging and Exposure

### [개념]

Token Logging and Exposure는 token이 개발자 도구, console, URL, error log, analytics, monitoring 도구에 노출되는 것을 방지하는 기준이다.

token은 인증 권한을 가진 민감정보이므로 로그와 URL에 남기지 않아야 한다.

---

### [핵심]

금지:

- accessToken console.log
- refreshToken console.log
- Authorization Header log
- token URL query 유지
- token local error report 전송
- token analytics event 전송
- token hardcoding
- token screenshot 공유

주의 대상:

- browser console
- Network tab
- error boundary
- monitoring SDK
- URL query string
- localStorage inspection
- clipboard
- screenshot

---

### [실무]

금지 예:

```tsx
console.log(accessToken);
console.log(refreshToken);
console.log(error.config.headers.Authorization);
```

URL token 제거 예:

```tsx
function cleanTokenFromUrl() {
  window.history.replaceState({}, document.title, window.location.pathname);
}
```

Error Sanitizing 예:

```tsx
function sanitizeAuthError(error: unknown) {
  if (!isAxiosError(error)) {
    return error;
  }

  return {
    status: error.response?.status,
    message: error.message,
  };
}
```

주의:

- token 디버깅은 Network 탭에서 존재 여부만 확인
- token 전체 문자열 공유 금지
- OAuth2 callback에서 URL token 즉시 제거
- error reporting 도구에 Authorization Header 포함 금지
- `.env`에 secret 저장 금지
- Frontend 환경변수는 빌드 결과에 노출 가능

---

### [FAQ]

Q. token을 console.log로 찍어도 돼?
A. 안 된다. token은 인증에 사용되는 민감정보이므로 로그에 남기지 않는 것이 원칙이다.

Q. Authorization Header를 에러 로그에 남겨도 돼?
A. 안 된다. Authorization Header에는 token이 포함될 수 있으므로 로그 전송 전에 제거해야 한다.

Q. OAuth2 callback에서 URL에 token이 있으면?
A. 즉시 저장 또는 처리한 뒤 replace navigation으로 URL에서 token을 제거하는 것이 좋다.

---

## 5.2 Token Storage Security

### [개념]

Token Storage Security는 token을 브라우저에 저장할 때 발생할 수 있는 보안 위험을 줄이는 기준이다.

Token 저장 방식은 XSS, CSRF, 새로고침 복원, 사용자 경험, Backend 정책을 함께 고려해야 한다.

---

### [핵심]

주의 대상:

- localStorage
- sessionStorage
- memory
- HttpOnly Cookie
- XSS
- CSRF
- token leakage
- persistent storage
- browser extension
- shared computer
- refresh token exposure

기본 원칙:

- token 하드코딩 금지
- token 로그 출력 금지
- refresh token 신중히 저장
- 민감정보 persist 최소화
- logout cleanup 필수
- Backend 정책과 통일

---

### [실무]

저장 정책 예:

```text
학습 / 개인 프로젝트
→ sessionStorage access token
→ refresh token 없이 짧은 세션
→ 위험성 문서화

일반 웹 서비스
→ access token memory
→ refresh token HttpOnly Cookie
→ /me 기반 복원

보안 요구 높은 서비스
→ HttpOnly Secure Cookie
→ SameSite / CSRF 대응
→ refresh rotation
→ short-lived access token
```

주의:

- localStorage는 XSS에 취약할 수 있음
- HttpOnly Cookie는 CSRF 대응 필요
- 어떤 저장 방식도 만능은 아님
- Frontend 저장소 선택은 Backend 인증 정책과 함께 결정
- refresh token은 access token보다 더 민감
- 브라우저 확장 프로그램과 공유 PC 환경도 고려
- token 저장보다 XSS 방어와 권한 최소화가 중요

---

### [FAQ]

Q. localStorage에 token을 저장하면 보안상 위험해?
A. XSS가 발생하면 JavaScript로 token을 읽을 수 있으므로 위험할 수 있다.

Q. HttpOnly Cookie가 보안상 항상 최고야?
A. 항상 최고는 아니다. JS 접근 차단 장점은 있지만 CSRF, SameSite, Secure, CORS 설정이 함께 필요하다.

Q. refresh token은 어디에 저장하는 게 좋아?
A. 보안 요구가 있다면 HttpOnly Cookie를 우선 검토하고, Web Storage 저장은 신중히 결정해야 한다.

---

# 6. Token Cleanup Rules

## 6.1 Clear Token and Clear Auth

### [개념]

Clear Token은 저장된 Access Token과 Refresh Token을 제거하는 작업이다.

Clear Auth는 token 제거뿐 아니라 Auth State, user state, user-specific cache를 함께 정리하는 작업이다.

Token만 삭제하면 UI와 cache에 이전 사용자 정보가 남을 수 있다.

---

### [핵심]

정리 대상:

- accessToken
- refreshToken
- user
- authenticated
- authError
- tokenExpired
- auth store
- persisted storage
- user-specific query cache
- notification state
- private page state

기본 Flow:

```text
Logout or Refresh Failure
→ Clear Access Token
→ Clear Refresh Token
→ Clear User
→ Set Authenticated False
→ Clear User Cache
→ Redirect Login or Main
```

---

### [실무]

Clear Tokens 예:

```tsx
function clearTokens() {
  sessionStorage.removeItem("accessToken");
  sessionStorage.removeItem("refreshToken");
}
```

Clear Auth 예:

```tsx
function clearAuth() {
  clearTokens();

  setUser(null);
  setAuthenticated(false);
  setAuthError(null);
}
```

Cache 정리 예:

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

- token만 삭제하지 말고 user state도 정리
- authenticated false 처리 필수
- React Query / TanStack Query cache 정리 고려
- notification / message / private data state 정리
- persisted auth store 정리
- 다른 탭 logout 동기화 필요 가능
- refresh 실패 시에도 clearAuth 필요
- logout API 실패 여부와 local cleanup 정책 결정

---

### [FAQ]

Q. 로그아웃할 때 token만 지우면 돼?
A. 아니다. user state, authenticated 상태, 사용자별 cache, persisted store도 함께 정리해야 한다.

Q. refresh 실패 시 token을 유지해도 돼?
A. 권장하지 않는다. refresh 실패는 인증 복원 실패로 보고 token과 Auth State를 정리하는 것이 일반적이다.

Q. logout API가 실패하면 local token을 유지해야 해?
A. 프로젝트 정책에 따라 다르지만 사용자 입장에서는 로그아웃을 요청했으므로 local 인증 정보를 정리하는 경우가 많다.

---

## 6.2 Cross Tab Token Cleanup

### [개념]

Cross Tab Token Cleanup은 여러 브라우저 탭이 열려 있을 때 한 탭에서 로그아웃하면 다른 탭도 로그아웃 상태로 동기화하는 기준이다.

localStorage 또는 BroadcastChannel을 사용해 탭 간 인증 상태 변경을 전달할 수 있다.

---

### [핵심]

사용 상황:

- multiple tabs
- logout in one tab
- storage event
- BroadcastChannel
- clearAuth sync
- token removal sync
- stale user UI prevention

---

### [실무]

storage event 예:

```tsx
useEffect(() => {
  function handleStorageChange(event: StorageEvent) {
    if (event.key === "auth:logout") {
      clearAuth();
    }
  }

  window.addEventListener("storage", handleStorageChange);

  return () => {
    window.removeEventListener("storage", handleStorageChange);
  };
}, []);
```

logout broadcast 예:

```tsx
function broadcastLogout() {
  localStorage.setItem("auth:logout", String(Date.now()));
}
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
  }
};
```

주의:

- sessionStorage는 탭 간 공유되지 않음
- localStorage event는 같은 탭에서는 발생하지 않음
- BroadcastChannel 지원 범위 확인
- 동기화 후 route redirect 처리 필요
- user cache도 함께 정리
- 단순 프로젝트에서는 생략 가능

---

### [FAQ]

Q. 한 탭에서 로그아웃했는데 다른 탭은 로그인 상태야?
A. 탭 간 인증 상태 동기화가 없으면 발생할 수 있다. storage event나 BroadcastChannel을 사용할 수 있다.

Q. sessionStorage를 쓰면 탭 간 로그아웃 동기화가 돼?
A. 기본적으로 어렵다. sessionStorage는 탭 단위 저장소이므로 별도 broadcast가 필요하다.

Q. Cross Tab Logout은 필수야?
A. 실서비스 UX에서는 유용하지만 단순 학습 프로젝트에서는 우선순위를 낮출 수 있다.

---

# 7. Token Troubleshooting

## 7.1 Token Missing Troubleshooting

### [개념]

Token Missing 문제는 인증 API 요청에 token이 포함되지 않아 401이 발생하는 상황이다.

대부분 token 저장, Authorization Header, authApi 사용, interceptor 등록 중 하나가 누락되어 발생한다.

---

### [핵심]

확인 대상:

- token storage
- getAccessToken return value
- Authorization Header
- Bearer prefix
- authApi usage
- interceptor registration
- request timing
- login response mapping
- response.data.data unwrap
- token save timing

---

### [실무]

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

문제 예:

```text
문제: localStorage에 token은 있음
원인: authApi request interceptor에서 token을 읽지 않음
해결: getAccessToken과 Authorization Header 추가 로직 확인
```

문제 예:

```text
문제: 로그인 직후 첫 API만 401
원인: token 저장 전에 인증 API 요청 발생
해결: token 저장 완료 후 authenticated API 호출
```

주의:

- token이 저장되어도 Header에 없으면 인증 실패
- publicApi로 요청하면 header 누락 가능
- interceptor 설정 파일 import 누락 가능
- token 저장 전 API 요청이 먼저 발생할 수 있음
- tokenType 중복으로 Header가 잘못될 수 있음
- token 로그 출력은 금지

---

### [FAQ]

Q. localStorage에 token이 있는데 401이 나?
A. Network 탭에서 Authorization Header에 실제로 token이 포함되었는지 확인해야 한다.

Q. 로그인 직후 API만 401이 나?
A. token 저장 또는 Auth State 갱신이 완료되기 전에 인증 API 요청이 먼저 실행되었을 수 있다.

Q. 인증 API에 publicApi를 쓰면 어떻게 돼?
A. Authorization Header가 누락되어 401이 발생할 수 있다.

---

## 7.2 Refresh Loop Troubleshooting

### [개념]

Refresh Loop는 token 재발급 로직이 실패하거나 조건이 잘못되어 refresh 요청이 반복되는 문제다.

Refresh Loop는 사용자 경험과 서버 부하를 모두 악화시킨다.

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
- 여러 요청 동시 만료 처리 기준 필요
- login 실패 401과 token 만료 401 구분
- interceptor에서 error를 삼키지 않음

---

### [FAQ]

Q. refresh 요청이 계속 반복돼?
A. refresh API까지 401 interceptor가 재시도 대상으로 잡혔거나 retry 제한이 없을 가능성이 있다.

Q. refresh 실패 후에도 계속 API가 호출돼?
A. clearAuth와 redirect 처리가 누락되었거나 원래 요청 retry 제한이 없을 수 있다.

Q. refresh loop는 어떻게 막아?
A. `_retry` 플래그, refresh endpoint 제외, refresh 실패 시 clearAuth, Promise.reject 반환으로 막는다.

---

# 8. Part04 Review Checklist

## 8.1 Token Handling / Storage Checklist

### [개념]

Part04 검수는 Access Token, Refresh Token, Authorization Header, Token Storage, Refresh Flow, Token Security, Token Cleanup이 일관되게 연결되는지 확인한다.

---

### [핵심]

Checklist:

```md
- [ ] Access Token 역할이 명확한가?
- [ ] Refresh Token 역할이 명확한가?
- [ ] Authorization Header 형식이 포함되었는가?
- [ ] Bearer Token 기준이 포함되었는가?
- [ ] tokenType 중복 주의가 포함되었는가?
- [ ] Access Token Lifecycle이 포함되었는가?
- [ ] Refresh Token Flow가 포함되었는가?
- [ ] Refresh Retry Guard 기준이 포함되었는가?
- [ ] Concurrent Refresh Handling 기준이 포함되었는가?
- [ ] Token Storage Options 비교가 포함되었는가?
- [ ] Memory State 저장 기준이 포함되었는가?
- [ ] localStorage / sessionStorage 기준이 포함되었는가?
- [ ] HttpOnly Cookie 기준이 포함되었는가?
- [ ] Token Logging 금지가 포함되었는가?
- [ ] Token Storage Security 기준이 포함되었는가?
- [ ] Clear Token / Clear Auth 기준이 포함되었는가?
- [ ] Cross Tab Token Cleanup 기준이 포함되었는가?
- [ ] Token Missing Troubleshooting이 포함되었는가?
- [ ] Refresh Loop Troubleshooting이 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

Part04 이후 권장 문서 순서:

```text
Part04 Token Handling / Token Storage
→ Part05 Axios Auth Integration
→ Part06 Protected Route / Role Based Route
→ Part07 Logout / User Profile Fetch
→ Part08 OAuth2 Frontend Flow
→ Part09 401 / 403 / Troubleshooting
→ Part10 Security / Checklist / Retrieval Optimization
```

검수 기준:

```text
Token Receive
→ Token Storage
→ Authorization Header
→ Token Expired
→ Refresh Token
→ Retry Request
→ Token Cleanup
→ Security Review
```

---

### [FAQ]

Q. Part04의 핵심은 뭐야?
A. Access Token과 Refresh Token 처리, Authorization Header, Token Storage, Refresh Flow, Token Cleanup 기준을 정리하는 것이다.

Q. Part04에서 Axios Interceptor를 깊게 다뤄?
A. 기본 흐름은 포함하지만 Axios Instance와 Interceptor 상세 구현은 Part05에서 자세히 다룬다.

Q. Part04에서 Protected Route를 다뤄?
A. 아니다. Token 상태와 Route Guard 연결은 언급하지만 Protected Route 상세 구현은 별도 문서에서 다룬다.

---

# Retrieval Queries

### [FAQ]

Q. Access Token은 어디에 써?
A. 인증이 필요한 API 요청의 Authorization Header에 넣어 사용한다.

Q. Refresh Token은 어디에 써?
A. Access Token이 만료되었을 때 새 Access Token을 발급받는 데 사용한다.

Q. Frontend가 token을 검증해?
A. 아니다. Frontend는 token을 사용하고 실제 검증은 Backend가 수행한다.

Q. Authorization Header 형식은 뭐야?
A. 일반적으로 `Authorization: Bearer <accessToken>` 형식을 사용한다.

Q. Bearer를 빼먹으면 어떻게 돼?
A. Backend가 token 형식을 인식하지 못해 401이 발생할 수 있다.

Q. tokenType이 Bearer로 오면 어떻게 해?
A. Authorization Header 생성 시 `Bearer Bearer token`처럼 중복되지 않도록 처리 기준을 통일해야 한다.

Q. token은 있는데 401이 나?
A. Authorization Header에 실제로 포함되었는지, Bearer 형식이 맞는지, token이 만료되지 않았는지 확인해야 한다.

Q. access token이 만료되면 어떻게 해?
A. refresh token이 있으면 새 access token을 요청하고 성공 시 원래 API 요청을 재시도할 수 있다.

Q. access token은 항상 localStorage에 저장해?
A. 아니다. memory, sessionStorage, localStorage, cookie 등 프로젝트 보안 요구사항에 따라 선택한다.

Q. access token을 삭제하면 로그아웃이야?
A. token 삭제만으로는 부족하다. user state, authenticated 상태, cache도 함께 정리해야 한다.

Q. refresh token은 어떻게 처리해?
A. access token 만료로 401이 발생하면 refresh token으로 새 access token을 요청하고 성공 시 원래 요청을 재시도한다.

Q. refresh 요청도 실패하면?
A. 인증 정보를 정리하고 login 페이지로 이동시키는 것이 일반적이다.

Q. refresh 요청이 무한 반복될 수 있어?
A. 잘못 구현하면 가능하다. refresh 요청 자체에는 retry를 걸지 않거나 `_retry` 같은 플래그로 반복을 막아야 한다.

Q. refresh token은 access token보다 더 중요해?
A. 그렇다. refresh token은 새 access token을 발급받을 수 있으므로 더 민감하게 다뤄야 한다.

Q. `_retry` 플래그는 왜 필요해?
A. 같은 요청이 401을 계속 받을 때 refresh와 retry가 무한 반복되는 것을 막기 위해 필요하다.

Q. refresh API도 401이면 다시 refresh를 시도해?
A. 아니다. refresh API 실패는 인증 복원 실패로 보고 clearAuth 또는 login redirect 처리해야 한다.

Q. Login API 401도 refresh를 시도해야 해?
A. 아니다. Login API 401은 로그인 실패로 처리해야 하며 token 만료 401과 구분해야 한다.

Q. 여러 API가 동시에 401이면 어떻게 해?
A. refresh 요청을 하나만 수행하고 나머지 요청은 대기시킨 뒤 새 token으로 재시도하는 queue 방식이 필요할 수 있다.

Q. concurrent refresh 처리는 꼭 필요해?
A. 모든 프로젝트에서 필수는 아니지만 동시에 많은 인증 API를 호출하는 앱에서는 안정성을 높인다.

Q. token은 localStorage에 저장하면 돼?
A. 가능은 하지만 XSS 위험이 있다. 프로젝트 보안 요구사항에 따라 memory, sessionStorage, HttpOnly Cookie 등을 검토해야 한다.

Q. HttpOnly Cookie가 무조건 정답이야?
A. 항상 정답은 아니다. JS 접근 차단 장점이 있지만 CSRF, SameSite, Backend 설정 등 함께 고려해야 한다.

Q. sessionStorage는 안전해?
A. localStorage보다 유지 범위는 좁지만 XSS에 노출될 수 있으므로 완전히 안전하다고 볼 수 없다.

Q. token 저장 방식은 Frontend 혼자 정해도 돼?
A. 아니다. Backend 인증 방식, refresh token 정책, CORS, cookie 설정과 함께 결정해야 한다.

Q. token을 memory에만 저장하면 안전해?
A. persistent storage 노출은 줄지만 XSS 위험이 완전히 사라지는 것은 아니다. 새로고침 시 사라지는 UX 문제도 있다.

Q. memory 방식이면 새로고침 후 로그인이 풀려?
A. access token만 memory에 있으면 풀릴 수 있다. refresh token cookie와 조합하면 복원할 수 있다.

Q. localStorage에 token을 저장하면 무조건 안 돼?
A. 무조건 금지는 아니지만 XSS에 노출될 수 있어 보안 요구사항에 따라 신중히 결정해야 한다.

Q. sessionStorage는 localStorage보다 나아?
A. 탭 종료 시 사라지는 장점은 있지만 JavaScript 접근이 가능하므로 XSS 위험은 여전히 있다.

Q. refresh token도 localStorage에 저장해도 돼?
A. 가능은 하지만 refresh token은 더 민감하므로 HttpOnly Cookie 같은 대안을 우선 검토하는 것이 좋다.

Q. HttpOnly Cookie를 쓰면 Frontend에서 token을 읽을 수 있어?
A. 아니다. HttpOnly Cookie는 JavaScript로 읽을 수 없고 Frontend는 `/me` API 응답으로 인증 상태를 확인한다.

Q. HttpOnly Cookie를 쓰면 Authorization Header가 필요 없어?
A. Cookie 기반 인증이면 필요 없을 수 있다. Backend 인증 방식에 따라 Header Auth와 Cookie Auth 중 기준을 통일해야 한다.

Q. Cookie Auth에서도 CSRF를 고려해야 해?
A. 해야 한다. Cookie는 자동 전송될 수 있으므로 SameSite, CSRF token, Backend 방어 정책을 함께 고려해야 한다.

Q. withCredentials는 언제 필요해?
A. cross-origin 요청에서 cookie를 포함해야 할 때 필요할 수 있으며 Backend CORS 설정과 함께 맞춰야 한다.

Q. token을 console.log로 찍어도 돼?
A. 안 된다. token은 인증에 사용되는 민감정보이므로 로그에 남기지 않는 것이 원칙이다.

Q. Authorization Header를 에러 로그에 남겨도 돼?
A. 안 된다. Authorization Header에는 token이 포함될 수 있으므로 로그 전송 전에 제거해야 한다.

Q. OAuth2 callback에서 URL에 token이 있으면?
A. 즉시 저장 또는 처리한 뒤 replace navigation으로 URL에서 token을 제거하는 것이 좋다.

Q. localStorage에 token을 저장하면 보안상 위험해?
A. XSS가 발생하면 JavaScript로 token을 읽을 수 있으므로 위험할 수 있다.

Q. refresh token은 어디에 저장하는 게 좋아?
A. 보안 요구가 있다면 HttpOnly Cookie를 우선 검토하고, Web Storage 저장은 신중히 결정해야 한다.

Q. 로그아웃할 때 token만 지우면 돼?
A. 아니다. user state, authenticated 상태, 사용자별 cache, persisted store도 함께 정리해야 한다.

Q. refresh 실패 시 token을 유지해도 돼?
A. 권장하지 않는다. refresh 실패는 인증 복원 실패로 보고 token과 Auth State를 정리하는 것이 일반적이다.

Q. 한 탭에서 로그아웃했는데 다른 탭은 로그인 상태야?
A. 탭 간 인증 상태 동기화가 없으면 발생할 수 있다. storage event나 BroadcastChannel을 사용할 수 있다.

Q. sessionStorage를 쓰면 탭 간 로그아웃 동기화가 돼?
A. 기본적으로 어렵다. sessionStorage는 탭 단위 저장소이므로 별도 broadcast가 필요하다.

Q. 로그인 직후 API만 401이 나?
A. token 저장 또는 Auth State 갱신이 완료되기 전에 인증 API 요청이 먼저 실행되었을 수 있다.

Q. 인증 API에 publicApi를 쓰면 어떻게 돼?
A. Authorization Header가 누락되어 401이 발생할 수 있다.

Q. refresh 요청이 계속 반복돼?
A. refresh API까지 401 interceptor가 재시도 대상으로 잡혔거나 retry 제한이 없을 가능성이 있다.

Q. refresh loop는 어떻게 막아?
A. `_retry` 플래그, refresh endpoint 제외, refresh 실패 시 clearAuth, Promise.reject 반환으로 막는다.

Q. Part04 다음 문서는 뭐야?
A. Axios Auth Integration 문서가 이어지는 것이 좋다.
