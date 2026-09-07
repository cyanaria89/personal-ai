# Security Advanced Part03 - Password, Login, Logout

---

# 1. Password Security Overview

## 1.1 Password Security Concept

### [개념]

Password Security는 사용자 비밀번호를 안전하게 저장하고 검증하기 위한 Backend 보안 기준이다.

Spring Security 기반 Backend에서는 비밀번호를 평문으로 저장하지 않고 `PasswordEncoder`를 사용해 단방향 해시로 저장해야 한다.

---

### [핵심]

Password Security 핵심 키워드:

- PasswordEncoder
- BCryptPasswordEncoder
- encode
- matches
- raw password
- encoded password
- one-way hash
- salt
- password storage
- password verification
- password reset
- no plain password

비밀번호 보안 원칙:

- 평문 저장 금지
- 평문 로그 출력 금지
- 단방향 해시 저장
- 로그인 검증 시 `matches` 사용
- 비밀번호 찾기 시 기존 비밀번호 반환 금지
- 비밀번호 변경 시 재해시 저장

---

### [실무]

2026 실무 기준에서 비밀번호는 반드시 단방향 해시로 저장한다.

회원가입 흐름:

```text
SignUp Request
→ raw password 입력
→ PasswordEncoder.encode
→ encoded password 저장
→ User 생성 완료
```

로그인 흐름:

```text
Login Request
→ raw password 입력
→ User 조회
→ PasswordEncoder.matches(raw, encoded)
→ 인증 성공 또는 실패
```

주의:

- `encode(rawPassword).equals(encodedPassword)` 비교 금지
- BCrypt는 같은 비밀번호도 매번 다른 해시가 나올 수 있음
- 로그인 검증은 반드시 `passwordEncoder.matches(raw, encoded)` 사용
- 비밀번호를 응답 DTO에 포함하지 않음
- 비밀번호를 로그에 출력하지 않음

---

### [FAQ]

Q. 비밀번호는 어떻게 저장해야 해?
A. BCrypt 같은 PasswordEncoder로 단방향 해시 처리해 저장해야 한다.

Q. 비밀번호를 평문으로 저장하면 안 돼?
A. 안 된다. DB 유출 시 모든 계정이 즉시 위험해지므로 평문 저장은 심각한 보안 Anti Pattern이다.

Q. 로그인할 때 encode해서 DB 값과 비교하면 돼?
A. 안 된다. BCrypt는 매번 다른 해시가 나올 수 있으므로 `matches(raw, encoded)`로 비교해야 한다.

---

# 2. PasswordEncoder Rules

## 2.1 PasswordEncoder Concept

### [개념]

`PasswordEncoder`는 비밀번호를 단방향 해시로 변환하고 로그인 시 입력 비밀번호와 저장된 해시 값을 비교하는 Spring Security 컴포넌트다.

대표 구현체로 `BCryptPasswordEncoder`를 사용할 수 있다.

---

### [핵심]

PasswordEncoder 주요 메서드:

- `encode(rawPassword)`
- `matches(rawPassword, encodedPassword)`

주요 구현체:

- BCryptPasswordEncoder
- DelegatingPasswordEncoder
- Argon2PasswordEncoder
- Pbkdf2PasswordEncoder

기본 권장:

```text
BCryptPasswordEncoder
```

---

### [실무]

Bean 등록 예:

```java
@Bean
public PasswordEncoder passwordEncoder() {
    return new BCryptPasswordEncoder();
}
```

회원가입 사용 예:

```java
String encodedPassword = passwordEncoder.encode(request.password());

User user = User.builder()
        .email(request.email())
        .password(encodedPassword)
        .role(Role.USER)
        .build();
```

로그인 검증 예:

```java
if (!passwordEncoder.matches(request.password(), user.getPassword())) {
    throw new BusinessException("INVALID_LOGIN", "아이디 또는 비밀번호가 올바르지 않습니다.");
}
```

권장:

- `PasswordEncoder`는 Bean으로 등록한다.
- Service에서 주입받아 사용한다.
- 회원가입, 비밀번호 변경, 임시 비밀번호 저장 시 encode한다.
- 로그인 검증 시 matches를 사용한다.
- 테스트 코드에서도 동일한 PasswordEncoder 기준을 사용한다.

---

### [FAQ]

Q. PasswordEncoder는 왜 필요해?
A. 비밀번호를 평문으로 저장하지 않고 안전한 단방향 해시로 저장하기 위해 필요하다.

Q. BCryptPasswordEncoder를 써도 돼?
A. 일반적인 Spring Boot Backend에서는 BCryptPasswordEncoder를 기본 선택지로 사용할 수 있다.

Q. PasswordEncoder는 어디에 등록해?
A. 보통 SecurityConfig 또는 별도 Config에서 Bean으로 등록한다.

Q. 비밀번호 변경 시에도 encode해야 해?
A. 반드시 해야 한다. 새 비밀번호도 평문이 아니라 해시 값으로 저장해야 한다.

---

## 2.2 Password Verification Rules

### [개념]

Password Verification은 로그인 요청의 raw password와 DB에 저장된 encoded password를 비교해 사용자의 인증 여부를 판단하는 과정이다.

---

### [핵심]

검증 입력:

- raw password
- encoded password

검증 메서드:

```java
passwordEncoder.matches(rawPassword, encodedPassword)
```

검증 실패 응답:

```text
HTTP 401 Unauthorized
errorCode: INVALID_LOGIN
message: 아이디 또는 비밀번호가 올바르지 않습니다.
```

---

### [실무]

로그인 검증 흐름:

```text
Login Request
→ email 조회
→ User 존재 여부 확인
→ passwordEncoder.matches
→ 실패 시 인증 실패
→ 성공 시 Token 발급
```

예:

```java
User user = userRepository.findByEmail(request.email())
        .orElseThrow(() -> new BusinessException(
                "INVALID_LOGIN",
                "아이디 또는 비밀번호가 올바르지 않습니다."
        ));

if (!passwordEncoder.matches(request.password(), user.getPassword())) {
    throw new BusinessException(
            "INVALID_LOGIN",
            "아이디 또는 비밀번호가 올바르지 않습니다."
    );
}
```

권장:

- 이메일 없음과 비밀번호 불일치 메시지를 과도하게 구분하지 않는다.
- 로그인 실패 사유를 상세히 노출하지 않는다.
- 실패 횟수 제한 또는 잠금 정책을 검토할 수 있다.
- 탈퇴 / 정지 사용자 로그인 차단 기준을 둔다.
- 비밀번호 비교는 PasswordEncoder에 위임한다.

---

### [FAQ]

Q. 로그인 실패 시 이메일 없음과 비밀번호 오류를 구분해도 돼?
A. 보안상 과도하게 구분하지 않는 것이 좋다. 계정 존재 여부가 노출될 수 있다.

Q. matches의 첫 번째 인자는 뭐야?
A. 사용자가 입력한 raw password다.

Q. matches의 두 번째 인자는 뭐야?
A. DB에 저장된 encoded password다.

Q. 비밀번호 검증 실패는 401이야 403이야?
A. 인증 실패이므로 일반적으로 401 Unauthorized 계열로 처리한다.

---

## 2.3 Password Anti Pattern

### [개념]

Password Anti Pattern은 비밀번호 저장, 검증, 응답, 로그 처리에서 발생하는 잘못된 보안 구현이다.

---

### [핵심]

대표 Anti Pattern:

- 비밀번호 평문 저장
- 비밀번호 평문 로그 출력
- 비밀번호를 응답 DTO에 포함
- `encode(raw).equals(encoded)` 비교
- `matches` 미사용
- 비밀번호 찾기에서 기존 비밀번호 반환
- 기본 비밀번호를 고정값으로 발급
- 임시 비밀번호를 장기간 유지
- 관리자 화면에서 사용자 비밀번호 조회 허용
- Token Claim에 비밀번호 포함

---

### [실무]

잘못된 예:

```java
if (passwordEncoder.encode(request.password()).equals(user.getPassword())) {
    // login success
}
```

수정 예:

```java
if (passwordEncoder.matches(request.password(), user.getPassword())) {
    // login success
}
```

잘못된 응답 예:

```java
public record UserResponse(
        Long userId,
        String email,
        String password
) {
}
```

수정 예:

```java
public record UserResponse(
        Long userId,
        String email,
        String nickname
) {
}
```

Review 기준:

```text
Entity password 필드 확인
→ DTO password 노출 여부 확인
→ 로그 출력 확인
→ encode / matches 사용 확인
→ 비밀번호 찾기 / 변경 로직 확인
```

---

### [FAQ]

Q. 비밀번호를 응답 DTO에 넣어도 돼?
A. 안 된다. 비밀번호 해시라도 외부 응답으로 노출하면 안 된다.

Q. 비밀번호를 로그로 찍어도 돼?
A. 안 된다. raw password, encoded password 모두 로그 출력 금지 대상이다.

Q. 비밀번호 찾기에서 기존 비밀번호를 알려줘도 돼?
A. 안 된다. 비밀번호는 복호화할 수 없어야 하며 재설정 방식으로 처리해야 한다.

---

# 3. Login Flow Rules

## 3.1 Login Flow Concept

### [개념]

Login Flow는 사용자의 자격 증명을 검증하고 인증 성공 시 Access Token과 Refresh Token 또는 Session을 발급하는 과정이다.

JWT 기반 REST API에서는 로그인 성공 후 Access Token과 Refresh Token을 발급하는 구조를 자주 사용한다.

---

### [핵심]

Login Flow 핵심 키워드:

- Login Request
- email
- password
- PasswordEncoder.matches
- Authentication
- Access Token
- Refresh Token
- Login Response
- SecurityContext
- Invalid Login
- 401 Unauthorized

JWT Login Flow:

```text
Login Request
→ email / password 검증
→ User 조회
→ PasswordEncoder.matches
→ User 상태 확인
→ Access Token 생성
→ Refresh Token 생성
→ Refresh Token 저장
→ Login Response
```

---

### [실무]

Login Service 예:

```java
@Transactional
public LoginResponse login(LoginRequest request) {
    User user = userRepository.findByEmail(request.email())
            .orElseThrow(() -> new BusinessException(
                    "INVALID_LOGIN",
                    "아이디 또는 비밀번호가 올바르지 않습니다."
            ));

    if (!passwordEncoder.matches(request.password(), user.getPassword())) {
        throw new BusinessException(
                "INVALID_LOGIN",
                "아이디 또는 비밀번호가 올바르지 않습니다."
        );
    }

    validateLoginAllowed(user);

    String accessToken = jwtTokenProvider.createAccessToken(user.getId(), user.getRole());
    String refreshToken = jwtTokenProvider.createRefreshToken(user.getId());

    refreshTokenService.saveOrUpdate(user.getId(), refreshToken);

    return new LoginResponse(accessToken, refreshToken, user.getId(), user.getRole());
}
```

권장:

- 로그인 요청 DTO에는 email / password만 최소 포함한다.
- 로그인 실패 메시지는 과도하게 상세히 노출하지 않는다.
- 탈퇴 / 정지 / 휴면 계정 상태를 확인한다.
- Access Token은 짧은 만료 시간을 사용한다.
- Refresh Token은 서버 저장소에 저장을 검토한다.
- Token 원문을 로그로 남기지 않는다.

---

### [FAQ]

Q. 로그인 성공하면 뭘 반환해?
A. JWT 구조에서는 Access Token, Refresh Token, 사용자 요약 정보를 반환할 수 있다.

Q. 로그인 실패 이유를 자세히 알려줘도 돼?
A. 보안상 이메일 존재 여부나 비밀번호 오류를 과도하게 구분하지 않는 것이 좋다.

Q. 로그인 성공 시 SecurityContext에 저장해야 해?
A. 전통 Form Login에서는 저장되지만 JWT REST API에서는 이후 요청마다 JWT Filter가 검증해 SecurityContext에 저장하는 구조가 일반적이다.

---

## 3.2 Login Request Rules

### [개념]

Login Request는 사용자가 인증을 위해 서버에 전달하는 자격 증명 요청이다.

일반적으로 email 또는 username과 password를 포함한다.

---

### [핵심]

Login Request 포함 후보:

- email
- username
- password

Login Request 제외 후보:

- role
- userId
- authority
- accountStatus
- accessToken
- refreshToken

DTO 예:

```java
public record LoginRequest(
        String email,
        String password
) {
}
```

---

### [실무]

Validation 예:

```java
public record LoginRequest(
        @NotBlank
        @Email
        String email,

        @NotBlank
        String password
) {
}
```

권장:

- email 형식을 검증한다.
- password blank를 검증한다.
- role, userId는 요청에서 받지 않는다.
- 로그인 요청의 권한 정보는 신뢰하지 않는다.
- 로그인 실패 시 입력 password를 로그에 남기지 않는다.
- Brute Force 방어를 위해 실패 횟수 제한을 검토할 수 있다.

잘못된 예:

```java
public record LoginRequest(
        String email,
        String password,
        String role
) {
}
```

문제:

```text
Client가 role을 조작할 수 있으므로 Login Request에서 role을 받으면 안 된다.
```

---

### [FAQ]

Q. Login Request에 role을 넣어도 돼?
A. 안 된다. 권한은 서버에 저장된 사용자 정보 기준으로 판단해야 한다.

Q. Login Request에 userId를 넣어도 돼?
A. 일반적으로 필요 없다. email 또는 username으로 사용자를 조회하고 서버에서 userId를 판단한다.

Q. 로그인 요청 DTO에 Validation이 필요해?
A. 필요하다. email 형식과 password blank 여부를 검증하는 것이 좋다.

---

## 3.3 Login Response Rules

### [개념]

Login Response는 인증 성공 후 Client가 인증 상태를 유지하고 사용자 정보를 표시할 수 있도록 반환하는 응답이다.

JWT 기반 구조에서는 Access Token, Refresh Token, 사용자 요약 정보를 포함할 수 있다.

---

### [핵심]

Login Response 포함 후보:

- accessToken
- refreshToken
- tokenType
- expiresIn
- userId
- email
- nickname
- role

Login Response 제외 후보:

- password
- encodedPassword
- secretKey
- internal token id
- 민감 개인정보
- 불필요한 User Entity 전체

---

### [실무]

Login Response 예:

```java
public record LoginResponse(
        String accessToken,
        String refreshToken,
        String tokenType,
        Long expiresIn,
        Long userId,
        String email,
        String role
) {
}
```

응답 예:

```json
{
  "accessToken": "access-token-value",
  "refreshToken": "refresh-token-value",
  "tokenType": "Bearer",
  "expiresIn": 1800,
  "userId": 1,
  "email": "user@example.com",
  "role": "ROLE_USER"
}
```

권장:

- Token Type을 명확히 제공한다.
- Access Token 만료 시간을 제공할 수 있다.
- 사용자 정보는 화면 표시와 권한 판단에 필요한 최소 정보만 반환한다.
- 비밀번호와 내부 보안 값은 절대 반환하지 않는다.
- Refresh Token을 응답 Body로 줄지 Cookie로 줄지는 Frontend Auth 정책과 함께 결정한다.

---

### [FAQ]

Q. Login Response에 Refresh Token을 포함해도 돼?
A. 가능하다. 다만 저장 위치, XSS, CSRF, Cookie 정책을 Frontend Auth Flow와 함께 검토해야 한다.

Q. Login Response에 사용자 role을 포함해도 돼?
A. UI 표시와 권한 UX를 위해 포함할 수 있지만 Backend 권한 검증을 대체하지 않는다.

Q. Login Response에 password hash를 포함해도 돼?
A. 안 된다. 해시 값이라도 응답에 포함하면 안 된다.

---

# 4. Login Failure Rules

## 4.1 Invalid Login Handling

### [개념]

Invalid Login Handling은 로그인 실패 시 응답 상태, errorCode, message를 일관되게 처리하는 기준이다.

로그인 실패는 인증 실패이며 일반적으로 401 Unauthorized 계열로 처리한다.

---

### [핵심]

로그인 실패 원인:

- email 없음
- password 불일치
- 탈퇴 사용자
- 정지 사용자
- 휴면 사용자
- OAuth2 전용 계정
- 인증 방식 불일치

권장 응답:

```text
HTTP 401 Unauthorized
errorCode: INVALID_LOGIN
message: 아이디 또는 비밀번호가 올바르지 않습니다.
```

---

### [실무]

실패 메시지 통일 예:

```java
private BusinessException invalidLoginException() {
    return new BusinessException(
            "INVALID_LOGIN",
            "아이디 또는 비밀번호가 올바르지 않습니다."
    );
}
```

사용 예:

```java
User user = userRepository.findByEmail(request.email())
        .orElseThrow(this::invalidLoginException);

if (!passwordEncoder.matches(request.password(), user.getPassword())) {
    throw invalidLoginException();
}
```

권장:

- email 없음과 password 오류를 같은 메시지로 처리한다.
- 실패 횟수 제한을 검토한다.
- 계정 잠금 정책을 검토한다.
- IP / User-Agent 기반 이상 시도를 로깅할 수 있다.
- 비밀번호와 Token 원문은 로깅하지 않는다.

주의:

- 탈퇴 / 정지 계정 메시지는 정책에 따라 분리 가능하지만 계정 상태 노출 위험을 검토한다.
- Frontend가 처리 가능한 errorCode를 제공한다.
- 보안상 상세 원인은 서버 로그에만 남긴다.

---

### [FAQ]

Q. 로그인 실패는 401이 맞아?
A. 일반적으로 인증 실패이므로 401 Unauthorized 계열이 맞다.

Q. 이메일이 없는 경우와 비밀번호가 틀린 경우를 구분해도 돼?
A. 보안상 계정 존재 여부가 노출될 수 있으므로 일반 로그인 실패 메시지로 통일하는 것이 좋다.

Q. 로그인 실패 횟수 제한이 필요해?
A. Brute Force 방어를 위해 실패 횟수 제한, 지연 응답, 계정 잠금 정책을 검토할 수 있다.

---

## 4.2 Account Status Check

### [개념]

Account Status Check는 로그인 시 사용자의 계정 상태가 인증을 허용할 수 있는 상태인지 확인하는 과정이다.

비밀번호가 맞더라도 탈퇴, 정지, 휴면, 이메일 미인증 상태에 따라 로그인을 제한할 수 있다.

---

### [핵심]

계정 상태 후보:

- ACTIVE
- WITHDRAWN
- SUSPENDED
- DORMANT
- PENDING_EMAIL_VERIFICATION
- LOCKED
- OAUTH_ONLY

상태 검증 시점:

```text
User 조회
→ Password 검증
→ Account Status 확인
→ Token 발급
```

---

### [실무]

계정 상태 검증 예:

```java
private void validateLoginAllowed(User user) {
    if (user.isWithdrawn()) {
        throw new BusinessException("ACCOUNT_DISABLED", "로그인할 수 없는 계정입니다.");
    }

    if (user.isSuspended()) {
        throw new BusinessException("ACCOUNT_SUSPENDED", "로그인이 제한된 계정입니다.");
    }

    if (user.isLocked()) {
        throw new BusinessException("ACCOUNT_LOCKED", "계정이 잠겼습니다.");
    }
}
```

권장:

- User Entity에 상태 값을 명확히 둔다.
- 로그인 가능 상태와 불가능 상태를 분리한다.
- Token 발급 전 상태 검증을 수행한다.
- 정지 / 탈퇴 사용자의 Refresh Token도 무효화할 수 있다.
- 정책상 필요한 경우 이메일 인증 전 로그인 제한을 적용한다.

주의:

- 계정 상태 메시지가 과도하게 상세하면 사용자 정보가 노출될 수 있다.
- 관리자 정지와 사용자 탈퇴 상태는 도메인 정책에 따라 구분한다.
- 상태 변경 시 기존 Refresh Token 무효화를 검토한다.

---

### [FAQ]

Q. 비밀번호가 맞으면 무조건 로그인시켜도 돼?
A. 아니다. 탈퇴, 정지, 잠금, 이메일 미인증 같은 계정 상태를 확인해야 한다.

Q. 정지된 사용자는 Token 발급을 막아야 해?
A. 일반적으로 막아야 한다. 필요하면 기존 Refresh Token도 무효화한다.

Q. 이메일 인증 전 로그인을 허용할지는 어디서 정해?
A. 프로젝트 정책에서 정하고 Login Flow 또는 Authorization 정책에 반영한다.

---

# 5. Token Issue After Login

## 5.1 Access Token Issue Rules

### [개념]

Access Token Issue는 로그인 성공 후 Client가 Protected API에 접근할 수 있도록 짧은 수명의 Access Token을 발급하는 과정이다.

Access Token은 API 요청의 Authorization Header에 Bearer Token으로 전달된다.

---

### [핵심]

Access Token Claim 후보:

- subject
- userId
- role
- authority
- issuedAt
- expiration

Access Token 제외 Claim:

- password
- refreshToken
- phoneNumber
- address
- 주민등록번호
- 민감 개인정보

---

### [실무]

Access Token 생성 흐름:

```text
Login Success
→ userId 확인
→ role 확인
→ Access Token Claims 구성
→ 만료 시간 설정
→ 서명
→ Login Response 포함
```

예:

```java
String accessToken = jwtTokenProvider.createAccessToken(
        user.getId(),
        user.getRole()
);
```

권장:

- Access Token 만료 시간은 짧게 설정한다.
- Claim에는 최소 정보만 포함한다.
- 서명 Secret 또는 Private Key를 안전하게 관리한다.
- Token 원문을 로그에 남기지 않는다.
- HTTPS 사용을 전제로 한다.
- Client는 Authorization Header에 Bearer 형식으로 전송한다.

---

### [FAQ]

Q. Access Token에는 뭘 넣어야 해?
A. userId, role, 만료 시간처럼 인증과 권한 판단에 필요한 최소 정보만 넣는 것이 좋다.

Q. Access Token 만료 시간은 짧게 해야 해?
A. 일반적으로 짧게 설정해 탈취 시 피해 시간을 줄이고 Refresh Token으로 재발급하는 구조를 사용한다.

Q. Access Token에 개인정보를 많이 넣어도 돼?
A. 권장하지 않는다. JWT Payload는 디코딩 가능하므로 민감정보를 넣으면 안 된다.

---

## 5.2 Refresh Token Issue Rules

### [개념]

Refresh Token Issue는 Access Token이 만료되었을 때 새 Access Token을 발급받을 수 있도록 긴 수명의 Refresh Token을 발급하는 과정이다.

Refresh Token은 로그아웃, 강제 만료, 탈취 대응을 위해 서버 저장소에 저장하는 구조를 검토한다.

---

### [핵심]

Refresh Token 특징:

- Long Expiration
- Token Reissue
- Server-side Storage
- Rotation
- Logout Invalidation
- Device Session
- Theft Detection

저장소 후보:

- Database
- Redis
- Secure Cookie
- Token Store

---

### [실무]

Refresh Token 생성 흐름:

```text
Login Success
→ Refresh Token 생성
→ 사용자 / 기기 정보와 연결
→ DB 또는 Redis 저장
→ Login Response 또는 Cookie 전달
```

예:

```java
String refreshToken = jwtTokenProvider.createRefreshToken(user.getId());

refreshTokenService.saveOrUpdate(
        user.getId(),
        refreshToken
);
```

권장:

- Refresh Token은 Access Token보다 길게 설정한다.
- 서버 저장소 저장을 검토한다.
- 로그아웃 시 삭제 또는 무효화한다.
- 재발급 시 Rotation을 검토한다.
- 사용자 / 기기 단위 관리가 필요하면 deviceId를 함께 저장한다.
- 탈취 의심 시 전체 Refresh Token 무효화를 고려한다.

주의:

- Refresh Token도 탈취되면 위험하다.
- 저장 위치와 전송 방식은 Frontend Auth Flow와 함께 결정한다.
- Cookie 저장 시 CSRF / SameSite / HttpOnly / Secure를 검토한다.
- LocalStorage 저장 시 XSS 위험을 검토한다.

---

### [FAQ]

Q. Refresh Token은 왜 필요해?
A. Access Token을 짧게 유지하면서 사용자가 자주 로그인하지 않도록 새 Access Token을 발급하기 위해 필요하다.

Q. Refresh Token도 DB에 저장해야 해?
A. 로그아웃, 강제 만료, 탈취 대응이 필요하면 DB나 Redis 같은 서버 저장소에 저장하는 것이 좋다.

Q. Refresh Token은 Access Token보다 길게 설정해?
A. 일반적으로 Access Token보다 긴 만료 시간을 사용한다.

---

# 6. Logout Rules

## 6.1 Logout Concept

### [개념]

Logout은 사용자의 인증 상태를 종료하고 Refresh Token 또는 Session 정보를 무효화하는 과정이다.

JWT Stateless 구조에서는 Access Token을 즉시 무효화하기 어렵기 때문에 Refresh Token 삭제와 Access Token 짧은 만료 시간 전략을 함께 사용한다.

---

### [핵심]

JWT Logout 핵심 키워드:

- Logout
- Refresh Token Delete
- Refresh Token Invalidation
- Access Token Expiration
- Token Blacklist
- Client Token Remove
- SecurityContext clear
- Device Logout
- Global Logout

JWT Logout Flow:

```text
Logout Request
→ 인증 사용자 확인
→ 저장된 Refresh Token 삭제 또는 무효화
→ Client Token 제거 안내
→ Response
```

---

### [실무]

Logout Service 예:

```java
@Transactional
public void logout(Long userId) {
    refreshTokenRepository.deleteByUserId(userId);
}
```

Controller 예:

```java
@PostMapping("/logout")
public ApiResponse<Void> logout(
        @AuthenticationPrincipal CustomUserPrincipal principal
) {
    authService.logout(principal.userId());
    return ApiResponse.success();
}
```

권장:

- Logout API는 Protected API로 처리한다.
- 인증된 Principal 기준으로 로그아웃 처리한다.
- RequestBody userId를 신뢰하지 않는다.
- 서버 저장 Refresh Token을 삭제하거나 무효화한다.
- Client는 Access Token / Refresh Token을 제거한다.
- Access Token은 짧은 만료 시간으로 위험을 완화한다.

---

### [FAQ]

Q. JWT 로그아웃은 서버에서 바로 Access Token을 무효화할 수 있어?
A. 기본 Stateless JWT는 어렵다. Blacklist를 쓰거나 Access Token 만료 시간을 짧게 두고 Refresh Token을 무효화하는 방식이 일반적이다.

Q. 로그아웃 시 Refresh Token은 삭제해야 해?
A. 서버에 저장한 Refresh Token이 있다면 삭제하거나 무효화하는 것이 좋다.

Q. Logout API는 인증이 필요해?
A. 일반적으로 필요하다. 현재 로그인한 사용자의 Refresh Token을 무효화해야 하기 때문이다.

---

## 6.2 Device Logout and Global Logout

### [개념]

Device Logout은 특정 기기 또는 특정 Refresh Token만 무효화하는 로그아웃 방식이다.

Global Logout은 사용자의 모든 기기 Refresh Token을 무효화하는 로그아웃 방식이다.

---

### [핵심]

Device Logout:

- 현재 기기만 로그아웃
- 특정 refreshToken 삭제
- deviceId 기준 삭제
- sessionId 기준 삭제

Global Logout:

- 모든 기기 로그아웃
- userId 기준 전체 Refresh Token 삭제
- 비밀번호 변경 시 사용 가능
- 계정 탈취 의심 시 사용 가능

---

### [실무]

Device Logout Flow:

```text
Logout Request
→ userId 확인
→ deviceId 또는 refreshToken 확인
→ 해당 Refresh Token 삭제
→ 현재 기기 로그아웃
```

Global Logout Flow:

```text
Global Logout Request
→ userId 확인
→ userId 기준 모든 Refresh Token 삭제
→ 모든 기기 재로그인 요구
```

Repository 예:

```java
void deleteByUserId(Long userId);

void deleteByUserIdAndDeviceId(Long userId, String deviceId);
```

권장:

- 단일 기기 로그인만 지원하면 userId 기준 삭제로 충분할 수 있다.
- 다중 기기 로그인을 지원하면 deviceId 또는 tokenId 관리가 필요하다.
- 비밀번호 변경 후 전체 로그아웃을 검토한다.
- 계정 정지 / 탈퇴 시 모든 Refresh Token을 삭제한다.
- 관리자 강제 로그아웃 정책을 별도로 둘 수 있다.

---

### [FAQ]

Q. 다중 기기 로그인을 지원하려면 Refresh Token을 어떻게 저장해?
A. userId와 deviceId 또는 tokenId를 함께 저장해 기기별로 관리하는 것이 좋다.

Q. 비밀번호 변경 후 모든 기기에서 로그아웃시켜야 해?
A. 보안상 권장된다. 비밀번호 변경 시 모든 Refresh Token을 삭제하면 된다.

Q. 현재 기기만 로그아웃하려면 어떻게 해?
A. 현재 요청의 Refresh Token 또는 deviceId 기준으로 해당 Token만 삭제한다.

---

## 6.3 Logout Anti Pattern

### [개념]

Logout Anti Pattern은 JWT 구조에서 Token 무효화 전략 없이 Client Token 삭제만 의존하거나 Access Token 장기 만료를 사용하는 잘못된 로그아웃 설계다.

---

### [핵심]

대표 Anti Pattern:

- Refresh Token을 서버에 저장하지 않음
- 로그아웃 시 Client에서만 Token 삭제
- Access Token 만료 시간이 과도하게 김
- Refresh Token 삭제 로직 없음
- 비밀번호 변경 후 기존 Token 유지
- 탈퇴 / 정지 후 Refresh Token 유지
- Token Blacklist를 무분별하게 사용
- RequestBody userId로 로그아웃 처리

---

### [실무]

잘못된 예:

```java
@PostMapping("/logout")
public ApiResponse<Void> logout(@RequestBody LogoutRequest request) {
    authService.logout(request.userId());
    return ApiResponse.success();
}
```

문제:

```text
RequestBody userId는 조작 가능하므로 다른 사용자의 로그아웃을 유도할 수 있다.
```

수정 예:

```java
@PostMapping("/logout")
public ApiResponse<Void> logout(
        @AuthenticationPrincipal CustomUserPrincipal principal
) {
    authService.logout(principal.userId());
    return ApiResponse.success();
}
```

Review 기준:

```text
Logout API 인증 필요 여부 확인
→ Principal 기준 처리 확인
→ Refresh Token 삭제 여부 확인
→ Access Token 만료 시간 확인
→ 비밀번호 변경 / 탈퇴 시 Token 무효화 확인
```

---

### [FAQ]

Q. 로그아웃을 Client Token 삭제만으로 처리해도 돼?
A. 부족하다. 서버에 저장된 Refresh Token이 있다면 반드시 삭제하거나 무효화해야 한다.

Q. RequestBody userId로 로그아웃 처리해도 돼?
A. 안 된다. 인증 Principal의 userId를 기준으로 처리해야 한다.

Q. Access Token 만료 시간이 길면 왜 위험해?
A. 탈취된 Access Token이 오래 유효하게 남아 로그아웃 후에도 API 접근에 사용될 수 있기 때문이다.

---

# 7. Password Reset and Change Rules

## 7.1 Password Change Rules

### [개념]

Password Change는 로그인한 사용자가 기존 비밀번호를 확인한 뒤 새 비밀번호로 변경하는 기능이다.

비밀번호 변경 시 새 비밀번호는 반드시 PasswordEncoder로 다시 해시 처리해 저장한다.

---

### [핵심]

Password Change Flow:

```text
Authenticated User
→ Current Password 입력
→ PasswordEncoder.matches 검증
→ New Password 정책 검증
→ PasswordEncoder.encode
→ Password Update
→ 기존 Refresh Token 무효화 검토
```

필수 검증:

- 인증 사용자 확인
- 현재 비밀번호 확인
- 새 비밀번호 형식 검증
- 새 비밀번호 재확인
- 기존 비밀번호와 동일 여부 검토
- Refresh Token 무효화 여부 검토

---

### [실무]

Service 예:

```java
@Transactional
public void changePassword(
        Long currentUserId,
        PasswordChangeRequest request
) {
    User user = userRepository.findById(currentUserId)
            .orElseThrow(() -> new BusinessException("USER_NOT_FOUND", "사용자를 찾을 수 없습니다."));

    if (!passwordEncoder.matches(request.currentPassword(), user.getPassword())) {
        throw new BusinessException("INVALID_PASSWORD", "비밀번호가 올바르지 않습니다.");
    }

    user.changePassword(passwordEncoder.encode(request.newPassword()));

    refreshTokenRepository.deleteByUserId(currentUserId);
}
```

권장:

- `currentUserId`는 Principal에서 가져온다.
- RequestBody userId를 신뢰하지 않는다.
- 현재 비밀번호를 확인한다.
- 새 비밀번호는 encode 후 저장한다.
- 비밀번호 변경 후 모든 Refresh Token 삭제를 검토한다.
- 변경 완료 후 재로그인을 요구할 수 있다.

---

### [FAQ]

Q. 비밀번호 변경 시 현재 비밀번호 확인이 필요해?
A. 로그인한 사용자의 보안 강화를 위해 현재 비밀번호 확인을 요구하는 것이 일반적이다.

Q. 비밀번호 변경 후 Refresh Token을 삭제해야 해?
A. 보안상 권장된다. 기존 기기 세션을 모두 무효화하고 재로그인을 요구할 수 있다.

Q. 새 비밀번호도 encode해야 해?
A. 반드시 해야 한다. 모든 저장 비밀번호는 해시 값이어야 한다.

---

## 7.2 Password Reset Rules

### [개념]

Password Reset은 사용자가 비밀번호를 잊었을 때 이메일 인증, 재설정 Token, 임시 링크 등을 통해 새 비밀번호를 설정하게 하는 기능이다.

Password Reset은 기존 비밀번호를 알려주는 기능이 아니라 새 비밀번호로 재설정하는 기능이다.

---

### [핵심]

Password Reset Flow:

```text
Password Reset Request
→ email 입력
→ 사용자 존재 여부 확인
→ Reset Token 생성
→ Reset Token 저장
→ Email 발송
→ Reset Token 검증
→ New Password 입력
→ PasswordEncoder.encode
→ Password Update
→ Reset Token 무효화
→ Refresh Token 무효화
```

필수 요소:

- resetToken
- expiration
- used flag
- email verification
- one-time use
- password re-encode
- refresh token invalidation

---

### [실무]

Reset Token 검증 기준:

```text
Token 존재 여부
→ Token 만료 여부
→ Token 사용 여부
→ 사용자 상태 확인
→ 새 비밀번호 정책 검증
→ 비밀번호 변경
→ Token 사용 완료 처리
```

권장:

- 비밀번호 재설정 Token은 짧은 만료 시간을 둔다.
- Reset Token은 1회용으로 처리한다.
- 사용자 존재 여부를 응답에서 과도하게 노출하지 않는다.
- 새 비밀번호 저장 시 PasswordEncoder를 사용한다.
- 재설정 완료 후 기존 Refresh Token을 무효화한다.
- Reset Token 원문을 로그에 남기지 않는다.

응답 메시지 예:

```text
입력한 이메일로 비밀번호 재설정 안내가 발송됩니다.
```

주의:

- 이메일이 존재하지 않아도 같은 응답을 줄 수 있다.
- 기존 비밀번호를 이메일로 보내면 안 된다.
- 임시 비밀번호를 발급하더라도 즉시 변경 요구를 검토한다.

---

### [FAQ]

Q. 비밀번호 찾기에서 기존 비밀번호를 알려줘도 돼?
A. 안 된다. 비밀번호는 복호화할 수 없어야 하며 새 비밀번호 재설정 방식으로 처리해야 한다.

Q. Password Reset Token은 얼마나 유효해야 해?
A. 짧은 만료 시간을 두는 것이 좋다. 프로젝트 정책에 따라 다르지만 장기간 유효하면 위험하다.

Q. 비밀번호 재설정 후 기존 로그인은 유지해도 돼?
A. 보안상 기존 Refresh Token을 삭제해 모든 기기에서 재로그인하도록 하는 것이 좋다.

---

# 8. Login and Logout Testing

## 8.1 Login Test Rules

### [개념]

Login Test는 사용자 인증 흐름이 정상적으로 동작하고 실패 케이스가 안전하게 처리되는지 검증하는 과정이다.

---

### [핵심]

Login Test 대상:

- 정상 로그인
- 존재하지 않는 email
- 잘못된 password
- blank email
- blank password
- 탈퇴 사용자 로그인
- 정지 사용자 로그인
- Token 발급 확인
- Refresh Token 저장 확인
- password 로그 노출 여부 확인

---

### [실무]

테스트 시나리오:

```text
Valid email + Valid password
→ 200 OK
→ Access Token 발급
→ Refresh Token 발급
```

```text
Invalid email
→ 401 Unauthorized
→ INVALID_LOGIN
```

```text
Valid email + Invalid password
→ 401 Unauthorized
→ INVALID_LOGIN
```

```text
Suspended user
→ 401 또는 정책별 상태 코드
→ ACCOUNT_SUSPENDED
```

검증 기준:

- Access Token이 응답되는가?
- Refresh Token이 응답 또는 Cookie로 전달되는가?
- Refresh Token이 DB / Redis에 저장되는가?
- password가 응답에 포함되지 않는가?
- password가 로그에 남지 않는가?
- 실패 메시지가 계정 존재 여부를 노출하지 않는가?

---

### [FAQ]

Q. 로그인 테스트에서 가장 중요한 것은 뭐야?
A. 정상 로그인 Token 발급, 잘못된 비밀번호 실패, 계정 존재 여부 노출 방지, password 응답/로그 노출 방지다.

Q. 로그인 실패 테스트는 401을 보면 돼?
A. 일반적으로 401과 errorCode를 함께 확인하는 것이 좋다.

Q. Refresh Token 저장도 테스트해야 해?
A. 해야 한다. 재발급과 로그아웃 기능이 Refresh Token 저장 상태에 의존하기 때문이다.

---

## 8.2 Logout Test Rules

### [개념]

Logout Test는 로그아웃 시 Refresh Token이 정상적으로 삭제 또는 무효화되고 이후 재발급이 차단되는지 검증하는 과정이다.

---

### [핵심]

Logout Test 대상:

- 정상 로그아웃
- Token 없이 로그아웃
- 위조 Token으로 로그아웃
- 다른 사용자 userId 조작 시도
- Refresh Token 삭제 확인
- 로그아웃 후 재발급 차단
- Global Logout
- Device Logout

---

### [실무]

테스트 시나리오:

```text
Valid Access Token
→ Logout Request
→ 200 OK
→ Refresh Token 삭제
```

```text
No Token
→ Logout Request
→ 401 Unauthorized
```

```text
Logout 완료 후 Refresh Token으로 Reissue
→ 401 Unauthorized
→ REFRESH_TOKEN_INVALID
```

```text
RequestBody userId 조작
→ Principal userId 기준 처리
→ 다른 사용자 Token 삭제 불가
```

검증 기준:

- Logout API가 Protected API인가?
- Principal 기준으로 처리하는가?
- Refresh Token이 삭제되는가?
- 로그아웃 후 Token Reissue가 실패하는가?
- Client Token 제거 안내가 있는가?
- Access Token 장기 만료로 인한 위험을 줄였는가?

---

### [FAQ]

Q. 로그아웃 테스트에서 가장 중요한 것은 뭐야?
A. Refresh Token 삭제와 로그아웃 후 재발급 차단 여부다.

Q. 로그아웃 후 Access Token은 바로 못 쓰게 돼?
A. 기본 Stateless JWT는 Access Token이 만료 전까지 유효할 수 있다. 짧은 만료 시간이나 Blacklist 전략을 사용해야 즉시 차단할 수 있다.

Q. 로그아웃 후 재발급이 되면 문제야?
A. 문제다. Refresh Token이 삭제되지 않았거나 재발급 검증이 잘못된 것이다.

---

# 9. Part03 Checklist

## 9.1 Password Login Logout Checklist

### [개념]

Part03 Checklist는 Password, Login, Logout 흐름이 Security Advanced 기준에 맞게 설계되었는지 검수하기 위한 목록이다.

---

### [핵심]

Checklist:

```md
- [ ] PasswordEncoder Bean이 등록되었는가?
- [ ] 비밀번호가 평문 저장되지 않는가?
- [ ] 회원가입 시 passwordEncoder.encode를 사용하는가?
- [ ] 로그인 시 passwordEncoder.matches를 사용하는가?
- [ ] encode 결과끼리 문자열 비교하지 않는가?
- [ ] 비밀번호가 응답 DTO에 포함되지 않는가?
- [ ] 비밀번호가 로그에 출력되지 않는가?
- [ ] Login Request에 role/userId를 받지 않는가?
- [ ] Login Response에 password hash가 포함되지 않는가?
- [ ] 로그인 실패 메시지가 계정 존재 여부를 과도하게 노출하지 않는가?
- [ ] 계정 상태 검증이 있는가?
- [ ] 로그인 성공 시 Access Token이 발급되는가?
- [ ] 로그인 성공 시 Refresh Token이 발급되는가?
- [ ] Refresh Token 저장 전략이 있는가?
- [ ] Logout API가 Protected API인가?
- [ ] 로그아웃 시 Principal 기준으로 처리하는가?
- [ ] 로그아웃 시 Refresh Token을 삭제 또는 무효화하는가?
- [ ] 로그아웃 후 재발급이 차단되는가?
- [ ] 비밀번호 변경 시 현재 비밀번호를 확인하는가?
- [ ] 비밀번호 변경 시 새 비밀번호를 encode하는가?
- [ ] 비밀번호 변경 후 Refresh Token 무효화를 검토하는가?
- [ ] Password Reset Token에 만료와 1회성 처리가 있는가?
- [ ] 기존 비밀번호를 알려주는 기능이 없는가?
```

---

### [실무]

Review Flow:

```text
PasswordEncoder 확인
→ 회원가입 encode 확인
→ 로그인 matches 확인
→ Login Request / Response 검수
→ Login Failure 응답 검수
→ Token 발급 검수
→ Refresh Token 저장 검수
→ Logout 처리 검수
→ Password Change / Reset 검수
→ 테스트 시나리오 확인
```

후속 문서 연결:

```text
Part03 Password Login Logout
→ Part04 JWT Access Token Refresh Token
→ Part05 Authorization Resource Owner Check
→ Part06 Exception Handling CORS CSRF
→ Part08 Security Testing Troubleshooting
```

---

### [FAQ]

Q. Part03에서 가장 중요한 검수 포인트는 뭐야?
A. PasswordEncoder 사용, matches 검증, Login Response 보안, Refresh Token 저장, Logout 시 Refresh Token 무효화다.

Q. Password 문서와 JWT 문서는 어떻게 연결돼?
A. Login에서 비밀번호 검증이 성공하면 JWT Access Token과 Refresh Token을 발급하는 흐름으로 연결된다.

Q. Logout 문서와 Token Reissue 문서는 어떻게 연결돼?
A. Logout에서 Refresh Token을 무효화해야 이후 Token Reissue가 차단된다.

---

# Retrieval Queries

### [FAQ]

Q. 비밀번호는 어떻게 저장해야 해?
A. BCrypt 같은 PasswordEncoder로 단방향 해시 처리해 저장해야 한다.

Q. 비밀번호를 평문으로 저장하면 안 돼?
A. 안 된다. DB 유출 시 모든 계정이 즉시 위험해지므로 평문 저장은 심각한 보안 Anti Pattern이다.

Q. 로그인할 때 encode해서 DB 값과 비교하면 돼?
A. 안 된다. BCrypt는 매번 다른 해시가 나올 수 있으므로 `matches(raw, encoded)`로 비교해야 한다.

Q. PasswordEncoder는 왜 필요해?
A. 비밀번호를 평문으로 저장하지 않고 안전한 단방향 해시로 저장하기 위해 필요하다.

Q. BCryptPasswordEncoder를 써도 돼?
A. 일반적인 Spring Boot Backend에서는 BCryptPasswordEncoder를 기본 선택지로 사용할 수 있다.

Q. PasswordEncoder는 어디에 등록해?
A. 보통 SecurityConfig 또는 별도 Config에서 Bean으로 등록한다.

Q. 비밀번호 변경 시에도 encode해야 해?
A. 반드시 해야 한다. 새 비밀번호도 평문이 아니라 해시 값으로 저장해야 한다.

Q. matches의 첫 번째 인자는 뭐야?
A. 사용자가 입력한 raw password다.

Q. matches의 두 번째 인자는 뭐야?
A. DB에 저장된 encoded password다.

Q. 비밀번호 검증 실패는 401이야 403이야?
A. 인증 실패이므로 일반적으로 401 Unauthorized 계열로 처리한다.

Q. 비밀번호를 응답 DTO에 넣어도 돼?
A. 안 된다. 비밀번호 해시라도 외부 응답으로 노출하면 안 된다.

Q. 비밀번호를 로그로 찍어도 돼?
A. 안 된다. raw password, encoded password 모두 로그 출력 금지 대상이다.

Q. 비밀번호 찾기에서 기존 비밀번호를 알려줘도 돼?
A. 안 된다. 비밀번호는 복호화할 수 없어야 하며 재설정 방식으로 처리해야 한다.

Q. 로그인 성공하면 뭘 반환해?
A. JWT 구조에서는 Access Token, Refresh Token, 사용자 요약 정보를 반환할 수 있다.

Q. 로그인 실패 이유를 자세히 알려줘도 돼?
A. 보안상 이메일 존재 여부나 비밀번호 오류를 과도하게 구분하지 않는 것이 좋다.

Q. 로그인 성공 시 SecurityContext에 저장해야 해?
A. 전통 Form Login에서는 저장되지만 JWT REST API에서는 이후 요청마다 JWT Filter가 검증해 SecurityContext에 저장하는 구조가 일반적이다.

Q. Login Request에 role을 넣어도 돼?
A. 안 된다. 권한은 서버에 저장된 사용자 정보 기준으로 판단해야 한다.

Q. Login Request에 userId를 넣어도 돼?
A. 일반적으로 필요 없다. email 또는 username으로 사용자를 조회하고 서버에서 userId를 판단한다.

Q. 로그인 요청 DTO에 Validation이 필요해?
A. 필요하다. email 형식과 password blank 여부를 검증하는 것이 좋다.

Q. Login Response에 Refresh Token을 포함해도 돼?
A. 가능하다. 다만 저장 위치, XSS, CSRF, Cookie 정책을 Frontend Auth Flow와 함께 검토해야 한다.

Q. Login Response에 사용자 role을 포함해도 돼?
A. UI 표시와 권한 UX를 위해 포함할 수 있지만 Backend 권한 검증을 대체하지 않는다.

Q. Login Response에 password hash를 포함해도 돼?
A. 안 된다. 해시 값이라도 응답에 포함하면 안 된다.

Q. 로그인 실패는 401이 맞아?
A. 일반적으로 인증 실패이므로 401 Unauthorized 계열이 맞다.

Q. 이메일이 없는 경우와 비밀번호가 틀린 경우를 구분해도 돼?
A. 보안상 계정 존재 여부가 노출될 수 있으므로 일반 로그인 실패 메시지로 통일하는 것이 좋다.

Q. 로그인 실패 횟수 제한이 필요해?
A. Brute Force 방어를 위해 실패 횟수 제한, 지연 응답, 계정 잠금 정책을 검토할 수 있다.

Q. 비밀번호가 맞으면 무조건 로그인시켜도 돼?
A. 아니다. 탈퇴, 정지, 잠금, 이메일 미인증 같은 계정 상태를 확인해야 한다.

Q. 정지된 사용자는 Token 발급을 막아야 해?
A. 일반적으로 막아야 한다. 필요하면 기존 Refresh Token도 무효화한다.

Q. 이메일 인증 전 로그인을 허용할지는 어디서 정해?
A. 프로젝트 정책에서 정하고 Login Flow 또는 Authorization 정책에 반영한다.

Q. Access Token에는 뭘 넣어야 해?
A. userId, role, 만료 시간처럼 인증과 권한 판단에 필요한 최소 정보만 넣는 것이 좋다.

Q. Access Token 만료 시간은 짧게 해야 해?
A. 일반적으로 짧게 설정해 탈취 시 피해 시간을 줄이고 Refresh Token으로 재발급하는 구조를 사용한다.

Q. Access Token에 개인정보를 많이 넣어도 돼?
A. 권장하지 않는다. JWT Payload는 디코딩 가능하므로 민감정보를 넣으면 안 된다.

Q. Refresh Token은 왜 필요해?
A. Access Token을 짧게 유지하면서 사용자가 자주 로그인하지 않도록 새 Access Token을 발급하기 위해 필요하다.

Q. Refresh Token도 DB에 저장해야 해?
A. 로그아웃, 강제 만료, 탈취 대응이 필요하면 DB나 Redis 같은 서버 저장소에 저장하는 것이 좋다.

Q. Refresh Token은 Access Token보다 길게 설정해?
A. 일반적으로 Access Token보다 긴 만료 시간을 사용한다.

Q. JWT 로그아웃은 서버에서 바로 Access Token을 무효화할 수 있어?
A. 기본 Stateless JWT는 어렵다. Blacklist를 쓰거나 Access Token 만료 시간을 짧게 두고 Refresh Token을 무효화하는 방식이 일반적이다.

Q. 로그아웃 시 Refresh Token은 삭제해야 해?
A. 서버에 저장한 Refresh Token이 있다면 삭제하거나 무효화하는 것이 좋다.

Q. Logout API는 인증이 필요해?
A. 일반적으로 필요하다. 현재 로그인한 사용자의 Refresh Token을 무효화해야 하기 때문이다.

Q. 다중 기기 로그인을 지원하려면 Refresh Token을 어떻게 저장해?
A. userId와 deviceId 또는 tokenId를 함께 저장해 기기별로 관리하는 것이 좋다.

Q. 비밀번호 변경 후 모든 기기에서 로그아웃시켜야 해?
A. 보안상 권장된다. 비밀번호 변경 시 모든 Refresh Token을 삭제하면 된다.

Q. 현재 기기만 로그아웃하려면 어떻게 해?
A. 현재 요청의 Refresh Token 또는 deviceId 기준으로 해당 Token만 삭제한다.

Q. 로그아웃을 Client Token 삭제만으로 처리해도 돼?
A. 부족하다. 서버에 저장된 Refresh Token이 있다면 반드시 삭제하거나 무효화해야 한다.

Q. RequestBody userId로 로그아웃 처리해도 돼?
A. 안 된다. 인증 Principal의 userId를 기준으로 처리해야 한다.

Q. Access Token 만료 시간이 길면 왜 위험해?
A. 탈취된 Access Token이 오래 유효하게 남아 로그아웃 후에도 API 접근에 사용될 수 있기 때문이다.

Q. 비밀번호 변경 시 현재 비밀번호 확인이 필요해?
A. 로그인한 사용자의 보안 강화를 위해 현재 비밀번호 확인을 요구하는 것이 일반적이다.

Q. 비밀번호 변경 후 Refresh Token을 삭제해야 해?
A. 보안상 권장된다. 기존 기기 세션을 모두 무효화하고 재로그인을 요구할 수 있다.

Q. 새 비밀번호도 encode해야 해?
A. 반드시 해야 한다. 모든 저장 비밀번호는 해시 값이어야 한다.

Q. Password Reset Token은 얼마나 유효해야 해?
A. 짧은 만료 시간을 두는 것이 좋다. 프로젝트 정책에 따라 다르지만 장기간 유효하면 위험하다.

Q. 비밀번호 재설정 후 기존 로그인은 유지해도 돼?
A. 보안상 기존 Refresh Token을 삭제해 모든 기기에서 재로그인하도록 하는 것이 좋다.

Q. 로그인 테스트에서 가장 중요한 것은 뭐야?
A. 정상 로그인 Token 발급, 잘못된 비밀번호 실패, 계정 존재 여부 노출 방지, password 응답/로그 노출 방지다.

Q. 로그인 실패 테스트는 401을 보면 돼?
A. 일반적으로 401과 errorCode를 함께 확인하는 것이 좋다.

Q. Refresh Token 저장도 테스트해야 해?
A. 해야 한다. 재발급과 로그아웃 기능이 Refresh Token 저장 상태에 의존하기 때문이다.

Q. 로그아웃 테스트에서 가장 중요한 것은 뭐야?
A. Refresh Token 삭제와 로그아웃 후 재발급 차단 여부다.

Q. 로그아웃 후 Access Token은 바로 못 쓰게 돼?
A. 기본 Stateless JWT는 Access Token이 만료 전까지 유효할 수 있다. 짧은 만료 시간이나 Blacklist 전략을 사용해야 즉시 차단할 수 있다.

Q. 로그아웃 후 재발급이 되면 문제야?
A. 문제다. Refresh Token이 삭제되지 않았거나 재발급 검증이 잘못된 것이다.

Q. Part03에서 가장 중요한 검수 포인트는 뭐야?
A. PasswordEncoder 사용, matches 검증, Login Response 보안, Refresh Token 저장, Logout 시 Refresh Token 무효화다.

Q. Password 문서와 JWT 문서는 어떻게 연결돼?
A. Login에서 비밀번호 검증이 성공하면 JWT Access Token과 Refresh Token을 발급하는 흐름으로 연결된다.

Q. Logout 문서와 Token Reissue 문서는 어떻게 연결돼?
A. Logout에서 Refresh Token을 무효화해야 이후 Token Reissue가 차단된다.
