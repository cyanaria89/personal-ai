# Security Advanced Part08 - Testing, Troubleshooting, Review

---

# 1. Security Testing Overview

## 1.1 Security Testing Concept

### [개념]

Security Testing은 Spring Security 기반 Backend에서 인증(Authentication), 인가(Authorization), JWT, Token Reissue, Logout, CORS, CSRF, OAuth2 Login 정책이 의도대로 동작하는지 검증하는 과정이다.

Security Testing은 단순히 정상 로그인만 확인하는 것이 아니라 Token 없음, 위조 Token, 만료 Token, 권한 부족, 타인 리소스 접근, Refresh Token 실패, CORS Preflight, CSRF 정책까지 함께 검증해야 한다.

---

### [핵심]

Security Testing 핵심 키워드:

- Security Test
- Authentication Test
- Authorization Test
- JWT Test
- Access Token Test
- Refresh Token Test
- Token Reissue Test
- Logout Test
- Resource Owner Test
- Admin API Test
- CORS Test
- CSRF Test
- OAuth2 Login Test
- 401 Unauthorized
- 403 Forbidden
- MockMvc
- Postman
- Swagger

기본 테스트 축:

```text
Authentication
→ Authorization
→ Token Reissue
→ Logout
→ CORS / CSRF
→ OAuth2
→ Troubleshooting
```

---

### [실무]

2026 실무 기준 Security Test는 수동 테스트와 자동화 테스트를 함께 구성한다.

테스트 도구 후보:

```text
Swagger UI
→ API 수동 확인

Postman
→ Token Header / Reissue / Logout 수동 검증

MockMvc
→ Controller / Security Filter 자동 테스트

Spring Security Test
→ 인증 사용자 Mocking

Browser DevTools
→ CORS / Preflight 확인
```

Security Test 기본 흐름:

```text
Public API 접근 확인
→ Protected API Token 없음 확인
→ 유효 Access Token 확인
→ 위조 Access Token 확인
→ 만료 Access Token 확인
→ User Token to Admin API 확인
→ Owner Resource 접근 확인
→ Other User Resource 접근 확인
→ Refresh Token Reissue 확인
→ Logout 후 Reissue 차단 확인
→ CORS Preflight 확인
```

권장:

- 401과 403을 반드시 분리해 검증한다.
- 정상 케이스보다 실패 케이스를 더 중요하게 본다.
- Token 원문을 테스트 로그에 남기지 않는다.
- Frontend errorCode 계약과 응답 형식을 함께 검증한다.
- 보안 테스트 결과는 API Design / Testing 문서와 연결한다.

---

### [FAQ]

Q. Security Testing은 왜 필요해?
A. 인증, 인가, JWT, 권한 검증은 설정 실수 하나로 API가 열리거나 막힐 수 있으므로 반드시 테스트해야 한다.

Q. Security Test에서 가장 중요한 것은 뭐야?
A. Token 없음은 401, 권한 부족은 403, 정상 권한은 200 계열인지 확인하는 것이다.

Q. 정상 로그인만 테스트하면 충분해?
A. 아니다. 위조 Token, 만료 Token, 권한 부족, 타인 리소스 접근, Reissue 실패까지 테스트해야 한다.

---

# 2. Authentication Test Rules

## 2.1 Public API Test

### [개념]

Public API Test는 인증 없이 접근 가능한 API가 Token 없이 정상 동작하는지 검증하는 테스트다.

회원가입, 로그인, 토큰 재발급 진입 경로, 공개 조회, Health Check는 Public API 후보가 될 수 있다.

---

### [핵심]

Public API 테스트 대상:

- 회원가입
- 로그인
- 토큰 재발급 경로
- 공개 게시글 목록
- 공개 게시글 상세
- 공개 축제 목록
- 공개 축제 상세
- Health Check
- Swagger 개발 경로

기대 결과:

```text
Public API without Token
→ 200 OK 또는 정책별 정상 응답
```

---

### [실무]

테스트 시나리오:

```text
GET /api/public/posts
Authorization Header 없음
→ 200 OK
```

```text
POST /api/auth/login
Authorization Header 없음
→ 로그인 성공 또는 INVALID_LOGIN
→ SecurityFilterChain 401 차단이면 안 됨
```

MockMvc 예:

```java
@Test
void publicApiCanAccessWithoutToken() throws Exception {
    mockMvc.perform(get("/api/public/posts"))
            .andExpect(status().isOk());
}
```

검증 기준:

- Public API가 Token 없이 접근 가능한가?
- JWT Filter가 Token 없음으로 Public API를 차단하지 않는가?
- 로그인 API가 SecurityFilterChain에서 막히지 않는가?
- Swagger 경로가 개발 환경에서만 열리는가?
- Public API 범위가 과도하게 넓지 않은가?

---

### [FAQ]

Q. Public API 테스트는 뭘 확인해?
A. 인증 없이 접근해야 하는 API가 Token 없이 정상 동작하는지 확인한다.

Q. 로그인 API가 401로 막히면 뭐가 문제야?
A. requestMatchers permitAll 누락 또는 JWT Filter가 Token 없음 자체를 실패 처리하는 문제일 수 있다.

Q. Public API 테스트에서 보안상 같이 볼 것은 뭐야?
A. Public API 범위가 너무 넓어 Protected API나 Admin API가 열리지 않았는지 확인해야 한다.

---

## 2.2 Protected API Authentication Test

### [개념]

Protected API Authentication Test는 인증이 필요한 API가 Token 없음, 위조 Token, 만료 Token을 올바르게 401 Unauthorized로 처리하는지 검증하는 테스트다.

---

### [핵심]

테스트 대상:

- Token 없음
- Bearer prefix 누락
- 위조 Token
- 만료 Access Token
- Refresh Token을 Access Token 위치에 사용
- 잘못된 tokenType
- JWT Filter 미동작
- SecurityContext 저장 실패

기대 결과:

```text
No Token to Protected API
→ 401 Unauthorized

Invalid Token to Protected API
→ 401 Unauthorized

Expired Access Token
→ 401 TOKEN_EXPIRED
```

---

### [실무]

테스트 시나리오:

```text
GET /api/users/me
Authorization Header 없음
→ 401 Unauthorized
```

```text
GET /api/users/me
Authorization: Bearer invalid-token
→ 401 Unauthorized
```

```text
GET /api/users/me
Authorization: Bearer expired-access-token
→ 401 TOKEN_EXPIRED
```

MockMvc 예:

```java
@Test
void protectedApiWithoutTokenReturns401() throws Exception {
    mockMvc.perform(get("/api/users/me"))
            .andExpect(status().isUnauthorized());
}
```

위조 Token 테스트:

```text
정상 JWT 문자열 일부 변경
→ Protected API 요청
→ Signature 검증 실패
→ 401 Unauthorized
```

검증 기준:

- Token 없음은 401인가?
- 위조 Token은 401인가?
- 만료 Token은 401인가?
- errorCode가 Frontend 재발급 흐름과 맞는가?
- AuthenticationEntryPoint가 적용되는가?
- Token 원문이 응답이나 로그에 노출되지 않는가?

---

### [FAQ]

Q. Protected API에 Token이 없으면 몇 번 응답이 맞아?
A. 인증 정보가 없으므로 401 Unauthorized가 맞다.

Q. 위조 JWT는 어떻게 테스트해?
A. 유효한 JWT 문자열 일부를 변경해 서명 검증 실패가 401로 처리되는지 확인한다.

Q. 만료 Access Token은 401이야 403이야?
A. 인증 실패이므로 일반적으로 401이다.

---

# 3. Authorization Test Rules

## 3.1 Role Authorization Test

### [개념]

Role Authorization Test는 사용자 Role에 따라 API 접근 권한이 올바르게 제한되는지 검증하는 테스트다.

일반 User Token으로 Admin API 접근 시 403 Forbidden이 발생해야 하며, Admin Token으로 접근 시 성공해야 한다.

---

### [핵심]

테스트 대상:

- User Token
- Admin Token
- ROLE_USER
- ROLE_ADMIN
- hasRole
- hasAuthority
- ROLE\_ prefix
- Admin API
- AccessDeniedHandler

기대 결과:

```text
User Token to User API
→ 200 OK

User Token to Admin API
→ 403 Forbidden

Admin Token to Admin API
→ 200 OK
```

---

### [실무]

테스트 시나리오:

```text
GET /api/admin/users
Authorization: Bearer user-access-token
→ 403 ACCESS_DENIED
```

```text
GET /api/admin/users
Authorization: Bearer admin-access-token
→ 200 OK
```

MockMvc 예:

```java
@Test
void userTokenCannotAccessAdminApi() throws Exception {
    mockMvc.perform(get("/api/admin/users")
                    .header("Authorization", "Bearer " + userAccessToken))
            .andExpect(status().isForbidden());
}
```

검증 기준:

- User Token으로 Admin API 접근 시 403인가?
- Admin Token으로 Admin API 접근 시 성공하는가?
- hasRole / hasAuthority 규칙이 DB Role 값과 일치하는가?
- ROLE\_ prefix 불일치가 없는가?
- AccessDeniedHandler 응답 형식이 적용되는가?
- 403을 401로 잘못 처리하지 않는가?

---

### [FAQ]

Q. User Token으로 Admin API를 호출하면 몇 번 응답이 맞아?
A. 인증은 되었지만 관리자 권한이 부족하므로 403 Forbidden이 맞다.

Q. Role 권한 테스트에서 가장 자주 나는 문제는 뭐야?
A. ROLE\_ prefix 불일치로 권한이 있어도 403이 발생하는 문제다.

Q. Admin API는 Frontend에서 메뉴만 숨기면 충분해?
A. 아니다. Backend에서 ROLE_ADMIN 검증을 테스트해야 한다.

---

## 3.2 Resource Owner Test

### [개념]

Resource Owner Test는 인증된 사용자가 본인 리소스에는 접근 가능하고 타인 리소스에는 접근할 수 없는지 검증하는 테스트다.

Role이 같아도 리소스 소유자가 다르면 수정, 삭제, 조회가 제한될 수 있다.

---

### [핵심]

테스트 대상:

- 내 게시글 수정
- 타인 게시글 수정
- 내 댓글 삭제
- 타인 댓글 삭제
- 내 알림 조회
- 타인 알림 조회
- 내 결제 내역 조회
- 타인 결제 내역 조회
- RequestBody userId 조작
- PathVariable userId 조작

기대 결과:

```text
Owner Token + Owner Resource
→ 200 OK

Other User Token + Owner Resource
→ 403 Forbidden

RequestBody userId 조작
→ Principal 기준 처리
→ 권한 우회 실패
```

---

### [실무]

테스트 시나리오:

```text
PUT /api/posts/{postId}
Owner Token
→ 200 OK
```

```text
PUT /api/posts/{postId}
Other User Token
→ 403 RESOURCE_ACCESS_DENIED
```

```text
PUT /api/posts/{postId}
Other User Token + RequestBody userId = ownerId
→ 403 Forbidden
```

MockMvc 예:

```java
@Test
void userCannotUpdateOtherUserPostEvenIfRequestUserIdIsManipulated() throws Exception {
    mockMvc.perform(put("/api/posts/{postId}", otherUserPostId)
                    .header("Authorization", "Bearer " + userAccessToken)
                    .contentType(MediaType.APPLICATION_JSON)
                    .content("""
                            {
                              "userId": 1,
                              "title": "changed",
                              "content": "changed"
                            }
                            """))
            .andExpect(status().isForbidden());
}
```

검증 기준:

- currentUserId가 Principal 기준인가?
- RequestBody userId를 신뢰하지 않는가?
- Service에서 Resource Owner Check를 수행하는가?
- 타인 리소스 접근이 403으로 차단되는가?
- 관리자 Override 정책이 있다면 의도대로 동작하는가?

---

### [FAQ]

Q. Resource Owner 테스트는 왜 필요해?
A. 로그인한 사용자가 타인 리소스를 수정하거나 조회하는 권한 우회를 막기 위해 필요하다.

Q. RequestBody userId 조작 테스트도 해야 해?
A. 해야 한다. Client가 userId를 조작해도 Principal 기준으로 처리되는지 확인해야 한다.

Q. 타인 게시글 수정은 401이야 403이야?
A. 인증은 되었지만 소유자가 아니므로 일반적으로 403 Forbidden이다.

---

# 4. JWT and Token Test Rules

## 4.1 Access Token Test

### [개념]

Access Token Test는 Access Token 발급, Claim, 만료, 검증, SecurityContext 저장이 정상 동작하는지 확인하는 테스트다.

---

### [핵심]

테스트 대상:

- Access Token 발급
- Access Token Claim
- userId Claim
- role Claim
- tokenType Claim
- expiration
- Signature 검증
- JWT Filter 검증
- SecurityContext 저장
- Principal 접근

기대 결과:

```text
Valid Access Token
→ Protected API 200
→ Principal userId 사용 가능

Expired Access Token
→ 401 TOKEN_EXPIRED

Invalid Access Token
→ 401 TOKEN_INVALID
```

---

### [실무]

테스트 시나리오:

```text
Login 성공
→ Access Token 발급 확인
→ Authorization Header 첨부
→ /api/users/me 호출
→ 200 OK
```

```text
Access Token Payload 확인
→ password 없음
→ refreshToken 없음
→ 민감정보 없음
→ exp 존재
```

검증 기준:

- Access Token에 만료 시간이 있는가?
- Claim에 민감정보가 없는가?
- role Claim이 Authority로 변환되는가?
- JWT Filter가 SecurityContext에 Authentication을 저장하는가?
- Controller에서 `@AuthenticationPrincipal`을 사용할 수 있는가?
- Access Token 원문이 로그에 남지 않는가?

---

### [FAQ]

Q. Access Token 테스트에서 가장 중요한 것은 뭐야?
A. 유효 Token 인증 성공, 만료 Token 401, 위조 Token 401, SecurityContext 저장 여부다.

Q. Access Token Payload에서 확인할 것은 뭐야?
A. userId, role, exp가 있고 password, refreshToken, 민감정보가 없는지 확인한다.

Q. Token은 정상인데 Principal이 null이면 뭐가 문제야?
A. JWT Filter가 실행되지 않았거나 Authentication을 SecurityContext에 저장하지 않았을 수 있다.

---

## 4.2 Refresh Token and Reissue Test

### [개념]

Refresh Token and Reissue Test는 Refresh Token 저장, 검증, Access Token 재발급, Rotation, 실패 처리가 올바르게 동작하는지 검증하는 테스트다.

---

### [핵심]

테스트 대상:

- Refresh Token 발급
- Refresh Token 저장
- Refresh Token hash 저장
- Refresh Token 만료
- 저장소 Token 일치
- Token Reissue
- Refresh Token Rotation
- revoked Token
- Logout 후 Reissue 차단
- 탈퇴 / 정지 사용자 Reissue 차단

기대 결과:

```text
Valid Refresh Token
→ Reissue 200
→ New Access Token 발급

Expired Refresh Token
→ 401 REFRESH_TOKEN_INVALID

Logout 후 Refresh Token
→ 401 REFRESH_TOKEN_INVALID
```

---

### [실무]

테스트 시나리오:

```text
Login 성공
→ Refresh Token 저장 확인
→ Access Token 만료
→ Reissue 요청
→ 새 Access Token 발급
```

```text
Refresh Token 문자열 일부 변경
→ Reissue 요청
→ 401 REFRESH_TOKEN_INVALID
```

```text
Logout 성공
→ Refresh Token 삭제
→ 기존 Refresh Token으로 Reissue 요청
→ 401 REFRESH_TOKEN_INVALID
```

Rotation 테스트:

```text
Reissue 성공
→ 새 Refresh Token 발급
→ 이전 Refresh Token 재사용
→ 401 또는 탈취 대응 정책 실행
```

검증 기준:

- Refresh Token이 서버 저장소에 저장되는가?
- 저장소 Token과 요청 Token을 비교하는가?
- 만료 Refresh Token은 401인가?
- Logout 후 Reissue가 차단되는가?
- 정지 / 탈퇴 사용자의 Reissue가 차단되는가?
- Rotation 사용 시 이전 Token이 무효화되는가?

---

### [FAQ]

Q. Refresh Token 테스트에서 가장 중요한 것은 뭐야?
A. 저장소 검증, 만료 처리, Reissue 성공, Logout 후 Reissue 차단이다.

Q. 로그아웃 후 Reissue가 성공하면 문제야?
A. 문제다. Refresh Token 삭제 또는 저장소 검증이 제대로 동작하지 않는 것이다.

Q. Rotation 테스트는 꼭 필요해?
A. Rotation을 사용하는 구조라면 이전 Refresh Token 재사용 차단 테스트가 필요하다.

---

# 5. Logout Test Rules

## 5.1 Logout Test

### [개념]

Logout Test는 로그아웃 요청 시 서버 저장 Refresh Token이 삭제 또는 무효화되고 이후 Token Reissue가 차단되는지 확인하는 테스트다.

JWT Stateless 구조에서는 Client Token 삭제만으로는 충분하지 않다.

---

### [핵심]

테스트 대상:

- 정상 로그아웃
- Token 없이 로그아웃
- 위조 Token으로 로그아웃
- RequestBody userId 조작
- Refresh Token 삭제
- Refresh Token Cookie 제거
- 로그아웃 후 Reissue 차단
- Global Logout
- Device Logout

기대 결과:

```text
Valid Access Token
→ Logout 200
→ Refresh Token 삭제

No Token
→ Logout 401

Logout 후 Reissue
→ 401 REFRESH_TOKEN_INVALID
```

---

### [실무]

테스트 시나리오:

```text
POST /api/auth/logout
Authorization: Bearer valid-access-token
→ 200 OK
→ Refresh Token 삭제
```

```text
POST /api/auth/logout
Authorization Header 없음
→ 401 Unauthorized
```

```text
POST /api/auth/logout
Access Token은 User A
RequestBody userId는 User B
→ User A Principal 기준 로그아웃
→ User B Token 영향 없음
```

검증 기준:

- Logout API가 Protected API인가?
- Principal 기준으로 로그아웃 처리하는가?
- RequestBody userId를 신뢰하지 않는가?
- Refresh Token이 삭제 또는 revoked 처리되는가?
- Cookie 방식이면 Set-Cookie maxAge=0이 내려가는가?
- 로그아웃 후 Reissue가 실패하는가?

---

### [FAQ]

Q. Logout 테스트에서 가장 중요한 것은 뭐야?
A. Refresh Token 삭제와 로그아웃 후 Reissue 차단 여부다.

Q. 로그아웃 API는 인증이 필요해?
A. 일반적으로 필요하다. 현재 인증 사용자 기준으로 Refresh Token을 무효화해야 한다.

Q. RequestBody userId로 로그아웃 처리하면 안 돼?
A. 안 된다. 조작 가능하므로 Principal userId 기준으로 처리해야 한다.

---

# 6. CORS and CSRF Test Rules

## 6.1 CORS Test

### [개념]

CORS Test는 실제 브라우저 환경에서 Frontend Origin, Authorization Header, credentials, OPTIONS Preflight가 정상 허용되는지 확인하는 테스트다.

CORS는 Postman이 아니라 브라우저에서 검증해야 한다.

---

### [핵심]

테스트 대상:

- 개발 Origin
- 운영 Origin
- 허용되지 않은 Origin
- OPTIONS Preflight
- Authorization Header
- Content-Type Header
- credentials
- allowedMethods
- allowedHeaders
- allowedOrigins

기대 결과:

```text
Allowed Origin
→ Preflight 성공
→ Actual Request 진행

Blocked Origin
→ Browser CORS 차단

Authorization Header 포함
→ allowedHeaders에 Authorization 필요
```

---

### [실무]

브라우저 검증 흐름:

```text
Browser DevTools
→ Network
→ OPTIONS Request 확인
→ Response Header 확인
→ Access-Control-Allow-Origin 확인
→ Access-Control-Allow-Headers 확인
→ Access-Control-Allow-Methods 확인
→ Access-Control-Allow-Credentials 확인
```

Postman과 차이:

```text
Postman API 성공
→ CORS 성공을 의미하지 않음

Browser API 실패
→ Preflight / Origin / Header 확인 필요
```

검증 기준:

- Frontend Origin이 allowedOrigins에 있는가?
- Authorization Header가 allowedHeaders에 있는가?
- OPTIONS Method가 허용되는가?
- credentials 사용 시 allowCredentials가 true인가?
- credentials true인데 wildcard Origin을 사용하지 않는가?
- SecurityFilterChain에 cors가 연결되어 있는가?

---

### [FAQ]

Q. CORS 테스트는 Postman으로 가능해?
A. 부족하다. CORS는 브라우저 정책이므로 실제 브라우저 요청으로 확인해야 한다.

Q. Postman은 되는데 브라우저에서 CORS 에러가 나면 뭐야?
A. CORS는 브라우저에서만 적용되므로 allowedOrigins, allowedHeaders, OPTIONS Preflight를 확인해야 한다.

Q. Authorization Header가 있으면 CORS 설정에서 뭘 봐야 해?
A. allowedHeaders에 Authorization이 포함되어 있는지 확인해야 한다.

---

## 6.2 CSRF Test

### [개념]

CSRF Test는 인증 방식과 Token 저장 위치에 따라 CSRF 보호가 필요한지, CSRF 비활성화 근거가 타당한지 검증하는 테스트다.

Cookie 기반 인증 또는 Refresh Token Cookie 구조에서는 CSRF 위험을 검토해야 한다.

---

### [핵심]

테스트 대상:

- Session Cookie 기반 인증
- Authorization Header 기반 JWT
- Refresh Token HttpOnly Cookie
- POST / PUT / PATCH / DELETE 요청
- CSRF Token 포함 요청
- CSRF Token 누락 요청
- SameSite Cookie 정책

기대 결과:

```text
Session Cookie + CSRF Token 없음 + 상태 변경 요청
→ 403

Session Cookie + CSRF Token 있음 + 상태 변경 요청
→ 200

Authorization Header JWT
→ CSRF Token보다 JWT 검증 기준으로 처리
```

---

### [실무]

Cookie 기반 테스트:

```text
로그인 Session Cookie 있음
→ CSRF Token 없이 POST 요청
→ 403 기대
```

Header JWT 기반 테스트:

```text
Authorization Header 없음
→ Protected API
→ 401

Authorization Header 있음
→ Protected API
→ JWT 검증 기준으로 처리
```

Refresh Token Cookie 검토:

```text
Reissue API
→ Cookie 자동 전송 여부 확인
→ SameSite 정책 확인
→ CSRF 위험 검토
```

검증 기준:

- CSRF disable 근거가 문서화되어 있는가?
- 인증 정보가 Cookie로 자동 전송되는가?
- 상태 변경 요청이 보호되는가?
- Refresh Token Cookie 사용 시 SameSite가 설정되어 있는가?
- Header 기반 JWT 구조라면 XSS 위험을 별도로 검토했는가?

---

### [FAQ]

Q. CSRF 테스트는 언제 필요해?
A. Cookie 기반 인증이나 Refresh Token Cookie 구조를 사용할 때 필요하다.

Q. Header 기반 JWT에서도 CSRF가 중요해?
A. 상대적으로 중요도는 낮지만 Token 저장 방식과 CSRF disable 근거는 확인해야 한다.

Q. Refresh Token을 Cookie에 넣으면 뭘 테스트해야 해?
A. SameSite, Secure, HttpOnly, Reissue API CSRF 위험, Cookie 자동 전송 여부를 확인해야 한다.

---

# 7. OAuth2 and Frontend Integration Test Rules

## 7.1 OAuth2 Login Test

### [개념]

OAuth2 Login Test는 Provider 인증, Provider Attribute Mapping, Local User Mapping, JWT 발급, Redirect URL 검증, 계정 상태 차단이 정상 동작하는지 확인하는 테스트다.

---

### [핵심]

테스트 대상:

- OAuth2 Login 시작
- Provider Callback
- 신규 OAuth2 User 생성
- 기존 OAuth2 User 조회
- provider + providerId Mapping
- email 누락 처리
- email_verified 확인
- 정지 / 탈퇴 사용자 차단
- SuccessHandler JWT 발급
- FailureHandler Redirect
- Open Redirect 방지

기대 결과:

```text
신규 OAuth2 사용자
→ Local User 생성
→ ROLE_USER 부여
→ JWT 발급
→ Frontend Success Redirect
```

```text
정지 사용자
→ OAuth2 인증 성공
→ Local User 상태 확인
→ Token 발급 차단
→ Failure Redirect
```

---

### [실무]

검증 기준:

```text
providerId 저장 확인
→ provider + providerId 조회 확인
→ email 단독 식별 금지 확인
→ Role 부여 확인
→ 계정 상태 검증 확인
→ SuccessHandler Token 발급 확인
→ Refresh Token 저장 확인
→ Redirect URL 허용 목록 확인
→ Token Query 전달 위험 확인
```

OAuth2 실패 테스트:

```text
Provider 인증 취소
→ FailureHandler
→ Frontend Failure Redirect
```

```text
지원하지 않는 Provider
→ OAUTH_PROVIDER_NOT_SUPPORTED
→ Failure 처리
```

주의:

- Provider API는 외부 의존성이 있으므로 통합 테스트와 단위 테스트를 분리한다.
- Provider Attribute Mapping은 Mock Attribute로 테스트할 수 있다.
- Token 원문과 Authorization Code를 로그에 남기지 않는다.
- Redirect URL을 요청 파라미터로 받을 경우 허용 목록 검증이 필요하다.

---

### [FAQ]

Q. OAuth2 Login 테스트에서 가장 중요한 것은 뭐야?
A. provider + providerId Mapping, Local User 생성 / 조회, JWT 발급, Redirect URL 검증이다.

Q. OAuth2 Provider 인증이 성공하면 무조건 로그인 성공이야?
A. 아니다. Local User Mapping, 계정 상태, 필수 정보, 서비스 정책 검증이 통과해야 한다.

Q. OAuth2 테스트에서 외부 Provider를 항상 호출해야 해?
A. 아니다. Attribute Mapping과 Local User Mapping은 Mock 데이터로 단위 테스트할 수 있다.

---

## 7.2 Frontend Auth Integration Test

### [개념]

Frontend Auth Integration Test는 Backend Token API와 Frontend Interceptor, Protected Route, User Summary API, Logout 흐름이 정상적으로 연결되는지 검증하는 테스트다.

---

### [핵심]

테스트 대상:

- Login Response
- Authorization Header 첨부
- `/api/users/me`
- Access Token 만료
- Reissue 성공
- Reissue 실패
- 403 권한 부족
- Logout
- Refresh Token Cookie 제거
- CORS Authorization Header
- Reissue Loop Prevention

기대 결과:

```text
Access Token 만료
→ 401 TOKEN_EXPIRED
→ Reissue 성공
→ 원 요청 재시도
→ 200

Refresh Token 만료
→ Reissue 401
→ Client Token 제거
→ Login Page 이동

User Role로 Admin API 접근
→ 403
→ Reissue 시도하지 않음
```

---

### [실무]

검증 기준:

```text
401 TOKEN_EXPIRED 처리 확인
→ Reissue API 호출 확인
→ 새 Access Token 저장 확인
→ 원 요청 재시도 확인
→ Reissue 실패 시 Logout 확인
→ 403에서 Reissue 미호출 확인
```

Backend 계약 확인:

```text
TOKEN_EXPIRED
REFRESH_TOKEN_INVALID
ACCESS_DENIED
Authorization Header 허용
Logout API
User Summary API
```

주의:

- 모든 401에 Reissue를 시도하면 무한 루프가 발생할 수 있다.
- Reissue API 401은 재발급 대상이 아니라 Logout 대상이다.
- 403은 권한 부족이므로 Token 재발급 대상이 아니다.
- Frontend Protected Route는 Backend API 보안을 대체하지 않는다.

---

### [FAQ]

Q. Frontend Auth 연동 테스트에서 가장 중요한 것은 뭐야?
A. Authorization Header 첨부, 401 Reissue, 403 권한 없음, Logout 후 Reissue 차단이다.

Q. 403이 발생했을 때 Reissue가 호출되면 문제야?
A. 문제다. 403은 권한 부족이므로 Token 재발급 대상이 아니다.

Q. Reissue 무한 루프는 어떻게 테스트해?
A. Reissue API가 401을 반환할 때 추가 Reissue를 시도하지 않고 Logout 처리되는지 확인한다.

---

# 8. Troubleshooting Rules

## 8.1 401 Unauthorized Troubleshooting

### [개념]

401 Unauthorized는 인증 정보가 없거나 유효하지 않아 사용자가 누구인지 확인할 수 없는 상태다.

401 문제는 Authorization Header, Bearer prefix, JWT Filter, Token 검증, SecurityContext 저장, AuthenticationEntryPoint 순서로 확인한다.

---

### [핵심]

401 원인:

- Authorization Header 없음
- Bearer prefix 누락
- Token 만료
- Token 서명 오류
- Secret Key 불일치
- JWT Filter 미등록
- JWT Filter 실행 안 됨
- SecurityContext 저장 실패
- Public / Protected matcher 오류
- tokenType 불일치

---

### [실무]

Debug Flow:

```text
요청 Header 확인
→ Authorization Bearer 형식 확인
→ JWT Filter 실행 여부 확인
→ Token 검증 결과 확인
→ Secret Key 확인
→ Expiration 확인
→ tokenType 확인
→ SecurityContext 저장 확인
→ EntryPoint 응답 확인
```

확인 예:

```text
Authorization: Bearer <access-token>
```

자주 발생:

```text
문제:
로그인 성공 후 /api/users/me 호출 시 401

원인 후보:
- Frontend가 Authorization Header를 안 붙임
- Bearer prefix 누락
- Access Token 저장 실패
- JWT Filter가 SecurityContext 저장 안 함
- Token 만료
```

권장:

- 먼저 Network 탭에서 Authorization Header를 확인한다.
- JWT Filter 로그는 Token 원문 없이 실행 여부만 남긴다.
- Token 만료와 위조를 구분한다.
- Public API가 401이면 matcher와 Filter 동작을 확인한다.

---

### [FAQ]

Q. 로그인했는데 401이 나와?
A. Authorization Header 누락, Bearer prefix 누락, Token 만료 / 위조, JWT Filter 미동작, SecurityContext 저장 실패를 확인해야 한다.

Q. Bearer prefix가 꼭 필요해?
A. 프로젝트 JWT Filter가 Bearer 형식을 기준으로 파싱한다면 필요하다.

Q. Public API가 401이면 뭘 봐야 해?
A. requestMatchers permitAll 설정과 JWT Filter가 Token 없음 요청을 차단하지 않는지 확인해야 한다.

---

## 8.2 403 Forbidden Troubleshooting

### [개념]

403 Forbidden은 인증은 되었지만 접근 권한이 부족한 상태다.

403 문제는 Authentication 존재 여부, Principal Role, Authority 문자열, ROLE\_ prefix, Resource Owner Check, AccessDeniedHandler 순서로 확인한다.

---

### [핵심]

403 원인:

- Role 부족
- Authority 부족
- ROLE\_ prefix 불일치
- hasRole / hasAuthority 혼동
- 관리자 API 접근
- Resource Owner Check 실패
- Method Security 실패
- Business Authorization 실패
- AccessDeniedHandler 응답

---

### [실무]

Debug Flow:

```text
Authentication 존재 확인
→ Principal userId 확인
→ Principal Role 확인
→ GrantedAuthority 확인
→ SecurityFilterChain 권한 규칙 확인
→ hasRole / hasAuthority 확인
→ Resource Owner Check 확인
→ Method Security 확인
→ AccessDeniedHandler 응답 확인
```

자주 발생:

```text
문제:
Admin Token인데 /api/admin/users 호출 시 403

원인 후보:
- DB 저장 값: ROLE_ADMIN
- 설정: hasRole("ROLE_ADMIN")
- 실제 매칭: ROLE_ROLE_ADMIN 기대
- prefix 불일치로 403
```

수정 방향:

```text
hasRole("ADMIN")
또는
hasAuthority("ROLE_ADMIN")
중 하나로 통일
```

---

### [FAQ]

Q. 토큰은 정상인데 403이 나와?
A. Role / Authority 부족, ROLE\_ prefix 불일치, Resource Owner Check 실패, Method Security 실패를 확인해야 한다.

Q. ROLE\_ prefix 때문에 403이 날 수 있어?
A. 가능하다. hasRole과 hasAuthority 사용 방식과 저장된 권한 문자열을 맞춰야 한다.

Q. 타인 리소스 접근이 403이면 정상일 수 있어?
A. 맞다. 인증은 되었지만 소유자가 아니면 403이 정상이다.

---

## 8.3 Token Reissue Troubleshooting

### [개념]

Token Reissue Troubleshooting은 Access Token 재발급이 실패하거나 무한 반복되는 문제를 분석하는 과정이다.

Refresh Token 전달, 만료, 저장소 일치, Rotation, 사용자 상태, Frontend Interceptor를 함께 확인해야 한다.

---

### [핵심]

Reissue 실패 원인:

- Refresh Token 없음
- Refresh Token 만료
- Refresh Token 서명 오류
- 저장소 Token 없음
- 저장소 Token 불일치
- revoked Token
- Rotation 후 이전 Token 사용
- 사용자 탈퇴 / 정지
- Cookie Path 불일치
- withCredentials 누락
- Reissue Loop

---

### [실무]

Debug Flow:

```text
Refresh Token 전달 확인
→ Cookie / Body / Header 위치 확인
→ Refresh Token 검증
→ 저장소 Token 조회
→ Token 일치 확인
→ revoked 여부 확인
→ 사용자 상태 확인
→ 새 Access Token 발급 확인
→ Frontend 저장 확인
```

Cookie 방식 확인:

```text
Set-Cookie Path
→ Reissue Request Path
→ SameSite
→ Secure
→ HttpOnly
→ withCredentials
```

자주 발생:

```text
문제:
로그인 후 Reissue API에서 Refresh Token 없음

원인 후보:
- Cookie Path가 /api/auth/reissue와 다름
- Frontend withCredentials 누락
- Backend CORS allowCredentials 누락
- SameSite=None인데 Secure 없음
```

---

### [FAQ]

Q. 재발급이 계속 실패하면 뭘 확인해?
A. Refresh Token 전달 방식, 만료 여부, 저장소 일치 여부, 사용자 상태, Cookie 설정, Rotation 로직을 확인한다.

Q. Reissue 무한 루프는 왜 생겨?
A. 모든 401에 재발급을 시도하거나 Reissue API 실패에도 다시 Reissue를 호출하면 발생한다.

Q. Logout 후 Reissue가 성공하면 뭐가 문제야?
A. Refresh Token 삭제 또는 저장소 검증이 제대로 동작하지 않는 것이다.

---

## 8.4 CORS Troubleshooting

### [개념]

CORS Troubleshooting은 브라우저에서 Cross-Origin API 요청이 차단되는 문제를 분석하는 과정이다.

CORS 문제는 인증 실패가 아니라 브라우저 Origin 정책 문제다.

---

### [핵심]

CORS 원인:

- Frontend Origin 미허용
- Authorization Header 미허용
- Content-Type Header 미허용
- OPTIONS Method 미허용
- SecurityFilterChain cors 누락
- credentials와 wildcard Origin 충돌
- allowCredentials 누락
- 운영 / 개발 Origin 불일치

---

### [실무]

Debug Flow:

```text
Browser Console 확인
→ Network에서 OPTIONS 요청 확인
→ Request Origin 확인
→ Response Header 확인
→ Access-Control-Allow-Origin 확인
→ Access-Control-Allow-Headers 확인
→ Access-Control-Allow-Methods 확인
→ Access-Control-Allow-Credentials 확인
→ SecurityFilterChain cors 설정 확인
```

자주 발생:

```text
문제:
Postman은 성공하지만 브라우저에서 실패

원인:
CORS는 브라우저 정책이므로 Postman에서는 발생하지 않음
```

```text
문제:
Authorization Header 포함 요청만 실패

원인:
allowedHeaders에 Authorization 누락 가능
```

---

### [FAQ]

Q. Postman은 되는데 브라우저에서 CORS 에러가 나?
A. CORS는 브라우저 보안 정책이므로 Postman에서는 발생하지 않을 수 있다.

Q. Authorization Header 때문에 CORS가 날 수 있어?
A. 가능하다. allowedHeaders에 Authorization이 허용되어 있는지 확인해야 한다.

Q. CORS 에러는 JWT 문제야?
A. 아니다. 브라우저 Origin 정책 문제다. JWT 인증 실패와 구분해야 한다.

---

# 9. Security Review Rules

## 9.1 Security Code Review Checklist

### [개념]

Security Code Review Checklist는 Spring Security, JWT, Authorization, CORS, CSRF, OAuth2, Frontend Integration 구현을 Agent가 검수하기 위한 기준이다.

---

### [핵심]

Checklist:

```md
- [ ] SecurityFilterChain Bean 기반 설정인가?
- [ ] Public / Protected / Admin API가 분리되었는가?
- [ ] 넓은 permitAll 규칙이 없는가?
- [ ] anyRequest().authenticated()가 마지막에 있는가?
- [ ] JWT Filter가 등록되었는가?
- [ ] JWT Filter가 Public API를 막지 않는가?
- [ ] JWT Filter가 SecurityContext에 Authentication을 저장하는가?
- [ ] PasswordEncoder를 사용하는가?
- [ ] 비밀번호가 평문 저장 / 응답 / 로그 출력되지 않는가?
- [ ] Login Request에 role / userId를 받지 않는가?
- [ ] Access Token과 Refresh Token 역할이 분리되었는가?
- [ ] Access Token에 민감정보가 없는가?
- [ ] Refresh Token 저장 / 무효화 전략이 있는가?
- [ ] Token Reissue에서 저장소 Token과 비교하는가?
- [ ] Logout 시 Refresh Token을 삭제하는가?
- [ ] Role / Authority naming이 통일되었는가?
- [ ] Resource Owner Check가 필요한 곳에 있는가?
- [ ] RequestBody userId를 신뢰하지 않는가?
- [ ] 401 / 403이 분리되어 있는가?
- [ ] AuthenticationEntryPoint가 등록되어 있는가?
- [ ] AccessDeniedHandler가 등록되어 있는가?
- [ ] CORS allowedOrigins가 제한되어 있는가?
- [ ] Authorization Header가 CORS에 허용되어 있는가?
- [ ] CSRF disable 근거가 명확한가?
- [ ] OAuth2 사용자를 provider + providerId로 식별하는가?
- [ ] OAuth2 Redirect URL 검증이 있는가?
- [ ] Frontend Reissue 무한 루프 방지 기준이 있는가?
```

---

### [실무]

Review Flow:

```text
SecurityConfig Review
→ JWT Filter Review
→ Password / Login Review
→ JWT / Refresh / Reissue Review
→ Authorization / Owner Check Review
→ Exception Handler Review
→ CORS / CSRF Review
→ OAuth2 Review
→ Frontend Integration Review
→ Security Test Review
```

우선순위:

```text
치명적 위험
→ 인증 우회
→ 권한 우회
→ Token 탈취 위험
→ 개인정보 노출
→ 운영 설정 노출
→ UX / errorCode 문제
```

---

### [FAQ]

Q. Security Review에서 가장 먼저 볼 것은 뭐야?
A. SecurityFilterChain의 permitAll 범위, JWT Filter, 401/403 분리, Resource Owner Check를 먼저 확인하는 것이 좋다.

Q. 가장 치명적인 보안 실수는 뭐야?
A. 모든 API permitAll, 비밀번호 평문 저장, RequestBody userId 신뢰, JWT 민감정보 포함, Resource Owner Check 누락이다.

Q. Review Agent는 뭘 기준으로 판단해야 해?
A. 인증 우회, 권한 우회, Token 위험, 민감정보 노출, 운영 설정 노출 여부를 우선 판단해야 한다.

---

## 9.2 Common Security Anti Pattern Summary

### [개념]

Common Security Anti Pattern Summary는 Security Advanced 전체에서 반복적으로 탐지해야 하는 대표 보안 실수 목록이다.

---

### [핵심]

인증 Anti Pattern:

- 모든 API permitAll
- JWT Filter 미등록
- SecurityContext 저장 누락
- Token 원문 로그 출력
- Access Token 만료 없음
- Refresh Token 저장 전략 없음

비밀번호 Anti Pattern:

- 비밀번호 평문 저장
- PasswordEncoder.matches 미사용
- 비밀번호 응답 DTO 포함
- 비밀번호 로그 출력

인가 Anti Pattern:

- Frontend 권한 체크만 신뢰
- RequestBody userId 신뢰
- Resource Owner Check 누락
- Admin API Role 검증 누락
- hasRole / hasAuthority prefix 불일치

예외 처리 Anti Pattern:

- 401 / 403 혼동
- AuthenticationEntryPoint 미등록
- AccessDeniedHandler 미등록
- Stack trace 응답
- 내부 예외 메시지 노출

CORS / CSRF Anti Pattern:

- 운영에서 모든 Origin 허용
- Authorization Header 미허용
- Cookie 인증인데 CSRF disable
- CORS와 CSRF 혼동

OAuth2 / Frontend Anti Pattern:

- OAuth2 email 단독 식별
- Redirect URL 검증 없음
- Refresh Token Query 전달
- 모든 401에 Reissue 시도
- 403에도 Reissue 시도
- Logout 시 Client Token만 삭제

---

### [실무]

Anti Pattern 탐지 Flow:

```text
SecurityConfig
→ 넓은 permitAll / anyRequest permitAll 확인

AuthService
→ PasswordEncoder / Login / Token 발급 확인

JwtFilter
→ Token 검증 / SecurityContext 저장 확인

Service
→ Resource Owner Check 확인

Exception Handler
→ 401 / 403 분리 확인

CORS / CSRF
→ 운영 Origin / Cookie 인증 확인

OAuth2 / Frontend
→ providerId / Redirect / Reissue 확인
```

수정 우선순위:

```text
1. 인증 우회 제거
2. 권한 우회 제거
3. 비밀번호 / Token 노출 제거
4. Refresh Token 무효화 보완
5. 401 / 403 응답 정리
6. CORS / CSRF 운영 설정 정리
7. OAuth2 / Frontend 연동 안정화
```

---

### [FAQ]

Q. Security Anti Pattern 중 가장 먼저 고칠 것은 뭐야?
A. 인증 우회와 권한 우회다. permitAll 과다 설정, Resource Owner Check 누락, Admin API 권한 누락을 먼저 고쳐야 한다.

Q. Token 로그 출력은 왜 위험해?
A. Token을 획득한 사람이 사용자처럼 API를 호출할 수 있으므로 인증 수단이 노출되는 문제다.

Q. Frontend Auth Anti Pattern은 Backend 보안에도 영향이 있어?
A. 있다. 401/403 처리 오류, Logout 누락, Reissue 무한 루프는 인증 흐름 전체를 불안정하게 만든다.

---

# 10. Security Troubleshooting Matrix

## 10.1 Problem Cause Solution Matrix

### [개념]

Security Troubleshooting Matrix는 자주 발생하는 Spring Security 문제를 증상, 원인, 확인 위치, 해결 방향으로 정리한 검색 최적화 표다.

---

### [핵심]

| 증상                   | 주요 원인                                  | 확인 위치                      | 해결 방향                                     |
| ---------------------- | ------------------------------------------ | ------------------------------ | --------------------------------------------- |
| 로그인 API 401         | permitAll 누락, JWT Filter Token 없음 차단 | SecurityFilterChain, JwtFilter | auth 경로 permitAll, Token 없으면 다음 Filter |
| Protected API 401      | Header 없음, Token 만료, Filter 미동작     | Network, JwtFilter             | Authorization Header, Token 검증              |
| Admin API 403          | Role 부족, prefix 불일치                   | Authority, hasRole             | ROLE\_ 규칙 통일                              |
| 타인 리소스 수정 가능  | Owner Check 누락                           | Service                        | Principal 기반 Owner Check 추가               |
| Reissue 실패           | Refresh Token 누락, 저장소 불일치          | Cookie, DB, Redis              | 전달 방식 / 저장소 비교 확인                  |
| Logout 후 Reissue 성공 | Refresh Token 삭제 누락                    | LogoutService                  | Refresh Token 무효화                          |
| Browser CORS 실패      | Origin / Header / OPTIONS 누락             | DevTools Network               | CORS 설정 수정                                |
| CSRF 403               | CSRF Token 누락                            | SecurityConfig, Request        | CSRF 정책 확인                                |
| OAuth2 Redirect 실패   | Redirect URI 불일치                        | Provider Console               | Callback URL 수정                             |
| 403에서 Reissue 반복   | Frontend errorCode 처리 오류               | Axios Interceptor              | 403은 Reissue 제외                            |

---

### [실무]

문제 해결 순서:

```text
증상 확인
→ Status Code 확인
→ 401 / 403 / CORS 구분
→ Request Header 확인
→ SecurityFilterChain 확인
→ JWT Filter 확인
→ Service 권한 검증 확인
→ Frontend Interceptor 확인
→ Test Case 추가
```

권장:

- 증상만 보고 JWT 문제로 단정하지 않는다.
- 401, 403, CORS, CSRF를 먼저 분류한다.
- 브라우저 문제는 DevTools Network를 먼저 확인한다.
- 권한 문제는 Principal과 Authority를 먼저 확인한다.
- 해결 후 동일 케이스를 테스트로 고정한다.

---

### [FAQ]

Q. Security 문제를 가장 빨리 분류하는 방법은 뭐야?
A. 먼저 Status Code를 확인하고 401, 403, CORS, CSRF 중 어디에 해당하는지 나누는 것이다.

Q. Postman은 되는데 브라우저에서 안 되면 뭘 의심해?
A. CORS Preflight, allowedOrigins, allowedHeaders, credentials 설정을 먼저 확인한다.

Q. 문제를 고친 뒤에는 뭘 해야 해?
A. 같은 문제가 재발하지 않도록 MockMvc, Postman, Frontend 통합 테스트 케이스를 추가해야 한다.

---

# 11. Part08 Checklist

## 11.1 Testing Troubleshooting Review Checklist

### [개념]

Part08 Checklist는 Security Testing, Troubleshooting, Review 문서가 Security Advanced 기준에 맞게 구성되었는지 검수하기 위한 목록이다.

---

### [핵심]

Checklist:

```md
- [ ] Security Testing 전체 목적이 포함되었는가?
- [ ] Public API Test 기준이 포함되었는가?
- [ ] Protected API Authentication Test 기준이 포함되었는가?
- [ ] Token 없음 401 테스트가 포함되었는가?
- [ ] 위조 Token 401 테스트가 포함되었는가?
- [ ] 만료 Token 401 테스트가 포함되었는가?
- [ ] Role Authorization Test 기준이 포함되었는가?
- [ ] User Token to Admin API 403 테스트가 포함되었는가?
- [ ] Resource Owner Test 기준이 포함되었는가?
- [ ] RequestBody userId 조작 테스트가 포함되었는가?
- [ ] Access Token Test 기준이 포함되었는가?
- [ ] Refresh Token Reissue Test 기준이 포함되었는가?
- [ ] Logout 후 Reissue 차단 테스트가 포함되었는가?
- [ ] CORS Test 기준이 포함되었는가?
- [ ] CSRF Test 기준이 포함되었는가?
- [ ] OAuth2 Login Test 기준이 포함되었는가?
- [ ] Frontend Auth Integration Test 기준이 포함되었는가?
- [ ] 401 Troubleshooting이 포함되었는가?
- [ ] 403 Troubleshooting이 포함되었는가?
- [ ] Reissue Troubleshooting이 포함되었는가?
- [ ] CORS Troubleshooting이 포함되었는가?
- [ ] Security Code Review Checklist가 포함되었는가?
- [ ] Common Security Anti Pattern Summary가 포함되었는가?
- [ ] Troubleshooting Matrix가 포함되었는가?
- [ ] Retrieval Queries가 충분한가?
```

---

### [실무]

전체 문서 연결:

```text
Part01 Core Concepts
→ 인증 / 인가 / SecurityContext / 401 / 403 기준

Part02 SecurityFilterChain
→ requestMatchers / JWT Filter / CORS / CSRF / Handler 설정

Part03 Password Login Logout
→ PasswordEncoder / Login / Logout 테스트 기준

Part04 JWT Access Refresh Reissue
→ Token 검증 / Reissue / Refresh Token 저장 기준

Part05 Authorization Resource Owner Check
→ Role / Owner Check / 403 테스트 기준

Part06 Exception Handling CORS CSRF
→ EntryPoint / AccessDeniedHandler / CORS / CSRF 테스트 기준

Part07 OAuth2 Frontend Integration
→ OAuth2 / Frontend Interceptor / Logout 연동 기준

Part08 Testing Troubleshooting Review
→ 전체 Security 검증 / 문제 해결 / Review 기준
```

최종 Review Flow:

```text
문서 구조 검수
→ Required Section 검수
→ FAQ 검수
→ Retrieval Queries 검수
→ Part 간 용어 통일 검수
→ Security Anti Pattern 검수
→ Testing Coverage 검수
→ 최종 RAG 업로드 대상 확정
```

---

### [FAQ]

Q. Part08에서 가장 중요한 검수 포인트는 뭐야?
A. 401/403 테스트, Token Reissue 테스트, Resource Owner 테스트, CORS 테스트, Security Review Checklist다.

Q. Part08은 Security Advanced의 마지막 문서로 적합해?
A. 적합하다. 앞선 모든 Security 문서를 테스트, 문제 해결, 검수 기준으로 마무리한다.

Q. Security Advanced 전체에서 최종적으로 확인할 것은 뭐야?
A. 인증 우회, 권한 우회, Token 노출, 비밀번호 노출, CORS/CSRF 오설정, OAuth2 Mapping 오류가 없는지 확인해야 한다.

---

# Retrieval Queries

### [FAQ]

Q. Security Testing은 왜 필요해?
A. 인증, 인가, JWT, 권한 검증은 설정 실수 하나로 API가 열리거나 막힐 수 있으므로 반드시 테스트해야 한다.

Q. Security Test에서 가장 중요한 것은 뭐야?
A. Token 없음은 401, 권한 부족은 403, 정상 권한은 200 계열인지 확인하는 것이다.

Q. 정상 로그인만 테스트하면 충분해?
A. 아니다. 위조 Token, 만료 Token, 권한 부족, 타인 리소스 접근, Reissue 실패까지 테스트해야 한다.

Q. Public API 테스트는 뭘 확인해?
A. 인증 없이 접근해야 하는 API가 Token 없이 정상 동작하는지 확인한다.

Q. 로그인 API가 401로 막히면 뭐가 문제야?
A. requestMatchers permitAll 누락 또는 JWT Filter가 Token 없음 자체를 실패 처리하는 문제일 수 있다.

Q. Public API 테스트에서 보안상 같이 볼 것은 뭐야?
A. Public API 범위가 너무 넓어 Protected API나 Admin API가 열리지 않았는지 확인해야 한다.

Q. Protected API에 Token이 없으면 몇 번 응답이 맞아?
A. 인증 정보가 없으므로 401 Unauthorized가 맞다.

Q. 위조 JWT는 어떻게 테스트해?
A. 유효한 JWT 문자열 일부를 변경해 서명 검증 실패가 401로 처리되는지 확인한다.

Q. 만료 Access Token은 401이야 403이야?
A. 인증 실패이므로 일반적으로 401이다.

Q. User Token으로 Admin API를 호출하면 몇 번 응답이 맞아?
A. 인증은 되었지만 관리자 권한이 부족하므로 403 Forbidden이 맞다.

Q. Role 권한 테스트에서 가장 자주 나는 문제는 뭐야?
A. ROLE\_ prefix 불일치로 권한이 있어도 403이 발생하는 문제다.

Q. Admin API는 Frontend에서 메뉴만 숨기면 충분해?
A. 아니다. Backend에서 ROLE_ADMIN 검증을 테스트해야 한다.

Q. Resource Owner 테스트는 왜 필요해?
A. 로그인한 사용자가 타인 리소스를 수정하거나 조회하는 권한 우회를 막기 위해 필요하다.

Q. RequestBody userId 조작 테스트도 해야 해?
A. 해야 한다. Client가 userId를 조작해도 Principal 기준으로 처리되는지 확인해야 한다.

Q. 타인 게시글 수정은 401이야 403이야?
A. 인증은 되었지만 소유자가 아니므로 일반적으로 403 Forbidden이다.

Q. Access Token 테스트에서 가장 중요한 것은 뭐야?
A. 유효 Token 인증 성공, 만료 Token 401, 위조 Token 401, SecurityContext 저장 여부다.

Q. Access Token Payload에서 확인할 것은 뭐야?
A. userId, role, exp가 있고 password, refreshToken, 민감정보가 없는지 확인한다.

Q. Token은 정상인데 Principal이 null이면 뭐가 문제야?
A. JWT Filter가 실행되지 않았거나 Authentication을 SecurityContext에 저장하지 않았을 수 있다.

Q. Refresh Token 테스트에서 가장 중요한 것은 뭐야?
A. 저장소 검증, 만료 처리, Reissue 성공, Logout 후 Reissue 차단이다.

Q. 로그아웃 후 Reissue가 성공하면 문제야?
A. 문제다. Refresh Token 삭제 또는 저장소 검증이 제대로 동작하지 않는 것이다.

Q. Rotation 테스트는 꼭 필요해?
A. Rotation을 사용하는 구조라면 이전 Refresh Token 재사용 차단 테스트가 필요하다.

Q. Logout 테스트에서 가장 중요한 것은 뭐야?
A. Refresh Token 삭제와 로그아웃 후 Reissue 차단 여부다.

Q. 로그아웃 API는 인증이 필요해?
A. 일반적으로 필요하다. 현재 인증 사용자 기준으로 Refresh Token을 무효화해야 한다.

Q. RequestBody userId로 로그아웃 처리하면 안 돼?
A. 안 된다. 조작 가능하므로 Principal userId 기준으로 처리해야 한다.

Q. CORS 테스트는 Postman으로 가능해?
A. 부족하다. CORS는 브라우저 정책이므로 실제 브라우저 요청으로 확인해야 한다.

Q. Postman은 되는데 브라우저에서 CORS 에러가 나면 뭐야?
A. CORS는 브라우저에서만 적용되므로 allowedOrigins, allowedHeaders, OPTIONS Preflight를 확인해야 한다.

Q. Authorization Header가 있으면 CORS 설정에서 뭘 봐야 해?
A. allowedHeaders에 Authorization이 포함되어 있는지 확인해야 한다.

Q. CSRF 테스트는 언제 필요해?
A. Cookie 기반 인증이나 Refresh Token Cookie 구조를 사용할 때 필요하다.

Q. Header 기반 JWT에서도 CSRF가 중요해?
A. 상대적으로 중요도는 낮지만 Token 저장 방식과 CSRF disable 근거는 확인해야 한다.

Q. Refresh Token을 Cookie에 넣으면 뭘 테스트해야 해?
A. SameSite, Secure, HttpOnly, Reissue API CSRF 위험, Cookie 자동 전송 여부를 확인해야 한다.

Q. OAuth2 Login 테스트에서 가장 중요한 것은 뭐야?
A. provider + providerId Mapping, Local User 생성 / 조회, JWT 발급, Redirect URL 검증이다.

Q. OAuth2 Provider 인증이 성공하면 무조건 로그인 성공이야?
A. 아니다. Local User Mapping, 계정 상태, 필수 정보, 서비스 정책 검증이 통과해야 한다.

Q. OAuth2 테스트에서 외부 Provider를 항상 호출해야 해?
A. 아니다. Attribute Mapping과 Local User Mapping은 Mock 데이터로 단위 테스트할 수 있다.

Q. Frontend Auth 연동 테스트에서 가장 중요한 것은 뭐야?
A. Authorization Header 첨부, 401 Reissue, 403 권한 없음, Logout 후 Reissue 차단이다.

Q. 403이 발생했을 때 Reissue가 호출되면 문제야?
A. 문제다. 403은 권한 부족이므로 Token 재발급 대상이 아니다.

Q. Reissue 무한 루프는 어떻게 테스트해?
A. Reissue API가 401을 반환할 때 추가 Reissue를 시도하지 않고 Logout 처리되는지 확인한다.

Q. 로그인했는데 401이 나와?
A. Authorization Header 누락, Bearer prefix 누락, Token 만료 / 위조, JWT Filter 미동작, SecurityContext 저장 실패를 확인해야 한다.

Q. Bearer prefix가 꼭 필요해?
A. 프로젝트 JWT Filter가 Bearer 형식을 기준으로 파싱한다면 필요하다.

Q. Public API가 401이면 뭘 봐야 해?
A. requestMatchers permitAll 설정과 JWT Filter가 Token 없음 요청을 차단하지 않는지 확인해야 한다.

Q. 토큰은 정상인데 403이 나와?
A. Role / Authority 부족, ROLE\_ prefix 불일치, Resource Owner Check 실패, Method Security 실패를 확인해야 한다.

Q. ROLE\_ prefix 때문에 403이 날 수 있어?
A. 가능하다. hasRole과 hasAuthority 사용 방식과 저장된 권한 문자열을 맞춰야 한다.

Q. 타인 리소스 접근이 403이면 정상일 수 있어?
A. 맞다. 인증은 되었지만 소유자가 아니면 403이 정상이다.

Q. 재발급이 계속 실패하면 뭘 확인해?
A. Refresh Token 전달 방식, 만료 여부, 저장소 일치 여부, 사용자 상태, Cookie 설정, Rotation 로직을 확인한다.

Q. Reissue 무한 루프는 왜 생겨?
A. 모든 401에 재발급을 시도하거나 Reissue API 실패에도 다시 Reissue를 호출하면 발생한다.

Q. CORS 에러는 JWT 문제야?
A. 아니다. 브라우저 Origin 정책 문제다. JWT 인증 실패와 구분해야 한다.

Q. Security Review에서 가장 먼저 볼 것은 뭐야?
A. SecurityFilterChain의 permitAll 범위, JWT Filter, 401/403 분리, Resource Owner Check를 먼저 확인하는 것이 좋다.

Q. 가장 치명적인 보안 실수는 뭐야?
A. 모든 API permitAll, 비밀번호 평문 저장, RequestBody userId 신뢰, JWT 민감정보 포함, Resource Owner Check 누락이다.

Q. Review Agent는 뭘 기준으로 판단해야 해?
A. 인증 우회, 권한 우회, Token 위험, 민감정보 노출, 운영 설정 노출 여부를 우선 판단해야 한다.

Q. Security Anti Pattern 중 가장 먼저 고칠 것은 뭐야?
A. 인증 우회와 권한 우회다. permitAll 과다 설정, Resource Owner Check 누락, Admin API 권한 누락을 먼저 고쳐야 한다.

Q. Token 로그 출력은 왜 위험해?
A. Token을 획득한 사람이 사용자처럼 API를 호출할 수 있으므로 인증 수단이 노출되는 문제다.

Q. Frontend Auth Anti Pattern은 Backend 보안에도 영향이 있어?
A. 있다. 401/403 처리 오류, Logout 누락, Reissue 무한 루프는 인증 흐름 전체를 불안정하게 만든다.

Q. Security 문제를 가장 빨리 분류하는 방법은 뭐야?
A. 먼저 Status Code를 확인하고 401, 403, CORS, CSRF 중 어디에 해당하는지 나누는 것이다.

Q. Postman은 되는데 브라우저에서 안 되면 뭘 의심해?
A. CORS Preflight, allowedOrigins, allowedHeaders, credentials 설정을 먼저 확인한다.

Q. 문제를 고친 뒤에는 뭘 해야 해?
A. 같은 문제가 재발하지 않도록 MockMvc, Postman, Frontend 통합 테스트 케이스를 추가해야 한다.

Q. Part08에서 가장 중요한 검수 포인트는 뭐야?
A. 401/403 테스트, Token Reissue 테스트, Resource Owner 테스트, CORS 테스트, Security Review Checklist다.

Q. Part08은 Security Advanced의 마지막 문서로 적합해?
A. 적합하다. 앞선 모든 Security 문서를 테스트, 문제 해결, 검수 기준으로 마무리한다.

Q. Security Advanced 전체에서 최종적으로 확인할 것은 뭐야?
A. 인증 우회, 권한 우회, Token 노출, 비밀번호 노출, CORS/CSRF 오설정, OAuth2 Mapping 오류가 없는지 확인해야 한다.
