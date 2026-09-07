# Authentication Frontend Flow Part08 - OAuth2 Frontend Flow / Social Login / Callback Handling

---

# 1. OAuth2 Frontend Flow Overview

## 1.1 OAuth2 Frontend Responsibility

### [개념]

OAuth2 Frontend Flow는 사용자가 소셜 로그인 버튼을 클릭하고 OAuth2 Provider 인증을 거친 뒤 Frontend Callback Page에서 인증 결과를 처리하는 흐름이다.

Frontend는 OAuth2 Provider Secret을 가지지 않는다.

Frontend는 OAuth2 인증 시작, callback 결과 처리, token / code / cookie 기반 인증 복원, Auth State 갱신, redirect를 담당한다.

OAuth2 인증 처리의 핵심 검증과 Provider 연동은 Backend가 담당한다.

---

### [핵심]

핵심 키워드:

- OAuth2 Frontend Flow
- Social Login
- OAuth2 Redirect
- OAuth2 Callback
- Authorization Endpoint
- Backend OAuth2 Endpoint
- Provider Login
- Kakao Login
- Google Login
- Naver Login
- Access Token
- Refresh Token
- Authorization Code
- One-Time Login Code
- State Parameter
- Callback Page
- Auth State Update
- Me API
- Redirect After OAuth2
- Safe Redirect
- Token URL Cleanup
- OAuth2 Error Handling
- OAuth Secret Protection

Frontend 책임:

- Social Login Button 제공
- Backend OAuth2 Authorization Endpoint로 redirect
- OAuth2 Callback Page 처리
- token / code / cookie 결과 처리
- Auth State 갱신
- `/me` API 호출
- OAuth2 실패 메시지 처리
- callback URL token cleanup
- login 이후 redirect 처리
- safe returnUrl 검증

Frontend 책임 아님:

- Provider Client Secret 보관
- Provider Token Exchange 직접 수행
- OAuth2 Access Token 검증
- Backend JWT 생성
- Refresh Token Rotation
- Provider Secret 관리
- Backend OAuth2 Callback 상세 설정

---

### [실무]

기본 OAuth2 Flow:

```text
Click Social Login
→ Redirect Backend OAuth2 Authorization Endpoint
→ Backend redirects Provider Login Page
→ User Provider Login
→ Provider redirects Backend Callback
→ Backend OAuth2 Success
→ Backend redirects Frontend Callback
→ Frontend receives result
→ Store Token or Exchange Code or Restore Cookie Auth
→ Fetch /me if needed
→ Update Auth State
→ Clean URL
→ Navigate Main or Previous Page
```

권장 기준:

- OAuth2 시작 URL은 Backend 기준
- Frontend에 OAuth Client Secret 저장 금지
- Frontend는 Provider Secret을 알 필요 없음
- callback parameter 이름 Backend와 통일
- token을 URL로 받을 경우 즉시 제거
- code 방식이면 Backend에 code exchange 요청
- cookie 방식이면 `/me` API로 인증 상태 복원
- OAuth2 실패 callback 처리 필요
- OAuth2 로그인 후 `/me` API로 user summary 복원 권장
- redirect target 검증 필요
- Provider Redirect URI / Backend OAuth2 Callback 상세 설정은 Backend Security / OAuth2 문서에서 최종 확인

주의:

```text
Frontend에 Kakao Client Secret 저장
→ 빌드 결과에 노출
→ 보안 위험
→ Backend에서 관리해야 함
```

```text
OAuth2 callback route를 PublicOnlyRoute로 감쌈
→ callback 처리 전 redirect 가능
→ OAuth2 login loop 발생 가능
```

---

### [FAQ]

Q. OAuth2 Frontend Flow는 뭐야?
A. 사용자가 소셜 로그인 버튼을 누른 뒤 Backend OAuth2 Endpoint로 이동하고, 로그인 결과를 Frontend Callback Page에서 처리하는 흐름이다.

Q. 소셜 로그인 버튼은 Frontend에서 뭘 해?
A. 대부분 Backend OAuth2 authorization endpoint로 redirect한다.

Q. Kakao client secret을 Frontend에 넣어도 돼?
A. 안 된다. Frontend에 secret을 넣으면 노출된다. secret은 Backend에서 관리해야 한다.

Q. OAuth2 전체 인증 검증은 Frontend가 해?
A. 아니다. Provider 연동, token exchange, 사용자 검증, JWT 발급은 Backend가 담당한다.

Q. Provider Redirect URI 상세 설정은 이 문서에서 다뤄?
A. 아니다. Frontend 흐름에서는 개념만 다루고 상세 설정은 Backend Security / OAuth2 문서에서 확인한다.

---

## 1.2 OAuth2 Flow Variants

### [개념]

OAuth2 Frontend Flow는 Backend 설계에 따라 token 전달 방식, authorization code 처리 방식, cookie 처리 방식, one-time login code 처리 방식으로 나뉜다.

Frontend Agent는 프로젝트 Backend OAuth2 정책을 먼저 확인해야 한다.

---

### [핵심]

대표 방식:

- Backend Redirect + Token Query
- Backend Redirect + Authorization Code
- Backend Redirect + HttpOnly Cookie
- Backend Redirect + One-Time Login Code
- Backend Redirect + Session Cookie
- Popup Social Login
- Account Linking Flow

비교:

| 방식                | Frontend 역할                | 주의                          |
| ------------------- | ---------------------------- | ----------------------------- |
| Token Query         | URL token 읽고 저장          | URL 노출 위험                 |
| Authorization Code  | Backend에 code exchange 요청 | code 만료 / state 확인        |
| HttpOnly Cookie     | `/me` 호출로 복원            | withCredentials / CSRF        |
| One-Time Login Code | code를 Backend에 교환        | 재사용 방지                   |
| Popup Login         | 부모 창에 결과 전달          | popup 차단 / postMessage 보안 |

---

### [실무]

방식 선택 기준:

```text
보안 단순화 우선
→ Backend가 HttpOnly Cookie 설정
→ Frontend는 /me 호출

SPA 구현 편의 우선
→ Backend가 Frontend callback에 accessToken 전달
→ Frontend는 즉시 저장 후 URL cleanup

노출 최소화 우선
→ one-time login code 전달
→ Frontend가 Backend에 code exchange 요청
```

주의:

- token query 방식은 구현이 쉽지만 URL 노출 위험이 있음
- HttpOnly Cookie 방식은 Frontend token 접근 불가
- code 방식은 exchange API와 만료 정책 필요
- popup 방식은 postMessage origin 검증 필요
- 프로젝트 보안 요구사항에 따라 결정
- Backend Security 문서와 정책 일치 필요
- OAuth2 방식은 Frontend가 단독으로 결정하지 않음

---

### [FAQ]

Q. OAuth2 callback에서 token을 URL로 받아도 돼?
A. 가능은 하지만 URL 노출 위험이 있으므로 즉시 처리 후 replace navigation으로 제거해야 한다.

Q. HttpOnly Cookie 방식이면 Frontend는 뭘 해?
A. callback 후 `/me` API를 호출해 인증 상태와 user summary를 복원한다.

Q. one-time login code 방식은 왜 써?
A. access token을 URL에 직접 노출하지 않고 짧은 수명의 code를 Backend에 교환하기 위해 사용한다.

Q. OAuth2 방식은 Frontend가 정해도 돼?
A. 아니다. Backend OAuth2 설계와 보안 정책에 맞춰 Frontend 처리 방식을 맞춘다.

---

# 2. Social Login Button

## 2.1 Backend OAuth2 Authorization Redirect

### [개념]

Social Login Button은 사용자를 Backend OAuth2 Authorization Endpoint로 이동시키는 UI다.

Frontend가 Provider Authorization URL을 직접 조립하기보다 Backend가 제공하는 OAuth2 시작 URL로 redirect하는 방식이 일반적이다.

---

### [핵심]

필수 요소:

- Social Login Button
- Backend OAuth2 Endpoint
- provider name
- redirect
- window.location.href
- API_BASE_URL
- returnUrl optional
- state parameter
- loading state

예시 Endpoint:

```text
/oauth2/authorization/kakao
/oauth2/authorization/google
/oauth2/authorization/naver
```

---

### [실무]

Kakao Login Button 예:

```tsx
function KakaoLoginButton() {
  function handleClick() {
    window.location.href = `${API_BASE_URL}/oauth2/authorization/kakao`;
  }

  return (
    <button type="button" onClick={handleClick}>
      카카오 로그인
    </button>
  );
}
```

Provider 선택 예:

```tsx
type OAuthProvider = "kakao" | "google" | "naver";

function redirectToOAuth(provider: OAuthProvider) {
  window.location.href = `${API_BASE_URL}/oauth2/authorization/${provider}`;
}
```

returnUrl 전달 예:

```tsx
function redirectToOAuth(provider: OAuthProvider, returnUrl: string) {
  const searchParams = new URLSearchParams({
    returnUrl,
  });

  window.location.href = `${API_BASE_URL}/oauth2/authorization/${provider}?${searchParams}`;
}
```

주의:

- OAuth2 시작 URL은 Backend 기준
- Frontend가 Provider Client Secret을 가지면 안 됨
- returnUrl 전달 방식은 Backend OAuth2 설계에 따라 달라짐
- Frontend가 query로 전달할 수도 있고 Backend가 state/session에 저장할 수도 있음
- returnUrl은 Backend 또는 Frontend에서 안전성 검증 필요
- 버튼 클릭 중 중복 클릭 방지 가능
- Provider 이름은 Backend route와 통일
- 로그인 실패 시 돌아올 callback route 확인
- popup 방식이 아니면 현재 페이지를 벗어남

---

### [FAQ]

Q. 소셜 로그인 버튼에서 axios 요청을 보내?
A. 보통 axios 요청이 아니라 `window.location.href`로 Backend OAuth2 시작 URL로 이동한다.

Q. Provider OAuth URL을 Frontend에서 직접 만들면 안 돼?
A. 가능은 하지만 secret, redirect URI, state 검증이 복잡해지므로 Backend OAuth2 Endpoint로 이동하는 방식이 일반적이다.

Q. 카카오 로그인 시작 URL은 어디 기준이야?
A. Provider 직접 URL이 아니라 Backend가 제공하는 `/oauth2/authorization/kakao` 같은 시작 URL을 기준으로 하는 경우가 많다.

Q. returnUrl은 반드시 Frontend가 query로 붙여야 해?
A. 아니다. Backend가 state 또는 session에 저장할 수도 있다. 프로젝트 Backend OAuth2 설계에 맞춘다.

---

## 2.2 Social Login Button UX

### [개념]

Social Login Button UX는 사용자가 소셜 로그인 버튼을 클릭했을 때 중복 클릭, loading 표시, provider 구분, 실패 안내를 처리하는 기준이다.

소셜 로그인은 외부 페이지 이동이 발생하므로 일반 Login API submit과 UX가 다를 수 있다.

---

### [핵심]

UX 기준:

- provider button
- loading state
- disabled state
- duplicate click prevention
- provider icon
- accessibility label
- error message
- terms notice
- privacy notice
- account linking notice

---

### [실무]

Button 예:

```tsx
function SocialLoginButton({
  provider,
  label,
}: {
  provider: "kakao" | "google" | "naver";
  label: string;
}) {
  const [redirecting, setRedirecting] = useState(false);

  function handleClick() {
    if (redirecting) {
      return;
    }

    setRedirecting(true);
    window.location.href = `${API_BASE_URL}/oauth2/authorization/${provider}`;
  }

  return (
    <button type="button" onClick={handleClick} disabled={redirecting}>
      {redirecting ? "이동 중..." : label}
    </button>
  );
}
```

주의:

- 클릭 후 외부 redirect가 발생하므로 loading은 짧게 표시
- provider별 브랜드 가이드 확인 가능
- 접근성 label 제공
- 중복 클릭 방지
- 소셜 로그인 실패 메시지는 callback page 또는 login page에서 처리 가능
- returnUrl 저장 정책 확인
- 약관 동의가 필요한 서비스는 별도 흐름 필요 가능

---

### [FAQ]

Q. 소셜 로그인 버튼에도 loading이 필요해?
A. 필수는 아니지만 중복 클릭 방지와 사용자 피드백을 위해 짧은 loading 상태를 둘 수 있다.

Q. 소셜 로그인 실패 메시지는 어디서 보여줘?
A. Backend가 실패 후 Frontend callback 또는 login page로 redirect하면 해당 페이지에서 메시지를 보여준다.

Q. 소셜 로그인 버튼에 provider icon을 넣어야 해?
A. 필수는 아니지만 사용자 인식과 UX를 위해 provider별 버튼 스타일을 맞추는 경우가 많다.

---

# 3. OAuth2 Callback Handling

## 3.1 OAuth2 Callback Page Purpose

### [개념]

OAuth2 Callback Page는 Backend OAuth2 성공 또는 실패 후 Frontend가 전달받은 결과를 처리하는 전용 페이지다.

Callback Page는 token, code, error, redirect target을 읽고 인증 상태를 갱신한 뒤 최종 목적지로 이동한다.

Callback Page는 일반 login page나 protected page와 다르게 auth guard 예외로 두는 것이 안전하다.

---

### [핵심]

처리 대상:

- access token
- refresh token
- authorization code
- one-time login code
- cookie auth result
- error
- error description
- provider
- redirect target
- query string
- hash fragment
- user info fetch
- token cleanup from URL

기본 Flow:

```text
Callback Page Mount
→ Read Query Params
→ Validate Result
→ Store Token or Exchange Code or Restore Cookie Auth
→ Fetch /me if Needed
→ Update Auth State
→ Clean URL
→ Redirect Main or Previous Page
```

---

### [실무]

Callback Route 예:

```tsx
<Route path="/oauth/callback" element={<OAuthCallbackPage />} />
```

Callback Page 기본 예:

```tsx
function OAuthCallbackPage() {
  const [searchParams] = useSearchParams();
  const navigate = useNavigate();

  useEffect(() => {
    async function handleCallback() {
      const accessToken = searchParams.get("accessToken");
      const error = searchParams.get("error");

      if (error) {
        navigate("/login", {
          replace: true,
          state: { message: "소셜 로그인에 실패했습니다." },
        });
        return;
      }

      if (!accessToken) {
        navigate("/login", {
          replace: true,
          state: { message: "로그인 결과를 확인할 수 없습니다." },
        });
        return;
      }

      setAccessToken(accessToken);

      const user = await getMe();
      setUser(user);
      setAuthenticated(true);

      navigate("/", { replace: true });
    }

    handleCallback();
  }, [searchParams, navigate]);

  return <p>로그인 처리 중...</p>;
}
```

주의:

- callback 처리 중 loading UI 제공
- error param 처리
- token 전달 방식 보안 검토
- token을 URL에 남겨두지 않음
- replace navigation 사용
- 중복 처리 방지
- Backend와 callback parameter 이름 통일
- Callback Page를 PublicOnlyRoute로 감싸지 않도록 주의
- Callback Page를 ProtectedRoute로 감싸지 않도록 주의
- callback 처리 완료 전 navigate 금지

---

### [FAQ]

Q. OAuth2 callback page는 왜 필요해?
A. 소셜 로그인 결과로 전달된 token, code, error를 처리하고 Auth State를 갱신한 뒤 최종 페이지로 이동시키기 위해 필요하다.

Q. OAuth2 callback에서 에러가 오면?
A. login 페이지로 이동하고 사용자에게 로그인 실패 메시지를 보여준다.

Q. OAuth2 callback도 PublicOnlyRoute로 감싸도 돼?
A. 주의해야 한다. callback 처리 전에 authenticated 상태가 바뀌거나 redirect가 발생하면 OAuth2 처리가 중단될 수 있다.

Q. OAuth2 callback을 ProtectedRoute로 감싸도 돼?
A. 권장하지 않는다. 로그인 결과를 처리해야 하는 route이므로 인증 전에도 접근 가능해야 한다.

---

## 3.2 Token Query Callback

### [개념]

Token Query Callback은 Backend가 OAuth2 성공 후 Frontend callback URL에 accessToken 또는 refreshToken을 query parameter로 전달하는 방식이다.

구현은 단순하지만 URL에 token이 노출될 수 있으므로 즉시 cleanup이 필요하다.

---

### [핵심]

Flow:

```text
Backend OAuth2 Success
→ Redirect /oauth/callback?accessToken=...
→ Frontend reads accessToken
→ Store Token
→ Clean URL
→ Fetch /me
→ Set Auth State
→ Navigate
```

필수 처리:

- accessToken read
- refreshToken read optional
- token validation presence
- set token
- getMe
- set authenticated
- replace navigation
- token URL cleanup

---

### [실무]

Token Query 처리 예:

```tsx
async function handleTokenQueryCallback(searchParams: URLSearchParams) {
  const accessToken = searchParams.get("accessToken");
  const refreshToken = searchParams.get("refreshToken");

  if (!accessToken) {
    throw new Error("Access token missing");
  }

  setAccessToken(accessToken);

  if (refreshToken) {
    setRefreshToken(refreshToken);
  }

  const user = await getMe();

  setUser(user);
  setAuthenticated(true);
}
```

URL cleanup 예:

```tsx
navigate("/", { replace: true });
```

또는:

```tsx
window.history.replaceState({}, document.title, "/");
```

주의:

- URL에 token이 남지 않도록 즉시 replace
- token query는 browser history, server log, screenshot에 노출될 수 있음
- refreshToken query 전달은 특히 위험
- token을 console.log로 출력하지 않음
- URL cleanup 전 error reporting 주의
- 가능한 경우 one-time code 또는 cookie 방식 검토
- HTTPS 사용 필수

---

### [FAQ]

Q. OAuth2 callback에서 token을 URL로 받으면 어떻게 해?
A. 즉시 저장 또는 처리한 뒤 replace navigation으로 URL에서 token을 제거하는 것이 좋다. 보안상 token 전달 방식도 Backend와 검토해야 한다.

Q. refreshToken도 URL로 받아도 돼?
A. 권장하지 않는다. refreshToken은 더 민감하므로 HttpOnly Cookie나 one-time code 방식을 우선 검토하는 것이 좋다.

Q. URL에서 token을 제거하지 않으면?
A. 브라우저 history, screenshot, log, 공유 URL에 token이 노출될 수 있다.

Q. token query 방식은 무조건 금지야?
A. 무조건 금지는 아니지만 위험을 이해하고 즉시 cleanup하며 가능하면 one-time code나 HttpOnly Cookie를 검토하는 것이 좋다.

---

## 3.3 Authorization Code Callback

### [개념]

Authorization Code Callback은 Frontend가 callback URL에서 code를 받은 뒤 Backend에 code exchange 요청을 보내 인증 결과를 받는 방식이다.

Frontend가 Provider와 직접 token exchange를 하지 않고 Backend에 code를 전달하는 구조가 일반적이다.

---

### [핵심]

Flow:

```text
Backend or Provider redirects Frontend Callback
→ Frontend reads code
→ Frontend sends code to Backend
→ Backend exchanges code
→ Backend returns app token or sets cookie
→ Frontend fetches /me
→ Auth State update
```

필수 요소:

- code
- state
- provider
- exchange API
- code expiration
- one-time use
- error handling
- redirect target

---

### [실무]

Code Exchange API 예:

```tsx
export async function exchangeOAuthCode(requestBody: OAuthCodeExchangeRequest) {
  const response = await publicApi.post<ApiResponse<LoginResponse>>(
    "/auth/oauth2/exchange",
    requestBody,
  );

  return response.data.data;
}
```

Callback 처리 예:

```tsx
async function handleCodeCallback(searchParams: URLSearchParams) {
  const code = searchParams.get("code");
  const state = searchParams.get("state");
  const provider = searchParams.get("provider");

  if (!code || !provider) {
    throw new Error("OAuth callback parameter missing");
  }

  const result = await exchangeOAuthCode({
    code,
    state,
    provider,
  });

  setAccessToken(result.accessToken);

  if (result.refreshToken) {
    setRefreshToken(result.refreshToken);
  }

  const user = result.user ?? (await getMe());

  setUser(user);
  setAuthenticated(true);
}
```

주의:

- code는 짧은 수명과 1회 사용이 일반적
- state 검증은 Backend 또는 Frontend 정책 확인
- code exchange API는 publicApi 사용 가능
- Provider Client Secret은 Backend에서 사용
- code exchange 실패 시 login으로 이동
- callback URL cleanup 필요
- replay 방지 정책 필요
- code 방식도 URL에 code가 남지 않도록 cleanup 권장

---

### [FAQ]

Q. OAuth2 code를 Frontend가 직접 Provider에 교환해?
A. 일반적으로 아니다. Provider secret이 필요할 수 있으므로 Backend에 code를 전달하고 Backend가 교환한다.

Q. code 방식은 token query 방식보다 안전해?
A. access token을 URL에 직접 노출하지 않는 장점이 있다. 단 code 만료와 1회 사용 정책이 필요하다.

Q. code exchange API는 authApi로 호출해?
A. 로그인 전 상태이므로 보통 publicApi로 호출한다.

Q. code도 URL에서 제거해야 해?
A. token보다 위험도는 낮을 수 있지만 재사용 방지와 노출 최소화를 위해 callback 처리 후 URL cleanup을 권장한다.

---

## 3.4 HttpOnly Cookie Callback

### [개념]

HttpOnly Cookie Callback은 Backend가 OAuth2 성공 후 HttpOnly Cookie를 설정하고 Frontend callback으로 redirect하는 방식이다.

Frontend는 token을 읽지 않고 `/me` API를 호출해 인증 상태를 복원한다.

---

### [핵심]

Flow:

```text
Backend OAuth2 Success
→ Set HttpOnly Cookie
→ Redirect Frontend Callback
→ Frontend calls /me with credentials
→ Backend validates cookie
→ Return user summary
→ Frontend set authenticated true
```

필수 요소:

- HttpOnly Cookie
- Set-Cookie
- withCredentials
- SameSite
- Secure
- CSRF
- Me API
- Auth Restore

---

### [실무]

Axios 설정:

```tsx
export const authApi = axios.create({
  baseURL: API_BASE_URL,
  withCredentials: true,
});
```

Callback 처리:

```tsx
async function handleCookieCallback() {
  const user = await getMe();

  setUser(user);
  setAuthenticated(true);

  navigate("/", { replace: true });
}
```

Callback Page 예:

```tsx
function OAuthCookieCallbackPage() {
  const navigate = useNavigate();

  useEffect(() => {
    async function handleCallback() {
      try {
        const user = await getMe();

        setUser(user);
        setAuthenticated(true);

        navigate("/", { replace: true });
      } catch {
        clearAuth();

        navigate("/login", {
          replace: true,
          state: { message: "소셜 로그인에 실패했습니다." },
        });
      }
    }

    handleCallback();
  }, [navigate]);

  return <p>로그인 처리 중...</p>;
}
```

주의:

- Frontend는 cookie 값을 읽지 않음
- `/me` API로 인증 상태 확인
- cross-origin이면 withCredentials 필요 가능
- Backend CORS credentials 설정 필요
- SameSite=None이면 Secure 필요
- CSRF 정책 확인
- callback 후 user summary 설정 필요

---

### [FAQ]

Q. HttpOnly Cookie 방식에서는 OAuth2 callback에서 token을 읽어?
A. 아니다. Frontend는 token을 읽지 않고 `/me` API로 인증 상태를 확인한다.

Q. Cookie 방식 OAuth2에서 Authorization Header가 필요해?
A. Backend가 Cookie Auth를 기준으로 하면 Authorization Header가 필요 없을 수 있다.

Q. Cookie 방식인데 /me가 401이 나?
A. cookie가 전송되지 않았거나 CORS credentials, SameSite, Secure, Backend cookie 설정 문제가 있을 수 있다.

Q. Cookie 방식에서는 Auth State를 어떻게 채워?
A. `/me` API 응답으로 user summary를 받고 authenticated true로 설정한다.

---

# 4. OAuth2 Redirect Handling

## 4.1 Redirect After OAuth2 Login

### [개념]

Redirect After OAuth2 Login은 소셜 로그인 성공 후 사용자를 어느 페이지로 이동시킬지 결정하는 흐름이다.

일반 로그인과 마찬가지로 보호 페이지 접근 후 소셜 로그인을 한 경우 원래 페이지로 돌려보낼 수 있다.

returnUrl 전달 방식은 Backend OAuth2 설계에 따라 달라진다.

Frontend가 query로 전달할 수도 있고 Backend가 state 또는 session에 저장할 수도 있다.

어떤 방식이든 Frontend callback에서는 safe redirect 검증을 수행한다.

---

### [핵심]

사용 상황:

- direct social login
- protected page access
- signup-required social login
- account linking
- email required
- profile setup required

Redirect 후보:

- previous protected path
- main page
- profile setup page
- terms agreement page
- account linking page
- login page on failure

전달 방식:

```text
Frontend Query 방식
→ /oauth2/authorization/kakao?returnUrl=/mypage
```

```text
Backend State / Session 방식
→ Backend stores returnUrl with OAuth2 state
→ Callback returns safe target or handles redirect
```

---

### [실무]

Frontend query 방식 예:

```tsx
function startOAuthLogin(provider: OAuthProvider) {
  const returnUrl = getSafeRedirectPath(location.state?.from ?? "/");

  const searchParams = new URLSearchParams({
    returnUrl,
  });

  window.location.href = `${API_BASE_URL}/oauth2/authorization/${provider}?${searchParams}`;
}
```

Callback에서 사용:

```tsx
const returnUrl = getSafeRedirectPath(searchParams.get("returnUrl"));

navigate(returnUrl, { replace: true });
```

Backend state/session 방식 예:

```text
OAuth2 Start
→ Backend stores returnUrl with state/session
→ Provider Login
→ Backend OAuth2 Success
→ Backend redirects Frontend Callback
→ Frontend receives returnUrl or default redirect
→ Frontend validates returnUrl
```

Safe Redirect 예:

```tsx
function getSafeRedirectPath(path: unknown) {
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

- returnUrl은 반드시 safe redirect 검증
- 외부 URL redirect 금지
- login / signup / callback으로 redirect loop 방지
- profile setup이 필요한 신규 소셜 계정은 별도 route 가능
- 약관 동의가 필요한 경우 바로 main 이동 금지
- OAuth2 실패 시 login page로 이동
- returnUrl 관리 주체는 Backend 설계에 맞춤

---

### [FAQ]

Q. 소셜 로그인 후 원래 보려던 페이지로 돌아가려면?
A. OAuth2 시작 시 returnUrl을 저장하고 callback에서 검증 후 해당 경로로 navigate한다.

Q. OAuth2 returnUrl도 검증해야 해?
A. 해야 한다. 외부 URL redirect와 callback loop를 막기 위해 내부 경로인지 확인해야 한다.

Q. returnUrl은 Frontend가 관리해 Backend가 관리해?
A. 프로젝트에 따라 다르다. Frontend query 방식, Backend state/session 방식 모두 가능하며 safe redirect 검증은 필요하다.

Q. 신규 소셜 가입자는 바로 main으로 보내도 돼?
A. 약관 동의, 추가 정보 입력, 이메일 확인이 필요하면 profile setup이나 terms page로 보내야 한다.

---

## 4.2 OAuth2 New User Flow

### [개념]

OAuth2 New User Flow는 소셜 로그인으로 처음 가입한 사용자가 추가 정보 입력, 약관 동의, 닉네임 설정, 프로필 설정을 완료하도록 처리하는 흐름이다.

OAuth2 Provider에서 받은 정보만으로 서비스 회원가입이 완성되지 않을 수 있다.

temporary token은 필수 구조가 아니다.

Backend 정책에 따라 정식 accessToken, 임시 token, one-time setup code, HttpOnly Cookie 중 하나를 사용할 수 있다.

---

### [핵심]

신규 사용자 처리 후보:

- needsSignup
- needsProfileSetup
- needsTermsAgreement
- needsNickname
- needsEmail
- provider email missing
- provider account linked
- temporary token optional
- one-time setup code optional
- onboarding route

Flow:

```text
OAuth2 Provider Login
→ Backend identifies new user
→ Redirect Frontend Callback
→ Frontend sees needsProfileSetup
→ Navigate Profile Setup
→ Submit additional info
→ Complete Signup
→ Refresh /me
→ Navigate Main or returnUrl
```

---

### [실무]

Callback Result 예:

```json
{
  "accessToken": "final-or-temporary-token",
  "user": {
    "userId": 1,
    "nickname": null,
    "role": "ROLE_USER"
  },
  "needsProfileSetup": true
}
```

처리 예:

```tsx
if (result.needsProfileSetup) {
  setAccessToken(result.accessToken);
  setUser(result.user);
  setAuthenticated(true);

  navigate("/profile/setup", { replace: true });
  return;
}
```

One-Time Setup Code 후보:

```text
OAuth2 Success
→ Backend redirects callback with setupCode
→ Frontend exchanges setupCode or submits profile setup
→ Backend completes signup
→ Frontend calls /me
```

Profile Setup Route 주의:

```text
Profile Setup
→ 로그인은 되었지만 onboarding incomplete
→ 일부 기능 접근 제한 가능
→ setup 완료 후 /me refetch
```

주의:

- 신규 사용자와 기존 사용자 흐름 구분
- provider email이 없을 수 있음
- nickname 중복 검증 필요
- 약관 동의가 별도 필요할 수 있음
- 임시 token / 정식 token / one-time code / cookie 중 무엇을 쓰는지 Backend 정책 확인
- setup 완료 전 접근 가능한 route 제한
- profile setup 완료 후 Auth State 갱신
- onboarding incomplete 상태는 Role Based Route와 별도 조건일 수 있음

---

### [FAQ]

Q. 소셜 로그인 신규 사용자는 바로 회원가입 완료야?
A. 서비스 정책에 따라 다르다. 약관 동의, 닉네임, 추가 정보 입력이 필요하면 onboarding flow가 필요하다.

Q. provider에서 email이 안 오면?
A. 추가 입력 화면에서 email을 받거나 email 없는 계정 정책을 Backend와 정해야 한다.

Q. temporary token은 OAuth2 신규 사용자 flow에서 필수야?
A. 아니다. Backend 정책에 따라 정식 token, 임시 token, one-time setup code, HttpOnly Cookie 중 하나를 사용할 수 있다.

Q. profile setup 완료 후 뭘 해야 해?
A. `/me`를 다시 조회하거나 Auth State user summary를 갱신한 뒤 main 또는 returnUrl로 이동한다.

---

# 5. OAuth2 Account Linking

## 5.1 Account Linking Flow

### [개념]

Account Linking은 기존 로그인 사용자가 Kakao, Google, Naver 같은 OAuth2 Provider 계정을 자신의 서비스 계정에 연결하는 흐름이다.

Account Linking은 일반 Social Login과 다르며 이미 로그인된 상태에서 수행될 수 있다.

Account Linking / Unlink는 기본 로그인 흐름의 필수 요소가 아니라 계정 설정 기능이 있는 서비스에서 선택적으로 적용한다.

---

### [핵심]

사용 상황:

- link provider account
- unlink provider account
- already linked provider
- provider conflict
- authenticated user required
- account settings
- reauthentication
- linking callback

Flow:

```text
Authenticated User
→ Click Link Provider
→ Redirect Backend OAuth2 Linking Endpoint
→ Provider Login
→ Backend Links Provider Account
→ Redirect Frontend Linking Callback
→ Show Success / Failure
→ Refresh Profile
```

---

### [실무]

Link 시작 예:

```tsx
function linkOAuthProvider(provider: OAuthProvider) {
  window.location.href = `${API_BASE_URL}/oauth2/link/${provider}`;
}
```

Callback 처리 예:

```tsx
function OAuthLinkCallbackPage() {
  const [searchParams] = useSearchParams();
  const navigate = useNavigate();

  useEffect(() => {
    const error = searchParams.get("error");

    if (error) {
      navigate("/settings/account", {
        replace: true,
        state: { message: "계정 연결에 실패했습니다." },
      });
      return;
    }

    navigate("/settings/account", {
      replace: true,
      state: { message: "계정 연결이 완료되었습니다." },
    });
  }, [searchParams, navigate]);

  return <p>계정 연결 처리 중...</p>;
}
```

주의:

- Account Linking은 로그인 상태 필요
- 일반 login callback과 route 분리 권장
- provider conflict 처리 필요
- 이미 연결된 provider 처리 필요
- unlink 시 재인증 필요 가능
- profile cache 갱신 필요
- Backend가 현재 사용자와 Provider 계정을 안전하게 연결해야 함
- Foundation 인증 흐름에서는 선택 항목

---

### [FAQ]

Q. 소셜 로그인과 계정 연결은 같은 거야?
A. 아니다. 소셜 로그인은 인증 방식이고 계정 연결은 기존 계정에 provider를 추가하는 흐름이다.

Q. 계정 연결은 비로그인 상태에서도 가능해?
A. 보통 기존 계정에 연결하는 작업이므로 로그인 상태가 필요하다.

Q. provider conflict는 뭐야?
A. 해당 provider 계정이 이미 다른 서비스 계정에 연결되어 있는 충돌 상황이다.

Q. Account Linking은 필수 구현이야?
A. 아니다. 기본 로그인 흐름의 필수 요소가 아니라 계정 설정 기능이 있는 서비스에서 선택적으로 적용한다.

---

## 5.2 Account Unlink Flow

### [개념]

Account Unlink Flow는 사용자가 연결된 OAuth2 Provider 계정을 서비스 계정에서 해제하는 흐름이다.

연결 해제는 계정 접근 수단을 줄이는 작업이므로 보안 정책과 재인증 기준이 필요하다.

Account Unlink는 기본 인증 흐름의 필수 요소가 아니라 계정 설정 기능에 속하는 선택 기능이다.

---

### [핵심]

처리 대상:

- unlink provider
- reauthentication
- last login method
- password exists
- provider count
- account lockout prevention
- profile cache refresh

주의 상황:

```text
마지막 로그인 수단 제거
→ 사용자가 더 이상 로그인할 수 없음
→ password 설정 또는 다른 provider 연결 필요
```

---

### [실무]

Unlink API 예:

```tsx
export async function unlinkOAuthProvider(provider: OAuthProvider) {
  const response = await authApi.delete<ApiResponse<void>>(
    `/users/me/oauth-providers/${provider}`,
  );

  return response.data.data;
}
```

처리 예:

```tsx
async function handleUnlink(provider: OAuthProvider) {
  await unlinkOAuthProvider(provider);

  await queryClient.invalidateQueries({ queryKey: ["myProfile"] });
  await queryClient.invalidateQueries({ queryKey: ["me"] });
}
```

주의:

- 마지막 로그인 수단 제거 방지
- 비밀번호 없는 계정은 provider unlink 제한 가능
- 재인증 요구 가능
- Backend 정책과 메시지 통일
- unlink 후 profile cache 갱신
- unlink 실패 403 / 409 처리
- OAuth2 Provider 연결 상태 UI 갱신
- Foundation 인증 흐름에서는 선택 항목

---

### [FAQ]

Q. 연결된 소셜 계정을 그냥 해제해도 돼?
A. 마지막 로그인 수단인지 확인해야 한다. 해제 후 로그인 불가능한 상태가 되지 않도록 Backend 정책이 필요하다.

Q. unlink에 재인증이 필요해?
A. 보안 요구가 높으면 비밀번호 확인이나 provider 재인증을 요구할 수 있다.

Q. unlink 후 UI가 그대로야?
A. profile cache나 provider list query를 invalidate하지 않았을 가능성이 있다.

Q. Account Unlink는 필수 구현이야?
A. 아니다. 계정 설정 기능이 있는 서비스에서 선택적으로 적용한다.

---

# 6. OAuth2 Error Handling

## 6.1 OAuth2 Callback Error

### [개념]

OAuth2 Callback Error는 소셜 로그인 중 Provider 인증 실패, 사용자 취소, Backend 검증 실패, 계정 충돌, callback parameter 누락 등으로 발생한다.

Frontend는 error parameter 또는 Backend error response를 사용자 메시지로 변환해야 한다.

---

### [핵심]

오류 원인:

- access_denied
- user_cancelled
- invalid_state
- invalid_code
- provider_error
- account_conflict
- email_required
- signup_required
- token_missing
- code_expired
- server_error

처리 기준:

- login page redirect
- error message
- account linking page redirect
- retry social login
- support message
- no internal detail exposure
- clear partial auth state

---

### [실무]

Error Mapping 예:

```tsx
function getOAuthErrorMessage(errorCode: string | null) {
  if (errorCode === "access_denied" || errorCode === "user_cancelled") {
    return "소셜 로그인이 취소되었습니다.";
  }

  if (errorCode === "account_conflict") {
    return "이미 다른 계정에 연결된 소셜 계정입니다.";
  }

  if (errorCode === "email_required") {
    return "이메일 정보가 필요합니다.";
  }

  return "소셜 로그인에 실패했습니다. 다시 시도해 주세요.";
}
```

Callback 실패 처리:

```tsx
const errorCode = searchParams.get("error");

if (errorCode) {
  clearAuth();

  navigate("/login", {
    replace: true,
    state: { message: getOAuthErrorMessage(errorCode) },
  });
  return;
}
```

주의:

- 내부 error stack 노출 금지
- Provider 원본 오류를 그대로 노출하지 않음
- 사용자 취소와 서버 오류 메시지 구분 가능
- 계정 충돌은 account linking 안내 필요 가능
- invalid_state는 보안상 중요하므로 Backend 로그 확인 필요
- callback 실패 후 Auth State를 authenticated true로 만들지 않음
- partial token 저장 상태가 있으면 clearAuth

---

### [FAQ]

Q. OAuth2 callback에서 에러가 오면?
A. login 페이지로 이동하고 사용자에게 로그인 실패 메시지를 보여준다.

Q. 사용자가 소셜 로그인을 취소하면 에러야?
A. 기술적으로 error callback이 올 수 있으며 사용자에게 “로그인이 취소되었습니다” 정도로 안내할 수 있다.

Q. account_conflict는 어떻게 처리해?
A. 이미 다른 계정에 연결된 provider일 수 있으므로 계정 연결 안내나 고객 지원 메시지를 제공할 수 있다.

Q. invalid_state는 단순 로그인 실패야?
A. 사용자에게는 실패로 안내하지만 보안상 중요한 이벤트일 수 있으므로 Backend 로그 확인이 필요하다.

---

## 6.2 OAuth2 Callback Missing Parameter

### [개념]

OAuth2 Callback Missing Parameter는 callback page에 필요한 accessToken, code, setupCode, error 정보가 누락된 상황이다.

Frontend는 누락된 parameter를 인증 실패로 처리하고 login page로 안전하게 이동시켜야 한다.

---

### [핵심]

누락 후보:

- accessToken missing
- code missing
- setupCode missing
- state missing
- provider missing
- returnUrl missing
- error missing
- callback mode unknown

처리 기준:

- fail closed
- clearAuth
- login redirect
- generic error message
- no partial auth state
- no authenticated true

---

### [실무]

처리 예:

```tsx
function assertOAuthCallbackParams(searchParams: URLSearchParams) {
  const accessToken = searchParams.get("accessToken");
  const code = searchParams.get("code");
  const setupCode = searchParams.get("setupCode");
  const error = searchParams.get("error");

  if (error) {
    return;
  }

  if (!accessToken && !code && !setupCode) {
    throw new Error("OAuth callback result missing");
  }
}
```

실패 처리:

```tsx
try {
  assertOAuthCallbackParams(searchParams);
  await handleOAuthCallback(searchParams);
} catch {
  clearAuth();

  navigate("/login", {
    replace: true,
    state: { message: "소셜 로그인 결과를 확인할 수 없습니다." },
  });
}
```

주의:

- parameter 누락 시 인증 성공 처리 금지
- 부분적으로 token만 저장한 상태 방지
- clearAuth 수행
- callback mode를 Backend와 통일
- returnUrl 누락은 기본 경로로 대체 가능
- error 없는 빈 callback은 실패로 처리
- cookie callback 방식은 query parameter 없이 `/me`로 확인할 수 있으므로 mode 구분 필요

---

### [FAQ]

Q. OAuth2 callback에 token도 code도 없으면?
A. 인증 결과를 확인할 수 없으므로 clearAuth 후 login 페이지로 이동시키는 것이 안전하다.

Q. returnUrl이 없으면 로그인 실패야?
A. 아니다. returnUrl은 없으면 기본 경로 `/`로 대체할 수 있다.

Q. callback parameter 이름이 Backend와 다르면?
A. Frontend가 값을 읽지 못해 로그인 실패처럼 처리될 수 있으므로 이름을 통일해야 한다.

Q. Cookie callback 방식은 parameter가 없어도 돼?
A. 가능하다. 이 경우 `/me` API로 cookie 인증 상태를 확인하는 별도 callback mode가 필요하다.

---

# 7. OAuth2 Security Rules

## 7.1 OAuth Secret and Frontend Environment

### [개념]

OAuth Secret은 Provider와 Backend 간 인증에 사용하는 민감정보다.

Frontend `.env`는 빌드 결과에 포함될 수 있으므로 OAuth Client Secret, private API key, server secret을 저장하면 안 된다.

---

### [핵심]

Frontend에 저장 금지:

- OAuth Client Secret
- Kakao Client Secret
- Google Client Secret
- Naver Client Secret
- Backend JWT Secret
- Refresh Token Secret
- private API key
- server-only token

Frontend에 허용 가능:

- public API base URL
- public OAuth provider name
- public client id 일부 상황
- public redirect path
- UI config

---

### [실무]

나쁜 예:

```env
VITE_KAKAO_CLIENT_SECRET=secret-value
REACT_APP_GOOGLE_CLIENT_SECRET=secret-value
```

가능한 예:

```env
VITE_API_BASE_URL=https://api.example.com
VITE_OAUTH_KAKAO_ENABLED=true
```

주의:

- Frontend 환경변수는 secret 보호 수단이 아님
- 빌드된 JavaScript에서 값 확인 가능
- Provider Secret은 Backend에서 관리
- OAuth token exchange는 Backend에서 처리
- 공개 client id도 provider 정책 확인
- secret 유출 시 즉시 rotation 필요

---

### [FAQ]

Q. Frontend .env에 OAuth secret을 넣어도 돼?
A. 안 된다. Frontend 환경변수는 빌드 결과에 노출될 수 있으므로 secret을 넣으면 안 된다.

Q. Frontend .env는 안전한 비밀 저장소야?
A. 아니다. Frontend 번들에 포함될 수 있으므로 공개되어도 되는 값만 넣어야 한다.

Q. OAuth token exchange는 어디서 해?
A. 일반적으로 Backend에서 수행한다. Provider secret이 필요할 수 있기 때문이다.

---

## 7.2 OAuth2 State and CSRF Awareness

### [개념]

OAuth2 State Parameter는 OAuth2 redirect flow에서 요청과 callback을 연결하고 CSRF 공격을 줄이기 위해 사용하는 값이다.

Frontend가 state를 직접 생성하거나 검증하는지, Backend가 state를 관리하는지는 프로젝트 OAuth2 설계에 따라 다르다.

---

### [핵심]

핵심 요소:

- state parameter
- CSRF prevention
- request correlation
- redirect integrity
- callback validation
- Backend state storage
- session / cookie state
- invalid_state error
- returnUrl binding

---

### [실무]

Backend 중심 state 관리 Flow:

```text
Frontend clicks social login
→ Backend creates state
→ Backend stores returnUrl if needed
→ Backend redirects provider
→ Provider returns state
→ Backend validates state
→ Backend redirects Frontend callback
```

Frontend returnUrl 포함 시 주의:

```text
returnUrl 전달
→ Backend stores with state
→ callback success
→ Backend returns safe returnUrl
→ Frontend validates again
```

주의:

- state 검증 누락은 보안 위험
- state는 예측 불가능해야 함
- returnUrl을 state와 묶어 관리 가능
- invalid_state는 단순 UX 오류가 아니라 보안 이벤트일 수 있음
- Frontend 단독 검증보다 Backend 검증이 중요
- OAuth2 Provider callback은 Backend가 받는 구조가 일반적

---

### [FAQ]

Q. OAuth2 state는 왜 필요해?
A. OAuth2 요청과 callback을 연결하고 CSRF 공격을 줄이기 위해 필요하다.

Q. state 검증은 Frontend가 해?
A. 프로젝트 구조에 따라 다르지만 Backend가 OAuth2 flow를 관리한다면 Backend에서 state를 생성하고 검증하는 경우가 많다.

Q. invalid_state가 나오면?
A. 인증 흐름이 유효하지 않은 상태로 보고 로그인 실패 처리하며 Backend 로그를 확인해야 한다.

Q. returnUrl과 state는 관련 있어?
A. Backend가 returnUrl을 state와 함께 저장하면 redirect 조작 위험을 줄일 수 있다.

---

## 7.3 OAuth2 Token URL Exposure

### [개념]

OAuth2 Token URL Exposure는 callback URL query string 또는 hash fragment에 token이 포함되어 노출되는 위험이다.

URL에 token이 남으면 browser history, server log, referrer, screenshot, 공유 URL을 통해 노출될 수 있다.

---

### [핵심]

노출 위치:

- browser address bar
- browser history
- server access log
- referrer header
- screenshot
- copied URL
- error report
- analytics
- monitoring tool

대응:

- replace navigation
- one-time code
- HttpOnly Cookie
- short-lived token
- no token logging
- sanitize error report
- safe redirect validation

---

### [실무]

즉시 cleanup:

```tsx
const accessToken = searchParams.get("accessToken");

if (accessToken) {
  setAccessToken(accessToken);
  window.history.replaceState({}, document.title, "/");
}
```

더 권장되는 대안:

```text
Token Query
→ 구현 단순
→ URL 노출 위험

One-Time Code
→ token 직접 노출 감소
→ code exchange 필요

HttpOnly Cookie
→ JS token 접근 차단
→ CSRF / CORS cookie 설정 필요
```

주의:

- token query 방식은 반드시 HTTPS 사용
- callback 처리 후 replace로 URL 제거
- referrer policy 검토 가능
- refresh token URL 전달은 특히 지양
- analytics page view에 token URL 전송 금지
- error boundary가 URL을 외부로 전송하지 않도록 주의

---

### [FAQ]

Q. URL에 token이 남아 있으면 왜 위험해?
A. browser history, screenshot, referrer, log, analytics를 통해 token이 노출될 수 있기 때문이다.

Q. token query 방식은 쓰면 안 돼?
A. 무조건 금지는 아니지만 위험을 이해하고 즉시 cleanup하며 가능하면 one-time code나 HttpOnly Cookie를 검토하는 것이 좋다.

Q. OAuth2 callback URL을 analytics에 보내도 돼?
A. token이 포함될 수 있으므로 analytics 전송 전에 URL을 정리해야 한다.

---

# 8. OAuth2 Troubleshooting

## 8.1 OAuth2 Callback Not Called

### [개념]

OAuth2 Callback Not Called는 소셜 로그인 후 Frontend Callback Page로 돌아오지 않는 문제다.

대부분 redirect URI 불일치, Backend OAuth2 설정 오류, Provider Console 설정 오류, Backend success handler redirect 누락으로 발생한다.

Provider Redirect URI와 Backend OAuth2 Callback 상세 설정은 Backend Security / OAuth2 문서에서 최종 확인한다.

---

### [핵심]

원인:

- Provider redirect URI mismatch
- Backend callback URL mismatch
- Frontend callback path mismatch
- OAuth2 success handler redirect missing
- wrong domain
- http / https mismatch
- port mismatch
- provider app setting
- environment variable mismatch

---

### [실무]

Debug Flow:

```text
소셜 로그인 후 callback 안 옴
→ Provider Console Redirect URI 확인
→ Backend OAuth2 redirect URI 확인
→ Backend success handler redirect 확인
→ Frontend callback route 존재 확인
→ domain / port / scheme 확인
→ local / production env 확인
```

예시:

```text
Provider Redirect URI
→ Backend OAuth2 Callback URI 예시

Backend Success Redirect
→ Frontend Callback URI 예시

Frontend Route
→ /oauth/callback
```

주의:

- Provider redirect URI는 보통 Backend callback URI
- Frontend callback URI와 Provider redirect URI를 혼동하지 않음
- Backend success handler가 Frontend로 redirect해야 함
- 로컬 포트와 배포 도메인 차이 확인
- http / https mismatch 확인
- trailing slash 차이 확인
- Backend Security / OAuth2 설정 문서와 함께 확인

---

### [FAQ]

Q. 소셜 로그인 후 Frontend callback으로 안 돌아와?
A. Provider redirect URI, Backend OAuth2 callback, Backend success redirect, Frontend callback route를 순서대로 확인해야 한다.

Q. Provider redirect URI는 Frontend callback 주소야?
A. Backend가 OAuth2 flow를 담당한다면 Provider redirect URI는 보통 Backend callback 주소다.

Q. 로컬에서는 되는데 배포에서 안 돼?
A. 배포 도메인, HTTPS, Provider Console redirect URI, Backend 환경변수 설정을 확인해야 한다.

Q. Provider Redirect URI 상세 설정은 어디서 확인해?
A. Backend Security / OAuth2 문서에서 최종 확인한다.

---

## 8.2 OAuth2 Login Success but User Missing

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
- /me 401
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

## 8.3 OAuth2 Redirect Loop

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
- /me fails then retry social login
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

권장 callback route:

```tsx
<Route path="/oauth/callback" element={<OAuthCallbackPage />} />
```

Safe Redirect 보정:

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

# 9. Part08 Review Checklist

## 9.1 OAuth2 Frontend Flow Checklist

### [개념]

Part08 검수는 OAuth2 Social Login, Callback Handling, Redirect, New User Flow, 선택적 Account Linking, Error Handling, Security가 일관되게 연결되는지 확인한다.

---

### [핵심]

Checklist:

```md
- [ ] OAuth2 Frontend 책임이 명확한가?
- [ ] Backend OAuth2 책임과 분리되었는가?
- [ ] OAuth Secret Frontend 저장 금지가 포함되었는가?
- [ ] Social Login Button 기준이 포함되었는가?
- [ ] Backend OAuth2 Authorization Endpoint 기준이 포함되었는가?
- [ ] OAuth2 Flow Variants가 포함되었는가?
- [ ] OAuth2 Callback Page 기준이 포함되었는가?
- [ ] Callback route auth guard 예외 기준이 포함되었는가?
- [ ] Token Query Callback 기준이 포함되었는가?
- [ ] Authorization Code Callback 기준이 포함되었는가?
- [ ] HttpOnly Cookie Callback 기준이 포함되었는가?
- [ ] Redirect After OAuth2 기준이 포함되었는가?
- [ ] returnUrl 전달 방식이 Backend 정책 의존임을 명시했는가?
- [ ] Safe returnUrl 검증 기준이 포함되었는가?
- [ ] OAuth2 New User Flow 기준이 포함되었는가?
- [ ] temporary token이 필수 구조가 아님을 명시했는가?
- [ ] Account Linking / Unlink가 선택 기능임을 명시했는가?
- [ ] OAuth2 Callback Error Handling이 포함되었는가?
- [ ] Missing Parameter 처리가 포함되었는가?
- [ ] OAuth2 State / CSRF 인식이 포함되었는가?
- [ ] Token URL Exposure 주의가 포함되었는가?
- [ ] Callback Not Called Troubleshooting이 포함되었는가?
- [ ] Provider Redirect URI 상세 설정은 Backend Security 문서 참조로 분리되었는가?
- [ ] Login Success but User Missing Troubleshooting이 포함되었는가?
- [ ] OAuth2 Redirect Loop Troubleshooting이 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

Part08 이후 권장 문서 순서:

```text
Part08 OAuth2 Frontend Flow
→ Part09 401 / 403 / Troubleshooting
→ Part10 Security / Checklist / Retrieval Optimization
```

검수 기준:

```text
Social Login Button
→ Backend OAuth2 Redirect
→ Provider Login
→ Frontend Callback
→ Token / Code / Cookie Handling
→ Auth State Update
→ Safe Redirect
→ Security Review
→ Troubleshooting
```

---

### [FAQ]

Q. Part08의 핵심은 뭐야?
A. OAuth2 소셜 로그인 버튼, Backend OAuth2 redirect, callback 처리, token/code/cookie 방식, Auth State 갱신, 보안 주의사항을 정리하는 것이다.

Q. Part08에서 Backend OAuth2 설정을 구현해?
A. 아니다. Backend OAuth2 Provider 설정과 Security 설정은 Backend Security 문서에서 다루고 Part08은 Frontend 흐름을 다룬다.

Q. Account Linking은 Part08 필수 범위야?
A. 아니다. 기본 로그인 흐름의 필수 요소가 아니라 계정 설정 기능이 있는 서비스에서 선택적으로 적용한다.

Q. Part08 다음 문서는 뭐야?
A. 401 / 403 / Troubleshooting 문서가 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. OAuth2 Frontend Flow는 뭐야?
A. 사용자가 소셜 로그인 버튼을 누른 뒤 Backend OAuth2 Endpoint로 이동하고, 로그인 결과를 Frontend Callback Page에서 처리하는 흐름이다.

Q. 소셜 로그인 버튼은 Frontend에서 뭘 해?
A. 대부분 Backend OAuth2 authorization endpoint로 redirect한다.

Q. Kakao client secret을 Frontend에 넣어도 돼?
A. 안 된다. Frontend에 secret을 넣으면 노출된다. secret은 Backend에서 관리해야 한다.

Q. OAuth2 전체 인증 검증은 Frontend가 해?
A. 아니다. Provider 연동, token exchange, 사용자 검증, JWT 발급은 Backend가 담당한다.

Q. Provider Redirect URI 상세 설정은 이 문서에서 다뤄?
A. 아니다. Frontend 흐름에서는 개념만 다루고 상세 설정은 Backend Security / OAuth2 문서에서 확인한다.

Q. OAuth2 callback에서 token을 URL로 받아도 돼?
A. 가능은 하지만 URL 노출 위험이 있으므로 즉시 처리 후 replace navigation으로 제거해야 한다.

Q. HttpOnly Cookie 방식이면 Frontend는 뭘 해?
A. callback 후 `/me` API를 호출해 인증 상태와 user summary를 복원한다.

Q. one-time login code 방식은 왜 써?
A. access token을 URL에 직접 노출하지 않고 짧은 수명의 code를 Backend에 교환하기 위해 사용한다.

Q. OAuth2 방식은 Frontend가 정해도 돼?
A. 아니다. Backend OAuth2 설계와 보안 정책에 맞춰 Frontend 처리 방식을 맞춘다.

Q. 소셜 로그인 버튼에서 axios 요청을 보내?
A. 보통 axios 요청이 아니라 `window.location.href`로 Backend OAuth2 시작 URL로 이동한다.

Q. Provider OAuth URL을 Frontend에서 직접 만들면 안 돼?
A. 가능은 하지만 secret, redirect URI, state 검증이 복잡해지므로 Backend OAuth2 Endpoint로 이동하는 방식이 일반적이다.

Q. returnUrl은 반드시 Frontend가 query로 붙여야 해?
A. 아니다. Backend가 state 또는 session에 저장할 수도 있다. 프로젝트 Backend OAuth2 설계에 맞춘다.

Q. OAuth2 callback page는 왜 필요해?
A. 소셜 로그인 결과로 전달된 token, code, error를 처리하고 Auth State를 갱신한 뒤 최종 페이지로 이동시키기 위해 필요하다.

Q. OAuth2 callback에서 에러가 오면?
A. login 페이지로 이동하고 사용자에게 로그인 실패 메시지를 보여준다.

Q. OAuth2 callback도 PublicOnlyRoute로 감싸도 돼?
A. 주의해야 한다. callback 처리 전에 authenticated 상태가 바뀌거나 redirect가 발생하면 OAuth2 처리가 중단될 수 있다.

Q. OAuth2 callback을 ProtectedRoute로 감싸도 돼?
A. 권장하지 않는다. 로그인 결과를 처리해야 하는 route이므로 인증 전에도 접근 가능해야 한다.

Q. OAuth2 callback에서 token을 URL로 받으면 어떻게 해?
A. 즉시 저장 또는 처리한 뒤 replace navigation으로 URL에서 token을 제거하는 것이 좋다.

Q. refreshToken도 URL로 받아도 돼?
A. 권장하지 않는다. refreshToken은 더 민감하므로 HttpOnly Cookie나 one-time code 방식을 우선 검토하는 것이 좋다.

Q. URL에서 token을 제거하지 않으면?
A. 브라우저 history, screenshot, log, 공유 URL에 token이 노출될 수 있다.

Q. code 방식은 token query 방식보다 안전해?
A. access token을 URL에 직접 노출하지 않는 장점이 있다. 단 code 만료와 1회 사용 정책이 필요하다.

Q. code exchange API는 authApi로 호출해?
A. 로그인 전 상태이므로 보통 publicApi로 호출한다.

Q. code도 URL에서 제거해야 해?
A. token보다 위험도는 낮을 수 있지만 재사용 방지와 노출 최소화를 위해 callback 처리 후 URL cleanup을 권장한다.

Q. HttpOnly Cookie 방식에서는 OAuth2 callback에서 token을 읽어?
A. 아니다. Frontend는 token을 읽지 않고 `/me` API로 인증 상태를 확인한다.

Q. Cookie 방식 OAuth2에서 Authorization Header가 필요해?
A. Backend가 Cookie Auth를 기준으로 하면 Authorization Header가 필요 없을 수 있다.

Q. Cookie 방식인데 /me가 401이 나?
A. cookie가 전송되지 않았거나 CORS credentials, SameSite, Secure, Backend cookie 설정 문제가 있을 수 있다.

Q. 소셜 로그인 후 원래 보려던 페이지로 돌아가려면?
A. OAuth2 시작 시 returnUrl을 저장하고 callback에서 검증 후 해당 경로로 navigate한다.

Q. OAuth2 returnUrl도 검증해야 해?
A. 해야 한다. 외부 URL redirect와 callback loop를 막기 위해 내부 경로인지 확인해야 한다.

Q. returnUrl은 Frontend가 관리해 Backend가 관리해?
A. 프로젝트에 따라 다르다. Frontend query 방식, Backend state/session 방식 모두 가능하며 safe redirect 검증은 필요하다.

Q. 신규 소셜 가입자는 바로 main으로 보내도 돼?
A. 약관 동의, 추가 정보 입력, 이메일 확인이 필요하면 profile setup이나 terms page로 보내야 한다.

Q. 소셜 로그인 신규 사용자는 바로 회원가입 완료야?
A. 서비스 정책에 따라 다르다. 약관 동의, 닉네임, 추가 정보 입력이 필요하면 onboarding flow가 필요하다.

Q. provider에서 email이 안 오면?
A. 추가 입력 화면에서 email을 받거나 email 없는 계정 정책을 Backend와 정해야 한다.

Q. temporary token은 OAuth2 신규 사용자 flow에서 필수야?
A. 아니다. Backend 정책에 따라 정식 token, 임시 token, one-time setup code, HttpOnly Cookie 중 하나를 사용할 수 있다.

Q. profile setup 완료 후 뭘 해야 해?
A. `/me`를 다시 조회하거나 Auth State user summary를 갱신한 뒤 main 또는 returnUrl로 이동한다.

Q. 소셜 로그인과 계정 연결은 같은 거야?
A. 아니다. 소셜 로그인은 인증 방식이고 계정 연결은 기존 계정에 provider를 추가하는 흐름이다.

Q. Account Linking은 필수 구현이야?
A. 아니다. 기본 로그인 흐름의 필수 요소가 아니라 계정 설정 기능이 있는 서비스에서 선택적으로 적용한다.

Q. 연결된 소셜 계정을 그냥 해제해도 돼?
A. 마지막 로그인 수단인지 확인해야 한다. 해제 후 로그인 불가능한 상태가 되지 않도록 Backend 정책이 필요하다.

Q. Account Unlink는 필수 구현이야?
A. 아니다. 계정 설정 기능이 있는 서비스에서 선택적으로 적용한다.

Q. 사용자가 소셜 로그인을 취소하면 에러야?
A. 기술적으로 error callback이 올 수 있으며 사용자에게 “로그인이 취소되었습니다” 정도로 안내할 수 있다.

Q. invalid_state는 단순 로그인 실패야?
A. 사용자에게는 실패로 안내하지만 보안상 중요한 이벤트일 수 있으므로 Backend 로그 확인이 필요하다.

Q. OAuth2 callback에 token도 code도 없으면?
A. 인증 결과를 확인할 수 없으므로 clearAuth 후 login 페이지로 이동시키는 것이 안전하다.

Q. Cookie callback 방식은 parameter가 없어도 돼?
A. 가능하다. 이 경우 `/me` API로 cookie 인증 상태를 확인하는 별도 callback mode가 필요하다.

Q. Frontend .env에 OAuth secret을 넣어도 돼?
A. 안 된다. Frontend 환경변수는 빌드 결과에 노출될 수 있으므로 secret을 넣으면 안 된다.

Q. OAuth token exchange는 어디서 해?
A. 일반적으로 Backend에서 수행한다. Provider secret이 필요할 수 있기 때문이다.

Q. OAuth2 state는 왜 필요해?
A. OAuth2 요청과 callback을 연결하고 CSRF 공격을 줄이기 위해 필요하다.

Q. state 검증은 Frontend가 해?
A. 프로젝트 구조에 따라 다르지만 Backend가 OAuth2 flow를 관리한다면 Backend에서 state를 생성하고 검증하는 경우가 많다.

Q. returnUrl과 state는 관련 있어?
A. Backend가 returnUrl을 state와 함께 저장하면 redirect 조작 위험을 줄일 수 있다.

Q. URL에 token이 남아 있으면 왜 위험해?
A. browser history, screenshot, referrer, log, analytics를 통해 token이 노출될 수 있기 때문이다.

Q. OAuth2 callback URL을 analytics에 보내도 돼?
A. token이 포함될 수 있으므로 analytics 전송 전에 URL을 정리해야 한다.

Q. 소셜 로그인 후 Frontend callback으로 안 돌아와?
A. Provider redirect URI, Backend OAuth2 callback, Backend success redirect, Frontend callback route를 순서대로 확인해야 한다.

Q. Provider redirect URI는 Frontend callback 주소야?
A. Backend가 OAuth2 flow를 담당한다면 Provider redirect URI는 보통 Backend callback 주소다.

Q. Provider Redirect URI 상세 설정은 어디서 확인해?
A. Backend Security / OAuth2 문서에서 최종 확인한다.

Q. OAuth2 로그인 성공했는데 Header가 로그인 상태로 안 바뀌어?
A. callback에서 `/me` API 호출 또는 user state 설정이 누락되었을 가능성이 있다.

Q. OAuth2 후 token은 있는데 user가 null이야?
A. token 저장 후 Auth State user를 채우지 않았거나 `/me` 호출이 실패했을 수 있다.

Q. Cookie 방식 OAuth2 후 /me가 401이야?
A. cookie 전송 설정, withCredentials, SameSite, Secure, Backend CORS credentials 설정을 확인해야 한다.

Q. OAuth2 callback과 login이 계속 반복돼?
A. callback route guard 설정, Auth State 갱신 순서, returnUrl이 login 또는 callback인지 확인해야 한다.

Q. returnUrl이 callback이면 어떻게 해?
A. callback loop를 막기 위해 기본 경로 `/`로 보정하는 것이 좋다.

Q. Part08 다음 문서는 뭐야?
A. 401 / 403 / Troubleshooting 문서가 이어지는 것이 좋다.
