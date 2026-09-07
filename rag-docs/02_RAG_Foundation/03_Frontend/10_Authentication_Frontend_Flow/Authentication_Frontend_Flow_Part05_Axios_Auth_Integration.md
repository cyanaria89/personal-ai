# Authentication Frontend Flow Part05 - Axios Auth Integration / Interceptor / API Client

---

# 1. Axios Auth Integration Overview

## 1.1 Public API and Auth API

### [개념]

Axios Auth Integration은 Frontend에서 인증이 필요한 API 요청과 인증이 필요 없는 API 요청을 분리하고, token 또는 cookie 인증 정보를 일관되게 포함시키는 API Client 구성 기준이다.

Public API는 인증이 필요 없는 요청에 사용한다.

Auth API는 Authorization Header 또는 Cookie 인증이 필요한 요청에 사용한다.

이 문서는 token storage 자체보다 Axios Instance, Request Interceptor, Response Interceptor, 401 / 403 처리, refresh retry 연결에 집중한다.

Token 저장 정책과 Access Token / Refresh Token lifecycle은 Token Handling 문서에서 다룬다.

---

### [핵심]

핵심 키워드:

- Axios Auth Integration
- Axios Instance
- publicApi
- authApi
- baseURL
- Authorization Header
- Bearer Token
- Request Interceptor
- Response Interceptor
- 401 Handling
- 403 Handling
- Token Refresh
- Retry Original Request
- Promise.reject
- API Response Unwrap
- Auth Event Pattern
- Error Normalization

구분 기준:

```text
publicApi
→ Login API
→ Signup API
→ Public Search API
→ Public Content API
→ Refresh API 선택 가능
→ 인증 필요 없는 요청
```

```text
authApi
→ Me API
→ MyPage API
→ Favorite API
→ Notification API
→ Profile API
→ 인증 필요 API
```

---

### [실무]

기본 구조:

```tsx
import axios from "axios";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export const publicApi = axios.create({
  baseURL: API_BASE_URL,
});

export const authApi = axios.create({
  baseURL: API_BASE_URL,
});
```

사용 예:

```tsx
export function login(requestBody: LoginRequest) {
  return publicApi.post("/auth/login", requestBody);
}

export function signup(requestBody: SignupRequest) {
  return publicApi.post("/auth/signup", requestBody);
}

export function getMe() {
  return authApi.get("/users/me");
}

export function getMyFavorites() {
  return authApi.get("/favorites");
}
```

권장 기준:

- 인증 필요 API에 authApi 사용
- 인증 불필요 API에 publicApi 사용
- Login / Signup은 보통 publicApi 사용
- `/me` API는 authApi 사용
- baseURL 중복 관리 금지
- API 함수에서 response unwrap 기준 통일
- 인증 필요 API에 publicApi 사용 금지
- 공개 API에 불필요한 Authorization Header 전송 지양
- refresh endpoint는 publicApi 또는 별도 refreshApi 사용 가능
- Cookie Auth에서는 authApi에 `withCredentials` 설정 가능

주의:

```text
인증 API에 publicApi 사용
→ Authorization Header 누락
→ 401 Unauthorized 발생 가능
```

```text
공개 API에 authApi 사용
→ 불필요한 token 전송
→ 로그 / 모니터링 / 캐시 정책 혼선 가능
```

---

### [FAQ]

Q. publicApi와 authApi를 나누는 이유는?
A. 인증이 필요 없는 요청과 Authorization Header가 필요한 요청을 명확히 구분하기 위해서다.

Q. 인증 API에 publicApi를 쓰면 어떻게 돼?
A. Authorization Header가 누락되어 401이 발생할 수 있다.

Q. Login API도 authApi로 호출해야 해?
A. 보통 로그인 전에는 token이 없으므로 Login API는 publicApi로 호출한다.

Q. Refresh API는 publicApi야 authApi야?
A. access token header가 필요 없다면 publicApi 또는 별도 refreshApi를 사용할 수 있다. 프로젝트 Backend 정책에 맞춘다.

Q. 공개 API에 token을 보내도 돼?
A. 가능은 하지만 불필요한 token 노출을 줄이기 위해 공개 API에는 publicApi를 사용하는 것이 좋다.

---

# 2. Axios Instance Rules

## 2.1 Base URL and Environment Variable

### [개념]

Base URL은 Frontend API Client가 요청을 보낼 Backend 서버 주소다.

환경별 API 주소가 달라질 수 있으므로 `.env` 또는 환경변수 기반으로 관리한다.

Frontend 환경변수는 빌드 결과에 노출될 수 있으므로 secret을 저장하면 안 된다.

---

### [핵심]

확인 대상:

- VITE_API_BASE_URL
- REACT_APP_API_BASE_URL
- import.meta.env
- process.env
- development baseURL
- production baseURL
- relative path
- proxy
- CORS
- secret exposure

환경 기준:

```text
Vite
→ import.meta.env.VITE_API_BASE_URL
```

```text
Create React App
→ process.env.REACT_APP_API_BASE_URL
```

---

### [실무]

Vite 예:

```tsx
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export const publicApi = axios.create({
  baseURL: API_BASE_URL,
});

export const authApi = axios.create({
  baseURL: API_BASE_URL,
});
```

CRA 예:

```tsx
const API_BASE_URL = process.env.REACT_APP_API_BASE_URL;

export const publicApi = axios.create({
  baseURL: API_BASE_URL,
});
```

`.env` 예:

```env
VITE_API_BASE_URL=http://localhost:8080/api
```

주의:

- Frontend `.env`에 OAuth secret 저장 금지
- Frontend `.env`에 private API key 저장 금지
- Frontend `.env`에 JWT secret 저장 금지
- 환경변수 prefix 확인
- baseURL 마지막 slash 중복 주의
- endpoint path slash 기준 통일
- 배포환경 CORS 설정 확인
- CRA와 Vite 환경변수 접근 방식 구분

---

### [FAQ]

Q. Frontend .env에 API 서버 주소를 넣어도 돼?
A. 가능하다. API base URL처럼 공개되어도 되는 값은 넣을 수 있다.

Q. Frontend .env에 OAuth secret을 넣어도 돼?
A. 안 된다. Frontend 환경변수는 빌드 결과에 노출될 수 있으므로 secret을 넣으면 안 된다.

Q. Vite와 CRA의 환경변수 이름이 달라?
A. 다르다. Vite는 `VITE_` prefix와 `import.meta.env`를 사용하고 CRA는 `REACT_APP_` prefix와 `process.env`를 사용한다.

Q. baseURL 끝에 slash가 있으면 문제야?
A. endpoint path와 합쳐질 때 `//`가 생길 수 있으므로 프로젝트 기준을 통일하는 것이 좋다.

---

## 2.2 API Function Layer

### [개념]

API Function Layer는 Component가 Axios를 직접 호출하지 않고 도메인별 API 함수로 요청을 분리하는 구조다.

API 함수를 분리하면 response unwrap, error handling, endpoint 관리, authApi 사용 기준을 통일할 수 있다.

---

### [핵심]

구성 기준:

- authApi.ts
- userApi.ts
- profileApi.ts
- festivalApi.ts
- favoriteApi.ts
- notificationApi.ts
- login function
- signup function
- getMe function
- response unwrap
- request DTO mapping
- response DTO typing

권장 구조:

```text
Component
→ Custom Hook
→ API Function
→ Axios Instance
→ Backend API
```

---

### [실무]

API 함수 예:

```tsx
export async function login(requestBody: LoginRequest) {
  const response = await publicApi.post<ApiResponse<LoginResponse>>(
    "/auth/login",
    requestBody,
  );

  return response.data.data;
}

export async function getMe() {
  const response = await authApi.get<ApiResponse<AuthUser>>("/users/me");

  return response.data.data;
}
```

Component 사용 예:

```tsx
async function handleLogin(values: LoginFormValues) {
  const result = await login(toLoginRequest(values));

  applyLoginResult(result);
}
```

주의:

- Component에서 endpoint 문자열 직접 반복 금지
- response.data.data unwrap 기준 API 함수에서 통일
- authApi / publicApi 선택을 API 함수에서 결정
- DTO 변환 함수와 API 호출 함수 역할 분리
- TypeScript 타입으로 request / response 명확화
- 인증 오류 공통 처리는 interceptor 또는 hook과 연결
- 일반 Error Toast / Loading Skeleton / Empty State UX는 Error Handling & Loading UX 문서에서 다룸

---

### [FAQ]

Q. Component에서 바로 axios.get을 호출해도 돼?
A. 가능은 하지만 endpoint, unwrap, error handling이 흩어지므로 API 함수 계층으로 분리하는 것이 유지보수에 좋다.

Q. response.data.data unwrap은 어디서 해?
A. API 함수에서 통일하는 것이 좋다. Component가 Backend wrapper 구조를 직접 알지 않도록 한다.

Q. authApi와 publicApi 선택은 어디서 해?
A. API 함수 계층에서 endpoint 성격에 맞게 선택하는 것이 좋다.

Q. API 함수는 인증 오류 메시지도 전부 처리해야 해?
A. 공통 인증 처리는 interceptor와 연결하고 화면별 메시지는 hook 또는 Component에서 처리하는 것이 좋다.

---

# 3. Request Interceptor Rules

## 3.1 Authorization Header Attach

### [개념]

Request Interceptor는 API 요청이 서버로 전송되기 전에 Authorization Header 같은 공통 값을 추가하는 기능이다.

인증이 필요한 요청에는 Access Token을 `Authorization: Bearer <accessToken>` 형식으로 포함한다.

---

### [핵심]

사용 대상:

- access token attach
- Authorization Header
- Bearer Token
- request config
- token getter
- request reject
- authApi only
- token missing skip

Header 형식:

```text
Authorization: Bearer <accessToken>
```

---

### [실무]

기본 예:

```tsx
authApi.interceptors.request.use(
  (config) => {
    const accessToken = getAccessToken();

    if (accessToken) {
      config.headers.Authorization = `Bearer ${accessToken}`;
    }

    return config;
  },
  (error) => Promise.reject(error),
);
```

유틸 분리 예:

```tsx
function attachAuthorizationHeader(config: InternalAxiosRequestConfig) {
  const accessToken = getAccessToken();

  if (!accessToken) {
    return config;
  }

  config.headers.Authorization = `Bearer ${accessToken}`;

  return config;
}
```

주의:

- token이 없으면 Header 생략
- token 로그 출력 금지
- Authorization spelling 확인
- Bearer prefix 확인
- Bearer 뒤 공백 확인
- `Bearer undefined` 금지
- `Bearer Bearer token` 중복 금지
- request interceptor는 authApi에만 적용
- publicApi에는 불필요한 Authorization Header 지양

---

### [FAQ]

Q. Authorization Header를 매 API 함수마다 넣어야 해?
A. 가능하지만 authApi request interceptor에서 공통 처리하는 것이 유지보수에 좋다.

Q. token이 없을 때 Authorization Header를 빈 값으로 넣어도 돼?
A. 권장하지 않는다. token이 없으면 Header 자체를 생략하는 것이 좋다.

Q. Request Interceptor에서 token을 console.log로 확인해도 돼?
A. 안 된다. token은 민감정보이므로 로그에 남기지 않는다.

Q. Header에 Bearer undefined가 들어가?
A. token getter가 undefined를 반환했는데 Header를 무조건 추가했을 가능성이 있다.

---

## 3.2 Request Interceptor Registration

### [개념]

Request Interceptor Registration은 interceptor 설정 코드가 언제, 어디에서, 몇 번 실행되는지 관리하는 기준이다.

interceptor가 중복 등록되면 요청마다 같은 로직이 여러 번 실행되거나 Header가 예상과 다르게 처리될 수 있다.

---

### [핵심]

확인 대상:

- setup file
- module import
- duplicate registration
- React StrictMode
- AuthProvider remount
- interceptor eject
- single initialization
- app bootstrap

권장 위치:

```text
apiClient.ts
→ axios instance 생성
→ interceptor 1회 등록
→ API 함수에서 instance import
```

---

### [실무]

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

지양 구조:

```tsx
function SomeComponent() {
  authApi.interceptors.request.use((config) => {
    return config;
  });

  return null;
}
```

eject가 필요한 예:

```tsx
useEffect(() => {
  const interceptorId = authApi.interceptors.response.use(
    (response) => response,
    (error) => Promise.reject(error),
  );

  return () => {
    authApi.interceptors.response.eject(interceptorId);
  };
}, []);
```

주의:

- Component render 내부에서 interceptor 등록 금지
- AuthProvider가 remount될 때 중복 등록 주의
- interceptor ID를 저장하고 eject할 수 있음
- 설정 파일 import 누락 시 interceptor가 동작하지 않을 수 있음
- 테스트 환경에서 interceptor 초기화 순서 확인
- Hot Reload 중 중복 등록 가능성 주의

---

### [FAQ]

Q. interceptor가 여러 번 실행돼?
A. 설정 코드가 여러 번 실행되어 interceptor가 중복 등록되면 같은 로직이 반복될 수 있다. 초기화 위치를 통일해야 한다.

Q. interceptor는 Component 안에서 등록해도 돼?
A. 권장하지 않는다. Component가 렌더링될 때마다 중복 등록될 수 있다.

Q. interceptor 설정 파일을 import하지 않으면?
A. 설정 코드가 실행되지 않아 Authorization Header가 붙지 않을 수 있다.

Q. eject는 언제 필요해?
A. Component 또는 Hook 내부에서 부득이하게 등록하는 경우 cleanup으로 eject가 필요하다. 가능하면 module scope 등록을 우선한다.

---

## 3.3 Request Metadata and Credentials

### [개념]

Request Metadata는 API 요청에 추가로 포함하는 공통 정보다.

인증 흐름에서는 Authorization Header 외에도 cookie 전달을 위한 `withCredentials`, locale header, request id, CSRF token 등을 사용할 수 있다.

---

### [핵심]

추가 후보:

- withCredentials
- Accept-Language
- X-Request-Id
- Content-Type
- CSRF Token
- Timezone
- Client Version

주의 대상:

- Authorization Header
- Cookie
- CORS
- CSRF
- secret header
- sensitive metadata

---

### [실무]

Cookie Auth 예:

```tsx
export const authApi = axios.create({
  baseURL: API_BASE_URL,
  withCredentials: true,
});
```

Locale Header 예:

```tsx
authApi.interceptors.request.use((config) => {
  config.headers["Accept-Language"] = "ko-KR";

  return config;
});
```

CSRF Token 예:

```tsx
authApi.interceptors.request.use((config) => {
  const csrfToken = getCsrfToken();

  if (csrfToken) {
    config.headers["X-CSRF-Token"] = csrfToken;
  }

  return config;
});
```

주의:

- Cookie Auth는 Backend CORS credentials 설정과 맞춰야 함
- CSRF Token 방식은 Backend 정책과 맞춤
- 민감한 secret을 Header에 넣지 않음
- Authorization Header와 Cookie Auth를 혼용할 경우 기준 명확화
- Content-Type은 FormData 요청에서 자동 설정을 고려
- 공통 Header가 모든 API에 필요한지 검토

---

### [FAQ]

Q. withCredentials는 언제 써?
A. cross-origin 요청에서 cookie를 포함해야 할 때 필요할 수 있으며 Backend CORS 설정과 함께 맞춰야 한다.

Q. Authorization Header 방식과 Cookie Auth 방식을 같이 써도 돼?
A. 가능은 하지만 인증 기준이 혼란스러워질 수 있으므로 프로젝트 기준을 명확히 해야 한다.

Q. CSRF Token Header는 Frontend에서 넣어야 해?
A. Backend가 CSRF Token 방식을 요구한다면 Frontend에서 해당 Header를 포함해야 한다.

Q. Header에 secret을 넣어도 돼?
A. Frontend secret은 노출될 수 있으므로 server-only secret을 Header에 넣으면 안 된다.

---

# 4. Response Interceptor Rules

## 4.1 Response Interceptor Overview

### [개념]

Response Interceptor는 서버 응답이나 에러를 Component로 전달하기 전에 공통 처리하는 기능이다.

인증 흐름에서는 401 처리, token refresh, 403 처리, auth expired event, error normalization에 사용할 수 있다.

---

### [핵심]

사용 대상:

- 401 Handling
- 403 Handling
- Token Refresh
- Retry Original Request
- Logout
- Clear Auth
- Auth Expired Event
- Error Normalization
- Promise.reject
- Refresh Loop Prevention

기본 Flow:

```text
API Response
→ Success: return response
→ Error: inspect status
→ 401: refresh or clearAuth
→ 403: forbidden handling
→ others: Promise.reject
```

---

### [실무]

기본 예:

```tsx
authApi.interceptors.response.use(
  (response) => response,
  async (error) => {
    const status = error.response?.status;

    if (status === 401) {
      clearAuth();
      emitAuthExpired();
    }

    return Promise.reject(error);
  },
);
```

성공 응답 unwrap은 interceptor보다 API 함수에서 처리 권장:

```tsx
export async function getMe() {
  const response = await authApi.get<ApiResponse<AuthUser>>("/users/me");

  return response.data.data;
}
```

주의:

- 에러를 삼키지 말고 Promise.reject로 전달
- 401 / 403 구분
- refresh token flow가 있으면 무한 loop 방지
- 원래 요청 retry는 제한
- login API / refresh API에는 별도 처리 필요 가능
- UI 메시지는 호출부에서 처리할 수 있게 유지
- response unwrap을 interceptor에서 전역 처리하면 타입 추론이 복잡해질 수 있음
- interceptor에서 React hook 직접 사용 금지

---

### [FAQ]

Q. Response Interceptor에서 401을 처리하면 Component에서는 에러 처리를 안 해도 돼?
A. 아니다. 공통 인증 처리는 interceptor에서 하고, 화면별 사용자 메시지는 Component나 hook에서 처리할 수 있다.

Q. interceptor에서 Promise.reject를 왜 해?
A. 호출한 API 함수나 화면에서도 에러를 인식하고 적절한 UI를 보여줄 수 있게 하기 위해서다.

Q. response.data.data unwrap을 interceptor에서 해도 돼?
A. 가능은 하지만 TypeScript 타입 추론과 예외 처리가 복잡해질 수 있어 API 함수에서 통일하는 방식이 안정적이다.

Q. interceptor에서 useNavigate를 써도 돼?
A. React Router hook은 Component 내부에서만 사용할 수 있으므로 interceptor 일반 모듈에서 직접 사용하면 안 된다.

---

## 4.2 401 Handling in Response Interceptor

### [개념]

401 Handling은 인증되지 않았거나 Access Token이 유효하지 않을 때 발생하는 응답을 처리하는 흐름이다.

Response Interceptor는 401을 감지해 Refresh Token Flow를 시도하거나 Auth State를 정리할 수 있다.

---

### [핵심]

401 원인:

- token 없음
- token 만료
- token 위조
- Bearer 형식 오류
- Authorization Header 누락
- refresh 실패
- 로그인 필요 API 접근

처리 후보:

- refresh token 시도
- original request retry
- clearAuth
- auth expired event
- login redirect
- user message
- Promise.reject

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

    if (status === 401 && originalRequest && !originalRequest._retry) {
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
- 원래 요청 retry는 1회만
- refresh 실패 시 clearAuth
- redirect는 interceptor 내부보다 auth event 또는 router 계층에서 처리 가능
- interceptor에서 React hook 직접 사용 금지
- Promise.reject로 호출부에 에러 전달

---

### [FAQ]

Q. 401이 나오면 무조건 로그아웃해야 해?
A. refresh token flow가 있으면 먼저 재발급을 시도할 수 있다. 재발급 실패 시 로그아웃 처리한다.

Q. Login API 실패 401도 interceptor에서 refresh해야 해?
A. 아니다. Login API 실패 401은 로그인 실패로 처리하고 token 만료 401과 구분해야 한다.

Q. refresh endpoint가 401이면 어떻게 해?
A. refresh 실패로 보고 clearAuth 후 login redirect 처리하는 것이 일반적이다.

Q. 401 처리 후 Component catch도 실행돼야 해?
A. 화면별 메시지 처리가 필요하면 interceptor에서 Promise.reject를 반환해야 한다.

---

## 4.3 403 Handling in Response Interceptor

### [개념]

403 Handling은 인증은 되었지만 접근 권한이 부족한 응답을 처리하는 흐름이다.

403은 인증 실패가 아니라 인가 실패이므로 기본적으로 Auth State를 지우지 않는다.

---

### [핵심]

403 원인:

- role 부족
- 관리자 권한 없음
- 작성자 / 소유자 불일치
- 접근 금지 리소스
- Backend Authorization 실패

처리 기준:

- Do Not Clear Auth by Default
- Forbidden Page
- Permission Denied Message
- Previous Page
- Role Refetch
- Promise.reject

---

### [실무]

기본 처리:

```tsx
authApi.interceptors.response.use(
  (response) => response,
  (error) => {
    const status = error.response?.status;

    if (status === 403) {
      markForbiddenError(error);
    }

    return Promise.reject(error);
  },
);
```

화면 처리 예:

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

주의:

- 403을 login redirect로 처리하지 않음
- 403에서 clearAuth 기본 처리 금지
- 인증 상태는 유지될 수 있음
- 권한 없음 화면 또는 메시지 표시
- role 정보가 오래되었으면 `/me` refetch 가능
- 사용자에게 내부 권한 정책 과다 노출 금지
- Backend Authorization이 최종 권한 판단 기준

---

### [FAQ]

Q. 403이면 로그아웃해야 해?
A. 대부분 아니다. 인증은 되었지만 권한이 없는 상태이므로 권한 없음 화면이나 메시지를 보여주는 것이 일반적이다.

Q. 403과 401을 같은 방식으로 처리해도 돼?
A. 권장하지 않는다. 401은 인증 문제, 403은 권한 문제다.

Q. 403에서 login 페이지로 보내도 돼?
A. 권장하지 않는다. 이미 로그인된 사용자라면 forbidden page나 권한 없음 메시지가 더 적절하다.

Q. 403이 나면 role을 다시 조회해야 해?
A. role 변경 가능성이 있는 서비스라면 `/me` refetch로 최신 권한을 확인할 수 있다.

---

# 5. Refresh Interceptor Pattern

## 5.1 Retry Original Request

### [개념]

Retry Original Request는 Access Token 만료로 실패한 원래 요청을 Refresh Token으로 새 Access Token을 받은 뒤 다시 실행하는 Axios Response Interceptor 패턴이다.

Token lifecycle 설명은 Token Handling 문서의 범위이고, 이 섹션은 Axios에서 `originalRequest`를 어떻게 retry하는지에 집중한다.

---

### [핵심]

Flow:

```text
Original Request
→ 401 Unauthorized
→ Response Interceptor
→ Refresh Access Token
→ Save New Access Token
→ Update Original Request Header
→ Retry Original Request
→ Return Retried Response
```

필수 요소:

- originalRequest
- `_retry`
- refreshAccessToken
- newAccessToken
- Authorization Header update
- authApi(originalRequest)
- Promise.reject on failure
- refresh endpoint exclude

---

### [실무]

구현 예:

```tsx
authApi.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    if (error.response?.status !== 401) {
      return Promise.reject(error);
    }

    if (!originalRequest || originalRequest._retry) {
      return Promise.reject(error);
    }

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
  },
);
```

주의:

- originalRequest가 없을 수 있으므로 방어 코드 필요
- retry는 한 번만 수행
- refresh 실패 시 원래 요청 재시도 금지
- 새 token 저장 후 Header 갱신
- authApi(originalRequest) 반환 필요
- Promise chain이 끊기지 않도록 return 필수
- mutation 요청 retry는 중복 실행 위험 검토
- 결제 / 주문 / 중복 생성 요청은 idempotency 검토

---

### [FAQ]

Q. original request retry는 왜 필요해?
A. access token 만료로 실패한 요청을 새 token으로 다시 보내 사용자 작업을 이어가기 위해 필요하다.

Q. 원래 요청 retry는 여러 번 해도 돼?
A. 권장하지 않는다. `_retry` 플래그로 1회만 재시도해야 refresh loop를 막을 수 있다.

Q. POST 요청도 자동 retry해도 돼?
A. 가능하지만 결제, 주문, 중복 생성 같은 요청은 idempotency와 중복 실행 위험을 검토해야 한다.

Q. refresh 성공했는데 다음 요청도 401이야?
A. 새 access token 저장이 누락되었거나 원래 요청 Header에 이전 token이 남아 있을 수 있다.

---

## 5.2 Exclude Refresh and Login Endpoint

### [개념]

Refresh and Login Endpoint Exclusion은 refresh API와 login API를 global 401 refresh 처리 대상에서 제외하는 기준이다.

refresh API의 401까지 refresh 대상으로 잡으면 무한 루프가 발생할 수 있다.

---

### [핵심]

제외 대상:

- /auth/login
- /auth/signup
- /auth/refresh
- /oauth/callback
- /oauth2/callback
- password reset
- public endpoint

제외 이유:

- Login API 401은 로그인 실패
- Refresh API 401은 refresh 실패
- Signup API 401은 인증 만료가 아님
- Public API는 token refresh 대상 아님
- OAuth2 Callback은 별도 흐름

---

### [실무]

URL 제외 예:

```tsx
function isAuthExcludedUrl(url?: string) {
  if (!url) {
    return false;
  }

  return (
    url.includes("/auth/login") ||
    url.includes("/auth/signup") ||
    url.includes("/auth/refresh") ||
    url.includes("/oauth/callback") ||
    url.includes("/oauth2/callback")
  );
}
```

interceptor 적용 예:

```tsx
if (
  status === 401 &&
  originalRequest &&
  !originalRequest._retry &&
  !isAuthExcludedUrl(originalRequest.url)
) {
  originalRequest._retry = true;

  const newAccessToken = await refreshAccessToken();
  originalRequest.headers.Authorization = `Bearer ${newAccessToken}`;

  return authApi(originalRequest);
}
```

주의:

- refresh API는 별도 axios instance를 사용할 수 있음
- login API는 publicApi 사용 권장
- refresh 실패 시 clearAuth
- URL path matching 기준 통일
- baseURL 포함 여부에 따라 URL 비교 방식 확인
- OAuth2 callback은 별도 흐름으로 처리
- refresh endpoint 자체에는 refresh retry 금지

---

### [FAQ]

Q. refresh API도 401이면 다시 refresh를 시도해?
A. 아니다. refresh API 실패는 인증 복원 실패로 보고 clearAuth 또는 login redirect 처리해야 한다.

Q. Login API 401도 refresh를 시도해야 해?
A. 아니다. Login API 401은 로그인 실패로 처리해야 하며 token 만료 401과 구분해야 한다.

Q. refresh API는 publicApi로 호출해도 돼?
A. 가능하다. refresh API에 access token header가 필요 없다면 publicApi 또는 별도 refreshApi를 사용할 수 있다.

Q. OAuth2 callback도 refresh retry 대상이야?
A. 아니다. OAuth2 callback은 별도 인증 결과 처리 흐름이며 global refresh retry 대상으로 두지 않는 것이 안전하다.

---

## 5.3 Auth Event Pattern for Redirect

### [개념]

Auth Event Pattern은 interceptor 같은 일반 모듈에서 직접 React Router hook을 사용할 수 없을 때 인증 만료 이벤트를 발생시키고 Router 계층에서 redirect를 처리하는 방식이다.

interceptor는 인증 상태 정리와 이벤트 발생만 담당하고, 실제 navigation은 React Component 영역에서 처리한다.

Auth Event Pattern은 refresh 실패, 인증 만료, cross tab auth expired 처리와 연결된다.

상세 troubleshooting은 401 / 403 Troubleshooting 문서에서 확인한다.

---

### [핵심]

필요 이유:

- interceptor module
- no React hook
- navigate unavailable
- auth expired event
- router layer handling
- clearAuth
- login redirect
- previous location
- cross tab auth expired optional

Flow:

```text
Interceptor detects refresh failure
→ clearAuth
→ emit AUTH_EXPIRED event
→ App listens event
→ navigate login
```

---

### [실무]

Event 유틸 예:

```tsx
const AUTH_EXPIRED_EVENT = "auth:expired";

export function emitAuthExpired() {
  window.dispatchEvent(new Event(AUTH_EXPIRED_EVENT));
}

export function listenAuthExpired(callback: () => void) {
  window.addEventListener(AUTH_EXPIRED_EVENT, callback);

  return () => {
    window.removeEventListener(AUTH_EXPIRED_EVENT, callback);
  };
}
```

interceptor에서 사용:

```tsx
catch (refreshError) {
  clearAuth();
  emitAuthExpired();

  return Promise.reject(refreshError);
}
```

App에서 처리:

```tsx
useEffect(() => {
  return listenAuthExpired(() => {
    navigate("/login", { replace: true });
  });
}, [navigate]);
```

주의:

- interceptor에서 useNavigate 직접 호출 금지
- event listener cleanup 필요
- 인증 만료와 단순 권한 없음 이벤트 구분
- 여러 번 이벤트 발생 시 중복 redirect 방지
- login page에서 다시 login으로 이동하지 않도록 조건 처리
- 상태관리 store subscription 방식으로 대체 가능
- cross tab auth expired는 Logout / Profile 문서의 cross tab sync와 연결 가능

---

### [FAQ]

Q. interceptor에서 navigate를 바로 쓸 수 없어?
A. React Router hook은 Component 내부에서만 사용할 수 있으므로 일반 interceptor 모듈에서는 직접 사용할 수 없다.

Q. refresh 실패 후 login redirect는 어디서 처리해?
A. interceptor는 auth expired event를 발생시키고 App 또는 Router 계층에서 navigate 처리하는 방식이 안정적이다.

Q. auth expired event가 여러 번 발생하면?
A. 현재 경로가 login인지 확인하거나 중복 redirect 방지 로직을 추가하는 것이 좋다.

Q. Auth Event Pattern은 어디와 연결돼?
A. refresh 실패, 401 인증 만료, Part09 Troubleshooting, cross tab auth expired 처리와 연결된다.

---

# 6. Axios Auth Error Normalization

## 6.1 API Error Normalization

### [개념]

API Error Normalization은 Backend Error Response를 Frontend에서 일관된 형태로 변환하는 기준이다.

이 문서에서는 Axios 인증 오류 정규화에 집중한다.

일반 Error Toast, Loading Skeleton, Empty State UX, 화면별 오류 표현은 Error Handling & Loading UX 문서에서 다룬다.

---

### [핵심]

정규화 대상:

- status
- message
- code
- fieldErrors
- originalError
- isUnauthorized
- isForbidden
- isNetworkError
- isValidationError

Backend 응답 후보:

```json
{
  "success": false,
  "message": "인증이 필요합니다.",
  "code": "UNAUTHORIZED",
  "errors": null
}
```

---

### [실무]

Normalized Error 타입 예:

```tsx
type ApiError = {
  status?: number;
  message: string;
  code?: string;
  fieldErrors?: Record<string, string>;
};
```

변환 함수 예:

```tsx
function normalizeApiError(error: unknown): ApiError {
  if (!isAxiosError(error)) {
    return {
      message: "알 수 없는 오류가 발생했습니다.",
    };
  }

  if (!error.response) {
    return {
      message: "네트워크 연결을 확인해 주세요.",
    };
  }

  return {
    status: error.response.status,
    message:
      error.response.data?.message ?? "요청 처리 중 오류가 발생했습니다.",
    code: error.response.data?.code,
    fieldErrors: error.response.data?.errors,
  };
}
```

주의:

- token이나 Authorization Header를 error object에서 노출하지 않음
- Backend error wrapper 구조 확인
- field error와 global error 구분
- 401 / 403은 status 기준으로 구분
- network error는 response가 없을 수 있음
- Component는 normalized error를 기준으로 메시지 표시
- 일반 UX 메시지 정책은 Error Handling & Loading UX 문서와 연결

---

### [FAQ]

Q. API 에러 메시지는 어디서 변환해?
A. 공통 normalizeApiError 함수나 API hook에서 변환하고 Component는 변환된 메시지를 표시하는 방식이 좋다.

Q. Network Error에는 status가 없어?
A. Axios에서 서버 응답을 받지 못한 경우 `error.response`가 없을 수 있다.

Q. 에러 객체를 그대로 화면에 보여줘도 돼?
A. 권장하지 않는다. 내부 정보나 민감정보가 노출될 수 있으므로 사용자용 메시지로 변환해야 한다.

Q. 일반 Toast나 Loading UX도 이 문서에서 다뤄?
A. 아니다. 이 문서에서는 Axios Auth Error Mapping까지만 다루고 일반 UX는 Error Handling & Loading UX 문서에서 다룬다.

---

## 6.2 Auth Error Mapping

### [개념]

Auth Error Mapping은 인증 관련 HTTP 상태와 Backend error code를 Frontend 인증 흐름에 맞는 처리로 매핑하는 기준이다.

401은 인증 문제, 403은 권한 문제, 400은 입력 검증 문제로 구분한다.

---

### [핵심]

Mapping 기준:

|      Status | 의미          | 인증 흐름 처리             |
| ----------: | ------------- | -------------------------- |
|         400 | 입력값 오류   | field error / global error |
|         401 | 인증 실패     | refresh or login redirect  |
|         403 | 권한 부족     | forbidden message / page   |
|         409 | 중복 / 충돌   | duplicate field message    |
|         500 | 서버 오류     | common error message       |
| no response | 네트워크 오류 | network error message      |

---

### [실무]

Auth Error Message 예:

```tsx
function getAuthErrorMessage(error: ApiError) {
  if (error.status === 400) {
    return "입력값을 확인해 주세요.";
  }

  if (error.status === 401) {
    return "로그인이 필요합니다.";
  }

  if (error.status === 403) {
    return "접근 권한이 없습니다.";
  }

  if (error.status === 409) {
    return "이미 사용 중인 정보입니다.";
  }

  return "요청 처리 중 오류가 발생했습니다.";
}
```

401 / 403 분리:

```text
401
→ refresh 시도
→ 실패 시 clearAuth
→ login redirect

403
→ Auth State 유지
→ forbidden message
→ forbidden page
```

주의:

- Login API 401 메시지와 인증 만료 401 메시지 구분
- 403에서 logout 처리 금지
- Validation Error는 field mapping 가능
- Backend code가 있으면 더 세밀한 처리 가능
- 사용자에게 내부 정책 과다 노출 금지
- Error Handling & Loading UX 문서와 연결
- Backend Error Response Contract와 일치해야 함

---

### [FAQ]

Q. 401과 403을 같은 메시지로 보여줘도 돼?
A. 권장하지 않는다. 401은 로그인 필요 또는 인증 실패이고 403은 권한 부족이다.

Q. 로그인 실패 401 메시지는 뭐가 좋아?
A. 보안상 “이메일 또는 비밀번호를 확인해 주세요”처럼 일반화된 메시지가 좋다.

Q. 403 메시지는 어떻게 보여줘?
A. “접근 권한이 없습니다” 같은 권한 부족 메시지나 forbidden page로 처리할 수 있다.

Q. 403에서 Auth State를 지워야 해?
A. 기본적으로 지우지 않는다. 403은 인증 실패가 아니라 권한 부족이다.

---

# 7. Axios Auth Troubleshooting

## 7.1 Authorization Header Missing

### [개념]

Authorization Header Missing은 인증 API 요청에 Access Token이 포함되지 않아 401이 발생하는 문제다.

대부분 authApi 미사용, interceptor 미등록, token getter 오류, token 저장 타이밍 문제로 발생한다.

---

### [핵심]

확인 대상:

- Network Request Headers
- Authorization Header
- Bearer prefix
- access token storage
- getAccessToken
- authApi usage
- publicApi misuse
- interceptor registration
- setup file import
- login response unwrap

---

### [실무]

Debug Flow:

```text
401 발생
→ Network 탭 확인
→ Request Headers 확인
→ Authorization Header 존재 확인
→ Bearer 형식 확인
→ authApi 사용 여부 확인
→ getAccessToken 반환값 확인
→ interceptor 등록 여부 확인
→ login response unwrap 확인
```

문제 예:

```text
문제: localStorage에 token은 있음
원인: 인증 API 함수가 publicApi 사용
해결: authApi로 변경
```

문제 예:

```text
문제: token 저장 직후 첫 요청만 401
원인: token 저장 전 요청 실행
해결: login result 적용 후 인증 API 호출
```

주의:

- token 존재와 Header 포함은 다른 문제
- Header에 `Bearer undefined`가 들어가지 않게 처리
- Header에 `Bearer Bearer token` 중복 주의
- interceptor 파일 import 누락 확인
- 인증 API endpoint가 실제로 Security 허용 경로인지 Backend도 확인
- token 값 자체를 console.log로 출력하지 않음

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

## 7.2 Interceptor Duplicate Registration

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

Debug Flow:

```text
API 요청 1회
→ interceptor log count 확인
→ interceptor 등록 위치 확인
→ Component 내부 등록 여부 확인
→ AuthProvider remount 여부 확인
→ setup function 호출 횟수 확인
→ eject 필요 여부 확인
```

eject 예:

```tsx
useEffect(() => {
  const interceptorId = authApi.interceptors.response.use(
    (response) => response,
    (error) => Promise.reject(error),
  );

  return () => {
    authApi.interceptors.response.eject(interceptorId);
  };
}, []);
```

권장:

```text
apiClient.ts module scope
→ axios instance 생성
→ interceptor 1회 등록
→ 재등록 없음
```

주의:

- Component 내부 등록은 가능하면 피함
- module scope 등록은 대부분 1회 실행
- test 환경에서는 setup 초기화 격리 필요
- Hot Reload 중 개발환경에서만 중복처럼 보일 수 있음
- production build에서도 재현되는지 확인
- refresh 중복 발생 시 concurrent 401 문제와 함께 확인

---

### [FAQ]

Q. interceptor가 여러 번 실행돼?
A. interceptor가 중복 등록되었을 가능성이 있다. 등록 위치를 module scope로 옮기거나 eject 처리를 확인해야 한다.

Q. Component에서 interceptor를 등록하면 왜 문제야?
A. Component가 렌더링되거나 remount될 때마다 interceptor가 추가될 수 있다.

Q. refresh 요청이 여러 번 나가?
A. interceptor 중복 등록 또는 concurrent 401 처리가 없어서 발생할 수 있다.

Q. 개발환경에서만 interceptor가 두 번 실행되는 것 같아?
A. StrictMode, Hot Reload, setup 중복 import 여부를 확인해야 한다.

---

## 7.3 Response Interceptor Swallow Error

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
  emitAuthExpired();

  return Promise.reject(refreshError);
}
```

주의:

- interceptor error handler는 항상 response 또는 Promise.reject 반환
- 에러를 처리해도 호출부에 전달할지 기준 필요
- 공통 auth cleanup과 화면별 message 처리는 분리
- Promise chain이 끊기면 loading이 끝나지 않을 수 있음
- async function에서는 `throw error`도 가능
- normalizeApiError 후에도 호출부 전달 여부를 명확히 함

---

### [FAQ]

Q. interceptor에서 Promise.reject를 왜 해?
A. 호출한 API 함수나 화면에서도 에러를 인식하고 적절한 UI를 보여줄 수 있게 하기 위해서다.

Q. Component catch가 실행되지 않아?
A. response interceptor에서 에러를 삼키고 Promise.reject를 반환하지 않았을 가능성이 있다.

Q. API 실패 후 loading이 계속 돌아?
A. 호출부 catch나 finally가 실행되지 않았을 수 있으며 interceptor 반환값을 확인해야 한다.

Q. refresh 실패 후 아무 반응이 없어?
A. refresh 실패 catch에서 clearAuth, auth expired event, Promise.reject 중 일부가 누락되었을 수 있다.

---

# 8. Part05 Review Checklist

## 8.1 Axios Auth Integration Checklist

### [개념]

Part05 검수는 publicApi / authApi 분리, Request Interceptor, Response Interceptor, Refresh Retry, Auth Event Pattern, Auth Error Normalization, Troubleshooting이 일관되게 연결되는지 확인한다.

---

### [핵심]

Checklist:

```md
- [ ] publicApi와 authApi 구분 기준이 포함되었는가?
- [ ] Login / Signup API는 publicApi 기준인가?
- [ ] 인증 필요 API는 authApi 기준인가?
- [ ] refresh API가 global retry 대상에서 제외되는가?
- [ ] baseURL 환경변수 기준이 포함되었는가?
- [ ] Frontend .env secret 금지가 포함되었는가?
- [ ] API Function Layer 기준이 포함되었는가?
- [ ] response.data.data unwrap 위치가 포함되었는가?
- [ ] Request Interceptor 기준이 포함되었는가?
- [ ] Authorization Header attach 기준이 포함되었는가?
- [ ] Bearer Token 기준이 포함되었는가?
- [ ] Bearer undefined / Bearer 중복 방지가 포함되었는가?
- [ ] Interceptor Registration 기준이 포함되었는가?
- [ ] withCredentials / Cookie Auth 기준이 포함되었는가?
- [ ] Response Interceptor 기준이 포함되었는가?
- [ ] 401 Handling 기준이 포함되었는가?
- [ ] 403 Handling 기준이 포함되었는가?
- [ ] Retry Original Request 기준이 포함되었는가?
- [ ] refresh / login endpoint 제외 기준이 포함되었는가?
- [ ] Auth Event Pattern 기준이 포함되었는가?
- [ ] Error Normalization 범위가 Axios Auth Error로 제한되었는가?
- [ ] Auth Error Mapping 기준이 포함되었는가?
- [ ] 일반 Error UX는 별도 문서 범위임을 명시했는가?
- [ ] Authorization Header Missing Troubleshooting이 포함되었는가?
- [ ] Interceptor Duplicate Registration Troubleshooting이 포함되었는가?
- [ ] Response Interceptor Swallow Error Troubleshooting이 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

Part05 이후 권장 문서 순서:

```text
Part05 Axios Auth Integration
→ Part06 Protected Route / Role Based Route
→ Part07 Logout / User Profile Fetch
→ Part08 OAuth2 Frontend Flow
→ Part09 401 / 403 / Troubleshooting
→ Part10 Security / Checklist / Retrieval Optimization
```

검수 기준:

```text
Axios Instance
→ publicApi / authApi
→ Request Interceptor
→ Response Interceptor
→ Refresh Retry
→ Auth Event
→ Error Mapping
→ Troubleshooting
```

---

### [FAQ]

Q. Part05의 핵심은 뭐야?
A. publicApi와 authApi 분리, Authorization Header 자동 추가, 401 / 403 공통 처리, refresh retry, auth event, error normalization 기준을 정리하는 것이다.

Q. Part05에서 Token Storage를 깊게 다뤄?
A. 아니다. Token Storage와 Token Lifecycle은 Part04에서 다루고 Part05는 Axios Interceptor 흐름에 집중한다.

Q. Part05에서 일반 Loading UX를 깊게 다뤄?
A. 아니다. 일반 Error Toast, Loading Skeleton, Empty State UX는 Error Handling & Loading UX 문서에서 다룬다.

Q. Part05에서 Protected Route를 다뤄?
A. 아니다. 인증 요청과 API Client 흐름을 다루고 Route Guard 상세 구현은 Part06에서 다룬다.

Q. Part05에서 OAuth2 Callback을 깊게 다뤄?
A. 아니다. OAuth2 Callback은 별도 문서에서 다루고 여기서는 API Client와 인증 오류 처리 중심으로 다룬다.

---

# Retrieval Queries

### [FAQ]

Q. publicApi와 authApi를 나누는 이유는?
A. 인증이 필요 없는 요청과 Authorization Header가 필요한 요청을 명확히 구분하기 위해서다.

Q. 인증 API에 publicApi를 쓰면 어떻게 돼?
A. Authorization Header가 누락되어 401이 발생할 수 있다.

Q. Login API도 authApi로 호출해야 해?
A. 보통 로그인 전에는 token이 없으므로 Login API는 publicApi로 호출한다.

Q. Refresh API는 publicApi야 authApi야?
A. access token header가 필요 없다면 publicApi 또는 별도 refreshApi를 사용할 수 있다. 프로젝트 Backend 정책에 맞춘다.

Q. 공개 API에 token을 보내도 돼?
A. 가능은 하지만 불필요한 token 노출을 줄이기 위해 공개 API에는 publicApi를 사용하는 것이 좋다.

Q. Frontend .env에 API 서버 주소를 넣어도 돼?
A. 가능하다. API base URL처럼 공개되어도 되는 값은 넣을 수 있다.

Q. Frontend .env에 OAuth secret을 넣어도 돼?
A. 안 된다. Frontend 환경변수는 빌드 결과에 노출될 수 있으므로 secret을 넣으면 안 된다.

Q. Vite와 CRA의 환경변수 이름이 달라?
A. 다르다. Vite는 `VITE_` prefix와 `import.meta.env`를 사용하고 CRA는 `REACT_APP_` prefix와 `process.env`를 사용한다.

Q. Component에서 바로 axios.get을 호출해도 돼?
A. 가능은 하지만 endpoint, unwrap, error handling이 흩어지므로 API 함수 계층으로 분리하는 것이 유지보수에 좋다.

Q. response.data.data unwrap은 어디서 해?
A. API 함수에서 통일하는 것이 좋다. Component가 Backend wrapper 구조를 직접 알지 않도록 한다.

Q. authApi와 publicApi 선택은 어디서 해?
A. API 함수 계층에서 endpoint 성격에 맞게 선택하는 것이 좋다.

Q. Authorization Header를 매 API 함수마다 넣어야 해?
A. 가능하지만 authApi request interceptor에서 공통 처리하는 것이 유지보수에 좋다.

Q. token이 없을 때 Authorization Header를 빈 값으로 넣어도 돼?
A. 권장하지 않는다. token이 없으면 Header 자체를 생략하는 것이 좋다.

Q. Request Interceptor에서 token을 console.log로 확인해도 돼?
A. 안 된다. token은 민감정보이므로 로그에 남기지 않는다.

Q. Header에 Bearer undefined가 들어가?
A. token getter가 undefined를 반환했는데 Header를 무조건 추가했을 가능성이 있다.

Q. interceptor가 여러 번 실행돼?
A. 설정 코드가 여러 번 실행되어 interceptor가 중복 등록되면 같은 로직이 반복될 수 있다. 초기화 위치를 통일해야 한다.

Q. interceptor는 Component 안에서 등록해도 돼?
A. 권장하지 않는다. Component가 렌더링될 때마다 중복 등록될 수 있다.

Q. interceptor 설정 파일을 import하지 않으면?
A. 설정 코드가 실행되지 않아 Authorization Header가 붙지 않을 수 있다.

Q. withCredentials는 언제 써?
A. cross-origin 요청에서 cookie를 포함해야 할 때 필요할 수 있으며 Backend CORS 설정과 함께 맞춰야 한다.

Q. Authorization Header 방식과 Cookie Auth 방식을 같이 써도 돼?
A. 가능은 하지만 인증 기준이 혼란스러워질 수 있으므로 프로젝트 기준을 명확히 해야 한다.

Q. CSRF Token Header는 Frontend에서 넣어야 해?
A. Backend가 CSRF Token 방식을 요구한다면 Frontend에서 해당 Header를 포함해야 한다.

Q. Response Interceptor에서 401을 처리하면 Component에서는 에러 처리를 안 해도 돼?
A. 아니다. 공통 인증 처리는 interceptor에서 하고, 화면별 사용자 메시지는 Component나 hook에서 처리할 수 있다.

Q. interceptor에서 Promise.reject를 왜 해?
A. 호출한 API 함수나 화면에서도 에러를 인식하고 적절한 UI를 보여줄 수 있게 하기 위해서다.

Q. response.data.data unwrap을 interceptor에서 해도 돼?
A. 가능은 하지만 TypeScript 타입 추론과 예외 처리가 복잡해질 수 있어 API 함수에서 통일하는 방식이 안정적이다.

Q. 401이 나오면 무조건 로그아웃해야 해?
A. refresh token flow가 있으면 먼저 재발급을 시도할 수 있다. 재발급 실패 시 로그아웃 처리한다.

Q. Login API 실패 401도 interceptor에서 refresh해야 해?
A. 아니다. Login API 실패 401은 로그인 실패로 처리하고 token 만료 401과 구분해야 한다.

Q. refresh endpoint가 401이면 어떻게 해?
A. refresh 실패로 보고 clearAuth 후 login redirect 처리하는 것이 일반적이다.

Q. interceptor에서 navigate를 바로 써도 돼?
A. React Router hook은 일반 모듈에서 직접 사용할 수 없다. auth event, callback, history router 구조 등을 별도로 설계해야 한다.

Q. 403이면 로그아웃해야 해?
A. 대부분 아니다. 인증은 되었지만 권한이 없는 상태이므로 권한 없음 화면이나 메시지를 보여주는 것이 일반적이다.

Q. 403과 401을 같은 방식으로 처리해도 돼?
A. 권장하지 않는다. 401은 인증 문제, 403은 권한 문제다.

Q. 403에서 login 페이지로 보내도 돼?
A. 권장하지 않는다. 이미 로그인된 사용자라면 forbidden page나 권한 없음 메시지가 더 적절하다.

Q. original request retry는 왜 필요해?
A. access token 만료로 실패한 요청을 새 token으로 다시 보내 사용자 작업을 이어가기 위해 필요하다.

Q. 원래 요청 retry는 여러 번 해도 돼?
A. 권장하지 않는다. `_retry` 플래그로 1회만 재시도해야 refresh loop를 막을 수 있다.

Q. POST 요청도 자동 retry해도 돼?
A. 가능하지만 결제, 주문, 중복 생성 같은 요청은 idempotency와 중복 실행 위험을 검토해야 한다.

Q. refresh API도 401이면 다시 refresh를 시도해?
A. 아니다. refresh API 실패는 인증 복원 실패로 보고 clearAuth 또는 login redirect 처리해야 한다.

Q. refresh API는 publicApi로 호출해도 돼?
A. 가능하다. refresh API에 access token header가 필요 없다면 publicApi 또는 별도 refreshApi를 사용할 수 있다.

Q. OAuth2 callback도 refresh retry 대상이야?
A. 아니다. OAuth2 callback은 별도 인증 결과 처리 흐름이며 global refresh retry 대상으로 두지 않는 것이 안전하다.

Q. interceptor에서 navigate를 바로 쓸 수 없어?
A. React Router hook은 Component 내부에서만 사용할 수 있으므로 일반 interceptor 모듈에서는 직접 사용할 수 없다.

Q. refresh 실패 후 login redirect는 어디서 처리해?
A. interceptor는 auth expired event를 발생시키고 App 또는 Router 계층에서 navigate 처리하는 방식이 안정적이다.

Q. Auth Event Pattern은 어디와 연결돼?
A. refresh 실패, 401 인증 만료, Part09 Troubleshooting, cross tab auth expired 처리와 연결된다.

Q. API 에러 메시지는 어디서 변환해?
A. 공통 normalizeApiError 함수나 API hook에서 변환하고 Component는 변환된 메시지를 표시하는 방식이 좋다.

Q. Network Error에는 status가 없어?
A. Axios에서 서버 응답을 받지 못한 경우 `error.response`가 없을 수 있다.

Q. 에러 객체를 그대로 화면에 보여줘도 돼?
A. 권장하지 않는다. 내부 정보나 민감정보가 노출될 수 있으므로 사용자용 메시지로 변환해야 한다.

Q. 일반 Toast나 Loading UX도 이 문서에서 다뤄?
A. 아니다. 이 문서에서는 Axios Auth Error Mapping까지만 다루고 일반 UX는 Error Handling & Loading UX 문서에서 다룬다.

Q. 401과 403을 같은 메시지로 보여줘도 돼?
A. 권장하지 않는다. 401은 로그인 필요 또는 인증 실패이고 403은 권한 부족이다.

Q. 로그인 실패 401 메시지는 뭐가 좋아?
A. 보안상 “이메일 또는 비밀번호를 확인해 주세요”처럼 일반화된 메시지가 좋다.

Q. 403 메시지는 어떻게 보여줘?
A. “접근 권한이 없습니다” 같은 권한 부족 메시지나 forbidden page로 처리할 수 있다.

Q. 403에서 Auth State를 지워야 해?
A. 기본적으로 지우지 않는다. 403은 인증 실패가 아니라 권한 부족이다.

Q. localStorage에 token이 있는데 401이 나?
A. Network 탭에서 Authorization Header에 실제로 token이 포함되었는지 확인해야 한다.

Q. 인증 API에 publicApi를 쓰면 어떻게 돼?
A. Authorization Header가 누락되어 401이 발생할 수 있다.

Q. 로그인 직후 API만 401이 나?
A. token 저장 또는 Auth State 갱신이 완료되기 전에 인증 API 요청이 먼저 실행되었을 수 있다.

Q. Component catch가 실행되지 않아?
A. response interceptor에서 에러를 삼키고 Promise.reject를 반환하지 않았을 가능성이 있다.

Q. API 실패 후 loading이 계속 돌아?
A. 호출부 catch나 finally가 실행되지 않았을 수 있으며 interceptor 반환값을 확인해야 한다.

Q. refresh 실패 후 아무 반응이 없어?
A. refresh 실패 catch에서 clearAuth, auth expired event, Promise.reject 중 일부가 누락되었을 수 있다.

Q. Part05 다음 문서는 뭐야?
A. Protected Route / Role Based Route 문서가 이어지는 것이 좋다.
