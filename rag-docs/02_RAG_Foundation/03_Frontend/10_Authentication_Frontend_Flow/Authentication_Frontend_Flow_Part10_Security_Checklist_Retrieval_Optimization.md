# Authentication Frontend Flow Part10 - Security / Final Checklist / Retrieval Optimization

---

# 1. Frontend Auth Security Overview

## 1.1 Frontend Security Responsibility

### [개념]

Frontend Auth Security는 로그인 상태 UX, token 전달, Route Guard, 권한 UI 분기, 오류 메시지, 민감정보 노출 방지를 안전하게 설계하는 기준이다.

Frontend는 인증 흐름을 보조하지만 최종 보안 판단자가 아니다.

실제 token 검증, 사용자 식별, 권한 판단, API 접근 제어는 Backend Authorization이 수행해야 한다.

Part10은 Part01부터 Part09까지의 구현 내용을 반복 설명하는 문서가 아니라, 최종 보안 검수와 RAG Retrieval 최적화를 위한 기준 문서다.

---

### [핵심]

Frontend Auth Security 핵심:

- token 노출 방지
- password 노출 방지
- Authorization Header 노출 방지
- Frontend `.env` secret 금지
- OAuth Client Secret 저장 금지
- token URL cleanup
- Auth State 최소화
- user summary 최소화
- Protected Route는 UX Guard
- Role Based UI는 UX Guard
- Backend Authorization Required
- 401 / 403 분리
- logout cleanup
- user-specific cache cleanup
- OAuth2 callback security
- XSS Awareness
- CSRF Awareness

Frontend가 하는 일:

```text
Auth UX 처리
→ token 전달
→ 인증 상태 표시
→ route guard
→ role based UI
→ 오류 메시지
→ logout cleanup
```

Backend가 하는 일:

```text
Token 발급
→ Token 검증
→ 사용자 식별
→ Role / Owner 검증
→ API 접근 제어
→ 401 / 403 응답
```

---

### [실무]

2026 실무 기준 Frontend 인증 보안은 “화면에서 막았으니 안전하다”가 아니다.

Frontend는 아래 기준으로 안전성을 높인다.

```text
민감정보를 저장하지 않는다
→ 저장해야 한다면 최소화한다
→ 전송 시 형식을 통일한다
→ 오류 시 상태를 정리한다
→ 권한 판단은 Backend에 맡긴다
```

필수 주의:

- password console.log 금지
- accessToken console.log 금지
- refreshToken console.log 금지
- Authorization Header error log 금지
- Frontend `.env` secret 금지
- URL query token 즉시 제거
- token 존재만으로 authenticated 확정 금지
- Auth Restore는 `/me` 또는 Backend 검증 기반
- 403에서 logout 기본 처리 금지
- logout 시 cache와 private state 정리
- 관리자 버튼 숨김은 보안이 아님
- Backend API에서 role / owner 검증 필수

---

### [FAQ]

Q. Frontend Auth Security의 핵심은 뭐야?
A. 민감정보 노출을 줄이고 Auth State, token 전달, Route Guard, 오류 처리를 안전하게 구성하되 최종 보안은 Backend가 담당한다는 기준이다.

Q. Frontend에서 Protected Route를 만들면 보안이 완성돼?
A. 아니다. Protected Route는 UX Guard이고 실제 API 접근 제어는 Backend Authorization이 수행해야 한다.

Q. 관리자 버튼을 숨기면 관리자 기능이 안전해져?
A. 아니다. 버튼 숨김은 UX용이고 관리자 API는 Backend에서 ROLE_ADMIN 검증을 해야 한다.

Q. Part10은 구현 상세 문서야?
A. 아니다. Part02부터 Part09까지의 구현 내용을 최종 검수하고 검색 가능하게 묶는 보안 / 체크리스트 / Retrieval 최적화 문서다.

---

# 2. Sensitive Data Exposure Prevention

## 2.1 Password and Token Logging Ban

### [개념]

Password and Token Logging Ban은 password, accessToken, refreshToken, Authorization Header 같은 민감정보를 console, error log, monitoring, analytics, screenshot, URL에 남기지 않는 기준이다.

민감정보는 한 번 노출되면 사용자의 계정 접근 권한이 탈취될 수 있다.

---

### [핵심]

로그 금지 대상:

- password
- confirmPassword
- accessToken
- refreshToken
- Authorization Header
- OAuth authorization code
- one-time login code
- session identifier
- cookie value
- CSRF token
- provider token

노출 위험 위치:

- browser console
- Network tab 공유
- error report
- monitoring SDK
- analytics event
- URL query string
- browser history
- screenshot
- clipboard
- localStorage inspection

---

### [실무]

금지 예:

```tsx
console.log(password);
console.log(accessToken);
console.log(refreshToken);
console.log(error.config.headers.Authorization);
```

권장 Debug 예:

```tsx
console.log({
  hasAccessToken: Boolean(accessToken),
  status: error.response?.status,
});
```

Error Sanitizing 예:

```tsx
function sanitizeAuthError(error: unknown) {
  if (!isAxiosError(error)) {
    return {
      message: "Unknown error",
    };
  }

  return {
    status: error.response?.status,
    code: error.response?.data?.code,
    message: error.response?.data?.message,
  };
}
```

주의:

- token 전체 문자열을 출력하지 않음
- Authorization Header를 error reporting에 보내지 않음
- OAuth2 callback URL을 analytics에 보내기 전 cleanup
- Network 탭 캡처 공유 시 token 마스킹
- password field value를 debug object에 포함하지 않음
- 개발용 log도 배포 전 제거
- logging utility에서 auth header redaction 적용

---

### [FAQ]

Q. token을 console.log로 찍어도 돼?
A. 안 된다. token은 인증에 사용되는 민감정보이므로 로그에 남기지 않는 것이 원칙이다.

Q. password를 디버깅하려면 어떻게 해?
A. 값 자체를 출력하지 말고 입력 여부, validation 결과, status code 정도만 확인한다.

Q. Authorization Header를 에러 로그에 남겨도 돼?
A. 안 된다. Authorization Header에는 token이 포함될 수 있으므로 로그 전송 전에 제거해야 한다.

Q. OAuth2 callback URL을 analytics에 보내도 돼?
A. token이나 code가 포함될 수 있으므로 analytics 전송 전에 URL을 정리해야 한다.

---

## 2.2 Frontend Environment Secret Ban

### [개념]

Frontend Environment Secret Ban은 Frontend `.env` 또는 client bundle에 OAuth Client Secret, JWT Secret, private API key 같은 비밀값을 저장하지 않는 기준이다.

Frontend 환경변수는 빌드 결과에 포함될 수 있으므로 secret 보호 수단이 아니다.

---

### [핵심]

Frontend 저장 금지:

- OAuth Client Secret
- Kakao Client Secret
- Google Client Secret
- Naver Client Secret
- JWT Secret
- Refresh Token Secret
- Database Password
- Server Private Key
- private API key
- Admin API Secret
- Backend internal token

Frontend 저장 가능 후보:

- public API base URL
- public provider name
- public feature flag
- public redirect path
- public client id 일부 상황
- UI config
- app version

---

### [실무]

나쁜 예:

```env
VITE_KAKAO_CLIENT_SECRET=secret-value
REACT_APP_JWT_SECRET=secret-value
VITE_DATABASE_PASSWORD=password
```

가능한 예:

```env
VITE_API_BASE_URL=https://api.example.com
VITE_OAUTH_KAKAO_ENABLED=true
VITE_APP_VERSION=1.0.0
```

검수 기준:

```text
.env 값 확인
→ 공개되어도 되는 값인가?
→ Backend 전용 secret인가?
→ Provider Secret인가?
→ 빌드 결과에 노출되어도 안전한가?
```

주의:

- Frontend `.env`는 secret vault가 아님
- 빌드된 JS에서 값 확인 가능
- OAuth token exchange는 Backend에서 처리
- secret이 노출되면 rotation 필요
- Provider Console에 등록된 secret은 Backend에서만 사용
- API baseURL은 secret이 아님
- private API key가 필요한 외부 API는 Backend proxy 검토

---

### [FAQ]

Q. Frontend .env에 OAuth secret을 넣어도 돼?
A. 안 된다. Frontend 환경변수는 빌드 결과에 노출될 수 있으므로 secret을 넣으면 안 된다.

Q. Frontend .env는 안전한 비밀 저장소야?
A. 아니다. Frontend 번들에 포함될 수 있으므로 공개되어도 되는 값만 넣어야 한다.

Q. API 서버 주소는 .env에 넣어도 돼?
A. 가능하다. API base URL처럼 공개되어도 되는 값은 넣을 수 있다.

Q. private API key가 필요한 외부 API는 어떻게 써?
A. Frontend에 직접 넣지 말고 Backend를 통해 proxy하거나 Backend에서 호출하는 구조를 검토한다.

---

## 2.3 URL Token Exposure Prevention

### [개념]

URL Token Exposure Prevention은 OAuth2 callback이나 redirect flow에서 token, code, session identifier가 URL에 남아 노출되는 것을 방지하는 기준이다.

URL에 민감값이 남으면 browser history, referrer, log, screenshot, 공유 URL을 통해 노출될 수 있다.

---

### [핵심]

위험 대상:

- accessToken query
- refreshToken query
- authorization code query
- one-time login code query
- hash fragment token
- returnUrl에 민감값 포함
- error report URL
- analytics page URL

대응:

- replace navigation
- history.replaceState
- one-time code 사용
- HttpOnly Cookie 사용
- short-lived code 사용
- referrer policy 검토
- analytics 전 URL cleanup
- refreshToken URL 전달 지양

---

### [실무]

Callback URL cleanup 예:

```tsx
const accessToken = searchParams.get("accessToken");

if (accessToken) {
  setAccessToken(accessToken);
  window.history.replaceState({}, document.title, "/");
}
```

React Router cleanup 예:

```tsx
navigate("/", { replace: true });
```

권장 방식 비교:

```text
Token Query
→ 구현 쉬움
→ URL 노출 위험
→ 즉시 cleanup 필수

One-Time Code
→ token 직접 노출 감소
→ code exchange 필요

HttpOnly Cookie
→ JS token 접근 차단
→ CSRF / Cookie 설정 필요
```

주의:

- URL에 token을 오래 남기지 않음
- refreshToken query 전달은 특히 지양
- callback 처리 중 error boundary가 URL을 외부 전송하지 않게 주의
- analytics SDK page view 전송 시 URL cleanup 확인
- returnUrl에 외부 URL 또는 민감값 포함 금지
- HTTPS 사용 필수
- token cleanup 전 console.log 금지

---

### [FAQ]

Q. OAuth2 callback에서 token을 URL로 받으면 어떻게 해?
A. 즉시 저장 또는 처리한 뒤 replace navigation으로 URL에서 token을 제거하는 것이 좋다.

Q. URL에서 token을 제거하지 않으면?
A. 브라우저 history, screenshot, log, 공유 URL에 token이 노출될 수 있다.

Q. refreshToken도 URL로 받아도 돼?
A. 권장하지 않는다. refreshToken은 더 민감하므로 HttpOnly Cookie나 one-time code 방식을 우선 검토하는 것이 좋다.

Q. token query 방식은 무조건 금지야?
A. 무조건 금지는 아니지만 위험을 이해하고 즉시 cleanup하며 가능하면 one-time code나 HttpOnly Cookie를 검토하는 것이 좋다.

---

# 3. Token Storage Security Final Rules

## 3.1 Storage Option Security Review

### [개념]

Token Storage Security Review는 accessToken과 refreshToken을 어디에 저장할지 결정할 때 보안, UX, 새로고침 복원, Backend 정책을 함께 검토하는 기준이다.

어떤 저장 방식도 완전한 정답은 아니며 프로젝트 상황에 맞춰 선택한다.

Token Storage 상세 구현과 lifecycle은 Part04에서 다루고, 이 문서에서는 최종 검수 기준만 정리한다.

---

### [핵심]

저장 방식 비교:

| 저장 위치       | 장점                         | 주요 위험             | 사용 기준                      |
| --------------- | ---------------------------- | --------------------- | ------------------------------ |
| Memory State    | persistent storage 노출 감소 | 새로고침 시 사라짐    | 보안 우선, refresh cookie 조합 |
| sessionStorage  | 탭 단위 유지                 | XSS 노출 가능         | 학습/단순 프로젝트             |
| localStorage    | 새로고침/재시작 유지         | XSS 노출 가능         | 편의성 우선, 위험 문서화       |
| HttpOnly Cookie | JS 접근 불가                 | CSRF / CORS 설정 필요 | refresh token 보호             |
| Zustand Persist | 구현 편리                    | 민감정보 persist 위험 | 최소 user summary만 권장       |
| Redux Persist   | 전역 상태 유지               | 민감정보 persist 위험 | auth 정보 최소화 필요          |

기본 원칙:

- refreshToken은 accessToken보다 더 민감
- token 저장은 최소화
- user summary 저장은 최소화
- logout 시 저장소 정리
- token 존재만으로 authenticated 확정 금지
- 저장 정책은 Backend와 함께 결정

---

### [실무]

권장 패턴 후보:

```text
학습 프로젝트
→ sessionStorage accessToken
→ refreshToken 생략 또는 제한적 사용
→ 위험성 문서화
```

```text
일반 서비스
→ accessToken memory
→ refreshToken HttpOnly Cookie
→ /me 기반 Auth Restore
```

```text
Cookie Auth 서비스
→ HttpOnly Secure Cookie
→ SameSite / CSRF 대응
→ withCredentials 설정
→ /me 기반 인증 확인
```

주의:

- localStorage와 sessionStorage는 XSS에 노출될 수 있음
- HttpOnly Cookie는 CSRF 대응 필요
- Memory State도 XSS 위험이 완전히 사라지는 것은 아님
- Browser extension과 공유 PC 환경 고려
- refreshToken을 Web Storage에 저장하는 것은 신중히 결정
- logout 시 token, Auth State, cache, private state 정리
- token 저장 방식과 Auth Restore 방식은 함께 설계

---

### [FAQ]

Q. token은 localStorage에 저장하면 돼?
A. 가능은 하지만 XSS 위험이 있다. 프로젝트 보안 요구사항에 따라 memory, sessionStorage, HttpOnly Cookie 등을 검토해야 한다.

Q. sessionStorage는 안전해?
A. localStorage보다 유지 범위는 좁지만 JavaScript 접근이 가능하므로 XSS 위험은 여전히 있다.

Q. HttpOnly Cookie가 무조건 정답이야?
A. 항상 정답은 아니다. JS 접근 차단 장점이 있지만 CSRF, SameSite, Backend 설정 등 함께 고려해야 한다.

Q. refreshToken은 어디에 저장하는 게 좋아?
A. 보안 요구가 있다면 HttpOnly Cookie를 우선 검토하고 Web Storage 저장은 신중히 결정해야 한다.

---

## 3.2 XSS Awareness for Frontend Auth

### [개념]

XSS Awareness는 악성 script가 Frontend에서 실행될 경우 token, user data, private state가 노출될 수 있다는 위험을 인식하고 줄이는 기준이다.

Frontend Auth 문서는 XSS 전체 방어 문서가 아니지만 token 저장과 민감정보 관리에서 XSS 위험을 고려해야 한다.

---

### [핵심]

XSS 위험 대상:

- localStorage token
- sessionStorage token
- JS memory token
- user profile data
- private cache
- form draft
- Authorization Header
- DOM injection
- unsafe HTML rendering

기본 대응 인식:

- token 저장 최소화
- refreshToken Web Storage 저장 지양
- `dangerouslySetInnerHTML` 주의
- 사용자 입력 escape
- 외부 HTML 렌더링 주의
- CSP 검토
- dependency 보안 관리
- 민감정보 log 금지

---

### [실무]

위험 예:

```tsx
<div dangerouslySetInnerHTML={{ __html: userInputHtml }} />
```

권장 인식:

```text
XSS 발생 가능성 있음
→ Web Storage token 탈취 가능
→ token 저장 최소화 필요
→ HttpOnly Cookie 또는 memory 조합 검토
→ 사용자 입력 렌더링 주의
```

주의:

- localStorage token은 XSS 발생 시 탈취 가능
- sessionStorage도 XSS에 안전하지 않음
- HttpOnly Cookie는 JS 직접 접근을 막지만 CSRF 고려 필요
- React가 기본적으로 text escaping을 제공하지만 unsafe HTML은 별도 주의
- auth error message에 서버 원문 HTML을 직접 렌더링하지 않음
- user profile field를 HTML로 직접 렌더링하지 않음

---

### [FAQ]

Q. localStorage에 token을 저장하면 보안상 위험해?
A. XSS가 발생하면 JavaScript로 token을 읽을 수 있으므로 위험할 수 있다.

Q. sessionStorage는 XSS에 안전해?
A. 아니다. JavaScript로 접근 가능하므로 XSS가 발생하면 노출될 수 있다.

Q. HttpOnly Cookie를 쓰면 XSS가 완전히 해결돼?
A. token 직접 접근은 줄일 수 있지만 XSS 자체와 CSRF 문제는 별도로 고려해야 한다.

Q. Auth 문서에서 XSS 전체 방어를 다뤄?
A. 아니다. 여기서는 token 저장과 민감정보 노출 관점의 XSS 인식을 다룬다.

---

## 3.3 CSRF Awareness for Cookie Auth

### [개념]

CSRF Awareness는 Cookie 기반 인증에서 브라우저가 cookie를 자동으로 전송할 수 있기 때문에 발생하는 요청 위조 위험을 고려하는 기준이다.

HttpOnly Cookie를 사용할 때는 CSRF, SameSite, Secure, CORS credentials 설정을 Backend와 함께 검토해야 한다.

---

### [핵심]

CSRF 관련 키워드:

- HttpOnly Cookie
- SameSite
- Secure
- CSRF Token
- withCredentials
- CORS credentials
- unsafe method
- POST / PATCH / DELETE
- Cookie Auth
- Backend CSRF Defense

검토 기준:

```text
Cookie Auth 사용
→ cookie 자동 전송 가능
→ SameSite 정책 확인
→ CSRF token 필요 여부 확인
→ CORS credentials 설정 확인
→ Backend CSRF 방어 확인
```

---

### [실무]

Cookie Auth Axios 예:

```tsx
export const authApi = axios.create({
  baseURL: API_BASE_URL,
  withCredentials: true,
});
```

CSRF Token Header 예:

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

- HttpOnly Cookie는 JS token 접근 차단에 유리
- Cookie Auth는 CSRF 대응이 필요할 수 있음
- SameSite=Lax / Strict / None 정책 확인
- SameSite=None이면 Secure 필요
- cross-origin cookie는 CORS credentials 설정 필요
- CSRF Token 방식은 Backend 정책과 일치해야 함
- Auth 문서는 CSRF 전체 심화가 아니라 Cookie Auth 인식 수준을 다룸

---

### [FAQ]

Q. Cookie Auth에서도 CSRF를 고려해야 해?
A. 해야 한다. Cookie는 자동 전송될 수 있으므로 SameSite, CSRF token, Backend 방어 정책을 함께 고려해야 한다.

Q. withCredentials는 언제 필요해?
A. cross-origin 요청에서 cookie를 포함해야 할 때 필요할 수 있으며 Backend CORS 설정과 함께 맞춰야 한다.

Q. HttpOnly Cookie를 쓰면 Authorization Header가 필요 없어?
A. Cookie 기반 인증이면 필요 없을 수 있다. Backend 인증 방식에 따라 Header Auth와 Cookie Auth 중 기준을 통일해야 한다.

Q. CSRF Token Header는 Frontend에서 넣어야 해?
A. Backend가 CSRF Token 방식을 요구한다면 Frontend에서 해당 Header를 포함해야 한다.

---

# 4. Backend Authorization Required

## 4.1 Frontend Guard Is Not Security Boundary

### [개념]

Frontend Guard는 사용자의 화면 접근과 UX를 정리하는 장치다.

Frontend Guard는 보안 경계가 아니다.

사용자는 브라우저 개발자 도구, 직접 HTTP 요청, 수정된 client code를 통해 Frontend guard를 우회할 수 있다.

따라서 모든 보호 API는 Backend에서 인증과 인가를 검증해야 한다.

---

### [핵심]

Frontend UX Guard:

- Protected Route
- PublicOnlyRoute
- Role Based Route
- Role Based UI
- PermissionGate
- Owner button hiding
- conditional rendering

Backend Security Boundary:

- JWT 검증
- Session 검증
- Role Authorization
- Owner Authorization
- Resource Authorization
- API 접근 제어
- 401 response
- 403 response

필수 원칙:

```text
Frontend에서 숨긴다
→ UX 개선

Backend에서 막는다
→ 실제 보안
```

---

### [실무]

관리자 메뉴 예:

```tsx
{
  user?.role === "ROLE_ADMIN" && <Link to="/admin">Admin</Link>;
}
```

Backend 검증 필수:

```text
GET /admin/users
→ Backend JWT 검증
→ ROLE_ADMIN 확인
→ 권한 없으면 403
```

작성자 버튼 예:

```tsx
{
  user?.userId === post.authorId && <button>삭제</button>;
}
```

Backend 검증 필수:

```text
DELETE /posts/{postId}
→ Backend JWT 검증
→ post.authorId == currentUserId 확인
→ 아니면 403
```

주의:

- Frontend에서 role check를 해도 API 권한 검증 필수
- 버튼 숨김은 보안이 아님
- Route Guard 통과와 API 권한은 별개
- Backend는 current user 기준으로 resource owner를 다시 확인
- Frontend userId는 조작 가능하다고 가정
- 403은 Backend Authorization 실패로 볼 수 있음

---

### [FAQ]

Q. Frontend에서 ROLE_ADMIN을 확인하면 관리자 API가 안전해져?
A. 아니다. Frontend role check는 화면 접근 UX용이고 관리자 API는 Backend에서 반드시 권한 검증해야 한다.

Q. 삭제 버튼을 작성자에게만 보여주면 충분해?
A. 아니다. 버튼 표시 제어는 UX용이고 실제 삭제 API는 Backend에서 작성자 여부를 검증해야 한다.

Q. Protected Route로 감싸면 API 호출도 막혀?
A. 아니다. 화면 접근 UX만 막는 것이고 API 접근은 Backend Authorization으로 막아야 한다.

Q. Backend Authorization Required는 왜 반복해서 써야 해?
A. Agent가 Frontend UI 제어를 실제 보안으로 착각하지 않도록 하기 위해 반드시 반복 명시해야 한다.

---

## 4.2 401 and 403 Backend Contract

### [개념]

401 and 403 Backend Contract는 Backend가 인증 실패와 권한 부족을 구분해 일관된 HTTP Status와 Error Response를 반환하는 기준이다.

Frontend는 이 계약을 기반으로 refresh, login redirect, forbidden page, error message를 처리한다.

---

### [핵심]

Backend Contract:

```text
인증 없음 / token 문제
→ 401 Unauthorized
```

```text
인증됨 / 권한 부족
→ 403 Forbidden
```

Frontend 처리:

```text
401
→ refresh 시도
→ 실패 시 clearAuth
→ login redirect
```

```text
403
→ Auth State 유지
→ forbidden message/page
```

Error Response 후보:

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

권장 Mapping:

| Backend 상황     |       Status | Frontend 처리     |
| ---------------- | -----------: | ----------------- |
| token 없음       |          401 | login redirect    |
| token 만료       |          401 | refresh 시도      |
| token 위조       |          401 | clearAuth         |
| refresh 실패     |          401 | clearAuth + login |
| role 부족        |          403 | forbidden         |
| owner 불일치     |          403 | 권한 없음 메시지  |
| 계정 비활성 정책 | 403 또는 401 | 정책에 따라 처리  |
| validation error |          400 | field error       |
| duplicate email  |          409 | duplicate message |

주의:

- Backend가 401과 403을 혼용하면 Frontend 처리가 어려움
- Login API 실패 401과 token 만료 401은 Frontend에서 context로 구분
- 403을 login redirect로 처리하지 않음
- Error code가 있으면 세밀한 메시지 가능
- 내부 보안 사유를 과도하게 노출하지 않음
- Frontend와 Backend의 response wrapper 구조 통일

---

### [FAQ]

Q. Backend가 403 대신 401을 주면 어떻게 돼?
A. Frontend가 권한 부족을 인증 만료로 오해해 logout이나 refresh를 시도할 수 있다.

Q. 401과 403 계약이 왜 중요해?
A. Frontend가 refresh, login redirect, forbidden page를 정확히 분기하기 위해 필요하다.

Q. role 부족은 401이야 403이야?
A. 인증은 되었지만 권한이 부족한 상황이므로 일반적으로 403이다.

Q. token 만료는 401이야 403이야?
A. token이 유효하지 않은 인증 문제이므로 일반적으로 401이다.

---

# 5. Final Implementation Checklist

## 5.1 Login / Signup Checklist

### [개념]

Login / Signup Checklist는 인증 진입 흐름이 안전하고 일관되게 구현되었는지 확인하는 최종 검수 기준이다.

세부 구현 흐름은 Login / Signup 문서에서 다루고, 이 섹션은 최종 확인 항목만 제공한다.

---

### [핵심]

Checklist:

```md
- [ ] Login API는 publicApi를 사용하는가?
- [ ] Signup API는 publicApi를 사용하는가?
- [ ] Login Request DTO와 Backend 필드명이 일치하는가?
- [ ] Signup Request DTO와 Backend 필드명이 일치하는가?
- [ ] password를 trim하지 않는 기준이 명확한가?
- [ ] password / token console.log가 없는가?
- [ ] submit loading이 있는가?
- [ ] duplicate submit prevention이 있는가?
- [ ] Login Response unwrap 기준이 통일되었는가?
- [ ] accessToken 저장 기준이 있는가?
- [ ] refreshToken 처리 기준이 있는가?
- [ ] user summary 처리 기준이 있는가?
- [ ] 로그인 응답에 user가 없으면 /me 호출 기준이 있는가?
- [ ] 로그인 실패 시 authenticated true가 되지 않는가?
- [ ] 로그인 실패 메시지가 과도하게 상세하지 않은가?
- [ ] 회원가입 성공 후 login redirect 또는 auto login 정책이 명확한가?
- [ ] Client Validation과 Backend Validation 역할이 분리되었는가?
- [ ] field error와 global error mapping이 가능한가?
- [ ] redirect target 검증이 있는가?
```

---

### [실무]

검수 Flow:

```text
Form Submit
→ Request DTO Mapping
→ API Call
→ Response Unwrap
→ Token Handling
→ User State
→ Auth State
→ Redirect
→ Error Handling
```

주의:

- login success 전 authenticated true 금지
- signup auto login 시 Login Flow와 동일하게 처리
- confirmPassword는 Backend 전송 여부 검토
- email duplicate는 Backend 기준
- error object를 그대로 출력하지 않음
- password, token, Authorization Header 로그 금지

---

### [FAQ]

Q. Login / Signup 최종 검수에서 가장 중요한 건 뭐야?
A. Request/Response mapping, token 처리, Auth State 갱신, error handling, redirect가 일관되게 연결되는지 확인하는 것이다.

Q. 로그인 실패 시 user state를 유지해도 돼?
A. 권장하지 않는다. 실패 상황에서는 이전 user state가 남지 않도록 clearAuth 기준을 검토해야 한다.

Q. 회원가입 자동 로그인은 어떻게 검수해?
A. Signup Response가 token과 user를 제공하는지 확인하고 Login Flow와 동일하게 Auth State를 갱신해야 한다.

---

## 5.2 Auth State / Restore Checklist

### [개념]

Auth State / Restore Checklist는 앱 시작, 새로고침, 로그인, 로그아웃, token 만료 상황에서 인증 상태가 안정적으로 유지되는지 확인하는 기준이다.

세부 구현은 Auth State / Auth Restore 문서에서 다루고, 이 섹션은 최종 확인 항목만 제공한다.

---

### [핵심]

Checklist:

```md
- [ ] initialized 상태가 있는가?
- [ ] loading 상태가 있는가?
- [ ] authenticated 상태가 있는가?
- [ ] user summary가 있는가?
- [ ] role naming이 통일되었는가?
- [ ] user null과 비로그인 상태를 구분하는가?
- [ ] token 존재만으로 authenticated true 처리하지 않는가?
- [ ] App Start 시 Auth Restore가 실행되는가?
- [ ] /me API로 인증 상태를 확인하는가?
- [ ] /me 실패 시 clearAuth 하는가?
- [ ] initialized는 finally에서 true 처리되는가?
- [ ] token이 없어도 initialized true가 되는가?
- [ ] AuthProvider가 Route Guard보다 상위에 있는가?
- [ ] StrictMode effect 중복 실행을 고려했는가?
- [ ] role 정보가 없는 동안 UI flicker를 방지하는가?
- [ ] Auth State와 persisted storage 불일치 가능성을 점검했는가?
```

---

### [실무]

검수 Flow:

```text
App Start
→ initialized false
→ check token or cookie
→ call /me
→ success setUser + authenticated true
→ failure clearAuth
→ finally initialized true
→ render routes
```

주의:

- initialized 전 Protected Route redirect 금지
- user null인데 authenticated true 상태 지양
- role naming은 `ROLE_USER`, `ROLE_ADMIN` 등으로 통일
- `/me` 응답에 role 포함 권장
- Auth Restore가 무한 loading에 빠지지 않도록 finally 확인
- Auth State 변경 후 Header / Route / API Client가 같은 기준을 사용해야 함

---

### [FAQ]

Q. Auth State 최종 검수에서 가장 중요한 건 뭐야?
A. initialized, authenticated, user, role을 분리하고 새로고침 복원 시 `/me` 기반으로 상태를 확정하는 것이다.

Q. token이 있으면 바로 authenticated true로 해도 돼?
A. 가능은 하지만 token이 만료되었거나 위조되었을 수 있으므로 `/me` 같은 API로 확인하는 흐름이 더 안전하다.

Q. initialized가 없으면 어떤 문제가 생겨?
A. 새로고침 복원 중 비로그인으로 오판해 login redirect나 UI flicker가 발생할 수 있다.

---

## 5.3 Token / Axios Checklist

### [개념]

Token / Axios Checklist는 Access Token, Refresh Token, Authorization Header, Axios Instance, Interceptor가 일관되게 동작하는지 확인하는 기준이다.

세부 구현은 Token Handling 문서와 Axios Auth Integration 문서에서 다루고, 이 섹션은 최종 확인 항목만 제공한다.

---

### [핵심]

Checklist:

```md
- [ ] publicApi와 authApi가 분리되었는가?
- [ ] baseURL 환경변수 기준이 통일되었는가?
- [ ] Frontend .env에 secret이 없는가?
- [ ] 인증 필요 API는 authApi를 사용하는가?
- [ ] 공개 API는 publicApi를 사용하는가?
- [ ] Authorization Header 형식이 `Bearer <token>`인가?
- [ ] Bearer 중복이 없는가?
- [ ] Bearer undefined가 없는가?
- [ ] Request Interceptor가 1회만 등록되는가?
- [ ] Component 내부에서 interceptor를 등록하지 않는가?
- [ ] Response Interceptor가 Promise.reject를 반환하는가?
- [ ] Login API 401과 token expired 401을 구분하는가?
- [ ] refresh endpoint는 refresh retry 대상에서 제외되는가?
- [ ] `_retry` 플래그가 있는가?
- [ ] refresh 실패 시 clearAuth 하는가?
- [ ] concurrent 401 처리 필요 여부를 검토했는가?
- [ ] response.data.data unwrap 위치가 통일되었는가?
- [ ] Error Normalization 기준이 있는가?
```

---

### [실무]

검수 Flow:

```text
API Function
→ publicApi / authApi 선택
→ Request Interceptor
→ Authorization Header
→ Response Interceptor
→ 401 / 403 분기
→ Refresh Retry
→ Error Propagation
```

주의:

- 인증 API에 publicApi 사용 금지
- 공개 API에 불필요한 token 전송 지양
- refresh API는 publicApi 또는 별도 refreshApi 검토
- interceptor에서 useNavigate 직접 사용 금지
- auth expired event pattern 검토
- Promise chain이 끊기지 않도록 return 확인
- mutation auto retry는 중복 실행 위험 검토

---

### [FAQ]

Q. Axios Auth 최종 검수에서 가장 중요한 건 뭐야?
A. publicApi/authApi 분리, Authorization Header 자동 추가, 401/403 분기, refresh retry, Promise.reject 반환이다.

Q. 인증 API에 publicApi를 쓰면 어떻게 돼?
A. Authorization Header가 누락되어 401이 발생할 수 있다.

Q. interceptor가 여러 번 등록되면?
A. Header 처리, refresh 요청, logout event가 중복 실행될 수 있다.

Q. Response Interceptor에서 Promise.reject를 왜 반환해?
A. 호출부 catch와 finally가 정상 실행되고 화면별 에러 처리가 가능하도록 하기 위해서다.

---

## 5.4 Route Guard / Role UI Checklist

### [개념]

Route Guard / Role UI Checklist는 Protected Route, PublicOnlyRoute, Role Based Route, Forbidden Page, Role Based UI가 Auth State와 정확히 연결되는지 확인하는 기준이다.

세부 구현은 Protected Route / Role Based Route 문서에서 다루고, 이 섹션은 최종 확인 항목만 제공한다.

---

### [핵심]

Checklist:

```md
- [ ] Protected Route가 initialized를 확인하는가?
- [ ] Protected Route가 authenticated를 확인하는가?
- [ ] 비로그인 사용자를 login으로 redirect하는가?
- [ ] previous location 저장 기준이 있는가?
- [ ] redirect target 검증이 있는가?
- [ ] PublicOnlyRoute가 login / signup에 적용되는가?
- [ ] login page를 Protected Route로 감싸지 않았는가?
- [ ] OAuth2 callback route는 guard 예외인가?
- [ ] Role Based Route가 allowedRoles를 확인하는가?
- [ ] ROLE_USER / ROLE_ADMIN naming이 통일되었는가?
- [ ] 권한 없으면 forbidden page로 이동하는가?
- [ ] forbidden page가 RoleRoute 내부에 있지 않은가?
- [ ] Role Based UI가 user null을 안전하게 처리하는가?
- [ ] owner button hiding이 UX용임을 명시했는가?
- [ ] Backend Authorization 필수 기준이 포함되었는가?
```

---

### [실무]

검수 Flow:

```text
Route Access
→ initialized check
→ authenticated check
→ role check
→ owner UX check
→ redirect target check
→ forbidden handling
→ Backend Authorization check
```

주의:

- initialized 전 redirect 금지
- login / signup / callback redirect loop 주의
- RoleRoute가 Backend Authorization을 대체하지 않음
- Forbidden Page는 RoleRoute 밖에 둠
- role naming 불일치 확인
- owner check는 Backend에서 최종 검증
- Header 메뉴 flicker 방지

---

### [FAQ]

Q. Route Guard 최종 검수에서 가장 중요한 건 뭐야?
A. initialized 전 redirect를 막고, authenticated와 role 조건을 분리하며, Backend Authorization이 최종 보안임을 명시하는 것이다.

Q. login page를 Protected Route로 감싸도 돼?
A. 아니다. login page는 비로그인 사용자가 접근해야 하므로 Protected Route로 감싸면 redirect loop가 생길 수 있다.

Q. forbidden page는 어디에 둬야 해?
A. RoleRoute 보호 밖에 두어 권한 없는 사용자도 권한 없음 화면을 볼 수 있게 해야 한다.

---

## 5.5 Logout / Profile / OAuth2 Checklist

### [개념]

Logout / Profile / OAuth2 Checklist는 로그아웃 정리, 사용자 정보 동기화, 소셜 로그인 callback 처리, OAuth2 보안 기준을 최종 확인하는 기준이다.

세부 구현은 Logout / User Profile Fetch 문서와 OAuth2 Frontend Flow 문서에서 다루고, 이 섹션은 최종 확인 항목만 제공한다.

---

### [핵심]

Logout Checklist:

```md
- [ ] logout API 필요 여부가 정리되었는가?
- [ ] accessToken을 제거하는가?
- [ ] refreshToken을 제거하는가?
- [ ] user state를 null 처리하는가?
- [ ] authenticated false 처리하는가?
- [ ] query cache를 정리하는가?
- [ ] persisted auth store를 정리하는가?
- [ ] private UI state를 정리하는가?
- [ ] WebSocket / subscription을 정리하는가?
- [ ] cross tab logout 필요 여부를 검토했는가?
- [ ] logout 후 public route로 replace navigation 하는가?
```

Profile Checklist:

```md
- [ ] /me API와 profile API 역할이 분리되었는가?
- [ ] Auth State에는 최소 user summary만 저장하는가?
- [ ] profile detail은 화면 단위 query로 조회하는가?
- [ ] profile update 후 Auth State 또는 /me cache를 갱신하는가?
- [ ] profile response에 password hash가 없는가?
- [ ] role / status 변경 시 Auth State sync 기준이 있는가?
```

OAuth2 Checklist:

```md
- [ ] OAuth2 시작은 Backend Authorization Endpoint 기준인가?
- [ ] Frontend에 OAuth Client Secret이 없는가?
- [ ] callback route가 존재하는가?
- [ ] callback route가 PublicOnlyRoute / ProtectedRoute에 막히지 않는가?
- [ ] token query 방식이면 URL cleanup을 수행하는가?
- [ ] code 방식이면 Backend exchange API를 호출하는가?
- [ ] cookie 방식이면 /me API로 인증 복원하는가?
- [ ] returnUrl 검증이 있는가?
- [ ] returnUrl 전달 방식이 Backend 정책에 맞는가?
- [ ] OAuth2 error parameter를 처리하는가?
- [ ] 신규 소셜 사용자 onboarding 기준이 있는가?
- [ ] Account Linking / Unlink가 선택 기능으로 분리되었는가?
```

---

### [실무]

검수 Flow:

```text
Logout
→ Clear Auth
→ Clear Cache
→ Clear Private State
→ Redirect
```

```text
Profile Update
→ Update API
→ Invalidate myProfile
→ Invalidate /me
→ Update Auth State
```

```text
OAuth2 Callback
→ read result
→ token / code / cookie handling
→ getMe
→ setAuth
→ cleanup URL
→ safe redirect
```

주의:

- logout 시 token만 삭제하면 부족
- query cache에 이전 사용자 데이터가 남을 수 있음
- profile update 후 Header와 MyPage 불일치 주의
- OAuth2 callback에서 Auth State 갱신 전 navigate 금지
- OAuth2 returnUrl 외부 URL 금지
- OAuth2 Client Secret Frontend 저장 금지
- callback missing parameter는 fail closed 처리

---

### [FAQ]

Q. Logout 최종 검수에서 가장 중요한 건 뭐야?
A. token뿐 아니라 user state, authenticated, query cache, persisted store, private state, WebSocket까지 정리하는 것이다.

Q. Profile 수정 후 Header가 안 바뀌면?
A. profile cache만 갱신하고 Auth State 또는 `/me` cache를 갱신하지 않았을 가능성이 있다.

Q. OAuth2 최종 검수에서 가장 중요한 건 뭐야?
A. Frontend secret 금지, callback route 예외 처리, token/code/cookie 방식 명확화, `/me` 기반 Auth State 갱신, URL cleanup이다.

Q. Account Linking은 최종 완료 조건이야?
A. 아니다. 계정 설정 기능이 있는 서비스에서 선택적으로 적용한다.

---

# 6. Error-to-Document Retrieval Map

## 6.1 Scenario Based Retrieval Map

### [개념]

Error-to-Document Retrieval Map은 인증 문제 상황별로 어떤 Part를 우선 검색해야 하는지 정의하는 RAG Retrieval 색인이다.

Part11 Index / Cross Reference 문서를 별도로 작성하지 않는다면 이 섹션을 Part10에 유지한다.

Part11을 작성한다면 이 섹션은 Part11로 이동하고, Part10에는 “상세 Index는 Part11 참조”만 남기는 것이 적절하다.

---

### [핵심]

문제별 우선 참조:

| 문제 상황                         | 우선 참조                                          |
| --------------------------------- | -------------------------------------------------- |
| 로그인 요청 / 응답 문제           | Part02 Login / Signup                              |
| 로그인 후 user null               | Part03 Auth State, Part07 Profile                  |
| 새로고침 후 login 이동            | Part03 Auth Restore, Part06 Protected Route        |
| token 저장 / 만료 문제            | Part04 Token Handling                              |
| Authorization Header 누락         | Part05 Axios, Part09 401                           |
| refresh loop                      | Part04 Token, Part05 Axios, Part09 Troubleshooting |
| Protected Route loop              | Part06 Route Guard, Part09 Troubleshooting         |
| 관리자 메뉴 안 보임               | Part03 Role, Part06 Role UI                        |
| 관리자 API 403                    | Part06 Role Route, Part09 403                      |
| logout 후 user 남음               | Part07 Logout Cleanup                              |
| OAuth2 callback 실패              | Part08 OAuth2                                      |
| OAuth2 login success user missing | Part08 OAuth2, Part09 Troubleshooting              |
| token 보안 검수                   | Part04 Token, Part10 Security                      |
| Frontend secret 검수              | Part08 OAuth2, Part10 Security                     |

---

### [실무]

Agent Retrieval Flow:

```text
User reports auth problem
→ Extract symptom keyword
→ Determine status code if API issue
→ Determine route / state if UI issue
→ Search matching Part
→ Apply checklist
→ Return fix steps
```

검색 키워드 예:

```text
401 localStorage token exists
→ Part05 Authorization Header Missing
→ Part09 Token Missing 401
```

```text
logout nickname remains
→ Part07 Logout State Remains
→ Part10 Logout Checklist
```

```text
OAuth2 callback login loop
→ Part08 OAuth2 Redirect Loop
→ Part09 OAuth2 Troubleshooting
```

주의:

- API status code가 있으면 401 / 403 먼저 분기
- 화면 문제면 Auth State / Route Guard 먼저 확인
- token 문제면 Header와 Storage를 분리
- OAuth2 문제는 callback route와 Backend redirect를 함께 확인
- 보안 검수는 Part10 최종 기준을 적용
- Part11 작성 시 이 map은 Part11로 이동 가능

---

### [FAQ]

Q. 인증 문제 발생 시 어떤 문서부터 봐?
A. status code가 있으면 Part09를 먼저 보고, login/token/route/OAuth2 등 원인별 Part로 이동한다.

Q. Authorization Header 누락 문제는 어디를 봐?
A. Part05 Axios Auth Integration과 Part09 Token Missing 401을 우선 참조한다.

Q. logout 후 이전 사용자 정보가 남는 문제는 어디를 봐?
A. Part07 Logout Cleanup과 Part10 Logout Checklist를 참조한다.

Q. OAuth2 callback 문제는 어디를 봐?
A. Part08 OAuth2 Frontend Flow와 Part09 OAuth2 Auth Troubleshooting을 참조한다.

Q. Part11을 만들면 이 섹션은 어떻게 해?
A. Part11로 이동하고 Part10에는 “상세 Index는 Part11 참조” 수준으로 축소하는 것이 좋다.

---

# 7. Final Document Linkage Check

## 7.1 Cross Document Consistency

### [개념]

Cross Document Consistency는 Authentication Frontend Flow 전체 Part가 같은 용어, 같은 책임 분리, 같은 status handling, 같은 보안 기준을 사용하는지 확인하는 검수 절차다.

---

### [핵심]

통일해야 할 용어:

- Authentication
- Authorization
- Access Token
- Refresh Token
- Authorization Header
- Bearer Token
- Auth State
- initialized
- authenticated
- user
- role
- ROLE_USER
- ROLE_ADMIN
- Protected Route
- PublicOnlyRoute
- Role Based Route
- Role Based UI
- 401 Unauthorized
- 403 Forbidden
- Backend Authorization

통일해야 할 기준:

- 401은 인증 문제
- 403은 권한 문제
- 403에서 기본 logout 금지
- Frontend role check는 UX용
- Backend Authorization은 필수
- token log 금지
- Frontend secret 금지
- `/me`는 auth restore와 user summary 확인용
- logout은 token + state + cache 정리
- OAuth2 callback은 guard 예외 가능
- response unwrap은 API 함수에서 통일
- Account Linking은 선택 기능

---

### [실무]

최종 연결 구조:

```text
Part01
→ 전체 책임과 범위 정의
```

```text
Part02
→ Login / Signup 진입점
```

```text
Part03
→ Auth State / Auth Restore
```

```text
Part04
→ Token Handling / Storage
```

```text
Part05
→ Axios API Client / Interceptor
```

```text
Part06
→ Route Guard / Role UI
```

```text
Part07
→ Logout / Profile / Cache Cleanup
```

```text
Part08
→ OAuth2 / Callback
```

```text
Part09
→ 401 / 403 / Troubleshooting
```

```text
Part10
→ Security / Final Checklist / Retrieval Optimization
```

검수 기준:

```text
용어 통일
→ 책임 분리 통일
→ status code 처리 통일
→ token 보안 통일
→ route guard 기준 통일
→ FAQ 중복 검색성 확보
```

---

### [FAQ]

Q. 전체 문서에서 가장 중요한 일관성 기준은?
A. Frontend는 UX와 요청 흐름 담당이고 Backend Authorization이 최종 보안이라는 기준이다.

Q. 401 / 403 기준은 모든 Part에서 같아야 해?
A. 그렇다. 401은 인증 문제, 403은 권한 문제로 일관되게 처리해야 한다.

Q. role naming은 왜 통일해야 해?
A. `ROLE_ADMIN`과 `ADMIN`을 혼용하면 Role Based UI와 Role Based Route가 실패할 수 있기 때문이다.

Q. response unwrap 기준은 어디서 통일해?
A. API Function Layer에서 `response.data.data` 같은 wrapper unwrap 기준을 통일하는 것이 좋다.

---

# 8. Final Quality Checklist

## 8.1 RAG Document Quality Checklist

### [개념]

RAG Document Quality Checklist는 Authentication Frontend Flow 문서가 사람용 설명서가 아니라 Agent Retrieval과 Code Generation Support에 최적화되었는지 확인하는 최종 기준이다.

---

### [핵심]

Quality Checklist:

```md
- [ ] 문서 목적이 Agent Retrieval에 맞는가?
- [ ] 사람용 장문 설명보다 검색 가능한 키워드가 충분한가?
- [ ] [개념], [핵심], [실무], [FAQ] 구조가 유지되는가?
- [ ] 각 Section이 독립 chunk로 검색 가능한가?
- [ ] 하나의 chunk에 하나의 주제가 유지되는가?
- [ ] code example이 짧고 직접적인가?
- [ ] flow diagram이 text 기반으로 포함되는가?
- [ ] FAQ가 실제 검색 질문 형태인가?
- [ ] Retrieval Queries가 충분한가?
- [ ] 용어가 일관되는가?
- [ ] 401 / 403 기준이 일관되는가?
- [ ] Backend Authorization Required가 반복 명시되는가?
- [ ] Frontend secret 금지가 포함되는가?
- [ ] token log 금지가 포함되는가?
- [ ] OAuth2 callback security가 포함되는가?
- [ ] logout cleanup이 cache까지 포함하는가?
- [ ] Troubleshooting이 증상 기반으로 구성되는가?
- [ ] 오타와 용어 혼용이 최소화되었는가?
```

---

### [실무]

RAG 최적화 기준:

```text
검색 질문
→ 관련 keyword hit
→ 독립 chunk 이해 가능
→ 예제 코드 확인
→ 주의사항 확인
→ FAQ로 결론 확인
```

좋은 FAQ 예:

```text
Q. localStorage에 token이 있는데 401이 나?
A. Network 탭에서 Authorization Header에 실제로 token이 포함되었는지 확인해야 한다.
```

나쁜 FAQ 예:

```text
Q. 인증은 중요한가?
A. 중요하다.
```

주의:

- 추상 질문보다 실제 에러 질문 중심
- `token`, `401`, `Authorization Header`, `Bearer`, `authApi` 같은 키워드 포함
- `403`, `ROLE_ADMIN`, `forbidden`, `Backend Authorization` 같이 함께 검색될 단어 포함
- OAuth2는 `callback`, `returnUrl`, `code`, `cookie`, `withCredentials` 키워드 포함
- logout은 `cache`, `persisted store`, `WebSocket`, `private state` 키워드 포함

---

### [FAQ]

Q. RAG 문서 품질에서 가장 중요한 것은?
A. Agent가 실제 문제 상황을 검색했을 때 정확한 chunk를 찾고 바로 구현 또는 검수에 활용할 수 있는 것이다.

Q. FAQ는 왜 많이 넣어?
A. 사용자의 실제 질문 형태가 Retrieval Query와 유사하기 때문에 검색 적중률을 높인다.

Q. code example은 길수록 좋아?
A. 아니다. RAG 문서에서는 짧고 직접적인 예제가 검색성과 재사용성에 유리하다.

Q. Troubleshooting은 왜 증상 기반으로 써야 해?
A. 실제 Agent 요청은 “401이 나요”, “로그아웃했는데 닉네임이 남아요”처럼 증상 기반으로 들어오기 때문이다.

---

# 9. Final Completion Status

## 9.1 Authentication Frontend Flow Completion

### [개념]

Authentication Frontend Flow Part01부터 Part10까지 작성되면 Frontend 인증 흐름 문서의 Foundation 범위는 완료 상태로 볼 수 있다.

Part11 Index / Cross Reference 문서는 필수 완료 조건이 아니라 RAG 검색 보강용 선택 문서다.

---

### [핵심]

완료 구조:

```text
Part01 Overview / Responsibility / Scope
Part02 Login Flow / Signup Flow
Part03 Auth State / Auth Restore
Part04 Token Handling / Token Storage
Part05 Axios Auth Integration
Part06 Protected Route / Role Based Route
Part07 Logout / User Profile Fetch
Part08 OAuth2 Frontend Flow
Part09 401 / 403 / Troubleshooting
Part10 Security / Checklist / Retrieval Optimization
```

완료 기준:

- Login Flow 포함
- Signup Flow 포함
- Auth State 포함
- Auth Restore 포함
- Token Handling 포함
- Axios Interceptor 포함
- Protected Route 포함
- Role Based Route 포함
- Logout Cleanup 포함
- OAuth2 Callback 포함
- 401 / 403 Troubleshooting 포함
- Security Final Checklist 포함
- Retrieval Queries 포함

선택 확장:

```text
Part11 Index / Cross Reference / Scenario Retrieval Map
→ RAG 테스트 후 필요 시 추가
→ Foundation 완료 필수 조건 아님
```

---

### [실무]

Project Progress 반영 기준:

```text
Authentication Frontend Flow
→ Part10 완료 시 Foundation 범위 Completed 로 이동 가능
```

연계 문서:

```text
React Router
→ Protected Route / PublicOnlyRoute

State Management
→ Auth State / Auth Store

Data Fetching & REST API Integration
→ Axios authApi / publicApi

Form Handling & Validation
→ Login Form / Signup Form

Error Handling & Loading UX
→ Auth Loading / 401 / 403

Backend Security
→ JWT / OAuth2 / Authorization
```

주의:

- 이 문서는 Backend Security 구현 문서가 아님
- 이 문서는 Frontend 인증 흐름 Foundation 문서임
- Security 심화, Permission Matrix, MFA, Passkey, SSO, CSRF 심화는 별도 문서 범위
- 실제 RAG 테스트 후 부족한 검색 query는 Retrieval Queries에 추가 가능
- Part11은 필요할 때만 추가

---

### [FAQ]

Q. Authentication Frontend Flow는 Part10까지면 완료야?
A. Foundation 범위에서는 완료로 볼 수 있다. RAG 테스트 후 필요하면 Part11 Index 문서를 추가할 수 있다.

Q. Project Progress에서 Completed로 옮겨도 돼?
A. Part10까지 작성했다면 Authentication Frontend Flow는 Completed로 이동 가능하다.

Q. 추가로 반드시 필요한 문서가 있어?
A. 필수는 아니다. 다만 실제 검색 테스트에서 누락이 있으면 Index / Cross Reference 문서를 추가할 수 있다.

Q. Part11은 완료 조건이야?
A. 아니다. Part11은 RAG 검색 보강용 선택 문서이고 Part10 완료 시 Foundation 범위는 완료로 볼 수 있다.

Q. 이 문서는 Backend Security 문서야?
A. 아니다. Frontend 인증 흐름, token 사용, route guard, OAuth2 callback, troubleshooting에 집중하는 Frontend Foundation 문서다.

---

# Retrieval Queries

### [FAQ]

Q. Frontend Auth Security의 핵심은 뭐야?
A. 민감정보 노출을 줄이고 Auth State, token 전달, Route Guard, 오류 처리를 안전하게 구성하되 최종 보안은 Backend가 담당한다는 기준이다.

Q. Frontend에서 Protected Route를 만들면 보안이 완성돼?
A. 아니다. Protected Route는 UX Guard이고 실제 API 접근 제어는 Backend Authorization이 수행해야 한다.

Q. 관리자 버튼을 숨기면 관리자 기능이 안전해져?
A. 아니다. 버튼 숨김은 UX용이고 관리자 API는 Backend에서 ROLE_ADMIN 검증을 해야 한다.

Q. Part10은 구현 상세 문서야?
A. 아니다. Part02부터 Part09까지의 구현 내용을 최종 검수하고 검색 가능하게 묶는 보안 / 체크리스트 / Retrieval 최적화 문서다.

Q. token을 console.log로 찍어도 돼?
A. 안 된다. token은 인증에 사용되는 민감정보이므로 로그에 남기지 않는 것이 원칙이다.

Q. password를 디버깅하려면 어떻게 해?
A. 값 자체를 출력하지 말고 입력 여부, validation 결과, status code 정도만 확인한다.

Q. Authorization Header를 에러 로그에 남겨도 돼?
A. 안 된다. Authorization Header에는 token이 포함될 수 있으므로 로그 전송 전에 제거해야 한다.

Q. Frontend .env에 OAuth secret을 넣어도 돼?
A. 안 된다. Frontend 환경변수는 빌드 결과에 노출될 수 있으므로 secret을 넣으면 안 된다.

Q. Frontend .env는 안전한 비밀 저장소야?
A. 아니다. Frontend 번들에 포함될 수 있으므로 공개되어도 되는 값만 넣어야 한다.

Q. API 서버 주소는 .env에 넣어도 돼?
A. 가능하다. API base URL처럼 공개되어도 되는 값은 넣을 수 있다.

Q. OAuth2 callback에서 token을 URL로 받으면 어떻게 해?
A. 즉시 저장 또는 처리한 뒤 replace navigation으로 URL에서 token을 제거하는 것이 좋다.

Q. URL에서 token을 제거하지 않으면?
A. 브라우저 history, screenshot, log, 공유 URL에 token이 노출될 수 있다.

Q. refreshToken도 URL로 받아도 돼?
A. 권장하지 않는다. refreshToken은 더 민감하므로 HttpOnly Cookie나 one-time code 방식을 우선 검토하는 것이 좋다.

Q. token은 localStorage에 저장하면 돼?
A. 가능은 하지만 XSS 위험이 있다. 프로젝트 보안 요구사항에 따라 memory, sessionStorage, HttpOnly Cookie 등을 검토해야 한다.

Q. sessionStorage는 안전해?
A. localStorage보다 유지 범위는 좁지만 JavaScript 접근이 가능하므로 XSS 위험은 여전히 있다.

Q. HttpOnly Cookie가 무조건 정답이야?
A. 항상 정답은 아니다. JS 접근 차단 장점이 있지만 CSRF, SameSite, Backend 설정 등 함께 고려해야 한다.

Q. refreshToken은 어디에 저장하는 게 좋아?
A. 보안 요구가 있다면 HttpOnly Cookie를 우선 검토하고 Web Storage 저장은 신중히 결정해야 한다.

Q. localStorage에 token을 저장하면 보안상 위험해?
A. XSS가 발생하면 JavaScript로 token을 읽을 수 있으므로 위험할 수 있다.

Q. HttpOnly Cookie를 쓰면 XSS가 완전히 해결돼?
A. token 직접 접근은 줄일 수 있지만 XSS 자체와 CSRF 문제는 별도로 고려해야 한다.

Q. Cookie Auth에서도 CSRF를 고려해야 해?
A. 해야 한다. Cookie는 자동 전송될 수 있으므로 SameSite, CSRF token, Backend 방어 정책을 함께 고려해야 한다.

Q. withCredentials는 언제 필요해?
A. cross-origin 요청에서 cookie를 포함해야 할 때 필요할 수 있으며 Backend CORS 설정과 함께 맞춰야 한다.

Q. Frontend에서 ROLE_ADMIN을 확인하면 관리자 API가 안전해져?
A. 아니다. Frontend role check는 화면 접근 UX용이고 관리자 API는 Backend에서 반드시 권한 검증해야 한다.

Q. 삭제 버튼을 작성자에게만 보여주면 충분해?
A. 아니다. 버튼 표시 제어는 UX용이고 실제 삭제 API는 Backend에서 작성자 여부를 검증해야 한다.

Q. Backend Authorization Required는 왜 반복해서 써야 해?
A. Agent가 Frontend UI 제어를 실제 보안으로 착각하지 않도록 하기 위해 반드시 반복 명시해야 한다.

Q. 401과 403 계약이 왜 중요해?
A. Frontend가 refresh, login redirect, forbidden page를 정확히 분기하기 위해 필요하다.

Q. role 부족은 401이야 403이야?
A. 인증은 되었지만 권한이 부족한 상황이므로 일반적으로 403이다.

Q. token 만료는 401이야 403이야?
A. token이 유효하지 않은 인증 문제이므로 일반적으로 401이다.

Q. Login / Signup 최종 검수에서 가장 중요한 건 뭐야?
A. Request/Response mapping, token 처리, Auth State 갱신, error handling, redirect가 일관되게 연결되는지 확인하는 것이다.

Q. Auth State 최종 검수에서 가장 중요한 건 뭐야?
A. initialized, authenticated, user, role을 분리하고 새로고침 복원 시 `/me` 기반으로 상태를 확정하는 것이다.

Q. Axios Auth 최종 검수에서 가장 중요한 건 뭐야?
A. publicApi/authApi 분리, Authorization Header 자동 추가, 401/403 분기, refresh retry, Promise.reject 반환이다.

Q. Route Guard 최종 검수에서 가장 중요한 건 뭐야?
A. initialized 전 redirect를 막고, authenticated와 role 조건을 분리하며, Backend Authorization이 최종 보안임을 명시하는 것이다.

Q. Logout 최종 검수에서 가장 중요한 건 뭐야?
A. token뿐 아니라 user state, authenticated, query cache, persisted store, private state, WebSocket까지 정리하는 것이다.

Q. Profile 수정 후 Header가 안 바뀌면?
A. profile cache만 갱신하고 Auth State 또는 `/me` cache를 갱신하지 않았을 가능성이 있다.

Q. OAuth2 최종 검수에서 가장 중요한 건 뭐야?
A. Frontend secret 금지, callback route 예외 처리, token/code/cookie 방식 명확화, `/me` 기반 Auth State 갱신, URL cleanup이다.

Q. Account Linking은 최종 완료 조건이야?
A. 아니다. 계정 설정 기능이 있는 서비스에서 선택적으로 적용한다.

Q. 인증 문제 발생 시 어떤 문서부터 봐?
A. status code가 있으면 Part09를 먼저 보고, login/token/route/OAuth2 등 원인별 Part로 이동한다.

Q. Authorization Header 누락 문제는 어디를 봐?
A. Part05 Axios Auth Integration과 Part09 Token Missing 401을 우선 참조한다.

Q. logout 후 이전 사용자 정보가 남는 문제는 어디를 봐?
A. Part07 Logout Cleanup과 Part10 Logout Checklist를 참조한다.

Q. OAuth2 callback 문제는 어디를 봐?
A. Part08 OAuth2 Frontend Flow와 Part09 OAuth2 Auth Troubleshooting을 참조한다.

Q. Part11을 만들면 Retrieval Map은 어떻게 해?
A. Part10의 Scenario Based Retrieval Map을 Part11로 이동하고 Part10에는 Part11 참조 문장만 남기는 것이 좋다.

Q. 전체 문서에서 가장 중요한 일관성 기준은?
A. Frontend는 UX와 요청 흐름 담당이고 Backend Authorization이 최종 보안이라는 기준이다.

Q. 401 / 403 기준은 모든 Part에서 같아야 해?
A. 그렇다. 401은 인증 문제, 403은 권한 문제로 일관되게 처리해야 한다.

Q. role naming은 왜 통일해야 해?
A. `ROLE_ADMIN`과 `ADMIN`을 혼용하면 Role Based UI와 Role Based Route가 실패할 수 있기 때문이다.

Q. RAG 문서 품질에서 가장 중요한 것은?
A. Agent가 실제 문제 상황을 검색했을 때 정확한 chunk를 찾고 바로 구현 또는 검수에 활용할 수 있는 것이다.

Q. FAQ는 왜 많이 넣어?
A. 사용자의 실제 질문 형태가 Retrieval Query와 유사하기 때문에 검색 적중률을 높인다.

Q. Troubleshooting은 왜 증상 기반으로 써야 해?
A. 실제 Agent 요청은 “401이 나요”, “로그아웃했는데 닉네임이 남아요”처럼 증상 기반으로 들어오기 때문이다.

Q. Authentication Frontend Flow는 Part10까지면 완료야?
A. Foundation 범위에서는 완료로 볼 수 있다. RAG 테스트 후 필요하면 Part11 Index 문서를 추가할 수 있다.

Q. Project Progress에서 Completed로 옮겨도 돼?
A. Part10까지 작성했다면 Authentication Frontend Flow는 Completed로 이동 가능하다.

Q. Part11은 완료 조건이야?
A. 아니다. Part11은 RAG 검색 보강용 선택 문서이고 Part10 완료 시 Foundation 범위는 완료로 볼 수 있다.

Q. 이 문서는 Backend Security 문서야?
A. 아니다. Frontend 인증 흐름, token 사용, route guard, OAuth2 callback, troubleshooting에 집중하는 Frontend Foundation 문서다.
