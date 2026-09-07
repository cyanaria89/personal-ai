# Frontend Authentication Architecture Domain Rules

---

# 1. Domain Purpose

## 1.1 Frontend Authentication Architecture Domain 목적

### [개념]

Frontend Authentication Architecture Domain 문서는 Frontend Agent / Next.js Agent / Review Agent / Architecture Review Agent / Security Review Agent용 RAG 문서 제작 규칙이다.

Frontend Authentication Architecture는 사용자의 로그인 상태, 세션 유지, 토큰 갱신, 보호 라우트, 권한 UI, 로그아웃, 인증 만료, OAuth Callback, 서버 인증 검증, 클라이언트 캐시 정리를 안정적으로 설계하는 영역이다.

목적:

- 프론트엔드 인증 구조 설계 지원
- 로그인 / 로그아웃 / 세션 확인 Flow 지원
- Access Token / Refresh Token / Cookie / Session 구조 판단 지원
- HttpOnly Cookie 기반 인증 구조 지원
- Bearer Token 기반 인증 구조 지원
- Current User / Me Query 설계 지원
- Protected Route / Auth Guard 설계 지원
- Role / Permission UI 처리 지원
- 401 / 403 처리 기준 제공
- Token Refresh / Session Expiration 처리 지원
- Next.js App Router 인증 구조 지원
- Server Action / Route Handler 인증 검증 기준 제공
- 보안 리뷰 및 코드 리뷰 지원

---

### [핵심]

우선순위:

1. Authentication vs Authorization
2. Session Model
3. Token Model
4. Cookie-based Authentication
5. Bearer Token Authentication
6. Current User Query
7. Auth State Management
8. Protected Route
9. Auth Guard
10. Login Flow
11. Logout Flow
12. Token Refresh Flow
13. Session Expiration
14. OAuth Callback Flow
15. Role / Permission UI
16. Server-side Authorization
17. Cache Cleanup
18. Next.js App Router Auth
19. Security Review
20. Troubleshooting

---

### [실무]

2026 실무 기준:

- React / TypeScript / Next.js App Router 기준 예제 우선
- 인증 상태는 서버 세션 또는 서버 검증 결과를 기준으로 판단
- 클라이언트 Auth State는 UX 표시용으로 취급
- 실제 권한 검증은 API / Server Action / Route Handler / Backend에서 수행
- Token 저장 위치는 XSS / CSRF / UX / Backend 구조를 함께 고려
- Refresh Token은 HttpOnly Cookie 우선 검토
- Access Token은 짧은 만료 시간과 갱신 전략을 함께 설계
- Current User Query를 인증 상태의 기준점으로 사용
- Logout 시 사용자별 Query Cache / Client State / Persistent Cache 정리
- 401과 403은 명확히 구분
- OAuth redirect / callback / state / returnUrl 검증 포함
- Next.js App Router에서는 Server Component / Client Component / Middleware / Server Action 경계를 명확히 설명
- Agent가 인증 구조와 코드 리뷰에 바로 사용할 수 있는 판단 기준 포함

---

### [FAQ]

Q. Frontend Authentication Architecture 문서는 무엇을 위한 문서인가?

A.
Agent가 프론트엔드 프로젝트에서 로그인, 세션 확인, 토큰 갱신, 보호 라우트, 권한 UI, 로그아웃, 인증 만료 처리 구조를 설계하고 리뷰하도록 돕는 RAG 문서 제작 규칙이다.

Q. 프론트엔드 인증 구조에서 가장 중요한 것은?

A.
클라이언트 상태만 믿지 않고 서버 검증을 기준으로 인증 상태와 권한을 판단하는 것이다.

Q. 인증과 권한은 같은가?

A.
아니다. 인증은 사용자가 누구인지 확인하는 것이고, 권한은 그 사용자가 어떤 작업을 할 수 있는지 확인하는 것이다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

Frontend Authentication Architecture Domain은 브라우저 인증 상태, 세션 유지, 토큰 저장, 보호 라우트, 권한 UI, 서버 검증 경계, 인증 에러 처리를 포함한다.

---

### [핵심]

포함 범위:

- Authentication
- Authorization
- Session
- Access Token
- Refresh Token
- JWT
- Cookie Authentication
- HttpOnly Cookie
- Secure Cookie
- SameSite Cookie
- Bearer Token
- LocalStorage Token
- SessionStorage Token
- Memory Token
- Current User
- Me Query
- Auth Provider
- Auth Context
- Auth Store
- Protected Route
- Auth Guard
- Route Guard
- Permission Guard
- Role-based UI
- Permission-based UI
- Login Flow
- Logout Flow
- Signup Flow
- Password Reset Flow
- Email Verification Flow
- OAuth Login
- OAuth Callback
- Redirect URL
- Return URL
- Token Refresh
- Silent Refresh
- Session Expiration
- 401 Handling
- 403 Handling
- Multi-tab Logout
- Cache Cleanup
- Query Cache Clear
- Next.js App Router Auth
- Server Component Auth
- Client Component Auth
- Middleware / Proxy Auth
- Server Action Auth
- Route Handler Auth
- CSRF
- XSS
- CORS
- Security Review
- Auth Testing

---

### [실무]

제외 범위:

- OAuth2 / OIDC 프로토콜 심화 전체
- Backend Security 심화 전체
- Password Hashing 구현 심화
- Session Store 구현 심화
- Identity Provider 운영 심화
- MFA 세부 구현 심화
- SSO 조직 정책 심화
- Cryptography 심화
- Penetration Testing 심화
- 모바일 네이티브 인증 심화
- Kubernetes / Infra 보안 심화

단, 프론트엔드 인증 구조 판단에 필요한 수준의 OAuth Callback, Token, Cookie, CSRF, XSS, Server Authorization, Next.js 보안 지식은 포함 가능하다.

---

### [FAQ]

Q. OAuth2 심화도 포함해야 하나?

A.
심화는 제외한다. 단, 프론트엔드에서 필요한 redirect, callback, state, returnUrl, token 처리 기준은 포함한다.

Q. Backend 인증 구현도 포함하나?

A.
심화는 제외한다. 하지만 프론트엔드가 서버 인증 검증과 어떻게 연결되는지는 포함해야 한다.

Q. Frontend Security 문서와 중복되지 않나?

A.
중복을 최소화한다. 이 문서는 인증 흐름과 상태 관리 구조에 집중하고, XSS / CSRF / Token 보안은 인증 구조 관점에서 연결한다.

---

# 3. Required Section Rules

## 3.1 문서 Section 구조

### [개념]

모든 Frontend Authentication Architecture RAG 문서는 MASTER_RAG_RULES의 기본 Section 구조를 따른다.

---

### [핵심]

필수 Section:

- `[개념]`
- `[핵심]`
- `[실무]`
- `[FAQ]`

강력 권장 Section:

- `[Flow]`
- `[예제]`
- `[주의]`
- `[Best Practice]`
- `[Troubleshooting]`
- `[Checklist]`
- `[Comparison]`

---

### [실무]

Frontend Authentication Architecture 문서는 상태 전이와 보안 경계가 중요하므로 아래 Section을 적극 사용한다.

- `[Flow]`: Login → Session Issue → Current User Fetch → Protected UI → Refresh → Logout
- `[Comparison]`: Cookie Auth vs Bearer Token Auth, 401 vs 403
- `[Best Practice]`: Current User Query, Server Authorization, Logout Cache Cleanup
- `[Troubleshooting]`: 새로고침 시 로그인 풀림, 무한 refresh, 이전 사용자 데이터 노출
- `[Checklist]`: Auth Architecture 코드 리뷰

---

### [FAQ]

Q. 인증 문서에 Flow가 중요한 이유는?

A.
인증은 로그인, 세션 확인, 갱신, 만료, 로그아웃, 캐시 정리가 연결된 상태 전이이므로 Flow가 있어야 한다.

Q. `[FAQ]` 대신 `[면접]` 섹션을 써도 되나?

A.
안 된다. MASTER_RAG_RULES에 따라 반드시 `[FAQ]`를 사용한다.

---

# 4. Authentication Core Concept Rules

## 4.1 인증 기본 개념

### [개념]

Authentication은 사용자가 누구인지 확인하는 과정이다.

Authorization은 인증된 사용자가 특정 페이지, 기능, 데이터, API, Server Action을 사용할 수 있는지 판단하는 과정이다.

---

### [핵심]

핵심 용어:

- Authentication
- Authorization
- Identity
- Principal
- Session
- Credential
- Access Token
- Refresh Token
- JWT
- Cookie
- Current User
- Permission
- Role
- Scope
- Claim
- Auth Guard
- Protected Resource

기본 Flow:

```text
사용자 로그인
→ 서버 인증 성공
→ Session 또는 Token 발급
→ 프론트엔드 Current User 확인
→ 보호 UI 렌더링
→ API 요청 시 인증 정보 포함
→ 만료 시 갱신 또는 로그아웃
```

---

### [실무]

작성 기준:

- “로그인 여부”와 “권한 여부”를 분리
- 인증 상태는 서버 검증 또는 current user API 기준
- JWT payload decode만으로 보안 판단 금지
- 클라이언트 Auth Store는 UX 최적화용
- API 권한 검증은 서버에서 수행
- 권한별 UI 숨김은 보안이 아니라 UX
- session expiration과 refresh 실패 상태 처리
- 로그인 상태 loading / authenticated / unauthenticated / expired 구분
- 인증 관련 오류는 안전한 메시지로 표시
- 로그아웃 시 인증 정보와 사용자별 cache 정리

---

### [FAQ]

Q. Authentication과 Authorization 차이는?

A.
Authentication은 사용자가 누구인지 확인하는 것이고, Authorization은 그 사용자가 특정 작업을 할 권한이 있는지 확인하는 것이다.

Q. JWT payload를 decode하면 로그인 상태를 믿어도 되나?

A.
UI 표시에는 참고할 수 있지만 보안 판단은 서버에서 서명, 만료, 권한을 검증해야 한다.

Q. Auth Store에 user가 있으면 로그인된 것인가?

A.
UX상 로그인 상태처럼 보일 수 있지만 실제 기준은 서버 세션 또는 current user 검증 결과여야 한다.

---

# 5. Session Model Rules

## 5.1 Session 기반 인증 모델

### [개념]

Session 기반 인증은 서버가 사용자 세션을 관리하고 브라우저는 세션 식별 정보를 Cookie 등으로 보관하는 구조이다.

프론트엔드는 세션 내용을 직접 알기보다 current user API를 통해 로그인 상태를 확인한다.

---

### [핵심]

필수 포함:

- Server Session
- Session ID
- Session Cookie
- HttpOnly Cookie
- Current User API
- Session Expiration
- Session Renewal
- Logout
- CSRF
- SameSite
- Secure
- Session Store

Session Flow:

```text
Login
→ Server creates session
→ Browser receives HttpOnly session cookie
→ Frontend calls /me
→ Server validates session
→ Frontend renders authenticated UI
```

---

### [실무]

작성 기준:

- 세션 쿠키는 HttpOnly / Secure / SameSite 검토
- current user API로 인증 상태 확인
- 프론트엔드는 session id를 직접 읽지 않음
- Cookie 기반 mutation은 CSRF 방어 검토
- 세션 만료 시 401 처리
- 로그아웃 시 서버 세션 무효화
- 로그아웃 후 client cache 정리
- 로그인 직후 current user query 갱신
- 다중 탭 로그아웃 동기화 검토
- public cache에 사용자별 응답 저장 금지

주의:

- HttpOnly Cookie는 JavaScript에서 읽을 수 없음
- current user loading 상태 설계 필요
- SameSite 설정은 OAuth / 외부 redirect에 영향 가능
- CSRF와 CORS를 혼동하지 않기
- 서버 세션 만료와 클라이언트 상태 불일치 가능

---

### [FAQ]

Q. Session 기반 인증에서 프론트엔드는 로그인 상태를 어떻게 아나?

A.
HttpOnly Cookie를 직접 읽지 않고 current user API를 호출해 서버가 세션을 검증한 결과로 판단한다.

Q. HttpOnly Cookie를 쓰면 token 탈취 걱정이 없나?

A.
JavaScript로 직접 읽기 어렵지만 XSS 자체와 CSRF 위험은 여전히 관리해야 한다.

Q. Session 기반 인증에서 CSRF가 중요한 이유는?

A.
브라우저가 Cookie를 자동 전송하기 때문에 공격자가 사용자의 인증 상태를 악용한 요청을 만들 수 있다.

---

# 6. Token Model Rules

## 6.1 Token 기반 인증 모델

### [개념]

Token 기반 인증은 서버가 Access Token과 Refresh Token을 발급하고, 클라이언트가 API 요청에 인증 정보를 포함하는 구조이다.

Access Token은 짧게 유지하고, Refresh Token은 더 안전한 저장소와 갱신 정책을 사용해야 한다.

---

### [핵심]

필수 포함:

- Access Token
- Refresh Token
- JWT
- Bearer Token
- Token Expiration
- Token Refresh
- Token Rotation
- Refresh Failure
- Token Storage
- Authorization Header
- Token Revocation
- Logout Cleanup

Token Flow:

```text
Login
→ Access Token 발급
→ Refresh Token 발급
→ API 요청에 Access Token 사용
→ Access Token 만료
→ Refresh 요청
→ 새 Access Token 발급
→ Refresh 실패 시 Logout
```

---

### [실무]

작성 기준:

- Access Token 만료 시간은 짧게 설계
- Refresh Token은 HttpOnly Cookie 우선 검토
- Access Token을 memory에 두면 새로고침 UX 처리 필요
- LocalStorage 저장은 XSS 위험 명시
- SessionStorage도 XSS에는 취약함
- Authorization header에 Bearer Token 사용 가능
- refresh 요청 중복 방지
- refresh 실패 시 모든 protected query 중단
- logout 시 token / cache / user state 정리
- token을 URL, log, query key에 넣지 않기

주의:

- JWT payload는 암호화가 아니라 인코딩일 수 있음
- token을 localStorage에 두면 XSS 방어가 더 중요함
- refresh loop가 발생하지 않게 실패 조건 처리
- 만료 직전 동시 요청에서 refresh race condition 발생 가능
- token rotation을 사용하면 이전 refresh token 처리 기준 필요

---

### [FAQ]

Q. Access Token과 Refresh Token 차이는?

A.
Access Token은 API 요청 인증에 쓰는 짧은 수명의 토큰이고, Refresh Token은 새 Access Token을 발급받기 위한 긴 수명의 토큰이다.

Q. Access Token을 LocalStorage에 저장해도 되나?

A.
가능은 하지만 XSS 시 탈취 위험이 크다. 보안 요구가 높으면 HttpOnly Cookie 또는 memory 저장을 검토한다.

Q. Refresh Token은 어디에 저장하는 것이 좋은가?

A.
대체로 HttpOnly Secure Cookie가 우선 후보이다. JavaScript에서 직접 접근 가능한 저장소는 위험이 크다.

---

# 7. Cookie Authentication Rules

## 7.1 Cookie 기반 인증 구조

### [개념]

Cookie 기반 인증은 브라우저가 요청 시 Cookie를 자동으로 전송하고 서버가 Cookie를 검증해 사용자를 식별하는 구조이다.

---

### [핵심]

필수 포함:

- HttpOnly Cookie
- Secure Cookie
- SameSite Cookie
- Session Cookie
- Refresh Cookie
- CSRF Token
- Credentials Include
- Current User API
- Cookie Expiration
- Logout Cookie Clear

Cookie 속성:

| 속성              | 목적                    |
| ----------------- | ----------------------- |
| HttpOnly          | JavaScript 접근 제한    |
| Secure            | HTTPS에서만 전송        |
| SameSite          | cross-site 전송 제한    |
| Path              | Cookie 전송 경로 제한   |
| Domain            | Cookie 전송 도메인 제한 |
| Max-Age / Expires | 만료 시간 제어          |

---

### [실무]

작성 기준:

- 인증 Cookie는 HttpOnly 권장
- 운영 환경에서는 Secure 필수
- SameSite=Lax 또는 Strict 기본 검토
- cross-site 인증이 필요하면 SameSite=None + Secure
- API 요청 시 credentials 설정 필요 여부 명확화
- Cookie 기반 상태 변경 요청은 CSRF 방어 검토
- logout 시 서버에서 Cookie 무효화
- current user API로 세션 상태 확인
- Cookie에 민감정보 자체를 저장하지 않기
- frontend에서 Cookie 값을 직접 읽는 구조 지양

예시:

```ts
await fetch("/api/me", {
  credentials: "include",
});
```

주의:

- CORS credentials 설정과 Cookie SameSite 정책이 함께 맞아야 함
- Cookie는 요청마다 전송되어 크기 관리 필요
- HttpOnly Cookie는 JS에서 못 읽으므로 user state는 API로 확인
- OAuth redirect에서 SameSite 설정이 영향을 줄 수 있음
- Cookie 기반 인증은 CSRF 위협 모델을 고려해야 함

---

### [FAQ]

Q. Cookie 기반 인증의 장점은?

A.
HttpOnly Cookie를 사용하면 JavaScript로 token을 직접 탈취하기 어렵고 서버 세션과 연결하기 쉽다.

Q. Cookie 기반 인증의 단점은?

A.
브라우저가 Cookie를 자동 전송하므로 CSRF 방어와 CORS credentials 설정을 함께 고려해야 한다.

Q. 프론트엔드에서 HttpOnly Cookie를 읽을 수 있나?

A.
읽을 수 없다. 로그인 상태는 current user API로 확인해야 한다.

---

# 8. Bearer Token Authentication Rules

## 8.1 Bearer Token 기반 인증 구조

### [개념]

Bearer Token 기반 인증은 프론트엔드가 Access Token을 API 요청의 Authorization Header에 넣어 서버에 전달하는 구조이다.

---

### [핵심]

필수 포함:

- Authorization Header
- Bearer Token
- Access Token
- Token Storage
- Token Expiration
- Token Refresh
- API Client Interceptor
- 401 Handling
- Refresh Queue
- Logout Cleanup

예시:

```ts
await fetch("/api/posts", {
  headers: {
    Authorization: `Bearer ${accessToken}`,
  },
});
```

---

### [실무]

작성 기준:

- API Client 계층에서 Authorization header 주입
- token 저장 위치를 명확히 결정
- 401 발생 시 refresh flow 실행
- refresh 중 다른 요청은 queue 또는 대기 처리
- refresh 실패 시 logout
- token을 log / error / query string에 남기지 않기
- token을 Query Key에 포함하지 않기
- localStorage 저장 시 XSS 방어 강화
- memory 저장 시 새로고침 후 current user / refresh flow 설계
- API Client에서 token refresh 무한 루프 방지

주의:

- Bearer Token은 가진 사람이 권한을 갖는 구조
- XSS로 token이 탈취되면 위험
- Authorization Header 사용은 일반적 CSRF 위험을 줄일 수 있지만 XSS 위험은 남음
- refresh 요청이 동시에 여러 번 발생하지 않도록 제어
- token 만료와 클라이언트 clock 차이 고려

---

### [FAQ]

Q. Bearer Token 인증은 어떻게 동작하나?

A.
프론트엔드가 Access Token을 Authorization Header에 담아 API 요청을 보내고 서버가 이를 검증한다.

Q. Bearer Token 방식은 CSRF에 안전한가?

A.
Cookie 자동 전송 방식보다 일반적인 CSRF 위험은 낮지만 XSS로 token이 탈취될 수 있으므로 XSS 방어가 중요하다.

Q. API Client에서 Authorization Header를 넣는 이유는?

A.
모든 요청에 인증 처리를 일관되게 적용하고 token refresh, 401 처리, logging redaction을 중앙화하기 위해서이다.

---

# 9. Token Storage Decision Rules

## 9.1 Token 저장 위치 판단

### [개념]

Token Storage Decision은 token을 어디에 저장할지 결정하는 보안 / UX / 구현 복잡도 판단 기준이다.

---

### [핵심]

비교 대상:

| 저장 위치           | 장점            | 위험                |
| ------------------- | --------------- | ------------------- |
| HttpOnly Cookie     | JS 탈취 어려움  | CSRF 고려 필요      |
| Memory              | XSS 탈취면 감소 | 새로고침 처리 복잡  |
| LocalStorage        | 구현 쉬움       | XSS 시 탈취 위험    |
| SessionStorage      | 탭 종료 시 삭제 | XSS 시 탈취 위험    |
| Non-HttpOnly Cookie | 자동 전송 가능  | JS 접근 / CSRF 위험 |

---

### [실무]

판단 기준:

- Refresh Token은 HttpOnly Cookie 우선 검토
- Access Token은 memory 또는 짧은 수명 검토
- LocalStorage는 보안 요구가 낮거나 구조상 필요한 경우 위험을 명시
- SessionStorage는 탭 단위 UX에는 유리하지만 XSS 방어 필요
- Token을 URL에 저장하지 않기
- Token을 Query Key / Log / Analytics에 넣지 않기
- Token 저장소 변경 시 logout / refresh / multi-tab UX 검토
- 저장 위치는 Backend 인증 구조와 함께 결정
- XSS 위험이 큰 앱은 JS 접근 가능한 저장소를 더 신중히 검토

---

### [FAQ]

Q. Token 저장 위치는 무엇을 기준으로 결정하나?

A.
XSS 위험, CSRF 위험, 새로고침 UX, 다중 탭 UX, Backend 구조, Refresh Token 정책을 함께 보고 결정한다.

Q. Memory에 Access Token을 저장하면 안전한가?

A.
브라우저 저장소보다 탈취면은 줄지만 새로고침 시 사라지므로 refresh flow나 current user 확인 전략이 필요하다.

Q. LocalStorage와 SessionStorage 중 무엇이 더 안전한가?

A.
SessionStorage는 탭 종료 시 사라지지만 XSS로 읽힐 수 있다는 점은 LocalStorage와 같다.

---

# 10. Current User Query Rules

## 10.1 Current User / Me Query 설계

### [개념]

Current User Query는 프론트엔드가 현재 로그인한 사용자의 인증 상태와 기본 정보를 서버에 확인하는 핵심 Query이다.

---

### [핵심]

필수 포함:

- `/me`
- Current User
- Session Check
- Auth Loading
- Authenticated
- Unauthenticated
- Expired
- Refetch
- User Scope
- Role
- Permission
- Profile Summary
- Query Cache

Current User 상태:

```text
unknown
→ loading
→ authenticated
→ unauthenticated
→ expired
```

---

### [실무]

작성 기준:

- 앱 초기 진입 시 current user query 실행
- 인증 상태 loading UI 제공
- 로그인 성공 후 current user query 갱신
- 로그아웃 후 current user cache 제거
- 401이면 unauthenticated 처리
- 403은 일반적으로 current user endpoint에서는 권장되지 않음
- current user에는 화면에 필요한 최소 정보만 포함
- permission / role 정보 포함 여부는 보안 모델에 맞춤
- current user query stale time은 UX와 보안 균형으로 결정
- 사용자 변경 시 user scope cache 정리

예시 응답 모델:

```ts
type CurrentUser = {
  id: string;
  name: string;
  role: "USER" | "ADMIN";
};
```

주의:

- current user query 실패를 무조건 서버 장애로 처리하지 않기
- 401은 정상적인 비로그인 상태일 수 있음
- user 객체에 민감정보를 과도하게 포함하지 않기
- current user cache가 오래 유지되면 권한 변경 반영이 늦을 수 있음
- client user state와 server session이 불일치할 수 있음

---

### [FAQ]

Q. Current User Query는 왜 필요한가?

A.
프론트엔드가 현재 로그인 상태와 사용자 정보를 서버 기준으로 확인하기 위해 필요하다.

Q. current user API에서 401이 오면 장애인가?

A.
항상 장애는 아니다. 로그인하지 않은 사용자라면 정상적인 unauthenticated 상태일 수 있다.

Q. current user 응답에 모든 사용자 정보를 넣어도 되나?

A.
권장하지 않는다. 화면과 권한 판단에 필요한 최소 정보만 포함하는 것이 좋다.

---

# 11. Auth State Management Rules

## 11.1 인증 상태 관리

### [개념]

Auth State Management는 current user, token, session status, auth loading, permission, logout 상태를 프론트엔드에서 일관되게 관리하는 구조이다.

---

### [핵심]

상태 유형:

- Unknown
- Loading
- Authenticated
- Unauthenticated
- Expired
- Refreshing
- Logging Out
- Forbidden
- Auth Error

관리 대상:

- Current User
- Auth Status
- Access Token
- Permission
- Role
- Session Expiry
- Refresh State
- Auth Error

---

### [실무]

작성 기준:

- 인증 상태와 사용자 데이터를 분리 가능하게 설계
- Server State는 Query Cache로 관리
- 단순 UI 상태는 Context / Store 사용 가능
- token refresh 상태는 중복 요청 방지 필요
- auth loading 중 protected content 노출 방지
- unauthenticated와 expired 구분 가능
- 403 forbidden은 인증 실패와 구분
- logout 중 UI 상태 처리
- Auth Provider는 너무 많은 책임을 갖지 않게 분리
- Auth Context value는 memoization과 re-render 고려

주의:

- Auth Context에 자주 바뀌는 큰 객체를 넣으면 re-render 증가
- current user와 permission cache가 불일치할 수 있음
- auth 상태를 localStorage flag만으로 판단 금지
- refresh 실패 상태를 무한 loading으로 두지 않기
- auth store에 민감 token 저장 시 보안 검토

---

### [FAQ]

Q. Auth State는 어디에 저장해야 하나?

A.
Current User 같은 서버 상태는 Query Cache로 관리하고, UI용 auth status나 modal 상태는 Context / Store로 관리할 수 있다.

Q. Auth Provider에 모든 인증 로직을 넣어도 되나?

A.
권장하지 않는다. API Client, Query, Guard, Permission, Logout cleanup 책임을 분리하는 것이 유지보수에 좋다.

Q. 로그인 상태를 localStorage boolean으로 판단해도 되나?

A.
안 된다. localStorage 값은 조작 가능하며 서버 세션과 불일치할 수 있다.

---

# 12. Login Flow Rules

## 12.1 로그인 Flow 설계

### [개념]

Login Flow는 사용자가 자격 증명을 제출하고 서버 인증에 성공한 뒤, 세션 또는 토큰을 발급받고 프론트엔드 인증 상태를 갱신하는 과정이다.

---

### [핵심]

Flow:

```text
Login Form 입력
→ Client Validation
→ Login Request
→ Server Authentication
→ Session / Token 발급
→ Current User Query 갱신
→ Redirect 또는 이전 페이지 복귀
```

검토 대상:

- Form Validation
- Login Error
- Pending State
- Duplicate Submit Prevention
- Rate Limit Message
- Session Issue
- Token Issue
- Current User Refetch
- Safe Redirect
- Return URL

---

### [실무]

작성 기준:

- 로그인 Form client validation 제공
- 제출 중 버튼 비활성화
- 로그인 실패 메시지는 과도한 계정 정보 노출 금지
- 서버 오류와 인증 실패 구분
- 성공 후 current user query invalidate / refetch
- 성공 후 private cache 초기화 또는 새 사용자 기준 재조회
- returnUrl은 내부 경로만 허용
- 로그인 성공 후 redirect 경로 명확화
- token / password를 log에 남기지 않기
- 자동완성 / password manager UX 고려

예시 Flow:

```text
사용자가 로그인 버튼 클릭
→ pending 상태 표시
→ 성공하면 /me refetch
→ returnUrl이 안전하면 이동
→ 실패하면 안전한 에러 메시지 표시
```

주의:

- 로그인 실패 시 “이메일 없음”처럼 계정 존재 여부를 과도하게 노출하지 않기
- returnUrl open redirect 방지
- 로그인 성공 후 이전 사용자 cache가 남지 않게 관리
- 중복 제출로 여러 세션 / token 발급 주의
- MFA가 있는 경우 추가 상태 필요

---

### [FAQ]

Q. 로그인 성공 후 무엇을 해야 하나?

A.
Current User Query를 갱신하고 사용자별 cache를 정리 또는 재조회한 뒤 안전한 redirect를 수행해야 한다.

Q. 로그인 실패 메시지는 자세할수록 좋은가?

A.
아니다. 계정 존재 여부가 노출되지 않도록 안전한 메시지를 사용하는 것이 좋다.

Q. 로그인 후 returnUrl은 어떻게 검증하나?

A.
내부 상대 경로만 허용하거나 허용된 도메인 allowlist를 사용해야 한다.

---

# 13. Logout Flow Rules

## 13.1 로그아웃 Flow 설계

### [개념]

Logout Flow는 서버 세션 또는 token을 무효화하고, 프론트엔드에 남아 있는 사용자별 상태와 cache를 안전하게 정리하는 과정이다.

---

### [핵심]

Flow:

```text
Logout 요청
→ Server Session / Token 무효화
→ Client Auth State 초기화
→ User-specific Query Cache 제거
→ Persistent Cache 정리
→ 로그인 페이지 또는 공개 페이지 이동
```

검토 대상:

- Server Logout
- Cookie Clear
- Token Clear
- Query Cache Clear
- Store Reset
- Persistent Cache Clear
- Multi-tab Logout
- Redirect
- WebSocket Disconnect
- Subscription Cleanup

---

### [실무]

작성 기준:

- 서버 logout API 호출
- Cookie / Refresh Token 무효화
- memory token 제거
- localStorage / sessionStorage token 제거
- current user query 제거
- 사용자별 query cache 제거
- auth store reset
- WebSocket / SSE 연결 종료
- private subscription cleanup
- 다른 탭에 logout 이벤트 전파 검토
- logout 후 protected page 접근 차단
- logout 실패 시 UX 정책 명확화

주의:

- 클라이언트 state만 지우고 서버 세션을 무효화하지 않으면 위험
- query cache를 지우지 않으면 이전 사용자 데이터가 보일 수 있음
- 다중 탭에서 한 탭만 로그아웃되는 문제 주의
- logout 직후 background refetch가 다시 사용자 데이터를 가져오지 않게 처리
- refresh 중 logout race condition 주의

---

### [FAQ]

Q. 로그아웃할 때 무엇을 지워야 하나?

A.
서버 세션 / token을 무효화하고, current user, 사용자별 query cache, auth store, persisted cache, 실시간 연결을 정리해야 한다.

Q. 로그아웃 후 이전 사용자 데이터가 보이면 왜 그런가?

A.
사용자별 Query Cache나 전역 Store가 정리되지 않았기 때문이다.

Q. 여러 탭에서 로그아웃을 동기화해야 하나?

A.
가능하면 해야 한다. 한 탭에서 로그아웃했는데 다른 탭이 로그인 상태처럼 보이면 보안과 UX 문제가 생긴다.

---

# 14. Token Refresh Rules

## 14.1 Token Refresh / Silent Refresh

### [개념]

Token Refresh는 Access Token이 만료되었거나 만료 직전일 때 Refresh Token 또는 세션을 사용해 새 Access Token을 발급받는 과정이다.

---

### [핵심]

검토 대상:

- Access Token Expiration
- Refresh Token
- Silent Refresh
- Refresh Queue
- Refresh Lock
- 401 Retry
- Refresh Failure
- Token Rotation
- Infinite Loop Prevention
- Concurrent Request
- Logout on Failure

Refresh Flow:

```text
API 요청
→ Access Token 만료
→ 401 응답
→ Refresh 요청
→ 새 Access Token 저장
→ 원래 요청 재시도
→ Refresh 실패 시 Logout
```

---

### [실무]

작성 기준:

- refresh 요청은 중복 실행되지 않게 lock / queue 처리
- refresh 성공 후 실패했던 요청 재시도 가능
- refresh 실패 시 logout 처리
- refresh endpoint 자체의 401은 재귀 refresh 금지
- refresh token rotation 시 새 token 반영
- 동시 API 요청이 모두 401일 때 하나의 refresh만 수행
- refresh 중 사용자 logout 발생 처리
- retry 횟수 제한
- refresh 상태를 UI에 무한 loading으로 두지 않기
- refresh 실패 원인을 Observability에 기록하되 token은 기록 금지

주의:

- 무한 refresh loop는 흔한 장애
- refresh token 만료와 access token 만료를 구분
- 클라이언트 clock 기준 만료 판단은 오차 가능
- refresh 실패 후 protected query들이 계속 retry하지 않게 중지
- refresh 요청도 CSRF / Cookie 정책 검토 필요

---

### [FAQ]

Q. Token Refresh에서 가장 흔한 문제는?

A.
동시 요청으로 refresh가 여러 번 발생하거나 refresh 실패 후 무한 retry loop가 생기는 문제이다.

Q. 401이 오면 항상 refresh해야 하나?

A.
아니다. refresh endpoint 자체의 401, 권한 문제, 이미 로그아웃된 상태는 refresh 대상이 아닐 수 있다.

Q. Refresh 실패 시 어떻게 해야 하나?

A.
인증 상태를 만료로 처리하고 token / cache를 정리한 뒤 로그인 화면이나 세션 만료 안내로 이동한다.

---

# 15. Session Expiration Rules

## 15.1 세션 만료 처리

### [개념]

Session Expiration은 사용자의 세션이나 token이 만료되어 더 이상 보호 리소스에 접근할 수 없는 상태를 처리하는 기준이다.

---

### [핵심]

상태:

- Active Session
- Expiring Soon
- Expired
- Refreshing
- Refresh Failed
- Logged Out
- Re-auth Required

처리 대상:

- 401 Response
- Current User Expired
- Token Expired
- Idle Timeout
- Absolute Timeout
- Session Renewal
- Re-authentication

---

### [실무]

작성 기준:

- 401 응답을 인증 만료로 처리
- refresh 가능하면 refresh flow 실행
- refresh 불가하면 logout / expired 상태 전환
- 세션 만료 안내 메시지 제공
- 보호 페이지에서 로그인 페이지로 redirect
- 사용자가 작성 중인 Form Draft 보호 검토
- 만료 후 private cache 정리
- background request 401로 전체 앱이 과도하게 튕기지 않게 정책 설정
- idle timeout은 사용자 경고 후 만료 가능
- re-auth가 필요한 민감 작업 구분 가능

주의:

- 401과 403을 혼동하지 않기
- 세션 만료를 서버 오류처럼 표시하지 않기
- 만료된 상태에서 무한 API retry 금지
- 세션 만료 후 이전 화면 데이터 노출 주의
- 로그인 페이지 redirect 시 returnUrl 검증

---

### [FAQ]

Q. 세션 만료 시 어떻게 처리해야 하나?

A.
Refresh 가능하면 갱신하고, 실패하면 인증 상태를 만료로 전환해 cache를 정리하고 로그인 또는 세션 만료 안내를 보여준다.

Q. 세션 만료는 에러인가?

A.
사용자 관점에서는 안내가 필요한 상태이고, 시스템 관점에서는 정상적인 인증 상태 전이일 수 있다.

Q. 401이 발생하면 무조건 로그아웃해야 하나?

A.
Refresh 가능한 구조라면 먼저 갱신을 시도하고, 실패할 때 로그아웃 처리한다.

---

# 16. Protected Route Rules

## 16.1 보호 라우트 / Auth Guard

### [개념]

Protected Route는 인증된 사용자만 접근할 수 있는 페이지이다.

Auth Guard는 사용자의 인증 상태를 확인해 페이지 접근, redirect, loading, forbidden 상태를 처리하는 구조이다.

---

### [핵심]

검토 대상:

- Protected Route
- Public Route
- Guest-only Route
- Admin Route
- Auth Guard
- Route Guard
- Layout Guard
- Middleware Guard
- Server Guard
- Client Guard
- Redirect
- Return URL
- Loading Gate

---

### [실무]

작성 기준:

- 인증 확인 전 protected content 노출 방지
- Auth Loading 상태 제공
- unauthenticated면 login redirect
- authenticated인데 권한 없으면 forbidden 처리
- 로그인 사용자가 login page 접근 시 redirect 가능
- returnUrl은 safe redirect 기준 적용
- Client Guard는 UX용으로 사용 가능
- 서버 데이터 접근 지점에서 인증 / 권한 재검증
- Next.js에서는 Layout / Server Component / Middleware / Route Handler 경계 검토
- 보호 페이지의 prefetch가 민감 데이터 노출을 만들지 않도록 주의

예시 Flow:

```text
Protected Page 접근
→ Current User 확인
→ Loading 표시
→ 로그인 안 됨: /login?returnUrl=...
→ 로그인 됨: 페이지 표시
→ 권한 없음: 403 UI
```

주의:

- 클라이언트 redirect만으로 보안 처리 완료 아님
- protected page HTML / data가 public cache에 저장되지 않도록 주의
- 권한 없는 사용자의 API 직접 호출 가능성을 고려
- redirect loop 방지
- auth loading 중 화면 깜빡임 관리

---

### [FAQ]

Q. Protected Route는 클라이언트에서만 막아도 되나?

A.
아니다. 클라이언트 guard는 UX용이고 실제 데이터 접근은 서버에서 인증과 권한을 검증해야 한다.

Q. Auth 확인 중에는 무엇을 보여줘야 하나?

A.
보호 콘텐츠를 노출하지 않고 loading 또는 skeleton을 보여주는 것이 좋다.

Q. 로그인 페이지에 로그인 사용자가 접근하면 어떻게 하나?

A.
홈이나 이전 returnUrl 등 적절한 페이지로 redirect할 수 있다.

---

# 17. Authorization UI Rules

## 17.1 Role / Permission UI

### [개념]

Authorization UI는 사용자 role, permission, plan, feature flag에 따라 메뉴, 버튼, 페이지, 기능을 다르게 보여주는 UI 구조이다.

하지만 Authorization UI는 보안 경계가 아니라 사용자 경험을 위한 표시 제어이다.

---

### [핵심]

검토 대상:

- Role-based UI
- Permission-based UI
- Feature Flag
- Plan-based UI
- Admin Menu
- Disabled Action
- Hidden Action
- 403 Page
- Permission Hook
- Permission Component
- Server Authorization

예시:

```tsx
function Can({
  allowed,
  children,
}: {
  allowed: boolean;
  children: React.ReactNode;
}) {
  if (!allowed) return null;
  return <>{children}</>;
}
```

---

### [실무]

작성 기준:

- role보다 permission 중심 설계 검토
- 메뉴 숨김은 UX일 뿐 서버 검증 필수
- 삭제 / 승인 / 결제 같은 mutation은 서버 권한 검증
- 권한 없는 action은 숨김 또는 disabled 정책 명확화
- disabled라면 이유 안내 가능
- 403 UI 제공
- permission 변경 후 current user / permission query 갱신
- feature flag와 authorization 혼동 금지
- Client Component에 관리자 전용 민감 데이터 포함 금지
- 권한 helper를 중앙화해 중복 조건 방지

주의:

- client에서 role 값을 조작할 수 있다고 가정
- JWT claim만 보고 서버 권한 검증 생략 금지
- role 조건이 컴포넌트 곳곳에 흩어지면 유지보수 어려움
- hidden action도 API 직접 호출 가능
- 권한 UI와 Server Authorization 테스트를 함께 수행

---

### [FAQ]

Q. 버튼을 숨기면 권한 처리가 된 것인가?

A.
아니다. 버튼 숨김은 UX이고 실제 권한 검증은 서버 API, Server Action, Route Handler에서 수행해야 한다.

Q. Role과 Permission 중 무엇이 더 좋은가?

A.
간단한 앱은 role로 충분할 수 있지만 기능이 복잡해지면 permission 기반이 더 유연하다.

Q. Feature Flag를 권한처럼 써도 되나?

A.
안 된다. Feature Flag는 기능 노출 제어이고 보안 권한 검증을 대체할 수 없다.

---

# 18. OAuth Callback Rules

## 18.1 OAuth / Social Login Callback

### [개념]

OAuth Callback은 외부 인증 제공자가 로그인 결과를 redirect로 돌려주는 지점이다.

프론트엔드는 callback 처리 중 state 검증, code 전달, safe redirect, error handling, current user 갱신을 안전하게 수행해야 한다.

---

### [핵심]

검토 대상:

- OAuth Login
- Provider Redirect
- Callback URL
- Authorization Code
- State Parameter
- Code Exchange
- Error Callback
- Return URL
- Open Redirect Prevention
- Current User Refetch
- Account Linking
- Signup Completion

OAuth Flow:

```text
사용자 OAuth 로그인 클릭
→ Provider로 이동
→ Provider 인증
→ Callback으로 code / state 전달
→ 서버에서 code 교환
→ session / token 발급
→ current user 갱신
→ 안전한 redirect
```

---

### [실무]

작성 기준:

- state parameter 검증
- redirect_uri allowlist 검증
- code exchange는 서버에서 수행
- client secret은 프론트엔드에 노출 금지
- OAuth callback error 처리
- callback 후 current user query 갱신
- returnUrl은 내부 경로만 허용
- account linking 상태 처리
- 신규 사용자 추가 정보 입력 flow 고려
- provider별 실패 / 취소 상태 처리
- callback URL에 token 직접 노출 지양

주의:

- OAuth Client Secret을 브라우저에 두면 안 됨
- state 검증 누락은 CSRF / flow injection 위험
- returnUrl open redirect 방지
- provider callback error를 그대로 노출하지 않기
- SameSite Cookie 정책이 OAuth redirect에 영향 가능

---

### [FAQ]

Q. OAuth code exchange는 어디서 해야 하나?

A.
서버에서 해야 한다. Client Secret이나 token 교환 로직을 브라우저에 노출하면 안 된다.

Q. OAuth state parameter는 왜 필요한가?

A.
로그인 요청과 callback을 연결하고 CSRF성 공격을 방지하기 위해 필요하다.

Q. OAuth callback 후 무엇을 해야 하나?

A.
서버 세션 또는 token 발급을 확인하고 current user query를 갱신한 뒤 안전한 경로로 redirect해야 한다.

---

# 19. Password Reset / Email Verification Rules

## 19.1 비밀번호 재설정 / 이메일 인증 Flow

### [개념]

Password Reset과 Email Verification은 사용자의 계정 복구와 이메일 소유 확인을 처리하는 인증 보조 Flow이다.

이 Flow는 token, URL, 만료, 재사용 방지, 안전한 메시지 처리가 중요하다.

---

### [핵심]

검토 대상:

- Password Reset Request
- Reset Token
- Reset Link
- Token Expiration
- Token Reuse Prevention
- Email Verification Token
- Verification Link
- Safe Error Message
- Account Enumeration Prevention
- Success / Failure State

---

### [실무]

작성 기준:

- 비밀번호 재설정 요청 메시지는 계정 존재 여부 노출 최소화
- reset token은 URL에 포함될 수 있으므로 로그 / analytics 노출 주의
- reset token은 서버에서 검증
- token 만료 / 사용 완료 상태 처리
- 새 비밀번호 Form validation
- reset 성공 후 login 또는 current session 정책 명확화
- 이메일 인증 성공 / 만료 / 이미 인증됨 상태 구분
- 인증 링크 처리 후 token을 화면이나 log에 노출하지 않음
- query string에서 token 제거 또는 history replace 검토
- 에러 메시지는 안전하게 표시

주의:

- reset token을 localStorage에 저장하지 않기
- reset token을 observability log에 남기지 않기
- 계정 존재 여부를 직접 알려주는 문구 주의
- token 재사용 방지는 서버 책임
- 이메일 인증 후 current user 갱신 필요 가능

---

### [FAQ]

Q. 비밀번호 재설정 요청 시 계정이 없다고 알려줘도 되나?

A.
권장하지 않는다. 계정 존재 여부를 노출하지 않는 일반 메시지가 더 안전하다.

Q. Reset Token은 프론트엔드에서 검증하나?

A.
서버에서 검증해야 한다. 프론트엔드는 token을 제출하고 결과에 따라 UI를 보여준다.

Q. 이메일 인증 후 current user를 갱신해야 하나?

A.
로그인 상태에서 인증했다면 current user나 permission 상태를 갱신하는 것이 좋다.

---

# 20. Multi-tab and Cross-tab Auth Rules

## 20.1 다중 탭 인증 동기화

### [개념]

Multi-tab Auth는 같은 브라우저의 여러 탭에서 로그인, 로그아웃, 세션 만료, token refresh 상태가 일관되게 반영되도록 하는 구조이다.

---

### [핵심]

검토 대상:

- Multi-tab Login
- Multi-tab Logout
- Storage Event
- BroadcastChannel
- Shared Cache
- Token Refresh Race
- Session Expiration Sync
- Current User Refetch
- Tab Visibility
- Focus Refetch

---

### [실무]

작성 기준:

- 한 탭에서 logout하면 다른 탭도 logout 반영
- localStorage event 또는 BroadcastChannel 사용 검토
- refresh token flow가 여러 탭에서 동시에 실행되지 않게 주의
- 탭 focus 시 current user refetch 가능
- session 만료 상태 전파
- 다른 계정으로 로그인 시 cache isolation
- WebSocket / SSE 연결 정리
- private data가 다른 탭에 남지 않도록 cache clear
- cross-tab 메시지에 token 포함 금지

주의:

- Memory token 방식은 탭 간 공유가 어려움
- LocalStorage event는 같은 탭에서 발생한 변경에는 직접 반응하지 않을 수 있음
- BroadcastChannel 지원 여부 검토
- 다중 탭 refresh race는 흔한 장애
- cross-tab 이벤트도 클라이언트 신호일 뿐 서버 검증 대체 불가

---

### [FAQ]

Q. 여러 탭에서 로그아웃을 동기화해야 하나?

A.
가능하면 해야 한다. 한 탭에서 로그아웃했는데 다른 탭에서 private data가 계속 보이면 보안과 UX 문제가 생긴다.

Q. Cross-tab 메시지에 token을 넣어도 되나?

A.
안 된다. token은 메시지로 전달하지 말고 상태 변경 신호만 전달하는 것이 좋다.

Q. Memory token 방식은 다중 탭에서 어떤 문제가 있나?

A.
탭 간 token 공유가 어렵고 새 탭이나 새로고침 시 인증 복원 flow가 필요하다.

---

# 21. Cache and Server State Cleanup Rules

## 21.1 인증과 Cache 정리

### [개념]

Authentication Cache Cleanup은 로그인, 로그아웃, 사용자 변경, 권한 변경, 세션 만료 시 Server State Cache와 Client State를 안전하게 정리하는 기준이다.

---

### [핵심]

정리 대상:

- Current User Query
- User Profile Query
- Private Data Query
- Notification Query
- Cart Query
- Permission Query
- Dashboard Query
- Local Store
- Form Draft
- Persistent Cache
- WebSocket Subscription
- SSE Subscription

---

### [실무]

작성 기준:

- logout 시 사용자별 Query Cache 제거
- 세션 만료 시 private cache 제거
- 사용자 전환 시 이전 사용자 cache 제거
- 권한 변경 후 permission / menu / protected data refetch
- login 성공 후 current user query 갱신
- persistent cache에 private data 저장 주의
- auth token 제거와 cache 제거 순서 명확화
- background refetch가 logout 후 실행되지 않도록 중지
- 실시간 subscription cleanup
- Form Draft 보존 여부는 정책에 따라 결정

예시 Flow:

```text
Logout
→ 서버 logout 요청
→ protected query cancel
→ private query cache clear
→ auth store reset
→ subscription close
→ login page redirect
```

주의:

- current user만 지우고 다른 private query를 남기지 않기
- stale cache로 이전 사용자 정보가 보일 수 있음
- persisted cache는 브라우저에 남을 수 있음
- logout 중 진행 중인 mutation 처리 정책 필요
- 사용자별 query key 설계가 cache cleanup에 영향

---

### [FAQ]

Q. 로그아웃 시 Query Cache를 전부 지워야 하나?

A.
공개 데이터는 유지할 수 있지만 사용자별 민감 데이터는 반드시 제거해야 한다.

Q. 사용자 변경 시 왜 cache 정리가 필요한가?

A.
이전 사용자의 프로필, 알림, 장바구니, 권한 정보가 새 사용자에게 보일 수 있기 때문이다.

Q. 권한 변경 후 무엇을 갱신해야 하나?

A.
current user, permission, menu, protected query, role-based UI 관련 cache를 갱신해야 한다.

---

# 22. Next.js App Router Authentication Rules

## 22.1 Next.js App Router 인증 구조

### [개념]

Next.js App Router Authentication은 Server Component, Client Component, Middleware / Proxy, Route Handler, Server Action, Layout, Cache 정책을 조합해 인증 흐름을 구성하는 구조이다.

---

### [핵심]

검토 대상:

- Server Component Auth Check
- Client Component Auth UI
- Layout Guard
- Middleware / Proxy Guard
- Route Handler Auth
- Server Action Auth
- Cookie Access
- Dynamic Rendering
- Static Rendering Risk
- Public Cache Risk
- Redirect
- `notFound`
- `error.tsx`
- `loading.tsx`

---

### [실무]

작성 기준:

- 서버에서 보호 데이터 조회 전 인증 확인
- Server Component에서 auth check 가능
- Client Component guard만으로 보안 처리 완료 금지
- Middleware / Proxy는 early redirect와 UX 보조로 사용 가능
- Route Handler는 API처럼 인증 / 권한 검증
- Server Action은 public endpoint처럼 보고 내부 검증
- 사용자별 데이터는 static / public cache 금지
- `cookies()` / session 접근 시 rendering strategy 영향 확인
- 로그인 페이지와 protected layout 분리
- auth loading / redirect loop 방지

예시 구조:

```text
app
├ (public)
│  └ login
├ (protected)
│  ├ layout.tsx  ← server auth check
│  └ dashboard
└ api
   └ route handlers  ← auth / authorization check
```

주의:

- Server Component에서 가져온 민감 데이터를 Client Component로 과도하게 전달 금지
- Middleware에서 통과했다고 Server Action 권한 검증 생략 금지
- App Router Cache와 사용자별 데이터 cache 혼동 금지
- `revalidatePath`와 auth state 갱신을 혼동하지 않기
- client bundle에 server-only auth utility 포함 금지

---

### [FAQ]

Q. Next.js App Router에서 Auth Check는 어디서 해야 하나?

A.
보호 데이터 접근 지점인 Server Component, Route Handler, Server Action에서 서버 기준으로 검증해야 한다. Middleware는 보조 guard로 사용할 수 있다.

Q. Middleware만으로 보호 페이지 보안이 충분한가?

A.
아니다. Middleware는 우회나 누락 가능성을 고려해 실제 데이터 접근 지점에서 다시 검증해야 한다.

Q. 사용자별 페이지는 Static Rendering해도 되나?

A.
권장하지 않는다. 사용자별 데이터는 Dynamic Rendering 또는 private cache 전략을 사용해야 한다.

---

# 23. Server Action Auth Rules

## 23.1 Server Action 인증 / 권한 검증

### [개념]

Server Action은 서버에서 실행되지만 클라이언트에서 호출될 수 있으므로 인증과 권한 검증이 반드시 필요한 mutation entry point이다.

---

### [핵심]

검토 대상:

- Server Action
- Mutation
- Public Endpoint Assumption
- Require User
- Permission Check
- Input Validation
- CSRF Consideration
- Rate Limit
- Audit Log
- Error Sanitization
- Revalidation
- Cache Invalidation

예시:

```ts
"use server";

export async function deletePostAction(postId: string) {
  const user = await requireUser();
  await assertCanDeletePost(user.id, postId);

  await deletePost(postId);
}
```

---

### [실무]

작성 기준:

- Action 내부에서 `requireUser()` 호출
- client에서 전달된 userId / role 신뢰 금지
- 권한 검증은 서버 데이터 기준
- 입력값 schema validation
- 민감 mutation은 audit log 검토
- 실패 메시지는 안전하게 반환
- mutation 후 필요한 revalidation 수행
- action 호출 가능성을 public endpoint처럼 판단
- 페이지에서 이미 인증 확인했어도 action에서 재검증
- 삭제 / 결제 / 승인 action은 특히 엄격히 검토

주의:

- hidden input 값을 신뢰하지 않기
- role-based UI로 버튼을 숨겨도 action 직접 호출 가능
- action error에 내부 정보 노출 금지
- revalidation은 권한 검증 이후 수행
- CSRF 위협 모델 검토 필요

---

### [FAQ]

Q. Server Action 내부에서도 인증 검증을 해야 하나?

A.
반드시 해야 한다. Server Action은 클라이언트에서 호출될 수 있으므로 별도의 mutation endpoint처럼 취급해야 한다.

Q. Client가 보낸 userId를 사용해도 되나?

A.
권장하지 않는다. 현재 사용자는 서버 세션에서 확인하고 권한도 서버 데이터 기준으로 검증해야 한다.

Q. Server Action에서 권한 검증을 생략하면 어떤 문제가 생기나?

A.
버튼을 숨긴 사용자도 action을 직접 호출해 삭제, 수정, 승인 같은 작업을 수행할 수 있다.

---

# 24. Route Handler Auth Rules

## 24.1 Route Handler 인증 / 권한 검증

### [개념]

Route Handler는 Next.js App Router의 API endpoint 역할을 하므로 일반 Backend API처럼 인증, 권한, 입력 검증, 에러 처리가 필요하다.

---

### [핵심]

검토 대상:

- Route Handler
- API Endpoint
- Method Check
- Require User
- Permission Check
- Request Validation
- Response Sanitization
- 401 Response
- 403 Response
- Rate Limit
- CORS
- CSRF
- Audit Log

---

### [실무]

작성 기준:

- GET / POST / PATCH / DELETE method별 검증
- 보호 endpoint는 requireUser 적용
- 관리자 endpoint는 permission 검증
- request body schema validation
- query param validation
- 응답에 민감정보 포함 금지
- 401 / 403 / 404 구분
- error response는 안전하게 반환
- rate limit 필요한 endpoint 검토
- file upload / payment / admin API는 강화된 검증
- CORS와 인증 / 권한을 혼동하지 않기

예시:

```ts
export async function DELETE(
  request: Request,
  context: { params: Promise<{ postId: string }> },
) {
  const user = await requireUser();
  const { postId } = await context.params;

  await assertCanDeletePost(user.id, postId);
  await deletePost(postId);

  return Response.json({ ok: true });
}
```

주의:

- Route Handler도 외부에서 호출 가능하다고 가정
- client guard 통과 여부를 신뢰하지 않기
- request body의 role / userId 신뢰 금지
- 서버 내부 에러를 그대로 반환하지 않기
- preflight / CORS 설정을 보안 검증으로 오해하지 않기

---

### [FAQ]

Q. Route Handler도 인증 검증이 필요한가?

A.
필요하다. Route Handler는 외부에서 호출 가능한 API endpoint이므로 인증, 권한, 입력 검증을 해야 한다.

Q. 401과 403은 Route Handler에서 어떻게 구분하나?

A.
인증이 없으면 401, 인증은 되었지만 권한이 없으면 403을 반환한다.

Q. request body에 userId가 있으면 그대로 써도 되나?

A.
안 된다. 사용자 식별은 서버 세션 기준으로 해야 하며 body의 userId는 조작 가능하다.

---

# 25. API Client Auth Rules

## 25.1 API Client 인증 처리

### [개념]

API Client Auth는 프론트엔드 API Client 계층에서 Authorization Header, credentials, 401 / 403, token refresh, retry, error normalization을 일관되게 처리하는 구조이다.

---

### [핵심]

검토 대상:

- API Client
- Authorization Header
- Credentials Include
- Token Injection
- Token Refresh
- Refresh Queue
- 401 Handling
- 403 Handling
- Error Normalization
- Retry Policy
- Timeout
- Trace ID
- Redaction

---

### [실무]

작성 기준:

- 인증 방식별 API Client 분리 가능
- Cookie 기반이면 credentials 설정 기준 명확화
- Bearer 기반이면 Authorization header 주입
- 401은 refresh 또는 logout flow
- 403은 forbidden UI / error
- refresh 중복 요청 방지
- token을 log에 남기지 않기
- retry는 idempotent 요청 중심
- 결제 / 생성 mutation retry 주의
- API Error를 정규화해 UI 계층에 전달
- trace id / correlation id 추가 가능

예시:

```ts
type AuthError =
  | { type: "unauthorized"; message: string }
  | { type: "forbidden"; message: string }
  | { type: "session-expired"; message: string };
```

주의:

- API Client가 UI toast를 직접 띄우면 재사용성 저하
- refresh endpoint에 다시 refresh를 시도하는 loop 금지
- token이 error object에 포함되지 않게 redaction
- credentials include는 CORS / Cookie 정책과 연결
- 여러 API base URL의 인증 정책 구분

---

### [FAQ]

Q. API Client에서 인증을 처리하는 이유는?

A.
Authorization header, credentials, 401 / 403, refresh, error normalization을 일관되게 처리하기 위해서이다.

Q. API Client가 toast를 직접 띄워도 되나?

A.
권장하지 않는다. API Client는 정규화된 에러를 반환하고 UI 계층에서 표시 방식을 결정하는 것이 좋다.

Q. 403은 refresh 대상인가?

A.
일반적으로 아니다. 403은 권한 부족이므로 token refresh로 해결되지 않을 가능성이 높다.

---

# 26. Error Handling Rules

## 26.1 인증 에러 처리

### [개념]

Authentication Error Handling은 인증 실패, 권한 없음, 세션 만료, refresh 실패, OAuth 실패, 네트워크 오류를 구분해 처리하는 기준이다.

---

### [핵심]

에러 유형:

- 400 Bad Request
- 401 Unauthorized
- 403 Forbidden
- 404 Not Found
- 409 Conflict
- 422 Validation Error
- 429 Rate Limit
- 500 Server Error
- Network Error
- Token Expired
- Refresh Failed
- OAuth Error
- Session Expired

---

### [실무]

처리 기준:

- 401: 로그인 필요 / 세션 만료 / refresh 시도
- 403: 권한 없음 UI
- 404: 대상 없음
- 409: 상태 충돌
- 422: 입력 검증 에러
- 429: 잠시 후 재시도 안내
- 500: 일반 서버 오류 메시지
- OAuth error: provider 실패 / 취소 / state 불일치 처리
- Network error: 네트워크 안내와 retry
- Refresh failed: logout 또는 session expired 처리

주의:

- 모든 auth error를 login redirect로 처리하지 않기
- 403을 401처럼 refresh하면 불필요한 요청 발생
- 서버 raw error를 사용자에게 그대로 노출 금지
- token / password / auth header를 log에 남기지 않기
- Error Boundary와 인증 에러 UI 역할 구분

---

### [FAQ]

Q. 401과 403은 어떻게 다르게 처리하나?

A.
401은 인증이 없거나 만료된 상태이고, 403은 인증은 되었지만 권한이 없는 상태이다.

Q. 403이 오면 refresh를 시도해야 하나?

A.
일반적으로 아니다. 권한 부족은 새 token으로 해결되지 않을 수 있으므로 forbidden UI를 보여주는 것이 적합하다.

Q. 인증 에러 메시지는 자세히 보여줘도 되나?

A.
내부 정보나 계정 존재 여부를 과도하게 노출하지 않는 안전한 메시지를 사용해야 한다.

---

# 27. Security Rules

## 27.1 인증 구조 보안 기준

### [개념]

Authentication Architecture Security는 인증 정보, token, cookie, redirect, cache, log, client bundle에서 발생할 수 있는 보안 위험을 줄이는 기준이다.

---

### [핵심]

검토 대상:

- Token Exposure
- XSS
- CSRF
- Open Redirect
- Cookie Security
- Token Storage
- Secret Exposure
- Cache Leakage
- Session Fixation
- Clickjacking
- Sensitive Log
- Source Map Exposure
- Auth Callback Security
- Third-party SDK

---

### [실무]

작성 기준:

- token을 URL query에 넣지 않기
- token을 localStorage에 저장할 경우 XSS 방어 강화
- Refresh Token은 HttpOnly Cookie 검토
- Cookie 기반 인증은 CSRF 방어 검토
- returnUrl / redirect URL allowlist 적용
- auth error log에 token / password 포함 금지
- Client Component에 secret 포함 금지
- `NEXT_PUBLIC_`에 auth secret 넣지 않기
- 사용자별 cache public 저장 금지
- Session Replay / Observability에 인증 정보 masking
- OAuth state 검증
- Server Action / Route Handler 권한 재검증

주의:

- 클라이언트 인증 상태는 조작 가능
- JWT는 브라우저에서 읽을 수 있으면 탈취 가능
- HttpOnly Cookie도 XSS 피해를 완전히 막지는 못함
- CORS는 인증 / 권한 검증을 대체하지 않음
- Feature Flag는 Authorization이 아님

---

### [FAQ]

Q. 인증 구조에서 가장 위험한 실수는?

A.
클라이언트 상태를 신뢰하거나 token / secret / 사용자별 데이터를 브라우저와 로그에 과도하게 노출하는 것이다.

Q. returnUrl은 왜 검증해야 하나?

A.
검증하지 않으면 공식 도메인을 거쳐 공격자 사이트로 이동시키는 open redirect가 발생할 수 있다.

Q. CORS를 막으면 인증 보안이 끝나나?

A.
아니다. CORS는 브라우저 접근 제어이고 서버 인증 / 권한 검증은 별도로 필요하다.

---

# 28. Testing Rules

## 28.1 인증 구조 테스트 기준

### [개념]

Authentication Testing은 로그인, 로그아웃, 세션 만료, refresh, protected route, 권한 UI, 401 / 403, OAuth callback, cache cleanup이 올바르게 동작하는지 검증하는 테스트이다.

---

### [핵심]

테스트 대상:

- Login Success
- Login Failure
- Logout
- Current User Query
- Protected Route Redirect
- Guest-only Route Redirect
- Session Expiration
- Token Refresh Success
- Token Refresh Failure
- 401 Handling
- 403 Handling
- Role-based UI
- Permission-based UI
- Server Action Authorization
- Route Handler Authorization
- OAuth Callback
- Safe Redirect
- Cache Cleanup
- Multi-tab Logout

---

### [실무]

작성 기준:

- login success / failure 테스트
- current user loading / authenticated / unauthenticated 상태 테스트
- protected route 접근 테스트
- 401 발생 시 refresh 또는 login redirect 테스트
- 403 발생 시 forbidden UI 테스트
- logout 후 private cache 제거 테스트
- 다른 사용자 로그인 시 이전 사용자 데이터 미노출 테스트
- Server Action / Route Handler 권한 테스트
- returnUrl allowlist 테스트
- OAuth callback error 테스트
- multi-tab logout은 통합 또는 E2E 테스트 검토
- token / password를 테스트 로그에 남기지 않기

예시 Flow:

```text
비로그인 사용자가 /dashboard 접근
→ auth loading
→ 로그인 페이지 redirect
→ 로그인 성공
→ /dashboard 복귀
→ current user 표시
```

주의:

- UI 버튼 숨김만 테스트하고 서버 권한 테스트 생략 금지
- 실제 production token 사용 금지
- refresh retry가 테스트를 느리게 만들 수 있음
- mock auth와 실제 auth API 계약 불일치 주의
- E2E 테스트 계정과 데이터 격리 필요

---

### [FAQ]

Q. 인증 테스트에서 가장 중요한 것은?

A.
로그인 성공 / 실패, 세션 만료, 401 / 403, 보호 라우트, 로그아웃 cache cleanup, 서버 권한 검증을 확인하는 것이다.

Q. 권한 UI만 테스트하면 충분한가?

A.
아니다. Server Action, Route Handler, Backend API의 권한 검증도 함께 테스트해야 한다.

Q. 로그아웃 테스트에서 무엇을 봐야 하나?

A.
서버 로그아웃, current user 제거, 사용자별 cache 제거, protected route 차단, 이전 사용자 데이터 미노출을 확인한다.

---

# 29. Troubleshooting Rules

## 29.1 자주 발생하는 인증 문제

### [개념]

Troubleshooting 문서는 Agent가 Frontend Authentication Architecture 문제의 원인과 해결책을 빠르게 검색할 수 있도록 문제 / 원인 / 해결 형식을 사용한다.

---

### [핵심]

필수 Troubleshooting 항목:

- 새로고침 시 로그인 풀림
- 로그인 후 current user가 null
- 로그아웃 후 이전 사용자 데이터 표시
- 401 무한 refresh loop
- 403인데 계속 refresh 시도
- 다중 탭 로그아웃 불일치
- Protected Route에서 화면 깜빡임
- 로그인 페이지 redirect loop
- returnUrl open redirect 위험
- OAuth callback 실패
- SameSite Cookie 때문에 OAuth 실패
- Cookie가 전송되지 않음
- CORS credentials 오류
- LocalStorage token 탈취 위험
- Server Action 권한 검증 누락
- Route Handler 인증 누락
- Query Cache에 이전 사용자 정보 남음
- Session expired UI가 안 보임
- 로그인 성공 후 redirect가 안 됨
- refresh token 만료 후 무한 loading

---

### [실무]

형식:

```md
문제:

원인:

해결:
```

예시:

```md
문제:

- 새로고침하면 로그인 상태가 풀림

원인:

- Access Token을 memory에만 저장
- current user 복원 flow 없음
- refresh token cookie가 전송되지 않음
- SameSite / Secure / credentials 설정 불일치

해결:

- 앱 초기화 시 current user query 실행
- refresh flow 추가
- cookie 속성과 fetch credentials 확인
- unauthenticated / loading 상태 분리
```

예시:

```md
문제:

- 401 응답 이후 무한 refresh가 발생함

원인:

- refresh endpoint의 401도 다시 refresh 시도
- retry 횟수 제한 없음
- refresh 실패 시 logout 처리 없음
- 동시 요청 refresh queue 없음

해결:

- refresh endpoint는 refresh 대상에서 제외
- refresh lock / queue 적용
- 실패 시 logout 처리
- retry 횟수 제한
```

예시:

```md
문제:

- 로그아웃 후 이전 사용자 데이터가 보임

원인:

- current user만 초기화하고 private query cache는 유지
- persistent cache에 사용자별 데이터 저장
- WebSocket subscription cleanup 누락

해결:

- logout 시 사용자별 query cache clear
- persisted cache에서 private data 제거
- subscription 종료
- 새 사용자 로그인 시 cache scope 재설정
```

---

### [FAQ]

Q. 새로고침 시 로그인 풀림은 왜 생기나?

A.
Access Token을 memory에만 저장했거나 current user / refresh flow가 없거나 Cookie credentials 설정이 맞지 않을 때 발생할 수 있다.

Q. 401 무한 refresh loop는 어떻게 막나?

A.
refresh endpoint를 refresh 대상에서 제외하고, refresh lock / queue와 실패 시 logout 처리를 추가해야 한다.

Q. 로그아웃 후 이전 사용자 데이터가 보이면 무엇을 확인하나?

A.
사용자별 Query Cache, persistent cache, auth store, WebSocket subscription 정리 여부를 확인해야 한다.

---

# 30. Code Example Rules

## 30.1 코드 예제 작성 기준

### [개념]

Frontend Authentication Architecture 문서의 Code Example은 Agent 코드 생성과 리뷰에 직접 사용될 수 있도록 짧고 안전해야 한다.

---

### [핵심]

코드 예제 필수 기준:

- TypeScript 우선
- React / Next.js 기준 예제 우선
- Auth Flow가 명확해야 함
- Server Authorization 포함 권장
- Cache Cleanup 포함 권장
- Secret 하드코딩 금지
- Token logging 금지
- Password logging 금지
- Query Key에 token 포함 금지
- 공격 코드 예제 지양
- 코드블록에 `id=""` 제거

---

### [실무]

권장 예제 유형:

- Current User Query
- Login Flow
- Logout Cleanup
- Protected Route Guard
- Permission Component
- API Client 401 / 403 처리
- Token Refresh Queue Flow
- Server Action `requireUser`
- Route Handler Auth Check
- Safe Redirect Helper
- OAuth Callback Flow
- Multi-tab Logout Signal
- Query Cache Clear on Logout

금지 예제:

- token을 localStorage에 무조건 저장하는 기본 예제
- token을 URL query로 전달
- password / token console log
- client role만 믿고 권한 처리
- 권한 검증 없는 Server Action
- 모든 401에 무한 refresh
- 403에도 refresh 시도
- 사용자별 데이터 public cache
- returnUrl 검증 없는 redirect
- `NEXT_PUBLIC_`에 secret 저장

---

### [FAQ]

Q. 인증 코드 예제는 어떤 기준으로 작성해야 하나?

A.
서버 검증, current user 확인, 안전한 token 처리, logout cache cleanup, 401 / 403 구분이 드러나도록 짧게 작성해야 한다.

Q. LocalStorage token 예제를 넣어도 되나?

A.
위험과 대안을 함께 명시할 때만 가능하다. 기본 권장처럼 작성하면 안 된다.

---

# 31. Comparison Rules

## 31.1 필수 비교 대상

### [개념]

Frontend Authentication Architecture 문서는 Agent의 인증 구조 판단을 돕기 위해 비교 섹션을 적극 사용한다.

---

### [핵심]

필수 비교:

- Authentication vs Authorization
- Session Auth vs Token Auth
- Cookie Auth vs Bearer Token Auth
- Access Token vs Refresh Token
- LocalStorage vs SessionStorage vs Memory vs HttpOnly Cookie
- 401 vs 403
- Client Guard vs Server Guard
- Middleware Guard vs Server Authorization
- Role-based UI vs Permission-based UI
- Current User Query vs Local Auth Flag
- Login Redirect vs Forbidden UI
- Silent Refresh vs Re-login
- SameSite Lax vs Strict vs None
- CSRF vs XSS
- Public Route vs Protected Route vs Guest-only Route
- Server Action Auth vs Route Handler Auth
- Client Cache Clear vs Server Session Invalidation
- OAuth Login vs Password Login

---

### [실무]

Comparison 작성 기준:

- 표 사용 권장
- 기준은 목적 / 장점 / 위험 / 적합 상황 / 주의점으로 정리
- 결론을 명확히 작성
- “항상 A” 같은 절대 표현 금지
- 실무 판단 Flow 포함

---

### [FAQ]

Q. Cookie Auth와 Bearer Token Auth 중 무엇이 더 좋은가?

A.
상황에 따라 다르다. Cookie Auth는 JS token 탈취면이 낮지만 CSRF를 고려해야 하고, Bearer Token은 API 구조가 명확하지만 XSS token 탈취 위험을 고려해야 한다.

Q. Client Guard와 Server Guard 차이는?

A.
Client Guard는 UX용 접근 제어이고, Server Guard는 실제 데이터 접근과 권한을 보호하는 보안 경계이다.

Q. Role-based UI와 Permission-based UI 차이는?

A.
Role-based UI는 역할 단위로 제어하고, Permission-based UI는 기능 권한 단위로 더 세밀하게 제어한다.

---

# 32. Checklist Rules

## 32.1 문서 품질 체크리스트

### [개념]

Frontend Authentication Architecture RAG 문서는 출력 전 구조, 용어, Retrieval Query, 코드 안전성을 검수해야 한다.

---

### [핵심]

Checklist:

- [ ] Frontend Authentication Architecture 목적이 명확한가?
- [ ] Authentication / Authorization 차이를 포함했는가?
- [ ] Session Model 기준을 포함했는가?
- [ ] Token Model 기준을 포함했는가?
- [ ] Cookie Auth 기준을 포함했는가?
- [ ] Bearer Token Auth 기준을 포함했는가?
- [ ] Token Storage 판단 기준을 포함했는가?
- [ ] Current User Query 기준을 포함했는가?
- [ ] Auth State Management 기준을 포함했는가?
- [ ] Login Flow 기준을 포함했는가?
- [ ] Logout Flow와 Cache Cleanup 기준을 포함했는가?
- [ ] Token Refresh / Silent Refresh 기준을 포함했는가?
- [ ] Session Expiration 처리 기준을 포함했는가?
- [ ] Protected Route / Auth Guard 기준을 포함했는가?
- [ ] Role / Permission UI 기준을 포함했는가?
- [ ] OAuth Callback 기준을 포함했는가?
- [ ] Password Reset / Email Verification 기준을 포함했는가?
- [ ] Multi-tab Auth 기준을 포함했는가?
- [ ] Next.js App Router Auth 기준을 포함했는가?
- [ ] Server Action / Route Handler Auth 기준을 포함했는가?
- [ ] API Client Auth 기준을 포함했는가?
- [ ] 401 / 403 Error Handling 기준을 포함했는가?
- [ ] Security 기준을 포함했는가?
- [ ] Testing 기준을 포함했는가?
- [ ] Troubleshooting을 포함했는가?
- [ ] FAQ를 충분히 포함했는가?
- [ ] Retrieval Queries를 포함했는가?
- [ ] 코드블록에 `id=""`가 없는가?
- [ ] token / password / secret 예제 노출이 없는가?
- [ ] 오타와 용어 혼용을 제거했는가?
- [ ] Frontend Security / Data Fetching / Next.js 문서와 충돌하지 않는가?

---

### [실무]

검수 기준:

- Minimum Quality: 95/100
- Target Quality: 97+/100
- 문서 하나는 하나의 주제를 중심으로 작성
- Chunk 단위로 독립 검색 가능해야 함
- FAQ는 실제 사용자 질문 문장으로 작성
- Retrieval Queries는 Agent 검색 패턴 중심으로 작성
- 인증 문서는 보안 경계와 UX 경계를 명확히 구분
- Frontend Security / Data Fetching / Next.js / Testing 문서와 연계 가능해야 함

---

### [FAQ]

Q. Frontend Authentication Architecture 문서 품질에서 가장 중요한 것은?

A.
인증과 권한의 차이, 서버 검증 경계, token / cookie 처리, current user query, refresh, logout cache cleanup, 401 / 403 구분이 명확해야 한다.

---

# 33. Retrieval Optimization Rules

## 33.1 검색 최적화 키워드

### [개념]

Retrieval Optimization은 Agent가 사용자의 질문을 정확한 문서 Chunk로 연결하도록 키워드와 질문 패턴을 강화하는 규칙이다.

---

### [핵심]

강조 키워드:

- Frontend Authentication Architecture
- Authentication
- Authorization
- Session Auth
- Token Auth
- Cookie Auth
- Bearer Token Auth
- Access Token
- Refresh Token
- JWT
- HttpOnly Cookie
- Secure Cookie
- SameSite Cookie
- LocalStorage Token
- SessionStorage Token
- Memory Token
- Current User
- Me Query
- Auth State
- Auth Provider
- Protected Route
- Auth Guard
- Route Guard
- Permission Guard
- Role-based UI
- Permission-based UI
- Login Flow
- Logout Flow
- Token Refresh
- Silent Refresh
- Session Expiration
- 401 Unauthorized
- 403 Forbidden
- OAuth Callback
- Safe Redirect
- Return URL
- Multi-tab Logout
- Query Cache Clear
- Next.js Auth
- App Router Auth
- Server Action Auth
- Route Handler Auth
- API Client Auth
- CSRF
- XSS
- Token Storage
- Auth Testing

---

### [실무]

FAQ와 Retrieval Queries에는 아래 표현을 포함한다.

- Frontend Authentication Architecture는 뭐야?
- 프론트엔드 인증 구조 어떻게 잡아?
- Authentication Authorization 차이
- Cookie Auth Bearer Token 차이
- Access Token Refresh Token 차이
- Token 어디에 저장해야 해?
- LocalStorage JWT 저장해도 돼?
- HttpOnly Cookie 인증은 어떻게 해?
- Current User Query는 왜 필요해?
- 로그인 상태는 어떻게 관리해?
- 새로고침하면 로그인 풀려
- 로그인 후 me가 null이야
- 로그아웃 후 이전 사용자 데이터 보여
- Protected Route는 어떻게 만들어?
- Auth Guard는 클라이언트에서 해도 돼?
- 401 403 차이
- 401 오면 refresh 해야 해?
- 403인데 refresh 하면 안 돼?
- Token Refresh 무한 루프
- OAuth Callback은 어떻게 처리해?
- returnUrl open redirect 막는 법
- Server Action 인증 검증 해야 해?
- Route Handler 인증 검증 해야 해?
- Next.js App Router Auth 구조
- 로그아웃 시 Query Cache 지워야 해?
- 다중 탭 로그아웃 동기화
- Frontend Auth 코드 리뷰 기준

---

### [FAQ]

Q. Retrieval Queries는 왜 필요한가?

A.
사용자의 자연어 질문을 문서 Chunk와 매칭하기 위해 필요하다.

Q. 키워드 반복은 허용되나?

A.
허용된다. 단, 문서 품질을 해치지 않는 범위에서 검색 친화적으로 반복한다.

---

# 34. Version Rules

## 34.1 기준 버전

### [개념]

Frontend Authentication Architecture 문서는 Modern Frontend 기준으로 작성하며 React / Next.js App Router / TypeScript 환경과 연계 가능해야 한다.

---

### [핵심]

기준:

- Modern React
- React 19+
- Next.js App Router
- TypeScript
- Server Component
- Client Component
- Server Action
- Route Handler
- Middleware / Proxy
- HttpOnly Cookie
- SameSite Cookie
- Access Token
- Refresh Token
- Current User Query
- Query Cache
- Protected Route
- OAuth Callback
- Permission-based UI
- Server-side Authorization
- Privacy-aware Auth
- Security-first Auth Flow

Legacy 제외:

- client-only authentication
- localStorage boolean 기반 로그인 판단
- token을 URL query로 전달
- JWT payload만 믿고 권한 판단
- 버튼 숨김만으로 authorization 처리
- 권한 검증 없는 Server Action
- 인증 검증 없는 Route Handler
- 모든 401을 무한 refresh
- 403에도 refresh 시도
- logout 시 cache cleanup 없는 구조
- 사용자별 데이터를 public cache하는 구조
- `NEXT_PUBLIC_`에 auth secret 저장
- password / token logging

---

### [실무]

문서 작성 시 주의:

- 인증 구조는 Backend / Security / Data Fetching과 강하게 연결됨
- Token / Cookie 정책은 프로젝트 보안 요구와 배포 환경에 따라 달라짐
- Next.js App Router의 auth / cache / rendering 동작은 버전별 변화 가능성 있음
- OAuth / OIDC Provider별 상세 동작은 서비스별 문서 확인 필요
- 특정 인증 라이브러리보다 인증 아키텍처 판단 기준을 우선
- 보안 관련 예제는 방어 중심으로 작성
- 실제 secret / token 예제 사용 금지

---

### [FAQ]

Q. Frontend Authentication 문서는 특정 인증 라이브러리 기준이어야 하나?

A.
아니다. NextAuth, Auth.js, custom JWT, session auth 등을 다룰 수 있지만 핵심은 인증 상태, token / cookie, 서버 검증, cache cleanup 기준이다.

Q. 인증 구조는 최신성이 중요한가?

A.
중요하다. 브라우저 Cookie 정책, Next.js App Router, 인증 라이브러리, 보안 권장사항은 변할 수 있으므로 최신 공식 문서 확인이 필요하다.

---

# 35. Common Mistakes

## 35.1 자주 발생하는 실수

### [개념]

Common Mistakes는 Agent가 Frontend Authentication Architecture 코드 리뷰와 문제 진단에서 자주 참조하는 검색 최적화 Chunk이다.

---

### [핵심]

자주 발생하는 실수:

- Authentication과 Authorization 혼동
- client auth state만 신뢰
- localStorage boolean으로 로그인 판단
- JWT payload만 보고 권한 판단
- Access Token을 localStorage에 저장하고 XSS 방어 없음
- Token을 URL query에 전달
- Token을 log / error / query key에 남김
- Refresh Token을 JavaScript 접근 저장소에 저장
- 401과 403 혼동
- 403에도 token refresh 시도
- 401 무한 refresh loop
- refresh 요청 중복 실행
- refresh 실패 후 logout 처리 없음
- 로그아웃 시 query cache 정리 누락
- 이전 사용자 데이터가 다음 사용자에게 보임
- Auth Guard를 client에서만 처리
- 버튼 숨김만으로 권한 처리
- Server Action 권한 검증 누락
- Route Handler 인증 검증 누락
- OAuth state 검증 누락
- returnUrl open redirect 검증 누락
- SameSite / credentials 설정 불일치
- Cookie 기반 인증에서 CSRF 고려 누락
- current user query 없이 local state만 사용
- Auth Provider에 모든 책임 집중

---

### [실무]

리뷰 기준:

- 인증 / 권한 분리 확인
- 서버 검증 경계 확인
- Token 저장 위치 확인
- Cookie 속성 확인
- Current User Query 확인
- Login / Logout Flow 확인
- Refresh Flow 중복 방지 확인
- 401 / 403 처리 확인
- Protected Route 보안 경계 확인
- Role / Permission UI와 서버 권한 검증 확인
- Logout cache cleanup 확인
- OAuth callback / state / returnUrl 확인
- Next.js Server Action / Route Handler 인증 확인
- 민감정보 log 여부 확인
- 테스트에서 auth flow 검증 여부 확인

---

### [FAQ]

Q. Frontend Authentication에서 가장 흔한 실수는?

A.
클라이언트 상태를 신뢰하고 서버 검증 없이 로그인 여부나 권한을 판단하는 것이다.

Q. Token Refresh에서 가장 흔한 실수는?

A.
401 응답마다 refresh를 중복 실행하거나 refresh 실패 후 무한 루프가 발생하는 것이다.

Q. 로그아웃에서 가장 흔한 실수는?

A.
서버 세션이나 token만 무효화하고 프론트엔드 Query Cache와 사용자별 상태를 정리하지 않는 것이다.

---

# 36. Final Goal

## 36.1 최종 목표

### [개념]

Frontend Authentication Architecture RAG 문서는 Agent가 프론트엔드 프로젝트에서 인증 구조를 설계, 생성, 검토, 개선할 수 있도록 만들어야 한다.

---

### [핵심]

Agent가 수행 가능해야 하는 작업:

- Authentication / Authorization 구분
- Session Auth / Token Auth 구조 판단
- Cookie Auth / Bearer Token Auth 비교
- Token Storage 전략 제안
- Current User Query 설계
- Auth State Management 설계
- Login Flow 설계
- Logout Flow와 Cache Cleanup 설계
- Token Refresh / Silent Refresh 설계
- Session Expiration 처리 설계
- Protected Route / Auth Guard 설계
- Role / Permission UI 설계
- OAuth Callback Flow 검토
- Password Reset / Email Verification Flow 검토
- Multi-tab Auth 동기화 설계
- Next.js App Router Auth 구조 검토
- Server Action Auth 검증 리뷰
- Route Handler Auth 검증 리뷰
- API Client Auth 처리 설계
- 401 / 403 Error Handling 설계
- 인증 보안 위험 진단
- Auth Flow 테스트 기준 제안
- Frontend Authentication 코드 리뷰

---

### [실무]

최종 품질 기준:

- 검색 가능한 Chunk 구조
- 명확한 용어 통일
- FAQ 강화
- 실무 판단 기준 포함
- 코드 예제는 짧고 안전하게 작성
- Token / Cookie / Current User / Refresh / Logout 경계 명확화
- Client Guard와 Server Authorization 차이 명확화
- Next.js App Router / Data Fetching / Security / Testing 문서와 연계 가능
- Retrieval Queries 포함

---

### [FAQ]

Q. Frontend Authentication Architecture Domain Rules의 최종 목적은?

A.
Agent가 프론트엔드 프로젝트에서 로그인, 세션 유지, token refresh, protected route, 권한 UI, logout cache cleanup, Next.js 인증 경계를 설계하고 리뷰하도록 만드는 것이다.

---

# Retrieval Queries

### [FAQ]

Q. Frontend Authentication Architecture 문서는 어떤 기준으로 작성해야 해?

A.
Authentication / Authorization 구분, Session / Token 구조, Current User Query, Protected Route, Token Refresh, Logout Cache Cleanup, Next.js Auth 경계를 중심으로 작성해야 한다.

Q. Frontend Authentication Architecture는 뭐야?

A.
프론트엔드에서 로그인 상태, 세션 유지, token 처리, 보호 route, 권한 UI, 로그아웃, 인증 만료를 일관되게 설계하는 구조이다.

Q. 프론트엔드 인증 구조 어떻게 잡아?

A.
서버 검증을 기준으로 current user query를 두고, token / cookie 저장 전략, protected route, refresh, logout cache cleanup, 401 / 403 처리를 설계한다.

Q. Authentication Authorization 차이?

A.
Authentication은 사용자가 누구인지 확인하는 것이고, Authorization은 해당 사용자가 어떤 작업을 할 수 있는지 확인하는 것이다.

Q. Session Auth와 Token Auth 차이는?

A.
Session Auth는 서버가 세션을 관리하고 Cookie로 식별하는 구조이고, Token Auth는 Access Token / Refresh Token으로 API 요청을 인증하는 구조이다.

Q. Cookie Auth Bearer Token 차이?

A.
Cookie Auth는 브라우저가 Cookie를 자동 전송하고, Bearer Token Auth는 Authorization Header에 token을 넣어 전송한다.

Q. Access Token Refresh Token 차이?

A.
Access Token은 API 요청 인증에 쓰는 짧은 수명의 token이고, Refresh Token은 새 Access Token을 발급받기 위한 긴 수명의 token이다.

Q. Token 어디에 저장해야 해?

A.
XSS, CSRF, 새로고침 UX, 다중 탭 UX, Backend 구조를 고려해 HttpOnly Cookie, memory, localStorage, sessionStorage 중 선택한다.

Q. LocalStorage JWT 저장해도 돼?

A.
가능은 하지만 XSS 시 탈취 위험이 크다. 보안 요구가 높으면 HttpOnly Cookie 또는 memory 저장을 검토한다.

Q. SessionStorage는 LocalStorage보다 안전해?

A.
탭 종료 시 사라지는 차이는 있지만 XSS로 읽힐 수 있다는 점은 같다.

Q. Memory Token 방식은 뭐가 문제야?

A.
브라우저 저장소 노출은 줄지만 새로고침이나 새 탭에서 인증 복원 flow가 필요하다.

Q. Refresh Token은 어디에 저장하는 게 좋아?

A.
대체로 HttpOnly Secure Cookie를 우선 검토한다. JavaScript에서 직접 접근 가능한 저장소는 위험이 크다.

Q. HttpOnly Cookie 인증은 어떻게 해?

A.
서버가 HttpOnly Cookie를 발급하고, 프론트엔드는 current user API로 세션 상태를 확인한다.

Q. HttpOnly Cookie를 프론트엔드에서 읽을 수 있어?

A.
읽을 수 없다. 로그인 상태는 current user API로 확인해야 한다.

Q. Cookie 기반 인증에서 CSRF가 중요한 이유는?

A.
브라우저가 Cookie를 자동 전송하므로 공격자가 사용자의 인증 상태를 악용한 요청을 만들 수 있기 때문이다.

Q. SameSite Cookie는 왜 필요해?

A.
cross-site 요청에서 Cookie 전송 범위를 제한해 CSRF 위험을 줄이기 위해 필요하다.

Q. Bearer Token 방식은 CSRF에 안전해?

A.
Cookie 자동 전송 방식보다 일반적인 CSRF 위험은 낮지만 XSS로 token이 탈취될 수 있으므로 XSS 방어가 중요하다.

Q. Current User Query는 왜 필요해?

A.
프론트엔드가 현재 로그인 상태와 사용자 정보를 서버 기준으로 확인하기 위해 필요하다.

Q. current user API에서 401이 오면 장애야?

A.
항상 장애는 아니다. 로그인하지 않은 사용자라면 정상적인 unauthenticated 상태일 수 있다.

Q. current user 응답에 모든 사용자 정보를 넣어도 돼?

A.
권장하지 않는다. 화면과 권한 판단에 필요한 최소 정보만 포함하는 것이 좋다.

Q. 로그인 상태는 어떻게 관리해?

A.
Current User 같은 서버 상태는 Query Cache로 관리하고, UI용 auth status나 modal 상태는 Context / Store로 관리할 수 있다.

Q. Auth Provider에 모든 인증 로직 넣어도 돼?

A.
권장하지 않는다. API Client, Query, Guard, Permission, Logout Cleanup 책임을 분리하는 것이 좋다.

Q. 로그인 상태를 localStorage boolean으로 판단해도 돼?

A.
안 된다. localStorage 값은 조작 가능하며 서버 세션과 불일치할 수 있다.

Q. Login Flow는 어떻게 구성해?

A.
Form 입력, client validation, login request, 서버 인증, session / token 발급, current user 갱신, safe redirect 순서로 구성한다.

Q. 로그인 성공 후 무엇을 해야 해?

A.
Current User Query를 갱신하고 사용자별 cache를 정리 또는 재조회한 뒤 안전한 redirect를 수행해야 한다.

Q. 로그인 실패 메시지는 자세할수록 좋아?

A.
아니다. 계정 존재 여부가 노출되지 않도록 안전한 메시지를 사용하는 것이 좋다.

Q. 로그인 후 me가 null이야. 왜?

A.
세션 Cookie가 전송되지 않았거나 current user query 갱신 누락, credentials 설정 누락, 서버 세션 발급 실패가 원인일 수 있다.

Q. 새로고침하면 로그인 풀려. 왜?

A.
Access Token을 memory에만 저장했거나 current user / refresh flow가 없거나 Cookie credentials 설정이 맞지 않을 수 있다.

Q. Logout Flow는 어떻게 구성해?

A.
서버 logout 요청, session / token 무효화, current user 제거, 사용자별 query cache 제거, auth store reset, redirect 순서로 구성한다.

Q. 로그아웃 시 Query Cache 지워야 해?

A.
공개 데이터는 유지할 수 있지만 사용자별 민감 데이터는 반드시 제거해야 한다.

Q. 로그아웃 후 이전 사용자 데이터 보여. 왜?

A.
사용자별 Query Cache, persistent cache, auth store, WebSocket subscription이 정리되지 않았을 수 있다.

Q. 다중 탭 로그아웃 동기화 해야 해?

A.
가능하면 해야 한다. 한 탭에서 로그아웃했는데 다른 탭에서 private data가 보이면 보안과 UX 문제가 생긴다.

Q. Cross-tab 메시지에 token 넣어도 돼?

A.
안 된다. token은 전달하지 말고 logout이나 auth changed 같은 상태 변경 신호만 전달해야 한다.

Q. Token Refresh는 어떻게 해?

A.
Access Token 만료나 401 발생 시 refresh 요청을 보내 새 token을 받고, 성공하면 원래 요청을 재시도하며 실패하면 logout 처리한다.

Q. 401 오면 refresh 해야 해?

A.
Refresh 가능한 구조라면 시도할 수 있다. 단, refresh endpoint의 401이나 이미 로그아웃된 상태는 제외해야 한다.

Q. 403인데 refresh 하면 안 돼?

A.
일반적으로 안 된다. 403은 권한 부족이므로 token refresh로 해결되지 않을 가능성이 높다.

Q. Token Refresh 무한 루프는 왜 생겨?

A.
refresh endpoint의 401도 다시 refresh하거나, retry 제한과 실패 시 logout 처리가 없을 때 발생한다.

Q. Token Refresh 중복 요청은 어떻게 막아?

A.
refresh lock 또는 queue를 두어 동시 401 요청이 하나의 refresh 요청을 공유하게 한다.

Q. Refresh 실패 시 어떻게 해?

A.
token / auth state / private cache를 정리하고 session expired 또는 login 화면으로 이동한다.

Q. 세션 만료 시 어떻게 처리해?

A.
Refresh 가능하면 갱신하고 실패하면 인증 만료 상태로 전환해 cache를 정리한 뒤 로그인 안내를 보여준다.

Q. 세션 만료는 에러야?

A.
사용자 관점에서는 안내가 필요한 상태이고 시스템 관점에서는 정상적인 인증 상태 전이일 수 있다.

Q. Protected Route는 어떻게 만들어?

A.
Current User 확인 중에는 loading을 보여주고, 비로그인 사용자는 login으로 redirect하며, 권한 없는 사용자는 403 UI를 보여준다.

Q. Auth Guard는 클라이언트에서 해도 돼?

A.
UX용으로는 가능하지만 실제 보안은 Server Component, Route Handler, Server Action, Backend에서 검증해야 한다.

Q. Protected Route에서 화면 깜빡임은 왜 생겨?

A.
인증 상태 확인 전에 보호 콘텐츠를 먼저 렌더링하거나 auth loading 상태가 분리되지 않았기 때문이다.

Q. 로그인 페이지 redirect loop는 왜 생겨?

A.
returnUrl 처리 오류, auth loading과 unauthenticated 상태 혼동, 로그인 페이지 자체에 guard가 잘못 적용된 경우 발생할 수 있다.

Q. 버튼 숨기면 권한 처리 된 거야?

A.
아니다. 버튼 숨김은 UX이고 실제 권한 검증은 서버 API, Server Action, Route Handler에서 수행해야 한다.

Q. Role과 Permission 중 뭐가 좋아?

A.
간단한 앱은 role로 충분할 수 있지만 기능이 복잡해지면 permission 기반이 더 유연하다.

Q. Feature Flag를 권한처럼 써도 돼?

A.
안 된다. Feature Flag는 기능 노출 제어이고 보안 권한 검증을 대체할 수 없다.

Q. OAuth Callback은 어떻게 처리해?

A.
state 검증, code 전달, 서버 code exchange, session / token 발급, current user 갱신, safe redirect 순서로 처리한다.

Q. OAuth code exchange는 어디서 해?

A.
서버에서 해야 한다. Client Secret이나 token 교환 로직을 브라우저에 노출하면 안 된다.

Q. OAuth state parameter는 왜 필요해?

A.
로그인 요청과 callback을 연결하고 CSRF성 공격을 방지하기 위해 필요하다.

Q. SameSite Cookie 때문에 OAuth 실패할 수 있어?

A.
가능하다. OAuth redirect는 cross-site 이동을 포함할 수 있으므로 SameSite 정책과 callback flow를 함께 검토해야 한다.

Q. returnUrl open redirect 막는 법?

A.
returnUrl은 내부 상대 경로만 허용하거나 허용된 도메인 allowlist로 검증해야 한다.

Q. 비밀번호 재설정 요청 시 계정 없음이라고 알려줘도 돼?

A.
권장하지 않는다. 계정 존재 여부가 노출되지 않도록 일반 메시지를 사용하는 것이 안전하다.

Q. Reset Token은 프론트에서 검증해?

A.
서버에서 검증해야 한다. 프론트엔드는 token을 제출하고 결과에 따라 UI를 보여준다.

Q. Next.js App Router Auth 구조는 어떻게 잡아?

A.
Server Component / Layout에서 초기 auth check를 하고, Route Handler와 Server Action에서 인증 / 권한을 재검증하며, Client Component는 UX 상태를 담당한다.

Q. Middleware만으로 보호 페이지 보안 충분해?

A.
아니다. Middleware는 보조 guard이고 실제 데이터 접근 지점에서 다시 인증 / 권한 검증이 필요하다.

Q. 사용자별 페이지는 Static Rendering해도 돼?

A.
권장하지 않는다. 사용자별 데이터는 Dynamic Rendering 또는 private cache 전략을 사용해야 한다.

Q. Server Action 인증 검증 해야 해?

A.
반드시 해야 한다. Server Action은 클라이언트에서 호출될 수 있으므로 별도의 mutation endpoint처럼 취급해야 한다.

Q. Server Action에서 client가 보낸 userId 믿어도 돼?

A.
안 된다. 현재 사용자는 서버 세션에서 확인하고 권한도 서버 데이터 기준으로 검증해야 한다.

Q. Route Handler 인증 검증 해야 해?

A.
필요하다. Route Handler는 외부에서 호출 가능한 API endpoint이므로 인증, 권한, 입력 검증을 해야 한다.

Q. Route Handler에서 request body의 userId를 써도 돼?

A.
안 된다. 사용자 식별은 서버 세션 기준으로 해야 하며 body의 userId는 조작 가능하다.

Q. API Client Auth는 무엇을 처리해?

A.
Authorization header, credentials, 401 / 403, refresh, error normalization, timeout, trace id, token redaction을 처리한다.

Q. API Client가 toast를 직접 띄워도 돼?

A.
권장하지 않는다. API Client는 정규화된 에러를 반환하고 UI 계층에서 표시 방식을 결정하는 것이 좋다.

Q. 인증 구조에서 가장 위험한 실수는?

A.
클라이언트 상태를 신뢰하거나 token / secret / 사용자별 데이터를 브라우저와 로그에 과도하게 노출하는 것이다.

Q. Token을 URL query에 넣어도 돼?

A.
안 된다. browser history, referrer, log, analytics에 노출될 수 있다.

Q. Token을 Query Key에 넣어도 돼?

A.
안 된다. token은 민감정보이며 cache key로 사용하면 보안과 관리 문제가 생긴다.

Q. CORS를 막으면 인증 보안 끝이야?

A.
아니다. CORS는 브라우저 접근 제어이고 서버 인증 / 권한 검증은 별도로 필요하다.

Q. 인증 테스트에서 뭘 봐야 해?

A.
로그인 성공 / 실패, current user, protected route, 401 / 403, refresh, logout cache cleanup, Server Action / Route Handler 권한 검증을 확인해야 한다.

Q. Auth 코드 리뷰 기준은?

A.
인증 / 권한 분리, 서버 검증, token 저장 위치, current user query, refresh flow, logout cache cleanup, 401 / 403 처리, Next.js auth 경계를 확인한다.

Q. Frontend Authentication Architecture RAG 문서 최종 목표는?

A.
Agent가 프론트엔드 프로젝트에서 로그인, 세션 유지, token refresh, protected route, 권한 UI, logout cache cleanup, Next.js 인증 경계를 설계하고 리뷰하게 만드는 것이다.
