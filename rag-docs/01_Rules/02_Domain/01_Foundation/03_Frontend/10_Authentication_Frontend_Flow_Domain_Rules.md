# Authentication Frontend Flow Domain Rules

---

# 1. Domain Purpose

## 1.1 Purpose

### [개념]

Authentication Frontend Flow Domain 문서는 Frontend Agent / Review Agent / PM Agent용 RAG 문서 제작 규칙이다.

목적:

- Frontend 인증 흐름 설계 기준 제공
- Login / Logout / Signup 화면 흐름 지원
- Access Token / Refresh Token 처리 기준 제공
- Authorization Header 적용 기준 제공
- Auth State 관리 기준 제공
- Protected Route 구현 기준 제공
- Role Based UI 처리 기준 제공
- Token Expired 처리 기준 제공
- 401 / 403 응답 처리 기준 제공
- OAuth2 로그인 Frontend 연동 기준 제공
- 사용자 정보 조회 API 연동 기준 제공
- 인증 관련 보안 주의사항 제공
- Backend 인증/인가와 Frontend UX 역할 구분 지원

---

### [핵심]

우선순위:

1. Authentication Flow
2. Login Flow
3. Logout Flow
4. Signup Flow
5. Auth State
6. Access Token
7. Refresh Token
8. Authorization Header
9. Axios Interceptor
10. Protected Route
11. Role Based UI
12. User Profile Fetch
13. Token Expired Handling
14. 401 / 403 Handling
15. OAuth2 Frontend Flow
16. Secure Token Handling
17. Auth Troubleshooting

---

### [실무]

2026 실무 기준에서 Authentication Frontend Flow 문서는 단순 로그인 Form 문서가 아니다.

Frontend Agent가 아래 작업을 수행할 수 있도록 작성한다.

- 로그인 Form 제출 흐름 설계
- 로그인 성공 후 token / user state 처리
- 인증 필요 API 요청에 Authorization Header 포함
- 새로고침 후 인증 상태 복원
- Protected Route 접근 제어
- 로그인 후 이전 페이지 redirect
- 로그아웃 시 token / user state / cache 정리
- token 만료 시 401 처리
- refresh token 기반 재발급 흐름 검토
- 권한 부족 403 처리
- ROLE_USER / ROLE_ADMIN UI 분기
- OAuth2 redirect callback 처리
- Frontend 보안 위험 검토

---

### [FAQ]

Q. Authentication Frontend Flow 문서는 Form Handling과 뭐가 달라?

A.
Form Handling은 입력값과 검증 중심이고 Authentication Frontend Flow는 로그인 이후 token, auth state, protected route, 인증 API 흐름에 집중한다.

Q. Frontend 인증에서 가장 중요한 기준은 뭐야?

A.
Auth State, token 처리, Authorization Header, Protected Route, 401 / 403 처리, Backend 보안과 Frontend UX 역할 구분이다.

Q. Frontend에서 로그인 상태를 확인하면 보안이 되는 거야?

A.
아니다. Frontend 인증 처리는 UX용이고 실제 보안은 Backend 인증/인가가 반드시 담당해야 한다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

Authentication Frontend Flow 문서는 React Frontend 인증 흐름 구현에 필요한 범위를 포함한다.

포함 범위:

- Login Flow
- Logout Flow
- Signup Flow Basics
- Auth State
- Auth Loading
- User Summary State
- Access Token
- Refresh Token Basics
- Token Storage Criteria
- Authorization Header
- Bearer Token
- Axios Auth Instance
- Request Interceptor
- Response Interceptor
- 401 Handling
- 403 Handling
- Token Expired Handling
- Token Refresh Basics
- Protected Route
- Private Route
- Public Only Route
- Role Based Route
- Role Based UI
- User Profile Fetch
- Auth Restore on Refresh
- Redirect After Login
- OAuth2 Redirect Flow Basics
- Social Login Callback Basics
- Auth Error Handling
- Auth Security Basics
- Auth Troubleshooting
- Logout Cleanup
- Query Cache Cleanup

---

### [핵심]

반드시 포함:

- 인증 상태는 loading / authenticated / unauthenticated를 구분
- 로그인 성공 후 token과 user state 처리 기준 필요
- 인증 API 요청에는 Authorization Header 필요
- Authorization 형식은 `Bearer <accessToken>` 기준
- Protected Route는 UX용 접근 제어
- Backend 인증/인가가 실제 보안 기준
- 401과 403을 구분
- token 만료 시 refresh 또는 logout 기준 필요
- 새로고침 후 인증 상태 복원 흐름 필요
- 로그아웃 시 token, user state, cache 정리 필요
- role 기반 UI는 Backend 권한 검증을 대체하지 않음

---

### [실무]

Authentication Frontend Flow는 Form Handling과 Data Fetching 위에서 동작한다.

실무 연결:

```text
Form Handling & Validation
→ Login API Request
→ Token Handling
→ Auth State Update
→ Axios Authorization Header
→ Protected Route
→ Authenticated API Integration
→ Logout / Token Expired Handling
```

---

### [FAQ]

Q. Auth 문서에서 JWT 구조도 깊게 다뤄?

A.
Frontend에서 필요한 token 사용 흐름은 포함하지만 JWT 서명, 필터, Security 설정은 Backend Security 문서에서 다룬다.

Q. OAuth2 전체 구조도 여기서 다뤄?

A.
Frontend redirect callback 처리와 사용자 상태 반영 기준은 포함하지만 OAuth2 서버 설정 심화는 Backend Security 또는 OAuth2 문서에서 다룬다.

Q. refresh token 보안 저장 전략을 깊게 다뤄?

A.
기초 주의사항은 포함하지만 상세 보안 정책은 Security / Authentication Architecture 문서에서 다룬다.

---

## 2.2 Excluded Scope

### [개념]

Authentication Frontend Flow 문서에서는 Backend 인증 구현과 고급 보안 아키텍처 심화를 제외한다.

제외 범위:

- Spring Security Filter Chain 심화
- JWT 서명 / 검증 로직
- JWT Claims 설계 심화
- OAuth2 Provider 설정 심화
- Backend Refresh Token Rotation 심화
- CSRF 방어 전략 심화
- XSS 방어 전체 전략
- HttpOnly Cookie 보안 심화
- Session 기반 인증 Backend 심화
- MFA / 2FA 심화
- Passkey / WebAuthn 심화
- Admin Permission Matrix 심화
- SSO / SAML 심화
- Backend Authorization Policy 심화

---

### [핵심]

제외 이유:

- Frontend Foundation 범위 초과
- Backend Security 문서와 역할 분리 필요
- Agent Retrieval 혼선 방지
- Chunk 품질 유지
- Frontend 인증 흐름과 UX 처리에 집중

---

### [실무]

고급 기술은 별도 Domain Rules에서 관리한다.

예:

```text
Authentication Frontend Flow
→ Security Frontend Basics
→ Spring Security JWT
→ OAuth2 Backend Integration
→ Advanced Auth Architecture
```

---

### [FAQ]

Q. JWT 만드는 코드는 여기서 다뤄?

A.
아니다. JWT 생성과 검증은 Backend 영역이고 Frontend는 발급받은 token을 사용하는 흐름을 다룬다.

Q. Spring Security 설정도 여기서 다뤄?

A.
아니다. Frontend 인증 흐름과 Backend Security 설정은 문서를 분리한다.

---

# 3. Section Priority

## 3.1 Required Sections

### [개념]

Authentication Frontend Flow RAG 문서는 모든 주요 Chunk에 아래 Section을 우선 포함한다.

Required:

- [개념]
- [핵심]
- [실무]
- [FAQ]

---

### [핵심]

필수 Section 목적:

- [개념]: 정의와 역할
- [핵심]: 검색 친화 키워드
- [실무]: 실제 인증 흐름 적용 기준
- [FAQ]: 사용자 질문 매칭 강화

---

### [실무]

각 문서는 아래 구조를 기본으로 한다.

```md
# Topic

## Sub Topic

### [개념]

### [핵심]

### [실무]

### [FAQ]
```

---

### [FAQ]

Q. 모든 Authentication 문서에 FAQ가 필요해?

A.
필요하다. FAQ는 사용자 질문과 RAG 검색 매칭을 강화한다.

Q. [면접] 섹션을 써도 돼?

A.
안 된다. 반드시 [FAQ] 섹션을 사용한다.

---

## 3.2 Recommended Sections

### [개념]

Authentication Frontend Flow 문서에는 인증 흐름과 오류 검증을 위해 추가 Section을 포함할 수 있다.

Strongly Recommended:

- [Flow]
- [예제]
- [주의]
- [Best Practice]
- [Troubleshooting]
- [Checklist]
- [Comparison]

---

### [핵심]

추천 Section 사용 기준:

- Login Flow → [Flow], [예제]
- Protected Route → [Flow], [주의]
- Token Handling → [Best Practice], [주의]
- 401 / 403 → [Troubleshooting], [Comparison]
- Refresh Token → [Flow], [주의]
- OAuth2 Callback → [Flow], [Troubleshooting]
- Logout Cleanup → [Checklist]

---

### [실무]

예시:

```md
### [Flow]

Login Submit
→ Login API
→ Receive Token
→ Store Auth Result
→ Fetch User Profile
→ Update Auth State
→ Redirect
```

---

### [FAQ]

Q. Authentication 문서에 Troubleshooting이 중요한 이유는?

A.
401, 403, token 누락, Bearer 형식 오류, 새로고침 후 로그아웃, redirect loop 같은 문제가 자주 발생하기 때문이다.

Q. Comparison은 언제 쓰면 좋아?

A.
401 vs 403, Access Token vs Refresh Token, localStorage vs cookie, Protected Route vs Backend Authorization처럼 헷갈리는 개념을 비교할 때 사용한다.

---

# 4. Authentication Overview Rules

## 4.1 Authentication vs Authorization

### [개념]

Authentication은 사용자가 누구인지 확인하는 과정이다.

Authorization은 확인된 사용자가 특정 기능이나 리소스에 접근할 권한이 있는지 판단하는 과정이다.

---

### [핵심]

반드시 설명:

- Authentication
- Authorization
- Login
- Role
- Permission
- 401
- 403
- Protected Route
- Backend Authorization
- Frontend UX Guard

비교:

| 비교          | Authentication      | Authorization            |
| ------------- | ------------------- | ------------------------ |
| 의미          | 누구인지 확인       | 무엇을 할 수 있는지 확인 |
| 예            | 로그인              | 관리자 페이지 접근       |
| 실패 Status   | 401                 | 403                      |
| Frontend 역할 | 로그인 상태 UX 처리 | 메뉴 / 화면 노출 제어    |
| 최종 보안     | Backend 검증 필수   | Backend 검증 필수        |

---

### [실무]

예:

```text
로그인하지 않은 사용자가 /mypage 접근
→ Authentication 실패
→ 401 또는 login redirect

일반 사용자가 /admin 접근
→ Authorization 실패
→ 403 또는 forbidden page
```

주의:

- 로그인 여부와 권한 여부를 구분
- Frontend role check는 UX용
- Backend API 권한 검증 필수
- 401과 403을 같은 에러로 처리하지 않음

---

### [FAQ]

Q. Authentication과 Authorization 차이는?

A.
Authentication은 사용자가 누구인지 확인하는 것이고 Authorization은 그 사용자가 접근 권한이 있는지 확인하는 것이다.

Q. 401과 403 차이는?

A.
401은 인증 실패 또는 로그인 필요이고 403은 인증은 되었지만 권한이 부족한 경우다.

---

## 4.2 Frontend Auth Responsibility

### [개념]

Frontend 인증 책임은 사용자 경험을 관리하는 것이다.

Frontend는 로그인 상태에 따라 화면을 바꾸고, 인증 API에 token을 포함하고, 인증 실패 시 적절한 UI를 보여준다.

---

### [핵심]

Frontend 책임:

- Login Form 제공
- Signup Form 제공
- Auth State 관리
- Token 전달
- Protected Route UX 처리
- Role Based UI 처리
- Logout 처리
- 401 / 403 UI 처리
- 인증 상태 loading 처리
- redirect 처리

Frontend 책임 아님:

- 실제 token 검증
- 최종 권한 판단
- 비밀번호 검증 최종 책임
- API 보안 보장
- 사용자 권한 강제

---

### [실무]

Frontend Auth Flow:

```text
User Action
→ Frontend Auth UI
→ Backend Auth API
→ Backend Token / User Response
→ Frontend Auth State Update
→ Authenticated API Request
→ Backend Authorization Check
```

주의:

- Frontend에서 버튼을 숨겨도 API 직접 호출은 가능
- Backend에서 반드시 인증/인가 확인
- Frontend는 사용자 경험과 요청 흐름을 담당
- 보안 판단은 Backend 기준

---

### [FAQ]

Q. 관리자 버튼을 Frontend에서 숨기면 보안이 돼?

A.
아니다. 버튼 숨김은 UX용이고 실제 관리자 API는 Backend에서 권한 검증해야 한다.

Q. Frontend Auth State가 true면 사용자를 신뢰해도 돼?

A.
Frontend 표시에는 사용할 수 있지만 실제 데이터 접근 권한은 Backend 응답으로 확인해야 한다.

---

# 5. Login Flow Rules

## 5.1 Login Form Flow

### [개념]

Login Form Flow는 사용자가 이메일 / 아이디와 비밀번호를 입력해 로그인 API를 호출하고 인증 상태를 갱신하는 흐름이다.

---

### [핵심]

기본 Flow:

```text
Input Email / Password
→ Client Validation
→ Login API Request
→ Success
→ Store Token / Auth Result
→ Fetch User Profile if Needed
→ Update Auth State
→ Redirect
→ Failure
→ Show Error Message
```

---

### [실무]

Login Submit 예:

```tsx
type LoginRequest = {
  email: string;
  password: string;
};

async function handleLogin(values: LoginRequest) {
  try {
    const response = await login(values);

    setAccessToken(response.accessToken);
    setAuthenticated(true);
    setUser(response.user);

    navigate("/", { replace: true });
  } catch (error) {
    setSubmitError("이메일 또는 비밀번호를 확인해 주세요.");
  }
}
```

권장:

- password console.log 금지
- 로그인 실패 메시지는 과도하게 상세하지 않게 처리
- submit loading 처리
- 중복 제출 방지
- 로그인 성공 후 redirect 기준 명확화
- 이전 위치로 돌아가기 지원 가능
- token 저장과 user state 업데이트 분리 가능

---

### [FAQ]

Q. 로그인 성공 후 바로 메인으로 이동하면 돼?

A.
가능하다. 다만 보호 페이지에서 로그인으로 온 경우 원래 페이지로 돌아가는 redirect flow를 제공할 수 있다.

Q. 로그인 실패 메시지는 어떻게 보여줘?

A.
계정 정보 불일치는 global form error로 표시하는 경우가 많고, 이메일 형식 오류는 field error로 처리한다.

Q. password를 console.log로 확인해도 돼?

A.
안 된다. 비밀번호는 민감정보이므로 로그에 남기지 않는다.

---

## 5.2 Login Response Handling

### [개념]

Login Response Handling은 로그인 API 성공 응답에서 token과 사용자 정보를 어떻게 처리할지 정하는 기준이다.

---

### [핵심]

응답 후보:

- accessToken
- refreshToken
- userId
- email
- nickname
- role
- tokenType
- expiresIn
- user summary
- redirect target

---

### [실무]

응답 예:

```json
{
  "accessToken": "access-token-value",
  "refreshToken": "refresh-token-value",
  "user": {
    "userId": 1,
    "nickname": "jun",
    "role": "ROLE_USER"
  }
}
```

처리 기준:

```text
accessToken → Authorization Header에 사용
refreshToken → 재발급 흐름에 사용
user summary → Auth State에 저장
role → Role Based UI에 사용
expiresIn → 만료 처리 기준에 사용 가능
```

주의:

- Backend 응답 wrapper 구조 확인
- response.data.data 구조 확인
- tokenType이 있으면 Bearer 중복 주의
- 사용자 상세 정보가 부족하면 `/me` API 조회
- 민감한 사용자 정보 저장 최소화

---

### [FAQ]

Q. 로그인 응답에 user 정보가 없으면 어떻게 해?

A.
로그인 성공 후 access token으로 `/me` 또는 사용자 정보 조회 API를 호출해 Auth State를 채울 수 있다.

Q. tokenType이 Bearer로 오면 어떻게 해?

A.
Authorization Header 생성 시 `Bearer Bearer token`처럼 중복되지 않도록 처리 기준을 통일해야 한다.

---

## 5.3 Redirect After Login

### [개념]

Redirect After Login은 로그인 성공 후 사용자를 어디로 이동시킬지 결정하는 흐름이다.

---

### [핵심]

사용 상황:

- login page에서 직접 로그인
- protected page 접근 후 login redirect
- token expired 후 login redirect
- signup 후 login
- OAuth2 callback 후 redirect

---

### [실무]

Flow:

```text
Protected Page Access
→ Save Current Location
→ Redirect Login
→ Login Success
→ Navigate Saved Location
```

React Router 예:

```tsx
const location = useLocation();
const navigate = useNavigate();

const from = location.state?.from ?? "/";

navigate(from, { replace: true });
```

Protected Route에서 전달:

```tsx
return <Navigate to="/login" replace state={{ from: location.pathname }} />;
```

주의:

- redirect loop 방지
- 외부 URL redirect 방지
- redirect target validation 고려
- login page 접근 시 이미 로그인된 사용자는 main으로 이동 가능
- replace 옵션으로 history 정리

---

### [FAQ]

Q. 로그인 후 원래 보려던 페이지로 돌아가려면?

A.
Protected Route에서 location state나 query string에 이전 경로를 저장하고 로그인 성공 후 해당 경로로 navigate한다.

Q. redirect loop는 왜 생겨?

A.
인증 상태 loading을 기다리지 않거나 login page와 protected page가 서로 redirect 조건에 걸릴 때 발생한다.

---

# 6. Signup Flow Rules

## 6.1 Signup Flow Basics

### [개념]

Signup Flow는 회원가입 Form 입력값을 검증하고 회원가입 API를 호출한 뒤 후속 이동을 처리하는 흐름이다.

---

### [핵심]

기본 Flow:

```text
Input Signup Fields
→ Client Validation
→ Signup API Request
→ Server Validation
→ Success
→ Login Page Redirect or Auto Login
→ Failure
→ Field Error / Global Error
```

---

### [실무]

Signup 처리 기준:

- email format 검증
- password policy 검증
- confirm password 검증
- nickname 검증
- agreement checkbox 검증
- duplicate email / nickname server validation
- 회원가입 성공 후 로그인 페이지 이동
- 자동 로그인 여부는 프로젝트 정책에 따름

예:

```tsx
async function handleSignup(values: SignupFormValues) {
  const requestBody = toSignupRequest(values);

  try {
    await signup(requestBody);
    navigate("/login", { replace: true });
  } catch (error) {
    setErrors(mapServerValidationErrors(error));
  }
}
```

주의:

- Client Validation만 신뢰하지 않음
- password 로그 출력 금지
- 서버 field error mapping 기준 필요
- 회원가입 성공 후 token 발급 여부 확인
- 자동 로그인 시 Login Flow와 동일하게 Auth State 업데이트

---

### [FAQ]

Q. 회원가입 성공 후 자동 로그인해야 해?

A.
프로젝트 정책에 따라 다르다. 자동 로그인하려면 로그인 응답과 동일하게 token과 user state를 처리해야 한다.

Q. 이메일 중복 검사는 Frontend에서 가능해?

A.
형식 검사는 Frontend에서 가능하지만 실제 중복 여부는 Backend API 기준으로 확인해야 한다.

---

# 7. Auth State Rules

## 7.1 Auth State Design

### [개념]

Auth State는 사용자의 인증 여부, 인증 확인 진행 상태, 사용자 요약 정보를 표현하는 상태다.

---

### [핵심]

Auth State 구성:

- authenticated
- loading
- user
- role
- accessToken presence
- initialized
- authError
- tokenExpired
- login action
- logout action

---

### [실무]

TypeScript 예:

```tsx
type AuthUser = {
  userId: number;
  nickname: string;
  role: "ROLE_USER" | "ROLE_ADMIN";
};

type AuthState = {
  initialized: boolean;
  authenticated: boolean;
  loading: boolean;
  user: AuthUser | null;
};
```

상태 구분:

```text
initialized false → 앱 시작 후 인증 상태 확인 중
authenticated true → 로그인 상태
authenticated false → 비로그인 상태
loading true → login / logout / me 요청 처리 중
user null → 사용자 정보 없음
```

권장:

- authenticated와 user를 함께 관리
- 초기 인증 확인 상태 initialized 구분
- token 존재만으로 authenticated 확정하지 않음
- `/me` API로 사용자 상태 확인 가능
- logout 시 user와 authenticated 초기화
- role naming 통일

---

### [FAQ]

Q. token이 있으면 authenticated true로 해도 돼?

A.
가능은 하지만 token이 만료되었거나 위조되었을 수 있으므로 `/me` 같은 API로 확인하는 흐름이 더 안전하다.

Q. auth loading은 왜 필요해?

A.
새로고침 후 인증 상태 확인 전에 Protected Route가 login으로 잘못 redirect하는 것을 막기 위해 필요하다.

---

## 7.2 Auth State Storage

### [개념]

Auth State Storage는 token과 사용자 정보를 브라우저 어디에 보관할지 결정하는 기준이다.

---

### [핵심]

저장 후보:

- memory state
- localStorage
- sessionStorage
- HttpOnly Cookie
- Zustand persist
- Context state
- Redux store

---

### [실무]

비교:

| 저장 위치       | 장점               | 주의                     |
| --------------- | ------------------ | ------------------------ |
| Memory State    | XSS 노출 감소      | 새로고침 시 사라짐       |
| localStorage    | 새로고침 유지 쉬움 | XSS 노출 위험            |
| sessionStorage  | 탭 단위 유지       | XSS 노출 위험            |
| HttpOnly Cookie | JS 접근 불가       | CSRF / Backend 설정 고려 |
| Zustand Persist | 구현 편리          | 저장 대상 최소화 필요    |

주의:

- Frontend 저장소는 보안 요구사항에 따라 결정
- access token / refresh token 저장 위치는 Backend 정책과 함께 결정
- 민감정보를 user state에 과도하게 저장하지 않음
- localStorage에 저장한 token은 XSS에 취약할 수 있음
- logout 시 저장소 정리 필수

---

### [FAQ]

Q. token은 localStorage에 저장하면 돼?

A.
가능은 하지만 XSS 위험이 있다. 프로젝트 보안 요구사항에 따라 memory, sessionStorage, HttpOnly Cookie 등을 검토해야 한다.

Q. user 정보를 전부 저장해도 돼?

A.
권장하지 않는다. UI에 필요한 최소한의 user summary만 저장하는 것이 좋다.

---

## 7.3 Auth Restore on Refresh

### [개념]

Auth Restore on Refresh는 브라우저 새로고침 후에도 로그인 상태를 복원하는 흐름이다.

---

### [핵심]

필수 포함:

- app initialization
- token check
- `/me` request
- auth loading
- initialized state
- token expired
- refresh token
- logout fallback

---

### [실무]

Flow:

```text
App Start
→ Check Stored Token or Cookie
→ If Exists Call /me
→ Success: Set User and Authenticated
→ Failure: Clear Auth
→ Set Initialized True
→ Render Routes
```

예:

```tsx
useEffect(() => {
  async function initializeAuth() {
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

  initializeAuth();
}, []);
```

주의:

- 초기화 완료 전 Protected Route redirect 보류
- token 존재만으로 로그인 확정하지 않음
- `/me` 실패 시 token 정리
- refresh token flow가 있으면 재발급 후 `/me` 재시도 가능
- 앱 첫 렌더링 깜빡임 방지 고려

---

### [FAQ]

Q. 새로고침하면 로그인이 풀려?

A.
Auth State가 memory에만 있거나 초기 인증 복원 로직이 없으면 새로고침 시 로그인이 풀릴 수 있다.

Q. 새로고침 후 바로 login으로 튕겨?

A.
인증 상태 확인 loading을 기다리지 않고 Protected Route가 먼저 redirect했을 가능성이 있다.

---

# 8. Token Handling Rules

## 8.1 Access Token Rules

### [개념]

Access Token은 인증된 API 요청에 사용되는 짧은 수명의 token이다.

Frontend는 인증이 필요한 API 요청에 access token을 Authorization Header로 포함한다.

---

### [핵심]

필수 포함:

- access token
- Authorization Header
- Bearer Token
- expiration
- authenticated request
- token storage
- token removal
- token refresh

---

### [실무]

Header 형식:

```text
Authorization: Bearer <accessToken>
```

Axios Interceptor 예:

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

- Bearer와 token 사이 공백 필요
- access token이 없으면 header 생략
- token 만료 시 401 가능
- token을 console.log로 출력하지 않음
- token 저장 위치 보안 검토
- logout 시 access token 제거

---

### [FAQ]

Q. Authorization Header 형식은 뭐야?

A.
일반적으로 `Authorization: Bearer <accessToken>` 형식을 사용한다.

Q. token은 있는데 401이 나?

A.
Authorization Header에 실제로 포함되었는지, Bearer 형식이 맞는지, token이 만료되지 않았는지 확인해야 한다.

---

## 8.2 Refresh Token Rules

### [개념]

Refresh Token은 access token이 만료되었을 때 새 access token을 발급받기 위한 token이다.

Frontend에서는 refresh token flow를 통해 사용자 재로그인 빈도를 줄일 수 있다.

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

---

### [실무]

주의:

- refresh token 저장 위치는 보안 요구사항에 따라 결정
- refresh 요청 중 중복 refresh 방지
- 원래 요청 retry는 한 번만 수행
- refresh 실패 시 logout 처리
- refresh loop 방지
- refresh token rotation 정책은 Backend와 맞춤
- 여러 요청이 동시에 401을 받을 때 queue 처리 고려

간단 기준:

```text
401 발생
→ refresh 가능 여부 확인
→ refresh 성공: token 갱신 후 원래 요청 재시도
→ refresh 실패: clearAuth 후 login redirect
```

---

### [FAQ]

Q. access token이 만료되면 어떻게 해?

A.
refresh token이 있으면 새 access token을 요청하고 성공 시 원래 API 요청을 재시도할 수 있다.

Q. refresh 요청도 실패하면?

A.
인증 정보를 정리하고 login 페이지로 이동시키는 것이 일반적이다.

Q. refresh 요청이 무한 반복될 수 있어?

A.
잘못 구현하면 가능하다. refresh 요청 자체에는 retry를 걸지 않거나 `_retry` 같은 플래그로 반복을 막아야 한다.

---

## 8.3 Token Storage Security Rules

### [개념]

Token Storage Security는 token을 브라우저에 저장할 때 발생할 수 있는 보안 위험을 줄이는 기준이다.

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
- console log
- browser extension
- persistent storage

---

### [실무]

기준:

- token을 코드에 하드코딩하지 않음
- token을 console.log로 출력하지 않음
- localStorage는 XSS에 취약할 수 있음
- HttpOnly Cookie는 JS 접근이 불가능하지만 CSRF 대응 필요
- refresh token은 access token보다 더 민감하게 취급
- 민감정보는 persist 대상 최소화
- logout 시 storage 정리
- Frontend 저장소 선택은 Backend 인증 정책과 함께 결정

주의:

- 어떤 저장 방식도 완전한 만능은 아님
- 프로젝트 보안 수준에 따라 trade-off가 있음
- 학습/프로젝트용과 실서비스 보안 기준은 구분
- token 노출 위험이 큰 화면 공유 / 로그 주의

---

### [FAQ]

Q. localStorage에 token을 저장하면 무조건 안 돼?

A.
무조건 금지는 아니지만 XSS에 노출될 수 있어 보안 요구사항에 따라 신중히 결정해야 한다.

Q. HttpOnly Cookie가 무조건 정답이야?

A.
항상 정답은 아니다. JS 접근 차단 장점이 있지만 CSRF, SameSite, Backend 설정 등 함께 고려해야 한다.

---

# 9. Axios Auth Integration Rules

## 9.1 Public API and Auth API

### [개념]

Public API와 Auth API를 분리하면 인증이 필요 없는 요청과 Authorization Header가 필요한 요청을 명확히 구분할 수 있다.

---

### [핵심]

구분:

- publicApi
- authApi
- baseURL
- Authorization Header
- request interceptor
- response interceptor
- authenticated endpoint
- public endpoint

---

### [실무]

예:

```tsx
import axios from "axios";

export const publicApi = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
});

export const authApi = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
});

authApi.interceptors.request.use((config) => {
  const token = getAccessToken();

  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  return config;
});
```

사용 예:

```tsx
export function getFestivals(params) {
  return publicApi.get("/festivals", { params });
}

export function getMyFavorites() {
  return authApi.get("/favorites");
}
```

주의:

- 인증 필요 API에 publicApi 사용 금지
- 공개 API에 불필요한 token 전송 지양
- instance import 기준 통일
- baseURL 중복 관리 금지
- response.data unwrap 기준 통일

---

### [FAQ]

Q. publicApi와 authApi를 나누는 이유는?

A.
인증이 필요 없는 요청과 Authorization Header가 필요한 요청을 명확히 구분하기 위해서다.

Q. 인증 API에 publicApi를 쓰면 어떻게 돼?

A.
Authorization Header가 누락되어 401이 발생할 수 있다.

---

## 9.2 Request Interceptor Rules

### [개념]

Request Interceptor는 API 요청이 서버로 전송되기 전에 Authorization Header 같은 공통 값을 추가하는 기능이다.

---

### [핵심]

사용 대상:

- access token attach
- Authorization Header
- request logging caution
- locale header
- request id basics
- credentials basics

---

### [실무]

예:

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

주의:

- token이 없으면 Header 생략
- token 로그 출력 금지
- Authorization spelling 확인
- Bearer prefix 확인
- interceptor에서 복잡한 비즈니스 로직 지양
- request interceptor가 여러 번 중복 등록되지 않도록 주의

---

### [FAQ]

Q. Authorization Header를 매 API 함수마다 넣어야 해?

A.
가능하지만 authApi request interceptor에서 공통 처리하는 것이 유지보수에 좋다.

Q. interceptor가 여러 번 실행돼?

A.
설정 코드가 여러 번 실행되어 interceptor가 중복 등록되면 같은 로직이 반복될 수 있다. 초기화 위치를 통일해야 한다.

---

## 9.3 Response Interceptor Rules

### [개념]

Response Interceptor는 서버 응답이나 에러를 Component로 전달하기 전에 공통 처리하는 기능이다.

401 처리, token refresh, 공통 에러 mapping에 사용할 수 있다.

---

### [핵심]

사용 대상:

- 401 handling
- 403 handling
- token refresh
- retry original request
- logout
- error normalization
- Promise.reject

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
    }

    return Promise.reject(error);
  },
);
```

주의:

- 에러를 삼키지 말고 Promise.reject로 전달
- 401 / 403 구분
- refresh token flow가 있으면 무한 loop 방지
- 원래 요청 retry는 제한
- login API / refresh API에는 별도 처리 필요 가능
- UI 메시지는 호출부에서 처리할 수 있게 유지

---

### [FAQ]

Q. Response Interceptor에서 401을 처리하면 Component에서는 에러 처리를 안 해도 돼?

A.
아니다. 공통 인증 처리는 interceptor에서 하고, 화면별 사용자 메시지는 Component나 hook에서 처리할 수 있다.

Q. interceptor에서 Promise.reject를 왜 해?

A.
호출한 API 함수나 화면에서도 에러를 인식하고 적절한 UI를 보여줄 수 있게 하기 위해서다.

---

# 10. Protected Route Rules

## 10.1 Protected Route Basics

### [개념]

Protected Route는 로그인하지 않은 사용자가 접근하면 로그인 페이지로 redirect하는 Frontend Route Guard다.

---

### [핵심]

필수 포함:

- protected route
- private route
- authenticated
- auth loading
- Navigate
- redirect
- previous location
- replace
- UX guard
- Backend security

---

### [실무]

예:

```tsx
function ProtectedRoute({ children }) {
  const { initialized, authenticated } = useAuth();
  const location = useLocation();

  if (!initialized) {
    return <p>Loading...</p>;
  }

  if (!authenticated) {
    return <Navigate to="/login" replace state={{ from: location.pathname }} />;
  }

  return children;
}
```

적용:

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

주의:

- auth initialized 전 redirect 금지
- redirect loop 방지
- Protected Route는 UX용
- Backend API 권한 검증 필수
- 이전 location 저장 가능
- replace 옵션으로 history 정리

---

### [FAQ]

Q. Protected Route는 보안적으로 충분해?

A.
아니다. Frontend Route 보호는 UX용이고 실제 보안은 Backend 인증/인가가 담당해야 한다.

Q. auth loading 중에는 어떻게 해?

A.
로그인 페이지로 보내지 말고 loading UI를 보여주며 인증 상태 확인이 끝날 때까지 기다리는 것이 좋다.

---

## 10.2 Public Only Route Rules

### [개념]

Public Only Route는 이미 로그인한 사용자가 login, signup 같은 페이지에 접근하지 못하도록 처리하는 Route다.

---

### [핵심]

사용 대상:

- login page
- signup page
- find password page
- OAuth2 callback basics
- already authenticated redirect

---

### [실무]

예:

```tsx
function PublicOnlyRoute({ children }) {
  const { initialized, authenticated } = useAuth();

  if (!initialized) {
    return <p>Loading...</p>;
  }

  if (authenticated) {
    return <Navigate to="/" replace />;
  }

  return children;
}
```

주의:

- 이미 로그인한 사용자의 login page 접근 기준 통일
- OAuth2 callback은 예외 처리가 필요할 수 있음
- redirect target 기준 명확화
- loading 중 redirect 금지

---

### [FAQ]

Q. 로그인한 사용자가 login 페이지에 접근하면 어떻게 해?

A.
보통 메인 페이지나 이전 페이지로 redirect한다.

Q. Public Only Route도 꼭 필요해?

A.
필수는 아니지만 로그인/회원가입 페이지 UX를 정리하는 데 유용하다.

---

## 10.3 Role Based Route Rules

### [개념]

Role Based Route는 사용자 role에 따라 접근 가능한 Route를 제한하는 Frontend Route Guard다.

---

### [핵심]

필수 포함:

- role
- ROLE_USER
- ROLE_ADMIN
- allowedRoles
- forbidden page
- Navigate
- Backend authorization
- role naming

---

### [실무]

예:

```tsx
function RoleRoute({ allowedRoles, children }) {
  const { user, initialized, authenticated } = useAuth();

  if (!initialized) {
    return <p>Loading...</p>;
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

주의:

- ROLE_ADMIN / ADMIN naming 혼용 금지
- Frontend role check는 UX용
- Backend API role check 필수
- role 정보가 없을 때 loading / error 처리
- 권한 없음은 403 UI와 연결 가능

---

### [FAQ]

Q. Frontend에서 ROLE_ADMIN을 확인하면 관리자 API가 안전해져?

A.
아니다. Frontend role check는 화면 접근 UX용이고 관리자 API는 Backend에서 반드시 권한 검증해야 한다.

Q. 권한 없는 사용자는 어디로 보내?

A.
프로젝트 기준에 따라 `/forbidden`, `/`, `/login` 중 하나로 보낼 수 있다. 기준을 통일해야 한다.

---

# 11. Role Based UI Rules

## 11.1 Role Based UI

### [개념]

Role Based UI는 사용자 권한에 따라 메뉴, 버튼, 링크, 페이지 일부를 다르게 보여주는 방식이다.

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

---

### [실무]

예:

```tsx
function Header() {
  const { authenticated, user } = useAuth();

  return (
    <header>
      <Link to="/">Home</Link>

      {authenticated && <Link to="/mypage">My Page</Link>}

      {user?.role === "ROLE_ADMIN" && <Link to="/admin">Admin</Link>}
    </header>
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

---

### [FAQ]

Q. 삭제 버튼을 작성자에게만 보여주면 충분해?

A.
아니다. 버튼 표시 제어는 UX용이고 실제 삭제 API는 Backend에서 작성자 여부를 검증해야 한다.

Q. role이 없을 때 UI가 깜빡여?

A.
Auth loading이 끝나기 전 조건부 렌더링이 실행되면 flicker가 생길 수 있다. initialized 상태를 사용해 제어한다.

---

# 12. Logout Flow Rules

## 12.1 Logout Flow

### [개념]

Logout Flow는 사용자의 인증 상태를 종료하고 token, user state, 관련 cache를 정리하는 흐름이다.

---

### [핵심]

기본 Flow:

```text
User Click Logout
→ Optional Logout API
→ Clear Token
→ Clear Auth State
→ Clear User-specific Cache
→ Redirect Main or Login
```

---

### [실무]

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

정리 대상:

- accessToken
- refreshToken
- user
- authenticated
- authStore
- notification state
- user-specific query cache
- private page state
- persisted auth storage

주의:

- logout API 실패해도 local auth 정리 여부 결정
- query cache에 사용자 데이터가 남지 않도록 처리
- 다른 탭 로그인 상태 동기화 필요 가능
- logout 후 protected page history 접근 방지
- replace 옵션 고려

---

### [FAQ]

Q. 로그아웃할 때 token만 지우면 돼?

A.
아니다. user state, authenticated 상태, 사용자별 cache, persisted store도 함께 정리해야 한다.

Q. logout API가 실패하면 local token을 유지해야 해?

A.
프로젝트 정책에 따라 다르지만 사용자 입장에서는 로그아웃을 요청했으므로 local 인증 정보를 정리하는 경우가 많다.

---

# 13. User Profile Fetch Rules

## 13.1 Me API Flow

### [개념]

Me API는 현재 로그인한 사용자의 정보를 조회하는 API다.

Frontend는 access token 또는 cookie 인증을 기반으로 `/me` API를 호출해 사용자 상태를 복원할 수 있다.

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

---

### [실무]

Flow:

```text
Stored Token Exists
→ Call /me
→ Success: Set User / Authenticated
→ 401: Clear Auth
→ 403: Show Forbidden or Clear Auth
```

예:

```tsx
export async function getMe() {
  const response = await authApi.get("/users/me");
  return response.data.data;
}
```

주의:

- `/me` API는 authApi 사용
- 로그인 직후 user 정보가 부족하면 `/me` 호출
- 새로고침 복원에서 `/me` 활용 가능
- 401이면 token 만료 또는 인증 실패
- 사용자 정보 DTO는 최소화
- role 정보 포함 여부 확인

---

### [FAQ]

Q. 로그인 응답에 user가 있는데 /me API도 필요해?

A.
항상 필요하지는 않다. 하지만 새로고침 후 인증 상태 복원이나 최신 사용자 정보 확인에는 유용하다.

Q. /me API가 401이면 어떻게 해?

A.
token이 유효하지 않은 상태로 보고 인증 정보를 정리하거나 refresh flow를 시도한다.

---

# 14. OAuth2 Frontend Flow Rules

## 14.1 OAuth2 Login Redirect Flow

### [개념]

OAuth2 Frontend Flow는 사용자가 소셜 로그인 버튼을 클릭하고 OAuth2 Provider 인증을 거친 뒤 Frontend callback에서 인증 결과를 처리하는 흐름이다.

---

### [핵심]

기본 Flow:

```text
Click Social Login
→ Redirect Backend OAuth2 Authorization Endpoint
→ Provider Login
→ Backend OAuth2 Success
→ Redirect Frontend Callback
→ Frontend Receive Token or Code Result
→ Store Auth State
→ Navigate
```

---

### [실무]

소셜 로그인 버튼 예:

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

주의:

- OAuth2 시작 URL은 Backend 기준
- Frontend가 provider secret을 가지면 안 됨
- callback URL 기준 명확화
- token을 query string으로 전달할 경우 노출 위험 검토
- code / state / token 처리 방식은 Backend 설계에 따름
- OAuth2 실패 callback 처리 필요

---

### [FAQ]

Q. 소셜 로그인 버튼은 Frontend에서 뭘 해?

A.
대부분 Backend OAuth2 authorization endpoint로 redirect한다.

Q. Kakao client secret을 Frontend에 넣어도 돼?

A.
안 된다. Frontend에 secret을 넣으면 노출된다. secret은 Backend에서 관리해야 한다.

---

## 14.2 OAuth2 Callback Handling

### [개념]

OAuth2 Callback Handling은 OAuth2 로그인 성공 또는 실패 후 Frontend가 전달받은 결과를 처리하는 흐름이다.

---

### [핵심]

처리 대상:

- access token
- refresh token
- auth code
- error
- redirect target
- query string
- hash fragment
- user info fetch
- token cleanup from URL

---

### [실무]

Flow:

```text
Callback Page Mount
→ Read Query Params
→ Validate Result
→ Store Token or Exchange Code
→ Fetch /me if Needed
→ Clean URL
→ Redirect Main or Previous Page
```

예:

```tsx
function OAuthCallbackPage() {
  const [searchParams] = useSearchParams();
  const navigate = useNavigate();

  useEffect(() => {
    const accessToken = searchParams.get("accessToken");
    const error = searchParams.get("error");

    if (error) {
      navigate("/login", { replace: true });
      return;
    }

    if (accessToken) {
      setAccessToken(accessToken);
      navigate("/", { replace: true });
    }
  }, [searchParams, navigate]);

  return <p>로그인 처리 중...</p>;
}
```

주의:

- URL에 token이 남지 않도록 replace 이동
- error param 처리
- token 전달 방식 보안 검토
- callback 처리 중 loading UI 제공
- 중복 처리 방지
- Backend와 callback parameter 이름 통일

---

### [FAQ]

Q. OAuth2 callback에서 token을 URL로 받으면 어떻게 해?

A.
즉시 저장 또는 처리한 뒤 replace navigation으로 URL에서 token을 제거하는 것이 좋다. 보안상 token 전달 방식도 Backend와 검토해야 한다.

Q. OAuth2 callback에서 에러가 오면?

A.
login 페이지로 이동하고 사용자에게 로그인 실패 메시지를 보여준다.

---

# 15. 401 / 403 Error Handling Rules

## 15.1 401 Handling

### [개념]

401 Unauthorized는 사용자가 인증되지 않았거나 access token이 유효하지 않을 때 발생하는 응답이다.

---

### [핵심]

원인:

- token 없음
- token 만료
- token 위조
- Bearer 형식 오류
- Authorization Header 누락
- refresh 실패
- 로그인 필요 API 접근

처리:

- refresh token 시도
- refresh 실패 시 logout
- login redirect
- auth state clear
- 사용자 메시지 표시
- 원래 요청 retry

---

### [실무]

401 처리 Flow:

```text
Receive 401
→ Check Refresh Available
→ If Refresh Success Retry Request
→ If Refresh Fail Clear Auth
→ Redirect Login
```

주의:

- 모든 401을 즉시 login redirect하면 UX가 나쁠 수 있음
- refresh endpoint의 401은 재시도 금지
- 반복 retry 방지
- login API 실패 401과 token 만료 401 구분
- 호출 화면에서 사용자 메시지 처리 가능

---

### [FAQ]

Q. 401이 나오면 무조건 로그아웃해야 해?

A.
refresh token flow가 있으면 먼저 재발급을 시도할 수 있다. 재발급 실패 시 로그아웃 처리한다.

Q. 로그인 실패도 401이야?

A.
Backend 설계에 따라 그럴 수 있다. 로그인 실패 401과 기존 세션 만료 401을 처리 흐름에서 구분해야 한다.

---

## 15.2 403 Handling

### [개념]

403 Forbidden은 사용자가 인증은 되었지만 해당 리소스나 기능에 접근할 권한이 없을 때 발생하는 응답이다.

---

### [핵심]

원인:

- role 부족
- 관리자 권한 없음
- 작성자 / 소유자 불일치
- 접근 금지 리소스
- Backend Authorization 실패

처리:

- Forbidden Page 표시
- 권한 없음 메시지 표시
- 이전 페이지 이동
- 관리자 문의 안내
- logout과 구분

---

### [실무]

403 처리 기준:

```text
Receive 403
→ Do Not Clear Auth by Default
→ Show Forbidden Message
→ Navigate Forbidden Page or Previous Page
```

주의:

- 403을 login redirect로 처리하지 않음
- 인증 상태는 유지될 수 있음
- role 정보가 오래되었는지 확인 가능
- Backend 권한 기준 확인
- 사용자에게 과도한 내부 권한 정보 노출 금지

---

### [FAQ]

Q. 403이면 로그아웃해야 해?

A.
대부분 아니다. 인증은 되었지만 권한이 없는 상태이므로 권한 없음 화면이나 메시지를 보여주는 것이 일반적이다.

Q. 403과 401을 같은 방식으로 처리해도 돼?

A.
권장하지 않는다. 401은 인증 문제, 403은 권한 문제다.

---

# 16. Auth Troubleshooting Rules

## 16.1 Token Missing Troubleshooting

### [개념]

Token Missing 문제는 인증 API 요청에 token이 포함되지 않아 401이 발생하는 상황이다.

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
→ interceptor 등록 여부 확인
→ login response mapping 확인
```

주의:

- token이 저장되어도 Header에 없으면 인증 실패
- publicApi로 요청하면 header 누락 가능
- interceptor 설정 파일 import 누락 가능
- token 저장 전 API 요청이 먼저 발생할 수 있음
- token 로그 출력은 주의

---

### [FAQ]

Q. localStorage에 token이 있는데 401이 나?

A.
Network 탭에서 Authorization Header에 실제로 token이 포함되었는지 확인해야 한다.

Q. Bearer를 빼먹으면 어떻게 돼?

A.
Backend가 token 형식을 인식하지 못해 401이 발생할 수 있다.

---

## 16.2 Refresh Loop Troubleshooting

### [개념]

Refresh Loop는 token 재발급 로직이 실패하거나 조건이 잘못되어 refresh 요청이 반복되는 문제다.

---

### [핵심]

원인:

- refresh API도 interceptor 대상
- `_retry` 플래그 없음
- refresh 실패 후 clearAuth 누락
- 동일 401 요청 무한 재시도
- refresh token 만료
- 여러 요청 동시 401 처리 미흡

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
```

주의:

- refresh 요청은 재귀 refresh 대상에서 제외
- 원래 요청 retry는 1회 제한
- refresh 실패 시 즉시 auth 정리
- 여러 요청 동시 만료 처리 기준 필요
- 무한 loop는 사용자 경험과 서버 부하 모두 악화

---

### [FAQ]

Q. refresh 요청이 계속 반복돼?

A.
refresh API까지 401 interceptor가 재시도 대상으로 잡혔거나 retry 제한이 없을 가능성이 있다.

Q. 여러 API가 동시에 401이면 어떻게 해?

A.
refresh 요청을 하나만 수행하고 나머지 요청은 대기시킨 뒤 새 token으로 재시도하는 queue 방식이 필요할 수 있다.

---

## 16.3 Auth Redirect Loop Troubleshooting

### [개념]

Auth Redirect Loop는 login page와 protected page 사이에서 redirect가 반복되는 문제다.

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

---

### [실무]

Debug Flow:

```text
Current Route 확인
→ Auth State 확인
→ initialized 확인
→ authenticated 확인
→ user null 여부 확인
→ Route Guard 조건 확인
→ Navigate target 확인
```

주의:

- 초기 인증 확인 전 redirect하지 않음
- login route는 protected로 감싸지 않음
- 이미 로그인한 사용자의 login 접근 처리 기준 명확화
- Navigate replace 사용 고려
- redirect target이 다시 guard에 걸리는지 확인

---

### [FAQ]

Q. login과 mypage 사이를 계속 왔다 갔다 해?

A.
auth initialized 전에 redirect하거나 ProtectedRoute와 PublicOnlyRoute 조건이 충돌했을 가능성이 크다.

Q. token은 있는데 login으로 보내져?

A.
user 정보 복원 전 authenticated를 false로 판단했거나 `/me` 확인 loading을 기다리지 않았을 수 있다.

---

## 16.4 Role UI Not Updating

### [개념]

Role UI Not Updating은 사용자 권한 변경이나 로그인 상태 변화 후 메뉴 / 버튼 / route 접근이 갱신되지 않는 문제다.

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

---

### [실무]

Debug Flow:

```text
Auth User 확인
→ role 값 확인
→ Conditional Rendering 조건 확인
→ /me 응답 확인
→ Store 업데이트 확인
→ Role naming 확인
→ Cache invalidate 확인
```

주의:

- role 값은 Backend와 naming 통일
- 권한 변경 후 `/me` refetch 필요 가능
- UI 숨김과 API 권한 검증은 별개
- user null 상태 처리

---

### [FAQ]

Q. 관리자 계정인데 관리자 메뉴가 안 보여?

A.
user.role 값, role naming, Auth State 업데이트, 조건부 렌더링 조건을 확인해야 한다.

Q. ROLE_ADMIN과 ADMIN은 같은 거야?

A.
프로젝트 기준에 따라 다르지만 문자열이 다르면 조건문에서 다르게 처리된다. naming을 통일해야 한다.

---

# 17. Security Rules

## 17.1 Frontend Auth Security Basics

### [개념]

Frontend Auth Security는 인증 흐름에서 민감정보 노출과 잘못된 신뢰를 줄이기 위한 기본 기준이다.

---

### [핵심]

주의 대상:

- password
- access token
- refresh token
- Authorization Header
- user personal data
- localStorage
- sessionStorage
- URL query token
- console log
- XSS
- CSRF
- API secret

---

### [실무]

기준:

- password 로그 출력 금지
- token 로그 출력 금지
- API Secret을 Frontend에 저장 금지
- Frontend .env에 secret 저장 금지
- URL에 token 노출 시 즉시 제거
- 민감정보를 Auth State에 과도하게 저장하지 않음
- Frontend role check를 보안으로 착각하지 않음
- Backend 인증/인가가 최종 보안 기준
- OAuth provider secret은 Backend에서 관리
- token 저장 위치는 보안 요구사항에 따라 결정

---

### [FAQ]

Q. Frontend .env에 OAuth secret을 넣어도 돼?

A.
안 된다. Frontend 환경변수는 빌드 결과에 노출될 수 있으므로 secret을 넣으면 안 된다.

Q. token을 console.log로 찍어도 돼?

A.
안 된다. token은 인증에 사용되는 민감정보이므로 로그에 남기지 않는 것이 원칙이다.

---

# 18. Comparison Rules

## 18.1 Required Comparisons

### [개념]

Authentication Frontend Flow 문서는 헷갈리는 인증 개념을 비교해서 작성한다.

---

### [핵심]

필수 비교 대상:

- Authentication vs Authorization
- 401 vs 403
- Access Token vs Refresh Token
- Login State vs User Profile
- Protected Route vs Backend Authorization
- Public Route vs Protected Route
- PublicOnlyRoute vs ProtectedRoute
- Role Based Route vs Role Based UI
- localStorage vs sessionStorage vs HttpOnly Cookie
- Authorization Header vs Cookie Auth
- Token Expired vs Logged Out
- OAuth2 Redirect Login vs Normal Login
- Client Validation vs Backend Auth Validation
- Auth Loading vs API Loading

---

### [실무]

예시:

| 비교        | Protected Route   | Backend Authorization |
| ----------- | ----------------- | --------------------- |
| 위치        | Frontend          | Backend               |
| 목적        | 화면 접근 UX 제어 | 실제 API 보안         |
| 우회 가능성 | 가능              | 서버 검증             |
| 예          | /mypage redirect  | JWT / Role 검증       |
| 중요도      | 사용자 경험       | 보안 필수             |

---

### [FAQ]

Q. 비교 표는 왜 필요해?

A.
사용자가 자주 헷갈리는 인증 질문에서 Retrieval Hit와 답변 정확도를 높이기 위해 필요하다.

Q. Authentication 비교 문서에서 가장 중요한 것은?

A.
Frontend UX 처리와 Backend 보안 책임을 명확히 구분하는 것이다.

---

# 19. Checklist Rules

## 19.1 Authentication Frontend Checklist

### [개념]

Authentication Frontend Flow 문서 검수 시 인증 흐름 체크리스트를 사용한다.

---

### [핵심]

Checklist:

```md
- [ ] Authentication / Authorization 차이가 포함되었는가?
- [ ] Login Flow가 포함되었는가?
- [ ] Signup Flow가 포함되었는가?
- [ ] Auth State 구조가 포함되었는가?
- [ ] Auth Loading / Initialized 기준이 포함되었는가?
- [ ] Access Token 처리 기준이 포함되었는가?
- [ ] Refresh Token 기초 기준이 포함되었는가?
- [ ] Authorization Header 기준이 포함되었는가?
- [ ] Axios Request Interceptor 기준이 포함되었는가?
- [ ] Axios Response Interceptor 기준이 포함되었는가?
- [ ] Protected Route 기준이 포함되었는가?
- [ ] PublicOnlyRoute 기준이 포함되었는가?
- [ ] Role Based Route / UI 기준이 포함되었는가?
- [ ] Logout Cleanup 기준이 포함되었는가?
- [ ] /me API 인증 복원 기준이 포함되었는가?
- [ ] OAuth2 Callback 기초가 포함되었는가?
- [ ] 401 / 403 처리 기준이 포함되었는가?
- [ ] Auth Troubleshooting이 포함되었는가?
- [ ] Security 주의사항이 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 기준:

```text
Draft
→ Auth Concept Check
→ Login Flow Check
→ Token Handling Check
→ Auth State Check
→ Route Guard Check
→ Axios Interceptor Check
→ 401 / 403 Check
→ Logout Cleanup Check
→ Security Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

---

### [FAQ]

Q. Authentication 문서 검수에서 가장 중요한 것은?

A.
Auth State, token 처리, Protected Route, Authorization Header, 401 / 403 처리, Backend 보안 책임 구분 포함 여부다.

---

# 20. Retrieval Optimization Rules

## 20.1 Keyword Rules

### [개념]

Authentication Frontend Flow 문서는 검색 매칭을 위해 핵심 키워드를 반복 허용한다.

---

### [핵심]

강조 키워드:

- Authentication Frontend Flow
- Frontend Authentication
- Login Flow
- Logout Flow
- Signup Flow
- Auth State
- Auth Loading
- Initialized
- Access Token
- Refresh Token
- Authorization Header
- Bearer Token
- Axios Interceptor
- Request Interceptor
- Response Interceptor
- 401 Unauthorized
- 403 Forbidden
- Protected Route
- Private Route
- PublicOnlyRoute
- Role Based Route
- Role Based UI
- ROLE_USER
- ROLE_ADMIN
- User Profile
- Me API
- Auth Restore
- Token Expired
- Token Refresh
- Redirect After Login
- OAuth2 Frontend Flow
- OAuth2 Callback
- Social Login
- Auth Troubleshooting
- Frontend Auth Security

---

### [실무]

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

예:

- 로그인 성공 후 뭘 해야 해?
- token은 어디에 저장해?
- Authorization Header는 어떻게 넣어?
- token은 있는데 401이 나?
- 401과 403 차이는?
- 새로고침하면 로그인이 풀려?
- Protected Route는 어떻게 만들어?
- 로그인 후 원래 페이지로 돌아가려면?
- 로그아웃할 때 뭘 지워야 해?
- refresh token은 어떻게 처리해?
- 관리자 메뉴는 어떻게 숨겨?
- Frontend에서 role check하면 보안이 돼?
- OAuth2 callback은 어떻게 처리해?
- localStorage에 token 저장해도 돼?

---

### [FAQ]

Q. 키워드 반복은 중복이야?

A.
불필요한 장문 중복은 금지지만 Retrieval 최적화를 위한 핵심 키워드 반복은 허용된다.

Q. FAQ 질문은 어떤 스타일이 좋아?

A.
실제 사용자가 검색하거나 질문할 법한 문장형 질문이 좋다.

---

# 21. Version Rules

## 21.1 Modern Authentication Frontend 기준

### [개념]

Authentication Frontend Flow 문서는 Modern React Frontend 인증 흐름 기준으로 작성한다.

---

### [핵심]

기준:

- React 18+
- React 19 호환 고려
- Functional Component
- Hook 기반 Auth State
- React Router v6+
- Protected Route
- Axios Instance
- Axios Interceptor
- REST API Auth
- JWT Based Auth Awareness
- OAuth2 Redirect Awareness
- TypeScript Ready Auth Type
- Backend Authorization Required
- Security Caution Included

Legacy 제외:

- jQuery AJAX 로그인 중심 설명
- token을 전역 변수에만 저장하는 방식
- class component auth guard 중심 설명
- Frontend role check를 보안으로 간주
- password / token console.log
- 모든 인증 상태를 localStorage에 무분별하게 저장
- 401 / 403 동일 처리
- auth loading 없이 즉시 redirect
- OAuth secret을 Frontend에 저장

---

### [실무]

실무 기준:

```text
Modern Frontend Auth
→ Login API
→ Token Handling
→ Auth State
→ Authenticated API
→ Protected Route
→ Refresh / Logout
→ Security Review
```

---

### [FAQ]

Q. React에서 인증은 무조건 Redux로 해야 해?

A.
아니다. 프로젝트 규모에 따라 Context, Zustand, Redux Toolkit, TanStack Query 조합 중 선택할 수 있다.

Q. class component 방식 auth guard도 다뤄?

A.
신규 문서에서는 Functional Component와 Hook 기반 인증 흐름을 우선한다.

---

# 22. Common Mistakes

## 22.1 Authentication Common Mistakes

### [개념]

Authentication Frontend Flow 문서는 자주 발생하는 인증 구현 실수를 명확히 포함해야 한다.

---

### [핵심]

자주 발생:

- password를 console.log로 출력
- token을 console.log로 출력
- Authorization Header 누락
- Bearer prefix 누락
- publicApi로 인증 API 호출
- token 저장 후 Auth State 업데이트 누락
- user state와 token 상태 불일치
- 새로고침 후 인증 복원 로직 없음
- auth loading 없이 Protected Route redirect
- redirect loop 발생
- 401과 403을 같은 방식으로 처리
- 403에서 logout 처리
- refresh token 무한 loop
- refresh API도 interceptor retry 대상에 포함
- logout 시 query cache 정리 누락
- Role naming 혼용
- Frontend role check를 보안으로 착각
- OAuth secret을 Frontend에 저장
- OAuth callback URL에 token을 남겨둠
- localStorage token 저장 위험을 고려하지 않음
- Backend 인증/인가 없이 Frontend만 막음

---

### [실무]

문서 작성 시 Common Mistakes는 Troubleshooting과 연결한다.

예:

```text
문제: token은 있는데 401 발생
원인: Authorization Header에 token이 포함되지 않음
해결: Network 탭에서 Request Header 확인 후 authApi interceptor와 Bearer 형식 점검
```

---

### [FAQ]

Q. Authentication 초보가 가장 많이 하는 실수는?

A.
Authorization Header 누락, auth loading 미처리, token 저장과 user state 불일치, 401 / 403 혼동이 많다.

Q. Auth 문제는 어떻게 찾는 게 좋아?

A.
Network Header, Status Code, Auth State, token 저장 여부, Route Guard 조건, Backend Security 로그를 순서대로 확인한다.

---

# 23. Final Goal

## 23.1 Domain Final Goal

### [개념]

Authentication Frontend Flow RAG 문서는 Frontend Agent가 로그인부터 인증 API 호출, Route 보호, token 만료 처리, 로그아웃까지 일관된 인증 흐름을 설계하고 검토하도록 지원해야 한다.

---

### [핵심]

최종 목표:

- Authentication / Authorization 구분
- Login Flow 설계
- Signup Flow 설계
- Login Response 처리
- Auth State 설계
- Auth Loading / Initialized 처리
- Access Token 처리
- Refresh Token 기초 처리
- Authorization Header 적용
- Axios Request Interceptor 설계
- Axios Response Interceptor 설계
- Protected Route 구현
- PublicOnlyRoute 구현
- Role Based Route 구현
- Role Based UI 구현
- Redirect After Login 구현
- Logout Cleanup 구현
- Me API 인증 복원 구현
- OAuth2 Frontend Flow 이해
- OAuth2 Callback 처리
- 401 / 403 처리
- Token Expired 처리
- Auth Troubleshooting 수행
- Frontend Auth Security 검토

---

### [실무]

Agent 수행 가능 작업:

```text
User Auth Request
→ Identify Auth Scenario
→ Define Login / Logout Flow
→ Define Auth State
→ Define Token Handling
→ Configure Authorization Header
→ Add Protected Route
→ Add Role Based UI
→ Handle 401 / 403
→ Check Security Risks
→ Authentication Frontend Output
```

---

### [FAQ]

Q. Authentication Frontend Flow 문서의 최종 목적은 뭐야?

A.
Frontend Agent가 인증 상태, token, route guard, 인증 API, 401 / 403, logout cleanup을 일관되게 설계하게 만드는 것이다.

Q. 이 문서 다음에는 어떤 Domain Rules가 이어져야 해?

A.
Error Handling & Loading UX, Frontend Testing, Frontend Accessibility, Frontend Build & Deploy 순서로 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. Authentication Frontend Flow 문서는 왜 필요해?
A. Frontend Agent가 로그인, token 처리, 인증 API 요청, Protected Route, 로그아웃 흐름을 안정적으로 구현해야 하기 때문이다.

Q. Authentication과 Authorization 차이는?
A. Authentication은 사용자가 누구인지 확인하는 것이고 Authorization은 그 사용자가 접근 권한이 있는지 확인하는 것이다.

Q. 401과 403 차이는?
A. 401은 인증 실패 또는 로그인 필요이고 403은 인증은 되었지만 권한이 부족한 경우다.

Q. Frontend 인증 처리는 보안이야 UX야?
A. Frontend 인증 처리는 주로 UX용이고 실제 보안은 Backend 인증/인가가 담당해야 한다.

Q. Frontend에서 로그인 상태를 확인하면 보안이 돼?
A. 아니다. Frontend 인증 상태는 화면 제어용이고 실제 API 접근 권한은 Backend에서 검증해야 한다.

Q. 로그인 성공 후 뭘 해야 해?
A. token을 처리하고 user state를 갱신한 뒤 인증 상태를 true로 만들고 적절한 페이지로 redirect한다.

Q. 로그인 응답에 user 정보가 없으면 어떻게 해?
A. 로그인 성공 후 access token으로 `/me` 또는 사용자 정보 조회 API를 호출해 Auth State를 채울 수 있다.

Q. 로그인 실패 메시지는 어떻게 보여줘?
A. 계정 정보 불일치는 global form error로 표시하고 이메일 형식 오류 같은 입력 문제는 field error로 처리한다.

Q. password를 console.log로 확인해도 돼?
A. 안 된다. 비밀번호는 민감정보이므로 로그에 남기지 않는다.

Q. 로그인 후 원래 보려던 페이지로 돌아가려면?
A. Protected Route에서 location state나 query string에 이전 경로를 저장하고 로그인 성공 후 해당 경로로 navigate한다.

Q. redirect loop는 왜 생겨?
A. 인증 상태 loading을 기다리지 않거나 login page와 protected page가 서로 redirect 조건에 걸릴 때 발생한다.

Q. 회원가입 성공 후 자동 로그인해야 해?
A. 프로젝트 정책에 따라 다르다. 자동 로그인하려면 로그인 응답과 동일하게 token과 user state를 처리해야 한다.

Q. 이메일 중복 검사는 Frontend에서 가능해?
A. 형식 검사는 Frontend에서 가능하지만 실제 중복 여부는 Backend API 기준으로 확인해야 한다.

Q. Auth State에는 무엇이 들어가?
A. authenticated, initialized, loading, user, role, authError 같은 인증 상태 정보가 들어갈 수 있다.

Q. token이 있으면 authenticated true로 해도 돼?
A. 가능은 하지만 token이 만료되었거나 위조되었을 수 있으므로 `/me` 같은 API로 확인하는 흐름이 더 안전하다.

Q. auth loading은 왜 필요해?
A. 새로고침 후 인증 상태 확인 전에 Protected Route가 login으로 잘못 redirect하는 것을 막기 위해 필요하다.

Q. 새로고침하면 로그인이 풀려?
A. Auth State가 memory에만 있거나 초기 인증 복원 로직이 없으면 새로고침 시 로그인이 풀릴 수 있다.

Q. 새로고침 후 바로 login으로 튕겨?
A. 인증 상태 확인 loading을 기다리지 않고 Protected Route가 먼저 redirect했을 가능성이 있다.

Q. token은 localStorage에 저장하면 돼?
A. 가능은 하지만 XSS 위험이 있다. 프로젝트 보안 요구사항에 따라 memory, sessionStorage, HttpOnly Cookie 등을 검토해야 한다.

Q. user 정보를 전부 저장해도 돼?
A. 권장하지 않는다. UI에 필요한 최소한의 user summary만 저장하는 것이 좋다.

Q. Authorization Header 형식은 뭐야?
A. 일반적으로 `Authorization: Bearer <accessToken>` 형식을 사용한다.

Q. token은 있는데 401이 나?
A. Authorization Header에 실제로 포함되었는지, Bearer 형식이 맞는지, token이 만료되지 않았는지 확인해야 한다.

Q. Bearer를 빼먹으면 어떻게 돼?
A. Backend가 token 형식을 인식하지 못해 401이 발생할 수 있다.

Q. access token이 만료되면 어떻게 해?
A. refresh token이 있으면 새 access token을 요청하고 성공 시 원래 API 요청을 재시도할 수 있다.

Q. refresh 요청도 실패하면?
A. 인증 정보를 정리하고 login 페이지로 이동시키는 것이 일반적이다.

Q. refresh 요청이 무한 반복될 수 있어?
A. 잘못 구현하면 가능하다. refresh 요청 자체에는 retry를 걸지 않거나 `_retry` 같은 플래그로 반복을 막아야 한다.

Q. localStorage에 token을 저장하면 무조건 안 돼?
A. 무조건 금지는 아니지만 XSS에 노출될 수 있어 보안 요구사항에 따라 신중히 결정해야 한다.

Q. HttpOnly Cookie가 무조건 정답이야?
A. 항상 정답은 아니다. JS 접근 차단 장점이 있지만 CSRF, SameSite, Backend 설정 등 함께 고려해야 한다.

Q. publicApi와 authApi를 나누는 이유는?
A. 인증이 필요 없는 요청과 Authorization Header가 필요한 요청을 명확히 구분하기 위해서다.

Q. 인증 API에 publicApi를 쓰면 어떻게 돼?
A. Authorization Header가 누락되어 401이 발생할 수 있다.

Q. Authorization Header를 매 API 함수마다 넣어야 해?
A. 가능하지만 authApi request interceptor에서 공통 처리하는 것이 유지보수에 좋다.

Q. Axios Interceptor는 언제 써?
A. Authorization Header 추가, 401 처리, token refresh 같은 공통 인증 로직이 필요할 때 사용한다.

Q. interceptor에서 Promise.reject를 왜 해?
A. 호출한 API 함수나 화면에서도 에러를 인식하고 적절한 UI를 보여줄 수 있게 하기 위해서다.

Q. Protected Route는 어떻게 만들어?
A. 인증 상태를 확인하고 비로그인 상태면 Navigate로 login 페이지에 redirect한다.

Q. Protected Route는 보안적으로 충분해?
A. 아니다. Frontend Route 보호는 UX용이고 실제 보안은 Backend 인증/인가가 담당해야 한다.

Q. auth loading 중에는 어떻게 해?
A. 로그인 페이지로 보내지 말고 loading UI를 보여주며 인증 상태 확인이 끝날 때까지 기다리는 것이 좋다.

Q. 로그인한 사용자가 login 페이지에 접근하면 어떻게 해?
A. 보통 메인 페이지나 이전 페이지로 redirect한다.

Q. Role Based Route는 어떻게 만들어?
A. user.role이 allowedRoles에 포함되는지 확인하고 권한이 없으면 forbidden page로 redirect한다.

Q. Frontend에서 ROLE_ADMIN을 확인하면 관리자 API가 안전해져?
A. 아니다. Frontend role check는 화면 접근 UX용이고 관리자 API는 Backend에서 반드시 권한 검증해야 한다.

Q. 권한 없는 사용자는 어디로 보내?
A. 프로젝트 기준에 따라 `/forbidden`, `/`, `/login` 중 하나로 보낼 수 있다. 기준을 통일해야 한다.

Q. 관리자 메뉴는 어떻게 숨겨?
A. Auth State의 user.role을 확인해 ROLE_ADMIN일 때만 메뉴를 렌더링한다.

Q. 삭제 버튼을 작성자에게만 보여주면 충분해?
A. 아니다. 버튼 표시 제어는 UX용이고 실제 삭제 API는 Backend에서 작성자 여부를 검증해야 한다.

Q. role이 없을 때 UI가 깜빡여?
A. Auth loading이 끝나기 전 조건부 렌더링이 실행되면 flicker가 생길 수 있다. initialized 상태를 사용해 제어한다.

Q. 로그아웃할 때 token만 지우면 돼?
A. 아니다. user state, authenticated 상태, 사용자별 cache, persisted store도 함께 정리해야 한다.

Q. logout API가 실패하면 local token을 유지해야 해?
A. 프로젝트 정책에 따라 다르지만 사용자 입장에서는 로그아웃을 요청했으므로 local 인증 정보를 정리하는 경우가 많다.

Q. /me API는 언제 써?
A. 새로고침 후 인증 상태 복원, 로그인 응답에 사용자 정보가 부족한 경우, 최신 user profile 확인에 사용한다.

Q. /me API가 401이면 어떻게 해?
A. token이 유효하지 않은 상태로 보고 인증 정보를 정리하거나 refresh flow를 시도한다.

Q. 소셜 로그인 버튼은 Frontend에서 뭘 해?
A. 대부분 Backend OAuth2 authorization endpoint로 redirect한다.

Q. Kakao client secret을 Frontend에 넣어도 돼?
A. 안 된다. Frontend에 secret을 넣으면 노출된다. secret은 Backend에서 관리해야 한다.

Q. OAuth2 callback에서 token을 URL로 받으면 어떻게 해?
A. 즉시 저장 또는 처리한 뒤 replace navigation으로 URL에서 token을 제거하는 것이 좋다. 보안상 token 전달 방식도 Backend와 검토해야 한다.

Q. OAuth2 callback에서 에러가 오면?
A. login 페이지로 이동하고 사용자에게 로그인 실패 메시지를 보여준다.

Q. 401이 나오면 무조건 로그아웃해야 해?
A. refresh token flow가 있으면 먼저 재발급을 시도할 수 있다. 재발급 실패 시 로그아웃 처리한다.

Q. 403이면 로그아웃해야 해?
A. 대부분 아니다. 인증은 되었지만 권한이 없는 상태이므로 권한 없음 화면이나 메시지를 보여주는 것이 일반적이다.

Q. 403과 401을 같은 방식으로 처리해도 돼?
A. 권장하지 않는다. 401은 인증 문제, 403은 권한 문제다.

Q. localStorage에 token이 있는데 401이 나?
A. Network 탭에서 Authorization Header에 실제로 token이 포함되었는지 확인해야 한다.

Q. refresh 요청이 계속 반복돼?
A. refresh API까지 401 interceptor가 재시도 대상으로 잡혔거나 retry 제한이 없을 가능성이 있다.

Q. login과 mypage 사이를 계속 왔다 갔다 해?
A. auth initialized 전에 redirect하거나 ProtectedRoute와 PublicOnlyRoute 조건이 충돌했을 가능성이 크다.

Q. token은 있는데 login으로 보내져?
A. user 정보 복원 전 authenticated를 false로 판단했거나 `/me` 확인 loading을 기다리지 않았을 수 있다.

Q. 관리자 계정인데 관리자 메뉴가 안 보여?
A. user.role 값, role naming, Auth State 업데이트, 조건부 렌더링 조건을 확인해야 한다.

Q. ROLE_ADMIN과 ADMIN은 같은 거야?
A. 프로젝트 기준에 따라 다르지만 문자열이 다르면 조건문에서 다르게 처리된다. naming을 통일해야 한다.

Q. Frontend .env에 OAuth secret을 넣어도 돼?
A. 안 된다. Frontend 환경변수는 빌드 결과에 노출될 수 있으므로 secret을 넣으면 안 된다.

Q. token을 console.log로 찍어도 돼?
A. 안 된다. token은 인증에 사용되는 민감정보이므로 로그에 남기지 않는 것이 원칙이다.

Q. React에서 인증은 무조건 Redux로 해야 해?
A. 아니다. 프로젝트 규모에 따라 Context, Zustand, Redux Toolkit, TanStack Query 조합 중 선택할 수 있다.

Q. Authentication 초보가 가장 많이 하는 실수는?
A. Authorization Header 누락, auth loading 미처리, token 저장과 user state 불일치, 401 / 403 혼동이 많다.

Q. Auth 문제는 어떻게 찾는 게 좋아?
A. Network Header, Status Code, Auth State, token 저장 여부, Route Guard 조건, Backend Security 로그를 순서대로 확인한다.

Q. Authentication Frontend Flow 다음 문서는 뭐가 좋아?
A. Error Handling & Loading UX, Frontend Testing, Frontend Accessibility, Frontend Build & Deploy 순서가 좋다.
