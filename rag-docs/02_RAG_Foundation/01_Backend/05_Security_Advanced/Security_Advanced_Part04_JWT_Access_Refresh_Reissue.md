# Security Advanced Part04 - JWT, Access Token, Refresh Token, Reissue

---

# 1. JWT Overview

## 1.1 JWT Concept

### [개념]

JWT(JSON Web Token)는 JSON Claim을 서명해 전달하는 Token 형식이다.

Spring Security 기반 Stateless REST API에서는 인증된 사용자의 식별 정보와 권한 정보를 Access Token에 담아 API 요청 인증에 사용할 수 있다.

JWT는 암호화된 데이터가 아니라 서명된 데이터다. Payload는 쉽게 디코딩될 수 있으므로 민감정보를 넣으면 안 된다.

---

### [핵심]

JWT 핵심 키워드:

- JWT
- JSON Web Token
- Header
- Payload
- Signature
- Claims
- Subject
- Issued At
- Expiration
- Secret Key
- Bearer Token
- Access Token
- Refresh Token
- JWT Filter
- SecurityContext

JWT 구성:

```text
Header
→ Payload
→ Signature
```

JWT 사용 목적:

- 인증 사용자 식별
- API 요청 인증
- 권한 정보 전달
- Stateless Authentication 지원
- Access Token 기반 SecurityContext 구성

---

### [실무]

JWT 기반 API 요청 흐름:

```text
Client
→ Authorization: Bearer AccessToken
→ JWT Filter
→ Signature 검증
→ Expiration 검증
→ Claims 추출
→ Principal 생성
→ Authentication 생성
→ SecurityContext 저장
→ Authorization
→ Controller
```

주의:

- JWT Payload는 암호화가 아니라 Base64Url 인코딩이다.
- 비밀번호, 주민등록번호, Refresh Token, 민감 개인정보를 Claim에 넣지 않는다.
- JWT Secret Key는 안전하게 관리한다.
- Token 만료 시간은 반드시 설정한다.
- Access Token은 짧게 유지한다.
- Refresh Token은 서버 저장소에 저장하고, 가능하면 원문이 아니라 hash로 저장하는 것을 권장한다.
- HTTPS 사용을 전제로 한다.
- Token 원문을 로그에 남기지 않는다.

---

### [FAQ]

Q. JWT는 뭐야?
A. JSON Claim을 서명해 전달하는 Token 형식이며 API 요청에서 인증 정보를 증명하는 데 사용할 수 있다.

Q. JWT Payload는 안전해?
A. 아니다. Payload는 쉽게 디코딩될 수 있으므로 비밀번호나 민감정보를 넣으면 안 된다.

Q. JWT는 암호화야?
A. 일반적인 JWT는 암호화가 아니라 서명이다. 변조 여부는 검증할 수 있지만 Payload 내용은 읽을 수 있다.

Q. JWT를 쓰면 서버 저장소가 전혀 필요 없어?
A. Access Token은 Stateless하게 사용할 수 있지만 Refresh Token 관리, 로그아웃, 강제 만료가 필요하면 서버 저장소가 필요하다.

---

## 1.2 JWT Authentication Flow

### [개념]

JWT Authentication Flow는 Client가 보낸 Access Token을 검증하고 인증 객체를 SecurityContext에 저장하는 과정이다.

Spring Security에서는 보통 Custom JWT Filter가 이 흐름을 담당한다.

---

### [핵심]

JWT Authentication 단계:

- Authorization Header 확인
- Bearer prefix 확인
- Access Token 추출
- Signature 검증
- Expiration 검증
- Claims 추출
- User 상태 확인
- Principal 생성
- Authentication 생성
- SecurityContext 저장

---

### [실무]

JWT Authentication Flow:

```text
Request
→ Authorization Header 확인
→ Bearer Token 추출
→ Access Token 유효성 검증
→ Claims에서 userId / role 추출
→ CustomUserPrincipal 생성
→ UsernamePasswordAuthenticationToken 생성
→ SecurityContextHolder 저장
→ 다음 Filter 진행
```

JWT Filter 예:

```java
String authorizationHeader = request.getHeader("Authorization");

if (authorizationHeader == null || !authorizationHeader.startsWith("Bearer ")) {
    filterChain.doFilter(request, response);
    return;
}

String token = authorizationHeader.substring(7);

if (jwtTokenProvider.validateAccessToken(token)) {
    CustomUserPrincipal principal = jwtTokenProvider.getPrincipal(token);

    Authentication authentication =
            new UsernamePasswordAuthenticationToken(
                    principal,
                    null,
                    principal.getAuthorities()
            );

    SecurityContextHolder.getContext().setAuthentication(authentication);
}

filterChain.doFilter(request, response);
```

권장:

- Token이 없는 Public API는 실패 처리하지 않고 다음 Filter로 넘긴다.
- 잘못된 Token은 인증 실패로 처리한다.
- 인증 성공 시 SecurityContext에 Authentication을 저장한다.
- 이미 Authentication이 있으면 중복 저장을 피한다.
- Token 원문을 로그에 출력하지 않는다.
- 검증 실패 원인은 응답과 서버 로그를 분리한다.

---

### [FAQ]

Q. JWT Filter는 무슨 일을 해?
A. Authorization Header에서 Bearer Token을 추출하고 검증한 뒤 Authentication을 만들어 SecurityContext에 저장한다.

Q. Token이 없으면 JWT Filter에서 바로 401을 반환해야 해?
A. Public API 접근 가능성을 고려해 Token 없음 자체는 다음 Filter로 넘기고 Protected API 인증 실패는 SecurityFilterChain에서 처리하는 구조가 일반적이다.

Q. JWT 인증 성공 후 Controller에서 인증 사용자를 어떻게 가져와?
A. SecurityContext 또는 `@AuthenticationPrincipal`을 통해 Principal을 가져온다.

---

# 2. JWT Structure Rules

## 2.1 Header Rules

### [개념]

JWT Header는 Token 타입과 서명 알고리즘 정보를 담는 영역이다.

Header는 JWT 검증 과정에서 어떤 알고리즘과 Token 타입을 사용하는지 판단하는 데 사용된다.

---

### [핵심]

Header 주요 값:

- typ
- alg

예:

```json
{
  "typ": "JWT",
  "alg": "HS256"
}
```

Header 키워드:

- JWT Header
- Algorithm
- HS256
- RS256
- Token Type
- Signature Algorithm

---

### [실무]

실무 기준:

- 프로젝트에서 사용하는 서명 알고리즘을 명확히 한다.
- 대칭키 방식이면 Secret Key 관리가 중요하다.
- 비대칭키 방식이면 Private Key / Public Key 관리가 중요하다.
- 알고리즘을 무분별하게 허용하지 않는다.
- 라이브러리 기본 설정을 이해하고 사용한다.

주의:

- `alg: none` 같은 취약 설정을 허용하지 않는다.
- 검증 알고리즘과 발급 알고리즘을 일관되게 관리한다.
- Secret Key를 코드에 하드코딩하지 않는다.

---

### [FAQ]

Q. JWT Header에는 뭐가 들어가?
A. Token 타입과 서명 알고리즘 정보가 들어간다.

Q. JWT 알고리즘은 중요해?
A. 중요하다. 서명 검증 방식과 Key 관리 방식이 알고리즘에 따라 달라진다.

Q. Secret Key를 코드에 직접 써도 돼?
A. 안 된다. 환경변수나 Secret 관리 시스템을 통해 관리해야 한다.

---

## 2.2 Payload and Claims Rules

### [개념]

JWT Payload는 Claim을 담는 영역이다.

Claim은 사용자 식별, 권한, 발급 시간, 만료 시간 같은 Token 정보를 표현한다.

---

### [핵심]

표준 Claim 후보:

- sub
- iat
- exp
- iss
- aud
- jti

Custom Claim 후보:

- userId
- role
- authorities
- tokenType

Claim 제외 대상:

- password
- encodedPassword
- refreshToken
- phoneNumber
- address
- 주민등록번호
- 민감 개인정보
- 내부 Secret

---

### [실무]

Access Token Claim 예:

```json
{
  "sub": "1",
  "userId": 1,
  "role": "ROLE_USER",
  "iat": 1790000000,
  "exp": 1790001800
}
```

권장:

- Claim은 최소 정보만 포함한다.
- userId 또는 subject를 사용자 식별 기준으로 사용한다.
- role 또는 authorities를 권한 판단에 사용할 수 있다.
- 만료 시간 exp는 반드시 포함한다.
- tokenType Claim으로 Access / Refresh를 구분할 수 있다.
- Payload에 민감정보를 넣지 않는다.

주의:

- JWT Payload는 누구나 디코딩할 수 있다.
- Claim 정보가 오래 유지되면 사용자 권한 변경 반영이 늦어질 수 있다.
- 권한 변경이 잦은 서비스는 DB 조회 또는 Token 재발급 전략을 검토한다.

---

### [FAQ]

Q. JWT Claim에는 뭘 넣어야 해?
A. userId, role, 만료 시간처럼 인증과 권한 판단에 필요한 최소 정보만 넣는 것이 좋다.

Q. JWT에 비밀번호를 넣어도 돼?
A. 절대 안 된다. JWT Payload는 쉽게 디코딩될 수 있으므로 비밀번호나 민감정보를 넣으면 안 된다.

Q. role을 JWT에 넣어도 돼?
A. 가능하다. 다만 권한 변경 반영 지연 문제가 있으므로 프로젝트 정책에 맞게 검토해야 한다.

---

## 2.3 Signature Rules

### [개념]

JWT Signature는 Header와 Payload가 변조되지 않았는지 검증하기 위한 서명 값이다.

서명 검증에 실패하면 Token은 신뢰할 수 없으며 인증 실패로 처리해야 한다.

---

### [핵심]

Signature 검증 대상:

- Header 변조 여부
- Payload 변조 여부
- Secret Key 일치 여부
- Algorithm 일치 여부
- Token 무결성

Signature 실패 원인:

- Token 문자열 변경
- Secret Key 불일치
- Algorithm 불일치
- Token 형식 오류
- 손상된 Token

---

### [실무]

검증 흐름:

```text
Token 수신
→ Header / Payload 파싱
→ Signature 검증
→ 실패 시 401 Unauthorized
→ 성공 시 Expiration 검증
```

위조 Token 테스트:

```text
정상 JWT 문자열 일부 변경
→ Protected API 요청
→ Signature 검증 실패
→ 401 Unauthorized
```

권장:

- Signature 검증 실패는 401로 처리한다.
- 상세한 검증 실패 사유를 응답에 노출하지 않는다.
- Secret Key를 환경변수 또는 Secret Manager로 관리한다.
- 운영 Secret Key를 Git에 커밋하지 않는다.
- Token 원문과 Secret Key를 로그에 남기지 않는다.

---

### [FAQ]

Q. JWT Signature는 왜 필요해?
A. Header와 Payload가 변조되지 않았는지 검증하기 위해 필요하다.

Q. 위조 JWT는 어떻게 테스트해?
A. 유효한 JWT 문자열 일부를 변경해 서명 검증 실패가 401로 처리되는지 확인할 수 있다.

Q. Signature 검증 실패는 401이야 403이야?
A. 사용자를 신뢰할 수 없으므로 인증 실패인 401로 처리하는 것이 일반적이다.

---

# 3. Access Token Rules

## 3.1 Access Token Concept

### [개념]

Access Token은 API 접근 시 인증 정보를 증명하기 위해 사용하는 짧은 수명의 Token이다.

Client는 Protected API 요청 시 Access Token을 Authorization Header에 Bearer Token 형식으로 전달한다.

---

### [핵심]

Access Token 핵심 키워드:

- Access Token
- API Authorization
- Short Expiration
- Bearer Token
- Authorization Header
- User ID Claim
- Role Claim
- Stateless Validation
- JWT Filter
- SecurityContext

Access Token 특징:

- 짧은 만료 시간
- API 요청 인증용
- 탈취 피해 시간 최소화
- Refresh Token으로 재발급
- 일반적으로 Stateless 검증

---

### [실무]

Access Token 요청 형식:

```http
Authorization: Bearer access-token-value
```

Access Token Flow:

```text
Login 성공
→ Access Token 발급
→ Client 저장
→ API 요청 Header에 첨부
→ JWT Filter 검증
→ SecurityContext 저장
→ Controller 접근
```

권장:

- Access Token 만료 시간을 짧게 설정한다.
- Claim에는 최소 정보만 포함한다.
- Authorization Header Bearer 방식을 사용한다.
- HTTPS 사용을 전제로 한다.
- 탈취 대응을 위해 Refresh Token 구조와 함께 설계한다.
- 만료 시 Refresh Token으로 재발급한다.

---

### [FAQ]

Q. Access Token은 뭐야?
A. API 요청 시 사용자의 인증 정보를 증명하기 위해 사용하는 짧은 수명의 Token이다.

Q. Access Token은 어디에 보내?
A. 일반적으로 Authorization Header에 Bearer Token 형식으로 보낸다.

Q. Access Token 만료 시간은 짧게 해야 해?
A. 일반적으로 짧게 설정해 탈취 시 피해 시간을 줄이고 Refresh Token으로 재발급하는 구조를 사용한다.

---

## 3.2 Access Token Validation Rules

### [개념]

Access Token Validation은 API 요청에 포함된 Access Token의 서명, 만료, 형식, Claim을 검증하는 과정이다.

검증에 성공하면 Authentication 객체를 생성하고 SecurityContext에 저장한다.

---

### [핵심]

검증 항목:

- Token 존재 여부
- Bearer prefix
- Token 형식
- Signature
- Expiration
- tokenType
- subject
- userId
- role
- 사용자 상태

검증 실패 응답:

```text
HTTP 401 Unauthorized
errorCode: UNAUTHORIZED 또는 TOKEN_EXPIRED
message: 인증이 필요합니다.
```

---

### [실무]

Access Token 검증 흐름:

```text
Authorization Header 확인
→ Bearer prefix 확인
→ Token 추출
→ Signature 검증
→ Expiration 검증
→ tokenType 확인
→ Claims 추출
→ Principal 생성
→ Authentication 생성
→ SecurityContext 저장
```

검증 기준:

- 만료된 Access Token은 401로 처리한다.
- 위조된 Access Token은 401로 처리한다.
- Refresh Token을 Access Token 위치에 보내면 실패 처리한다.
- 탈퇴 / 정지 사용자라면 인증 차단을 검토한다.
- Role 변경 즉시 반영이 필요하면 DB 조회를 검토한다.

주의:

- Token 만료와 위조를 사용자 응답에서 과도하게 구분하지 않는다.
- 서버 로그에는 진단 가능한 수준의 원인을 남길 수 있다.
- Token 원문은 로그에 남기지 않는다.

---

### [FAQ]

Q. Access Token 검증에서 뭘 확인해?
A. 서명, 만료 시간, 형식, tokenType, 사용자 식별 Claim, 권한 Claim을 확인한다.

Q. Access Token이 만료되면 어떻게 해?
A. 401로 응답하고 Client가 Refresh Token으로 재발급을 시도하도록 설계한다.

Q. Refresh Token을 Access Token 대신 보내면 어떻게 해?
A. tokenType 검증이 있다면 인증 실패로 처리해야 한다.

---

## 3.3 Access Token Anti Pattern

### [개념]

Access Token Anti Pattern은 Access Token을 과도하게 오래 유지하거나 민감정보를 담거나 검증 없이 신뢰하는 잘못된 설계다.

---

### [핵심]

대표 Anti Pattern:

- Access Token 만료 시간 없음
- Access Token 만료 시간이 과도하게 김
- Payload에 password 포함
- Payload에 refreshToken 포함
- Payload에 민감 개인정보 포함
- Signature 검증 누락
- Expiration 검증 누락
- tokenType 검증 없음
- Token 원문 로그 출력
- HTTP 환경에서 Token 전송
- Frontend role만 믿고 Backend 권한 검증 생략

---

### [실무]

잘못된 Claim 예:

```json
{
  "userId": 1,
  "email": "user@example.com",
  "password": "raw-password",
  "refreshToken": "refresh-token-value",
  "role": "ROLE_ADMIN"
}
```

수정 Claim 예:

```json
{
  "sub": "1",
  "userId": 1,
  "role": "ROLE_USER",
  "tokenType": "ACCESS",
  "exp": 1790001800
}
```

Review 기준:

```text
Access Token Claim 확인
→ 만료 시간 확인
→ Signature 검증 확인
→ Expiration 검증 확인
→ tokenType 검증 확인
→ 로그 출력 확인
→ Authorization 검증 확인
```

---

### [FAQ]

Q. Access Token에 사용자 정보를 많이 넣어도 돼?
A. 권장하지 않는다. userId, role처럼 최소 정보만 넣는 것이 좋다.

Q. Access Token에 만료 시간이 없어도 돼?
A. 안 된다. 탈취 시 피해가 커지므로 만료 시간을 반드시 설정해야 한다.

Q. Access Token을 로그로 찍어도 돼?
A. 안 된다. Token은 인증 수단이므로 원문을 로그에 남기면 안 된다.

---

# 4. Refresh Token Rules

## 4.1 Refresh Token Concept

### [개념]

Refresh Token은 Access Token이 만료되었을 때 새 Access Token을 발급받기 위한 긴 수명의 Token이다.

Refresh Token은 Access Token보다 더 민감하게 관리해야 하며 로그아웃, 강제 만료, 탈취 대응을 위해 서버 저장소에 저장해야 한다.

서버 저장 시에는 가능하면 Refresh Token 원문이 아니라 hash 값을 저장하는 것을 권장한다.

---

### [핵심]

Refresh Token 핵심 키워드:

- Refresh Token
- Token Reissue
- Long Expiration
- Server-side Storage
- Token Hash
- Rotation
- Logout Invalidation
- Device Session
- Theft Detection
- DB
- Redis

Refresh Token 역할:

- Access Token 재발급
- 로그인 유지
- 로그아웃 제어
- 기기별 세션 관리
- 탈취 대응
- 강제 만료 지원

Refresh Token 저장 원칙:

```text
권장 기본값
→ 서버 저장소 저장
→ 원문 저장보다 hash 저장 권장
→ Reissue 시 요청 Token과 저장 hash를 비교
```

---

### [실무]

Refresh Token 발급 흐름:

```text
Login 성공
→ Refresh Token 생성
→ Refresh Token hash 생성
→ userId / deviceId와 연결
→ DB 또는 Redis 저장
→ Client 전달
→ Access Token 만료 시 Reissue 요청
```

저장 예:

```java
String refreshToken = jwtTokenProvider.createRefreshToken(user.getId());
String refreshTokenHash = refreshTokenHasher.hash(refreshToken);

refreshTokenService.saveOrUpdate(
        user.getId(),
        refreshTokenHash,
        expiresAt
);
```

권장:

- Refresh Token은 Access Token보다 긴 만료 시간을 사용한다.
- Refresh Token은 DB 또는 Redis에 저장한다.
- 저장소에는 원문보다 hash 저장을 우선 검토한다.
- 사용자 / 기기 단위 관리가 필요하면 deviceId를 함께 저장한다.
- 로그아웃 시 삭제 또는 무효화한다.
- 비밀번호 변경, 탈퇴, 정지 시 무효화한다.
- 재발급 시 Rotation을 검토한다.

주의:

- Refresh Token도 탈취되면 위험하다.
- 저장 위치는 Frontend Auth Flow와 함께 결정한다.
- Cookie 저장 시 CSRF / SameSite / HttpOnly / Secure를 검토한다.
- LocalStorage 저장 시 XSS 위험을 검토한다.
- Refresh Token 원문을 로그에 남기지 않는다.
- Refresh Token 원문 저장은 구현은 단순하지만 저장소 유출 시 즉시 악용될 수 있으므로 권장하지 않는다.

---

### [FAQ]

Q. Refresh Token은 왜 필요해?
A. Access Token을 짧게 유지하면서 사용자가 자주 로그인하지 않도록 새 Access Token을 발급하기 위해 필요하다.

Q. Refresh Token도 DB에 저장해야 해?
A. 로그아웃, 강제 만료, 탈취 대응이 필요하면 DB나 Redis 같은 서버 저장소에 저장해야 한다.

Q. Refresh Token은 Access Token보다 안전해?
A. 아니다. 수명이 길기 때문에 탈취되면 더 위험할 수 있어 더 엄격하게 관리해야 한다.

Q. Refresh Token은 원문으로 저장해도 돼?
A. 가능은 하지만 권장하지 않는다. 저장소 유출 위험을 줄이기 위해 hash 저장을 우선 검토하는 것이 좋다.

---

## 4.2 Refresh Token Storage Rules

### [개념]

Refresh Token Storage는 발급된 Refresh Token을 서버 저장소에 저장하고 재발급, 로그아웃, 강제 만료, 탈취 대응에 사용하는 설계다.

Refresh Token 저장소에는 Token 원문보다 hash 값을 저장하는 구조를 권장한다.

---

### [핵심]

저장소 후보:

- MySQL
- PostgreSQL
- Redis
- Token Store

저장 필드 후보:

- id
- userId
- tokenHash
- deviceId
- userAgent
- ipAddress
- expiresAt
- revoked
- createdAt
- lastUsedAt

저장 제외 권장:

- refreshToken 원문
- accessToken 원문
- password
- secret key
- 불필요한 개인정보

---

### [실무]

Entity 예:

```java
@Entity
public class RefreshToken {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private Long userId;

    private String tokenHash;

    private String deviceId;

    private LocalDateTime expiresAt;

    private boolean revoked;

    private LocalDateTime createdAt;

    private LocalDateTime lastUsedAt;
}
```

Reissue 비교 예:

```java
if (!refreshTokenHasher.matches(requestRefreshToken, savedToken.getTokenHash())) {
    throw new BusinessException(
            "REFRESH_TOKEN_INVALID",
            "다시 로그인해주세요."
    );
}
```

권장:

- Refresh Token 원문 저장 대신 hash 저장을 우선 검토한다.
- 단일 기기 로그인 정책이면 userId 기준 1개 Token 관리가 가능하다.
- 다중 기기 로그인 정책이면 deviceId 또는 tokenId 기준으로 관리한다.
- Redis는 만료 처리와 빠른 조회에 유리하다.
- DB는 감사 추적과 기기 관리에 유리하다.
- 저장소 Token hash와 요청 Token 원문을 비교한다.

주의:

- Refresh Token 원문 로그 출력 금지
- 만료된 Token 정리 정책 필요
- 탈퇴 / 정지 사용자 Token 무효화 필요
- Rotation 사용 시 이전 Token 처리 정책 필요
- hash 저장 시 재발급 요청에서 받은 원문 Token과 저장 hash를 비교할 수 있는 Hasher가 필요하다.

---

### [FAQ]

Q. Refresh Token을 DB에 원문으로 저장해도 돼?
A. 가능은 하지만 권장하지 않는다. 저장소가 유출되면 Token 원문이 바로 악용될 수 있으므로 hash 저장을 우선 검토하는 것이 좋다.

Q. Redis와 DB 중 어디에 저장하는 게 좋아?
A. Redis는 만료와 성능에 유리하고 DB는 감사 추적과 기기 관리에 유리하다. 프로젝트 요구사항에 따라 선택한다.

Q. 다중 기기 로그인을 지원하려면 어떻게 저장해?
A. userId와 deviceId 또는 tokenId를 함께 저장해 기기별 Refresh Token을 관리한다.

Q. hash로 저장하면 Reissue 때 어떻게 검증해?
A. 요청으로 받은 Refresh Token 원문을 Hasher의 matches 함수로 저장된 tokenHash와 비교한다.

---

## 4.3 Refresh Token Rotation Rules

### [개념]

Refresh Token Rotation은 Token Reissue 시 기존 Refresh Token을 새 Refresh Token으로 교체하는 전략이다.

Rotation은 Refresh Token 재사용을 탐지하고 탈취 피해를 줄이기 위해 사용할 수 있다.

---

### [핵심]

Rotation 핵심 키워드:

- Refresh Token Rotation
- Token Reuse Detection
- Old Token Invalidation
- New Refresh Token
- New Token Hash
- Theft Detection
- Device Session
- Revoked Token

Rotation Flow:

```text
Reissue Request
→ Refresh Token 검증
→ 저장소 Token hash 일치 확인
→ 새 Access Token 발급
→ 새 Refresh Token 발급
→ 새 Refresh Token hash 저장
→ 기존 Refresh Token 폐기
```

---

### [실무]

Rotation 적용 기준:

- 보안 요구사항이 높은 서비스
- 장기 로그인 유지 기능
- 다중 기기 세션 관리
- 탈취 탐지 필요
- 재사용 탐지 정책 필요

재사용 탐지 흐름:

```text
이미 폐기된 Refresh Token으로 Reissue 요청
→ Token 재사용 의심
→ 해당 사용자 또는 기기 Token 전체 무효화
→ 재로그인 요구
```

권장:

- Rotation 사용 여부를 명확히 문서화한다.
- Rotation 사용 시 이전 Token을 즉시 무효화한다.
- 새 Refresh Token도 hash로 저장한다.
- 폐기된 Token 재사용 시 탈취 가능성으로 판단한다.
- 사용자 / 기기 단위 무효화 정책을 둔다.
- Frontend는 새 Refresh Token을 안전하게 교체 저장해야 한다.

주의:

- Rotation은 구현 복잡도를 높인다.
- 동시 요청 상황에서 Race Condition이 발생할 수 있다.
- Token 교체 실패 시 사용자가 로그아웃될 수 있다.
- Frontend 저장 실패 시 재발급 루프가 발생할 수 있다.

---

### [FAQ]

Q. Refresh Token Rotation은 뭐야?
A. 재발급할 때 기존 Refresh Token을 새 Refresh Token으로 교체하는 전략이다.

Q. Rotation은 꼭 해야 해?
A. 필수는 아니다. 보안 요구사항, 구현 복잡도, 사용자 경험을 고려해 선택한다.

Q. 폐기된 Refresh Token이 다시 오면 어떻게 해?
A. 탈취 또는 재사용 가능성으로 보고 해당 기기 또는 사용자 Token을 무효화하는 정책을 검토한다.

Q. Rotation에서도 hash 저장을 써야 해?
A. 권장된다. 새로 발급한 Refresh Token도 원문보다 hash로 저장하는 것이 안전하다.

---

# 5. Token Reissue Rules

## 5.1 Token Reissue Concept

### [개념]

Token Reissue는 유효한 Refresh Token을 검증한 뒤 새 Access Token을 발급하는 과정이다.

Access Token이 만료되었을 때 사용자가 다시 로그인하지 않고 인증 상태를 유지할 수 있게 한다.

Reissue에서는 JWT 자체 검증뿐 아니라 서버 저장소에 저장된 Refresh Token hash와 요청 Refresh Token의 일치 여부를 반드시 확인해야 한다.

---

### [핵심]

Token Reissue 핵심 키워드:

- Token Reissue
- Access Token Expired
- Refresh Token Validation
- Stored Token Hash Match
- User Status Check
- Access Token Issue
- Refresh Token Rotation
- 401 Unauthorized

검증 대상:

- Refresh Token 서명
- Refresh Token 만료
- tokenType
- 저장소 존재 여부
- 저장소 tokenHash 일치 여부
- revoked 여부
- 사용자 상태
- Rotation 여부

---

### [실무]

Reissue Flow:

```text
Reissue Request
→ Refresh Token 추출
→ Refresh Token 서명 검증
→ Refresh Token 만료 검증
→ tokenType 확인
→ 저장소 Token 조회
→ 요청 Refresh Token과 저장 tokenHash 비교
→ 사용자 상태 확인
→ 새 Access Token 생성
→ 필요 시 Refresh Token Rotation
→ Reissue Response
```

Service 예:

```java
@Transactional
public TokenReissueResponse reissue(String refreshToken) {
    jwtTokenProvider.validateRefreshToken(refreshToken);

    Long userId = jwtTokenProvider.getUserId(refreshToken);

    RefreshToken savedToken = refreshTokenRepository.findByUserId(userId)
            .orElseThrow(() -> new BusinessException(
                    "REFRESH_TOKEN_INVALID",
                    "다시 로그인해주세요."
            ));

    if (savedToken.isRevoked()) {
        throw new BusinessException(
                "REFRESH_TOKEN_INVALID",
                "다시 로그인해주세요."
        );
    }

    if (!refreshTokenHasher.matches(refreshToken, savedToken.getTokenHash())) {
        throw new BusinessException(
                "REFRESH_TOKEN_INVALID",
                "다시 로그인해주세요."
        );
    }

    User user = userRepository.findById(userId)
            .orElseThrow(() -> new BusinessException(
                    "USER_NOT_FOUND",
                    "사용자를 찾을 수 없습니다."
            ));

    validateUserCanReissue(user);

    String newAccessToken = jwtTokenProvider.createAccessToken(user.getId(), user.getRole());

    return new TokenReissueResponse(newAccessToken, "Bearer", accessTokenExpiresIn);
}
```

권장:

- Refresh Token 검증 실패는 401로 처리한다.
- 저장소 tokenHash와 요청 Token 일치 여부를 확인한다.
- Refresh Token 원문 저장을 전제로 구현하지 않는다.
- 탈퇴 / 정지 / 잠금 사용자는 재발급을 차단한다.
- 새 Access Token의 권한 Claim은 최신 사용자 권한 기준으로 생성한다.
- Refresh Token Rotation 사용 여부를 명확히 한다.

---

### [FAQ]

Q. Token Reissue는 뭐야?
A. 유효한 Refresh Token을 검증해 새 Access Token을 발급하는 과정이다.

Q. Access Token이 만료되면 어떻게 해?
A. Refresh Token이 유효하면 재발급 API로 새 Access Token을 받고, Refresh Token도 만료되었으면 재로그인해야 한다.

Q. 재발급 API는 Public API야?
A. 경로 접근은 permitAll일 수 있지만 Refresh Token 검증이 반드시 필요한 API다.

Q. Reissue에서 저장소 검증은 왜 필요해?
A. JWT 서명이 유효하더라도 로그아웃, 강제 만료, 탈취 대응을 위해 서버 저장소의 tokenHash와 일치하는지 확인해야 한다.

---

## 5.2 Reissue Request and Response Rules

### [개념]

Reissue Request는 Client가 Refresh Token을 서버에 전달해 새 Access Token 발급을 요청하는 것이다.

Reissue Response는 새 Access Token과 필요 시 새 Refresh Token을 반환하는 응답이다.

---

### [핵심]

Refresh Token 전달 방식 후보:

- Request Body
- HttpOnly Cookie
- Authorization Header
- Custom Header

Reissue Response 포함 후보:

- accessToken
- refreshToken
- tokenType
- expiresIn

Reissue Response 제외 대상:

- password
- secretKey
- internal token id
- 민감 개인정보
- User Entity 전체

---

### [실무]

Request Body 방식 예:

```java
public record TokenReissueRequest(
        String refreshToken
) {
}
```

Response 예:

```java
public record TokenReissueResponse(
        String accessToken,
        String refreshToken,
        String tokenType,
        Long expiresIn
) {
}
```

Rotation 없는 응답 예:

```json
{
  "accessToken": "new-access-token",
  "tokenType": "Bearer",
  "expiresIn": 1800
}
```

Rotation 있는 응답 예:

```json
{
  "accessToken": "new-access-token",
  "refreshToken": "new-refresh-token",
  "tokenType": "Bearer",
  "expiresIn": 1800
}
```

권장:

- Refresh Token 전달 방식을 Frontend Auth Flow와 일치시킨다.
- Cookie 방식이면 CSRF, SameSite, HttpOnly, Secure를 검토한다.
- Body 방식이면 XSS와 저장 위치를 검토한다.
- Rotation을 사용하면 새 Refresh Token을 반드시 Client에 반영한다.
- Rotation 사용 시 서버 저장소에는 새 Refresh Token hash를 저장한다.
- 실패 응답은 Frontend가 재로그인 판단 가능하게 설계한다.

---

### [FAQ]

Q. Refresh Token은 어디에 담아 보내?
A. Request Body, HttpOnly Cookie, Header 방식이 가능하며 Frontend Auth 정책과 보안 요구사항에 맞게 선택한다.

Q. Reissue Response에 Refresh Token도 다시 줘야 해?
A. Rotation을 사용한다면 새 Refresh Token을 반환해야 한다. Rotation을 사용하지 않으면 Access Token만 반환할 수 있다.

Q. Refresh Token을 Authorization Header에 보내도 돼?
A. 가능하지만 Access Token과 혼동되지 않도록 tokenType 검증과 API 규칙을 명확히 해야 한다.

---

## 5.3 Reissue Failure Rules

### [개념]

Reissue Failure는 Refresh Token이 유효하지 않거나 저장소 상태와 일치하지 않아 새 Access Token을 발급할 수 없는 상태다.

Reissue 실패는 인증 상태를 유지할 수 없다는 의미이므로 일반적으로 401 Unauthorized로 처리한다.

---

### [핵심]

Reissue 실패 원인:

- Refresh Token 없음
- Refresh Token 만료
- Refresh Token 서명 오류
- Refresh Token 형식 오류
- tokenType 불일치
- 저장소 Token 없음
- 저장소 tokenHash 불일치
- revoked Token
- 폐기된 Token 재사용
- 사용자 탈퇴
- 사용자 정지
- 사용자 잠금

권장 응답:

```text
HTTP 401 Unauthorized
errorCode: REFRESH_TOKEN_INVALID
message: 다시 로그인해주세요.
```

---

### [실무]

실패 처리 예:

```java
throw new BusinessException(
        "REFRESH_TOKEN_INVALID",
        "다시 로그인해주세요."
);
```

실패 흐름:

```text
Refresh Token 검증 실패
→ 저장소 tokenHash 불일치
→ Reissue 실패
→ 401 Unauthorized
→ Client Token 제거
→ 재로그인 요구
```

권장:

- 실패 원인을 사용자에게 과도하게 노출하지 않는다.
- Frontend는 Reissue 실패 시 로그아웃 처리한다.
- 저장소 tokenHash 불일치는 탈취 가능성으로 검토한다.
- Rotation 재사용 탐지 시 해당 사용자 또는 기기 Token 전체 무효화를 검토한다.
- 탈퇴 / 정지 사용자는 재발급을 차단한다.

---

### [FAQ]

Q. Refresh Token이 틀리면 어떤 응답을 줘?
A. 인증 실패로 보고 401 계열 응답을 주는 것이 일반적이다. 상세 메시지는 보안상 과도하게 노출하지 않는다.

Q. Refresh Token이 만료되면 어떻게 해?
A. 새 Access Token을 발급할 수 없으므로 Client는 Token을 제거하고 재로그인을 요구해야 한다.

Q. 저장소 Token과 요청 Token이 다르면 어떻게 해?
A. 탈취 가능성을 고려해 401로 차단하고 해당 사용자 또는 기기 Token 무효화를 검토한다.

Q. 저장소 tokenHash와 요청 Token이 다르면 어떻게 해?
A. 저장된 Refresh Token과 요청 Token이 일치하지 않는 것이므로 401로 차단하고 탈취 또는 재사용 가능성을 검토한다.

---

# 6. Token Storage Strategy

## 6.1 Frontend Token Storage Overview

### [개념]

Token Storage Strategy는 Client가 Access Token과 Refresh Token을 어디에 저장하고 어떻게 전송할지 결정하는 보안 설계다.

Backend 문서는 저장 방식의 장단점과 API 응답 / Header / Cookie 정책을 Frontend Auth Flow와 연동할 수 있도록 기준을 제공해야 한다.

---

### [핵심]

Token 저장 후보:

- Memory
- LocalStorage
- SessionStorage
- HttpOnly Cookie
- Secure Cookie
- SameSite Cookie

검토 위험:

- XSS
- CSRF
- Token Theft
- Browser Auto Credential
- Reissue Flow
- Logout Flow

---

### [실무]

Backend 제공 기준:

- Login Response 형식
- Refresh Token 전달 방식
- Reissue API 명세
- Logout API 명세
- 401 / 403 errorCode
- CORS allowCredentials 여부
- Cookie SameSite / HttpOnly / Secure 여부
- Authorization Header 사용 여부

저장 방식 비교:

| 저장 방식       | 장점               | 주의                |
| --------------- | ------------------ | ------------------- |
| Memory          | XSS 노출 시간 감소 | 새로고침 시 사라짐  |
| LocalStorage    | 구현 쉬움          | XSS에 취약          |
| SessionStorage  | 탭 단위 유지       | XSS에 취약          |
| HttpOnly Cookie | JS 접근 차단       | CSRF 검토 필요      |
| Secure Cookie   | HTTPS 전송         | 로컬 개발 설정 필요 |

권장:

- Access Token은 Authorization Header 사용 여부를 명확히 한다.
- Refresh Token을 Cookie로 전달하면 CSRF 설정과 CORS credentials를 검토한다.
- LocalStorage 사용 시 XSS 위험을 문서화한다.
- 저장 방식은 Frontend Auth Flow 문서와 함께 결정한다.
- Backend 저장소에는 Refresh Token 원문보다 hash 저장을 우선 검토한다.

---

### [FAQ]

Q. Token은 어디에 저장하는 게 좋아?
A. 정답은 없다. XSS, CSRF, UX, 구현 복잡도를 고려해 Frontend Auth Flow와 함께 결정해야 한다.

Q. LocalStorage에 Token을 저장해도 돼?
A. 구현은 쉽지만 XSS에 취약하므로 위험을 이해하고 사용해야 한다.

Q. HttpOnly Cookie가 무조건 안전해?
A. JS 접근은 막을 수 있지만 CSRF와 SameSite, Secure 설정을 함께 검토해야 한다.

---

## 6.2 Backend Token Storage Requirements

### [개념]

Backend Token Storage Requirements는 서버가 Refresh Token을 저장하고 검증하기 위해 갖춰야 할 기준이다.

Access Token은 일반적인 Stateless JWT 구조에서는 DB에 저장하지 않는다.

Refresh Token은 로그아웃, 재발급 제어, 강제 만료, 탈취 대응을 위해 서버 저장소에 저장하며, 가능하면 원문이 아니라 hash로 저장하는 것을 권장한다.

---

### [핵심]

Backend 저장 대상:

- Refresh Token Hash
- User ID
- Device ID
- Expiration
- Revoked 여부
- Last Used At
- Created At

Backend 저장 제외 대상:

- Access Token 원문
- Refresh Token 원문
- Password
- Secret Key
- 불필요한 개인정보

---

### [실무]

단일 Refresh Token 정책:

```text
userId 기준 Refresh Token hash 1개 저장
→ 새 로그인 시 기존 Token hash 교체
→ 한 계정 한 기기 로그인 정책에 적합
```

다중 Refresh Token 정책:

```text
userId + deviceId 기준 Refresh Token hash 여러 개 저장
→ 기기별 로그아웃 가능
→ 다중 기기 로그인 정책에 적합
```

권장:

- Refresh Token 원문 저장 대신 hash 저장을 검토한다.
- expiresAt을 저장해 만료 정리 작업을 수행한다.
- revoked 상태를 저장해 강제 무효화할 수 있다.
- 비밀번호 변경 / 탈퇴 / 정지 시 Token을 무효화한다.
- Reissue 시 lastUsedAt을 갱신할 수 있다.
- Reissue 시 요청 Token 원문과 저장 tokenHash를 비교한다.

---

### [FAQ]

Q. Access Token도 DB에 저장해야 해?
A. 일반적인 Stateless JWT 구조에서는 Access Token을 DB에 저장하지 않는다.

Q. Refresh Token hash 저장은 왜 해?
A. 저장소가 유출되었을 때 Refresh Token 원문 악용 위험을 줄이기 위해서다.

Q. 단일 기기 로그인과 다중 기기 로그인은 Token 저장이 달라?
A. 다르다. 단일 기기는 userId 기준 1개, 다중 기기는 userId + deviceId 기준 여러 개를 관리할 수 있다.

Q. Refresh Token 원문 저장은 금지야?
A. 반드시 기술적으로 불가능한 것은 아니지만 권장하지 않는다. 보안 기준에서는 hash 저장을 우선 검토한다.

---

# 7. JWT Exception Rules

## 7.1 Token Expired vs Token Invalid

### [개념]

Token Expired는 Token의 만료 시간이 지나 인증에 사용할 수 없는 상태다.

Token Invalid는 서명 오류, 형식 오류, tokenType 불일치, 저장소 tokenHash 불일치 등으로 Token 자체를 신뢰할 수 없는 상태다.

둘 다 인증 실패이므로 일반적으로 401 Unauthorized로 처리한다.

---

### [핵심]

Token Expired:

- exp 만료
- Access Token 재발급 가능성 있음
- Refresh Token 만료 시 재로그인 필요

Token Invalid:

- Signature 오류
- Token 형식 오류
- tokenType 불일치
- 저장소 tokenHash 불일치
- 위조 가능성

공통 응답:

```text
HTTP 401 Unauthorized
```

---

### [실무]

Access Token Expired Flow:

```text
Access Token 만료
→ 401 TOKEN_EXPIRED
→ Client Reissue 요청
→ Refresh Token 유효
→ 저장소 tokenHash 일치
→ 새 Access Token 발급
```

Refresh Token Expired Flow:

```text
Refresh Token 만료
→ Reissue 실패
→ 401 REFRESH_TOKEN_INVALID
→ Client Token 제거
→ 재로그인 요구
```

Invalid Token Flow:

```text
Token 위조 또는 형식 오류
→ 401 UNAUTHORIZED
→ Client Token 제거 또는 재로그인
```

권장:

- Access Token 만료는 Frontend가 재발급을 시도할 수 있게 errorCode를 제공한다.
- Refresh Token 실패는 재로그인으로 연결한다.
- 위조 Token 상세 사유는 응답에 과도하게 노출하지 않는다.
- 서버 로그에는 진단 가능한 오류 분류를 남길 수 있다.
- Token 원문은 로그에 남기지 않는다.

---

### [FAQ]

Q. Token Expired와 Token Invalid는 뭐가 달라?
A. Expired는 만료 시간이 지난 것이고 Invalid는 서명, 형식, 타입, 저장소 일치 여부 등이 잘못되어 신뢰할 수 없는 상태다.

Q. Access Token 만료는 어떤 errorCode가 좋아?
A. Frontend 재발급 판단을 위해 TOKEN_EXPIRED 같은 구분 가능한 errorCode를 사용할 수 있다.

Q. 위조 Token도 TOKEN_EXPIRED로 처리해도 돼?
A. 권장하지 않는다. 위조나 형식 오류는 UNAUTHORIZED 또는 TOKEN_INVALID처럼 구분하는 것이 좋다.

---

## 7.2 Token Error Response Rules

### [개념]

Token Error Response는 JWT 검증 실패 시 Client가 재발급, 로그아웃, 재로그인을 판단할 수 있도록 제공하는 일관된 인증 실패 응답이다.

---

### [핵심]

응답 필드 후보:

- status
- errorCode
- message
- timestamp
- path

errorCode 후보:

- UNAUTHORIZED
- TOKEN_EXPIRED
- TOKEN_INVALID
- REFRESH_TOKEN_INVALID
- REFRESH_TOKEN_EXPIRED
- ACCESS_TOKEN_REQUIRED

---

### [실무]

Access Token 없음:

```json
{
  "status": 401,
  "errorCode": "ACCESS_TOKEN_REQUIRED",
  "message": "인증이 필요합니다."
}
```

Access Token 만료:

```json
{
  "status": 401,
  "errorCode": "TOKEN_EXPIRED",
  "message": "인증이 만료되었습니다."
}
```

Refresh Token 실패:

```json
{
  "status": 401,
  "errorCode": "REFRESH_TOKEN_INVALID",
  "message": "다시 로그인해주세요."
}
```

권장:

- API 전체 Error Response 형식과 맞춘다.
- Frontend가 처리 가능한 errorCode를 제공한다.
- Token 원인 상세를 과도하게 노출하지 않는다.
- Stack trace를 응답하지 않는다.
- Secret Key, Token 원문, 내부 예외 메시지를 응답하지 않는다.

---

### [FAQ]

Q. Token Error Response도 ApiResponse 형식으로 맞춰야 해?
A. 프로젝트 응답 규칙이 있다면 맞추는 것이 Frontend 처리에 좋다.

Q. Access Token 만료와 Refresh Token 만료 errorCode를 분리해야 해?
A. Frontend 처리 흐름이 다르므로 분리하는 것이 좋다.

Q. JWT 예외는 GlobalExceptionHandler에서 처리돼?
A. Filter Chain에서 발생한 예외는 AuthenticationEntryPoint에서 처리되는 경우가 많다.

---

# 8. JWT Security Review

## 8.1 JWT Security Checklist

### [개념]

JWT Security Checklist는 Access Token, Refresh Token, Reissue, 저장소, 예외 처리, 로그 보안을 검수하기 위한 기준이다.

---

### [핵심]

Checklist:

```md
- [ ] JWT Payload에 민감정보가 없는가?
- [ ] Access Token 만료 시간이 설정되어 있는가?
- [ ] Access Token 만료 시간이 과도하게 길지 않은가?
- [ ] Refresh Token 만료 시간이 설정되어 있는가?
- [ ] Access Token과 Refresh Token 역할이 분리되어 있는가?
- [ ] tokenType 검증이 가능한가?
- [ ] Signature 검증을 수행하는가?
- [ ] Expiration 검증을 수행하는가?
- [ ] JWT Filter가 등록되어 있는가?
- [ ] JWT Filter가 SecurityContext에 Authentication을 저장하는가?
- [ ] Token 없음 Public API 요청을 무조건 실패 처리하지 않는가?
- [ ] Refresh Token 서버 저장소가 있는가?
- [ ] Refresh Token 원문 대신 hash 저장을 검토했는가?
- [ ] Reissue에서 요청 Token과 저장 tokenHash를 비교하는가?
- [ ] Refresh Token Rotation 여부가 결정되어 있는가?
- [ ] Logout 시 Refresh Token이 무효화되는가?
- [ ] Password 변경 시 Refresh Token 무효화를 검토하는가?
- [ ] 탈퇴 / 정지 사용자 Reissue가 차단되는가?
- [ ] Token 원문을 로그로 출력하지 않는가?
- [ ] Secret Key를 코드에 하드코딩하지 않는가?
- [ ] Token 오류 응답이 401 기준으로 처리되는가?
```

---

### [실무]

Review Flow:

```text
JWT 발급 로직 확인
→ Access Token Claim 확인
→ Refresh Token Claim 확인
→ Token 검증 로직 확인
→ JWT Filter 확인
→ SecurityContext 저장 확인
→ Refresh Token 저장소 확인
→ tokenHash 저장 여부 확인
→ Reissue Flow 확인
→ Logout 무효화 확인
→ Token Error Response 확인
→ 로그 노출 확인
```

테스트 우선순위:

```text
정상 Access Token
→ Protected API 200

Access Token 없음
→ Protected API 401

위조 Access Token
→ Protected API 401

만료 Access Token
→ Protected API 401 TOKEN_EXPIRED

유효 Refresh Token
→ Reissue 200

만료 Refresh Token
→ Reissue 401

로그아웃 후 Refresh Token
→ Reissue 401

저장소 tokenHash 불일치 Refresh Token
→ Reissue 401
```

---

### [FAQ]

Q. JWT 검수에서 가장 중요한 것은 뭐야?
A. Payload 민감정보 금지, 서명/만료 검증, Access/Refresh 역할 분리, Refresh Token hash 저장/무효화, SecurityContext 저장이다.

Q. JWT 테스트에서 위조 Token은 어떻게 만들어?
A. 정상 JWT 문자열 일부를 변경해 Signature 검증 실패가 401로 처리되는지 확인하면 된다.

Q. 로그아웃 후 Reissue가 성공하면 문제야?
A. 문제다. Refresh Token 무효화 또는 저장소 검증이 제대로 동작하지 않는 것이다.

Q. Refresh Token hash 불일치 테스트도 필요해?
A. 필요하다. 저장소 Token과 요청 Token이 다를 때 Reissue가 401로 차단되는지 확인해야 한다.

---

# 9. Part04 Checklist

## 9.1 JWT Access Refresh Reissue Checklist

### [개념]

Part04 Checklist는 JWT, Access Token, Refresh Token, Token Reissue 문서가 Security Advanced 기준에 맞게 작성되었는지 확인하는 검수 목록이다.

---

### [핵심]

Checklist:

```md
- [ ] JWT 개념이 서명 기반 Token으로 설명되었는가?
- [ ] JWT Payload가 암호화가 아니라는 점이 포함되었는가?
- [ ] JWT Header / Payload / Signature가 설명되었는가?
- [ ] Claim 최소화 기준이 포함되었는가?
- [ ] 민감정보 Claim 금지가 포함되었는가?
- [ ] Access Token 역할이 설명되었는가?
- [ ] Access Token 만료 시간 기준이 포함되었는가?
- [ ] Access Token 검증 흐름이 포함되었는가?
- [ ] Refresh Token 역할이 설명되었는가?
- [ ] Refresh Token 서버 저장소 기준이 포함되었는가?
- [ ] Refresh Token 원문 저장보다 hash 저장 권장 기준이 포함되었는가?
- [ ] Reissue에서 tokenHash 비교 기준이 포함되었는가?
- [ ] Refresh Token Rotation 기준이 포함되었는가?
- [ ] Token Reissue Flow가 포함되었는가?
- [ ] Reissue 실패 기준이 포함되었는가?
- [ ] Token Storage Strategy가 포함되었는가?
- [ ] Token Expired와 Token Invalid 비교가 포함되었는가?
- [ ] Token Error Response 기준이 포함되었는가?
- [ ] JWT Anti Pattern이 포함되었는가?
- [ ] SecurityContext 연결이 포함되었는가?
- [ ] Logout / Password Change 후 Refresh Token 무효화 연결이 포함되었는가?
- [ ] Testing 문서와 연결 가능한 테스트 기준이 포함되었는가?
- [ ] Retrieval Queries가 충분한가?
```

---

### [실무]

후속 문서 연결:

```text
Part04 JWT Access Refresh Reissue
→ Part05 Authorization Resource Owner Check
→ Part06 Exception Handling CORS CSRF
→ Part07 OAuth2 Frontend Integration
→ Part08 Security Testing Troubleshooting
```

선행 문서 연결:

```text
Part01 Core Concepts
→ Authentication / SecurityContext / Principal / 401 기준 제공

Part02 SecurityFilterChain
→ JWT Filter 등록 / Stateless Session / Exception Handler 기준 제공

Part03 Password Login Logout
→ Login 성공 후 Token 발급 / Logout 시 Refresh Token 무효화 기준 제공
```

---

### [FAQ]

Q. Part04에서 가장 중요한 주제는 뭐야?
A. JWT 구조, Access Token 검증, Refresh Token hash 저장, Token Reissue, Token Error Response다.

Q. Part04는 Login 문서와 어떻게 연결돼?
A. Login에서 비밀번호 검증이 성공하면 Access Token과 Refresh Token을 발급하는 흐름으로 연결된다.

Q. Part04는 Logout 문서와 어떻게 연결돼?
A. Logout에서 Refresh Token을 무효화해야 Reissue가 차단된다.

Q. Part04는 SecurityFilterChain 문서와 어떻게 연결돼?
A. SecurityFilterChain에 등록된 JWT Filter가 Access Token을 검증하고 SecurityContext에 Authentication을 저장한다.

---

# Retrieval Queries

### [FAQ]

Q. JWT는 뭐야?
A. JSON Claim을 서명해 전달하는 Token 형식이며 API 요청에서 인증 정보를 증명하는 데 사용할 수 있다.

Q. JWT Payload는 안전해?
A. 아니다. Payload는 쉽게 디코딩될 수 있으므로 비밀번호나 민감정보를 넣으면 안 된다.

Q. JWT는 암호화야?
A. 일반적인 JWT는 암호화가 아니라 서명이다. 변조 여부는 검증할 수 있지만 Payload 내용은 읽을 수 있다.

Q. JWT를 쓰면 서버 저장소가 전혀 필요 없어?
A. Access Token은 Stateless하게 사용할 수 있지만 Refresh Token 관리, 로그아웃, 강제 만료가 필요하면 서버 저장소가 필요하다.

Q. JWT Filter는 무슨 일을 해?
A. Authorization Header에서 Bearer Token을 추출하고 검증한 뒤 Authentication을 만들어 SecurityContext에 저장한다.

Q. Token이 없으면 JWT Filter에서 바로 401을 반환해야 해?
A. Public API 접근 가능성을 고려해 Token 없음 자체는 다음 Filter로 넘기고 Protected API 인증 실패는 SecurityFilterChain에서 처리하는 구조가 일반적이다.

Q. JWT 인증 성공 후 Controller에서 인증 사용자를 어떻게 가져와?
A. SecurityContext 또는 `@AuthenticationPrincipal`을 통해 Principal을 가져온다.

Q. JWT Header에는 뭐가 들어가?
A. Token 타입과 서명 알고리즘 정보가 들어간다.

Q. JWT 알고리즘은 중요해?
A. 중요하다. 서명 검증 방식과 Key 관리 방식이 알고리즘에 따라 달라진다.

Q. Secret Key를 코드에 직접 써도 돼?
A. 안 된다. 환경변수나 Secret 관리 시스템을 통해 관리해야 한다.

Q. JWT Claim에는 뭘 넣어야 해?
A. userId, role, 만료 시간처럼 인증과 권한 판단에 필요한 최소 정보만 넣는 것이 좋다.

Q. JWT에 비밀번호를 넣어도 돼?
A. 절대 안 된다. JWT Payload는 쉽게 디코딩될 수 있으므로 비밀번호나 민감정보를 넣으면 안 된다.

Q. role을 JWT에 넣어도 돼?
A. 가능하다. 다만 권한 변경 반영 지연 문제가 있으므로 프로젝트 정책에 맞게 검토해야 한다.

Q. JWT Signature는 왜 필요해?
A. Header와 Payload가 변조되지 않았는지 검증하기 위해 필요하다.

Q. 위조 JWT는 어떻게 테스트해?
A. 유효한 JWT 문자열 일부를 변경해 서명 검증 실패가 401로 처리되는지 확인할 수 있다.

Q. Signature 검증 실패는 401이야 403이야?
A. 사용자를 신뢰할 수 없으므로 인증 실패인 401로 처리하는 것이 일반적이다.

Q. Access Token은 뭐야?
A. API 요청 시 사용자의 인증 정보를 증명하기 위해 사용하는 짧은 수명의 Token이다.

Q. Access Token은 어디에 보내?
A. 일반적으로 Authorization Header에 Bearer Token 형식으로 보낸다.

Q. Access Token 만료 시간은 짧게 해야 해?
A. 일반적으로 짧게 설정해 탈취 시 피해 시간을 줄이고 Refresh Token으로 재발급하는 구조를 사용한다.

Q. Access Token 검증에서 뭘 확인해?
A. 서명, 만료 시간, 형식, tokenType, 사용자 식별 Claim, 권한 Claim을 확인한다.

Q. Access Token이 만료되면 어떻게 해?
A. 401로 응답하고 Client가 Refresh Token으로 재발급을 시도하도록 설계한다.

Q. Refresh Token을 Access Token 대신 보내면 어떻게 해?
A. tokenType 검증이 있다면 인증 실패로 처리해야 한다.

Q. Access Token에 사용자 정보를 많이 넣어도 돼?
A. 권장하지 않는다. userId, role처럼 최소 정보만 넣는 것이 좋다.

Q. Access Token에 만료 시간이 없어도 돼?
A. 안 된다. 탈취 시 피해가 커지므로 만료 시간을 반드시 설정해야 한다.

Q. Access Token을 로그로 찍어도 돼?
A. 안 된다. Token은 인증 수단이므로 원문을 로그에 남기면 안 된다.

Q. Refresh Token은 왜 필요해?
A. Access Token을 짧게 유지하면서 사용자가 자주 로그인하지 않도록 새 Access Token을 발급하기 위해 필요하다.

Q. Refresh Token도 DB에 저장해야 해?
A. 로그아웃, 강제 만료, 탈취 대응이 필요하면 DB나 Redis 같은 서버 저장소에 저장해야 한다.

Q. Refresh Token은 Access Token보다 안전해?
A. 아니다. 수명이 길기 때문에 탈취되면 더 위험할 수 있어 더 엄격하게 관리해야 한다.

Q. Refresh Token은 원문으로 저장해도 돼?
A. 가능은 하지만 권장하지 않는다. 저장소 유출 위험을 줄이기 위해 hash 저장을 우선 검토하는 것이 좋다.

Q. Refresh Token을 DB에 원문으로 저장해도 돼?
A. 가능은 하지만 권장하지 않는다. 저장소가 유출되면 Token 원문이 바로 악용될 수 있으므로 hash 저장을 우선 검토하는 것이 좋다.

Q. Redis와 DB 중 어디에 저장하는 게 좋아?
A. Redis는 만료와 성능에 유리하고 DB는 감사 추적과 기기 관리에 유리하다. 프로젝트 요구사항에 따라 선택한다.

Q. 다중 기기 로그인을 지원하려면 어떻게 저장해?
A. userId와 deviceId 또는 tokenId를 함께 저장해 기기별 Refresh Token을 관리한다.

Q. hash로 저장하면 Reissue 때 어떻게 검증해?
A. 요청으로 받은 Refresh Token 원문을 Hasher의 matches 함수로 저장된 tokenHash와 비교한다.

Q. Refresh Token Rotation은 뭐야?
A. 재발급할 때 기존 Refresh Token을 새 Refresh Token으로 교체하는 전략이다.

Q. Rotation은 꼭 해야 해?
A. 필수는 아니다. 보안 요구사항, 구현 복잡도, 사용자 경험을 고려해 선택한다.

Q. 폐기된 Refresh Token이 다시 오면 어떻게 해?
A. 탈취 또는 재사용 가능성으로 보고 해당 기기 또는 사용자 Token을 무효화하는 정책을 검토한다.

Q. Rotation에서도 hash 저장을 써야 해?
A. 권장된다. 새로 발급한 Refresh Token도 원문보다 hash로 저장하는 것이 안전하다.

Q. Token Reissue는 뭐야?
A. 유효한 Refresh Token을 검증해 새 Access Token을 발급하는 과정이다.

Q. Access Token이 만료되면 어떻게 해?
A. Refresh Token이 유효하면 재발급 API로 새 Access Token을 받고, Refresh Token도 만료되었으면 재로그인해야 한다.

Q. 재발급 API는 Public API야?
A. 경로 접근은 permitAll일 수 있지만 Refresh Token 검증이 반드시 필요한 API다.

Q. Reissue에서 저장소 검증은 왜 필요해?
A. JWT 서명이 유효하더라도 로그아웃, 강제 만료, 탈취 대응을 위해 서버 저장소의 tokenHash와 일치하는지 확인해야 한다.

Q. Refresh Token은 어디에 담아 보내?
A. Request Body, HttpOnly Cookie, Header 방식이 가능하며 Frontend Auth 정책과 보안 요구사항에 맞게 선택한다.

Q. Reissue Response에 Refresh Token도 다시 줘야 해?
A. Rotation을 사용한다면 새 Refresh Token을 반환해야 한다. Rotation을 사용하지 않으면 Access Token만 반환할 수 있다.

Q. Refresh Token을 Authorization Header에 보내도 돼?
A. 가능하지만 Access Token과 혼동되지 않도록 tokenType 검증과 API 규칙을 명확히 해야 한다.

Q. Refresh Token이 틀리면 어떤 응답을 줘?
A. 인증 실패로 보고 401 계열 응답을 주는 것이 일반적이다. 상세 메시지는 보안상 과도하게 노출하지 않는다.

Q. Refresh Token이 만료되면 어떻게 해?
A. 새 Access Token을 발급할 수 없으므로 Client는 Token을 제거하고 재로그인을 요구해야 한다.

Q. 저장소 Token과 요청 Token이 다르면 어떻게 해?
A. 탈취 가능성을 고려해 401로 차단하고 해당 사용자 또는 기기 Token 무효화를 검토한다.

Q. 저장소 tokenHash와 요청 Token이 다르면 어떻게 해?
A. 저장된 Refresh Token과 요청 Token이 일치하지 않는 것이므로 401로 차단하고 탈취 또는 재사용 가능성을 검토한다.

Q. Token은 어디에 저장하는 게 좋아?
A. 정답은 없다. XSS, CSRF, UX, 구현 복잡도를 고려해 Frontend Auth Flow와 함께 결정해야 한다.

Q. LocalStorage에 Token을 저장해도 돼?
A. 구현은 쉽지만 XSS에 취약하므로 위험을 이해하고 사용해야 한다.

Q. HttpOnly Cookie가 무조건 안전해?
A. JS 접근은 막을 수 있지만 CSRF와 SameSite, Secure 설정을 함께 검토해야 한다.

Q. Access Token도 DB에 저장해야 해?
A. 일반적인 Stateless JWT 구조에서는 Access Token을 DB에 저장하지 않는다.

Q. Refresh Token hash 저장은 왜 해?
A. 저장소가 유출되었을 때 Refresh Token 원문 악용 위험을 줄이기 위해서다.

Q. 단일 기기 로그인과 다중 기기 로그인은 Token 저장이 달라?
A. 다르다. 단일 기기는 userId 기준 1개, 다중 기기는 userId + deviceId 기준 여러 개를 관리할 수 있다.

Q. Refresh Token 원문 저장은 금지야?
A. 반드시 기술적으로 불가능한 것은 아니지만 권장하지 않는다. 보안 기준에서는 hash 저장을 우선 검토한다.

Q. Token Expired와 Token Invalid는 뭐가 달라?
A. Expired는 만료 시간이 지난 것이고 Invalid는 서명, 형식, 타입, 저장소 일치 여부 등이 잘못되어 신뢰할 수 없는 상태다.

Q. Access Token 만료는 어떤 errorCode가 좋아?
A. Frontend 재발급 판단을 위해 TOKEN_EXPIRED 같은 구분 가능한 errorCode를 사용할 수 있다.

Q. 위조 Token도 TOKEN_EXPIRED로 처리해도 돼?
A. 권장하지 않는다. 위조나 형식 오류는 UNAUTHORIZED 또는 TOKEN_INVALID처럼 구분하는 것이 좋다.

Q. Token Error Response도 ApiResponse 형식으로 맞춰야 해?
A. 프로젝트 응답 규칙이 있다면 맞추는 것이 Frontend 처리에 좋다.

Q. Access Token 만료와 Refresh Token 만료 errorCode를 분리해야 해?
A. Frontend 처리 흐름이 다르므로 분리하는 것이 좋다.

Q. JWT 예외는 GlobalExceptionHandler에서 처리돼?
A. Filter Chain에서 발생한 예외는 AuthenticationEntryPoint에서 처리되는 경우가 많다.

Q. JWT 검수에서 가장 중요한 것은 뭐야?
A. Payload 민감정보 금지, 서명/만료 검증, Access/Refresh 역할 분리, Refresh Token hash 저장/무효화, SecurityContext 저장이다.

Q. JWT 테스트에서 위조 Token은 어떻게 만들어?
A. 정상 JWT 문자열 일부를 변경해 Signature 검증 실패가 401로 처리되는지 확인하면 된다.

Q. 로그아웃 후 Reissue가 성공하면 문제야?
A. 문제다. Refresh Token 무효화 또는 저장소 검증이 제대로 동작하지 않는 것이다.

Q. Refresh Token hash 불일치 테스트도 필요해?
A. 필요하다. 저장소 Token과 요청 Token이 다를 때 Reissue가 401로 차단되는지 확인해야 한다.

Q. Part04에서 가장 중요한 주제는 뭐야?
A. JWT 구조, Access Token 검증, Refresh Token hash 저장, Token Reissue, Token Error Response다.

Q. Part04는 Login 문서와 어떻게 연결돼?
A. Login에서 비밀번호 검증이 성공하면 Access Token과 Refresh Token을 발급하는 흐름으로 연결된다.

Q. Part04는 Logout 문서와 어떻게 연결돼?
A. Logout에서 Refresh Token을 무효화해야 Reissue가 차단된다.

Q. Part04는 SecurityFilterChain 문서와 어떻게 연결돼?
A. SecurityFilterChain에 등록된 JWT Filter가 Access Token을 검증하고 SecurityContext에 Authentication을 저장한다.
