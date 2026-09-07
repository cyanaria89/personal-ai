# Security Advanced Part06 - Exception Handling, CORS, CSRF

---

# 1. Security Exception Handling Overview

## 1.1 Security Exception Handling Concept

### [개념]

Security Exception Handling은 Spring Security 인증 / 인가 실패를 API 응답 형식에 맞게 처리하는 보안 예외 처리 기준이다.

Spring Security Filter Chain에서 발생한 인증 / 인가 예외는 일반적인 `GlobalExceptionHandler` 또는 `@ControllerAdvice`까지 도달하지 않을 수 있다.

따라서 인증 실패는 `AuthenticationEntryPoint`, 인가 실패는 `AccessDeniedHandler`에서 처리하는 구조를 명확히 해야 한다.

---

### [핵심]

Security Exception Handling 핵심 키워드:

- Security Exception Handling
- AuthenticationEntryPoint
- AccessDeniedHandler
- AuthenticationException
- AccessDeniedException
- 401 Unauthorized
- 403 Forbidden
- Filter Chain
- GlobalExceptionHandler
- ApiResponse
- Error Response

Security 예외 구분:

```text
Authentication Failure
→ AuthenticationEntryPoint
→ 401 Unauthorized
```

```text
Authorization Failure
→ AccessDeniedHandler
→ 403 Forbidden
```

---

### [실무]

2026 실무 기준 Spring Security 예외 응답은 API 전체 Error Response 형식과 일관되게 맞추는 것이 좋다.

Security 예외 처리 흐름:

```text
Request
→ SecurityFilterChain
→ Authentication 실패
→ AuthenticationEntryPoint
→ 401 JSON Response
```

```text
Request
→ SecurityFilterChain
→ Authentication 성공
→ Authorization 실패
→ AccessDeniedHandler
→ 403 JSON Response
```

권장:

- 인증 실패와 인가 실패를 분리한다.
- 401과 403을 명확히 구분한다.
- Security 예외 응답도 API 공통 응답 형식과 맞춘다.
- Stack trace를 응답하지 않는다.
- Token 원문, Secret, 내부 예외 메시지를 응답하지 않는다.
- Frontend가 처리 가능한 `errorCode`를 제공한다.

---

### [FAQ]

Q. Security 예외도 GlobalExceptionHandler에서 처리돼?
A. 항상 그렇지 않다. Filter Chain에서 발생한 인증 / 인가 예외는 AuthenticationEntryPoint 또는 AccessDeniedHandler에서 처리되는 경우가 많다.

Q. Security Exception Handling에서 가장 중요한 것은 뭐야?
A. 인증 실패 401과 인가 실패 403을 분리하고 API 공통 에러 응답 형식과 맞추는 것이다.

Q. Security 에러 응답도 ApiResponse 형식으로 맞춰야 해?
A. 프로젝트 응답 규칙이 있다면 맞추는 것이 Frontend 처리에 좋다.

---

# 2. AuthenticationEntryPoint Rules

## 2.1 AuthenticationEntryPoint Concept

### [개념]

`AuthenticationEntryPoint`는 인증되지 않은 사용자가 Protected API에 접근하거나 인증 정보가 유효하지 않을 때 401 Unauthorized 응답을 처리하는 진입점이다.

JWT 기반 API에서는 Token 없음, Token 만료, Token 위조, Token 형식 오류 같은 인증 실패를 처리한다.

---

### [핵심]

AuthenticationEntryPoint 처리 상황:

- Access Token 없음
- Authorization Header 없음
- Bearer prefix 누락
- Access Token 만료
- JWT 서명 오류
- JWT 형식 오류
- JWT tokenType 오류
- Authentication 객체 없음
- Anonymous 접근 차단

응답 기준:

```text
HTTP 401 Unauthorized
errorCode: UNAUTHORIZED
message: 인증이 필요합니다.
```

---

### [실무]

SecurityFilterChain 등록 예:

```java
.exceptionHandling(exception -> exception
        .authenticationEntryPoint(customAuthenticationEntryPoint)
)
```

Custom EntryPoint 예:

```java
@Component
public class CustomAuthenticationEntryPoint implements AuthenticationEntryPoint {

    @Override
    public void commence(
            HttpServletRequest request,
            HttpServletResponse response,
            AuthenticationException authException
    ) throws IOException {
        response.setStatus(HttpServletResponse.SC_UNAUTHORIZED);
        response.setContentType(MediaType.APPLICATION_JSON_VALUE);
        response.setCharacterEncoding(StandardCharsets.UTF_8.name());

        response.getWriter().write("""
                {
                  "status": 401,
                  "errorCode": "UNAUTHORIZED",
                  "message": "인증이 필요합니다."
                }
                """);
    }
}
```

권장:

- 인증 실패는 401로 응답한다.
- Access Token 만료는 `TOKEN_EXPIRED`로 구분 가능하다.
- 위조 Token 상세 원인을 사용자 응답에 과도하게 노출하지 않는다.
- Frontend가 재발급 또는 재로그인 판단을 할 수 있도록 errorCode를 설계한다.
- EntryPoint 응답 형식은 GlobalExceptionHandler 응답과 맞춘다.

---

### [FAQ]

Q. AuthenticationEntryPoint는 언제 실행돼?
A. 인증 정보가 없거나 유효하지 않아 Protected API 접근이 거부될 때 실행된다.

Q. JWT 만료는 EntryPoint에서 처리해?
A. 일반적으로 인증 실패로 보고 401 응답을 EntryPoint에서 처리한다.

Q. Token 없음과 Token 위조를 모두 같은 메시지로 처리해도 돼?
A. 가능하다. 보안상 상세 원인을 과도하게 노출하지 않는 것이 좋다.

---

## 2.2 Authentication Failure Response Rules

### [개념]

Authentication Failure Response는 인증 실패 상황에서 Client가 재발급, 재로그인, Token 제거를 판단할 수 있도록 제공하는 401 응답이다.

---

### [핵심]

401 Error Code 후보:

- UNAUTHORIZED
- ACCESS_TOKEN_REQUIRED
- TOKEN_EXPIRED
- TOKEN_INVALID
- INVALID_LOGIN
- REFRESH_TOKEN_INVALID
- REFRESH_TOKEN_EXPIRED

응답 필드 후보:

- status
- errorCode
- message
- timestamp
- path

---

### [실무]

Access Token 없음 응답:

```json
{
  "status": 401,
  "errorCode": "ACCESS_TOKEN_REQUIRED",
  "message": "인증이 필요합니다."
}
```

Access Token 만료 응답:

```json
{
  "status": 401,
  "errorCode": "TOKEN_EXPIRED",
  "message": "인증이 만료되었습니다."
}
```

위조 Token 응답:

```json
{
  "status": 401,
  "errorCode": "TOKEN_INVALID",
  "message": "인증 정보가 유효하지 않습니다."
}
```

권장:

- Access Token 만료와 위조 Token을 errorCode로 구분할 수 있다.
- Refresh Token 실패는 재로그인으로 연결한다.
- 응답 message는 짧고 명확하게 작성한다.
- 내부 예외 class 이름을 노출하지 않는다.
- Secret Key, Token 원문, Stack trace를 응답하지 않는다.

---

### [FAQ]

Q. 401 errorCode를 세분화해야 해?
A. Frontend 재발급 흐름이 필요하면 TOKEN_EXPIRED 같은 errorCode를 분리하는 것이 좋다.

Q. JWT 위조 상세 사유를 응답해도 돼?
A. 권장하지 않는다. 서명 오류, 파싱 오류 같은 상세 원인은 서버 로그에서만 관리하는 것이 좋다.

Q. Access Token 만료와 Refresh Token 만료는 같은 응답이어도 돼?
A. 처리 흐름이 다르므로 구분하는 것이 좋다. Access Token 만료는 재발급 시도, Refresh Token 만료는 재로그인이 필요하다.

---

# 3. AccessDeniedHandler Rules

## 3.1 AccessDeniedHandler Concept

### [개념]

`AccessDeniedHandler`는 인증은 되었지만 권한이 부족한 사용자의 접근을 403 Forbidden으로 처리하는 Handler다.

Role 부족, Authority 부족, Resource Owner Check 실패, Method Security 실패 같은 인가 실패를 처리한다.

---

### [핵심]

AccessDeniedHandler 처리 상황:

- Role 부족
- Authority 부족
- ROLE\_ prefix 불일치
- Admin API 접근 실패
- Resource Owner Check 실패
- Method Security 실패
- 본인 리소스 아님
- 비즈니스 권한 부족

응답 기준:

```text
HTTP 403 Forbidden
errorCode: ACCESS_DENIED
message: 접근 권한이 없습니다.
```

---

### [실무]

SecurityFilterChain 등록 예:

```java
.exceptionHandling(exception -> exception
        .authenticationEntryPoint(customAuthenticationEntryPoint)
        .accessDeniedHandler(customAccessDeniedHandler)
)
```

Custom AccessDeniedHandler 예:

```java
@Component
public class CustomAccessDeniedHandler implements AccessDeniedHandler {

    @Override
    public void handle(
            HttpServletRequest request,
            HttpServletResponse response,
            AccessDeniedException accessDeniedException
    ) throws IOException {
        response.setStatus(HttpServletResponse.SC_FORBIDDEN);
        response.setContentType(MediaType.APPLICATION_JSON_VALUE);
        response.setCharacterEncoding(StandardCharsets.UTF_8.name());

        response.getWriter().write("""
                {
                  "status": 403,
                  "errorCode": "ACCESS_DENIED",
                  "message": "접근 권한이 없습니다."
                }
                """);
    }
}
```

권장:

- 인가 실패는 403으로 응답한다.
- 인증 실패와 권한 실패를 혼동하지 않는다.
- 관리자 권한 실패는 403으로 처리한다.
- Resource Owner Check 실패는 403으로 처리한다.
- 리소스 존재 여부를 과도하게 노출하지 않는다.
- Frontend는 403을 재로그인 흐름으로만 처리하지 않는다.

---

### [FAQ]

Q. AccessDeniedHandler는 언제 실행돼?
A. 인증은 되었지만 Role, Authority, Resource Owner 조건을 만족하지 못할 때 실행된다.

Q. User Token으로 Admin API를 호출하면 EntryPoint가 실행돼?
A. 아니다. 인증은 되었으므로 일반적으로 AccessDeniedHandler가 실행되고 403이 반환된다.

Q. Resource Owner Check 실패는 401이야 403이야?
A. 인증된 사용자가 권한이 없는 상태이므로 일반적으로 403 Forbidden이다.

---

## 3.2 Authorization Failure Response Rules

### [개념]

Authorization Failure Response는 인증된 사용자의 권한 부족을 Client에 전달하는 403 응답이다.

403 응답은 재로그인보다 권한 없음 안내, 접근 차단, 관리자 권한 필요 안내와 연결된다.

---

### [핵심]

403 Error Code 후보:

- ACCESS_DENIED
- ROLE_REQUIRED
- ADMIN_REQUIRED
- RESOURCE_ACCESS_DENIED
- OWNER_REQUIRED
- FORBIDDEN

응답 필드 후보:

- status
- errorCode
- message
- timestamp
- path

---

### [실무]

일반 권한 부족 응답:

```json
{
  "status": 403,
  "errorCode": "ACCESS_DENIED",
  "message": "접근 권한이 없습니다."
}
```

관리자 권한 부족 응답:

```json
{
  "status": 403,
  "errorCode": "ADMIN_REQUIRED",
  "message": "관리자 권한이 필요합니다."
}
```

리소스 소유자 실패 응답:

```json
{
  "status": 403,
  "errorCode": "RESOURCE_ACCESS_DENIED",
  "message": "해당 리소스에 접근할 권한이 없습니다."
}
```

주의:

- 내부 권한 구조를 상세히 노출하지 않는다.
- 어떤 Role이 필요한지 과도하게 노출하지 않는다.
- 리소스 존재 여부를 숨길 필요가 있으면 404 전략을 검토한다.
- 401과 403 errorCode를 분리한다.
- Frontend는 403을 Token 재발급 대상으로 보지 않는다.

---

### [FAQ]

Q. 403 응답은 언제 사용해?
A. 인증은 되었지만 해당 기능이나 리소스에 접근할 권한이 없을 때 사용한다.

Q. 403이 오면 Frontend는 재로그인하면 돼?
A. 아니다. 403은 권한 부족이므로 권한 없음 안내나 접근 차단 처리가 맞다.

Q. 403 대신 404를 써도 돼?
A. 리소스 존재 여부를 숨겨야 하는 보안 정책이 있다면 404 전략을 검토할 수 있다.

---

# 4. 401 vs 403 Handling

## 4.1 401 and 403 Comparison

### [개념]

401 Unauthorized는 인증 실패이고 403 Forbidden은 인가 실패다.

Spring Security 예외 처리에서 401과 403은 원인, Handler, Frontend 처리 방식이 다르므로 반드시 분리해야 한다.

---

### [핵심]

| 구분          | 401 Unauthorized         | 403 Forbidden          |
| ------------- | ------------------------ | ---------------------- |
| 의미          | 인증 실패                | 권한 부족              |
| 사용자 상태   | 누구인지 확인 불가       | 로그인은 됨            |
| 대표 원인     | Token 없음 / 만료 / 위조 | Role 부족 / Owner 아님 |
| Handler       | AuthenticationEntryPoint | AccessDeniedHandler    |
| Frontend 처리 | 재발급 / 재로그인        | 권한 없음 안내         |
| 예외          | AuthenticationException  | AccessDeniedException  |

---

### [실무]

401 Debug Flow:

```text
401 발생
→ Authorization Header 확인
→ Bearer prefix 확인
→ Token 서명 확인
→ Token 만료 확인
→ JWT Filter 실행 확인
→ SecurityContext 저장 확인
→ AuthenticationEntryPoint 확인
```

403 Debug Flow:

```text
403 발생
→ Authentication 존재 확인
→ Principal 확인
→ Role / Authority 확인
→ hasRole / hasAuthority 확인
→ Resource Owner Check 확인
→ Method Security 확인
→ AccessDeniedHandler 확인
```

권장:

- Token 없음은 401이다.
- Token 위조는 401이다.
- Token 만료는 401이다.
- User Token으로 Admin API 접근은 403이다.
- 본인 리소스가 아닌 경우는 403이다.
- Role prefix 불일치로 권한 부족이면 403이다.

---

### [FAQ]

Q. 401과 403 차이는?
A. 401은 인증 실패이고 403은 인증은 되었지만 권한이 부족한 상태다.

Q. Token이 없으면 401이야 403이야?
A. 사용자를 확인할 수 없으므로 401이다.

Q. User Token으로 Admin API를 호출하면 401이야 403이야?
A. 사용자는 인증되었지만 관리자 권한이 부족하므로 403이다.

---

## 4.2 Common Misclassification Rules

### [개념]

Common Misclassification은 인증 실패와 인가 실패를 잘못 분류해 401 / 403 응답을 반대로 처리하는 문제다.

이 문제는 Frontend 재발급 로직, 권한 안내, 사용자 경험, 보안 분석을 모두 혼란스럽게 만든다.

---

### [핵심]

잘못된 분류 예:

- Token 없음인데 403
- Token 만료인데 403
- User Token으로 Admin API 접근인데 401
- Resource Owner Check 실패인데 401
- 로그인 실패인데 403
- 권한 부족인데 재로그인 유도

올바른 분류:

```text
인증 정보 없음 / 유효하지 않음
→ 401

인증은 되었지만 권한 부족
→ 403
```

---

### [실무]

잘못된 예:

```text
User Token으로 /api/admin/users 호출
→ 401 Unauthorized
→ Frontend가 재로그인 시도
→ 재로그인해도 계속 실패
```

수정:

```text
User Token으로 /api/admin/users 호출
→ 403 Forbidden
→ Frontend가 권한 없음 안내
```

검수 기준:

```text
Token 없음 테스트
→ 401 확인

위조 Token 테스트
→ 401 확인

만료 Token 테스트
→ 401 확인

User Token to Admin API
→ 403 확인

Other User Resource 접근
→ 403 확인
```

---

### [FAQ]

Q. 401과 403을 잘못 쓰면 어떤 문제가 생겨?
A. Frontend가 재발급, 재로그인, 권한 없음 처리를 잘못 수행해 사용자 경험과 보안 분석이 혼란스러워진다.

Q. 권한 부족을 401로 처리하면 안 돼?
A. 권장하지 않는다. 인증된 사용자의 권한 부족은 403으로 처리하는 것이 일반적이다.

Q. Token 만료를 403으로 처리해도 돼?
A. 권장하지 않는다. Token 만료는 인증 실패이므로 401로 처리하는 것이 일반적이다.

---

# 5. CORS Rules

## 5.1 CORS Concept

### [개념]

CORS(Cross-Origin Resource Sharing)는 브라우저가 다른 Origin으로 API 요청을 보낼 때 서버가 해당 요청을 허용할지 판단하는 브라우저 보안 정책이다.

CORS는 인증 / 인가를 대체하는 보안 기능이 아니라 브라우저의 Origin 접근 제어 정책이다.

---

### [핵심]

CORS 핵심 키워드:

- CORS
- Origin
- Cross-Origin
- allowedOrigins
- allowedMethods
- allowedHeaders
- exposedHeaders
- allowCredentials
- Preflight
- OPTIONS
- Authorization Header
- Cookie
- withCredentials

CORS Flow:

```text
Browser
→ Preflight OPTIONS
→ Server CORS Policy 확인
→ 허용 시 실제 요청
```

---

### [실무]

CORS 설정은 Frontend Token 전달 방식에 따라 달라진다.

Header 기반 JWT 구조:

```text
Access Token
→ Authorization Header로 전달
→ CORS allowedHeaders에 Authorization 필요
→ allowCredentials는 필수 아님
```

Cookie 기반 Refresh Token 구조:

```text
Refresh Token
→ HttpOnly Cookie로 전달
→ CORS allowCredentials(true) 필요할 수 있음
→ allowedOrigins는 wildcard 사용 금지
→ Frontend withCredentials 설정 필요
```

Spring Security CORS 연결 예:

```java
@Bean
public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
    return http
            .cors(cors -> {})
            .csrf(csrf -> csrf.disable())
            .authorizeHttpRequests(auth -> auth
                    .requestMatchers("/api/auth/**").permitAll()
                    .anyRequest().authenticated()
            )
            .build();
}
```

Header 기반 JWT CORS 예:

```java
@Bean
public CorsConfigurationSource corsConfigurationSource() {
    CorsConfiguration config = new CorsConfiguration();

    config.setAllowedOrigins(List.of(
            "http://localhost:3000",
            "https://app.example.com"
    ));
    config.setAllowedMethods(List.of(
            "GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"
    ));
    config.setAllowedHeaders(List.of(
            "Authorization", "Content-Type"
    ));

    UrlBasedCorsConfigurationSource source =
            new UrlBasedCorsConfigurationSource();
    source.registerCorsConfiguration("/**", config);

    return source;
}
```

Cookie 기반 Refresh Token CORS 예:

```java
@Bean
public CorsConfigurationSource corsConfigurationSource() {
    CorsConfiguration config = new CorsConfiguration();

    config.setAllowedOrigins(List.of(
            "https://app.example.com"
    ));
    config.setAllowedMethods(List.of(
            "GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"
    ));
    config.setAllowedHeaders(List.of(
            "Authorization", "Content-Type"
    ));
    config.setAllowCredentials(true);

    UrlBasedCorsConfigurationSource source =
            new UrlBasedCorsConfigurationSource();
    source.registerCorsConfiguration("/**", config);

    return source;
}
```

권장:

- Frontend Origin을 정확히 등록한다.
- 개발 Origin과 운영 Origin을 분리한다.
- Authorization Header를 허용한다.
- OPTIONS Preflight를 차단하지 않는다.
- Cookie 인증 또는 Cookie Refresh Token을 사용하지 않는다면 `allowCredentials(true)`가 필수는 아니다.
- credentials 사용 시 wildcard Origin을 피한다.
- CORS와 인증 실패를 구분한다.

---

### [FAQ]

Q. CORS는 뭐야?
A. 브라우저가 다른 Origin으로 API 요청을 보낼 때 서버 허용 여부를 확인하는 보안 정책이다.

Q. CORS는 인증이야?
A. 아니다. CORS는 브라우저 Origin 정책이며 인증 / 인가를 대체하지 않는다.

Q. Spring Security를 쓰면 CORS 설정도 SecurityFilterChain에 연결해야 해?
A. 맞다. SecurityFilterChain에서 cors 설정을 활성화해야 CORS 정책이 제대로 적용된다.

Q. allowCredentials(true)는 항상 필요해?
A. 아니다. Cookie를 주고받는 구조라면 필요할 수 있지만 Header 기반 JWT만 사용한다면 필수는 아니다.

---

## 5.2 Preflight OPTIONS Rules

### [개념]

Preflight OPTIONS는 브라우저가 실제 요청을 보내기 전에 서버가 Cross-Origin 요청을 허용하는지 확인하기 위해 보내는 사전 요청이다.

Authorization Header, Custom Header, PUT, PATCH, DELETE 같은 요청은 Preflight가 발생할 수 있다.

---

### [핵심]

Preflight 핵심 키워드:

- OPTIONS
- Preflight Request
- Access-Control-Request-Method
- Access-Control-Request-Headers
- Access-Control-Allow-Origin
- Access-Control-Allow-Methods
- Access-Control-Allow-Headers

Preflight 발생 후보:

- Authorization Header 포함
- Content-Type이 단순 요청 범위를 벗어남
- PUT / PATCH / DELETE 사용
- Custom Header 사용
- credentials 사용

---

### [실무]

Preflight Flow:

```text
Browser
→ OPTIONS /api/posts
→ Origin 확인
→ Access-Control-Request-Method 확인
→ Access-Control-Request-Headers 확인
→ Server CORS Policy 응답
→ 실제 요청 진행
```

권장:

- OPTIONS Method를 CORS allowedMethods에 포함한다.
- Authorization Header를 allowedHeaders에 포함한다.
- Spring Security에서 OPTIONS 요청이 불필요하게 인증 실패하지 않도록 설정한다.
- 개발자 도구 Network에서 Preflight 요청을 확인한다.
- Postman 테스트와 브라우저 테스트를 구분한다.

문제 상황:

```text
Postman 요청 성공
→ Browser 요청 실패
→ CORS Preflight 차단 가능성 확인
```

---

### [FAQ]

Q. Preflight는 뭐야?
A. 브라우저가 실제 요청 전에 서버의 CORS 허용 여부를 확인하기 위해 보내는 OPTIONS 요청이다.

Q. Authorization Header 때문에 Preflight가 생길 수 있어?
A. 가능하다. Authorization Header는 Preflight를 유발할 수 있으므로 allowedHeaders에 포함해야 한다.

Q. Postman에서는 되는데 브라우저에서 안 되는 이유는 뭐야?
A. CORS는 브라우저 정책이므로 Postman에서는 발생하지 않을 수 있다.

---

## 5.3 CORS Credentials Rules

### [개념]

CORS Credentials는 브라우저가 Cross-Origin 요청에서 Cookie, Authorization 인증서, TLS Client Certificate 같은 인증 정보를 포함해 요청할 수 있도록 허용하는 설정이다.

Spring Boot + SPA 구조에서 `allowCredentials(true)`는 주로 Cookie 기반 Refresh Token 또는 Cookie 기반 Session을 사용할 때 검토한다.

---

### [핵심]

Credentials 관련 키워드:

- allowCredentials
- withCredentials
- Cookie
- HttpOnly Cookie
- Refresh Token Cookie
- Access-Control-Allow-Credentials
- wildcard origin
- SameSite
- Secure

Credentials 필요 후보:

- Refresh Token HttpOnly Cookie
- Session Cookie
- OAuth2 Authorization Request Cookie
- Cross-Origin Cookie 기반 로그인 유지

Credentials가 필수가 아닌 후보:

- Access Token을 Authorization Header로만 전송
- Cookie를 사용하지 않는 순수 Header 기반 JWT API

---

### [실무]

Cookie 기반 요청 구조:

```text
Backend
→ Set-Cookie: refreshToken=...
→ Frontend Reissue 요청 withCredentials=true
→ Browser Cookie 자동 전송
→ Backend Refresh Token 검증
```

Backend CORS 조건:

```text
allowCredentials(true)
allowedOrigins에 명시적 Origin 사용
wildcard "*" 사용 금지
```

Frontend 조건:

```javascript
axios.post("/api/auth/reissue", null, {
  withCredentials: true,
});
```

Header 기반 JWT 구조:

```text
Access Token
→ Authorization Header 직접 첨부
→ Cookie 자동 전송 없음
→ allowCredentials(true)는 필수 아님
```

권장:

- Cookie를 사용하지 않으면 credentials 설정을 과도하게 켜지 않는다.
- credentials를 켜면 allowedOrigins를 명시적으로 제한한다.
- `*` Origin과 credentials 조합을 피한다.
- Cookie 방식은 CSRF와 SameSite 정책을 함께 검토한다.
- 개발 / 운영 Origin을 profile로 분리한다.

---

### [FAQ]

Q. allowCredentials(true)는 언제 필요해?
A. Cross-Origin 요청에서 Cookie를 보내야 할 때 필요할 수 있다. 예를 들어 Refresh Token을 HttpOnly Cookie로 저장하는 구조다.

Q. Header 기반 JWT에서도 allowCredentials(true)가 필요해?
A. 일반적으로 필수는 아니다. Access Token을 Authorization Header로만 보낸다면 credentials 없이도 동작할 수 있다.

Q. credentials를 켜면 왜 wildcard Origin을 피해야 해?
A. 인증 정보가 포함되는 요청이므로 허용 Origin을 명확히 제한해야 한다.

---

## 5.4 CORS Troubleshooting

### [개념]

CORS Troubleshooting은 브라우저에서 Cross-Origin API 요청이 차단되는 문제를 분석하는 과정이다.

CORS 에러는 인증 실패가 아니라 브라우저 Origin 정책 문제다.

---

### [핵심]

확인 대상:

- Frontend Origin
- Backend allowedOrigins
- allowedMethods
- allowedHeaders
- exposedHeaders
- allowCredentials
- OPTIONS Preflight
- SecurityFilterChain cors 설정
- Authorization Header 허용 여부
- withCredentials 사용 여부

---

### [실무]

Debug Flow:

```text
Browser Console 확인
→ Network에서 OPTIONS 요청 확인
→ Request Origin 확인
→ Response Header 확인
→ allowedOrigins 확인
→ allowedMethods 확인
→ allowedHeaders 확인
→ allowCredentials 확인
→ SecurityFilterChain cors 설정 확인
→ Cookie 사용 시 withCredentials 확인
```

자주 발생하는 원인:

```text
Frontend Origin 불일치
→ http://localhost:3000 누락

Authorization Header 미허용
→ allowedHeaders에 Authorization 없음

OPTIONS 미허용
→ allowedMethods에 OPTIONS 없음

credentials + wildcard Origin
→ allowCredentials(true)와 "*" 조합 문제

Cookie 사용 중 withCredentials 누락
→ Refresh Token Cookie 미전송

SecurityFilterChain cors 미연결
→ .cors(cors -> {}) 누락
```

권장:

- 브라우저 개발자 도구 Console과 Network를 함께 확인한다.
- Preflight 응답 Header를 확인한다.
- 실제 API 응답이 아니라 Preflight에서 막혔는지 구분한다.
- CORS 문제를 JWT 문제로 오해하지 않는다.
- 운영 환경에서 모든 Origin 허용을 피한다.

---

### [FAQ]

Q. CORS 에러는 인증 실패야?
A. 아니다. 브라우저 Origin 정책 문제다. 인증 실패와 CORS 설정 문제를 구분해야 한다.

Q. Authorization Header 때문에 CORS가 날 수 있어?
A. 가능하다. allowedHeaders에 Authorization이 허용되어 있는지 확인해야 한다.

Q. CORS 문제는 어디서 확인해?
A. 브라우저 개발자 도구 Console과 Network의 OPTIONS Preflight 요청을 확인한다.

Q. Cookie 방식인데 Refresh Token이 안 보내지면 뭘 봐야 해?
A. allowCredentials, allowedOrigins, SameSite, Secure, withCredentials, Cookie Path를 확인해야 한다.

---

## 5.5 CORS Anti Pattern

### [개념]

CORS Anti Pattern은 개발 편의를 위해 모든 Origin, Method, Header를 무분별하게 허용하거나 CORS를 인증 / 인가처럼 오해하는 잘못된 설정이다.

---

### [핵심]

대표 Anti Pattern:

- 운영에서 모든 Origin 허용
- credentials 사용하면서 wildcard Origin 사용
- Cookie를 쓰지 않는데 credentials를 습관적으로 켬
- Authorization Header 미허용
- OPTIONS 요청 차단
- CORS를 인증 실패로 오해
- Postman 성공을 브라우저 성공으로 착각
- CORS 허용을 API 보안으로 착각
- 개발 Origin을 운영 설정에 방치
- 운영 Origin 누락

위험한 설정 예:

```java
config.setAllowedOrigins(List.of("*"));
config.setAllowedMethods(List.of("*"));
config.setAllowedHeaders(List.of("*"));
config.setAllowCredentials(true);
```

---

### [실무]

Header 기반 JWT 운영 권장 예:

```java
config.setAllowedOrigins(List.of(
        "https://app.example.com"
));
config.setAllowedMethods(List.of(
        "GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"
));
config.setAllowedHeaders(List.of(
        "Authorization", "Content-Type"
));
```

Cookie 기반 Refresh Token 운영 권장 예:

```java
config.setAllowedOrigins(List.of(
        "https://app.example.com"
));
config.setAllowedMethods(List.of(
        "GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"
));
config.setAllowedHeaders(List.of(
        "Authorization", "Content-Type"
));
config.setAllowCredentials(true);
```

Review 기준:

```text
CORS allowedOrigins 확인
→ 운영 Origin만 허용되는지 확인
→ wildcard 사용 여부 확인
→ credentials 필요 여부 확인
→ Cookie 사용 여부 확인
→ Authorization Header 허용 확인
→ OPTIONS 허용 확인
→ SecurityFilterChain cors 연결 확인
```

주의:

- CORS를 모두 허용해도 Backend 인증 / 인가는 반드시 필요하다.
- CORS 차단은 브라우저 요청 차단이지 API 권한 검증이 아니다.
- 운영에서는 허용 Origin을 최소화한다.
- Localhost 개발 Origin이 운영에 남지 않도록 profile 분리를 검토한다.

---

### [FAQ]

Q. CORS를 모두 허용하면 안전해?
A. 아니다. 개발 중 임시 허용은 가능하지만 운영에서는 허용 Origin, Method, Header를 제한해야 한다.

Q. CORS 허용하면 API 보안도 해결돼?
A. 아니다. CORS는 인증 / 인가가 아니므로 Backend Security는 별도로 필요하다.

Q. 운영에서 localhost Origin을 남겨도 돼?
A. 권장하지 않는다. 개발 / 운영 CORS 설정을 profile로 분리하는 것이 좋다.

Q. Cookie를 안 쓰는데 allowCredentials(true)를 켜야 해?
A. 필수는 아니다. Header 기반 JWT만 사용한다면 credentials 설정은 보통 필요하지 않다.

---

# 6. CSRF Rules

## 6.1 CSRF Concept

### [개념]

CSRF(Cross-Site Request Forgery)는 사용자가 인증된 상태를 악용해 원치 않는 요청을 보내게 하는 공격이다.

브라우저가 Cookie 같은 인증 정보를 자동으로 전송하는 구조에서 특히 중요하다.

---

### [핵심]

CSRF 핵심 키워드:

- CSRF
- Cross-Site Request Forgery
- Cookie-based Session
- Browser Auto Credential
- CSRF Token
- SameSite Cookie
- HttpOnly
- Secure
- Stateless JWT
- Authorization Header
- Refresh Token Cookie

CSRF 위험 조건:

```text
Browser가 인증 정보를 자동 전송
→ 공격 페이지에서 요청 유도
→ 사용자가 의도하지 않은 요청 실행
```

---

### [실무]

CSRF 발생 가능성이 높은 구조:

```text
Session Cookie 기반 로그인
→ Browser가 JSESSIONID 자동 전송
→ CSRF 보호 필요
```

CSRF 위험이 상대적으로 낮은 구조:

```text
Authorization Header 기반 Stateless JWT
→ 공격 페이지가 Header Token을 자동 첨부하기 어려움
→ CSRF disable 검토 가능
```

Refresh Token Cookie 구조:

```text
Refresh Token HttpOnly Cookie 저장
→ Reissue 요청 시 Cookie 자동 전송 가능
→ SameSite / CSRF 정책 검토 필요
```

주의:

- CSRF는 CORS와 다르다.
- CSRF disable을 무조건 적용하지 않는다.
- Cookie에 Token을 저장하면 CSRF를 다시 검토해야 한다.
- SameSite, HttpOnly, Secure Cookie 설정을 함께 검토한다.
- 보안 요구사항이 높으면 별도 위협 모델을 작성한다.

---

### [FAQ]

Q. CSRF는 뭐야?
A. 사용자가 인증된 상태를 악용해 원치 않는 요청을 보내게 하는 공격이다.

Q. CSRF와 CORS는 같은 거야?
A. 아니다. CORS는 Origin 접근 정책이고 CSRF는 사용자의 인증 상태를 악용한 요청 위조 공격이다.

Q. Cookie 기반 로그인에서 CSRF가 중요한 이유는 뭐야?
A. 브라우저가 인증 Cookie를 자동 전송하므로 사용자가 의도하지 않은 요청이 인증된 상태로 처리될 수 있기 때문이다.

---

## 6.2 CSRF Disable Decision Rules

### [개념]

CSRF Disable Decision은 Spring Security에서 CSRF 보호를 비활성화해도 되는 구조인지 판단하는 기준이다.

JWT 기반 REST API라고 해서 항상 CSRF 비활성화가 안전한 것은 아니며 Token 저장 위치와 인증 전송 방식에 따라 판단해야 한다.

---

### [핵심]

판단 기준:

```text
Session Cookie 기반 인증인가?
→ CSRF 보호 필요

Authorization Header 기반 Stateless JWT인가?
→ CSRF 위험 상대적으로 낮음
→ csrf disable 검토 가능

JWT 또는 Refresh Token을 Cookie에 저장하는가?
→ CSRF 다시 검토 필요
```

설정 예:

```java
.csrf(csrf -> csrf.disable())
```

---

### [실무]

CSRF disable 가능 후보:

```text
React SPA
→ Access Token Memory 또는 Storage 저장
→ API 요청 시 Authorization Header 직접 첨부
→ Stateless JWT API
→ Cookie 자동 전송 없음
→ csrf.disable 검토 가능
```

CSRF 보호 필요 후보:

```text
Spring MVC Form Login
→ JSESSIONID Cookie 사용
→ Browser 자동 Cookie 전송
→ CSRF Token 필요
```

Cookie JWT / Refresh Token 구조 검토:

```text
Refresh Token HttpOnly Cookie 저장
→ Reissue API 요청 시 Cookie 자동 전송
→ SameSite / CSRF 방어 검토
```

권장:

- CSRF disable 사유를 문서화한다.
- 인증 정보가 자동 전송되는지 확인한다.
- Cookie 저장 방식이면 SameSite 정책을 검토한다.
- Header 기반 Token이면 CSRF 위험은 낮지만 XSS 위험을 별도로 검토한다.
- 보안 요구사항이 높은 서비스는 CSRF / XSS를 함께 분석한다.

---

### [FAQ]

Q. JWT를 쓰면 CSRF를 꺼도 돼?
A. Authorization Header 기반 Stateless JWT 구조라면 CSRF 비활성화를 검토할 수 있다. 단, Cookie 저장 방식이면 다시 검토해야 한다.

Q. csrf.disable은 항상 안전해?
A. 아니다. 인증 정보가 Cookie로 자동 전송되는 구조라면 CSRF 보호가 필요할 수 있다.

Q. Refresh Token을 HttpOnly Cookie에 넣으면 CSRF를 검토해야 해?
A. 맞다. Cookie는 브라우저가 자동 전송할 수 있으므로 SameSite와 CSRF 정책을 함께 검토해야 한다.

---

## 6.3 CSRF Token Rules

### [개념]

CSRF Token은 서버가 발급한 난수 값을 요청에 함께 보내도록 해 위조 요청을 차단하는 방어 수단이다.

Session Cookie 기반 인증 구조에서는 CSRF Token을 사용해 사용자가 의도한 요청인지 확인할 수 있다.

---

### [핵심]

CSRF Token 핵심 키워드:

- CSRF Token
- Synchronizer Token Pattern
- CookieCsrfTokenRepository
- X-CSRF-TOKEN
- SameSite
- Session
- Form Login

검증 흐름:

```text
Page Load
→ CSRF Token 발급
→ Form 또는 Header에 Token 포함
→ State-changing Request
→ Server Token 검증
→ 허용 또는 차단
```

---

### [실무]

CSRF 보호가 필요한 요청:

- POST
- PUT
- PATCH
- DELETE
- 상태 변경 요청
- 결제 요청
- 계정 변경 요청
- 비밀번호 변경 요청

예시 설정:

```java
.csrf(csrf -> csrf
        .csrfTokenRepository(CookieCsrfTokenRepository.withHttpOnlyFalse())
)
```

주의:

- REST API + Authorization Header JWT 구조에서는 사용하지 않을 수 있다.
- Cookie 기반 인증이면 CSRF Token 또는 SameSite 정책을 검토한다.
- CSRF Token을 LocalStorage에 무분별하게 저장하지 않는다.
- Token 검증 실패는 403으로 처리될 수 있다.
- Frontend가 CSRF Token을 Header에 포함하도록 연동해야 한다.

---

### [FAQ]

Q. CSRF Token은 언제 필요해?
A. Cookie 기반 인증에서 POST, PUT, PATCH, DELETE 같은 상태 변경 요청을 보호할 때 필요하다.

Q. CSRF Token 검증 실패는 401이야 403이야?
A. 인증 상태는 있을 수 있지만 요청이 허용되지 않는 것이므로 일반적으로 403으로 처리될 수 있다.

Q. REST API에서도 CSRF Token이 항상 필요해?
A. 아니다. Authorization Header 기반 Stateless JWT 구조라면 필요성이 낮을 수 있다.

---

## 6.4 SameSite, HttpOnly, Secure Cookie Rules

### [개념]

SameSite, HttpOnly, Secure는 Cookie 기반 인증 또는 Refresh Token Cookie 구조에서 함께 검토해야 하는 Cookie 보안 속성이다.

Cookie를 사용하면 브라우저가 인증 정보를 자동 전송할 수 있으므로 CSRF와 XSS 관점의 보안 설정이 필요하다.

---

### [핵심]

Cookie 보안 속성:

- HttpOnly
- Secure
- SameSite
- Path
- Max-Age
- Domain

속성 의미:

| 속성     | 목적                        | 주의                            |
| -------- | --------------------------- | ------------------------------- |
| HttpOnly | JavaScript 접근 차단        | XSS 완화                        |
| Secure   | HTTPS에서만 전송            | 로컬 개발 예외 필요             |
| SameSite | Cross-Site Cookie 전송 제한 | OAuth2 / Cross-Origin 구조 검토 |
| Path     | Cookie 전송 경로 제한       | Reissue 경로와 일치 필요        |
| Max-Age  | Cookie 수명                 | Refresh Token 만료와 일치 필요  |

---

### [실무]

Refresh Token Cookie 예:

```java
ResponseCookie cookie = ResponseCookie.from("refreshToken", refreshToken)
        .httpOnly(true)
        .secure(true)
        .sameSite("Lax")
        .path("/api/auth/reissue")
        .maxAge(refreshTokenMaxAge)
        .build();

response.addHeader(HttpHeaders.SET_COOKIE, cookie.toString());
```

Cookie 제거 예:

```java
ResponseCookie deleteCookie = ResponseCookie.from("refreshToken", "")
        .httpOnly(true)
        .secure(true)
        .sameSite("Lax")
        .path("/api/auth/reissue")
        .maxAge(0)
        .build();

response.addHeader(HttpHeaders.SET_COOKIE, deleteCookie.toString());
```

권장:

- Refresh Token Cookie는 HttpOnly를 적용한다.
- 운영 환경에서는 Secure를 적용한다.
- Cross-Site 요청이 필요한 경우 SameSite 정책을 명확히 검토한다.
- Cookie Path는 Reissue API 경로와 맞춘다.
- Logout 시 동일 Path와 속성으로 Cookie를 제거한다.
- Cookie 방식이면 CORS credentials와 CSRF 정책을 함께 검토한다.

---

### [FAQ]

Q. Refresh Token Cookie에는 HttpOnly를 써야 해?
A. 권장된다. JavaScript 접근을 막아 XSS로 인한 Token 탈취 위험을 줄일 수 있다.

Q. Secure는 언제 필요해?
A. 운영 환경에서는 HTTPS에서만 Cookie가 전송되도록 Secure를 적용하는 것이 좋다.

Q. SameSite는 왜 중요해?
A. Cross-Site 요청에서 Cookie가 자동 전송되는 범위를 제한해 CSRF 위험을 줄일 수 있다.

Q. Cookie 삭제가 안 되면 뭘 확인해?
A. Cookie를 만들 때 사용한 Path, Domain, SameSite, Secure 조건과 삭제 응답의 조건이 일치하는지 확인해야 한다.

---

## 6.5 CSRF Anti Pattern

### [개념]

CSRF Anti Pattern은 인증 방식과 Token 저장 위치를 고려하지 않고 CSRF를 무조건 비활성화하거나 CORS와 혼동하는 잘못된 보안 설정이다.

---

### [핵심]

대표 Anti Pattern:

- Cookie 기반 Session인데 csrf.disable 적용
- Refresh Token Cookie 사용하면서 CSRF 검토 없음
- CSRF와 CORS를 같은 문제로 오해
- SameSite 없이 Cookie 인증 사용
- 상태 변경 요청에 CSRF 방어 없음
- CSRF Token 검증 실패를 인증 실패로 오해
- 보안 요구사항 검토 없이 disable 복붙

---

### [실무]

Review 기준:

```text
인증 방식 확인
→ Session Cookie 사용 여부 확인
→ JWT 저장 위치 확인
→ Cookie 자동 전송 여부 확인
→ State-changing API 확인
→ csrf.disable 근거 확인
→ SameSite / HttpOnly / Secure 확인
```

잘못된 예:

```java
.csrf(csrf -> csrf.disable())
```

문제:

```text
Session Cookie 기반 인증인데 CSRF 비활성화
→ 공격 페이지에서 인증된 상태 변경 요청을 유도할 수 있음
```

수정 방향:

```text
Session Cookie 기반 인증
→ CSRF Token 사용 검토
→ SameSite Cookie 설정 검토
→ State-changing API 보호
```

---

### [FAQ]

Q. CSRF disable을 복붙해도 돼?
A. 안 된다. 인증 방식과 Token 저장 위치를 기준으로 판단해야 한다.

Q. CORS를 설정하면 CSRF도 막혀?
A. 아니다. CORS와 CSRF는 목적과 동작 방식이 다르다.

Q. Cookie 인증을 쓰면 무조건 위험해?
A. 무조건 위험한 것은 아니지만 CSRF, SameSite, HttpOnly, Secure 정책을 반드시 검토해야 한다.

---

# 7. Security Error Response Design

## 7.1 Common Error Response Format

### [개념]

Common Error Response Format은 Security 예외와 일반 Business 예외의 응답 형식을 통일하기 위한 API 응답 규칙이다.

Frontend는 일관된 `status`, `errorCode`, `message`를 기준으로 인증 만료, 권한 부족, 재로그인, 접근 차단을 처리할 수 있다.

---

### [핵심]

권장 필드:

- status
- errorCode
- message
- timestamp
- path

보안상 제외:

- stackTrace
- exception class full name
- raw token
- secret key
- password
- internal server path
- SQL message
- internal debug detail

---

### [실무]

공통 응답 예:

```json
{
  "status": 401,
  "errorCode": "TOKEN_EXPIRED",
  "message": "인증이 만료되었습니다.",
  "timestamp": "2026-07-04T12:00:00",
  "path": "/api/users/me"
}
```

SecurityConfig 연결 예:

```java
.exceptionHandling(exception -> exception
        .authenticationEntryPoint(customAuthenticationEntryPoint)
        .accessDeniedHandler(customAccessDeniedHandler)
)
```

권장:

- Security Handler에서도 공통 Error Response 객체를 재사용한다.
- ObjectMapper로 JSON 응답을 작성할 수 있다.
- 401 / 403 errorCode를 분리한다.
- Frontend Interceptor 처리 기준과 맞춘다.
- 보안 예외 응답은 짧고 명확하게 작성한다.

---

### [FAQ]

Q. Security Handler에서 ApiResponse 객체를 써도 돼?
A. 가능하다. ObjectMapper로 공통 응답 객체를 JSON으로 작성하면 응답 형식을 통일할 수 있다.

Q. Stack trace를 응답에 포함해도 돼?
A. 안 된다. 내부 구현 정보가 노출될 수 있다.

Q. errorCode는 왜 필요해?
A. Frontend가 Token 재발급, 재로그인, 권한 없음 안내를 구분하기 위해 필요하다.

---

## 7.2 Frontend Error Handling Contract

### [개념]

Frontend Error Handling Contract는 Backend Security 예외 응답을 Frontend가 어떻게 처리해야 하는지 정하는 연동 규칙이다.

Backend는 401 / 403 errorCode를 명확히 제공해 Frontend Auth Interceptor가 올바르게 동작하도록 해야 한다.

---

### [핵심]

Frontend 처리 기준:

```text
401 TOKEN_EXPIRED
→ Reissue 시도

401 REFRESH_TOKEN_INVALID
→ Logout 처리
→ Login Page 이동

401 UNAUTHORIZED
→ Login Page 이동

403 ACCESS_DENIED
→ 권한 없음 안내

403 ADMIN_REQUIRED
→ 관리자 권한 필요 안내
```

연동 요소:

- Axios Interceptor
- Authorization Header
- Refresh API
- Logout
- Protected Route
- Error Page
- Toast Message

---

### [실무]

Backend가 제공해야 할 정보:

- Access Token 만료 errorCode
- Refresh Token 실패 errorCode
- 일반 인증 실패 errorCode
- 권한 부족 errorCode
- Reissue API 명세
- Logout API 명세
- CORS Authorization Header 허용
- Cookie 사용 시 credentials 정책
- Cookie 사용 시 CSRF / SameSite 정책

권장:

- 401을 모두 재로그인으로 처리하지 않도록 errorCode를 분리한다.
- 403을 Token 재발급 대상으로 처리하지 않는다.
- Reissue 실패 시 Client Token을 제거하도록 명시한다.
- 권한 부족은 UX 안내로 처리한다.
- 반복 재발급 루프를 방지한다.

---

### [FAQ]

Q. 401이 오면 Frontend는 항상 재로그인해야 해?
A. 아니다. Access Token 만료라면 재발급을 시도하고, 재발급도 실패하면 재로그인 처리한다.

Q. 403이 오면 Token 재발급을 시도해야 해?
A. 아니다. 403은 권한 부족이므로 재발급 대상이 아니다.

Q. Backend가 errorCode를 세분화해야 하는 이유는 뭐야?
A. Frontend가 재발급, 로그아웃, 권한 없음 안내를 정확히 구분하기 위해서다.

---

# 8. Exception, CORS, CSRF Testing

## 8.1 Security Exception Test Rules

### [개념]

Security Exception Test는 인증 실패와 인가 실패가 올바른 Status Code와 errorCode로 응답되는지 검증하는 테스트다.

---

### [핵심]

테스트 대상:

- Token 없음
- 위조 Token
- 만료 Token
- User Token to Admin API
- Other User Resource 접근
- Method Security 실패
- Resource Owner Check 실패

기본 기대값:

```text
No Token
→ 401

Invalid Token
→ 401

Expired Token
→ 401 TOKEN_EXPIRED

User Token to Admin API
→ 403 ACCESS_DENIED

Other User Resource
→ 403 RESOURCE_ACCESS_DENIED
```

---

### [실무]

테스트 시나리오:

```text
Protected API without Token
→ AuthenticationEntryPoint
→ 401 확인
```

```text
Admin API with User Token
→ AccessDeniedHandler
→ 403 확인
```

```text
Owner API with Other User Token
→ AccessDeniedException
→ 403 확인
```

검증 기준:

- status code가 정확한가?
- errorCode가 Frontend 처리 기준과 맞는가?
- message가 과도하게 상세하지 않은가?
- Stack trace가 응답되지 않는가?
- 401과 403이 혼동되지 않는가?
- Security Handler가 적용되는가?

---

### [FAQ]

Q. Security Exception 테스트에서 가장 중요한 것은 뭐야?
A. 401과 403이 올바르게 분리되고 errorCode가 Frontend 처리 기준과 맞는지 확인하는 것이다.

Q. 위조 Token 테스트는 어떻게 해?
A. 정상 JWT 문자열 일부를 변경해 Protected API 요청 시 401이 반환되는지 확인한다.

Q. User Token으로 Admin API 테스트는 어떤 결과가 맞아?
A. 인증은 되었지만 관리자 권한이 없으므로 403이 맞다.

---

## 8.2 CORS Test Rules

### [개념]

CORS Test는 브라우저 환경에서 Frontend Origin, Authorization Header, Cookie credentials, OPTIONS Preflight가 정상 허용되는지 검증하는 테스트다.

---

### [핵심]

테스트 대상:

- 개발 Frontend Origin
- 운영 Frontend Origin
- 허용되지 않은 Origin
- Authorization Header
- Content-Type Header
- OPTIONS Preflight
- credentials
- allowedMethods
- allowedHeaders

기본 기대값:

```text
Allowed Origin
→ Preflight 성공
→ Actual Request 진행

Blocked Origin
→ Browser CORS 차단

Authorization Header 포함
→ allowedHeaders에 Authorization 필요

Cookie 포함 요청
→ allowCredentials와 withCredentials 필요
```

---

### [실무]

검증 흐름:

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

확인 Header:

```text
Access-Control-Allow-Origin
Access-Control-Allow-Methods
Access-Control-Allow-Headers
Access-Control-Allow-Credentials
```

권장:

- Postman만으로 CORS 테스트를 끝내지 않는다.
- 브라우저에서 실제 Frontend 요청으로 확인한다.
- 개발 / 운영 Origin을 각각 확인한다.
- Authorization Header 포함 요청을 확인한다.
- Cookie를 사용하지 않는 Header 기반 JWT 구조라면 credentials 테스트는 필수 항목이 아니다.
- Cookie 방식이면 credentials와 Cookie 전송 여부를 확인한다.

---

### [FAQ]

Q. CORS 테스트는 Postman으로 가능해?
A. 부족하다. CORS는 브라우저 정책이므로 실제 브라우저 요청으로 확인해야 한다.

Q. CORS 테스트에서 뭘 봐야 해?
A. Origin, OPTIONS Preflight, allowedHeaders, allowedMethods, 필요 시 allowCredentials를 확인해야 한다.

Q. Authorization Header가 있는 요청은 따로 테스트해야 해?
A. 해야 한다. allowedHeaders에 Authorization이 없으면 브라우저에서 차단될 수 있다.

Q. credentials 테스트는 항상 필요해?
A. 아니다. Cookie를 사용하지 않는 Header 기반 JWT 구조라면 필수는 아니다. Cookie 기반 Refresh Token이나 Session을 쓰면 필요하다.

---

## 8.3 CSRF Test Rules

### [개념]

CSRF Test는 인증 방식에 따라 CSRF 보호가 필요한 요청이 적절히 보호되는지 또는 비활성화 근거가 타당한지 검증하는 테스트다.

---

### [핵심]

테스트 대상:

- Session Cookie 기반 인증
- JWT Authorization Header 기반 인증
- Refresh Token Cookie 사용
- POST / PUT / PATCH / DELETE 요청
- CSRF Token 포함 요청
- CSRF Token 누락 요청
- SameSite Cookie 정책

---

### [실무]

Session Cookie 기반 테스트:

```text
로그인 Session Cookie 있음
→ CSRF Token 없이 POST 요청
→ 403 기대

로그인 Session Cookie 있음
→ CSRF Token 포함 POST 요청
→ 200 기대
```

JWT Header 기반 테스트:

```text
Authorization Header 없음
→ Protected API
→ 401 기대

Authorization Header 있음
→ Protected API
→ JWT 검증 기준으로 처리

CSRF Token 없음
→ Header 기반 JWT에서는 구조상 영향 낮음
```

Cookie Refresh Token 사용 시:

```text
Reissue API
→ Cookie 자동 전송 여부 확인
→ SameSite 정책 확인
→ CSRF 위험 검토
```

권장:

- CSRF disable이면 그 근거를 문서화한다.
- Cookie 기반 인증이면 상태 변경 요청 보호를 검증한다.
- Header 기반 JWT이면 XSS 위험도 함께 검토한다.
- Refresh Token Cookie 구조는 CSRF 검토 대상이다.

---

### [FAQ]

Q. CSRF 테스트는 언제 필요해?
A. Cookie 기반 인증이나 Refresh Token Cookie 구조를 사용할 때 필요하다.

Q. Header 기반 JWT에서도 CSRF 테스트가 필요해?
A. 상대적으로 중요도는 낮지만 CSRF disable 근거와 Token 저장 방식을 검토해야 한다.

Q. CSRF Token이 없으면 무조건 실패해야 해?
A. Cookie 기반 CSRF 보호가 활성화된 상태 변경 요청이라면 실패해야 한다.

---

# 9. Common Mistakes

## 9.1 Exception Handling Mistakes

### [개념]

Exception Handling Mistakes는 인증 실패와 권한 실패를 잘못 처리하거나 Security Filter Chain 예외가 GlobalExceptionHandler에서 처리된다고 오해하는 문제다.

---

### [핵심]

대표 실수:

- AuthenticationEntryPoint 미등록
- AccessDeniedHandler 미등록
- 401과 403 혼동
- Token 만료를 403으로 처리
- 권한 부족을 401로 처리
- Security 예외가 ControllerAdvice로 처리된다고 가정
- Stack trace 응답
- Token 원문 응답
- 내부 예외 메시지 노출
- Frontend 처리 기준 없는 errorCode

---

### [실무]

검수 기준:

```text
SecurityConfig exceptionHandling 확인
→ AuthenticationEntryPoint 등록 확인
→ AccessDeniedHandler 등록 확인
→ 401 / 403 테스트 확인
→ Error Response 형식 확인
→ 민감정보 노출 확인
→ Frontend errorCode 계약 확인
```

수정 방향:

```java
.exceptionHandling(exception -> exception
        .authenticationEntryPoint(customAuthenticationEntryPoint)
        .accessDeniedHandler(customAccessDeniedHandler)
)
```

---

### [FAQ]

Q. Security 예외 처리에서 가장 흔한 실수는 뭐야?
A. 401과 403을 혼동하거나 AuthenticationEntryPoint와 AccessDeniedHandler를 등록하지 않는 것이다.

Q. Security 예외가 ControllerAdvice에서 안 잡히면 문제야?
A. Spring Security Filter Chain 예외는 Handler에서 처리되는 것이 일반적이므로 EntryPoint와 AccessDeniedHandler를 구성해야 한다.

Q. Token 원문을 에러 응답에 넣어도 돼?
A. 안 된다. Token은 인증 수단이므로 응답과 로그에 노출하지 않는 것이 원칙이다.

---

## 9.2 CORS and CSRF Mistakes

### [개념]

CORS and CSRF Mistakes는 브라우저 Origin 정책과 요청 위조 공격을 혼동하거나 개발 편의 설정을 운영에 남기는 문제다.

---

### [핵심]

대표 실수:

- CORS를 인증 / 인가로 오해
- CORS 에러를 JWT 오류로 오해
- Postman 성공을 브라우저 성공으로 착각
- 운영에서 모든 Origin 허용
- credentials와 wildcard Origin 조합
- Cookie를 쓰지 않는데 credentials를 습관적으로 켬
- Authorization Header 미허용
- OPTIONS 차단
- Cookie 인증인데 CSRF disable
- Refresh Token Cookie 사용하면서 CSRF 검토 없음
- CORS와 CSRF를 같은 개념으로 처리

---

### [실무]

검수 기준:

```text
CORS allowedOrigins 확인
→ Authorization Header 허용 확인
→ OPTIONS 허용 확인
→ Cookie 사용 여부 확인
→ allowCredentials 필요 여부 확인
→ CSRF disable 근거 확인
→ SameSite / HttpOnly / Secure 확인
```

수정 방향:

```text
CORS 문제
→ Browser DevTools Network에서 Preflight 확인

CSRF 문제
→ 인증 정보 자동 전송 여부 확인
→ Cookie 기반이면 CSRF 보호 검토
```

---

### [FAQ]

Q. CORS와 CSRF를 헷갈리면 어떤 문제가 생겨?
A. 브라우저 차단 문제와 요청 위조 방어 문제를 잘못 해결해 보안 설정이 무력화될 수 있다.

Q. Postman에서 되면 CORS는 문제없는 거야?
A. 아니다. CORS는 브라우저 정책이므로 Postman 결과만으로 판단하면 안 된다.

Q. JWT를 쓰는데도 CSRF가 문제가 될 수 있어?
A. JWT를 Cookie에 저장하고 브라우저가 자동 전송하는 구조라면 CSRF를 검토해야 한다.

---

# 10. Part06 Checklist

## 10.1 Exception CORS CSRF Checklist

### [개념]

Part06 Checklist는 Security Exception Handling, CORS, CSRF 문서가 Security Advanced 기준에 맞게 설계되었는지 검수하기 위한 목록이다.

---

### [핵심]

Checklist:

```md
- [ ] AuthenticationEntryPoint 기준이 포함되었는가?
- [ ] AccessDeniedHandler 기준이 포함되었는가?
- [ ] 401 Unauthorized 기준이 명확한가?
- [ ] 403 Forbidden 기준이 명확한가?
- [ ] 401과 403 비교가 포함되었는가?
- [ ] Security 예외가 GlobalExceptionHandler로 항상 처리되지 않는다는 점이 포함되었는가?
- [ ] Security Error Response 형식이 포함되었는가?
- [ ] Frontend errorCode 처리 기준이 포함되었는가?
- [ ] Token 만료 / 위조 / 누락 응답 기준이 포함되었는가?
- [ ] Role 부족 / Owner Check 실패 응답 기준이 포함되었는가?
- [ ] CORS 개념이 포함되었는가?
- [ ] Preflight OPTIONS 기준이 포함되었는가?
- [ ] Authorization Header CORS 허용 기준이 포함되었는가?
- [ ] allowCredentials 조건부 기준이 포함되었는가?
- [ ] Header 기반 JWT와 Cookie 기반 Refresh Token CORS 차이가 포함되었는가?
- [ ] 운영 Origin 제한 기준이 포함되었는가?
- [ ] CORS Troubleshooting이 포함되었는가?
- [ ] CSRF 개념이 포함되었는가?
- [ ] CSRF disable 판단 기준이 포함되었는가?
- [ ] Cookie 기반 인증 CSRF 기준이 포함되었는가?
- [ ] Header 기반 JWT CSRF 기준이 포함되었는가?
- [ ] SameSite / HttpOnly / Secure 검토가 포함되었는가?
- [ ] CORS와 CSRF 차이가 포함되었는가?
- [ ] Security Exception Test 기준이 포함되었는가?
- [ ] CORS Test 기준이 포함되었는가?
- [ ] CSRF Test 기준이 포함되었는가?
- [ ] Retrieval Queries가 충분한가?
```

---

### [실무]

Review Flow:

```text
SecurityConfig exceptionHandling 확인
→ AuthenticationEntryPoint 확인
→ AccessDeniedHandler 확인
→ 401 / 403 테스트 확인
→ Error Response 형식 확인
→ CORS 설정 확인
→ Header 기반 JWT / Cookie 기반 Token 구조 확인
→ Browser Preflight 확인
→ CSRF disable 근거 확인
→ Cookie 인증 여부 확인
→ SameSite / HttpOnly / Secure 확인
→ Frontend Error Handling Contract 확인
```

선행 문서 연결:

```text
Part01 Core Concepts
→ 401 / 403 / Authentication / Authorization 기준 제공

Part02 SecurityFilterChain
→ exceptionHandling / cors / csrf 설정 위치 제공

Part04 JWT
→ Token Error Response / Access Token 만료 / Refresh Token Cookie 기준 제공

Part05 Authorization
→ AccessDeniedException / Resource Owner Check 실패 기준 제공
```

후속 문서 연결:

```text
Part06 Exception Handling CORS CSRF
→ Part07 OAuth2 Frontend Integration
→ Part08 Security Testing Troubleshooting
```

---

### [FAQ]

Q. Part06에서 가장 중요한 검수 포인트는 뭐야?
A. AuthenticationEntryPoint, AccessDeniedHandler, 401/403 분리, CORS Preflight, allowCredentials 조건, CSRF disable 판단 기준이다.

Q. Part06은 Frontend Auth Flow와 어떻게 연결돼?
A. 401 / 403 errorCode, CORS Authorization Header, Cookie credentials, Token 재발급 흐름으로 연결된다.

Q. Part06은 Testing 문서와 어떻게 연결돼?
A. Token 없음, 위조 Token, User Token to Admin API, CORS Preflight, CSRF Token 테스트로 연결된다.

---

# Retrieval Queries

### [FAQ]

Q. Security 예외도 GlobalExceptionHandler에서 처리돼?
A. 항상 그렇지 않다. Filter Chain에서 발생한 인증 / 인가 예외는 AuthenticationEntryPoint 또는 AccessDeniedHandler에서 처리되는 경우가 많다.

Q. Security Exception Handling에서 가장 중요한 것은 뭐야?
A. 인증 실패 401과 인가 실패 403을 분리하고 API 공통 에러 응답 형식과 맞추는 것이다.

Q. Security 에러 응답도 ApiResponse 형식으로 맞춰야 해?
A. 프로젝트 응답 규칙이 있다면 맞추는 것이 Frontend 처리에 좋다.

Q. AuthenticationEntryPoint는 언제 실행돼?
A. 인증 정보가 없거나 유효하지 않아 Protected API 접근이 거부될 때 실행된다.

Q. JWT 만료는 EntryPoint에서 처리해?
A. 일반적으로 인증 실패로 보고 401 응답을 EntryPoint에서 처리한다.

Q. Token 없음과 Token 위조를 모두 같은 메시지로 처리해도 돼?
A. 가능하다. 보안상 상세 원인을 과도하게 노출하지 않는 것이 좋다.

Q. 401 errorCode를 세분화해야 해?
A. Frontend 재발급 흐름이 필요하면 TOKEN_EXPIRED 같은 errorCode를 분리하는 것이 좋다.

Q. JWT 위조 상세 사유를 응답해도 돼?
A. 권장하지 않는다. 서명 오류, 파싱 오류 같은 상세 원인은 서버 로그에서만 관리하는 것이 좋다.

Q. Access Token 만료와 Refresh Token 만료는 같은 응답이어도 돼?
A. 처리 흐름이 다르므로 구분하는 것이 좋다. Access Token 만료는 재발급 시도, Refresh Token 만료는 재로그인이 필요하다.

Q. AccessDeniedHandler는 언제 실행돼?
A. 인증은 되었지만 Role, Authority, Resource Owner 조건을 만족하지 못할 때 실행된다.

Q. User Token으로 Admin API를 호출하면 EntryPoint가 실행돼?
A. 아니다. 인증은 되었으므로 일반적으로 AccessDeniedHandler가 실행되고 403이 반환된다.

Q. Resource Owner Check 실패는 401이야 403이야?
A. 인증된 사용자가 권한이 없는 상태이므로 일반적으로 403 Forbidden이다.

Q. 403 응답은 언제 사용해?
A. 인증은 되었지만 해당 기능이나 리소스에 접근할 권한이 없을 때 사용한다.

Q. 403이 오면 Frontend는 재로그인하면 돼?
A. 아니다. 403은 권한 부족이므로 권한 없음 안내나 접근 차단 처리가 맞다.

Q. 403 대신 404를 써도 돼?
A. 리소스 존재 여부를 숨겨야 하는 보안 정책이 있다면 404 전략을 검토할 수 있다.

Q. 401과 403 차이는?
A. 401은 인증 실패이고 403은 인증은 되었지만 권한이 부족한 상태다.

Q. Token이 없으면 401이야 403이야?
A. 사용자를 확인할 수 없으므로 401이다.

Q. User Token으로 Admin API를 호출하면 401이야 403이야?
A. 사용자는 인증되었지만 관리자 권한이 부족하므로 403이다.

Q. 401과 403을 잘못 쓰면 어떤 문제가 생겨?
A. Frontend가 재발급, 재로그인, 권한 없음 처리를 잘못 수행해 사용자 경험과 보안 분석이 혼란스러워진다.

Q. 권한 부족을 401로 처리하면 안 돼?
A. 권장하지 않는다. 인증된 사용자의 권한 부족은 403으로 처리하는 것이 일반적이다.

Q. Token 만료를 403으로 처리해도 돼?
A. 권장하지 않는다. Token 만료는 인증 실패이므로 401로 처리하는 것이 일반적이다.

Q. CORS는 뭐야?
A. 브라우저가 다른 Origin으로 API 요청을 보낼 때 서버 허용 여부를 확인하는 보안 정책이다.

Q. CORS는 인증이야?
A. 아니다. CORS는 브라우저 Origin 정책이며 인증 / 인가를 대체하지 않는다.

Q. Spring Security를 쓰면 CORS 설정도 SecurityFilterChain에 연결해야 해?
A. 맞다. SecurityFilterChain에서 cors 설정을 활성화해야 CORS 정책이 제대로 적용된다.

Q. allowCredentials(true)는 항상 필요해?
A. 아니다. Cookie를 주고받는 구조라면 필요할 수 있지만 Header 기반 JWT만 사용한다면 필수는 아니다.

Q. Preflight는 뭐야?
A. 브라우저가 실제 요청 전에 서버의 CORS 허용 여부를 확인하기 위해 보내는 OPTIONS 요청이다.

Q. Authorization Header 때문에 Preflight가 생길 수 있어?
A. 가능하다. Authorization Header는 Preflight를 유발할 수 있으므로 allowedHeaders에 포함해야 한다.

Q. Postman에서는 되는데 브라우저에서 안 되는 이유는 뭐야?
A. CORS는 브라우저 정책이므로 Postman에서는 발생하지 않을 수 있다.

Q. allowCredentials(true)는 언제 필요해?
A. Cross-Origin 요청에서 Cookie를 보내야 할 때 필요할 수 있다. 예를 들어 Refresh Token을 HttpOnly Cookie로 저장하는 구조다.

Q. Header 기반 JWT에서도 allowCredentials(true)가 필요해?
A. 일반적으로 필수는 아니다. Access Token을 Authorization Header로만 보낸다면 credentials 없이도 동작할 수 있다.

Q. credentials를 켜면 왜 wildcard Origin을 피해야 해?
A. 인증 정보가 포함되는 요청이므로 허용 Origin을 명확히 제한해야 한다.

Q. CORS 에러는 인증 실패야?
A. 아니다. 브라우저 Origin 정책 문제다. 인증 실패와 CORS 설정 문제를 구분해야 한다.

Q. Authorization Header 때문에 CORS가 날 수 있어?
A. 가능하다. allowedHeaders에 Authorization이 허용되어 있는지 확인해야 한다.

Q. CORS 문제는 어디서 확인해?
A. 브라우저 개발자 도구 Console과 Network의 OPTIONS Preflight 요청을 확인한다.

Q. Cookie 방식인데 Refresh Token이 안 보내지면 뭘 봐야 해?
A. allowCredentials, allowedOrigins, SameSite, Secure, withCredentials, Cookie Path를 확인해야 한다.

Q. CORS를 모두 허용하면 안전해?
A. 아니다. 개발 중 임시 허용은 가능하지만 운영에서는 허용 Origin, Method, Header를 제한해야 한다.

Q. CORS 허용하면 API 보안도 해결돼?
A. 아니다. CORS는 인증 / 인가가 아니므로 Backend Security는 별도로 필요하다.

Q. 운영에서 localhost Origin을 남겨도 돼?
A. 권장하지 않는다. 개발 / 운영 CORS 설정을 profile로 분리하는 것이 좋다.

Q. Cookie를 안 쓰는데 allowCredentials(true)를 켜야 해?
A. 필수는 아니다. Header 기반 JWT만 사용한다면 credentials 설정은 보통 필요하지 않다.

Q. CSRF는 뭐야?
A. 사용자가 인증된 상태를 악용해 원치 않는 요청을 보내게 하는 공격이다.

Q. CSRF와 CORS는 같은 거야?
A. 아니다. CORS는 Origin 접근 정책이고 CSRF는 사용자의 인증 상태를 악용한 요청 위조 공격이다.

Q. Cookie 기반 로그인에서 CSRF가 중요한 이유는 뭐야?
A. 브라우저가 인증 Cookie를 자동 전송하므로 사용자가 의도하지 않은 요청이 인증된 상태로 처리될 수 있기 때문이다.

Q. JWT를 쓰면 CSRF를 꺼도 돼?
A. Authorization Header 기반 Stateless JWT 구조라면 CSRF 비활성화를 검토할 수 있다. 단, Cookie 저장 방식이면 다시 검토해야 한다.

Q. csrf.disable은 항상 안전해?
A. 아니다. 인증 정보가 Cookie로 자동 전송되는 구조라면 CSRF 보호가 필요할 수 있다.

Q. Refresh Token을 HttpOnly Cookie에 넣으면 CSRF를 검토해야 해?
A. 맞다. Cookie는 브라우저가 자동 전송할 수 있으므로 SameSite와 CSRF 정책을 함께 검토해야 한다.

Q. CSRF Token은 언제 필요해?
A. Cookie 기반 인증에서 POST, PUT, PATCH, DELETE 같은 상태 변경 요청을 보호할 때 필요하다.

Q. CSRF Token 검증 실패는 401이야 403이야?
A. 인증 상태는 있을 수 있지만 요청이 허용되지 않는 것이므로 일반적으로 403으로 처리될 수 있다.

Q. REST API에서도 CSRF Token이 항상 필요해?
A. 아니다. Authorization Header 기반 Stateless JWT 구조라면 필요성이 낮을 수 있다.

Q. Refresh Token Cookie에는 HttpOnly를 써야 해?
A. 권장된다. JavaScript 접근을 막아 XSS로 인한 Token 탈취 위험을 줄일 수 있다.

Q. Secure는 언제 필요해?
A. 운영 환경에서는 HTTPS에서만 Cookie가 전송되도록 Secure를 적용하는 것이 좋다.

Q. SameSite는 왜 중요해?
A. Cross-Site 요청에서 Cookie가 자동 전송되는 범위를 제한해 CSRF 위험을 줄일 수 있다.

Q. Cookie 삭제가 안 되면 뭘 확인해?
A. Cookie를 만들 때 사용한 Path, Domain, SameSite, Secure 조건과 삭제 응답의 조건이 일치하는지 확인해야 한다.

Q. CSRF disable을 복붙해도 돼?
A. 안 된다. 인증 방식과 Token 저장 위치를 기준으로 판단해야 한다.

Q. CORS를 설정하면 CSRF도 막혀?
A. 아니다. CORS와 CSRF는 목적과 동작 방식이 다르다.

Q. Cookie 인증을 쓰면 무조건 위험해?
A. 무조건 위험한 것은 아니지만 CSRF, SameSite, HttpOnly, Secure 정책을 반드시 검토해야 한다.

Q. Security Handler에서 ApiResponse 객체를 써도 돼?
A. 가능하다. ObjectMapper로 공통 응답 객체를 JSON으로 작성하면 응답 형식을 통일할 수 있다.

Q. Stack trace를 응답에 포함해도 돼?
A. 안 된다. 내부 구현 정보가 노출될 수 있다.

Q. errorCode는 왜 필요해?
A. Frontend가 Token 재발급, 재로그인, 권한 없음 안내를 구분하기 위해 필요하다.

Q. 401이 오면 Frontend는 항상 재로그인해야 해?
A. 아니다. Access Token 만료라면 재발급을 시도하고, 재발급도 실패하면 재로그인 처리한다.

Q. 403이 오면 Token 재발급을 시도해야 해?
A. 아니다. 403은 권한 부족이므로 재발급 대상이 아니다.

Q. Backend가 errorCode를 세분화해야 하는 이유는 뭐야?
A. Frontend가 재발급, 로그아웃, 권한 없음 안내를 정확히 구분하기 위해서다.

Q. Security Exception 테스트에서 가장 중요한 것은 뭐야?
A. 401과 403이 올바르게 분리되고 errorCode가 Frontend 처리 기준과 맞는지 확인하는 것이다.

Q. 위조 Token 테스트는 어떻게 해?
A. 정상 JWT 문자열 일부를 변경해 Protected API 요청 시 401이 반환되는지 확인한다.

Q. User Token으로 Admin API 테스트는 어떤 결과가 맞아?
A. 인증은 되었지만 관리자 권한이 없으므로 403이 맞다.

Q. CORS 테스트는 Postman으로 가능해?
A. 부족하다. CORS는 브라우저 정책이므로 실제 브라우저 요청으로 확인해야 한다.

Q. CORS 테스트에서 뭘 봐야 해?
A. Origin, OPTIONS Preflight, allowedHeaders, allowedMethods, 필요 시 allowCredentials를 확인해야 한다.

Q. Authorization Header가 있는 요청은 따로 테스트해야 해?
A. 해야 한다. allowedHeaders에 Authorization이 없으면 브라우저에서 차단될 수 있다.

Q. credentials 테스트는 항상 필요해?
A. 아니다. Cookie를 사용하지 않는 Header 기반 JWT 구조라면 필수는 아니다. Cookie 기반 Refresh Token이나 Session을 쓰면 필요하다.

Q. CSRF 테스트는 언제 필요해?
A. Cookie 기반 인증이나 Refresh Token Cookie 구조를 사용할 때 필요하다.

Q. Header 기반 JWT에서도 CSRF 테스트가 필요해?
A. 상대적으로 중요도는 낮지만 CSRF disable 근거와 Token 저장 방식을 검토해야 한다.

Q. CSRF Token이 없으면 무조건 실패해야 해?
A. Cookie 기반 CSRF 보호가 활성화된 상태 변경 요청이라면 실패해야 한다.

Q. Security 예외 처리에서 가장 흔한 실수는 뭐야?
A. 401과 403을 혼동하거나 AuthenticationEntryPoint와 AccessDeniedHandler를 등록하지 않는 것이다.

Q. Security 예외가 ControllerAdvice에서 안 잡히면 문제야?
A. Spring Security Filter Chain 예외는 Handler에서 처리되는 것이 일반적이므로 EntryPoint와 AccessDeniedHandler를 구성해야 한다.

Q. Token 원문을 에러 응답에 넣어도 돼?
A. 안 된다. Token은 인증 수단이므로 응답과 로그에 노출하지 않는 것이 원칙이다.

Q. CORS와 CSRF를 헷갈리면 어떤 문제가 생겨?
A. 브라우저 차단 문제와 요청 위조 방어 문제를 잘못 해결해 보안 설정이 무력화될 수 있다.

Q. JWT를 쓰는데도 CSRF가 문제가 될 수 있어?
A. JWT를 Cookie에 저장하고 브라우저가 자동 전송하는 구조라면 CSRF를 검토해야 한다.

Q. Part06에서 가장 중요한 검수 포인트는 뭐야?
A. AuthenticationEntryPoint, AccessDeniedHandler, 401/403 분리, CORS Preflight, allowCredentials 조건, CSRF disable 판단 기준이다.

Q. Part06은 Frontend Auth Flow와 어떻게 연결돼?
A. 401 / 403 errorCode, CORS Authorization Header, Cookie credentials, Token 재발급 흐름으로 연결된다.

Q. Part06은 Testing 문서와 어떻게 연결돼?
A. Token 없음, 위조 Token, User Token to Admin API, CORS Preflight, CSRF Token 테스트로 연결된다.
