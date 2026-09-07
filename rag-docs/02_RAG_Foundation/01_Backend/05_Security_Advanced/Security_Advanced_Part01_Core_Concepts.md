# Security Advanced Part01 - Core Concepts

---

# 1. Security Advanced Overview

## 1.1 Security Advanced Purpose

### [개념]

Security Advanced는 Spring Boot Backend에서 인증(Authentication), 인가(Authorization), JWT, SecurityFilterChain, SecurityContext, 401/403 예외 처리, CORS/CSRF, OAuth2 Login 흐름을 설계하고 검증하기 위한 보안 기준 문서다.

이 문서는 학습용 설명 문서가 아니라 Backend Agent / Review Agent / PM Agent가 Security 구조를 검색하고 판단하기 위한 RAG Retrieval 최적화 문서다.

---

### [핵심]

Security Advanced 핵심 목적:

- Spring Security 인증 구조 설계
- Spring Security 인가 구조 설계
- SecurityFilterChain 흐름 판단
- JWT Access Token / Refresh Token 역할 분리
- SecurityContext 저장 기준 제공
- Principal / Authority 설계 기준 제공
- Public API / Protected API 분리
- 401 Unauthorized / 403 Forbidden 구분
- AuthenticationEntryPoint / AccessDeniedHandler 분리
- CORS / CSRF 판단 기준 제공
- OAuth2 Login 연동 기준 제공
- Security Anti Pattern 탐지

---

### [실무]

2026 실무 기준에서 Spring Boot Backend 보안은 단순히 `SecurityConfig`를 작성하는 작업이 아니다.

Security 설계 흐름:

```text
Requirement
→ Public / Protected API 분리
→ Authentication 방식 선택
→ SecurityFilterChain 구성
→ Login / Token 발급
→ JWT Filter 검증
→ SecurityContext 저장
→ Authorization 적용
→ 401 / 403 Exception Handling
→ CORS / CSRF 정책 확인
→ Security Test
```

Security Advanced 문서는 아래 문서와 함께 사용된다.

```text
Java
→ Spring Boot
→ JPA Advanced
→ Security Advanced
→ API Design
→ Testing
→ Authentication Frontend Flow
```

---

### [FAQ]

Q. Security Advanced 문서는 왜 필요해?
A. Backend Agent가 Spring Security, JWT, 인증, 인가, 예외 처리, CORS, OAuth2를 일관된 기준으로 설계하고 검토하기 위해 필요하다.

Q. Security Advanced는 Spring Boot 문서와 뭐가 달라?
A. Spring Boot 문서는 일반 Backend 구조를 다루고, Security Advanced는 인증, 인가, Filter Chain, JWT, OAuth2, 보안 예외 처리를 집중적으로 다룬다.

Q. 이 문서는 사람이 읽는 설명 문서야?
A. 아니다. AI Agent Retrieval, Code Generation, Review, Validation을 위한 RAG 최적화 문서다.

---

# 2. Authentication and Authorization

## 2.1 Authentication Concept

### [개념]

Authentication은 사용자가 누구인지 확인하는 과정이다.

Spring Security에서 Authentication은 로그인, JWT 검증, OAuth2 Login 등을 통해 사용자의 신원을 확인하고 Authentication 객체를 생성하는 흐름을 의미한다.

---

### [핵심]

Authentication 핵심 키워드:

- Authentication
- Login
- JWT Validation
- OAuth2 Login
- UserDetails
- Principal
- Credentials
- PasswordEncoder
- SecurityContext
- 401 Unauthorized

Authentication 질문:

```text
이 사용자는 누구인가?
```

Authentication 실패 예:

- Token 없음
- Token 만료
- Token 위조
- 로그인 실패
- 비밀번호 불일치
- 인증 객체 없음

---

### [실무]

JWT Authentication Flow:

```text
Client Request
→ Authorization Header 확인
→ Bearer Token 추출
→ JWT Signature 검증
→ JWT Expiration 검증
→ Claims 추출
→ Authentication 객체 생성
→ SecurityContext 저장
→ Controller 접근
```

Login Authentication Flow:

```text
Login Request
→ email / password 입력
→ User 조회
→ PasswordEncoder.matches
→ Authentication 성공
→ Access Token 발급
→ Refresh Token 발급
→ Login Response
```

인증 실패는 일반적으로 401 Unauthorized로 처리한다.

---

### [FAQ]

Q. Authentication은 뭐야?
A. 사용자가 누구인지 확인하는 인증 과정이다.

Q. 로그인은 Authentication이야?
A. 맞다. 로그인은 사용자의 신원을 확인하는 대표적인 Authentication 과정이다.

Q. JWT 검증도 Authentication이야?
A. 맞다. JWT를 검증해 사용자를 식별하고 Authentication 객체를 만드는 과정이다.

Q. Authentication 실패는 몇 번 응답이야?
A. 일반적으로 401 Unauthorized 응답이다.

---

## 2.2 Authorization Concept

### [개념]

Authorization은 인증된 사용자가 특정 리소스나 기능에 접근할 권한이 있는지 확인하는 과정이다.

Spring Security에서 Authorization은 Role, Authority, Resource Owner Check, Method Security 등을 통해 수행된다.

---

### [핵심]

Authorization 핵심 키워드:

- Authorization
- Role
- Authority
- ROLE_USER
- ROLE_ADMIN
- hasRole
- hasAuthority
- @PreAuthorize
- Resource Owner Check
- AccessDeniedHandler
- 403 Forbidden

Authorization 질문:

```text
이 사용자는 접근 가능한가?
```

Authorization 실패 예:

- Role 부족
- Authority 부족
- 관리자 API 접근 실패
- 본인 리소스 아님
- Method Security 실패
- Resource Owner Check 실패

---

### [실무]

Authorization Flow:

```text
Authenticated User
→ Principal 확인
→ Authority 확인
→ SecurityFilterChain 권한 규칙 확인
→ Method Security 확인
→ Resource Owner Check 확인
→ 접근 허용 또는 거부
```

인가 실패는 일반적으로 403 Forbidden으로 처리한다.

관리자 API 예:

```java
.requestMatchers("/api/admin/**").hasRole("ADMIN")
```

본인 리소스 검증 예:

```java
if (!post.isOwner(currentUserId)) {
    throw new AccessDeniedException("권한이 없습니다.");
}
```

---

### [FAQ]

Q. Authorization은 뭐야?
A. 인증된 사용자가 특정 기능이나 리소스에 접근할 권한이 있는지 확인하는 과정이다.

Q. 로그인했는데도 403이 나올 수 있어?
A. 가능하다. 인증은 되었지만 권한이 부족하면 403 Forbidden이 발생한다.

Q. 관리자 API 접근은 Authentication이야 Authorization이야?
A. Authorization이다. 이미 인증된 사용자가 관리자 권한을 가졌는지 확인하는 과정이다.

Q. 본인 게시글 수정 권한은 어디서 검증해?
A. 일반적으로 Service에서 Resource Owner Check로 검증한다.

---

## 2.3 Authentication vs Authorization

### [개념]

Authentication은 신원 확인이고 Authorization은 권한 확인이다.

둘은 Spring Security에서 반드시 구분해야 하는 핵심 개념이다.

---

### [핵심]

| 구분      | Authentication           | Authorization       |
| --------- | ------------------------ | ------------------- |
| 의미      | 신원 확인                | 권한 확인           |
| 질문      | 누구인가?                | 접근 가능한가?      |
| 실패 응답 | 401 Unauthorized         | 403 Forbidden       |
| 대표 예   | 로그인, JWT 검증         | ROLE_ADMIN 확인     |
| 주요 객체 | Authentication           | GrantedAuthority    |
| Handler   | AuthenticationEntryPoint | AccessDeniedHandler |

---

### [실무]

전체 흐름:

```text
Login Request
→ Authentication 성공
→ Access Token 발급
→ API Request with Token
→ JWT Authentication
→ Authorization 확인
→ Controller 접근
```

주의:

- 로그인 성공은 Authentication 성공이다.
- 관리자 API 접근 가능 여부는 Authorization이다.
- Frontend에서 버튼 숨김은 Authorization이 아니다.
- Backend에서 Role / Authority / Resource Owner Check를 반드시 수행해야 한다.
- 인증 실패와 인가 실패 응답을 구분해야 한다.

---

### [FAQ]

Q. 인증과 인가는 뭐가 달라?
A. 인증은 사용자가 누구인지 확인하는 것이고, 인가는 그 사용자가 특정 기능에 접근할 권한이 있는지 확인하는 것이다.

Q. 401과 403은 어떻게 구분해?
A. 401은 인증 실패이고 403은 인증은 되었지만 권한이 부족한 상태다.

Q. Frontend에서 관리자 버튼을 숨기면 인가가 된 거야?
A. 아니다. Frontend 제한은 UX이고 실제 인가는 Backend에서 검증해야 한다.

---

# 3. SecurityContext Core

## 3.1 SecurityContext Concept

### [개념]

SecurityContext는 현재 요청에서 인증된 사용자 정보를 저장하는 Spring Security Context다.

SecurityContext 내부에는 Authentication 객체가 저장되며, Authentication 객체를 통해 Principal, Credentials, Authorities를 확인할 수 있다.

---

### [핵심]

SecurityContext 핵심 구성:

- SecurityContext
- SecurityContextHolder
- Authentication
- Principal
- Credentials
- Authorities
- GrantedAuthority
- CustomUserPrincipal
- UserDetails

SecurityContext 역할:

- 현재 요청의 인증 정보 저장
- Controller / Service에서 인증 사용자 접근 지원
- 권한 검증 기준 제공
- JWT 인증 결과 저장
- Principal 기반 사용자 식별 지원

---

### [실무]

JWT 인증 성공 후 흐름:

```text
JWT 검증 성공
→ Claims 추출
→ User 정보 조회 또는 Claim 사용
→ Authentication 객체 생성
→ SecurityContextHolder에 Authentication 저장
→ Controller / Service에서 인증 사용자 사용
```

기본 접근 예:

```java
Authentication authentication =
        SecurityContextHolder.getContext().getAuthentication();
```

Controller 접근 예:

```java
@GetMapping("/me")
public ApiResponse<UserResponse> me(
        @AuthenticationPrincipal CustomUserPrincipal principal
) {
    return ApiResponse.success(userService.getMe(principal.userId()));
}
```

권장 기준:

- JWT Filter에서 Authentication 저장
- Controller에서 RequestBody userId를 신뢰하지 않음
- 인증 사용자 기준 작업은 Principal에서 userId 추출
- SecurityContext는 요청 단위로 이해
- 비동기 처리 시 SecurityContext 전달 주의

---

### [FAQ]

Q. SecurityContext는 뭐야?
A. 현재 요청의 인증 정보를 저장하는 Spring Security Context다.

Q. SecurityContext에는 뭐가 들어 있어?
A. Authentication 객체가 들어 있고, Principal과 Authority 정보를 확인할 수 있다.

Q. JWT 인증 후 SecurityContext에 뭘 저장해?
A. 인증된 사용자 정보를 담은 Authentication 객체를 저장한다.

Q. Controller에서 userId를 RequestBody로 받아도 돼?
A. 인증 사용자 기준 작업이라면 RequestBody userId보다 SecurityContext 또는 Principal의 userId를 사용해야 한다.

---

## 3.2 Authentication Object

### [개념]

Authentication 객체는 Spring Security에서 인증 결과를 표현하는 객체다.

Authentication은 Principal, Credentials, Authorities, authenticated 상태를 포함한다.

---

### [핵심]

Authentication 구성 요소:

- Principal: 인증된 사용자 주체
- Credentials: 인증 자격 정보
- Authorities: 권한 목록
- isAuthenticated: 인증 여부
- Details: 요청 부가 정보

JWT 인증 후 Authentication 예:

```text
Principal = CustomUserPrincipal
Credentials = null
Authorities = ROLE_USER
Authenticated = true
```

---

### [실무]

JWT Filter에서 Authentication 생성 예:

```java
UsernamePasswordAuthenticationToken authentication =
        new UsernamePasswordAuthenticationToken(
                principal,
                null,
                principal.getAuthorities()
        );

SecurityContextHolder.getContext().setAuthentication(authentication);
```

권장:

- JWT 인증 후 Credentials는 null 처리 가능
- Principal에는 최소 사용자 정보만 포함
- Authorities에는 Role / Authority를 명확히 포함
- 인증 실패 시 SecurityContext에 저장하지 않음
- 이미 인증 객체가 있으면 중복 저장 주의

---

### [FAQ]

Q. Authentication 객체는 뭐야?
A. 인증된 사용자 정보와 권한 정보를 담는 Spring Security 인증 결과 객체다.

Q. Authentication에 비밀번호를 넣어야 해?
A. JWT 인증 이후에는 Credentials를 null로 두는 것이 일반적이다.

Q. Authentication은 어디서 만들어?
A. 로그인 처리 또는 JWT Filter 같은 인증 처리 지점에서 만든다.

---

# 4. Principal and Authority

## 4.1 Principal Rules

### [개념]

Principal은 인증된 사용자 주체를 의미한다.

Spring Security에서 Principal은 현재 요청을 보낸 사용자를 식별하기 위해 사용된다.

---

### [핵심]

Principal 포함 후보:

- userId
- email
- nickname
- role
- authorities
- provider
- providerId

Principal 제외 후보:

- password
- refreshToken
- accessToken
- 주민등록번호
- 민감 개인정보
- 불필요한 User Entity 전체

---

### [실무]

Custom Principal 예:

```java
public record CustomUserPrincipal(
        Long userId,
        String email,
        String role
) {
}
```

Controller 사용 예:

```java
@PostMapping("/posts")
public ApiResponse<Long> createPost(
        @AuthenticationPrincipal CustomUserPrincipal principal,
        @RequestBody PostCreateRequest request
) {
    return ApiResponse.success(
            postService.createPost(principal.userId(), request)
    );
}
```

권장:

- Principal에는 필요한 최소 정보만 넣는다.
- User Entity 전체를 Principal로 직접 노출하지 않는다.
- 민감정보를 Principal에 넣지 않는다.
- Controller에서는 Principal 기준으로 인증 사용자를 판단한다.
- userId 조작 방지를 위해 RequestBody userId를 신뢰하지 않는다.

---

### [FAQ]

Q. Principal은 뭐야?
A. 인증된 사용자 주체를 의미하며 현재 요청의 사용자 식별 정보로 사용된다.

Q. Principal에는 뭘 넣어야 해?
A. userId, email, role처럼 인증 사용자 식별과 권한 판단에 필요한 최소 정보를 넣는 것이 좋다.

Q. User Entity 전체를 Principal로 써도 돼?
A. 권장하지 않는다. 민감정보 노출과 의존성 증가 위험이 있으므로 Custom Principal을 사용하는 것이 좋다.

---

## 4.2 Authority Rules

### [개념]

Authority는 인증된 사용자가 가진 권한을 의미한다.

Spring Security는 Authority를 기준으로 API 접근 허용 여부를 판단할 수 있다.

---

### [핵심]

Authority 핵심 키워드:

- GrantedAuthority
- SimpleGrantedAuthority
- ROLE_USER
- ROLE_ADMIN
- hasRole
- hasAuthority
- @PreAuthorize
- Method Security

Role / Authority 예:

```text
ROLE_USER
ROLE_ADMIN
POST_WRITE
POST_DELETE
```

---

### [실무]

Authority 생성 예:

```java
List<GrantedAuthority> authorities = List.of(
        new SimpleGrantedAuthority("ROLE_USER")
);
```

SecurityFilterChain 예:

```java
.requestMatchers("/api/admin/**").hasRole("ADMIN")
.requestMatchers("/api/posts/**").authenticated()
```

Method Security 예:

```java
@PreAuthorize("hasRole('ADMIN')")
public void deleteUser(Long userId) {
}
```

권장:

- Role naming 규칙을 통일한다.
- `ROLE_` prefix 정책을 명확히 한다.
- `hasRole`과 `hasAuthority` 사용 기준을 문서화한다.
- Frontend 권한 표시는 UX용으로만 본다.
- Backend에서 최종 권한 검증을 수행한다.

---

### [FAQ]

Q. Authority는 뭐야?
A. 인증된 사용자가 가진 권한 정보다.

Q. ROLE*USER와 USER는 달라?
A. Spring Security에서 Role 처리 시 `ROLE*` prefix가 관여할 수 있으므로 프로젝트 권한 이름 규칙을 통일해야 한다.

Q. hasRole과 hasAuthority는 뭐가 달라?
A. hasRole은 일반적으로 `ROLE_` prefix 처리가 관여하고, hasAuthority는 권한 문자열을 직접 비교한다.

Q. 권한 검증은 Frontend에서만 해도 돼?
A. 아니다. Frontend 권한 표시는 UX이고 최종 보안 검증은 Backend에서 해야 한다.

---

# 5. Public API and Protected API

## 5.1 Public API Rules

### [개념]

Public API는 인증 없이 접근 가능한 API다.

회원가입, 로그인, 공개 조회, Health Check 같은 기능은 Public API로 분리할 수 있다.

---

### [핵심]

Public API 후보:

- 회원가입
- 로그인
- 토큰 재발급
- 공개 게시글 목록
- 공개 게시글 상세
- 공개 축제 목록
- 공개 축제 상세
- Swagger 개발 환경
- Health Check

Public API 키워드:

- permitAll
- requestMatchers
- anonymous access
- no token required

---

### [실무]

SecurityFilterChain 예:

```java
.authorizeHttpRequests(auth -> auth
        .requestMatchers("/api/auth/signup").permitAll()
        .requestMatchers("/api/auth/login").permitAll()
        .requestMatchers("/api/auth/reissue").permitAll()
        .requestMatchers("/api/public/**").permitAll()
        .anyRequest().authenticated()
)
```

주의:

- 임시 permitAll을 운영에 남기지 않는다.
- Swagger 허용은 profile 기준으로 분리한다.
- 재발급 API는 Public처럼 보이지만 Refresh Token 검증이 필요하다.
- 공개 조회 API와 사용자 맞춤 API를 구분한다.

---

### [FAQ]

Q. Public API는 뭐야?
A. 인증 없이 접근 가능한 API다.

Q. 로그인 API도 인증이 필요해?
A. 아니다. 로그인은 인증 전 접근해야 하므로 permitAll 대상이다.

Q. 토큰 재발급 API는 Public API야?
A. 경로 접근은 permitAll일 수 있지만 Refresh Token 검증은 반드시 필요하다.

---

## 5.2 Protected API Rules

### [개념]

Protected API는 인증 또는 특정 권한이 필요한 API다.

내 정보 조회, 게시글 작성, 댓글 작성, 결제 내역, 알림 조회, 관리자 API는 Protected API로 분리한다.

---

### [핵심]

Protected API 후보:

- 내 정보 조회
- 내 정보 수정
- 게시글 작성
- 게시글 수정
- 댓글 작성
- 좋아요 / 찜
- 알림 조회
- 결제 내역 조회
- 관리자 API
- 사용자별 데이터 조회

Protected API 키워드:

- authenticated
- hasRole
- hasAuthority
- @PreAuthorize
- Resource Owner Check
- Principal required

---

### [실무]

SecurityFilterChain 예:

```java
.authorizeHttpRequests(auth -> auth
        .requestMatchers("/api/admin/**").hasRole("ADMIN")
        .requestMatchers("/api/users/me").authenticated()
        .requestMatchers("/api/posts/**").authenticated()
        .anyRequest().authenticated()
)
```

설계 흐름:

```text
API 목록 작성
→ 인증 필요 여부 표시
→ 권한 필요 여부 표시
→ Public / Protected 분리
→ SecurityFilterChain matcher 작성
→ Controller / Service 권한 보완
→ 테스트 작성
```

주의:

- 모든 API를 permitAll로 열지 않는다.
- Backend API 보호와 Frontend Route 보호를 혼동하지 않는다.
- Resource Owner Check는 Service에서 보완한다.
- 관리자 API는 Role 검증 필수다.

---

### [FAQ]

Q. Protected API는 뭐야?
A. 인증 또는 특정 권한이 있어야 접근 가능한 API다.

Q. Frontend에서 페이지 접근을 막으면 Backend API 보안은 필요 없어?
A. 아니다. Frontend 제한은 UX이고 실제 API 보호는 Backend Security에서 해야 한다.

Q. 모든 API를 permitAll로 열고 Service에서 검사하면 돼?
A. 권장하지 않는다. SecurityFilterChain에서 기본 접근 제어를 하고 Service에서 세부 권한을 보완하는 것이 좋다.

---

# 6. 401 and 403 Core Rules

## 6.1 401 Unauthorized

### [개념]

401 Unauthorized는 인증 정보가 없거나 유효하지 않아 사용자가 누구인지 확인할 수 없는 상태다.

---

### [핵심]

401 발생 상황:

- Authorization Header 없음
- Bearer prefix 누락
- Access Token 만료
- JWT 서명 오류
- JWT 형식 오류
- JWT Filter 미등록
- SecurityContext 저장 실패
- 로그인 실패
- 인증 객체 없음

Handler:

```text
AuthenticationEntryPoint
```

---

### [실무]

권장 응답:

```text
HTTP 401 Unauthorized
errorCode: UNAUTHORIZED
message: 인증이 필요합니다.
```

JWT 만료 응답 예:

```text
HTTP 401 Unauthorized
errorCode: TOKEN_EXPIRED
message: 인증이 만료되었습니다.
```

주의:

- Token 위조 상세 원인을 과도하게 노출하지 않는다.
- Stack trace를 응답하지 않는다.
- Frontend가 재발급 또는 재로그인을 판단할 수 있도록 errorCode를 제공한다.
- 인증 실패와 권한 실패를 혼동하지 않는다.

---

### [FAQ]

Q. 401은 언제 발생해?
A. 인증 정보가 없거나 유효하지 않아 사용자가 누구인지 확인할 수 없을 때 발생한다.

Q. JWT 만료는 401이야 403이야?
A. 일반적으로 인증 실패이므로 401로 처리한다.

Q. 로그인했는데 401이 나와?
A. Authorization Header 누락, Token 만료, Token 위조, JWT Filter 오류, SecurityContext 저장 실패를 확인해야 한다.

---

## 6.2 403 Forbidden

### [개념]

403 Forbidden은 인증은 되었지만 접근 권한이 부족한 상태다.

---

### [핵심]

403 발생 상황:

- Role 부족
- Authority 부족
- ROLE\_ prefix 불일치
- 관리자 API 접근 실패
- Resource Owner Check 실패
- Method Security 실패
- 본인 리소스 아님

Handler:

```text
AccessDeniedHandler
```

---

### [실무]

권장 응답:

```text
HTTP 403 Forbidden
errorCode: ACCESS_DENIED
message: 접근 권한이 없습니다.
```

주의:

- 인증 실패와 권한 실패를 구분한다.
- Resource 존재 여부를 과도하게 노출하지 않는다.
- 관리자 권한 실패는 403으로 처리한다.
- Frontend는 403 발생 시 권한 없음 안내를 처리한다.

---

### [FAQ]

Q. 403은 언제 발생해?
A. 인증은 되었지만 해당 리소스나 기능에 접근할 권한이 없을 때 발생한다.

Q. 로그인했는데 403이 나올 수 있어?
A. 가능하다. 로그인은 되었지만 Role, Authority, Resource Owner 조건을 만족하지 못하면 403이 발생한다.

Q. 토큰은 정상인데 403이 나와?
A. Role / Authority 부족, ROLE\_ prefix 불일치, Resource Owner Check 실패를 확인해야 한다.

---

## 6.3 401 vs 403

### [개념]

401은 인증 실패이고 403은 인가 실패다.

Spring Security에서 401과 403은 Handler와 원인이 다르므로 반드시 구분해야 한다.

---

### [핵심]

| 비교          | 401 Unauthorized         | 403 Forbidden                |
| ------------- | ------------------------ | ---------------------------- |
| 의미          | 인증 실패                | 권한 부족                    |
| 사용자 상태   | 누구인지 확인 불가       | 로그인은 됨                  |
| 예            | Token 없음 / 만료 / 위조 | Role 부족 / 본인 리소스 아님 |
| Handler       | AuthenticationEntryPoint | AccessDeniedHandler          |
| Frontend 처리 | 재발급 / 재로그인        | 권한 없음 안내               |

---

### [실무]

Debug 기준:

```text
401 발생
→ Header 확인
→ Token 검증
→ JWT Filter 확인
→ SecurityContext 저장 확인
→ EntryPoint 확인
```

```text
403 발생
→ Authentication 존재 확인
→ Principal Role 확인
→ Authority 문자열 확인
→ hasRole / hasAuthority 확인
→ Resource Owner Check 확인
→ AccessDeniedHandler 확인
```

---

### [FAQ]

Q. 401과 403 차이는?
A. 401은 인증 실패이고 403은 인증은 되었지만 권한이 부족한 상태다.

Q. Token이 없으면 401이야 403이야?
A. Token이 없어서 사용자를 확인할 수 없으면 401이다.

Q. User Token으로 Admin API를 호출하면 401이야 403이야?
A. 사용자는 인증되었지만 관리자 권한이 부족하므로 403이다.

---

# 7. Security Anti Pattern Overview

## 7.1 Common Security Mistakes

### [개념]

Security Anti Pattern은 인증, 인가, JWT, CORS, CSRF, 예외 처리에서 자주 발생하는 잘못된 구현 방식이다.

Review Agent는 Security Anti Pattern을 탐지하고 수정 방향을 제시해야 한다.

---

### [핵심]

대표 Anti Pattern:

- Authentication과 Authorization 혼동
- 401과 403 혼동
- 모든 API를 permitAll로 설정
- Frontend 권한 체크만 신뢰
- RequestBody userId 신뢰
- 비밀번호 평문 저장
- PasswordEncoder.matches 미사용
- JWT Payload에 민감정보 저장
- Token 만료 검증 누락
- Refresh Token 저장 / 무효화 전략 없음
- 로그에 Token 출력
- ROLE\_ prefix 불일치
- hasRole / hasAuthority 혼동
- JWT Filter 미등록
- JWT Filter 위치 오류
- SecurityContext 저장 누락
- CORS를 인증 문제로 오해
- CORS 전체 허용을 운영에 남김
- CSRF disable을 구조 검토 없이 적용
- EntryPoint / AccessDeniedHandler 미구분
- OAuth2 사용자를 email만으로 식별
- 관리자 API 권한 검증 누락

---

### [실무]

Review 우선순위:

```text
Authentication / Authorization 구분
→ Public / Protected API 분리
→ PasswordEncoder 적용
→ JWT 검증 기준
→ SecurityContext 저장
→ Role / Authority 규칙
→ Resource Owner Check
→ 401 / 403 Handler 분리
→ CORS / CSRF 정책
→ Token / Password 로그 노출 확인
```

Anti Pattern 예:

```text
문제:
Controller에서 request.userId로 내 정보 수정 처리

원인:
사용자가 userId를 조작할 수 있음

해결:
SecurityContext의 Principal userId를 기준으로 처리
```

---

### [FAQ]

Q. Spring Security 초보가 가장 많이 하는 실수는?
A. 401/403 혼동, JWT Filter 누락, SecurityContext 저장 누락, Role prefix 불일치, CORS 문제 오해가 많다.

Q. userId를 RequestBody로 받아서 본인 확인하면 안 돼?
A. 안 된다. 사용자가 조작할 수 있으므로 인증 Principal의 userId를 기준으로 검증해야 한다.

Q. JWT Payload에 개인정보를 넣어도 돼?
A. 안 된다. JWT Payload는 쉽게 디코딩될 수 있으므로 민감정보를 넣으면 안 된다.

---

# 8. Security Core Flow

## 8.1 Request Security Flow

### [개념]

Spring Security Request Flow는 HTTP 요청이 Controller에 도달하기 전에 SecurityFilterChain을 통과하며 인증과 인가를 수행하는 흐름이다.

---

### [핵심]

핵심 흐름:

```text
Request
→ SecurityFilterChain
→ CORS / CSRF 처리
→ JWT Filter
→ Authentication 생성
→ SecurityContext 저장
→ Authorization 확인
→ Controller
→ Response
```

주요 판단:

- 요청 경로가 Public API인가?
- Authorization Header가 있는가?
- JWT가 유효한가?
- SecurityContext에 Authentication이 저장되었는가?
- 필요한 Role / Authority가 있는가?
- Resource Owner 조건을 만족하는가?

---

### [실무]

Public API 흐름:

```text
Request
→ SecurityFilterChain
→ permitAll matcher
→ Controller
```

Protected API 정상 흐름:

```text
Request
→ JWT Filter
→ Token 검증 성공
→ Authentication 생성
→ SecurityContext 저장
→ Authorization 성공
→ Controller
```

Protected API 인증 실패 흐름:

```text
Request
→ JWT Filter
→ Token 없음 또는 유효하지 않음
→ AuthenticationEntryPoint
→ 401 Unauthorized
```

Protected API 인가 실패 흐름:

```text
Request
→ JWT Filter
→ Authentication 성공
→ Authorization 실패
→ AccessDeniedHandler
→ 403 Forbidden
```

---

### [FAQ]

Q. 요청은 Controller에 바로 도달해?
A. 아니다. Spring Security를 사용하면 Controller 전에 SecurityFilterChain을 통과한다.

Q. JWT Filter는 왜 필요해?
A. 요청 Header의 Token을 검증하고 Authentication을 SecurityContext에 저장하기 위해 필요하다.

Q. 인증 성공 후에도 인가 검증이 필요해?
A. 필요하다. 인증은 신원 확인이고 인가는 접근 권한 확인이다.

---

# 9. Part01 Checklist

## 9.1 Core Concept Checklist

### [개념]

Part01 검수는 Security Advanced 전체 문서의 기본 개념이 정확히 잡혔는지 확인하는 과정이다.

---

### [핵심]

Checklist:

```md
- [ ] Security Advanced 목적이 명확한가?
- [ ] Authentication 개념이 포함되었는가?
- [ ] Authorization 개념이 포함되었는가?
- [ ] Authentication vs Authorization 비교가 포함되었는가?
- [ ] SecurityContext 개념이 포함되었는가?
- [ ] Authentication 객체 설명이 포함되었는가?
- [ ] Principal 기준이 포함되었는가?
- [ ] Authority 기준이 포함되었는가?
- [ ] Public API 기준이 포함되었는가?
- [ ] Protected API 기준이 포함되었는가?
- [ ] 401 Unauthorized 기준이 포함되었는가?
- [ ] 403 Forbidden 기준이 포함되었는가?
- [ ] 401 vs 403 비교가 포함되었는가?
- [ ] Security Anti Pattern 개요가 포함되었는가?
- [ ] Request Security Flow가 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

Part01이 안정적이어야 이후 문서가 흔들리지 않는다.

후속 문서 연결:

```text
Part01 Core Concepts
→ Part02 SecurityFilterChain
→ Part03 Password and Login
→ Part04 JWT Access Token Refresh Token
→ Part05 Authorization and Resource Owner Check
→ Part06 CORS CSRF Exception Handling
→ Part07 OAuth2 Frontend Integration
→ Part08 Security Testing Troubleshooting
```

---

### [FAQ]

Q. Part01에서 가장 중요한 개념은 뭐야?
A. Authentication과 Authorization 구분, SecurityContext, Principal, Authority, 401/403 구분이다.

Q. Part01을 먼저 만드는 이유는 뭐야?
A. 이후 JWT, SecurityFilterChain, 예외 처리, 권한 검증 문서가 이 개념을 기준으로 연결되기 때문이다.

---

# Retrieval Queries

### [FAQ]

Q. Security Advanced 문서는 왜 필요해?
A. Backend Agent가 Spring Security, JWT, 인증, 인가, 예외 처리, CORS, OAuth2를 일관된 기준으로 설계하고 검토하기 위해 필요하다.

Q. Security Advanced는 Spring Boot 문서와 뭐가 달라?
A. Spring Boot 문서는 일반 Backend 구조를 다루고, Security Advanced는 인증, 인가, Filter Chain, JWT, OAuth2, 보안 예외 처리를 집중적으로 다룬다.

Q. Authentication은 뭐야?
A. 사용자가 누구인지 확인하는 인증 과정이다.

Q. Authorization은 뭐야?
A. 인증된 사용자가 특정 기능이나 리소스에 접근할 권한이 있는지 확인하는 과정이다.

Q. 인증과 인가는 뭐가 달라?
A. 인증은 사용자가 누구인지 확인하는 것이고, 인가는 그 사용자가 특정 기능에 접근할 권한이 있는지 확인하는 것이다.

Q. 로그인은 Authentication이야?
A. 맞다. 로그인은 사용자의 신원을 확인하는 대표적인 Authentication 과정이다.

Q. JWT 검증도 Authentication이야?
A. 맞다. JWT를 검증해 사용자를 식별하고 Authentication 객체를 만드는 과정이다.

Q. 관리자 API 접근은 Authorization이야?
A. 맞다. 인증된 사용자가 관리자 권한을 가졌는지 확인하는 Authorization 과정이다.

Q. 로그인했는데도 403이 나올 수 있어?
A. 가능하다. 인증은 되었지만 권한이 부족하면 403 Forbidden이 발생한다.

Q. Frontend에서 관리자 버튼을 숨기면 인가가 된 거야?
A. 아니다. Frontend 제한은 UX이고 실제 인가는 Backend에서 검증해야 한다.

Q. SecurityContext는 뭐야?
A. 현재 요청의 인증 정보를 저장하는 Spring Security Context다.

Q. SecurityContext에는 뭐가 들어 있어?
A. Authentication 객체가 들어 있고, Principal과 Authority 정보를 확인할 수 있다.

Q. JWT 인증 후 SecurityContext에 뭘 저장해?
A. 인증된 사용자 정보를 담은 Authentication 객체를 저장한다.

Q. Authentication 객체는 뭐야?
A. 인증된 사용자 정보와 권한 정보를 담는 Spring Security 인증 결과 객체다.

Q. Authentication에 비밀번호를 넣어야 해?
A. JWT 인증 이후에는 Credentials를 null로 두는 것이 일반적이다.

Q. Principal은 뭐야?
A. 인증된 사용자 주체를 의미하며 현재 요청의 사용자 식별 정보로 사용된다.

Q. Principal에는 뭘 넣어야 해?
A. userId, email, role처럼 인증 사용자 식별과 권한 판단에 필요한 최소 정보를 넣는 것이 좋다.

Q. User Entity 전체를 Principal로 써도 돼?
A. 권장하지 않는다. 민감정보 노출과 의존성 증가 위험이 있으므로 Custom Principal을 사용하는 것이 좋다.

Q. Authority는 뭐야?
A. 인증된 사용자가 가진 권한 정보다.

Q. ROLE*USER와 USER는 달라?
A. Spring Security에서 Role 처리 시 `ROLE*` prefix가 관여할 수 있으므로 프로젝트 권한 이름 규칙을 통일해야 한다.

Q. hasRole과 hasAuthority는 뭐가 달라?
A. hasRole은 일반적으로 `ROLE_` prefix 처리가 관여하고, hasAuthority는 권한 문자열을 직접 비교한다.

Q. Public API는 뭐야?
A. 인증 없이 접근 가능한 API다.

Q. Protected API는 뭐야?
A. 인증 또는 특정 권한이 있어야 접근 가능한 API다.

Q. 로그인 API도 인증이 필요해?
A. 아니다. 로그인은 인증 전 접근해야 하므로 permitAll 대상이다.

Q. 토큰 재발급 API는 Public API야?
A. 경로 접근은 permitAll일 수 있지만 Refresh Token 검증은 반드시 필요하다.

Q. Frontend에서 페이지 접근을 막으면 Backend API 보안은 필요 없어?
A. 아니다. Frontend 제한은 UX이고 실제 API 보호는 Backend Security에서 해야 한다.

Q. 모든 API를 permitAll로 열고 Service에서 검사하면 돼?
A. 권장하지 않는다. SecurityFilterChain에서 기본 접근 제어를 하고 Service에서 세부 권한을 보완하는 것이 좋다.

Q. 401은 언제 발생해?
A. 인증 정보가 없거나 유효하지 않아 사용자가 누구인지 확인할 수 없을 때 발생한다.

Q. 403은 언제 발생해?
A. 인증은 되었지만 해당 리소스나 기능에 접근할 권한이 없을 때 발생한다.

Q. 401과 403 차이는?
A. 401은 인증 실패이고 403은 인증은 되었지만 권한이 부족한 상태다.

Q. JWT 만료는 401이야 403이야?
A. 일반적으로 인증 실패이므로 401로 처리한다.

Q. User Token으로 Admin API를 호출하면 401이야 403이야?
A. 사용자는 인증되었지만 관리자 권한이 부족하므로 403이다.

Q. 로그인했는데 401이 나와?
A. Authorization Header 누락, Token 만료, Token 위조, JWT Filter 오류, SecurityContext 저장 실패를 확인해야 한다.

Q. 토큰은 정상인데 403이 나와?
A. Role / Authority 부족, ROLE\_ prefix 불일치, Resource Owner Check 실패를 확인해야 한다.

Q. Spring Security 초보가 가장 많이 하는 실수는?
A. 401/403 혼동, JWT Filter 누락, SecurityContext 저장 누락, Role prefix 불일치, CORS 문제 오해가 많다.

Q. userId를 RequestBody로 받아서 본인 확인하면 안 돼?
A. 안 된다. 사용자가 조작할 수 있으므로 인증 Principal의 userId를 기준으로 검증해야 한다.

Q. JWT Payload에 개인정보를 넣어도 돼?
A. 안 된다. JWT Payload는 쉽게 디코딩될 수 있으므로 민감정보를 넣으면 안 된다.

Q. Spring Security 요청 흐름은 어떻게 돼?
A. Request가 SecurityFilterChain을 통과하고 JWT Filter, Authentication, SecurityContext 저장, Authorization 확인 후 Controller에 도달한다.

Q. JWT Filter는 왜 필요해?
A. 요청 Header의 Token을 검증하고 Authentication을 SecurityContext에 저장하기 위해 필요하다.

Q. 인증 성공 후에도 인가 검증이 필요해?
A. 필요하다. 인증은 신원 확인이고 인가는 접근 권한 확인이다.

Q. Part01에서 가장 중요한 개념은 뭐야?
A. Authentication과 Authorization 구분, SecurityContext, Principal, Authority, 401/403 구분이다.

Q. Security Advanced Part01 다음 문서는 뭐야?
A. SecurityFilterChain, Password/Login, JWT, Authorization, CORS/CSRF, OAuth2, Testing 문서로 이어지는 것이 좋다.
