# Security Advanced Part02 - SecurityFilterChain

---

# 1. SecurityFilterChain Overview

## 1.1 SecurityFilterChain Concept

### [개념]

SecurityFilterChain은 Spring Security에서 HTTP 요청이 Controller에 도달하기 전에 통과하는 보안 Filter 체인이다.

SecurityFilterChain은 인증(Authentication), 인가(Authorization), CORS, CSRF, Session 정책, JWT Filter 등록, 예외 처리, 접근 제어 규칙을 구성하는 핵심 보안 설정이다.

---

### [핵심]

SecurityFilterChain 핵심 키워드:

- SecurityFilterChain
- HttpSecurity
- Security Filter
- Filter Chain
- authorizeHttpRequests
- requestMatchers
- permitAll
- authenticated
- hasRole
- hasAuthority
- sessionManagement
- SessionCreationPolicy.STATELESS
- csrf
- cors
- exceptionHandling
- addFilterBefore
- AuthenticationEntryPoint
- AccessDeniedHandler

SecurityFilterChain 역할:

- Public API 접근 허용
- Protected API 인증 요구
- Admin API 권한 요구
- JWT Filter 등록
- Stateless Session 정책 설정
- CORS 설정 연결
- CSRF 정책 설정
- 401 / 403 예외 Handler 연결

---

### [실무]

2026 실무 기준 Spring Boot 3.x / Spring Security 6.x에서는 `WebSecurityConfigurerAdapter`가 아니라 `SecurityFilterChain` Bean 기반 설정을 우선 사용한다.

기본 구조:

```java
@Bean
public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
    return http
            .csrf(csrf -> csrf.disable())
            .cors(cors -> {})
            .sessionManagement(session ->
                    session.sessionCreationPolicy(SessionCreationPolicy.STATELESS)
            )
            .authorizeHttpRequests(auth -> auth
                    .requestMatchers("/api/auth/**").permitAll()
                    .requestMatchers("/api/admin/**").hasRole("ADMIN")
                    .anyRequest().authenticated()
            )
            .build();
}
```

실무 설계 흐름:

```text
API 목록 확인
→ Public / Protected / Admin API 분리
→ Session 정책 결정
→ CSRF 정책 결정
→ CORS 설정 연결
→ JWT Filter 위치 결정
→ 401 / 403 Handler 등록
→ requestMatchers 순서 검토
→ Security Test 수행
```

---

### [FAQ]

Q. SecurityFilterChain은 뭐야?
A. 요청이 Controller에 도달하기 전에 인증, 인가, CORS, CSRF, 예외 처리를 수행하는 Spring Security Filter 체인이다.

Q. Spring Security 6에서도 WebSecurityConfigurerAdapter를 써야 해?
A. 아니다. 신규 Spring Security 6 기준에서는 SecurityFilterChain Bean 기반 설정을 우선 사용한다.

Q. SecurityFilterChain에서 가장 중요한 설정은 뭐야?
A. Public / Protected API 분리, JWT Filter 등록, Stateless Session, 401/403 Handler, requestMatchers 순서가 중요하다.

---

# 2. Request Matcher Rules

## 2.1 requestMatchers Concept

### [개념]

`requestMatchers`는 특정 HTTP 요청 경로와 Method에 대해 인증 또는 권한 규칙을 적용하는 Spring Security 설정이다.

API 경로별로 `permitAll`, `authenticated`, `hasRole`, `hasAuthority` 같은 접근 정책을 지정한다.

---

### [핵심]

requestMatchers 핵심 키워드:

- requestMatchers
- permitAll
- authenticated
- hasRole
- hasAuthority
- anyRequest
- HTTP Method
- Path Pattern
- Public API
- Protected API
- Admin API

접근 정책 예:

```text
/api/auth/**      → permitAll
/api/public/**    → permitAll
/api/users/me     → authenticated
/api/admin/**     → hasRole("ADMIN")
anyRequest        → authenticated
```

---

### [실무]

권장 구조:

```java
.authorizeHttpRequests(auth -> auth
        .requestMatchers("/api/auth/signup").permitAll()
        .requestMatchers("/api/auth/login").permitAll()
        .requestMatchers("/api/auth/reissue").permitAll()
        .requestMatchers("/api/public/**").permitAll()
        .requestMatchers("/api/admin/**").hasRole("ADMIN")
        .anyRequest().authenticated()
)
```

HTTP Method 기준 분리 예:

```java
.authorizeHttpRequests(auth -> auth
        .requestMatchers(HttpMethod.GET, "/api/posts/**").permitAll()
        .requestMatchers(HttpMethod.POST, "/api/posts/**").authenticated()
        .requestMatchers(HttpMethod.DELETE, "/api/posts/**").authenticated()
        .anyRequest().authenticated()
)
```

권장:

- API 목록을 먼저 작성한다.
- Public API와 Protected API를 명확히 분리한다.
- 관리자 API는 별도 matcher로 분리한다.
- GET 공개 조회와 POST 작성 API를 Method 기준으로 구분한다.
- `anyRequest().authenticated()`를 마지막에 둔다.

---

### [FAQ]

Q. requestMatchers는 뭐야?
A. 특정 요청 경로와 Method에 대해 인증 또는 권한 규칙을 적용하는 설정이다.

Q. GET 조회는 공개이고 POST 작성은 로그인 필요하게 할 수 있어?
A. 가능하다. HTTP Method 기준 requestMatchers를 사용해 GET은 permitAll, POST는 authenticated로 분리할 수 있다.

Q. anyRequest는 어디에 둬야 해?
A. 일반적으로 가장 마지막에 두어 앞에서 처리되지 않은 모든 요청에 기본 정책을 적용한다.

---

## 2.2 Matcher Order Rules

### [개념]

SecurityFilterChain에서 requestMatchers 순서는 중요하다.

더 구체적인 경로를 먼저 선언하고, 넓은 범위의 규칙은 뒤에 배치해야 한다.

---

### [핵심]

순서 기준:

- 구체적인 경로 먼저
- 관리자 경로 먼저
- 인증 예외 경로 먼저
- 넓은 wildcard 경로 나중
- anyRequest는 마지막

좋은 순서:

```text
/api/auth/login
→ /api/auth/reissue
→ /api/admin/**
→ /api/public/**
→ anyRequest
```

위험한 순서:

```text
/api/**
→ /api/admin/**
→ anyRequest
```

---

### [실무]

좋은 예:

```java
.authorizeHttpRequests(auth -> auth
        .requestMatchers("/api/auth/**").permitAll()
        .requestMatchers("/api/admin/**").hasRole("ADMIN")
        .requestMatchers("/api/users/me").authenticated()
        .anyRequest().authenticated()
)
```

위험한 예:

```java
.authorizeHttpRequests(auth -> auth
        .requestMatchers("/api/**").permitAll()
        .requestMatchers("/api/admin/**").hasRole("ADMIN")
        .anyRequest().authenticated()
)
```

문제:

```text
/api/** permitAll이 먼저 적용되면
/api/admin/**도 인증 없이 접근될 위험이 있다.
```

검수 기준:

- `/api/**.permitAll()` 같은 넓은 허용 규칙이 있는지 확인한다.
- 관리자 API가 Public matcher에 포함되지 않는지 확인한다.
- Swagger 허용 경로가 운영 환경에 남아 있지 않은지 확인한다.
- `anyRequest().permitAll()`이 사용되지 않았는지 확인한다.

---

### [FAQ]

Q. requestMatchers 순서가 중요해?
A. 중요하다. 더 구체적인 경로를 먼저 선언하고 전체 규칙은 뒤에 두는 것이 좋다.

Q. /api/\*\*를 permitAll로 열어도 돼?
A. 권장하지 않는다. 관리자 API나 보호 API까지 열릴 수 있으므로 필요한 Public API만 명시적으로 허용해야 한다.

Q. anyRequest().permitAll()을 쓰면 안 돼?
A. 개발 중 임시 사용은 가능하지만 운영 코드에 남기면 대부분의 API가 보호되지 않는 심각한 보안 문제가 된다.

---

# 3. Public API Configuration

## 3.1 Public API Matcher Rules

### [개념]

Public API Matcher는 인증 없이 접근 가능한 API 경로를 SecurityFilterChain에서 명시적으로 허용하는 설정이다.

회원가입, 로그인, 토큰 재발급, 공개 조회, Health Check, 개발용 Swagger 경로가 Public API 후보가 될 수 있다.

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
- Health Check
- Swagger 개발 환경

Public API 설정 키워드:

- permitAll
- requestMatchers
- anonymous access
- no token required
- public endpoint

---

### [실무]

Public API 예:

```java
.requestMatchers("/api/auth/signup").permitAll()
.requestMatchers("/api/auth/login").permitAll()
.requestMatchers("/api/auth/reissue").permitAll()
.requestMatchers(HttpMethod.GET, "/api/festivals/**").permitAll()
.requestMatchers("/actuator/health").permitAll()
```

Swagger 개발 환경 예:

```java
.requestMatchers(
        "/swagger-ui/**",
        "/v3/api-docs/**"
).permitAll()
```

주의:

- Swagger 허용은 개발 profile 기준으로 분리하는 것이 좋다.
- 운영 환경에서 불필요한 API 문서 공개를 피한다.
- 토큰 재발급 API는 접근은 Public이지만 Refresh Token 검증은 반드시 수행한다.
- 공개 조회 API와 사용자 맞춤 조회 API를 구분한다.
- Public API라도 입력값 검증과 Rate Limit 정책을 고려한다.

---

### [FAQ]

Q. Public API는 SecurityFilterChain에서 어떻게 설정해?
A. requestMatchers에 Public API 경로를 지정하고 permitAll을 적용한다.

Q. 로그인 API는 permitAll이 맞아?
A. 맞다. 로그인은 인증 전 접근해야 하므로 permitAll 대상이다.

Q. 토큰 재발급 API도 permitAll이야?
A. 경로 접근은 permitAll일 수 있지만 Refresh Token 검증은 Service 또는 Filter에서 반드시 수행해야 한다.

Q. Swagger도 permitAll로 열어도 돼?
A. 개발 환경에서는 가능하지만 운영 환경에서는 profile 분리나 접근 제한을 검토해야 한다.

---

## 3.2 Public API Anti Pattern

### [개념]

Public API Anti Pattern은 인증이 필요한 API를 실수로 permitAll로 열어두는 잘못된 보안 설정이다.

---

### [핵심]

위험한 Public API 설정:

- 모든 API permitAll
- `/api/**` permitAll
- 관리자 API permitAll
- 사용자 정보 API permitAll
- 결제 내역 API permitAll
- 알림 API permitAll
- 게시글 작성 API permitAll
- 임시 Swagger 허용 운영 반영

Anti Pattern 예:

```java
.anyRequest().permitAll()
```

```java
.requestMatchers("/api/**").permitAll()
```

---

### [실무]

검수 기준:

```text
SecurityConfig 확인
→ permitAll 경로 목록 추출
→ API 명세와 비교
→ 인증 필요 API가 포함되었는지 확인
→ 관리자 API 포함 여부 확인
→ 사용자 개인 데이터 API 포함 여부 확인
→ 운영 profile 노출 여부 확인
```

수정 방향:

```java
.authorizeHttpRequests(auth -> auth
        .requestMatchers("/api/auth/**").permitAll()
        .requestMatchers(HttpMethod.GET, "/api/posts/**").permitAll()
        .requestMatchers("/api/admin/**").hasRole("ADMIN")
        .anyRequest().authenticated()
)
```

권장:

- Public API를 최소화한다.
- 보호 API는 기본적으로 authenticated 처리한다.
- 관리자 API는 hasRole 또는 hasAuthority를 적용한다.
- 사용자 데이터 API는 Principal 기반 검증을 추가한다.

---

### [FAQ]

Q. 모든 API를 permitAll로 열고 Service에서 검사하면 돼?
A. 권장하지 않는다. SecurityFilterChain에서 기본 접근 제어를 하고 Service에서 세부 권한을 보완해야 한다.

Q. /api/\*\* permitAll이 왜 위험해?
A. 관리자 API, 사용자 정보 API, 결제 API까지 인증 없이 접근될 수 있기 때문이다.

Q. 개발 중 임시 permitAll은 어떻게 관리해?
A. 주석이나 TODO만 믿지 말고 profile 분리, 테스트, 배포 전 보안 체크리스트로 제거 여부를 확인해야 한다.

---

# 4. Protected API Configuration

## 4.1 Protected API Matcher Rules

### [개념]

Protected API Matcher는 인증된 사용자만 접근 가능한 API 경로를 SecurityFilterChain에서 지정하는 설정이다.

내 정보 조회, 게시글 작성, 댓글 작성, 좋아요, 찜, 알림, 결제 내역, 사용자별 데이터 API는 Protected API로 분리한다.

---

### [핵심]

Protected API 후보:

- 내 정보 조회
- 내 정보 수정
- 게시글 작성
- 게시글 수정
- 댓글 작성
- 댓글 삭제
- 좋아요 / 찜
- 알림 조회
- 결제 내역 조회
- 사용자별 데이터 조회

Protected API 설정 키워드:

- authenticated
- Principal required
- SecurityContext required
- Authorization Header
- Bearer Token
- JWT Filter

---

### [실무]

Protected API 예:

```java
.authorizeHttpRequests(auth -> auth
        .requestMatchers("/api/users/me").authenticated()
        .requestMatchers(HttpMethod.POST, "/api/posts/**").authenticated()
        .requestMatchers(HttpMethod.POST, "/api/comments/**").authenticated()
        .requestMatchers("/api/notifications/**").authenticated()
        .requestMatchers("/api/payments/**").authenticated()
        .anyRequest().authenticated()
)
```

Controller 사용 예:

```java
@GetMapping("/api/users/me")
public ApiResponse<UserResponse> me(
        @AuthenticationPrincipal CustomUserPrincipal principal
) {
    return ApiResponse.success(userService.getMe(principal.userId()));
}
```

권장:

- 인증 사용자 기준 작업은 Principal에서 userId를 가져온다.
- RequestBody userId를 신뢰하지 않는다.
- Protected API는 Token 없음 / 위조 / 만료 테스트를 수행한다.
- Resource Owner Check는 Service에서 보완한다.

---

### [FAQ]

Q. Protected API는 SecurityFilterChain에서 어떻게 설정해?
A. requestMatchers에 경로를 지정하고 authenticated를 적용한다.

Q. 인증된 사용자 정보는 어디서 가져와?
A. SecurityContext 또는 @AuthenticationPrincipal을 통해 Principal에서 가져온다.

Q. Protected API에서 RequestBody userId를 믿어도 돼?
A. 안 된다. 인증 Principal의 userId를 기준으로 처리해야 한다.

---

## 4.2 Admin API Matcher Rules

### [개념]

Admin API Matcher는 관리자 권한을 가진 사용자만 접근 가능한 API 경로를 SecurityFilterChain에서 지정하는 설정이다.

Admin API는 단순 인증이 아니라 Role 또는 Authority 기반 인가 검증이 필요하다.

---

### [핵심]

Admin API 후보:

- 사용자 관리
- 게시글 강제 삭제
- 댓글 관리
- 신고 관리
- 시스템 공지 등록
- 운영 통계 조회
- 결제 관리
- 관리자 설정

Admin API 설정 키워드:

- hasRole("ADMIN")
- hasAuthority("ROLE_ADMIN")
- ROLE_ADMIN
- AccessDeniedHandler
- 403 Forbidden
- Method Security

---

### [실무]

hasRole 예:

```java
.requestMatchers("/api/admin/**").hasRole("ADMIN")
```

hasAuthority 예:

```java
.requestMatchers("/api/admin/**").hasAuthority("ROLE_ADMIN")
```

Method Security 보완 예:

```java
@PreAuthorize("hasRole('ADMIN')")
public void deleteUser(Long userId) {
}
```

주의:

- `hasRole("ADMIN")`은 일반적으로 `ROLE_ADMIN` 권한과 매칭된다.
- `hasAuthority("ROLE_ADMIN")`는 문자열을 직접 비교한다.
- Role 저장 값과 Security 설정 방식을 통일해야 한다.
- Admin API를 Frontend 메뉴 숨김에만 의존하면 안 된다.
- 권한 부족은 403 Forbidden으로 처리한다.

---

### [FAQ]

Q. 관리자 API는 authenticated만 걸면 돼?
A. 아니다. 로그인 여부뿐 아니라 ROLE_ADMIN 같은 관리자 권한을 검증해야 한다.

Q. hasRole("ADMIN")과 hasAuthority("ROLE*ADMIN")는 같아?
A. 비슷하게 동작시킬 수 있지만 hasRole은 ROLE* prefix 처리가 관여하고 hasAuthority는 문자열을 직접 비교하므로 프로젝트 규칙을 통일해야 한다.

Q. User Token으로 Admin API를 호출하면 어떤 응답이 맞아?
A. 인증은 되었지만 관리자 권한이 부족하므로 403 Forbidden이 맞다.

---

# 5. Stateless Session Policy

## 5.1 SessionCreationPolicy.STATELESS

### [개념]

`SessionCreationPolicy.STATELESS`는 Spring Security가 서버 세션을 생성하거나 사용하지 않도록 설정하는 정책이다.

JWT 기반 REST API에서는 일반적으로 Stateless Session 정책을 사용한다.

---

### [핵심]

STATELESS 핵심 키워드:

- SessionCreationPolicy.STATELESS
- Stateless API
- JWT Authentication
- No Server Session
- Access Token
- Refresh Token
- SecurityContext per request

Session 정책 예:

```java
.sessionManagement(session ->
        session.sessionCreationPolicy(SessionCreationPolicy.STATELESS)
)
```

---

### [실무]

JWT Stateless Flow:

```text
Client
→ Authorization: Bearer AccessToken
→ JWT Filter
→ Token 검증
→ Authentication 생성
→ SecurityContext 저장
→ 요청 종료 후 Context 정리
```

권장:

- JWT 기반 API에서는 STATELESS 설정을 검토한다.
- 매 요청마다 Access Token을 검증한다.
- 서버 Session에 로그인 상태를 저장하지 않는다.
- Refresh Token은 DB 또는 Redis 저장을 검토할 수 있다.
- SecurityContext는 요청 단위 인증 정보로 이해한다.

주의:

- STATELESS라고 해서 Refresh Token 저장소가 필요 없는 것은 아니다.
- 로그아웃, 강제 만료, 탈취 대응이 필요하면 서버 저장소가 필요할 수 있다.
- Session 기반 로그인과 JWT 기반 로그인을 혼용할 경우 정책을 명확히 분리해야 한다.

---

### [FAQ]

Q. STATELESS는 무슨 뜻이야?
A. 서버가 로그인 세션을 생성하거나 저장하지 않고 매 요청의 Token으로 인증 상태를 판단한다는 뜻이다.

Q. JWT를 쓰면 무조건 STATELESS야?
A. 일반적으로 REST API에서는 STATELESS를 사용하지만, OAuth2 Login이나 Session 기반 기능과 혼용하면 구조를 명확히 설계해야 한다.

Q. STATELESS면 Refresh Token도 저장하면 안 돼?
A. 아니다. Access Token 인증은 Stateless하게 처리하더라도 Refresh Token은 로그아웃과 탈취 대응을 위해 서버에 저장할 수 있다.

---

## 5.2 Stateful vs Stateless

### [개념]

Stateful 인증은 서버가 Session에 로그인 상태를 저장하는 방식이다.

Stateless 인증은 서버 Session 없이 Token을 통해 매 요청마다 인증 상태를 검증하는 방식이다.

---

### [핵심]

| 구분      | Stateful Session  | Stateless JWT                   |
| --------- | ----------------- | ------------------------------- |
| 인증 상태 | 서버 Session 저장 | Token 기반                      |
| 확장성    | Session 공유 필요 | 상대적으로 유리                 |
| 로그아웃  | 서버 Session 제거 | Refresh Token 제거 / Blacklist  |
| CSRF      | 주의 필요         | Header 기반이면 상대적으로 낮음 |
| 대표 사용 | 전통 Web MVC      | REST API / SPA                  |

---

### [실무]

Spring Boot REST API + React / Vue / Mobile 구조에서는 Stateless JWT 방식이 자주 사용된다.

Stateless JWT 구성:

```text
Login
→ Access Token 발급
→ Refresh Token 발급
→ API 요청마다 Access Token 검증
→ Access Token 만료 시 Refresh Token으로 재발급
```

Stateful Session 구성:

```text
Login
→ Server Session 생성
→ Browser Cookie로 Session ID 전달
→ 요청마다 Session 조회
→ Logout 시 Session 제거
```

선택 기준:

- SSR 기반 전통 웹: Session 고려 가능
- REST API / SPA: JWT Stateless 고려 가능
- OAuth2 Login + JWT: OAuth2 인증 후 자체 JWT 발급 가능
- 보안 요구사항이 높으면 Cookie / Header / CSRF / XSS 위협 모델 함께 검토

---

### [FAQ]

Q. Stateful과 Stateless 차이는 뭐야?
A. Stateful은 서버가 Session에 인증 상태를 저장하고, Stateless는 Token으로 매 요청마다 인증 상태를 검증한다.

Q. REST API에서는 어떤 방식이 흔해?
A. React 같은 SPA와 연동하는 REST API에서는 Stateless JWT 방식이 자주 사용된다.

Q. Stateless JWT는 로그아웃이 어려워?
A. Access Token은 즉시 무효화가 어렵기 때문에 짧은 만료 시간과 Refresh Token 무효화 전략을 함께 사용한다.

---

# 6. CSRF Configuration

## 6.1 CSRF Decision Rules

### [개념]

CSRF는 사용자가 인증된 상태를 악용해 원치 않는 요청을 보내게 하는 공격이다.

Spring Security에서 CSRF 설정은 인증 방식에 따라 활성화 또는 비활성화를 판단해야 한다.

---

### [핵심]

CSRF 판단 키워드:

- CSRF
- Cookie-based Session
- Stateless JWT
- Authorization Header
- SameSite
- HttpOnly
- Secure
- Browser Auto Credential
- csrf.disable

판단 기준:

```text
Session Cookie 기반 인증인가?
→ CSRF 보호 필요

Authorization Header 기반 Stateless JWT인가?
→ CSRF 위험 상대적으로 낮음
→ csrf disable 검토 가능
```

---

### [실무]

JWT Header 기반 API 예:

```java
.csrf(csrf -> csrf.disable())
```

주의:

- CSRF disable을 무조건 적용하지 않는다.
- Cookie 기반 인증이면 CSRF 보호를 검토한다.
- Token을 Cookie에 저장하면 CSRF와 XSS를 함께 검토해야 한다.
- SameSite, HttpOnly, Secure 속성을 함께 고려한다.
- 보안 요구사항이 높은 서비스는 위협 모델을 별도로 점검한다.

실무 판단 예:

```text
React SPA
→ Access Token Authorization Header 사용
→ Stateless API
→ csrf.disable 검토 가능
```

```text
Server-side Session Login
→ JSESSIONID Cookie 사용
→ CSRF 보호 필요
```

---

### [FAQ]

Q. JWT를 쓰면 CSRF를 꺼도 돼?
A. Authorization Header 기반 Stateless JWT 구조라면 CSRF 비활성화를 검토할 수 있다. 단, Cookie 저장 방식이면 다시 검토해야 한다.

Q. CSRF disable은 항상 안전해?
A. 아니다. 인증 방식과 Token 저장 위치에 따라 달라진다.

Q. Cookie 기반 로그인에서는 CSRF가 왜 중요해?
A. 브라우저가 Cookie를 자동 전송하므로 사용자가 의도하지 않은 요청이 인증된 상태로 처리될 수 있기 때문이다.

---

# 7. CORS Configuration

## 7.1 CORS in SecurityFilterChain

### [개념]

CORS는 브라우저가 다른 Origin으로 API 요청을 보낼 때 서버 허용 여부를 확인하는 정책이다.

Spring Security를 사용하는 경우 CORS 설정이 SecurityFilterChain과 연결되어야 브라우저 요청이 정상 처리된다.

---

### [핵심]

CORS 핵심 키워드:

- CORS
- Origin
- allowedOrigins
- allowedMethods
- allowedHeaders
- allowCredentials
- exposedHeaders
- preflight
- OPTIONS
- Authorization Header
- cors

CORS Flow:

```text
Browser
→ Preflight OPTIONS
→ Server CORS Policy 확인
→ 허용 시 실제 요청
```

---

### [실무]

SecurityFilterChain 연결 예:

```java
.cors(cors -> {})
```

CorsConfigurationSource 예:

```java
@Bean
public CorsConfigurationSource corsConfigurationSource() {
    CorsConfiguration config = new CorsConfiguration();

    config.setAllowedOrigins(List.of("http://localhost:3000"));
    config.setAllowedMethods(List.of("GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"));
    config.setAllowedHeaders(List.of("Authorization", "Content-Type"));
    config.setAllowCredentials(true);

    UrlBasedCorsConfigurationSource source =
            new UrlBasedCorsConfigurationSource();
    source.registerCorsConfiguration("/**", config);

    return source;
}
```

권장:

- 개발 Origin과 운영 Origin을 분리한다.
- Authorization Header를 허용한다.
- OPTIONS preflight를 차단하지 않는다.
- credentials 사용 시 `*` Origin을 피한다.
- CORS를 인증/인가 대체 수단으로 오해하지 않는다.

---

### [FAQ]

Q. Spring Security를 쓰면 CORS 설정도 SecurityFilterChain에 연결해야 해?
A. 맞다. SecurityFilterChain에서 cors 설정을 활성화해야 CORS 정책이 제대로 적용된다.

Q. Authorization Header 때문에 CORS 에러가 날 수 있어?
A. 가능하다. allowedHeaders에 Authorization이 허용되어 있는지 확인해야 한다.

Q. CORS는 인증이야?
A. 아니다. CORS는 브라우저 Origin 정책이며 인증/인가를 대체하지 않는다.

---

## 7.2 CORS Anti Pattern

### [개념]

CORS Anti Pattern은 개발 편의를 위해 모든 Origin, Method, Header를 무분별하게 허용하거나 CORS를 인증/인가처럼 오해하는 잘못된 설정이다.

---

### [핵심]

대표 Anti Pattern:

- 운영에서 모든 Origin 허용
- credentials 사용하면서 wildcard Origin 사용
- Authorization Header 미허용
- OPTIONS 요청 차단
- CORS를 인증 실패로 오해
- Postman 성공을 브라우저 성공으로 착각
- CORS 허용을 API 보안으로 착각

위험한 설정 예:

```java
config.setAllowedOrigins(List.of("*"));
config.setAllowedMethods(List.of("*"));
config.setAllowedHeaders(List.of("*"));
```

---

### [실무]

문제 분석 흐름:

```text
Browser Console 확인
→ Request Origin 확인
→ Preflight OPTIONS 확인
→ allowedOrigins 확인
→ allowedMethods 확인
→ allowedHeaders 확인
→ SecurityFilterChain cors 설정 확인
→ credentials 정책 확인
```

운영 권장:

```text
allowedOrigins:
- https://service.example.com

allowedMethods:
- GET
- POST
- PUT
- PATCH
- DELETE
- OPTIONS

allowedHeaders:
- Authorization
- Content-Type
```

주의:

- Postman은 CORS 정책을 적용하지 않는다.
- CORS 에러는 브라우저 정책 문제다.
- 인증 실패는 401, 권한 실패는 403, CORS 차단은 브라우저 요청 차단으로 구분한다.

---

### [FAQ]

Q. Postman은 되는데 브라우저에서 CORS 에러가 나?
A. CORS는 브라우저 보안 정책이므로 Postman에서는 발생하지 않을 수 있다.

Q. CORS를 모두 허용하면 안전해?
A. 아니다. 개발 중 임시 허용은 가능하지만 운영에서는 허용 Origin, Method, Header를 제한해야 한다.

Q. CORS 에러는 인증 실패야?
A. 아니다. 브라우저 Origin 정책 문제다. 인증 실패와 CORS 설정 문제를 구분해야 한다.

---

# 8. JWT Filter Registration

## 8.1 JWT Filter Position

### [개념]

JWT Filter는 요청 Header의 Access Token을 검증하고 Authentication을 SecurityContext에 저장하는 Custom Filter다.

SecurityFilterChain에서는 JWT Filter를 적절한 위치에 등록해야 한다.

---

### [핵심]

JWT Filter 역할:

- Authorization Header 읽기
- Bearer Token 추출
- Token 서명 검증
- Token 만료 검증
- Claims 추출
- Principal 생성
- Authentication 생성
- SecurityContext 저장
- 다음 Filter로 요청 전달

Filter 등록 키워드:

- addFilterBefore
- UsernamePasswordAuthenticationFilter
- OncePerRequestFilter
- SecurityContextHolder

---

### [실무]

일반적인 등록 예:

```java
.addFilterBefore(jwtAuthenticationFilter, UsernamePasswordAuthenticationFilter.class)
```

SecurityFilterChain 예:

```java
@Bean
public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
    return http
            .csrf(csrf -> csrf.disable())
            .cors(cors -> {})
            .sessionManagement(session ->
                    session.sessionCreationPolicy(SessionCreationPolicy.STATELESS)
            )
            .authorizeHttpRequests(auth -> auth
                    .requestMatchers("/api/auth/**").permitAll()
                    .requestMatchers("/api/admin/**").hasRole("ADMIN")
                    .anyRequest().authenticated()
            )
            .addFilterBefore(jwtAuthenticationFilter, UsernamePasswordAuthenticationFilter.class)
            .build();
}
```

권장:

- JWT Filter는 Controller 도달 전에 실행되어야 한다.
- Public API는 Token이 없어도 통과 가능해야 한다.
- 잘못된 Token은 401 처리 기준을 명확히 한다.
- 인증 성공 시 SecurityContext에 Authentication을 저장한다.
- 이미 인증 객체가 있으면 중복 처리하지 않는다.

---

### [FAQ]

Q. JWT Filter는 어디에 등록해?
A. 보통 UsernamePasswordAuthenticationFilter 이전에 addFilterBefore로 등록한다.

Q. JWT Filter는 왜 Controller 전에 실행돼야 해?
A. Controller에서 인증 사용자 정보를 사용하려면 요청 전에 Token 검증과 SecurityContext 저장이 끝나야 하기 때문이다.

Q. Public API도 JWT Filter를 통과해?
A. Filter Chain에 포함될 수 있다. 다만 Token이 없는 Public API는 실패 처리하지 않고 다음 Filter로 넘겨야 한다.

---

## 8.2 JWT Filter Registration Mistakes

### [개념]

JWT Filter 등록 오류는 인증이 정상적으로 수행되지 않거나 모든 Protected API가 401로 실패하는 원인이 된다.

---

### [핵심]

자주 발생하는 문제:

- JWT Filter 미등록
- Filter 위치 오류
- Bearer Token 파싱 실패
- Public API에서 Token 없음으로 401 처리
- SecurityContext 저장 누락
- Authentication 생성 실패
- ExceptionHandling과 연결 누락
- 동일 Filter 중복 등록

---

### [실무]

Debug Flow:

```text
요청 Header 확인
→ JWT Filter 실행 여부 확인
→ Bearer Token 추출 확인
→ Token 검증 확인
→ Authentication 생성 확인
→ SecurityContext 저장 확인
→ 다음 Filter 진행 확인
→ Controller 인증 정보 확인
```

잘못된 흐름:

```text
Public Login Request
→ JWT Filter
→ Token 없음
→ 401 반환
→ Login API 접근 실패
```

수정 방향:

```text
Token 없음
→ Public API 또는 인증이 필요 없는 요청이면 다음 Filter 진행
→ Protected API는 SecurityFilterChain에서 인증 실패 처리
```

권장:

- JWT Filter 로그는 최소한으로 남긴다.
- Token 원문을 로그에 남기지 않는다.
- Token 오류 원인은 서버 로그와 사용자 응답을 분리한다.
- 테스트에서 Token 없음 / 위조 / 만료 / 정상 케이스를 검증한다.

---

### [FAQ]

Q. JWT Filter를 등록했는데 로그인 API가 401이 나와?
A. Public API에서 Token 없음 자체를 실패로 처리하고 있을 수 있다. Token이 없으면 다음 Filter로 넘기는 구조를 검토해야 한다.

Q. Token은 보냈는데 Controller에서 Principal이 null이야?
A. JWT Filter가 실행되지 않았거나 Authentication을 SecurityContext에 저장하지 않았을 수 있다.

Q. JWT Filter에서 Token 원문을 로그로 찍어도 돼?
A. 안 된다. Token은 민감정보이므로 로그에 남기지 않아야 한다.

---

# 9. Exception Handling Configuration

## 9.1 AuthenticationEntryPoint Registration

### [개념]

AuthenticationEntryPoint는 인증되지 않은 사용자가 Protected API에 접근하거나 Token이 유효하지 않을 때 401 Unauthorized 응답을 처리하는 진입점이다.

---

### [핵심]

AuthenticationEntryPoint 처리 상황:

- Token 없음
- Token 만료
- Token 위조
- Token 형식 오류
- 인증 객체 없음
- Anonymous 접근 차단

설정 키워드:

- exceptionHandling
- authenticationEntryPoint
- 401 Unauthorized
- UNAUTHORIZED
- TOKEN_EXPIRED

---

### [실무]

SecurityFilterChain 등록 예:

```java
.exceptionHandling(exception -> exception
        .authenticationEntryPoint(customAuthenticationEntryPoint)
)
```

권장 응답:

```text
HTTP 401 Unauthorized
errorCode: UNAUTHORIZED
message: 인증이 필요합니다.
```

주의:

- Filter Chain에서 발생한 인증 예외는 ControllerAdvice까지 가지 않을 수 있다.
- Security 예외 응답 형식을 API 공통 응답과 맞추는 것이 좋다.
- Token 상세 오류를 사용자에게 과도하게 노출하지 않는다.
- Frontend가 재발급 또는 재로그인을 판단할 수 있도록 errorCode를 설계한다.

---

### [FAQ]

Q. AuthenticationEntryPoint는 언제 실행돼?
A. 인증 정보가 없거나 유효하지 않아 Protected API 접근이 거부될 때 실행된다.

Q. Security 예외도 GlobalExceptionHandler에서 처리돼?
A. 항상 그렇지 않다. Filter Chain에서 발생한 인증 예외는 AuthenticationEntryPoint에서 처리되는 경우가 많다.

Q. JWT 만료는 EntryPoint에서 처리해?
A. 일반적으로 인증 실패로 보고 401 응답을 EntryPoint에서 처리한다.

---

## 9.2 AccessDeniedHandler Registration

### [개념]

AccessDeniedHandler는 인증은 되었지만 권한이 부족한 사용자의 접근을 403 Forbidden으로 처리하는 Handler다.

---

### [핵심]

AccessDeniedHandler 처리 상황:

- Role 부족
- Authority 부족
- 관리자 API 접근 실패
- Method Security 실패
- Resource Owner Check 실패
- 인증은 되었지만 권한 없음

설정 키워드:

- exceptionHandling
- accessDeniedHandler
- 403 Forbidden
- ACCESS_DENIED

---

### [실무]

SecurityFilterChain 등록 예:

```java
.exceptionHandling(exception -> exception
        .authenticationEntryPoint(customAuthenticationEntryPoint)
        .accessDeniedHandler(customAccessDeniedHandler)
)
```

권장 응답:

```text
HTTP 403 Forbidden
errorCode: ACCESS_DENIED
message: 접근 권한이 없습니다.
```

주의:

- 인증 실패와 권한 실패를 구분한다.
- 관리자 권한 실패는 403으로 처리한다.
- Resource 존재 여부를 과도하게 노출하지 않는다.
- Frontend는 403 시 권한 없음 안내를 처리한다.

---

### [FAQ]

Q. AccessDeniedHandler는 언제 실행돼?
A. 인증은 되었지만 Role, Authority, Resource Owner 조건을 만족하지 못할 때 실행된다.

Q. User Token으로 Admin API를 호출하면 EntryPoint가 실행돼?
A. 아니다. 인증은 되었으므로 일반적으로 AccessDeniedHandler가 실행되고 403이 반환된다.

Q. 403 응답 메시지는 상세해야 해?
A. 과도하게 상세할 필요는 없다. 접근 권한이 없다는 정도로 통일하는 것이 좋다.

---

# 10. Full SecurityFilterChain Template

## 10.1 JWT REST API Template

### [개념]

JWT REST API Template은 Spring Boot REST API에서 Stateless JWT 인증을 사용하는 기본 SecurityFilterChain 구성 예시다.

---

### [핵심]

Template 구성 요소:

- csrf disable
- cors enable
- stateless session
- public endpoint permitAll
- admin endpoint hasRole
- protected endpoint authenticated
- exceptionHandling
- jwtAuthenticationFilter
- addFilterBefore

---

### [실무]

기본 Template:

```java
@Bean
public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
    return http
            .csrf(csrf -> csrf.disable())
            .cors(cors -> {})
            .sessionManagement(session ->
                    session.sessionCreationPolicy(SessionCreationPolicy.STATELESS)
            )
            .exceptionHandling(exception -> exception
                    .authenticationEntryPoint(customAuthenticationEntryPoint)
                    .accessDeniedHandler(customAccessDeniedHandler)
            )
            .authorizeHttpRequests(auth -> auth
                    .requestMatchers("/api/auth/signup").permitAll()
                    .requestMatchers("/api/auth/login").permitAll()
                    .requestMatchers("/api/auth/reissue").permitAll()
                    .requestMatchers(HttpMethod.GET, "/api/posts/**").permitAll()
                    .requestMatchers(HttpMethod.GET, "/api/festivals/**").permitAll()
                    .requestMatchers("/api/admin/**").hasRole("ADMIN")
                    .requestMatchers("/api/users/me").authenticated()
                    .requestMatchers("/api/notifications/**").authenticated()
                    .requestMatchers("/api/payments/**").authenticated()
                    .anyRequest().authenticated()
            )
            .addFilterBefore(jwtAuthenticationFilter, UsernamePasswordAuthenticationFilter.class)
            .build();
}
```

주의:

- 프로젝트 API 경로에 맞게 matcher를 수정한다.
- Swagger 경로는 개발 profile에서만 허용하는 것이 좋다.
- `hasRole` / `hasAuthority` 규칙을 권한 저장 방식과 맞춘다.
- Refresh Token 검증은 재발급 로직에서 별도 처리한다.
- 실제 운영에서는 CORS Origin을 명시적으로 제한한다.

---

### [FAQ]

Q. 이 Template을 그대로 쓰면 돼?
A. 기본 구조로 참고할 수 있지만 프로젝트 API 경로, 권한 규칙, CORS Origin, 예외 응답 형식에 맞게 수정해야 한다.

Q. anyRequest().authenticated()는 왜 마지막에 둬?
A. 명시되지 않은 나머지 API를 기본적으로 보호하기 위해 마지막에 둔다.

Q. JWT Filter는 Template에서 필수야?
A. JWT 기반 인증을 사용한다면 Access Token 검증과 SecurityContext 저장을 위해 필요하다.

---

## 10.2 Configuration Review Checklist

### [개념]

SecurityFilterChain Review Checklist는 SecurityConfig 설정이 인증, 인가, JWT, CORS, CSRF, 예외 처리 기준에 맞는지 검수하기 위한 목록이다.

---

### [핵심]

Checklist:

```md
- [ ] SecurityFilterChain Bean 기반 설정인가?
- [ ] WebSecurityConfigurerAdapter를 사용하지 않는가?
- [ ] Public API가 명확히 분리되었는가?
- [ ] Protected API가 authenticated로 보호되는가?
- [ ] Admin API에 hasRole 또는 hasAuthority가 적용되었는가?
- [ ] requestMatchers 순서가 적절한가?
- [ ] 넓은 permitAll 규칙이 없는가?
- [ ] anyRequest().authenticated()가 마지막에 있는가?
- [ ] SessionCreationPolicy.STATELESS가 필요한 구조인가?
- [ ] CSRF disable 판단 근거가 있는가?
- [ ] CORS 설정이 SecurityFilterChain과 연결되었는가?
- [ ] Authorization Header가 CORS allowedHeaders에 포함되었는가?
- [ ] JWT Filter가 등록되었는가?
- [ ] JWT Filter 위치가 적절한가?
- [ ] AuthenticationEntryPoint가 등록되었는가?
- [ ] AccessDeniedHandler가 등록되었는가?
- [ ] 401 / 403 응답이 분리되는가?
- [ ] Swagger 허용이 운영에 노출되지 않는가?
- [ ] Token 원문 로그 출력이 없는가?
```

---

### [실무]

Review Flow:

```text
SecurityConfig 확인
→ requestMatchers 추출
→ Public API 검수
→ Protected API 검수
→ Admin API 검수
→ Session / CSRF / CORS 검수
→ JWT Filter 등록 확인
→ Exception Handler 확인
→ 401 / 403 테스트
→ 운영 노출 위험 확인
```

테스트 케이스:

```text
No Token to Protected API
→ 401

Invalid Token to Protected API
→ 401

Valid User Token to User API
→ 200

Valid User Token to Admin API
→ 403

Valid Admin Token to Admin API
→ 200

Public API without Token
→ 200
```

---

### [FAQ]

Q. SecurityFilterChain 검수에서 가장 먼저 볼 것은 뭐야?
A. Public / Protected / Admin API 분리와 requestMatchers 순서를 먼저 확인하는 것이 좋다.

Q. SecurityConfig에서 가장 위험한 실수는 뭐야?
A. `/api/**.permitAll()` 또는 `anyRequest().permitAll()`처럼 모든 API를 열어두는 실수다.

Q. SecurityFilterChain 테스트는 어떻게 해?
A. Token 없음, 위조 Token, 일반 User Token, Admin Token으로 Public / Protected / Admin API 응답을 검증한다.

---

# Retrieval Queries

### [FAQ]

Q. SecurityFilterChain은 뭐야?
A. 요청이 Controller에 도달하기 전에 인증, 인가, CORS, CSRF, 예외 처리를 수행하는 Spring Security Filter 체인이다.

Q. Spring Security 6에서도 WebSecurityConfigurerAdapter를 써야 해?
A. 아니다. 신규 Spring Security 6 기준에서는 SecurityFilterChain Bean 기반 설정을 우선 사용한다.

Q. SecurityFilterChain에서 가장 중요한 설정은 뭐야?
A. Public / Protected API 분리, JWT Filter 등록, Stateless Session, 401/403 Handler, requestMatchers 순서가 중요하다.

Q. requestMatchers는 뭐야?
A. 특정 요청 경로와 Method에 대해 인증 또는 권한 규칙을 적용하는 설정이다.

Q. GET 조회는 공개이고 POST 작성은 로그인 필요하게 할 수 있어?
A. 가능하다. HTTP Method 기준 requestMatchers를 사용해 GET은 permitAll, POST는 authenticated로 분리할 수 있다.

Q. anyRequest는 어디에 둬야 해?
A. 일반적으로 가장 마지막에 두어 앞에서 처리되지 않은 모든 요청에 기본 정책을 적용한다.

Q. requestMatchers 순서가 중요해?
A. 중요하다. 더 구체적인 경로를 먼저 선언하고 전체 규칙은 뒤에 두는 것이 좋다.

Q. /api/\*\*를 permitAll로 열어도 돼?
A. 권장하지 않는다. 관리자 API나 보호 API까지 열릴 수 있으므로 필요한 Public API만 명시적으로 허용해야 한다.

Q. anyRequest().permitAll()을 쓰면 안 돼?
A. 개발 중 임시 사용은 가능하지만 운영 코드에 남기면 대부분의 API가 보호되지 않는 심각한 보안 문제가 된다.

Q. Public API는 SecurityFilterChain에서 어떻게 설정해?
A. requestMatchers에 Public API 경로를 지정하고 permitAll을 적용한다.

Q. 로그인 API는 permitAll이 맞아?
A. 맞다. 로그인은 인증 전 접근해야 하므로 permitAll 대상이다.

Q. 토큰 재발급 API도 permitAll이야?
A. 경로 접근은 permitAll일 수 있지만 Refresh Token 검증은 Service 또는 Filter에서 반드시 수행해야 한다.

Q. Swagger도 permitAll로 열어도 돼?
A. 개발 환경에서는 가능하지만 운영 환경에서는 profile 분리나 접근 제한을 검토해야 한다.

Q. 모든 API를 permitAll로 열고 Service에서 검사하면 돼?
A. 권장하지 않는다. SecurityFilterChain에서 기본 접근 제어를 하고 Service에서 세부 권한을 보완해야 한다.

Q. /api/\*\* permitAll이 왜 위험해?
A. 관리자 API, 사용자 정보 API, 결제 API까지 인증 없이 접근될 수 있기 때문이다.

Q. 개발 중 임시 permitAll은 어떻게 관리해?
A. 주석이나 TODO만 믿지 말고 profile 분리, 테스트, 배포 전 보안 체크리스트로 제거 여부를 확인해야 한다.

Q. Protected API는 SecurityFilterChain에서 어떻게 설정해?
A. requestMatchers에 경로를 지정하고 authenticated를 적용한다.

Q. 인증된 사용자 정보는 어디서 가져와?
A. SecurityContext 또는 @AuthenticationPrincipal을 통해 Principal에서 가져온다.

Q. Protected API에서 RequestBody userId를 믿어도 돼?
A. 안 된다. 인증 Principal의 userId를 기준으로 처리해야 한다.

Q. 관리자 API는 authenticated만 걸면 돼?
A. 아니다. 로그인 여부뿐 아니라 ROLE_ADMIN 같은 관리자 권한을 검증해야 한다.

Q. hasRole("ADMIN")과 hasAuthority("ROLE*ADMIN")는 같아?
A. 비슷하게 동작시킬 수 있지만 hasRole은 ROLE* prefix 처리가 관여하고 hasAuthority는 문자열을 직접 비교하므로 프로젝트 규칙을 통일해야 한다.

Q. User Token으로 Admin API를 호출하면 어떤 응답이 맞아?
A. 인증은 되었지만 관리자 권한이 부족하므로 403 Forbidden이 맞다.

Q. STATELESS는 무슨 뜻이야?
A. 서버가 로그인 세션을 생성하거나 저장하지 않고 매 요청의 Token으로 인증 상태를 판단한다는 뜻이다.

Q. JWT를 쓰면 무조건 STATELESS야?
A. 일반적으로 REST API에서는 STATELESS를 사용하지만, OAuth2 Login이나 Session 기반 기능과 혼용하면 구조를 명확히 설계해야 한다.

Q. STATELESS면 Refresh Token도 저장하면 안 돼?
A. 아니다. Access Token 인증은 Stateless하게 처리하더라도 Refresh Token은 로그아웃과 탈취 대응을 위해 서버에 저장할 수 있다.

Q. Stateful과 Stateless 차이는 뭐야?
A. Stateful은 서버가 Session에 인증 상태를 저장하고, Stateless는 Token으로 매 요청마다 인증 상태를 검증한다.

Q. REST API에서는 어떤 방식이 흔해?
A. React 같은 SPA와 연동하는 REST API에서는 Stateless JWT 방식이 자주 사용된다.

Q. Stateless JWT는 로그아웃이 어려워?
A. Access Token은 즉시 무효화가 어렵기 때문에 짧은 만료 시간과 Refresh Token 무효화 전략을 함께 사용한다.

Q. JWT를 쓰면 CSRF를 꺼도 돼?
A. Authorization Header 기반 Stateless JWT 구조라면 CSRF 비활성화를 검토할 수 있다. 단, Cookie 저장 방식이면 다시 검토해야 한다.

Q. CSRF disable은 항상 안전해?
A. 아니다. 인증 방식과 Token 저장 위치에 따라 달라진다.

Q. Cookie 기반 로그인에서는 CSRF가 왜 중요해?
A. 브라우저가 Cookie를 자동 전송하므로 사용자가 의도하지 않은 요청이 인증된 상태로 처리될 수 있기 때문이다.

Q. Spring Security를 쓰면 CORS 설정도 SecurityFilterChain에 연결해야 해?
A. 맞다. SecurityFilterChain에서 cors 설정을 활성화해야 CORS 정책이 제대로 적용된다.

Q. Authorization Header 때문에 CORS 에러가 날 수 있어?
A. 가능하다. allowedHeaders에 Authorization이 허용되어 있는지 확인해야 한다.

Q. CORS는 인증이야?
A. 아니다. CORS는 브라우저 Origin 정책이며 인증/인가를 대체하지 않는다.

Q. Postman은 되는데 브라우저에서 CORS 에러가 나?
A. CORS는 브라우저 보안 정책이므로 Postman에서는 발생하지 않을 수 있다.

Q. CORS를 모두 허용하면 안전해?
A. 아니다. 개발 중 임시 허용은 가능하지만 운영에서는 허용 Origin, Method, Header를 제한해야 한다.

Q. CORS 에러는 인증 실패야?
A. 아니다. 브라우저 Origin 정책 문제다. 인증 실패와 CORS 설정 문제를 구분해야 한다.

Q. JWT Filter는 어디에 등록해?
A. 보통 UsernamePasswordAuthenticationFilter 이전에 addFilterBefore로 등록한다.

Q. JWT Filter는 왜 Controller 전에 실행돼야 해?
A. Controller에서 인증 사용자 정보를 사용하려면 요청 전에 Token 검증과 SecurityContext 저장이 끝나야 하기 때문이다.

Q. Public API도 JWT Filter를 통과해?
A. Filter Chain에 포함될 수 있다. 다만 Token이 없는 Public API는 실패 처리하지 않고 다음 Filter로 넘겨야 한다.

Q. JWT Filter를 등록했는데 로그인 API가 401이 나와?
A. Public API에서 Token 없음 자체를 실패로 처리하고 있을 수 있다. Token이 없으면 다음 Filter로 넘기는 구조를 검토해야 한다.

Q. Token은 보냈는데 Controller에서 Principal이 null이야?
A. JWT Filter가 실행되지 않았거나 Authentication을 SecurityContext에 저장하지 않았을 수 있다.

Q. JWT Filter에서 Token 원문을 로그로 찍어도 돼?
A. 안 된다. Token은 민감정보이므로 로그에 남기지 않아야 한다.

Q. AuthenticationEntryPoint는 언제 실행돼?
A. 인증 정보가 없거나 유효하지 않아 Protected API 접근이 거부될 때 실행된다.

Q. Security 예외도 GlobalExceptionHandler에서 처리돼?
A. 항상 그렇지 않다. Filter Chain에서 발생한 인증 예외는 AuthenticationEntryPoint에서 처리되는 경우가 많다.

Q. JWT 만료는 EntryPoint에서 처리해?
A. 일반적으로 인증 실패로 보고 401 응답을 EntryPoint에서 처리한다.

Q. AccessDeniedHandler는 언제 실행돼?
A. 인증은 되었지만 Role, Authority, Resource Owner 조건을 만족하지 못할 때 실행된다.

Q. User Token으로 Admin API를 호출하면 EntryPoint가 실행돼?
A. 아니다. 인증은 되었으므로 일반적으로 AccessDeniedHandler가 실행되고 403이 반환된다.

Q. 403 응답 메시지는 상세해야 해?
A. 과도하게 상세할 필요는 없다. 접근 권한이 없다는 정도로 통일하는 것이 좋다.

Q. SecurityFilterChain Template을 그대로 쓰면 돼?
A. 기본 구조로 참고할 수 있지만 프로젝트 API 경로, 권한 규칙, CORS Origin, 예외 응답 형식에 맞게 수정해야 한다.

Q. anyRequest().authenticated()는 왜 마지막에 둬?
A. 명시되지 않은 나머지 API를 기본적으로 보호하기 위해 마지막에 둔다.

Q. JWT Filter는 Template에서 필수야?
A. JWT 기반 인증을 사용한다면 Access Token 검증과 SecurityContext 저장을 위해 필요하다.

Q. SecurityFilterChain 검수에서 가장 먼저 볼 것은 뭐야?
A. Public / Protected / Admin API 분리와 requestMatchers 순서를 먼저 확인하는 것이 좋다.

Q. SecurityConfig에서 가장 위험한 실수는 뭐야?
A. `/api/**.permitAll()` 또는 `anyRequest().permitAll()`처럼 모든 API를 열어두는 실수다.

Q. SecurityFilterChain 테스트는 어떻게 해?
A. Token 없음, 위조 Token, 일반 User Token, Admin Token으로 Public / Protected / Admin API 응답을 검증한다.
