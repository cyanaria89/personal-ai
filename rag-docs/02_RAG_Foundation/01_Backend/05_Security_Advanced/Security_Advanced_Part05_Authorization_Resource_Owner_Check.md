# Security Advanced Part05 - Authorization and Resource Owner Check

---

# 1. Authorization Overview

## 1.1 Authorization Concept

### [개념]

Authorization은 인증된 사용자가 특정 API, 리소스, 기능에 접근할 권한이 있는지 확인하는 과정이다.

Spring Security에서 Authorization은 Role, Authority, Method Security, Resource Owner Check, 비즈니스 권한 검증을 통해 수행된다.

Authentication이 사용자가 누구인지 확인하는 과정이라면 Authorization은 그 사용자가 무엇을 할 수 있는지 확인하는 과정이다.

---

### [핵심]

Authorization 핵심 키워드:

- Authorization
- Role
- Authority
- GrantedAuthority
- ROLE_USER
- ROLE_ADMIN
- hasRole
- hasAuthority
- @PreAuthorize
- Method Security
- Resource Owner Check
- AccessDeniedHandler
- 403 Forbidden

Authorization 판단 질문:

```text
이 사용자는 이 API에 접근할 수 있는가?
이 사용자는 이 리소스를 수정할 수 있는가?
이 사용자는 관리자 기능을 실행할 수 있는가?
```

Authorization 실패 응답:

```text
HTTP 403 Forbidden
errorCode: ACCESS_DENIED
message: 접근 권한이 없습니다.
```

---

### [실무]

2026 실무 기준 Backend Authorization은 Frontend 권한 표시나 버튼 숨김에 의존하지 않는다.

권한 검증 흐름:

```text
Request
→ JWT Authentication
→ SecurityContext 저장
→ SecurityFilterChain Role / Authority 검증
→ Method Security 검증
→ Service Resource Owner Check
→ Business Authorization
→ Controller Response
```

권장:

- 단순 Role 검증은 SecurityFilterChain 또는 Method Security에서 처리한다.
- 리소스 소유자 검증은 Service에서 처리한다.
- 복잡한 비즈니스 권한은 Domain / Service 로직에서 처리한다.
- Frontend 권한 표시는 UX로만 본다.
- Backend에서 최종 Authorization을 수행한다.
- 권한 부족은 403 Forbidden으로 처리한다.

---

### [FAQ]

Q. Authorization은 뭐야?
A. 인증된 사용자가 특정 API, 리소스, 기능에 접근할 권한이 있는지 확인하는 과정이다.

Q. Authentication과 Authorization은 뭐가 달라?
A. Authentication은 사용자가 누구인지 확인하는 것이고 Authorization은 그 사용자가 접근 가능한지 확인하는 것이다.

Q. 로그인했는데도 403이 나올 수 있어?
A. 가능하다. 인증은 되었지만 Role, Authority, Resource Owner 조건을 만족하지 못하면 403이 발생한다.

Q. Frontend에서 버튼을 숨기면 권한 검증이 된 거야?
A. 아니다. Frontend 제한은 UX이고 실제 권한 검증은 Backend에서 해야 한다.

---

# 2. Role and Authority Rules

## 2.1 Role Concept

### [개념]

Role은 사용자에게 부여된 역할 기반 권한이다.

Spring Security에서는 `ROLE_USER`, `ROLE_ADMIN` 같은 Role을 사용해 API 접근 권한을 제어할 수 있다.

---

### [핵심]

Role 핵심 키워드:

- Role
- ROLE_USER
- ROLE_ADMIN
- hasRole
- GrantedAuthority
- SimpleGrantedAuthority
- Role Prefix
- Admin API
- User API

일반 Role 예:

```text
ROLE_USER
ROLE_ADMIN
ROLE_MANAGER
```

Role 사용 예:

```java
.requestMatchers("/api/admin/**").hasRole("ADMIN")
```

---

### [실무]

Role 저장 기준:

```text
User Entity
→ role = ROLE_USER 또는 ROLE_ADMIN
→ JWT Claim에 role 포함 가능
→ Principal Authorities로 변환
→ SecurityFilterChain / Method Security에서 검증
```

권장:

- Role 이름 규칙을 프로젝트 전체에서 통일한다.
- `ROLE_` prefix 사용 여부를 명확히 한다.
- DB 저장 값과 Security 설정 방식을 맞춘다.
- 관리자 기능은 `ROLE_ADMIN` 기준으로 보호한다.
- 일반 사용자 기능은 `ROLE_USER` 또는 authenticated 기준으로 보호한다.
- Role만으로 부족한 경우 Resource Owner Check를 추가한다.

예:

```java
public enum Role {
    ROLE_USER,
    ROLE_ADMIN
}
```

Authority 변환 예:

```java
List<GrantedAuthority> authorities = List.of(
        new SimpleGrantedAuthority(user.getRole().name())
);
```

---

### [FAQ]

Q. Role은 뭐야?
A. 사용자에게 부여된 역할 기반 권한이다. 예를 들어 ROLE_USER, ROLE_ADMIN이 있다.

Q. ROLE*USER와 USER는 달라?
A. Spring Security에서 Role 처리 시 `ROLE*` prefix가 관여할 수 있으므로 프로젝트 권한 이름 규칙을 통일해야 한다.

Q. 관리자 API는 Role로 보호하면 돼?
A. 기본적으로 ROLE_ADMIN 같은 Role 검증이 필요하다. 추가로 세부 권한이 있으면 Authority나 Service 검증을 보완한다.

---

## 2.2 Authority Concept

### [개념]

Authority는 사용자가 가진 구체적인 권한 문자열이다.

Role이 큰 역할 단위라면 Authority는 더 세부적인 기능 권한으로 사용할 수 있다.

---

### [핵심]

Authority 핵심 키워드:

- Authority
- GrantedAuthority
- SimpleGrantedAuthority
- hasAuthority
- POST_WRITE
- POST_DELETE
- USER_READ
- ADMIN_ACCESS
- Permission

Authority 예:

```text
ROLE_USER
ROLE_ADMIN
POST_WRITE
POST_DELETE
USER_READ
PAYMENT_READ
```

Authority 사용 예:

```java
.requestMatchers("/api/admin/**").hasAuthority("ROLE_ADMIN")
```

---

### [실무]

Authority 생성 예:

```java
List<GrantedAuthority> authorities = List.of(
        new SimpleGrantedAuthority("ROLE_USER"),
        new SimpleGrantedAuthority("POST_WRITE")
);
```

Method Security 예:

```java
@PreAuthorize("hasAuthority('POST_DELETE')")
public void deletePost(Long postId) {
}
```

권장:

- Role과 Authority 사용 기준을 분리한다.
- 단순 역할 기반은 Role로 처리한다.
- 세부 기능 권한은 Authority로 처리한다.
- 권한 문자열을 상수 또는 Enum으로 관리한다.
- 권한 이름 오타를 방지한다.
- DB 권한 값과 코드 권한 문자열을 일치시킨다.

---

### [FAQ]

Q. Authority는 뭐야?
A. 사용자가 가진 구체적인 권한 문자열이다.

Q. Role과 Authority는 뭐가 달라?
A. Role은 역할 단위 권한이고 Authority는 더 세부적인 기능 권한으로 사용할 수 있다.

Q. Authority 문자열은 어디서 관리해?
A. Enum, 상수, DB 권한 테이블 등 프로젝트 기준에 맞게 일관되게 관리해야 한다.

---

## 2.3 hasRole vs hasAuthority

### [개념]

`hasRole`은 Role 기반 검증이고, `hasAuthority`는 권한 문자열을 직접 비교하는 검증이다.

Spring Security에서 `hasRole("ADMIN")`은 일반적으로 `ROLE_ADMIN` 권한과 매칭된다.

---

### [핵심]

비교:

| 구분      | hasRole            | hasAuthority               |
| --------- | ------------------ | -------------------------- |
| 기준      | Role               | Authority 문자열           |
| Prefix    | ROLE\_ prefix 관여 | 문자열 직접 비교           |
| 예        | hasRole("ADMIN")   | hasAuthority("ROLE_ADMIN") |
| 매칭 후보 | ROLE_ADMIN         | ROLE_ADMIN                 |
| 주의      | prefix 혼동        | 문자열 오타                |

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

주의:

```text
DB 저장 권한 = ROLE_ADMIN
Security 설정 = hasRole("ROLE_ADMIN")
→ ROLE_ROLE_ADMIN으로 해석될 수 있어 오류 가능
```

권장:

- `hasRole("ADMIN")` 또는 `hasAuthority("ROLE_ADMIN")` 중 하나의 스타일을 정한다.
- DB 저장 값과 검증 방식을 통일한다.
- 문서 전체에서 Role Naming을 통일한다.
- 테스트에서 User Token / Admin Token 접근 결과를 검증한다.
- 403 발생 시 ROLE\_ prefix 불일치를 먼저 확인한다.

---

### [FAQ]

Q. hasRole과 hasAuthority는 뭐가 달라?
A. hasRole은 일반적으로 ROLE\_ prefix 처리가 관여하고 hasAuthority는 권한 문자열을 직접 비교한다.

Q. hasRole("ROLE*ADMIN")으로 써도 돼?
A. 권장하지 않는다. hasRole은 ROLE* prefix를 내부적으로 붙일 수 있으므로 hasRole("ADMIN")처럼 사용하는 것이 일반적이다.

Q. ROLE\_ prefix 때문에 403이 날 수 있어?
A. 가능하다. 저장된 권한 문자열과 hasRole / hasAuthority 사용 방식이 맞지 않으면 403이 발생할 수 있다.

---

# 3. SecurityFilterChain Authorization

## 3.1 URL Authorization Rules

### [개념]

URL Authorization은 SecurityFilterChain에서 API 경로와 HTTP Method에 따라 접근 권한을 지정하는 방식이다.

Public API, Protected API, Admin API를 경로 기준으로 분리해 기본 보안 경계를 만든다.

---

### [핵심]

URL Authorization 키워드:

- authorizeHttpRequests
- requestMatchers
- permitAll
- authenticated
- hasRole
- hasAuthority
- anyRequest
- HTTP Method
- URL Pattern

권한 설정 예:

```text
/api/auth/**      → permitAll
/api/public/**    → permitAll
/api/users/me     → authenticated
/api/admin/**     → hasRole("ADMIN")
anyRequest        → authenticated
```

---

### [실무]

SecurityFilterChain 예:

```java
.authorizeHttpRequests(auth -> auth
        .requestMatchers("/api/auth/**").permitAll()
        .requestMatchers(HttpMethod.GET, "/api/posts/**").permitAll()
        .requestMatchers(HttpMethod.POST, "/api/posts/**").authenticated()
        .requestMatchers("/api/admin/**").hasRole("ADMIN")
        .anyRequest().authenticated()
)
```

권장:

- Public API는 명시적으로만 허용한다.
- 관리자 API는 `hasRole` 또는 `hasAuthority`로 보호한다.
- 사용자 개인 데이터 API는 `authenticated`로 보호한다.
- HTTP Method별 권한을 분리한다.
- `anyRequest().authenticated()`를 마지막에 둔다.
- 넓은 `permitAll` 규칙을 피한다.

---

### [FAQ]

Q. URL Authorization은 뭐야?
A. API 경로와 HTTP Method에 따라 접근 권한을 지정하는 방식이다.

Q. GET은 공개, POST는 로그인 필요로 만들 수 있어?
A. 가능하다. HTTP Method 기준 requestMatchers를 사용하면 된다.

Q. Admin API는 URL Authorization만으로 충분해?
A. 기본 보호는 가능하지만 복잡한 관리자 기능은 Method Security나 Service 검증을 추가할 수 있다.

---

## 3.2 URL Authorization Anti Pattern

### [개념]

URL Authorization Anti Pattern은 SecurityFilterChain에서 경로 접근 규칙을 잘못 설정해 보호 API가 열리거나 관리자 API가 우회되는 문제다.

---

### [핵심]

대표 Anti Pattern:

- `/api/**` permitAll
- `anyRequest().permitAll()`
- 관리자 API permitAll
- 사용자 정보 API permitAll
- 결제 API permitAll
- 알림 API permitAll
- 넓은 matcher를 구체 matcher보다 먼저 선언
- HTTP Method 구분 누락
- 운영 Swagger 전체 공개

잘못된 예:

```java
.authorizeHttpRequests(auth -> auth
        .requestMatchers("/api/**").permitAll()
        .requestMatchers("/api/admin/**").hasRole("ADMIN")
)
```

---

### [실무]

검수 흐름:

```text
SecurityConfig 확인
→ permitAll 경로 추출
→ API 명세와 비교
→ Admin API 포함 여부 확인
→ 개인 데이터 API 포함 여부 확인
→ anyRequest 정책 확인
→ HTTP Method 권한 확인
```

수정 예:

```java
.authorizeHttpRequests(auth -> auth
        .requestMatchers("/api/auth/**").permitAll()
        .requestMatchers(HttpMethod.GET, "/api/posts/**").permitAll()
        .requestMatchers("/api/admin/**").hasRole("ADMIN")
        .anyRequest().authenticated()
)
```

권장:

- 허용 목록 방식으로 Public API를 관리한다.
- 기본 정책은 인증 필요로 둔다.
- 관리자 API는 별도 matcher로 분리한다.
- 테스트에서 Public / Protected / Admin API를 모두 확인한다.

---

### [FAQ]

Q. /api/\*\* permitAll이 왜 위험해?
A. 관리자 API, 사용자 정보 API, 결제 API까지 인증 없이 접근될 수 있기 때문이다.

Q. anyRequest().permitAll()은 개발 중이면 괜찮아?
A. 임시 테스트 외에는 위험하다. 운영 코드에 남으면 대부분의 API가 보호되지 않는다.

Q. URL Authorization 검수에서 가장 먼저 볼 것은 뭐야?
A. permitAll이 적용된 경로와 anyRequest 정책을 먼저 확인해야 한다.

---

# 4. Method Security Rules

## 4.1 Method Security Concept

### [개념]

Method Security는 Service 또는 Controller 메서드 단위로 권한 조건을 선언하는 Spring Security 기능이다.

URL 경로 기반 권한 검증만으로 부족한 경우 `@PreAuthorize`, `@PostAuthorize` 같은 Annotation을 사용해 세부 권한을 보완할 수 있다.

---

### [핵심]

Method Security 핵심 키워드:

- Method Security
- @EnableMethodSecurity
- @PreAuthorize
- @PostAuthorize
- hasRole
- hasAuthority
- principal
- SpEL
- 403 Forbidden

활성화 예:

```java
@EnableMethodSecurity
@Configuration
public class SecurityConfig {
}
```

사용 예:

```java
@PreAuthorize("hasRole('ADMIN')")
public void deleteUser(Long userId) {
}
```

---

### [실무]

Method Security 예:

```java
@PreAuthorize("hasRole('ADMIN')")
@Transactional
public void deleteNotice(Long noticeId) {
    noticeRepository.deleteById(noticeId);
}
```

Authority 기반 예:

```java
@PreAuthorize("hasAuthority('POST_DELETE')")
@Transactional
public void deletePostByAdmin(Long postId) {
    postRepository.deleteById(postId);
}
```

권장:

- 관리자 기능처럼 명확한 권한은 Method Security로 보호할 수 있다.
- URL Authorization과 중복되어도 핵심 관리자 기능은 방어적으로 보호할 수 있다.
- 복잡한 리소스 소유자 검증은 Service 내부 로직으로 처리하는 것이 명확하다.
- SpEL이 과도하게 복잡해지면 가독성과 유지보수가 나빠진다.
- Method Security 실패는 일반적으로 403으로 처리한다.

---

### [FAQ]

Q. Method Security는 뭐야?
A. 메서드 단위로 권한 조건을 선언해 접근을 제어하는 Spring Security 기능이다.

Q. @PreAuthorize는 언제 써?
A. 관리자 기능이나 특정 권한이 필요한 Service / Controller 메서드를 보호할 때 사용할 수 있다.

Q. Method Security를 쓰면 SecurityFilterChain은 필요 없어?
A. 아니다. SecurityFilterChain으로 기본 경계를 만들고 Method Security로 세부 권한을 보완하는 것이 좋다.

---

## 4.2 Method Security Anti Pattern

### [개념]

Method Security Anti Pattern은 Annotation 권한 조건을 잘못 작성하거나 과도하게 복잡한 SpEL로 비즈니스 권한을 처리해 유지보수성과 보안성을 떨어뜨리는 문제다.

---

### [핵심]

대표 Anti Pattern:

- @EnableMethodSecurity 누락
- hasRole / hasAuthority prefix 불일치
- Annotation 권한 문자열 오타
- 복잡한 Resource Owner Check를 SpEL에 과도하게 작성
- URL Authorization 없이 Method Security에만 의존
- 테스트 없이 권한 Annotation 추가
- 내부 호출로 Method Security 우회 가능성 미검토

잘못된 예:

```java
@PreAuthorize("hasRole('ROLE_ADMIN')")
public void deleteUser(Long userId) {
}
```

---

### [실무]

검수 기준:

```text
@EnableMethodSecurity 확인
→ Annotation 적용 위치 확인
→ hasRole / hasAuthority 문자열 확인
→ ROLE_ prefix 확인
→ URL Authorization과 중복 보호 확인
→ 테스트 작성 확인
```

권장:

- Role 기반 단순 권한에 사용한다.
- 복잡한 Owner Check는 Service 내부 명시적 코드로 처리한다.
- Annotation 문자열은 상수화 또는 테스트로 보완한다.
- 내부 self-invocation 구조에서는 Method Security 적용 여부를 주의한다.
- 권한 실패 테스트를 작성한다.

---

### [FAQ]

Q. @PreAuthorize가 동작하지 않으면 뭘 확인해?
A. @EnableMethodSecurity 활성화 여부, 프록시 적용 구조, 권한 문자열, ROLE\_ prefix를 확인한다.

Q. 복잡한 본인 확인 로직을 @PreAuthorize에 다 넣어도 돼?
A. 권장하지 않는다. Resource Owner Check는 Service에서 명시적으로 처리하는 것이 더 안전하고 읽기 쉽다.

Q. Method Security 실패는 401이야 403이야?
A. 인증된 사용자의 권한 부족이면 일반적으로 403 Forbidden이다.

---

# 5. Resource Owner Check

## 5.1 Resource Owner Check Concept

### [개념]

Resource Owner Check는 인증된 사용자가 특정 리소스의 소유자인지 확인하는 인가 검증이다.

Role 기반 권한만으로는 "내 게시글", "내 댓글", "내 알림", "내 결제 내역" 같은 사용자별 리소스 접근을 안전하게 제어할 수 없다.

---

### [핵심]

Resource Owner Check 대상:

- 내 게시글 수정 / 삭제
- 내 댓글 수정 / 삭제
- 내 정보 수정
- 내 알림 조회
- 내 결제 내역 조회
- 내 찜 목록 조회
- 내 주문 내역 조회
- 내 파일 삭제
- 내 리뷰 수정 / 삭제

핵심 기준:

- currentUserId는 Principal에서 가져온다.
- RequestBody userId를 신뢰하지 않는다.
- Service에서 리소스 조회 후 소유자 검증한다.
- 소유자가 아니면 403 Forbidden 처리한다.
- 관리자 예외 정책은 명확히 한다.

---

### [실무]

Resource Owner Check Flow:

```text
Request
→ JWT 인증
→ Principal에서 currentUserId 추출
→ Service 호출
→ Resource 조회
→ resource.ownerId와 currentUserId 비교
→ 일치하면 처리
→ 불일치하면 403 Forbidden
```

Service 예:

```java
@Transactional
public void updatePost(
        Long postId,
        Long currentUserId,
        PostUpdateRequest request
) {
    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException(
                    "POST_NOT_FOUND",
                    "게시글을 찾을 수 없습니다."
            ));

    if (!post.isOwner(currentUserId)) {
        throw new AccessDeniedException("접근 권한이 없습니다.");
    }

    post.update(request.title(), request.content());
}
```

Entity 예:

```java
public boolean isOwner(Long userId) {
    return this.user.getId().equals(userId);
}
```

---

### [FAQ]

Q. Resource Owner Check는 뭐야?
A. 인증된 사용자가 특정 리소스의 소유자인지 확인하는 인가 검증이다.

Q. 내 게시글 수정 권한은 Role로만 보면 돼?
A. 아니다. 사용자가 해당 게시글의 소유자인지 Service에서 Resource Owner Check를 해야 한다.

Q. 본인 리소스 검증은 어디서 해?
A. 리소스를 조회하고 비즈니스 규칙을 판단하는 Service에서 처리하는 것이 일반적이다.

---

## 5.2 Principal Based Owner Check

### [개념]

Principal Based Owner Check는 현재 인증된 사용자의 userId를 SecurityContext 또는 `@AuthenticationPrincipal`에서 가져와 리소스 소유자 검증에 사용하는 방식이다.

Client가 전달한 userId는 조작 가능하므로 소유자 검증 기준으로 사용하면 안 된다.

---

### [핵심]

사용 기준:

- `@AuthenticationPrincipal`
- CustomUserPrincipal
- SecurityContextHolder
- currentUserId
- authenticated user
- ownerId

금지 기준:

- RequestBody userId 신뢰
- RequestParam userId 신뢰
- PathVariable userId만으로 본인 검증
- Frontend 로그인 상태 신뢰
- JWT Payload 검증 없이 userId 사용

---

### [실무]

Controller 예:

```java
@PutMapping("/api/posts/{postId}")
public ApiResponse<Void> updatePost(
        @AuthenticationPrincipal CustomUserPrincipal principal,
        @PathVariable Long postId,
        @RequestBody PostUpdateRequest request
) {
    postService.updatePost(postId, principal.userId(), request);
    return ApiResponse.success();
}
```

잘못된 예:

```java
@PutMapping("/api/posts/{postId}")
public ApiResponse<Void> updatePost(
        @PathVariable Long postId,
        @RequestBody PostUpdateRequest request
) {
    postService.updatePost(postId, request.userId(), request);
    return ApiResponse.success();
}
```

문제:

```text
request.userId는 Client가 조작할 수 있다.
다른 사용자의 userId를 넣어 권한 우회가 가능하다.
```

권장:

- Controller에서 Principal userId를 Service로 전달한다.
- Service에서 Resource Owner Check를 수행한다.
- RequestBody에는 userId를 포함하지 않는다.
- 포함되어 있더라도 권한 판단에 사용하지 않는다.
- PathVariable userId가 필요한 API도 Principal과 비교한다.

---

### [FAQ]

Q. userId를 요청으로 받아서 본인 확인하면 안 돼?
A. 안 된다. 사용자가 조작할 수 있으므로 인증 Principal의 userId를 기준으로 검증해야 한다.

Q. @AuthenticationPrincipal은 왜 써?
A. SecurityContext에 저장된 인증 사용자 정보를 안전하게 가져오기 위해 사용한다.

Q. PathVariable userId는 믿어도 돼?
A. 단독으로 신뢰하면 안 된다. Principal userId와 비교하거나 관리자 권한을 확인해야 한다.

---

## 5.3 Admin Override Rules

### [개념]

Admin Override는 일반 사용자는 자신의 리소스만 접근할 수 있지만 관리자는 예외적으로 전체 리소스에 접근할 수 있도록 허용하는 정책이다.

관리자 예외는 명확한 규칙으로 작성해야 하며 무분별하게 허용하면 권한 과잉 문제가 발생한다.

---

### [핵심]

Admin Override 사용 후보:

- 관리자 게시글 삭제
- 신고 게시글 조치
- 사용자 계정 정지
- 리뷰 블라인드 처리
- 공지 강제 수정
- 운영 데이터 조회

검증 기준:

- owner check 통과
- 또는 ROLE_ADMIN 보유
- 관리자 행위 로그 기록
- 관리자 권한 범위 제한

---

### [실무]

예:

```java
@Transactional
public void deletePost(
        Long postId,
        CustomUserPrincipal principal
) {
    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException(
                    "POST_NOT_FOUND",
                    "게시글을 찾을 수 없습니다."
            ));

    boolean owner = post.isOwner(principal.userId());
    boolean admin = principal.hasRole("ROLE_ADMIN");

    if (!owner && !admin) {
        throw new AccessDeniedException("접근 권한이 없습니다.");
    }

    post.delete();
}
```

권장:

- 관리자 예외 허용 여부를 기능별로 명확히 정한다.
- 관리자 작업은 Audit Log를 남길 수 있다.
- 관리자 권한도 최소 권한 원칙을 따른다.
- 일반 API와 관리자 API를 분리하는 것이 더 명확할 수 있다.
- 관리자 Override가 필요한 이유를 도메인 정책에 기록한다.

---

### [FAQ]

Q. 관리자는 모든 사용자 리소스를 수정해도 돼?
A. 프로젝트 정책에 따라 다르다. 필요한 기능만 명시적으로 허용하고 Audit Log를 검토하는 것이 좋다.

Q. Owner Check에 관리자 예외를 넣어도 돼?
A. 가능하다. 다만 기능별로 허용 여부를 명확히 하고 권한 과잉을 피해야 한다.

Q. 관리자 기능은 별도 API로 분리하는 게 좋아?
A. 운영 기능이 많다면 `/api/admin/**`처럼 분리하는 것이 접근 제어와 감사 추적에 유리하다.

---

# 6. Domain Authorization Rules

## 6.1 Business Authorization Concept

### [개념]

Business Authorization은 단순 Role이나 Owner Check만으로 판단할 수 없는 도메인 규칙 기반 권한 검증이다.

리소스 상태, 참여 여부, 결제 상태, 기간, 승인 상태, 팀 소속 여부 같은 비즈니스 조건을 함께 확인한다.

---

### [핵심]

Business Authorization 후보:

- 게시글 작성 가능 상태
- 댓글 작성 허용 여부
- 축제 종료 후 리뷰 작성 가능 여부
- 결제 완료 사용자만 접근
- 팀 멤버만 프로젝트 접근
- 승인된 사용자만 기능 사용
- 정지 사용자의 작성 제한
- 기간 종료 후 수정 금지
- 소유자지만 삭제 불가 상태

검증 위치:

- Service
- Domain Method
- Policy Class
- Authorization Service

---

### [실무]

예:

```java
@Transactional
public void writeReview(
        Long festivalId,
        Long currentUserId,
        ReviewCreateRequest request
) {
    Festival festival = festivalRepository.findById(festivalId)
            .orElseThrow(() -> new BusinessException(
                    "FESTIVAL_NOT_FOUND",
                    "축제를 찾을 수 없습니다."
            ));

    if (!festival.isReviewAllowed()) {
        throw new BusinessException(
                "REVIEW_NOT_ALLOWED",
                "리뷰 작성이 허용되지 않습니다."
        );
    }

    if (reviewRepository.existsByFestivalIdAndUserId(festivalId, currentUserId)) {
        throw new BusinessException(
                "REVIEW_ALREADY_EXISTS",
                "이미 리뷰를 작성했습니다."
        );
    }

    reviewRepository.save(Review.create(festival, currentUserId, request));
}
```

권장:

- 단순 권한과 비즈니스 권한을 구분한다.
- 도메인 상태 기반 검증은 Service 또는 Domain Method에서 처리한다.
- 실패 응답은 403 또는 도메인 예외를 정책에 맞게 선택한다.
- 권한 부족인지 상태 불가인지 errorCode를 구분한다.
- Review Agent는 권한 검증 누락 여부를 확인한다.

---

### [FAQ]

Q. Business Authorization은 뭐야?
A. Role이나 Owner Check만으로 부족한 도메인 상태 기반 권한 검증이다.

Q. 소유자면 항상 수정 가능해?
A. 아니다. 리소스 상태나 기간 정책에 따라 소유자라도 수정이 제한될 수 있다.

Q. 비즈니스 권한 검증은 어디서 해?
A. 일반적으로 Service, Domain Method, Policy Class에서 처리한다.

---

## 6.2 Policy Class Rules

### [개념]

Policy Class는 복잡한 권한 조건을 별도 클래스로 분리해 재사용성과 가독성을 높이는 방식이다.

권한 조건이 여러 Service에서 반복되거나 복잡해질 때 사용할 수 있다.

---

### [핵심]

Policy Class 사용 후보:

- 게시글 수정 권한
- 프로젝트 멤버 권한
- 관리자 Override
- 결제 접근 권한
- 리뷰 작성 가능 여부
- 팀 소속 검증
- 상태 기반 수정 제한

구성 후보:

- AuthorizationPolicy
- PostPolicy
- ReviewPolicy
- PaymentAccessPolicy
- ProjectMemberPolicy

---

### [실무]

Policy 예:

```java
@Component
public class PostAuthorizationPolicy {

    public boolean canUpdate(Post post, CustomUserPrincipal principal) {
        return post.isOwner(principal.userId())
                || principal.hasRole("ROLE_ADMIN");
    }

    public void validateCanUpdate(Post post, CustomUserPrincipal principal) {
        if (!canUpdate(post, principal)) {
            throw new AccessDeniedException("접근 권한이 없습니다.");
        }
    }
}
```

Service 사용 예:

```java
@Transactional
public void updatePost(
        Long postId,
        CustomUserPrincipal principal,
        PostUpdateRequest request
) {
    Post post = postRepository.findById(postId)
            .orElseThrow(() -> new BusinessException(
                    "POST_NOT_FOUND",
                    "게시글을 찾을 수 없습니다."
            ));

    postAuthorizationPolicy.validateCanUpdate(post, principal);

    post.update(request.title(), request.content());
}
```

권장:

- 권한 조건이 반복되면 Policy Class로 분리한다.
- Policy는 권한 판단에 집중한다.
- DB 조회는 Service에서 하고 Policy에는 도메인 객체를 전달하는 방식이 명확하다.
- 예외를 던지는 메서드와 boolean 반환 메서드를 구분할 수 있다.
- Policy 이름은 도메인 기준으로 명확히 작성한다.

---

### [FAQ]

Q. Policy Class는 언제 써?
A. 권한 조건이 복잡하거나 여러 Service에서 반복될 때 사용한다.

Q. Policy Class에서 DB 조회를 해도 돼?
A. 가능하지만 Service에서 리소스를 조회하고 Policy는 판단만 하게 분리하면 테스트와 가독성이 좋아진다.

Q. Resource Owner Check도 Policy로 분리할 수 있어?
A. 가능하다. 특히 관리자 예외나 상태 조건이 함께 있으면 Policy Class가 유용하다.

---

# 7. Authorization Error Handling

## 7.1 AccessDeniedException Rules

### [개념]

`AccessDeniedException`은 인증된 사용자가 권한이 부족해 접근할 수 없을 때 사용하는 Spring Security 인가 실패 예외다.

일반적으로 AccessDeniedHandler에서 403 Forbidden 응답으로 변환된다.

---

### [핵심]

사용 상황:

- Role 부족
- Authority 부족
- Resource Owner Check 실패
- 관리자 권한 없음
- Method Security 실패
- 본인 리소스 아님

권장 응답:

```text
HTTP 403 Forbidden
errorCode: ACCESS_DENIED
message: 접근 권한이 없습니다.
```

---

### [실무]

예:

```java
if (!post.isOwner(currentUserId)) {
    throw new AccessDeniedException("접근 권한이 없습니다.");
}
```

AccessDeniedHandler 예:

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

- 권한 부족은 403으로 처리한다.
- 인증 실패와 권한 실패를 구분한다.
- 리소스 존재 여부를 과도하게 노출하지 않는다.
- 관리자 API 실패도 403으로 처리한다.
- 응답 형식은 API 공통 에러 형식과 맞춘다.

---

### [FAQ]

Q. 권한이 부족하면 어떤 예외를 던져?
A. Spring Security 기준으로 AccessDeniedException을 사용할 수 있다.

Q. AccessDeniedException은 몇 번 응답이야?
A. 인증은 되었지만 권한이 부족한 상태이므로 일반적으로 403 Forbidden이다.

Q. 리소스 소유자가 아니면 401이야 403이야?
A. 인증된 사용자가 권한이 없는 것이므로 일반적으로 403이다.

---

## 7.2 403 Response Rules

### [개념]

403 Forbidden 응답은 인증은 되었지만 권한이 부족한 상태를 Client에 전달하는 인가 실패 응답이다.

Frontend는 403 응답을 받으면 권한 없음 안내, 접근 차단, 관리자 권한 필요 메시지 등을 처리할 수 있다.

---

### [핵심]

403 발생 원인:

- Role 부족
- Authority 부족
- Resource Owner Check 실패
- Method Security 실패
- 관리자 API 접근 실패
- 비즈니스 권한 부족

응답 필드 후보:

- status
- errorCode
- message
- timestamp
- path

---

### [실무]

권장 응답:

```json
{
  "status": 403,
  "errorCode": "ACCESS_DENIED",
  "message": "접근 권한이 없습니다."
}
```

Resource Owner 실패 응답:

```json
{
  "status": 403,
  "errorCode": "RESOURCE_ACCESS_DENIED",
  "message": "해당 리소스에 접근할 권한이 없습니다."
}
```

주의:

- 403 응답에 내부 권한 구조를 상세히 노출하지 않는다.
- "관리자 권한이 없음", "소유자가 아님" 같은 메시지는 정책에 따라 조절한다.
- 리소스 존재 여부를 숨기고 싶다면 404 처리 전략도 검토할 수 있다.
- 401과 403 errorCode를 분리한다.
- Frontend는 403을 재로그인으로만 처리하지 않는다.

---

### [FAQ]

Q. 403 응답은 언제 사용해?
A. 인증은 되었지만 해당 기능이나 리소스에 접근할 권한이 없을 때 사용한다.

Q. 403이 오면 Frontend는 재로그인하면 돼?
A. 아니다. 403은 권한 부족이므로 재로그인보다 권한 없음 안내나 접근 차단 처리가 맞다.

Q. 리소스 존재 여부를 숨기고 싶으면 어떻게 해?
A. 보안 정책에 따라 403 대신 404로 응답하는 전략을 검토할 수 있다.

---

# 8. Authorization Testing

## 8.1 Role Authorization Test Rules

### [개념]

Role Authorization Test는 Role 기반 API 접근 제어가 의도대로 동작하는지 검증하는 테스트다.

일반 User Token과 Admin Token을 구분해 Protected API와 Admin API 접근 결과를 확인한다.

---

### [핵심]

테스트 대상:

- Public API
- Protected API
- Admin API
- User Token
- Admin Token
- No Token
- Invalid Token
- Role Prefix
- hasRole / hasAuthority

기본 시나리오:

```text
No Token to Protected API
→ 401 Unauthorized

User Token to User API
→ 200 OK

User Token to Admin API
→ 403 Forbidden

Admin Token to Admin API
→ 200 OK
```

---

### [실무]

테스트 체크:

```text
Admin API 호출
→ User Token 사용
→ 403 확인
→ Admin Token 사용
→ 200 확인
```

MockMvc 예:

```java
@Test
void userTokenCannotAccessAdminApi() throws Exception {
    mockMvc.perform(delete("/api/admin/users/1")
                    .header("Authorization", "Bearer " + userAccessToken))
            .andExpect(status().isForbidden());
}
```

권장:

- User / Admin Token을 모두 준비한다.
- 401과 403을 구분해 검증한다.
- Role prefix 불일치 케이스를 확인한다.
- hasRole / hasAuthority 설정과 DB 저장 권한을 비교한다.
- 관리자 API 전체에 테스트를 적용한다.

---

### [FAQ]

Q. Role 권한 테스트에서 뭘 봐야 해?
A. User Token으로 Admin API 접근 시 403, Admin Token으로 접근 시 200이 나오는지 확인한다.

Q. Token이 없으면 403이야?
A. 아니다. 인증 정보가 없으면 401이고, 인증은 되었지만 권한이 부족하면 403이다.

Q. ROLE\_ prefix 테스트도 필요해?
A. 필요하다. prefix 불일치로 권한이 있어도 403이 발생할 수 있다.

---

## 8.2 Resource Owner Test Rules

### [개념]

Resource Owner Test는 인증된 사용자가 본인 리소스에는 접근 가능하고 타인 리소스에는 접근할 수 없는지 검증하는 테스트다.

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

기본 시나리오:

```text
Owner Token + Owner Resource
→ 200 OK

Other User Token + Owner Resource
→ 403 Forbidden

No Token + Owner Resource
→ 401 Unauthorized
```

---

### [실무]

테스트 예:

```java
@Test
void userCannotUpdateOtherUserPost() throws Exception {
    mockMvc.perform(put("/api/posts/{postId}", otherUserPostId)
                    .header("Authorization", "Bearer " + userAccessToken)
                    .contentType(MediaType.APPLICATION_JSON)
                    .content("""
                            {
                              "title": "changed",
                              "content": "changed"
                            }
                            """))
            .andExpect(status().isForbidden());
}
```

검증 기준:

- Service에서 Owner Check가 수행되는가?
- currentUserId는 Principal 기준인가?
- RequestBody userId 조작이 무시되는가?
- 타인 리소스 접근이 403으로 차단되는가?
- 관리자 예외가 정책대로 동작하는가?

---

### [FAQ]

Q. Resource Owner 테스트는 왜 필요해?
A. 로그인한 사용자가 타인 리소스를 수정하거나 조회하는 권한 우회를 막기 위해 필요하다.

Q. RequestBody userId 조작 테스트도 해야 해?
A. 해야 한다. Client가 userId를 조작해도 Principal 기준으로 처리되는지 확인해야 한다.

Q. 타인 게시글 수정 시 어떤 응답이 맞아?
A. 인증은 되었지만 소유자가 아니므로 일반적으로 403 Forbidden이 맞다.

---

# 9. Authorization Anti Pattern

## 9.1 Common Authorization Mistakes

### [개념]

Authorization Anti Pattern은 인증된 사용자라는 이유만으로 모든 리소스 접근을 허용하거나 Frontend 권한 표시만 신뢰하는 잘못된 권한 검증 방식이다.

---

### [핵심]

대표 Anti Pattern:

- 로그인만 확인하고 Owner Check 생략
- Frontend 버튼 숨김만 믿음
- RequestBody userId 신뢰
- PathVariable userId 단독 신뢰
- 모든 Protected API를 authenticated만 적용
- Admin API에 Role 검증 없음
- hasRole / hasAuthority prefix 불일치
- Method Security 활성화 누락
- 복잡한 권한을 Controller에 분산
- Service 권한 검증 누락
- 관리자 Override 무분별 허용
- 권한 실패를 401로 처리
- 403 응답에 내부 권한 구조 노출

---

### [실무]

잘못된 예:

```java
@Transactional
public void updatePost(Long postId, PostUpdateRequest request) {
    Post post = postRepository.findById(postId)
            .orElseThrow();

    post.update(request.title(), request.content());
}
```

문제:

```text
로그인 사용자 여부만 확인하고 게시글 소유자 검증이 없다.
타인의 게시글을 수정할 수 있다.
```

수정 예:

```java
@Transactional
public void updatePost(
        Long postId,
        Long currentUserId,
        PostUpdateRequest request
) {
    Post post = postRepository.findById(postId)
            .orElseThrow();

    if (!post.isOwner(currentUserId)) {
        throw new AccessDeniedException("접근 권한이 없습니다.");
    }

    post.update(request.title(), request.content());
}
```

Review 우선순위:

```text
Admin API Role 확인
→ authenticated만으로 충분한지 확인
→ Resource Owner Check 확인
→ RequestBody userId 사용 여부 확인
→ Method Security 활성화 확인
→ 401 / 403 분리 확인
```

---

### [FAQ]

Q. Authorization에서 가장 위험한 실수는 뭐야?
A. 로그인만 확인하고 리소스 소유자 검증을 생략하는 것이다.

Q. authenticated만 걸면 충분해?
A. 사용자 개인 리소스나 관리자 기능에는 충분하지 않다. Role 또는 Resource Owner Check가 필요하다.

Q. 권한 실패를 401로 처리해도 돼?
A. 인증된 사용자의 권한 부족은 403으로 처리하는 것이 일반적이다.

---

# 10. Part05 Checklist

## 10.1 Authorization Checklist

### [개념]

Part05 Checklist는 Authorization, Role, Authority, Method Security, Resource Owner Check가 Security Advanced 기준에 맞게 설계되었는지 검수하기 위한 목록이다.

---

### [핵심]

Checklist:

```md
- [ ] Authentication과 Authorization이 구분되었는가?
- [ ] Role naming 규칙이 통일되었는가?
- [ ] ROLE\_ prefix 정책이 명확한가?
- [ ] hasRole / hasAuthority 사용 기준이 정해졌는가?
- [ ] Admin API에 Role 또는 Authority 검증이 적용되었는가?
- [ ] URL Authorization이 Public / Protected / Admin API를 분리하는가?
- [ ] 넓은 permitAll 규칙이 없는가?
- [ ] Method Security가 필요한 기능에 적용되었는가?
- [ ] @EnableMethodSecurity가 활성화되었는가?
- [ ] Resource Owner Check가 필요한 기능에 적용되었는가?
- [ ] currentUserId를 Principal에서 가져오는가?
- [ ] RequestBody userId를 신뢰하지 않는가?
- [ ] PathVariable userId 단독으로 본인 검증하지 않는가?
- [ ] 관리자 Override 정책이 명확한가?
- [ ] Business Authorization이 필요한 도메인 조건을 검증하는가?
- [ ] Policy Class 분리가 필요한 복잡도인지 검토했는가?
- [ ] 권한 부족을 403으로 처리하는가?
- [ ] AccessDeniedHandler 응답 형식이 통일되었는가?
- [ ] Role Authorization Test가 있는가?
- [ ] Resource Owner Test가 있는가?
- [ ] Retrieval Queries가 충분한가?
```

---

### [실무]

Review Flow:

```text
SecurityFilterChain 권한 규칙 확인
→ Role / Authority 문자열 확인
→ Method Security 확인
→ Controller Principal 사용 확인
→ Service Resource Owner Check 확인
→ Business Authorization 확인
→ 403 Error Response 확인
→ Authorization Test 확인
```

선행 문서 연결:

```text
Part01 Core Concepts
→ Authentication / Authorization / Principal / 401 / 403 기준 제공

Part02 SecurityFilterChain
→ URL Authorization / requestMatchers / Admin API 기준 제공

Part04 JWT
→ JWT Claim role / SecurityContext Authentication 기준 제공
```

후속 문서 연결:

```text
Part05 Authorization Resource Owner Check
→ Part06 Exception Handling CORS CSRF
→ Part08 Security Testing Troubleshooting
```

---

### [FAQ]

Q. Part05에서 가장 중요한 검수 포인트는 뭐야?
A. Role / Authority 규칙, Admin API 보호, Principal 기반 Resource Owner Check, 403 응답 처리다.

Q. Part05는 JWT 문서와 어떻게 연결돼?
A. JWT Claim에서 role을 가져와 Authentication의 Authority로 변환하고 Authorization에 사용한다.

Q. Part05는 Testing 문서와 어떻게 연결돼?
A. User Token, Admin Token, Owner Resource, Other User Resource 테스트로 권한 정책을 검증한다.

---

# Retrieval Queries

### [FAQ]

Q. Authorization은 뭐야?
A. 인증된 사용자가 특정 API, 리소스, 기능에 접근할 권한이 있는지 확인하는 과정이다.

Q. Authentication과 Authorization은 뭐가 달라?
A. Authentication은 사용자가 누구인지 확인하는 것이고 Authorization은 그 사용자가 접근 가능한지 확인하는 것이다.

Q. 로그인했는데도 403이 나올 수 있어?
A. 가능하다. 인증은 되었지만 Role, Authority, Resource Owner 조건을 만족하지 못하면 403이 발생한다.

Q. Frontend에서 버튼을 숨기면 권한 검증이 된 거야?
A. 아니다. Frontend 제한은 UX이고 실제 권한 검증은 Backend에서 해야 한다.

Q. Role은 뭐야?
A. 사용자에게 부여된 역할 기반 권한이다. 예를 들어 ROLE_USER, ROLE_ADMIN이 있다.

Q. ROLE*USER와 USER는 달라?
A. Spring Security에서 Role 처리 시 `ROLE*` prefix가 관여할 수 있으므로 프로젝트 권한 이름 규칙을 통일해야 한다.

Q. 관리자 API는 Role로 보호하면 돼?
A. 기본적으로 ROLE_ADMIN 같은 Role 검증이 필요하다. 추가로 세부 권한이 있으면 Authority나 Service 검증을 보완한다.

Q. Authority는 뭐야?
A. 사용자가 가진 구체적인 권한 문자열이다.

Q. Role과 Authority는 뭐가 달라?
A. Role은 역할 단위 권한이고 Authority는 더 세부적인 기능 권한으로 사용할 수 있다.

Q. Authority 문자열은 어디서 관리해?
A. Enum, 상수, DB 권한 테이블 등 프로젝트 기준에 맞게 일관되게 관리해야 한다.

Q. hasRole과 hasAuthority는 뭐가 달라?
A. hasRole은 일반적으로 ROLE\_ prefix 처리가 관여하고 hasAuthority는 권한 문자열을 직접 비교한다.

Q. hasRole("ROLE*ADMIN")으로 써도 돼?
A. 권장하지 않는다. hasRole은 ROLE* prefix를 내부적으로 붙일 수 있으므로 hasRole("ADMIN")처럼 사용하는 것이 일반적이다.

Q. ROLE\_ prefix 때문에 403이 날 수 있어?
A. 가능하다. 저장된 권한 문자열과 hasRole / hasAuthority 사용 방식이 맞지 않으면 403이 발생할 수 있다.

Q. URL Authorization은 뭐야?
A. API 경로와 HTTP Method에 따라 접근 권한을 지정하는 방식이다.

Q. GET은 공개, POST는 로그인 필요로 만들 수 있어?
A. 가능하다. HTTP Method 기준 requestMatchers를 사용하면 된다.

Q. Admin API는 URL Authorization만으로 충분해?
A. 기본 보호는 가능하지만 복잡한 관리자 기능은 Method Security나 Service 검증을 추가할 수 있다.

Q. /api/\*\* permitAll이 왜 위험해?
A. 관리자 API, 사용자 정보 API, 결제 API까지 인증 없이 접근될 수 있기 때문이다.

Q. anyRequest().permitAll()은 개발 중이면 괜찮아?
A. 임시 테스트 외에는 위험하다. 운영 코드에 남으면 대부분의 API가 보호되지 않는다.

Q. URL Authorization 검수에서 가장 먼저 볼 것은 뭐야?
A. permitAll이 적용된 경로와 anyRequest 정책을 먼저 확인해야 한다.

Q. Method Security는 뭐야?
A. 메서드 단위로 권한 조건을 선언해 접근을 제어하는 Spring Security 기능이다.

Q. @PreAuthorize는 언제 써?
A. 관리자 기능이나 특정 권한이 필요한 Service / Controller 메서드를 보호할 때 사용할 수 있다.

Q. Method Security를 쓰면 SecurityFilterChain은 필요 없어?
A. 아니다. SecurityFilterChain으로 기본 경계를 만들고 Method Security로 세부 권한을 보완하는 것이 좋다.

Q. @PreAuthorize가 동작하지 않으면 뭘 확인해?
A. @EnableMethodSecurity 활성화 여부, 프록시 적용 구조, 권한 문자열, ROLE\_ prefix를 확인한다.

Q. 복잡한 본인 확인 로직을 @PreAuthorize에 다 넣어도 돼?
A. 권장하지 않는다. Resource Owner Check는 Service에서 명시적으로 처리하는 것이 더 안전하고 읽기 쉽다.

Q. Method Security 실패는 401이야 403이야?
A. 인증된 사용자의 권한 부족이면 일반적으로 403 Forbidden이다.

Q. Resource Owner Check는 뭐야?
A. 인증된 사용자가 특정 리소스의 소유자인지 확인하는 인가 검증이다.

Q. 내 게시글 수정 권한은 Role로만 보면 돼?
A. 아니다. 사용자가 해당 게시글의 소유자인지 Service에서 Resource Owner Check를 해야 한다.

Q. 본인 리소스 검증은 어디서 해?
A. 리소스를 조회하고 비즈니스 규칙을 판단하는 Service에서 처리하는 것이 일반적이다.

Q. userId를 요청으로 받아서 본인 확인하면 안 돼?
A. 안 된다. 사용자가 조작할 수 있으므로 인증 Principal의 userId를 기준으로 검증해야 한다.

Q. @AuthenticationPrincipal은 왜 써?
A. SecurityContext에 저장된 인증 사용자 정보를 안전하게 가져오기 위해 사용한다.

Q. PathVariable userId는 믿어도 돼?
A. 단독으로 신뢰하면 안 된다. Principal userId와 비교하거나 관리자 권한을 확인해야 한다.

Q. 관리자는 모든 사용자 리소스를 수정해도 돼?
A. 프로젝트 정책에 따라 다르다. 필요한 기능만 명시적으로 허용하고 Audit Log를 검토하는 것이 좋다.

Q. Owner Check에 관리자 예외를 넣어도 돼?
A. 가능하다. 다만 기능별로 허용 여부를 명확히 하고 권한 과잉을 피해야 한다.

Q. 관리자 기능은 별도 API로 분리하는 게 좋아?
A. 운영 기능이 많다면 `/api/admin/**`처럼 분리하는 것이 접근 제어와 감사 추적에 유리하다.

Q. Business Authorization은 뭐야?
A. Role이나 Owner Check만으로 부족한 도메인 상태 기반 권한 검증이다.

Q. 소유자면 항상 수정 가능해?
A. 아니다. 리소스 상태나 기간 정책에 따라 소유자라도 수정이 제한될 수 있다.

Q. 비즈니스 권한 검증은 어디서 해?
A. 일반적으로 Service, Domain Method, Policy Class에서 처리한다.

Q. Policy Class는 언제 써?
A. 권한 조건이 복잡하거나 여러 Service에서 반복될 때 사용한다.

Q. Policy Class에서 DB 조회를 해도 돼?
A. 가능하지만 Service에서 리소스를 조회하고 Policy는 판단만 하게 분리하면 테스트와 가독성이 좋아진다.

Q. Resource Owner Check도 Policy로 분리할 수 있어?
A. 가능하다. 특히 관리자 예외나 상태 조건이 함께 있으면 Policy Class가 유용하다.

Q. 권한이 부족하면 어떤 예외를 던져?
A. Spring Security 기준으로 AccessDeniedException을 사용할 수 있다.

Q. AccessDeniedException은 몇 번 응답이야?
A. 인증은 되었지만 권한이 부족한 상태이므로 일반적으로 403 Forbidden이다.

Q. 리소스 소유자가 아니면 401이야 403이야?
A. 인증된 사용자가 권한이 없는 것이므로 일반적으로 403이다.

Q. 403 응답은 언제 사용해?
A. 인증은 되었지만 해당 기능이나 리소스에 접근할 권한이 없을 때 사용한다.

Q. 403이 오면 Frontend는 재로그인하면 돼?
A. 아니다. 403은 권한 부족이므로 재로그인보다 권한 없음 안내나 접근 차단 처리가 맞다.

Q. 리소스 존재 여부를 숨기고 싶으면 어떻게 해?
A. 보안 정책에 따라 403 대신 404로 응답하는 전략을 검토할 수 있다.

Q. Role 권한 테스트에서 뭘 봐야 해?
A. User Token으로 Admin API 접근 시 403, Admin Token으로 접근 시 200이 나오는지 확인한다.

Q. Token이 없으면 403이야?
A. 아니다. 인증 정보가 없으면 401이고, 인증은 되었지만 권한이 부족하면 403이다.

Q. ROLE\_ prefix 테스트도 필요해?
A. 필요하다. prefix 불일치로 권한이 있어도 403이 발생할 수 있다.

Q. Resource Owner 테스트는 왜 필요해?
A. 로그인한 사용자가 타인 리소스를 수정하거나 조회하는 권한 우회를 막기 위해 필요하다.

Q. RequestBody userId 조작 테스트도 해야 해?
A. 해야 한다. Client가 userId를 조작해도 Principal 기준으로 처리되는지 확인해야 한다.

Q. 타인 게시글 수정 시 어떤 응답이 맞아?
A. 인증은 되었지만 소유자가 아니므로 일반적으로 403 Forbidden이 맞다.

Q. Authorization에서 가장 위험한 실수는 뭐야?
A. 로그인만 확인하고 리소스 소유자 검증을 생략하는 것이다.

Q. authenticated만 걸면 충분해?
A. 사용자 개인 리소스나 관리자 기능에는 충분하지 않다. Role 또는 Resource Owner Check가 필요하다.

Q. 권한 실패를 401로 처리해도 돼?
A. 인증된 사용자의 권한 부족은 403으로 처리하는 것이 일반적이다.

Q. Part05에서 가장 중요한 검수 포인트는 뭐야?
A. Role / Authority 규칙, Admin API 보호, Principal 기반 Resource Owner Check, 403 응답 처리다.

Q. Part05는 JWT 문서와 어떻게 연결돼?
A. JWT Claim에서 role을 가져와 Authentication의 Authority로 변환하고 Authorization에 사용한다.

Q. Part05는 Testing 문서와 어떻게 연결돼?
A. User Token, Admin Token, Owner Resource, Other User Resource 테스트로 권한 정책을 검증한다.
