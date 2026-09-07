# Security Advanced Part07 - OAuth2 Login and Frontend Auth Integration

---

# 1. OAuth2 Login Overview

## 1.1 OAuth2 Login Concept

### [개념]

OAuth2 Login은 외부 Provider를 통해 사용자 인증을 수행하고 Application에서 자체 사용자 계정과 연결하는 인증 방식이다.

Spring Security 기반 Backend에서는 OAuth2 Provider 인증 성공 후 Local User를 조회하거나 생성하고, 자체 API 인증을 위해 JWT Access Token / Refresh Token을 발급하는 구조를 사용할 수 있다.

OAuth2 Login은 외부 인증이고, Application API 접근 권한은 Backend Security 정책으로 다시 검증해야 한다.

---

### [핵심]

OAuth2 Login 핵심 키워드:

- OAuth2 Login
- Provider
- Authorization Code
- Redirect URI
- Client ID
- Client Secret
- Scope
- OAuth2User
- OAuth2UserService
- SuccessHandler
- FailureHandler
- User Mapping
- Local User
- JWT Issue
- One-time Code
- HttpOnly Cookie
- Frontend Redirect

OAuth2 Login 기본 흐름:

```text
User OAuth2 Login Click
→ Provider Authorization Page
→ Authorization Code 발급
→ Backend Callback
→ Provider User Info 조회
→ Local User 조회 / 가입
→ Application Token 발급 또는 One-time Code 발급
→ Frontend Redirect
```

---

### [실무]

2026 실무 기준에서 OAuth2 Login은 Provider 인증 자체보다 Application 계정 연결, JWT 발급, Frontend Redirect, Token 전달 방식, 보안 예외 처리가 중요하다.

Spring Security OAuth2 Login Flow:

```text
Frontend Login Button
→ Backend OAuth2 Authorization Endpoint
→ Provider Login
→ Provider Callback
→ Spring Security OAuth2LoginAuthenticationFilter
→ OAuth2UserService
→ Local User Mapping
→ OAuth2 SuccessHandler
→ JWT Access Token / Refresh Token 발급 또는 One-time Code 발급
→ Frontend Redirect
```

권장:

- Provider별 사용자 식별자를 저장한다.
- `provider + providerId` 조합으로 사용자 식별한다.
- email만으로 OAuth2 사용자를 식별하지 않는다.
- 최초 로그인 시 회원 생성 정책을 명확히 한다.
- SuccessHandler에서 Token 전달 전략을 안전하게 설계한다.
- Access Token / Refresh Token을 URL Query Parameter로 직접 전달하지 않는 것을 권장한다.
- One-time Code 교환 방식 또는 HttpOnly Cookie 방식을 우선 검토한다.
- Frontend Redirect URL을 허용 목록 기반으로 제한한다.
- OAuth2 사용자도 Backend Role / Authority 검증을 적용한다.

---

### [FAQ]

Q. OAuth2 Login은 뭐야?
A. Google, Kakao, Naver 같은 외부 Provider를 통해 사용자를 인증하고 Application 계정과 연결하는 로그인 방식이다.

Q. OAuth2 Login을 쓰면 JWT가 필요 없어?
A. 아니다. OAuth2로 외부 인증을 받은 뒤 자체 API 인증을 위해 JWT를 발급하는 구조를 사용할 수 있다.

Q. OAuth2 Login에서 가장 중요한 Backend 작업은 뭐야?
A. Provider 사용자 정보를 Local User와 안전하게 Mapping하고 Application 인증 수단을 안전하게 발급 / 전달하는 것이다.

Q. OAuth2 성공 후 Token을 URL Query로 보내도 돼?
A. 권장하지 않는다. 브라우저 기록, 로그, Referer로 노출될 수 있으므로 One-time Code 교환 방식이나 HttpOnly Cookie 방식을 우선 검토한다.

---

# 2. OAuth2 Provider Rules

## 2.1 Provider Identity Rules

### [개념]

Provider Identity는 OAuth2 Provider가 제공하는 사용자 식별 정보다.

Application은 Provider별 사용자 정보를 Local User와 연결해야 하며, 사용자 식별 기준은 email 단독보다 `provider + providerId` 조합이 안전하다.

---

### [핵심]

Provider Identity 핵심 키워드:

- provider
- providerId
- registrationId
- OAuth2User
- attributes
- email
- email_verified
- nickname
- profileImage
- subject
- Local User Mapping

Provider 예:

```text
GOOGLE
KAKAO
NAVER
GITHUB
```

사용자 식별 기준:

```text
provider + providerId
```

---

### [실무]

Provider Identity 저장 예:

```java
public enum OAuthProvider {
    GOOGLE,
    KAKAO,
    NAVER
}
```

User Entity 필드 후보:

```java
private OAuthProvider provider;

private String providerId;

private String email;

private String nickname;

private Role role;
```

권장:

- Provider별 고유 ID를 저장한다.
- email은 변경 가능하거나 제공되지 않을 수 있다고 가정한다.
- email_verified가 있는 Provider는 검증 여부를 확인한다.
- Provider별 attribute 구조를 별도 Mapper로 분리한다.
- 동일 email 기존 계정과 연결할지 정책을 정한다.
- Provider 응답 원본 전체 저장은 지양한다.

주의:

- email만으로 OAuth2 사용자를 식별하면 계정 병합 문제가 생길 수 있다.
- Provider마다 attribute 구조가 다르다.
- Kakao / Naver / Google의 사용자 정보 필드명이 다를 수 있다.
- email이 null일 수 있는 경우를 처리해야 한다.

---

### [FAQ]

Q. OAuth2 사용자는 어떻게 식별해?
A. 일반적으로 provider와 providerId 조합으로 식별한다. email만으로 식별하면 변경이나 중복 문제가 생길 수 있다.

Q. OAuth2 Provider email을 그대로 믿어도 돼?
A. Provider와 email_verified 여부에 따라 다르다. 프로젝트 정책에 맞게 검증 기준을 정해야 한다.

Q. providerId는 왜 저장해?
A. Provider가 보장하는 사용자 고유 식별자를 Local User와 연결하기 위해 필요하다.

---

## 2.2 Provider Attribute Mapping

### [개념]

Provider Attribute Mapping은 Provider별 OAuth2 사용자 응답을 Application 공통 사용자 정보로 변환하는 과정이다.

Provider마다 응답 구조가 다르므로 공통 Interface 또는 Mapper를 사용해 구조를 분리하는 것이 좋다.

---

### [핵심]

Mapping 대상:

- provider
- providerId
- email
- emailVerified
- nickname
- profileImage
- attributes

Provider별 차이:

```text
Google → sub, email, name, picture
Kakao → id, kakao_account.email, properties.nickname
Naver → response.id, response.email, response.nickname
```

---

### [실무]

공통 OAuth2 User Info 예:

```java
public interface OAuth2UserInfo {

    OAuthProvider provider();

    String providerId();

    String email();

    String nickname();

    String profileImage();
}
```

Provider별 구현 예:

```java
public class GoogleOAuth2UserInfo implements OAuth2UserInfo {

    private final Map<String, Object> attributes;

    public OAuthProvider provider() {
        return OAuthProvider.GOOGLE;
    }

    public String providerId() {
        return String.valueOf(attributes.get("sub"));
    }

    public String email() {
        return String.valueOf(attributes.get("email"));
    }

    public String nickname() {
        return String.valueOf(attributes.get("name"));
    }

    public String profileImage() {
        return String.valueOf(attributes.get("picture"));
    }
}
```

Factory 예:

```java
public class OAuth2UserInfoFactory {

    public static OAuth2UserInfo of(
            String registrationId,
            Map<String, Object> attributes
    ) {
        if ("google".equals(registrationId)) {
            return new GoogleOAuth2UserInfo(attributes);
        }

        if ("kakao".equals(registrationId)) {
            return new KakaoOAuth2UserInfo(attributes);
        }

        throw new BusinessException(
                "OAUTH_PROVIDER_NOT_SUPPORTED",
                "지원하지 않는 OAuth2 Provider입니다."
        );
    }
}
```

권장:

- Provider별 attribute parsing을 분리한다.
- Controller나 Service에 Provider별 Map 접근 로직을 흩뿌리지 않는다.
- email null 케이스를 처리한다.
- 필수 정보 누락 시 가입 제한 또는 추가 정보 입력 흐름으로 연결한다.
- Provider 추가 시 Factory / Mapper만 확장 가능하게 설계한다.

---

### [FAQ]

Q. OAuth2 Provider마다 응답 구조가 달라?
A. 다르다. Google, Kakao, Naver는 사용자 정보 attribute 구조가 다르므로 Provider별 Mapping이 필요하다.

Q. Provider별 Mapping 로직은 어디에 두는 게 좋아?
A. OAuth2UserInfo 구현체나 Mapper / Factory로 분리하는 것이 좋다.

Q. email이 없는 Provider 응답은 어떻게 처리해?
A. 프로젝트 정책에 따라 가입을 제한하거나 추가 정보 입력 화면으로 연결해야 한다.

---

# 3. OAuth2 User Mapping Rules

## 3.1 Local User Mapping Concept

### [개념]

Local User Mapping은 OAuth2 Provider 사용자 정보를 Application의 User Entity와 연결하는 과정이다.

OAuth2 인증 성공 후에도 Application 내부에서는 Local User 기준으로 Role, Authority, JWT, Refresh Token, 서비스 이용 상태를 관리해야 한다.

---

### [핵심]

Local User Mapping 핵심 키워드:

- Local User
- User Entity
- provider
- providerId
- email
- role
- accountStatus
- first login
- existing user
- auto signup
- account linking

Mapping 흐름:

```text
OAuth2UserInfo 생성
→ provider + providerId로 User 조회
→ 기존 User 있으면 로그인 처리
→ 없으면 신규 User 생성 또는 추가 정보 입력
→ Role 부여
→ Account Status 확인
→ Application 인증 수단 발급
```

---

### [실무]

OAuth2 User Service 예:

```java
@Service
public class CustomOAuth2UserService
        extends DefaultOAuth2UserService {

    @Override
    public OAuth2User loadUser(OAuth2UserRequest userRequest)
            throws OAuth2AuthenticationException {

        OAuth2User oauth2User = super.loadUser(userRequest);

        String registrationId =
                userRequest.getClientRegistration().getRegistrationId();

        OAuth2UserInfo userInfo =
                OAuth2UserInfoFactory.of(registrationId, oauth2User.getAttributes());

        User user = userRepository
                .findByProviderAndProviderId(userInfo.provider(), userInfo.providerId())
                .orElseGet(() -> registerOAuth2User(userInfo));

        validateOAuth2LoginAllowed(user);

        return new CustomOAuth2Principal(
                user.getId(),
                user.getEmail(),
                user.getRole(),
                oauth2User.getAttributes()
        );
    }
}
```

권장:

- `provider + providerId`로 기존 User를 조회한다.
- 신규 사용자 기본 Role을 명확히 부여한다.
- 탈퇴 / 정지 사용자의 OAuth2 Login을 차단한다.
- 최초 로그인 시 필수 약관, 닉네임, 추가 정보 입력 정책을 정한다.
- OAuth2 사용자도 일반 User와 동일한 권한 검증 체계에 포함한다.
- Provider 응답 attribute를 그대로 Principal에 과도하게 넣지 않는다.

---

### [FAQ]

Q. OAuth2 로그인 후 User Entity가 꼭 필요해?
A. 대부분 필요하다. Application 권한, 서비스 데이터, JWT 발급, 계정 상태 관리를 위해 Local User가 필요하다.

Q. OAuth2 최초 로그인 시 회원가입을 자동으로 해도 돼?
A. 가능하다. 다만 필수 약관, 추가 정보 입력, 기본 권한 부여 정책을 정해야 한다.

Q. OAuth2 사용자도 Role이 필요해?
A. 필요하다. Application API 접근 권한은 Backend Role / Authority 기준으로 검증해야 한다.

---

## 3.2 Existing Account Linking Rules

### [개념]

Existing Account Linking은 OAuth2 사용자와 기존 Local 계정을 연결할지 결정하는 정책이다.

동일 email을 가진 기존 계정이 있을 때 자동 연결할지, 추가 인증을 요구할지, 별도 계정으로 둘지 명확히 정해야 한다.

---

### [핵심]

계정 연결 후보:

- 동일 email 기존 Local 계정
- 동일 email 다른 Provider 계정
- provider + providerId 신규 계정
- email_verified 확인 필요
- 추가 본인 확인 필요

정책 후보:

```text
자동 연결
추가 인증 후 연결
연결 금지
별도 계정 생성
```

---

### [실무]

자동 연결 위험:

```text
Provider email만 일치
→ 기존 계정과 자동 연결
→ email 신뢰성이 낮으면 계정 탈취 위험
```

권장 흐름:

```text
OAuth2 Login 성공
→ provider + providerId 조회
→ 없으면 email 기존 계정 조회
→ email_verified 확인
→ 추가 인증 또는 계정 연결 동의
→ 연결 저장
```

Entity 설계 후보:

```java
@Entity
public class OAuthAccount {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private Long userId;

    private OAuthProvider provider;

    private String providerId;

    private String email;
}
```

권장:

- 계정 연결 정책을 명확히 문서화한다.
- email_verified가 없는 email은 자동 연결하지 않는다.
- 여러 Provider 연결을 지원하려면 별도 OAuthAccount 테이블을 검토한다.
- 단일 Provider만 지원하면 User Entity에 provider / providerId 필드로 단순화할 수 있다.
- 연결 해제 정책도 함께 검토한다.

---

### [FAQ]

Q. 같은 email이면 기존 계정과 자동 연결해도 돼?
A. 신중해야 한다. Provider의 email_verified 여부와 추가 인증 정책을 확인해야 한다.

Q. 여러 OAuth2 Provider를 한 계정에 연결하려면 어떻게 해?
A. User와 OAuthAccount를 분리해 userId, provider, providerId 조합으로 관리하는 구조를 검토한다.

Q. OAuth2 계정 연결 해제도 필요해?
A. 서비스 정책에 따라 필요할 수 있다. 마지막 로그인 수단인지 확인하고 연결 해제 제한을 둘 수 있다.

---

# 4. OAuth2 Success and Failure Handling

## 4.1 OAuth2 SuccessHandler Rules

### [개념]

OAuth2 SuccessHandler는 OAuth2 인증이 성공한 후 Application 후속 처리를 수행하는 Handler다.

주요 역할은 Local User 확인, 인증 수단 발급, Refresh Token 저장, Frontend Redirect, 안전한 Token 전달 흐름 구성이다.

---

### [핵심]

SuccessHandler 역할:

- 인증 성공 사용자 확인
- Local User Principal 추출
- Account Status 확인
- Access Token 생성
- Refresh Token 생성
- Refresh Token 저장
- One-time Code 생성
- Frontend Redirect URL 결정
- Token 전달 방식 적용
- 로그인 성공 응답 처리

Token 전달 후보:

- One-time Code 교환 방식
- HttpOnly Cookie 방식
- Backend-for-Frontend Session 방식
- Redirect Query Parameter 직접 Token 전달은 비권장

---

### [실무]

권장 OAuth2 Success Flow:

```text
OAuth2 Authentication Success
→ CustomOAuth2Principal 추출
→ User 상태 확인
→ One-time Code 생성
→ One-time Code와 userId 매핑 저장
→ Frontend Success URL로 code만 Redirect
→ Frontend가 Token Exchange API 호출
→ Backend가 Access Token / Refresh Token 발급
```

One-time Code 방식 SuccessHandler 예:

```java
@Component
public class OAuth2SuccessHandler extends SimpleUrlAuthenticationSuccessHandler {

    @Override
    public void onAuthenticationSuccess(
            HttpServletRequest request,
            HttpServletResponse response,
            Authentication authentication
    ) throws IOException {

        CustomOAuth2Principal principal =
                (CustomOAuth2Principal) authentication.getPrincipal();

        String oneTimeCode = oneTimeCodeService.issue(principal.userId());

        String targetUrl = UriComponentsBuilder
                .fromUriString(frontendSuccessUrl)
                .queryParam("code", oneTimeCode)
                .build()
                .toUriString();

        getRedirectStrategy().sendRedirect(request, response, targetUrl);
    }
}
```

Token Exchange API Flow:

```text
POST /api/auth/oauth2/token
Request: oneTimeCode
→ oneTimeCode 검증
→ userId 조회
→ Access Token 발급
→ Refresh Token 발급
→ Refresh Token 저장
→ oneTimeCode 사용 완료 처리
→ Login Response 반환
```

Token Exchange 예:

```java
@Transactional
public OAuth2TokenResponse exchange(String oneTimeCode) {
    Long userId = oneTimeCodeService.consume(oneTimeCode);

    User user = userRepository.findById(userId)
            .orElseThrow(() -> new BusinessException(
                    "USER_NOT_FOUND",
                    "사용자를 찾을 수 없습니다."
            ));

    validateOAuth2LoginAllowed(user);

    String accessToken = tokenProvider.createAccessToken(
            user.getId(),
            user.getRole()
    );

    String refreshToken = tokenProvider.createRefreshToken(user.getId());

    refreshTokenService.saveOrUpdate(user.getId(), refreshToken);

    return new OAuth2TokenResponse(
            accessToken,
            refreshToken,
            "Bearer",
            accessTokenExpiresIn
    );
}
```

권장:

- SuccessHandler에서 Access Token / Refresh Token을 URL Query로 직접 전달하지 않는다.
- Redirect에는 짧은 수명의 One-time Code만 전달하는 방식을 우선 검토한다.
- One-time Code는 짧은 만료 시간과 1회성 사용을 보장한다.
- One-time Code는 사용 후 즉시 폐기한다.
- Refresh Token은 서버 저장소에 저장한다.
- Frontend Redirect URL은 허용 목록 기반으로 제한한다.
- Token 원문을 로그에 남기지 않는다.

주의:

- Access Token을 Query Parameter로 전달하면 브라우저 기록, 로그, Referer에 노출될 수 있다.
- Refresh Token을 Query Parameter로 전달하는 것은 권장하지 않는다.
- One-time Code도 인증 교환 수단이므로 짧은 만료 시간과 1회성을 가져야 한다.
- Redirect URL을 요청 파라미터로 검증 없이 사용하면 Open Redirect 위험이 있다.

---

### [FAQ]

Q. OAuth2 SuccessHandler는 뭐 하는 곳이야?
A. OAuth2 인증 성공 후 Local User 확인, One-time Code 발급, Frontend Redirect 같은 후속 처리를 수행한다.

Q. OAuth2 성공 후 JWT를 어디서 발급해?
A. 안전한 구조에서는 SuccessHandler가 One-time Code를 발급하고, 별도 Token Exchange API에서 JWT를 발급할 수 있다.

Q. Access Token을 Redirect Query로 보내도 돼?
A. 권장하지 않는다. 브라우저 기록, 로그, Referer로 노출될 수 있으므로 One-time Code 교환 방식이나 HttpOnly Cookie 방식을 우선 검토한다.

Q. One-time Code는 왜 써?
A. Token 원문을 URL로 직접 전달하지 않고, 짧은 수명의 1회용 Code를 통해 안전하게 Token을 교환하기 위해 사용한다.

---

## 4.2 HttpOnly Cookie OAuth2 Success Rules

### [개념]

HttpOnly Cookie OAuth2 Success 방식은 OAuth2 인증 성공 후 Backend가 Refresh Token을 HttpOnly Cookie로 내려주고 Frontend로 Redirect하는 구조다.

이 방식은 JavaScript에서 Refresh Token을 직접 읽지 못하게 할 수 있지만 CORS credentials, SameSite, CSRF 정책을 함께 검토해야 한다.

---

### [핵심]

HttpOnly Cookie 방식 핵심 키워드:

- HttpOnly Cookie
- Refresh Token Cookie
- Set-Cookie
- SameSite
- Secure
- Path
- Max-Age
- allowCredentials
- withCredentials
- CSRF

Flow:

```text
OAuth2 Success
→ Access Token 발급 방식 결정
→ Refresh Token 발급
→ Refresh Token 서버 저장
→ Set-Cookie Refresh Token
→ Frontend Redirect
```

---

### [실무]

Cookie 설정 예:

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

Access Token 전달 방식 후보:

```text
1. Frontend Redirect 후 /api/auth/reissue 호출
   → Refresh Token Cookie 기반으로 Access Token 발급

2. One-time Code로 Access Token 교환
   → Refresh Token은 Cookie로 관리

3. BFF Session 방식
   → Frontend는 Token을 직접 다루지 않음
```

권장:

- Refresh Token Cookie는 HttpOnly를 적용한다.
- 운영 환경에서는 Secure를 적용한다.
- SameSite 정책을 OAuth2 Redirect / Cross-Origin 구조에 맞게 검토한다.
- Cookie Path를 Reissue API로 제한할 수 있다.
- CORS에서 credentials 사용 여부를 명확히 한다.
- CSRF 위험을 검토한다.
- Logout 시 동일 Path와 속성으로 Cookie를 제거한다.

주의:

- HttpOnly Cookie는 XSS로 인한 JS 접근을 줄이지만 CSRF 검토가 필요하다.
- Cross-Origin Cookie를 쓰면 `allowCredentials(true)`와 Frontend `withCredentials` 설정이 필요할 수 있다.
- credentials 사용 시 wildcard Origin을 사용하면 안 된다.

---

### [FAQ]

Q. OAuth2 성공 후 Refresh Token을 HttpOnly Cookie로 내려도 돼?
A. 가능하다. 다만 SameSite, Secure, CSRF, CORS credentials 정책을 함께 검토해야 한다.

Q. HttpOnly Cookie 방식이면 XSS가 완전히 해결돼?
A. 아니다. JavaScript가 Cookie를 직접 읽기 어렵게 할 뿐이며 CSRF와 다른 XSS 피해는 별도로 검토해야 한다.

Q. Cookie 방식이면 CORS에서 뭘 맞춰야 해?
A. Backend allowCredentials, 명시적 allowedOrigins, Frontend withCredentials 설정을 맞춰야 한다.

---

## 4.3 OAuth2 FailureHandler Rules

### [개념]

OAuth2 FailureHandler는 OAuth2 인증 실패 또는 Provider 연동 실패 시 Client에 실패 결과를 전달하는 Handler다.

Provider 인증 실패, 사용자 정보 조회 실패, 필수 정보 누락, 계정 상태 제한 등을 처리한다.

---

### [핵심]

Failure 원인:

- Provider 인증 취소
- Authorization Code 오류
- Provider API 오류
- 필수 email 누락
- 지원하지 않는 Provider
- Local User Mapping 실패
- 정지 / 탈퇴 사용자
- 계정 연결 정책 실패

Failure 처리 후보:

- Frontend 실패 URL Redirect
- errorCode 전달
- 짧은 실패 메시지 전달
- 서버 로그 기록
- 민감정보 미노출

---

### [실무]

Failure Redirect 예:

```text
OAuth2 Failure
→ /login?error=OAUTH2_LOGIN_FAILED
```

FailureHandler 예:

```java
@Component
public class OAuth2FailureHandler
        extends SimpleUrlAuthenticationFailureHandler {

    @Override
    public void onAuthenticationFailure(
            HttpServletRequest request,
            HttpServletResponse response,
            AuthenticationException exception
    ) throws IOException {

        String targetUrl = UriComponentsBuilder
                .fromUriString(frontendFailureUrl)
                .queryParam("errorCode", "OAUTH2_LOGIN_FAILED")
                .build()
                .toUriString();

        getRedirectStrategy().sendRedirect(request, response, targetUrl);
    }
}
```

권장:

- Provider 내부 오류를 사용자에게 상세히 노출하지 않는다.
- Frontend가 처리 가능한 errorCode를 전달한다.
- 실패 원인은 서버 로그에만 진단 가능하게 남긴다.
- Token, Authorization Code, Client Secret을 로그에 남기지 않는다.
- 계정 상태 실패와 Provider 실패를 구분할지 정책화한다.
- 실패 Redirect URL도 허용 목록 기반으로 관리한다.

---

### [FAQ]

Q. OAuth2 로그인 실패는 어떻게 처리해?
A. FailureHandler에서 Frontend 실패 URL로 Redirect하고 errorCode를 전달하는 방식이 일반적이다.

Q. Provider 오류 상세를 사용자에게 보여줘도 돼?
A. 권장하지 않는다. 사용자에게는 짧은 실패 메시지를 보여주고 상세 원인은 서버 로그에서 확인한다.

Q. OAuth2 실패도 401 응답이야?
A. Redirect 기반 OAuth2 Login에서는 실패 URL로 Redirect하는 경우가 많다. REST API 방식이면 401 또는 적절한 errorCode로 처리할 수 있다.

---

# 5. OAuth2 SecurityFilterChain Rules

## 5.1 OAuth2 Login Configuration

### [개념]

OAuth2 Login Configuration은 Spring SecurityFilterChain에서 OAuth2 Login 진입점, UserInfo 처리, SuccessHandler, FailureHandler를 연결하는 설정이다.

JWT REST API와 OAuth2 Login을 함께 사용할 경우 Stateless API 정책과 OAuth2 Redirect Flow를 함께 고려해야 한다.

---

### [핵심]

설정 키워드:

- oauth2Login
- authorizationEndpoint
- redirectionEndpoint
- userInfoEndpoint
- userService
- successHandler
- failureHandler
- clientRegistration
- redirectUri
- loginPage

---

### [실무]

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
                    .requestMatchers("/oauth2/**").permitAll()
                    .requestMatchers("/login/oauth2/code/**").permitAll()
                    .anyRequest().authenticated()
            )
            .oauth2Login(oauth2 -> oauth2
                    .userInfoEndpoint(userInfo ->
                            userInfo.userService(customOAuth2UserService)
                    )
                    .successHandler(oAuth2SuccessHandler)
                    .failureHandler(oAuth2FailureHandler)
            )
            .addFilterBefore(jwtAuthenticationFilter, UsernamePasswordAuthenticationFilter.class)
            .build();
}
```

권장:

- OAuth2 Authorization Endpoint는 Public 접근 가능해야 한다.
- OAuth2 Callback Endpoint는 Provider가 접근 가능해야 한다.
- OAuth2 SuccessHandler / FailureHandler를 명확히 등록한다.
- OAuth2 Login 후 자체 인증 수단을 발급하는 구조를 문서화한다.
- JWT Filter가 OAuth2 Login Flow를 방해하지 않도록 확인한다.
- Redirect URL과 CORS 설정을 Frontend와 맞춘다.

주의:

- OAuth2 Login은 Redirect 기반 흐름이므로 순수 REST Login과 다르게 동작한다.
- STATELESS 정책과 OAuth2 Authorization Request 저장소가 충돌할 수 있다.
- 필요 시 AuthorizationRequestRepository를 Cookie 기반으로 구성할 수 있다.
- Provider Callback URL은 정확히 등록해야 한다.
- Cookie 기반 AuthorizationRequestRepository를 사용하면 SameSite / Secure / CSRF 관점도 함께 검토한다.

---

### [FAQ]

Q. OAuth2 Login 경로도 permitAll이 필요해?
A. 필요하다. 사용자가 인증 전 OAuth2 Login을 시작하고 Provider Callback을 받아야 하기 때문이다.

Q. JWT Filter가 OAuth2 Login을 방해할 수 있어?
A. 잘못 구현하면 Token 없는 OAuth2 경로를 401로 막을 수 있다. Public 경로와 Filter 동작을 확인해야 한다.

Q. OAuth2 Login과 JWT Login을 같이 쓸 수 있어?
A. 가능하다. OAuth2 인증 성공 후 자체 JWT 또는 One-time Code 교환 방식을 통해 API 인증에 사용할 수 있다.

---

## 5.2 Redirect URI and Allowed URL Rules

### [개념]

Redirect URI는 OAuth2 Provider가 인증 결과를 전달하기 위해 호출하는 Backend Callback URL이다.

Frontend Redirect URL은 OAuth2 성공 또는 실패 후 사용자를 이동시킬 Client URL이다.

둘 다 허용된 URL만 사용해야 Open Redirect와 Token 노출 위험을 줄일 수 있다.

---

### [핵심]

Redirect 관련 키워드:

- Redirect URI
- Callback URL
- Frontend Success URL
- Frontend Failure URL
- Allowed Redirect URL
- Open Redirect
- Provider Console
- Authorization Code
- One-time Code

구분:

```text
Provider Redirect URI
→ Backend Callback URL

Frontend Redirect URL
→ OAuth2 처리 후 Client 이동 URL
```

---

### [실무]

Provider Redirect URI 예:

```text
https://api.example.com/login/oauth2/code/google
```

Frontend Success URL 예:

```text
https://app.example.com/oauth2/success
```

Frontend Failure URL 예:

```text
https://app.example.com/login?error=OAUTH2_LOGIN_FAILED
```

권장:

- Provider Console에 Backend Callback URL을 정확히 등록한다.
- Frontend Redirect URL은 서버 설정값 또는 허용 목록으로 관리한다.
- 요청 파라미터의 redirect_uri를 그대로 신뢰하지 않는다.
- Open Redirect를 방지한다.
- Redirect에는 Token 원문 대신 One-time Code 같은 짧은 수명 교환 코드를 사용하는 것이 좋다.
- 운영 / 개발 Redirect URI를 분리한다.

잘못된 예:

```text
SuccessHandler가 request redirectUrl 파라미터를 검증 없이 사용
→ 공격자가 외부 도메인으로 Code 또는 Token 탈취 유도 가능
```

---

### [FAQ]

Q. Provider Redirect URI와 Frontend Redirect URL은 달라?
A. 다르다. Provider Redirect URI는 Backend Callback이고 Frontend Redirect URL은 로그인 처리 후 사용자를 이동시킬 Client URL이다.

Q. Redirect URL을 요청 파라미터로 받아도 돼?
A. 검증 없이 사용하면 Open Redirect 위험이 있으므로 허용 목록 기반으로 제한해야 한다.

Q. OAuth2 Redirect URI가 틀리면 어떻게 돼?
A. Provider 인증 후 Callback이 실패하거나 redirect_uri mismatch 오류가 발생할 수 있다.

Q. Redirect URL에 Token을 직접 붙여도 돼?
A. 권장하지 않는다. Token 원문 대신 One-time Code를 붙이고 별도 API에서 Token을 교환하는 방식이 안전하다.

---

# 6. Frontend Auth Integration Overview

## 6.1 Frontend Auth Integration Concept

### [개념]

Frontend Auth Integration은 Backend 인증 구조와 Frontend 로그인 상태 관리가 연동되는 방식이다.

Backend는 Login API, OAuth2 Token Exchange API, Token 발급, Token Reissue, Logout, 401 / 403 Error Response, CORS 정책을 명확히 제공해야 하며 Frontend는 이를 기준으로 인증 상태를 관리한다.

---

### [핵심]

Frontend Auth Integration 핵심 키워드:

- Login API
- OAuth2 Login
- OAuth2 Token Exchange
- One-time Code
- Access Token
- Refresh Token
- Token Storage
- Authorization Header
- Axios Interceptor
- Token Reissue
- Logout
- Protected Route
- Auth State
- 401 Handling
- 403 Handling
- CORS
- credentials

Backend 제공 기준:

- Login Response 형식
- OAuth2 Success 처리 방식
- OAuth2 Token Exchange API 명세
- Access Token 만료 errorCode
- Refresh API 명세
- Logout API 명세
- 401 / 403 Error Response
- User Summary API
- Role Naming
- CORS allowedHeaders
- Cookie 사용 시 credentials / CSRF 정책

---

### [실무]

일반 Login Frontend Auth Flow:

```text
Login 성공
→ Access Token 저장
→ API 요청 시 Authorization Header 첨부
→ 401 TOKEN_EXPIRED 발생
→ Refresh Token으로 Reissue 요청
→ 새 Access Token 저장
→ 기존 요청 재시도
→ Reissue 실패 시 Logout 처리
```

OAuth2 One-time Code Flow:

```text
OAuth2 성공
→ Frontend /oauth2/success?code=oneTimeCode 진입
→ POST /api/auth/oauth2/token 호출
→ Access Token / Refresh Token 수신
→ Auth State 저장
→ /api/users/me 호출
→ 로그인 완료
```

Backend 연동 API 후보:

```text
POST /api/auth/login
POST /api/auth/oauth2/token
POST /api/auth/reissue
POST /api/auth/logout
GET /api/users/me
GET /oauth2/authorization/{provider}
GET /login/oauth2/code/{provider}
```

권장:

- Backend와 Frontend가 401 / 403 처리 규칙을 공유한다.
- Access Token 만료 errorCode를 명확히 한다.
- Reissue 실패 시 재로그인으로 연결한다.
- 403은 권한 없음 안내로 처리한다.
- CORS에서 Authorization Header를 허용한다.
- Cookie 사용 시 `withCredentials`와 allowedCredentials를 맞춘다.
- OAuth2 성공 Redirect에서는 Token 원문을 직접 다루지 않도록 한다.

---

### [FAQ]

Q. Frontend Auth Integration에서 Backend가 정해야 할 것은 뭐야?
A. Token 발급 형식, OAuth2 Token Exchange API, Reissue API, Logout API, 401/403 errorCode, CORS 정책, 사용자 정보 API를 명확히 해야 한다.

Q. Frontend 로그인 상태만 확인하면 보안이 돼?
A. 아니다. Frontend 로그인 상태는 UX용이고 실제 API 접근 권한은 Backend에서 검증해야 한다.

Q. 403을 받으면 Frontend는 Token 재발급을 해야 해?
A. 아니다. 403은 권한 부족이므로 권한 없음 안내나 접근 차단 처리가 맞다.

---

# 7. Token Storage and Transmission

## 7.1 Access Token Storage Rules

### [개념]

Access Token Storage는 Frontend가 Access Token을 어디에 저장하고 API 요청에 어떻게 첨부할지 결정하는 전략이다.

Access Token은 API 인증 수단이므로 XSS, 만료 시간, 재발급 흐름을 함께 고려해야 한다.

---

### [핵심]

저장 후보:

- Memory
- LocalStorage
- SessionStorage
- HttpOnly Cookie

전송 방식:

```text
Authorization: Bearer AccessToken
```

위험 요소:

- XSS
- Token Theft
- Browser Refresh
- Token Expiration
- Reissue Loop

---

### [실무]

Authorization Header 요청 예:

```javascript
axiosInstance.interceptors.request.use((config) => {
  const token = getAccessToken();

  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  return config;
});
```

저장 방식 비교:

| 저장 방식       | 장점                      | 주의               |
| --------------- | ------------------------- | ------------------ |
| Memory          | Token 노출 지속 시간 감소 | 새로고침 시 사라짐 |
| LocalStorage    | 구현 쉬움                 | XSS에 취약         |
| SessionStorage  | 탭 단위 유지              | XSS에 취약         |
| HttpOnly Cookie | JS 접근 차단              | CSRF 검토 필요     |

권장:

- Access Token 만료 시간을 짧게 둔다.
- Authorization Header 방식을 명확히 문서화한다.
- LocalStorage 사용 시 XSS 위험을 인지한다.
- Memory 저장 시 새로고침 복구 전략을 검토한다.
- Cookie 저장 시 CSRF와 SameSite를 검토한다.
- Backend CORS allowedHeaders에 Authorization을 포함한다.

---

### [FAQ]

Q. Access Token은 어디에 저장하는 게 좋아?
A. 정답은 없다. Memory, LocalStorage, Cookie 각각 장단점이 있어 XSS, CSRF, UX를 기준으로 선택해야 한다.

Q. Access Token을 LocalStorage에 저장해도 돼?
A. 구현은 쉽지만 XSS에 취약하므로 위험을 이해하고 사용해야 한다.

Q. Authorization Header를 쓰면 Backend에서 뭘 허용해야 해?
A. CORS allowedHeaders에 Authorization을 포함해야 브라우저 요청이 차단되지 않는다.

---

## 7.2 Refresh Token Storage Rules

### [개념]

Refresh Token Storage는 Client가 Refresh Token을 어디에 저장하고 Reissue 요청에 어떻게 전달할지 결정하는 전략이다.

Refresh Token은 Access Token보다 수명이 길어 탈취 시 위험이 크므로 더 엄격한 저장 정책이 필요하다.

---

### [핵심]

저장 후보:

- HttpOnly Secure Cookie
- LocalStorage
- SessionStorage
- Memory
- Native Secure Storage

전송 후보:

- Cookie 자동 전송
- Request Body
- Custom Header
- Authorization Header

검토 항목:

- XSS
- CSRF
- SameSite
- HttpOnly
- Secure
- Reissue API
- Logout API
- Rotation

---

### [실무]

HttpOnly Cookie 방식:

```text
Login Success
→ Backend Set-Cookie Refresh Token
→ Browser Cookie 저장
→ Reissue 요청 시 Cookie 자동 전송
→ Backend Refresh Token 검증
```

Cookie 설정 후보:

```text
HttpOnly
Secure
SameSite=Lax 또는 Strict 또는 None
Max-Age
Path=/api/auth/reissue
```

Response Cookie 예:

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

Request Body 방식:

```json
{
  "refreshToken": "refresh-token-value"
}
```

권장:

- Refresh Token은 서버 저장소에도 저장하거나 hash 저장을 검토한다.
- Cookie 방식이면 CSRF와 SameSite 정책을 검토한다.
- Body 방식이면 XSS와 저장 위치를 검토한다.
- Rotation 사용 시 새 Refresh Token 저장이 실패하지 않도록 설계한다.
- Logout 시 Refresh Token 삭제와 Cookie 제거를 함께 처리한다.

---

### [FAQ]

Q. Refresh Token은 어디에 저장하는 게 좋아?
A. HttpOnly Cookie를 자주 검토하지만 CSRF 설정이 필요하다. LocalStorage는 XSS 위험이 있어 주의해야 한다.

Q. Refresh Token을 Cookie에 넣으면 안전해?
A. JS 접근은 막을 수 있지만 CSRF와 SameSite, Secure 설정을 함께 검토해야 한다.

Q. Refresh Token을 LocalStorage에 넣어도 돼?
A. 가능은 하지만 XSS에 취약하므로 위험을 명확히 이해하고 사용해야 한다.

---

# 8. Axios Interceptor and Reissue Flow

## 8.1 Axios Interceptor Rules

### [개념]

Axios Interceptor는 Frontend에서 API 요청 전 Access Token을 Header에 첨부하고, 응답 후 401 에러를 감지해 Token Reissue를 수행하는 흐름을 구성할 때 사용된다.

Backend는 Interceptor가 판단할 수 있는 errorCode와 Reissue API를 제공해야 한다.

---

### [핵심]

Axios Interceptor 역할:

- Request Header에 Access Token 첨부
- 401 TOKEN_EXPIRED 감지
- Refresh Token으로 Reissue 요청
- 새 Access Token 저장
- 실패한 요청 재시도
- Reissue 실패 시 Logout 처리
- 403 ACCESS_DENIED는 권한 없음 처리

필수 Backend 계약:

- TOKEN_EXPIRED errorCode
- Reissue API
- REFRESH_TOKEN_INVALID errorCode
- Logout API
- CORS Authorization Header 허용

---

### [실무]

Interceptor Flow:

```text
API Request
→ Authorization Header 첨부
→ Access Token 만료
→ 401 TOKEN_EXPIRED
→ Reissue 요청
→ 새 Access Token 수신
→ 원래 요청 재시도
→ Reissue 실패
→ Logout 처리
```

Frontend 처리 기준:

```text
401 TOKEN_EXPIRED
→ Reissue 시도

401 REFRESH_TOKEN_INVALID
→ Logout

401 UNAUTHORIZED
→ Login Page

403 ACCESS_DENIED
→ 권한 없음 안내
```

주의:

- 동시에 여러 요청이 401을 받으면 Reissue 중복 요청이 발생할 수 있다.
- Reissue 실패 시 무한 루프를 방지해야 한다.
- Reissue API 자체가 401이면 다시 Reissue를 시도하지 않는다.
- 403은 Reissue 대상이 아니다.
- Backend errorCode가 일관되어야 한다.

---

### [FAQ]

Q. Axios Interceptor는 왜 써?
A. API 요청마다 Access Token을 붙이고 Token 만료 시 재발급을 자동 처리하기 위해 사용한다.

Q. 401이면 항상 Reissue를 시도해도 돼?
A. 아니다. TOKEN_EXPIRED처럼 재발급 가능한 errorCode일 때만 시도하는 것이 좋다.

Q. 403도 Interceptor에서 Reissue해야 해?
A. 아니다. 403은 권한 부족이므로 Token 재발급 대상이 아니다.

---

## 8.2 Reissue Loop Prevention

### [개념]

Reissue Loop Prevention은 Access Token 재발급 실패 또는 Reissue API 자체 실패 시 무한 재시도 루프가 발생하지 않도록 방지하는 설계다.

---

### [핵심]

무한 루프 원인:

- 모든 401에 Reissue 시도
- Reissue API 401에도 Reissue 반복
- Refresh Token 만료 후 재시도 반복
- 새 Access Token 저장 실패
- 동시 요청 중복 Reissue
- errorCode 미구분

방지 기준:

- `_retry` flag
- Reissue API 제외
- errorCode 분기
- Refresh 실패 시 Logout
- Pending request queue
- Single refresh request

---

### [실무]

Frontend 흐름:

```text
401 TOKEN_EXPIRED 수신
→ 기존 요청이 retry된 적 있는지 확인
→ Reissue API가 아닌지 확인
→ Reissue 요청
→ 성공 시 원 요청 1회 재시도
→ 실패 시 Logout
```

Backend 제공 기준:

```text
Access Token 만료
→ TOKEN_EXPIRED

Refresh Token 만료
→ REFRESH_TOKEN_INVALID 또는 REFRESH_TOKEN_EXPIRED

권한 부족
→ ACCESS_DENIED
```

권장:

- Reissue API 실패는 즉시 Logout 처리한다.
- `_retry` flag로 동일 요청 반복을 막는다.
- 동시 요청이 많을 때 Reissue 요청을 하나로 합치는 전략을 검토한다.
- Backend는 errorCode를 안정적으로 제공한다.
- Refresh Token Rotation 사용 시 새 Refresh Token 저장 완료 후 재시도한다.

---

### [FAQ]

Q. Reissue 무한 루프는 왜 생겨?
A. 모든 401에 재발급을 시도하거나 Reissue API 실패에도 다시 Reissue를 호출하면 발생한다.

Q. Reissue API가 401이면 어떻게 해야 해?
A. Refresh Token이 유효하지 않다고 보고 Logout 또는 재로그인으로 처리해야 한다.

Q. 동시에 여러 요청이 만료되면 어떻게 해?
A. Reissue 요청을 하나로 모으고 나머지 요청은 대기시키는 queue 전략을 검토할 수 있다.

---

# 9. Protected Route and Auth State

## 9.1 Frontend Protected Route Rules

### [개념]

Frontend Protected Route는 로그인 상태가 필요한 화면 접근을 제한하는 UX 기능이다.

Protected Route는 사용자 경험을 위한 Client-side Guard이며 Backend API 보안을 대체하지 않는다.

---

### [핵심]

Protected Route 사용 후보:

- 내 정보 페이지
- 글 작성 페이지
- 결제 페이지
- 알림 페이지
- 관리자 페이지
- 사용자 설정 페이지

Frontend Guard 기준:

- Access Token 존재 여부
- Auth State
- User Summary
- Role
- Route Meta
- Loading State

---

### [실무]

Frontend Protected Route Flow:

```text
Route 진입
→ Auth State 확인
→ Access Token 확인
→ 필요 시 /api/users/me 호출
→ 인증됨
→ Page Render
→ 인증 안 됨
→ Login Page Redirect
```

관리자 Route Flow:

```text
Admin Route 진입
→ Auth State 확인
→ User Role 확인
→ ROLE_ADMIN이면 Render
→ 아니면 권한 없음 Page
```

Backend 기준:

```text
Frontend Protected Route
→ UX Guard

Backend SecurityFilterChain
→ 실제 API 보호
```

권장:

- Frontend Route 보호와 Backend API 보호를 분리해서 이해한다.
- 관리자 화면 숨김만으로 Admin API를 보호하지 않는다.
- 새로고침 시 Auth State 복구 전략을 둔다.
- `/api/users/me` 같은 사용자 요약 API를 제공한다.
- Role은 UX 판단에 사용할 수 있지만 최종 검증은 Backend에서 한다.

---

### [FAQ]

Q. Frontend Protected Route가 있으면 Backend 인증은 필요 없어?
A. 아니다. Frontend 보호는 UX이고 실제 API 보안은 Backend에서 수행해야 한다.

Q. 관리자 메뉴를 숨기면 Admin API도 안전해?
A. 아니다. 사용자가 직접 API를 호출할 수 있으므로 Backend에서 Role 검증이 필요하다.

Q. 새로고침하면 로그인 상태가 사라지면 어떻게 해?
A. Token 저장 전략과 `/api/users/me` 또는 Reissue 흐름으로 Auth State를 복구해야 한다.

---

## 9.2 User Summary API Rules

### [개념]

User Summary API는 Frontend가 현재 로그인한 사용자 정보를 확인하기 위해 호출하는 API다.

보통 `/api/users/me` 형태로 제공하며 SecurityContext의 Principal을 기준으로 사용자 정보를 반환한다.

---

### [핵심]

User Summary API 포함 후보:

- userId
- email
- nickname
- role
- profileImage
- accountStatus
- provider

제외 대상:

- password
- encodedPassword
- refreshToken
- accessToken
- secret
- 민감 개인정보

---

### [실무]

Controller 예:

```java
@GetMapping("/api/users/me")
public ApiResponse<UserSummaryResponse> me(
        @AuthenticationPrincipal CustomUserPrincipal principal
) {
    return ApiResponse.success(
            userService.getSummary(principal.userId())
    );
}
```

Response 예:

```java
public record UserSummaryResponse(
        Long userId,
        String email,
        String nickname,
        String role,
        String profileImage
) {
}
```

권장:

- `/me` API는 Protected API로 설정한다.
- Principal userId 기준으로 조회한다.
- RequestParam userId를 받지 않는다.
- 응답에는 화면 표시와 권한 UX에 필요한 최소 정보만 포함한다.
- 비밀번호와 Token을 반환하지 않는다.
- Frontend Auth State 복구에 사용할 수 있다.

---

### [FAQ]

Q. /api/users/me는 왜 필요해?
A. Frontend가 현재 로그인한 사용자 정보를 확인하고 Auth State를 복구하기 위해 필요하다.

Q. /me API에서 userId를 파라미터로 받아도 돼?
A. 아니다. 현재 인증 사용자는 Principal 기준으로 판단해야 한다.

Q. User Summary Response에 role을 포함해도 돼?
A. 가능하다. Frontend 권한 UX에 사용할 수 있지만 Backend 권한 검증을 대체하지 않는다.

---

# 10. Logout Integration

## 10.1 Frontend Logout Flow

### [개념]

Frontend Logout Flow는 사용자가 로그아웃할 때 Client Token을 제거하고 Backend Refresh Token을 무효화하는 연동 흐름이다.

JWT 구조에서는 Client Token 삭제만으로 충분하지 않으며 Backend 저장 Refresh Token도 삭제해야 한다.

---

### [핵심]

Logout Flow:

```text
Logout Click
→ Backend Logout API 호출
→ Refresh Token 삭제 또는 무효화
→ Cookie Refresh Token 제거
→ Frontend Access Token 제거
→ Auth State 초기화
→ Login Page 또는 Home 이동
```

Backend Logout API:

```text
POST /api/auth/logout
Authorization: Bearer AccessToken
```

---

### [실무]

Backend Logout 응답 시 Cookie 제거 예:

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

Frontend 처리 기준:

```text
Logout API 성공
→ Access Token 제거
→ User State 제거
→ Refresh Token Cookie 제거 응답 반영
→ Login Page 이동
```

권장:

- Logout API는 Protected API로 둔다.
- Principal 기준으로 Refresh Token을 삭제한다.
- Cookie 방식이면 Set-Cookie maxAge=0으로 제거한다.
- Reissue 실패 시에도 Client Token을 제거한다.
- 비밀번호 변경 / 탈퇴 시 전체 Refresh Token 삭제를 검토한다.

---

### [FAQ]

Q. 로그아웃 시 Frontend에서 Token만 삭제하면 돼?
A. 부족하다. Backend에 저장된 Refresh Token도 삭제하거나 무효화해야 한다.

Q. Cookie Refresh Token은 로그아웃 때 어떻게 제거해?
A. 같은 Path와 속성으로 maxAge=0인 Set-Cookie를 내려 제거한다.

Q. 로그아웃 API는 인증이 필요해?
A. 일반적으로 필요하다. 현재 인증 사용자 기준으로 Refresh Token을 무효화해야 하기 때문이다.

---

# 11. OAuth2 and Frontend Security Anti Pattern

## 11.1 OAuth2 Anti Pattern

### [개념]

OAuth2 Anti Pattern은 Provider 인증 결과를 과도하게 신뢰하거나 Redirect / Token 전달 / 계정 Mapping을 잘못 설계해 보안 문제가 발생하는 구현 방식이다.

---

### [핵심]

대표 Anti Pattern:

- email만으로 OAuth2 사용자 식별
- providerId 저장 누락
- Provider별 attribute 구조 하드코딩 분산
- email_verified 미확인 자동 연결
- Redirect URL 검증 없음
- Open Redirect 허용
- Access Token을 Query Parameter로 전달
- Refresh Token을 Query Parameter로 전달
- One-time Code 만료 / 1회성 처리 없음
- Token 원문 로그 출력
- Provider 응답 원본 전체 저장
- 탈퇴 / 정지 사용자 OAuth2 Login 허용
- OAuth2 사용자 Role 미부여
- OAuth2 Login 후 Backend 권한 검증 생략

---

### [실무]

잘못된 예:

```text
OAuth2 Success
→ email만으로 User 조회
→ email 일치하면 자동 로그인
→ email 신뢰성 낮은 Provider에서 계정 연결 위험
```

잘못된 Token 전달 예:

```text
OAuth2 Success
→ /oauth2/success?accessToken=...&refreshToken=...
→ Browser History / Server Log / Referer 노출 위험
```

수정 방향:

```text
OAuth2 Success
→ provider + providerId로 User 조회
→ 없으면 email_verified 확인
→ 계정 연결 정책 적용
→ Local User 생성 / 연결
→ One-time Code 또는 HttpOnly Cookie 방식으로 인증 연동
```

Review 기준:

```text
providerId 저장 확인
→ provider + providerId 조회 확인
→ Redirect URL 검증 확인
→ Token 전달 방식 확인
→ One-time Code 만료 / 1회성 확인
→ SuccessHandler 로그 확인
→ OAuth2 User Role 확인
→ 계정 상태 검증 확인
```

---

### [FAQ]

Q. OAuth2에서 가장 위험한 실수는 뭐야?
A. email만으로 사용자를 식별하거나 검증 없는 Redirect URL로 Token을 전달하는 것이다.

Q. Refresh Token을 URL Query로 보내도 돼?
A. 권장하지 않는다. URL 기록, 로그, Referer로 노출될 수 있어 위험하다.

Q. OAuth2 사용자도 정지 상태를 확인해야 해?
A. 해야 한다. Local User 상태가 정지 / 탈퇴라면 로그인과 Token 발급을 차단해야 한다.

Q. One-time Code를 쓰면 무조건 안전해?
A. 아니다. 짧은 만료 시간, 1회성 사용, 사용 후 폐기, Redirect URL 검증이 함께 필요하다.

---

## 11.2 Frontend Auth Anti Pattern

### [개념]

Frontend Auth Anti Pattern은 Frontend 로그인 상태나 Token 저장만으로 보안이 완성되었다고 오해하거나 401 / 403 처리와 Reissue 흐름을 잘못 구현하는 문제다.

---

### [핵심]

대표 Anti Pattern:

- Frontend 로그인 상태만 신뢰
- Admin 메뉴 숨김만으로 Admin API 보호
- 401과 403을 동일하게 처리
- 모든 401에 Reissue 시도
- Reissue API 실패에도 무한 재시도
- 403에도 Token 재발급 시도
- Access Token 장기 저장
- Refresh Token 저장 위험 미검토
- Logout 시 Client Token만 삭제
- OAuth2 Success URL에서 Token 원문 파싱
- CORS Authorization Header 미설정
- Cookie credentials 설정 불일치

---

### [실무]

잘못된 처리:

```text
403 ACCESS_DENIED
→ Reissue 시도
→ 새 Token 발급
→ 다시 403
→ 반복 또는 잘못된 UX
```

수정 처리:

```text
403 ACCESS_DENIED
→ 권한 없음 안내
→ Reissue 시도하지 않음
```

OAuth2 잘못된 처리:

```text
Frontend가 URL Query에서 accessToken / refreshToken 직접 파싱
→ URL 노출 위험 증가
```

OAuth2 권장 처리:

```text
Frontend가 URL Query에서 oneTimeCode만 파싱
→ Token Exchange API 호출
→ Token 수신 후 URL code 제거
```

Review 기준:

```text
401 TOKEN_EXPIRED 처리 확인
→ Reissue 실패 처리 확인
→ 403 처리 확인
→ OAuth2 code exchange 처리 확인
→ Logout API 호출 확인
→ Token 저장 위치 확인
→ CORS Authorization Header 확인
→ credentials 정책 확인
```

권장:

- Frontend Auth는 UX로 이해한다.
- Backend API Security를 최종 기준으로 둔다.
- 401 / 403 errorCode를 분리 처리한다.
- Reissue 무한 루프를 방지한다.
- Logout 시 Backend Refresh Token 무효화를 호출한다.
- OAuth2 Success 후 URL에 남은 code는 교환 후 제거한다.

---

### [FAQ]

Q. Frontend Auth에서 가장 흔한 실수는 뭐야?
A. Frontend 로그인 상태만 믿거나 401과 403을 구분하지 않는 것이다.

Q. Admin Route를 숨기면 보안이 되는 거야?
A. 아니다. Admin API는 Backend에서 Role 검증을 해야 한다.

Q. Reissue 실패 후에도 계속 재시도하면 안 돼?
A. 안 된다. Refresh Token이 유효하지 않으면 Logout 처리하고 재로그인을 요구해야 한다.

Q. OAuth2 Success URL에서 Token을 직접 파싱해도 돼?
A. 권장하지 않는다. One-time Code를 교환하는 방식으로 처리하고 URL의 code는 교환 후 제거하는 것이 좋다.

---

# 12. OAuth2 and Frontend Auth Testing

## 12.1 OAuth2 Login Test Rules

### [개념]

OAuth2 Login Test는 Provider 인증, Local User Mapping, 인증 수단 발급, Redirect, 계정 상태 검증이 정상 동작하는지 확인하는 테스트다.

---

### [핵심]

테스트 대상:

- OAuth2 Login 시작
- Provider Callback
- 신규 OAuth2 사용자 가입
- 기존 OAuth2 사용자 로그인
- provider + providerId Mapping
- email 누락
- 정지 / 탈퇴 사용자 차단
- SuccessHandler One-time Code 발급
- Token Exchange API
- FailureHandler Redirect
- Frontend Redirect URL 검증
- Open Redirect 방지

---

### [실무]

테스트 시나리오:

```text
신규 OAuth2 사용자
→ Provider 인증 성공
→ Local User 생성
→ ROLE_USER 부여
→ One-time Code 발급
→ Frontend Success Redirect
→ Token Exchange API 호출
→ Access Token / Refresh Token 발급
```

```text
기존 OAuth2 사용자
→ provider + providerId 조회 성공
→ One-time Code 발급
→ Token Exchange 성공
```

```text
정지 사용자
→ OAuth2 인증 성공
→ Local User 상태 확인
→ Token 발급 차단
→ Failure Redirect
```

```text
사용 완료된 One-time Code 재사용
→ Token Exchange 실패
→ 401 또는 정책별 인증 실패
```

검증 기준:

- providerId가 저장되는가?
- email만으로 조회하지 않는가?
- Role이 부여되는가?
- One-time Code가 짧은 만료 시간을 가지는가?
- One-time Code가 1회만 사용되는가?
- Token Exchange 후 Refresh Token이 저장되는가?
- Redirect URL이 허용 목록 기준인가?
- Token이 URL Query나 로그에 노출되지 않는가?

---

### [FAQ]

Q. OAuth2 Login 테스트에서 가장 중요한 것은 뭐야?
A. provider + providerId Mapping, Local User 생성 / 조회, One-time Code 발급, Token Exchange, Redirect URL 검증이다.

Q. Provider 인증이 성공하면 무조건 로그인 성공이야?
A. 아니다. Local User Mapping, 계정 상태, 필수 정보, 서비스 정책 검증이 통과해야 한다.

Q. OAuth2 신규 사용자는 어떤 Role을 받아야 해?
A. 프로젝트 기본 정책에 따라 일반적으로 ROLE_USER를 부여한다.

Q. One-time Code 테스트는 뭘 확인해?
A. 만료 시간, 1회성 사용, 사용 후 폐기, 재사용 차단을 확인해야 한다.

---

## 12.2 Frontend Auth Integration Test Rules

### [개념]

Frontend Auth Integration Test는 Backend Token API와 Frontend Interceptor, Protected Route, Logout 흐름이 정상적으로 연결되는지 검증하는 테스트다.

---

### [핵심]

테스트 대상:

- Login Response
- OAuth2 Token Exchange Response
- Authorization Header 첨부
- `/api/users/me`
- Access Token 만료
- Reissue 성공
- Reissue 실패
- 403 권한 부족
- Logout
- Refresh Token Cookie 제거
- CORS Authorization Header
- OAuth2 Success URL code 제거

---

### [실무]

테스트 시나리오:

```text
Login 성공
→ Access Token 저장
→ Authorization Header 첨부
→ /api/users/me 200
```

```text
OAuth2 Success Redirect
→ URL code 추출
→ Token Exchange API 호출
→ Access Token 저장
→ URL code 제거
→ /api/users/me 200
```

```text
Access Token 만료
→ API 401 TOKEN_EXPIRED
→ Reissue 성공
→ 원 요청 재시도
→ 200
```

```text
Refresh Token 만료
→ Reissue 401 REFRESH_TOKEN_INVALID
→ Client Token 제거
→ Login Page 이동
```

```text
User Role로 Admin API 접근
→ 403 ACCESS_DENIED
→ Reissue 시도하지 않음
→ 권한 없음 안내
```

검증 기준:

- 401 / 403 errorCode가 분리되는가?
- Reissue 무한 루프가 없는가?
- Authorization Header가 CORS에서 허용되는가?
- Cookie 방식이면 credentials 설정이 맞는가?
- Logout 후 Reissue가 실패하는가?
- OAuth2 Success URL에서 Token 원문이 노출되지 않는가?
- Protected Route가 Backend API 보안을 대체하지 않는가?

---

### [FAQ]

Q. Frontend Auth 연동 테스트에서 가장 중요한 것은 뭐야?
A. Authorization Header 첨부, 401 Reissue, 403 권한 없음, OAuth2 Code Exchange, Logout 후 Reissue 차단이다.

Q. 403이 발생했을 때 Reissue가 호출되면 문제야?
A. 문제다. 403은 권한 부족이므로 Token 재발급 대상이 아니다.

Q. Logout 후 Reissue가 성공하면 문제야?
A. 문제다. Refresh Token 삭제 또는 무효화가 제대로 되지 않은 것이다.

Q. OAuth2 Success URL에 Token 원문이 보이면 문제야?
A. 문제다. URL 기록, 로그, Referer로 노출될 수 있으므로 One-time Code 방식으로 수정하는 것이 좋다.

---

# 13. Part07 Checklist

## 13.1 OAuth2 Frontend Integration Checklist

### [개념]

Part07 Checklist는 OAuth2 Login과 Frontend Auth Integration이 Security Advanced 기준에 맞게 설계되었는지 검수하기 위한 목록이다.

---

### [핵심]

Checklist:

```md
- [ ] OAuth2 Login 흐름이 포함되었는가?
- [ ] Provider Identity 기준이 포함되었는가?
- [ ] provider + providerId 식별 기준이 포함되었는가?
- [ ] email 단독 식별 금지가 포함되었는가?
- [ ] Provider Attribute Mapping 기준이 포함되었는가?
- [ ] Local User Mapping 기준이 포함되었는가?
- [ ] OAuth2 최초 로그인 회원 생성 정책이 포함되었는가?
- [ ] 기존 계정 연결 정책이 포함되었는가?
- [ ] SuccessHandler 기준이 포함되었는가?
- [ ] One-time Code 교환 방식이 포함되었는가?
- [ ] HttpOnly Cookie 방식 기준이 포함되었는가?
- [ ] URL Query Token 전달 비권장 기준이 포함되었는가?
- [ ] FailureHandler 기준이 포함되었는가?
- [ ] JWT 발급과 Refresh Token 저장 기준이 포함되었는가?
- [ ] Redirect URI와 Frontend Redirect URL 구분이 포함되었는가?
- [ ] Open Redirect 방지 기준이 포함되었는가?
- [ ] OAuth2 SecurityFilterChain 설정 기준이 포함되었는가?
- [ ] Frontend Auth Integration 기준이 포함되었는가?
- [ ] Token Storage 기준이 포함되었는가?
- [ ] Axios Interceptor 기준이 포함되었는가?
- [ ] Reissue Loop Prevention 기준이 포함되었는가?
- [ ] Protected Route는 UX용이라는 점이 포함되었는가?
- [ ] User Summary API 기준이 포함되었는가?
- [ ] Logout Integration 기준이 포함되었는가?
- [ ] OAuth2 Anti Pattern이 포함되었는가?
- [ ] Frontend Auth Anti Pattern이 포함되었는가?
- [ ] OAuth2 Login Test 기준이 포함되었는가?
- [ ] Frontend Auth Integration Test 기준이 포함되었는가?
- [ ] Retrieval Queries가 충분한가?
```

---

### [실무]

Review Flow:

```text
OAuth2 Provider 설정 확인
→ Provider Attribute Mapping 확인
→ Local User Mapping 확인
→ provider + providerId 저장 확인
→ SuccessHandler One-time Code 발급 확인
→ Token Exchange API 확인
→ Refresh Token 저장 확인
→ Redirect URL 검증 확인
→ URL Query Token 전달 여부 확인
→ Frontend Token 전달 방식 확인
→ 401 / 403 errorCode 계약 확인
→ Reissue Flow 확인
→ Logout Integration 확인
→ OAuth2 / Frontend Auth 테스트 확인
```

선행 문서 연결:

```text
Part01 Core Concepts
→ Authentication / Authorization / Principal 기준 제공

Part02 SecurityFilterChain
→ oauth2Login / permitAll / JWT Filter 기준 제공

Part03 Password Login Logout
→ Login / Refresh Token / Logout 기준 제공

Part04 JWT
→ Access Token / Refresh Token / Reissue 기준 제공

Part06 Exception CORS CSRF
→ 401 / 403 / CORS / CSRF / Cookie 기준 제공
```

후속 문서 연결:

```text
Part07 OAuth2 Frontend Integration
→ Part08 Security Testing Troubleshooting
```

---

### [FAQ]

Q. Part07에서 가장 중요한 검수 포인트는 뭐야?
A. provider + providerId 식별, Local User Mapping, One-time Code 또는 HttpOnly Cookie 기반 Token 전달, Redirect URL 검증, 401/403 Frontend 연동이다.

Q. Part07은 JWT 문서와 어떻게 연결돼?
A. OAuth2 Login 성공 후 Access Token과 Refresh Token을 안전하게 발급하고 Reissue / Logout 흐름으로 이어진다.

Q. Part07은 CORS / CSRF 문서와 어떻게 연결돼?
A. Frontend Authorization Header, Cookie Refresh Token, credentials, SameSite, CSRF 검토 기준으로 연결된다.

---

# Retrieval Queries

### [FAQ]

Q. OAuth2 Login은 뭐야?
A. Google, Kakao, Naver 같은 외부 Provider를 통해 사용자를 인증하고 Application 계정과 연결하는 로그인 방식이다.

Q. OAuth2 Login을 쓰면 JWT가 필요 없어?
A. 아니다. OAuth2로 외부 인증을 받은 뒤 자체 API 인증을 위해 JWT를 발급하는 구조를 사용할 수 있다.

Q. OAuth2 Login에서 가장 중요한 Backend 작업은 뭐야?
A. Provider 사용자 정보를 Local User와 안전하게 Mapping하고 Application 인증 수단을 안전하게 발급 / 전달하는 것이다.

Q. OAuth2 성공 후 Token을 URL Query로 보내도 돼?
A. 권장하지 않는다. 브라우저 기록, 로그, Referer로 노출될 수 있으므로 One-time Code 교환 방식이나 HttpOnly Cookie 방식을 우선 검토한다.

Q. OAuth2 사용자는 어떻게 식별해?
A. 일반적으로 provider와 providerId 조합으로 식별한다. email만으로 식별하면 변경이나 중복 문제가 생길 수 있다.

Q. OAuth2 Provider email을 그대로 믿어도 돼?
A. Provider와 email_verified 여부에 따라 다르다. 프로젝트 정책에 맞게 검증 기준을 정해야 한다.

Q. providerId는 왜 저장해?
A. Provider가 보장하는 사용자 고유 식별자를 Local User와 연결하기 위해 필요하다.

Q. OAuth2 Provider마다 응답 구조가 달라?
A. 다르다. Google, Kakao, Naver는 사용자 정보 attribute 구조가 다르므로 Provider별 Mapping이 필요하다.

Q. Provider별 Mapping 로직은 어디에 두는 게 좋아?
A. OAuth2UserInfo 구현체나 Mapper / Factory로 분리하는 것이 좋다.

Q. email이 없는 Provider 응답은 어떻게 처리해?
A. 프로젝트 정책에 따라 가입을 제한하거나 추가 정보 입력 화면으로 연결해야 한다.

Q. OAuth2 로그인 후 User Entity가 꼭 필요해?
A. 대부분 필요하다. Application 권한, 서비스 데이터, JWT 발급, 계정 상태 관리를 위해 Local User가 필요하다.

Q. OAuth2 최초 로그인 시 회원가입을 자동으로 해도 돼?
A. 가능하다. 다만 필수 약관, 추가 정보 입력, 기본 권한 부여 정책을 정해야 한다.

Q. OAuth2 사용자도 Role이 필요해?
A. 필요하다. Application API 접근 권한은 Backend Role / Authority 기준으로 검증해야 한다.

Q. 같은 email이면 기존 계정과 자동 연결해도 돼?
A. 신중해야 한다. Provider의 email_verified 여부와 추가 인증 정책을 확인해야 한다.

Q. 여러 OAuth2 Provider를 한 계정에 연결하려면 어떻게 해?
A. User와 OAuthAccount를 분리해 userId, provider, providerId 조합으로 관리하는 구조를 검토한다.

Q. OAuth2 계정 연결 해제도 필요해?
A. 서비스 정책에 따라 필요할 수 있다. 마지막 로그인 수단인지 확인하고 연결 해제 제한을 둘 수 있다.

Q. OAuth2 SuccessHandler는 뭐 하는 곳이야?
A. OAuth2 인증 성공 후 Local User 확인, One-time Code 발급, Frontend Redirect 같은 후속 처리를 수행한다.

Q. OAuth2 성공 후 JWT를 어디서 발급해?
A. 안전한 구조에서는 SuccessHandler가 One-time Code를 발급하고, 별도 Token Exchange API에서 JWT를 발급할 수 있다.

Q. Access Token을 Redirect Query로 보내도 돼?
A. 권장하지 않는다. 브라우저 기록, 로그, Referer로 노출될 수 있으므로 One-time Code 교환 방식이나 HttpOnly Cookie 방식을 우선 검토한다.

Q. One-time Code는 왜 써?
A. Token 원문을 URL로 직접 전달하지 않고, 짧은 수명의 1회용 Code를 통해 안전하게 Token을 교환하기 위해 사용한다.

Q. OAuth2 성공 후 Refresh Token을 HttpOnly Cookie로 내려도 돼?
A. 가능하다. 다만 SameSite, Secure, CSRF, CORS credentials 정책을 함께 검토해야 한다.

Q. HttpOnly Cookie 방식이면 XSS가 완전히 해결돼?
A. 아니다. JavaScript가 Cookie를 직접 읽기 어렵게 할 뿐이며 CSRF와 다른 XSS 피해는 별도로 검토해야 한다.

Q. Cookie 방식이면 CORS에서 뭘 맞춰야 해?
A. Backend allowCredentials, 명시적 allowedOrigins, Frontend withCredentials 설정을 맞춰야 한다.

Q. OAuth2 로그인 실패는 어떻게 처리해?
A. FailureHandler에서 Frontend 실패 URL로 Redirect하고 errorCode를 전달하는 방식이 일반적이다.

Q. Provider 오류 상세를 사용자에게 보여줘도 돼?
A. 권장하지 않는다. 사용자에게는 짧은 실패 메시지를 보여주고 상세 원인은 서버 로그에서 확인한다.

Q. OAuth2 실패도 401 응답이야?
A. Redirect 기반 OAuth2 Login에서는 실패 URL로 Redirect하는 경우가 많다. REST API 방식이면 401 또는 적절한 errorCode로 처리할 수 있다.

Q. OAuth2 Login 경로도 permitAll이 필요해?
A. 필요하다. 사용자가 인증 전 OAuth2 Login을 시작하고 Provider Callback을 받아야 하기 때문이다.

Q. JWT Filter가 OAuth2 Login을 방해할 수 있어?
A. 잘못 구현하면 Token 없는 OAuth2 경로를 401로 막을 수 있다. Public 경로와 Filter 동작을 확인해야 한다.

Q. OAuth2 Login과 JWT Login을 같이 쓸 수 있어?
A. 가능하다. OAuth2 인증 성공 후 자체 JWT 또는 One-time Code 교환 방식을 통해 API 인증에 사용할 수 있다.

Q. Provider Redirect URI와 Frontend Redirect URL은 달라?
A. 다르다. Provider Redirect URI는 Backend Callback이고 Frontend Redirect URL은 로그인 처리 후 사용자를 이동시킬 Client URL이다.

Q. Redirect URL을 요청 파라미터로 받아도 돼?
A. 검증 없이 사용하면 Open Redirect 위험이 있으므로 허용 목록 기반으로 제한해야 한다.

Q. OAuth2 Redirect URI가 틀리면 어떻게 돼?
A. Provider 인증 후 Callback이 실패하거나 redirect_uri mismatch 오류가 발생할 수 있다.

Q. Redirect URL에 Token을 직접 붙여도 돼?
A. 권장하지 않는다. Token 원문 대신 One-time Code를 붙이고 별도 API에서 Token을 교환하는 방식이 안전하다.

Q. Frontend Auth Integration에서 Backend가 정해야 할 것은 뭐야?
A. Token 발급 형식, OAuth2 Token Exchange API, Reissue API, Logout API, 401/403 errorCode, CORS 정책, 사용자 정보 API를 명확히 해야 한다.

Q. Frontend 로그인 상태만 확인하면 보안이 돼?
A. 아니다. Frontend 로그인 상태는 UX용이고 실제 API 접근 권한은 Backend에서 검증해야 한다.

Q. 403을 받으면 Frontend는 Token 재발급을 해야 해?
A. 아니다. 403은 권한 부족이므로 권한 없음 안내나 접근 차단 처리가 맞다.

Q. Access Token은 어디에 저장하는 게 좋아?
A. 정답은 없다. Memory, LocalStorage, Cookie 각각 장단점이 있어 XSS, CSRF, UX를 기준으로 선택해야 한다.

Q. Access Token을 LocalStorage에 저장해도 돼?
A. 구현은 쉽지만 XSS에 취약하므로 위험을 이해하고 사용해야 한다.

Q. Authorization Header를 쓰면 Backend에서 뭘 허용해야 해?
A. CORS allowedHeaders에 Authorization을 포함해야 브라우저 요청이 차단되지 않는다.

Q. Refresh Token은 어디에 저장하는 게 좋아?
A. HttpOnly Cookie를 자주 검토하지만 CSRF 설정이 필요하다. LocalStorage는 XSS 위험이 있어 주의해야 한다.

Q. Refresh Token을 Cookie에 넣으면 안전해?
A. JS 접근은 막을 수 있지만 CSRF와 SameSite, Secure 설정을 함께 검토해야 한다.

Q. Refresh Token을 LocalStorage에 넣어도 돼?
A. 가능은 하지만 XSS에 취약하므로 위험을 명확히 이해하고 사용해야 한다.

Q. Axios Interceptor는 왜 써?
A. API 요청마다 Access Token을 붙이고 Token 만료 시 재발급을 자동 처리하기 위해 사용한다.

Q. 401이면 항상 Reissue를 시도해도 돼?
A. 아니다. TOKEN_EXPIRED처럼 재발급 가능한 errorCode일 때만 시도하는 것이 좋다.

Q. 403도 Interceptor에서 Reissue해야 해?
A. 아니다. 403은 권한 부족이므로 Token 재발급 대상이 아니다.

Q. Reissue 무한 루프는 왜 생겨?
A. 모든 401에 재발급을 시도하거나 Reissue API 실패에도 다시 Reissue를 호출하면 발생한다.

Q. Reissue API가 401이면 어떻게 해야 해?
A. Refresh Token이 유효하지 않다고 보고 Logout 또는 재로그인으로 처리해야 한다.

Q. 동시에 여러 요청이 만료되면 어떻게 해?
A. Reissue 요청을 하나로 모으고 나머지 요청은 대기시키는 queue 전략을 검토할 수 있다.

Q. Frontend Protected Route가 있으면 Backend 인증은 필요 없어?
A. 아니다. Frontend 보호는 UX이고 실제 API 보안은 Backend에서 수행해야 한다.

Q. 관리자 메뉴를 숨기면 Admin API도 안전해?
A. 아니다. 사용자가 직접 API를 호출할 수 있으므로 Backend에서 Role 검증이 필요하다.

Q. 새로고침하면 로그인 상태가 사라지면 어떻게 해?
A. Token 저장 전략과 `/api/users/me` 또는 Reissue 흐름으로 Auth State를 복구해야 한다.

Q. /api/users/me는 왜 필요해?
A. Frontend가 현재 로그인한 사용자 정보를 확인하고 Auth State를 복구하기 위해 필요하다.

Q. /me API에서 userId를 파라미터로 받아도 돼?
A. 아니다. 현재 인증 사용자는 Principal 기준으로 판단해야 한다.

Q. User Summary Response에 role을 포함해도 돼?
A. 가능하다. Frontend 권한 UX에 사용할 수 있지만 Backend 권한 검증을 대체하지 않는다.

Q. 로그아웃 시 Frontend에서 Token만 삭제하면 돼?
A. 부족하다. Backend에 저장된 Refresh Token도 삭제하거나 무효화해야 한다.

Q. Cookie Refresh Token은 로그아웃 때 어떻게 제거해?
A. 같은 Path와 속성으로 maxAge=0인 Set-Cookie를 내려 제거한다.

Q. 로그아웃 API는 인증이 필요해?
A. 일반적으로 필요하다. 현재 인증 사용자 기준으로 Refresh Token을 무효화해야 하기 때문이다.

Q. OAuth2에서 가장 위험한 실수는 뭐야?
A. email만으로 사용자를 식별하거나 검증 없는 Redirect URL로 Token을 전달하는 것이다.

Q. Refresh Token을 URL Query로 보내도 돼?
A. 권장하지 않는다. URL 기록, 로그, Referer로 노출될 수 있어 위험하다.

Q. OAuth2 사용자도 정지 상태를 확인해야 해?
A. 해야 한다. Local User 상태가 정지 / 탈퇴라면 로그인과 Token 발급을 차단해야 한다.

Q. One-time Code를 쓰면 무조건 안전해?
A. 아니다. 짧은 만료 시간, 1회성 사용, 사용 후 폐기, Redirect URL 검증이 함께 필요하다.

Q. Frontend Auth에서 가장 흔한 실수는 뭐야?
A. Frontend 로그인 상태만 믿거나 401과 403을 구분하지 않는 것이다.

Q. Admin Route를 숨기면 보안이 되는 거야?
A. 아니다. Admin API는 Backend에서 Role 검증을 해야 한다.

Q. Reissue 실패 후에도 계속 재시도하면 안 돼?
A. 안 된다. Refresh Token이 유효하지 않으면 Logout 처리하고 재로그인을 요구해야 한다.

Q. OAuth2 Success URL에서 Token을 직접 파싱해도 돼?
A. 권장하지 않는다. One-time Code를 교환하는 방식으로 처리하고 URL의 code는 교환 후 제거하는 것이 좋다.

Q. OAuth2 Login 테스트에서 가장 중요한 것은 뭐야?
A. provider + providerId Mapping, Local User 생성 / 조회, One-time Code 발급, Token Exchange, Redirect URL 검증이다.

Q. Provider 인증이 성공하면 무조건 로그인 성공이야?
A. 아니다. Local User Mapping, 계정 상태, 필수 정보, 서비스 정책 검증이 통과해야 한다.

Q. OAuth2 신규 사용자는 어떤 Role을 받아야 해?
A. 프로젝트 기본 정책에 따라 일반적으로 ROLE_USER를 부여한다.

Q. One-time Code 테스트는 뭘 확인해?
A. 만료 시간, 1회성 사용, 사용 후 폐기, 재사용 차단을 확인해야 한다.

Q. Frontend Auth 연동 테스트에서 가장 중요한 것은 뭐야?
A. Authorization Header 첨부, 401 Reissue, 403 권한 없음, OAuth2 Code Exchange, Logout 후 Reissue 차단이다.

Q. 403이 발생했을 때 Reissue가 호출되면 문제야?
A. 문제다. 403은 권한 부족이므로 Token 재발급 대상이 아니다.

Q. Logout 후 Reissue가 성공하면 문제야?
A. 문제다. Refresh Token 삭제 또는 무효화가 제대로 되지 않은 것이다.

Q. OAuth2 Success URL에 Token 원문이 보이면 문제야?
A. 문제다. URL 기록, 로그, Referer로 노출될 수 있으므로 One-time Code 방식으로 수정하는 것이 좋다.

Q. Part07에서 가장 중요한 검수 포인트는 뭐야?
A. provider + providerId 식별, Local User Mapping, One-time Code 또는 HttpOnly Cookie 기반 Token 전달, Redirect URL 검증, 401/403 Frontend 연동이다.

Q. Part07은 JWT 문서와 어떻게 연결돼?
A. OAuth2 Login 성공 후 Access Token과 Refresh Token을 안전하게 발급하고 Reissue / Logout 흐름으로 이어진다.

Q. Part07은 CORS / CSRF 문서와 어떻게 연결돼?
A. Frontend Authorization Header, Cookie Refresh Token, credentials, SameSite, CSRF 검토 기준으로 연결된다.
