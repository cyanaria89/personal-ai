# Authentication Frontend Flow Part01 - Overview / Responsibility / Scope

---

# 1. Authentication Frontend Flow Overview

## 1.1 Domain Purpose

### [개념]

Authentication Frontend Flow는 React Frontend에서 로그인 상태, token 처리, 인증 API 요청, Route 보호, 권한 UI 분기, 인증 오류 처리를 일관되게 설계하기 위한 Frontend 인증 흐름 문서다.

이 문서는 Backend Security 구현 문서가 아니다.

Frontend Agent / Review Agent / PM Agent가 인증 관련 화면과 API 연동을 설계하고 검수할 때 참조하는 RAG 문서다.

---

### [핵심]

- Authentication Frontend Flow
- Frontend Authentication
- Login Flow
- Logout Flow
- Signup Flow
- Auth State
- Auth Loading
- Access Token
- Refresh Token
- Authorization Header
- Bearer Token
- Axios Interceptor
- Protected Route
- Role Based UI
- 401 Unauthorized
- 403 Forbidden
- OAuth2 Callback
- Frontend Auth Security
- Backend Authorization Required

---

### [실무]

2026 실무 기준에서 Frontend 인증 문서는 단순 Login Form 구현 문서가 아니다.

Frontend Agent는 아래 흐름을 설계할 수 있어야 한다.

```text
User Login
→ Login API Request
→ Receive Access Token / Refresh Token / User Summary
→ Store Auth Result
→ Update Auth State
→ Attach Authorization Header
→ Access Protected Route
→ Handle 401 / 403
→ Logout Cleanup
```

Frontend 인증 문서는 아래 작업을 지원한다.

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

Q. Authentication Frontend Flow 문서는 왜 필요해?
A. Frontend Agent가 로그인, token 처리, 인증 API 요청, Protected Route, 로그아웃 흐름을 안정적으로 구현해야 하기 때문이다.

Q. 이 문서는 Login Form 문서야?
A. 아니다. Login Form뿐 아니라 Auth State, Token Handling, Authorization Header, Protected Route, 401 / 403, OAuth2 Callback까지 포함하는 인증 흐름 문서다.

Q. 이 문서는 Backend Security 문서야?
A. 아니다. Backend 인증/인가 구현은 Security Domain에서 다루고 이 문서는 Frontend 인증 UX와 API 연동 흐름에 집중한다.

---

# 2. Authentication and Authorization

## 2.1 Authentication vs Authorization

### [개념]

Authentication은 사용자가 누구인지 확인하는 과정이다.

Authorization은 인증된 사용자가 특정 기능이나 리소스에 접근할 권한이 있는지 확인하는 과정이다.

Frontend에서는 Authentication과 Authorization을 화면 흐름과 UX 제어에 사용하지만, 최종 보안 판단은 Backend가 수행해야 한다.

---

### [핵심]

| 비교          | Authentication         | Authorization                     |
| ------------- | ---------------------- | --------------------------------- |
| 의미          | 사용자가 누구인지 확인 | 사용자가 무엇을 할 수 있는지 확인 |
| 예시          | 로그인                 | 관리자 페이지 접근                |
| 실패 상태     | 401 Unauthorized       | 403 Forbidden                     |
| Frontend 역할 | 로그인 상태 UX 처리    | 메뉴 / 화면 노출 제어             |
| 최종 보안     | Backend 검증 필수      | Backend 검증 필수                 |

핵심 키워드:

- Authentication
- Authorization
- Login
- Role
- Permission
- 401 Unauthorized
- 403 Forbidden
- Protected Route
- Backend Authorization
- Frontend UX Guard

---

### [실무]

인증과 인가는 반드시 분리해서 처리한다.

```text
로그인하지 않은 사용자가 /mypage 접근
→ Authentication 실패
→ login redirect 또는 401 처리
```

```text
일반 사용자가 /admin 접근
→ Authorization 실패
→ forbidden page 또는 403 처리
```

주의:

- 로그인 여부와 권한 여부를 구분
- 401과 403을 같은 방식으로 처리하지 않음
- Frontend role check는 UX용
- Backend API 권한 검증 필수
- 관리자 버튼 숨김은 보안이 아님
- 관리자 API는 Backend에서 ROLE_ADMIN 검증 필요

---

### [FAQ]

Q. Authentication과 Authorization 차이는?
A. Authentication은 사용자가 누구인지 확인하는 것이고 Authorization은 그 사용자가 접근 권한이 있는지 확인하는 것이다.

Q. 401과 403 차이는?
A. 401은 인증 실패 또는 로그인 필요이고 403은 인증은 되었지만 권한이 부족한 경우다.

Q. 로그인한 사용자는 모든 API를 호출할 수 있어?
A. 아니다. 로그인은 Authentication이고 API별 권한은 Authorization으로 별도 검증해야 한다.

Q. Frontend에서 ROLE_ADMIN을 확인하면 관리자 API가 안전해져?
A. 아니다. Frontend role check는 화면 접근 UX용이고 관리자 API는 Backend에서 반드시 권한 검증해야 한다.

---

# 3. Frontend Auth Responsibility

## 3.1 Frontend Responsibility

### [개념]

Frontend 인증 책임은 사용자 경험과 인증 요청 흐름을 관리하는 것이다.

Frontend는 로그인 상태에 따라 화면을 바꾸고, 인증 API 요청에 token을 포함하고, 인증 실패 시 적절한 UI를 보여준다.

Frontend는 실제 token 검증이나 최종 권한 판단을 담당하지 않는다.

---

### [핵심]

Frontend 책임:

- Login Form 제공
- Signup Form 제공
- Auth State 관리
- Auth Loading 관리
- Token 전달
- Authorization Header 추가
- Protected Route UX 처리
- Role Based UI 처리
- Logout 처리
- 401 / 403 UI 처리
- 인증 상태 복원
- redirect 처리
- OAuth2 Callback 처리

Frontend 책임 아님:

- 실제 token 검증
- JWT 서명 검증
- 최종 권한 판단
- API 보안 보장
- 비밀번호 검증 최종 책임
- 사용자 권한 강제
- OAuth Provider Secret 관리

---

### [실무]

Frontend Auth Flow는 Backend Auth API와 연결된다.

```text
User Action
→ Frontend Auth UI
→ Backend Auth API
→ Backend Token / User Response
→ Frontend Auth State Update
→ Authenticated API Request
→ Backend Authorization Check
```

Frontend는 다음을 수행한다.

```text
로그인 성공
→ accessToken 저장 또는 관리
→ user summary 저장
→ authenticated true
→ authApi Authorization Header 적용
→ protected page 접근 허용
```

Backend는 다음을 수행한다.

```text
Request 수신
→ JWT 검증
→ 사용자 식별
→ 권한 확인
→ API 응답 또는 401 / 403 반환
```

주의:

- Frontend에서 버튼을 숨겨도 API 직접 호출은 가능
- Backend에서 반드시 인증/인가 확인
- Frontend는 사용자 경험과 요청 흐름 담당
- 보안 판단은 Backend 기준
- Frontend Auth State를 실제 보안 기준으로 착각하지 않음

---

### [FAQ]

Q. Frontend 인증 처리는 보안이야 UX야?
A. Frontend 인증 처리는 주로 UX용이고 실제 보안은 Backend 인증/인가가 담당해야 한다.

Q. 관리자 버튼을 Frontend에서 숨기면 보안이 돼?
A. 아니다. 버튼 숨김은 UX용이고 실제 관리자 API는 Backend에서 권한 검증해야 한다.

Q. Frontend Auth State가 true면 사용자를 신뢰해도 돼?
A. Frontend 표시에는 사용할 수 있지만 실제 데이터 접근 권한은 Backend 응답으로 확인해야 한다.

Q. Frontend에서 token을 해석해서 권한을 판단해도 돼?
A. UI 분기에는 참고할 수 있지만 최종 권한 판단은 Backend API 검증 결과를 기준으로 해야 한다.

---

# 4. Scope Rules

## 4.1 Included Scope

### [개념]

Authentication Frontend Flow 문서는 React Frontend 인증 흐름 구현에 필요한 범위를 포함한다.

이 범위는 Frontend Agent가 로그인부터 로그아웃까지 인증 UX와 API 연동을 일관되게 구현하도록 지원한다.

---

### [핵심]

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
- Me API
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

### [실무]

Authentication Frontend Flow는 Form Handling과 Data Fetching 위에서 동작한다.

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

Frontend 인증 문서에서 우선 다루는 것은 구현 흐름이다.

```text
화면 입력
→ API 호출
→ token 처리
→ 상태 갱신
→ route 제어
→ 오류 처리
→ 정리
```

---

### [FAQ]

Q. Auth 문서에서 JWT 구조도 깊게 다뤄?
A. Frontend에서 필요한 token 사용 흐름은 포함하지만 JWT 서명, 필터, Security 설정은 Backend Security 문서에서 다룬다.

Q. OAuth2 전체 구조도 여기서 다뤄?
A. Frontend redirect callback 처리와 사용자 상태 반영 기준은 포함하지만 OAuth2 서버 설정 심화는 Backend Security 또는 OAuth2 문서에서 다룬다.

Q. refresh token 보안 저장 전략을 깊게 다뤄?
A. 기초 주의사항은 포함하지만 상세 보안 정책은 Security / Authentication Architecture 문서에서 다룬다.

---

## 4.2 Excluded Scope

### [개념]

Authentication Frontend Flow 문서에서는 Backend 인증 구현과 고급 보안 아키텍처 심화를 제외한다.

제외 범위를 명확히 해야 Agent Retrieval 혼선을 줄일 수 있다.

---

### [핵심]

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

### [실무]

고급 기술은 별도 Domain Rules에서 관리한다.

```text
Authentication Frontend Flow
→ Security Frontend Basics
→ Spring Security JWT
→ OAuth2 Backend Integration
→ Advanced Auth Architecture
```

역할 분리 기준:

```text
Frontend Authentication
→ token 사용
→ auth state 관리
→ UX guard 처리
→ 401 / 403 화면 처리
```

```text
Backend Security
→ token 발급
→ token 검증
→ 권한 판단
→ API 접근 제어
```

---

### [FAQ]

Q. JWT 만드는 코드는 여기서 다뤄?
A. 아니다. JWT 생성과 검증은 Backend 영역이고 Frontend는 발급받은 token을 사용하는 흐름을 다룬다.

Q. Spring Security 설정도 여기서 다뤄?
A. 아니다. Frontend 인증 흐름과 Backend Security 설정은 문서를 분리한다.

Q. CSRF나 XSS 보안 전체 전략도 여기서 다뤄?
A. 기본 주의사항은 포함하지만 심화 보안 설계는 별도 Security 문서에서 다룬다.

---

# 5. Authentication Frontend Flow Position

## 5.1 Relation with Other Frontend Domains

### [개념]

Authentication Frontend Flow는 Form Handling, Data Fetching, React Router, State Management, Error Handling 문서와 연결되는 Frontend Foundation 문서다.

인증 흐름은 독립 기능이 아니라 여러 Frontend 기술의 조합으로 동작한다.

---

### [핵심]

연계 Domain:

- Form Handling & Validation
- Data Fetching & REST API Integration
- React Router
- State Management
- Error Handling & Loading UX
- Frontend Security
- Frontend Testing
- Frontend Code Review
- Backend Security
- API Design

---

### [실무]

문서 간 연결 흐름:

```text
Form Handling & Validation
→ Login Form / Signup Form
```

```text
Data Fetching & REST API Integration
→ Login API / Me API / Auth API
```

```text
React Router
→ Protected Route / PublicOnlyRoute / Redirect After Login
```

```text
State Management
→ Auth State / User Summary / Token State
```

```text
Error Handling & Loading UX
→ 401 / 403 / Auth Loading / Token Expired
```

```text
Backend Security
→ JWT 발급 / 검증 / Role Authorization
```

Agent는 인증 기능을 구현할 때 단일 문서만 참조하지 않고 관련 Domain을 함께 검색해야 한다.

---

### [FAQ]

Q. Authentication Frontend Flow는 어떤 문서와 같이 봐야 해?
A. Form Handling, Data Fetching, React Router, State Management, Error Handling, Backend Security 문서와 함께 참조해야 한다.

Q. 로그인 Form 검증은 이 문서에서 다뤄?
A. 기본 흐름은 다루지만 상세 입력 검증 규칙은 Form Handling & Validation 문서에서 다룬다.

Q. API 에러 공통 처리는 이 문서에서 다뤄?
A. 401 / 403 인증 오류는 다루지만 전체 에러 UX는 Error Handling & Loading UX 문서와 연결한다.

---

# 6. Modern Authentication Frontend Baseline

## 6.1 Version and Implementation Baseline

### [개념]

Authentication Frontend Flow 문서는 Modern React Frontend 인증 흐름 기준으로 작성한다.

Legacy 방식보다 Functional Component, Hook 기반 Auth State, React Router v6+, Axios Instance, REST API Auth 흐름을 우선한다.

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
- class component auth guard 중심 설명
- token을 전역 변수에만 저장하는 방식
- Frontend role check를 보안으로 간주
- password / token console.log
- 모든 인증 상태를 localStorage에 무분별하게 저장
- 401 / 403 동일 처리
- auth loading 없이 즉시 redirect
- OAuth secret을 Frontend에 저장

---

### [실무]

현대적인 Frontend 인증 흐름은 아래 구조를 기본으로 한다.

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

구현 기준:

```text
Auth Provider 또는 Auth Store
→ authApi Axios Instance
→ Request Interceptor
→ Response Interceptor
→ ProtectedRoute
→ PublicOnlyRoute
→ RoleRoute
→ Logout Cleanup
```

권장:

- 인증 상태는 initialized / loading / authenticated 구분
- token 존재만으로 인증 완료 판단하지 않음
- `/me` API로 인증 복원 가능
- 401과 403 분리
- role naming 통일
- Backend Authorization을 최종 보안 기준으로 명시

---

### [FAQ]

Q. React에서 인증은 무조건 Redux로 해야 해?
A. 아니다. 프로젝트 규모에 따라 Context, Zustand, Redux Toolkit, TanStack Query 조합 중 선택할 수 있다.

Q. class component 방식 auth guard도 다뤄?
A. 신규 문서에서는 Functional Component와 Hook 기반 인증 흐름을 우선한다.

Q. React Router v6 기준으로 Protected Route를 설계해?
A. 그렇다. Navigate, Outlet, wrapper route 방식 등 React Router v6+ 흐름을 기준으로 한다.

---

# 7. Part01 Review Checklist

## 7.1 Overview Checklist

### [개념]

Part01은 Authentication Frontend Flow의 목적, 책임, 범위, 문서 간 위치를 정의한다.

이 문서는 이후 Login Flow, Auth State, Token Handling, Axios Interceptor, Protected Route, 401 / 403, OAuth2 문서의 기준점이다.

---

### [핵심]

Checklist:

```md
- [ ] Authentication Frontend Flow 목적이 명확한가?
- [ ] Frontend 인증과 Backend Security 역할이 분리되었는가?
- [ ] Authentication과 Authorization 차이가 포함되었는가?
- [ ] 401과 403 차이가 포함되었는가?
- [ ] Frontend Auth Responsibility가 정의되었는가?
- [ ] Included Scope가 명확한가?
- [ ] Excluded Scope가 명확한가?
- [ ] 관련 Frontend Domain과의 연결이 포함되었는가?
- [ ] Modern React 기준이 포함되었는가?
- [ ] Backend Authorization Required 기준이 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

Part01 이후 권장 문서 순서:

```text
Part01 Overview / Responsibility / Scope
→ Part02 Login Flow / Signup Flow
→ Part03 Auth State / Auth Restore
→ Part04 Token Handling / Token Storage
→ Part05 Axios Auth Integration
→ Part06 Protected Route / Role Based Route
→ Part07 Logout / User Profile Fetch
→ Part08 OAuth2 Frontend Flow
→ Part09 401 / 403 / Troubleshooting
→ Part10 Security / Checklist / Retrieval Optimization
```

---

### [FAQ]

Q. Part01의 목적은 뭐야?
A. Authentication Frontend Flow의 전체 목적, Frontend 책임, Backend 책임, 포함 범위와 제외 범위를 정리하는 것이다.

Q. Part01만 보고 구현할 수 있어?
A. 전체 방향은 잡을 수 있지만 실제 구현은 Login Flow, Auth State, Token Handling, Axios Interceptor, Protected Route 문서가 이어져야 한다.

Q. Part01에서 가장 중요한 기준은?
A. Frontend 인증은 UX와 요청 흐름 담당이고 실제 보안은 Backend 인증/인가가 담당한다는 역할 분리다.

---

# Retrieval Queries

### [FAQ]

Q. Authentication Frontend Flow 문서는 왜 필요해?
A. Frontend Agent가 로그인, token 처리, 인증 API 요청, Protected Route, 로그아웃 흐름을 안정적으로 구현해야 하기 때문이다.

Q. Authentication Frontend Flow는 Login Form 문서야?
A. 아니다. Login Form뿐 아니라 Auth State, Token Handling, Authorization Header, Protected Route, 401 / 403, OAuth2 Callback까지 포함하는 인증 흐름 문서다.

Q. Authentication과 Authorization 차이는?
A. Authentication은 사용자가 누구인지 확인하는 것이고 Authorization은 그 사용자가 접근 권한이 있는지 확인하는 것이다.

Q. 401과 403 차이는?
A. 401은 인증 실패 또는 로그인 필요이고 403은 인증은 되었지만 권한이 부족한 경우다.

Q. Frontend 인증 처리는 보안이야 UX야?
A. Frontend 인증 처리는 주로 UX용이고 실제 보안은 Backend 인증/인가가 담당해야 한다.

Q. Frontend Auth State가 true면 사용자를 신뢰해도 돼?
A. Frontend 표시에는 사용할 수 있지만 실제 데이터 접근 권한은 Backend 응답으로 확인해야 한다.

Q. 관리자 버튼을 Frontend에서 숨기면 보안이 돼?
A. 아니다. 버튼 숨김은 UX용이고 실제 관리자 API는 Backend에서 권한 검증해야 한다.

Q. Frontend에서 ROLE_ADMIN을 확인하면 관리자 API가 안전해져?
A. 아니다. Frontend role check는 화면 접근 UX용이고 관리자 API는 Backend에서 반드시 권한 검증해야 한다.

Q. Frontend 인증 문서에 포함되는 범위는?
A. Login Flow, Logout Flow, Auth State, Token Handling, Authorization Header, Axios Interceptor, Protected Route, Role Based UI, 401 / 403, OAuth2 Callback이다.

Q. Frontend 인증 문서에서 제외되는 범위는?
A. Spring Security Filter Chain, JWT 서명 검증, OAuth2 Provider 설정, Refresh Token Rotation, CSRF / XSS 심화, Backend Authorization Policy는 제외한다.

Q. JWT 만드는 코드는 여기서 다뤄?
A. 아니다. JWT 생성과 검증은 Backend 영역이고 Frontend는 발급받은 token을 사용하는 흐름을 다룬다.

Q. Spring Security 설정도 여기서 다뤄?
A. 아니다. Frontend 인증 흐름과 Backend Security 설정은 문서를 분리한다.

Q. Authentication Frontend Flow는 어떤 문서와 같이 봐야 해?
A. Form Handling, Data Fetching, React Router, State Management, Error Handling, Backend Security 문서와 함께 참조해야 한다.

Q. 로그인 Form 검증은 이 문서에서 다뤄?
A. 기본 흐름은 다루지만 상세 입력 검증 규칙은 Form Handling & Validation 문서에서 다룬다.

Q. API 에러 공통 처리는 이 문서에서 다뤄?
A. 401 / 403 인증 오류는 다루지만 전체 에러 UX는 Error Handling & Loading UX 문서와 연결한다.

Q. Modern React 인증 기준은 뭐야?
A. Functional Component, Hook 기반 Auth State, React Router v6+, Axios Instance, Axios Interceptor, REST API Auth 흐름을 우선한다.

Q. React에서 인증은 무조건 Redux로 해야 해?
A. 아니다. 프로젝트 규모에 따라 Context, Zustand, Redux Toolkit, TanStack Query 조합 중 선택할 수 있다.

Q. Part01의 목적은 뭐야?
A. Authentication Frontend Flow의 전체 목적, Frontend 책임, Backend 책임, 포함 범위와 제외 범위를 정리하는 것이다.

Q. Part01 다음 문서는 뭐야?
A. Login Flow / Signup Flow, Auth State / Auth Restore, Token Handling, Axios Auth Integration, Protected Route 순서로 이어지는 것이 좋다.
