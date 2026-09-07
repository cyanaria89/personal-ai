# Security Advanced Domain Rules

---

# 1. Domain Purpose

## 1.1 Purpose

### [개념]

Security Advanced Domain Rules 문서는 Backend Agent / Review Agent / PM Agent용 RAG 문서 제작 규칙이다.

목적:

- Spring Security 기반 인증 / 인가 구조 설계 지원
- SecurityFilterChain 흐름 이해 지원
- Authentication / Authorization 판단 기준 제공
- JWT Access Token / Refresh Token 설계 기준 제공
- Login / Logout / Token Refresh 흐름 설계 지원
- SecurityContext 사용 기준 제공
- Custom UserDetails / Principal 설계 지원
- CORS / CSRF / Session 정책 판단 기준 제공
- Exception Handling / EntryPoint / AccessDeniedHandler 기준 제공
- OAuth2 Login 연동 기준 제공
- Security Anti Pattern 탐지 지원

---

### [핵심]

우선순위:

1. SecurityFilterChain
2. Authentication
3. Authorization
4. SecurityContext
5. Principal
6. Password Encoding
7. Login Flow
8. JWT Authentication
9. Access Token
10. Refresh Token
11. Token Reissue
12. Stateless Session
13. CORS
14. CSRF
15. Exception Handling
16. AuthenticationEntryPoint
17. AccessDeniedHandler
18. Role / Authority
19. OAuth2 Login
20. Security Anti Pattern

---

### [실무]

Security Advanced 문서는 단순 설정 코드 모음이 아니다.

Backend Agent가 아래 작업을 수행할 수 있도록 작성한다.

- 인증 / 인가 흐름 설계
- SecurityFilterChain 구성 검토
- Public / Protected Endpoint 분리
- JWT Filter 위치 판단
- Access Token / Refresh Token 역할 분리
- PasswordEncoder 적용 여부 검토
- SecurityContext 인증 객체 저장 기준 판단
- Controller에서 인증 사용자 접근 기준 제공
- 401 / 403 예외 응답 분리
- CORS와 인증 문제 구분
- CSRF 비활성화 여부 판단
- OAuth2 Login 흐름 설계
- 권한 검증 위치 판단
- 보안 취약 Anti Pattern 탐지

---

### [FAQ]

Q. Security Advanced Domain Rules는 Spring Boot Domain Rules와 뭐가 달라?

A.
Spring Boot Domain Rules는 일반 Backend 구조이고 Security Advanced는 인증, 인가, Filter Chain, JWT, OAuth2, 보안 예외 처리를 다룬다.

Q. Spring Security에서 가장 중요한 기준은 뭐야?

A.
Authentication과 Authorization 구분, Filter Chain 흐름, SecurityContext, JWT 검증 위치, 401/403 분리, 권한 검증 기준이다.

Q. JWT만 있으면 보안이 끝나는 거야?

A.
아니다. Token 검증, 만료, 재발급, 저장 위치, 탈취 대응, 권한 검증, HTTPS, CORS 정책까지 함께 설계해야 한다.

---

# 2. Scope

## 2.1 Included Scope

### [개념]

Security Advanced 문서는 Spring Boot Backend 보안 구현에 필요한 핵심 범위를 포함한다.

포함 범위:

- Spring Security Concept
- SecurityFilterChain
- Authentication
- Authorization
- SecurityContext
- Principal
- UserDetails / UserDetailsService
- PasswordEncoder
- Login Flow
- Logout Flow
- JWT Access Token
- JWT Refresh Token
- JWT Filter
- Token Reissue
- Stateless Session
- Role / Authority
- Method Security Basics
- CORS Security
- CSRF Basics
- Security Exception Handling
- AuthenticationEntryPoint
- AccessDeniedHandler
- OAuth2 Login Basics
- Protected API
- Public API
- Frontend Auth Integration
- Common Security Anti Patterns

---

### [핵심]

반드시 포함:

- 인증(Authentication)과 인가(Authorization)를 구분
- 인증 성공 후 SecurityContext에 Authentication 저장
- 권한 검증은 Backend에서 최종 수행
- Password는 반드시 PasswordEncoder로 단방향 해시
- JWT는 서명, 만료, 클레임을 검증
- Access Token과 Refresh Token 역할 분리
- Stateless API에서는 SessionCreationPolicy.STATELESS 고려
- 401과 403 응답을 분리
- CORS는 인증/인가 대체 수단이 아님
- CSRF 비활성화는 구조에 따라 판단
- Controller에서 userId를 RequestBody로 신뢰하지 않음
- 토큰과 비밀번호를 로그에 남기지 않음

---

### [실무]

Security 문서는 Java / Spring Boot / JPA / API Design 문서와 함께 사용된다.

실무 연결:

```text
Java
→ Spring Boot
→ JPA
→ Security Advanced
→ API Design
→ Testing
```

Security 구현 흐름:

```text
Requirement
→ Public / Protected API 분리
→ Authentication 방식 선택
→ SecurityFilterChain 구성
→ Login / Token 발급
→ JWT Filter 검증
→ SecurityContext 저장
→ Authorization 적용
→ Exception Handling
→ Test
```

---

### [FAQ]

Q. Security 문서에서 OAuth2를 깊게 다뤄?

A.
OAuth2 Login 흐름과 Spring Security 연동 기준은 포함하지만 Provider별 상세 설정은 별도 문서로 분리할 수 있다.

Q. JWT 저장 위치까지 다뤄?

A.
기본 보안 기준과 주의사항은 포함한다. Frontend 저장 전략은 Authentication Frontend Flow 문서와 함께 검토한다.

Q. HTTPS나 인프라 보안도 여기서 다뤄?

A.
Application Security 기준은 포함하지만 TLS, WAF, 운영 보안 심화는 Security Operations 또는 DevOps Expert 문서에서 다룬다.

---

## 2.2 Excluded Scope

### [개념]

Security Advanced 문서에서는 운영 보안과 고급 인증 프로토콜 심화를 제외한다.

제외 범위:

- OAuth2 Provider별 전체 설정 심화
- OpenID Connect 심화
- SAML
- LDAP
- WebAuthn / Passkey
- Zero Trust Architecture
- WAF / IDS / IPS
- Network Security 심화
- Cloud IAM 심화
- Kubernetes Secret 관리 심화
- Rate Limiting 고급 설계
- 보안 관제 / SIEM
- Penetration Testing 심화
- 암호학 수학 심화

---

### [핵심]

제외 이유:

- Foundation / Advanced Backend 범위 유지
- Agent Retrieval 혼선 방지
- DevOps / Security Operations / Frontend Auth 문서와 책임 분리
- Spring Security Application 구현 기준에 집중

---

### [실무]

고급 기술은 별도 Domain Rules로 분리한다.

예:

```text
Security Advanced
→ Authentication Frontend Flow
→ API Design
→ Security Operations
→ AI Guardrails Security
```

---

### [FAQ]

Q. 보안 운영까지 여기서 다뤄?

A.
아니다. 이 문서는 Spring Boot Application 보안 구현 중심이고 운영 보안은 DevOps Expert 영역으로 분리한다.

Q. OAuth2 Provider별 설정을 모두 포함해야 해?

A.
기초 흐름과 확장 기준만 포함하고 Google, Kakao, Naver 같은 Provider별 상세는 별도 문서로 분리할 수 있다.

---

# 3. Section Priority

## 3.1 Required Sections

### [개념]

Security Advanced RAG 문서는 모든 주요 Chunk에 아래 Section을 우선 포함한다.

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
- [실무]: 실제 보안 구현 기준
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

Q. Security 문서에도 FAQ가 필요해?

A.
필요하다. 인증, 인가, JWT, Filter Chain, 401/403, CORS 같은 질문과 RAG 검색 매칭을 강화한다.

Q. [면접] 섹션을 써도 돼?

A.
안 된다. 반드시 [FAQ] 섹션을 사용한다.

---

## 3.2 Recommended Sections

### [개념]

Security 문서에는 인증 흐름과 오류 분석을 위해 추가 Section을 포함할 수 있다.

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

- Authentication 설명 → [Flow]
- JWT 설명 → [Flow], [주의]
- SecurityFilterChain 설명 → [Flow]
- 401 / 403 설명 → [Comparison], [Troubleshooting]
- CORS / CSRF 설명 → [주의]
- Anti Pattern 설명 → [Troubleshooting], [Checklist]

---

### [실무]

예시:

```md
### [Flow]

Request
→ Security Filter
→ JWT 검증
→ Authentication 생성
→ SecurityContext 저장
→ Authorization
→ Controller
```

---

### [FAQ]

Q. Security 문서에 Flow가 중요한 이유는?

A.
Spring Security는 Filter Chain 흐름을 이해해야 인증 실패, 권한 실패, JWT 오류를 정확히 분석할 수 있다.

Q. Troubleshooting이 필요한 이유는?

A.
401, 403, CORS, JWT 만료, Filter 미동작, 권한 누락 문제가 자주 발생하기 때문이다.

---

# 4. Core Security Concept Rules

## 4.1 Authentication vs Authorization

### [개념]

Authentication은 사용자가 누구인지 확인하는 과정이다.

Authorization은 인증된 사용자가 특정 리소스나 기능에 접근할 권한이 있는지 확인하는 과정이다.

---

### [핵심]

비교:

| 구분 | Authentication      | Authorization   |
| ---- | ------------------- | --------------- |
| 의미 | 신원 확인           | 권한 확인       |
| 질문 | 누구인가?           | 접근 가능한가?  |
| 실패 | 401 Unauthorized    | 403 Forbidden   |
| 예   | 로그인, JWT 검증    | ROLE_ADMIN 확인 |
| 결과 | Authentication 객체 | Access Decision |

---

### [실무]

Flow:

```text
Login Request
→ ID / Password 확인
→ Authentication 성공
→ Token 발급
→ API Request with Token
→ Token 검증
→ Authorization 확인
→ Controller 접근
```

주의:

- 로그인 성공은 인증 성공
- 관리자 API 접근은 인가 검증
- Frontend에서 버튼 숨김은 UX일 뿐 보안 아님
- Backend에서 Role / Authority 검증 필수

---

### [FAQ]

Q. 인증과 인가는 뭐가 달라?

A.
인증은 사용자가 누구인지 확인하는 것이고 인가는 그 사용자가 특정 기능에 접근할 권한이 있는지 확인하는 것이다.

Q. 로그인했는데 403이 나올 수 있어?

A.
가능하다. 인증은 되었지만 해당 리소스에 접근할 권한이 없으면 403이 발생한다.

---

## 4.2 SecurityContext Rules

### [개념]

SecurityContext는 현재 요청에서 인증된 사용자 정보를 보관하는 Spring Security Context다.

Authentication 객체를 통해 Principal과 Authority를 확인할 수 있다.

---

### [핵심]

구성:

- SecurityContext
- Authentication
- Principal
- Credentials
- Authorities
- SecurityContextHolder

---

### [실무]

JWT 인증 성공 후 흐름:

```text
JWT 검증 성공
→ User 정보 조회 또는 Claim 사용
→ Authentication 객체 생성
→ SecurityContextHolder에 저장
→ Controller / Service에서 인증 정보 사용
```

예:

```java
Authentication authentication = SecurityContextHolder.getContext().getAuthentication();
```

권장:

- 인증 Filter에서 Authentication 저장
- Controller에서는 인증된 Principal 사용
- userId를 RequestBody로 신뢰하지 않음
- SecurityContext는 요청 단위로 이해
- 비동기 처리 시 Context 전달 주의

---

### [FAQ]

Q. SecurityContext는 뭐야?

A.
현재 요청의 인증 정보를 저장하는 Context이며 Authentication 객체를 통해 사용자와 권한 정보를 제공한다.

Q. Controller에서 userId를 직접 받아도 돼?

A.
인증 사용자 기준 작업이라면 RequestBody의 userId보다 SecurityContext 또는 Principal에서 가져오는 것이 안전하다.

---

## 4.3 Principal and Authority Rules

### [개념]

Principal은 인증된 사용자 주체를 의미한다.

Authority는 사용자가 가진 권한을 의미한다.

---

### [핵심]

포함 개념:

- Principal
- UserDetails
- CustomUserDetails
- GrantedAuthority
- ROLE_USER
- ROLE_ADMIN
- Authority Naming

---

### [실무]

권장:

- Principal에는 필요한 최소 사용자 정보만 포함
- Role naming 통일
- `ROLE_` prefix 정책 명확화
- Controller에서 `@AuthenticationPrincipal` 사용 가능
- 민감정보를 Principal에 과도하게 넣지 않음
- 권한은 Backend 기준으로 검증

예:

```java
@GetMapping("/me")
public ApiResponse<UserResponse> me(
        @AuthenticationPrincipal CustomUserPrincipal principal
) {
    return ApiResponse.success(userService.getMe(principal.userId()));
}
```

---

### [FAQ]

Q. Principal에는 뭘 넣어야 해?

A.
userId, email, role처럼 인증 사용자 식별과 권한 판단에 필요한 최소 정보를 넣는 것이 좋다.

Q. ROLE_USER와 USER는 달라?

A.
Spring Security에서 Role 처리 시 `ROLE_` prefix가 관여할 수 있으므로 프로젝트 권한 이름 규칙을 통일해야 한다.

---

# 5. SecurityFilterChain Rules

## 5.1 SecurityFilterChain Basics

### [개념]

SecurityFilterChain은 HTTP 요청이 Controller에 도달하기 전에 거치는 보안 Filter들의 체인이다.

인증, 인가, CORS, CSRF, 예외 처리 등이 Filter Chain에서 처리된다.

---

### [핵심]

핵심 요소:

- SecurityFilterChain
- HttpSecurity
- authorizeHttpRequests
- requestMatchers
- permitAll
- authenticated
- hasRole
- hasAuthority
- sessionManagement
- exceptionHandling
- addFilterBefore

---

### [실무]

기초 예:

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

권장:

- Public API와 Protected API 명확히 분리
- 더 구체적인 matcher를 먼저 배치
- Stateless JWT 구조면 STATELESS 설정
- JWT Filter 위치 명확화
- Security 예외 응답 Handler 등록
- 테스트로 접근 정책 검증

---

### [FAQ]

Q. SecurityFilterChain은 뭐야?

A.
요청이 Controller에 도달하기 전에 인증, 인가, CORS, CSRF, 예외 처리를 수행하는 보안 Filter 체인이다.

Q. requestMatchers 순서가 중요해?

A.
중요하다. 더 구체적인 경로를 먼저 선언하고 전체 규칙은 뒤에 두는 것이 좋다.

---

## 5.2 JWT Filter Position Rules

### [개념]

JWT Filter는 요청 Header의 Token을 검증하고 인증 객체를 SecurityContext에 저장하는 Custom Filter다.

---

### [핵심]

역할:

- Authorization Header 읽기
- Bearer Token 추출
- Token 서명 검증
- Token 만료 검증
- 사용자 정보 확인
- Authentication 생성
- SecurityContext 저장
- Filter Chain 계속 진행

---

### [실무]

Flow:

```text
Request
→ JWT Filter
→ Authorization Header 확인
→ Bearer Token 추출
→ Token 검증
→ Authentication 생성
→ SecurityContext 저장
→ 다음 Filter
→ Controller
```

Filter 등록 예:

```java
.addFilterBefore(jwtAuthenticationFilter, UsernamePasswordAuthenticationFilter.class)
```

주의:

- Public API는 Token이 없어도 통과 가능해야 함
- Token이 잘못된 경우 인증 실패 응답 기준 명확화
- 이미 SecurityContext에 인증이 있으면 중복 처리 주의
- Filter에서 비즈니스 로직 과다 수행 금지
- 예외 응답 형식은 EntryPoint와 조율

---

### [FAQ]

Q. JWT Filter는 어디에 넣어?

A.
보통 UsernamePasswordAuthenticationFilter 이전에 등록해 Controller 도달 전에 Token을 검증한다.

Q. JWT Filter에서 DB를 매번 조회해야 해?

A.
구조에 따라 다르다. Claim만 사용할 수도 있고 사용자 상태 확인을 위해 DB 조회를 할 수도 있다. 성능과 보안 요구사항을 함께 고려한다.

---

## 5.3 Public and Protected Endpoint Rules

### [개념]

Public Endpoint는 인증 없이 접근 가능한 API다.

Protected Endpoint는 인증 또는 특정 권한이 필요한 API다.

---

### [핵심]

Public 후보:

- 회원가입
- 로그인
- 토큰 재발급
- 공개 게시글 목록
- 공개 축제 목록
- Swagger 개발 환경
- Health Check

Protected 후보:

- 내 정보 조회
- 게시글 작성
- 댓글 작성
- 좋아요 / 찜
- 알림 조회
- 결제 내역
- 관리자 API

---

### [실무]

설계 기준:

```text
API 목록 작성
→ 인증 필요 여부 표시
→ 권한 필요 여부 표시
→ SecurityFilterChain matcher 작성
→ Controller / Method Security 보완
→ 테스트 작성
```

주의:

- 임시 permitAll을 운영에 남기지 않음
- Swagger 허용은 profile 기준 검토
- 관리자 API는 Role 검증 필수
- Frontend 라우팅 보호와 Backend API 보호를 혼동하지 않음

---

### [FAQ]

Q. 로그인 API도 인증이 필요해?

A.
아니다. 로그인 API는 인증 전 접근해야 하므로 permitAll 대상이다.

Q. Frontend에서 페이지 접근을 막으면 Backend API 보안은 필요 없어?

A.
아니다. Frontend 제한은 UX이고 실제 API 보호는 Backend Security에서 해야 한다.

---

# 6. Password and Login Rules

## 6.1 PasswordEncoder Rules

### [개념]

PasswordEncoder는 비밀번호를 단방향 해시로 저장하고 로그인 시 입력 비밀번호와 비교하는 도구다.

---

### [핵심]

기준:

- BCryptPasswordEncoder
- encode
- matches
- raw password
- encoded password
- salt
- one-way hash

---

### [실무]

Bean 예:

```java
@Bean
public PasswordEncoder passwordEncoder() {
    return new BCryptPasswordEncoder();
}
```

회원가입:

```java
String encodedPassword = passwordEncoder.encode(request.password());
```

로그인 검증:

```java
if (!passwordEncoder.matches(request.password(), user.getPassword())) {
    throw new BusinessException("INVALID_LOGIN", "아이디 또는 비밀번호가 올바르지 않습니다.");
}
```

주의:

- 비밀번호 평문 저장 금지
- 비밀번호 로그 출력 금지
- encode 결과끼리 문자열 비교 금지
- matches 사용
- 비밀번호 찾기 시 기존 비밀번호 반환 금지

---

### [FAQ]

Q. 비밀번호는 어떻게 저장해야 해?

A.
BCrypt 같은 PasswordEncoder로 단방향 해시 처리해 저장해야 한다.

Q. 로그인할 때 encode해서 DB 값과 비교하면 돼?

A.
BCrypt는 매번 다른 해시가 나올 수 있으므로 `matches(raw, encoded)`로 비교해야 한다.

---

## 6.2 Login Flow Rules

### [개념]

Login Flow는 사용자 자격 증명을 검증하고 인증 결과로 Token 또는 Session을 발급하는 과정이다.

---

### [핵심]

JWT Login Flow:

```text
Login Request
→ email / password 검증
→ User 조회
→ PasswordEncoder.matches
→ Access Token 생성
→ Refresh Token 생성
→ Refresh Token 저장
→ Login Response
```

---

### [실무]

권장:

- 로그인 실패 메시지는 과도하게 상세히 노출하지 않음
- 비밀번호 검증은 PasswordEncoder.matches 사용
- Refresh Token 저장 전략 명확화
- Access Token 만료 시간 짧게 설정
- Refresh Token 만료 시간 상대적으로 길게 설정
- 로그인 응답에 필요한 사용자 요약 정보 포함 가능
- 토큰을 로그에 남기지 않음

---

### [FAQ]

Q. 로그인 성공하면 뭘 반환해?

A.
JWT 구조에서는 Access Token, Refresh Token, 사용자 요약 정보를 반환할 수 있다. 프로젝트 보안 정책에 따라 달라진다.

Q. 로그인 실패 이유를 자세히 알려줘도 돼?

A.
보안상 이메일 존재 여부나 비밀번호 오류를 과도하게 구분하지 않는 것이 좋다.

---

## 6.3 Logout Rules

### [개념]

Logout은 사용자의 인증 상태를 종료하고 Refresh Token 또는 세션 정보를 무효화하는 과정이다.

---

### [핵심]

JWT Logout 고려사항:

- Refresh Token 삭제
- Refresh Token blacklist
- Access Token 만료 대기
- Client Token 제거
- SecurityContext clear
- Device별 로그아웃
- 전체 로그아웃

---

### [실무]

JWT Logout Flow:

```text
Logout Request
→ 인증 사용자 확인
→ 저장된 Refresh Token 삭제 또는 무효화
→ Client Token 제거 안내
→ 응답
```

주의:

- Stateless Access Token은 서버에서 즉시 무효화하기 어려움
- 짧은 Access Token 만료 시간으로 위험 완화
- Refresh Token은 서버 저장소에서 삭제 가능
- 로그아웃 후 사용자별 Cache / Store 초기화는 Frontend와 연동

---

### [FAQ]

Q. JWT 로그아웃은 서버에서 바로 Access Token을 무효화할 수 있어?

A.
기본 Stateless JWT는 어렵다. Blacklist를 쓰거나 Access Token 만료 시간을 짧게 두고 Refresh Token을 무효화하는 방식이 일반적이다.

Q. 로그아웃 시 Refresh Token은 삭제해야 해?

A.
서버에 저장한 Refresh Token이 있다면 삭제하거나 무효화하는 것이 좋다.

---

# 7. JWT Rules

## 7.1 JWT Concept Rules

### [개념]

JWT(JSON Web Token)는 JSON Claim을 서명해 전달하는 Token 형식이다.

인증된 사용자의 식별 정보와 권한 정보를 담아 API 요청에 사용할 수 있다.

---

### [핵심]

구성:

- Header
- Payload
- Signature
- Claims
- Subject
- Expiration
- Issued At
- Secret Key
- Bearer Token

---

### [실무]

JWT 요청 흐름:

```text
Client
→ Authorization: Bearer AccessToken
→ JWT Filter
→ Signature 검증
→ Expiration 검증
→ Claims 추출
→ Authentication 생성
→ SecurityContext 저장
```

주의:

- JWT Payload는 암호화가 아니라 인코딩
- 민감정보를 Claim에 넣지 않음
- 서명 Secret 관리 중요
- 만료 시간 설정 필수
- HTTPS 사용 권장
- Token 탈취 대응 전략 필요

---

### [FAQ]

Q. JWT Payload는 안전해?

A.
Payload는 쉽게 디코딩될 수 있으므로 비밀번호나 민감정보를 넣으면 안 된다.

Q. JWT는 서버 저장소가 전혀 필요 없어?

A.
Access Token은 Stateless하게 사용할 수 있지만 Refresh Token 관리, 로그아웃, 강제 만료가 필요하면 서버 저장소가 필요할 수 있다.

---

## 7.2 Access Token Rules

### [개념]

Access Token은 API 접근 시 인증 정보를 증명하기 위해 사용하는 짧은 수명의 Token이다.

---

### [핵심]

특징:

- API Authorization
- Short Expiration
- Bearer Token
- User ID Claim
- Role Claim
- Stateless Validation
- Refresh 필요

---

### [실무]

권장:

- 만료 시간을 짧게 설정
- 사용자 식별자와 권한 정도만 Claim에 포함
- 민감정보 Claim 금지
- Authorization Header 사용
- 만료 시 Refresh Token으로 재발급
- 탈취 시 피해 시간을 줄이는 방향 설계

---

### [FAQ]

Q. Access Token 만료 시간은 짧게 해야 해?

A.
일반적으로 짧게 설정해 탈취 시 피해 시간을 줄이고 Refresh Token으로 재발급하는 구조를 사용한다.

Q. Access Token에 사용자 정보를 많이 넣어도 돼?

A.
권장하지 않는다. userId, role처럼 최소 정보만 넣는 것이 좋다.

---

## 7.3 Refresh Token Rules

### [개념]

Refresh Token은 Access Token이 만료되었을 때 새 Access Token을 발급받기 위한 긴 수명의 Token이다.

---

### [핵심]

특징:

- Token Reissue
- Long Expiration
- Server-side Storage
- Rotation
- Logout Invalidation
- Theft Detection
- Device Session

---

### [실무]

Refresh Flow:

```text
Access Token 만료
→ Refresh Token 전송
→ Refresh Token 검증
→ 저장소 Token과 일치 확인
→ 새 Access Token 발급
→ 필요 시 Refresh Token Rotation
```

권장:

- Refresh Token은 서버 저장소에 저장 고려
- 사용자 / 기기 단위 관리 가능
- 재발급 시 기존 Token 교체 검토
- 로그아웃 시 삭제
- 탈취 의심 시 전체 무효화
- 만료 시간은 Access Token보다 길게 설정

주의:

- Refresh Token도 탈취되면 위험
- 저장 위치와 전송 방식 보안 검토
- DB / Redis 저장 전략 선택
- 재사용 탐지 전략 검토 가능

---

### [FAQ]

Q. Refresh Token은 왜 필요해?

A.
Access Token을 짧게 유지하면서 사용자가 자주 로그인하지 않도록 새 Access Token을 발급하기 위해 필요하다.

Q. Refresh Token도 DB에 저장해야 해?

A.
로그아웃, 강제 만료, 탈취 대응이 필요하면 DB나 Redis 같은 서버 저장소에 저장하는 것이 좋다.

---

## 7.4 Token Reissue Rules

### [개념]

Token Reissue는 유효한 Refresh Token을 바탕으로 새 Access Token을 발급하는 과정이다.

---

### [핵심]

검증 대상:

- Refresh Token 서명
- Refresh Token 만료
- 저장소 존재 여부
- 사용자 상태
- Token 일치 여부
- 재사용 여부
- Rotation 여부

---

### [실무]

Flow:

```text
Reissue Request
→ Refresh Token 추출
→ Token 유효성 검증
→ 저장소 Token 조회
→ 사용자 상태 확인
→ 새 Access Token 생성
→ Refresh Token Rotation 선택
→ Response
```

주의:

- 만료된 Refresh Token은 재로그인 요구
- 저장소 Token과 다르면 탈취 가능성 검토
- 정지 / 탈퇴 사용자 재발급 차단
- 재발급 API는 Public처럼 보이지만 Refresh Token 검증이 필요
- 응답 형식과 에러 코드를 명확히 분리

---

### [FAQ]

Q. Access Token이 만료되면 어떻게 해?

A.
Refresh Token이 유효하면 재발급 API로 새 Access Token을 받고, Refresh Token도 만료되었으면 재로그인해야 한다.

Q. Refresh Token이 틀리면 어떤 응답을 줘?

A.
인증 실패로 보고 401 계열 응답을 주는 것이 일반적이다. 상세 메시지는 보안상 과도하게 노출하지 않는다.

---

# 8. Authorization Rules

## 8.1 Role and Authority Rules

### [개념]

Role과 Authority는 인증된 사용자가 어떤 기능에 접근할 수 있는지 판단하는 권한 정보다.

---

### [핵심]

개념:

- ROLE_USER
- ROLE_ADMIN
- GrantedAuthority
- hasRole
- hasAuthority
- @PreAuthorize
- Method Security
- Resource Owner Check

---

### [실무]

권장:

- Role naming 통일
- 관리자 기능은 Backend에서 검증
- 리소스 소유자 검증은 Service에서 처리 가능
- 단순 Role 검증은 SecurityFilterChain 또는 Method Security 사용
- 복잡한 권한은 비즈니스 로직과 함께 검증
- Frontend 권한 표시는 UX일 뿐 최종 보안 아님

예:

```java
.requestMatchers("/api/admin/**").hasRole("ADMIN")
```

Method Security 예:

```java
@PreAuthorize("hasRole('ADMIN')")
public void deleteUser(Long userId) {
}
```

---

### [FAQ]

Q. hasRole과 hasAuthority는 뭐가 달라?

A.
hasRole은 일반적으로 ROLE\_ prefix 처리가 관여하고 hasAuthority는 권한 문자열을 직접 비교한다. 프로젝트 규칙을 통일해야 한다.

Q. 내 게시글 수정 권한은 Role로만 보면 돼?

A.
아니다. 사용자가 해당 게시글의 소유자인지 Service에서 Resource Owner Check를 해야 한다.

---

## 8.2 Resource Owner Check Rules

### [개념]

Resource Owner Check는 인증된 사용자가 특정 리소스의 소유자인지 확인하는 인가 검증이다.

---

### [핵심]

사용 상황:

- 내 게시글 수정 / 삭제
- 내 댓글 삭제
- 내 정보 수정
- 내 알림 조회
- 내 결제 내역 조회
- 내 찜 목록 조회

---

### [실무]

예:

```java
@Transactional
public void updatePost(Long postId, Long currentUserId, PostUpdateRequest request) {
    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException("POST_NOT_FOUND", "게시글을 찾을 수 없습니다."));

    if (!post.isOwner(currentUserId)) {
        throw new AccessDeniedException("권한이 없습니다.");
    }

    post.update(request.title(), request.content());
}
```

권장:

- currentUserId는 SecurityContext에서 가져옴
- RequestBody userId 신뢰 금지
- Service에서 리소스 소유자 검증
- 관리자 예외 정책 명확화
- 403 응답으로 처리

---

### [FAQ]

Q. userId를 요청으로 받아서 본인 확인하면 안 돼?

A.
안 된다. 사용자가 조작할 수 있으므로 인증 Principal의 userId를 기준으로 검증해야 한다.

Q. 본인 리소스 검증은 어디서 해?

A.
리소스를 조회하고 비즈니스 규칙을 판단하는 Service에서 처리하는 것이 일반적이다.

---

# 9. CORS and CSRF Rules

## 9.1 CORS Rules

### [개념]

CORS는 브라우저가 다른 Origin으로 API 요청을 보낼 때 서버 허용 여부를 확인하는 보안 정책이다.

---

### [핵심]

구성:

- allowedOrigins
- allowedMethods
- allowedHeaders
- allowCredentials
- exposedHeaders
- preflight
- OPTIONS

---

### [실무]

주의:

- CORS는 브라우저 정책
- 서버 인증/인가를 대체하지 않음
- Frontend origin 정확히 등록
- credentials 사용 시 `*` Origin 주의
- Spring Security 사용 시 SecurityFilterChain CORS 설정 확인
- 개발 / 운영 Origin 분리
- Authorization Header 허용 필요 가능

Flow:

```text
Browser
→ Preflight OPTIONS
→ Server CORS Policy 확인
→ 허용 시 실제 요청
```

---

### [FAQ]

Q. CORS 에러는 인증 실패야?

A.
아니다. 브라우저 Origin 정책 문제다. 인증 실패와 CORS 설정 문제를 구분해야 한다.

Q. CORS를 모두 허용하면 안전해?

A.
아니다. 개발 중 임시 허용은 가능하지만 운영에서는 허용 Origin, Method, Header를 제한해야 한다.

---

## 9.2 CSRF Rules

### [개념]

CSRF는 사용자가 인증된 상태를 악용해 원치 않는 요청을 보내게 하는 공격이다.

---

### [핵심]

관련 개념:

- Cookie-based Session
- CSRF Token
- Stateless API
- JWT Header
- Browser Auto Credential
- SameSite Cookie

---

### [실무]

판단 기준:

```text
Session Cookie 기반 인증인가?
→ CSRF 보호 필요

Authorization Header 기반 Stateless JWT인가?
→ CSRF 위험 상대적으로 낮음
→ csrf disable 검토 가능
```

주의:

- CSRF disable을 무조건 적용하지 않음
- Cookie에 Token 저장 시 CSRF / XSS 함께 검토
- SameSite, HttpOnly, Secure 속성 고려
- 인증 방식에 따라 판단
- 보안 요구사항이 높으면 별도 위협 모델 검토

---

### [FAQ]

Q. JWT를 쓰면 CSRF를 꺼도 돼?

A.
Authorization Header 기반 Stateless JWT 구조라면 CSRF 비활성화를 검토할 수 있다. 단, Cookie 저장 방식이면 다시 검토해야 한다.

Q. CSRF와 CORS는 같은 거야?

A.
아니다. CORS는 Origin 접근 정책이고 CSRF는 사용자의 인증 상태를 악용한 요청 위조 공격이다.

---

# 10. Security Exception Handling Rules

## 10.1 AuthenticationEntryPoint Rules

### [개념]

AuthenticationEntryPoint는 인증되지 않은 사용자가 보호된 리소스에 접근할 때 401 응답을 처리하는 진입점이다.

---

### [핵심]

사용 상황:

- Token 없음
- Token 만료
- Token 형식 오류
- Token 서명 오류
- 인증 객체 없음
- Anonymous 접근 차단

---

### [실무]

권장 응답:

```text
HTTP 401 Unauthorized
errorCode: UNAUTHORIZED
message: 인증이 필요합니다.
```

주의:

- Token 만료와 위조를 과도하게 상세 노출하지 않음
- JSON 응답 형식 통일
- Filter에서 발생한 인증 예외와 연결
- Frontend가 재로그인 / 재발급 판단 가능하게 errorCode 설계

---

### [FAQ]

Q. 401은 언제 발생해?

A.
인증 정보가 없거나 유효하지 않아 사용자가 누구인지 확인할 수 없을 때 발생한다.

Q. JWT 만료는 401이야 403이야?

A.
일반적으로 인증 실패이므로 401로 처리한다.

---

## 10.2 AccessDeniedHandler Rules

### [개념]

AccessDeniedHandler는 인증은 되었지만 권한이 부족한 사용자의 접근을 403 응답으로 처리한다.

---

### [핵심]

사용 상황:

- Role 부족
- Authority 부족
- Resource Owner 아님
- 관리자 API 접근 실패
- Method Security 실패

---

### [실무]

권장 응답:

```text
HTTP 403 Forbidden
errorCode: ACCESS_DENIED
message: 접근 권한이 없습니다.
```

주의:

- 인증 실패와 권한 실패를 구분
- Resource 존재 여부를 과도하게 노출하지 않음
- 관리자 권한 실패는 403
- Frontend는 403 시 권한 없음 화면 또는 알림 처리

---

### [FAQ]

Q. 403은 언제 발생해?

A.
로그인은 되었지만 해당 리소스나 기능에 접근할 권한이 없을 때 발생한다.

Q. 401과 403 차이는?

A.
401은 인증 실패이고 403은 인증은 되었지만 권한이 부족한 상태다.

---

## 10.3 Security Error Response Rules

### [개념]

Security Error Response는 인증 / 인가 실패 응답을 API 전체 에러 응답 형식과 맞추는 규칙이다.

---

### [핵심]

필수 요소:

- status
- errorCode
- message
- timestamp
- path
- consistent JSON
- no sensitive detail

---

### [실무]

권장:

- GlobalExceptionHandler 응답 형식과 통일
- EntryPoint / AccessDeniedHandler에서 JSON 직접 작성 가능
- Filter 예외가 ControllerAdvice까지 가지 않을 수 있음을 이해
- Token 상세 오류는 로그와 응답 분리
- Frontend 처리 가능한 errorCode 제공

주의:

- Stack trace 응답 금지
- Secret / Token / 내부 예외 메시지 노출 금지
- 401 / 403 구분 유지

---

### [FAQ]

Q. Security 예외도 GlobalExceptionHandler에서 처리돼?

A.
항상 그렇지 않다. Filter Chain에서 발생한 인증/인가 예외는 EntryPoint나 AccessDeniedHandler에서 처리하는 경우가 많다.

Q. Security 에러 응답도 ApiResponse 형식으로 맞춰야 해?

A.
프로젝트 응답 규칙이 있다면 맞추는 것이 Frontend 처리에 좋다.

---

# 11. OAuth2 Login Rules

## 11.1 OAuth2 Login Concept Rules

### [개념]

OAuth2 Login은 외부 Provider를 통해 사용자 인증을 수행하고 Application에서 자체 사용자 계정과 연결하는 인증 방식이다.

---

### [핵심]

구성:

- Provider
- Authorization Code
- Redirect URI
- Client ID
- Client Secret
- Scope
- OAuth2User
- SuccessHandler
- User Mapping
- Token Issue

---

### [실무]

흐름:

```text
User OAuth2 Login Click
→ Provider Authorization Page
→ Authorization Code 발급
→ Backend Callback
→ Provider User Info 조회
→ Local User 조회 / 가입
→ Application Token 발급
→ Frontend Redirect
```

권장:

- Provider 사용자 식별자 저장
- email 신뢰 기준 검토
- 최초 로그인 시 회원 생성 정책 정의
- SuccessHandler에서 JWT 발급 가능
- Frontend Redirect URI 관리
- Provider별 응답 필드 Mapping 분리
- 탈퇴 / 연결 해제 정책 검토

---

### [FAQ]

Q. OAuth2 Login을 쓰면 JWT가 필요 없어?

A.
아니다. OAuth2로 외부 인증을 받은 뒤 자체 API 인증을 위해 JWT를 발급하는 구조를 사용할 수 있다.

Q. OAuth2 Provider email을 그대로 믿어도 돼?

A.
Provider와 email_verified 여부에 따라 다르다. 프로젝트 정책에 맞게 검증 기준을 정해야 한다.

---

## 11.2 OAuth2 User Mapping Rules

### [개념]

OAuth2 User Mapping은 Provider별 사용자 정보를 Application의 User Entity 또는 Principal로 변환하는 과정이다.

---

### [핵심]

Mapping 대상:

- provider
- providerId
- email
- nickname
- profileImage
- role
- linked user
- first login
- existing user

---

### [실무]

권장:

- provider + providerId 조합으로 사용자 식별
- Provider별 attribute 구조 분리
- 기존 이메일 계정과 연결 정책 명확화
- 신규 가입 기본 Role 설정
- 필수 정보 누락 시 처리 기준 정의
- Provider 응답 원본 전체 저장 지양

주의:

- Provider마다 attribute 구조가 다름
- email이 없거나 변경될 수 있음
- 동일 이메일 계정 병합 정책 필요
- OAuth2 로그인 사용자도 Backend 권한 검증 필요

---

### [FAQ]

Q. OAuth2 사용자는 어떻게 식별해?

A.
일반적으로 provider와 providerId 조합으로 식별한다. email만으로 식별하면 변경이나 중복 문제가 생길 수 있다.

Q. OAuth2 최초 로그인 시 회원가입을 자동으로 해도 돼?

A.
가능하다. 다만 필수 약관, 추가 정보 입력, 기본 권한 부여 정책을 정해야 한다.

---

# 12. Frontend Integration Rules

## 12.1 Frontend Auth Integration

### [개념]

Frontend Auth Integration은 Backend 인증 구조와 Frontend 로그인 상태 관리가 연동되는 방식이다.

---

### [핵심]

연동 요소:

- Login API
- Token Storage
- Authorization Header
- Axios Interceptor
- Token Reissue
- Logout
- Protected Route
- Auth State
- 401 Handling
- 403 Handling

---

### [실무]

Backend 기준 제공 사항:

- Login Response 형식
- Access Token 만료 에러 코드
- Refresh API 명세
- Logout API 명세
- 401 / 403 에러 형식
- 사용자 요약 정보 API
- 권한 정보 Role 명칭
- CORS 허용 Header

주의:

- Frontend Auth State는 UX용
- Backend가 최종 보안 기준
- Token 저장 위치는 XSS / CSRF 위험과 함께 검토
- 만료 처리 흐름을 명확히 문서화

---

### [FAQ]

Q. Frontend에서 로그인 상태만 확인하면 보안이 돼?

A.
아니다. Frontend 로그인 상태는 UX용이고 실제 API 접근 권한은 Backend에서 검증해야 한다.

Q. 401이 오면 Frontend는 뭘 해야 해?

A.
Access Token 만료라면 재발급을 시도하고, 재발급도 실패하면 로그아웃 또는 재로그인으로 처리한다.

---

# 13. Testing and Review Rules

## 13.1 Security Test Rules

### [개념]

Security Test는 인증 / 인가 정책이 의도대로 동작하는지 검증하는 과정이다.

---

### [핵심]

테스트 대상:

- Public API 접근
- Protected API Token 없음
- 유효 Token 접근
- 만료 Token 접근
- 위조 Token 접근
- 권한 부족 접근
- 관리자 API 접근
- 본인 리소스 접근
- 타인 리소스 접근
- Refresh Token 재발급
- Logout 후 재발급 차단

---

### [실무]

테스트 흐름:

```text
No Token
→ 401 확인

Invalid Token
→ 401 확인

Valid User Token
→ User API 200 확인

User Token to Admin API
→ 403 확인

Owner Resource
→ 200 확인

Other User Resource
→ 403 확인
```

권장:

- Swagger / Postman 수동 테스트 가능
- MockMvc / Spring Security Test로 자동화 가능
- JWT 위조는 문자열 일부 변경으로 테스트 가능
- 만료 Token은 짧은 만료 시간 또는 테스트용 Token 사용
- 응답 status와 errorCode 함께 검증

---

### [FAQ]

Q. 위조 JWT는 어떻게 테스트해?

A.
유효한 JWT 문자열 일부를 변경해 서명 검증 실패가 401로 처리되는지 확인할 수 있다.

Q. 권한 테스트에서 뭘 봐야 해?

A.
토큰 없음은 401, 권한 부족은 403, 정상 권한은 200 계열인지 확인한다.

---

# 14. Troubleshooting Rules

## 14.1 401 Unauthorized Troubleshooting

### [개념]

401 Unauthorized는 인증 정보가 없거나 유효하지 않아 인증에 실패한 상태다.

---

### [핵심]

원인:

- Authorization Header 없음
- Bearer prefix 누락
- Token 만료
- Token 서명 오류
- Secret Key 불일치
- JWT Filter 미등록
- SecurityContext 저장 실패
- Public / Protected matcher 오류

---

### [실무]

Debug Flow:

```text
요청 Header 확인
→ Authorization Bearer 형식 확인
→ JWT Filter 실행 여부 확인
→ Token 검증 결과 확인
→ SecurityContext 저장 확인
→ EntryPoint 응답 확인
```

---

### [FAQ]

Q. 로그인했는데 401이 나와?

A.
Authorization Header가 누락되었거나 Token이 만료 / 위조되었거나 JWT Filter가 인증 객체를 저장하지 못했을 수 있다.

Q. Bearer prefix가 꼭 필요해?

A.
프로젝트 JWT Filter가 Bearer 형식을 기준으로 파싱한다면 필요하다.

---

## 14.2 403 Forbidden Troubleshooting

### [개념]

403 Forbidden은 인증은 되었지만 접근 권한이 부족한 상태다.

---

### [핵심]

원인:

- Role 부족
- Authority 문자열 불일치
- ROLE\_ prefix 불일치
- 관리자 API 접근
- Resource Owner 불일치
- Method Security 실패
- AccessDeniedHandler 응답

---

### [실무]

Debug Flow:

```text
Authentication 존재 확인
→ Principal Role 확인
→ SecurityFilterChain 권한 규칙 확인
→ hasRole / hasAuthority 확인
→ Resource Owner Check 확인
→ AccessDeniedHandler 응답 확인
```

---

### [FAQ]

Q. 토큰은 정상인데 403이 나와?

A.
인증은 되었지만 Role / Authority가 부족하거나 해당 리소스의 소유자가 아닐 수 있다.

Q. ROLE\_ prefix 때문에 403이 날 수 있어?

A.
가능하다. hasRole과 hasAuthority 사용 방식과 저장된 권한 문자열을 맞춰야 한다.

---

## 14.3 CORS Troubleshooting

### [개념]

CORS Troubleshooting은 브라우저에서 다른 Origin API 요청이 차단되는 문제를 분석하는 과정이다.

---

### [핵심]

확인 대상:

- Frontend Origin
- Backend allowedOrigins
- allowedMethods
- allowedHeaders
- Authorization Header
- credentials
- OPTIONS preflight
- Security CORS 설정

---

### [실무]

Debug Flow:

```text
Browser Console 확인
→ Request Origin 확인
→ Preflight OPTIONS 확인
→ CORS Config 확인
→ SecurityFilterChain cors 설정 확인
→ Authorization Header 허용 확인
→ credentials 정책 확인
```

---

### [FAQ]

Q. Postman은 되는데 브라우저에서 CORS 에러가 나?

A.
CORS는 브라우저 보안 정책이므로 Postman에서는 발생하지 않을 수 있다.

Q. Authorization Header 때문에 CORS가 날 수 있어?

A.
가능하다. allowedHeaders에 Authorization이 허용되어 있는지 확인해야 한다.

---

## 14.4 JWT Reissue Troubleshooting

### [개념]

JWT Reissue Troubleshooting은 Access Token 재발급이 실패하는 문제를 분석하는 과정이다.

---

### [핵심]

원인:

- Refresh Token 만료
- Refresh Token 서명 오류
- 저장소 Token 없음
- 저장소 Token 불일치
- 사용자 탈퇴 / 정지
- Token Rotation 처리 오류
- Cookie / Header 전달 누락

---

### [실무]

Debug Flow:

```text
Refresh Token 전달 확인
→ Refresh Token 검증
→ 저장소 조회
→ Token 일치 확인
→ 사용자 상태 확인
→ 새 Token 발급 확인
→ 응답 저장 확인
```

---

### [FAQ]

Q. 재발급이 계속 실패하면 뭘 확인해?

A.
Refresh Token 전달 방식, 만료 여부, 저장소 일치 여부, 사용자 상태, Rotation 로직을 확인한다.

---

# 15. Comparison Rules

## 15.1 Required Comparisons

### [개념]

Security 문서는 헷갈리는 보안 개념을 비교해서 작성한다.

---

### [핵심]

필수 비교 대상:

- Authentication vs Authorization
- 401 vs 403
- Access Token vs Refresh Token
- Session vs JWT
- Stateful vs Stateless
- hasRole vs hasAuthority
- CORS vs CSRF
- AuthenticationEntryPoint vs AccessDeniedHandler
- Filter vs Interceptor
- Principal vs User Entity
- UserDetails vs OAuth2User
- Public API vs Protected API
- Token Expired vs Token Invalid
- Frontend Auth State vs Backend Security

---

### [실무]

예시:

| 비교        | 401 Unauthorized         | 403 Forbidden       |
| ----------- | ------------------------ | ------------------- |
| 의미        | 인증 실패                | 권한 부족           |
| 사용자 상태 | 누구인지 확인 불가       | 로그인은 됨         |
| 예          | Token 없음 / 만료        | Role 부족           |
| 처리        | 재로그인 / 재발급        | 권한 없음 안내      |
| Handler     | AuthenticationEntryPoint | AccessDeniedHandler |

---

### [FAQ]

Q. Security Comparison은 왜 필요해?

A.
Spring Security는 인증과 인가, 401과 403, CORS와 CSRF처럼 비슷하지만 다른 개념이 많기 때문이다.

Q. 가장 중요한 비교는 뭐야?

A.
Authentication vs Authorization, 401 vs 403, Access Token vs Refresh Token, CORS vs CSRF다.

---

# 16. Checklist Rules

## 16.1 Security Checklist

### [개념]

Security 문서 검수 시 인증 / 인가 / Token / 예외 처리 체크리스트를 사용한다.

---

### [핵심]

Checklist:

```md
- [ ] Authentication / Authorization 차이가 포함되었는가?
- [ ] SecurityFilterChain 흐름이 포함되었는가?
- [ ] Public / Protected API 분리 기준이 포함되었는가?
- [ ] PasswordEncoder 기준이 포함되었는가?
- [ ] Login Flow가 포함되었는가?
- [ ] Logout Flow가 포함되었는가?
- [ ] JWT 구조와 검증 기준이 포함되었는가?
- [ ] Access Token / Refresh Token 차이가 포함되었는가?
- [ ] Token Reissue 기준이 포함되었는가?
- [ ] JWT Filter 위치 기준이 포함되었는가?
- [ ] SecurityContext 저장 기준이 포함되었는가?
- [ ] Principal / Authority 기준이 포함되었는가?
- [ ] Role / Resource Owner Check 기준이 포함되었는가?
- [ ] CORS 기준이 포함되었는가?
- [ ] CSRF 판단 기준이 포함되었는가?
- [ ] 401 / 403 차이가 포함되었는가?
- [ ] AuthenticationEntryPoint 기준이 포함되었는가?
- [ ] AccessDeniedHandler 기준이 포함되었는가?
- [ ] OAuth2 Login 흐름이 포함되었는가?
- [ ] Frontend Auth 연동 기준이 포함되었는가?
- [ ] Security Test 기준이 포함되었는가?
- [ ] Troubleshooting이 포함되었는가?
- [ ] Common Mistakes가 포함되었는가?
- [ ] FAQ가 충분한가?
- [ ] Retrieval Queries가 포함되었는가?
```

---

### [실무]

검수 흐름:

```text
Draft
→ Auth Concept Check
→ Filter Chain Check
→ JWT Check
→ Authorization Check
→ Exception Response Check
→ CORS / CSRF Check
→ OAuth2 Check
→ Test Scenario Check
→ Troubleshooting Check
→ FAQ Check
→ Retrieval Query Check
→ Final Review
```

---

### [FAQ]

Q. Security 문서 검수에서 가장 중요한 것은?

A.
인증/인가 구분, JWT 검증 흐름, SecurityContext 저장, 401/403 분리, 권한 검증, Token 보안 주의사항이다.

---

# 17. Retrieval Optimization Rules

## 17.1 Keyword Rules

### [개념]

Security 문서는 검색 매칭을 위해 핵심 키워드를 반복 허용한다.

---

### [핵심]

강조 키워드:

- Spring Security
- SecurityFilterChain
- Authentication
- Authorization
- SecurityContext
- Principal
- UserDetails
- GrantedAuthority
- ROLE_USER
- ROLE_ADMIN
- PasswordEncoder
- BCryptPasswordEncoder
- Login
- Logout
- JWT
- Access Token
- Refresh Token
- Bearer Token
- JWT Filter
- Token Reissue
- Stateless
- SessionCreationPolicy.STATELESS
- CORS
- CSRF
- 401 Unauthorized
- 403 Forbidden
- AuthenticationEntryPoint
- AccessDeniedHandler
- OAuth2 Login
- OAuth2User
- SuccessHandler
- Resource Owner Check
- hasRole
- hasAuthority
- @PreAuthorize
- Security Anti Pattern

---

### [실무]

FAQ와 Retrieval Queries에는 실제 사용자가 질문할 표현을 포함한다.

예:

- 인증과 인가는 뭐가 달라?
- SecurityFilterChain은 뭐야?
- JWT Filter는 어디에 넣어?
- Access Token과 Refresh Token 차이는?
- Refresh Token은 DB에 저장해야 해?
- 401과 403 차이는?
- CORS 에러는 인증 실패야?
- CSRF는 꺼도 돼?
- PasswordEncoder는 왜 써?
- 로그인 성공하면 뭘 반환해?
- userId를 RequestBody로 받아도 돼?
- ROLE\_ prefix 때문에 403이 나?
- OAuth2 Login 후 JWT를 발급해도 돼?
- 위조 JWT는 어떻게 테스트해?

---

### [FAQ]

Q. 키워드 반복은 중복이야?

A.
불필요한 장문 반복은 금지지만 Retrieval 최적화를 위한 핵심 키워드 반복은 허용된다.

Q. Security FAQ 질문은 어떤 스타일이 좋아?

A.
실제 개발 중 자주 묻는 JWT, 401/403, CORS, Filter Chain, 권한 문제 질문 형태가 좋다.

---

# 18. Version Rules

## 18.1 Modern Spring Security 기준

### [개념]

Security 문서는 Modern Spring Boot + Spring Security 기준으로 작성한다.

---

### [핵심]

기준:

- Spring Boot 3.x
- Spring Security 6.x
- Java 17+
- SecurityFilterChain Bean 기반 설정
- Lambda DSL
- Jakarta Namespace
- Stateless JWT API
- PasswordEncoder
- SecurityContext
- AuthenticationEntryPoint
- AccessDeniedHandler
- Method Security
- OAuth2 Login 연계 가능성

Legacy 제외:

- WebSecurityConfigurerAdapter 중심 신규 문서
- XML Security 설정 중심
- 비밀번호 평문 저장
- Controller에서 인증 직접 구현
- RequestBody userId 신뢰
- 모든 API permitAll
- Role 검증을 Frontend에만 의존
- Token을 로그에 출력
- JWT Payload에 민감정보 저장
- CORS를 인증 대체로 사용

---

### [실무]

실무 기준:

```text
Modern Spring Security
→ SecurityFilterChain
→ Stateless JWT
→ PasswordEncoder
→ JWT Filter
→ SecurityContext
→ Authorization
→ 401 / 403 Handler
→ Test
```

---

### [FAQ]

Q. WebSecurityConfigurerAdapter를 써야 해?

A.
신규 Spring Security 6 기준에서는 SecurityFilterChain Bean 기반 설정을 우선한다.

Q. 모든 API를 permitAll로 열고 Service에서 검사하면 돼?

A.
권장하지 않는다. SecurityFilterChain에서 기본 접근 제어를 하고 Service에서 리소스 소유자 같은 세부 권한을 보완하는 것이 좋다.

---

# 19. Common Mistakes

## 19.1 Security Common Mistakes

### [개념]

Security 문서는 자주 발생하는 인증 / 인가 / JWT / CORS 실수를 명확히 포함해야 한다.

---

### [핵심]

자주 발생:

- Authentication과 Authorization 혼동
- 401과 403 혼동
- 모든 API를 permitAll로 둠
- Frontend 권한 체크만 믿음
- RequestBody userId를 신뢰
- 비밀번호 평문 저장
- PasswordEncoder.matches 미사용
- JWT Payload에 민감정보 저장
- Token 만료 검증 누락
- Refresh Token 저장 / 무효화 전략 없음
- 로그에 Token 출력
- ROLE\_ prefix 불일치
- hasRole / hasAuthority 혼동
- JWT Filter 미등록 또는 위치 오류
- SecurityContext 저장 누락
- CORS를 인증 문제로 오해
- CORS 전체 허용을 운영에 남김
- CSRF disable을 구조 검토 없이 적용
- EntryPoint / AccessDeniedHandler 미구분
- OAuth2 사용자 식별을 email만으로 처리
- 관리자 API 권한 검증 누락

---

### [실무]

문서 작성 시 Common Mistakes는 Troubleshooting과 연결한다.

예:

```text
문제: 로그인 후 관리자 API 호출 시 403
원인: Token의 권한은 ADMIN인데 hasRole('ADMIN')과 저장 권한 문자열 prefix가 불일치
해결: ROLE_ADMIN / hasRole / hasAuthority 규칙을 통일
```

예:

```text
문제: Postman은 성공하지만 브라우저에서 API 실패
원인: CORS 설정에서 Frontend Origin 또는 Authorization Header 미허용
해결: CORS allowedOrigins / allowedHeaders / Security cors 설정 확인
```

---

### [FAQ]

Q. Spring Security 초보가 가장 많이 하는 실수는?

A.
401/403을 혼동하거나 JWT Filter, SecurityContext 저장, Role prefix, CORS 설정을 제대로 구분하지 못하는 실수가 많다.

Q. Security 문제는 어떻게 찾는 게 좋아?

A.
요청 Header, Token 검증, Filter 실행, SecurityContext 저장, 권한 문자열, 401/403 Handler, CORS 순서로 확인한다.

---

# 20. Final Goal

## 20.1 Domain Final Goal

### [개념]

Security Advanced RAG 문서는 Backend Agent가 Spring Security 설정을 단순히 작성하는 것이 아니라 인증 / 인가 / JWT / 예외 처리 / Frontend 연동까지 고려해 안전한 Backend Security 구조를 설계하도록 지원해야 한다.

---

### [핵심]

최종 목표:

- Authentication / Authorization 구분
- SecurityFilterChain 설계
- Public / Protected API 분리
- PasswordEncoder 적용
- Login Flow 설계
- Logout Flow 설계
- JWT 구조 이해
- Access Token / Refresh Token 분리
- Token Reissue 설계
- JWT Filter 위치 결정
- SecurityContext 저장
- Principal / Authority 설계
- Role / Resource Owner Check 적용
- CORS 정책 판단
- CSRF 정책 판단
- 401 / 403 응답 분리
- AuthenticationEntryPoint 구성
- AccessDeniedHandler 구성
- OAuth2 Login 흐름 설계
- Frontend Auth 연동 기준 제공
- Security Test Scenario 구성
- Security Anti Pattern 탐지

---

### [실무]

Agent 수행 가능 작업:

```text
User Security Request
→ Identify Auth Requirement
→ Separate Public / Protected API
→ Configure SecurityFilterChain
→ Design Login / Token Flow
→ Add JWT Filter
→ Store Authentication in SecurityContext
→ Apply Authorization
→ Handle 401 / 403
→ Configure CORS / CSRF
→ Review Token Risk
→ Security Output
```

---

### [FAQ]

Q. Security Advanced 문서의 최종 목적은 뭐야?

A.
Backend Agent가 Spring Security, JWT, 권한 검증, 예외 처리, CORS, OAuth2를 기준에 맞게 설계하고 보안 Anti Pattern을 탐지하게 만드는 것이다.

Q. 이 문서 다음에는 어떤 Domain Rules가 이어져야 해?

A.
QueryDSL Practical, Testing, API Design, Authentication Frontend Flow Domain Rules와 이어지는 것이 좋다.

---

# Retrieval Queries

### [FAQ]

Q. Security Advanced Domain Rules는 왜 필요해?
A. Backend Agent가 Spring Security 인증, 인가, JWT, OAuth2, 예외 처리, 권한 검증을 일관되게 설계해야 하기 때문이다.

Q. 인증과 인가는 뭐가 달라?
A. 인증은 사용자가 누구인지 확인하는 것이고 인가는 그 사용자가 특정 기능에 접근할 권한이 있는지 확인하는 것이다.

Q. 로그인했는데 403이 나올 수 있어?
A. 가능하다. 인증은 되었지만 해당 리소스에 접근할 권한이 없으면 403이 발생한다.

Q. SecurityContext는 뭐야?
A. 현재 요청의 인증 정보를 저장하는 Context이며 Authentication 객체를 통해 사용자와 권한 정보를 제공한다.

Q. Principal에는 뭘 넣어야 해?
A. userId, email, role처럼 인증 사용자 식별과 권한 판단에 필요한 최소 정보를 넣는 것이 좋다.

Q. Controller에서 userId를 직접 받아도 돼?
A. 인증 사용자 기준 작업이라면 RequestBody의 userId보다 SecurityContext 또는 Principal에서 가져오는 것이 안전하다.

Q. ROLE*USER와 USER는 달라?
A. Spring Security에서 Role 처리 시 ROLE* prefix가 관여할 수 있으므로 프로젝트 권한 이름 규칙을 통일해야 한다.

Q. SecurityFilterChain은 뭐야?
A. 요청이 Controller에 도달하기 전에 인증, 인가, CORS, CSRF, 예외 처리를 수행하는 보안 Filter 체인이다.

Q. requestMatchers 순서가 중요해?
A. 중요하다. 더 구체적인 경로를 먼저 선언하고 전체 규칙은 뒤에 두는 것이 좋다.

Q. JWT Filter는 어디에 넣어?
A. 보통 UsernamePasswordAuthenticationFilter 이전에 등록해 Controller 도달 전에 Token을 검증한다.

Q. JWT Filter는 무슨 일을 해?
A. Authorization Header에서 Bearer Token을 추출하고 검증한 뒤 Authentication을 만들어 SecurityContext에 저장한다.

Q. JWT Filter에서 DB를 매번 조회해야 해?
A. 구조에 따라 다르다. Claim만 사용할 수도 있고 사용자 상태 확인을 위해 DB 조회를 할 수도 있다. 성능과 보안 요구사항을 함께 고려한다.

Q. 로그인 API도 인증이 필요해?
A. 아니다. 로그인 API는 인증 전 접근해야 하므로 permitAll 대상이다.

Q. Frontend에서 페이지 접근을 막으면 Backend API 보안은 필요 없어?
A. 아니다. Frontend 제한은 UX이고 실제 API 보호는 Backend Security에서 해야 한다.

Q. 비밀번호는 어떻게 저장해야 해?
A. BCrypt 같은 PasswordEncoder로 단방향 해시 처리해 저장해야 한다.

Q. 로그인할 때 encode해서 DB 값과 비교하면 돼?
A. BCrypt는 매번 다른 해시가 나올 수 있으므로 matches(raw, encoded)로 비교해야 한다.

Q. 로그인 성공하면 뭘 반환해?
A. JWT 구조에서는 Access Token, Refresh Token, 사용자 요약 정보를 반환할 수 있다. 프로젝트 보안 정책에 따라 달라진다.

Q. 로그인 실패 이유를 자세히 알려줘도 돼?
A. 보안상 이메일 존재 여부나 비밀번호 오류를 과도하게 구분하지 않는 것이 좋다.

Q. JWT 로그아웃은 서버에서 바로 Access Token을 무효화할 수 있어?
A. 기본 Stateless JWT는 어렵다. Blacklist를 쓰거나 Access Token 만료 시간을 짧게 두고 Refresh Token을 무효화하는 방식이 일반적이다.

Q. 로그아웃 시 Refresh Token은 삭제해야 해?
A. 서버에 저장한 Refresh Token이 있다면 삭제하거나 무효화하는 것이 좋다.

Q. JWT Payload는 안전해?
A. Payload는 쉽게 디코딩될 수 있으므로 비밀번호나 민감정보를 넣으면 안 된다.

Q. JWT는 서버 저장소가 전혀 필요 없어?
A. Access Token은 Stateless하게 사용할 수 있지만 Refresh Token 관리, 로그아웃, 강제 만료가 필요하면 서버 저장소가 필요할 수 있다.

Q. Access Token 만료 시간은 짧게 해야 해?
A. 일반적으로 짧게 설정해 탈취 시 피해 시간을 줄이고 Refresh Token으로 재발급하는 구조를 사용한다.

Q. Access Token에 사용자 정보를 많이 넣어도 돼?
A. 권장하지 않는다. userId, role처럼 최소 정보만 넣는 것이 좋다.

Q. Refresh Token은 왜 필요해?
A. Access Token을 짧게 유지하면서 사용자가 자주 로그인하지 않도록 새 Access Token을 발급하기 위해 필요하다.

Q. Refresh Token도 DB에 저장해야 해?
A. 로그아웃, 강제 만료, 탈취 대응이 필요하면 DB나 Redis 같은 서버 저장소에 저장하는 것이 좋다.

Q. Access Token이 만료되면 어떻게 해?
A. Refresh Token이 유효하면 재발급 API로 새 Access Token을 받고, Refresh Token도 만료되었으면 재로그인해야 한다.

Q. Refresh Token이 틀리면 어떤 응답을 줘?
A. 인증 실패로 보고 401 계열 응답을 주는 것이 일반적이다. 상세 메시지는 보안상 과도하게 노출하지 않는다.

Q. hasRole과 hasAuthority는 뭐가 달라?
A. hasRole은 일반적으로 ROLE\_ prefix 처리가 관여하고 hasAuthority는 권한 문자열을 직접 비교한다. 프로젝트 규칙을 통일해야 한다.

Q. 내 게시글 수정 권한은 Role로만 보면 돼?
A. 아니다. 사용자가 해당 게시글의 소유자인지 Service에서 Resource Owner Check를 해야 한다.

Q. userId를 요청으로 받아서 본인 확인하면 안 돼?
A. 안 된다. 사용자가 조작할 수 있으므로 인증 Principal의 userId를 기준으로 검증해야 한다.

Q. 본인 리소스 검증은 어디서 해?
A. 리소스를 조회하고 비즈니스 규칙을 판단하는 Service에서 처리하는 것이 일반적이다.

Q. CORS 에러는 인증 실패야?
A. 아니다. 브라우저 Origin 정책 문제다. 인증 실패와 CORS 설정 문제를 구분해야 한다.

Q. CORS를 모두 허용하면 안전해?
A. 아니다. 개발 중 임시 허용은 가능하지만 운영에서는 허용 Origin, Method, Header를 제한해야 한다.

Q. JWT를 쓰면 CSRF를 꺼도 돼?
A. Authorization Header 기반 Stateless JWT 구조라면 CSRF 비활성화를 검토할 수 있다. 단, Cookie 저장 방식이면 다시 검토해야 한다.

Q. CSRF와 CORS는 같은 거야?
A. 아니다. CORS는 Origin 접근 정책이고 CSRF는 사용자의 인증 상태를 악용한 요청 위조 공격이다.

Q. 401은 언제 발생해?
A. 인증 정보가 없거나 유효하지 않아 사용자가 누구인지 확인할 수 없을 때 발생한다.

Q. JWT 만료는 401이야 403이야?
A. 일반적으로 인증 실패이므로 401로 처리한다.

Q. 403은 언제 발생해?
A. 로그인은 되었지만 해당 리소스나 기능에 접근할 권한이 없을 때 발생한다.

Q. 401과 403 차이는?
A. 401은 인증 실패이고 403은 인증은 되었지만 권한이 부족한 상태다.

Q. Security 예외도 GlobalExceptionHandler에서 처리돼?
A. 항상 그렇지 않다. Filter Chain에서 발생한 인증/인가 예외는 EntryPoint나 AccessDeniedHandler에서 처리하는 경우가 많다.

Q. Security 에러 응답도 ApiResponse 형식으로 맞춰야 해?
A. 프로젝트 응답 규칙이 있다면 맞추는 것이 Frontend 처리에 좋다.

Q. OAuth2 Login을 쓰면 JWT가 필요 없어?
A. 아니다. OAuth2로 외부 인증을 받은 뒤 자체 API 인증을 위해 JWT를 발급하는 구조를 사용할 수 있다.

Q. OAuth2 Provider email을 그대로 믿어도 돼?
A. Provider와 email_verified 여부에 따라 다르다. 프로젝트 정책에 맞게 검증 기준을 정해야 한다.

Q. OAuth2 사용자는 어떻게 식별해?
A. 일반적으로 provider와 providerId 조합으로 식별한다. email만으로 식별하면 변경이나 중복 문제가 생길 수 있다.

Q. OAuth2 최초 로그인 시 회원가입을 자동으로 해도 돼?
A. 가능하다. 다만 필수 약관, 추가 정보 입력, 기본 권한 부여 정책을 정해야 한다.

Q. Frontend에서 로그인 상태만 확인하면 보안이 돼?
A. 아니다. Frontend 로그인 상태는 UX용이고 실제 API 접근 권한은 Backend에서 검증해야 한다.

Q. 401이 오면 Frontend는 뭘 해야 해?
A. Access Token 만료라면 재발급을 시도하고, 재발급도 실패하면 로그아웃 또는 재로그인으로 처리한다.

Q. 위조 JWT는 어떻게 테스트해?
A. 유효한 JWT 문자열 일부를 변경해 서명 검증 실패가 401로 처리되는지 확인할 수 있다.

Q. 권한 테스트에서 뭘 봐야 해?
A. 토큰 없음은 401, 권한 부족은 403, 정상 권한은 200 계열인지 확인한다.

Q. 로그인했는데 401이 나와?
A. Authorization Header가 누락되었거나 Token이 만료 / 위조되었거나 JWT Filter가 인증 객체를 저장하지 못했을 수 있다.

Q. Bearer prefix가 꼭 필요해?
A. 프로젝트 JWT Filter가 Bearer 형식을 기준으로 파싱한다면 필요하다.

Q. 토큰은 정상인데 403이 나와?
A. 인증은 되었지만 Role / Authority가 부족하거나 해당 리소스의 소유자가 아닐 수 있다.

Q. ROLE\_ prefix 때문에 403이 날 수 있어?
A. 가능하다. hasRole과 hasAuthority 사용 방식과 저장된 권한 문자열을 맞춰야 한다.

Q. Postman은 되는데 브라우저에서 CORS 에러가 나?
A. CORS는 브라우저 보안 정책이므로 Postman에서는 발생하지 않을 수 있다.

Q. Authorization Header 때문에 CORS가 날 수 있어?
A. 가능하다. allowedHeaders에 Authorization이 허용되어 있는지 확인해야 한다.

Q. 재발급이 계속 실패하면 뭘 확인해?
A. Refresh Token 전달 방식, 만료 여부, 저장소 일치 여부, 사용자 상태, Rotation 로직을 확인한다.

Q. WebSecurityConfigurerAdapter를 써야 해?
A. 신규 Spring Security 6 기준에서는 SecurityFilterChain Bean 기반 설정을 우선한다.

Q. 모든 API를 permitAll로 열고 Service에서 검사하면 돼?
A. 권장하지 않는다. SecurityFilterChain에서 기본 접근 제어를 하고 Service에서 리소스 소유자 같은 세부 권한을 보완하는 것이 좋다.

Q. Spring Security 초보가 가장 많이 하는 실수는?
A. 401/403을 혼동하거나 JWT Filter, SecurityContext 저장, Role prefix, CORS 설정을 제대로 구분하지 못하는 실수가 많다.

Q. Security 문제는 어떻게 찾는 게 좋아?
A. 요청 Header, Token 검증, Filter 실행, SecurityContext 저장, 권한 문자열, 401/403 Handler, CORS 순서로 확인한다.

Q. Security Advanced 다음 문서는 뭐가 좋아?
A. QueryDSL Practical, Testing, API Design, Authentication Frontend Flow Domain Rules와 이어지는 것이 좋다.
